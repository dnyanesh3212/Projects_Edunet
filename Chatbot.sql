-- 1. Create the Database
CREATE DATABASE IF NOT EXISTS chatbot_app;
USE chatbot_app;

------------------------------------------------------------
-- 2. Create the Users Table (Stores user details)
------------------------------------------------------------
DROP TABLE IF EXISTS Users;
CREATE TABLE Users (
  user_id INT AUTO_INCREMENT PRIMARY KEY,
  user_name VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

------------------------------------------------------------
-- 3. Create the Ai_Models Table (Stores AI model integration details)
------------------------------------------------------------
DROP TABLE IF EXISTS Ai_Models;
CREATE TABLE Ai_Models (
  model_id INT AUTO_INCREMENT PRIMARY KEY,
  version VARCHAR(50) NOT NULL,
  name VARCHAR(100) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

------------------------------------------------------------
-- 4. Create the Conversations Table (Logs each conversation session)
------------------------------------------------------------
DROP TABLE IF EXISTS Conversations;
CREATE TABLE Conversations (
  conversation_id INT AUTO_INCREMENT PRIMARY KEY,
  model_id INT NOT NULL,
  user_id INT NOT NULL,
  start_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  end_time TIMESTAMP NULL,
  FOREIGN KEY (model_id) REFERENCES Ai_Models(model_id) ON DELETE CASCADE,
  FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
);

------------------------------------------------------------
-- 5. Create the Messages Table (Stores messages for each conversation)
------------------------------------------------------------
DROP TABLE IF EXISTS Messages;
CREATE TABLE Messages (
  message_id INT AUTO_INCREMENT PRIMARY KEY,
  conversation_id INT NOT NULL,
  message TEXT NOT NULL,
  send_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  counter INT DEFAULT 1,
  response_id INT,  -- Optional link to a response (if available)
  FOREIGN KEY (conversation_id) REFERENCES Conversations(conversation_id) ON DELETE CASCADE
);

------------------------------------------------------------
-- 6. Create the Responses Table (Stores responses for messages)
------------------------------------------------------------
DROP TABLE IF EXISTS Responses;
CREATE TABLE Responses (
  response_id INT AUTO_INCREMENT PRIMARY KEY,
  conversation_id INT NOT NULL,
  message_id INT NOT NULL,
  response TEXT NOT NULL,
  receive_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (conversation_id) REFERENCES Conversations(conversation_id) ON DELETE CASCADE,
  FOREIGN KEY (message_id) REFERENCES Messages(message_id) ON DELETE CASCADE
);

------------------------------------------------------------
-- 7. Create the Query_Pattern Table (Logs query patterns)
------------------------------------------------------------
DROP TABLE IF EXISTS Query_Pattern;
CREATE TABLE Query_Pattern (
  response_id INT NOT NULL,
  conversation_id INT NOT NULL,
  message_id INT NOT NULL,
  counter INT DEFAULT 1,
  PRIMARY KEY (response_id, conversation_id, message_id),
  FOREIGN KEY (response_id) REFERENCES Responses(response_id) ON DELETE CASCADE,
  FOREIGN KEY (conversation_id) REFERENCES Conversations(conversation_id) ON DELETE CASCADE,
  FOREIGN KEY (message_id) REFERENCES Messages(message_id) ON DELETE CASCADE
);


-- Insert Users
INSERT INTO Users (user_name, email, phone) VALUES
('Alice Johnson', 'alice@example.com', '1234567890'),
('Bob Smith', 'bob@example.com', '9876543210'),
('Charlie Davis', 'charlie@example.com', '5556667777'),
('David Miller', 'david@example.com', '4445556666'),
('Emma Wilson', 'emma@example.com', '3332221111'),
('Frank Harris', 'frank@example.com', '7778889999'),
('Grace White', 'grace@example.com', '1112223333'),
('Hannah Scott', 'hannah@example.com', '9998887777'),
('Ian Brown', 'ian@example.com', '6665554444'),
('Jack Lee', 'jack@example.com', '2223334444');

-- Insert AI Models
INSERT INTO Ai_Models (version, name, description) VALUES
('1.0', 'ChatGPT', 'AI chatbot for text-based conversations'),
('2.0', 'BardAI', 'Enhanced AI chatbot with contextual understanding'),
('1.1', 'Gemini', 'Smart conversational AI for businesses'),
('3.0', 'ClaudeAI', 'Advanced AI for deep learning conversations'),
('2.5', 'DialogFlow', 'AI for voice and chat applications'),
('1.2', 'Siri', 'AI assistant for Apple devices'),
('1.3', 'Alexa', 'Voice-enabled AI assistant'),
('4.0', 'DeepChat', 'AI specialized in complex discussions'),
('3.1', 'Cortana', 'Microsoft’s AI assistant'),
('2.1', 'Watson', 'IBM’s AI for enterprise solutions');

-- Insert Conversations
INSERT INTO Conversations (model_id, user_id, start_time, end_time) VALUES
(1, 1, NOW(), NULL),
(2, 2, NOW(), NULL),
(3, 3, NOW(), NULL),
(4, 4, NOW(), NULL),
(5, 5, NOW(), NULL),
(6, 6, NOW(), NULL),
(7, 7, NOW(), NULL),
(8, 8, NOW(), NULL),
(9, 9, NOW(), NULL),
(10, 10, NOW(), NULL);

-- Insert Messages
INSERT INTO Messages (conversation_id, message) VALUES
(1, 'Hello, how are you?'),
(2, 'What is the weather like today?'),
(3, 'Tell me a joke.'),
(4, 'Can you recommend a book?'),
(5, 'How does machine learning work?'),
(6, 'What are the benefits of AI?'),
(7, 'Can you translate this sentence?'),
(8, 'What is the capital of France?'),
(9, 'Who won the last World Cup?'),
(10, 'Tell me about black holes.');

INSERT INTO Messages (conversation_id, message) VALUES (11, 'Can you recommend a book?');

-- Insert Responses
INSERT INTO Responses (conversation_id, message_id, response) VALUES
(1, 1, 'I am good! How can I assist you?'),
(2, 2, 'The weather is sunny today.'),
(3, 3, 'Sure! Why did the chicken cross the road?'),
(4, 4, 'I recommend "The Alchemist" by Paulo Coelho.'),
(5, 5, 'Machine learning works by training models on data.'),
(6, 6, 'AI helps in automation, efficiency, and data analysis.'),
(7, 7, 'Sure! "Hello" in French is "Bonjour".'),
(8, 8, 'The capital of France is Paris.'),
(9, 9, 'Argentina won the last FIFA World Cup.'),
(10, 10, 'Black holes are regions of space with intense gravity.');


-- Insert Query Patterns
INSERT INTO Query_Pattern (response_id, message_id, conversation_id, counter) VALUES
(1, 1, 1, 5),
(2, 2, 2, 3),
(3, 3, 3, 7),
(4, 4, 4, 2),
(5, 5, 5, 6),
(6, 6, 6, 4),
(7, 7, 7, 5),
(8, 8, 8, 8),
(9, 9, 9, 9),
(10, 10, 10, 10);



-- 1. Get All Users
SELECT * FROM Users;

-- 2. Get Conversations and Their Users
SELECT c.conversation_id, u.user_name, c.start_time 
FROM Conversations c 
JOIN Users u ON c.user_id = u.user_id;


-- 3. Get All Messages for a Specific Conversation
SELECT m.message_id, m.message, m.send_timestamp 
FROM Messages m 
WHERE m.conversation_id = 1;


-- 4. Find Frequently Asked Queries
SELECT qp.response_id, qp.message_id, qp.counter, m.message  
FROM Query_Pattern qp  
JOIN Messages m ON qp.message_id = m.message_id  
ORDER BY qp.counter DESC  
LIMIT 5;