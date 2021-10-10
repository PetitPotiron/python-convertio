import convertio
import time

client = convertio.Client(token="INSERT_YOUR_TOKEN_HERE")
conversion_id = client.convert_by_filename('source.txt', 'pdf')
while client.check_conversion(conversion_id).step != 'finish':
    time.sleep(1)
client.download(conversion_id, 'result.pdf')
client.delete(conversion_id)
