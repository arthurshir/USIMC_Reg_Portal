--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.3
-- Dumped by pg_dump version 9.6.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: usimc
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE auth_group OWNER TO usimc;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: usimc
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_group_id_seq OWNER TO usimc;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: usimc
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: usimc
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE auth_group_permissions OWNER TO usimc;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: usimc
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_group_permissions_id_seq OWNER TO usimc;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: usimc
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: usimc
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE auth_permission OWNER TO usimc;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: usimc
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_permission_id_seq OWNER TO usimc;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: usimc
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: usimc
--

CREATE TABLE auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE auth_user OWNER TO usimc;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: usimc
--

CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE auth_user_groups OWNER TO usimc;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: usimc
--

CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_groups_id_seq OWNER TO usimc;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: usimc
--

ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: usimc
--

CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_id_seq OWNER TO usimc;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: usimc
--

ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: usimc
--

CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE auth_user_user_permissions OWNER TO usimc;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: usimc
--

CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_user_permissions_id_seq OWNER TO usimc;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: usimc
--

ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: usimc
--

CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE django_admin_log OWNER TO usimc;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: usimc
--

CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_admin_log_id_seq OWNER TO usimc;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: usimc
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: usimc
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE django_content_type OWNER TO usimc;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: usimc
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_content_type_id_seq OWNER TO usimc;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: usimc
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: usimc
--

CREATE TABLE django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE django_migrations OWNER TO usimc;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: usimc
--

CREATE SEQUENCE django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_migrations_id_seq OWNER TO usimc;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: usimc
--

ALTER SEQUENCE django_migrations_id_seq OWNED BY django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: usimc
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE django_session OWNER TO usimc;

--
-- Name: registration_site_charge; Type: TABLE; Schema: public; Owner: usimc
--

CREATE TABLE registration_site_charge (
    id integer NOT NULL,
    charge_id character varying(200) NOT NULL,
    charge_amount integer NOT NULL,
    charge_customer character varying(200) NOT NULL,
    charge_description character varying(500) NOT NULL,
    charge_failure_message character varying(500) NOT NULL,
    charge_paid boolean NOT NULL,
    charge_receipt_email character varying(500) NOT NULL,
    entry_id integer NOT NULL,
    usimc_user_id integer NOT NULL
);


ALTER TABLE registration_site_charge OWNER TO usimc;

--
-- Name: registration_site_charge_id_seq; Type: SEQUENCE; Schema: public; Owner: usimc
--

CREATE SEQUENCE registration_site_charge_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE registration_site_charge_id_seq OWNER TO usimc;

--
-- Name: registration_site_charge_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: usimc
--

ALTER SEQUENCE registration_site_charge_id_seq OWNED BY registration_site_charge.id;


--
-- Name: registration_site_ensemblemember; Type: TABLE; Schema: public; Owner: usimc
--

CREATE TABLE registration_site_ensemblemember (
    id integer NOT NULL,
    first_name character varying(200),
    last_name character varying(200),
    instrument character varying(200),
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    entry_id integer NOT NULL,
    day character varying(2),
    month character varying(2),
    year character varying(4)
);


ALTER TABLE registration_site_ensemblemember OWNER TO usimc;

--
-- Name: registration_site_ensemblemember_id_seq; Type: SEQUENCE; Schema: public; Owner: usimc
--

CREATE SEQUENCE registration_site_ensemblemember_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE registration_site_ensemblemember_id_seq OWNER TO usimc;

--
-- Name: registration_site_ensemblemember_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: usimc
--

ALTER SEQUENCE registration_site_ensemblemember_id_seq OWNED BY registration_site_ensemblemember.id;


--
-- Name: registration_site_entry; Type: TABLE; Schema: public; Owner: usimc
--

CREATE TABLE registration_site_entry (
    id integer NOT NULL,
    awards_applying_for character varying(20)[] NOT NULL,
    instrument_category character varying(100) NOT NULL,
    age_category character varying(1) NOT NULL,
    submitted boolean NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    usimc_user_id integer NOT NULL,
    lead_performer_id integer,
    teacher_id integer,
    parent_contact_id integer,
    is_not_international boolean NOT NULL,
    proof_of_age character varying(100),
    signature character varying(500)
);


ALTER TABLE registration_site_entry OWNER TO usimc;

--
-- Name: registration_site_entry_id_seq; Type: SEQUENCE; Schema: public; Owner: usimc
--

CREATE SEQUENCE registration_site_entry_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE registration_site_entry_id_seq OWNER TO usimc;

--
-- Name: registration_site_entry_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: usimc
--

ALTER SEQUENCE registration_site_entry_id_seq OWNED BY registration_site_entry.id;


--
-- Name: registration_site_parentcontact; Type: TABLE; Schema: public; Owner: usimc
--

CREATE TABLE registration_site_parentcontact (
    id integer NOT NULL,
    first_name character varying(200),
    last_name character varying(200),
    email character varying(200),
    phone_number character varying(200),
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL
);


ALTER TABLE registration_site_parentcontact OWNER TO usimc;

--
-- Name: registration_site_parentcontact_id_seq; Type: SEQUENCE; Schema: public; Owner: usimc
--

CREATE SEQUENCE registration_site_parentcontact_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE registration_site_parentcontact_id_seq OWNER TO usimc;

--
-- Name: registration_site_parentcontact_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: usimc
--

ALTER SEQUENCE registration_site_parentcontact_id_seq OWNED BY registration_site_parentcontact.id;


--
-- Name: registration_site_person; Type: TABLE; Schema: public; Owner: usimc
--

CREATE TABLE registration_site_person (
    id integer NOT NULL,
    first_name character varying(200),
    last_name character varying(200),
    instrument character varying(200),
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    address character varying(200),
    city character varying(200),
    country character varying(200),
    state character varying(200),
    zip_code character varying(200),
    day character varying(2),
    month character varying(2),
    year character varying(4)
);


ALTER TABLE registration_site_person OWNER TO usimc;

--
-- Name: registration_site_person_id_seq; Type: SEQUENCE; Schema: public; Owner: usimc
--

CREATE SEQUENCE registration_site_person_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE registration_site_person_id_seq OWNER TO usimc;

--
-- Name: registration_site_person_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: usimc
--

ALTER SEQUENCE registration_site_person_id_seq OWNED BY registration_site_person.id;


--
-- Name: registration_site_piece; Type: TABLE; Schema: public; Owner: usimc
--

CREATE TABLE registration_site_piece (
    id integer NOT NULL,
    title character varying(200),
    composer character varying(200),
    entry_id integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    movement character varying(200),
    opus character varying(200),
    youtube_link character varying(200),
    minutes character varying(6),
    seconds character varying(6)
);


ALTER TABLE registration_site_piece OWNER TO usimc;

--
-- Name: registration_site_piece_id_seq; Type: SEQUENCE; Schema: public; Owner: usimc
--

CREATE SEQUENCE registration_site_piece_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE registration_site_piece_id_seq OWNER TO usimc;

--
-- Name: registration_site_piece_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: usimc
--

ALTER SEQUENCE registration_site_piece_id_seq OWNED BY registration_site_piece.id;


--
-- Name: registration_site_teacher; Type: TABLE; Schema: public; Owner: usimc
--

CREATE TABLE registration_site_teacher (
    id integer NOT NULL,
    first_name character varying(200),
    last_name character varying(200),
    email character varying(200),
    cmtanc_code character varying(200),
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL
);


ALTER TABLE registration_site_teacher OWNER TO usimc;

--
-- Name: registration_site_teacher_id_seq; Type: SEQUENCE; Schema: public; Owner: usimc
--

CREATE SEQUENCE registration_site_teacher_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE registration_site_teacher_id_seq OWNER TO usimc;

--
-- Name: registration_site_teacher_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: usimc
--

ALTER SEQUENCE registration_site_teacher_id_seq OWNED BY registration_site_teacher.id;


--
-- Name: registration_site_usimcuser; Type: TABLE; Schema: public; Owner: usimc
--

CREATE TABLE registration_site_usimcuser (
    id integer NOT NULL,
    user_id integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    is_admin boolean NOT NULL
);


ALTER TABLE registration_site_usimcuser OWNER TO usimc;

--
-- Name: registration_site_usimcuser_id_seq; Type: SEQUENCE; Schema: public; Owner: usimc
--

CREATE SEQUENCE registration_site_usimcuser_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE registration_site_usimcuser_id_seq OWNER TO usimc;

--
-- Name: registration_site_usimcuser_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: usimc
--

ALTER SEQUENCE registration_site_usimcuser_id_seq OWNED BY registration_site_usimcuser.id;


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY django_migrations ALTER COLUMN id SET DEFAULT nextval('django_migrations_id_seq'::regclass);


--
-- Name: registration_site_charge id; Type: DEFAULT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY registration_site_charge ALTER COLUMN id SET DEFAULT nextval('registration_site_charge_id_seq'::regclass);


--
-- Name: registration_site_ensemblemember id; Type: DEFAULT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY registration_site_ensemblemember ALTER COLUMN id SET DEFAULT nextval('registration_site_ensemblemember_id_seq'::regclass);


--
-- Name: registration_site_entry id; Type: DEFAULT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY registration_site_entry ALTER COLUMN id SET DEFAULT nextval('registration_site_entry_id_seq'::regclass);


--
-- Name: registration_site_parentcontact id; Type: DEFAULT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY registration_site_parentcontact ALTER COLUMN id SET DEFAULT nextval('registration_site_parentcontact_id_seq'::regclass);


--
-- Name: registration_site_person id; Type: DEFAULT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY registration_site_person ALTER COLUMN id SET DEFAULT nextval('registration_site_person_id_seq'::regclass);


--
-- Name: registration_site_piece id; Type: DEFAULT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY registration_site_piece ALTER COLUMN id SET DEFAULT nextval('registration_site_piece_id_seq'::regclass);


--
-- Name: registration_site_teacher id; Type: DEFAULT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY registration_site_teacher ALTER COLUMN id SET DEFAULT nextval('registration_site_teacher_id_seq'::regclass);


--
-- Name: registration_site_usimcuser id; Type: DEFAULT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY registration_site_usimcuser ALTER COLUMN id SET DEFAULT nextval('registration_site_usimcuser_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: usimc
--

COPY auth_group (id, name) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: usimc
--

SELECT pg_catalog.setval('auth_group_id_seq', 1, false);


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: usimc
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: usimc
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 1, false);


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: usimc
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can add permission	2	add_permission
5	Can change permission	2	change_permission
6	Can delete permission	2	delete_permission
7	Can add user	3	add_user
8	Can change user	3	change_user
9	Can delete user	3	delete_user
10	Can add group	4	add_group
11	Can change group	4	change_group
12	Can delete group	4	delete_group
13	Can add content type	5	add_contenttype
14	Can change content type	5	change_contenttype
15	Can delete content type	5	delete_contenttype
16	Can add session	6	add_session
17	Can change session	6	change_session
18	Can delete session	6	delete_session
19	Can add usimc user	7	add_usimcuser
20	Can change usimc user	7	change_usimcuser
21	Can delete usimc user	7	delete_usimcuser
22	Can add entry	8	add_entry
23	Can change entry	8	change_entry
24	Can delete entry	8	delete_entry
25	Can add piece	9	add_piece
26	Can change piece	9	change_piece
27	Can delete piece	9	delete_piece
28	Can add person	10	add_person
29	Can change person	10	change_person
30	Can delete person	10	delete_person
31	Can add teacher	11	add_teacher
32	Can change teacher	11	change_teacher
33	Can delete teacher	11	delete_teacher
34	Can add ensemble member	12	add_ensemblemember
35	Can change ensemble member	12	change_ensemblemember
36	Can delete ensemble member	12	delete_ensemblemember
37	Can add parent contact	13	add_parentcontact
38	Can change parent contact	13	change_parentcontact
39	Can delete parent contact	13	delete_parentcontact
40	Can add charge	14	add_charge
41	Can change charge	14	change_charge
42	Can delete charge	14	delete_charge
\.


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: usimc
--

SELECT pg_catalog.setval('auth_permission_id_seq', 42, true);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: usimc
--

COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
4	pbkdf2_sha256$30000$9q3VjiV2FSmU$OYxzJjp7U5iDIPaKDpnxc56ZPx2JsaaFBAsQ7Xt7DSU=	2017-03-21 20:39:05.838354-07	f	arthur@gmail.com			arthur@gmail.com	f	t	2017-03-21 20:39:05.765193-07
5	pbkdf2_sha256$30000$6VigOjbISyEE$QWPnBqVMzKwaz4G0n3mhsQqgBH7lfQaQVGPtkC69mYs=	2017-03-21 20:57:45.360615-07	f	60@gmail.com			60@gmail.com	f	t	2017-03-21 20:57:45.300583-07
6	pbkdf2_sha256$30000$72x9zaGPT8dT$L4kPKKPBYf8fIame/2maZNfCOAwGBBRnDWKkbQQ7KEA=	2017-03-21 21:06:21.401784-07	f	example@gmail.com			example@gmail.com	f	t	2017-03-21 21:06:21.34683-07
3	pbkdf2_sha256$30000$G1Pw4UGTlDhA$G9VVS+9Q4kBqZALMfM9tDZpygEZ254VEhbLj/yanupE=	2017-03-28 05:45:52.674488-07	f	test@gmail.com			test@gmail.com	f	t	2017-03-19 23:23:44.20395-07
1	pbkdf2_sha256$30000$z7LEcHc672iR$bYlKfhpcKCKAubu6IrxlVS6DghwC99D+eqha1bbxyys=	2017-03-30 01:12:16.713052-07	f	roylkingarthur@gmail.com	Arthur	Shir	roylkingarthur@gmail.com	f	t	2017-03-09 00:07:15.751889-08
2	pbkdf2_sha256$30000$xfQZk5ScM0v0$AXP1QqA+epByedVgN9sZy+uA1akyTXvYq6s6AhYcbIc=	2017-04-04 22:45:23.309007-07	f	Arthur.shir@gmail.com			Arthur.shir@gmail.com	f	t	2017-03-17 22:34:13.983483-07
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: usimc
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: usimc
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: usimc
--

SELECT pg_catalog.setval('auth_user_id_seq', 6, true);


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: usimc
--

COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: usimc
--

SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: usimc
--

COPY django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: usimc
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 1, false);


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: usimc
--

COPY django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	user
4	auth	group
5	contenttypes	contenttype
6	sessions	session
7	registration_site	usimcuser
8	registration_site	entry
9	registration_site	piece
10	registration_site	person
11	registration_site	teacher
12	registration_site	ensemblemember
13	registration_site	parentcontact
14	registration_site	charge
\.


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: usimc
--

SELECT pg_catalog.setval('django_content_type_id_seq', 14, true);


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: usimc
--

COPY django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2017-03-08 00:36:19.512076-08
2	auth	0001_initial	2017-03-08 00:36:19.62056-08
3	admin	0001_initial	2017-03-08 00:36:19.664231-08
4	admin	0002_logentry_remove_auto_add	2017-03-08 00:36:19.685941-08
5	contenttypes	0002_remove_content_type_name	2017-03-08 00:36:19.738131-08
6	auth	0002_alter_permission_name_max_length	2017-03-08 00:36:19.757489-08
7	auth	0003_alter_user_email_max_length	2017-03-08 00:36:19.774821-08
8	auth	0004_alter_user_username_opts	2017-03-08 00:36:19.794743-08
9	auth	0005_alter_user_last_login_null	2017-03-08 00:36:19.814142-08
10	auth	0006_require_contenttypes_0002	2017-03-08 00:36:19.817111-08
11	auth	0007_alter_validators_add_error_messages	2017-03-08 00:36:19.838822-08
12	auth	0008_alter_user_username_max_length	2017-03-08 00:36:19.866299-08
13	registration_site	0001_initial	2017-03-08 00:36:19.977165-08
14	registration_site	0002_auto_20170226_1249	2017-03-08 00:36:20.048724-08
15	registration_site	0003_auto_20170226_1508	2017-03-08 00:36:20.252326-08
16	registration_site	0004_auto_20170226_1522	2017-03-08 00:36:20.293528-08
17	registration_site	0005_auto_20170226_1526	2017-03-08 00:36:20.463574-08
18	registration_site	0006_person_created_at	2017-03-08 00:36:20.514362-08
19	registration_site	0007_auto_20170228_1210	2017-03-08 00:36:20.75798-08
20	sessions	0001_initial	2017-03-08 00:36:20.780427-08
21	registration_site	0008_auto_20170308_0836	2017-03-08 00:36:30.711661-08
22	registration_site	0009_auto_20170309_0843	2017-03-09 00:43:42.274471-08
23	registration_site	0010_auto_20170309_0853	2017-03-09 00:53:23.431507-08
24	registration_site	0011_auto_20170309_0907	2017-03-09 01:07:54.961791-08
25	registration_site	0012_auto_20170312_0055	2017-03-11 16:55:40.876491-08
26	registration_site	0013_auto_20170312_0545	2017-03-11 21:45:46.309895-08
27	registration_site	0014_auto_20170312_0625	2017-03-11 22:25:15.026805-08
28	registration_site	0015_auto_20170312_0732	2017-03-11 23:32:27.390628-08
29	registration_site	0016_entry_is_international	2017-03-12 16:39:40.413329-07
30	registration_site	0017_auto_20170312_2356	2017-03-12 16:56:43.133035-07
31	registration_site	0018_auto_20170313_0225	2017-03-12 19:25:42.091997-07
32	registration_site	0019_auto_20170313_0227	2017-03-12 19:27:21.845407-07
33	registration_site	0020_auto_20170313_0247	2017-03-12 19:48:02.283487-07
34	registration_site	0021_auto_20170316_2313	2017-03-16 16:13:45.861191-07
35	registration_site	0022_auto_20170316_2342	2017-03-16 16:44:05.647793-07
36	registration_site	0023_auto_20170316_2344	2017-03-16 16:44:59.699381-07
37	registration_site	0024_auto_20170326_0312	2017-03-25 20:12:46.710152-07
38	registration_site	0025_charge	2017-03-26 02:08:12.577501-07
39	registration_site	0026_auto_20170326_0917	2017-03-26 02:17:29.292397-07
40	registration_site	0027_auto_20170326_0928	2017-03-26 02:28:17.885371-07
41	registration_site	0028_auto_20170326_1031	2017-03-26 03:31:34.557656-07
42	registration_site	0029_auto_20170328_0924	2017-03-28 02:24:38.900901-07
43	registration_site	0030_auto_20170329_0029	2017-03-28 17:29:44.737944-07
44	registration_site	0031_auto_20170331_0115	2017-03-30 18:15:17.822682-07
45	registration_site	0032_auto_20170331_0627	2017-03-30 23:27:38.982567-07
46	registration_site	0033_auto_20170331_0649	2017-03-30 23:50:01.126258-07
47	registration_site	0034_remove_teacher_phone_number	2017-03-31 03:16:31.681552-07
48	registration_site	0035_auto_20170331_1027	2017-03-31 03:27:48.338864-07
49	registration_site	0036_auto_20170331_1323	2017-03-31 06:23:55.171498-07
50	registration_site	0037_entry_signature	2017-04-04 00:05:37.491717-07
\.


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: usimc
--

SELECT pg_catalog.setval('django_migrations_id_seq', 50, true);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: usimc
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
tkk1wqu3moed85y86amnkuwr6f2r9fis	MDYxMWE3ZjMyZTQxYmVlY2IwMDkxMzJmYjA3ZGMyMGYyMTcyY2RkYzp7Il9hdXRoX3VzZXJfaGFzaCI6ImE0YzhjNzRkMDAwMWRkZDU5OTZmOGEyNjA0YmE3ZGI1ZjkyZTNmMWQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=	2017-04-16 22:50:07.132617-07
l8w6tfkt8pmq1l0m9tdmqjl3w61g80t2	YzI2OTVmMzQ4Nzg2YTNlZjAyYWFlMDllNWJiNzNkNGNhZTI4MTk1Zjp7Il9hdXRoX3VzZXJfaGFzaCI6IjhkMjBkYTkwN2FhMjA3OGJjYmI4ZDcyMmUwOWYxN2MzMzZmZTMyNzIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=	2017-04-18 22:45:23.313258-07
\.


--
-- Data for Name: registration_site_charge; Type: TABLE DATA; Schema: public; Owner: usimc
--

COPY registration_site_charge (id, charge_id, charge_amount, charge_customer, charge_description, charge_failure_message, charge_paid, charge_receipt_email, entry_id, usimc_user_id) FROM stdin;
25	ch_1A2yQ1GL55NcmcjHvP1T33ZV	20000		USIMC entry ID:97,  Category: Cello, Age Category: A, below 11 years old		t		97	1
26	ch_1A32DDGL55NcmcjHdwHLlLYN	20000		USIMC entry ID:102,  Category: Chamber Ensemble, Age Category: A, below 15 years old		t		102	2
27	ch_1A32EQGL55NcmcjHqchILgBT	30000		USIMC entry ID:103,  Category: Cello, Age Category: A, below 11 years old		t		103	2
28	ch_1A32FlGL55NcmcjHLlKoZyI9	30000		USIMC entry ID:104,  Category: Chamber Ensemble, Age Category: A, below 15 years old		t		104	2
29	ch_1A32IZGL55NcmcjHFZ9S9wiB	30000		USIMC entry ID:105,  Category: Chamber Ensemble, Age Category: A, below 15 years old		t		105	2
30	ch_1A32P7GL55NcmcjHRbvtjZzr	20000		USIMC entry ID:106,  Category: Chamber Ensemble, Age Category: B, below 30 years old		t		106	2
31	ch_1A32qOGL55NcmcjHbYk20rU9	20000		USIMC entry ID:107,  Category: Chamber Ensemble, Age Category: B, below 30 years old		t		107	2
32	ch_1A32tVGL55NcmcjHMlyBajFS	10000		USIMC entry ID:108,  Category: Cello, Age Category: B, below 14 years old		t		108	2
33	ch_1A331MGL55NcmcjHBSI2dpVt	10000		USIMC entry ID:109,  Category: Chinese Traditional Instruments Ensemble, Age Category: B, below 30 years old		t		109	2
34	ch_1A3NVjGL55NcmcjHOlEl3aao	20000		USIMC entry ID:119,  Category: Cello, Age Category: B, below 14 years old		t		119	1
35	ch_1A3VOGGL55NcmcjHQ8zewHOP	20000		USIMC entry ID:121,  Category: Plucked String - Chinese Traditional Instrument, Age Category: B, below 14 years old		t		121	1
36	ch_1A4mJVGL55NcmcjHaMYd8Buy	8000		USIMC entry ID:126,  Category: Chamber Ensemble, Age Category: B, below 30 years old		t		126	1
37	ch_1A571OGL55NcmcjHyZNO3MqN	10000		USIMC entry ID:99,  Category: Cello, Age Category: A, below 11 years old		t		99	2
38	ch_1A5756GL55NcmcjHi0rIego5	10000		USIMC entry ID:124,  Category: Chamber Ensemble, Age Category: B, below 30 years old		t		124	2
\.


--
-- Name: registration_site_charge_id_seq; Type: SEQUENCE SET; Schema: public; Owner: usimc
--

SELECT pg_catalog.setval('registration_site_charge_id_seq', 38, true);


--
-- Data for Name: registration_site_ensemblemember; Type: TABLE DATA; Schema: public; Owner: usimc
--

