#Title: Python project
#Name : Kerlwin Wong
#Group Name : Apeh Legend
#Class : PN2004L
#Date : 9 February 2021

#Import pandas for data analysis
import pandas as pd

#Define Class - Data Analyise
class DataAnalyse:
  def __init__(self):
    df = pd.read_csv('MonthlyVisitor.csv')
    SortCountry(df)
    UserPrompt(df)

#Start of Main Function
def SortCountry(df):
  #Print out the Whole File
  print("PART 1")
  #print("There are " + str(len(df)) +  " data rows. \n")
  #print(df)
  #print("\n-----Testing Line-----")
  #print(df.iloc[12:24])

  #Print Out Name of Columns
  #print(df.columns)

  #First, Limit the file to the Countries I need
  #Print Year and Month of (USA, Canada, Australia, New Zealand, Africa Columns)
  MonthsSelected = df[['Year','Month',' USA ',' Canada ',' Australia ',' New Zealand ',' Africa ']]
  #print("\nPrinting Out the Specific Countries")
  #print(MonthsSelected)

  #Print out Rows needed(Years) for the specific Countries
  #print("\nPrinting Out Years need for Specific Countries")
  YearsSelected = MonthsSelected.iloc[216:348]
  #print(YearsSelected)

  #Second,
  #Select Only the countries needed
  CountriesSelected = YearsSelected[[' USA ',' Canada ',' Australia ',' New Zealand ',' Africa ']]

  #Third,
  #Sum up the Columns(Countries) to obtain total amount of visitors in the 10 years span
  TotalVisitors = CountriesSelected.sum(axis=0)
  #print(TotalVisitors)

  #Lastly,
  #Display the top 3 Countires that visited Singapore in the span of 1996-2006
  MostVisitors_Descending = TotalVisitors.sort_values(ascending = False)
  Top3Countries = MostVisitors_Descending.head(3)
  print("\nThese are the Top 3 Countries that Visited Singapore in the years 1996-2006")
  print(Top3Countries)
#End of Function (SortCountry)

