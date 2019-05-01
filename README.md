# CS410_Final_Project
CS410 Spring 2019 Final Project Resume Ranker
Team members: Peng Gu, Jiawen Wu, Jinlin Xu, Yujie Shao, Kehan Li

## Usage of the application: 

Go to our website at [https://yujies1218.github.io/cs410final-project-front-end/](https://yujies1218.github.io/cs410final-project-front-end/). We have more than 20 resumes from candidates majoring in financial engineering, computer engineering, computer science and other majors. Enter keywords about the job position in the search box, then select the number of most qualified candidates you want to display. Click search button, and you will see names of top candidates and links to their PDF resumes. Candidates are displayed based on how much their resumes match the entered keywords. You can click the link to candidates' resumes to take a closer look at their experience and background. 

## Implementation of the application:

### Front end: 

We use React to develop front end user interface. We got feedback about the design and user interface of our website from our peers and made changes accordingly. 

### Back end:

We use Flask as our web framework for back end. We save resumes of candidates on Heroku cloud application platform. We developed a ranking function to rank candidates based on how much their resumes match keywords entered by the employer. Resumes are parsed into json files for ranking. 

