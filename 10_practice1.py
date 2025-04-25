class Programmer:
    comp_name="Microsoft"
    location="America"
    pincode=528732

    def __init__(self,name,phoneno,department):
        self.name=name
        self.phoneno=phoneno
        self.department=department

        print("A class is created")

rohan=Programmer("Rohan",861265897,"Devops")
print(f"{rohan.name} is working in {rohan.department} department in {rohan.comp_name} company which is located in {rohan.location}.")