COPY registration_site_ensemblemember (id, first_name, last_name, instrument, created_at, updated_at, entry_id, day, month, year) FROM stdin;
54	Arthur	Shir	sd	2017-03-30 02:57:37.507877-07	2017-03-30 02:59:59.857776-07	100	\N	\N	\N
55	\N	\N	\N	2017-03-30 03:01:11.790927-07	2017-03-30 03:01:11.791244-07	101	\N	\N	\N
56	Arthur	Shir	sdf	2017-03-30 05:16:21.81569-07	2017-03-30 05:16:43.96522-07	102	\N	\N	\N
57	Arthur	Shir	pdf	2017-03-30 05:19:03.414317-07	2017-03-30 05:19:41.658112-07	104	\N	\N	\N
58	sdfd	sdfd	pdf	2017-03-30 05:19:41.619111-07	2017-03-30 05:19:41.660337-07	104	\N	\N	\N
59	Devin	Choi	Cello	2017-03-30 05:21:38.755902-07	2017-03-30 05:22:35.994765-07	105	\N	\N	\N
60	Frank	Chen	Cello	2017-03-30 05:22:35.85581-07	2017-03-30 05:22:36.00319-07	105	\N	\N	\N
61	Arthur	Shir	sdf	2017-03-30 05:25:35.10497-07	2017-03-30 05:29:22.679545-07	106	\N	\N	\N
62	Arthur	Shir	pdf	2017-03-30 05:41:48.807313-07	2017-03-30 05:42:13.983562-07	107	\N	\N	\N
63	Arthur	Shir	sdf	2017-03-30 06:08:23.826988-07	2017-03-30 06:08:41.258072-07	109	\N	\N	\N
64	\N	\N	\N	2017-03-30 06:09:50.622951-07	2017-03-30 06:09:50.623312-07	110	\N	\N	\N
119	lkj	lkj	lkjs	2017-03-31 13:23:04.051181-07	2017-04-02 05:47:23.234073-07	122	1	1	2010
122	lklj	lkj	lkj	2017-04-02 23:50:41.097416-07	2017-04-04 00:30:27.805856-07	126	09	09	2010
121	lkj	lkj	lkj	2017-04-02 22:50:23.014128-07	2017-04-04 22:52:58.461388-07	124	28	02	1993
120	lkj	lkj	lkj	2017-04-02 22:23:41.442302-07	2017-04-02 23:18:22.76806-07	123	28	02	1993
\.


--
-- Name: registration_site_ensemblemember_id_seq; Type: SEQUENCE SET; Schema: public; Owner: usimc
--

SELECT pg_catalog.setval('registration_site_ensemblemember_id_seq', 122, true);


--
-- Data for Name: registration_site_entry; Type: TABLE DATA; Schema: public; Owner: usimc
--

COPY registration_site_entry (id, awards_applying_for, instrument_category, age_category, submitted, created_at, updated_at, usimc_user_id, lead_performer_id, teacher_id, parent_contact_id, is_not_international, proof_of_age, signature) FROM stdin;
122	{young_artist_award}	chamber_ensemble	A	f	2017-03-31 13:23:04.030276-07	2017-04-02 05:47:23.202807-07	1	128	128	118	t		\N
109	{young_artist_award}	chinese_traditional_instruments_ensemble	B	t	2017-03-30 06:08:23.80721-07	2017-03-30 06:09:03.072094-07	2	115	115	105	t		\N
110	{young_artist_award,special_theme_bach}	chamber_ensemble	B	f	2017-03-30 06:09:50.604896-07	2017-03-30 06:09:50.619532-07	2	116	116	106	t		\N
119	{young_artist_award,special_theme_bach}	cello	B	t	2017-03-31 03:14:53.879219-07	2017-03-31 04:02:17.148612-07	1	125	125	115	t		\N
123	{young_artist_award}	chamber_ensemble	B	f	2017-04-02 22:23:41.422961-07	2017-04-02 23:18:22.733842-07	1	129	129	119	t		\N
99	{young_artist_award}	cello	A	t	2017-03-30 02:57:26.276527-07	2017-04-04 22:49:36.519359-07	2	105	105	95	t		Arthur Abraham Shir
124	{young_artist_award}	chamber_ensemble	B	t	2017-04-02 22:50:22.992612-07	2017-04-04 22:53:26.278066-07	2	130	130	120	t		Arthur Abraham Shir
107	{young_artist_award,special_theme_bach}	chamber_ensemble	B	t	2017-03-30 05:41:48.788433-07	2017-03-30 05:57:43.359177-07	2	113	113	103	t		\N
121	{young_artist_award,special_theme_bach}	chinese_traditional_instrument_plucked_string	B	t	2017-03-31 12:23:40.188257-07	2017-03-31 12:26:29.669029-07	1	127	127	117	t		\N
97	{young_artist_award,special_theme_bach}	cello	A	t	2017-03-30 01:13:18.318263-07	2017-03-30 01:14:11.853956-07	1	103	103	93	t		\N
127	{special_theme_bach}	cello	B	f	2017-04-04 23:15:56.188376-07	2017-04-04 23:15:56.202989-07	2	133	133	123	t		\N
100	{young_artist_award}	chamber_ensemble	A	f	2017-03-30 02:57:37.49219-07	2017-03-30 02:59:59.704666-07	2	106	106	96	t		\N
101	{young_artist_award,special_theme_bach}	chamber_ensemble	A	f	2017-03-30 03:01:11.774439-07	2017-03-30 03:01:11.787682-07	2	107	107	97	t		\N
126	{young_artist_award}	chamber_ensemble	B	t	2017-04-02 23:50:41.079688-07	2017-04-04 00:42:56.183869-07	1	132	132	122	t		Arthur Abraham Shir
102	{young_artist_award,special_theme_bach}	chamber_ensemble	A	t	2017-03-30 05:16:21.793279-07	2017-03-30 05:17:29.619544-07	2	108	108	98	t		\N
125	{young_artist_award}	chinese_traditional_instrument_bowed_strings	C	f	2017-04-02 23:45:56.157812-07	2017-04-04 00:45:38.059658-07	1	131	131	121	t		\N
103	{young_artist_award,special_theme_bach,chinese_music_award}	cello	A	t	2017-03-30 05:17:38.378863-07	2017-03-30 05:18:30.696228-07	2	109	109	99	t		\N
108	{young_artist_award}	cello	B	t	2017-03-30 05:59:43.459797-07	2017-03-30 06:00:56.000171-07	2	114	114	104	t		\N
104	{young_artist_award,special_theme_bach}	chamber_ensemble	A	t	2017-03-30 05:19:03.397519-07	2017-03-30 05:19:51.899477-07	2	110	110	100	t		\N
105	{young_artist_award,special_theme_bach}	chamber_ensemble	A	t	2017-03-30 05:21:38.736558-07	2017-03-30 05:22:46.198773-07	2	111	111	101	t		\N
106	{young_artist_award,special_theme_bach}	chamber_ensemble	B	t	2017-03-30 05:25:35.085418-07	2017-03-30 05:29:32.93247-07	2	112	112	102	t		\N
\.


--
-- Name: registration_site_entry_id_seq; Type: SEQUENCE SET; Schema: public; Owner: usimc
--

SELECT pg_catalog.setval('registration_site_entry_id_seq', 127, true);


--
-- Data for Name: registration_site_parentcontact; Type: TABLE DATA; Schema: public; Owner: usimc
--

