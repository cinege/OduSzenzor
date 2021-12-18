from datetime import datetime, date, timedelta
import chart_studio.plotly as py
import plotly.graph_objects as go

#intervals
interval = 30
#record count
record_count = 49

now = datetime.now()
minutes_since_midnight = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()/60
today_day_string = now.strftime("%Y.%m.%d")
yesterday_day_string = (now - timedelta(days=1)).strftime("%Y.%m.%d")
filename_today = "/home/pi/sensors/data/" + today_day_string
filename_yesterday = "/home/pi/sensors/data/" + yesterday_day_string

if minutes_since_midnight < interval * 49 :
   with open(filename_yesterday, "r") as yesterday_file_handle:
      yesterday_data = yesterday_file_handle.readlines()
else:
   yesterday_data = []

with open(filename_today, "r") as today_file_handle:
   today_data = today_file_handle.readlines()

data = yesterday_data + today_data

time_list = []
temp_list = []
pres_list = []
tempin_list = []
hum_list = []

length = len(data)
for i in range(length-record_count, length):
   if "," in data[i]:
      time, temp, pres, tempin, hum = data[i].split(",")
      time_list.append(time[5:][:6] + time[-8:][:5])
      temp_list.append(temp)
      pres_list.append(pres)
      tempin_list.append(tempin)
      #hum_list.append(hum)

float_temp_list = [float(i) for i in temp_list]
avg = round(sum(float_temp_list) / len(temp_list),1)
avg_temp_list = [avg] * len(temp_list)

trace0 = go.Scatter(x=time_list,y=temp_list,name="C")
trace01 = go.Scatter(x=time_list,y=avg_temp_list,name="Atlag C")
trace02 = go.Scatter(x=time_list,y=tempin_list,name="Bent C")
trace1 = go.Scatter(x=time_list,y=pres_list)
#trace2 = go.Scatter(x=time_list,y=hum_list)

sent_data0 = [trace0,trace01,trace02]
sent_data1 = [trace1]
#sent_data2 = [trace2]

#layout0=go.Layout(title="Homerseklet", xaxis={'title':''}, yaxis={'title':'C'})
#figure0=go.Figure(data=sent_data0,layout=layout0)


link0 = py.plot(sent_data0, filename = 'homerseklet2', auto_open=True)
link1 = py.plot(sent_data1, filename = 'legnyomas2', auto_open=True)
#link2 = py.plot(sent_data2, filename = 'paratartalom', auto_open=True)

print(link0)
print(link1)
#print(link2)
