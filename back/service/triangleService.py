def triangle_atom(arg_list):
        side1, side2, side3 = arg_list[0], arg_list[1], arg_list[2]
        maxside = max(side1, side2, side3)
        if side1 <= 0 or side2 <= 0 or side3 <= 0 or side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
            return '数值不合法'
        else:
            if pow(maxside, 2) * 2 == pow(side1, 2) + pow(side2, 2) + pow(side3, 2):
                if side1 == side2 or side1 == side3 or side2 == side3:
                    return '等腰直角三角形'
                else:
                    return '普通直角三角形'
            elif pow(maxside, 2) * 2 > pow(side1, 2) + pow(side2, 2) + pow(side3, 2):
                if side1 == side2 or side1 == side3 or side2 == side3:
                    return '等腰钝角三角形'
                else:
                    return '普通钝角三角形'
            elif pow(maxside, 2) * 2 < pow(side1, 2) + pow(side2, 2) + pow(side3, 2):
                if side1 == side2 and side1 == side3 and side2 == side3:
                    return '等边三角形'
                else:
                    if side1 != side2 and side1 != side3 and side2 != side3:
                        return '普通锐角三角形'
                    else:
                        return '等腰锐角三角形'



class TriService(object):
    def handlerData(self,data):
        print(data)
        data['ActualOutput']=data['ExpectedOutput']
        for index,row in data.iterrows():
            side1=row['Side1']
            side2=row['Side2']
            side3=row['Side3']
            result=triangle_atom((side1,side2,side3))
            print(result)
            row['ActualOutput']=result
            pass
        data.to_csv(r"./csv/triangle/output.csv")

