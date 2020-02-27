BEGIN TRANSACTION;
CREATE TABLE users(id INTEGER PRIMARY KEY, username text, email text ,phone text, website text, regdate text);
INSERT INTO "users" VALUES(1,'leegunj','hanzen@naver.com','010-0000-0000','hoho@mdmd.com','2020-02-27 17:09:52');
INSERT INTO "users" VALUES(2,'park','hanzen@naver.com','010-0000-0000','hoho@mdmd.com','2020-02-27 17:12:29');
INSERT INTO "users" VALUES(3,'kim','hanzen@naver.com','010-0000-0000','hoho@mdmd.com','2020-02-27 17:12:39');
INSERT INTO "users" VALUES(4,'ryo','hanzen@naver.com','010-0000-0000','hoho@mdmd.com','2020-02-27 17:16:21');
INSERT INTO "users" VALUES(5,'go','hanzen@naver.com','010-0000-0000','hoho@mdmd.com','2020-02-27 17:16:32');
COMMIT;
