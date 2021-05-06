


def commission_atom(arg_list):
    host_price, display_price, peripheral_price = 25, 30, 45
    host_num, display_num, peripheral_num = arg_list[0], arg_list[1], arg_list[2]
    if host_num <= 0 or display_num <= 0 or peripheral_num <= 0 or host_num > 70 or display_num > 80 or peripheral_num > 90:
        return 'error', 'error'
    sales = host_num * host_price + display_num * display_price + peripheral_num * peripheral_price
    if sales <= 1000:
        return sales, float('%.2f' % (sales * 0.1))
    elif sales <= 1800:
        return sales, float('%.2f' % (sales * 0.15))
    else:
        return sales, float('%.2f' % (sales * 0.2))


class ComService(object):
    def handlerData(self,data):
        print(data)
        data['ActualSales']=data['ExpectedSales']
        data['ActualCommission']=data['ExpectedCommission']
        data['flag']=data['ExpectedSales']
        for index,row in data.iterrows():
            host=row['Host']
            display=row['Display']
            peripheral=row['Peripheral']
            sales,commission=commission_atom((host,display,peripheral))
            data.at[index,'ActualCommission']=commission
            data.at[index,'ActualSales']=sales
            if commission=='error':
                data.at[index,'flag']=(commission==row['ExpectedCommission']) and (sales==row['ExpectedSales'])
            else:
                data.at[index,'flag']=(float(commission)==float(row['ExpectedCommission'])) and (float(sales)==float(row['ExpectedSales']))
        data.to_csv(r"./csv/com/output.csv")