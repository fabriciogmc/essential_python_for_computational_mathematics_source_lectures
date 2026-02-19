# Simple iteration using for

best_subjects = ["data structures", 
                 "math for computer science"]

for idx, subject in enumerate(best_subjects):
    print(idx, subject)

for i in range(len(best_subjects)):
    print(best_subjects[i])
