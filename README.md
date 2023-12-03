## **House Price in Washington, USA between 1900 - 2014**

Aims: 
1. To determine whether a machine learning model would be effective in predicting the price of houses based on the selected categories. 
2. To create an interactive page that allows users to select the number of bedrooms and bathrooms, the size of the land, and the year the house was built in order to determine the price of the house. 


## **Data and Data Delivery** 

The dataset used for this was retrieved from Kaggle via https://www.kaggle.com/datasets/shree1992/housedata. 
we cleaned the data set to get the columns for price, bedroom, bathroom sqft living sqft built

![image](https://github.com/shaylahong/P4/assets/134757827/87fcb9ea-c0b2-474c-9214-a4050e4ce564)
we then tested the data using the machine learning models 
1. Linear Regression 
2. Decision Tree 
3. Random Forest

We found that the linear regression model returned a higher R-squared value in comparison to the decision tree and random forest model. This indicates that the linear regression model is more likely to yield a higher accuracy in predicting house prices. 

Linear Regression 
![image](https://github.com/shaylahong/P4/assets/134757827/e0e94142-774a-4466-b338-cebf129c62c8)

Random Forest 
![image](https://github.com/shaylahong/P4/assets/134757827/b2aff9c3-ca55-4cc6-b97a-78a52c03b534)

Desision tree
![image](https://github.com/shaylahong/P4/assets/134757827/f86c7e22-2337-4610-be78-4ffb31388c05)

As a result, we chose to utilise the trained linear regression model to predict house prices. 

The webpage is designed to predict house prices when the user inputs the number of bedrooms, number of bathrooms, square footage of living area, and the year it was built. 

We sourced assistance from a variety of resources such as Stack Overflow, as well as trial and error to determine which parts of the code required modification in order to attain the desired output. 

