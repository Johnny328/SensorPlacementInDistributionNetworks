#coding:utf-8

from splitfile import split_file
from  generatetimelist import generate_timelist
from commandline import command_line
import threading

'''
def thread1(sun):
    s = str("node%d.rpt"% sun)
    print(s)

for i in range(10):
    t = threading.Thread(target=thread1, args=(i,))
    t.start()
    '''
'''
def threaddemo(count):
    count  = int(count)
    for i in range(10):
        #if (count+i) <= 85:
        print(count+i)
    print(threading.currentThread().getName())

for i in range(10):
    i = i*10
    t = threading.Thread(target=threaddemo, args=(i,))
    t.start()
    '''

if __name__ == "__main__":
    '''
    file1 = "F:/AWorkSpace/test/Net2node11.rpt"
    file2 = "F:/AWorkSpace/test/ky2node55.rpt"
    list1 = split_file(file1, 4, '  [0-9]')
    list2= split_file(file2, 4, '  J')
    #print(np.array(list1))
    #print(np.array(list2))

    Net2node11_list = generate_timelist(list1, 11, 36, 10800, 600)
    ky2node55_list = generate_timelist(list2, 55, 809, 10800, 600)
    print(Net2node11_list)
    print(ky2node55_list)
    
    # Test1
    exe1 = "F:/AWorkSpace/test/EPANETDEMO.exe"
    input1 = "F:/AWorkSpace/test/Net2.inp"
    rpt1 = "F:/AWorkSpace/test/Net2node11.rpt"
    node1 = 11
    sourcequality1 = 200000  # 投入的污染物mg数
    duration1 = 10800  # 水力模拟时间参数
    qual_reportstep1 = 600  # 水质步长与报告间隔时间
    command_line(exe1, input1, rpt1, node1, sourcequality1, duration1, qual_reportstep1)
    '''