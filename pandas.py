import pandas as pd 
populations = [26.8, 21.1, 7.9, 2.6]
cities = ["Shanghai", "Beijing", \
          "Hangzhou", "Zibo"]
pop_ser = pd.Series(populations, index=cities)
print(pop_ser)
print()
pop_ser.name = "Population"
print(pop_ser)
print()
print(pop_ser["Beijing"])
print()
print(pop_ser[["Beijing", "Zibo"]])
print()
print(pop_ser["Beijing": "Zibo"])
print()
print(pop_ser.iloc[1])
print("*", pop_ser.iloc[[1, 3]])
print("average population:", pop_ser.mean())
print("standard deviation population:", \
      pop_ser.std())
print()
pop_ser["Liuzhou"] = 2.1
print(pop_ser)
print(len(pop_ser))
print(pop_ser.shape)
print()
pop_ser2 = pd.Series(dtype=float)
print(pop_ser2)
pop_ser2["Liuzhou"] = 2.1
print(pop_ser2)
print()
pop_data = [
    ["Shanghai", 26.8, "Large"],
    ["Beijing", 21.1, "Large"],
    ["Hangzhou", 7.9, "Medium"],
    ["Zibo", 2.6, "Small"]
]
header = ["City", "Population", "Class"]
pop_df = pd.DataFrame(pop_data, columns=header)
print(pop_df)

pop_ser3 = pop_df["Population"]
print(type(pop_ser3))
print(pop_ser3)

pop_ser4 = pop_df.iloc[:, 1] 

print(pop_ser4)

print(pop_df.iloc[0, 1])
pop_df = pop_df.set_index("City")

print(pop_df)

print(pop_df.loc["Shanghai"]["Population"])
print(pop_df["Population"]["Shanghai"])

regions_df = pd.read_csv("regions.csv",
                         index_col=0)
print(regions_df)
print()
merged_df = pop_df.merge(regions_df,
                         on=["City"],
                         how="outer")
print(merged_df)
print()


grouped_by_class = merged_df.groupby("Class")
mean_pop_ser = grouped_by_class["Population"].mean()

mean_pop_ser.name = "Mean Population"
print(mean_pop_ser)
print()

large_df = grouped_by_class.get_group("Large")
print(large_df)
print()
large_df2 = \
    merged_df[merged_df["Class"] == "Large"]
print(large_df2)
print()

print(merged_df["Class"].value_counts())
print()
merged_df = \
    merged_df.sort_values("Population",
                          ascending=False)
print(merged_df)
print()
print(merged_df.isnull())
print()
print(merged_df.isnull().sum())
print()
print(merged_df.isnull().sum().sum())
