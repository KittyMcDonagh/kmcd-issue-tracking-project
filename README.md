**_KMcD Software Solutions_ - ISSUE TRACKER**  
======================

![alt text](/static/images/headfordsunset.jpg "Headford Sunset")
======================

# **INTRODUCTION**

## **1.1 PURPOSE**

The purpose of the [Issue Tracker](https://kmcd-issue-tracker.herokuapp.com/issue_tracker/apphome/) is to allow clients to log the issues that they are experiencing with the _KMcD Online Accounting System_, as well as request new features. The issue tracker will provide a common area where all Clients can log their issues and request features. They will be able to see each others' issues and features, comment on them, and upvote them if they have the same issue, or want the same feature.

While bugs will be fixed for free, upvoting new features will cost a certain amount of money depending on the complexity of the requested feature (this will be decided on per feature by the Vendor).

The issue tracker will be used by both the vendor (_KMcD Accounting Solutions_) and clients to monitor the progress of issues & features.

The app employs data protection policies in not allowing clients to see each others client codes, client details, or user ids.


## **1.2 BACKGROUND**

_KMcD Accounting Solutions_, provides an Online Accounting System for small to medium-sized businesses. While the accounting system has been well-received, clients are experiencing issues with it and many have requested additional features. A means of logging these issues and features is required that will allow us to focus on fixing the issues that are of highest priority to our clients, and deliver new features in a timely manner. Hence the decision was made to create an online [issue tracker](https://kmcd-issue-tracker.herokuapp.com/issue_tracker/apphome/) that will help us to respond quickly to our clients' needs, thereby improving client satisfaction.


# **2 DESIGN APPROACH**

## **2.1 LOOK & FEEL**

I used [figma.com](https://www.figma.com/file/g5LWnVMBRVwuMGNSxHS7qb/Home-Page?node-id=0%3A1) to design the look and feel of the website. These screen layouts laid the foundation for the site. The original design focused on the Issues, but I based the Features list and details on the same design, so I didn't create any new designs for these. 

As regards adding the comments, thumbs up, and add to cart, I didn't want to deviate too much from the original design, so I added these items in such a way that they blended in with the original designs.

I have added the screen shots of the original design in the 'Design' folder of the root directory, and they can be seen [here on github](https://github.com/KittyMcDonagh/kmcd-issue-tracking-project/tree/master/Design/figma-wireframes). 


## **2.2 Logic Flows**

I used Microsoft Publisher to create logic flows for the Issue Tracker and user setup, for Vendor-side and Client-side processing, and workflows for the Issues & Features - these can be seen [here on github](https://github.com/KittyMcDonagh/kmcd-issue-tracking-project/tree/master/Design/system-diagrams)


### **2.2.1 Issue Tracker High Level Overview**

![alt text](/Design/system-diagrams/issue_tracking_overall_view.png "Issue Tracker Overview")


### **2.2.2 User Setup**

![alt text](/Design/system-diagrams/user-setup.png "Issue Tracker User Setup")


### **2.2.3 Vendor side - System Logic Flow**

![alt text](/Design/system-diagrams/vendor-system-logic.png "Vendor System Logic")


### **2.2.4 Client side - System Logic Flow**

![alt text](/Design/system-diagrams/client-system-logic.png "Client System Logic")


### **2.2.5 Issue / Feature - Client-side Workflow**

![alt text](/Design/system-diagrams/issue-feature-c-workflow.png "Issue Tracker Client-side Workflow")


### **2.2.6 Issue / Feature - Vendor-side Workflow**

![alt text](/Design/system-diagrams/issue-feature-v-workflow.png "Issue Tracker Vendor-side Workflow")


# **3. UX**

## **3.1 WEBSITE REQUIREMENTS**

### **3.1.1 High Level Requirements**

These are the high level requirements for the [Issue Tracker app](https://kmcd-issue-tracker.herokuapp.com/issue_tracker/apphome/):

1. The online [Issue Tracker](https://kmcd-issue-tracker.herokuapp.com/issue_tracker/apphome/) is required to be a central point where clients can log the    issues that they are experiencing with the _KMcD Online Accounting System_, and where they can request new features
2. The app requires two perspectives, a Client perspective and a Vendor perspective
3. Clients must be able to restrict the Vendor and other clients from seeing the Issue/Feature they input until they are satisfied with the details, and       have set it to an appropriate status to allow the Vendor and other Clients to view it
4. Clients must be able to search for Issues/Features based on the details in the Summary field
5. Clients must be able to flag another clients' Issue, to indicate they have this also
6. Clients must be able to flag and pay for a Feature (their own or another client's) that they require
7. Clients must be able to add comments on their own and on other clients' Issues and Features
8. Clients must be able to see all the comments input against a particular Issue/Feature
9. Clients must be able to run an Issues report that shows a list of the Issues they have input and the Issues that they have flagged, in Priority order
10. Clients must be able to run a Features report that shows a list of the Features they have input and Features they have paid for, in Amount Paid order
11. Once an Issue / Feature is at a status where other clients can view it, the client should not be able to edit its details - they should only be able to     update the user to whom the Issue/Feature is assigned on the client side

12. Clients must be able to see a list of Issues
13. Clients must be able to filter the Issues list by an Issues Filter which allows the user to select:
    - Issues Assigned to the Logged in user only
    - Issues that belong to the client the user is associated with only
    - Issues that belong to other clients only
    - All Issues
14. Clients must be able to filter the Issues list by Status, and Priority  

15. Clients must be able to see a list of Features
16. Clients must be able to filter the Features list by a Features Filter which allows the user to select:
    - Features Assigned to the Logged in user only
    - Features that belong to the client the user is associated with only
    - Features that belong to other clients only
    - All Features
17. Clients must be able to filter the Features list by Status
18. Clients must be able to sort the Features list by Total Amount Paid for the Feature

19. Since the business contract is between the client and the Vendor, not between one client and another, there are certain things a client should not be      able to do - in the interests of data protection:
   - While clients should be able to see other clients' Issues and Features, but they should **not** be able to see another client's client code or name,    nor the user id of a user who is associated with another client (this includes user ids shown on Issues, Features, and on Comments)
   - Clients should **not** be able to edit / update another client's Issues / Features
   - A client should **not** have access to another client's Reports

20. A vendor-side user should **not** be able to input Issues/Features
21. A Vendor-side user **should** be able to input comments on Issues/Features
22. A vendor-side user should **not** be able to edit the details of an Issue/Feature

23. A vendor-side user should be able to update the following fields on an Issue:
    - The user to whom the Issue is assigned on the Vendor side
    - The Status of the Issue
    - The Priority of the Issue

24. A vendor-side user should be able to update the following fields on a Feature:
    - The user to whom the Feature is assigned on the Vendor side
    - The Status of the Feature
    - The Price of the Feature

25. Vendor-side users must be able to see a list of Issues
26. Vendor-side users must be able to filter the Issues list by an Issues Filter which allows the user to select:
    - Issues Assigned to the Logged in user only
    - All Issues
27. Vendor-side must be able to filter the Issues list by Status, Priority, and Client  

28. Vendor-side users must be able to see a list of Features
29. Vendor-side users must be able to filter the Features list by a Features Filter which allows the user to select:
    - Features Assigned to the Logged in user only
    - All Features
30. Vendor-side users must be able to filter the Features list by Status, and Client
31. Vendor-side users must be able to sort the Features list by Total Amount Paid for the Feature

32. Vendor-side users must be able to run an Issues report that:
    (a) Shows a rolled up total line for each Client, showing the number of Issues per Client, 
    (b) Orders the rolled up total lines by the number of Issues per client, from highest to lowest
    (c) Allows the user to click on a rolled up total line to show/hide the list of Issues underneath
    (d) Lists the Issues in Priority order, from most urgent to least urgent

33. Vendor-side users must be able to run an Features report that:
    (a) Shows a rolled up total line for each Client, showing the number of Issues per Client, 
    (b) Orders the rolled up total lines by the number of Issues per client, from highest to lowest
    (c) Allows the user to click on a rolled up total line to show/hide the list of Issues underneath
    (d) Lists the Issues in Priority order, from most urgent to least urgent




32. Since there is a contract between the Vendor and the Client:
    - Clients **should** be able to see the user id of Comments input by a user that is associated with the Vendor
    - The vendor should be able to see the client code and name
    - The vendor they should be able to see the user ids of Isssues, Features, and of Comments
    - The vendor should be able to see reports for all clients





15. It should be possible to filter issues by various options, status, priority, and for vendor-side users, by client
16. It should be possible to filter features by various options, status, sort them by amount paid, and for vendor-side users, filter by client
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


# **4. DJANGO DATABASES**

## 4.1	VENDOR DATABASE

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


## 4.2	CLIENT DATABASE

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


## 4.3	USER DETAILS DATABASE

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


## 4.4	ISSUES 

### 4.4.1	ISSUES DATABASE

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


### 4.4.2	ISSUE COMMENTS DATABASE

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


### 4.4.3	ISSUE 'THUMBS UP' DATABASE

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


## 4.5	FEATURES 

### 4.5.1	FEATURES DATABASE

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


### 4.5.2	FEATURE COMMENTS DATABASE

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



### 4.5.3	FEATURE PAID DATABASE

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




### **4.5.4	FEATURE ORDER**

#### 4.5.4.1. Ordering Client Details

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


#### 4.5.4.2. Order Line - One per Feature

The Features being paid for are added to the Order lines at Checkout.

|Field Name           |Description                                 | 
|---------------------|--------------------------------------------|
|order         	    |Foreign Key to above Ordering Client Details| 
|feature         	    |Foreign Key to the Feature being paid for   | 
|quantity      	    |The number of units being paid for          | 





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

      


|Features         |Website                                                                            |COMMENTS                                                                                                  |
|-----------------|-----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| Color Scheme    |[Color Wheel](https://www.canva.com/colors/color-wheel/)                           |I used this websiteto choose the base colors for my website.                                              |                                                                    
| Colors          |[w3schools](https://www.w3schools.com/colors/colors_picker.asp)                    |I used this website to get different shades of the base colors.                                          |
| Web page layouts|[bootstrap](https://getbootstrap.com/)                                             |I used bootstraps container, row and column classes to create my page layouts and to make them responsive |         
| Navigation bar  |[bootstrap](https://getbootstrap.com/)                                             |I used bootstraps nav bar classes to create my navigation bars, and burger menu.                     |         
| Wireframes      |[Figma](https://www.figma.com/file/g5LWnVMBRVwuMGNSxHS7qb/Home-Page?node-id=71%3A1)|I used figma when designing my website. See screen shots in Design folder on github                      |
|Django Pagination|https://django-el-pagination.readthedocs.io/en/latest/digg_pagination.html         |I used django pagination to create the paginate functionality on the Issues and Features Lists   


# **6. TESTING**

## **6.1 Manual Testing**

### **6.1.1. Account Testing**

#### 6.1.1.1 Registering


#### 6.1.1.2 Logging In


#### 6.1.1.3 Logging Out


#### 6.1.1.4 Forgotten Password


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

1. Follow this link to my [Project Repository on Github](https://github.com/KittyMcDonagh/Second-Milestone-Project)
2. On the repository page click "Clone or Download"
3. In the Clone with HTTPs section, copy the clone URL for the repository.
4. In your local IDE open Git Bash.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type git clone, and then paste the URL you copied in Step 3 - 
    "git clone https://kittymcdonagh.github.io/Second-Milestone-Project/"
7. Press enter and your local clone will be created.



# **8. CREDITS**

## **8.1 CONTENT**

### **8.2 IMAGES AND ICONS USED ON ISSUE TRACKER **

The following icons/images were used to create the overview diagram of the Issue Tracking System:

|IMAGE / ICON                           |COPIED FROM
|---------------------------------------|----------------------------------------------------------------------------------------------|
|Questions Comments Concerns icon       |http://clipart-library.com/clipart/ziXoGpb7T.htm                                              |
|Client group icon                      |http://clipart-library.com/clipart/1745500.htm                                                |
|Group sitting around globe of world    |http://clipart-library.com/img1/1474499.jpg                                                   |
|Online Server image                    |http://clipart-library.com/clipart/99610.htm                                                  |
|Online computer image                  |http://clipart-library.com/image_gallery2/Hosting-Free-Download-PNG.png                       |
|Blue user image                        |http://clipart-library.com/clipart/2038276.htm                                                |
|Orange user image                      |http://clipart-library.com/clipart/rcLnpabKi.htm                                              |
|Grey user image                        |http://clipart-library.com/clipart/773211.htm                                                 |



## **CODE SNIPPETS**

1. I have used code from the mini project to add a map to Rosie's resume, to load my map.
2. I used https://developers.google.com/maps/documentation/javascript/examples/place-details to add an infowindow for the location 
   name to the markers.
3. I have copied classes from my Milestone 1 project for the navigation bar, the links and hovering.
4. Comments have been added in the files where copied code is used.
5. With assistance from Slack I copied code from Stack Overflow to close the burger menu


## **8.3 ACKNOWLEDGEMENTS**

|NAME                          |COMMENTS
|------------------------------|----------------------------------------------------------------------------------------------|
|The Code Institute            |I learnt everything I needed to know to build this website from the Code Institute.           |
|Fellow students on Slack      |I received a lot of assistance and feedback from students on Slack which improved my project. |
|My mentor Seun Owonikoko      |I received assistance, feedback and encouragement from Seun.                                  |












