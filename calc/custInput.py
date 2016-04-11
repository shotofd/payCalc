'''
Created on Apr 11, 2016

@author: David
'''

class custCalc(object):
    '''
    classdocs
    '''
    
    def revAnnual(self):
        
        self.monthly = self.annualSalary / 12
        #self.daily = self.weekly / 5
        #self.hourly  = self.weekly / 40
        
        print(self.annualSalary)
        return self.annualSalary
    
    def revMonthly (self):
        return (self.annualSalary / 26) * 2
        
    def revWeekly(self):
        return self.annualSalary / 52
        
    def revBiWeekly(self):
        return self.annualSalary / 26 
    
    def revDaily(self):
        return (self.annualSalary / 52) / 5

    def __init__(self , annualSal):
        '''
        Constructor
        '''
        self.annualSalary = annualSal
        

        