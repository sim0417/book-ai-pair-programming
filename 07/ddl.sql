-- 학생 테이블
CREATE TABLE Students (
	student_id INT PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	grade INT NOT NULL CHECK (grade BETWEEN 1 AND 6),
	class INT NOT NULL,
	teacher_id INT,
	FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id)
);

-- 선생님 테이블
CREATE TABLE Teachers (
	teacher_id INT PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	subject_id INT,
	FOREIGN KEY (subject_id) REFERENCES Subjects(subject_id)
);

-- 과목 테이블
CREATE TABLE Subjects (
	subject_id INT PRIMARY KEY,
	name VARCHAR(50) NOT NULL
);

-- 반 테이블
CREATE TABLE Classes (
	class_id INT PRIMARY KEY,
	grade INT NOT NULL CHECK (grade BETWEEN 1 AND 6),
	class_number INT NOT NULL,
	teacher_id INT,
	FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id)
);

-- 과목 데이터 삽입
INSERT INTO Subjects (subject_id, name) VALUES
(1, '수학'),
(2, '국어'),
(3, '영어'),
(4, '체육'),
(5, '음악'),
(6, '과학'),
(7, '사회'),
(8, '도덕');