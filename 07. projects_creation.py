name_of_the_architect = input()
number_of_projects = int(input())

time_for_project = 3

time_for_all_projects = number_of_projects * time_for_project

print(f"The architect {name_of_the_architect} will need {time_for_all_projects} "
      f"hours to complete {number_of_projects} project/s.")