COPY registration_site_parentcontact (id, first_name, last_name, email, phone_number, created_at, updated_at) FROM stdin;
34	\N	\N	\N	\N	2017-03-16 17:32:05.418826-07	2017-03-16 17:32:05.419186-07
35	\N	\N	\N	\N	2017-03-17 15:49:52.144866-07	2017-03-17 15:49:52.145109-07
50	\N	\N	\N	\N	2017-03-21 01:19:26.83813-07	2017-03-21 01:19:26.838459-07
51	\N	\N	\N	\N	2017-03-21 01:19:37.581802-07	2017-03-21 01:19:37.582054-07
52					2017-03-21 01:20:57.336602-07	2017-03-21 01:21:25.639057-07
53	\N	\N	\N	\N	2017-03-21 03:15:50.67071-07	2017-03-21 03:15:50.670999-07
54	\N	\N	\N	\N	2017-03-21 03:18:53.873608-07	2017-03-21 03:18:53.873861-07
55	\N	\N	\N	\N	2017-03-21 03:29:49.897487-07	2017-03-21 03:29:49.897753-07
56	\N	\N	\N	\N	2017-03-21 04:47:54.529738-07	2017-03-21 04:47:54.530045-07
57	\N	\N	\N	\N	2017-03-21 19:29:38.183684-07	2017-03-21 19:29:38.184004-07
58	\N	\N	\N	\N	2017-03-21 20:12:02.077751-07	2017-03-21 20:12:02.078071-07
59					2017-03-21 20:26:15.165371-07	2017-03-21 20:27:22.341527-07
60	Ling	Lee	LingLshir@gmail.com	5102199877	2017-03-21 20:45:40.442185-07	2017-03-21 20:45:50.696228-07
61					2017-03-21 20:51:44.554126-07	2017-03-21 20:51:47.214192-07
62	\N	\N	\N	\N	2017-03-21 20:58:17.802255-07	2017-03-21 20:58:17.802601-07
63					2017-03-21 21:07:51.846666-07	2017-03-21 21:07:54.938084-07
103	Arthur	Shir	arthur.shir@gmail.com	5107709877	2017-03-30 05:41:48.799796-07	2017-03-30 05:42:13.9665-07
69			Arthur.shir@gmail.com		2017-03-25 20:18:08.595542-07	2017-03-26 03:02:11.368803-07
79	\N	\N	\N	\N	2017-03-28 05:14:30.794839-07	2017-03-28 05:14:30.795068-07
104	Arthur	Shir	arthur.shir@gmail.com	5107709877	2017-03-30 05:59:43.469477-07	2017-03-30 06:00:34.544883-07
78	Arthur	Shir	test@gmail.com	5106768998	2017-03-28 04:46:47.973492-07	2017-03-28 05:18:45.859364-07
80	\N	\N	\N	\N	2017-03-28 05:21:17.272105-07	2017-03-28 05:21:17.272353-07
81	\N	\N	\N	\N	2017-03-28 05:46:03.020952-07	2017-03-28 05:46:03.021242-07
82	\N	\N	\N	\N	2017-03-28 05:46:30.273631-07	2017-03-28 05:46:30.273875-07
33	Ling Lee	Shir	LingLshir@gmail.com	5102199877	2017-03-16 16:45:19.749643-07	2017-03-17 17:38:22.849216-07
36	\N	\N	\N	\N	2017-03-17 21:52:49.925819-07	2017-03-17 21:52:49.926102-07
83	Arthur	Shir	Arthur.shir@gmail.com	5106768998	2017-03-28 15:21:14.345399-07	2017-03-28 15:23:54.411458-07
84	\N	\N	\N	\N	2017-03-28 15:27:04.905256-07	2017-03-28 15:27:04.905478-07
85	\N	\N	\N	\N	2017-03-28 16:48:15.054639-07	2017-03-28 16:48:15.05533-07
86	\N	\N	\N	\N	2017-03-28 16:48:23.276522-07	2017-03-28 16:48:23.276739-07
87	\N	\N	\N	\N	2017-03-28 16:54:21.508501-07	2017-03-28 16:54:21.508761-07
105	Arthur	Shir	arthur.shir@gmail.com	5107709877	2017-03-30 06:08:23.819798-07	2017-03-30 06:08:41.22821-07
106	\N	\N	\N	\N	2017-03-30 06:09:50.61455-07	2017-03-30 06:09:50.6149-07
107	\N	\N	\N	\N	2017-03-30 16:49:49.346219-07	2017-03-30 16:49:49.34656-07
38					2017-03-17 22:34:21.788852-07	2017-03-17 22:36:04.234353-07
37					2017-03-17 22:23:17.500724-07	2017-03-17 23:45:13.643568-07
39					2017-03-17 23:45:31.1367-07	2017-03-18 15:00:15.942566-07
40	\N	\N	\N	\N	2017-03-18 15:00:44.110296-07	2017-03-18 15:00:44.110699-07
41	\N	\N	\N	\N	2017-03-18 15:08:37.165744-07	2017-03-18 15:08:37.16623-07
42	Arthur	Shir	Arthur.shir@gmail.com	5106768998	2017-03-19 23:05:00.576616-07	2017-03-19 23:05:42.112752-07
43	\N	\N	\N	\N	2017-03-19 23:06:00.918875-07	2017-03-19 23:06:00.919131-07
44					2017-03-19 23:08:05.185252-07	2017-03-19 23:14:35.66903-07
45	test				2017-03-19 23:14:44.35319-07	2017-03-19 23:15:02.318494-07
46	\N	\N	\N	\N	2017-03-19 23:19:45.824472-07	2017-03-19 23:19:45.82479-07
48	\N	\N	\N	\N	2017-03-20 23:15:16.737335-07	2017-03-20 23:15:16.737659-07
88	Arthur	Shir	Arthur.shir@gmail.com	5106768998	2017-03-28 17:23:33.241171-07	2017-03-28 18:12:23.877961-07
89	\N	\N	\N	\N	2017-03-29 19:43:59.703801-07	2017-03-29 19:43:59.704091-07
49	\N	\N	\N	\N	2017-03-21 00:05:05.918576-07	2017-03-21 00:05:05.918895-07
47					2017-03-19 23:29:45.072101-07	2017-03-21 00:06:21.717408-07
90	\N	\N	\N	\N	2017-03-29 19:44:13.835623-07	2017-03-29 19:44:13.835866-07
91	Arthur	Shir	Arthur.shir@gmail.com	5106768998	2017-03-29 20:28:29.226177-07	2017-03-29 20:29:05.757372-07
92	\N	\N	\N	\N	2017-03-30 01:07:04.832306-07	2017-03-30 01:07:04.832634-07
68					2017-03-25 20:06:58.83557-07	2017-03-26 03:31:53.231462-07
66					2017-03-25 18:54:49.55204-07	2017-03-25 20:49:20.398323-07
70					2017-03-26 00:50:36.263778-07	2017-03-26 00:50:38.512188-07
71			Arthur.shir@gmail.com		2017-03-26 03:34:34.339507-07	2017-03-26 03:34:41.674811-07
64					2017-03-21 21:08:46.262152-07	2017-03-26 01:53:39.304392-07
65					2017-03-25 18:54:32.959488-07	2017-03-26 01:53:44.902696-07
67			Arthur.shir@gmail.com		2017-03-25 19:04:22.97778-07	2017-03-26 02:51:06.404846-07
93	Arthur	Shir	Arthur.shir@gmail.com	5106768998	2017-03-30 01:13:18.332951-07	2017-03-30 01:14:00.339558-07
72			Arthur.shir@gmail.com		2017-03-26 03:35:41.311977-07	2017-03-26 03:35:46.197575-07
73			Arthur.shir@gmail.com		2017-03-26 03:40:33.495867-07	2017-03-26 03:40:38.604788-07
74	\N	\N	\N	\N	2017-03-27 03:01:54.783478-07	2017-03-27 03:01:54.783751-07
75	\N	\N	\N	\N	2017-03-28 02:24:23.017477-07	2017-03-28 02:24:23.017786-07
76	\N	\N	\N	\N	2017-03-28 02:24:40.465137-07	2017-03-28 02:24:40.465379-07
77	\N	\N	\N	\N	2017-03-28 02:29:25.046012-07	2017-03-28 02:29:25.046371-07
96	Arthur	Shir	arthur.shir@gmail.com	5107709877	2017-03-30 02:57:37.500428-07	2017-03-30 02:59:59.838461-07
97	\N	\N	\N	\N	2017-03-30 03:01:11.783295-07	2017-03-30 03:01:11.783532-07
98	Arthur	Shir	arthur.shir@gmail.com	5107709877	2017-03-30 05:16:21.807236-07	2017-03-30 05:16:43.955216-07
99	Arthur	Shir	arthur.shir@gmail.com	5107709877	2017-03-30 05:17:38.390063-07	2017-03-30 05:17:57.767203-07
100	Arthur	Shir	arthur.shir@gmail.com	5107709877	2017-03-30 05:19:03.406515-07	2017-03-30 05:19:41.646498-07
101	Arthur	Shir	arthur.shir@gmail.com	5107709877	2017-03-30 05:21:38.748439-07	2017-03-30 05:22:35.972861-07
102	Arthur	Shir	arthur.shir@gmail.com	5107709877	2017-03-30 05:25:35.09744-07	2017-03-30 05:29:22.663257-07
109	Ar	Shir	Arthur.shir@gmail.com	5106768998	2017-03-30 17:01:26.756207-07	2017-03-30 18:03:08.972812-07
111	slkdjf	lk	Arthur.shir@gmail.com	5106768998	2017-03-30 18:15:58.500997-07	2017-03-30 18:17:56.860928-07
112	\N	\N	\N	\N	2017-03-30 23:07:31.327055-07	2017-03-30 23:07:31.32735-07
116	Ling	Lee	Arthur.shir@gmail.com	5106768998	2017-03-31 04:20:48.281378-07	2017-03-31 13:22:28.774932-07
95	lkjsd	lkj	Arthur.shir@gmail.com	5106768998	2017-03-30 02:57:26.286918-07	2017-04-04 22:49:01.292858-07
114	Ling	Lee	\N	\N	2017-03-31 01:47:41.791667-07	2017-03-31 12:21:54.813602-07
120	lkj	lkj	Arthur.shir@gmail.com	lkj	2017-04-02 22:50:23.006128-07	2017-04-04 22:52:58.450114-07
115	Arthur	Shir	Arthur.shir@gmail.com	5106768998	2017-03-31 03:14:53.891785-07	2017-03-31 04:00:59.761433-07
123	\N	\N	\N	\N	2017-04-04 23:15:56.198691-07	2017-04-04 23:15:56.19898-07
110	Arthu	\N	Arthur.shir@gmail.com	\N	2017-03-30 18:04:34.324928-07	2017-03-31 04:08:16.398024-07
108	Arthur	Shir	Arthur.shir@gmail.com	\N	2017-03-30 16:50:44.148052-07	2017-03-31 04:08:49.795928-07
117	Ling	Lee	Arthur.shir@gmail.com	5106768998	2017-03-31 12:23:40.199202-07	2017-03-31 12:25:55.855469-07
118	Arthur	Shir	Arthur.shir@gmail.com	5106768998	2017-03-31 13:23:04.042112-07	2017-04-02 05:47:23.214116-07
113	\N	\N	\N	\N	2017-03-31 01:11:08.46492-07	2017-03-31 01:47:31.93159-07
122	ljk	lkj	Arthur.shir@gmail.com	5106768998	2017-04-02 23:50:41.089743-07	2017-04-04 00:30:27.785706-07
94	sdf	\N	\N	\N	2017-03-30 01:31:09.699328-07	2017-03-31 04:13:48.912004-07
119	k	jlkj	Arthur.shir@gmail.com	5106768998	2017-04-02 22:23:41.434053-07	2017-04-02 23:18:22.742851-07
121	lkj	lkjlk	Arthur.shir@gmail.com	jkl	2017-04-02 23:45:56.170801-07	2017-04-04 00:45:38.067954-07
\.


--
-- Name: registration_site_parentcontact_id_seq; Type: SEQUENCE SET; Schema: public; Owner: usimc
--

SELECT pg_catalog.setval('registration_site_parentcontact_id_seq', 123, true);


--
-- Data for Name: registration_site_person; Type: TABLE DATA; Schema: public; Owner: usimc
--

