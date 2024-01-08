from datetime import datetime, timedelta

start_date = datetime(2001, 3, 1)
end_date = datetime(2022, 12, 1)

current_date = start_date
file_list = []

while current_date <= end_date:
  filename = f"Great_Slave_Lake_Basin_remapped_{current_date.strftime('%Y-%m-%d-%H-%M-%S')}.nc"
  file_list.append(filename)
  current_date += timedelta(days=31)  # increment by one month approximately

# print the file list
for file in file_list:
  print(file)