#Function for Part 2
def UserPrompt(df):
  #Variables
  Line1 = 0
  Line2 = 0
  df = pd.read_csv('MonthlyVisitor.csv')
  print("\nPART 2")
  print("\nPlease choose a region you want to be displayed")
  #Print Out menu for user to choose which region to show
  print("\nSouth-East Asia, Asia Pacific , South-Asia Pacific, Middle-East, Europe, North-America, Australia, Africa")
  PromptForRegion = True
  #Error checking and Loop
  while PromptForRegion == True:
      #Prompt User for the Region
      CountryChosen = input("Please input the region you desire:")
      #Check the user input for the Correct region
      if CountryChosen == "South-East Asia" or CountryChosen == "south-east asia":
        CountriesSelected = df[[' Brunei Darussalam ', ' Indonesia ',' Malaysia ',' Philippines ', ' Thailand ', ' Viet Nam ', ' Myanmar ']]
        PromptForRegion = False

      if CountryChosen == "Asia Pacific" or CountryChosen == "asia pacific":
        CountriesSelected = df[[' Japan ',' Hong Kong ', ' China ', ' Taiwan ', ' Korea, Republic Of ']]
        PromptForRegion = False

      if CountryChosen == "South-Asia Pacific" or CountryChosen == "south-asia pacific":
        CountriesSelected = df[[' India ',' Pakistan ', ' Sri Lanka ']]
        PromptForRegion = False

      if CountryChosen == "Middle-East" or CountryChosen == "middle-east":
        CountriesSelected = df[[' Saudi Arabia ', ' Kuwait ', ' UAE ']]
        PromptForRegion = False

      if CountryChosen == "Europe" or CountryChosen == "europe":
        CountriesSelected = df[[' United Kingdom ', ' Germany ', ' France ', ' Italy ', ' Netherlands ',' Greece ', ' Belgium & Luxembourg ', ' Switzerland ', ' Austria ',' Scandinavia ', ' CIS & Eastern Europe ']]
        PromptForRegion = False

      if CountryChosen == "North-America" or CountryChosen == "north-america":
        CountriesSelected = df[[' USA ', ' Canada ']]
        PromptForRegion = False

      if CountryChosen == "Australia" or CountryChosen == "autralia":
        CountriesSelected = df[[' Australia ', ' New Zealand ']]
        PromptForRegion = False

      if CountryChosen == "Africa" or CountryChosen == "africa":
        CountriesSelected = df[[' Africa ']]
        PromptForRegion = False

      else:
        print("Error! Wrong region name Entered.")
  #Print out the range of years
  print("\nPlease choose a year from start to finish")
  print("\nThe Range you can choose from is from 1978 to 2017")
  PromptForYear = True
  #Error Checking and Loop
  while PromptForYear == True:
    #Error Checking for Whether Inputs are Numeric
    Year1 = input("Please input the First year:")
    try:
      Year1 = float(Year1)
    except:
      print("Invalid format!")
    else:
      Year2 = input("Please input the Last Year:")
      try:
        Year2 = float(Year2)
      except:
        print("Invalid Format")
      else:
        Year1 = int(Year1)
        Year2 = int(Year2)
        print("You have chosen " + str(Year1) + " and " + str(Year2))
    #Error Check for Whether the in the Range of the years
    if Year1 >= 1978 and Year2 <= 2017:
      try:
        if Year1 > Year2:
          Store = Year2
          Year2 = Year1
          Year1 = Store
          #The Starting Year has to be at January Line, While the Ending Line needs to be at December Line, From #####1978-2017#####
        #The First Year
        if str(Year1) == "1978":
          Line1 = 0
        if str(Year1) == "1979":
          Line1 = 12
        if str(Year1) == "1980":
          Line1 = 24
        if str(Year1) == "1981":
          Line1 = 36
        if str(Year1) == "1982":
          Line1 = 48
        if str(Year1) == "1983":
          Line1 = 60
        if str(Year1) == "1984":
          Line1 = 72
        if str(Year1) == "1985":
          Line1 = 84
        if str(Year1) == "1986":
          Line1 = 96
        if str(Year1) == "1987":
          Line1 = 108
        if str(Year1) == "1988":
          Line1 = 120
        if str(Year1) == "1989":
          Line1 = 132
        if str(Year1) == "1990":
          Line1 = 144
        if str(Year1) == "1991":
          Line1 = 156
        if str(Year1) == "1992":
          Line1 = 168
        if str(Year1) == "1993":
          Line1 = 180
        if str(Year1) == "1994":
          Line1 = 192
        if str(Year1) == "1995":
          Line1 = 204
        if str(Year1) == "1996":
          Line1 = 216
        if str(Year1) == "1997":
          Line1 = 228
        if str(Year1) == "1998":
          Line1 = 240
        if str(Year1) == "1999":
          Line1 = 252
        if str(Year1) == "2000":
          Line1 = 264
        if str(Year1) == "2001":
          Line1 = 276
        if str(Year1) == "2002":
          Line1 = 288
        if str(Year1) == "2003":
          Line1 = 300
        if str(Year1) == "2004":
          Line1 = 312
        if str(Year1) == "2005":
          Line1 = 324
        if str(Year1) == "2006":
          Line1 = 336
        if str(Year1) == "2007":
          Line1 = 348
        if str(Year1) == "2008":
          Line1 = 360
        if str(Year1) == "2009":
          Line1 = 372
        if str(Year1) == "2010":
          Line1 = 384
        if str(Year1) == "2011":
          Line1 = 396
        if str(Year1) == "2012":
          Line1 = 408
        if str(Year1) == "2013":
          Line1 = 420
        if str(Year1) == "2014":
          Line1 = 432
        if str(Year1) == "2015":
          Line1 = 444
        if str(Year1) == "2016":
          Line1 = 456
        if str(Year1) == "2017":
          Line1 = 468

        #For Second Year
        if str(Year2) == "1978":
          Line2 = 12
        if str(Year2) == "1979":
          Line2 = 24
        if str(Year2) == "1980":
          Line2 = 36
        if str(Year2) == "1981":
          Line2 = 48
        if str(Year2) == "1982":
          Line2 = 60
        if str(Year2) == "1983":
          Line2 = 72
        if str(Year2) == "1984":
          Line2 = 84
        if str(Year2) == "1985":
          Line2 = 96
        if str(Year2) == "1986":
          Line2 = 108
        if str(Year2) == "1987":
          Line2 = 120
        if str(Year2) == "1988":
          Line2 = 132
        if str(Year2) == "1989":
          Line2 = 144
        if str(Year2) == "1990":
          Line2 = 156
        if str(Year2) == "1991":
          Line2 = 168
        if str(Year2) == "1992":
          Line2 = 180
        if str(Year2) == "1993":
          Line2 = 192
        if str(Year2) == "1994":
          Line2 = 204
        if str(Year2) == "1995":
          Line2 = 216
        if str(Year2) == "1996":
          Line2 = 228
        if str(Year2) == "1997":
          Line2 = 240
        if str(Year2) == "1998":
          Line2 = 252
        if str(Year2) == "1999":
          Line2 = 264
        if str(Year2) == "2000":
          Line2 = 276
        if str(Year2) == "2001":
          Line2 = 288
        if str(Year2) == "2002":
          Line2 = 300
        if str(Year2) == "2003":
          Line2 = 312
        if str(Year2) == "2004":
          Line2 = 324
        if str(Year2) == "2005":
          Line2 = 336
        if str(Year2) == "2006":
          Line2 = 348
        if str(Year2) == "2007":
          Line2 = 360
        if str(Year2) == "2008":
          Line2 = 372
        if str(Year2) == "2009":
          Line2 = 384
        if str(Year2) == "2010":
          Line2 = 396
        if str(Year2) == "2011":
          Line2 = 408
        if str(Year2) == "2012":
          Line2 = 420
        if str(Year2) == "2013":
          Line2 = 432
        if str(Year2) == "2014":
          Line2 = 444
        if str(Year2) == "2015":
          Line2 = 456
        if str(Year2) == "2016":
          Line2 = 468
        if str(Year2) == "2017":
          Line2 = 480

      finally:
        print("Line 1 is " + str(Line1) + " and Line 2 is " + str(Line2))
        PromptForYear = False

  CountryYear = CountriesSelected.iloc[Line1:Line2]
  print(CountryYear)

  FinalResult = CountryYear.sum(axis = 0)
  print("\nPrinting Top 3 Countries in the chosen Region and Period")
  TopChosen = FinalResult.sort_values(ascending = False)
  print(TopChosen.head(3))

#Main Code
if __name__ == '__main__':
  #Run Code
  DataAnalyse()
