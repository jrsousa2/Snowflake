-- These cmds are run from snowsql (in cmd prompt)
--All commands and sample csv file in the video description--
create database SLEEKDATA;

create schema OMS;
create stage MY_STAGE;

create table MY_TABLE (
    ID int,
    Name varchar(100),
    Age int,
    Region varchar(10)
);

-- Run put command in SNOWSQL CLI
-- (transfers the file from local machine to a stage within snowflake)
-- compresses the raw file and uploads to snowflake
put file://D:/mydata.csv @MY_STAGE;

copy into MY_TABLE from @MY_STAGE/mydata.csv.gz;

select * from MY_TABLE;