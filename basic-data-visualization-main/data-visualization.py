
# To create dataframe to show unemployment rate

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Bar graph
data = {'Year': [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010],
        'Unemployment_Rate': [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
        }
df = pd.DataFrame(data, columns = ['Year', 'Unemployment_Rate'])

plt.plot(df['Year'], df['Unemployment_Rate'],marker='o', color = 'orange')
plt.title('Unemployment Rate Vs Year', fontsize = 14)
plt.xlabel('Year', fontsize = 14)
plt.ylabel('Unemployment Rate', fontsize = 14)
plt.grid(True)
plt.show()

# Histogram
x = np.random.randint(5,50,30)

plt.hist(x,bins=10, color='red')
plt.title ("Simple histogram")
plt.show()

plt.hist (x, bins =10, histtype='step', color='orange')
plt.title('Step-Type Histogram')
plt.show()

plt.hist (x, bins =10, cumulative=True)
plt.title("Cumulative Histogram")
plt.show()

#Scatter Plot
x = np.random.normal(5.0, 1.0, 1000)
y = np.random.normal(10.0, 2.0, 1000)

plt.scatter(x, y)
plt.show()