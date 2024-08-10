class Employee:
    def __init__(self, firstname: str, lastname: str) -> None:
        self.fullname = f"{firstname} {lastname}"
        self.email = f"{firstname}.{lastname}@company.com".lower()


employee1 = Employee("Tom", "Edwards")

print(employee1.fullname)
print(employee1.email)

