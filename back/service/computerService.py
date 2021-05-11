import os
import datetime


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
    def handlerData(self,data,name,testmethod):
        print(data)
        data['ActualSales']=data['ExpectedSales']
        data['ActualCommission']=data['ExpectedCommission']
        data['flag']=data['ExpectedSales']
        data['测试人员']=data['ExpectedSales']
        data['测试时间']=data['ExpectedSales']
        count=0
        for index,row in data.iterrows():
            host=row['Host']
            display=row['Display']
            peripheral=row['Peripheral']
            sales,commission=commission_atom((host,display,peripheral))
            data.at[index,'ActualCommission']=commission

            data.at[index,'ActualSales']=sales
            data.at[index,'测试人员']=name
            data.at[index,'测试时间']=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            if commission=='error':
                data.at[index,'flag']=(commission==row['ExpectedCommission']) and (sales==row['ExpectedSales'])
            else:
                data.at[index,'flag']=(float(commission)==float(row['ExpectedCommission'])) and (float(sales)==float(row['ExpectedSales']))
            if data.at[index,'flag']==True:
                count+=1
        path="./csv"+"./"+name+"./"+"com./"+testmethod
        filename="./csv"+"/"+name+"/"+"com/"+testmethod+"/output.csv"
        if not  os.path.isdir(path):
            os.makedirs(path)
        
        data.to_csv(filename)
        return count/len(data)