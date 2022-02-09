import datetime
import time
from hashlib import sha256
print("Starting mining....")
st=time.time()
for i in range(1,10000000000000000000000000000000):
 fs=sha256(str(i).encode()).hexdigest()
 if(fs.startswith('0000000')):
   break
print(i,'is nonce',fs)
time.sleep(1)
et=time.time()
print('Mining sucessfully ended with time of',str(datetime.timedelta(seconds=et-st)))





