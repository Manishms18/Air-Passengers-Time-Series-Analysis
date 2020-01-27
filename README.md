# Air-Passengers-Time-Series-Analysis
Forecasting number of passengers for airlines using ARIMA model in python.
You can view the project demo on [YouTube](https://www.youtube.com/watch?v=zkw2CZEssT8).
   
## Table of contents

* [General info](#general-info)
* [Screenshots](#screenshots)
* [Demo](#demo)
* [Methods and Tools](#methods-and-tools)
* [Code Examples](#code-examples)
* [Status](#status)
* [Contact](#contact)
* [Reference](#reference)

## General info

Project was Time Series Analysis, used ARIMA method to build the model.
Major steps involved were as follow :                                 
* STEP: 1 - Data Cleaning and Analysis
* STEP: 2 - Checking Stationarity (ADF Test) 
* STEP: 3 - Transformation  
* STEP: 4 - Differencing
* STEP: 5 - Time Series Components 
* STEP: 6 - Finding ACF and PACF
* STEP: 7 - ARIMA Modeling 
* STEP: 8 - Forecast

## Demo

![Example screenshot](./images/Demo.gif)

**The entire demo of the project can be found on [YouTube](https://www.youtube.com/watch?v=zkw2CZEssT8).**

## Screenshots

![Example screenshot](./images/Image1.png)
![Example screenshot](./images/Image2.png)
![Example screenshot](./images/Image3.png)
![Example screenshot](./images/Image4.png)

## Methods and Tools
* Python 
* Advanced Excel
* ARIMA 
* Augmented Dickey-Fuller Test
* ACF and PACF
* Statsmodels

## Code Examples

````
# Code for Augemneted Dickey-Fuller Test and Rolling Mean to check stationarity  

def stationarity(timeseries):
    
    rolmean=timeseries.rolling(window=12).mean()
    rolstd=timeseries.rolling(window=12).std()
    
    plt.figure(figsize=(20,10))
    actual=plt.plot(timeseries, color='red', label='Actual')
    mean_6=plt.plot(rolmean, color='green', label='Rolling Mean') 
    std_6=plt.plot(rolstd, color='black', label='Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show(block=False)
    
    print('Dickey-Fuller Test: ')
    dftest=adfuller(timeseries['Passengers'], autolag='AIC')
    dfoutput=pd.Series(dftest[0:4], index=['Test Statistic','p-value','Lags Used','No. of Obs'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value
    print(dfoutput)

````

## Status
Project is: _finished_.

## Contact
If you loved what you read here and feel like we can collaborate to produce some exciting stuff, or if you
just want to shoot a question, please feel free to connect with me on 
<a href="mailto:manishshukla.ms18@gmail.com">email</a> or 
<a href="https://www.linkedin.com/in/manishshukla-ms/" target="_blank">LinkedIn</a>

## Reference
* Edureka
