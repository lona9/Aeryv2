CREATE TABLE IF NOT EXISTS languages (
  GuildID VARCHAR PRIMARY KEY,
  GuildLang VARCHAR DEFAULT "SP",
  GuildName VARCHAR,
  GuildSize VARCHAR
);

CREATE TABLE IF NOT EXISTS logs (
  EventDate DATE,
  GuildID VARCHAR,
  GuildName VARCHAR,
  Command VARCHAR,
  Arguments VARCHAR DEFAULT "None"
);
