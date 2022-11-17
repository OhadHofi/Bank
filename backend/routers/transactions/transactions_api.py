from fastapi import APIRouter, Response, status
# from . import transactions_utils
from .transaction import Transaction
from DB.db_manager import db_manager


router = APIRouter()

@router.get("/transactions")
def get_all_transactions(response: Response):
    try:
        return {"transactions": db_manager.get_all_table("Bank_transaction")}
    except Exception as error:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return error
        


@router.post("/transactions")
def add_transaction(transaction:Transaction, response: Response):
    try:
        response.status_code = status.HTTP_201_CREATED
        return {"transaction": db_manager.add_transaction(transaction)}
    except Exception as error:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return error


@router.delete("/transactions/{transactions_id}")
def delete_hero(transactions_id: int, response: Response):
    try:
        response.status_code = status.HTTP_204_NO_CONTENT
        return {"transactions": db_manager.delete_by_one_number_key("Bank_transaction", "id", transactions_id)}
    except Exception as error:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return error



@router.get("/transactions/category")
def get_amount_by_category(response: Response):
    try:
        return db_manager.get_all_categories_with_sum_of_amount()
    except Exception as error:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return error

    
