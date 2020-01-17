# KMcD Issue Tracker

![alt text](/static/images/headfordsunset.jpg "Headford Sunset")

## **1.1 PURPOSE**

_KMcD Accounting Solutions_, provides an Online Accounting System for small to medium-sized businesses. While the accounting system has been well-received, clients are experiencing issues with it and many have requested additional features. A means of logging these issues and features is required that will allow us to focus on fixing the issues that are of highest priority to our clients, and delivering new features in a timely manner. This will help us to respond quickly to their needs and improve client satisfaction. Hence the decision was made to create an online [issue tracker app](https://kmcd-issue-tracker.herokuapp.com/issue_tracker/apphome/).



# **2. UX**

## **2.1 BACKGROUND**

An Issue Tracking System is required where clients can log the issues that they are experiencing with the _KMcD Online Accounting System_, as well as request new features that they would like added to the software. 

The Issue Tracking System will allow clients to see each other’s issues, and feature requests, comment on them, and upvote them.

While bug fixes will be free, inputting, commenting on, and upvoting new features will cost a certain amount of money depending on the complexity of the requested feature (this will be decided on by the Vendor).

The issue tracker will be used by both the vendor (_KMcD Accounting Solutions_) and clients to monitor the progress of issues / features.

### **2.1.1 Issue Tracking Overview**

![alt text](/static/images/issue_tracker_overall_view.png "Issue Tracking Overview")




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

## **3.1 KMCD ISSUE TRACKER APP**

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
   

**NOTES**



## **3.6 NAVIGATION AND RESPONSIVENESS**





# **4. TECHNOLOGIES USED**

|Technologies                 |Website                                                                 |
|-----------------------------|------------------------------------------------------------------------|
|HTML                         |[w3schools](https://www.w3schools.com/)                                 |
|CSS                          |[w3schools](https://www.w3schools.com/)                                 |
|Javascript                   |                                                                        |
|Jquery                       |[jQuery website](https://code.jquery.com/)                              |
|Bootstrap                    |[Bootstrap website](https://getbootstrap.com/)                          |
|Font Awesome                 |[Font Awesome website](https://fontawesome.com/)                        |
|AutoPrefixer                 |[Autoprefixer website](https://autoprefixer.github.io/)                 |
|dc                           |[dc website](https://cdnjs.cloudflare.com/ajax/libs/dc/3.0.12/)         |
|d3                           |[d3 website](https://d3js.org/)                                         |
|google maps api              |[Google Maps API website](https://maps.googleapis.com/maps/api/)        |
|                             |[Google Maps API Developer website[(https://developers.google.com)      |
|Jasmine Testing              |[jasmine website](https://cdnjs.cloudflare.com/ajax/libs/jasmine/3.4.0) |      


|Features         |Website                                                                                       |COMMENTS                                                                                  |
|-----------------|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| Color Scheme    |[google maps logo colors](https://www.schemecolor.com/google-maps-colors.php)                 |I used this website when choosing the base colors for my website.                         |                                                                    |  
| Colors          |[w3schools](https://www.w3schools.com/colors/colors_picker.asp)                               |I used this website for choosing different shades of the base colors for my website.      |
| Grids           |[bootstrap](https://getbootstrap.com/)                                                        |I used bootstraps container, row and column classes to create my page grids               |         
| Navigation bar  |[bootstrap](https://getbootstrap.com/)                                                        |I used bootstraps nav bar classes to create my navigation bars, and burger menu.          |         
| Wireframes      |[Figma](https://www.figma.com/file/Q9lO2ZVjv6ovP9RsVDKji9ZY/MySouthAfricanTrip?node-id=0%3A1) |I used figma  when designing my website. See screen shots in figma directory on github    |



# **5. TESTING**

## **5.1 Manual Testing**

### **5.1.1. Navigation Test**

1. Load the [**South African Trip** web page](https://milestone-project-2-kittyjo.c9users.io/index.html)
2. Verify that the logo, home icon, all links, slidedown user message, and google map are appearing correctly on the page
3. In the top navigation bar, hover over each link and verify that the hover affects are working 
   (i.e. the link is highlighted in a shade of yellow: #ffe047)
5. In the bottom navigation link, hover over the link  and verify that the hover affects are working
   (i.e. the link is highlighted in a shade of yellow: #ffe047)
8. Do the following tests on the top navigation bar:
    - Click on "Home" and on the logo image and verify that they reload the page
    - Click on "Lodgings" and verify that the user message disappears, the Lodging Filter appears as a piechart, 
      and 8 markers appear on the map. Click on Home again
    - Click on "Safari" and verify that the user message disappears, the Safari Filter appears as a piechart,
      and 8 markers appear on the map. Click on Home again
    - Click on "Sight Seeing" and verify that the user message disappears the Sight Seeing Filter appears as a piechart,
      and 8 markers appear on the map. Click on Home again
    - Click on "Gallery" and verify that it jumps to the Gallery section of the page. 

### 5.1.2 Features Test

#### 5.1.2.1 LODGINGS

1. Click on "Lodgings" and verify that the Filter Piechart showing different types of dwellings appears
2. Check that there are 8 markers on the map and 8 photos in the Gallery
3. Check that the letters on the map match the letter on the photo names
4. Click on each marker and verify that the name is correct for that marker
5. Hover on each slice of the Filter Piechart and verify how many lodgings of that type the slice covers
6. Click on a slice of the Filter Piechart and verify that the same number of markers appear on the map
7. Click on Gallery (or scroll down to Gallery) and verify that only the photos relevant to that slice of the piechart 
   are showing
8. Click on more pieces of the Filter Piechart to include or exclude the types for those slices. Verify that only those
   markers and photos are shown,  that are relevant to the piece(s) of the piechart that is/are selected

#### 5.1.2.2 SAFARI

1. Click on "Safari" and verify that the Filter Piechart showing different types of Safari animals appears
2. Check that there are 8 markers on the map and 8 photos in the Gallery
3. Check that the letters on the map match the letter on the photo names
4. Click on each marker and verify that the name is correct for that marker
5. Hover on each slice of the Filter Piechart and verify how many animal of that type the slice covers
6. Click on a slice of the Filter Piechart and verify that the same number of markers appear on the map
7. Click on Gallery (or scroll down to Gallery) and verify that only the photos relevant to that slice of the piechart 
   are showing
8. Click on more pieces of the Filter Piechart to include or exclude the types for those slices. Verify that only those
   markers and photos are shown,  that are relevant to the piece(s) of the piechart that is/are selected

#### 5.1.2.3 SIGHT SEEING

1. Click on "Sight Seeing" and verify that the Filter Piechart showing different types of sightseeing appears
2. Check that there are 8 markers on the map and 8 photos in the Gallery
3. Check that the letters on the map match the letter on the photo names
4. Click on each marker and verify that the name is correct for that marker
5. Hover on each slice of the Filter Piechart and verify how many sight seeing of that type the slice covers
6. Click on a slice of the Filter Piechart and verify that the same number of markers appear on the map
7. Click on Gallery (or scroll down to Gallery) and verify that only the photos relevant to that slice of the piechart 
   are showing
8. Click on more pieces of the Filter Piechart to include or exclude the types for those slices. Verify that only those
   markers and photos are shown,  that are relevant to the piece(s) of the piechart that is/are selected


#### 5.1.2.4 THE GALLERY

1. Click on each link under each photo and verify that the website for that link opens in a new tab

## **5.2 JASMINE Testing**

**NOTE**
1. I am not sure if I have taken the right approach to Jasmine testing, but here's what I have done:
   - I have taken the functions that deal with user interactions and created some jasmine tests
   - I have removed any code that takes values from the DOM or adds information to the DOM
   - The values being tested are passed in from calcSpec
   - I have based the test around being able to return the correct Marker Labels and Location names only 
   - I am testing only my own javascript code - I'm not testing dc/d3 or maps (I don't know how to do that)


    
### 5.2.1 Navigation Test

1. I tested that the Main Headings (Lodgings, Safari, and Sight Seeing) returned the correct marker labels and location names
2. I tested that the Filter Piecharts returned the correct marker labels and location names depending on which 'slice' was selected


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

### **7.2 PHOTOGRAPHS**

1. The photos on [my website](https://milestone-project-2-kittyjo.c9users.io/index.html) were copied from:
    - [Hotel Verde website](https://www.verdehotels.com/capetown/)
    - [Quayside Hotel website](https://www.aha.co.za/quayside/)
    - [Milkwood Manor website](http://www.milkwoodmanor.co.za/)
    - [Protea Hotel website](https://www.marriott.com/hotels/travel/jnbro-protea-hotel-roodepoort)
    - [Knysna Elephant Park website](https://knysnaelephantpark.co.za/)
    - [Glen Afric website](https://www.glenafric.co.za/gallery.html)
    - [Addo Elephant Park website](https://www.sanparks.org/gallery/parks/addo-elephant-national-park)
    - [Lower Sabie Rest Camp website](http://www.krugerpark.co.za/Kruger_National_Park_Lodging_&_Camping_Guide-travel/lower-sabie-camp_accommodation.html)
    - [Google Image - 1](https://www.google.ie/url?sa=i&source=images&cd=&ved=2ahUKEwjLzI6TkPjiAhVIZcAKHUQUBx4QjRx6BAgBEAU&url=https%3A%2F%2Ftraveltriangle.com%2Fblog%2Fkruger-national-park-south-africa%2F&psig=AOvVaw1ejAYpZxCnH7tcrV2cXzeA&ust=1561122358506228)
    - [Lion and Safari website](http://www.lionandsafaripark.com/)
    - [de Wildt Cheetah Sanctuary website](http://dewildt.co.za/)
    - [Zulu Nyala website](http://zulunyalagroup.com/)
    - [Google Maps Image](https://www.google.ie/maps/uv?hl=en&pb=!1s0x1ebe391bbc301847%3A0xb04e56d51d86baed!2m22!2m2!1i80!2i80!3m1!2i20!16m16!1b1!2m2!1m1!1e1!2m2!1m1!1e3!2m2!1m1!1e5!2m2!1m1!1e4!2m2!1m1!1e6!3m1!7e115!4shttps%3A%2F%2Fostrovok.ru%2Frooms%2Fukutula_lion_lodge%2F!5sukutula%20lodge%20and%20lion%20centre%20-%20Google%20Search!15sCAQ&imagekey=!1e1!2shttps%3A%2F%2Fbstatic.com%2Fxdata%2Fw%2Fhotel%2Fmax1500_watermarked_standard_bluecom%2FUl2O-ydSLLJd7DjiOt_wTTw5PQalexfVd5tMHgGKcyB1HUy2S0Oc0hSIf7IYn-Ul0VGqpLMkJifSViUKLIdB6Xv56US0Au4koTYMNzaDDE9nSApsIkFJNA4OZ5ERWWE.jpg&sa=X&ved=2ahUKEwj0q56xlPjiAhV0nVwKHcL1BnoQoiowFXoECA0QBg#)
    - [Google Image - 2](https://www.google.ie/url?sa=i&source=images&cd=&ved=2ahUKEwjM3fjclfjiAhU0Q0EAHcVuDo8QjRx6BAgBEAU&url=https%3A%2F%2Fwww.thesouthafrican.com%2Ftravel%2Fexploring-the-wonder-of-chapmans-peak-video%2F&psig=AOvVaw24AxQ72SgSHTbs-KCxhKn0&ust=1561123760736862)
    - [Google Image - 3](https://www.google.ie/url?sa=i&source=images&cd=&ved=2ahUKEwjulvHtlvjiAhXMfMAKHSmOCg8QjRx6BAgBEAU&url=https%3A%2F%2Fwww.privatetransportcapetown.com%2Ftour%2Fcape-of-good-hope-and-cape-point-sightseeing-private-cape-peninsula-day-tour%2F&psig=AOvVaw3-tM30-c1DkaN7q9Kai38B&ust=1561124099375976)
    - [Stellenbosch website](https://www.stellenbosch.travel/attractions/heritage-architecture)
    - [Stellenbosch website](https://www.stellenbosch.travel/)
    - [Marianne Wine Estates website](http://www.mariannewines.com/our-winery/tasting-room)
    - [Ocean Safari website](http://oceansafaris.co.za/gallery/)
    - [Google Image - 4](https://www.google.ie/url?sa=i&source=images&cd=&ved=2ahUKEwiKo-TzmvjiAhVyQUEAHduwCj0QjRx6BAgBEAU&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FNature%2527s_Valley&psig=AOvVaw0DkfC7Z1orAzHaluMjTDRD&ust=1561125251107402)
    - [Google Image - 5](https://www.google.ie/url?sa=i&source=images&cd=&ved=2ahUKEwiA_pWqm_jiAhWLT8AKHWwmDSAQjRx6BAgBEAU&url=https%3A%2F%2Fwww.thenational.ae%2Flifestyle%2Ftravel%2Fmy-kind-of-place-port-elizabeth-south-africa-1.165596&psig=AOvVaw0CtESsVnHBKH7nxDpZ7wdt&ust=1561125353100379)
    - [Google Image - 6](https://www.google.ie/url?sa=i&source=images&cd=&ved=2ahUKEwi6r7Lcm_jiAhXMa8AKHcAsAYAQjRx6BAgBEAU&url=https%3A%2F%2Fwww.lonelyplanet.com%2Fsouth-africa%2Fgauteng%2Fjohannesburg&psig=AOvVaw1dc6BmwwX0X4PTSd1NZdlO&ust=1561125454470675)
2. The map is from [Google Maps API](https://maps.googleapis.com/maps/api/)


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












