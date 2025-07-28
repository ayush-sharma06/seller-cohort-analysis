-- sql/cohort_queries.sql

-- 1) Cohort sizes for 2025
SELECT
  cohort_year,
  cohort_month,
  SUM(active_sellers) AS cohort_size
FROM metrics
WHERE cohort_year = 2025
GROUP BY cohort_year, cohort_month
ORDER BY cohort_month;

-- 2) Monthly retention rates
WITH base AS (
  SELECT
    cohort_year,
    cohort_month,
    SUM(active_sellers) AS cohort_size
  FROM metrics
  GROUP BY cohort_year, cohort_month
)
SELECT
  m.cohort_year,
  m.cohort_month,
  m.order_year,
  m.order_month,
  m.active_sellers * 1.0 / b.cohort_size AS retention_rate
FROM metrics m
JOIN base b
  ON m.cohort_year = b.cohort_year
 AND m.cohort_month = b.cohort_month
ORDER BY m.cohort_year, m.cohort_month, m.order_year, m.order_month;

-- 3) Total cohort revenue trends
SELECT
  cohort_year,
  cohort_month,
  SUM(total_revenue) AS cohort_revenue
FROM metrics
GROUP BY cohort_year, cohort_month
ORDER BY cohort_year, cohort_month;
