# Inbank homework

## Part 1: Aggregated Monthly Payments (SQL)

Using four tables (payments, currencies, exchange rates, blacklist), please write a query to return the amounts in euros aggregated by transaction_date.

To run: 

`cd WeekendDatProcessing && python3 combine_csvs.py data_2023-02-11.csv data_2023-02-12.csv`

This was fairly straight-forward. I used mostly LEFTJOIN to get the valid data, taking into account the currencies that had expired, users on blacklist, correct currency_id. There was some ambiguity with the blacklist, since there was an end date aswell meaning that the user could be whitelisted after some time period and this needed to be taken into account. A similar date that should've been taken into consideration was the exchange date and transaction date relation. The line "OR c.END_DATE >= p.TRANSACTION_DATE" checks if the currency was still valid during the time of the transaction.

## Part 2: Weekend Data Processing (Python)

#### Input: 2 csv files with aggregated data for Saturday and Sunday.

####  Output: 1 csv file with Saturday and Sunday data combined.

This required some consideration as there was three things to ponder:

Firstly, the question of how to sort the data arose: should it be done by date or by metric_id? The decision was made to opt for the latter as it enhances readability and comprehension, especially when scanning through the data.

Second issue was the aggregation of both files. To maintain the granularity of the data and ensure that each weekend's metrics are accurately represented without introducing anomalies, the appropriate approach was to append the data from each day to create a combined CSV file. This preserves the original metric dates for each record, allowing for accurate analysis and reporting.

By appending the data and sorting it, we ensure that each day's data is distinct and identifiable. This approach aligns with the goal of maintaining data integrity and avoiding anomalies in the combined dataset. 

Lastly the issue of naming. Sticking to the naming convention of the original files and it was decided to rename the files to be more descriptive. There could be a problem with shorter names when the weekend falls at the end of the month or at the end of the year and thus both days are mentioned in addition to the "combined" keyword.



