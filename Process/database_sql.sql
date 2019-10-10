CREATE DATABASE teste;
CREATE TABLE rule (id serial primary key, rule varchar (500));

INSERT INTO rule (rule) VALUES('If temp > 30: print("entrou no if") else: print("nops")');

UPDATE rule SET rule='if #c9e28736-7217-47ed-b9e5-5dd6bc96d3a0 > 30: print("entrou no if") \n else: print("nops")';





INSERT INTO publicacoes (datacoleta, valorcoletado, sensor_uuid) VALUES('2019-09-23 10:22:22', '50', '3bc35657-e010-4316-a7b8-b050692c7de9');

INSERT INTO sensores (uuid, nome) VALUES('3bc35657-e010-4316-a7b8-b050692c7de9', 'Sensor_2');

