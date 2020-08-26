import sqlcheck
import re

filepath = 'C:\\Users\\chris\\OneDrive\\National Park\\2017.csv'
with open(filepath, "r") as ifile:
    for line in ifile:
        line=re.sub(r'(?!(([^"]*"){2})*[^"]*$),', '', line).split(',')
        agency=None
        park=None
        campground=None
        agency=line[2].strip('"')
        park=line[6].strip('"')
        campground=line[10].strip('"')
        campgroundstate=line[18].strip('"')
        campgroundlon=line[19].strip('"')
        campgroundlat=line[20].strip('"')
        custzip=line[21].strip('"')
        custstate=line[22].strip('"')
        custcountry=line[23].strip('"')
        totalpaid=line[29].strip('"')
        startdate=line[30].strip('"')
        enddate=line[31].strip('"')
        orderdate=line[32].strip('"')
        numberofpeople=line[33].strip('"')
        if line[2].strip('"')=="NPS":
            park=line[6].strip('"')
        if line[2].strip('"')=="USFS":
            park=line[8].strip('"')
            print(park,campground,campgroundstate,campgroundlon,campgroundlat,custzip,custstate,custcountry,totalpaid,startdate,enddate,orderdate,numberofpeople)
        if agency=='NPS' or agency=='USFS':
            sqlcheck.insertresrvation(agency,park,campground,campgroundstate,campgroundlon,campgroundlat,custzip,custstate,custcountry,totalpaid,startdate,enddate,orderdate,numberofpeople)
            

