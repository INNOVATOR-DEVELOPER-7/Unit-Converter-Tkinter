from tkinter import *
from tkinter import ttk

uni = Tk()
uni.title("Unit Converter")
uni.geometry("500x500")
uni.config(bg= "gold")
uni.resizable(0,0)

def reset():
    input_field.delete(0, END)  
    output_field.delete(0, END)  

    input_value.set(SELECTIONS[0])  
    output_value.set(SELECTIONS[0])

    input_field.focus_set()  

def convert():

    inputVal = float(input_field.get())  
    input_unit = input_value.get()  
    output_unit = output_value.get() 

    conversion_factors = [input_unit in length_units and output_unit in length_units,  
    input_unit in weight_units and output_unit in weight_units,  
    input_unit in temperature_units and output_unit in temperature_units,  
    input_unit in area_units and output_unit in area_units,  
    input_unit in volume_units and output_unit in volume_units]

    if any(conversion_factors):
         
        if input_unit == "Celsius" and output_unit == "Fahrenheit":  
            output_field.delete(0, END)  
            output_field.insert(0, (inputVal * 1.8) + 32)  
        elif input_unit == "fahrenheit" and output_unit == "celsius":
            output_field.delete(0, END)  
            output_field.insert(0, (inputVal - 32) * (5/9))  
        else:  
            output_field.delete(0, END)  
            output_field.insert(0, round(inputVal * unitDict[input_unit] / unitDict[output_unit], 5))  

    else:
        output_field.delete(0, END)  
        output_field.insert(0, "ERROR") 
    


unitDict = {
    "Millimeter" : 0.001,  
    "Centimeter" : 0.01,  
    "Meter" : 1.0,  
    "Kilometer" : 1000.0,  
    "Foot" : 0.3048,  
    "Mile" : 1609.344,  
    "Yard" : 0.9144,  
    "Inch" : 0.0254,  
    "Square Meter" : 1.0,  
    "Square Kilometer" : 1000000.0,  
    "Square Centimeter" : 0.0001,  
    "Square Millimeter" : 0.000001,  
    "Are" : 100.0,  
    "Hectare" : 10000.0,  
    "Acre" : 4046.856,  
    "Square Mile" : 2590000.0,  
    "Square Foot" : 0.0929,  
    "Cubic Meter" : 1000.0,  
    "Cubic Centimeter" : 0.001,  
    "Litre" :  1.0,  
    "Millilitre" : 0.001,  
    "Gallon" : 3.785,  
    "Gram" : 1.0,  
    "Kilogram" : 1000.0,  
    "Milligram" : 0.001,  
    "Quintal" : 100000.0,  
    "Ton" : 1000000.0,  
    "Pound" : 453.592,  
    "Ounce" : 28.3495
    }  

length_units = [
    "Millimeter", "Centimeter", "Meter", "Kilometer", "Foot", "Mile", "Yard", "Inch"
    ]  
temperature_units = [
    "Celsius", "Fahrenheit"
    ]  
area_units = [  
     "Square Meter", "Square Kilometer", "Square Centimeter", "Square Millimeter",  
    "Are", "Hectare", "Acre", "Square Mile", "Square Foot"  
    ]  
volume_units = [  
    "Cubic Meter", "Cubic Centimeter", "Litre", "Millilitre", "Gallon"     
    ]  

weight_units = [  
    "Gram", "Kilogram", "Milligram", "Quintal", "Ton", "Pound", "Ounce"  
    ]  

SELECTIONS = [  
    "Select Unit", 
    "==== Length Unit ====",
    "Millimeter" ,  
    "Centimeter" ,  
    "Meter" ,  
    "Kilometer" ,  
    "Foot" ,  
    "Mile" ,  
    "Yard" ,  
    "Inch" ,
    " ==== Temperature Units ====",
    "Celsius", 
    "Fahrenheit",
    "==== Area Units ====",  
    "Square Meter" ,  
    "Square Kilometer",  
    "Square Centimeter" ,  
    "Square Millimeter" ,  
    "Are" ,  
    "Hectare" ,  
    "Acre" ,  
    "Square Mile" ,  
    "Square Foot" ,
    "==== Volume Units ====",
    "Cubic Meter" ,  
    "Cubic Centimeter" ,  
    "Litre" ,  
    "Millilitre",  
    "Gallon" ,  
    "==== Weight Units ====",
    "Gram" ,  
    "Kilogram",  
    "Milligram" ,  
    "Quintal",  
    "Ton" ,  
    "Pound" ,  
    "Ounce" 
    ]  
  
L1= Label(uni,text= "STANDRAD UNIT CONVERTER",font= ("Bradley Hand ITC",20,"bold"))
L1.config(bg = "gold",fg = 'black')
L1.place(x= 35,y= 30)

input_value = StringVar()  
output_value = StringVar()
    
input_value.set(SELECTIONS[0])  
output_value.set(SELECTIONS[0])

input_label = Label(uni,text = "From",font= ("Bradley Hand ITC", 30,"bold"))
input_label.config(bg = 'gold', fg='black')
input_label.place(x=200,y=100)

output_label = Label( uni,text = "To",font= ("Bradley Hand ITC", 30,"bold"))
output_label.config(bg = 'gold', fg='black')
output_label.place(x= 220,y = 240)

input_field = Entry(uni,bg = "white",font =("Forte",25,'bold') )
input_field.config(width=10)
input_field.place(x= 30,y= 170)

output_field = Entry( uni, bg = "white",font=("Forte",25,'bold')  )  
output_field.config(width = 10)
output_field.place(x = 30, y= 310)

input_menu = OptionMenu(uni,input_value, *SELECTIONS) 
input_menu.config(font= ("Bradley Hand ITC", 18,"bold"))
input_menu.place(x=250, y= 168)

output_menu = OptionMenu(uni,output_value, *SELECTIONS )
output_menu.config(font= ("Bradley Hand ITC", 18,"bold"))
output_menu.place(x=250,y = 308)

convert_button = Button(uni,text = "CONVERT",bg = "green",fg="black", command = convert)
convert_button.config(font= ("Bradley Hand ITC", 19,"bold"))
convert_button.place(x= 260, y= 390)

reset_button = Button(uni,text = "RESET",bg = "red",  fg = "black", command = reset)  
reset_button.config(font=("Bradley Hand ITC",19,"bold"))
reset_button.place(x=100,y=390)  

uni.mainloop()