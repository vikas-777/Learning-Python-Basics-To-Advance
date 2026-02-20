def rec_fun(num):
    if num == 0 or num == 1:
       return 1
    else:
        return num * rec_fun(num-1)
print(rec_fun(7))