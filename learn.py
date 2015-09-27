from urllib import request
yahoo_url =  "http://www.canbike.org/information-technology/yahoo-finance-key-statistics-download-to-a-csv-file.html"
def download_stock_data(csv_url):
     response = request.urlopen(csv_url)
     csv = response.read()
     csv_str =  str(csv)
     lines = csv_str.split("\\n")
     dest_url = r'yahoo.csv'
     fx = open(dest_url, 'w')
     for line in lines:
          fx.write(line + "\n")
     fx.close()
download_stock_data(yahoo_url)