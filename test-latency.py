#! /usr/bin/env python

# Test network latency.
#
# Usage:
# test-latency.py ip count
#



import numpy
import pexpect
import sys


class NetworkLatencyBenchmark(object):
    def __init__(self, ip):
        object.__init__(self)

        self.ip = ip
        self.interval = 0.5

        ping_command = 'ping -i ' + str(self.interval) + ' ' + self.ip
        self.ping = pexpect.spawn(ping_command)

        self.ping.timeout = 1200
        self.ping.readline()  # init
        self.wifi_latency = []
        self.wifi_timeout = 0

    def run_test(self, n_test):
        for n in range(n_test):
            p = self.ping.readline()

            try:
                ping_time = float(p[p.find('time=') + 5:p.find(' ms')])
                self.wifi_latency.append(ping_time)
                print('test:', n + 1, '/', n_test, ', ping latency :', ping_time, 'ms')
            except:
                self.wifi_timeout = self.wifi_timeout + 1
                print('timeout')

        self.wifi_timeout = self.wifi_timeout / float(n_test)
        self.wifi_latency = numpy.array(self.wifi_delay)

    def get_results(self):
        print('mean latency', numpy.mean(self.wifi_latency), 'ms')
        print('std latency', numpy.std(self.wifi_latency), 'ms')
        print('timeout', self.wifi_timeout * 100, '%')


if __name__ == '__main__':

    if len(sys.argv)>1:
        ip = sys.argv[1]
    if len(sys.argv)>2:
        n_test = eval(sys.argv[2])

    netbench = NetworkLatencyBenchmark(ip)

    netbench.run_test(n_test)
    netbench.get_results()