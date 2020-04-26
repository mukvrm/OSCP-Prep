import http.client

print('** Lists methods available via OPTIONS/HTTP **\n')

host = input('Insert the host/DST IP: ')
port = input('Insert the DST PORT:(default:80) ')

if(port == ''):
    port = 80

try:
    connection = http.client.HTTPConnection(host, port)
    connection.request('OPTIONS', '/')
    response = connection.getresponse()
    print('Enabled methods on webserver are: ', response.getheader('allow'))
    connection.close()
except ConnectionRefusedError:
    print('Connection Failed')