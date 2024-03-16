Create DataBase Chinook_MART
Go

Set dateformat ymd
go
Use Chinook_MART
go

CREATE TABLE Dim_Customer (
    id_customer integer not null primary key,
    firstName NVARCHAR(40),
    lastName NVARCHAR(20),
    adress NVARCHAR(70),
    city NVARCHAR(40),
    country NVARCHAR(40)
);

CREATE TABLE Dim_Employee (
    id_employee integer not null primary key,
    firstName NVARCHAR(20),
    lastName NVARCHAR(20),
    title NVARCHAR(30),
    birthDate DATE,
    hireDate DATE,
    address NVARCHAR(70),
    city NVARCHAR(40),
    country NVARCHAR(40)
);

CREATE TABLE Dim_Invoice (
    id_invoice integer not null primary key,
    billingAddress NVARCHAR(70),
    billingCity NVARCHAR(40),
    billingcountry NVARCHAR(40)
);

CREATE TABLE Dim_Artist (
    id_artist integer not null primary key,
    name NVARCHAR(120),
    listeners NVARCHAR(10),
    scroobies NVARCHAR(10)
);

CREATE TABLE Dim_Album (
    id_album integer not null primary key,
    title NVARCHAR(160)
);

CREATE TABLE Dim_MediaType (
    id_mediatype integer not null primary key,
    name NVARCHAR(120)
);

CREATE TABLE Dim_Genre (
    id_genre integer not null primary key,
    name NVARCHAR(120),
    parentGenre NVARCHAR(50),
    description TEXT,
    relatedGenre NVARCHAR(50),
    popularArtist NVARCHAR(150)
);

CREATE TABLE Dim_Track (
    id_track integer not null primary key,
    name NVARCHAR(200),
    id_album INT,
    id_mediatype INT,
    id_genre INT,
    milliseconds INT,
    bytes INT,
    FOREIGN KEY (id_album) REFERENCES Dim_Album(id_album),
    FOREIGN KEY (id_mediatype) REFERENCES Dim_Mediatype(id_mediatype),
    FOREIGN KEY (id_genre) REFERENCES Dim_Genre(id_genre)
);

CREATE TABLE Dim_Date (
    id_date integer not null primary key,
    dateValue date, 
    year smallint,
    semester nvarchar(30),
    quarter nvarchar(30),
    month nvarchar(30),
    dayOfTheWeek nvarchar(30),
    numSemester smallint,
    numQuarter smallint,
    numMonth smallint,
    numDayOfTheWeek smallint,
    numDay smallint
);

CREATE TABLE Fact_Sales (
    id_sale integer not null primary key,
    id_customer INT,
    id_employee INT,
    id_invoice INT,
    id_artist INT,
    id_track INT,
    id_date INT,
    unit_price NUMERIC(10,2),
    quantity INT,
    total NUMERIC(10,2),
    FOREIGN KEY (id_customer) REFERENCES Dim_Customer(id_customer),
    FOREIGN KEY (id_employee) REFERENCES Dim_Employee(id_employee),
    FOREIGN KEY (id_invoice) REFERENCES Dim_Invoice(id_invoice),
    FOREIGN KEY (id_artist) REFERENCES Dim_Artist(id_artist),
    FOREIGN KEY (id_track) REFERENCES Dim_Track(id_track),
    FOREIGN KEY (id_date) REFERENCES Dim_Date(id_date)
);
