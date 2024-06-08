import pandas as pd
from pyexcel_ods import get_data

# ODS files not provided. However this is how the ratings and the student pairs are extracted:
 
# Function to read ODS files
def read_ods(path, sheet_index):
    data = get_data(path)
    sheet = list(data.values())[sheet_index]
    df = pd.DataFrame(sheet[1:], columns=sheet[0])
    return df

"""Example usage with the original files:

# Read the data from ODS files
path_students = "flow_student.ods"
path_students_ratings = "flow_student_rating.ods"

students_answers_raw = read_ods(path_students, 0)
students_ratings_raw = read_ods(path_students_ratings, 0)

# Extract relevant columns
students_answers = students_answers_raw[["fs_id", "sid", "fs_answer"]]
students_ratings = students_ratings_raw[["fsr_sid", "fsr_group_id", "fsr_rating", "fsr_rated_id"]]

# Group students by group_id
grouped_ratings = students_ratings.groupby("fsr_group_id")

# Process the data to organize students in groups and extract pairwise ratings
groups = {}
for group_id, group_data in grouped_ratings:
    group_members = group_data["fsr_sid"].unique()
    pairwise_ratings = group_data.pivot(index="fsr_sid", columns="fsr_rated_id", values="fsr_rating")
    groups[group_id] = {
        "members": group_members,
        "pairwise_ratings": pairwise_ratings
    }

# Merge answers with the grouped data
for group_id in groups:
    members = groups[group_id]["members"]
    answers = students_answers[students_answers["fs_id"].isin(members)]
    groups[group_id]["answers"] = answers

# The resulting groups dictionary contains the organized data
# Example access:
# group_id = 1
# print(groups[group_id]["members"])
# print(groups[group_id]["pairwise_ratings"])
# print(groups[group_id]["answers"])"""
