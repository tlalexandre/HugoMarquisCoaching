# Hugo-Marquis-Coaching-PP4

[(Developer: Darrach Barneveld)](https://github.com/tlalexandre)

[Link to deployed site](https://hugo-marquis-297dbddc34dd.herokuapp.com/)

<hr>
Hugo Marquis Coaching is a website for a french sports coach, to allow him to post articles, let people know when he holds classes, and allow clients to book sessions with him.

![CoolCoders Image](./documentation/images/HomePage.png)

# Table Of Content

- [User Experience](#user-experience)
  - [User Stories](#user-stories)
  - [Site Goals](#site-goals)
  - [Scope](#scope)
- [Design](#design)
  - [Colour Scheme](#colour-scheme)
  - [Database Schema](#database-schema)
  - [Fonts](#fonts)
  - [Wireframes](#wireframes)
  - [Agile Methodology](#agile-methodology)
    - [Overview](#overview)
    - [EPICS(Milestones)](#epics---milestones)
    - [User Stories Issues](#user-stories---issues)
    - [MoSCoW prioritization](#moscow-prioritization)
    - [GitHub Projects](#github-projectskanban)
    - [Late Design Changes](#late-design-changes)
- [Features](#features)
  - [Navigation Header](#navigation-header)
  - [Footer](#footer)
  - [Home Page](#home-page)
  - [News Page](#post-detail-page)
  - [Bookings Page](#bookings-page)
  - [Edit/Add News Page](#addedit-news-page)
  - [Edit Classes Page](#edit-classes-page)
  - [Sign Up Page](#sign-up-page)
  - [Sign In Page](#sign-in-page)
  - [Sign Out Page](#sign-out-page)
  - [News Preview Card](#news-preview-card)
  - [Notification Messages](#notification-messages)
  - [Confirmation Modal](#confirmation-modal)
  - [Comment Form](#comment-form)
  - [Pending Post](#pending-post)
  - [Pending Private Session](#pending-private-session)
  - [Error Pages](#comment-form)
- [Testing](#testing)
- [Bugs](#bugs)
- [Technologies and Languages](#technologies-and-languages)
  - [Languages](#languages-used)
  - [Python Modules](#python-modules-imported)
  - [Technologies and programs](#technologies-and-programs)
- [Deployment](#deployment)
  - [Pre Deployment](#pre-deployment)
  - [Deploying on Heroku](#deploying-on-heroku)
  - [Fork the Repository](#fork-the-repository)
  - [Clone the Repository](#clone-the-repository)
  - [Run the Repository Locally](#run-the-repository-locally)
- [Credits](#credits)
  - [Content](#content)
  - [Media](#media)
  - [Code](#code)
  - [Acknowledgements](#acknowledgements)

## User Experience

### User Stories

#### New User

1. As a user I want the website to be responsive so I can view it on multiple devices [#23](https://github.com/tlalexandre/HugoMarquisCoaching/issues/23)
2. As a User I can intuitively navigate through the website so that I can view all content with ease. [#24](https://github.com/tlalexandre/HugoMarquisCoaching/issues/24)
3. As a User, I can create an account so that I can comment, like and book a coaching with the coach. [#6](https://github.com/tlalexandre/HugoMarquisCoaching/issues/6)
4. As a User, I can log out so that I can secure my account from potential hacks [#10](https://github.com/DarrachBarneveld/CoolCoders-PP4/issues/10)
5. As a User, I can post an article so that I can share my insights with the community. [#25](https://github.com/tlalexandre/HugoMarquisCoaching/issues/25)
6. As a User, I can view content on the home page so that I can learn more about the coach and his methods. [#26](https://github.com/tlalexandre/HugoMarquisCoaching/issues/26)
7. As a User, I can view a selected article with its comments so that I can explore in-depth content and engage with the community. [#3](https://github.com/tlalexandre/HugoMarquisCoaching/issues/3)
8. As a User I can see notification messages when performing CRUD operations or login/logout, signup so that I can stay informed about the outcome of my actions. [#27](https://github.com/tlalexandre/HugoMarquisCoaching/issues/27)
9. As a User, I want to view comments on an individual post so that I can see the discussions going on a particular topic. [#5](https://github.com/tlalexandre/HugoMarquisCoaching/issues/5)
10. As a User, I want to be able to see the differents classes offered by the coach, so that I can choose the one that fits me best. [#13](https://github.com/tlalexandre/HugoMarquisCoaching/issues/13)
11. As a User, I can click on the footer contact social links so I can find out more information about the brand [#28](https://github.com/tlalexandre/HugoMarquisCoaching/issues/28)

#### Existing User

1. As a User, I can access my account so that I can create and edit content and view my saved information [#9](https://github.com/DarrachBarneveld/CoolCoders-PP4/issues/9)
2. As a User, I can view my posts that are pending approval on my profile page so that I can track the status of my submitted content. [#45](https://github.com/DarrachBarneveld/CoolCoders-PP4/issues/45)
3. As a User, I can create comments on articles, so that I can engage with the content and share my thoughts. [#7](https://github.com/tlalexandre/HugoMarquisCoaching/issues/7)
4. As a User, I can leave a like on an article, so that I can let others know I appreciate that content. [#8](https://github.com/tlalexandre/HugoMarquisCoaching/issues/8)
5. As a User, I can book private sessions with the coach, so that I can get custom training with the coach. [#12](https://github.com/tlalexandre/HugoMarquisCoaching/issues/12)
6. As a User, I can see if my private sessions have been approved or deleted, so that I can stay aware of my schedule. [#32](https://github.com/tlalexandre/HugoMarquisCoaching/issues/32)
7. As a User, I can join a group class, so that I can take part in group classes led by the coach.[#29](https://github.com/tlalexandre/HugoMarquisCoaching/issues/29)
8. As a User, I can receive notifications about any changes happening with the classes or privates sessions I take part in, so that I always stay informed if any changes happens. [#30] (https://github.com/tlalexandre/HugoMarquisCoaching/issues/30)
9. As a User , I can only see the content of the private sessions I created , so that the privacy and objectives of everyone stays personal.[#31](https://github.com/tlalexandre/HugoMarquisCoaching/issues/31)
10. As a User , I can see the coach's unavailabilities so that I can plan my sessions around those. [#33](https://github.com/tlalexandre/HugoMarquisCoaching/issues/33)
11. As a User, I can contact the coach through the contact form, so that I can ask him any questions .[#34](https://github.com/tlalexandre/HugoMarquisCoaching/issues/34)


#### Website Owner

1. As a Website Owner, I can create news article through the website, so that I can share my latest news with my community.
2. As a Website Owner, I can add images to illustrate my articles, so that I show my community more about the news.
3. As a Website Owner, I can update or delete my article news through the django admin panel, so that I change my opinion about an article and do what I want about it.
4. As a Website Owner, I can create a class in the calendar, so that my clients can see the differents classes I hold.
5. As a Website Owner, I can see a list of the differents participants, so that I can organize my courses in relation.
6. As a Website Owner, I can update a classe, so that I can modify my classes as I need.
7. As a Website Owner, I can notify all my users about any modifications with an automatic email system, so that my clients will never get wrong informations.
8. As a Website Owner, I can accept the private sessions of my clients, so that I can choose which session to take or not.
9. As a Website Owner, I can delete a private session and send an autonatic email, so that I can choose my schedule while still letting the client know.
10. As a Website Owner, I can setup my availabilities, so that I can let my clients know when I'm free or not.
11. As a Website Owner, I can create recurrent classes, so that I can make my schedule weeks ahead.
12. As a Website Owner, I can setup a maximum of participants for each course, so that I can let people know when a course is full or not.


### Site Goals

1. Allow an easy access to sports.
2. Create a community around sports.
3. Create a platform for users to be able to book sports classes, and share about them.
4. Give a useful tool to the coach

### Scope
The project's scope is to create and maintain "Hugo Marquis" an online platform dedicated to Hugo Marquis, sports coach, and his clients. Hugo Marquis will serve as a user-friendly and responsive space for individuals to explore, share, and interact with the coach's content. Development will be assisted by following a number of EPIC stories which will focus on different aspects of the site. The platform will encompass the following key features:

1. [EPIC - Essential Website Features :](https://github.com/tlalexandre/HugoMarquisCoaching/milestone/3) 
  - I set up a Django project to create the project's structure.
  - Database, media storage and email system will be connected to ensure communication, data storage and retrieval.
  - I deployed at early stages of the project to ensure the initial setup is working correctly.
  - The website needs to be responsive, and its design based on wireframes created beforehand.

2. [EPIC - Blog :](https://github.com/tlalexandre/HugoMarquisCoaching/milestone/1)
  - I wanted to have a functioning blog, that includes articles with custom images.
  - I want the ability for each user to be able to comment and like on the article.
  - I wanted to let the admin be able to create articles from the website.
  - Rest of the CRUD operations will be done through the admin platform of the website.

3. [EPIC - Calendar :](https://github.com/tlalexandre/HugoMarquisCoaching/milestone/2)
  - I wanted to set up a calendar that would be easy to use.
  - The first feature of the calendar is the ability for the coach to display his classes.
  - Secondly, the clients are able to book private sessions, as well as joining the coach's classes.
  - Every private session needs to be approved by the coach. 
  - Privacy was one of the main features I wanted with this calendar, so clients can't see the content of other clients , but the coach gets access to every event.
  - The coach has the possibility to setup unavailabilites , to prevent clients to book sessions when he's not free.

4. [EPIC - Communication between coach and clients :](https://github.com/tlalexandre/HugoMarquisCoaching/milestone/4)
  - The website includes a contact form to allow clients to ask questions to the coach.
  - Every modification(update or deletion) of an event (classes or private sessions) will be notified to the clients, to allow them to adapt to the coach schedule.
  - The notification of modification of events is done by email sent automatically to the clients by the website, containing all the essentials informations.
  -Every single action on website, such as connection, signing out or adding an event will create a notification message on the website , to allow users to know that their action has been taken in.


Benefits of key features and the EPIC Milestone Approach:

1. Prioritizing User Needs: The platform places the user's requirements at the forefront, streamlining the browsing experience, available posts creation and user communication on such posts.
2. Streamlined and Easy Navigation: Users can effortlessly move through various website sections, ensuring convenient and hassle-free access. This is performed by using the news page, as well as the calendar.
3. User Analytics: Users gain valuable insights, allowing them to book sessions at ease, as well as letting the coach create his schedule around that tool designed for him.

## Design

The primary design goal of the Hugo Marquis Website was to focus of ease of navigation for users, as well as creating a theme that would fit with the content of the website , Sports . The main purpose was not only the content of the website but the users/community.

The primary objective of our website design was to ensure an incredibly user-friendly and efficient navigation experience. A strong emphasis on user-centricity and content accessibility. This entailed making posts,events and comments easily reachable, thus simplifying the overall navigation process.

I wanted to minimize page transitions and streamline actions by introducing a versatile, reusable confirm-delete modal.

### Colour Scheme

The website adopts a simple and efficient colour theme, remembering sports , and motion. I used 4 colors over the whole website, black , dark gray and yellow. Those colors were chosen with the client beforehand , to bring an energetic , clear and simple interface to the users.

![Colour Scheme](./documentation/images/theme/ColorPalette.png)

### Database Schema

![Database schema](./documentation/images/DatabaseDiagram.png)

### Models

#### Allauth User Model

The User model is an integral component of Django Allauth, featuring pre-established fields as part of its standard configuration. Among these fields are username, email, name, password, and others. This model primarily serves the purpose of user authentication, which is why it is not recommended to make direct alterations to it. Furthermore, the User model is linked to the Profile model through a one-to-one relationship, facilitating the management of user-specific data and interactions.

#### Post Model

The Post Model is the core of the content creation process, where the coach can share his sports knowledge, experiences, and insights. This model includes fields for post content, author, publication date,featured image and engagement metrics such as likes and comments.

#### Comment Model

The Comment Model serves as the foundation for user engagement on the platform, allowing users to interact with posts by sharing their thoughts and feedback. It includes fields for the comment content, author, timestamp, and a foreign key relationship to associated posts.

#### Course Model

The Course Model is used by the coach to allow people to know which classes he holds , allowing them as well to join those course. 
It includes several fields such as name, description , start_time, end_time, location , a maximum number of participants, and last but not least , an option to make the classe recurrent over the next 4 weeks, to simplify planning for the coach.

#### PrivateSession Model

The PrivateSession model is used by the clients of the coach to book private sessions with him. It includes several fields such as name,description,start_time, end_time, location , and a boolean field is_approved to ensure that the coach accepts the session before confirming it.

#### UnavailablePeriod Model

The UnavailablePeriod model allows the coach to setup periods where he will not take any classes or private sessions. It includes a start_time and an end_time as its main fields.

### Fonts

The fonts used in this project are Outfit and ZillaSlab , which compliments the sports design of the website. <br>
![Font](./documentation/images/OutfitFont.png)
![Font](./documentation/images/ZillaSlab.png)

### Wireframes

#### Desktop

<details><summary>Home</summary>
<img src="./documentation/images/HomePageWireframe.png">
</details>
<details><summary>News</summary>
<img src="./documentation/images/NewsPageWireframe.png">
</details>
<details><summary>News Details</summary>
<img src="./documentation/images/NewsDetailsWireframe.png">
</details>
<details><summary>Calendar</summary>
<img src="./documentation/images/CalendarWireframe.png">
</details>
<details><summary>Contact</summary>
<img src="./documentation/images/ContactWireframe.png">
</details>

### Final Result of the website
#### Desktop
##### HomePage
 <video src="./documentation/videos/Hugo Marquis HomePage.mp4" controls title="Title"></video>

### Agile Methodology

#### Overview

This project was developed following agile principles. Employing the agile methodology enabled me to meticulously map out the website's features by crafting user stories, each of which came with defined acceptance criteria and tasks. Grouping each of these stories into EPIC milestones allowed me to focus on the key elements of the site one by one. These elements served to distinctly delineate the necessary prerequisites for the successful implementation of each feature.

#### EPICS - Milestones

Within the Agile methodology framework, user stories are organized into eight EPICS or Milestones. Additionally, there is also additional Milestones known as Error Handling that was created for the sole purpose of handling any errors that came up during testing, development or tweaking site elements with more refactored coded or enchancements.

<details><summary>Milestones</summary>
<img src="./documentation/images/epicmilestones.png">
</details>

#### User Stories - Issues

The user story issue format consists of the user story itself, as well as acceptance criteria and tasks that outline the essential steps for addressing the issue. When possible, during the development process, commit messages are associated with their corresponding issues. This practice ensures the relevance of each commit and also provides a visual representation of the progress made on each project issue. These issues are monitored using milestones, Kanban boards, and other Agile tools.

<details><summary>User Story</summary>
<img src="./documentation/images/userstories.png">
</details>

#### MoSCoW Prioritization

The project employed the "MoSCoW" technique to effectively categorize and prioritize its features and requirements based on their importance. "MoSCoW" stands for "Must have, Should have, Could have, and Won't have," with each category contributing to the organization and prioritization of features. This approach acts as a guiding principle for the development process, ensuring that the most crucial elements are addressed as a top priority.

<details><summary>MoSCoW</summary>
<img src="./documentation/images/moscow.png">
</details>

#### GitHub Projects/Kanban

The project adopted a basic Kanban Board structure, which was divided into columns such as Todo, In Progress and Done. This setup provided a clear and organized way to track the progress of tasks, making it easier to visualize and manage the workflow throughout the development process. The GitHub project Kanban was linked to the repo for consistant reference.

<details><summary>Kanban</summary>
<img src="./documentation/images/kanban.png">
</details>

#### Late Design Changes

In response to user feedback during alpha testing, I made a change to our comment approval process. Initially, all content needed admin approval, which slowed down user interaction. Now, comments are automatically posted, giving users a form of instant CRUD (Create, Read, Update, Delete) functionality for their comments. Posts still require approval, and a "Code of Conduct" explains content guidelines. Harmful comments may be removed, enhancing user interaction and immediacy.

## Features

### Navigation Header

The navigation bar is a consistent element across all pages, designed using Bootstrap and optimized for full responsiveness. The left is centered around navigation of content while the right hand side is related to user authentication. Authenticated users can also see create posts and view profile links while unauthenticated users only see a prompt to login/register.

The mobile version of the navbar has all the content rendered when a hamburger icon is clicked. When clicked a dropdown display is rendered showing all navigation links.

<details><summary>Mobile</summary>
<img src="./documentation/images/features/mobilenav.png">
</details>
<details><summary>Auth</summary>
<img src="./documentation/images/features/navauth.png">
</details>
<details><summary>UnAuth</summary>
<img src="./documentation/images/features/navunauth.png">
</details>

### Footer

The footer is a miniinmalist footer designed to link users to cool coders social links. The link are only for educational purposes as just link to the social platforms base url.

<details><summary>Footer</summary>
<img src="./documentation/images/features/footer.png">
</details>

### Home Page

The Home Hero Section on Cool Coders features carefully curated tech-related content with three components: Popular Posts, highlighting articles with active user comments; Trending Posts, showcasing popular content based on user likes; and Editor's Choice, handpicked by the editorial team. Each post is displayed as a card with a link to the full article, accompanied by engagement metrics like comments and likes. Users can also access the author's profile, promoting community interaction and enhancing the user experience. Additionally, tag links are displayed to showcase posts from various categories, further enhancing content discovery.

<details><summary>Home</summary>
<img src="./documentation/images/features/homepage.png">
</details>

### Categories Page

The Category Page on Cool Coders is a dedicated space where users can explore a comprehensive collection of articles grouped by specific tech-related categories. Each category page is thoughtfully organized, presenting users with a wealth of content tailored to their interests. The articles are neatly paginated, with up to six articles displayed per page for easy navigation and efficient content browsing. This design allows users to delve deeply into the topics that intrigue them most, making it a valuable resource for in-depth exploration of various tech-related subjects within the Cool Coders community.

<details><summary>Categories</summary>
<img src="./documentation/images/features/categories.png">
</details>

### Post Detail Page

The Post Detail Page on Cool Coders is an immersive experience designed to provide users with in-depth access to an article's content and foster engagement. Here's what users can expect on this page:

1. Article Content: The central focus of the page is the article itself. Users can read the full content of the post, gaining insights into the topic, industry trends, or tech-related experiences shared by the author.
2. Comments Section: A dedicated comments section accompanies the article, displaying all user-generated comments related to the post. Users can participate in discussions, share their thoughts, and engage with the Cool Coders community by leaving comments or replies.
3. Comment Form: Below the comments section, a user-friendly comment form is readily available. Users can easily contribute to the conversation by typing and submitting their comments, which will appear alongside existing discussions.
4. Popular Posts in Category: To encourage further exploration within the same category, the page also showcases a selection of popular posts from the related category. This feature helps users discover additional relevant content, offering a seamless navigation experience.

The Post Detail Page serves as a hub for knowledge sharing and community interaction, ensuring that users not only have access to insightful content but can also actively engage, discuss, and explore more related posts within the category.

<details><summary>Post Detail</summary>
<img src="./documentation/images/features/postdetail.png">
</details>

### Profile Page

The Profile Page on Cool Coders is an essential space for users to showcase their tech passions and contributions while also gaining insights into their own engagement within the community. Here's what you'll find on a user's profile:

<details><summary>Profile</summary>
<img src="./documentation/images/features/profile.png">
</details>

#### Profile Info

1. Username, First Name and Last Name: Users' first and last names, adding a personal touch to their profiles.
2. Bio: A brief bio or description, allowing users to share more about themselves, their interests, or their professional background.
3. Email Address: The user's contact information, enabling communication with other community members.
4. Member Since:The date the user joined Cool Coders, providing a sense of their tenure within the community.

#### Post Info

1. Total Posts: The cumulative number of posts by the user.
2. Total Likes: The cumulative number of likes received by the user across all their posts, reflecting their content's popularity.
3. Total Comments: The overall count of comments made on the user's posts, indicating engagement and interaction with their content.
4. Total Favourites: The cumulative number of favourited posts of the user.
5. Posts: A paginated list of all the users posts
6. Favourites: A paginated list of all the users favourite posts

If the user is viewing their own profile, they have the ability to edit their posts and profile information, ensuring their profile remains up-to-date and their posts are well-maintained.
Users can also access their list of favorited posts, making it convenient to revisit their favorite content.

The Profile Page serves as an information-rich hub, where users can introduce themselves, showcase their contributions, and gain insights into their impact within the Cool Coders community. It fosters a sense of belonging and encourages active participation while enabling users to manage their own content and profile details.

### Add/Edit Post Page

The Add/Edit Post Page on Cool Coders is a versatile platform that empowers users to craft and refine their tech-related articles with ease. Here's what this feature offers:

1. Create and Edit Articles: Users can compose new articles or edit existing ones, maintaining control over their content and insights.
2. Title: A clear and captivating title helps users convey the article's main theme, attracting readers and providing a structured entry point.
3. Content: The page provides a dedicated space for users to input the full content of their articles, allowing for in-depth exploration of tech topics.
4. Excerpt: Users can include a concise and engaging excerpt that provides a preview of the article's key points, enticing readers to delve further.
5. Image: The option to upload an image enhances visual appeal and adds context to the article, creating a more engaging reading experience.
   6.Category: Users can assign their articles to specific tech-related categories, ensuring they are appropriately classified and easily discoverable by others.
6. Delete Post Button (Edit Mode): In edit mode, users have the ability to delete their posts using a dedicated "Delete Post" button, granting full control over their content's management.

The Add/Edit Post Page is a user-friendly tool designed to facilitate content creation and refinement, enabling users to share their tech insights and knowledge within the Cool Coders community.

<details><summary>Add/Edit Post</summary>
<img src="./documentation/images/features/addeditpost.png">
</details>

### Edit Profile Page

The Edit User Profile Page on Cool Coders is a user-centric feature that empowers users to manage and customize their personal information seamlessly. Here's what this page offers:

1. Edit User Profile Information: Users can conveniently update their First Name, Last Name, Username, Email, and Bio, ensuring that their profile accurately reflects their identity and interests.
   2.Password Change: This feature allows users to modify their password, enhancing account security and ensuring they maintain control over their login credentials.
2. Account Deletion: For those who choose to do so, the option to delete their account is available, allowing users to exercise control over their Cool Coders membership. Users will be prompted to confirm their action with a modal popup.

The Edit User Profile Page ensures a personalized and adaptable user experience, enabling individuals to make changes to their profile and account settings as needed while prioritizing their data security and personalization options.

<details><summary>Edit Profile</summary>
<img src="./documentation/images/features/editprofile.png">
</details>

### Code of Conduct Page

The Code of Conduct Page on Cool Coders is a fundamental resource that outlines the community's behavioral guidelines and expectations. Here's what this page covers:

1. Understanding Community Rules: Users can review and familiarise themselves with the rules and expectations set forth by Cool Coders. This knowledge is essential for maintaining a positive and respectful online environment.
2. Promoting Respectful Interaction: The code of conduct emphasises the importance of respectful communication and interactions within the Cool Coders community, fostering a welcoming atmosphere.
3. Consequences of Non-Compliance: Users will find information regarding the consequences of not adhering to the established guidelines. This may include warnings, suspensions, or account bans in extreme cases.

The Code of Conduct Page serves as a critical reference point for all members, ensuring a harmonious and inclusive environment within the Cool Coders community.

<details><summary>Code of Conduct</summary>
<img src="./documentation/images/features/codeofconduct.png">
</details>

### Sign Up page

This page comprises a form with fields for entering a username and password. Beneath the form is the sign up button which submits the form. Below the form is a redirect to the register page if the user does not have an account. Click the remember me checkbox to remain logged in as a session.

<details><summary>Sign Up</summary>
<img src="./documentation/images/features/signup.png">
</details>

### Sign In page

It features a form with fields for inputting name, email, username, password, and password confirmation. Underneath the form, there is a link to log in for users with existing accounts, followed by the signup button. After signup, users receive a welcome email at the provided email address and are then directed to the profile page update form, where they can personalise their profiles.

<details><summary>Sign In</summary>
<img src="./documentation/images/features/signin.png">
</details>

### Sign out page

Upon clicking the "log out" link in the navigation, users are directed to a confirmation page. This page includes a cautionary message and two buttons: one for returning and one for logging out.

<details><summary>Sign Out</summary>
<img src="./documentation/images/features/signout.png">
</details>

### Article Preview Card

The Article Card on Cool Coders is a concise yet informative snapshot of a user's post within a specific tech-related category. It includes the following key elements:

1. Author Profile: A visual representation of the author's profile picture and username, providing a quick way to identify the content creator.
2. Likes: The number of likes the post has received, offering a sense of its popularity and engagement.
3. Comments: The count of comments on the post, indicating the level of community discussion and interaction.
4. Category: Clearly indicating the tech category to which the post belongs, helping users quickly identify the content's subject matter.
5. Post Date: The date when the article was published, offering a reference for the recency of the content.
6. Title: The headline of the post, serving as a captivating entry point to the article's content.
7. Excerpt: A brief summary or excerpt from the article, providing users with a glimpse of the post's key points and enticing them to read further.

Together, these elements create a Category Card that is both visually appealing and informative, allowing users to make informed choices about which posts to explore further within a specific category.

<details><summary>Article Card</summary>
<img src="./documentation/images/features/articlecard.png">
</details>

### Notification Messages

Notification messages were user every time the user performs CRUD operation, sign in, and sign out.

<details><summary>Notifications</summary>
<img src="./documentation/images/features/notifications.png">
</details>

### Confirmation Modal

This modal appears whenever a users is performing a delete CRUD operation. It ensures the user must confirm their action before the permanent deletion of an item/account

<details><summary>Confirmation Modal</summary>
<img src="./documentation/images/features/confirmationmodal.png">
</details>

### Toggle Favourites

The "Toggle Favorites" button allows authenticated users to quickly add or remove articles from their favorites, tailoring their content preferences with ease.

<details><summary>Toggle Favourites</summary>
<img src="./documentation/images/features/togglefavourites.png">
</details>

### Comment Card

The comment card elegantly showcases the user's comment, the author's identity, and the date, encapsulating a meaningful exchange of ideas and perspectives on the article. Comments can only be created and deleted in similar fashion to Twitter/X.

<details><summary>Comment Card</summary>
<img src="./documentation/images/features/commentcard.png">
</details>

### Comment Form

The "Toggle Favorites" button allows authenticated users to quickly add or remove articles from their favorites, tailoring their content preferences with ease.

<details><summary>Comment Form</summary>
<img src="./documentation/images/features/commentform.png">
</details>

### Pending Post

The pending post card shows users their pending post approvals in one convenient card for quick and easy management. The can edit the post by clicking on the overlay

<details><summary>Pending Post</summary>
<img src="./documentation/images/features/pending-post.png">
</details>

### Error Pages

Custom Error pages are rendered to show the user what went wrong with their request. These error pages allow the user to redirect to the home page.

Examples below are 403, 404

<details><summary>403</summary>
<img src="./documentation/images/features/403error.png">
</details>
<details><summary>404</summary>
<img src="./documentation/images/features/404error.png">
</details>

## Future Features

Implementing future features is essential to maintain website growth and user retention because they not only keep the platform relevant and competitive but also provide added value to users, enticing them to return and engage with fresh, exciting content and functionalities.

### Search Feature

Implement a search bar in the navigation menu to allow users to search for specific users or articles by entering text, enhancing content discoverability.

### Password Reset with Email Validation

Introduce a secure and user-friendly password reset system that relies on email validation, making it easier for users to regain access to their accounts.

### Messaging System/Ticket System

- Develop a messaging system that enables users to send direct messages to each other, fostering user interaction.
- Alternatively, create a ticket system where users can contact the developer for technical issues or support, providing a more organized and responsive channel for communication. This is especially important because the current contact method is limited to an email in the footer, which may not be as user-friendly.

### Article Sharing

4. Add a share button to articles, allowing users to effortlessly share content on their social media platforms, increasing the website's visibility and user engagement.

These features have been added to the Agile Project Board in the unresolved column so they can be implemented at a later date.

- [Search Feature](https://github.com/DarrachBarneveld/CoolCoders-PP4/issues/48)
- [Password Reset with Email Validation](https://github.com/DarrachBarneveld/CoolCoders-PP4/issues/49)
- [Messaging System/Ticket System](https://github.com/DarrachBarneveld/CoolCoders-PP4/issues/50)
- [Article Sharing](https://github.com/DarrachBarneveld/CoolCoders-PP4/issues/51)

## Testing

In depth testing documentation can be found [here.](./TESTING.md)

## Bugs

Here is a list of all the major bugs encountered throughout development. Links to specific issues provide a more in depth analysis of how they were identified and resolved. This can also be found documented in [TESTING.md](./TESTING.md)

| Bug                                                                                                                        | Status |
| -------------------------------------------------------------------------------------------------------------------------- | ------ |
| [Profile routing based on slug errors #31](https://github.com/DarrachBarneveld/CoolCoders-PP4/issues/31)                   | Closed |
| [UpdateView Profile throwing errors with multiple forms #32](https://github.com/DarrachBarneveld/CoolCoders-PP4/issues/32) | Closed |
| [Content creating widget not responsive #37](https://github.com/DarrachBarneveld/CoolCoders-PP4/issues/37)                 | Closed |
| [Pagination on profile page renders only first results #38](https://github.com/DarrachBarneveld/CoolCoders-PP4/issues/38)  | Closed |
| [Lighthouse Performance Scores #41](https://github.com/DarrachBarneveld/CoolCoders-PP4/issues/41)                          | Closed |
| [User Edit Profile Form Autofocus #42](https://github.com/DarrachBarneveld/CoolCoders-PP4/issues/42)                       | Closed |
| [UX/UI Final Sweep #44](https://github.com/DarrachBarneveld/CoolCoders-PP4/issues/44)                                      | Closed |
| [Refresh Routing on changed Username #47](https://github.com/DarrachBarneveld/CoolCoders-PP4/issues/47)                    | Open   |
| [Env File not properly ignored #54](https://github.com/DarrachBarneveld/CoolCoders-PP4/issues/54)                          | Closed |
| [User Account Updated #55](https://github.com/DarrachBarneveld/CoolCoders-PP4/issues/55)                                   | Closed |

## Technologies And Languages

### Languages Used

- HTML
- CSS
- JavaScript
- Bootstrap
- Python
- Django

### Python Modules Imported

[Django-allauth](https://pypi.org/project/django-allauth/) is a versatile authentication and account management package for Django, providing a comprehensive set of features for user registration, authentication, account management, and social account integration.

[Dj-database-url](https://pypi.org/project/dj-database-url/) is used to parse the database URL specified in the DATABASE_URL environment variable, which is commonly used for configuring database connections in Django projects.

[Gunicorn](https://pypi.org/project/gunicorn/) is a popular WSGI (Web Server Gateway Interface) HTTP server for running Python web applications, including Django applications, in a production environment.

[Psycopg2](https://pypi.org/project/psycopg2/) is a PostgreSQL adapter for Python. It allows Django to connect to PostgreSQL databases.

[Django Summernote](https://pypi.org/project/django-summernote/) is a rich text editor and WYSIWYG plugin for Django that simplifies the process of incorporating and editing formatted content within web applications.

[Django Crispy Forms](https://pypi.org/project/django-crispy-forms/) is a Django application that enhances the presentation and customization of Django forms, making it easier to create aesthetically pleasing and responsive forms for web applications.

[Dj3-cloudinary-storage](https://pypi.org/project/dj3-cloudinary-storage/) is a Django storage backend that simplifies the integration of Cloudinary with Django, allowing for seamless and efficient storage and retrieval of media and static files in web applications.

[Cloudinary](https://pypi.org/project/cloudinary/1.27.0/) is a cloud-based media management platform that offers a comprehensive set of tools and services for storing, optimizing, transforming, and delivering images, videos, and other media assets, making it a valuable asset for web and app developers.

### Technologies and programs

- [Bootstrap](https://getbootstrap.com/) was used to quickly layout the responsive structure of the website
- [Chat-GPT](https://chat.openai.com/) was used to create all written content and copy of the website
- [VS Code](https://code.visualstudio.com/) was used to code the website locally
- [Balsamiq - Wireframe](https://balsamiq.com/wireframes/) was used to create quick and precise wireframes
- [Favicon Generator](https://favicon.io/favicon-converter/) was used to generate Favicon
- [Font Awesome](https://fontawesome.com/) was used for all icons on the website
- [GitHub](https://github.com/) is the hosting site used to store the code for the website.
- [Git](https://git-scm.com/) was used as a version control software to commit and push the code to the GitHub repository.
- [Google Fonts](https://fonts.google.com/) was used to import fonts.
- [Google Chrome Lighthouse](https://developers.google.com/web/tools/lighthouse) was used for scoring the website during the testing phase
- [Google Chrome Developer Tools](https://developer.chrome.com/docs/devtools/overview/) was used during testing, debugging and making the website responsive.
- [W3C HTML Validator](https://validator.w3.org/) was used to check for errors in the HTML code.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to check for errors in the CSS code
- [Wave Accessibility Tool](https://wave.webaim.org/) was used during testing to check accessibility
- [WebAim Contrast Checker](https://webaim.org/resources/contrastchecker/) was used to ensure proper contrast guidelines where adhered to.
- [Pylance Validator](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) was used as a linter to enhance best practice in the Python code.
- [CI Python Pep8 Checker](https://pep8ci.herokuapp.com/) was used to validate the Python code.
- [Cloudinary](https://cloudinary.com/) was used to store static files and images.
- [Coolors.co](https://coolors.co/) was used to display the colour scheme.
- [DBDiagram](https://dbdiagram.io/) was used to visually create the database structure and schemas
- [PostGresSQl](https://www.postgresql.org/) was used in development to store the database information locally
- [ElephantSQL](https://www.elephantsql.com/) was the database hosting provider for the production app
- [Heroku](https://heroku.com/) was the hosting provider used.

## Deployment

### Pre Deployment

To guarantee the proper deployment of the application on Heroku, it's essential to make sure that the requirements.txt file is kept up to date so as all imported python modules are configured correctly.

Secondly a Procfile is required to allow Heroku deployment to be properly configured to a gunicorn web app.

Thirdly in settings.py configure the ALLOWED_HOSTS list the format ['app_name.heroku.com', 'localhost'], make sure all static files and directorys are configured correctly.

Finally all environment variables on the env.py which gitignored on the repo must be configured correctly with the database url, storage url and secret key.

The hidden variables are as follows

- SECRET_KEY
- DATABASE_URL
- CLOUDINARY_URL
- PORT

### Deploying on Heroku

1. Create a Heroku account.
2. Sign up with a student account for credits. (optional)
3. Once logged in, select create a new app.
4. Select an app name and region.
5. Select deployment method as connect to github.
6. Find the desired repo. Coolcoders PP4 in this instance.
7. Enable automatic deploys and select the main branch
8. In the settings tab select reveal config vars. Input the required hidden variables.
9. Select nodejs and python as the buildpack.
10. Deploy.

### Fork The Repository

1. Go to the GitHub repository
2. Click on Fork button in the upper right-hand corner
3. Edit the repository name and description if desired
4. Click the green create fork button

### Clone The Repository

1. Go to the GitHub repository
2. Locate the green Code button above the list of files and click it
3. Select if you prefer to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7. Press Enter to create your local clone.

### Run The Repository Locally

1. Go to the GitHub repository
2. Locate the green Code button above the list of files and click it
3. From the dropdown menu select download Zip.
4. Download and open the zip file to run in an editor
5. Create an env.py file and input the environment variables
6. Ensure [PostgreSQL](https://www.postgresql.org/) is install on your computer and ports are open
7. Create a virtual environment for installing the python modules in the pip file.
8. Run python3 makemigrations, migrate and runserver

## Credits

### Content

All websites articles are written by me with the aid of promting CHATGPT. The AI Assisted in quickly outputting articles so the website was fleshed out.

### Media

- [Placeholder](https://codeinstitute.s3.amazonaws.com/fullstack/blog/default.jpg)
- [AI Image](https://www.risknet.de/en/topics/news-details/if-chat-gpt-becomes-superintelligent/)
- [Abacus](https://www.wnyc.org/story/tools-of-the-trade-the-abacus/)
- [Women in Tech](https://women-in-tech.org/)
- [Web vs App](https://www.linkedin.com/pulse/mobile-developer-vs-web-choose-right-career-mircea-turcanu/)
- [OOP](https://www.techtarget.com/searchapparchitecture/definition/object-oriented-programming-OOP)
- [Sleep and Code](https://medium.com/codex/sleep-more-code-more-aafa217fcb94)
- [Portable Monitor](https://www.pcworld.com/article/609831/fopos-triple-laptop-monitor-is-a-crazy-cool-road-warriors-tool.html)
- [Blue Light Glasses](https://edition.cnn.com/2023/08/17/health/blue-light-glasses-study-wellness/index.html)
- [Beer and Code](https://www.eventbrite.com/o/show-me-your-code-beer-bratislava-28116838723)
- [Hackathons](https://edison365.com/how-do-hackathons-work/)

### Code

Credit to [ByteGrad](https://www.youtube.com/watch?v=Jdkvmq8MtJY) for helping my css knowledge for making text appear with ellipse after a certain line to allow my article cards to be uniform in size and appearance.

Credit to [Dayana-N](https://github.com/Dayana-N/AutoMarket-PP4) for the well structured and coherent README which was used as a template to create my own.

Credit to [b0uh](https://b0uh.github.io/django-multiple-forms-in-one-class-based-view.html) for helping me understand how to have multiple forms rendering context on a single view class.

Credit to [Codemy.com](https://www.youtube.com/watch?v=H8MmNqDyra8&t=556s) for helping create profile classes directly linked to User instances.

Credit to [Maximilian Schwarzmüller](https://www.udemy.com/course/python-django-the-practical-guide/) for helping me understand django based view classes to a much higher degree.

Credit to [Dr Angela Yu](https://www.udemy.com/course/100-days-of-code/) for assisting my knowledge in python basics such as list comprehension

Credit to [Stackoverflow](https://stackoverflow.com/questions/10511873/can-django-pagination-do-multiple-paginations-per-page) for understand the correct approach for implementing multiple pagination on a single view class.

Credit to [Bootstrap](https://getbootstrap.com/docs/4.0/components/modal/) for providing the modal component

Credit to [StackOverflow](https://stackoverflow.com/questions/45467731/django-template-displays-edited-user-context-info-despite-validationerror) for helping me figure out the req.user instance issues when using form validation allowing me to have the nav bar remain consistant when username validation errors occur.

Credit to [StackOverflow](https://stackoverflow.com/questions/34959897/set-favicon-in-django-admin) for showing me how to add a favicon to the admin portal django template

### Acknowledgements

- A huge thanks to my mentor AntonioRodriguez who really helped me understand the MVC architechture seen in this project and giving me support above and beyond what was expected.
- Stef Cruz, Shane Donlon, Tanguy L'Alexandre, Callum Dennis, Daisy McGirr and Alan Bushell for manually testing and finding any potential errors before submission
- The Codu community for providing inspiration and motivation to continue my learning.
