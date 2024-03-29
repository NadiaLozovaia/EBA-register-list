import sqlite3


def hello_world():
    return {"Hello": "World"}


def company_select():
    con = sqlite3.connect("PSDMD.db")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM PSDMD LIMIT 5")
    companies_list = res.fetchall()

    companies = []
    for company in companies_list:

        company_dict = {"id": company[0],
                        "ref_code": company[1],
                        "name_lat": company[2],
                        "name_second": company[3],
                        "country": company[4],
                        "services": company[5],
                        "date": company[6]}
        companies.append(company_dict)

    return companies


def info_company(id_company):
    con = sqlite3.connect("PSDMD.db")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM PSDMD WHERE id = ?", id_company)
    company = res.fetchone()

    company_dict = {"id": company[0],
                    "ref_code": company[1],
                    "name_lat": company[2],
                    "name_second": company[3],
                    "country": company[4],
                    "services": company[5],
                    "date": company[6]}
    
    return company_dict

def company_list_country(country):
    con = sqlite3.connect("PSDMD.db")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM PSDMD WHERE country = ?", (country,))
    companies_list = res.fetchall()
    companies = []
    for company in companies_list:
        company_dict = {
                        "ref_code": company[1],
                        "name_lat": company[2]                       
                        }
       
        companies.append(company_dict)
    return companies

def company_by_ref_code(ref_code):
    con = sqlite3.connect("PSDMD.db")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM PSDMD WHERE  reference_code= ?", (ref_code,))
    company = res.fetchone()
    
    company_dict = {"id": company[0],
                    "ref_code": company[1],
                    "name_lat": company[2],
                    "name_second": company[3],
                    "country": company[4],
                    "services": company[5],
                    "date": company[6]}
    return company_dict
# print(company_by_ref_code('R162223'))