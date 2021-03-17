from load_data import *
import pandas as pd

""" Useful infos : salaire (moyen+median), jobtitle, work for one or several companies, 
team size, experience years, gender, geolocation"""

def pruning(df, columns):
    """Function that only keeps the columns we want from a dataframe"""
    return df.loc[:,columns]

pd.set_option("max_rows", None)
pd.set_option("max_columns", None)


# We can get rid of columns: first row (index), Job Description, Rating, Company Name, Headquarters
# Size, Founded, Type of ownership, Industry, Sector, Revenue, Competitors, Easy Apply
# We keep: Job Title, Salary Estimate, Location

df_raw_k_short = pruning(df_raw_k, ['Job Title', 'Salary Estimate', 'Location'])

# We can get rid of columns: SurveyYear, Timestamp, PrimaryDatabase, YearsWithThisDatabase, OtherDatabases,
# EmploymentStatus, ManageStaff, CompanyEmployeesOverall, DatabaseServers, Education, EducationComputerRelated,
# Certifications, TelecommuteDaysPerWeek, NewestVersionInProduction, OldestVersionInProduction,
# canPopulationOfLargestCityWithin20Mile, EmploymentSector, CareerPlansThisYear, OtherJobDuties,
# KindsOfTasksPerformed, Counter
# We keep : Index, SalaryUSD, Country, PostalCode, JobTitle, YearsWithThisTypeOfJob, HowManyCompanies,
# OtherPeopleOnYourTeam, HoursWorkedPerWeek, LookingForAnotherJob, Gender

df_raw_b_short = pruning(df_raw_b, ['SalaryUSD', 'Country', 'PostalCode', 'JobTitle',
                                  'YearsWithThisTypeOfJob', 'HowManyCompanies', 'OtherPeopleOnYourTeam',
                                  'HoursWorkedPerWeek', 'LookingForAnotherJob', 'Gender'])

# We checked that United States is the only spelling that refers to USA
# We only keep the data from United States
df_raw_b_short = df_raw_b_short[df_raw_b_short.Country == 'United States']

def missing_values(df):
    """Give us the number of missing values per column in the dataframe"""
    print("Number of empty data\n", df.isnull().sum())

# Check if the first dataframe has missing values
missing_values(df_raw_k_short)

# Check if the second dataframe has missing values
missing_values(df_raw_b_short)


# Replace the missing value of PostalCode by Not Asked
df_raw_b_short.PostalCode = df_raw_b_short.PostalCode.fillna("Not Asked")
missing_values(df_raw_b_short)


# Convert PostalCode column in string to use it
df_raw_b_short.PostalCode = df_raw_b_short.PostalCode.astype(str)
# Modify wrong PostalCode with Not Asked
df_raw_b_short.loc[(df_raw_b_short.PostalCode.str.len()) != 5 | df_raw_b_short.PostalCode.str.isalpha(),
                   "PostalCode"] = "Not Asked"


# Rows with salary values below 20000 and over 800000 are deleted
df_raw_b_short.drop(df_raw_b_short[(df_raw_b_short.SalaryUSD < 20000.00) | (df_raw_b_short.SalaryUSD > 800000.00)].index, inplace=True)


# JobTitle
# Assign the value Other to JobTitle that appears less than 5 times
cond = df_raw_b_short.groupby('JobTitle').JobTitle.count() < 5
df_raw_b_short.loc[df_raw_b_short.JobTitle.isin(cond.loc[cond].index), "JobTitle"] = "Other"


# YearsWithThisTypeOfJob
# print(df_raw_b_short.YearsWithThisTypeOfJob.sort_values())

# HowManyCompanies
# print(df_raw_b_short.groupby('HowManyCompanies').HowManyCompanies.count().sort_values())

# OtherPeopleOnYourTeam
# print(df_raw_b_short.groupby('OtherPeopleOnYourTeam').OtherPeopleOnYourTeam.count().sort_values())

# HoursWorkedPerWeek
# print(df_raw_b_short.groupby('HoursWorkedPerWeek').HoursWorkedPerWeek.count())
df_raw_b_short.loc[df_raw_b_short.HoursWorkedPerWeek == 150,
                   "HoursWorkedPerWeek"] = "Not Asked"

# LookingForAnotherJob
# print(df_raw_b_short.groupby('LookingForAnotherJob').LookingForAnotherJob.count())

# Gender
# print(df_raw_b_short.groupby('Gender').Gender.count().sort_values())
cond = df_raw_b_short.groupby('Gender').Gender.count() < 40
df_raw_b_short.loc[df_raw_b_short.Gender.isin(cond.loc[cond].index), "Gender"] = "Not Asked"



# print(df_raw_b_short.SalaryUSD.sort_values())



# print(df_raw_b_short.count())

# print(df_raw_b_short.groupby('PostalCode').PostalCode.count())


