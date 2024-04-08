# [Intranet Research Lab Website](https://intranetlab.netlify.app/)

This repository holds the [website](https://intranetlab.netlify.app/) for the **In**novative **Tra**nsportation and **Net**works (Intranet) Lab. The static website is built with [Hugo](https://github.com/gohugoio/hugo), and is deployed with [Netlify](https://www.netlify.com/). The template comes from [Wowchemy](https://hugoblox.com/) (now called Hugo Blox). 

## The components of the website
- The first time you go to the website, you will see a *tour page*. We try to introduce our team and impress the viewer in three pages. 
- In the top left corner you will see the logo of our team. Clicking it will route you to the initial tour page. On the right left corner you can find the navigation bar and a search function button to search all content in the website.
- In the *home page* we will introduce our team. We will then show some recent news (all news are in news page). At the bottom the 'meet the team' button can route the viewer to people page. 
- The *people page* lists all team members. [See instructions here](#update-people-profile) on how to modify your profile.
- The *research page* lists all ongoing and previous research projects. [See instructions here](#update-research-projects) to create a project introduction.
- The *news page* contains all news and blogs. You can post your own blogs. [See instructions here](#update-news).?
- The *publication page* lists all our results related to the lab. [See here for instructions](#update-publications) on how to upload your work.
- The *teaching* shows courses taught by us. 
- The *contact page* tells others how to contact us. We can post some hiring ads here.
 

## How to update the website
Hugo makes it easy to update the website content. The CI/CD platform, Netlify, linked to this Github repo, will automatically compile and deploy the website if the content is modified. Therefore, one can directly modify the `markdown` files (or the configuration `yaml` files if you know what you are doing). The changes will automatically appear on the website if they are merged to the main branch.

### Update people profile

A typical profile looks like this in the *people page*:
![profile](./images/profile.png)

which shows some basic info including avatar, name, title, and contact information.

Clicking the avatar will redirect you to the detailed profile where a short bio, research interests, education experience, and recent works would be shown.

#### How to create/update profile

1. Each profile corresponds to a folder under `/content/authors`. 
2. Create a new folder or find your profile folder under `/content/authors`, typically the folder name should be your name. 
3. Under `/content/authors/your name`, create a `_index.md` file, where you write things about yourself. An example is given under `../costas/_index.md`. You can directly copy the codes and make necessary changes. The comments in the code specify the role of each line. 
4. Upload your photo to the same folder and name it with `avatar`, currently known supported formats are `jpg` and `png`.   
5. Publications and profiles are decoupled. You don't have to write publications in profile. Instead, after you [create new publication](#update-publications) in `/content/publication`, it would automatically show under corresponding authors. 
6. Check [official document](https://docs.hugoblox.com/tutorial/resume/step-2/) for help.

### Update research projects

`TODO`

### Update news

`TODO`

### Update publications

All publications would be shown in `Publications` page, where there is a filter to search and sort publications.

#### Steps to create/update a publication
1. Each publication corresponds to a folder under `/content/publication`.
2. Create a new folder or find the folder under `/content/publication`, remember to name the folder in a way that is easy to recognize.
3. Under `/content/publication/your publication folder`, create a `index.md` file which includes basic info, abstract of the publication. Different examples are given, including sample `conference-paper`, sample `journal-article`, and sample `preprint`. Read the comments in the code and you will figure out what to do. `Note`: under `authors` field, you should use the name of your profile file under `/content/authors` to let hugo create links between you and your publication.  
4. [Optional] Upload feature picture named `featured`. Provide bib citations in `cite.bib`. Other features commented out in `index.md`.
5. See [official document](https://bootstrap.hugoblox.com/content/publications/) for advanced features.

### Update teaching

`TODO`

## TODOs
-  Update everything according to [above design](#the-components-of-the-website)

    Upload all team member profiles, projects, publications...

- Finish this readme
- Design a logo
- Come up with some nice short sentences for the tour page and home page
- Test and fix any bug or inconsistency
- Figure out the layout of project/course.