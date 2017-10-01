DROP SCHEMA if exists snap_jobs CASCADE;

CREATE SCHEMA snap_jobs;

CREATE TABLE snap_jobs."Jobs"
(
    job_id BIGSERIAL PRIMARY KEY,
    job_title character varying(150),
    category character varying(100),
    status character varying(100),
    location character varying(100),
    CONSTRAINT job_constraint UNIQUE (job_title, category, status, location)
)
