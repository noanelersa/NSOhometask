# NSOhometask

This project is a Python-based pipeline to fetch, transform, and store asteroid data from the NASA Web Service. It fetches asteroid data using the NASA API, transforms raw data and extract the required fields, stores data into a SQLite database and processes the stored data to provide insights (for example, the 5 largest asteroids).

usage:
run the pipeline- "python main.py"

API:
    handels the requests and responses from the API- in our case- NASA API.
database:
    handels the connection to the db (sqlite). supports creation, insertion and query execusions.
pipelines:
    does the pipeline steps: fetching, transform, store, proccess.
transformers:
    transforms raw API data into a format suitable for database storage as required.
config.py:
    define reusable constants for a simple way to make a minor edit of the code.
main.py:
    runs the pipeline which handels all the steps

example of output of the 5 largest:
    [('152931 (2000 EA107)', 3206.5644897089, '2024-12-22', 27.8999562208), ('(2014 HQ124)', 977.3271842103, '2024-12-22', 18.7140123696), ('302169 (2001 TD45)', 594.3468684194, '2024-12-21', 22.9888639604), ('(2022 MO2)', 430.566244241, '2024-12-20', 14.5645255921), ('(2016 LL1)', 304.8175575085, '2024-12-20', 22.1494548862)]

future improvments:
    -add unit test
    -utilize Docker and use loggers instead of prints

contributors:
    Noa Nelersa
