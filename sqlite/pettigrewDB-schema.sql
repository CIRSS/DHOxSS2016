CREATE TABLE letters (
       verbatimIndexInfo TEXT,
       box 		 TEXT,
       folder 		 TEXT,
       senderName 	 TEXT,
       notes 		 TEXT,
       recipient	 TEXT,
       letter		 TEXT,
       untaggedLetter	 TEXT,
       organization 	 TEXT,
       location		 TEXT,
       artifact		 TEXT,
       person		 TEXT,
       longWords	 TEXT,
       letterLength	 TEXT );


CREATE TABLE pgindex (
       boxNumber     INT DEFAULT (null),
       folderNumber  TEXT,
       senderName    TEXT,
       recpientName  TEXT,
       date	     TEXT,
       isoDate	     TEXT );
