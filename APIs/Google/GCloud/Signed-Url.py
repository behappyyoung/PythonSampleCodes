import base64
import datetime
import hashlib
# import md5
import time
import Crypto.Hash.SHA256 as SHA256
import Crypto.PublicKey.RSA as RSA
import Crypto.Signature.PKCS1_v1_5 as PKCS1_v1_5
import requests


class CloudStorageURLSigner(object):

  def __init__(self, key, client_id_email, gcs_api_endpoint, expiration=10,
               session=None):
    self.key = RSA.importKey(key)
    self.client_id_email = client_id_email
    self.gcs_api_endpoint = gcs_api_endpoint

    self.expiration = (datetime.datetime.now() + datetime.timedelta(days=expiration))
    self.expiration = int(time.mktime(self.expiration.timetuple()))
    self.session = session or requests.Session()

  def _Base64Sign(self, plaintext):
    shahash = SHA256.new(plaintext)
    signer = PKCS1_v1_5.new(self.key)
    signature_bytes = signer.sign(shahash)
    return base64.b64encode(signature_bytes)

  def _MakeSignatureString(self, verb, path, content_md5, content_type):
    """Creates the signature string for signing according to GCS docs."""
    signature_string = ('{verb}\n'
                        '{content_md5}\n'
                        '{content_type}\n'
                        '{expiration}\n'
                        '{resource}')
    return signature_string.format(verb=verb,
                                   content_md5=content_md5,
                                   content_type=content_type,
                                   expiration=self.expiration,
                                   resource=path)

  def _MakeUrl(self, verb, path, content_type='', content_md5=''):
    """Forms and returns the full signed URL to access GCS."""
    base_url = '%s%s' % (self.gcs_api_endpoint, path)
    signature_string = self._MakeSignatureString(verb, path, content_md5,
                                                 content_type).encode('utf-8')
    print('signature string', signature_string)
    # signature_string = signature_string.encode('utf-8')
    signature_signed = self._Base64Sign(signature_string)
    query_params = {'GoogleAccessId': self.client_id_email,
                    'Expires': str(self.expiration),
                    'Signature': signature_signed}
    return base_url, query_params

  def Get(self, path):
    """Performs a GET request.
    Args:
      path: The relative API path to access, e.g. '/bucket/object'.
    Returns:
      An instance of requests.Response containing the HTTP response.
    """
    base_url, query_params = self._MakeUrl('GET', path)
    print(base_url, query_params)
    return self.session.get(base_url, params=query_params)

  def Put(self, path, content_type, data):
    """Performs a PUT request.
    Args:
      path: The relative API path to access, e.g. '/bucket/object'.
      content_type: The content type to assign to the upload.
      data: The file data to upload to the new file.
    Returns:
      An instance of requests.Response containing the HTTP response.
    """
    md5_digest = base64.b64encode(hashlib.md5.new(data).digest())
    base_url, query_params = self._MakeUrl('PUT', path, content_type,
                                           md5_digest)
    headers = {}
    headers['Content-Type'] = content_type
    headers['Content-Length'] = str(len(data))
    headers['Content-MD5'] = md5_digest
    return self.session.put(base_url, params=query_params, headers=headers,
                            data=data)

  def Delete(self, path):
    """Performs a DELETE request.
    Args:
      path: The relative API path to access, e.g. '/bucket/object'.
    Returns:
      An instance of requests.Response containing the HTTP response.
    """
    base_url, query_params = self._MakeUrl('DELETE', path)
    return self.session.delete(base_url, params=query_params)


from oauth2client.service_account import ServiceAccountCredentials
import settings

creds = ServiceAccountCredentials.from_json_keyfile_name(settings.AUTH_JSON)
private_key = creds._private_key_pkcs8_pem
SERVICE_ACCOUNT_EMAIL = creds.service_account_email

GCS_API_ENDPOINT = settings.GCS_API_ENDPOINT

signer = CloudStorageURLSigner(private_key, SERVICE_ACCOUNT_EMAIL,GCS_API_ENDPOINT, 30)

file_path = '/cgs-dev-lims/Quantifications/163/image1.png'
r = signer.Get(file_path)
print('url', r.request.url)