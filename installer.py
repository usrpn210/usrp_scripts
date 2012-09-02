#!/usr/bin/env python
import commands

def perfom_install():
    cmd_list = ["git clone git://code.ettus.com/ettus/uhd.git",
                "sudo mv uhd  /usr/local/src/",
                "cd /usr/local/src/uhd/host",
                "sudo mkdir build",
                "cd build",
                "sudo cmake ../",
                "sudo make",
                "sudo make test",
                "sudo make install",
                "cd ~/",
                "git clone http://gnuradio.org/git/gnuradio.git",
                "cd gnuradio",
                "mkdir build",
                "cd build",
                "cmake ../",
                "make",
                "make test",
                "sudo make install",
                "sudo ldconfig"]
    
    for cmd in cmd_list:
        (status , output) = commands.getstatusoutput(cmd)
        print status
        print output
        
    

    pass

def main():
    perfom_install()
    pass

if __name__ == "__main__" :
    main()