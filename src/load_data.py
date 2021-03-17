import pandas as pd


# import mysql.connector
# from sqlalchemy import create_engine
# import pymysql
# from sqlalchemy.types import Integer, String, Float, Date, DateTime


def info_df(df):
    """Function that returns size and datatype and length of a dataframe"""
    index = df.index
    rows = len(index)
    print("Nombre de lignes :", rows)  # Display the number of rows
    print(df.head())  # Display the 5 first rows
    print(df.dtypes)  # Display column types
    # Display the column names and their maximum length
    print("Dataset : ",
          dict([(v, df[v].apply(lambda r: len(str(r)) if r != None else 0).max()) for v in df.columns.values]))


def import_data():
    """Function that return the dataframe from our excel and csv files"""
    # Import the csv file
    df_raw_k = pd.read_csv("../data/01_raw/DataAnalyst.csv")
    # Import the excel file and skip the 3 first empty rows
    df_raw_b = pd.read_excel("../data/01_raw/2020_Data_Professional_Salary_Survey_Responses.xlsx",
                             skiprows=3)
    return df_raw_k, df_raw_b


df_raw_k, df_raw_b = import_data()



