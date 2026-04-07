USE aerofit;

# Finding the number of sales per treadmill type in descending order
SELECT product, COUNT(*) AS qty_sold
FROM data
GROUP BY product
ORDER BY qty_sold DESC
;

# Average income of buyers per treadmill type
SELECT product, ROUND(AVG(income), 2) AS avg_income
FROM data 
GROUP BY product
ORDER BY avg_income DESC
;

# Average age of buyers per treadmill type
SELECT product, ROUND(AVG(age),1) AS avg_age
FROM data 
GROUP BY product
;

# Distribution of buyer fitness level per treadmill type
SELECT product, fitness, COUNT(*) AS count
FROM data
GROUP BY product, fitness
ORDER BY product, fitness
;

# Finding % sums of male, females, single and partnered people per treadmill type
SELECT
    product,
    COUNT(*) AS qty_sold,
    ROUND(SUM(CASE WHEN gender = 'Male' THEN 1.0 ELSE 0 END) / COUNT(*) * 100, 1) AS pct_male,
    ROUND(SUM(CASE WHEN gender = 'Female' THEN 1.0 ELSE 0 END) / COUNT(*) * 100, 1) AS pct_female,
    ROUND(SUM(CASE WHEN maritalstatus = 'Single' THEN 1.0 ELSE 0 END) / COUNT(*) * 100, 1) AS pct_single,
    ROUND(SUM(CASE WHEN maritalstatus = 'Partnered' THEN 1.0 ELSE 0 END) / COUNT(*) * 100, 1) AS pct_partnered
FROM data
GROUP BY product;
