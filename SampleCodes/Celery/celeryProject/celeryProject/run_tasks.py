from celeryProject import tasks
import time


if __name__ == '__main__':
    result_mid = tasks.midcal.delay()
    print('Task result_mid finished? ', result_mid.ready())
    print('Task result_mid result: ', result_mid.result)
    # sleep 10 seconds to ensure the task has been finished
    time.sleep(10)
    # now the task should be finished and ready method will return True
    print('Task result_mid finished? ', result_mid.ready())
    print('Task result_mid result: ', result_mid.result)

    result = tasks.longcal.delay()
    print('Task longcal finished? ', result.ready())
    print('Task longcal result: ', result.result)
    # sleep 10 seconds to ensure the task has been finished
    time.sleep(10)
    # now the task should be finished and ready method will return True
    print('Task longcal finished? ', result.ready())
    print('Task longcal result: ', result.result)

