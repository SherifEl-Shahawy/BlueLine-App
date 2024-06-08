import sqlite3

# ===================SQL Connectivity=================

# SQL Connection
connection = sqlite3.connect('collective.db')
cursor = connection.cursor()

connection_1 = sqlite3.connect('Materials.db')
cursor_1 = connection_1.cursor()


# SQL functions


def check_store(date_1, pay, from_1, tor, owner, bank, detail):
    cursor.execute(
        'INSERT INTO Checks VALUES (:Service, :Date, :Payment, :From_1, :To_2, :Owner, :Bank_n, :Details)',
        {
            'Service': 1,
            'Date': date_1,
            'Payment': pay,
            'From_1': from_1,
            'To_2': tor,
            'Owner': owner,
            'Bank_n': bank,
            'Details': detail
        })
    connection.commit()


def check_ftch():
    cursor.execute('SELECT Date,Payment,From_1,To_2,Owner,Bank_n,Details FROM Checks ORDER BY Date DESC')
    recordy = cursor.fetchall()
    return recordy


def check_owner_ftch():
    cursor.execute('SELECT Owner FROM Checks ORDER BY Date DESC')
    recordy = cursor.fetchall()
    return recordy


def check_delete(name, date):
    cursor.execute(f"DELETE FROM Checks WHERE Owner = '{name}' AND Date = '{date}'")
    connection.commit()

# ============== Guests ======== #


def guests_store(name_1, prod, color, weight, price, total, date_1):
    cursor.execute(
        'INSERT INTO Clients VALUES (:Service, :Name, :Prod, :Color, :Weight, :Price, :Total, :Date)',
        {
            'Service': 1,
            'Name': name_1,
            'Prod': prod,
            'Color': color,
            'Weight': weight,
            'Price': price,
            'Total': total,
            'Date': date_1
        })
    connection.commit()


def guests_client_pay(name_1, payment, date):
    cursor.execute('INSERT INTO Clients_Payment VALUES (:Service, :Name, :Payment, :Date)',
                   {
                       'Service': 1,
                       'Name': name_1,
                       'Payment': payment,
                       'Date': date
                   })
    connection.commit()


def guests_dealer_deleted(name, pay, date):
    cursor.execute(f"DELETE FROM Clients_Payment WHERE Name = '{name}' AND Date = '{date}' AND Payment = '{pay}'")
    connection.commit()


def guests_ftchs():
    cursor.execute('SELECT Name FROM Prof_Client')
    pro_name = cursor.fetchall()
    pro_list = []
    for name in pro_name:
        nx = str(name[0])
        pro_list.append(nx)
    return pro_list


def guests_pay_ftchs(name):
    cursor.execute(f'SELECT Date,Payment FROM Clients_Payment WHERE Name = "{name}" ORDER BY Date DESC')
    pro_name = cursor.fetchall()
    return pro_name


def colors_ftchs():
    cursor_1.execute('SELECT Name FROM Color_T')
    q_name = cursor_1.fetchall()
    q_list = []
    for name in q_name:
        nx = str(name[0])
        q_list.append(nx)
    return q_list


def client_rets_f(name_1):
    cursor.execute(f'SELECT Rest FROM Prof_Client WHERE Name = "{name_1}" ')
    pro_rest = cursor.fetchall()
    pro_list = []
    for name in pro_rest:
        nx = str(name[0])
        pro_list.append(nx)
    return pro_list


def guests_pro(name_1, total):
    cursor.execute('INSERT INTO Prof_Client VALUES (:Service, :Name, :Total, :Edit_Color, :Rest)',
                   {
                       'Service': 1,
                       'Name': name_1,
                       'Total': total,
                       'Edit_Color': 0,
                       'Rest': total
                   })
    connection.commit()


def guests_pro_del(name):
    cursor.execute(f"DELETE FROM Prof_Client WHERE Name = '{name}'")
    connection.commit()

    
def guests_store_del(name, date, prod):
    cursor.execute(f"SELECT Total FROM Clients WHERE Name = '{name}' AND Date = '{date}' AND Prod = '{prod}'")
    total_minu = cursor.fetchone()
    cursor.execute(f'UPDATE Prof_Client SET Total = Total - {total_minu[0]} WHERE Name = "{name}"')
    cursor.execute(f'UPDATE Prof_Client SET Rest = Rest - {total_minu[0]} WHERE Name = "{name}"')
    cursor.execute(f"DELETE FROM Clients WHERE Name = '{name}' AND Date = '{date}' AND Prod = '{prod}'")
    connection.commit()


