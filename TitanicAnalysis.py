#Khushi Chauhan(0722283)

# Technique: Sunburst Chart that shows data for titanic ship. Based on the category of
# ticket: first class, sencond class and third class(depending on the fare
# attribute), the data is divided into the number of male and female that
# bought the ticket and each category,how many number of males and females
# survived and did not survive

import plotly.express as px
import pandas as pd

# Load the Titanic dataset
titanic = pd.read_csv("titanic.csv")

# Map survival status to categorical values
titanic['Survived'] = titanic['Survived'].map({0: 'Not Survived', 1: 'Survived'})

# Prepare the data for the sunburst chart
fig = px.sunburst(
    titanic,
    path=['Pclass', 'Sex', 'Survived'],
    title='Titanic Passenger Analysis(Khushi Chauhan - 0722283)',
    labels={'Pclass': 'Ticket Class', 'Sex': 'Gender', 'Survived': 'Survival Status'},
    color='Fare',
    hover_data={'Fare': ':,.2f'},
)

# Show the plot
fig.show()

#dataset: https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv
#references: https://plotly.com/python/sunburst-charts/

