
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# rpc_user and rpc_password are set in the litecoin.conf file
rpc_user = 'user'
rpc_password = 'password'

rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:9332"%(rpc_user, rpc_password))
data = rpc_connection.omni_listproperties() 

prop_num = 0
max_prop_num = (len(data))-1

user_def_name = input('enter the name of the property you wish to extract try "charlitopanama" or "SIPI_Jelly_Beans_" \n')

#user_def_name = 'charlitopanama'
#user_def_name = 'SIPI_Jelly_Beans_'
serial_number = 100001
num_of_tokens = []

f = open('data.txt', 'w+')
f.close()

while prop_num < max_prop_num:  
    if data[prop_num]['name'][:-5] == user_def_name and str(data[prop_num]['name'][-5:]) == str(serial_number)[1:]:
        prop_num += 1
        serial_number += 1
        num_of_tokens.append('x')        
    elif prop_num == max_prop_num:       
        break
    else:
        prop_num += 1

serial_number = 100001
prop_num = 0        
max_token_num = (len(num_of_tokens)) +100000

def add_to_output_txt():
    f = open('data.txt', 'a+')
    f.write(data[prop_num]['category'])
    f.write(data[prop_num]['subcategory'])
    f.write(data[prop_num]['data'])
    f.close()

while prop_num <= max_prop_num:
    if data[prop_num]['name'][:-5] == user_def_name and str(data[prop_num]['name'][-5:]) == str(serial_number)[1:]:
        #print((data[prop_num]['name']),(data[prop_num]['category'][:5]),(data[prop_num]['category'][-5:]),(data[prop_num]['data'][-5:]))
        add_to_output_txt()
        prop_num += 1
        serial_number += 1   
    elif serial_number-1 == max_token_num:
        break
    elif prop_num == max_prop_num:
        prop_num = 0
    else:
        prop_num += 1

import base64_to_image
