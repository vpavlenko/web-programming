CREATE TABLE "lessons_lesson" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" text NOT NULL, "content" text NOT NULL);
CREATE TABLE "lessons_problem" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" text NOT NULL, "statement" text NOT NULL, "lesson_id" integer NOT NULL REFERENCES "lessons_lesson" ("id"));
CREATE TABLE "lessons_test" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "number" integer NOT NULL UNIQUE, "input" text NOT NULL, "answer" text NOT NULL, "problem_id" integer NOT NULL REFERENCES "lessons_problem" ("id"));
CREATE TABLE "lessons_submission" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "code" text NOT NULL, "problem_id" integer NOT NULL REFERENCES "lessons_problem" ("id"), "info" text NOT NULL, "status" text NOT NULL);
CREATE INDEX "lessons_problem_55174b7b" ON "lessons_problem" ("lesson_id");
CREATE INDEX "lessons_test_919b1d80" ON "lessons_test" ("problem_id");
CREATE INDEX "lessons_submission_919b1d80" ON "lessons_submission" ("problem_id");

INSERT INTO "lessons_lesson" VALUES(1,'Арифметические операции','В Питоне сложить два числа можно так:
<pre>
def action(a, b):
    return a + b
</pre>');

INSERT INTO "lessons_problem" VALUES(1,'Сложение трёх чисел','В функцию подаются три числа. Напишите тело функции так, чтобы оно возвращало их сумму.',1);

INSERT INTO "lessons_test" VALUES(1,1,'(2, 3, 4)','9',1);
INSERT INTO "lessons_test" VALUES(2,2,'(10, -100, 1)','-89',1);

INSERT INTO "lessons_submission" VALUES(7,'def action(a, b, c):
    return a + b',1,'','WA');
INSERT INTO "lessons_submission" VALUES(9,'def action(a, b, c):
    return a + b + c',1,'','OK');
INSERT INTO "lessons_submission" VALUES(12,'def action(...):
    return ...
    ',1,'invalid syntax (<string>, line 1)','RE');
