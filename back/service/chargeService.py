import datetime
import os


def charge_problem(arg_list):
    monthly_fee, cost_per_min = 25, 0.15
    talk_time_month, unpaid_num_year = \
        arg_list[0], arg_list[1]
    cost = monthly_fee
    if talk_time_month < 0 or talk_time_month > 44640 or unpaid_num_year < 0 or unpaid_num_year > 11:
        return 'error'
    if talk_time_month <= 60 and unpaid_num_year <= 1:
        cost += talk_time_month * cost_per_min * (1 - 0.01)
    elif 60 < talk_time_month <= 120 and unpaid_num_year <= 2:
        cost += talk_time_month * cost_per_min * (1 - 0.015)
    elif 120 < talk_time_month <= 180 and unpaid_num_year <= 3:
        cost += talk_time_month * cost_per_min * (1 - 0.02)
    elif 180 < talk_time_month <= 300 and unpaid_num_year <= 3:
        cost += talk_time_month * cost_per_min * (1 - 0.025)
    elif talk_time_month > 300 and unpaid_num_year <= 6:
        cost += talk_time_month * cost_per_min * (1 - 0.03)
    else:
        cost += talk_time_month * cost_per_min
    return cost


class CharService:
    def handlerData(self, data,name,testmethod):
        print(data)
        data['ActualOutput'] = data['ExpectedOutput']
        data['flag'] = data['ExpectedOutput']
        data['测试人员'] = data['ExpectedOutput']
        data['测试时间'] = data['ExpectedOutput']
        count = 0

        for index, row in data.iterrows():
            monthtalktime = row['MonthTalkTime']
            yearunpaidnum = row['YearUnpaidNum']
            cost = commission_atom((monthtalktime, yearunpaidnum))
            data.at[index, 'ActualOutput']=cost
            data.at[index, '测试人员'] = name
            data.at[index, '测试时间'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if cost=='error':
                data.at[index,'flag']=(cost==row['ExpectedOutput'])
            else:
                data.at[index,'flag']=(float(cost)==float(row['ExpectedOutput']))
            if data.at[index,'flag']==True:
                count+=1
        path = "./csv" + "./" + name + "./" + "charge./" + testmethod
        filename = "./csv" + "/" + name + "/" + "charge/" + testmethod + "/output.csv"
        if not os.path.isdir(path):
            os.makedirs(path)

        data.to_csv(filename)
        return count / len(data)