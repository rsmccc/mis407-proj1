# MIS 407 Group Project

Our team is named MTSF and consists of Michael Tuttle, Riley McCloskey, William Smith, and Miranda Fisher. 

Many different open data sources were found online. A few of these include Google Data Explorer, Gov’t Open Data, Quandl, Awesome Public Datasets, and Open FEC API Documentation.

We have developed a specific question after reviewing several different data sources. Is there any correlation between financial capital (in dollar amounts) donated to specific political parties or party members and their success in elections?

We have compiled a list of specific data sources that we have chosen to use. The first is 2009 Campaign Contributions to candidates for the City of New York on Data.gov. Next we are using data on each candidate who has registered with the FEC for election to the U.S. House of Representatives, U.S. Senate, or U.S. President in 2012. Thirdly we will be using Federal Election Commission data relating to 2012 political committees and their financial contributions to candidates. Our fourth and fifth sources are a list of only top candidates for the 2012 and 2016 elections that are registered with FEC. These sources show a wide variety of data that will be combined to find answers to our question. 

There are several relevant columns between each specific data source that we have chosen which will help to create specific data needed to provide factual answers. In the 2009 Campaign Contributions for the City of New York we are using Candidate Last Name, Candidate First Name, Amount, and Location.

From the 2012 candidate data in FEC for election to the U.S. House of Representatives, U.S. Senate, or U.S. President we will use Candidate Name, Total Receipts, Total Disbursements, Cash on Hand, and Debts Owed by Committee.
On the Federal Election Commission data relating to 2012 political committee financial contributions we will use Committee Name, Total Receipts, Total Disbursements, and Ending Cash On Hand.

From the list of only top candidates for the 2012 and 2016 elections that are registered with FEC we are using Contribution Receipt Amount, Candidate Party Affiliation, Individual Contribution, and Candidate Name Title columns.

Using the sources listed above to answer our specific question will require a detailed outline of tasks. First of all, we will need to read each of our data files into Python as a data frame. Once this is complete we will start actually manipulating each column listed above. For the 2009 Campaign Contributions for the City of New York we will identify the maximum dollar amounts and order the column from highest to lowest. We will then use this data to create a histogram of the top candidates and their contributions. We will identify candidates by the Candidate Last Name, Candidate First Name, and Location columns.
For the 2012 candidate data in FEC for election to the U.S. House of Representatives, U.S. Senate, or U.S. President we will compare the Total Receipts and Total Disbursements columns. For those candidates with the greatest resulting values we will read their data into a histogram. We will also compare the amount of Cash on Hand to Debts Owed by each Committee. After identifying each candidate with the Candidate Name column we will be able to see how much risk each committee was willing to put into their respective candidate.

On the Federal Election Commission data relating to 2012 political committee financial contributions we will identify each committee with the Committee Name column. After this we will compare each committee by their Total Receipts and Total Disbursements to see which ones donates the highest amount. We will also read the committees with the highest Ending Cash On Hand columns into a histogram.

With the list of only top candidates for the 2012 and 2016 elections that are registered with FEC we will do a number of comparisons. First we will group contribution receipt amounts by candidate party affiliation. We will then do the same with individual contribution amounts and candidate party affiliation. After this we will get more specific and compare contribution receipt amounts to individual candidate names. By doing this for the past and current election we will be able to see election trends between parties and top candidates.


