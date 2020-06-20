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

#### Home Page
This is the landing page for the music library, explaining briefly what to expect from using the website, and displaying the 8 different images of genres of music that users can choose from.

#### Genre Page (Any one of the genres)
When a user clicks on any one of the genres, the page will show only songs that belong in that particular genre. On this page, it will show the same information that is shown on **All Songs Page** (see below).

#### All Songs
When users click on this page, they will be able to view all songs added to the music library. The songs are seperated into Materalize cards, and features on each card:
- Artist Image
- Genre
- Artist Name
- Song Name
- View Song (in more detail)

#### View Song
When a user clicks on the View Song button on the song card, the user can see:
- Artist Image
- Genre
- Artist Name
- Song Name
- Spotify Player
- Delete and Edit buttons for whether a user wants to amend existing details or to remove the song from the library.

#### Edit Song
Users can edit any of the following details of a song already saved in the music library:
- Genre
- URL of Artist Image
- Album Name
- Song Name
- Artist Name
- Spotify URL

#### Add Song
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

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
    - HTML was used for constructing the base of the project
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
    - CSS for simple styling
- [Materialize CSS](https://materializecss.com/)
    - The main framework used to build responsive front-end design of the website.
- [JQuery](https://jquery.com)
    - Was used to initialise the Materialize CSS framework

- [Visual Studio Code](https://code.visualstudio.com/)
    - Project was built predominately on VS Code for Mac
- [GitHub](https://github.com/)
    - Used for housing repository and version control

- [Google Chrome](https://www.google.com/chrome/)
    - Used for browser and dev tools
- [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/new)
    - Used for testing

## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X
