create database if not exists snowpark_demo;

use database snowpark_demo;
use schema public;

create stage if not exists snowpark_demo.public.stage;
