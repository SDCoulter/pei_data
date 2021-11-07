# PEI Open Data Analysis

Exploratory analysis on Prince Edward Island datasets.

## 03_Elections

### 2019 Provincial Election - PEI

* Scraping data from [Elections PEI](https://www.electionspei.ca/2019-election-results) website, forming simple datasets to be used in visualizations.
* Using the [Represent Open North](https://represent.opennorth.ca/) API we gather more information about the districts.

**/elections_transformed/**:

* _01_2019_provincial_election_summary.csv_ - summary DF containing the Popular Vote, Percent, and Leading values by Party.
* _02a_2019_provincial_election_district_counts.csv_ - votes for each party separated by district.
* _02b_2019_provincial_election_district_counts_by_dist.csv_ - as above, but transposed.
* _03_district_dict.pkl_ - pickle file to store the returned DataFrames for each district (vote counts for each party, etc)
* _04a_2019_pe_district_counts_by_dist_named.csv_ - counts as above (02) but containing district names, transposed.
* _04a_2019_pe_district_counts_named.csv_ - counts as above (02) but containing district names.
* _04_district_dict_fin.pkl_ - all individual district DataFrames transformed and saved as a pickle object.
* _05_2019_pe_district_api_links.csv_ - URLs for each district to gather further information.
* _individual_districts/_ - individual DataFrames for each district with voting information (from 04 pickle).

### _Previous Election Data Analysis:_

* 01 - 03 - Campaign donation analysis - dataset: [Elections PEI - Open Data](https://www.electionspei.ca/resources/open-data), and more specifically [Yearly Political Party Contributions - Open Data](https://www.electionspei.ca/yearly-political-party-contributions-open-data)
