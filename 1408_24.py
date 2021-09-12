from datetime import timedelta
import datetime
from sys import stdin

H, M, S = map(int, stdin.readline().rstrip().split(':'))
HH, MM, SS = map(int, stdin.readline().rstrip().split(':'))

nowTime = timedelta(hours=H, minutes=M, seconds=S)
startTime = timedelta(hours=HH, minutes=MM, seconds=SS)

print(':'.join(str(startTime-nowTime).split(':')[:2]))