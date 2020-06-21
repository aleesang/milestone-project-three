# Music Library - Milestone Project Three

This project is a "Music Library", which will allow users to add their favourite tunes, so users can share and discover new music. Users can easily add, update, edit or delete songs in the music library.

The aim is to easily share music in one music library with other music lovers. The songs are grouped into "Genres" so it can easily be identified when a user has a specific preference for a particular type of music, or they can simply view and browse all songs in one place.
 
## UX

The website's purpose is to provide a one stop shop for all music lovers who want to discover new songs, or share their favourite songs by linking the songs they add via Spotify. The users are able to easily navigate through the library by clicking on the different genre's, or viewing all songs in the database on one page. It's a simple repository created to meet the purpose of the website.

The target audience for this website are music lovers who want an easy and simple database to discover new music, or share their own recommendations with other music afficianados.

### User Stories
1. As a user, I want to discover new songs and artists
2. As a user, I want to share their favourite songs and artists with other users
3. As a user, I want to find songs in a simple and easy to use database

Links to user stories and wireframes can be found [here.](/UX)

## Features
### Existing Features

#### [Home Page](https://milestone-project-three-final.herokuapp.com/)
This is the landing page for the music library, explaining briefly what to expect from using the website, and displaying the eight different images of that displays the genres of music that users can choose from.


