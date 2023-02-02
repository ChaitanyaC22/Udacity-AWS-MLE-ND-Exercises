# Write the the following code within the cell as python script named 'xgboost_process_script.py'

# Execute this cell first to write this script to your local directory. 

import pandas

# This method filters out the column at index 1, which is the crime data. 

def filter_crime_data(input_data_path):
    with open(input_data_path, 'r') as f:
        df = pandas.read_csv(f)
    df.drop(df.columns[[1]], axis=1)
    return df

# The main method takes in data at '/opt/ml/processing/input/data/train.csv' 
# and outputs it as a csv to '/opt/ml/processing/output/data_processed'

if __name__ == "__main__":
    filtered_data = filter_crime_data('/opt/ml/processing/input/data/train.csv')
    filtered_data.to_csv('/opt/ml/processing/output/data_processed')

