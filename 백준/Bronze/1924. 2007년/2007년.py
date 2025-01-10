x,y=map(int,input().split())
print(['MON','TUE','WED','THU','FRI','SAT','SUN'][(sum([0,31,28,31,30,31,30,31,31,30,31,30,31][:x])+y-1)%7])

