# Tax calculation for multiple state


def GrossIncome(state, grossincome):

    statetaxrate = {'California': 9.25, 'Oregon': 9, 'Texas':0, 'NJ':6}
    if state in statetaxrate:
        income = grossincome - (grossincome*10/100) - (grossincome*statetaxrate[state]/100)
        return income
    else:
        print(state + " is not in the list of tax claculation")
Income = GrossIncome('OR', 80000)

print(Income)
