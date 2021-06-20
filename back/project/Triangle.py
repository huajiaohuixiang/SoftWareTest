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
