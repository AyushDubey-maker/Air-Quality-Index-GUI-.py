from tkinter import *
from PIL import ImageTk,Image
import requests
#AirNow API
import json
root=Tk()
# Mumbai Latitude and Longitude.
# 19.2856
# 72.8691
def getaqi():
  
    try:
        api_requests=requests.get("https://www.airnowapi.org/aq/observation/latLong/current/?format=application/json&latitude="+ str(latitude.get()) +"&longitude="+ str(longitude.get()) +"&distance=25&API_KEY=24AC5342-CE2D-4757-ADC7-D8C4D13A15F2")
        api=json.loads(api_requests.content)
        city=api[0]['ReportingArea']
        quality=api[0]['AQI']
        category=api[0]['Category']['Name']
        if category=='Good':
            weather_color="#0C0"
        elif category=='Moderate':
            weather_color="#FFFF00"
        elif category=='Unhealthy for Sensitive Groups':
            weather_color="#FF9900"
        elif category=='Unhealthy':
            weather_color="#FF0000"
        elif category=='Very Unhealthy':
            weather_color="#990066"
        elif category=='Hazardous':
            weather_color="#660000"
        #root.configure(background=weather_color)
        
        label=Label(root,text=city+"\n"+"Air Quality Index: "+str(quality)+"\n"+category,font=("Helvetica",20),background=weather_color)
        label.grid(row=4,column=0,columnspan=3)
    except Exception :
        api="Error.."

# Image banner for the App.
myImage=Image.open('AQI-Scale.jpeg')
Img=myImage.resize((800,200),Image.ANTIALIAS)
resizedImg=ImageTk.PhotoImage(Img)
imgLabel=Label(image=resizedImg)
imgLabel.grid(row=0,column=0,columnspan=3)
# Latitude TextBoxes
latitude=Entry(root)
latitude.grid(row=1,column=1,padx=10)
longitude=Entry(root)
longitude.grid(row=2,column=1,padx=10)
#Latitude Longitude Labels
latitude_label=Label(root,text="Latitude:")
latitude_label.grid(row=1,column=0,padx=10,columnspan=2)

longitude_label=Label(root,text="Longitude:")
longitude_label.grid(row=2,column=0,padx=10,columnspan=2)

subBtn=Button(root,text="Get AQI",command=getaqi)
subBtn.grid(row=3,column=0,columnspan=3,padx=10,pady=10,ipadx=120)
root.mainloop()