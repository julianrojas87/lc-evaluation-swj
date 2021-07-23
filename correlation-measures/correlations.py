import numpy as np

# Formated names for networks
networks = [
    "Netherlands-Waterbus", "Kobe-Subway", "Sydney-Trainlink",
    "San Francisco-BART", "Thailand-Greenbus", "Spain-RENFE",
    "Germany-DB", "Auckland-Waiheke", "Belgium-NMBS",
    "London-Tube", "Nairobi-SACCO", "EU-Flixbus",
    "France-SNCF", "Amsterdam-GVB", "Brussels-STIB",
    "New York-MTABC", "Madrid-CRTM", "Helsinki-HSL",
    "New Zealand-Bus", "Wallonia-TEC", "Chicago-CTA", "Flanders-De Lijn"
]

# Metric values
performance = np.array([
    27, 37, 45.81, 49.84, 36.27, 154.23, 182.15, 283.67, 760.62, 942.02,
    990.84, 2220.44, 2295.44, 1885.51, 4816.93, 5319.87, 7761, 12004.97,
    16394.7, 36311.72, 27887.7, 34130.91 
])

stops = np.array([44, 27, 361, 50, 112, 714, 433, 125, 606, 379, 2787, 
    1744, 4646, 1356, 2316, 3590, 5192, 8155, 2259, 31131, 11042, 29905])

connections = np.array([936, 6086, 891, 7755, 1024, 6159, 7680, 6020, 57950, 321952, 5857, 
    51636, 79796, 180695, 350038, 343582, 706642, 689834, 153690, 623808, 1128828, 826572])

K = np.array([1.179, 6.595, 0.192, 9.282, 3.206, 3.481, 4.476, 0.153, 35.367, 1056.554,
     6.711, 162.011, 20.196, 0.687, 2.474, 1.197, 3.937, 130.761, 0.509, 36.023, 2.209, 117.118])

D = np.array([9.1, 84, 0.1, 63.1, 9.6, 1.6, 3.4, 0.4, 19.4,
     931.7, 0.8, 30.9, 1.4, 0.2, 0.3, 0.1, 0.2, 5.3, 0.07, 0.3, 0.06, 1.3])

C = np.array([0, 0, 0.015, 0.198, 0.974, 2.692, 6.584, 0, 0.545, 6.778, 1.262, 27.142,
     2.575, 0.001, 0.138, 0.596, 2.614, 3.781, 0.032, 3.991, 0.331, 1.625])

ACD = np.array([11.08, 2.57, 51.24, 4.53, 83.81, 32.97, 33.05, 1.6, 5.66, 2.51, 4.69,
       133.05, 16.52, 2.11, 1.76, 4.19, 5.49, 1.62, 2.01, 1.55, 1.37, 1.56])

# Calculate Pearson coefficient
pearson_stops = np.corrcoef(stops, performance)[0][1]
print("pearson_stops = " + str(pearson_stops))
pearson_connections = np.corrcoef(connections, performance)[0][1]
print("pearson_connections = " + str(pearson_connections))
pearson_K = np.corrcoef(K, performance)[0][1]
print("pearson_K = " + str(pearson_K))
pearson_D = np.corrcoef(D, performance)[0][1]
print("pearson_D = " + str(pearson_D))
pearson_C = np.corrcoef(C, performance)[0][1]
print("pearson_C = " + str(pearson_C))
pearson_ACD = np.corrcoef(ACD, performance)[0][1]
print("pearson_ACD = " + str(pearson_ACD))
print("------------------------------------------")

# Calculate Covariances
cov_stops = np.cov(stops, performance)[0][1]
print("cov_stops = " + str(cov_stops))
cov_connections = np.cov(connections, performance)[0][1]
print("cov_connections = " + str(cov_connections))
cov_K = np.cov(K, performance)[0][1]
print("cov_K = " + str(cov_K))
cov_D = np.cov(D, performance)[0][1]
print("cov_D = " + str(cov_D))
cov_C = np.cov(C, performance)[0][1]
print("cov_C = " + str(cov_C))
cov_ACD = np.cov(ACD, performance)[0][1]
print("cov_ACD = " + str(cov_ACD))
print("------------------------------------------")

# Calculate Coefficient of Determination R^2
R2_stops = np.corrcoef(stops, performance)[0][1] ** 2 * 100
print("R^2_stops = " + str(R2_stops))
R2_connections = np.corrcoef(connections, performance)[0][1] ** 2 * 100
print("R^2_connections = " + str(R2_connections))
R2_K = np.corrcoef(K, performance)[0][1] ** 2 * 100
print("R^2_K = " + str(R2_K))
R2_D = np.corrcoef(D, performance)[0][1] ** 2 * 100
print("R^2_D = " + str(R2_D))
R2_C = np.corrcoef(C, performance)[0][1] ** 2 * 100
print("R^2_C = " + str(R2_C))
R2_ACD = np.corrcoef(ACD, performance)[0][1] ** 2 * 100
print("R^2_ACD = " + str(R2_ACD))