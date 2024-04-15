# Inbank homework

## Part 1: Aggregated Monthly Payments (SQL)

Using four tables (payments, currencies, exchange rates, blacklist), please write a query to return the amounts in euros aggregated by transaction_date.

This was fairly straight-forward. I used mostly LEFTJOIN to get the valid data, taking into account the currencies that had expired, users on blacklist, correct currency_id. There was some ambiguity with the blacklist, since there was an end date aswell meaning that the user could be whitelisted after some time period and this needed to be taken into account. This is the main reason the WHERE clause is as long as it is.

## Part 2: Weekend Data Processing (Python)

#### Input: 2 csv files with aggregated data for Saturday and Sunday.

####  Output: 1 csv file with Saturday and Sunday data combined.

This required some consideration as there was two things to ponder:

Firstly, the question of how to sort the data arose: should it be done by date or by metric_id? The decision was made to opt for the latter as it enhances readability and comprehension, especially when scanning through the data.

Second issue was the aggregation of both files. To maintain the granularity of the data and ensure that each weekend's metrics are accurately represented without introducing anomalies, the appropriate approach was to append the data from each day to create a combined CSV file. This preserves the original metric dates for each record, allowing for accurate analysis and reporting.

By appending the data and sorting it, we ensure that each day's data is distinct and identifiable. This approach aligns with the goal of maintaining data integrity and avoiding anomalies in the combined dataset. 



