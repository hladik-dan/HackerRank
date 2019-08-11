SELECT
    *
FROM
    (
        SELECT
            CITY,
            LENGTH(CITY)
        FROM
            STATION
        ORDER BY
            LENGTH(CITY) ASC,
            CITY ASC
    )
WHERE
    ROWNUM = 1;

SELECT
    *
FROM
    (
        SELECT
            CITY,
            LENGTH(CITY)
        FROM
            STATION
        ORDER BY
            LENGTH(CITY) DESC,
            CITY ASC
    )
WHERE
    ROWNUM = 1;
