#Alex Bernal Quantlab Interview Question
#July 24, 2020
# Import Libraries
import pandas as pd
import numpy as np

# Read Data
df = pd.read_csv("C://Users//User//Documents//input.csv")
df.columns=['microsecs','symbol','volume','price']
df['DollarVolume'] = (df['price'] * df['volume'])/df['volume'].sum()

# Get Unique Symbols and Sort
symbols = sorted(set(df['symbol']))

# Create Output File and Header Row
fh = open("C://Users//User//Documents//output.csv","w")
fh.write("<symbol>,<MaxTimeGap>,<Volume>,<WeightedAveragePrice>,<MaxPrice>\n")

# Main
for sym in symbols:

        tempdf = df[df['symbol'] == sym]
        tempdf.sort_values(['microsecs'])
        
        
        if len(tempdf) > 1:
                max_time = np.nanmax(tempdf['microsecs'] - tempdf['microsecs'].shift(1))
                total_volume = tempdf['volume'].sum()
                max_price    = tempdf['price'].max()
                total_dollar = tempdf['DollarVolume'].sum()
        else:
                print("1 Trade Per Symbol: %6s" % sym)
                break

        fh.write("%s,%d,%d,%.2f,%.2f\n" % (sym, max_time, total_volume, float(total_dollar/total_volume), max_price))
        dfSolution = dfSolution.append({'Symbol': sym, 'MaxTimeGap': max_time, 'Volume': total_volume, 'WeightedAveragePrice': total_dollar, 'MaxPrice': max_price}, ignore_index=True)
fh.close()
print(dfSolution)
