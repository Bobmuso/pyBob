from hmac import digest_size

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = [0, 1, 3, 2, 4, 1, 2, 1, 4, 3, 2, 5, 2, 3, 4, 3, 5, 2, 5, 4, 4, 3, 5, 5, 4, 5, 5, 3, 5, 4, 5, 4, 4, 5, 5]

plt.hist(data, bins = 6)
plt.xlabel('Number of hurricanes per year')
plt.ylabel('Frequency')
plt.show()