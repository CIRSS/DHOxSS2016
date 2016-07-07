-- Explore and profile the pgindex data:

-- List all box numbers in reverse order: 
-- There are 13 of them.
-- Note: data type was set to INT (integer) in the database schema

SELECT DISTINCT boxNumber
FROM pgindex
ORDER BY boxNumber DESC;

-- List all folder numbers in reverse order:
-- There are 94 of them.
-- Note: data type was set (by default) to TEXT
-- => What's the problem?

SELECT DISTINCT folderNumber
FROM pgindex
ORDER BY folderNumber DESC;

-- after change folderNumber from TEXT to INT (note the manual edits in the log file!)
-- we now get a "proper" list of folder numbers in reverse order (94 of them)

/* When editing the column, SQLite warns you about the possible consequences.
   Here is what's it is doing. It works fine here. One result value is NOT an integer (color coded) => hand-edit

Are you sure you want to perform the following operation(s):
Alter Column boxNumber in table pgindex
SQL:
ALTER TABLE "main"."pgindex" RENAME TO "oXHFcGcd04oXHFcGcd04_pgindex"
CREATE TABLE "main"."pgindex" ("boxNumber" INT DEFAULT (null) ,"folderNumber" ,"senderName" ,"recpientName" ,"date" ,"isoDate" )
INSERT INTO "main"."pgindex" SELECT "boxNumber","folderNumber","senderName","recpientName","date","isoDate" FROM "main"."oXHFcGcd04oXHFcGcd04_pgindex"
DROP TABLE "main"."oXHFcGcd04oXHFcGcd04_pgindex"

*/

-- At first sight, it looks as if each folder is associated with one box.
-- Is this always the case? Maybe it's an integrity constraints.
-- Let's test it: How many boxes are there per folder ? 

SELECT folderNumber, COUNT (boxNumber) as boxCount
FROM    pgindex 
GROUP BY folderNumber 
ORDER BY boxCount DESC;

SELECT folderNumber, COUNT (DISTINCT boxNumber) as boxCount
FROM    pgindex 
GROUP BY folderNumber 
ORDER BY boxCount DESC;




SELECT MIN(folderNumber) + 1
FROM   pgindex PGo
WHERE  NOT EXISTS
        (
        SELECT  NULL
        FROM    pgindex PGi 
        WHERE   PGi.folderNumber = PGo.folderNumber + 1
        )



SELECT senderName, count (*) 
FROM pgindex I
-- WHERE L.senderName = I.senderName
GROUP BY senderName
ORDER BY COUNT(*) DESC



- 
SELECT L.senderName, count (*) 
FROM letters L, pgindex I
WHERE L.senderName = I.senderName
GROUP BY L.senderName
ORDER BY COUNT(*) DESC ;

