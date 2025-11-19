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







/*******************************
 Phase 1: Database Design (DDL)
*******************************/
-- 1. Artists
CREATE TABLE Artists (
    artist_id INT PRIMARY KEY,
    name TEXT NOT NULL,
    country TEXT,
    formation_year INT
);

-- 2. Albums
CREATE TABLE Albums (
    album_id INT PRIMARY KEY,
    title TEXT NOT NULL,
    release_date DATE,
    artist_id INT,
    FOREIGN KEY (artist_id) REFERENCES Artists(artist_id)
);

-- 3. Songs
CREATE TABLE Songs (
    song_id INT PRIMARY KEY,
    title TEXT NOT NULL,
    duration_seconds INT CHECK(duration_seconds > 0),
    album_id INT,
    FOREIGN KEY (album_id) REFERENCES Albums(album_id)
);

-- 4. Users
CREATE TABLE Users (
    user_id INT PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    email TEXT NOT NULL,
    join_date DATE
);

-- 5. Playlists
CREATE TABLE Playlists (
    playlist_id INT PRIMARY KEY,
    user_id INT,
    name TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- 6. Playlist_Songs (Many-to-Many)
CREATE TABLE Playlist_Songs (
    playlist_id INT,
    song_id INT,
    PRIMARY KEY (playlist_id, song_id),
    FOREIGN KEY (playlist_id) REFERENCES Playlists(playlist_id),
    FOREIGN KEY (song_id) REFERENCES Songs(song_id)
);

/*******************************
 Phase 2: Data Population (DML)
*******************************/
-- 1. Artists
INSERT INTO Artists (artist_id, name, country, formation_year) VALUES 
(101, 'The Lumineers', 'USA', 2005), 
(102, 'Dua Lipa', 'UK', 2013), 
(103, 'A.R. Rahman', 'India', 1992), 
(104, 'No Album Artist', 'Canada', 2018),  
(105, 'Adele', 'UK', 2006), 
(106, 'Queen', 'UK', 1970);

-- 2. Albums
INSERT INTO Albums (album_id, title, release_date, artist_id) VALUES 
(201, 'Cleopatra', '2016-04-08', 101), 
(202, 'Future Nostalgia', '2020-03-27', 102), 
(203, 'Rahman Hits Vol. 1', '2005-01-01', 103), 
(204, 'Album With No Songs', '2022-11-15', 101),  
(205, '21', '2011-01-24', 105), 
(206, 'A Day at the Races', '1976-12-10', 106), 
(207, 'Empty Album', '2023-01-01', 105);

-- 3. Songs
INSERT INTO Songs (song_id, title, duration_seconds, album_id) VALUES 
(301, 'Ophelia', 160, 201), 
(302, 'Cleopatra', 240, 201), 
(303, 'Ho Hey', 163, 201), 
(304, 'Don''t Start Now', 183, 202), 
(305, 'Levitating', 203, 202), 
(306, 'New Rules', 200, 202), 
(307, 'Jai Ho', 305, 203), 
(308, 'Love in the Time of Madness', 255, 203), 
(309, 'Big Love', 220, 201), 
(310, 'One Day', 155, 202), 
(311, 'Bohemian Rhapsody', 354, 206), 
(312, 'Someone Like You', 285, 205), 
(313, 'Set Fire to the Rain', 241, 205), 
(314, 'Another one Bites the Dust', 214, 206), 
(315, 'Crazy Little Thing Called Love', 160, 206);

-- 4. Users
INSERT INTO Users (user_id, username, email, join_date) VALUES 
(401, 'MusicLover77', 'mlover@example.com', '2024-01-10'), 
(402, 'Chill_Vibes', 'chill@example.com', '2023-05-20'), 
(403, 'SQL_Master', 'sqlmaster@example.com', '2024-10-15');

-- 5. Playlists
INSERT INTO Playlists (playlist_id, user_id, name) VALUES 
(501, 401, 'Acoustic Roadtrip'), 
(502, 402, 'Morning Energy'), 
(503, 401, 'Bollywood Grooves'), 
(504, 403, 'Rock Classics');

-- 6. Playlist_Songs
INSERT INTO Playlist_Songs (playlist_id, song_id) VALUES 
(501, 301), 
(501, 302), 
(501, 309), 
(502, 304), 
(502, 305), 
(502, 306), 
(502, 312),  
(503, 307), 
(503, 308), 
(503, 313), 
(504, 311), 
(504, 314);

/*******************************
 Phase 3: CRUD & Schema Modification
*******************************/
-- 1. Add followers_count column
ALTER TABLE Artists ADD followers_count INT;

-- 2. Update followers_count
UPDATE Artists SET followers_count = 1500000 WHERE artist_id = 102;
UPDATE Artists SET followers_count = 500000 WHERE artist_id = 101;
UPDATE Artists SET followers_count = 200000 WHERE artist_id = 103;
UPDATE Artists SET followers_count = 100000 WHERE artist_id = 104;
UPDATE Artists SET followers_count = 1200000 WHERE artist_id = 105;
UPDATE Artists SET followers_count = 800000 WHERE artist_id = 106;

-- 3. Update username
UPDATE Users SET username = 'MusicFanatic77' WHERE user_id = 401;

-- 4. Delete album with no songs and its songs
DELETE FROM Songs WHERE album_id = 204;
DELETE FROM Albums WHERE album_id = 204;

/*******************************
 Phase 4: Data Retrieval & Analysis
*******************************/
-- 1. Select all song titles and durations
SELECT title, duration_seconds FROM Songs;

-- 2. Alias artist_id and name
SELECT artist_id AS ID, name AS Artist_Name FROM Artists;

-- 3. Artists formed before 2000
SELECT * FROM Artists WHERE formation_year < 2000;

-- 4. Songs longer than 200s OR with 'Love' in title
SELECT * FROM Songs WHERE duration_seconds > 200 OR title LIKE '%Love%';

-- 5. Artists NOT from USA AND followers > 1,000,000
SELECT * FROM Artists WHERE country <> 'USA' AND followers_count > 1000000;

-- 6. Songs with duration BETWEEN 150 and 250
SELECT * FROM Songs WHERE duration_seconds BETWEEN 150 AND 250;

-- 7. Users with username IN list
SELECT * FROM Users WHERE username IN ('MusicFanatic77','Chill_Vibes','SQL_Master');

-- 8. Aggregate functions
SELECT COUNT(*) AS Total_Songs FROM Songs;
SELECT MAX(duration_seconds) AS Longest_Song FROM Songs;
SELECT SUM(duration_seconds) AS Total_Album_Duration FROM Songs WHERE album_id = 201;
SELECT AVG(duration_seconds) AS Avg_Song_Duration FROM Songs;

/*******************************
 Phase 5: Relational Queries (Joins)
*******************************/
-- 1. Artist & Album (INNER JOIN)
SELECT a.name AS Artist_Name, al.title AS Album_Title
FROM Artists a
INNER JOIN Albums al ON a.artist_id = al.artist_id;

-- 2. Songs on Playlists (Many-to-Many)
SELECT s.title AS Song_Title, p.name AS Playlist_Name
FROM Songs s
INNER JOIN Playlist_Songs ps ON s.song_id = ps.song_id
INNER JOIN Playlists p ON ps.playlist_id = p.playlist_id;

-- 3A. Albums without Songs (LEFT JOIN)
SELECT al.title AS Album_Title
FROM Albums al
LEFT JOIN Songs s ON al.album_id = s.album_id
WHERE s.song_id IS NULL;

-- 3B. RIGHT JOIN explanation: Reversing tables gives same unmatched albums result

-- 4. Artists with No Albums (LEFT JOIN)
SELECT a.name AS Artist_Name
FROM Artists a
LEFT JOIN Albums al ON a.artist_id = al.artist_id
WHERE al.album_id IS NULL;

-- 5. Full relational query (songs > 300s from UK artists)
SELECT s.title AS Song_Title, al.title AS Album_Title, ar.name AS Artist_Name
FROM Songs s
INNER JOIN Albums al ON s.album_id = al.album_id
INNER JOIN Artists ar ON al.artist_id = ar.artist_id
WHERE s.duration_seconds > 300 AND ar.country = 'UK';
