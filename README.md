# CS410_Final_Project
Backend of CS410 Spring 2019 Final Project

Architecture:

Front End (ReactJs)
  Upload pdf file and send it to backend (optional)
  User able to enter queries and keywords
  Simple UI Design
Back End (Python Flask)
  File storage
  Either Use illinois Box api: https://github.com/box/box-python-sdk (hard)
  OR Directly save the pdf file to python API (easy)
  Store parsed file information (e.g name, phone number)
  Ranking systems
  Use the top ranking function of MP-2
  Return the result of ranking to front end:
  Name of the candidate
  Link of pdf file of that candidate
