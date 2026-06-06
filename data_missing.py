# 1.List of employee ID's who COMPLETED the training
trained_employees = ["ID-10", "ID-45", "ID-99", "ID-88"]

# .The employee ID we are auditing today 
audit_target = "ID-27"

# 3 Use the plain-English "not in "tool to detect the anomaly!
if audit_target not in trained_employees:
    print("Flagged:", audit_target," has not completed the training!")
else:
    print("clear:", audit_target, "is fully compliant")
