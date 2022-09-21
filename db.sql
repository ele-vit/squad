--
-- PostgreSQL database dump
--

-- Dumped from database version 14.5 (Ubuntu 14.5-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.5 (Ubuntu 14.5-0ubuntu0.22.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: jokes; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.jokes (
    id character(36),
    joke character varying(100)
);


ALTER TABLE public.jokes OWNER TO admin;

--
-- Data for Name: jokes; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.jokes (id, joke) FROM stdin;
\.


--
-- PostgreSQL database dump complete
--

