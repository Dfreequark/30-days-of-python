import time

epoch = time.gmtime(0) # Jan 1, 1970, 00:00:00 UTC

# cut-off time around 2038; as C lib uses 32-bit system to handle time

#functions

current_time = time.time()
print(time.ctime(current_time))

utc_time= time.gmtime(current_time)
print("UTC time:", utc_time)
