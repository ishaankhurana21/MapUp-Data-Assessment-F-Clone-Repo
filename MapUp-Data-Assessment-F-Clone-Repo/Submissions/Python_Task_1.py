#!/usr/bin/env python
# coding: utf-8

# # ANSWER 1

# In[4]:


import pandas as pd
df = pd.read_csv("C:/Users/ishaan khurana/Desktop/dataset-1.csv")


def generate_car_matrix(df)->pd.DataFrame:
    """
    Creates a DataFrame  for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values, 
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    # Write your logic here
    car_matrix = df.pivot(index='id_1', columns='id_2', values='car').fillna(0)
    return car_matrix
result_df = generate_car_matrix(df)
print(result_df)


# # ANSWER 2

# In[5]:


import numpy as np
def get_type_count(df)->dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    # Write your logic here
    conditions = [
        (df['car'] <= 15),
        (df['car'] > 15) & (df['car'] <= 25),
        (df['car'] > 25)
    ]
    choices = ['low', 'medium', 'high']
    df['car_type'] = pd.Series(np.select(conditions, choices), dtype='category')
    type_counts = df['car_type'].value_counts().to_dict()
    sorted_type_counts = dict(sorted(type_counts.items()))
    return sorted_type_counts

result = get_type_count(df)
print(result)


# # ANSWER 3

# In[6]:


def get_bus_indexes(df)->list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    # Write your logic here
    bus_mean = df['bus'].mean()
    bus_indexes = df[df['bus'] > 2 * bus_mean].index.tolist()
    bus_indexes.sort()

    return bus_indexes
result = get_bus_indexes(df)
print(result)


# # ANSWER 4

# In[7]:


def filter_routes(df)->list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    # Write your logic here
    average_truck_by_route = df.groupby('route')['truck'].mean()
    selected_routes = average_truck_by_route[average_truck_by_route > 7].index.tolist()
    selected_routes.sort()
    return selected_routes
result = filter_routes(df)
print(result)


# # ANSWER 5

# In[8]:


def multiply_matrix(matrix)->pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    # Write your logic here
    modified_matrix = matrix.copy()
    modified_matrix[modified_matrix > 20] *= 0.75
    modified_matrix[modified_matrix <= 20] *= 1.25
    modified_matrix = modified_matrix.round(1)
    return modified_matrix
 
modified_result_df = multiply_matrix(result_df)
print(modified_result_df)


# # ANSWER 6

# In[10]:


import pandas as pd
df = pd.read_csv("C:/Users/ishaan khurana/Desktop/dataset-2.csv")
def time_check(df)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here
    df['start_datetime'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'], errors='coerce')
    df['end_datetime'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'], errors='coerce')
    full_day_coverage = (df['end_datetime'] - df['start_datetime']).dt.total_seconds() == 24 * 60 * 60
    days_of_week_coverage = df.groupby(['id', 'id_2'])['start_datetime'].transform(lambda x: x.dt.dayofweek.nunique() == 7)
    is_complete = full_day_coverage & days_of_week_coverage

    return is_complete




result_series = time_check(df)
print(result_series)


# In[ ]:





# In[ ]:




