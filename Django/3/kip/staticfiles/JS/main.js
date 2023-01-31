
$(function () {
    'use strict';

  $(".failed_row input, .failed_row select").attr("disabled", true);

    //Add spinner cursor whenever the user initiates AJAX request.
  $(document).ajaxSend(function() {
    $("body").addClass("waiting");
  })
  //Remove spinner whenever an AJAX request completes.
  $(document).ajaxComplete(function() {
    $("body").removeClass("waiting");
  })

  if ( typeof $(".popup").draggable !== 'undefined'){
    $(".popup").draggable();
  }
  $('[data-toggle="tooltip"]').tooltip();
  if(localStorage.openMenu == "true"){
    openMenu();
  }else{
    closeMenu();
  }

});

function htmlDecode(input){
  var e = document.createElement('div');
  e.innerHTML = input;
  return e.childNodes.length === 0 ? "" : e.childNodes[0].nodeValue;
}

function get_current_date(){
    var d = new Date,
    dformat = [d.getFullYear() ,d.getMonth()+1,
               d.getDate()
               ].join('-')+' '+
              [d.getHours(),
               d.getMinutes(),
               d.getSeconds()].join(':');
    return dformat;
}
function dateFormat(date_str, include_time=true){
            if(date_str =='' || date_str == null){
                return '--'
            }
            var c_date = new Date(date_str);

            var c_month = (c_date.getMonth() >= 9) ? c_date.getMonth() + 1 : '0'+ (c_date.getMonth()+1);
            var c_day = ( c_date.getDate() >9 ) ? c_date.getDate() : '0' + c_date.getDate();
            var c_hour = ( c_date.getHours() >9 ) ? c_date.getHours() : '0' + c_date.getHours();
            var c_min = ( c_date.getMinutes() >9 ) ? c_date.getMinutes() : '0' + c_date.getMinutes();
            // return c_month + '/' + c_day + '/' + c_date.getFullYear() + ' ' + c_hour + ':' + c_min
            if(include_time){
                return c_date.getFullYear() + '-' + c_month + '-' + c_day + ' ' + c_hour + ':' + c_min
            }else{
                return c_date.getFullYear() + '-' + c_month + '-' + c_day
            }


}
function go_cartagenia(){
    window.open("/mybackend/sso_cartagenia/", "_blank", 'toolbar,resizable');
}

function user_message(mtype, msg, refresh=false){
    var yes_html ='';
	if(mtype.toLowerCase()=='error'){
		$('#modal-title').html('Error Message');
        yes_html = ' <button type="button" class="btn btn-default" data-dismiss="modal" >Close</button>';

	}else if(mtype.toLowerCase()=='status'){
 		$('#modal-title').html('Status');
        yes_html = ' <button type="button" class="btn btn-default" data-dismiss="modal" >Close</button>';

    }else if(mtype.toLowerCase() == 'wait'){
        $('#modal-title').html('Please Wait');
         msg = msg +  '<img class="wait-image" src="/static/IMAGES/icon_spinner.gif" />';
 	}else{
        $('#modal-title').html(mtype);
        yes_html = ' <button type="button" class="btn btn-default" data-dismiss="modal" >Close</button>';

    }
    $('#yes-button').html(yes_html);
    $('#model-message').html(msg);

    $('#gimsModal').modal("show");
    if(refresh){
         setTimeout(function() {
                window.location.reload();
        }, 1000);
    }
 }
function confirm_message(submit_title="Confirm", msg='Ready?', f_arg='', f_name='afterConfirmed'){
    var f_name = (f_name=='')? 'afterConfirmed' : f_name;
    $('#modal-title').html(submit_title);
    $('#model-message').html(msg);
    $('#yes-button').html(' <button type="button" class="btn btn-default" data-dismiss="modal" >Cancel</button>\
        <button type="button" class="btn btn-primary" data-dismiss="modal" onClick="'+f_name+'(\''+f_arg+'\')">Confirm</button>');
    $('#gimsModal').modal("show");
 }

 function submit_form(form_id){
    form_id.submit();
 }
 function confirm_submit(form_id, msg='Ready to submit change?', submit_title="Submit Changes"){
    $('#modal-title').html(submit_title);
    $('#model-message').html(msg);
    $('#yes-button').html(' <button type="button" class="btn btn-default" data-dismiss="modal" >Cancel</button>\
        <button type="button" class="btn btn-primary" data-dismiss="modal" onClick="submit_form(' + form_id + ')">Submit</button>');
    $('#gimsModal').modal("show");
 }
function OpenPopupCenter(pageURL, title, w, h) {
            // var left = (screen.width - w) / 2;
            var left = window.screen.availLeft + 300;
            // var top = (screen.height - h) / 4;  // for 25% - devide by 4  |  for 33% - devide by 3
            var top = window.screen.availTop + 200;
            var title = window.open(pageURL, title, 'toolbar=no, location=no, directories=no, status=no, menubar=no, scrollbars=no, resizable=no, copyhistory=no, width=' + w + ', height=' + h + ', top=' + top + ', left=' + left);
            return title
}


var closeMenu = function(){
        $('.slide-menu').css('display', 'none');
        $('.main-content').css('width', '100%');
        $('#openMenu').css('display', 'inline-block');
        $('#closeMenu').css('display', 'none');
        localStorage.openMenu = 'false';
}
var openMenu = function(){
        $('.slide-menu').css('display', 'inline-block');
        $('.main-content').css('width', 'calc(100% - 250px)');
        $('#closeMenu').css('display', 'inline-block');
        $('#openMenu').css('display', 'none');
        localStorage.openMenu = 'true'
}

function updateSampleNote(cid, width=950, height=600) {
    // Args:
    //    cid: `int`. A Sample id.
    //    width: `int`. Modal width in px.
    //    height: `int`. Modal height in px.
    window.notew = OpenPopupCenter('/Sample/Note/'+cid+'/', 'notew', width, height);
}
