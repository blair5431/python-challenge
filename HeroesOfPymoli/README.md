

```python
#improting pandas
import pandas as pd
```


```python
#path to json file
file = "purchase_data.json"

#read dataframe into pandas
game_df = pd.read_json(file)
#game_df.head()
```

 Player Count


```python
#player count
total_players= len(game_df["SN"].unique())
pd.DataFrame([total_players], columns=['Total Players'])

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>573</td>
    </tr>
  </tbody>
</table>
</div>



Purchasing Analysis (Total)


```python
#Purching Analysis (Total) 

#number of unique items
unique =game_df ["Item Name"].nunique()
#unique

#average purchase price
Avg_Price = round(game_df["Price"].mean(),2)
Avg_Price 

#total Revenue 
tot_rev=round(game_df["Price"].sum(),2)
tot_rev

#total number of purchases 
tot_purch = game_df["Price"].count()
tot_purch

#combinging everything into one table 
purching_analysis =pd.DataFrame ({"Unique Items":[unique],
                                  "Average Price":[Avg_Price], 
                                  "Total Revenue":[tot_rev], "Total Purchase":[tot_purch]})
purching_analysis
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Price</th>
      <th>Total Purchase</th>
      <th>Total Revenue</th>
      <th>Unique Items</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2.93</td>
      <td>780</td>
      <td>2286.33</td>
      <td>179</td>
    </tr>
  </tbody>
</table>
</div>




Gender Demogarphics 


```python
#Gender Demogarhpics 
gender_counts =game_df["Gender"].value_counts()
gender_demographics = pd.DataFrame({"Counts": gender_counts})
gender_demographics
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Counts</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>633</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>136</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>



Purchasing Analysis (Gender)


```python
#purchase analysis by Gender 
grouped_gender_df = game_df.groupby(["Gender"])
grouped_gender_df.count().head(10)

#average purchase price 
Avg_Price_MF = round(grouped_gender_df["Price"].mean(),2)
#print(Avg_Price_MF)

#purchase count
purch_count_mf = grouped_gender_df["Price"].count()
#print(purch_count_mf)

#total purchase value 
tot_purch_mf= grouped_gender_df["Price"].sum()
#print(tot_purch_mf)

#normalized Totals 
norm_tot_purch_mf = tot_purch_mf/tot_purch_mf.sum()
#print(norm_tot_purch_mf.round(2))


#putting all the data together in one table 
gender_analysis= pd.DataFrame ({"Average Price":Avg_Price_MF,
                                  "Purchase Count":purch_count_mf, 
                                  "Total Purcahse Value":tot_purch_mf,
                                "Normalized Total":norm_tot_purch_mf })
gender_analysis.style.format({'Total Purcahse Value': '${:.2f}', 'Average Price': '${:.2f}', 'Normalized Total': '${:.2f}'})


gender_analysis
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Price</th>
      <th>Normalized Total</th>
      <th>Purchase Count</th>
      <th>Total Purcahse Value</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>2.82</td>
      <td>0.167478</td>
      <td>136</td>
      <td>382.91</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>2.95</td>
      <td>0.816890</td>
      <td>633</td>
      <td>1867.68</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>3.25</td>
      <td>0.015632</td>
      <td>11</td>
      <td>35.74</td>
    </tr>
  </tbody>
</table>
</div>






Age Demographcis


