"""Making a choropleth map of unemployment (2009) in each county in the US."""

### imports
import pandas as pd
from bs4 import BeautifulSoup


### Map colors from http://colorbrewer2.org/#type=sequential&scheme=Blues&n=6
colors = ['#eff3ff', '#c6dbef', '#9ecae1', '#6baed6', '#3182bd', '#08519c']


### Read the unemployment info
unemployment = pd.read_excel('unemployment2009.xlsx', 'Sheet1')


### Load the SVG base map
svg = open('us_counties.svg', 'r').read()
soup = BeautifulSoup(svg, 'html.parser')
paths = soup.findAll('path')


### Change colors accordingly
path_style = 'font-size:12px; fill-rule:nonzero; stroke:#FFFFFF; ' \
             'stroke-opacity:1; stroke-width:{}; stroke-miterlimit:4; ' \
             'stroke-dasharray:none; stroke-linecap:butt; ' \
             'marker-start:none; stroke-linejoin:bevel; fill:{}'
for p in paths:
    if p['id'] in ["State_Lines"]:
        p['style'] = path_style.format(1, 'none')
    else:
        #deal with some inconsistency in the data and map
        try:
            rate = unemployment[unemployment['FIPS'] == int(p['id'])]['RATE'].values
            county = unemployment[unemployment['FIPS'] == int(p['id'])]['COUNTY'].values
        except:
            continue

        if len(rate) > 0: # Lines 38-54 Revised on 11/12/2023
            rate_value = rate[0]
            if rate_value > 10:
                color_class = 5
            elif rate_value > 8:
                color_class = 4
            elif rate_value > 6:
                color_class = 3
            elif rate_value > 4:
                color_class = 2
            elif rate_value > 2:
                color_class = 1
            else:
                color_class = 0
        else:
            # Handle the case when the rate is not available for the current county
            color_class = 0  # You can set it to a default color class or do something else

        color = colors[color_class]
        p['style'] = path_style.format(0.1, color)
        
        #print(p['id'], str(color_class), str(county), str(rate))


### Save the results
fo = open("us_counties_unemployment.svg", "w")
fo.write(str(soup))
fo.close()