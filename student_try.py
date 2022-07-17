import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap


def main():
    student_df = pd.read_csv(filepath_or_buffer="C:\\Users\\user\\PycharmProjects\\datasets\\student_data.csv")
    # getting the dataframe (tuple) printed
    print(student_df)
    # printing the various column heads
    print(student_df.columns)
    # printing out the first 8 and last 6 details of the database
    print(student_df.head(8), student_df.tail(6))
    # finding out if there is any null values in the various columns
    print(student_df.isnull().any())
    # creating a copy of student perf dataset
    student_info = student_df.copy()
    # creating a new dataframe to contain full name of schools
    abbr = pd.DataFrame({"school": ["GP", "MS"], "school_name": ["Glen Preparatory", "Montessori"]})
    print(abbr)
    # merging the full names of school to the original dataframe
    merge = pd.merge(student_info, abbr, on="school")
    print(merge)
    # computing the average age of students in both schools combined
    average_age = student_info["age"].mean()
    print("average age of students in 2 schools combined is: ", average_age)
    # print total number of students at Montessori and Glen respectively
    # count() brings out total on column, values_count() uses unique labels to count
    print(student_info["school"].value_counts())
    # grouping students by school
    group_student = student_info.groupby("school")
    print(group_student["age"].mean())
    # finding males and females in both schools
    males_females_total = student_info["sex"].value_counts()
    print(males_females_total)
    # finding males and females by school
    group_sex = group_student["sex"].value_counts()
    print(group_sex)
    # Extracting students that failed and finding out the total
    failure = student_info.loc[(student_info["failures"] > 0), ["school", "failures", "absences"]]
    print(failure)
    print("Total number of failures recorded from both schools: ", len(failure))
    # finding failures by schools (Glen and Montessori respectively)
    failure_GP = student_info.loc[(student_info["failures"] > 0) & (student_info["school"] == "GP"),
                                  ["school", "failures", "absences"]]
    print("Glen total number of failures:", len(failure_GP))
    failure_MS = student_info.loc[(student_info["failures"] > 0) & (student_info["school"] == "MS"),
                                  ["school", "failures", "absences"]]
    print("Montessori total number of failures:", len(failure_MS))
    # finding out how many students passed and use the absences to compare those who failed
    passed = student_info.loc[(student_info["failures"] == 0), ["school", "failures", "absences", "G1"]]
    print(passed.head(30))
    # total number of students who passed
    print("Total passed from both schools:", len(passed))
    # average grade (G1, G2 nd G3) of students
    print("average grade of students by school: ")
    print(group_student["G1"].mean())
    print(group_student["G2"].mean())
    print(group_student["G3"].mean())
    # Maximum and minimum grade for both schools
    print("Finding out maximum score in grade 1")
    print(group_student["G1"].max())
    print("Finding out minimum score in grade 1")
    print(group_student["G1"].min())
    print("Finding out maximum score in grade 2")
    print(group_student["G2"].max())
    print("Finding out minimum score in grade 2")
    print(group_student["G2"].min())
    print("Finding out maximum score in grade 3")
    print(group_student["G3"].max())
    print("Finding out minimum score in grade 3")
    print(group_student["G3"].min())
    # Finding out those who paid their fees and those who didn't pay
    print("Total number of students who paid their fees")
    paid = student_info.loc[(student_info["paid"] == "yes"), ["school", "paid"]]
    not_paid = student_info.loc[(student_info["paid"] == "no"), ["school", "paid"]]
    print(paid)
    print("Total no:", len(paid))
    print("Total number of students who did not pay their fees")
    print(not_paid)
    print("Total no:", len(not_paid))
    print("Students that have paid fees In Glen Preparatory")
    GP_paid = student_info.loc[(student_info["paid"] == "yes") & (student_info["school"] == "GP"), ["school", "paid"]]
    print(GP_paid)
    print("Total no of Students that have paid fees In Glen Preparatory:", len(GP_paid))
    print("Index representing students that have not paid fees In Glen Preparatory")
    GP_notpaid = student_info.loc[(student_info["paid"] == "no") & (student_info["school"] == "GP"), ["school", "paid"]]
    print(GP_notpaid)
    print("Total no of Students that have not paid fees In Glen Preparatory:", len(GP_notpaid))
    print("Students that have paid fees In Glen Montessori")
    MS_paid = student_info.loc[(student_info["paid"] == "yes") & (student_info["school"] == "MS"), ["school", "paid"]]
    print(MS_paid)
    print("Total no of Students that have paid fees Montessori:", len(MS_paid))
    print("Index representing students that have not paid fees In Montessori")
    MS_notpaid = student_info.loc[(student_info["paid"] == "no") & (student_info["school"] == "MS"), ["school", "paid"]]
    print(MS_notpaid)
    print("Total no of Students that have not paid fees In Montessori:", len(MS_notpaid))
    # info() function describes the dataset. null values present or data types
    print(student_info.info())
    print(student_info.describe())
    print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
