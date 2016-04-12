'''
Created on Apr 11, 2016

@author: David
'''

class Annual(object):
    '''
    classdocs
    '''
    
    def revAnnual(self):
        return self.annualSalary
    
    def revMonthly (self):
        return (self.annualSalary / 26) * 2
        
    def revWeekly(self):
        return self.annualSalary / 52
        
    def revBiWeekly(self):
        return self.annualSalary / 26 
    
    def revDaily(self):
        return (self.annualSalary / 52) / 5
    
    def revHourly(self):
        return (self.annualSalary / 52) / 40

    def __init__(self , annualSal):
        '''
        Constructor
        '''
        self.annualSalary = annualSal
        

        