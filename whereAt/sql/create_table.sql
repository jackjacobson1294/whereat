USE whereAtdb;

CREATE TABLE Events(
eventID int AUTO_INCREMENT,
eventName varchar(20), 
time DATETIME, 
eventCreator varchar(256),
PRIMARY KEY(eventID));

CREATE TABLE UserAccess(
eventID int AUTO_INCREMENT,
eventCreator varchar(256),
RSVP int,
Availability DATETIME,
PRIMARY KEY (eventID),
FOREIGN KEY (eventID) REFERENCES Events(eventID)

);















