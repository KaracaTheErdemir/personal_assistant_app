CREATE TABLE friends (
    friend_id SERIAL PRIMARY KEY,
    name CHAR(255),
    full_name CHAR(255),
    sex CHAR(10),
    profession CHAR(255),
    meet_score INT,
    last_seen DATE,
    friends_since INT
);

CREATE TABLE meetings (
    meeting_id SERIAL PRIMARY KEY,
    people CHAR(255),
    place CHAR(255),
    category CHAR(255),
    meeting_date DATE,
    duration CHAR(50),
    note CHAR(255)
);

CREATE TABLE todos (
    todo_id SERIAL PRIMARY KEY,
    label CHAR(255),
    priority INT,
    create_date DATE,
    deadline DATE
);

CREATE TABLE expenses (
    expense_id SERIAL PRIMARY KEY,
    category CHAR(255),
    label CHAR(255),
    cost FLOAT,
    currency CHAR(10),
    create_date DATE
);

CREATE TABLE habits (
    habit_id SERIAL PRIMARY KEY,
    category CHAR(255),
    label CHAR(255),
    priority INT,
    currently_tracked BOOLEAN,
    track_interval CHAR(255),
    performance int,
    create_date DATE
);