def guests_upd(name_1, total):
    cursor.execute(f'UPDATE Prof_Client SET Total = Total + {total} WHERE Name = "{name_1}"')
    cursor.execute(f'UPDATE Prof_Client SET Rest = Rest + {total} WHERE Name = "{name_1}"')
    connection.commit()


def client_upd_rt(name_1, pay):
    cursor.execute(f'UPDATE Prof_Client SET Paid = Paid + {pay} WHERE Name = "{name_1}"')
    cursor.execute(f'UPDATE Prof_Client SET Rest = Rest - {pay} WHERE Name = "{name_1}"')
    connection.commit()

def client_upd_del(name_1, pay):
    cursor.execute(f'UPDATE Prof_Client SET Total = Total - {pay} WHERE Name = "{name_1}"')
    cursor.execute(f'UPDATE Prof_Client SET Rest = Rest + {pay} WHERE Name = "{name_1}"')
    connection.commit()


# =================== mater ================= #


def mater_store(name_1, kind, quant, price, total, date_1):
    cursor.execute(
        'INSERT INTO Dealers VALUES (:Service, :Name, :Kind, :Quant, :Cost, :Total, :Date)',
        {
            'Service': 1,
            'Name': name_1,
            'Kind': kind,
            'Quant': quant,
            'Cost': price,
            'Total': total,
            'Date': date_1
        })
    connection.commit()


def mater_pro(name_1, total):
    cursor.execute('INSERT INTO Prof_Deal VALUES (:Service, :Name, :Total, :Edit_Color, :Rest)',
                   {
                       'Service': 1,
                       'Name': name_1,
                       'Total': total,
                       'Edit_Color': 0,
                       'Rest': total
                   })
    connection.commit()
    
def mater_pro_del(name):
    cursor.execute(f"DELETE FROM Prof_Deal WHERE Name = '{name}'")
    connection.commit()

    
def mater_store_del(name, date, kind):
    cursor.execute(f"SELECT Total FROM Dealers WHERE Name = '{name}' AND Date = '{date}' AND Kind = '{kind}'")
    total_minu = cursor.fetchone()
    cursor.execute(f'UPDATE Prof_Deal SET Total = Total - {total_minu[0]} WHERE Name = "{name}"')
    cursor.execute(f'UPDATE Prof_Deal SET Rest = Rest - {total_minu[0]} WHERE Name = "{name}"')
    cursor.execute(f"DELETE FROM Dealers WHERE Name = '{name}' AND Date = '{date}' AND Kind = '{kind}'")
    connection.commit()


def mater_dealer_pay(name_1, payment, date):
    cursor.execute('INSERT INTO Dealers_Payment VALUES (:Service, :Name, :Payment, :Date)',
                   {
                       'Service': 1,
                       'Name': name_1,
                       'Payment': payment,
                       'Date': date
                   })
    connection.commit()


def mater_dealer_deleted(name, pay, date):
    cursor.execute(f"DELETE FROM Dealers_Payment WHERE Name = '{name}' AND Date = '{date}' AND Payment = '{pay}'")
    connection.commit()



def mater_ftchs():
    cursor.execute('SELECT Name FROM Prof_Deal')
    pro_name = cursor.fetchall()
    pro_list = []
    for name in pro_name:
        nx = str(name[0])
        pro_list.append(nx)
    return pro_list


def kind_ftchs():
    cursor_1.execute('SELECT Name FROM Material_Q')
    q_name = cursor_1.fetchall()
    q_list = []
    for name in q_name:
        nx = str(name[0])
        q_list.append(nx)
    return q_list


def mater_pay_ftchs(name):
    cursor.execute(f'SELECT Date,Payment FROM Dealers_Payment WHERE Name = "{name}" ORDER BY Date DESC')
    pro_name = cursor.fetchall()
    return pro_name


def mater_price_ftchs():
    cursor_1.execute(f'SELECT Name,Price FROM Material_Q')
    pro_name = cursor_1.fetchall()
    return pro_name


def mater_quant_ftchs():
    cursor_1.execute(f'SELECT Name,Storage FROM Material_Q')
    pro_name = cursor_1.fetchall()
    return pro_name


def mater_rets_f(name_1):
    cursor.execute(f'SELECT Rest FROM Prof_Deal WHERE Name = "{name_1}" ')
    pro_rest = cursor.fetchall()
    pro_list = []
    for name in pro_rest:
        nx = str(name[0])
        pro_list.append(nx)
    return pro_list


