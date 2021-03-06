# Compute the regression of '_VEGESU1' as a function of 'INCOME2' using SciPy's linregress().
# Compute the regression of '_VEGESU1' as a function of 'INCOME2' using StatsModels' smf.ols().

# from scipy.stats import linregress
# import statsmodels.formula.api as smf
#
# # Run regression with linregress
# subset = brfss.dropna(subset=['INCOME2', '_VEGESU1'])
# xs = subset['INCOME2']
# ys = subset['_VEGESU1']
# res = linregress(xs,ys)
# print(res)
#
# # Run regression with StatsModels
# results = smf.ols('_VEGESU1 ~ INCOME2', data = brfss).fit()
# print(results.params)
# *
# ------------------------------------------------
# To get a closer look at the relationship between income and education,
# let's use the variable 'educ' to group the data, then plot mean income in each group.
# # Group by educ
# grouped = gss.groupby('educ')
#
# # Compute mean income in each group
# mean_income_by_educ = grouped['realinc'].mean()
#
# # Plot mean income as a scatter plot
# plt.plot(mean_income_by_educ,'o',alpha=0.5)
#
# # Label the axes
# plt.xlabel('Education (years)')
# plt.ylabel('Income (1986 $)')
# plt.show()
# *
# ------------------------------------------------
# import statsmodels.formula.api as smf
#
# # Add a new column with educ squared
# gss['educ2'] = gss['educ']**2
#
# # Run a regression model with educ, educ2, age, and age2
# results = smf.ols('realinc ~ educ + educ2 + age + age2',data=gss).fit()
#
# # Print the estimated parameters
# print(results.params)
# *
# ------------------------------------------------
# # Run a regression model with educ, educ2, age, and age2
# results = smf.ols('realinc ~ educ + educ2 + age + age2', data=gss).fit()
#
# # Make the DataFrame
# df = pd.DataFrame()
# df['educ'] = np.linspace(0,20)
# df['age'] = 30
# df['educ2'] = df['educ']**2
# df['age2'] = df['age']**2
#
# # Generate and plot the predictions
# pred = results.predict(df)
# print(pred.head())
# *
# ------------------------------------------------
# # Plot mean income in each age group
# plt.clf()
# grouped = gss.groupby('educ')
# mean_income_by_educ = grouped['realinc'].mean()
# plt.plot(mean_income_by_educ,'o',alpha=0.5)
#
# # Plot the predictions
# pred = results.predict(df)
# plt.plot(df['educ'], pred, label='Age 30')
#
# # Label axes
# plt.xlabel('Education (years)')
# plt.ylabel('Income (1986 $)')
# plt.legend()
# plt.show()
# *
# ------------------------------------------------
# # Recode grass
# gss['grass'].replace(2, 0, inplace=True)
#
# # Run logistic regression
# results = smf.logit('grass ~ age + age2 + educ + educ2 + C(sex)', data=gss).fit()
# results.params
#
# # Make a DataFrame with a range of ages
# df = pd.DataFrame()
# df['age'] = np.linspace(18, 89)
# df['age2'] = df['age']**2
#
# # Set the education level to 12
# df['educ'] = 12
# df['educ2'] = df['educ']**2
#
# # Generate predictions for men and women
# df['sex'] = 1
# pred1 = results.predict(df)
#
# df['sex'] = 2
# pred2 = results.predict(df)
#
# plt.clf()
# grouped = gss.groupby('age')
# favor_by_age = grouped['grass'].mean()
# plt.plot(favor_by_age, 'o', alpha=0.5)
#
# plt.plot(df['age'], pred1, label='Male')
# plt.plot(df['age'], pred2, label='Female')
#
# plt.xlabel('Age')
# plt.ylabel('Probability of favoring legalization')
# plt.legend()
# plt.show()
# *
# ------------------------------------------------
# ------------------------------------------------