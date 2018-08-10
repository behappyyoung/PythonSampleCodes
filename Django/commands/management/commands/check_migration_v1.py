from django.core.management import BaseCommand
from lims.models import SangerStatus, FluidigmResult, ControlLog
from workflows.models import QTWorkFlowStatus, QTWorkFlows, FPWorkFlowStatus, FPWorkFlows, SangerWorkFlows, LabWorkFlows, LabWorkFlowStatus
from mybackend import functions


class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            print('check data for correct workflows')
            wfs = LabWorkFlows.objects.all()
            check = True
            try:
                for w in wfs:
                    qt = QTWorkFlows.objects.get(id=w.id, name=w.name, created_date=w.created_date, username=w.username,
                                     result_data=w.result_data, status_id=w.status_id, type_id=w.type_id, note=w.note)
                    fp = FPWorkFlows.objects.get(id=w.id, name=w.name, created_date=w.created_date, username=w.username,
                                     result_data=w.result_data, status_id=w.status_id, type_id=w.type_id, note=w.note)
                    ss = SangerWorkFlows.objects.get(id=w.id, name=w.name, created_date=w.created_date, username=w.username,
                                     result_data=w.result_data, status_id=w.status_id, type_id=w.type_id, note=w.note)
                print(' -- workflows are correct')
            except Exception as e:
                e_message = e.message if e.message else ','.join(map(str, e.args))
                print(' -- workflows are not correct !!!!!!!!!!! ')
                raise functions.CustomError('Error to check workflows update : %s' % e_message)

            print('check data for correct workflows status')
            wfs = LabWorkFlowStatus.objects.all()
            try:
                for w in wfs:
                    qt = QTWorkFlowStatus.objects.get(id=w.id, workflow_id=w.workflow_id, tube_number=w.tube_number,
                                          control_id=w.control_id, sample_id=w.sample_id, container=w.container,
                                          status_id=w.status_id, result=w.result)
                    fp = FPWorkFlowStatus.objects.get(id=w.id, workflow_id=w.workflow_id, tube_number=w.tube_number,
                                          control_id=w.control_id, sample_id=w.sample_id, container=w.container,
                                          status_id=w.status_id, result=w.result)
                print(' -- workflowstatus are correct')
            except Exception as e:
                e_message = e.message if e.message else ','.join(map(str, e.args))
                print(' -- workflowsstatus are not correct !!!!!!!!!!!! ')
                raise functions.CustomError('Error to check workflows status update : %s' % e_message)

            print('check data for Control Log')
            check = True
            controllogs = ControlLog.objects.all()
            try:
                for clog in controllogs:
                    if clog.labtype_id == 1:
                        if clog.qt_status_id != clog.wf_status_id:
                            check = False
                    elif clog.labtype_id == 2:
                        if clog.fp_status_id != clog.wf_status_id:
                            check = False
                    else:
                        pass
                if check:
                    print(' -- Control log is correct')
                else:
                    print(' -- Control log is not correct !!!!!!!!!!!!')
            except Exception as e:
                e_message = e.message if e.message else ','.join(map(str, e.args))
                raise functions.CustomError('Error to check Control Log : %s' % e_message)

            print('check data for sanger status')
            sangerstatus = SangerStatus.objects.all()
            check = True
            try:
                for ss in sangerstatus:
                    if ss.sangerworkflow_id != ss.workflow_id:
                        check = False
                if check:
                    print(' -- Sanger Status is correct')
                else:
                    print(' -- Sanger Status is not correct !!!!!!!!!!!')
            except Exception as e:
                e_message = e.message if e.message else ','.join(map(str, e.args))
                raise functions.CustomError('Error to check sanger status : %s' % e_message)

            print('check data for fluidigm result')
            fluidigmresult = FluidigmResult.objects.all()
            check = True
            try:
                for fr in fluidigmresult:
                    if fr.sangerworkflow_id != fr.workflow_id:
                        check = False
                if check:
                    print(' -- Sanger Status is correct')
                else:
                    print(' -- Sanger Status is not correct !!!!!!!!!! ')
            except Exception as e:
                e_message = e.message if e.message else ','.join(map(str, e.args))
                raise functions.CustomError('Error to check fluidigm result : %s' % e_message)

        except Exception as e:
            e_message = e.message if e.message else ','.join(map(str, e.args))
            print(e_message)