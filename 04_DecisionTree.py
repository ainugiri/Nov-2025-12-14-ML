import pandas as pd
from sklearn import tree

from sklearn.tree import DecisionTreeRegressor, plot_tree   
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.tree import export_graphviz
import matplotlib.pyplot as plt
df = pd.read_csv("./house_dataset_100rows.csv")
print(df.head())
'''
The dataset has the following columns:
# size_sqft	bedrooms	age_years	bathrooms	parking	price_lakhs
# 1360	2	42	1	0	67
# 1794	1	44	2	1	108
# 1630	4	24	2	0	136
# 1595	3	15	3	1	148
# 2138	3	32	2	0	35
# 2669	2	32	1	1	88
# 966	4	24	3	1	41
# 1738	1	41	1	0	112
# 830	3	49	1	0	95
# 1982	4	49	2	1	173
# 2635	4	12	2	0	163
# 630	2	39	2	1	198
# 2185	3	2	2	0	105
# 1269	3	3	2	1	48
# 2891	1	49	3	1	88
# 2015	3	37	1	1	66
# 2933	1	49	1	1	113
# 1715	3	17	1	1	163
# 1455	2	49	1	1	195
# 2824	3	2	2	0	104
# 1684	1	2	1	0	58
# 959	1	28	3	0	119
# 521	2	23	3	1	52
# 2800	3	37	1	1	120
# 1247	3	32	1	1	42
# 974	2	33	3	1	29
# 1582	3	1	3	0	88
# 2547	3	19	2	0	119
# 1475	1	2	3	1	53
# 2306	3	44	2	0	199
# 689	3	26	2	0	157
# 1062	2	32	2	1	166
# 2399	2	6	2	0	115
# 1767	4	32	2	1	20
# 2028	1	4	1	0	88
# 1146	3	11	3	1	23
# 2568	3	17	2	1	35
# 2714	4	38	3	1	43
# 1797	3	24	3	1	99
# 2935	1	5	2	0	21
# 1100	4	34	1	1	147
# 2863	1	6	2	1	179
# 2561	4	22	1	1	103
# 741	4	11	3	0	171
# 2541	2	48	1	1	159
# 1863	1	16	1	0	197
# 2639	3	33	1	1	182
# 1890	3	9	3	0	143
# 1978	1	6	3	0	52
# 1275	3	16	1	1	180
# 534	3	29	1	0	198
# 2753	1	3	2	1	190
# 2455	4	20	1	1	120
# 2085	1	36	2	1	31
# 1521	4	19	1	0	86
# 1629	3	26	2	0	84
# 2000	3	3	3	1	180
# 1202	3	19	1	1	187
# 2949	2	20	1	0	93
# 2079	4	32	1	1	62
# 661	2	7	1	1	63
# 701	2	41	2	1	48
# 2481	1	33	1	0	160
# 1495	2	40	3	0	31
# 2817	1	39	3	0	114
# 1315	1	18	1	1	65
# 955	2	40	3	1	149
# 1775	4	1	1	1	54
# 1516	4	11	1	0	100
# 2843	4	28	3	1	109
# 837	4	25	1	1	27
# 1378	4	23	3	1	112
# 1576	2	31	2	1	173
# 1291	2	30	1	0	109
# 2764	3	42	2	0	181
# 1263	4	35	3	1	134
# 2735	2	7	2	0	124
# 879	3	16	2	0	154
# 992	4	26	3	1	77
# 1680	1	48	2	1	133
# 2562	3	49	2	0	94
# 564	2	2	3	1	176
# 1867	1	1	2	0	139
# 1652	1	48	3	1	183
# 2527	1	12	2	0	40
# 1995	3	5	3	1	183
# 1662	2	37	3	0	157
# 2022	1	32	2	0	120
# 891	4	9	2	0	171
# 2198	1	41	2	1	196
# 918	1	35	1	0	118
# 2836	3	19	1	0	55
# 878	3	48	1	1	115
# 2296	2	16	3	1	171
# 2778	4	3	2	0	170
# 2588	3	20	3	0	56
# 2682	1	24	1	1	31
# 700	2	33	2	1	132
# 2363	1	24	3	1	32
# 1279	1	11	2	1	42
'''

x = df.drop("price_lakhs", axis=1) # Features
y = df["price_lakhs"] # Target



model = DecisionTreeRegressor(max_depth=5)
model.fit(x, y) 
y_pred = model.predict(x)
print("Predicted values:", y_pred)
print("R2 Score:", r2_score(y, y_pred))
print("Mean Squared Error:", mean_squared_error(y, y_pred))


plt.figure(figsize=(12,8))
plot_tree(model, feature_names=x.columns, filled=True, rounded=True)
plt.show()