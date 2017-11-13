f = open('crime_rates.csv','r')
data = f.read()
rows = data.split('\n')
crime_rates = []
for row in rows:
    crime_rates.append(int(row.split(',')[1]))
highest = crime_rates[0]
count = 0
for crime_rate in crime_rates:
    count += 1
    if crime_rate > highest:
         highest = crime_rate
print(highest)


    
