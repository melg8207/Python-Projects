payroll={}
n=int(input("Enter the number of employees: "))
for i in range(n):
    emp_id=int(input("Enter employee ID: "))
    name=input("Enter employee name: ")
    basic=float(input("Enter basic salary: "))
    allowance=float(input("Enter allowance: "))
    payroll[emp_id]=(name,basic,allowance)
try:
    file=open("payroll.txt","w")
    for emp_id,data in payroll.items():
        name,basic,allowance=data
        net_salary=basic+allowance
        file.write(str(emp_id)+" "+name+" "+str(net_salary)+"\n")
    file.close()
    print("Payroll data saved to file")
except Exception as e:
    print("Error saving payroll data to file",e)