COPY registration_site_person (id, first_name, last_name, instrument, created_at, updated_at, address, city, country, state, zip_code, day, month, year) FROM stdin;
1	\N	\N	\N	2017-03-09 00:12:43.95655-08	2017-03-09 00:12:43.956912-08	\N	\N	\N	\N	\N	\N	\N	\N
2	\N	\N	\N	2017-03-09 00:12:56.133784-08	2017-03-09 00:12:56.134071-08	\N	\N	\N	\N	\N	\N	\N	\N
3	\N	\N	\N	2017-03-09 00:13:06.98546-08	2017-03-09 00:13:06.985747-08	\N	\N	\N	\N	\N	\N	\N	\N
4	\N	\N	\N	2017-03-09 00:14:13.499675-08	2017-03-09 00:14:13.500014-08	\N	\N	\N	\N	\N	\N	\N	\N
5	\N	\N	\N	2017-03-09 00:14:46.777557-08	2017-03-09 00:14:46.777895-08	\N	\N	\N	\N	\N	\N	\N	\N
6	\N	\N	\N	2017-03-09 00:15:00.631225-08	2017-03-09 00:15:00.631577-08	\N	\N	\N	\N	\N	\N	\N	\N
7	\N	\N	\N	2017-03-09 00:22:28.157782-08	2017-03-09 00:22:28.15813-08	\N	\N	\N	\N	\N	\N	\N	\N
8	\N	\N	\N	2017-03-09 00:30:43.894602-08	2017-03-09 00:30:43.894956-08	\N	\N	\N	\N	\N	\N	\N	\N
9	\N	\N	\N	2017-03-09 00:53:27.412317-08	2017-03-09 00:53:27.412636-08	\N	\N	\N	\N	\N	\N	\N	\N
10				2017-03-09 01:02:21.538487-08	2017-03-09 01:02:21.55848-08						\N	\N	\N
11	\N	\N	\N	2017-03-09 01:08:25.522195-08	2017-03-09 01:08:25.52254-08	\N	\N	\N	\N	\N	\N	\N	\N
12				2017-03-09 01:08:32.139533-08	2017-03-09 01:08:32.157942-08						\N	\N	\N
13				2017-03-09 01:09:05.720624-08	2017-03-09 01:09:05.73925-08						\N	\N	\N
14	\N	\N	\N	2017-03-09 01:09:56.427413-08	2017-03-09 01:09:56.427763-08	\N	\N	\N	\N	\N	\N	\N	\N
15	\N	\N	\N	2017-03-09 01:11:08.84229-08	2017-03-09 01:11:08.84263-08	\N	\N	\N	\N	\N	\N	\N	\N
17				2017-03-09 01:12:32.279015-08	2017-03-09 01:12:32.296119-08						\N	\N	\N
18				2017-03-09 01:12:48.711882-08	2017-03-09 01:12:48.728709-08						\N	\N	\N
19				2017-03-09 01:13:35.046169-08	2017-03-09 01:13:35.07287-08						\N	\N	\N
20				2017-03-09 01:14:03.678861-08	2017-03-09 01:14:03.696445-08						\N	\N	\N
16	123	123	sdf	2017-03-09 01:12:23.856219-08	2017-03-11 16:49:22.009016-08				sdf	94539	\N	\N	\N
22				2017-03-11 17:00:10.619388-08	2017-03-11 17:18:15.031726-08						\N	\N	\N
21	d			2017-03-11 16:49:39.981558-08	2017-03-11 17:20:29.492604-08						\N	\N	\N
23				2017-03-11 17:18:33.679335-08	2017-03-11 17:29:26.511414-08						\N	\N	\N
24	\N	\N	\N	2017-03-11 22:25:48.41492-08	2017-03-11 22:25:48.41533-08	\N	\N	\N	\N	\N	\N	\N	\N
25	\N	\N	\N	2017-03-11 22:28:27.845275-08	2017-03-11 22:28:27.845905-08	\N	\N	\N	\N	\N	\N	\N	\N
27	\N	\N	\N	2017-03-11 22:29:16.619394-08	2017-03-11 22:29:16.619791-08	\N	\N	\N	\N	\N	\N	\N	\N
53	\N	\N	\N	2017-03-19 23:06:00.916669-07	2017-03-19 23:06:00.917125-07	\N	\N	\N	\N	\N	\N	\N	\N
28				2017-03-11 22:42:29.687985-08	2017-03-11 23:39:59.543958-08						\N	\N	\N
30				2017-03-11 23:57:21.434075-08	2017-03-12 00:25:03.862562-08						\N	\N	\N
54	test			2017-03-19 23:08:05.183287-07	2017-03-19 23:14:35.661268-07						\N	\N	\N
29				2017-03-11 23:42:17.287074-08	2017-03-12 00:55:46.775005-08						\N	\N	\N
55	ARthur			2017-03-19 23:14:44.351069-07	2017-03-19 23:15:02.31304-07						\N	\N	\N
56	\N	\N	\N	2017-03-19 23:19:45.822411-07	2017-03-19 23:19:45.822779-07	\N	\N	\N	\N	\N	\N	\N	\N
26				2017-03-11 22:29:03.866341-08	2017-03-12 01:02:03.570151-08						\N	\N	\N
31	\N	\N	\N	2017-03-12 16:56:46.017505-07	2017-03-12 16:56:46.018078-07	\N	\N	\N	\N	\N	\N	\N	\N
32	\N	\N	\N	2017-03-12 16:57:03.34842-07	2017-03-12 16:57:03.348717-07	\N	\N	\N	\N	\N	\N	\N	\N
33	\N	\N	\N	2017-03-12 16:57:18.838594-07	2017-03-12 16:57:18.838874-07	\N	\N	\N	\N	\N	\N	\N	\N
34	\N	\N	\N	2017-03-12 16:58:03.978081-07	2017-03-12 16:58:03.97844-07	\N	\N	\N	\N	\N	\N	\N	\N
58	\N	\N	\N	2017-03-20 23:15:16.735079-07	2017-03-20 23:15:16.735474-07	\N	\N	\N	\N	\N	\N	\N	\N
76	Arthur			2017-03-25 18:54:49.55016-07	2017-03-25 20:49:20.39047-07						\N	\N	\N
43	Arthur	Shir		2017-03-16 16:45:19.747675-07	2017-03-17 17:38:22.844473-07	566 Bella Vista Court	Fremont	United States	CA	94539	\N	\N	\N
35				2017-03-12 17:40:07.735039-07	2017-03-12 17:46:18.291028-07						\N	\N	\N
46	\N	\N	\N	2017-03-17 21:52:49.922424-07	2017-03-17 21:52:49.922756-07	\N	\N	\N	\N	\N	\N	\N	\N
59	\N	\N	\N	2017-03-21 00:05:05.916469-07	2017-03-21 00:05:05.916843-07	\N	\N	\N	\N	\N	\N	\N	\N
57				2017-03-19 23:29:45.068925-07	2017-03-21 00:06:21.712798-07						\N	\N	\N
60	\N	\N	\N	2017-03-21 01:19:26.835877-07	2017-03-21 01:19:26.83627-07	\N	\N	\N	\N	\N	\N	\N	\N
61	\N	\N	\N	2017-03-21 01:19:37.57984-07	2017-03-21 01:19:37.580144-07	\N	\N	\N	\N	\N	\N	\N	\N
62				2017-03-21 01:20:57.33388-07	2017-03-21 01:21:25.632542-07						\N	\N	\N
36				2017-03-12 17:43:09.564568-07	2017-03-12 17:48:38.409311-07						\N	\N	\N
37	\N	\N	\N	2017-03-12 19:18:42.705442-07	2017-03-12 19:18:42.705788-07	\N	\N	\N	\N	\N	\N	\N	\N
38	\N	\N	\N	2017-03-12 19:20:50.106516-07	2017-03-12 19:20:50.106876-07	\N	\N	\N	\N	\N	\N	\N	\N
39	\N	\N	\N	2017-03-12 19:27:25.149552-07	2017-03-12 19:27:25.149909-07	\N	\N	\N	\N	\N	\N	\N	\N
40	\N	\N	\N	2017-03-12 19:31:53.478069-07	2017-03-12 19:31:53.478364-07	\N	\N	\N	\N	\N	\N	\N	\N
41	\N	\N	\N	2017-03-12 19:32:06.552067-07	2017-03-12 19:32:06.55236-07	\N	\N	\N	\N	\N	\N	\N	\N
63	\N	\N	\N	2017-03-21 03:15:50.668341-07	2017-03-21 03:15:50.668642-07	\N	\N	\N	\N	\N	\N	\N	\N
64	\N	\N	\N	2017-03-21 03:18:53.871531-07	2017-03-21 03:18:53.871839-07	\N	\N	\N	\N	\N	\N	\N	\N
65	\N	\N	\N	2017-03-21 03:29:49.895242-07	2017-03-21 03:29:49.895529-07	\N	\N	\N	\N	\N	\N	\N	\N
66	\N	\N	\N	2017-03-21 04:47:54.527606-07	2017-03-21 04:47:54.527961-07	\N	\N	\N	\N	\N	\N	\N	\N
67	\N	\N	\N	2017-03-21 19:29:38.181447-07	2017-03-21 19:29:38.18183-07	\N	\N	\N	\N	\N	\N	\N	\N
68	\N	\N	\N	2017-03-21 20:12:02.075627-07	2017-03-21 20:12:02.075996-07	\N	\N	\N	\N	\N	\N	\N	\N
69				2017-03-21 20:26:15.163286-07	2017-03-21 20:27:22.333431-07						\N	\N	\N
42				2017-03-16 16:01:40.969667-07	2017-03-16 16:31:53.231781-07						\N	\N	\N
44	\N	\N	\N	2017-03-16 17:32:05.416711-07	2017-03-16 17:32:05.417039-07	\N	\N	\N	\N	\N	\N	\N	\N
45	\N	\N	\N	2017-03-17 15:49:52.142784-07	2017-03-17 15:49:52.143082-07	\N	\N	\N	\N	\N	\N	\N	\N
48				2017-03-17 22:34:21.786991-07	2017-03-17 22:36:04.22625-07						\N	\N	\N
70				2017-03-21 20:45:40.439952-07	2017-03-21 20:45:50.690603-07						\N	\N	\N
71				2017-03-21 20:51:44.552068-07	2017-03-21 20:51:47.206885-07						\N	\N	\N
47	Arthur	Shir		2017-03-17 22:23:17.498366-07	2017-03-17 23:45:13.631018-07	566 Bella Vista Court	Fremont	United States	CA	94539	\N	\N	\N
72	\N	\N	\N	2017-03-21 20:58:17.800156-07	2017-03-21 20:58:17.800461-07	\N	\N	\N	\N	\N	\N	\N	\N
49				2017-03-17 23:45:31.132284-07	2017-03-18 15:00:15.934987-07						\N	\N	\N
50	\N	\N	\N	2017-03-18 15:00:44.108084-07	2017-03-18 15:00:44.108377-07	\N	\N	\N	\N	\N	\N	\N	\N
51	\N	\N	\N	2017-03-18 15:08:37.163539-07	2017-03-18 15:08:37.163895-07	\N	\N	\N	\N	\N	\N	\N	\N
52	Arthur	Shir		2017-03-19 23:05:00.574289-07	2017-03-19 23:05:42.10796-07	566 Bella Vista Court	Fremont	United States	CA	94539	\N	\N	\N
73				2017-03-21 21:07:51.844305-07	2017-03-21 21:07:54.932819-07						\N	\N	\N
80				2017-03-26 00:50:36.261839-07	2017-03-26 00:50:38.507905-07						\N	\N	\N
74				2017-03-21 21:08:46.259993-07	2017-03-26 01:53:39.296574-07						\N	\N	\N
75				2017-03-25 18:54:32.955939-07	2017-03-26 01:53:44.894899-07						\N	\N	\N
77	Arthur			2017-03-25 19:04:22.975866-07	2017-03-26 02:51:06.399263-07						\N	\N	\N
79				2017-03-25 20:18:08.593472-07	2017-03-26 03:02:11.361048-07						\N	\N	\N
101	Arthur	Shir		2017-03-29 20:28:29.224195-07	2017-03-29 20:29:05.753558-07	566 Bella Vista Court	Fremont	United States	CA	94539	\N	\N	\N
78				2017-03-25 20:06:58.833218-07	2017-03-26 03:31:53.225919-07						\N	\N	\N
89	\N	\N	\N	2017-03-28 05:14:30.792892-07	2017-03-28 05:14:30.793202-07	\N	\N	\N	\N	\N	\N	\N	\N
81				2017-03-26 03:34:34.336489-07	2017-03-26 03:34:41.666934-07						\N	\N	\N
102	\N	\N	\N	2017-03-30 01:07:04.828574-07	2017-03-30 01:07:04.82895-07	\N	\N	\N	\N	\N	\N	\N	\N
82				2017-03-26 03:35:41.309945-07	2017-03-26 03:35:46.193455-07						\N	\N	\N
88	Arthur	Shir		2017-03-28 04:46:47.971426-07	2017-03-28 05:18:45.851245-07	566 Bella Vista Court	Fremont	United States	CA	94539	\N	\N	\N
83				2017-03-26 03:40:33.493643-07	2017-03-26 03:40:38.598826-07						\N	\N	\N
84	\N	\N	\N	2017-03-27 03:01:54.781154-07	2017-03-27 03:01:54.781467-07	\N	\N	\N	\N	\N	\N	\N	\N
85	\N	\N	\N	2017-03-28 02:24:23.014835-07	2017-03-28 02:24:23.015181-07	\N	\N	\N	\N	\N	\N	\N	\N
86	\N	\N	\N	2017-03-28 02:24:40.463216-07	2017-03-28 02:24:40.463551-07	\N	\N	\N	\N	\N	\N	\N	\N
87	\N	\N	\N	2017-03-28 02:29:25.043179-07	2017-03-28 02:29:25.044001-07	\N	\N	\N	\N	\N	\N	\N	\N
90	\N	\N	\N	2017-03-28 05:21:17.270028-07	2017-03-28 05:21:17.27034-07	\N	\N	\N	\N	\N	\N	\N	\N
91	\N	\N	\N	2017-03-28 05:46:03.018867-07	2017-03-28 05:46:03.019284-07	\N	\N	\N	\N	\N	\N	\N	\N
92	\N	\N	\N	2017-03-28 05:46:30.271524-07	2017-03-28 05:46:30.271856-07	\N	\N	\N	\N	\N	\N	\N	\N
93	123	123		2017-03-28 15:21:14.342735-07	2017-03-28 15:23:54.403428-07	s	sdf	sdf	sdf	sdf	\N	\N	\N
94	\N	\N	\N	2017-03-28 15:27:04.903344-07	2017-03-28 15:27:04.903625-07	\N	\N	\N	\N	\N	\N	\N	\N
95	\N	\N	\N	2017-03-28 16:48:15.052085-07	2017-03-28 16:48:15.052434-07	\N	\N	\N	\N	\N	\N	\N	\N
96	\N	\N	\N	2017-03-28 16:48:23.27464-07	2017-03-28 16:48:23.274923-07	\N	\N	\N	\N	\N	\N	\N	\N
97	\N	\N	\N	2017-03-28 16:54:21.506039-07	2017-03-28 16:54:21.506472-07	\N	\N	\N	\N	\N	\N	\N	\N
103	Arthur	Shir		2017-03-30 01:13:18.329567-07	2017-03-30 01:14:00.335465-07	566 Bella Vista Court	Fremont	United States	CA	94539	\N	\N	\N
98	sdf	sd		2017-03-28 17:23:33.239002-07	2017-03-28 18:12:23.874176-07	sd	sd	sd	sd	sd	\N	\N	\N
99	\N	\N	\N	2017-03-29 19:43:59.701268-07	2017-03-29 19:43:59.701612-07	\N	\N	\N	\N	\N	\N	\N	\N
100	\N	\N	\N	2017-03-29 19:44:13.833698-07	2017-03-29 19:44:13.833996-07	\N	\N	\N	\N	\N	\N	\N	\N
106	Arthur	Shir		2017-03-30 02:57:37.498592-07	2017-03-30 02:59:59.823069-07	1617 VALDORA Street #22	Davis	United States	CA	95616	\N	\N	\N
107	\N	\N	\N	2017-03-30 03:01:11.781375-07	2017-03-30 03:01:11.781669-07	\N	\N	\N	\N	\N	\N	\N	\N
108	Arthur	Shir		2017-03-30 05:16:21.804807-07	2017-03-30 05:16:43.951173-07	1617 VALDORA Street #22	Davis	United States	CA	95616	\N	\N	\N
109	Arthur	Shir		2017-03-30 05:17:38.388058-07	2017-03-30 05:17:57.762114-07	1617 VALDORA Street #22	Davis	United States	CA	95616	\N	\N	\N
110	Arthur	Shir		2017-03-30 05:19:03.40461-07	2017-03-30 05:19:41.642233-07	1617 VALDORA Street #22	Davis	United States	CA	95616	\N	\N	\N
111	Arthur	Shir		2017-03-30 05:21:38.746604-07	2017-03-30 05:22:35.960805-07	1617 VALDORA Street #22	Davis	United States	CA	95616	\N	\N	\N
112	Arthur	Shir	sdf	2017-03-30 05:25:35.095169-07	2017-03-30 05:29:22.655393-07	1617 VALDORA Street #22	Davis	United States	CA	95616	\N	\N	\N
113	Arthur	Shir	pdf	2017-03-30 05:41:48.797919-07	2017-03-30 05:42:13.955094-07	1617 VALDORA Street #22	Davis	United States	CA	95616	\N	\N	\N
114	Arthur	Shir	pdf	2017-03-30 05:59:43.467516-07	2017-03-30 06:00:34.540446-07	1617 VALDORA Street #22	Davis	United States	CA	95616	\N	\N	\N
115	Arthur	Shir	pdf	2017-03-30 06:08:23.817663-07	2017-03-30 06:08:41.207001-07	1617 VALDORA Street #22	Davis	United States	CA	95616	\N	\N	\N
116	\N	\N	\N	2017-03-30 06:09:50.612459-07	2017-03-30 06:09:50.612786-07	\N	\N	\N	\N	\N	\N	\N	\N
117	\N	\N	\N	2017-03-30 16:49:49.343752-07	2017-03-30 16:49:49.344081-07	\N	\N	\N	\N	\N	\N	\N	\N
126	sdf	sdlkfj	lkj	2017-03-31 04:20:48.279403-07	2017-03-31 13:22:28.777784-07	lkj	lkj	jlk	lkj	lkjlk	05	08	2005
119	Arth	dsf	sdf	2017-03-30 17:01:26.754324-07	2017-03-30 18:03:08.968691-07	sdf	df	df	df	fdf	\N	\N	\N
124	Arthur	Shir	sdfd	2017-03-31 01:47:41.789833-07	2017-03-31 12:21:54.815616-07	566 Bella Vista Court	Fremont	United States	CA	94539	\N	\N	\N
121	klj	lkjlk	jlk	2017-03-30 18:15:58.498906-07	2017-03-30 18:17:56.857011-07	jlk	jlk	jkl	jkl	jkl	\N	\N	\N
122	\N	\N	\N	2017-03-30 23:07:31.324946-07	2017-03-30 23:07:31.325289-07	\N	\N	\N	\N	\N	\N	\N	\N
125	Arthur	Shir	Cello	2017-03-31 03:14:53.888426-07	2017-03-31 04:00:59.766877-07	566 Bella Vista Court	Fremont	United States	CA	94539	\N	\N	\N
120	Arthur	Shir	sdf	2017-03-30 18:04:34.322791-07	2017-03-31 04:08:16.400931-07	566 Bella Vista Court	Fremont	United States	CA	94539	\N	\N	\N
118	\N	\N	\N	2017-03-30 16:50:44.145991-07	2017-03-31 04:08:49.798224-07	\N	\N	\N	\N	\N	\N	\N	\N
127	lksdj	lkj	lkjl	2017-03-31 12:23:40.197325-07	2017-03-31 12:25:55.858149-07	lkjlk	jkl	j	jlk	jkl	09	08	2007
104	\N	asdfsda	\N	2017-03-30 01:31:09.696836-07	2017-03-31 04:13:48.914714-07	\N	sdfsd	\N	\N	\N	\N	\N	\N
123	sdf	\N	\N	2017-03-31 01:11:08.462777-07	2017-03-31 01:47:31.934398-07	\N	\N	\N	\N	\N	\N	\N	\N
132	asdlkj	lkj	lkj	2017-04-02 23:50:41.087725-07	2017-04-04 00:30:27.789132-07	lkj	lkj	lkj	lkj	lkj	09	09	2010
131	jlk	jlk	jkl	2017-04-02 23:45:56.168321-07	2017-04-04 00:45:38.071025-07	jlk	jkl	jlk	jkl	jkl	09	09	2010
105	lkj	lkj	lkj	2017-03-30 02:57:26.28467-07	2017-04-04 22:49:01.294826-07	lkj	lkj	ljk	lkj	lkj	09	09	2010
130	lkj	lkj	lkj	2017-04-02 22:50:23.003008-07	2017-04-04 22:52:58.452-07	lkj	klj	lkj	lkj	lkj	05	08	1995
133	\N	\N	\N	2017-04-04 23:15:56.196726-07	2017-04-04 23:15:56.197053-07	\N	\N	\N	\N	\N	\N	\N	\N
128	lkj	lkj	lkjlkj	2017-03-31 13:23:04.040111-07	2017-04-02 05:47:23.217312-07	lkjlkj	lkjkl	j	jlk	jlk	1	1	2010
129	lkj	lkj	lkj	2017-04-02 22:23:41.431893-07	2017-04-02 23:18:22.747007-07	lkj	lkj	lkj	lkj	lkj	09	09	1993
\.


