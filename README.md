# Congressional Twitter Dataset Organizer
A tool to organize tweets by members of the United States Congress. Includes party, state/district, chamber, date information and more!
## Currently implemented:
  * by party (all time)
  * by state (all time)
  * by state and party (all time)
  * by n-week and party
  
Note that the datasets included are from 1 January 2020 to 28 July 2020 and only include members serving in the 116th United States Congress as of 28 July 2020. Members of the 116th United States Congress who have resigned or passed away before this time are not included (ex. Rep. Hill (D-CA), Rep. Lewis (D-GA)), but any new or previous members may be added via the legislators-current.csv file and findauthor.py file.  

Please reach out if you'd like to get the pickle files so that you don't have to compile from scratch (however, the data set may be old).

# Acknowledgements
Source for raw twitter data: https://github.com/alexlitel/congresstweets.

Exact source for raw twitter data: https://github.com/alexlitel/congresstweets/tree/master/data.

Includes other non-individual accounts (e.g. Caucus accounts).

This source is updated daily, the datasets included on this repo are updated as of 7/28/20.
