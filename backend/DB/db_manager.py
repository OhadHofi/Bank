import pymysql

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
    
    def get_all_transactions_with_categories(self):
        query : str = """   SELECT Bank_Transaction.id, Bank_Transaction.amount, Category.id, Category.vendor, Category.category
                            FROM Bank_Transaction JOIN TransactionCategory
                            ON Bank_Transaction.id = TransactionCategory.transaction_id
                            JOIN Category
                            ON Category.id = TransactionCategory.category_id;"""
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            return result


    def add_transaction(self , amount:int, vendor:str, category:str):
        add_bank_transaction_query : str =  """INSERT INTO Bank_Transaction (amount)
                                                VALUES ('{amount}');"""
        add_category_query : str =          """INSERT INTO Category (vendor, category)
                                                VALUES ('{vendor}', '{category}');"""
        add_transaction_category_query =    """INSERT INTO TransactionCategory (transaction_id, category_id)
                                                VALUES(%d, %d);"""

        with self.connection.cursor() as cursor:
            cursor.execute(add_bank_transaction_query)
            transaction_id:int = cursor.lastrowid

            cursor.execute(add_category_query)
            category_id:int = cursor.lastrowid

            cursor.execute(add_transaction_category_query, [transaction_id, category_id])

            self.connection.commit()




    def delete_transaction(self, transaction_id: int, category_id: int):
        delete_by_id_query : str =  """DELETE FROM %s WHERE id=%d;"""
        delete_transaction_category_query : str =   """DELETE FROM TransactionCategory 
                                                    WHERE transaction_id={transaction_id} AND category_id={category_id};"""

        with self.connection.cursor() as cursor:
            cursor.execute(delete_by_id_query, ["Bank_Transaction", transaction_id])
            cursor.execute(delete_by_id_query, ["Category", category_id])
            cursor.execute(delete_transaction_category_query)
            self.connection.commit()


    def get_all_categories_with_sum_of_amount(self):
        categories_with_sum_of_amount_quary: str =  """ SELECT Category.category, SUM(Bank_Transaction.amount),
                                                        FROM Bank_Transaction JOIN TransactionCategory
                                                        ON Bank_Transaction.id = TransactionCategory.transaction_id
                                                        JOIN Category
                                                        ON Category.id = TransactionCategory.category_id
                                                        GROUP BY Category.category"""
        with self.connection.cursor() as cursor:
            cursor.execute(categories_with_sum_of_amount_quary)
            result = cursor.fetchall()
            return result

db_manager = DB_Manager()

print("fd")
print(db_manager.get_all_transactions_with_categories())
print("o")