attendance = [18, 20, 19, 15, 21]
full=0
total=0
for x in attendance:
      total+=x
      if x>=20:
          print('full')
          full+=1
      else:
          print('not full')
print('Number of full days =',full)
print('Total attendance=',total)