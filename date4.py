from datetime import datetime

date1 = datetime(2024, 6, 20, 12, 0, 0)
date2 = datetime(2024, 6, 26, 12, 0, 0) 

difference = date2 - date1
difference_in_seconds = difference.total_seconds()

print(difference_in_seconds) 