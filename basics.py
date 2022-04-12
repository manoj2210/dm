import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = [17, 23, 35, 36, 51, 53, 54, 55, 60, 77, 110]
quartiles = np.percentile(data, [25,50,75])
print(f"Median = {np.median(data)}\nQuartiles = {quartiles}")

inter_quantile_region = quartiles[2] - quartiles[0]
low = quartiles[0] - 1.5*inter_quantile_region
high = quartiles[2] + 1.5*inter_quantile_region
outliers = []
for i in data:
    if i > high or i < low:
        outliers.append(i)
print(f"Outliers in dataset: {outliers}")

sns.boxplot(data)
plt.show()


####

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = [6, 25, 39, 62, 65, 74, 80, 94, 125, 127, 154, 159, 184, 210, 251]
quartiles = np.percentile(data, [25,50,75])
print(f"Median = {np.median(data)}\nQuartiles = {quartiles}")

inter_quantile_region = quartiles[2] - quartiles[0]
low = quartiles[0] - 1.5*inter_quantile_region
high = quartiles[2] + 1.5*inter_quantile_region
outliers = []
for i in data:
    if i > high or i < low:
        outliers.append(i)
print(f"Outliers in dataset: {outliers}")

sns.boxplot(data)
plt.show()

####

import seaborn as sns
import matplotlib.pyplot as plt

# Pblm: Find the time by which 75% of the children in school A had completed the puzzle.
# Soln: 75% is quartile 3. Its value from the graph is 17. So, 75% of the children complete the puzzle in around 17 minutes.

# Pblm: State what the two crosses (x) represent on the box plot above. Interpret these in context
# Soln: The two crosses are outliers. Two students are taking a longer time to complete the puzzle

# Pblm: Determine if there are any outliers.
# Soln: There are no outliers

sns.boxplot([6,12,15,17,22])
plt.show()