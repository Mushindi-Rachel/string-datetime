from datetime import datetime
data_string = "Jun 25 2022 19:20"
date_object = datetime.strptime(data_string, '%b %d %Y %H:%M')
print(date_object)