def mater_upd(name_1, total):
    cursor.execute(f'UPDATE Prof_Deal SET Total = Total + {total} WHERE Name = "{name_1}"')
    cursor.execute(f'UPDATE Prof_Deal SET Rest = Rest + {total} WHERE Name = "{name_1}"')
    connection.commit()


def mater_upd_rt(name_1, pay):
    cursor.execute(f'UPDATE Prof_Deal SET Total = Total + {pay} WHERE Name = "{name_1}"')
    cursor.execute(f'UPDATE Prof_Deal SET Rest = Rest - {pay} WHERE Name = "{name_1}"')
    connection.commit()


def mater_upd_del(name_1, pay):
    cursor.execute(f'UPDATE Prof_Deal SET Total = Total - {pay} WHERE Name = "{name_1}"')
    cursor.execute(f'UPDATE Prof_Deal SET Rest = Rest + {pay} WHERE Name = "{name_1}"')
    connection.commit()


def q_update(prod, qant, price):
    cursor_1.execute(f'UPDATE Material_Q SET Storage = Storage + {qant} WHERE Name = "{prod}"')
    cursor_1.execute(f'UPDATE Material_Q SET Price = {price} WHERE Name = "{prod}"')
    connection_1.commit()


# =============== Records ============#

def dealers_ftch(name):
    cursor.execute(f'SELECT Date,Kind,Quant,Cost,Total FROM Dealers WHERE Name = "{name}" ORDER BY Date DESC')
    recordy = cursor.fetchall()
    return recordy


def client_ftch(name):
    cursor.execute(f'SELECT Date,Prod,color,Weight,Price,Total FROM Clients WHERE Name = "{name}" ORDER BY Date DESC')
    recordy = cursor.fetchall()
    return recordy


def client_profile():
    cursor.execute('SELECT Name,Edit_Color,Rest FROM Prof_Client')
    recordy = cursor.fetchall()
    return recordy


def deal_profile():
    cursor.execute('SELECT Name,Edit_Color,Rest FROM Prof_Deal')
    recordy = cursor.fetchall()
    return recordy


# =============== Expenses ============#


def fix_store(date_1, title, amount):
    cursor.execute('INSERT INTO Fixed_Exp VALUES (:Date, :Title, :Amount, :Month)',
                   {
                       'Date': date_1,
                       'Title': title,
                       'Amount': amount,
                       'Month': date_1[5:7],
                   })
    connection.commit()


def var_store(date_2, title, amount):
    cursor.execute('INSERT INTO Var_Exp VALUES (:Date, :Title, :Amount, :Month)',
                   {
                       'Date': date_2,
                       'Title': title,
                       'Amount': amount,
                       'Month': date_2[5:7],
                   })
    connection.commit()


def salary_store(date_3, name, amount):
    cursor.execute('INSERT INTO Salary VALUES (:Date, :Name, :Amount, :Month)',
                   {
                       'Date': date_3,
                       'Name': name,
                       'Amount': amount,
                       'Month': date_3[5:7],
                   })
    connection.commit()


def fix_ftch(month_no):
    cursor.execute(f'SELECT Date,Title,Amount FROM Fixed_Exp Where Month = "{month_no}"')
    fixed = cursor.fetchall()
    return fixed


def var_ftch(month_no):
    cursor.execute(f'SELECT Date,Title,Amount FROM Var_Exp Where Month = "{month_no}"')
    varis = cursor.fetchall()
    return varis


def salary_ftch(month_no):
    cursor.execute(f'SELECT Date,Name,Amount FROM Salary Where Month = "{month_no}"')
    slry = cursor.fetchall()
    return slry


# =============== Colors Tab =========== #


def rg_color_t(name, t_n):
    cursor_1.execute('INSERT INTO Color_T VALUES (:Name, :T_N)',
                     {
                         'Name': name,
                         'T_N': t_n
                     })
    connection_1.commit()


def color_ftch_rate(name):
    cursor_1.execute(f'SELECT T_N FROM Color_T Where Name = "{name}"')
    getz = cursor_1.fetchone()
    rev = str(getz[0])
    cursor_1.execute(f'SELECT * FROM {rev} Where Name = "{name}"')
    pro_rest = cursor_1.fetchall()
    return pro_rest


def materials_ftch(name):
    cursor_1.execute(f'SELECT Price FROM Material_Q WHERE Name = "{name}"')
    equals = cursor_1.fetchone()
    return int(equals[0])


