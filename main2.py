work_experience = int(input("Enter your full work experience in years: "))

if work_experience<=5 and work_experience>=1:
    developer_type = "Middle"
elif work_experience<=1:
    developer_type = "Junior"
else:
    developer_type = "Senior"
print(f"developer_type = {developer_type}")

len() 