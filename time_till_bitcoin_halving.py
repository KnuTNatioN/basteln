import http.client
import datetime

def printDATAby():
    result = "Retrieved current data from Blockchain.com"
    result += "\n" + "Thank you at this point."
    result += "\n" + "https://www.blockchain.com/de/legal/api-terms"
    result += "\n" + " and "
    result += "\n" + "https://www.blockchain.com/de/explorer/api/q"

    print(result)

def getData(connection, path):
    connection.request("GET", path)
    FULLresult = connection.getresponse()
    if(FULLresult.status != 200):
        return 0
    result = FULLresult.read().decode()
    return result

def secondsToPrettyTime(seconds):
    now = datetime.datetime.now()
    then = now + datetime.timedelta(seconds=seconds)
    
    difference = then - now
    
    years = difference.days // 365
    month = difference.days // 30
    weeks = difference.days // 7
    days = difference.days
    hours = difference.seconds // 3600
    minutes = (difference.seconds % 3600) // 60
    seconds = difference.seconds % 60
    return '{:02d} years, {:02d} month, {:02d} weeks, {:02d} days, {:02d}:{:02d}:{:02d}'.format(years, month, weeks, days, hours, minutes, seconds)

if __name__ == "__main__":
    printDATAby()
    conn = http.client.HTTPSConnection('blockchain.info')
    halvingAmount = 210000                              # halving every 210000th block
    interval = float(getData(conn, "/q/interval"))      # Average time between blocks in seconds
    height = float(getData(conn, "/q/getblockcount"))   # Current block height in the longest chain

    blocks_left = halvingAmount - height % halvingAmount
    sec_till_halv = blocks_left * interval
    print(secondsToPrettyTime(sec_till_halv))