def rg_color_1x(name, con_1, con_p_1):
    cursor_1.execute('INSERT INTO M_1x VALUES (:Name, :Con_1, :Con_p_1)',
                     {
                         'Name': name,
                         'Con_1': con_1,
                         'Con_p_1': con_p_1
                     })
    connection_1.commit()


def rg_color_2x(name, con_1, con_p_1, con_2, con_p_2):
    cursor_1.execute('INSERT INTO M_2x VALUES (:Name, :Con_1, :Con_p_1, :Con_2, :Con_p_2)',
                     {
                         'Name': name,
                         'Con_1': con_1,
                         'Con_p_1': con_p_1,
                         'Con_2': con_2,
                         'Con_p_2': con_p_2
                     })
    connection_1.commit()


def rg_color_3x(name, con_1, con_p_1, con_2, con_p_2, con_3, con_p_3):
    cursor_1.execute('INSERT INTO M_3x VALUES (:Name, :Con_1, :Con_p_1, :Con_2, :Con_p_2, :Con_3, :Con_p_3)',
                     {
                         'Name': name,
                         'Con_1': con_1,
                         'Con_p_1': con_p_1,
                         'Con_2': con_2,
                         'Con_p_2': con_p_2,
                         'Con_3': con_3,
                         'Con_p_3': con_p_3
                     })
    connection_1.commit()


def rg_color_4x(name, con_1, con_p_1, con_2, con_p_2, con_3, con_p_3, con_4, con_p_4):
    cursor_1.execute(
        'INSERT INTO M_4x VALUES (:Name, :Con_1, :Con_p_1, :Con_2, :Con_p_2, :Con_3, :Con_p_3, :Con_4, :Con_p_4)',
        {
            'Name': name,
            'Con_1': con_1,
            'Con_p_1': con_p_1,
            'Con_2': con_2,
            'Con_p_2': con_p_2,
            'Con_3': con_3,
            'Con_p_3': con_p_3,
            'Con_4': con_4,
            'Con_p_4': con_p_4
        })
    connection_1.commit()


def rg_color_5x(name, con_1, con_p_1, con_2, con_p_2, con_3, con_p_3, con_4, con_p_4, con_5, con_p_5):
    cursor_1.execute(
        'INSERT INTO M_5x VALUES (:Name, :Con_1, :Con_p_1, :Con_2, :Con_p_2, :Con_3, :Con_p_3, :Con_4, :Con_p_4, :Con_5, :Con_p_5)',
        {
            'Name': name,
            'Con_1': con_1,
            'Con_p_1': con_p_1,
            'Con_2': con_2,
            'Con_p_2': con_p_2,
            'Con_3': con_3,
            'Con_p_3': con_p_3,
            'Con_4': con_4,
            'Con_p_4': con_p_4,
            'Con_5': con_5,
            'Con_p_5': con_p_5
        })
    connection_1.commit()


def rg_color_6x(name, con_1, con_p_1, con_2, con_p_2, con_3, con_p_3, con_4, con_p_4, con_5, con_p_5, con_6, con_p_6):
    cursor_1.execute(
        'INSERT INTO M_6x VALUES (:Name, :Con_1, :Con_p_1, :Con_2, :Con_p_2, :Con_3, :Con_p_3, :Con_4, :Con_p_4, :Con_5, :Con_p_5, :Con_6, :Con_p_6)',
        {
            'Name': name,
            'Con_1': con_1,
            'Con_p_1': con_p_1,
            'Con_2': con_2,
            'Con_p_2': con_p_2,
            'Con_3': con_3,
            'Con_p_3': con_p_3,
            'Con_4': con_4,
            'Con_p_4': con_p_4,
            'Con_5': con_5,
            'Con_p_5': con_p_5,
            'Con_6': con_6,
            'Con_p_6': con_p_6
        })
    connection_1.commit()


def rg_color_7x(name, con_1, con_p_1, con_2, con_p_2, con_3, con_p_3, con_4, con_p_4, con_5, con_p_5, con_6, con_p_6,
                con_7, con_p_7):
    cursor_1.execute(
        'INSERT INTO M_7x VALUES (:Name, :Con_1, :Con_p_1, :Con_2, :Con_p_2, :Con_3, :Con_p_3, :Con_4, :Con_p_4, :Con_5, :Con_p_5, :Con_6, :Con_p_6, :Con_7, :Con_p_7)',
        {
            'Name': name,
            'Con_1': con_1,
            'Con_p_1': con_p_1,
            'Con_2': con_2,
            'Con_p_2': con_p_2,
            'Con_3': con_3,
            'Con_p_3': con_p_3,
            'Con_4': con_4,
            'Con_p_4': con_p_4,
            'Con_5': con_5,
            'Con_p_5': con_p_5,
            'Con_6': con_6,
            'Con_p_6': con_p_6,
            'Con_7': con_7,
            'Con_p_7': con_p_7
        })
    connection_1.commit()


