# <p align="center" dir="auto">Price Elasticity</p>
<div align="center">
<img src="https://github.com/pedrocortez09/price_elasticity/assets/103151311/5b0e8e69-0de3-4d21-b781-6d041481bfc4" width="700" />
</div>

# 1. Business Problem.

In this public dataset, we have various sales data from well-known E-commerce companies such as Best Buy and Walmart. Our goal is to identify potential products that have room for increasing the store's REVENUE. The final outcome is expected to be a list of products with the greatest possibilities for revenue growth, along with the amount of money that will be risked and the return it can bring.


# 2. Business Assumptions.

Although in the dataset I have daily sales, I grouped the sales by week in order to have a larger time measure. Additionally, for each week, I replaced the sales value with the average price for that week, so we can observe the weekly price variation along with the weekly demand.
Some weeks had null prices because there were no sales. Therefore, for these values, I replaced the price with the overall median for that product and the demand with zero.


# 3. Solution Strategy

Our goal is to fit the best regression line to the data, in this case, price x demand. For this, we will use the method of least squares from the StatsModel library.

After plotting the line, we will perform a statistical test to check the R² and p-value to evaluate how well the line was fitted. For this:

- Data description to identify null and missing values;
- Descriptive statistics of the data to get an idea of the distributions;
- Define the columns of the dataset and group it by period;
- After defining the dataset, we will divide it into two: demand per week and price per week;
- The first one will contain the prices of each product per week, and the second one will contain the demand;
- We will plot the regression line and perform the statistical test for each product using the OLS library from Stats Models;
- We will check which products fall within the probability range set in the statistical test;
- We will calculate the potential return with an example discount.


# 4. Machine Learning Model Applied

The OLS (Ordinary Least Squares) library from StatsModels is a powerful and widely used tool for conducting linear regression analysis. It allows fitting regression models and calculating coefficients that best fit observed data. The OLS regression method is commonly employed to find the line or plane that best fits a dataset with a response variable and multiple explanatory variables.

Key features of the StatsModels OLS library include model fitting for simple and multiple linear regression, weighted and robust regression, automatic estimation of regression coefficients using the least squares method, and the calculation of fit statistics like R² to measure the proportion of variance explained by the model. Additionally, it provides various statistical tests for model significance and individual coefficient significance, as well as tools for residual analysis to assess model adequacy and detect potential regression assumptions violations.

Overall, the StatsModels OLS library is a powerful tool used for regression analysis, enabling researchers to explore relationships between variables and make predictions in various fields such as statistics, economics, and data science.

# 5. Business Results

## As a result of the products that passed the statistical test, we have:
<img src="https://github.com/pedrocortez09/price_elasticity/assets/103151311/5af2f52e-b69a-4301-92d5-915923ffe9c0" width="700" />

- In this case Apple Macbook Air would be the most sensitive to a price change

##  The financial outcome assuming we would give a 10% discount on these products would be:
<img src="https://github.com/pedrocortez09/price_elasticity/assets/103151311/616afd26-745f-491b-a257-ae2c09343f11" width="700" />

Where:

- faturamento_atual: Standard product revenue
- faturamento_reducao: 10% discount applied to the revenue
- perda_faturamento: Basically the money we would put at risk
- faturamento_novo: New revenue if the demand changes as planned
- variacao_faturamento: Difference in revenues (profit if the discount is applied)
- variacao_percentual: percentage gain over the standard revenue.

# 6. Conclusions

From the list of considered products, we identified 4 in which giving a 10% discount could bring a **259.55%** increase in store revenue in the same period.

 
