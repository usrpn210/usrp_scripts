#!/usr/bin/python
import commands
import time
import os
import re
import pexpect
import sys
dir_path = "/home/li/workspace/gnu-dev/gr-digital/examples/narrowband"
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
        rangeList = range(240,250,1)
        for r in rangeList:
            print r
            print commands.getstatusoutput("pwd")
            G = r * .01
            print G
            cmd = "./benchmark_rx.py -f "+str(G)+"G -r "+ str(0.5)+"M -v"
            print cmd
            #status, text = commands.getstatusoutput(cmd)
            child = pexpect.spawn (cmd)
            fout = file("output.txt","w")
            #child.logfile = sys.stdout
            #print status
            #print child
            #print child.stdout
           
            pattern = "ok"
            #child.expect(pexpect.EOF, timeout = 60)
            time.sleep(60)
            #child.wait()
            print child.before
            print child.after
            child.sendline ('\x03')
            time.sleep(10)
    pass

def main():
    run_tx_script()
    
if __name__== "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    
