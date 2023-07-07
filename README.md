# [Intranet Research Lab Website](https://intranetlab.netlify.app/)

This repository holds the [website](https://intranetlab.netlify.app/) for the **In**novative **Tran**sportation and **Net**works (Intranet) Lab. The static website is built with [Hugo](https://github.com/gohugoio/hugo), and is deployed with [Netlify](https://www.netlify.com/). The template comes from [Wowchemy](https://wowchemy.com). 

## The components of the website
- The first time you go to the website, you will see a *tour page*. We try to introduce our team and impress the viewer in three pages. 
- In the top left corner you will see the logo of our team. Clicking it will route you to the initial tour page. On the right left corner you can find the navigation bar and a search function button to search all content in the website.
- In the *home page* we will introduce our team. We will then show some recent news (all news are in news page). At the bottom the 'meet the team' button can route the viewer to people page. 
- The *people page* lists all team members. [See instructions here](#update-people-profile) on how to modify your profile.
- The *research page* lists all ongoing and previous research projects. [See instructions here](#update-research-projects) to create a project introduction.
- The *news page* contains all news and blogs. You can post your own blogs. [See instructions here](#update-news). `Do we really need this page`?
- The *publication page* lists all our results related to the lab. [See here for instructions](#update-publications) on how to upload your work.
- The *relevant works page* shows some important research results by others. 
- The *contact page* tells others how to contact us. We can post some hiring ads here.
- `?` Should we include a *teaching page* so the students can attend the relevant courses if they are interested. 

## How to update the website
Netlify makes it easy to update the website content. The CI/CD platform, linked to this Github repo, will automatically compile and deploy the website if the content is modified. Therefore, you can directly modify the `markdown` files (or the configuration `yaml` files if you know what you are doing). The changes will automatically appear on the website.

### Update people profile

A typical profile looks like this in the *people page*:
![profile](./images/profile.png)

It shows some basic info including name, avatar, title, and contact information.

Clicking the avatar will redirect you to the detailed profile where a short bio, research interests, education experience, and recent works would be shown.

OK, how do I create/modify my profile?

Go to `./content/authors`, you create `a folder with your name`, under that folder, create a `_index.md` file, upload your most beautiful photo, name it with `avatar.jpg`, and copy the codes in `../admin/_index.md`. Read the comments. Remember to change everything to avoid plagiarism. Set `superuser: false`.

### Update research projects

`TODO`

### Update news

`TODO`

### Update publications

`TODO`

### Update relevant works

`TODO`

## TODOs
-  Update everything according to [above design](#the-components-of-the-website)

    Upload all team member profiles, projects, publications...

- Finish this readme
- Design a logo
- Come up with some nice short sentences for the tour page and home page
- Test and fix any bug or inconsistency
- ...
- Discussions:
  - Do we need the news page?
  - Should we include a teaching page?
  - Improve the structure to make it more impressive?