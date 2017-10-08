from googlefinance.client import get_price_data, get_prices_data, get_prices_time_data
import time
import sys

# Usage: stocks.py [history in years] [ticker file start at] [ticker file end at]

chunk_size=5
start_position=-1
end_position=-1
period = "5Y"

if len(sys.argv) >= 2:
  period=str(int(sys.argv[1]))+"Y"
if len(sys.argv) >= 3:
  start_position=int(sys.argv[2])
if len(sys.argv) >= 4:
  end_position=int(sys.argv[3])

print "Period: "+str(period)
print "Ticker start pos: "+str(start_position)
print "Ticker end pos: "+str(end_position)

start = time.time()
params = []

print "Reading in tickers..."
count=0
with open('tickers') as f:
  for line in f:
    if start_position != -1 and count < start_position-1:
      count = count+1
      continue
    if count % 100 == 0:
      print "Ticker position: "+str(count)
    if end_position != -1 and count >= end_position:
      break
    count+=1
    params.append({'q':str(line).strip()})
    if count % chunk_size == 0:
      print "Sending request for "+str(len(params))+" tickers"
      request_start_time=time.time()
      df = get_prices_data(params, period)
      req_time = time.time()-request_start_time
      print "Request took "+str(req_time)+" secs ("+str(req_time/chunk_size)+" sec per ticker.) Writing to csv.."
      params = []
      df.to_csv(str(count-chunk_size)+'-'+str(count-1)+'.csv')

end = time.time()
elapsed=end-start

print "Elapsed time: "+str(elapsed)
