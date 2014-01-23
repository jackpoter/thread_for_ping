import subprocess    
import re
import thread 
#import threading  
import time
'''

'''

def test2 (iplist):
    reip = re.compile("(.*)\.(.*)\.(.*)\.(.*)", re.IGNORECASE)
    raw_iplist = reip.findall(iplist)[0][0] + '.' + reip.findall(iplist)[0][1] + '.' + reip.findall(iplist)[0][2] 
    #d_ip = reip.findall(iplist)[0][3] 
    for ip in xrange(1,255):
        ip = raw_iplist + '.' +  str(ip)
        thread.start_new_thread(pingip, (ip,  ))
        #thread.start_new_thread(pingip, (imap_ip, ))
        time.sleep(0.1)
    time.sleep(1)
	#thread.exit_thread()  

def pingip (ip):
    p = subprocess.Popen(["ping", ip, '-n', '1'], \
    #p = subprocess.Popen(["ping", ip, '-c', '1'], 
         stdin = subprocess.PIPE, \
         stdout = subprocess.PIPE, \
         stderr = subprocess.PIPE, \
         shell = True)    
    out = p.stdout.read() 
    regex = re.compile("Minimum = (\d+)ms, Maximum = (\d+)ms, Average = (\d+)ms", re.IGNORECASE)
    #    Minimum = 46ms, Maximum = 46ms, Average = 46ms
    #regex = re.compile("Minimum = (\d+)ms, Maximum = (\d+)ms, Average = (\d+)ms", re.IGNORECASE)
    #    最短 = 486ms，最长 = 486ms，平均 = 486ms
    #regex = re.compile(u"最短 = (\d+)ms, 最长 = (\d+)ms, 平均 = (\d+)ms", re.IGNORECASE)
    # rtt min/avg/max/mdev = 251.990/252.087/252.142/0.360 ms
    #regex = re.compile(u"mdev = (.*?)/(.*?)/", re.IGNORECASE)
    n = 0
    try:
        if 'out' in out:
            n = 1
        if n == 0:
            print ip, regex.findall(out)[0][1], 'ms'
    except:pass


if __name__=='__main__':  
    print 'go'
    iplist = '192.168.1.1'
    #print 'tye:', type(iplist)
    test2(iplist)  
    #raw_input('end_>')
    raw_input()
