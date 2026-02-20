# import socket
# host_name = socket.gethostname()
# ip_address = socket.gethostbyname(host_name)
# print("\n HOST NAME IS : ",host_name)
# print("\n IP ADDRESS IS : ",ip_address)
#
# import numpy as np
# arr = np.arange(16)
# print(arr)
# print(arr.shape)
# print(arr.ndim)
# arr_2 = arr.reshape([2,2,4])
# print(arr_2)
# print(arr_2.ndim)
# print(arr_2.shape)
# import pandas as pd
#
# list1 = ["Vikas",55]
# list2 = ["hari",99]
# list3 = ["Sahasra",33]
#
# xyz = pd.DataFrame(data=[list1,list2,list3],columns =["Name","No.of_Customers"])
#
# print(xyz)
#

import numpy as np
arr = np.arange(10)
arr = arr[arr%2 == 1]
print(arr)
