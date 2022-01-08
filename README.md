# L.I.S.A.
Learning Intelligent Super Algorithm

Fun little project to help people write speeches. Aka most sophisticated way to cheat/plagiarise speech script writing that I can think of.

## To run docker 
 ```
 docker-compose up -d
 ```
## Running the app
To fun the Streamlit application:
```
make app
```
## Project layout 
```
project
│   README.md
│   docker-compose.yml
│
└───webscraping (golang)
│
└───neural_net (python)
        │
        └───data_cleaning
```
The webscraping folder collects TedX transcripts from their website in Golang using Colly.

The neural-net folder trains a deep learning model to predict the next words after an input word.
