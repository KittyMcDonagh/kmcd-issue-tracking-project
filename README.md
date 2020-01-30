**_KMcD Software Solutions_ - ISSUE TRACKER**  
======================

![alt text](/static/images/galwaybay.jpg "Galway Bay sunset")
======================

# **1 INTRODUCTION**

## **1.1 PURPOSE**

The purpose of the [Issue Tracker](https://kmcd-issue-tracker.herokuapp.com/issue_tracker/apphome/) is to allow clients to log the issues that they are experiencing with the _KMcD Online Accounting System_, as well as request new features. The Issue Tracker will provide a common area where all Clients can log their issues and request features. They will be able to see each others' issues and features, comment on them, and upvote them if they have the same issue, or want the same feature.

While bugs will be fixed for free, upvoting new features will cost a certain amount of money depending on the complexity of the requested feature (this will be decided upon per feature by the Vendor).

The Issue Tracker will be used by both the vendor (_KMcD Accounting Solutions_) and clients to monitor and manage the progress of issues & features.

The app employs data protection policies in not allowing clients to see each others client codes, client details, or user ids.


## **1.2 BACKGROUND**

_KMcD Accounting Solutions_, provides an Online Accounting System for small to medium-sized businesses. While the accounting system has been well-received, clients are experiencing issues with it and many have requested additional features. A means of logging these issues and features is required that will allow us to focus on fixing the issues that are of highest priority to our clients, and deliver new features in a timely manner. Hence the decision was made to create an online [Issue Tracker](https://kmcd-issue-tracker.herokuapp.com/issue_tracker/apphome/) that will help us to respond quickly to our clients' needs, thereby improving client satisfaction.


# **2 UX**

## **2.1 LOOK & FEEL**

I used [figma.com](https://www.figma.com/file/g5LWnVMBRVwuMGNSxHS7qb/Home-Page?node-id=0%3A1) to design the look and feel of the website. These screen layouts laid the foundation for the site. The original design focused on the Issues, but I based the Features list and details on the same design, so I didn't create any new designs for these. 

As regards adding the comments, thumbs up, and add to cart, I didn't want to deviate too much from the original design, so I added these items in such a way that they blended in with the original designs.

I have added the screen shots of the original design in the 'Design' folder of the root directory, and they can be seen [here on github](https://github.com/KittyMcDonagh/kmcd-issue-tracking-project/tree/master/Design/figma-wireframes). 

I designed the screens so that they wouldn't vary too much from one device to another, and so that the user can see the same information regardless of what device they're using. Therefore I made the Issue and Features List tables responsive so that they would slide from left to right, rather than removing columns on smaller devices. 


## **2.2 Logic Flows**

I used _Microsoft Publisher_ to create logic flows for:
- The Issue Tracker 
- User setup
- Vendor-side processing
- Client-side processing
- Workflows for the Issues & Features

I have included these diagrams in this README document, and they can also be seen [here on github](https://github.com/KittyMcDonagh/kmcd-issue-tracking-project/tree/master/Design/system-diagrams)


### **2.2.1 Issue Tracker High Level Overview**

![alt text](/Design/system-diagrams/issue_tracking_overall_view.png "Issue Tracker Overview")


### **2.2.2 Vendor side - System Logic Flow**

![alt text](/Design/system-diagrams/vendor-system-logic.png "Vendor System Logic")


### **2.2.3 Client side - System Logic Flow**

![alt text](/Design/system-diagrams/client-system-logic.png "Client System Logic")


### **2.2.4 Issue / Feature - Client-side Workflow**

![alt text](/Design/system-diagrams/issue-feature-c-workflow.png "Issue Tracker Client-side Workflow")


### **2.2.5 Issue / Feature - Vendor-side Workflow**

![alt text](/Design/system-diagrams/issue-feature-v-workflow.png "Issue Tracker Vendor-side Workflow")


## **2.3 USER STORIES** ##

|No. |Who I am                 |What I want to do                                                                                    | Why I want to do it
|----|-------------------------|-----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
|1.  |The Vendor               |I want to see all the issues/features clients are raising against the _KMcD Online Accounting System_. |I want to monitor them and keep track of them.                                                                       |
|2.  |The Vendor               |I want to be able to see all the details of issues / features.                                       |I want have a good understanding of the problems encountered, and the features required.                              |
|3.  |The Vendor               |I want to be able to assign issues/features to different users.                                      |So that certain users have a number of issues / features that they monitor for certain clients.                          |
|4.  |The Vendor               |I want to be able to change the priority and status of an issue.                                     |So that clients can see the priority given to their issues, and how they are progressing as their status changes.          |
|5.  |The Vendor               |I want to be able to change the status of a feature, as the feature progresses.                      |So that clients can see how their features are progressing.                                                                |
|6.  |The Vendor               |I want to be able to change the price a feature as we gain more understanding of the work involved.  |The price reflects the complexity of the feature.                                                                         |
|7.  |The Vendor               |I want to be able to input comments on issues / features.                                            |So as to give relevant information in relation to the issue/feature, or respond to comments input by the client.          |
|8.  |Vendor                   |I want to be able to select issues assigned to me or all issues, and filter by priority, status and client.|It will help me focus on certain types of issues, or issues of a particular client, as required.                   | 
|9.  |The Vendor               |I want to be able select features assigned to me or all, and by status, and client.                   |It will help me focus on certain types or categories of features, or features of a particular client, as required.       |         
|10.  |The Vendor               |I want to be able order features by amount paid per feature.                                         |It will help me see which features are of most concern to my clients.                                                  |
|11. |The Vendor               |I want to have an issues report by client, showing me the issues they have input and flagged.        |I will be able to see which issues are of most concern to my clients.                                                    |
|12. |The Vendor               |I want to have a features report by client, showing me the features they have input and paid for.    |I will be able to see which features are of most concern to my clients, and which clients are paying the most.           |
|13. |A Client                 |I want to be able to input and edit the details of issues and features.                              |I want to log issues / features once in one place, where I can monitor them and where the vendor has sight of them.       |
|14. |A Client                 |I want to see all the issues/features raised by us and by other clients.                             |I want to monitor our own issues/features and see if other clients are having the same issues, or want the same features.|
|15. |A Client                 |I want to be able to see all the details of issues / features.                                       |I want to see the details of our own issues / features and see how they compare with those of other clients.         |
|16. |A Client                 |I want to be able to assign issues/features to different users.                                      |So that certain users have a number of issues / features that they monitor.                                              |
|17. |A Client                 |I want to be able to keep an issue/feature from pubic view.                                          |I don't want an issue/feature appearing on the vendor list or other clients' lists until the details have been agreed internally.                     |
|18. |A Client                 |I want to be able to input comments on issues / features.                                            |So as to give relevant information in relation to the issue/feature, or respond to comments input by others.     |
|19. |A Client                 |I want to be able to select issues assigned to me, or all issues, or our issues only, or other clients' issues only, and filter by priority, and status |It will help me focus on certain types of issues as required.                                                            |
|20. |A Client                 |I want to be able to filter features, by those assigned to me or all, and by status                  |It will help me focus on certain types or categories of features as required.                                            |         
|21. |A Client                 |I want to be able to order features by amount paid per feature.                                         |It will help me see which features the vendor should be giving priority to.                                            |
|22. |A Client                 |I want to be able to flag an issue (to say I have this too), and flag a feature (to say I want this too).|I want to avoid having to enter the same issue/feature, but I still want the vendor to know I have the issue, or want the feature.
|22. |A Client                 |I want to have an issues report, showing me the issues we have input and flagged.                    |I will be able to see the issues that are of concern to us.                                                              |
|23. |A Client                 |I want to have a features report, showing me the features we have input and paid for.                |I will be able to see the features that are of concern to us.                                                            |


## **2.4 WEBSITE REQUIREMENTS**

### **2.4.1 High Level Requirements**

1. The online [Issue Tracker](https://kmcd-issue-tracker.herokuapp.com/issue_tracker/apphome/) is required to be a central point where clients can log the      issues that they are experiencing with the _KMcD Online Accounting System_, and where they can log requests for new features
2. The app requires two perspectives, a Client perspective and a Vendor perspective
3. Clients must be able to restrict the Vendor and other clients from seeing the Issue/Feature they input until they are satisfied with the details, and       have set it to an appropriate status to allow the Vendor and other Clients to view it
4. Clients must be able to search for Issues/Features based on the details in the Summary field
5. Clients must be able to flag another clients' Issue, to indicate they have this also
6. Clients must be able to flag and pay for a Feature (their own or another client's) that they require
7. Clients must be able to add comments on their own and on other clients' Issues and Features
8. Clients must be able to see all the comments and differentiate between those input by clients and those input by the Vendor

9. Once an Issue / Feature is at a status where other clients can view it, the client should not be able to edit its details - they should only be able to     update the user to whom the Issue/Feature is assigned on the client side

10. Clients must be able to see a list of Issues
11. Clients must be able to filter the Issues list by various options - e.g. Status, Priority, Ours, Other Clients
12. Clients must be able to flag another client's Issue to indicate that they have it too
13. Clients must **not** be able to flag their own Issues

16. Clients must be able to see a list of Features
17. Clients must be able to filter the Features list by various options - e.g. Status, Ours, Other Clients
19. Clients must be able to sort the Features list by the amount paid for a Feature
20. Clients must be able flag a Feature and pay for it

22. Clients must be able to run an Issues report that shows a list of Issues that they have input and/or flagged
23. Clients must be able to run a Features report that they have input and/or paid for:

25. A vendor-side user should **not** be able to input or edit Issues/Features
27. A Vendor-side user **should** be able to input comments on Issues/Features
28. A Vendor-side user should be able to view all comments and differentiate between those input by clients and those input by the Vendor

29. A vendor-side user **should** be able to update the certain fields on an Issue pertaining to its progress, priority, or change of user assignment on       the Vendor side

30. A vendor-side user **should** be able to update certain fields on a Feature pertaining to its progress, price, or change of user assignment on             the Vendor side

31. Vendor-side users must be able to see a list of Issues
32. Vendor-side users must be able to filter the Issues list  by various options - e.g. Status, Priority, Client

34. Vendor-side users must be able to see a list of Features
35. Vendor-side users must be able to filter the Features list  by various options - e.g. Status, Client
    - Features Assigned to the Logged in user only
    - All Features
36. Vendor-side users must be able to filter the Features list by Status, and Client
37. Vendor-side users must be able to sort the Features list by Total Amount Paid for the Feature

38. Vendor-side users must be able to run an Issues report that:
    - (a) Shows a rolled up total line for each Client, showing the number of Issues input and/or flagged by the Client, 
    - (b) Orders the rolled up total lines by the number of Issues per client, from highest to lowest
    - (c) Allows the user to click on a rolled up total line to show/hide the list of Issues underneath
    - (d) Lists the Issues in Priority order, from most urgent to least urgent

39. Vendor-side users must be able to run a Features report that show the Features they have input and/or paid for

24. Since the business contract is between the client and the Vendor, not between one client and another, data protection restrictions need to be applied      in relation to the client details that other clients are allowed to see

40. Since there is a contract between the Vendor and the Client no data protection restrictions need apply in relation to client details.
    - The vendor should be able to see the client code and name
    - The vendor they should be able to see the user ids of Isssues, Features, and of Comments
    - The vendor should be able to see reports for all clients
    - Clients **should** be able to see the user id of Comments input by a user that is associated with the Vendor

41. It must be possible to differentiate comments input by vendor-side user from comments input by client-side users
 


# **3. ISSUE TRACKER FEATURES**

## **3.1 EXISTING FEATURES**

### **3.1.1 NAVIGATION**

1. Before logging in, the top navigation bar gives easy access to Home, Login, Register.
2. After logging in, the top navigation bar gives easy access from all screens to Home, Profile, Logout, Issues List, Add an Issue (client users only),         Features List, Add a feature (client users only), and the Cart
3. After logging in, the footer links give easy access from all screens to the Issues Report and the Features Report


### **3.1.2 RESPONSIVENESS**

1. This app was built with 'mobile first' design in view. 

2. Various sizes of Bootstrap columns are used to allow the screens to be drawn to fit the size of the viewport.

3. It was decided to make all the same information available on all devices. Hence The Issues & Features tables scroll across the screen on smaller             devices so that the user can see all the information available.


### **3.1.3 General Functionality**

1. The app will initially request a login to the Issue Tracker, as it is available only to clients who are using the _KMcD Online Accounting System_
2. Registering to use the Issue Tracker is a 2-step process:
   - A user may register as a new user on the Issue Tracker
   - The user's details must be set up, via Django Admin, on the UserDetails database
   - Once these 2 steps are completed the user will have access to the Issue Tracker

3. Once logged in the user will be presented with a list of the Issues that are assigned to them

4. From the **Navigation Bar** the user has access to **Home,** **Profile,** **Logout,** the **Issues List,** **New Issue,** **Features List,** 
   **New Feature,** **Cart,**

5. From the **Footer** the user can select **Issues Report,** **Features Report,** and see the copyright notice

6. From the **Issues List** page all users can:
   - See high level details of up to five Issues per page, and paginate to other pages
   - See the id, input date, Client Code, Assigned User, Software Component, Issue Summary, Status
   - See the number of **other** individual Clients who have flagged ('thumbed up') the Issue (in the flagged column)
   - Select to see the details of a particular Issue
   - Select to see the comments on a particular Issue
   
   - See the id, input date, Client Code, Assigned User, Software Component, Feature Summary 
   - See the Status, Price, Total Paid so far
   - See the number of individual Clients who have paid for the Feature (in the flagged column)
   - Select to see the details of a particular Feature
   - Select to see the comments on a particular Feature

7. **Client-side** users may filter the Issues List by an Issues Filter which allows the user to select:
    - Issues Assigned to the Logged in user only
    - Issues that belong to the client the user is associated with only
    - Issues that belong to other clients only
    - All Issues
    
8. Client-side users are able to filter the Issues list by Status, and Priority
9. Client-side userd are able to flag another client's Issue by clicking a 'thumbs up' icon for that Issue, to indicate that they have it too
10. Client-side users are able to unflag an Issue that they previously flagged
11. Clients are **not* be able to flag their own Issues

12. **Vendor-side** users are able to filter the Issues list by an Issues Filter which allows the user to select:
    - Issues Assigned to the Logged in user only
    - All Issues
13. Vendor-side users are able to filter the Issues list by Status, Priority, and Client  

14. From the **Features List** page all users can:
   - See high level details of up to five features per page, and paginate to other pages
   - See the id, input date, Client Code, Assigned User, Software Component, Feature Summary 
   - See the Status, Price, Total Paid so far
   - See the number of individual Clients who have paid for the Feature (in the flagged column)
   - Select to see the details of a particular Feature
   - Select to see the comments on a particular Feature
   
15. Client-side users are able to filter the Features list by a Features Filter which allows the user to select:
    - Features Assigned to the Logged in user only
    - Features that belong to the client the user is associated with only
    - Features that belong to other clients only
    - All Features
    
16. Client-side users are able to filter the Features list by Status
17. Client-side users are able to sort the Features list by Total Amount Paid for the Feature
18. Client-side users are able to flag their own or another client's Feature, and add it to cart and pay for it, indicating they want this Feature too
19. Clients are **not** be able to unflag a Feature that they previously flagged and paid for

20. Vendor-side users are able to filter the Features list by a Features Filter which allows the user to select:
    - Features Assigned to the Logged in user only
    - All Features
21. Vendor-side users are able to filter the Features list by Status, and Client
22. Vendor-side users are able to sort the Features list by Total Amount Paid for the Feature


23. Issue / Feature **Issue/Feature Logging Page**:
   - Client-side users only may input new Issues/Features
   - When the user selects to add a new Issue/Feature, the Issue/Feature Logging page will open
   - The user may select the Software Component from a dropdown box
   - The user may select the user the Issue/Feature is assigned to from a dropdown box
   - The user may select the Priority (for Issues only) from a dropdown box
   - The user may input the Title, Summary, and Details
   - The user may choose to upload an image
   - The user may not change the Status from 'DRAFT' when logging a new Issue/Feature
   - The user may not input a price when inputting a new Feature

24. Issue / Feature **Details Page**:
   - If the user inputs a new Issue/Feature or selects the 'more' icon from the Issues/Features List:
     + The details screen will open showing the Issue/Feature details 
     + The user can click the comments icon to open the comments dashboard, where they can click on the '+' icon to add a comment or on the 'eye' icon to      show/hide a list of existing comments
     + The user will be able to go back to the list page on which they clicked the 'more' icon by clicking on the 'Back to list' link
   
   - If the user selects the 'comments' icon from the Issues/Feature List:
     + The details screen will open with the comments dashboad and the list of comments for that Issue/Feature already showing
     + The user may use the 'comments' icon, and the comments dashboard to clear the comments or add a new comment
     + The user will be able to go back to the list page on which they clicked the 'comments' icon by clicking on the 'Back to list' link

25. Issue / Feature **Issue/Feature Editing**:
    - Client-side users only may edit Issues/Features
    - The 'Edit' option will appear on the Issue/Feature details page, if the Issue/Feature is still at a status of 'DRAFT' or 'LOGGED'
    - The user may change all the details that are input when an Issue/Featur is logged
    - In addition they can change the Status from 'DRAFT' to 'LOGGED'

26. Issue / Feature **Issue/Feature Updating**:
    - Client-side users and Vendor-side users may update Issues/Features
    - For Client-side users, the 'Update' option will appear on the Issue/Feature details page, if the Issue/Feature is no longer at a status of 'DRAFT' or   'LOGGED'
    - For vendor-side users the 'Update' option will appear on the Issues/Details page for all the Issues/Feature that they can view
    - The Client-side user may update the User the Issue/Feature is assigned to on the Client side only
    - For Issues and Features, the Vendor-side user may update the Software Component, Status, and the User the Issue/Feature is assigned to on the Vendor     side
    - For Features, the Vendor-side user may update the Price

27. Client-side users are able to run an Issues report that:
    - (a) Shows a rolled up total line for the Client, showing the number of Issues input and/or flagged by the Client, 
    - (b) Allows the user to click on a rolled up total line to show/hide the list of Issues underneath
    - (d) Lists the Issues in Priority order, from most urgent to least urgent

28. Client-side users are able to run a Features report that:
    - (a) Shows a rolled up total line for the Client, showing the number of Features input and/or flagged by the Client, and the total amount the Client        has paid for Features
    - (b) Allows the user to click on a rolled up total line to show/hide the list of Features underneath
    - (c) Lists the Features in order of amounts paid by the Client per Feature, from highest to lowest

29. Vendor-side users are able to run an Issues report that:
    - (a) Shows a rolled up total line for each Client, showing the number of Issues input and/or flagged by the Client, 
    - (b) Orders the rolled up total lines by the number of Issues per client, from highest to lowest
    - (c) Allows the user to click on a rolled up total line to show/hide the list of Issues underneath
    - (d) Lists the Issues in Priority order, from most urgent to least urgent

30. Vendor-side users are able to run a Features report that:
    - (a) Shows a rolled up total line for each Client, showing the number of Features input and/or flagged by the Client, and the total amount the Client       has paid for Features
    - (b) Orders the rolled up total lines by the total amount paid, from highest to lowest
    - (c) Allows the user to click on a rolled up total line to show/hide the list of Features underneath
    - (d) Lists the Features in order of amounts paid by the Client per Feature, from most highest to lowest
     
    
31. In the interests of data protection:
    - Clients are **not** be able to see another client's client code or name, nor the user id of a user who is associated with another client (this         includes user ids shown on Issues, Features, and on Comments)
    - Clients are **not** be able to edit / update another client's Issues / Features
    - A client does **not** have access to another client's Reports
 
 32. Since there is a contract between the Vendor and the Client the above data protection restrictions are not applied to Vendor-side users.
    


### **3.1.4 DJANGO DATABASES**

#### 3.1.4.1	VENDOR DATABASE

   The Vendor is _KMcD Accounting Solutions_. The Vendor details will be input via Django Admin. 
   There will only be **one** record in this database.
   

|Field Name        |Description                                   |Validation                     |
|------------------|----------------------------------------------|-------------------------------|
|vend_code	       |Uniquely identifies the Vendor                | 6 alpha-numeric characters.   |                   
|vend_name	       |Vendor Name                                   | Up to 50 characters           |                   
|vend_address      |Vendor Address                                | Up to 100 characters          |                   
|vend_city         |Vendor City                                   | Up to 30 characters           |                   
|vend_country      |Vendor Country                                | Up to 30 characters           |                   
|vend_email_addr   |Vendor Email Address                          | Up to 64 characters           |                   
|vend_contact_nr   |Vendor Contact Number                         | Up to 20 characters           |                   


#### 3.1.4.2	CLIENT DATABASE

   This database will contain the details of all the Clients using _KMcD Accounting System_. 
   The details will be input via Django Admin.

|Field Name        |Description                            |Validation                      |
|------------------|---------------------------------------|--------------------------------|
|client_code	    |Uniquely identifies the Client         | 6 alpha-numeric characters.    |                   
|                  |                                       | Uniquely identifies the Client |                   
|client_name       |Client Name                            | Up to 50 characters            |                   
|client_address    |Client Address                         | Up to 100 characters           |                   
|client_city       |Client City                            | Up to 30 characters            |                                     
|client_country    |Client Country                         | Up to 30 characters            |                   
|client_email_addr |Client Email Address                   | Up to 64 characters            |                   
|client_contact_nr |Client Contact Number                  | Up to 20 characters            |                   


### 3.1.4.3	USERDETAILS DATABASE

   Details of Users associated with the Vendor, _KMcD Accounting Solutions_, will be input via Django Admin.
   Details of Users, associated with the Clients who use _KMcD Accounting System_, will be input via Django Admin.
   
   When a user registers via the Issue Tracker, they will be registered as a Django Admin user. However, in order to
   get access to the Issue Tracker, they must be set up in the User Details database.
   
   This Database tells us about the user's relationship with the Issue Tracker. 
   The user may be working for either the Vendor or for a Client of the Vendor.
   The User Type indicates which - 'V'=Vendor; 'C'=Client.


|Field Name        |Description                       |Validation                                   | DB Links  |
|------------------|----------------------------------|---------------------------------------------|-----------|
|user_id     	    |Uniquely identifies the User      | 10 alpha-numeric characters.                |           |
|                  |                                  | This must be same as the user's             |           |   
|                  |                                  | Django Admin Username                       |           |
|user_first_name   |User's First Name                 | Up to 20 characters                         |           |
|user_second_name  |User's Last Name                  | Up to 20 characters                         |           |
|user_type         |Vendor-side, or Client-side user  | 1 character:                                |           | 
|                  |                                  | = "V" for Vendor side user;                 |           | 
|                  |                                  | = "C" for Client side user                  |           |
|vend_client_code  |Vendor Code or Client Code        | The Vendor Code, if 'user_type' = "V";      | Vendor DB |      
|                  |                                  | Otherwise, Client Code of the user's client | Client DB |
|user_email_addr   |User's Email Address              | Up to 64 characters                         |           |
|user_contact_nr   |Client Contact Number             | Up to 20 characters                         |           |


#### 3.1.4.4	ISSUES DATABASE

Issue details will be input by users who are associated with the Clients who use _KMcD Accounting System_.

|Field Name           |Description                       |Validation                                  | DB Links       |
|---------------------|----------------------------------|--------------------------------------------|----------------|
|issue_id     	       |Uniquely identifies the Issue     | Generated automatically by Django          |                |
|input_date  	       |The date the Issue was input      | Updated automatically with today's date    |                |
|client_code  	       |The client who input the Issue    | Copied from the UserDetails of the User    | Client DB      |
|                     |                                  | who input the Issue                        |                |
|software_component   |The part of the Accounting System | Selected from a dropdown list by the user  |                |
|                     |the issue has arisen on           |                                            |                |
|user_id              |ID of user who input the Issue    | Copied from the UserDetails of the user    | UserDetails DB |
|                     |                                  | who input the issue                        |                |
|assigned_client_user |The id of the user the issue is   | Initially set to the id of the input user  | Client DB      |
|                     |assigned to on the Client side    |                                            |                |
|assigned_vendor_user |The id of the user the issue is   | Initially set to the 'admin'               | Vendor DB      |
|                     |assigned to on the Vendor side    |                                            |                |
|title                |Brief title for the Issue         | Max 50 chars. Entered by the user when     |                |
|                     |                                  | logging the Issue                          |                |
|summary              |Brief summary for the Issue       | Max 100 chars. Entered by the user when    |                |
|                     |                                  | logging the Issue                          |                |
|details              |Detailed description of the Issue | Max 700 chars. Entered by the user when    |                |
|                     |                                  | logging the Issue                          |                |
|priority             |Priority of the issue.            | 1 char, value 1 - 5. Selected from a       |                |
|                     |                                  | dropdown list by the user                  |                |
|status               |Status of the Issue               | Initially set to "DRAFT"                   |                |
|thumbs_up_count      |The number of individual Clients  | Incremented each time a different Client   |                |
|                     |who have flagged the Issue        | 'thumbs up' the Issue                      |                |
|image                |Users may upload an image for     |  Image upload is optional                  |                |
|                     |the Issue                         |


#### 3.1.4.5	ISSUE COMMENTS DATABASE

Issue comments will be input by vendor-side and client-side users.

|Field Name           |Description                      |Validation                                 |DB Links        |
|---------------------|---------------------------------|-------------------------------------------|----------------|
|issue_id     	       |Identifies the Issue the comment | Copied from the Issues Database id field  | Issues DB      |
|                     |relates to                       |                                           |                |  
|input_date  	       |The date the comment was input   | Updated automatically with today's date   |                |
|vend_client_ind      |Indicates whether the user is on | Copied from the UserDetails of the        |                | 
|                     |the Vendor or Client side        | input user                                |                |
|vend_client_code     |Either the Vendor Code or the    | Copied from the UserDetails of the user   | Vendor DB      |
|                     |Client Code                      | who input the comment                     | Client DB      |
|user_id              |ID of the user who input the     | Copied from the UserDetails of the user   | UserDetails DB |
|                     |Comment                          | who input the comment                     |                |     
|comments             |The comment input by the user    | Max 300 characters.                       |                |


#### 3.1.4.6	ISSUE 'THUMBS UP' DATABASE

Each time a client inputs an Issue, a record will be created in the DB for that Issue, with the 'thumbs_up' field = '0'. This field is used for the 
'thumbs up' processing in 'app2_user_home/views.py'.
Clients will not be able to 'thumb up' their own Issues. Each time they 'thumb up' another clients' Issue, a record will be added to this database, with 'thumbs_up' field = '1'.

|Field Name           |Description                 |Validation                       |DB Links        |
|---------------------|----------------------------|---------------------------------|----------------|
|issue_id     	       |Identifies the Issue that   | Copied from the Issues Database | Issues DB      |
|                     |is being 'thumbed up'       | id field                        |                |
|client_code          |The Client Code of the user | Copied from the UserDetails of  | Client DB      |
|                     |                            | the user                        |                | 
|author               |The Client Code of the Issue| Copied from the Issue record    | Issues DB      |
|                     |being thumbed up            |                                 |                |
|user_id              |ID of the user who          | Copied from the UserDetails     | UserDetails DB |
|                     |'thumbed up' the Issue      | of the user                     |                |    
|thumbs_up            |Thumbs up value             | = '0' where the client is also  |                |
|                     |                            | the author. Otherwise set to '1'|                |


#### 3.1.4.7	FEATURES DATABASE

Feature details will be input by users who are associated with the Clients who use _KMcD Accounting System_.

|Field Name           |Description                       |Validation                                  | DB Links       |
|---------------------|----------------------------------|--------------------------------------------|----------------|
|feature_id           |Uniquely identifies the Feature   | Generated automatically by Django          |                |
|input_date  	       |The date the Feature was input    | Updated automatically with today's date    |                |
|client_code  	       |The client who input the Feature  | Copied from the UserDetails of the User    | Client DB      |
|                     |                                  | who input the Feature                      |                |
|software_component   |The part of the Accounting System | Selected from a dropdown list by the user  |                |
|                     |the Feature is required for       |                                            |                |
|user_id              |ID of user who input the Feature  | Copied from the UserDetails of the user    | UserDetails DB |
|                     |                                  | who input the Feature                      |                |
|title                |Brief title for the Feature       | Max 50 chars. Entered by the user when     |                |
|                     |                                  | logging the Feature                        |                |
|summary              |Brief summary for the Feature     | Max 100 chars. Entered by the user when    |                |
|                     |                                  | logging the Feature                        |                |
|details              |Detailed description of the       | Max 700 chars. Entered by the user when    |                |
|                     |Feature                           | logging the Feature                        |                |
|paid                 |Total amount paid for this Feature| Amounts paid for this Feature are added    |                |
|                     |                                  | to this field                              |                |
|status               |Status of the Feature             | Initially set to "DRAFT"                   |                |
|assigned_client_user |The id of the user the Feature is | Initially set to the id of the input user  | Client DB      |
|                     |assigned to on the Client side    |                                            |                |
|assigned_vendor_user |The id of the user the Feature is | Initially set to the 'admin'               | Vendor DB      |
|                     |assigned to on the Vendor side    |                                            |                |
|price                |The unit price for the Feature    | The price will be set by the Vendor        |                |
|client_count         |The number of individual Clients  | Incremented each time a different Client   |                |
|                     |who have aid for this Feature     | pays for the Feature                       |                |
|image                |Users may upload an image for     |  Image upload is optional                  |                |
|                     |the Feature                       |


#### 3.1.4.8	FEATURE COMMENTS DATABASE

Feature comments will be input by vendor-side and client-side users.

|Field Name           |Description                      |Validation                                 |DB Links        |
|---------------------|---------------------------------|-------------------------------------------|----------------|
|feature_id           |Identifies the Feature the       | Copied from the Features Database id field| Features DB    |
|                     |commentrelates to                |                                           |                |  
|input_date  	       |The date the comment was input   | Updated automatically with today's date   |                |
|vend_client_ind      |Indicates whether the user is on | Copied from the UserDetails of the        |                | 
|                     |the Vendor or Client side        | input user                                |                |
|vend_client_code     |Either the Vendor Code or the    | Copied from the UserDetails of the user   | Vendor DB      |
|                     |Client Code                      | who input the comment                     | Client DB      |
|user_id              |ID of the user who input the     | Copied from the UserDetails of the user   | UserDetails DB |
|                     |Comment                          | who input the comment                     |                |     
|comments             |The comment input by the user    | Max 300 characters.                       |                |



#### 3.1.4.9	FEATURE PAID DATABASE

Each time a client pays for a different Feature, a record will be created in the DB for that Client and Feature. If a Client pays more money for a Feature
they have already paid for, the amount will be added to this record.

|Field Name           |Description                 |Validation                       |DB Links        |
|---------------------|----------------------------|---------------------------------|----------------|
|feature_id     	    |Identifies the Feature that | Copied from the Features DB     | Feature DB     |
|                     |is being paid for           | id field                        |                |
|client_code          |The Client Code of the user | Copied from the UserDetails of  | Client DB      |
|                     |                            | the user                        |                | 
|author               |The Client Code of the      | Copied from the Feature record  | Client DB      |
|                     |Feature being paid for      |                                 |                |
|user_id              |ID of the user who          | Copied from the UserDetails     | UserDetails DB |
|                     |paid for the Feature        | of the user                     |                |    
|quantity             |The number of units paid for| Numerical value                 |                |
|                     |by the user                 |                                 |                |
|amount_paid          |The total amount paid for   | Decimal value                   |                |
|                     |this Feature by this client |                                 |                |




#### 3.1.4.10 FEATURE ORDER - CLIENT DETAILS

The Ordering Client details are added to the Order at Checkout.

|Field Name           |Description                         |Validation                                  |
|---------------------|------------------------------------|--------------------------------------------|
|full_name     	    |Ordering Client's Name              | Max chars = 50. Input by the user          |
|phone_number         |Ordering Client's phone number      | Max chars = 20. Input by the user          |
|country              |Ordering Client's country           | Max chars = 40. Input by the user          |
|postcode             |ordering Client's post code         | Max chars = 20. Input by the user          |
|town_or_city         |Ordering Client's town/city         | Max chars = 40. Input by the user          |
|street_address1      |Ordering Client's address line 1    | Max chars = 40. Input by the user          |
|street_address2      |Ordering Client's address line 2    | Max chars = 40. Input by the user          |
|county               |Ordering Client's address line 2    | Max chars = 40. Input by the user          |
|date                 |The date the order is made          | Updated automatically with today's date    |


#### 3.1.4.11 FEATURE ORDER - ORDER LINE

The Features being paid for are added to the Order lines at Checkout.

|Field Name           |Description                                 | 
|---------------------|--------------------------------------------|
|order         	    |Foreign Key to above Ordering Client Details| 
|feature         	    |Foreign Key to the Feature being paid for   | 
|quantity      	    |The number of units being paid for          | 



## **3.4 FEATURES LEFT TO IMPLEMENT**

1. Allow archiving of Closed Issues & Features


# **5. TECHNOLOGIES USED**

|Technologies                 |Website                                                                   |
|-----------------------------|--------------------------------------------------------------------------|
|HTML                         |[w3schools](https://www.w3schools.com/)                                   |
|CSS                          |[w3schools](https://www.w3schools.com/)                                   |
|Javascript                   |[MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript)   |
|Jquery                       |[jQuery website](https://code.jquery.com/)                                |
|Bootstrap                    |[Bootstrap website](https://getbootstrap.com/)                            |
|Font Awesome                 |[Font Awesome website](https://fontawesome.com/)                          |
|AutoPrefixer                 |[Autoprefixer website](https://autoprefixer.github.io/)                   |
|Django                       |[django documentation](https://docs.djangoproject.com/en/3.0/)            |
|AWS s3 Buckets               |aws.amazon.com                                                            |
|Stripe Payments              |https://stripe.com/ie                                                     |


      


|Features            |Website                                                                            |COMMENTS                                                                                                 |
|--------------------|-----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------- ----|
| Color Scheme       |[Color Wheel](https://www.canva.com/colors/color-wheel/)                           |I used this websiteto choose the base colors for my website.                                              |                                                                    
| Colors             |[w3schools](https://www.w3schools.com/colors/colors_picker.asp)                    |I used this website to get different shades of the base colors.                                          |
| Web page layouts   |[bootstrap](https://getbootstrap.com/)                                             |I used bootstraps container, row and column classes to create my page layouts and to make them responsive |         
| Navigation bar     |[bootstrap](https://getbootstrap.com/)                                             |I used bootstraps nav bar classes to create my navigation bars, and burger menu.                     |         
| Wireframes         |[Figma](https://www.figma.com/file/g5LWnVMBRVwuMGNSxHS7qb/Home-Page?node-id=71%3A1)|I used figma when designing my website. See screen shots in Design folder on github                      |
|Django Pagination   |https://django-el-pagination.readthedocs.io/en/latest/digg_pagination.html         |I used django pagination to create the paginate functionality on the Issues and Features Lists        |
|Microsoft Publisher |https://www.microsoft.com/en-ie/default.aspx                                       | I used Publisher to create logic & workflow diagrams                                              |


# **6. TESTING**

## **6.1 Manual Testing**

### **6.1.1. User Setup**

You may get access to Django Admin with user id/psw = admin/isstrk.123. However I have also preset some details, as explained below, to save testers setting up details via Django Admin.

In order for users to have access to the app, they must be registered on Django Admin and have a corresponding record in the UserDetails database. Users may register on the Issue Tracker app, but the UserDetails record needs to be set up via Django Admin:


![alt text](/Design/system-diagrams/user-setup.png "Issue Tracker User Setup")


I have set up a number of user codes on the UserDetails database, which don't have corresponding Django Admin users registered. This is to allow testers to register via the app with these user codes and have immediate access to the Issue Tracker.

The app has a Vendor perspective and a Client perspective, therefore it is necessary to be able to distinguish the different types of users. 

There are two types of users: Vendor-side users (users who work for the Vendor), and Client-side users (users who work for a Client of the Vendor)

#### 6.1.1.1 Vendor-side Users

The following table shows:
 - Vendor-side users already registered and set up on the UserDetails database. Testers may log in with these usernames and passwords 
 - Vendor-side users set up on the UserDetails database only. Registering as new users on the Issue Tracker with these codes will give immediate access to      the Issue Tracker


|Vendor Code   |Usernames Registered | Passwords    | Usernames on UserDetails |
|--------------|---------------------|--------------|--------------------------|
| KMCD01       | venduser01          | venduser01   | venduser01               |
|              | venduser02          | venduser02   | venduser02               |
|              | venduser03          | venduser03   | venduser03               |
|              |                     |              |                          |
|              |                     |              | venduser04               |
|              |                     |              | venduser05               |
|              |                     |              | venduser06               |
|              |                     |              |                          |

#### 6.1.1.2 Client-side Users

The following table shows:
 - Client-side users already registered and set up on the UserDetails database. Testers may log in with these usernames and passwords 
 - Client-side users set up on the UserDetails database only. Registering as new users on the Issue Tracker with these codes will give immediate access to      the Issue Tracker

|Client Code   |Usernames Registered | Passwords    | Usernames on UserDetails |
|--------------|---------------------|--------------|--------------------------|
| C00001       | c1_user001          | c1_user001   | c1_user001               |
|              | c1_user002          | c1_user002   | c1_user002               |
|              | c1_user003          | c1_user003   | c1_user003               |
|              |                     |              |                          |
|              |                     |              | c1_user004               |
|              |                     |              | c1_user005               |
|              |                     |              |                          |
|              |                     |              |                          |
| C00002       | c2_user001          | clt2usr1     | c2_user001               |
|              |                     |              |                          |
|              |                     |              | c2_user002               |
|              |                     |              | c2_user003               |
|              |                     |              |                          |
|              |                     |              |                          |
| C00003       | c3_user001          | c3_user001   | c3_user001               |
|              |                     |              |                          |
|              |                     |              | c3_user002               |
|              |                     |              | c3_user003               |
|              |                     |              |                          |

### **6.1.2 Details of Vendor, Clients, Users**

##### 6.1.2.1 The Vendor

These are the details of the Vendor that are set up in the **Vendor** database:

|Vendor Code   |Name                       | 
|--------------|---------------------------|
| KMCD01       | KMcD Accounting Solutions | 


#### 6.1.2.2 The Clients

These are the details of the Clients that are set up in the **Client** database:

|Client Code   |Name                       | 
|--------------|---------------------------|
| COOO1        | Small Business Ltd        | 
| COOO2        | Medium Business Ltd       | 
| COOO3        | Breaking Ground Ltd       | 


#### 6.1.2.3 The Users

These are the details of the users that are set up in the **UserDetails** database:

|Use Code      |Name                       | Vendor / Client User |Registered on Django Admin?|
|--------------|---------------------------|----------------------|---------------------------|
| admin        | Superuser                 |     V                |           Y               |
| venduser01   | Vendor_user_1             |     V                |           Y               |     
| venduser02   | Vendor_user_2             |     V                |           Y               |  
| venduser03   | Vendor_user_3             |     V                |           Y               | 
| venduser04   | Vendor_user_4             |     V                |           N               |  
| venduser05   | Vendor_user_5             |     V                |           N               |  
| venduser06   | Vendor_user_6             |     V                |           N               |  
|              |                           |                      |                           |
|              |                           |                      |                           |
| c1_user001   | Client1_user_001          |     C                |           Y               |  
| c1_user002   | Client1_user_002          |     C                |           Y               |
| c1_user003   | Client1_user_003          |     C                |           Y               | 
| c1_user004   | Client1_user_004          |     C                |           N               |  
| c1_user005   | Client1_user_005          |     C                |           N               |
|              |                           |                      |                           |
|              |                           |                      |                           |
| c2_user001   | Client2_user_001          |     C                |           Y               |  
| c2_user002   | Client2_user_002          |     C                |           N               |
| c2_user003   | Client2_user_003          |     C                |           N               | 
|              |                           |                      |                           |
|              |                           |                      |                           |
| c3_user001   | Client3_user_001          |     C                |           Y               |  
| c3_user002   | Client3_user_002          |     C                |           N               |
| c3_user003   | Client3_user_003          |     C                |           N               | 
|              |                           |                      |                           |



### 6.1.3 Testing Registration / Login Page

When the Issue Tracker app loads initially it will be on the Registration / Login page.

#### 6.1.3.1 Pre-Login Navigation

1. Confirm that the app remains on this page when you clicking on the logo and the home icon
2. Confirm that clicking on both 'Register' in the navigation bar, and 'Register' on the page message brings you to the Registration page
3. Confirm that clicking on both 'Login' in the navigation bar, and 'Please Login' on the page message brings you to the Login page


#### 6.1.3.2 Register

1. Click 'Register' 

2. Input the details of a brand new user with email address = "kittymcdonagh@gmail.com" and confirm the error "email address must be unique" is returned
 
3. Test password input to ensure it doesn't allow the input in the 2 password fields to be different

4. Enter valid details for a brand new user and confirm you are returned to the Registration / Login page and that the message "You have registered              successfully! **Contact the System Administrator about setting you up on the Issue Tracking Sytem**" is displayed just above the welcome message.

5. Register as one of the unregistered Vendor User codes in the above table, and confirm the same message is received as above

6. Register as one of the unregistered Client User codes in the above table, and confirm the same message is received as above


#### 6.1.3.3 Login

1. Attempt to log in as the brand new user and confirm that you get the message "User not set up on the Issue Tracking System".

2. Login with a Vendor user code you registered above and confirm that the Issue Tracker page loads with 'KMcD Accounting Solutions' showing on the left of    the top line of the screen and 'Welcome, _user name_!' (see above user table for correct user name) in the middle of the top line of the screen

4. Login with the Client User code you registered above and confirm that the Issue Tracker page loads with the relevant Client Code and Client Name (see         Client table above for correct name) showing on the left of the top line of the screen and 'Welcome, _user name_!' (see above user table for correct user     name) in the middle    of the top line of the screen

5. If you wish, add the brand new user you created above to the UserDetails database via Django Admin, as a Vendor-side user. Then log in as that user and         confirm that the Vendor name and the user name showing on the screen are correct

6. If you wish, register as a new user, and set yourself up via Django Admin, as a Client-side user. Then log in as that user and confirm that the Company       name and the user name showing on the screen are correct


#### 6.1.3.4 Post-Login Navigation

1. Log in as a **Client-side** user 
2. Click on the logo and on the home icon and confirm that they display the same page showing the messages "You are already logged in!", and "Please go to       Issue Tracking System or Logout"
3. Clck on 'Issue Tracking System' in the page message and confirm it takes you to the Issues List
4. Confirm that the top navigation bar contains the following options 'Issues List'(enabled), 'Add Issue'(enabled), 'Features List'(enabled), 'Add               Feature'(enabled), and cart(disabled)
5. Confirm the following options appear in the Footer - Issues List, Features List
6. Log in as a **Vendor-side** user and confirm that the top navigation bar contains the following options 'Issues List'(enabled), 'Add Issue'(**disabled**),        'Features List'(enabled), 'Add Feature'(**disabled**), and cart(disabled)


#### 6.1.3.5 Profile

1. While logged in as a Vendor-side user, click on 'Profile' and confirm you are brought to a page showing the Vendor Name, Username and Email Address.

2. While logged in as a Client-side user, click on 'Profile' and confirm you are brought to a page showing the Company Name, Username and Email Address.


#### 6.1.3.6 Logout

While still logged in as a Vendor-side or Client-side user click on the 'Logout' and confirm that you are brought to the Registration & Login page.


#### 6.1.3.7 Forgot Password

In order to test this, you need to set yourself up as a user on the Issue Tracker and add a valid email account to your Django Admin User profile.

1. Click 'Forgot Password' and confirm you are requested for an email address

2. Enter the email address of the Django User you set up above. Click 'Reset Password'

3. Confirm you receive a Django Admin message confirming a password has been sent to the email account

4. Retrieve the email and reset the password

5. Log into the Issue Tracker with the username and new password, and confirm the password was changed

#### Please Note

The email address from which the email is being sent is a gmail account which allows access to less secure apps, and 2-step authentication is not set. This was all working fine when I set it up a few months back

However, when I was ran this functionality again, while writing this section of the readme file, I started getting a 'SMTPAuthenticationError'. The reset email was also a gmail account.

After checking the error message online, and not getting any answers I tried tutor support. They suggested running "https://accounts.google.com/DisplayUnlockCaptcha", after which the emails were sent to the gmail account, and I could reset the password. I ran the reset password a few more times using the gmail account, and it worked fine each time.

Then I decided to send the reset email to a hotmail account. It received the email ok. However when I try to send another reset email, either to the gmail or the hotmail account, I get a 'SMTPAuthenticationError' again. To clear this I run "https://accounts.google.com/DisplayUnlockCaptcha" again. However, it will consistently give me an error after sending to a hotmail account.

_I'm noting this here in case testers run into any issues._


### **6.1.4. Log/Edit/Update Issues & Features Testing**

1. Log in as the different **Client-side** users and select 'Add Issue' / 'Add Feature' from the navigation bar
2. Input the Title, upload an image, input Summary and Details, and Submit
3. Confirm Status cannot be changed from 'DRAFT' - only Clients who own the Issue / Feature can see it while at a Status of 'DRAFT'
4. Confirm the Issue / Feature Details are redisplayed
5. New Issues / Features are automatically assigned to the user who input them on the Client side, and to 'admin' on the Vendor side
6. Confirm that the 'Back to list' link on the Issue / Feature Details screen, takes you back to the Issues / Features List
7. Confirm that the Issue / Feature you just input is in the list
8. Select the Issue by clicking the 'more ('...') icon and click 'Edit' at the bottom of the Issue / Feature Details screen
9. Confirm that all details can still be changed
10. Confirm that the Status can only be changed to 'DRAFT' and 'LOGGED'
11. Change the Status to 'LOGGED' - only Clients who own it and Vendor-side users, can see Issue / Feature while at a Status of 'LOGGED'
12. Select the Issue / Feature again and confirm you can still edit the details as above, while it is at a status of 'LOGGED'
13. Log in as a **Vendor-side** user and select an Issue / Feature that is at a status of 'LOGGED'
14. Confirm that 'Update' I(instead of 'Edit') appears at the bottom of the Issue / Feature Details screen, and select it
15. Confirm you can only change the 'Assigned to' user, Status and Priority on Issues, and the 'Assigned to' user, Status and Price on Features
16. Change the Status to a value other than 'DRAFT' or 'LOGGED' - all Clients will now be able to see this Issue / Feature
17. Select the Issue / Feature for Update again, and confirm you can still change the same fields
18. Log in as a **Client-side** user again and select an Issue / Feature that belongs to the Client you're associated with 
19. Confirm that 'Update' (instead of 'Edit') appears at the bottom of the Issue / Feature Details screen
20. Select 'Update' and confirm you can only change the 'Assigned to' user
21. Select an Issue / Feature from the List and confirm that there is no option to Edit or Update it at the bottom of the Issue / Feature Details screen
22. Comments Input / Viewing:
    - (a) Select an Issue / Feature that belongs to the user's Client from the Issues List
    - (b) Click on the 'comments' icon and confirmit shows/hides a dashboard with options to Add or View comments
    - (c) Click on '+' / '-' in the dashboard to show/hide a comments input form
    - (d) Input a few comments
    - (e) From the Issues / Features List select an Issue / Feature that belongs to another Client
    - (f) Enter a comment as described above
    - (g) Go back to the Issues / Features List and click on the 'comments' icon for the Issues / Features you input the comments on
    - (h) Confirm the Issue / Features Details are shown with the comments list open
    - (i) When on the Issue / Features Details page, use the 'comments' icon and the 'view' icon in the dashboard to show/hide the comments on that Issue /        Feature


### **6.1.5. Issues List Testing**

**Notes**

- The client-side users c1_user001, c1_user002, and c1_user003 are all associated with the same Client - C00001. c2_user001 is associated with Client c000002,   and c3_user001 is associated with Client C00003
- The **Issues Filter** is the main filter - when you select a value from it, it resets all the other filters to 'ALL'. Whereas the Status, Priority and        Client filters, will take the value of the other 3 filters into account.
- Each time the Issues List reloads (except when you click 'Back to list' on Issue Details screen) it shows all Issues assigned to the logged in user, or an    empty list if nothing is assigned to them

1. First login as **Client** side use - c1_user001
2. Confirm that the Issues in the list are all 'Assigned to' the logged in user and are in order of id number - highest to lowest 
3. Select 'All Issues' from the Issues Filter - selecting a value from the Issues Filter will cause the Status and Priority Filters to be reset to 'ALL'
4. Confirm that all the 'Assigned to' user codes that are displayed are all associated with the same client as the logged in user - see above tables (users      should not be able to see the user codes of users that are associated with other clients)
5. Confirm that all the Issues at a Status of 'DRAFT' or 'LOGGED' belong to the same client as the logged in user - i.e. their Client Code is the same as the    one showing on the top left corner of the screen (users should not be able to see the Issues of other clients that are still at a status of 'DRAFT' or        'LOGGED')
6. Confirm that the 'thumbs up' icon is disabled for Issues that belong to the client the logged in user is associated with
7. Confirm that Issues that belong to other clients are showing "******" in the 'Assigned to' column
8. Confirm that the 'thumbs up/down' icon on Issues that belong to other clients, and that don't have a Status of 'DEPLOYED' or 'CLOSED', is enabled
9. Confirm that the 'thumbs up/down' icon on Issues that belong to other clients, and that do have a Status of 'DEPLOYED' or 'CLOSED', is disabled
10. Confirm that when you click on an enabled 'thumbs up' icon it changes to a 'thumbs down' icon and the number in the Flag column is incremented
11. Confirm that when you click on an enabled 'thumbs down' it changes to a 'thumbs up' and the number in the Flag column is decremented
12. Confirm that a 'thumbs down' is shown on Issues that have already been 'thumbed up' by the client associated with this user (i.e. it may have been            'thumbed-up' by a different user, but for the same client)
13. Enter text in the Search box - it will search for the text in the Issue Summary field of **all** Issues - and confirm that Issues with that text are          displayed and that the Issues, Status and Priority Filters are showing no values - this is to avoid confusing the user, since the Search searches all         Issues for the text input
14. Select "Our Issues Only" from the Issues Filter and confirm that the Issues displayed belong to the client the logged in user is associated with - the        'Assigned to' user code will be displayed for all of these and the 'thumbs up' icon will be disabled
15. Select "Other Clients' Issues Only" from the Issues Filter and confirm that the Issues displayed do not belong to the client the logged in user is            associated with - the 'Assigned to' column will show "******" for all of these, and the 'thumbs up' icon will be enabled for Issues that don't have a         status of 'DEPLOYED' or 'CLOSED'
16. Select "Assigned to Me" from the Issues Filter and confirm that only those Issues assigned to the logged in user are shown 
17. Select each Status value in turn from the Status Filter and confirm that only those Issues in the current list (as determined by the other Filters) with      that Status value are shown
18. When a Status value is selected for which there are no Issues with that value in the current list, confirm that an empty list is shown and that the           message "No issues found for the selected criteria!" is displayed
19. Select each Priority value in turn from the Priority Filter and confirm that only those Issues in the current list (as determined by the other Filters)       with that Priority value are shown
20. When a Priority value is selected for which there are no Issues with that value in the current list, confirm that an empty list is shown and that the         message "No issues found for the selected criteria!" is displayed

21. Login as users c1_user002 and/or c1_user003, who are be associated with the same client as the above user, and run through the above tests again 
22. Log in as c2_user001 and/or c3_user001, who are associated with a **different client** to the above users, and run through the above tests again 

23. Log in as **Vendor-side** user (eg. admin, venduser01). The Issues List will function as above, with the following exceptions:
    - (a) A Client Filter will appear on the screen, allowing the user to see Issues for the selected Client only
    - (b) The Issues Filter will have 2 options only - 'ASSIGNED TO ME' and 'ALL ISSUES'
    - (c) Issues with a Status of 'LOGGED' will show (Issues with a Status of 'DRAFT' will not show)
    - (d) The 'thumbs up' icon will be disabled on all Issues (the Vendor cannot flag an Issue)
    - (e) The Client Code will show on all Issues
    - (f) The 'Assigned to' user, will be the user the Issue is assigned to on the Vendor side


### **6.1.6. Features List Testing**

The Features List functions the same way as the Issues List, except for the following exceptions:
- The Priority Filter is replaced by Paid order - use can choose to order the current list (as determined by the other filters) by the amount paid per          Feature - 'LOWEST TO HIGHEST', or 'HIGHEST TO LOWEST'
- The 'thumbs up' icon is replaced by a '+cart' icon
- Only a Vendor-side user can set the price on a Feature, and only after the Feature reaches a status of 'LOGGED'

1. Select 'LOWEST TO HIGHEST' from the Paid Order dropdown and confirm the Features are listed starting with the lowest amount paid, to the highest amount       paid
2. Select 'HIGHEST TO LOWEST' from the Paid Order dropdown and confirm the Features are listed starting with the highest amount paid, to the lowest amount       paid
3. While logged in as a **Vendor-side** user:
   - Confirm that the '+cart' icon is disabled on all Features (Vendor-side users cannot pay for Features)
   - Select a Feature by clicking the 'more' ('...') icon and update the Feature's price, if it is still at zero
4. Log in as **Client-side** user 'c1_user001':
   - (a) Confirm that the '+cart' icon is disabled when the price is zero, and enabled when the price is greater than zero
   - (b) Confirm that the '+cart' icon is enabled (where the price is greater than zero) on all Features, regardless of who they belong to - i.e. a                 Client can pay for Features that they input, and Features that were input by other Clients
   - (c) Confirm that each time you click the '+cart' icon '1' is added to the cart in the navigation bar, and it becomes enabled (a user may click on the          same feature more than once, this will increment the quantity)
   - (d) Click on the 'cart' icon in the navigation bar and confirm that the items and quantities per item are correct
   - (e) Remove items from the cart by amending the 'quantity' to '0', and confirm the price is adjusted
   - (f) Remove all items from the cart and confirm the Features List is re-displayed and the 'cart' icon in the navigation bar is disabled
   - (g) Add items to the cart, select the cart and click 'checkout'
   - (h) Enter the payment details (card no. = 4242424242424242, cvv = '111', month/year in the future), and click 'Submit Payment'
   - (i) Confirm the message "You have successfully paid" is received, and the Feature List is redisplayed, and that the number in the flagged column for the       Features paid for has been incremented by '1' (this is the number of individual Clients who have paid for this Feature)
   - (j) Pay for another Feature, and confirm that the number in the flagged column has not been incremented
   - (j) Log in as user 'c2_user001' and pay for a Feature you paid for as user 'c1_user001'. Confirm that the number in the flagged column for this Feature        has been incremented by '1'

   
### **6.1.7 Issues Report Testing**

1. Log in as a **Client-side** user
2. Click on **Issues Report** in the Footer and confirm that one total line appears showing the total number of Issues input or flagged by the Client the       user is associated with
3. Click on the total line 'chevron' icon and confirm that it shows / hides the same number of Issues as is showing in the total line
4. Confirm that it is showing all the Issues input by the Client the user is associated with (the Client Code showing in the list will be the same as the        Client Code showing at the top left of the page) - all Issues will be included regardless of Status
5. Confirm that it is showing all the Issues that have been flagged by the Client the user is associated with (the Client Code on these Issues will show as      '******', as users can only flag other clients' Issues)
6. Confirm that the Issues are in order of Priority
7. Confirm that when you click on the 'chevron' icon in the 'Details' column, it will show / hide the Issue Details
8. Log in as a **Vendor-side** user
9. Click on **Issues Report** in the Footer and confirm that a total line appears for each Client, showing the total number of Issues input or flagged by       each Client, ordered by the number of Issues input or flagged, from highest to lowest
10. Click on a Client's total line 'chevron' icon and confirm that it shows / hides the same number of Issues as is showing in the total line
11. Confirm that it is showing all the Issues for that Client - all Issues will be included regardless of Status
12. Confirm that it is showing all the Issues that have been flagged by the Client 
13. Confirm that the Issues are in order of Priority
14. Confirm that when you click on the 'chevron' icon in the 'Details' column, it will show / hide the Issue Details
15. More than one Client may have flagged the same Issue, so the same Issue can appear on more than one Client Report


### **6.1.8 Feature Report Testing**

1. Log in as a **Client-side** user
2. Click on **Features Report** in the Footer and confirm that one total line appears showing the Total Paid, and the total number of Features input or         paid for by the Client the user is associated with
3. Click on the total line 'chevron' icon and confirm that it shows / hides the same number of Features as is showing in the total line
4. Confirm that it is showing all the Features input by the Client the user is associated with (the Client Code showing in the list will be the same as the        Client Code showing at the top left of the page) - all Features will be included regardless of Status
5. Confirm that it is showing all the Features that have been paid for by the Client the user is associated with - Clients can pay for their own Features and    for other Clients' Features - so the user's Client Code will appear on their own Features and '******' on other Clients' Features
6. Confirm that the Features are in order of Amount Paid - from highest to lowest
7. Confirm that when you click on the 'chevron' icon in the 'Details' column, it will show / hide the Feature Details
8. Log in as a **Vendor-side** user
9. Click on **Features Report** in the Footer and confirm that a total line appears for each Client, showing the Total Paid, and the total number of Features    input or paid for by each Client, ordered by the **Total Paid** - from highest to lowest
10. Click on a Client's total line 'chevron' icon and confirm that it shows / hides the same number of Features as is showing in the total line
11. Confirm that it is showing all the Issues for that Client - all Issues will be included regardless of Status
12. Confirm that it is showing all the Features that have been paid for by the Client 
13. Confirm that the Issues are in order of Amount Paid - from highest to lowest
14. Confirm that when you click on the 'chevron' icon in the 'Details' column, it will show / hide the Feature Details
15. More than one Client may have paid for the same Feature, so the same Feature can appear on more than one Client Report

### **6.1.9 Issues Responsiveness Testing**

The Issue Tracker has been designed with mobile-first design in mind, therefore it should be 
tested on devices will various size screens - Ipad, Table, Mobile Phones




## **6.2 Automated Testing**

Due to time constraints I didn't get around to creating automated tests.


    
# 7. DEPLOYMENT

## 7.1 DEPLOYING FROM GITHUB 

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


## 7.2 CLONING FROM GITHUB 

1. Follow this link to my [Project Repository on Github](https://github.com/KittyMcDonagh?tab=repositories)
2. On the repository page click "Clone or Download"
3. In the Clone with HTTPs section, copy the clone URL for the repository.
4. In your local IDE open Git Bash.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type git clone, and then paste the URL you copied in Step 3 - 
    "git clone https://github.com/KittyMcDonagh/kmcd-issue-tracking-project"
7. Press enter and your local clone will be created.


## 7.3 Deploying to Heroku

1. Log into heroku
   - Select new/create new app
   - New app = kmcd-issue-tracker / europe

2. Click on Resources
   - In add-ons type postgres - select Heroku Postgres
   - Select plan name - "Hobby Dev - free" and click "Provision"

3. Click on Settings. Click on Reveal Config Vars.
   - You will see DATABASE_URL with value "postgres://etc "
   - Copy the DATABASE_URL value

4. Go back to cloud9
   - In the terminal type "pip3 install dj-database-url"
   - And in the terminal type "sudo pip3 install psycopg2~=2.7.3.1"
   
5. Create the 'requirements.txt' file:
   - In the terminal type "pip3 freeze > requirements.txt"

6. Open 'settings.py' and point 'DATABASES' to 'dj_database_url'

7. Create env.py and hide the following as environment variables:
   - STRIPE_PUBLISHABLE
   - STRIPE_SECRET
   - DATABASE_URL
   - SECRET_KEY

8. Change settings.py to get the value of the above from the environment variables

9. In the terminal type "python3 manage.py makemigrations" (no changes)
10. In the terminal type "python3 manage.py migrate" (all existing migrations are migrated to the new postgres database)

11. As this is a brand new database, a new superuser must be created

12. Sign into AWS Account and set up an S3 bucket for 'kmcd_issue_tracker'

13. Add s3 to Django
    - Install django-storages
    - Install boto3
    - Add 'storages' to INSTALLED_APPS in settings.py
    - Add the environment variables AWS Access Key ID and Secret Access key to settings.py 
    
14. Add the AWS Access Key ID and Secret Access key to env.py

15. Create custom_storages.py in the project root and create the classes for s3 to separate the images uploaded to the Issue Tracker from static files
16. Update the Static File and Media File Storage in settings.py to point to the location set up in custom_storages
17. From the terminal type 'python3 manage.py collectstatic'
18. From the terminal run 'pip3 freeze > requirements.txt'

19. Log into travis-ci.org 
20. Click on the project name - 'kmcd-issue-tracking-project'
    - The page will show 'build unknown' for this project
    - Click on 'unknown', in the 'format' field of the box that comes up select 'markdown'
    - Copy the text that is shown in the 'result' field, and paste it into the end of the readme file.:
      [![Build Status](https://travis-ci.org/KittyMcDonagh/fsf-ecommerce-project.svg?branch=master)](https://travis-ci.org/KittyMcDonagh/fsf-ecommerce-project)

21. Create ".travis.yml" at project root level:
      language: python
      python:
          - "3.6"
      install: "pip install -r requirements.txt"
      script:
          - SECRET_KEY="whatever" ./manage.py test

22. Add the following changes to settings.py to stop travis generating errors:

    - # Travis will generate an error trying to import env.py. This if statement will stop it trying to import it:
        if os.path.exists('env.py'):
            import env               

    - # Travis will generate an error trying to find dj_database_url. This if statement will stop it looking for it:
        if "DATABASE_URL" in os.environ:
          DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL')) }   
        else:                                                                                                                            
          print("Database URL not found. Using SQLite instead.")
          
          DATABASES = {
              'default': {
                  'ENGINE': 'django.db.backends.sqlite3',
                  'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
          }
      }

23. From the c9 terminal do a git add, commit and push

24. Check to see if travis build worked - you should see 'build passing' at the bottom of your github repository page.

25. Back to Heroku and add the environment variables to 'config vars:
    - STRIPE_PUBLISHABLE
    - STRIPE_SECRET
    - SECRET_KEY
    - DATABASE_URL
    - AWS_ACCESS_KEY_ID
    - AWS_SECRET_ACCESS_KEY

26. Click on Deploy
    - Click 'connect to github'
    - Enter repo name - "kmcd-issue-tracking-project"
    - Click 'connect

27. Back to c9 terminal and type "sudo pip3 install gunicorn"
28. Copy "gunicorn==20.0.4" into requirements.txt (don't re-generate it, otherwise it will add back in what was taken out to make travis build successfully)
29. Create a Procfile with the line "web: gunicorn kmcd_issue_tracker.wsgi:application"
30. From the c9 terminal do a git add, commit and push
31. To stop heroku from collecting static add the config var 'DISABLE_COLLECTSTATIC' with value = 1  
32. Click on 'Deploy' and 'Deploy Branch'
33. Update ALLOWED_HOSTS in settings.py to allow 'kmcd-issue-tracker.herokuapp.com'
34. Run the heroku app
35. 



# **8. CREDITS**

## **8.1 CONTENT**

### **8.2 IMAGES AND ICONS USED ON ISSUE TRACKER **

The following icons/images were used to create the overview diagram of the Issue Tracking System:

|IMAGEs USED ON ISSUES & FEATURES       |Owner
|---------------------------------------|-----------------|
|I took all these photos myself         | Kitty McDonagh  |


|IMAGE / ICON in flow diagrams          |COPIED FROM
|---------------------------------------|-------------------------------------------------------------------------|
|Questions Comments Concerns icon       |http://clipart-library.com/clipart/ziXoGpb7T.htm                         |
|Client group icon                      |http://clipart-library.com/clipart/1745500.htm                           |
|Group sitting around globe of world    |http://clipart-library.com/img1/1474499.jpg                              |
|Online Server image                    |http://clipart-library.com/clipart/99610.htm                             |
|Online computer image                  |http://clipart-library.com/image_gallery2/Hosting-Free-Download-PNG.png  |
|Blue user image                        |http://clipart-library.com/clipart/2038276.htm                           |
|Orange user image                      |http://clipart-library.com/clipart/rcLnpabKi.htm                         |
|Grey user image                        |http://clipart-library.com/clipart/773211.htm                            |
|                                       |                                                                         |


## **8.2 TEXT USED FOR ISSUES / FEATURES DETAILS**

|DESCRIPTION                                    |COPIED FROM
|-----------------------------------------------|-----------------------------------------------|
|Lorem ipsum text for Issues/Features details   |https://loremipsum.io/generator/               |
|                                               |                                               |



## **CODE SNIPPETS**

|Description of problem                             |Solution found on
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| I had tuples of (client, total number of issues)  | https://www.geeksforgeeks.org/python-list-sort/)                                                      |
| and I needed to  sort by the 2nd parameter        |                                                                                                       |
|                                                   |                                                                                                       |
| I needed to insert a new record into a Django db  | https://stackoverflow.com/questions/35602049/how-to-insert-data-to-django-database-from-views-py-file |
|                                                   |                                                                                                       |
| Although not in the video,                        | Help received from Slack with this when creating OrderLineItem(models.Model)                          |
| "on_delete=models.CASCADE," needs to be           |                                                                                                       |
|  added to 'ForeignKey' otherwise you get a red x  |                                                                                                       |
|                                                   |                                                                                                       |
| # MEDIA_URL = '/media/' didn't work for me        | I found "MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)" on Slack  and    |
| after I set up s3 Buckets                         | it worked!  There's no mention of this change in the lessons (perhaps because they were still on the  |
|                                                   | old c9)                                                                                               |
|                                                   |                                                                                                       |
| Cart & Checkout functionality                     | The code was initially copied from the e-commerce project we did as part of  the course and adjusted  |
| Strip payments                                    | js code copied from stripe.com as per e-commerce project                                              |



## **8.3 ACKNOWLEDGEMENTS**

|NAME                          |COMMENTS
|------------------------------|---------------------------------------------------------------------------------------------------------------------------|
|The Code Institute            |I learnt everything I needed to know to build this website from the Code Institute.                                        |
|Fellow students on Slack      |I received a lot of assistance and feedback from students on Slack which improved my project.                              |
|My mentor Seun Owonikoko      |I received assistance, feedback and encouragement from Seun.                                                               |
|@mormoran (Andy) on Slack     |Helped me to create functions that called python views for dislaying Issues/Features list based on various user selections |



[![Build Status](https://travis-ci.org/KittyMcDonagh/kmcd-issue-tracking-project.svg?branch=master)](https://travis-ci.org/KittyMcDonagh/kmcd-issue-tracking-project)



