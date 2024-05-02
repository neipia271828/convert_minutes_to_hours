
minutes = input("Please type the current time:")

miss = 0
hour = None
minutes_is_int = False

def change_data_type(minutes):
  global miss
  global minutes_is_int
  try:
    minutes = int(minutes)
    minutes_is_int = True
  except ValueError:
    minutes = input("Please type the current time:")
    miss = miss + 1

def calculation_prosess(hour):
  global miss
  global minutes
  global minutes_is_int
  change_data_type(minutes)
  if minutes_is_int == True:
    hour = minutes / 60
    hour = str(hour)
  else:
    miss = miss + 1

def intereface_about_data_type():
  global hour
  global miss
  global minutes_is_int
  while minutes_is_int == False:
    calculation_prosess(hour)
    if miss > 5:
      print("Systemlog:Processing has been interrupted because the system has determined that it cannot continue.")
      break

def cal_hour_to_min():
  intereface_about_data_type()
  print(f"{minutes}minutes is {hour}hours")

cal_hour_to_min()
