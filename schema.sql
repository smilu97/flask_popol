drop table if exists html_posts;
drop table if exists css_posts;
drop table if exists piano_posts;
drop table if exists musicetc_posts;
drop table if exists reversing_posts;

create table html_posts(
	id integer primary key autoincrement,
	title string not null,
	content string not null
);
create table css_posts(
	id integer primary key autoincrement,
	title string not null,
	content string not null
);	
create table piano_posts(
	id integer primary key autoincrement,
	title string not null,
	content string not null
);
create table musicetc_posts(
	id integer primary key autoincrement,
	title string not null,
	content string not null
);
create table reversing_posts(
	id integer primary key autoincrement,
	title string not null,
	content string not null
);