--
-- Name: registration_site_person_id_seq; Type: SEQUENCE SET; Schema: public; Owner: usimc
--

SELECT pg_catalog.setval('registration_site_person_id_seq', 133, true);


--
-- Data for Name: registration_site_piece; Type: TABLE DATA; Schema: public; Owner: usimc
--

COPY registration_site_piece (id, title, composer, entry_id, created_at, updated_at, movement, opus, youtube_link, minutes, seconds) FROM stdin;
125	pdfsdf	sdfds	106	2017-03-30 05:25:35.099346-07	2017-03-30 05:29:22.671844-07			youtube.com/watch?v=OINa46HeWg8	\N	\N
126	sdf	pdfds	107	2017-03-30 05:41:48.801835-07	2017-03-30 05:42:13.976876-07				\N	\N
192	lkj	lkj	124	2017-04-02 22:50:23.007947-07	2017-04-04 22:52:58.474189-07	\N	\N	lkj	lkj	ljk
127	sdf	sdfd	108	2017-03-30 05:59:43.471444-07	2017-03-30 06:00:34.549936-07			pdf	\N	\N
128	pdf	sdf	109	2017-03-30 06:08:23.821664-07	2017-03-30 06:08:41.24852-07				\N	\N
129	\N	\N	110	2017-03-30 06:09:50.616869-07	2017-03-30 06:09:50.617231-07	\N	\N	\N	\N	\N
114	sd	sd	97	2017-03-30 01:13:18.33607-07	2017-03-30 01:14:00.343331-07				\N	\N
200	ljk	lkj	124	2017-04-04 22:52:56.31592-07	2017-04-04 22:52:58.477987-07	\N	\N	ljk	lkj	ljk
117	sdf	sdf	100	2017-03-30 02:57:37.502136-07	2017-03-30 02:59:59.849897-07				\N	\N
118	\N	\N	101	2017-03-30 03:01:11.784948-07	2017-03-30 03:01:11.785212-07	\N	\N	\N	\N	\N
119	sd	pdf	102	2017-03-30 05:16:21.80923-07	2017-03-30 05:16:43.959561-07				\N	\N
120	sdf	sdfd	103	2017-03-30 05:17:38.391789-07	2017-03-30 05:17:57.773896-07				\N	\N
121	sdfd	pdf	104	2017-03-30 05:19:03.408346-07	2017-03-30 05:19:41.651265-07		pdf		\N	\N
122	pdf	pdf	104	2017-03-30 05:19:41.634642-07	2017-03-30 05:19:41.65359-07				\N	\N
123	pdf	pdfd	105	2017-03-30 05:21:38.750344-07	2017-03-30 05:22:35.985958-07			https://www.youtube.com/watch?v=iqxIu1cyRfk	\N	\N
124	sdf	pdf	105	2017-03-30 05:22:35.888569-07	2017-03-30 05:22:35.989032-07	pdf	sdf	https://www.youtube.com/watch?v=iqxIu1cyRfk	\N	\N
201	\N	\N	127	2017-04-04 23:15:56.200493-07	2017-04-04 23:15:56.200847-07	\N	\N	\N	\N	\N
138	sdf	df	119	2017-03-31 03:14:53.893784-07	2017-03-31 04:00:59.777424-07	\N	\N	\N	6	30
191	kjh	lkj	123	2017-04-02 22:23:41.436043-07	2017-04-02 23:18:22.793228-07	\N	\N	lkj	lkj	lkj
193	lkj	lkj	123	2017-04-02 23:18:20.31732-07	2017-04-02 23:18:22.802773-07	\N	\N	lk	lkj	lkj
171	jl	lk;j	121	2017-03-31 12:23:40.200914-07	2017-03-31 12:25:55.890217-07	\N	kjkl	\N	lkj	lkj
172	lkj	klj	121	2017-03-31 12:24:09.114619-07	2017-03-31 12:25:55.893635-07	\N	\N	\N	lkjl	kkjl
173	klj	lkj	121	2017-03-31 12:24:09.117123-07	2017-03-31 12:25:55.89808-07	kjl	klj	\N	ljk	lkj
195	lkj	lkj	126	2017-04-02 23:50:41.091524-07	2017-04-04 00:30:27.823956-07	\N	\N	sdf	klj	lkj
196	lkj	lkj	126	2017-04-03 22:51:19.629951-07	2017-04-04 00:30:27.82781-07	\N	\N	lkj	lkj	lkj
197	lkj	lkj	126	2017-04-03 22:59:59.351148-07	2017-04-04 00:30:27.831469-07	\N	\N	lkj	lkj	lkj
189	Bach Suite	sdfsdf	122	2017-03-31 13:24:55.792769-07	2017-04-02 05:47:23.254268-07	\N	\N	sdf	sdf	sdf
190	sdfsd	sdf	122	2017-04-02 05:45:34.454938-07	2017-04-02 05:47:23.259541-07	\N	\N	sdfs	sdf	sdf
194	lkj	lkjlk	125	2017-04-02 23:45:56.172694-07	2017-04-04 00:45:38.084409-07	\N	\N	lkjlkjkl	lkjlkj	klj
198	lkj	lkjkl	125	2017-04-04 00:45:30.705229-07	2017-04-04 00:45:38.087979-07	\N	\N	jlk	jlk	jlk
116	lk	kl	99	2017-03-30 02:57:26.288976-07	2017-04-04 22:49:01.308921-07	\N	\N	lkj	kl	lk
199	lk	lk	99	2017-04-04 22:48:58.830209-07	2017-04-04 22:49:01.312724-07	\N	\N	lk	kl	lk
\.


--
-- Name: registration_site_piece_id_seq; Type: SEQUENCE SET; Schema: public; Owner: usimc
--

SELECT pg_catalog.setval('registration_site_piece_id_seq', 201, true);


--
-- Data for Name: registration_site_teacher; Type: TABLE DATA; Schema: public; Owner: usimc
--

