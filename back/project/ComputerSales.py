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