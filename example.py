import convertio
import time

client = convertio.Client(token="INSERT_YOUR_TOKEN_HERE")
id = client.convert_by_filename('source.txt', 'pdf')
while client.check_conversion(id).step != 'finish':
    time.sleep(1)
client.download(id, 'result.pdf')
client.delete(id)