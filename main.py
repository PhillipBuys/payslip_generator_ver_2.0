gross_pay = 0
gross_after_paye = 0
nett_pay = 0
full_time_men = 0
women_total_paye = []
paye = 0
total_paid = []
medical_aid = 0

number = (input("number? "))

while number != '0':
    if number == "0":
        break

    name = input("name? ")
    hours = int(input("hours? "))

    gender = input("gender? ")

    code = int(input('Code? '))
    if code == 1:
        gross_pay = (hours * 30)
        total_paid.append(gross_pay)

        if gender == 'm':
            paye = (gross_pay * 0.15)
            medical_aid = 200
        elif gender == 'f':
            paye = (gross_pay * 0.1)
            medical_aid = 100

    elif code == 2:
        gross_pay = (hours * 20)
        medical_aid = 0
        total_paid.append(gross_pay)

        if gender == 'm':
            paye = (gross_pay * 0.1)
        elif gender == 'f':
            paye = (gross_pay * 0.05)

    if gender == 'm':
        gross_pay = float(gross_pay)
        gross_after_paye = gross_pay - paye
        nett_pay = gross_after_paye - medical_aid

        if code == 1 and gender == 'm':
            full_time_men += 1

        print(f'{number},{name},{hours},{gender},{code}')
        print('**********')
        print(f'ID:{number}')
        print(f'Name:{name}')
        print(f'Gross:{gross_pay}')
        print(f'PAYE:{paye}')
        print(f'Medical aid: {medical_aid}')
        print(f'Total Deductions: {(paye + medical_aid)}')
        print(f'Net:{nett_pay}')
        print('**********')

    elif gender == 'f':
        print('female works')
        gross_pay = float(gross_pay)
        gross_after_paye = gross_pay - paye
        nett_pay = gross_after_paye - medical_aid
        women_total_paye.append(paye)

        print(f'{number},{name},{hours},{gender},{code}')
        print('**********')
        print(f'ID:{number}')
        print(f'{name}')
        print(f'Gross:{gross_pay}')
        print(f'PAYE:{paye}')
        print(f'Medical aid: {medical_aid}')
        print(f'Total Deductions: {(paye + medical_aid)}')
        print(f'Net:{nett_pay}')
        print('**********')

    number = (input("number? "))

print(f'The total number of men who work full-time:{full_time_men}')
print(f'the total PAYE paid by women:{sum(women_total_paye)}')
print(f'The total amount paid out by the company to all its employees:{sum(total_paid)}')
