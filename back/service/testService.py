import pandas as pd;
import project.ComputerSales;
import os
import datetime
from project.add import add ;
class TestService(object):
    def isSame(a,b):
        if isinstance(a,str):
            return a==b
        else:
            return float(a)==float(b)


    def handlerData(self,data,projectName,name,testmethod):
        projectInfo=pd.read_csv('./project/projectInfo.csv',sep=';')

        print(projectName)
        funcName=''
        inputParam=''
        outputParam=''
        for index,row in projectInfo.iterrows():
                if row['projectName']==projectName:
                    funcName=row['funcName']
                    inputParam=row['inputParam']
                    outputParam=row['outputParam']
                    break
        inputParams=inputParam[1:len(inputParam)-1].split(',')
        outputParams=outputParam[1:len(outputParam)-1].split(',')
        #接下来把那个换成globals()[funcName](1,2,3)就行\
            
        for param in outputParams:
            param=param.replace(' ','')
            param=param[1:len(param)-1]
            data['Actual'+param]=data[param]
        # for inputparam in inputParams:
        #     inputparam=inputParam.replace(' ','')
        #     inputParam=inputParam[1:len(inputParam)-1]
        data['flag']=True
        data['测试人员']=name
        data['测试时间']=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        count=0
        for index,row in data.iterrows():
            inputs=[]
            for param in inputParams[:]:
                param= param.replace(' ','')
                param=param[1:len(param)-1]
                inputs.append(row[param])
            outputs=globals()[funcName](inputs)
            if len(outputParams)==1:
                data.at[index,'Actual'+outputParams[0].replace(' ','')[1:len(outputParams[0])-1]]=outputs
            else:
                tempi=0
                for param in outputParams[:]:
                    param=param.replace(' ','')
                    param=param[1:len(param)-1]
                    data.at[index,'Actual'+param]=outputs[tempi]
                    tempi+=1
        
            # data.at[index,'测试人员']=name
            # data.at[index,'测试时间']=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            i=0
            for param in outputParams[:]:
                
                param=param.replace(' ','')
                param=param[1:len(param)-1]
                actual= data.at[index,'Actual'+param]
                if not self.isSame(actual,data.at[index,param]) :
                    data.at[index,'flag']=False
                    break
                i+=1
            if i==len(outputParams):
                data.at[index,'flag']=True
            if data.at[index,'flag']==True:
                count+=1
        path="./output"+"./"+projectName+"./"+name+"./"+testmethod
        filename=path+"/output.csv"

        if not  os.path.isdir(path):
            os.makedirs(path)
        
        data.to_csv(filename)
        return count/len(data)
       

       



def commission_atom(arg_list):
    host_price, display_price, peripheral_price = 25, 30, 45
    host_num,display_num,peripheral_num=arg_list[0],arg_list[1],arg_list[2]
    if host_num <= 0 or display_num <= 0 or peripheral_num <= 0 or host_num > 70 or display_num > 80 or peripheral_num > 90:
        return 'error', 'error'
    sales = host_num * host_price + display_num * display_price + peripheral_num * peripheral_price
    if sales <= 1000:
        return sales, float('%.2f' % (sales * 0.1))
    elif sales <= 1800:
        return sales, float('%.2f' % (sales * 0.15))
    else:
        return sales, float('%.2f' % (sales * 0.2))

def triangle_atom(arg_list):
        a,b,c=float(arg_list[0]),float(arg_list[1]),float(arg_list[2])
        if a > 200 or b > 200 or c > 200:
           return '数值越界'
        if a <= 0 or b <= 0 or c <= 0:
           return '数值不合法'
        if a + b > c and a + c > b and b + c > a:
            if a == b or a == c or b == c:
                if a == b and b == c:
                   return '等边三角形'
                elif a * a + b * b == c * c or b * b + c * c == a * a or a * a + c * c == b * b:
                   return '等腰直角三角形'
                else:
                 return '等腰三角形'
            if a * a + b * b == c * c or b * b + c * c == a * a or a * a + c * c == b * b:
                 return '直角三角形'
            else:
                 return '普通三角形'
        else:
             return '非三角形'
def charge(arg_list):
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

def test_triangle_atom(arg_list):
        side1, side2, side3 = arg_list[0], arg_list[1], arg_list[2]
        a, b, c = arg_list[0], arg_list[1], arg_list[2]
        if a > 200 or b > 200 or c > 200:
           return '数值越界'
        if a <= 0 or b <= 0 or c <= 0:
           return '数值不合法'
        if a + b > c and a + c > b and b + c > a:
            if a == b or a == c or b == c:
                if a == b and b == c:
                   return '等边三角形'
                elif a * a + b * b == c * c or b * b + c * c == a * a or a * a + c * c == b * b:
                   return '等腰直角三角形'
                else:
                 return '等腰三角形'
            if a * a + b * b == c * c or b * b + c * c == a * a or a * a + c * c == b * b:
                 return '直角三角形'
            else:
                 return '普通三角形'
        else:
             return '非三角形'
