from sklearn.linear_model import LinearRegression
import pandas as pd
# TODO: Add import statements


# Assign the dataframe to this variable.
bmi_life_data = pd.read_csv("resource/bmi_life_expectancy.csv")

#print bmi_life_data['Life expectancy']
#print bmi_life_data['BMI']

# Make and fit the linear regression model
bmi_life_model = LinearRegression()
bmi_life_model.fit(bmi_life_data[['BMI']],bmi_life_data[['Life expectancy']])

# Make a prediction using the model
# TODO: Predict life expectancy for a BMI value of 21.07931
laos_life_exp = bmi_life_model.predict(21.07931)

print laos_life_exp
