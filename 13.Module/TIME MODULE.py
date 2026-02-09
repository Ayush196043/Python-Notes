# TIME MODULE 

# 1. time.time()--> print current time in second (epock).{1970 1 junvery}.

#Exampel:-
import time
a= time.time()
print(a)

# 2. time.ctime("second")--> second (epoch) time ko string mreconvert kare ga.
#example:-

import time
#input:-1741200724.1455853
b = time.ctime(1741200724.1455853)
print(b)
#output:-Thu Mar  6 00:22:04 2025

# 3. time.sleep("second")--> input second delay kar ke run kare ga.

import time
print("ayush pandey.")
for i in range(9):
    i+=1
    time.sleep(1)
    print(i)

# 4. time.localtime()--> it return  local time in second.{tm_sec,tm_wday,tm_yday,tm_isdst)

# Convert seconds since the Epoch to a time tuple expressing local time.
# When 'seconds' is not passed in, convert the current time instead.}
# example:-
import time
print(time.localtime())


#5. time.strftime()-->  convert epoch in string.

#example:-
print(time.strftime("%Y-%m-%d %H:%M:%S"))
#output:-2025-03-06 01:00:33




