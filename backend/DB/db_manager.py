import pymysql
from routers.transactions.transaction import Transaction

DEFAULT_HOST = "localhost"
DEFAULT_USER = "root"
DEFAULT_DB = "bank"
DEFAULT_PWD = ""

class DB_Manager:
    def __init__(self, host = DEFAULT_HOST, user = DEFAULT_USER, pwd = DEFAULT_PWD, db = DEFAULT_DB):
        self.connection = pymysql.connect(
            host=host,
            user=user,
            password=pwd,
            db=db,
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )
    
    def get_all_table(self, table_name:str) -> list[Transaction]:
        get_table_query : str = f"""SELECT * FROM {table_name}"""

        try:
            self.connection.ping()
            with self.connection.cursor() as cursor:
                cursor.execute(get_table_query)
                result = cursor.fetchall()
                return result
        except Exception as error:
            raise error


    def add_transaction(self , transaction:Transaction) -> Transaction:
        add_transaction_query : str =   f"""INSERT INTO Bank_Transaction (amount, vendor, category) VALUES ({transaction.amount},"{transaction.vendor}","{transaction.category}");"""
        
        try:
            self.connection.ping()
            with self.connection.cursor() as cursor:
                cursor.execute(add_transaction_query)
                transaction_id:int = cursor.lastrowid
                transaction.set_id(transaction_id)
                self.connection.commit()
                return transaction
        except Exception as error:
            raise error




    def delete_by_one_number_key(self, table_name:str, key_name:str, value:int) -> dict:
        delete_by_one_number_key_query : str = f"""DELETE FROM {table_name} WHERE {key_name}={value};"""
        find_by_one_number_key_query : str = f"""SELECT * FROM {table_name} WHERE {key_name}={value};"""

        try:
            self.connection.ping()
            with self.connection.cursor() as cursor:
                cursor.execute(find_by_one_number_key_query)
                result = cursor.fetchone()
                if(cursor.execute(delete_by_one_number_key_query) == 0):
                    raise ValueError('transaction not exist')
                self.connection.commit()
                return result
        except Exception as error:
            raise error


    def get_all_categories_with_sum_of_amount(self) -> list[Transaction]:
        categories_with_sum_of_amount_quary: str =  """SELECT category, sum(amount) as totalAmount FROM bank_transaction GROUP BY category"""
        
        try:
            self.connection.ping()
            with self.connection.cursor() as cursor:
                cursor.execute(categories_with_sum_of_amount_quary)
                res = cursor.fetchall()
                return res
        except Exception as error:
            raise error

    def get_balance(self) -> dict[int]:
        balance_query: str =  """SELECT SUM(amount) as balance FROM Bank_Transaction;"""
        
        try:
            self.connection.ping()
            with self.connection.cursor() as cursor:
                cursor.execute(balance_query)
                res = cursor.fetchone()
                return res
        except Exception as error:
            raise error
    

db_manager = DB_Manager()

