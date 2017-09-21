
create table train (
    id integer primary key,
    name text,
    type text,
    origin text,
    dest text
);

create table station (
    code text primary key,
    name text
);
