
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# rpc_user and rpc_password are set in the litecoin.conf file
rpc_user = 'user'
rpc_password = 'password'

rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:9332"%(rpc_user, rpc_password))
data = rpc_connection.omni_listproperties() 

prop_num = 0
max_prop_num = (len(data))-1
user_def_name = 'Treaty With The Chippewa Of The Mississippi, 1867-'
serial_number = 100001

f = open('data.txt', 'w+')
f.close()

def add_to_output_txt():
    f = open('data.txt', 'a+')
    f.write(data[prop_num]['category'])
    f.write(data[prop_num]['subcategory'])
    f.write(data[prop_num]['data'])
    f.close()

while prop_num <= max_prop_num:
    if data[prop_num]['name'][:-5] == user_def_name and str(data[prop_num]['name'][-5:]) == str(serial_number)[1:]:
        print((data[prop_num]['name']),(data[prop_num]['category'][:5]),(data[prop_num]['category'][-5:]),(data[prop_num]['data'][-5:]))
        add_to_output_txt()
        prop_num += 1
        serial_number += 1
       
    elif prop_num == max_prop_num:
        prop_num = 0
     
    else:
        prop_num += 1
        




