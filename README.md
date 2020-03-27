# RASA Chatbot

This chatbot will answer the questions related books and authors. 
For now only two types of questions are covered.

1. Author of the particular book
2. All the books written by particular author


## DATA

I have setup MySQL server on my localhost.

- Database - books
- Table    - books
    1. id: unique id (int: primary key)
    2. name: name of the book (varchar)
    3. author: name of the author (varchar)
    
As of now, Table has only 10 entries and 
likely to add more data and more complex table structure in future


## Steps

- git clone https://github.com/sociopath00/BookBot

- Install the requirements
    `pip install requirements.txt`
    
    Note: I would recommend creating a new environment.
    
- Train the model 
    `rasa train`
    
- Start action server
    `rasa run actions`
    
- Start RASA server
    `rasa run --endpoints endpoints.yml`
    
- Test the responses
    `python talk.py`
    
    Note: change the question and try again OR 
          you can test the responses using POSTMAN
          
