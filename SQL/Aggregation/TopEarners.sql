SELECT
    (SALARY * MONTHS),
    COUNT(*)
FROM
    EMPLOYEE
WHERE
    (SALARY * MONTHS) =
        (
            SELECT
                MAX(SALARY * MONTHS)
            FROM
                EMPLOYEE
        )
GROUP BY
    (SALARY * MONTHS);
