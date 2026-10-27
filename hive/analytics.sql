-- 1. Most-issued books
SELECT
    book_title,
    COUNT(*) AS total_issues
FROM library_books
GROUP BY book_title
ORDER BY total_issues DESC;

-- 2. Most popular book categories
SELECT
    category,
    COUNT(*) AS total_issues
FROM library_books
GROUP BY category
ORDER BY total_issues DESC;

-- 3. Monthly borrowing trends
SELECT
    DATE_FORMAT(issue_date, 'yyyy-MM') AS month,
    COUNT(*) AS total_issues
FROM library_books
GROUP BY DATE_FORMAT(issue_date, 'yyyy-MM')
ORDER BY month;

-- 4. Most frequent borrowers
SELECT
    student_id,
    COUNT(*) AS books_borrowed
FROM library_books
GROUP BY student_id
ORDER BY books_borrowed DESC;
