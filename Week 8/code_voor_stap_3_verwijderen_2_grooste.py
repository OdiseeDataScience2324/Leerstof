# stap 3
df["winst"] = (df.revenue - df.budget) / df.budget 
# drop two largest since they are not counted in dollars but in million dollars, next 5 largest are correct
largest_two = df.nlargest(2, "winst").index
df.drop(largest_two, inplace=True)
df_origin_with_budget.drop(largest_two, inplace=True)