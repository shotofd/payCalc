'''
Created on Apr 11, 2016

@author: David
'''

class Hourly(object):
    '''
    calculates salary from hourly rate
    '''
    def daily(self): return self.hourly * 8
    def weekly(self): return self.hourly * 40
    def bi_weekly(self): return self.hourly * 80 
    def monthly(self): return self.hourly * 160
    def annual(self): return (self.hourly * 40) * 52

    def __init__(self, hourly):
        '''
        Constructor
        '''
        self.hourly = hourly
#         self.daily = self.hourly * 8
#         self.weekly = self.hourly * 40
#         self.bi_weekly = self.hourly * 80 
#         self.monthly = self.hourly * 160
#         self.annual = (self.hourly * 40) * 52
            