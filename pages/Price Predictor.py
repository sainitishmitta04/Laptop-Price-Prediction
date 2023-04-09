import streamlit as st
import pandas as pd
import os
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor


# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "laptop.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "laptop_price.csv")

#Page Heading
st.header(":violet[Laptop Price Prediction]:desktop_computer:")

df = pd.read_csv(DATA_PATH)
data = df.copy()

# Accepting the required features from user
with st.form(key='my_form'):
    brand = st.selectbox(
        'Select Laptop Brand',
        (df.Brand.unique()))

    operating_system = st.selectbox(
        'Select Operating System',
        (df['Operating System'].unique()))

    processor = st.selectbox(
        'Select Processor Type',
        (df['Processor'].unique()))

    ram_type = st.selectbox(
        'Select RAM Type',
        (df['RAM Type'].unique()))

    ram_size = st.selectbox(
        'Select RAM Size',
        (df['RAM Size'].unique()))

    disc_type = st.selectbox(
        'Select DISC Type',
        (df['Disc Type'].unique()))

    disc_size = st.selectbox(
        'Select DISC Size',
        (df['Disc Size'].unique()))

    submitted = st.form_submit_button(label='Submit')

if submitted:
    st.snow()
    st.write('Your Selected Brand:', brand)
    st.write('Your Selected Operating System:', operating_system)
    st.write('Your Selected Processor Type:', processor)
    st.write('Your Selected RAM Type:', ram_type)
    st.write('Your Selected RAM Size:', ram_size)
    st.write('Your Selected DISC Type:', disc_type)
    st.write('Your Selected DISC Size:', disc_size)

#Create dataframe using all these values
sample=pd.DataFrame({"Brand":[brand],"Operating System":[operating_system], "Processor":[processor],
                   "RAM Type":[ram_type], "RAM Size":[ram_size],
                   "Disc Type":[disc_type], "Disc Size":[disc_size]})

#Convert these values to suitable integer form
#Function to change brand to number
def replace_brand(brand):
    if brand=='Lenovo':
        return 1
    elif brand=='ASUS':
        return 2
    elif brand=='HP':
        return 3
    elif brand=='DELL':
        return 4
    elif brand=='RedmiBook':
        return 5
    elif brand=='realme':
        return 6
    elif brand=='acer':
        return 7
    elif brand=='MSI':
        return 8
    elif brand=='APPLE':
        return 9
    elif brand=='Infinix':
        return 10
    elif brand=='SAMSUNG':
        return 11
    elif brand=='Ultimus':
        return 12
    elif brand=='Vaio':
        return 13
    elif brand=='GIGABYTE':
        return 14
    elif brand=='Nokia':
        return 15
    elif brand=='ALIENWARE':
        return 16
data['Brand']=data['Brand'].apply(replace_brand)

#Function to change processor to number
def replace_processor(Processor):
    if Processor=='Intel':
        return 1
    elif Processor=='AMD':
        return 2
    elif Processor=='Apple':
        return 3
    elif Processor=='Qualcomm':
        return 4
data['Processor']=data['Processor'].apply(replace_processor)

#Function to change os to number
def replace_os(os):
    if os=='Windows 11':
        return 1
    elif os=='Windows 10':
        return 2
    elif os=='Mac':
        return 3
    elif os=='Chrome':
        return 4
    elif os=='DOS':
        return 5
data['Operating System']=data['Operating System'].apply(replace_os)

#Function to change ram type to number
def replace_ram_type(ram_type):
    if ram_type=='DDR4':
        return 1
    elif ram_type=='DDR5':
        return 2
    elif ram_type=='LPDDR4':
        return 3
    elif ram_type=='Unified':
        return 4
    elif ram_type=='LPDDR4X':
        return 5
    elif ram_type=='LPDDR5':
        return 6
    elif ram_type=='LPDDR3':
        return 7
data['RAM Type']=data['RAM Type'].apply(replace_ram_type)

#Function to change ram size to number
def replace_ram_size(ram_size):
    if ram_size=='8GB':
        return 1
    elif ram_size=='16GB':
        return 2
    elif ram_size=='4GB':
        return 3
    elif ram_size=='32GB':
        return 4
data['RAM Size']=data['RAM Size'].apply(replace_ram_size)

#Function to disc type to number
def replace_disc_type(disc_type):
    if disc_type=='SSD':
        return 1
    elif disc_type=='HDD':
        return 2
    elif disc_type=='EMMC':
        return 3
data['Disc Type']=data['Disc Type'].apply(replace_disc_type)

#Function to change disc size to number
def replace_disc_size(disc_size):
    if disc_size=='256GB':
        return 1
    elif disc_size=='512GB':
        return 2
    elif disc_size=='1TB':
        return 3
    elif disc_size=='128GB':
        return 4
    elif disc_size=='64GB':
        return 5
    elif disc_size=='32GB':
        return 6
    elif disc_size=='2TB':
        return 7
data['Disc Size']=data['Disc Size'].apply(replace_disc_size)

#Split data into X and y
X=data.drop('MRP', axis=1).values
y=data['MRP'].values

#Standarizing the features
std=StandardScaler()
std_fit=std.fit(X)
X=std_fit.transform(X)

#Train the model
reg = RandomForestRegressor()
reg.fit(X, y)


#Convert User input to suitable integer form
sample['Brand']=sample['Brand'].apply(replace_brand)
sample['Operating System']=sample['Operating System'].apply(replace_os)
sample['Processor']=sample['Processor'].apply(replace_processor)
sample['RAM Type']=sample['RAM Type'].apply(replace_ram_type)
sample['RAM Size']=sample['RAM Size'].apply(replace_ram_size)
sample['Disc Type']=sample['Disc Type'].apply(replace_disc_type)
sample['Disc Size']=sample['Disc Size'].apply(replace_disc_size)

#Standardize the features
sample=sample.values
sample=std_fit.transform(sample)



#Prediction
if st.button('Predict'):
    st.balloons()
    price=reg.predict(sample)
    price=price[0].round(2)
    st.subheader(":violet[Laptop Price For Your Selected Feature :] :green[{}]".format("₹"+str(price)))
else:
    pass

