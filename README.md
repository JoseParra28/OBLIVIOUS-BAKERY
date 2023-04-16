# Oblivious bakery

 ## Oblivious bakery, is a fictional bakery website. The signature of this business is that when am user places an order, they get a complimentary pastry, but they won't find out until they receive it, hense the name Oblivious 

[Live link to website here](https://oblivious-bakery.herokuapp.com/)

---

## CONTENTS

* [User Experience](#user-experience-ux)
  * [User Stories](#user-stories)

* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Images](#images)
  * [Wireframes](#wireframes)

* [Features](#features)
  * [Future Implementations](#future-implementations)
  * [Accessibility](#accessibility)

* [Technologies and Languages Used](#technologies-used)
  * [Database design](#database-design)

---

## User Experience (UX)
I wanted to keep the design quite simple on this site so as to not distract the user. I used the main linear gradient colour throughout the site to establish a brand with oblivious. The off-white colour I used for my background look and the 
dark-gray for my font color was used to keep it simple but appealing.

### Colour Scheme

| HEX            | Placemnet.    |
| -------------  | ------------- |
| `#f5f5f5`      |Backgound color|
| `#424040`      | Font color    |
|     Linear-gradient colors     |
|                |               
| `#782b25`      | Falu red
| `#a23930`      | Auburn
| `#872b20`      | Burnt umber
| `#d9402f`      | Chilli red
| `#61111f`      | Chocolate cosmos
| `#6a1818`      | Rosewood

I used [coolors.co](https://coolors.co/) to generate my colour palette.

<img src="food/static/css/readme-img/color-pallet.jpg" alt="color-pallete">

I've used CSS :root variables to easily update the global colour scheme by changing only one value, instead of everywhere in the CSS file.
I have also set the values of h1, h2, h3, p, and button values at the beginning of the main css page to avoid rewriting them.
I created 4 css files to keep the code more organised. These being MAIN, COLORS, MENU, FORMS.css.

<img src="food/static/css/readme-img/root.jpg" alt="color-root">

## Typography

- Lato
- Sans-serif 
- Font awsome for icons

## Images
### Logo
Site's logo was created by myself using photoshop.
<img src="food/static/images/oblivious-logo.jpg" alt="logo">

Images were carefully selected to reflect the purpose of this site. 
menu images were attached to it's respective model and item. I have used [Cloudinary](https://cloudinary.com/ip/gr-sea-gg-brand-home-base?utm_source=google&utm_medium=search&utm_campaign=goog_selfserve_brand_wk22_replicate_core_branded_keyword&utm_term=1329&campaignid=17601148700&adgroupid=141182782954&keyword=cloudinary&device=c&matchtype=e&adposition=&gclid=CjwKCAjwue6hBhBVEiwA9YTx8P-hLvbb_KcqF4Bpd047hJ-hJhBm6HgQxVqJVLussoHWF4oyXnSv8BoCFpYQAvD_BwE) to add custom images to the each item.

## User Stories

### New Site Users
- As a new site user, I would like to clearly see the site's purpose, so that I can decide whether or not to sign up. (MUST HAVE)
- As a new site user, I would like to sign up for the site and create an account, so that I can create my profile and start ordering from the site. (MUST HAVE)

### Registered Users
- As a registered user, I would like to log in to my account, so that I can access the site. (MUST HAVE)
- As a registered user, I would like to log out of my account, so that I can end my session on my current device. (MUST HAVE)
- As a registered user, I would like to create a new review, so that I can share my thoughts with other customers. (MUST HAVE)
- As a registered user, I would like to delete my review, so that I can remove content that I no longer want published. (MUST HAVE)
- As a registered user, I would like to easily navigate the site, so that I can access what I need at the click of a button. (MUST HAVE)
- As a registered user, I would like to reset my password if I forget it, so that I can regain access to my account. (SHOULD HAVE)

# Wireframes

<details>
<summary> drodm</summary>
<img src="food/static/images/readme-img/root.jpg" alt="color-root">

</details>


--- 
# Features 
This site was created specifically for an intuitive navigation. With clear pictures, description of the bussiness and its staff to add a personal touch to it. 
## Existing Features
  - Landing Page

This is the page a user lands on when arriving at the site for the first time or before they've logged in if they don't have an active session. It welcomes them to the site and gives them a brief description of the company as well as staff. If the user is logged in they will get an indication that they are by having the logout button in the navigation bar.
<img src="food/static/css/readme-img/color-pallet.jpg" alt="color-pallete">

  -  About section
The about section is found in the home page, desided to do this instead of creating a new page all together.

  - Review section 
The review section can be found right under the About section, this is where users can write a review, edit and delete. Only authenticated can write revies, not account holders with be able to see the review but not who wrote them to protect their identity.

  - Meet the team section
This is where users can meet the team, and read a little bit about their background.  

  - Footer
The footer contains future links such as career etc. It will also contain contact information.

  - Menu
The menu contains a brief description of the company’s menu as well as manu cards with the description of the item and a button to access the add items page. 

  - Cakes, Pies, Donuts
With a model for each item users can add the items of their choice and the size of their choice,they can browse through the site and add the items they want to the basket-preview and they will also be able to remove the item if they wish. The `check out` button with brinf them to the submit order page. 

  - Basket 
Here users can see what they have added and what they will be purchasing, they can also delete any item that they added if they change their mind. They can also leave an note to customise their order a bit more.

  - Login
Users can login if they have an accound with us, if not, they will have a button to sign up that will redirect them to signup form.

  - Signup
User can create an account if they don't have one with us. They need a username, e-mail, name, password and rewrite password. The form was done with Django's NewUserForm so that that they enter a strong password. Their data will be stored in the database.

  - Success page
After submiting their order users are redirected to the susscess page. Here they can either go back home of logout.

# Future implementations

  - Full payment system 
  - Change password
  - Allow the user to add an image to their account
  - Review likes

# Accessibly 
kfkfkffk

# Technologies and Languages Used
- [HTML](https://en.wikipedia.org/wiki/HTML)used for the main site content.
- [CSS](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [CSS :root](https://www.w3schools.com/css/css3_variables.asp)variables used for reusable styles throughout the site.
- [Bootstrap](https://getbootstrap.com/) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [Javascript](https://www.javascript.com/) used for user interaction on the site for automatically closing Django Messages and to handle the notification dropdown and notification delete functions.
- [Python](https://www.python.org/) used as the back-end programming language.
- [Git](https://git-scm.com/) Git used for version control. (git add, git commit, git push)
- [GitHub](https://github.com/) used for secure online code storage.
- [Gitpod](https://gitpod.io/workspaces) used as a cloud-based IDE for development.
- [Django](https://www.djangoproject.com/) used as the Python framework for the site.
- [PostgreSQL](https://www.postgresql.org/) used as the relational database management.
- [ElephantSQL](https://www.elephantsql.com/) used as the Postgres database.
- [Heroku](https://dashboard.heroku.com) used for hosting the deployed back-end site.
- [Cloudinary](https://cloudinary.com/) used for online static file storage.
- [Adobe Photoshop](https://www.adobe.com) to create the logo
- [Lucidchart](https://www.lucidchart.com) used to create the database design

# Database Design
I created an entity relationship diagram using Diagrams.net. This helped me to visualize the relationships between my data structures and made the development process easier as I had everything mapped out in front of me for reference to avoid having to reference each models.py file individually.