COPY registration_site_teacher (id, first_name, last_name, email, cmtanc_code, created_at, updated_at) FROM stdin;
1	\N	\N	\N	\N	2017-03-09 00:12:43.953768-08	2017-03-09 00:12:43.954106-08
2	\N	\N	\N	\N	2017-03-09 00:12:56.131746-08	2017-03-09 00:12:56.132025-08
3	\N	\N	\N	\N	2017-03-09 00:13:06.983297-08	2017-03-09 00:13:06.983575-08
4	\N	\N	\N	\N	2017-03-09 00:14:13.497614-08	2017-03-09 00:14:13.497968-08
5	\N	\N	\N	\N	2017-03-09 00:14:46.775525-08	2017-03-09 00:14:46.775839-08
6	\N	\N	\N	\N	2017-03-09 00:15:00.629185-08	2017-03-09 00:15:00.629532-08
7	\N	\N	\N	\N	2017-03-09 00:22:28.155588-08	2017-03-09 00:22:28.155921-08
8	\N	\N	\N	\N	2017-03-09 00:30:43.892468-08	2017-03-09 00:30:43.892805-08
9	\N	\N	\N	\N	2017-03-09 00:53:27.410155-08	2017-03-09 00:53:27.410486-08
10					2017-03-09 01:02:21.539518-08	2017-03-09 01:02:21.561647-08
11	\N	\N	\N	\N	2017-03-09 01:08:25.520078-08	2017-03-09 01:08:25.520412-08
12					2017-03-09 01:08:32.14021-08	2017-03-09 01:08:32.160117-08
13	Maxine				2017-03-09 01:09:05.721562-08	2017-03-09 01:09:05.742245-08
14	\N	\N	\N	\N	2017-03-09 01:09:56.424912-08	2017-03-09 01:09:56.425231-08
15	\N	\N	\N	\N	2017-03-09 01:11:08.84023-08	2017-03-09 01:11:08.840577-08
17					2017-03-09 01:12:32.279661-08	2017-03-09 01:12:32.298863-08
18					2017-03-09 01:12:48.712522-08	2017-03-09 01:12:48.731342-08
19					2017-03-09 01:13:35.047317-08	2017-03-09 01:13:35.079814-08
20					2017-03-09 01:14:03.679517-08	2017-03-09 01:14:03.700763-08
30					2017-03-11 23:57:21.432011-08	2017-03-12 00:25:03.865254-08
16	sdfsd	sdf		sdf	2017-03-09 01:12:23.854248-08	2017-03-11 16:49:22.014424-08
29				11	2017-03-11 23:42:17.284028-08	2017-03-12 00:55:46.777657-08
26				1111	2017-03-11 22:29:03.864178-08	2017-03-12 01:02:03.574067-08
31	\N	\N	\N	\N	2017-03-12 16:56:46.014278-07	2017-03-12 16:56:46.014915-07
32	\N	\N	\N	\N	2017-03-12 16:57:03.34603-07	2017-03-12 16:57:03.346293-07
33	\N	\N	\N	\N	2017-03-12 16:57:18.836593-07	2017-03-12 16:57:18.836886-07
34	\N	\N	\N	\N	2017-03-12 16:58:03.97574-07	2017-03-12 16:58:03.97607-07
22					2017-03-11 17:00:10.617094-08	2017-03-11 17:18:15.037486-08
21				1232	2017-03-11 16:49:39.978948-08	2017-03-11 17:20:29.496104-08
35				1111	2017-03-12 17:40:07.733015-07	2017-03-12 17:46:18.295804-07
23					2017-03-11 17:18:33.677381-08	2017-03-11 17:29:26.514418-08
24	\N	\N	\N	\N	2017-03-11 22:25:48.41279-08	2017-03-11 22:25:48.413155-08
25	\N	\N	\N	\N	2017-03-11 22:28:27.842874-08	2017-03-11 22:28:27.843265-08
27	\N	\N	\N	\N	2017-03-11 22:29:16.617059-08	2017-03-11 22:29:16.617336-08
36				1111	2017-03-12 17:43:09.562461-07	2017-03-12 17:48:38.412509-07
37	\N	\N	\N	\N	2017-03-12 19:18:42.703327-07	2017-03-12 19:18:42.703694-07
38	\N	\N	\N	\N	2017-03-12 19:20:50.102275-07	2017-03-12 19:20:50.103183-07
39	\N	\N	\N	\N	2017-03-12 19:27:25.147366-07	2017-03-12 19:27:25.147699-07
40	\N	\N	\N	\N	2017-03-12 19:31:53.475477-07	2017-03-12 19:31:53.475757-07
41	\N	\N	\N	\N	2017-03-12 19:32:06.549984-07	2017-03-12 19:32:06.550274-07
28					2017-03-11 22:42:29.685575-08	2017-03-11 23:39:59.549364-08
69					2017-03-21 20:26:15.16123-07	2017-03-21 20:27:22.339098-07
70					2017-03-21 20:45:40.437827-07	2017-03-21 20:45:50.69396-07
71					2017-03-21 20:51:44.550034-07	2017-03-21 20:51:47.21211-07
72	\N	\N	\N	\N	2017-03-21 20:58:17.798022-07	2017-03-21 20:58:17.798325-07
42					2017-03-16 16:01:40.967279-07	2017-03-16 16:31:53.237219-07
44	\N	\N	\N	\N	2017-03-16 17:32:05.414103-07	2017-03-16 17:32:05.414449-07
45	\N	\N	\N	\N	2017-03-17 15:49:52.140341-07	2017-03-17 15:49:52.140665-07
73					2017-03-21 21:07:51.842093-07	2017-03-21 21:07:54.935815-07
80					2017-03-26 00:50:36.25938-07	2017-03-26 00:50:38.510409-07
78					2017-03-25 20:06:58.830968-07	2017-03-26 03:31:53.229361-07
74					2017-03-21 21:08:46.257978-07	2017-03-26 01:53:39.302463-07
75					2017-03-25 18:54:32.951917-07	2017-03-26 01:53:44.900698-07
43	Laila	Doulaki	Lailadoulaki@gmail.com	1111	2017-03-16 16:45:19.745205-07	2017-03-17 17:38:22.847323-07
46	\N	\N	\N	\N	2017-03-17 21:52:49.91876-07	2017-03-17 21:52:49.919105-07
77					2017-03-25 19:04:22.973335-07	2017-03-26 02:51:06.402531-07
81					2017-03-26 03:34:34.334165-07	2017-03-26 03:34:41.672732-07
79					2017-03-25 20:18:08.591142-07	2017-03-26 03:02:11.366523-07
82					2017-03-26 03:35:41.307923-07	2017-03-26 03:35:46.195777-07
83					2017-03-26 03:40:33.49098-07	2017-03-26 03:40:38.602662-07
84	\N	\N	\N	\N	2017-03-27 03:01:54.778763-07	2017-03-27 03:01:54.779077-07
85	\N	\N	\N	\N	2017-03-28 02:24:23.012747-07	2017-03-28 02:24:23.013099-07
86	\N	\N	\N	\N	2017-03-28 02:24:40.461005-07	2017-03-28 02:24:40.461277-07
87	\N	\N	\N	\N	2017-03-28 02:29:25.03949-07	2017-03-28 02:29:25.040167-07
48					2017-03-17 22:34:21.785059-07	2017-03-17 22:36:04.232344-07
106	Arthur	Shir	arthur.shir@gmail.com		2017-03-30 02:57:37.496477-07	2017-03-30 02:59:59.830073-07
107	\N	\N	\N	\N	2017-03-30 03:01:11.779201-07	2017-03-30 03:01:11.779522-07
47					2017-03-17 22:23:17.495935-07	2017-03-17 23:45:13.64034-07
108	Arthur	Shir	arthur.shir@gmail.com		2017-03-30 05:16:21.802611-07	2017-03-30 05:16:43.953463-07
49				1111	2017-03-17 23:45:31.127346-07	2017-03-18 15:00:15.94056-07
50	\N	\N	\N	\N	2017-03-18 15:00:44.106049-07	2017-03-18 15:00:44.106339-07
51	\N	\N	\N	\N	2017-03-18 15:08:37.160933-07	2017-03-18 15:08:37.161365-07
52	Mrs.	Kim	12@gmail.com	1111	2017-03-19 23:05:00.571898-07	2017-03-19 23:05:42.110764-07
53	\N	\N	\N	\N	2017-03-19 23:06:00.914636-07	2017-03-19 23:06:00.914934-07
109	Arthur	Shir	arthur.shir@gmail.com		2017-03-30 05:17:38.385627-07	2017-03-30 05:17:57.764867-07
110	Arthur	Shir	arthur.shir@gmail.com		2017-03-30 05:19:03.402635-07	2017-03-30 05:19:41.644513-07
111	Arthur	Shir	arthur.shir@gmail.com		2017-03-30 05:21:38.744538-07	2017-03-30 05:22:35.969599-07
54					2017-03-19 23:08:05.181342-07	2017-03-19 23:14:35.666692-07
55					2017-03-19 23:14:44.349144-07	2017-03-19 23:15:02.316499-07
56	\N	\N	\N	\N	2017-03-19 23:19:45.820133-07	2017-03-19 23:19:45.820479-07
58	\N	\N	\N	\N	2017-03-20 23:15:16.731665-07	2017-03-20 23:15:16.732218-07
112	Arthur	Shir	arthur.shir@gmail.com		2017-03-30 05:25:35.092936-07	2017-03-30 05:29:22.660004-07
98	12	3	Arthur.shir@gmail.com		2017-03-28 17:23:33.236431-07	2017-03-28 18:12:23.876226-07
89	\N	\N	\N	\N	2017-03-28 05:14:30.790668-07	2017-03-28 05:14:30.79097-07
99	\N	\N	\N	\N	2017-03-29 19:43:59.699034-07	2017-03-29 19:43:59.699374-07
59	\N	\N	\N	\N	2017-03-21 00:05:05.914284-07	2017-03-21 00:05:05.914662-07
57				1111	2017-03-19 23:29:45.065621-07	2017-03-21 00:06:21.715367-07
60	\N	\N	\N	\N	2017-03-21 01:19:26.833538-07	2017-03-21 01:19:26.833984-07
61	\N	\N	\N	\N	2017-03-21 01:19:37.577853-07	2017-03-21 01:19:37.578152-07
62				1111	2017-03-21 01:20:57.331728-07	2017-03-21 01:21:25.63665-07
63	\N	\N	\N	\N	2017-03-21 03:15:50.666283-07	2017-03-21 03:15:50.666576-07
64	\N	\N	\N	\N	2017-03-21 03:18:53.869325-07	2017-03-21 03:18:53.869621-07
65	\N	\N	\N	\N	2017-03-21 03:29:49.893296-07	2017-03-21 03:29:49.893586-07
66	\N	\N	\N	\N	2017-03-21 04:47:54.525517-07	2017-03-21 04:47:54.525861-07
67	\N	\N	\N	\N	2017-03-21 19:29:38.179242-07	2017-03-21 19:29:38.179614-07
68	\N	\N	\N	\N	2017-03-21 20:12:02.07352-07	2017-03-21 20:12:02.07388-07
88	Arthur	Shir	a@gmail.com		2017-03-28 04:46:47.969217-07	2017-03-28 05:18:45.856487-07
90	\N	\N	\N	\N	2017-03-28 05:21:17.267724-07	2017-03-28 05:21:17.268048-07
91	\N	\N	\N	\N	2017-03-28 05:46:03.01655-07	2017-03-28 05:46:03.016974-07
92	\N	\N	\N	\N	2017-03-28 05:46:30.269353-07	2017-03-28 05:46:30.269638-07
93	dsfjk	lskdjf	arthur.shir@gmail.com		2017-03-28 15:21:14.340249-07	2017-03-28 15:23:54.40901-07
94	\N	\N	\N	\N	2017-03-28 15:27:04.901263-07	2017-03-28 15:27:04.901559-07
95	\N	\N	\N	\N	2017-03-28 16:48:15.049661-07	2017-03-28 16:48:15.05006-07
96	\N	\N	\N	\N	2017-03-28 16:48:23.272402-07	2017-03-28 16:48:23.272697-07
97	\N	\N	\N	\N	2017-03-28 16:54:21.50285-07	2017-03-28 16:54:21.50312-07
76					2017-03-25 18:54:49.548029-07	2017-03-25 20:49:20.395507-07
100	\N	\N	\N	\N	2017-03-29 19:44:13.831664-07	2017-03-29 19:44:13.831956-07
101	ARthu	Shir	Arthur.shir@gmail.com		2017-03-29 20:28:29.222066-07	2017-03-29 20:29:05.755615-07
102	\N	\N	\N	\N	2017-03-30 01:07:04.824182-07	2017-03-30 01:07:04.824639-07
103	Arthur	Shir	Arthur.shir@gmail.com		2017-03-30 01:13:18.325942-07	2017-03-30 01:14:00.337848-07
113	Arthur	Shir	arthur.shir@gmail.com		2017-03-30 05:41:48.795866-07	2017-03-30 05:42:13.963122-07
114	Arthur	Shir	arthur.shir@gmail.com		2017-03-30 05:59:43.465316-07	2017-03-30 06:00:34.542925-07
115	Arthur	Shir	arthur.shir@gmail.com		2017-03-30 06:08:23.815374-07	2017-03-30 06:08:41.221286-07
116	\N	\N	\N	\N	2017-03-30 06:09:50.610415-07	2017-03-30 06:09:50.61075-07
117	\N	\N	\N	\N	2017-03-30 16:49:49.341487-07	2017-03-30 16:49:49.341819-07
119	Arthur	Shir	Arthur.shir@gmail.com		2017-03-30 17:01:26.752148-07	2017-03-30 18:03:08.970829-07
121	jlk	jlk	Arthur.shir@gmail.com		2017-03-30 18:15:58.496642-07	2017-03-30 18:17:56.859206-07
122	\N	\N	\N	\N	2017-03-30 23:07:31.322747-07	2017-03-30 23:07:31.323085-07
123	\N	\N	\N	\N	2017-03-31 01:11:08.459681-07	2017-03-31 01:47:31.929766-07
104	\N	\N	\N	\N	2017-03-30 01:31:09.694715-07	2017-03-31 04:13:48.908292-07
125	Ling	Lee	Arthur.shir@gmail.com	\N	2017-03-31 03:14:53.886398-07	2017-03-31 04:00:59.759466-07
120	Arthur	Shir	Arthur.shir@gmail.com	PN00007	2017-03-30 18:04:34.320721-07	2017-03-31 04:08:16.396213-07
118	\N	\N	\N	\N	2017-03-30 16:50:44.143878-07	2017-03-31 04:08:49.79405-07
124	Lingll	Lee	Arthur.shir@gmail.com	\N	2017-03-31 01:47:41.787801-07	2017-03-31 12:21:54.81164-07
126	lkj	lkj	Arthur.shir@gmail.com	klj	2017-03-31 04:20:48.277149-07	2017-03-31 13:22:28.770944-07
127	Te	Ching	Arthur.shir@gmail.com	\N	2017-03-31 12:23:40.195232-07	2017-03-31 12:25:55.853434-07
128	Ling	Lee	Arthur.shir@gmail.com	\N	2017-03-31 13:23:04.037973-07	2017-04-02 05:47:23.211138-07
129	Arthur	Shir	Arthur.shir@gmail.com	\N	2017-04-02 22:23:41.429504-07	2017-04-02 23:18:22.739133-07
132	ldskj	lkj	Arthur.shir@gmail.com	HP12500	2017-04-02 23:50:41.085713-07	2017-04-04 00:30:27.783044-07
131	jkl	jklj	Arthur.shir@gmail.com	\N	2017-04-02 23:45:56.165961-07	2017-04-04 00:45:38.065381-07
105	lkj	lkj	Arthur.shir@gmail.com	\N	2017-03-30 02:57:26.282209-07	2017-04-04 22:49:01.290956-07
130	lkj	lkj	Arthur.shir@gmail.com	\N	2017-04-02 22:50:22.998904-07	2017-04-04 22:52:58.447763-07
133	\N	\N	\N	\N	2017-04-04 23:15:56.194896-07	2017-04-04 23:15:56.1952-07
\.


