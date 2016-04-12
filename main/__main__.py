'''
Created on Apr 11, 2016

@author: David
'''
#from calc import custInput
from calc import annual
from calc import hourly

class runCalc:
    
    runApp = input("Analyze salary info? Y/N: ").lower().startswith('y')
    
    while runApp:
        print('in the while ')
        choice = input('Hourly or Annual: ').lower()
        print(choice)
        if choice.startswith('a'): #== 'annual':
            salary = annual.Annual(float(input('Enter Annual Salary: ')))
            print("Annual: "+str(salary.revAnnual()))
            print("Monthly: "+str(salary.revMonthly()))
            print("Bi-Weekly: "+str(salary.revBiWeekly()))
            print("Weekly: "+str(salary.revWeekly()))
            print("Daily: "+str(salary.revDaily()))
            print("Hourly: "+str(salary.revHourly()))
        elif choice.startswith('h'): 
            rate = hourly.Hourly(float(input('Enter Hourly Rate: ')))
            print("Annual: "+str(rate.annual))
            print("Monthly: "+str(rate.monthly))
            print("Bi-Weekly: "+str(rate.bi_weekly))
            print("Weekly: "+str(rate.weekly))
            print("Daily: "+str(rate.daily))
        else:
            print("FAIL - try again if you'd like")

        runApp = input("Continue?: ").lower().startswith('y')
        print(runApp)

    
#     name = input('Enter Name: ')
#      
#     print('name: '+name)    
#     if input('Hourly Info? Y/N: ') == 'Y':
#         hourly = int(input('Enter Hourly Rate: '))
#         weekly = hourly * 40
#         biWeekly = weekly * 2
#         monthly = weekly * 4
#         Annual = weekly * 52
#      
#         print('weekly: '+str(weekly))
#         print('bi-weekly: '+str(biWeekly))
#         print('monthly: '+str(monthly))
#         print('Annual: '+str(Annual))
#     else:
#         annualRev = int(input('Enter Annual Salary: '))
#         revMonthly = annualRev/12
#         revWeekly = annualRev/52
#         revBiWeekly = revWeekly*2
#         revDaily = revWeekly/5
#         revHourly = revWeekly /40
#      
#         print('daily: ' + str(revDaily))
#         print('hourly: ' + str(revHourly))
#         print('weekly: ' + str(revWeekly))
#         print('bi-weekly: ' + str(revBiWeekly))
#         print('monthly: ' + str(revMonthly))
#         print('Annual: ' + str(annualRev))
    

if __name__ == '__main__':
    pass