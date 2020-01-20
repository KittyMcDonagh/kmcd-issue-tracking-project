# KMcD Issue Tracker

![alt text](/static/images/headfordsunset.jpg "Headford Sunset")

## **1.1 PURPOSE**

The purpose of the [Issue Tracker](https://kmcd-issue-tracker.herokuapp.com/issue_tracker/apphome/) is to allow clients to log the issues that they are experiencing with the _KMcD Online Accounting System_, as well as request new features. The issue tracker will provide a common area where all Clients can log their issues & features. They will be able to see each others' issues and features, comment on and upvote them, if they have the same issue, or want the same feature.

While bugs will be fixed for free, upvoting new features will cost a certain amount of money depending on the complexity of the requested feature (this will be decided on by the Vendor).

The issue tracker will be used by both the vendor (_KMcD Accounting Solutions_) and clients to monitor the progress of issues & features.

The app employs data protection policies in not allowing clients to see each others client codes, client details, or user ids.


## **1.2 DESIGN**

I used figma.com ([link to my designs](https://www.figma.com/file/g5LWnVMBRVwuMGNSxHS7qb/Home-Page?node-id=0%3A1)) to design the look and feel of the website. These screen layouts laid the foundation for the site. The original design focused on the Issues, but I based the Features list and details on the same design,so I didn't create any new design for these. 

As regards adding the comments, thumbs up, and add to cart, I didn't want to deviate too much from the original design, so I added these items in such a way that they blended in with the original design.

I have added screen shots of the original design in the 'Design' folder of the root directory. 



# **2. UX**

## **2.1 BACKGROUND**

_KMcD Accounting Solutions_, provides an Online Accounting System for small to medium-sized businesses. While the accounting system has been well-received, clients are experiencing issues with it and many have requested additional features. A means of logging these issues and features is required that will allow us to focus on fixing the issues that are of highest priority to our clients, and deliver new features in a timely manner. This will help us to respond quickly to their needs and improve client satisfaction. Hence the decision was made to create an online [issue tracker](https://kmcd-issue-tracker.herokuapp.com/issue_tracker/apphome/).


### **2.1.1 Issue Tracker High Level Overview**

![alt text](/static/images/issue_tracking_overall_view.png "Issue Tracker Overview")

### **2.1.2 Issue / Feature - Client-side Workflow**

![alt text](/static/images/issue-feature-c-workflow.png "Issue Tracker Client-side Workflow")

### **2.1.3 Issue / Feature - Vendor-side Workflow**

![alt text](/static/images/issue-feature-v-workflow.png "Issue Tracker Vendor-side Workflow")

### **2.1.4 Vendor & Client Views**

![alt text](/static/images/issue-feature-v-workflow.png "Issue Tracker Vendor & Client Views")




## **2.2 WEBSITE REQUIREMENTS**

### **2.2.1 High Level Requirements**

These are the high level requirements for [the issue tracker app](https://kmcd-issue-tracker.herokuapp.com/issue_tracker/apphome/).

1. The [the issue tracker app](https://kmcd-issue-tracker.herokuapp.com/issue_tracker/apphome/) is required to be a central point where clients can log all    issues that they are experiencing with the _KMcD Online Accounting System_, and where they can log new features that they require
2. So that clients don't have to input the same issue/feature that another client has, the app should allow clients to search for issues/features and to 
   flag another clients' issue, to indicate they have this also, and to pay a price to flag a feature (their own or another client's) that they require
3. Clients must be able to add comments on their own and on other clients' issues and features
4. Clients should be able to see all the comments input against a particular issue/feature
5. Clients must be able to run an issues and a features report that shows a list of the issues/features they have input and the issues that they have         flagged
6. The app requires two perspectives, a client perspective and a vendor perspective
7. Since the business contract is between the client and the vendor, not between one client and another, there are certain things a client should not be      able to do in relation to another clients' details - in the interests of data protection :
   - While clients should be able to see other clients' issues and features, but they should _not_ be able to see another client's client code or name, nor   the user id of a user who is associated with another client (this includes user ids shown on issues, features, and on comments)
   - Clients should not be able to edit / update another client's issues / features
   - A client should **not** have access to another client's reports
   - Clients **should** be able to see the user id of comments input by a user that is associated with the vendor
8. A client should not be able to see another client's issues or features until that client is satisfied with the details input and has set the               issue/feature to an appropriate status to allow other clients to view it
9. Once the issue / feature is at a status where other clients can view it, the client should not be able to edit its details - they should only be able to    update the client assigned user of the issue / feature
10. Since there is a contract between the vendor and the client there is no restriction required as to what client details the vendor can see:
    - The vendor shoud be able to see the client code and name
    - The vendor they should be able to see the user ids of isssues, features, and of comments
    - The vendor should be able to see reports for all clients
11. A vendor-side user should not be able to input new issues / features
12. A vendor-side user should not be able to edit the details of an issue/feature
13. A vendor-side user should be able to update the vendor assigned user, the status, and the priority on issues
14. A vendor-side user should be able to update the vendor assigned user, the status, and the price on features
15. It should be possible to filter issues by various options, status, priority, and for vendor-side users, by client
16. It should be possible to filter features by various options, status, sort them by amount paid, and for vendor-side users, filter by client
17. It should be possible for both vendor and clients to input comments on issues and features
18. It should be possible for both vendor and clients to view comments input on issues and features
19. It should be possible to differentiate comments input by vendor-side user from comments input by client-side users
 


## **2.2.2 USER STORIES** ##

|No. |Who I am                 |What I want to do                                                                                    | Why I want to do it
|----|-------------------------|-----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
|1.  |The Vendor               |I want to see all the issues/features clients are raising against the KMcD Online Accounting System. |I want to monitor them and keep track of them.                                                                       |
|2.  |The Vendor               |I want to be able to see all the details of issues / features.                                       |I want have a good understanding of the problems encountered, and the features required.                              |
|3.  |The Vendor               |I want to be able to assign issues/features to different users.                                      |So that certain users have a number of issues / features that they monitor for certain clients.                          |
|4.  |The Vendor               |I want to be able to change the priority and status of an issue.                                     |So that clients can see the priority given to their issues, and how they are progressing as their status changes.      |
|5   |The Vendor               |I want to be able to change the price and status of a feature, as the issue progresses.              |So that clients can see the priority given to their issues, and how they are progressing as their status changes.      |
|6.  |The Vendor               |I want to be able to input comments on issues / features.                                            |So as to give relevant information in relation to the issue/feature, or respond to comments input by the client. |
|7.  |Vendor                   |I want to be able select issues assigned to me or all issues, filter by priority, status and client. |It will help me focus on certain types of issues as required.                                                            |
|8.  |The Vendor               |I want to be able filter features by those assigned to me or all, by status, and client.             |It will help me focus on certain types or categories of features as required.                                            |         
|9.  |The Vendor               |I want to be able order features by amount paid per feature.                                         |It will help me see which features are of most concern to my clients.                                                  |
|10. |The Vendor               |I want to have an issues report by client, showing me the issues they have input and flagged.        |I will be able to see which issues are of most concern to my clients.                                                    |
|11. |The Vendor               |I want to have a features report by client, showing me the features they have input and paid for.    |I will be able to see which features are of most concern to my clients, and which clients are paying the most.           |
|12. |A Client                 |I want to be able to input and edit the details of issues and features.                              |I want to log issues / features once in one place, where I monitor them and where the vendor has sight of them.         |
|13. |A Client                 |I want to see all the issues/features raised by us and by other clients.                             |I want to monitor our own issues and see if other clients are having the same issues.                                    |
|14. |A Client                 |I want to be able to see all the details of issues / features.                                       |I want to see the details of our own issues / features and see how they compare with those of other clients.         |
|15. |A Client                 |I want to be able to assign issues/features to different users.                                      |So that certain users have a number of issues / features that they monitor.                                              |
|16. |A Client                 |I want to be able to change the status of an issue.                                                  |I want to be able to change the status from its initial value so that the vendor can view it.                           |
|17. |A Client                 |I want to be able to input comments on issues / features.                                            |So as to give relevant information in relation to the issue/feature, or respond to comments input by others.     |
|18. |A Client                 |I want to be able select issues assigned to me or all issues, filter by priority, status and client. |It will help me focus on certain types of issues as required.                                                            |
|19. |A Client                 |I want to be able filter features by those assigned to me or all, by status, and client.             |It will help me focus on certain types or categories of features as required.                                            |         
|20. |A Client                 |I want to be able order features by amount paid per feature.                                         |It will help me see which features the vendor should be giving priority to.                                            |
|21. |A Client                 |I want to have an issues report, showing me the issues we have input and flagged.                    |I will be able to see the issues that are of concern to us.                                                              |
|22. |A Client                 |I want to have a features report, showing me the features we have input and paid for.                |I will be able to see the features that are of concern to us.                                                            |



# **3. FEATURES**

## **3.1 ISSUE TRACKER**

These are the high level features of the Issue Tracker:
1. The app will initially request a login to the Issue Tracker, as it is available only to clients who are using the _KMcD Online Accounting System_
2. Once logged in the user will be presented with a list of issues that are assigned to them
3. From the **Navigation Bar** the user can select **Home,** **Profile,** **Logout,** the **Issues List,** **New Issue,** **Features List,** 
   **New Feature,** **Cart,**
4. From the **Footer** the user can select **Issues Report,** **Features Report,** and see the copyright notice
5. From the **Issues List** page the user can:
   - See summary details of up to five issues per page, and paginate to other pages 
   - Filter the issues list by Issues Filter, Status Filter, Priority Filter and, if the user is a vendor-side user, by Client 
   - Select to see the details of a particular issue
   - Select to see the comments on a particular issue
   - Flag an issue belonging to another client using the 'thumbs up' icon, to indicate they also have this
6. From the **Features List** page the user can:
   - See summary details of up to five features per page, and paginate to other pages 
   - Filter the features list by Features Filter, Status Filter, Sort by Amount paid per feauture and, if the user is a vendor-side user, filter by Client 
   - Select to see the details of a particular feature
   - Select to see the comments on a particular feature
   - Pay for a feature (their own or another client's) using the add to cart ('cart+') icon for that feature, to indicate they also want this 
   - Select the cart from the navigation bar, once features have been added to it, increase/reduce the quantity or remove an item, and proceed to checkout   to pay for the item(s)
7. Issue / Feature **Details Page**:
   - If the user selects the 'more' icon from the issues/features list:
     + The details screen will open showing the issue/feature details 
     + The user can click the comments icon to open the comments dashboard, where they can click on the '+' icon to add a comment or on the 'eye' icon to      view a list of existing comments
     + The user will be able to go back to the list page on which they clicked the 'more' icon by clicking on the 'Back to list' link
   
   - If the user selects the 'comments' icon from the issues/feature list:
     + The details screen will open with the comments dashboad and the list of comments for that issue/feature already showing
     + The user may use the 'comments' icon, and the comments dashboard to clear the comments or add a new comment
     + The user will be able to go back to the list page on which they clicked the 'comments' icon by clicking on the 'Back to list' link
   

## **3.2 NAVIGATION**

1. Before logging in, the top navigation bar gives easy access to Home, Login, Register.
2. After logging in, the top navigation bar gives easy access from all screens to Home, Profile, Logout, Issues List, Add an Issue (client users only),       Ffeatures List, Add a feature (client users only), and the Cart
3. After logging in, the footer links give easy access from all screens to the Issues Report and the Features Report


## **3.2 RESPONSIVENESS**

1. This app was built with 'mobile first' design in view. 

2. Various sizes of Bootstrap columns are used to allow the screens to be drawn to fit the size of the viewport.

3. It was decided to make all the same information available on all devices. Hence The Issues & Features tables scroll across the screen on smaller           devices so that the user can see all the information available.



# **4. TECHNOLOGIES USED**

|Technologies                 |Website                                                                   |
|-----------------------------|--------------------------------------------------------------------------|
|HTML                         |[w3schools](https://www.w3schools.com/)                                   |
|CSS                          |[w3schools](https://www.w3schools.com/)                                   |
|Javascript                   |[MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript)        |
|Jquery                       |[jQuery website](https://code.jquery.com/)                                |
|Bootstrap                    |[Bootstrap website](https://getbootstrap.com/)                            |
|Font Awesome                 |[Font Awesome website](https://fontawesome.com/)                          |
|AutoPrefixer                 |[Autoprefixer website](https://autoprefixer.github.io/)                   |
|Django                       |[django documentation](https://docs.djangoproject.com/en/3.0/)            |

      


|Features         |Website                                                                                       |COMMENTS                                                                                  |
|-----------------|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| Color Scheme    |[Color Wheel](https://www.canva.com/colors/color-wheel/)                                      |I used this website when choosing the base colors for my website.                         |                                                                    |  
| Colors          |[w3schools](https://www.w3schools.com/colors/colors_picker.asp)                               |I used this website for choosing different shades of the base colors for my website. |
| Web page layouts|[bootstrap](https://getbootstrap.com/)                                                        |I used bootstraps container, row and column classes to create my page layouts and to make them responsive               |         
| Navigation bar  |[bootstrap](https://getbootstrap.com/)                                                        |I used bootstraps nav bar classes to create my navigation bars, and burger menu.          |         
| Wireframes      |[Figma](https://www.figma.com/file/g5LWnVMBRVwuMGNSxHS7qb/Home-Page?node-id=71%3A1)           |I used figma when designing my website. See screen shots in Design folder on github    |
|Django Pagination|https://django-el-pagination.readthedocs.io/en/latest/digg_pagination.html                    |I used django pagination to create the paginate functionality on the Issues and Features Lists   


# **5. TESTING**

## **5.1 Manual Testing**

### **5.1.1. Account Testing**

#### 5.1.1.1 Registering


#### 5.1.1.2 Logging In


#### 5.1.1.3 Logging Out


#### 5.1.1.4 Forgotten Password






## **5.2 Automated Testing**

Due to time constraints I didn't get around to creating automated tests.


    
# 6. DEPLOYMENT

## 6.1 DEPLOYING FROM GITHUB 

1. Log onto Github
2. Select the respository you want to deploy
3. On the repository page, click on "Settings" and scroll down to "Github Pages"
4. From the "Source" dropdown select "Master Branch" and click "Save"
5. The message "Your site is ready to be published at https://username.github.io/Repository Name/" will 
   appear under Github Pages
6. When you click on this link your webpage will open in a browser window
7. If you receive a 404 error, wait a few minutes and try again. It usually takes a few minutes to deploy
8. Once your website launches you will need to retest it (see Testing section) to ensure that it can still 
   find all the resources (css file, images, etc)

## 6.2 CLONING FROM GITHUB 

1. Follow this link to my [Project Repository on Github](https://github.com/KittyMcDonagh/Second-Milestone-Project)
2. On the repository page click "Clone or Download"
3. In the Clone with HTTPs section, copy the clone URL for the repository.
4. In your local IDE open Git Bash.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type git clone, and then paste the URL you copied in Step 3 - 
    "git clone https://kittymcdonagh.github.io/Second-Milestone-Project/"
7. Press enter and your local clone will be created.



# **7. CREDITS**

## **7.1 CONTENT**

### **7.2 IMAGES AND ICONS USED ON ISSUE TRACKER **

The following icons/images were used to create the overview diagram of the Issue Tracking System:

|IMAGE / ICON                           |COPIED FROM
|---------------------------------------|----------------------------------------------------------------------------------------------|
|Questions Comments Concerns icon       |http://clipart-library.com/clipart/ziXoGpb7T.htm                                              |
|Client group icon                      |http://clipart-library.com/clipart/1745500.htm                                                |
|Group sitting around globe of world    |http://clipart-library.com/img1/1474499.jpg                                                   |
|Online Server image                    |http://clipart-library.com/clipart/99610.htm                                                  |
|Online computer image                  |http://clipart-library.com/image_gallery2/Hosting-Free-Download-PNG.png                       |



## **CODE SNIPPETS**

1. I have used code from the mini project to add a map to Rosie's resume, to load my map.
2. I used https://developers.google.com/maps/documentation/javascript/examples/place-details to add an infowindow for the location 
   name to the markers.
3. I have copied classes from my Milestone 1 project for the navigation bar, the links and hovering.
4. Comments have been added in the files where copied code is used.
5. With assistance from Slack I copied code from Stack Overflow to close the burger menu


## **7.3 ACKNOWLEDGEMENTS**

|NAME                          |COMMENTS
|------------------------------|----------------------------------------------------------------------------------------------|
|The Code Institute            |I learnt everything I needed to know to build this website from the Code Institute.           |
|Fellow students on Slack      |I received a lot of assistance and feedback from students on Slack which improved my project. |
|My mentor Seun Owonikoko      |I received assistance, feedback and encouragement from Seun.                                  |












