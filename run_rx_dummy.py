#!/usr/bin/python
import commands
import time
import os
import re
import pexpect
dir_path = "/home/li/workspace/gnu-dev/gnuradio/gr-digital/examples/narrowband"
pattern = "No UHD Devices Found"

def run_tx_script():
    global pattern,dir_path
    """
        perform initial setup for the USRP2
    """
    commands.getstatusoutput("sudo ifconfig eth0 192.168.10.1")
    time.sleep(1)
    resp = commands.getoutput('uhd_find_devices')
    #print resp
    isFound = re.search(pattern, resp, flags=0)
    if isFound:
        print "please connect your uhd_device"
    else:
        #commands.getstatusoutput("sudo ifconfig eth0 192.168.10.1")
        os.chdir(dir_path)
        print commands.getstatusoutput("pwd")
        cmd = "./benchmark_rx.py -f "+str(2.4)+"G -r "+ str(0.5)+"M -v"
        print cmd
        status, text = commands.getstatusoutput(cmd)
            #print status
       


def main():
    run_tx_script()
    
if __name__== "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    