**Genres (Any one of the genres)**
The genre's a user can choose from are:
- **[Chill](https://milestone-project-three-final.herokuapp.com/get_chill)**
- **[Country](https://milestone-project-three-final.herokuapp.com/get_country)**
- **[Folk](https://milestone-project-three-final.herokuapp.com/get_folk)**
- **[Pop](https://milestone-project-three-final.herokuapp.com/get_pop)**
- **[Reggae](https://milestone-project-three-final.herokuapp.com/get_reggae)**
- **[Rock](https://milestone-project-three-final.herokuapp.com/get_rock)**
- **[Urban](https://milestone-project-three-final.herokuapp.com/get_urban)**
- **[Other](https://milestone-project-three-final.herokuapp.com/get_other)**

When a user clicks on any one of the genres, the page will show only songs belonging in that particular genre. On this page, it will show the same information that is shown on **All Songs Page** (see below).

#### [All Songs](https://milestone-project-three-final.herokuapp.com/get_songs)
When users click on this page, they will be able to view all songs added to the music library. The songs are seperated into Materalize cards, and features on each card the following:
- Artist Image
- Genre
- Artist Name
- Song Name
- View Song (in more detail)

#### [View Song](https://milestone-project-three-final.herokuapp.com/show_song/5ee38a068423865c031b0e2d) - (example)
When a user clicks on the View Song button on the song card, the user can see:
- Artist Image
- Genre
- Artist Name
- Song Name
- Spotify Player
- Delete and Edit buttons for whether a user wants to amend existing details or to remove the song from the library.

#### [Edit Song](https://milestone-project-three-final.herokuapp.com/edit_song/5ee38a068423865c031b0e2d) - (example)
Users can edit any of the following details of a song already saved in the music library:
- Genre
- URL of Artist Image
- Album Name
- Song Name
- Artist Name
- Spotify URL

#### [Add Song](https://milestone-project-three-final.herokuapp.com/add_song/)
Users can add any new song to save to the music library with the following required details:
- Genre
- URL of Artist Image
- Album Name
- Song Name
- Artist Name
- Spotify URL

### Features Left to Implement
- Giving users the ability to sort and filter songs on **All Songs Page**

## Technologies Used

The following technologies were used in the making of this project.

- [HTML](https://www.w3schools.com/html/) was used for constructing the base of the project.
- [CSS](https://www.w3schools.com/css/) for simple styling.
- [Materialize CSS](https://materializecss.com/) the main framework used to build the responsive front-end design of the website.
- [JQuery](https://jquery.com) was used to initialise the Materialize CSS framework.
- [Google Fonts](https://fonts.google.com/) used as main fonts on website.
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) is the database used to store the music library.
- [Flask](https://www.fullstackpython.com/flask.html) is the framework that was used to route python functions and link to the html pages.
- [Python](https://www.python.org/) was used to build the functions that rendered the songs from the mongodb database.
- [Visual Studio Code](https://code.visualstudio.com/) was used to predominately build the code on Mac.
- [GitPod](https://www.gitpod.io/) was used in the beginning of the project for code management as it's linked directly in the github repository. Switched to VS Code shortly after due to convenience.
- [GitHub](https://github.com/) was used for version control and repository housing.
- [Heroku](https://heroku.com) was used for the deployment of website.


## Testing
#### Manual Testing
Manual testing conducted were as follows:
- Tested navigation menu and hyperlinks work on every page and through the hamburger menu when screen is re-sized for mobile view.
- Tested CRUD funcationality and ensured the basic functionality was passing correctly in the mongo database
    - **Genre Page** (Any one of the genres) - Made sure that genres were being collected and displayed correctly
    - **All Songs** - Made sure the songs were being sorted by last added, so users could find songs they just added recently and easily
    - **View Song** - When user clicks on View Song Button that they are presented with more information of the song and the spotify music player to play song.
    - **Edit Song** - Made sure that when the user clicks edit, that all current information is displayed in form fields already and the user can simply overwrite the information and click save to submit the changes.
    - **Delete Song** - Made sure that when a user clicks on Delete that a prompt pops up via Modal to confirm they want to remove the song from the library.
    - **Add Song** - When a user clicks Add Song from the navigation menu, that the form is empty and allows users to enter information in the form fields. When trying to submit the form, the user will get an error if any field is left blank. Also will get an error if wrong type of text is being inputted (eg. URL in a Text Field instead of the URL field). If a user is successful, the form routes to All Songs Page where their song appears first in the list.
- Tested the responsiveness of the website on different browsers and devices to ensure the grid system I chose to use via Materialize was responsive at different screen sizes.

#### Technologies Used For Testing
- [HTML Validator](https://validator.w3.org/) found no html errors, but errors pertaining to use of python/flask in code show as errors or warnings in the validator.
- [CSS Validator](https://jigsaw.w3.org/css-validator) found no errors with CSS code. However found 20 warnings for:
    - -moz-transition
    - webkit-transition
    - -o-transition


These are vendor etensions that help support browser compatibility efforts, which will always show as "invalid" on the CSS Validator.
- [pyTest](https://docs.pytest.org/en/stable/getting-started.html) was initially used in the beginning of my project to test app routes and defining variables
- [Repl.It](https://repl.it/)  was used to test and validate my python code during the project.


**Browsers and Devices**
- [Google Chrome](https://www.google.com/chrome/) was used predominately for testing and for Inspecting via Development Tools
- [Mozilla Firefox](https://www.mozilla.org/en-US/exp/) was used for testing only
- [Safari](https://www.apple.com/au/safari/) was used for testing only.
- [Samsung Galaxy S10 5g and S20 Ultra](https://www.samsung.com.au) used to test mobile responsiveness
- [iPad mini](https://www.apple.com/au/ipad-mini/) was used to test alternate device responsiveness.
- [MacBook Pro 13 inch 2017](https://support.apple.com/kb/SP754?locale=en_AU) was the main device used for building the project and testing
- [HP Elitebook 14 inch](https://en.wikipedia.org/wiki/HP_EliteBook) was used as another device to check responsiveness

The main issue I have found with testing responsiveness in particular, was the horizontal card display I chose for the **View Song** page. The image does not stack above the row, but rather stays in the same row and is squashed in mobile view. At this time, it is the only problem I am encountering.


## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.

## Credits
### Code and Inspiration Used from Other Sources
The project used inspiration or code from the below sources, and it's thanks to them I could display and have my website function the way I wanted it to.

- [python-dotenv:](https://pypi.org/project/python-dotenv/)
- [Sort Genre Names:](https://www.w3schools.com/python/python_mongodb_sort.asp) to sort the songs on the Genre Pages by Artist Name.
- [Fix Height of Card:](https://stackoverflow.com/questions/61819829/materialize-grid-columns-overflowing) to display materialize cards all the same size, regardless of content within it.
- [Split and Join string:](https://realpython.com/python-string-split-concatenate-join/)
- [sort all songs page:](https://stackoverflow.com/questions/57778658/typeerror-if-no-direction-is-specified-key-or-list-must-be-an-instance-of-list)

### Content
- Original content was written by me.

### Media
- [Spotify](https://www.spotify.com/au/) - the music player for users to play and link the songs.
- [Google](https://www.google.com.au/) - images of musicians and artists were found here.

### Acknowledgements
A big thanks to the following for their support and guidance on this project.
- **Seun Owonikoko** - Mentor on this project who provided guidance
- **Code Institute** - Re-visited Python modules to help direct me on how to create the functionality of this project.
