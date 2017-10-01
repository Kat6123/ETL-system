DROP SCHEMA if exists hello CASCADE;

CREATE SCHEMA hello;

CREATE TABLE hello."Jobs"
(
    job_id BIGSERIAL PRIMARY KEY,
    job_title character varying(150),
    category character varying(100),
    status character varying(100),
    location character varying(100),
    CONSTRAINT job_constraint UNIQUE (job_title, category, status, location)
)
