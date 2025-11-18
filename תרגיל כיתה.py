import time
q = 100000
start = time.time()
for _ in range(q):pass
print("O(n):", round(time.time() - start, 5), "seconds")
start = time.time()
for _ in range(q):
 for _ in range(q):pass
print("O(n²):", round(time.time() - start, 5), "seconds")
from models.book import Book
from models.user import User
from typing import List, Optional
        return f"{user.name} returned '{book.title}'."
        
     -- ================================
-- 1. יצירת מסד נתונים
-- ================================
CREATE DATABASE school;
USE school;

-- ================================
-- 2. יצירת טבלה teachers_backup
-- ================================
CREATE TABLE teachers_backup (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    TeacherName VARCHAR(50) NOT NULL,
    Email VARCHAR(70) NOT NULL,
    Phone VARCHAR(15)
);

-- ================================
-- 3. ייבוא טבלאות (classes, courses, lecturers, students_temp, study_hours_extended)
-- מתבצע דרך phpMyAdmin - אין SQL
-- ================================


-- ================================
-- 4. יצירת טבלה study_hours לכיתות 1-5
-- ================================
CREATE TABLE study_hours AS
SELECT *
FROM study_hours_extended
WHERE classId IN (1, 2, 3, 4, 5);

-- ================================
-- 5. הוספת עמודה Email לטבלה lecturers
-- ================================
ALTER TABLE lecturers
ADD Email VARCHAR(70) NOT NULL;

-- ================================
-- 6. שינוי העמודה FullName ל-VARCHAR(80) NOT NULL
-- ================================
ALTER TABLE lecturers
MODIFY FullName VARCHAR(80) NOT NULL;

-- ================================
-- 7. הסרת העמודה status מטבלת classes
-- ================================
ALTER TABLE classes
DROP COLUMN status;

-- ================================
-- 8. מחיקת הטבלה teachers_backup
-- ================================
DROP TABLE teachers_backup;

-- ================================
-- 9. יצירת טבלה students מבוססת על students_temp
-- ================================
CREATE TABLE students AS
SELECT *
FROM students_temp;

-- ================================
-- 10. הסרת עמודת personalId
-- ================================
ALTER TABLE students
DROP COLUMN personalId;

-- ================================
-- 11. הוספת עמודת age מסוג מספר קטן
-- ================================
ALTER TABLE students
ADD age TINYINT;

-- ================================
-- 12. מחיקת תלמידים שנולדו לפני 01/01/1992
-- ================================
DELETE FROM students
WHERE BirthDate < '1992-01-01';

-- ================================
-- 13. הוספת CHECK על BirthDate בין 1992 ל-2000
-- ================================
ALTER TABLE students
MODIFY BirthDate DATE
CHECK (BirthDate BETWEEN '1992-01-01' AND '2000-12-31');

-- ================================
-- 14. מחיקת טבלה students_temp
-- ================================
DROP TABLE students_temp;      






UPDATE students
SET BirthDate = CONCAT(
    SUBSTRING(BirthDate, 7, 4), '-',   
    SUBSTRING(BirthDate, 4, 2), '-',   
    SUBSTRING(BirthDate, 1, 2)      
)
WHERE BirthDate LIKE '__/__/____';
