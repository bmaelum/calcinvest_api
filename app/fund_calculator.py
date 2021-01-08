import pandas as pd
#from populate_db import *

def fundSavingsROI(dataDict):
    sum_input = dataDict['startingEquity']
    sum_with_return = dataDict['startingEquity']
    MoM_return = dataDict['interestRateMoM']
    cost_of_fund = dataDict['costOfFund']
    tax_rate = dataDict['taxRate']
    num_years = dataDict['numYears']
    accumulated_cost_of_fund = 0

    data_list = []

    year = 1

    for i in range(1, dataDict['numMonths']):
        #print('--- Month ' + str(i) + '---')
        sum_input += dataDict['savingsPerMonth']
        sum_with_return += dataDict['savingsPerMonth']
        sum_with_return = int(sum_with_return * (MoM_return))
        #print('Accumulated savings:  ' + str(sum_input) + ',-')
        #print('With return:          ' + str(sum_with_return) + ',-')
        if i % 12 == 0:
            #print('\n- Year ' + str(int(i / 12)) + ' -')
            year += 1
            sum_with_return = int(sum_with_return * (1 - cost_of_fund))
            current_cost_of_fund = int(sum_with_return * cost_of_fund)
            accumulated_cost_of_fund += current_cost_of_fund
            #print('Yearly cost of fund = ' + str(round(current_cost_of_fund)) + ',-')
            #print('Sum after yearly cost deducted from overall sum = ' + str(sum_with_return) + ',-')
            #print('-------------------------\n')

        data_list.append([i, year, sum_input, sum_with_return])
        
    df_data = pd.DataFrame(columns=['month', 'year', 'sum_input', 'sum_with_return'], data=data_list)

    dataDict['accumulated_savings'] = round(sum_input,2)
    dataDict['accumulated_savings_with_return'] = round(sum_with_return,2)
    dataDict['accumulated_cost_of_fund'] = accumulated_cost_of_fund

    total_gain = sum_with_return - sum_input 
    dataDict['total_gain'] = round(total_gain,2)

    gain_after_tax = total_gain * (1 - (tax_rate))
    tax_deduction = total_gain * tax_rate
    #print('Tax = ' + str(tax_deduction) + ',-')
    #print('Actual gain after ' + str(num_years) + ' years = ' + str(gain_after_tax) + ',-')
    dataDict['tax'] = round(tax_deduction,2)

    total_fund_cost = dataDict['accumulated_cost_of_fund'] + tax_deduction
    #print('Total cost of fund = ' + str(total_fund_cost))
    dataDict['total_cost_of_fund'] = round(total_fund_cost)

    dataDict['actual_gain_at_withdraw'] = round(gain_after_tax,2)
    dataDict['actual_gain_at_withdraw']

    dataDict['fortune'] = dataDict['accumulated_savings'] + dataDict['actual_gain_at_withdraw']
    dataDict['fortune']

    #populate_db_fund_calculator(dataDict)

    return dataDict, df_data