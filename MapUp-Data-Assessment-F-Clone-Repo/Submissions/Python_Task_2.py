#!/usr/bin/env python
# coding: utf-8

# # ANSWER 1

# In[4]:


import pandas as pd
df=pd.read_csv("C:/Users/ishaan khurana/Desktop/dataset-3.csv")
def calculate_distance_matrix(df)->pd.DataFrame():
    """
    Calculate a distance matrix based on the dataframe, df.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Distance matrix
    """
    # Write your logic here
    unique_ids = sorted(set(df['id_start'].unique()).union(df['id_end'].unique()))
    distance_matrix = pd.DataFrame(index=unique_ids, columns=unique_ids)
    distance_matrix = distance_matrix.fillna(0)

    for index, row in df.iterrows():
        start, end, distance = row['id_start'], row['id_end'], row['distance']
        distance_matrix.at[start, end] = distance
        distance_matrix.at[end, start] = distance

    for i in distance_matrix.index:
        for j in distance_matrix.index:
            if i == j:
                continue
            if distance_matrix.at[i, j] == 0:
                for k in distance_matrix.index:
                    if i != k and j != k and distance_matrix.at[i, k] != 0 and distance_matrix.at[k, j] != 0:
                        distance_matrix.at[i, j] = distance_matrix.at[i, k] + distance_matrix.at[k, j]

    return distance_matrix

result_matrix = calculate_distance_matrix(df)
print(result_matrix)


# # ANSWER 2

# In[6]:


df=result_matrix.copy()
def unroll_distance_matrix(df)->pd.DataFrame():
    """
    Unroll a distance matrix to a DataFrame in the style of the initial dataset.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Unrolled DataFrame containing columns 'id_start', 'id_end', and 'distance'.
    """
    # Write your logic here
    unrolled_df = pd.DataFrame(columns=['id_start', 'id_end', 'distance'])
    for i in df.index:
        for j in df.index:
            if i != j and df.at[i, j] != 0:
                unrolled_df = unrolled_df.append({'id_start': i, 'id_end': j, 'distance': df.at[i, j]}, ignore_index=True)

    return unrolled_df
result_unrolled_df = unroll_distance_matrix(result_matrix)
print(result_unrolled_df)


# # ANSWER 3

# In[14]:


def find_ids_within_ten_percentage_threshold(df, reference_id)->pd.DataFrame():
    """
    Find all IDs whose average distance lies within 10% of the average distance of the reference ID.

    Args:
        df (pandas.DataFrame)
        reference_id (int)

    Returns:
        pandas.DataFrame: DataFrame with IDs whose average distance is within the specified percentage threshold
                          of the reference ID's average distance.
    """
    # Write your logic here
    reference_avg_distance = df[df['id_start'] == reference_id]['id_start'].mean()
    lower_threshold = reference_avg_distance - (reference_avg_distance * 0.10)
    upper_threshold = reference_avg_distance + (reference_avg_distance * 0.10)
    within_threshold_values = df[(df['id_start'] >= lower_threshold) & (df['id_start'] <= upper_threshold)]['id_start']
    sorted_within_threshold_values = sorted(within_threshold_values.unique())
    return sorted_within_threshold_values
reference_id = result_unrolled_df['id_start']
result_list = find_ids_within_ten_percentage_threshold(result_unrolled_df, reference_id)
print(result_list)


# # ANSWER 4

# In[5]:


def calculate_toll_rate(df)->pd.DataFrame():
    """
    Calculate toll rates for each vehicle type based on the unrolled DataFrame.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # Wrie your logic here
    rate_coefficients = {'moto': 0.8, 'car': 1.2, 'rv': 1.5, 'bus': 2.2, 'truck': 3.6}
    for vehicle_type, rate_coefficient in rate_coefficients.items():
        df[vehicle_type] = df['distance'] * rate_coefficient

    return df
result_with_toll_rates = calculate_toll_rate(result_unrolled_df)
print(result_with_toll_rates)


# # ANSWER 5

# In[ ]:


def calculate_time_based_toll_rates(df)->pd.DataFrame():
    """
    Calculate time-based toll rates for different time intervals within a day.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # Write your logic here

    return df

