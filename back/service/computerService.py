


def commission_atom(arg_list):
    host_price, display_price, peripheral_price = 25, 30, 45
    host_num, display_num, peripheral_num = arg_list[0], arg_list[1], arg_list[2]
    if host_num <= 0 or display_num <= 0 or peripheral_num <= 0 or host_num > 70 or display_num > 80 or peripheral_num > 90:
        return 'error', 'error'
    commission = host_num * host_price + display_num * display_price + peripheral_num * peripheral_price
    if commission <= 1000:
        return commission, float('%.2f' % (commission * 0.1))
    elif commission <= 1800:
        return commission, float('%.2f' % (commission * 0.15))
    else:
        return commission, float('%.2f' % (commission * 0.2))


class ComService(object):
    def handlerData(self,data):
        print(data)
        data['ActualOutput2']=data['ExpectedOutput2']
        data['ActualOutput1']=data['ExpectedOutput1']
        
        for index,row in data.iterrows():
            host=row['Host']
            display=row['Display']
            peripheral=row['Peripheral']
            commission,sales=commission_atom((host,display,peripheral))
            row['ActualOutput1']=commission
            row['ActualOutput2']=sales
            pass
        data.to_csv(r"./csv/com/output.csv")