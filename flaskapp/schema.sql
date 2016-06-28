drop table if exists user;
create table user (
    user_id integer primary key,
    first_name text not null,
    last_name text not null,
    profile_url text not null
);
