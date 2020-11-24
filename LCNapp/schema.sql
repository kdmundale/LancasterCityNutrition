DROP TABLE IF EXISTS has_had;
DROP TABLE IF EXISTS daily;
DROP TABLE IF EXISTS shakes;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email text UNIQUE NOT NULL,
    password bytea NOT NULL,
    first_name text,
    last_name text,
    dob date,
    last_login date,
    total_login bigint,
    role varchar(7) NOT NULL CHECK (role IN ('admin', 'member','guest','store'))
);

CREATE TABLE shakes (
  id SERIAL PRIMARY KEY,
  name text UNIQUE NOT NULL,
  shake_group int NOT NULL,
  CHECK (shake_group BETWEEN 1 AND 10),
  description text UNIQUE NOT NULL,
  suggestions text,
  available boolean NOT NULL
);

CREATE TABLE has_had (
  id SERIAL PRIMARY KEY,
  user_id bigint NOT NULL,
  shake_id bigint NOT NULL,
  rating int,
  CHECK (rating BETWEEN 1 AND 5),
  comment text,
  this_shake int
);

ALTER TABLE has_had
  ADD CONSTRAINT had_shake FOREIGN KEY (shake_id)
    REFERENCES shakes(id);

ALTER TABLE has_had
  ADD CONSTRAINT had_user FOREIGN KEY (user_id)
    REFERENCES users(id);

CREATE TABLE daily (
  id SERIAL PRIMARY KEY,
  day date NOT NULL,
  shake_id bigint NOT NULL,
  daily_total int NOT NULL
);

ALTER TABLE daily
  ADD CONSTRAINT daily_shake FOREIGN KEY (shake_id)
    REFERENCES shakes(id);
