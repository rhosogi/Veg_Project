Renee Hosogi
Meat and Produce Consumption in the US

Introduction

Over the last decade, there has been an increasing interest in food production in regards to the rising global population. This is largely due to articles like the one the United Nations produced concerning an alarming population increase in developing countries, showing the population rising to 9.8 billion people by 2050.  This estimate is based on 2010 censuses from 233 countries and other demographic data. While this data could be grossly hyped up, as much media tends to do, it raised a pivotal question: how will we feed the world? 

Sci-Fi genres aside, growing economic and health-related awareness in the United States could be seen through various media outlets, including an enthusiastic Michelle Obama. Through this raised awareness, one of the working hypotheses of many scientists and economists has been to reduce meat intake, and increase produce and vegetable-protein intakes.  Vegetable protein and produce production were long thought to be more economical in comparison to meat production in terms of space, time, and energy, but the choices in such matters have been limited. Recently, more plant alternative proteins have been making the news and hitting markets. However, what I aim to explore in this paper is whether or not consumers are following the media blitzes through actual expenditure. 

Hypothesis

If American consumers are becoming increasingly food-conscious, then they are also buying more food-conscious and we can see that in the form of buying less meat. Should this be true across five years of data, then applications would include helping the FDA develop more guidelines for lab-grown vegetable and meat protein alternatives; more dedicated research to long-term effects on health and resources; and global food production initiatives. If the UN’s population prediction were accurate, it would be necessary to have these assurances for safety and health reasons.

Method

Using the Consumer Expenditure reports from the Bureau of Labor Statistics from 2010-2014, I initially explored the most recent five years of food data. I used the diary data, specifically pulling in the fmld CSV files, as the diary data is collected over 2 consecutive weeks, 4 times a year. It is meant specifically for smaller ticket items such as food purchases while the interview data is used for larger ticket items, such as cars and houses. There are four fmld CSV files in each diary data zip file, showing the data from each quarter that the surveyors were able to collect. This data has approximately 538 columns and 6,000-11,000 rows. Each column represents a different purchase while each row represents a different household. Using cat method in the command line, I was able to combine the four quarters for annual data concerning how much meat and produce each household bought for that year. The basic command line function for this was:

Renees-MacBook-Pro:diary10 reneehosogi$ cat < fmld101.csv <(tail +3 fmld102.csv) <(tail +3 fmld103.csv) <(tail +3 fmld104.csv) > veg10.csv

Doing this for each year, I was able to get the amount spent on each food item, which I then made columns for in Python. I labeled one column ‘MEAT’, which comprised of ‘BEEF’, ‘POULTRY’, ‘PORK’, ‘SEAFOOD’, and ‘OTHMEAT’. Next, I made a column for ‘PRODUCE’, comprised of ‘FRSHFRUIT’, ‘FRSHVEG’, ‘PROCFRUT’, and ‘PROCVEG’.  Below are the results and analysis, followed by a revised method and analysis. 

Results and Analysis

One of the main components that I first explored was the money spent on meat versus produce. After initial results, I noticed that meat consumption seemed to be much higher. This wasn’t inline with my initial hypothesis, nor was it the suggested USDA diet. While I know that not everyone follows the food pyramid to the tee, I remembered that on the general whole, meat was more expensive than produce. I checked this across three different variables: family size, region, and age. 

  
Figure 1
Meat and produce consumption in 2014, measured by family size. Produce is scaled to $600 while meat is scaled to $1200.
  
Figure 2
Meat and produce consumption in 2014, measured by region. Produce is scaled to $600 while meat is scaled to $1200.

  
Figure 3
Meat and produce consumption in 2014, measured by age. Produce is scaled to $600 while meat is scaled to $1200.

Once I noted this, I used the US Department of Labor’s annual price reports to average the yearly costs of meat, produce, and processed produce to come up with average prices per unit of food type. Below is the table of price per pound that I used to divide the cost of each food product:

