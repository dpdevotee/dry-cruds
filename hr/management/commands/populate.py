# pylint: disable=no-member,too-many-statements,expression-not-assigned
from django.core.management.base import BaseCommand

from hr.models import Country, Department, Dependent, Employee, Job, Location, Region


class Command(BaseCommand):
    help = "Create records in the database"

    def handle(self, *args, **options) -> None:
        regions = [
            None,
            Region.objects.create(region_name="Europe"),
            Region.objects.create(region_name="Americas"),
            Region.objects.create(region_name="Asia"),
            Region.objects.create(region_name="Middle East and Africa"),
        ]
        countries = {
            "AR": Country.objects.create(country_id="AR", country_name="Argentina", region=regions[2]),
            "AU": Country.objects.create(country_id="AU", country_name="Australia", region=regions[3]),
            "BE": Country.objects.create(country_id="BE", country_name="Belgium", region=regions[1]),
            "BR": Country.objects.create(country_id="BR", country_name="Brazil", region=regions[2]),
            "CA": Country.objects.create(country_id="CA", country_name="Canada", region=regions[2]),
            "CH": Country.objects.create(country_id="CH", country_name="Switzerland", region=regions[1]),
            "CN": Country.objects.create(country_id="CN", country_name="China", region=regions[3]),
            "DE": Country.objects.create(country_id="DE", country_name="Germany", region=regions[1]),
            "DK": Country.objects.create(country_id="DK", country_name="Denmark", region=regions[1]),
            "EG": Country.objects.create(country_id="EG", country_name="Egypt", region=regions[4]),
            "FR": Country.objects.create(country_id="FR", country_name="France", region=regions[1]),
            "HK": Country.objects.create(country_id="HK", country_name="HongKong", region=regions[3]),
            "IL": Country.objects.create(country_id="IL", country_name="Israel", region=regions[4]),
            "IN": Country.objects.create(country_id="IN", country_name="India", region=regions[3]),
            "IT": Country.objects.create(country_id="IT", country_name="Italy", region=regions[1]),
            "JP": Country.objects.create(country_id="JP", country_name="Japan", region=regions[3]),
            "KW": Country.objects.create(country_id="KW", country_name="Kuwait", region=regions[4]),
            "MX": Country.objects.create(country_id="MX", country_name="Mexico", region=regions[2]),
            "NG": Country.objects.create(country_id="NG", country_name="Nigeria", region=regions[4]),
            "NL": Country.objects.create(country_id="NL", country_name="Netherlands", region=regions[1]),
            "SG": Country.objects.create(country_id="SG", country_name="Singapore", region=regions[3]),
            "UK": Country.objects.create(country_id="UK", country_name="United Kingdom", region=regions[1]),
            "US": Country.objects.create(country_id="US", country_name="United States of America", region=regions[2]),
            "ZM": Country.objects.create(country_id="ZM", country_name="Zambia", region=regions[4]),
            "ZW": Country.objects.create(country_id="ZW", country_name="Zimbabwe", region=regions[4]),
        }
        locations = [
            Location.objects.create(
                street_address="2014 Jabberwocky Rd",
                postal_code="26192",
                city="Southlake",
                state_province="Texas",
                country=countries["US"],
            ),
            Location.objects.create(
                street_address="2011 Interiors Blvd",
                postal_code="99236",
                city="South San Francisco",
                state_province="California",
                country=countries["US"],
            ),
            Location.objects.create(
                street_address="2004 Charade Rd",
                postal_code="98199",
                city="Seattle",
                state_province="Washington",
                country=countries["US"],
            ),
            Location.objects.create(
                street_address="147 Spadina Ave",
                postal_code="M5V 2L7",
                city="Toronto",
                state_province="Ontario",
                country=countries["CA"],
            ),
            Location.objects.create(
                street_address="8204 Arthur St",
                postal_code="None",
                city="London",
                state_province="None",
                country=countries["UK"],
            ),
            Location.objects.create(
                street_address="Magdalen Centre, The Oxford Science Park",
                postal_code="OX9 9ZB",
                city="Oxford",
                state_province="Oxford",
                country=countries["UK"],
            ),
            Location.objects.create(
                street_address="Schwanthalerstr. 7031",
                postal_code="80925",
                city="Munich",
                state_province="Bavaria",
                country=countries["DE"],
            ),
        ]

        departments = [
            None,
            Department.objects.create(department_name="Administration", location=locations[0]),
            Department.objects.create(department_name="Marketing", location=locations[0]),
            Department.objects.create(department_name="Purchasing", location=locations[1]),
            Department.objects.create(department_name="Human Resources", location=locations[2]),
            Department.objects.create(department_name="Shipping", location=locations[3]),
            Department.objects.create(department_name="IT", location=locations[3]),
            Department.objects.create(department_name="Public Relations", location=locations[4]),
            Department.objects.create(department_name="Sales", location=locations[5]),
            Department.objects.create(department_name="Executive", location=locations[5]),
            Department.objects.create(department_name="Finance", location=locations[6]),
            Department.objects.create(department_name="Accounting", location=locations[6]),
        ]

        jobs = [
            None,
            Job.objects.create(job_title="Public Accountant", min_salary=4200.00, max_salary=9000.00),
            Job.objects.create(job_title="Accounting Manager", min_salary=8200.00, max_salary=16000.00),
            Job.objects.create(job_title="Administration Assistant", min_salary=3000.00, max_salary=6000.00),
            Job.objects.create(job_title="President", min_salary=20000.00, max_salary=40000.00),
            Job.objects.create(job_title="Administration Vice President", min_salary=15000.00, max_salary=30000.00),
            Job.objects.create(job_title="Accountant", min_salary=4200.00, max_salary=9000.00),
            Job.objects.create(job_title="Finance Manager", min_salary=8200.00, max_salary=16000.00),
            Job.objects.create(job_title="Human Resources Representative", min_salary=4000.00, max_salary=9000.00),
            Job.objects.create(job_title="Programmer", min_salary=4000.00, max_salary=10000.00),
            Job.objects.create(job_title="Marketing Manager", min_salary=9000.00, max_salary=15000.00),
            Job.objects.create(job_title="Marketing Representative", min_salary=4000.00, max_salary=9000.00),
            Job.objects.create(job_title="Public Relations Representative", min_salary=4500.00, max_salary=10500.00),
            Job.objects.create(job_title="Purchasing Clerk", min_salary=2500.00, max_salary=5500.00),
            Job.objects.create(job_title="Purchasing Manager", min_salary=8000.00, max_salary=15000.00),
            Job.objects.create(job_title="Sales Manager", min_salary=10000.00, max_salary=20000.00),
            Job.objects.create(job_title="Sales Representative", min_salary=6000.00, max_salary=12000.00),
            Job.objects.create(job_title="Shipping Clerk", min_salary=2500.00, max_salary=5500.00),
            Job.objects.create(job_title="Stock Clerk", min_salary=2000.00, max_salary=5000.00),
            Job.objects.create(job_title="Stock Manager", min_salary=5500.00, max_salary=8500.00),
        ]

        employees = []
        employees.append(
            Employee.objects.create(
                first_name="Steven",
                last_name="King",
                email="steven.king@sqltutorial.org",
                phone_number="515.123.4567",
                hire_date="1987-06-17",
                job=jobs[4],
                salary=24000.00,
                department=departments[9],
            )
        )
        employees.append(
            Employee.objects.create(
                first_name="Neena",
                last_name="Kochhar",
                email="neena.kochhar@sqltutorial.org",
                phone_number="515.123.4568",
                hire_date="1989-09-21",
                job=jobs[5],
                salary=17000.00,
                department=departments[9],
                manager=employees[0],
            )
        )
        employees.append(
            Employee.objects.create(
                first_name="Lex",
                last_name="De Haan",
                email="lex.de haan@sqltutorial.org",
                phone_number="515.123.4569",
                hire_date="1993-01-13",
                job=jobs[5],
                salary=17000.00,
                department=departments[9],
                manager=employees[0],
            )
        )
        employees.append(
            Employee.objects.create(
                first_name="Alexander",
                last_name="Hunold",
                email="alexander.hunold@sqltutorial.org",
                phone_number="590.423.4567",
                hire_date="1990-01-03",
                job=jobs[9],
                salary=9000.00,
                department=departments[6],
                manager=employees[2],
            )
        )
        employees.append(
            Employee.objects.create(
                first_name="Bruce",
                last_name="Ernst",
                email="bruce.ernst@sqltutorial.org",
                phone_number="590.423.4568",
                hire_date="1991-05-21",
                job=jobs[9],
                salary=6000.00,
                department=departments[6],
                manager=employees[3],
            )
        )
        employees.append(
            Employee.objects.create(
                first_name="David",
                last_name="Austin",
                email="david.austin@sqltutorial.org",
                phone_number="590.423.4569",
                hire_date="1997-06-25",
                job=jobs[9],
                salary=4800.00,
                department=departments[6],
                manager=employees[3],
            )
        )
        employees.append(
            Employee.objects.create(
                first_name="Valli",
                last_name="Pataballa",
                email="valli.pataballa@sqltutorial.org",
                phone_number="590.423.4560",
                hire_date="1998-02-05",
                job=jobs[9],
                salary=4800.00,
                department=departments[6],
                manager=employees[3],
            )
        )
        employees.append(
            Employee.objects.create(
                first_name="Diana",
                last_name="Lorentz",
                email="diana.lorentz@sqltutorial.org",
                phone_number="590.423.5567",
                hire_date="1999-02-07",
                job=jobs[9],
                salary=4200.00,
                department=departments[6],
                manager=employees[3],
            )
        )
        employees.append(
            Employee.objects.create(
                first_name="Nancy",
                last_name="Greenberg",
                email="nancy.greenberg@sqltutorial.org",
                phone_number="515.124.4569",
                hire_date="1994-08-17",
                job=jobs[7],
                salary=12000.00,
                department=departments[10],
                manager=employees[1],
            )
        )
        employees.append(
            Employee.objects.create(
                first_name="Daniel",
                last_name="Faviet",
                email="daniel.faviet@sqltutorial.org",
                phone_number="515.124.4169",
                hire_date="1994-08-16",
                job=jobs[6],
                salary=9000.00,
                department=departments[10],
                manager=employees[8],
            )
        )
        employees.append(
            Employee.objects.create(
                first_name="John",
                last_name="Chen",
                email="john.chen@sqltutorial.org",
                phone_number="515.124.4269",
                hire_date="1997-09-28",
                job=jobs[6],
                salary=8200.00,
                department=departments[10],
                manager=employees[8],
            )
        )
        employees.append(
            Employee.objects.create(
                first_name="Ismael",
                last_name="Sciarra",
                email="ismael.sciarra@sqltutorial.org",
                phone_number="515.124.4369",
                hire_date="1997-09-30",
                job=jobs[6],
                salary=7700.00,
                department=departments[10],
                manager=employees[8],
            )
        )
        employees.append(
            Employee.objects.create(
                first_name="Jose Manuel",
                last_name="Urman",
                email="jose manuel.urman@sqltutorial.org",
                phone_number="515.124.4469",
                hire_date="1998-03-07",
                job=jobs[6],
                salary=7800.00,
                department=departments[10],
                manager=employees[8],
            )
        )
        employees.append(
            Employee.objects.create(
                first_name="Luis",
                last_name="Popp",
                email="luis.popp@sqltutorial.org",
                phone_number="515.124.4567",
                hire_date="1999-12-07",
                job=jobs[6],
                salary=6900.00,
                department=departments[10],
                manager=employees[8],
            )
        )
        employees.append(
            Employee.objects.create(
                first_name="Den",
                last_name="Raphaely",
                email="den.raphaely@sqltutorial.org",
                phone_number="515.127.4561",
                hire_date="1994-12-07",
                job=jobs[14],
                salary=11000.00,
                department=departments[3],
                manager=employees[0],
            )
        )
        employees.append(
            Employee.objects.create(
                first_name="Alexander",
                last_name="Khoo",
                email="alexander.khoo@sqltutorial.org",
                phone_number="515.127.4562",
                hire_date="1995-05-18",
                job=jobs[13],
                salary=3100.00,
                department=departments[3],
                manager=employees[14],
            )
        )
        employees.append(
            Employee.objects.create(
                first_name="Shelli",
                last_name="Baida",
                email="shelli.baida@sqltutorial.org",
                phone_number="515.127.4563",
                hire_date="1997-12-24",
                job=jobs[13],
                salary=2900.00,
                department=departments[3],
                manager=employees[14],
            )
        )
        employees.append(
            Employee.objects.create(
                first_name="Sigal",
                last_name="Tobias",
                email="sigal.tobias@sqltutorial.org",
                phone_number="515.127.4564",
                hire_date="1997-07-24",
                job=jobs[13],
                salary=2800.00,
                department=departments[3],
                manager=employees[14],
            )
        )
        employees.append(
            Employee.objects.create(
                first_name="Guy",
                last_name="Himuro",
                email="guy.himuro@sqltutorial.org",
                phone_number="515.127.4565",
                hire_date="1998-11-15",
                job=jobs[13],
                salary=2600.00,
                department=departments[3],
                manager=employees[14],
            )
        )
        employees.append(
            Employee.objects.create(
                first_name="Karen",
                last_name="Colmenares",
                email="karen.colmenares@sqltutorial.org",
                phone_number="515.127.4566",
                hire_date="1999-08-10",
                job=jobs[13],
                salary=2500.00,
                department=departments[3],
                manager=employees[14],
            )
        )
        employees.append(
            Employee.objects.create(
                first_name="Matthew",
                last_name="Weiss",
                email="matthew.weiss@sqltutorial.org",
                phone_number="650.123.1234",
                hire_date="1996-07-18",
                job=jobs[19],
                salary=8000.00,
                department=departments[5],
                manager=employees[0],
            )
        )
        employees.append(
            Employee.objects.create(
                first_name="Adam",
                last_name="Fripp",
                email="adam.fripp@sqltutorial.org",
                phone_number="650.123.2234",
                hire_date="1997-04-10",
                job=jobs[19],
                salary=8200.00,
                department=departments[5],
                manager=employees[0],
            )
        )
        employees.append(
            Employee.objects.create(
                first_name="Payam",
                last_name="Kaufling",
                email="payam.kaufling@sqltutorial.org",
                phone_number="650.123.3234",
                hire_date="1995-05-01",
                job=jobs[19],
                salary=7900.00,
                department=departments[5],
                manager=employees[0],
            )
        )
        employees.append(
            Employee.objects.create(
                first_name="Shanta",
                last_name="Vollman",
                email="shanta.vollman@sqltutorial.org",
                phone_number="650.123.4234",
                hire_date="1997-10-10",
                job=jobs[19],
                salary=6500.00,
                department=departments[5],
                manager=employees[0],
            )
        )
        employees.append(
            Employee.objects.create(
                first_name="Irene",
                last_name="Mikkilineni",
                email="irene.mikkilineni@sqltutorial.org",
                phone_number="650.124.1224",
                hire_date="1998-09-28",
                job=jobs[18],
                salary=2700.00,
                department=departments[5],
                manager=employees[20],
            )
        )
        employees.append(
            Employee.objects.create(
                first_name="John",
                last_name="Russell",
                email="john.russell@sqltutorial.org",
                phone_number="None",
                hire_date="1996-10-01",
                job=jobs[15],
                salary=14000.00,
                department=departments[8],
                manager=employees[0],
            )
        )
        employees.append(
            Employee.objects.create(
                first_name="Karen",
                last_name="Partners",
                email="karen.partners@sqltutorial.org",
                phone_number="None",
                hire_date="1997-01-05",
                job=jobs[15],
                salary=13500.00,
                department=departments[8],
                manager=employees[0],
            )
        )
        employees.append(
            Employee.objects.create(
                first_name="Jonathon",
                last_name="Taylor",
                email="jonathon.taylor@sqltutorial.org",
                phone_number="None",
                hire_date="1998-03-24",
                job=jobs[16],
                salary=8600.00,
                department=departments[8],
                manager=employees[0],
            )
        )
        employees.append(
            Employee.objects.create(
                first_name="Jack",
                last_name="Livingston",
                email="jack.livingston@sqltutorial.org",
                phone_number="None",
                hire_date="1998-04-23",
                job=jobs[16],
                salary=8400.00,
                department=departments[8],
                manager=employees[0],
            )
        )
        employees.append(
            Employee.objects.create(
                first_name="Kimberely",
                last_name="Grant",
                email="kimberely.grant@sqltutorial.org",
                phone_number="None",
                hire_date="1999-05-24",
                job=jobs[16],
                salary=7000.00,
                department=departments[8],
                manager=employees[0],
            )
        )
        employees.append(
            Employee.objects.create(
                first_name="Charles",
                last_name="Johnson",
                email="charles.johnson@sqltutorial.org",
                phone_number="None",
                hire_date="2000-01-04",
                job=jobs[16],
                salary=6200.00,
                department=departments[8],
                manager=employees[0],
            )
        )
        employees.append(
            Employee.objects.create(
                first_name="Sarah",
                last_name="Bell",
                email="sarah.bell@sqltutorial.org",
                phone_number="650.501.1876",
                hire_date="1996-02-04",
                job=jobs[17],
                salary=4000.00,
                department=departments[5],
                manager=employees[23],
            )
        )
        employees.append(
            Employee.objects.create(
                first_name="Britney",
                last_name="Everett",
                email="britney.everett@sqltutorial.org",
                phone_number="650.501.2876",
                hire_date="1997-03-03",
                job=jobs[17],
                salary=3900.00,
                department=departments[5],
                manager=employees[23],
            )
        )
        employees.append(
            Employee.objects.create(
                first_name="Jennifer",
                last_name="Whalen",
                email="jennifer.whalen@sqltutorial.org",
                phone_number="515.123.4444",
                hire_date="1987-09-17",
                job=jobs[3],
                salary=4400.00,
                department=departments[1],
                manager=employees[1],
            )
        )
        employees.append(
            Employee.objects.create(
                first_name="Michael",
                last_name="Hartstein",
                email="michael.hartstein@sqltutorial.org",
                phone_number="515.123.5555",
                hire_date="1996-02-17",
                job=jobs[10],
                salary=13000.00,
                department=departments[2],
                manager=employees[0],
            )
        )
        employees.append(
            Employee.objects.create(
                first_name="Pat",
                last_name="Fay",
                email="pat.fay@sqltutorial.org",
                phone_number="603.123.6666",
                hire_date="1997-08-17",
                job=jobs[11],
                salary=6000.00,
                department=departments[2],
                manager=employees[34],
            )
        )
        employees.append(
            Employee.objects.create(
                first_name="Susan",
                last_name="Mavris",
                email="susan.mavris@sqltutorial.org",
                phone_number="515.123.7777",
                hire_date="1994-06-07",
                job=jobs[8],
                salary=6500.00,
                department=departments[4],
                manager=employees[1],
            )
        )
        employees.append(
            Employee.objects.create(
                first_name="Hermann",
                last_name="Baer",
                email="hermann.baer@sqltutorial.org",
                phone_number="515.123.8888",
                hire_date="1994-06-07",
                job=jobs[12],
                salary=10000.00,
                department=departments[7],
                manager=employees[1],
            )
        )
        employees.append(
            Employee.objects.create(
                first_name="Shelley",
                last_name="Higgins",
                email="shelley.higgins@sqltutorial.org",
                phone_number="515.123.8080",
                hire_date="1994-06-07",
                job=jobs[2],
                salary=12000.00,
                department=departments[11],
                manager=employees[1],
            )
        )
        employees.append(
            Employee.objects.create(
                first_name="William",
                last_name="Gietz",
                email="william.gietz@sqltutorial.org",
                phone_number="515.123.8181",
                hire_date="1994-06-07",
                job=jobs[1],
                salary=8300.00,
                department=departments[11],
                manager=employees[38],
            )
        )

        Dependent.objects.create(first_name="Penelope", last_name="Gietz", relationship="Child", employee=employees[12])
        Dependent.objects.create(first_name="Nick", last_name="Higgins", relationship="Child", employee=employees[28])
        Dependent.objects.create(first_name="Ed", last_name="Whalen", relationship="Child", employee=employees[9])
        Dependent.objects.create(first_name="Jennifer", last_name="King", relationship="Child", employee=employees[9])
        Dependent.objects.create(first_name="Johnny", last_name="Kochhar", relationship="Child", employee=employees[23])
        Dependent.objects.create(first_name="Bette", last_name="De Haan", relationship="Child", employee=employees[7])
        Dependent.objects.create(first_name="Grace", last_name="Faviet", relationship="Child", employee=employees[16])
        Dependent.objects.create(first_name="Matthew", last_name="Chen", relationship="Child", employee=employees[39])
        Dependent.objects.create(first_name="Joe", last_name="Sciarra", relationship="Child", employee=employees[10])
        Dependent.objects.create(
            first_name="Christian", last_name="Urman", relationship="Child", employee=employees[28]
        )
        Dependent.objects.create(first_name="Zero", last_name="Popp", relationship="Child", employee=employees[24])
        Dependent.objects.create(first_name="Karl", last_name="Greenberg", relationship="Child", employee=employees[21])
        Dependent.objects.create(first_name="Uma", last_name="Mavris", relationship="Child", employee=employees[38])
        Dependent.objects.create(first_name="Vivien", last_name="Hunold", relationship="Child", employee=employees[19])
        Dependent.objects.create(first_name="Cuba", last_name="Ernst", relationship="Child", employee=employees[39])
        Dependent.objects.create(first_name="Fred", last_name="Austin", relationship="Child", employee=employees[17])
        Dependent.objects.create(
            first_name="Helen", last_name="Pataballa", relationship="Child", employee=employees[35]
        )
        Dependent.objects.create(first_name="Dan", last_name="Lorentz", relationship="Child", employee=employees[7])
        Dependent.objects.create(first_name="Bob", last_name="Hartstein", relationship="Child", employee=employees[6])
        Dependent.objects.create(first_name="Lucille", last_name="Fay", relationship="Child", employee=employees[6])
        Dependent.objects.create(first_name="Kirsten", last_name="Baer", relationship="Child", employee=employees[30])
        Dependent.objects.create(first_name="Elvis", last_name="Khoo", relationship="Child", employee=employees[15])
        Dependent.objects.create(first_name="Sandra", last_name="Baida", relationship="Child", employee=employees[31])
        Dependent.objects.create(first_name="Cameron", last_name="Tobias", relationship="Child", employee=employees[3])
        Dependent.objects.create(first_name="Kevin", last_name="Himuro", relationship="Child", employee=employees[24])
        Dependent.objects.create(first_name="Rip", last_name="Colmenares", relationship="Child", employee=employees[22])
        Dependent.objects.create(first_name="Julia", last_name="Raphaely", relationship="Child", employee=employees[15])
        Dependent.objects.create(first_name="Woody", last_name="Russell", relationship="Child", employee=employees[32])
        Dependent.objects.create(first_name="Alec", last_name="Partners", relationship="Child", employee=employees[2])
        Dependent.objects.create(first_name="Sandra", last_name="Taylor", relationship="Child", employee=employees[17])

        self.stdout.write(self.style.SUCCESS("All records successfully created"))
