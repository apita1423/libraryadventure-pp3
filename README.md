# Library Adventure
Library Adventure is a text-based adventure game. The player is someone visitng the library and notices a book on the shelf. The players start reading and is transported to a far way land where the players meets a wizard. The player is given two choices through the storyline and with every correct answer he is 

Library Adventure is Live!  Visit [Here]().  Have a great adventure!

---

## Table of Contents

* [User Experience](#user-experience-ux)
    * [User Stories](#user-stories)

* [Design](#design)
    * [Colour Scheme](#colour-scheme)
    * [Imagery](#imagery)

* [Features](#features)
    * [Flow Chart](#flow-chart)
    * [General Features](#general-features)
    * [Future Implementation](#future-implementations)

* [Technologies Used](#technologies-used)
    * [Languages Used](#languages-used)
    * [Modules Used](#modules-used)
    * [Libraries and Programs Used](#libraries-and-programs-used)

* [Deployment](#deployment)
    * [Deployment](#deployment-1)

* [Testing](#testing)
    * [Testing Validation](#testing-validation)
    * [Unfixed Bugs](#unfixed-bugs)

* [Credits](#credits)
    * [Code Used](#code-used)
    * [Content](#content)
    * [Media](#media)
    * [Acknowledgments](#acknowledgments)

---

## User Experience

### User Stories


---

## Design

### Colour Scheme
I used the Colorama module as a way to colour my text in the Python terminal. The Library Adenture title has stayed white because I wanted the title to pop especially with the black background. The book ASCII art is red due to the story mentioning a red book. "Please enter your name:" is yellow as well as when the user puts in their name or decides not to. When the user inputs the wrong answer, the prompt they receive is red. When the user is asked if they want to play again, the "Play Again?" is in green. 

### Imagery 
Talking about libraries and books, of course, I wanted to add an image books. The ASCII book art was a great choice, especially with one book on it's side. It is like that book is the one that catches the players eyes. 
---

## Features

### General features on each page

### Flow Chart
I used [Lucid Chart](https://lucid.app/) to create my story flow for the text-based adventure game. 

![Library Adventure Flow Chart](/readme-images/flowchart.png)

### Future Implementations

- Add another adventure to the story. At the end of Library Adventure, there is an option to go on another adventure, but I added that it was still in the middle of brewing. 
- I would also like to experiment with adding different characters to the story. 

---

## Tools and Technologies Used

### Languages Used
- Python 3

### Modules Used
- Time (sleep)
- Sys (typewriter effect)
- Colorama (fore)

### Libraries and Programs Used
- [Codeanywhere](https://app/codeanywhere.com) - Used to write the python code.
- [Github](https://github.com/) - Used to hold my repository. 
- [Git](https://git-scm.com/) - User for version control.
- [ASCII Art Archive](https://www.asciiart.eu/books/books) - Used to create the book art - Initial of the creator was kept with the art (lower right corner).
- [ASCII Art Title](https://patorjk.com/software/taag/#p=display&f=Big&t=%0A) - Used to create the Library Adventure title.
- [Lucid Chart](https://lucid.app) - Used to create the flowchart for the flow of the story. 

---

## Deployment
Library Adventure has been deployed through Heroku.

- Click Here for the live site: [Library Adventure]()

Instructions on how to deploy on [Heroku](https://www.heroku.com):

1. Login to Heroku.
2. Once set up a multifactor authentication needs to be approved.
3. On your Dashboard, click on the Create new app button.
4. Now enter a name in the App name. Each name is unique. Once enter, a green checkmark should appear if its valid.
5. Choose a region: United States or Europe (depending where you are located). Then click on the Create app button.
6. After clicking on the Create app button, the updated Dashboard has a few tabs listed. Two tabs that needs to be updated is Deploy and Settings.
7. Settings will be first. 
8. Under Settings, chose Congif Vars first. Enter PORT into the key section and 8000 into the value section. 
9. Under Settings, click on Add buildpack. Click on Python --> Saves Changes then click on nodejs --> Save Changes. They have to be in that order Python then nodejs.
10. Now head to the Deploy tab. 
11. Select in the Deplyment method: Github. Confirm to connect to Github. 
12. Search for the repository to connect to. [Github Repository - apita1423](https://github.com/apita1423/libraryadventure-pp3).
13. When the repository is chosen, click connect. 
14. Two ways that the project can be deployed: manual or automatic. 
15. If automatic deploy is chosen, it will deploy when the code is pushed. For manual deploy, the Deploy Branch button has to be click for the code that was pushed to be deployed.

---

## Testing

### Testing Validation 
I used the [CI Python Linter](https://pep8ci.herokuapp.com/) for test validation.

![CI Python Linter](/readme-images/python_linter.png)

### Unfixed Bugs
I took the Library Adventure title and book art from ASCII. Both the title and art made it within the 80 col rule, but there were trailing white spaces that I was not able to get rid off. When I tried it moved the symbols in a different directions. Puting it through the CI Python Linter, it does show the trailing whitespaces for that area. 

---

## Credits

### Code Used
Python was fun and I would like to continue creating other projects. But, I did have much help from the people of YouTube.

- Learn Learn Scratch Tutorials helped with the creation of the typewriter effect block of code.

[Learn Learn Scratch Tutorials YouTube](https://www.youtube.com/watch?v=2h8e0tXHfk0&t=134s)

- Bro Code was a awesome source to go over Python. 

[Bro Code Python Course YouTube](https://www.youtube.com/watch?v=XKHEtdqhLK8&t=11415s)

- Tech with Tim gave me the inspiration for a text-based adventure game.

[Tech with Tim YouTube](https://www.youtube.com/watch?v=DLn3jOsNRVE&t=3757s)

- Tech with Tim helped with adding colour to the text with using Colorama.

[Tech with Tim YouTube](https://www.youtube.com/watch?v=u51Zjlnui4Y)

### Content

The Library Adventure story content was thought of by Amanda Pita, but the inspiration for the story came from reading countless fantasy stories. It sometimes helps to be a librarian. 

### Acknowledgments
Again, I would like to give thanks to my husband. Who continues to encourage me to keep going forward. 

As always, I'm extremely grateful to my mentor Martina who encourages me. The best mentor anyone can ask for!