# Segmenting and Clustering Neighborhoods Assignment 
## Applied Data Science Capstone Week 5 Peer-Graded Project Report

By Parth Parekh
March 10 2020

## Introduction to the opportunity
Fredericton is the Capital City of the only Canadian fully-bilingual Province of New Brunswick and is beautifully located on the banks of the Saint John River.  While one of the least populated provincial capital cities with a population base of less than 60 thousand residents, it offers a wide spectrum of venues and is a governement, university and cultural hub.  

As the city grows and develops, it becomes increasingly important to examine and understand it quantitiatively. The City of Fredericton provides open data for everyone and encourages entrepreneurial use to develop services for the benefit of its ciitzens.  

Developers, investors, policy makers and/or city planners have an interest in answering the following questions as the need for additional services and citizen protection:

1. What neighbourhoods have the highest crime?
2. Is population density correlated to crime level?
3. Using Foursquare data, what venues are most common in different locations within the city?
4. Does the Knowledge Park really need a coffee shop?

Does the Open Data project have specific enough or thick enough data to empower decisions to be made or is it too aggregate to provide value in its current detail? Let's find out.


```python
from IPython.display import Image
from IPython.core.display import HTML 
Image(url= "http://www.tourismfredericton.ca/sites/default/files/field/image/fredericton.jpg")
```




<img src="http://www.tourismfredericton.ca/sites/default/files/field/image/fredericton.jpg"/>



## Data 
To understand and explore we will need the following City of Fredericton Open Data:

1. Open Data Site: http://data-fredericton.opendata.arcgis.com/
2. Fredericton Neighbourhoods: http://data-fredericton.opendata.arcgis.com/datasets/neighbourhoods--quartiers
3. Fredericton Crime by Neighbourhood: http://data-fredericton.opendata.arcgis.com/datasets/crime-by-neighbourhood-2017--crime-par-quartier-2017
4. Fredericton Census Tract Demographics: http://data-fredericton.opendata.arcgis.com/datasets/census-tract-demographics--donn%C3%A9es-d%C3%A9mographiques-du-secteur-de-recensement
5. Fredericton locations of interest: https://github.com/JasonLUrquhart/Applied-Data-Science-Capstone/blob/master/Fredericton%20Locations.xlsx
6. Foursquare Developers Access to venue data: https://foursquare.com/

Using this data will allow exploration and examination to answer the questions. The neighbourhood data will enable us to properly group crime by neighbourhood. The Census data will enable us to then compare the population density to examine if areas of highest crime are also most densely populated. Fredericton locations of interest will then allow us to cluster and quantitatively understand the venues most common to that location.


# Methodology
All steps are referenced beleow in the Appendix: Analysis section.

The methodology will include:
1. Loading each data set
2. Examine the crime frequency by neighbourhood
3. Study the crime types and then pivot analysis of crime type frequency by neighbourhood
4. Understand correlation between crimes and population density
5. Perform k-means statisical analysis on venues by locations of interest based on findings from crimes and neighbourhood
6. Determine which venues are most common statistically in the region of greatest crime count then in all other locations of interest.
6. Determine if an area, such as the Knowledge Park needs a coffee shop.



### Loading the data
After loading the applicable libraries, the referenced geojson neighbourhood data was loaded from the City of Fredericton Open Data site.  This dataset uses block polygon shape coordinates which are better for visualization and comparison.  The City also uses Ward data but the Neighbourhood location data is more accurate and includes more details. The same type of dataset was then loaded for the population density from the Stats Canada Census tracts.  

The third dataset, an excel file, "Crime by Neighbourhood 2017" downloaded from the City of Fredericton Open Data site is found under the Public Safety domain.  This dataset was then uploaded for the analysis.  It's interesting to note the details of this dataset are aggregated by neighbourhood.  It is not an exhaustive set by not including all crimes (violent offenses) nor specific location data of the crime but is referenced by neighbourhood.  

This means we can gain an understanding of the crime volume by type by area but not specific enough to understand the distribution properties.  Valuable questions such as, "are these crimes occuring more often in a specific area and at a certain time by a specific demographic of people?" cannot be answered nor explored due to what is reasonably assumed to be personal and private information with associated legal risks.  



There is value to the city to explore the detailed crime data using data science to predict frequency, location, timing and conditions to best allocated resources for the benefit of its citizens and it's police force.  However, human behaviour is complex requiring thick profile data by individual and the conditions surrounding the event(s).  To be sufficient for reliable future prediction it would need to demonstrate validity, currency, reliability and sufficiency.


### Exploring the data
Exploring the count of crimes by neighbourhood gives us the first glimpse into the distribution.

One note is the possibility neighbourhoods names could change at different times.  The crime dataset did not mention which specific neighbourhood naming dataset it was using but we assumed the neighbourhood data provided aligned with the neighbourhoods used in the crime data.  It may be beneficial for the City to note and timestamp neighbourhood naming in the future or simply reference with neighbourhood naming file it used for the crime dataset.

An example of data errors:  There was an error found in the naming of the neighbourhood "Platt".  The neighbourhood data stated "Plat" while the crime data stated "Platt".  Given the crime dataset was most simple to manipulate it was modified to "Plat".  The true name of the neighbourhood is "Platt".


#### First Visualization of Crime
Once the data was prepared, a choropleth map was created to view the crime count by neighbourhood.  As expected the region of greatest crime count was found in the downtown and Platt neighbourhoods.

Examining the crime types enables us to learn the most frequent occuring crimes which we then plot as a bar chart to see most frequenty type.

Theft from motor vehicles is most prevalent in the same area as the most frequent crimes.  It's interesting to note this area is mostly residential and most do not have garages.  It would be interesting to further examine if surveillance is a deterant for motor vehicle crimes in the downtown core compared to low surveillance in the Platt neighbourhood.



#### Examining 2nd most common crime given it is specific: theft from vehicles
After exploring the pivot table showing Crime_Type by Neighbourhood, we drill into a specific type of crime, theft from vehicles and plot the choropleth map to see which area has the greatest frequency. 

Again, the Platt neighbourhood appears as the most frequent.

Is this due to population density?

#### Introducing the Census data to explore the correlation between crime frequency and population density.
Visualising the population density enables us to determine that the Platt neighbourhood has lower correlation to crime frequency than I would have expected.

It would be interesting to further study the Census data and if this captures the population that is renting or more temporary/transient poplution, given the City is a University hub.



### Look at specific locations to understand the connection to venues using Foursquare data
Loading the "Fredericton Locations" data enables us to perform a statistical analysis on the most common venues by location.

We might wonder if the prevalence of bars and clubs in the downtown region has something to do with the higher crime rate in the near Platt region.

Plotting the latitude and longitude coordinates of the locations of interest onto the crime choropleth map enables us to now study the most common venues by using the Foursquare data.

#### Analysing each Location
Grouping rows by location and the mean of the frequency of occurance of each category we venue categories we study the top five most common venues.

Putting this data into a pandas dataframe we can then determine the most common venues by location and plot onto a map.

## Results
The analysis enabled us to discover and describe visually and quantitatively:
1. Neighbourhoods in Fredericton

2. Crime freqency by neighbourhood

3. Crime type frequency and statistics.  The mean crime count in the City of Fredericton is 22.

4. Crime type count by neighbourhood.  
Theft from motor vehicles is most prevalent in the same area as the most frequent crimes. It's interesting to note this area is mostly residential and most do not have garages. It would be interesting to further examine if surveillance is a deterant for motor vehicle crimes in the downtown core compared to low surveillance in the Platt neighbourhood.


5. Motor Vehicle crimes less than $5000 analysis by neighbourhood and resulting statistics.  
The most common crime is **Other Theft less than 5k** followed by **Motor Vehicle Theft less than 5k**.
There is a mean of 6 motor vehicle thefts less than 5k by neighbourhood in the City.

6. That population density and resulting visual correlation is not strongly correlated to crime frequency.  Causation for crime is not able to be determined given lack of open data specificity by individual and environment.

7. Using k-menas, we were able to determine the top 10 most common venues within a 1 km radius of the centroid of the highest crime neighbourhood.  **The most common venues in the highest crime neighbourhood are coffee shops followed by Pubs and Bars**.    

While, it is not valid, consistent, reliable or sufficient to assume a higher concentration of the combination of coffee shops, bars and clubs predicts the amount of crime occurance in the City of Fredericton, this may be a part of the model needed to be able to in the future.

8. We were able to determine the top 10 most common venues by location of interest.

9. Statisically, we determined there are no coffee shops within the Knowledge Park clusters.   

## Discussion and Recommendations

The City of Fredericton Open Data enables us to gain an understanding of the crime volume by type by area but not specific enough to understand the distribution properties. Valuable questions such as, "are these crimes occuring more often in a specific area and at a certain time by a specific demographic of people?" cannot be answered nor explored due to what is reasonably assumed to be personal and private information with associated legal risks.

There is value to the city to explore the detailed crime data using data science to predict frequency, location, timing and conditions to best allocated resources for the benefit of its citizens and it's police force. However, human behaviour is complex requiring thick profile data by individual and the conditions surrounding the event(s). To be sufficient for reliable future prediction it would need to demonstrate validity, currency, reliability and sufficiency.

A note of caution is the possibility neighbourhoods names could change. The crime dataset did not mention which specific neighbourhood naming dataset it was using but we assumed the neighbourhood data provided aligned with the neighbourhoods used in the crime data. It may be beneficial for the City to note and timestamp neighbourhood naming in the future or simply reference with neighbourhood naming file it used for the crime dataset.





Errors exist in the current open data. An error was found in the naming of the neighbourhood "Platt". 
The neighbourhood data stated "Plat" while the crime data stated "Platt". Given the crime dataset was most simple to manipulate it was modified to "Plat". The true name of the neighbourhood is "Platt".

Theft from motor vehicles is most prevalent in the same area as the most frequent crimes. 
It is interesting to note this area is mostly residential and most do not have garages. It would be interesting to further examine if surveillance is a deterant for motor vehicle crimes in the downtown core compared to low surveillance in the Platt neighbourhood.

It would be interesting to further study the Census data and if this captures the population that is renting or more temporary/transient poplution, given the City is a University hub.

Given the findings of the top 10 most frequent venues by locations of interest, the Knowledge Park does not have Coffee Shops in the top 10 most common venues as determined from the Foursquare dataset.  Given this area has the greatest concentration of stores and shops as venues, it would be safe to assume a coffee shop would be beneficial to the business community and the citizens of Fredericton.

## Conclusion
Using a combination of datasets from the City of Fredericton Open Data project and Foursquare venue data we were able to analyse, discover and describe neighbhourhoods, crime, population density and statistically describe quantitatively venues by locations of interest.

While overall, the City of Fredericton Open Data is interesting, it misses the details required for true valued quantitiatve analysis and predictive analytics which would be most valued by investors and developers to make appropriate investments and to minimize risk.

The Open Data project is a great start and empowers the need for a "Citizens Like Me" model to be developed where citizens of digital Fredericton are able to share their data as they wish for detailed analysis that enables the creation of valued services.


# APPENDIX:  Analysis


### Load Libraries


```python
import numpy as np # library to handle data in a vectorized manner

import pandas as pd # library for data analysis
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

import json # library to handle JSON files

!conda install -c conda-forge geopy --yes # uncomment this line if you haven't completed the Foursquare API lab
from geopy.geocoders import Nominatim # convert an address into latitude and longitude values

import requests # library to handle requests
from pandas.io.json import json_normalize # tranform JSON file into a pandas dataframe

# Matplotlib and associated plotting modules
import matplotlib.cm as cm
import matplotlib.colors as colors

# import k-means from clustering stage
from sklearn.cluster import KMeans

# for webscraping import Beautiful Soup 
from bs4 import BeautifulSoup

import xml

!conda install -c conda-forge folium=0.5.0 --yes 
import folium # map rendering library

print('Libraries imported.')
```

    Solving environment: done
    
    # All requested packages already installed.
    
    Solving environment: done
    
    # All requested packages already installed.
    
    Libraries imported.



```python
r = requests.get('https://opendata.arcgis.com/datasets/823d86e17a6d47808c6e4f1c2dd97928_0.geojson')
fredericton_geo = r.json()
```


```python
neighborhoods_data = fredericton_geo['features']
```


```python
neighborhoods_data[0]
```




    {'type': 'Feature',
     'properties': {'FID': 1,
      'OBJECTID': 1,
      'Neighbourh': 'Fredericton South',
      'Shape_Leng': 40412.2767429,
      'Shape_Area': 32431889.0002},
     'geometry': {'type': 'Polygon',
      'coordinates': [[[-66.6193489311946, 45.8688925859664],
        [-66.5986068312843, 45.8934317575498],
        [-66.5998465063764, 45.8962889533894],
        [-66.6005561754508, 45.8987959122414],
        [-66.6007627879662, 45.9004150599189],
        [-66.6005112596866, 45.9020341603803],
        [-66.5993703992758, 45.9049409211054],
        [-66.5983912356161, 45.9066536507875],
        [-66.5950405196063, 45.9110977503182],
        [-66.5924713378938, 45.9137165396725],
        [-66.5975198697905, 45.9151915074375],
        [-66.6016161874861, 45.9165914405789],
        [-66.6063862416448, 45.9184662957134],
        [-66.6102310310608, 45.9201848572716],
        [-66.6193938469588, 45.9264149777787],
        [-66.6194297795702, 45.9243466803461],
        [-66.6206694546623, 45.9221345790227],
        [-66.6241459348118, 45.9181100781124],
        [-66.6249634017204, 45.9177976046497],
        [-66.6258796833102, 45.917910095299],
        [-66.6292124330143, 45.9200348758374],
        [-66.632733828928, 45.9225720071846],
        [-66.6356353872957, 45.924409167803],
        [-66.6362731911474, 45.9249840491044],
        [-66.6381955858555, 45.9258900999313],
        [-66.6400281490351, 45.9272147820915],
        [-66.6469721261813, 45.9309512150791],
        [-66.6492628301558, 45.9324257247173],
        [-66.6501521622871, 45.9331254782868],
        [-66.6504306400252, 45.9337564984884],
        [-66.6505653873178, 45.9347436246005],
        [-66.6503587748024, 45.9357182382069],
        [-66.6520745569951, 45.9352246860213],
        [-66.6532513500173, 45.9350872403269],
        [-66.6541855979128, 45.9351122304785],
        [-66.6557756159657, 45.9353808738969],
        [-66.6597461695215, 45.9365616400027],
        [-66.6692323789218, 45.9408659130747],
        [-66.6702205257343, 45.9411720097543],
        [-66.6705888350008, 45.9415718069541],
        [-66.6717027459531, 45.9418654061867],
        [-66.6805601346545, 45.9456570693391],
        [-66.6808206460869, 45.945613344883],
        [-66.690998558256, 45.9498794400526],
        [-66.6932353633134, 45.9503791076107],
        [-66.6956697977334, 45.9504478115476],
        [-66.6955530167465, 45.9498607024316],
        [-66.695014027576, 45.9498607024316],
        [-66.6956248819692, 45.948261735435],
        [-66.699766115429, 45.9452510552052],
        [-66.6993978061625, 45.9450511702315],
        [-66.6996762839006, 45.9448512845371],
        [-66.6992271262585, 45.9446139193389],
        [-66.7022364824603, 45.9407722096716],
        [-66.7041049782513, 45.9393666396225],
        [-66.7046080348104, 45.9387919073835],
        [-66.7061441539463, 45.9390980155132],
        [-66.7051919397451, 45.9388543785676],
        [-66.7056949963042, 45.937405028971],
        [-66.706611277894, 45.9362430230541],
        [-66.7074107784969, 45.9356745059121],
        [-66.7087133356588, 45.9350435075345],
        [-66.7110938711618, 45.9342063302882],
        [-66.7122526978783, 45.9309262230525],
        [-66.7096026677901, 45.9293891917718],
        [-66.6746402369322, 45.9061285859908],
        [-66.6193489311946, 45.8688925859664]],
       [[-66.6934150263703, 45.938648223393],
        [-66.7001973067654, 45.9422339647247],
        [-66.6939180829294, 45.9467626619838],
        [-66.6912141539242, 45.9449262417569],
        [-66.6899475293736, 45.9445014828376],
        [-66.6890312477838, 45.9444702504357],
        [-66.6889683657139, 45.9443827996167],
        [-66.6899565125264, 45.9418404190785],
        [-66.6934150263703, 45.938648223393]],
       [[-66.6550120479742, 45.9291455121693],
        [-66.6557756159657, 45.9292704762017],
        [-66.6599797314954, 45.9309387190672],
        [-66.6629172224744, 45.9322757763752],
        [-66.6631867170597, 45.932475707408],
        [-66.6631238349898, 45.9327880982037],
        [-66.6619290756619, 45.9341813397283],
        [-66.6616146653125, 45.9340751297235],
        [-66.6601863440107, 45.934818595486],
        [-66.6591442982811, 45.9350997354041],
        [-66.6586053091106, 45.9351059829416],
        [-66.6564673187345, 45.9348748235837],
        [-66.6542933957469, 45.9340501391045],
        [-66.6529908385849, 45.9333129107794],
        [-66.652308118969, 45.9324569639043],
        [-66.652191337982, 45.9319696305845],
        [-66.6522721863576, 45.9313573339335],
        [-66.6520476075366, 45.9305825815444],
        [-66.6521284559121, 45.9301264722544],
        [-66.6524428662616, 45.9296016295261],
        [-66.6531166027247, 45.9293392062996],
        [-66.6540508506202, 45.9291580085852],
        [-66.6550120479742, 45.9291455121693]],
       [[-66.6318085641854, 45.8878357293373],
        [-66.6328775593735, 45.8879357750148],
        [-66.6341801165354, 45.8882108996987],
        [-66.6351502970423, 45.8885422980769],
        [-66.6362462416889, 45.8890987927924],
        [-66.6370098096804, 45.8896365239624],
        [-66.6381596532441, 45.8909183040123],
        [-66.6385818614276, 45.8918186586532],
        [-66.6387435581788, 45.8925689430378],
        [-66.6385908445805, 45.8940757335582],
        [-66.6327517952337, 45.900733882662],
        [-66.62923039932, 45.9050971942525],
        [-66.6276673307256, 45.9064848805016],
        [-66.626454605092, 45.9071974626627],
        [-66.6253856099039, 45.9076662617274],
        [-66.6230230407067, 45.9082913209882],
        [-66.6205077579111, 45.9084913384651],
        [-66.6180014582685, 45.9082413165064],
        [-66.6181092561025, 45.9082100636823],
        [-66.6170312777616, 45.9076037554142],
        [-66.6161239793246, 45.9068661756028],
        [-66.6150909167479, 45.9054972515047],
        [-66.6147944727041, 45.9047533927481],
        [-66.6146417591058, 45.9037907372083],
        [-66.6146956580229, 45.9030155998367],
        [-66.614974135761, 45.9020654166814],
        [-66.617345688111, 45.8989772091164],
        [-66.6203819937714, 45.8954199312614],
        [-66.6263468072579, 45.8892363524244],
        [-66.6281254715205, 45.8883672199348],
        [-66.6291315846387, 45.8880795903605],
        [-66.6304521081064, 45.8878732464875],
        [-66.6318085641854, 45.8878357293373]]]}}




```python
g = requests.get('https://opendata.arcgis.com/datasets/6179d35eacb144a5b5fdcc869f86dfb5_0.geojson')
demog_geo = g.json()
```


```python
demog_data = demog_geo['features']
demog_data[0]
```




    {'type': 'Feature',
     'properties': {'FID': 1,
      'OBJECTID': 501,
      'DBUID': '1310024304',
      'DAUID': '13100243',
      'CDUID': '1310',
      'CTUID': '3200002.00',
      'CTNAME': '0002.00',
      'DBuid_1': '1310024304',
      'DBpop2011': 60,
      'DBtdwell20': 25,
      'DBurdwell2': 22,
      'Shape_Leng': 0.00746165241824,
      'Shape_Area': 2.81310751889e-06,
      'CTIDLINK': 3200002,
      'Shape__Area': 2.81310897700361e-06,
      'Shape__Length': 0.00746165464503067},
     'geometry': {'type': 'Polygon',
      'coordinates': [[[-66.634784212921, 45.9519239912381],
        [-66.6351046935752, 45.9507605156138],
        [-66.6378263667982, 45.9510868696778],
        [-66.636944377136, 45.9521037018384],
        [-66.634784212921, 45.9519239912381]]]}}




```python

```


```python
import os
os.listdir('.')
```




    ['Capstone Project Course.ipynb',
     'Fredericton_Census_Tract_Demographics.csv',
     '.DS_Store',
     'Fredericton_Census_Tract_Demographics.xlsx',
     'Crime_by_neighbourhood_2017.xlsx',
     'Capstone Fredericton Crime and Police Station Location.ipynb',
     'Boston_Neighborhoods (1).geojson',
     'Fredericton Locations.xlsx',
     'Week 3 Capstone - Segmenting and Clustering Neighbourhoods in Toronto_Part 2.ipynb',
     'Fredericton.jpg',
     'Week 3 Capstone - Segmenting and Clustering Neighbourhoods in Toronto_Part 2.pdf',
     'Boston_Neighborhoods.geojson',
     '.ipynb_checkpoints',
     '.git',
     'Week 3 Capstone - Segmenting and Clustering Neighbourhoods in Toronto.ipynb',
     'Week 4 Capstone - Segmenting and Clustering Neighbourhoods in Boston.ipynb',
     'Week 3 Capstone - Segmenting and Clustering Neighbourhoods in Toronto_Part 2.htm',
     'Week 4 Capstone - Segmenting and Clustering Neighbourhoods in Fredericton.ipynb',
     'Week 4 Capstone - Segmenting and Clustering Neighbourhoods in Fredericton - Github submit.ipynb',
     'Week 3 Capstone - Segmenting and Clustering Neighbourhoods in Toronto_Part 2_files']




```python
opencrime = 'Crime_by_neighbourhood_2017.xlsx'
```


```python
workbook = pd.ExcelFile(opencrime)
print(workbook.sheet_names)
```

    ['Crime_by_neighbourhood_2017']



```python
crime_df = workbook.parse('Crime_by_neighbourhood_2017')
crime_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Neighbourhood</th>
      <th>From_Date</th>
      <th>To_Date</th>
      <th>Crime_Code</th>
      <th>Crime_Type</th>
      <th>Ward</th>
      <th>City</th>
      <th>FID</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Fredericton South</td>
      <td>2017-01-05T00:00:00.000Z</td>
      <td>2017-01-26T00:00:00.000Z</td>
      <td>2120</td>
      <td>B&amp;E NON-RESIDNCE</td>
      <td>7</td>
      <td>Fredericton</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Fredericton South</td>
      <td>2017-03-04T00:00:00.000Z</td>
      <td>2017-03-06T00:00:00.000Z</td>
      <td>2120</td>
      <td>B&amp;E NON-RESIDNCE</td>
      <td>7</td>
      <td>Fredericton</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Fredericton South</td>
      <td>2017-05-07T00:00:00.000Z</td>
      <td>NaN</td>
      <td>2120</td>
      <td>B&amp;E NON-RESIDNCE</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Fredericton South</td>
      <td>2017-06-20T00:00:00.000Z</td>
      <td>2017-06-21T00:00:00.000Z</td>
      <td>2120</td>
      <td>B&amp;E NON-RESIDNCE</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Fredericton South</td>
      <td>2017-07-09T00:00:00.000Z</td>
      <td>2017-07-10T00:00:00.000Z</td>
      <td>2120</td>
      <td>B&amp;E NON-RESIDNCE</td>
      <td>7</td>
      <td>Fredericton</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
crime_df.drop(['From_Date', 'To_Date'], axis=1,inplace=True)
```

## What is the crime count by neighbourhood?


```python
crime_data = crime_df.groupby(['Neighbourhood']).size().to_frame(name='Count').reset_index()
crime_data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Neighbourhood</th>
      <th>Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Barkers Point</td>
      <td>47</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Brookside</td>
      <td>54</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Brookside Estates</td>
      <td>9</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Brookside Mini Home Park</td>
      <td>5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>College Hill</td>
      <td>41</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Colonial heights</td>
      <td>9</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Cotton Mill Creek</td>
      <td>4</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Diamond Street</td>
      <td>1</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Doak Road</td>
      <td>1</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Douglas</td>
      <td>3</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Downtown</td>
      <td>127</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Dun's Crossing</td>
      <td>18</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Forest Hill</td>
      <td>12</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Fredericton South</td>
      <td>85</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Fulton Heights</td>
      <td>36</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Garden Creek</td>
      <td>13</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Garden Place</td>
      <td>4</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Gilridge Estates</td>
      <td>3</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Golf Club</td>
      <td>7</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Grasse Circle</td>
      <td>1</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Greenwood Minihome Park</td>
      <td>2</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Hanwell North</td>
      <td>8</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Heron Springs</td>
      <td>3</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Highpoint Ridge</td>
      <td>5</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Kelly's Court Minihome Park</td>
      <td>1</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Knob Hill</td>
      <td>4</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Knowledge Park</td>
      <td>1</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Lian / Valcore</td>
      <td>7</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Lincoln</td>
      <td>13</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Lincoln Heights</td>
      <td>14</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Main Street</td>
      <td>78</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Marysville</td>
      <td>39</td>
    </tr>
    <tr>
      <th>32</th>
      <td>McKnight</td>
      <td>4</td>
    </tr>
    <tr>
      <th>33</th>
      <td>McLeod Hill</td>
      <td>3</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Monteith / Talisman</td>
      <td>12</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Montogomery / Prospect East</td>
      <td>16</td>
    </tr>
    <tr>
      <th>36</th>
      <td>Nashwaaksis</td>
      <td>25</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Nethervue Minihome Park</td>
      <td>1</td>
    </tr>
    <tr>
      <th>38</th>
      <td>North Devon</td>
      <td>113</td>
    </tr>
    <tr>
      <th>39</th>
      <td>Northbrook Heights</td>
      <td>10</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Plat</td>
      <td>198</td>
    </tr>
    <tr>
      <th>41</th>
      <td>Poet's Hill</td>
      <td>4</td>
    </tr>
    <tr>
      <th>42</th>
      <td>Prospect</td>
      <td>81</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Rail Side</td>
      <td>3</td>
    </tr>
    <tr>
      <th>44</th>
      <td>Regiment Creek</td>
      <td>1</td>
    </tr>
    <tr>
      <th>45</th>
      <td>Royal Road</td>
      <td>7</td>
    </tr>
    <tr>
      <th>46</th>
      <td>Saint Mary's First Nation</td>
      <td>25</td>
    </tr>
    <tr>
      <th>47</th>
      <td>Saint Thomas University</td>
      <td>1</td>
    </tr>
    <tr>
      <th>48</th>
      <td>Sandyville</td>
      <td>9</td>
    </tr>
    <tr>
      <th>49</th>
      <td>Serenity Lane</td>
      <td>2</td>
    </tr>
    <tr>
      <th>50</th>
      <td>Shadowood Estates</td>
      <td>5</td>
    </tr>
    <tr>
      <th>51</th>
      <td>Silverwood</td>
      <td>12</td>
    </tr>
    <tr>
      <th>52</th>
      <td>Skyline Acrea</td>
      <td>27</td>
    </tr>
    <tr>
      <th>53</th>
      <td>South Devon</td>
      <td>68</td>
    </tr>
    <tr>
      <th>54</th>
      <td>Southwood Park</td>
      <td>16</td>
    </tr>
    <tr>
      <th>55</th>
      <td>Springhill</td>
      <td>1</td>
    </tr>
    <tr>
      <th>56</th>
      <td>Sunshine Gardens</td>
      <td>10</td>
    </tr>
    <tr>
      <th>57</th>
      <td>The Hill</td>
      <td>44</td>
    </tr>
    <tr>
      <th>58</th>
      <td>The Hugh John Flemming Forestry Center</td>
      <td>3</td>
    </tr>
    <tr>
      <th>59</th>
      <td>University Of New Brunswick</td>
      <td>15</td>
    </tr>
    <tr>
      <th>60</th>
      <td>Waterloo Row</td>
      <td>9</td>
    </tr>
    <tr>
      <th>61</th>
      <td>Wesbett / Case</td>
      <td>1</td>
    </tr>
    <tr>
      <th>62</th>
      <td>West Hills</td>
      <td>5</td>
    </tr>
    <tr>
      <th>63</th>
      <td>Williams / Hawkins Area</td>
      <td>17</td>
    </tr>
    <tr>
      <th>64</th>
      <td>Woodstock Road</td>
      <td>41</td>
    </tr>
    <tr>
      <th>65</th>
      <td>Youngs Crossing</td>
      <td>16</td>
    </tr>
  </tbody>
</table>
</div>




```python
crime_data.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>66.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>22.121212</td>
    </tr>
    <tr>
      <th>std</th>
      <td>34.879359</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>9.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>23.250000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>198.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
crime_data.rename(index=str, columns={'Neighbourhood':'Neighbourh','Count':'Crime_Count'}, inplace=True)
crime_data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Neighbourh</th>
      <th>Crime_Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Barkers Point</td>
      <td>47</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Brookside</td>
      <td>54</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Brookside Estates</td>
      <td>9</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Brookside Mini Home Park</td>
      <td>5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>College Hill</td>
      <td>41</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Colonial heights</td>
      <td>9</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Cotton Mill Creek</td>
      <td>4</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Diamond Street</td>
      <td>1</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Doak Road</td>
      <td>1</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Douglas</td>
      <td>3</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Downtown</td>
      <td>127</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Dun's Crossing</td>
      <td>18</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Forest Hill</td>
      <td>12</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Fredericton South</td>
      <td>85</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Fulton Heights</td>
      <td>36</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Garden Creek</td>
      <td>13</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Garden Place</td>
      <td>4</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Gilridge Estates</td>
      <td>3</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Golf Club</td>
      <td>7</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Grasse Circle</td>
      <td>1</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Greenwood Minihome Park</td>
      <td>2</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Hanwell North</td>
      <td>8</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Heron Springs</td>
      <td>3</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Highpoint Ridge</td>
      <td>5</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Kelly's Court Minihome Park</td>
      <td>1</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Knob Hill</td>
      <td>4</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Knowledge Park</td>
      <td>1</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Lian / Valcore</td>
      <td>7</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Lincoln</td>
      <td>13</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Lincoln Heights</td>
      <td>14</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Main Street</td>
      <td>78</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Marysville</td>
      <td>39</td>
    </tr>
    <tr>
      <th>32</th>
      <td>McKnight</td>
      <td>4</td>
    </tr>
    <tr>
      <th>33</th>
      <td>McLeod Hill</td>
      <td>3</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Monteith / Talisman</td>
      <td>12</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Montogomery / Prospect East</td>
      <td>16</td>
    </tr>
    <tr>
      <th>36</th>
      <td>Nashwaaksis</td>
      <td>25</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Nethervue Minihome Park</td>
      <td>1</td>
    </tr>
    <tr>
      <th>38</th>
      <td>North Devon</td>
      <td>113</td>
    </tr>
    <tr>
      <th>39</th>
      <td>Northbrook Heights</td>
      <td>10</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Plat</td>
      <td>198</td>
    </tr>
    <tr>
      <th>41</th>
      <td>Poet's Hill</td>
      <td>4</td>
    </tr>
    <tr>
      <th>42</th>
      <td>Prospect</td>
      <td>81</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Rail Side</td>
      <td>3</td>
    </tr>
    <tr>
      <th>44</th>
      <td>Regiment Creek</td>
      <td>1</td>
    </tr>
    <tr>
      <th>45</th>
      <td>Royal Road</td>
      <td>7</td>
    </tr>
    <tr>
      <th>46</th>
      <td>Saint Mary's First Nation</td>
      <td>25</td>
    </tr>
    <tr>
      <th>47</th>
      <td>Saint Thomas University</td>
      <td>1</td>
    </tr>
    <tr>
      <th>48</th>
      <td>Sandyville</td>
      <td>9</td>
    </tr>
    <tr>
      <th>49</th>
      <td>Serenity Lane</td>
      <td>2</td>
    </tr>
    <tr>
      <th>50</th>
      <td>Shadowood Estates</td>
      <td>5</td>
    </tr>
    <tr>
      <th>51</th>
      <td>Silverwood</td>
      <td>12</td>
    </tr>
    <tr>
      <th>52</th>
      <td>Skyline Acrea</td>
      <td>27</td>
    </tr>
    <tr>
      <th>53</th>
      <td>South Devon</td>
      <td>68</td>
    </tr>
    <tr>
      <th>54</th>
      <td>Southwood Park</td>
      <td>16</td>
    </tr>
    <tr>
      <th>55</th>
      <td>Springhill</td>
      <td>1</td>
    </tr>
    <tr>
      <th>56</th>
      <td>Sunshine Gardens</td>
      <td>10</td>
    </tr>
    <tr>
      <th>57</th>
      <td>The Hill</td>
      <td>44</td>
    </tr>
    <tr>
      <th>58</th>
      <td>The Hugh John Flemming Forestry Center</td>
      <td>3</td>
    </tr>
    <tr>
      <th>59</th>
      <td>University Of New Brunswick</td>
      <td>15</td>
    </tr>
    <tr>
      <th>60</th>
      <td>Waterloo Row</td>
      <td>9</td>
    </tr>
    <tr>
      <th>61</th>
      <td>Wesbett / Case</td>
      <td>1</td>
    </tr>
    <tr>
      <th>62</th>
      <td>West Hills</td>
      <td>5</td>
    </tr>
    <tr>
      <th>63</th>
      <td>Williams / Hawkins Area</td>
      <td>17</td>
    </tr>
    <tr>
      <th>64</th>
      <td>Woodstock Road</td>
      <td>41</td>
    </tr>
    <tr>
      <th>65</th>
      <td>Youngs Crossing</td>
      <td>16</td>
    </tr>
  </tbody>
</table>
</div>




```python
crime_data.rename({'Platt': 'Plat'},inplace=True)
crime_data.rename(index=str, columns={'Neighbourhood':'Neighbourh','Count':'Crime_Count'}, inplace=True)
crime_data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Neighbourh</th>
      <th>Crime_Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Barkers Point</td>
      <td>47</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Brookside</td>
      <td>54</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Brookside Estates</td>
      <td>9</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Brookside Mini Home Park</td>
      <td>5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>College Hill</td>
      <td>41</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Colonial heights</td>
      <td>9</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Cotton Mill Creek</td>
      <td>4</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Diamond Street</td>
      <td>1</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Doak Road</td>
      <td>1</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Douglas</td>
      <td>3</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Downtown</td>
      <td>127</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Dun's Crossing</td>
      <td>18</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Forest Hill</td>
      <td>12</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Fredericton South</td>
      <td>85</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Fulton Heights</td>
      <td>36</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Garden Creek</td>
      <td>13</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Garden Place</td>
      <td>4</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Gilridge Estates</td>
      <td>3</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Golf Club</td>
      <td>7</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Grasse Circle</td>
      <td>1</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Greenwood Minihome Park</td>
      <td>2</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Hanwell North</td>
      <td>8</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Heron Springs</td>
      <td>3</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Highpoint Ridge</td>
      <td>5</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Kelly's Court Minihome Park</td>
      <td>1</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Knob Hill</td>
      <td>4</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Knowledge Park</td>
      <td>1</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Lian / Valcore</td>
      <td>7</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Lincoln</td>
      <td>13</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Lincoln Heights</td>
      <td>14</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Main Street</td>
      <td>78</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Marysville</td>
      <td>39</td>
    </tr>
    <tr>
      <th>32</th>
      <td>McKnight</td>
      <td>4</td>
    </tr>
    <tr>
      <th>33</th>
      <td>McLeod Hill</td>
      <td>3</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Monteith / Talisman</td>
      <td>12</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Montogomery / Prospect East</td>
      <td>16</td>
    </tr>
    <tr>
      <th>36</th>
      <td>Nashwaaksis</td>
      <td>25</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Nethervue Minihome Park</td>
      <td>1</td>
    </tr>
    <tr>
      <th>38</th>
      <td>North Devon</td>
      <td>113</td>
    </tr>
    <tr>
      <th>39</th>
      <td>Northbrook Heights</td>
      <td>10</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Plat</td>
      <td>198</td>
    </tr>
    <tr>
      <th>41</th>
      <td>Poet's Hill</td>
      <td>4</td>
    </tr>
    <tr>
      <th>42</th>
      <td>Prospect</td>
      <td>81</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Rail Side</td>
      <td>3</td>
    </tr>
    <tr>
      <th>44</th>
      <td>Regiment Creek</td>
      <td>1</td>
    </tr>
    <tr>
      <th>45</th>
      <td>Royal Road</td>
      <td>7</td>
    </tr>
    <tr>
      <th>46</th>
      <td>Saint Mary's First Nation</td>
      <td>25</td>
    </tr>
    <tr>
      <th>47</th>
      <td>Saint Thomas University</td>
      <td>1</td>
    </tr>
    <tr>
      <th>48</th>
      <td>Sandyville</td>
      <td>9</td>
    </tr>
    <tr>
      <th>49</th>
      <td>Serenity Lane</td>
      <td>2</td>
    </tr>
    <tr>
      <th>50</th>
      <td>Shadowood Estates</td>
      <td>5</td>
    </tr>
    <tr>
      <th>51</th>
      <td>Silverwood</td>
      <td>12</td>
    </tr>
    <tr>
      <th>52</th>
      <td>Skyline Acrea</td>
      <td>27</td>
    </tr>
    <tr>
      <th>53</th>
      <td>South Devon</td>
      <td>68</td>
    </tr>
    <tr>
      <th>54</th>
      <td>Southwood Park</td>
      <td>16</td>
    </tr>
    <tr>
      <th>55</th>
      <td>Springhill</td>
      <td>1</td>
    </tr>
    <tr>
      <th>56</th>
      <td>Sunshine Gardens</td>
      <td>10</td>
    </tr>
    <tr>
      <th>57</th>
      <td>The Hill</td>
      <td>44</td>
    </tr>
    <tr>
      <th>58</th>
      <td>The Hugh John Flemming Forestry Center</td>
      <td>3</td>
    </tr>
    <tr>
      <th>59</th>
      <td>University Of New Brunswick</td>
      <td>15</td>
    </tr>
    <tr>
      <th>60</th>
      <td>Waterloo Row</td>
      <td>9</td>
    </tr>
    <tr>
      <th>61</th>
      <td>Wesbett / Case</td>
      <td>1</td>
    </tr>
    <tr>
      <th>62</th>
      <td>West Hills</td>
      <td>5</td>
    </tr>
    <tr>
      <th>63</th>
      <td>Williams / Hawkins Area</td>
      <td>17</td>
    </tr>
    <tr>
      <th>64</th>
      <td>Woodstock Road</td>
      <td>41</td>
    </tr>
    <tr>
      <th>65</th>
      <td>Youngs Crossing</td>
      <td>16</td>
    </tr>
  </tbody>
</table>
</div>




```python
address = 'Fredericton, Canada'

geolocator = Nominatim()
location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude
print('The geograpical coordinate of Fredericton, New Brunswick is {}, {}.'.format(latitude, longitude))
```

    /anaconda3/lib/python3.7/site-packages/ipykernel_launcher.py:3: DeprecationWarning: Using Nominatim with the default "geopy/1.18.1" `user_agent` is strongly discouraged, as it violates Nominatim's ToS https://operations.osmfoundation.org/policies/nominatim/ and may possibly cause 403 and 429 HTTP errors. Please specify a custom `user_agent` with `Nominatim(user_agent="my-application")` or by overriding the default `user_agent`: `geopy.geocoders.options.default_user_agent = "my-application"`. In geopy 2.0 this will become an exception.
      This is separate from the ipykernel package so we can avoid doing imports until


    The geograpical coordinate of Fredericton, New Brunswick is 45.966425, -66.645813.



```python
world_geo = r'world_countries.json' # geojson file

fredericton_1_map = folium.Map(location=[45.97, -66.65], width=1000, height=750,zoom_start=12)

fredericton_1_map
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><iframe src="data:text/html;charset=utf-8;base64,PCFET0NUWVBFIGh0bWw+CjxoZWFkPiAgICAKICAgIDxtZXRhIGh0dHAtZXF1aXY9ImNvbnRlbnQtdHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PVVURi04IiAvPgogICAgPHNjcmlwdD5MX1BSRUZFUl9DQU5WQVMgPSBmYWxzZTsgTF9OT19UT1VDSCA9IGZhbHNlOyBMX0RJU0FCTEVfM0QgPSBmYWxzZTs8L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2FqYXguZ29vZ2xlYXBpcy5jb20vYWpheC9saWJzL2pxdWVyeS8xLjExLjEvanF1ZXJ5Lm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvanMvYm9vdHN0cmFwLm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvTGVhZmxldC5hd2Vzb21lLW1hcmtlcnMvMi4wLjIvbGVhZmxldC5hd2Vzb21lLW1hcmtlcnMuanMiPjwvc2NyaXB0PgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9jc3MvYm9vdHN0cmFwLm1pbi5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvY3NzL2Jvb3RzdHJhcC10aGVtZS5taW4uY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vbWF4Y2RuLmJvb3RzdHJhcGNkbi5jb20vZm9udC1hd2Vzb21lLzQuNi4zL2Nzcy9mb250LWF3ZXNvbWUubWluLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9MZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy8yLjAuMi9sZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9yYXdnaXQuY29tL3B5dGhvbi12aXN1YWxpemF0aW9uL2ZvbGl1bS9tYXN0ZXIvZm9saXVtL3RlbXBsYXRlcy9sZWFmbGV0LmF3ZXNvbWUucm90YXRlLmNzcyIvPgogICAgPHN0eWxlPmh0bWwsIGJvZHkge3dpZHRoOiAxMDAlO2hlaWdodDogMTAwJTttYXJnaW46IDA7cGFkZGluZzogMDt9PC9zdHlsZT4KICAgIDxzdHlsZT4jbWFwIHtwb3NpdGlvbjphYnNvbHV0ZTt0b3A6MDtib3R0b206MDtyaWdodDowO2xlZnQ6MDt9PC9zdHlsZT4KICAgIAogICAgICAgICAgICA8c3R5bGU+ICNtYXBfMmIyNGQ0YWM3MWM2NDY1NTkyMzNlOTljYjU0ZTNlOTIgewogICAgICAgICAgICAgICAgcG9zaXRpb24gOiByZWxhdGl2ZTsKICAgICAgICAgICAgICAgIHdpZHRoIDogMTAwMC4wcHg7CiAgICAgICAgICAgICAgICBoZWlnaHQ6IDc1MC4wcHg7CiAgICAgICAgICAgICAgICBsZWZ0OiAwLjAlOwogICAgICAgICAgICAgICAgdG9wOiAwLjAlOwogICAgICAgICAgICAgICAgfQogICAgICAgICAgICA8L3N0eWxlPgogICAgICAgIAo8L2hlYWQ+Cjxib2R5PiAgICAKICAgIAogICAgICAgICAgICA8ZGl2IGNsYXNzPSJmb2xpdW0tbWFwIiBpZD0ibWFwXzJiMjRkNGFjNzFjNjQ2NTU5MjMzZTk5Y2I1NGUzZTkyIiA+PC9kaXY+CiAgICAgICAgCjwvYm9keT4KPHNjcmlwdD4gICAgCiAgICAKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGJvdW5kcyA9IG51bGw7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgdmFyIG1hcF8yYjI0ZDRhYzcxYzY0NjU1OTIzM2U5OWNiNTRlM2U5MiA9IEwubWFwKAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ21hcF8yYjI0ZDRhYzcxYzY0NjU1OTIzM2U5OWNiNTRlM2U5MicsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB7Y2VudGVyOiBbNDUuOTcsLTY2LjY1XSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHpvb206IDEyLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbWF4Qm91bmRzOiBib3VuZHMsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBsYXllcnM6IFtdLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgd29ybGRDb3B5SnVtcDogZmFsc2UsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBjcnM6IEwuQ1JTLkVQU0czODU3CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIH0pOwogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgdGlsZV9sYXllcl83OTkxZjQ0NjJjNWY0ZjBiYjkxMzg4MWQzNDUyYTM3MiA9IEwudGlsZUxheWVyKAogICAgICAgICAgICAgICAgJ2h0dHBzOi8ve3N9LnRpbGUub3BlbnN0cmVldG1hcC5vcmcve3p9L3t4fS97eX0ucG5nJywKICAgICAgICAgICAgICAgIHsKICAiYXR0cmlidXRpb24iOiBudWxsLAogICJkZXRlY3RSZXRpbmEiOiBmYWxzZSwKICAibWF4Wm9vbSI6IDE4LAogICJtaW5ab29tIjogMSwKICAibm9XcmFwIjogZmFsc2UsCiAgInN1YmRvbWFpbnMiOiAiYWJjIgp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8yYjI0ZDRhYzcxYzY0NjU1OTIzM2U5OWNiNTRlM2U5Mik7CiAgICAgICAgCjwvc2NyaXB0Pg==" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>




```python
fredericton_geo = r.json()

threshold_scale = np.linspace(crime_data['Crime_Count'].min(),crime_data['Crime_Count'].max(), 6,dtype=int)
threshold_scale = threshold_scale.tolist()
threshold_scale[-1] = threshold_scale[-1]+1

fredericton_1_map.choropleth(geo_data=fredericton_geo, data=crime_data,columns=['Neighbourh', 'Crime_Count'],
    key_on='feature.properties.Neighbourh', threshold_scale=threshold_scale,fill_color='YlOrRd', fill_opacity=0.7, 
    line_opacity=0.1, legend_name='Fredericton Neighbourhoods')

fredericton_1_map
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><iframe src="data:text/html;charset=utf-8;base64,PCFET0NUWVBFIGh0bWw+CjxoZWFkPiAgICAKICAgIDxtZXRhIGh0dHAtZXF1aXY9ImNvbnRlbnQtdHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PVVURi04IiAvPgogICAgPHNjcmlwdD5MX1BSRUZFUl9DQU5WQVMgPSBmYWxzZTsgTF9OT19UT1VDSCA9IGZhbHNlOyBMX0RJU0FCTEVfM0QgPSBmYWxzZTs8L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2FqYXguZ29vZ2xlYXBpcy5jb20vYWpheC9saWJzL2pxdWVyeS8xLjExLjEvanF1ZXJ5Lm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvanMvYm9vdHN0cmFwLm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvTGVhZmxldC5hd2Vzb21lLW1hcmtlcnMvMi4wLjIvbGVhZmxldC5hd2Vzb21lLW1hcmtlcnMuanMiPjwvc2NyaXB0PgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9jc3MvYm9vdHN0cmFwLm1pbi5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvY3NzL2Jvb3RzdHJhcC10aGVtZS5taW4uY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vbWF4Y2RuLmJvb3RzdHJhcGNkbi5jb20vZm9udC1hd2Vzb21lLzQuNi4zL2Nzcy9mb250LWF3ZXNvbWUubWluLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9MZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy8yLjAuMi9sZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9yYXdnaXQuY29tL3B5dGhvbi12aXN1YWxpemF0aW9uL2ZvbGl1bS9tYXN0ZXIvZm9saXVtL3RlbXBsYXRlcy9sZWFmbGV0LmF3ZXNvbWUucm90YXRlLmNzcyIvPgogICAgPHN0eWxlPmh0bWwsIGJvZHkge3dpZHRoOiAxMDAlO2hlaWdodDogMTAwJTttYXJnaW46IDA7cGFkZGluZzogMDt9PC9zdHlsZT4KICAgIDxzdHlsZT4jbWFwIHtwb3NpdGlvbjphYnNvbHV0ZTt0b3A6MDtib3R0b206MDtyaWdodDowO2xlZnQ6MDt9PC9zdHlsZT4KICAgIAogICAgICAgICAgICA8c3R5bGU+ICNtYXBfMmIyNGQ0YWM3MWM2NDY1NTkyMzNlOTljYjU0ZTNlOTIgewogICAgICAgICAgICAgICAgcG9zaXRpb24gOiByZWxhdGl2ZTsKICAgICAgICAgICAgICAgIHdpZHRoIDogMTAwMC4wcHg7CiAgICAgICAgICAgICAgICBoZWlnaHQ6IDc1MC4wcHg7CiAgICAgICAgICAgICAgICBsZWZ0OiAwLjAlOwogICAgICAgICAgICAgICAgdG9wOiAwLjAlOwogICAgICAgICAgICAgICAgfQogICAgICAgICAgICA8L3N0eWxlPgogICAgICAgIAogICAgPHNjcmlwdCBzcmM9Imh0dHBzOi8vY2RuanMuY2xvdWRmbGFyZS5jb20vYWpheC9saWJzL2QzLzMuNS41L2QzLm1pbi5qcyI+PC9zY3JpcHQ+CjwvaGVhZD4KPGJvZHk+ICAgIAogICAgCiAgICAgICAgICAgIDxkaXYgY2xhc3M9ImZvbGl1bS1tYXAiIGlkPSJtYXBfMmIyNGQ0YWM3MWM2NDY1NTkyMzNlOTljYjU0ZTNlOTIiID48L2Rpdj4KICAgICAgICAKPC9ib2R5Pgo8c2NyaXB0PiAgICAKICAgIAoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgYm91bmRzID0gbnVsbDsKICAgICAgICAgICAgCgogICAgICAgICAgICB2YXIgbWFwXzJiMjRkNGFjNzFjNjQ2NTU5MjMzZTk5Y2I1NGUzZTkyID0gTC5tYXAoCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAnbWFwXzJiMjRkNGFjNzFjNjQ2NTU5MjMzZTk5Y2I1NGUzZTkyJywKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHtjZW50ZXI6IFs0NS45NywtNjYuNjVdLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgem9vbTogMTIsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBtYXhCb3VuZHM6IGJvdW5kcywKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGxheWVyczogW10sCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB3b3JsZENvcHlKdW1wOiBmYWxzZSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGNyczogTC5DUlMuRVBTRzM4NTcKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgfSk7CiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciB0aWxlX2xheWVyXzc5OTFmNDQ2MmM1ZjRmMGJiOTEzODgxZDM0NTJhMzcyID0gTC50aWxlTGF5ZXIoCiAgICAgICAgICAgICAgICAnaHR0cHM6Ly97c30udGlsZS5vcGVuc3RyZWV0bWFwLm9yZy97en0ve3h9L3t5fS5wbmcnLAogICAgICAgICAgICAgICAgewogICJhdHRyaWJ1dGlvbiI6IG51bGwsCiAgImRldGVjdFJldGluYSI6IGZhbHNlLAogICJtYXhab29tIjogMTgsCiAgIm1pblpvb20iOiAxLAogICJub1dyYXAiOiBmYWxzZSwKICAic3ViZG9tYWlucyI6ICJhYmMiCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzJiMjRkNGFjNzFjNjQ2NTU5MjMzZTk5Y2I1NGUzZTkyKTsKICAgICAgICAKICAgIAoKICAgICAgICAgICAgCgogICAgICAgICAgICAgICAgdmFyIGdlb19qc29uXzk2NjY0MDlkMTI2YTQ5MjU5NTNiZDdhNjRkY2QxZGUzID0gTC5nZW9Kc29uKAogICAgICAgICAgICAgICAgICAgIHsiZmVhdHVyZXMiOiBbeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjE5MzQ4OTMxMTk0NiwgNDUuODY4ODkyNTg1OTY2NF0sIFstNjYuNTk4NjA2ODMxMjg0MywgNDUuODkzNDMxNzU3NTQ5OF0sIFstNjYuNTk5ODQ2NTA2Mzc2NCwgNDUuODk2Mjg4OTUzMzg5NF0sIFstNjYuNjAwNTU2MTc1NDUwOCwgNDUuODk4Nzk1OTEyMjQxNF0sIFstNjYuNjAwNzYyNzg3OTY2MiwgNDUuOTAwNDE1MDU5OTE4OV0sIFstNjYuNjAwNTExMjU5Njg2NiwgNDUuOTAyMDM0MTYwMzgwM10sIFstNjYuNTk5MzcwMzk5Mjc1OCwgNDUuOTA0OTQwOTIxMTA1NF0sIFstNjYuNTk4MzkxMjM1NjE2MSwgNDUuOTA2NjUzNjUwNzg3NV0sIFstNjYuNTk1MDQwNTE5NjA2MywgNDUuOTExMDk3NzUwMzE4Ml0sIFstNjYuNTkyNDcxMzM3ODkzOCwgNDUuOTEzNzE2NTM5NjcyNV0sIFstNjYuNTk3NTE5ODY5NzkwNSwgNDUuOTE1MTkxNTA3NDM3NV0sIFstNjYuNjAxNjE2MTg3NDg2MSwgNDUuOTE2NTkxNDQwNTc4OV0sIFstNjYuNjA2Mzg2MjQxNjQ0OCwgNDUuOTE4NDY2Mjk1NzEzNF0sIFstNjYuNjEwMjMxMDMxMDYwOCwgNDUuOTIwMTg0ODU3MjcxNl0sIFstNjYuNjE5MzkzODQ2OTU4OCwgNDUuOTI2NDE0OTc3Nzc4N10sIFstNjYuNjE5NDI5Nzc5NTcwMiwgNDUuOTI0MzQ2NjgwMzQ2MV0sIFstNjYuNjIwNjY5NDU0NjYyMywgNDUuOTIyMTM0NTc5MDIyN10sIFstNjYuNjI0MTQ1OTM0ODExOCwgNDUuOTE4MTEwMDc4MTEyNF0sIFstNjYuNjI0OTYzNDAxNzIwNCwgNDUuOTE3Nzk3NjA0NjQ5N10sIFstNjYuNjI1ODc5NjgzMzEwMiwgNDUuOTE3OTEwMDk1Mjk5XSwgWy02Ni42MjkyMTI0MzMwMTQzLCA0NS45MjAwMzQ4NzU4Mzc0XSwgWy02Ni42MzI3MzM4Mjg5MjgsIDQ1LjkyMjU3MjAwNzE4NDZdLCBbLTY2LjYzNTYzNTM4NzI5NTcsIDQ1LjkyNDQwOTE2NzgwM10sIFstNjYuNjM2MjczMTkxMTQ3NCwgNDUuOTI0OTg0MDQ5MTA0NF0sIFstNjYuNjM4MTk1NTg1ODU1NSwgNDUuOTI1ODkwMDk5OTMxM10sIFstNjYuNjQwMDI4MTQ5MDM1MSwgNDUuOTI3MjE0NzgyMDkxNV0sIFstNjYuNjQ2OTcyMTI2MTgxMywgNDUuOTMwOTUxMjE1MDc5MV0sIFstNjYuNjQ5MjYyODMwMTU1OCwgNDUuOTMyNDI1NzI0NzE3M10sIFstNjYuNjUwMTUyMTYyMjg3MSwgNDUuOTMzMTI1NDc4Mjg2OF0sIFstNjYuNjUwNDMwNjQwMDI1MiwgNDUuOTMzNzU2NDk4NDg4NF0sIFstNjYuNjUwNTY1Mzg3MzE3OCwgNDUuOTM0NzQzNjI0NjAwNV0sIFstNjYuNjUwMzU4Nzc0ODAyNCwgNDUuOTM1NzE4MjM4MjA2OV0sIFstNjYuNjUyMDc0NTU2OTk1MSwgNDUuOTM1MjI0Njg2MDIxM10sIFstNjYuNjUzMjUxMzUwMDE3MywgNDUuOTM1MDg3MjQwMzI2OV0sIFstNjYuNjU0MTg1NTk3OTEyOCwgNDUuOTM1MTEyMjMwNDc4NV0sIFstNjYuNjU1Nzc1NjE1OTY1NywgNDUuOTM1MzgwODczODk2OV0sIFstNjYuNjU5NzQ2MTY5NTIxNSwgNDUuOTM2NTYxNjQwMDAyN10sIFstNjYuNjY5MjMyMzc4OTIxOCwgNDUuOTQwODY1OTEzMDc0N10sIFstNjYuNjcwMjIwNTI1NzM0MywgNDUuOTQxMTcyMDA5NzU0M10sIFstNjYuNjcwNTg4ODM1MDAwOCwgNDUuOTQxNTcxODA2OTU0MV0sIFstNjYuNjcxNzAyNzQ1OTUzMSwgNDUuOTQxODY1NDA2MTg2N10sIFstNjYuNjgwNTYwMTM0NjU0NSwgNDUuOTQ1NjU3MDY5MzM5MV0sIFstNjYuNjgwODIwNjQ2MDg2OSwgNDUuOTQ1NjEzMzQ0ODgzXSwgWy02Ni42OTA5OTg1NTgyNTYsIDQ1Ljk0OTg3OTQ0MDA1MjZdLCBbLTY2LjY5MzIzNTM2MzMxMzQsIDQ1Ljk1MDM3OTEwNzYxMDddLCBbLTY2LjY5NTY2OTc5NzczMzQsIDQ1Ljk1MDQ0NzgxMTU0NzZdLCBbLTY2LjY5NTU1MzAxNjc0NjUsIDQ1Ljk0OTg2MDcwMjQzMTZdLCBbLTY2LjY5NTAxNDAyNzU3NiwgNDUuOTQ5ODYwNzAyNDMxNl0sIFstNjYuNjk1NjI0ODgxOTY5MiwgNDUuOTQ4MjYxNzM1NDM1XSwgWy02Ni42OTk3NjYxMTU0MjksIDQ1Ljk0NTI1MTA1NTIwNTJdLCBbLTY2LjY5OTM5NzgwNjE2MjUsIDQ1Ljk0NTA1MTE3MDIzMTVdLCBbLTY2LjY5OTY3NjI4MzkwMDYsIDQ1Ljk0NDg1MTI4NDUzNzFdLCBbLTY2LjY5OTIyNzEyNjI1ODUsIDQ1Ljk0NDYxMzkxOTMzODldLCBbLTY2LjcwMjIzNjQ4MjQ2MDMsIDQ1Ljk0MDc3MjIwOTY3MTZdLCBbLTY2LjcwNDEwNDk3ODI1MTMsIDQ1LjkzOTM2NjYzOTYyMjVdLCBbLTY2LjcwNDYwODAzNDgxMDQsIDQ1LjkzODc5MTkwNzM4MzVdLCBbLTY2LjcwNjE0NDE1Mzk0NjMsIDQ1LjkzOTA5ODAxNTUxMzJdLCBbLTY2LjcwNTE5MTkzOTc0NTEsIDQ1LjkzODg1NDM3ODU2NzZdLCBbLTY2LjcwNTY5NDk5NjMwNDIsIDQ1LjkzNzQwNTAyODk3MV0sIFstNjYuNzA2NjExMjc3ODk0LCA0NS45MzYyNDMwMjMwNTQxXSwgWy02Ni43MDc0MTA3Nzg0OTY5LCA0NS45MzU2NzQ1MDU5MTIxXSwgWy02Ni43MDg3MTMzMzU2NTg4LCA0NS45MzUwNDM1MDc1MzQ1XSwgWy02Ni43MTEwOTM4NzExNjE4LCA0NS45MzQyMDYzMzAyODgyXSwgWy02Ni43MTIyNTI2OTc4NzgzLCA0NS45MzA5MjYyMjMwNTI1XSwgWy02Ni43MDk2MDI2Njc3OTAxLCA0NS45MjkzODkxOTE3NzE4XSwgWy02Ni42NzQ2NDAyMzY5MzIyLCA0NS45MDYxMjg1ODU5OTA4XSwgWy02Ni42MTkzNDg5MzExOTQ2LCA0NS44Njg4OTI1ODU5NjY0XV0sIFtbLTY2LjY5MzQxNTAyNjM3MDMsIDQ1LjkzODY0ODIyMzM5M10sIFstNjYuNzAwMTk3MzA2NzY1NCwgNDUuOTQyMjMzOTY0NzI0N10sIFstNjYuNjkzOTE4MDgyOTI5NCwgNDUuOTQ2NzYyNjYxOTgzOF0sIFstNjYuNjkxMjE0MTUzOTI0MiwgNDUuOTQ0OTI2MjQxNzU2OV0sIFstNjYuNjg5OTQ3NTI5MzczNiwgNDUuOTQ0NTAxNDgyODM3Nl0sIFstNjYuNjg5MDMxMjQ3NzgzOCwgNDUuOTQ0NDcwMjUwNDM1N10sIFstNjYuNjg4OTY4MzY1NzEzOSwgNDUuOTQ0MzgyNzk5NjE2N10sIFstNjYuNjg5OTU2NTEyNTI2NCwgNDUuOTQxODQwNDE5MDc4NV0sIFstNjYuNjkzNDE1MDI2MzcwMywgNDUuOTM4NjQ4MjIzMzkzXV0sIFtbLTY2LjY1NTAxMjA0Nzk3NDIsIDQ1LjkyOTE0NTUxMjE2OTNdLCBbLTY2LjY1NTc3NTYxNTk2NTcsIDQ1LjkyOTI3MDQ3NjIwMTddLCBbLTY2LjY1OTk3OTczMTQ5NTQsIDQ1LjkzMDkzODcxOTA2NzJdLCBbLTY2LjY2MjkxNzIyMjQ3NDQsIDQ1LjkzMjI3NTc3NjM3NTJdLCBbLTY2LjY2MzE4NjcxNzA1OTcsIDQ1LjkzMjQ3NTcwNzQwOF0sIFstNjYuNjYzMTIzODM0OTg5OCwgNDUuOTMyNzg4MDk4MjAzN10sIFstNjYuNjYxOTI5MDc1NjYxOSwgNDUuOTM0MTgxMzM5NzI4M10sIFstNjYuNjYxNjE0NjY1MzEyNSwgNDUuOTM0MDc1MTI5NzIzNV0sIFstNjYuNjYwMTg2MzQ0MDEwNywgNDUuOTM0ODE4NTk1NDg2XSwgWy02Ni42NTkxNDQyOTgyODExLCA0NS45MzUwOTk3MzU0MDQxXSwgWy02Ni42NTg2MDUzMDkxMTA2LCA0NS45MzUxMDU5ODI5NDE2XSwgWy02Ni42NTY0NjczMTg3MzQ1LCA0NS45MzQ4NzQ4MjM1ODM3XSwgWy02Ni42NTQyOTMzOTU3NDY5LCA0NS45MzQwNTAxMzkxMDQ1XSwgWy02Ni42NTI5OTA4Mzg1ODQ5LCA0NS45MzMzMTI5MTA3Nzk0XSwgWy02Ni42NTIzMDgxMTg5NjksIDQ1LjkzMjQ1Njk2MzkwNDNdLCBbLTY2LjY1MjE5MTMzNzk4MiwgNDUuOTMxOTY5NjMwNTg0NV0sIFstNjYuNjUyMjcyMTg2MzU3NiwgNDUuOTMxMzU3MzMzOTMzNV0sIFstNjYuNjUyMDQ3NjA3NTM2NiwgNDUuOTMwNTgyNTgxNTQ0NF0sIFstNjYuNjUyMTI4NDU1OTEyMSwgNDUuOTMwMTI2NDcyMjU0NF0sIFstNjYuNjUyNDQyODY2MjYxNiwgNDUuOTI5NjAxNjI5NTI2MV0sIFstNjYuNjUzMTE2NjAyNzI0NywgNDUuOTI5MzM5MjA2Mjk5Nl0sIFstNjYuNjU0MDUwODUwNjIwMiwgNDUuOTI5MTU4MDA4NTg1Ml0sIFstNjYuNjU1MDEyMDQ3OTc0MiwgNDUuOTI5MTQ1NTEyMTY5M11dLCBbWy02Ni42MzE4MDg1NjQxODU0LCA0NS44ODc4MzU3MjkzMzczXSwgWy02Ni42MzI4Nzc1NTkzNzM1LCA0NS44ODc5MzU3NzUwMTQ4XSwgWy02Ni42MzQxODAxMTY1MzU0LCA0NS44ODgyMTA4OTk2OTg3XSwgWy02Ni42MzUxNTAyOTcwNDIzLCA0NS44ODg1NDIyOTgwNzY5XSwgWy02Ni42MzYyNDYyNDE2ODg5LCA0NS44ODkwOTg3OTI3OTI0XSwgWy02Ni42MzcwMDk4MDk2ODA0LCA0NS44ODk2MzY1MjM5NjI0XSwgWy02Ni42MzgxNTk2NTMyNDQxLCA0NS44OTA5MTgzMDQwMTIzXSwgWy02Ni42Mzg1ODE4NjE0Mjc2LCA0NS44OTE4MTg2NTg2NTMyXSwgWy02Ni42Mzg3NDM1NTgxNzg4LCA0NS44OTI1Njg5NDMwMzc4XSwgWy02Ni42Mzg1OTA4NDQ1ODA1LCA0NS44OTQwNzU3MzM1NTgyXSwgWy02Ni42MzI3NTE3OTUyMzM3LCA0NS45MDA3MzM4ODI2NjJdLCBbLTY2LjYyOTIzMDM5OTMyLCA0NS45MDUwOTcxOTQyNTI1XSwgWy02Ni42Mjc2NjczMzA3MjU2LCA0NS45MDY0ODQ4ODA1MDE2XSwgWy02Ni42MjY0NTQ2MDUwOTIsIDQ1LjkwNzE5NzQ2MjY2MjddLCBbLTY2LjYyNTM4NTYwOTkwMzksIDQ1LjkwNzY2NjI2MTcyNzRdLCBbLTY2LjYyMzAyMzA0MDcwNjcsIDQ1LjkwODI5MTMyMDk4ODJdLCBbLTY2LjYyMDUwNzc1NzkxMTEsIDQ1LjkwODQ5MTMzODQ2NTFdLCBbLTY2LjYxODAwMTQ1ODI2ODUsIDQ1LjkwODI0MTMxNjUwNjRdLCBbLTY2LjYxODEwOTI1NjEwMjUsIDQ1LjkwODIxMDA2MzY4MjNdLCBbLTY2LjYxNzAzMTI3Nzc2MTYsIDQ1LjkwNzYwMzc1NTQxNDJdLCBbLTY2LjYxNjEyMzk3OTMyNDYsIDQ1LjkwNjg2NjE3NTYwMjhdLCBbLTY2LjYxNTA5MDkxNjc0NzksIDQ1LjkwNTQ5NzI1MTUwNDddLCBbLTY2LjYxNDc5NDQ3MjcwNDEsIDQ1LjkwNDc1MzM5Mjc0ODFdLCBbLTY2LjYxNDY0MTc1OTEwNTgsIDQ1LjkwMzc5MDczNzIwODNdLCBbLTY2LjYxNDY5NTY1ODAyMjksIDQ1LjkwMzAxNTU5OTgzNjddLCBbLTY2LjYxNDk3NDEzNTc2MSwgNDUuOTAyMDY1NDE2NjgxNF0sIFstNjYuNjE3MzQ1Njg4MTExLCA0NS44OTg5NzcyMDkxMTY0XSwgWy02Ni42MjAzODE5OTM3NzE0LCA0NS44OTU0MTk5MzEyNjE0XSwgWy02Ni42MjYzNDY4MDcyNTc5LCA0NS44ODkyMzYzNTI0MjQ0XSwgWy02Ni42MjgxMjU0NzE1MjA1LCA0NS44ODgzNjcyMTk5MzQ4XSwgWy02Ni42MjkxMzE1ODQ2Mzg3LCA0NS44ODgwNzk1OTAzNjA1XSwgWy02Ni42MzA0NTIxMDgxMDY0LCA0NS44ODc4NzMyNDY0ODc1XSwgWy02Ni42MzE4MDg1NjQxODU0LCA0NS44ODc4MzU3MjkzMzczXV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiAxLCAiTmVpZ2hib3VyaCI6ICJGcmVkZXJpY3RvbiBTb3V0aCIsICJPQkpFQ1RJRCI6IDEsICJTaGFwZV9BcmVhIjogMzI0MzE4ODkuMDAwMiwgIlNoYXBlX0xlbmciOiA0MDQxMi4yNzY3NDI5LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZDhkM2MiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjYzNTcxNjIzNTY3MTMsIDQ2LjAwODY5MDU3MjYyMzVdLCBbLTY2LjY0MDYzOTAwMzQyODMsIDQ2LjAwMjk3NTEzMTYwMzVdLCBbLTY2LjYzOTMxODQ3OTk2MDYsIDQ2LjAwMjM4ODU3OTEzODNdLCBbLTY2LjYzODIyMjUzNTMxNCwgNDYuMDAxNjE0ODE5NTY1Nl0sIFstNjYuNjM3Mzg3MTAyMDk5OCwgNDYuMDAwNjk3NTI2MDUzOF0sIFstNjYuNjM2ODU3MDk2MDgyMSwgNDUuOTk5Njc0MTMzMDMxNF0sIFstNjYuNjM2ODMwMTQ2NjIzNiwgNDUuOTk4ODUwNDEyNzAzM10sIFstNjYuNjM3MDI3Nzc1OTg2MSwgNDUuOTk3ODM5NDY2NDQ5OF0sIFstNjYuNjM3NDQ5OTg0MTY5NiwgNDUuOTk2ODU5NzA0NjE3Ml0sIFstNjYuNjM4MTA1NzU0MzI3LCA0NS45OTU5NDIzMzIyNzE0XSwgWy02Ni42Mzg5NzcxMjAxNTI2LCA0NS45OTUxMTIzMTU2MTU5XSwgWy02Ni42NDAwMTkxNjU4ODIyLCA0NS45OTQ0MDA4NjI4NTk3XSwgWy02Ni42NDEyODU3OTA0MzI4LCA0NS45OTM4MDE3Mzc2NTVdLCBbLTY2LjY0Mjk2NTY0MDAxNDEsIDQ1Ljk5MzE4Mzg4Mjk5NDNdLCBbLTY2LjY0NDc1MzI4NzQyOTUsIDQ1Ljk5MjcyMjA0NzczMjldLCBbLTY2LjY0NjYxMjgwMDA2NzcsIDQ1Ljk5MjQyMjQ3Njg1NF0sIFstNjYuNjQ4NTA4MjQ1MzE3MiwgNDUuOTkyMjg1MTcyOTkyNV0sIFstNjYuNjUwMDI2Mzk4MTQ3MywgNDUuOTkyMzAzODk2MjY2NF0sIFstNjYuNjUxNzY5MTI5Nzk4NSwgNDUuOTkwMzU2NjQxODU2M10sIFstNjYuNjQ1MjIwNDExMzc3MywgNDUuOTkxMTI0MzE3NjQwOF0sIFstNjYuNjQzMTM2MzE5OTE4MSwgNDUuOTkxMTExODM1MTkyOV0sIFstNjYuNjQxMDk3MTQ0MjIzMiwgNDUuOTkwODYyMTg1NjQzM10sIFstNjYuNjM5Nzc2NjIwNzU1NSwgNDUuOTkwNTYyNjA0Njk3M10sIFstNjYuNjM4MjA0NTY5MDA4MywgNDUuOTkwMDUwODE2ODNdLCBbLTY2LjYzNjE2NTM5MzMxMzMsIDQ1Ljk4ODgwMjUzMzg5MjFdLCBbLTY2LjYzNTE5NTIxMjgwNjUsIDQ1Ljk4ODM5NjgzNTg3NThdLCBbLTY2LjYzMzg5MjY1NTY0NDUsIDQ1Ljk4ODExNTk2NjI3NjVdLCBbLTY2LjYzMjc2OTc2MTUzOTQsIDQ1Ljk4ODA2NjAzMzc1NDFdLCBbLTY2LjYzMTg3MTQ0NjI1NTIsIDQ1Ljk4ODE1MzQxNTYzODhdLCBbLTY2LjYzMDY0MDc1NDMxNiwgNDUuOTg3OTE2MjM1OTE2Nl0sIFstNjYuNjI5MDc3Njg1NzIxNiwgNDUuOTg3MzE3MDQwNTEyOF0sIFstNjYuNjI3NjQ5MzY0NDE5OSwgNDUuOTg2MzEyMTI1MzI3MV0sIFstNjYuNjI1Nzg5ODUxNzgxOCwgNDUuOTg1NjgxNzAzMzgzMV0sIFstNjYuNjIzODMxNTI0NDYyNCwgNDUuOTg1MjA3MzIxNzQxXSwgWy02Ni41OTk2MDM5NjEyNDk3LCA0Ni4wMTQ5OTE4NDgxODQ4XSwgWy02Ni42MjMxMDM4ODkwODIyLCA0Ni4wMjIxMjIwMjk3MjcyXSwgWy02Ni42NjY0NjU1Njc4NDY3LCA0Ni4wMjA0MTkxMDQwNjM1XSwgWy02Ni42NjM4ODc0MDI5ODEzLCA0Ni4wMTQ2NDI0ODkzMjkxXSwgWy02Ni42NjA1NzI2MTk1ODI5LCA0Ni4wMDYwNTEzMTAyNTE1XSwgWy02Ni42NTk0Njc2OTE3ODM0LCA0Ni4wMDI0MjYwMTg4NDMyXSwgWy02Ni42NTk1MDM2MjQzOTQ4LCA0Ni4wMDEyMDI5NzUzODAzXSwgWy02Ni42NTg0MjU2NDYwNTM4LCA0Ni4wMDE5ODkyMjA3MTAxXSwgWy02Ni42NTY5ODgzNDE1OTkyLCA0Ni4wMDI0MTM1Mzg5NDQ0XSwgWy02Ni42NTU2MTM5MTkyMTQ1LCA0Ni4wMDI0Mzg0OTg3MzkyXSwgWy02Ni42NTQxNDk2NjUzMDE0LCA0Ni4wMDIwNTc4NjA2NDUxXSwgWy02Ni42NTQ4NjgzMTc1Mjg3LCA0Ni4wMDMwMjUwNTA2NzUxXSwgWy02Ni42NTUyNDU2MDk5NDgsIDQ2LjAwNDA3MzM0MDc3MzhdLCBbLTY2LjY1NTI2MzU3NjI1MzcsIDQ2LjAwNTE1OTA0ODg2NDNdLCBbLTY2LjY1NDkyMjIxNjQ0NTgsIDQ2LjAwNjIxOTc3NzU2OTZdLCBbLTY2LjY1Mzk1MjAzNTkzODksIDQ2LjAwNzQ5MjYyNTE2ODFdLCBbLTY2LjY1MjYwNDU2MzAxMjcsIDQ2LjAwODMwMzczODI2MDZdLCBbLTY2LjY1MDcxODEwMDkxNjEsIDQ2LjAwODgyMTU5NjU1MjVdLCBbLTY2LjY0ODY5Njg5MTUyNjgsIDQ2LjAwODg5NjQ2NzIyOTddLCBbLTY2LjY0OTYwNDE4OTk2MzgsIDQ2LjAxMDA4ODE0NTE5NzldLCBbLTY2LjY1MDA0NDM2NDQ1MywgNDYuMDExMjA0OTMwMDQwNV0sIFstNjYuNjQ5NTk1MjA2ODEwOSwgNDYuMDExODQ3NTM5MDMwN10sIFstNjYuNjQ4ODc2NTU0NTgzNiwgNDYuMDEyMzQ2NjQ3NjU3OF0sIFstNjYuNjQ4MTEyOTg2NTkyMSwgNDYuMDEyNjA4Njc3ODg0XSwgWy02Ni42NDc0NDgyMzMyODE5LCA0Ni4wMTI3MDg0OTg1OTZdLCBbLTY2LjY0NTYyNDY1MzI1NTEsIDQ2LjAxMjU4OTk2MTQ4MDRdLCBbLTY2LjY0MzA1NTQ3MTU0MjUsIDQ2LjAxMjE2NTcyMTMwMDldLCBbLTY2LjY0MDE4OTg0NTc4NjIsIDQ2LjAxMTM5MjA5ODQ3ODJdLCBbLTY2LjY0MDk5ODMyOTU0MTksIDQ2LjAxMjYzMzYzMzA3ODldLCBbLTY2LjY0MTIzMTg5MTUxNTgsIDQ2LjAxMzE5NTEyMTk4NjldLCBbLTY2LjY0MTE5NTk1ODkwNDQsIDQ2LjAxMzQ4ODM0MTcwNjRdLCBbLTY2LjY0MDkzNTQ0NzQ3MiwgNDYuMDE0MTk5NTQ5MDM1Nl0sIFstNjYuNjQwNTQ5MTcxODk5OCwgNDYuMDE0NzIzNTkwNjg4OF0sIFstNjYuNjM5NDA4MzExNDg5LCA0Ni4wMTU1ODQ1MDU0ODE0XSwgWy02Ni42MzgxNzc2MTk1NDk4LCA0Ni4wMTU5NTI1NzM2NTc5XSwgWy02Ni42MzUzODM4NTkwMTYyLCA0Ni4wMTYzMDE5MjQyMzcxXSwgWy02Ni42MzM3NzU4NzQ2NTc2LCA0Ni4wMTYzMzMxMTYxNDU4XSwgWy02Ni42MzAzNjIyNzY1Nzc5LCA0Ni4wMTYxNDU5NjQ0Mjk4XSwgWy02Ni42MzA2NzY2ODY5Mjc0LCA0Ni4wMTQzOTI5NDU5MzgxXSwgWy02Ni42MzA5NjQxNDc4MTgzLCA0Ni4wMDc0MjM5OTE5NzZdLCBbLTY2LjYzMzYwNTE5NDc1MzYsIDQ2LjAwODAyOTIwOTAwN10sIFstNjYuNjM1NzE2MjM1NjcxMywgNDYuMDA4NjkwNTcyNjIzNV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogMiwgIk5laWdoYm91cmgiOiAiQnJvb2tzaWRlIiwgIk9CSkVDVElEIjogMiwgIlNoYXBlX0FyZWEiOiAxMDQ0MzU4My42NTk4LCAiU2hhcGVfTGVuZyI6IDIyMDEwLjYzMTA2NjIsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlYjI0YyIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNzEwNTU0ODgxOTkxMywgNDUuOTc1Nzc1MDIxODMxMV0sIFstNjYuNzA1NTE1MzMzMjQ3NCwgNDUuOTc2MDEyMjUzNTcxMl0sIFstNjYuNzAxMzQ3MTUwMzI5MSwgNDUuOTc2ODMwMDcwOTg5N10sIFstNjYuNjk5ODgyODk2NDE1OSwgNDUuOTc2OTA0OTg0OTU4NV0sIFstNjYuNjk4OTkzNTY0Mjg0NywgNDUuOTc2NzE3Njk5ODQ2NF0sIFstNjYuNjk4NDQ1NTkxOTYxNCwgNDUuOTc5MTk2MDU0ODkxXSwgWy02Ni42OTgxNzYwOTczNzYxLCA0NS45ODI4MTY2MjYwNzY3XSwgWy02Ni42OTg2NzkxNTM5MzUyLCA0NS45ODY0MTgyMzUyNDU0XSwgWy02Ni43MDAyNTEyMDU2ODI0LCA0NS45ODkyNDU2Nzc1NTgxXSwgWy02Ni43MDIxMTA3MTgzMjA2LCA0NS45OTE5ODU1OTk3NDg5XSwgWy02Ni43MTkyNDE1OTA3ODg3LCA0NS45OTMyOTYyMjA3MTg0XSwgWy02Ni43MzMxODM0NDM5OTgzLCA0NS45NzY2NTUyNzEzMzQ5XSwgWy02Ni43MzI3NzkyMDIxMjA0LCA0NS45NzY1MjQxNzEyMzE4XSwgWy02Ni43MzExODkxODQwNjc1LCA0NS45NzYzNDkzNzA2MTE1XSwgWy02Ni43MzA2NTkxNzgwNDk5LCA0NS45NzY0NTU0OTk2MjU0XSwgWy02Ni43MjgxMTY5NDU3OTU4LCA0NS45NzY0NTU0OTk2MjU0XSwgWy02Ni43MjYzMjAzMTUyMjc2LCA0NS45NzYyNjE5NzAwOTQ0XSwgWy02Ni43MjI2MDEyODk5NTEzLCA0NS45NzYwNzQ2ODI4MDc2XSwgWy02Ni43MjAzMDE2MDI4MjQsIDQ1Ljk3NjI2MTk3MDA5NDRdLCBbLTY2LjcxNjgwNzE1NjM2ODgsIDQ1Ljk3NjMxMTkxMzI2MzldLCBbLTY2LjcxMDU1NDg4MTk5MTMsIDQ1Ljk3NTc3NTAyMTgzMTFdXSwgW1stNjYuNzIwMTEyOTU2NjE0MywgNDUuOTc3NzYwMjQ1NTg1OF0sIFstNjYuNzIxNDA2NTMwNjIzNCwgNDUuOTc3ODIyNjcyODUxNV0sIFstNjYuNzI0NDUxODE5NDM2NiwgNDUuOTc3OTc4NzQwNzA3OF0sIFstNjYuNzIwNTcxMDk3NDA5MiwgNDUuOTgyNzcyOTMwOTM5M10sIFstNjYuNzIwMDUwMDc0NTQ0NCwgNDUuOTgzMDc4Nzk2MTc2NF0sIFstNjYuNzE5NTM4MDM0ODMyNSwgNDUuOTgzMjIyMzY0OTkwNl0sIFstNjYuNzE4NDYwMDU2NDkxNSwgNDUuOTgzMTg0OTEyMjkyM10sIFstNjYuNzE3ODY3MTY4NDA0LCA0NS45ODI5NDc3MTEyODE3XSwgWy02Ni43MTczNjQxMTE4NDQ5LCA0NS45ODI0OTIwMzI4MDQ2XSwgWy02Ni43MTcxOTM0MzE5NDA5LCA0NS45ODIwMzAxMDgzMjg1XSwgWy02Ni43MTczMTAyMTI5Mjc5LCA0NS45ODE0NjgzMDMwOTYxXSwgWy02Ni43MjAxMTI5NTY2MTQzLCA0NS45Nzc3NjAyNDU1ODU4XV0sIFtbLTY2LjcwNDU3MjEwMjE5OSwgNDUuOTc4MzQwODE2NDQwNl0sIFstNjYuNzA1Mzk4NTUyMjYwNCwgNDUuOTc5OTUxNDAwNDkyOV0sIFstNjYuNzA1NjE0MTQ3OTI4NiwgNDUuOTgxMzYyMTgzNjg5OF0sIFstNjYuNzA1MjcyNzg4MTIwNywgNDUuOTgyMzIzNDkzMjM5Nl0sIFstNjYuNzA0Njg4ODgzMTg2LCA0NS45ODI2MTY4NzY1OTZdLCBbLTY2LjcwMzk3MDIzMDk1ODcsIDQ1Ljk4MjY4NTU0MDU2MTJdLCBbLTY2LjcwMzM5NTMwOTE3NjgsIDQ1Ljk4MjU1NDQ1NDczNTVdLCBbLTY2LjcwMTYyNTYyODA2NzEsIDQ1Ljk4MDU0NDQzMzIwNzNdLCBbLTY2LjcwMTI0ODMzNTY0NzgsIDQ1Ljk3OTY3NjczMDU1NzJdLCBbLTY2LjcwMTA5NTYyMjA0OTUsIDQ1Ljk3ODU5Njc2NTA5OTJdLCBbLTY2LjcwNDU3MjEwMjE5OSwgNDUuOTc4MzQwODE2NDQwNl1dLCBbWy02Ni43MTAxOTU1NTU4Nzc2LCA0NS45NzYyMjQ1MTI2ODc3XSwgWy02Ni43MTEwNDg5NTUzOTc2LCA0NS45NzYzMTE5MTMyNjM5XSwgWy02Ni43MTE2Nzc3NzYwOTY0LCA0NS45NzY0OTkxOTk3NDg0XSwgWy02Ni43MTIxMzU5MTY4OTEzLCA0NS45NzcwNTQ4MTI1OTIxXSwgWy02Ni43MTIxNDQ5MDAwNDQyLCA0NS45Nzc5MTAwNzA5MDUyXSwgWy02Ni43MTY3NzEyMjM3NTc0LCA0NS45Nzc2NDE2MzM1ODddLCBbLTY2LjcxNTg0NTk1OTAxNDcsIDQ1Ljk3ODk1ODgzNjc5MDddLCBbLTY2LjcxNDcwNTA5ODYwMzksIDQ1Ljk4MDE5NDg1Njc5NjldLCBbLTY2LjcxMzA4ODEzMTA5MjUsIDQ1Ljk4MTU0MzIxMDc4OThdLCBbLTY2LjcxMTczMTY3NTAxMzUsIDQ1Ljk4MjM2NzE4ODczMTZdLCBbLTY2LjcxMDcwNzU5NTU4OTYsIDQ1Ljk4MjYzNTYwMzE0MDRdLCBbLTY2LjcwOTgwOTI4MDMwNTUsIDQ1Ljk4MjY4NTU0MDU2MTJdLCBbLTY2LjcwODQ4ODc1NjgzNzgsIDQ1Ljk4MjA0MjU5MjgyNDVdLCBbLTY2LjcwNzUxODU3NjMzMSwgNDUuOTgxMTQ5OTQ0MjY3MV0sIFstNjYuNzA3MDk2MzY4MTQ3NCwgNDUuOTgwNDA3MDk5ODgwN10sIFstNjYuNzA3MTMyMzAwNzU4OCwgNDUuOTgwMjAxMDk5MjUyMV0sIFstNjYuNzA3NDY0Njc3NDEzOSwgNDUuOTc5MjE0NzgyNTkyNV0sIFstNjYuNzA4MTY1MzYzMzM1NSwgNDUuOTc4MTAzNTk0Njc2Ml0sIFstNjYuNzA3MzU2ODc5NTc5OCwgNDUuOTc4MTU5Nzc4ODcwMl0sIFstNjYuNzA3Mzc0ODQ1ODg1NSwgNDUuOTc4MDM0OTI1MDI4NV0sIFstNjYuNzA3ODY4OTE5MjkxOCwgNDUuOTc3MTE3MjQwNjUzMV0sIFstNjYuNzA4NzEzMzM1NjU4OCwgNDUuOTc2NTA1NDQyNjIwM10sIFstNjYuNzA5MzUxMTM5NTEwNiwgNDUuOTc2MzExOTEzMjYzOV0sIFstNjYuNzEwMTk1NTU1ODc3NiwgNDUuOTc2MjI0NTEyNjg3N11dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogMywgIk5laWdoYm91cmgiOiAiRG91Z2xhcyIsICJPQkpFQ1RJRCI6IDMsICJTaGFwZV9BcmVhIjogMzIzMTQ1Ni40MzM4NywgIlNoYXBlX0xlbmciOiAxMzYwNC44Mjk1OTAxLCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjY4MTM3NzYwMTU2MzEsIDQ2LjAxNzAwMDYxODc3NDddLCBbLTY2LjY4MDI4MTY1NjkxNjUsIDQ2LjAxNjE1MjIwMjgzMDZdLCBbLTY2LjY3OTA4Njg5NzU4ODYsIDQ2LjAxNDk5ODA4NjcxNTddLCBbLTY2LjY3ODEwNzczMzkyODksIDQ2LjAxMzc1MDM2NjUyMzRdLCBbLTY2LjY3NzM1MzE0OTA5MDIsIDQ2LjAxMjQyNzc1MjM4NDNdLCBbLTY2LjY3NzExOTU4NzExNjQsIDQ2LjAxMTg3ODczMzQ1MThdLCBbLTY2LjY3NjU2MjYzMTY0MDIsIDQ2LjAwOTA1MjQ0NzQ4MTddLCBbLTY2LjY3NTY0NjM1MDA1MDQsIDQ2LjAwNTU0NTkwNTIxODldLCBbLTY2LjY3NDczOTA1MTYxMzQsIDQ2LjAwMjc2Mjk3NTA0NjddLCBbLTY2LjY3MzM5MTU3ODY4NzMsIDQ1Ljk5OTMxODQzNzEyMTRdLCBbLTY2LjY3MTI5ODUwNDA3NTMsIDQ1Ljk5Njk0NzA3MjYxODldLCBbLTY2LjY2ODgxMDE3MDczODIsIDQ1Ljk5NDc2OTA3MjAwN10sIFstNjYuNjY2NDAyNjg1Nzc2OCwgNDUuOTkzMDc3Nzg2MDQ1NV0sIFstNjYuNjY1NjkzMDE2NzAyNCwgNDUuOTkzMjgzNzM4NzYwNF0sIFstNjYuNjYzMzM5NDMwNjU4LCA0NS45OTQyMDczOTYwNTQ4XSwgWy02Ni42NjEyNDYzNTYwNDYsIDQ1Ljk5NTM5MzE0OTcxMjRdLCBbLTY2LjY2MDQ1NTgzODU5NTksIDQ1Ljk5NzA5Njg0NjAxNTFdLCBbLTY2LjY1OTg4OTg5OTk2NjksIDQ1Ljk5ODg1MDQxMjcwMzNdLCBbLTY2LjY1OTU1NzUyMzMxMTgsIDQ2LjAwMDYyODg4NDQzMTFdLCBbLTY2LjY1OTQ2NzY5MTc4MzQsIDQ2LjAwMjQyNjAxODg0MzJdLCBbLTY2LjY2MDU3MjYxOTU4MjksIDQ2LjAwNjA1MTMxMDI1MTVdLCBbLTY2LjY2MzU1NTAyNjMyNjIsIDQ2LjAxMzgwNjUxNDUzNjldLCBbLTY2LjY2NjQ2NTU2Nzg0NjcsIDQ2LjAyMDQxOTEwNDA2MzVdLCBbLTY2LjY4MTUyMTMzMjAwODUsIDQ2LjAxOTc1MTY0MjcwMDldLCBbLTY2LjY4MTM3NzYwMTU2MzEsIDQ2LjAxNzAwMDYxODc3NDddXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDQsICJOZWlnaGJvdXJoIjogIk1jTGVvZCBIaWxsIiwgIk9CSkVDVElEIjogNCwgIlNoYXBlX0FyZWEiOiAzMTU4NjUyLjMxNDU4LCAiU2hhcGVfTGVuZyI6IDc3OTkuODkxMzQ1NiwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmVkOTc2IiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni42MDc2OTc3ODE5NTk2LCA0NS45NzU0NTAzODcyNzY3XSwgWy02Ni42MDUxMTA2MzM5NDEzLCA0NS45NzUwNDQ1OTE0MDc1XSwgWy02Ni42MDI5OTA2MDk4NzA4LCA0NS45NzQ0NzAyMjkwOTQ0XSwgWy02Ni42MDE5NDg1NjQxNDEyLCA0NS45NzQwNjQ0MjYwNDI4XSwgWy02Ni42MDE4Njc3MTU3NjU3LCA0NS45NzIxNjY0NzY5MTEyXSwgWy02Ni42MDE1NDQzMjIyNjM0LCA0NS45NzAyODA5NDk4ODQyXSwgWy02Ni42MDA4NTI2MTk0OTQ2LCA0NS45NjgwNTgxOTMyMDczXSwgWy02Ni42MDAzNDk1NjI5MzU1LCA0NS45NjcyMDkwMjY2NjA1XSwgWy02Ni41OTgwNjc4NDIxMTM4LCA0NS45NjQzODY3MDMxMzhdLCBbLTY2LjU5NTQ4MDY5NDA5NTYsIDQ1Ljk2MTY5NTM3MTMzOTRdLCBbLTY2LjU5MjU5NzEwMjAzMzYsIDQ1Ljk1OTE2MDAyOTY4NzVdLCBbLTY2LjU4OTQzNTAzMjIzMzUsIDQ1Ljk1Njc4Njk0NDcwNzhdLCBbLTY2LjU3NDQ5NjA0OTA1ODUsIDQ1Ljk3MzkxNDU5MDMxODNdLCBbLTY2LjU1MDM0OTMzNDIyMTQsIDQ2LjAwMjA1MTYyMDY1NDZdLCBbLTY2LjU4MjEwNDc3OTUxNSwgNDYuMDA5MDA4NzczMDU1NF0sIFstNjYuNTkyMjAxODQzMzA4NSwgNDYuMDEzMjU3NTA5MjkxNV0sIFstNjYuNTk0ODk2Nzg5MTYwOSwgNDYuMDEzODY4OTAxMTUxOF0sIFstNjYuNjE0MTM4NzAyNTQ2NywgNDUuOTkwOTkzMjUxNzk3Ml0sIFstNjYuNjExOTM3ODMwMTAwNiwgNDUuOTkwMjk0MjI4NzIyOV0sIFstNjYuNjA5NTc1MjYwOTAzNCwgNDUuOTg5MjE0NDcwMzczOF0sIFstNjYuNjA4OTI4NDczODk4OCwgNDUuOTg5NjEzOTIxMDA0XSwgWy02Ni42MDgzMDg2MzYzNTI4LCA0NS45ODk4MzIzNjkzNDgxXSwgWy02Ni42MDY4NzEzMzE4OTgyLCA0NS45ODk5Njk2NzkyOTQ1XSwgWy02Ni42MDUyMDk0NDg2MjI2LCA0NS45ODk3MzI1MDczNTQ5XSwgWy02Ni42MDM3OTAxMTA0NzM3LCA0NS45ODkxMDIxMjQzNjQ2XSwgWy02Ni42MDI3NzUwMTQyMDI2LCA0NS45ODgxNTk2NTcxOTY3XSwgWy02Ni42MDE3Njg5MDEwODQ0LCA0NS45ODYxMzczNTU2MDY0XSwgWy02Ni42MDEyNDc4NzgyMTk2LCA0NS45ODQzMjA5NjYyMDA2XSwgWy02Ni42MDEwOTUxNjQ2MjEzLCA0NS45ODI0NjcwNjQwMTI1XSwgWy02Ni41OTk5OTkyMTk5NzQ3LCA0NS45ODc4Mjg4NTM2NTc1XSwgWy02Ni41OTk4ODI0Mzg5ODc4LCA0NS45ODkxMTQ2MDcyNjU4XSwgWy02Ni41OTkzOTczNDg3MzQzLCA0NS45OTAzNTY2NDE4NTYzXSwgWy02Ni41OTg1Nzk4ODE4MjU4LCA0NS45OTE1MTEyNzIxMzAxXSwgWy02Ni41OTc2NTQ2MTcwODMxLCA0NS45OTIzNzI1NDgyMTY1XSwgWy02Ni41OTYzMDcxNDQxNTcsIDQ1Ljk5MzI1MjUzMzg1MjhdLCBbLTY2LjU5NTAxMzU3MDE0NzgsIDQ1Ljk5MzgzMjk0MjI1MjldLCBbLTY2LjU5MjM4MTUwNjM2NTQsIDQ1Ljk5NDQzODMwNzk2OTddLCBbLTY2LjU5MDY1Njc0MTAxOTksIDQ1Ljk5MzgzMjk0MjI1MjldLCBbLTY2LjU4OTA5MzY3MjQyNTUsIDQ1Ljk5MzA0MDM0MDAxNTFdLCBbLTY2LjU4Nzg2Mjk4MDQ4NjMsIDQ1Ljk5MTg3MzI1OTM2NDRdLCBbLTY2LjU4NjY1MDI1NDg1MjcsIDQ1Ljk5MDM0NDE1OTIzNTJdLCBbLTY2LjU4NTg3NzcwMzcwODMsIDQ1Ljk4ODk5NjAxOTU5MTFdLCBbLTY2LjU4NTkzMTYwMjYyNTQsIDQ1Ljk4ODI2NTc2MzU3MzVdLCBbLTY2LjU4NjMzNTg0NDUwMzIsIDQ1Ljk4NzU5MTY3MjU0NDddLCBbLTY2LjU4NzAzNjUzMDQyNDgsIDQ1Ljk4NzA0ODY0ODgwMTVdLCBbLTY2LjU4Nzk2MTc5NTE2NzUsIDQ1Ljk4NjY5OTExMzQ1OTJdLCBbLTY2LjU4OTQ4ODkzMTE1MDUsIDQ1Ljk4NjQ4Njg5NDQ5NTldLCBbLTY2LjU4OTc1ODQyNTczNTcsIDQ1Ljk4NjEzNzM1NTYwNjRdLCBbLTY2LjU5MDE4OTYxNzA3MjEsIDQ1Ljk4NTM4ODMzNjI2ODNdLCBbLTY2LjU5MDUwNDAyNzQyMTUsIDQ1Ljk4NDQxNDU5NTk3NzNdLCBbLTY2LjU5MDc4MjUwNTE1OTYsIDQ1Ljk4MDc1NjY3NDk1MTFdLCBbLTY2LjU5MTQwMjM0MjcwNTcsIDQ1Ljk4MDA4ODczNDk0OThdLCBbLTY2LjU5MjAyMjE4MDI1MTcsIDQ1Ljk3OTgyNjU1MDY5MTFdLCBbLTY2LjU5Mjg3NTU3OTc3MTYsIDQ1Ljk3OTcyNjY3MDY0NjldLCBbLTY2LjU5NTc2ODE1NDk4NjUsIDQ1Ljk4MDI0NDc5NjQxOTJdLCBbLTY2LjU5NzYyNzY2NzYyNDYsIDQ1Ljk4MDc4MTY0NDUxNDZdLCBbLTY2LjU5OTI4MDU2Nzc0NzQsIDQ1Ljk4MTQxMjEyMjI1OTNdLCBbLTY2LjYwMDM0OTU2MjkzNTUsIDQ1Ljk4MTk0MjcxNjc3NzldLCBbLTY2LjYwMTA5NTE2NDYyMTMsIDQ1Ljk4MjQ2NzA2NDAxMjVdLCBbLTY2LjYwMTM5MTYwODY2NTEsIDQ1Ljk3OTMzMzM5MTIyMTRdLCBbLTY2LjYwMzMwNTAyMDIyMDMsIDQ1Ljk3OTQ0NTc1NzA1NjZdLCBbLTY2LjYwNDY3OTQ0MjYwNDksIDQ1Ljk3OTc3MDM2ODE4ODRdLCBbLTY2LjYwNDg3NzA3MTk2NzUsIDQ1Ljk3ODU4NDI3OTgyNjJdLCBbLTY2LjYwNTQyNTA0NDI5MDgsIDQ1Ljk3NzQ2MDU5MzczMDZdLCBbLTY2LjYwNjMwNTM5MzI2OTIsIDQ1Ljk3NjQ0MzAxMzg2OTZdLCBbLTY2LjYwNzY5Nzc4MTk1OTYsIDQ1Ljk3NTQ1MDM4NzI3NjddXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDUsICJOZWlnaGJvdXJoIjogIk1hcnlzdmlsbGUiLCAiT0JKRUNUSUQiOiA1LCAiU2hhcGVfQXJlYSI6IDE0MTE5NDQwLjQyMDEsICJTaGFwZV9MZW5nIjogMjI1NTAuNTEwODMyMSwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmVkOTc2IiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni42MzQ5MDc3NTE5MTU2LCA0NS45NjkwMTk3MzM3MjgxXSwgWy02Ni42MzQ1MDM1MTAwMzc3LCA0NS45NjkwNjk2ODM0MjldLCBbLTY2LjYzMzQ3OTQzMDYxMzgsIDQ1Ljk2ODQ4Mjc3MTU5OTFdLCBbLTY2LjYyOTU2Mjc3NTk3NTEsIDQ1Ljk3MjcyMjEzMzIyNjJdLCBbLTY2LjYyOTMxMTI0NzY5NTUsIDQ1Ljk3NDIyMDUwNDQ5MTVdLCBbLTY2LjYyMTc5MjM0ODc2NzQsIDQ1Ljk4MTg5Mjc3ODY4N10sIFstNjYuNTk0ODk2Nzg5MTYwOSwgNDYuMDEzODY4OTAxMTUxOF0sIFstNjYuNTk5NjAzOTYxMjQ5NywgNDYuMDE0OTkxODQ4MTg0OF0sIFstNjYuNjMwMzgwMjQyODgzNiwgNDUuOTc3MTQyMjExODU3OF0sIFstNjYuNjM0MDYzMzM1NTQ4NSwgNDUuOTcyNzk3MDUyNzUyMl0sIFstNjYuNjMzODkyNjU1NjQ0NSwgNDUuOTcxOTQxNzE1NDY5OF0sIFstNjYuNjMyMzM4NTcwMjAzLCA0NS45NzE1NDIxMzczMjJdLCBbLTY2LjYzMzM4OTU5OTA4NTQsIDQ1Ljk3MDI0MzQ4ODQzMl0sIFstNjYuNjM0OTA3NzUxOTE1NiwgNDUuOTY5MDE5NzMzNzI4MV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogNiwgIk5laWdoYm91cmgiOiAiU2FpbnQgTWFyeSdzIEZpcnN0IE5hdGlvbiIsICJPQkpFQ1RJRCI6IDYsICJTaGFwZV9BcmVhIjogMTg1MTQzNS4xNzI0OCwgIlNoYXBlX0xlbmciOiAxMjM2Ny42MTg2MjE0LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjYwMDExNjAwMDk2MTYsIDQ1Ljk4NzQxNjkwNjg2MzhdLCBbLTY2LjU5NzEwNjY0NDc1OTgsIDQ1Ljk4NjgwNTIyMjYzNTddLCBbLTY2LjU5MzY5MzA0NjY4MDIsIDQ1Ljk4NjQzNjk2MDUwNF0sIFstNjYuNTkxMjc2NTc4NTY1OSwgNDUuOTg2MzgwNzg0NzA5Ml0sIFstNjYuNTg5MjY0MzUyMzI5NSwgNDUuOTg2NTExODYxNDc1XSwgWy02Ni41ODc3OTExMTUyNjM1LCA0NS45ODY3NDI4MDU0OTc2XSwgWy02Ni41ODY2NTAyNTQ4NTI3LCA0NS45ODcyOTgzMTU1NTE5XSwgWy02Ni41ODU5NzY1MTgzODk2LCA0NS45ODgxNDcxNzQwODAyXSwgWy02Ni41ODU4Nzc3MDM3MDgzLCA0NS45ODg5OTYwMTk1OTExXSwgWy02Ni41ODcyMTYxOTM0ODE3LCA0NS45OTExMjQzMTc2NDA4XSwgWy02Ni41ODkwOTM2NzI0MjU1LCA0NS45OTMwNDAzNDAwMTUxXSwgWy02Ni41OTA2NTY3NDEwMTk5LCA0NS45OTM4MzI5NDIyNTI5XSwgWy02Ni41OTIzODE1MDYzNjU0LCA0NS45OTQ0MzgzMDc5Njk3XSwgWy02Ni41OTUwMTM1NzAxNDc4LCA0NS45OTM4MzI5NDIyNTI5XSwgWy02Ni41OTU1NDM1NzYxNjU1LCA0NS45OTM2MjA3NTA2NDA1XSwgWy02Ni41OTY3ODMyNTEyNTc1LCA0NS45OTI5ODQxNzA5MjE4XSwgWy02Ni41OTgwNDk4NzU4MDgyLCA0NS45OTIwNDE3Njk4NTU2XSwgWy02Ni41OTg4ODUzMDkwMjI0LCA0NS45OTExNDMwNDEzMDc0XSwgWy02Ni41OTk1OTQ5NzgwOTY4LCA0NS45ODk5NTA5NTUyMzFdLCBbLTY2LjU5OTkyNzM1NDc1MiwgNDUuOTg4OTAyMzk3NTYzMV0sIFstNjYuNjAwMTE2MDAwOTYxNiwgNDUuOTg3NDE2OTA2ODYzOF1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogNywgIk5laWdoYm91cmgiOiAiU2FuZHl2aWxsZSIsICJPQkpFQ1RJRCI6IDcsICJTaGFwZV9BcmVhIjogNzI4ODU5LjQ4MTAwMSwgIlNoYXBlX0xlbmciOiAzMTc1LjQyMDA2NDU0LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjU4OTQ4ODkzMTE1MDUsIDQ1Ljk4NjQ4Njg5NDQ5NTldLCBbLTY2LjU5MTU3MzAyMjYwOTcsIDQ1Ljk4NjM3NDU0Mjk1MDddLCBbLTY2LjU5NDA2MTM1NTk0NjcsIDQ1Ljk4NjQ2ODE2OTI1NDJdLCBbLTY2LjU5NzUzNzgzNjA5NjIsIDQ1Ljk4Njg3Mzg4MTQwNjJdLCBbLTY2LjYwMDExNjAwMDk2MTYsIDQ1Ljk4NzQxNjkwNjg2MzhdLCBbLTY2LjYwMTA5NTE2NDYyMTMsIDQ1Ljk4MjQ2NzA2NDAxMjVdLCBbLTY2LjU5OTUwNTE0NjU2ODQsIDQ1Ljk4MTUwNTc1Njk1NTZdLCBbLTY2LjU5NjUyMjczOTgyNTEsIDQ1Ljk4MDQ0NDU1NDQ1ODFdLCBbLTY2LjU5MzE2MzA0MDY2MjUsIDQ1Ljk3OTc1MTY0MDY3NDhdLCBbLTY2LjU5MjQ0NDM4ODQzNTMsIDQ1Ljk3OTc0NTM5ODE2ODldLCBbLTY2LjU5MTg4NzQzMjk1OTEsIDQ1Ljk3OTg2NDAwNTY2MTJdLCBbLTY2LjU5MTIwNDcxMzM0MzIsIDQ1Ljk4MDIyNjA2OTA2NjFdLCBbLTY2LjU5MDc4MjUwNTE1OTYsIDQ1Ljk4MDc1NjY3NDk1MTFdLCBbLTY2LjU5MDQ2ODA5NDgxMDIsIDQ1Ljk4NDYxNDMzODk3MThdLCBbLTY2LjU5MDA5OTc4NTU0MzcsIDQ1Ljk4NTU4MTgzMzkwMTVdLCBbLTY2LjU4OTQ4ODkzMTE1MDUsIDQ1Ljk4NjQ4Njg5NDQ5NTldXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDgsICJOZWlnaGJvdXJoIjogIktub2IgSGlsbCIsICJPQkpFQ1RJRCI6IDgsICJTaGFwZV9BcmVhIjogNTQ1MDIzLjE0NTc1MywgIlNoYXBlX0xlbmciOiAyOTc1LjkzNjQ4NDUzLCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjYwMTk0ODU2NDE0MTIsIDQ1Ljk3NDA2NDQyNjA0MjhdLCBbLTY2LjYwMzIwNjIwNTUzOSwgNDUuOTc0NTMyNjYwMDY5Ml0sIFstNjYuNjA2MTE2NzQ3MDU5NSwgNDUuOTc1MjUwNjExMjIwNF0sIFstNjYuNjA3Nzg3NjEzNDg4LCA0NS45NzU0NjI4NzMyNTYzXSwgWy02Ni42MTEwMDM1ODIyMDUyLCA0NS45NzU1ODc3MzI4OTc0XSwgWy02Ni42MTE5NzM3NjI3MTIsIDQ1Ljk3NTM5NDIwMDMzMzhdLCBbLTY2LjYxMjkwODAxMDYwNzUsIDQ1Ljk3NDg4MjI3MjIyNzNdLCBbLTY2LjYxMzQxMTA2NzE2NjYsIDQ1Ljk3NDI3MDQ0OTUwMjJdLCBbLTY2LjYxMzU3Mjc2MzkxNzcsIDQ1Ljk3MzQ1MjU5NDI4MjNdLCBbLTY2LjYxMzMyMTIzNTYzODIsIDQ1Ljk3Mjc3MjA3OTU4ODFdLCBbLTY2LjYxMjYyOTUzMjg2OTQsIDQ1Ljk3MjEwNDA0MzI2OV0sIFstNjYuNjA2MTk3NTk1NDM1MSwgNDUuOTY4NzQ1MDA5NTY4M10sIFstNjYuNjA0NjE2NTYwNTM1MSwgNDUuOTY1NDEwNzQ4NjQ4XSwgWy02Ni42MDM4Nzk5NDIwMDIxLCA0NS45NjQ4ODYyMzk4OTc5XSwgWy02Ni42MDI1OTUzNTExNDU4LCA0NS45NjQyNDMwODU0ODU5XSwgWy02Ni42MDA4ODg1NTIxMDYsIDQ1Ljk2Mzc2ODUyMDE2MTVdLCBbLTY2LjU5OTMxNjUwMDM1ODgsIDQ1Ljk2MzYxMjQxMjI1ODNdLCBbLTY2LjU5NzQ4MzkzNzE3OTIsIDQ1Ljk2MzczNzI5ODYxNl0sIFstNjYuNjAwNjk5OTA1ODk2MywgNDUuOTY3Njg5ODA2Mzc3Nl0sIFstNjYuNjAxMzU1Njc2MDUzNywgNDUuOTY5NTMxNzE2MDI2NV0sIFstNjYuNjAxNzA2MDE5MDE0NSwgNDUuOTcxMDMwMTczNjA3XSwgWy02Ni42MDE5NDg1NjQxNDEyLCA0NS45NzQwNjQ0MjYwNDI4XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiA5LCAiTmVpZ2hib3VyaCI6ICJZb3VuZ3MgQ3Jvc3NpbmciLCAiT0JKRUNUSUQiOiA5LCAiU2hhcGVfQXJlYSI6IDc0ODQ5MC4wODMxMjUsICJTaGFwZV9MZW5nIjogNDA5Ni4yMzk3MjIzMiwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmVkOTc2IiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni42MjM3Nzc2MjU1NDUzLCA0NS45NTU0MzE3NDI2OTU1XSwgWy02Ni42MjMzNzMzODM2Njc1LCA0NS45NTQzOTUwMjIwMDgxXSwgWy02Ni42MjM1Nzk5OTYxODI4LCA0NS45NTMwNTg0OTgwNDY3XSwgWy02Ni42MjM4MjI1NDEzMDk1LCA0NS45NTI1NzEzNDU3ODM5XSwgWy02Ni42MjM5OTMyMjEyMTM1LCA0NS45NTA0MDQwOTA4NzAzXSwgWy02Ni42MjM5MTIzNzI4MzgsIDQ1Ljk0OTM2NzI3NjEzMDhdLCBbLTY2LjYyMjgzNDM5NDQ5NywgNDUuOTQzOTI2ODAzODI1NF0sIFstNjYuNjIyNTExMDAwOTk0NywgNDUuOTQzNTU4MjU2NTQxXSwgWy02Ni42MjI1NDY5MzM2MDYxLCA0NS45NDMwNzEwMjA3Nzc0XSwgWy02Ni42MjIxNzg2MjQzMzk2LCA0NS45NDI3MDI0Njc4MDM5XSwgWy02Ni42MjIxNTE2NzQ4ODExLCA0NS45NDIyMTUyMjQ1MTkyXSwgWy02Ni42MjE1NzY3NTMwOTkyLCA0NS45NDIwMzQwNjg4NzI2XSwgWy02Ni42MjA4ODUwNTAzMzA1LCA0NS45NDExMzQ1Mjg2MTldLCBbLTY2LjYxNjgzMzY0ODM5OTEsIDQ1LjkzNzE2MTM4NDU4NjZdLCBbLTY2LjYxNDA0ODg3MTAxODMsIDQ1LjkzNTE0MzQ2ODE1MjFdLCBbLTY2LjYxMDIyMjA0NzkwOCwgNDUuOTMyOTI1NTQ5NTk2NF0sIFstNjYuNjA4NDM0NDAwNDkyNiwgNDUuOTMyMzE5NTExMzUwMl0sIFstNjYuNjA2NzAwNjUxOTk0MiwgNDUuOTMxMzY5ODI5ODUxMV0sIFstNjYuNjA1ODc0MjAxOTMyOCwgNDUuOTMxMTA3NDE0OTkwNF0sIFstNjYuNjAzNjI4NDEzNzIyNSwgNDUuOTMwMTEzOTc2MDU2N10sIFstNjYuNjAwMTk2ODQ5MzM3MiwgNDUuOTI4OTA4MDc5NzMyXSwgWy02Ni41OTczODUxMjI0OTc5LCA0NS45MjcyNzcyNjYzMTc4XSwgWy02Ni41OTY5MTc5OTg1NTAyLCA0NS45MjY4OTYxMTE0NDI2XSwgWy02Ni41OTU5NTY4MDExOTYyLCA0NS45MjU3Mjc2MzY3MzRdLCBbLTY2LjU5MjY2ODk2NzI1NjMsIDQ1LjkyODQwODIxODY0NzNdLCBbLTY2LjYwNTExMDYzMzk0MTMsIDQ1LjkzODY3OTQ1OTA3NDhdLCBbLTY2LjU4OTQzNTAzMjIzMzUsIDQ1Ljk1Njc4Njk0NDcwNzhdLCBbLTY2LjU5Mjk4MzM3NzYwNTcsIDQ1Ljk1OTQ3MjI3MDE0NV0sIFstNjYuNTk1NzQxMjA1NTI4LCA0NS45NjE5NDUxNTI0MTYyXSwgWy02Ni41OTY5OTg4NDY5MjU3LCA0NS45NjE3MTQxMDQ5NTkyXSwgWy02Ni42MDI2NzYxOTk1MjE0LCA0NS45NjEwMzM0NDYwMzk3XSwgWy02Ni42MDQ0OTA3OTYzOTUzLCA0NS45NjEwODM0MDI5NDJdLCBbLTY2LjYwNjg5ODI4MTM1NjcsIDQ1Ljk2MTUyMDUyMzkxNTZdLCBbLTY2LjYwNzg1OTQ3ODcxMDcsIDQ1Ljk2MTU2NDIzNTgyMzNdLCBbLTY2LjYwODc5MzcyNjYwNjIsIDQ1Ljk2MTQwMTg3NzEzNTJdLCBbLTY2LjYwOTg5ODY1NDQwNTcsIDQ1Ljk2MDg1ODU5NjUyN10sIFstNjYuNjEwNTgxMzc0MDIxNiwgNDUuOTYwMjA5MTUwNjQ4N10sIFstNjYuNjEwOTk0NTk5MDUyMywgNDUuOTU5NDUzNTM1NzY3Ml0sIFstNjYuNjExMDg0NDMwNTgwNywgNDUuOTU4NTIzMDUzNjk4XSwgWy02Ni42MTA3NzAwMjAyMzEzLCA0NS45NTc2MzAwMjYwMTExXSwgWy02Ni42MTAzMDI4OTYyODM1LCA0NS45NTcwMjQyNTc3NzkyXSwgWy02Ni42MDkzNjg2NDgzODgxLCA0NS45NTYyOTM1ODAwNjk4XSwgWy02Ni42MDk0MjI1NDczMDUxLCA0NS45NTU5Mzc2MDUzODc4XSwgWy02Ni42MDk3ODE4NzM0MTg4LCA0NS45NTU2ODc3OTcyMjhdLCBbLTY2LjYxMDE5NTA5ODQ0OTUsIDQ1Ljk1NTYzMTU5MDIzNjhdLCBbLTY2LjYxMDUyNzQ3NTEwNDYsIDQ1Ljk1NTcxMjc3ODA5NDZdLCBbLTY2LjYxMTgwMzA4MjgwOCwgNDUuOTU2NjU1Nzk3NTc0NF0sIFstNjYuNjEzMDMzNzc0NzQ3MywgNDUuOTU3MTg2NjI5Mjk1MV0sIFstNjYuNjE0NDYyMDk2MDQ5LCA0NS45NTc1NTUwODU5NzAyXSwgWy02Ni42MTU3MTk3Mzc0NDY4LCA0NS45NTc2NDI1MTYwMDhdLCBbLTY2LjYxNjk1OTQxMjUzODksIDQ1Ljk1NzQ5ODg4MDg3M10sIFstNjYuNjE4NjMwMjc4OTY3MywgNDUuOTU3MDQ5MjM4MDQzNF0sIFstNjYuNjIzNzc3NjI1NTQ1MywgNDUuOTU1NDMxNzQyNjk1NV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogMTAsICJOZWlnaGJvdXJoIjogIkJhcmtlcnMgUG9pbnQiLCAiT0JKRUNUSUQiOiAxMCwgIlNoYXBlX0FyZWEiOiA1Nzc5MDIxLjk2ODQsICJTaGFwZV9MZW5nIjogMTIzMTkuMjM5MDQ5NCwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmViMjRjIiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni42Mjg2NzM0NDM4NDM4LCA0NS45NjQ4MzAwNDIyMzczXSwgWy02Ni42Mjc3MzAyMTI3OTU1LCA0NS45NjM1Njg3MDE5NjY2XSwgWy02Ni42Mjc2MjI0MTQ5NjE0LCA0NS45NjMyMDY1Mjk2NTE0XSwgWy02Ni42MjcxMTAzNzUyNDk0LCA0NS45NjI2OTQ0ODg4OV0sIFstNjYuNjI2NzQyMDY1OTgyOSwgNDUuOTYxNzE0MTA0OTU5Ml0sIFstNjYuNjI2NzE1MTE2NTI0NCwgNDUuOTYwNzUyNDM3NjI1XSwgWy02Ni42MjU1MDIzOTA4OTA4LCA0NS45NTk2MDk2NTUzODg5XSwgWy02Ni42MjU0MTI1NTkzNjI0LCA0NS45NTg3NzkwOTM5NDY1XSwgWy02Ni42MjUxMDcxMzIxNjU4LCA0NS45NTc5OTIyMzQ3Nzk4XSwgWy02Ni42MjUzMTM3NDQ2ODEyLCA0NS45NTc3NTQ5MjU4NTM5XSwgWy02Ni42MjUyODY3OTUyMjI3LCA0NS45NTc1NzM4MjA5ODk5XSwgWy02Ni42MjQ4ODI1NTMzNDQ4LCA0NS45NTc1MDUxMjU4ODY2XSwgWy02Ni42MjQ3MDI4OTAyODgsIDQ1Ljk1NzI5Mjc5NTAyOV0sIFstNjYuNjI1MDA4MzE3NDg0NiwgNDUuOTU2NzMwNzM4ODMxNV0sIFstNjYuNjI1MDA4MzE3NDg0NiwgNDUuOTU2MzgxMDEyMDk4XSwgWy02Ni42MjQyOTg2NDg0MTAxLCA0NS45NTYxODc0MTI0MjE1XSwgWy02Ni42MjM3Nzc2MjU1NDUzLCA0NS45NTU0MzE3NDI2OTU1XSwgWy02Ni42MTg2MzAyNzg5NjczLCA0NS45NTcwNDkyMzgwNDM0XSwgWy02Ni42MTY5NTk0MTI1Mzg5LCA0NS45NTc0OTg4ODA4NzNdLCBbLTY2LjYxNTcxOTczNzQ0NjgsIDQ1Ljk1NzY0MjUxNjAwOF0sIFstNjYuNjE0MjY0NDY2Njg2NSwgNDUuOTU3NTE3NjE1OTExN10sIFstNjYuNjEyODA5MTk1OTI2MiwgNDUuOTU3MTExNjg4NjU0Nl0sIFstNjYuNjExNjIzNDE5NzUxMiwgNDUuOTU2NTQ5NjMwNjIwMV0sIFstNjYuNjEwNTk5MzQwMzI3MywgNDUuOTU1NzQ0MDA0MTYyMV0sIFstNjYuNjEwMjg0OTI5OTc3OSwgNDUuOTU1NjQ0MDgwNjg0Ml0sIFstNjYuNjA5ODYyNzIxNzk0MywgNDUuOTU1NjYyODE2MzUwMV0sIFstNjYuNjA5NDIyNTQ3MzA1MSwgNDUuOTU1OTM3NjA1Mzg3OF0sIFstNjYuNjA5MzY4NjQ4Mzg4MSwgNDUuOTU2MjkzNTgwMDY5OF0sIFstNjYuNjEwNjQ0MjU2MDkxNSwgNDUuOTU3NDE3Njk1NjMyXSwgWy02Ni42MTEwMzA1MzE2NjM3LCA0NS45NTgyNTQ1MjI0MTAzXSwgWy02Ni42MTEwODQ0MzA1ODA3LCA0NS45NTkwNTM4Njc1MzExXSwgWy02Ni42MTA4ODY4MDEyMTgyLCA0NS45NTk3MDk1NzE3MTZdLCBbLTY2LjYxMDQ5MTU0MjQ5MzIsIDQ1Ljk2MDMyNzc5OTk4MzJdLCBbLTY2LjYwOTg5ODY1NDQwNTcsIDQ1Ljk2MDg1ODU5NjUyN10sIFstNjYuNjA5Mjk2NzgzMTY1MywgNDUuOTYxMjAyMDUwNDA0NF0sIFstNjYuNjA4NDM0NDAwNDkyNiwgNDUuOTYxNTA4MDM0NzkyOF0sIFstNjYuNjA3NDczMjAzMTM4NiwgNDUuOTYxNTY0MjM1ODIzM10sIFstNjYuNjA0NDkwNzk2Mzk1MywgNDUuOTYxMDgzNDAyOTQyXSwgWy02Ni42MDIzNzA3NzIzMjQ4LCA0NS45NjEwNDU5MzUyNjk1XSwgWy02Ni41OTU3NDEyMDU1MjgsIDQ1Ljk2MTk0NTE1MjQxNjJdLCBbLTY2LjU5NzQ4MzkzNzE3OTIsIDQ1Ljk2MzczNzI5ODYxNl0sIFstNjYuNTk5MzE2NTAwMzU4OCwgNDUuOTYzNjEyNDEyMjU4M10sIFstNjYuNjAxMTQwMDgwMzg1NSwgNDUuOTYzODEyMjMwMjk1NV0sIFstNjYuNjAyODE5OTI5OTY2OCwgNDUuOTY0MzM2NzQ5MjE0M10sIFstNjYuNjA0MDc3NTcxMzY0NiwgNDUuOTY1MDExMTIzMzg0MV0sIFstNjYuNjA0NjE2NTYwNTM1MSwgNDUuOTY1NDEwNzQ4NjQ4XSwgWy02Ni42MDYxOTc1OTU0MzUxLCA0NS45Njg3NDUwMDk1NjgzXSwgWy02Ni42MTI3NTUyOTcwMDkyLCA0NS45NzIxOTE0NTAzNDgzXSwgWy02Ni42MTM0NTU5ODI5MzA4LCA0NS45NzMwMDkzMjQxOTI0XSwgWy02Ni42MTM1MzY4MzEzMDY0LCA0NS45NzM5NTgyOTI0NDY1XSwgWy02Ni42MTYwMTYxODE0OTA1LCA0NS45NzMzMDI3NTY5MDI0XSwgWy02Ni42MTgyMDgwNzA3ODM4LCA0NS45NzIyNjAxMjcyNDI1XSwgWy02Ni42MjI3ODk0Nzg3MzI4LCA0NS45Njg3NzYyMjgyOTE0XSwgWy02Ni42MjU4NjE3MTcwMDQ1LCA0NS45NjYxNTM3OTQyMDk1XSwgWy02Ni42MjY3OTU5NjQ5LCA0NS45NjU2MTA1NjAxOTg4XSwgWy02Ni42Mjg2NzM0NDM4NDM4LCA0NS45NjQ4MzAwNDIyMzczXV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiAxMSwgIk5laWdoYm91cmgiOiAiU291dGggRGV2b24iLCAiT0JKRUNUSUQiOiAxMSwgIlNoYXBlX0FyZWEiOiAyNTI1MjkzLjc1MTM1LCAiU2hhcGVfTGVuZyI6IDc4ODQuOTY2NzA3NDMsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlYjI0YyIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjAxMDk1MTY0NjIxMywgNDUuOTgyNDY3MDY0MDEyNV0sIFstNjYuNjAxMjQ3ODc4MjE5NiwgNDUuOTg0MzIwOTY2MjAwNl0sIFstNjYuNjAxNjYxMTAzMjUwMywgNDUuOTg1ODM3NzQ5MDg3M10sIFstNjYuNjAyNjA0MzM0Mjk4NiwgNDUuOTg3ODg1MDI3OTgyOF0sIFstNjYuNjAzMzQ5OTM1OTg0NSwgNDUuOTg4Nzc3NTY3OTQ2Ml0sIFstNjYuNjA0NjQzNTA5OTkzNiwgNDUuOTg5NTM5MDI0MjMwNF0sIFstNjYuNjA2MDI2OTE1NTMxMSwgNDUuOTg5OTAxMDI0MzYzOV0sIFstNjYuNjA3ODIzNTQ2MDk5NCwgNDUuOTg5OTI1OTg5ODAzXSwgWy02Ni42MDkwOTkxNTM4MDI4LCA0NS45ODk1MjY1NDE0MjVdLCBbLTY2LjYwOTgxNzgwNjAzMDEsIDQ1Ljk4ODk4OTc3ODEyNzVdLCBbLTY2LjYxMDIyMjA0NzkwOCwgNDUuOTg4MzA5NDU0Mzc1NF0sIFstNjYuNjEwMTc3MTMyMTQzOCwgNDUuOTg1OTUwMTAxNzIyXSwgWy02Ni42MTAwMTU0MzUzOTI2LCA0NS45ODQ5NDUxNjE3MjExXSwgWy02Ni42MDk1OTMyMjcyMDkxLCA0NS45ODM3MDkyNDc3NjIyXSwgWy02Ni42MDkwOTAxNzA2NSwgNDUuOTgyNzYwNDQ2NjA4MV0sIFstNjYuNjA4NDE2NDM0MTg2OSwgNDUuOTgxODk5MDIwOTUwOV0sIFstNjYuNjA2ODk4MjgxMzU2NywgNDUuOTgwNzgxNjQ0NTE0Nl0sIFstNjYuNjA0Nzk2MjIzNTkxOSwgNDUuOTc5ODA3ODIzMTk2NV0sIFstNjYuNjAzNjEwNDQ3NDE2OSwgNDUuOTc5NDgzMjEyMjg0M10sIFstNjYuNjAxMzkxNjA4NjY1MSwgNDUuOTc5MzMzMzkxMjIxNF0sIFstNjYuNjAxMDk1MTY0NjIxMywgNDUuOTgyNDY3MDY0MDEyNV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogMTIsICJOZWlnaGJvdXJoIjogIkNvdHRvbiBNaWxsIENyZWVrIiwgIk9CSkVDVElEIjogMTIsICJTaGFwZV9BcmVhIjogNjM5ODc5LjA5NDAxOCwgIlNoYXBlX0xlbmciOiAzMTIwLjc4MzIwMjI3LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjY2Mzk3NzIzNDUwOTcsIDQ1Ljk4NDQ4OTQ5OTY4NDddLCBbLTY2LjY2NDU2MTEzOTQ0NDQsIDQ1Ljk4NDI2NDc4ODI1ODVdLCBbLTY2LjY2NTI0Mzg1OTA2MDMsIDQ1Ljk4NDczOTE3Nzk3NzRdLCBbLTY2LjY2NTU2NzI1MjU2MjYsIDQ1Ljk4NTI2MzQ5ODcyNjZdLCBbLTY2LjY2NTkzNTU2MTgyOTEsIDQ1Ljk4NTQzODI3MTIwNjFdLCBbLTY2LjY2NjUzNzQzMzA2OTQsIDQ1Ljk4NTQxOTU0NTYwOTddLCBbLTY2LjY2NzQ5ODYzMDQyMzQsIDQ1Ljk4NTA4MjQ4Mzc5MTFdLCBbLTY2LjY2ODA5MTUxODUxMDksIDQ1Ljk4NTIwNzMyMTc0MV0sIFstNjYuNjY5MDQzNzMyNzEyMSwgNDUuOTg2MzgwNzg0NzA5Ml0sIFstNjYuNjY5NTM3ODA2MTE4NCwgNDUuOTg2NjQyOTM3OTMwNF0sIFstNjYuNjcxNTE0MDk5NzQzNCwgNDUuOTg2MjU1OTQ5NDA1Nl0sIFstNjYuNjcyODcwNTU1ODIyNSwgNDUuOTg1ODMxNTA3MjY3Nl0sIFstNjYuNjczMzQ2NjYyOTIzMSwgNDUuOTg2MDY4Njk1OTIyNF0sIFstNjYuNjczNzU5ODg3OTUzOCwgNDUuOTg2NTg2NzYyMzQ0N10sIFstNjYuNjczNzE0OTcyMTg5NSwgNDUuOTg2Nzk4OTgwOTI1XSwgWy02Ni42NzMyMDI5MzI0Nzc2LCA0NS45ODcyMDQ2OTA2NTI1XSwgWy02Ni42NzMwNjgxODUxODUsIDQ1Ljk4NzUyMzAxNDY2NDRdLCBbLTY2LjY3MzcwNTk4OTAzNjcsIDQ1Ljk4Nzk0MTIwMjI1MV0sIFstNjYuNjczODQwNzM2MzI5MywgNDUuOTg4NjcxNDYyNTUwNV0sIFstNjYuNjczNzY4ODcxMTA2NiwgNDUuOTg5MjUxOTE4OTkyOF0sIFstNjYuNjczNTQ0MjkyMjg1NiwgNDUuOTg5ODE5ODg2NjA4OF0sIFstNjYuNjcyODE2NjU2OTA1NCwgNDUuOTkwNTMxMzk4MjU1NV0sIFstNjYuNjcxNTA1MTE2NTkwNiwgNDUuOTkxNDczODI1MDM5N10sIFstNjYuNjY5OTY4OTk3NDU0OCwgNDUuOTkyMjI5MDAzMTMyOV0sIFstNjYuNjY4MjYyMTk4NDE0OSwgNDUuOTkyNzc4MjE3MDkyMl0sIFstNjYuNjY2NDM4NjE4Mzg4MiwgNDUuOTkzMDk2NTA5MDUxM10sIFstNjYuNjY5Mzk0MDc1NjcyOSwgNDUuOTkyODU5MzUwNTEwNV0sIFstNjYuNjczMTEzMTAwOTQ5MiwgNDUuOTkyNzE1ODA2Njg5NV0sIFstNjYuNjc5OTY3MjQ2NTY3LCA0NS45OTI2NzIxMTkzNjU3XSwgWy02Ni42ODMwOTMzODM3NTU4LCA0NS45OTI4NTkzNTA1MTA1XSwgWy02Ni42ODYxNjU2MjIwMjc0LCA0NS45OTMyOTYyMjA3MTg0XSwgWy02Ni42ODg2NTM5NTUzNjQ0LCA0NS45OTM4NzAzODc3NDcxXSwgWy02Ni42OTA4MDA5Mjg4OTM1LCA0NS45OTQ3MTkxNDU0ODY2XSwgWy02Ni42OTI0MTc4OTY0MDQ5LCA0NS45OTU2NjE1MDA5NjE5XSwgWy02Ni42OTYwMTExNTc1NDE0LCA0NS45OTE1Mjk5OTU2NjU4XSwgWy02Ni43MDIxMTA3MTgzMjA2LCA0NS45OTE5ODU1OTk3NDg5XSwgWy02Ni42OTk2OTQyNTAyMDYzLCA0NS45ODgzMTU2OTU5MTU4XSwgWy02Ni42OTg2NzkxNTM5MzUyLCA0NS45ODY0MTgyMzUyNDU0XSwgWy02Ni42OTg0OTk0OTA4Nzg0LCA0NS45ODU2MjU1MjY4MjE5XSwgWy02Ni42OTgyMjEwMTMxNDAzLCA0NS45ODM2MjE4NTg4NjIxXSwgWy02Ni42OTgyMDMwNDY4MzQ2LCA0NS45ODEyMDYxMjUzN10sIFstNjYuNjk4NTYyMzcyOTQ4MywgNDUuOTc4NDg0Mzk3NTQxMV0sIFstNjYuNjk4OTkzNTY0Mjg0NywgNDUuOTc2NzE3Njk5ODQ2NF0sIFstNjYuNjk3OTg3NDUxMTY2NSwgNDUuOTc2NzgwMTI4Mjg3NV0sIFstNjYuNjk2Mjg5NjM1Mjc5NSwgNDUuOTc3MTU0Njk3NDU1OV0sIFstNjYuNjk1MzEwNDcxNjE5OCwgNDUuOTc3MjQyMDk2NTY0XSwgWy02Ni42OTQxMDY3MjkxMzkxLCA0NS45NzcxNzk2Njg2NDM3XSwgWy02Ni42OTAyODg4ODkxODE1LCA0NS45NzYzMTE5MTMyNjM5XSwgWy02Ni42ODQ5NTI4OTYzOTM5LCA0NS45NzQ2NzAwMDc5NjU5XSwgWy02Ni42ODAyMDA4MDg1NDA5LCA0NS45NzE5NjY2ODkwMDg0XSwgWy02Ni42Nzg0MjIxNDQyNzgzLCA0NS45NzE0MjM1MTIwMDQ0XSwgWy02Ni42NzYxMjI0NTcxNTEsIDQ1Ljk3MTM0MjM0NzE2N10sIFstNjYuNjczNTQ0MjkyMjg1NiwgNDUuOTcxNDM1OTk4ODkxOV0sIFstNjYuNjY1Mzg3NTg5NTA1OCwgNDUuOTcyMDg1MzEzMTYyNl0sIFstNjYuNjU0MTc2NjE0NzU5OSwgNDUuOTcyNTg0NzgwNDk4NV0sIFstNjYuNjUwNDEyNjczNzE5NSwgNDUuOTcyNTIyMzQ3MzI3OF0sIFstNjYuNjQ3ODUyNDc1MTU5NywgNDUuOTcyMjk3NTg3MzMwN10sIFstNjYuNjQ3NTAyMTMyMTk4OSwgNDUuOTcyMTQxNTAzNDYyN10sIFstNjYuNjQzNzkyMDkwMDc1NSwgNDUuOTcxNjI5NTQ1Mjg4MV0sIFstNjYuNjQxNDU2NDcwMzM2OCwgNDUuOTcxMDMwMTczNjA3XSwgWy02Ni42NDYyOTgzODk3MTgyLCA0NS45NzI1NDEwNzcyODY0XSwgWy02Ni42NTAzNDA4MDg0OTY4LCA0NS45NzQwMjA3MjM5OTg0XSwgWy02Ni42NTU3MTI3MzM4OTU4LCA0NS45NzY0MDU1NTY1ODUzXSwgWy02Ni42NTgxOTIwODQwOCwgNDUuOTc3NzIyNzg5MTkyNV0sIFstNjYuNjYwNDQ2ODU1NDQzMSwgNDUuOTc5MjMzNTEwMjg3Nl0sIFstNjYuNjYyMDcyODA2MTA3NCwgNDUuOTgwNjgxNzY2MTkzM10sIFstNjYuNjYzMzEyNDgxMTk5NCwgNDUuOTgyNTE3MDAxNTg1NF0sIFstNjYuNjYzOTc3MjM0NTA5NywgNDUuOTg0NDg5NDk5Njg0N11dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogMTMsICJOZWlnaGJvdXJoIjogIk5hc2h3YWFrc2lzIiwgIk9CSkVDVElEIjogMTMsICJTaGFwZV9BcmVhIjogNTkyODk2NC4xMTU5NSwgIlNoYXBlX0xlbmciOiAxNDAzMC40MTk0OTU1LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjY1MDAyNjM5ODE0NzMsIDQ1Ljk5MjMwMzg5NjI2NjRdLCBbLTY2LjY0ODEyMTk2OTc0NSwgNDUuOTkyMjk3NjU1MTc1OF0sIFstNjYuNjQ2NjEyODAwMDY3NywgNDUuOTkyNDIyNDc2ODU0XSwgWy02Ni42NDQ3NTMyODc0Mjk1LCA0NS45OTI3MjIwNDc3MzI5XSwgWy02Ni42NDMzMTU5ODI5NzQ5LCA0NS45OTMwNzc3ODYwNDU1XSwgWy02Ni42NDE2MDkxODM5MzUxLCA0NS45OTM2NjQ0MzcyMTU0XSwgWy02Ni42NDAwMTkxNjU4ODIyLCA0NS45OTQ0MDA4NjI4NTk3XSwgWy02Ni42Mzg0MjkxNDc4MjkzLCA0NS45OTU1OTkwOTM4MTA3XSwgWy02Ni42Mzc1NjY3NjUxNTY2LCA0NS45OTY2NzI0ODcwMDYzXSwgWy02Ni42MzcwOTA2NTgwNTYsIDQ1Ljk5NzYzOTc3MTE3ODFdLCBbLTY2LjYzNjg0ODExMjkyOTMsIDQ1Ljk5ODY1MDcyMTA4MDFdLCBbLTY2LjYzNjg1NzA5NjA4MjEsIDQ1Ljk5OTY3NDEzMzAzMTRdLCBbLTY2LjYzNzI3MDMyMTExMjgsIDQ2LjAwMDUyOTA0MTkxODhdLCBbLTY2LjYzNzkwODEyNDk2NDUsIDQ2LjAwMTMyMTUzNjg5OTRdLCBbLTY2LjYzODczNDU3NTAyNTksIDQ2LjAwMjAyNjY2MDY4NTJdLCBbLTY2LjYzOTc0MDY4ODE0NDEsIDQ2LjAwMjYwNjk3NzA1OTVdLCBbLTY2LjY0MDYzOTAwMzQyODMsIDQ2LjAwMjk3NTEzMTYwMzVdLCBbLTY2LjY1MDAyNjM5ODE0NzMsIDQ1Ljk5MjMwMzg5NjI2NjRdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDE0LCAiTmVpZ2hib3VyaCI6ICJXZXN0IEhpbGxzIiwgIk9CSkVDVElEIjogMTQsICJTaGFwZV9BcmVhIjogNTk3MzAzLjg5MDQ3MiwgIlNoYXBlX0xlbmciOiAzMzY0LjU0NzMzMDM1LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjYzMDk1NTE2NDY2NTUsIDQ2LjAwNzU5ODY5NDQ3OTJdLCBbLTY2LjYzMDY3NjY4NjkyNzQsIDQ2LjAxNDM5Mjk0NTkzODFdLCBbLTY2LjYzMDM2MjI3NjU3NzksIDQ2LjAxNjE0NTk2NDQyOThdLCBbLTY2LjYzMzc3NTg3NDY1NzYsIDQ2LjAxNjMzMzExNjE0NThdLCBbLTY2LjYzNTM4Mzg1OTAxNjIsIDQ2LjAxNjMwMTkyNDIzNzFdLCBbLTY2LjYzODE3NzYxOTU0OTgsIDQ2LjAxNTk1MjU3MzY1NzldLCBbLTY2LjYzOTQwODMxMTQ4OSwgNDYuMDE1NTg0NTA1NDgxNF0sIFstNjYuNjQwMDM3MTMyMTg3OSwgNDYuMDE1MTkxNDgwODI1N10sIFstNjYuNjQwNjY1OTUyODg2OCwgNDYuMDE0NTk4ODE5MzE3XSwgWy02Ni42NDEwNzAxOTQ3NjQ2LCA0Ni4wMTM5MTg4MTAzOTNdLCBbLTY2LjY0MTIzMTg5MTUxNTgsIDQ2LjAxMzE5NTEyMTk4NjldLCBbLTY2LjY0MDYzMDAyMDI3NTQsIDQ2LjAxMTk3ODU1NTQ4MTNdLCBbLTY2LjYzOTY5NTc3MjM3OTksIDQ2LjAxMDg2ODAyNTI1NjVdLCBbLTY2LjYzODY5ODY0MjQxNDYsIDQ2LjAxMDA1Njk0OTc2NjhdLCBbLTY2LjYzNzI2MTMzNzk2LCA0Ni4wMDkyNDU4NjIzODMyXSwgWy02Ni42MzMxNzQwMDM0MTcyLCA0Ni4wMDc5MTA2NjE4NjI2XSwgWy02Ni42MzA5NjQxNDc4MTgzLCA0Ni4wMDc0MjM5OTE5NzZdLCBbLTY2LjYzMDk1NTE2NDY2NTUsIDQ2LjAwNzU5ODY5NDQ3OTJdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDE1LCAiTmVpZ2hib3VyaCI6ICJOb3J0aGJyb29rIEhlaWdodHMiLCAiT0JKRUNUSUQiOiAxNSwgIlNoYXBlX0FyZWEiOiA2MTI3MDIuMjg2OTU3LCAiU2hhcGVfTGVuZyI6IDMwNzYuMDY3NTU5MTIsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlZDk3NiIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjQwMTg5ODQ1Nzg2MiwgNDYuMDExMzkyMDk4NDc4Ml0sIFstNjYuNjQzOTA4ODcxMDYyNSwgNDYuMDEyMzM0MTY5OTk3XSwgWy02Ni42NDcyNzc1NTMzNzc5LCA0Ni4wMTI3MTQ3MzczODQ1XSwgWy02Ni42NDgxMTI5ODY1OTIxLCA0Ni4wMTI2MDg2Nzc4ODRdLCBbLTY2LjY0OTAxMTMwMTg3NjIsIDQ2LjAxMjI3MTc4MTY1MDldLCBbLTY2LjY0OTU5NTIwNjgxMDksIDQ2LjAxMTg0NzUzOTAzMDddLCBbLTY2LjY1MDA0NDM2NDQ1MywgNDYuMDExMjA0OTMwMDQwNV0sIFstNjYuNjQ5Njg1MDM4MzM5NCwgNDYuMDEwMjQ0MTIyMDg5M10sIFstNjYuNjQ5MDkyMTUwMjUxOCwgNDYuMDA5MzM5NDQ5OTk2XSwgWy02Ni42NDgyODM2NjY0OTYxLCA0Ni4wMDg1MjIxMTI4MzAzXSwgWy02Ni42NDcyODY1MzY1MzA3LCA0Ni4wMDc4MTA4MzI0OTE0XSwgWy02Ni42NDYzNzAyNTQ5NDA5LCA0Ni4wMDczMzY2NDA1MTc1XSwgWy02Ni42NDQ4MzQxMzU4MDUxLCA0Ni4wMDY4MTI1Mjg4Njk1XSwgWy02Ni42NDIxMzAyMDY3OTk5LCA0Ni4wMDU1OTU4MjE5NzA5XSwgWy02Ni42MzkyNDY2MTQ3Mzc5LCA0Ni4wMDQ1OTEyMzg2NzAyXSwgWy02Ni42MzU3MTYyMzU2NzEzLCA0Ni4wMDg2OTA1NzI2MjM1XSwgWy02Ni42MzcyNjEzMzc5NiwgNDYuMDA5MjQ1ODYyMzgzMl0sIFstNjYuNjM4MjQwNTAxNjE5NywgNDYuMDA5NzU3NDcyNzMzM10sIFstNjYuNjM5MzA5NDk2ODA3OCwgNDYuMDEwNTE4NjQwMzQ5OV0sIFstNjYuNjQwMTg5ODQ1Nzg2MiwgNDYuMDExMzkyMDk4NDc4Ml1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogMTYsICJOZWlnaGJvdXJoIjogIkJyb29rc2lkZSBNaW5pIEhvbWUgUGFyayIsICJPQkpFQ1RJRCI6IDE2LCAiU2hhcGVfQXJlYSI6IDU3NTE4OC4wMzQzNzcsICJTaGFwZV9MZW5nIjogMzAyMi45NzU2NDMzLCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjY0ODY5Njg5MTUyNjgsIDQ2LjAwODg5NjQ2NzIyOTddLCBbLTY2LjY0OTk2MzUxNjA3NzQsIDQ2LjAwODkwMjcwNjQ0ODJdLCBbLTY2LjY1MTIxMjE3NDMyMjMsIDQ2LjAwODczNDI0NzMwMV0sIFstNjYuNjUyMzc5OTg0MTkxNywgNDYuMDA4MzkxMDg4MTkxOV0sIFstNjYuNjUzNjE5NjU5MjgzOCwgNDYuMDA3NzczMzk2NDMwN10sIFstNjYuNjU0MzgzMjI3Mjc1MywgNDYuMDA3MDQzMzg4MTgzNV0sIFstNjYuNjU1MDAzMDY0ODIxMywgNDYuMDA2MDQ1MDcwNzExM10sIFstNjYuNjU1MjkwNTI1NzEyMywgNDYuMDA0OTc4MDk4OTk1Nl0sIFstNjYuNjU1MjA5Njc3MzM2NywgNDYuMDAzODk4NjI3MTM2OF0sIFstNjYuNjU0OTQ5MTY1OTA0MywgNDYuMDAzMTkzNTI3MjA5Ml0sIFstNjYuNjU0NDE5MTU5ODg2NywgNDYuMDAyMzY5ODU5Mjc2NF0sIFstNjYuNjUzNTExODYxNDQ5NywgNDYuMDAxNDA4ODk3ODU2Ml0sIFstNjYuNjUyMjk5MTM1ODE2MSwgNDYuMDAwNDA0MjM4NTI1MV0sIFstNjYuNjQ5OTk5NDQ4Njg4OCwgNDUuOTk5MDQzODYzMjc2MV0sIFstNjYuNjQ1NzUwNDE3Mzk0OSwgNDUuOTk3MjAyOTM1MjU4OF0sIFstNjYuNjM5MjQ2NjE0NzM3OSwgNDYuMDA0NTkxMjM4NjcwMl0sIFstNjYuNjQxNjU0MDk5Njk5MywgNDYuMDA1NDE0ODczNTMwOF0sIFstNjYuNjQ0ODM0MTM1ODA1MSwgNDYuMDA2ODEyNTI4ODY5NV0sIFstNjYuNjQ2NTQ5OTE3OTk3OCwgNDYuMDA3NDIzOTkxOTc2XSwgWy02Ni42NDc4MTY1NDI1NDg0LCA0Ni4wMDgxNjAyMzQ1MDI1XSwgWy02Ni42NDg2OTY4OTE1MjY4LCA0Ni4wMDg4OTY0NjcyMjk3XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiAxNywgIk5laWdoYm91cmgiOiAiSGVyb24gU3ByaW5ncyIsICJPQkpFQ1RJRCI6IDE3LCAiU2hhcGVfQXJlYSI6IDk2NTEzMS4wMDAzMjEsICJTaGFwZV9MZW5nIjogMzgwMC45NDU5ODkyOCwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmVkOTc2IiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni42NjY0Mzg2MTgzODgyLCA0NS45OTMwOTY1MDkwNTEzXSwgWy02Ni42Njg0NTA4NDQ2MjQ2LCA0NS45OTQ0OTQ0NzU1ODcxXSwgWy02Ni42NzAyOTIzOTA5NTcsIDQ1Ljk5NTk5ODQ5ODM2MjNdLCBbLTY2LjY3MTk0NTI5MTA3OTgsIDQ1Ljk5NzYxNDgwOTIxODVdLCBbLTY2LjY3MzM5MTU3ODY4NzMsIDQ1Ljk5OTMxODQzNzEyMTRdLCBbLTY2LjY3NDczOTA1MTYxMzQsIDQ2LjAwMjc2Mjk3NTA0NjddLCBbLTY2LjY3NTY0NjM1MDA1MDQsIDQ2LjAwNTU0NTkwNTIxODldLCBbLTY2LjY3NjU2MjYzMTY0MDIsIDQ2LjAwOTA1MjQ0NzQ4MTddLCBbLTY2LjY3NzExOTU4NzExNjQsIDQ2LjAxMTg3ODczMzQ1MThdLCBbLTY2LjY3NzM1MzE0OTA5MDIsIDQ2LjAxMjQyNzc1MjM4NDNdLCBbLTY2LjY3ODEwNzczMzkyODksIDQ2LjAxMzc1MDM2NjUyMzRdLCBbLTY2LjY3OTA4Njg5NzU4ODYsIDQ2LjAxNDk5ODA4NjcxNTddLCBbLTY2LjY4MDI4MTY1NjkxNjUsIDQ2LjAxNjE1MjIwMjgzMDZdLCBbLTY2LjY4MTM3NzYwMTU2MzEsIDQ2LjAxNzAwMDYxODc3NDddLCBbLTY2LjY4MTAwMDMwOTE0MzgsIDQ2LjAwOTYxMzk3Mjc0NjhdLCBbLTY2LjY5MjQxNzg5NjQwNDksIDQ1Ljk5NTY2MTUwMDk2MTldLCBbLTY2LjY5MDgwMDkyODg5MzUsIDQ1Ljk5NDcxOTE0NTQ4NjZdLCBbLTY2LjY4ODY1Mzk1NTM2NDQsIDQ1Ljk5Mzg3MDM4Nzc0NzFdLCBbLTY2LjY4NjE2NTYyMjAyNzQsIDQ1Ljk5MzI5NjIyMDcxODRdLCBbLTY2LjY4MzA5MzM4Mzc1NTgsIDQ1Ljk5Mjg1OTM1MDUxMDVdLCBbLTY2LjY3OTk2NzI0NjU2NywgNDUuOTkyNjcyMTE5MzY1N10sIFstNjYuNjczMTEzMTAwOTQ5MiwgNDUuOTkyNzE1ODA2Njg5NV0sIFstNjYuNjY5Mzk0MDc1NjcyOSwgNDUuOTkyODU5MzUwNTEwNV0sIFstNjYuNjY2NDM4NjE4Mzg4MiwgNDUuOTkzMDk2NTA5MDUxM11dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogMTgsICJOZWlnaGJvdXJoIjogIlJveWFsIFJvYWQiLCAiT0JKRUNUSUQiOiAxOCwgIlNoYXBlX0FyZWEiOiAyMTk2ODI3LjQyNzU4LCAiU2hhcGVfTGVuZyI6IDc2NzQuODIyNjU1MzMsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlZDk3NiIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjM3OTI2MDkxMjcwMiwgNDUuOTc2NzIzOTQyNjkzN10sIFstNjYuNjM4NTk5ODI3NzMzMywgNDUuOTc2OTczNjU2MDA3NV0sIFstNjYuNjM4MDUxODU1NDEsIDQ1Ljk3NjkxMTIyNzc4NDZdLCBbLTY2LjYzNzY0NzYxMzUzMjEsIDQ1Ljk3NzExNzI0MDY1MzFdLCBbLTY2LjYzNjIyODI3NTM4MzIsIDQ1Ljk3ODg5NjQxMDgwNTldLCBbLTY2LjYzNTQyODc3NDc4MDQsIDQ1Ljk4MDM2MzQwMjg0MTddLCBbLTY2LjYzNTA2OTQ0ODY2NjcsIDQ1Ljk4MTk5ODg5NzA3NjNdLCBbLTY2LjYzNTMyOTk2MDA5OTEsIDQ1Ljk4NjkwNTA4OTkxMDFdLCBbLTY2LjYzNTk1ODc4MDc5OCwgNDUuOTg4MTY1ODk4NzUzOV0sIFstNjYuNjM3MTg5NDcyNzM3MiwgNDUuOTg5NDI2Njc4ODhdLCBbLTY2LjYzODIwNDU2OTAwODMsIDQ1Ljk5MDA1MDgxNjgzXSwgWy02Ni42NDAxMDAwMTQyNTc4LCA0NS45OTA2NDk5ODI2NDA3XSwgWy02Ni42NDIxMTIyNDA0OTQyLCA0NS45OTEwMTgyMTY3NDM3XSwgWy02Ni42NDQxNzgzNjU2NDc3LCA0NS45OTExNDkyODI1MjgyXSwgWy02Ni42NDU5MDMxMzA5OTMyLCA0NS45OTEwODA2MjkwNjA4XSwgWy02Ni42NTAzMjI4NDIxOTExLCA0NS45OTA1NTYzNjM0MTAzXSwgWy02Ni42NTU1OTU5NTI5MDg5LCA0NS45ODk3MTM3ODMyMTExXSwgWy02Ni42NTU5NDYyOTU4Njk3LCA0NS45ODgzNTkzODY2NzgzXSwgWy02Ni42NTY1MjEyMTc2NTE1LCA0NS45ODcwNDg2NDg4MDE1XSwgWy02Ni42NTc3MTU5NzY5Nzk0LCA0NS45ODUzMDcxOTE4OTgyXSwgWy02Ni42NTg1NjkzNzY0OTkzLCA0NS45ODQzODMzODYwNjk0XSwgWy02Ni42NTg3NjcwMDU4NjE4LCA0NS45ODQzNzA5MDIxMDEyXSwgWy02Ni42NTg2NjgxOTExODA2LCA0NS45ODQxMDI0OTYxMDU3XSwgWy02Ni42NTY3OTk2OTUzODk2LCA0NS45ODI5OTE0MDYyODExXSwgWy02Ni42NTQzNTYyNzc4MTY4LCA0NS45ODE5NjE0NDM1NTA0XSwgWy02Ni42Mzc5MjYwOTEyNzAyLCA0NS45NzY3MjM5NDI2OTM3XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiAxOSwgIk5laWdoYm91cmgiOiAiRnVsdG9uIEhlaWdodHMiLCAiT0JKRUNUSUQiOiAxOSwgIlNoYXBlX0FyZWEiOiAyMDA4Njk5LjI0OTAxLCAiU2hhcGVfTGVuZyI6IDU1ODYuMDc4OTcxODcsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlZDk3NiIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjU5MDI3NTE3Mjk0MiwgNDUuOTg0NDE0NTk1OTc3M10sIFstNjYuNjYyMjM0NTAyODU4NSwgNDUuOTg1NjQ0MjUyMzQ4Nl0sIFstNjYuNjYzMDk2ODg1NTMxMiwgNDUuOTg1NzQ0MTIxNzE3Nl0sIFstNjYuNjY0MzM2NTYwNjIzMywgNDUuOTg1NjMxNzY4NjY0OF0sIFstNjYuNjY0MjI4NzYyNzg5MiwgNDUuOTg0ODc2NTAwNTU4NF0sIFstNjYuNjYzMDUxOTY5NzY3LCA0NS45ODIwNDI1OTI4MjQ1XSwgWy02Ni42NjE4ODQxNTk4OTc3LCA0NS45ODA0Njk1MjQxNjIzXSwgWy02Ni42NjA0NDY4NTU0NDMxLCA0NS45NzkyMzM1MTAyODc2XSwgWy02Ni42NTg5NzM2MTgzNzcxLCA0NS45NzgyMDM0Nzc2NDgzXSwgWy02Ni42NTY5NzkzNTg0NDY0LCA0NS45NzcwNDIzMjY5NzE0XSwgWy02Ni42NTIzMDgxMTg5NjksIDQ1Ljk3NDgzODU3MDgyODJdLCBbLTY2LjY0NzY2MzgyODk1MDEsIDQ1Ljk3MzAwOTMyNDE5MjRdLCBbLTY2LjY0MTQ1NjQ3MDMzNjgsIDQ1Ljk3MTAzMDE3MzYwN10sIFstNjYuNjQwMjE2Nzk1MjQ0NywgNDUuOTczNTA4NzgzMTk1Ml0sIFstNjYuNjM3OTI2MDkxMjcwMiwgNDUuOTc2NzIzOTQyNjkzN10sIFstNjYuNjU0NzE1NjAzOTMwNCwgNDUuOTgyMDg2Mjg4NTM4Ml0sIFstNjYuNjU3MTIzMDg4ODkxOSwgNDUuOTgzMTY2MTg1OTMzN10sIFstNjYuNjU4NjY4MTkxMTgwNiwgNDUuOTg0MTAyNDk2MTA1N10sIFstNjYuNjU4NzY3MDA1ODYxOCwgNDUuOTg0MzcwOTAyMTAxMl0sIFstNjYuNjU5MDI3NTE3Mjk0MiwgNDUuOTg0NDE0NTk1OTc3M11dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogMjAsICJOZWlnaGJvdXJoIjogIk1haW4gU3RyZWV0IiwgIk9CSkVDVElEIjogMjAsICJTaGFwZV9BcmVhIjogMTI5NDU4Mi4xNzQ0NCwgIlNoYXBlX0xlbmciOiA1NTQ1Ljg5MzE1Nzk4LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWIyNGMiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjcwNDU3MjEwMjE5OSwgNDUuOTc4MzQwODE2NDQwNl0sIFstNjYuNzAxMDk1NjIyMDQ5NSwgNDUuOTc4NTk2NzY1MDk5Ml0sIFstNjYuNzAxMjQ4MzM1NjQ3OCwgNDUuOTc5Njc2NzMwNTU3Ml0sIFstNjYuNzAxNjI1NjI4MDY3MSwgNDUuOTgwNTQ0NDMzMjA3M10sIFstNjYuNzAzMzk1MzA5MTc2OCwgNDUuOTgyNTU0NDU0NzM1NV0sIFstNjYuNzAzOTcwMjMwOTU4NywgNDUuOTgyNjg1NTQwNTYxMl0sIFstNjYuNzA0Njg4ODgzMTg2LCA0NS45ODI2MTY4NzY1OTZdLCBbLTY2LjcwNTI3Mjc4ODEyMDcsIDQ1Ljk4MjMyMzQ5MzIzOTZdLCBbLTY2LjcwNTYxNDE0NzkyODYsIDQ1Ljk4MTM2MjE4MzY4OThdLCBbLTY2LjcwNTM5ODU1MjI2MDQsIDQ1Ljk3OTk1MTQwMDQ5MjldLCBbLTY2LjcwNDU3MjEwMjE5OSwgNDUuOTc4MzQwODE2NDQwNl1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogMjEsICJOZWlnaGJvdXJoIjogIlJlZ2ltZW50IENyZWVrIiwgIk9CSkVDVElEIjogMjEsICJTaGFwZV9BcmVhIjogMTIzNjMyLjEyNjg5NCwgIlNoYXBlX0xlbmciOiAxMzc1LjAzMjY1MDMsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlZDk3NiIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNzE2Njk5MzU4NTM0NywgNDUuOTc3NjQxNjMzNTg3XSwgWy02Ni43MDgxNjUzNjMzMzU1LCA0NS45NzgxMDM1OTQ2NzYyXSwgWy02Ni43MDc0NjQ2Nzc0MTM5LCA0NS45NzkyMTQ3ODI1OTI1XSwgWy02Ni43MDcwOTYzNjgxNDc0LCA0NS45ODA0MDcwOTk4ODA3XSwgWy02Ni43MDc2MzUzNTczMTc5LCA0NS45ODEyODcyNzU3NTEyXSwgWy02Ni43MDg2NTk0MzY3NDE4LCA0NS45ODIxNDg3MTA5MjY2XSwgWy02Ni43MDk4MDkyODAzMDU1LCA0NS45ODI2ODU1NDA1NjEyXSwgWy02Ni43MTA3MDc1OTU1ODk2LCA0NS45ODI2MzU2MDMxNDA0XSwgWy02Ni43MTE3MzE2NzUwMTM1LCA0NS45ODIzNjcxODg3MzE2XSwgWy02Ni43MTMwODgxMzEwOTI1LCA0NS45ODE1NDMyMTA3ODk4XSwgWy02Ni43MTQ3MDUwOTg2MDM5LCA0NS45ODAxOTQ4NTY3OTY5XSwgWy02Ni43MTYwNDM1ODgzNzczLCA0NS45Nzg3MDI4ODk4MDU3XSwgWy02Ni43MTY2OTkzNTg1MzQ3LCA0NS45Nzc2NDE2MzM1ODddXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDIyLCAiTmVpZ2hib3VyaCI6ICJHaWxyaWRnZSBFc3RhdGVzIiwgIk9CSkVDVElEIjogMjIsICJTaGFwZV9BcmVhIjogMjcxNzM5LjY3Mjc0NCwgIlNoYXBlX0xlbmciOiAyMDk1Ljc3NjAzNDgsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlZDk3NiIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNzU5NzQ2NjI2OTQ5NywgNDUuOTU4NDM1NjI1MDQ5NV0sIFstNjYuNzQ0ODc5NTA4OTk3NSwgNDUuOTU4NDY2ODQ5NTgyN10sIFstNjYuNzQ1MDMyMjIyNTk1OCwgNDUuOTU4ODQ3Nzg3NDcwNF0sIFstNjYuNzQ1ODEzNzU2ODkzLCA0NS45NTk1OTA5MjEwNTc2XSwgWy02Ni43NDU2MzQwOTM4MzYyLCA0NS45NTk4NTMyMDExMjA1XSwgWy02Ni43NDU2MDcxNDQzNzc2LCA0NS45NjAzMzQwNDQ2NzhdLCBbLTY2Ljc0NTA0MTIwNTc0ODYsIDQ1Ljk2MTAxNDcxMjE4OTddLCBbLTY2Ljc0NTE5MzkxOTM0NjksIDQ1Ljk2MTMyNjk0MjE5NTZdLCBbLTY2Ljc0NTA3NzEzODM2LCA0NS45NjE5MDc2ODUzMjY1XSwgWy02Ni43NDU1NTMyNDU0NjA2LCA0NS45NjIxMTk5OTg0OTk5XSwgWy02Ni43NDU2MDcxNDQzNzc2LCA0NS45NjIyODg1OTk1NTgxXSwgWy02Ni43NDQ3NDQ3NjE3MDQ5LCA0NS45NjM0NTAwNTk1NzIzXSwgWy02Ni43NDQ2NzI4OTY0ODIxLCA0NS45NjQ1NDkwNTMwNzkxXSwgWy02Ni43NDUzNzM1ODI0MDM4LCA0NS45NjUzMzU4MTkxMzA2XSwgWy02Ni43NDU4MjI3NDAwNDU4LCA0NS45NjU0NzMxODk4MzVdLCBbLTY2Ljc0NjE4MjA2NjE1OTUsIDQ1Ljk2NTgyMjg1OTE4Ml0sIFstNjYuNzQ2NDk2NDc2NTA4OSwgNDUuOTY3MzA4OTI5MjgyOF0sIFstNjYuNzQ3ODUyOTMyNTg3OSwgNDUuOTY3MTkwMjk0ODk4N10sIFstNjYuNzQ5NTQxNzY1MzIyMSwgNDUuOTY3NTA4NzMzOTg3XSwgWy02Ni43NDk2MTM2MzA1NDQ4LCA0NS45NjQ0ODAzNjY2MjM2XSwgWy02Ni43NTU1ODc0MjcxODQyLCA0NS45NjQ4MjM3OTgwNDkzXSwgWy02Ni43NTU1Nzg0NDQwMzE0LCA0NS45NjkwMTk3MzM3MjgxXSwgWy02Ni43NTU3MjIxNzQ0NzY4LCA0NS45NjkwNzU5MjcxMzg0XSwgWy02Ni43NjA4Nzg1MDQyMDc3LCA0NS45Njk3MzE1MTI3MTI4XSwgWy02Ni43NjI0MjM2MDY0OTYzLCA0NS45NzAxNjIzMjE4NjU0XSwgWy02Ni43NjMzMTI5Mzg2Mjc2LCA0NS45NzA1NjgxNTM1MDkxXSwgWy02Ni43NjU4MTkyMzgyNzAzLCA0NS45NzA5MzAyNzc2OTYyXSwgWy02Ni43NjcxNjY3MTExOTY1LCA0NS45NzA4ODY1NzMxNzg2XSwgWy02Ni43NjkzODU1NDk5NDgzLCA0NS45NzExNTUwNDMyNDIxXSwgWy02Ni43NzI5OTY3NzczOTA0LCA0NS45NzA5MTE1NDcxOTI5XSwgWy02Ni43NzQzMDgzMTc3MDUyLCA0NS45NzA5OTg5NTYxNTQyXSwgWy02Ni43NzY3Njk3MDE1ODM3LCA0NS45NzA3MzY3Mjg4NTYzXSwgWy02Ni43Nzg1NzUzMTUzMDQ4LCA0NS45NzA5Njc3Mzg2ODM5XSwgWy02Ni43Nzk0Mjg3MTQ4MjQ3LCA0NS45NzEzNzk4MDc4NzU5XSwgWy02Ni43ODE4OTAwOTg3MDMyLCA0NS45NzE1Mjk2NTA0NTg0XSwgWy02Ni43ODE5OTc4OTY1MzczLCA0NS45NzE2NzMyNDkyMTk1XSwgWy02Ni43ODI5MzIxNDQ0MzI4LCA0NS45NzE3MTA3MDk3MDQ2XSwgWy02Ni43ODM0NjIxNTA0NTA0LCA0NS45NzE1Mjk2NTA0NTg0XSwgWy02Ni43ODMxMjk3NzM3OTUzLCA0NS45NzA3NDkyMTU4OTg2XSwgWy02Ni43ODI0MDIxMzg0MTUyLCA0NS45Njk4MjUxNjcxNjE1XSwgWy02Ni43ODE4NTQxNjYwOTE5LCA0NS45Njk2OTQwNTA4ODkxXSwgWy02Ni43ODE2NDc1NTM1NzY1LCA0NS45NjkyNjMyMzgwOTQzXSwgWy02Ni43ODExODk0MTI3ODE2LCA0NS45Njg4NTczOTY4ODkzXSwgWy02Ni43ODA1NDI2MjU3NzcsIDQ1Ljk2ODYyMDEzNDQ5OTddLCBbLTY2Ljc4MDA2NjUxODY3NjQsIDQ1Ljk2ODY3MDA4NDU2MDldLCBbLTY2Ljc3OTk1ODcyMDg0MjQsIDQ1Ljk2ODU3MDE4NDM5MzVdLCBbLTY2Ljc3OTk1ODcyMDg0MjQsIDQ1Ljk2ODM5NTM1ODY2NjldLCBbLTY2Ljc4MDI0NjE4MTczMzMsIDQ1Ljk2ODA4MzE2ODQ5NjldLCBbLTY2Ljc3OTk4NTY3MDMwMDksIDQ1Ljk2NzIyNzc1ODQxNTldLCBbLTY2Ljc4MDAzMDU4NjA2NTEsIDQ1Ljk2NjMyMjM4Mjk5MTddLCBbLTY2Ljc3OTg5NTgzODc3MjUsIDQ1Ljk2NjEyODgxODA1XSwgWy02Ni43Nzk1NTQ0Nzg5NjQ1LCA0NS45NjYwNzI2MjE2NDk5XSwgWy02Ni43NzkzMjk5MDAxNDM1LCA0NS45NjU1NzMwOTU1ODhdLCBbLTY2Ljc3OTAwNjUwNjY0MTIsIDQ1Ljk2NTM0MjA2MzI2MDldLCBbLTY2Ljc3OTMyMDkxNjk5MDYsIDQ1Ljk2NDY0ODk2MDQ5ODZdLCBbLTY2Ljc3OTA5NjMzODE2OTYsIDQ1Ljk2NDE4MDY0MjkxMjNdLCBbLTY2Ljc3Nzk3MzQ0NDA2NDUsIDQ1Ljk2MzQyNTA4MjE5MzhdLCBbLTY2Ljc3ODMwNTgyMDcxOTYsIDQ1Ljk2MzAxOTE5ODIxNDVdLCBbLTY2Ljc3NzU0MjI1MjcyODEsIDQ1Ljk2MjcwMDczMzMxOF0sIFstNjYuNzc3NTUxMjM1ODgwOSwgNDUuOTYyMjMyMzk5MjYyNF0sIFstNjYuNzc4NDA0NjM1NDAwOCwgNDUuOTYxNTE0Mjc5MzU0NV0sIFstNjYuNzc4OTI1NjU4MjY1NiwgNDUuOTYwNzk2MTUwMTM4N10sIFstNjYuNzc5MDA2NTA2NjQxMiwgNDUuOTYwMTY1NDM3NjcxOV0sIFstNjYuNzgwMTM4MzgzODk5MiwgNDUuOTU4OTk3NjYzOTU0Ml0sIFstNjYuNzgxMDU0NjY1NDg5LCA0NS45NTg4MzUyOTc3NDUxXSwgWy02Ni43ODE0ODU4NTY4MjU0LCA0NS45NTgzNzk0MjA4NDU1XSwgWy02Ni43NzA2MjUyMjUwNDA0LCA0NS45NTg0MTA2NDU0MTAzXSwgWy02Ni43NzE1NDE1MDY2MzAyLCA0NS45NjYwNzg4NjU2OTcyXSwgWy02Ni43Njc3NDE2MzI5NzgzLCA0NS45NjU0NDE5NjkyNTAzXSwgWy02Ni43NTk4NTQ0MjQ3ODM4LCA0NS45NjUxMDQ3ODU4MTRdLCBbLTY2Ljc2MDAxNjEyMTUzNDksIDQ1Ljk2MzIyNTI2Mjc2MDJdLCBbLTY2Ljc1OTc0NjYyNjk0OTcsIDQ1Ljk1ODQzNTYyNTA0OTVdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDIzLCAiTmVpZ2hib3VyaCI6ICJTaWx2ZXJ3b29kIiwgIk9CSkVDVElEIjogMjMsICJTaGFwZV9BcmVhIjogMjUwNDk0MC4wODY2NiwgIlNoYXBlX0xlbmciOiAxMTMxMi43ODg2MDk5LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjcxMzUxMDMzOTI3NiwgNDUuOTU4NTI5Mjk4NTk2Ml0sIFstNjYuNzEyMDM3MTAyMjEwMSwgNDUuOTU4ODYwMjc3MTkyOF0sIFstNjYuNzEwNjcxNjYyOTc4MiwgNDUuOTU5MzU5ODYzNzgzXSwgWy02Ni43MDk2ODM1MTYxNjU3LCA0NS45NTk4NjU2OTA2MTYzXSwgWy02Ni43MDg2MTQ1MjA5Nzc2LCA0NS45NjA2Mjc1NDQ1Mzg4XSwgWy02Ni43MDc3NDMxNTUxNTIsIDQ1Ljk2MTQ5NTU0NTY2NzFdLCBbLTY2LjcwNzExNDMzNDQ1MzEsIDQ1Ljk2MjQxOTczMzM1OTddLCBbLTY2LjcwNjk3MDYwNDAwNzcsIDQ1Ljk2MzE5NDA0MDkwODZdLCBbLTY2LjcwNzE3NzIxNjUyMywgNDUuOTYzOTU1ODQ5MDY0Nl0sIFstNjYuNzA4MjkxMTI3NDc1MywgNDUuOTY0MTYxOTEwMTI2NV0sIFstNjYuNzA5NDMxOTg3ODg2MSwgNDUuOTY0MTE4MjAwMjY4M10sIFstNjYuNzA5ODA5MjgwMzA1NSwgNDUuOTY0MDQ5NTEzMjc4N10sIFstNjYuNzEyMTQ0OTAwMDQ0MiwgNDUuOTYzMDMxNjg2OTk2Nl0sIFstNjYuNzE2ODM0MTA1ODI3MywgNDUuOTYyMzM4NTU1MzI4Nl0sIFstNjYuNzE5ODk3MzYwOTQ2MSwgNDUuOTYyMDM4ODIwMDI5N10sIFstNjYuNzIxOTA5NTg3MTgyNiwgNDUuOTYxNjY0MTQ4NjI1Nl0sIFstNjYuNzI0MDI5NjExMjUzMSwgNDUuOTYxNTY0MjM1ODIzM10sIFstNjYuNzI3MTkxNjgxMDUzMiwgNDUuOTYxNzk1MjgzOTA1Ml0sIFstNjYuNzI5Nzk2Nzk1Mzc3MSwgNDUuOTYyNzk0Mzk5NjU0XSwgWy02Ni43MzA3MjIwNjAxMTk4LCA0NS45NjI5NzU0ODc0NTQ3XSwgWy02Ni43MzE2MjAzNzU0MDM5LCA0NS45NjI5NjkyNDMwNTc2XSwgWy02Ni43MzI0NjQ3OTE3NzEsIDQ1Ljk2MzM2MjYzODY5ODJdLCBbLTY2LjczMzYxNDYzNTMzNDYsIDQ1Ljk2MzY0MzYzMzg3NDFdLCBbLTY2LjczNTk4NjE4NzY4NDcsIDQ1Ljk2NDQ5Mjg1NTA3NjRdLCBbLTY2LjczNzU5NDE3MjA0MzMsIDQ1Ljk2NDgyMzc5ODA0OTNdLCBbLTY2LjczODkwNTcxMjM1ODEsIDQ1Ljk2NDk3MzY1ODM2NzhdLCBbLTY2Ljc0MDMzNDAzMzY1OTgsIDQ1Ljk2NTMxMDg0MjYwMjNdLCBbLTY2Ljc0MTgxNjI1Mzg3ODYsIDQ1Ljk2NTQ5ODE2NjI5MDJdLCBbLTY2Ljc0MzMxNjQ0MDQwMzEsIDQ1Ljk2NTUxMDY1NDUxMzVdLCBbLTY2Ljc0NTIxMTg4NTY1MjYsIDQ1Ljk2NTEzNjAwNjU4ODddLCBbLTY2Ljc0NDY3Mjg5NjQ4MjEsIDQ1Ljk2NDU0OTA1MzA3OTFdLCBbLTY2Ljc0NDczNTc3ODU1MiwgNDUuOTYzNTYyNDU3NjM2NF0sIFstNjYuNzQ0ODUyNTU5NTM5LCA0NS45NjMyMzE1MDcxMjg0XSwgWy02Ni43NDUzNDY2MzI5NDUyLCA0NS45NjI3Njk0MjE5Nzk5XSwgWy02Ni43NDU2MDcxNDQzNzc2LCA0NS45NjIyODg1OTk1NTgxXSwgWy02Ni43NDU1NTMyNDU0NjA2LCA0NS45NjIxMTk5OTg0OTk5XSwgWy02Ni43NDUwNzcxMzgzNiwgNDUuOTYxOTA3Njg1MzI2NV0sIFstNjYuNzQ1MTkzOTE5MzQ2OSwgNDUuOTYxMzI2OTQyMTk1Nl0sIFstNjYuNzQ1MDQxMjA1NzQ4NiwgNDUuOTYxMDE0NzEyMTg5N10sIFstNjYuNzQ1NjA3MTQ0Mzc3NiwgNDUuOTYwMzM0MDQ0Njc4XSwgWy02Ni43NDU2MzQwOTM4MzYyLCA0NS45NTk4NTMyMDExMjA1XSwgWy02Ni43NDU4MTM3NTY4OTMsIDQ1Ljk1OTU5MDkyMTA1NzZdLCBbLTY2Ljc0NTAzMjIyMjU5NTgsIDQ1Ljk1ODg0Nzc4NzQ3MDRdLCBbLTY2Ljc0NDg3OTUwODk5NzUsIDQ1Ljk1ODQ2Njg0OTU4MjddLCBbLTY2LjcxMzUxMDMzOTI3NiwgNDUuOTU4NTI5Mjk4NTk2Ml1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogMjQsICJOZWlnaGJvdXJoIjogIlNwcmluZ2hpbGwiLCAiT0JKRUNUSUQiOiAyNCwgIlNoYXBlX0FyZWEiOiAxNTEwMjM0LjU2MjM0LCAiU2hhcGVfTGVuZyI6IDcyMzEuMzExNjkzNjQsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlZDk3NiIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNzI3MTkxNjgxMDUzMiwgNDUuOTYxNzk1MjgzOTA1Ml0sIFstNjYuNzI2MTY3NjAxNjI5MywgNDUuOTY1MDc5ODA5MTgxNV0sIFstNjYuNzI2MTk0NTUxMDg3OCwgNDUuOTY1NDkxOTIyMTc3NF0sIFstNjYuNzI2NDU1MDYyNTIwMiwgNDUuOTY1ODcyODExNzY1Nl0sIFstNjYuNzI3MDEyMDE3OTk2NCwgNDUuOTY2MTg1MDE0MzkzMV0sIFstNjYuNzI3OTgyMTk4NTAzMiwgNDUuOTY2MTM1MDYyMDkwOV0sIFstNjYuNzMwMTc0MDg3Nzk2NSwgNDUuOTY1OTQxNDk2NDk0Nl0sIFstNjYuNzMxNTAzNTk0NDE2OSwgNDUuOTY1NDk4MTY2MjkwMl0sIFstNjYuNzMyMjQ5MTk2MTAyOCwgNDUuOTY0OTIzNzA0OTczM10sIFstNjYuNzMyNDkxNzQxMjI5NSwgNDUuOTY0NDQ5MTQ1NDc5M10sIFstNjYuNzMyNDY0NzkxNzcxLCA0NS45NjM4MzcyMDc0OTk1XSwgWy02Ni43MzE5OTc2Njc4MjMyLCA0NS45NjMyMTI3NzQwMjE3XSwgWy02Ni43MzE2MjAzNzU0MDM5LCA0NS45NjI5NjkyNDMwNTc2XSwgWy02Ni43MzA3MjIwNjAxMTk4LCA0NS45NjI5NzU0ODc0NTQ3XSwgWy02Ni43Mjk3OTY3OTUzNzcxLCA0NS45NjI3OTQzOTk2NTRdLCBbLTY2LjcyNzE5MTY4MTA1MzIsIDQ1Ljk2MTc5NTI4MzkwNTJdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDI1LCAiTmVpZ2hib3VyaCI6ICJOZXRoZXJ2dWUgTWluaWhvbWUgUGFyayIsICJPQkpFQ1RJRCI6IDI1LCAiU2hhcGVfQXJlYSI6IDE2NTUyMi4yNzYwNDksICJTaGFwZV9MZW5nIjogMTU5MC40NzIwMjExNywgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmVkOTc2IiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni43MzE4NjI5MjA1MzA2LCA0NS45NjUyNzMzNzc3ODg3XSwgWy02Ni43MzEwMDA1Mzc4NTc4LCA0NS45NjU3MjI5NTM4Nzk1XSwgWy02Ni43Mjk5NzY0NTg0MzQsIDQ1Ljk2NTk2NjQ3MjczODZdLCBbLTY2LjcyNzAxMjAxNzk5NjQsIDQ1Ljk2NjE4NTAxNDM5MzFdLCBbLTY2LjcyNjUyNjkyNzc0MjksIDQ1Ljk2NTkzNTI1MjQzMTldLCBbLTY2LjcyNjIzMDQ4MzY5OTIsIDQ1Ljk2NTU3MzA5NTU4OF0sIFstNjYuNzI2MTU4NjE4NDc2NCwgNDUuOTY1MTYwOTgzMTk1OV0sIFstNjYuNzI3MTkxNjgxMDUzMiwgNDUuOTYxNzk1MjgzOTA1Ml0sIFstNjYuNzI0NjQwNDY1NjQ2MywgNDUuOTYxNTg5MjE0MDQwN10sIFstNjYuNzIzMTIyMzEyODE2MSwgNDUuOTYxNTcwNDgwMzc4N10sIFstNjYuNzIxNjEzMTQzMTM4OCwgNDUuOTYxNzAxNjE1ODhdLCBbLTY2LjcxOTU0NzAxNzk4NTMsIDQ1Ljk2MjA4MjUzMTUyODRdLCBbLTY2LjcxNzY0MjU4OTU4MywgNDUuOTYyMjMyMzk5MjYyNF0sIFstNjYuNzE3Njk2NDg4NSwgNDUuOTYyNjA3MDY2ODIzNl0sIFstNjYuNzE3MjY1Mjk3MTYzNywgNDUuOTY0MjkzMDM5NDk0MV0sIFstNjYuNzE2MzIyMDY2MTE1MywgNDUuOTY2ODcxODUzOTc5OF0sIFstNjYuNzE1NzU2MTI3NDg2MywgNDUuOTY4MDAxOTk4NzY0NV0sIFstNjYuNzIwNzk1Njc2MjMwMywgNDUuOTY3NzY0NzMyNzEwOV0sIFstNjYuNzI1MDE3NzU4MDY1NiwgNDUuOTY3OTM5NTYwNDI3OV0sIFstNjYuNzI4MTUyODc4NDA3MiwgNDUuOTY4MjE0Mjg4NTgyNl0sIFstNjYuNzMxMzY4ODQ3MTI0MywgNDUuOTY3ODk1ODUzNTUwNF0sIFstNjYuNzMxODYyOTIwNTMwNiwgNDUuOTY1MjczMzc3Nzg4N11dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogMjYsICJOZWlnaGJvdXJoIjogIk1vbnRlaXRoIC8gVGFsaXNtYW4iLCAiT0JKRUNUSUQiOiAyNiwgIlNoYXBlX0FyZWEiOiA1OTM1NDcuNTEzOTQsICJTaGFwZV9MZW5nIjogMzg1MS4zMjAzMTQzMiwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmVkOTc2IiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni43MTc2NDI1ODk1ODMsIDQ1Ljk2MjIzMjM5OTI2MjRdLCBbLTY2LjcxMjE0NDkwMDA0NDIsIDQ1Ljk2MzAzMTY4Njk5NjZdLCBbLTY2LjcwOTgwOTI4MDMwNTUsIDQ1Ljk2NDA0OTUxMzI3ODddLCBbLTY2LjcwOTA1NDY5NTQ2NjgsIDQ1Ljk2NDE2MTkxMDEyNjVdLCBbLTY2LjcwNzkxMzgzNTA1NiwgNDUuOTY0MTE4MjAwMjY4M10sIFstNjYuNzA1NTY5MjMyMTY0NCwgNDUuOTYzNTA2MjU4NjMyOV0sIFstNjYuNzAzNzQ1NjUyMTM3NywgNDUuOTYzMzE4OTI4MjA5NV0sIFstNjYuNzAyOTgyMDg0MTQ2MiwgNDUuOTYzNzE4NTY1NjgwM10sIFstNjYuNzAxOTY2OTg3ODc1MSwgNDUuOTY1MDExMTIzMzg0MV0sIFstNjYuNzAxNDQ1OTY1MDEwMywgNDUuOTY2MjQ3NDU0NzA3NF0sIFstNjYuNzAxMjg0MjY4MjU5MiwgNDUuOTY3MzIxNDE3MDk3OV0sIFstNjYuNzAyMzYyMjQ2NjAwMSwgNDUuOTY3MjY1MjIxOTA3N10sIFstNjYuNzAyNTc3ODQyMjY4MywgNDUuOTY3MzkwMTAwMDMwOF0sIFstNjYuNzAzMjA2NjYyOTY3MiwgNDUuOTY3MzU4ODgwNTI2NF0sIFstNjYuNzAzNzI3Njg1ODMyLCA0NS45Njc0OTAwMDIzMjY2XSwgWy02Ni43MDY2MjAyNjEwNDY4LCA0NS45Njc1NDYxOTcyODg4XSwgWy02Ni43MDc2NzEyODk5MjkzLCA0NS45Njc3NTg0ODg4NTM3XSwgWy02Ni43MDkwMDk3Nzk3MDI2LCA0NS45Njc4MzM0MTUwOTQxXSwgWy02Ni43MTAwNjk3OTE3Mzc5LCA0NS45Njc4NzcxMjIwMjA5XSwgWy02Ni43MTExODM3MDI2OTAyLCA0NS45Njc3ODM0NjQyNzg0XSwgWy02Ni43MTQ2OTYxMTU0NTExLCA0NS45NjgwMjA3MzAyNTE4XSwgWy02Ni43MTU3NTYxMjc0ODYzLCA0NS45NjgwMDE5OTg3NjQ1XSwgWy02Ni43MTYzMjIwNjYxMTUzLCA0NS45NjY4NzE4NTM5Nzk4XSwgWy02Ni43MTcyNjUyOTcxNjM3LCA0NS45NjQyOTMwMzk0OTQxXSwgWy02Ni43MTc2OTY0ODg1LCA0NS45NjI2MDcwNjY4MjM2XSwgWy02Ni43MTc2NDI1ODk1ODMsIDQ1Ljk2MjIzMjM5OTI2MjRdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDI3LCAiTmVpZ2hib3VyaCI6ICJHYXJkZW4gQ3JlZWsiLCAiT0JKRUNUSUQiOiAyNywgIlNoYXBlX0FyZWEiOiA1NjU2NTUuNTQxNDg0LCAiU2hhcGVfTGVuZyI6IDM0NDIuNDY5NjcxNjUsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlZDk3NiIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjk4ODQ5ODMzODM5MiwgNDUuOTU2MjY4NTk5NDY1XSwgWy02Ni43MDA0NzU3ODQ1MDM1LCA0NS45NTY3NjE5NjQzMjU0XSwgWy02Ni43MDE4NDEyMjM3MzUzLCA0NS45NTc1NDI1OTU5NTM1XSwgWy02Ni43MDE4MTQyNzQyNzY4LCA0NS45NTg4NDc3ODc0NzA0XSwgWy02Ni43MDExNjc0ODcyNzIyLCA0NS45NjAzMzQwNDQ2NzhdLCBbLTY2LjcwMTE2NzQ4NzI3MjIsIDQ1Ljk2MDgyMTEyODcwMjRdLCBbLTY2LjcwMTY1MjU3NzUyNTcsIDQ1Ljk2MTM3Njg5ODgzMzJdLCBbLTY2LjcwMjg5MjI1MjYxNzcsIDQ1Ljk2MTE2NDU4MjgxMjFdLCBbLTY2LjcwMzUzMDA1NjQ2OTUsIDQ1Ljk2MDc3MTE3MTU2MzddLCBbLTY2LjcwNzA1MTQ1MjM4MzIsIDQ1Ljk1NzMyNDAyMDIwNjJdLCBbLTY2LjcwODQzNDg1NzkyMDgsIDQ1Ljk1NTQ4Nzk0OTg4OTNdLCBbLTY2LjcwOTAwMDc5NjU0OTgsIDQ1Ljk1NDI1MTM3ODQ1NTRdLCBbLTY2LjcwOTMyNDE5MDA1MiwgNDUuOTUyOTc3MzA2MzAwMl0sIFstNjYuNzA5Mzk2MDU1Mjc0OCwgNDUuOTUxNjc4MjIyMTgwNl0sIFstNjYuNzA5MTYyNDkzMzAwOSwgNDUuOTUwMTM1NTIwMjM4OF0sIFstNjYuNzA4NjQxNDcwNDM2MSwgNDUuOTUwMDY2ODE1OTE0OF0sIFstNjYuNzA1MzUzNjM2NDk2MiwgNDUuOTUwMzg1MzUzNDI2N10sIFstNjYuNzAxMTY3NDg3MjcyMiwgNDUuOTUwNTk3NzEwNzUwOV0sIFstNjYuNzAwMTM0NDI0Njk1NSwgNDUuOTUwODAzODIxNDkzNF0sIFstNjYuNjk5MTczMjI3MzQxNSwgNDUuOTUxMTUzNTgzNDIzN10sIFstNjYuNjk4NDkwNTA3NzI1NiwgNDUuOTUyNDMzOTQzMDg5NF0sIFstNjYuNjk3Mjc3NzgyMDkyLCA0NS45NTU4NTY0MTc4NTk0XSwgWy02Ni42OTgwNTkzMTYzODkyLCA0NS45NTYyMDYxNDc5MDM2XSwgWy02Ni42OTg4NDk4MzM4MzkyLCA0NS45NTYyNjg1OTk0NjVdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDI4LCAiTmVpZ2hib3VyaCI6ICJIaWdocG9pbnQgUmlkZ2UiLCAiT0JKRUNUSUQiOiAyOCwgIlNoYXBlX0FyZWEiOiA3MjQyNDcuODk3MjcsICJTaGFwZV9MZW5nIjogMzY2OC43MTMxMzE2MSwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmVkOTc2IiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni43MTEwOTM4NzExNjE4LCA0NS45MzQyMDYzMzAyODgyXSwgWy02Ni43MDg3MTMzMzU2NTg4LCA0NS45MzUwNDM1MDc1MzQ1XSwgWy02Ni43MDc1OTA0NDE1NTM3LCA0NS45MzU1NzQ1NDYyNTE3XSwgWy02Ni43MDY3NjM5OTE0OTIzLCA0NS45MzYxMjQzMjIxNTQyXSwgWy02Ni43MDU2OTQ5OTYzMDQyLCA0NS45Mzc0MDUwMjg5NzFdLCBbLTY2LjcwNTE5MTkzOTc0NTEsIDQ1LjkzODg1NDM3ODU2NzZdLCBbLTY2LjcwOTEwODU5NDM4MzgsIDQ1LjkzOTgzNTE2NjkzMTNdLCBbLTY2LjcxMTA5Mzg3MTE2MTgsIDQ1LjkzNDIwNjMzMDI4ODJdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDI5LCAiTmVpZ2hib3VyaCI6ICJHcmVlbndvb2QgTWluaWhvbWUgUGFyayIsICJPQkpFQ1RJRCI6IDI5LCAiU2hhcGVfQXJlYSI6IDE1MjUzOS40ODc5NjUsICJTaGFwZV9MZW5nIjogMTY5OS42NDcxNjEyMiwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmVkOTc2IiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni43MDM4NzE0MTYyNzc0LCA0NS45NjMyODc3MDY0MTA2XSwgWy02Ni43MDI5ODIwODQxNDYyLCA0NS45NjI2MzIwNDQ1NzA5XSwgWy02Ni43MDE3MTU0NTk1OTU1LCA0NS45NjE5MjY0MTg4NzQ1XSwgWy02Ni43MDAzMTQwODc3NTIzLCA0NS45NjEzNTgxNjUwOTk0XSwgWy02Ni42OTkwOTIzNzg5NjU5LCA0NS45NjEwMDg0Njc1NzE3XSwgWy02Ni42OTcwMjYyNTM4MTI0LCA0NS45NjA2NDYyNzg1MTk3XSwgWy02Ni42OTQ4OTcyNDY1ODkxLCA0NS45NjA1MDI2NTExNzFdLCBbLTY2LjY4ODg3ODUzNDE4NTUsIDQ1Ljk1OTc3MjAxOTMyODldLCBbLTY2LjY4NzY4Mzc3NDg1NzYsIDQ1Ljk2MDAxNTU2NDM0NjhdLCBbLTY2LjY4NjY4NjY0NDg5MjIsIDQ1Ljk2MDUzMzg3NDUzOTRdLCBbLTY2LjY4NTQxMTAzNzE4ODgsIDQ1Ljk2MDU1ODg1MzIyMTRdLCBbLTY2LjY4NDY4MzQwMTgwODYsIDQ1Ljk2MDIxNTM5NTM1NjhdLCBbLTY2LjY4MzgyMTAxOTEzNTksIDQ1Ljk2MDEwMjk5MDUwMjRdLCBbLTY2LjY3ODAyNjg4NTU1MzMsIDQ1Ljk2MDUxNTE0MDUyMDVdLCBbLTY2LjY3Njk0ODkwNzIxMjQsIDQ1Ljk2MDc4OTkwNTQ5Nl0sIFstNjYuNjc2MTY3MzcyOTE1MiwgNDUuOTYxMTI3MTE1MTk0NV0sIFstNjYuNjc1MzMxOTM5NzAxLCA0NS45NjE2NzY2Mzc3MTMyXSwgWy02Ni42NzQ3OTI5NTA1MzA1LCA0NS45NjIxOTQ5MzIzNjY5XSwgWy02Ni42NzYzMjAwODY1MTM1LCA0NS45NjI2NTcwMjIzMDddLCBbLTY2LjY3OTE2Nzc0NTk2NDIsIDQ1Ljk2Mjg4MTgyMTQyNDhdLCBbLTY2LjY4NzcwMTc0MTE2MzMsIDQ1Ljk2Mjc3NTY2NjM5OTVdLCBbLTY2LjY5MjMwMTExNTQxOCwgNDUuOTYyOTg3OTc2MjQ2N10sIFstNjYuNjk3MDA4Mjg3NTA2OCwgNDUuOTYzNDM3NTcwODg0NV0sIFstNjYuNjk4MjI5OTk2MjkzMiwgNDUuOTYzNDUwMDU5NTcyM10sIFstNjYuNjk5NzM5MTY1OTcwNSwgNDUuOTYzMzAwMTk1MTMyM10sIFstNjYuNzAxMzkyMDY2MDkzMywgNDUuOTYzNjc0ODU1NDcyM10sIFstNjYuNzAyNjQwNzI0MzM4MiwgNDUuOTY0MjM2ODQxMjMxN10sIFstNjYuNzAzMDcxOTE1Njc0NiwgNDUuOTYzNjQzNjMzODc0MV0sIFstNjYuNzAzODcxNDE2Mjc3NCwgNDUuOTYzMjg3NzA2NDEwNl1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogMzAsICJOZWlnaGJvdXJoIjogIkdvbGYgQ2x1YiIsICJPQkpFQ1RJRCI6IDMwLCAiU2hhcGVfQXJlYSI6IDU5NzU3NC42OTMwMSwgIlNoYXBlX0xlbmciOiA0ODE0Ljg1OTU5NTcxLCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjY4NzY1NjgyNTM5OTEsIDQ1Ljk2MDAyODA1MzgwNjFdLCBbLTY2LjY4ODE2ODg2NTExMSwgNDUuOTU5Mzc4NTk4MTkyNV0sIFstNjYuNjg5NjMzMTE5MDI0MSwgNDUuOTU2NTM3MTQwMzc2OF0sIFstNjYuNjkwNTMxNDM0MzA4MywgNDUuOTU1Mzk0MjcxMjAxM10sIFstNjYuNjkxMDYxNDQwMzI1OSwgNDUuOTU1MDY5NTE3MTg5OF0sIFstNjYuNjkxODUxOTU3Nzc1OSwgNDUuOTU0Nzk0NzIzODQ3NV0sIFstNjYuNjkyNDgwNzc4NDc0OCwgNDUuOTU1MDAwODE4OTgyXSwgWy02Ni42OTMxNDU1MzE3ODUsIDQ1Ljk1NDg4MjE1ODI0MDZdLCBbLTY2LjY5MzUyMjgyNDIwNDQsIDQ1Ljk1NDU1NzQwMTIyODFdLCBbLTY2LjY5MzcxMTQ3MDQxNCwgNDUuOTU0MDE0MDUzNTA5MV0sIFstNjYuNjkzNjM5NjA1MTkxMywgNDUuOTUzMzU4MjgxOTI2Ml0sIFstNjYuNjkzMTAwNjE2MDIwOCwgNDUuOTUyODIxMTY3OTkyXSwgWy02Ni42OTE2OTkyNDQxNzc2LCA0NS45NTIyNTkwNjY0NDAxXSwgWy02Ni42OTAxODEwOTEzNDc1LCA0NS45NTE5MDMwNjU4NDE5XSwgWy02Ni42ODgwNDMxMDA5NzEyLCA0NS45NTE3OTY4ODk3ODIyXSwgWy02Ni42ODc1ODQ5NjAxNzYzLCA0NS45NTIxMjc5MDg1OTFdLCBbLTY2LjY4NjU3ODg0NzA1ODEsIDQ1Ljk1MzAzOTc2MTUwMDRdLCBbLTY2LjY4NTkzMjA2MDA1MzYsIDQ1Ljk1MzgzOTE4MTg0NTddLCBbLTY2LjY4NTQyMDAyMDM0MTYsIDQ1Ljk1NDY5NDc5ODY1NzldLCBbLTY2LjY4NDk4ODgyOTAwNTIsIDQ1Ljk1NTgxMjcwMTQ0ODddLCBbLTY2LjY4NDcxOTMzNDQyLCA0NS45NTcwMDU1MjI1NzM3XSwgWy02Ni42ODQ3MDEzNjgxMTQzLCA0NS45NTgyMDQ1NjI5NTczXSwgWy02Ni42ODQ5MzQ5MzAwODgyLCA0NS45NTkzOTczMzI1OTU3XSwgWy02Ni42ODU0MTEwMzcxODg4LCA0NS45NjA1NTg4NTMyMjE0XSwgWy02Ni42ODY2ODY2NDQ4OTIyLCA0NS45NjA1MzM4NzQ1Mzk0XSwgWy02Ni42ODc2NTY4MjUzOTkxLCA0NS45NjAwMjgwNTM4MDYxXV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiAzMSwgIk5laWdoYm91cmgiOiAiS2VsbHkncyBDb3VydCBNaW5paG9tZSBQYXJrIiwgIk9CSkVDVElEIjogMzEsICJTaGFwZV9BcmVhIjogMzc1NjYwLjIwNzMzNSwgIlNoYXBlX0xlbmciOiAyNzEzLjA5MjcwMzUzLCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjY3MzY4ODAyMjczMSwgNDUuOTY0MjExODY0MjA3OV0sIFstNjYuNjc3ODc0MTcxOTU1LCA0NS45NjQ4ODYyMzk4OTc5XSwgWy02Ni42NzgzNzcyMjg1MTQxLCA0NS45NjUxMDQ3ODU4MTRdLCBbLTY2LjY3OTMyMDQ1OTU2MjQsIDQ1Ljk2NTEyMzUxODI4MDldLCBbLTY2LjY4MzI5OTk5NjI3MTEsIDQ1Ljk2NTcyMjk1Mzg3OTVdLCBbLTY2LjY4MzQxNjc3NzI1OCwgNDUuOTY1NjQxNzgwNjg4Nl0sIFstNjYuNjg0NjQ3NDY5MTk3MywgNDUuOTY1OTA0MDMyMTA3Nl0sIFstNjYuNjg1MDMzNzQ0NzY5NSwgNDUuOTY1OTIyNzY0MzA0M10sIFstNjYuNjg1MjQwMzU3Mjg0OCwgNDUuOTY1ODIyODU5MTgyXSwgWy02Ni42ODUzMzkxNzE5NjYsIDQ1Ljk2NjAxMDE4MTEzODVdLCBbLTY2LjY4NjcwNDYxMTE5NzksIDQ1Ljk2NjA0MTQwMTQwM10sIFstNjYuNjg3MzQyNDE1MDQ5NiwgNDUuOTY2MzY2MDkxMTEwN10sIFstNjYuNjg5NTUyMjcwNjQ4NiwgNDUuOTY2NzE1NzU0ODIxNV0sIFstNjYuNjk0NDY2MDU1MjUyNywgNDUuOTY2ODQ2ODc4MTQ0XSwgWy02Ni43MDA4NjIwNjAwNzU2LCA0NS45NjczNzEzNjgzMzAzXSwgWy02Ni43MDEyODQyNjgyNTkyLCA0NS45NjczMjE0MTcwOTc5XSwgWy02Ni43MDE0MDEwNDkyNDYxLCA0NS45NjY0MjIyODcyMTMxXSwgWy02Ni43MDE4MTQyNzQyNzY4LCA0NS45NjUyOTIxMTAxOTg2XSwgWy02Ni43MDI2NDA3MjQzMzgyLCA0NS45NjQyMzY4NDEyMzE3XSwgWy02Ni43MDEzOTIwNjYwOTMzLCA0NS45NjM2NzQ4NTU0NzIzXSwgWy02Ni42OTk3MzkxNjU5NzA1LCA0NS45NjMzMDAxOTUxMzIzXSwgWy02Ni42OTgyMjk5OTYyOTMyLCA0NS45NjM0NTAwNTk1NzIzXSwgWy02Ni42OTcwMDgyODc1MDY4LCA0NS45NjM0Mzc1NzA4ODQ1XSwgWy02Ni42OTIzMDExMTU0MTgsIDQ1Ljk2Mjk4Nzk3NjI0NjddLCBbLTY2LjY4NzcwMTc0MTE2MzMsIDQ1Ljk2Mjc3NTY2NjM5OTVdLCBbLTY2LjY3OTE2Nzc0NTk2NDIsIDQ1Ljk2Mjg4MTgyMTQyNDhdLCBbLTY2LjY3NjMyMDA4NjUxMzUsIDQ1Ljk2MjY1NzAyMjMwN10sIFstNjYuNjc0NzkyOTUwNTMwNSwgNDUuOTYyMjAxMTc2ODUxMl0sIFstNjYuNjczNjg4MDIyNzMxLCA0NS45NjQyMTE4NjQyMDc5XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiAzMiwgIk5laWdoYm91cmgiOiAiV29vZHN0b2NrIFJvYWQiLCAiT0JKRUNUSUQiOiAzMiwgIlNoYXBlX0FyZWEiOiA3NTgzMzYuODM4Nzg3LCAiU2hhcGVfTGVuZyI6IDUwNDguNDM3NDkwMDMsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlYjI0YyIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjY5NTQ2Nzg5MjcxMiwgNDUuOTYxNjM5MTcwNDQxOV0sIFstNjYuNjY4NTg1NTkxOTE3MiwgNDUuOTYwNzI3NDU5MDMwM10sIFstNjYuNjY3MDc2NDIyMjM5OSwgNDUuOTU5OTg0MzQwNjg2NF0sIFstNjYuNjYzODk2Mzg2MTM0MSwgNDUuOTU5MTQxMjk1MjA0MV0sIFstNjYuNjYxNjE0NjY1MzEyNSwgNDUuOTU4OTE2NDgwOTA5MV0sIFstNjYuNjU5MTQ0Mjk4MjgxMSwgNDUuOTYyNDM4NDY2NzM0Nl0sIFstNjYuNjU4ODExOTIxNjI2LCA0NS45NjMyNTY0ODQ1OTQyXSwgWy02Ni42NTg3MzEwNzMyNTA0LCA0NS45NjQwOTk0Njc0NjE0XSwgWy02Ni42NjAwNTE1OTY3MTgxLCA0NS45NjQwODA3MzQ2NDgyXSwgWy02Ni42NjE4MzkyNDQxMzM1LCA0NS45NjM3ODcyNTMwODAzXSwgWy02Ni42Njc4MTMwNDA3NzI5LCA0NS45NjIyNDQ4ODgyMjE5XSwgWy02Ni42Njk1NDY3ODkyNzEyLCA0NS45NjE2MzkxNzA0NDE5XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiAzMywgIk5laWdoYm91cmgiOiAiU3Vuc2hpbmUgR2FyZGVucyIsICJPQkpFQ1RJRCI6IDMzLCAiU2hhcGVfQXJlYSI6IDI4NjUzOS4xOTYyNzIsICJTaGFwZV9MZW5nIjogMjIzMS4wMzIwMDMxMywgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmVkOTc2IiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni42MzIxMjI5NzQ1MzQ4LCA0NS45NTQ5MDA4OTQxNjRdLCBbLTY2LjYzMjU1NDE2NTg3MTIsIDQ1Ljk1NjU0OTYzMDYyMDFdLCBbLTY2LjYzMzcwNDAwOTQzNDksIDQ1Ljk1ODU2Njc2Nzk3MDVdLCBbLTY2LjYzNDc1NTAzODMxNzMsIDQ1Ljk1OTU2NTk0MTkzOTJdLCBbLTY2LjYzNjI2NDIwNzk5NDYsIDQ1Ljk2MTM4MzE0MzQwOThdLCBbLTY2LjYzNzg3MjE5MjM1MzIsIDQ1Ljk2Mjc0NDQ0NDI5NDVdLCBbLTY2LjY0MDQyMzQwNzc2MDEsIDQ1Ljk2NDM4MDQ1ODldLCBbLTY2LjY0MjM1NDc4NTYyMDksIDQ1Ljk2NTM5ODI2MDQwMjFdLCBbLTY2LjY0NDUxOTcyNTQ1NTcsIDQ1Ljk2NjEwMzg0MTg3OTJdLCBbLTY2LjY0NzQwMzMxNzUxNzcsIDQ1Ljk2NjUzNDY3OTI0NjhdLCBbLTY2LjY1MDQyMTY1Njg3MjMsIDQ1Ljk2NjQwOTc5OTE5NTNdLCBbLTY2LjY1MzU5MjcwOTgyNTMsIDQ1Ljk2NjEwMzg0MTg3OTJdLCBbLTY2LjY1NjQwNDQzNjY2NDYsIDQ1Ljk2NjQ3ODQ4MzI1ODVdLCBbLTY2LjY1NzczMzk0MzI4NTEsIDQ1Ljk2NjUwMzQ1OTI2MDRdLCBbLTY2LjY1NjI1MTcyMzA2NjMsIDQ1Ljk2NTkyOTAwODM2ODRdLCBbLTY2LjY1NDY3MDY4ODE2NjIsIDQ1Ljk2NTUwNDQxMDQwMjJdLCBbLTY2LjY1MzAxNzc4ODA0MzQsIDQ1Ljk2NTI0MjE1NzA5MTNdLCBbLTY2LjY1MjAwMjY5MTc3MjQsIDQ1Ljk2NTI3OTYyMTkyNl0sIFstNjYuNjUxMTg1MjI0ODYzOCwgNDUuOTY1MDYxMDc2Njk5N10sIFstNjYuNjUwNDg0NTM4OTQyMiwgNDUuOTY0NTU1Mjk3Mjk4MV0sIFstNjYuNjUwNDg0NTM4OTQyMiwgNDUuOTY0MjkzMDM5NDk0MV0sIFstNjYuNjUwOTk2NTc4NjU0MiwgNDUuOTYzNzY4NTIwMTYxNV0sIFstNjYuNjUxOTM5ODA5NzAyNSwgNDUuOTYzNDYyNTQ4MjU3NF0sIFstNjYuNjMyMTIyOTc0NTM0OCwgNDUuOTU0OTAwODk0MTY0XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiAzNCwgIk5laWdoYm91cmgiOiAiRG93bnRvd24iLCAiT0JKRUNUSUQiOiAzNCwgIlNoYXBlX0FyZWEiOiA4MTkyMzYuNzA1Njk3LCAiU2hhcGVfTGVuZyI6IDUzMDAuNzQwMzExMjIsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2YwM2IyMCIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjM0MTM1MjAwNzcxMiwgNDUuOTU1NzY4OTg1MDAzNF0sIFstNjYuNjUxOTM5ODA5NzAyNSwgNDUuOTYzNDYyNTQ4MjU3NF0sIFstNjYuNjU0MTU4NjQ4NDU0MywgNDUuOTYzNTgxMTkwNjI0OV0sIFstNjYuNjU2ODM1NjI4MDAwOSwgNDUuOTYzOTk5NTU5MDUwOV0sIFstNjYuNjU4ODI5ODg3OTMxNywgNDUuOTY0MTU1NjY1ODYzMV0sIFstNjYuNjU4NzMxMDczMjUwNCwgNDUuOTY0MDk5NDY3NDYxNF0sIFstNjYuNjU4Nzc1OTg5MDE0NiwgNDUuOTYzNDI1MDgyMTkzOF0sIFstNjYuNjU5MTQ0Mjk4MjgxMSwgNDUuOTYyNDM4NDY2NzM0Nl0sIFstNjYuNjYwNzUyMjgyNjM5NywgNDUuOTU5OTk2ODMwMTUyN10sIFstNjYuNjYxNjc3NTQ3MzgyMywgNDUuOTU4OTE2NDgwOTA5MV0sIFstNjYuNjYxMzA5MjM4MTE1OCwgNDUuOTU4MDg1OTA5MDc2MV0sIFstNjYuNjYwNDAxOTM5Njc4OSwgNDUuOTU3NDczOTAwODExNV0sIFstNjYuNjU2OTYxMzkyMTQwNywgNDUuOTU2ODc0Mzc1OTU3Nl0sIFstNjYuNjU1MjgxNTQyNTU5NCwgNDUuOTU2MzE4NTYwNjYzNF0sIFstNjYuNjUzMjY5MzE2MzIzLCA0NS45NTU1MDY2ODU2MDhdLCBbLTY2LjY1MDQ2NjU3MjYzNjUsIDQ1Ljk1NDE3NjQzMzg0NTNdLCBbLTY2LjY0OTEwMTEzMzQwNDcsIDQ1Ljk1MzY3NjgwMDUyMTNdLCBbLTY2LjY0NzMwNDUwMjgzNjQsIDQ1Ljk1MzE5NTg5OTE5MjddLCBbLTY2LjY0MjkxMTc0MTA5NzEsIDQ1Ljk1MTQ3MjExNDY4OThdLCBbLTY2LjY0MTg3ODY3ODUyMDMsIDQ1Ljk1MDc3ODgzODQxMzldLCBbLTY2LjY0MDcwMTg4NTQ5ODEsIDQ1Ljk1MDQ4NTI4NjM4NjVdLCBbLTY2LjYzOTQ1MzIyNzI1MzIsIDQ1Ljk1MDUyOTAwNjk5OTddLCBbLTY2LjYzODQyOTE0NzgyOTMsIDQ1Ljk1MTIzNDc3Nzg0MThdLCBbLTY2LjYzNzU5MzcxNDYxNTEsIDQ1Ljk1MjA1Mjk2MTEwOTNdLCBbLTY2LjYzNjUzMzcwMjU3OTgsIDQ1Ljk1MzQ4OTQzNjg2MzVdLCBbLTY2LjYzNDEzNTIwMDc3MTIsIDQ1Ljk1NTc2ODk4NTAwMzRdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDM1LCAiTmVpZ2hib3VyaCI6ICJQbGF0IiwgIk9CSkVDVElEIjogMzUsICJTaGFwZV9BcmVhIjogMTU5NjQwMS40MjUzNiwgIlNoYXBlX0xlbmciOiA1NTUxLjM4MTAwMzAxLCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNiZDAwMjYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjYyODk2MDkwNDczNDcsIDQ1LjkzOTUxNjU2ODc5MjFdLCBbLTY2LjYyODk4Nzg1NDE5MzIsIDQ1Ljk0MDI1MzcxNDY0NTddLCBbLTY2LjYyOTEzMTU4NDYzODcsIDQ1Ljk0MDM5NzM5NDQ3NThdLCBbLTY2LjYyOTYwNzY5MTczOTMsIDQ1Ljk0MDUwMzU5MjM3MTldLCBbLTY2LjYzMDA5Mjc4MTk5MjcsIDQ1Ljk0MjAyNzgyMjExNTZdLCBbLTY2LjYzMDc2NjUxODQ1NTgsIDQ1Ljk0MzA5NjAwNzMzMV0sIFstNjYuNjMxMjMzNjQyNDAzNSwgNDUuOTQ0NzU3NTg3ODY5N10sIFstNjYuNjMxNjU1ODUwNTg3MSwgNDUuOTQ3NjU1ODY0Nzk2Nl0sIFstNjYuNjMxNzYzNjQ4NDIxMiwgNDUuOTQ4MDI0Mzg0ODM5OV0sIFstNjYuNjMxODM1NTEzNjQzOSwgNDUuOTQ4MTExODI5OTE0Ml0sIFstNjYuNjMxOTYxMjc3NzgzNywgNDUuOTQ3OTY4MTcwMDc2NF0sIFstNjYuNjMyMDk2MDI1MDc2MywgNDUuOTQ4Mzg2NjU2MzkyN10sIFstNjYuNjMyMTA1MDA4MjI5MSwgNDUuOTUwNjE2NDQ4MTIyOF0sIFstNjYuNjMxOTA3Mzc4ODY2NiwgNDUuOTUxNTE1ODM0NTI0Nl0sIFstNjYuNjMxOTcwMjYwOTM2NSwgNDUuOTU0MjA3NjYwNzc4NV0sIFstNjYuNjMyMTIyOTc0NTM0OCwgNDUuOTU0OTAwODk0MTY0XSwgWy02Ni42MzQxMzUyMDA3NzEyLCA0NS45NTU3Njg5ODUwMDM0XSwgWy02Ni42MzY4NTcwOTYwODIxLCA0NS45NTMxNDU5MzUxNzldLCBbLTY2LjYzNzg5OTE0MTgxMTcsIDQ1Ljk1MTcxNTY5NjE4NzVdLCBbLTY2LjYzODgxNTQyMzQwMTUsIDQ1Ljk1MDk0MTIyODIyOTJdLCBbLTY2LjYzOTYxNDkyNDAwNDQsIDQ1Ljk1MDQ5Nzc3Nzk5MzhdLCBbLTY2LjYzOTU3MDAwODI0MDIsIDQ1Ljk1MDMwNDE1Nzc2NDFdLCBbLTY2LjYzOTMxODQ3OTk2MDYsIDQ1Ljk0OTgzNTcxODkyN10sIFstNjYuNjM4MDc4ODA0ODY4NSwgNDUuOTQ4ODYxMzUzNDY0MV0sIFstNjYuNjM2NzEzMzY1NjM2NywgNDUuOTQ3NTQ5NjgwNjAwNl0sIFstNjYuNjM0OTYxNjUwODMyNiwgNDUuOTQ1MjU3MzAxNTk5XSwgWy02Ni42MzQwNjMzMzU1NDg1LCA0NS45NDQyOTUzNDg2NTk3XSwgWy02Ni42MzMzNzE2MzI3Nzk3LCA0NS45NDMyNDU5MjY0MTZdLCBbLTY2LjYzMjY2MTk2MzcwNTMsIDQ1Ljk0MTQxNTYzNjUxNl0sIFstNjYuNjMyMjEyODA2MDYzMiwgNDUuOTQwNzg0NzAzNDY3OF0sIFstNjYuNjMxNzAwNzY2MzUxMywgNDUuOTQwMzQxMTcxOTc3OV0sIFstNjYuNjMwOTAxMjY1NzQ4NCwgNDUuOTM5OTEwMTMwOTMzM10sIFstNjYuNjI5OTY3MDE3ODUyOSwgNDUuOTM5NjI5MDE1NDAzMl0sIFstNjYuNjI4OTYwOTA0NzM0NywgNDUuOTM5NTE2NTY4NzkyMV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogMzYsICJOZWlnaGJvdXJoIjogIldhdGVybG9vIFJvdyIsICJPQkpFQ1RJRCI6IDM2LCAiU2hhcGVfQXJlYSI6IDU4MDYzNS45MDI4MzQsICJTaGFwZV9MZW5nIjogNDI2MC40ODI0MTc2LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjY0NjQzMzEzNzAxMDgsIDQ1Ljk0MjQxNTExOTcxODFdLCBbLTY2LjY0NTc2ODM4MzcwMDYsIDQ1Ljk0MjA4NDA0MjkwMzFdLCBbLTY2LjY0NTY3ODU1MjE3MjIsIDQ1Ljk0MTg5NjY0MDA1NjFdLCBbLTY2LjY1MDE0MzE3OTEzNDIsIDQ1LjkzNjYwNTM3MTU5NzhdLCBbLTY2LjY1MDI3NzkyNjQyNjksIDQ1LjkzNjMxNzk5MTkxMjZdLCBbLTY2LjY1MDA5ODI2MzM3LCA0NS45MzYxMzY4MTY5OTc4XSwgWy02Ni42NDk2NjcwNzIwMzM3LCA0NS45MzYyMjQyODA4MjM3XSwgWy02Ni42NDc2NjM4Mjg5NTAxLCA0NS45Mzc0ODYyNDM1Mjc5XSwgWy02Ni42NDQyNzcxODAzMjg5LCA0NS45NDAwNTM4MTE2NTM4XSwgWy02Ni42NDM0NDE3NDcxMTQ3LCA0NS45NDA1NTk4MTQ3MDUxXSwgWy02Ni42NDI0MzU2MzM5OTY1LCA0NS45NDA5NjU4NjMxOTY3XSwgWy02Ni42NDEyMjI5MDgzNjI5LCA0NS45NDEyNDY5NzE5NDg5XSwgWy02Ni42NDAxMTc5ODA1NjM1LCA0NS45NDEzMjgxODA4Nzg2XSwgWy02Ni42Mzg4NjAzMzkxNjU3LCA0NS45NDEyMjgyMzE0MDk3XSwgWy02Ni42Mzc4MDkzMTAyODMzLCA0NS45NDE3OTY2OTE2MTIxXSwgWy02Ni42MzcwMjc3NzU5ODYxLCA0NS45NDI1NDYzMDA1NTA3XSwgWy02Ni42MzYxNDc0MjcwMDc3LCA0NS45NDQ1MjAyMjIyNzAzXSwgWy02Ni42MzU4Nzc5MzI0MjI0LCA0NS45NDY1ODE1MjExOTY1XSwgWy02Ni42Mzc1NzU3NDgzMDk0LCA0NS45NDg0MTE2NDA1NTA0XSwgWy02Ni42MzkzMTg0Nzk5NjA2LCA0NS45NDk4MzU3MTg5MjddLCBbLTY2LjYzOTYxNDkyNDAwNDQsIDQ1Ljk1MDQ5Nzc3Nzk5MzhdLCBbLTY2LjY0MTAwNzMxMjY5NDcsIDQ1Ljk1MDUyOTAwNjk5OTddLCBbLTY2LjY0MjExMjI0MDQ5NDIsIDQ1Ljk1MDg4NTAxNjQyMzldLCBbLTY2LjY0MjU0MzQzMTgzMDYsIDQ1Ljk1MDM4NTM1MzQyNjddLCBbLTY2LjY0NTIyOTM5NDUzMDEsIDQ1Ljk0NzAzMTI0ODk1ODNdLCBbLTY2LjY0NDEwNjUwMDQyNSwgNDUuOTQ2NTg3NzY3NDQwNF0sIFstNjYuNjQ0ODQzMTE4OTU3OSwgNDUuOTQ1NzUwNzY0NDg2Ml0sIFstNjYuNjQ1MDIyNzgyMDE0OCwgNDUuOTQ1Mjg4NTMzNTU3NV0sIFstNjYuNjQ0OTQxOTMzNjM5MiwgNDUuOTQ0NzcwMDgwNzY3OF0sIFstNjYuNjQ0NDQ3ODYwMjMyOSwgNDUuOTQzNzE0NDIwOTQzN10sIFstNjYuNjQ0NTI4NzA4NjA4NSwgNDUuOTQzNDgzMjk3NDcxNV0sIFstNjYuNjQ2NDMzMTM3MDEwOCwgNDUuOTQyNDE1MTE5NzE4MV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogMzcsICJOZWlnaGJvdXJoIjogIlVuaXZlcnNpdHkgT2YgTmV3IEJydW5zd2ljayIsICJPQkpFQ1RJRCI6IDM3LCAiU2hhcGVfQXJlYSI6IDcwNDc2My41NzEzODQsICJTaGFwZV9MZW5nIjogNDQ4MC40NjM4ODI1LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjY0NjQzMzEzNzAxMDgsIDQ1Ljk0MjQxNTExOTcxODFdLCBbLTY2LjY0NDUyODcwODYwODUsIDQ1Ljk0MzQ4MzI5NzQ3MTVdLCBbLTY2LjY0NDQ0Nzg2MDIzMjksIDQ1Ljk0MzcxNDQyMDk0MzddLCBbLTY2LjY0NDk0MTkzMzYzOTIsIDQ1Ljk0NDc3MDA4MDc2NzhdLCBbLTY2LjY0NTAyMjc4MjAxNDgsIDQ1Ljk0NTI4ODUzMzU1NzVdLCBbLTY2LjY0NDg0MzExODk1NzksIDQ1Ljk0NTc1MDc2NDQ4NjJdLCBbLTY2LjY0NDEwNjUwMDQyNSwgNDUuOTQ2NTg3NzY3NDQwNF0sIFstNjYuNjQ1MjI5Mzk0NTMwMSwgNDUuOTQ3MDMxMjQ4OTU4M10sIFstNjYuNjQ4NTE3MjI4NDcsIDQ1Ljk0MzI4OTY1MjczOTRdLCBbLTY2LjY0NjQzMzEzNzAxMDgsIDQ1Ljk0MjQxNTExOTcxODFdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDM4LCAiTmVpZ2hib3VyaCI6ICJTYWludCBUaG9tYXMgVW5pdmVyc2l0eSIsICJPQkpFQ1RJRCI6IDM4LCAiU2hhcGVfQXJlYSI6IDg0ODEzLjE1ODUzNzEsICJTaGFwZV9MZW5nIjogMTM0MS41Mzg0ODM1OSwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmVkOTc2IiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni42NDg1MTcyMjg0NywgNDUuOTQzMjg5NjUyNzM5NF0sIFstNjYuNjQ1MjI5Mzk0NTMwMSwgNDUuOTQ3MDMxMjQ4OTU4M10sIFstNjYuNjQyMTEyMjQwNDk0MiwgNDUuOTUwODg1MDE2NDIzOV0sIFstNjYuNjQyOTExNzQxMDk3MSwgNDUuOTUxNDcyMTE0Njg5OF0sIFstNjYuNjQ2MDczODEwODk3MiwgNDUuOTUyNjcxMjc0ODAyM10sIFstNjYuNjUyNjIyNTI5MzE4NCwgNDUuOTQ0OTk0OTUyNDUyOF0sIFstNjYuNjQ4NTE3MjI4NDcsIDQ1Ljk0MzI4OTY1MjczOTRdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDM5LCAiTmVpZ2hib3VyaCI6ICJDb2xsZWdlIEhpbGwiLCAiT0JKRUNUSUQiOiAzOSwgIlNoYXBlX0FyZWEiOiAzNjY3ODcuMDcyMDc5LCAiU2hhcGVfTGVuZyI6IDI3MTMuMjU2ODE0MzgsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlYjI0YyIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjUyNDUxODQ5NDE0NCwgNDUuOTQ0OTE5OTk1MzI1OF0sIFstNjYuNjUyNjIyNTI5MzE4NCwgNDUuOTQ0OTk0OTUyNDUyOF0sIFstNjYuNjQ2MDczODEwODk3MiwgNDUuOTUyNjcxMjc0ODAyM10sIFstNjYuNjQ3MzA0NTAyODM2NCwgNDUuOTUzMTk1ODk5MTkyN10sIFstNjYuNjUwMTM0MTk1OTgxNCwgNDUuOTU0MDM5MDM1MTMwM10sIFstNjYuNjU0ODY4MzE3NTI4NywgNDUuOTU2MTY4Njc2OTMzXSwgWy02Ni42NTY5NjEzOTIxNDA3LCA0NS45NTY4NzQzNzU5NTc2XSwgWy02Ni42NTc3MDY5OTM4MjY1LCA0NS45NTY5ODA1NDIyODk4XSwgWy02Ni42NTg3NDkwMzk1NTYxLCA0NS45NTY0MTg0ODI5MjUxXSwgWy02Ni42NjAyODUxNTg2OTE5LCA0NS45NTYwMDAwNTcyNTE4XSwgWy02Ni42NjU3NjQ4ODE5MjUxLCA0NS45NDk2Nzk1NzE3NjgxXSwgWy02Ni42NjY0NTY1ODQ2OTM4LCA0NS45NDkwNTQ5Nzg3MzM5XSwgWy02Ni42NjY4NTE4NDM0MTg5LCA0NS45NDg0ODY1OTI5NTYxXSwgWy02Ni42NjcxMzAzMjExNTY5LCA0NS45NDc3MTgzMjU5OTMzXSwgWy02Ni42NjcxNTcyNzA2MTU1LCA0NS45NDY5MzEzMDk3NzFdLCBbLTY2LjY2NjkyMzcwODY0MTYsIDQ1Ljk0NjE1Njc3NDk2MDNdLCBbLTY2LjY2NjU2NDM4MjUyOCwgNDUuOTQ1NTc1ODY2NzUwMl0sIFstNjYuNjYyMzQyMzAwNjkyNiwgNDUuOTQzNzgzMTMzMTQxNV0sIFstNjYuNjU3MTMyMDcyMDQ0NywgNDUuOTQxODA5MTg1MTc3NF0sIFstNjYuNjU1NTUxMDM3MTQ0NiwgNDUuOTQyNDA4ODczMDA0MV0sIFstNjYuNjU0MzgzMjI3Mjc1MywgNDUuOTQzMDY0Nzc0MTM3Ml0sIFstNjYuNjUzMjE1NDE3NDA1OSwgNDUuOTQ0MDIwNTAxODk2OV0sIFstNjYuNjUyNDUxODQ5NDE0NCwgNDUuOTQ0OTE5OTk1MzI1OF1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogNDAsICJOZWlnaGJvdXJoIjogIlRoZSBIaWxsIiwgIk9CSkVDVElEIjogNDAsICJTaGFwZV9BcmVhIjogMTYzNzE0OS41NzQwNywgIlNoYXBlX0xlbmciOiA0OTM0LjkwODE2ODE5LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWIyNGMiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjYzMDUzMjk1NjQ4MTksIDQ1LjkzOTc3MjY5Njg1MjJdLCBbLTY2LjYzMTY0Njg2NzQzNDIsIDQ1Ljk0MDMwMzY5MDI4MV0sIFstNjYuNjMyMzU2NTM2NTA4NywgNDUuOTQwOTQwODc1NjgzMV0sIFstNjYuNjMzNjIzMTYxMDU5MywgNDUuOTQzNjc2OTQxNTI3Ml0sIFstNjYuNjM1ODc3OTMyNDIyNCwgNDUuOTQ2NTgxNTIxMTk2NV0sIFstNjYuNjM2MDg0NTQ0OTM3OCwgNDUuOTQ0Nzc2MzI3MjE1OV0sIFstNjYuNjM2NzQ5Mjk4MjQ4LCA0NS45NDI5NzEwNzQ0NTA0XSwgWy02Ni42Mzc2NTY1OTY2ODUsIDQ1Ljk0MTkxNTM4MDM2OTNdLCBbLTY2LjYzODQ4MzA0Njc0NjQsIDQ1Ljk0MTM5Njg5NjAzMzldLCBbLTY2LjYzODg2MDMzOTE2NTcsIDQ1Ljk0MTIyODIzMTQwOTddLCBbLTY2LjYzOTA0MDAwMjIyMjUsIDQ1Ljk0MTI1MzIxODc5MzhdLCBbLTY2LjYzODk3NzEyMDE1MjYsIDQ1Ljk0MTEzNDUyODYxOV0sIFstNjYuNjM4MzU3MjgyNjA2NiwgNDUuOTQwMzcyNDA2NzA2XSwgWy02Ni42MzU3NTIxNjgyODI3LCA0NS45Mzk0OTE1ODA2MjUzXSwgWy02Ni42MzUwODc0MTQ5NzI0LCA0NS45Mzg1ODU3NTE5NzY2XSwgWy02Ni42MzQzMzI4MzAxMzM3LCA0NS45MzY0NDkxODcxNzExXSwgWy02Ni42MzMzMzU3MDAxNjg0LCA0NS45MzUxMTg0NzgwMTQ2XSwgWy02Ni42Mjk5NzYwMDEwMDU4LCA0NS45MzIzMTk1MTEzNTAyXSwgWy02Ni42Mjc5Mjc4NDIxNTgsIDQ1LjkzMDIzODkzNzkwNzJdLCBbLTY2LjYyNzY3NjMxMzg3ODQsIDQ1LjkzMDEwMTQ3OTg1NjFdLCBbLTY2LjYyNzI4MTA1NTE1MzQsIDQ1LjkzMDA3NjQ4NzQ0NjZdLCBbLTY2LjYyNjgwNDk0ODA1MjgsIDQ1LjkzMDM1MTQwMzMzMTldLCBbLTY2LjYyNjg0MDg4MDY2NDIsIDQ1LjkzMDczMjUzNDQ2NDNdLCBbLTY2LjYyNzQwNjgxOTI5MzIsIDQ1LjkzMTM2OTgyOTg1MTFdLCBbLTY2LjYyODE0MzQzNzgyNjIsIDQ1LjkzMTg0NDY3MjYzMzNdLCBbLTY2LjYzMDE0NjY4MDkwOTcsIDQ1LjkzMzczMTUwNzcyNThdLCBbLTY2LjYzMTU3NTAwMjIxMTUsIDQ1LjkzNTE5OTY5NTkyMDRdLCBbLTY2LjYzMTk2MTI3Nzc4MzcsIDQ1LjkzNTg2MTkyOTc4OThdLCBbLTY2LjYzMjAzMzE0MzAwNjQsIDQ1LjkzNjMzNjczNDExMTRdLCBbLTY2LjYzMTY5MTc4MzE5ODQsIDQ1LjkzNzYwNDk0MTUxMjVdLCBbLTY2LjYzMDUzMjk1NjQ4MTksIDQ1LjkzOTc3MjY5Njg1MjJdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDQxLCAiTmVpZ2hib3VyaCI6ICJGb3Jlc3QgSGlsbCIsICJPQkpFQ1RJRCI6IDQxLCAiU2hhcGVfQXJlYSI6IDM5NjA0MC4xNDQ0NDgsICJTaGFwZV9MZW5nIjogNDQyMi4yMDg2NzUyNSwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmVkOTc2IiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni42MzUyMjIxNjIyNjUsIDQ1LjkzODg0MTg4NDMzNjVdLCBbLTY2LjYzNjc1ODI4MTQwMDksIDQ1LjkzODkxMDYwMjU3MzJdLCBbLTY2LjYzNzk4ODk3MzM0MDEsIDQ1LjkzODg0ODEzMTQ1MjRdLCBbLTY2LjYzOTE5MjcxNTgyMDgsIDQ1LjkzODY2Njk2NDgwNDJdLCBbLTY2LjY0MDYzOTAwMzQyODMsIDQ1LjkzODI5ODM4MjU1NDddLCBbLTY2LjY0NzYwMDk0Njg4MDIsIDQ1LjkzNTUzMDgxMzg0MzZdLCBbLTY2LjY1MDQ5MzUyMjA5NSwgNDUuOTMzOTkzOTEwMTcwN10sIFstNjYuNjUwMTUyMTYyMjg3MSwgNDUuOTMzMTI1NDc4Mjg2OF0sIFstNjYuNjQ3OTk2MjA1NjA1MiwgNDUuOTMxNTU3MjY4Mjc3MV0sIFstNjYuNjQwMDI4MTQ5MDM1MSwgNDUuOTI3MjE0NzgyMDkxNV0sIFstNjYuNjM4MDk2NzcxMTc0MiwgNDUuOTI1ODI3NjE0MTQyNV0sIFstNjYuNjM2MDU3NTk1NDc5MywgNDUuOTI0OTAyODE2MjM4NV0sIFstNjYuNjMyNzc4NzQ0NjkyMiwgNDUuOTI3MjU4NTIxMDU3M10sIFstNjYuNjMxMDAwMDgwNDI5NywgNDUuOTI5MzcwNDQ3MjI1XSwgWy02Ni42MzAwNTY4NDkzODEzLCA0NS45Mjk2NTE2MTQ3NjE4XSwgWy02Ni42Mjg4MTcxNzQyODkzLCA0NS45Mjk4NDUzMDcxMjQ3XSwgWy02Ni42Mjc5MTg4NTkwMDUxLCA0NS45MzAyMzI2ODk4MjEzXSwgWy02Ni42Mjk5NzYwMDEwMDU4LCA0NS45MzIzMTk1MTEzNTAyXSwgWy02Ni42MzI2OTc4OTYzMTY2LCA0NS45MzQ0ODc0NzMzMTAyXSwgWy02Ni42MzM0Nzk0MzA2MTM4LCA0NS45MzUyODA5MTM3MDcyXSwgWy02Ni42MzQ1MTI0OTMxOTA2LCA0NS45MzY3OTI3OTIzMjkzXSwgWy02Ni42MzUyMjIxNjIyNjUsIDQ1LjkzODg0MTg4NDMzNjVdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDQyLCAiTmVpZ2hib3VyaCI6ICJTa3lsaW5lIEFjcmVhIiwgIk9CSkVDVElEIjogNDIsICJTaGFwZV9BcmVhIjogMTQ1NzUxMC4wODc2MSwgIlNoYXBlX0xlbmciOiA0ODk0LjY2MDAyMjIsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlZDk3NiIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjM1MjIyMTYyMjY1LCA0NS45Mzg4NDE4ODQzMzY1XSwgWy02Ni42MzU4ODY5MTU1NzUzLCA0NS45Mzk2MDQwMjcyODcxXSwgWy02Ni42MzgzNTcyODI2MDY2LCA0NS45NDAzNzI0MDY3MDZdLCBbLTY2LjYzOTA0MDAwMjIyMjUsIDQ1Ljk0MTI1MzIxODc5MzhdLCBbLTY2LjY0MDczNzgxODEwOTUsIDQ1Ljk0MTI5Njk0NjY4ODldLCBbLTY2LjY0MjQzNTYzMzk5NjUsIDQ1Ljk0MDk2NTg2MzE5NjddLCBbLTY2LjY0Mzk0NDgwMzY3MzgsIDQ1Ljk0MDI3ODcwMjQ2OV0sIFstNjYuNjQ3NjYzODI4OTUwMSwgNDUuOTM3NDg2MjQzNTI3OV0sIFstNjYuNjQ5NzI5OTU0MTAzNSwgNDUuOTM2MTg2Nzk2MzQzN10sIFstNjYuNjUwMTQzMTc5MTM0MiwgNDUuOTM2MTU1NTU5MjU3OF0sIFstNjYuNjUwNTExNDg4NDAwNywgNDUuOTM1MTc0NzA1ODA4Ml0sIFstNjYuNjUwNDkzNTIyMDk1LCA0NS45MzM5OTM5MTAxNzA3XSwgWy02Ni42NDc2MDA5NDY4ODAyLCA0NS45MzU1MzA4MTM4NDM2XSwgWy02Ni42NDA2MzkwMDM0MjgzLCA0NS45MzgyOTgzODI1NTQ3XSwgWy02Ni42MzkxOTI3MTU4MjA4LCA0NS45Mzg2NjY5NjQ4MDQyXSwgWy02Ni42Mzc5ODg5NzMzNDAxLCA0NS45Mzg4NDgxMzE0NTI0XSwgWy02Ni42MzY3NTgyODE0MDA5LCA0NS45Mzg5MTA2MDI1NzMyXSwgWy02Ni42MzUyMjIxNjIyNjUsIDQ1LjkzODg0MTg4NDMzNjVdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDQzLCAiTmVpZ2hib3VyaCI6ICJQb2V0J3MgSGlsbCIsICJPQkpFQ1RJRCI6IDQzLCAiU2hhcGVfQXJlYSI6IDI5NzAyMC43MjgwNTgsICJTaGFwZV9MZW5nIjogMzA4NC4xMTAyMzIwNSwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmVkOTc2IiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni42MjE1NDA4MjA0ODc5LCA0NS45MzA4MjYyNTQ4MzM0XSwgWy02Ni42MjE3OTIzNDg3Njc0LCA0NS45MzExOTQ4ODY3NDg2XSwgWy02Ni42MjI2MDA4MzI1MjMxLCA0NS45MzE4ODg0MDc5NDgzXSwgWy02Ni42MjI2NjM3MTQ1OTMsIDQ1LjkzMjAzMjEwOTQ1NDZdLCBbLTY2LjYyMjUwMjAxNzg0MTksIDQ1LjkzMTkzMjE0MzIyODhdLCBbLTY2LjYyMjU3Mzg4MzA2NDYsIDQ1LjkzMjA3NTg0NDYyMTddLCBbLTY2LjYyMjg4ODI5MzQxNDEsIDQ1LjkzMjE1NzA2Njk4MzVdLCBbLTY2LjYyMjg1MjM2MDgwMjcsIDQ1LjkzMjI1NzAzMjgwMzldLCBbLTY2LjYyMzE4NDczNzQ1NzgsIDQ1LjkzMjU5NDQxNjExNzZdLCBbLTY2LjYyNDAxMTE4NzUxOTIsIDQ1LjkzMzEzMTcyNjA0NjddLCBbLTY2LjYyNDc3NDc1NTUxMDcsIDQ1LjkzNDQ2ODczMDQ4NjRdLCBbLTY2LjYyNjM3Mzc1NjcxNjQsIDQ1LjkzNTkyNDQwNDI3NDldLCBbLTY2LjYyNzI4MTA1NTE1MzQsIDQ1LjkzNjk2MTQ3MDQ0NjFdLCBbLTY2LjYyNzY1ODM0NzU3MjcsIDQ1LjkzNzIwNTExNTcwODhdLCBbLTY2LjYyODk2MDkwNDczNDcsIDQ1LjkzOTUxNjU2ODc5MjFdLCBbLTY2LjYzMDUzMjk1NjQ4MTksIDQ1LjkzOTc3MjY5Njg1MjJdLCBbLTY2LjYzMTQ5NDE1MzgzNTksIDQ1LjkzODA5ODQ3MjUxMzNdLCBbLTY2LjYzMjAzMzE0MzAwNjQsIDQ1LjkzNjIxODAzMzQxMjFdLCBbLTY2LjYzMTY1NTg1MDU4NzEsIDQ1LjkzNTI5OTY1NjI1NjVdLCBbLTY2LjYzMDE0NjY4MDkwOTcsIDQ1LjkzMzczMTUwNzcyNThdLCBbLTY2LjYyODE0MzQzNzgyNjIsIDQ1LjkzMTg0NDY3MjYzMzNdLCBbLTY2LjYyNzQwNjgxOTI5MzIsIDQ1LjkzMTM2OTgyOTg1MTFdLCBbLTY2LjYyNjk2NjY0NDgwNCwgNDUuOTMwODUxMjQ2OTA1MV0sIFstNjYuNjI1MjA1OTQ2ODQ3MSwgNDUuOTMxMjgyMzU4MzY4OF0sIFstNjYuNjI0NTA1MjYwOTI1NSwgNDUuOTMxMjAxMTM0NzI2XSwgWy02Ni42MjM3OTU1OTE4NTEsIDQ1LjkzMDg4ODczNDk5MTVdLCBbLTY2LjYyMzExMjg3MjIzNTEsIDQ1LjkzMDc0NTAzMDUyMjddLCBbLTY2LjYyMjIzMjUyMzI1NjYsIDQ1LjkzMDcyMDAzODQwMzFdLCBbLTY2LjYyMTU0MDgyMDQ4NzksIDQ1LjkzMDgyNjI1NDgzMzRdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDQ0LCAiTmVpZ2hib3VyaCI6ICJEdW4ncyBDcm9zc2luZyIsICJPQkpFQ1RJRCI6IDQ0LCAiU2hhcGVfQXJlYSI6IDM2MzU0My4yNzgzMjMsICJTaGFwZV9MZW5nIjogMjkyMS45NDYyNTk3LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjYxOTgyNTAzODI5NTIsIDQ1LjkyOTY3NjYwNzM2MjddLCBbLTY2LjYyMTU0MDgyMDQ4NzksIDQ1LjkzMDgyNjI1NDgzMzRdLCBbLTY2LjYyMjk0MjE5MjMzMTEsIDQ1LjkzMDcyNjI4NjQzNDFdLCBbLTY2LjYyMzc5NTU5MTg1MSwgNDUuOTMwODg4NzM0OTkxNV0sIFstNjYuNjI0NjQwMDA4MjE4MSwgNDUuOTMxMjMyMzc0NjAyN10sIFstNjYuNjI1NjI4MTU1MDMwNiwgNDUuOTMxMjQ0ODcwNTQ4NV0sIFstNjYuNjI2OTY2NjQ0ODA0LCA0NS45MzA4NTEyNDY5MDUxXSwgWy02Ni42MjY3NjkwMTU0NDE1LCA0NS45MzA0NTEzNzI0MDY5XSwgWy02Ni42MjcxMjgzNDE1NTUxLCA0NS45MzAxMDc3Mjc5NTY3XSwgWy02Ni42Mjc1OTU0NjU1MDI5LCA0NS45MzAwODI3MzU1NV0sIFstNjYuNjI3OTE4ODU5MDA1MSwgNDUuOTMwMjMyNjg5ODIxM10sIFstNjYuNjI4ODE3MTc0Mjg5MywgNDUuOTI5ODQ1MzA3MTI0N10sIFstNjYuNjMwMDU2ODQ5MzgxMywgNDUuOTI5NjUxNjE0NzYxOF0sIFstNjYuNjMxMDAwMDgwNDI5NywgNDUuOTI5MzcwNDQ3MjI1XSwgWy02Ni42MzI3Nzg3NDQ2OTIyLCA0NS45MjcyNTg1MjEwNTczXSwgWy02Ni42MzUyODUwNDQzMzQ5LCA0NS45MjUzOTY0NjAyODEyXSwgWy02Ni42MzYwNTc1OTU0NzkzLCA0NS45MjQ5MDI4MTYyMzg1XSwgWy02Ni42MzYyNzMxOTExNDc0LCA0NS45MjQ5ODQwNDkxMDQ0XSwgWy02Ni42MzU2MzUzODcyOTU3LCA0NS45MjQ0MDkxNjc4MDNdLCBbLTY2LjYzMjczMzgyODkyOCwgNDUuOTIyNTcyMDA3MTg0Nl0sIFstNjYuNjI4NjI4NTI4MDc5NiwgNDUuOTE5NjQ3NDIxOTIyNl0sIFstNjYuNjI1NjY0MDg3NjQyLCA0NS45MTc4NDEzNTEwNDA0XSwgWy02Ni42MjQ3Mjk4Mzk3NDY1LCA0NS45MTc4MzUxMDE1NTgxXSwgWy02Ni42MjQwNzQwNjk1ODkxLCA0NS45MTgxNzI1NzI1OTM3XSwgWy02Ni42MjA4NDkxMTc3MTkxLCA0NS45MjE5MDMzNjU2MDFdLCBbLTY2LjYxOTc2MjE1NjIyNTMsIDQ1LjkyMzU4NDMyNzcwNF0sIFstNjYuNjE5NDI5Nzc5NTcwMiwgNDUuOTI0MzQ2NjgwMzQ2MV0sIFstNjYuNjE5MzY2ODk3NTAwMywgNDUuOTI1NjUyNjUzNTU5M10sIFstNjYuNjE5ODI1MDM4Mjk1MiwgNDUuOTI5Njc2NjA3MzYyN11dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogNDUsICJOZWlnaGJvdXJoIjogIlNvdXRod29vZCBQYXJrIiwgIk9CSkVDVElEIjogNDUsICJTaGFwZV9BcmVhIjogMTIxODM5OC4wNDE4MSwgIlNoYXBlX0xlbmciOiA0MzczLjgyNDMzNjAyLCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbWy02Ni41ODg0ODI4MTgwMzIzLCA0NS45MTM1MTY1NDEwMjUyXSwgWy02Ni41ODg2MzU1MzE2MzA2LCA0NS45MTM3MjI3ODk2MTg2XSwgWy02Ni41ODg1MDMwMDk1MjI2LCA0NS45MTM1MjIwNTk5MTk1XSwgWy02Ni41ODg0ODI4MTgwMzIzLCA0NS45MTM1MTY1NDEwMjUyXV1dLCBbW1stNjYuNTk4NjI0Nzk3NTksIDQ1Ljg5ODA4OTQ3Mzk0MzVdLCBbLTY2LjU5NzE3ODUwOTk4MjYsIDQ1Ljg5ODI2NDUyMTQzOV0sIFstNjYuNTk1ODQwMDIwMjA5MiwgNDUuODk4Njg5NjM0NDg3OF0sIFstNjYuNTk0Njk5MTU5Nzk4NCwgNDUuODk5MzMzNTQ5NTI0OF0sIFstNjYuNTg2NjIzMzA1Mzk0MiwgNDUuOTA4NDg1MDg3OTI5OV0sIFstNjYuNTg2ODExOTUxNjAzOCwgNDUuOTA5OTE2NDQyMTI1N10sIFstNjYuNTg3MTQ0MzI4MjU4OSwgNDUuOTExMDQxNDk4MTE3M10sIFstNjYuNTg3NzczMTQ4OTU3OCwgNDUuOTEyNDE2NTM1NTgxN10sIFstNjYuNTg4NTAzMDA5NTIyNiwgNDUuOTEzNTIyMDU5OTE5NV0sIFstNjYuNTg5NDg4OTMxMTUwNSwgNDUuOTEzNzkxNTM4OTc5NF0sIFstNjYuNTkwNTU3OTI2MzM4NiwgNDUuOTEzOTEwMjg3Njc0N10sIFstNjYuNTkyNDcxMzM3ODkzOCwgNDUuOTEzNzE2NTM5NjcyNV0sIFstNjYuNTk0MTMzMjIxMTY5NCwgNDUuOTEyMTA0MDMwMDU4NF0sIFstNjYuNTk1ODc1OTUyODIwNiwgNDUuOTEwMDYwMjAwNTUxXSwgWy02Ni41OTg5MjEyNDE2MzM3LCA0NS45MDU4MDM1NDMzODk3XSwgWy02Ni42MDA0MjE0MjgxNTgyLCA0NS45MDIyNzc5NTkwNjIzXSwgWy02Ni42MDA2NzI5NTY0Mzc4LCA0NS45MDEzNzc3NzM5OTIxXSwgWy02Ni42MDA3NjI3ODc5NjYyLCA0NS45MDAyNDAwMTkyMDNdLCBbLTY2LjYwMDY2Mzk3MzI4NDksIDQ1Ljg5OTMyNzI5Nzk1ODRdLCBbLTY2LjYwMDMyMjYxMzQ3NywgNDUuODk4MjA4MjU2MjMyN10sIFstNjYuNTk4NjI0Nzk3NTksIDQ1Ljg5ODA4OTQ3Mzk0MzVdXV1dLCAidHlwZSI6ICJNdWx0aVBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDQ2LCAiTmVpZ2hib3VyaCI6ICJMaW5jb2xuIEhlaWdodHMiLCAiT0JKRUNUSUQiOiA0NiwgIlNoYXBlX0FyZWEiOiAxMDkyNDYxLjI4ODI5LCAiU2hhcGVfTGVuZyI6IDQ1MDUuNjc3ODIxNzQsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlZDk3NiIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNTUyNDg3MzI0NTk3NiwgNDUuODk1MDUxMDYxNjQyNl0sIFstNjYuNTUxMzE5NTE0NzI4MiwgNDUuODk1NDE5OTMxMjYxNF0sIFstNjYuNTUxMjI5NjgzMTk5OSwgNDUuODk1ODQ1MDY2MDg4XSwgWy02Ni41NTEzOTEzNzk5NTEsIDQ1Ljg5NjQzODk5ODk5ODhdLCBbLTY2LjU1MTEzMDg2ODUxODYsIDQ1Ljg5NjgwMTYwNzU0NzZdLCBbLTY2LjU1MTE5Mzc1MDU4ODUsIDQ1Ljg5Njk0NTM5OTkzNzJdLCBbLTY2LjU1NTcxMjI3NjQ2NzYsIDQ1Ljg5OTkxNDk0MjEyMzhdLCBbLTY2LjU1Nzg5NTE4MjYwOCwgNDUuOTAxMTQwMjIyNzIwMV0sIFstNjYuNTYwMTk0ODY5NzM1NCwgNDUuOTAyMjQwNDUxNjQyNF0sIFstNjYuNTYyNTAzNTQwMDE1NSwgNDUuOTAyNzkwNTU3OTI3NF0sIFstNjYuNTY0NjIzNTY0MDg2MSwgNDUuOTAzMDQwNjA0NDM2OV0sIFstNjYuNTY0OTgyODkwMTk5NywgNDUuOTAzMjk2OTAwOTQwNF0sIFstNjYuNTY4MDE5MTk1ODYsIDQ1LjkwNDM5NzA4NzEyNF0sIFstNjYuNTY4NTA0Mjg2MTEzNSwgNDUuOTA0NzM0NjM5ODc3NV0sIFstNjYuNTY5MDUyMjU4NDM2OCwgNDUuOTA0ODE1OTAyMjcwOV0sIFstNjYuNTcwOTI5NzM3MzgwNiwgNDUuOTA1NTc4NTEyNzgxOF0sIFstNjYuNTcwOTkyNjE5NDUwNSwgNDUuOTA1OTE2MDU4MzUxN10sIFstNjYuNTcyMjA1MzQ1MDg0LCA0NS45MDU5NTk4MTQxMDg2XSwgWy02Ni41NzUxMTU4ODY2MDQ2LCA0NS45MDcyNzI0NzA3NzkxXSwgWy02Ni41NzYyNjU3MzAxNjgzLCA0NS45MDc2NDc1MDk4NDA4XSwgWy02Ni41Nzc3ODM4ODI5OTg0LCA0NS45MDg3OTEzNjMzMjkxXSwgWy02Ni41Nzg2MzcyODI1MTgzLCA0NS45MDkyNjAxNDg5MzI1XSwgWy02Ni41ODAxNDY0NTIxOTU2LCA0NS45MDk4MDM5MzUyNzIzXSwgWy02Ni41ODE2NjQ2MDUwMjU4LCA0NS45MTA3MzUyMzUxMzQyXSwgWy02Ni41ODgyODUxODg2Njk4LCA0NS45MTU0NzI3NDY4NDA5XSwgWy02Ni41OTAyODg0MzE3NTM0LCA0NS45MTcwNzg5MDkwMDc5XSwgWy02Ni41OTA5NTMxODUwNjM2LCA0NS45MTc5Mjg4NDM3MTg0XSwgWy02Ni41OTI0MDg0NTU4MjM5LCA0NS45MTg4OTc1MDM0MzM5XSwgWy02Ni41OTI3NzY3NjUwOTA0LCA0NS45MTk0MDk5NDg4MzExXSwgWy02Ni41OTM2ODQwNjM1MjczLCA0NS45MjAwNDExMjUwNzE5XSwgWy02Ni41OTc5OTU5NzY4OTExLCA0NS45MjIzMjIwNDg2NTcyXSwgWy02Ni42MDE3MjM5ODUzMjAyLCA0NS45MjQ5NDAzMDgzNDUyXSwgWy02Ni42MDIxMDEyNzc3Mzk1LCA0NS45MjQ5NDAzMDgzNDUyXSwgWy02Ni42MDI2MzEyODM3NTcyLCA0NS45MjUxMjc3Njg0OTldLCBbLTY2LjYwMzMyMjk4NjUyNTksIDQ1LjkyNTc3MTM3Njg3MjRdLCBbLTY2LjYwMzk2OTc3MzUzMDUsIDQ1LjkyNTg4Mzg1MTM1NTZdLCBbLTY2LjYwNDYwNzU3NzM4MjIsIDQ1LjkyNjE5MDAzMDczNzldLCBbLTY2LjYwNTUwNTg5MjY2NjMsIDQ1LjkyNjQxNDk3Nzc3ODddLCBbLTY2LjYwNzYzNDg5OTg4OTcsIDQ1LjkyNjc2NDg5MzU4NDVdLCBbLTY2LjYwOTE0NDA2OTU2NywgNDUuOTI2ODI3Mzc4MzE3NV0sIFstNjYuNjExMDY2NDY0Mjc1MSwgNDUuOTI2NzMzNjUxMTkxNl0sIFstNjYuNjEyNTc1NjMzOTUyNCwgNDUuOTI2OTQ2MDk5MTE2NF0sIFstNjYuNjEzMDUxNzQxMDUzLCA0NS45MjczMjcyNTM2NDgxXSwgWy02Ni42MTM5MTQxMjM3MjU3LCA0NS45Mjc0ODM0NjM3NjUyXSwgWy02Ni42MTg1MDQ1MTQ4Mjc2LCA0NS45MjkyMDE3NDYwMTg3XSwgWy02Ni42MTg4OTk3NzM1NTI2LCA0NS45MjkyNDU0ODM0MTc4XSwgWy02Ni42MTk4MjUwMzgyOTUyLCA0NS45Mjk2NzY2MDczNjI3XSwgWy02Ni42MTkzOTM4NDY5NTg4LCA0NS45MjY0MTQ5Nzc3Nzg3XSwgWy02Ni42MTAyMzEwMzEwNjA4LCA0NS45MjAxODQ4NTcyNzE2XSwgWy02Ni42MDcxOTQ3MjU0MDA1LCA0NS45MTg4MTAwMTIyODMzXSwgWy02Ni42MDQwNzc1NzEzNjQ2LCA0NS45MTc1MjI2MjY1NDddLCBbLTY2LjYwMzI2MDEwNDQ1NjEsIDQ1LjkxODc3ODc2NTQxMDRdLCBbLTY2LjYwMjE0NjE5MzUwMzcsIDQ1LjkxOTkxNjE0MDI0NzhdLCBbLTY2LjYwMDc3MTc3MTExOSwgNDUuOTIwOTAzNTEyNjg0N10sIFstNjYuNTk5NDUxMjQ3NjUxNCwgNDUuOTIxNTkwOTEzNTAwM10sIFstNjYuNTk0MzMwODUwNTMxOSwgNDUuOTE4NTI4Nzg5NzkzNV0sIFstNjYuNTkyNTc5MTM1NzI3OSwgNDUuOTE3MjAzOTAwMjIyOV0sIFstNjYuNTkzMjA3OTU2NDI2OCwgNDUuOTE2NDkxNDQ2NTI1OF0sIFstNjYuNTk0MjMyMDM1ODUwNywgNDUuOTE1Nzc4OTgzNjgxM10sIFstNjYuNTk1NDcxNzEwOTQyNywgNDUuOTE1MjY2NTA0NzUxMV0sIFstNjYuNTk2ODU1MTE2NDgwMywgNDUuOTE0OTg1MjY0MzAyNV0sIFstNjYuNTkyNDcxMzM3ODkzOCwgNDUuOTEzNzE2NTM5NjcyNV0sIFstNjYuNTkwNTU3OTI2MzM4NiwgNDUuOTEzOTEwMjg3Njc0N10sIFstNjYuNTg5NDg4OTMxMTUwNSwgNDUuOTEzNzkxNTM4OTc5NF0sIFstNjYuNTg4NDk4MTQ2MjU5NSwgNDUuOTEzNTIwNzMwNjU0OV0sIFstNjYuNTg4NjM1NTMxNjMwNiwgNDUuOTEzNzIyNzg5NjE4Nl0sIFstNjYuNTg4NDgyODE4MDMyMywgNDUuOTEzNTE2NTQxMDI1Ml0sIFstNjYuNTg4NDk4MTQ2MjU5NSwgNDUuOTEzNTIwNzMwNjU0OV0sIFstNjYuNTg3OTI1ODYyNTU2MSwgNDUuOTEyNjc5MDM4ODYxM10sIFstNjYuNTg3MjUyMTI2MDkzLCA0NS45MTEzMjI3NTg1NTE5XSwgWy02Ni41ODY4MTE5NTE2MDM4LCA0NS45MDk5MTY0NDIxMjU3XSwgWy02Ni41ODY2MjMzMDUzOTQyLCA0NS45MDg0ODUwODc5Mjk5XSwgWy02Ni41ODIzMjkzNTgzMzYxLCA0NS45MDQ4NDcxNTcwMDU5XSwgWy02Ni41ODAzODAwMTQxNjk1LCA0NS45MDI5MjgwODM2NDddLCBbLTY2LjU3ODEyNTI0MjgwNjQsIDQ1LjkwMDQ0MDA2NTY5MDRdLCBbLTY2LjU3NzY2NzEwMjAxMTUsIDQ1LjkwMDIwMjUxMDQwNjRdLCBbLTY2LjU3NjMyODYxMjIzODEsIDQ1Ljg5OTcwODY0MjIyMV0sIFstNjYuNTc1NzQ0NzA3MzAzNSwgNDUuODk5NjQ2MTI2OTQ3Nl0sIFstNjYuNTc0NjMwNzk2MzUxMiwgNDUuODk5ODk2MTg3NjE4OV0sIFstNjYuNTczNzY4NDEzNjc4NCwgNDUuOTAwMjgzNzc5NDMzN10sIFstNjYuNTczNDAwMTA0NDExOSwgNDUuOTAwMjk2MjgyMzUwNV0sIFstNjYuNTczMDQ5NzYxNDUxMSwgNDUuODk5NjAyMzY2MjE0NF0sIFstNjYuNTcyNjkwNDM1MzM3NSwgNDUuODk5MjY0NzgyMjU1N10sIFstNjYuNTcxOTcxNzgzMTEwMiwgNDUuODk4OTk1OTYzOTMxOF0sIFstNjYuNTcxMTQ1MzMzMDQ4OCwgNDUuODk4OTA4NDQxNDA1OV0sIFstNjYuNTY5Nzk3ODYwMTIyNiwgNDUuODk4ODk1OTM4MTc2N10sIFstNjYuNTY4NzY0Nzk3NTQ1OSwgNDUuODk5NDA4NTY4MjY2OF0sIFstNjYuNTY4NjY1OTgyODY0NiwgNDUuODk5MzUyMzA0MjE5OF0sIFstNjYuNTY4NzE5ODgxNzgxNiwgNDUuODk4ODA4NDE1NDkzMl0sIFstNjYuNTY4NDIzNDM3NzM3OSwgNDUuODk4NTU4MzQ5OTIzXSwgWy02Ni41Njc1ODgwMDQ1MjM3LCA0NS44OTgzODk1NTUwMjY1XSwgWy02Ni41NjY1NTQ5NDE5NDY5LCA0NS44OTg3NzcxNTczNTg1XSwgWy02Ni41NjYwNTE4ODUzODc4LCA0NS44OTgwNzA3MTg4MjE5XSwgWy02Ni41NjQ1OTY2MTQ2Mjc1LCA0NS44OTc2MjA1OTQwMDQ3XSwgWy02Ni41NjM5MDQ5MTE4NTg4LCA0NS44OTc2NDU2MDEwMzQ3XSwgWy02Ni41NjMwOTY0MjgxMDMxLCA0NS44OTc5NDU2ODQ1MTY1XSwgWy02Ni41NjI0Njc2MDc0MDQyLCA0NS44OTgzNzA4MDAwMDYzXSwgWy02Ni41NjE2MDUyMjQ3MzE0LCA0NS44OTg1NTgzNDk5MjNdLCBbLTY2LjU2MTA0ODI2OTI1NTMsIDQ1Ljg5ODU1MjA5ODI2OTNdLCBbLTY2LjU2MDM5MjQ5OTA5NzksIDQ1Ljg5Nzk4OTQ0NjU1NTRdLCBbLTY2LjU1OTM2ODQxOTY3NCwgNDUuODk3NjY0MzU2Mjk5OF0sIFstNjYuNTU5MTQzODQwODUyOSwgNDUuODk3NDk1NTU4Njg1N10sIFstNjYuNTU4NjIyODE3OTg4MiwgNDUuODk3NDI2Nzg5MTQwMl0sIFstNjYuNTU4MTE5NzYxNDI5LCA0NS44OTcwNzY2ODgzMTU1XSwgWy02Ni41NTgyNjM0OTE4NzQ1LCA0NS44OTY1ODkwNDQyMDI3XSwgWy02Ni41NTgwMDI5ODA0NDIxLCA0NS44OTY2NTE1NjI5MTgxXSwgWy02Ni41NTc4NjgyMzMxNDk1LCA0NS44OTY1ODI3OTIzMjczXSwgWy02Ni41NTgzNTMzMjM0MDI5LCA0NS44OTY0MjY0OTUyMTM1XSwgWy02Ni41NTc5NDAwOTgzNzIyLCA0NS44OTU4ODg4Mjk3ODI0XSwgWy02Ni41NTgxMTA3NzgyNzYyLCA0NS44OTU1MzI0NjcyNjc2XSwgWy02Ni41NTc0OTA5NDA3MzAyLCA0NS44OTYwMzg4NzY0NzI5XSwgWy02Ni41NTYzMDUxNjQ1NTUxLCA0NS44OTYyNDUxOTAwMTAzXSwgWy02Ni41NTYxODgzODM1NjgyLCA0NS44OTY0MjY0OTUyMTM1XSwgWy02Ni41NTYyNjkyMzE5NDM4LCA0NS44OTY4NTE2MjIzMzQxXSwgWy02Ni41NTY0Mzk5MTE4NDc3LCA0NS44OTcyMTQyMjgxODg1XSwgWy02Ni41NTY4MzUxNzA1NzI4LCA0NS44OTc0ODkzMDY5MTIzXSwgWy02Ni41NTY3MDk0MDY0MzMsIDQ1Ljg5NzYyNjg0NTc2MzJdLCBbLTY2LjU1NjA3MTYwMjU4MTMsIDQ1Ljg5Nzc4MzEzOTQ5ODVdLCBbLTY2LjU1NTEyODM3MTUzMjksIDQ1Ljg5NzE0NTQ1ODI5NDZdLCBbLTY2LjU1NDU4MDM5OTIwOTYsIDQ1Ljg5NjI1MTQ0MTkyMzhdLCBbLTY2LjU1NDIwMzEwNjc5MDMsIDQ1Ljg5NjIyMDE4MjM0OTddLCBbLTY2LjU1MzM2NzY3MzU3NiwgNDUuODk2NDU3NzU0NjcxNV0sIFstNjYuNTUyOTU0NDQ4NTQ1NCwgNDUuODk2MzQ1MjIwNTQwNV0sIFstNjYuNTUyODQ2NjUwNzExMywgNDUuODk2MDg4ODkxOTQ2M10sIFstNjYuNTUzMTg4MDEwNTE5MiwgNDUuODk1NDEzNjc5MjU0NF0sIFstNjYuNTUzMDk4MTc4OTkwOCwgNDUuODk1MDY5ODE3Nzg0XSwgWy02Ni41NTI0ODczMjQ1OTc2LCA0NS44OTUwNTEwNjE2NDI2XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiA0NywgIk5laWdoYm91cmgiOiAiTGluY29sbiIsICJPQkpFQ1RJRCI6IDQ3LCAiU2hhcGVfQXJlYSI6IDI5OTExNDguODAxNzYsICJTaGFwZV9MZW5nIjogMTYyNjIuMTIzMjM5LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjY2ODYzMDUwNzY4MTQsIDQ1Ljk2MDc1ODY4MjI3MTldLCBbLTY2LjY2OTU0Njc4OTI3MTIsIDQ1Ljk2MTYzOTE3MDQ0MTldLCBbLTY2LjY3MTQ1MTIxNzY3MzYsIDQ1Ljk2MTIzOTUxNzk3MTNdLCBbLTY2LjY3Mjc4OTcwNzQ0NjksIDQ1Ljk2MTE4OTU2MTIwOThdLCBbLTY2LjY3Mzg4NTY1MjA5MzUsIDQ1Ljk2MTQ4OTMwMTEwMzNdLCBbLTY2LjY3NDgxMDkxNjgzNjIsIDQ1Ljk2MjE2OTk1NDQyMjVdLCBbLTY2LjY3NTgzNDk5NjI2MDEsIDQ1Ljk2MTMyMDY5NzYxMjddLCBbLTY2LjY3NzE3MzQ4NjAzMzQsIDQ1Ljk2MDcyMTIxNDM3OTldLCBbLTY2LjY3ODQ4NTAyNjM0ODIsIDQ1Ljk2MDQ0NjQ0OTA2MzddLCBbLTY2LjY4MTIzMzg3MTExNzYsIDQ1Ljk2MDI3Nzg0MjM5OTZdLCBbLTY2LjY4MTM4NjU4NDcxNTksIDQ1Ljk1OTExNjMxNTg4M10sIFstNjYuNjgxMDcyMTc0MzY2NSwgNDUuOTU3OTY3MjU0OTQwOF0sIFstNjYuNjgwNDYxMzE5OTczMywgNDUuOTU3MDYxNzI4MTcxMl0sIFstNjYuNjc5NTk4OTM3MzAwNSwgNDUuOTU2NzkzMTg5ODAxNl0sIFstNjYuNjc3OTgxOTY5Nzg5MSwgNDUuOTU2NTY4MzY1OTc5N10sIFstNjYuNjc2MTEzNDczOTk4MSwgNDUuOTU2NzI0NDkzNzMwNl0sIFstNjYuNjcwMDU4ODI4OTgzMiwgNDUuOTU4ODU0MDMyMzMxOV0sIFstNjYuNjY5MjUwMzQ1MjI3NSwgNDUuOTU5NTU5Njk3MTU3OV0sIFstNjYuNjY4NjMwNTA3NjgxNCwgNDUuOTYwNzU4NjgyMjcxOV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogNDgsICJOZWlnaGJvdXJoIjogIkNvbG9uaWFsIGhlaWdodHMiLCAiT0JKRUNUSUQiOiA0OCwgIlNoYXBlX0FyZWEiOiAzNzY4ODUuNDg2OTU0LCAiU2hhcGVfTGVuZyI6IDI2MzQuODMxMDYxMTYsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlZDk3NiIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjk4MTIyMTk4NDU5MSwgNDUuOTYwODA4NjM5NDIyXSwgWy02Ni42OTk3MTIyMTY1MTIsIDQ1Ljk2MTE3MDgyNzQxMjZdLCBbLTY2LjcwMTA2ODY3MjU5MSwgNDUuOTYxNjM5MTcwNDQxOV0sIFstNjYuNzAxNjQzNTk0MzcyOCwgNDUuOTYxMzc2ODk4ODMzMl0sIFstNjYuNzAxMjc1Mjg1MTA2MywgNDUuOTYxMDI3MjAxNDIzN10sIFstNjYuNzAxMTMxNTU0NjYwOSwgNDUuOTYwNTE1MTQwNTIwNV0sIFstNjYuNzAxODE0Mjc0Mjc2OCwgNDUuOTU4ODQ3Nzg3NDcwNF0sIFstNjYuNzAxODQxMjIzNzM1MywgNDUuOTU3NTQyNTk1OTUzNV0sIFstNjYuNzAxMTA0NjA1MjAyMywgNDUuOTU3MDY3OTczMjM0MV0sIFstNjYuNzAwMDM1NjEwMDE0MiwgNDUuOTU2NTkzMzQ2NDQ5NF0sIFstNjYuNjk4ODQ5ODMzODM5MiwgNDUuOTU2MjY4NTk5NDY1XSwgWy02Ni42OTc5MzM1NTIyNDk0LCA0NS45NTYxNzQ5MjIwOTY1XSwgWy02Ni42OTcyNzc3ODIwOTIsIDQ1Ljk1NTg1NjQxNzg1OTRdLCBbLTY2LjY5NjU3NzA5NjE3MDQsIDQ1Ljk1NzI1NTMyNDc5MzJdLCBbLTY2LjY5NjQ2MDMxNTE4MzQsIDQ1Ljk1ODU1NDI3ODE4MTldLCBbLTY2LjY5NzA4MDE1MjcyOTUsIDQ1Ljk1OTc1OTUyOTgxMl0sIFstNjYuNjk4MTIyMTk4NDU5MSwgNDUuOTYwODA4NjM5NDIyXV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiA0OSwgIk5laWdoYm91cmgiOiAiR2FyZGVuIFBsYWNlIiwgIk9CSkVDVElEIjogNDksICJTaGFwZV9BcmVhIjogMTg4NjEwLjQ1MzA0LCAiU2hhcGVfTGVuZyI6IDE3NTIuMDAyODM5MiwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmVkOTc2IiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni43MDEwNjg2NzI1OTEsIDQ1Ljk2MTYzOTE3MDQ0MTldLCBbLTY2LjcwMjU2ODg1OTExNTUsIDQ1Ljk2MjM3NjAyMjEyN10sIFstNjYuNzAzODcxNDE2Mjc3NCwgNDUuOTYzMjg3NzA2NDEwNl0sIFstNjYuNzA1NTY5MjMyMTY0NCwgNDUuOTYzNTA2MjU4NjMyOV0sIFstNjYuNzA3MTc3MjE2NTIzLCA0NS45NjM5NTU4NDkwNjQ2XSwgWy02Ni43MDY5NzA2MDQwMDc3LCA0NS45NjMxOTQwNDA5MDg2XSwgWy02Ni43MDcxNzcyMTY1MjMsIDQ1Ljk2MjI5NDg0NDAzMTldLCBbLTY2LjcwNzkwNDg1MTkwMzEsIDQ1Ljk2MTMxNDQ1MzAyOTFdLCBbLTY2LjcwOTAxODc2Mjg1NTQsIDQ1Ljk2MDMwOTA2NTg5NDddLCBbLTY2LjcxMDk0MTE1NzU2MzUsIDQ1Ljk1OTI0NzQ1NzE5M10sIFstNjYuNzEyMDM3MTAyMjEwMSwgNDUuOTU4ODYwMjc3MTkyOF0sIFstNjYuNzEzNTEwMzM5Mjc2LCA0NS45NTg1MjkyOTg1OTYyXSwgWy02Ni43MTQxMTIyMTA1MTY0LCA0NS45NTc5NTQ3NjUwMTddLCBbLTY2LjcxNTMwNjk2OTg0NDMsIDQ1Ljk1ODA3MzQxOTE3OTFdLCBbLTY2LjcxNzM3MzA5NDk5NzgsIDQ1Ljk1MDkyMjQ5MDk2NzFdLCBbLTY2LjcwOTE2MjQ5MzMwMDksIDQ1Ljk1MDEzNTUyMDIzODhdLCBbLTY2LjcwOTM5NjA1NTI3NDgsIDQ1Ljk1MTY3ODIyMjE4MDZdLCBbLTY2LjcwOTI3OTI3NDI4NzgsIDQ1Ljk1MzIzMzM3MjE3MzRdLCBbLTY2LjcwODgwMzE2NzE4NzMsIDQ1Ljk1NDc1MTAwNjU5OTJdLCBbLTY2LjcwNzk3NjcxNzEyNTksIDQ1Ljk1NjE5OTkwMjc0MzZdLCBbLTY2LjcwNzA1MTQ1MjM4MzIsIDQ1Ljk1NzMyNDAyMDIwNjJdLCBbLTY2LjcwMzQ0MDIyNDk0MSwgNDUuOTYwODUyMzUxODkxM10sIFstNjYuNzAyNzY2NDg4NDc4LCA0NS45NjEyMTQ1Mzk1OTYyXSwgWy02Ni43MDE2NDM1OTQzNzI4LCA0NS45NjEzNzY4OTg4MzMyXSwgWy02Ni43MDEwNjg2NzI1OTEsIDQ1Ljk2MTYzOTE3MDQ0MTldXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDUwLCAiTmVpZ2hib3VyaCI6ICJGcmVkZXJpY3RvbiBTb3V0aCIsICJPQkpFQ1RJRCI6IDUwLCAiU2hhcGVfQXJlYSI6IDc1NzkzMy40NTkwOCwgIlNoYXBlX0xlbmciOiA0NTY4LjI2NjU4MTMzLCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZDhkM2MiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjY1MzMyMzIxNTI0LCA0NS45MzM1MDY1OTAzNTYzXSwgWy02Ni42NTQ1NDQ5MjQwMjY0LCA0NS45MzQxNzUwOTIwODY2XSwgWy02Ni42NTU5MDEzODAxMDU1LCA0NS45MzQ2OTk4OTE1MzcxXSwgWy02Ni42NTY3Mjc4MzAxNjY4LCA0NS45MzQ5MjQ4MDQwNjddLCBbLTY2LjY1ODA2NjMxOTk0MDIsIDQ1LjkzNTA4MDk5Mjc4NzJdLCBbLTY2LjY1OTE0NDI5ODI4MTEsIDQ1LjkzNTA5OTczNTQwNDFdLCBbLTY2LjY1OTc4MjEwMjEzMjgsIDQ1LjkzNDk0OTc5NDI5MThdLCBbLTY2LjY2MDc2MTI2NTc5MjUsIDQ1LjkzNDU4MTE4NzMzNDFdLCBbLTY2LjY2MTYxNDY2NTMxMjUsIDQ1LjkzNDA3NTEyOTcyMzVdLCBbLTY2LjY2MTM4MTEwMzMzODYsIDQ1LjkzMzYxMjgwMTQ1MDFdLCBbLTY2LjY2MDk0MDkyODg0OTQsIDQ1LjkzMzIzMTY5MDExMDRdLCBbLTY2LjY1NzU2MzI2MzM4MTEsIDQ1LjkzMTYwNzI1MTc1MDRdLCBbLTY2LjY1NjI4NzY1NTY3NzYsIDQ1LjkzMTE4ODYzODc3MDRdLCBbLTY2LjY1NDM0NzI5NDY2MzksIDQ1LjkzMDg4MjQ4Njk3ODhdLCBbLTY2LjY1MjYyMjUyOTMxODQsIDQ1LjkzMDk4ODcwMzA5OF0sIFstNjYuNjUyNDE1OTE2ODAzMSwgNDUuOTMxMDMyNDM5MDg3OV0sIFstNjYuNjUyMzA4MTE4OTY5LCA0NS45MzEyNjM2MTQ0NjE4XSwgWy02Ni42NTIxOTEzMzc5ODIsIDQ1LjkzMTg2OTY2NDI0NjFdLCBbLTY2LjY1MjMxNzEwMjEyMTgsIDQ1LjkzMjQ2OTQ1OTU3NDFdLCBbLTY2LjY1Mjc3NTI0MjkxNjcsIDQ1LjkzMzEyNTQ3ODI4NjhdLCBbLTY2LjY1MzMyMzIxNTI0LCA0NS45MzM1MDY1OTAzNTYzXV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiA1MSwgIk5laWdoYm91cmgiOiAiVGhlIEh1Z2ggSm9obiBGbGVtbWluZyBGb3Jlc3RyeSBDZW50ZXIiLCAiT0JKRUNUSUQiOiA1MSwgIlNoYXBlX0FyZWEiOiAyMjA3MTguOTcwODgsICJTaGFwZV9MZW5nIjogMTg3My44NDcwMzA3NSwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmVkOTc2IiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni42NjE2MDU2ODIxNTk2LCA0NS45MzQwMzc2NDM3OTA4XSwgWy02Ni42NjE5MjkwNzU2NjE5LCA0NS45MzQxODEzMzk3MjgzXSwgWy02Ni42NjMxMjM4MzQ5ODk4LCA0NS45MzI3ODgwOTgyMDM3XSwgWy02Ni42NjMxODY3MTcwNTk3LCA0NS45MzI0NzU3MDc0MDhdLCBbLTY2LjY2MjkxNzIyMjQ3NDQsIDQ1LjkzMjI3NTc3NjM3NTJdLCBbLTY2LjY1OTk3OTczMTQ5NTQsIDQ1LjkzMDkzODcxOTA2NzJdLCBbLTY2LjY1NTc3NTYxNTk2NTcsIDQ1LjkyOTI3MDQ3NjIwMTddLCBbLTY2LjY1NTAxMjA0Nzk3NDIsIDQ1LjkyOTE0NTUxMjE2OTNdLCBbLTY2LjY1NDA1MDg1MDYyMDIsIDQ1LjkyOTE1ODAwODU4NTJdLCBbLTY2LjY1MzExNjYwMjcyNDcsIDQ1LjkyOTMzOTIwNjI5OTZdLCBbLTY2LjY1MjQ0Mjg2NjI2MTYsIDQ1LjkyOTYwMTYyOTUyNjFdLCBbLTY2LjY1MjA1NjU5MDY4OTQsIDQ1LjkzMDQ2Mzg2ODUyODZdLCBbLTY2LjY1MjI3MjE4NjM1NzYsIDQ1LjkzMTM1NzMzMzkzMzVdLCBbLTY2LjY1MjQxNTkxNjgwMzEsIDQ1LjkzMTAzMjQzOTA4NzldLCBbLTY2LjY1MzkwNzEyMDE3NDcsIDQ1LjkzMDg2OTk5MDk1MTRdLCBbLTY2LjY1NDk4NTA5ODUxNTcsIDQ1LjkzMDk0NDk2NzA3MzVdLCBbLTY2LjY1NjcyNzgzMDE2NjgsIDQ1LjkzMTMwMTEwMjI2OTVdLCBbLTY2LjY2MDkzMTk0NTY5NjUsIDQ1LjkzMzIyNTQ0MjM2MTddLCBbLTY2LjY2MTM3MjEyMDE4NTcsIDQ1LjkzMzU5NDA1ODMzMDddLCBbLTY2LjY2MTYwNTY4MjE1OTYsIDQ1LjkzNDAzNzY0Mzc5MDhdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDUyLCAiTmVpZ2hib3VyaCI6ICJLbm93bGVkZ2UgUGFyayIsICJPQkpFQ1RJRCI6IDUyLCAiU2hhcGVfQXJlYSI6IDE2MTkxNS41NDI0MDUsICJTaGFwZV9MZW5nIjogMjI3OC41NTA5NTgyMiwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmVkOTc2IiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni43MjMwODYzODAyMDQ3LCA0NS45Nzc5MTAwNzA5MDUyXSwgWy02Ni43MjAxMTI5NTY2MTQzLCA0NS45Nzc3NjAyNDU1ODU4XSwgWy02Ni43MTcyNjUyOTcxNjM3LCA0NS45ODE1NTU2OTUzOTU1XSwgWy02Ni43MTcxOTM0MzE5NDA5LCA0NS45ODIwMzAxMDgzMjg1XSwgWy02Ni43MTczMTAyMTI5Mjc5LCA0NS45ODI0MDQ2NDE5ODMxXSwgWy02Ni43MTc5NzQ5NjYyMzgxLCA0NS45ODMwMDM4OTA1NjAzXSwgWy02Ni43MTg3MjA1Njc5MjM5LCA0NS45ODMyMzQ4NDkyMTc3XSwgWy02Ni43MTk0MDMyODc1Mzk5LCA0NS45ODMyNDEwOTEzMzAyXSwgWy02Ni43MjAwNTAwNzQ1NDQ0LCA0NS45ODMwNzg3OTYxNzY0XSwgWy02Ni43MjA2NTE5NDU3ODQ4LCA0NS45ODI2OTE3ODI3MzU3XSwgWy02Ni43MjQ0NTE4MTk0MzY2LCA0NS45Nzc5Nzg3NDA3MDc4XSwgWy02Ni43MjMwODYzODAyMDQ3LCA0NS45Nzc5MTAwNzA5MDUyXV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiA1MywgIk5laWdoYm91cmgiOiAiRGlhbW9uZCBTdHJlZXQiLCAiT0JKRUNUSUQiOiA1MywgIlNoYXBlX0FyZWEiOiAxODk3MTAuNjE2MjY3LCAiU2hhcGVfTGVuZyI6IDE4MzAuMTM3MjM3MTIsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlZDk3NiIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNzEyMTQ0OTAwMDQ0MiwgNDUuOTc3OTEwMDcwOTA1Ml0sIFstNjYuNzEyMTg5ODE1ODA4NCwgNDUuOTc3MjY3MDY3NzEyNF0sIFstNjYuNzExODMwNDg5Njk0NywgNDUuOTc2NTYxNjI4NDM1OF0sIFstNjYuNzExMDQ4OTU1Mzk3NiwgNDUuOTc2MzExOTEzMjYzOV0sIFstNjYuNzEwMDI0ODc1OTczNywgNDUuOTc2MjMwNzU1NTkwNl0sIFstNjYuNzA5MDI3NzQ2MDA4MywgNDUuOTc2MzkzMDcwODE4M10sIFstNjYuNzA4MzA5MDkzNzgxLCA0NS45NzY3MzAxODU1NDAyXSwgWy02Ni43MDc2MjYzNzQxNjUxLCA0NS45Nzc0NDE4NjU0MzU4XSwgWy02Ni43MDczNTY4Nzk1Nzk4LCA0NS45NzgxNTk3Nzg4NzAyXSwgWy02Ni43MTIxNDQ5MDAwNDQyLCA0NS45Nzc5MTAwNzA5MDUyXV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiA1NCwgIk5laWdoYm91cmgiOiAiR3Jhc3NlIENpcmNsZSIsICJPQkpFQ1RJRCI6IDU0LCAiU2hhcGVfQXJlYSI6IDYwOTMyLjA1OTQ3MTksICJTaGFwZV9MZW5nIjogMTAwMS4yNzE2MDk0MywgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmVkOTc2IiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni42NTQxNDk2NjUzMDE0LCA0Ni4wMDIwNTc4NjA2NDUxXSwgWy02Ni42NTU0MjUyNzMwMDQ5LCA0Ni4wMDI0MTM1Mzg5NDQ0XSwgWy02Ni42NTY3OTA3MTIyMzY3LCA0Ni4wMDI0Mzg0OTg3MzkyXSwgWy02Ni42NTgwOTMyNjkzOTg3LCA0Ni4wMDIxMzI3NDA0NzcxXSwgWy02Ni42NTkyNzkwNDU1NzM3LCA0Ni4wMDE0Mjc2MTgwNDMyXSwgWy02Ni42NTk1MDM2MjQzOTQ4LCA0Ni4wMDEyMDI5NzUzODAzXSwgWy02Ni42NTk3MTAyMzY5MTAxLCA0NS45OTk2Njc4OTI3NzJdLCBbLTY2LjY2MDE3NzM2MDg1NzksIDQ1Ljk5Nzg1ODE4Nzg0NDZdLCBbLTY2LjY2MTI0NjM1NjA0NiwgNDUuOTk1MzkzMTQ5NzEyNF0sIFstNjYuNjU4ODU2ODM3MzkwMiwgNDUuOTk0MTc2MTkxNjY4MV0sIFstNjYuNjU2MjE1NzkwNDU0OSwgNDUuOTkzMjQwMDUxODg0OV0sIFstNjYuNjUzMzg2MDk3MzA5OSwgNDUuOTkyNjE1OTQ5ODk4N10sIFstNjYuNjUwMDI2Mzk4MTQ3MywgNDUuOTkyMzAzODk2MjY2NF0sIFstNjYuNjQ1NzUwNDE3Mzk0OSwgNDUuOTk3MjAyOTM1MjU4OF0sIFstNjYuNjQ5Njg1MDM4MzM5NCwgNDUuOTk4OTAwMzM1NDk2NV0sIFstNjYuNjUxMTk0MjA4MDE2NywgNDUuOTk5NjgwMzczMjkwMl0sIFstNjYuNjUyODAyMTkyMzc1MiwgNDYuMDAwNzkxMTI4MTI5M10sIFstNjYuNjU0MTQ5NjY1MzAxNCwgNDYuMDAyMDU3ODYwNjQ1MV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogNTUsICJOZWlnaGJvdXJoIjogIkJyb29rc2lkZSBFc3RhdGVzIiwgIk9CSkVDVElEIjogNTUsICJTaGFwZV9BcmVhIjogODQ0OTE0LjIxNjE2OCwgIlNoYXBlX0xlbmciOiAzNTc5LjU2NTQ2NDc1LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjY1ODk1NTY1MjA3MTUsIDQ1Ljk4NDM1ODQxODEzMDNdLCBbLTY2LjY1ODU2OTM3NjQ5OTMsIDQ1Ljk4NDM4MzM4NjA2OTRdLCBbLTY2LjY1Njk3OTM1ODQ0NjQsIDQ1Ljk4NjI4NzE1ODI1NzldLCBbLTY2LjY1NjA0NTExMDU1MDksIDQ1Ljk4ODA5NzI0MTU4NTldLCBbLTY2LjY1NTU5NTk1MjkwODksIDQ1Ljk4OTcxMzc4MzIxMTFdLCBbLTY2LjY1NTI2MzU3NjI1MzcsIDQ1Ljk4OTc2MzcxNDI0NzFdLCBbLTY2LjY1OTEzNTMxNTEyODMsIDQ1Ljk4OTM4OTIzMDM3OTJdLCBbLTY2LjY2NTE5ODk0MzI5NjEsIDQ1Ljk4OTYyNjQwMzc4OTddLCBbLTY2LjY2NjEyNDIwODAzODcsIDQ1Ljk5MjI5NzY1NTE3NThdLCBbLTY2LjY2NjM3NTczNjMxODMsIDQ1Ljk5MjY2NTg3ODMxNjZdLCBbLTY2LjY2Njg2OTgwOTcyNDUsIDQ1Ljk5MzA0MDM0MDAxNTFdLCBbLTY2LjY2ODcxMTM1NjA1NywgNDUuOTkyNjU5NjM3MjY2OF0sIFstNjYuNjcwNjg3NjQ5NjgyMSwgNDUuOTkxOTEwNzA2MTg0Nl0sIFstNjYuNjcyMTYwODg2NzQ4LCA0NS45OTEwNDk0MjI5MTExXSwgWy02Ni42NzM1NDQyOTIyODU2LCA0NS45ODk4MTk4ODY2MDg4XSwgWy02Ni42NzM4MDQ4MDM3MTgsIDQ1Ljk4OTEwODM2NTgxNTZdLCBbLTY2LjY3Mzc4NjgzNzQxMjMsIDQ1Ljk4ODIyODMxNDI4NzNdLCBbLTY2LjY3MzcwNTk4OTAzNjcsIDQ1Ljk4Nzk0MTIwMjI1MV0sIFstNjYuNjczMDY4MTg1MTg1LCA0NS45ODc1MjMwMTQ2NjQ0XSwgWy02Ni42NzMyMDI5MzI0Nzc2LCA0NS45ODcyMDQ2OTA2NTI1XSwgWy02Ni42NzM2NzkwMzk1NzgyLCA0NS45ODY4MzY0MzExNzgzXSwgWy02Ni42NzM3Njg4NzExMDY2LCA0NS45ODY2MzA0NTQ0NzE4XSwgWy02Ni42NzM1MTczNDI4MjcsIDQ1Ljk4NjIzMDk4MjMxMTFdLCBbLTY2LjY3MzA1OTIwMjAzMjEsIDQ1Ljk4NTg2ODk1ODE3NTRdLCBbLTY2LjY3MjczNTgwODUyOTksIDQ1Ljk4NTg0Mzk5MDkwNjRdLCBbLTY2LjY3MTUxNDA5OTc0MzQsIDQ1Ljk4NjI1NTk0OTQwNTZdLCBbLTY2LjY2OTUzNzgwNjExODQsIDQ1Ljk4NjY0MjkzNzkzMDRdLCBbLTY2LjY2OTA0MzczMjcxMjEsIDQ1Ljk4NjM4MDc4NDcwOTJdLCBbLTY2LjY2ODA5MTUxODUxMDksIDQ1Ljk4NTIwNzMyMTc0MV0sIFstNjYuNjY3NDk4NjMwNDIzNCwgNDUuOTg1MDgyNDgzNzkxMV0sIFstNjYuNjY2NTM3NDMzMDY5NCwgNDUuOTg1NDE5NTQ1NjA5N10sIFstNjYuNjY1OTM1NTYxODI5MSwgNDUuOTg1NDM4MjcxMjA2MV0sIFstNjYuNjY1NTY3MjUyNTYyNiwgNDUuOTg1MjYzNDk4NzI2Nl0sIFstNjYuNjY1MjQzODU5MDYwMywgNDUuOTg0NzM5MTc3OTc3NF0sIFstNjYuNjY0NTYxMTM5NDQ0NCwgNDUuOTg0MjY0Nzg4MjU4NV0sIFstNjYuNjYzOTk1MjAwODE1NCwgNDUuOTg0NDc3MDE1NzQwNV0sIFstNjYuNjY0MjI4NzYyNzg5MiwgNDUuOTg0ODc2NTAwNTU4NF0sIFstNjYuNjY0MzM2NTYwNjIzMywgNDUuOTg1NjMxNzY4NjY0OF0sIFstNjYuNjYzMDk2ODg1NTMxMiwgNDUuOTg1NzQ0MTIxNzE3Nl0sIFstNjYuNjYxODMwMjYwOTgwNiwgNDUuOTg1NTMxODk5MDkzMl0sIFstNjYuNjU4OTU1NjUyMDcxNSwgNDUuOTg0MzU4NDE4MTMwM11dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogNTYsICJOZWlnaGJvdXJoIjogIldpbGxpYW1zIC8gSGF3a2lucyBBcmVhIiwgIk9CSkVDVElEIjogNTYsICJTaGFwZV9BcmVhIjogNzY1NTYxLjg3NTM4NiwgIlNoYXBlX0xlbmciOiA0NTExLjgwNTA3NjI4LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjY2MDM1NzAyMzkxNDcsIDQ1Ljk4OTQwNzk1NDYzMjhdLCBbLTY2LjY1ODgyOTg4NzkzMTcsIDQ1Ljk4OTQwMTcxMzIxNTZdLCBbLTY2LjY1Njk3MDM3NTI5MzYsIDQ1Ljk4OTU1MTUwNzAzMzFdLCBbLTY2LjY1MTc2OTEyOTc5ODUsIDQ1Ljk5MDM1NjY0MTg1NjNdLCBbLTY2LjY1MDAyNjM5ODE0NzMsIDQ1Ljk5MjMwMzg5NjI2NjRdLCBbLTY2LjY1MzAwODgwNDg5MDYsIDQ1Ljk5MjU1OTc4MDM3NDhdLCBbLTY2LjY1NTQ3OTE3MTkyMTksIDQ1Ljk5MzA0NjU4MTAyMTldLCBbLTY2LjY1NzgzMjc1Nzk2NjMsIDQ1Ljk5Mzc3MDUzMzAzOTZdLCBbLTY2LjY2MDAyNDY0NzI1OTYsIDQ1Ljk5NDcxMjkwNDY2ODNdLCBbLTY2LjY2MDYyNjUxODQ5OTksIDQ1Ljk5MzQzOTc2MzAzNDFdLCBbLTY2LjY2MDY2MjQ1MTExMTMsIDQ1Ljk5Mjk5MDQxMTkzNV0sIFstNjYuNjYwMzU3MDIzOTE0NywgNDUuOTg5NDA3OTU0NjMyOF1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogNTcsICJOZWlnaGJvdXJoIjogIk1jS25pZ2h0IiwgIk9CSkVDVElEIjogNTcsICJTaGFwZV9BcmVhIjogMjg3OTU2LjI4MTQ3OCwgIlNoYXBlX0xlbmciOiAyMzYwLjg0Nzc2NjYxLCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjY2MDAyNDY0NzI1OTYsIDQ1Ljk5NDcxMjkwNDY2ODNdLCBbLTY2LjY2MTI0NjM1NjA0NiwgNDUuOTk1MzkzMTQ5NzEyNF0sIFstNjYuNjYyNDU5MDgxNjc5NSwgNDUuOTk0NjU2NzM3MjcyNl0sIFstNjYuNjY0MTExOTgxODAyMywgNDUuOTkzODY0MTQ2ODMzMV0sIFstNjYuNjY1ODkwNjQ2MDY0OSwgNDUuOTkzMjIxMzI4OTI3N10sIFstNjYuNjY2ODY5ODA5NzI0NSwgNDUuOTkzMDQwMzQwMDE1MV0sIFstNjYuNjY2Mzc1NzM2MzE4MywgNDUuOTkyNjY1ODc4MzE2Nl0sIFstNjYuNjY2MTI0MjA4MDM4NywgNDUuOTkyMjk3NjU1MTc1OF0sIFstNjYuNjY1MTk4OTQzMjk2MSwgNDUuOTg5NjI2NDAzNzg5N10sIFstNjYuNjYwMzU3MDIzOTE0NywgNDUuOTg5NDA3OTU0NjMyOF0sIFstNjYuNjYwNjYyNDUxMTExMywgNDUuOTkyOTkwNDExOTM1XSwgWy02Ni42NjA2MjY1MTg0OTk5LCA0NS45OTM0Mzk3NjMwMzQxXSwgWy02Ni42NjAwMjQ2NDcyNTk2LCA0NS45OTQ3MTI5MDQ2NjgzXV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiA1OCwgIk5laWdoYm91cmgiOiAiU2hhZG93b29kIEVzdGF0ZXMiLCAiT0JKRUNUSUQiOiA1OCwgIlNoYXBlX0FyZWEiOiAyMjEzMDkuNDY3NzU3LCAiU2hhcGVfTGVuZyI6IDIwMTkuNzYwNTAwMzIsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlZDk3NiIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjMxODcxNDQ2MjU1MiwgNDUuOTg4MTUzNDE1NjM4OF0sIFstNjYuNjMzNDQzNDk4MDAyNSwgNDUuOTg4MDcyMjc1MzIxOV0sIFstNjYuNjM0NzczMDA0NjIzLCA0NS45ODgyNzgyNDY2NjMzXSwgWy02Ni42MzU5NzY3NDcxMDM3LCA0NS45ODg3MDg5MTE1MzY5XSwgWy02Ni42MzcxODk0NzI3MzcyLCA0NS45ODk0MjY2Nzg4OF0sIFstNjYuNjM1OTU4NzgwNzk4LCA0NS45ODgxNjU4OTg3NTM5XSwgWy02Ni42MzUyOTQwMjc0ODc3LCA0NS45ODY3NjE1MzA2NDY0XSwgWy02Ni42MzUwNTE0ODIzNjEsIDQ1Ljk4MjQyMzM2ODU5OTNdLCBbLTY2LjYzNTIwNDE5NTk1OTMsIDQ1Ljk4MTExODczMjUxODddLCBbLTY2LjYzNTgxNTA1MDM1MjUsIDQ1Ljk3OTU1MTg4MDEzNl0sIFstNjYuNjM2ODEyMTgwMzE3OSwgNDUuOTc4MDk3MzUxOTg0NV0sIFstNjYuNjM3ODAwMzI3MTMwNCwgNDUuOTc3MDExMTEyOTA3NV0sIFstNjYuNjM4MTIzNzIwNjMyNywgNDUuOTc2OTExMjI3Nzg0Nl0sIFstNjYuNjM4NTk5ODI3NzMzMywgNDUuOTc2OTczNjU2MDA3NV0sIFstNjYuNjM3ODk5MTQxODExNywgNDUuOTc2NzU1MTU2OTE5NV0sIFstNjYuNjQwMjE2Nzk1MjQ0NywgNDUuOTczNTA4NzgzMTk1Ml0sIFstNjYuNjQxNDU2NDcwMzM2OCwgNDUuOTcxMDMwMTczNjA3XSwgWy02Ni42Mzc2NjU1Nzk4Mzc4LCA0NS45Njk5NzUwMTM5NDk5XSwgWy02Ni42MzUxNzcyNDY1MDA4LCA0NS45Njg5OTQ3NTg4NjA4XSwgWy02Ni42MzQ5MDc3NTE5MTU2LCA0NS45NjkwMTk3MzM3MjgxXSwgWy02Ni42MzMzODk1OTkwODU0LCA0NS45NzAyNDM0ODg0MzJdLCBbLTY2LjYzMjMzODU3MDIwMywgNDUuOTcxNTQyMTM3MzIyXSwgWy02Ni42MzM4OTI2NTU2NDQ1LCA0NS45NzE5NDE3MTU0Njk4XSwgWy02Ni42MzQwNjMzMzU1NDg1LCA0NS45NzI3OTcwNTI3NTIyXSwgWy02Ni42MjM4MzE1MjQ0NjI0LCA0NS45ODUyMDczMjE3NDFdLCBbLTY2LjYyNTc4OTg1MTc4MTgsIDQ1Ljk4NTY4MTcwMzM4MzFdLCBbLTY2LjYyNzI5MDAzODMwNjIsIDQ1Ljk4NjE2ODU2NDUyNTZdLCBbLTY2LjYyOTQ5OTg5MzkwNTIsIDQ1Ljk4NzUxNjc3MzAzNDddLCBbLTY2LjYzMDY0MDc1NDMxNiwgNDUuOTg3OTE2MjM1OTE2Nl0sIFstNjYuNjMxODcxNDQ2MjU1MiwgNDUuOTg4MTUzNDE1NjM4OF1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogNTksICJOZWlnaGJvdXJoIjogIk5vcnRoIERldm9uIiwgIk9CSkVDVElEIjogNTksICJTaGFwZV9BcmVhIjogMTIzNzk1Ni44MTg4NiwgIlNoYXBlX0xlbmciOiA2MTg5LjY4NjI2MzUyLCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZDhkM2MiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjYyMDUxNjc0MTA2NCwgNDUuOTcwNTE4MjA1MTU5Nl0sIFstNjYuNjE4NjkzMTYxMDM3MiwgNDUuOTcxOTQxNzE1NDY5OF0sIFstNjYuNjE3MTU3MDQxOTAxNCwgNDUuOTcyODI4MjY5MTkxNV0sIFstNjYuNjE1NDIzMjkzNDAzLCA0NS45NzM1MDg3ODMxOTUyXSwgWy02Ni42MTM1MzY4MzEzMDY0LCA0NS45NzM5NTgyOTI0NDY1XSwgWy02Ni42MTI5ODg4NTg5ODMxLCA0NS45NzQ4MDczNTU1MjJdLCBbLTY2LjYxMjEwODUxMDAwNDYsIDQ1Ljk3NTM0NDI1NjMzNjZdLCBbLTY2LjYxMDgyMzkxOTE0ODMsIDQ1Ljk3NTU5Mzk3NTg3MjFdLCBbLTY2LjYwNzY5Nzc4MTk1OTYsIDQ1Ljk3NTQ1MDM4NzI3NjddLCBbLTY2LjYwNjY2NDcxOTM4MjksIDQ1Ljk3NjEzNzExMTk3MzZdLCBbLTY2LjYwNTgyOTI4NjE2ODYsIDQ1Ljk3NjkzNjE5OTA4MjJdLCBbLTY2LjYwNTIwMDQ2NTQ2OTgsIDQ1Ljk3NzgyODkxNTU3NDJdLCBbLTY2LjYwNDg3NzA3MTk2NzUsIDQ1Ljk3ODU4NDI3OTgyNjJdLCBbLTY2LjYwNDY3OTQ0MjYwNDksIDQ1Ljk3OTc3MDM2ODE4ODRdLCBbLTY2LjYwNjU5Mjg1NDE2MDEsIDQ1Ljk4MDYxMzA5OTc0MjldLCBbLTY2LjYwODAwMzIwOTE1NjIsIDQ1Ljk4MTU0OTQ1MzA5M10sIFstNjYuNjA4Nzc1NzYwMzAwNSwgNDUuOTgyMzA0NzY2NTg5Nl0sIFstNjYuNjA5NTkzMjI3MjA5MSwgNDUuOTgzNzA5MjQ3NzYyMl0sIFstNjYuNjEwMTIzMjMzMjI2NywgNDUuOTg1NDQ0NTEzMDcwMl0sIFstNjYuNjEwMjkzOTEzMTMwNywgNDUuOTg3Nzk3NjQ1Njc0NF0sIFstNjYuNjEwMDk2MjgzNzY4MiwgNDUuOTg4NjA5MDQ3NTE2OF0sIFstNjYuNjA5NTc1MjYwOTAzNCwgNDUuOTg5MjE0NDcwMzczOF0sIFstNjYuNjExOTM3ODMwMTAwNiwgNDUuOTkwMjk0MjI4NzIyOV0sIFstNjYuNjE0MTM4NzAyNTQ2NywgNDUuOTkwOTkzMjUxNzk3Ml0sIFstNjYuNjIxNzkyMzQ4NzY3NCwgNDUuOTgxODkyNzc4Njg3XSwgWy02Ni42MjkzMTEyNDc2OTU1LCA0NS45NzQyMjA1MDQ0OTE1XSwgWy02Ni42MjkzNDcxODAzMDY5LCA0NS45NzQwMDE5OTQ1NDAyXSwgWy02Ni42Mjg2Mzc1MTEyMzI0LCA0NS45NzM5MDgzNDcxNTQzXSwgWy02Ni42MjY3NjkwMTU0NDE1LCA0NS45NzMwMjE4MTA3MjI0XSwgWy02Ni42MjU4MDc4MTgwODc1LCA0NS45NzI5MjgxNjE2NzldLCBbLTY2LjYyNTIxNDkyOTk5OTksIDQ1Ljk3MjY5MDkxNjcyN10sIFstNjYuNjI0OTgxMzY4MDI2MSwgNDUuOTcyOTY1NjIxMzE1NF0sIFstNjYuNjIzNzk1NTkxODUxLCA0NS45NzI3MDk2NDY2Mjg2XSwgWy02Ni42MjA1MTY3NDEwNjQsIDQ1Ljk3MDUxODIwNTE1OTZdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDYwLCAiTmVpZ2hib3VyaCI6ICJOb3J0aCBEZXZvbiIsICJPQkpFQ1RJRCI6IDYwLCAiU2hhcGVfQXJlYSI6IDIwNDI4ODUuMzc0OTcsICJTaGFwZV9MZW5nIjogNjQ4MS4zOTQyODA2NywgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmQ4ZDNjIiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni41OTY4NTUxMTY0ODAzLCA0NS45MTQ5ODUyNjQzMDI1XSwgWy02Ni41OTU0NzE3MTA5NDI3LCA0NS45MTUyNjY1MDQ3NTExXSwgWy02Ni41OTQyMzIwMzU4NTA3LCA0NS45MTU3Nzg5ODM2ODEzXSwgWy02Ni41OTMyMDc5NTY0MjY4LCA0NS45MTY0OTE0NDY1MjU4XSwgWy02Ni41OTI1NzkxMzU3Mjc5LCA0NS45MTcyMDM5MDAyMjI5XSwgWy02Ni41OTQzMzA4NTA1MzE5LCA0NS45MTg1Mjg3ODk3OTM1XSwgWy02Ni41OTk0NTEyNDc2NTE0LCA0NS45MjE1OTA5MTM1MDAzXSwgWy02Ni42MDA3NzE3NzExMTksIDQ1LjkyMDkwMzUxMjY4NDddLCBbLTY2LjYwMjE0NjE5MzUwMzcsIDQ1LjkxOTkxNjE0MDI0NzhdLCBbLTY2LjYwMzI2MDEwNDQ1NjEsIDQ1LjkxODc3ODc2NTQxMDRdLCBbLTY2LjYwNDA3NzU3MTM2NDYsIDQ1LjkxNzUyMjYyNjU0N10sIFstNjYuNTk2ODU1MTE2NDgwMywgNDUuOTE0OTg1MjY0MzAyNV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogNjEsICJOZWlnaGJvdXJoIjogIldlc2JldHQgLyBDYXNlIiwgIk9CSkVDVElEIjogNjEsICJTaGFwZV9BcmVhIjogMzY1OTI1LjM0MzM0LCAiU2hhcGVfTGVuZyI6IDIzNjguNTc5NzI5NzgsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlZDk3NiIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNzA2MTQ0MTUzOTQ2MywgNDUuOTM5MDk4MDE1NTEzMl0sIFstNjYuNzA0NjA4MDM0ODEwNCwgNDUuOTM4NzkxOTA3MzgzNV0sIFstNjYuNzA0MTA0OTc4MjUxMywgNDUuOTM5MzY2NjM5NjIyNV0sIFstNjYuNzAyMjM2NDgyNDYwMywgNDUuOTQwNzcyMjA5NjcxNl0sIFstNjYuNjk5MjI3MTI2MjU4NSwgNDUuOTQ0NjEzOTE5MzM4OV0sIFstNjYuNjk5Njc2MjgzOTAwNiwgNDUuOTQ0ODUxMjg0NTM3MV0sIFstNjYuNjk5Mzk3ODA2MTYyNSwgNDUuOTQ1MDUxMTcwMjMxNV0sIFstNjYuNjk5NzY2MTE1NDI5LCA0NS45NDUyNTEwNTUyMDUyXSwgWy02Ni42OTU2MjQ4ODE5NjkyLCA0NS45NDgyNjE3MzU0MzVdLCBbLTY2LjY5NTAxNDAyNzU3NiwgNDUuOTQ5ODYwNzAyNDMxNl0sIFstNjYuNjk1NTUzMDE2NzQ2NSwgNDUuOTQ5ODYwNzAyNDMxNl0sIFstNjYuNjk1NzIzNjk2NjUwNSwgNDUuOTUwNzE2MzgwNjY1OV0sIFstNjYuNjk5ODkxODc5NTY4OCwgNDUuOTUwMzQxNjMyNzAwMV0sIFstNjYuNzAwMjYwMTg4ODM1MywgNDUuOTUwNzY2MzQ2ODY5OV0sIFstNjYuNzAxMzU2MTMzNDgxOSwgNDUuOTUwNTc4OTczMzcyN10sIFstNjYuNzA1MzUzNjM2NDk2MiwgNDUuOTUwMzg1MzUzNDI2N10sIFstNjYuNzA4NjQxNDcwNDM2MSwgNDUuOTUwMDY2ODE1OTE0OF0sIFstNjYuNzEwMjc2NDA0MjUzMiwgNDUuOTQ2ODM3NjE2NjE5Ml0sIFstNjYuNzExNzQwNjU4MTY2MywgNDUuOTQyMzAyNjc4NzU3NF0sIFstNjYuNzA4NDI1ODc0NzY3OSwgNDUuOTQxNzQ2NzE3MzIyNV0sIFstNjYuNzA5MTA4NTk0MzgzOCwgNDUuOTM5ODM1MTY2OTMxM10sIFstNjYuNzA2MTQ0MTUzOTQ2MywgNDUuOTM5MDk4MDE1NTEzMl1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogNjIsICJOZWlnaGJvdXJoIjogIlNlcmVuaXR5IExhbmUiLCAiT0JKRUNUSUQiOiA2MiwgIlNoYXBlX0FyZWEiOiAxMDQwMDA1LjkxNTk5LCAiU2hhcGVfTGVuZyI6IDQ0NTguMTQyMjI5MiwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmVkOTc2IiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni43MzE4NjI5MjA1MzA2LCA0NS45NjUyNzMzNzc3ODg3XSwgWy02Ni43MzEzNjg4NDcxMjQzLCA0NS45Njc4OTU4NTM1NTA0XSwgWy02Ni43MzU2NjI3OTQxODI0LCA0NS45Njc2NTg1ODcwNDIyXSwgWy02Ni43MzU5MzIyODg3Njc3LCA0NS45Njc3MzM1MTM0MTc3XSwgWy02Ni43MzYxMDI5Njg2NzE2LCA0NS45Njc1ODM2NjA1NjUyXSwgWy02Ni43MzcwMjgyMzM0MTQzLCA0NS45Njc1NTg2ODUwNTA0XSwgWy02Ni43NDI3Njg0NjgwNzk4LCA0NS45Njc2Mzk4NTU0MzI0XSwgWy02Ni43NDUyNjU3ODQ1Njk3LCA0NS45NjczMjc2NjEwMDQ0XSwgWy02Ni43NDU1MTczMTI4NDkyLCA0NS45NjcxNzc4MDcwNTRdLCBbLTY2Ljc0NjA4MzI1MTQ3ODIsIDQ1Ljk2NzEzNDA5OTU3NTVdLCBbLTY2Ljc0NjQ5NjQ3NjUwODksIDQ1Ljk2NzMwODkyOTI4MjhdLCBbLTY2Ljc0NjE4MjA2NjE1OTUsIDQ1Ljk2NTgyMjg1OTE4Ml0sIFstNjYuNzQ1ODk0NjA1MjY4NSwgNDUuOTY1NTIzMTQyNzM0XSwgWy02Ni43NDUzNzM1ODI0MDM4LCA0NS45NjUzMzU4MTkxMzA2XSwgWy02Ni43NDUyMTE4ODU2NTI2LCA0NS45NjUxMzYwMDY1ODg3XSwgWy02Ni43NDMzMTY0NDA0MDMxLCA0NS45NjU1MTA2NTQ1MTM1XSwgWy02Ni43NDIxMTI2OTc5MjI0LCA0NS45NjU1MTA2NTQ1MTM1XSwgWy02Ni43NDA2MjE0OTQ1NTA4LCA0NS45NjUzNjA3OTU2NDc2XSwgWy02Ni43Mzg5MDU3MTIzNTgxLCA0NS45NjQ5NzM2NTgzNjc4XSwgWy02Ni43Mzc1OTQxNzIwNDMzLCA0NS45NjQ4MjM3OTgwNDkzXSwgWy02Ni43MzU5ODYxODc2ODQ3LCA0NS45NjQ0OTI4NTUwNzY0XSwgWy02Ni43MzE3OTEwNTUzMDc5LCA0NS45NjMwNjI5MDg5Mzk3XSwgWy02Ni43MzIzMTIwNzgxNzI3LCA0NS45NjM1NDk5Njg5NzM5XSwgWy02Ni43MzI1MTg2OTA2ODgsIDQ1Ljk2NDE0MzE3NzMzNDRdLCBbLTY2LjczMjM3NDk2MDI0MjUsIDQ1Ljk2NDc0MjYyMzU0MDhdLCBbLTY2LjczMTg2MjkyMDUzMDYsIDQ1Ljk2NTI3MzM3Nzc4ODddXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDYzLCAiTmVpZ2hib3VyaCI6ICJNb250ZWl0aCAvIFRhbGlzbWFuIiwgIk9CSkVDVElEIjogNjMsICJTaGFwZV9BcmVhIjogMzQyMjk4LjIxMDU3NSwgIlNoYXBlX0xlbmciOiAzMTU5LjE2MDQ1NzI3LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2Ljc0OTU0MTc2NTMyMjEsIDQ1Ljk2NzUwODczMzk4N10sIFstNjYuNzUwOTg4MDUyOTI5NSwgNDUuOTY3OTIwODI4OTEzMl0sIFstNjYuNzUzMjk2NzIzMjA5NywgNDUuOTY4Mjk1NDU4MDAzOV0sIFstNjYuNzU1NTc4NDQ0MDMxNCwgNDUuOTY5MDE5NzMzNzI4MV0sIFstNjYuNzU1NTg3NDI3MTg0MiwgNDUuOTY0ODIzNzk4MDQ5M10sIFstNjYuNzQ5NjEzNjMwNTQ0OCwgNDUuOTY0NDgwMzY2NjIzNl0sIFstNjYuNzQ5NTQxNzY1MzIyMSwgNDUuOTY3NTA4NzMzOTg3XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiA2NCwgIk5laWdoYm91cmgiOiAiUmFpbCBTaWRlIiwgIk9CSkVDVElEIjogNjQsICJTaGFwZV9BcmVhIjogMTg0NDQ0LjU5NDM0NiwgIlNoYXBlX0xlbmciOiAxNzc2LjczNzczNTczLCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2Ljc1OTc0NjYyNjk0OTcsIDQ1Ljk1ODQzNTYyNTA0OTVdLCBbLTY2Ljc2MDAxNjEyMTUzNDksIDQ1Ljk2MzIyNTI2Mjc2MDJdLCBbLTY2Ljc1OTg1NDQyNDc4MzgsIDQ1Ljk2NTEwNDc4NTgxNF0sIFstNjYuNzY3NzQxNjMyOTc4MywgNDUuOTY1NDQxOTY5MjUwM10sIFstNjYuNzcxNTQxNTA2NjMwMiwgNDUuOTY2MDc4ODY1Njk3Ml0sIFstNjYuNzcwNTM1MzkzNTExOSwgNDUuOTU3NDQyNjc1NzE4OV0sIFstNjYuNzY1Mjk4MjE1NDA1NSwgNDUuOTU3Nzk4NjQwNzMyNV0sIFstNjYuNzY1MzA3MTk4NTU4NCwgNDUuOTU3OTExMDUwMjYxN10sIFstNjYuNzY1MDkxNjAyODkwMiwgNDUuOTU3OTIzNTQwMTk1M10sIFstNjYuNzY1MTYzNDY4MTEyOSwgNDUuOTU4NDIzMTM1MjMxM10sIFstNjYuNzY1MDY0NjUzNDMxNywgNDUuOTU4MzIzMjE2NTg0NV0sIFstNjYuNzYzNjk5MjE0MTk5OCwgNDUuOTU4NDIzMTM1MjMxM10sIFstNjYuNzYzNjA5MzgyNjcxNCwgNDUuOTU4MTEwODg4ODYxN10sIFstNjYuNzYyMDU1Mjk3MjI5OSwgNDUuOTU4MTE3MTMzODA2M10sIFstNjYuNzU5NjgzNzQ0ODc5OCwgNDUuOTU3NDA1MjA1NTg0NF0sIFstNjYuNzU5NzQ2NjI2OTQ5NywgNDUuOTU4NDM1NjI1MDQ5NV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogNjUsICJOZWlnaGJvdXJoIjogIlNpbHZlcndvb2QiLCAiT0JKRUNUSUQiOiA2NSwgIlNoYXBlX0FyZWEiOiA3Mjg1NjUuNjYyNDQ5LCAiU2hhcGVfTGVuZyI6IDM3MTAuNzUxNjMwMzMsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlZDk3NiIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjY3MDA0NTU3MDE3MiwgNDUuOTQ2MzMxNjcwODYzNV0sIFstNjYuNjc5MDk1ODgwNzQxNCwgNDUuOTQ3OTExOTU1MjU1OV0sIFstNjYuNjc5MzI5NDQyNzE1MywgNDUuOTQ3Njc0NjAzMTYzXSwgWy02Ni42NzkyNzU1NDM3OTgyLCA0NS45NDcwNjg3MjYxMDddLCBbLTY2LjY4MDU2MDEzNDY1NDUsIDQ1Ljk0NTY2MzMxNTY4NzJdLCBbLTY2LjY3MTcwMjc0NTk1MzEsIDQ1Ljk0MTg2NTQwNjE4NjddLCBbLTY2LjY3MDU4ODgzNTAwMDgsIDQ1Ljk0MTU3MTgwNjk1NDFdLCBbLTY2LjY3MDIyMDUyNTczNDMsIDQ1Ljk0MTE3MjAwOTc1NDNdLCBbLTY2LjY2OTIzMjM3ODkyMTgsIDQ1Ljk0MDg2NTkxMzA3NDddLCBbLTY2LjY1OTkxNjg0OTQyNTUsIDQ1LjkzNjYzNjYwODQzMDRdLCBbLTY2LjY1NjE3MDg3NDY5MDcsIDQ1Ljk0MDk0NzEyMjU2MjVdLCBbLTY2LjY1NzY0NDExMTc1NjcsIDQ1Ljk0MTU3MTgwNjk1NDFdLCBbLTY2LjY1NzQxOTUzMjkzNTYsIDQ1Ljk0MTkwOTEzMzU5OV0sIFstNjYuNjYyMDU0ODM5ODAxNywgNDUuOTQzNjY0NDQ4MzgyN10sIFstNjYuNjY2NTY0MzgyNTI4LCA0NS45NDU1NzU4NjY3NTAyXSwgWy02Ni42NjcwMDQ1NTcwMTcyLCA0NS45NDYzMzE2NzA4NjM1XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiA2NiwgIk5laWdoYm91cmgiOiAiUHJvc3BlY3QiLCAiT0JKRUNUSUQiOiA2NiwgIlNoYXBlX0FyZWEiOiA5NzI5MDIuODE4NTc2LCAiU2hhcGVfTGVuZyI6IDQ3ODUuNTQxMTIxMjIsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZkOGQzYyIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjg5MDMxMjQ3NzgzOCwgNDUuOTQ0NDcwMjUwNDM1N10sIFstNjYuNjg5OTIwNTc5OTE1MSwgNDUuOTQ0NDk1MjM2MzU4Nl0sIFstNjYuNjkxMjE0MTUzOTI0MiwgNDUuOTQ0OTI2MjQxNzU2OV0sIFstNjYuNjkzOTQ1MDMyMzg3OSwgNDUuOTQ2NzgxNDAwNjUyMl0sIFstNjYuNzAwMTk3MzA2NzY1NCwgNDUuOTQyMjMzOTY0NzI0N10sIFstNjYuNjkzNDE1MDI2MzcwMywgNDUuOTM4NjQ4MjIzMzkzXSwgWy02Ni42ODk5NTY1MTI1MjY0LCA0NS45NDE4NDA0MTkwNzg1XSwgWy02Ni42ODkwMzEyNDc3ODM4LCA0NS45NDQ0NzAyNTA0MzU3XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiA2NywgIk5laWdoYm91cmgiOiAiTGlhbiAvIFZhbGNvcmUiLCAiT0JKRUNUSUQiOiA2NywgIlNoYXBlX0FyZWEiOiA0MTExOTcuOTU2MjQ0LCAiU2hhcGVfTGVuZyI6IDI1ODguMzUwMjUyMjcsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlZDk3NiIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjIwNTE2NzQxMDY0LCA0NS45NzA1MTgyMDUxNTk2XSwgWy02Ni42MjM3OTU1OTE4NTEsIDQ1Ljk3MjcwOTY0NjYyODZdLCBbLTY2LjYyNDk4MTM2ODAyNjEsIDQ1Ljk3Mjk2NTYyMTMxNTRdLCBbLTY2LjYyNTIxNDkyOTk5OTksIDQ1Ljk3MjY5MDkxNjcyN10sIFstNjYuNjI1ODA3ODE4MDg3NSwgNDUuOTcyOTI4MTYxNjc5XSwgWy02Ni42MjY3NjkwMTU0NDE1LCA0NS45NzMwMjE4MTA3MjI0XSwgWy02Ni42Mjg2Mzc1MTEyMzI0LCA0NS45NzM5MDgzNDcxNTQzXSwgWy02Ni42MjkzNDcxODAzMDY5LCA0NS45NzQwMDE5OTQ1NDAyXSwgWy02Ni42Mjk1NjI3NzU5NzUxLCA0NS45NzI3MjIxMzMyMjYyXSwgWy02Ni42MzM0Nzk0MzA2MTM4LCA0NS45Njg0ODI3NzE1OTkxXSwgWy02Ni42MzI4Nzc1NTkzNzM1LCA0NS45Njc5ODk1MTExMDI5XSwgWy02Ni42MzExMTY4NjE0MTY2LCA0NS45NjcwOTAzOTIwNjI0XSwgWy02Ni42MzA1MzI5NTY0ODE5LCA0NS45NjY1MDk3MDMyNTkxXSwgWy02Ni42MzA2NTg3MjA2MjE3LCA0NS45NjYyMjg3MjI2MjA1XSwgWy02Ni42MzA1NTk5MDU5NDA0LCA0NS45NjYwNzI2MjE2NDk5XSwgWy02Ni42MjkxNTg1MzQwOTcyLCA0NS45NjUzMDQ1OTg0Njg0XSwgWy02Ni42Mjg2NzM0NDM4NDM4LCA0NS45NjQ4MzAwNDIyMzczXSwgWy02Ni42MjY3OTU5NjQ5LCA0NS45NjU2MTA1NjAxOTg4XSwgWy02Ni42MjU4NjE3MTcwMDQ1LCA0NS45NjYxNTM3OTQyMDk1XSwgWy02Ni42MjI3ODk0Nzg3MzI4LCA0NS45Njg3NzYyMjgyOTE0XSwgWy02Ni42MjA1MTY3NDEwNjQsIDQ1Ljk3MDUxODIwNTE1OTZdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDY4LCAiTmVpZ2hib3VyaCI6ICJOb3J0aCBEZXZvbiIsICJPQkpFQ1RJRCI6IDY4LCAiU2hhcGVfQXJlYSI6IDU0NzA2Ny4yNzUzNjEsICJTaGFwZV9MZW5nIjogMzAzMC41OTE3NDE1NSwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmQ4ZDNjIiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni42NzEwNjQ5NDIxMDE0LCA0NS45NTg0NjY4NDk1ODI3XSwgWy02Ni42NzYxMTM0NzM5OTgxLCA0NS45NTY3MjQ0OTM3MzA2XSwgWy02Ni42Nzc1MTQ4NDU4NDE0LCA0NS45NTY1NjgzNjU5Nzk3XSwgWy02Ni42Nzg5MjUyMDA4Mzc0LCA0NS45NTY2NTU3OTc1NzQ0XSwgWy02Ni42ODA0NjEzMTk5NzMzLCA0NS45NTcwNjE3MjgxNzEyXSwgWy02Ni42ODA5MTA0Nzc2MTUzLCA0NS45NTc2NTUwMDYwMDIyXSwgWy02Ni42ODEzNjg2MTg0MTAyLCA0NS45NTg5NDc3MDUxNzEzXSwgWy02Ni42ODEyMzM4NzExMTc2LCA0NS45NjAyNzc4NDIzOTk2XSwgWy02Ni42ODQxMTc0NjMxNzk2LCA0NS45NjAxMDkyMzUyMjI1XSwgWy02Ni42ODQ4MTgxNDkxMDEzLCA0NS45NjAyNTkxMDgyOTQyXSwgWy02Ni42ODU0MTEwMzcxODg4LCA0NS45NjA1NTg4NTMyMjE0XSwgWy02Ni42ODUwMDY3OTUzMTA5LCA0NS45NTk2MzQ2MzQ0ODc2XSwgWy02Ni42ODQ3MjgzMTc1NzI4LCA0NS45NTg0NDgxMTQ4NjQ5XSwgWy02Ni42ODQ2ODM0MDE4MDg2LCA0NS45NTc0ODYzOTA4NDM3XSwgWy02Ni42ODQ4NTQwODE3MTI2LCA0NS45NTYyODczMzQ5MTk2XSwgWy02Ni42ODUyMjIzOTA5NzkxLCA0NS45NTUxMzgyMTUzMTI1XSwgWy02Ni42ODU3NzkzNDY0NTUzLCA0NS45NTQwNTc3NzEzMzg3XSwgWy02Ni42ODY1NjA4ODA3NTI1LCA0NS45NTMwNTg0OTgwNDY3XSwgWy02Ni42ODc1NTgwMTA3MTc4LCA0NS45NTIxNDY2NDU0NDU2XSwgWy02Ni42ODQzNTEwMjUxNTM1LCA0NS45NTEzNzg0MjkyMTMzXSwgWy02Ni42ODI2ODkxNDE4Nzc5LCA0NS45NTExNTk4MjkxNTI0XSwgWy02Ni42ODA1NjkxMTc4MDc0LCA0NS45NTEwNDc0MDU5MjgyXSwgWy02Ni42NzgyNTE0NjQzNzQzLCA0NS45NTEzNTk2OTIwOTldLCBbLTY2LjY3NjA3NzU0MTM4NjgsIDQ1Ljk1MTk5Njc1MDQzMTZdLCBbLTY2LjY3NDY1ODIwMzIzNzksIDQ1Ljk1MjYzMzgwMTQ0MTVdLCBbLTY2LjY3MzM4MjU5NTUzNDQsIDQ1Ljk1MzQwODI0NTc0ODRdLCBbLTY2LjY3MjI5NTYzNDA0MDYsIDQ1Ljk1NDMwNzU4Njg0NjVdLCBbLTY2LjY3MTM5NzMxODc1NjUsIDQ1Ljk1NTMwNjgzNzYxNjJdLCBbLTY2LjY3MTAxMTA0MzE4NDMsIDQ1Ljk1NTk5MzgxMjA2ODVdLCBbLTY2LjY3MDc5NTQ0NzUxNjIsIDQ1Ljk1NjgxMTkyNTA3ODldLCBbLTY2LjY3MDgxMzQxMzgyMTgsIDQ1Ljk1NzY0ODc2MTAwNTRdLCBbLTY2LjY3MTA2NDk0MjEwMTQsIDQ1Ljk1ODQ2Njg0OTU4MjddXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDY5LCAiTmVpZ2hib3VyaCI6ICJIYW53ZWxsIE5vcnRoIiwgIk9CSkVDVElEIjogNjksICJTaGFwZV9BcmVhIjogNzQ3MjUxLjQ0NDgxOCwgIlNoYXBlX0xlbmciOiA0MzAxLjQzNDc0MDQ3LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjYxODEwOTI1NjEwMjUsIDQ1LjkwODIxMDA2MzY4MjNdLCBbLTY2LjYxODAwMTQ1ODI2ODUsIDQ1LjkwODI0MTMxNjUwNjRdLCBbLTY2LjYxOTI0MTEzMzM2MDUsIDQ1LjkwODQyMjU4MjUzODddLCBbLTY2LjYyMTE0NTU2MTc2MjksIDQ1LjkwODQ4NTA4NzkyOTldLCBbLTY2LjYyMjcwODYzMDM1NzIsIDQ1LjkwODM0MTMyNTQyNV0sIFstNjYuNjI0MjI2NzgzMTg3NCwgNDUuOTA4MDI4Nzk2OTU2XSwgWy02Ni42MjU2NTUxMDQ0ODkxLCA0NS45MDc1NTM3NTAzMTI5XSwgWy02Ni42MjY5NTc2NjE2NTExLCA0NS45MDY5Mjg2ODI3NDY2XSwgWy02Ni42MjgxMDc1MDUyMTQ4LCA0NS45MDYxNjYwOTA3ODM5XSwgWy02Ni42MjkyMzAzOTkzMiwgNDUuOTA1MDk3MTk0MjUyNV0sIFstNjYuNjMyNzUxNzk1MjMzNywgNDUuOTAwNzMzODgyNjYyXSwgWy02Ni42Mzg1OTA4NDQ1ODA1LCA0NS44OTQwNzU3MzM1NTgyXSwgWy02Ni42Mzg3NDM1NTgxNzg4LCA0NS44OTI1Njg5NDMwMzc4XSwgWy02Ni42Mzg1ODE4NjE0Mjc2LCA0NS44OTE4MTg2NTg2NTMyXSwgWy02Ni42MzgxNTk2NTMyNDQxLCA0NS44OTA5MTgzMDQwMTIzXSwgWy02Ni42MzcwMDk4MDk2ODA0LCA0NS44ODk2MzY1MjM5NjI0XSwgWy02Ni42MzYyNDYyNDE2ODg5LCA0NS44ODkwOTg3OTI3OTI0XSwgWy02Ni42MzUxNTAyOTcwNDIzLCA0NS44ODg1NDIyOTgwNzY5XSwgWy02Ni42MzMxNDcwNTM5NTg3LCA0NS44ODc5NzMyOTIwOTc0XSwgWy02Ni42MzA5OTEwOTcyNzY4LCA0NS44ODc4MzU3MjkzMzczXSwgWy02Ni42Mjg4NzEwNzMyMDYzLCA0NS44ODgxNDIxMTg2NTU1XSwgWy02Ni42MjY5NzU2Mjc5NTY4LCA0NS44ODg4Njc0NDE3MzM4XSwgWy02Ni42MjYzNDY4MDcyNTc5LCA0NS44ODkyMzYzNTI0MjQ0XSwgWy02Ni42MjQyODk2NjUyNTczLCA0NS44OTEyNjIxOTExODgyXSwgWy02Ni42MTkxNDIzMTg2NzkzLCA0NS44OTY4MzI4NjY3OTQ0XSwgWy02Ni42MTUwNjM5NjcyODk0LCA0NS45MDE4ODQxMjk4OV0sIFstNjYuNjE0NjUwNzQyMjU4NywgNDUuOTAzNDAzMTY5ODc1M10sIFstNjYuNjE0ODU3MzU0Nzc0LCA0NS45MDQ5NDA5MjExMDU0XSwgWy02Ni42MTU1NDAwNzQzOSwgNDUuOTA2MjA5ODQ2MzQzN10sIFstNjYuNjE2NjQ1MDAyMTg5NCwgNDUuOTA3MzIyNDc2MTMzN10sIFstNjYuNjE4MTA5MjU2MTAyNSwgNDUuOTA4MjEwMDYzNjgyM11dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogNzAsICJOZWlnaGJvdXJoIjogIkRvYWsgUm9hZCIsICJPQkpFQ1RJRCI6IDcwLCAiU2hhcGVfQXJlYSI6IDI1NjAxMzAuMTc2MDQsICJTaGFwZV9MZW5nIjogNjM1MC42NjEzODcwNCwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmVkOTc2IiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni42NTAzNTg3NzQ4MDI0LCA0NS45MzU3MTgyMzgyMDY5XSwgWy02Ni42NTAxNDMxNzkxMzQyLCA0NS45MzYxNTU1NTkyNTc4XSwgWy02Ni42NTAyNzc5MjY0MjY5LCA0NS45MzYzNTU0NzYzMDM4XSwgWy02Ni42NTAxNDMxNzkxMzQyLCA0NS45MzY2MDUzNzE1OTc4XSwgWy02Ni42NDU2Njk1NjkwMTkzLCA0NS45NDE5NDY2MTQyMTA2XSwgWy02Ni42NDYyMzU1MDc2NDgzLCA0NS45NDIzMzM5MTIzODA1XSwgWy02Ni42NTI0NTE4NDk0MTQ0LCA0NS45NDQ5MTk5OTUzMjU4XSwgWy02Ni42NTMzODYwOTczMDk5LCA0NS45NDM4NDU1OTg3MDJdLCBbLTY2LjY1NDYwNzgwNjA5NjMsIDQ1Ljk0MjkyNzM0Nzg3NTddLCBbLTY2LjY1NjU4NDA5OTcyMTQsIDQ1Ljk0MTk4NDA5NDc5NjldLCBbLTY2LjY1NzEzMjA3MjA0NDcsIDQ1Ljk0MTgwOTE4NTE3NzRdLCBbLTY2LjY1NzQxOTUzMjkzNTYsIDQ1Ljk0MTkwOTEzMzU5OV0sIFstNjYuNjU3NjQ0MTExNzU2NywgNDUuOTQxNTcxODA2OTU0MV0sIFstNjYuNjU2MTcwODc0NjkwNywgNDUuOTQwOTQ3MTIyNTYyNV0sIFstNjYuNjU5OTE2ODQ5NDI1NSwgNDUuOTM2NjM2NjA4NDMwNF0sIFstNjYuNjU1Nzc1NjE1OTY1NywgNDUuOTM1MzgwODczODk2OV0sIFstNjYuNjU0MTg1NTk3OTEyOCwgNDUuOTM1MTEyMjMwNDc4NV0sIFstNjYuNjUzMjUxMzUwMDE3MywgNDUuOTM1MDg3MjQwMzI2OV0sIFstNjYuNjUyMDc0NTU2OTk1MSwgNDUuOTM1MjI0Njg2MDIxM10sIFstNjYuNjUwMzU4Nzc0ODAyNCwgNDUuOTM1NzE4MjM4MjA2OV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogNzEsICJOZWlnaGJvdXJoIjogIk1vbnRvZ29tZXJ5IC8gUHJvc3BlY3QgRWFzdCIsICJPQkpFQ1RJRCI6IDcxLCAiU2hhcGVfQXJlYSI6IDY3ODI1MS4wNDI2MTgsICJTaGFwZV9MZW5nIjogMzQ4MS4zMzI4NTE0OSwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmVkOTc2IiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni41OTg2MDY4MzEyODQzLCA0NS44OTM0MzE3NTc1NDk4XSwgWy02Ni41OTAyMzQ1MzI4MzYzLCA0NS44ODQwNDYzNjY2NDYyXSwgWy02Ni41OTAzNTEzMTM4MjMyLCA0NS44ODQ0Mjc4MTU4NDUxXSwgWy02Ni41ODk5MzgwODg3OTI2LCA0NS44ODQ3NTI5ODM1ODU5XSwgWy02Ni41ODk0NjE5ODE2OTIsIDQ1Ljg4NDg0MDUyODQyMTddLCBbLTY2LjU4OTQ1Mjk5ODUzOTEsIDQ1Ljg4NTIyODIyNTMyMTldLCBbLTY2LjU4OTEyMDYyMTg4NCwgNDUuODg1MjkwNzU2ODI2Nl0sIFstNjYuNTg4NTcyNjQ5NTYwNywgNDUuODg1MDE1NjE3Njc5NF0sIFstNjYuNTg4MjY3MjIyMzY0MSwgNDUuODg1MzAzMjYzMTE5MV0sIFstNjYuNTg3ODE4MDY0NzIyLCA0NS44ODUwOTY5MDg5MzI5XSwgWy02Ni41ODcxNzEyNzc3MTc1LCA0NS44ODUyNDA3MzE2Mjg1XSwgWy02Ni41ODYyODE5NDU1ODYyLCA0NS44ODYwNjYxNDE2MzcxXSwgWy02Ni41ODU4OTU2NzAwMTQsIDQ1Ljg4NjcyODk2MjAwNzhdLCBbLTY2LjU4NjM4MDc2MDI2NzQsIDQ1Ljg4NjgxNjUwMzcyOTZdLCBbLTY2LjU4NjQ3MDU5MTc5NTgsIDQ1Ljg4NzMwNDIzMzY1NDRdLCBbLTY2LjU4Njk2NDY2NTIwMjEsIDQ1Ljg4NzY2NjkwMTg0OF0sIFstNjYuNTg2ODM4OTAxMDYyNCwgNDUuODg4MDU0NTc5MDIyOF0sIFstNjYuNTg2MzYyNzkzOTYxOCwgNDUuODg4Mjc5NjgwNjU2OF0sIFstNjYuNTg2MDIxNDM0MTUzOCwgNDUuODg4NzE3Mzc1NjY3MV0sIFstNjYuNTg2MTU2MTgxNDQ2NCwgNDUuODg5MDk4NzkyNzkyNF0sIFstNjYuNTg1NTkwMjQyODE3NCwgNDUuODg5NzkyODQwMTg2M10sIFstNjYuNTg1MDc4MjAzMTA1NSwgNDUuODkwMTMwNDgxNzI4N10sIFstNjYuNTg0ODQ0NjQxMTMxNiwgNDUuODkwMTA1NDcxMzE0NV0sIFstNjYuNTg0NTIxMjQ3NjI5MywgNDUuODg5ODY3ODcxODE3Nl0sIFstNjYuNTgzODI5NTQ0ODYwNSwgNDUuODkwMTk5MjYwMzA5OF0sIFstNjYuNTgzMDY1OTc2ODY5LCA0NS44ODk5MTc4OTI4NDg4XSwgWy02Ni41ODI3NTE1NjY1MTk2LCA0NS44OTAyNzQyOTEzOTJdLCBbLTY2LjU4MjMzODM0MTQ4ODksIDQ1Ljg5MDM4MDU4NTI1MTZdLCBbLTY2LjU4MTc2MzQxOTcwNzEsIDQ1Ljg5MDc2ODI0MzQ4NjVdLCBbLTY2LjU4MTU0NzgyNDAzODksIDQ1Ljg5MTM4NzI0MDU0MjRdLCBbLTY2LjU4MTkxNjEzMzMwNTQsIDQ1Ljg5MTU4NzMxODkyMzVdLCBbLTY2LjU4MTczNjQ3MDI0ODUsIDQ1Ljg5MTc5OTkwMTQxMzddLCBbLTY2LjU4MTIwNjQ2NDIzMDksIDQ1Ljg5MTgwNjE1MzgyNzVdLCBbLTY2LjU4MTI3ODMyOTQ1MzYsIDQ1Ljg5MjMzNzYwNjQzMzRdLCBbLTY2LjU4MDkwMTAzNzAzNDMsIDQ1Ljg5MjQzNzY0NDAwMjJdLCBbLTY2LjU4MDc2NjI4OTc0MTcsIDQ1Ljg5MjgwMDI3ODY3ODddLCBbLTY2LjU3NzM4ODYyNDI3MzQsIDQ1Ljg5NTM4MjQxOTIwODddLCBbLTY2LjU3Nzc5Mjg2NjE1MTMsIDQ1Ljg5NjcxNDA4MTU2M10sIFstNjYuNTc4MzEzODg5MDE2LCA0NS44OTc3ODkzOTEyMzg4XSwgWy02Ni41NzkzNjQ5MTc4OTg1LCA0NS44OTg0NDU4MjAwNDldLCBbLTY2LjU4MDIxODMxNzQxODQsIDQ1Ljg5ODc4MzQwODk4NjldLCBbLTY2LjU4MDMxNzEzMjA5OTYsIDQ1Ljg5OTA3MDk4MzEyOThdLCBbLTY2LjU3OTkyMTg3MzM3NDYsIDQ1Ljg5OTM4OTgxMzU5MDhdLCBbLTY2LjU3OTA5NTQyMzMxMzIsIDQ1Ljg5OTYyMTEyMDgxODZdLCBbLTY2LjU3OTA2ODQ3Mzg1NDcsIDQ1LjkwMDI1ODc3MzU5MThdLCBbLTY2LjU3ODg3OTgyNzY0NSwgNDUuOTAwNTMzODM3MjMzMl0sIFstNjYuNTc4NDM5NjUzMTU1OCwgNDUuOTAwNTcxMzQ1ODA2XSwgWy02Ni41NzgxMjUyNDI4MDY0LCA0NS45MDA0NDAwNjU2OTA0XSwgWy02Ni41ODAzODAwMTQxNjk1LCA0NS45MDI5MjgwODM2NDddLCBbLTY2LjU4MjMyOTM1ODMzNjEsIDQ1LjkwNDg0NzE1NzAwNTldLCBbLTY2LjU4NjYyMzMwNTM5NDIsIDQ1LjkwODQ4NTA4NzkyOTldLCBbLTY2LjU5NDUyODQ3OTg5NDQsIDQ1Ljg5OTQ1ODU4MDcwNTFdLCBbLTY2LjU5NDg2OTgzOTcwMjQsIDQ1Ljg5OTIxNDc2OTY0MjhdLCBbLTY2LjU5NTYzMzQwNzY5MzksIDQ1Ljg5ODc4MzQwODk4NjldLCBbLTY2LjU5NjcyMDM2OTE4NzcsIDQ1Ljg5ODM4MzMwMzM1MzhdLCBbLTY2LjU5NzY1NDYxNzA4MzEsIDQ1Ljg5ODE3Njk5Nzc2MDJdLCBbLTY2LjU5ODg2NzM0MjcxNjcsIDQ1Ljg5ODA4MzIyMjIzN10sIFstNjYuNjAwMzIyNjEzNDc3LCA0NS44OTgyMDgyNTYyMzI3XSwgWy02Ni42MDA2MzcwMjM4MjY0LCA0NS44OTkyMTQ3Njk2NDI4XSwgWy02Ni41OTk4NDY1MDYzNzY0LCA0NS44OTYyODg5NTMzODk0XSwgWy02Ni41OTg2MDY4MzEyODQzLCA0NS44OTM0MzE3NTc1NDk4XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiA3MiwgIk5laWdoYm91cmgiOiAiRnJlZGVyaWN0b24gU291dGgiLCAiT0JKRUNUSUQiOiA3MiwgIlNoYXBlX0FyZWEiOiAyNTA0MDY2Ljk0Mzk1LCAiU2hhcGVfTGVuZyI6IDc3MjIuNDc5MzQ2MDUsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZkOGQzYyIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjgwNTYwMTM0NjU0NSwgNDUuOTQ1NjU3MDY5MzM5MV0sIFstNjYuNjc5Mjc1NTQzNzk4MiwgNDUuOTQ3MDY4NzI2MTA3XSwgWy02Ni42NzkzMjk0NDI3MTUzLCA0NS45NDc2NzQ2MDMxNjNdLCBbLTY2LjY3OTA5NTg4MDc0MTQsIDQ1Ljk0NzkxMTk1NTI1NTldLCBbLTY2LjY2NzAwNDU1NzAxNzIsIDQ1Ljk0NjMzMTY3MDg2MzVdLCBbLTY2LjY2NzE3NTIzNjkyMTEsIDQ1Ljk0NzEwNjIwMzIzMDVdLCBbLTY2LjY2NzEzMDMyMTE1NjksIDQ1Ljk0NzczMDgxODIyNDJdLCBbLTY2LjY2Njg1MTg0MzQxODksIDQ1Ljk0ODQ5MjgzODk4NTNdLCBbLTY2LjY2NjQ1NjU4NDY5MzgsIDQ1Ljk0OTA2MTIyNDY5OTFdLCBbLTY2LjY2NTc2NDg4MTkyNTEsIDQ1Ljk0OTY3OTU3MTc2ODFdLCBbLTY2LjY2MDI4NTE1ODY5MTksIDQ1Ljk1NjAwMDA1NzI1MThdLCBbLTY2LjY1ODc0OTAzOTU1NjEsIDQ1Ljk1NjQxODQ4MjkyNTFdLCBbLTY2LjY1NzcwNjk5MzgyNjUsIDQ1Ljk1Njk4MDU0MjI4OThdLCBbLTY2LjY2MDExNDQ3ODc4OCwgNDUuOTU3MzczOTgwNDUzXSwgWy02Ni42NjA1MzY2ODY5NzE1LCA0NS45NTc1MzAxMDU5MzRdLCBbLTY2LjY2MTM5MDA4NjQ5MTQsIDQ1Ljk1ODE4NTgyODE1MDldLCBbLTY2LjY2MTY3NzU0NzM4MjMsIDQ1Ljk1ODkxNjQ4MDkwOTFdLCBbLTY2LjY2MzA5Njg4NTUzMTIsIDQ1Ljk1OTAxNjM5ODQ4NjFdLCBbLTY2LjY2NDQ2MjMyNDc2MzEsIDQ1Ljk1OTI3MjQzNjQ1NDldLCBbLTY2LjY2NzIyMDE1MjY4NTQsIDQ1Ljk2MDAyODA1MzgwNjFdLCBbLTY2LjY2ODYzMDUwNzY4MTQsIDQ1Ljk2MDc1ODY4MjI3MTldLCBbLTY2LjY2OTUxMDg1NjY1OTksIDQ1Ljk1OTI3MjQzNjQ1NDldLCBbLTY2LjY3MDA1ODgyODk4MzIsIDQ1Ljk1ODg1NDAzMjMzMTldLCBbLTY2LjY3MTA2NDk0MjEwMTQsIDQ1Ljk1ODQ2Njg0OTU4MjddLCBbLTY2LjY3MDc3NzQ4MTIxMDUsIDQ1Ljk1NzE0OTE1ODk4NzVdLCBbLTY2LjY3MTA4MjkwODQwNzEsIDQ1Ljk1NTgzMTQzNzA1NzVdLCBbLTY2LjY3MjA5ODAwNDY3ODEsIDQ1Ljk1NDUwMTE5MzA5MDRdLCBbLTY2LjY3MzYyNTE0MDY2MTEsIDQ1Ljk1MzI0NTg2MzE2MTRdLCBbLTY2LjY3NTQ5MzYzNjQ1MjEsIDQ1Ljk1MjIzNDA4NDAxNjZdLCBbLTY2LjY3NzkyODA3MDg3MjEsIDQ1Ljk1MTQyODM5NDgyMDVdLCBbLTY2LjY4MDU2OTExNzgwNzQsIDQ1Ljk1MTA0NzQwNTkyODJdLCBbLTY2LjY4MjY4OTE0MTg3NzksIDQ1Ljk1MTE1OTgyOTE1MjRdLCBbLTY2LjY4NTE3NzQ3NTIxNDksIDQ1Ljk1MTUyODMyNTg5OTddLCBbLTY2LjY4NzU1ODAxMDcxNzgsIDQ1Ljk1MjE0NjY0NTQ0NTZdLCBbLTY2LjY4ODA0MzEwMDk3MTIsIDQ1Ljk1MTc5Njg4OTc4MjJdLCBbLTY2LjY4OTM4MTU5MDc0NDYsIDQ1Ljk1MTgwOTM4MTA5MzldLCBbLTY2LjY5MDcwMjExNDIxMjIsIDQ1Ljk1MTk5Njc1MDQzMTZdLCBbLTY2LjY5Mjg4NTAyMDM1MjcsIDQ1Ljk1MjcwODc0ODEzNzddLCBbLTY2LjY5MzM3OTA5Mzc1ODksIDQ1Ljk1MzAyNzI3MDQ2Nl0sIFstNjYuNjkzNjM5NjA1MTkxMywgNDUuOTUzMzU4MjgxOTI2Ml0sIFstNjYuNjkzNzExNDcwNDE0LCA0NS45NTQwMTQwNTM1MDkxXSwgWy02Ni42OTMyOTgyNDUzODM0LCA0NS45NTQ3OTQ3MjM4NDc1XSwgWy02Ni42OTI1Nzk1OTMxNTYxLCA0NS45NTUwMDcwNjQyNzcxXSwgWy02Ni42OTE4NTE5NTc3NzU5LCA0NS45NTQ3OTQ3MjM4NDc1XSwgWy02Ni42OTE2ODEyNzc4NzE5LCA0NS45NTQ4Mzg0NDEwNjEzXSwgWy02Ni42OTA5MTc3MDk4ODA0LCA0NS45NTUxNDQ0NjA1OTIxXSwgWy02Ni42OTAzNjA3NTQ0MDQzLCA0NS45NTU1NzUzODMxODg3XSwgWy02Ni42ODk2MzMxMTkwMjQxLCA0NS45NTY1MzcxNDAzNzY4XSwgWy02Ni42ODgxNjg4NjUxMTEsIDQ1Ljk1OTM3ODU5ODE5MjVdLCBbLTY2LjY4NzY1NjgyNTM5OTEsIDQ1Ljk2MDAyODA1MzgwNjFdLCBbLTY2LjY4ODg3ODUzNDE4NTUsIDQ1Ljk1OTc3MjAxOTMyODldLCBbLTY2LjY5ODEyMjE5ODQ1OTEsIDQ1Ljk2MDgwODYzOTQyMl0sIFstNjYuNjk3MzQwNjY0MTYxOSwgNDUuOTYwMDc4MDExNjE0OV0sIFstNjYuNjk2Njc1OTEwODUxNiwgNDUuOTU5MDg1MDkxNzE1OF0sIFstNjYuNjk2NDYwMzE1MTgzNCwgNDUuOTU4NTU0Mjc4MTgxOV0sIFstNjYuNjk2NDk2MjQ3Nzk0OCwgNDUuOTU3NjIzNzgxMDExNV0sIFstNjYuNjk4Nzk1OTM0OTIyMiwgNDUuOTUxNzg0Mzk4NDY3N10sIFstNjYuNjk5MTczMjI3MzQxNSwgNDUuOTUxMTUzNTgzNDIzN10sIFstNjYuNzAwMjYwMTg4ODM1MywgNDUuOTUwNzY2MzQ2ODY5OV0sIFstNjYuNjk5ODkxODc5NTY4OCwgNDUuOTUwMzQxNjMyNzAwMV0sIFstNjYuNjk1NzIzNjk2NjUwNSwgNDUuOTUwNzE2MzgwNjY1OV0sIFstNjYuNjk1NjY5Nzk3NzMzNCwgNDUuOTUwNDQ3ODExNTQ3Nl0sIFstNjYuNjkzODAxMzAxOTQyNCwgNDUuOTUwNDM1MzE5OTI5MV0sIFstNjYuNjkxOTU5NzU1NjEsIDQ1Ljk1MDE0ODAxMTkyNV0sIFstNjYuNjkwMTcyMTA4MTk0NiwgNDUuOTQ5NTc5NjM3MzU1Nl0sIFstNjYuNjgwODIwNjQ2MDg2OSwgNDUuOTQ1NjEzMzQ0ODgzXSwgWy02Ni42ODA1NjAxMzQ2NTQ1LCA0NS45NDU2NTcwNjkzMzkxXV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiA3MywgIk5laWdoYm91cmgiOiAiRnJlZGVyaWN0b24gU291dGgiLCAiT0JKRUNUSUQiOiA3MywgIlNoYXBlX0FyZWEiOiAyMjI3Njg5LjMwNDczLCAiU2hhcGVfTGVuZyI6IDExMTQ4LjE5OTE3NzQsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZkOGQzYyIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjc0NzkyOTUwNTMwNSwgNDUuOTYyMjAxMTc2ODUxMl0sIFstNjYuNjc0Mjg5ODkzOTcxNCwgNDUuOTYxNzA3ODYwNDJdLCBbLTY2LjY3MzU5ODE5MTIwMjYsIDQ1Ljk2MTM3MDY1NDI1Nl0sIFstNjYuNjcyNzg5NzA3NDQ2OSwgNDUuOTYxMTg5NTYxMjA5OF0sIFstNjYuNjcxOTQ1MjkxMDc5OCwgNDUuOTYxMTc3MDcyMDEyNF0sIFstNjYuNjY5ODc5MTY1OTI2MywgNDUuOTYxNTUxNzQ2NzEwM10sIFstNjYuNjY3ODEzMDQwNzcyOSwgNDUuOTYyMjQ0ODg4MjIxOV0sIFstNjYuNjYwODUxMDk3MzIwOSwgNDUuOTYzOTgwODI2MjAzOV0sIFstNjYuNjU4NjA1MzA5MTEwNiwgNDUuOTY0MTYxOTEwMTI2NV0sIFstNjYuNjU2ODM1NjI4MDAwOSwgNDUuOTYzOTk5NTU5MDUwOV0sIFstNjYuNjU0MTU4NjQ4NDU0MywgNDUuOTYzNTgxMTkwNjI0OV0sIFstNjYuNjUyMDkyNTIzMzAwOCwgNDUuOTYzNDU2MzAzOTE1Ml0sIFstNjYuNjUxNDU0NzE5NDQ5MSwgNDUuOTYzNTYyNDU3NjM2NF0sIFstNjYuNjUxMDA1NTYxODA3LCA0NS45NjM3NjIyNzU4NTM4XSwgWy02Ni42NTA1OTIzMzY3NzYzLCA0NS45NjQxMTgyMDAyNjgzXSwgWy02Ni42NTA0MTI2NzM3MTk1LCA0NS45NjQ0Njc4NzgxNjhdLCBbLTY2LjY1MDk1MTY2Mjg5LCA0NS45NjQ5NDI0Mzc1MDE1XSwgWy02Ni42NTE1ODA0ODM1ODg4LCA0NS45NjUxOTg0NDgwODU1XSwgWy02Ni42NTIyOTAxNTI2NjMzLCA0NS45NjUzMDQ1OTg0Njg0XSwgWy02Ni42NTMwMTc3ODgwNDM0LCA0NS45NjUyNDIxNTcwOTEzXSwgWy02Ni42NTQ2NzA2ODgxNjYyLCA0NS45NjU1MDQ0MTA0MDIyXSwgWy02Ni42NTYyNTE3MjMwNjYzLCA0NS45NjU5MjkwMDgzNjg0XSwgWy02Ni42NTc3MzM5NDMyODUxLCA0NS45NjY1MDM0NTkyNjA0XSwgWy02Ni42NTk3NzMxMTg5OCwgNDUuOTY2MjM0OTY2NjUwMl0sIFstNjYuNjYwOTg1ODQ0NjEzNiwgNDUuOTY1ODY2NTY3Njk1Ml0sIFstNjYuNjYyNjQ3NzI3ODg5MiwgNDUuOTY1NjIzMDQ4Mzk2OF0sIFstNjYuNjY0MzA5NjExMTY0OCwgNDUuOTY1MDQ4NTg4Mzc1MV0sIFstNjYuNjY2MTA2MjQxNzMzMSwgNDUuOTY0NjU1MjA0NzA2NF0sIFstNjYuNjY2MjU4OTU1MzMxNCwgNDUuOTY0NDYxNjMzOTM5Ml0sIFstNjYuNjY2NTE5NDY2NzYzNywgNDUuOTY0NTU1Mjk3Mjk4MV0sIFstNjYuNjY5NDIxMDI1MTMxNCwgNDUuOTY0MTgwNjQyOTEyM10sIFstNjYuNjcwODY3MzEyNzM4OSwgNDUuOTY0MDk5NDY3NDYxNF0sIFstNjYuNjczNjg4MDIyNzMxLCA0NS45NjQyMTE4NjQyMDc5XSwgWy02Ni42NzQ3OTI5NTA1MzA1LCA0NS45NjIyMDExNzY4NTEyXV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiA3NCwgIk5laWdoYm91cmgiOiAiV29vZHN0b2NrIFJvYWQiLCAiT0JKRUNUSUQiOiA3NCwgIlNoYXBlX0FyZWEiOiA0Mzk3NjMuOTMyNTQzLCAiU2hhcGVfTGVuZyI6IDQyNDAuMzk5MTQ5MDYsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlYjI0YyIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifV0sICJ0eXBlIjogIkZlYXR1cmVDb2xsZWN0aW9uIn0KICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8yYjI0ZDRhYzcxYzY0NjU1OTIzM2U5OWNiNTRlM2U5Mik7CiAgICAgICAgICAgICAgICBnZW9fanNvbl85NjY2NDA5ZDEyNmE0OTI1OTUzYmQ3YTY0ZGNkMWRlMy5zZXRTdHlsZShmdW5jdGlvbihmZWF0dXJlKSB7cmV0dXJuIGZlYXR1cmUucHJvcGVydGllcy5zdHlsZTt9KTsKCiAgICAgICAgICAgIAogICAgCiAgICB2YXIgY29sb3JfbWFwXzU3YTVkMDQxN2FlNDQ4ZmJiNzRlM2JjYmE2NGZiZWU2ID0ge307CgogICAgCiAgICBjb2xvcl9tYXBfNTdhNWQwNDE3YWU0NDhmYmI3NGUzYmNiYTY0ZmJlZTYuY29sb3IgPSBkMy5zY2FsZS50aHJlc2hvbGQoKQogICAgICAgICAgICAgIC5kb21haW4oWzEuMCwgMS4zOTY3OTM1ODcxNzQzNDg2LCAxLjc5MzU4NzE3NDM0ODY5NzMsIDIuMTkwMzgwNzYxNTIzMDQ2LCAyLjU4NzE3NDM0ODY5NzM5NDYsIDIuOTgzOTY3OTM1ODcxNzQzNSwgMy4zODA3NjE1MjMwNDYwOTIzLCAzLjc3NzU1NTExMDIyMDQ0MDgsIDQuMTc0MzQ4Njk3Mzk0Nzg5LCA0LjU3MTE0MjI4NDU2OTEzOCwgNC45Njc5MzU4NzE3NDM0ODcsIDUuMzY0NzI5NDU4OTE3ODM2LCA1Ljc2MTUyMzA0NjA5MjE4NSwgNi4xNTgzMTY2MzMyNjY1MzMsIDYuNTU1MTEwMjIwNDQwODgxNSwgNi45NTE5MDM4MDc2MTUyMywgNy4zNDg2OTczOTQ3ODk1NzksIDcuNzQ1NDkwOTgxOTYzOTI4LCA4LjE0MjI4NDU2OTEzODI3NiwgOC41MzkwNzgxNTYzMTI2MjUsIDguOTM1ODcxNzQzNDg2OTc0LCA5LjMzMjY2NTMzMDY2MTMyMywgOS43Mjk0NTg5MTc4MzU2NzIsIDEwLjEyNjI1MjUwNTAxMDAyLCAxMC41MjMwNDYwOTIxODQzNywgMTAuOTE5ODM5Njc5MzU4NzE4LCAxMS4zMTY2MzMyNjY1MzMwNjUsIDExLjcxMzQyNjg1MzcwNzQxNCwgMTIuMTEwMjIwNDQwODgxNzYzLCAxMi41MDcwMTQwMjgwNTYxMTIsIDEyLjkwMzgwNzYxNTIzMDQ2LCAxMy4zMDA2MDEyMDI0MDQ4MSwgMTMuNjk3Mzk0Nzg5NTc5MTU5LCAxNC4wOTQxODgzNzY3NTM1MDcsIDE0LjQ5MDk4MTk2MzkyNzg1NiwgMTQuODg3Nzc1NTUxMTAyMjA1LCAxNS4yODQ1NjkxMzgyNzY1NTIsIDE1LjY4MTM2MjcyNTQ1MDkwMSwgMTYuMDc4MTU2MzEyNjI1MjUsIDE2LjQ3NDk0OTg5OTc5OTU5NywgMTYuODcxNzQzNDg2OTczOTQ4LCAxNy4yNjg1MzcwNzQxNDgyOTUsIDE3LjY2NTMzMDY2MTMyMjY0NiwgMTguMDYyMTI0MjQ4NDk2OTkzLCAxOC40NTg5MTc4MzU2NzEzNDMsIDE4Ljg1NTcxMTQyMjg0NTY5LCAxOS4yNTI1MDUwMTAwMjAwNCwgMTkuNjQ5Mjk4NTk3MTk0Mzg4LCAyMC4wNDYwOTIxODQzNjg3NCwgMjAuNDQyODg1NzcxNTQzMDg2LCAyMC44Mzk2NzkzNTg3MTc0MzYsIDIxLjIzNjQ3Mjk0NTg5MTc4NCwgMjEuNjMzMjY2NTMzMDY2MTMsIDIyLjAzMDA2MDEyMDI0MDQ4LCAyMi40MjY4NTM3MDc0MTQ4MywgMjIuODIzNjQ3Mjk0NTg5MTgsIDIzLjIyMDQ0MDg4MTc2MzUyNiwgMjMuNjE3MjM0NDY4OTM3ODc3LCAyNC4wMTQwMjgwNTYxMTIyMjQsIDI0LjQxMDgyMTY0MzI4NjU3NSwgMjQuODA3NjE1MjMwNDYwOTIsIDI1LjIwNDQwODgxNzYzNTI3MiwgMjUuNjAxMjAyNDA0ODA5NjIsIDI1Ljk5Nzk5NTk5MTk4Mzk2NiwgMjYuMzk0Nzg5NTc5MTU4MzE3LCAyNi43OTE1ODMxNjYzMzI2NjQsIDI3LjE4ODM3Njc1MzUwNzAxNSwgMjcuNTg1MTcwMzQwNjgxMzYyLCAyNy45ODE5NjM5Mjc4NTU3MTMsIDI4LjM3ODc1NzUxNTAzMDA2LCAyOC43NzU1NTExMDIyMDQ0MSwgMjkuMTcyMzQ0Njg5Mzc4NzU3LCAyOS41NjkxMzgyNzY1NTMxMDUsIDI5Ljk2NTkzMTg2MzcyNzQ1NSwgMzAuMzYyNzI1NDUwOTAxODAyLCAzMC43NTk1MTkwMzgwNzYxNTMsIDMxLjE1NjMxMjYyNTI1MDUsIDMxLjU1MzEwNjIxMjQyNDg1LCAzMS45NDk4OTk3OTk1OTkxOTgsIDMyLjM0NjY5MzM4Njc3MzU1LCAzMi43NDM0ODY5NzM5NDc4OTYsIDMzLjE0MDI4MDU2MTEyMjI0NiwgMzMuNTM3MDc0MTQ4Mjk2NTksIDMzLjkzMzg2NzczNTQ3MDk0LCAzNC4zMzA2NjEzMjI2NDUyOSwgMzQuNzI3NDU0OTA5ODE5NjQsIDM1LjEyNDI0ODQ5Njk5Mzk4NSwgMzUuNTIxMDQyMDg0MTY4MzM2LCAzNS45MTc4MzU2NzEzNDI2OSwgMzYuMzE0NjI5MjU4NTE3MDQsIDM2LjcxMTQyMjg0NTY5MTM4LCAzNy4xMDgyMTY0MzI4NjU3MywgMzcuNTA1MDEwMDIwMDQwMDgsIDM3LjkwMTgwMzYwNzIxNDQyNiwgMzguMjk4NTk3MTk0Mzg4Nzc2LCAzOC42OTUzOTA3ODE1NjMxMywgMzkuMDkyMTg0MzY4NzM3NDgsIDM5LjQ4ODk3Nzk1NTkxMTgyLCAzOS44ODU3NzE1NDMwODYxNywgNDAuMjgyNTY1MTMwMjYwNTIsIDQwLjY3OTM1ODcxNzQzNDg3LCA0MS4wNzYxNTIzMDQ2MDkyMiwgNDEuNDcyOTQ1ODkxNzgzNTcsIDQxLjg2OTczOTQ3ODk1NzkyLCA0Mi4yNjY1MzMwNjYxMzIyNiwgNDIuNjYzMzI2NjUzMzA2NjEsIDQzLjA2MDEyMDI0MDQ4MDk2LCA0My40NTY5MTM4Mjc2NTUzMSwgNDMuODUzNzA3NDE0ODI5NjYsIDQ0LjI1MDUwMTAwMjAwNDAxLCA0NC42NDcyOTQ1ODkxNzgzNiwgNDUuMDQ0MDg4MTc2MzUyNzEsIDQ1LjQ0MDg4MTc2MzUyNzA1LCA0NS44Mzc2NzUzNTA3MDE0LCA0Ni4yMzQ0Njg5Mzc4NzU3NTQsIDQ2LjYzMTI2MjUyNTA1MDEsIDQ3LjAyODA1NjExMjIyNDQ1LCA0Ny40MjQ4NDk2OTkzOTg4LCA0Ny44MjE2NDMyODY1NzMxNSwgNDguMjE4NDM2ODczNzQ3NDksIDQ4LjYxNTIzMDQ2MDkyMTg0LCA0OS4wMTIwMjQwNDgwOTYxOTQsIDQ5LjQwODgxNzYzNTI3MDU0NSwgNDkuODA1NjExMjIyNDQ0ODksIDUwLjIwMjQwNDgwOTYxOTI0LCA1MC41OTkxOTgzOTY3OTM1OSwgNTAuOTk1OTkxOTgzOTY3OTMsIDUxLjM5Mjc4NTU3MTE0MjI4NCwgNTEuNzg5NTc5MTU4MzE2NjM0LCA1Mi4xODYzNzI3NDU0OTA5ODUsIDUyLjU4MzE2NjMzMjY2NTMzLCA1Mi45Nzk5NTk5MTk4Mzk2OCwgNTMuMzc2NzUzNTA3MDE0MDMsIDUzLjc3MzU0NzA5NDE4ODM3LCA1NC4xNzAzNDA2ODEzNjI3MjQsIDU0LjU2NzEzNDI2ODUzNzA3NSwgNTQuOTYzOTI3ODU1NzExNDI1LCA1NS4zNjA3MjE0NDI4ODU3NywgNTUuNzU3NTE1MDMwMDYwMTIsIDU2LjE1NDMwODYxNzIzNDQ3LCA1Ni41NTExMDIyMDQ0MDg4MiwgNTYuOTQ3ODk1NzkxNTgzMTY0LCA1Ny4zNDQ2ODkzNzg3NTc1MTUsIDU3Ljc0MTQ4Mjk2NTkzMTg2NiwgNTguMTM4Mjc2NTUzMTA2MjEsIDU4LjUzNTA3MDE0MDI4MDU2LCA1OC45MzE4NjM3Mjc0NTQ5MSwgNTkuMzI4NjU3MzE0NjI5MjYsIDU5LjcyNTQ1MDkwMTgwMzYwNSwgNjAuMTIyMjQ0NDg4OTc3OTU1LCA2MC41MTkwMzgwNzYxNTIzMDYsIDYwLjkxNTgzMTY2MzMyNjY2LCA2MS4zMTI2MjUyNTA1MDEsIDYxLjcwOTQxODgzNzY3NTM1LCA2Mi4xMDYyMTI0MjQ4NDk3LCA2Mi41MDMwMDYwMTIwMjQwNDUsIDYyLjg5OTc5OTU5OTE5ODM5NiwgNjMuMjk2NTkzMTg2MzcyNzQ2LCA2My42OTMzODY3NzM1NDcxLCA2NC4wOTAxODAzNjA3MjE0MywgNjQuNDg2OTczOTQ3ODk1NzksIDY0Ljg4Mzc2NzUzNTA3MDE1LCA2NS4yODA1NjExMjIyNDQ0OSwgNjUuNjc3MzU0NzA5NDE4ODQsIDY2LjA3NDE0ODI5NjU5MzE4LCA2Ni40NzA5NDE4ODM3Njc1NCwgNjYuODY3NzM1NDcwOTQxODgsIDY3LjI2NDUyOTA1ODExNjI0LCA2Ny42NjEzMjI2NDUyOTA1OCwgNjguMDU4MTE2MjMyNDY0OTMsIDY4LjQ1NDkwOTgxOTYzOTI4LCA2OC44NTE3MDM0MDY4MTM2MywgNjkuMjQ4NDk2OTkzOTg3OTcsIDY5LjY0NTI5MDU4MTE2MjMzLCA3MC4wNDIwODQxNjgzMzY2NywgNzAuNDM4ODc3NzU1NTExMDIsIDcwLjgzNTY3MTM0MjY4NTM3LCA3MS4yMzI0NjQ5Mjk4NTk3MiwgNzEuNjI5MjU4NTE3MDM0MDcsIDcyLjAyNjA1MjEwNDIwODQyLCA3Mi40MjI4NDU2OTEzODI3NiwgNzIuODE5NjM5Mjc4NTU3MTIsIDczLjIxNjQzMjg2NTczMTQ2LCA3My42MTMyMjY0NTI5MDU4LCA3NC4wMTAwMjAwNDAwODAxNiwgNzQuNDA2ODEzNjI3MjU0NTEsIDc0LjgwMzYwNzIxNDQyODg1LCA3NS4yMDA0MDA4MDE2MDMyMSwgNzUuNTk3MTk0Mzg4Nzc3NTUsIDc1Ljk5Mzk4Nzk3NTk1MTkxLCA3Ni4zOTA3ODE1NjMxMjYyNSwgNzYuNzg3NTc1MTUwMzAwNiwgNzcuMTg0MzY4NzM3NDc0OTUsIDc3LjU4MTE2MjMyNDY0OTMsIDc3Ljk3Nzk1NTkxMTgyMzY0LCA3OC4zNzQ3NDk0OTg5OTgsIDc4Ljc3MTU0MzA4NjE3MjM0LCA3OS4xNjgzMzY2NzMzNDY2OSwgNzkuNTY1MTMwMjYwNTIxMDQsIDc5Ljk2MTkyMzg0NzY5NTM5LCA4MC4zNTg3MTc0MzQ4Njk3NSwgODAuNzU1NTExMDIyMDQ0MDksIDgxLjE1MjMwNDYwOTIxODQzLCA4MS41NDkwOTgxOTYzOTI3OSwgODEuOTQ1ODkxNzgzNTY3MTMsIDgyLjM0MjY4NTM3MDc0MTQ4LCA4Mi43Mzk0Nzg5NTc5MTU4NCwgODMuMTM2MjcyNTQ1MDkwMTgsIDgzLjUzMzA2NjEzMjI2NDUyLCA4My45Mjk4NTk3MTk0Mzg4OCwgODQuMzI2NjUzMzA2NjEzMjIsIDg0LjcyMzQ0Njg5Mzc4NzU4LCA4NS4xMjAyNDA0ODA5NjE5MywgODUuNTE3MDM0MDY4MTM2MjcsIDg1LjkxMzgyNzY1NTMxMDYzLCA4Ni4zMTA2MjEyNDI0ODQ5NywgODYuNzA3NDE0ODI5NjU5MzEsIDg3LjEwNDIwODQxNjgzMzY3LCA4Ny41MDEwMDIwMDQwMDgwMSwgODcuODk3Nzk1NTkxMTgyMzYsIDg4LjI5NDU4OTE3ODM1NjcyLCA4OC42OTEzODI3NjU1MzEwNiwgODkuMDg4MTc2MzUyNzA1NDIsIDg5LjQ4NDk2OTkzOTg3OTc2LCA4OS44ODE3NjM1MjcwNTQxLCA5MC4yNzg1NTcxMTQyMjg0NiwgOTAuNjc1MzUwNzAxNDAyOCwgOTEuMDcyMTQ0Mjg4NTc3MTUsIDkxLjQ2ODkzNzg3NTc1MTUxLCA5MS44NjU3MzE0NjI5MjU4NSwgOTIuMjYyNTI1MDUwMTAwMiwgOTIuNjU5MzE4NjM3Mjc0NTUsIDkzLjA1NjExMjIyNDQ0ODksIDkzLjQ1MjkwNTgxMTYyMzI1LCA5My44NDk2OTkzOTg3OTc2LCA5NC4yNDY0OTI5ODU5NzE5NCwgOTQuNjQzMjg2NTczMTQ2MywgOTUuMDQwMDgwMTYwMzIwNjQsIDk1LjQzNjg3Mzc0NzQ5NDk5LCA5NS44MzM2NjczMzQ2NjkzNCwgOTYuMjMwNDYwOTIxODQzNjksIDk2LjYyNzI1NDUwOTAxODAzLCA5Ny4wMjQwNDgwOTYxOTIzOSwgOTcuNDIwODQxNjgzMzY2NzMsIDk3LjgxNzYzNTI3MDU0MTA5LCA5OC4yMTQ0Mjg4NTc3MTU0MywgOTguNjExMjIyNDQ0ODg5NzgsIDk5LjAwODAxNjAzMjA2NDEzLCA5OS40MDQ4MDk2MTkyMzg0OCwgOTkuODAxNjAzMjA2NDEyODIsIDEwMC4xOTgzOTY3OTM1ODcxOCwgMTAwLjU5NTE5MDM4MDc2MTUyLCAxMDAuOTkxOTgzOTY3OTM1ODcsIDEwMS4zODg3Nzc1NTUxMTAyMiwgMTAxLjc4NTU3MTE0MjI4NDU3LCAxMDIuMTgyMzY0NzI5NDU4OTEsIDEwMi41NzkxNTgzMTY2MzMyNywgMTAyLjk3NTk1MTkwMzgwNzYxLCAxMDMuMzcyNzQ1NDkwOTgxOTcsIDEwMy43Njk1MzkwNzgxNTYzMSwgMTA0LjE2NjMzMjY2NTMzMDY2LCAxMDQuNTYzMTI2MjUyNTA1MDEsIDEwNC45NTk5MTk4Mzk2NzkzNiwgMTA1LjM1NjcxMzQyNjg1MzcsIDEwNS43NTM1MDcwMTQwMjgwNiwgMTA2LjE1MDMwMDYwMTIwMjQsIDEwNi41NDcwOTQxODgzNzY3NSwgMTA2Ljk0Mzg4Nzc3NTU1MTEsIDEwNy4zNDA2ODEzNjI3MjU0NSwgMTA3LjczNzQ3NDk0OTg5OTgsIDEwOC4xMzQyNjg1MzcwNzQxNSwgMTA4LjUzMTA2MjEyNDI0ODQ5LCAxMDguOTI3ODU1NzExNDIyODUsIDEwOS4zMjQ2NDkyOTg1OTcyLCAxMDkuNzIxNDQyODg1NzcxNTQsIDExMC4xMTgyMzY0NzI5NDU5LCAxMTAuNTE1MDMwMDYwMTIwMjQsIDExMC45MTE4MjM2NDcyOTQ1OCwgMTExLjMwODYxNzIzNDQ2ODk0LCAxMTEuNzA1NDEwODIxNjQzMjgsIDExMi4xMDIyMDQ0MDg4MTc2NCwgMTEyLjQ5ODk5Nzk5NTk5MTk5LCAxMTIuODk1NzkxNTgzMTY2MzMsIDExMy4yOTI1ODUxNzAzNDA2OSwgMTEzLjY4OTM3ODc1NzUxNTAzLCAxMTQuMDg2MTcyMzQ0Njg5MzcsIDExNC40ODI5NjU5MzE4NjM3MywgMTE0Ljg3OTc1OTUxOTAzODA3LCAxMTUuMjc2NTUzMTA2MjEyNDIsIDExNS42NzMzNDY2OTMzODY3OCwgMTE2LjA3MDE0MDI4MDU2MTEyLCAxMTYuNDY2OTMzODY3NzM1NDgsIDExNi44NjM3Mjc0NTQ5MDk4MiwgMTE3LjI2MDUyMTA0MjA4NDE2LCAxMTcuNjU3MzE0NjI5MjU4NTIsIDExOC4wNTQxMDgyMTY0MzI4NywgMTE4LjQ1MDkwMTgwMzYwNzIxLCAxMTguODQ3Njk1MzkwNzgxNTcsIDExOS4yNDQ0ODg5Nzc5NTU5MSwgMTE5LjY0MTI4MjU2NTEzMDI1LCAxMjAuMDM4MDc2MTUyMzA0NjEsIDEyMC40MzQ4Njk3Mzk0Nzg5NiwgMTIwLjgzMTY2MzMyNjY1MzMxLCAxMjEuMjI4NDU2OTEzODI3NjYsIDEyMS42MjUyNTA1MDEwMDIsIDEyMi4wMjIwNDQwODgxNzYzNiwgMTIyLjQxODgzNzY3NTM1MDcsIDEyMi44MTU2MzEyNjI1MjUwNSwgMTIzLjIxMjQyNDg0OTY5OTQsIDEyMy42MDkyMTg0MzY4NzM3NSwgMTI0LjAwNjAxMjAyNDA0ODA5LCAxMjQuNDAyODA1NjExMjIyNDUsIDEyNC43OTk1OTkxOTgzOTY3OSwgMTI1LjE5NjM5Mjc4NTU3MTE1LCAxMjUuNTkzMTg2MzcyNzQ1NDksIDEyNS45ODk5Nzk5NTk5MTk4NCwgMTI2LjM4Njc3MzU0NzA5NDIsIDEyNi43ODM1NjcxMzQyNjg1NCwgMTI3LjE4MDM2MDcyMTQ0Mjg4LCAxMjcuNTc3MTU0MzA4NjE3MjQsIDEyNy45NzM5NDc4OTU3OTE1OCwgMTI4LjM3MDc0MTQ4Mjk2NTksIDEyOC43Njc1MzUwNzAxNDAzLCAxMjkuMTY0MzI4NjU3MzE0NjMsIDEyOS41NjExMjIyNDQ0ODg5OCwgMTI5Ljk1NzkxNTgzMTY2MzMsIDEzMC4zNTQ3MDk0MTg4Mzc2NywgMTMwLjc1MTUwMzAwNjAxMjAzLCAxMzEuMTQ4Mjk2NTkzMTg2MzYsIDEzMS41NDUwOTAxODAzNjA3MiwgMTMxLjk0MTg4Mzc2NzUzNTA3LCAxMzIuMzM4Njc3MzU0NzA5NDMsIDEzMi43MzU0NzA5NDE4ODM3NiwgMTMzLjEzMjI2NDUyOTA1ODEyLCAxMzMuNTI5MDU4MTE2MjMyNDgsIDEzMy45MjU4NTE3MDM0MDY4LCAxMzQuMzIyNjQ1MjkwNTgxMTYsIDEzNC43MTk0Mzg4Nzc3NTU1MiwgMTM1LjExNjIzMjQ2NDkyOTg1LCAxMzUuNTEzMDI2MDUyMTA0MiwgMTM1LjkwOTgxOTYzOTI3ODU3LCAxMzYuMzA2NjEzMjI2NDUyOSwgMTM2LjcwMzQwNjgxMzYyNzI1LCAxMzcuMTAwMjAwNDAwODAxNiwgMTM3LjQ5Njk5Mzk4Nzk3NTk0LCAxMzcuODkzNzg3NTc1MTUwMywgMTM4LjI5MDU4MTE2MjMyNDY2LCAxMzguNjg3Mzc0NzQ5NDk4OTksIDEzOS4wODQxNjgzMzY2NzMzNCwgMTM5LjQ4MDk2MTkyMzg0NzcsIDEzOS44Nzc3NTU1MTEwMjIwMywgMTQwLjI3NDU0OTA5ODE5NjQsIDE0MC42NzEzNDI2ODUzNzA3NSwgMTQxLjA2ODEzNjI3MjU0NTEsIDE0MS40NjQ5Mjk4NTk3MTk0MywgMTQxLjg2MTcyMzQ0Njg5MzgsIDE0Mi4yNTg1MTcwMzQwNjgxNSwgMTQyLjY1NTMxMDYyMTI0MjQ4LCAxNDMuMDUyMTA0MjA4NDE2ODQsIDE0My40NDg4OTc3OTU1OTEyLCAxNDMuODQ1NjkxMzgyNzY1NTIsIDE0NC4yNDI0ODQ5Njk5Mzk4OCwgMTQ0LjYzOTI3ODU1NzExNDI0LCAxNDUuMDM2MDcyMTQ0Mjg4NTcsIDE0NS40MzI4NjU3MzE0NjI5MywgMTQ1LjgyOTY1OTMxODYzNzI4LCAxNDYuMjI2NDUyOTA1ODExNiwgMTQ2LjYyMzI0NjQ5Mjk4NTk3LCAxNDcuMDIwMDQwMDgwMTYwMzMsIDE0Ny40MTY4MzM2NjczMzQ2NiwgMTQ3LjgxMzYyNzI1NDUwOTAyLCAxNDguMjEwNDIwODQxNjgzMzcsIDE0OC42MDcyMTQ0Mjg4NTc3LCAxNDkuMDA0MDA4MDE2MDMyMDYsIDE0OS40MDA4MDE2MDMyMDY0MiwgMTQ5Ljc5NzU5NTE5MDM4MDc4LCAxNTAuMTk0Mzg4Nzc3NTU1MSwgMTUwLjU5MTE4MjM2NDcyOTQ2LCAxNTAuOTg3OTc1OTUxOTAzODIsIDE1MS4zODQ3Njk1MzkwNzgxNSwgMTUxLjc4MTU2MzEyNjI1MjUsIDE1Mi4xNzgzNTY3MTM0MjY4NywgMTUyLjU3NTE1MDMwMDYwMTIsIDE1Mi45NzE5NDM4ODc3NzU1NSwgMTUzLjM2ODczNzQ3NDk0OTksIDE1My43NjU1MzEwNjIxMjQyNCwgMTU0LjE2MjMyNDY0OTI5ODYsIDE1NC41NTkxMTgyMzY0NzI5NSwgMTU0Ljk1NTkxMTgyMzY0NzI4LCAxNTUuMzUyNzA1NDEwODIxNjQsIDE1NS43NDk0OTg5OTc5OTYsIDE1Ni4xNDYyOTI1ODUxNzAzMywgMTU2LjU0MzA4NjE3MjM0NDcsIDE1Ni45Mzk4Nzk3NTk1MTkwNCwgMTU3LjMzNjY3MzM0NjY5MzM3LCAxNTcuNzMzNDY2OTMzODY3NzMsIDE1OC4xMzAyNjA1MjEwNDIxLCAxNTguNTI3MDU0MTA4MjE2NDUsIDE1OC45MjM4NDc2OTUzOTA3OCwgMTU5LjMyMDY0MTI4MjU2NTEzLCAxNTkuNzE3NDM0ODY5NzM5NSwgMTYwLjExNDIyODQ1NjkxMzgyLCAxNjAuNTExMDIyMDQ0MDg4MTgsIDE2MC45MDc4MTU2MzEyNjI1NCwgMTYxLjMwNDYwOTIxODQzNjg3LCAxNjEuNzAxNDAyODA1NjExMjIsIDE2Mi4wOTgxOTYzOTI3ODU1OCwgMTYyLjQ5NDk4OTk3OTk1OTksIDE2Mi44OTE3ODM1NjcxMzQyNywgMTYzLjI4ODU3NzE1NDMwODYzLCAxNjMuNjg1MzcwNzQxNDgyOTYsIDE2NC4wODIxNjQzMjg2NTczLCAxNjQuNDc4OTU3OTE1ODMxNjcsIDE2NC44NzU3NTE1MDMwMDYsIDE2NS4yNzI1NDUwOTAxODAzNiwgMTY1LjY2OTMzODY3NzM1NDcyLCAxNjYuMDY2MTMyMjY0NTI5MDUsIDE2Ni40NjI5MjU4NTE3MDM0LCAxNjYuODU5NzE5NDM4ODc3NzYsIDE2Ny4yNTY1MTMwMjYwNTIxLCAxNjcuNjUzMzA2NjEzMjI2NDUsIDE2OC4wNTAxMDAyMDA0MDA4LCAxNjguNDQ2ODkzNzg3NTc1MTYsIDE2OC44NDM2ODczNzQ3NDk1LCAxNjkuMjQwNDgwOTYxOTIzODUsIDE2OS42MzcyNzQ1NDkwOTgyLCAxNzAuMDM0MDY4MTM2MjcyNTQsIDE3MC40MzA4NjE3MjM0NDY5LCAxNzAuODI3NjU1MzEwNjIxMjUsIDE3MS4yMjQ0NDg4OTc3OTU1OCwgMTcxLjYyMTI0MjQ4NDk2OTk0LCAxNzIuMDE4MDM2MDcyMTQ0MywgMTcyLjQxNDgyOTY1OTMxODYzLCAxNzIuODExNjIzMjQ2NDkyOTksIDE3My4yMDg0MTY4MzM2NjczNCwgMTczLjYwNTIxMDQyMDg0MTY3LCAxNzQuMDAyMDA0MDA4MDE2MDMsIDE3NC4zOTg3OTc1OTUxOTA0LCAxNzQuNzk1NTkxMTgyMzY0NzIsIDE3NS4xOTIzODQ3Njk1MzkwNywgMTc1LjU4OTE3ODM1NjcxMzQzLCAxNzUuOTg1OTcxOTQzODg3NzYsIDE3Ni4zODI3NjU1MzEwNjIxMiwgMTc2Ljc3OTU1OTExODIzNjQ4LCAxNzcuMTc2MzUyNzA1NDEwODQsIDE3Ny41NzMxNDYyOTI1ODUxNiwgMTc3Ljk2OTkzOTg3OTc1OTUyLCAxNzguMzY2NzMzNDY2OTMzODgsIDE3OC43NjM1MjcwNTQxMDgyLCAxNzkuMTYwMzIwNjQxMjgyNTcsIDE3OS41NTcxMTQyMjg0NTY5MiwgMTc5Ljk1MzkwNzgxNTYzMTI1LCAxODAuMzUwNzAxNDAyODA1NiwgMTgwLjc0NzQ5NDk4OTk3OTk3LCAxODEuMTQ0Mjg4NTc3MTU0MywgMTgxLjU0MTA4MjE2NDMyODY2LCAxODEuOTM3ODc1NzUxNTAzMDEsIDE4Mi4zMzQ2NjkzMzg2NzczNCwgMTgyLjczMTQ2MjkyNTg1MTcsIDE4My4xMjgyNTY1MTMwMjYwNiwgMTgzLjUyNTA1MDEwMDIwMDQsIDE4My45MjE4NDM2ODczNzQ3NSwgMTg0LjMxODYzNzI3NDU0OTEsIDE4NC43MTU0MzA4NjE3MjM0MywgMTg1LjExMjIyNDQ0ODg5NzgsIDE4NS41MDkwMTgwMzYwNzIxNSwgMTg1LjkwNTgxMTYyMzI0NjUsIDE4Ni4zMDI2MDUyMTA0MjA4NCwgMTg2LjY5OTM5ODc5NzU5NTIsIDE4Ny4wOTYxOTIzODQ3Njk1NSwgMTg3LjQ5Mjk4NTk3MTk0Mzg4LCAxODcuODg5Nzc5NTU5MTE4MjQsIDE4OC4yODY1NzMxNDYyOTI2LCAxODguNjgzMzY2NzMzNDY2OTMsIDE4OS4wODAxNjAzMjA2NDEyOCwgMTg5LjQ3Njk1MzkwNzgxNTY0LCAxODkuODczNzQ3NDk0OTg5OTcsIDE5MC4yNzA1NDEwODIxNjQzMywgMTkwLjY2NzMzNDY2OTMzODcsIDE5MS4wNjQxMjgyNTY1MTMwMiwgMTkxLjQ2MDkyMTg0MzY4NzM3LCAxOTEuODU3NzE1NDMwODYxNzMsIDE5Mi4yNTQ1MDkwMTgwMzYwNiwgMTkyLjY1MTMwMjYwNTIxMDQyLCAxOTMuMDQ4MDk2MTkyMzg0NzgsIDE5My40NDQ4ODk3Nzk1NTkxLCAxOTMuODQxNjgzMzY2NzMzNDYsIDE5NC4yMzg0NzY5NTM5MDc4MiwgMTk0LjYzNTI3MDU0MTA4MjE4LCAxOTUuMDMyMDY0MTI4MjU2NSwgMTk1LjQyODg1NzcxNTQzMDg3LCAxOTUuODI1NjUxMzAyNjA1MjIsIDE5Ni4yMjI0NDQ4ODk3Nzk1NSwgMTk2LjYxOTIzODQ3Njk1MzksIDE5Ny4wMTYwMzIwNjQxMjgyNywgMTk3LjQxMjgyNTY1MTMwMjYsIDE5Ny44MDk2MTkyMzg0NzY5NiwgMTk4LjIwNjQxMjgyNTY1MTMsIDE5OC42MDMyMDY0MTI4MjU2NCwgMTk5LjBdKQogICAgICAgICAgICAgIC5yYW5nZShbJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNiddKTsKICAgIAoKICAgIGNvbG9yX21hcF81N2E1ZDA0MTdhZTQ0OGZiYjc0ZTNiY2JhNjRmYmVlNi54ID0gZDMuc2NhbGUubGluZWFyKCkKICAgICAgICAgICAgICAuZG9tYWluKFsxLjAsIDE5OS4wXSkKICAgICAgICAgICAgICAucmFuZ2UoWzAsIDQwMF0pOwoKICAgIGNvbG9yX21hcF81N2E1ZDA0MTdhZTQ0OGZiYjc0ZTNiY2JhNjRmYmVlNi5sZWdlbmQgPSBMLmNvbnRyb2woe3Bvc2l0aW9uOiAndG9wcmlnaHQnfSk7CiAgICBjb2xvcl9tYXBfNTdhNWQwNDE3YWU0NDhmYmI3NGUzYmNiYTY0ZmJlZTYubGVnZW5kLm9uQWRkID0gZnVuY3Rpb24gKG1hcCkge3ZhciBkaXYgPSBMLkRvbVV0aWwuY3JlYXRlKCdkaXYnLCAnbGVnZW5kJyk7IHJldHVybiBkaXZ9OwogICAgY29sb3JfbWFwXzU3YTVkMDQxN2FlNDQ4ZmJiNzRlM2JjYmE2NGZiZWU2LmxlZ2VuZC5hZGRUbyhtYXBfMmIyNGQ0YWM3MWM2NDY1NTkyMzNlOTljYjU0ZTNlOTIpOwoKICAgIGNvbG9yX21hcF81N2E1ZDA0MTdhZTQ0OGZiYjc0ZTNiY2JhNjRmYmVlNi54QXhpcyA9IGQzLnN2Zy5heGlzKCkKICAgICAgICAuc2NhbGUoY29sb3JfbWFwXzU3YTVkMDQxN2FlNDQ4ZmJiNzRlM2JjYmE2NGZiZWU2LngpCiAgICAgICAgLm9yaWVudCgidG9wIikKICAgICAgICAudGlja1NpemUoMSkKICAgICAgICAudGlja1ZhbHVlcyhbMSwgNDAsIDc5LCAxMTksIDE1OCwgMTk5XSk7CgogICAgY29sb3JfbWFwXzU3YTVkMDQxN2FlNDQ4ZmJiNzRlM2JjYmE2NGZiZWU2LnN2ZyA9IGQzLnNlbGVjdCgiLmxlZ2VuZC5sZWFmbGV0LWNvbnRyb2wiKS5hcHBlbmQoInN2ZyIpCiAgICAgICAgLmF0dHIoImlkIiwgJ2xlZ2VuZCcpCiAgICAgICAgLmF0dHIoIndpZHRoIiwgNDUwKQogICAgICAgIC5hdHRyKCJoZWlnaHQiLCA0MCk7CgogICAgY29sb3JfbWFwXzU3YTVkMDQxN2FlNDQ4ZmJiNzRlM2JjYmE2NGZiZWU2LmcgPSBjb2xvcl9tYXBfNTdhNWQwNDE3YWU0NDhmYmI3NGUzYmNiYTY0ZmJlZTYuc3ZnLmFwcGVuZCgiZyIpCiAgICAgICAgLmF0dHIoImNsYXNzIiwgImtleSIpCiAgICAgICAgLmF0dHIoInRyYW5zZm9ybSIsICJ0cmFuc2xhdGUoMjUsMTYpIik7CgogICAgY29sb3JfbWFwXzU3YTVkMDQxN2FlNDQ4ZmJiNzRlM2JjYmE2NGZiZWU2Lmcuc2VsZWN0QWxsKCJyZWN0IikKICAgICAgICAuZGF0YShjb2xvcl9tYXBfNTdhNWQwNDE3YWU0NDhmYmI3NGUzYmNiYTY0ZmJlZTYuY29sb3IucmFuZ2UoKS5tYXAoZnVuY3Rpb24oZCwgaSkgewogICAgICAgICAgcmV0dXJuIHsKICAgICAgICAgICAgeDA6IGkgPyBjb2xvcl9tYXBfNTdhNWQwNDE3YWU0NDhmYmI3NGUzYmNiYTY0ZmJlZTYueChjb2xvcl9tYXBfNTdhNWQwNDE3YWU0NDhmYmI3NGUzYmNiYTY0ZmJlZTYuY29sb3IuZG9tYWluKClbaSAtIDFdKSA6IGNvbG9yX21hcF81N2E1ZDA0MTdhZTQ0OGZiYjc0ZTNiY2JhNjRmYmVlNi54LnJhbmdlKClbMF0sCiAgICAgICAgICAgIHgxOiBpIDwgY29sb3JfbWFwXzU3YTVkMDQxN2FlNDQ4ZmJiNzRlM2JjYmE2NGZiZWU2LmNvbG9yLmRvbWFpbigpLmxlbmd0aCA/IGNvbG9yX21hcF81N2E1ZDA0MTdhZTQ0OGZiYjc0ZTNiY2JhNjRmYmVlNi54KGNvbG9yX21hcF81N2E1ZDA0MTdhZTQ0OGZiYjc0ZTNiY2JhNjRmYmVlNi5jb2xvci5kb21haW4oKVtpXSkgOiBjb2xvcl9tYXBfNTdhNWQwNDE3YWU0NDhmYmI3NGUzYmNiYTY0ZmJlZTYueC5yYW5nZSgpWzFdLAogICAgICAgICAgICB6OiBkCiAgICAgICAgICB9OwogICAgICAgIH0pKQogICAgICAuZW50ZXIoKS5hcHBlbmQoInJlY3QiKQogICAgICAgIC5hdHRyKCJoZWlnaHQiLCAxMCkKICAgICAgICAuYXR0cigieCIsIGZ1bmN0aW9uKGQpIHsgcmV0dXJuIGQueDA7IH0pCiAgICAgICAgLmF0dHIoIndpZHRoIiwgZnVuY3Rpb24oZCkgeyByZXR1cm4gZC54MSAtIGQueDA7IH0pCiAgICAgICAgLnN0eWxlKCJmaWxsIiwgZnVuY3Rpb24oZCkgeyByZXR1cm4gZC56OyB9KTsKCiAgICBjb2xvcl9tYXBfNTdhNWQwNDE3YWU0NDhmYmI3NGUzYmNiYTY0ZmJlZTYuZy5jYWxsKGNvbG9yX21hcF81N2E1ZDA0MTdhZTQ0OGZiYjc0ZTNiY2JhNjRmYmVlNi54QXhpcykuYXBwZW5kKCJ0ZXh0IikKICAgICAgICAuYXR0cigiY2xhc3MiLCAiY2FwdGlvbiIpCiAgICAgICAgLmF0dHIoInkiLCAyMSkKICAgICAgICAudGV4dCgnRnJlZGVyaWN0b24gTmVpZ2hib3VyaG9vZHMnKTsKPC9zY3JpcHQ+" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>



## Examine Crime Types 


```python
crimetype_data = crime_df.groupby(['Crime_Type']).size().to_frame(name='Count').reset_index()
crimetype_data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Crime_Type</th>
      <th>Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td></td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ARSON</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ARSON BY NEG</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>ARSON-DAM.PROP.</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>B&amp;E NON-RESIDNCE</td>
      <td>51</td>
    </tr>
    <tr>
      <th>5</th>
      <td>B&amp;E OTHER</td>
      <td>58</td>
    </tr>
    <tr>
      <th>6</th>
      <td>B&amp;E RESIDENCE</td>
      <td>151</td>
    </tr>
    <tr>
      <th>7</th>
      <td>B&amp;E STEAL FIREAR</td>
      <td>3</td>
    </tr>
    <tr>
      <th>8</th>
      <td>MISCHIEF OBS USE</td>
      <td>1</td>
    </tr>
    <tr>
      <th>9</th>
      <td>MISCHIEF TO PROP</td>
      <td>246</td>
    </tr>
    <tr>
      <th>10</th>
      <td>MISCHIEF-DATA</td>
      <td>2</td>
    </tr>
    <tr>
      <th>11</th>
      <td>MOTOR VEH THEFT</td>
      <td>40</td>
    </tr>
    <tr>
      <th>12</th>
      <td>THEFT BIKE&lt;$5000</td>
      <td>63</td>
    </tr>
    <tr>
      <th>13</th>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>356</td>
    </tr>
    <tr>
      <th>14</th>
      <td>THEFT FROM MV &gt; $5000</td>
      <td>5</td>
    </tr>
    <tr>
      <th>15</th>
      <td>THEFT OTH &lt;$5000</td>
      <td>458</td>
    </tr>
    <tr>
      <th>16</th>
      <td>THEFT OTH &gt;$5000</td>
      <td>9</td>
    </tr>
    <tr>
      <th>17</th>
      <td>THEFT OVER $5000</td>
      <td>1</td>
    </tr>
    <tr>
      <th>18</th>
      <td>THEFT,BIKE&gt;$5000</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
crimetype_data.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>19.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>76.842105</td>
    </tr>
    <tr>
      <th>std</th>
      <td>133.196706</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>2.500000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>5.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>60.500000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>458.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
crimepivot = crime_df.pivot_table(index='Neighbourhood', columns='Crime_Type', aggfunc=pd.Series.count, fill_value=0)
crimepivot
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="19" halign="left">City</th>
      <th colspan="19" halign="left">Crime_Code</th>
      <th colspan="19" halign="left">FID</th>
      <th colspan="19" halign="left">Ward</th>
    </tr>
    <tr>
      <th>Crime_Type</th>
      <th></th>
      <th>ARSON</th>
      <th>ARSON BY NEG</th>
      <th>ARSON-DAM.PROP.</th>
      <th>B&amp;E NON-RESIDNCE</th>
      <th>B&amp;E OTHER</th>
      <th>B&amp;E RESIDENCE</th>
      <th>B&amp;E STEAL FIREAR</th>
      <th>MISCHIEF OBS USE</th>
      <th>MISCHIEF TO PROP</th>
      <th>MISCHIEF-DATA</th>
      <th>MOTOR VEH THEFT</th>
      <th>THEFT BIKE&lt;$5000</th>
      <th>THEFT FROM MV &lt; $5000</th>
      <th>THEFT FROM MV &gt; $5000</th>
      <th>THEFT OTH &lt;$5000</th>
      <th>THEFT OTH &gt;$5000</th>
      <th>THEFT OVER $5000</th>
      <th>THEFT,BIKE&gt;$5000</th>
      <th></th>
      <th>ARSON</th>
      <th>ARSON BY NEG</th>
      <th>ARSON-DAM.PROP.</th>
      <th>B&amp;E NON-RESIDNCE</th>
      <th>B&amp;E OTHER</th>
      <th>B&amp;E RESIDENCE</th>
      <th>B&amp;E STEAL FIREAR</th>
      <th>MISCHIEF OBS USE</th>
      <th>MISCHIEF TO PROP</th>
      <th>MISCHIEF-DATA</th>
      <th>MOTOR VEH THEFT</th>
      <th>THEFT BIKE&lt;$5000</th>
      <th>THEFT FROM MV &lt; $5000</th>
      <th>THEFT FROM MV &gt; $5000</th>
      <th>THEFT OTH &lt;$5000</th>
      <th>THEFT OTH &gt;$5000</th>
      <th>THEFT OVER $5000</th>
      <th>THEFT,BIKE&gt;$5000</th>
      <th></th>
      <th>ARSON</th>
      <th>ARSON BY NEG</th>
      <th>ARSON-DAM.PROP.</th>
      <th>B&amp;E NON-RESIDNCE</th>
      <th>B&amp;E OTHER</th>
      <th>B&amp;E RESIDENCE</th>
      <th>B&amp;E STEAL FIREAR</th>
      <th>MISCHIEF OBS USE</th>
      <th>MISCHIEF TO PROP</th>
      <th>MISCHIEF-DATA</th>
      <th>MOTOR VEH THEFT</th>
      <th>THEFT BIKE&lt;$5000</th>
      <th>THEFT FROM MV &lt; $5000</th>
      <th>THEFT FROM MV &gt; $5000</th>
      <th>THEFT OTH &lt;$5000</th>
      <th>THEFT OTH &gt;$5000</th>
      <th>THEFT OVER $5000</th>
      <th>THEFT,BIKE&gt;$5000</th>
      <th></th>
      <th>ARSON</th>
      <th>ARSON BY NEG</th>
      <th>ARSON-DAM.PROP.</th>
      <th>B&amp;E NON-RESIDNCE</th>
      <th>B&amp;E OTHER</th>
      <th>B&amp;E RESIDENCE</th>
      <th>B&amp;E STEAL FIREAR</th>
      <th>MISCHIEF OBS USE</th>
      <th>MISCHIEF TO PROP</th>
      <th>MISCHIEF-DATA</th>
      <th>MOTOR VEH THEFT</th>
      <th>THEFT BIKE&lt;$5000</th>
      <th>THEFT FROM MV &lt; $5000</th>
      <th>THEFT FROM MV &gt; $5000</th>
      <th>THEFT OTH &lt;$5000</th>
      <th>THEFT OTH &gt;$5000</th>
      <th>THEFT OVER $5000</th>
      <th>THEFT,BIKE&gt;$5000</th>
    </tr>
    <tr>
      <th>Neighbourhood</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Barkers Point</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>7</td>
      <td>7</td>
      <td>1</td>
      <td>0</td>
      <td>7</td>
      <td>0</td>
      <td>2</td>
      <td>2</td>
      <td>8</td>
      <td>0</td>
      <td>11</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>7</td>
      <td>7</td>
      <td>1</td>
      <td>0</td>
      <td>7</td>
      <td>0</td>
      <td>2</td>
      <td>2</td>
      <td>8</td>
      <td>0</td>
      <td>11</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>7</td>
      <td>7</td>
      <td>1</td>
      <td>0</td>
      <td>7</td>
      <td>0</td>
      <td>2</td>
      <td>2</td>
      <td>8</td>
      <td>0</td>
      <td>11</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>7</td>
      <td>7</td>
      <td>1</td>
      <td>0</td>
      <td>7</td>
      <td>0</td>
      <td>2</td>
      <td>2</td>
      <td>8</td>
      <td>0</td>
      <td>11</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Brookside</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>50</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>50</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>50</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>50</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Brookside Estates</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Brookside Mini Home Park</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>College Hill</th>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>13</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>10</td>
      <td>0</td>
      <td>8</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>13</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>10</td>
      <td>0</td>
      <td>8</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>13</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>10</td>
      <td>0</td>
      <td>8</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>13</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>10</td>
      <td>0</td>
      <td>8</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Colonial heights</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Cotton Mill Creek</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Diamond Street</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Doak Road</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Douglas</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Downtown</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>29</td>
      <td>1</td>
      <td>4</td>
      <td>8</td>
      <td>21</td>
      <td>0</td>
      <td>49</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>29</td>
      <td>1</td>
      <td>4</td>
      <td>8</td>
      <td>21</td>
      <td>0</td>
      <td>49</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>29</td>
      <td>1</td>
      <td>4</td>
      <td>8</td>
      <td>21</td>
      <td>0</td>
      <td>49</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>29</td>
      <td>1</td>
      <td>4</td>
      <td>8</td>
      <td>21</td>
      <td>0</td>
      <td>49</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Dun's Crossing</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>9</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>9</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>9</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>9</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Forest Hill</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>8</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>8</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>8</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>8</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Fredericton South</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>13</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>20</td>
      <td>1</td>
      <td>35</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>13</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>20</td>
      <td>1</td>
      <td>35</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>13</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>20</td>
      <td>1</td>
      <td>35</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>13</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>20</td>
      <td>1</td>
      <td>35</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Fulton Heights</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
      <td>8</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>12</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
      <td>8</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>12</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
      <td>8</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>12</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
      <td>8</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>12</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Garden Creek</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>7</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>7</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>7</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>7</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Garden Place</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Gilridge Estates</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Golf Club</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Grasse Circle</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Greenwood Minihome Park</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Hanwell North</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Heron Springs</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Highpoint Ridge</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Kelly's Court Minihome Park</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Knob Hill</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Knowledge Park</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Lian / Valcore</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Lincoln</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Lincoln Heights</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>11</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>11</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>11</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>11</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Main Street</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>4</td>
      <td>8</td>
      <td>0</td>
      <td>1</td>
      <td>12</td>
      <td>0</td>
      <td>2</td>
      <td>3</td>
      <td>10</td>
      <td>0</td>
      <td>33</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>4</td>
      <td>8</td>
      <td>0</td>
      <td>1</td>
      <td>12</td>
      <td>0</td>
      <td>2</td>
      <td>3</td>
      <td>10</td>
      <td>0</td>
      <td>33</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>4</td>
      <td>8</td>
      <td>0</td>
      <td>1</td>
      <td>12</td>
      <td>0</td>
      <td>2</td>
      <td>3</td>
      <td>10</td>
      <td>0</td>
      <td>33</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>4</td>
      <td>8</td>
      <td>0</td>
      <td>1</td>
      <td>12</td>
      <td>0</td>
      <td>2</td>
      <td>3</td>
      <td>10</td>
      <td>0</td>
      <td>33</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Marysville</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>8</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>10</td>
      <td>0</td>
      <td>10</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>8</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>10</td>
      <td>0</td>
      <td>10</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>8</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>10</td>
      <td>0</td>
      <td>10</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>8</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>10</td>
      <td>0</td>
      <td>10</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>McKnight</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>McLeod Hill</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Monteith / Talisman</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>2</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>2</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>2</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>2</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Montogomery / Prospect East</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>11</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>11</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>11</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>11</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Nashwaaksis</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>9</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>9</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>9</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>9</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Nethervue Minihome Park</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>North Devon</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>4</td>
      <td>11</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>17</td>
      <td>0</td>
      <td>30</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>4</td>
      <td>11</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>17</td>
      <td>0</td>
      <td>30</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>4</td>
      <td>11</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>17</td>
      <td>0</td>
      <td>30</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>4</td>
      <td>11</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>17</td>
      <td>0</td>
      <td>30</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Northbrook Heights</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Plat</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>10</td>
      <td>18</td>
      <td>0</td>
      <td>0</td>
      <td>31</td>
      <td>0</td>
      <td>3</td>
      <td>21</td>
      <td>40</td>
      <td>0</td>
      <td>71</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>10</td>
      <td>18</td>
      <td>0</td>
      <td>0</td>
      <td>31</td>
      <td>0</td>
      <td>3</td>
      <td>21</td>
      <td>40</td>
      <td>0</td>
      <td>71</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>10</td>
      <td>18</td>
      <td>0</td>
      <td>0</td>
      <td>31</td>
      <td>0</td>
      <td>3</td>
      <td>21</td>
      <td>40</td>
      <td>0</td>
      <td>71</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>10</td>
      <td>18</td>
      <td>0</td>
      <td>0</td>
      <td>31</td>
      <td>0</td>
      <td>3</td>
      <td>21</td>
      <td>40</td>
      <td>0</td>
      <td>71</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Poet's Hill</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Prospect</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>16</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>11</td>
      <td>2</td>
      <td>48</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>16</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>11</td>
      <td>2</td>
      <td>48</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>16</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>11</td>
      <td>2</td>
      <td>48</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>16</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>11</td>
      <td>2</td>
      <td>48</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Rail Side</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Regiment Creek</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Royal Road</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>2</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>2</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>2</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>2</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Saint Mary's First Nation</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>13</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>13</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>13</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>13</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Saint Thomas University</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Sandyville</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Serenity Lane</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Shadowood Estates</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Silverwood</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Skyline Acrea</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>13</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>13</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>13</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>13</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>South Devon</th>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>16</td>
      <td>0</td>
      <td>0</td>
      <td>8</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>22</td>
      <td>0</td>
      <td>10</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>16</td>
      <td>0</td>
      <td>0</td>
      <td>8</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>22</td>
      <td>0</td>
      <td>10</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>16</td>
      <td>0</td>
      <td>0</td>
      <td>8</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>22</td>
      <td>0</td>
      <td>10</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>16</td>
      <td>0</td>
      <td>0</td>
      <td>8</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>22</td>
      <td>0</td>
      <td>10</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Southwood Park</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Springhill</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Sunshine Gardens</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>7</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>7</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>7</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>7</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>The Hill</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>12</td>
      <td>1</td>
      <td>0</td>
      <td>7</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>11</td>
      <td>0</td>
      <td>10</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>12</td>
      <td>1</td>
      <td>0</td>
      <td>7</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>11</td>
      <td>0</td>
      <td>10</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>12</td>
      <td>1</td>
      <td>0</td>
      <td>7</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>11</td>
      <td>0</td>
      <td>10</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>12</td>
      <td>1</td>
      <td>0</td>
      <td>7</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>11</td>
      <td>0</td>
      <td>10</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>The Hugh John Flemming Forestry Center</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>University Of New Brunswick</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>4</td>
      <td>0</td>
      <td>8</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>4</td>
      <td>0</td>
      <td>8</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>4</td>
      <td>0</td>
      <td>8</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>4</td>
      <td>0</td>
      <td>8</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Waterloo Row</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Wesbett / Case</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>West Hills</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Williams / Hawkins Area</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>7</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>7</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>7</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>7</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Woodstock Road</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>4</td>
      <td>2</td>
      <td>20</td>
      <td>1</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>4</td>
      <td>2</td>
      <td>20</td>
      <td>1</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>4</td>
      <td>2</td>
      <td>20</td>
      <td>1</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>4</td>
      <td>2</td>
      <td>20</td>
      <td>1</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Youngs Crossing</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
crimetype_data.plot(x='Crime_Type', y='Count', kind='barh')

```




    <matplotlib.axes._subplots.AxesSubplot at 0x11682a860>




![png](output_42_1.png)



```python

```

## Let's examine theft from vehicles


```python
mvcrime_df = crime_df.loc[crime_df['Crime_Type'] == 'THEFT FROM MV < $5000']
mvcrime_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Neighbourhood</th>
      <th>Crime_Code</th>
      <th>Crime_Type</th>
      <th>Ward</th>
      <th>City</th>
      <th>FID</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>18</th>
      <td>Fredericton South</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>7</td>
      <td>Fredericton</td>
      <td>19</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Fredericton South</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>7</td>
      <td>Fredericton</td>
      <td>20</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Fredericton South</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>7</td>
      <td>Fredericton</td>
      <td>21</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Fredericton South</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>22</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Fredericton South</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>23</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Fredericton South</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>7</td>
      <td>Fredericton</td>
      <td>24</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Fredericton South</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>7</td>
      <td>Fredericton</td>
      <td>25</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Fredericton South</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>7</td>
      <td>Fredericton</td>
      <td>26</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Fredericton South</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>11</td>
      <td>Fredericton</td>
      <td>27</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Fredericton South</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>11</td>
      <td>Fredericton</td>
      <td>28</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Fredericton South</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>29</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Fredericton South</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>30</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Fredericton South</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>7</td>
      <td>Fredericton</td>
      <td>31</td>
    </tr>
    <tr>
      <th>51</th>
      <td>Barkers Point</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>6</td>
      <td>Fredericton</td>
      <td>52</td>
    </tr>
    <tr>
      <th>52</th>
      <td>Barkers Point</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>6</td>
      <td>Fredericton</td>
      <td>53</td>
    </tr>
    <tr>
      <th>53</th>
      <td>Barkers Point</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>6</td>
      <td>Fredericton</td>
      <td>54</td>
    </tr>
    <tr>
      <th>54</th>
      <td>Barkers Point</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>6</td>
      <td>Fredericton</td>
      <td>55</td>
    </tr>
    <tr>
      <th>55</th>
      <td>Barkers Point</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>6</td>
      <td>Fredericton</td>
      <td>56</td>
    </tr>
    <tr>
      <th>56</th>
      <td>Barkers Point</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>6</td>
      <td>Fredericton</td>
      <td>57</td>
    </tr>
    <tr>
      <th>57</th>
      <td>Barkers Point</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>6</td>
      <td>Fredericton</td>
      <td>58</td>
    </tr>
    <tr>
      <th>58</th>
      <td>Barkers Point</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>6</td>
      <td>Fredericton</td>
      <td>59</td>
    </tr>
    <tr>
      <th>100</th>
      <td>Sandyville</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>5</td>
      <td>Fredericton</td>
      <td>101</td>
    </tr>
    <tr>
      <th>107</th>
      <td>South Devon</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>4</td>
      <td>Fredericton</td>
      <td>108</td>
    </tr>
    <tr>
      <th>108</th>
      <td>South Devon</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>4</td>
      <td>Fredericton</td>
      <td>109</td>
    </tr>
    <tr>
      <th>109</th>
      <td>South Devon</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>4</td>
      <td>Fredericton</td>
      <td>110</td>
    </tr>
    <tr>
      <th>110</th>
      <td>South Devon</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>4</td>
      <td>Fredericton</td>
      <td>111</td>
    </tr>
    <tr>
      <th>111</th>
      <td>South Devon</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>4</td>
      <td>Fredericton</td>
      <td>112</td>
    </tr>
    <tr>
      <th>112</th>
      <td>South Devon</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>4</td>
      <td>Fredericton</td>
      <td>113</td>
    </tr>
    <tr>
      <th>113</th>
      <td>South Devon</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>4</td>
      <td>Fredericton</td>
      <td>114</td>
    </tr>
    <tr>
      <th>114</th>
      <td>South Devon</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>4</td>
      <td>Fredericton</td>
      <td>115</td>
    </tr>
    <tr>
      <th>115</th>
      <td>South Devon</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>4</td>
      <td>Fredericton</td>
      <td>116</td>
    </tr>
    <tr>
      <th>116</th>
      <td>South Devon</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>4</td>
      <td>Fredericton</td>
      <td>117</td>
    </tr>
    <tr>
      <th>117</th>
      <td>South Devon</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>4</td>
      <td>Fredericton</td>
      <td>118</td>
    </tr>
    <tr>
      <th>118</th>
      <td>South Devon</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>4</td>
      <td>Fredericton</td>
      <td>119</td>
    </tr>
    <tr>
      <th>119</th>
      <td>South Devon</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>4</td>
      <td>Fredericton</td>
      <td>120</td>
    </tr>
    <tr>
      <th>120</th>
      <td>South Devon</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>4</td>
      <td>Fredericton</td>
      <td>121</td>
    </tr>
    <tr>
      <th>121</th>
      <td>South Devon</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>4</td>
      <td>Fredericton</td>
      <td>122</td>
    </tr>
    <tr>
      <th>122</th>
      <td>South Devon</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>4</td>
      <td>Fredericton</td>
      <td>123</td>
    </tr>
    <tr>
      <th>123</th>
      <td>South Devon</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>4</td>
      <td>Fredericton</td>
      <td>124</td>
    </tr>
    <tr>
      <th>124</th>
      <td>South Devon</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>4</td>
      <td>Fredericton</td>
      <td>125</td>
    </tr>
    <tr>
      <th>125</th>
      <td>South Devon</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>4</td>
      <td>Fredericton</td>
      <td>126</td>
    </tr>
    <tr>
      <th>126</th>
      <td>South Devon</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>4</td>
      <td>Fredericton</td>
      <td>127</td>
    </tr>
    <tr>
      <th>127</th>
      <td>South Devon</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>4</td>
      <td>Fredericton</td>
      <td>128</td>
    </tr>
    <tr>
      <th>128</th>
      <td>South Devon</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>4</td>
      <td>Fredericton</td>
      <td>129</td>
    </tr>
    <tr>
      <th>151</th>
      <td>Sandyville</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>5</td>
      <td>Fredericton</td>
      <td>152</td>
    </tr>
    <tr>
      <th>156</th>
      <td>Knob Hill</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>5</td>
      <td>Fredericton</td>
      <td>157</td>
    </tr>
    <tr>
      <th>165</th>
      <td>Youngs Crossing</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>4</td>
      <td>Fredericton</td>
      <td>166</td>
    </tr>
    <tr>
      <th>166</th>
      <td>Youngs Crossing</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>4</td>
      <td>Fredericton</td>
      <td>167</td>
    </tr>
    <tr>
      <th>167</th>
      <td>Youngs Crossing</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>4</td>
      <td>Fredericton</td>
      <td>168</td>
    </tr>
    <tr>
      <th>168</th>
      <td>Youngs Crossing</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>4</td>
      <td>Fredericton</td>
      <td>169</td>
    </tr>
    <tr>
      <th>169</th>
      <td>Youngs Crossing</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>4</td>
      <td>Fredericton</td>
      <td>170</td>
    </tr>
    <tr>
      <th>170</th>
      <td>Youngs Crossing</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>4</td>
      <td>Fredericton</td>
      <td>171</td>
    </tr>
    <tr>
      <th>201</th>
      <td>Marysville</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>5</td>
      <td>Fredericton</td>
      <td>202</td>
    </tr>
    <tr>
      <th>252</th>
      <td>Marysville</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>5</td>
      <td>Fredericton</td>
      <td>253</td>
    </tr>
    <tr>
      <th>278</th>
      <td>Douglas</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>1</td>
      <td>Fredericton</td>
      <td>279</td>
    </tr>
    <tr>
      <th>280</th>
      <td>McLeod Hill</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>2</td>
      <td>Fredericton</td>
      <td>281</td>
    </tr>
    <tr>
      <th>281</th>
      <td>McLeod Hill</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>2</td>
      <td>Fredericton</td>
      <td>282</td>
    </tr>
    <tr>
      <th>301</th>
      <td>Marysville</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>0</td>
      <td>Fredericton</td>
      <td>302</td>
    </tr>
    <tr>
      <th>302</th>
      <td>Marysville</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>5</td>
      <td>Fredericton</td>
      <td>303</td>
    </tr>
    <tr>
      <th>303</th>
      <td>Marysville</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>5</td>
      <td>Fredericton</td>
      <td>304</td>
    </tr>
    <tr>
      <th>304</th>
      <td>Marysville</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>5</td>
      <td>Fredericton</td>
      <td>305</td>
    </tr>
    <tr>
      <th>305</th>
      <td>Marysville</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>5</td>
      <td>Fredericton</td>
      <td>306</td>
    </tr>
    <tr>
      <th>306</th>
      <td>Marysville</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>5</td>
      <td>Fredericton</td>
      <td>307</td>
    </tr>
    <tr>
      <th>307</th>
      <td>Marysville</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>5</td>
      <td>Fredericton</td>
      <td>308</td>
    </tr>
    <tr>
      <th>308</th>
      <td>Marysville</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>5</td>
      <td>Fredericton</td>
      <td>309</td>
    </tr>
    <tr>
      <th>330</th>
      <td>Saint Mary's First Nation</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>3</td>
      <td>Fredericton</td>
      <td>331</td>
    </tr>
    <tr>
      <th>349</th>
      <td>Sandyville</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>5</td>
      <td>Fredericton</td>
      <td>350</td>
    </tr>
    <tr>
      <th>354</th>
      <td>Nashwaaksis</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>1</td>
      <td>Fredericton</td>
      <td>355</td>
    </tr>
    <tr>
      <th>355</th>
      <td>Nashwaaksis</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>1</td>
      <td>Fredericton</td>
      <td>356</td>
    </tr>
    <tr>
      <th>356</th>
      <td>Nashwaaksis</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>1</td>
      <td>Fredericton</td>
      <td>357</td>
    </tr>
    <tr>
      <th>357</th>
      <td>Nashwaaksis</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>1</td>
      <td>Fredericton</td>
      <td>358</td>
    </tr>
    <tr>
      <th>358</th>
      <td>Nashwaaksis</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>1</td>
      <td>Fredericton</td>
      <td>359</td>
    </tr>
    <tr>
      <th>359</th>
      <td>Nashwaaksis</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>1</td>
      <td>Fredericton</td>
      <td>360</td>
    </tr>
    <tr>
      <th>360</th>
      <td>Nashwaaksis</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>1</td>
      <td>Fredericton</td>
      <td>361</td>
    </tr>
    <tr>
      <th>361</th>
      <td>Nashwaaksis</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>1</td>
      <td>Fredericton</td>
      <td>362</td>
    </tr>
    <tr>
      <th>362</th>
      <td>Nashwaaksis</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>1</td>
      <td>Fredericton</td>
      <td>363</td>
    </tr>
    <tr>
      <th>377</th>
      <td>Northbrook Heights</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>2</td>
      <td>Fredericton</td>
      <td>378</td>
    </tr>
    <tr>
      <th>378</th>
      <td>Northbrook Heights</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>2</td>
      <td>Fredericton</td>
      <td>379</td>
    </tr>
    <tr>
      <th>379</th>
      <td>Northbrook Heights</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>1</td>
      <td>Fredericton</td>
      <td>380</td>
    </tr>
    <tr>
      <th>380</th>
      <td>Northbrook Heights</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>2</td>
      <td>Fredericton</td>
      <td>381</td>
    </tr>
    <tr>
      <th>381</th>
      <td>Northbrook Heights</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>2</td>
      <td>Fredericton</td>
      <td>382</td>
    </tr>
    <tr>
      <th>388</th>
      <td>Heron Springs</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>2</td>
      <td>Fredericton</td>
      <td>389</td>
    </tr>
    <tr>
      <th>389</th>
      <td>Heron Springs</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>2</td>
      <td>Fredericton</td>
      <td>390</td>
    </tr>
    <tr>
      <th>400</th>
      <td>Downtown</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>401</td>
    </tr>
    <tr>
      <th>401</th>
      <td>Downtown</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>11</td>
      <td>Fredericton</td>
      <td>402</td>
    </tr>
    <tr>
      <th>402</th>
      <td>Downtown</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>11</td>
      <td>Fredericton</td>
      <td>403</td>
    </tr>
    <tr>
      <th>403</th>
      <td>Downtown</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>404</td>
    </tr>
    <tr>
      <th>404</th>
      <td>Downtown</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>405</td>
    </tr>
    <tr>
      <th>405</th>
      <td>Downtown</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>406</td>
    </tr>
    <tr>
      <th>408</th>
      <td>Downtown</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>409</td>
    </tr>
    <tr>
      <th>410</th>
      <td>Downtown</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>411</td>
    </tr>
    <tr>
      <th>411</th>
      <td>Downtown</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>412</td>
    </tr>
    <tr>
      <th>412</th>
      <td>Downtown</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>413</td>
    </tr>
    <tr>
      <th>413</th>
      <td>Downtown</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>414</td>
    </tr>
    <tr>
      <th>414</th>
      <td>Downtown</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>415</td>
    </tr>
    <tr>
      <th>415</th>
      <td>Downtown</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>416</td>
    </tr>
    <tr>
      <th>416</th>
      <td>Downtown</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>417</td>
    </tr>
    <tr>
      <th>417</th>
      <td>Downtown</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>418</td>
    </tr>
    <tr>
      <th>418</th>
      <td>Downtown</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>419</td>
    </tr>
    <tr>
      <th>419</th>
      <td>Downtown</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>420</td>
    </tr>
    <tr>
      <th>420</th>
      <td>Downtown</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>421</td>
    </tr>
    <tr>
      <th>421</th>
      <td>Downtown</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>422</td>
    </tr>
    <tr>
      <th>422</th>
      <td>Downtown</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>423</td>
    </tr>
    <tr>
      <th>506</th>
      <td>Downtown</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>507</td>
    </tr>
    <tr>
      <th>520</th>
      <td>Fulton Heights</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>3</td>
      <td>Fredericton</td>
      <td>521</td>
    </tr>
    <tr>
      <th>521</th>
      <td>Fulton Heights</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>3</td>
      <td>Fredericton</td>
      <td>522</td>
    </tr>
    <tr>
      <th>522</th>
      <td>Fulton Heights</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>3</td>
      <td>Fredericton</td>
      <td>523</td>
    </tr>
    <tr>
      <th>523</th>
      <td>Fulton Heights</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>3</td>
      <td>Fredericton</td>
      <td>524</td>
    </tr>
    <tr>
      <th>524</th>
      <td>Fulton Heights</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>2</td>
      <td>Fredericton</td>
      <td>525</td>
    </tr>
    <tr>
      <th>525</th>
      <td>Fulton Heights</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>3</td>
      <td>Fredericton</td>
      <td>526</td>
    </tr>
    <tr>
      <th>526</th>
      <td>Fulton Heights</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>3</td>
      <td>Fredericton</td>
      <td>527</td>
    </tr>
    <tr>
      <th>527</th>
      <td>Fulton Heights</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>3</td>
      <td>Fredericton</td>
      <td>528</td>
    </tr>
    <tr>
      <th>528</th>
      <td>Fulton Heights</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>3</td>
      <td>Fredericton</td>
      <td>529</td>
    </tr>
    <tr>
      <th>529</th>
      <td>Fulton Heights</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>2</td>
      <td>Fredericton</td>
      <td>530</td>
    </tr>
    <tr>
      <th>530</th>
      <td>Fulton Heights</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>3</td>
      <td>Fredericton</td>
      <td>531</td>
    </tr>
    <tr>
      <th>531</th>
      <td>Fulton Heights</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>3</td>
      <td>Fredericton</td>
      <td>532</td>
    </tr>
    <tr>
      <th>569</th>
      <td>Main Street</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>2</td>
      <td>Fredericton</td>
      <td>570</td>
    </tr>
    <tr>
      <th>570</th>
      <td>Main Street</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>3</td>
      <td>Fredericton</td>
      <td>571</td>
    </tr>
    <tr>
      <th>571</th>
      <td>Main Street</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>2</td>
      <td>Fredericton</td>
      <td>572</td>
    </tr>
    <tr>
      <th>572</th>
      <td>Main Street</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>2</td>
      <td>Fredericton</td>
      <td>573</td>
    </tr>
    <tr>
      <th>573</th>
      <td>Main Street</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>3</td>
      <td>Fredericton</td>
      <td>574</td>
    </tr>
    <tr>
      <th>574</th>
      <td>Main Street</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>2</td>
      <td>Fredericton</td>
      <td>575</td>
    </tr>
    <tr>
      <th>575</th>
      <td>Main Street</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>2</td>
      <td>Fredericton</td>
      <td>576</td>
    </tr>
    <tr>
      <th>576</th>
      <td>Main Street</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>2</td>
      <td>Fredericton</td>
      <td>577</td>
    </tr>
    <tr>
      <th>577</th>
      <td>Main Street</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>2</td>
      <td>Fredericton</td>
      <td>578</td>
    </tr>
    <tr>
      <th>578</th>
      <td>Main Street</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>2</td>
      <td>Fredericton</td>
      <td>579</td>
    </tr>
    <tr>
      <th>604</th>
      <td>Golf Club</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>605</td>
    </tr>
    <tr>
      <th>614</th>
      <td>Gilridge Estates</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>1</td>
      <td>Fredericton</td>
      <td>615</td>
    </tr>
    <tr>
      <th>622</th>
      <td>Nethervue Minihome Park</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>623</td>
    </tr>
    <tr>
      <th>625</th>
      <td>Monteith / Talisman</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>626</td>
    </tr>
    <tr>
      <th>626</th>
      <td>Monteith / Talisman</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>627</td>
    </tr>
    <tr>
      <th>631</th>
      <td>Garden Creek</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>632</td>
    </tr>
    <tr>
      <th>640</th>
      <td>Highpoint Ridge</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>641</td>
    </tr>
    <tr>
      <th>641</th>
      <td>Highpoint Ridge</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>642</td>
    </tr>
    <tr>
      <th>642</th>
      <td>Highpoint Ridge</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>643</td>
    </tr>
    <tr>
      <th>643</th>
      <td>Highpoint Ridge</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>644</td>
    </tr>
    <tr>
      <th>650</th>
      <td>Golf Club</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>651</td>
    </tr>
    <tr>
      <th>651</th>
      <td>Golf Club</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>652</td>
    </tr>
    <tr>
      <th>653</th>
      <td>Golf Club</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>654</td>
    </tr>
    <tr>
      <th>752</th>
      <td>Golf Club</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>753</td>
    </tr>
    <tr>
      <th>764</th>
      <td>Woodstock Road</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>765</td>
    </tr>
    <tr>
      <th>765</th>
      <td>Woodstock Road</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>766</td>
    </tr>
    <tr>
      <th>766</th>
      <td>Woodstock Road</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>767</td>
    </tr>
    <tr>
      <th>767</th>
      <td>Woodstock Road</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>768</td>
    </tr>
    <tr>
      <th>768</th>
      <td>Woodstock Road</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>769</td>
    </tr>
    <tr>
      <th>769</th>
      <td>Woodstock Road</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>770</td>
    </tr>
    <tr>
      <th>770</th>
      <td>Woodstock Road</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>771</td>
    </tr>
    <tr>
      <th>771</th>
      <td>Woodstock Road</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>772</td>
    </tr>
    <tr>
      <th>772</th>
      <td>Woodstock Road</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>773</td>
    </tr>
    <tr>
      <th>773</th>
      <td>Woodstock Road</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>774</td>
    </tr>
    <tr>
      <th>774</th>
      <td>Woodstock Road</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>775</td>
    </tr>
    <tr>
      <th>775</th>
      <td>Woodstock Road</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>776</td>
    </tr>
    <tr>
      <th>776</th>
      <td>Woodstock Road</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>0</td>
      <td>Fredericton</td>
      <td>777</td>
    </tr>
    <tr>
      <th>777</th>
      <td>Woodstock Road</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>778</td>
    </tr>
    <tr>
      <th>778</th>
      <td>Woodstock Road</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>779</td>
    </tr>
    <tr>
      <th>779</th>
      <td>Woodstock Road</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>780</td>
    </tr>
    <tr>
      <th>780</th>
      <td>Woodstock Road</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>781</td>
    </tr>
    <tr>
      <th>781</th>
      <td>Woodstock Road</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>782</td>
    </tr>
    <tr>
      <th>787</th>
      <td>Sunshine Gardens</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>788</td>
    </tr>
    <tr>
      <th>788</th>
      <td>Sunshine Gardens</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>789</td>
    </tr>
    <tr>
      <th>789</th>
      <td>Sunshine Gardens</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>790</td>
    </tr>
    <tr>
      <th>790</th>
      <td>Sunshine Gardens</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>791</td>
    </tr>
    <tr>
      <th>791</th>
      <td>Sunshine Gardens</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>792</td>
    </tr>
    <tr>
      <th>792</th>
      <td>Sunshine Gardens</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>793</td>
    </tr>
    <tr>
      <th>793</th>
      <td>Sunshine Gardens</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>794</td>
    </tr>
    <tr>
      <th>809</th>
      <td>Plat</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>0</td>
      <td>Fredericton</td>
      <td>810</td>
    </tr>
    <tr>
      <th>810</th>
      <td>Plat</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>11</td>
      <td>Fredericton</td>
      <td>811</td>
    </tr>
    <tr>
      <th>811</th>
      <td>Plat</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>11</td>
      <td>Fredericton</td>
      <td>812</td>
    </tr>
    <tr>
      <th>812</th>
      <td>Plat</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>813</td>
    </tr>
    <tr>
      <th>813</th>
      <td>Plat</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>11</td>
      <td>Fredericton</td>
      <td>814</td>
    </tr>
    <tr>
      <th>814</th>
      <td>Plat</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>815</td>
    </tr>
    <tr>
      <th>815</th>
      <td>Plat</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>816</td>
    </tr>
    <tr>
      <th>816</th>
      <td>Plat</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>817</td>
    </tr>
    <tr>
      <th>817</th>
      <td>Plat</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>818</td>
    </tr>
    <tr>
      <th>818</th>
      <td>Plat</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>819</td>
    </tr>
    <tr>
      <th>819</th>
      <td>Plat</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>11</td>
      <td>Fredericton</td>
      <td>820</td>
    </tr>
    <tr>
      <th>820</th>
      <td>Plat</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>821</td>
    </tr>
    <tr>
      <th>821</th>
      <td>Plat</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>822</td>
    </tr>
    <tr>
      <th>822</th>
      <td>Plat</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>823</td>
    </tr>
    <tr>
      <th>823</th>
      <td>Plat</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>824</td>
    </tr>
    <tr>
      <th>824</th>
      <td>Plat</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>825</td>
    </tr>
    <tr>
      <th>825</th>
      <td>Plat</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>0</td>
      <td>Fredericton</td>
      <td>826</td>
    </tr>
    <tr>
      <th>826</th>
      <td>Plat</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>11</td>
      <td>Fredericton</td>
      <td>827</td>
    </tr>
    <tr>
      <th>827</th>
      <td>Plat</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>828</td>
    </tr>
    <tr>
      <th>828</th>
      <td>Plat</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>829</td>
    </tr>
    <tr>
      <th>829</th>
      <td>Plat</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>830</td>
    </tr>
    <tr>
      <th>830</th>
      <td>Plat</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>11</td>
      <td>Fredericton</td>
      <td>831</td>
    </tr>
    <tr>
      <th>831</th>
      <td>Plat</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>11</td>
      <td>Fredericton</td>
      <td>832</td>
    </tr>
    <tr>
      <th>832</th>
      <td>Plat</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>833</td>
    </tr>
    <tr>
      <th>833</th>
      <td>Plat</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>11</td>
      <td>Fredericton</td>
      <td>834</td>
    </tr>
    <tr>
      <th>835</th>
      <td>Plat</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>836</td>
    </tr>
    <tr>
      <th>836</th>
      <td>Plat</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>11</td>
      <td>Fredericton</td>
      <td>837</td>
    </tr>
    <tr>
      <th>837</th>
      <td>Plat</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>838</td>
    </tr>
    <tr>
      <th>838</th>
      <td>Plat</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>839</td>
    </tr>
    <tr>
      <th>839</th>
      <td>Plat</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>11</td>
      <td>Fredericton</td>
      <td>840</td>
    </tr>
    <tr>
      <th>840</th>
      <td>Plat</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>841</td>
    </tr>
    <tr>
      <th>841</th>
      <td>Plat</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>842</td>
    </tr>
    <tr>
      <th>842</th>
      <td>Plat</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>843</td>
    </tr>
    <tr>
      <th>843</th>
      <td>Plat</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>844</td>
    </tr>
    <tr>
      <th>844</th>
      <td>Plat</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>845</td>
    </tr>
    <tr>
      <th>845</th>
      <td>Plat</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>11</td>
      <td>Fredericton</td>
      <td>846</td>
    </tr>
    <tr>
      <th>846</th>
      <td>Plat</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>847</td>
    </tr>
    <tr>
      <th>847</th>
      <td>Plat</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>848</td>
    </tr>
    <tr>
      <th>848</th>
      <td>Plat</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>11</td>
      <td>Fredericton</td>
      <td>849</td>
    </tr>
    <tr>
      <th>849</th>
      <td>Plat</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>850</td>
    </tr>
    <tr>
      <th>855</th>
      <td>Southwood Park</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>7</td>
      <td>Fredericton</td>
      <td>856</td>
    </tr>
    <tr>
      <th>856</th>
      <td>Southwood Park</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>7</td>
      <td>Fredericton</td>
      <td>857</td>
    </tr>
    <tr>
      <th>857</th>
      <td>Southwood Park</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>7</td>
      <td>Fredericton</td>
      <td>858</td>
    </tr>
    <tr>
      <th>865</th>
      <td>Lincoln Heights</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>7</td>
      <td>Fredericton</td>
      <td>866</td>
    </tr>
    <tr>
      <th>866</th>
      <td>Lincoln Heights</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>7</td>
      <td>Fredericton</td>
      <td>867</td>
    </tr>
    <tr>
      <th>867</th>
      <td>Lincoln Heights</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>7</td>
      <td>Fredericton</td>
      <td>868</td>
    </tr>
    <tr>
      <th>868</th>
      <td>Lincoln Heights</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>7</td>
      <td>Fredericton</td>
      <td>869</td>
    </tr>
    <tr>
      <th>869</th>
      <td>Lincoln Heights</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>7</td>
      <td>Fredericton</td>
      <td>870</td>
    </tr>
    <tr>
      <th>871</th>
      <td>Lincoln Heights</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>7</td>
      <td>Fredericton</td>
      <td>872</td>
    </tr>
    <tr>
      <th>875</th>
      <td>Lincoln Heights</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>7</td>
      <td>Fredericton</td>
      <td>876</td>
    </tr>
    <tr>
      <th>880</th>
      <td>Skyline Acrea</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>8</td>
      <td>Fredericton</td>
      <td>881</td>
    </tr>
    <tr>
      <th>881</th>
      <td>Lincoln Heights</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>7</td>
      <td>Fredericton</td>
      <td>882</td>
    </tr>
    <tr>
      <th>886</th>
      <td>Skyline Acrea</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>8</td>
      <td>Fredericton</td>
      <td>887</td>
    </tr>
    <tr>
      <th>887</th>
      <td>Lincoln Heights</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>7</td>
      <td>Fredericton</td>
      <td>888</td>
    </tr>
    <tr>
      <th>892</th>
      <td>Skyline Acrea</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>8</td>
      <td>Fredericton</td>
      <td>893</td>
    </tr>
    <tr>
      <th>893</th>
      <td>Lincoln Heights</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>7</td>
      <td>Fredericton</td>
      <td>894</td>
    </tr>
    <tr>
      <th>898</th>
      <td>Skyline Acrea</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>8</td>
      <td>Fredericton</td>
      <td>899</td>
    </tr>
    <tr>
      <th>899</th>
      <td>Skyline Acrea</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>8</td>
      <td>Fredericton</td>
      <td>900</td>
    </tr>
    <tr>
      <th>900</th>
      <td>Skyline Acrea</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>8</td>
      <td>Fredericton</td>
      <td>901</td>
    </tr>
    <tr>
      <th>901</th>
      <td>Skyline Acrea</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>8</td>
      <td>Fredericton</td>
      <td>902</td>
    </tr>
    <tr>
      <th>902</th>
      <td>Skyline Acrea</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>8</td>
      <td>Fredericton</td>
      <td>903</td>
    </tr>
    <tr>
      <th>903</th>
      <td>Skyline Acrea</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>8</td>
      <td>Fredericton</td>
      <td>904</td>
    </tr>
    <tr>
      <th>904</th>
      <td>Skyline Acrea</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>8</td>
      <td>Fredericton</td>
      <td>905</td>
    </tr>
    <tr>
      <th>905</th>
      <td>Skyline Acrea</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>8</td>
      <td>Fredericton</td>
      <td>906</td>
    </tr>
    <tr>
      <th>906</th>
      <td>Skyline Acrea</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>8</td>
      <td>Fredericton</td>
      <td>907</td>
    </tr>
    <tr>
      <th>907</th>
      <td>Skyline Acrea</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>8</td>
      <td>Fredericton</td>
      <td>908</td>
    </tr>
    <tr>
      <th>913</th>
      <td>Poet's Hill</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>8</td>
      <td>Fredericton</td>
      <td>914</td>
    </tr>
    <tr>
      <th>914</th>
      <td>Poet's Hill</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>8</td>
      <td>Fredericton</td>
      <td>915</td>
    </tr>
    <tr>
      <th>922</th>
      <td>Dun's Crossing</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>8</td>
      <td>Fredericton</td>
      <td>923</td>
    </tr>
    <tr>
      <th>923</th>
      <td>Dun's Crossing</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>8</td>
      <td>Fredericton</td>
      <td>924</td>
    </tr>
    <tr>
      <th>924</th>
      <td>Dun's Crossing</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>8</td>
      <td>Fredericton</td>
      <td>925</td>
    </tr>
    <tr>
      <th>925</th>
      <td>Dun's Crossing</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>8</td>
      <td>Fredericton</td>
      <td>926</td>
    </tr>
    <tr>
      <th>926</th>
      <td>Dun's Crossing</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>8</td>
      <td>Fredericton</td>
      <td>927</td>
    </tr>
    <tr>
      <th>927</th>
      <td>Dun's Crossing</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>8</td>
      <td>Fredericton</td>
      <td>928</td>
    </tr>
    <tr>
      <th>928</th>
      <td>Dun's Crossing</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>8</td>
      <td>Fredericton</td>
      <td>929</td>
    </tr>
    <tr>
      <th>929</th>
      <td>Dun's Crossing</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>8</td>
      <td>Fredericton</td>
      <td>930</td>
    </tr>
    <tr>
      <th>930</th>
      <td>Dun's Crossing</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>8</td>
      <td>Fredericton</td>
      <td>931</td>
    </tr>
    <tr>
      <th>938</th>
      <td>Southwood Park</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>7</td>
      <td>Fredericton</td>
      <td>939</td>
    </tr>
    <tr>
      <th>939</th>
      <td>Southwood Park</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>7</td>
      <td>Fredericton</td>
      <td>940</td>
    </tr>
    <tr>
      <th>940</th>
      <td>Southwood Park</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>7</td>
      <td>Fredericton</td>
      <td>941</td>
    </tr>
    <tr>
      <th>941</th>
      <td>Southwood Park</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>7</td>
      <td>Fredericton</td>
      <td>942</td>
    </tr>
    <tr>
      <th>946</th>
      <td>The Hill</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>9</td>
      <td>Fredericton</td>
      <td>947</td>
    </tr>
    <tr>
      <th>947</th>
      <td>The Hill</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>9</td>
      <td>Fredericton</td>
      <td>948</td>
    </tr>
    <tr>
      <th>948</th>
      <td>The Hill</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>9</td>
      <td>Fredericton</td>
      <td>949</td>
    </tr>
    <tr>
      <th>949</th>
      <td>The Hill</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>950</td>
    </tr>
    <tr>
      <th>950</th>
      <td>The Hill</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>951</td>
    </tr>
    <tr>
      <th>951</th>
      <td>The Hill</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>11</td>
      <td>Fredericton</td>
      <td>952</td>
    </tr>
    <tr>
      <th>952</th>
      <td>The Hill</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>9</td>
      <td>Fredericton</td>
      <td>953</td>
    </tr>
    <tr>
      <th>954</th>
      <td>The Hill</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>955</td>
    </tr>
    <tr>
      <th>955</th>
      <td>The Hill</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>956</td>
    </tr>
    <tr>
      <th>956</th>
      <td>The Hill</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>9</td>
      <td>Fredericton</td>
      <td>957</td>
    </tr>
    <tr>
      <th>957</th>
      <td>The Hill</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>9</td>
      <td>Fredericton</td>
      <td>958</td>
    </tr>
    <tr>
      <th>969</th>
      <td>Forest Hill</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>8</td>
      <td>Fredericton</td>
      <td>970</td>
    </tr>
    <tr>
      <th>970</th>
      <td>Forest Hill</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>8</td>
      <td>Fredericton</td>
      <td>971</td>
    </tr>
    <tr>
      <th>971</th>
      <td>Forest Hill</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>8</td>
      <td>Fredericton</td>
      <td>972</td>
    </tr>
    <tr>
      <th>972</th>
      <td>Forest Hill</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>8</td>
      <td>Fredericton</td>
      <td>973</td>
    </tr>
    <tr>
      <th>973</th>
      <td>Forest Hill</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>8</td>
      <td>Fredericton</td>
      <td>974</td>
    </tr>
    <tr>
      <th>974</th>
      <td>Forest Hill</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>8</td>
      <td>Fredericton</td>
      <td>975</td>
    </tr>
    <tr>
      <th>975</th>
      <td>Forest Hill</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>8</td>
      <td>Fredericton</td>
      <td>976</td>
    </tr>
    <tr>
      <th>976</th>
      <td>Forest Hill</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>8</td>
      <td>Fredericton</td>
      <td>977</td>
    </tr>
    <tr>
      <th>989</th>
      <td>Lincoln Heights</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>7</td>
      <td>Fredericton</td>
      <td>990</td>
    </tr>
    <tr>
      <th>996</th>
      <td>Diamond Street</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>1</td>
      <td>Fredericton</td>
      <td>997</td>
    </tr>
    <tr>
      <th>1027</th>
      <td>College Hill</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>11</td>
      <td>Fredericton</td>
      <td>1028</td>
    </tr>
    <tr>
      <th>1028</th>
      <td>College Hill</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>11</td>
      <td>Fredericton</td>
      <td>1029</td>
    </tr>
    <tr>
      <th>1029</th>
      <td>College Hill</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>11</td>
      <td>Fredericton</td>
      <td>1030</td>
    </tr>
    <tr>
      <th>1030</th>
      <td>College Hill</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>11</td>
      <td>Fredericton</td>
      <td>1031</td>
    </tr>
    <tr>
      <th>1031</th>
      <td>College Hill</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>11</td>
      <td>Fredericton</td>
      <td>1032</td>
    </tr>
    <tr>
      <th>1032</th>
      <td>College Hill</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>11</td>
      <td>Fredericton</td>
      <td>1033</td>
    </tr>
    <tr>
      <th>1033</th>
      <td>College Hill</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>11</td>
      <td>Fredericton</td>
      <td>1034</td>
    </tr>
    <tr>
      <th>1034</th>
      <td>College Hill</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>11</td>
      <td>Fredericton</td>
      <td>1035</td>
    </tr>
    <tr>
      <th>1035</th>
      <td>College Hill</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>11</td>
      <td>Fredericton</td>
      <td>1036</td>
    </tr>
    <tr>
      <th>1036</th>
      <td>College Hill</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>11</td>
      <td>Fredericton</td>
      <td>1037</td>
    </tr>
    <tr>
      <th>1060</th>
      <td>Brookside Estates</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>2</td>
      <td>Fredericton</td>
      <td>1061</td>
    </tr>
    <tr>
      <th>1061</th>
      <td>Brookside Estates</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>2</td>
      <td>Fredericton</td>
      <td>1062</td>
    </tr>
    <tr>
      <th>1062</th>
      <td>Brookside Estates</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>2</td>
      <td>Fredericton</td>
      <td>1063</td>
    </tr>
    <tr>
      <th>1116</th>
      <td>Lincoln</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>7</td>
      <td>Fredericton</td>
      <td>1117</td>
    </tr>
    <tr>
      <th>1124</th>
      <td>Colonial heights</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>1125</td>
    </tr>
    <tr>
      <th>1125</th>
      <td>Colonial heights</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>1126</td>
    </tr>
    <tr>
      <th>1126</th>
      <td>Colonial heights</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>1127</td>
    </tr>
    <tr>
      <th>1127</th>
      <td>Colonial heights</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>1128</td>
    </tr>
    <tr>
      <th>1128</th>
      <td>Colonial heights</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>11</td>
      <td>Fredericton</td>
      <td>1129</td>
    </tr>
    <tr>
      <th>1129</th>
      <td>Colonial heights</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>11</td>
      <td>Fredericton</td>
      <td>1130</td>
    </tr>
    <tr>
      <th>1131</th>
      <td>Garden Place</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>1132</td>
    </tr>
    <tr>
      <th>1132</th>
      <td>Garden Place</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>1133</td>
    </tr>
    <tr>
      <th>1133</th>
      <td>Garden Place</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>1134</td>
    </tr>
    <tr>
      <th>1144</th>
      <td>Waterloo Row</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>11</td>
      <td>Fredericton</td>
      <td>1145</td>
    </tr>
    <tr>
      <th>1145</th>
      <td>Waterloo Row</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>11</td>
      <td>Fredericton</td>
      <td>1146</td>
    </tr>
    <tr>
      <th>1146</th>
      <td>Waterloo Row</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>11</td>
      <td>Fredericton</td>
      <td>1147</td>
    </tr>
    <tr>
      <th>1151</th>
      <td>University Of New Brunswick</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>11</td>
      <td>Fredericton</td>
      <td>1152</td>
    </tr>
    <tr>
      <th>1152</th>
      <td>University Of New Brunswick</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>11</td>
      <td>Fredericton</td>
      <td>1153</td>
    </tr>
    <tr>
      <th>1153</th>
      <td>University Of New Brunswick</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>11</td>
      <td>Fredericton</td>
      <td>1154</td>
    </tr>
    <tr>
      <th>1154</th>
      <td>University Of New Brunswick</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>11</td>
      <td>Fredericton</td>
      <td>1155</td>
    </tr>
    <tr>
      <th>1163</th>
      <td>Saint Thomas University</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>11</td>
      <td>Fredericton</td>
      <td>1164</td>
    </tr>
    <tr>
      <th>1173</th>
      <td>Williams / Hawkins Area</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>2</td>
      <td>Fredericton</td>
      <td>1174</td>
    </tr>
    <tr>
      <th>1174</th>
      <td>Williams / Hawkins Area</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>2</td>
      <td>Fredericton</td>
      <td>1175</td>
    </tr>
    <tr>
      <th>1175</th>
      <td>Williams / Hawkins Area</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>2</td>
      <td>Fredericton</td>
      <td>1176</td>
    </tr>
    <tr>
      <th>1176</th>
      <td>Williams / Hawkins Area</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>2</td>
      <td>Fredericton</td>
      <td>1177</td>
    </tr>
    <tr>
      <th>1177</th>
      <td>Williams / Hawkins Area</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>2</td>
      <td>Fredericton</td>
      <td>1178</td>
    </tr>
    <tr>
      <th>1178</th>
      <td>Williams / Hawkins Area</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>2</td>
      <td>Fredericton</td>
      <td>1179</td>
    </tr>
    <tr>
      <th>1181</th>
      <td>McKnight</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>2</td>
      <td>Fredricton</td>
      <td>1182</td>
    </tr>
    <tr>
      <th>1187</th>
      <td>Shadowood Estates</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>2</td>
      <td>Fredericton</td>
      <td>1188</td>
    </tr>
    <tr>
      <th>1188</th>
      <td>Shadowood Estates</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>2</td>
      <td>Fredericton</td>
      <td>1189</td>
    </tr>
    <tr>
      <th>1240</th>
      <td>Lian / Valcore</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>1241</td>
    </tr>
    <tr>
      <th>1284</th>
      <td>North Devon</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>4</td>
      <td>Fredericton</td>
      <td>1285</td>
    </tr>
    <tr>
      <th>1285</th>
      <td>North Devon</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>4</td>
      <td>Fredericton</td>
      <td>1286</td>
    </tr>
    <tr>
      <th>1286</th>
      <td>North Devon</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>4</td>
      <td>Fredericton</td>
      <td>1287</td>
    </tr>
    <tr>
      <th>1287</th>
      <td>North Devon</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>4</td>
      <td>Fredericton</td>
      <td>1288</td>
    </tr>
    <tr>
      <th>1288</th>
      <td>North Devon</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>4</td>
      <td>Fredericton</td>
      <td>1289</td>
    </tr>
    <tr>
      <th>1289</th>
      <td>North Devon</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>4</td>
      <td>Fredericton</td>
      <td>1290</td>
    </tr>
    <tr>
      <th>1290</th>
      <td>North Devon</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>4</td>
      <td>Fredericton</td>
      <td>1291</td>
    </tr>
    <tr>
      <th>1302</th>
      <td>Rail Side</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>1303</td>
    </tr>
    <tr>
      <th>1306</th>
      <td>Rail Side</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>1307</td>
    </tr>
    <tr>
      <th>1316</th>
      <td>Silverwood</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>1317</td>
    </tr>
    <tr>
      <th>1317</th>
      <td>Silverwood</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>1318</td>
    </tr>
    <tr>
      <th>1339</th>
      <td>Prospect</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>9</td>
      <td>Fredericton</td>
      <td>1340</td>
    </tr>
    <tr>
      <th>1340</th>
      <td>Prospect</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>9</td>
      <td>Fredericton</td>
      <td>1341</td>
    </tr>
    <tr>
      <th>1341</th>
      <td>Prospect</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>9</td>
      <td>Fredericton</td>
      <td>1342</td>
    </tr>
    <tr>
      <th>1342</th>
      <td>Prospect</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>9</td>
      <td>Fredericton</td>
      <td>1343</td>
    </tr>
    <tr>
      <th>1343</th>
      <td>Prospect</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>9</td>
      <td>Fredericton</td>
      <td>1344</td>
    </tr>
    <tr>
      <th>1344</th>
      <td>Prospect</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>9</td>
      <td>Fredericton</td>
      <td>1345</td>
    </tr>
    <tr>
      <th>1345</th>
      <td>Prospect</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>11</td>
      <td>Fredericton</td>
      <td>1346</td>
    </tr>
    <tr>
      <th>1346</th>
      <td>Prospect</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>9</td>
      <td>Fredericton</td>
      <td>1347</td>
    </tr>
    <tr>
      <th>1347</th>
      <td>Prospect</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>9</td>
      <td>Fredericton</td>
      <td>1348</td>
    </tr>
    <tr>
      <th>1348</th>
      <td>Prospect</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>9</td>
      <td>Fredericton</td>
      <td>1349</td>
    </tr>
    <tr>
      <th>1349</th>
      <td>Prospect</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>9</td>
      <td>Fredericton</td>
      <td>1350</td>
    </tr>
    <tr>
      <th>1369</th>
      <td>North Devon</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>3</td>
      <td>Fredericton</td>
      <td>1370</td>
    </tr>
    <tr>
      <th>1370</th>
      <td>North Devon</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>3</td>
      <td>Fredericton</td>
      <td>1371</td>
    </tr>
    <tr>
      <th>1371</th>
      <td>North Devon</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>3</td>
      <td>Fredericton</td>
      <td>1372</td>
    </tr>
    <tr>
      <th>1372</th>
      <td>North Devon</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>3</td>
      <td>Fredericton</td>
      <td>1373</td>
    </tr>
    <tr>
      <th>1377</th>
      <td>North Devon</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>3</td>
      <td>Fredericton</td>
      <td>1378</td>
    </tr>
    <tr>
      <th>1380</th>
      <td>Hanwell North</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>1381</td>
    </tr>
    <tr>
      <th>1381</th>
      <td>Hanwell North</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>1382</td>
    </tr>
    <tr>
      <th>1382</th>
      <td>Hanwell North</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>1383</td>
    </tr>
    <tr>
      <th>1387</th>
      <td>Montogomery / Prospect East</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>11</td>
      <td>Fredericton</td>
      <td>1388</td>
    </tr>
    <tr>
      <th>1388</th>
      <td>Montogomery / Prospect East</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>11</td>
      <td>Fredericton</td>
      <td>1389</td>
    </tr>
    <tr>
      <th>1389</th>
      <td>Montogomery / Prospect East</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>9</td>
      <td>Fredericton</td>
      <td>1390</td>
    </tr>
    <tr>
      <th>1403</th>
      <td>Fredericton South</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>7</td>
      <td>Fredericton</td>
      <td>1404</td>
    </tr>
    <tr>
      <th>1408</th>
      <td>Fredericton South</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>1409</td>
    </tr>
    <tr>
      <th>1409</th>
      <td>Fredericton South</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>1410</td>
    </tr>
    <tr>
      <th>1410</th>
      <td>Fredericton South</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>1411</td>
    </tr>
    <tr>
      <th>1411</th>
      <td>Fredericton South</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>1412</td>
    </tr>
    <tr>
      <th>1412</th>
      <td>Fredericton South</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>1413</td>
    </tr>
    <tr>
      <th>1413</th>
      <td>Fredericton South</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>1414</td>
    </tr>
    <tr>
      <th>1420</th>
      <td>Woodstock Road</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>1421</td>
    </tr>
    <tr>
      <th>1421</th>
      <td>Woodstock Road</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>10</td>
      <td>Fredericton</td>
      <td>1422</td>
    </tr>
    <tr>
      <th>1437</th>
      <td>North Devon</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>3</td>
      <td>Fredericton</td>
      <td>1438</td>
    </tr>
    <tr>
      <th>1438</th>
      <td>North Devon</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>3</td>
      <td>Fredericton</td>
      <td>1439</td>
    </tr>
    <tr>
      <th>1439</th>
      <td>North Devon</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>3</td>
      <td>Fredericton</td>
      <td>1440</td>
    </tr>
    <tr>
      <th>1440</th>
      <td>North Devon</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>3</td>
      <td>Fredericton</td>
      <td>1441</td>
    </tr>
    <tr>
      <th>1441</th>
      <td>North Devon</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>3</td>
      <td>Fredericton</td>
      <td>1442</td>
    </tr>
    <tr>
      <th>1459</th>
      <td>Monteith / Talisman</td>
      <td>2142</td>
      <td>THEFT FROM MV &lt; $5000</td>
      <td>12</td>
      <td>Fredericton</td>
      <td>1460</td>
    </tr>
  </tbody>
</table>
</div>




```python
mvcrime_data = mvcrime_df.groupby(['Neighbourhood']).size().to_frame(name='Count').reset_index()
mvcrime_data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Neighbourhood</th>
      <th>Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Barkers Point</td>
      <td>8</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Brookside Estates</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>College Hill</td>
      <td>10</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Colonial heights</td>
      <td>6</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Diamond Street</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Douglas</td>
      <td>1</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Downtown</td>
      <td>21</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Dun's Crossing</td>
      <td>9</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Forest Hill</td>
      <td>8</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Fredericton South</td>
      <td>20</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Fulton Heights</td>
      <td>12</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Garden Creek</td>
      <td>1</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Garden Place</td>
      <td>3</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Gilridge Estates</td>
      <td>1</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Golf Club</td>
      <td>5</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Hanwell North</td>
      <td>3</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Heron Springs</td>
      <td>2</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Highpoint Ridge</td>
      <td>4</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Knob Hill</td>
      <td>1</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Lian / Valcore</td>
      <td>1</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Lincoln</td>
      <td>1</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Lincoln Heights</td>
      <td>11</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Main Street</td>
      <td>10</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Marysville</td>
      <td>10</td>
    </tr>
    <tr>
      <th>24</th>
      <td>McKnight</td>
      <td>1</td>
    </tr>
    <tr>
      <th>25</th>
      <td>McLeod Hill</td>
      <td>2</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Monteith / Talisman</td>
      <td>3</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Montogomery / Prospect East</td>
      <td>3</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Nashwaaksis</td>
      <td>9</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Nethervue Minihome Park</td>
      <td>1</td>
    </tr>
    <tr>
      <th>30</th>
      <td>North Devon</td>
      <td>17</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Northbrook Heights</td>
      <td>5</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Plat</td>
      <td>40</td>
    </tr>
    <tr>
      <th>33</th>
      <td>Poet's Hill</td>
      <td>2</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Prospect</td>
      <td>11</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Rail Side</td>
      <td>2</td>
    </tr>
    <tr>
      <th>36</th>
      <td>Saint Mary's First Nation</td>
      <td>1</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Saint Thomas University</td>
      <td>1</td>
    </tr>
    <tr>
      <th>38</th>
      <td>Sandyville</td>
      <td>3</td>
    </tr>
    <tr>
      <th>39</th>
      <td>Shadowood Estates</td>
      <td>2</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Silverwood</td>
      <td>2</td>
    </tr>
    <tr>
      <th>41</th>
      <td>Skyline Acrea</td>
      <td>13</td>
    </tr>
    <tr>
      <th>42</th>
      <td>South Devon</td>
      <td>22</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Southwood Park</td>
      <td>7</td>
    </tr>
    <tr>
      <th>44</th>
      <td>Sunshine Gardens</td>
      <td>7</td>
    </tr>
    <tr>
      <th>45</th>
      <td>The Hill</td>
      <td>11</td>
    </tr>
    <tr>
      <th>46</th>
      <td>University Of New Brunswick</td>
      <td>4</td>
    </tr>
    <tr>
      <th>47</th>
      <td>Waterloo Row</td>
      <td>3</td>
    </tr>
    <tr>
      <th>48</th>
      <td>Williams / Hawkins Area</td>
      <td>6</td>
    </tr>
    <tr>
      <th>49</th>
      <td>Woodstock Road</td>
      <td>20</td>
    </tr>
    <tr>
      <th>50</th>
      <td>Youngs Crossing</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>




```python
mvcrime_data.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MVCrime_Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>51.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>6.980392</td>
    </tr>
    <tr>
      <th>std</th>
      <td>7.457855</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>10.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>40.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
mvcrime_data.rename({'Platt': 'Plat'},inplace=True)
mvcrime_data.rename(index=str, columns={'Neighbourhood':'Neighbourh','Count':'MVCrime_Count'}, inplace=True)
mvcrime_data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Neighbourh</th>
      <th>MVCrime_Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Barkers Point</td>
      <td>8</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Brookside Estates</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>College Hill</td>
      <td>10</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Colonial heights</td>
      <td>6</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Diamond Street</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Douglas</td>
      <td>1</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Downtown</td>
      <td>21</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Dun's Crossing</td>
      <td>9</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Forest Hill</td>
      <td>8</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Fredericton South</td>
      <td>20</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Fulton Heights</td>
      <td>12</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Garden Creek</td>
      <td>1</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Garden Place</td>
      <td>3</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Gilridge Estates</td>
      <td>1</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Golf Club</td>
      <td>5</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Hanwell North</td>
      <td>3</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Heron Springs</td>
      <td>2</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Highpoint Ridge</td>
      <td>4</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Knob Hill</td>
      <td>1</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Lian / Valcore</td>
      <td>1</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Lincoln</td>
      <td>1</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Lincoln Heights</td>
      <td>11</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Main Street</td>
      <td>10</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Marysville</td>
      <td>10</td>
    </tr>
    <tr>
      <th>24</th>
      <td>McKnight</td>
      <td>1</td>
    </tr>
    <tr>
      <th>25</th>
      <td>McLeod Hill</td>
      <td>2</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Monteith / Talisman</td>
      <td>3</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Montogomery / Prospect East</td>
      <td>3</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Nashwaaksis</td>
      <td>9</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Nethervue Minihome Park</td>
      <td>1</td>
    </tr>
    <tr>
      <th>30</th>
      <td>North Devon</td>
      <td>17</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Northbrook Heights</td>
      <td>5</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Plat</td>
      <td>40</td>
    </tr>
    <tr>
      <th>33</th>
      <td>Poet's Hill</td>
      <td>2</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Prospect</td>
      <td>11</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Rail Side</td>
      <td>2</td>
    </tr>
    <tr>
      <th>36</th>
      <td>Saint Mary's First Nation</td>
      <td>1</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Saint Thomas University</td>
      <td>1</td>
    </tr>
    <tr>
      <th>38</th>
      <td>Sandyville</td>
      <td>3</td>
    </tr>
    <tr>
      <th>39</th>
      <td>Shadowood Estates</td>
      <td>2</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Silverwood</td>
      <td>2</td>
    </tr>
    <tr>
      <th>41</th>
      <td>Skyline Acrea</td>
      <td>13</td>
    </tr>
    <tr>
      <th>42</th>
      <td>South Devon</td>
      <td>22</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Southwood Park</td>
      <td>7</td>
    </tr>
    <tr>
      <th>44</th>
      <td>Sunshine Gardens</td>
      <td>7</td>
    </tr>
    <tr>
      <th>45</th>
      <td>The Hill</td>
      <td>11</td>
    </tr>
    <tr>
      <th>46</th>
      <td>University Of New Brunswick</td>
      <td>4</td>
    </tr>
    <tr>
      <th>47</th>
      <td>Waterloo Row</td>
      <td>3</td>
    </tr>
    <tr>
      <th>48</th>
      <td>Williams / Hawkins Area</td>
      <td>6</td>
    </tr>
    <tr>
      <th>49</th>
      <td>Woodstock Road</td>
      <td>20</td>
    </tr>
    <tr>
      <th>50</th>
      <td>Youngs Crossing</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>




```python
world_geo = r'world_countries.json' # geojson file

fredericton_c_map = folium.Map(location=[45.91, -66.65], width=1000, height=750,zoom_start=12)

fredericton_c_map
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><iframe src="data:text/html;charset=utf-8;base64,PCFET0NUWVBFIGh0bWw+CjxoZWFkPiAgICAKICAgIDxtZXRhIGh0dHAtZXF1aXY9ImNvbnRlbnQtdHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PVVURi04IiAvPgogICAgPHNjcmlwdD5MX1BSRUZFUl9DQU5WQVMgPSBmYWxzZTsgTF9OT19UT1VDSCA9IGZhbHNlOyBMX0RJU0FCTEVfM0QgPSBmYWxzZTs8L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2FqYXguZ29vZ2xlYXBpcy5jb20vYWpheC9saWJzL2pxdWVyeS8xLjExLjEvanF1ZXJ5Lm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvanMvYm9vdHN0cmFwLm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvTGVhZmxldC5hd2Vzb21lLW1hcmtlcnMvMi4wLjIvbGVhZmxldC5hd2Vzb21lLW1hcmtlcnMuanMiPjwvc2NyaXB0PgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9jc3MvYm9vdHN0cmFwLm1pbi5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvY3NzL2Jvb3RzdHJhcC10aGVtZS5taW4uY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vbWF4Y2RuLmJvb3RzdHJhcGNkbi5jb20vZm9udC1hd2Vzb21lLzQuNi4zL2Nzcy9mb250LWF3ZXNvbWUubWluLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9MZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy8yLjAuMi9sZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9yYXdnaXQuY29tL3B5dGhvbi12aXN1YWxpemF0aW9uL2ZvbGl1bS9tYXN0ZXIvZm9saXVtL3RlbXBsYXRlcy9sZWFmbGV0LmF3ZXNvbWUucm90YXRlLmNzcyIvPgogICAgPHN0eWxlPmh0bWwsIGJvZHkge3dpZHRoOiAxMDAlO2hlaWdodDogMTAwJTttYXJnaW46IDA7cGFkZGluZzogMDt9PC9zdHlsZT4KICAgIDxzdHlsZT4jbWFwIHtwb3NpdGlvbjphYnNvbHV0ZTt0b3A6MDtib3R0b206MDtyaWdodDowO2xlZnQ6MDt9PC9zdHlsZT4KICAgIAogICAgICAgICAgICA8c3R5bGU+ICNtYXBfNGY3M2EyZmE4YzMwNDljYTg0MTIxZDZlNDc0NzBhNzMgewogICAgICAgICAgICAgICAgcG9zaXRpb24gOiByZWxhdGl2ZTsKICAgICAgICAgICAgICAgIHdpZHRoIDogMTAwMC4wcHg7CiAgICAgICAgICAgICAgICBoZWlnaHQ6IDc1MC4wcHg7CiAgICAgICAgICAgICAgICBsZWZ0OiAwLjAlOwogICAgICAgICAgICAgICAgdG9wOiAwLjAlOwogICAgICAgICAgICAgICAgfQogICAgICAgICAgICA8L3N0eWxlPgogICAgICAgIAo8L2hlYWQ+Cjxib2R5PiAgICAKICAgIAogICAgICAgICAgICA8ZGl2IGNsYXNzPSJmb2xpdW0tbWFwIiBpZD0ibWFwXzRmNzNhMmZhOGMzMDQ5Y2E4NDEyMWQ2ZTQ3NDcwYTczIiA+PC9kaXY+CiAgICAgICAgCjwvYm9keT4KPHNjcmlwdD4gICAgCiAgICAKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGJvdW5kcyA9IG51bGw7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgdmFyIG1hcF80ZjczYTJmYThjMzA0OWNhODQxMjFkNmU0NzQ3MGE3MyA9IEwubWFwKAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ21hcF80ZjczYTJmYThjMzA0OWNhODQxMjFkNmU0NzQ3MGE3MycsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB7Y2VudGVyOiBbNDUuOTEsLTY2LjY1XSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHpvb206IDEyLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbWF4Qm91bmRzOiBib3VuZHMsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBsYXllcnM6IFtdLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgd29ybGRDb3B5SnVtcDogZmFsc2UsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBjcnM6IEwuQ1JTLkVQU0czODU3CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIH0pOwogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgdGlsZV9sYXllcl8zZGMxOWMwZmUyNDc0ZDUxOGM2Y2ZkNzgzYzUxZDQ2YyA9IEwudGlsZUxheWVyKAogICAgICAgICAgICAgICAgJ2h0dHBzOi8ve3N9LnRpbGUub3BlbnN0cmVldG1hcC5vcmcve3p9L3t4fS97eX0ucG5nJywKICAgICAgICAgICAgICAgIHsKICAiYXR0cmlidXRpb24iOiBudWxsLAogICJkZXRlY3RSZXRpbmEiOiBmYWxzZSwKICAibWF4Wm9vbSI6IDE4LAogICJtaW5ab29tIjogMSwKICAibm9XcmFwIjogZmFsc2UsCiAgInN1YmRvbWFpbnMiOiAiYWJjIgp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80ZjczYTJmYThjMzA0OWNhODQxMjFkNmU0NzQ3MGE3Myk7CiAgICAgICAgCjwvc2NyaXB0Pg==" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>




```python
## Motor Vehicle Crime <$5000 Count 
fredericton_geo = r.json()
threshold_scale = np.linspace(mvcrime_data['MVCrime_Count'].min(), mvcrime_data['MVCrime_Count'].max(),6,dtype=int)
threshold_scale = threshold_scale.tolist()
threshold_scale[-1] = threshold_scale[-1]+1

fredericton_c_map.choropleth(geo_data=fredericton_geo,data=mvcrime_data,columns=['Neighbourh', 'MVCrime_Count'],key_on='feature.properties.Neighbourh',
    threshold_scale=threshold_scale, fill_color='YlOrRd',fill_opacity=0.7,line_opacity=0.1,legend_name='Fredericton Neighbourhoods')
fredericton_c_map
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><iframe src="data:text/html;charset=utf-8;base64,PCFET0NUWVBFIGh0bWw+CjxoZWFkPiAgICAKICAgIDxtZXRhIGh0dHAtZXF1aXY9ImNvbnRlbnQtdHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PVVURi04IiAvPgogICAgPHNjcmlwdD5MX1BSRUZFUl9DQU5WQVMgPSBmYWxzZTsgTF9OT19UT1VDSCA9IGZhbHNlOyBMX0RJU0FCTEVfM0QgPSBmYWxzZTs8L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2FqYXguZ29vZ2xlYXBpcy5jb20vYWpheC9saWJzL2pxdWVyeS8xLjExLjEvanF1ZXJ5Lm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvanMvYm9vdHN0cmFwLm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvTGVhZmxldC5hd2Vzb21lLW1hcmtlcnMvMi4wLjIvbGVhZmxldC5hd2Vzb21lLW1hcmtlcnMuanMiPjwvc2NyaXB0PgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9jc3MvYm9vdHN0cmFwLm1pbi5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvY3NzL2Jvb3RzdHJhcC10aGVtZS5taW4uY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vbWF4Y2RuLmJvb3RzdHJhcGNkbi5jb20vZm9udC1hd2Vzb21lLzQuNi4zL2Nzcy9mb250LWF3ZXNvbWUubWluLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9MZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy8yLjAuMi9sZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9yYXdnaXQuY29tL3B5dGhvbi12aXN1YWxpemF0aW9uL2ZvbGl1bS9tYXN0ZXIvZm9saXVtL3RlbXBsYXRlcy9sZWFmbGV0LmF3ZXNvbWUucm90YXRlLmNzcyIvPgogICAgPHN0eWxlPmh0bWwsIGJvZHkge3dpZHRoOiAxMDAlO2hlaWdodDogMTAwJTttYXJnaW46IDA7cGFkZGluZzogMDt9PC9zdHlsZT4KICAgIDxzdHlsZT4jbWFwIHtwb3NpdGlvbjphYnNvbHV0ZTt0b3A6MDtib3R0b206MDtyaWdodDowO2xlZnQ6MDt9PC9zdHlsZT4KICAgIAogICAgICAgICAgICA8c3R5bGU+ICNtYXBfNGY3M2EyZmE4YzMwNDljYTg0MTIxZDZlNDc0NzBhNzMgewogICAgICAgICAgICAgICAgcG9zaXRpb24gOiByZWxhdGl2ZTsKICAgICAgICAgICAgICAgIHdpZHRoIDogMTAwMC4wcHg7CiAgICAgICAgICAgICAgICBoZWlnaHQ6IDc1MC4wcHg7CiAgICAgICAgICAgICAgICBsZWZ0OiAwLjAlOwogICAgICAgICAgICAgICAgdG9wOiAwLjAlOwogICAgICAgICAgICAgICAgfQogICAgICAgICAgICA8L3N0eWxlPgogICAgICAgIAogICAgPHNjcmlwdCBzcmM9Imh0dHBzOi8vY2RuanMuY2xvdWRmbGFyZS5jb20vYWpheC9saWJzL2QzLzMuNS41L2QzLm1pbi5qcyI+PC9zY3JpcHQ+CjwvaGVhZD4KPGJvZHk+ICAgIAogICAgCiAgICAgICAgICAgIDxkaXYgY2xhc3M9ImZvbGl1bS1tYXAiIGlkPSJtYXBfNGY3M2EyZmE4YzMwNDljYTg0MTIxZDZlNDc0NzBhNzMiID48L2Rpdj4KICAgICAgICAKPC9ib2R5Pgo8c2NyaXB0PiAgICAKICAgIAoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgYm91bmRzID0gbnVsbDsKICAgICAgICAgICAgCgogICAgICAgICAgICB2YXIgbWFwXzRmNzNhMmZhOGMzMDQ5Y2E4NDEyMWQ2ZTQ3NDcwYTczID0gTC5tYXAoCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAnbWFwXzRmNzNhMmZhOGMzMDQ5Y2E4NDEyMWQ2ZTQ3NDcwYTczJywKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHtjZW50ZXI6IFs0NS45MSwtNjYuNjVdLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgem9vbTogMTIsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBtYXhCb3VuZHM6IGJvdW5kcywKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGxheWVyczogW10sCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB3b3JsZENvcHlKdW1wOiBmYWxzZSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGNyczogTC5DUlMuRVBTRzM4NTcKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgfSk7CiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciB0aWxlX2xheWVyXzNkYzE5YzBmZTI0NzRkNTE4YzZjZmQ3ODNjNTFkNDZjID0gTC50aWxlTGF5ZXIoCiAgICAgICAgICAgICAgICAnaHR0cHM6Ly97c30udGlsZS5vcGVuc3RyZWV0bWFwLm9yZy97en0ve3h9L3t5fS5wbmcnLAogICAgICAgICAgICAgICAgewogICJhdHRyaWJ1dGlvbiI6IG51bGwsCiAgImRldGVjdFJldGluYSI6IGZhbHNlLAogICJtYXhab29tIjogMTgsCiAgIm1pblpvb20iOiAxLAogICJub1dyYXAiOiBmYWxzZSwKICAic3ViZG9tYWlucyI6ICJhYmMiCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzRmNzNhMmZhOGMzMDQ5Y2E4NDEyMWQ2ZTQ3NDcwYTczKTsKICAgICAgICAKICAgIAoKICAgICAgICAgICAgCgogICAgICAgICAgICAgICAgdmFyIGdlb19qc29uX2MzOWZjOGZiODE2ZTQ4NzNiZmVlYjlmOWM4MzAzNTU0ID0gTC5nZW9Kc29uKAogICAgICAgICAgICAgICAgICAgIHsiZmVhdHVyZXMiOiBbeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjE5MzQ4OTMxMTk0NiwgNDUuODY4ODkyNTg1OTY2NF0sIFstNjYuNTk4NjA2ODMxMjg0MywgNDUuODkzNDMxNzU3NTQ5OF0sIFstNjYuNTk5ODQ2NTA2Mzc2NCwgNDUuODk2Mjg4OTUzMzg5NF0sIFstNjYuNjAwNTU2MTc1NDUwOCwgNDUuODk4Nzk1OTEyMjQxNF0sIFstNjYuNjAwNzYyNzg3OTY2MiwgNDUuOTAwNDE1MDU5OTE4OV0sIFstNjYuNjAwNTExMjU5Njg2NiwgNDUuOTAyMDM0MTYwMzgwM10sIFstNjYuNTk5MzcwMzk5Mjc1OCwgNDUuOTA0OTQwOTIxMTA1NF0sIFstNjYuNTk4MzkxMjM1NjE2MSwgNDUuOTA2NjUzNjUwNzg3NV0sIFstNjYuNTk1MDQwNTE5NjA2MywgNDUuOTExMDk3NzUwMzE4Ml0sIFstNjYuNTkyNDcxMzM3ODkzOCwgNDUuOTEzNzE2NTM5NjcyNV0sIFstNjYuNTk3NTE5ODY5NzkwNSwgNDUuOTE1MTkxNTA3NDM3NV0sIFstNjYuNjAxNjE2MTg3NDg2MSwgNDUuOTE2NTkxNDQwNTc4OV0sIFstNjYuNjA2Mzg2MjQxNjQ0OCwgNDUuOTE4NDY2Mjk1NzEzNF0sIFstNjYuNjEwMjMxMDMxMDYwOCwgNDUuOTIwMTg0ODU3MjcxNl0sIFstNjYuNjE5MzkzODQ2OTU4OCwgNDUuOTI2NDE0OTc3Nzc4N10sIFstNjYuNjE5NDI5Nzc5NTcwMiwgNDUuOTI0MzQ2NjgwMzQ2MV0sIFstNjYuNjIwNjY5NDU0NjYyMywgNDUuOTIyMTM0NTc5MDIyN10sIFstNjYuNjI0MTQ1OTM0ODExOCwgNDUuOTE4MTEwMDc4MTEyNF0sIFstNjYuNjI0OTYzNDAxNzIwNCwgNDUuOTE3Nzk3NjA0NjQ5N10sIFstNjYuNjI1ODc5NjgzMzEwMiwgNDUuOTE3OTEwMDk1Mjk5XSwgWy02Ni42MjkyMTI0MzMwMTQzLCA0NS45MjAwMzQ4NzU4Mzc0XSwgWy02Ni42MzI3MzM4Mjg5MjgsIDQ1LjkyMjU3MjAwNzE4NDZdLCBbLTY2LjYzNTYzNTM4NzI5NTcsIDQ1LjkyNDQwOTE2NzgwM10sIFstNjYuNjM2MjczMTkxMTQ3NCwgNDUuOTI0OTg0MDQ5MTA0NF0sIFstNjYuNjM4MTk1NTg1ODU1NSwgNDUuOTI1ODkwMDk5OTMxM10sIFstNjYuNjQwMDI4MTQ5MDM1MSwgNDUuOTI3MjE0NzgyMDkxNV0sIFstNjYuNjQ2OTcyMTI2MTgxMywgNDUuOTMwOTUxMjE1MDc5MV0sIFstNjYuNjQ5MjYyODMwMTU1OCwgNDUuOTMyNDI1NzI0NzE3M10sIFstNjYuNjUwMTUyMTYyMjg3MSwgNDUuOTMzMTI1NDc4Mjg2OF0sIFstNjYuNjUwNDMwNjQwMDI1MiwgNDUuOTMzNzU2NDk4NDg4NF0sIFstNjYuNjUwNTY1Mzg3MzE3OCwgNDUuOTM0NzQzNjI0NjAwNV0sIFstNjYuNjUwMzU4Nzc0ODAyNCwgNDUuOTM1NzE4MjM4MjA2OV0sIFstNjYuNjUyMDc0NTU2OTk1MSwgNDUuOTM1MjI0Njg2MDIxM10sIFstNjYuNjUzMjUxMzUwMDE3MywgNDUuOTM1MDg3MjQwMzI2OV0sIFstNjYuNjU0MTg1NTk3OTEyOCwgNDUuOTM1MTEyMjMwNDc4NV0sIFstNjYuNjU1Nzc1NjE1OTY1NywgNDUuOTM1MzgwODczODk2OV0sIFstNjYuNjU5NzQ2MTY5NTIxNSwgNDUuOTM2NTYxNjQwMDAyN10sIFstNjYuNjY5MjMyMzc4OTIxOCwgNDUuOTQwODY1OTEzMDc0N10sIFstNjYuNjcwMjIwNTI1NzM0MywgNDUuOTQxMTcyMDA5NzU0M10sIFstNjYuNjcwNTg4ODM1MDAwOCwgNDUuOTQxNTcxODA2OTU0MV0sIFstNjYuNjcxNzAyNzQ1OTUzMSwgNDUuOTQxODY1NDA2MTg2N10sIFstNjYuNjgwNTYwMTM0NjU0NSwgNDUuOTQ1NjU3MDY5MzM5MV0sIFstNjYuNjgwODIwNjQ2MDg2OSwgNDUuOTQ1NjEzMzQ0ODgzXSwgWy02Ni42OTA5OTg1NTgyNTYsIDQ1Ljk0OTg3OTQ0MDA1MjZdLCBbLTY2LjY5MzIzNTM2MzMxMzQsIDQ1Ljk1MDM3OTEwNzYxMDddLCBbLTY2LjY5NTY2OTc5NzczMzQsIDQ1Ljk1MDQ0NzgxMTU0NzZdLCBbLTY2LjY5NTU1MzAxNjc0NjUsIDQ1Ljk0OTg2MDcwMjQzMTZdLCBbLTY2LjY5NTAxNDAyNzU3NiwgNDUuOTQ5ODYwNzAyNDMxNl0sIFstNjYuNjk1NjI0ODgxOTY5MiwgNDUuOTQ4MjYxNzM1NDM1XSwgWy02Ni42OTk3NjYxMTU0MjksIDQ1Ljk0NTI1MTA1NTIwNTJdLCBbLTY2LjY5OTM5NzgwNjE2MjUsIDQ1Ljk0NTA1MTE3MDIzMTVdLCBbLTY2LjY5OTY3NjI4MzkwMDYsIDQ1Ljk0NDg1MTI4NDUzNzFdLCBbLTY2LjY5OTIyNzEyNjI1ODUsIDQ1Ljk0NDYxMzkxOTMzODldLCBbLTY2LjcwMjIzNjQ4MjQ2MDMsIDQ1Ljk0MDc3MjIwOTY3MTZdLCBbLTY2LjcwNDEwNDk3ODI1MTMsIDQ1LjkzOTM2NjYzOTYyMjVdLCBbLTY2LjcwNDYwODAzNDgxMDQsIDQ1LjkzODc5MTkwNzM4MzVdLCBbLTY2LjcwNjE0NDE1Mzk0NjMsIDQ1LjkzOTA5ODAxNTUxMzJdLCBbLTY2LjcwNTE5MTkzOTc0NTEsIDQ1LjkzODg1NDM3ODU2NzZdLCBbLTY2LjcwNTY5NDk5NjMwNDIsIDQ1LjkzNzQwNTAyODk3MV0sIFstNjYuNzA2NjExMjc3ODk0LCA0NS45MzYyNDMwMjMwNTQxXSwgWy02Ni43MDc0MTA3Nzg0OTY5LCA0NS45MzU2NzQ1MDU5MTIxXSwgWy02Ni43MDg3MTMzMzU2NTg4LCA0NS45MzUwNDM1MDc1MzQ1XSwgWy02Ni43MTEwOTM4NzExNjE4LCA0NS45MzQyMDYzMzAyODgyXSwgWy02Ni43MTIyNTI2OTc4NzgzLCA0NS45MzA5MjYyMjMwNTI1XSwgWy02Ni43MDk2MDI2Njc3OTAxLCA0NS45MjkzODkxOTE3NzE4XSwgWy02Ni42NzQ2NDAyMzY5MzIyLCA0NS45MDYxMjg1ODU5OTA4XSwgWy02Ni42MTkzNDg5MzExOTQ2LCA0NS44Njg4OTI1ODU5NjY0XV0sIFtbLTY2LjY5MzQxNTAyNjM3MDMsIDQ1LjkzODY0ODIyMzM5M10sIFstNjYuNzAwMTk3MzA2NzY1NCwgNDUuOTQyMjMzOTY0NzI0N10sIFstNjYuNjkzOTE4MDgyOTI5NCwgNDUuOTQ2NzYyNjYxOTgzOF0sIFstNjYuNjkxMjE0MTUzOTI0MiwgNDUuOTQ0OTI2MjQxNzU2OV0sIFstNjYuNjg5OTQ3NTI5MzczNiwgNDUuOTQ0NTAxNDgyODM3Nl0sIFstNjYuNjg5MDMxMjQ3NzgzOCwgNDUuOTQ0NDcwMjUwNDM1N10sIFstNjYuNjg4OTY4MzY1NzEzOSwgNDUuOTQ0MzgyNzk5NjE2N10sIFstNjYuNjg5OTU2NTEyNTI2NCwgNDUuOTQxODQwNDE5MDc4NV0sIFstNjYuNjkzNDE1MDI2MzcwMywgNDUuOTM4NjQ4MjIzMzkzXV0sIFtbLTY2LjY1NTAxMjA0Nzk3NDIsIDQ1LjkyOTE0NTUxMjE2OTNdLCBbLTY2LjY1NTc3NTYxNTk2NTcsIDQ1LjkyOTI3MDQ3NjIwMTddLCBbLTY2LjY1OTk3OTczMTQ5NTQsIDQ1LjkzMDkzODcxOTA2NzJdLCBbLTY2LjY2MjkxNzIyMjQ3NDQsIDQ1LjkzMjI3NTc3NjM3NTJdLCBbLTY2LjY2MzE4NjcxNzA1OTcsIDQ1LjkzMjQ3NTcwNzQwOF0sIFstNjYuNjYzMTIzODM0OTg5OCwgNDUuOTMyNzg4MDk4MjAzN10sIFstNjYuNjYxOTI5MDc1NjYxOSwgNDUuOTM0MTgxMzM5NzI4M10sIFstNjYuNjYxNjE0NjY1MzEyNSwgNDUuOTM0MDc1MTI5NzIzNV0sIFstNjYuNjYwMTg2MzQ0MDEwNywgNDUuOTM0ODE4NTk1NDg2XSwgWy02Ni42NTkxNDQyOTgyODExLCA0NS45MzUwOTk3MzU0MDQxXSwgWy02Ni42NTg2MDUzMDkxMTA2LCA0NS45MzUxMDU5ODI5NDE2XSwgWy02Ni42NTY0NjczMTg3MzQ1LCA0NS45MzQ4NzQ4MjM1ODM3XSwgWy02Ni42NTQyOTMzOTU3NDY5LCA0NS45MzQwNTAxMzkxMDQ1XSwgWy02Ni42NTI5OTA4Mzg1ODQ5LCA0NS45MzMzMTI5MTA3Nzk0XSwgWy02Ni42NTIzMDgxMTg5NjksIDQ1LjkzMjQ1Njk2MzkwNDNdLCBbLTY2LjY1MjE5MTMzNzk4MiwgNDUuOTMxOTY5NjMwNTg0NV0sIFstNjYuNjUyMjcyMTg2MzU3NiwgNDUuOTMxMzU3MzMzOTMzNV0sIFstNjYuNjUyMDQ3NjA3NTM2NiwgNDUuOTMwNTgyNTgxNTQ0NF0sIFstNjYuNjUyMTI4NDU1OTEyMSwgNDUuOTMwMTI2NDcyMjU0NF0sIFstNjYuNjUyNDQyODY2MjYxNiwgNDUuOTI5NjAxNjI5NTI2MV0sIFstNjYuNjUzMTE2NjAyNzI0NywgNDUuOTI5MzM5MjA2Mjk5Nl0sIFstNjYuNjU0MDUwODUwNjIwMiwgNDUuOTI5MTU4MDA4NTg1Ml0sIFstNjYuNjU1MDEyMDQ3OTc0MiwgNDUuOTI5MTQ1NTEyMTY5M11dLCBbWy02Ni42MzE4MDg1NjQxODU0LCA0NS44ODc4MzU3MjkzMzczXSwgWy02Ni42MzI4Nzc1NTkzNzM1LCA0NS44ODc5MzU3NzUwMTQ4XSwgWy02Ni42MzQxODAxMTY1MzU0LCA0NS44ODgyMTA4OTk2OTg3XSwgWy02Ni42MzUxNTAyOTcwNDIzLCA0NS44ODg1NDIyOTgwNzY5XSwgWy02Ni42MzYyNDYyNDE2ODg5LCA0NS44ODkwOTg3OTI3OTI0XSwgWy02Ni42MzcwMDk4MDk2ODA0LCA0NS44ODk2MzY1MjM5NjI0XSwgWy02Ni42MzgxNTk2NTMyNDQxLCA0NS44OTA5MTgzMDQwMTIzXSwgWy02Ni42Mzg1ODE4NjE0Mjc2LCA0NS44OTE4MTg2NTg2NTMyXSwgWy02Ni42Mzg3NDM1NTgxNzg4LCA0NS44OTI1Njg5NDMwMzc4XSwgWy02Ni42Mzg1OTA4NDQ1ODA1LCA0NS44OTQwNzU3MzM1NTgyXSwgWy02Ni42MzI3NTE3OTUyMzM3LCA0NS45MDA3MzM4ODI2NjJdLCBbLTY2LjYyOTIzMDM5OTMyLCA0NS45MDUwOTcxOTQyNTI1XSwgWy02Ni42Mjc2NjczMzA3MjU2LCA0NS45MDY0ODQ4ODA1MDE2XSwgWy02Ni42MjY0NTQ2MDUwOTIsIDQ1LjkwNzE5NzQ2MjY2MjddLCBbLTY2LjYyNTM4NTYwOTkwMzksIDQ1LjkwNzY2NjI2MTcyNzRdLCBbLTY2LjYyMzAyMzA0MDcwNjcsIDQ1LjkwODI5MTMyMDk4ODJdLCBbLTY2LjYyMDUwNzc1NzkxMTEsIDQ1LjkwODQ5MTMzODQ2NTFdLCBbLTY2LjYxODAwMTQ1ODI2ODUsIDQ1LjkwODI0MTMxNjUwNjRdLCBbLTY2LjYxODEwOTI1NjEwMjUsIDQ1LjkwODIxMDA2MzY4MjNdLCBbLTY2LjYxNzAzMTI3Nzc2MTYsIDQ1LjkwNzYwMzc1NTQxNDJdLCBbLTY2LjYxNjEyMzk3OTMyNDYsIDQ1LjkwNjg2NjE3NTYwMjhdLCBbLTY2LjYxNTA5MDkxNjc0NzksIDQ1LjkwNTQ5NzI1MTUwNDddLCBbLTY2LjYxNDc5NDQ3MjcwNDEsIDQ1LjkwNDc1MzM5Mjc0ODFdLCBbLTY2LjYxNDY0MTc1OTEwNTgsIDQ1LjkwMzc5MDczNzIwODNdLCBbLTY2LjYxNDY5NTY1ODAyMjksIDQ1LjkwMzAxNTU5OTgzNjddLCBbLTY2LjYxNDk3NDEzNTc2MSwgNDUuOTAyMDY1NDE2NjgxNF0sIFstNjYuNjE3MzQ1Njg4MTExLCA0NS44OTg5NzcyMDkxMTY0XSwgWy02Ni42MjAzODE5OTM3NzE0LCA0NS44OTU0MTk5MzEyNjE0XSwgWy02Ni42MjYzNDY4MDcyNTc5LCA0NS44ODkyMzYzNTI0MjQ0XSwgWy02Ni42MjgxMjU0NzE1MjA1LCA0NS44ODgzNjcyMTk5MzQ4XSwgWy02Ni42MjkxMzE1ODQ2Mzg3LCA0NS44ODgwNzk1OTAzNjA1XSwgWy02Ni42MzA0NTIxMDgxMDY0LCA0NS44ODc4NzMyNDY0ODc1XSwgWy02Ni42MzE4MDg1NjQxODU0LCA0NS44ODc4MzU3MjkzMzczXV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiAxLCAiTmVpZ2hib3VyaCI6ICJGcmVkZXJpY3RvbiBTb3V0aCIsICJPQkpFQ1RJRCI6IDEsICJTaGFwZV9BcmVhIjogMzI0MzE4ODkuMDAwMiwgIlNoYXBlX0xlbmciOiA0MDQxMi4yNzY3NDI5LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZDhkM2MiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjYzNTcxNjIzNTY3MTMsIDQ2LjAwODY5MDU3MjYyMzVdLCBbLTY2LjY0MDYzOTAwMzQyODMsIDQ2LjAwMjk3NTEzMTYwMzVdLCBbLTY2LjYzOTMxODQ3OTk2MDYsIDQ2LjAwMjM4ODU3OTEzODNdLCBbLTY2LjYzODIyMjUzNTMxNCwgNDYuMDAxNjE0ODE5NTY1Nl0sIFstNjYuNjM3Mzg3MTAyMDk5OCwgNDYuMDAwNjk3NTI2MDUzOF0sIFstNjYuNjM2ODU3MDk2MDgyMSwgNDUuOTk5Njc0MTMzMDMxNF0sIFstNjYuNjM2ODMwMTQ2NjIzNiwgNDUuOTk4ODUwNDEyNzAzM10sIFstNjYuNjM3MDI3Nzc1OTg2MSwgNDUuOTk3ODM5NDY2NDQ5OF0sIFstNjYuNjM3NDQ5OTg0MTY5NiwgNDUuOTk2ODU5NzA0NjE3Ml0sIFstNjYuNjM4MTA1NzU0MzI3LCA0NS45OTU5NDIzMzIyNzE0XSwgWy02Ni42Mzg5NzcxMjAxNTI2LCA0NS45OTUxMTIzMTU2MTU5XSwgWy02Ni42NDAwMTkxNjU4ODIyLCA0NS45OTQ0MDA4NjI4NTk3XSwgWy02Ni42NDEyODU3OTA0MzI4LCA0NS45OTM4MDE3Mzc2NTVdLCBbLTY2LjY0Mjk2NTY0MDAxNDEsIDQ1Ljk5MzE4Mzg4Mjk5NDNdLCBbLTY2LjY0NDc1MzI4NzQyOTUsIDQ1Ljk5MjcyMjA0NzczMjldLCBbLTY2LjY0NjYxMjgwMDA2NzcsIDQ1Ljk5MjQyMjQ3Njg1NF0sIFstNjYuNjQ4NTA4MjQ1MzE3MiwgNDUuOTkyMjg1MTcyOTkyNV0sIFstNjYuNjUwMDI2Mzk4MTQ3MywgNDUuOTkyMzAzODk2MjY2NF0sIFstNjYuNjUxNzY5MTI5Nzk4NSwgNDUuOTkwMzU2NjQxODU2M10sIFstNjYuNjQ1MjIwNDExMzc3MywgNDUuOTkxMTI0MzE3NjQwOF0sIFstNjYuNjQzMTM2MzE5OTE4MSwgNDUuOTkxMTExODM1MTkyOV0sIFstNjYuNjQxMDk3MTQ0MjIzMiwgNDUuOTkwODYyMTg1NjQzM10sIFstNjYuNjM5Nzc2NjIwNzU1NSwgNDUuOTkwNTYyNjA0Njk3M10sIFstNjYuNjM4MjA0NTY5MDA4MywgNDUuOTkwMDUwODE2ODNdLCBbLTY2LjYzNjE2NTM5MzMxMzMsIDQ1Ljk4ODgwMjUzMzg5MjFdLCBbLTY2LjYzNTE5NTIxMjgwNjUsIDQ1Ljk4ODM5NjgzNTg3NThdLCBbLTY2LjYzMzg5MjY1NTY0NDUsIDQ1Ljk4ODExNTk2NjI3NjVdLCBbLTY2LjYzMjc2OTc2MTUzOTQsIDQ1Ljk4ODA2NjAzMzc1NDFdLCBbLTY2LjYzMTg3MTQ0NjI1NTIsIDQ1Ljk4ODE1MzQxNTYzODhdLCBbLTY2LjYzMDY0MDc1NDMxNiwgNDUuOTg3OTE2MjM1OTE2Nl0sIFstNjYuNjI5MDc3Njg1NzIxNiwgNDUuOTg3MzE3MDQwNTEyOF0sIFstNjYuNjI3NjQ5MzY0NDE5OSwgNDUuOTg2MzEyMTI1MzI3MV0sIFstNjYuNjI1Nzg5ODUxNzgxOCwgNDUuOTg1NjgxNzAzMzgzMV0sIFstNjYuNjIzODMxNTI0NDYyNCwgNDUuOTg1MjA3MzIxNzQxXSwgWy02Ni41OTk2MDM5NjEyNDk3LCA0Ni4wMTQ5OTE4NDgxODQ4XSwgWy02Ni42MjMxMDM4ODkwODIyLCA0Ni4wMjIxMjIwMjk3MjcyXSwgWy02Ni42NjY0NjU1Njc4NDY3LCA0Ni4wMjA0MTkxMDQwNjM1XSwgWy02Ni42NjM4ODc0MDI5ODEzLCA0Ni4wMTQ2NDI0ODkzMjkxXSwgWy02Ni42NjA1NzI2MTk1ODI5LCA0Ni4wMDYwNTEzMTAyNTE1XSwgWy02Ni42NTk0Njc2OTE3ODM0LCA0Ni4wMDI0MjYwMTg4NDMyXSwgWy02Ni42NTk1MDM2MjQzOTQ4LCA0Ni4wMDEyMDI5NzUzODAzXSwgWy02Ni42NTg0MjU2NDYwNTM4LCA0Ni4wMDE5ODkyMjA3MTAxXSwgWy02Ni42NTY5ODgzNDE1OTkyLCA0Ni4wMDI0MTM1Mzg5NDQ0XSwgWy02Ni42NTU2MTM5MTkyMTQ1LCA0Ni4wMDI0Mzg0OTg3MzkyXSwgWy02Ni42NTQxNDk2NjUzMDE0LCA0Ni4wMDIwNTc4NjA2NDUxXSwgWy02Ni42NTQ4NjgzMTc1Mjg3LCA0Ni4wMDMwMjUwNTA2NzUxXSwgWy02Ni42NTUyNDU2MDk5NDgsIDQ2LjAwNDA3MzM0MDc3MzhdLCBbLTY2LjY1NTI2MzU3NjI1MzcsIDQ2LjAwNTE1OTA0ODg2NDNdLCBbLTY2LjY1NDkyMjIxNjQ0NTgsIDQ2LjAwNjIxOTc3NzU2OTZdLCBbLTY2LjY1Mzk1MjAzNTkzODksIDQ2LjAwNzQ5MjYyNTE2ODFdLCBbLTY2LjY1MjYwNDU2MzAxMjcsIDQ2LjAwODMwMzczODI2MDZdLCBbLTY2LjY1MDcxODEwMDkxNjEsIDQ2LjAwODgyMTU5NjU1MjVdLCBbLTY2LjY0ODY5Njg5MTUyNjgsIDQ2LjAwODg5NjQ2NzIyOTddLCBbLTY2LjY0OTYwNDE4OTk2MzgsIDQ2LjAxMDA4ODE0NTE5NzldLCBbLTY2LjY1MDA0NDM2NDQ1MywgNDYuMDExMjA0OTMwMDQwNV0sIFstNjYuNjQ5NTk1MjA2ODEwOSwgNDYuMDExODQ3NTM5MDMwN10sIFstNjYuNjQ4ODc2NTU0NTgzNiwgNDYuMDEyMzQ2NjQ3NjU3OF0sIFstNjYuNjQ4MTEyOTg2NTkyMSwgNDYuMDEyNjA4Njc3ODg0XSwgWy02Ni42NDc0NDgyMzMyODE5LCA0Ni4wMTI3MDg0OTg1OTZdLCBbLTY2LjY0NTYyNDY1MzI1NTEsIDQ2LjAxMjU4OTk2MTQ4MDRdLCBbLTY2LjY0MzA1NTQ3MTU0MjUsIDQ2LjAxMjE2NTcyMTMwMDldLCBbLTY2LjY0MDE4OTg0NTc4NjIsIDQ2LjAxMTM5MjA5ODQ3ODJdLCBbLTY2LjY0MDk5ODMyOTU0MTksIDQ2LjAxMjYzMzYzMzA3ODldLCBbLTY2LjY0MTIzMTg5MTUxNTgsIDQ2LjAxMzE5NTEyMTk4NjldLCBbLTY2LjY0MTE5NTk1ODkwNDQsIDQ2LjAxMzQ4ODM0MTcwNjRdLCBbLTY2LjY0MDkzNTQ0NzQ3MiwgNDYuMDE0MTk5NTQ5MDM1Nl0sIFstNjYuNjQwNTQ5MTcxODk5OCwgNDYuMDE0NzIzNTkwNjg4OF0sIFstNjYuNjM5NDA4MzExNDg5LCA0Ni4wMTU1ODQ1MDU0ODE0XSwgWy02Ni42MzgxNzc2MTk1NDk4LCA0Ni4wMTU5NTI1NzM2NTc5XSwgWy02Ni42MzUzODM4NTkwMTYyLCA0Ni4wMTYzMDE5MjQyMzcxXSwgWy02Ni42MzM3NzU4NzQ2NTc2LCA0Ni4wMTYzMzMxMTYxNDU4XSwgWy02Ni42MzAzNjIyNzY1Nzc5LCA0Ni4wMTYxNDU5NjQ0Mjk4XSwgWy02Ni42MzA2NzY2ODY5Mjc0LCA0Ni4wMTQzOTI5NDU5MzgxXSwgWy02Ni42MzA5NjQxNDc4MTgzLCA0Ni4wMDc0MjM5OTE5NzZdLCBbLTY2LjYzMzYwNTE5NDc1MzYsIDQ2LjAwODAyOTIwOTAwN10sIFstNjYuNjM1NzE2MjM1NjcxMywgNDYuMDA4NjkwNTcyNjIzNV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogMiwgIk5laWdoYm91cmgiOiAiQnJvb2tzaWRlIiwgIk9CSkVDVElEIjogMiwgIlNoYXBlX0FyZWEiOiAxMDQ0MzU4My42NTk4LCAiU2hhcGVfTGVuZyI6IDIyMDEwLjYzMTA2NjIsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZmZmZiMiIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNzEwNTU0ODgxOTkxMywgNDUuOTc1Nzc1MDIxODMxMV0sIFstNjYuNzA1NTE1MzMzMjQ3NCwgNDUuOTc2MDEyMjUzNTcxMl0sIFstNjYuNzAxMzQ3MTUwMzI5MSwgNDUuOTc2ODMwMDcwOTg5N10sIFstNjYuNjk5ODgyODk2NDE1OSwgNDUuOTc2OTA0OTg0OTU4NV0sIFstNjYuNjk4OTkzNTY0Mjg0NywgNDUuOTc2NzE3Njk5ODQ2NF0sIFstNjYuNjk4NDQ1NTkxOTYxNCwgNDUuOTc5MTk2MDU0ODkxXSwgWy02Ni42OTgxNzYwOTczNzYxLCA0NS45ODI4MTY2MjYwNzY3XSwgWy02Ni42OTg2NzkxNTM5MzUyLCA0NS45ODY0MTgyMzUyNDU0XSwgWy02Ni43MDAyNTEyMDU2ODI0LCA0NS45ODkyNDU2Nzc1NTgxXSwgWy02Ni43MDIxMTA3MTgzMjA2LCA0NS45OTE5ODU1OTk3NDg5XSwgWy02Ni43MTkyNDE1OTA3ODg3LCA0NS45OTMyOTYyMjA3MTg0XSwgWy02Ni43MzMxODM0NDM5OTgzLCA0NS45NzY2NTUyNzEzMzQ5XSwgWy02Ni43MzI3NzkyMDIxMjA0LCA0NS45NzY1MjQxNzEyMzE4XSwgWy02Ni43MzExODkxODQwNjc1LCA0NS45NzYzNDkzNzA2MTE1XSwgWy02Ni43MzA2NTkxNzgwNDk5LCA0NS45NzY0NTU0OTk2MjU0XSwgWy02Ni43MjgxMTY5NDU3OTU4LCA0NS45NzY0NTU0OTk2MjU0XSwgWy02Ni43MjYzMjAzMTUyMjc2LCA0NS45NzYyNjE5NzAwOTQ0XSwgWy02Ni43MjI2MDEyODk5NTEzLCA0NS45NzYwNzQ2ODI4MDc2XSwgWy02Ni43MjAzMDE2MDI4MjQsIDQ1Ljk3NjI2MTk3MDA5NDRdLCBbLTY2LjcxNjgwNzE1NjM2ODgsIDQ1Ljk3NjMxMTkxMzI2MzldLCBbLTY2LjcxMDU1NDg4MTk5MTMsIDQ1Ljk3NTc3NTAyMTgzMTFdXSwgW1stNjYuNzIwMTEyOTU2NjE0MywgNDUuOTc3NzYwMjQ1NTg1OF0sIFstNjYuNzIxNDA2NTMwNjIzNCwgNDUuOTc3ODIyNjcyODUxNV0sIFstNjYuNzI0NDUxODE5NDM2NiwgNDUuOTc3OTc4NzQwNzA3OF0sIFstNjYuNzIwNTcxMDk3NDA5MiwgNDUuOTgyNzcyOTMwOTM5M10sIFstNjYuNzIwMDUwMDc0NTQ0NCwgNDUuOTgzMDc4Nzk2MTc2NF0sIFstNjYuNzE5NTM4MDM0ODMyNSwgNDUuOTgzMjIyMzY0OTkwNl0sIFstNjYuNzE4NDYwMDU2NDkxNSwgNDUuOTgzMTg0OTEyMjkyM10sIFstNjYuNzE3ODY3MTY4NDA0LCA0NS45ODI5NDc3MTEyODE3XSwgWy02Ni43MTczNjQxMTE4NDQ5LCA0NS45ODI0OTIwMzI4MDQ2XSwgWy02Ni43MTcxOTM0MzE5NDA5LCA0NS45ODIwMzAxMDgzMjg1XSwgWy02Ni43MTczMTAyMTI5Mjc5LCA0NS45ODE0NjgzMDMwOTYxXSwgWy02Ni43MjAxMTI5NTY2MTQzLCA0NS45Nzc3NjAyNDU1ODU4XV0sIFtbLTY2LjcwNDU3MjEwMjE5OSwgNDUuOTc4MzQwODE2NDQwNl0sIFstNjYuNzA1Mzk4NTUyMjYwNCwgNDUuOTc5OTUxNDAwNDkyOV0sIFstNjYuNzA1NjE0MTQ3OTI4NiwgNDUuOTgxMzYyMTgzNjg5OF0sIFstNjYuNzA1MjcyNzg4MTIwNywgNDUuOTgyMzIzNDkzMjM5Nl0sIFstNjYuNzA0Njg4ODgzMTg2LCA0NS45ODI2MTY4NzY1OTZdLCBbLTY2LjcwMzk3MDIzMDk1ODcsIDQ1Ljk4MjY4NTU0MDU2MTJdLCBbLTY2LjcwMzM5NTMwOTE3NjgsIDQ1Ljk4MjU1NDQ1NDczNTVdLCBbLTY2LjcwMTYyNTYyODA2NzEsIDQ1Ljk4MDU0NDQzMzIwNzNdLCBbLTY2LjcwMTI0ODMzNTY0NzgsIDQ1Ljk3OTY3NjczMDU1NzJdLCBbLTY2LjcwMTA5NTYyMjA0OTUsIDQ1Ljk3ODU5Njc2NTA5OTJdLCBbLTY2LjcwNDU3MjEwMjE5OSwgNDUuOTc4MzQwODE2NDQwNl1dLCBbWy02Ni43MTAxOTU1NTU4Nzc2LCA0NS45NzYyMjQ1MTI2ODc3XSwgWy02Ni43MTEwNDg5NTUzOTc2LCA0NS45NzYzMTE5MTMyNjM5XSwgWy02Ni43MTE2Nzc3NzYwOTY0LCA0NS45NzY0OTkxOTk3NDg0XSwgWy02Ni43MTIxMzU5MTY4OTEzLCA0NS45NzcwNTQ4MTI1OTIxXSwgWy02Ni43MTIxNDQ5MDAwNDQyLCA0NS45Nzc5MTAwNzA5MDUyXSwgWy02Ni43MTY3NzEyMjM3NTc0LCA0NS45Nzc2NDE2MzM1ODddLCBbLTY2LjcxNTg0NTk1OTAxNDcsIDQ1Ljk3ODk1ODgzNjc5MDddLCBbLTY2LjcxNDcwNTA5ODYwMzksIDQ1Ljk4MDE5NDg1Njc5NjldLCBbLTY2LjcxMzA4ODEzMTA5MjUsIDQ1Ljk4MTU0MzIxMDc4OThdLCBbLTY2LjcxMTczMTY3NTAxMzUsIDQ1Ljk4MjM2NzE4ODczMTZdLCBbLTY2LjcxMDcwNzU5NTU4OTYsIDQ1Ljk4MjYzNTYwMzE0MDRdLCBbLTY2LjcwOTgwOTI4MDMwNTUsIDQ1Ljk4MjY4NTU0MDU2MTJdLCBbLTY2LjcwODQ4ODc1NjgzNzgsIDQ1Ljk4MjA0MjU5MjgyNDVdLCBbLTY2LjcwNzUxODU3NjMzMSwgNDUuOTgxMTQ5OTQ0MjY3MV0sIFstNjYuNzA3MDk2MzY4MTQ3NCwgNDUuOTgwNDA3MDk5ODgwN10sIFstNjYuNzA3MTMyMzAwNzU4OCwgNDUuOTgwMjAxMDk5MjUyMV0sIFstNjYuNzA3NDY0Njc3NDEzOSwgNDUuOTc5MjE0NzgyNTkyNV0sIFstNjYuNzA4MTY1MzYzMzM1NSwgNDUuOTc4MTAzNTk0Njc2Ml0sIFstNjYuNzA3MzU2ODc5NTc5OCwgNDUuOTc4MTU5Nzc4ODcwMl0sIFstNjYuNzA3Mzc0ODQ1ODg1NSwgNDUuOTc4MDM0OTI1MDI4NV0sIFstNjYuNzA3ODY4OTE5MjkxOCwgNDUuOTc3MTE3MjQwNjUzMV0sIFstNjYuNzA4NzEzMzM1NjU4OCwgNDUuOTc2NTA1NDQyNjIwM10sIFstNjYuNzA5MzUxMTM5NTEwNiwgNDUuOTc2MzExOTEzMjYzOV0sIFstNjYuNzEwMTk1NTU1ODc3NiwgNDUuOTc2MjI0NTEyNjg3N11dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogMywgIk5laWdoYm91cmgiOiAiRG91Z2xhcyIsICJPQkpFQ1RJRCI6IDMsICJTaGFwZV9BcmVhIjogMzIzMTQ1Ni40MzM4NywgIlNoYXBlX0xlbmciOiAxMzYwNC44Mjk1OTAxLCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjY4MTM3NzYwMTU2MzEsIDQ2LjAxNzAwMDYxODc3NDddLCBbLTY2LjY4MDI4MTY1NjkxNjUsIDQ2LjAxNjE1MjIwMjgzMDZdLCBbLTY2LjY3OTA4Njg5NzU4ODYsIDQ2LjAxNDk5ODA4NjcxNTddLCBbLTY2LjY3ODEwNzczMzkyODksIDQ2LjAxMzc1MDM2NjUyMzRdLCBbLTY2LjY3NzM1MzE0OTA5MDIsIDQ2LjAxMjQyNzc1MjM4NDNdLCBbLTY2LjY3NzExOTU4NzExNjQsIDQ2LjAxMTg3ODczMzQ1MThdLCBbLTY2LjY3NjU2MjYzMTY0MDIsIDQ2LjAwOTA1MjQ0NzQ4MTddLCBbLTY2LjY3NTY0NjM1MDA1MDQsIDQ2LjAwNTU0NTkwNTIxODldLCBbLTY2LjY3NDczOTA1MTYxMzQsIDQ2LjAwMjc2Mjk3NTA0NjddLCBbLTY2LjY3MzM5MTU3ODY4NzMsIDQ1Ljk5OTMxODQzNzEyMTRdLCBbLTY2LjY3MTI5ODUwNDA3NTMsIDQ1Ljk5Njk0NzA3MjYxODldLCBbLTY2LjY2ODgxMDE3MDczODIsIDQ1Ljk5NDc2OTA3MjAwN10sIFstNjYuNjY2NDAyNjg1Nzc2OCwgNDUuOTkzMDc3Nzg2MDQ1NV0sIFstNjYuNjY1NjkzMDE2NzAyNCwgNDUuOTkzMjgzNzM4NzYwNF0sIFstNjYuNjYzMzM5NDMwNjU4LCA0NS45OTQyMDczOTYwNTQ4XSwgWy02Ni42NjEyNDYzNTYwNDYsIDQ1Ljk5NTM5MzE0OTcxMjRdLCBbLTY2LjY2MDQ1NTgzODU5NTksIDQ1Ljk5NzA5Njg0NjAxNTFdLCBbLTY2LjY1OTg4OTg5OTk2NjksIDQ1Ljk5ODg1MDQxMjcwMzNdLCBbLTY2LjY1OTU1NzUyMzMxMTgsIDQ2LjAwMDYyODg4NDQzMTFdLCBbLTY2LjY1OTQ2NzY5MTc4MzQsIDQ2LjAwMjQyNjAxODg0MzJdLCBbLTY2LjY2MDU3MjYxOTU4MjksIDQ2LjAwNjA1MTMxMDI1MTVdLCBbLTY2LjY2MzU1NTAyNjMyNjIsIDQ2LjAxMzgwNjUxNDUzNjldLCBbLTY2LjY2NjQ2NTU2Nzg0NjcsIDQ2LjAyMDQxOTEwNDA2MzVdLCBbLTY2LjY4MTUyMTMzMjAwODUsIDQ2LjAxOTc1MTY0MjcwMDldLCBbLTY2LjY4MTM3NzYwMTU2MzEsIDQ2LjAxNzAwMDYxODc3NDddXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDQsICJOZWlnaGJvdXJoIjogIk1jTGVvZCBIaWxsIiwgIk9CSkVDVElEIjogNCwgIlNoYXBlX0FyZWEiOiAzMTU4NjUyLjMxNDU4LCAiU2hhcGVfTGVuZyI6IDc3OTkuODkxMzQ1NiwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmVkOTc2IiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni42MDc2OTc3ODE5NTk2LCA0NS45NzU0NTAzODcyNzY3XSwgWy02Ni42MDUxMTA2MzM5NDEzLCA0NS45NzUwNDQ1OTE0MDc1XSwgWy02Ni42MDI5OTA2MDk4NzA4LCA0NS45NzQ0NzAyMjkwOTQ0XSwgWy02Ni42MDE5NDg1NjQxNDEyLCA0NS45NzQwNjQ0MjYwNDI4XSwgWy02Ni42MDE4Njc3MTU3NjU3LCA0NS45NzIxNjY0NzY5MTEyXSwgWy02Ni42MDE1NDQzMjIyNjM0LCA0NS45NzAyODA5NDk4ODQyXSwgWy02Ni42MDA4NTI2MTk0OTQ2LCA0NS45NjgwNTgxOTMyMDczXSwgWy02Ni42MDAzNDk1NjI5MzU1LCA0NS45NjcyMDkwMjY2NjA1XSwgWy02Ni41OTgwNjc4NDIxMTM4LCA0NS45NjQzODY3MDMxMzhdLCBbLTY2LjU5NTQ4MDY5NDA5NTYsIDQ1Ljk2MTY5NTM3MTMzOTRdLCBbLTY2LjU5MjU5NzEwMjAzMzYsIDQ1Ljk1OTE2MDAyOTY4NzVdLCBbLTY2LjU4OTQzNTAzMjIzMzUsIDQ1Ljk1Njc4Njk0NDcwNzhdLCBbLTY2LjU3NDQ5NjA0OTA1ODUsIDQ1Ljk3MzkxNDU5MDMxODNdLCBbLTY2LjU1MDM0OTMzNDIyMTQsIDQ2LjAwMjA1MTYyMDY1NDZdLCBbLTY2LjU4MjEwNDc3OTUxNSwgNDYuMDA5MDA4NzczMDU1NF0sIFstNjYuNTkyMjAxODQzMzA4NSwgNDYuMDEzMjU3NTA5MjkxNV0sIFstNjYuNTk0ODk2Nzg5MTYwOSwgNDYuMDEzODY4OTAxMTUxOF0sIFstNjYuNjE0MTM4NzAyNTQ2NywgNDUuOTkwOTkzMjUxNzk3Ml0sIFstNjYuNjExOTM3ODMwMTAwNiwgNDUuOTkwMjk0MjI4NzIyOV0sIFstNjYuNjA5NTc1MjYwOTAzNCwgNDUuOTg5MjE0NDcwMzczOF0sIFstNjYuNjA4OTI4NDczODk4OCwgNDUuOTg5NjEzOTIxMDA0XSwgWy02Ni42MDgzMDg2MzYzNTI4LCA0NS45ODk4MzIzNjkzNDgxXSwgWy02Ni42MDY4NzEzMzE4OTgyLCA0NS45ODk5Njk2NzkyOTQ1XSwgWy02Ni42MDUyMDk0NDg2MjI2LCA0NS45ODk3MzI1MDczNTQ5XSwgWy02Ni42MDM3OTAxMTA0NzM3LCA0NS45ODkxMDIxMjQzNjQ2XSwgWy02Ni42MDI3NzUwMTQyMDI2LCA0NS45ODgxNTk2NTcxOTY3XSwgWy02Ni42MDE3Njg5MDEwODQ0LCA0NS45ODYxMzczNTU2MDY0XSwgWy02Ni42MDEyNDc4NzgyMTk2LCA0NS45ODQzMjA5NjYyMDA2XSwgWy02Ni42MDEwOTUxNjQ2MjEzLCA0NS45ODI0NjcwNjQwMTI1XSwgWy02Ni41OTk5OTkyMTk5NzQ3LCA0NS45ODc4Mjg4NTM2NTc1XSwgWy02Ni41OTk4ODI0Mzg5ODc4LCA0NS45ODkxMTQ2MDcyNjU4XSwgWy02Ni41OTkzOTczNDg3MzQzLCA0NS45OTAzNTY2NDE4NTYzXSwgWy02Ni41OTg1Nzk4ODE4MjU4LCA0NS45OTE1MTEyNzIxMzAxXSwgWy02Ni41OTc2NTQ2MTcwODMxLCA0NS45OTIzNzI1NDgyMTY1XSwgWy02Ni41OTYzMDcxNDQxNTcsIDQ1Ljk5MzI1MjUzMzg1MjhdLCBbLTY2LjU5NTAxMzU3MDE0NzgsIDQ1Ljk5MzgzMjk0MjI1MjldLCBbLTY2LjU5MjM4MTUwNjM2NTQsIDQ1Ljk5NDQzODMwNzk2OTddLCBbLTY2LjU5MDY1Njc0MTAxOTksIDQ1Ljk5MzgzMjk0MjI1MjldLCBbLTY2LjU4OTA5MzY3MjQyNTUsIDQ1Ljk5MzA0MDM0MDAxNTFdLCBbLTY2LjU4Nzg2Mjk4MDQ4NjMsIDQ1Ljk5MTg3MzI1OTM2NDRdLCBbLTY2LjU4NjY1MDI1NDg1MjcsIDQ1Ljk5MDM0NDE1OTIzNTJdLCBbLTY2LjU4NTg3NzcwMzcwODMsIDQ1Ljk4ODk5NjAxOTU5MTFdLCBbLTY2LjU4NTkzMTYwMjYyNTQsIDQ1Ljk4ODI2NTc2MzU3MzVdLCBbLTY2LjU4NjMzNTg0NDUwMzIsIDQ1Ljk4NzU5MTY3MjU0NDddLCBbLTY2LjU4NzAzNjUzMDQyNDgsIDQ1Ljk4NzA0ODY0ODgwMTVdLCBbLTY2LjU4Nzk2MTc5NTE2NzUsIDQ1Ljk4NjY5OTExMzQ1OTJdLCBbLTY2LjU4OTQ4ODkzMTE1MDUsIDQ1Ljk4NjQ4Njg5NDQ5NTldLCBbLTY2LjU4OTc1ODQyNTczNTcsIDQ1Ljk4NjEzNzM1NTYwNjRdLCBbLTY2LjU5MDE4OTYxNzA3MjEsIDQ1Ljk4NTM4ODMzNjI2ODNdLCBbLTY2LjU5MDUwNDAyNzQyMTUsIDQ1Ljk4NDQxNDU5NTk3NzNdLCBbLTY2LjU5MDc4MjUwNTE1OTYsIDQ1Ljk4MDc1NjY3NDk1MTFdLCBbLTY2LjU5MTQwMjM0MjcwNTcsIDQ1Ljk4MDA4ODczNDk0OThdLCBbLTY2LjU5MjAyMjE4MDI1MTcsIDQ1Ljk3OTgyNjU1MDY5MTFdLCBbLTY2LjU5Mjg3NTU3OTc3MTYsIDQ1Ljk3OTcyNjY3MDY0NjldLCBbLTY2LjU5NTc2ODE1NDk4NjUsIDQ1Ljk4MDI0NDc5NjQxOTJdLCBbLTY2LjU5NzYyNzY2NzYyNDYsIDQ1Ljk4MDc4MTY0NDUxNDZdLCBbLTY2LjU5OTI4MDU2Nzc0NzQsIDQ1Ljk4MTQxMjEyMjI1OTNdLCBbLTY2LjYwMDM0OTU2MjkzNTUsIDQ1Ljk4MTk0MjcxNjc3NzldLCBbLTY2LjYwMTA5NTE2NDYyMTMsIDQ1Ljk4MjQ2NzA2NDAxMjVdLCBbLTY2LjYwMTM5MTYwODY2NTEsIDQ1Ljk3OTMzMzM5MTIyMTRdLCBbLTY2LjYwMzMwNTAyMDIyMDMsIDQ1Ljk3OTQ0NTc1NzA1NjZdLCBbLTY2LjYwNDY3OTQ0MjYwNDksIDQ1Ljk3OTc3MDM2ODE4ODRdLCBbLTY2LjYwNDg3NzA3MTk2NzUsIDQ1Ljk3ODU4NDI3OTgyNjJdLCBbLTY2LjYwNTQyNTA0NDI5MDgsIDQ1Ljk3NzQ2MDU5MzczMDZdLCBbLTY2LjYwNjMwNTM5MzI2OTIsIDQ1Ljk3NjQ0MzAxMzg2OTZdLCBbLTY2LjYwNzY5Nzc4MTk1OTYsIDQ1Ljk3NTQ1MDM4NzI3NjddXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDUsICJOZWlnaGJvdXJoIjogIk1hcnlzdmlsbGUiLCAiT0JKRUNUSUQiOiA1LCAiU2hhcGVfQXJlYSI6IDE0MTE5NDQwLjQyMDEsICJTaGFwZV9MZW5nIjogMjI1NTAuNTEwODMyMSwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmViMjRjIiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni42MzQ5MDc3NTE5MTU2LCA0NS45NjkwMTk3MzM3MjgxXSwgWy02Ni42MzQ1MDM1MTAwMzc3LCA0NS45NjkwNjk2ODM0MjldLCBbLTY2LjYzMzQ3OTQzMDYxMzgsIDQ1Ljk2ODQ4Mjc3MTU5OTFdLCBbLTY2LjYyOTU2Mjc3NTk3NTEsIDQ1Ljk3MjcyMjEzMzIyNjJdLCBbLTY2LjYyOTMxMTI0NzY5NTUsIDQ1Ljk3NDIyMDUwNDQ5MTVdLCBbLTY2LjYyMTc5MjM0ODc2NzQsIDQ1Ljk4MTg5Mjc3ODY4N10sIFstNjYuNTk0ODk2Nzg5MTYwOSwgNDYuMDEzODY4OTAxMTUxOF0sIFstNjYuNTk5NjAzOTYxMjQ5NywgNDYuMDE0OTkxODQ4MTg0OF0sIFstNjYuNjMwMzgwMjQyODgzNiwgNDUuOTc3MTQyMjExODU3OF0sIFstNjYuNjM0MDYzMzM1NTQ4NSwgNDUuOTcyNzk3MDUyNzUyMl0sIFstNjYuNjMzODkyNjU1NjQ0NSwgNDUuOTcxOTQxNzE1NDY5OF0sIFstNjYuNjMyMzM4NTcwMjAzLCA0NS45NzE1NDIxMzczMjJdLCBbLTY2LjYzMzM4OTU5OTA4NTQsIDQ1Ljk3MDI0MzQ4ODQzMl0sIFstNjYuNjM0OTA3NzUxOTE1NiwgNDUuOTY5MDE5NzMzNzI4MV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogNiwgIk5laWdoYm91cmgiOiAiU2FpbnQgTWFyeSdzIEZpcnN0IE5hdGlvbiIsICJPQkpFQ1RJRCI6IDYsICJTaGFwZV9BcmVhIjogMTg1MTQzNS4xNzI0OCwgIlNoYXBlX0xlbmciOiAxMjM2Ny42MTg2MjE0LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjYwMDExNjAwMDk2MTYsIDQ1Ljk4NzQxNjkwNjg2MzhdLCBbLTY2LjU5NzEwNjY0NDc1OTgsIDQ1Ljk4NjgwNTIyMjYzNTddLCBbLTY2LjU5MzY5MzA0NjY4MDIsIDQ1Ljk4NjQzNjk2MDUwNF0sIFstNjYuNTkxMjc2NTc4NTY1OSwgNDUuOTg2MzgwNzg0NzA5Ml0sIFstNjYuNTg5MjY0MzUyMzI5NSwgNDUuOTg2NTExODYxNDc1XSwgWy02Ni41ODc3OTExMTUyNjM1LCA0NS45ODY3NDI4MDU0OTc2XSwgWy02Ni41ODY2NTAyNTQ4NTI3LCA0NS45ODcyOTgzMTU1NTE5XSwgWy02Ni41ODU5NzY1MTgzODk2LCA0NS45ODgxNDcxNzQwODAyXSwgWy02Ni41ODU4Nzc3MDM3MDgzLCA0NS45ODg5OTYwMTk1OTExXSwgWy02Ni41ODcyMTYxOTM0ODE3LCA0NS45OTExMjQzMTc2NDA4XSwgWy02Ni41ODkwOTM2NzI0MjU1LCA0NS45OTMwNDAzNDAwMTUxXSwgWy02Ni41OTA2NTY3NDEwMTk5LCA0NS45OTM4MzI5NDIyNTI5XSwgWy02Ni41OTIzODE1MDYzNjU0LCA0NS45OTQ0MzgzMDc5Njk3XSwgWy02Ni41OTUwMTM1NzAxNDc4LCA0NS45OTM4MzI5NDIyNTI5XSwgWy02Ni41OTU1NDM1NzYxNjU1LCA0NS45OTM2MjA3NTA2NDA1XSwgWy02Ni41OTY3ODMyNTEyNTc1LCA0NS45OTI5ODQxNzA5MjE4XSwgWy02Ni41OTgwNDk4NzU4MDgyLCA0NS45OTIwNDE3Njk4NTU2XSwgWy02Ni41OTg4ODUzMDkwMjI0LCA0NS45OTExNDMwNDEzMDc0XSwgWy02Ni41OTk1OTQ5NzgwOTY4LCA0NS45ODk5NTA5NTUyMzFdLCBbLTY2LjU5OTkyNzM1NDc1MiwgNDUuOTg4OTAyMzk3NTYzMV0sIFstNjYuNjAwMTE2MDAwOTYxNiwgNDUuOTg3NDE2OTA2ODYzOF1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogNywgIk5laWdoYm91cmgiOiAiU2FuZHl2aWxsZSIsICJPQkpFQ1RJRCI6IDcsICJTaGFwZV9BcmVhIjogNzI4ODU5LjQ4MTAwMSwgIlNoYXBlX0xlbmciOiAzMTc1LjQyMDA2NDU0LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjU4OTQ4ODkzMTE1MDUsIDQ1Ljk4NjQ4Njg5NDQ5NTldLCBbLTY2LjU5MTU3MzAyMjYwOTcsIDQ1Ljk4NjM3NDU0Mjk1MDddLCBbLTY2LjU5NDA2MTM1NTk0NjcsIDQ1Ljk4NjQ2ODE2OTI1NDJdLCBbLTY2LjU5NzUzNzgzNjA5NjIsIDQ1Ljk4Njg3Mzg4MTQwNjJdLCBbLTY2LjYwMDExNjAwMDk2MTYsIDQ1Ljk4NzQxNjkwNjg2MzhdLCBbLTY2LjYwMTA5NTE2NDYyMTMsIDQ1Ljk4MjQ2NzA2NDAxMjVdLCBbLTY2LjU5OTUwNTE0NjU2ODQsIDQ1Ljk4MTUwNTc1Njk1NTZdLCBbLTY2LjU5NjUyMjczOTgyNTEsIDQ1Ljk4MDQ0NDU1NDQ1ODFdLCBbLTY2LjU5MzE2MzA0MDY2MjUsIDQ1Ljk3OTc1MTY0MDY3NDhdLCBbLTY2LjU5MjQ0NDM4ODQzNTMsIDQ1Ljk3OTc0NTM5ODE2ODldLCBbLTY2LjU5MTg4NzQzMjk1OTEsIDQ1Ljk3OTg2NDAwNTY2MTJdLCBbLTY2LjU5MTIwNDcxMzM0MzIsIDQ1Ljk4MDIyNjA2OTA2NjFdLCBbLTY2LjU5MDc4MjUwNTE1OTYsIDQ1Ljk4MDc1NjY3NDk1MTFdLCBbLTY2LjU5MDQ2ODA5NDgxMDIsIDQ1Ljk4NDYxNDMzODk3MThdLCBbLTY2LjU5MDA5OTc4NTU0MzcsIDQ1Ljk4NTU4MTgzMzkwMTVdLCBbLTY2LjU4OTQ4ODkzMTE1MDUsIDQ1Ljk4NjQ4Njg5NDQ5NTldXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDgsICJOZWlnaGJvdXJoIjogIktub2IgSGlsbCIsICJPQkpFQ1RJRCI6IDgsICJTaGFwZV9BcmVhIjogNTQ1MDIzLjE0NTc1MywgIlNoYXBlX0xlbmciOiAyOTc1LjkzNjQ4NDUzLCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjYwMTk0ODU2NDE0MTIsIDQ1Ljk3NDA2NDQyNjA0MjhdLCBbLTY2LjYwMzIwNjIwNTUzOSwgNDUuOTc0NTMyNjYwMDY5Ml0sIFstNjYuNjA2MTE2NzQ3MDU5NSwgNDUuOTc1MjUwNjExMjIwNF0sIFstNjYuNjA3Nzg3NjEzNDg4LCA0NS45NzU0NjI4NzMyNTYzXSwgWy02Ni42MTEwMDM1ODIyMDUyLCA0NS45NzU1ODc3MzI4OTc0XSwgWy02Ni42MTE5NzM3NjI3MTIsIDQ1Ljk3NTM5NDIwMDMzMzhdLCBbLTY2LjYxMjkwODAxMDYwNzUsIDQ1Ljk3NDg4MjI3MjIyNzNdLCBbLTY2LjYxMzQxMTA2NzE2NjYsIDQ1Ljk3NDI3MDQ0OTUwMjJdLCBbLTY2LjYxMzU3Mjc2MzkxNzcsIDQ1Ljk3MzQ1MjU5NDI4MjNdLCBbLTY2LjYxMzMyMTIzNTYzODIsIDQ1Ljk3Mjc3MjA3OTU4ODFdLCBbLTY2LjYxMjYyOTUzMjg2OTQsIDQ1Ljk3MjEwNDA0MzI2OV0sIFstNjYuNjA2MTk3NTk1NDM1MSwgNDUuOTY4NzQ1MDA5NTY4M10sIFstNjYuNjA0NjE2NTYwNTM1MSwgNDUuOTY1NDEwNzQ4NjQ4XSwgWy02Ni42MDM4Nzk5NDIwMDIxLCA0NS45NjQ4ODYyMzk4OTc5XSwgWy02Ni42MDI1OTUzNTExNDU4LCA0NS45NjQyNDMwODU0ODU5XSwgWy02Ni42MDA4ODg1NTIxMDYsIDQ1Ljk2Mzc2ODUyMDE2MTVdLCBbLTY2LjU5OTMxNjUwMDM1ODgsIDQ1Ljk2MzYxMjQxMjI1ODNdLCBbLTY2LjU5NzQ4MzkzNzE3OTIsIDQ1Ljk2MzczNzI5ODYxNl0sIFstNjYuNjAwNjk5OTA1ODk2MywgNDUuOTY3Njg5ODA2Mzc3Nl0sIFstNjYuNjAxMzU1Njc2MDUzNywgNDUuOTY5NTMxNzE2MDI2NV0sIFstNjYuNjAxNzA2MDE5MDE0NSwgNDUuOTcxMDMwMTczNjA3XSwgWy02Ni42MDE5NDg1NjQxNDEyLCA0NS45NzQwNjQ0MjYwNDI4XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiA5LCAiTmVpZ2hib3VyaCI6ICJZb3VuZ3MgQ3Jvc3NpbmciLCAiT0JKRUNUSUQiOiA5LCAiU2hhcGVfQXJlYSI6IDc0ODQ5MC4wODMxMjUsICJTaGFwZV9MZW5nIjogNDA5Ni4yMzk3MjIzMiwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmVkOTc2IiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni42MjM3Nzc2MjU1NDUzLCA0NS45NTU0MzE3NDI2OTU1XSwgWy02Ni42MjMzNzMzODM2Njc1LCA0NS45NTQzOTUwMjIwMDgxXSwgWy02Ni42MjM1Nzk5OTYxODI4LCA0NS45NTMwNTg0OTgwNDY3XSwgWy02Ni42MjM4MjI1NDEzMDk1LCA0NS45NTI1NzEzNDU3ODM5XSwgWy02Ni42MjM5OTMyMjEyMTM1LCA0NS45NTA0MDQwOTA4NzAzXSwgWy02Ni42MjM5MTIzNzI4MzgsIDQ1Ljk0OTM2NzI3NjEzMDhdLCBbLTY2LjYyMjgzNDM5NDQ5NywgNDUuOTQzOTI2ODAzODI1NF0sIFstNjYuNjIyNTExMDAwOTk0NywgNDUuOTQzNTU4MjU2NTQxXSwgWy02Ni42MjI1NDY5MzM2MDYxLCA0NS45NDMwNzEwMjA3Nzc0XSwgWy02Ni42MjIxNzg2MjQzMzk2LCA0NS45NDI3MDI0Njc4MDM5XSwgWy02Ni42MjIxNTE2NzQ4ODExLCA0NS45NDIyMTUyMjQ1MTkyXSwgWy02Ni42MjE1NzY3NTMwOTkyLCA0NS45NDIwMzQwNjg4NzI2XSwgWy02Ni42MjA4ODUwNTAzMzA1LCA0NS45NDExMzQ1Mjg2MTldLCBbLTY2LjYxNjgzMzY0ODM5OTEsIDQ1LjkzNzE2MTM4NDU4NjZdLCBbLTY2LjYxNDA0ODg3MTAxODMsIDQ1LjkzNTE0MzQ2ODE1MjFdLCBbLTY2LjYxMDIyMjA0NzkwOCwgNDUuOTMyOTI1NTQ5NTk2NF0sIFstNjYuNjA4NDM0NDAwNDkyNiwgNDUuOTMyMzE5NTExMzUwMl0sIFstNjYuNjA2NzAwNjUxOTk0MiwgNDUuOTMxMzY5ODI5ODUxMV0sIFstNjYuNjA1ODc0MjAxOTMyOCwgNDUuOTMxMTA3NDE0OTkwNF0sIFstNjYuNjAzNjI4NDEzNzIyNSwgNDUuOTMwMTEzOTc2MDU2N10sIFstNjYuNjAwMTk2ODQ5MzM3MiwgNDUuOTI4OTA4MDc5NzMyXSwgWy02Ni41OTczODUxMjI0OTc5LCA0NS45MjcyNzcyNjYzMTc4XSwgWy02Ni41OTY5MTc5OTg1NTAyLCA0NS45MjY4OTYxMTE0NDI2XSwgWy02Ni41OTU5NTY4MDExOTYyLCA0NS45MjU3Mjc2MzY3MzRdLCBbLTY2LjU5MjY2ODk2NzI1NjMsIDQ1LjkyODQwODIxODY0NzNdLCBbLTY2LjYwNTExMDYzMzk0MTMsIDQ1LjkzODY3OTQ1OTA3NDhdLCBbLTY2LjU4OTQzNTAzMjIzMzUsIDQ1Ljk1Njc4Njk0NDcwNzhdLCBbLTY2LjU5Mjk4MzM3NzYwNTcsIDQ1Ljk1OTQ3MjI3MDE0NV0sIFstNjYuNTk1NzQxMjA1NTI4LCA0NS45NjE5NDUxNTI0MTYyXSwgWy02Ni41OTY5OTg4NDY5MjU3LCA0NS45NjE3MTQxMDQ5NTkyXSwgWy02Ni42MDI2NzYxOTk1MjE0LCA0NS45NjEwMzM0NDYwMzk3XSwgWy02Ni42MDQ0OTA3OTYzOTUzLCA0NS45NjEwODM0MDI5NDJdLCBbLTY2LjYwNjg5ODI4MTM1NjcsIDQ1Ljk2MTUyMDUyMzkxNTZdLCBbLTY2LjYwNzg1OTQ3ODcxMDcsIDQ1Ljk2MTU2NDIzNTgyMzNdLCBbLTY2LjYwODc5MzcyNjYwNjIsIDQ1Ljk2MTQwMTg3NzEzNTJdLCBbLTY2LjYwOTg5ODY1NDQwNTcsIDQ1Ljk2MDg1ODU5NjUyN10sIFstNjYuNjEwNTgxMzc0MDIxNiwgNDUuOTYwMjA5MTUwNjQ4N10sIFstNjYuNjEwOTk0NTk5MDUyMywgNDUuOTU5NDUzNTM1NzY3Ml0sIFstNjYuNjExMDg0NDMwNTgwNywgNDUuOTU4NTIzMDUzNjk4XSwgWy02Ni42MTA3NzAwMjAyMzEzLCA0NS45NTc2MzAwMjYwMTExXSwgWy02Ni42MTAzMDI4OTYyODM1LCA0NS45NTcwMjQyNTc3NzkyXSwgWy02Ni42MDkzNjg2NDgzODgxLCA0NS45NTYyOTM1ODAwNjk4XSwgWy02Ni42MDk0MjI1NDczMDUxLCA0NS45NTU5Mzc2MDUzODc4XSwgWy02Ni42MDk3ODE4NzM0MTg4LCA0NS45NTU2ODc3OTcyMjhdLCBbLTY2LjYxMDE5NTA5ODQ0OTUsIDQ1Ljk1NTYzMTU5MDIzNjhdLCBbLTY2LjYxMDUyNzQ3NTEwNDYsIDQ1Ljk1NTcxMjc3ODA5NDZdLCBbLTY2LjYxMTgwMzA4MjgwOCwgNDUuOTU2NjU1Nzk3NTc0NF0sIFstNjYuNjEzMDMzNzc0NzQ3MywgNDUuOTU3MTg2NjI5Mjk1MV0sIFstNjYuNjE0NDYyMDk2MDQ5LCA0NS45NTc1NTUwODU5NzAyXSwgWy02Ni42MTU3MTk3Mzc0NDY4LCA0NS45NTc2NDI1MTYwMDhdLCBbLTY2LjYxNjk1OTQxMjUzODksIDQ1Ljk1NzQ5ODg4MDg3M10sIFstNjYuNjE4NjMwMjc4OTY3MywgNDUuOTU3MDQ5MjM4MDQzNF0sIFstNjYuNjIzNzc3NjI1NTQ1MywgNDUuOTU1NDMxNzQyNjk1NV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogMTAsICJOZWlnaGJvdXJoIjogIkJhcmtlcnMgUG9pbnQiLCAiT0JKRUNUSUQiOiAxMCwgIlNoYXBlX0FyZWEiOiA1Nzc5MDIxLjk2ODQsICJTaGFwZV9MZW5nIjogMTIzMTkuMjM5MDQ5NCwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmViMjRjIiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni42Mjg2NzM0NDM4NDM4LCA0NS45NjQ4MzAwNDIyMzczXSwgWy02Ni42Mjc3MzAyMTI3OTU1LCA0NS45NjM1Njg3MDE5NjY2XSwgWy02Ni42Mjc2MjI0MTQ5NjE0LCA0NS45NjMyMDY1Mjk2NTE0XSwgWy02Ni42MjcxMTAzNzUyNDk0LCA0NS45NjI2OTQ0ODg4OV0sIFstNjYuNjI2NzQyMDY1OTgyOSwgNDUuOTYxNzE0MTA0OTU5Ml0sIFstNjYuNjI2NzE1MTE2NTI0NCwgNDUuOTYwNzUyNDM3NjI1XSwgWy02Ni42MjU1MDIzOTA4OTA4LCA0NS45NTk2MDk2NTUzODg5XSwgWy02Ni42MjU0MTI1NTkzNjI0LCA0NS45NTg3NzkwOTM5NDY1XSwgWy02Ni42MjUxMDcxMzIxNjU4LCA0NS45NTc5OTIyMzQ3Nzk4XSwgWy02Ni42MjUzMTM3NDQ2ODEyLCA0NS45NTc3NTQ5MjU4NTM5XSwgWy02Ni42MjUyODY3OTUyMjI3LCA0NS45NTc1NzM4MjA5ODk5XSwgWy02Ni42MjQ4ODI1NTMzNDQ4LCA0NS45NTc1MDUxMjU4ODY2XSwgWy02Ni42MjQ3MDI4OTAyODgsIDQ1Ljk1NzI5Mjc5NTAyOV0sIFstNjYuNjI1MDA4MzE3NDg0NiwgNDUuOTU2NzMwNzM4ODMxNV0sIFstNjYuNjI1MDA4MzE3NDg0NiwgNDUuOTU2MzgxMDEyMDk4XSwgWy02Ni42MjQyOTg2NDg0MTAxLCA0NS45NTYxODc0MTI0MjE1XSwgWy02Ni42MjM3Nzc2MjU1NDUzLCA0NS45NTU0MzE3NDI2OTU1XSwgWy02Ni42MTg2MzAyNzg5NjczLCA0NS45NTcwNDkyMzgwNDM0XSwgWy02Ni42MTY5NTk0MTI1Mzg5LCA0NS45NTc0OTg4ODA4NzNdLCBbLTY2LjYxNTcxOTczNzQ0NjgsIDQ1Ljk1NzY0MjUxNjAwOF0sIFstNjYuNjE0MjY0NDY2Njg2NSwgNDUuOTU3NTE3NjE1OTExN10sIFstNjYuNjEyODA5MTk1OTI2MiwgNDUuOTU3MTExNjg4NjU0Nl0sIFstNjYuNjExNjIzNDE5NzUxMiwgNDUuOTU2NTQ5NjMwNjIwMV0sIFstNjYuNjEwNTk5MzQwMzI3MywgNDUuOTU1NzQ0MDA0MTYyMV0sIFstNjYuNjEwMjg0OTI5OTc3OSwgNDUuOTU1NjQ0MDgwNjg0Ml0sIFstNjYuNjA5ODYyNzIxNzk0MywgNDUuOTU1NjYyODE2MzUwMV0sIFstNjYuNjA5NDIyNTQ3MzA1MSwgNDUuOTU1OTM3NjA1Mzg3OF0sIFstNjYuNjA5MzY4NjQ4Mzg4MSwgNDUuOTU2MjkzNTgwMDY5OF0sIFstNjYuNjEwNjQ0MjU2MDkxNSwgNDUuOTU3NDE3Njk1NjMyXSwgWy02Ni42MTEwMzA1MzE2NjM3LCA0NS45NTgyNTQ1MjI0MTAzXSwgWy02Ni42MTEwODQ0MzA1ODA3LCA0NS45NTkwNTM4Njc1MzExXSwgWy02Ni42MTA4ODY4MDEyMTgyLCA0NS45NTk3MDk1NzE3MTZdLCBbLTY2LjYxMDQ5MTU0MjQ5MzIsIDQ1Ljk2MDMyNzc5OTk4MzJdLCBbLTY2LjYwOTg5ODY1NDQwNTcsIDQ1Ljk2MDg1ODU5NjUyN10sIFstNjYuNjA5Mjk2NzgzMTY1MywgNDUuOTYxMjAyMDUwNDA0NF0sIFstNjYuNjA4NDM0NDAwNDkyNiwgNDUuOTYxNTA4MDM0NzkyOF0sIFstNjYuNjA3NDczMjAzMTM4NiwgNDUuOTYxNTY0MjM1ODIzM10sIFstNjYuNjA0NDkwNzk2Mzk1MywgNDUuOTYxMDgzNDAyOTQyXSwgWy02Ni42MDIzNzA3NzIzMjQ4LCA0NS45NjEwNDU5MzUyNjk1XSwgWy02Ni41OTU3NDEyMDU1MjgsIDQ1Ljk2MTk0NTE1MjQxNjJdLCBbLTY2LjU5NzQ4MzkzNzE3OTIsIDQ1Ljk2MzczNzI5ODYxNl0sIFstNjYuNTk5MzE2NTAwMzU4OCwgNDUuOTYzNjEyNDEyMjU4M10sIFstNjYuNjAxMTQwMDgwMzg1NSwgNDUuOTYzODEyMjMwMjk1NV0sIFstNjYuNjAyODE5OTI5OTY2OCwgNDUuOTY0MzM2NzQ5MjE0M10sIFstNjYuNjA0MDc3NTcxMzY0NiwgNDUuOTY1MDExMTIzMzg0MV0sIFstNjYuNjA0NjE2NTYwNTM1MSwgNDUuOTY1NDEwNzQ4NjQ4XSwgWy02Ni42MDYxOTc1OTU0MzUxLCA0NS45Njg3NDUwMDk1NjgzXSwgWy02Ni42MTI3NTUyOTcwMDkyLCA0NS45NzIxOTE0NTAzNDgzXSwgWy02Ni42MTM0NTU5ODI5MzA4LCA0NS45NzMwMDkzMjQxOTI0XSwgWy02Ni42MTM1MzY4MzEzMDY0LCA0NS45NzM5NTgyOTI0NDY1XSwgWy02Ni42MTYwMTYxODE0OTA1LCA0NS45NzMzMDI3NTY5MDI0XSwgWy02Ni42MTgyMDgwNzA3ODM4LCA0NS45NzIyNjAxMjcyNDI1XSwgWy02Ni42MjI3ODk0Nzg3MzI4LCA0NS45Njg3NzYyMjgyOTE0XSwgWy02Ni42MjU4NjE3MTcwMDQ1LCA0NS45NjYxNTM3OTQyMDk1XSwgWy02Ni42MjY3OTU5NjQ5LCA0NS45NjU2MTA1NjAxOTg4XSwgWy02Ni42Mjg2NzM0NDM4NDM4LCA0NS45NjQ4MzAwNDIyMzczXV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiAxMSwgIk5laWdoYm91cmgiOiAiU291dGggRGV2b24iLCAiT0JKRUNUSUQiOiAxMSwgIlNoYXBlX0FyZWEiOiAyNTI1MjkzLjc1MTM1LCAiU2hhcGVfTGVuZyI6IDc4ODQuOTY2NzA3NDMsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZkOGQzYyIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjAxMDk1MTY0NjIxMywgNDUuOTgyNDY3MDY0MDEyNV0sIFstNjYuNjAxMjQ3ODc4MjE5NiwgNDUuOTg0MzIwOTY2MjAwNl0sIFstNjYuNjAxNjYxMTAzMjUwMywgNDUuOTg1ODM3NzQ5MDg3M10sIFstNjYuNjAyNjA0MzM0Mjk4NiwgNDUuOTg3ODg1MDI3OTgyOF0sIFstNjYuNjAzMzQ5OTM1OTg0NSwgNDUuOTg4Nzc3NTY3OTQ2Ml0sIFstNjYuNjA0NjQzNTA5OTkzNiwgNDUuOTg5NTM5MDI0MjMwNF0sIFstNjYuNjA2MDI2OTE1NTMxMSwgNDUuOTg5OTAxMDI0MzYzOV0sIFstNjYuNjA3ODIzNTQ2MDk5NCwgNDUuOTg5OTI1OTg5ODAzXSwgWy02Ni42MDkwOTkxNTM4MDI4LCA0NS45ODk1MjY1NDE0MjVdLCBbLTY2LjYwOTgxNzgwNjAzMDEsIDQ1Ljk4ODk4OTc3ODEyNzVdLCBbLTY2LjYxMDIyMjA0NzkwOCwgNDUuOTg4MzA5NDU0Mzc1NF0sIFstNjYuNjEwMTc3MTMyMTQzOCwgNDUuOTg1OTUwMTAxNzIyXSwgWy02Ni42MTAwMTU0MzUzOTI2LCA0NS45ODQ5NDUxNjE3MjExXSwgWy02Ni42MDk1OTMyMjcyMDkxLCA0NS45ODM3MDkyNDc3NjIyXSwgWy02Ni42MDkwOTAxNzA2NSwgNDUuOTgyNzYwNDQ2NjA4MV0sIFstNjYuNjA4NDE2NDM0MTg2OSwgNDUuOTgxODk5MDIwOTUwOV0sIFstNjYuNjA2ODk4MjgxMzU2NywgNDUuOTgwNzgxNjQ0NTE0Nl0sIFstNjYuNjA0Nzk2MjIzNTkxOSwgNDUuOTc5ODA3ODIzMTk2NV0sIFstNjYuNjAzNjEwNDQ3NDE2OSwgNDUuOTc5NDgzMjEyMjg0M10sIFstNjYuNjAxMzkxNjA4NjY1MSwgNDUuOTc5MzMzMzkxMjIxNF0sIFstNjYuNjAxMDk1MTY0NjIxMywgNDUuOTgyNDY3MDY0MDEyNV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogMTIsICJOZWlnaGJvdXJoIjogIkNvdHRvbiBNaWxsIENyZWVrIiwgIk9CSkVDVElEIjogMTIsICJTaGFwZV9BcmVhIjogNjM5ODc5LjA5NDAxOCwgIlNoYXBlX0xlbmciOiAzMTIwLjc4MzIwMjI3LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZmZmYjIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjY2Mzk3NzIzNDUwOTcsIDQ1Ljk4NDQ4OTQ5OTY4NDddLCBbLTY2LjY2NDU2MTEzOTQ0NDQsIDQ1Ljk4NDI2NDc4ODI1ODVdLCBbLTY2LjY2NTI0Mzg1OTA2MDMsIDQ1Ljk4NDczOTE3Nzk3NzRdLCBbLTY2LjY2NTU2NzI1MjU2MjYsIDQ1Ljk4NTI2MzQ5ODcyNjZdLCBbLTY2LjY2NTkzNTU2MTgyOTEsIDQ1Ljk4NTQzODI3MTIwNjFdLCBbLTY2LjY2NjUzNzQzMzA2OTQsIDQ1Ljk4NTQxOTU0NTYwOTddLCBbLTY2LjY2NzQ5ODYzMDQyMzQsIDQ1Ljk4NTA4MjQ4Mzc5MTFdLCBbLTY2LjY2ODA5MTUxODUxMDksIDQ1Ljk4NTIwNzMyMTc0MV0sIFstNjYuNjY5MDQzNzMyNzEyMSwgNDUuOTg2MzgwNzg0NzA5Ml0sIFstNjYuNjY5NTM3ODA2MTE4NCwgNDUuOTg2NjQyOTM3OTMwNF0sIFstNjYuNjcxNTE0MDk5NzQzNCwgNDUuOTg2MjU1OTQ5NDA1Nl0sIFstNjYuNjcyODcwNTU1ODIyNSwgNDUuOTg1ODMxNTA3MjY3Nl0sIFstNjYuNjczMzQ2NjYyOTIzMSwgNDUuOTg2MDY4Njk1OTIyNF0sIFstNjYuNjczNzU5ODg3OTUzOCwgNDUuOTg2NTg2NzYyMzQ0N10sIFstNjYuNjczNzE0OTcyMTg5NSwgNDUuOTg2Nzk4OTgwOTI1XSwgWy02Ni42NzMyMDI5MzI0Nzc2LCA0NS45ODcyMDQ2OTA2NTI1XSwgWy02Ni42NzMwNjgxODUxODUsIDQ1Ljk4NzUyMzAxNDY2NDRdLCBbLTY2LjY3MzcwNTk4OTAzNjcsIDQ1Ljk4Nzk0MTIwMjI1MV0sIFstNjYuNjczODQwNzM2MzI5MywgNDUuOTg4NjcxNDYyNTUwNV0sIFstNjYuNjczNzY4ODcxMTA2NiwgNDUuOTg5MjUxOTE4OTkyOF0sIFstNjYuNjczNTQ0MjkyMjg1NiwgNDUuOTg5ODE5ODg2NjA4OF0sIFstNjYuNjcyODE2NjU2OTA1NCwgNDUuOTkwNTMxMzk4MjU1NV0sIFstNjYuNjcxNTA1MTE2NTkwNiwgNDUuOTkxNDczODI1MDM5N10sIFstNjYuNjY5OTY4OTk3NDU0OCwgNDUuOTkyMjI5MDAzMTMyOV0sIFstNjYuNjY4MjYyMTk4NDE0OSwgNDUuOTkyNzc4MjE3MDkyMl0sIFstNjYuNjY2NDM4NjE4Mzg4MiwgNDUuOTkzMDk2NTA5MDUxM10sIFstNjYuNjY5Mzk0MDc1NjcyOSwgNDUuOTkyODU5MzUwNTEwNV0sIFstNjYuNjczMTEzMTAwOTQ5MiwgNDUuOTkyNzE1ODA2Njg5NV0sIFstNjYuNjc5OTY3MjQ2NTY3LCA0NS45OTI2NzIxMTkzNjU3XSwgWy02Ni42ODMwOTMzODM3NTU4LCA0NS45OTI4NTkzNTA1MTA1XSwgWy02Ni42ODYxNjU2MjIwMjc0LCA0NS45OTMyOTYyMjA3MTg0XSwgWy02Ni42ODg2NTM5NTUzNjQ0LCA0NS45OTM4NzAzODc3NDcxXSwgWy02Ni42OTA4MDA5Mjg4OTM1LCA0NS45OTQ3MTkxNDU0ODY2XSwgWy02Ni42OTI0MTc4OTY0MDQ5LCA0NS45OTU2NjE1MDA5NjE5XSwgWy02Ni42OTYwMTExNTc1NDE0LCA0NS45OTE1Mjk5OTU2NjU4XSwgWy02Ni43MDIxMTA3MTgzMjA2LCA0NS45OTE5ODU1OTk3NDg5XSwgWy02Ni42OTk2OTQyNTAyMDYzLCA0NS45ODgzMTU2OTU5MTU4XSwgWy02Ni42OTg2NzkxNTM5MzUyLCA0NS45ODY0MTgyMzUyNDU0XSwgWy02Ni42OTg0OTk0OTA4Nzg0LCA0NS45ODU2MjU1MjY4MjE5XSwgWy02Ni42OTgyMjEwMTMxNDAzLCA0NS45ODM2MjE4NTg4NjIxXSwgWy02Ni42OTgyMDMwNDY4MzQ2LCA0NS45ODEyMDYxMjUzN10sIFstNjYuNjk4NTYyMzcyOTQ4MywgNDUuOTc4NDg0Mzk3NTQxMV0sIFstNjYuNjk4OTkzNTY0Mjg0NywgNDUuOTc2NzE3Njk5ODQ2NF0sIFstNjYuNjk3OTg3NDUxMTY2NSwgNDUuOTc2NzgwMTI4Mjg3NV0sIFstNjYuNjk2Mjg5NjM1Mjc5NSwgNDUuOTc3MTU0Njk3NDU1OV0sIFstNjYuNjk1MzEwNDcxNjE5OCwgNDUuOTc3MjQyMDk2NTY0XSwgWy02Ni42OTQxMDY3MjkxMzkxLCA0NS45NzcxNzk2Njg2NDM3XSwgWy02Ni42OTAyODg4ODkxODE1LCA0NS45NzYzMTE5MTMyNjM5XSwgWy02Ni42ODQ5NTI4OTYzOTM5LCA0NS45NzQ2NzAwMDc5NjU5XSwgWy02Ni42ODAyMDA4MDg1NDA5LCA0NS45NzE5NjY2ODkwMDg0XSwgWy02Ni42Nzg0MjIxNDQyNzgzLCA0NS45NzE0MjM1MTIwMDQ0XSwgWy02Ni42NzYxMjI0NTcxNTEsIDQ1Ljk3MTM0MjM0NzE2N10sIFstNjYuNjczNTQ0MjkyMjg1NiwgNDUuOTcxNDM1OTk4ODkxOV0sIFstNjYuNjY1Mzg3NTg5NTA1OCwgNDUuOTcyMDg1MzEzMTYyNl0sIFstNjYuNjU0MTc2NjE0NzU5OSwgNDUuOTcyNTg0NzgwNDk4NV0sIFstNjYuNjUwNDEyNjczNzE5NSwgNDUuOTcyNTIyMzQ3MzI3OF0sIFstNjYuNjQ3ODUyNDc1MTU5NywgNDUuOTcyMjk3NTg3MzMwN10sIFstNjYuNjQ3NTAyMTMyMTk4OSwgNDUuOTcyMTQxNTAzNDYyN10sIFstNjYuNjQzNzkyMDkwMDc1NSwgNDUuOTcxNjI5NTQ1Mjg4MV0sIFstNjYuNjQxNDU2NDcwMzM2OCwgNDUuOTcxMDMwMTczNjA3XSwgWy02Ni42NDYyOTgzODk3MTgyLCA0NS45NzI1NDEwNzcyODY0XSwgWy02Ni42NTAzNDA4MDg0OTY4LCA0NS45NzQwMjA3MjM5OTg0XSwgWy02Ni42NTU3MTI3MzM4OTU4LCA0NS45NzY0MDU1NTY1ODUzXSwgWy02Ni42NTgxOTIwODQwOCwgNDUuOTc3NzIyNzg5MTkyNV0sIFstNjYuNjYwNDQ2ODU1NDQzMSwgNDUuOTc5MjMzNTEwMjg3Nl0sIFstNjYuNjYyMDcyODA2MTA3NCwgNDUuOTgwNjgxNzY2MTkzM10sIFstNjYuNjYzMzEyNDgxMTk5NCwgNDUuOTgyNTE3MDAxNTg1NF0sIFstNjYuNjYzOTc3MjM0NTA5NywgNDUuOTg0NDg5NDk5Njg0N11dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogMTMsICJOZWlnaGJvdXJoIjogIk5hc2h3YWFrc2lzIiwgIk9CSkVDVElEIjogMTMsICJTaGFwZV9BcmVhIjogNTkyODk2NC4xMTU5NSwgIlNoYXBlX0xlbmciOiAxNDAzMC40MTk0OTU1LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWIyNGMiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjY1MDAyNjM5ODE0NzMsIDQ1Ljk5MjMwMzg5NjI2NjRdLCBbLTY2LjY0ODEyMTk2OTc0NSwgNDUuOTkyMjk3NjU1MTc1OF0sIFstNjYuNjQ2NjEyODAwMDY3NywgNDUuOTkyNDIyNDc2ODU0XSwgWy02Ni42NDQ3NTMyODc0Mjk1LCA0NS45OTI3MjIwNDc3MzI5XSwgWy02Ni42NDMzMTU5ODI5NzQ5LCA0NS45OTMwNzc3ODYwNDU1XSwgWy02Ni42NDE2MDkxODM5MzUxLCA0NS45OTM2NjQ0MzcyMTU0XSwgWy02Ni42NDAwMTkxNjU4ODIyLCA0NS45OTQ0MDA4NjI4NTk3XSwgWy02Ni42Mzg0MjkxNDc4MjkzLCA0NS45OTU1OTkwOTM4MTA3XSwgWy02Ni42Mzc1NjY3NjUxNTY2LCA0NS45OTY2NzI0ODcwMDYzXSwgWy02Ni42MzcwOTA2NTgwNTYsIDQ1Ljk5NzYzOTc3MTE3ODFdLCBbLTY2LjYzNjg0ODExMjkyOTMsIDQ1Ljk5ODY1MDcyMTA4MDFdLCBbLTY2LjYzNjg1NzA5NjA4MjEsIDQ1Ljk5OTY3NDEzMzAzMTRdLCBbLTY2LjYzNzI3MDMyMTExMjgsIDQ2LjAwMDUyOTA0MTkxODhdLCBbLTY2LjYzNzkwODEyNDk2NDUsIDQ2LjAwMTMyMTUzNjg5OTRdLCBbLTY2LjYzODczNDU3NTAyNTksIDQ2LjAwMjAyNjY2MDY4NTJdLCBbLTY2LjYzOTc0MDY4ODE0NDEsIDQ2LjAwMjYwNjk3NzA1OTVdLCBbLTY2LjY0MDYzOTAwMzQyODMsIDQ2LjAwMjk3NTEzMTYwMzVdLCBbLTY2LjY1MDAyNjM5ODE0NzMsIDQ1Ljk5MjMwMzg5NjI2NjRdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDE0LCAiTmVpZ2hib3VyaCI6ICJXZXN0IEhpbGxzIiwgIk9CSkVDVElEIjogMTQsICJTaGFwZV9BcmVhIjogNTk3MzAzLjg5MDQ3MiwgIlNoYXBlX0xlbmciOiAzMzY0LjU0NzMzMDM1LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZmZmYjIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjYzMDk1NTE2NDY2NTUsIDQ2LjAwNzU5ODY5NDQ3OTJdLCBbLTY2LjYzMDY3NjY4NjkyNzQsIDQ2LjAxNDM5Mjk0NTkzODFdLCBbLTY2LjYzMDM2MjI3NjU3NzksIDQ2LjAxNjE0NTk2NDQyOThdLCBbLTY2LjYzMzc3NTg3NDY1NzYsIDQ2LjAxNjMzMzExNjE0NThdLCBbLTY2LjYzNTM4Mzg1OTAxNjIsIDQ2LjAxNjMwMTkyNDIzNzFdLCBbLTY2LjYzODE3NzYxOTU0OTgsIDQ2LjAxNTk1MjU3MzY1NzldLCBbLTY2LjYzOTQwODMxMTQ4OSwgNDYuMDE1NTg0NTA1NDgxNF0sIFstNjYuNjQwMDM3MTMyMTg3OSwgNDYuMDE1MTkxNDgwODI1N10sIFstNjYuNjQwNjY1OTUyODg2OCwgNDYuMDE0NTk4ODE5MzE3XSwgWy02Ni42NDEwNzAxOTQ3NjQ2LCA0Ni4wMTM5MTg4MTAzOTNdLCBbLTY2LjY0MTIzMTg5MTUxNTgsIDQ2LjAxMzE5NTEyMTk4NjldLCBbLTY2LjY0MDYzMDAyMDI3NTQsIDQ2LjAxMTk3ODU1NTQ4MTNdLCBbLTY2LjYzOTY5NTc3MjM3OTksIDQ2LjAxMDg2ODAyNTI1NjVdLCBbLTY2LjYzODY5ODY0MjQxNDYsIDQ2LjAxMDA1Njk0OTc2NjhdLCBbLTY2LjYzNzI2MTMzNzk2LCA0Ni4wMDkyNDU4NjIzODMyXSwgWy02Ni42MzMxNzQwMDM0MTcyLCA0Ni4wMDc5MTA2NjE4NjI2XSwgWy02Ni42MzA5NjQxNDc4MTgzLCA0Ni4wMDc0MjM5OTE5NzZdLCBbLTY2LjYzMDk1NTE2NDY2NTUsIDQ2LjAwNzU5ODY5NDQ3OTJdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDE1LCAiTmVpZ2hib3VyaCI6ICJOb3J0aGJyb29rIEhlaWdodHMiLCAiT0JKRUNUSUQiOiAxNSwgIlNoYXBlX0FyZWEiOiA2MTI3MDIuMjg2OTU3LCAiU2hhcGVfTGVuZyI6IDMwNzYuMDY3NTU5MTIsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlZDk3NiIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjQwMTg5ODQ1Nzg2MiwgNDYuMDExMzkyMDk4NDc4Ml0sIFstNjYuNjQzOTA4ODcxMDYyNSwgNDYuMDEyMzM0MTY5OTk3XSwgWy02Ni42NDcyNzc1NTMzNzc5LCA0Ni4wMTI3MTQ3MzczODQ1XSwgWy02Ni42NDgxMTI5ODY1OTIxLCA0Ni4wMTI2MDg2Nzc4ODRdLCBbLTY2LjY0OTAxMTMwMTg3NjIsIDQ2LjAxMjI3MTc4MTY1MDldLCBbLTY2LjY0OTU5NTIwNjgxMDksIDQ2LjAxMTg0NzUzOTAzMDddLCBbLTY2LjY1MDA0NDM2NDQ1MywgNDYuMDExMjA0OTMwMDQwNV0sIFstNjYuNjQ5Njg1MDM4MzM5NCwgNDYuMDEwMjQ0MTIyMDg5M10sIFstNjYuNjQ5MDkyMTUwMjUxOCwgNDYuMDA5MzM5NDQ5OTk2XSwgWy02Ni42NDgyODM2NjY0OTYxLCA0Ni4wMDg1MjIxMTI4MzAzXSwgWy02Ni42NDcyODY1MzY1MzA3LCA0Ni4wMDc4MTA4MzI0OTE0XSwgWy02Ni42NDYzNzAyNTQ5NDA5LCA0Ni4wMDczMzY2NDA1MTc1XSwgWy02Ni42NDQ4MzQxMzU4MDUxLCA0Ni4wMDY4MTI1Mjg4Njk1XSwgWy02Ni42NDIxMzAyMDY3OTk5LCA0Ni4wMDU1OTU4MjE5NzA5XSwgWy02Ni42MzkyNDY2MTQ3Mzc5LCA0Ni4wMDQ1OTEyMzg2NzAyXSwgWy02Ni42MzU3MTYyMzU2NzEzLCA0Ni4wMDg2OTA1NzI2MjM1XSwgWy02Ni42MzcyNjEzMzc5NiwgNDYuMDA5MjQ1ODYyMzgzMl0sIFstNjYuNjM4MjQwNTAxNjE5NywgNDYuMDA5NzU3NDcyNzMzM10sIFstNjYuNjM5MzA5NDk2ODA3OCwgNDYuMDEwNTE4NjQwMzQ5OV0sIFstNjYuNjQwMTg5ODQ1Nzg2MiwgNDYuMDExMzkyMDk4NDc4Ml1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogMTYsICJOZWlnaGJvdXJoIjogIkJyb29rc2lkZSBNaW5pIEhvbWUgUGFyayIsICJPQkpFQ1RJRCI6IDE2LCAiU2hhcGVfQXJlYSI6IDU3NTE4OC4wMzQzNzcsICJTaGFwZV9MZW5nIjogMzAyMi45NzU2NDMzLCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZmZmYjIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjY0ODY5Njg5MTUyNjgsIDQ2LjAwODg5NjQ2NzIyOTddLCBbLTY2LjY0OTk2MzUxNjA3NzQsIDQ2LjAwODkwMjcwNjQ0ODJdLCBbLTY2LjY1MTIxMjE3NDMyMjMsIDQ2LjAwODczNDI0NzMwMV0sIFstNjYuNjUyMzc5OTg0MTkxNywgNDYuMDA4MzkxMDg4MTkxOV0sIFstNjYuNjUzNjE5NjU5MjgzOCwgNDYuMDA3NzczMzk2NDMwN10sIFstNjYuNjU0MzgzMjI3Mjc1MywgNDYuMDA3MDQzMzg4MTgzNV0sIFstNjYuNjU1MDAzMDY0ODIxMywgNDYuMDA2MDQ1MDcwNzExM10sIFstNjYuNjU1MjkwNTI1NzEyMywgNDYuMDA0OTc4MDk4OTk1Nl0sIFstNjYuNjU1MjA5Njc3MzM2NywgNDYuMDAzODk4NjI3MTM2OF0sIFstNjYuNjU0OTQ5MTY1OTA0MywgNDYuMDAzMTkzNTI3MjA5Ml0sIFstNjYuNjU0NDE5MTU5ODg2NywgNDYuMDAyMzY5ODU5Mjc2NF0sIFstNjYuNjUzNTExODYxNDQ5NywgNDYuMDAxNDA4ODk3ODU2Ml0sIFstNjYuNjUyMjk5MTM1ODE2MSwgNDYuMDAwNDA0MjM4NTI1MV0sIFstNjYuNjQ5OTk5NDQ4Njg4OCwgNDUuOTk5MDQzODYzMjc2MV0sIFstNjYuNjQ1NzUwNDE3Mzk0OSwgNDUuOTk3MjAyOTM1MjU4OF0sIFstNjYuNjM5MjQ2NjE0NzM3OSwgNDYuMDA0NTkxMjM4NjcwMl0sIFstNjYuNjQxNjU0MDk5Njk5MywgNDYuMDA1NDE0ODczNTMwOF0sIFstNjYuNjQ0ODM0MTM1ODA1MSwgNDYuMDA2ODEyNTI4ODY5NV0sIFstNjYuNjQ2NTQ5OTE3OTk3OCwgNDYuMDA3NDIzOTkxOTc2XSwgWy02Ni42NDc4MTY1NDI1NDg0LCA0Ni4wMDgxNjAyMzQ1MDI1XSwgWy02Ni42NDg2OTY4OTE1MjY4LCA0Ni4wMDg4OTY0NjcyMjk3XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiAxNywgIk5laWdoYm91cmgiOiAiSGVyb24gU3ByaW5ncyIsICJPQkpFQ1RJRCI6IDE3LCAiU2hhcGVfQXJlYSI6IDk2NTEzMS4wMDAzMjEsICJTaGFwZV9MZW5nIjogMzgwMC45NDU5ODkyOCwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmVkOTc2IiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni42NjY0Mzg2MTgzODgyLCA0NS45OTMwOTY1MDkwNTEzXSwgWy02Ni42Njg0NTA4NDQ2MjQ2LCA0NS45OTQ0OTQ0NzU1ODcxXSwgWy02Ni42NzAyOTIzOTA5NTcsIDQ1Ljk5NTk5ODQ5ODM2MjNdLCBbLTY2LjY3MTk0NTI5MTA3OTgsIDQ1Ljk5NzYxNDgwOTIxODVdLCBbLTY2LjY3MzM5MTU3ODY4NzMsIDQ1Ljk5OTMxODQzNzEyMTRdLCBbLTY2LjY3NDczOTA1MTYxMzQsIDQ2LjAwMjc2Mjk3NTA0NjddLCBbLTY2LjY3NTY0NjM1MDA1MDQsIDQ2LjAwNTU0NTkwNTIxODldLCBbLTY2LjY3NjU2MjYzMTY0MDIsIDQ2LjAwOTA1MjQ0NzQ4MTddLCBbLTY2LjY3NzExOTU4NzExNjQsIDQ2LjAxMTg3ODczMzQ1MThdLCBbLTY2LjY3NzM1MzE0OTA5MDIsIDQ2LjAxMjQyNzc1MjM4NDNdLCBbLTY2LjY3ODEwNzczMzkyODksIDQ2LjAxMzc1MDM2NjUyMzRdLCBbLTY2LjY3OTA4Njg5NzU4ODYsIDQ2LjAxNDk5ODA4NjcxNTddLCBbLTY2LjY4MDI4MTY1NjkxNjUsIDQ2LjAxNjE1MjIwMjgzMDZdLCBbLTY2LjY4MTM3NzYwMTU2MzEsIDQ2LjAxNzAwMDYxODc3NDddLCBbLTY2LjY4MTAwMDMwOTE0MzgsIDQ2LjAwOTYxMzk3Mjc0NjhdLCBbLTY2LjY5MjQxNzg5NjQwNDksIDQ1Ljk5NTY2MTUwMDk2MTldLCBbLTY2LjY5MDgwMDkyODg5MzUsIDQ1Ljk5NDcxOTE0NTQ4NjZdLCBbLTY2LjY4ODY1Mzk1NTM2NDQsIDQ1Ljk5Mzg3MDM4Nzc0NzFdLCBbLTY2LjY4NjE2NTYyMjAyNzQsIDQ1Ljk5MzI5NjIyMDcxODRdLCBbLTY2LjY4MzA5MzM4Mzc1NTgsIDQ1Ljk5Mjg1OTM1MDUxMDVdLCBbLTY2LjY3OTk2NzI0NjU2NywgNDUuOTkyNjcyMTE5MzY1N10sIFstNjYuNjczMTEzMTAwOTQ5MiwgNDUuOTkyNzE1ODA2Njg5NV0sIFstNjYuNjY5Mzk0MDc1NjcyOSwgNDUuOTkyODU5MzUwNTEwNV0sIFstNjYuNjY2NDM4NjE4Mzg4MiwgNDUuOTkzMDk2NTA5MDUxM11dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogMTgsICJOZWlnaGJvdXJoIjogIlJveWFsIFJvYWQiLCAiT0JKRUNUSUQiOiAxOCwgIlNoYXBlX0FyZWEiOiAyMTk2ODI3LjQyNzU4LCAiU2hhcGVfTGVuZyI6IDc2NzQuODIyNjU1MzMsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZmZmZiMiIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjM3OTI2MDkxMjcwMiwgNDUuOTc2NzIzOTQyNjkzN10sIFstNjYuNjM4NTk5ODI3NzMzMywgNDUuOTc2OTczNjU2MDA3NV0sIFstNjYuNjM4MDUxODU1NDEsIDQ1Ljk3NjkxMTIyNzc4NDZdLCBbLTY2LjYzNzY0NzYxMzUzMjEsIDQ1Ljk3NzExNzI0MDY1MzFdLCBbLTY2LjYzNjIyODI3NTM4MzIsIDQ1Ljk3ODg5NjQxMDgwNTldLCBbLTY2LjYzNTQyODc3NDc4MDQsIDQ1Ljk4MDM2MzQwMjg0MTddLCBbLTY2LjYzNTA2OTQ0ODY2NjcsIDQ1Ljk4MTk5ODg5NzA3NjNdLCBbLTY2LjYzNTMyOTk2MDA5OTEsIDQ1Ljk4NjkwNTA4OTkxMDFdLCBbLTY2LjYzNTk1ODc4MDc5OCwgNDUuOTg4MTY1ODk4NzUzOV0sIFstNjYuNjM3MTg5NDcyNzM3MiwgNDUuOTg5NDI2Njc4ODhdLCBbLTY2LjYzODIwNDU2OTAwODMsIDQ1Ljk5MDA1MDgxNjgzXSwgWy02Ni42NDAxMDAwMTQyNTc4LCA0NS45OTA2NDk5ODI2NDA3XSwgWy02Ni42NDIxMTIyNDA0OTQyLCA0NS45OTEwMTgyMTY3NDM3XSwgWy02Ni42NDQxNzgzNjU2NDc3LCA0NS45OTExNDkyODI1MjgyXSwgWy02Ni42NDU5MDMxMzA5OTMyLCA0NS45OTEwODA2MjkwNjA4XSwgWy02Ni42NTAzMjI4NDIxOTExLCA0NS45OTA1NTYzNjM0MTAzXSwgWy02Ni42NTU1OTU5NTI5MDg5LCA0NS45ODk3MTM3ODMyMTExXSwgWy02Ni42NTU5NDYyOTU4Njk3LCA0NS45ODgzNTkzODY2NzgzXSwgWy02Ni42NTY1MjEyMTc2NTE1LCA0NS45ODcwNDg2NDg4MDE1XSwgWy02Ni42NTc3MTU5NzY5Nzk0LCA0NS45ODUzMDcxOTE4OTgyXSwgWy02Ni42NTg1NjkzNzY0OTkzLCA0NS45ODQzODMzODYwNjk0XSwgWy02Ni42NTg3NjcwMDU4NjE4LCA0NS45ODQzNzA5MDIxMDEyXSwgWy02Ni42NTg2NjgxOTExODA2LCA0NS45ODQxMDI0OTYxMDU3XSwgWy02Ni42NTY3OTk2OTUzODk2LCA0NS45ODI5OTE0MDYyODExXSwgWy02Ni42NTQzNTYyNzc4MTY4LCA0NS45ODE5NjE0NDM1NTA0XSwgWy02Ni42Mzc5MjYwOTEyNzAyLCA0NS45NzY3MjM5NDI2OTM3XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiAxOSwgIk5laWdoYm91cmgiOiAiRnVsdG9uIEhlaWdodHMiLCAiT0JKRUNUSUQiOiAxOSwgIlNoYXBlX0FyZWEiOiAyMDA4Njk5LjI0OTAxLCAiU2hhcGVfTGVuZyI6IDU1ODYuMDc4OTcxODcsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlYjI0YyIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjU5MDI3NTE3Mjk0MiwgNDUuOTg0NDE0NTk1OTc3M10sIFstNjYuNjYyMjM0NTAyODU4NSwgNDUuOTg1NjQ0MjUyMzQ4Nl0sIFstNjYuNjYzMDk2ODg1NTMxMiwgNDUuOTg1NzQ0MTIxNzE3Nl0sIFstNjYuNjY0MzM2NTYwNjIzMywgNDUuOTg1NjMxNzY4NjY0OF0sIFstNjYuNjY0MjI4NzYyNzg5MiwgNDUuOTg0ODc2NTAwNTU4NF0sIFstNjYuNjYzMDUxOTY5NzY3LCA0NS45ODIwNDI1OTI4MjQ1XSwgWy02Ni42NjE4ODQxNTk4OTc3LCA0NS45ODA0Njk1MjQxNjIzXSwgWy02Ni42NjA0NDY4NTU0NDMxLCA0NS45NzkyMzM1MTAyODc2XSwgWy02Ni42NTg5NzM2MTgzNzcxLCA0NS45NzgyMDM0Nzc2NDgzXSwgWy02Ni42NTY5NzkzNTg0NDY0LCA0NS45NzcwNDIzMjY5NzE0XSwgWy02Ni42NTIzMDgxMTg5NjksIDQ1Ljk3NDgzODU3MDgyODJdLCBbLTY2LjY0NzY2MzgyODk1MDEsIDQ1Ljk3MzAwOTMyNDE5MjRdLCBbLTY2LjY0MTQ1NjQ3MDMzNjgsIDQ1Ljk3MTAzMDE3MzYwN10sIFstNjYuNjQwMjE2Nzk1MjQ0NywgNDUuOTczNTA4NzgzMTk1Ml0sIFstNjYuNjM3OTI2MDkxMjcwMiwgNDUuOTc2NzIzOTQyNjkzN10sIFstNjYuNjU0NzE1NjAzOTMwNCwgNDUuOTgyMDg2Mjg4NTM4Ml0sIFstNjYuNjU3MTIzMDg4ODkxOSwgNDUuOTgzMTY2MTg1OTMzN10sIFstNjYuNjU4NjY4MTkxMTgwNiwgNDUuOTg0MTAyNDk2MTA1N10sIFstNjYuNjU4NzY3MDA1ODYxOCwgNDUuOTg0MzcwOTAyMTAxMl0sIFstNjYuNjU5MDI3NTE3Mjk0MiwgNDUuOTg0NDE0NTk1OTc3M11dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogMjAsICJOZWlnaGJvdXJoIjogIk1haW4gU3RyZWV0IiwgIk9CSkVDVElEIjogMjAsICJTaGFwZV9BcmVhIjogMTI5NDU4Mi4xNzQ0NCwgIlNoYXBlX0xlbmciOiA1NTQ1Ljg5MzE1Nzk4LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWIyNGMiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjcwNDU3MjEwMjE5OSwgNDUuOTc4MzQwODE2NDQwNl0sIFstNjYuNzAxMDk1NjIyMDQ5NSwgNDUuOTc4NTk2NzY1MDk5Ml0sIFstNjYuNzAxMjQ4MzM1NjQ3OCwgNDUuOTc5Njc2NzMwNTU3Ml0sIFstNjYuNzAxNjI1NjI4MDY3MSwgNDUuOTgwNTQ0NDMzMjA3M10sIFstNjYuNzAzMzk1MzA5MTc2OCwgNDUuOTgyNTU0NDU0NzM1NV0sIFstNjYuNzAzOTcwMjMwOTU4NywgNDUuOTgyNjg1NTQwNTYxMl0sIFstNjYuNzA0Njg4ODgzMTg2LCA0NS45ODI2MTY4NzY1OTZdLCBbLTY2LjcwNTI3Mjc4ODEyMDcsIDQ1Ljk4MjMyMzQ5MzIzOTZdLCBbLTY2LjcwNTYxNDE0NzkyODYsIDQ1Ljk4MTM2MjE4MzY4OThdLCBbLTY2LjcwNTM5ODU1MjI2MDQsIDQ1Ljk3OTk1MTQwMDQ5MjldLCBbLTY2LjcwNDU3MjEwMjE5OSwgNDUuOTc4MzQwODE2NDQwNl1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogMjEsICJOZWlnaGJvdXJoIjogIlJlZ2ltZW50IENyZWVrIiwgIk9CSkVDVElEIjogMjEsICJTaGFwZV9BcmVhIjogMTIzNjMyLjEyNjg5NCwgIlNoYXBlX0xlbmciOiAxMzc1LjAzMjY1MDMsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZmZmZiMiIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNzE2Njk5MzU4NTM0NywgNDUuOTc3NjQxNjMzNTg3XSwgWy02Ni43MDgxNjUzNjMzMzU1LCA0NS45NzgxMDM1OTQ2NzYyXSwgWy02Ni43MDc0NjQ2Nzc0MTM5LCA0NS45NzkyMTQ3ODI1OTI1XSwgWy02Ni43MDcwOTYzNjgxNDc0LCA0NS45ODA0MDcwOTk4ODA3XSwgWy02Ni43MDc2MzUzNTczMTc5LCA0NS45ODEyODcyNzU3NTEyXSwgWy02Ni43MDg2NTk0MzY3NDE4LCA0NS45ODIxNDg3MTA5MjY2XSwgWy02Ni43MDk4MDkyODAzMDU1LCA0NS45ODI2ODU1NDA1NjEyXSwgWy02Ni43MTA3MDc1OTU1ODk2LCA0NS45ODI2MzU2MDMxNDA0XSwgWy02Ni43MTE3MzE2NzUwMTM1LCA0NS45ODIzNjcxODg3MzE2XSwgWy02Ni43MTMwODgxMzEwOTI1LCA0NS45ODE1NDMyMTA3ODk4XSwgWy02Ni43MTQ3MDUwOTg2MDM5LCA0NS45ODAxOTQ4NTY3OTY5XSwgWy02Ni43MTYwNDM1ODgzNzczLCA0NS45Nzg3MDI4ODk4MDU3XSwgWy02Ni43MTY2OTkzNTg1MzQ3LCA0NS45Nzc2NDE2MzM1ODddXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDIyLCAiTmVpZ2hib3VyaCI6ICJHaWxyaWRnZSBFc3RhdGVzIiwgIk9CSkVDVElEIjogMjIsICJTaGFwZV9BcmVhIjogMjcxNzM5LjY3Mjc0NCwgIlNoYXBlX0xlbmciOiAyMDk1Ljc3NjAzNDgsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlZDk3NiIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNzU5NzQ2NjI2OTQ5NywgNDUuOTU4NDM1NjI1MDQ5NV0sIFstNjYuNzQ0ODc5NTA4OTk3NSwgNDUuOTU4NDY2ODQ5NTgyN10sIFstNjYuNzQ1MDMyMjIyNTk1OCwgNDUuOTU4ODQ3Nzg3NDcwNF0sIFstNjYuNzQ1ODEzNzU2ODkzLCA0NS45NTk1OTA5MjEwNTc2XSwgWy02Ni43NDU2MzQwOTM4MzYyLCA0NS45NTk4NTMyMDExMjA1XSwgWy02Ni43NDU2MDcxNDQzNzc2LCA0NS45NjAzMzQwNDQ2NzhdLCBbLTY2Ljc0NTA0MTIwNTc0ODYsIDQ1Ljk2MTAxNDcxMjE4OTddLCBbLTY2Ljc0NTE5MzkxOTM0NjksIDQ1Ljk2MTMyNjk0MjE5NTZdLCBbLTY2Ljc0NTA3NzEzODM2LCA0NS45NjE5MDc2ODUzMjY1XSwgWy02Ni43NDU1NTMyNDU0NjA2LCA0NS45NjIxMTk5OTg0OTk5XSwgWy02Ni43NDU2MDcxNDQzNzc2LCA0NS45NjIyODg1OTk1NTgxXSwgWy02Ni43NDQ3NDQ3NjE3MDQ5LCA0NS45NjM0NTAwNTk1NzIzXSwgWy02Ni43NDQ2NzI4OTY0ODIxLCA0NS45NjQ1NDkwNTMwNzkxXSwgWy02Ni43NDUzNzM1ODI0MDM4LCA0NS45NjUzMzU4MTkxMzA2XSwgWy02Ni43NDU4MjI3NDAwNDU4LCA0NS45NjU0NzMxODk4MzVdLCBbLTY2Ljc0NjE4MjA2NjE1OTUsIDQ1Ljk2NTgyMjg1OTE4Ml0sIFstNjYuNzQ2NDk2NDc2NTA4OSwgNDUuOTY3MzA4OTI5MjgyOF0sIFstNjYuNzQ3ODUyOTMyNTg3OSwgNDUuOTY3MTkwMjk0ODk4N10sIFstNjYuNzQ5NTQxNzY1MzIyMSwgNDUuOTY3NTA4NzMzOTg3XSwgWy02Ni43NDk2MTM2MzA1NDQ4LCA0NS45NjQ0ODAzNjY2MjM2XSwgWy02Ni43NTU1ODc0MjcxODQyLCA0NS45NjQ4MjM3OTgwNDkzXSwgWy02Ni43NTU1Nzg0NDQwMzE0LCA0NS45NjkwMTk3MzM3MjgxXSwgWy02Ni43NTU3MjIxNzQ0NzY4LCA0NS45NjkwNzU5MjcxMzg0XSwgWy02Ni43NjA4Nzg1MDQyMDc3LCA0NS45Njk3MzE1MTI3MTI4XSwgWy02Ni43NjI0MjM2MDY0OTYzLCA0NS45NzAxNjIzMjE4NjU0XSwgWy02Ni43NjMzMTI5Mzg2Mjc2LCA0NS45NzA1NjgxNTM1MDkxXSwgWy02Ni43NjU4MTkyMzgyNzAzLCA0NS45NzA5MzAyNzc2OTYyXSwgWy02Ni43NjcxNjY3MTExOTY1LCA0NS45NzA4ODY1NzMxNzg2XSwgWy02Ni43NjkzODU1NDk5NDgzLCA0NS45NzExNTUwNDMyNDIxXSwgWy02Ni43NzI5OTY3NzczOTA0LCA0NS45NzA5MTE1NDcxOTI5XSwgWy02Ni43NzQzMDgzMTc3MDUyLCA0NS45NzA5OTg5NTYxNTQyXSwgWy02Ni43NzY3Njk3MDE1ODM3LCA0NS45NzA3MzY3Mjg4NTYzXSwgWy02Ni43Nzg1NzUzMTUzMDQ4LCA0NS45NzA5Njc3Mzg2ODM5XSwgWy02Ni43Nzk0Mjg3MTQ4MjQ3LCA0NS45NzEzNzk4MDc4NzU5XSwgWy02Ni43ODE4OTAwOTg3MDMyLCA0NS45NzE1Mjk2NTA0NTg0XSwgWy02Ni43ODE5OTc4OTY1MzczLCA0NS45NzE2NzMyNDkyMTk1XSwgWy02Ni43ODI5MzIxNDQ0MzI4LCA0NS45NzE3MTA3MDk3MDQ2XSwgWy02Ni43ODM0NjIxNTA0NTA0LCA0NS45NzE1Mjk2NTA0NTg0XSwgWy02Ni43ODMxMjk3NzM3OTUzLCA0NS45NzA3NDkyMTU4OTg2XSwgWy02Ni43ODI0MDIxMzg0MTUyLCA0NS45Njk4MjUxNjcxNjE1XSwgWy02Ni43ODE4NTQxNjYwOTE5LCA0NS45Njk2OTQwNTA4ODkxXSwgWy02Ni43ODE2NDc1NTM1NzY1LCA0NS45NjkyNjMyMzgwOTQzXSwgWy02Ni43ODExODk0MTI3ODE2LCA0NS45Njg4NTczOTY4ODkzXSwgWy02Ni43ODA1NDI2MjU3NzcsIDQ1Ljk2ODYyMDEzNDQ5OTddLCBbLTY2Ljc4MDA2NjUxODY3NjQsIDQ1Ljk2ODY3MDA4NDU2MDldLCBbLTY2Ljc3OTk1ODcyMDg0MjQsIDQ1Ljk2ODU3MDE4NDM5MzVdLCBbLTY2Ljc3OTk1ODcyMDg0MjQsIDQ1Ljk2ODM5NTM1ODY2NjldLCBbLTY2Ljc4MDI0NjE4MTczMzMsIDQ1Ljk2ODA4MzE2ODQ5NjldLCBbLTY2Ljc3OTk4NTY3MDMwMDksIDQ1Ljk2NzIyNzc1ODQxNTldLCBbLTY2Ljc4MDAzMDU4NjA2NTEsIDQ1Ljk2NjMyMjM4Mjk5MTddLCBbLTY2Ljc3OTg5NTgzODc3MjUsIDQ1Ljk2NjEyODgxODA1XSwgWy02Ni43Nzk1NTQ0Nzg5NjQ1LCA0NS45NjYwNzI2MjE2NDk5XSwgWy02Ni43NzkzMjk5MDAxNDM1LCA0NS45NjU1NzMwOTU1ODhdLCBbLTY2Ljc3OTAwNjUwNjY0MTIsIDQ1Ljk2NTM0MjA2MzI2MDldLCBbLTY2Ljc3OTMyMDkxNjk5MDYsIDQ1Ljk2NDY0ODk2MDQ5ODZdLCBbLTY2Ljc3OTA5NjMzODE2OTYsIDQ1Ljk2NDE4MDY0MjkxMjNdLCBbLTY2Ljc3Nzk3MzQ0NDA2NDUsIDQ1Ljk2MzQyNTA4MjE5MzhdLCBbLTY2Ljc3ODMwNTgyMDcxOTYsIDQ1Ljk2MzAxOTE5ODIxNDVdLCBbLTY2Ljc3NzU0MjI1MjcyODEsIDQ1Ljk2MjcwMDczMzMxOF0sIFstNjYuNzc3NTUxMjM1ODgwOSwgNDUuOTYyMjMyMzk5MjYyNF0sIFstNjYuNzc4NDA0NjM1NDAwOCwgNDUuOTYxNTE0Mjc5MzU0NV0sIFstNjYuNzc4OTI1NjU4MjY1NiwgNDUuOTYwNzk2MTUwMTM4N10sIFstNjYuNzc5MDA2NTA2NjQxMiwgNDUuOTYwMTY1NDM3NjcxOV0sIFstNjYuNzgwMTM4MzgzODk5MiwgNDUuOTU4OTk3NjYzOTU0Ml0sIFstNjYuNzgxMDU0NjY1NDg5LCA0NS45NTg4MzUyOTc3NDUxXSwgWy02Ni43ODE0ODU4NTY4MjU0LCA0NS45NTgzNzk0MjA4NDU1XSwgWy02Ni43NzA2MjUyMjUwNDA0LCA0NS45NTg0MTA2NDU0MTAzXSwgWy02Ni43NzE1NDE1MDY2MzAyLCA0NS45NjYwNzg4NjU2OTcyXSwgWy02Ni43Njc3NDE2MzI5NzgzLCA0NS45NjU0NDE5NjkyNTAzXSwgWy02Ni43NTk4NTQ0MjQ3ODM4LCA0NS45NjUxMDQ3ODU4MTRdLCBbLTY2Ljc2MDAxNjEyMTUzNDksIDQ1Ljk2MzIyNTI2Mjc2MDJdLCBbLTY2Ljc1OTc0NjYyNjk0OTcsIDQ1Ljk1ODQzNTYyNTA0OTVdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDIzLCAiTmVpZ2hib3VyaCI6ICJTaWx2ZXJ3b29kIiwgIk9CSkVDVElEIjogMjMsICJTaGFwZV9BcmVhIjogMjUwNDk0MC4wODY2NiwgIlNoYXBlX0xlbmciOiAxMTMxMi43ODg2MDk5LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjcxMzUxMDMzOTI3NiwgNDUuOTU4NTI5Mjk4NTk2Ml0sIFstNjYuNzEyMDM3MTAyMjEwMSwgNDUuOTU4ODYwMjc3MTkyOF0sIFstNjYuNzEwNjcxNjYyOTc4MiwgNDUuOTU5MzU5ODYzNzgzXSwgWy02Ni43MDk2ODM1MTYxNjU3LCA0NS45NTk4NjU2OTA2MTYzXSwgWy02Ni43MDg2MTQ1MjA5Nzc2LCA0NS45NjA2Mjc1NDQ1Mzg4XSwgWy02Ni43MDc3NDMxNTUxNTIsIDQ1Ljk2MTQ5NTU0NTY2NzFdLCBbLTY2LjcwNzExNDMzNDQ1MzEsIDQ1Ljk2MjQxOTczMzM1OTddLCBbLTY2LjcwNjk3MDYwNDAwNzcsIDQ1Ljk2MzE5NDA0MDkwODZdLCBbLTY2LjcwNzE3NzIxNjUyMywgNDUuOTYzOTU1ODQ5MDY0Nl0sIFstNjYuNzA4MjkxMTI3NDc1MywgNDUuOTY0MTYxOTEwMTI2NV0sIFstNjYuNzA5NDMxOTg3ODg2MSwgNDUuOTY0MTE4MjAwMjY4M10sIFstNjYuNzA5ODA5MjgwMzA1NSwgNDUuOTY0MDQ5NTEzMjc4N10sIFstNjYuNzEyMTQ0OTAwMDQ0MiwgNDUuOTYzMDMxNjg2OTk2Nl0sIFstNjYuNzE2ODM0MTA1ODI3MywgNDUuOTYyMzM4NTU1MzI4Nl0sIFstNjYuNzE5ODk3MzYwOTQ2MSwgNDUuOTYyMDM4ODIwMDI5N10sIFstNjYuNzIxOTA5NTg3MTgyNiwgNDUuOTYxNjY0MTQ4NjI1Nl0sIFstNjYuNzI0MDI5NjExMjUzMSwgNDUuOTYxNTY0MjM1ODIzM10sIFstNjYuNzI3MTkxNjgxMDUzMiwgNDUuOTYxNzk1MjgzOTA1Ml0sIFstNjYuNzI5Nzk2Nzk1Mzc3MSwgNDUuOTYyNzk0Mzk5NjU0XSwgWy02Ni43MzA3MjIwNjAxMTk4LCA0NS45NjI5NzU0ODc0NTQ3XSwgWy02Ni43MzE2MjAzNzU0MDM5LCA0NS45NjI5NjkyNDMwNTc2XSwgWy02Ni43MzI0NjQ3OTE3NzEsIDQ1Ljk2MzM2MjYzODY5ODJdLCBbLTY2LjczMzYxNDYzNTMzNDYsIDQ1Ljk2MzY0MzYzMzg3NDFdLCBbLTY2LjczNTk4NjE4NzY4NDcsIDQ1Ljk2NDQ5Mjg1NTA3NjRdLCBbLTY2LjczNzU5NDE3MjA0MzMsIDQ1Ljk2NDgyMzc5ODA0OTNdLCBbLTY2LjczODkwNTcxMjM1ODEsIDQ1Ljk2NDk3MzY1ODM2NzhdLCBbLTY2Ljc0MDMzNDAzMzY1OTgsIDQ1Ljk2NTMxMDg0MjYwMjNdLCBbLTY2Ljc0MTgxNjI1Mzg3ODYsIDQ1Ljk2NTQ5ODE2NjI5MDJdLCBbLTY2Ljc0MzMxNjQ0MDQwMzEsIDQ1Ljk2NTUxMDY1NDUxMzVdLCBbLTY2Ljc0NTIxMTg4NTY1MjYsIDQ1Ljk2NTEzNjAwNjU4ODddLCBbLTY2Ljc0NDY3Mjg5NjQ4MjEsIDQ1Ljk2NDU0OTA1MzA3OTFdLCBbLTY2Ljc0NDczNTc3ODU1MiwgNDUuOTYzNTYyNDU3NjM2NF0sIFstNjYuNzQ0ODUyNTU5NTM5LCA0NS45NjMyMzE1MDcxMjg0XSwgWy02Ni43NDUzNDY2MzI5NDUyLCA0NS45NjI3Njk0MjE5Nzk5XSwgWy02Ni43NDU2MDcxNDQzNzc2LCA0NS45NjIyODg1OTk1NTgxXSwgWy02Ni43NDU1NTMyNDU0NjA2LCA0NS45NjIxMTk5OTg0OTk5XSwgWy02Ni43NDUwNzcxMzgzNiwgNDUuOTYxOTA3Njg1MzI2NV0sIFstNjYuNzQ1MTkzOTE5MzQ2OSwgNDUuOTYxMzI2OTQyMTk1Nl0sIFstNjYuNzQ1MDQxMjA1NzQ4NiwgNDUuOTYxMDE0NzEyMTg5N10sIFstNjYuNzQ1NjA3MTQ0Mzc3NiwgNDUuOTYwMzM0MDQ0Njc4XSwgWy02Ni43NDU2MzQwOTM4MzYyLCA0NS45NTk4NTMyMDExMjA1XSwgWy02Ni43NDU4MTM3NTY4OTMsIDQ1Ljk1OTU5MDkyMTA1NzZdLCBbLTY2Ljc0NTAzMjIyMjU5NTgsIDQ1Ljk1ODg0Nzc4NzQ3MDRdLCBbLTY2Ljc0NDg3OTUwODk5NzUsIDQ1Ljk1ODQ2Njg0OTU4MjddLCBbLTY2LjcxMzUxMDMzOTI3NiwgNDUuOTU4NTI5Mjk4NTk2Ml1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogMjQsICJOZWlnaGJvdXJoIjogIlNwcmluZ2hpbGwiLCAiT0JKRUNUSUQiOiAyNCwgIlNoYXBlX0FyZWEiOiAxNTEwMjM0LjU2MjM0LCAiU2hhcGVfTGVuZyI6IDcyMzEuMzExNjkzNjQsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZmZmZiMiIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNzI3MTkxNjgxMDUzMiwgNDUuOTYxNzk1MjgzOTA1Ml0sIFstNjYuNzI2MTY3NjAxNjI5MywgNDUuOTY1MDc5ODA5MTgxNV0sIFstNjYuNzI2MTk0NTUxMDg3OCwgNDUuOTY1NDkxOTIyMTc3NF0sIFstNjYuNzI2NDU1MDYyNTIwMiwgNDUuOTY1ODcyODExNzY1Nl0sIFstNjYuNzI3MDEyMDE3OTk2NCwgNDUuOTY2MTg1MDE0MzkzMV0sIFstNjYuNzI3OTgyMTk4NTAzMiwgNDUuOTY2MTM1MDYyMDkwOV0sIFstNjYuNzMwMTc0MDg3Nzk2NSwgNDUuOTY1OTQxNDk2NDk0Nl0sIFstNjYuNzMxNTAzNTk0NDE2OSwgNDUuOTY1NDk4MTY2MjkwMl0sIFstNjYuNzMyMjQ5MTk2MTAyOCwgNDUuOTY0OTIzNzA0OTczM10sIFstNjYuNzMyNDkxNzQxMjI5NSwgNDUuOTY0NDQ5MTQ1NDc5M10sIFstNjYuNzMyNDY0NzkxNzcxLCA0NS45NjM4MzcyMDc0OTk1XSwgWy02Ni43MzE5OTc2Njc4MjMyLCA0NS45NjMyMTI3NzQwMjE3XSwgWy02Ni43MzE2MjAzNzU0MDM5LCA0NS45NjI5NjkyNDMwNTc2XSwgWy02Ni43MzA3MjIwNjAxMTk4LCA0NS45NjI5NzU0ODc0NTQ3XSwgWy02Ni43Mjk3OTY3OTUzNzcxLCA0NS45NjI3OTQzOTk2NTRdLCBbLTY2LjcyNzE5MTY4MTA1MzIsIDQ1Ljk2MTc5NTI4MzkwNTJdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDI1LCAiTmVpZ2hib3VyaCI6ICJOZXRoZXJ2dWUgTWluaWhvbWUgUGFyayIsICJPQkpFQ1RJRCI6IDI1LCAiU2hhcGVfQXJlYSI6IDE2NTUyMi4yNzYwNDksICJTaGFwZV9MZW5nIjogMTU5MC40NzIwMjExNywgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmVkOTc2IiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni43MzE4NjI5MjA1MzA2LCA0NS45NjUyNzMzNzc3ODg3XSwgWy02Ni43MzEwMDA1Mzc4NTc4LCA0NS45NjU3MjI5NTM4Nzk1XSwgWy02Ni43Mjk5NzY0NTg0MzQsIDQ1Ljk2NTk2NjQ3MjczODZdLCBbLTY2LjcyNzAxMjAxNzk5NjQsIDQ1Ljk2NjE4NTAxNDM5MzFdLCBbLTY2LjcyNjUyNjkyNzc0MjksIDQ1Ljk2NTkzNTI1MjQzMTldLCBbLTY2LjcyNjIzMDQ4MzY5OTIsIDQ1Ljk2NTU3MzA5NTU4OF0sIFstNjYuNzI2MTU4NjE4NDc2NCwgNDUuOTY1MTYwOTgzMTk1OV0sIFstNjYuNzI3MTkxNjgxMDUzMiwgNDUuOTYxNzk1MjgzOTA1Ml0sIFstNjYuNzI0NjQwNDY1NjQ2MywgNDUuOTYxNTg5MjE0MDQwN10sIFstNjYuNzIzMTIyMzEyODE2MSwgNDUuOTYxNTcwNDgwMzc4N10sIFstNjYuNzIxNjEzMTQzMTM4OCwgNDUuOTYxNzAxNjE1ODhdLCBbLTY2LjcxOTU0NzAxNzk4NTMsIDQ1Ljk2MjA4MjUzMTUyODRdLCBbLTY2LjcxNzY0MjU4OTU4MywgNDUuOTYyMjMyMzk5MjYyNF0sIFstNjYuNzE3Njk2NDg4NSwgNDUuOTYyNjA3MDY2ODIzNl0sIFstNjYuNzE3MjY1Mjk3MTYzNywgNDUuOTY0MjkzMDM5NDk0MV0sIFstNjYuNzE2MzIyMDY2MTE1MywgNDUuOTY2ODcxODUzOTc5OF0sIFstNjYuNzE1NzU2MTI3NDg2MywgNDUuOTY4MDAxOTk4NzY0NV0sIFstNjYuNzIwNzk1Njc2MjMwMywgNDUuOTY3NzY0NzMyNzEwOV0sIFstNjYuNzI1MDE3NzU4MDY1NiwgNDUuOTY3OTM5NTYwNDI3OV0sIFstNjYuNzI4MTUyODc4NDA3MiwgNDUuOTY4MjE0Mjg4NTgyNl0sIFstNjYuNzMxMzY4ODQ3MTI0MywgNDUuOTY3ODk1ODUzNTUwNF0sIFstNjYuNzMxODYyOTIwNTMwNiwgNDUuOTY1MjczMzc3Nzg4N11dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogMjYsICJOZWlnaGJvdXJoIjogIk1vbnRlaXRoIC8gVGFsaXNtYW4iLCAiT0JKRUNUSUQiOiAyNiwgIlNoYXBlX0FyZWEiOiA1OTM1NDcuNTEzOTQsICJTaGFwZV9MZW5nIjogMzg1MS4zMjAzMTQzMiwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmVkOTc2IiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni43MTc2NDI1ODk1ODMsIDQ1Ljk2MjIzMjM5OTI2MjRdLCBbLTY2LjcxMjE0NDkwMDA0NDIsIDQ1Ljk2MzAzMTY4Njk5NjZdLCBbLTY2LjcwOTgwOTI4MDMwNTUsIDQ1Ljk2NDA0OTUxMzI3ODddLCBbLTY2LjcwOTA1NDY5NTQ2NjgsIDQ1Ljk2NDE2MTkxMDEyNjVdLCBbLTY2LjcwNzkxMzgzNTA1NiwgNDUuOTY0MTE4MjAwMjY4M10sIFstNjYuNzA1NTY5MjMyMTY0NCwgNDUuOTYzNTA2MjU4NjMyOV0sIFstNjYuNzAzNzQ1NjUyMTM3NywgNDUuOTYzMzE4OTI4MjA5NV0sIFstNjYuNzAyOTgyMDg0MTQ2MiwgNDUuOTYzNzE4NTY1NjgwM10sIFstNjYuNzAxOTY2OTg3ODc1MSwgNDUuOTY1MDExMTIzMzg0MV0sIFstNjYuNzAxNDQ1OTY1MDEwMywgNDUuOTY2MjQ3NDU0NzA3NF0sIFstNjYuNzAxMjg0MjY4MjU5MiwgNDUuOTY3MzIxNDE3MDk3OV0sIFstNjYuNzAyMzYyMjQ2NjAwMSwgNDUuOTY3MjY1MjIxOTA3N10sIFstNjYuNzAyNTc3ODQyMjY4MywgNDUuOTY3MzkwMTAwMDMwOF0sIFstNjYuNzAzMjA2NjYyOTY3MiwgNDUuOTY3MzU4ODgwNTI2NF0sIFstNjYuNzAzNzI3Njg1ODMyLCA0NS45Njc0OTAwMDIzMjY2XSwgWy02Ni43MDY2MjAyNjEwNDY4LCA0NS45Njc1NDYxOTcyODg4XSwgWy02Ni43MDc2NzEyODk5MjkzLCA0NS45Njc3NTg0ODg4NTM3XSwgWy02Ni43MDkwMDk3Nzk3MDI2LCA0NS45Njc4MzM0MTUwOTQxXSwgWy02Ni43MTAwNjk3OTE3Mzc5LCA0NS45Njc4NzcxMjIwMjA5XSwgWy02Ni43MTExODM3MDI2OTAyLCA0NS45Njc3ODM0NjQyNzg0XSwgWy02Ni43MTQ2OTYxMTU0NTExLCA0NS45NjgwMjA3MzAyNTE4XSwgWy02Ni43MTU3NTYxMjc0ODYzLCA0NS45NjgwMDE5OTg3NjQ1XSwgWy02Ni43MTYzMjIwNjYxMTUzLCA0NS45NjY4NzE4NTM5Nzk4XSwgWy02Ni43MTcyNjUyOTcxNjM3LCA0NS45NjQyOTMwMzk0OTQxXSwgWy02Ni43MTc2OTY0ODg1LCA0NS45NjI2MDcwNjY4MjM2XSwgWy02Ni43MTc2NDI1ODk1ODMsIDQ1Ljk2MjIzMjM5OTI2MjRdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDI3LCAiTmVpZ2hib3VyaCI6ICJHYXJkZW4gQ3JlZWsiLCAiT0JKRUNUSUQiOiAyNywgIlNoYXBlX0FyZWEiOiA1NjU2NTUuNTQxNDg0LCAiU2hhcGVfTGVuZyI6IDM0NDIuNDY5NjcxNjUsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlZDk3NiIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjk4ODQ5ODMzODM5MiwgNDUuOTU2MjY4NTk5NDY1XSwgWy02Ni43MDA0NzU3ODQ1MDM1LCA0NS45NTY3NjE5NjQzMjU0XSwgWy02Ni43MDE4NDEyMjM3MzUzLCA0NS45NTc1NDI1OTU5NTM1XSwgWy02Ni43MDE4MTQyNzQyNzY4LCA0NS45NTg4NDc3ODc0NzA0XSwgWy02Ni43MDExNjc0ODcyNzIyLCA0NS45NjAzMzQwNDQ2NzhdLCBbLTY2LjcwMTE2NzQ4NzI3MjIsIDQ1Ljk2MDgyMTEyODcwMjRdLCBbLTY2LjcwMTY1MjU3NzUyNTcsIDQ1Ljk2MTM3Njg5ODgzMzJdLCBbLTY2LjcwMjg5MjI1MjYxNzcsIDQ1Ljk2MTE2NDU4MjgxMjFdLCBbLTY2LjcwMzUzMDA1NjQ2OTUsIDQ1Ljk2MDc3MTE3MTU2MzddLCBbLTY2LjcwNzA1MTQ1MjM4MzIsIDQ1Ljk1NzMyNDAyMDIwNjJdLCBbLTY2LjcwODQzNDg1NzkyMDgsIDQ1Ljk1NTQ4Nzk0OTg4OTNdLCBbLTY2LjcwOTAwMDc5NjU0OTgsIDQ1Ljk1NDI1MTM3ODQ1NTRdLCBbLTY2LjcwOTMyNDE5MDA1MiwgNDUuOTUyOTc3MzA2MzAwMl0sIFstNjYuNzA5Mzk2MDU1Mjc0OCwgNDUuOTUxNjc4MjIyMTgwNl0sIFstNjYuNzA5MTYyNDkzMzAwOSwgNDUuOTUwMTM1NTIwMjM4OF0sIFstNjYuNzA4NjQxNDcwNDM2MSwgNDUuOTUwMDY2ODE1OTE0OF0sIFstNjYuNzA1MzUzNjM2NDk2MiwgNDUuOTUwMzg1MzUzNDI2N10sIFstNjYuNzAxMTY3NDg3MjcyMiwgNDUuOTUwNTk3NzEwNzUwOV0sIFstNjYuNzAwMTM0NDI0Njk1NSwgNDUuOTUwODAzODIxNDkzNF0sIFstNjYuNjk5MTczMjI3MzQxNSwgNDUuOTUxMTUzNTgzNDIzN10sIFstNjYuNjk4NDkwNTA3NzI1NiwgNDUuOTUyNDMzOTQzMDg5NF0sIFstNjYuNjk3Mjc3NzgyMDkyLCA0NS45NTU4NTY0MTc4NTk0XSwgWy02Ni42OTgwNTkzMTYzODkyLCA0NS45NTYyMDYxNDc5MDM2XSwgWy02Ni42OTg4NDk4MzM4MzkyLCA0NS45NTYyNjg1OTk0NjVdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDI4LCAiTmVpZ2hib3VyaCI6ICJIaWdocG9pbnQgUmlkZ2UiLCAiT0JKRUNUSUQiOiAyOCwgIlNoYXBlX0FyZWEiOiA3MjQyNDcuODk3MjcsICJTaGFwZV9MZW5nIjogMzY2OC43MTMxMzE2MSwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmVkOTc2IiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni43MTEwOTM4NzExNjE4LCA0NS45MzQyMDYzMzAyODgyXSwgWy02Ni43MDg3MTMzMzU2NTg4LCA0NS45MzUwNDM1MDc1MzQ1XSwgWy02Ni43MDc1OTA0NDE1NTM3LCA0NS45MzU1NzQ1NDYyNTE3XSwgWy02Ni43MDY3NjM5OTE0OTIzLCA0NS45MzYxMjQzMjIxNTQyXSwgWy02Ni43MDU2OTQ5OTYzMDQyLCA0NS45Mzc0MDUwMjg5NzFdLCBbLTY2LjcwNTE5MTkzOTc0NTEsIDQ1LjkzODg1NDM3ODU2NzZdLCBbLTY2LjcwOTEwODU5NDM4MzgsIDQ1LjkzOTgzNTE2NjkzMTNdLCBbLTY2LjcxMTA5Mzg3MTE2MTgsIDQ1LjkzNDIwNjMzMDI4ODJdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDI5LCAiTmVpZ2hib3VyaCI6ICJHcmVlbndvb2QgTWluaWhvbWUgUGFyayIsICJPQkpFQ1RJRCI6IDI5LCAiU2hhcGVfQXJlYSI6IDE1MjUzOS40ODc5NjUsICJTaGFwZV9MZW5nIjogMTY5OS42NDcxNjEyMiwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmZmZmIyIiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni43MDM4NzE0MTYyNzc0LCA0NS45NjMyODc3MDY0MTA2XSwgWy02Ni43MDI5ODIwODQxNDYyLCA0NS45NjI2MzIwNDQ1NzA5XSwgWy02Ni43MDE3MTU0NTk1OTU1LCA0NS45NjE5MjY0MTg4NzQ1XSwgWy02Ni43MDAzMTQwODc3NTIzLCA0NS45NjEzNTgxNjUwOTk0XSwgWy02Ni42OTkwOTIzNzg5NjU5LCA0NS45NjEwMDg0Njc1NzE3XSwgWy02Ni42OTcwMjYyNTM4MTI0LCA0NS45NjA2NDYyNzg1MTk3XSwgWy02Ni42OTQ4OTcyNDY1ODkxLCA0NS45NjA1MDI2NTExNzFdLCBbLTY2LjY4ODg3ODUzNDE4NTUsIDQ1Ljk1OTc3MjAxOTMyODldLCBbLTY2LjY4NzY4Mzc3NDg1NzYsIDQ1Ljk2MDAxNTU2NDM0NjhdLCBbLTY2LjY4NjY4NjY0NDg5MjIsIDQ1Ljk2MDUzMzg3NDUzOTRdLCBbLTY2LjY4NTQxMTAzNzE4ODgsIDQ1Ljk2MDU1ODg1MzIyMTRdLCBbLTY2LjY4NDY4MzQwMTgwODYsIDQ1Ljk2MDIxNTM5NTM1NjhdLCBbLTY2LjY4MzgyMTAxOTEzNTksIDQ1Ljk2MDEwMjk5MDUwMjRdLCBbLTY2LjY3ODAyNjg4NTU1MzMsIDQ1Ljk2MDUxNTE0MDUyMDVdLCBbLTY2LjY3Njk0ODkwNzIxMjQsIDQ1Ljk2MDc4OTkwNTQ5Nl0sIFstNjYuNjc2MTY3MzcyOTE1MiwgNDUuOTYxMTI3MTE1MTk0NV0sIFstNjYuNjc1MzMxOTM5NzAxLCA0NS45NjE2NzY2Mzc3MTMyXSwgWy02Ni42NzQ3OTI5NTA1MzA1LCA0NS45NjIxOTQ5MzIzNjY5XSwgWy02Ni42NzYzMjAwODY1MTM1LCA0NS45NjI2NTcwMjIzMDddLCBbLTY2LjY3OTE2Nzc0NTk2NDIsIDQ1Ljk2Mjg4MTgyMTQyNDhdLCBbLTY2LjY4NzcwMTc0MTE2MzMsIDQ1Ljk2Mjc3NTY2NjM5OTVdLCBbLTY2LjY5MjMwMTExNTQxOCwgNDUuOTYyOTg3OTc2MjQ2N10sIFstNjYuNjk3MDA4Mjg3NTA2OCwgNDUuOTYzNDM3NTcwODg0NV0sIFstNjYuNjk4MjI5OTk2MjkzMiwgNDUuOTYzNDUwMDU5NTcyM10sIFstNjYuNjk5NzM5MTY1OTcwNSwgNDUuOTYzMzAwMTk1MTMyM10sIFstNjYuNzAxMzkyMDY2MDkzMywgNDUuOTYzNjc0ODU1NDcyM10sIFstNjYuNzAyNjQwNzI0MzM4MiwgNDUuOTY0MjM2ODQxMjMxN10sIFstNjYuNzAzMDcxOTE1Njc0NiwgNDUuOTYzNjQzNjMzODc0MV0sIFstNjYuNzAzODcxNDE2Mjc3NCwgNDUuOTYzMjg3NzA2NDEwNl1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogMzAsICJOZWlnaGJvdXJoIjogIkdvbGYgQ2x1YiIsICJPQkpFQ1RJRCI6IDMwLCAiU2hhcGVfQXJlYSI6IDU5NzU3NC42OTMwMSwgIlNoYXBlX0xlbmciOiA0ODE0Ljg1OTU5NTcxLCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjY4NzY1NjgyNTM5OTEsIDQ1Ljk2MDAyODA1MzgwNjFdLCBbLTY2LjY4ODE2ODg2NTExMSwgNDUuOTU5Mzc4NTk4MTkyNV0sIFstNjYuNjg5NjMzMTE5MDI0MSwgNDUuOTU2NTM3MTQwMzc2OF0sIFstNjYuNjkwNTMxNDM0MzA4MywgNDUuOTU1Mzk0MjcxMjAxM10sIFstNjYuNjkxMDYxNDQwMzI1OSwgNDUuOTU1MDY5NTE3MTg5OF0sIFstNjYuNjkxODUxOTU3Nzc1OSwgNDUuOTU0Nzk0NzIzODQ3NV0sIFstNjYuNjkyNDgwNzc4NDc0OCwgNDUuOTU1MDAwODE4OTgyXSwgWy02Ni42OTMxNDU1MzE3ODUsIDQ1Ljk1NDg4MjE1ODI0MDZdLCBbLTY2LjY5MzUyMjgyNDIwNDQsIDQ1Ljk1NDU1NzQwMTIyODFdLCBbLTY2LjY5MzcxMTQ3MDQxNCwgNDUuOTU0MDE0MDUzNTA5MV0sIFstNjYuNjkzNjM5NjA1MTkxMywgNDUuOTUzMzU4MjgxOTI2Ml0sIFstNjYuNjkzMTAwNjE2MDIwOCwgNDUuOTUyODIxMTY3OTkyXSwgWy02Ni42OTE2OTkyNDQxNzc2LCA0NS45NTIyNTkwNjY0NDAxXSwgWy02Ni42OTAxODEwOTEzNDc1LCA0NS45NTE5MDMwNjU4NDE5XSwgWy02Ni42ODgwNDMxMDA5NzEyLCA0NS45NTE3OTY4ODk3ODIyXSwgWy02Ni42ODc1ODQ5NjAxNzYzLCA0NS45NTIxMjc5MDg1OTFdLCBbLTY2LjY4NjU3ODg0NzA1ODEsIDQ1Ljk1MzAzOTc2MTUwMDRdLCBbLTY2LjY4NTkzMjA2MDA1MzYsIDQ1Ljk1MzgzOTE4MTg0NTddLCBbLTY2LjY4NTQyMDAyMDM0MTYsIDQ1Ljk1NDY5NDc5ODY1NzldLCBbLTY2LjY4NDk4ODgyOTAwNTIsIDQ1Ljk1NTgxMjcwMTQ0ODddLCBbLTY2LjY4NDcxOTMzNDQyLCA0NS45NTcwMDU1MjI1NzM3XSwgWy02Ni42ODQ3MDEzNjgxMTQzLCA0NS45NTgyMDQ1NjI5NTczXSwgWy02Ni42ODQ5MzQ5MzAwODgyLCA0NS45NTkzOTczMzI1OTU3XSwgWy02Ni42ODU0MTEwMzcxODg4LCA0NS45NjA1NTg4NTMyMjE0XSwgWy02Ni42ODY2ODY2NDQ4OTIyLCA0NS45NjA1MzM4NzQ1Mzk0XSwgWy02Ni42ODc2NTY4MjUzOTkxLCA0NS45NjAwMjgwNTM4MDYxXV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiAzMSwgIk5laWdoYm91cmgiOiAiS2VsbHkncyBDb3VydCBNaW5paG9tZSBQYXJrIiwgIk9CSkVDVElEIjogMzEsICJTaGFwZV9BcmVhIjogMzc1NjYwLjIwNzMzNSwgIlNoYXBlX0xlbmciOiAyNzEzLjA5MjcwMzUzLCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZmZmYjIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjY3MzY4ODAyMjczMSwgNDUuOTY0MjExODY0MjA3OV0sIFstNjYuNjc3ODc0MTcxOTU1LCA0NS45NjQ4ODYyMzk4OTc5XSwgWy02Ni42NzgzNzcyMjg1MTQxLCA0NS45NjUxMDQ3ODU4MTRdLCBbLTY2LjY3OTMyMDQ1OTU2MjQsIDQ1Ljk2NTEyMzUxODI4MDldLCBbLTY2LjY4MzI5OTk5NjI3MTEsIDQ1Ljk2NTcyMjk1Mzg3OTVdLCBbLTY2LjY4MzQxNjc3NzI1OCwgNDUuOTY1NjQxNzgwNjg4Nl0sIFstNjYuNjg0NjQ3NDY5MTk3MywgNDUuOTY1OTA0MDMyMTA3Nl0sIFstNjYuNjg1MDMzNzQ0NzY5NSwgNDUuOTY1OTIyNzY0MzA0M10sIFstNjYuNjg1MjQwMzU3Mjg0OCwgNDUuOTY1ODIyODU5MTgyXSwgWy02Ni42ODUzMzkxNzE5NjYsIDQ1Ljk2NjAxMDE4MTEzODVdLCBbLTY2LjY4NjcwNDYxMTE5NzksIDQ1Ljk2NjA0MTQwMTQwM10sIFstNjYuNjg3MzQyNDE1MDQ5NiwgNDUuOTY2MzY2MDkxMTEwN10sIFstNjYuNjg5NTUyMjcwNjQ4NiwgNDUuOTY2NzE1NzU0ODIxNV0sIFstNjYuNjk0NDY2MDU1MjUyNywgNDUuOTY2ODQ2ODc4MTQ0XSwgWy02Ni43MDA4NjIwNjAwNzU2LCA0NS45NjczNzEzNjgzMzAzXSwgWy02Ni43MDEyODQyNjgyNTkyLCA0NS45NjczMjE0MTcwOTc5XSwgWy02Ni43MDE0MDEwNDkyNDYxLCA0NS45NjY0MjIyODcyMTMxXSwgWy02Ni43MDE4MTQyNzQyNzY4LCA0NS45NjUyOTIxMTAxOTg2XSwgWy02Ni43MDI2NDA3MjQzMzgyLCA0NS45NjQyMzY4NDEyMzE3XSwgWy02Ni43MDEzOTIwNjYwOTMzLCA0NS45NjM2NzQ4NTU0NzIzXSwgWy02Ni42OTk3MzkxNjU5NzA1LCA0NS45NjMzMDAxOTUxMzIzXSwgWy02Ni42OTgyMjk5OTYyOTMyLCA0NS45NjM0NTAwNTk1NzIzXSwgWy02Ni42OTcwMDgyODc1MDY4LCA0NS45NjM0Mzc1NzA4ODQ1XSwgWy02Ni42OTIzMDExMTU0MTgsIDQ1Ljk2Mjk4Nzk3NjI0NjddLCBbLTY2LjY4NzcwMTc0MTE2MzMsIDQ1Ljk2Mjc3NTY2NjM5OTVdLCBbLTY2LjY3OTE2Nzc0NTk2NDIsIDQ1Ljk2Mjg4MTgyMTQyNDhdLCBbLTY2LjY3NjMyMDA4NjUxMzUsIDQ1Ljk2MjY1NzAyMjMwN10sIFstNjYuNjc0NzkyOTUwNTMwNSwgNDUuOTYyMjAxMTc2ODUxMl0sIFstNjYuNjczNjg4MDIyNzMxLCA0NS45NjQyMTE4NjQyMDc5XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiAzMiwgIk5laWdoYm91cmgiOiAiV29vZHN0b2NrIFJvYWQiLCAiT0JKRUNUSUQiOiAzMiwgIlNoYXBlX0FyZWEiOiA3NTgzMzYuODM4Nzg3LCAiU2hhcGVfTGVuZyI6IDUwNDguNDM3NDkwMDMsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZkOGQzYyIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjY5NTQ2Nzg5MjcxMiwgNDUuOTYxNjM5MTcwNDQxOV0sIFstNjYuNjY4NTg1NTkxOTE3MiwgNDUuOTYwNzI3NDU5MDMwM10sIFstNjYuNjY3MDc2NDIyMjM5OSwgNDUuOTU5OTg0MzQwNjg2NF0sIFstNjYuNjYzODk2Mzg2MTM0MSwgNDUuOTU5MTQxMjk1MjA0MV0sIFstNjYuNjYxNjE0NjY1MzEyNSwgNDUuOTU4OTE2NDgwOTA5MV0sIFstNjYuNjU5MTQ0Mjk4MjgxMSwgNDUuOTYyNDM4NDY2NzM0Nl0sIFstNjYuNjU4ODExOTIxNjI2LCA0NS45NjMyNTY0ODQ1OTQyXSwgWy02Ni42NTg3MzEwNzMyNTA0LCA0NS45NjQwOTk0Njc0NjE0XSwgWy02Ni42NjAwNTE1OTY3MTgxLCA0NS45NjQwODA3MzQ2NDgyXSwgWy02Ni42NjE4MzkyNDQxMzM1LCA0NS45NjM3ODcyNTMwODAzXSwgWy02Ni42Njc4MTMwNDA3NzI5LCA0NS45NjIyNDQ4ODgyMjE5XSwgWy02Ni42Njk1NDY3ODkyNzEyLCA0NS45NjE2MzkxNzA0NDE5XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiAzMywgIk5laWdoYm91cmgiOiAiU3Vuc2hpbmUgR2FyZGVucyIsICJPQkpFQ1RJRCI6IDMzLCAiU2hhcGVfQXJlYSI6IDI4NjUzOS4xOTYyNzIsICJTaGFwZV9MZW5nIjogMjIzMS4wMzIwMDMxMywgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmVkOTc2IiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni42MzIxMjI5NzQ1MzQ4LCA0NS45NTQ5MDA4OTQxNjRdLCBbLTY2LjYzMjU1NDE2NTg3MTIsIDQ1Ljk1NjU0OTYzMDYyMDFdLCBbLTY2LjYzMzcwNDAwOTQzNDksIDQ1Ljk1ODU2Njc2Nzk3MDVdLCBbLTY2LjYzNDc1NTAzODMxNzMsIDQ1Ljk1OTU2NTk0MTkzOTJdLCBbLTY2LjYzNjI2NDIwNzk5NDYsIDQ1Ljk2MTM4MzE0MzQwOThdLCBbLTY2LjYzNzg3MjE5MjM1MzIsIDQ1Ljk2Mjc0NDQ0NDI5NDVdLCBbLTY2LjY0MDQyMzQwNzc2MDEsIDQ1Ljk2NDM4MDQ1ODldLCBbLTY2LjY0MjM1NDc4NTYyMDksIDQ1Ljk2NTM5ODI2MDQwMjFdLCBbLTY2LjY0NDUxOTcyNTQ1NTcsIDQ1Ljk2NjEwMzg0MTg3OTJdLCBbLTY2LjY0NzQwMzMxNzUxNzcsIDQ1Ljk2NjUzNDY3OTI0NjhdLCBbLTY2LjY1MDQyMTY1Njg3MjMsIDQ1Ljk2NjQwOTc5OTE5NTNdLCBbLTY2LjY1MzU5MjcwOTgyNTMsIDQ1Ljk2NjEwMzg0MTg3OTJdLCBbLTY2LjY1NjQwNDQzNjY2NDYsIDQ1Ljk2NjQ3ODQ4MzI1ODVdLCBbLTY2LjY1NzczMzk0MzI4NTEsIDQ1Ljk2NjUwMzQ1OTI2MDRdLCBbLTY2LjY1NjI1MTcyMzA2NjMsIDQ1Ljk2NTkyOTAwODM2ODRdLCBbLTY2LjY1NDY3MDY4ODE2NjIsIDQ1Ljk2NTUwNDQxMDQwMjJdLCBbLTY2LjY1MzAxNzc4ODA0MzQsIDQ1Ljk2NTI0MjE1NzA5MTNdLCBbLTY2LjY1MjAwMjY5MTc3MjQsIDQ1Ljk2NTI3OTYyMTkyNl0sIFstNjYuNjUxMTg1MjI0ODYzOCwgNDUuOTY1MDYxMDc2Njk5N10sIFstNjYuNjUwNDg0NTM4OTQyMiwgNDUuOTY0NTU1Mjk3Mjk4MV0sIFstNjYuNjUwNDg0NTM4OTQyMiwgNDUuOTY0MjkzMDM5NDk0MV0sIFstNjYuNjUwOTk2NTc4NjU0MiwgNDUuOTYzNzY4NTIwMTYxNV0sIFstNjYuNjUxOTM5ODA5NzAyNSwgNDUuOTYzNDYyNTQ4MjU3NF0sIFstNjYuNjMyMTIyOTc0NTM0OCwgNDUuOTU0OTAwODk0MTY0XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiAzNCwgIk5laWdoYm91cmgiOiAiRG93bnRvd24iLCAiT0JKRUNUSUQiOiAzNCwgIlNoYXBlX0FyZWEiOiA4MTkyMzYuNzA1Njk3LCAiU2hhcGVfTGVuZyI6IDUzMDAuNzQwMzExMjIsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZkOGQzYyIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjM0MTM1MjAwNzcxMiwgNDUuOTU1NzY4OTg1MDAzNF0sIFstNjYuNjUxOTM5ODA5NzAyNSwgNDUuOTYzNDYyNTQ4MjU3NF0sIFstNjYuNjU0MTU4NjQ4NDU0MywgNDUuOTYzNTgxMTkwNjI0OV0sIFstNjYuNjU2ODM1NjI4MDAwOSwgNDUuOTYzOTk5NTU5MDUwOV0sIFstNjYuNjU4ODI5ODg3OTMxNywgNDUuOTY0MTU1NjY1ODYzMV0sIFstNjYuNjU4NzMxMDczMjUwNCwgNDUuOTY0MDk5NDY3NDYxNF0sIFstNjYuNjU4Nzc1OTg5MDE0NiwgNDUuOTYzNDI1MDgyMTkzOF0sIFstNjYuNjU5MTQ0Mjk4MjgxMSwgNDUuOTYyNDM4NDY2NzM0Nl0sIFstNjYuNjYwNzUyMjgyNjM5NywgNDUuOTU5OTk2ODMwMTUyN10sIFstNjYuNjYxNjc3NTQ3MzgyMywgNDUuOTU4OTE2NDgwOTA5MV0sIFstNjYuNjYxMzA5MjM4MTE1OCwgNDUuOTU4MDg1OTA5MDc2MV0sIFstNjYuNjYwNDAxOTM5Njc4OSwgNDUuOTU3NDczOTAwODExNV0sIFstNjYuNjU2OTYxMzkyMTQwNywgNDUuOTU2ODc0Mzc1OTU3Nl0sIFstNjYuNjU1MjgxNTQyNTU5NCwgNDUuOTU2MzE4NTYwNjYzNF0sIFstNjYuNjUzMjY5MzE2MzIzLCA0NS45NTU1MDY2ODU2MDhdLCBbLTY2LjY1MDQ2NjU3MjYzNjUsIDQ1Ljk1NDE3NjQzMzg0NTNdLCBbLTY2LjY0OTEwMTEzMzQwNDcsIDQ1Ljk1MzY3NjgwMDUyMTNdLCBbLTY2LjY0NzMwNDUwMjgzNjQsIDQ1Ljk1MzE5NTg5OTE5MjddLCBbLTY2LjY0MjkxMTc0MTA5NzEsIDQ1Ljk1MTQ3MjExNDY4OThdLCBbLTY2LjY0MTg3ODY3ODUyMDMsIDQ1Ljk1MDc3ODgzODQxMzldLCBbLTY2LjY0MDcwMTg4NTQ5ODEsIDQ1Ljk1MDQ4NTI4NjM4NjVdLCBbLTY2LjYzOTQ1MzIyNzI1MzIsIDQ1Ljk1MDUyOTAwNjk5OTddLCBbLTY2LjYzODQyOTE0NzgyOTMsIDQ1Ljk1MTIzNDc3Nzg0MThdLCBbLTY2LjYzNzU5MzcxNDYxNTEsIDQ1Ljk1MjA1Mjk2MTEwOTNdLCBbLTY2LjYzNjUzMzcwMjU3OTgsIDQ1Ljk1MzQ4OTQzNjg2MzVdLCBbLTY2LjYzNDEzNTIwMDc3MTIsIDQ1Ljk1NTc2ODk4NTAwMzRdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDM1LCAiTmVpZ2hib3VyaCI6ICJQbGF0IiwgIk9CSkVDVElEIjogMzUsICJTaGFwZV9BcmVhIjogMTU5NjQwMS40MjUzNiwgIlNoYXBlX0xlbmciOiA1NTUxLjM4MTAwMzAxLCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNiZDAwMjYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjYyODk2MDkwNDczNDcsIDQ1LjkzOTUxNjU2ODc5MjFdLCBbLTY2LjYyODk4Nzg1NDE5MzIsIDQ1Ljk0MDI1MzcxNDY0NTddLCBbLTY2LjYyOTEzMTU4NDYzODcsIDQ1Ljk0MDM5NzM5NDQ3NThdLCBbLTY2LjYyOTYwNzY5MTczOTMsIDQ1Ljk0MDUwMzU5MjM3MTldLCBbLTY2LjYzMDA5Mjc4MTk5MjcsIDQ1Ljk0MjAyNzgyMjExNTZdLCBbLTY2LjYzMDc2NjUxODQ1NTgsIDQ1Ljk0MzA5NjAwNzMzMV0sIFstNjYuNjMxMjMzNjQyNDAzNSwgNDUuOTQ0NzU3NTg3ODY5N10sIFstNjYuNjMxNjU1ODUwNTg3MSwgNDUuOTQ3NjU1ODY0Nzk2Nl0sIFstNjYuNjMxNzYzNjQ4NDIxMiwgNDUuOTQ4MDI0Mzg0ODM5OV0sIFstNjYuNjMxODM1NTEzNjQzOSwgNDUuOTQ4MTExODI5OTE0Ml0sIFstNjYuNjMxOTYxMjc3NzgzNywgNDUuOTQ3OTY4MTcwMDc2NF0sIFstNjYuNjMyMDk2MDI1MDc2MywgNDUuOTQ4Mzg2NjU2MzkyN10sIFstNjYuNjMyMTA1MDA4MjI5MSwgNDUuOTUwNjE2NDQ4MTIyOF0sIFstNjYuNjMxOTA3Mzc4ODY2NiwgNDUuOTUxNTE1ODM0NTI0Nl0sIFstNjYuNjMxOTcwMjYwOTM2NSwgNDUuOTU0MjA3NjYwNzc4NV0sIFstNjYuNjMyMTIyOTc0NTM0OCwgNDUuOTU0OTAwODk0MTY0XSwgWy02Ni42MzQxMzUyMDA3NzEyLCA0NS45NTU3Njg5ODUwMDM0XSwgWy02Ni42MzY4NTcwOTYwODIxLCA0NS45NTMxNDU5MzUxNzldLCBbLTY2LjYzNzg5OTE0MTgxMTcsIDQ1Ljk1MTcxNTY5NjE4NzVdLCBbLTY2LjYzODgxNTQyMzQwMTUsIDQ1Ljk1MDk0MTIyODIyOTJdLCBbLTY2LjYzOTYxNDkyNDAwNDQsIDQ1Ljk1MDQ5Nzc3Nzk5MzhdLCBbLTY2LjYzOTU3MDAwODI0MDIsIDQ1Ljk1MDMwNDE1Nzc2NDFdLCBbLTY2LjYzOTMxODQ3OTk2MDYsIDQ1Ljk0OTgzNTcxODkyN10sIFstNjYuNjM4MDc4ODA0ODY4NSwgNDUuOTQ4ODYxMzUzNDY0MV0sIFstNjYuNjM2NzEzMzY1NjM2NywgNDUuOTQ3NTQ5NjgwNjAwNl0sIFstNjYuNjM0OTYxNjUwODMyNiwgNDUuOTQ1MjU3MzAxNTk5XSwgWy02Ni42MzQwNjMzMzU1NDg1LCA0NS45NDQyOTUzNDg2NTk3XSwgWy02Ni42MzMzNzE2MzI3Nzk3LCA0NS45NDMyNDU5MjY0MTZdLCBbLTY2LjYzMjY2MTk2MzcwNTMsIDQ1Ljk0MTQxNTYzNjUxNl0sIFstNjYuNjMyMjEyODA2MDYzMiwgNDUuOTQwNzg0NzAzNDY3OF0sIFstNjYuNjMxNzAwNzY2MzUxMywgNDUuOTQwMzQxMTcxOTc3OV0sIFstNjYuNjMwOTAxMjY1NzQ4NCwgNDUuOTM5OTEwMTMwOTMzM10sIFstNjYuNjI5OTY3MDE3ODUyOSwgNDUuOTM5NjI5MDE1NDAzMl0sIFstNjYuNjI4OTYwOTA0NzM0NywgNDUuOTM5NTE2NTY4NzkyMV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogMzYsICJOZWlnaGJvdXJoIjogIldhdGVybG9vIFJvdyIsICJPQkpFQ1RJRCI6IDM2LCAiU2hhcGVfQXJlYSI6IDU4MDYzNS45MDI4MzQsICJTaGFwZV9MZW5nIjogNDI2MC40ODI0MTc2LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjY0NjQzMzEzNzAxMDgsIDQ1Ljk0MjQxNTExOTcxODFdLCBbLTY2LjY0NTc2ODM4MzcwMDYsIDQ1Ljk0MjA4NDA0MjkwMzFdLCBbLTY2LjY0NTY3ODU1MjE3MjIsIDQ1Ljk0MTg5NjY0MDA1NjFdLCBbLTY2LjY1MDE0MzE3OTEzNDIsIDQ1LjkzNjYwNTM3MTU5NzhdLCBbLTY2LjY1MDI3NzkyNjQyNjksIDQ1LjkzNjMxNzk5MTkxMjZdLCBbLTY2LjY1MDA5ODI2MzM3LCA0NS45MzYxMzY4MTY5OTc4XSwgWy02Ni42NDk2NjcwNzIwMzM3LCA0NS45MzYyMjQyODA4MjM3XSwgWy02Ni42NDc2NjM4Mjg5NTAxLCA0NS45Mzc0ODYyNDM1Mjc5XSwgWy02Ni42NDQyNzcxODAzMjg5LCA0NS45NDAwNTM4MTE2NTM4XSwgWy02Ni42NDM0NDE3NDcxMTQ3LCA0NS45NDA1NTk4MTQ3MDUxXSwgWy02Ni42NDI0MzU2MzM5OTY1LCA0NS45NDA5NjU4NjMxOTY3XSwgWy02Ni42NDEyMjI5MDgzNjI5LCA0NS45NDEyNDY5NzE5NDg5XSwgWy02Ni42NDAxMTc5ODA1NjM1LCA0NS45NDEzMjgxODA4Nzg2XSwgWy02Ni42Mzg4NjAzMzkxNjU3LCA0NS45NDEyMjgyMzE0MDk3XSwgWy02Ni42Mzc4MDkzMTAyODMzLCA0NS45NDE3OTY2OTE2MTIxXSwgWy02Ni42MzcwMjc3NzU5ODYxLCA0NS45NDI1NDYzMDA1NTA3XSwgWy02Ni42MzYxNDc0MjcwMDc3LCA0NS45NDQ1MjAyMjIyNzAzXSwgWy02Ni42MzU4Nzc5MzI0MjI0LCA0NS45NDY1ODE1MjExOTY1XSwgWy02Ni42Mzc1NzU3NDgzMDk0LCA0NS45NDg0MTE2NDA1NTA0XSwgWy02Ni42MzkzMTg0Nzk5NjA2LCA0NS45NDk4MzU3MTg5MjddLCBbLTY2LjYzOTYxNDkyNDAwNDQsIDQ1Ljk1MDQ5Nzc3Nzk5MzhdLCBbLTY2LjY0MTAwNzMxMjY5NDcsIDQ1Ljk1MDUyOTAwNjk5OTddLCBbLTY2LjY0MjExMjI0MDQ5NDIsIDQ1Ljk1MDg4NTAxNjQyMzldLCBbLTY2LjY0MjU0MzQzMTgzMDYsIDQ1Ljk1MDM4NTM1MzQyNjddLCBbLTY2LjY0NTIyOTM5NDUzMDEsIDQ1Ljk0NzAzMTI0ODk1ODNdLCBbLTY2LjY0NDEwNjUwMDQyNSwgNDUuOTQ2NTg3NzY3NDQwNF0sIFstNjYuNjQ0ODQzMTE4OTU3OSwgNDUuOTQ1NzUwNzY0NDg2Ml0sIFstNjYuNjQ1MDIyNzgyMDE0OCwgNDUuOTQ1Mjg4NTMzNTU3NV0sIFstNjYuNjQ0OTQxOTMzNjM5MiwgNDUuOTQ0NzcwMDgwNzY3OF0sIFstNjYuNjQ0NDQ3ODYwMjMyOSwgNDUuOTQzNzE0NDIwOTQzN10sIFstNjYuNjQ0NTI4NzA4NjA4NSwgNDUuOTQzNDgzMjk3NDcxNV0sIFstNjYuNjQ2NDMzMTM3MDEwOCwgNDUuOTQyNDE1MTE5NzE4MV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogMzcsICJOZWlnaGJvdXJoIjogIlVuaXZlcnNpdHkgT2YgTmV3IEJydW5zd2ljayIsICJPQkpFQ1RJRCI6IDM3LCAiU2hhcGVfQXJlYSI6IDcwNDc2My41NzEzODQsICJTaGFwZV9MZW5nIjogNDQ4MC40NjM4ODI1LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjY0NjQzMzEzNzAxMDgsIDQ1Ljk0MjQxNTExOTcxODFdLCBbLTY2LjY0NDUyODcwODYwODUsIDQ1Ljk0MzQ4MzI5NzQ3MTVdLCBbLTY2LjY0NDQ0Nzg2MDIzMjksIDQ1Ljk0MzcxNDQyMDk0MzddLCBbLTY2LjY0NDk0MTkzMzYzOTIsIDQ1Ljk0NDc3MDA4MDc2NzhdLCBbLTY2LjY0NTAyMjc4MjAxNDgsIDQ1Ljk0NTI4ODUzMzU1NzVdLCBbLTY2LjY0NDg0MzExODk1NzksIDQ1Ljk0NTc1MDc2NDQ4NjJdLCBbLTY2LjY0NDEwNjUwMDQyNSwgNDUuOTQ2NTg3NzY3NDQwNF0sIFstNjYuNjQ1MjI5Mzk0NTMwMSwgNDUuOTQ3MDMxMjQ4OTU4M10sIFstNjYuNjQ4NTE3MjI4NDcsIDQ1Ljk0MzI4OTY1MjczOTRdLCBbLTY2LjY0NjQzMzEzNzAxMDgsIDQ1Ljk0MjQxNTExOTcxODFdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDM4LCAiTmVpZ2hib3VyaCI6ICJTYWludCBUaG9tYXMgVW5pdmVyc2l0eSIsICJPQkpFQ1RJRCI6IDM4LCAiU2hhcGVfQXJlYSI6IDg0ODEzLjE1ODUzNzEsICJTaGFwZV9MZW5nIjogMTM0MS41Mzg0ODM1OSwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmVkOTc2IiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni42NDg1MTcyMjg0NywgNDUuOTQzMjg5NjUyNzM5NF0sIFstNjYuNjQ1MjI5Mzk0NTMwMSwgNDUuOTQ3MDMxMjQ4OTU4M10sIFstNjYuNjQyMTEyMjQwNDk0MiwgNDUuOTUwODg1MDE2NDIzOV0sIFstNjYuNjQyOTExNzQxMDk3MSwgNDUuOTUxNDcyMTE0Njg5OF0sIFstNjYuNjQ2MDczODEwODk3MiwgNDUuOTUyNjcxMjc0ODAyM10sIFstNjYuNjUyNjIyNTI5MzE4NCwgNDUuOTQ0OTk0OTUyNDUyOF0sIFstNjYuNjQ4NTE3MjI4NDcsIDQ1Ljk0MzI4OTY1MjczOTRdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDM5LCAiTmVpZ2hib3VyaCI6ICJDb2xsZWdlIEhpbGwiLCAiT0JKRUNUSUQiOiAzOSwgIlNoYXBlX0FyZWEiOiAzNjY3ODcuMDcyMDc5LCAiU2hhcGVfTGVuZyI6IDI3MTMuMjU2ODE0MzgsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlYjI0YyIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjUyNDUxODQ5NDE0NCwgNDUuOTQ0OTE5OTk1MzI1OF0sIFstNjYuNjUyNjIyNTI5MzE4NCwgNDUuOTQ0OTk0OTUyNDUyOF0sIFstNjYuNjQ2MDczODEwODk3MiwgNDUuOTUyNjcxMjc0ODAyM10sIFstNjYuNjQ3MzA0NTAyODM2NCwgNDUuOTUzMTk1ODk5MTkyN10sIFstNjYuNjUwMTM0MTk1OTgxNCwgNDUuOTU0MDM5MDM1MTMwM10sIFstNjYuNjU0ODY4MzE3NTI4NywgNDUuOTU2MTY4Njc2OTMzXSwgWy02Ni42NTY5NjEzOTIxNDA3LCA0NS45NTY4NzQzNzU5NTc2XSwgWy02Ni42NTc3MDY5OTM4MjY1LCA0NS45NTY5ODA1NDIyODk4XSwgWy02Ni42NTg3NDkwMzk1NTYxLCA0NS45NTY0MTg0ODI5MjUxXSwgWy02Ni42NjAyODUxNTg2OTE5LCA0NS45NTYwMDAwNTcyNTE4XSwgWy02Ni42NjU3NjQ4ODE5MjUxLCA0NS45NDk2Nzk1NzE3NjgxXSwgWy02Ni42NjY0NTY1ODQ2OTM4LCA0NS45NDkwNTQ5Nzg3MzM5XSwgWy02Ni42NjY4NTE4NDM0MTg5LCA0NS45NDg0ODY1OTI5NTYxXSwgWy02Ni42NjcxMzAzMjExNTY5LCA0NS45NDc3MTgzMjU5OTMzXSwgWy02Ni42NjcxNTcyNzA2MTU1LCA0NS45NDY5MzEzMDk3NzFdLCBbLTY2LjY2NjkyMzcwODY0MTYsIDQ1Ljk0NjE1Njc3NDk2MDNdLCBbLTY2LjY2NjU2NDM4MjUyOCwgNDUuOTQ1NTc1ODY2NzUwMl0sIFstNjYuNjYyMzQyMzAwNjkyNiwgNDUuOTQzNzgzMTMzMTQxNV0sIFstNjYuNjU3MTMyMDcyMDQ0NywgNDUuOTQxODA5MTg1MTc3NF0sIFstNjYuNjU1NTUxMDM3MTQ0NiwgNDUuOTQyNDA4ODczMDA0MV0sIFstNjYuNjU0MzgzMjI3Mjc1MywgNDUuOTQzMDY0Nzc0MTM3Ml0sIFstNjYuNjUzMjE1NDE3NDA1OSwgNDUuOTQ0MDIwNTAxODk2OV0sIFstNjYuNjUyNDUxODQ5NDE0NCwgNDUuOTQ0OTE5OTk1MzI1OF1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogNDAsICJOZWlnaGJvdXJoIjogIlRoZSBIaWxsIiwgIk9CSkVDVElEIjogNDAsICJTaGFwZV9BcmVhIjogMTYzNzE0OS41NzQwNywgIlNoYXBlX0xlbmciOiA0OTM0LjkwODE2ODE5LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWIyNGMiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjYzMDUzMjk1NjQ4MTksIDQ1LjkzOTc3MjY5Njg1MjJdLCBbLTY2LjYzMTY0Njg2NzQzNDIsIDQ1Ljk0MDMwMzY5MDI4MV0sIFstNjYuNjMyMzU2NTM2NTA4NywgNDUuOTQwOTQwODc1NjgzMV0sIFstNjYuNjMzNjIzMTYxMDU5MywgNDUuOTQzNjc2OTQxNTI3Ml0sIFstNjYuNjM1ODc3OTMyNDIyNCwgNDUuOTQ2NTgxNTIxMTk2NV0sIFstNjYuNjM2MDg0NTQ0OTM3OCwgNDUuOTQ0Nzc2MzI3MjE1OV0sIFstNjYuNjM2NzQ5Mjk4MjQ4LCA0NS45NDI5NzEwNzQ0NTA0XSwgWy02Ni42Mzc2NTY1OTY2ODUsIDQ1Ljk0MTkxNTM4MDM2OTNdLCBbLTY2LjYzODQ4MzA0Njc0NjQsIDQ1Ljk0MTM5Njg5NjAzMzldLCBbLTY2LjYzODg2MDMzOTE2NTcsIDQ1Ljk0MTIyODIzMTQwOTddLCBbLTY2LjYzOTA0MDAwMjIyMjUsIDQ1Ljk0MTI1MzIxODc5MzhdLCBbLTY2LjYzODk3NzEyMDE1MjYsIDQ1Ljk0MTEzNDUyODYxOV0sIFstNjYuNjM4MzU3MjgyNjA2NiwgNDUuOTQwMzcyNDA2NzA2XSwgWy02Ni42MzU3NTIxNjgyODI3LCA0NS45Mzk0OTE1ODA2MjUzXSwgWy02Ni42MzUwODc0MTQ5NzI0LCA0NS45Mzg1ODU3NTE5NzY2XSwgWy02Ni42MzQzMzI4MzAxMzM3LCA0NS45MzY0NDkxODcxNzExXSwgWy02Ni42MzMzMzU3MDAxNjg0LCA0NS45MzUxMTg0NzgwMTQ2XSwgWy02Ni42Mjk5NzYwMDEwMDU4LCA0NS45MzIzMTk1MTEzNTAyXSwgWy02Ni42Mjc5Mjc4NDIxNTgsIDQ1LjkzMDIzODkzNzkwNzJdLCBbLTY2LjYyNzY3NjMxMzg3ODQsIDQ1LjkzMDEwMTQ3OTg1NjFdLCBbLTY2LjYyNzI4MTA1NTE1MzQsIDQ1LjkzMDA3NjQ4NzQ0NjZdLCBbLTY2LjYyNjgwNDk0ODA1MjgsIDQ1LjkzMDM1MTQwMzMzMTldLCBbLTY2LjYyNjg0MDg4MDY2NDIsIDQ1LjkzMDczMjUzNDQ2NDNdLCBbLTY2LjYyNzQwNjgxOTI5MzIsIDQ1LjkzMTM2OTgyOTg1MTFdLCBbLTY2LjYyODE0MzQzNzgyNjIsIDQ1LjkzMTg0NDY3MjYzMzNdLCBbLTY2LjYzMDE0NjY4MDkwOTcsIDQ1LjkzMzczMTUwNzcyNThdLCBbLTY2LjYzMTU3NTAwMjIxMTUsIDQ1LjkzNTE5OTY5NTkyMDRdLCBbLTY2LjYzMTk2MTI3Nzc4MzcsIDQ1LjkzNTg2MTkyOTc4OThdLCBbLTY2LjYzMjAzMzE0MzAwNjQsIDQ1LjkzNjMzNjczNDExMTRdLCBbLTY2LjYzMTY5MTc4MzE5ODQsIDQ1LjkzNzYwNDk0MTUxMjVdLCBbLTY2LjYzMDUzMjk1NjQ4MTksIDQ1LjkzOTc3MjY5Njg1MjJdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDQxLCAiTmVpZ2hib3VyaCI6ICJGb3Jlc3QgSGlsbCIsICJPQkpFQ1RJRCI6IDQxLCAiU2hhcGVfQXJlYSI6IDM5NjA0MC4xNDQ0NDgsICJTaGFwZV9MZW5nIjogNDQyMi4yMDg2NzUyNSwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmViMjRjIiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni42MzUyMjIxNjIyNjUsIDQ1LjkzODg0MTg4NDMzNjVdLCBbLTY2LjYzNjc1ODI4MTQwMDksIDQ1LjkzODkxMDYwMjU3MzJdLCBbLTY2LjYzNzk4ODk3MzM0MDEsIDQ1LjkzODg0ODEzMTQ1MjRdLCBbLTY2LjYzOTE5MjcxNTgyMDgsIDQ1LjkzODY2Njk2NDgwNDJdLCBbLTY2LjY0MDYzOTAwMzQyODMsIDQ1LjkzODI5ODM4MjU1NDddLCBbLTY2LjY0NzYwMDk0Njg4MDIsIDQ1LjkzNTUzMDgxMzg0MzZdLCBbLTY2LjY1MDQ5MzUyMjA5NSwgNDUuOTMzOTkzOTEwMTcwN10sIFstNjYuNjUwMTUyMTYyMjg3MSwgNDUuOTMzMTI1NDc4Mjg2OF0sIFstNjYuNjQ3OTk2MjA1NjA1MiwgNDUuOTMxNTU3MjY4Mjc3MV0sIFstNjYuNjQwMDI4MTQ5MDM1MSwgNDUuOTI3MjE0NzgyMDkxNV0sIFstNjYuNjM4MDk2NzcxMTc0MiwgNDUuOTI1ODI3NjE0MTQyNV0sIFstNjYuNjM2MDU3NTk1NDc5MywgNDUuOTI0OTAyODE2MjM4NV0sIFstNjYuNjMyNzc4NzQ0NjkyMiwgNDUuOTI3MjU4NTIxMDU3M10sIFstNjYuNjMxMDAwMDgwNDI5NywgNDUuOTI5MzcwNDQ3MjI1XSwgWy02Ni42MzAwNTY4NDkzODEzLCA0NS45Mjk2NTE2MTQ3NjE4XSwgWy02Ni42Mjg4MTcxNzQyODkzLCA0NS45Mjk4NDUzMDcxMjQ3XSwgWy02Ni42Mjc5MTg4NTkwMDUxLCA0NS45MzAyMzI2ODk4MjEzXSwgWy02Ni42Mjk5NzYwMDEwMDU4LCA0NS45MzIzMTk1MTEzNTAyXSwgWy02Ni42MzI2OTc4OTYzMTY2LCA0NS45MzQ0ODc0NzMzMTAyXSwgWy02Ni42MzM0Nzk0MzA2MTM4LCA0NS45MzUyODA5MTM3MDcyXSwgWy02Ni42MzQ1MTI0OTMxOTA2LCA0NS45MzY3OTI3OTIzMjkzXSwgWy02Ni42MzUyMjIxNjIyNjUsIDQ1LjkzODg0MTg4NDMzNjVdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDQyLCAiTmVpZ2hib3VyaCI6ICJTa3lsaW5lIEFjcmVhIiwgIk9CSkVDVElEIjogNDIsICJTaGFwZV9BcmVhIjogMTQ1NzUxMC4wODc2MSwgIlNoYXBlX0xlbmciOiA0ODk0LjY2MDAyMjIsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlYjI0YyIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjM1MjIyMTYyMjY1LCA0NS45Mzg4NDE4ODQzMzY1XSwgWy02Ni42MzU4ODY5MTU1NzUzLCA0NS45Mzk2MDQwMjcyODcxXSwgWy02Ni42MzgzNTcyODI2MDY2LCA0NS45NDAzNzI0MDY3MDZdLCBbLTY2LjYzOTA0MDAwMjIyMjUsIDQ1Ljk0MTI1MzIxODc5MzhdLCBbLTY2LjY0MDczNzgxODEwOTUsIDQ1Ljk0MTI5Njk0NjY4ODldLCBbLTY2LjY0MjQzNTYzMzk5NjUsIDQ1Ljk0MDk2NTg2MzE5NjddLCBbLTY2LjY0Mzk0NDgwMzY3MzgsIDQ1Ljk0MDI3ODcwMjQ2OV0sIFstNjYuNjQ3NjYzODI4OTUwMSwgNDUuOTM3NDg2MjQzNTI3OV0sIFstNjYuNjQ5NzI5OTU0MTAzNSwgNDUuOTM2MTg2Nzk2MzQzN10sIFstNjYuNjUwMTQzMTc5MTM0MiwgNDUuOTM2MTU1NTU5MjU3OF0sIFstNjYuNjUwNTExNDg4NDAwNywgNDUuOTM1MTc0NzA1ODA4Ml0sIFstNjYuNjUwNDkzNTIyMDk1LCA0NS45MzM5OTM5MTAxNzA3XSwgWy02Ni42NDc2MDA5NDY4ODAyLCA0NS45MzU1MzA4MTM4NDM2XSwgWy02Ni42NDA2MzkwMDM0MjgzLCA0NS45MzgyOTgzODI1NTQ3XSwgWy02Ni42MzkxOTI3MTU4MjA4LCA0NS45Mzg2NjY5NjQ4MDQyXSwgWy02Ni42Mzc5ODg5NzMzNDAxLCA0NS45Mzg4NDgxMzE0NTI0XSwgWy02Ni42MzY3NTgyODE0MDA5LCA0NS45Mzg5MTA2MDI1NzMyXSwgWy02Ni42MzUyMjIxNjIyNjUsIDQ1LjkzODg0MTg4NDMzNjVdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDQzLCAiTmVpZ2hib3VyaCI6ICJQb2V0J3MgSGlsbCIsICJPQkpFQ1RJRCI6IDQzLCAiU2hhcGVfQXJlYSI6IDI5NzAyMC43MjgwNTgsICJTaGFwZV9MZW5nIjogMzA4NC4xMTAyMzIwNSwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmVkOTc2IiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni42MjE1NDA4MjA0ODc5LCA0NS45MzA4MjYyNTQ4MzM0XSwgWy02Ni42MjE3OTIzNDg3Njc0LCA0NS45MzExOTQ4ODY3NDg2XSwgWy02Ni42MjI2MDA4MzI1MjMxLCA0NS45MzE4ODg0MDc5NDgzXSwgWy02Ni42MjI2NjM3MTQ1OTMsIDQ1LjkzMjAzMjEwOTQ1NDZdLCBbLTY2LjYyMjUwMjAxNzg0MTksIDQ1LjkzMTkzMjE0MzIyODhdLCBbLTY2LjYyMjU3Mzg4MzA2NDYsIDQ1LjkzMjA3NTg0NDYyMTddLCBbLTY2LjYyMjg4ODI5MzQxNDEsIDQ1LjkzMjE1NzA2Njk4MzVdLCBbLTY2LjYyMjg1MjM2MDgwMjcsIDQ1LjkzMjI1NzAzMjgwMzldLCBbLTY2LjYyMzE4NDczNzQ1NzgsIDQ1LjkzMjU5NDQxNjExNzZdLCBbLTY2LjYyNDAxMTE4NzUxOTIsIDQ1LjkzMzEzMTcyNjA0NjddLCBbLTY2LjYyNDc3NDc1NTUxMDcsIDQ1LjkzNDQ2ODczMDQ4NjRdLCBbLTY2LjYyNjM3Mzc1NjcxNjQsIDQ1LjkzNTkyNDQwNDI3NDldLCBbLTY2LjYyNzI4MTA1NTE1MzQsIDQ1LjkzNjk2MTQ3MDQ0NjFdLCBbLTY2LjYyNzY1ODM0NzU3MjcsIDQ1LjkzNzIwNTExNTcwODhdLCBbLTY2LjYyODk2MDkwNDczNDcsIDQ1LjkzOTUxNjU2ODc5MjFdLCBbLTY2LjYzMDUzMjk1NjQ4MTksIDQ1LjkzOTc3MjY5Njg1MjJdLCBbLTY2LjYzMTQ5NDE1MzgzNTksIDQ1LjkzODA5ODQ3MjUxMzNdLCBbLTY2LjYzMjAzMzE0MzAwNjQsIDQ1LjkzNjIxODAzMzQxMjFdLCBbLTY2LjYzMTY1NTg1MDU4NzEsIDQ1LjkzNTI5OTY1NjI1NjVdLCBbLTY2LjYzMDE0NjY4MDkwOTcsIDQ1LjkzMzczMTUwNzcyNThdLCBbLTY2LjYyODE0MzQzNzgyNjIsIDQ1LjkzMTg0NDY3MjYzMzNdLCBbLTY2LjYyNzQwNjgxOTI5MzIsIDQ1LjkzMTM2OTgyOTg1MTFdLCBbLTY2LjYyNjk2NjY0NDgwNCwgNDUuOTMwODUxMjQ2OTA1MV0sIFstNjYuNjI1MjA1OTQ2ODQ3MSwgNDUuOTMxMjgyMzU4MzY4OF0sIFstNjYuNjI0NTA1MjYwOTI1NSwgNDUuOTMxMjAxMTM0NzI2XSwgWy02Ni42MjM3OTU1OTE4NTEsIDQ1LjkzMDg4ODczNDk5MTVdLCBbLTY2LjYyMzExMjg3MjIzNTEsIDQ1LjkzMDc0NTAzMDUyMjddLCBbLTY2LjYyMjIzMjUyMzI1NjYsIDQ1LjkzMDcyMDAzODQwMzFdLCBbLTY2LjYyMTU0MDgyMDQ4NzksIDQ1LjkzMDgyNjI1NDgzMzRdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDQ0LCAiTmVpZ2hib3VyaCI6ICJEdW4ncyBDcm9zc2luZyIsICJPQkpFQ1RJRCI6IDQ0LCAiU2hhcGVfQXJlYSI6IDM2MzU0My4yNzgzMjMsICJTaGFwZV9MZW5nIjogMjkyMS45NDYyNTk3LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWIyNGMiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjYxOTgyNTAzODI5NTIsIDQ1LjkyOTY3NjYwNzM2MjddLCBbLTY2LjYyMTU0MDgyMDQ4NzksIDQ1LjkzMDgyNjI1NDgzMzRdLCBbLTY2LjYyMjk0MjE5MjMzMTEsIDQ1LjkzMDcyNjI4NjQzNDFdLCBbLTY2LjYyMzc5NTU5MTg1MSwgNDUuOTMwODg4NzM0OTkxNV0sIFstNjYuNjI0NjQwMDA4MjE4MSwgNDUuOTMxMjMyMzc0NjAyN10sIFstNjYuNjI1NjI4MTU1MDMwNiwgNDUuOTMxMjQ0ODcwNTQ4NV0sIFstNjYuNjI2OTY2NjQ0ODA0LCA0NS45MzA4NTEyNDY5MDUxXSwgWy02Ni42MjY3NjkwMTU0NDE1LCA0NS45MzA0NTEzNzI0MDY5XSwgWy02Ni42MjcxMjgzNDE1NTUxLCA0NS45MzAxMDc3Mjc5NTY3XSwgWy02Ni42Mjc1OTU0NjU1MDI5LCA0NS45MzAwODI3MzU1NV0sIFstNjYuNjI3OTE4ODU5MDA1MSwgNDUuOTMwMjMyNjg5ODIxM10sIFstNjYuNjI4ODE3MTc0Mjg5MywgNDUuOTI5ODQ1MzA3MTI0N10sIFstNjYuNjMwMDU2ODQ5MzgxMywgNDUuOTI5NjUxNjE0NzYxOF0sIFstNjYuNjMxMDAwMDgwNDI5NywgNDUuOTI5MzcwNDQ3MjI1XSwgWy02Ni42MzI3Nzg3NDQ2OTIyLCA0NS45MjcyNTg1MjEwNTczXSwgWy02Ni42MzUyODUwNDQzMzQ5LCA0NS45MjUzOTY0NjAyODEyXSwgWy02Ni42MzYwNTc1OTU0NzkzLCA0NS45MjQ5MDI4MTYyMzg1XSwgWy02Ni42MzYyNzMxOTExNDc0LCA0NS45MjQ5ODQwNDkxMDQ0XSwgWy02Ni42MzU2MzUzODcyOTU3LCA0NS45MjQ0MDkxNjc4MDNdLCBbLTY2LjYzMjczMzgyODkyOCwgNDUuOTIyNTcyMDA3MTg0Nl0sIFstNjYuNjI4NjI4NTI4MDc5NiwgNDUuOTE5NjQ3NDIxOTIyNl0sIFstNjYuNjI1NjY0MDg3NjQyLCA0NS45MTc4NDEzNTEwNDA0XSwgWy02Ni42MjQ3Mjk4Mzk3NDY1LCA0NS45MTc4MzUxMDE1NTgxXSwgWy02Ni42MjQwNzQwNjk1ODkxLCA0NS45MTgxNzI1NzI1OTM3XSwgWy02Ni42MjA4NDkxMTc3MTkxLCA0NS45MjE5MDMzNjU2MDFdLCBbLTY2LjYxOTc2MjE1NjIyNTMsIDQ1LjkyMzU4NDMyNzcwNF0sIFstNjYuNjE5NDI5Nzc5NTcwMiwgNDUuOTI0MzQ2NjgwMzQ2MV0sIFstNjYuNjE5MzY2ODk3NTAwMywgNDUuOTI1NjUyNjUzNTU5M10sIFstNjYuNjE5ODI1MDM4Mjk1MiwgNDUuOTI5Njc2NjA3MzYyN11dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogNDUsICJOZWlnaGJvdXJoIjogIlNvdXRod29vZCBQYXJrIiwgIk9CSkVDVElEIjogNDUsICJTaGFwZV9BcmVhIjogMTIxODM5OC4wNDE4MSwgIlNoYXBlX0xlbmciOiA0MzczLjgyNDMzNjAyLCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbWy02Ni41ODg0ODI4MTgwMzIzLCA0NS45MTM1MTY1NDEwMjUyXSwgWy02Ni41ODg2MzU1MzE2MzA2LCA0NS45MTM3MjI3ODk2MTg2XSwgWy02Ni41ODg1MDMwMDk1MjI2LCA0NS45MTM1MjIwNTk5MTk1XSwgWy02Ni41ODg0ODI4MTgwMzIzLCA0NS45MTM1MTY1NDEwMjUyXV1dLCBbW1stNjYuNTk4NjI0Nzk3NTksIDQ1Ljg5ODA4OTQ3Mzk0MzVdLCBbLTY2LjU5NzE3ODUwOTk4MjYsIDQ1Ljg5ODI2NDUyMTQzOV0sIFstNjYuNTk1ODQwMDIwMjA5MiwgNDUuODk4Njg5NjM0NDg3OF0sIFstNjYuNTk0Njk5MTU5Nzk4NCwgNDUuODk5MzMzNTQ5NTI0OF0sIFstNjYuNTg2NjIzMzA1Mzk0MiwgNDUuOTA4NDg1MDg3OTI5OV0sIFstNjYuNTg2ODExOTUxNjAzOCwgNDUuOTA5OTE2NDQyMTI1N10sIFstNjYuNTg3MTQ0MzI4MjU4OSwgNDUuOTExMDQxNDk4MTE3M10sIFstNjYuNTg3NzczMTQ4OTU3OCwgNDUuOTEyNDE2NTM1NTgxN10sIFstNjYuNTg4NTAzMDA5NTIyNiwgNDUuOTEzNTIyMDU5OTE5NV0sIFstNjYuNTg5NDg4OTMxMTUwNSwgNDUuOTEzNzkxNTM4OTc5NF0sIFstNjYuNTkwNTU3OTI2MzM4NiwgNDUuOTEzOTEwMjg3Njc0N10sIFstNjYuNTkyNDcxMzM3ODkzOCwgNDUuOTEzNzE2NTM5NjcyNV0sIFstNjYuNTk0MTMzMjIxMTY5NCwgNDUuOTEyMTA0MDMwMDU4NF0sIFstNjYuNTk1ODc1OTUyODIwNiwgNDUuOTEwMDYwMjAwNTUxXSwgWy02Ni41OTg5MjEyNDE2MzM3LCA0NS45MDU4MDM1NDMzODk3XSwgWy02Ni42MDA0MjE0MjgxNTgyLCA0NS45MDIyNzc5NTkwNjIzXSwgWy02Ni42MDA2NzI5NTY0Mzc4LCA0NS45MDEzNzc3NzM5OTIxXSwgWy02Ni42MDA3NjI3ODc5NjYyLCA0NS45MDAyNDAwMTkyMDNdLCBbLTY2LjYwMDY2Mzk3MzI4NDksIDQ1Ljg5OTMyNzI5Nzk1ODRdLCBbLTY2LjYwMDMyMjYxMzQ3NywgNDUuODk4MjA4MjU2MjMyN10sIFstNjYuNTk4NjI0Nzk3NTksIDQ1Ljg5ODA4OTQ3Mzk0MzVdXV1dLCAidHlwZSI6ICJNdWx0aVBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDQ2LCAiTmVpZ2hib3VyaCI6ICJMaW5jb2xuIEhlaWdodHMiLCAiT0JKRUNUSUQiOiA0NiwgIlNoYXBlX0FyZWEiOiAxMDkyNDYxLjI4ODI5LCAiU2hhcGVfTGVuZyI6IDQ1MDUuNjc3ODIxNzQsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlYjI0YyIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNTUyNDg3MzI0NTk3NiwgNDUuODk1MDUxMDYxNjQyNl0sIFstNjYuNTUxMzE5NTE0NzI4MiwgNDUuODk1NDE5OTMxMjYxNF0sIFstNjYuNTUxMjI5NjgzMTk5OSwgNDUuODk1ODQ1MDY2MDg4XSwgWy02Ni41NTEzOTEzNzk5NTEsIDQ1Ljg5NjQzODk5ODk5ODhdLCBbLTY2LjU1MTEzMDg2ODUxODYsIDQ1Ljg5NjgwMTYwNzU0NzZdLCBbLTY2LjU1MTE5Mzc1MDU4ODUsIDQ1Ljg5Njk0NTM5OTkzNzJdLCBbLTY2LjU1NTcxMjI3NjQ2NzYsIDQ1Ljg5OTkxNDk0MjEyMzhdLCBbLTY2LjU1Nzg5NTE4MjYwOCwgNDUuOTAxMTQwMjIyNzIwMV0sIFstNjYuNTYwMTk0ODY5NzM1NCwgNDUuOTAyMjQwNDUxNjQyNF0sIFstNjYuNTYyNTAzNTQwMDE1NSwgNDUuOTAyNzkwNTU3OTI3NF0sIFstNjYuNTY0NjIzNTY0MDg2MSwgNDUuOTAzMDQwNjA0NDM2OV0sIFstNjYuNTY0OTgyODkwMTk5NywgNDUuOTAzMjk2OTAwOTQwNF0sIFstNjYuNTY4MDE5MTk1ODYsIDQ1LjkwNDM5NzA4NzEyNF0sIFstNjYuNTY4NTA0Mjg2MTEzNSwgNDUuOTA0NzM0NjM5ODc3NV0sIFstNjYuNTY5MDUyMjU4NDM2OCwgNDUuOTA0ODE1OTAyMjcwOV0sIFstNjYuNTcwOTI5NzM3MzgwNiwgNDUuOTA1NTc4NTEyNzgxOF0sIFstNjYuNTcwOTkyNjE5NDUwNSwgNDUuOTA1OTE2MDU4MzUxN10sIFstNjYuNTcyMjA1MzQ1MDg0LCA0NS45MDU5NTk4MTQxMDg2XSwgWy02Ni41NzUxMTU4ODY2MDQ2LCA0NS45MDcyNzI0NzA3NzkxXSwgWy02Ni41NzYyNjU3MzAxNjgzLCA0NS45MDc2NDc1MDk4NDA4XSwgWy02Ni41Nzc3ODM4ODI5OTg0LCA0NS45MDg3OTEzNjMzMjkxXSwgWy02Ni41Nzg2MzcyODI1MTgzLCA0NS45MDkyNjAxNDg5MzI1XSwgWy02Ni41ODAxNDY0NTIxOTU2LCA0NS45MDk4MDM5MzUyNzIzXSwgWy02Ni41ODE2NjQ2MDUwMjU4LCA0NS45MTA3MzUyMzUxMzQyXSwgWy02Ni41ODgyODUxODg2Njk4LCA0NS45MTU0NzI3NDY4NDA5XSwgWy02Ni41OTAyODg0MzE3NTM0LCA0NS45MTcwNzg5MDkwMDc5XSwgWy02Ni41OTA5NTMxODUwNjM2LCA0NS45MTc5Mjg4NDM3MTg0XSwgWy02Ni41OTI0MDg0NTU4MjM5LCA0NS45MTg4OTc1MDM0MzM5XSwgWy02Ni41OTI3NzY3NjUwOTA0LCA0NS45MTk0MDk5NDg4MzExXSwgWy02Ni41OTM2ODQwNjM1MjczLCA0NS45MjAwNDExMjUwNzE5XSwgWy02Ni41OTc5OTU5NzY4OTExLCA0NS45MjIzMjIwNDg2NTcyXSwgWy02Ni42MDE3MjM5ODUzMjAyLCA0NS45MjQ5NDAzMDgzNDUyXSwgWy02Ni42MDIxMDEyNzc3Mzk1LCA0NS45MjQ5NDAzMDgzNDUyXSwgWy02Ni42MDI2MzEyODM3NTcyLCA0NS45MjUxMjc3Njg0OTldLCBbLTY2LjYwMzMyMjk4NjUyNTksIDQ1LjkyNTc3MTM3Njg3MjRdLCBbLTY2LjYwMzk2OTc3MzUzMDUsIDQ1LjkyNTg4Mzg1MTM1NTZdLCBbLTY2LjYwNDYwNzU3NzM4MjIsIDQ1LjkyNjE5MDAzMDczNzldLCBbLTY2LjYwNTUwNTg5MjY2NjMsIDQ1LjkyNjQxNDk3Nzc3ODddLCBbLTY2LjYwNzYzNDg5OTg4OTcsIDQ1LjkyNjc2NDg5MzU4NDVdLCBbLTY2LjYwOTE0NDA2OTU2NywgNDUuOTI2ODI3Mzc4MzE3NV0sIFstNjYuNjExMDY2NDY0Mjc1MSwgNDUuOTI2NzMzNjUxMTkxNl0sIFstNjYuNjEyNTc1NjMzOTUyNCwgNDUuOTI2OTQ2MDk5MTE2NF0sIFstNjYuNjEzMDUxNzQxMDUzLCA0NS45MjczMjcyNTM2NDgxXSwgWy02Ni42MTM5MTQxMjM3MjU3LCA0NS45Mjc0ODM0NjM3NjUyXSwgWy02Ni42MTg1MDQ1MTQ4Mjc2LCA0NS45MjkyMDE3NDYwMTg3XSwgWy02Ni42MTg4OTk3NzM1NTI2LCA0NS45MjkyNDU0ODM0MTc4XSwgWy02Ni42MTk4MjUwMzgyOTUyLCA0NS45Mjk2NzY2MDczNjI3XSwgWy02Ni42MTkzOTM4NDY5NTg4LCA0NS45MjY0MTQ5Nzc3Nzg3XSwgWy02Ni42MTAyMzEwMzEwNjA4LCA0NS45MjAxODQ4NTcyNzE2XSwgWy02Ni42MDcxOTQ3MjU0MDA1LCA0NS45MTg4MTAwMTIyODMzXSwgWy02Ni42MDQwNzc1NzEzNjQ2LCA0NS45MTc1MjI2MjY1NDddLCBbLTY2LjYwMzI2MDEwNDQ1NjEsIDQ1LjkxODc3ODc2NTQxMDRdLCBbLTY2LjYwMjE0NjE5MzUwMzcsIDQ1LjkxOTkxNjE0MDI0NzhdLCBbLTY2LjYwMDc3MTc3MTExOSwgNDUuOTIwOTAzNTEyNjg0N10sIFstNjYuNTk5NDUxMjQ3NjUxNCwgNDUuOTIxNTkwOTEzNTAwM10sIFstNjYuNTk0MzMwODUwNTMxOSwgNDUuOTE4NTI4Nzg5NzkzNV0sIFstNjYuNTkyNTc5MTM1NzI3OSwgNDUuOTE3MjAzOTAwMjIyOV0sIFstNjYuNTkzMjA3OTU2NDI2OCwgNDUuOTE2NDkxNDQ2NTI1OF0sIFstNjYuNTk0MjMyMDM1ODUwNywgNDUuOTE1Nzc4OTgzNjgxM10sIFstNjYuNTk1NDcxNzEwOTQyNywgNDUuOTE1MjY2NTA0NzUxMV0sIFstNjYuNTk2ODU1MTE2NDgwMywgNDUuOTE0OTg1MjY0MzAyNV0sIFstNjYuNTkyNDcxMzM3ODkzOCwgNDUuOTEzNzE2NTM5NjcyNV0sIFstNjYuNTkwNTU3OTI2MzM4NiwgNDUuOTEzOTEwMjg3Njc0N10sIFstNjYuNTg5NDg4OTMxMTUwNSwgNDUuOTEzNzkxNTM4OTc5NF0sIFstNjYuNTg4NDk4MTQ2MjU5NSwgNDUuOTEzNTIwNzMwNjU0OV0sIFstNjYuNTg4NjM1NTMxNjMwNiwgNDUuOTEzNzIyNzg5NjE4Nl0sIFstNjYuNTg4NDgyODE4MDMyMywgNDUuOTEzNTE2NTQxMDI1Ml0sIFstNjYuNTg4NDk4MTQ2MjU5NSwgNDUuOTEzNTIwNzMwNjU0OV0sIFstNjYuNTg3OTI1ODYyNTU2MSwgNDUuOTEyNjc5MDM4ODYxM10sIFstNjYuNTg3MjUyMTI2MDkzLCA0NS45MTEzMjI3NTg1NTE5XSwgWy02Ni41ODY4MTE5NTE2MDM4LCA0NS45MDk5MTY0NDIxMjU3XSwgWy02Ni41ODY2MjMzMDUzOTQyLCA0NS45MDg0ODUwODc5Mjk5XSwgWy02Ni41ODIzMjkzNTgzMzYxLCA0NS45MDQ4NDcxNTcwMDU5XSwgWy02Ni41ODAzODAwMTQxNjk1LCA0NS45MDI5MjgwODM2NDddLCBbLTY2LjU3ODEyNTI0MjgwNjQsIDQ1LjkwMDQ0MDA2NTY5MDRdLCBbLTY2LjU3NzY2NzEwMjAxMTUsIDQ1LjkwMDIwMjUxMDQwNjRdLCBbLTY2LjU3NjMyODYxMjIzODEsIDQ1Ljg5OTcwODY0MjIyMV0sIFstNjYuNTc1NzQ0NzA3MzAzNSwgNDUuODk5NjQ2MTI2OTQ3Nl0sIFstNjYuNTc0NjMwNzk2MzUxMiwgNDUuODk5ODk2MTg3NjE4OV0sIFstNjYuNTczNzY4NDEzNjc4NCwgNDUuOTAwMjgzNzc5NDMzN10sIFstNjYuNTczNDAwMTA0NDExOSwgNDUuOTAwMjk2MjgyMzUwNV0sIFstNjYuNTczMDQ5NzYxNDUxMSwgNDUuODk5NjAyMzY2MjE0NF0sIFstNjYuNTcyNjkwNDM1MzM3NSwgNDUuODk5MjY0NzgyMjU1N10sIFstNjYuNTcxOTcxNzgzMTEwMiwgNDUuODk4OTk1OTYzOTMxOF0sIFstNjYuNTcxMTQ1MzMzMDQ4OCwgNDUuODk4OTA4NDQxNDA1OV0sIFstNjYuNTY5Nzk3ODYwMTIyNiwgNDUuODk4ODk1OTM4MTc2N10sIFstNjYuNTY4NzY0Nzk3NTQ1OSwgNDUuODk5NDA4NTY4MjY2OF0sIFstNjYuNTY4NjY1OTgyODY0NiwgNDUuODk5MzUyMzA0MjE5OF0sIFstNjYuNTY4NzE5ODgxNzgxNiwgNDUuODk4ODA4NDE1NDkzMl0sIFstNjYuNTY4NDIzNDM3NzM3OSwgNDUuODk4NTU4MzQ5OTIzXSwgWy02Ni41Njc1ODgwMDQ1MjM3LCA0NS44OTgzODk1NTUwMjY1XSwgWy02Ni41NjY1NTQ5NDE5NDY5LCA0NS44OTg3NzcxNTczNTg1XSwgWy02Ni41NjYwNTE4ODUzODc4LCA0NS44OTgwNzA3MTg4MjE5XSwgWy02Ni41NjQ1OTY2MTQ2Mjc1LCA0NS44OTc2MjA1OTQwMDQ3XSwgWy02Ni41NjM5MDQ5MTE4NTg4LCA0NS44OTc2NDU2MDEwMzQ3XSwgWy02Ni41NjMwOTY0MjgxMDMxLCA0NS44OTc5NDU2ODQ1MTY1XSwgWy02Ni41NjI0Njc2MDc0MDQyLCA0NS44OTgzNzA4MDAwMDYzXSwgWy02Ni41NjE2MDUyMjQ3MzE0LCA0NS44OTg1NTgzNDk5MjNdLCBbLTY2LjU2MTA0ODI2OTI1NTMsIDQ1Ljg5ODU1MjA5ODI2OTNdLCBbLTY2LjU2MDM5MjQ5OTA5NzksIDQ1Ljg5Nzk4OTQ0NjU1NTRdLCBbLTY2LjU1OTM2ODQxOTY3NCwgNDUuODk3NjY0MzU2Mjk5OF0sIFstNjYuNTU5MTQzODQwODUyOSwgNDUuODk3NDk1NTU4Njg1N10sIFstNjYuNTU4NjIyODE3OTg4MiwgNDUuODk3NDI2Nzg5MTQwMl0sIFstNjYuNTU4MTE5NzYxNDI5LCA0NS44OTcwNzY2ODgzMTU1XSwgWy02Ni41NTgyNjM0OTE4NzQ1LCA0NS44OTY1ODkwNDQyMDI3XSwgWy02Ni41NTgwMDI5ODA0NDIxLCA0NS44OTY2NTE1NjI5MTgxXSwgWy02Ni41NTc4NjgyMzMxNDk1LCA0NS44OTY1ODI3OTIzMjczXSwgWy02Ni41NTgzNTMzMjM0MDI5LCA0NS44OTY0MjY0OTUyMTM1XSwgWy02Ni41NTc5NDAwOTgzNzIyLCA0NS44OTU4ODg4Mjk3ODI0XSwgWy02Ni41NTgxMTA3NzgyNzYyLCA0NS44OTU1MzI0NjcyNjc2XSwgWy02Ni41NTc0OTA5NDA3MzAyLCA0NS44OTYwMzg4NzY0NzI5XSwgWy02Ni41NTYzMDUxNjQ1NTUxLCA0NS44OTYyNDUxOTAwMTAzXSwgWy02Ni41NTYxODgzODM1NjgyLCA0NS44OTY0MjY0OTUyMTM1XSwgWy02Ni41NTYyNjkyMzE5NDM4LCA0NS44OTY4NTE2MjIzMzQxXSwgWy02Ni41NTY0Mzk5MTE4NDc3LCA0NS44OTcyMTQyMjgxODg1XSwgWy02Ni41NTY4MzUxNzA1NzI4LCA0NS44OTc0ODkzMDY5MTIzXSwgWy02Ni41NTY3MDk0MDY0MzMsIDQ1Ljg5NzYyNjg0NTc2MzJdLCBbLTY2LjU1NjA3MTYwMjU4MTMsIDQ1Ljg5Nzc4MzEzOTQ5ODVdLCBbLTY2LjU1NTEyODM3MTUzMjksIDQ1Ljg5NzE0NTQ1ODI5NDZdLCBbLTY2LjU1NDU4MDM5OTIwOTYsIDQ1Ljg5NjI1MTQ0MTkyMzhdLCBbLTY2LjU1NDIwMzEwNjc5MDMsIDQ1Ljg5NjIyMDE4MjM0OTddLCBbLTY2LjU1MzM2NzY3MzU3NiwgNDUuODk2NDU3NzU0NjcxNV0sIFstNjYuNTUyOTU0NDQ4NTQ1NCwgNDUuODk2MzQ1MjIwNTQwNV0sIFstNjYuNTUyODQ2NjUwNzExMywgNDUuODk2MDg4ODkxOTQ2M10sIFstNjYuNTUzMTg4MDEwNTE5MiwgNDUuODk1NDEzNjc5MjU0NF0sIFstNjYuNTUzMDk4MTc4OTkwOCwgNDUuODk1MDY5ODE3Nzg0XSwgWy02Ni41NTI0ODczMjQ1OTc2LCA0NS44OTUwNTEwNjE2NDI2XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiA0NywgIk5laWdoYm91cmgiOiAiTGluY29sbiIsICJPQkpFQ1RJRCI6IDQ3LCAiU2hhcGVfQXJlYSI6IDI5OTExNDguODAxNzYsICJTaGFwZV9MZW5nIjogMTYyNjIuMTIzMjM5LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjY2ODYzMDUwNzY4MTQsIDQ1Ljk2MDc1ODY4MjI3MTldLCBbLTY2LjY2OTU0Njc4OTI3MTIsIDQ1Ljk2MTYzOTE3MDQ0MTldLCBbLTY2LjY3MTQ1MTIxNzY3MzYsIDQ1Ljk2MTIzOTUxNzk3MTNdLCBbLTY2LjY3Mjc4OTcwNzQ0NjksIDQ1Ljk2MTE4OTU2MTIwOThdLCBbLTY2LjY3Mzg4NTY1MjA5MzUsIDQ1Ljk2MTQ4OTMwMTEwMzNdLCBbLTY2LjY3NDgxMDkxNjgzNjIsIDQ1Ljk2MjE2OTk1NDQyMjVdLCBbLTY2LjY3NTgzNDk5NjI2MDEsIDQ1Ljk2MTMyMDY5NzYxMjddLCBbLTY2LjY3NzE3MzQ4NjAzMzQsIDQ1Ljk2MDcyMTIxNDM3OTldLCBbLTY2LjY3ODQ4NTAyNjM0ODIsIDQ1Ljk2MDQ0NjQ0OTA2MzddLCBbLTY2LjY4MTIzMzg3MTExNzYsIDQ1Ljk2MDI3Nzg0MjM5OTZdLCBbLTY2LjY4MTM4NjU4NDcxNTksIDQ1Ljk1OTExNjMxNTg4M10sIFstNjYuNjgxMDcyMTc0MzY2NSwgNDUuOTU3OTY3MjU0OTQwOF0sIFstNjYuNjgwNDYxMzE5OTczMywgNDUuOTU3MDYxNzI4MTcxMl0sIFstNjYuNjc5NTk4OTM3MzAwNSwgNDUuOTU2NzkzMTg5ODAxNl0sIFstNjYuNjc3OTgxOTY5Nzg5MSwgNDUuOTU2NTY4MzY1OTc5N10sIFstNjYuNjc2MTEzNDczOTk4MSwgNDUuOTU2NzI0NDkzNzMwNl0sIFstNjYuNjcwMDU4ODI4OTgzMiwgNDUuOTU4ODU0MDMyMzMxOV0sIFstNjYuNjY5MjUwMzQ1MjI3NSwgNDUuOTU5NTU5Njk3MTU3OV0sIFstNjYuNjY4NjMwNTA3NjgxNCwgNDUuOTYwNzU4NjgyMjcxOV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogNDgsICJOZWlnaGJvdXJoIjogIkNvbG9uaWFsIGhlaWdodHMiLCAiT0JKRUNUSUQiOiA0OCwgIlNoYXBlX0FyZWEiOiAzNzY4ODUuNDg2OTU0LCAiU2hhcGVfTGVuZyI6IDI2MzQuODMxMDYxMTYsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlZDk3NiIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjk4MTIyMTk4NDU5MSwgNDUuOTYwODA4NjM5NDIyXSwgWy02Ni42OTk3MTIyMTY1MTIsIDQ1Ljk2MTE3MDgyNzQxMjZdLCBbLTY2LjcwMTA2ODY3MjU5MSwgNDUuOTYxNjM5MTcwNDQxOV0sIFstNjYuNzAxNjQzNTk0MzcyOCwgNDUuOTYxMzc2ODk4ODMzMl0sIFstNjYuNzAxMjc1Mjg1MTA2MywgNDUuOTYxMDI3MjAxNDIzN10sIFstNjYuNzAxMTMxNTU0NjYwOSwgNDUuOTYwNTE1MTQwNTIwNV0sIFstNjYuNzAxODE0Mjc0Mjc2OCwgNDUuOTU4ODQ3Nzg3NDcwNF0sIFstNjYuNzAxODQxMjIzNzM1MywgNDUuOTU3NTQyNTk1OTUzNV0sIFstNjYuNzAxMTA0NjA1MjAyMywgNDUuOTU3MDY3OTczMjM0MV0sIFstNjYuNzAwMDM1NjEwMDE0MiwgNDUuOTU2NTkzMzQ2NDQ5NF0sIFstNjYuNjk4ODQ5ODMzODM5MiwgNDUuOTU2MjY4NTk5NDY1XSwgWy02Ni42OTc5MzM1NTIyNDk0LCA0NS45NTYxNzQ5MjIwOTY1XSwgWy02Ni42OTcyNzc3ODIwOTIsIDQ1Ljk1NTg1NjQxNzg1OTRdLCBbLTY2LjY5NjU3NzA5NjE3MDQsIDQ1Ljk1NzI1NTMyNDc5MzJdLCBbLTY2LjY5NjQ2MDMxNTE4MzQsIDQ1Ljk1ODU1NDI3ODE4MTldLCBbLTY2LjY5NzA4MDE1MjcyOTUsIDQ1Ljk1OTc1OTUyOTgxMl0sIFstNjYuNjk4MTIyMTk4NDU5MSwgNDUuOTYwODA4NjM5NDIyXV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiA0OSwgIk5laWdoYm91cmgiOiAiR2FyZGVuIFBsYWNlIiwgIk9CSkVDVElEIjogNDksICJTaGFwZV9BcmVhIjogMTg4NjEwLjQ1MzA0LCAiU2hhcGVfTGVuZyI6IDE3NTIuMDAyODM5MiwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmVkOTc2IiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni43MDEwNjg2NzI1OTEsIDQ1Ljk2MTYzOTE3MDQ0MTldLCBbLTY2LjcwMjU2ODg1OTExNTUsIDQ1Ljk2MjM3NjAyMjEyN10sIFstNjYuNzAzODcxNDE2Mjc3NCwgNDUuOTYzMjg3NzA2NDEwNl0sIFstNjYuNzA1NTY5MjMyMTY0NCwgNDUuOTYzNTA2MjU4NjMyOV0sIFstNjYuNzA3MTc3MjE2NTIzLCA0NS45NjM5NTU4NDkwNjQ2XSwgWy02Ni43MDY5NzA2MDQwMDc3LCA0NS45NjMxOTQwNDA5MDg2XSwgWy02Ni43MDcxNzcyMTY1MjMsIDQ1Ljk2MjI5NDg0NDAzMTldLCBbLTY2LjcwNzkwNDg1MTkwMzEsIDQ1Ljk2MTMxNDQ1MzAyOTFdLCBbLTY2LjcwOTAxODc2Mjg1NTQsIDQ1Ljk2MDMwOTA2NTg5NDddLCBbLTY2LjcxMDk0MTE1NzU2MzUsIDQ1Ljk1OTI0NzQ1NzE5M10sIFstNjYuNzEyMDM3MTAyMjEwMSwgNDUuOTU4ODYwMjc3MTkyOF0sIFstNjYuNzEzNTEwMzM5Mjc2LCA0NS45NTg1MjkyOTg1OTYyXSwgWy02Ni43MTQxMTIyMTA1MTY0LCA0NS45NTc5NTQ3NjUwMTddLCBbLTY2LjcxNTMwNjk2OTg0NDMsIDQ1Ljk1ODA3MzQxOTE3OTFdLCBbLTY2LjcxNzM3MzA5NDk5NzgsIDQ1Ljk1MDkyMjQ5MDk2NzFdLCBbLTY2LjcwOTE2MjQ5MzMwMDksIDQ1Ljk1MDEzNTUyMDIzODhdLCBbLTY2LjcwOTM5NjA1NTI3NDgsIDQ1Ljk1MTY3ODIyMjE4MDZdLCBbLTY2LjcwOTI3OTI3NDI4NzgsIDQ1Ljk1MzIzMzM3MjE3MzRdLCBbLTY2LjcwODgwMzE2NzE4NzMsIDQ1Ljk1NDc1MTAwNjU5OTJdLCBbLTY2LjcwNzk3NjcxNzEyNTksIDQ1Ljk1NjE5OTkwMjc0MzZdLCBbLTY2LjcwNzA1MTQ1MjM4MzIsIDQ1Ljk1NzMyNDAyMDIwNjJdLCBbLTY2LjcwMzQ0MDIyNDk0MSwgNDUuOTYwODUyMzUxODkxM10sIFstNjYuNzAyNzY2NDg4NDc4LCA0NS45NjEyMTQ1Mzk1OTYyXSwgWy02Ni43MDE2NDM1OTQzNzI4LCA0NS45NjEzNzY4OTg4MzMyXSwgWy02Ni43MDEwNjg2NzI1OTEsIDQ1Ljk2MTYzOTE3MDQ0MTldXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDUwLCAiTmVpZ2hib3VyaCI6ICJGcmVkZXJpY3RvbiBTb3V0aCIsICJPQkpFQ1RJRCI6IDUwLCAiU2hhcGVfQXJlYSI6IDc1NzkzMy40NTkwOCwgIlNoYXBlX0xlbmciOiA0NTY4LjI2NjU4MTMzLCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZDhkM2MiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjY1MzMyMzIxNTI0LCA0NS45MzM1MDY1OTAzNTYzXSwgWy02Ni42NTQ1NDQ5MjQwMjY0LCA0NS45MzQxNzUwOTIwODY2XSwgWy02Ni42NTU5MDEzODAxMDU1LCA0NS45MzQ2OTk4OTE1MzcxXSwgWy02Ni42NTY3Mjc4MzAxNjY4LCA0NS45MzQ5MjQ4MDQwNjddLCBbLTY2LjY1ODA2NjMxOTk0MDIsIDQ1LjkzNTA4MDk5Mjc4NzJdLCBbLTY2LjY1OTE0NDI5ODI4MTEsIDQ1LjkzNTA5OTczNTQwNDFdLCBbLTY2LjY1OTc4MjEwMjEzMjgsIDQ1LjkzNDk0OTc5NDI5MThdLCBbLTY2LjY2MDc2MTI2NTc5MjUsIDQ1LjkzNDU4MTE4NzMzNDFdLCBbLTY2LjY2MTYxNDY2NTMxMjUsIDQ1LjkzNDA3NTEyOTcyMzVdLCBbLTY2LjY2MTM4MTEwMzMzODYsIDQ1LjkzMzYxMjgwMTQ1MDFdLCBbLTY2LjY2MDk0MDkyODg0OTQsIDQ1LjkzMzIzMTY5MDExMDRdLCBbLTY2LjY1NzU2MzI2MzM4MTEsIDQ1LjkzMTYwNzI1MTc1MDRdLCBbLTY2LjY1NjI4NzY1NTY3NzYsIDQ1LjkzMTE4ODYzODc3MDRdLCBbLTY2LjY1NDM0NzI5NDY2MzksIDQ1LjkzMDg4MjQ4Njk3ODhdLCBbLTY2LjY1MjYyMjUyOTMxODQsIDQ1LjkzMDk4ODcwMzA5OF0sIFstNjYuNjUyNDE1OTE2ODAzMSwgNDUuOTMxMDMyNDM5MDg3OV0sIFstNjYuNjUyMzA4MTE4OTY5LCA0NS45MzEyNjM2MTQ0NjE4XSwgWy02Ni42NTIxOTEzMzc5ODIsIDQ1LjkzMTg2OTY2NDI0NjFdLCBbLTY2LjY1MjMxNzEwMjEyMTgsIDQ1LjkzMjQ2OTQ1OTU3NDFdLCBbLTY2LjY1Mjc3NTI0MjkxNjcsIDQ1LjkzMzEyNTQ3ODI4NjhdLCBbLTY2LjY1MzMyMzIxNTI0LCA0NS45MzM1MDY1OTAzNTYzXV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiA1MSwgIk5laWdoYm91cmgiOiAiVGhlIEh1Z2ggSm9obiBGbGVtbWluZyBGb3Jlc3RyeSBDZW50ZXIiLCAiT0JKRUNUSUQiOiA1MSwgIlNoYXBlX0FyZWEiOiAyMjA3MTguOTcwODgsICJTaGFwZV9MZW5nIjogMTg3My44NDcwMzA3NSwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmZmZmIyIiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni42NjE2MDU2ODIxNTk2LCA0NS45MzQwMzc2NDM3OTA4XSwgWy02Ni42NjE5MjkwNzU2NjE5LCA0NS45MzQxODEzMzk3MjgzXSwgWy02Ni42NjMxMjM4MzQ5ODk4LCA0NS45MzI3ODgwOTgyMDM3XSwgWy02Ni42NjMxODY3MTcwNTk3LCA0NS45MzI0NzU3MDc0MDhdLCBbLTY2LjY2MjkxNzIyMjQ3NDQsIDQ1LjkzMjI3NTc3NjM3NTJdLCBbLTY2LjY1OTk3OTczMTQ5NTQsIDQ1LjkzMDkzODcxOTA2NzJdLCBbLTY2LjY1NTc3NTYxNTk2NTcsIDQ1LjkyOTI3MDQ3NjIwMTddLCBbLTY2LjY1NTAxMjA0Nzk3NDIsIDQ1LjkyOTE0NTUxMjE2OTNdLCBbLTY2LjY1NDA1MDg1MDYyMDIsIDQ1LjkyOTE1ODAwODU4NTJdLCBbLTY2LjY1MzExNjYwMjcyNDcsIDQ1LjkyOTMzOTIwNjI5OTZdLCBbLTY2LjY1MjQ0Mjg2NjI2MTYsIDQ1LjkyOTYwMTYyOTUyNjFdLCBbLTY2LjY1MjA1NjU5MDY4OTQsIDQ1LjkzMDQ2Mzg2ODUyODZdLCBbLTY2LjY1MjI3MjE4NjM1NzYsIDQ1LjkzMTM1NzMzMzkzMzVdLCBbLTY2LjY1MjQxNTkxNjgwMzEsIDQ1LjkzMTAzMjQzOTA4NzldLCBbLTY2LjY1MzkwNzEyMDE3NDcsIDQ1LjkzMDg2OTk5MDk1MTRdLCBbLTY2LjY1NDk4NTA5ODUxNTcsIDQ1LjkzMDk0NDk2NzA3MzVdLCBbLTY2LjY1NjcyNzgzMDE2NjgsIDQ1LjkzMTMwMTEwMjI2OTVdLCBbLTY2LjY2MDkzMTk0NTY5NjUsIDQ1LjkzMzIyNTQ0MjM2MTddLCBbLTY2LjY2MTM3MjEyMDE4NTcsIDQ1LjkzMzU5NDA1ODMzMDddLCBbLTY2LjY2MTYwNTY4MjE1OTYsIDQ1LjkzNDAzNzY0Mzc5MDhdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDUyLCAiTmVpZ2hib3VyaCI6ICJLbm93bGVkZ2UgUGFyayIsICJPQkpFQ1RJRCI6IDUyLCAiU2hhcGVfQXJlYSI6IDE2MTkxNS41NDI0MDUsICJTaGFwZV9MZW5nIjogMjI3OC41NTA5NTgyMiwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmZmZmIyIiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni43MjMwODYzODAyMDQ3LCA0NS45Nzc5MTAwNzA5MDUyXSwgWy02Ni43MjAxMTI5NTY2MTQzLCA0NS45Nzc3NjAyNDU1ODU4XSwgWy02Ni43MTcyNjUyOTcxNjM3LCA0NS45ODE1NTU2OTUzOTU1XSwgWy02Ni43MTcxOTM0MzE5NDA5LCA0NS45ODIwMzAxMDgzMjg1XSwgWy02Ni43MTczMTAyMTI5Mjc5LCA0NS45ODI0MDQ2NDE5ODMxXSwgWy02Ni43MTc5NzQ5NjYyMzgxLCA0NS45ODMwMDM4OTA1NjAzXSwgWy02Ni43MTg3MjA1Njc5MjM5LCA0NS45ODMyMzQ4NDkyMTc3XSwgWy02Ni43MTk0MDMyODc1Mzk5LCA0NS45ODMyNDEwOTEzMzAyXSwgWy02Ni43MjAwNTAwNzQ1NDQ0LCA0NS45ODMwNzg3OTYxNzY0XSwgWy02Ni43MjA2NTE5NDU3ODQ4LCA0NS45ODI2OTE3ODI3MzU3XSwgWy02Ni43MjQ0NTE4MTk0MzY2LCA0NS45Nzc5Nzg3NDA3MDc4XSwgWy02Ni43MjMwODYzODAyMDQ3LCA0NS45Nzc5MTAwNzA5MDUyXV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiA1MywgIk5laWdoYm91cmgiOiAiRGlhbW9uZCBTdHJlZXQiLCAiT0JKRUNUSUQiOiA1MywgIlNoYXBlX0FyZWEiOiAxODk3MTAuNjE2MjY3LCAiU2hhcGVfTGVuZyI6IDE4MzAuMTM3MjM3MTIsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlZDk3NiIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNzEyMTQ0OTAwMDQ0MiwgNDUuOTc3OTEwMDcwOTA1Ml0sIFstNjYuNzEyMTg5ODE1ODA4NCwgNDUuOTc3MjY3MDY3NzEyNF0sIFstNjYuNzExODMwNDg5Njk0NywgNDUuOTc2NTYxNjI4NDM1OF0sIFstNjYuNzExMDQ4OTU1Mzk3NiwgNDUuOTc2MzExOTEzMjYzOV0sIFstNjYuNzEwMDI0ODc1OTczNywgNDUuOTc2MjMwNzU1NTkwNl0sIFstNjYuNzA5MDI3NzQ2MDA4MywgNDUuOTc2MzkzMDcwODE4M10sIFstNjYuNzA4MzA5MDkzNzgxLCA0NS45NzY3MzAxODU1NDAyXSwgWy02Ni43MDc2MjYzNzQxNjUxLCA0NS45Nzc0NDE4NjU0MzU4XSwgWy02Ni43MDczNTY4Nzk1Nzk4LCA0NS45NzgxNTk3Nzg4NzAyXSwgWy02Ni43MTIxNDQ5MDAwNDQyLCA0NS45Nzc5MTAwNzA5MDUyXV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiA1NCwgIk5laWdoYm91cmgiOiAiR3Jhc3NlIENpcmNsZSIsICJPQkpFQ1RJRCI6IDU0LCAiU2hhcGVfQXJlYSI6IDYwOTMyLjA1OTQ3MTksICJTaGFwZV9MZW5nIjogMTAwMS4yNzE2MDk0MywgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmZmZmIyIiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni42NTQxNDk2NjUzMDE0LCA0Ni4wMDIwNTc4NjA2NDUxXSwgWy02Ni42NTU0MjUyNzMwMDQ5LCA0Ni4wMDI0MTM1Mzg5NDQ0XSwgWy02Ni42NTY3OTA3MTIyMzY3LCA0Ni4wMDI0Mzg0OTg3MzkyXSwgWy02Ni42NTgwOTMyNjkzOTg3LCA0Ni4wMDIxMzI3NDA0NzcxXSwgWy02Ni42NTkyNzkwNDU1NzM3LCA0Ni4wMDE0Mjc2MTgwNDMyXSwgWy02Ni42NTk1MDM2MjQzOTQ4LCA0Ni4wMDEyMDI5NzUzODAzXSwgWy02Ni42NTk3MTAyMzY5MTAxLCA0NS45OTk2Njc4OTI3NzJdLCBbLTY2LjY2MDE3NzM2MDg1NzksIDQ1Ljk5Nzg1ODE4Nzg0NDZdLCBbLTY2LjY2MTI0NjM1NjA0NiwgNDUuOTk1MzkzMTQ5NzEyNF0sIFstNjYuNjU4ODU2ODM3MzkwMiwgNDUuOTk0MTc2MTkxNjY4MV0sIFstNjYuNjU2MjE1NzkwNDU0OSwgNDUuOTkzMjQwMDUxODg0OV0sIFstNjYuNjUzMzg2MDk3MzA5OSwgNDUuOTkyNjE1OTQ5ODk4N10sIFstNjYuNjUwMDI2Mzk4MTQ3MywgNDUuOTkyMzAzODk2MjY2NF0sIFstNjYuNjQ1NzUwNDE3Mzk0OSwgNDUuOTk3MjAyOTM1MjU4OF0sIFstNjYuNjQ5Njg1MDM4MzM5NCwgNDUuOTk4OTAwMzM1NDk2NV0sIFstNjYuNjUxMTk0MjA4MDE2NywgNDUuOTk5NjgwMzczMjkwMl0sIFstNjYuNjUyODAyMTkyMzc1MiwgNDYuMDAwNzkxMTI4MTI5M10sIFstNjYuNjU0MTQ5NjY1MzAxNCwgNDYuMDAyMDU3ODYwNjQ1MV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogNTUsICJOZWlnaGJvdXJoIjogIkJyb29rc2lkZSBFc3RhdGVzIiwgIk9CSkVDVElEIjogNTUsICJTaGFwZV9BcmVhIjogODQ0OTE0LjIxNjE2OCwgIlNoYXBlX0xlbmciOiAzNTc5LjU2NTQ2NDc1LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjY1ODk1NTY1MjA3MTUsIDQ1Ljk4NDM1ODQxODEzMDNdLCBbLTY2LjY1ODU2OTM3NjQ5OTMsIDQ1Ljk4NDM4MzM4NjA2OTRdLCBbLTY2LjY1Njk3OTM1ODQ0NjQsIDQ1Ljk4NjI4NzE1ODI1NzldLCBbLTY2LjY1NjA0NTExMDU1MDksIDQ1Ljk4ODA5NzI0MTU4NTldLCBbLTY2LjY1NTU5NTk1MjkwODksIDQ1Ljk4OTcxMzc4MzIxMTFdLCBbLTY2LjY1NTI2MzU3NjI1MzcsIDQ1Ljk4OTc2MzcxNDI0NzFdLCBbLTY2LjY1OTEzNTMxNTEyODMsIDQ1Ljk4OTM4OTIzMDM3OTJdLCBbLTY2LjY2NTE5ODk0MzI5NjEsIDQ1Ljk4OTYyNjQwMzc4OTddLCBbLTY2LjY2NjEyNDIwODAzODcsIDQ1Ljk5MjI5NzY1NTE3NThdLCBbLTY2LjY2NjM3NTczNjMxODMsIDQ1Ljk5MjY2NTg3ODMxNjZdLCBbLTY2LjY2Njg2OTgwOTcyNDUsIDQ1Ljk5MzA0MDM0MDAxNTFdLCBbLTY2LjY2ODcxMTM1NjA1NywgNDUuOTkyNjU5NjM3MjY2OF0sIFstNjYuNjcwNjg3NjQ5NjgyMSwgNDUuOTkxOTEwNzA2MTg0Nl0sIFstNjYuNjcyMTYwODg2NzQ4LCA0NS45OTEwNDk0MjI5MTExXSwgWy02Ni42NzM1NDQyOTIyODU2LCA0NS45ODk4MTk4ODY2MDg4XSwgWy02Ni42NzM4MDQ4MDM3MTgsIDQ1Ljk4OTEwODM2NTgxNTZdLCBbLTY2LjY3Mzc4NjgzNzQxMjMsIDQ1Ljk4ODIyODMxNDI4NzNdLCBbLTY2LjY3MzcwNTk4OTAzNjcsIDQ1Ljk4Nzk0MTIwMjI1MV0sIFstNjYuNjczMDY4MTg1MTg1LCA0NS45ODc1MjMwMTQ2NjQ0XSwgWy02Ni42NzMyMDI5MzI0Nzc2LCA0NS45ODcyMDQ2OTA2NTI1XSwgWy02Ni42NzM2NzkwMzk1NzgyLCA0NS45ODY4MzY0MzExNzgzXSwgWy02Ni42NzM3Njg4NzExMDY2LCA0NS45ODY2MzA0NTQ0NzE4XSwgWy02Ni42NzM1MTczNDI4MjcsIDQ1Ljk4NjIzMDk4MjMxMTFdLCBbLTY2LjY3MzA1OTIwMjAzMjEsIDQ1Ljk4NTg2ODk1ODE3NTRdLCBbLTY2LjY3MjczNTgwODUyOTksIDQ1Ljk4NTg0Mzk5MDkwNjRdLCBbLTY2LjY3MTUxNDA5OTc0MzQsIDQ1Ljk4NjI1NTk0OTQwNTZdLCBbLTY2LjY2OTUzNzgwNjExODQsIDQ1Ljk4NjY0MjkzNzkzMDRdLCBbLTY2LjY2OTA0MzczMjcxMjEsIDQ1Ljk4NjM4MDc4NDcwOTJdLCBbLTY2LjY2ODA5MTUxODUxMDksIDQ1Ljk4NTIwNzMyMTc0MV0sIFstNjYuNjY3NDk4NjMwNDIzNCwgNDUuOTg1MDgyNDgzNzkxMV0sIFstNjYuNjY2NTM3NDMzMDY5NCwgNDUuOTg1NDE5NTQ1NjA5N10sIFstNjYuNjY1OTM1NTYxODI5MSwgNDUuOTg1NDM4MjcxMjA2MV0sIFstNjYuNjY1NTY3MjUyNTYyNiwgNDUuOTg1MjYzNDk4NzI2Nl0sIFstNjYuNjY1MjQzODU5MDYwMywgNDUuOTg0NzM5MTc3OTc3NF0sIFstNjYuNjY0NTYxMTM5NDQ0NCwgNDUuOTg0MjY0Nzg4MjU4NV0sIFstNjYuNjYzOTk1MjAwODE1NCwgNDUuOTg0NDc3MDE1NzQwNV0sIFstNjYuNjY0MjI4NzYyNzg5MiwgNDUuOTg0ODc2NTAwNTU4NF0sIFstNjYuNjY0MzM2NTYwNjIzMywgNDUuOTg1NjMxNzY4NjY0OF0sIFstNjYuNjYzMDk2ODg1NTMxMiwgNDUuOTg1NzQ0MTIxNzE3Nl0sIFstNjYuNjYxODMwMjYwOTgwNiwgNDUuOTg1NTMxODk5MDkzMl0sIFstNjYuNjU4OTU1NjUyMDcxNSwgNDUuOTg0MzU4NDE4MTMwM11dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogNTYsICJOZWlnaGJvdXJoIjogIldpbGxpYW1zIC8gSGF3a2lucyBBcmVhIiwgIk9CSkVDVElEIjogNTYsICJTaGFwZV9BcmVhIjogNzY1NTYxLjg3NTM4NiwgIlNoYXBlX0xlbmciOiA0NTExLjgwNTA3NjI4LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjY2MDM1NzAyMzkxNDcsIDQ1Ljk4OTQwNzk1NDYzMjhdLCBbLTY2LjY1ODgyOTg4NzkzMTcsIDQ1Ljk4OTQwMTcxMzIxNTZdLCBbLTY2LjY1Njk3MDM3NTI5MzYsIDQ1Ljk4OTU1MTUwNzAzMzFdLCBbLTY2LjY1MTc2OTEyOTc5ODUsIDQ1Ljk5MDM1NjY0MTg1NjNdLCBbLTY2LjY1MDAyNjM5ODE0NzMsIDQ1Ljk5MjMwMzg5NjI2NjRdLCBbLTY2LjY1MzAwODgwNDg5MDYsIDQ1Ljk5MjU1OTc4MDM3NDhdLCBbLTY2LjY1NTQ3OTE3MTkyMTksIDQ1Ljk5MzA0NjU4MTAyMTldLCBbLTY2LjY1NzgzMjc1Nzk2NjMsIDQ1Ljk5Mzc3MDUzMzAzOTZdLCBbLTY2LjY2MDAyNDY0NzI1OTYsIDQ1Ljk5NDcxMjkwNDY2ODNdLCBbLTY2LjY2MDYyNjUxODQ5OTksIDQ1Ljk5MzQzOTc2MzAzNDFdLCBbLTY2LjY2MDY2MjQ1MTExMTMsIDQ1Ljk5Mjk5MDQxMTkzNV0sIFstNjYuNjYwMzU3MDIzOTE0NywgNDUuOTg5NDA3OTU0NjMyOF1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogNTcsICJOZWlnaGJvdXJoIjogIk1jS25pZ2h0IiwgIk9CSkVDVElEIjogNTcsICJTaGFwZV9BcmVhIjogMjg3OTU2LjI4MTQ3OCwgIlNoYXBlX0xlbmciOiAyMzYwLjg0Nzc2NjYxLCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjY2MDAyNDY0NzI1OTYsIDQ1Ljk5NDcxMjkwNDY2ODNdLCBbLTY2LjY2MTI0NjM1NjA0NiwgNDUuOTk1MzkzMTQ5NzEyNF0sIFstNjYuNjYyNDU5MDgxNjc5NSwgNDUuOTk0NjU2NzM3MjcyNl0sIFstNjYuNjY0MTExOTgxODAyMywgNDUuOTkzODY0MTQ2ODMzMV0sIFstNjYuNjY1ODkwNjQ2MDY0OSwgNDUuOTkzMjIxMzI4OTI3N10sIFstNjYuNjY2ODY5ODA5NzI0NSwgNDUuOTkzMDQwMzQwMDE1MV0sIFstNjYuNjY2Mzc1NzM2MzE4MywgNDUuOTkyNjY1ODc4MzE2Nl0sIFstNjYuNjY2MTI0MjA4MDM4NywgNDUuOTkyMjk3NjU1MTc1OF0sIFstNjYuNjY1MTk4OTQzMjk2MSwgNDUuOTg5NjI2NDAzNzg5N10sIFstNjYuNjYwMzU3MDIzOTE0NywgNDUuOTg5NDA3OTU0NjMyOF0sIFstNjYuNjYwNjYyNDUxMTExMywgNDUuOTkyOTkwNDExOTM1XSwgWy02Ni42NjA2MjY1MTg0OTk5LCA0NS45OTM0Mzk3NjMwMzQxXSwgWy02Ni42NjAwMjQ2NDcyNTk2LCA0NS45OTQ3MTI5MDQ2NjgzXV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiA1OCwgIk5laWdoYm91cmgiOiAiU2hhZG93b29kIEVzdGF0ZXMiLCAiT0JKRUNUSUQiOiA1OCwgIlNoYXBlX0FyZWEiOiAyMjEzMDkuNDY3NzU3LCAiU2hhcGVfTGVuZyI6IDIwMTkuNzYwNTAwMzIsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlZDk3NiIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjMxODcxNDQ2MjU1MiwgNDUuOTg4MTUzNDE1NjM4OF0sIFstNjYuNjMzNDQzNDk4MDAyNSwgNDUuOTg4MDcyMjc1MzIxOV0sIFstNjYuNjM0NzczMDA0NjIzLCA0NS45ODgyNzgyNDY2NjMzXSwgWy02Ni42MzU5NzY3NDcxMDM3LCA0NS45ODg3MDg5MTE1MzY5XSwgWy02Ni42MzcxODk0NzI3MzcyLCA0NS45ODk0MjY2Nzg4OF0sIFstNjYuNjM1OTU4NzgwNzk4LCA0NS45ODgxNjU4OTg3NTM5XSwgWy02Ni42MzUyOTQwMjc0ODc3LCA0NS45ODY3NjE1MzA2NDY0XSwgWy02Ni42MzUwNTE0ODIzNjEsIDQ1Ljk4MjQyMzM2ODU5OTNdLCBbLTY2LjYzNTIwNDE5NTk1OTMsIDQ1Ljk4MTExODczMjUxODddLCBbLTY2LjYzNTgxNTA1MDM1MjUsIDQ1Ljk3OTU1MTg4MDEzNl0sIFstNjYuNjM2ODEyMTgwMzE3OSwgNDUuOTc4MDk3MzUxOTg0NV0sIFstNjYuNjM3ODAwMzI3MTMwNCwgNDUuOTc3MDExMTEyOTA3NV0sIFstNjYuNjM4MTIzNzIwNjMyNywgNDUuOTc2OTExMjI3Nzg0Nl0sIFstNjYuNjM4NTk5ODI3NzMzMywgNDUuOTc2OTczNjU2MDA3NV0sIFstNjYuNjM3ODk5MTQxODExNywgNDUuOTc2NzU1MTU2OTE5NV0sIFstNjYuNjQwMjE2Nzk1MjQ0NywgNDUuOTczNTA4NzgzMTk1Ml0sIFstNjYuNjQxNDU2NDcwMzM2OCwgNDUuOTcxMDMwMTczNjA3XSwgWy02Ni42Mzc2NjU1Nzk4Mzc4LCA0NS45Njk5NzUwMTM5NDk5XSwgWy02Ni42MzUxNzcyNDY1MDA4LCA0NS45Njg5OTQ3NTg4NjA4XSwgWy02Ni42MzQ5MDc3NTE5MTU2LCA0NS45NjkwMTk3MzM3MjgxXSwgWy02Ni42MzMzODk1OTkwODU0LCA0NS45NzAyNDM0ODg0MzJdLCBbLTY2LjYzMjMzODU3MDIwMywgNDUuOTcxNTQyMTM3MzIyXSwgWy02Ni42MzM4OTI2NTU2NDQ1LCA0NS45NzE5NDE3MTU0Njk4XSwgWy02Ni42MzQwNjMzMzU1NDg1LCA0NS45NzI3OTcwNTI3NTIyXSwgWy02Ni42MjM4MzE1MjQ0NjI0LCA0NS45ODUyMDczMjE3NDFdLCBbLTY2LjYyNTc4OTg1MTc4MTgsIDQ1Ljk4NTY4MTcwMzM4MzFdLCBbLTY2LjYyNzI5MDAzODMwNjIsIDQ1Ljk4NjE2ODU2NDUyNTZdLCBbLTY2LjYyOTQ5OTg5MzkwNTIsIDQ1Ljk4NzUxNjc3MzAzNDddLCBbLTY2LjYzMDY0MDc1NDMxNiwgNDUuOTg3OTE2MjM1OTE2Nl0sIFstNjYuNjMxODcxNDQ2MjU1MiwgNDUuOTg4MTUzNDE1NjM4OF1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogNTksICJOZWlnaGJvdXJoIjogIk5vcnRoIERldm9uIiwgIk9CSkVDVElEIjogNTksICJTaGFwZV9BcmVhIjogMTIzNzk1Ni44MTg4NiwgIlNoYXBlX0xlbmciOiA2MTg5LjY4NjI2MzUyLCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZDhkM2MiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjYyMDUxNjc0MTA2NCwgNDUuOTcwNTE4MjA1MTU5Nl0sIFstNjYuNjE4NjkzMTYxMDM3MiwgNDUuOTcxOTQxNzE1NDY5OF0sIFstNjYuNjE3MTU3MDQxOTAxNCwgNDUuOTcyODI4MjY5MTkxNV0sIFstNjYuNjE1NDIzMjkzNDAzLCA0NS45NzM1MDg3ODMxOTUyXSwgWy02Ni42MTM1MzY4MzEzMDY0LCA0NS45NzM5NTgyOTI0NDY1XSwgWy02Ni42MTI5ODg4NTg5ODMxLCA0NS45NzQ4MDczNTU1MjJdLCBbLTY2LjYxMjEwODUxMDAwNDYsIDQ1Ljk3NTM0NDI1NjMzNjZdLCBbLTY2LjYxMDgyMzkxOTE0ODMsIDQ1Ljk3NTU5Mzk3NTg3MjFdLCBbLTY2LjYwNzY5Nzc4MTk1OTYsIDQ1Ljk3NTQ1MDM4NzI3NjddLCBbLTY2LjYwNjY2NDcxOTM4MjksIDQ1Ljk3NjEzNzExMTk3MzZdLCBbLTY2LjYwNTgyOTI4NjE2ODYsIDQ1Ljk3NjkzNjE5OTA4MjJdLCBbLTY2LjYwNTIwMDQ2NTQ2OTgsIDQ1Ljk3NzgyODkxNTU3NDJdLCBbLTY2LjYwNDg3NzA3MTk2NzUsIDQ1Ljk3ODU4NDI3OTgyNjJdLCBbLTY2LjYwNDY3OTQ0MjYwNDksIDQ1Ljk3OTc3MDM2ODE4ODRdLCBbLTY2LjYwNjU5Mjg1NDE2MDEsIDQ1Ljk4MDYxMzA5OTc0MjldLCBbLTY2LjYwODAwMzIwOTE1NjIsIDQ1Ljk4MTU0OTQ1MzA5M10sIFstNjYuNjA4Nzc1NzYwMzAwNSwgNDUuOTgyMzA0NzY2NTg5Nl0sIFstNjYuNjA5NTkzMjI3MjA5MSwgNDUuOTgzNzA5MjQ3NzYyMl0sIFstNjYuNjEwMTIzMjMzMjI2NywgNDUuOTg1NDQ0NTEzMDcwMl0sIFstNjYuNjEwMjkzOTEzMTMwNywgNDUuOTg3Nzk3NjQ1Njc0NF0sIFstNjYuNjEwMDk2MjgzNzY4MiwgNDUuOTg4NjA5MDQ3NTE2OF0sIFstNjYuNjA5NTc1MjYwOTAzNCwgNDUuOTg5MjE0NDcwMzczOF0sIFstNjYuNjExOTM3ODMwMTAwNiwgNDUuOTkwMjk0MjI4NzIyOV0sIFstNjYuNjE0MTM4NzAyNTQ2NywgNDUuOTkwOTkzMjUxNzk3Ml0sIFstNjYuNjIxNzkyMzQ4NzY3NCwgNDUuOTgxODkyNzc4Njg3XSwgWy02Ni42MjkzMTEyNDc2OTU1LCA0NS45NzQyMjA1MDQ0OTE1XSwgWy02Ni42MjkzNDcxODAzMDY5LCA0NS45NzQwMDE5OTQ1NDAyXSwgWy02Ni42Mjg2Mzc1MTEyMzI0LCA0NS45NzM5MDgzNDcxNTQzXSwgWy02Ni42MjY3NjkwMTU0NDE1LCA0NS45NzMwMjE4MTA3MjI0XSwgWy02Ni42MjU4MDc4MTgwODc1LCA0NS45NzI5MjgxNjE2NzldLCBbLTY2LjYyNTIxNDkyOTk5OTksIDQ1Ljk3MjY5MDkxNjcyN10sIFstNjYuNjI0OTgxMzY4MDI2MSwgNDUuOTcyOTY1NjIxMzE1NF0sIFstNjYuNjIzNzk1NTkxODUxLCA0NS45NzI3MDk2NDY2Mjg2XSwgWy02Ni42MjA1MTY3NDEwNjQsIDQ1Ljk3MDUxODIwNTE1OTZdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDYwLCAiTmVpZ2hib3VyaCI6ICJOb3J0aCBEZXZvbiIsICJPQkpFQ1RJRCI6IDYwLCAiU2hhcGVfQXJlYSI6IDIwNDI4ODUuMzc0OTcsICJTaGFwZV9MZW5nIjogNjQ4MS4zOTQyODA2NywgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmQ4ZDNjIiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni41OTY4NTUxMTY0ODAzLCA0NS45MTQ5ODUyNjQzMDI1XSwgWy02Ni41OTU0NzE3MTA5NDI3LCA0NS45MTUyNjY1MDQ3NTExXSwgWy02Ni41OTQyMzIwMzU4NTA3LCA0NS45MTU3Nzg5ODM2ODEzXSwgWy02Ni41OTMyMDc5NTY0MjY4LCA0NS45MTY0OTE0NDY1MjU4XSwgWy02Ni41OTI1NzkxMzU3Mjc5LCA0NS45MTcyMDM5MDAyMjI5XSwgWy02Ni41OTQzMzA4NTA1MzE5LCA0NS45MTg1Mjg3ODk3OTM1XSwgWy02Ni41OTk0NTEyNDc2NTE0LCA0NS45MjE1OTA5MTM1MDAzXSwgWy02Ni42MDA3NzE3NzExMTksIDQ1LjkyMDkwMzUxMjY4NDddLCBbLTY2LjYwMjE0NjE5MzUwMzcsIDQ1LjkxOTkxNjE0MDI0NzhdLCBbLTY2LjYwMzI2MDEwNDQ1NjEsIDQ1LjkxODc3ODc2NTQxMDRdLCBbLTY2LjYwNDA3NzU3MTM2NDYsIDQ1LjkxNzUyMjYyNjU0N10sIFstNjYuNTk2ODU1MTE2NDgwMywgNDUuOTE0OTg1MjY0MzAyNV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogNjEsICJOZWlnaGJvdXJoIjogIldlc2JldHQgLyBDYXNlIiwgIk9CSkVDVElEIjogNjEsICJTaGFwZV9BcmVhIjogMzY1OTI1LjM0MzM0LCAiU2hhcGVfTGVuZyI6IDIzNjguNTc5NzI5NzgsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZmZmZiMiIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNzA2MTQ0MTUzOTQ2MywgNDUuOTM5MDk4MDE1NTEzMl0sIFstNjYuNzA0NjA4MDM0ODEwNCwgNDUuOTM4NzkxOTA3MzgzNV0sIFstNjYuNzA0MTA0OTc4MjUxMywgNDUuOTM5MzY2NjM5NjIyNV0sIFstNjYuNzAyMjM2NDgyNDYwMywgNDUuOTQwNzcyMjA5NjcxNl0sIFstNjYuNjk5MjI3MTI2MjU4NSwgNDUuOTQ0NjEzOTE5MzM4OV0sIFstNjYuNjk5Njc2MjgzOTAwNiwgNDUuOTQ0ODUxMjg0NTM3MV0sIFstNjYuNjk5Mzk3ODA2MTYyNSwgNDUuOTQ1MDUxMTcwMjMxNV0sIFstNjYuNjk5NzY2MTE1NDI5LCA0NS45NDUyNTEwNTUyMDUyXSwgWy02Ni42OTU2MjQ4ODE5NjkyLCA0NS45NDgyNjE3MzU0MzVdLCBbLTY2LjY5NTAxNDAyNzU3NiwgNDUuOTQ5ODYwNzAyNDMxNl0sIFstNjYuNjk1NTUzMDE2NzQ2NSwgNDUuOTQ5ODYwNzAyNDMxNl0sIFstNjYuNjk1NzIzNjk2NjUwNSwgNDUuOTUwNzE2MzgwNjY1OV0sIFstNjYuNjk5ODkxODc5NTY4OCwgNDUuOTUwMzQxNjMyNzAwMV0sIFstNjYuNzAwMjYwMTg4ODM1MywgNDUuOTUwNzY2MzQ2ODY5OV0sIFstNjYuNzAxMzU2MTMzNDgxOSwgNDUuOTUwNTc4OTczMzcyN10sIFstNjYuNzA1MzUzNjM2NDk2MiwgNDUuOTUwMzg1MzUzNDI2N10sIFstNjYuNzA4NjQxNDcwNDM2MSwgNDUuOTUwMDY2ODE1OTE0OF0sIFstNjYuNzEwMjc2NDA0MjUzMiwgNDUuOTQ2ODM3NjE2NjE5Ml0sIFstNjYuNzExNzQwNjU4MTY2MywgNDUuOTQyMzAyNjc4NzU3NF0sIFstNjYuNzA4NDI1ODc0NzY3OSwgNDUuOTQxNzQ2NzE3MzIyNV0sIFstNjYuNzA5MTA4NTk0MzgzOCwgNDUuOTM5ODM1MTY2OTMxM10sIFstNjYuNzA2MTQ0MTUzOTQ2MywgNDUuOTM5MDk4MDE1NTEzMl1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogNjIsICJOZWlnaGJvdXJoIjogIlNlcmVuaXR5IExhbmUiLCAiT0JKRUNUSUQiOiA2MiwgIlNoYXBlX0FyZWEiOiAxMDQwMDA1LjkxNTk5LCAiU2hhcGVfTGVuZyI6IDQ0NTguMTQyMjI5MiwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmZmZmIyIiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni43MzE4NjI5MjA1MzA2LCA0NS45NjUyNzMzNzc3ODg3XSwgWy02Ni43MzEzNjg4NDcxMjQzLCA0NS45Njc4OTU4NTM1NTA0XSwgWy02Ni43MzU2NjI3OTQxODI0LCA0NS45Njc2NTg1ODcwNDIyXSwgWy02Ni43MzU5MzIyODg3Njc3LCA0NS45Njc3MzM1MTM0MTc3XSwgWy02Ni43MzYxMDI5Njg2NzE2LCA0NS45Njc1ODM2NjA1NjUyXSwgWy02Ni43MzcwMjgyMzM0MTQzLCA0NS45Njc1NTg2ODUwNTA0XSwgWy02Ni43NDI3Njg0NjgwNzk4LCA0NS45Njc2Mzk4NTU0MzI0XSwgWy02Ni43NDUyNjU3ODQ1Njk3LCA0NS45NjczMjc2NjEwMDQ0XSwgWy02Ni43NDU1MTczMTI4NDkyLCA0NS45NjcxNzc4MDcwNTRdLCBbLTY2Ljc0NjA4MzI1MTQ3ODIsIDQ1Ljk2NzEzNDA5OTU3NTVdLCBbLTY2Ljc0NjQ5NjQ3NjUwODksIDQ1Ljk2NzMwODkyOTI4MjhdLCBbLTY2Ljc0NjE4MjA2NjE1OTUsIDQ1Ljk2NTgyMjg1OTE4Ml0sIFstNjYuNzQ1ODk0NjA1MjY4NSwgNDUuOTY1NTIzMTQyNzM0XSwgWy02Ni43NDUzNzM1ODI0MDM4LCA0NS45NjUzMzU4MTkxMzA2XSwgWy02Ni43NDUyMTE4ODU2NTI2LCA0NS45NjUxMzYwMDY1ODg3XSwgWy02Ni43NDMzMTY0NDA0MDMxLCA0NS45NjU1MTA2NTQ1MTM1XSwgWy02Ni43NDIxMTI2OTc5MjI0LCA0NS45NjU1MTA2NTQ1MTM1XSwgWy02Ni43NDA2MjE0OTQ1NTA4LCA0NS45NjUzNjA3OTU2NDc2XSwgWy02Ni43Mzg5MDU3MTIzNTgxLCA0NS45NjQ5NzM2NTgzNjc4XSwgWy02Ni43Mzc1OTQxNzIwNDMzLCA0NS45NjQ4MjM3OTgwNDkzXSwgWy02Ni43MzU5ODYxODc2ODQ3LCA0NS45NjQ0OTI4NTUwNzY0XSwgWy02Ni43MzE3OTEwNTUzMDc5LCA0NS45NjMwNjI5MDg5Mzk3XSwgWy02Ni43MzIzMTIwNzgxNzI3LCA0NS45NjM1NDk5Njg5NzM5XSwgWy02Ni43MzI1MTg2OTA2ODgsIDQ1Ljk2NDE0MzE3NzMzNDRdLCBbLTY2LjczMjM3NDk2MDI0MjUsIDQ1Ljk2NDc0MjYyMzU0MDhdLCBbLTY2LjczMTg2MjkyMDUzMDYsIDQ1Ljk2NTI3MzM3Nzc4ODddXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDYzLCAiTmVpZ2hib3VyaCI6ICJNb250ZWl0aCAvIFRhbGlzbWFuIiwgIk9CSkVDVElEIjogNjMsICJTaGFwZV9BcmVhIjogMzQyMjk4LjIxMDU3NSwgIlNoYXBlX0xlbmciOiAzMTU5LjE2MDQ1NzI3LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2Ljc0OTU0MTc2NTMyMjEsIDQ1Ljk2NzUwODczMzk4N10sIFstNjYuNzUwOTg4MDUyOTI5NSwgNDUuOTY3OTIwODI4OTEzMl0sIFstNjYuNzUzMjk2NzIzMjA5NywgNDUuOTY4Mjk1NDU4MDAzOV0sIFstNjYuNzU1NTc4NDQ0MDMxNCwgNDUuOTY5MDE5NzMzNzI4MV0sIFstNjYuNzU1NTg3NDI3MTg0MiwgNDUuOTY0ODIzNzk4MDQ5M10sIFstNjYuNzQ5NjEzNjMwNTQ0OCwgNDUuOTY0NDgwMzY2NjIzNl0sIFstNjYuNzQ5NTQxNzY1MzIyMSwgNDUuOTY3NTA4NzMzOTg3XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiA2NCwgIk5laWdoYm91cmgiOiAiUmFpbCBTaWRlIiwgIk9CSkVDVElEIjogNjQsICJTaGFwZV9BcmVhIjogMTg0NDQ0LjU5NDM0NiwgIlNoYXBlX0xlbmciOiAxNzc2LjczNzczNTczLCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2Ljc1OTc0NjYyNjk0OTcsIDQ1Ljk1ODQzNTYyNTA0OTVdLCBbLTY2Ljc2MDAxNjEyMTUzNDksIDQ1Ljk2MzIyNTI2Mjc2MDJdLCBbLTY2Ljc1OTg1NDQyNDc4MzgsIDQ1Ljk2NTEwNDc4NTgxNF0sIFstNjYuNzY3NzQxNjMyOTc4MywgNDUuOTY1NDQxOTY5MjUwM10sIFstNjYuNzcxNTQxNTA2NjMwMiwgNDUuOTY2MDc4ODY1Njk3Ml0sIFstNjYuNzcwNTM1MzkzNTExOSwgNDUuOTU3NDQyNjc1NzE4OV0sIFstNjYuNzY1Mjk4MjE1NDA1NSwgNDUuOTU3Nzk4NjQwNzMyNV0sIFstNjYuNzY1MzA3MTk4NTU4NCwgNDUuOTU3OTExMDUwMjYxN10sIFstNjYuNzY1MDkxNjAyODkwMiwgNDUuOTU3OTIzNTQwMTk1M10sIFstNjYuNzY1MTYzNDY4MTEyOSwgNDUuOTU4NDIzMTM1MjMxM10sIFstNjYuNzY1MDY0NjUzNDMxNywgNDUuOTU4MzIzMjE2NTg0NV0sIFstNjYuNzYzNjk5MjE0MTk5OCwgNDUuOTU4NDIzMTM1MjMxM10sIFstNjYuNzYzNjA5MzgyNjcxNCwgNDUuOTU4MTEwODg4ODYxN10sIFstNjYuNzYyMDU1Mjk3MjI5OSwgNDUuOTU4MTE3MTMzODA2M10sIFstNjYuNzU5NjgzNzQ0ODc5OCwgNDUuOTU3NDA1MjA1NTg0NF0sIFstNjYuNzU5NzQ2NjI2OTQ5NywgNDUuOTU4NDM1NjI1MDQ5NV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogNjUsICJOZWlnaGJvdXJoIjogIlNpbHZlcndvb2QiLCAiT0JKRUNUSUQiOiA2NSwgIlNoYXBlX0FyZWEiOiA3Mjg1NjUuNjYyNDQ5LCAiU2hhcGVfTGVuZyI6IDM3MTAuNzUxNjMwMzMsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlZDk3NiIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjY3MDA0NTU3MDE3MiwgNDUuOTQ2MzMxNjcwODYzNV0sIFstNjYuNjc5MDk1ODgwNzQxNCwgNDUuOTQ3OTExOTU1MjU1OV0sIFstNjYuNjc5MzI5NDQyNzE1MywgNDUuOTQ3Njc0NjAzMTYzXSwgWy02Ni42NzkyNzU1NDM3OTgyLCA0NS45NDcwNjg3MjYxMDddLCBbLTY2LjY4MDU2MDEzNDY1NDUsIDQ1Ljk0NTY2MzMxNTY4NzJdLCBbLTY2LjY3MTcwMjc0NTk1MzEsIDQ1Ljk0MTg2NTQwNjE4NjddLCBbLTY2LjY3MDU4ODgzNTAwMDgsIDQ1Ljk0MTU3MTgwNjk1NDFdLCBbLTY2LjY3MDIyMDUyNTczNDMsIDQ1Ljk0MTE3MjAwOTc1NDNdLCBbLTY2LjY2OTIzMjM3ODkyMTgsIDQ1Ljk0MDg2NTkxMzA3NDddLCBbLTY2LjY1OTkxNjg0OTQyNTUsIDQ1LjkzNjYzNjYwODQzMDRdLCBbLTY2LjY1NjE3MDg3NDY5MDcsIDQ1Ljk0MDk0NzEyMjU2MjVdLCBbLTY2LjY1NzY0NDExMTc1NjcsIDQ1Ljk0MTU3MTgwNjk1NDFdLCBbLTY2LjY1NzQxOTUzMjkzNTYsIDQ1Ljk0MTkwOTEzMzU5OV0sIFstNjYuNjYyMDU0ODM5ODAxNywgNDUuOTQzNjY0NDQ4MzgyN10sIFstNjYuNjY2NTY0MzgyNTI4LCA0NS45NDU1NzU4NjY3NTAyXSwgWy02Ni42NjcwMDQ1NTcwMTcyLCA0NS45NDYzMzE2NzA4NjM1XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiA2NiwgIk5laWdoYm91cmgiOiAiUHJvc3BlY3QiLCAiT0JKRUNUSUQiOiA2NiwgIlNoYXBlX0FyZWEiOiA5NzI5MDIuODE4NTc2LCAiU2hhcGVfTGVuZyI6IDQ3ODUuNTQxMTIxMjIsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlYjI0YyIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjg5MDMxMjQ3NzgzOCwgNDUuOTQ0NDcwMjUwNDM1N10sIFstNjYuNjg5OTIwNTc5OTE1MSwgNDUuOTQ0NDk1MjM2MzU4Nl0sIFstNjYuNjkxMjE0MTUzOTI0MiwgNDUuOTQ0OTI2MjQxNzU2OV0sIFstNjYuNjkzOTQ1MDMyMzg3OSwgNDUuOTQ2NzgxNDAwNjUyMl0sIFstNjYuNzAwMTk3MzA2NzY1NCwgNDUuOTQyMjMzOTY0NzI0N10sIFstNjYuNjkzNDE1MDI2MzcwMywgNDUuOTM4NjQ4MjIzMzkzXSwgWy02Ni42ODk5NTY1MTI1MjY0LCA0NS45NDE4NDA0MTkwNzg1XSwgWy02Ni42ODkwMzEyNDc3ODM4LCA0NS45NDQ0NzAyNTA0MzU3XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiA2NywgIk5laWdoYm91cmgiOiAiTGlhbiAvIFZhbGNvcmUiLCAiT0JKRUNUSUQiOiA2NywgIlNoYXBlX0FyZWEiOiA0MTExOTcuOTU2MjQ0LCAiU2hhcGVfTGVuZyI6IDI1ODguMzUwMjUyMjcsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlZDk3NiIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjIwNTE2NzQxMDY0LCA0NS45NzA1MTgyMDUxNTk2XSwgWy02Ni42MjM3OTU1OTE4NTEsIDQ1Ljk3MjcwOTY0NjYyODZdLCBbLTY2LjYyNDk4MTM2ODAyNjEsIDQ1Ljk3Mjk2NTYyMTMxNTRdLCBbLTY2LjYyNTIxNDkyOTk5OTksIDQ1Ljk3MjY5MDkxNjcyN10sIFstNjYuNjI1ODA3ODE4MDg3NSwgNDUuOTcyOTI4MTYxNjc5XSwgWy02Ni42MjY3NjkwMTU0NDE1LCA0NS45NzMwMjE4MTA3MjI0XSwgWy02Ni42Mjg2Mzc1MTEyMzI0LCA0NS45NzM5MDgzNDcxNTQzXSwgWy02Ni42MjkzNDcxODAzMDY5LCA0NS45NzQwMDE5OTQ1NDAyXSwgWy02Ni42Mjk1NjI3NzU5NzUxLCA0NS45NzI3MjIxMzMyMjYyXSwgWy02Ni42MzM0Nzk0MzA2MTM4LCA0NS45Njg0ODI3NzE1OTkxXSwgWy02Ni42MzI4Nzc1NTkzNzM1LCA0NS45Njc5ODk1MTExMDI5XSwgWy02Ni42MzExMTY4NjE0MTY2LCA0NS45NjcwOTAzOTIwNjI0XSwgWy02Ni42MzA1MzI5NTY0ODE5LCA0NS45NjY1MDk3MDMyNTkxXSwgWy02Ni42MzA2NTg3MjA2MjE3LCA0NS45NjYyMjg3MjI2MjA1XSwgWy02Ni42MzA1NTk5MDU5NDA0LCA0NS45NjYwNzI2MjE2NDk5XSwgWy02Ni42MjkxNTg1MzQwOTcyLCA0NS45NjUzMDQ1OTg0Njg0XSwgWy02Ni42Mjg2NzM0NDM4NDM4LCA0NS45NjQ4MzAwNDIyMzczXSwgWy02Ni42MjY3OTU5NjQ5LCA0NS45NjU2MTA1NjAxOTg4XSwgWy02Ni42MjU4NjE3MTcwMDQ1LCA0NS45NjYxNTM3OTQyMDk1XSwgWy02Ni42MjI3ODk0Nzg3MzI4LCA0NS45Njg3NzYyMjgyOTE0XSwgWy02Ni42MjA1MTY3NDEwNjQsIDQ1Ljk3MDUxODIwNTE1OTZdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDY4LCAiTmVpZ2hib3VyaCI6ICJOb3J0aCBEZXZvbiIsICJPQkpFQ1RJRCI6IDY4LCAiU2hhcGVfQXJlYSI6IDU0NzA2Ny4yNzUzNjEsICJTaGFwZV9MZW5nIjogMzAzMC41OTE3NDE1NSwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmQ4ZDNjIiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni42NzEwNjQ5NDIxMDE0LCA0NS45NTg0NjY4NDk1ODI3XSwgWy02Ni42NzYxMTM0NzM5OTgxLCA0NS45NTY3MjQ0OTM3MzA2XSwgWy02Ni42Nzc1MTQ4NDU4NDE0LCA0NS45NTY1NjgzNjU5Nzk3XSwgWy02Ni42Nzg5MjUyMDA4Mzc0LCA0NS45NTY2NTU3OTc1NzQ0XSwgWy02Ni42ODA0NjEzMTk5NzMzLCA0NS45NTcwNjE3MjgxNzEyXSwgWy02Ni42ODA5MTA0Nzc2MTUzLCA0NS45NTc2NTUwMDYwMDIyXSwgWy02Ni42ODEzNjg2MTg0MTAyLCA0NS45NTg5NDc3MDUxNzEzXSwgWy02Ni42ODEyMzM4NzExMTc2LCA0NS45NjAyNzc4NDIzOTk2XSwgWy02Ni42ODQxMTc0NjMxNzk2LCA0NS45NjAxMDkyMzUyMjI1XSwgWy02Ni42ODQ4MTgxNDkxMDEzLCA0NS45NjAyNTkxMDgyOTQyXSwgWy02Ni42ODU0MTEwMzcxODg4LCA0NS45NjA1NTg4NTMyMjE0XSwgWy02Ni42ODUwMDY3OTUzMTA5LCA0NS45NTk2MzQ2MzQ0ODc2XSwgWy02Ni42ODQ3MjgzMTc1NzI4LCA0NS45NTg0NDgxMTQ4NjQ5XSwgWy02Ni42ODQ2ODM0MDE4MDg2LCA0NS45NTc0ODYzOTA4NDM3XSwgWy02Ni42ODQ4NTQwODE3MTI2LCA0NS45NTYyODczMzQ5MTk2XSwgWy02Ni42ODUyMjIzOTA5NzkxLCA0NS45NTUxMzgyMTUzMTI1XSwgWy02Ni42ODU3NzkzNDY0NTUzLCA0NS45NTQwNTc3NzEzMzg3XSwgWy02Ni42ODY1NjA4ODA3NTI1LCA0NS45NTMwNTg0OTgwNDY3XSwgWy02Ni42ODc1NTgwMTA3MTc4LCA0NS45NTIxNDY2NDU0NDU2XSwgWy02Ni42ODQzNTEwMjUxNTM1LCA0NS45NTEzNzg0MjkyMTMzXSwgWy02Ni42ODI2ODkxNDE4Nzc5LCA0NS45NTExNTk4MjkxNTI0XSwgWy02Ni42ODA1NjkxMTc4MDc0LCA0NS45NTEwNDc0MDU5MjgyXSwgWy02Ni42NzgyNTE0NjQzNzQzLCA0NS45NTEzNTk2OTIwOTldLCBbLTY2LjY3NjA3NzU0MTM4NjgsIDQ1Ljk1MTk5Njc1MDQzMTZdLCBbLTY2LjY3NDY1ODIwMzIzNzksIDQ1Ljk1MjYzMzgwMTQ0MTVdLCBbLTY2LjY3MzM4MjU5NTUzNDQsIDQ1Ljk1MzQwODI0NTc0ODRdLCBbLTY2LjY3MjI5NTYzNDA0MDYsIDQ1Ljk1NDMwNzU4Njg0NjVdLCBbLTY2LjY3MTM5NzMxODc1NjUsIDQ1Ljk1NTMwNjgzNzYxNjJdLCBbLTY2LjY3MTAxMTA0MzE4NDMsIDQ1Ljk1NTk5MzgxMjA2ODVdLCBbLTY2LjY3MDc5NTQ0NzUxNjIsIDQ1Ljk1NjgxMTkyNTA3ODldLCBbLTY2LjY3MDgxMzQxMzgyMTgsIDQ1Ljk1NzY0ODc2MTAwNTRdLCBbLTY2LjY3MTA2NDk0MjEwMTQsIDQ1Ljk1ODQ2Njg0OTU4MjddXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDY5LCAiTmVpZ2hib3VyaCI6ICJIYW53ZWxsIE5vcnRoIiwgIk9CSkVDVElEIjogNjksICJTaGFwZV9BcmVhIjogNzQ3MjUxLjQ0NDgxOCwgIlNoYXBlX0xlbmciOiA0MzAxLjQzNDc0MDQ3LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjYxODEwOTI1NjEwMjUsIDQ1LjkwODIxMDA2MzY4MjNdLCBbLTY2LjYxODAwMTQ1ODI2ODUsIDQ1LjkwODI0MTMxNjUwNjRdLCBbLTY2LjYxOTI0MTEzMzM2MDUsIDQ1LjkwODQyMjU4MjUzODddLCBbLTY2LjYyMTE0NTU2MTc2MjksIDQ1LjkwODQ4NTA4NzkyOTldLCBbLTY2LjYyMjcwODYzMDM1NzIsIDQ1LjkwODM0MTMyNTQyNV0sIFstNjYuNjI0MjI2NzgzMTg3NCwgNDUuOTA4MDI4Nzk2OTU2XSwgWy02Ni42MjU2NTUxMDQ0ODkxLCA0NS45MDc1NTM3NTAzMTI5XSwgWy02Ni42MjY5NTc2NjE2NTExLCA0NS45MDY5Mjg2ODI3NDY2XSwgWy02Ni42MjgxMDc1MDUyMTQ4LCA0NS45MDYxNjYwOTA3ODM5XSwgWy02Ni42MjkyMzAzOTkzMiwgNDUuOTA1MDk3MTk0MjUyNV0sIFstNjYuNjMyNzUxNzk1MjMzNywgNDUuOTAwNzMzODgyNjYyXSwgWy02Ni42Mzg1OTA4NDQ1ODA1LCA0NS44OTQwNzU3MzM1NTgyXSwgWy02Ni42Mzg3NDM1NTgxNzg4LCA0NS44OTI1Njg5NDMwMzc4XSwgWy02Ni42Mzg1ODE4NjE0Mjc2LCA0NS44OTE4MTg2NTg2NTMyXSwgWy02Ni42MzgxNTk2NTMyNDQxLCA0NS44OTA5MTgzMDQwMTIzXSwgWy02Ni42MzcwMDk4MDk2ODA0LCA0NS44ODk2MzY1MjM5NjI0XSwgWy02Ni42MzYyNDYyNDE2ODg5LCA0NS44ODkwOTg3OTI3OTI0XSwgWy02Ni42MzUxNTAyOTcwNDIzLCA0NS44ODg1NDIyOTgwNzY5XSwgWy02Ni42MzMxNDcwNTM5NTg3LCA0NS44ODc5NzMyOTIwOTc0XSwgWy02Ni42MzA5OTEwOTcyNzY4LCA0NS44ODc4MzU3MjkzMzczXSwgWy02Ni42Mjg4NzEwNzMyMDYzLCA0NS44ODgxNDIxMTg2NTU1XSwgWy02Ni42MjY5NzU2Mjc5NTY4LCA0NS44ODg4Njc0NDE3MzM4XSwgWy02Ni42MjYzNDY4MDcyNTc5LCA0NS44ODkyMzYzNTI0MjQ0XSwgWy02Ni42MjQyODk2NjUyNTczLCA0NS44OTEyNjIxOTExODgyXSwgWy02Ni42MTkxNDIzMTg2NzkzLCA0NS44OTY4MzI4NjY3OTQ0XSwgWy02Ni42MTUwNjM5NjcyODk0LCA0NS45MDE4ODQxMjk4OV0sIFstNjYuNjE0NjUwNzQyMjU4NywgNDUuOTAzNDAzMTY5ODc1M10sIFstNjYuNjE0ODU3MzU0Nzc0LCA0NS45MDQ5NDA5MjExMDU0XSwgWy02Ni42MTU1NDAwNzQzOSwgNDUuOTA2MjA5ODQ2MzQzN10sIFstNjYuNjE2NjQ1MDAyMTg5NCwgNDUuOTA3MzIyNDc2MTMzN10sIFstNjYuNjE4MTA5MjU2MTAyNSwgNDUuOTA4MjEwMDYzNjgyM11dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogNzAsICJOZWlnaGJvdXJoIjogIkRvYWsgUm9hZCIsICJPQkpFQ1RJRCI6IDcwLCAiU2hhcGVfQXJlYSI6IDI1NjAxMzAuMTc2MDQsICJTaGFwZV9MZW5nIjogNjM1MC42NjEzODcwNCwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmZmZmIyIiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni42NTAzNTg3NzQ4MDI0LCA0NS45MzU3MTgyMzgyMDY5XSwgWy02Ni42NTAxNDMxNzkxMzQyLCA0NS45MzYxNTU1NTkyNTc4XSwgWy02Ni42NTAyNzc5MjY0MjY5LCA0NS45MzYzNTU0NzYzMDM4XSwgWy02Ni42NTAxNDMxNzkxMzQyLCA0NS45MzY2MDUzNzE1OTc4XSwgWy02Ni42NDU2Njk1NjkwMTkzLCA0NS45NDE5NDY2MTQyMTA2XSwgWy02Ni42NDYyMzU1MDc2NDgzLCA0NS45NDIzMzM5MTIzODA1XSwgWy02Ni42NTI0NTE4NDk0MTQ0LCA0NS45NDQ5MTk5OTUzMjU4XSwgWy02Ni42NTMzODYwOTczMDk5LCA0NS45NDM4NDU1OTg3MDJdLCBbLTY2LjY1NDYwNzgwNjA5NjMsIDQ1Ljk0MjkyNzM0Nzg3NTddLCBbLTY2LjY1NjU4NDA5OTcyMTQsIDQ1Ljk0MTk4NDA5NDc5NjldLCBbLTY2LjY1NzEzMjA3MjA0NDcsIDQ1Ljk0MTgwOTE4NTE3NzRdLCBbLTY2LjY1NzQxOTUzMjkzNTYsIDQ1Ljk0MTkwOTEzMzU5OV0sIFstNjYuNjU3NjQ0MTExNzU2NywgNDUuOTQxNTcxODA2OTU0MV0sIFstNjYuNjU2MTcwODc0NjkwNywgNDUuOTQwOTQ3MTIyNTYyNV0sIFstNjYuNjU5OTE2ODQ5NDI1NSwgNDUuOTM2NjM2NjA4NDMwNF0sIFstNjYuNjU1Nzc1NjE1OTY1NywgNDUuOTM1MzgwODczODk2OV0sIFstNjYuNjU0MTg1NTk3OTEyOCwgNDUuOTM1MTEyMjMwNDc4NV0sIFstNjYuNjUzMjUxMzUwMDE3MywgNDUuOTM1MDg3MjQwMzI2OV0sIFstNjYuNjUyMDc0NTU2OTk1MSwgNDUuOTM1MjI0Njg2MDIxM10sIFstNjYuNjUwMzU4Nzc0ODAyNCwgNDUuOTM1NzE4MjM4MjA2OV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogNzEsICJOZWlnaGJvdXJoIjogIk1vbnRvZ29tZXJ5IC8gUHJvc3BlY3QgRWFzdCIsICJPQkpFQ1RJRCI6IDcxLCAiU2hhcGVfQXJlYSI6IDY3ODI1MS4wNDI2MTgsICJTaGFwZV9MZW5nIjogMzQ4MS4zMzI4NTE0OSwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmVkOTc2IiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni41OTg2MDY4MzEyODQzLCA0NS44OTM0MzE3NTc1NDk4XSwgWy02Ni41OTAyMzQ1MzI4MzYzLCA0NS44ODQwNDYzNjY2NDYyXSwgWy02Ni41OTAzNTEzMTM4MjMyLCA0NS44ODQ0Mjc4MTU4NDUxXSwgWy02Ni41ODk5MzgwODg3OTI2LCA0NS44ODQ3NTI5ODM1ODU5XSwgWy02Ni41ODk0NjE5ODE2OTIsIDQ1Ljg4NDg0MDUyODQyMTddLCBbLTY2LjU4OTQ1Mjk5ODUzOTEsIDQ1Ljg4NTIyODIyNTMyMTldLCBbLTY2LjU4OTEyMDYyMTg4NCwgNDUuODg1MjkwNzU2ODI2Nl0sIFstNjYuNTg4NTcyNjQ5NTYwNywgNDUuODg1MDE1NjE3Njc5NF0sIFstNjYuNTg4MjY3MjIyMzY0MSwgNDUuODg1MzAzMjYzMTE5MV0sIFstNjYuNTg3ODE4MDY0NzIyLCA0NS44ODUwOTY5MDg5MzI5XSwgWy02Ni41ODcxNzEyNzc3MTc1LCA0NS44ODUyNDA3MzE2Mjg1XSwgWy02Ni41ODYyODE5NDU1ODYyLCA0NS44ODYwNjYxNDE2MzcxXSwgWy02Ni41ODU4OTU2NzAwMTQsIDQ1Ljg4NjcyODk2MjAwNzhdLCBbLTY2LjU4NjM4MDc2MDI2NzQsIDQ1Ljg4NjgxNjUwMzcyOTZdLCBbLTY2LjU4NjQ3MDU5MTc5NTgsIDQ1Ljg4NzMwNDIzMzY1NDRdLCBbLTY2LjU4Njk2NDY2NTIwMjEsIDQ1Ljg4NzY2NjkwMTg0OF0sIFstNjYuNTg2ODM4OTAxMDYyNCwgNDUuODg4MDU0NTc5MDIyOF0sIFstNjYuNTg2MzYyNzkzOTYxOCwgNDUuODg4Mjc5NjgwNjU2OF0sIFstNjYuNTg2MDIxNDM0MTUzOCwgNDUuODg4NzE3Mzc1NjY3MV0sIFstNjYuNTg2MTU2MTgxNDQ2NCwgNDUuODg5MDk4NzkyNzkyNF0sIFstNjYuNTg1NTkwMjQyODE3NCwgNDUuODg5NzkyODQwMTg2M10sIFstNjYuNTg1MDc4MjAzMTA1NSwgNDUuODkwMTMwNDgxNzI4N10sIFstNjYuNTg0ODQ0NjQxMTMxNiwgNDUuODkwMTA1NDcxMzE0NV0sIFstNjYuNTg0NTIxMjQ3NjI5MywgNDUuODg5ODY3ODcxODE3Nl0sIFstNjYuNTgzODI5NTQ0ODYwNSwgNDUuODkwMTk5MjYwMzA5OF0sIFstNjYuNTgzMDY1OTc2ODY5LCA0NS44ODk5MTc4OTI4NDg4XSwgWy02Ni41ODI3NTE1NjY1MTk2LCA0NS44OTAyNzQyOTEzOTJdLCBbLTY2LjU4MjMzODM0MTQ4ODksIDQ1Ljg5MDM4MDU4NTI1MTZdLCBbLTY2LjU4MTc2MzQxOTcwNzEsIDQ1Ljg5MDc2ODI0MzQ4NjVdLCBbLTY2LjU4MTU0NzgyNDAzODksIDQ1Ljg5MTM4NzI0MDU0MjRdLCBbLTY2LjU4MTkxNjEzMzMwNTQsIDQ1Ljg5MTU4NzMxODkyMzVdLCBbLTY2LjU4MTczNjQ3MDI0ODUsIDQ1Ljg5MTc5OTkwMTQxMzddLCBbLTY2LjU4MTIwNjQ2NDIzMDksIDQ1Ljg5MTgwNjE1MzgyNzVdLCBbLTY2LjU4MTI3ODMyOTQ1MzYsIDQ1Ljg5MjMzNzYwNjQzMzRdLCBbLTY2LjU4MDkwMTAzNzAzNDMsIDQ1Ljg5MjQzNzY0NDAwMjJdLCBbLTY2LjU4MDc2NjI4OTc0MTcsIDQ1Ljg5MjgwMDI3ODY3ODddLCBbLTY2LjU3NzM4ODYyNDI3MzQsIDQ1Ljg5NTM4MjQxOTIwODddLCBbLTY2LjU3Nzc5Mjg2NjE1MTMsIDQ1Ljg5NjcxNDA4MTU2M10sIFstNjYuNTc4MzEzODg5MDE2LCA0NS44OTc3ODkzOTEyMzg4XSwgWy02Ni41NzkzNjQ5MTc4OTg1LCA0NS44OTg0NDU4MjAwNDldLCBbLTY2LjU4MDIxODMxNzQxODQsIDQ1Ljg5ODc4MzQwODk4NjldLCBbLTY2LjU4MDMxNzEzMjA5OTYsIDQ1Ljg5OTA3MDk4MzEyOThdLCBbLTY2LjU3OTkyMTg3MzM3NDYsIDQ1Ljg5OTM4OTgxMzU5MDhdLCBbLTY2LjU3OTA5NTQyMzMxMzIsIDQ1Ljg5OTYyMTEyMDgxODZdLCBbLTY2LjU3OTA2ODQ3Mzg1NDcsIDQ1LjkwMDI1ODc3MzU5MThdLCBbLTY2LjU3ODg3OTgyNzY0NSwgNDUuOTAwNTMzODM3MjMzMl0sIFstNjYuNTc4NDM5NjUzMTU1OCwgNDUuOTAwNTcxMzQ1ODA2XSwgWy02Ni41NzgxMjUyNDI4MDY0LCA0NS45MDA0NDAwNjU2OTA0XSwgWy02Ni41ODAzODAwMTQxNjk1LCA0NS45MDI5MjgwODM2NDddLCBbLTY2LjU4MjMyOTM1ODMzNjEsIDQ1LjkwNDg0NzE1NzAwNTldLCBbLTY2LjU4NjYyMzMwNTM5NDIsIDQ1LjkwODQ4NTA4NzkyOTldLCBbLTY2LjU5NDUyODQ3OTg5NDQsIDQ1Ljg5OTQ1ODU4MDcwNTFdLCBbLTY2LjU5NDg2OTgzOTcwMjQsIDQ1Ljg5OTIxNDc2OTY0MjhdLCBbLTY2LjU5NTYzMzQwNzY5MzksIDQ1Ljg5ODc4MzQwODk4NjldLCBbLTY2LjU5NjcyMDM2OTE4NzcsIDQ1Ljg5ODM4MzMwMzM1MzhdLCBbLTY2LjU5NzY1NDYxNzA4MzEsIDQ1Ljg5ODE3Njk5Nzc2MDJdLCBbLTY2LjU5ODg2NzM0MjcxNjcsIDQ1Ljg5ODA4MzIyMjIzN10sIFstNjYuNjAwMzIyNjEzNDc3LCA0NS44OTgyMDgyNTYyMzI3XSwgWy02Ni42MDA2MzcwMjM4MjY0LCA0NS44OTkyMTQ3Njk2NDI4XSwgWy02Ni41OTk4NDY1MDYzNzY0LCA0NS44OTYyODg5NTMzODk0XSwgWy02Ni41OTg2MDY4MzEyODQzLCA0NS44OTM0MzE3NTc1NDk4XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiA3MiwgIk5laWdoYm91cmgiOiAiRnJlZGVyaWN0b24gU291dGgiLCAiT0JKRUNUSUQiOiA3MiwgIlNoYXBlX0FyZWEiOiAyNTA0MDY2Ljk0Mzk1LCAiU2hhcGVfTGVuZyI6IDc3MjIuNDc5MzQ2MDUsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZkOGQzYyIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjgwNTYwMTM0NjU0NSwgNDUuOTQ1NjU3MDY5MzM5MV0sIFstNjYuNjc5Mjc1NTQzNzk4MiwgNDUuOTQ3MDY4NzI2MTA3XSwgWy02Ni42NzkzMjk0NDI3MTUzLCA0NS45NDc2NzQ2MDMxNjNdLCBbLTY2LjY3OTA5NTg4MDc0MTQsIDQ1Ljk0NzkxMTk1NTI1NTldLCBbLTY2LjY2NzAwNDU1NzAxNzIsIDQ1Ljk0NjMzMTY3MDg2MzVdLCBbLTY2LjY2NzE3NTIzNjkyMTEsIDQ1Ljk0NzEwNjIwMzIzMDVdLCBbLTY2LjY2NzEzMDMyMTE1NjksIDQ1Ljk0NzczMDgxODIyNDJdLCBbLTY2LjY2Njg1MTg0MzQxODksIDQ1Ljk0ODQ5MjgzODk4NTNdLCBbLTY2LjY2NjQ1NjU4NDY5MzgsIDQ1Ljk0OTA2MTIyNDY5OTFdLCBbLTY2LjY2NTc2NDg4MTkyNTEsIDQ1Ljk0OTY3OTU3MTc2ODFdLCBbLTY2LjY2MDI4NTE1ODY5MTksIDQ1Ljk1NjAwMDA1NzI1MThdLCBbLTY2LjY1ODc0OTAzOTU1NjEsIDQ1Ljk1NjQxODQ4MjkyNTFdLCBbLTY2LjY1NzcwNjk5MzgyNjUsIDQ1Ljk1Njk4MDU0MjI4OThdLCBbLTY2LjY2MDExNDQ3ODc4OCwgNDUuOTU3MzczOTgwNDUzXSwgWy02Ni42NjA1MzY2ODY5NzE1LCA0NS45NTc1MzAxMDU5MzRdLCBbLTY2LjY2MTM5MDA4NjQ5MTQsIDQ1Ljk1ODE4NTgyODE1MDldLCBbLTY2LjY2MTY3NzU0NzM4MjMsIDQ1Ljk1ODkxNjQ4MDkwOTFdLCBbLTY2LjY2MzA5Njg4NTUzMTIsIDQ1Ljk1OTAxNjM5ODQ4NjFdLCBbLTY2LjY2NDQ2MjMyNDc2MzEsIDQ1Ljk1OTI3MjQzNjQ1NDldLCBbLTY2LjY2NzIyMDE1MjY4NTQsIDQ1Ljk2MDAyODA1MzgwNjFdLCBbLTY2LjY2ODYzMDUwNzY4MTQsIDQ1Ljk2MDc1ODY4MjI3MTldLCBbLTY2LjY2OTUxMDg1NjY1OTksIDQ1Ljk1OTI3MjQzNjQ1NDldLCBbLTY2LjY3MDA1ODgyODk4MzIsIDQ1Ljk1ODg1NDAzMjMzMTldLCBbLTY2LjY3MTA2NDk0MjEwMTQsIDQ1Ljk1ODQ2Njg0OTU4MjddLCBbLTY2LjY3MDc3NzQ4MTIxMDUsIDQ1Ljk1NzE0OTE1ODk4NzVdLCBbLTY2LjY3MTA4MjkwODQwNzEsIDQ1Ljk1NTgzMTQzNzA1NzVdLCBbLTY2LjY3MjA5ODAwNDY3ODEsIDQ1Ljk1NDUwMTE5MzA5MDRdLCBbLTY2LjY3MzYyNTE0MDY2MTEsIDQ1Ljk1MzI0NTg2MzE2MTRdLCBbLTY2LjY3NTQ5MzYzNjQ1MjEsIDQ1Ljk1MjIzNDA4NDAxNjZdLCBbLTY2LjY3NzkyODA3MDg3MjEsIDQ1Ljk1MTQyODM5NDgyMDVdLCBbLTY2LjY4MDU2OTExNzgwNzQsIDQ1Ljk1MTA0NzQwNTkyODJdLCBbLTY2LjY4MjY4OTE0MTg3NzksIDQ1Ljk1MTE1OTgyOTE1MjRdLCBbLTY2LjY4NTE3NzQ3NTIxNDksIDQ1Ljk1MTUyODMyNTg5OTddLCBbLTY2LjY4NzU1ODAxMDcxNzgsIDQ1Ljk1MjE0NjY0NTQ0NTZdLCBbLTY2LjY4ODA0MzEwMDk3MTIsIDQ1Ljk1MTc5Njg4OTc4MjJdLCBbLTY2LjY4OTM4MTU5MDc0NDYsIDQ1Ljk1MTgwOTM4MTA5MzldLCBbLTY2LjY5MDcwMjExNDIxMjIsIDQ1Ljk1MTk5Njc1MDQzMTZdLCBbLTY2LjY5Mjg4NTAyMDM1MjcsIDQ1Ljk1MjcwODc0ODEzNzddLCBbLTY2LjY5MzM3OTA5Mzc1ODksIDQ1Ljk1MzAyNzI3MDQ2Nl0sIFstNjYuNjkzNjM5NjA1MTkxMywgNDUuOTUzMzU4MjgxOTI2Ml0sIFstNjYuNjkzNzExNDcwNDE0LCA0NS45NTQwMTQwNTM1MDkxXSwgWy02Ni42OTMyOTgyNDUzODM0LCA0NS45NTQ3OTQ3MjM4NDc1XSwgWy02Ni42OTI1Nzk1OTMxNTYxLCA0NS45NTUwMDcwNjQyNzcxXSwgWy02Ni42OTE4NTE5NTc3NzU5LCA0NS45NTQ3OTQ3MjM4NDc1XSwgWy02Ni42OTE2ODEyNzc4NzE5LCA0NS45NTQ4Mzg0NDEwNjEzXSwgWy02Ni42OTA5MTc3MDk4ODA0LCA0NS45NTUxNDQ0NjA1OTIxXSwgWy02Ni42OTAzNjA3NTQ0MDQzLCA0NS45NTU1NzUzODMxODg3XSwgWy02Ni42ODk2MzMxMTkwMjQxLCA0NS45NTY1MzcxNDAzNzY4XSwgWy02Ni42ODgxNjg4NjUxMTEsIDQ1Ljk1OTM3ODU5ODE5MjVdLCBbLTY2LjY4NzY1NjgyNTM5OTEsIDQ1Ljk2MDAyODA1MzgwNjFdLCBbLTY2LjY4ODg3ODUzNDE4NTUsIDQ1Ljk1OTc3MjAxOTMyODldLCBbLTY2LjY5ODEyMjE5ODQ1OTEsIDQ1Ljk2MDgwODYzOTQyMl0sIFstNjYuNjk3MzQwNjY0MTYxOSwgNDUuOTYwMDc4MDExNjE0OV0sIFstNjYuNjk2Njc1OTEwODUxNiwgNDUuOTU5MDg1MDkxNzE1OF0sIFstNjYuNjk2NDYwMzE1MTgzNCwgNDUuOTU4NTU0Mjc4MTgxOV0sIFstNjYuNjk2NDk2MjQ3Nzk0OCwgNDUuOTU3NjIzNzgxMDExNV0sIFstNjYuNjk4Nzk1OTM0OTIyMiwgNDUuOTUxNzg0Mzk4NDY3N10sIFstNjYuNjk5MTczMjI3MzQxNSwgNDUuOTUxMTUzNTgzNDIzN10sIFstNjYuNzAwMjYwMTg4ODM1MywgNDUuOTUwNzY2MzQ2ODY5OV0sIFstNjYuNjk5ODkxODc5NTY4OCwgNDUuOTUwMzQxNjMyNzAwMV0sIFstNjYuNjk1NzIzNjk2NjUwNSwgNDUuOTUwNzE2MzgwNjY1OV0sIFstNjYuNjk1NjY5Nzk3NzMzNCwgNDUuOTUwNDQ3ODExNTQ3Nl0sIFstNjYuNjkzODAxMzAxOTQyNCwgNDUuOTUwNDM1MzE5OTI5MV0sIFstNjYuNjkxOTU5NzU1NjEsIDQ1Ljk1MDE0ODAxMTkyNV0sIFstNjYuNjkwMTcyMTA4MTk0NiwgNDUuOTQ5NTc5NjM3MzU1Nl0sIFstNjYuNjgwODIwNjQ2MDg2OSwgNDUuOTQ1NjEzMzQ0ODgzXSwgWy02Ni42ODA1NjAxMzQ2NTQ1LCA0NS45NDU2NTcwNjkzMzkxXV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiA3MywgIk5laWdoYm91cmgiOiAiRnJlZGVyaWN0b24gU291dGgiLCAiT0JKRUNUSUQiOiA3MywgIlNoYXBlX0FyZWEiOiAyMjI3Njg5LjMwNDczLCAiU2hhcGVfTGVuZyI6IDExMTQ4LjE5OTE3NzQsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZkOGQzYyIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjc0NzkyOTUwNTMwNSwgNDUuOTYyMjAxMTc2ODUxMl0sIFstNjYuNjc0Mjg5ODkzOTcxNCwgNDUuOTYxNzA3ODYwNDJdLCBbLTY2LjY3MzU5ODE5MTIwMjYsIDQ1Ljk2MTM3MDY1NDI1Nl0sIFstNjYuNjcyNzg5NzA3NDQ2OSwgNDUuOTYxMTg5NTYxMjA5OF0sIFstNjYuNjcxOTQ1MjkxMDc5OCwgNDUuOTYxMTc3MDcyMDEyNF0sIFstNjYuNjY5ODc5MTY1OTI2MywgNDUuOTYxNTUxNzQ2NzEwM10sIFstNjYuNjY3ODEzMDQwNzcyOSwgNDUuOTYyMjQ0ODg4MjIxOV0sIFstNjYuNjYwODUxMDk3MzIwOSwgNDUuOTYzOTgwODI2MjAzOV0sIFstNjYuNjU4NjA1MzA5MTEwNiwgNDUuOTY0MTYxOTEwMTI2NV0sIFstNjYuNjU2ODM1NjI4MDAwOSwgNDUuOTYzOTk5NTU5MDUwOV0sIFstNjYuNjU0MTU4NjQ4NDU0MywgNDUuOTYzNTgxMTkwNjI0OV0sIFstNjYuNjUyMDkyNTIzMzAwOCwgNDUuOTYzNDU2MzAzOTE1Ml0sIFstNjYuNjUxNDU0NzE5NDQ5MSwgNDUuOTYzNTYyNDU3NjM2NF0sIFstNjYuNjUxMDA1NTYxODA3LCA0NS45NjM3NjIyNzU4NTM4XSwgWy02Ni42NTA1OTIzMzY3NzYzLCA0NS45NjQxMTgyMDAyNjgzXSwgWy02Ni42NTA0MTI2NzM3MTk1LCA0NS45NjQ0Njc4NzgxNjhdLCBbLTY2LjY1MDk1MTY2Mjg5LCA0NS45NjQ5NDI0Mzc1MDE1XSwgWy02Ni42NTE1ODA0ODM1ODg4LCA0NS45NjUxOTg0NDgwODU1XSwgWy02Ni42NTIyOTAxNTI2NjMzLCA0NS45NjUzMDQ1OTg0Njg0XSwgWy02Ni42NTMwMTc3ODgwNDM0LCA0NS45NjUyNDIxNTcwOTEzXSwgWy02Ni42NTQ2NzA2ODgxNjYyLCA0NS45NjU1MDQ0MTA0MDIyXSwgWy02Ni42NTYyNTE3MjMwNjYzLCA0NS45NjU5MjkwMDgzNjg0XSwgWy02Ni42NTc3MzM5NDMyODUxLCA0NS45NjY1MDM0NTkyNjA0XSwgWy02Ni42NTk3NzMxMTg5OCwgNDUuOTY2MjM0OTY2NjUwMl0sIFstNjYuNjYwOTg1ODQ0NjEzNiwgNDUuOTY1ODY2NTY3Njk1Ml0sIFstNjYuNjYyNjQ3NzI3ODg5MiwgNDUuOTY1NjIzMDQ4Mzk2OF0sIFstNjYuNjY0MzA5NjExMTY0OCwgNDUuOTY1MDQ4NTg4Mzc1MV0sIFstNjYuNjY2MTA2MjQxNzMzMSwgNDUuOTY0NjU1MjA0NzA2NF0sIFstNjYuNjY2MjU4OTU1MzMxNCwgNDUuOTY0NDYxNjMzOTM5Ml0sIFstNjYuNjY2NTE5NDY2NzYzNywgNDUuOTY0NTU1Mjk3Mjk4MV0sIFstNjYuNjY5NDIxMDI1MTMxNCwgNDUuOTY0MTgwNjQyOTEyM10sIFstNjYuNjcwODY3MzEyNzM4OSwgNDUuOTY0MDk5NDY3NDYxNF0sIFstNjYuNjczNjg4MDIyNzMxLCA0NS45NjQyMTE4NjQyMDc5XSwgWy02Ni42NzQ3OTI5NTA1MzA1LCA0NS45NjIyMDExNzY4NTEyXV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiA3NCwgIk5laWdoYm91cmgiOiAiV29vZHN0b2NrIFJvYWQiLCAiT0JKRUNUSUQiOiA3NCwgIlNoYXBlX0FyZWEiOiA0Mzk3NjMuOTMyNTQzLCAiU2hhcGVfTGVuZyI6IDQyNDAuMzk5MTQ5MDYsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZkOGQzYyIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifV0sICJ0eXBlIjogIkZlYXR1cmVDb2xsZWN0aW9uIn0KICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80ZjczYTJmYThjMzA0OWNhODQxMjFkNmU0NzQ3MGE3Myk7CiAgICAgICAgICAgICAgICBnZW9fanNvbl9jMzlmYzhmYjgxNmU0ODczYmZlZWI5ZjljODMwMzU1NC5zZXRTdHlsZShmdW5jdGlvbihmZWF0dXJlKSB7cmV0dXJuIGZlYXR1cmUucHJvcGVydGllcy5zdHlsZTt9KTsKCiAgICAgICAgICAgIAogICAgCiAgICB2YXIgY29sb3JfbWFwX2IxYTFlZmM2MmExYzQzMGU4NGY1OTQ1ZWQwNDU3YmEwID0ge307CgogICAgCiAgICBjb2xvcl9tYXBfYjFhMWVmYzYyYTFjNDMwZTg0ZjU5NDVlZDA0NTdiYTAuY29sb3IgPSBkMy5zY2FsZS50aHJlc2hvbGQoKQogICAgICAgICAgICAgIC5kb21haW4oWzEuMCwgMS4wODAxNjAzMjA2NDEyODI2LCAxLjE2MDMyMDY0MTI4MjU2NSwgMS4yNDA0ODA5NjE5MjM4NDc3LCAxLjMyMDY0MTI4MjU2NTEzMDEsIDEuNDAwODAxNjAzMjA2NDEyOCwgMS40ODA5NjE5MjM4NDc2OTU0LCAxLjU2MTEyMjI0NDQ4ODk3OCwgMS42NDEyODI1NjUxMzAyNjA1LCAxLjcyMTQ0Mjg4NTc3MTU0MzEsIDEuODAxNjAzMjA2NDEyODI1NiwgMS44ODE3NjM1MjcwNTQxMDgyLCAxLjk2MTkyMzg0NzY5NTM5MDksIDIuMDQyMDg0MTY4MzM2NjczNSwgMi4xMjIyNDQ0ODg5Nzc5NTYsIDIuMjAyNDA0ODA5NjE5MjM5LCAyLjI4MjU2NTEzMDI2MDUyMSwgMi4zNjI3MjU0NTA5MDE4MDM2LCAyLjQ0Mjg4NTc3MTU0MzA4NjMsIDIuNTIzMDQ2MDkyMTg0MzY4NSwgMi42MDMyMDY0MTI4MjU2NTEsIDIuNjgzMzY2NzMzNDY2OTMzOCwgMi43NjM1MjcwNTQxMDgyMTY0LCAyLjg0MzY4NzM3NDc0OTQ5OSwgMi45MjM4NDc2OTUzOTA3ODE3LCAzLjAwNDAwODAxNjAzMjA2NCwgMy4wODQxNjgzMzY2NzMzNDY2LCAzLjE2NDMyODY1NzMxNDYyOSwgMy4yNDQ0ODg5Nzc5NTU5MTIsIDMuMzI0NjQ5Mjk4NTk3MTk0NSwgMy40MDQ4MDk2MTkyMzg0NzcsIDMuNDg0OTY5OTM5ODc5NzU5MywgMy41NjUxMzAyNjA1MjEwNDIsIDMuNjQ1MjkwNTgxMTYyMzI0NiwgMy43MjU0NTA5MDE4MDM2MDczLCAzLjgwNTYxMTIyMjQ0NDg5LCAzLjg4NTc3MTU0MzA4NjE3MjYsIDMuOTY1OTMxODYzNzI3NDU0OCwgNC4wNDYwOTIxODQzNjg3MzcsIDQuMTI2MjUyNTA1MDEwMDIwNSwgNC4yMDY0MTI4MjU2NTEzMDIsIDQuMjg2NTczMTQ2MjkyNTg2LCA0LjM2NjczMzQ2NjkzMzg2NzUsIDQuNDQ2ODkzNzg3NTc1MTUsIDQuNTI3MDU0MTA4MjE2NDMzLCA0LjYwNzIxNDQyODg1NzcxNTUsIDQuNjg3Mzc0NzQ5NDk4OTk4LCA0Ljc2NzUzNTA3MDE0MDI4MSwgNC44NDc2OTUzOTA3ODE1NjMsIDQuOTI3ODU1NzExNDIyODQ1LCA1LjAwODAxNjAzMjA2NDEyOCwgNS4wODgxNzYzNTI3MDU0MTA1LCA1LjE2ODMzNjY3MzM0NjY5MywgNS4yNDg0OTY5OTM5ODc5NzYsIDUuMzI4NjU3MzE0NjI5MjU4LCA1LjQwODgxNzYzNTI3MDU0MSwgNS40ODg5Nzc5NTU5MTE4MjQsIDUuNTY5MTM4Mjc2NTUzMTA2LCA1LjY0OTI5ODU5NzE5NDM4OSwgNS43Mjk0NTg5MTc4MzU2NzIsIDUuODA5NjE5MjM4NDc2OTU0LCA1Ljg4OTc3OTU1OTExODIzNiwgNS45Njk5Mzk4Nzk3NTk1MTksIDYuMDUwMTAwMjAwNDAwODAxLCA2LjEzMDI2MDUyMTA0MjA4NCwgNi4yMTA0MjA4NDE2ODMzNjcsIDYuMjkwNTgxMTYyMzI0NjQ5LCA2LjM3MDc0MTQ4Mjk2NTkzMiwgNi40NTA5MDE4MDM2MDcyMTQ1LCA2LjUzMTA2MjEyNDI0ODQ5NywgNi42MTEyMjI0NDQ4ODk3OCwgNi42OTEzODI3NjU1MzEwNjI1LCA2Ljc3MTU0MzA4NjE3MjM0NSwgNi44NTE3MDM0MDY4MTM2MjcsIDYuOTMxODYzNzI3NDU0OTA5NSwgNy4wMTIwMjQwNDgwOTYxOTIsIDcuMDkyMTg0MzY4NzM3NDc1LCA3LjE3MjM0NDY4OTM3ODc1NzUsIDcuMjUyNTA1MDEwMDIwMDQsIDcuMzMyNjY1MzMwNjYxMzIzLCA3LjQxMjgyNTY1MTMwMjYwNSwgNy40OTI5ODU5NzE5NDM4ODgsIDcuNTczMTQ2MjkyNTg1MTcxLCA3LjY1MzMwNjYxMzIyNjQ1MywgNy43MzM0NjY5MzM4Njc3MzUsIDcuODEzNjI3MjU0NTA5MDE4LCA3Ljg5Mzc4NzU3NTE1MDMsIDcuOTczOTQ3ODk1NzkxNTgzLCA4LjA1NDEwODIxNjQzMjg2NiwgOC4xMzQyNjg1MzcwNzQxNSwgOC4yMTQ0Mjg4NTc3MTU0MzEsIDguMjk0NTg5MTc4MzU2NzEzLCA4LjM3NDc0OTQ5ODk5Nzk5NiwgOC40NTQ5MDk4MTk2MzkyOCwgOC41MzUwNzAxNDAyODA1NjIsIDguNjE1MjMwNDYwOTIxODQzLCA4LjY5NTM5MDc4MTU2MzEyNywgOC43NzU1NTExMDIyMDQ0MDksIDguODU1NzExNDIyODQ1NjksIDguOTM1ODcxNzQzNDg2OTc0LCA5LjAxNjAzMjA2NDEyODI1NiwgOS4wOTYxOTIzODQ3Njk1NCwgOS4xNzYzNTI3MDU0MTA4MjEsIDkuMjU2NTEzMDI2MDUyMTA0LCA5LjMzNjY3MzM0NjY5MzM4NiwgOS40MTY4MzM2NjczMzQ2NywgOS40OTY5OTM5ODc5NzU5NTIsIDkuNTc3MTU0MzA4NjE3MjM1LCA5LjY1NzMxNDYyOTI1ODUxNywgOS43Mzc0NzQ5NDk4OTk4LCA5LjgxNzYzNTI3MDU0MTA4MiwgOS44OTc3OTU1OTExODIzNjQsIDkuOTc3OTU1OTExODIzNjQ3LCAxMC4wNTgxMTYyMzI0NjQ5MywgMTAuMTM4Mjc2NTUzMTA2MjEzLCAxMC4yMTg0MzY4NzM3NDc0OTQsIDEwLjI5ODU5NzE5NDM4ODc3OCwgMTAuMzc4NzU3NTE1MDMwMDYsIDEwLjQ1ODkxNzgzNTY3MTM0MywgMTAuNTM5MDc4MTU2MzEyNjI1LCAxMC42MTkyMzg0NzY5NTM5MDksIDEwLjY5OTM5ODc5NzU5NTE5LCAxMC43Nzk1NTkxMTgyMzY0NzIsIDEwLjg1OTcxOTQzODg3Nzc1NiwgMTAuOTM5ODc5NzU5NTE5MDM3LCAxMS4wMjAwNDAwODAxNjAzMiwgMTEuMTAwMjAwNDAwODAxNjAzLCAxMS4xODAzNjA3MjE0NDI4ODYsIDExLjI2MDUyMTA0MjA4NDE2OCwgMTEuMzQwNjgxMzYyNzI1NDUxLCAxMS40MjA4NDE2ODMzNjY3MzMsIDExLjUwMTAwMjAwNDAwODAxNywgMTEuNTgxMTYyMzI0NjQ5Mjk5LCAxMS42NjEzMjI2NDUyOTA1ODIsIDExLjc0MTQ4Mjk2NTkzMTg2NCwgMTEuODIxNjQzMjg2NTczMTQ2LCAxMS45MDE4MDM2MDcyMTQ0MjksIDExLjk4MTk2MzkyNzg1NTcxLCAxMi4wNjIxMjQyNDg0OTY5OTQsIDEyLjE0MjI4NDU2OTEzODI3NiwgMTIuMjIyNDQ0ODg5Nzc5NTYsIDEyLjMwMjYwNTIxMDQyMDg0MSwgMTIuMzgyNzY1NTMxMDYyMTI1LCAxMi40NjI5MjU4NTE3MDM0MDcsIDEyLjU0MzA4NjE3MjM0NDY5LCAxMi42MjMyNDY0OTI5ODU5NzIsIDEyLjcwMzQwNjgxMzYyNzI1NCwgMTIuNzgzNTY3MTM0MjY4NTM3LCAxMi44NjM3Mjc0NTQ5MDk4MTksIDEyLjk0Mzg4Nzc3NTU1MTEwMywgMTMuMDI0MDQ4MDk2MTkyMzg0LCAxMy4xMDQyMDg0MTY4MzM2NjgsIDEzLjE4NDM2ODczNzQ3NDk1LCAxMy4yNjQ1MjkwNTgxMTYyMzMsIDEzLjM0NDY4OTM3ODc1NzUxNSwgMTMuNDI0ODQ5Njk5Mzk4Nzk4LCAxMy41MDUwMTAwMjAwNDAwOCwgMTMuNTg1MTcwMzQwNjgxMzYyLCAxMy42NjUzMzA2NjEzMjI2NDYsIDEzLjc0NTQ5MDk4MTk2MzkyNywgMTMuODI1NjUxMzAyNjA1MjEsIDEzLjkwNTgxMTYyMzI0NjQ5MywgMTMuOTg1OTcxOTQzODg3Nzc2LCAxNC4wNjYxMzIyNjQ1MjkwNTgsIDE0LjE0NjI5MjU4NTE3MDM0MSwgMTQuMjI2NDUyOTA1ODExNjIzLCAxNC4zMDY2MTMyMjY0NTI5MDcsIDE0LjM4Njc3MzU0NzA5NDE4OCwgMTQuNDY2OTMzODY3NzM1NDcsIDE0LjU0NzA5NDE4ODM3Njc1NCwgMTQuNjI3MjU0NTA5MDE4MDM1LCAxNC43MDc0MTQ4Mjk2NTkzMTksIDE0Ljc4NzU3NTE1MDMwMDYsIDE0Ljg2NzczNTQ3MDk0MTg4NCwgMTQuOTQ3ODk1NzkxNTgzMTY2LCAxNS4wMjgwNTYxMTIyMjQ0NSwgMTUuMTA4MjE2NDMyODY1NzMxLCAxNS4xODgzNzY3NTM1MDcwMTUsIDE1LjI2ODUzNzA3NDE0ODI5NywgMTUuMzQ4Njk3Mzk0Nzg5NTc4LCAxNS40Mjg4NTc3MTU0MzA4NjIsIDE1LjUwOTAxODAzNjA3MjE0NCwgMTUuNTg5MTc4MzU2NzEzNDI3LCAxNS42NjkzMzg2NzczNTQ3MDksIDE1Ljc0OTQ5ODk5Nzk5NTk5MywgMTUuODI5NjU5MzE4NjM3Mjc0LCAxNS45MDk4MTk2MzkyNzg1NTgsIDE1Ljk4OTk3OTk1OTkxOTg0LCAxNi4wNzAxNDAyODA1NjExMjMsIDE2LjE1MDMwMDYwMTIwMjQwMywgMTYuMjMwNDYwOTIxODQzNjg3LCAxNi4zMTA2MjEyNDI0ODQ5NywgMTYuMzkwNzgxNTYzMTI2MjU0LCAxNi40NzA5NDE4ODM3Njc1MzcsIDE2LjU1MTEwMjIwNDQwODgxNywgMTYuNjMxMjYyNTI1MDUwMSwgMTYuNzExNDIyODQ1NjkxMzgsIDE2Ljc5MTU4MzE2NjMzMjY2NCwgMTYuODcxNzQzNDg2OTczOTQ4LCAxNi45NTE5MDM4MDc2MTUyMywgMTcuMDMyMDY0MTI4MjU2NTEsIDE3LjExMjIyNDQ0ODg5Nzc5NSwgMTcuMTkyMzg0NzY5NTM5MDgsIDE3LjI3MjU0NTA5MDE4MDM2MiwgMTcuMzUyNzA1NDEwODIxNjQyLCAxNy40MzI4NjU3MzE0NjI5MjUsIDE3LjUxMzAyNjA1MjEwNDIxLCAxNy41OTMxODYzNzI3NDU0OTIsIDE3LjY3MzM0NjY5MzM4Njc3MiwgMTcuNzUzNTA3MDE0MDI4MDU2LCAxNy44MzM2NjczMzQ2NjkzNCwgMTcuOTEzODI3NjU1MzEwNjIsIDE3Ljk5Mzk4Nzk3NTk1MTkwMywgMTguMDc0MTQ4Mjk2NTkzMTg3LCAxOC4xNTQzMDg2MTcyMzQ0NywgMTguMjM0NDY4OTM3ODc1NzUsIDE4LjMxNDYyOTI1ODUxNzAzNCwgMTguMzk0Nzg5NTc5MTU4MzE3LCAxOC40NzQ5NDk4OTk3OTk2LCAxOC41NTUxMTAyMjA0NDA4OCwgMTguNjM1MjcwNTQxMDgyMTY0LCAxOC43MTU0MzA4NjE3MjM0NDgsIDE4Ljc5NTU5MTE4MjM2NDcyOCwgMTguODc1NzUxNTAzMDA2MDEsIDE4Ljk1NTkxMTgyMzY0NzI5NSwgMTkuMDM2MDcyMTQ0Mjg4NTgsIDE5LjExNjIzMjQ2NDkyOTg2LCAxOS4xOTYzOTI3ODU1NzExNDIsIDE5LjI3NjU1MzEwNjIxMjQyNSwgMTkuMzU2NzEzNDI2ODUzNzEsIDE5LjQzNjg3Mzc0NzQ5NDk5LCAxOS41MTcwMzQwNjgxMzYyNzIsIDE5LjU5NzE5NDM4ODc3NzU1NiwgMTkuNjc3MzU0NzA5NDE4ODM2LCAxOS43NTc1MTUwMzAwNjAxMiwgMTkuODM3Njc1MzUwNzAxNDAzLCAxOS45MTc4MzU2NzEzNDI2ODcsIDE5Ljk5Nzk5NTk5MTk4Mzk2NiwgMjAuMDc4MTU2MzEyNjI1MjUsIDIwLjE1ODMxNjYzMzI2NjUzNCwgMjAuMjM4NDc2OTUzOTA3ODE3LCAyMC4zMTg2MzcyNzQ1NDkwOTcsIDIwLjM5ODc5NzU5NTE5MDM4LCAyMC40Nzg5NTc5MTU4MzE2NjQsIDIwLjU1OTExODIzNjQ3Mjk0NCwgMjAuNjM5Mjc4NTU3MTE0MjI4LCAyMC43MTk0Mzg4Nzc3NTU1MSwgMjAuNzk5NTk5MTk4Mzk2Nzk1LCAyMC44Nzk3NTk1MTkwMzgwNzUsIDIwLjk1OTkxOTgzOTY3OTM2LCAyMS4wNDAwODAxNjAzMjA2NCwgMjEuMTIwMjQwNDgwOTYxOTI1LCAyMS4yMDA0MDA4MDE2MDMyMDUsIDIxLjI4MDU2MTEyMjI0NDQ5LCAyMS4zNjA3MjE0NDI4ODU3NzIsIDIxLjQ0MDg4MTc2MzUyNzA1NiwgMjEuNTIxMDQyMDg0MTY4MzM2LCAyMS42MDEyMDI0MDQ4MDk2MiwgMjEuNjgxMzYyNzI1NDUwOTAzLCAyMS43NjE1MjMwNDYwOTIxODMsIDIxLjg0MTY4MzM2NjczMzQ2NiwgMjEuOTIxODQzNjg3Mzc0NzUsIDIyLjAwMjAwNDAwODAxNjAzNCwgMjIuMDgyMTY0MzI4NjU3MzEzLCAyMi4xNjIzMjQ2NDkyOTg1OTcsIDIyLjI0MjQ4NDk2OTkzOTg4LCAyMi4zMjI2NDUyOTA1ODExNjQsIDIyLjQwMjgwNTYxMTIyMjQ0NCwgMjIuNDgyOTY1OTMxODYzNzI4LCAyMi41NjMxMjYyNTI1MDUwMSwgMjIuNjQzMjg2NTczMTQ2MjksIDIyLjcyMzQ0Njg5Mzc4NzU3NSwgMjIuODAzNjA3MjE0NDI4ODU4LCAyMi44ODM3Njc1MzUwNzAxNCwgMjIuOTYzOTI3ODU1NzExNDIsIDIzLjA0NDA4ODE3NjM1MjcwNSwgMjMuMTI0MjQ4NDk2OTkzOTksIDIzLjIwNDQwODgxNzYzNTI3MiwgMjMuMjg0NTY5MTM4Mjc2NTUyLCAyMy4zNjQ3Mjk0NTg5MTc4MzYsIDIzLjQ0NDg4OTc3OTU1OTEyLCAyMy41MjUwNTAxMDAyMDA0LCAyMy42MDUyMTA0MjA4NDE2ODMsIDIzLjY4NTM3MDc0MTQ4Mjk2NiwgMjMuNzY1NTMxMDYyMTI0MjUsIDIzLjg0NTY5MTM4Mjc2NTUzLCAyMy45MjU4NTE3MDM0MDY4MTMsIDI0LjAwNjAxMjAyNDA0ODA5NywgMjQuMDg2MTcyMzQ0Njg5MzgsIDI0LjE2NjMzMjY2NTMzMDY2LCAyNC4yNDY0OTI5ODU5NzE5NDQsIDI0LjMyNjY1MzMwNjYxMzIyOCwgMjQuNDA2ODEzNjI3MjU0NTA4LCAyNC40ODY5NzM5NDc4OTU3OSwgMjQuNTY3MTM0MjY4NTM3MDc1LCAyNC42NDcyOTQ1ODkxNzgzNTgsIDI0LjcyNzQ1NDkwOTgxOTYzOCwgMjQuODA3NjE1MjMwNDYwOTIsIDI0Ljg4Nzc3NTU1MTEwMjIwNSwgMjQuOTY3OTM1ODcxNzQzNDksIDI1LjA0ODA5NjE5MjM4NDc3LCAyNS4xMjgyNTY1MTMwMjYwNTIsIDI1LjIwODQxNjgzMzY2NzMzNiwgMjUuMjg4NTc3MTU0MzA4NjE2LCAyNS4zNjg3Mzc0NzQ5NDk5LCAyNS40NDg4OTc3OTU1OTExODMsIDI1LjUyOTA1ODExNjIzMjQ2NiwgMjUuNjA5MjE4NDM2ODczNzQ2LCAyNS42ODkzNzg3NTc1MTUwMywgMjUuNzY5NTM5MDc4MTU2MzEzLCAyNS44NDk2OTkzOTg3OTc1OTcsIDI1LjkyOTg1OTcxOTQzODg3NywgMjYuMDEwMDIwMDQwMDgwMTYsIDI2LjA5MDE4MDM2MDcyMTQ0NCwgMjYuMTcwMzQwNjgxMzYyNzI0LCAyNi4yNTA1MDEwMDIwMDQwMDcsIDI2LjMzMDY2MTMyMjY0NTI5LCAyNi40MTA4MjE2NDMyODY1NzUsIDI2LjQ5MDk4MTk2MzkyNzg1NSwgMjYuNTcxMTQyMjg0NTY5MTM4LCAyNi42NTEzMDI2MDUyMTA0MiwgMjYuNzMxNDYyOTI1ODUxNzA1LCAyNi44MTE2MjMyNDY0OTI5ODUsIDI2Ljg5MTc4MzU2NzEzNDI3LCAyNi45NzE5NDM4ODc3NzU1NTIsIDI3LjA1MjEwNDIwODQxNjgzMiwgMjcuMTMyMjY0NTI5MDU4MTE2LCAyNy4yMTI0MjQ4NDk2OTk0LCAyNy4yOTI1ODUxNzAzNDA2ODMsIDI3LjM3Mjc0NTQ5MDk4MTk2MywgMjcuNDUyOTA1ODExNjIzMjQ2LCAyNy41MzMwNjYxMzIyNjQ1MywgMjcuNjEzMjI2NDUyOTA1ODEzLCAyNy42OTMzODY3NzM1NDcwOTMsIDI3Ljc3MzU0NzA5NDE4ODM3NywgMjcuODUzNzA3NDE0ODI5NjYsIDI3LjkzMzg2NzczNTQ3MDk0LCAyOC4wMTQwMjgwNTYxMTIyMjQsIDI4LjA5NDE4ODM3Njc1MzUwNywgMjguMTc0MzQ4Njk3Mzk0NzksIDI4LjI1NDUwOTAxODAzNjA3LCAyOC4zMzQ2NjkzMzg2NzczNTQsIDI4LjQxNDgyOTY1OTMxODYzOCwgMjguNDk0OTg5OTc5OTU5OTIsIDI4LjU3NTE1MDMwMDYwMTIsIDI4LjY1NTMxMDYyMTI0MjQ4NSwgMjguNzM1NDcwOTQxODgzNzcsIDI4LjgxNTYzMTI2MjUyNTA1LCAyOC44OTU3OTE1ODMxNjYzMzIsIDI4Ljk3NTk1MTkwMzgwNzYxNiwgMjkuMDU2MTEyMjI0NDQ4OSwgMjkuMTM2MjcyNTQ1MDkwMTgsIDI5LjIxNjQzMjg2NTczMTQ2MywgMjkuMjk2NTkzMTg2MzcyNzQ2LCAyOS4zNzY3NTM1MDcwMTQwMywgMjkuNDU2OTEzODI3NjU1MzEsIDI5LjUzNzA3NDE0ODI5NjU5MywgMjkuNjE3MjM0NDY4OTM3ODc3LCAyOS42OTczOTQ3ODk1NzkxNTcsIDI5Ljc3NzU1NTExMDIyMDQ0LCAyOS44NTc3MTU0MzA4NjE3MjQsIDI5LjkzNzg3NTc1MTUwMzAwNywgMzAuMDE4MDM2MDcyMTQ0Mjg3LCAzMC4wOTgxOTYzOTI3ODU1NywgMzAuMTc4MzU2NzEzNDI2ODU0LCAzMC4yNTg1MTcwMzQwNjgxMzgsIDMwLjMzODY3NzM1NDcwOTQxOCwgMzAuNDE4ODM3Njc1MzUwNywgMzAuNDk4OTk3OTk1OTkxOTg1LCAzMC41NzkxNTgzMTY2MzMyNjUsIDMwLjY1OTMxODYzNzI3NDU1LCAzMC43Mzk0Nzg5NTc5MTU4MzIsIDMwLjgxOTYzOTI3ODU1NzExNiwgMzAuODk5Nzk5NTk5MTk4Mzk2LCAzMC45Nzk5NTk5MTk4Mzk2OCwgMzEuMDYwMTIwMjQwNDgwOTYzLCAzMS4xNDAyODA1NjExMjIyNDYsIDMxLjIyMDQ0MDg4MTc2MzUyNiwgMzEuMzAwNjAxMjAyNDA0ODEsIDMxLjM4MDc2MTUyMzA0NjA5MywgMzEuNDYwOTIxODQzNjg3MzczLCAzMS41NDEwODIxNjQzMjg2NTcsIDMxLjYyMTI0MjQ4NDk2OTk0LCAzMS43MDE0MDI4MDU2MTEyMjQsIDMxLjc4MTU2MzEyNjI1MjUwNCwgMzEuODYxNzIzNDQ2ODkzNzg3LCAzMS45NDE4ODM3Njc1MzUwNywgMzIuMDIyMDQ0MDg4MTc2MzYsIDMyLjEwMjIwNDQwODgxNzYzNCwgMzIuMTgyMzY0NzI5NDU4OTIsIDMyLjI2MjUyNTA1MDEwMDIsIDMyLjM0MjY4NTM3MDc0MTQ4LCAzMi40MjI4NDU2OTEzODI3NiwgMzIuNTAzMDA2MDEyMDI0MDQ1LCAzMi41ODMxNjYzMzI2NjUzMywgMzIuNjYzMzI2NjUzMzA2NjEsIDMyLjc0MzQ4Njk3Mzk0Nzg5NiwgMzIuODIzNjQ3Mjk0NTg5MTgsIDMyLjkwMzgwNzYxNTIzMDQ2LCAzMi45ODM5Njc5MzU4NzE3NDYsIDMzLjA2NDEyODI1NjUxMzAyLCAzMy4xNDQyODg1NzcxNTQzMDYsIDMzLjIyNDQ0ODg5Nzc5NTU5LCAzMy4zMDQ2MDkyMTg0MzY4NywgMzMuMzg0NzY5NTM5MDc4MTYsIDMzLjQ2NDkyOTg1OTcxOTQ0LCAzMy41NDUwOTAxODAzNjA3MjQsIDMzLjYyNTI1MDUwMTAwMjAxLCAzMy43MDU0MTA4MjE2NDMyODQsIDMzLjc4NTU3MTE0MjI4NDU3LCAzMy44NjU3MzE0NjI5MjU4NSwgMzMuOTQ1ODkxNzgzNTY3MTM0LCAzNC4wMjYwNTIxMDQyMDg0MiwgMzQuMTA2MjEyNDI0ODQ5NywgMzQuMTg2MzcyNzQ1NDkwOTg1LCAzNC4yNjY1MzMwNjYxMzIyNiwgMzQuMzQ2NjkzMzg2NzczNTQ1LCAzNC40MjY4NTM3MDc0MTQ4MywgMzQuNTA3MDE0MDI4MDU2MTEsIDM0LjU4NzE3NDM0ODY5NzM5NSwgMzQuNjY3MzM0NjY5MzM4NjgsIDM0Ljc0NzQ5NDk4OTk3OTk2LCAzNC44Mjc2NTUzMTA2MjEyNCwgMzQuOTA3ODE1NjMxMjYyNTIsIDM0Ljk4Nzk3NTk1MTkwMzgwNiwgMzUuMDY4MTM2MjcyNTQ1MDksIDM1LjE0ODI5NjU5MzE4NjM3LCAzNS4yMjg0NTY5MTM4Mjc2NiwgMzUuMzA4NjE3MjM0NDY4OTQsIDM1LjM4ODc3NzU1NTExMDIyNCwgMzUuNDY4OTM3ODc1NzUxNSwgMzUuNTQ5MDk4MTk2MzkyNzg0LCAzNS42MjkyNTg1MTcwMzQwNywgMzUuNzA5NDE4ODM3Njc1MzUsIDM1Ljc4OTU3OTE1ODMxNjYzNCwgMzUuODY5NzM5NDc4OTU3OTIsIDM1Ljk0OTg5OTc5OTU5OTIsIDM2LjAzMDA2MDEyMDI0MDQ4LCAzNi4xMTAyMjA0NDA4ODE3NiwgMzYuMTkwMzgwNzYxNTIzMDQ1LCAzNi4yNzA1NDEwODIxNjQzMywgMzYuMzUwNzAxNDAyODA1NjEsIDM2LjQzMDg2MTcyMzQ0Njg5NSwgMzYuNTExMDIyMDQ0MDg4MTgsIDM2LjU5MTE4MjM2NDcyOTQ1NSwgMzYuNjcxMzQyNjg1MzcwNzQsIDM2Ljc1MTUwMzAwNjAxMjAyLCAzNi44MzE2NjMzMjY2NTMzMDYsIDM2LjkxMTgyMzY0NzI5NDU5LCAzNi45OTE5ODM5Njc5MzU4NywgMzcuMDcyMTQ0Mjg4NTc3MTYsIDM3LjE1MjMwNDYwOTIxODQ0LCAzNy4yMzI0NjQ5Mjk4NTk3MiwgMzcuMzEyNjI1MjUwNTAxLCAzNy4zOTI3ODU1NzExNDIyODQsIDM3LjQ3Mjk0NTg5MTc4MzU3LCAzNy41NTMxMDYyMTI0MjQ4NSwgMzcuNjMzMjY2NTMzMDY2MTM0LCAzNy43MTM0MjY4NTM3MDc0MiwgMzcuNzkzNTg3MTc0MzQ4Njk0LCAzNy44NzM3NDc0OTQ5ODk5OCwgMzcuOTUzOTA3ODE1NjMxMjYsIDM4LjAzNDA2ODEzNjI3MjU0NSwgMzguMTE0MjI4NDU2OTEzODMsIDM4LjE5NDM4ODc3NzU1NTExLCAzOC4yNzQ1NDkwOTgxOTYzOTUsIDM4LjM1NDcwOTQxODgzNzY3LCAzOC40MzQ4Njk3Mzk0Nzg5NTUsIDM4LjUxNTAzMDA2MDEyMDI0LCAzOC41OTUxOTAzODA3NjE1MiwgMzguNjc1MzUwNzAxNDAyODA2LCAzOC43NTU1MTEwMjIwNDQwOSwgMzguODM1NjcxMzQyNjg1MzcsIDM4LjkxNTgzMTY2MzMyNjY2LCAzOC45OTU5OTE5ODM5Njc5MywgMzkuMDc2MTUyMzA0NjA5MjIsIDM5LjE1NjMxMjYyNTI1MDUsIDM5LjIzNjQ3Mjk0NTg5MTc4NCwgMzkuMzE2NjMzMjY2NTMzMDcsIDM5LjM5Njc5MzU4NzE3NDM1LCAzOS40NzY5NTM5MDc4MTU2MzQsIDM5LjU1NzExNDIyODQ1NjkxLCAzOS42MzcyNzQ1NDkwOTgxOTQsIDM5LjcxNzQzNDg2OTczOTQ4LCAzOS43OTc1OTUxOTAzODA3NiwgMzkuODc3NzU1NTExMDIyMDQ1LCAzOS45NTc5MTU4MzE2NjMzMywgNDAuMDM4MDc2MTUyMzA0NjEsIDQwLjExODIzNjQ3Mjk0NTg5LCA0MC4xOTgzOTY3OTM1ODcxNywgNDAuMjc4NTU3MTE0MjI4NDU1LCA0MC4zNTg3MTc0MzQ4Njk3NCwgNDAuNDM4ODc3NzU1NTExMDIsIDQwLjUxOTAzODA3NjE1MjMwNiwgNDAuNTk5MTk4Mzk2NzkzNTksIDQwLjY3OTM1ODcxNzQzNDg3LCA0MC43NTk1MTkwMzgwNzYxNSwgNDAuODM5Njc5MzU4NzE3NDMsIDQwLjkxOTgzOTY3OTM1ODcyLCA0MS4wXSkKICAgICAgICAgICAgICAucmFuZ2UoWycjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnXSk7CiAgICAKCiAgICBjb2xvcl9tYXBfYjFhMWVmYzYyYTFjNDMwZTg0ZjU5NDVlZDA0NTdiYTAueCA9IGQzLnNjYWxlLmxpbmVhcigpCiAgICAgICAgICAgICAgLmRvbWFpbihbMS4wLCA0MS4wXSkKICAgICAgICAgICAgICAucmFuZ2UoWzAsIDQwMF0pOwoKICAgIGNvbG9yX21hcF9iMWExZWZjNjJhMWM0MzBlODRmNTk0NWVkMDQ1N2JhMC5sZWdlbmQgPSBMLmNvbnRyb2woe3Bvc2l0aW9uOiAndG9wcmlnaHQnfSk7CiAgICBjb2xvcl9tYXBfYjFhMWVmYzYyYTFjNDMwZTg0ZjU5NDVlZDA0NTdiYTAubGVnZW5kLm9uQWRkID0gZnVuY3Rpb24gKG1hcCkge3ZhciBkaXYgPSBMLkRvbVV0aWwuY3JlYXRlKCdkaXYnLCAnbGVnZW5kJyk7IHJldHVybiBkaXZ9OwogICAgY29sb3JfbWFwX2IxYTFlZmM2MmExYzQzMGU4NGY1OTQ1ZWQwNDU3YmEwLmxlZ2VuZC5hZGRUbyhtYXBfNGY3M2EyZmE4YzMwNDljYTg0MTIxZDZlNDc0NzBhNzMpOwoKICAgIGNvbG9yX21hcF9iMWExZWZjNjJhMWM0MzBlODRmNTk0NWVkMDQ1N2JhMC54QXhpcyA9IGQzLnN2Zy5heGlzKCkKICAgICAgICAuc2NhbGUoY29sb3JfbWFwX2IxYTFlZmM2MmExYzQzMGU4NGY1OTQ1ZWQwNDU3YmEwLngpCiAgICAgICAgLm9yaWVudCgidG9wIikKICAgICAgICAudGlja1NpemUoMSkKICAgICAgICAudGlja1ZhbHVlcyhbMSwgOCwgMTYsIDI0LCAzMiwgNDFdKTsKCiAgICBjb2xvcl9tYXBfYjFhMWVmYzYyYTFjNDMwZTg0ZjU5NDVlZDA0NTdiYTAuc3ZnID0gZDMuc2VsZWN0KCIubGVnZW5kLmxlYWZsZXQtY29udHJvbCIpLmFwcGVuZCgic3ZnIikKICAgICAgICAuYXR0cigiaWQiLCAnbGVnZW5kJykKICAgICAgICAuYXR0cigid2lkdGgiLCA0NTApCiAgICAgICAgLmF0dHIoImhlaWdodCIsIDQwKTsKCiAgICBjb2xvcl9tYXBfYjFhMWVmYzYyYTFjNDMwZTg0ZjU5NDVlZDA0NTdiYTAuZyA9IGNvbG9yX21hcF9iMWExZWZjNjJhMWM0MzBlODRmNTk0NWVkMDQ1N2JhMC5zdmcuYXBwZW5kKCJnIikKICAgICAgICAuYXR0cigiY2xhc3MiLCAia2V5IikKICAgICAgICAuYXR0cigidHJhbnNmb3JtIiwgInRyYW5zbGF0ZSgyNSwxNikiKTsKCiAgICBjb2xvcl9tYXBfYjFhMWVmYzYyYTFjNDMwZTg0ZjU5NDVlZDA0NTdiYTAuZy5zZWxlY3RBbGwoInJlY3QiKQogICAgICAgIC5kYXRhKGNvbG9yX21hcF9iMWExZWZjNjJhMWM0MzBlODRmNTk0NWVkMDQ1N2JhMC5jb2xvci5yYW5nZSgpLm1hcChmdW5jdGlvbihkLCBpKSB7CiAgICAgICAgICByZXR1cm4gewogICAgICAgICAgICB4MDogaSA/IGNvbG9yX21hcF9iMWExZWZjNjJhMWM0MzBlODRmNTk0NWVkMDQ1N2JhMC54KGNvbG9yX21hcF9iMWExZWZjNjJhMWM0MzBlODRmNTk0NWVkMDQ1N2JhMC5jb2xvci5kb21haW4oKVtpIC0gMV0pIDogY29sb3JfbWFwX2IxYTFlZmM2MmExYzQzMGU4NGY1OTQ1ZWQwNDU3YmEwLngucmFuZ2UoKVswXSwKICAgICAgICAgICAgeDE6IGkgPCBjb2xvcl9tYXBfYjFhMWVmYzYyYTFjNDMwZTg0ZjU5NDVlZDA0NTdiYTAuY29sb3IuZG9tYWluKCkubGVuZ3RoID8gY29sb3JfbWFwX2IxYTFlZmM2MmExYzQzMGU4NGY1OTQ1ZWQwNDU3YmEwLngoY29sb3JfbWFwX2IxYTFlZmM2MmExYzQzMGU4NGY1OTQ1ZWQwNDU3YmEwLmNvbG9yLmRvbWFpbigpW2ldKSA6IGNvbG9yX21hcF9iMWExZWZjNjJhMWM0MzBlODRmNTk0NWVkMDQ1N2JhMC54LnJhbmdlKClbMV0sCiAgICAgICAgICAgIHo6IGQKICAgICAgICAgIH07CiAgICAgICAgfSkpCiAgICAgIC5lbnRlcigpLmFwcGVuZCgicmVjdCIpCiAgICAgICAgLmF0dHIoImhlaWdodCIsIDEwKQogICAgICAgIC5hdHRyKCJ4IiwgZnVuY3Rpb24oZCkgeyByZXR1cm4gZC54MDsgfSkKICAgICAgICAuYXR0cigid2lkdGgiLCBmdW5jdGlvbihkKSB7IHJldHVybiBkLngxIC0gZC54MDsgfSkKICAgICAgICAuc3R5bGUoImZpbGwiLCBmdW5jdGlvbihkKSB7IHJldHVybiBkLno7IH0pOwoKICAgIGNvbG9yX21hcF9iMWExZWZjNjJhMWM0MzBlODRmNTk0NWVkMDQ1N2JhMC5nLmNhbGwoY29sb3JfbWFwX2IxYTFlZmM2MmExYzQzMGU4NGY1OTQ1ZWQwNDU3YmEwLnhBeGlzKS5hcHBlbmQoInRleHQiKQogICAgICAgIC5hdHRyKCJjbGFzcyIsICJjYXB0aW9uIikKICAgICAgICAuYXR0cigieSIsIDIxKQogICAgICAgIC50ZXh0KCdGcmVkZXJpY3RvbiBOZWlnaGJvdXJob29kcycpOwo8L3NjcmlwdD4=" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>



## Is it possible the higher rate of crime in the downtown area is due to population density?


```python
opendemog = 'Fredericton_Census_Tract_Demographics.xlsx'

workbook = pd.ExcelFile(opendemog)
print(workbook.sheet_names)
```

    ['Fredericton_Census_Tract_Demogr']



```python
demog_df = workbook.parse('Fredericton_Census_Tract_Demogr')
demog_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>FID</th>
      <th>OBJECTID</th>
      <th>DBUID</th>
      <th>DAUID</th>
      <th>CDUID</th>
      <th>CTUID</th>
      <th>CTNAME</th>
      <th>DBuid_1</th>
      <th>DBpop2011</th>
      <th>DBtdwell20</th>
      <th>DBurdwell2</th>
      <th>Shape_Leng</th>
      <th>Shape_Area</th>
      <th>CTIDLINK</th>
      <th>Shape__Area</th>
      <th>Shape__Length</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>501</td>
      <td>1310024304</td>
      <td>13100243</td>
      <td>1310</td>
      <td>3200002</td>
      <td>2</td>
      <td>1310024304</td>
      <td>60</td>
      <td>25</td>
      <td>22</td>
      <td>0.007462</td>
      <td>0.000003</td>
      <td>3200002</td>
      <td>0.000003</td>
      <td>0.007462</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>502</td>
      <td>1310032004</td>
      <td>13100320</td>
      <td>1310</td>
      <td>3200010</td>
      <td>10</td>
      <td>1310032004</td>
      <td>15</td>
      <td>3</td>
      <td>3</td>
      <td>0.009008</td>
      <td>0.000003</td>
      <td>3200010</td>
      <td>0.000003</td>
      <td>0.009008</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>503</td>
      <td>1310017103</td>
      <td>13100171</td>
      <td>1310</td>
      <td>3200014</td>
      <td>14</td>
      <td>1310017103</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.010602</td>
      <td>0.000007</td>
      <td>3200014</td>
      <td>0.000007</td>
      <td>0.010602</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>504</td>
      <td>1310018301</td>
      <td>13100183</td>
      <td>1310</td>
      <td>3200012</td>
      <td>12</td>
      <td>1310018301</td>
      <td>108</td>
      <td>60</td>
      <td>50</td>
      <td>0.039599</td>
      <td>0.000068</td>
      <td>3200012</td>
      <td>0.000068</td>
      <td>0.039599</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>505</td>
      <td>1310022905</td>
      <td>13100229</td>
      <td>1310</td>
      <td>3200007</td>
      <td>7</td>
      <td>1310022905</td>
      <td>129</td>
      <td>47</td>
      <td>44</td>
      <td>0.011833</td>
      <td>0.000005</td>
      <td>3200007</td>
      <td>0.000005</td>
      <td>0.011834</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


```python

```


```python
# Population Density 
world_geo = r'world_countries.json' # geojson file
fredericton_d_map = folium.Map(location=[45.94, -66.63], width=1200, height=750,zoom_start=12)
fredericton_d_map

threshold_scale = np.linspace(demog_df['DBpop2011'].min(),demog_df['DBpop2011'].max(),6,dtype=int)
threshold_scale = threshold_scale.tolist()
threshold_scale[-1] = threshold_scale[-1]+1

fredericton_d_map.choropleth(geo_data=demog_geo,data=demog_df,columns=['OBJECTID','DBpop2011'],key_on='feature.properties.OBJECTID',
    threshold_scale=threshold_scale,fill_color='PuBuGn',fill_opacity=0.7, line_opacity=0.1,legend_name='Fredericton Population Density')
fredericton_d_map
```







## Let's look at specific locations in Fredericton


```python
pointbook = 'Fredericton Locations.xlsx'

workbook_2 = pd.ExcelFile(pointbook)
print(workbook_2.sheet_names)
```

    ['Sheet1']



```python
location_df = workbook_2.parse('Sheet1')
location_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Location</th>
      <th>Neighbourh</th>
      <th>Latitude</th>
      <th>Longitude</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Knowledge Park</td>
      <td>NaN</td>
      <td>45.931143</td>
      <td>-66.652700</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Fredericton Hill</td>
      <td>NaN</td>
      <td>45.948512</td>
      <td>-66.656045</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Nashwaaksis</td>
      <td>NaN</td>
      <td>45.983382</td>
      <td>-66.644856</td>
    </tr>
    <tr>
      <th>3</th>
      <td>University of New Brunswick</td>
      <td>NaN</td>
      <td>45.948121</td>
      <td>-66.641406</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Devon</td>
      <td>NaN</td>
      <td>45.968802</td>
      <td>-66.622738</td>
    </tr>
    <tr>
      <th>5</th>
      <td>New Maryland</td>
      <td>NaN</td>
      <td>45.892795</td>
      <td>-66.683673</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Marysville</td>
      <td>NaN</td>
      <td>45.978913</td>
      <td>-66.589491</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Skyline Acres</td>
      <td>NaN</td>
      <td>45.931827</td>
      <td>-66.640339</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Hanwell</td>
      <td>NaN</td>
      <td>45.902315</td>
      <td>-66.755113</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Downtown</td>
      <td>NaN</td>
      <td>45.958327</td>
      <td>-66.647211</td>
    </tr>
  </tbody>
</table>
</div>




```python
location_df.drop(['Neighbourh'], axis=1,inplace=True)
location_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Location</th>
      <th>Latitude</th>
      <th>Longitude</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Knowledge Park</td>
      <td>45.931143</td>
      <td>-66.652700</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Fredericton Hill</td>
      <td>45.948512</td>
      <td>-66.656045</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Nashwaaksis</td>
      <td>45.983382</td>
      <td>-66.644856</td>
    </tr>
    <tr>
      <th>3</th>
      <td>University of New Brunswick</td>
      <td>45.948121</td>
      <td>-66.641406</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Devon</td>
      <td>45.968802</td>
      <td>-66.622738</td>
    </tr>
    <tr>
      <th>5</th>
      <td>New Maryland</td>
      <td>45.892795</td>
      <td>-66.683673</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Marysville</td>
      <td>45.978913</td>
      <td>-66.589491</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Skyline Acres</td>
      <td>45.931827</td>
      <td>-66.640339</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Hanwell</td>
      <td>45.902315</td>
      <td>-66.755113</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
    </tr>
  </tbody>
</table>
</div>



### Add location markers to map


```python
for lat, lng, point in zip(location_df['Latitude'], location_df['Longitude'], location_df['Location']):
    label = '{}'.format(point)
    label = folium.Popup(label, parse_html=True)
    folium.CircleMarker([lat, lng],radium=1,popup=label,color='blue',fill=True,fill_color='#3186cc',fill_opacity=0.7,
        parse_html=False).add_to(fredericton_c_map)
fredericton_c_map
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><iframe src="data:text/html;charset=utf-8;base64,PCFET0NUWVBFIGh0bWw+CjxoZWFkPiAgICAKICAgIDxtZXRhIGh0dHAtZXF1aXY9ImNvbnRlbnQtdHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PVVURi04IiAvPgogICAgPHNjcmlwdD5MX1BSRUZFUl9DQU5WQVMgPSBmYWxzZTsgTF9OT19UT1VDSCA9IGZhbHNlOyBMX0RJU0FCTEVfM0QgPSBmYWxzZTs8L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2FqYXguZ29vZ2xlYXBpcy5jb20vYWpheC9saWJzL2pxdWVyeS8xLjExLjEvanF1ZXJ5Lm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvanMvYm9vdHN0cmFwLm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvTGVhZmxldC5hd2Vzb21lLW1hcmtlcnMvMi4wLjIvbGVhZmxldC5hd2Vzb21lLW1hcmtlcnMuanMiPjwvc2NyaXB0PgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9jc3MvYm9vdHN0cmFwLm1pbi5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvY3NzL2Jvb3RzdHJhcC10aGVtZS5taW4uY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vbWF4Y2RuLmJvb3RzdHJhcGNkbi5jb20vZm9udC1hd2Vzb21lLzQuNi4zL2Nzcy9mb250LWF3ZXNvbWUubWluLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9MZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy8yLjAuMi9sZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9yYXdnaXQuY29tL3B5dGhvbi12aXN1YWxpemF0aW9uL2ZvbGl1bS9tYXN0ZXIvZm9saXVtL3RlbXBsYXRlcy9sZWFmbGV0LmF3ZXNvbWUucm90YXRlLmNzcyIvPgogICAgPHN0eWxlPmh0bWwsIGJvZHkge3dpZHRoOiAxMDAlO2hlaWdodDogMTAwJTttYXJnaW46IDA7cGFkZGluZzogMDt9PC9zdHlsZT4KICAgIDxzdHlsZT4jbWFwIHtwb3NpdGlvbjphYnNvbHV0ZTt0b3A6MDtib3R0b206MDtyaWdodDowO2xlZnQ6MDt9PC9zdHlsZT4KICAgIAogICAgICAgICAgICA8c3R5bGU+ICNtYXBfNGY3M2EyZmE4YzMwNDljYTg0MTIxZDZlNDc0NzBhNzMgewogICAgICAgICAgICAgICAgcG9zaXRpb24gOiByZWxhdGl2ZTsKICAgICAgICAgICAgICAgIHdpZHRoIDogMTAwMC4wcHg7CiAgICAgICAgICAgICAgICBoZWlnaHQ6IDc1MC4wcHg7CiAgICAgICAgICAgICAgICBsZWZ0OiAwLjAlOwogICAgICAgICAgICAgICAgdG9wOiAwLjAlOwogICAgICAgICAgICAgICAgfQogICAgICAgICAgICA8L3N0eWxlPgogICAgICAgIAogICAgPHNjcmlwdCBzcmM9Imh0dHBzOi8vY2RuanMuY2xvdWRmbGFyZS5jb20vYWpheC9saWJzL2QzLzMuNS41L2QzLm1pbi5qcyI+PC9zY3JpcHQ+CjwvaGVhZD4KPGJvZHk+ICAgIAogICAgCiAgICAgICAgICAgIDxkaXYgY2xhc3M9ImZvbGl1bS1tYXAiIGlkPSJtYXBfNGY3M2EyZmE4YzMwNDljYTg0MTIxZDZlNDc0NzBhNzMiID48L2Rpdj4KICAgICAgICAKPC9ib2R5Pgo8c2NyaXB0PiAgICAKICAgIAoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgYm91bmRzID0gbnVsbDsKICAgICAgICAgICAgCgogICAgICAgICAgICB2YXIgbWFwXzRmNzNhMmZhOGMzMDQ5Y2E4NDEyMWQ2ZTQ3NDcwYTczID0gTC5tYXAoCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAnbWFwXzRmNzNhMmZhOGMzMDQ5Y2E4NDEyMWQ2ZTQ3NDcwYTczJywKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHtjZW50ZXI6IFs0NS45MSwtNjYuNjVdLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgem9vbTogMTIsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBtYXhCb3VuZHM6IGJvdW5kcywKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGxheWVyczogW10sCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB3b3JsZENvcHlKdW1wOiBmYWxzZSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGNyczogTC5DUlMuRVBTRzM4NTcKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgfSk7CiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciB0aWxlX2xheWVyXzNkYzE5YzBmZTI0NzRkNTE4YzZjZmQ3ODNjNTFkNDZjID0gTC50aWxlTGF5ZXIoCiAgICAgICAgICAgICAgICAnaHR0cHM6Ly97c30udGlsZS5vcGVuc3RyZWV0bWFwLm9yZy97en0ve3h9L3t5fS5wbmcnLAogICAgICAgICAgICAgICAgewogICJhdHRyaWJ1dGlvbiI6IG51bGwsCiAgImRldGVjdFJldGluYSI6IGZhbHNlLAogICJtYXhab29tIjogMTgsCiAgIm1pblpvb20iOiAxLAogICJub1dyYXAiOiBmYWxzZSwKICAic3ViZG9tYWlucyI6ICJhYmMiCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzRmNzNhMmZhOGMzMDQ5Y2E4NDEyMWQ2ZTQ3NDcwYTczKTsKICAgICAgICAKICAgIAoKICAgICAgICAgICAgCgogICAgICAgICAgICAgICAgdmFyIGdlb19qc29uX2MzOWZjOGZiODE2ZTQ4NzNiZmVlYjlmOWM4MzAzNTU0ID0gTC5nZW9Kc29uKAogICAgICAgICAgICAgICAgICAgIHsiZmVhdHVyZXMiOiBbeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjE5MzQ4OTMxMTk0NiwgNDUuODY4ODkyNTg1OTY2NF0sIFstNjYuNTk4NjA2ODMxMjg0MywgNDUuODkzNDMxNzU3NTQ5OF0sIFstNjYuNTk5ODQ2NTA2Mzc2NCwgNDUuODk2Mjg4OTUzMzg5NF0sIFstNjYuNjAwNTU2MTc1NDUwOCwgNDUuODk4Nzk1OTEyMjQxNF0sIFstNjYuNjAwNzYyNzg3OTY2MiwgNDUuOTAwNDE1MDU5OTE4OV0sIFstNjYuNjAwNTExMjU5Njg2NiwgNDUuOTAyMDM0MTYwMzgwM10sIFstNjYuNTk5MzcwMzk5Mjc1OCwgNDUuOTA0OTQwOTIxMTA1NF0sIFstNjYuNTk4MzkxMjM1NjE2MSwgNDUuOTA2NjUzNjUwNzg3NV0sIFstNjYuNTk1MDQwNTE5NjA2MywgNDUuOTExMDk3NzUwMzE4Ml0sIFstNjYuNTkyNDcxMzM3ODkzOCwgNDUuOTEzNzE2NTM5NjcyNV0sIFstNjYuNTk3NTE5ODY5NzkwNSwgNDUuOTE1MTkxNTA3NDM3NV0sIFstNjYuNjAxNjE2MTg3NDg2MSwgNDUuOTE2NTkxNDQwNTc4OV0sIFstNjYuNjA2Mzg2MjQxNjQ0OCwgNDUuOTE4NDY2Mjk1NzEzNF0sIFstNjYuNjEwMjMxMDMxMDYwOCwgNDUuOTIwMTg0ODU3MjcxNl0sIFstNjYuNjE5MzkzODQ2OTU4OCwgNDUuOTI2NDE0OTc3Nzc4N10sIFstNjYuNjE5NDI5Nzc5NTcwMiwgNDUuOTI0MzQ2NjgwMzQ2MV0sIFstNjYuNjIwNjY5NDU0NjYyMywgNDUuOTIyMTM0NTc5MDIyN10sIFstNjYuNjI0MTQ1OTM0ODExOCwgNDUuOTE4MTEwMDc4MTEyNF0sIFstNjYuNjI0OTYzNDAxNzIwNCwgNDUuOTE3Nzk3NjA0NjQ5N10sIFstNjYuNjI1ODc5NjgzMzEwMiwgNDUuOTE3OTEwMDk1Mjk5XSwgWy02Ni42MjkyMTI0MzMwMTQzLCA0NS45MjAwMzQ4NzU4Mzc0XSwgWy02Ni42MzI3MzM4Mjg5MjgsIDQ1LjkyMjU3MjAwNzE4NDZdLCBbLTY2LjYzNTYzNTM4NzI5NTcsIDQ1LjkyNDQwOTE2NzgwM10sIFstNjYuNjM2MjczMTkxMTQ3NCwgNDUuOTI0OTg0MDQ5MTA0NF0sIFstNjYuNjM4MTk1NTg1ODU1NSwgNDUuOTI1ODkwMDk5OTMxM10sIFstNjYuNjQwMDI4MTQ5MDM1MSwgNDUuOTI3MjE0NzgyMDkxNV0sIFstNjYuNjQ2OTcyMTI2MTgxMywgNDUuOTMwOTUxMjE1MDc5MV0sIFstNjYuNjQ5MjYyODMwMTU1OCwgNDUuOTMyNDI1NzI0NzE3M10sIFstNjYuNjUwMTUyMTYyMjg3MSwgNDUuOTMzMTI1NDc4Mjg2OF0sIFstNjYuNjUwNDMwNjQwMDI1MiwgNDUuOTMzNzU2NDk4NDg4NF0sIFstNjYuNjUwNTY1Mzg3MzE3OCwgNDUuOTM0NzQzNjI0NjAwNV0sIFstNjYuNjUwMzU4Nzc0ODAyNCwgNDUuOTM1NzE4MjM4MjA2OV0sIFstNjYuNjUyMDc0NTU2OTk1MSwgNDUuOTM1MjI0Njg2MDIxM10sIFstNjYuNjUzMjUxMzUwMDE3MywgNDUuOTM1MDg3MjQwMzI2OV0sIFstNjYuNjU0MTg1NTk3OTEyOCwgNDUuOTM1MTEyMjMwNDc4NV0sIFstNjYuNjU1Nzc1NjE1OTY1NywgNDUuOTM1MzgwODczODk2OV0sIFstNjYuNjU5NzQ2MTY5NTIxNSwgNDUuOTM2NTYxNjQwMDAyN10sIFstNjYuNjY5MjMyMzc4OTIxOCwgNDUuOTQwODY1OTEzMDc0N10sIFstNjYuNjcwMjIwNTI1NzM0MywgNDUuOTQxMTcyMDA5NzU0M10sIFstNjYuNjcwNTg4ODM1MDAwOCwgNDUuOTQxNTcxODA2OTU0MV0sIFstNjYuNjcxNzAyNzQ1OTUzMSwgNDUuOTQxODY1NDA2MTg2N10sIFstNjYuNjgwNTYwMTM0NjU0NSwgNDUuOTQ1NjU3MDY5MzM5MV0sIFstNjYuNjgwODIwNjQ2MDg2OSwgNDUuOTQ1NjEzMzQ0ODgzXSwgWy02Ni42OTA5OTg1NTgyNTYsIDQ1Ljk0OTg3OTQ0MDA1MjZdLCBbLTY2LjY5MzIzNTM2MzMxMzQsIDQ1Ljk1MDM3OTEwNzYxMDddLCBbLTY2LjY5NTY2OTc5NzczMzQsIDQ1Ljk1MDQ0NzgxMTU0NzZdLCBbLTY2LjY5NTU1MzAxNjc0NjUsIDQ1Ljk0OTg2MDcwMjQzMTZdLCBbLTY2LjY5NTAxNDAyNzU3NiwgNDUuOTQ5ODYwNzAyNDMxNl0sIFstNjYuNjk1NjI0ODgxOTY5MiwgNDUuOTQ4MjYxNzM1NDM1XSwgWy02Ni42OTk3NjYxMTU0MjksIDQ1Ljk0NTI1MTA1NTIwNTJdLCBbLTY2LjY5OTM5NzgwNjE2MjUsIDQ1Ljk0NTA1MTE3MDIzMTVdLCBbLTY2LjY5OTY3NjI4MzkwMDYsIDQ1Ljk0NDg1MTI4NDUzNzFdLCBbLTY2LjY5OTIyNzEyNjI1ODUsIDQ1Ljk0NDYxMzkxOTMzODldLCBbLTY2LjcwMjIzNjQ4MjQ2MDMsIDQ1Ljk0MDc3MjIwOTY3MTZdLCBbLTY2LjcwNDEwNDk3ODI1MTMsIDQ1LjkzOTM2NjYzOTYyMjVdLCBbLTY2LjcwNDYwODAzNDgxMDQsIDQ1LjkzODc5MTkwNzM4MzVdLCBbLTY2LjcwNjE0NDE1Mzk0NjMsIDQ1LjkzOTA5ODAxNTUxMzJdLCBbLTY2LjcwNTE5MTkzOTc0NTEsIDQ1LjkzODg1NDM3ODU2NzZdLCBbLTY2LjcwNTY5NDk5NjMwNDIsIDQ1LjkzNzQwNTAyODk3MV0sIFstNjYuNzA2NjExMjc3ODk0LCA0NS45MzYyNDMwMjMwNTQxXSwgWy02Ni43MDc0MTA3Nzg0OTY5LCA0NS45MzU2NzQ1MDU5MTIxXSwgWy02Ni43MDg3MTMzMzU2NTg4LCA0NS45MzUwNDM1MDc1MzQ1XSwgWy02Ni43MTEwOTM4NzExNjE4LCA0NS45MzQyMDYzMzAyODgyXSwgWy02Ni43MTIyNTI2OTc4NzgzLCA0NS45MzA5MjYyMjMwNTI1XSwgWy02Ni43MDk2MDI2Njc3OTAxLCA0NS45MjkzODkxOTE3NzE4XSwgWy02Ni42NzQ2NDAyMzY5MzIyLCA0NS45MDYxMjg1ODU5OTA4XSwgWy02Ni42MTkzNDg5MzExOTQ2LCA0NS44Njg4OTI1ODU5NjY0XV0sIFtbLTY2LjY5MzQxNTAyNjM3MDMsIDQ1LjkzODY0ODIyMzM5M10sIFstNjYuNzAwMTk3MzA2NzY1NCwgNDUuOTQyMjMzOTY0NzI0N10sIFstNjYuNjkzOTE4MDgyOTI5NCwgNDUuOTQ2NzYyNjYxOTgzOF0sIFstNjYuNjkxMjE0MTUzOTI0MiwgNDUuOTQ0OTI2MjQxNzU2OV0sIFstNjYuNjg5OTQ3NTI5MzczNiwgNDUuOTQ0NTAxNDgyODM3Nl0sIFstNjYuNjg5MDMxMjQ3NzgzOCwgNDUuOTQ0NDcwMjUwNDM1N10sIFstNjYuNjg4OTY4MzY1NzEzOSwgNDUuOTQ0MzgyNzk5NjE2N10sIFstNjYuNjg5OTU2NTEyNTI2NCwgNDUuOTQxODQwNDE5MDc4NV0sIFstNjYuNjkzNDE1MDI2MzcwMywgNDUuOTM4NjQ4MjIzMzkzXV0sIFtbLTY2LjY1NTAxMjA0Nzk3NDIsIDQ1LjkyOTE0NTUxMjE2OTNdLCBbLTY2LjY1NTc3NTYxNTk2NTcsIDQ1LjkyOTI3MDQ3NjIwMTddLCBbLTY2LjY1OTk3OTczMTQ5NTQsIDQ1LjkzMDkzODcxOTA2NzJdLCBbLTY2LjY2MjkxNzIyMjQ3NDQsIDQ1LjkzMjI3NTc3NjM3NTJdLCBbLTY2LjY2MzE4NjcxNzA1OTcsIDQ1LjkzMjQ3NTcwNzQwOF0sIFstNjYuNjYzMTIzODM0OTg5OCwgNDUuOTMyNzg4MDk4MjAzN10sIFstNjYuNjYxOTI5MDc1NjYxOSwgNDUuOTM0MTgxMzM5NzI4M10sIFstNjYuNjYxNjE0NjY1MzEyNSwgNDUuOTM0MDc1MTI5NzIzNV0sIFstNjYuNjYwMTg2MzQ0MDEwNywgNDUuOTM0ODE4NTk1NDg2XSwgWy02Ni42NTkxNDQyOTgyODExLCA0NS45MzUwOTk3MzU0MDQxXSwgWy02Ni42NTg2MDUzMDkxMTA2LCA0NS45MzUxMDU5ODI5NDE2XSwgWy02Ni42NTY0NjczMTg3MzQ1LCA0NS45MzQ4NzQ4MjM1ODM3XSwgWy02Ni42NTQyOTMzOTU3NDY5LCA0NS45MzQwNTAxMzkxMDQ1XSwgWy02Ni42NTI5OTA4Mzg1ODQ5LCA0NS45MzMzMTI5MTA3Nzk0XSwgWy02Ni42NTIzMDgxMTg5NjksIDQ1LjkzMjQ1Njk2MzkwNDNdLCBbLTY2LjY1MjE5MTMzNzk4MiwgNDUuOTMxOTY5NjMwNTg0NV0sIFstNjYuNjUyMjcyMTg2MzU3NiwgNDUuOTMxMzU3MzMzOTMzNV0sIFstNjYuNjUyMDQ3NjA3NTM2NiwgNDUuOTMwNTgyNTgxNTQ0NF0sIFstNjYuNjUyMTI4NDU1OTEyMSwgNDUuOTMwMTI2NDcyMjU0NF0sIFstNjYuNjUyNDQyODY2MjYxNiwgNDUuOTI5NjAxNjI5NTI2MV0sIFstNjYuNjUzMTE2NjAyNzI0NywgNDUuOTI5MzM5MjA2Mjk5Nl0sIFstNjYuNjU0MDUwODUwNjIwMiwgNDUuOTI5MTU4MDA4NTg1Ml0sIFstNjYuNjU1MDEyMDQ3OTc0MiwgNDUuOTI5MTQ1NTEyMTY5M11dLCBbWy02Ni42MzE4MDg1NjQxODU0LCA0NS44ODc4MzU3MjkzMzczXSwgWy02Ni42MzI4Nzc1NTkzNzM1LCA0NS44ODc5MzU3NzUwMTQ4XSwgWy02Ni42MzQxODAxMTY1MzU0LCA0NS44ODgyMTA4OTk2OTg3XSwgWy02Ni42MzUxNTAyOTcwNDIzLCA0NS44ODg1NDIyOTgwNzY5XSwgWy02Ni42MzYyNDYyNDE2ODg5LCA0NS44ODkwOTg3OTI3OTI0XSwgWy02Ni42MzcwMDk4MDk2ODA0LCA0NS44ODk2MzY1MjM5NjI0XSwgWy02Ni42MzgxNTk2NTMyNDQxLCA0NS44OTA5MTgzMDQwMTIzXSwgWy02Ni42Mzg1ODE4NjE0Mjc2LCA0NS44OTE4MTg2NTg2NTMyXSwgWy02Ni42Mzg3NDM1NTgxNzg4LCA0NS44OTI1Njg5NDMwMzc4XSwgWy02Ni42Mzg1OTA4NDQ1ODA1LCA0NS44OTQwNzU3MzM1NTgyXSwgWy02Ni42MzI3NTE3OTUyMzM3LCA0NS45MDA3MzM4ODI2NjJdLCBbLTY2LjYyOTIzMDM5OTMyLCA0NS45MDUwOTcxOTQyNTI1XSwgWy02Ni42Mjc2NjczMzA3MjU2LCA0NS45MDY0ODQ4ODA1MDE2XSwgWy02Ni42MjY0NTQ2MDUwOTIsIDQ1LjkwNzE5NzQ2MjY2MjddLCBbLTY2LjYyNTM4NTYwOTkwMzksIDQ1LjkwNzY2NjI2MTcyNzRdLCBbLTY2LjYyMzAyMzA0MDcwNjcsIDQ1LjkwODI5MTMyMDk4ODJdLCBbLTY2LjYyMDUwNzc1NzkxMTEsIDQ1LjkwODQ5MTMzODQ2NTFdLCBbLTY2LjYxODAwMTQ1ODI2ODUsIDQ1LjkwODI0MTMxNjUwNjRdLCBbLTY2LjYxODEwOTI1NjEwMjUsIDQ1LjkwODIxMDA2MzY4MjNdLCBbLTY2LjYxNzAzMTI3Nzc2MTYsIDQ1LjkwNzYwMzc1NTQxNDJdLCBbLTY2LjYxNjEyMzk3OTMyNDYsIDQ1LjkwNjg2NjE3NTYwMjhdLCBbLTY2LjYxNTA5MDkxNjc0NzksIDQ1LjkwNTQ5NzI1MTUwNDddLCBbLTY2LjYxNDc5NDQ3MjcwNDEsIDQ1LjkwNDc1MzM5Mjc0ODFdLCBbLTY2LjYxNDY0MTc1OTEwNTgsIDQ1LjkwMzc5MDczNzIwODNdLCBbLTY2LjYxNDY5NTY1ODAyMjksIDQ1LjkwMzAxNTU5OTgzNjddLCBbLTY2LjYxNDk3NDEzNTc2MSwgNDUuOTAyMDY1NDE2NjgxNF0sIFstNjYuNjE3MzQ1Njg4MTExLCA0NS44OTg5NzcyMDkxMTY0XSwgWy02Ni42MjAzODE5OTM3NzE0LCA0NS44OTU0MTk5MzEyNjE0XSwgWy02Ni42MjYzNDY4MDcyNTc5LCA0NS44ODkyMzYzNTI0MjQ0XSwgWy02Ni42MjgxMjU0NzE1MjA1LCA0NS44ODgzNjcyMTk5MzQ4XSwgWy02Ni42MjkxMzE1ODQ2Mzg3LCA0NS44ODgwNzk1OTAzNjA1XSwgWy02Ni42MzA0NTIxMDgxMDY0LCA0NS44ODc4NzMyNDY0ODc1XSwgWy02Ni42MzE4MDg1NjQxODU0LCA0NS44ODc4MzU3MjkzMzczXV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiAxLCAiTmVpZ2hib3VyaCI6ICJGcmVkZXJpY3RvbiBTb3V0aCIsICJPQkpFQ1RJRCI6IDEsICJTaGFwZV9BcmVhIjogMzI0MzE4ODkuMDAwMiwgIlNoYXBlX0xlbmciOiA0MDQxMi4yNzY3NDI5LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZDhkM2MiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjYzNTcxNjIzNTY3MTMsIDQ2LjAwODY5MDU3MjYyMzVdLCBbLTY2LjY0MDYzOTAwMzQyODMsIDQ2LjAwMjk3NTEzMTYwMzVdLCBbLTY2LjYzOTMxODQ3OTk2MDYsIDQ2LjAwMjM4ODU3OTEzODNdLCBbLTY2LjYzODIyMjUzNTMxNCwgNDYuMDAxNjE0ODE5NTY1Nl0sIFstNjYuNjM3Mzg3MTAyMDk5OCwgNDYuMDAwNjk3NTI2MDUzOF0sIFstNjYuNjM2ODU3MDk2MDgyMSwgNDUuOTk5Njc0MTMzMDMxNF0sIFstNjYuNjM2ODMwMTQ2NjIzNiwgNDUuOTk4ODUwNDEyNzAzM10sIFstNjYuNjM3MDI3Nzc1OTg2MSwgNDUuOTk3ODM5NDY2NDQ5OF0sIFstNjYuNjM3NDQ5OTg0MTY5NiwgNDUuOTk2ODU5NzA0NjE3Ml0sIFstNjYuNjM4MTA1NzU0MzI3LCA0NS45OTU5NDIzMzIyNzE0XSwgWy02Ni42Mzg5NzcxMjAxNTI2LCA0NS45OTUxMTIzMTU2MTU5XSwgWy02Ni42NDAwMTkxNjU4ODIyLCA0NS45OTQ0MDA4NjI4NTk3XSwgWy02Ni42NDEyODU3OTA0MzI4LCA0NS45OTM4MDE3Mzc2NTVdLCBbLTY2LjY0Mjk2NTY0MDAxNDEsIDQ1Ljk5MzE4Mzg4Mjk5NDNdLCBbLTY2LjY0NDc1MzI4NzQyOTUsIDQ1Ljk5MjcyMjA0NzczMjldLCBbLTY2LjY0NjYxMjgwMDA2NzcsIDQ1Ljk5MjQyMjQ3Njg1NF0sIFstNjYuNjQ4NTA4MjQ1MzE3MiwgNDUuOTkyMjg1MTcyOTkyNV0sIFstNjYuNjUwMDI2Mzk4MTQ3MywgNDUuOTkyMzAzODk2MjY2NF0sIFstNjYuNjUxNzY5MTI5Nzk4NSwgNDUuOTkwMzU2NjQxODU2M10sIFstNjYuNjQ1MjIwNDExMzc3MywgNDUuOTkxMTI0MzE3NjQwOF0sIFstNjYuNjQzMTM2MzE5OTE4MSwgNDUuOTkxMTExODM1MTkyOV0sIFstNjYuNjQxMDk3MTQ0MjIzMiwgNDUuOTkwODYyMTg1NjQzM10sIFstNjYuNjM5Nzc2NjIwNzU1NSwgNDUuOTkwNTYyNjA0Njk3M10sIFstNjYuNjM4MjA0NTY5MDA4MywgNDUuOTkwMDUwODE2ODNdLCBbLTY2LjYzNjE2NTM5MzMxMzMsIDQ1Ljk4ODgwMjUzMzg5MjFdLCBbLTY2LjYzNTE5NTIxMjgwNjUsIDQ1Ljk4ODM5NjgzNTg3NThdLCBbLTY2LjYzMzg5MjY1NTY0NDUsIDQ1Ljk4ODExNTk2NjI3NjVdLCBbLTY2LjYzMjc2OTc2MTUzOTQsIDQ1Ljk4ODA2NjAzMzc1NDFdLCBbLTY2LjYzMTg3MTQ0NjI1NTIsIDQ1Ljk4ODE1MzQxNTYzODhdLCBbLTY2LjYzMDY0MDc1NDMxNiwgNDUuOTg3OTE2MjM1OTE2Nl0sIFstNjYuNjI5MDc3Njg1NzIxNiwgNDUuOTg3MzE3MDQwNTEyOF0sIFstNjYuNjI3NjQ5MzY0NDE5OSwgNDUuOTg2MzEyMTI1MzI3MV0sIFstNjYuNjI1Nzg5ODUxNzgxOCwgNDUuOTg1NjgxNzAzMzgzMV0sIFstNjYuNjIzODMxNTI0NDYyNCwgNDUuOTg1MjA3MzIxNzQxXSwgWy02Ni41OTk2MDM5NjEyNDk3LCA0Ni4wMTQ5OTE4NDgxODQ4XSwgWy02Ni42MjMxMDM4ODkwODIyLCA0Ni4wMjIxMjIwMjk3MjcyXSwgWy02Ni42NjY0NjU1Njc4NDY3LCA0Ni4wMjA0MTkxMDQwNjM1XSwgWy02Ni42NjM4ODc0MDI5ODEzLCA0Ni4wMTQ2NDI0ODkzMjkxXSwgWy02Ni42NjA1NzI2MTk1ODI5LCA0Ni4wMDYwNTEzMTAyNTE1XSwgWy02Ni42NTk0Njc2OTE3ODM0LCA0Ni4wMDI0MjYwMTg4NDMyXSwgWy02Ni42NTk1MDM2MjQzOTQ4LCA0Ni4wMDEyMDI5NzUzODAzXSwgWy02Ni42NTg0MjU2NDYwNTM4LCA0Ni4wMDE5ODkyMjA3MTAxXSwgWy02Ni42NTY5ODgzNDE1OTkyLCA0Ni4wMDI0MTM1Mzg5NDQ0XSwgWy02Ni42NTU2MTM5MTkyMTQ1LCA0Ni4wMDI0Mzg0OTg3MzkyXSwgWy02Ni42NTQxNDk2NjUzMDE0LCA0Ni4wMDIwNTc4NjA2NDUxXSwgWy02Ni42NTQ4NjgzMTc1Mjg3LCA0Ni4wMDMwMjUwNTA2NzUxXSwgWy02Ni42NTUyNDU2MDk5NDgsIDQ2LjAwNDA3MzM0MDc3MzhdLCBbLTY2LjY1NTI2MzU3NjI1MzcsIDQ2LjAwNTE1OTA0ODg2NDNdLCBbLTY2LjY1NDkyMjIxNjQ0NTgsIDQ2LjAwNjIxOTc3NzU2OTZdLCBbLTY2LjY1Mzk1MjAzNTkzODksIDQ2LjAwNzQ5MjYyNTE2ODFdLCBbLTY2LjY1MjYwNDU2MzAxMjcsIDQ2LjAwODMwMzczODI2MDZdLCBbLTY2LjY1MDcxODEwMDkxNjEsIDQ2LjAwODgyMTU5NjU1MjVdLCBbLTY2LjY0ODY5Njg5MTUyNjgsIDQ2LjAwODg5NjQ2NzIyOTddLCBbLTY2LjY0OTYwNDE4OTk2MzgsIDQ2LjAxMDA4ODE0NTE5NzldLCBbLTY2LjY1MDA0NDM2NDQ1MywgNDYuMDExMjA0OTMwMDQwNV0sIFstNjYuNjQ5NTk1MjA2ODEwOSwgNDYuMDExODQ3NTM5MDMwN10sIFstNjYuNjQ4ODc2NTU0NTgzNiwgNDYuMDEyMzQ2NjQ3NjU3OF0sIFstNjYuNjQ4MTEyOTg2NTkyMSwgNDYuMDEyNjA4Njc3ODg0XSwgWy02Ni42NDc0NDgyMzMyODE5LCA0Ni4wMTI3MDg0OTg1OTZdLCBbLTY2LjY0NTYyNDY1MzI1NTEsIDQ2LjAxMjU4OTk2MTQ4MDRdLCBbLTY2LjY0MzA1NTQ3MTU0MjUsIDQ2LjAxMjE2NTcyMTMwMDldLCBbLTY2LjY0MDE4OTg0NTc4NjIsIDQ2LjAxMTM5MjA5ODQ3ODJdLCBbLTY2LjY0MDk5ODMyOTU0MTksIDQ2LjAxMjYzMzYzMzA3ODldLCBbLTY2LjY0MTIzMTg5MTUxNTgsIDQ2LjAxMzE5NTEyMTk4NjldLCBbLTY2LjY0MTE5NTk1ODkwNDQsIDQ2LjAxMzQ4ODM0MTcwNjRdLCBbLTY2LjY0MDkzNTQ0NzQ3MiwgNDYuMDE0MTk5NTQ5MDM1Nl0sIFstNjYuNjQwNTQ5MTcxODk5OCwgNDYuMDE0NzIzNTkwNjg4OF0sIFstNjYuNjM5NDA4MzExNDg5LCA0Ni4wMTU1ODQ1MDU0ODE0XSwgWy02Ni42MzgxNzc2MTk1NDk4LCA0Ni4wMTU5NTI1NzM2NTc5XSwgWy02Ni42MzUzODM4NTkwMTYyLCA0Ni4wMTYzMDE5MjQyMzcxXSwgWy02Ni42MzM3NzU4NzQ2NTc2LCA0Ni4wMTYzMzMxMTYxNDU4XSwgWy02Ni42MzAzNjIyNzY1Nzc5LCA0Ni4wMTYxNDU5NjQ0Mjk4XSwgWy02Ni42MzA2NzY2ODY5Mjc0LCA0Ni4wMTQzOTI5NDU5MzgxXSwgWy02Ni42MzA5NjQxNDc4MTgzLCA0Ni4wMDc0MjM5OTE5NzZdLCBbLTY2LjYzMzYwNTE5NDc1MzYsIDQ2LjAwODAyOTIwOTAwN10sIFstNjYuNjM1NzE2MjM1NjcxMywgNDYuMDA4NjkwNTcyNjIzNV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogMiwgIk5laWdoYm91cmgiOiAiQnJvb2tzaWRlIiwgIk9CSkVDVElEIjogMiwgIlNoYXBlX0FyZWEiOiAxMDQ0MzU4My42NTk4LCAiU2hhcGVfTGVuZyI6IDIyMDEwLjYzMTA2NjIsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZmZmZiMiIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNzEwNTU0ODgxOTkxMywgNDUuOTc1Nzc1MDIxODMxMV0sIFstNjYuNzA1NTE1MzMzMjQ3NCwgNDUuOTc2MDEyMjUzNTcxMl0sIFstNjYuNzAxMzQ3MTUwMzI5MSwgNDUuOTc2ODMwMDcwOTg5N10sIFstNjYuNjk5ODgyODk2NDE1OSwgNDUuOTc2OTA0OTg0OTU4NV0sIFstNjYuNjk4OTkzNTY0Mjg0NywgNDUuOTc2NzE3Njk5ODQ2NF0sIFstNjYuNjk4NDQ1NTkxOTYxNCwgNDUuOTc5MTk2MDU0ODkxXSwgWy02Ni42OTgxNzYwOTczNzYxLCA0NS45ODI4MTY2MjYwNzY3XSwgWy02Ni42OTg2NzkxNTM5MzUyLCA0NS45ODY0MTgyMzUyNDU0XSwgWy02Ni43MDAyNTEyMDU2ODI0LCA0NS45ODkyNDU2Nzc1NTgxXSwgWy02Ni43MDIxMTA3MTgzMjA2LCA0NS45OTE5ODU1OTk3NDg5XSwgWy02Ni43MTkyNDE1OTA3ODg3LCA0NS45OTMyOTYyMjA3MTg0XSwgWy02Ni43MzMxODM0NDM5OTgzLCA0NS45NzY2NTUyNzEzMzQ5XSwgWy02Ni43MzI3NzkyMDIxMjA0LCA0NS45NzY1MjQxNzEyMzE4XSwgWy02Ni43MzExODkxODQwNjc1LCA0NS45NzYzNDkzNzA2MTE1XSwgWy02Ni43MzA2NTkxNzgwNDk5LCA0NS45NzY0NTU0OTk2MjU0XSwgWy02Ni43MjgxMTY5NDU3OTU4LCA0NS45NzY0NTU0OTk2MjU0XSwgWy02Ni43MjYzMjAzMTUyMjc2LCA0NS45NzYyNjE5NzAwOTQ0XSwgWy02Ni43MjI2MDEyODk5NTEzLCA0NS45NzYwNzQ2ODI4MDc2XSwgWy02Ni43MjAzMDE2MDI4MjQsIDQ1Ljk3NjI2MTk3MDA5NDRdLCBbLTY2LjcxNjgwNzE1NjM2ODgsIDQ1Ljk3NjMxMTkxMzI2MzldLCBbLTY2LjcxMDU1NDg4MTk5MTMsIDQ1Ljk3NTc3NTAyMTgzMTFdXSwgW1stNjYuNzIwMTEyOTU2NjE0MywgNDUuOTc3NzYwMjQ1NTg1OF0sIFstNjYuNzIxNDA2NTMwNjIzNCwgNDUuOTc3ODIyNjcyODUxNV0sIFstNjYuNzI0NDUxODE5NDM2NiwgNDUuOTc3OTc4NzQwNzA3OF0sIFstNjYuNzIwNTcxMDk3NDA5MiwgNDUuOTgyNzcyOTMwOTM5M10sIFstNjYuNzIwMDUwMDc0NTQ0NCwgNDUuOTgzMDc4Nzk2MTc2NF0sIFstNjYuNzE5NTM4MDM0ODMyNSwgNDUuOTgzMjIyMzY0OTkwNl0sIFstNjYuNzE4NDYwMDU2NDkxNSwgNDUuOTgzMTg0OTEyMjkyM10sIFstNjYuNzE3ODY3MTY4NDA0LCA0NS45ODI5NDc3MTEyODE3XSwgWy02Ni43MTczNjQxMTE4NDQ5LCA0NS45ODI0OTIwMzI4MDQ2XSwgWy02Ni43MTcxOTM0MzE5NDA5LCA0NS45ODIwMzAxMDgzMjg1XSwgWy02Ni43MTczMTAyMTI5Mjc5LCA0NS45ODE0NjgzMDMwOTYxXSwgWy02Ni43MjAxMTI5NTY2MTQzLCA0NS45Nzc3NjAyNDU1ODU4XV0sIFtbLTY2LjcwNDU3MjEwMjE5OSwgNDUuOTc4MzQwODE2NDQwNl0sIFstNjYuNzA1Mzk4NTUyMjYwNCwgNDUuOTc5OTUxNDAwNDkyOV0sIFstNjYuNzA1NjE0MTQ3OTI4NiwgNDUuOTgxMzYyMTgzNjg5OF0sIFstNjYuNzA1MjcyNzg4MTIwNywgNDUuOTgyMzIzNDkzMjM5Nl0sIFstNjYuNzA0Njg4ODgzMTg2LCA0NS45ODI2MTY4NzY1OTZdLCBbLTY2LjcwMzk3MDIzMDk1ODcsIDQ1Ljk4MjY4NTU0MDU2MTJdLCBbLTY2LjcwMzM5NTMwOTE3NjgsIDQ1Ljk4MjU1NDQ1NDczNTVdLCBbLTY2LjcwMTYyNTYyODA2NzEsIDQ1Ljk4MDU0NDQzMzIwNzNdLCBbLTY2LjcwMTI0ODMzNTY0NzgsIDQ1Ljk3OTY3NjczMDU1NzJdLCBbLTY2LjcwMTA5NTYyMjA0OTUsIDQ1Ljk3ODU5Njc2NTA5OTJdLCBbLTY2LjcwNDU3MjEwMjE5OSwgNDUuOTc4MzQwODE2NDQwNl1dLCBbWy02Ni43MTAxOTU1NTU4Nzc2LCA0NS45NzYyMjQ1MTI2ODc3XSwgWy02Ni43MTEwNDg5NTUzOTc2LCA0NS45NzYzMTE5MTMyNjM5XSwgWy02Ni43MTE2Nzc3NzYwOTY0LCA0NS45NzY0OTkxOTk3NDg0XSwgWy02Ni43MTIxMzU5MTY4OTEzLCA0NS45NzcwNTQ4MTI1OTIxXSwgWy02Ni43MTIxNDQ5MDAwNDQyLCA0NS45Nzc5MTAwNzA5MDUyXSwgWy02Ni43MTY3NzEyMjM3NTc0LCA0NS45Nzc2NDE2MzM1ODddLCBbLTY2LjcxNTg0NTk1OTAxNDcsIDQ1Ljk3ODk1ODgzNjc5MDddLCBbLTY2LjcxNDcwNTA5ODYwMzksIDQ1Ljk4MDE5NDg1Njc5NjldLCBbLTY2LjcxMzA4ODEzMTA5MjUsIDQ1Ljk4MTU0MzIxMDc4OThdLCBbLTY2LjcxMTczMTY3NTAxMzUsIDQ1Ljk4MjM2NzE4ODczMTZdLCBbLTY2LjcxMDcwNzU5NTU4OTYsIDQ1Ljk4MjYzNTYwMzE0MDRdLCBbLTY2LjcwOTgwOTI4MDMwNTUsIDQ1Ljk4MjY4NTU0MDU2MTJdLCBbLTY2LjcwODQ4ODc1NjgzNzgsIDQ1Ljk4MjA0MjU5MjgyNDVdLCBbLTY2LjcwNzUxODU3NjMzMSwgNDUuOTgxMTQ5OTQ0MjY3MV0sIFstNjYuNzA3MDk2MzY4MTQ3NCwgNDUuOTgwNDA3MDk5ODgwN10sIFstNjYuNzA3MTMyMzAwNzU4OCwgNDUuOTgwMjAxMDk5MjUyMV0sIFstNjYuNzA3NDY0Njc3NDEzOSwgNDUuOTc5MjE0NzgyNTkyNV0sIFstNjYuNzA4MTY1MzYzMzM1NSwgNDUuOTc4MTAzNTk0Njc2Ml0sIFstNjYuNzA3MzU2ODc5NTc5OCwgNDUuOTc4MTU5Nzc4ODcwMl0sIFstNjYuNzA3Mzc0ODQ1ODg1NSwgNDUuOTc4MDM0OTI1MDI4NV0sIFstNjYuNzA3ODY4OTE5MjkxOCwgNDUuOTc3MTE3MjQwNjUzMV0sIFstNjYuNzA4NzEzMzM1NjU4OCwgNDUuOTc2NTA1NDQyNjIwM10sIFstNjYuNzA5MzUxMTM5NTEwNiwgNDUuOTc2MzExOTEzMjYzOV0sIFstNjYuNzEwMTk1NTU1ODc3NiwgNDUuOTc2MjI0NTEyNjg3N11dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogMywgIk5laWdoYm91cmgiOiAiRG91Z2xhcyIsICJPQkpFQ1RJRCI6IDMsICJTaGFwZV9BcmVhIjogMzIzMTQ1Ni40MzM4NywgIlNoYXBlX0xlbmciOiAxMzYwNC44Mjk1OTAxLCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjY4MTM3NzYwMTU2MzEsIDQ2LjAxNzAwMDYxODc3NDddLCBbLTY2LjY4MDI4MTY1NjkxNjUsIDQ2LjAxNjE1MjIwMjgzMDZdLCBbLTY2LjY3OTA4Njg5NzU4ODYsIDQ2LjAxNDk5ODA4NjcxNTddLCBbLTY2LjY3ODEwNzczMzkyODksIDQ2LjAxMzc1MDM2NjUyMzRdLCBbLTY2LjY3NzM1MzE0OTA5MDIsIDQ2LjAxMjQyNzc1MjM4NDNdLCBbLTY2LjY3NzExOTU4NzExNjQsIDQ2LjAxMTg3ODczMzQ1MThdLCBbLTY2LjY3NjU2MjYzMTY0MDIsIDQ2LjAwOTA1MjQ0NzQ4MTddLCBbLTY2LjY3NTY0NjM1MDA1MDQsIDQ2LjAwNTU0NTkwNTIxODldLCBbLTY2LjY3NDczOTA1MTYxMzQsIDQ2LjAwMjc2Mjk3NTA0NjddLCBbLTY2LjY3MzM5MTU3ODY4NzMsIDQ1Ljk5OTMxODQzNzEyMTRdLCBbLTY2LjY3MTI5ODUwNDA3NTMsIDQ1Ljk5Njk0NzA3MjYxODldLCBbLTY2LjY2ODgxMDE3MDczODIsIDQ1Ljk5NDc2OTA3MjAwN10sIFstNjYuNjY2NDAyNjg1Nzc2OCwgNDUuOTkzMDc3Nzg2MDQ1NV0sIFstNjYuNjY1NjkzMDE2NzAyNCwgNDUuOTkzMjgzNzM4NzYwNF0sIFstNjYuNjYzMzM5NDMwNjU4LCA0NS45OTQyMDczOTYwNTQ4XSwgWy02Ni42NjEyNDYzNTYwNDYsIDQ1Ljk5NTM5MzE0OTcxMjRdLCBbLTY2LjY2MDQ1NTgzODU5NTksIDQ1Ljk5NzA5Njg0NjAxNTFdLCBbLTY2LjY1OTg4OTg5OTk2NjksIDQ1Ljk5ODg1MDQxMjcwMzNdLCBbLTY2LjY1OTU1NzUyMzMxMTgsIDQ2LjAwMDYyODg4NDQzMTFdLCBbLTY2LjY1OTQ2NzY5MTc4MzQsIDQ2LjAwMjQyNjAxODg0MzJdLCBbLTY2LjY2MDU3MjYxOTU4MjksIDQ2LjAwNjA1MTMxMDI1MTVdLCBbLTY2LjY2MzU1NTAyNjMyNjIsIDQ2LjAxMzgwNjUxNDUzNjldLCBbLTY2LjY2NjQ2NTU2Nzg0NjcsIDQ2LjAyMDQxOTEwNDA2MzVdLCBbLTY2LjY4MTUyMTMzMjAwODUsIDQ2LjAxOTc1MTY0MjcwMDldLCBbLTY2LjY4MTM3NzYwMTU2MzEsIDQ2LjAxNzAwMDYxODc3NDddXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDQsICJOZWlnaGJvdXJoIjogIk1jTGVvZCBIaWxsIiwgIk9CSkVDVElEIjogNCwgIlNoYXBlX0FyZWEiOiAzMTU4NjUyLjMxNDU4LCAiU2hhcGVfTGVuZyI6IDc3OTkuODkxMzQ1NiwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmVkOTc2IiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni42MDc2OTc3ODE5NTk2LCA0NS45NzU0NTAzODcyNzY3XSwgWy02Ni42MDUxMTA2MzM5NDEzLCA0NS45NzUwNDQ1OTE0MDc1XSwgWy02Ni42MDI5OTA2MDk4NzA4LCA0NS45NzQ0NzAyMjkwOTQ0XSwgWy02Ni42MDE5NDg1NjQxNDEyLCA0NS45NzQwNjQ0MjYwNDI4XSwgWy02Ni42MDE4Njc3MTU3NjU3LCA0NS45NzIxNjY0NzY5MTEyXSwgWy02Ni42MDE1NDQzMjIyNjM0LCA0NS45NzAyODA5NDk4ODQyXSwgWy02Ni42MDA4NTI2MTk0OTQ2LCA0NS45NjgwNTgxOTMyMDczXSwgWy02Ni42MDAzNDk1NjI5MzU1LCA0NS45NjcyMDkwMjY2NjA1XSwgWy02Ni41OTgwNjc4NDIxMTM4LCA0NS45NjQzODY3MDMxMzhdLCBbLTY2LjU5NTQ4MDY5NDA5NTYsIDQ1Ljk2MTY5NTM3MTMzOTRdLCBbLTY2LjU5MjU5NzEwMjAzMzYsIDQ1Ljk1OTE2MDAyOTY4NzVdLCBbLTY2LjU4OTQzNTAzMjIzMzUsIDQ1Ljk1Njc4Njk0NDcwNzhdLCBbLTY2LjU3NDQ5NjA0OTA1ODUsIDQ1Ljk3MzkxNDU5MDMxODNdLCBbLTY2LjU1MDM0OTMzNDIyMTQsIDQ2LjAwMjA1MTYyMDY1NDZdLCBbLTY2LjU4MjEwNDc3OTUxNSwgNDYuMDA5MDA4NzczMDU1NF0sIFstNjYuNTkyMjAxODQzMzA4NSwgNDYuMDEzMjU3NTA5MjkxNV0sIFstNjYuNTk0ODk2Nzg5MTYwOSwgNDYuMDEzODY4OTAxMTUxOF0sIFstNjYuNjE0MTM4NzAyNTQ2NywgNDUuOTkwOTkzMjUxNzk3Ml0sIFstNjYuNjExOTM3ODMwMTAwNiwgNDUuOTkwMjk0MjI4NzIyOV0sIFstNjYuNjA5NTc1MjYwOTAzNCwgNDUuOTg5MjE0NDcwMzczOF0sIFstNjYuNjA4OTI4NDczODk4OCwgNDUuOTg5NjEzOTIxMDA0XSwgWy02Ni42MDgzMDg2MzYzNTI4LCA0NS45ODk4MzIzNjkzNDgxXSwgWy02Ni42MDY4NzEzMzE4OTgyLCA0NS45ODk5Njk2NzkyOTQ1XSwgWy02Ni42MDUyMDk0NDg2MjI2LCA0NS45ODk3MzI1MDczNTQ5XSwgWy02Ni42MDM3OTAxMTA0NzM3LCA0NS45ODkxMDIxMjQzNjQ2XSwgWy02Ni42MDI3NzUwMTQyMDI2LCA0NS45ODgxNTk2NTcxOTY3XSwgWy02Ni42MDE3Njg5MDEwODQ0LCA0NS45ODYxMzczNTU2MDY0XSwgWy02Ni42MDEyNDc4NzgyMTk2LCA0NS45ODQzMjA5NjYyMDA2XSwgWy02Ni42MDEwOTUxNjQ2MjEzLCA0NS45ODI0NjcwNjQwMTI1XSwgWy02Ni41OTk5OTkyMTk5NzQ3LCA0NS45ODc4Mjg4NTM2NTc1XSwgWy02Ni41OTk4ODI0Mzg5ODc4LCA0NS45ODkxMTQ2MDcyNjU4XSwgWy02Ni41OTkzOTczNDg3MzQzLCA0NS45OTAzNTY2NDE4NTYzXSwgWy02Ni41OTg1Nzk4ODE4MjU4LCA0NS45OTE1MTEyNzIxMzAxXSwgWy02Ni41OTc2NTQ2MTcwODMxLCA0NS45OTIzNzI1NDgyMTY1XSwgWy02Ni41OTYzMDcxNDQxNTcsIDQ1Ljk5MzI1MjUzMzg1MjhdLCBbLTY2LjU5NTAxMzU3MDE0NzgsIDQ1Ljk5MzgzMjk0MjI1MjldLCBbLTY2LjU5MjM4MTUwNjM2NTQsIDQ1Ljk5NDQzODMwNzk2OTddLCBbLTY2LjU5MDY1Njc0MTAxOTksIDQ1Ljk5MzgzMjk0MjI1MjldLCBbLTY2LjU4OTA5MzY3MjQyNTUsIDQ1Ljk5MzA0MDM0MDAxNTFdLCBbLTY2LjU4Nzg2Mjk4MDQ4NjMsIDQ1Ljk5MTg3MzI1OTM2NDRdLCBbLTY2LjU4NjY1MDI1NDg1MjcsIDQ1Ljk5MDM0NDE1OTIzNTJdLCBbLTY2LjU4NTg3NzcwMzcwODMsIDQ1Ljk4ODk5NjAxOTU5MTFdLCBbLTY2LjU4NTkzMTYwMjYyNTQsIDQ1Ljk4ODI2NTc2MzU3MzVdLCBbLTY2LjU4NjMzNTg0NDUwMzIsIDQ1Ljk4NzU5MTY3MjU0NDddLCBbLTY2LjU4NzAzNjUzMDQyNDgsIDQ1Ljk4NzA0ODY0ODgwMTVdLCBbLTY2LjU4Nzk2MTc5NTE2NzUsIDQ1Ljk4NjY5OTExMzQ1OTJdLCBbLTY2LjU4OTQ4ODkzMTE1MDUsIDQ1Ljk4NjQ4Njg5NDQ5NTldLCBbLTY2LjU4OTc1ODQyNTczNTcsIDQ1Ljk4NjEzNzM1NTYwNjRdLCBbLTY2LjU5MDE4OTYxNzA3MjEsIDQ1Ljk4NTM4ODMzNjI2ODNdLCBbLTY2LjU5MDUwNDAyNzQyMTUsIDQ1Ljk4NDQxNDU5NTk3NzNdLCBbLTY2LjU5MDc4MjUwNTE1OTYsIDQ1Ljk4MDc1NjY3NDk1MTFdLCBbLTY2LjU5MTQwMjM0MjcwNTcsIDQ1Ljk4MDA4ODczNDk0OThdLCBbLTY2LjU5MjAyMjE4MDI1MTcsIDQ1Ljk3OTgyNjU1MDY5MTFdLCBbLTY2LjU5Mjg3NTU3OTc3MTYsIDQ1Ljk3OTcyNjY3MDY0NjldLCBbLTY2LjU5NTc2ODE1NDk4NjUsIDQ1Ljk4MDI0NDc5NjQxOTJdLCBbLTY2LjU5NzYyNzY2NzYyNDYsIDQ1Ljk4MDc4MTY0NDUxNDZdLCBbLTY2LjU5OTI4MDU2Nzc0NzQsIDQ1Ljk4MTQxMjEyMjI1OTNdLCBbLTY2LjYwMDM0OTU2MjkzNTUsIDQ1Ljk4MTk0MjcxNjc3NzldLCBbLTY2LjYwMTA5NTE2NDYyMTMsIDQ1Ljk4MjQ2NzA2NDAxMjVdLCBbLTY2LjYwMTM5MTYwODY2NTEsIDQ1Ljk3OTMzMzM5MTIyMTRdLCBbLTY2LjYwMzMwNTAyMDIyMDMsIDQ1Ljk3OTQ0NTc1NzA1NjZdLCBbLTY2LjYwNDY3OTQ0MjYwNDksIDQ1Ljk3OTc3MDM2ODE4ODRdLCBbLTY2LjYwNDg3NzA3MTk2NzUsIDQ1Ljk3ODU4NDI3OTgyNjJdLCBbLTY2LjYwNTQyNTA0NDI5MDgsIDQ1Ljk3NzQ2MDU5MzczMDZdLCBbLTY2LjYwNjMwNTM5MzI2OTIsIDQ1Ljk3NjQ0MzAxMzg2OTZdLCBbLTY2LjYwNzY5Nzc4MTk1OTYsIDQ1Ljk3NTQ1MDM4NzI3NjddXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDUsICJOZWlnaGJvdXJoIjogIk1hcnlzdmlsbGUiLCAiT0JKRUNUSUQiOiA1LCAiU2hhcGVfQXJlYSI6IDE0MTE5NDQwLjQyMDEsICJTaGFwZV9MZW5nIjogMjI1NTAuNTEwODMyMSwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmViMjRjIiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni42MzQ5MDc3NTE5MTU2LCA0NS45NjkwMTk3MzM3MjgxXSwgWy02Ni42MzQ1MDM1MTAwMzc3LCA0NS45NjkwNjk2ODM0MjldLCBbLTY2LjYzMzQ3OTQzMDYxMzgsIDQ1Ljk2ODQ4Mjc3MTU5OTFdLCBbLTY2LjYyOTU2Mjc3NTk3NTEsIDQ1Ljk3MjcyMjEzMzIyNjJdLCBbLTY2LjYyOTMxMTI0NzY5NTUsIDQ1Ljk3NDIyMDUwNDQ5MTVdLCBbLTY2LjYyMTc5MjM0ODc2NzQsIDQ1Ljk4MTg5Mjc3ODY4N10sIFstNjYuNTk0ODk2Nzg5MTYwOSwgNDYuMDEzODY4OTAxMTUxOF0sIFstNjYuNTk5NjAzOTYxMjQ5NywgNDYuMDE0OTkxODQ4MTg0OF0sIFstNjYuNjMwMzgwMjQyODgzNiwgNDUuOTc3MTQyMjExODU3OF0sIFstNjYuNjM0MDYzMzM1NTQ4NSwgNDUuOTcyNzk3MDUyNzUyMl0sIFstNjYuNjMzODkyNjU1NjQ0NSwgNDUuOTcxOTQxNzE1NDY5OF0sIFstNjYuNjMyMzM4NTcwMjAzLCA0NS45NzE1NDIxMzczMjJdLCBbLTY2LjYzMzM4OTU5OTA4NTQsIDQ1Ljk3MDI0MzQ4ODQzMl0sIFstNjYuNjM0OTA3NzUxOTE1NiwgNDUuOTY5MDE5NzMzNzI4MV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogNiwgIk5laWdoYm91cmgiOiAiU2FpbnQgTWFyeSdzIEZpcnN0IE5hdGlvbiIsICJPQkpFQ1RJRCI6IDYsICJTaGFwZV9BcmVhIjogMTg1MTQzNS4xNzI0OCwgIlNoYXBlX0xlbmciOiAxMjM2Ny42MTg2MjE0LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjYwMDExNjAwMDk2MTYsIDQ1Ljk4NzQxNjkwNjg2MzhdLCBbLTY2LjU5NzEwNjY0NDc1OTgsIDQ1Ljk4NjgwNTIyMjYzNTddLCBbLTY2LjU5MzY5MzA0NjY4MDIsIDQ1Ljk4NjQzNjk2MDUwNF0sIFstNjYuNTkxMjc2NTc4NTY1OSwgNDUuOTg2MzgwNzg0NzA5Ml0sIFstNjYuNTg5MjY0MzUyMzI5NSwgNDUuOTg2NTExODYxNDc1XSwgWy02Ni41ODc3OTExMTUyNjM1LCA0NS45ODY3NDI4MDU0OTc2XSwgWy02Ni41ODY2NTAyNTQ4NTI3LCA0NS45ODcyOTgzMTU1NTE5XSwgWy02Ni41ODU5NzY1MTgzODk2LCA0NS45ODgxNDcxNzQwODAyXSwgWy02Ni41ODU4Nzc3MDM3MDgzLCA0NS45ODg5OTYwMTk1OTExXSwgWy02Ni41ODcyMTYxOTM0ODE3LCA0NS45OTExMjQzMTc2NDA4XSwgWy02Ni41ODkwOTM2NzI0MjU1LCA0NS45OTMwNDAzNDAwMTUxXSwgWy02Ni41OTA2NTY3NDEwMTk5LCA0NS45OTM4MzI5NDIyNTI5XSwgWy02Ni41OTIzODE1MDYzNjU0LCA0NS45OTQ0MzgzMDc5Njk3XSwgWy02Ni41OTUwMTM1NzAxNDc4LCA0NS45OTM4MzI5NDIyNTI5XSwgWy02Ni41OTU1NDM1NzYxNjU1LCA0NS45OTM2MjA3NTA2NDA1XSwgWy02Ni41OTY3ODMyNTEyNTc1LCA0NS45OTI5ODQxNzA5MjE4XSwgWy02Ni41OTgwNDk4NzU4MDgyLCA0NS45OTIwNDE3Njk4NTU2XSwgWy02Ni41OTg4ODUzMDkwMjI0LCA0NS45OTExNDMwNDEzMDc0XSwgWy02Ni41OTk1OTQ5NzgwOTY4LCA0NS45ODk5NTA5NTUyMzFdLCBbLTY2LjU5OTkyNzM1NDc1MiwgNDUuOTg4OTAyMzk3NTYzMV0sIFstNjYuNjAwMTE2MDAwOTYxNiwgNDUuOTg3NDE2OTA2ODYzOF1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogNywgIk5laWdoYm91cmgiOiAiU2FuZHl2aWxsZSIsICJPQkpFQ1RJRCI6IDcsICJTaGFwZV9BcmVhIjogNzI4ODU5LjQ4MTAwMSwgIlNoYXBlX0xlbmciOiAzMTc1LjQyMDA2NDU0LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjU4OTQ4ODkzMTE1MDUsIDQ1Ljk4NjQ4Njg5NDQ5NTldLCBbLTY2LjU5MTU3MzAyMjYwOTcsIDQ1Ljk4NjM3NDU0Mjk1MDddLCBbLTY2LjU5NDA2MTM1NTk0NjcsIDQ1Ljk4NjQ2ODE2OTI1NDJdLCBbLTY2LjU5NzUzNzgzNjA5NjIsIDQ1Ljk4Njg3Mzg4MTQwNjJdLCBbLTY2LjYwMDExNjAwMDk2MTYsIDQ1Ljk4NzQxNjkwNjg2MzhdLCBbLTY2LjYwMTA5NTE2NDYyMTMsIDQ1Ljk4MjQ2NzA2NDAxMjVdLCBbLTY2LjU5OTUwNTE0NjU2ODQsIDQ1Ljk4MTUwNTc1Njk1NTZdLCBbLTY2LjU5NjUyMjczOTgyNTEsIDQ1Ljk4MDQ0NDU1NDQ1ODFdLCBbLTY2LjU5MzE2MzA0MDY2MjUsIDQ1Ljk3OTc1MTY0MDY3NDhdLCBbLTY2LjU5MjQ0NDM4ODQzNTMsIDQ1Ljk3OTc0NTM5ODE2ODldLCBbLTY2LjU5MTg4NzQzMjk1OTEsIDQ1Ljk3OTg2NDAwNTY2MTJdLCBbLTY2LjU5MTIwNDcxMzM0MzIsIDQ1Ljk4MDIyNjA2OTA2NjFdLCBbLTY2LjU5MDc4MjUwNTE1OTYsIDQ1Ljk4MDc1NjY3NDk1MTFdLCBbLTY2LjU5MDQ2ODA5NDgxMDIsIDQ1Ljk4NDYxNDMzODk3MThdLCBbLTY2LjU5MDA5OTc4NTU0MzcsIDQ1Ljk4NTU4MTgzMzkwMTVdLCBbLTY2LjU4OTQ4ODkzMTE1MDUsIDQ1Ljk4NjQ4Njg5NDQ5NTldXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDgsICJOZWlnaGJvdXJoIjogIktub2IgSGlsbCIsICJPQkpFQ1RJRCI6IDgsICJTaGFwZV9BcmVhIjogNTQ1MDIzLjE0NTc1MywgIlNoYXBlX0xlbmciOiAyOTc1LjkzNjQ4NDUzLCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjYwMTk0ODU2NDE0MTIsIDQ1Ljk3NDA2NDQyNjA0MjhdLCBbLTY2LjYwMzIwNjIwNTUzOSwgNDUuOTc0NTMyNjYwMDY5Ml0sIFstNjYuNjA2MTE2NzQ3MDU5NSwgNDUuOTc1MjUwNjExMjIwNF0sIFstNjYuNjA3Nzg3NjEzNDg4LCA0NS45NzU0NjI4NzMyNTYzXSwgWy02Ni42MTEwMDM1ODIyMDUyLCA0NS45NzU1ODc3MzI4OTc0XSwgWy02Ni42MTE5NzM3NjI3MTIsIDQ1Ljk3NTM5NDIwMDMzMzhdLCBbLTY2LjYxMjkwODAxMDYwNzUsIDQ1Ljk3NDg4MjI3MjIyNzNdLCBbLTY2LjYxMzQxMTA2NzE2NjYsIDQ1Ljk3NDI3MDQ0OTUwMjJdLCBbLTY2LjYxMzU3Mjc2MzkxNzcsIDQ1Ljk3MzQ1MjU5NDI4MjNdLCBbLTY2LjYxMzMyMTIzNTYzODIsIDQ1Ljk3Mjc3MjA3OTU4ODFdLCBbLTY2LjYxMjYyOTUzMjg2OTQsIDQ1Ljk3MjEwNDA0MzI2OV0sIFstNjYuNjA2MTk3NTk1NDM1MSwgNDUuOTY4NzQ1MDA5NTY4M10sIFstNjYuNjA0NjE2NTYwNTM1MSwgNDUuOTY1NDEwNzQ4NjQ4XSwgWy02Ni42MDM4Nzk5NDIwMDIxLCA0NS45NjQ4ODYyMzk4OTc5XSwgWy02Ni42MDI1OTUzNTExNDU4LCA0NS45NjQyNDMwODU0ODU5XSwgWy02Ni42MDA4ODg1NTIxMDYsIDQ1Ljk2Mzc2ODUyMDE2MTVdLCBbLTY2LjU5OTMxNjUwMDM1ODgsIDQ1Ljk2MzYxMjQxMjI1ODNdLCBbLTY2LjU5NzQ4MzkzNzE3OTIsIDQ1Ljk2MzczNzI5ODYxNl0sIFstNjYuNjAwNjk5OTA1ODk2MywgNDUuOTY3Njg5ODA2Mzc3Nl0sIFstNjYuNjAxMzU1Njc2MDUzNywgNDUuOTY5NTMxNzE2MDI2NV0sIFstNjYuNjAxNzA2MDE5MDE0NSwgNDUuOTcxMDMwMTczNjA3XSwgWy02Ni42MDE5NDg1NjQxNDEyLCA0NS45NzQwNjQ0MjYwNDI4XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiA5LCAiTmVpZ2hib3VyaCI6ICJZb3VuZ3MgQ3Jvc3NpbmciLCAiT0JKRUNUSUQiOiA5LCAiU2hhcGVfQXJlYSI6IDc0ODQ5MC4wODMxMjUsICJTaGFwZV9MZW5nIjogNDA5Ni4yMzk3MjIzMiwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmVkOTc2IiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni42MjM3Nzc2MjU1NDUzLCA0NS45NTU0MzE3NDI2OTU1XSwgWy02Ni42MjMzNzMzODM2Njc1LCA0NS45NTQzOTUwMjIwMDgxXSwgWy02Ni42MjM1Nzk5OTYxODI4LCA0NS45NTMwNTg0OTgwNDY3XSwgWy02Ni42MjM4MjI1NDEzMDk1LCA0NS45NTI1NzEzNDU3ODM5XSwgWy02Ni42MjM5OTMyMjEyMTM1LCA0NS45NTA0MDQwOTA4NzAzXSwgWy02Ni42MjM5MTIzNzI4MzgsIDQ1Ljk0OTM2NzI3NjEzMDhdLCBbLTY2LjYyMjgzNDM5NDQ5NywgNDUuOTQzOTI2ODAzODI1NF0sIFstNjYuNjIyNTExMDAwOTk0NywgNDUuOTQzNTU4MjU2NTQxXSwgWy02Ni42MjI1NDY5MzM2MDYxLCA0NS45NDMwNzEwMjA3Nzc0XSwgWy02Ni42MjIxNzg2MjQzMzk2LCA0NS45NDI3MDI0Njc4MDM5XSwgWy02Ni42MjIxNTE2NzQ4ODExLCA0NS45NDIyMTUyMjQ1MTkyXSwgWy02Ni42MjE1NzY3NTMwOTkyLCA0NS45NDIwMzQwNjg4NzI2XSwgWy02Ni42MjA4ODUwNTAzMzA1LCA0NS45NDExMzQ1Mjg2MTldLCBbLTY2LjYxNjgzMzY0ODM5OTEsIDQ1LjkzNzE2MTM4NDU4NjZdLCBbLTY2LjYxNDA0ODg3MTAxODMsIDQ1LjkzNTE0MzQ2ODE1MjFdLCBbLTY2LjYxMDIyMjA0NzkwOCwgNDUuOTMyOTI1NTQ5NTk2NF0sIFstNjYuNjA4NDM0NDAwNDkyNiwgNDUuOTMyMzE5NTExMzUwMl0sIFstNjYuNjA2NzAwNjUxOTk0MiwgNDUuOTMxMzY5ODI5ODUxMV0sIFstNjYuNjA1ODc0MjAxOTMyOCwgNDUuOTMxMTA3NDE0OTkwNF0sIFstNjYuNjAzNjI4NDEzNzIyNSwgNDUuOTMwMTEzOTc2MDU2N10sIFstNjYuNjAwMTk2ODQ5MzM3MiwgNDUuOTI4OTA4MDc5NzMyXSwgWy02Ni41OTczODUxMjI0OTc5LCA0NS45MjcyNzcyNjYzMTc4XSwgWy02Ni41OTY5MTc5OTg1NTAyLCA0NS45MjY4OTYxMTE0NDI2XSwgWy02Ni41OTU5NTY4MDExOTYyLCA0NS45MjU3Mjc2MzY3MzRdLCBbLTY2LjU5MjY2ODk2NzI1NjMsIDQ1LjkyODQwODIxODY0NzNdLCBbLTY2LjYwNTExMDYzMzk0MTMsIDQ1LjkzODY3OTQ1OTA3NDhdLCBbLTY2LjU4OTQzNTAzMjIzMzUsIDQ1Ljk1Njc4Njk0NDcwNzhdLCBbLTY2LjU5Mjk4MzM3NzYwNTcsIDQ1Ljk1OTQ3MjI3MDE0NV0sIFstNjYuNTk1NzQxMjA1NTI4LCA0NS45NjE5NDUxNTI0MTYyXSwgWy02Ni41OTY5OTg4NDY5MjU3LCA0NS45NjE3MTQxMDQ5NTkyXSwgWy02Ni42MDI2NzYxOTk1MjE0LCA0NS45NjEwMzM0NDYwMzk3XSwgWy02Ni42MDQ0OTA3OTYzOTUzLCA0NS45NjEwODM0MDI5NDJdLCBbLTY2LjYwNjg5ODI4MTM1NjcsIDQ1Ljk2MTUyMDUyMzkxNTZdLCBbLTY2LjYwNzg1OTQ3ODcxMDcsIDQ1Ljk2MTU2NDIzNTgyMzNdLCBbLTY2LjYwODc5MzcyNjYwNjIsIDQ1Ljk2MTQwMTg3NzEzNTJdLCBbLTY2LjYwOTg5ODY1NDQwNTcsIDQ1Ljk2MDg1ODU5NjUyN10sIFstNjYuNjEwNTgxMzc0MDIxNiwgNDUuOTYwMjA5MTUwNjQ4N10sIFstNjYuNjEwOTk0NTk5MDUyMywgNDUuOTU5NDUzNTM1NzY3Ml0sIFstNjYuNjExMDg0NDMwNTgwNywgNDUuOTU4NTIzMDUzNjk4XSwgWy02Ni42MTA3NzAwMjAyMzEzLCA0NS45NTc2MzAwMjYwMTExXSwgWy02Ni42MTAzMDI4OTYyODM1LCA0NS45NTcwMjQyNTc3NzkyXSwgWy02Ni42MDkzNjg2NDgzODgxLCA0NS45NTYyOTM1ODAwNjk4XSwgWy02Ni42MDk0MjI1NDczMDUxLCA0NS45NTU5Mzc2MDUzODc4XSwgWy02Ni42MDk3ODE4NzM0MTg4LCA0NS45NTU2ODc3OTcyMjhdLCBbLTY2LjYxMDE5NTA5ODQ0OTUsIDQ1Ljk1NTYzMTU5MDIzNjhdLCBbLTY2LjYxMDUyNzQ3NTEwNDYsIDQ1Ljk1NTcxMjc3ODA5NDZdLCBbLTY2LjYxMTgwMzA4MjgwOCwgNDUuOTU2NjU1Nzk3NTc0NF0sIFstNjYuNjEzMDMzNzc0NzQ3MywgNDUuOTU3MTg2NjI5Mjk1MV0sIFstNjYuNjE0NDYyMDk2MDQ5LCA0NS45NTc1NTUwODU5NzAyXSwgWy02Ni42MTU3MTk3Mzc0NDY4LCA0NS45NTc2NDI1MTYwMDhdLCBbLTY2LjYxNjk1OTQxMjUzODksIDQ1Ljk1NzQ5ODg4MDg3M10sIFstNjYuNjE4NjMwMjc4OTY3MywgNDUuOTU3MDQ5MjM4MDQzNF0sIFstNjYuNjIzNzc3NjI1NTQ1MywgNDUuOTU1NDMxNzQyNjk1NV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogMTAsICJOZWlnaGJvdXJoIjogIkJhcmtlcnMgUG9pbnQiLCAiT0JKRUNUSUQiOiAxMCwgIlNoYXBlX0FyZWEiOiA1Nzc5MDIxLjk2ODQsICJTaGFwZV9MZW5nIjogMTIzMTkuMjM5MDQ5NCwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmViMjRjIiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni42Mjg2NzM0NDM4NDM4LCA0NS45NjQ4MzAwNDIyMzczXSwgWy02Ni42Mjc3MzAyMTI3OTU1LCA0NS45NjM1Njg3MDE5NjY2XSwgWy02Ni42Mjc2MjI0MTQ5NjE0LCA0NS45NjMyMDY1Mjk2NTE0XSwgWy02Ni42MjcxMTAzNzUyNDk0LCA0NS45NjI2OTQ0ODg4OV0sIFstNjYuNjI2NzQyMDY1OTgyOSwgNDUuOTYxNzE0MTA0OTU5Ml0sIFstNjYuNjI2NzE1MTE2NTI0NCwgNDUuOTYwNzUyNDM3NjI1XSwgWy02Ni42MjU1MDIzOTA4OTA4LCA0NS45NTk2MDk2NTUzODg5XSwgWy02Ni42MjU0MTI1NTkzNjI0LCA0NS45NTg3NzkwOTM5NDY1XSwgWy02Ni42MjUxMDcxMzIxNjU4LCA0NS45NTc5OTIyMzQ3Nzk4XSwgWy02Ni42MjUzMTM3NDQ2ODEyLCA0NS45NTc3NTQ5MjU4NTM5XSwgWy02Ni42MjUyODY3OTUyMjI3LCA0NS45NTc1NzM4MjA5ODk5XSwgWy02Ni42MjQ4ODI1NTMzNDQ4LCA0NS45NTc1MDUxMjU4ODY2XSwgWy02Ni42MjQ3MDI4OTAyODgsIDQ1Ljk1NzI5Mjc5NTAyOV0sIFstNjYuNjI1MDA4MzE3NDg0NiwgNDUuOTU2NzMwNzM4ODMxNV0sIFstNjYuNjI1MDA4MzE3NDg0NiwgNDUuOTU2MzgxMDEyMDk4XSwgWy02Ni42MjQyOTg2NDg0MTAxLCA0NS45NTYxODc0MTI0MjE1XSwgWy02Ni42MjM3Nzc2MjU1NDUzLCA0NS45NTU0MzE3NDI2OTU1XSwgWy02Ni42MTg2MzAyNzg5NjczLCA0NS45NTcwNDkyMzgwNDM0XSwgWy02Ni42MTY5NTk0MTI1Mzg5LCA0NS45NTc0OTg4ODA4NzNdLCBbLTY2LjYxNTcxOTczNzQ0NjgsIDQ1Ljk1NzY0MjUxNjAwOF0sIFstNjYuNjE0MjY0NDY2Njg2NSwgNDUuOTU3NTE3NjE1OTExN10sIFstNjYuNjEyODA5MTk1OTI2MiwgNDUuOTU3MTExNjg4NjU0Nl0sIFstNjYuNjExNjIzNDE5NzUxMiwgNDUuOTU2NTQ5NjMwNjIwMV0sIFstNjYuNjEwNTk5MzQwMzI3MywgNDUuOTU1NzQ0MDA0MTYyMV0sIFstNjYuNjEwMjg0OTI5OTc3OSwgNDUuOTU1NjQ0MDgwNjg0Ml0sIFstNjYuNjA5ODYyNzIxNzk0MywgNDUuOTU1NjYyODE2MzUwMV0sIFstNjYuNjA5NDIyNTQ3MzA1MSwgNDUuOTU1OTM3NjA1Mzg3OF0sIFstNjYuNjA5MzY4NjQ4Mzg4MSwgNDUuOTU2MjkzNTgwMDY5OF0sIFstNjYuNjEwNjQ0MjU2MDkxNSwgNDUuOTU3NDE3Njk1NjMyXSwgWy02Ni42MTEwMzA1MzE2NjM3LCA0NS45NTgyNTQ1MjI0MTAzXSwgWy02Ni42MTEwODQ0MzA1ODA3LCA0NS45NTkwNTM4Njc1MzExXSwgWy02Ni42MTA4ODY4MDEyMTgyLCA0NS45NTk3MDk1NzE3MTZdLCBbLTY2LjYxMDQ5MTU0MjQ5MzIsIDQ1Ljk2MDMyNzc5OTk4MzJdLCBbLTY2LjYwOTg5ODY1NDQwNTcsIDQ1Ljk2MDg1ODU5NjUyN10sIFstNjYuNjA5Mjk2NzgzMTY1MywgNDUuOTYxMjAyMDUwNDA0NF0sIFstNjYuNjA4NDM0NDAwNDkyNiwgNDUuOTYxNTA4MDM0NzkyOF0sIFstNjYuNjA3NDczMjAzMTM4NiwgNDUuOTYxNTY0MjM1ODIzM10sIFstNjYuNjA0NDkwNzk2Mzk1MywgNDUuOTYxMDgzNDAyOTQyXSwgWy02Ni42MDIzNzA3NzIzMjQ4LCA0NS45NjEwNDU5MzUyNjk1XSwgWy02Ni41OTU3NDEyMDU1MjgsIDQ1Ljk2MTk0NTE1MjQxNjJdLCBbLTY2LjU5NzQ4MzkzNzE3OTIsIDQ1Ljk2MzczNzI5ODYxNl0sIFstNjYuNTk5MzE2NTAwMzU4OCwgNDUuOTYzNjEyNDEyMjU4M10sIFstNjYuNjAxMTQwMDgwMzg1NSwgNDUuOTYzODEyMjMwMjk1NV0sIFstNjYuNjAyODE5OTI5OTY2OCwgNDUuOTY0MzM2NzQ5MjE0M10sIFstNjYuNjA0MDc3NTcxMzY0NiwgNDUuOTY1MDExMTIzMzg0MV0sIFstNjYuNjA0NjE2NTYwNTM1MSwgNDUuOTY1NDEwNzQ4NjQ4XSwgWy02Ni42MDYxOTc1OTU0MzUxLCA0NS45Njg3NDUwMDk1NjgzXSwgWy02Ni42MTI3NTUyOTcwMDkyLCA0NS45NzIxOTE0NTAzNDgzXSwgWy02Ni42MTM0NTU5ODI5MzA4LCA0NS45NzMwMDkzMjQxOTI0XSwgWy02Ni42MTM1MzY4MzEzMDY0LCA0NS45NzM5NTgyOTI0NDY1XSwgWy02Ni42MTYwMTYxODE0OTA1LCA0NS45NzMzMDI3NTY5MDI0XSwgWy02Ni42MTgyMDgwNzA3ODM4LCA0NS45NzIyNjAxMjcyNDI1XSwgWy02Ni42MjI3ODk0Nzg3MzI4LCA0NS45Njg3NzYyMjgyOTE0XSwgWy02Ni42MjU4NjE3MTcwMDQ1LCA0NS45NjYxNTM3OTQyMDk1XSwgWy02Ni42MjY3OTU5NjQ5LCA0NS45NjU2MTA1NjAxOTg4XSwgWy02Ni42Mjg2NzM0NDM4NDM4LCA0NS45NjQ4MzAwNDIyMzczXV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiAxMSwgIk5laWdoYm91cmgiOiAiU291dGggRGV2b24iLCAiT0JKRUNUSUQiOiAxMSwgIlNoYXBlX0FyZWEiOiAyNTI1MjkzLjc1MTM1LCAiU2hhcGVfTGVuZyI6IDc4ODQuOTY2NzA3NDMsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZkOGQzYyIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjAxMDk1MTY0NjIxMywgNDUuOTgyNDY3MDY0MDEyNV0sIFstNjYuNjAxMjQ3ODc4MjE5NiwgNDUuOTg0MzIwOTY2MjAwNl0sIFstNjYuNjAxNjYxMTAzMjUwMywgNDUuOTg1ODM3NzQ5MDg3M10sIFstNjYuNjAyNjA0MzM0Mjk4NiwgNDUuOTg3ODg1MDI3OTgyOF0sIFstNjYuNjAzMzQ5OTM1OTg0NSwgNDUuOTg4Nzc3NTY3OTQ2Ml0sIFstNjYuNjA0NjQzNTA5OTkzNiwgNDUuOTg5NTM5MDI0MjMwNF0sIFstNjYuNjA2MDI2OTE1NTMxMSwgNDUuOTg5OTAxMDI0MzYzOV0sIFstNjYuNjA3ODIzNTQ2MDk5NCwgNDUuOTg5OTI1OTg5ODAzXSwgWy02Ni42MDkwOTkxNTM4MDI4LCA0NS45ODk1MjY1NDE0MjVdLCBbLTY2LjYwOTgxNzgwNjAzMDEsIDQ1Ljk4ODk4OTc3ODEyNzVdLCBbLTY2LjYxMDIyMjA0NzkwOCwgNDUuOTg4MzA5NDU0Mzc1NF0sIFstNjYuNjEwMTc3MTMyMTQzOCwgNDUuOTg1OTUwMTAxNzIyXSwgWy02Ni42MTAwMTU0MzUzOTI2LCA0NS45ODQ5NDUxNjE3MjExXSwgWy02Ni42MDk1OTMyMjcyMDkxLCA0NS45ODM3MDkyNDc3NjIyXSwgWy02Ni42MDkwOTAxNzA2NSwgNDUuOTgyNzYwNDQ2NjA4MV0sIFstNjYuNjA4NDE2NDM0MTg2OSwgNDUuOTgxODk5MDIwOTUwOV0sIFstNjYuNjA2ODk4MjgxMzU2NywgNDUuOTgwNzgxNjQ0NTE0Nl0sIFstNjYuNjA0Nzk2MjIzNTkxOSwgNDUuOTc5ODA3ODIzMTk2NV0sIFstNjYuNjAzNjEwNDQ3NDE2OSwgNDUuOTc5NDgzMjEyMjg0M10sIFstNjYuNjAxMzkxNjA4NjY1MSwgNDUuOTc5MzMzMzkxMjIxNF0sIFstNjYuNjAxMDk1MTY0NjIxMywgNDUuOTgyNDY3MDY0MDEyNV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogMTIsICJOZWlnaGJvdXJoIjogIkNvdHRvbiBNaWxsIENyZWVrIiwgIk9CSkVDVElEIjogMTIsICJTaGFwZV9BcmVhIjogNjM5ODc5LjA5NDAxOCwgIlNoYXBlX0xlbmciOiAzMTIwLjc4MzIwMjI3LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZmZmYjIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjY2Mzk3NzIzNDUwOTcsIDQ1Ljk4NDQ4OTQ5OTY4NDddLCBbLTY2LjY2NDU2MTEzOTQ0NDQsIDQ1Ljk4NDI2NDc4ODI1ODVdLCBbLTY2LjY2NTI0Mzg1OTA2MDMsIDQ1Ljk4NDczOTE3Nzk3NzRdLCBbLTY2LjY2NTU2NzI1MjU2MjYsIDQ1Ljk4NTI2MzQ5ODcyNjZdLCBbLTY2LjY2NTkzNTU2MTgyOTEsIDQ1Ljk4NTQzODI3MTIwNjFdLCBbLTY2LjY2NjUzNzQzMzA2OTQsIDQ1Ljk4NTQxOTU0NTYwOTddLCBbLTY2LjY2NzQ5ODYzMDQyMzQsIDQ1Ljk4NTA4MjQ4Mzc5MTFdLCBbLTY2LjY2ODA5MTUxODUxMDksIDQ1Ljk4NTIwNzMyMTc0MV0sIFstNjYuNjY5MDQzNzMyNzEyMSwgNDUuOTg2MzgwNzg0NzA5Ml0sIFstNjYuNjY5NTM3ODA2MTE4NCwgNDUuOTg2NjQyOTM3OTMwNF0sIFstNjYuNjcxNTE0MDk5NzQzNCwgNDUuOTg2MjU1OTQ5NDA1Nl0sIFstNjYuNjcyODcwNTU1ODIyNSwgNDUuOTg1ODMxNTA3MjY3Nl0sIFstNjYuNjczMzQ2NjYyOTIzMSwgNDUuOTg2MDY4Njk1OTIyNF0sIFstNjYuNjczNzU5ODg3OTUzOCwgNDUuOTg2NTg2NzYyMzQ0N10sIFstNjYuNjczNzE0OTcyMTg5NSwgNDUuOTg2Nzk4OTgwOTI1XSwgWy02Ni42NzMyMDI5MzI0Nzc2LCA0NS45ODcyMDQ2OTA2NTI1XSwgWy02Ni42NzMwNjgxODUxODUsIDQ1Ljk4NzUyMzAxNDY2NDRdLCBbLTY2LjY3MzcwNTk4OTAzNjcsIDQ1Ljk4Nzk0MTIwMjI1MV0sIFstNjYuNjczODQwNzM2MzI5MywgNDUuOTg4NjcxNDYyNTUwNV0sIFstNjYuNjczNzY4ODcxMTA2NiwgNDUuOTg5MjUxOTE4OTkyOF0sIFstNjYuNjczNTQ0MjkyMjg1NiwgNDUuOTg5ODE5ODg2NjA4OF0sIFstNjYuNjcyODE2NjU2OTA1NCwgNDUuOTkwNTMxMzk4MjU1NV0sIFstNjYuNjcxNTA1MTE2NTkwNiwgNDUuOTkxNDczODI1MDM5N10sIFstNjYuNjY5OTY4OTk3NDU0OCwgNDUuOTkyMjI5MDAzMTMyOV0sIFstNjYuNjY4MjYyMTk4NDE0OSwgNDUuOTkyNzc4MjE3MDkyMl0sIFstNjYuNjY2NDM4NjE4Mzg4MiwgNDUuOTkzMDk2NTA5MDUxM10sIFstNjYuNjY5Mzk0MDc1NjcyOSwgNDUuOTkyODU5MzUwNTEwNV0sIFstNjYuNjczMTEzMTAwOTQ5MiwgNDUuOTkyNzE1ODA2Njg5NV0sIFstNjYuNjc5OTY3MjQ2NTY3LCA0NS45OTI2NzIxMTkzNjU3XSwgWy02Ni42ODMwOTMzODM3NTU4LCA0NS45OTI4NTkzNTA1MTA1XSwgWy02Ni42ODYxNjU2MjIwMjc0LCA0NS45OTMyOTYyMjA3MTg0XSwgWy02Ni42ODg2NTM5NTUzNjQ0LCA0NS45OTM4NzAzODc3NDcxXSwgWy02Ni42OTA4MDA5Mjg4OTM1LCA0NS45OTQ3MTkxNDU0ODY2XSwgWy02Ni42OTI0MTc4OTY0MDQ5LCA0NS45OTU2NjE1MDA5NjE5XSwgWy02Ni42OTYwMTExNTc1NDE0LCA0NS45OTE1Mjk5OTU2NjU4XSwgWy02Ni43MDIxMTA3MTgzMjA2LCA0NS45OTE5ODU1OTk3NDg5XSwgWy02Ni42OTk2OTQyNTAyMDYzLCA0NS45ODgzMTU2OTU5MTU4XSwgWy02Ni42OTg2NzkxNTM5MzUyLCA0NS45ODY0MTgyMzUyNDU0XSwgWy02Ni42OTg0OTk0OTA4Nzg0LCA0NS45ODU2MjU1MjY4MjE5XSwgWy02Ni42OTgyMjEwMTMxNDAzLCA0NS45ODM2MjE4NTg4NjIxXSwgWy02Ni42OTgyMDMwNDY4MzQ2LCA0NS45ODEyMDYxMjUzN10sIFstNjYuNjk4NTYyMzcyOTQ4MywgNDUuOTc4NDg0Mzk3NTQxMV0sIFstNjYuNjk4OTkzNTY0Mjg0NywgNDUuOTc2NzE3Njk5ODQ2NF0sIFstNjYuNjk3OTg3NDUxMTY2NSwgNDUuOTc2NzgwMTI4Mjg3NV0sIFstNjYuNjk2Mjg5NjM1Mjc5NSwgNDUuOTc3MTU0Njk3NDU1OV0sIFstNjYuNjk1MzEwNDcxNjE5OCwgNDUuOTc3MjQyMDk2NTY0XSwgWy02Ni42OTQxMDY3MjkxMzkxLCA0NS45NzcxNzk2Njg2NDM3XSwgWy02Ni42OTAyODg4ODkxODE1LCA0NS45NzYzMTE5MTMyNjM5XSwgWy02Ni42ODQ5NTI4OTYzOTM5LCA0NS45NzQ2NzAwMDc5NjU5XSwgWy02Ni42ODAyMDA4MDg1NDA5LCA0NS45NzE5NjY2ODkwMDg0XSwgWy02Ni42Nzg0MjIxNDQyNzgzLCA0NS45NzE0MjM1MTIwMDQ0XSwgWy02Ni42NzYxMjI0NTcxNTEsIDQ1Ljk3MTM0MjM0NzE2N10sIFstNjYuNjczNTQ0MjkyMjg1NiwgNDUuOTcxNDM1OTk4ODkxOV0sIFstNjYuNjY1Mzg3NTg5NTA1OCwgNDUuOTcyMDg1MzEzMTYyNl0sIFstNjYuNjU0MTc2NjE0NzU5OSwgNDUuOTcyNTg0NzgwNDk4NV0sIFstNjYuNjUwNDEyNjczNzE5NSwgNDUuOTcyNTIyMzQ3MzI3OF0sIFstNjYuNjQ3ODUyNDc1MTU5NywgNDUuOTcyMjk3NTg3MzMwN10sIFstNjYuNjQ3NTAyMTMyMTk4OSwgNDUuOTcyMTQxNTAzNDYyN10sIFstNjYuNjQzNzkyMDkwMDc1NSwgNDUuOTcxNjI5NTQ1Mjg4MV0sIFstNjYuNjQxNDU2NDcwMzM2OCwgNDUuOTcxMDMwMTczNjA3XSwgWy02Ni42NDYyOTgzODk3MTgyLCA0NS45NzI1NDEwNzcyODY0XSwgWy02Ni42NTAzNDA4MDg0OTY4LCA0NS45NzQwMjA3MjM5OTg0XSwgWy02Ni42NTU3MTI3MzM4OTU4LCA0NS45NzY0MDU1NTY1ODUzXSwgWy02Ni42NTgxOTIwODQwOCwgNDUuOTc3NzIyNzg5MTkyNV0sIFstNjYuNjYwNDQ2ODU1NDQzMSwgNDUuOTc5MjMzNTEwMjg3Nl0sIFstNjYuNjYyMDcyODA2MTA3NCwgNDUuOTgwNjgxNzY2MTkzM10sIFstNjYuNjYzMzEyNDgxMTk5NCwgNDUuOTgyNTE3MDAxNTg1NF0sIFstNjYuNjYzOTc3MjM0NTA5NywgNDUuOTg0NDg5NDk5Njg0N11dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogMTMsICJOZWlnaGJvdXJoIjogIk5hc2h3YWFrc2lzIiwgIk9CSkVDVElEIjogMTMsICJTaGFwZV9BcmVhIjogNTkyODk2NC4xMTU5NSwgIlNoYXBlX0xlbmciOiAxNDAzMC40MTk0OTU1LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWIyNGMiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjY1MDAyNjM5ODE0NzMsIDQ1Ljk5MjMwMzg5NjI2NjRdLCBbLTY2LjY0ODEyMTk2OTc0NSwgNDUuOTkyMjk3NjU1MTc1OF0sIFstNjYuNjQ2NjEyODAwMDY3NywgNDUuOTkyNDIyNDc2ODU0XSwgWy02Ni42NDQ3NTMyODc0Mjk1LCA0NS45OTI3MjIwNDc3MzI5XSwgWy02Ni42NDMzMTU5ODI5NzQ5LCA0NS45OTMwNzc3ODYwNDU1XSwgWy02Ni42NDE2MDkxODM5MzUxLCA0NS45OTM2NjQ0MzcyMTU0XSwgWy02Ni42NDAwMTkxNjU4ODIyLCA0NS45OTQ0MDA4NjI4NTk3XSwgWy02Ni42Mzg0MjkxNDc4MjkzLCA0NS45OTU1OTkwOTM4MTA3XSwgWy02Ni42Mzc1NjY3NjUxNTY2LCA0NS45OTY2NzI0ODcwMDYzXSwgWy02Ni42MzcwOTA2NTgwNTYsIDQ1Ljk5NzYzOTc3MTE3ODFdLCBbLTY2LjYzNjg0ODExMjkyOTMsIDQ1Ljk5ODY1MDcyMTA4MDFdLCBbLTY2LjYzNjg1NzA5NjA4MjEsIDQ1Ljk5OTY3NDEzMzAzMTRdLCBbLTY2LjYzNzI3MDMyMTExMjgsIDQ2LjAwMDUyOTA0MTkxODhdLCBbLTY2LjYzNzkwODEyNDk2NDUsIDQ2LjAwMTMyMTUzNjg5OTRdLCBbLTY2LjYzODczNDU3NTAyNTksIDQ2LjAwMjAyNjY2MDY4NTJdLCBbLTY2LjYzOTc0MDY4ODE0NDEsIDQ2LjAwMjYwNjk3NzA1OTVdLCBbLTY2LjY0MDYzOTAwMzQyODMsIDQ2LjAwMjk3NTEzMTYwMzVdLCBbLTY2LjY1MDAyNjM5ODE0NzMsIDQ1Ljk5MjMwMzg5NjI2NjRdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDE0LCAiTmVpZ2hib3VyaCI6ICJXZXN0IEhpbGxzIiwgIk9CSkVDVElEIjogMTQsICJTaGFwZV9BcmVhIjogNTk3MzAzLjg5MDQ3MiwgIlNoYXBlX0xlbmciOiAzMzY0LjU0NzMzMDM1LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZmZmYjIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjYzMDk1NTE2NDY2NTUsIDQ2LjAwNzU5ODY5NDQ3OTJdLCBbLTY2LjYzMDY3NjY4NjkyNzQsIDQ2LjAxNDM5Mjk0NTkzODFdLCBbLTY2LjYzMDM2MjI3NjU3NzksIDQ2LjAxNjE0NTk2NDQyOThdLCBbLTY2LjYzMzc3NTg3NDY1NzYsIDQ2LjAxNjMzMzExNjE0NThdLCBbLTY2LjYzNTM4Mzg1OTAxNjIsIDQ2LjAxNjMwMTkyNDIzNzFdLCBbLTY2LjYzODE3NzYxOTU0OTgsIDQ2LjAxNTk1MjU3MzY1NzldLCBbLTY2LjYzOTQwODMxMTQ4OSwgNDYuMDE1NTg0NTA1NDgxNF0sIFstNjYuNjQwMDM3MTMyMTg3OSwgNDYuMDE1MTkxNDgwODI1N10sIFstNjYuNjQwNjY1OTUyODg2OCwgNDYuMDE0NTk4ODE5MzE3XSwgWy02Ni42NDEwNzAxOTQ3NjQ2LCA0Ni4wMTM5MTg4MTAzOTNdLCBbLTY2LjY0MTIzMTg5MTUxNTgsIDQ2LjAxMzE5NTEyMTk4NjldLCBbLTY2LjY0MDYzMDAyMDI3NTQsIDQ2LjAxMTk3ODU1NTQ4MTNdLCBbLTY2LjYzOTY5NTc3MjM3OTksIDQ2LjAxMDg2ODAyNTI1NjVdLCBbLTY2LjYzODY5ODY0MjQxNDYsIDQ2LjAxMDA1Njk0OTc2NjhdLCBbLTY2LjYzNzI2MTMzNzk2LCA0Ni4wMDkyNDU4NjIzODMyXSwgWy02Ni42MzMxNzQwMDM0MTcyLCA0Ni4wMDc5MTA2NjE4NjI2XSwgWy02Ni42MzA5NjQxNDc4MTgzLCA0Ni4wMDc0MjM5OTE5NzZdLCBbLTY2LjYzMDk1NTE2NDY2NTUsIDQ2LjAwNzU5ODY5NDQ3OTJdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDE1LCAiTmVpZ2hib3VyaCI6ICJOb3J0aGJyb29rIEhlaWdodHMiLCAiT0JKRUNUSUQiOiAxNSwgIlNoYXBlX0FyZWEiOiA2MTI3MDIuMjg2OTU3LCAiU2hhcGVfTGVuZyI6IDMwNzYuMDY3NTU5MTIsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlZDk3NiIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjQwMTg5ODQ1Nzg2MiwgNDYuMDExMzkyMDk4NDc4Ml0sIFstNjYuNjQzOTA4ODcxMDYyNSwgNDYuMDEyMzM0MTY5OTk3XSwgWy02Ni42NDcyNzc1NTMzNzc5LCA0Ni4wMTI3MTQ3MzczODQ1XSwgWy02Ni42NDgxMTI5ODY1OTIxLCA0Ni4wMTI2MDg2Nzc4ODRdLCBbLTY2LjY0OTAxMTMwMTg3NjIsIDQ2LjAxMjI3MTc4MTY1MDldLCBbLTY2LjY0OTU5NTIwNjgxMDksIDQ2LjAxMTg0NzUzOTAzMDddLCBbLTY2LjY1MDA0NDM2NDQ1MywgNDYuMDExMjA0OTMwMDQwNV0sIFstNjYuNjQ5Njg1MDM4MzM5NCwgNDYuMDEwMjQ0MTIyMDg5M10sIFstNjYuNjQ5MDkyMTUwMjUxOCwgNDYuMDA5MzM5NDQ5OTk2XSwgWy02Ni42NDgyODM2NjY0OTYxLCA0Ni4wMDg1MjIxMTI4MzAzXSwgWy02Ni42NDcyODY1MzY1MzA3LCA0Ni4wMDc4MTA4MzI0OTE0XSwgWy02Ni42NDYzNzAyNTQ5NDA5LCA0Ni4wMDczMzY2NDA1MTc1XSwgWy02Ni42NDQ4MzQxMzU4MDUxLCA0Ni4wMDY4MTI1Mjg4Njk1XSwgWy02Ni42NDIxMzAyMDY3OTk5LCA0Ni4wMDU1OTU4MjE5NzA5XSwgWy02Ni42MzkyNDY2MTQ3Mzc5LCA0Ni4wMDQ1OTEyMzg2NzAyXSwgWy02Ni42MzU3MTYyMzU2NzEzLCA0Ni4wMDg2OTA1NzI2MjM1XSwgWy02Ni42MzcyNjEzMzc5NiwgNDYuMDA5MjQ1ODYyMzgzMl0sIFstNjYuNjM4MjQwNTAxNjE5NywgNDYuMDA5NzU3NDcyNzMzM10sIFstNjYuNjM5MzA5NDk2ODA3OCwgNDYuMDEwNTE4NjQwMzQ5OV0sIFstNjYuNjQwMTg5ODQ1Nzg2MiwgNDYuMDExMzkyMDk4NDc4Ml1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogMTYsICJOZWlnaGJvdXJoIjogIkJyb29rc2lkZSBNaW5pIEhvbWUgUGFyayIsICJPQkpFQ1RJRCI6IDE2LCAiU2hhcGVfQXJlYSI6IDU3NTE4OC4wMzQzNzcsICJTaGFwZV9MZW5nIjogMzAyMi45NzU2NDMzLCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZmZmYjIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjY0ODY5Njg5MTUyNjgsIDQ2LjAwODg5NjQ2NzIyOTddLCBbLTY2LjY0OTk2MzUxNjA3NzQsIDQ2LjAwODkwMjcwNjQ0ODJdLCBbLTY2LjY1MTIxMjE3NDMyMjMsIDQ2LjAwODczNDI0NzMwMV0sIFstNjYuNjUyMzc5OTg0MTkxNywgNDYuMDA4MzkxMDg4MTkxOV0sIFstNjYuNjUzNjE5NjU5MjgzOCwgNDYuMDA3NzczMzk2NDMwN10sIFstNjYuNjU0MzgzMjI3Mjc1MywgNDYuMDA3MDQzMzg4MTgzNV0sIFstNjYuNjU1MDAzMDY0ODIxMywgNDYuMDA2MDQ1MDcwNzExM10sIFstNjYuNjU1MjkwNTI1NzEyMywgNDYuMDA0OTc4MDk4OTk1Nl0sIFstNjYuNjU1MjA5Njc3MzM2NywgNDYuMDAzODk4NjI3MTM2OF0sIFstNjYuNjU0OTQ5MTY1OTA0MywgNDYuMDAzMTkzNTI3MjA5Ml0sIFstNjYuNjU0NDE5MTU5ODg2NywgNDYuMDAyMzY5ODU5Mjc2NF0sIFstNjYuNjUzNTExODYxNDQ5NywgNDYuMDAxNDA4ODk3ODU2Ml0sIFstNjYuNjUyMjk5MTM1ODE2MSwgNDYuMDAwNDA0MjM4NTI1MV0sIFstNjYuNjQ5OTk5NDQ4Njg4OCwgNDUuOTk5MDQzODYzMjc2MV0sIFstNjYuNjQ1NzUwNDE3Mzk0OSwgNDUuOTk3MjAyOTM1MjU4OF0sIFstNjYuNjM5MjQ2NjE0NzM3OSwgNDYuMDA0NTkxMjM4NjcwMl0sIFstNjYuNjQxNjU0MDk5Njk5MywgNDYuMDA1NDE0ODczNTMwOF0sIFstNjYuNjQ0ODM0MTM1ODA1MSwgNDYuMDA2ODEyNTI4ODY5NV0sIFstNjYuNjQ2NTQ5OTE3OTk3OCwgNDYuMDA3NDIzOTkxOTc2XSwgWy02Ni42NDc4MTY1NDI1NDg0LCA0Ni4wMDgxNjAyMzQ1MDI1XSwgWy02Ni42NDg2OTY4OTE1MjY4LCA0Ni4wMDg4OTY0NjcyMjk3XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiAxNywgIk5laWdoYm91cmgiOiAiSGVyb24gU3ByaW5ncyIsICJPQkpFQ1RJRCI6IDE3LCAiU2hhcGVfQXJlYSI6IDk2NTEzMS4wMDAzMjEsICJTaGFwZV9MZW5nIjogMzgwMC45NDU5ODkyOCwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmVkOTc2IiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni42NjY0Mzg2MTgzODgyLCA0NS45OTMwOTY1MDkwNTEzXSwgWy02Ni42Njg0NTA4NDQ2MjQ2LCA0NS45OTQ0OTQ0NzU1ODcxXSwgWy02Ni42NzAyOTIzOTA5NTcsIDQ1Ljk5NTk5ODQ5ODM2MjNdLCBbLTY2LjY3MTk0NTI5MTA3OTgsIDQ1Ljk5NzYxNDgwOTIxODVdLCBbLTY2LjY3MzM5MTU3ODY4NzMsIDQ1Ljk5OTMxODQzNzEyMTRdLCBbLTY2LjY3NDczOTA1MTYxMzQsIDQ2LjAwMjc2Mjk3NTA0NjddLCBbLTY2LjY3NTY0NjM1MDA1MDQsIDQ2LjAwNTU0NTkwNTIxODldLCBbLTY2LjY3NjU2MjYzMTY0MDIsIDQ2LjAwOTA1MjQ0NzQ4MTddLCBbLTY2LjY3NzExOTU4NzExNjQsIDQ2LjAxMTg3ODczMzQ1MThdLCBbLTY2LjY3NzM1MzE0OTA5MDIsIDQ2LjAxMjQyNzc1MjM4NDNdLCBbLTY2LjY3ODEwNzczMzkyODksIDQ2LjAxMzc1MDM2NjUyMzRdLCBbLTY2LjY3OTA4Njg5NzU4ODYsIDQ2LjAxNDk5ODA4NjcxNTddLCBbLTY2LjY4MDI4MTY1NjkxNjUsIDQ2LjAxNjE1MjIwMjgzMDZdLCBbLTY2LjY4MTM3NzYwMTU2MzEsIDQ2LjAxNzAwMDYxODc3NDddLCBbLTY2LjY4MTAwMDMwOTE0MzgsIDQ2LjAwOTYxMzk3Mjc0NjhdLCBbLTY2LjY5MjQxNzg5NjQwNDksIDQ1Ljk5NTY2MTUwMDk2MTldLCBbLTY2LjY5MDgwMDkyODg5MzUsIDQ1Ljk5NDcxOTE0NTQ4NjZdLCBbLTY2LjY4ODY1Mzk1NTM2NDQsIDQ1Ljk5Mzg3MDM4Nzc0NzFdLCBbLTY2LjY4NjE2NTYyMjAyNzQsIDQ1Ljk5MzI5NjIyMDcxODRdLCBbLTY2LjY4MzA5MzM4Mzc1NTgsIDQ1Ljk5Mjg1OTM1MDUxMDVdLCBbLTY2LjY3OTk2NzI0NjU2NywgNDUuOTkyNjcyMTE5MzY1N10sIFstNjYuNjczMTEzMTAwOTQ5MiwgNDUuOTkyNzE1ODA2Njg5NV0sIFstNjYuNjY5Mzk0MDc1NjcyOSwgNDUuOTkyODU5MzUwNTEwNV0sIFstNjYuNjY2NDM4NjE4Mzg4MiwgNDUuOTkzMDk2NTA5MDUxM11dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogMTgsICJOZWlnaGJvdXJoIjogIlJveWFsIFJvYWQiLCAiT0JKRUNUSUQiOiAxOCwgIlNoYXBlX0FyZWEiOiAyMTk2ODI3LjQyNzU4LCAiU2hhcGVfTGVuZyI6IDc2NzQuODIyNjU1MzMsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZmZmZiMiIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjM3OTI2MDkxMjcwMiwgNDUuOTc2NzIzOTQyNjkzN10sIFstNjYuNjM4NTk5ODI3NzMzMywgNDUuOTc2OTczNjU2MDA3NV0sIFstNjYuNjM4MDUxODU1NDEsIDQ1Ljk3NjkxMTIyNzc4NDZdLCBbLTY2LjYzNzY0NzYxMzUzMjEsIDQ1Ljk3NzExNzI0MDY1MzFdLCBbLTY2LjYzNjIyODI3NTM4MzIsIDQ1Ljk3ODg5NjQxMDgwNTldLCBbLTY2LjYzNTQyODc3NDc4MDQsIDQ1Ljk4MDM2MzQwMjg0MTddLCBbLTY2LjYzNTA2OTQ0ODY2NjcsIDQ1Ljk4MTk5ODg5NzA3NjNdLCBbLTY2LjYzNTMyOTk2MDA5OTEsIDQ1Ljk4NjkwNTA4OTkxMDFdLCBbLTY2LjYzNTk1ODc4MDc5OCwgNDUuOTg4MTY1ODk4NzUzOV0sIFstNjYuNjM3MTg5NDcyNzM3MiwgNDUuOTg5NDI2Njc4ODhdLCBbLTY2LjYzODIwNDU2OTAwODMsIDQ1Ljk5MDA1MDgxNjgzXSwgWy02Ni42NDAxMDAwMTQyNTc4LCA0NS45OTA2NDk5ODI2NDA3XSwgWy02Ni42NDIxMTIyNDA0OTQyLCA0NS45OTEwMTgyMTY3NDM3XSwgWy02Ni42NDQxNzgzNjU2NDc3LCA0NS45OTExNDkyODI1MjgyXSwgWy02Ni42NDU5MDMxMzA5OTMyLCA0NS45OTEwODA2MjkwNjA4XSwgWy02Ni42NTAzMjI4NDIxOTExLCA0NS45OTA1NTYzNjM0MTAzXSwgWy02Ni42NTU1OTU5NTI5MDg5LCA0NS45ODk3MTM3ODMyMTExXSwgWy02Ni42NTU5NDYyOTU4Njk3LCA0NS45ODgzNTkzODY2NzgzXSwgWy02Ni42NTY1MjEyMTc2NTE1LCA0NS45ODcwNDg2NDg4MDE1XSwgWy02Ni42NTc3MTU5NzY5Nzk0LCA0NS45ODUzMDcxOTE4OTgyXSwgWy02Ni42NTg1NjkzNzY0OTkzLCA0NS45ODQzODMzODYwNjk0XSwgWy02Ni42NTg3NjcwMDU4NjE4LCA0NS45ODQzNzA5MDIxMDEyXSwgWy02Ni42NTg2NjgxOTExODA2LCA0NS45ODQxMDI0OTYxMDU3XSwgWy02Ni42NTY3OTk2OTUzODk2LCA0NS45ODI5OTE0MDYyODExXSwgWy02Ni42NTQzNTYyNzc4MTY4LCA0NS45ODE5NjE0NDM1NTA0XSwgWy02Ni42Mzc5MjYwOTEyNzAyLCA0NS45NzY3MjM5NDI2OTM3XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiAxOSwgIk5laWdoYm91cmgiOiAiRnVsdG9uIEhlaWdodHMiLCAiT0JKRUNUSUQiOiAxOSwgIlNoYXBlX0FyZWEiOiAyMDA4Njk5LjI0OTAxLCAiU2hhcGVfTGVuZyI6IDU1ODYuMDc4OTcxODcsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlYjI0YyIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjU5MDI3NTE3Mjk0MiwgNDUuOTg0NDE0NTk1OTc3M10sIFstNjYuNjYyMjM0NTAyODU4NSwgNDUuOTg1NjQ0MjUyMzQ4Nl0sIFstNjYuNjYzMDk2ODg1NTMxMiwgNDUuOTg1NzQ0MTIxNzE3Nl0sIFstNjYuNjY0MzM2NTYwNjIzMywgNDUuOTg1NjMxNzY4NjY0OF0sIFstNjYuNjY0MjI4NzYyNzg5MiwgNDUuOTg0ODc2NTAwNTU4NF0sIFstNjYuNjYzMDUxOTY5NzY3LCA0NS45ODIwNDI1OTI4MjQ1XSwgWy02Ni42NjE4ODQxNTk4OTc3LCA0NS45ODA0Njk1MjQxNjIzXSwgWy02Ni42NjA0NDY4NTU0NDMxLCA0NS45NzkyMzM1MTAyODc2XSwgWy02Ni42NTg5NzM2MTgzNzcxLCA0NS45NzgyMDM0Nzc2NDgzXSwgWy02Ni42NTY5NzkzNTg0NDY0LCA0NS45NzcwNDIzMjY5NzE0XSwgWy02Ni42NTIzMDgxMTg5NjksIDQ1Ljk3NDgzODU3MDgyODJdLCBbLTY2LjY0NzY2MzgyODk1MDEsIDQ1Ljk3MzAwOTMyNDE5MjRdLCBbLTY2LjY0MTQ1NjQ3MDMzNjgsIDQ1Ljk3MTAzMDE3MzYwN10sIFstNjYuNjQwMjE2Nzk1MjQ0NywgNDUuOTczNTA4NzgzMTk1Ml0sIFstNjYuNjM3OTI2MDkxMjcwMiwgNDUuOTc2NzIzOTQyNjkzN10sIFstNjYuNjU0NzE1NjAzOTMwNCwgNDUuOTgyMDg2Mjg4NTM4Ml0sIFstNjYuNjU3MTIzMDg4ODkxOSwgNDUuOTgzMTY2MTg1OTMzN10sIFstNjYuNjU4NjY4MTkxMTgwNiwgNDUuOTg0MTAyNDk2MTA1N10sIFstNjYuNjU4NzY3MDA1ODYxOCwgNDUuOTg0MzcwOTAyMTAxMl0sIFstNjYuNjU5MDI3NTE3Mjk0MiwgNDUuOTg0NDE0NTk1OTc3M11dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogMjAsICJOZWlnaGJvdXJoIjogIk1haW4gU3RyZWV0IiwgIk9CSkVDVElEIjogMjAsICJTaGFwZV9BcmVhIjogMTI5NDU4Mi4xNzQ0NCwgIlNoYXBlX0xlbmciOiA1NTQ1Ljg5MzE1Nzk4LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWIyNGMiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjcwNDU3MjEwMjE5OSwgNDUuOTc4MzQwODE2NDQwNl0sIFstNjYuNzAxMDk1NjIyMDQ5NSwgNDUuOTc4NTk2NzY1MDk5Ml0sIFstNjYuNzAxMjQ4MzM1NjQ3OCwgNDUuOTc5Njc2NzMwNTU3Ml0sIFstNjYuNzAxNjI1NjI4MDY3MSwgNDUuOTgwNTQ0NDMzMjA3M10sIFstNjYuNzAzMzk1MzA5MTc2OCwgNDUuOTgyNTU0NDU0NzM1NV0sIFstNjYuNzAzOTcwMjMwOTU4NywgNDUuOTgyNjg1NTQwNTYxMl0sIFstNjYuNzA0Njg4ODgzMTg2LCA0NS45ODI2MTY4NzY1OTZdLCBbLTY2LjcwNTI3Mjc4ODEyMDcsIDQ1Ljk4MjMyMzQ5MzIzOTZdLCBbLTY2LjcwNTYxNDE0NzkyODYsIDQ1Ljk4MTM2MjE4MzY4OThdLCBbLTY2LjcwNTM5ODU1MjI2MDQsIDQ1Ljk3OTk1MTQwMDQ5MjldLCBbLTY2LjcwNDU3MjEwMjE5OSwgNDUuOTc4MzQwODE2NDQwNl1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogMjEsICJOZWlnaGJvdXJoIjogIlJlZ2ltZW50IENyZWVrIiwgIk9CSkVDVElEIjogMjEsICJTaGFwZV9BcmVhIjogMTIzNjMyLjEyNjg5NCwgIlNoYXBlX0xlbmciOiAxMzc1LjAzMjY1MDMsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZmZmZiMiIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNzE2Njk5MzU4NTM0NywgNDUuOTc3NjQxNjMzNTg3XSwgWy02Ni43MDgxNjUzNjMzMzU1LCA0NS45NzgxMDM1OTQ2NzYyXSwgWy02Ni43MDc0NjQ2Nzc0MTM5LCA0NS45NzkyMTQ3ODI1OTI1XSwgWy02Ni43MDcwOTYzNjgxNDc0LCA0NS45ODA0MDcwOTk4ODA3XSwgWy02Ni43MDc2MzUzNTczMTc5LCA0NS45ODEyODcyNzU3NTEyXSwgWy02Ni43MDg2NTk0MzY3NDE4LCA0NS45ODIxNDg3MTA5MjY2XSwgWy02Ni43MDk4MDkyODAzMDU1LCA0NS45ODI2ODU1NDA1NjEyXSwgWy02Ni43MTA3MDc1OTU1ODk2LCA0NS45ODI2MzU2MDMxNDA0XSwgWy02Ni43MTE3MzE2NzUwMTM1LCA0NS45ODIzNjcxODg3MzE2XSwgWy02Ni43MTMwODgxMzEwOTI1LCA0NS45ODE1NDMyMTA3ODk4XSwgWy02Ni43MTQ3MDUwOTg2MDM5LCA0NS45ODAxOTQ4NTY3OTY5XSwgWy02Ni43MTYwNDM1ODgzNzczLCA0NS45Nzg3MDI4ODk4MDU3XSwgWy02Ni43MTY2OTkzNTg1MzQ3LCA0NS45Nzc2NDE2MzM1ODddXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDIyLCAiTmVpZ2hib3VyaCI6ICJHaWxyaWRnZSBFc3RhdGVzIiwgIk9CSkVDVElEIjogMjIsICJTaGFwZV9BcmVhIjogMjcxNzM5LjY3Mjc0NCwgIlNoYXBlX0xlbmciOiAyMDk1Ljc3NjAzNDgsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlZDk3NiIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNzU5NzQ2NjI2OTQ5NywgNDUuOTU4NDM1NjI1MDQ5NV0sIFstNjYuNzQ0ODc5NTA4OTk3NSwgNDUuOTU4NDY2ODQ5NTgyN10sIFstNjYuNzQ1MDMyMjIyNTk1OCwgNDUuOTU4ODQ3Nzg3NDcwNF0sIFstNjYuNzQ1ODEzNzU2ODkzLCA0NS45NTk1OTA5MjEwNTc2XSwgWy02Ni43NDU2MzQwOTM4MzYyLCA0NS45NTk4NTMyMDExMjA1XSwgWy02Ni43NDU2MDcxNDQzNzc2LCA0NS45NjAzMzQwNDQ2NzhdLCBbLTY2Ljc0NTA0MTIwNTc0ODYsIDQ1Ljk2MTAxNDcxMjE4OTddLCBbLTY2Ljc0NTE5MzkxOTM0NjksIDQ1Ljk2MTMyNjk0MjE5NTZdLCBbLTY2Ljc0NTA3NzEzODM2LCA0NS45NjE5MDc2ODUzMjY1XSwgWy02Ni43NDU1NTMyNDU0NjA2LCA0NS45NjIxMTk5OTg0OTk5XSwgWy02Ni43NDU2MDcxNDQzNzc2LCA0NS45NjIyODg1OTk1NTgxXSwgWy02Ni43NDQ3NDQ3NjE3MDQ5LCA0NS45NjM0NTAwNTk1NzIzXSwgWy02Ni43NDQ2NzI4OTY0ODIxLCA0NS45NjQ1NDkwNTMwNzkxXSwgWy02Ni43NDUzNzM1ODI0MDM4LCA0NS45NjUzMzU4MTkxMzA2XSwgWy02Ni43NDU4MjI3NDAwNDU4LCA0NS45NjU0NzMxODk4MzVdLCBbLTY2Ljc0NjE4MjA2NjE1OTUsIDQ1Ljk2NTgyMjg1OTE4Ml0sIFstNjYuNzQ2NDk2NDc2NTA4OSwgNDUuOTY3MzA4OTI5MjgyOF0sIFstNjYuNzQ3ODUyOTMyNTg3OSwgNDUuOTY3MTkwMjk0ODk4N10sIFstNjYuNzQ5NTQxNzY1MzIyMSwgNDUuOTY3NTA4NzMzOTg3XSwgWy02Ni43NDk2MTM2MzA1NDQ4LCA0NS45NjQ0ODAzNjY2MjM2XSwgWy02Ni43NTU1ODc0MjcxODQyLCA0NS45NjQ4MjM3OTgwNDkzXSwgWy02Ni43NTU1Nzg0NDQwMzE0LCA0NS45NjkwMTk3MzM3MjgxXSwgWy02Ni43NTU3MjIxNzQ0NzY4LCA0NS45NjkwNzU5MjcxMzg0XSwgWy02Ni43NjA4Nzg1MDQyMDc3LCA0NS45Njk3MzE1MTI3MTI4XSwgWy02Ni43NjI0MjM2MDY0OTYzLCA0NS45NzAxNjIzMjE4NjU0XSwgWy02Ni43NjMzMTI5Mzg2Mjc2LCA0NS45NzA1NjgxNTM1MDkxXSwgWy02Ni43NjU4MTkyMzgyNzAzLCA0NS45NzA5MzAyNzc2OTYyXSwgWy02Ni43NjcxNjY3MTExOTY1LCA0NS45NzA4ODY1NzMxNzg2XSwgWy02Ni43NjkzODU1NDk5NDgzLCA0NS45NzExNTUwNDMyNDIxXSwgWy02Ni43NzI5OTY3NzczOTA0LCA0NS45NzA5MTE1NDcxOTI5XSwgWy02Ni43NzQzMDgzMTc3MDUyLCA0NS45NzA5OTg5NTYxNTQyXSwgWy02Ni43NzY3Njk3MDE1ODM3LCA0NS45NzA3MzY3Mjg4NTYzXSwgWy02Ni43Nzg1NzUzMTUzMDQ4LCA0NS45NzA5Njc3Mzg2ODM5XSwgWy02Ni43Nzk0Mjg3MTQ4MjQ3LCA0NS45NzEzNzk4MDc4NzU5XSwgWy02Ni43ODE4OTAwOTg3MDMyLCA0NS45NzE1Mjk2NTA0NTg0XSwgWy02Ni43ODE5OTc4OTY1MzczLCA0NS45NzE2NzMyNDkyMTk1XSwgWy02Ni43ODI5MzIxNDQ0MzI4LCA0NS45NzE3MTA3MDk3MDQ2XSwgWy02Ni43ODM0NjIxNTA0NTA0LCA0NS45NzE1Mjk2NTA0NTg0XSwgWy02Ni43ODMxMjk3NzM3OTUzLCA0NS45NzA3NDkyMTU4OTg2XSwgWy02Ni43ODI0MDIxMzg0MTUyLCA0NS45Njk4MjUxNjcxNjE1XSwgWy02Ni43ODE4NTQxNjYwOTE5LCA0NS45Njk2OTQwNTA4ODkxXSwgWy02Ni43ODE2NDc1NTM1NzY1LCA0NS45NjkyNjMyMzgwOTQzXSwgWy02Ni43ODExODk0MTI3ODE2LCA0NS45Njg4NTczOTY4ODkzXSwgWy02Ni43ODA1NDI2MjU3NzcsIDQ1Ljk2ODYyMDEzNDQ5OTddLCBbLTY2Ljc4MDA2NjUxODY3NjQsIDQ1Ljk2ODY3MDA4NDU2MDldLCBbLTY2Ljc3OTk1ODcyMDg0MjQsIDQ1Ljk2ODU3MDE4NDM5MzVdLCBbLTY2Ljc3OTk1ODcyMDg0MjQsIDQ1Ljk2ODM5NTM1ODY2NjldLCBbLTY2Ljc4MDI0NjE4MTczMzMsIDQ1Ljk2ODA4MzE2ODQ5NjldLCBbLTY2Ljc3OTk4NTY3MDMwMDksIDQ1Ljk2NzIyNzc1ODQxNTldLCBbLTY2Ljc4MDAzMDU4NjA2NTEsIDQ1Ljk2NjMyMjM4Mjk5MTddLCBbLTY2Ljc3OTg5NTgzODc3MjUsIDQ1Ljk2NjEyODgxODA1XSwgWy02Ni43Nzk1NTQ0Nzg5NjQ1LCA0NS45NjYwNzI2MjE2NDk5XSwgWy02Ni43NzkzMjk5MDAxNDM1LCA0NS45NjU1NzMwOTU1ODhdLCBbLTY2Ljc3OTAwNjUwNjY0MTIsIDQ1Ljk2NTM0MjA2MzI2MDldLCBbLTY2Ljc3OTMyMDkxNjk5MDYsIDQ1Ljk2NDY0ODk2MDQ5ODZdLCBbLTY2Ljc3OTA5NjMzODE2OTYsIDQ1Ljk2NDE4MDY0MjkxMjNdLCBbLTY2Ljc3Nzk3MzQ0NDA2NDUsIDQ1Ljk2MzQyNTA4MjE5MzhdLCBbLTY2Ljc3ODMwNTgyMDcxOTYsIDQ1Ljk2MzAxOTE5ODIxNDVdLCBbLTY2Ljc3NzU0MjI1MjcyODEsIDQ1Ljk2MjcwMDczMzMxOF0sIFstNjYuNzc3NTUxMjM1ODgwOSwgNDUuOTYyMjMyMzk5MjYyNF0sIFstNjYuNzc4NDA0NjM1NDAwOCwgNDUuOTYxNTE0Mjc5MzU0NV0sIFstNjYuNzc4OTI1NjU4MjY1NiwgNDUuOTYwNzk2MTUwMTM4N10sIFstNjYuNzc5MDA2NTA2NjQxMiwgNDUuOTYwMTY1NDM3NjcxOV0sIFstNjYuNzgwMTM4MzgzODk5MiwgNDUuOTU4OTk3NjYzOTU0Ml0sIFstNjYuNzgxMDU0NjY1NDg5LCA0NS45NTg4MzUyOTc3NDUxXSwgWy02Ni43ODE0ODU4NTY4MjU0LCA0NS45NTgzNzk0MjA4NDU1XSwgWy02Ni43NzA2MjUyMjUwNDA0LCA0NS45NTg0MTA2NDU0MTAzXSwgWy02Ni43NzE1NDE1MDY2MzAyLCA0NS45NjYwNzg4NjU2OTcyXSwgWy02Ni43Njc3NDE2MzI5NzgzLCA0NS45NjU0NDE5NjkyNTAzXSwgWy02Ni43NTk4NTQ0MjQ3ODM4LCA0NS45NjUxMDQ3ODU4MTRdLCBbLTY2Ljc2MDAxNjEyMTUzNDksIDQ1Ljk2MzIyNTI2Mjc2MDJdLCBbLTY2Ljc1OTc0NjYyNjk0OTcsIDQ1Ljk1ODQzNTYyNTA0OTVdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDIzLCAiTmVpZ2hib3VyaCI6ICJTaWx2ZXJ3b29kIiwgIk9CSkVDVElEIjogMjMsICJTaGFwZV9BcmVhIjogMjUwNDk0MC4wODY2NiwgIlNoYXBlX0xlbmciOiAxMTMxMi43ODg2MDk5LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjcxMzUxMDMzOTI3NiwgNDUuOTU4NTI5Mjk4NTk2Ml0sIFstNjYuNzEyMDM3MTAyMjEwMSwgNDUuOTU4ODYwMjc3MTkyOF0sIFstNjYuNzEwNjcxNjYyOTc4MiwgNDUuOTU5MzU5ODYzNzgzXSwgWy02Ni43MDk2ODM1MTYxNjU3LCA0NS45NTk4NjU2OTA2MTYzXSwgWy02Ni43MDg2MTQ1MjA5Nzc2LCA0NS45NjA2Mjc1NDQ1Mzg4XSwgWy02Ni43MDc3NDMxNTUxNTIsIDQ1Ljk2MTQ5NTU0NTY2NzFdLCBbLTY2LjcwNzExNDMzNDQ1MzEsIDQ1Ljk2MjQxOTczMzM1OTddLCBbLTY2LjcwNjk3MDYwNDAwNzcsIDQ1Ljk2MzE5NDA0MDkwODZdLCBbLTY2LjcwNzE3NzIxNjUyMywgNDUuOTYzOTU1ODQ5MDY0Nl0sIFstNjYuNzA4MjkxMTI3NDc1MywgNDUuOTY0MTYxOTEwMTI2NV0sIFstNjYuNzA5NDMxOTg3ODg2MSwgNDUuOTY0MTE4MjAwMjY4M10sIFstNjYuNzA5ODA5MjgwMzA1NSwgNDUuOTY0MDQ5NTEzMjc4N10sIFstNjYuNzEyMTQ0OTAwMDQ0MiwgNDUuOTYzMDMxNjg2OTk2Nl0sIFstNjYuNzE2ODM0MTA1ODI3MywgNDUuOTYyMzM4NTU1MzI4Nl0sIFstNjYuNzE5ODk3MzYwOTQ2MSwgNDUuOTYyMDM4ODIwMDI5N10sIFstNjYuNzIxOTA5NTg3MTgyNiwgNDUuOTYxNjY0MTQ4NjI1Nl0sIFstNjYuNzI0MDI5NjExMjUzMSwgNDUuOTYxNTY0MjM1ODIzM10sIFstNjYuNzI3MTkxNjgxMDUzMiwgNDUuOTYxNzk1MjgzOTA1Ml0sIFstNjYuNzI5Nzk2Nzk1Mzc3MSwgNDUuOTYyNzk0Mzk5NjU0XSwgWy02Ni43MzA3MjIwNjAxMTk4LCA0NS45NjI5NzU0ODc0NTQ3XSwgWy02Ni43MzE2MjAzNzU0MDM5LCA0NS45NjI5NjkyNDMwNTc2XSwgWy02Ni43MzI0NjQ3OTE3NzEsIDQ1Ljk2MzM2MjYzODY5ODJdLCBbLTY2LjczMzYxNDYzNTMzNDYsIDQ1Ljk2MzY0MzYzMzg3NDFdLCBbLTY2LjczNTk4NjE4NzY4NDcsIDQ1Ljk2NDQ5Mjg1NTA3NjRdLCBbLTY2LjczNzU5NDE3MjA0MzMsIDQ1Ljk2NDgyMzc5ODA0OTNdLCBbLTY2LjczODkwNTcxMjM1ODEsIDQ1Ljk2NDk3MzY1ODM2NzhdLCBbLTY2Ljc0MDMzNDAzMzY1OTgsIDQ1Ljk2NTMxMDg0MjYwMjNdLCBbLTY2Ljc0MTgxNjI1Mzg3ODYsIDQ1Ljk2NTQ5ODE2NjI5MDJdLCBbLTY2Ljc0MzMxNjQ0MDQwMzEsIDQ1Ljk2NTUxMDY1NDUxMzVdLCBbLTY2Ljc0NTIxMTg4NTY1MjYsIDQ1Ljk2NTEzNjAwNjU4ODddLCBbLTY2Ljc0NDY3Mjg5NjQ4MjEsIDQ1Ljk2NDU0OTA1MzA3OTFdLCBbLTY2Ljc0NDczNTc3ODU1MiwgNDUuOTYzNTYyNDU3NjM2NF0sIFstNjYuNzQ0ODUyNTU5NTM5LCA0NS45NjMyMzE1MDcxMjg0XSwgWy02Ni43NDUzNDY2MzI5NDUyLCA0NS45NjI3Njk0MjE5Nzk5XSwgWy02Ni43NDU2MDcxNDQzNzc2LCA0NS45NjIyODg1OTk1NTgxXSwgWy02Ni43NDU1NTMyNDU0NjA2LCA0NS45NjIxMTk5OTg0OTk5XSwgWy02Ni43NDUwNzcxMzgzNiwgNDUuOTYxOTA3Njg1MzI2NV0sIFstNjYuNzQ1MTkzOTE5MzQ2OSwgNDUuOTYxMzI2OTQyMTk1Nl0sIFstNjYuNzQ1MDQxMjA1NzQ4NiwgNDUuOTYxMDE0NzEyMTg5N10sIFstNjYuNzQ1NjA3MTQ0Mzc3NiwgNDUuOTYwMzM0MDQ0Njc4XSwgWy02Ni43NDU2MzQwOTM4MzYyLCA0NS45NTk4NTMyMDExMjA1XSwgWy02Ni43NDU4MTM3NTY4OTMsIDQ1Ljk1OTU5MDkyMTA1NzZdLCBbLTY2Ljc0NTAzMjIyMjU5NTgsIDQ1Ljk1ODg0Nzc4NzQ3MDRdLCBbLTY2Ljc0NDg3OTUwODk5NzUsIDQ1Ljk1ODQ2Njg0OTU4MjddLCBbLTY2LjcxMzUxMDMzOTI3NiwgNDUuOTU4NTI5Mjk4NTk2Ml1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogMjQsICJOZWlnaGJvdXJoIjogIlNwcmluZ2hpbGwiLCAiT0JKRUNUSUQiOiAyNCwgIlNoYXBlX0FyZWEiOiAxNTEwMjM0LjU2MjM0LCAiU2hhcGVfTGVuZyI6IDcyMzEuMzExNjkzNjQsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZmZmZiMiIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNzI3MTkxNjgxMDUzMiwgNDUuOTYxNzk1MjgzOTA1Ml0sIFstNjYuNzI2MTY3NjAxNjI5MywgNDUuOTY1MDc5ODA5MTgxNV0sIFstNjYuNzI2MTk0NTUxMDg3OCwgNDUuOTY1NDkxOTIyMTc3NF0sIFstNjYuNzI2NDU1MDYyNTIwMiwgNDUuOTY1ODcyODExNzY1Nl0sIFstNjYuNzI3MDEyMDE3OTk2NCwgNDUuOTY2MTg1MDE0MzkzMV0sIFstNjYuNzI3OTgyMTk4NTAzMiwgNDUuOTY2MTM1MDYyMDkwOV0sIFstNjYuNzMwMTc0MDg3Nzk2NSwgNDUuOTY1OTQxNDk2NDk0Nl0sIFstNjYuNzMxNTAzNTk0NDE2OSwgNDUuOTY1NDk4MTY2MjkwMl0sIFstNjYuNzMyMjQ5MTk2MTAyOCwgNDUuOTY0OTIzNzA0OTczM10sIFstNjYuNzMyNDkxNzQxMjI5NSwgNDUuOTY0NDQ5MTQ1NDc5M10sIFstNjYuNzMyNDY0NzkxNzcxLCA0NS45NjM4MzcyMDc0OTk1XSwgWy02Ni43MzE5OTc2Njc4MjMyLCA0NS45NjMyMTI3NzQwMjE3XSwgWy02Ni43MzE2MjAzNzU0MDM5LCA0NS45NjI5NjkyNDMwNTc2XSwgWy02Ni43MzA3MjIwNjAxMTk4LCA0NS45NjI5NzU0ODc0NTQ3XSwgWy02Ni43Mjk3OTY3OTUzNzcxLCA0NS45NjI3OTQzOTk2NTRdLCBbLTY2LjcyNzE5MTY4MTA1MzIsIDQ1Ljk2MTc5NTI4MzkwNTJdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDI1LCAiTmVpZ2hib3VyaCI6ICJOZXRoZXJ2dWUgTWluaWhvbWUgUGFyayIsICJPQkpFQ1RJRCI6IDI1LCAiU2hhcGVfQXJlYSI6IDE2NTUyMi4yNzYwNDksICJTaGFwZV9MZW5nIjogMTU5MC40NzIwMjExNywgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmVkOTc2IiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni43MzE4NjI5MjA1MzA2LCA0NS45NjUyNzMzNzc3ODg3XSwgWy02Ni43MzEwMDA1Mzc4NTc4LCA0NS45NjU3MjI5NTM4Nzk1XSwgWy02Ni43Mjk5NzY0NTg0MzQsIDQ1Ljk2NTk2NjQ3MjczODZdLCBbLTY2LjcyNzAxMjAxNzk5NjQsIDQ1Ljk2NjE4NTAxNDM5MzFdLCBbLTY2LjcyNjUyNjkyNzc0MjksIDQ1Ljk2NTkzNTI1MjQzMTldLCBbLTY2LjcyNjIzMDQ4MzY5OTIsIDQ1Ljk2NTU3MzA5NTU4OF0sIFstNjYuNzI2MTU4NjE4NDc2NCwgNDUuOTY1MTYwOTgzMTk1OV0sIFstNjYuNzI3MTkxNjgxMDUzMiwgNDUuOTYxNzk1MjgzOTA1Ml0sIFstNjYuNzI0NjQwNDY1NjQ2MywgNDUuOTYxNTg5MjE0MDQwN10sIFstNjYuNzIzMTIyMzEyODE2MSwgNDUuOTYxNTcwNDgwMzc4N10sIFstNjYuNzIxNjEzMTQzMTM4OCwgNDUuOTYxNzAxNjE1ODhdLCBbLTY2LjcxOTU0NzAxNzk4NTMsIDQ1Ljk2MjA4MjUzMTUyODRdLCBbLTY2LjcxNzY0MjU4OTU4MywgNDUuOTYyMjMyMzk5MjYyNF0sIFstNjYuNzE3Njk2NDg4NSwgNDUuOTYyNjA3MDY2ODIzNl0sIFstNjYuNzE3MjY1Mjk3MTYzNywgNDUuOTY0MjkzMDM5NDk0MV0sIFstNjYuNzE2MzIyMDY2MTE1MywgNDUuOTY2ODcxODUzOTc5OF0sIFstNjYuNzE1NzU2MTI3NDg2MywgNDUuOTY4MDAxOTk4NzY0NV0sIFstNjYuNzIwNzk1Njc2MjMwMywgNDUuOTY3NzY0NzMyNzEwOV0sIFstNjYuNzI1MDE3NzU4MDY1NiwgNDUuOTY3OTM5NTYwNDI3OV0sIFstNjYuNzI4MTUyODc4NDA3MiwgNDUuOTY4MjE0Mjg4NTgyNl0sIFstNjYuNzMxMzY4ODQ3MTI0MywgNDUuOTY3ODk1ODUzNTUwNF0sIFstNjYuNzMxODYyOTIwNTMwNiwgNDUuOTY1MjczMzc3Nzg4N11dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogMjYsICJOZWlnaGJvdXJoIjogIk1vbnRlaXRoIC8gVGFsaXNtYW4iLCAiT0JKRUNUSUQiOiAyNiwgIlNoYXBlX0FyZWEiOiA1OTM1NDcuNTEzOTQsICJTaGFwZV9MZW5nIjogMzg1MS4zMjAzMTQzMiwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmVkOTc2IiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni43MTc2NDI1ODk1ODMsIDQ1Ljk2MjIzMjM5OTI2MjRdLCBbLTY2LjcxMjE0NDkwMDA0NDIsIDQ1Ljk2MzAzMTY4Njk5NjZdLCBbLTY2LjcwOTgwOTI4MDMwNTUsIDQ1Ljk2NDA0OTUxMzI3ODddLCBbLTY2LjcwOTA1NDY5NTQ2NjgsIDQ1Ljk2NDE2MTkxMDEyNjVdLCBbLTY2LjcwNzkxMzgzNTA1NiwgNDUuOTY0MTE4MjAwMjY4M10sIFstNjYuNzA1NTY5MjMyMTY0NCwgNDUuOTYzNTA2MjU4NjMyOV0sIFstNjYuNzAzNzQ1NjUyMTM3NywgNDUuOTYzMzE4OTI4MjA5NV0sIFstNjYuNzAyOTgyMDg0MTQ2MiwgNDUuOTYzNzE4NTY1NjgwM10sIFstNjYuNzAxOTY2OTg3ODc1MSwgNDUuOTY1MDExMTIzMzg0MV0sIFstNjYuNzAxNDQ1OTY1MDEwMywgNDUuOTY2MjQ3NDU0NzA3NF0sIFstNjYuNzAxMjg0MjY4MjU5MiwgNDUuOTY3MzIxNDE3MDk3OV0sIFstNjYuNzAyMzYyMjQ2NjAwMSwgNDUuOTY3MjY1MjIxOTA3N10sIFstNjYuNzAyNTc3ODQyMjY4MywgNDUuOTY3MzkwMTAwMDMwOF0sIFstNjYuNzAzMjA2NjYyOTY3MiwgNDUuOTY3MzU4ODgwNTI2NF0sIFstNjYuNzAzNzI3Njg1ODMyLCA0NS45Njc0OTAwMDIzMjY2XSwgWy02Ni43MDY2MjAyNjEwNDY4LCA0NS45Njc1NDYxOTcyODg4XSwgWy02Ni43MDc2NzEyODk5MjkzLCA0NS45Njc3NTg0ODg4NTM3XSwgWy02Ni43MDkwMDk3Nzk3MDI2LCA0NS45Njc4MzM0MTUwOTQxXSwgWy02Ni43MTAwNjk3OTE3Mzc5LCA0NS45Njc4NzcxMjIwMjA5XSwgWy02Ni43MTExODM3MDI2OTAyLCA0NS45Njc3ODM0NjQyNzg0XSwgWy02Ni43MTQ2OTYxMTU0NTExLCA0NS45NjgwMjA3MzAyNTE4XSwgWy02Ni43MTU3NTYxMjc0ODYzLCA0NS45NjgwMDE5OTg3NjQ1XSwgWy02Ni43MTYzMjIwNjYxMTUzLCA0NS45NjY4NzE4NTM5Nzk4XSwgWy02Ni43MTcyNjUyOTcxNjM3LCA0NS45NjQyOTMwMzk0OTQxXSwgWy02Ni43MTc2OTY0ODg1LCA0NS45NjI2MDcwNjY4MjM2XSwgWy02Ni43MTc2NDI1ODk1ODMsIDQ1Ljk2MjIzMjM5OTI2MjRdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDI3LCAiTmVpZ2hib3VyaCI6ICJHYXJkZW4gQ3JlZWsiLCAiT0JKRUNUSUQiOiAyNywgIlNoYXBlX0FyZWEiOiA1NjU2NTUuNTQxNDg0LCAiU2hhcGVfTGVuZyI6IDM0NDIuNDY5NjcxNjUsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlZDk3NiIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjk4ODQ5ODMzODM5MiwgNDUuOTU2MjY4NTk5NDY1XSwgWy02Ni43MDA0NzU3ODQ1MDM1LCA0NS45NTY3NjE5NjQzMjU0XSwgWy02Ni43MDE4NDEyMjM3MzUzLCA0NS45NTc1NDI1OTU5NTM1XSwgWy02Ni43MDE4MTQyNzQyNzY4LCA0NS45NTg4NDc3ODc0NzA0XSwgWy02Ni43MDExNjc0ODcyNzIyLCA0NS45NjAzMzQwNDQ2NzhdLCBbLTY2LjcwMTE2NzQ4NzI3MjIsIDQ1Ljk2MDgyMTEyODcwMjRdLCBbLTY2LjcwMTY1MjU3NzUyNTcsIDQ1Ljk2MTM3Njg5ODgzMzJdLCBbLTY2LjcwMjg5MjI1MjYxNzcsIDQ1Ljk2MTE2NDU4MjgxMjFdLCBbLTY2LjcwMzUzMDA1NjQ2OTUsIDQ1Ljk2MDc3MTE3MTU2MzddLCBbLTY2LjcwNzA1MTQ1MjM4MzIsIDQ1Ljk1NzMyNDAyMDIwNjJdLCBbLTY2LjcwODQzNDg1NzkyMDgsIDQ1Ljk1NTQ4Nzk0OTg4OTNdLCBbLTY2LjcwOTAwMDc5NjU0OTgsIDQ1Ljk1NDI1MTM3ODQ1NTRdLCBbLTY2LjcwOTMyNDE5MDA1MiwgNDUuOTUyOTc3MzA2MzAwMl0sIFstNjYuNzA5Mzk2MDU1Mjc0OCwgNDUuOTUxNjc4MjIyMTgwNl0sIFstNjYuNzA5MTYyNDkzMzAwOSwgNDUuOTUwMTM1NTIwMjM4OF0sIFstNjYuNzA4NjQxNDcwNDM2MSwgNDUuOTUwMDY2ODE1OTE0OF0sIFstNjYuNzA1MzUzNjM2NDk2MiwgNDUuOTUwMzg1MzUzNDI2N10sIFstNjYuNzAxMTY3NDg3MjcyMiwgNDUuOTUwNTk3NzEwNzUwOV0sIFstNjYuNzAwMTM0NDI0Njk1NSwgNDUuOTUwODAzODIxNDkzNF0sIFstNjYuNjk5MTczMjI3MzQxNSwgNDUuOTUxMTUzNTgzNDIzN10sIFstNjYuNjk4NDkwNTA3NzI1NiwgNDUuOTUyNDMzOTQzMDg5NF0sIFstNjYuNjk3Mjc3NzgyMDkyLCA0NS45NTU4NTY0MTc4NTk0XSwgWy02Ni42OTgwNTkzMTYzODkyLCA0NS45NTYyMDYxNDc5MDM2XSwgWy02Ni42OTg4NDk4MzM4MzkyLCA0NS45NTYyNjg1OTk0NjVdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDI4LCAiTmVpZ2hib3VyaCI6ICJIaWdocG9pbnQgUmlkZ2UiLCAiT0JKRUNUSUQiOiAyOCwgIlNoYXBlX0FyZWEiOiA3MjQyNDcuODk3MjcsICJTaGFwZV9MZW5nIjogMzY2OC43MTMxMzE2MSwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmVkOTc2IiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni43MTEwOTM4NzExNjE4LCA0NS45MzQyMDYzMzAyODgyXSwgWy02Ni43MDg3MTMzMzU2NTg4LCA0NS45MzUwNDM1MDc1MzQ1XSwgWy02Ni43MDc1OTA0NDE1NTM3LCA0NS45MzU1NzQ1NDYyNTE3XSwgWy02Ni43MDY3NjM5OTE0OTIzLCA0NS45MzYxMjQzMjIxNTQyXSwgWy02Ni43MDU2OTQ5OTYzMDQyLCA0NS45Mzc0MDUwMjg5NzFdLCBbLTY2LjcwNTE5MTkzOTc0NTEsIDQ1LjkzODg1NDM3ODU2NzZdLCBbLTY2LjcwOTEwODU5NDM4MzgsIDQ1LjkzOTgzNTE2NjkzMTNdLCBbLTY2LjcxMTA5Mzg3MTE2MTgsIDQ1LjkzNDIwNjMzMDI4ODJdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDI5LCAiTmVpZ2hib3VyaCI6ICJHcmVlbndvb2QgTWluaWhvbWUgUGFyayIsICJPQkpFQ1RJRCI6IDI5LCAiU2hhcGVfQXJlYSI6IDE1MjUzOS40ODc5NjUsICJTaGFwZV9MZW5nIjogMTY5OS42NDcxNjEyMiwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmZmZmIyIiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni43MDM4NzE0MTYyNzc0LCA0NS45NjMyODc3MDY0MTA2XSwgWy02Ni43MDI5ODIwODQxNDYyLCA0NS45NjI2MzIwNDQ1NzA5XSwgWy02Ni43MDE3MTU0NTk1OTU1LCA0NS45NjE5MjY0MTg4NzQ1XSwgWy02Ni43MDAzMTQwODc3NTIzLCA0NS45NjEzNTgxNjUwOTk0XSwgWy02Ni42OTkwOTIzNzg5NjU5LCA0NS45NjEwMDg0Njc1NzE3XSwgWy02Ni42OTcwMjYyNTM4MTI0LCA0NS45NjA2NDYyNzg1MTk3XSwgWy02Ni42OTQ4OTcyNDY1ODkxLCA0NS45NjA1MDI2NTExNzFdLCBbLTY2LjY4ODg3ODUzNDE4NTUsIDQ1Ljk1OTc3MjAxOTMyODldLCBbLTY2LjY4NzY4Mzc3NDg1NzYsIDQ1Ljk2MDAxNTU2NDM0NjhdLCBbLTY2LjY4NjY4NjY0NDg5MjIsIDQ1Ljk2MDUzMzg3NDUzOTRdLCBbLTY2LjY4NTQxMTAzNzE4ODgsIDQ1Ljk2MDU1ODg1MzIyMTRdLCBbLTY2LjY4NDY4MzQwMTgwODYsIDQ1Ljk2MDIxNTM5NTM1NjhdLCBbLTY2LjY4MzgyMTAxOTEzNTksIDQ1Ljk2MDEwMjk5MDUwMjRdLCBbLTY2LjY3ODAyNjg4NTU1MzMsIDQ1Ljk2MDUxNTE0MDUyMDVdLCBbLTY2LjY3Njk0ODkwNzIxMjQsIDQ1Ljk2MDc4OTkwNTQ5Nl0sIFstNjYuNjc2MTY3MzcyOTE1MiwgNDUuOTYxMTI3MTE1MTk0NV0sIFstNjYuNjc1MzMxOTM5NzAxLCA0NS45NjE2NzY2Mzc3MTMyXSwgWy02Ni42NzQ3OTI5NTA1MzA1LCA0NS45NjIxOTQ5MzIzNjY5XSwgWy02Ni42NzYzMjAwODY1MTM1LCA0NS45NjI2NTcwMjIzMDddLCBbLTY2LjY3OTE2Nzc0NTk2NDIsIDQ1Ljk2Mjg4MTgyMTQyNDhdLCBbLTY2LjY4NzcwMTc0MTE2MzMsIDQ1Ljk2Mjc3NTY2NjM5OTVdLCBbLTY2LjY5MjMwMTExNTQxOCwgNDUuOTYyOTg3OTc2MjQ2N10sIFstNjYuNjk3MDA4Mjg3NTA2OCwgNDUuOTYzNDM3NTcwODg0NV0sIFstNjYuNjk4MjI5OTk2MjkzMiwgNDUuOTYzNDUwMDU5NTcyM10sIFstNjYuNjk5NzM5MTY1OTcwNSwgNDUuOTYzMzAwMTk1MTMyM10sIFstNjYuNzAxMzkyMDY2MDkzMywgNDUuOTYzNjc0ODU1NDcyM10sIFstNjYuNzAyNjQwNzI0MzM4MiwgNDUuOTY0MjM2ODQxMjMxN10sIFstNjYuNzAzMDcxOTE1Njc0NiwgNDUuOTYzNjQzNjMzODc0MV0sIFstNjYuNzAzODcxNDE2Mjc3NCwgNDUuOTYzMjg3NzA2NDEwNl1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogMzAsICJOZWlnaGJvdXJoIjogIkdvbGYgQ2x1YiIsICJPQkpFQ1RJRCI6IDMwLCAiU2hhcGVfQXJlYSI6IDU5NzU3NC42OTMwMSwgIlNoYXBlX0xlbmciOiA0ODE0Ljg1OTU5NTcxLCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjY4NzY1NjgyNTM5OTEsIDQ1Ljk2MDAyODA1MzgwNjFdLCBbLTY2LjY4ODE2ODg2NTExMSwgNDUuOTU5Mzc4NTk4MTkyNV0sIFstNjYuNjg5NjMzMTE5MDI0MSwgNDUuOTU2NTM3MTQwMzc2OF0sIFstNjYuNjkwNTMxNDM0MzA4MywgNDUuOTU1Mzk0MjcxMjAxM10sIFstNjYuNjkxMDYxNDQwMzI1OSwgNDUuOTU1MDY5NTE3MTg5OF0sIFstNjYuNjkxODUxOTU3Nzc1OSwgNDUuOTU0Nzk0NzIzODQ3NV0sIFstNjYuNjkyNDgwNzc4NDc0OCwgNDUuOTU1MDAwODE4OTgyXSwgWy02Ni42OTMxNDU1MzE3ODUsIDQ1Ljk1NDg4MjE1ODI0MDZdLCBbLTY2LjY5MzUyMjgyNDIwNDQsIDQ1Ljk1NDU1NzQwMTIyODFdLCBbLTY2LjY5MzcxMTQ3MDQxNCwgNDUuOTU0MDE0MDUzNTA5MV0sIFstNjYuNjkzNjM5NjA1MTkxMywgNDUuOTUzMzU4MjgxOTI2Ml0sIFstNjYuNjkzMTAwNjE2MDIwOCwgNDUuOTUyODIxMTY3OTkyXSwgWy02Ni42OTE2OTkyNDQxNzc2LCA0NS45NTIyNTkwNjY0NDAxXSwgWy02Ni42OTAxODEwOTEzNDc1LCA0NS45NTE5MDMwNjU4NDE5XSwgWy02Ni42ODgwNDMxMDA5NzEyLCA0NS45NTE3OTY4ODk3ODIyXSwgWy02Ni42ODc1ODQ5NjAxNzYzLCA0NS45NTIxMjc5MDg1OTFdLCBbLTY2LjY4NjU3ODg0NzA1ODEsIDQ1Ljk1MzAzOTc2MTUwMDRdLCBbLTY2LjY4NTkzMjA2MDA1MzYsIDQ1Ljk1MzgzOTE4MTg0NTddLCBbLTY2LjY4NTQyMDAyMDM0MTYsIDQ1Ljk1NDY5NDc5ODY1NzldLCBbLTY2LjY4NDk4ODgyOTAwNTIsIDQ1Ljk1NTgxMjcwMTQ0ODddLCBbLTY2LjY4NDcxOTMzNDQyLCA0NS45NTcwMDU1MjI1NzM3XSwgWy02Ni42ODQ3MDEzNjgxMTQzLCA0NS45NTgyMDQ1NjI5NTczXSwgWy02Ni42ODQ5MzQ5MzAwODgyLCA0NS45NTkzOTczMzI1OTU3XSwgWy02Ni42ODU0MTEwMzcxODg4LCA0NS45NjA1NTg4NTMyMjE0XSwgWy02Ni42ODY2ODY2NDQ4OTIyLCA0NS45NjA1MzM4NzQ1Mzk0XSwgWy02Ni42ODc2NTY4MjUzOTkxLCA0NS45NjAwMjgwNTM4MDYxXV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiAzMSwgIk5laWdoYm91cmgiOiAiS2VsbHkncyBDb3VydCBNaW5paG9tZSBQYXJrIiwgIk9CSkVDVElEIjogMzEsICJTaGFwZV9BcmVhIjogMzc1NjYwLjIwNzMzNSwgIlNoYXBlX0xlbmciOiAyNzEzLjA5MjcwMzUzLCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZmZmYjIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjY3MzY4ODAyMjczMSwgNDUuOTY0MjExODY0MjA3OV0sIFstNjYuNjc3ODc0MTcxOTU1LCA0NS45NjQ4ODYyMzk4OTc5XSwgWy02Ni42NzgzNzcyMjg1MTQxLCA0NS45NjUxMDQ3ODU4MTRdLCBbLTY2LjY3OTMyMDQ1OTU2MjQsIDQ1Ljk2NTEyMzUxODI4MDldLCBbLTY2LjY4MzI5OTk5NjI3MTEsIDQ1Ljk2NTcyMjk1Mzg3OTVdLCBbLTY2LjY4MzQxNjc3NzI1OCwgNDUuOTY1NjQxNzgwNjg4Nl0sIFstNjYuNjg0NjQ3NDY5MTk3MywgNDUuOTY1OTA0MDMyMTA3Nl0sIFstNjYuNjg1MDMzNzQ0NzY5NSwgNDUuOTY1OTIyNzY0MzA0M10sIFstNjYuNjg1MjQwMzU3Mjg0OCwgNDUuOTY1ODIyODU5MTgyXSwgWy02Ni42ODUzMzkxNzE5NjYsIDQ1Ljk2NjAxMDE4MTEzODVdLCBbLTY2LjY4NjcwNDYxMTE5NzksIDQ1Ljk2NjA0MTQwMTQwM10sIFstNjYuNjg3MzQyNDE1MDQ5NiwgNDUuOTY2MzY2MDkxMTEwN10sIFstNjYuNjg5NTUyMjcwNjQ4NiwgNDUuOTY2NzE1NzU0ODIxNV0sIFstNjYuNjk0NDY2MDU1MjUyNywgNDUuOTY2ODQ2ODc4MTQ0XSwgWy02Ni43MDA4NjIwNjAwNzU2LCA0NS45NjczNzEzNjgzMzAzXSwgWy02Ni43MDEyODQyNjgyNTkyLCA0NS45NjczMjE0MTcwOTc5XSwgWy02Ni43MDE0MDEwNDkyNDYxLCA0NS45NjY0MjIyODcyMTMxXSwgWy02Ni43MDE4MTQyNzQyNzY4LCA0NS45NjUyOTIxMTAxOTg2XSwgWy02Ni43MDI2NDA3MjQzMzgyLCA0NS45NjQyMzY4NDEyMzE3XSwgWy02Ni43MDEzOTIwNjYwOTMzLCA0NS45NjM2NzQ4NTU0NzIzXSwgWy02Ni42OTk3MzkxNjU5NzA1LCA0NS45NjMzMDAxOTUxMzIzXSwgWy02Ni42OTgyMjk5OTYyOTMyLCA0NS45NjM0NTAwNTk1NzIzXSwgWy02Ni42OTcwMDgyODc1MDY4LCA0NS45NjM0Mzc1NzA4ODQ1XSwgWy02Ni42OTIzMDExMTU0MTgsIDQ1Ljk2Mjk4Nzk3NjI0NjddLCBbLTY2LjY4NzcwMTc0MTE2MzMsIDQ1Ljk2Mjc3NTY2NjM5OTVdLCBbLTY2LjY3OTE2Nzc0NTk2NDIsIDQ1Ljk2Mjg4MTgyMTQyNDhdLCBbLTY2LjY3NjMyMDA4NjUxMzUsIDQ1Ljk2MjY1NzAyMjMwN10sIFstNjYuNjc0NzkyOTUwNTMwNSwgNDUuOTYyMjAxMTc2ODUxMl0sIFstNjYuNjczNjg4MDIyNzMxLCA0NS45NjQyMTE4NjQyMDc5XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiAzMiwgIk5laWdoYm91cmgiOiAiV29vZHN0b2NrIFJvYWQiLCAiT0JKRUNUSUQiOiAzMiwgIlNoYXBlX0FyZWEiOiA3NTgzMzYuODM4Nzg3LCAiU2hhcGVfTGVuZyI6IDUwNDguNDM3NDkwMDMsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZkOGQzYyIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjY5NTQ2Nzg5MjcxMiwgNDUuOTYxNjM5MTcwNDQxOV0sIFstNjYuNjY4NTg1NTkxOTE3MiwgNDUuOTYwNzI3NDU5MDMwM10sIFstNjYuNjY3MDc2NDIyMjM5OSwgNDUuOTU5OTg0MzQwNjg2NF0sIFstNjYuNjYzODk2Mzg2MTM0MSwgNDUuOTU5MTQxMjk1MjA0MV0sIFstNjYuNjYxNjE0NjY1MzEyNSwgNDUuOTU4OTE2NDgwOTA5MV0sIFstNjYuNjU5MTQ0Mjk4MjgxMSwgNDUuOTYyNDM4NDY2NzM0Nl0sIFstNjYuNjU4ODExOTIxNjI2LCA0NS45NjMyNTY0ODQ1OTQyXSwgWy02Ni42NTg3MzEwNzMyNTA0LCA0NS45NjQwOTk0Njc0NjE0XSwgWy02Ni42NjAwNTE1OTY3MTgxLCA0NS45NjQwODA3MzQ2NDgyXSwgWy02Ni42NjE4MzkyNDQxMzM1LCA0NS45NjM3ODcyNTMwODAzXSwgWy02Ni42Njc4MTMwNDA3NzI5LCA0NS45NjIyNDQ4ODgyMjE5XSwgWy02Ni42Njk1NDY3ODkyNzEyLCA0NS45NjE2MzkxNzA0NDE5XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiAzMywgIk5laWdoYm91cmgiOiAiU3Vuc2hpbmUgR2FyZGVucyIsICJPQkpFQ1RJRCI6IDMzLCAiU2hhcGVfQXJlYSI6IDI4NjUzOS4xOTYyNzIsICJTaGFwZV9MZW5nIjogMjIzMS4wMzIwMDMxMywgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmVkOTc2IiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni42MzIxMjI5NzQ1MzQ4LCA0NS45NTQ5MDA4OTQxNjRdLCBbLTY2LjYzMjU1NDE2NTg3MTIsIDQ1Ljk1NjU0OTYzMDYyMDFdLCBbLTY2LjYzMzcwNDAwOTQzNDksIDQ1Ljk1ODU2Njc2Nzk3MDVdLCBbLTY2LjYzNDc1NTAzODMxNzMsIDQ1Ljk1OTU2NTk0MTkzOTJdLCBbLTY2LjYzNjI2NDIwNzk5NDYsIDQ1Ljk2MTM4MzE0MzQwOThdLCBbLTY2LjYzNzg3MjE5MjM1MzIsIDQ1Ljk2Mjc0NDQ0NDI5NDVdLCBbLTY2LjY0MDQyMzQwNzc2MDEsIDQ1Ljk2NDM4MDQ1ODldLCBbLTY2LjY0MjM1NDc4NTYyMDksIDQ1Ljk2NTM5ODI2MDQwMjFdLCBbLTY2LjY0NDUxOTcyNTQ1NTcsIDQ1Ljk2NjEwMzg0MTg3OTJdLCBbLTY2LjY0NzQwMzMxNzUxNzcsIDQ1Ljk2NjUzNDY3OTI0NjhdLCBbLTY2LjY1MDQyMTY1Njg3MjMsIDQ1Ljk2NjQwOTc5OTE5NTNdLCBbLTY2LjY1MzU5MjcwOTgyNTMsIDQ1Ljk2NjEwMzg0MTg3OTJdLCBbLTY2LjY1NjQwNDQzNjY2NDYsIDQ1Ljk2NjQ3ODQ4MzI1ODVdLCBbLTY2LjY1NzczMzk0MzI4NTEsIDQ1Ljk2NjUwMzQ1OTI2MDRdLCBbLTY2LjY1NjI1MTcyMzA2NjMsIDQ1Ljk2NTkyOTAwODM2ODRdLCBbLTY2LjY1NDY3MDY4ODE2NjIsIDQ1Ljk2NTUwNDQxMDQwMjJdLCBbLTY2LjY1MzAxNzc4ODA0MzQsIDQ1Ljk2NTI0MjE1NzA5MTNdLCBbLTY2LjY1MjAwMjY5MTc3MjQsIDQ1Ljk2NTI3OTYyMTkyNl0sIFstNjYuNjUxMTg1MjI0ODYzOCwgNDUuOTY1MDYxMDc2Njk5N10sIFstNjYuNjUwNDg0NTM4OTQyMiwgNDUuOTY0NTU1Mjk3Mjk4MV0sIFstNjYuNjUwNDg0NTM4OTQyMiwgNDUuOTY0MjkzMDM5NDk0MV0sIFstNjYuNjUwOTk2NTc4NjU0MiwgNDUuOTYzNzY4NTIwMTYxNV0sIFstNjYuNjUxOTM5ODA5NzAyNSwgNDUuOTYzNDYyNTQ4MjU3NF0sIFstNjYuNjMyMTIyOTc0NTM0OCwgNDUuOTU0OTAwODk0MTY0XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiAzNCwgIk5laWdoYm91cmgiOiAiRG93bnRvd24iLCAiT0JKRUNUSUQiOiAzNCwgIlNoYXBlX0FyZWEiOiA4MTkyMzYuNzA1Njk3LCAiU2hhcGVfTGVuZyI6IDUzMDAuNzQwMzExMjIsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZkOGQzYyIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjM0MTM1MjAwNzcxMiwgNDUuOTU1NzY4OTg1MDAzNF0sIFstNjYuNjUxOTM5ODA5NzAyNSwgNDUuOTYzNDYyNTQ4MjU3NF0sIFstNjYuNjU0MTU4NjQ4NDU0MywgNDUuOTYzNTgxMTkwNjI0OV0sIFstNjYuNjU2ODM1NjI4MDAwOSwgNDUuOTYzOTk5NTU5MDUwOV0sIFstNjYuNjU4ODI5ODg3OTMxNywgNDUuOTY0MTU1NjY1ODYzMV0sIFstNjYuNjU4NzMxMDczMjUwNCwgNDUuOTY0MDk5NDY3NDYxNF0sIFstNjYuNjU4Nzc1OTg5MDE0NiwgNDUuOTYzNDI1MDgyMTkzOF0sIFstNjYuNjU5MTQ0Mjk4MjgxMSwgNDUuOTYyNDM4NDY2NzM0Nl0sIFstNjYuNjYwNzUyMjgyNjM5NywgNDUuOTU5OTk2ODMwMTUyN10sIFstNjYuNjYxNjc3NTQ3MzgyMywgNDUuOTU4OTE2NDgwOTA5MV0sIFstNjYuNjYxMzA5MjM4MTE1OCwgNDUuOTU4MDg1OTA5MDc2MV0sIFstNjYuNjYwNDAxOTM5Njc4OSwgNDUuOTU3NDczOTAwODExNV0sIFstNjYuNjU2OTYxMzkyMTQwNywgNDUuOTU2ODc0Mzc1OTU3Nl0sIFstNjYuNjU1MjgxNTQyNTU5NCwgNDUuOTU2MzE4NTYwNjYzNF0sIFstNjYuNjUzMjY5MzE2MzIzLCA0NS45NTU1MDY2ODU2MDhdLCBbLTY2LjY1MDQ2NjU3MjYzNjUsIDQ1Ljk1NDE3NjQzMzg0NTNdLCBbLTY2LjY0OTEwMTEzMzQwNDcsIDQ1Ljk1MzY3NjgwMDUyMTNdLCBbLTY2LjY0NzMwNDUwMjgzNjQsIDQ1Ljk1MzE5NTg5OTE5MjddLCBbLTY2LjY0MjkxMTc0MTA5NzEsIDQ1Ljk1MTQ3MjExNDY4OThdLCBbLTY2LjY0MTg3ODY3ODUyMDMsIDQ1Ljk1MDc3ODgzODQxMzldLCBbLTY2LjY0MDcwMTg4NTQ5ODEsIDQ1Ljk1MDQ4NTI4NjM4NjVdLCBbLTY2LjYzOTQ1MzIyNzI1MzIsIDQ1Ljk1MDUyOTAwNjk5OTddLCBbLTY2LjYzODQyOTE0NzgyOTMsIDQ1Ljk1MTIzNDc3Nzg0MThdLCBbLTY2LjYzNzU5MzcxNDYxNTEsIDQ1Ljk1MjA1Mjk2MTEwOTNdLCBbLTY2LjYzNjUzMzcwMjU3OTgsIDQ1Ljk1MzQ4OTQzNjg2MzVdLCBbLTY2LjYzNDEzNTIwMDc3MTIsIDQ1Ljk1NTc2ODk4NTAwMzRdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDM1LCAiTmVpZ2hib3VyaCI6ICJQbGF0IiwgIk9CSkVDVElEIjogMzUsICJTaGFwZV9BcmVhIjogMTU5NjQwMS40MjUzNiwgIlNoYXBlX0xlbmciOiA1NTUxLjM4MTAwMzAxLCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNiZDAwMjYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjYyODk2MDkwNDczNDcsIDQ1LjkzOTUxNjU2ODc5MjFdLCBbLTY2LjYyODk4Nzg1NDE5MzIsIDQ1Ljk0MDI1MzcxNDY0NTddLCBbLTY2LjYyOTEzMTU4NDYzODcsIDQ1Ljk0MDM5NzM5NDQ3NThdLCBbLTY2LjYyOTYwNzY5MTczOTMsIDQ1Ljk0MDUwMzU5MjM3MTldLCBbLTY2LjYzMDA5Mjc4MTk5MjcsIDQ1Ljk0MjAyNzgyMjExNTZdLCBbLTY2LjYzMDc2NjUxODQ1NTgsIDQ1Ljk0MzA5NjAwNzMzMV0sIFstNjYuNjMxMjMzNjQyNDAzNSwgNDUuOTQ0NzU3NTg3ODY5N10sIFstNjYuNjMxNjU1ODUwNTg3MSwgNDUuOTQ3NjU1ODY0Nzk2Nl0sIFstNjYuNjMxNzYzNjQ4NDIxMiwgNDUuOTQ4MDI0Mzg0ODM5OV0sIFstNjYuNjMxODM1NTEzNjQzOSwgNDUuOTQ4MTExODI5OTE0Ml0sIFstNjYuNjMxOTYxMjc3NzgzNywgNDUuOTQ3OTY4MTcwMDc2NF0sIFstNjYuNjMyMDk2MDI1MDc2MywgNDUuOTQ4Mzg2NjU2MzkyN10sIFstNjYuNjMyMTA1MDA4MjI5MSwgNDUuOTUwNjE2NDQ4MTIyOF0sIFstNjYuNjMxOTA3Mzc4ODY2NiwgNDUuOTUxNTE1ODM0NTI0Nl0sIFstNjYuNjMxOTcwMjYwOTM2NSwgNDUuOTU0MjA3NjYwNzc4NV0sIFstNjYuNjMyMTIyOTc0NTM0OCwgNDUuOTU0OTAwODk0MTY0XSwgWy02Ni42MzQxMzUyMDA3NzEyLCA0NS45NTU3Njg5ODUwMDM0XSwgWy02Ni42MzY4NTcwOTYwODIxLCA0NS45NTMxNDU5MzUxNzldLCBbLTY2LjYzNzg5OTE0MTgxMTcsIDQ1Ljk1MTcxNTY5NjE4NzVdLCBbLTY2LjYzODgxNTQyMzQwMTUsIDQ1Ljk1MDk0MTIyODIyOTJdLCBbLTY2LjYzOTYxNDkyNDAwNDQsIDQ1Ljk1MDQ5Nzc3Nzk5MzhdLCBbLTY2LjYzOTU3MDAwODI0MDIsIDQ1Ljk1MDMwNDE1Nzc2NDFdLCBbLTY2LjYzOTMxODQ3OTk2MDYsIDQ1Ljk0OTgzNTcxODkyN10sIFstNjYuNjM4MDc4ODA0ODY4NSwgNDUuOTQ4ODYxMzUzNDY0MV0sIFstNjYuNjM2NzEzMzY1NjM2NywgNDUuOTQ3NTQ5NjgwNjAwNl0sIFstNjYuNjM0OTYxNjUwODMyNiwgNDUuOTQ1MjU3MzAxNTk5XSwgWy02Ni42MzQwNjMzMzU1NDg1LCA0NS45NDQyOTUzNDg2NTk3XSwgWy02Ni42MzMzNzE2MzI3Nzk3LCA0NS45NDMyNDU5MjY0MTZdLCBbLTY2LjYzMjY2MTk2MzcwNTMsIDQ1Ljk0MTQxNTYzNjUxNl0sIFstNjYuNjMyMjEyODA2MDYzMiwgNDUuOTQwNzg0NzAzNDY3OF0sIFstNjYuNjMxNzAwNzY2MzUxMywgNDUuOTQwMzQxMTcxOTc3OV0sIFstNjYuNjMwOTAxMjY1NzQ4NCwgNDUuOTM5OTEwMTMwOTMzM10sIFstNjYuNjI5OTY3MDE3ODUyOSwgNDUuOTM5NjI5MDE1NDAzMl0sIFstNjYuNjI4OTYwOTA0NzM0NywgNDUuOTM5NTE2NTY4NzkyMV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogMzYsICJOZWlnaGJvdXJoIjogIldhdGVybG9vIFJvdyIsICJPQkpFQ1RJRCI6IDM2LCAiU2hhcGVfQXJlYSI6IDU4MDYzNS45MDI4MzQsICJTaGFwZV9MZW5nIjogNDI2MC40ODI0MTc2LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjY0NjQzMzEzNzAxMDgsIDQ1Ljk0MjQxNTExOTcxODFdLCBbLTY2LjY0NTc2ODM4MzcwMDYsIDQ1Ljk0MjA4NDA0MjkwMzFdLCBbLTY2LjY0NTY3ODU1MjE3MjIsIDQ1Ljk0MTg5NjY0MDA1NjFdLCBbLTY2LjY1MDE0MzE3OTEzNDIsIDQ1LjkzNjYwNTM3MTU5NzhdLCBbLTY2LjY1MDI3NzkyNjQyNjksIDQ1LjkzNjMxNzk5MTkxMjZdLCBbLTY2LjY1MDA5ODI2MzM3LCA0NS45MzYxMzY4MTY5OTc4XSwgWy02Ni42NDk2NjcwNzIwMzM3LCA0NS45MzYyMjQyODA4MjM3XSwgWy02Ni42NDc2NjM4Mjg5NTAxLCA0NS45Mzc0ODYyNDM1Mjc5XSwgWy02Ni42NDQyNzcxODAzMjg5LCA0NS45NDAwNTM4MTE2NTM4XSwgWy02Ni42NDM0NDE3NDcxMTQ3LCA0NS45NDA1NTk4MTQ3MDUxXSwgWy02Ni42NDI0MzU2MzM5OTY1LCA0NS45NDA5NjU4NjMxOTY3XSwgWy02Ni42NDEyMjI5MDgzNjI5LCA0NS45NDEyNDY5NzE5NDg5XSwgWy02Ni42NDAxMTc5ODA1NjM1LCA0NS45NDEzMjgxODA4Nzg2XSwgWy02Ni42Mzg4NjAzMzkxNjU3LCA0NS45NDEyMjgyMzE0MDk3XSwgWy02Ni42Mzc4MDkzMTAyODMzLCA0NS45NDE3OTY2OTE2MTIxXSwgWy02Ni42MzcwMjc3NzU5ODYxLCA0NS45NDI1NDYzMDA1NTA3XSwgWy02Ni42MzYxNDc0MjcwMDc3LCA0NS45NDQ1MjAyMjIyNzAzXSwgWy02Ni42MzU4Nzc5MzI0MjI0LCA0NS45NDY1ODE1MjExOTY1XSwgWy02Ni42Mzc1NzU3NDgzMDk0LCA0NS45NDg0MTE2NDA1NTA0XSwgWy02Ni42MzkzMTg0Nzk5NjA2LCA0NS45NDk4MzU3MTg5MjddLCBbLTY2LjYzOTYxNDkyNDAwNDQsIDQ1Ljk1MDQ5Nzc3Nzk5MzhdLCBbLTY2LjY0MTAwNzMxMjY5NDcsIDQ1Ljk1MDUyOTAwNjk5OTddLCBbLTY2LjY0MjExMjI0MDQ5NDIsIDQ1Ljk1MDg4NTAxNjQyMzldLCBbLTY2LjY0MjU0MzQzMTgzMDYsIDQ1Ljk1MDM4NTM1MzQyNjddLCBbLTY2LjY0NTIyOTM5NDUzMDEsIDQ1Ljk0NzAzMTI0ODk1ODNdLCBbLTY2LjY0NDEwNjUwMDQyNSwgNDUuOTQ2NTg3NzY3NDQwNF0sIFstNjYuNjQ0ODQzMTE4OTU3OSwgNDUuOTQ1NzUwNzY0NDg2Ml0sIFstNjYuNjQ1MDIyNzgyMDE0OCwgNDUuOTQ1Mjg4NTMzNTU3NV0sIFstNjYuNjQ0OTQxOTMzNjM5MiwgNDUuOTQ0NzcwMDgwNzY3OF0sIFstNjYuNjQ0NDQ3ODYwMjMyOSwgNDUuOTQzNzE0NDIwOTQzN10sIFstNjYuNjQ0NTI4NzA4NjA4NSwgNDUuOTQzNDgzMjk3NDcxNV0sIFstNjYuNjQ2NDMzMTM3MDEwOCwgNDUuOTQyNDE1MTE5NzE4MV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogMzcsICJOZWlnaGJvdXJoIjogIlVuaXZlcnNpdHkgT2YgTmV3IEJydW5zd2ljayIsICJPQkpFQ1RJRCI6IDM3LCAiU2hhcGVfQXJlYSI6IDcwNDc2My41NzEzODQsICJTaGFwZV9MZW5nIjogNDQ4MC40NjM4ODI1LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjY0NjQzMzEzNzAxMDgsIDQ1Ljk0MjQxNTExOTcxODFdLCBbLTY2LjY0NDUyODcwODYwODUsIDQ1Ljk0MzQ4MzI5NzQ3MTVdLCBbLTY2LjY0NDQ0Nzg2MDIzMjksIDQ1Ljk0MzcxNDQyMDk0MzddLCBbLTY2LjY0NDk0MTkzMzYzOTIsIDQ1Ljk0NDc3MDA4MDc2NzhdLCBbLTY2LjY0NTAyMjc4MjAxNDgsIDQ1Ljk0NTI4ODUzMzU1NzVdLCBbLTY2LjY0NDg0MzExODk1NzksIDQ1Ljk0NTc1MDc2NDQ4NjJdLCBbLTY2LjY0NDEwNjUwMDQyNSwgNDUuOTQ2NTg3NzY3NDQwNF0sIFstNjYuNjQ1MjI5Mzk0NTMwMSwgNDUuOTQ3MDMxMjQ4OTU4M10sIFstNjYuNjQ4NTE3MjI4NDcsIDQ1Ljk0MzI4OTY1MjczOTRdLCBbLTY2LjY0NjQzMzEzNzAxMDgsIDQ1Ljk0MjQxNTExOTcxODFdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDM4LCAiTmVpZ2hib3VyaCI6ICJTYWludCBUaG9tYXMgVW5pdmVyc2l0eSIsICJPQkpFQ1RJRCI6IDM4LCAiU2hhcGVfQXJlYSI6IDg0ODEzLjE1ODUzNzEsICJTaGFwZV9MZW5nIjogMTM0MS41Mzg0ODM1OSwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmVkOTc2IiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni42NDg1MTcyMjg0NywgNDUuOTQzMjg5NjUyNzM5NF0sIFstNjYuNjQ1MjI5Mzk0NTMwMSwgNDUuOTQ3MDMxMjQ4OTU4M10sIFstNjYuNjQyMTEyMjQwNDk0MiwgNDUuOTUwODg1MDE2NDIzOV0sIFstNjYuNjQyOTExNzQxMDk3MSwgNDUuOTUxNDcyMTE0Njg5OF0sIFstNjYuNjQ2MDczODEwODk3MiwgNDUuOTUyNjcxMjc0ODAyM10sIFstNjYuNjUyNjIyNTI5MzE4NCwgNDUuOTQ0OTk0OTUyNDUyOF0sIFstNjYuNjQ4NTE3MjI4NDcsIDQ1Ljk0MzI4OTY1MjczOTRdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDM5LCAiTmVpZ2hib3VyaCI6ICJDb2xsZWdlIEhpbGwiLCAiT0JKRUNUSUQiOiAzOSwgIlNoYXBlX0FyZWEiOiAzNjY3ODcuMDcyMDc5LCAiU2hhcGVfTGVuZyI6IDI3MTMuMjU2ODE0MzgsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlYjI0YyIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjUyNDUxODQ5NDE0NCwgNDUuOTQ0OTE5OTk1MzI1OF0sIFstNjYuNjUyNjIyNTI5MzE4NCwgNDUuOTQ0OTk0OTUyNDUyOF0sIFstNjYuNjQ2MDczODEwODk3MiwgNDUuOTUyNjcxMjc0ODAyM10sIFstNjYuNjQ3MzA0NTAyODM2NCwgNDUuOTUzMTk1ODk5MTkyN10sIFstNjYuNjUwMTM0MTk1OTgxNCwgNDUuOTU0MDM5MDM1MTMwM10sIFstNjYuNjU0ODY4MzE3NTI4NywgNDUuOTU2MTY4Njc2OTMzXSwgWy02Ni42NTY5NjEzOTIxNDA3LCA0NS45NTY4NzQzNzU5NTc2XSwgWy02Ni42NTc3MDY5OTM4MjY1LCA0NS45NTY5ODA1NDIyODk4XSwgWy02Ni42NTg3NDkwMzk1NTYxLCA0NS45NTY0MTg0ODI5MjUxXSwgWy02Ni42NjAyODUxNTg2OTE5LCA0NS45NTYwMDAwNTcyNTE4XSwgWy02Ni42NjU3NjQ4ODE5MjUxLCA0NS45NDk2Nzk1NzE3NjgxXSwgWy02Ni42NjY0NTY1ODQ2OTM4LCA0NS45NDkwNTQ5Nzg3MzM5XSwgWy02Ni42NjY4NTE4NDM0MTg5LCA0NS45NDg0ODY1OTI5NTYxXSwgWy02Ni42NjcxMzAzMjExNTY5LCA0NS45NDc3MTgzMjU5OTMzXSwgWy02Ni42NjcxNTcyNzA2MTU1LCA0NS45NDY5MzEzMDk3NzFdLCBbLTY2LjY2NjkyMzcwODY0MTYsIDQ1Ljk0NjE1Njc3NDk2MDNdLCBbLTY2LjY2NjU2NDM4MjUyOCwgNDUuOTQ1NTc1ODY2NzUwMl0sIFstNjYuNjYyMzQyMzAwNjkyNiwgNDUuOTQzNzgzMTMzMTQxNV0sIFstNjYuNjU3MTMyMDcyMDQ0NywgNDUuOTQxODA5MTg1MTc3NF0sIFstNjYuNjU1NTUxMDM3MTQ0NiwgNDUuOTQyNDA4ODczMDA0MV0sIFstNjYuNjU0MzgzMjI3Mjc1MywgNDUuOTQzMDY0Nzc0MTM3Ml0sIFstNjYuNjUzMjE1NDE3NDA1OSwgNDUuOTQ0MDIwNTAxODk2OV0sIFstNjYuNjUyNDUxODQ5NDE0NCwgNDUuOTQ0OTE5OTk1MzI1OF1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogNDAsICJOZWlnaGJvdXJoIjogIlRoZSBIaWxsIiwgIk9CSkVDVElEIjogNDAsICJTaGFwZV9BcmVhIjogMTYzNzE0OS41NzQwNywgIlNoYXBlX0xlbmciOiA0OTM0LjkwODE2ODE5LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWIyNGMiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjYzMDUzMjk1NjQ4MTksIDQ1LjkzOTc3MjY5Njg1MjJdLCBbLTY2LjYzMTY0Njg2NzQzNDIsIDQ1Ljk0MDMwMzY5MDI4MV0sIFstNjYuNjMyMzU2NTM2NTA4NywgNDUuOTQwOTQwODc1NjgzMV0sIFstNjYuNjMzNjIzMTYxMDU5MywgNDUuOTQzNjc2OTQxNTI3Ml0sIFstNjYuNjM1ODc3OTMyNDIyNCwgNDUuOTQ2NTgxNTIxMTk2NV0sIFstNjYuNjM2MDg0NTQ0OTM3OCwgNDUuOTQ0Nzc2MzI3MjE1OV0sIFstNjYuNjM2NzQ5Mjk4MjQ4LCA0NS45NDI5NzEwNzQ0NTA0XSwgWy02Ni42Mzc2NTY1OTY2ODUsIDQ1Ljk0MTkxNTM4MDM2OTNdLCBbLTY2LjYzODQ4MzA0Njc0NjQsIDQ1Ljk0MTM5Njg5NjAzMzldLCBbLTY2LjYzODg2MDMzOTE2NTcsIDQ1Ljk0MTIyODIzMTQwOTddLCBbLTY2LjYzOTA0MDAwMjIyMjUsIDQ1Ljk0MTI1MzIxODc5MzhdLCBbLTY2LjYzODk3NzEyMDE1MjYsIDQ1Ljk0MTEzNDUyODYxOV0sIFstNjYuNjM4MzU3MjgyNjA2NiwgNDUuOTQwMzcyNDA2NzA2XSwgWy02Ni42MzU3NTIxNjgyODI3LCA0NS45Mzk0OTE1ODA2MjUzXSwgWy02Ni42MzUwODc0MTQ5NzI0LCA0NS45Mzg1ODU3NTE5NzY2XSwgWy02Ni42MzQzMzI4MzAxMzM3LCA0NS45MzY0NDkxODcxNzExXSwgWy02Ni42MzMzMzU3MDAxNjg0LCA0NS45MzUxMTg0NzgwMTQ2XSwgWy02Ni42Mjk5NzYwMDEwMDU4LCA0NS45MzIzMTk1MTEzNTAyXSwgWy02Ni42Mjc5Mjc4NDIxNTgsIDQ1LjkzMDIzODkzNzkwNzJdLCBbLTY2LjYyNzY3NjMxMzg3ODQsIDQ1LjkzMDEwMTQ3OTg1NjFdLCBbLTY2LjYyNzI4MTA1NTE1MzQsIDQ1LjkzMDA3NjQ4NzQ0NjZdLCBbLTY2LjYyNjgwNDk0ODA1MjgsIDQ1LjkzMDM1MTQwMzMzMTldLCBbLTY2LjYyNjg0MDg4MDY2NDIsIDQ1LjkzMDczMjUzNDQ2NDNdLCBbLTY2LjYyNzQwNjgxOTI5MzIsIDQ1LjkzMTM2OTgyOTg1MTFdLCBbLTY2LjYyODE0MzQzNzgyNjIsIDQ1LjkzMTg0NDY3MjYzMzNdLCBbLTY2LjYzMDE0NjY4MDkwOTcsIDQ1LjkzMzczMTUwNzcyNThdLCBbLTY2LjYzMTU3NTAwMjIxMTUsIDQ1LjkzNTE5OTY5NTkyMDRdLCBbLTY2LjYzMTk2MTI3Nzc4MzcsIDQ1LjkzNTg2MTkyOTc4OThdLCBbLTY2LjYzMjAzMzE0MzAwNjQsIDQ1LjkzNjMzNjczNDExMTRdLCBbLTY2LjYzMTY5MTc4MzE5ODQsIDQ1LjkzNzYwNDk0MTUxMjVdLCBbLTY2LjYzMDUzMjk1NjQ4MTksIDQ1LjkzOTc3MjY5Njg1MjJdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDQxLCAiTmVpZ2hib3VyaCI6ICJGb3Jlc3QgSGlsbCIsICJPQkpFQ1RJRCI6IDQxLCAiU2hhcGVfQXJlYSI6IDM5NjA0MC4xNDQ0NDgsICJTaGFwZV9MZW5nIjogNDQyMi4yMDg2NzUyNSwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmViMjRjIiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni42MzUyMjIxNjIyNjUsIDQ1LjkzODg0MTg4NDMzNjVdLCBbLTY2LjYzNjc1ODI4MTQwMDksIDQ1LjkzODkxMDYwMjU3MzJdLCBbLTY2LjYzNzk4ODk3MzM0MDEsIDQ1LjkzODg0ODEzMTQ1MjRdLCBbLTY2LjYzOTE5MjcxNTgyMDgsIDQ1LjkzODY2Njk2NDgwNDJdLCBbLTY2LjY0MDYzOTAwMzQyODMsIDQ1LjkzODI5ODM4MjU1NDddLCBbLTY2LjY0NzYwMDk0Njg4MDIsIDQ1LjkzNTUzMDgxMzg0MzZdLCBbLTY2LjY1MDQ5MzUyMjA5NSwgNDUuOTMzOTkzOTEwMTcwN10sIFstNjYuNjUwMTUyMTYyMjg3MSwgNDUuOTMzMTI1NDc4Mjg2OF0sIFstNjYuNjQ3OTk2MjA1NjA1MiwgNDUuOTMxNTU3MjY4Mjc3MV0sIFstNjYuNjQwMDI4MTQ5MDM1MSwgNDUuOTI3MjE0NzgyMDkxNV0sIFstNjYuNjM4MDk2NzcxMTc0MiwgNDUuOTI1ODI3NjE0MTQyNV0sIFstNjYuNjM2MDU3NTk1NDc5MywgNDUuOTI0OTAyODE2MjM4NV0sIFstNjYuNjMyNzc4NzQ0NjkyMiwgNDUuOTI3MjU4NTIxMDU3M10sIFstNjYuNjMxMDAwMDgwNDI5NywgNDUuOTI5MzcwNDQ3MjI1XSwgWy02Ni42MzAwNTY4NDkzODEzLCA0NS45Mjk2NTE2MTQ3NjE4XSwgWy02Ni42Mjg4MTcxNzQyODkzLCA0NS45Mjk4NDUzMDcxMjQ3XSwgWy02Ni42Mjc5MTg4NTkwMDUxLCA0NS45MzAyMzI2ODk4MjEzXSwgWy02Ni42Mjk5NzYwMDEwMDU4LCA0NS45MzIzMTk1MTEzNTAyXSwgWy02Ni42MzI2OTc4OTYzMTY2LCA0NS45MzQ0ODc0NzMzMTAyXSwgWy02Ni42MzM0Nzk0MzA2MTM4LCA0NS45MzUyODA5MTM3MDcyXSwgWy02Ni42MzQ1MTI0OTMxOTA2LCA0NS45MzY3OTI3OTIzMjkzXSwgWy02Ni42MzUyMjIxNjIyNjUsIDQ1LjkzODg0MTg4NDMzNjVdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDQyLCAiTmVpZ2hib3VyaCI6ICJTa3lsaW5lIEFjcmVhIiwgIk9CSkVDVElEIjogNDIsICJTaGFwZV9BcmVhIjogMTQ1NzUxMC4wODc2MSwgIlNoYXBlX0xlbmciOiA0ODk0LjY2MDAyMjIsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlYjI0YyIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjM1MjIyMTYyMjY1LCA0NS45Mzg4NDE4ODQzMzY1XSwgWy02Ni42MzU4ODY5MTU1NzUzLCA0NS45Mzk2MDQwMjcyODcxXSwgWy02Ni42MzgzNTcyODI2MDY2LCA0NS45NDAzNzI0MDY3MDZdLCBbLTY2LjYzOTA0MDAwMjIyMjUsIDQ1Ljk0MTI1MzIxODc5MzhdLCBbLTY2LjY0MDczNzgxODEwOTUsIDQ1Ljk0MTI5Njk0NjY4ODldLCBbLTY2LjY0MjQzNTYzMzk5NjUsIDQ1Ljk0MDk2NTg2MzE5NjddLCBbLTY2LjY0Mzk0NDgwMzY3MzgsIDQ1Ljk0MDI3ODcwMjQ2OV0sIFstNjYuNjQ3NjYzODI4OTUwMSwgNDUuOTM3NDg2MjQzNTI3OV0sIFstNjYuNjQ5NzI5OTU0MTAzNSwgNDUuOTM2MTg2Nzk2MzQzN10sIFstNjYuNjUwMTQzMTc5MTM0MiwgNDUuOTM2MTU1NTU5MjU3OF0sIFstNjYuNjUwNTExNDg4NDAwNywgNDUuOTM1MTc0NzA1ODA4Ml0sIFstNjYuNjUwNDkzNTIyMDk1LCA0NS45MzM5OTM5MTAxNzA3XSwgWy02Ni42NDc2MDA5NDY4ODAyLCA0NS45MzU1MzA4MTM4NDM2XSwgWy02Ni42NDA2MzkwMDM0MjgzLCA0NS45MzgyOTgzODI1NTQ3XSwgWy02Ni42MzkxOTI3MTU4MjA4LCA0NS45Mzg2NjY5NjQ4MDQyXSwgWy02Ni42Mzc5ODg5NzMzNDAxLCA0NS45Mzg4NDgxMzE0NTI0XSwgWy02Ni42MzY3NTgyODE0MDA5LCA0NS45Mzg5MTA2MDI1NzMyXSwgWy02Ni42MzUyMjIxNjIyNjUsIDQ1LjkzODg0MTg4NDMzNjVdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDQzLCAiTmVpZ2hib3VyaCI6ICJQb2V0J3MgSGlsbCIsICJPQkpFQ1RJRCI6IDQzLCAiU2hhcGVfQXJlYSI6IDI5NzAyMC43MjgwNTgsICJTaGFwZV9MZW5nIjogMzA4NC4xMTAyMzIwNSwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmVkOTc2IiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni42MjE1NDA4MjA0ODc5LCA0NS45MzA4MjYyNTQ4MzM0XSwgWy02Ni42MjE3OTIzNDg3Njc0LCA0NS45MzExOTQ4ODY3NDg2XSwgWy02Ni42MjI2MDA4MzI1MjMxLCA0NS45MzE4ODg0MDc5NDgzXSwgWy02Ni42MjI2NjM3MTQ1OTMsIDQ1LjkzMjAzMjEwOTQ1NDZdLCBbLTY2LjYyMjUwMjAxNzg0MTksIDQ1LjkzMTkzMjE0MzIyODhdLCBbLTY2LjYyMjU3Mzg4MzA2NDYsIDQ1LjkzMjA3NTg0NDYyMTddLCBbLTY2LjYyMjg4ODI5MzQxNDEsIDQ1LjkzMjE1NzA2Njk4MzVdLCBbLTY2LjYyMjg1MjM2MDgwMjcsIDQ1LjkzMjI1NzAzMjgwMzldLCBbLTY2LjYyMzE4NDczNzQ1NzgsIDQ1LjkzMjU5NDQxNjExNzZdLCBbLTY2LjYyNDAxMTE4NzUxOTIsIDQ1LjkzMzEzMTcyNjA0NjddLCBbLTY2LjYyNDc3NDc1NTUxMDcsIDQ1LjkzNDQ2ODczMDQ4NjRdLCBbLTY2LjYyNjM3Mzc1NjcxNjQsIDQ1LjkzNTkyNDQwNDI3NDldLCBbLTY2LjYyNzI4MTA1NTE1MzQsIDQ1LjkzNjk2MTQ3MDQ0NjFdLCBbLTY2LjYyNzY1ODM0NzU3MjcsIDQ1LjkzNzIwNTExNTcwODhdLCBbLTY2LjYyODk2MDkwNDczNDcsIDQ1LjkzOTUxNjU2ODc5MjFdLCBbLTY2LjYzMDUzMjk1NjQ4MTksIDQ1LjkzOTc3MjY5Njg1MjJdLCBbLTY2LjYzMTQ5NDE1MzgzNTksIDQ1LjkzODA5ODQ3MjUxMzNdLCBbLTY2LjYzMjAzMzE0MzAwNjQsIDQ1LjkzNjIxODAzMzQxMjFdLCBbLTY2LjYzMTY1NTg1MDU4NzEsIDQ1LjkzNTI5OTY1NjI1NjVdLCBbLTY2LjYzMDE0NjY4MDkwOTcsIDQ1LjkzMzczMTUwNzcyNThdLCBbLTY2LjYyODE0MzQzNzgyNjIsIDQ1LjkzMTg0NDY3MjYzMzNdLCBbLTY2LjYyNzQwNjgxOTI5MzIsIDQ1LjkzMTM2OTgyOTg1MTFdLCBbLTY2LjYyNjk2NjY0NDgwNCwgNDUuOTMwODUxMjQ2OTA1MV0sIFstNjYuNjI1MjA1OTQ2ODQ3MSwgNDUuOTMxMjgyMzU4MzY4OF0sIFstNjYuNjI0NTA1MjYwOTI1NSwgNDUuOTMxMjAxMTM0NzI2XSwgWy02Ni42MjM3OTU1OTE4NTEsIDQ1LjkzMDg4ODczNDk5MTVdLCBbLTY2LjYyMzExMjg3MjIzNTEsIDQ1LjkzMDc0NTAzMDUyMjddLCBbLTY2LjYyMjIzMjUyMzI1NjYsIDQ1LjkzMDcyMDAzODQwMzFdLCBbLTY2LjYyMTU0MDgyMDQ4NzksIDQ1LjkzMDgyNjI1NDgzMzRdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDQ0LCAiTmVpZ2hib3VyaCI6ICJEdW4ncyBDcm9zc2luZyIsICJPQkpFQ1RJRCI6IDQ0LCAiU2hhcGVfQXJlYSI6IDM2MzU0My4yNzgzMjMsICJTaGFwZV9MZW5nIjogMjkyMS45NDYyNTk3LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWIyNGMiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjYxOTgyNTAzODI5NTIsIDQ1LjkyOTY3NjYwNzM2MjddLCBbLTY2LjYyMTU0MDgyMDQ4NzksIDQ1LjkzMDgyNjI1NDgzMzRdLCBbLTY2LjYyMjk0MjE5MjMzMTEsIDQ1LjkzMDcyNjI4NjQzNDFdLCBbLTY2LjYyMzc5NTU5MTg1MSwgNDUuOTMwODg4NzM0OTkxNV0sIFstNjYuNjI0NjQwMDA4MjE4MSwgNDUuOTMxMjMyMzc0NjAyN10sIFstNjYuNjI1NjI4MTU1MDMwNiwgNDUuOTMxMjQ0ODcwNTQ4NV0sIFstNjYuNjI2OTY2NjQ0ODA0LCA0NS45MzA4NTEyNDY5MDUxXSwgWy02Ni42MjY3NjkwMTU0NDE1LCA0NS45MzA0NTEzNzI0MDY5XSwgWy02Ni42MjcxMjgzNDE1NTUxLCA0NS45MzAxMDc3Mjc5NTY3XSwgWy02Ni42Mjc1OTU0NjU1MDI5LCA0NS45MzAwODI3MzU1NV0sIFstNjYuNjI3OTE4ODU5MDA1MSwgNDUuOTMwMjMyNjg5ODIxM10sIFstNjYuNjI4ODE3MTc0Mjg5MywgNDUuOTI5ODQ1MzA3MTI0N10sIFstNjYuNjMwMDU2ODQ5MzgxMywgNDUuOTI5NjUxNjE0NzYxOF0sIFstNjYuNjMxMDAwMDgwNDI5NywgNDUuOTI5MzcwNDQ3MjI1XSwgWy02Ni42MzI3Nzg3NDQ2OTIyLCA0NS45MjcyNTg1MjEwNTczXSwgWy02Ni42MzUyODUwNDQzMzQ5LCA0NS45MjUzOTY0NjAyODEyXSwgWy02Ni42MzYwNTc1OTU0NzkzLCA0NS45MjQ5MDI4MTYyMzg1XSwgWy02Ni42MzYyNzMxOTExNDc0LCA0NS45MjQ5ODQwNDkxMDQ0XSwgWy02Ni42MzU2MzUzODcyOTU3LCA0NS45MjQ0MDkxNjc4MDNdLCBbLTY2LjYzMjczMzgyODkyOCwgNDUuOTIyNTcyMDA3MTg0Nl0sIFstNjYuNjI4NjI4NTI4MDc5NiwgNDUuOTE5NjQ3NDIxOTIyNl0sIFstNjYuNjI1NjY0MDg3NjQyLCA0NS45MTc4NDEzNTEwNDA0XSwgWy02Ni42MjQ3Mjk4Mzk3NDY1LCA0NS45MTc4MzUxMDE1NTgxXSwgWy02Ni42MjQwNzQwNjk1ODkxLCA0NS45MTgxNzI1NzI1OTM3XSwgWy02Ni42MjA4NDkxMTc3MTkxLCA0NS45MjE5MDMzNjU2MDFdLCBbLTY2LjYxOTc2MjE1NjIyNTMsIDQ1LjkyMzU4NDMyNzcwNF0sIFstNjYuNjE5NDI5Nzc5NTcwMiwgNDUuOTI0MzQ2NjgwMzQ2MV0sIFstNjYuNjE5MzY2ODk3NTAwMywgNDUuOTI1NjUyNjUzNTU5M10sIFstNjYuNjE5ODI1MDM4Mjk1MiwgNDUuOTI5Njc2NjA3MzYyN11dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogNDUsICJOZWlnaGJvdXJoIjogIlNvdXRod29vZCBQYXJrIiwgIk9CSkVDVElEIjogNDUsICJTaGFwZV9BcmVhIjogMTIxODM5OC4wNDE4MSwgIlNoYXBlX0xlbmciOiA0MzczLjgyNDMzNjAyLCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbWy02Ni41ODg0ODI4MTgwMzIzLCA0NS45MTM1MTY1NDEwMjUyXSwgWy02Ni41ODg2MzU1MzE2MzA2LCA0NS45MTM3MjI3ODk2MTg2XSwgWy02Ni41ODg1MDMwMDk1MjI2LCA0NS45MTM1MjIwNTk5MTk1XSwgWy02Ni41ODg0ODI4MTgwMzIzLCA0NS45MTM1MTY1NDEwMjUyXV1dLCBbW1stNjYuNTk4NjI0Nzk3NTksIDQ1Ljg5ODA4OTQ3Mzk0MzVdLCBbLTY2LjU5NzE3ODUwOTk4MjYsIDQ1Ljg5ODI2NDUyMTQzOV0sIFstNjYuNTk1ODQwMDIwMjA5MiwgNDUuODk4Njg5NjM0NDg3OF0sIFstNjYuNTk0Njk5MTU5Nzk4NCwgNDUuODk5MzMzNTQ5NTI0OF0sIFstNjYuNTg2NjIzMzA1Mzk0MiwgNDUuOTA4NDg1MDg3OTI5OV0sIFstNjYuNTg2ODExOTUxNjAzOCwgNDUuOTA5OTE2NDQyMTI1N10sIFstNjYuNTg3MTQ0MzI4MjU4OSwgNDUuOTExMDQxNDk4MTE3M10sIFstNjYuNTg3NzczMTQ4OTU3OCwgNDUuOTEyNDE2NTM1NTgxN10sIFstNjYuNTg4NTAzMDA5NTIyNiwgNDUuOTEzNTIyMDU5OTE5NV0sIFstNjYuNTg5NDg4OTMxMTUwNSwgNDUuOTEzNzkxNTM4OTc5NF0sIFstNjYuNTkwNTU3OTI2MzM4NiwgNDUuOTEzOTEwMjg3Njc0N10sIFstNjYuNTkyNDcxMzM3ODkzOCwgNDUuOTEzNzE2NTM5NjcyNV0sIFstNjYuNTk0MTMzMjIxMTY5NCwgNDUuOTEyMTA0MDMwMDU4NF0sIFstNjYuNTk1ODc1OTUyODIwNiwgNDUuOTEwMDYwMjAwNTUxXSwgWy02Ni41OTg5MjEyNDE2MzM3LCA0NS45MDU4MDM1NDMzODk3XSwgWy02Ni42MDA0MjE0MjgxNTgyLCA0NS45MDIyNzc5NTkwNjIzXSwgWy02Ni42MDA2NzI5NTY0Mzc4LCA0NS45MDEzNzc3NzM5OTIxXSwgWy02Ni42MDA3NjI3ODc5NjYyLCA0NS45MDAyNDAwMTkyMDNdLCBbLTY2LjYwMDY2Mzk3MzI4NDksIDQ1Ljg5OTMyNzI5Nzk1ODRdLCBbLTY2LjYwMDMyMjYxMzQ3NywgNDUuODk4MjA4MjU2MjMyN10sIFstNjYuNTk4NjI0Nzk3NTksIDQ1Ljg5ODA4OTQ3Mzk0MzVdXV1dLCAidHlwZSI6ICJNdWx0aVBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDQ2LCAiTmVpZ2hib3VyaCI6ICJMaW5jb2xuIEhlaWdodHMiLCAiT0JKRUNUSUQiOiA0NiwgIlNoYXBlX0FyZWEiOiAxMDkyNDYxLjI4ODI5LCAiU2hhcGVfTGVuZyI6IDQ1MDUuNjc3ODIxNzQsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlYjI0YyIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNTUyNDg3MzI0NTk3NiwgNDUuODk1MDUxMDYxNjQyNl0sIFstNjYuNTUxMzE5NTE0NzI4MiwgNDUuODk1NDE5OTMxMjYxNF0sIFstNjYuNTUxMjI5NjgzMTk5OSwgNDUuODk1ODQ1MDY2MDg4XSwgWy02Ni41NTEzOTEzNzk5NTEsIDQ1Ljg5NjQzODk5ODk5ODhdLCBbLTY2LjU1MTEzMDg2ODUxODYsIDQ1Ljg5NjgwMTYwNzU0NzZdLCBbLTY2LjU1MTE5Mzc1MDU4ODUsIDQ1Ljg5Njk0NTM5OTkzNzJdLCBbLTY2LjU1NTcxMjI3NjQ2NzYsIDQ1Ljg5OTkxNDk0MjEyMzhdLCBbLTY2LjU1Nzg5NTE4MjYwOCwgNDUuOTAxMTQwMjIyNzIwMV0sIFstNjYuNTYwMTk0ODY5NzM1NCwgNDUuOTAyMjQwNDUxNjQyNF0sIFstNjYuNTYyNTAzNTQwMDE1NSwgNDUuOTAyNzkwNTU3OTI3NF0sIFstNjYuNTY0NjIzNTY0MDg2MSwgNDUuOTAzMDQwNjA0NDM2OV0sIFstNjYuNTY0OTgyODkwMTk5NywgNDUuOTAzMjk2OTAwOTQwNF0sIFstNjYuNTY4MDE5MTk1ODYsIDQ1LjkwNDM5NzA4NzEyNF0sIFstNjYuNTY4NTA0Mjg2MTEzNSwgNDUuOTA0NzM0NjM5ODc3NV0sIFstNjYuNTY5MDUyMjU4NDM2OCwgNDUuOTA0ODE1OTAyMjcwOV0sIFstNjYuNTcwOTI5NzM3MzgwNiwgNDUuOTA1NTc4NTEyNzgxOF0sIFstNjYuNTcwOTkyNjE5NDUwNSwgNDUuOTA1OTE2MDU4MzUxN10sIFstNjYuNTcyMjA1MzQ1MDg0LCA0NS45MDU5NTk4MTQxMDg2XSwgWy02Ni41NzUxMTU4ODY2MDQ2LCA0NS45MDcyNzI0NzA3NzkxXSwgWy02Ni41NzYyNjU3MzAxNjgzLCA0NS45MDc2NDc1MDk4NDA4XSwgWy02Ni41Nzc3ODM4ODI5OTg0LCA0NS45MDg3OTEzNjMzMjkxXSwgWy02Ni41Nzg2MzcyODI1MTgzLCA0NS45MDkyNjAxNDg5MzI1XSwgWy02Ni41ODAxNDY0NTIxOTU2LCA0NS45MDk4MDM5MzUyNzIzXSwgWy02Ni41ODE2NjQ2MDUwMjU4LCA0NS45MTA3MzUyMzUxMzQyXSwgWy02Ni41ODgyODUxODg2Njk4LCA0NS45MTU0NzI3NDY4NDA5XSwgWy02Ni41OTAyODg0MzE3NTM0LCA0NS45MTcwNzg5MDkwMDc5XSwgWy02Ni41OTA5NTMxODUwNjM2LCA0NS45MTc5Mjg4NDM3MTg0XSwgWy02Ni41OTI0MDg0NTU4MjM5LCA0NS45MTg4OTc1MDM0MzM5XSwgWy02Ni41OTI3NzY3NjUwOTA0LCA0NS45MTk0MDk5NDg4MzExXSwgWy02Ni41OTM2ODQwNjM1MjczLCA0NS45MjAwNDExMjUwNzE5XSwgWy02Ni41OTc5OTU5NzY4OTExLCA0NS45MjIzMjIwNDg2NTcyXSwgWy02Ni42MDE3MjM5ODUzMjAyLCA0NS45MjQ5NDAzMDgzNDUyXSwgWy02Ni42MDIxMDEyNzc3Mzk1LCA0NS45MjQ5NDAzMDgzNDUyXSwgWy02Ni42MDI2MzEyODM3NTcyLCA0NS45MjUxMjc3Njg0OTldLCBbLTY2LjYwMzMyMjk4NjUyNTksIDQ1LjkyNTc3MTM3Njg3MjRdLCBbLTY2LjYwMzk2OTc3MzUzMDUsIDQ1LjkyNTg4Mzg1MTM1NTZdLCBbLTY2LjYwNDYwNzU3NzM4MjIsIDQ1LjkyNjE5MDAzMDczNzldLCBbLTY2LjYwNTUwNTg5MjY2NjMsIDQ1LjkyNjQxNDk3Nzc3ODddLCBbLTY2LjYwNzYzNDg5OTg4OTcsIDQ1LjkyNjc2NDg5MzU4NDVdLCBbLTY2LjYwOTE0NDA2OTU2NywgNDUuOTI2ODI3Mzc4MzE3NV0sIFstNjYuNjExMDY2NDY0Mjc1MSwgNDUuOTI2NzMzNjUxMTkxNl0sIFstNjYuNjEyNTc1NjMzOTUyNCwgNDUuOTI2OTQ2MDk5MTE2NF0sIFstNjYuNjEzMDUxNzQxMDUzLCA0NS45MjczMjcyNTM2NDgxXSwgWy02Ni42MTM5MTQxMjM3MjU3LCA0NS45Mjc0ODM0NjM3NjUyXSwgWy02Ni42MTg1MDQ1MTQ4Mjc2LCA0NS45MjkyMDE3NDYwMTg3XSwgWy02Ni42MTg4OTk3NzM1NTI2LCA0NS45MjkyNDU0ODM0MTc4XSwgWy02Ni42MTk4MjUwMzgyOTUyLCA0NS45Mjk2NzY2MDczNjI3XSwgWy02Ni42MTkzOTM4NDY5NTg4LCA0NS45MjY0MTQ5Nzc3Nzg3XSwgWy02Ni42MTAyMzEwMzEwNjA4LCA0NS45MjAxODQ4NTcyNzE2XSwgWy02Ni42MDcxOTQ3MjU0MDA1LCA0NS45MTg4MTAwMTIyODMzXSwgWy02Ni42MDQwNzc1NzEzNjQ2LCA0NS45MTc1MjI2MjY1NDddLCBbLTY2LjYwMzI2MDEwNDQ1NjEsIDQ1LjkxODc3ODc2NTQxMDRdLCBbLTY2LjYwMjE0NjE5MzUwMzcsIDQ1LjkxOTkxNjE0MDI0NzhdLCBbLTY2LjYwMDc3MTc3MTExOSwgNDUuOTIwOTAzNTEyNjg0N10sIFstNjYuNTk5NDUxMjQ3NjUxNCwgNDUuOTIxNTkwOTEzNTAwM10sIFstNjYuNTk0MzMwODUwNTMxOSwgNDUuOTE4NTI4Nzg5NzkzNV0sIFstNjYuNTkyNTc5MTM1NzI3OSwgNDUuOTE3MjAzOTAwMjIyOV0sIFstNjYuNTkzMjA3OTU2NDI2OCwgNDUuOTE2NDkxNDQ2NTI1OF0sIFstNjYuNTk0MjMyMDM1ODUwNywgNDUuOTE1Nzc4OTgzNjgxM10sIFstNjYuNTk1NDcxNzEwOTQyNywgNDUuOTE1MjY2NTA0NzUxMV0sIFstNjYuNTk2ODU1MTE2NDgwMywgNDUuOTE0OTg1MjY0MzAyNV0sIFstNjYuNTkyNDcxMzM3ODkzOCwgNDUuOTEzNzE2NTM5NjcyNV0sIFstNjYuNTkwNTU3OTI2MzM4NiwgNDUuOTEzOTEwMjg3Njc0N10sIFstNjYuNTg5NDg4OTMxMTUwNSwgNDUuOTEzNzkxNTM4OTc5NF0sIFstNjYuNTg4NDk4MTQ2MjU5NSwgNDUuOTEzNTIwNzMwNjU0OV0sIFstNjYuNTg4NjM1NTMxNjMwNiwgNDUuOTEzNzIyNzg5NjE4Nl0sIFstNjYuNTg4NDgyODE4MDMyMywgNDUuOTEzNTE2NTQxMDI1Ml0sIFstNjYuNTg4NDk4MTQ2MjU5NSwgNDUuOTEzNTIwNzMwNjU0OV0sIFstNjYuNTg3OTI1ODYyNTU2MSwgNDUuOTEyNjc5MDM4ODYxM10sIFstNjYuNTg3MjUyMTI2MDkzLCA0NS45MTEzMjI3NTg1NTE5XSwgWy02Ni41ODY4MTE5NTE2MDM4LCA0NS45MDk5MTY0NDIxMjU3XSwgWy02Ni41ODY2MjMzMDUzOTQyLCA0NS45MDg0ODUwODc5Mjk5XSwgWy02Ni41ODIzMjkzNTgzMzYxLCA0NS45MDQ4NDcxNTcwMDU5XSwgWy02Ni41ODAzODAwMTQxNjk1LCA0NS45MDI5MjgwODM2NDddLCBbLTY2LjU3ODEyNTI0MjgwNjQsIDQ1LjkwMDQ0MDA2NTY5MDRdLCBbLTY2LjU3NzY2NzEwMjAxMTUsIDQ1LjkwMDIwMjUxMDQwNjRdLCBbLTY2LjU3NjMyODYxMjIzODEsIDQ1Ljg5OTcwODY0MjIyMV0sIFstNjYuNTc1NzQ0NzA3MzAzNSwgNDUuODk5NjQ2MTI2OTQ3Nl0sIFstNjYuNTc0NjMwNzk2MzUxMiwgNDUuODk5ODk2MTg3NjE4OV0sIFstNjYuNTczNzY4NDEzNjc4NCwgNDUuOTAwMjgzNzc5NDMzN10sIFstNjYuNTczNDAwMTA0NDExOSwgNDUuOTAwMjk2MjgyMzUwNV0sIFstNjYuNTczMDQ5NzYxNDUxMSwgNDUuODk5NjAyMzY2MjE0NF0sIFstNjYuNTcyNjkwNDM1MzM3NSwgNDUuODk5MjY0NzgyMjU1N10sIFstNjYuNTcxOTcxNzgzMTEwMiwgNDUuODk4OTk1OTYzOTMxOF0sIFstNjYuNTcxMTQ1MzMzMDQ4OCwgNDUuODk4OTA4NDQxNDA1OV0sIFstNjYuNTY5Nzk3ODYwMTIyNiwgNDUuODk4ODk1OTM4MTc2N10sIFstNjYuNTY4NzY0Nzk3NTQ1OSwgNDUuODk5NDA4NTY4MjY2OF0sIFstNjYuNTY4NjY1OTgyODY0NiwgNDUuODk5MzUyMzA0MjE5OF0sIFstNjYuNTY4NzE5ODgxNzgxNiwgNDUuODk4ODA4NDE1NDkzMl0sIFstNjYuNTY4NDIzNDM3NzM3OSwgNDUuODk4NTU4MzQ5OTIzXSwgWy02Ni41Njc1ODgwMDQ1MjM3LCA0NS44OTgzODk1NTUwMjY1XSwgWy02Ni41NjY1NTQ5NDE5NDY5LCA0NS44OTg3NzcxNTczNTg1XSwgWy02Ni41NjYwNTE4ODUzODc4LCA0NS44OTgwNzA3MTg4MjE5XSwgWy02Ni41NjQ1OTY2MTQ2Mjc1LCA0NS44OTc2MjA1OTQwMDQ3XSwgWy02Ni41NjM5MDQ5MTE4NTg4LCA0NS44OTc2NDU2MDEwMzQ3XSwgWy02Ni41NjMwOTY0MjgxMDMxLCA0NS44OTc5NDU2ODQ1MTY1XSwgWy02Ni41NjI0Njc2MDc0MDQyLCA0NS44OTgzNzA4MDAwMDYzXSwgWy02Ni41NjE2MDUyMjQ3MzE0LCA0NS44OTg1NTgzNDk5MjNdLCBbLTY2LjU2MTA0ODI2OTI1NTMsIDQ1Ljg5ODU1MjA5ODI2OTNdLCBbLTY2LjU2MDM5MjQ5OTA5NzksIDQ1Ljg5Nzk4OTQ0NjU1NTRdLCBbLTY2LjU1OTM2ODQxOTY3NCwgNDUuODk3NjY0MzU2Mjk5OF0sIFstNjYuNTU5MTQzODQwODUyOSwgNDUuODk3NDk1NTU4Njg1N10sIFstNjYuNTU4NjIyODE3OTg4MiwgNDUuODk3NDI2Nzg5MTQwMl0sIFstNjYuNTU4MTE5NzYxNDI5LCA0NS44OTcwNzY2ODgzMTU1XSwgWy02Ni41NTgyNjM0OTE4NzQ1LCA0NS44OTY1ODkwNDQyMDI3XSwgWy02Ni41NTgwMDI5ODA0NDIxLCA0NS44OTY2NTE1NjI5MTgxXSwgWy02Ni41NTc4NjgyMzMxNDk1LCA0NS44OTY1ODI3OTIzMjczXSwgWy02Ni41NTgzNTMzMjM0MDI5LCA0NS44OTY0MjY0OTUyMTM1XSwgWy02Ni41NTc5NDAwOTgzNzIyLCA0NS44OTU4ODg4Mjk3ODI0XSwgWy02Ni41NTgxMTA3NzgyNzYyLCA0NS44OTU1MzI0NjcyNjc2XSwgWy02Ni41NTc0OTA5NDA3MzAyLCA0NS44OTYwMzg4NzY0NzI5XSwgWy02Ni41NTYzMDUxNjQ1NTUxLCA0NS44OTYyNDUxOTAwMTAzXSwgWy02Ni41NTYxODgzODM1NjgyLCA0NS44OTY0MjY0OTUyMTM1XSwgWy02Ni41NTYyNjkyMzE5NDM4LCA0NS44OTY4NTE2MjIzMzQxXSwgWy02Ni41NTY0Mzk5MTE4NDc3LCA0NS44OTcyMTQyMjgxODg1XSwgWy02Ni41NTY4MzUxNzA1NzI4LCA0NS44OTc0ODkzMDY5MTIzXSwgWy02Ni41NTY3MDk0MDY0MzMsIDQ1Ljg5NzYyNjg0NTc2MzJdLCBbLTY2LjU1NjA3MTYwMjU4MTMsIDQ1Ljg5Nzc4MzEzOTQ5ODVdLCBbLTY2LjU1NTEyODM3MTUzMjksIDQ1Ljg5NzE0NTQ1ODI5NDZdLCBbLTY2LjU1NDU4MDM5OTIwOTYsIDQ1Ljg5NjI1MTQ0MTkyMzhdLCBbLTY2LjU1NDIwMzEwNjc5MDMsIDQ1Ljg5NjIyMDE4MjM0OTddLCBbLTY2LjU1MzM2NzY3MzU3NiwgNDUuODk2NDU3NzU0NjcxNV0sIFstNjYuNTUyOTU0NDQ4NTQ1NCwgNDUuODk2MzQ1MjIwNTQwNV0sIFstNjYuNTUyODQ2NjUwNzExMywgNDUuODk2MDg4ODkxOTQ2M10sIFstNjYuNTUzMTg4MDEwNTE5MiwgNDUuODk1NDEzNjc5MjU0NF0sIFstNjYuNTUzMDk4MTc4OTkwOCwgNDUuODk1MDY5ODE3Nzg0XSwgWy02Ni41NTI0ODczMjQ1OTc2LCA0NS44OTUwNTEwNjE2NDI2XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiA0NywgIk5laWdoYm91cmgiOiAiTGluY29sbiIsICJPQkpFQ1RJRCI6IDQ3LCAiU2hhcGVfQXJlYSI6IDI5OTExNDguODAxNzYsICJTaGFwZV9MZW5nIjogMTYyNjIuMTIzMjM5LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjY2ODYzMDUwNzY4MTQsIDQ1Ljk2MDc1ODY4MjI3MTldLCBbLTY2LjY2OTU0Njc4OTI3MTIsIDQ1Ljk2MTYzOTE3MDQ0MTldLCBbLTY2LjY3MTQ1MTIxNzY3MzYsIDQ1Ljk2MTIzOTUxNzk3MTNdLCBbLTY2LjY3Mjc4OTcwNzQ0NjksIDQ1Ljk2MTE4OTU2MTIwOThdLCBbLTY2LjY3Mzg4NTY1MjA5MzUsIDQ1Ljk2MTQ4OTMwMTEwMzNdLCBbLTY2LjY3NDgxMDkxNjgzNjIsIDQ1Ljk2MjE2OTk1NDQyMjVdLCBbLTY2LjY3NTgzNDk5NjI2MDEsIDQ1Ljk2MTMyMDY5NzYxMjddLCBbLTY2LjY3NzE3MzQ4NjAzMzQsIDQ1Ljk2MDcyMTIxNDM3OTldLCBbLTY2LjY3ODQ4NTAyNjM0ODIsIDQ1Ljk2MDQ0NjQ0OTA2MzddLCBbLTY2LjY4MTIzMzg3MTExNzYsIDQ1Ljk2MDI3Nzg0MjM5OTZdLCBbLTY2LjY4MTM4NjU4NDcxNTksIDQ1Ljk1OTExNjMxNTg4M10sIFstNjYuNjgxMDcyMTc0MzY2NSwgNDUuOTU3OTY3MjU0OTQwOF0sIFstNjYuNjgwNDYxMzE5OTczMywgNDUuOTU3MDYxNzI4MTcxMl0sIFstNjYuNjc5NTk4OTM3MzAwNSwgNDUuOTU2NzkzMTg5ODAxNl0sIFstNjYuNjc3OTgxOTY5Nzg5MSwgNDUuOTU2NTY4MzY1OTc5N10sIFstNjYuNjc2MTEzNDczOTk4MSwgNDUuOTU2NzI0NDkzNzMwNl0sIFstNjYuNjcwMDU4ODI4OTgzMiwgNDUuOTU4ODU0MDMyMzMxOV0sIFstNjYuNjY5MjUwMzQ1MjI3NSwgNDUuOTU5NTU5Njk3MTU3OV0sIFstNjYuNjY4NjMwNTA3NjgxNCwgNDUuOTYwNzU4NjgyMjcxOV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogNDgsICJOZWlnaGJvdXJoIjogIkNvbG9uaWFsIGhlaWdodHMiLCAiT0JKRUNUSUQiOiA0OCwgIlNoYXBlX0FyZWEiOiAzNzY4ODUuNDg2OTU0LCAiU2hhcGVfTGVuZyI6IDI2MzQuODMxMDYxMTYsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlZDk3NiIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjk4MTIyMTk4NDU5MSwgNDUuOTYwODA4NjM5NDIyXSwgWy02Ni42OTk3MTIyMTY1MTIsIDQ1Ljk2MTE3MDgyNzQxMjZdLCBbLTY2LjcwMTA2ODY3MjU5MSwgNDUuOTYxNjM5MTcwNDQxOV0sIFstNjYuNzAxNjQzNTk0MzcyOCwgNDUuOTYxMzc2ODk4ODMzMl0sIFstNjYuNzAxMjc1Mjg1MTA2MywgNDUuOTYxMDI3MjAxNDIzN10sIFstNjYuNzAxMTMxNTU0NjYwOSwgNDUuOTYwNTE1MTQwNTIwNV0sIFstNjYuNzAxODE0Mjc0Mjc2OCwgNDUuOTU4ODQ3Nzg3NDcwNF0sIFstNjYuNzAxODQxMjIzNzM1MywgNDUuOTU3NTQyNTk1OTUzNV0sIFstNjYuNzAxMTA0NjA1MjAyMywgNDUuOTU3MDY3OTczMjM0MV0sIFstNjYuNzAwMDM1NjEwMDE0MiwgNDUuOTU2NTkzMzQ2NDQ5NF0sIFstNjYuNjk4ODQ5ODMzODM5MiwgNDUuOTU2MjY4NTk5NDY1XSwgWy02Ni42OTc5MzM1NTIyNDk0LCA0NS45NTYxNzQ5MjIwOTY1XSwgWy02Ni42OTcyNzc3ODIwOTIsIDQ1Ljk1NTg1NjQxNzg1OTRdLCBbLTY2LjY5NjU3NzA5NjE3MDQsIDQ1Ljk1NzI1NTMyNDc5MzJdLCBbLTY2LjY5NjQ2MDMxNTE4MzQsIDQ1Ljk1ODU1NDI3ODE4MTldLCBbLTY2LjY5NzA4MDE1MjcyOTUsIDQ1Ljk1OTc1OTUyOTgxMl0sIFstNjYuNjk4MTIyMTk4NDU5MSwgNDUuOTYwODA4NjM5NDIyXV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiA0OSwgIk5laWdoYm91cmgiOiAiR2FyZGVuIFBsYWNlIiwgIk9CSkVDVElEIjogNDksICJTaGFwZV9BcmVhIjogMTg4NjEwLjQ1MzA0LCAiU2hhcGVfTGVuZyI6IDE3NTIuMDAyODM5MiwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmVkOTc2IiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni43MDEwNjg2NzI1OTEsIDQ1Ljk2MTYzOTE3MDQ0MTldLCBbLTY2LjcwMjU2ODg1OTExNTUsIDQ1Ljk2MjM3NjAyMjEyN10sIFstNjYuNzAzODcxNDE2Mjc3NCwgNDUuOTYzMjg3NzA2NDEwNl0sIFstNjYuNzA1NTY5MjMyMTY0NCwgNDUuOTYzNTA2MjU4NjMyOV0sIFstNjYuNzA3MTc3MjE2NTIzLCA0NS45NjM5NTU4NDkwNjQ2XSwgWy02Ni43MDY5NzA2MDQwMDc3LCA0NS45NjMxOTQwNDA5MDg2XSwgWy02Ni43MDcxNzcyMTY1MjMsIDQ1Ljk2MjI5NDg0NDAzMTldLCBbLTY2LjcwNzkwNDg1MTkwMzEsIDQ1Ljk2MTMxNDQ1MzAyOTFdLCBbLTY2LjcwOTAxODc2Mjg1NTQsIDQ1Ljk2MDMwOTA2NTg5NDddLCBbLTY2LjcxMDk0MTE1NzU2MzUsIDQ1Ljk1OTI0NzQ1NzE5M10sIFstNjYuNzEyMDM3MTAyMjEwMSwgNDUuOTU4ODYwMjc3MTkyOF0sIFstNjYuNzEzNTEwMzM5Mjc2LCA0NS45NTg1MjkyOTg1OTYyXSwgWy02Ni43MTQxMTIyMTA1MTY0LCA0NS45NTc5NTQ3NjUwMTddLCBbLTY2LjcxNTMwNjk2OTg0NDMsIDQ1Ljk1ODA3MzQxOTE3OTFdLCBbLTY2LjcxNzM3MzA5NDk5NzgsIDQ1Ljk1MDkyMjQ5MDk2NzFdLCBbLTY2LjcwOTE2MjQ5MzMwMDksIDQ1Ljk1MDEzNTUyMDIzODhdLCBbLTY2LjcwOTM5NjA1NTI3NDgsIDQ1Ljk1MTY3ODIyMjE4MDZdLCBbLTY2LjcwOTI3OTI3NDI4NzgsIDQ1Ljk1MzIzMzM3MjE3MzRdLCBbLTY2LjcwODgwMzE2NzE4NzMsIDQ1Ljk1NDc1MTAwNjU5OTJdLCBbLTY2LjcwNzk3NjcxNzEyNTksIDQ1Ljk1NjE5OTkwMjc0MzZdLCBbLTY2LjcwNzA1MTQ1MjM4MzIsIDQ1Ljk1NzMyNDAyMDIwNjJdLCBbLTY2LjcwMzQ0MDIyNDk0MSwgNDUuOTYwODUyMzUxODkxM10sIFstNjYuNzAyNzY2NDg4NDc4LCA0NS45NjEyMTQ1Mzk1OTYyXSwgWy02Ni43MDE2NDM1OTQzNzI4LCA0NS45NjEzNzY4OTg4MzMyXSwgWy02Ni43MDEwNjg2NzI1OTEsIDQ1Ljk2MTYzOTE3MDQ0MTldXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDUwLCAiTmVpZ2hib3VyaCI6ICJGcmVkZXJpY3RvbiBTb3V0aCIsICJPQkpFQ1RJRCI6IDUwLCAiU2hhcGVfQXJlYSI6IDc1NzkzMy40NTkwOCwgIlNoYXBlX0xlbmciOiA0NTY4LjI2NjU4MTMzLCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZDhkM2MiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjY1MzMyMzIxNTI0LCA0NS45MzM1MDY1OTAzNTYzXSwgWy02Ni42NTQ1NDQ5MjQwMjY0LCA0NS45MzQxNzUwOTIwODY2XSwgWy02Ni42NTU5MDEzODAxMDU1LCA0NS45MzQ2OTk4OTE1MzcxXSwgWy02Ni42NTY3Mjc4MzAxNjY4LCA0NS45MzQ5MjQ4MDQwNjddLCBbLTY2LjY1ODA2NjMxOTk0MDIsIDQ1LjkzNTA4MDk5Mjc4NzJdLCBbLTY2LjY1OTE0NDI5ODI4MTEsIDQ1LjkzNTA5OTczNTQwNDFdLCBbLTY2LjY1OTc4MjEwMjEzMjgsIDQ1LjkzNDk0OTc5NDI5MThdLCBbLTY2LjY2MDc2MTI2NTc5MjUsIDQ1LjkzNDU4MTE4NzMzNDFdLCBbLTY2LjY2MTYxNDY2NTMxMjUsIDQ1LjkzNDA3NTEyOTcyMzVdLCBbLTY2LjY2MTM4MTEwMzMzODYsIDQ1LjkzMzYxMjgwMTQ1MDFdLCBbLTY2LjY2MDk0MDkyODg0OTQsIDQ1LjkzMzIzMTY5MDExMDRdLCBbLTY2LjY1NzU2MzI2MzM4MTEsIDQ1LjkzMTYwNzI1MTc1MDRdLCBbLTY2LjY1NjI4NzY1NTY3NzYsIDQ1LjkzMTE4ODYzODc3MDRdLCBbLTY2LjY1NDM0NzI5NDY2MzksIDQ1LjkzMDg4MjQ4Njk3ODhdLCBbLTY2LjY1MjYyMjUyOTMxODQsIDQ1LjkzMDk4ODcwMzA5OF0sIFstNjYuNjUyNDE1OTE2ODAzMSwgNDUuOTMxMDMyNDM5MDg3OV0sIFstNjYuNjUyMzA4MTE4OTY5LCA0NS45MzEyNjM2MTQ0NjE4XSwgWy02Ni42NTIxOTEzMzc5ODIsIDQ1LjkzMTg2OTY2NDI0NjFdLCBbLTY2LjY1MjMxNzEwMjEyMTgsIDQ1LjkzMjQ2OTQ1OTU3NDFdLCBbLTY2LjY1Mjc3NTI0MjkxNjcsIDQ1LjkzMzEyNTQ3ODI4NjhdLCBbLTY2LjY1MzMyMzIxNTI0LCA0NS45MzM1MDY1OTAzNTYzXV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiA1MSwgIk5laWdoYm91cmgiOiAiVGhlIEh1Z2ggSm9obiBGbGVtbWluZyBGb3Jlc3RyeSBDZW50ZXIiLCAiT0JKRUNUSUQiOiA1MSwgIlNoYXBlX0FyZWEiOiAyMjA3MTguOTcwODgsICJTaGFwZV9MZW5nIjogMTg3My44NDcwMzA3NSwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmZmZmIyIiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni42NjE2MDU2ODIxNTk2LCA0NS45MzQwMzc2NDM3OTA4XSwgWy02Ni42NjE5MjkwNzU2NjE5LCA0NS45MzQxODEzMzk3MjgzXSwgWy02Ni42NjMxMjM4MzQ5ODk4LCA0NS45MzI3ODgwOTgyMDM3XSwgWy02Ni42NjMxODY3MTcwNTk3LCA0NS45MzI0NzU3MDc0MDhdLCBbLTY2LjY2MjkxNzIyMjQ3NDQsIDQ1LjkzMjI3NTc3NjM3NTJdLCBbLTY2LjY1OTk3OTczMTQ5NTQsIDQ1LjkzMDkzODcxOTA2NzJdLCBbLTY2LjY1NTc3NTYxNTk2NTcsIDQ1LjkyOTI3MDQ3NjIwMTddLCBbLTY2LjY1NTAxMjA0Nzk3NDIsIDQ1LjkyOTE0NTUxMjE2OTNdLCBbLTY2LjY1NDA1MDg1MDYyMDIsIDQ1LjkyOTE1ODAwODU4NTJdLCBbLTY2LjY1MzExNjYwMjcyNDcsIDQ1LjkyOTMzOTIwNjI5OTZdLCBbLTY2LjY1MjQ0Mjg2NjI2MTYsIDQ1LjkyOTYwMTYyOTUyNjFdLCBbLTY2LjY1MjA1NjU5MDY4OTQsIDQ1LjkzMDQ2Mzg2ODUyODZdLCBbLTY2LjY1MjI3MjE4NjM1NzYsIDQ1LjkzMTM1NzMzMzkzMzVdLCBbLTY2LjY1MjQxNTkxNjgwMzEsIDQ1LjkzMTAzMjQzOTA4NzldLCBbLTY2LjY1MzkwNzEyMDE3NDcsIDQ1LjkzMDg2OTk5MDk1MTRdLCBbLTY2LjY1NDk4NTA5ODUxNTcsIDQ1LjkzMDk0NDk2NzA3MzVdLCBbLTY2LjY1NjcyNzgzMDE2NjgsIDQ1LjkzMTMwMTEwMjI2OTVdLCBbLTY2LjY2MDkzMTk0NTY5NjUsIDQ1LjkzMzIyNTQ0MjM2MTddLCBbLTY2LjY2MTM3MjEyMDE4NTcsIDQ1LjkzMzU5NDA1ODMzMDddLCBbLTY2LjY2MTYwNTY4MjE1OTYsIDQ1LjkzNDAzNzY0Mzc5MDhdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDUyLCAiTmVpZ2hib3VyaCI6ICJLbm93bGVkZ2UgUGFyayIsICJPQkpFQ1RJRCI6IDUyLCAiU2hhcGVfQXJlYSI6IDE2MTkxNS41NDI0MDUsICJTaGFwZV9MZW5nIjogMjI3OC41NTA5NTgyMiwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmZmZmIyIiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni43MjMwODYzODAyMDQ3LCA0NS45Nzc5MTAwNzA5MDUyXSwgWy02Ni43MjAxMTI5NTY2MTQzLCA0NS45Nzc3NjAyNDU1ODU4XSwgWy02Ni43MTcyNjUyOTcxNjM3LCA0NS45ODE1NTU2OTUzOTU1XSwgWy02Ni43MTcxOTM0MzE5NDA5LCA0NS45ODIwMzAxMDgzMjg1XSwgWy02Ni43MTczMTAyMTI5Mjc5LCA0NS45ODI0MDQ2NDE5ODMxXSwgWy02Ni43MTc5NzQ5NjYyMzgxLCA0NS45ODMwMDM4OTA1NjAzXSwgWy02Ni43MTg3MjA1Njc5MjM5LCA0NS45ODMyMzQ4NDkyMTc3XSwgWy02Ni43MTk0MDMyODc1Mzk5LCA0NS45ODMyNDEwOTEzMzAyXSwgWy02Ni43MjAwNTAwNzQ1NDQ0LCA0NS45ODMwNzg3OTYxNzY0XSwgWy02Ni43MjA2NTE5NDU3ODQ4LCA0NS45ODI2OTE3ODI3MzU3XSwgWy02Ni43MjQ0NTE4MTk0MzY2LCA0NS45Nzc5Nzg3NDA3MDc4XSwgWy02Ni43MjMwODYzODAyMDQ3LCA0NS45Nzc5MTAwNzA5MDUyXV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiA1MywgIk5laWdoYm91cmgiOiAiRGlhbW9uZCBTdHJlZXQiLCAiT0JKRUNUSUQiOiA1MywgIlNoYXBlX0FyZWEiOiAxODk3MTAuNjE2MjY3LCAiU2hhcGVfTGVuZyI6IDE4MzAuMTM3MjM3MTIsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlZDk3NiIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNzEyMTQ0OTAwMDQ0MiwgNDUuOTc3OTEwMDcwOTA1Ml0sIFstNjYuNzEyMTg5ODE1ODA4NCwgNDUuOTc3MjY3MDY3NzEyNF0sIFstNjYuNzExODMwNDg5Njk0NywgNDUuOTc2NTYxNjI4NDM1OF0sIFstNjYuNzExMDQ4OTU1Mzk3NiwgNDUuOTc2MzExOTEzMjYzOV0sIFstNjYuNzEwMDI0ODc1OTczNywgNDUuOTc2MjMwNzU1NTkwNl0sIFstNjYuNzA5MDI3NzQ2MDA4MywgNDUuOTc2MzkzMDcwODE4M10sIFstNjYuNzA4MzA5MDkzNzgxLCA0NS45NzY3MzAxODU1NDAyXSwgWy02Ni43MDc2MjYzNzQxNjUxLCA0NS45Nzc0NDE4NjU0MzU4XSwgWy02Ni43MDczNTY4Nzk1Nzk4LCA0NS45NzgxNTk3Nzg4NzAyXSwgWy02Ni43MTIxNDQ5MDAwNDQyLCA0NS45Nzc5MTAwNzA5MDUyXV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiA1NCwgIk5laWdoYm91cmgiOiAiR3Jhc3NlIENpcmNsZSIsICJPQkpFQ1RJRCI6IDU0LCAiU2hhcGVfQXJlYSI6IDYwOTMyLjA1OTQ3MTksICJTaGFwZV9MZW5nIjogMTAwMS4yNzE2MDk0MywgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmZmZmIyIiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni42NTQxNDk2NjUzMDE0LCA0Ni4wMDIwNTc4NjA2NDUxXSwgWy02Ni42NTU0MjUyNzMwMDQ5LCA0Ni4wMDI0MTM1Mzg5NDQ0XSwgWy02Ni42NTY3OTA3MTIyMzY3LCA0Ni4wMDI0Mzg0OTg3MzkyXSwgWy02Ni42NTgwOTMyNjkzOTg3LCA0Ni4wMDIxMzI3NDA0NzcxXSwgWy02Ni42NTkyNzkwNDU1NzM3LCA0Ni4wMDE0Mjc2MTgwNDMyXSwgWy02Ni42NTk1MDM2MjQzOTQ4LCA0Ni4wMDEyMDI5NzUzODAzXSwgWy02Ni42NTk3MTAyMzY5MTAxLCA0NS45OTk2Njc4OTI3NzJdLCBbLTY2LjY2MDE3NzM2MDg1NzksIDQ1Ljk5Nzg1ODE4Nzg0NDZdLCBbLTY2LjY2MTI0NjM1NjA0NiwgNDUuOTk1MzkzMTQ5NzEyNF0sIFstNjYuNjU4ODU2ODM3MzkwMiwgNDUuOTk0MTc2MTkxNjY4MV0sIFstNjYuNjU2MjE1NzkwNDU0OSwgNDUuOTkzMjQwMDUxODg0OV0sIFstNjYuNjUzMzg2MDk3MzA5OSwgNDUuOTkyNjE1OTQ5ODk4N10sIFstNjYuNjUwMDI2Mzk4MTQ3MywgNDUuOTkyMzAzODk2MjY2NF0sIFstNjYuNjQ1NzUwNDE3Mzk0OSwgNDUuOTk3MjAyOTM1MjU4OF0sIFstNjYuNjQ5Njg1MDM4MzM5NCwgNDUuOTk4OTAwMzM1NDk2NV0sIFstNjYuNjUxMTk0MjA4MDE2NywgNDUuOTk5NjgwMzczMjkwMl0sIFstNjYuNjUyODAyMTkyMzc1MiwgNDYuMDAwNzkxMTI4MTI5M10sIFstNjYuNjU0MTQ5NjY1MzAxNCwgNDYuMDAyMDU3ODYwNjQ1MV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogNTUsICJOZWlnaGJvdXJoIjogIkJyb29rc2lkZSBFc3RhdGVzIiwgIk9CSkVDVElEIjogNTUsICJTaGFwZV9BcmVhIjogODQ0OTE0LjIxNjE2OCwgIlNoYXBlX0xlbmciOiAzNTc5LjU2NTQ2NDc1LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjY1ODk1NTY1MjA3MTUsIDQ1Ljk4NDM1ODQxODEzMDNdLCBbLTY2LjY1ODU2OTM3NjQ5OTMsIDQ1Ljk4NDM4MzM4NjA2OTRdLCBbLTY2LjY1Njk3OTM1ODQ0NjQsIDQ1Ljk4NjI4NzE1ODI1NzldLCBbLTY2LjY1NjA0NTExMDU1MDksIDQ1Ljk4ODA5NzI0MTU4NTldLCBbLTY2LjY1NTU5NTk1MjkwODksIDQ1Ljk4OTcxMzc4MzIxMTFdLCBbLTY2LjY1NTI2MzU3NjI1MzcsIDQ1Ljk4OTc2MzcxNDI0NzFdLCBbLTY2LjY1OTEzNTMxNTEyODMsIDQ1Ljk4OTM4OTIzMDM3OTJdLCBbLTY2LjY2NTE5ODk0MzI5NjEsIDQ1Ljk4OTYyNjQwMzc4OTddLCBbLTY2LjY2NjEyNDIwODAzODcsIDQ1Ljk5MjI5NzY1NTE3NThdLCBbLTY2LjY2NjM3NTczNjMxODMsIDQ1Ljk5MjY2NTg3ODMxNjZdLCBbLTY2LjY2Njg2OTgwOTcyNDUsIDQ1Ljk5MzA0MDM0MDAxNTFdLCBbLTY2LjY2ODcxMTM1NjA1NywgNDUuOTkyNjU5NjM3MjY2OF0sIFstNjYuNjcwNjg3NjQ5NjgyMSwgNDUuOTkxOTEwNzA2MTg0Nl0sIFstNjYuNjcyMTYwODg2NzQ4LCA0NS45OTEwNDk0MjI5MTExXSwgWy02Ni42NzM1NDQyOTIyODU2LCA0NS45ODk4MTk4ODY2MDg4XSwgWy02Ni42NzM4MDQ4MDM3MTgsIDQ1Ljk4OTEwODM2NTgxNTZdLCBbLTY2LjY3Mzc4NjgzNzQxMjMsIDQ1Ljk4ODIyODMxNDI4NzNdLCBbLTY2LjY3MzcwNTk4OTAzNjcsIDQ1Ljk4Nzk0MTIwMjI1MV0sIFstNjYuNjczMDY4MTg1MTg1LCA0NS45ODc1MjMwMTQ2NjQ0XSwgWy02Ni42NzMyMDI5MzI0Nzc2LCA0NS45ODcyMDQ2OTA2NTI1XSwgWy02Ni42NzM2NzkwMzk1NzgyLCA0NS45ODY4MzY0MzExNzgzXSwgWy02Ni42NzM3Njg4NzExMDY2LCA0NS45ODY2MzA0NTQ0NzE4XSwgWy02Ni42NzM1MTczNDI4MjcsIDQ1Ljk4NjIzMDk4MjMxMTFdLCBbLTY2LjY3MzA1OTIwMjAzMjEsIDQ1Ljk4NTg2ODk1ODE3NTRdLCBbLTY2LjY3MjczNTgwODUyOTksIDQ1Ljk4NTg0Mzk5MDkwNjRdLCBbLTY2LjY3MTUxNDA5OTc0MzQsIDQ1Ljk4NjI1NTk0OTQwNTZdLCBbLTY2LjY2OTUzNzgwNjExODQsIDQ1Ljk4NjY0MjkzNzkzMDRdLCBbLTY2LjY2OTA0MzczMjcxMjEsIDQ1Ljk4NjM4MDc4NDcwOTJdLCBbLTY2LjY2ODA5MTUxODUxMDksIDQ1Ljk4NTIwNzMyMTc0MV0sIFstNjYuNjY3NDk4NjMwNDIzNCwgNDUuOTg1MDgyNDgzNzkxMV0sIFstNjYuNjY2NTM3NDMzMDY5NCwgNDUuOTg1NDE5NTQ1NjA5N10sIFstNjYuNjY1OTM1NTYxODI5MSwgNDUuOTg1NDM4MjcxMjA2MV0sIFstNjYuNjY1NTY3MjUyNTYyNiwgNDUuOTg1MjYzNDk4NzI2Nl0sIFstNjYuNjY1MjQzODU5MDYwMywgNDUuOTg0NzM5MTc3OTc3NF0sIFstNjYuNjY0NTYxMTM5NDQ0NCwgNDUuOTg0MjY0Nzg4MjU4NV0sIFstNjYuNjYzOTk1MjAwODE1NCwgNDUuOTg0NDc3MDE1NzQwNV0sIFstNjYuNjY0MjI4NzYyNzg5MiwgNDUuOTg0ODc2NTAwNTU4NF0sIFstNjYuNjY0MzM2NTYwNjIzMywgNDUuOTg1NjMxNzY4NjY0OF0sIFstNjYuNjYzMDk2ODg1NTMxMiwgNDUuOTg1NzQ0MTIxNzE3Nl0sIFstNjYuNjYxODMwMjYwOTgwNiwgNDUuOTg1NTMxODk5MDkzMl0sIFstNjYuNjU4OTU1NjUyMDcxNSwgNDUuOTg0MzU4NDE4MTMwM11dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogNTYsICJOZWlnaGJvdXJoIjogIldpbGxpYW1zIC8gSGF3a2lucyBBcmVhIiwgIk9CSkVDVElEIjogNTYsICJTaGFwZV9BcmVhIjogNzY1NTYxLjg3NTM4NiwgIlNoYXBlX0xlbmciOiA0NTExLjgwNTA3NjI4LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjY2MDM1NzAyMzkxNDcsIDQ1Ljk4OTQwNzk1NDYzMjhdLCBbLTY2LjY1ODgyOTg4NzkzMTcsIDQ1Ljk4OTQwMTcxMzIxNTZdLCBbLTY2LjY1Njk3MDM3NTI5MzYsIDQ1Ljk4OTU1MTUwNzAzMzFdLCBbLTY2LjY1MTc2OTEyOTc5ODUsIDQ1Ljk5MDM1NjY0MTg1NjNdLCBbLTY2LjY1MDAyNjM5ODE0NzMsIDQ1Ljk5MjMwMzg5NjI2NjRdLCBbLTY2LjY1MzAwODgwNDg5MDYsIDQ1Ljk5MjU1OTc4MDM3NDhdLCBbLTY2LjY1NTQ3OTE3MTkyMTksIDQ1Ljk5MzA0NjU4MTAyMTldLCBbLTY2LjY1NzgzMjc1Nzk2NjMsIDQ1Ljk5Mzc3MDUzMzAzOTZdLCBbLTY2LjY2MDAyNDY0NzI1OTYsIDQ1Ljk5NDcxMjkwNDY2ODNdLCBbLTY2LjY2MDYyNjUxODQ5OTksIDQ1Ljk5MzQzOTc2MzAzNDFdLCBbLTY2LjY2MDY2MjQ1MTExMTMsIDQ1Ljk5Mjk5MDQxMTkzNV0sIFstNjYuNjYwMzU3MDIzOTE0NywgNDUuOTg5NDA3OTU0NjMyOF1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogNTcsICJOZWlnaGJvdXJoIjogIk1jS25pZ2h0IiwgIk9CSkVDVElEIjogNTcsICJTaGFwZV9BcmVhIjogMjg3OTU2LjI4MTQ3OCwgIlNoYXBlX0xlbmciOiAyMzYwLjg0Nzc2NjYxLCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjY2MDAyNDY0NzI1OTYsIDQ1Ljk5NDcxMjkwNDY2ODNdLCBbLTY2LjY2MTI0NjM1NjA0NiwgNDUuOTk1MzkzMTQ5NzEyNF0sIFstNjYuNjYyNDU5MDgxNjc5NSwgNDUuOTk0NjU2NzM3MjcyNl0sIFstNjYuNjY0MTExOTgxODAyMywgNDUuOTkzODY0MTQ2ODMzMV0sIFstNjYuNjY1ODkwNjQ2MDY0OSwgNDUuOTkzMjIxMzI4OTI3N10sIFstNjYuNjY2ODY5ODA5NzI0NSwgNDUuOTkzMDQwMzQwMDE1MV0sIFstNjYuNjY2Mzc1NzM2MzE4MywgNDUuOTkyNjY1ODc4MzE2Nl0sIFstNjYuNjY2MTI0MjA4MDM4NywgNDUuOTkyMjk3NjU1MTc1OF0sIFstNjYuNjY1MTk4OTQzMjk2MSwgNDUuOTg5NjI2NDAzNzg5N10sIFstNjYuNjYwMzU3MDIzOTE0NywgNDUuOTg5NDA3OTU0NjMyOF0sIFstNjYuNjYwNjYyNDUxMTExMywgNDUuOTkyOTkwNDExOTM1XSwgWy02Ni42NjA2MjY1MTg0OTk5LCA0NS45OTM0Mzk3NjMwMzQxXSwgWy02Ni42NjAwMjQ2NDcyNTk2LCA0NS45OTQ3MTI5MDQ2NjgzXV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiA1OCwgIk5laWdoYm91cmgiOiAiU2hhZG93b29kIEVzdGF0ZXMiLCAiT0JKRUNUSUQiOiA1OCwgIlNoYXBlX0FyZWEiOiAyMjEzMDkuNDY3NzU3LCAiU2hhcGVfTGVuZyI6IDIwMTkuNzYwNTAwMzIsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlZDk3NiIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjMxODcxNDQ2MjU1MiwgNDUuOTg4MTUzNDE1NjM4OF0sIFstNjYuNjMzNDQzNDk4MDAyNSwgNDUuOTg4MDcyMjc1MzIxOV0sIFstNjYuNjM0NzczMDA0NjIzLCA0NS45ODgyNzgyNDY2NjMzXSwgWy02Ni42MzU5NzY3NDcxMDM3LCA0NS45ODg3MDg5MTE1MzY5XSwgWy02Ni42MzcxODk0NzI3MzcyLCA0NS45ODk0MjY2Nzg4OF0sIFstNjYuNjM1OTU4NzgwNzk4LCA0NS45ODgxNjU4OTg3NTM5XSwgWy02Ni42MzUyOTQwMjc0ODc3LCA0NS45ODY3NjE1MzA2NDY0XSwgWy02Ni42MzUwNTE0ODIzNjEsIDQ1Ljk4MjQyMzM2ODU5OTNdLCBbLTY2LjYzNTIwNDE5NTk1OTMsIDQ1Ljk4MTExODczMjUxODddLCBbLTY2LjYzNTgxNTA1MDM1MjUsIDQ1Ljk3OTU1MTg4MDEzNl0sIFstNjYuNjM2ODEyMTgwMzE3OSwgNDUuOTc4MDk3MzUxOTg0NV0sIFstNjYuNjM3ODAwMzI3MTMwNCwgNDUuOTc3MDExMTEyOTA3NV0sIFstNjYuNjM4MTIzNzIwNjMyNywgNDUuOTc2OTExMjI3Nzg0Nl0sIFstNjYuNjM4NTk5ODI3NzMzMywgNDUuOTc2OTczNjU2MDA3NV0sIFstNjYuNjM3ODk5MTQxODExNywgNDUuOTc2NzU1MTU2OTE5NV0sIFstNjYuNjQwMjE2Nzk1MjQ0NywgNDUuOTczNTA4NzgzMTk1Ml0sIFstNjYuNjQxNDU2NDcwMzM2OCwgNDUuOTcxMDMwMTczNjA3XSwgWy02Ni42Mzc2NjU1Nzk4Mzc4LCA0NS45Njk5NzUwMTM5NDk5XSwgWy02Ni42MzUxNzcyNDY1MDA4LCA0NS45Njg5OTQ3NTg4NjA4XSwgWy02Ni42MzQ5MDc3NTE5MTU2LCA0NS45NjkwMTk3MzM3MjgxXSwgWy02Ni42MzMzODk1OTkwODU0LCA0NS45NzAyNDM0ODg0MzJdLCBbLTY2LjYzMjMzODU3MDIwMywgNDUuOTcxNTQyMTM3MzIyXSwgWy02Ni42MzM4OTI2NTU2NDQ1LCA0NS45NzE5NDE3MTU0Njk4XSwgWy02Ni42MzQwNjMzMzU1NDg1LCA0NS45NzI3OTcwNTI3NTIyXSwgWy02Ni42MjM4MzE1MjQ0NjI0LCA0NS45ODUyMDczMjE3NDFdLCBbLTY2LjYyNTc4OTg1MTc4MTgsIDQ1Ljk4NTY4MTcwMzM4MzFdLCBbLTY2LjYyNzI5MDAzODMwNjIsIDQ1Ljk4NjE2ODU2NDUyNTZdLCBbLTY2LjYyOTQ5OTg5MzkwNTIsIDQ1Ljk4NzUxNjc3MzAzNDddLCBbLTY2LjYzMDY0MDc1NDMxNiwgNDUuOTg3OTE2MjM1OTE2Nl0sIFstNjYuNjMxODcxNDQ2MjU1MiwgNDUuOTg4MTUzNDE1NjM4OF1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogNTksICJOZWlnaGJvdXJoIjogIk5vcnRoIERldm9uIiwgIk9CSkVDVElEIjogNTksICJTaGFwZV9BcmVhIjogMTIzNzk1Ni44MTg4NiwgIlNoYXBlX0xlbmciOiA2MTg5LjY4NjI2MzUyLCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZDhkM2MiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjYyMDUxNjc0MTA2NCwgNDUuOTcwNTE4MjA1MTU5Nl0sIFstNjYuNjE4NjkzMTYxMDM3MiwgNDUuOTcxOTQxNzE1NDY5OF0sIFstNjYuNjE3MTU3MDQxOTAxNCwgNDUuOTcyODI4MjY5MTkxNV0sIFstNjYuNjE1NDIzMjkzNDAzLCA0NS45NzM1MDg3ODMxOTUyXSwgWy02Ni42MTM1MzY4MzEzMDY0LCA0NS45NzM5NTgyOTI0NDY1XSwgWy02Ni42MTI5ODg4NTg5ODMxLCA0NS45NzQ4MDczNTU1MjJdLCBbLTY2LjYxMjEwODUxMDAwNDYsIDQ1Ljk3NTM0NDI1NjMzNjZdLCBbLTY2LjYxMDgyMzkxOTE0ODMsIDQ1Ljk3NTU5Mzk3NTg3MjFdLCBbLTY2LjYwNzY5Nzc4MTk1OTYsIDQ1Ljk3NTQ1MDM4NzI3NjddLCBbLTY2LjYwNjY2NDcxOTM4MjksIDQ1Ljk3NjEzNzExMTk3MzZdLCBbLTY2LjYwNTgyOTI4NjE2ODYsIDQ1Ljk3NjkzNjE5OTA4MjJdLCBbLTY2LjYwNTIwMDQ2NTQ2OTgsIDQ1Ljk3NzgyODkxNTU3NDJdLCBbLTY2LjYwNDg3NzA3MTk2NzUsIDQ1Ljk3ODU4NDI3OTgyNjJdLCBbLTY2LjYwNDY3OTQ0MjYwNDksIDQ1Ljk3OTc3MDM2ODE4ODRdLCBbLTY2LjYwNjU5Mjg1NDE2MDEsIDQ1Ljk4MDYxMzA5OTc0MjldLCBbLTY2LjYwODAwMzIwOTE1NjIsIDQ1Ljk4MTU0OTQ1MzA5M10sIFstNjYuNjA4Nzc1NzYwMzAwNSwgNDUuOTgyMzA0NzY2NTg5Nl0sIFstNjYuNjA5NTkzMjI3MjA5MSwgNDUuOTgzNzA5MjQ3NzYyMl0sIFstNjYuNjEwMTIzMjMzMjI2NywgNDUuOTg1NDQ0NTEzMDcwMl0sIFstNjYuNjEwMjkzOTEzMTMwNywgNDUuOTg3Nzk3NjQ1Njc0NF0sIFstNjYuNjEwMDk2MjgzNzY4MiwgNDUuOTg4NjA5MDQ3NTE2OF0sIFstNjYuNjA5NTc1MjYwOTAzNCwgNDUuOTg5MjE0NDcwMzczOF0sIFstNjYuNjExOTM3ODMwMTAwNiwgNDUuOTkwMjk0MjI4NzIyOV0sIFstNjYuNjE0MTM4NzAyNTQ2NywgNDUuOTkwOTkzMjUxNzk3Ml0sIFstNjYuNjIxNzkyMzQ4NzY3NCwgNDUuOTgxODkyNzc4Njg3XSwgWy02Ni42MjkzMTEyNDc2OTU1LCA0NS45NzQyMjA1MDQ0OTE1XSwgWy02Ni42MjkzNDcxODAzMDY5LCA0NS45NzQwMDE5OTQ1NDAyXSwgWy02Ni42Mjg2Mzc1MTEyMzI0LCA0NS45NzM5MDgzNDcxNTQzXSwgWy02Ni42MjY3NjkwMTU0NDE1LCA0NS45NzMwMjE4MTA3MjI0XSwgWy02Ni42MjU4MDc4MTgwODc1LCA0NS45NzI5MjgxNjE2NzldLCBbLTY2LjYyNTIxNDkyOTk5OTksIDQ1Ljk3MjY5MDkxNjcyN10sIFstNjYuNjI0OTgxMzY4MDI2MSwgNDUuOTcyOTY1NjIxMzE1NF0sIFstNjYuNjIzNzk1NTkxODUxLCA0NS45NzI3MDk2NDY2Mjg2XSwgWy02Ni42MjA1MTY3NDEwNjQsIDQ1Ljk3MDUxODIwNTE1OTZdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDYwLCAiTmVpZ2hib3VyaCI6ICJOb3J0aCBEZXZvbiIsICJPQkpFQ1RJRCI6IDYwLCAiU2hhcGVfQXJlYSI6IDIwNDI4ODUuMzc0OTcsICJTaGFwZV9MZW5nIjogNjQ4MS4zOTQyODA2NywgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmQ4ZDNjIiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni41OTY4NTUxMTY0ODAzLCA0NS45MTQ5ODUyNjQzMDI1XSwgWy02Ni41OTU0NzE3MTA5NDI3LCA0NS45MTUyNjY1MDQ3NTExXSwgWy02Ni41OTQyMzIwMzU4NTA3LCA0NS45MTU3Nzg5ODM2ODEzXSwgWy02Ni41OTMyMDc5NTY0MjY4LCA0NS45MTY0OTE0NDY1MjU4XSwgWy02Ni41OTI1NzkxMzU3Mjc5LCA0NS45MTcyMDM5MDAyMjI5XSwgWy02Ni41OTQzMzA4NTA1MzE5LCA0NS45MTg1Mjg3ODk3OTM1XSwgWy02Ni41OTk0NTEyNDc2NTE0LCA0NS45MjE1OTA5MTM1MDAzXSwgWy02Ni42MDA3NzE3NzExMTksIDQ1LjkyMDkwMzUxMjY4NDddLCBbLTY2LjYwMjE0NjE5MzUwMzcsIDQ1LjkxOTkxNjE0MDI0NzhdLCBbLTY2LjYwMzI2MDEwNDQ1NjEsIDQ1LjkxODc3ODc2NTQxMDRdLCBbLTY2LjYwNDA3NzU3MTM2NDYsIDQ1LjkxNzUyMjYyNjU0N10sIFstNjYuNTk2ODU1MTE2NDgwMywgNDUuOTE0OTg1MjY0MzAyNV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogNjEsICJOZWlnaGJvdXJoIjogIldlc2JldHQgLyBDYXNlIiwgIk9CSkVDVElEIjogNjEsICJTaGFwZV9BcmVhIjogMzY1OTI1LjM0MzM0LCAiU2hhcGVfTGVuZyI6IDIzNjguNTc5NzI5NzgsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZmZmZiMiIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNzA2MTQ0MTUzOTQ2MywgNDUuOTM5MDk4MDE1NTEzMl0sIFstNjYuNzA0NjA4MDM0ODEwNCwgNDUuOTM4NzkxOTA3MzgzNV0sIFstNjYuNzA0MTA0OTc4MjUxMywgNDUuOTM5MzY2NjM5NjIyNV0sIFstNjYuNzAyMjM2NDgyNDYwMywgNDUuOTQwNzcyMjA5NjcxNl0sIFstNjYuNjk5MjI3MTI2MjU4NSwgNDUuOTQ0NjEzOTE5MzM4OV0sIFstNjYuNjk5Njc2MjgzOTAwNiwgNDUuOTQ0ODUxMjg0NTM3MV0sIFstNjYuNjk5Mzk3ODA2MTYyNSwgNDUuOTQ1MDUxMTcwMjMxNV0sIFstNjYuNjk5NzY2MTE1NDI5LCA0NS45NDUyNTEwNTUyMDUyXSwgWy02Ni42OTU2MjQ4ODE5NjkyLCA0NS45NDgyNjE3MzU0MzVdLCBbLTY2LjY5NTAxNDAyNzU3NiwgNDUuOTQ5ODYwNzAyNDMxNl0sIFstNjYuNjk1NTUzMDE2NzQ2NSwgNDUuOTQ5ODYwNzAyNDMxNl0sIFstNjYuNjk1NzIzNjk2NjUwNSwgNDUuOTUwNzE2MzgwNjY1OV0sIFstNjYuNjk5ODkxODc5NTY4OCwgNDUuOTUwMzQxNjMyNzAwMV0sIFstNjYuNzAwMjYwMTg4ODM1MywgNDUuOTUwNzY2MzQ2ODY5OV0sIFstNjYuNzAxMzU2MTMzNDgxOSwgNDUuOTUwNTc4OTczMzcyN10sIFstNjYuNzA1MzUzNjM2NDk2MiwgNDUuOTUwMzg1MzUzNDI2N10sIFstNjYuNzA4NjQxNDcwNDM2MSwgNDUuOTUwMDY2ODE1OTE0OF0sIFstNjYuNzEwMjc2NDA0MjUzMiwgNDUuOTQ2ODM3NjE2NjE5Ml0sIFstNjYuNzExNzQwNjU4MTY2MywgNDUuOTQyMzAyNjc4NzU3NF0sIFstNjYuNzA4NDI1ODc0NzY3OSwgNDUuOTQxNzQ2NzE3MzIyNV0sIFstNjYuNzA5MTA4NTk0MzgzOCwgNDUuOTM5ODM1MTY2OTMxM10sIFstNjYuNzA2MTQ0MTUzOTQ2MywgNDUuOTM5MDk4MDE1NTEzMl1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogNjIsICJOZWlnaGJvdXJoIjogIlNlcmVuaXR5IExhbmUiLCAiT0JKRUNUSUQiOiA2MiwgIlNoYXBlX0FyZWEiOiAxMDQwMDA1LjkxNTk5LCAiU2hhcGVfTGVuZyI6IDQ0NTguMTQyMjI5MiwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmZmZmIyIiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni43MzE4NjI5MjA1MzA2LCA0NS45NjUyNzMzNzc3ODg3XSwgWy02Ni43MzEzNjg4NDcxMjQzLCA0NS45Njc4OTU4NTM1NTA0XSwgWy02Ni43MzU2NjI3OTQxODI0LCA0NS45Njc2NTg1ODcwNDIyXSwgWy02Ni43MzU5MzIyODg3Njc3LCA0NS45Njc3MzM1MTM0MTc3XSwgWy02Ni43MzYxMDI5Njg2NzE2LCA0NS45Njc1ODM2NjA1NjUyXSwgWy02Ni43MzcwMjgyMzM0MTQzLCA0NS45Njc1NTg2ODUwNTA0XSwgWy02Ni43NDI3Njg0NjgwNzk4LCA0NS45Njc2Mzk4NTU0MzI0XSwgWy02Ni43NDUyNjU3ODQ1Njk3LCA0NS45NjczMjc2NjEwMDQ0XSwgWy02Ni43NDU1MTczMTI4NDkyLCA0NS45NjcxNzc4MDcwNTRdLCBbLTY2Ljc0NjA4MzI1MTQ3ODIsIDQ1Ljk2NzEzNDA5OTU3NTVdLCBbLTY2Ljc0NjQ5NjQ3NjUwODksIDQ1Ljk2NzMwODkyOTI4MjhdLCBbLTY2Ljc0NjE4MjA2NjE1OTUsIDQ1Ljk2NTgyMjg1OTE4Ml0sIFstNjYuNzQ1ODk0NjA1MjY4NSwgNDUuOTY1NTIzMTQyNzM0XSwgWy02Ni43NDUzNzM1ODI0MDM4LCA0NS45NjUzMzU4MTkxMzA2XSwgWy02Ni43NDUyMTE4ODU2NTI2LCA0NS45NjUxMzYwMDY1ODg3XSwgWy02Ni43NDMzMTY0NDA0MDMxLCA0NS45NjU1MTA2NTQ1MTM1XSwgWy02Ni43NDIxMTI2OTc5MjI0LCA0NS45NjU1MTA2NTQ1MTM1XSwgWy02Ni43NDA2MjE0OTQ1NTA4LCA0NS45NjUzNjA3OTU2NDc2XSwgWy02Ni43Mzg5MDU3MTIzNTgxLCA0NS45NjQ5NzM2NTgzNjc4XSwgWy02Ni43Mzc1OTQxNzIwNDMzLCA0NS45NjQ4MjM3OTgwNDkzXSwgWy02Ni43MzU5ODYxODc2ODQ3LCA0NS45NjQ0OTI4NTUwNzY0XSwgWy02Ni43MzE3OTEwNTUzMDc5LCA0NS45NjMwNjI5MDg5Mzk3XSwgWy02Ni43MzIzMTIwNzgxNzI3LCA0NS45NjM1NDk5Njg5NzM5XSwgWy02Ni43MzI1MTg2OTA2ODgsIDQ1Ljk2NDE0MzE3NzMzNDRdLCBbLTY2LjczMjM3NDk2MDI0MjUsIDQ1Ljk2NDc0MjYyMzU0MDhdLCBbLTY2LjczMTg2MjkyMDUzMDYsIDQ1Ljk2NTI3MzM3Nzc4ODddXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDYzLCAiTmVpZ2hib3VyaCI6ICJNb250ZWl0aCAvIFRhbGlzbWFuIiwgIk9CSkVDVElEIjogNjMsICJTaGFwZV9BcmVhIjogMzQyMjk4LjIxMDU3NSwgIlNoYXBlX0xlbmciOiAzMTU5LjE2MDQ1NzI3LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2Ljc0OTU0MTc2NTMyMjEsIDQ1Ljk2NzUwODczMzk4N10sIFstNjYuNzUwOTg4MDUyOTI5NSwgNDUuOTY3OTIwODI4OTEzMl0sIFstNjYuNzUzMjk2NzIzMjA5NywgNDUuOTY4Mjk1NDU4MDAzOV0sIFstNjYuNzU1NTc4NDQ0MDMxNCwgNDUuOTY5MDE5NzMzNzI4MV0sIFstNjYuNzU1NTg3NDI3MTg0MiwgNDUuOTY0ODIzNzk4MDQ5M10sIFstNjYuNzQ5NjEzNjMwNTQ0OCwgNDUuOTY0NDgwMzY2NjIzNl0sIFstNjYuNzQ5NTQxNzY1MzIyMSwgNDUuOTY3NTA4NzMzOTg3XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiA2NCwgIk5laWdoYm91cmgiOiAiUmFpbCBTaWRlIiwgIk9CSkVDVElEIjogNjQsICJTaGFwZV9BcmVhIjogMTg0NDQ0LjU5NDM0NiwgIlNoYXBlX0xlbmciOiAxNzc2LjczNzczNTczLCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2Ljc1OTc0NjYyNjk0OTcsIDQ1Ljk1ODQzNTYyNTA0OTVdLCBbLTY2Ljc2MDAxNjEyMTUzNDksIDQ1Ljk2MzIyNTI2Mjc2MDJdLCBbLTY2Ljc1OTg1NDQyNDc4MzgsIDQ1Ljk2NTEwNDc4NTgxNF0sIFstNjYuNzY3NzQxNjMyOTc4MywgNDUuOTY1NDQxOTY5MjUwM10sIFstNjYuNzcxNTQxNTA2NjMwMiwgNDUuOTY2MDc4ODY1Njk3Ml0sIFstNjYuNzcwNTM1MzkzNTExOSwgNDUuOTU3NDQyNjc1NzE4OV0sIFstNjYuNzY1Mjk4MjE1NDA1NSwgNDUuOTU3Nzk4NjQwNzMyNV0sIFstNjYuNzY1MzA3MTk4NTU4NCwgNDUuOTU3OTExMDUwMjYxN10sIFstNjYuNzY1MDkxNjAyODkwMiwgNDUuOTU3OTIzNTQwMTk1M10sIFstNjYuNzY1MTYzNDY4MTEyOSwgNDUuOTU4NDIzMTM1MjMxM10sIFstNjYuNzY1MDY0NjUzNDMxNywgNDUuOTU4MzIzMjE2NTg0NV0sIFstNjYuNzYzNjk5MjE0MTk5OCwgNDUuOTU4NDIzMTM1MjMxM10sIFstNjYuNzYzNjA5MzgyNjcxNCwgNDUuOTU4MTEwODg4ODYxN10sIFstNjYuNzYyMDU1Mjk3MjI5OSwgNDUuOTU4MTE3MTMzODA2M10sIFstNjYuNzU5NjgzNzQ0ODc5OCwgNDUuOTU3NDA1MjA1NTg0NF0sIFstNjYuNzU5NzQ2NjI2OTQ5NywgNDUuOTU4NDM1NjI1MDQ5NV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogNjUsICJOZWlnaGJvdXJoIjogIlNpbHZlcndvb2QiLCAiT0JKRUNUSUQiOiA2NSwgIlNoYXBlX0FyZWEiOiA3Mjg1NjUuNjYyNDQ5LCAiU2hhcGVfTGVuZyI6IDM3MTAuNzUxNjMwMzMsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlZDk3NiIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjY3MDA0NTU3MDE3MiwgNDUuOTQ2MzMxNjcwODYzNV0sIFstNjYuNjc5MDk1ODgwNzQxNCwgNDUuOTQ3OTExOTU1MjU1OV0sIFstNjYuNjc5MzI5NDQyNzE1MywgNDUuOTQ3Njc0NjAzMTYzXSwgWy02Ni42NzkyNzU1NDM3OTgyLCA0NS45NDcwNjg3MjYxMDddLCBbLTY2LjY4MDU2MDEzNDY1NDUsIDQ1Ljk0NTY2MzMxNTY4NzJdLCBbLTY2LjY3MTcwMjc0NTk1MzEsIDQ1Ljk0MTg2NTQwNjE4NjddLCBbLTY2LjY3MDU4ODgzNTAwMDgsIDQ1Ljk0MTU3MTgwNjk1NDFdLCBbLTY2LjY3MDIyMDUyNTczNDMsIDQ1Ljk0MTE3MjAwOTc1NDNdLCBbLTY2LjY2OTIzMjM3ODkyMTgsIDQ1Ljk0MDg2NTkxMzA3NDddLCBbLTY2LjY1OTkxNjg0OTQyNTUsIDQ1LjkzNjYzNjYwODQzMDRdLCBbLTY2LjY1NjE3MDg3NDY5MDcsIDQ1Ljk0MDk0NzEyMjU2MjVdLCBbLTY2LjY1NzY0NDExMTc1NjcsIDQ1Ljk0MTU3MTgwNjk1NDFdLCBbLTY2LjY1NzQxOTUzMjkzNTYsIDQ1Ljk0MTkwOTEzMzU5OV0sIFstNjYuNjYyMDU0ODM5ODAxNywgNDUuOTQzNjY0NDQ4MzgyN10sIFstNjYuNjY2NTY0MzgyNTI4LCA0NS45NDU1NzU4NjY3NTAyXSwgWy02Ni42NjcwMDQ1NTcwMTcyLCA0NS45NDYzMzE2NzA4NjM1XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiA2NiwgIk5laWdoYm91cmgiOiAiUHJvc3BlY3QiLCAiT0JKRUNUSUQiOiA2NiwgIlNoYXBlX0FyZWEiOiA5NzI5MDIuODE4NTc2LCAiU2hhcGVfTGVuZyI6IDQ3ODUuNTQxMTIxMjIsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlYjI0YyIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjg5MDMxMjQ3NzgzOCwgNDUuOTQ0NDcwMjUwNDM1N10sIFstNjYuNjg5OTIwNTc5OTE1MSwgNDUuOTQ0NDk1MjM2MzU4Nl0sIFstNjYuNjkxMjE0MTUzOTI0MiwgNDUuOTQ0OTI2MjQxNzU2OV0sIFstNjYuNjkzOTQ1MDMyMzg3OSwgNDUuOTQ2NzgxNDAwNjUyMl0sIFstNjYuNzAwMTk3MzA2NzY1NCwgNDUuOTQyMjMzOTY0NzI0N10sIFstNjYuNjkzNDE1MDI2MzcwMywgNDUuOTM4NjQ4MjIzMzkzXSwgWy02Ni42ODk5NTY1MTI1MjY0LCA0NS45NDE4NDA0MTkwNzg1XSwgWy02Ni42ODkwMzEyNDc3ODM4LCA0NS45NDQ0NzAyNTA0MzU3XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiA2NywgIk5laWdoYm91cmgiOiAiTGlhbiAvIFZhbGNvcmUiLCAiT0JKRUNUSUQiOiA2NywgIlNoYXBlX0FyZWEiOiA0MTExOTcuOTU2MjQ0LCAiU2hhcGVfTGVuZyI6IDI1ODguMzUwMjUyMjcsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZlZDk3NiIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjIwNTE2NzQxMDY0LCA0NS45NzA1MTgyMDUxNTk2XSwgWy02Ni42MjM3OTU1OTE4NTEsIDQ1Ljk3MjcwOTY0NjYyODZdLCBbLTY2LjYyNDk4MTM2ODAyNjEsIDQ1Ljk3Mjk2NTYyMTMxNTRdLCBbLTY2LjYyNTIxNDkyOTk5OTksIDQ1Ljk3MjY5MDkxNjcyN10sIFstNjYuNjI1ODA3ODE4MDg3NSwgNDUuOTcyOTI4MTYxNjc5XSwgWy02Ni42MjY3NjkwMTU0NDE1LCA0NS45NzMwMjE4MTA3MjI0XSwgWy02Ni42Mjg2Mzc1MTEyMzI0LCA0NS45NzM5MDgzNDcxNTQzXSwgWy02Ni42MjkzNDcxODAzMDY5LCA0NS45NzQwMDE5OTQ1NDAyXSwgWy02Ni42Mjk1NjI3NzU5NzUxLCA0NS45NzI3MjIxMzMyMjYyXSwgWy02Ni42MzM0Nzk0MzA2MTM4LCA0NS45Njg0ODI3NzE1OTkxXSwgWy02Ni42MzI4Nzc1NTkzNzM1LCA0NS45Njc5ODk1MTExMDI5XSwgWy02Ni42MzExMTY4NjE0MTY2LCA0NS45NjcwOTAzOTIwNjI0XSwgWy02Ni42MzA1MzI5NTY0ODE5LCA0NS45NjY1MDk3MDMyNTkxXSwgWy02Ni42MzA2NTg3MjA2MjE3LCA0NS45NjYyMjg3MjI2MjA1XSwgWy02Ni42MzA1NTk5MDU5NDA0LCA0NS45NjYwNzI2MjE2NDk5XSwgWy02Ni42MjkxNTg1MzQwOTcyLCA0NS45NjUzMDQ1OTg0Njg0XSwgWy02Ni42Mjg2NzM0NDM4NDM4LCA0NS45NjQ4MzAwNDIyMzczXSwgWy02Ni42MjY3OTU5NjQ5LCA0NS45NjU2MTA1NjAxOTg4XSwgWy02Ni42MjU4NjE3MTcwMDQ1LCA0NS45NjYxNTM3OTQyMDk1XSwgWy02Ni42MjI3ODk0Nzg3MzI4LCA0NS45Njg3NzYyMjgyOTE0XSwgWy02Ni42MjA1MTY3NDEwNjQsIDQ1Ljk3MDUxODIwNTE1OTZdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDY4LCAiTmVpZ2hib3VyaCI6ICJOb3J0aCBEZXZvbiIsICJPQkpFQ1RJRCI6IDY4LCAiU2hhcGVfQXJlYSI6IDU0NzA2Ny4yNzUzNjEsICJTaGFwZV9MZW5nIjogMzAzMC41OTE3NDE1NSwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmQ4ZDNjIiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni42NzEwNjQ5NDIxMDE0LCA0NS45NTg0NjY4NDk1ODI3XSwgWy02Ni42NzYxMTM0NzM5OTgxLCA0NS45NTY3MjQ0OTM3MzA2XSwgWy02Ni42Nzc1MTQ4NDU4NDE0LCA0NS45NTY1NjgzNjU5Nzk3XSwgWy02Ni42Nzg5MjUyMDA4Mzc0LCA0NS45NTY2NTU3OTc1NzQ0XSwgWy02Ni42ODA0NjEzMTk5NzMzLCA0NS45NTcwNjE3MjgxNzEyXSwgWy02Ni42ODA5MTA0Nzc2MTUzLCA0NS45NTc2NTUwMDYwMDIyXSwgWy02Ni42ODEzNjg2MTg0MTAyLCA0NS45NTg5NDc3MDUxNzEzXSwgWy02Ni42ODEyMzM4NzExMTc2LCA0NS45NjAyNzc4NDIzOTk2XSwgWy02Ni42ODQxMTc0NjMxNzk2LCA0NS45NjAxMDkyMzUyMjI1XSwgWy02Ni42ODQ4MTgxNDkxMDEzLCA0NS45NjAyNTkxMDgyOTQyXSwgWy02Ni42ODU0MTEwMzcxODg4LCA0NS45NjA1NTg4NTMyMjE0XSwgWy02Ni42ODUwMDY3OTUzMTA5LCA0NS45NTk2MzQ2MzQ0ODc2XSwgWy02Ni42ODQ3MjgzMTc1NzI4LCA0NS45NTg0NDgxMTQ4NjQ5XSwgWy02Ni42ODQ2ODM0MDE4MDg2LCA0NS45NTc0ODYzOTA4NDM3XSwgWy02Ni42ODQ4NTQwODE3MTI2LCA0NS45NTYyODczMzQ5MTk2XSwgWy02Ni42ODUyMjIzOTA5NzkxLCA0NS45NTUxMzgyMTUzMTI1XSwgWy02Ni42ODU3NzkzNDY0NTUzLCA0NS45NTQwNTc3NzEzMzg3XSwgWy02Ni42ODY1NjA4ODA3NTI1LCA0NS45NTMwNTg0OTgwNDY3XSwgWy02Ni42ODc1NTgwMTA3MTc4LCA0NS45NTIxNDY2NDU0NDU2XSwgWy02Ni42ODQzNTEwMjUxNTM1LCA0NS45NTEzNzg0MjkyMTMzXSwgWy02Ni42ODI2ODkxNDE4Nzc5LCA0NS45NTExNTk4MjkxNTI0XSwgWy02Ni42ODA1NjkxMTc4MDc0LCA0NS45NTEwNDc0MDU5MjgyXSwgWy02Ni42NzgyNTE0NjQzNzQzLCA0NS45NTEzNTk2OTIwOTldLCBbLTY2LjY3NjA3NzU0MTM4NjgsIDQ1Ljk1MTk5Njc1MDQzMTZdLCBbLTY2LjY3NDY1ODIwMzIzNzksIDQ1Ljk1MjYzMzgwMTQ0MTVdLCBbLTY2LjY3MzM4MjU5NTUzNDQsIDQ1Ljk1MzQwODI0NTc0ODRdLCBbLTY2LjY3MjI5NTYzNDA0MDYsIDQ1Ljk1NDMwNzU4Njg0NjVdLCBbLTY2LjY3MTM5NzMxODc1NjUsIDQ1Ljk1NTMwNjgzNzYxNjJdLCBbLTY2LjY3MTAxMTA0MzE4NDMsIDQ1Ljk1NTk5MzgxMjA2ODVdLCBbLTY2LjY3MDc5NTQ0NzUxNjIsIDQ1Ljk1NjgxMTkyNTA3ODldLCBbLTY2LjY3MDgxMzQxMzgyMTgsIDQ1Ljk1NzY0ODc2MTAwNTRdLCBbLTY2LjY3MTA2NDk0MjEwMTQsIDQ1Ljk1ODQ2Njg0OTU4MjddXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgInByb3BlcnRpZXMiOiB7IkZJRCI6IDY5LCAiTmVpZ2hib3VyaCI6ICJIYW53ZWxsIE5vcnRoIiwgIk9CSkVDVElEIjogNjksICJTaGFwZV9BcmVhIjogNzQ3MjUxLjQ0NDgxOCwgIlNoYXBlX0xlbmciOiA0MzAxLjQzNDc0MDQ3LCAiaGlnaGxpZ2h0Ijoge30sICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZWQ5NzYiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJvcGFjaXR5IjogMC4xLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbLTY2LjYxODEwOTI1NjEwMjUsIDQ1LjkwODIxMDA2MzY4MjNdLCBbLTY2LjYxODAwMTQ1ODI2ODUsIDQ1LjkwODI0MTMxNjUwNjRdLCBbLTY2LjYxOTI0MTEzMzM2MDUsIDQ1LjkwODQyMjU4MjUzODddLCBbLTY2LjYyMTE0NTU2MTc2MjksIDQ1LjkwODQ4NTA4NzkyOTldLCBbLTY2LjYyMjcwODYzMDM1NzIsIDQ1LjkwODM0MTMyNTQyNV0sIFstNjYuNjI0MjI2NzgzMTg3NCwgNDUuOTA4MDI4Nzk2OTU2XSwgWy02Ni42MjU2NTUxMDQ0ODkxLCA0NS45MDc1NTM3NTAzMTI5XSwgWy02Ni42MjY5NTc2NjE2NTExLCA0NS45MDY5Mjg2ODI3NDY2XSwgWy02Ni42MjgxMDc1MDUyMTQ4LCA0NS45MDYxNjYwOTA3ODM5XSwgWy02Ni42MjkyMzAzOTkzMiwgNDUuOTA1MDk3MTk0MjUyNV0sIFstNjYuNjMyNzUxNzk1MjMzNywgNDUuOTAwNzMzODgyNjYyXSwgWy02Ni42Mzg1OTA4NDQ1ODA1LCA0NS44OTQwNzU3MzM1NTgyXSwgWy02Ni42Mzg3NDM1NTgxNzg4LCA0NS44OTI1Njg5NDMwMzc4XSwgWy02Ni42Mzg1ODE4NjE0Mjc2LCA0NS44OTE4MTg2NTg2NTMyXSwgWy02Ni42MzgxNTk2NTMyNDQxLCA0NS44OTA5MTgzMDQwMTIzXSwgWy02Ni42MzcwMDk4MDk2ODA0LCA0NS44ODk2MzY1MjM5NjI0XSwgWy02Ni42MzYyNDYyNDE2ODg5LCA0NS44ODkwOTg3OTI3OTI0XSwgWy02Ni42MzUxNTAyOTcwNDIzLCA0NS44ODg1NDIyOTgwNzY5XSwgWy02Ni42MzMxNDcwNTM5NTg3LCA0NS44ODc5NzMyOTIwOTc0XSwgWy02Ni42MzA5OTEwOTcyNzY4LCA0NS44ODc4MzU3MjkzMzczXSwgWy02Ni42Mjg4NzEwNzMyMDYzLCA0NS44ODgxNDIxMTg2NTU1XSwgWy02Ni42MjY5NzU2Mjc5NTY4LCA0NS44ODg4Njc0NDE3MzM4XSwgWy02Ni42MjYzNDY4MDcyNTc5LCA0NS44ODkyMzYzNTI0MjQ0XSwgWy02Ni42MjQyODk2NjUyNTczLCA0NS44OTEyNjIxOTExODgyXSwgWy02Ni42MTkxNDIzMTg2NzkzLCA0NS44OTY4MzI4NjY3OTQ0XSwgWy02Ni42MTUwNjM5NjcyODk0LCA0NS45MDE4ODQxMjk4OV0sIFstNjYuNjE0NjUwNzQyMjU4NywgNDUuOTAzNDAzMTY5ODc1M10sIFstNjYuNjE0ODU3MzU0Nzc0LCA0NS45MDQ5NDA5MjExMDU0XSwgWy02Ni42MTU1NDAwNzQzOSwgNDUuOTA2MjA5ODQ2MzQzN10sIFstNjYuNjE2NjQ1MDAyMTg5NCwgNDUuOTA3MzIyNDc2MTMzN10sIFstNjYuNjE4MTA5MjU2MTAyNSwgNDUuOTA4MjEwMDYzNjgyM11dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogNzAsICJOZWlnaGJvdXJoIjogIkRvYWsgUm9hZCIsICJPQkpFQ1RJRCI6IDcwLCAiU2hhcGVfQXJlYSI6IDI1NjAxMzAuMTc2MDQsICJTaGFwZV9MZW5nIjogNjM1MC42NjEzODcwNCwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmZmZmIyIiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni42NTAzNTg3NzQ4MDI0LCA0NS45MzU3MTgyMzgyMDY5XSwgWy02Ni42NTAxNDMxNzkxMzQyLCA0NS45MzYxNTU1NTkyNTc4XSwgWy02Ni42NTAyNzc5MjY0MjY5LCA0NS45MzYzNTU0NzYzMDM4XSwgWy02Ni42NTAxNDMxNzkxMzQyLCA0NS45MzY2MDUzNzE1OTc4XSwgWy02Ni42NDU2Njk1NjkwMTkzLCA0NS45NDE5NDY2MTQyMTA2XSwgWy02Ni42NDYyMzU1MDc2NDgzLCA0NS45NDIzMzM5MTIzODA1XSwgWy02Ni42NTI0NTE4NDk0MTQ0LCA0NS45NDQ5MTk5OTUzMjU4XSwgWy02Ni42NTMzODYwOTczMDk5LCA0NS45NDM4NDU1OTg3MDJdLCBbLTY2LjY1NDYwNzgwNjA5NjMsIDQ1Ljk0MjkyNzM0Nzg3NTddLCBbLTY2LjY1NjU4NDA5OTcyMTQsIDQ1Ljk0MTk4NDA5NDc5NjldLCBbLTY2LjY1NzEzMjA3MjA0NDcsIDQ1Ljk0MTgwOTE4NTE3NzRdLCBbLTY2LjY1NzQxOTUzMjkzNTYsIDQ1Ljk0MTkwOTEzMzU5OV0sIFstNjYuNjU3NjQ0MTExNzU2NywgNDUuOTQxNTcxODA2OTU0MV0sIFstNjYuNjU2MTcwODc0NjkwNywgNDUuOTQwOTQ3MTIyNTYyNV0sIFstNjYuNjU5OTE2ODQ5NDI1NSwgNDUuOTM2NjM2NjA4NDMwNF0sIFstNjYuNjU1Nzc1NjE1OTY1NywgNDUuOTM1MzgwODczODk2OV0sIFstNjYuNjU0MTg1NTk3OTEyOCwgNDUuOTM1MTEyMjMwNDc4NV0sIFstNjYuNjUzMjUxMzUwMDE3MywgNDUuOTM1MDg3MjQwMzI2OV0sIFstNjYuNjUyMDc0NTU2OTk1MSwgNDUuOTM1MjI0Njg2MDIxM10sIFstNjYuNjUwMzU4Nzc0ODAyNCwgNDUuOTM1NzE4MjM4MjA2OV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAicHJvcGVydGllcyI6IHsiRklEIjogNzEsICJOZWlnaGJvdXJoIjogIk1vbnRvZ29tZXJ5IC8gUHJvc3BlY3QgRWFzdCIsICJPQkpFQ1RJRCI6IDcxLCAiU2hhcGVfQXJlYSI6IDY3ODI1MS4wNDI2MTgsICJTaGFwZV9MZW5nIjogMzQ4MS4zMzI4NTE0OSwgImhpZ2hsaWdodCI6IHt9LCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmVkOTc2IiwgImZpbGxPcGFjaXR5IjogMC43LCAib3BhY2l0eSI6IDAuMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWy02Ni41OTg2MDY4MzEyODQzLCA0NS44OTM0MzE3NTc1NDk4XSwgWy02Ni41OTAyMzQ1MzI4MzYzLCA0NS44ODQwNDYzNjY2NDYyXSwgWy02Ni41OTAzNTEzMTM4MjMyLCA0NS44ODQ0Mjc4MTU4NDUxXSwgWy02Ni41ODk5MzgwODg3OTI2LCA0NS44ODQ3NTI5ODM1ODU5XSwgWy02Ni41ODk0NjE5ODE2OTIsIDQ1Ljg4NDg0MDUyODQyMTddLCBbLTY2LjU4OTQ1Mjk5ODUzOTEsIDQ1Ljg4NTIyODIyNTMyMTldLCBbLTY2LjU4OTEyMDYyMTg4NCwgNDUuODg1MjkwNzU2ODI2Nl0sIFstNjYuNTg4NTcyNjQ5NTYwNywgNDUuODg1MDE1NjE3Njc5NF0sIFstNjYuNTg4MjY3MjIyMzY0MSwgNDUuODg1MzAzMjYzMTE5MV0sIFstNjYuNTg3ODE4MDY0NzIyLCA0NS44ODUwOTY5MDg5MzI5XSwgWy02Ni41ODcxNzEyNzc3MTc1LCA0NS44ODUyNDA3MzE2Mjg1XSwgWy02Ni41ODYyODE5NDU1ODYyLCA0NS44ODYwNjYxNDE2MzcxXSwgWy02Ni41ODU4OTU2NzAwMTQsIDQ1Ljg4NjcyODk2MjAwNzhdLCBbLTY2LjU4NjM4MDc2MDI2NzQsIDQ1Ljg4NjgxNjUwMzcyOTZdLCBbLTY2LjU4NjQ3MDU5MTc5NTgsIDQ1Ljg4NzMwNDIzMzY1NDRdLCBbLTY2LjU4Njk2NDY2NTIwMjEsIDQ1Ljg4NzY2NjkwMTg0OF0sIFstNjYuNTg2ODM4OTAxMDYyNCwgNDUuODg4MDU0NTc5MDIyOF0sIFstNjYuNTg2MzYyNzkzOTYxOCwgNDUuODg4Mjc5NjgwNjU2OF0sIFstNjYuNTg2MDIxNDM0MTUzOCwgNDUuODg4NzE3Mzc1NjY3MV0sIFstNjYuNTg2MTU2MTgxNDQ2NCwgNDUuODg5MDk4NzkyNzkyNF0sIFstNjYuNTg1NTkwMjQyODE3NCwgNDUuODg5NzkyODQwMTg2M10sIFstNjYuNTg1MDc4MjAzMTA1NSwgNDUuODkwMTMwNDgxNzI4N10sIFstNjYuNTg0ODQ0NjQxMTMxNiwgNDUuODkwMTA1NDcxMzE0NV0sIFstNjYuNTg0NTIxMjQ3NjI5MywgNDUuODg5ODY3ODcxODE3Nl0sIFstNjYuNTgzODI5NTQ0ODYwNSwgNDUuODkwMTk5MjYwMzA5OF0sIFstNjYuNTgzMDY1OTc2ODY5LCA0NS44ODk5MTc4OTI4NDg4XSwgWy02Ni41ODI3NTE1NjY1MTk2LCA0NS44OTAyNzQyOTEzOTJdLCBbLTY2LjU4MjMzODM0MTQ4ODksIDQ1Ljg5MDM4MDU4NTI1MTZdLCBbLTY2LjU4MTc2MzQxOTcwNzEsIDQ1Ljg5MDc2ODI0MzQ4NjVdLCBbLTY2LjU4MTU0NzgyNDAzODksIDQ1Ljg5MTM4NzI0MDU0MjRdLCBbLTY2LjU4MTkxNjEzMzMwNTQsIDQ1Ljg5MTU4NzMxODkyMzVdLCBbLTY2LjU4MTczNjQ3MDI0ODUsIDQ1Ljg5MTc5OTkwMTQxMzddLCBbLTY2LjU4MTIwNjQ2NDIzMDksIDQ1Ljg5MTgwNjE1MzgyNzVdLCBbLTY2LjU4MTI3ODMyOTQ1MzYsIDQ1Ljg5MjMzNzYwNjQzMzRdLCBbLTY2LjU4MDkwMTAzNzAzNDMsIDQ1Ljg5MjQzNzY0NDAwMjJdLCBbLTY2LjU4MDc2NjI4OTc0MTcsIDQ1Ljg5MjgwMDI3ODY3ODddLCBbLTY2LjU3NzM4ODYyNDI3MzQsIDQ1Ljg5NTM4MjQxOTIwODddLCBbLTY2LjU3Nzc5Mjg2NjE1MTMsIDQ1Ljg5NjcxNDA4MTU2M10sIFstNjYuNTc4MzEzODg5MDE2LCA0NS44OTc3ODkzOTEyMzg4XSwgWy02Ni41NzkzNjQ5MTc4OTg1LCA0NS44OTg0NDU4MjAwNDldLCBbLTY2LjU4MDIxODMxNzQxODQsIDQ1Ljg5ODc4MzQwODk4NjldLCBbLTY2LjU4MDMxNzEzMjA5OTYsIDQ1Ljg5OTA3MDk4MzEyOThdLCBbLTY2LjU3OTkyMTg3MzM3NDYsIDQ1Ljg5OTM4OTgxMzU5MDhdLCBbLTY2LjU3OTA5NTQyMzMxMzIsIDQ1Ljg5OTYyMTEyMDgxODZdLCBbLTY2LjU3OTA2ODQ3Mzg1NDcsIDQ1LjkwMDI1ODc3MzU5MThdLCBbLTY2LjU3ODg3OTgyNzY0NSwgNDUuOTAwNTMzODM3MjMzMl0sIFstNjYuNTc4NDM5NjUzMTU1OCwgNDUuOTAwNTcxMzQ1ODA2XSwgWy02Ni41NzgxMjUyNDI4MDY0LCA0NS45MDA0NDAwNjU2OTA0XSwgWy02Ni41ODAzODAwMTQxNjk1LCA0NS45MDI5MjgwODM2NDddLCBbLTY2LjU4MjMyOTM1ODMzNjEsIDQ1LjkwNDg0NzE1NzAwNTldLCBbLTY2LjU4NjYyMzMwNTM5NDIsIDQ1LjkwODQ4NTA4NzkyOTldLCBbLTY2LjU5NDUyODQ3OTg5NDQsIDQ1Ljg5OTQ1ODU4MDcwNTFdLCBbLTY2LjU5NDg2OTgzOTcwMjQsIDQ1Ljg5OTIxNDc2OTY0MjhdLCBbLTY2LjU5NTYzMzQwNzY5MzksIDQ1Ljg5ODc4MzQwODk4NjldLCBbLTY2LjU5NjcyMDM2OTE4NzcsIDQ1Ljg5ODM4MzMwMzM1MzhdLCBbLTY2LjU5NzY1NDYxNzA4MzEsIDQ1Ljg5ODE3Njk5Nzc2MDJdLCBbLTY2LjU5ODg2NzM0MjcxNjcsIDQ1Ljg5ODA4MzIyMjIzN10sIFstNjYuNjAwMzIyNjEzNDc3LCA0NS44OTgyMDgyNTYyMzI3XSwgWy02Ni42MDA2MzcwMjM4MjY0LCA0NS44OTkyMTQ3Njk2NDI4XSwgWy02Ni41OTk4NDY1MDYzNzY0LCA0NS44OTYyODg5NTMzODk0XSwgWy02Ni41OTg2MDY4MzEyODQzLCA0NS44OTM0MzE3NTc1NDk4XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiA3MiwgIk5laWdoYm91cmgiOiAiRnJlZGVyaWN0b24gU291dGgiLCAiT0JKRUNUSUQiOiA3MiwgIlNoYXBlX0FyZWEiOiAyNTA0MDY2Ljk0Mzk1LCAiU2hhcGVfTGVuZyI6IDc3MjIuNDc5MzQ2MDUsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZkOGQzYyIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjgwNTYwMTM0NjU0NSwgNDUuOTQ1NjU3MDY5MzM5MV0sIFstNjYuNjc5Mjc1NTQzNzk4MiwgNDUuOTQ3MDY4NzI2MTA3XSwgWy02Ni42NzkzMjk0NDI3MTUzLCA0NS45NDc2NzQ2MDMxNjNdLCBbLTY2LjY3OTA5NTg4MDc0MTQsIDQ1Ljk0NzkxMTk1NTI1NTldLCBbLTY2LjY2NzAwNDU1NzAxNzIsIDQ1Ljk0NjMzMTY3MDg2MzVdLCBbLTY2LjY2NzE3NTIzNjkyMTEsIDQ1Ljk0NzEwNjIwMzIzMDVdLCBbLTY2LjY2NzEzMDMyMTE1NjksIDQ1Ljk0NzczMDgxODIyNDJdLCBbLTY2LjY2Njg1MTg0MzQxODksIDQ1Ljk0ODQ5MjgzODk4NTNdLCBbLTY2LjY2NjQ1NjU4NDY5MzgsIDQ1Ljk0OTA2MTIyNDY5OTFdLCBbLTY2LjY2NTc2NDg4MTkyNTEsIDQ1Ljk0OTY3OTU3MTc2ODFdLCBbLTY2LjY2MDI4NTE1ODY5MTksIDQ1Ljk1NjAwMDA1NzI1MThdLCBbLTY2LjY1ODc0OTAzOTU1NjEsIDQ1Ljk1NjQxODQ4MjkyNTFdLCBbLTY2LjY1NzcwNjk5MzgyNjUsIDQ1Ljk1Njk4MDU0MjI4OThdLCBbLTY2LjY2MDExNDQ3ODc4OCwgNDUuOTU3MzczOTgwNDUzXSwgWy02Ni42NjA1MzY2ODY5NzE1LCA0NS45NTc1MzAxMDU5MzRdLCBbLTY2LjY2MTM5MDA4NjQ5MTQsIDQ1Ljk1ODE4NTgyODE1MDldLCBbLTY2LjY2MTY3NzU0NzM4MjMsIDQ1Ljk1ODkxNjQ4MDkwOTFdLCBbLTY2LjY2MzA5Njg4NTUzMTIsIDQ1Ljk1OTAxNjM5ODQ4NjFdLCBbLTY2LjY2NDQ2MjMyNDc2MzEsIDQ1Ljk1OTI3MjQzNjQ1NDldLCBbLTY2LjY2NzIyMDE1MjY4NTQsIDQ1Ljk2MDAyODA1MzgwNjFdLCBbLTY2LjY2ODYzMDUwNzY4MTQsIDQ1Ljk2MDc1ODY4MjI3MTldLCBbLTY2LjY2OTUxMDg1NjY1OTksIDQ1Ljk1OTI3MjQzNjQ1NDldLCBbLTY2LjY3MDA1ODgyODk4MzIsIDQ1Ljk1ODg1NDAzMjMzMTldLCBbLTY2LjY3MTA2NDk0MjEwMTQsIDQ1Ljk1ODQ2Njg0OTU4MjddLCBbLTY2LjY3MDc3NzQ4MTIxMDUsIDQ1Ljk1NzE0OTE1ODk4NzVdLCBbLTY2LjY3MTA4MjkwODQwNzEsIDQ1Ljk1NTgzMTQzNzA1NzVdLCBbLTY2LjY3MjA5ODAwNDY3ODEsIDQ1Ljk1NDUwMTE5MzA5MDRdLCBbLTY2LjY3MzYyNTE0MDY2MTEsIDQ1Ljk1MzI0NTg2MzE2MTRdLCBbLTY2LjY3NTQ5MzYzNjQ1MjEsIDQ1Ljk1MjIzNDA4NDAxNjZdLCBbLTY2LjY3NzkyODA3MDg3MjEsIDQ1Ljk1MTQyODM5NDgyMDVdLCBbLTY2LjY4MDU2OTExNzgwNzQsIDQ1Ljk1MTA0NzQwNTkyODJdLCBbLTY2LjY4MjY4OTE0MTg3NzksIDQ1Ljk1MTE1OTgyOTE1MjRdLCBbLTY2LjY4NTE3NzQ3NTIxNDksIDQ1Ljk1MTUyODMyNTg5OTddLCBbLTY2LjY4NzU1ODAxMDcxNzgsIDQ1Ljk1MjE0NjY0NTQ0NTZdLCBbLTY2LjY4ODA0MzEwMDk3MTIsIDQ1Ljk1MTc5Njg4OTc4MjJdLCBbLTY2LjY4OTM4MTU5MDc0NDYsIDQ1Ljk1MTgwOTM4MTA5MzldLCBbLTY2LjY5MDcwMjExNDIxMjIsIDQ1Ljk1MTk5Njc1MDQzMTZdLCBbLTY2LjY5Mjg4NTAyMDM1MjcsIDQ1Ljk1MjcwODc0ODEzNzddLCBbLTY2LjY5MzM3OTA5Mzc1ODksIDQ1Ljk1MzAyNzI3MDQ2Nl0sIFstNjYuNjkzNjM5NjA1MTkxMywgNDUuOTUzMzU4MjgxOTI2Ml0sIFstNjYuNjkzNzExNDcwNDE0LCA0NS45NTQwMTQwNTM1MDkxXSwgWy02Ni42OTMyOTgyNDUzODM0LCA0NS45NTQ3OTQ3MjM4NDc1XSwgWy02Ni42OTI1Nzk1OTMxNTYxLCA0NS45NTUwMDcwNjQyNzcxXSwgWy02Ni42OTE4NTE5NTc3NzU5LCA0NS45NTQ3OTQ3MjM4NDc1XSwgWy02Ni42OTE2ODEyNzc4NzE5LCA0NS45NTQ4Mzg0NDEwNjEzXSwgWy02Ni42OTA5MTc3MDk4ODA0LCA0NS45NTUxNDQ0NjA1OTIxXSwgWy02Ni42OTAzNjA3NTQ0MDQzLCA0NS45NTU1NzUzODMxODg3XSwgWy02Ni42ODk2MzMxMTkwMjQxLCA0NS45NTY1MzcxNDAzNzY4XSwgWy02Ni42ODgxNjg4NjUxMTEsIDQ1Ljk1OTM3ODU5ODE5MjVdLCBbLTY2LjY4NzY1NjgyNTM5OTEsIDQ1Ljk2MDAyODA1MzgwNjFdLCBbLTY2LjY4ODg3ODUzNDE4NTUsIDQ1Ljk1OTc3MjAxOTMyODldLCBbLTY2LjY5ODEyMjE5ODQ1OTEsIDQ1Ljk2MDgwODYzOTQyMl0sIFstNjYuNjk3MzQwNjY0MTYxOSwgNDUuOTYwMDc4MDExNjE0OV0sIFstNjYuNjk2Njc1OTEwODUxNiwgNDUuOTU5MDg1MDkxNzE1OF0sIFstNjYuNjk2NDYwMzE1MTgzNCwgNDUuOTU4NTU0Mjc4MTgxOV0sIFstNjYuNjk2NDk2MjQ3Nzk0OCwgNDUuOTU3NjIzNzgxMDExNV0sIFstNjYuNjk4Nzk1OTM0OTIyMiwgNDUuOTUxNzg0Mzk4NDY3N10sIFstNjYuNjk5MTczMjI3MzQxNSwgNDUuOTUxMTUzNTgzNDIzN10sIFstNjYuNzAwMjYwMTg4ODM1MywgNDUuOTUwNzY2MzQ2ODY5OV0sIFstNjYuNjk5ODkxODc5NTY4OCwgNDUuOTUwMzQxNjMyNzAwMV0sIFstNjYuNjk1NzIzNjk2NjUwNSwgNDUuOTUwNzE2MzgwNjY1OV0sIFstNjYuNjk1NjY5Nzk3NzMzNCwgNDUuOTUwNDQ3ODExNTQ3Nl0sIFstNjYuNjkzODAxMzAxOTQyNCwgNDUuOTUwNDM1MzE5OTI5MV0sIFstNjYuNjkxOTU5NzU1NjEsIDQ1Ljk1MDE0ODAxMTkyNV0sIFstNjYuNjkwMTcyMTA4MTk0NiwgNDUuOTQ5NTc5NjM3MzU1Nl0sIFstNjYuNjgwODIwNjQ2MDg2OSwgNDUuOTQ1NjEzMzQ0ODgzXSwgWy02Ni42ODA1NjAxMzQ2NTQ1LCA0NS45NDU2NTcwNjkzMzkxXV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiA3MywgIk5laWdoYm91cmgiOiAiRnJlZGVyaWN0b24gU291dGgiLCAiT0JKRUNUSUQiOiA3MywgIlNoYXBlX0FyZWEiOiAyMjI3Njg5LjMwNDczLCAiU2hhcGVfTGVuZyI6IDExMTQ4LjE5OTE3NzQsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZkOGQzYyIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1stNjYuNjc0NzkyOTUwNTMwNSwgNDUuOTYyMjAxMTc2ODUxMl0sIFstNjYuNjc0Mjg5ODkzOTcxNCwgNDUuOTYxNzA3ODYwNDJdLCBbLTY2LjY3MzU5ODE5MTIwMjYsIDQ1Ljk2MTM3MDY1NDI1Nl0sIFstNjYuNjcyNzg5NzA3NDQ2OSwgNDUuOTYxMTg5NTYxMjA5OF0sIFstNjYuNjcxOTQ1MjkxMDc5OCwgNDUuOTYxMTc3MDcyMDEyNF0sIFstNjYuNjY5ODc5MTY1OTI2MywgNDUuOTYxNTUxNzQ2NzEwM10sIFstNjYuNjY3ODEzMDQwNzcyOSwgNDUuOTYyMjQ0ODg4MjIxOV0sIFstNjYuNjYwODUxMDk3MzIwOSwgNDUuOTYzOTgwODI2MjAzOV0sIFstNjYuNjU4NjA1MzA5MTEwNiwgNDUuOTY0MTYxOTEwMTI2NV0sIFstNjYuNjU2ODM1NjI4MDAwOSwgNDUuOTYzOTk5NTU5MDUwOV0sIFstNjYuNjU0MTU4NjQ4NDU0MywgNDUuOTYzNTgxMTkwNjI0OV0sIFstNjYuNjUyMDkyNTIzMzAwOCwgNDUuOTYzNDU2MzAzOTE1Ml0sIFstNjYuNjUxNDU0NzE5NDQ5MSwgNDUuOTYzNTYyNDU3NjM2NF0sIFstNjYuNjUxMDA1NTYxODA3LCA0NS45NjM3NjIyNzU4NTM4XSwgWy02Ni42NTA1OTIzMzY3NzYzLCA0NS45NjQxMTgyMDAyNjgzXSwgWy02Ni42NTA0MTI2NzM3MTk1LCA0NS45NjQ0Njc4NzgxNjhdLCBbLTY2LjY1MDk1MTY2Mjg5LCA0NS45NjQ5NDI0Mzc1MDE1XSwgWy02Ni42NTE1ODA0ODM1ODg4LCA0NS45NjUxOTg0NDgwODU1XSwgWy02Ni42NTIyOTAxNTI2NjMzLCA0NS45NjUzMDQ1OTg0Njg0XSwgWy02Ni42NTMwMTc3ODgwNDM0LCA0NS45NjUyNDIxNTcwOTEzXSwgWy02Ni42NTQ2NzA2ODgxNjYyLCA0NS45NjU1MDQ0MTA0MDIyXSwgWy02Ni42NTYyNTE3MjMwNjYzLCA0NS45NjU5MjkwMDgzNjg0XSwgWy02Ni42NTc3MzM5NDMyODUxLCA0NS45NjY1MDM0NTkyNjA0XSwgWy02Ni42NTk3NzMxMTg5OCwgNDUuOTY2MjM0OTY2NjUwMl0sIFstNjYuNjYwOTg1ODQ0NjEzNiwgNDUuOTY1ODY2NTY3Njk1Ml0sIFstNjYuNjYyNjQ3NzI3ODg5MiwgNDUuOTY1NjIzMDQ4Mzk2OF0sIFstNjYuNjY0MzA5NjExMTY0OCwgNDUuOTY1MDQ4NTg4Mzc1MV0sIFstNjYuNjY2MTA2MjQxNzMzMSwgNDUuOTY0NjU1MjA0NzA2NF0sIFstNjYuNjY2MjU4OTU1MzMxNCwgNDUuOTY0NDYxNjMzOTM5Ml0sIFstNjYuNjY2NTE5NDY2NzYzNywgNDUuOTY0NTU1Mjk3Mjk4MV0sIFstNjYuNjY5NDIxMDI1MTMxNCwgNDUuOTY0MTgwNjQyOTEyM10sIFstNjYuNjcwODY3MzEyNzM4OSwgNDUuOTY0MDk5NDY3NDYxNF0sIFstNjYuNjczNjg4MDIyNzMxLCA0NS45NjQyMTE4NjQyMDc5XSwgWy02Ni42NzQ3OTI5NTA1MzA1LCA0NS45NjIyMDExNzY4NTEyXV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJwcm9wZXJ0aWVzIjogeyJGSUQiOiA3NCwgIk5laWdoYm91cmgiOiAiV29vZHN0b2NrIFJvYWQiLCAiT0JKRUNUSUQiOiA3NCwgIlNoYXBlX0FyZWEiOiA0Mzk3NjMuOTMyNTQzLCAiU2hhcGVfTGVuZyI6IDQyNDAuMzk5MTQ5MDYsICJoaWdobGlnaHQiOiB7fSwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZkOGQzYyIsICJmaWxsT3BhY2l0eSI6IDAuNywgIm9wYWNpdHkiOiAwLjEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifV0sICJ0eXBlIjogIkZlYXR1cmVDb2xsZWN0aW9uIn0KICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80ZjczYTJmYThjMzA0OWNhODQxMjFkNmU0NzQ3MGE3Myk7CiAgICAgICAgICAgICAgICBnZW9fanNvbl9jMzlmYzhmYjgxNmU0ODczYmZlZWI5ZjljODMwMzU1NC5zZXRTdHlsZShmdW5jdGlvbihmZWF0dXJlKSB7cmV0dXJuIGZlYXR1cmUucHJvcGVydGllcy5zdHlsZTt9KTsKCiAgICAgICAgICAgIAogICAgCiAgICB2YXIgY29sb3JfbWFwX2IxYTFlZmM2MmExYzQzMGU4NGY1OTQ1ZWQwNDU3YmEwID0ge307CgogICAgCiAgICBjb2xvcl9tYXBfYjFhMWVmYzYyYTFjNDMwZTg0ZjU5NDVlZDA0NTdiYTAuY29sb3IgPSBkMy5zY2FsZS50aHJlc2hvbGQoKQogICAgICAgICAgICAgIC5kb21haW4oWzEuMCwgMS4wODAxNjAzMjA2NDEyODI2LCAxLjE2MDMyMDY0MTI4MjU2NSwgMS4yNDA0ODA5NjE5MjM4NDc3LCAxLjMyMDY0MTI4MjU2NTEzMDEsIDEuNDAwODAxNjAzMjA2NDEyOCwgMS40ODA5NjE5MjM4NDc2OTU0LCAxLjU2MTEyMjI0NDQ4ODk3OCwgMS42NDEyODI1NjUxMzAyNjA1LCAxLjcyMTQ0Mjg4NTc3MTU0MzEsIDEuODAxNjAzMjA2NDEyODI1NiwgMS44ODE3NjM1MjcwNTQxMDgyLCAxLjk2MTkyMzg0NzY5NTM5MDksIDIuMDQyMDg0MTY4MzM2NjczNSwgMi4xMjIyNDQ0ODg5Nzc5NTYsIDIuMjAyNDA0ODA5NjE5MjM5LCAyLjI4MjU2NTEzMDI2MDUyMSwgMi4zNjI3MjU0NTA5MDE4MDM2LCAyLjQ0Mjg4NTc3MTU0MzA4NjMsIDIuNTIzMDQ2MDkyMTg0MzY4NSwgMi42MDMyMDY0MTI4MjU2NTEsIDIuNjgzMzY2NzMzNDY2OTMzOCwgMi43NjM1MjcwNTQxMDgyMTY0LCAyLjg0MzY4NzM3NDc0OTQ5OSwgMi45MjM4NDc2OTUzOTA3ODE3LCAzLjAwNDAwODAxNjAzMjA2NCwgMy4wODQxNjgzMzY2NzMzNDY2LCAzLjE2NDMyODY1NzMxNDYyOSwgMy4yNDQ0ODg5Nzc5NTU5MTIsIDMuMzI0NjQ5Mjk4NTk3MTk0NSwgMy40MDQ4MDk2MTkyMzg0NzcsIDMuNDg0OTY5OTM5ODc5NzU5MywgMy41NjUxMzAyNjA1MjEwNDIsIDMuNjQ1MjkwNTgxMTYyMzI0NiwgMy43MjU0NTA5MDE4MDM2MDczLCAzLjgwNTYxMTIyMjQ0NDg5LCAzLjg4NTc3MTU0MzA4NjE3MjYsIDMuOTY1OTMxODYzNzI3NDU0OCwgNC4wNDYwOTIxODQzNjg3MzcsIDQuMTI2MjUyNTA1MDEwMDIwNSwgNC4yMDY0MTI4MjU2NTEzMDIsIDQuMjg2NTczMTQ2MjkyNTg2LCA0LjM2NjczMzQ2NjkzMzg2NzUsIDQuNDQ2ODkzNzg3NTc1MTUsIDQuNTI3MDU0MTA4MjE2NDMzLCA0LjYwNzIxNDQyODg1NzcxNTUsIDQuNjg3Mzc0NzQ5NDk4OTk4LCA0Ljc2NzUzNTA3MDE0MDI4MSwgNC44NDc2OTUzOTA3ODE1NjMsIDQuOTI3ODU1NzExNDIyODQ1LCA1LjAwODAxNjAzMjA2NDEyOCwgNS4wODgxNzYzNTI3MDU0MTA1LCA1LjE2ODMzNjY3MzM0NjY5MywgNS4yNDg0OTY5OTM5ODc5NzYsIDUuMzI4NjU3MzE0NjI5MjU4LCA1LjQwODgxNzYzNTI3MDU0MSwgNS40ODg5Nzc5NTU5MTE4MjQsIDUuNTY5MTM4Mjc2NTUzMTA2LCA1LjY0OTI5ODU5NzE5NDM4OSwgNS43Mjk0NTg5MTc4MzU2NzIsIDUuODA5NjE5MjM4NDc2OTU0LCA1Ljg4OTc3OTU1OTExODIzNiwgNS45Njk5Mzk4Nzk3NTk1MTksIDYuMDUwMTAwMjAwNDAwODAxLCA2LjEzMDI2MDUyMTA0MjA4NCwgNi4yMTA0MjA4NDE2ODMzNjcsIDYuMjkwNTgxMTYyMzI0NjQ5LCA2LjM3MDc0MTQ4Mjk2NTkzMiwgNi40NTA5MDE4MDM2MDcyMTQ1LCA2LjUzMTA2MjEyNDI0ODQ5NywgNi42MTEyMjI0NDQ4ODk3OCwgNi42OTEzODI3NjU1MzEwNjI1LCA2Ljc3MTU0MzA4NjE3MjM0NSwgNi44NTE3MDM0MDY4MTM2MjcsIDYuOTMxODYzNzI3NDU0OTA5NSwgNy4wMTIwMjQwNDgwOTYxOTIsIDcuMDkyMTg0MzY4NzM3NDc1LCA3LjE3MjM0NDY4OTM3ODc1NzUsIDcuMjUyNTA1MDEwMDIwMDQsIDcuMzMyNjY1MzMwNjYxMzIzLCA3LjQxMjgyNTY1MTMwMjYwNSwgNy40OTI5ODU5NzE5NDM4ODgsIDcuNTczMTQ2MjkyNTg1MTcxLCA3LjY1MzMwNjYxMzIyNjQ1MywgNy43MzM0NjY5MzM4Njc3MzUsIDcuODEzNjI3MjU0NTA5MDE4LCA3Ljg5Mzc4NzU3NTE1MDMsIDcuOTczOTQ3ODk1NzkxNTgzLCA4LjA1NDEwODIxNjQzMjg2NiwgOC4xMzQyNjg1MzcwNzQxNSwgOC4yMTQ0Mjg4NTc3MTU0MzEsIDguMjk0NTg5MTc4MzU2NzEzLCA4LjM3NDc0OTQ5ODk5Nzk5NiwgOC40NTQ5MDk4MTk2MzkyOCwgOC41MzUwNzAxNDAyODA1NjIsIDguNjE1MjMwNDYwOTIxODQzLCA4LjY5NTM5MDc4MTU2MzEyNywgOC43NzU1NTExMDIyMDQ0MDksIDguODU1NzExNDIyODQ1NjksIDguOTM1ODcxNzQzNDg2OTc0LCA5LjAxNjAzMjA2NDEyODI1NiwgOS4wOTYxOTIzODQ3Njk1NCwgOS4xNzYzNTI3MDU0MTA4MjEsIDkuMjU2NTEzMDI2MDUyMTA0LCA5LjMzNjY3MzM0NjY5MzM4NiwgOS40MTY4MzM2NjczMzQ2NywgOS40OTY5OTM5ODc5NzU5NTIsIDkuNTc3MTU0MzA4NjE3MjM1LCA5LjY1NzMxNDYyOTI1ODUxNywgOS43Mzc0NzQ5NDk4OTk4LCA5LjgxNzYzNTI3MDU0MTA4MiwgOS44OTc3OTU1OTExODIzNjQsIDkuOTc3OTU1OTExODIzNjQ3LCAxMC4wNTgxMTYyMzI0NjQ5MywgMTAuMTM4Mjc2NTUzMTA2MjEzLCAxMC4yMTg0MzY4NzM3NDc0OTQsIDEwLjI5ODU5NzE5NDM4ODc3OCwgMTAuMzc4NzU3NTE1MDMwMDYsIDEwLjQ1ODkxNzgzNTY3MTM0MywgMTAuNTM5MDc4MTU2MzEyNjI1LCAxMC42MTkyMzg0NzY5NTM5MDksIDEwLjY5OTM5ODc5NzU5NTE5LCAxMC43Nzk1NTkxMTgyMzY0NzIsIDEwLjg1OTcxOTQzODg3Nzc1NiwgMTAuOTM5ODc5NzU5NTE5MDM3LCAxMS4wMjAwNDAwODAxNjAzMiwgMTEuMTAwMjAwNDAwODAxNjAzLCAxMS4xODAzNjA3MjE0NDI4ODYsIDExLjI2MDUyMTA0MjA4NDE2OCwgMTEuMzQwNjgxMzYyNzI1NDUxLCAxMS40MjA4NDE2ODMzNjY3MzMsIDExLjUwMTAwMjAwNDAwODAxNywgMTEuNTgxMTYyMzI0NjQ5Mjk5LCAxMS42NjEzMjI2NDUyOTA1ODIsIDExLjc0MTQ4Mjk2NTkzMTg2NCwgMTEuODIxNjQzMjg2NTczMTQ2LCAxMS45MDE4MDM2MDcyMTQ0MjksIDExLjk4MTk2MzkyNzg1NTcxLCAxMi4wNjIxMjQyNDg0OTY5OTQsIDEyLjE0MjI4NDU2OTEzODI3NiwgMTIuMjIyNDQ0ODg5Nzc5NTYsIDEyLjMwMjYwNTIxMDQyMDg0MSwgMTIuMzgyNzY1NTMxMDYyMTI1LCAxMi40NjI5MjU4NTE3MDM0MDcsIDEyLjU0MzA4NjE3MjM0NDY5LCAxMi42MjMyNDY0OTI5ODU5NzIsIDEyLjcwMzQwNjgxMzYyNzI1NCwgMTIuNzgzNTY3MTM0MjY4NTM3LCAxMi44NjM3Mjc0NTQ5MDk4MTksIDEyLjk0Mzg4Nzc3NTU1MTEwMywgMTMuMDI0MDQ4MDk2MTkyMzg0LCAxMy4xMDQyMDg0MTY4MzM2NjgsIDEzLjE4NDM2ODczNzQ3NDk1LCAxMy4yNjQ1MjkwNTgxMTYyMzMsIDEzLjM0NDY4OTM3ODc1NzUxNSwgMTMuNDI0ODQ5Njk5Mzk4Nzk4LCAxMy41MDUwMTAwMjAwNDAwOCwgMTMuNTg1MTcwMzQwNjgxMzYyLCAxMy42NjUzMzA2NjEzMjI2NDYsIDEzLjc0NTQ5MDk4MTk2MzkyNywgMTMuODI1NjUxMzAyNjA1MjEsIDEzLjkwNTgxMTYyMzI0NjQ5MywgMTMuOTg1OTcxOTQzODg3Nzc2LCAxNC4wNjYxMzIyNjQ1MjkwNTgsIDE0LjE0NjI5MjU4NTE3MDM0MSwgMTQuMjI2NDUyOTA1ODExNjIzLCAxNC4zMDY2MTMyMjY0NTI5MDcsIDE0LjM4Njc3MzU0NzA5NDE4OCwgMTQuNDY2OTMzODY3NzM1NDcsIDE0LjU0NzA5NDE4ODM3Njc1NCwgMTQuNjI3MjU0NTA5MDE4MDM1LCAxNC43MDc0MTQ4Mjk2NTkzMTksIDE0Ljc4NzU3NTE1MDMwMDYsIDE0Ljg2NzczNTQ3MDk0MTg4NCwgMTQuOTQ3ODk1NzkxNTgzMTY2LCAxNS4wMjgwNTYxMTIyMjQ0NSwgMTUuMTA4MjE2NDMyODY1NzMxLCAxNS4xODgzNzY3NTM1MDcwMTUsIDE1LjI2ODUzNzA3NDE0ODI5NywgMTUuMzQ4Njk3Mzk0Nzg5NTc4LCAxNS40Mjg4NTc3MTU0MzA4NjIsIDE1LjUwOTAxODAzNjA3MjE0NCwgMTUuNTg5MTc4MzU2NzEzNDI3LCAxNS42NjkzMzg2NzczNTQ3MDksIDE1Ljc0OTQ5ODk5Nzk5NTk5MywgMTUuODI5NjU5MzE4NjM3Mjc0LCAxNS45MDk4MTk2MzkyNzg1NTgsIDE1Ljk4OTk3OTk1OTkxOTg0LCAxNi4wNzAxNDAyODA1NjExMjMsIDE2LjE1MDMwMDYwMTIwMjQwMywgMTYuMjMwNDYwOTIxODQzNjg3LCAxNi4zMTA2MjEyNDI0ODQ5NywgMTYuMzkwNzgxNTYzMTI2MjU0LCAxNi40NzA5NDE4ODM3Njc1MzcsIDE2LjU1MTEwMjIwNDQwODgxNywgMTYuNjMxMjYyNTI1MDUwMSwgMTYuNzExNDIyODQ1NjkxMzgsIDE2Ljc5MTU4MzE2NjMzMjY2NCwgMTYuODcxNzQzNDg2OTczOTQ4LCAxNi45NTE5MDM4MDc2MTUyMywgMTcuMDMyMDY0MTI4MjU2NTEsIDE3LjExMjIyNDQ0ODg5Nzc5NSwgMTcuMTkyMzg0NzY5NTM5MDgsIDE3LjI3MjU0NTA5MDE4MDM2MiwgMTcuMzUyNzA1NDEwODIxNjQyLCAxNy40MzI4NjU3MzE0NjI5MjUsIDE3LjUxMzAyNjA1MjEwNDIxLCAxNy41OTMxODYzNzI3NDU0OTIsIDE3LjY3MzM0NjY5MzM4Njc3MiwgMTcuNzUzNTA3MDE0MDI4MDU2LCAxNy44MzM2NjczMzQ2NjkzNCwgMTcuOTEzODI3NjU1MzEwNjIsIDE3Ljk5Mzk4Nzk3NTk1MTkwMywgMTguMDc0MTQ4Mjk2NTkzMTg3LCAxOC4xNTQzMDg2MTcyMzQ0NywgMTguMjM0NDY4OTM3ODc1NzUsIDE4LjMxNDYyOTI1ODUxNzAzNCwgMTguMzk0Nzg5NTc5MTU4MzE3LCAxOC40NzQ5NDk4OTk3OTk2LCAxOC41NTUxMTAyMjA0NDA4OCwgMTguNjM1MjcwNTQxMDgyMTY0LCAxOC43MTU0MzA4NjE3MjM0NDgsIDE4Ljc5NTU5MTE4MjM2NDcyOCwgMTguODc1NzUxNTAzMDA2MDEsIDE4Ljk1NTkxMTgyMzY0NzI5NSwgMTkuMDM2MDcyMTQ0Mjg4NTgsIDE5LjExNjIzMjQ2NDkyOTg2LCAxOS4xOTYzOTI3ODU1NzExNDIsIDE5LjI3NjU1MzEwNjIxMjQyNSwgMTkuMzU2NzEzNDI2ODUzNzEsIDE5LjQzNjg3Mzc0NzQ5NDk5LCAxOS41MTcwMzQwNjgxMzYyNzIsIDE5LjU5NzE5NDM4ODc3NzU1NiwgMTkuNjc3MzU0NzA5NDE4ODM2LCAxOS43NTc1MTUwMzAwNjAxMiwgMTkuODM3Njc1MzUwNzAxNDAzLCAxOS45MTc4MzU2NzEzNDI2ODcsIDE5Ljk5Nzk5NTk5MTk4Mzk2NiwgMjAuMDc4MTU2MzEyNjI1MjUsIDIwLjE1ODMxNjYzMzI2NjUzNCwgMjAuMjM4NDc2OTUzOTA3ODE3LCAyMC4zMTg2MzcyNzQ1NDkwOTcsIDIwLjM5ODc5NzU5NTE5MDM4LCAyMC40Nzg5NTc5MTU4MzE2NjQsIDIwLjU1OTExODIzNjQ3Mjk0NCwgMjAuNjM5Mjc4NTU3MTE0MjI4LCAyMC43MTk0Mzg4Nzc3NTU1MSwgMjAuNzk5NTk5MTk4Mzk2Nzk1LCAyMC44Nzk3NTk1MTkwMzgwNzUsIDIwLjk1OTkxOTgzOTY3OTM2LCAyMS4wNDAwODAxNjAzMjA2NCwgMjEuMTIwMjQwNDgwOTYxOTI1LCAyMS4yMDA0MDA4MDE2MDMyMDUsIDIxLjI4MDU2MTEyMjI0NDQ5LCAyMS4zNjA3MjE0NDI4ODU3NzIsIDIxLjQ0MDg4MTc2MzUyNzA1NiwgMjEuNTIxMDQyMDg0MTY4MzM2LCAyMS42MDEyMDI0MDQ4MDk2MiwgMjEuNjgxMzYyNzI1NDUwOTAzLCAyMS43NjE1MjMwNDYwOTIxODMsIDIxLjg0MTY4MzM2NjczMzQ2NiwgMjEuOTIxODQzNjg3Mzc0NzUsIDIyLjAwMjAwNDAwODAxNjAzNCwgMjIuMDgyMTY0MzI4NjU3MzEzLCAyMi4xNjIzMjQ2NDkyOTg1OTcsIDIyLjI0MjQ4NDk2OTkzOTg4LCAyMi4zMjI2NDUyOTA1ODExNjQsIDIyLjQwMjgwNTYxMTIyMjQ0NCwgMjIuNDgyOTY1OTMxODYzNzI4LCAyMi41NjMxMjYyNTI1MDUwMSwgMjIuNjQzMjg2NTczMTQ2MjksIDIyLjcyMzQ0Njg5Mzc4NzU3NSwgMjIuODAzNjA3MjE0NDI4ODU4LCAyMi44ODM3Njc1MzUwNzAxNCwgMjIuOTYzOTI3ODU1NzExNDIsIDIzLjA0NDA4ODE3NjM1MjcwNSwgMjMuMTI0MjQ4NDk2OTkzOTksIDIzLjIwNDQwODgxNzYzNTI3MiwgMjMuMjg0NTY5MTM4Mjc2NTUyLCAyMy4zNjQ3Mjk0NTg5MTc4MzYsIDIzLjQ0NDg4OTc3OTU1OTEyLCAyMy41MjUwNTAxMDAyMDA0LCAyMy42MDUyMTA0MjA4NDE2ODMsIDIzLjY4NTM3MDc0MTQ4Mjk2NiwgMjMuNzY1NTMxMDYyMTI0MjUsIDIzLjg0NTY5MTM4Mjc2NTUzLCAyMy45MjU4NTE3MDM0MDY4MTMsIDI0LjAwNjAxMjAyNDA0ODA5NywgMjQuMDg2MTcyMzQ0Njg5MzgsIDI0LjE2NjMzMjY2NTMzMDY2LCAyNC4yNDY0OTI5ODU5NzE5NDQsIDI0LjMyNjY1MzMwNjYxMzIyOCwgMjQuNDA2ODEzNjI3MjU0NTA4LCAyNC40ODY5NzM5NDc4OTU3OSwgMjQuNTY3MTM0MjY4NTM3MDc1LCAyNC42NDcyOTQ1ODkxNzgzNTgsIDI0LjcyNzQ1NDkwOTgxOTYzOCwgMjQuODA3NjE1MjMwNDYwOTIsIDI0Ljg4Nzc3NTU1MTEwMjIwNSwgMjQuOTY3OTM1ODcxNzQzNDksIDI1LjA0ODA5NjE5MjM4NDc3LCAyNS4xMjgyNTY1MTMwMjYwNTIsIDI1LjIwODQxNjgzMzY2NzMzNiwgMjUuMjg4NTc3MTU0MzA4NjE2LCAyNS4zNjg3Mzc0NzQ5NDk5LCAyNS40NDg4OTc3OTU1OTExODMsIDI1LjUyOTA1ODExNjIzMjQ2NiwgMjUuNjA5MjE4NDM2ODczNzQ2LCAyNS42ODkzNzg3NTc1MTUwMywgMjUuNzY5NTM5MDc4MTU2MzEzLCAyNS44NDk2OTkzOTg3OTc1OTcsIDI1LjkyOTg1OTcxOTQzODg3NywgMjYuMDEwMDIwMDQwMDgwMTYsIDI2LjA5MDE4MDM2MDcyMTQ0NCwgMjYuMTcwMzQwNjgxMzYyNzI0LCAyNi4yNTA1MDEwMDIwMDQwMDcsIDI2LjMzMDY2MTMyMjY0NTI5LCAyNi40MTA4MjE2NDMyODY1NzUsIDI2LjQ5MDk4MTk2MzkyNzg1NSwgMjYuNTcxMTQyMjg0NTY5MTM4LCAyNi42NTEzMDI2MDUyMTA0MiwgMjYuNzMxNDYyOTI1ODUxNzA1LCAyNi44MTE2MjMyNDY0OTI5ODUsIDI2Ljg5MTc4MzU2NzEzNDI3LCAyNi45NzE5NDM4ODc3NzU1NTIsIDI3LjA1MjEwNDIwODQxNjgzMiwgMjcuMTMyMjY0NTI5MDU4MTE2LCAyNy4yMTI0MjQ4NDk2OTk0LCAyNy4yOTI1ODUxNzAzNDA2ODMsIDI3LjM3Mjc0NTQ5MDk4MTk2MywgMjcuNDUyOTA1ODExNjIzMjQ2LCAyNy41MzMwNjYxMzIyNjQ1MywgMjcuNjEzMjI2NDUyOTA1ODEzLCAyNy42OTMzODY3NzM1NDcwOTMsIDI3Ljc3MzU0NzA5NDE4ODM3NywgMjcuODUzNzA3NDE0ODI5NjYsIDI3LjkzMzg2NzczNTQ3MDk0LCAyOC4wMTQwMjgwNTYxMTIyMjQsIDI4LjA5NDE4ODM3Njc1MzUwNywgMjguMTc0MzQ4Njk3Mzk0NzksIDI4LjI1NDUwOTAxODAzNjA3LCAyOC4zMzQ2NjkzMzg2NzczNTQsIDI4LjQxNDgyOTY1OTMxODYzOCwgMjguNDk0OTg5OTc5OTU5OTIsIDI4LjU3NTE1MDMwMDYwMTIsIDI4LjY1NTMxMDYyMTI0MjQ4NSwgMjguNzM1NDcwOTQxODgzNzcsIDI4LjgxNTYzMTI2MjUyNTA1LCAyOC44OTU3OTE1ODMxNjYzMzIsIDI4Ljk3NTk1MTkwMzgwNzYxNiwgMjkuMDU2MTEyMjI0NDQ4OSwgMjkuMTM2MjcyNTQ1MDkwMTgsIDI5LjIxNjQzMjg2NTczMTQ2MywgMjkuMjk2NTkzMTg2MzcyNzQ2LCAyOS4zNzY3NTM1MDcwMTQwMywgMjkuNDU2OTEzODI3NjU1MzEsIDI5LjUzNzA3NDE0ODI5NjU5MywgMjkuNjE3MjM0NDY4OTM3ODc3LCAyOS42OTczOTQ3ODk1NzkxNTcsIDI5Ljc3NzU1NTExMDIyMDQ0LCAyOS44NTc3MTU0MzA4NjE3MjQsIDI5LjkzNzg3NTc1MTUwMzAwNywgMzAuMDE4MDM2MDcyMTQ0Mjg3LCAzMC4wOTgxOTYzOTI3ODU1NywgMzAuMTc4MzU2NzEzNDI2ODU0LCAzMC4yNTg1MTcwMzQwNjgxMzgsIDMwLjMzODY3NzM1NDcwOTQxOCwgMzAuNDE4ODM3Njc1MzUwNywgMzAuNDk4OTk3OTk1OTkxOTg1LCAzMC41NzkxNTgzMTY2MzMyNjUsIDMwLjY1OTMxODYzNzI3NDU1LCAzMC43Mzk0Nzg5NTc5MTU4MzIsIDMwLjgxOTYzOTI3ODU1NzExNiwgMzAuODk5Nzk5NTk5MTk4Mzk2LCAzMC45Nzk5NTk5MTk4Mzk2OCwgMzEuMDYwMTIwMjQwNDgwOTYzLCAzMS4xNDAyODA1NjExMjIyNDYsIDMxLjIyMDQ0MDg4MTc2MzUyNiwgMzEuMzAwNjAxMjAyNDA0ODEsIDMxLjM4MDc2MTUyMzA0NjA5MywgMzEuNDYwOTIxODQzNjg3MzczLCAzMS41NDEwODIxNjQzMjg2NTcsIDMxLjYyMTI0MjQ4NDk2OTk0LCAzMS43MDE0MDI4MDU2MTEyMjQsIDMxLjc4MTU2MzEyNjI1MjUwNCwgMzEuODYxNzIzNDQ2ODkzNzg3LCAzMS45NDE4ODM3Njc1MzUwNywgMzIuMDIyMDQ0MDg4MTc2MzYsIDMyLjEwMjIwNDQwODgxNzYzNCwgMzIuMTgyMzY0NzI5NDU4OTIsIDMyLjI2MjUyNTA1MDEwMDIsIDMyLjM0MjY4NTM3MDc0MTQ4LCAzMi40MjI4NDU2OTEzODI3NiwgMzIuNTAzMDA2MDEyMDI0MDQ1LCAzMi41ODMxNjYzMzI2NjUzMywgMzIuNjYzMzI2NjUzMzA2NjEsIDMyLjc0MzQ4Njk3Mzk0Nzg5NiwgMzIuODIzNjQ3Mjk0NTg5MTgsIDMyLjkwMzgwNzYxNTIzMDQ2LCAzMi45ODM5Njc5MzU4NzE3NDYsIDMzLjA2NDEyODI1NjUxMzAyLCAzMy4xNDQyODg1NzcxNTQzMDYsIDMzLjIyNDQ0ODg5Nzc5NTU5LCAzMy4zMDQ2MDkyMTg0MzY4NywgMzMuMzg0NzY5NTM5MDc4MTYsIDMzLjQ2NDkyOTg1OTcxOTQ0LCAzMy41NDUwOTAxODAzNjA3MjQsIDMzLjYyNTI1MDUwMTAwMjAxLCAzMy43MDU0MTA4MjE2NDMyODQsIDMzLjc4NTU3MTE0MjI4NDU3LCAzMy44NjU3MzE0NjI5MjU4NSwgMzMuOTQ1ODkxNzgzNTY3MTM0LCAzNC4wMjYwNTIxMDQyMDg0MiwgMzQuMTA2MjEyNDI0ODQ5NywgMzQuMTg2MzcyNzQ1NDkwOTg1LCAzNC4yNjY1MzMwNjYxMzIyNiwgMzQuMzQ2NjkzMzg2NzczNTQ1LCAzNC40MjY4NTM3MDc0MTQ4MywgMzQuNTA3MDE0MDI4MDU2MTEsIDM0LjU4NzE3NDM0ODY5NzM5NSwgMzQuNjY3MzM0NjY5MzM4NjgsIDM0Ljc0NzQ5NDk4OTk3OTk2LCAzNC44Mjc2NTUzMTA2MjEyNCwgMzQuOTA3ODE1NjMxMjYyNTIsIDM0Ljk4Nzk3NTk1MTkwMzgwNiwgMzUuMDY4MTM2MjcyNTQ1MDksIDM1LjE0ODI5NjU5MzE4NjM3LCAzNS4yMjg0NTY5MTM4Mjc2NiwgMzUuMzA4NjE3MjM0NDY4OTQsIDM1LjM4ODc3NzU1NTExMDIyNCwgMzUuNDY4OTM3ODc1NzUxNSwgMzUuNTQ5MDk4MTk2MzkyNzg0LCAzNS42MjkyNTg1MTcwMzQwNywgMzUuNzA5NDE4ODM3Njc1MzUsIDM1Ljc4OTU3OTE1ODMxNjYzNCwgMzUuODY5NzM5NDc4OTU3OTIsIDM1Ljk0OTg5OTc5OTU5OTIsIDM2LjAzMDA2MDEyMDI0MDQ4LCAzNi4xMTAyMjA0NDA4ODE3NiwgMzYuMTkwMzgwNzYxNTIzMDQ1LCAzNi4yNzA1NDEwODIxNjQzMywgMzYuMzUwNzAxNDAyODA1NjEsIDM2LjQzMDg2MTcyMzQ0Njg5NSwgMzYuNTExMDIyMDQ0MDg4MTgsIDM2LjU5MTE4MjM2NDcyOTQ1NSwgMzYuNjcxMzQyNjg1MzcwNzQsIDM2Ljc1MTUwMzAwNjAxMjAyLCAzNi44MzE2NjMzMjY2NTMzMDYsIDM2LjkxMTgyMzY0NzI5NDU5LCAzNi45OTE5ODM5Njc5MzU4NywgMzcuMDcyMTQ0Mjg4NTc3MTYsIDM3LjE1MjMwNDYwOTIxODQ0LCAzNy4yMzI0NjQ5Mjk4NTk3MiwgMzcuMzEyNjI1MjUwNTAxLCAzNy4zOTI3ODU1NzExNDIyODQsIDM3LjQ3Mjk0NTg5MTc4MzU3LCAzNy41NTMxMDYyMTI0MjQ4NSwgMzcuNjMzMjY2NTMzMDY2MTM0LCAzNy43MTM0MjY4NTM3MDc0MiwgMzcuNzkzNTg3MTc0MzQ4Njk0LCAzNy44NzM3NDc0OTQ5ODk5OCwgMzcuOTUzOTA3ODE1NjMxMjYsIDM4LjAzNDA2ODEzNjI3MjU0NSwgMzguMTE0MjI4NDU2OTEzODMsIDM4LjE5NDM4ODc3NzU1NTExLCAzOC4yNzQ1NDkwOTgxOTYzOTUsIDM4LjM1NDcwOTQxODgzNzY3LCAzOC40MzQ4Njk3Mzk0Nzg5NTUsIDM4LjUxNTAzMDA2MDEyMDI0LCAzOC41OTUxOTAzODA3NjE1MiwgMzguNjc1MzUwNzAxNDAyODA2LCAzOC43NTU1MTEwMjIwNDQwOSwgMzguODM1NjcxMzQyNjg1MzcsIDM4LjkxNTgzMTY2MzMyNjY2LCAzOC45OTU5OTE5ODM5Njc5MywgMzkuMDc2MTUyMzA0NjA5MjIsIDM5LjE1NjMxMjYyNTI1MDUsIDM5LjIzNjQ3Mjk0NTg5MTc4NCwgMzkuMzE2NjMzMjY2NTMzMDcsIDM5LjM5Njc5MzU4NzE3NDM1LCAzOS40NzY5NTM5MDc4MTU2MzQsIDM5LjU1NzExNDIyODQ1NjkxLCAzOS42MzcyNzQ1NDkwOTgxOTQsIDM5LjcxNzQzNDg2OTczOTQ4LCAzOS43OTc1OTUxOTAzODA3NiwgMzkuODc3NzU1NTExMDIyMDQ1LCAzOS45NTc5MTU4MzE2NjMzMywgNDAuMDM4MDc2MTUyMzA0NjEsIDQwLjExODIzNjQ3Mjk0NTg5LCA0MC4xOTgzOTY3OTM1ODcxNywgNDAuMjc4NTU3MTE0MjI4NDU1LCA0MC4zNTg3MTc0MzQ4Njk3NCwgNDAuNDM4ODc3NzU1NTExMDIsIDQwLjUxOTAzODA3NjE1MjMwNiwgNDAuNTk5MTk4Mzk2NzkzNTksIDQwLjY3OTM1ODcxNzQzNDg3LCA0MC43NTk1MTkwMzgwNzYxNSwgNDAuODM5Njc5MzU4NzE3NDMsIDQwLjkxOTgzOTY3OTM1ODcyLCA0MS4wXSkKICAgICAgICAgICAgICAucmFuZ2UoWycjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWQ5NzYnLCAnI2ZlZDk3NicsICcjZmVkOTc2JywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZlYjI0YycsICcjZmViMjRjJywgJyNmZWIyNGMnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2ZkOGQzYycsICcjZmQ4ZDNjJywgJyNmZDhkM2MnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjZjAzYjIwJywgJyNmMDNiMjAnLCAnI2YwM2IyMCcsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnLCAnI2JkMDAyNicsICcjYmQwMDI2JywgJyNiZDAwMjYnXSk7CiAgICAKCiAgICBjb2xvcl9tYXBfYjFhMWVmYzYyYTFjNDMwZTg0ZjU5NDVlZDA0NTdiYTAueCA9IGQzLnNjYWxlLmxpbmVhcigpCiAgICAgICAgICAgICAgLmRvbWFpbihbMS4wLCA0MS4wXSkKICAgICAgICAgICAgICAucmFuZ2UoWzAsIDQwMF0pOwoKICAgIGNvbG9yX21hcF9iMWExZWZjNjJhMWM0MzBlODRmNTk0NWVkMDQ1N2JhMC5sZWdlbmQgPSBMLmNvbnRyb2woe3Bvc2l0aW9uOiAndG9wcmlnaHQnfSk7CiAgICBjb2xvcl9tYXBfYjFhMWVmYzYyYTFjNDMwZTg0ZjU5NDVlZDA0NTdiYTAubGVnZW5kLm9uQWRkID0gZnVuY3Rpb24gKG1hcCkge3ZhciBkaXYgPSBMLkRvbVV0aWwuY3JlYXRlKCdkaXYnLCAnbGVnZW5kJyk7IHJldHVybiBkaXZ9OwogICAgY29sb3JfbWFwX2IxYTFlZmM2MmExYzQzMGU4NGY1OTQ1ZWQwNDU3YmEwLmxlZ2VuZC5hZGRUbyhtYXBfNGY3M2EyZmE4YzMwNDljYTg0MTIxZDZlNDc0NzBhNzMpOwoKICAgIGNvbG9yX21hcF9iMWExZWZjNjJhMWM0MzBlODRmNTk0NWVkMDQ1N2JhMC54QXhpcyA9IGQzLnN2Zy5heGlzKCkKICAgICAgICAuc2NhbGUoY29sb3JfbWFwX2IxYTFlZmM2MmExYzQzMGU4NGY1OTQ1ZWQwNDU3YmEwLngpCiAgICAgICAgLm9yaWVudCgidG9wIikKICAgICAgICAudGlja1NpemUoMSkKICAgICAgICAudGlja1ZhbHVlcyhbMSwgOCwgMTYsIDI0LCAzMiwgNDFdKTsKCiAgICBjb2xvcl9tYXBfYjFhMWVmYzYyYTFjNDMwZTg0ZjU5NDVlZDA0NTdiYTAuc3ZnID0gZDMuc2VsZWN0KCIubGVnZW5kLmxlYWZsZXQtY29udHJvbCIpLmFwcGVuZCgic3ZnIikKICAgICAgICAuYXR0cigiaWQiLCAnbGVnZW5kJykKICAgICAgICAuYXR0cigid2lkdGgiLCA0NTApCiAgICAgICAgLmF0dHIoImhlaWdodCIsIDQwKTsKCiAgICBjb2xvcl9tYXBfYjFhMWVmYzYyYTFjNDMwZTg0ZjU5NDVlZDA0NTdiYTAuZyA9IGNvbG9yX21hcF9iMWExZWZjNjJhMWM0MzBlODRmNTk0NWVkMDQ1N2JhMC5zdmcuYXBwZW5kKCJnIikKICAgICAgICAuYXR0cigiY2xhc3MiLCAia2V5IikKICAgICAgICAuYXR0cigidHJhbnNmb3JtIiwgInRyYW5zbGF0ZSgyNSwxNikiKTsKCiAgICBjb2xvcl9tYXBfYjFhMWVmYzYyYTFjNDMwZTg0ZjU5NDVlZDA0NTdiYTAuZy5zZWxlY3RBbGwoInJlY3QiKQogICAgICAgIC5kYXRhKGNvbG9yX21hcF9iMWExZWZjNjJhMWM0MzBlODRmNTk0NWVkMDQ1N2JhMC5jb2xvci5yYW5nZSgpLm1hcChmdW5jdGlvbihkLCBpKSB7CiAgICAgICAgICByZXR1cm4gewogICAgICAgICAgICB4MDogaSA/IGNvbG9yX21hcF9iMWExZWZjNjJhMWM0MzBlODRmNTk0NWVkMDQ1N2JhMC54KGNvbG9yX21hcF9iMWExZWZjNjJhMWM0MzBlODRmNTk0NWVkMDQ1N2JhMC5jb2xvci5kb21haW4oKVtpIC0gMV0pIDogY29sb3JfbWFwX2IxYTFlZmM2MmExYzQzMGU4NGY1OTQ1ZWQwNDU3YmEwLngucmFuZ2UoKVswXSwKICAgICAgICAgICAgeDE6IGkgPCBjb2xvcl9tYXBfYjFhMWVmYzYyYTFjNDMwZTg0ZjU5NDVlZDA0NTdiYTAuY29sb3IuZG9tYWluKCkubGVuZ3RoID8gY29sb3JfbWFwX2IxYTFlZmM2MmExYzQzMGU4NGY1OTQ1ZWQwNDU3YmEwLngoY29sb3JfbWFwX2IxYTFlZmM2MmExYzQzMGU4NGY1OTQ1ZWQwNDU3YmEwLmNvbG9yLmRvbWFpbigpW2ldKSA6IGNvbG9yX21hcF9iMWExZWZjNjJhMWM0MzBlODRmNTk0NWVkMDQ1N2JhMC54LnJhbmdlKClbMV0sCiAgICAgICAgICAgIHo6IGQKICAgICAgICAgIH07CiAgICAgICAgfSkpCiAgICAgIC5lbnRlcigpLmFwcGVuZCgicmVjdCIpCiAgICAgICAgLmF0dHIoImhlaWdodCIsIDEwKQogICAgICAgIC5hdHRyKCJ4IiwgZnVuY3Rpb24oZCkgeyByZXR1cm4gZC54MDsgfSkKICAgICAgICAuYXR0cigid2lkdGgiLCBmdW5jdGlvbihkKSB7IHJldHVybiBkLngxIC0gZC54MDsgfSkKICAgICAgICAuc3R5bGUoImZpbGwiLCBmdW5jdGlvbihkKSB7IHJldHVybiBkLno7IH0pOwoKICAgIGNvbG9yX21hcF9iMWExZWZjNjJhMWM0MzBlODRmNTk0NWVkMDQ1N2JhMC5nLmNhbGwoY29sb3JfbWFwX2IxYTFlZmM2MmExYzQzMGU4NGY1OTQ1ZWQwNDU3YmEwLnhBeGlzKS5hcHBlbmQoInRleHQiKQogICAgICAgIC5hdHRyKCJjbGFzcyIsICJjYXB0aW9uIikKICAgICAgICAuYXR0cigieSIsIDIxKQogICAgICAgIC50ZXh0KCdGcmVkZXJpY3RvbiBOZWlnaGJvdXJob29kcycpOwogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzQyY2I4NzUyMGY3OTQ5M2I5YTU3MGU4ZDk4OWRkZmQ2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDUuOTMxMTQzLC02Ni42NTI3XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiAxMCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80ZjczYTJmYThjMzA0OWNhODQxMjFkNmU0NzQ3MGE3Myk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9jYjkyZjJkYTUyMWY0ZmY4YWU5ZGY2MThhOGNhZDlhOCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mZGNjMGU0YWE5YTI0M2I2OGMyZmNkNTI1YTVjNTU4ZiA9ICQoJzxkaXYgaWQ9Imh0bWxfZmRjYzBlNGFhOWEyNDNiNjhjMmZjZDUyNWE1YzU1OGYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPktub3dsZWRnZSBQYXJrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9jYjkyZjJkYTUyMWY0ZmY4YWU5ZGY2MThhOGNhZDlhOC5zZXRDb250ZW50KGh0bWxfZmRjYzBlNGFhOWEyNDNiNjhjMmZjZDUyNWE1YzU1OGYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNDJjYjg3NTIwZjc5NDkzYjlhNTcwZThkOTg5ZGRmZDYuYmluZFBvcHVwKHBvcHVwX2NiOTJmMmRhNTIxZjRmZjhhZTlkZjYxOGE4Y2FkOWE4KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzMyMjc0ZGJmMDAxMDQzYzZiNDdhMjk4ZGU3MDk3NjYwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDUuOTQ4NTEyLC02Ni42NTYwNDVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDEwLAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzRmNzNhMmZhOGMzMDQ5Y2E4NDEyMWQ2ZTQ3NDcwYTczKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzFlN2UxZGQxOTY1ODRmYWNhZDA1MjZjYjA5NGZlNzA5ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzAxMTVhYTFhOGEzZjQzY2E5OGJmMDBlMDcyMTEyNTA3ID0gJCgnPGRpdiBpZD0iaHRtbF8wMTE1YWExYThhM2Y0M2NhOThiZjAwZTA3MjExMjUwNyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RnJlZGVyaWN0b24gSGlsbDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMWU3ZTFkZDE5NjU4NGZhY2FkMDUyNmNiMDk0ZmU3MDkuc2V0Q29udGVudChodG1sXzAxMTVhYTFhOGEzZjQzY2E5OGJmMDBlMDcyMTEyNTA3KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzMyMjc0ZGJmMDAxMDQzYzZiNDdhMjk4ZGU3MDk3NjYwLmJpbmRQb3B1cChwb3B1cF8xZTdlMWRkMTk2NTg0ZmFjYWQwNTI2Y2IwOTRmZTcwOSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9jOWE1Y2FlNjI4MGM0YmExODljYTViN2Y4MjE5ZDEwYyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQ1Ljk4MzM4MiwtNjYuNjQ0ODU2XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiAxMCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80ZjczYTJmYThjMzA0OWNhODQxMjFkNmU0NzQ3MGE3Myk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8xN2JjODA0ODdhMTk0Njc2YjYyNjI5ZjczYjdiZGJmMyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8xM2NlOGNlNWFkNmE0NTQ1YTc3YjQ0NDQzOTgwNWQ0MCA9ICQoJzxkaXYgaWQ9Imh0bWxfMTNjZThjZTVhZDZhNDU0NWE3N2I0NDQ0Mzk4MDVkNDAiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk5hc2h3YWFrc2lzPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8xN2JjODA0ODdhMTk0Njc2YjYyNjI5ZjczYjdiZGJmMy5zZXRDb250ZW50KGh0bWxfMTNjZThjZTVhZDZhNDU0NWE3N2I0NDQ0Mzk4MDVkNDApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYzlhNWNhZTYyODBjNGJhMTg5Y2E1YjdmODIxOWQxMGMuYmluZFBvcHVwKHBvcHVwXzE3YmM4MDQ4N2ExOTQ2NzZiNjI2MjlmNzNiN2JkYmYzKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzRlZWRkMmZkOWQ2YTQwZjJiMjhhNzBmNjg1MDJiNGQ5ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDUuOTQ4MTIxLC02Ni42NDE0MDZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDEwLAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzRmNzNhMmZhOGMzMDQ5Y2E4NDEyMWQ2ZTQ3NDcwYTczKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzRjZjg4ZDYzYzUxYjQ4ZDNhZGEyNGI1YTBhNzViYzNkID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzAzODNhZjM5ZGQzNzRlOGY5MzBmZTlhYTM4MzkwNzg0ID0gJCgnPGRpdiBpZD0iaHRtbF8wMzgzYWYzOWRkMzc0ZThmOTMwZmU5YWEzODM5MDc4NCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VW5pdmVyc2l0eSBvZiBOZXcgQnJ1bnN3aWNrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF80Y2Y4OGQ2M2M1MWI0OGQzYWRhMjRiNWEwYTc1YmMzZC5zZXRDb250ZW50KGh0bWxfMDM4M2FmMzlkZDM3NGU4ZjkzMGZlOWFhMzgzOTA3ODQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNGVlZGQyZmQ5ZDZhNDBmMmIyOGE3MGY2ODUwMmI0ZDkuYmluZFBvcHVwKHBvcHVwXzRjZjg4ZDYzYzUxYjQ4ZDNhZGEyNGI1YTBhNzViYzNkKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2M5NzkxOTZjOTk1YzRhNzFiZTZmZjg2MTY0ZjY0M2YwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDUuOTY4ODAyLC02Ni42MjI3MzhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDEwLAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzRmNzNhMmZhOGMzMDQ5Y2E4NDEyMWQ2ZTQ3NDcwYTczKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2VlYjI5MTBhYjFhZDQ0NDM4ODY1YzhkZGUxMTI2Yjk1ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2Y4NTQ1MjRmMDhjYTQ2YmU4ZWRmZGIyZjg1NmYzODE3ID0gJCgnPGRpdiBpZD0iaHRtbF9mODU0NTI0ZjA4Y2E0NmJlOGVkZmRiMmY4NTZmMzgxNyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RGV2b248L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2VlYjI5MTBhYjFhZDQ0NDM4ODY1YzhkZGUxMTI2Yjk1LnNldENvbnRlbnQoaHRtbF9mODU0NTI0ZjA4Y2E0NmJlOGVkZmRiMmY4NTZmMzgxNyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9jOTc5MTk2Yzk5NWM0YTcxYmU2ZmY4NjE2NGY2NDNmMC5iaW5kUG9wdXAocG9wdXBfZWViMjkxMGFiMWFkNDQ0Mzg4NjVjOGRkZTExMjZiOTUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMWRmNDdiZGM3NzQ3NDExNmIyNjUwODNjN2M2ZDVhMTAgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0NS44OTI3OTUsLTY2LjY4MzY3M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogMTAsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNGY3M2EyZmE4YzMwNDljYTg0MTIxZDZlNDc0NzBhNzMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMWU4OGI4NWM1Y2YxNGJiNjljYjYyNTFkMGVmOTFhYjYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZTM2YTJiMjE1Mjk4NDc3MWI0MGZmNTkzMzRhNTVkMjcgPSAkKCc8ZGl2IGlkPSJodG1sX2UzNmEyYjIxNTI5ODQ3NzFiNDBmZjU5MzM0YTU1ZDI3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5OZXcgTWFyeWxhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzFlODhiODVjNWNmMTRiYjY5Y2I2MjUxZDBlZjkxYWI2LnNldENvbnRlbnQoaHRtbF9lMzZhMmIyMTUyOTg0NzcxYjQwZmY1OTMzNGE1NWQyNyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8xZGY0N2JkYzc3NDc0MTE2YjI2NTA4M2M3YzZkNWExMC5iaW5kUG9wdXAocG9wdXBfMWU4OGI4NWM1Y2YxNGJiNjljYjYyNTFkMGVmOTFhYjYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfM2E0ZmY0MTI4Nzk1NDJjMGI0NzBjZDE1ZDM1ZThlYjMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0NS45Nzg5MTMsLTY2LjU4OTQ5MV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogMTAsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNGY3M2EyZmE4YzMwNDljYTg0MTIxZDZlNDc0NzBhNzMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYTRiNTA5ZWQ5MzdhNDUzYzgyMDJlNjRjMzk4ZDUwZTAgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYzMxYTgyMDFhZGIyNDU2YWJhNTlhMTRlZmUyZmIzNTAgPSAkKCc8ZGl2IGlkPSJodG1sX2MzMWE4MjAxYWRiMjQ1NmFiYTU5YTE0ZWZlMmZiMzUwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5NYXJ5c3ZpbGxlPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hNGI1MDllZDkzN2E0NTNjODIwMmU2NGMzOThkNTBlMC5zZXRDb250ZW50KGh0bWxfYzMxYTgyMDFhZGIyNDU2YWJhNTlhMTRlZmUyZmIzNTApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfM2E0ZmY0MTI4Nzk1NDJjMGI0NzBjZDE1ZDM1ZThlYjMuYmluZFBvcHVwKHBvcHVwX2E0YjUwOWVkOTM3YTQ1M2M4MjAyZTY0YzM5OGQ1MGUwKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzNjOTU4NzQ0ZWM4ZjRiMDY5ZDljZGY5NWMwZjc0NTllID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDUuOTMxODI3LC02Ni42NDAzMzldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDEwLAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzRmNzNhMmZhOGMzMDQ5Y2E4NDEyMWQ2ZTQ3NDcwYTczKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2IwZGRkNmU3OTRiOTQxY2Q5NjZjZmY5Zjg5ZjdhNDUyID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzkzMTY2MGNhY2ViYjQ4YmE5ZGJhYzYxMjE1NDlkNzQ5ID0gJCgnPGRpdiBpZD0iaHRtbF85MzE2NjBjYWNlYmI0OGJhOWRiYWM2MTIxNTQ5ZDc0OSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+U2t5bGluZSBBY3JlczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYjBkZGQ2ZTc5NGI5NDFjZDk2NmNmZjlmODlmN2E0NTIuc2V0Q29udGVudChodG1sXzkzMTY2MGNhY2ViYjQ4YmE5ZGJhYzYxMjE1NDlkNzQ5KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzNjOTU4NzQ0ZWM4ZjRiMDY5ZDljZGY5NWMwZjc0NTllLmJpbmRQb3B1cChwb3B1cF9iMGRkZDZlNzk0Yjk0MWNkOTY2Y2ZmOWY4OWY3YTQ1Mik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9mYmQ4YmI3ZTI2MDM0Nzg3ODU1NjQ3ODQxZmM3OWVlYSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQ1LjkwMjMxNSwtNjYuNzU1MTEzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiAxMCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80ZjczYTJmYThjMzA0OWNhODQxMjFkNmU0NzQ3MGE3Myk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9iODM5Y2NjNTE4Nzk0YmYxOTAwNjAxMzI5NjUyMDQxYSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8yZWM5ZGQzNDZlOWE0Nzg1YTI2MGEwZjFjZjYwMjA3OCA9ICQoJzxkaXYgaWQ9Imh0bWxfMmVjOWRkMzQ2ZTlhNDc4NWEyNjBhMGYxY2Y2MDIwNzgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkhhbndlbGw8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2I4MzljY2M1MTg3OTRiZjE5MDA2MDEzMjk2NTIwNDFhLnNldENvbnRlbnQoaHRtbF8yZWM5ZGQzNDZlOWE0Nzg1YTI2MGEwZjFjZjYwMjA3OCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9mYmQ4YmI3ZTI2MDM0Nzg3ODU1NjQ3ODQxZmM3OWVlYS5iaW5kUG9wdXAocG9wdXBfYjgzOWNjYzUxODc5NGJmMTkwMDYwMTMyOTY1MjA0MWEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOTZhNGFlOWE5Y2FhNGFlNWJjMjAwZTdhNjVhNTIxNDQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0NS45NTgzMjcsLTY2LjY0NzIxMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogMTAsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNGY3M2EyZmE4YzMwNDljYTg0MTIxZDZlNDc0NzBhNzMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNDM5MWE1Y2E3YmJhNDcxMjlmYzZhODkwNjBhNjA5YWIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOTBjMTk1Y2FjYjlhNGFlY2E3N2I2NWY3MDZhNjI1MTAgPSAkKCc8ZGl2IGlkPSJodG1sXzkwYzE5NWNhY2I5YTRhZWNhNzdiNjVmNzA2YTYyNTEwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Eb3dudG93bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNDM5MWE1Y2E3YmJhNDcxMjlmYzZhODkwNjBhNjA5YWIuc2V0Q29udGVudChodG1sXzkwYzE5NWNhY2I5YTRhZWNhNzdiNjVmNzA2YTYyNTEwKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzk2YTRhZTlhOWNhYTRhZTViYzIwMGU3YTY1YTUyMTQ0LmJpbmRQb3B1cChwb3B1cF80MzkxYTVjYTdiYmE0NzEyOWZjNmE4OTA2MGE2MDlhYik7CgogICAgICAgICAgICAKICAgICAgICAKPC9zY3JpcHQ+" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>




```python

```

## Explore Fredericton Neighbourhoods
#### Define Foursquare Credentials and Version


```python
CLIENT_ID = 'Nope' # your Foursquare ID
CLIENT_SECRET = 'Secret' # your Foursquare Secret
VERSION = '20181201' # Foursquare API version

print('Your credentails:')
print('CLIENT_ID: ' + CLIENT_ID)
print('CLIENT_SECRET:' + CLIENT_SECRET)
```

    Your credentails:
    CLIENT_ID: Nope
    CLIENT_SECRET:Secret


## Let's take a look at nearby venues


```python
def getNearbyVenues(names, latitudes, longitudes, radius=1000, LIMIT=100):
    
    venues_list=[]
    for name, lat, lng in zip(names, latitudes, longitudes):
        print(name)
            
        # create the API request URL
        url = 'https://api.foursquare.com/v2/venues/explore?&client_id={}&client_secret={}&v={}&ll={},{}&radius={}&limit={}'.format(
            CLIENT_ID, 
            CLIENT_SECRET, 
            VERSION, 
            lat, 
            lng, 
            radius, 
            LIMIT)
            
        # make the GET request
        results = requests.get(url).json()["response"]['groups'][0]['items']
        
        # return only relevant information for each nearby venue
        venues_list.append([(
            name, 
            lat, 
            lng,            
            v['venue']['name'], 
            v['venue']['id'],
            v['venue']['location']['lat'], 
            v['venue']['location']['lng'],  
            v['venue']['categories'][0]['name']) for v in results])

    nearby_venues = pd.DataFrame([item for venue_list in venues_list for item in venue_list])
    nearby_venues.columns = ['Location', 
                  'Location Latitude', 
                  'Location Longitude', 
                  'Venue',
                  'Venue id',                
                  'Venue Latitude', 
                  'Venue Longitude', 
                  'Venue Category'        
                   ]
    
    return(nearby_venues)
```


```python
fredericton_data_venues = getNearbyVenues(names=location_df['Location'],
                                   latitudes=location_df['Latitude'],
                                   longitudes=location_df['Longitude']
                                  )
```

    Knowledge Park
    Fredericton Hill
    Nashwaaksis
    University of New Brunswick
    Devon
    New Maryland
    Marysville
    Skyline Acres
    Hanwell
    Downtown



```python
print(fredericton_data_venues.shape)
fredericton_data_venues
```

    (166, 8)





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Location</th>
      <th>Location Latitude</th>
      <th>Location Longitude</th>
      <th>Venue</th>
      <th>Venue id</th>
      <th>Venue Latitude</th>
      <th>Venue Longitude</th>
      <th>Venue Category</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Knowledge Park</td>
      <td>45.931143</td>
      <td>-66.652700</td>
      <td>Costco Wholesale</td>
      <td>4e18ab92183880768f43bff6</td>
      <td>45.927034</td>
      <td>-66.663447</td>
      <td>Warehouse Store</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Knowledge Park</td>
      <td>45.931143</td>
      <td>-66.652700</td>
      <td>PetSmart</td>
      <td>4bbca501a0a0c9b6078f1a0f</td>
      <td>45.929768</td>
      <td>-66.659939</td>
      <td>Pet Store</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Knowledge Park</td>
      <td>45.931143</td>
      <td>-66.652700</td>
      <td>Montana's</td>
      <td>4e50406e62844166699b0780</td>
      <td>45.931511</td>
      <td>-66.662507</td>
      <td>Restaurant</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Knowledge Park</td>
      <td>45.931143</td>
      <td>-66.652700</td>
      <td>Boston Pizza</td>
      <td>4b64944af964a52041bf2ae3</td>
      <td>45.938123</td>
      <td>-66.660037</td>
      <td>Sports Bar</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Knowledge Park</td>
      <td>45.931143</td>
      <td>-66.652700</td>
      <td>Michaels</td>
      <td>4c489858417b20a13b82e1a9</td>
      <td>45.929965</td>
      <td>-66.659548</td>
      <td>Arts &amp; Crafts Store</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Knowledge Park</td>
      <td>45.931143</td>
      <td>-66.652700</td>
      <td>Alcool NB Liquor</td>
      <td>4b77335df964a5202c872ee3</td>
      <td>45.930680</td>
      <td>-66.664180</td>
      <td>Liquor Store</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Knowledge Park</td>
      <td>45.931143</td>
      <td>-66.652700</td>
      <td>Best Buy</td>
      <td>5520124a498e0467bb6e81c8</td>
      <td>45.937673</td>
      <td>-66.660380</td>
      <td>Electronics Store</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Knowledge Park</td>
      <td>45.931143</td>
      <td>-66.652700</td>
      <td>Wal-Mart</td>
      <td>4bad313ff964a5208c373be3</td>
      <td>45.934081</td>
      <td>-66.663539</td>
      <td>Big Box Store</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Knowledge Park</td>
      <td>45.931143</td>
      <td>-66.652700</td>
      <td>Booster Juice</td>
      <td>4c42414e520fa59334f9caac</td>
      <td>45.935198</td>
      <td>-66.663602</td>
      <td>Smoothie Shop</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Knowledge Park</td>
      <td>45.931143</td>
      <td>-66.652700</td>
      <td>Dairy Queen</td>
      <td>4b86f05bf964a52009a731e3</td>
      <td>45.938004</td>
      <td>-66.659442</td>
      <td>Fast Food Restaurant</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Knowledge Park</td>
      <td>45.931143</td>
      <td>-66.652700</td>
      <td>H&amp;M</td>
      <td>509c3265498efdffc5739a0f</td>
      <td>45.935196</td>
      <td>-66.663290</td>
      <td>Clothing Store</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Knowledge Park</td>
      <td>45.931143</td>
      <td>-66.652700</td>
      <td>Dairy Queen (Treat)</td>
      <td>4cc6123cbde8f04d9ce0b44b</td>
      <td>45.934520</td>
      <td>-66.663988</td>
      <td>Fast Food Restaurant</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Knowledge Park</td>
      <td>45.931143</td>
      <td>-66.652700</td>
      <td>Winners</td>
      <td>4caa46a744a8224b96e42640</td>
      <td>45.930427</td>
      <td>-66.659758</td>
      <td>Clothing Store</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Knowledge Park</td>
      <td>45.931143</td>
      <td>-66.652700</td>
      <td>East Side Mario's</td>
      <td>4b55d89bf964a520a2f227e3</td>
      <td>45.931376</td>
      <td>-66.663417</td>
      <td>Italian Restaurant</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Knowledge Park</td>
      <td>45.931143</td>
      <td>-66.652700</td>
      <td>McDonald's</td>
      <td>4c6e9ef665eda09377e951d0</td>
      <td>45.934575</td>
      <td>-66.663319</td>
      <td>Fast Food Restaurant</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Knowledge Park</td>
      <td>45.931143</td>
      <td>-66.652700</td>
      <td>Home Sense</td>
      <td>54024f60498ee424eedb7bf9</td>
      <td>45.930528</td>
      <td>-66.660103</td>
      <td>Department Store</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Knowledge Park</td>
      <td>45.931143</td>
      <td>-66.652700</td>
      <td>The Shoe company</td>
      <td>4bd76dfa5cf276b0fb469b00</td>
      <td>45.929636</td>
      <td>-66.660449</td>
      <td>Shoe Store</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Knowledge Park</td>
      <td>45.931143</td>
      <td>-66.652700</td>
      <td>Avalon Spa Uptown</td>
      <td>4cd99e0f51fc8cfa4369f05d</td>
      <td>45.930774</td>
      <td>-66.660927</td>
      <td>Spa</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Knowledge Park</td>
      <td>45.931143</td>
      <td>-66.652700</td>
      <td>Wicker Emporium</td>
      <td>4e6baff588772457c4fd1968</td>
      <td>45.930897</td>
      <td>-66.661338</td>
      <td>Furniture / Home Store</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Knowledge Park</td>
      <td>45.931143</td>
      <td>-66.652700</td>
      <td>Dollarama</td>
      <td>4ba3dd18f964a520d86738e3</td>
      <td>45.930897</td>
      <td>-66.661714</td>
      <td>Discount Store</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Knowledge Park</td>
      <td>45.931143</td>
      <td>-66.652700</td>
      <td>Bed Bath &amp; Beyond</td>
      <td>5083f283e4b0bf87c15e9ea1</td>
      <td>45.930097</td>
      <td>-66.662166</td>
      <td>Furniture / Home Store</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Knowledge Park</td>
      <td>45.931143</td>
      <td>-66.652700</td>
      <td>GAP Factory Store</td>
      <td>50a8f005e4b0e4f42e033a2a</td>
      <td>45.930211</td>
      <td>-66.662416</td>
      <td>Clothing Store</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Knowledge Park</td>
      <td>45.931143</td>
      <td>-66.652700</td>
      <td>carter's | OshKosh B'gosh</td>
      <td>50a51363e4b0a3e2f7db76bf</td>
      <td>45.929978</td>
      <td>-66.662966</td>
      <td>Kids Store</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Knowledge Park</td>
      <td>45.931143</td>
      <td>-66.652700</td>
      <td>Deluxe Fish &amp; Chips</td>
      <td>4e5d0b99fa76a4cf148d9a15</td>
      <td>45.931722</td>
      <td>-66.663131</td>
      <td>Seafood Restaurant</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Knowledge Park</td>
      <td>45.931143</td>
      <td>-66.652700</td>
      <td>Hallmark</td>
      <td>4cd96cf651fc8cfa522eef5d</td>
      <td>45.930646</td>
      <td>-66.663745</td>
      <td>Gift Shop</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Knowledge Park</td>
      <td>45.931143</td>
      <td>-66.652700</td>
      <td>NB Liquor</td>
      <td>5985f08b6cf01a7e38b85fba</td>
      <td>45.930228</td>
      <td>-66.664395</td>
      <td>Liquor Store</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Knowledge Park</td>
      <td>45.931143</td>
      <td>-66.652700</td>
      <td>Corbett Center</td>
      <td>57854d05498e301b3b5a4448</td>
      <td>45.929733</td>
      <td>-66.664601</td>
      <td>Shopping Plaza</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Knowledge Park</td>
      <td>45.931143</td>
      <td>-66.652700</td>
      <td>Costco Food Court</td>
      <td>53693053498ef3e4ea63560f</td>
      <td>45.927383</td>
      <td>-66.663544</td>
      <td>Fast Food Restaurant</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Knowledge Park</td>
      <td>45.931143</td>
      <td>-66.652700</td>
      <td>Sleep Country</td>
      <td>555b5660498eae864c440e77</td>
      <td>45.929074</td>
      <td>-66.664605</td>
      <td>Mattress Store</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Knowledge Park</td>
      <td>45.931143</td>
      <td>-66.652700</td>
      <td>Sport Chek Regent Mall</td>
      <td>4ca4ecae8a65bfb717422b22</td>
      <td>45.935211</td>
      <td>-66.663525</td>
      <td>Sporting Goods Shop</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Knowledge Park</td>
      <td>45.931143</td>
      <td>-66.652700</td>
      <td>Rôtisserie St-Hubert</td>
      <td>57164569498e9bb9e88d52b0</td>
      <td>45.929838</td>
      <td>-66.664749</td>
      <td>Restaurant</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Fredericton Hill</td>
      <td>45.948512</td>
      <td>-66.656045</td>
      <td>YMCA Fredericton</td>
      <td>4e93476b8231bf0d17ba3e24</td>
      <td>45.953217</td>
      <td>-66.649478</td>
      <td>Gym</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Fredericton Hill</td>
      <td>45.948512</td>
      <td>-66.656045</td>
      <td>20 Twenty Club</td>
      <td>4c5388b0f5f3d13ac74ba5f8</td>
      <td>45.951042</td>
      <td>-66.648112</td>
      <td>Bar</td>
    </tr>
    <tr>
      <th>33</th>
      <td>Fredericton Hill</td>
      <td>45.948512</td>
      <td>-66.656045</td>
      <td>Shoppers Drug Mart</td>
      <td>4fb699dc7bebbeb2a6c7ba88</td>
      <td>45.942627</td>
      <td>-66.655523</td>
      <td>Pharmacy</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Fredericton Hill</td>
      <td>45.948512</td>
      <td>-66.656045</td>
      <td>Subway</td>
      <td>4bae3571f964a52076923be3</td>
      <td>45.940931</td>
      <td>-66.657445</td>
      <td>Sandwich Place</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Fredericton Hill</td>
      <td>45.948512</td>
      <td>-66.656045</td>
      <td>Canadian Tire</td>
      <td>4bb52ba72ea19521201caa2f</td>
      <td>45.944409</td>
      <td>-66.666820</td>
      <td>Hardware Store</td>
    </tr>
    <tr>
      <th>36</th>
      <td>Fredericton Hill</td>
      <td>45.948512</td>
      <td>-66.656045</td>
      <td>Tim Hortons</td>
      <td>4dc29f89d4c07da169fbf84b</td>
      <td>45.943720</td>
      <td>-66.646907</td>
      <td>Coffee Shop</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Fredericton Hill</td>
      <td>45.948512</td>
      <td>-66.656045</td>
      <td>The Aitken University Centre - UNB</td>
      <td>4b6458eff964a52052ac2ae3</td>
      <td>45.941644</td>
      <td>-66.663667</td>
      <td>Hockey Arena</td>
    </tr>
    <tr>
      <th>38</th>
      <td>Fredericton Hill</td>
      <td>45.948512</td>
      <td>-66.656045</td>
      <td>Queen Square Park</td>
      <td>4b7acb0ef964a520113d2fe3</td>
      <td>45.950961</td>
      <td>-66.648245</td>
      <td>Park</td>
    </tr>
    <tr>
      <th>39</th>
      <td>Fredericton Hill</td>
      <td>45.948512</td>
      <td>-66.656045</td>
      <td>Great Canadian Bagel</td>
      <td>4b784edbf964a52013c42ee3</td>
      <td>45.941040</td>
      <td>-66.657545</td>
      <td>Bakery</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Fredericton Hill</td>
      <td>45.948512</td>
      <td>-66.656045</td>
      <td>Monkey Cakes</td>
      <td>4ec147368231b62f43026067</td>
      <td>45.940938</td>
      <td>-66.657346</td>
      <td>Bakery</td>
    </tr>
    <tr>
      <th>41</th>
      <td>Fredericton Hill</td>
      <td>45.948512</td>
      <td>-66.656045</td>
      <td>Papa John's Pizza</td>
      <td>4ecc29f59adfd1f5b5c7bbb1</td>
      <td>45.956655</td>
      <td>-66.657285</td>
      <td>Pizza Place</td>
    </tr>
    <tr>
      <th>42</th>
      <td>Fredericton Hill</td>
      <td>45.948512</td>
      <td>-66.656045</td>
      <td>Greco</td>
      <td>4cfc0660c51fa1cdd3d7e92b</td>
      <td>45.954055</td>
      <td>-66.647290</td>
      <td>Pizza Place</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Fredericton Hill</td>
      <td>45.948512</td>
      <td>-66.656045</td>
      <td>Dick's Grocery Store</td>
      <td>4c545e5db426ef3b11cc7e8a</td>
      <td>45.941957</td>
      <td>-66.663877</td>
      <td>Smoke Shop</td>
    </tr>
    <tr>
      <th>44</th>
      <td>Fredericton Hill</td>
      <td>45.948512</td>
      <td>-66.656045</td>
      <td>Tingley's Ice Cream</td>
      <td>4c13c001b7b9c9284e12aa37</td>
      <td>45.957087</td>
      <td>-66.655855</td>
      <td>Ice Cream Shop</td>
    </tr>
    <tr>
      <th>45</th>
      <td>Fredericton Hill</td>
      <td>45.948512</td>
      <td>-66.656045</td>
      <td>Domino's Pizza</td>
      <td>50f9bbc75d24acebc259244d</td>
      <td>45.957177</td>
      <td>-66.656638</td>
      <td>Pizza Place</td>
    </tr>
    <tr>
      <th>46</th>
      <td>Fredericton Hill</td>
      <td>45.948512</td>
      <td>-66.656045</td>
      <td>Jumbo Video</td>
      <td>4bc0d29a920eb71307a2192c</td>
      <td>45.957286</td>
      <td>-66.656312</td>
      <td>Video Store</td>
    </tr>
    <tr>
      <th>47</th>
      <td>Fredericton Hill</td>
      <td>45.948512</td>
      <td>-66.656045</td>
      <td>Goody Shop</td>
      <td>4b8580edf964a5201d6231e3</td>
      <td>45.951172</td>
      <td>-66.644000</td>
      <td>Bakery</td>
    </tr>
    <tr>
      <th>48</th>
      <td>Nashwaaksis</td>
      <td>45.983382</td>
      <td>-66.644856</td>
      <td>Peters Meat, Seafood &amp; Lobster Market</td>
      <td>4c4e04ecfb742d7fe7bba62d</td>
      <td>45.976652</td>
      <td>-66.649765</td>
      <td>Grocery Store</td>
    </tr>
    <tr>
      <th>49</th>
      <td>Nashwaaksis</td>
      <td>45.983382</td>
      <td>-66.644856</td>
      <td>Tim Hortons</td>
      <td>4b742f31f964a520b7cb2de3</td>
      <td>45.975294</td>
      <td>-66.646977</td>
      <td>Coffee Shop</td>
    </tr>
    <tr>
      <th>50</th>
      <td>Nashwaaksis</td>
      <td>45.983382</td>
      <td>-66.644856</td>
      <td>The Northside Market</td>
      <td>50270b2ae4b042eaf816ee61</td>
      <td>45.977779</td>
      <td>-66.635003</td>
      <td>Farmers Market</td>
    </tr>
    <tr>
      <th>51</th>
      <td>Nashwaaksis</td>
      <td>45.983382</td>
      <td>-66.644856</td>
      <td>Shoppers Drug Mart</td>
      <td>4c745e08db52b1f781f775dc</td>
      <td>45.976515</td>
      <td>-66.648534</td>
      <td>Pharmacy</td>
    </tr>
    <tr>
      <th>52</th>
      <td>Nashwaaksis</td>
      <td>45.983382</td>
      <td>-66.644856</td>
      <td>Subway</td>
      <td>4bc5db23693695213a9a8488</td>
      <td>45.976886</td>
      <td>-66.648661</td>
      <td>Sandwich Place</td>
    </tr>
    <tr>
      <th>53</th>
      <td>Nashwaaksis</td>
      <td>45.983382</td>
      <td>-66.644856</td>
      <td>Subway</td>
      <td>4c87f3b4bf40a1cd09fd08b4</td>
      <td>45.989114</td>
      <td>-66.652061</td>
      <td>Sandwich Place</td>
    </tr>
    <tr>
      <th>54</th>
      <td>Nashwaaksis</td>
      <td>45.983382</td>
      <td>-66.644856</td>
      <td>Kentucky Fried Chicken</td>
      <td>4eefb90ba69ddc7bcb336081</td>
      <td>45.975903</td>
      <td>-66.646846</td>
      <td>Fast Food Restaurant</td>
    </tr>
    <tr>
      <th>55</th>
      <td>Nashwaaksis</td>
      <td>45.983382</td>
      <td>-66.644856</td>
      <td>Nashwaaksis Field House</td>
      <td>4b73436cf964a52016a52de3</td>
      <td>45.984849</td>
      <td>-66.643635</td>
      <td>Gym</td>
    </tr>
    <tr>
      <th>56</th>
      <td>Nashwaaksis</td>
      <td>45.983382</td>
      <td>-66.644856</td>
      <td>KFC</td>
      <td>4c9267139199bfb7786c14df</td>
      <td>45.975907</td>
      <td>-66.646870</td>
      <td>Fast Food Restaurant</td>
    </tr>
    <tr>
      <th>57</th>
      <td>Nashwaaksis</td>
      <td>45.983382</td>
      <td>-66.644856</td>
      <td>Tim Hortons</td>
      <td>4c0104cf360a9c74bb11d9a0</td>
      <td>45.989221</td>
      <td>-66.652208</td>
      <td>Coffee Shop</td>
    </tr>
    <tr>
      <th>58</th>
      <td>Nashwaaksis</td>
      <td>45.983382</td>
      <td>-66.644856</td>
      <td>Thai spice</td>
      <td>503658e5e4b00b386cc5d972</td>
      <td>45.975890</td>
      <td>-66.647424</td>
      <td>Thai Restaurant</td>
    </tr>
    <tr>
      <th>59</th>
      <td>Nashwaaksis</td>
      <td>45.983382</td>
      <td>-66.644856</td>
      <td>Mike's Old Fashioned Bakery</td>
      <td>4d67fde7709bb60c5eacb014</td>
      <td>45.976560</td>
      <td>-66.650030</td>
      <td>Bakery</td>
    </tr>
    <tr>
      <th>60</th>
      <td>Nashwaaksis</td>
      <td>45.983382</td>
      <td>-66.644856</td>
      <td>Cox Electronics</td>
      <td>4d07eab6611ff04d4f4718fb</td>
      <td>45.976112</td>
      <td>-66.649222</td>
      <td>Electronics Store</td>
    </tr>
    <tr>
      <th>61</th>
      <td>Nashwaaksis</td>
      <td>45.983382</td>
      <td>-66.644856</td>
      <td>A Pile Of Scrap!</td>
      <td>4e9f0e9b93ad5d11f3d36ba1</td>
      <td>45.984398</td>
      <td>-66.633329</td>
      <td>Arts &amp; Crafts Store</td>
    </tr>
    <tr>
      <th>62</th>
      <td>Nashwaaksis</td>
      <td>45.983382</td>
      <td>-66.644856</td>
      <td>Jim Gilberts Wheels And Deals</td>
      <td>4b9a7ef5f964a520b6ba35e3</td>
      <td>45.980784</td>
      <td>-66.633311</td>
      <td>Auto Dealership</td>
    </tr>
    <tr>
      <th>63</th>
      <td>Nashwaaksis</td>
      <td>45.983382</td>
      <td>-66.644856</td>
      <td>Trailway Brewery</td>
      <td>574a1b86cd10af189e38500e</td>
      <td>45.975442</td>
      <td>-66.649496</td>
      <td>Beer Store</td>
    </tr>
    <tr>
      <th>64</th>
      <td>Nashwaaksis</td>
      <td>45.983382</td>
      <td>-66.644856</td>
      <td>The North Side Market</td>
      <td>501c19f7e4b01c57ff1b1212</td>
      <td>45.977837</td>
      <td>-66.635168</td>
      <td>Farmers Market</td>
    </tr>
    <tr>
      <th>65</th>
      <td>Nashwaaksis</td>
      <td>45.983382</td>
      <td>-66.644856</td>
      <td>Avalon SalonSpa</td>
      <td>4bc31784920eb71312ec1c2c</td>
      <td>45.974591</td>
      <td>-66.644756</td>
      <td>Spa</td>
    </tr>
    <tr>
      <th>66</th>
      <td>Nashwaaksis</td>
      <td>45.983382</td>
      <td>-66.644856</td>
      <td>Tony Pepperoni</td>
      <td>4c88f56dbbec6dcbe9f2d758</td>
      <td>45.991888</td>
      <td>-66.648599</td>
      <td>Pizza Place</td>
    </tr>
    <tr>
      <th>67</th>
      <td>University of New Brunswick</td>
      <td>45.948121</td>
      <td>-66.641406</td>
      <td>The Richard J. CURRIE Center - UNB</td>
      <td>4dbae5806e815ab0de5d2637</td>
      <td>45.946698</td>
      <td>-66.637891</td>
      <td>Basketball Court</td>
    </tr>
    <tr>
      <th>68</th>
      <td>University of New Brunswick</td>
      <td>45.948121</td>
      <td>-66.641406</td>
      <td>Charlotte Street Arts Centre</td>
      <td>4b7f0318f964a5203d1030e3</td>
      <td>45.955620</td>
      <td>-66.639324</td>
      <td>Art Gallery</td>
    </tr>
    <tr>
      <th>69</th>
      <td>University of New Brunswick</td>
      <td>45.948121</td>
      <td>-66.641406</td>
      <td>Sobeys</td>
      <td>4b6727daf964a520493e2be3</td>
      <td>45.954891</td>
      <td>-66.645920</td>
      <td>Grocery Store</td>
    </tr>
    <tr>
      <th>70</th>
      <td>University of New Brunswick</td>
      <td>45.948121</td>
      <td>-66.641406</td>
      <td>YMCA Fredericton</td>
      <td>4e93476b8231bf0d17ba3e24</td>
      <td>45.953217</td>
      <td>-66.649478</td>
      <td>Gym</td>
    </tr>
    <tr>
      <th>71</th>
      <td>University of New Brunswick</td>
      <td>45.948121</td>
      <td>-66.641406</td>
      <td>20 Twenty Club</td>
      <td>4c5388b0f5f3d13ac74ba5f8</td>
      <td>45.951042</td>
      <td>-66.648112</td>
      <td>Bar</td>
    </tr>
    <tr>
      <th>72</th>
      <td>University of New Brunswick</td>
      <td>45.948121</td>
      <td>-66.641406</td>
      <td>The Cellar Pub &amp; Grill - UNB</td>
      <td>4b7ac93ef964a520b53c2fe3</td>
      <td>45.945434</td>
      <td>-66.641626</td>
      <td>Pub</td>
    </tr>
    <tr>
      <th>73</th>
      <td>University of New Brunswick</td>
      <td>45.948121</td>
      <td>-66.641406</td>
      <td>Harvey's</td>
      <td>4bbdff85f57ba59320bdaeb9</td>
      <td>45.953544</td>
      <td>-66.645021</td>
      <td>Burger Joint</td>
    </tr>
    <tr>
      <th>74</th>
      <td>University of New Brunswick</td>
      <td>45.948121</td>
      <td>-66.641406</td>
      <td>Tim Hortons</td>
      <td>4c865c1774d7b60c3f41a3d8</td>
      <td>45.945185</td>
      <td>-66.641545</td>
      <td>Coffee Shop</td>
    </tr>
    <tr>
      <th>75</th>
      <td>University of New Brunswick</td>
      <td>45.948121</td>
      <td>-66.641406</td>
      <td>Tim Hortons</td>
      <td>4dc29f89d4c07da169fbf84b</td>
      <td>45.943720</td>
      <td>-66.646907</td>
      <td>Coffee Shop</td>
    </tr>
    <tr>
      <th>76</th>
      <td>University of New Brunswick</td>
      <td>45.948121</td>
      <td>-66.641406</td>
      <td>College Hill Social Club</td>
      <td>4b7aca23f964a520df3c2fe3</td>
      <td>45.945162</td>
      <td>-66.641472</td>
      <td>Bar</td>
    </tr>
    <tr>
      <th>77</th>
      <td>Devon</td>
      <td>45.968802</td>
      <td>-66.622738</td>
      <td>New England Pizza</td>
      <td>4c09984e7e3fc928b64bf282</td>
      <td>45.967675</td>
      <td>-66.629905</td>
      <td>Pizza Place</td>
    </tr>
    <tr>
      <th>78</th>
      <td>Devon</td>
      <td>45.968802</td>
      <td>-66.622738</td>
      <td>Wolastoq Wharf</td>
      <td>4fbaafb0e4b0c7f68a419500</td>
      <td>45.969975</td>
      <td>-66.632568</td>
      <td>Seafood Restaurant</td>
    </tr>
    <tr>
      <th>79</th>
      <td>Devon</td>
      <td>45.968802</td>
      <td>-66.622738</td>
      <td>Dairy Queen</td>
      <td>4c5cab2894fd0f473c69c945</td>
      <td>45.969077</td>
      <td>-66.632059</td>
      <td>Fast Food Restaurant</td>
    </tr>
    <tr>
      <th>80</th>
      <td>Devon</td>
      <td>45.968802</td>
      <td>-66.622738</td>
      <td>Pharmacie Jean Coutu</td>
      <td>4eb9523077c8972738ac89b2</td>
      <td>45.967766</td>
      <td>-66.630551</td>
      <td>Pharmacy</td>
    </tr>
    <tr>
      <th>81</th>
      <td>Devon</td>
      <td>45.968802</td>
      <td>-66.622738</td>
      <td>Tim Hortons</td>
      <td>4b5b0812f964a520d8df28e3</td>
      <td>45.969381</td>
      <td>-66.632730</td>
      <td>Coffee Shop</td>
    </tr>
    <tr>
      <th>82</th>
      <td>Devon</td>
      <td>45.968802</td>
      <td>-66.622738</td>
      <td>Henry Park</td>
      <td>4c8e283dad01199c7923726d</td>
      <td>45.963992</td>
      <td>-66.620283</td>
      <td>Baseball Field</td>
    </tr>
    <tr>
      <th>83</th>
      <td>Devon</td>
      <td>45.968802</td>
      <td>-66.622738</td>
      <td>Giant Tiger</td>
      <td>4c95354f58d4b60c80443029</td>
      <td>45.967715</td>
      <td>-66.630410</td>
      <td>Department Store</td>
    </tr>
    <tr>
      <th>84</th>
      <td>Devon</td>
      <td>45.968802</td>
      <td>-66.622738</td>
      <td>york arena</td>
      <td>4b6c4f10f964a520792f2ce3</td>
      <td>45.964888</td>
      <td>-66.617110</td>
      <td>Skating Rink</td>
    </tr>
    <tr>
      <th>85</th>
      <td>Devon</td>
      <td>45.968802</td>
      <td>-66.622738</td>
      <td>St. Mary's Supermarket</td>
      <td>4b9fa6adf964a520c93137e3</td>
      <td>45.971945</td>
      <td>-66.631248</td>
      <td>Grocery Store</td>
    </tr>
    <tr>
      <th>86</th>
      <td>Devon</td>
      <td>45.968802</td>
      <td>-66.622738</td>
      <td>Dixie Lee</td>
      <td>4c5cacc5d25320a103fdc37a</td>
      <td>45.962257</td>
      <td>-66.624952</td>
      <td>Fast Food Restaurant</td>
    </tr>
    <tr>
      <th>87</th>
      <td>Devon</td>
      <td>45.968802</td>
      <td>-66.622738</td>
      <td>St Marys Smoke Shop</td>
      <td>4ebddf8a4690d233887bf4a6</td>
      <td>45.972270</td>
      <td>-66.631348</td>
      <td>Smoke Shop</td>
    </tr>
    <tr>
      <th>88</th>
      <td>Devon</td>
      <td>45.968802</td>
      <td>-66.622738</td>
      <td>Carleton Park</td>
      <td>4bce2eeb29d4b7138521a8dc</td>
      <td>45.961182</td>
      <td>-66.626310</td>
      <td>Park</td>
    </tr>
    <tr>
      <th>89</th>
      <td>New Maryland</td>
      <td>45.892795</td>
      <td>-66.683673</td>
      <td>New York Fries</td>
      <td>4d8771fc651041bd194d9b30</td>
      <td>45.890420</td>
      <td>-66.683580</td>
      <td>Fast Food Restaurant</td>
    </tr>
    <tr>
      <th>90</th>
      <td>New Maryland</td>
      <td>45.892795</td>
      <td>-66.683673</td>
      <td>Centre De Danse Roca Dance Center</td>
      <td>55fdfc2b498ed76a0f7aa3f6</td>
      <td>45.890978</td>
      <td>-66.692237</td>
      <td>Dance Studio</td>
    </tr>
    <tr>
      <th>91</th>
      <td>New Maryland</td>
      <td>45.892795</td>
      <td>-66.683673</td>
      <td>Baseball, Basketball, Tennis and Hockey In One...</td>
      <td>4e48415862e148603b8b3fc2</td>
      <td>45.890726</td>
      <td>-66.692814</td>
      <td>Baseball Field</td>
    </tr>
    <tr>
      <th>92</th>
      <td>New Maryland</td>
      <td>45.892795</td>
      <td>-66.683673</td>
      <td>Circle K</td>
      <td>4b9e633ef964a5202fdf36e3</td>
      <td>45.885412</td>
      <td>-66.688995</td>
      <td>Gas Station</td>
    </tr>
    <tr>
      <th>93</th>
      <td>Marysville</td>
      <td>45.978913</td>
      <td>-66.589491</td>
      <td>Tim Hortons</td>
      <td>4baa1b40f964a520174b3ae3</td>
      <td>45.978193</td>
      <td>-66.593041</td>
      <td>Coffee Shop</td>
    </tr>
    <tr>
      <th>94</th>
      <td>Marysville</td>
      <td>45.978913</td>
      <td>-66.589491</td>
      <td>Royals Field</td>
      <td>4c573f916201e21edff8736e</td>
      <td>45.980267</td>
      <td>-66.588412</td>
      <td>Baseball Stadium</td>
    </tr>
    <tr>
      <th>95</th>
      <td>Marysville</td>
      <td>45.978913</td>
      <td>-66.589491</td>
      <td>Northside Pharmacy</td>
      <td>4c8bee978018a1cdd1f2e7d2</td>
      <td>45.980194</td>
      <td>-66.588628</td>
      <td>Pharmacy</td>
    </tr>
    <tr>
      <th>96</th>
      <td>Marysville</td>
      <td>45.978913</td>
      <td>-66.589491</td>
      <td>Marysville Place</td>
      <td>4ce6d19be1eeb60c512d99ae</td>
      <td>45.980243</td>
      <td>-66.588277</td>
      <td>Park</td>
    </tr>
    <tr>
      <th>97</th>
      <td>Marysville</td>
      <td>45.978913</td>
      <td>-66.589491</td>
      <td>Circle K</td>
      <td>4bb88fe853649c74431847fb</td>
      <td>45.979250</td>
      <td>-66.593232</td>
      <td>Gas Station</td>
    </tr>
    <tr>
      <th>98</th>
      <td>Skyline Acres</td>
      <td>45.931827</td>
      <td>-66.640339</td>
      <td>Grant Harvey Centre</td>
      <td>4f915a7ee4b01406ebc873ae</td>
      <td>45.925002</td>
      <td>-66.641004</td>
      <td>Hockey Arena</td>
    </tr>
    <tr>
      <th>99</th>
      <td>Skyline Acres</td>
      <td>45.931827</td>
      <td>-66.640339</td>
      <td>Kimble Field</td>
      <td>4fdaa8c2e4b08f3358b1b3d1</td>
      <td>45.930535</td>
      <td>-66.631233</td>
      <td>Baseball Field</td>
    </tr>
    <tr>
      <th>100</th>
      <td>Skyline Acres</td>
      <td>45.931827</td>
      <td>-66.640339</td>
      <td>Mandarin Palace</td>
      <td>4b786998f964a5204ecc2ee3</td>
      <td>45.935440</td>
      <td>-66.631007</td>
      <td>Chinese Restaurant</td>
    </tr>
    <tr>
      <th>101</th>
      <td>Skyline Acres</td>
      <td>45.931827</td>
      <td>-66.640339</td>
      <td>Oriental Pearl</td>
      <td>4ec68431775bf65c02417199</td>
      <td>45.930085</td>
      <td>-66.629518</td>
      <td>Chinese Restaurant</td>
    </tr>
    <tr>
      <th>102</th>
      <td>Hanwell</td>
      <td>45.902315</td>
      <td>-66.755113</td>
      <td>Advanced Fabrics</td>
      <td>53c133a4498e933c415c6118</td>
      <td>45.905297</td>
      <td>-66.750944</td>
      <td>Rental Service</td>
    </tr>
    <tr>
      <th>103</th>
      <td>Hanwell</td>
      <td>45.902315</td>
      <td>-66.755113</td>
      <td>Country Style</td>
      <td>56356c83498e17f8ed69a380</td>
      <td>45.905937</td>
      <td>-66.751084</td>
      <td>Coffee Shop</td>
    </tr>
    <tr>
      <th>104</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Cafe Loka &amp; Bistro</td>
      <td>4e70d116152073dd03c2c50e</td>
      <td>45.957570</td>
      <td>-66.647978</td>
      <td>Café</td>
    </tr>
    <tr>
      <th>105</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Boyce Farmers Market</td>
      <td>4b5163b4f964a5204d4c27e3</td>
      <td>45.958354</td>
      <td>-66.639654</td>
      <td>Farmers Market</td>
    </tr>
    <tr>
      <th>106</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Second Cup</td>
      <td>4b7067c6f964a5205a182de3</td>
      <td>45.961385</td>
      <td>-66.642372</td>
      <td>Coffee Shop</td>
    </tr>
    <tr>
      <th>107</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Lunar Rogue</td>
      <td>4b8c53e7f964a520d4ca32e3</td>
      <td>45.959998</td>
      <td>-66.639116</td>
      <td>Pub</td>
    </tr>
    <tr>
      <th>108</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Jonnie Java Roasters</td>
      <td>4bc47e80920eb71369c71e2c</td>
      <td>45.962226</td>
      <td>-66.643852</td>
      <td>Coffee Shop</td>
    </tr>
    <tr>
      <th>109</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Picaroon's Brewtique</td>
      <td>4ced5cfe7b943704ea782653</td>
      <td>45.962701</td>
      <td>-66.642731</td>
      <td>Brewery</td>
    </tr>
    <tr>
      <th>110</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Sobeys</td>
      <td>4b6727daf964a520493e2be3</td>
      <td>45.954891</td>
      <td>-66.645920</td>
      <td>Grocery Store</td>
    </tr>
    <tr>
      <th>111</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Luna Pizza</td>
      <td>4be47e9b2468c92811dbfe42</td>
      <td>45.962246</td>
      <td>-66.643788</td>
      <td>Italian Restaurant</td>
    </tr>
    <tr>
      <th>112</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Palate Restaurant &amp; Cafe</td>
      <td>4c2e0e6ae760c9b69bdf4549</td>
      <td>45.962338</td>
      <td>-66.641776</td>
      <td>Restaurant</td>
    </tr>
    <tr>
      <th>113</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Alcool NB Liquor</td>
      <td>4d9a52120d5f224bc5f7a34e</td>
      <td>45.956140</td>
      <td>-66.647558</td>
      <td>Liquor Store</td>
    </tr>
    <tr>
      <th>114</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>coffee and friends</td>
      <td>4b533f74f964a520009427e3</td>
      <td>45.961842</td>
      <td>-66.643479</td>
      <td>Coffee Shop</td>
    </tr>
    <tr>
      <th>115</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Chess Piece Pâtisserie &amp; Cafe</td>
      <td>53c00bcc498e1f34dc3687ae</td>
      <td>45.963354</td>
      <td>-66.644017</td>
      <td>Café</td>
    </tr>
    <tr>
      <th>116</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Victory Meat Market</td>
      <td>4bd1ffd341b9ef3bcb19fde5</td>
      <td>45.962661</td>
      <td>-66.645820</td>
      <td>Grocery Store</td>
    </tr>
    <tr>
      <th>117</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Exhibition Grounds</td>
      <td>4c76d45d07818cfafe94d2e3</td>
      <td>45.960078</td>
      <td>-66.655522</td>
      <td>Racetrack</td>
    </tr>
    <tr>
      <th>118</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>The Abbey Café &amp; Gallery</td>
      <td>57178722498e4222f7d5b298</td>
      <td>45.961301</td>
      <td>-66.640188</td>
      <td>Café</td>
    </tr>
    <tr>
      <th>119</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Charlotte Street Arts Centre</td>
      <td>4b7f0318f964a5203d1030e3</td>
      <td>45.955620</td>
      <td>-66.639324</td>
      <td>Art Gallery</td>
    </tr>
    <tr>
      <th>120</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Isaac's Way</td>
      <td>51c8a824498ef33c708ac9e9</td>
      <td>45.960944</td>
      <td>-66.637796</td>
      <td>Restaurant</td>
    </tr>
    <tr>
      <th>121</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>YMCA Fredericton</td>
      <td>4e93476b8231bf0d17ba3e24</td>
      <td>45.953217</td>
      <td>-66.649478</td>
      <td>Gym</td>
    </tr>
    <tr>
      <th>122</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Read's News Stand</td>
      <td>4b4b6bf2f964a5200a9b26e3</td>
      <td>45.961859</td>
      <td>-66.643464</td>
      <td>Coffee Shop</td>
    </tr>
    <tr>
      <th>123</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>King Street Ale House</td>
      <td>5283fd1c498e138a8297590c</td>
      <td>45.960460</td>
      <td>-66.641012</td>
      <td>Pub</td>
    </tr>
    <tr>
      <th>124</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>540 Kitchen and Bar</td>
      <td>53ab370e498e91a454f49e67</td>
      <td>45.961657</td>
      <td>-66.640152</td>
      <td>Gastropub</td>
    </tr>
    <tr>
      <th>125</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Dimitri's Souvlaki</td>
      <td>4bacf7e8f964a520571f3be3</td>
      <td>45.963093</td>
      <td>-66.644479</td>
      <td>Greek Restaurant</td>
    </tr>
    <tr>
      <th>126</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Smoke's Poutinerie</td>
      <td>51756ac6498ece19b79a31f6</td>
      <td>45.962032</td>
      <td>-66.644021</td>
      <td>Fast Food Restaurant</td>
    </tr>
    <tr>
      <th>127</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Snooty Fox</td>
      <td>4b4ca053f964a52006b826e3</td>
      <td>45.960794</td>
      <td>-66.638927</td>
      <td>Pub</td>
    </tr>
    <tr>
      <th>128</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Officer's Square</td>
      <td>4c83b0df2f1c236a4bc54443</td>
      <td>45.961754</td>
      <td>-66.639084</td>
      <td>Park</td>
    </tr>
    <tr>
      <th>129</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Fredericton Playhouse</td>
      <td>4b516b64f964a520df4c27e3</td>
      <td>45.960101</td>
      <td>-66.636969</td>
      <td>Performing Arts Venue</td>
    </tr>
    <tr>
      <th>130</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Willie O'Ree Place</td>
      <td>4b76879ef964a520a5502ee3</td>
      <td>45.963017</td>
      <td>-66.646100</td>
      <td>Hockey Arena</td>
    </tr>
    <tr>
      <th>131</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>The Joyce</td>
      <td>4b624863f964a5203b402ae3</td>
      <td>45.960309</td>
      <td>-66.636806</td>
      <td>Pub</td>
    </tr>
    <tr>
      <th>132</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Cora's Breakfast &amp; Lunch</td>
      <td>4b8130c7f964a520e99930e3</td>
      <td>45.962282</td>
      <td>-66.641607</td>
      <td>Breakfast Spot</td>
    </tr>
    <tr>
      <th>133</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Strange Adventures</td>
      <td>4babdcbdf964a5200cd03ae3</td>
      <td>45.962733</td>
      <td>-66.643315</td>
      <td>Hobby Shop</td>
    </tr>
    <tr>
      <th>134</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Naru Japanese Cuisine</td>
      <td>50461342e4b0c55b9639accc</td>
      <td>45.961721</td>
      <td>-66.640125</td>
      <td>Sushi Restaurant</td>
    </tr>
    <tr>
      <th>135</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Mexicali Rosas</td>
      <td>4c65dd9a19f3c9b697769eff</td>
      <td>45.962811</td>
      <td>-66.646079</td>
      <td>Mexican Restaurant</td>
    </tr>
    <tr>
      <th>136</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Brewbakers</td>
      <td>4b6754faf964a5208d482be3</td>
      <td>45.960703</td>
      <td>-66.640935</td>
      <td>Restaurant</td>
    </tr>
    <tr>
      <th>137</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Dolan's Pub</td>
      <td>4b516ddbf964a520144d27e3</td>
      <td>45.962886</td>
      <td>-66.644615</td>
      <td>Pub</td>
    </tr>
    <tr>
      <th>138</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Beaverbrook Art Gallery</td>
      <td>4c13a7f7b7b9c92865dea937</td>
      <td>45.959878</td>
      <td>-66.635858</td>
      <td>Art Museum</td>
    </tr>
    <tr>
      <th>139</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>McGinnis Landing</td>
      <td>4b6df601f964a5203d9f2ce3</td>
      <td>45.963013</td>
      <td>-66.646536</td>
      <td>Steakhouse</td>
    </tr>
    <tr>
      <th>140</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Atlantic Superstore</td>
      <td>4b5b0a91f964a5205fe028e3</td>
      <td>45.958260</td>
      <td>-66.658048</td>
      <td>Supermarket</td>
    </tr>
    <tr>
      <th>141</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>20 Twenty Club</td>
      <td>4c5388b0f5f3d13ac74ba5f8</td>
      <td>45.951042</td>
      <td>-66.648112</td>
      <td>Bar</td>
    </tr>
    <tr>
      <th>142</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Geek Chic</td>
      <td>4b516f03f964a520324d27e3</td>
      <td>45.960573</td>
      <td>-66.639225</td>
      <td>Toy / Game Store</td>
    </tr>
    <tr>
      <th>143</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Wilser's Room</td>
      <td>4ba01983f964a520f15937e3</td>
      <td>45.963192</td>
      <td>-66.644089</td>
      <td>Bar</td>
    </tr>
    <tr>
      <th>144</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Tim Hortons</td>
      <td>4b6455b0f964a52067ab2ae3</td>
      <td>45.959873</td>
      <td>-66.639259</td>
      <td>Coffee Shop</td>
    </tr>
    <tr>
      <th>145</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>TD Canada Trust</td>
      <td>4b6d8261f964a52022792ce3</td>
      <td>45.963891</td>
      <td>-66.645782</td>
      <td>Bank</td>
    </tr>
    <tr>
      <th>146</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Fit4Less</td>
      <td>4c9381ab94a0236a70ac8312</td>
      <td>45.958634</td>
      <td>-66.657319</td>
      <td>Gym / Fitness Center</td>
    </tr>
    <tr>
      <th>147</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Harvey's</td>
      <td>4bbdff85f57ba59320bdaeb9</td>
      <td>45.953544</td>
      <td>-66.645021</td>
      <td>Burger Joint</td>
    </tr>
    <tr>
      <th>148</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Shoppers Drug Mart</td>
      <td>4db07df34df03036e8bbb640</td>
      <td>45.961351</td>
      <td>-66.644493</td>
      <td>Pharmacy</td>
    </tr>
    <tr>
      <th>149</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Shan</td>
      <td>4dfb6fc31f6eeef806aacc25</td>
      <td>45.961818</td>
      <td>-66.643706</td>
      <td>Chinese Restaurant</td>
    </tr>
    <tr>
      <th>150</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>bulgogi</td>
      <td>4b605f0ff964a5203de229e3</td>
      <td>45.961522</td>
      <td>-66.642742</td>
      <td>Korean Restaurant</td>
    </tr>
    <tr>
      <th>151</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>William's Seafood</td>
      <td>4b7c26f5f964a52061802fe3</td>
      <td>45.959296</td>
      <td>-66.655663</td>
      <td>Seafood Restaurant</td>
    </tr>
    <tr>
      <th>152</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Subway</td>
      <td>4b6b883df964a5205a0e2ce3</td>
      <td>45.962580</td>
      <td>-66.645032</td>
      <td>Sandwich Place</td>
    </tr>
    <tr>
      <th>153</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Capital Complex</td>
      <td>4b6faa7cf964a52073f92ce3</td>
      <td>45.963245</td>
      <td>-66.644123</td>
      <td>Bar</td>
    </tr>
    <tr>
      <th>154</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>boom! Nightclub</td>
      <td>4ba240eef964a52050e737e3</td>
      <td>45.962315</td>
      <td>-66.641645</td>
      <td>Nightclub</td>
    </tr>
    <tr>
      <th>155</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Tim Hortons</td>
      <td>4ba8bdb3f964a5204ceb39e3</td>
      <td>45.959933</td>
      <td>-66.655493</td>
      <td>Coffee Shop</td>
    </tr>
    <tr>
      <th>156</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>King's Place Mall</td>
      <td>4bc61ba4d35d9c74292de23a</td>
      <td>45.961679</td>
      <td>-66.643267</td>
      <td>Shopping Mall</td>
    </tr>
    <tr>
      <th>157</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Running Room</td>
      <td>4c6d4adb23c1a1cdffc81bcf</td>
      <td>45.961812</td>
      <td>-66.643510</td>
      <td>Sporting Goods Shop</td>
    </tr>
    <tr>
      <th>158</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>The Happy Baker</td>
      <td>4b703d21f964a5204c0d2de3</td>
      <td>45.960536</td>
      <td>-66.641465</td>
      <td>Bakery</td>
    </tr>
    <tr>
      <th>159</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Owl's Nest Bookstore</td>
      <td>4d6ea0c98df1548152778123</td>
      <td>45.963051</td>
      <td>-66.643872</td>
      <td>Bookstore</td>
    </tr>
    <tr>
      <th>160</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Tingley's Ice Cream</td>
      <td>4c13c001b7b9c9284e12aa37</td>
      <td>45.957087</td>
      <td>-66.655855</td>
      <td>Ice Cream Shop</td>
    </tr>
    <tr>
      <th>161</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Jumbo Video</td>
      <td>4bc0d29a920eb71307a2192c</td>
      <td>45.957286</td>
      <td>-66.656312</td>
      <td>Video Store</td>
    </tr>
    <tr>
      <th>162</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Enterprise Rent-A-Car</td>
      <td>4d3ae3edbf6d5481b26fd1e1</td>
      <td>45.957743</td>
      <td>-66.656527</td>
      <td>Rental Car Location</td>
    </tr>
    <tr>
      <th>163</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Domino's Pizza</td>
      <td>50f9bbc75d24acebc259244d</td>
      <td>45.957177</td>
      <td>-66.656638</td>
      <td>Pizza Place</td>
    </tr>
    <tr>
      <th>164</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Papa John's Pizza</td>
      <td>4ecc29f59adfd1f5b5c7bbb1</td>
      <td>45.956655</td>
      <td>-66.657285</td>
      <td>Pizza Place</td>
    </tr>
    <tr>
      <th>165</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>Queen Square Park</td>
      <td>4b7acb0ef964a520113d2fe3</td>
      <td>45.950961</td>
      <td>-66.648245</td>
      <td>Park</td>
    </tr>
  </tbody>
</table>
</div>




```python
print('There are {} unique venue categories.'.format(len(fredericton_data_venues['Venue Category'].unique())))
```

    There are 73 unique venue categories.



```python
print('There are {} unique venues.'.format(len(fredericton_data_venues['Venue id'].unique())))
```

    There are 153 unique venues.



```python
univen = fredericton_data_venues.groupby('Location').nunique('Venue Category')
univen
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Location</th>
      <th>Location Latitude</th>
      <th>Location Longitude</th>
      <th>Venue</th>
      <th>Venue id</th>
      <th>Venue Latitude</th>
      <th>Venue Longitude</th>
      <th>Venue Category</th>
    </tr>
    <tr>
      <th>Location</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Devon</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>11</td>
    </tr>
    <tr>
      <th>Downtown</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>61</td>
      <td>62</td>
      <td>62</td>
      <td>62</td>
      <td>44</td>
    </tr>
    <tr>
      <th>Fredericton Hill</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>17</td>
      <td>17</td>
      <td>17</td>
      <td>17</td>
      <td>13</td>
    </tr>
    <tr>
      <th>Hanwell</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Knowledge Park</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>31</td>
      <td>31</td>
      <td>31</td>
      <td>31</td>
      <td>23</td>
    </tr>
    <tr>
      <th>Marysville</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
    </tr>
    <tr>
      <th>Nashwaaksis</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>17</td>
      <td>19</td>
      <td>19</td>
      <td>19</td>
      <td>15</td>
    </tr>
    <tr>
      <th>New Maryland</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Skyline Acres</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>3</td>
    </tr>
    <tr>
      <th>University of New Brunswick</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>9</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>




```python
fredericton_data_venues.groupby('Venue Category').nunique()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Location</th>
      <th>Location Latitude</th>
      <th>Location Longitude</th>
      <th>Venue</th>
      <th>Venue id</th>
      <th>Venue Latitude</th>
      <th>Venue Longitude</th>
      <th>Venue Category</th>
    </tr>
    <tr>
      <th>Venue Category</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Art Gallery</th>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Art Museum</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Arts &amp; Crafts Store</th>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Auto Dealership</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Bakery</th>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Bank</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Bar</th>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Baseball Field</th>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Baseball Stadium</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Basketball Court</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Beer Store</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Big Box Store</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Bookstore</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Breakfast Spot</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Brewery</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Burger Joint</th>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Café</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Chinese Restaurant</th>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Clothing Store</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Coffee Shop</th>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>6</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Dance Studio</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Department Store</th>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Discount Store</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Electronics Store</th>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Farmers Market</th>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Fast Food Restaurant</th>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>9</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Furniture / Home Store</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Gas Station</th>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Gastropub</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Gift Shop</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Greek Restaurant</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Grocery Store</th>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Gym</th>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Gym / Fitness Center</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Hardware Store</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Hobby Shop</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Hockey Arena</th>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Ice Cream Shop</th>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Italian Restaurant</th>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Kids Store</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Korean Restaurant</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Liquor Store</th>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Mattress Store</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Mexican Restaurant</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Nightclub</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Park</th>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Performing Arts Venue</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Pet Store</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Pharmacy</th>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>3</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Pizza Place</th>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Pub</th>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Racetrack</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Rental Car Location</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Rental Service</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Restaurant</th>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Sandwich Place</th>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>1</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Seafood Restaurant</th>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Shoe Store</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Shopping Mall</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Shopping Plaza</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Skating Rink</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Smoke Shop</th>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Smoothie Shop</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Spa</th>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Sporting Goods Shop</th>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Sports Bar</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Steakhouse</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Supermarket</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Sushi Restaurant</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Thai Restaurant</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Toy / Game Store</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Video Store</th>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Warehouse Store</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python

```

## Analyze each Location


```python
# one hot encoding
freddy_onehot = pd.get_dummies(fredericton_data_venues[['Venue Category']], prefix="", prefix_sep="")

# add neighbourhood column back to dataframe
freddy_onehot['Location'] = fredericton_data_venues['Location'] 

# move neighbourhood column to the first column
fixed_columns = [freddy_onehot.columns[-1]] + list(freddy_onehot.columns[:-1])
freddy_onehot = freddy_onehot[fixed_columns]

freddy_onehot.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Location</th>
      <th>Art Gallery</th>
      <th>Art Museum</th>
      <th>Arts &amp; Crafts Store</th>
      <th>Auto Dealership</th>
      <th>Bakery</th>
      <th>Bank</th>
      <th>Bar</th>
      <th>Baseball Field</th>
      <th>Baseball Stadium</th>
      <th>Basketball Court</th>
      <th>Beer Store</th>
      <th>Big Box Store</th>
      <th>Bookstore</th>
      <th>Breakfast Spot</th>
      <th>Brewery</th>
      <th>Burger Joint</th>
      <th>Café</th>
      <th>Chinese Restaurant</th>
      <th>Clothing Store</th>
      <th>Coffee Shop</th>
      <th>Dance Studio</th>
      <th>Department Store</th>
      <th>Discount Store</th>
      <th>Electronics Store</th>
      <th>Farmers Market</th>
      <th>Fast Food Restaurant</th>
      <th>Furniture / Home Store</th>
      <th>Gas Station</th>
      <th>Gastropub</th>
      <th>Gift Shop</th>
      <th>Greek Restaurant</th>
      <th>Grocery Store</th>
      <th>Gym</th>
      <th>Gym / Fitness Center</th>
      <th>Hardware Store</th>
      <th>Hobby Shop</th>
      <th>Hockey Arena</th>
      <th>Ice Cream Shop</th>
      <th>Italian Restaurant</th>
      <th>Kids Store</th>
      <th>Korean Restaurant</th>
      <th>Liquor Store</th>
      <th>Mattress Store</th>
      <th>Mexican Restaurant</th>
      <th>Nightclub</th>
      <th>Park</th>
      <th>Performing Arts Venue</th>
      <th>Pet Store</th>
      <th>Pharmacy</th>
      <th>Pizza Place</th>
      <th>Pub</th>
      <th>Racetrack</th>
      <th>Rental Car Location</th>
      <th>Rental Service</th>
      <th>Restaurant</th>
      <th>Sandwich Place</th>
      <th>Seafood Restaurant</th>
      <th>Shoe Store</th>
      <th>Shopping Mall</th>
      <th>Shopping Plaza</th>
      <th>Skating Rink</th>
      <th>Smoke Shop</th>
      <th>Smoothie Shop</th>
      <th>Spa</th>
      <th>Sporting Goods Shop</th>
      <th>Sports Bar</th>
      <th>Steakhouse</th>
      <th>Supermarket</th>
      <th>Sushi Restaurant</th>
      <th>Thai Restaurant</th>
      <th>Toy / Game Store</th>
      <th>Video Store</th>
      <th>Warehouse Store</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Knowledge Park</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Knowledge Park</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Knowledge Park</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Knowledge Park</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Knowledge Park</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
freddy_onehot.shape
```




    (166, 74)



### Group rows by location and by the mean of the frequency of occurrence of each category


```python
freddy_grouped = freddy_onehot.groupby('Location').mean().reset_index()
freddy_grouped
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Location</th>
      <th>Art Gallery</th>
      <th>Art Museum</th>
      <th>Arts &amp; Crafts Store</th>
      <th>Auto Dealership</th>
      <th>Bakery</th>
      <th>Bank</th>
      <th>Bar</th>
      <th>Baseball Field</th>
      <th>Baseball Stadium</th>
      <th>Basketball Court</th>
      <th>Beer Store</th>
      <th>Big Box Store</th>
      <th>Bookstore</th>
      <th>Breakfast Spot</th>
      <th>Brewery</th>
      <th>Burger Joint</th>
      <th>Café</th>
      <th>Chinese Restaurant</th>
      <th>Clothing Store</th>
      <th>Coffee Shop</th>
      <th>Dance Studio</th>
      <th>Department Store</th>
      <th>Discount Store</th>
      <th>Electronics Store</th>
      <th>Farmers Market</th>
      <th>Fast Food Restaurant</th>
      <th>Furniture / Home Store</th>
      <th>Gas Station</th>
      <th>Gastropub</th>
      <th>Gift Shop</th>
      <th>Greek Restaurant</th>
      <th>Grocery Store</th>
      <th>Gym</th>
      <th>Gym / Fitness Center</th>
      <th>Hardware Store</th>
      <th>Hobby Shop</th>
      <th>Hockey Arena</th>
      <th>Ice Cream Shop</th>
      <th>Italian Restaurant</th>
      <th>Kids Store</th>
      <th>Korean Restaurant</th>
      <th>Liquor Store</th>
      <th>Mattress Store</th>
      <th>Mexican Restaurant</th>
      <th>Nightclub</th>
      <th>Park</th>
      <th>Performing Arts Venue</th>
      <th>Pet Store</th>
      <th>Pharmacy</th>
      <th>Pizza Place</th>
      <th>Pub</th>
      <th>Racetrack</th>
      <th>Rental Car Location</th>
      <th>Rental Service</th>
      <th>Restaurant</th>
      <th>Sandwich Place</th>
      <th>Seafood Restaurant</th>
      <th>Shoe Store</th>
      <th>Shopping Mall</th>
      <th>Shopping Plaza</th>
      <th>Skating Rink</th>
      <th>Smoke Shop</th>
      <th>Smoothie Shop</th>
      <th>Spa</th>
      <th>Sporting Goods Shop</th>
      <th>Sports Bar</th>
      <th>Steakhouse</th>
      <th>Supermarket</th>
      <th>Sushi Restaurant</th>
      <th>Thai Restaurant</th>
      <th>Toy / Game Store</th>
      <th>Video Store</th>
      <th>Warehouse Store</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Devon</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.083333</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.083333</td>
      <td>0.00</td>
      <td>0.083333</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.166667</td>
      <td>0.000000</td>
      <td>0.00</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.083333</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.083333</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.083333</td>
      <td>0.083333</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.083333</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.083333</td>
      <td>0.083333</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Downtown</td>
      <td>0.016129</td>
      <td>0.016129</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.016129</td>
      <td>0.016129</td>
      <td>0.048387</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.016129</td>
      <td>0.016129</td>
      <td>0.016129</td>
      <td>0.016129</td>
      <td>0.048387</td>
      <td>0.016129</td>
      <td>0.000000</td>
      <td>0.096774</td>
      <td>0.00</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.016129</td>
      <td>0.016129</td>
      <td>0.000000</td>
      <td>0.00</td>
      <td>0.016129</td>
      <td>0.000000</td>
      <td>0.016129</td>
      <td>0.032258</td>
      <td>0.016129</td>
      <td>0.016129</td>
      <td>0.000000</td>
      <td>0.016129</td>
      <td>0.016129</td>
      <td>0.016129</td>
      <td>0.016129</td>
      <td>0.000000</td>
      <td>0.016129</td>
      <td>0.016129</td>
      <td>0.000000</td>
      <td>0.016129</td>
      <td>0.016129</td>
      <td>0.032258</td>
      <td>0.016129</td>
      <td>0.000000</td>
      <td>0.016129</td>
      <td>0.032258</td>
      <td>0.080645</td>
      <td>0.016129</td>
      <td>0.016129</td>
      <td>0.0</td>
      <td>0.048387</td>
      <td>0.016129</td>
      <td>0.016129</td>
      <td>0.000000</td>
      <td>0.016129</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.016129</td>
      <td>0.000000</td>
      <td>0.016129</td>
      <td>0.016129</td>
      <td>0.016129</td>
      <td>0.000000</td>
      <td>0.016129</td>
      <td>0.016129</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Fredericton Hill</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.176471</td>
      <td>0.000000</td>
      <td>0.058824</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.058824</td>
      <td>0.00</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.00</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.058824</td>
      <td>0.000000</td>
      <td>0.058824</td>
      <td>0.000000</td>
      <td>0.058824</td>
      <td>0.058824</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.058824</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.058824</td>
      <td>0.176471</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.058824</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.058824</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.058824</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Hanwell</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.500000</td>
      <td>0.00</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.00</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.5</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Knowledge Park</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.032258</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.032258</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.096774</td>
      <td>0.000000</td>
      <td>0.00</td>
      <td>0.032258</td>
      <td>0.032258</td>
      <td>0.032258</td>
      <td>0.000000</td>
      <td>0.129032</td>
      <td>0.064516</td>
      <td>0.00</td>
      <td>0.000000</td>
      <td>0.032258</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.032258</td>
      <td>0.032258</td>
      <td>0.000000</td>
      <td>0.064516</td>
      <td>0.032258</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.032258</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.064516</td>
      <td>0.000000</td>
      <td>0.032258</td>
      <td>0.032258</td>
      <td>0.000000</td>
      <td>0.032258</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.032258</td>
      <td>0.032258</td>
      <td>0.032258</td>
      <td>0.032258</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.032258</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Marysville</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.2</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.200000</td>
      <td>0.00</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.20</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.200000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.200000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Nashwaaksis</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.052632</td>
      <td>0.052632</td>
      <td>0.052632</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.052632</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.105263</td>
      <td>0.00</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.052632</td>
      <td>0.105263</td>
      <td>0.105263</td>
      <td>0.000000</td>
      <td>0.00</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.052632</td>
      <td>0.052632</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.052632</td>
      <td>0.052632</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.105263</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.052632</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.052632</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>7</th>
      <td>New Maryland</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.250000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.25</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.250000</td>
      <td>0.000000</td>
      <td>0.25</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Skyline Acres</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.250000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.500000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.00</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.00</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.250000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>9</th>
      <td>University of New Brunswick</td>
      <td>0.100000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.200000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.1</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.100000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.200000</td>
      <td>0.00</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.00</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.100000</td>
      <td>0.100000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.100000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
freddy_grouped.shape
```




    (10, 74)



### Print each Location with the top 5 most common venues


```python
num_top_venues = 5

for hood in freddy_grouped['Location']:
    print("----"+hood+"----")
    temp = freddy_grouped[freddy_grouped['Location'] == hood].T.reset_index()
    temp.columns = ['venue','freq']
    temp = temp.iloc[1:]
    temp['freq'] = temp['freq'].astype(float)
    temp = temp.round({'freq': 2})
    print(temp.sort_values('freq', ascending=False).reset_index(drop=True).head(num_top_venues))
    print('\n')
```

    ----Devon----
                      venue  freq
    0  Fast Food Restaurant  0.17
    1           Coffee Shop  0.08
    2         Grocery Store  0.08
    3    Seafood Restaurant  0.08
    4          Skating Rink  0.08
    
    
    ----Downtown----
             venue  freq
    0  Coffee Shop  0.10
    1          Pub  0.08
    2         Café  0.05
    3   Restaurant  0.05
    4          Bar  0.05
    
    
    ----Fredericton Hill----
                venue  freq
    0          Bakery  0.18
    1     Pizza Place  0.18
    2    Hockey Arena  0.06
    3      Smoke Shop  0.06
    4  Ice Cream Shop  0.06
    
    
    ----Hanwell----
                     venue  freq
    0          Coffee Shop   0.5
    1       Rental Service   0.5
    2          Art Gallery   0.0
    3  Rental Car Location   0.0
    4            Racetrack   0.0
    
    
    ----Knowledge Park----
                        venue  freq
    0    Fast Food Restaurant  0.13
    1          Clothing Store  0.10
    2            Liquor Store  0.06
    3              Restaurant  0.06
    4  Furniture / Home Store  0.06
    
    
    ----Marysville----
                  venue  freq
    0       Coffee Shop   0.2
    1          Pharmacy   0.2
    2              Park   0.2
    3  Baseball Stadium   0.2
    4       Gas Station   0.2
    
    
    ----Nashwaaksis----
                      venue  freq
    0        Farmers Market  0.11
    1        Sandwich Place  0.11
    2           Coffee Shop  0.11
    3  Fast Food Restaurant  0.11
    4            Beer Store  0.05
    
    
    ----New Maryland----
                      venue  freq
    0  Fast Food Restaurant  0.25
    1        Baseball Field  0.25
    2           Gas Station  0.25
    3          Dance Studio  0.25
    4           Art Gallery  0.00
    
    
    ----Skyline Acres----
                    venue  freq
    0  Chinese Restaurant  0.50
    1        Hockey Arena  0.25
    2      Baseball Field  0.25
    3           Pet Store  0.00
    4      Rental Service  0.00
    
    
    ----University of New Brunswick----
                  venue  freq
    0       Coffee Shop   0.2
    1               Bar   0.2
    2  Basketball Court   0.1
    3               Gym   0.1
    4     Grocery Store   0.1
    
    


### Now into a pandas dataframe


```python
def return_most_common_venues(row, num_top_venues):
    row_categories = row.iloc[1:]
    row_categories_sorted = row_categories.sort_values(ascending=False)
    
    return row_categories_sorted.index.values[0:num_top_venues]
```


```python
num_top_venues = 10

indicators = ['st', 'nd', 'rd']

# create columns according to number of top venues
columns = ['Location']
for ind in np.arange(num_top_venues):
    try:
        columns.append('{}{} Most Common Venue'.format(ind+1, indicators[ind]))
    except:
        columns.append('{}th Most Common Venue'.format(ind+1))

# create a new dataframe
location_venues_sorted = pd.DataFrame(columns=columns)
location_venues_sorted['Location'] = freddy_grouped['Location']

for ind in np.arange(freddy_grouped.shape[0]):
    location_venues_sorted.iloc[ind, 1:] = return_most_common_venues(freddy_grouped.iloc[ind, :], num_top_venues)

location_venues_sorted
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Location</th>
      <th>1st Most Common Venue</th>
      <th>2nd Most Common Venue</th>
      <th>3rd Most Common Venue</th>
      <th>4th Most Common Venue</th>
      <th>5th Most Common Venue</th>
      <th>6th Most Common Venue</th>
      <th>7th Most Common Venue</th>
      <th>8th Most Common Venue</th>
      <th>9th Most Common Venue</th>
      <th>10th Most Common Venue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Devon</td>
      <td>Fast Food Restaurant</td>
      <td>Grocery Store</td>
      <td>Smoke Shop</td>
      <td>Pharmacy</td>
      <td>Coffee Shop</td>
      <td>Seafood Restaurant</td>
      <td>Park</td>
      <td>Department Store</td>
      <td>Skating Rink</td>
      <td>Pizza Place</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Downtown</td>
      <td>Coffee Shop</td>
      <td>Pub</td>
      <td>Bar</td>
      <td>Café</td>
      <td>Restaurant</td>
      <td>Park</td>
      <td>Pizza Place</td>
      <td>Grocery Store</td>
      <td>Hockey Arena</td>
      <td>Greek Restaurant</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Fredericton Hill</td>
      <td>Bakery</td>
      <td>Pizza Place</td>
      <td>Hockey Arena</td>
      <td>Smoke Shop</td>
      <td>Hardware Store</td>
      <td>Video Store</td>
      <td>Ice Cream Shop</td>
      <td>Park</td>
      <td>Pharmacy</td>
      <td>Coffee Shop</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Hanwell</td>
      <td>Rental Service</td>
      <td>Coffee Shop</td>
      <td>Warehouse Store</td>
      <td>Dance Studio</td>
      <td>Department Store</td>
      <td>Discount Store</td>
      <td>Electronics Store</td>
      <td>Farmers Market</td>
      <td>Fast Food Restaurant</td>
      <td>Furniture / Home Store</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Knowledge Park</td>
      <td>Fast Food Restaurant</td>
      <td>Clothing Store</td>
      <td>Furniture / Home Store</td>
      <td>Liquor Store</td>
      <td>Restaurant</td>
      <td>Warehouse Store</td>
      <td>Shoe Store</td>
      <td>Pet Store</td>
      <td>Mattress Store</td>
      <td>Gift Shop</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Marysville</td>
      <td>Baseball Stadium</td>
      <td>Gas Station</td>
      <td>Pharmacy</td>
      <td>Park</td>
      <td>Coffee Shop</td>
      <td>Gift Shop</td>
      <td>Gastropub</td>
      <td>Greek Restaurant</td>
      <td>Furniture / Home Store</td>
      <td>Clothing Store</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Nashwaaksis</td>
      <td>Coffee Shop</td>
      <td>Sandwich Place</td>
      <td>Farmers Market</td>
      <td>Fast Food Restaurant</td>
      <td>Gym</td>
      <td>Spa</td>
      <td>Electronics Store</td>
      <td>Beer Store</td>
      <td>Pizza Place</td>
      <td>Pharmacy</td>
    </tr>
    <tr>
      <th>7</th>
      <td>New Maryland</td>
      <td>Gas Station</td>
      <td>Dance Studio</td>
      <td>Fast Food Restaurant</td>
      <td>Baseball Field</td>
      <td>Furniture / Home Store</td>
      <td>Department Store</td>
      <td>Discount Store</td>
      <td>Electronics Store</td>
      <td>Farmers Market</td>
      <td>Warehouse Store</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Skyline Acres</td>
      <td>Chinese Restaurant</td>
      <td>Baseball Field</td>
      <td>Hockey Arena</td>
      <td>Arts &amp; Crafts Store</td>
      <td>Coffee Shop</td>
      <td>Gym / Fitness Center</td>
      <td>Gym</td>
      <td>Grocery Store</td>
      <td>Greek Restaurant</td>
      <td>Gift Shop</td>
    </tr>
    <tr>
      <th>9</th>
      <td>University of New Brunswick</td>
      <td>Bar</td>
      <td>Coffee Shop</td>
      <td>Art Gallery</td>
      <td>Pub</td>
      <td>Burger Joint</td>
      <td>Basketball Court</td>
      <td>Grocery Store</td>
      <td>Gym</td>
      <td>Gift Shop</td>
      <td>Greek Restaurant</td>
    </tr>
  </tbody>
</table>
</div>



## Cluster Fredericton Locations

### Run k-means to cluster Locations into 5 clusters


```python
# set number of clusters
kclusters = 5

freddy_grouped_clustering = freddy_grouped.drop('Location', 1)

# run k-means clustering
kmeans = KMeans(n_clusters=kclusters, random_state=0).fit(freddy_grouped_clustering)

# check cluster labels generated for each row in the dataframe
kmeans.labels_[0:10] 
```




    array([1, 1, 1, 0, 1, 4, 1, 3, 2, 1], dtype=int32)



### Now creating a new dataframe including the cluster as well as the top 10 venues for each Location


```python
freddy_merged = location_df

# add clustering labels
freddy_merged['Cluster Labels'] = kmeans.labels_

# merge fredericton_grouped with location df to add latitude/longitude for each location
freddy_merged = freddy_merged.join(location_venues_sorted.set_index('Location'), on='Location')

freddy_merged# check the last columns!
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Location</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>Cluster Labels</th>
      <th>1st Most Common Venue</th>
      <th>2nd Most Common Venue</th>
      <th>3rd Most Common Venue</th>
      <th>4th Most Common Venue</th>
      <th>5th Most Common Venue</th>
      <th>6th Most Common Venue</th>
      <th>7th Most Common Venue</th>
      <th>8th Most Common Venue</th>
      <th>9th Most Common Venue</th>
      <th>10th Most Common Venue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Knowledge Park</td>
      <td>45.931143</td>
      <td>-66.652700</td>
      <td>1</td>
      <td>Fast Food Restaurant</td>
      <td>Clothing Store</td>
      <td>Furniture / Home Store</td>
      <td>Liquor Store</td>
      <td>Restaurant</td>
      <td>Warehouse Store</td>
      <td>Shoe Store</td>
      <td>Pet Store</td>
      <td>Mattress Store</td>
      <td>Gift Shop</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Fredericton Hill</td>
      <td>45.948512</td>
      <td>-66.656045</td>
      <td>1</td>
      <td>Bakery</td>
      <td>Pizza Place</td>
      <td>Hockey Arena</td>
      <td>Smoke Shop</td>
      <td>Hardware Store</td>
      <td>Video Store</td>
      <td>Ice Cream Shop</td>
      <td>Park</td>
      <td>Pharmacy</td>
      <td>Coffee Shop</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Nashwaaksis</td>
      <td>45.983382</td>
      <td>-66.644856</td>
      <td>1</td>
      <td>Coffee Shop</td>
      <td>Sandwich Place</td>
      <td>Farmers Market</td>
      <td>Fast Food Restaurant</td>
      <td>Gym</td>
      <td>Spa</td>
      <td>Electronics Store</td>
      <td>Beer Store</td>
      <td>Pizza Place</td>
      <td>Pharmacy</td>
    </tr>
    <tr>
      <th>3</th>
      <td>University of New Brunswick</td>
      <td>45.948121</td>
      <td>-66.641406</td>
      <td>0</td>
      <td>Bar</td>
      <td>Coffee Shop</td>
      <td>Art Gallery</td>
      <td>Pub</td>
      <td>Burger Joint</td>
      <td>Basketball Court</td>
      <td>Grocery Store</td>
      <td>Gym</td>
      <td>Gift Shop</td>
      <td>Greek Restaurant</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Devon</td>
      <td>45.968802</td>
      <td>-66.622738</td>
      <td>1</td>
      <td>Fast Food Restaurant</td>
      <td>Grocery Store</td>
      <td>Smoke Shop</td>
      <td>Pharmacy</td>
      <td>Coffee Shop</td>
      <td>Seafood Restaurant</td>
      <td>Park</td>
      <td>Department Store</td>
      <td>Skating Rink</td>
      <td>Pizza Place</td>
    </tr>
    <tr>
      <th>5</th>
      <td>New Maryland</td>
      <td>45.892795</td>
      <td>-66.683673</td>
      <td>4</td>
      <td>Gas Station</td>
      <td>Dance Studio</td>
      <td>Fast Food Restaurant</td>
      <td>Baseball Field</td>
      <td>Furniture / Home Store</td>
      <td>Department Store</td>
      <td>Discount Store</td>
      <td>Electronics Store</td>
      <td>Farmers Market</td>
      <td>Warehouse Store</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Marysville</td>
      <td>45.978913</td>
      <td>-66.589491</td>
      <td>1</td>
      <td>Baseball Stadium</td>
      <td>Gas Station</td>
      <td>Pharmacy</td>
      <td>Park</td>
      <td>Coffee Shop</td>
      <td>Gift Shop</td>
      <td>Gastropub</td>
      <td>Greek Restaurant</td>
      <td>Furniture / Home Store</td>
      <td>Clothing Store</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Skyline Acres</td>
      <td>45.931827</td>
      <td>-66.640339</td>
      <td>3</td>
      <td>Chinese Restaurant</td>
      <td>Baseball Field</td>
      <td>Hockey Arena</td>
      <td>Arts &amp; Crafts Store</td>
      <td>Coffee Shop</td>
      <td>Gym / Fitness Center</td>
      <td>Gym</td>
      <td>Grocery Store</td>
      <td>Greek Restaurant</td>
      <td>Gift Shop</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Hanwell</td>
      <td>45.902315</td>
      <td>-66.755113</td>
      <td>2</td>
      <td>Rental Service</td>
      <td>Coffee Shop</td>
      <td>Warehouse Store</td>
      <td>Dance Studio</td>
      <td>Department Store</td>
      <td>Discount Store</td>
      <td>Electronics Store</td>
      <td>Farmers Market</td>
      <td>Fast Food Restaurant</td>
      <td>Furniture / Home Store</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Downtown</td>
      <td>45.958327</td>
      <td>-66.647211</td>
      <td>1</td>
      <td>Coffee Shop</td>
      <td>Pub</td>
      <td>Bar</td>
      <td>Café</td>
      <td>Restaurant</td>
      <td>Park</td>
      <td>Pizza Place</td>
      <td>Grocery Store</td>
      <td>Hockey Arena</td>
      <td>Greek Restaurant</td>
    </tr>
  </tbody>
</table>
</div>




```python
# create map
map_clusters = folium.Map(location=[latitude, longitude], zoom_start=11)

# set color scheme for the clusters
x = np.arange(kclusters)
ys = [i+x+(i*x)**2 for i in range(kclusters)]
colors_array = cm.rainbow(np.linspace(0, 1, len(ys)))
rainbow = [colors.rgb2hex(i) for i in colors_array]

# add markers to the map
markers_colors = []
for lat, lon, poi, cluster in zip(freddy_merged['Latitude'], freddy_merged['Longitude'], freddy_merged['Location'], freddy_merged['Cluster Labels']):
    label = folium.Popup(str(poi) + ' Cluster ' + str(cluster), parse_html=True)
    folium.CircleMarker([lat, lon], radius=5,popup=label,color=rainbow[cluster-1],fill=True,fill_color=rainbow[cluster-1],
        fill_opacity=0.7).add_to(map_clusters)
map_clusters
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><iframe src="data:text/html;charset=utf-8;base64,PCFET0NUWVBFIGh0bWw+CjxoZWFkPiAgICAKICAgIDxtZXRhIGh0dHAtZXF1aXY9ImNvbnRlbnQtdHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PVVURi04IiAvPgogICAgPHNjcmlwdD5MX1BSRUZFUl9DQU5WQVMgPSBmYWxzZTsgTF9OT19UT1VDSCA9IGZhbHNlOyBMX0RJU0FCTEVfM0QgPSBmYWxzZTs8L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2FqYXguZ29vZ2xlYXBpcy5jb20vYWpheC9saWJzL2pxdWVyeS8xLjExLjEvanF1ZXJ5Lm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvanMvYm9vdHN0cmFwLm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvTGVhZmxldC5hd2Vzb21lLW1hcmtlcnMvMi4wLjIvbGVhZmxldC5hd2Vzb21lLW1hcmtlcnMuanMiPjwvc2NyaXB0PgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9jc3MvYm9vdHN0cmFwLm1pbi5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvY3NzL2Jvb3RzdHJhcC10aGVtZS5taW4uY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vbWF4Y2RuLmJvb3RzdHJhcGNkbi5jb20vZm9udC1hd2Vzb21lLzQuNi4zL2Nzcy9mb250LWF3ZXNvbWUubWluLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9MZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy8yLjAuMi9sZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9yYXdnaXQuY29tL3B5dGhvbi12aXN1YWxpemF0aW9uL2ZvbGl1bS9tYXN0ZXIvZm9saXVtL3RlbXBsYXRlcy9sZWFmbGV0LmF3ZXNvbWUucm90YXRlLmNzcyIvPgogICAgPHN0eWxlPmh0bWwsIGJvZHkge3dpZHRoOiAxMDAlO2hlaWdodDogMTAwJTttYXJnaW46IDA7cGFkZGluZzogMDt9PC9zdHlsZT4KICAgIDxzdHlsZT4jbWFwIHtwb3NpdGlvbjphYnNvbHV0ZTt0b3A6MDtib3R0b206MDtyaWdodDowO2xlZnQ6MDt9PC9zdHlsZT4KICAgIAogICAgICAgICAgICA8c3R5bGU+ICNtYXBfYzZkNmU5YmZkYWQ3NDgzYWE3NWNlMDhlMGQ3ZmUyOGUgewogICAgICAgICAgICAgICAgcG9zaXRpb24gOiByZWxhdGl2ZTsKICAgICAgICAgICAgICAgIHdpZHRoIDogMTAwLjAlOwogICAgICAgICAgICAgICAgaGVpZ2h0OiAxMDAuMCU7CiAgICAgICAgICAgICAgICBsZWZ0OiAwLjAlOwogICAgICAgICAgICAgICAgdG9wOiAwLjAlOwogICAgICAgICAgICAgICAgfQogICAgICAgICAgICA8L3N0eWxlPgogICAgICAgIAo8L2hlYWQ+Cjxib2R5PiAgICAKICAgIAogICAgICAgICAgICA8ZGl2IGNsYXNzPSJmb2xpdW0tbWFwIiBpZD0ibWFwX2M2ZDZlOWJmZGFkNzQ4M2FhNzVjZTA4ZTBkN2ZlMjhlIiA+PC9kaXY+CiAgICAgICAgCjwvYm9keT4KPHNjcmlwdD4gICAgCiAgICAKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGJvdW5kcyA9IG51bGw7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgdmFyIG1hcF9jNmQ2ZTliZmRhZDc0ODNhYTc1Y2UwOGUwZDdmZTI4ZSA9IEwubWFwKAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ21hcF9jNmQ2ZTliZmRhZDc0ODNhYTc1Y2UwOGUwZDdmZTI4ZScsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB7Y2VudGVyOiBbNDUuOTY2NDI1LC02Ni42NDU4MTNdLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgem9vbTogMTEsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBtYXhCb3VuZHM6IGJvdW5kcywKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGxheWVyczogW10sCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB3b3JsZENvcHlKdW1wOiBmYWxzZSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGNyczogTC5DUlMuRVBTRzM4NTcKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgfSk7CiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciB0aWxlX2xheWVyX2NhNjA0YWQ3MWI4NTQxZWE5NWMwNDU3YTQ3NDQ5M2EyID0gTC50aWxlTGF5ZXIoCiAgICAgICAgICAgICAgICAnaHR0cHM6Ly97c30udGlsZS5vcGVuc3RyZWV0bWFwLm9yZy97en0ve3h9L3t5fS5wbmcnLAogICAgICAgICAgICAgICAgewogICJhdHRyaWJ1dGlvbiI6IG51bGwsCiAgImRldGVjdFJldGluYSI6IGZhbHNlLAogICJtYXhab29tIjogMTgsCiAgIm1pblpvb20iOiAxLAogICJub1dyYXAiOiBmYWxzZSwKICAic3ViZG9tYWlucyI6ICJhYmMiCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2M2ZDZlOWJmZGFkNzQ4M2FhNzVjZTA4ZTBkN2ZlMjhlKTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8wZDIwOGNmZDcxZWI0ZWUxYjc5Zjk5NmJiOTljYTliYiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQ1LjkzMTE0MywtNjYuNjUyN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjODAwMGZmIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzgwMDBmZiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9jNmQ2ZTliZmRhZDc0ODNhYTc1Y2UwOGUwZDdmZTI4ZSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF83YTFlYjc4OThiYmU0MjJkYTA3NGE3OGM3MjBlNjEwZSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9hODYzYjRjMzg3MGM0ZGZmOTQ4MTRjZWZhMjVkOGU0ZiA9ICQoJzxkaXYgaWQ9Imh0bWxfYTg2M2I0YzM4NzBjNGRmZjk0ODE0Y2VmYTI1ZDhlNGYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPktub3dsZWRnZSBQYXJrIENsdXN0ZXIgMTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfN2ExZWI3ODk4YmJlNDIyZGEwNzRhNzhjNzIwZTYxMGUuc2V0Q29udGVudChodG1sX2E4NjNiNGMzODcwYzRkZmY5NDgxNGNlZmEyNWQ4ZTRmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzBkMjA4Y2ZkNzFlYjRlZTFiNzlmOTk2YmI5OWNhOWJiLmJpbmRQb3B1cChwb3B1cF83YTFlYjc4OThiYmU0MjJkYTA3NGE3OGM3MjBlNjEwZSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8zOTQ3MGMyMmQ5M2Y0MDlmOWEzNzBmMzBlMWNjMzYwZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQ1Ljk0ODUxMiwtNjYuNjU2MDQ1XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiM4MDAwZmYiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjODAwMGZmIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2M2ZDZlOWJmZGFkNzQ4M2FhNzVjZTA4ZTBkN2ZlMjhlKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzNhNzZiNjhlZGYxZDRmMDJiNTlmMDUwOGMwZWM1NGM3ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2QzNjBkNTBlMmM3ZTQ0NzA4NzczMjljZDk4NWEwMDdlID0gJCgnPGRpdiBpZD0iaHRtbF9kMzYwZDUwZTJjN2U0NDcwODc3MzI5Y2Q5ODVhMDA3ZSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RnJlZGVyaWN0b24gSGlsbCBDbHVzdGVyIDE8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzNhNzZiNjhlZGYxZDRmMDJiNTlmMDUwOGMwZWM1NGM3LnNldENvbnRlbnQoaHRtbF9kMzYwZDUwZTJjN2U0NDcwODc3MzI5Y2Q5ODVhMDA3ZSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8zOTQ3MGMyMmQ5M2Y0MDlmOWEzNzBmMzBlMWNjMzYwZS5iaW5kUG9wdXAocG9wdXBfM2E3NmI2OGVkZjFkNGYwMmI1OWYwNTA4YzBlYzU0YzcpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNGIxZmFmYjg2ZDEyNDZkMjlkMDNhMzAyNWJkNDQxMmQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0NS45ODMzODIsLTY2LjY0NDg1Nl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjODAwMGZmIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzgwMDBmZiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9jNmQ2ZTliZmRhZDc0ODNhYTc1Y2UwOGUwZDdmZTI4ZSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8yZTJlYTlkN2ZkNTA0Y2E2OGVhYjc5NmUyNWFmZDQ1MiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mNTkwOGI1NmMyNmE0YmY1YmIxMmMxNjg0ODgwMjQ2MyA9ICQoJzxkaXYgaWQ9Imh0bWxfZjU5MDhiNTZjMjZhNGJmNWJiMTJjMTY4NDg4MDI0NjMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk5hc2h3YWFrc2lzIENsdXN0ZXIgMTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMmUyZWE5ZDdmZDUwNGNhNjhlYWI3OTZlMjVhZmQ0NTIuc2V0Q29udGVudChodG1sX2Y1OTA4YjU2YzI2YTRiZjViYjEyYzE2ODQ4ODAyNDYzKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzRiMWZhZmI4NmQxMjQ2ZDI5ZDAzYTMwMjViZDQ0MTJkLmJpbmRQb3B1cChwb3B1cF8yZTJlYTlkN2ZkNTA0Y2E2OGVhYjc5NmUyNWFmZDQ1Mik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9lNjk5Y2ZlZGVmOTA0MjY2YTAwZTdjM2M5NzY5ZDAwMiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQ1Ljk0ODEyMSwtNjYuNjQxNDA2XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2M2ZDZlOWJmZGFkNzQ4M2FhNzVjZTA4ZTBkN2ZlMjhlKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2NkODY4YTU1ODM5YjQ2ZWM4MDczZGEyY2MxODAzOTZmID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzU3OGRjMWVmNjE5NDQ2YWU4NmNhY2RhODBjMWE1N2NiID0gJCgnPGRpdiBpZD0iaHRtbF81NzhkYzFlZjYxOTQ0NmFlODZjYWNkYTgwYzFhNTdjYiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VW5pdmVyc2l0eSBvZiBOZXcgQnJ1bnN3aWNrIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfY2Q4NjhhNTU4MzliNDZlYzgwNzNkYTJjYzE4MDM5NmYuc2V0Q29udGVudChodG1sXzU3OGRjMWVmNjE5NDQ2YWU4NmNhY2RhODBjMWE1N2NiKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2U2OTljZmVkZWY5MDQyNjZhMDBlN2MzYzk3NjlkMDAyLmJpbmRQb3B1cChwb3B1cF9jZDg2OGE1NTgzOWI0NmVjODA3M2RhMmNjMTgwMzk2Zik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80YmMzYmE3NzNhMTg0YzczOWI5MjA3MTQ0ZDg3NmMzNyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQ1Ljk2ODgwMiwtNjYuNjIyNzM4XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiM4MDAwZmYiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjODAwMGZmIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2M2ZDZlOWJmZGFkNzQ4M2FhNzVjZTA4ZTBkN2ZlMjhlKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2ZmNjRiYzQxMjAzZDQ3MzVhNWIyODAzMjdkMzFkMGVhID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzQ0OTU1NTA0M2Y0NDQxYTFhMjVmMTA4MmYwMWRhOThiID0gJCgnPGRpdiBpZD0iaHRtbF80NDk1NTUwNDNmNDQ0MWExYTI1ZjEwODJmMDFkYTk4YiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RGV2b24gQ2x1c3RlciAxPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9mZjY0YmM0MTIwM2Q0NzM1YTViMjgwMzI3ZDMxZDBlYS5zZXRDb250ZW50KGh0bWxfNDQ5NTU1MDQzZjQ0NDFhMWEyNWYxMDgyZjAxZGE5OGIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNGJjM2JhNzczYTE4NGM3MzliOTIwNzE0NGQ4NzZjMzcuYmluZFBvcHVwKHBvcHVwX2ZmNjRiYzQxMjAzZDQ3MzVhNWIyODAzMjdkMzFkMGVhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzMyZTlkZTIwNmJmNDRlMGE4YTNkZTgwNGIzMjZjZmJmID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDUuODkyNzk1LC02Ni42ODM2NzNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmYjM2MCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZmIzNjAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYzZkNmU5YmZkYWQ3NDgzYWE3NWNlMDhlMGQ3ZmUyOGUpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNjZiYzRiZTZiZjJlNDE3NjliZTVkZjk2NzkwNmQyYjYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNzM4NzNmM2RkOTA5NDQxNzllMTFiMmRhNDUyMGRkM2UgPSAkKCc8ZGl2IGlkPSJodG1sXzczODczZjNkZDkwOTQ0MTc5ZTExYjJkYTQ1MjBkZDNlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5OZXcgTWFyeWxhbmQgQ2x1c3RlciA0PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF82NmJjNGJlNmJmMmU0MTc2OWJlNWRmOTY3OTA2ZDJiNi5zZXRDb250ZW50KGh0bWxfNzM4NzNmM2RkOTA5NDQxNzllMTFiMmRhNDUyMGRkM2UpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMzJlOWRlMjA2YmY0NGUwYThhM2RlODA0YjMyNmNmYmYuYmluZFBvcHVwKHBvcHVwXzY2YmM0YmU2YmYyZTQxNzY5YmU1ZGY5Njc5MDZkMmI2KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzNmYzZmYjI0MmUyMDQ5ODFiZWI0ZDhmOGU2YzU2NzZjID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDUuOTc4OTEzLC02Ni41ODk0OTFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzgwMDBmZiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiM4MDAwZmYiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYzZkNmU5YmZkYWQ3NDgzYWE3NWNlMDhlMGQ3ZmUyOGUpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMWM1NGNmMjU3Zjk3NDgyMWI1NzZjYmI3MmJkZTBiYTcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZGIzZTJiYjliZmRlNDUwYTk0OGE2MGI1NDNkYjUyOGQgPSAkKCc8ZGl2IGlkPSJodG1sX2RiM2UyYmI5YmZkZTQ1MGE5NDhhNjBiNTQzZGI1MjhkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5NYXJ5c3ZpbGxlIENsdXN0ZXIgMTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMWM1NGNmMjU3Zjk3NDgyMWI1NzZjYmI3MmJkZTBiYTcuc2V0Q29udGVudChodG1sX2RiM2UyYmI5YmZkZTQ1MGE5NDhhNjBiNTQzZGI1MjhkKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzNmYzZmYjI0MmUyMDQ5ODFiZWI0ZDhmOGU2YzU2NzZjLmJpbmRQb3B1cChwb3B1cF8xYzU0Y2YyNTdmOTc0ODIxYjU3NmNiYjcyYmRlMGJhNyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl82NTE1Y2UyZmQ0NGE0YzM3YTdlZmM0M2E2MjhmOTJlNCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQ1LjkzMTgyNywtNjYuNjQwMzM5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiM4MGZmYjQiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjODBmZmI0IiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2M2ZDZlOWJmZGFkNzQ4M2FhNzVjZTA4ZTBkN2ZlMjhlKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzQ5YmJmOTJkZDg0NjQ0NjI5YWE4MDA4NTA3MjBhYjY0ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzYxOTZjNzBiMGJmMzQ0MTFiOGVmODkzODJmYzg1MjNkID0gJCgnPGRpdiBpZD0iaHRtbF82MTk2YzcwYjBiZjM0NDExYjhlZjg5MzgyZmM4NTIzZCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+U2t5bGluZSBBY3JlcyBDbHVzdGVyIDM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzQ5YmJmOTJkZDg0NjQ0NjI5YWE4MDA4NTA3MjBhYjY0LnNldENvbnRlbnQoaHRtbF82MTk2YzcwYjBiZjM0NDExYjhlZjg5MzgyZmM4NTIzZCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl82NTE1Y2UyZmQ0NGE0YzM3YTdlZmM0M2E2MjhmOTJlNC5iaW5kUG9wdXAocG9wdXBfNDliYmY5MmRkODQ2NDQ2MjlhYTgwMDg1MDcyMGFiNjQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMWViY2U1ODRkMzExNDQzODkwMTYxYjE1ZDVlNTk0MDYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0NS45MDIzMTUsLTY2Ljc1NTExM10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjMDBiNWViIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzAwYjVlYiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9jNmQ2ZTliZmRhZDc0ODNhYTc1Y2UwOGUwZDdmZTI4ZSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9iMTQzMjExMTMxN2E0M2IwOTUxNGM2ZDI1OGY3YjI1YSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8yZTM4YWY5ZGFmNzM0NWVjYjk2OGQ3NzY3MGFjMTQ4NiA9ICQoJzxkaXYgaWQ9Imh0bWxfMmUzOGFmOWRhZjczNDVlY2I5NjhkNzc2NzBhYzE0ODYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkhhbndlbGwgQ2x1c3RlciAyPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9iMTQzMjExMTMxN2E0M2IwOTUxNGM2ZDI1OGY3YjI1YS5zZXRDb250ZW50KGh0bWxfMmUzOGFmOWRhZjczNDVlY2I5NjhkNzc2NzBhYzE0ODYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMWViY2U1ODRkMzExNDQzODkwMTYxYjE1ZDVlNTk0MDYuYmluZFBvcHVwKHBvcHVwX2IxNDMyMTExMzE3YTQzYjA5NTE0YzZkMjU4ZjdiMjVhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzI5MmQwZTFhOGZkZjQ1YmNiOTBiZjkzNDA5MzUyZmJkID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDUuOTU4MzI3LC02Ni42NDcyMTFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzgwMDBmZiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiM4MDAwZmYiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYzZkNmU5YmZkYWQ3NDgzYWE3NWNlMDhlMGQ3ZmUyOGUpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMjRjYjc3MTA3NjNhNGMxNWI1ZDc3ZDc1NWE3MGRkNDkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOGM5MmVmYzM3YzNlNGE5MWFhMTc5OGE3MWFlMzViZDkgPSAkKCc8ZGl2IGlkPSJodG1sXzhjOTJlZmMzN2MzZTRhOTFhYTE3OThhNzFhZTM1YmQ5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Eb3dudG93biBDbHVzdGVyIDE8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzI0Y2I3NzEwNzYzYTRjMTViNWQ3N2Q3NTVhNzBkZDQ5LnNldENvbnRlbnQoaHRtbF84YzkyZWZjMzdjM2U0YTkxYWExNzk4YTcxYWUzNWJkOSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8yOTJkMGUxYThmZGY0NWJjYjkwYmY5MzQwOTM1MmZiZC5iaW5kUG9wdXAocG9wdXBfMjRjYjc3MTA3NjNhNGMxNWI1ZDc3ZDc1NWE3MGRkNDkpOwoKICAgICAgICAgICAgCiAgICAgICAgCjwvc2NyaXB0Pg==" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>




```python

```