

def commission_atom(arg_list):
    monthly_fee, cost_per_min = 25, 0.15
    talk_time_month, unpaid_num_year, unpaid_cost_across_year = \
        arg_list[0], arg_list[1], arg_list[2]
    cost = monthly_fee
    if talk_time_month < 0 or talk_time_month > 44640 or unpaid_num_year < 0 or unpaid_num_year > 11 or unpaid_cost_across_year < 0 or unpaid_cost_across_year > 500:
        return 'error'
    if talk_time_month <= 60 and unpaid_num_year <= 1:
        cost += talk_time_month * cost_per_min * 0.01
    elif talk_time_month <= 120 and unpaid_num_year <= 2:
        cost += talk_time_month * cost_per_min * 0.015
    elif talk_time_month <= 180 and unpaid_num_year <= 3:
        cost += talk_time_month * cost_per_min * 0.02
    elif talk_time_month <= 300 and unpaid_num_year <= 3:
        cost += talk_time_month * cost_per_min * 0.025
    elif talk_time_month > 300 and unpaid_num_year <= 6:
        cost += talk_time_month * cost_per_min * 0.03
    else:
        cost += talk_time_month * cost_per_min
    cost += unpaid_cost_across_year * 0.05
    return cost


class CharService:
    def handlerData(self, data):
        print(data)
        data['ActualOutput'] = data['ExpectedOutput']

        for index, row in data.iterrows():
            monthtalktime = row['MonthTalkTime']
            yearunpaidnum = row['YearUnpaidNum']
            unpaidcostacrossyear = row['UnpaidCostAcrossYear']
            cost = commission_atom((monthtalktime, yearunpaidnum, unpaidcostacrossyear))
            row['ActualOutput'] = cost
            pass
        data.to_csv(r"./csv/com/charge.csv")

    # def __init__(self):
    #     pass
    #
    # @staticmethod
    # def charge(method_type, code_version='v2'):
    #     csv_path = charge_index[method_type]
    #     df, arg_start, arg_end = df_read(csv_path)
    #     output1 = []
    #     for i in range(0, len(df)):
    #         arg_list = df.iloc[i, arg_start:arg_end].values.tolist()
    #         output1.append(code_v[code_version](arg_list))
    #     return df_update(df=df, csv_path=csv_path, actual_outputs=[output1], tester_name='anonymous')
    #
    # @staticmethod
    # def charge_method_test(request, code_version='v2'):
    #     arg_list = [request['talk_time_month'], request['unpaid_num_year'], request['unpaid_cost_across_year'],
    #                 request['pay_method']]
    #     return code_v[code_version](arg_list)