| Year   | Beef        | Poultry     |  Pork       | Other Meat | Fresh Fruits| Fresh Veg |Proc Fruits | Proc. Veg  |
|        | (per 500 g) | (per 500 g) | (per 500 g) | (per 500 g)| (per 500 g) |(per 500 g)| (per 500 g)|(per 500 g) |
| :----: |:-----------:|:-----------:|:---------:|:----------:|:------------:|:----------:|:----------:|:----------:|
| 2014   |    $5.71    |    $2.04    |   $3.83   |   $3.01    |   $1.49      |   $1.57    |   $2.53    |   $1.47    |
| 2013   |    $4.76    |    $2.02    |   $3.43   |   $3.05    |   $1.29      |   $1.49    |   $2.51    |   $1.42    |
| 2012   |    $4.57    |    $1.97    |   $3.37   |   $2.92    |   $1.34      |   $1.42    |   $2.66    |   $1.44    |
| 2011   |    $4.34    |    $1.89    |   $3.35   |   $3.15    |   $1.33      |   $1.58    |   $2.76    |   $1.42    |
| 2010   |    $5.26    |    $1.96    |   $3.10   |   $3.22    |   $1.32      |   $1.15    |   $2.47    |   $1.33    |

Unfortunately, regional costs per units weren’t posted, which would have given the numbers above another level of accuracy. The prices averaged were taken from the US averages of different product types, including different cuts of meats and different types of produce. Please see the attached appendix for the list of cuts of meat and types of produce factored into the price per unit averages.

Next, I made two new columns for number of meat units purchased and number of produce units purchased by taking each type of meat (beef, poultry, pork, and other meat) and each type of produce (fresh fruits, fresh vegetables, processed fruits, and processed vegetables) and dividing the columns by the appropriate price per unit. 

The numbers that came out for meat in 2014 looked like this:
 

With produce in 2014 looking like this:
 

Over 2013 and 2014, meat and produce looked like this:

   

However, when reading in 2010-2012, the numbers spiked. Both meat and produce by unit increased ten times when looking at the data from 2010, 2011, and 2012. At first I thought that this could be because more consumers were eating out than before, especially because of historical data (stock market crash in 2008). However, when I looked at the money spent on food at home versus the money spent on the food away, this is the chart that I got:

  

The increase between 2010-2014 wasn’t great enough to merit the high jump, so I looked for another reason. When looking at the raw data for each of the meat and produce components, I noticed that the means on the general whole were much higher, but when going into the individual quarter files, I noticed that the mean averages for all of the different products were much lower than what I was seeing in Python, so I remade the all-up CSV files with the annual data. What came through after the remade CSV files were these graphs of meat units purchased by region:

 
 

When comparing meat and produce consumption by family size this is what we see:

   

From these visualizations concerning regions and family size, we can see that the meat and produce consumption remain fairly consistent, with meat having a slightly positive linear trend and produce having a minor negative trend. From the meat and produce consumption graphs by family size, we generally see a mutual increase in meat and produce as family size increases. This means that in fact people are eating more meat and not less, regardless of the price of meat increasing in the last five years. Economically, there isn’t evidence to support my initial hypothesis, in that price increases would deter people from eating more meat. Measuring meat-intake on a social level would be interesting, but I’m not sure about getting that data to show in a non-biased way.

Prediction Modeling 

One of the most important parts of this project has been showing accurately what consumers are buying in terms of meat and produce. I think that while the initial model might be linear, given more data it might prove to be more complex. 

Conclusion

One of the next steps I would like to take would be to take more data from previous years to paint a bigger picture. This was an idea I had in the initial stages of my project, but I wanted to make sure that I could achieve this first. 

Further research

I would like to continue into more consumer expenditure reports and continue building an initial database for food data. I think this would make it easier to see whether or not the trend line is accurate for any sort of predictive modeling.  

Another set of data that I’d like to explore more is the USDA’s Food Availability (per capita) data. This is used to show food availability, food loss, and nutrient availability, but I think it would be interesting to take some of that info and cross-reference it to the data I have to show price of foods, consumer consumption, and food loss and see if there’s any correlation. 
