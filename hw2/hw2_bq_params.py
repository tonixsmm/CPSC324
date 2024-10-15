import datetime
from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

county_param = input("Enter the county: ")
state_param = input("Enter the state: ")
year_param = input("Enter the year: ")
month_param = input("Enter the month: ")
day_param = input("Enter the day: ")

query = """
        SELECT TIMESTAMP_ADD(@ts_value, INTERVAL 0 SECOND) as ts_value, county, state_name, confirmed_cases, deaths
        FROM `bigquery-public-data.covid19_nyt.us_counties`
        WHERE TIMESTAMP(date) = @ts_value AND county = @county AND state_name = @state_name;
        """

job_config = bigquery.QueryJobConfig(
    query_parameters=[
        bigquery.ScalarQueryParameter("ts_value", "TIMESTAMP", datetime.datetime(int(year_param), int(month_param), int(day_param))),
        bigquery.ScalarQueryParameter("county", "STRING", county_param),
        bigquery.ScalarQueryParameter("state_name", "STRING", state_param),
    ]
)
query_job = client.query(query, job_config=job_config)  # Make an API request.

for row in query_job:
    print("Day: {} \n County: {} \n State Name: {} \n Confirmed case: {} \n Deaths: {}".format(row.ts_value, row.county, row.state_name, row.confirmed_cases, row.deaths))