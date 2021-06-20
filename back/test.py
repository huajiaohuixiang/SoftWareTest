def commission_atom(host_num,display_num,peripheral_num):
    host_price, display_price, peripheral_price = 25, 30, 45
    
    if host_num <= 0 or display_num <= 0 or peripheral_num <= 0 or host_num > 70 or display_num > 80 or peripheral_num > 90:
        return 'error', 'error'
    sales = host_num * host_price + display_num * display_price + peripheral_num * peripheral_price
    if sales <= 1000:
        return sales, float('%.2f' % (sales * 0.1))
    elif sales <= 1800:
        return sales, float('%.2f' % (sales * 0.15))
    else:
        return sales, float('%.2f' % (sales * 0.2))



def triangle_atom(a,b,c):
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

print(triangle_atom(1,2,3))