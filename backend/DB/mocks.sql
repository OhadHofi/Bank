use bank;

INSERT INTO bank_transaction
OUTPUT Inserted.ID
(amount, vendor, category)

-- VALUES (200, "v2", "c1");

-- SELECT category, sum(amount) FROM bank_transaction GROUP BY category

SELECT * from Bank_Transaction