--
-- Name: registration_site_teacher_id_seq; Type: SEQUENCE SET; Schema: public; Owner: usimc
--

SELECT pg_catalog.setval('registration_site_teacher_id_seq', 133, true);


--
-- Data for Name: registration_site_usimcuser; Type: TABLE DATA; Schema: public; Owner: usimc
--

COPY registration_site_usimcuser (id, user_id, created_at, updated_at, is_admin) FROM stdin;
1	1	2017-03-09 00:07:15.80784-08	2017-03-09 00:07:15.80817-08	f
2	2	2017-03-17 22:34:14.036661-07	2017-03-17 22:34:14.03702-07	f
3	3	2017-03-19 23:23:44.255656-07	2017-03-19 23:23:44.256059-07	f
4	4	2017-03-21 20:39:05.830647-07	2017-03-21 20:39:05.83128-07	f
5	5	2017-03-21 20:57:45.353569-07	2017-03-21 20:57:45.353845-07	f
6	6	2017-03-21 21:06:21.394233-07	2017-03-21 21:06:21.394597-07	f
\.


--
-- Name: registration_site_usimcuser_id_seq; Type: SEQUENCE SET; Schema: public; Owner: usimc
--

SELECT pg_catalog.setval('registration_site_usimcuser_id_seq', 6, true);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: registration_site_charge registration_site_charge_pkey; Type: CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY registration_site_charge
    ADD CONSTRAINT registration_site_charge_pkey PRIMARY KEY (id);


--
-- Name: registration_site_ensemblemember registration_site_ensemblemember_pkey; Type: CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY registration_site_ensemblemember
    ADD CONSTRAINT registration_site_ensemblemember_pkey PRIMARY KEY (id);


--
-- Name: registration_site_entry registration_site_entry_lead_performer_id_key; Type: CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY registration_site_entry
    ADD CONSTRAINT registration_site_entry_lead_performer_id_key UNIQUE (lead_performer_id);


--
-- Name: registration_site_entry registration_site_entry_parent_contact_id_key; Type: CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY registration_site_entry
    ADD CONSTRAINT registration_site_entry_parent_contact_id_key UNIQUE (parent_contact_id);


--
-- Name: registration_site_entry registration_site_entry_pkey; Type: CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY registration_site_entry
    ADD CONSTRAINT registration_site_entry_pkey PRIMARY KEY (id);


--
-- Name: registration_site_entry registration_site_entry_teacher_id_key; Type: CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY registration_site_entry
    ADD CONSTRAINT registration_site_entry_teacher_id_key UNIQUE (teacher_id);


--
-- Name: registration_site_parentcontact registration_site_parentcontact_pkey; Type: CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY registration_site_parentcontact
    ADD CONSTRAINT registration_site_parentcontact_pkey PRIMARY KEY (id);


--
-- Name: registration_site_person registration_site_person_pkey; Type: CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY registration_site_person
    ADD CONSTRAINT registration_site_person_pkey PRIMARY KEY (id);


--
-- Name: registration_site_piece registration_site_piece_pkey; Type: CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY registration_site_piece
    ADD CONSTRAINT registration_site_piece_pkey PRIMARY KEY (id);


--
-- Name: registration_site_teacher registration_site_teacher_pkey; Type: CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY registration_site_teacher
    ADD CONSTRAINT registration_site_teacher_pkey PRIMARY KEY (id);


--
-- Name: registration_site_usimcuser registration_site_usimcuser_pkey; Type: CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY registration_site_usimcuser
    ADD CONSTRAINT registration_site_usimcuser_pkey PRIMARY KEY (id);


--
-- Name: registration_site_usimcuser registration_site_usimcuser_user_id_key; Type: CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY registration_site_usimcuser
    ADD CONSTRAINT registration_site_usimcuser_user_id_key UNIQUE (user_id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: usimc
--

CREATE INDEX auth_group_name_a6ea08ec_like ON auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_0e939a4f; Type: INDEX; Schema: public; Owner: usimc
--

CREATE INDEX auth_group_permissions_0e939a4f ON auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_8373b171; Type: INDEX; Schema: public; Owner: usimc
--

CREATE INDEX auth_group_permissions_8373b171 ON auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_417f1b1c; Type: INDEX; Schema: public; Owner: usimc
--

CREATE INDEX auth_permission_417f1b1c ON auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_0e939a4f; Type: INDEX; Schema: public; Owner: usimc
--

CREATE INDEX auth_user_groups_0e939a4f ON auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_e8701ad4; Type: INDEX; Schema: public; Owner: usimc
--

CREATE INDEX auth_user_groups_e8701ad4 ON auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_8373b171; Type: INDEX; Schema: public; Owner: usimc
--

CREATE INDEX auth_user_user_permissions_8373b171 ON auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_e8701ad4; Type: INDEX; Schema: public; Owner: usimc
--

CREATE INDEX auth_user_user_permissions_e8701ad4 ON auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: usimc
--

CREATE INDEX auth_user_username_6821ab7c_like ON auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_417f1b1c; Type: INDEX; Schema: public; Owner: usimc
--

CREATE INDEX django_admin_log_417f1b1c ON django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_e8701ad4; Type: INDEX; Schema: public; Owner: usimc
--

CREATE INDEX django_admin_log_e8701ad4 ON django_admin_log USING btree (user_id);


--
-- Name: django_session_de54fa62; Type: INDEX; Schema: public; Owner: usimc
--

CREATE INDEX django_session_de54fa62 ON django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: usimc
--

CREATE INDEX django_session_session_key_c0390e0f_like ON django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: registration_site_ensemblemember_b64a62ea; Type: INDEX; Schema: public; Owner: usimc
--

CREATE INDEX registration_site_ensemblemember_b64a62ea ON registration_site_ensemblemember USING btree (entry_id);


--
-- Name: registration_site_entry_da03336b; Type: INDEX; Schema: public; Owner: usimc
--

CREATE INDEX registration_site_entry_da03336b ON registration_site_entry USING btree (usimc_user_id);


--
-- Name: registration_site_piece_b64a62ea; Type: INDEX; Schema: public; Owner: usimc
--

CREATE INDEX registration_site_piece_b64a62ea ON registration_site_piece USING btree (entry_id);


--
-- Name: auth_group_permissions auth_group_permiss_permission_id_84c5c92e_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permiss_permission_id_84c5c92e_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permiss_content_type_id_2f476e4b_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permiss_content_type_id_2f476e4b_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_per_permission_id_1fbb5f2c_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_per_permission_id_1fbb5f2c_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: registration_site_entry b04018850a975f9b9931e2f91aaa34d7; Type: FK CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY registration_site_entry
    ADD CONSTRAINT b04018850a975f9b9931e2f91aaa34d7 FOREIGN KEY (parent_contact_id) REFERENCES registration_site_parentcontact(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_content_type_id_c4bce8eb_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_content_type_id_c4bce8eb_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: registration_site_entry regis_lead_performer_id_40579356_fk_registration_site_person_id; Type: FK CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY registration_site_entry
    ADD CONSTRAINT regis_lead_performer_id_40579356_fk_registration_site_person_id FOREIGN KEY (lead_performer_id) REFERENCES registration_site_person(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: registration_site_charge regist_usimc_user_id_29da227d_fk_registration_site_usimcuser_id; Type: FK CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY registration_site_charge
    ADD CONSTRAINT regist_usimc_user_id_29da227d_fk_registration_site_usimcuser_id FOREIGN KEY (usimc_user_id) REFERENCES registration_site_usimcuser(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: registration_site_entry regist_usimc_user_id_d02e1898_fk_registration_site_usimcuser_id; Type: FK CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY registration_site_entry
    ADD CONSTRAINT regist_usimc_user_id_d02e1898_fk_registration_site_usimcuser_id FOREIGN KEY (usimc_user_id) REFERENCES registration_site_usimcuser(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: registration_site_entry registratio_teacher_id_1d9d7bca_fk_registration_site_teacher_id; Type: FK CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY registration_site_entry
    ADD CONSTRAINT registratio_teacher_id_1d9d7bca_fk_registration_site_teacher_id FOREIGN KEY (teacher_id) REFERENCES registration_site_teacher(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: registration_site_ensemblemember registration_si_entry_id_0572c45f_fk_registration_site_entry_id; Type: FK CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY registration_site_ensemblemember
    ADD CONSTRAINT registration_si_entry_id_0572c45f_fk_registration_site_entry_id FOREIGN KEY (entry_id) REFERENCES registration_site_entry(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: registration_site_piece registration_si_entry_id_8fe11fc9_fk_registration_site_entry_id; Type: FK CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY registration_site_piece
    ADD CONSTRAINT registration_si_entry_id_8fe11fc9_fk_registration_site_entry_id FOREIGN KEY (entry_id) REFERENCES registration_site_entry(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: registration_site_charge registration_si_entry_id_ba328f96_fk_registration_site_entry_id; Type: FK CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY registration_site_charge
    ADD CONSTRAINT registration_si_entry_id_ba328f96_fk_registration_site_entry_id FOREIGN KEY (entry_id) REFERENCES registration_site_entry(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: registration_site_usimcuser registration_site_usimcuser_user_id_2b93b69c_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: usimc
--

ALTER TABLE ONLY registration_site_usimcuser
    ADD CONSTRAINT registration_site_usimcuser_user_id_2b93b69c_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

