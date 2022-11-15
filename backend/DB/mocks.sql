SELECT Category.category, SUM(Bank_Transaction.amount),
    FROM Bank_Transaction JOIN TransactionCategory
    ON Bank_Transaction.id = TransactionCategory.transaction_id
    JOIN Category
    ON Category.id = TransactionCategory.category_id
    GROUP BY Category.category