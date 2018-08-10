from django.core.management import BaseCommand
from lims.models import SangerStatus, FluidigmResult, ControlLog
from workflows.models import QTWorkFlowStatus, QTWorkFlows, FPWorkFlowStatus, FPWorkFlows, SangerWorkFlows, LabWorkFlows, LabWorkFlowStatus
from mybackend import functions


class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            print('insert data to correct workflows')
            wfs = LabWorkFlows.objects.all()
            try:
                for w in wfs:
                    qt = QTWorkFlows(id=w.id, name=w.name, created_date=w.created_date, username=w.username,
                                     result_data=w.result_data, status_id=w.status_id, type_id=w.type_id, note=w.note)
                    qt.save()
                    fp = FPWorkFlows(id=w.id, name=w.name, created_date=w.created_date, username=w.username,
                                     result_data=w.result_data, status_id=w.status_id, type_id=w.type_id, note=w.note)
                    fp.save()
                    ss = SangerWorkFlows(id=w.id, name=w.name, created_date=w.created_date, username=w.username,
                                     result_data=w.result_data, status_id=w.status_id, type_id=w.type_id, note=w.note)
                    ss.save()
            except Exception as e:
                e_message = e.message if e.message else ','.join(map(str, e.args))
                raise functions.CustomError('Error to update workflows : %s' % e_message)

            print('insert data to correct workflows status')
            wfs = LabWorkFlowStatus.objects.all()
            try:
                for w in wfs:
                    qt = QTWorkFlowStatus(id=w.id, workflow_id=w.workflow_id, tube_number=w.tube_number,
                                          control_id=w.control_id, sample_id=w.sample_id, container=w.container,
                                          status_id=w.status_id, result=w.result)
                    qt.save()
                    fp = FPWorkFlowStatus(id=w.id, workflow_id=w.workflow_id, tube_number=w.tube_number,
                                          control_id=w.control_id, sample_id=w.sample_id, container=w.container,
                                          status_id=w.status_id, result=w.result)
                    fp.save()
            except Exception as e:
                e_message = e.message if e.message else ','.join(map(str, e.args))
                raise functions.CustomError('Error to update workflows status : %s' % e_message)

            print('update Control Log')
            controllogs = ControlLog.objects.all()
            try:
                for clog in controllogs:
                    if clog.labtype_id == 1:
                        clog.qt_status_id = clog.wf_status_id
                    elif clog.labtype_id == 2:
                        clog.fp_status_id = clog.wf_status_id
                    else:
                        pass
                    clog.save()
            except Exception as e:
                e_message = e.message if e.message else ','.join(map(str, e.args))
                raise functions.CustomError('Error to update Control Log : %s' % e_message)

            print('update SangerStatus')
            sangerstatus = SangerStatus.objects.all()
            try:
                for ss in sangerstatus:
                    ss.sangerworkflow_id = ss.workflow_id
                    ss.save()
            except Exception as e:
                e_message = e.message if e.message else ','.join(map(str, e.args))
                raise functions.CustomError('Error to update sanger status : %s' % e_message)

            print('update fluidigm result')
            fluidigmresult = FluidigmResult.objects.all()
            try:
                for fr in fluidigmresult:
                    fr.fpworkflow_id = fr.workflow_id
                    fr.save()
            except Exception as e:
                e_message = e.message if e.message else ','.join(map(str, e.args))
                raise functions.CustomError('Error to fluidigm result : %s' % e_message)

        except Exception as e:
            e_message = e.message if e.message else ','.join(map(str, e.args))
            print(e_message)