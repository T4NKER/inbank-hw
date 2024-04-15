SELECT 
    SUM(
        CASE
            WHEN c.CURRENCY_CODE = 'EUR' THEN p.AMOUNT
            ELSE p.AMOUNT * er.EXCHANGE_RATE_TO_EUR
        END
    ) AS AMOUNT_IN_EUR, p.TRANSACTION_DATE
FROM PAYMENTS p
    LEFT JOIN CURRENCIES c ON p.CURRENCY = c.CURRENCY_ID
    LEFT JOIN CURRENCY_RATES er ON c.CURRENCY_ID = er.CURRENCY_ID
    AND er.EXCHANGE_DATE = p.TRANSACTION_DATE
    LEFT JOIN BLACKLIST bl ON bl.USER_ID = p.USER_ID_SENDER
WHERE (
        bl.USER_ID IS NULL
        AND c.END_DATE IS NULL
    )
    OR (
        bl.USER_ID IS NOT NULL
        AND bl.BLACKLIST_END_DATE IS NOT NULL
        AND bl.BLACKLIST_END_DATE < CURRENT_DATE
        AND c.END_DATE IS NULL
    )
GROUP BY p.TRANSACTION_DATE;