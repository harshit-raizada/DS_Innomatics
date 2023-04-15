import streamlit as st
import pandas as pd
import os
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor

st.header(":red[Laptop] :green[Price] :blue[Prediction]:desktop_computer:")

FILE_DIR1 = os.path.dirname(os.path.abspath(__file__))
FILE_DIR = os.path.join(FILE_DIR1,os.pardir)
dir_of_interest = os.path.join(FILE_DIR, "resource")
DATA_PATH = os.path.join(dir_of_interest, "data")

DATA_PATH1 = os.path.join(DATA_PATH, "cleaned.csv")
df = pd.read_csv(DATA_PATH1)
data = df.copy()

col1, col2, col3 = st.columns(3)

with col1:
    brand = st.selectbox(':green[Select Laptop Brand]', (df.Brand.unique()))

with col2:
    os = st.selectbox(':red[Select Operating System]', (df.OS.unique()))

with col3:
    processor = st.selectbox(':blue[Select Processor]', (df.Processor.unique()))

col1, col2 = st.columns(2)

with col1:
    ram = st.selectbox(':blue[Select Ram]', (df.RAM.unique()))

with col2:
    ramType = st.selectbox(':green[Select Ram Type]', (df.RamType.unique()))

col1, col2 = st.columns(2)

with col1:
    ssd = st.selectbox(':green[Select SSD]', (df.SSD.unique()))

with col2:
    hdd = st.selectbox(':red[Select HDD]', (df.HDD.unique()))

display = st.selectbox(':blue[Select Display Size]', (df.Display.unique()))

sample = pd.DataFrame({"Brand":[brand], "OS":[os], "Processor":[processor], 
                       "RAM":[ram], "SSD":[ssd], 'HDD':[hdd],
                       'RamType':[ramType], 'Display':[display]})

def replace_brand(brand):
    if brand == 'Lenovo':
        return 1
    elif brand == 'ASUS':
        return 2
    elif brand == 'HP':
        return 3
    elif brand == 'DELL':
        return 4
    elif brand == 'RedmiBook':
        return 5
    elif brand == 'realme':
        return 6
    elif brand == 'acer':
        return 7
    elif brand == 'MSI':
        return 8
    elif brand == 'APPLE':
        return 9
    elif brand == 'Infinix':
        return 10
    elif brand == 'SAMSUNG':
        return 11
    elif brand == 'Ultimus':
        return 12
    elif brand == 'Vaio':
        return 13
    elif brand == 'GIGABYTE':
        return 14
    elif brand == 'Nokia':
        return 15
    elif brand == 'ALIENWARE':
        return 16  
    
data['Brand'] = data['Brand'].apply(replace_brand)

def replace_processor(processor):
    if processor == 'Intel Core i5 Processor':
        return 1
    elif processor == 'Intel Core i3 Processor':
        return 2
    elif processor == 'Intel Core i7 Processor':
        return 3
    elif processor == 'AMD Ryzen 5 Hexa Core Processor':
        return 4
    elif processor == 'AMD Ryzen 7 Octa Core Processor':
        return 5
    elif processor == 'Intel Celeron Dual Core Processor':
        return 6
    elif processor == 'AMD Ryzen 3 Dual Core Processor':
        return 7
    elif processor == 'AMD Ryzen 9 Octa Core Processor':
        return 8
    elif processor == 'Intel Core i9 Processor':
        return 9
    elif processor == 'AMD Ryzen 5 Quad Core Processor':
        return 10
    elif processor == 'Apple M1 Processor':
        return 11
    elif processor == 'Apple M1 Pro Processor':
        return 12
    elif processor == 'Intel Pentium Silver Processor':
        return 13
    elif processor == 'AMD Ryzen 3 Quad Core Processor':
        return 14
    elif processor == 'Apple M2 Processor':
        return 15
    elif processor == 'Intel Pentium Quad Core Processor':
        return 16
    elif processor == 'AMD Athlon Dual Core Processor':
        return 17
    elif processor == 'Intel Celeron Quad Core Processor':
        return 18
    elif processor == 'AMD Ryzen 5 Dual Core Processor':
        return 19
    elif processor == 'AMD Ryzen 3 Hexa Core Processor':
        return 20
    elif processor == 'AMD Ryzen 7 Quad Core Processor':
        return 21
    elif processor == 'AMD Dual Core Processor':
        return 22
    elif processor == 'Apple M1 Max Processor':
        return 23
    elif processor == 'Intel Evo Core i5 Processor':
        return 24

data['Processor'] = data['Processor'].apply(replace_processor)

def replace_os(os):
    if os == 'Windows 11':
        return 1
    elif os == 'Windows 10':
        return 2
    elif os == 'Mac':
        return 3
    elif os == 'Chrome':
        return 4
    elif os == 'DOS':
        return 5
    
data['OS'] = data['OS'].apply(replace_os)

def replace_ram_type(ramType):
    if ramType == 'DDR4':
        return 1
    elif ramType =='DDR5':
        return 2
    elif ramType =='LPDDR4':
        return 3
    elif ramType =='Unified':
        return 4
    elif ramType =='LPDDR4X':
        return 5
    elif ramType =='LPDDR5':
        return 6
    elif ramType =='LPDDR3':
        return 7   
    
data['RamType'] = data['RamType'].apply(replace_ram_type)

x = data.drop('MRP', axis=1).values
y = data['MRP'].values

xgb = XGBRegressor()
xgb.fit(x, y)

std = StandardScaler()
std_fit = std.fit(x)
x = std_fit.transform(x)

sample['Brand'] = sample['Brand'].apply(replace_brand)
sample['OS'] = sample['OS'].apply(replace_os)
sample['Processor'] = sample['Processor'].apply(replace_processor)
sample['RamType'] = sample['RamType'].apply(replace_ram_type)

sample = sample.values
sample = std_fit.transform(sample)

if st.button('Predict'):
    price = xgb.predict(sample)[0]
    st.subheader(":blue[Laptop Price For The Selected Features:] :green[{}]".format("₹" + str(price)))
else:
    pass