def rg_color_8x(name, con_1, con_p_1, con_2, con_p_2, con_3, con_p_3, con_4, con_p_4, con_5, con_p_5, con_6, con_p_6,
                con_7, con_p_7, con_8, con_p_8):
    cursor_1.execute(
        'INSERT INTO M_8x VALUES (:Name, :Con_1, :Con_p_1, :Con_2, :Con_p_2, :Con_3, :Con_p_3, :Con_4, :Con_p_4, :Con_5, :Con_p_5, :Con_6, :Con_p_6, :Con_7, :Con_p_7, :Con_8, :Con_p_8)',
        {
            'Name': name,
            'Con_1': con_1,
            'Con_p_1': con_p_1,
            'Con_2': con_2,
            'Con_p_2': con_p_2,
            'Con_3': con_3,
            'Con_p_3': con_p_3,
            'Con_4': con_4,
            'Con_p_4': con_p_4,
            'Con_5': con_5,
            'Con_p_5': con_p_5,
            'Con_6': con_6,
            'Con_p_6': con_p_6,
            'Con_7': con_7,
            'Con_p_7': con_p_7,
            'Con_8': con_8,
            'Con_p_8': con_p_8
        })
    connection_1.commit()


def rg_color_9x(name, con_1, con_p_1, con_2, con_p_2, con_3, con_p_3, con_4, con_p_4, con_5, con_p_5, con_6, con_p_6,
                con_7, con_p_7, con_8, con_p_8, con_9, con_p_9):
    cursor_1.execute(
        'INSERT INTO M_9x VALUES (:Name, :Con_1, :Con_p_1, :Con_2, :Con_p_2, :Con_3, :Con_p_3, :Con_4, :Con_p_4, :Con_5, :Con_p_5, :Con_6, :Con_p_6, :Con_7, :Con_p_7, :Con_8, :Con_p_8, :Con_9, :Con_p_9)',
        {
            'Name': name,
            'Con_1': con_1,
            'Con_p_1': con_p_1,
            'Con_2': con_2,
            'Con_p_2': con_p_2,
            'Con_3': con_3,
            'Con_p_3': con_p_3,
            'Con_4': con_4,
            'Con_p_4': con_p_4,
            'Con_5': con_5,
            'Con_p_5': con_p_5,
            'Con_6': con_6,
            'Con_p_6': con_p_6,
            'Con_7': con_7,
            'Con_p_7': con_p_7,
            'Con_8': con_8,
            'Con_p_8': con_p_8,
            'Con_9': con_9,
            'Con_p_9': con_p_9
        })
    connection_1.commit()


def rg_color_10x(name, con_1, con_p_1, con_2, con_p_2, con_3, con_p_3, con_4, con_p_4, con_5, con_p_5, con_6, con_p_6,
                 con_7, con_p_7, con_8, con_p_8, con_9, con_p_9, con_10, con_p_10):
    cursor_1.execute(
        'INSERT INTO M_10x VALUES (:Name, :Con_1, :Con_p_1, :Con_2, :Con_p_2, :Con_3, :Con_p_3, :Con_4, :Con_p_4, :Con_5, :Con_p_5, :Con_6, :Con_p_6, :Con_7, :Con_p_7, :Con_8, :Con_p_8, :Con_9, :Con_p_9, :Con_10, :Con_p_10)',
        {
            'Name': name,
            'Con_1': con_1,
            'Con_p_1': con_p_1,
            'Con_2': con_2,
            'Con_p_2': con_p_2,
            'Con_3': con_3,
            'Con_p_3': con_p_3,
            'Con_4': con_4,
            'Con_p_4': con_p_4,
            'Con_5': con_5,
            'Con_p_5': con_p_5,
            'Con_6': con_6,
            'Con_p_6': con_p_6,
            'Con_7': con_7,
            'Con_p_7': con_p_7,
            'Con_8': con_8,
            'Con_p_8': con_p_8,
            'Con_9': con_9,
            'Con_p_9': con_p_9,
            'Con_10': con_10,
            'Con_p_10': con_p_10
        })
    connection_1.commit()


def color_del(name):
    cursor_1.execute(f"DELETE FROM Color_T WHERE Name = '{name}'")
    connection_1.commit()
