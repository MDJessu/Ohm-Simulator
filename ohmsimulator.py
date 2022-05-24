import streamlit as st
import matplotlib.pyplot as plt
 
st.set_page_config(layout="wide")

col1, col2, col3 = st.columns(3)

with col1:
    st.write(" ")

with col2:
    st.title('Ohms Law Simulator')

with col3:
    st.write("  ")
 
# VOLTAGE AND VOLTAGE UNITS
# voltage units
stromstatus = st.radio('Select your voltage unit: ',
                  ('mV', 'V', 'MV'))
 
# assigns voltage
if(stromstatus == 'mV'):

    strom = st.number_input('Millivolts') * 0.001
         
elif(stromstatus == 'V'):

    strom = st.number_input('Volts')
         
else:
    strom = st.number_input('Megavolts') * 1000
 
# 3 columns
col1, col2, col3 = st.columns(3)

with col1:
    
    #COL 1
    col1.header("First Resistor")
 
    res1status = st.radio('Select your first resitor unit: ',
                  ('mΩ', 'Ω', 'MΩ'))
 
    if(res1status == 'mΩ'):

        res1 = st.number_input('Milliohms') * 0.001
         
    elif(res1status == 'Ω'):

        res1 = st.number_input('Ohms')
         
    else:

        res1 = st.number_input('Megaohms') * 1000

# COL 2
with col2:
    
    col2.header("Second Resistor")
 
    res2status = st.radio('Select your second resitor unit: ',
                  (' mΩ', ' Ω', ' MΩ'))
 
   
    if(res2status == ' mΩ'):
     
        res2 = st.number_input(' Milliohms') * 0.001
         
    elif(res2status == ' Ω'):
        
        res2 = st.number_input(' Ohms')
         
    else:
  
        res2 = st.number_input(' Megaohms') * 1000

# COL3
with col3:
    
    col3.header("Third Resistor")
 
   
    res3status = st.radio('Select your third resitor unit: ',
                  ('mΩ ', 'Ω ', 'MΩ '))
 
    
    if(res3status == 'mΩ '):
      
        res3 = st.number_input('Milliohms ') * 0.001
        
    elif(res3status == 'Ω '):
          
        res3 = st.number_input('Ohms ')
         
    else:
        
        res3 = st.number_input('Megaohms ') * 1000

#Resistance Instructions

expander = st.expander("See Resistance Instructions")
expander.write("""
     Choose resistance units and resistance for up to 3 resistors. 
     If you would like fewer than 3 resistors set their value to 0.
 """)

restotal = (res1) + (res2) + (res3)
if restotal>0:
    amp = strom / restotal
    
    stromdrop1 = strom - (amp * res1)
    stromdrop2 = stromdrop1 - (amp * res2)
    stromdrop3 = stromdrop2 - (amp * res3)

    voltage = [strom, strom, stromdrop1, stromdrop2, stromdrop3]
    resistors = [0,1,2,3,4]
   
else:
    amp = st.write("Input Voltage and Resistance Values")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("    ")

with col2:
    if(st.button('Calculate Current')):
        
        st.text("The current is {}.".format(amp))

        x = resistors
        y = voltage

        fig, ax = plt.subplots()

        ax.step(x, y, linewidth=1)

        st.pyplot(fig)

with col3:
    st.write("     ")
