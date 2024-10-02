import requests
import struct
import binascii
constant_data_0 = '1218'
user_id = '363335333562613531326363306130623535633737313831' #hex of userid
constant_data_1 = '19' 
app_id = '32' # hex of 2 which is appid
app_version='333937' # hex of 397 which is app version
join_2 = '03' # joins appid and appversion
# appid and appversion
Latitude = 25.266313125893226
Longitude = 82.9888062453125
join = "21" # "!" 

packed_double = struct.pack('d', Latitude)
packed_double1 = struct.pack('d', Longitude)

hex_string = packed_double.hex()
hex_string1 = packed_double1.hex()

binary_data1 = bytes.fromhex(hex_string)
binary_data2 = bytes.fromhex(hex_string1)

raw_data = bytes.fromhex(constant_data_0)+bytes.fromhex(user_id)+bytes.fromhex(constant_data_1)+binary_data1+bytes.fromhex(join)+binary_data2+bytes.fromhex(app_id)+bytes.fromhex(join_2)+bytes.fromhex(app_version)



url = 'https://customer.rapido.bike/v2/cso/status'


headers = {
    'Callingfrom': 'appLaunch',
    'Accept': 'application/json,application/protobuf',
    'Accept-Charset': 'UTF-8,ISO-8859-1;q=0.1',
    'User-Agent': 'Ktor client',
    'City': 'Varanasi',
    'App_variant': 'v8',
    'Channel-Name': 'app',
    'Currentdatetime': '2024-04-25 21:11:21',
    'Channel-Host': 'android',
    'Appid': str(binascii.unhexlify(app_id).decode('utf-8')),
    'Latitude': str(Latitude),
    'Appversion': str(binascii.unhexlify(app_version).decode('utf-8')),
    'Channel-Entity': 'customer',
    'Appversionstring': '8.21.1',
    'Deviceid': '90344cc1522d9a99',
    'Longitude': str(Longitude),
    'Authorization': 'Bearer ...',
    'Key': 'r@pido333',
    'Content-Type': 'text/plain',  
    'Content-Length': str(len(raw_data)),
    'Accept-Encoding': 'gzip, deflate, br'
}

try:
    response = requests.post(url, headers=headers, data=raw_data)
    print("Response Status Code:", response.status_code)
    print("Response Content:", response.content)
except Exception as e:
    print("An error occurred:", e)
