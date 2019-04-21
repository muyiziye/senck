#!/usr/bin/env python
import gearman
import subprocess
from stock import get_stock_list

def run_command(cmd_str):
    subprocess.Popen(cmd_str.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout,stderr = test.communicate()
    
    return stdout


def task_listener_stock(gearman_worker, gearman_job):
    print 'Information transfer by work: ' + gearman_job.data
    stock_list = get_stock_list(1)
    stock_str = "".join(stock_list)
    #return "123321"
    return stock_str


gm_worker = gearman.GearmanWorker(['localhost:10000'])
# gm_worker.set_client_id is optional
gm_worker.set_client_id('python-worker')
gm_worker.register_task('stock', task_listener_stock)

# Enter our work loop and call gm_worker.after_poll() after each time we timeout/see socket activity
gm_worker.work()
