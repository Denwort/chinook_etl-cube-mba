Create DataBase Chinook_STAGE
Go

Set dateformat ymd
go
Use Chinook_STAGE
go

CREATE TABLE STG_Customer (
    id_customer integer not null primary key,
    FirstName NVARCHAR(40),
    LastName NVARCHAR(20),
    Address NVARCHAR(70),
    City NVARCHAR(40),
    Country NVARCHAR(40)
);

CREATE TABLE STG_Employee (
    id_employee integer not null primary key,
    FirstName NVARCHAR(20),
    LastName NVARCHAR(20),
    Title NVARCHAR(30),
    BirthDate DATE,
    HireDate DATE,
    Address NVARCHAR(70),
    City NVARCHAR(40),
    Country NVARCHAR(40)
);

CREATE TABLE STG_Invoice (
    id_invoice integer not null primary key,
    BillingAddress NVARCHAR(70),
    BillingCity NVARCHAR(40),
    BillingCountry NVARCHAR(40)
);

CREATE TABLE STG_Artist (
    id_artist integer not null primary key,
    Name NVARCHAR(120),
    Listeners NVARCHAR(10),
    Scroobies NVARCHAR(10)
);

CREATE TABLE Source2Artist (
    Id_Artist integer not null primary key,
    Name NVARCHAR(120),
    Listeners NVARCHAR(10),
    Scroobies NVARCHAR(10)
);


CREATE TABLE STG_Album (
    id_album integer not null primary key,
    Title NVARCHAR(160)
);

CREATE TABLE STG_Mediatype (
    id_mediatype integer not null primary key,
    Name NVARCHAR(120)
);

CREATE TABLE STG_Genre (
    id_genre integer identity(1,1) primary key,
    Name NVARCHAR(120),
    ParentGenre NVARCHAR(50),
    Description TEXT,
    RelatedGenre NVARCHAR(50),
    PopularArtist NVARCHAR(150)
);

CREATE TABLE Source3Genre (
    id integer identity(1,1) primary key,
    Name NVARCHAR(120),
    ParentGenre NVARCHAR(50),
    Description TEXT,
    RelatedGenre NVARCHAR(50),
    PopularArtist NVARCHAR(150)
);

CREATE TABLE STG_Track (
    id_track integer identity(1,1) primary key,
    prev_id integer,
    Name NVARCHAR(200),
    id_album INT,
    id_mediatype INT,
    id_genre INT,
    Milliseconds INT,
    Bytes INT
);

CREATE TABLE STG_Fechas (
    id_date integer not null primary key,
    Fecha date, 
    Anio smallint,
    Semestre nvarchar(30),
    Trimestre nvarchar(30),
    Mes nvarchar(30),
    DiaSemana nvarchar(30),
    NumSemestreAnio smallint,
    NumTrimestreAnio smallint,
    NumMesAnio smallint,
    NumDiaSemana smallint,
    NumDiaMes smallint
);

CREATE TABLE STG_FactSales (
    id_sale integer identity(1,1) primary key,
    id_customer INT,
    id_employee INT,
    id_invoice INT,
    id_artist INT,
    id_track INT,
    id_date INT,
    UnitPrice NUMERIC(10,2),
    Quantity INT,
    Total NUMERIC(10,2)
);

CREATE TABLE STG_Stats (
    id_sale integer identity(1,1) primary key,
    explicit NVARCHAR(10),
    danceability NUMERIC(10,10),
    energy NUMERIC(10,10),
    key_value INT,
    loudness NUMERIC(10,10)
);