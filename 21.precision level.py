import numpy as np
import pandas as pd
from scipy import stats

def calculate_confidence_interval(sample, confidence_level):
    n = len(sample)
    mean = np.mean(sample)
    std_error = stats.sem(sample)
    margin_of_error = std_error * stats.t.ppf((1 + confidence_level) / 2, n - 1)
    lower_bound = mean - margin_of_error
    upper_bound = mean + margin_of_error
    return (lower_bound, upper_bound)

def main():
    # Read the rare element concentration data from the CSV file
    data = pd.read_csv('rare_elements.csv')
    measurements = data['Concentration']

    # Get user inputs
    sample_size = int(input("Enter the sample size: "))
    confidence_level = float(input("Enter the confidence level (between 0 and 1): "))
    desired_precision = float(input("Enter the desired level of precision: "))

    # Check if the sample size is valid
    if sample_size >= len(measurements):
        print("Sample size should be smaller than the total number of measurements.")
        return

    # Randomly select the sample
    sample = np.random.choice(measurements, size=sample_size, replace=False)

    # Calculate point estimation (sample mean)
    point_estimate = np.mean(sample)

    # Calculate the confidence interval
    confidence_interval = calculate_confidence_interval(sample, confidence_level)

    # Calculate the margin of error
    margin_of_error = (confidence_interval[1] - confidence_interval[0]) / 2

    # Calculate the required sample size for desired level of precision
    required_sample_size = int(np.ceil((stats.t.ppf((1 + confidence_level) / 2, sample_size - 1) * np.std(measurements)) / desired_precision))

    # Display the results
    print("Sample Size:", sample_size)
    print("Confidence Level:", confidence_level)
    print("Desired Level of Precision:", desired_precision)
    print("Point Estimation (Sample Mean):", point_estimate)
    print("Confidence Interval:", confidence_interval)
    print("Margin of Error:", margin_of_error)
    print("Required Sample Size for Desired Precision:", required_sample_size)

if __name__ == "__main__":
    main()