```python
#AGE DEMOGRAPHICS each broken into bins of 4 years (i.e. <10, 10-14, 15-19, etc.)
#min age= 7 and max age =45
# Bins are 0 to 10, 10 to 14, 15 to 19, 75 to 100
bins = [0, 10, 15, 20, 25, 30, 35, 40, 45]
group_names =["<10", "10-15", "16-20", "21-25", "26-30", "31-35", "36-40", "41-45"]

pd.cut(game_df["Age"],bins, labels=group_names)

#adding age group varaible to dataset 
game_df["Age Group"]=pd.cut(game_df["Age"],bins, labels=group_names)

#creating a groups based off age bins
age_groups_df = game_df.groupby("Age Group")
age_groups_df.max() 

#total purchase value 
tot_purch_age= age_groups_df["Price"].sum()

#normalized Totals 
percent_age = ((tot_purch_age/tot_purch_age.sum())*100).round()

#age Counts
age_count=age_groups_df["Age"].count()

#putting everyting in table 
age_demogaraphics= pd.DataFrame ({"Percentage of Players":percent_age,
                                  "Total Count":age_count })

age_demogaraphics
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
    <tr>
      <th>Age Group</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>4.0</td>
      <td>32</td>
    </tr>
    <tr>
      <th>10-15</th>
      <td>10.0</td>
      <td>78</td>
    </tr>
    <tr>
      <th>16-20</th>
      <td>23.0</td>
      <td>184</td>
    </tr>
    <tr>
      <th>21-25</th>
      <td>39.0</td>
      <td>305</td>
    </tr>
    <tr>
      <th>26-30</th>
      <td>10.0</td>
      <td>76</td>
    </tr>
    <tr>
      <th>31-35</th>
      <td>8.0</td>
      <td>58</td>
    </tr>
    <tr>
      <th>36-40</th>
      <td>6.0</td>
      <td>44</td>
    </tr>
    <tr>
      <th>41-45</th>
      <td>0.0</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>



Purchasing Analysis (Age)


```python
#Purchasing Analysis (Age)

#average purchase price 
Avg_Price_age = round(age_groups_df["Price"].mean(),2)

#purchase count
purch_count_age = age_groups_df["Price"].count()




#normalized Totals 
norm_tot_purch_age = (tot_purch_age/age_count).round(2) 

#putting all the data together in one table 
age_purch_anlysis= pd.DataFrame ({"Average Price":Avg_Price_age.map("${:.2f}".format),
                                  "Purchase Count":purch_count_age, 
                                  "Total Purcahse Value":tot_purch_age.map("${:.2f}".format),
                                "Normalized Total":norm_tot_purch_age })

#age_purch_anlysis.style.format({'Total Purchase Value': '${:.2f}', 'Average Price': '${:.2f}', 'Normalized Total': '${:.2f}'})


age_purch_anlysis


```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Price</th>
      <th>Normalized Total</th>
      <th>Purchase Count</th>
      <th>Total Purcahse Value</th>
    </tr>
    <tr>
      <th>Age Group</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>$3.02</td>
      <td>3.02</td>
      <td>32</td>
      <td>$96.62</td>
    </tr>
    <tr>
      <th>10-15</th>
      <td>$2.87</td>
      <td>2.87</td>
      <td>78</td>
      <td>$224.15</td>
    </tr>
    <tr>
      <th>16-20</th>
      <td>$2.87</td>
      <td>2.87</td>
      <td>184</td>
      <td>$528.74</td>
    </tr>
    <tr>
      <th>21-25</th>
      <td>$2.96</td>
      <td>2.96</td>
      <td>305</td>
      <td>$902.61</td>
    </tr>
    <tr>
      <th>26-30</th>
      <td>$2.89</td>
      <td>2.89</td>
      <td>76</td>
      <td>$219.82</td>
    </tr>
    <tr>
      <th>31-35</th>
      <td>$3.07</td>
      <td>3.07</td>
      <td>58</td>
      <td>$178.26</td>
    </tr>
    <tr>
      <th>36-40</th>
      <td>$2.90</td>
      <td>2.90</td>
      <td>44</td>
      <td>$127.49</td>
    </tr>
    <tr>
      <th>41-45</th>
      <td>$2.88</td>
      <td>2.88</td>
      <td>3</td>
      <td>$8.64</td>
    </tr>
  </tbody>
</table>
</div>



Top Spenders

Top Spender


```python
#Top Spender

spender_items= game_df[["SN", "Price"]]
               
#group itmes by Item ID
grouped_sn = spender_items.groupby(["SN"])

#purchase count
sn_count_group = grouped_sn.count()
sn_count = pd.DataFrame(sn_count_group["Price"])

#Total Purchase Value
sn_tot_price = pd.DataFrame(grouped_sn.sum().round(2))

#Average Purchase Price
avg_sn_price = pd.DataFrame(grouped_sn.mean().round(2))

