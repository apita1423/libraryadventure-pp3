# Library Adventure
Library Adventure is my third project for Code Insitiute. The idea came from always enjoying the thought of jumping into a book that you love and experiencing the world and wonder what it would be like to go on all the adventures that all these main characters go on. 

Text-based adventure have come a long way, but there is something nostalgic when seeing the white blinking button waiting for your next move. So, I combined the two ideas of jumping into a book and going on text-based adventure. 

![Library Adventure Title Image](/assets/images/library_adventure.PNG)

Library Adventure is Live! Visit [Here](). Have a great adventure!

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
    * [Acknowledgments](#acknowledgments)

---

## User Experience

### User Stories
We have always had those stories that we just wanted to jump into and just stay there awhile. Experience what the main character is experiencing. That is what I tried to do with this project.

The story starts with the user in the library, which becomes a bit personal because I ask for their name and it prompts to welcome them to the library. The story continues with a red book (hence the red book ASCII art) and the user picks it up and starts reading and he essentially is transported into the book's world. Here the user is presented with the story and two different situations they can pick from. But, the user has to be careful with what option they choose. It could be the right or wrong answer. But, with every wrong answer there is a second chance for the user to chose the right path. 

---

## Design

### Colour Scheme
I used the Colorama module as a way to colour my text in the Python terminal. The Library Adenture title has stayed white because I wanted the title to pop especially with the black background. The book ASCII art is red due to the story mentioning a red book. "Please enter your name:" is yellow as well as when the user is prompted with "Welcome to the library (name). When the user inputs the wrong answer, the prompt they receive is red. When the user is asked if they want to play again, the "Play Again?" is in green. Game Over is also in red.

### Imagery 
Talking about libraries and books, of course, I wanted to add an image of books. The ASCII book art was a great choice, especially with one book on it's side. It is like that book is the one that catches the players' eyes. 

---

## Features
- Library Adventure Title - Build through ASCII.

![Library Adventure Title](/assets/images/library_adventure.PNG)

- Red book ASCII Art - A red book is mentioned in the story.

![Red books](/assets/images/red_book.PNG)

- Please enter you name prompt - Name is used to welcome the user into the library.

![Welcome to the library (name)](/assets/images/welcome_name.PNG)

- Mysterious User name prompt -  If user does not want to add name.

![Welcome Mysterious User](/assets/images/mysterious_user.PNG)

- Back story to the user in the library and then disappearing into the book. With a yes/no question at the end, which depending on he answer continues the game or goes back to the beginning.

![Start Adventure](/assets/images/adventure_begin.PNG)

- When the user typed "no" in the first question.

![No to wizard's gift](/assets/images/no_gift.PNG)

- If user typed "yes" to the wizard's gift the game starts, which gives the user two options (1 or 2) to chose from. This continues until the ending of the story. If user typed the correct number the storyline continues with two options. 

![Yes to the wizard's gift](/assets/images/choice_options.PNG)

- If, throughout the storyline, the user decides to pick the wrong answer, an Adventure Over! prompt is given and a Play Again option is also given.

![Second chances](/assets/images/wrong_answer.PNG)

- If the user types "no" on the Play Again option, then the user will have a GAME OVER prompt. It will wait a few seconds and restart the game from the beginning. 

![Game over](/assets/images/no_play_again.PNG)

### General features on each page

### Flow Chart
I used [Lucid Chart](https://lucid.app/) to create my story flow for the text-based adventure game. 

![Library Adventure Flow Chart](/assets/images/flowchart.png)

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
- [VSCode](https://code.visualstudio.com/) - Used to write the python code.
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
2. Once set up, a multifactor authentication needs to be approved.
3. On your Dashboard, click on the Create new app button.
4. Now enter a name in the App name. Each name is unique. Once enter, a green checkmark should appear if its valid.
5. Choose a region: United States or Europe (depending on location). Then click on the Create app button.
6. After clicking on the Create app button, the updated Dashboard has tabs listed. Two tabs that needs to be updated is Deploy and Settings.
7. Settings will be first. 
8. Under Settings, choose Congif Vars first. Enter PORT into the key section and 8000 into the value section. 
9. Under Settings, click on Add buildpack. Click on Python --> Saves Changes, then click on nodejs --> Save Changes. They have to be in this order Python then nodejs.
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

![CI Python Linter](/assets/images/python_linter.png)

### Unfixed Bugs
I took the Library Adventure title and book art from ASCII. Both the title and art made it within the 80 col rule, but there were trailing white spaces that I was not able to get rid of. When I tried, it would moved the symbols in different directions. Puting the code through the CI Python Linter, it does show the trailing whitespaces for that area. 

---

## Credits

### Code Used
I found python fun and I would like to continue creating other projects. But, I did have extra help from the people of YouTube.

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
Again, I would like to give thanks to my husband, who continues to encourage me to keep going forward. 

As always, I'm extremely grateful to my mentor Martina who encourages me every step of the way. The best mentor anyone can ask for!