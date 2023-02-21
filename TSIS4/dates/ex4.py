from datetime import datetime
  
start = datetime.strptime("2:25:43", "%H:%M:%S")
end = datetime.strptime("9:38:56", "%H:%M:%S")
  
difference = end - start
  
seconds = difference.total_seconds()
print('difference in seconds is:', seconds)
  