merge_sn =sn_count.merge(sn_tot_price, left_index=True, right_index=True).merge(avg_sn_price,left_index=True, right_index=True)
merge_sn= merge_sn.sort_values(by=["Price_x"], ascending=False).head(5)
top_spenders = merge_sn.rename(columns={"Price_x":"Purchase Count", "Price_y":"Total Price", "Price":"Average Price" })
top_spenders
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Total Price</th>
      <th>Average Price</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>5</td>
      <td>17.06</td>
      <td>3.41</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>4</td>
      <td>12.74</td>
      <td>3.18</td>
    </tr>
    <tr>
      <th>Qarwen67</th>
      <td>4</td>
      <td>9.97</td>
      <td>2.49</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>4</td>
      <td>13.56</td>
      <td>3.39</td>
    </tr>
    <tr>
      <th>Sondastan54</th>
      <td>4</td>
      <td>10.24</td>
      <td>2.56</td>
    </tr>
  </tbody>
</table>
</div>



Most Popular Items


```python
#Most Popular Items 
items= game_df[["Item ID", "Price", "Item Name"]]
               
#group itmes by Item ID
grouped_items = items.groupby(["Item ID", "Item Name"])


#top_items =grouped_items.count().sort_values(by=["Price"], ascending=False).head(5)
item_count_group = grouped_items.count()
item_count = pd.DataFrame(item_count_group["Price"])

item_tot_price = pd.DataFrame(grouped_items.sum())
item_item_price = pd.DataFrame(grouped_items.mean())


new_df =item_count.merge(item_item_price, left_index=True, right_index=True).merge(item_tot_price,left_index=True, right_index=True)
new_df2= new_df.sort_values(by=["Price_x"], ascending=False).head(5)
most_popular_itmes = new_df2.rename(columns={"Price_x":"Purchase Count", "Price_y":" Item Price", "Price":"Total Price" })
most_popular_itmes
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Price</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <th>Betrayal, Whisper of Grieving Widows</th>
      <td>11</td>
      <td>2.35</td>
      <td>25.85</td>
    </tr>
    <tr>
      <th>84</th>
      <th>Arcane Gem</th>
      <td>11</td>
      <td>2.23</td>
      <td>24.53</td>
    </tr>
    <tr>
      <th>31</th>
      <th>Trickster</th>
      <td>9</td>
      <td>2.07</td>
      <td>18.63</td>
    </tr>
    <tr>
      <th>175</th>
      <th>Woeful Adamantite Claymore</th>
      <td>9</td>
      <td>1.24</td>
      <td>11.16</td>
    </tr>
    <tr>
      <th>13</th>
      <th>Serenity</th>
      <td>9</td>
      <td>1.49</td>
      <td>13.41</td>
    </tr>
  </tbody>
</table>
</div>



Most Profitable Items


```python
#Most Profitable Items 
new_df3= new_df.sort_values(by=["Price"], ascending=False).head(5)
most_profitable_itmes = new_df3.rename(columns={"Price_x":"Purchase Count", "Price_y":" Item Price", "Price":"Total Price" })
most_profitable_itmes
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Price</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <th>Retribution Axe</th>
      <td>9</td>
      <td>4.14</td>
      <td>37.26</td>
    </tr>
    <tr>
      <th>115</th>
      <th>Spectral Diamond Doomblade</th>
      <td>7</td>
      <td>4.25</td>
      <td>29.75</td>
    </tr>
    <tr>
      <th>32</th>
      <th>Orenmir</th>
      <td>6</td>
      <td>4.95</td>
      <td>29.70</td>
    </tr>
    <tr>
      <th>103</th>
      <th>Singed Scalpel</th>
      <td>6</td>
      <td>4.87</td>
      <td>29.22</td>
    </tr>
    <tr>
      <th>107</th>
      <th>Splitter, Foe Of Subtlety</th>
      <td>8</td>
      <td>3.61</td>
      <td>28.88</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


      File "<ipython-input-12-1f5396e5a477>", line 1
        IPython nbconvert README.md --to markdown
                        ^
    SyntaxError: invalid syntax


