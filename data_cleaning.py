

# This module loads all CSV files from the dated data directory,
# merges them into a single DataFrame, applies cleaning and transformation steps,
# handles missing values, and prepares the dataset for database storage.



from datetime import datetime
import os 
import pandas as pd



def load_data():
    today = datetime.today().strftime('%Y-%m-%d')
    folder_path = os.path.join('data', today)


    csv_files = [f for f in os.listdir(folder_path) if f.endswith('csv')]
    df = [pd.read_csv(os.path.join(folder_path, f)) for f in csv_files]
    return df

def merge_dataset(df):
    merge_df = pd.concat(df, ignore_index=True)
    return merge_df


def clean_data(merge_df):
    merge_df.columns = merge_df.columns.str.strip().str.lower()

    merge_df['year'] = pd.to_numeric(merge_df['year'], errors= 'coerce')
    merge_df['month_num'] = pd.to_numeric(merge_df['month_num'], errors= 'coerce')

    merge_df['date'] = pd.to_datetime(dict(year = merge_df['year'], month = merge_df['month_num'], day = 1), errors= 'coerce')
    merge_df['month_name'] = merge_df['month_num'].dt.month_name()


    rename_col = {
        'city1' : 'departure_city',
        'city2' : 'arrival_city',
        'distance_gc_(km)' : 'distance',
        'rpks' : 'revenue_per_passanger',
        'asks' : 'available_seats'
    }
    merge_df.rename(columns = rename_col, inplace = True)

    return merge_df

def missing_values(merge_df):

    num_col = merge_df.select_dtypes(include = ['int64', 'float64']).columns
    for col in num_col:
        if merge_df[col].isnull().sum() > 0:
            mean_value = merge_df[col].mean()
            merge_df[col] = merge_df[col].fillna(mean_value)

    cat_col = merge_df.select_dtypes(include = ['object']).columns
    for col in cat_col:
        if merge_df[col].isnull().sum()>0:
            comm_value = merge_df[col].mode().iloc[0]
            merge_df[col] = merge_df[col].fillna(comm_value)

    merge_df = merge_df.drop_duplicates()

    return merge_df


if __name__ == 'main':
    from save import save_to_sql

    raw_df = load_data()
    merge_data = merge_dataset()

    cleaned_data = clean_data(merge_data)
    final_df = missing_values(clean_data)

    save_to_sql(
        df = final_df,
        table_name= '',
        server ='',
        database = '',
        username = '',
        password = ''
    )