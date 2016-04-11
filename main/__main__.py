'''
Created on Apr 11, 2016

@author: David
'''
#from calc import custInput
from calc import custInput


class runCalc:
    d = custInput.custCalc(int(input('Enter Annual Salary')))
    print(d.revAnnual())
    print(d.revMonthly())
    print(d.revBiWeekly())
    print(d.revWeekly())
    print(d.revDaily())

 
    name = input('Enter Name: ')
    
    print('name: '+name)
    if input('Hourly Info? Y/N: ') == 'Y':
        hourly = int(input('Enter Hourly Rate: '))
        weekly = hourly * 40
        biWeekly = weekly * 2
        monthly = weekly * 4
        annual = weekly * 52
    
        print('weekly: '+str(weekly))
        print('bi-weekly: '+str(biWeekly))
        print('monthly: '+str(monthly))
        print('annual: '+str(annual))
    else:
        annualRev = int(input('Enter Annual Salary: '))
        revMonthly = annualRev/12
        revWeekly = annualRev/52
        revBiWeekly = revWeekly*2
        revDaily = revWeekly/5
        revHourly = revWeekly /40
    
        print('daily: ' + str(revDaily))
        print('hourly: ' + str(revHourly))
        print('weekly: ' + str(revWeekly))
        print('bi-weekly: ' + str(revBiWeekly))
        print('monthly: ' + str(revMonthly))
        print('annual: ' + str(annualRev))
    

if __name__ == '__main__':
    pass