# MicroDonations Project-2-18
This is a project created in the 2020 Fall semester for UVA's CS 3240 Advanced Software Developement Techniques as assigned by Professor Mark Sherriff and Professor Will McBurnery. The theme selected for this project was Inclusion and Diversity in Software Development. The subtopic chosen within that theme is a MicroDonations app. Holistically the app supports the ability to post, view, and complete donations and tasks added by different users and the tasks donations they may choose to represent. 

You can find the site hosted on Heroku at https://micro-donations-cs3240.herokuapp.com/

# Team 2-18 Infomation: 
All work represented in this repo was created by the following team members on the project

Rohith Jampani (rvj8uc),
Wan Li (wl9wgc),
Liana Poon (lwp2fy),
Noal Zyglowicz (ntz3sw)

# Instructions on How to Use App:
## NavBar
The navbar at the top of the screen will help you navigate from page to page through the donations app. There is a dropdown on profile information that helps you o discover more information regarding profiles

## User Authentification
Much of the functionality of the project is only available to users once they are logged in. To log in click the login tab on the navbar and then click log in with google on the page you are directed to. This will take you to a page where you will need to log in with google to add and access your user account.

## Donation Page
### Overview of Donation Card
The donation holds the entire list of organizations that are available to donate to. These can be both larger charities or smaller coordinated efforts to raise money for a local supported cause. You can view the goal and progress bar to see the status of each donation goal (Note that you can donate even when the donation bar is full or the goal will be surpassed by your donation. The charities will always appreciate your overwhelming support :) ). 
### Donating
To donate click the donate button and you will be redirected to a page where you can input the desired amount you want to the organization. When you have the desired amount you wanted, click the PayPal pay now button to log into your account. Once logged in feel free to verify the amount that will be donated then when you are ready scroll down to the pay now button to confirm your donation.

*Important note about donating*
The steps above are implemented using PayPal's sandbox API. For the purpose of this project we are not running a legitimate business or charity and do not want and do not expect users or others testing the software to spend their own real money. Because setting up a sandbox account is inconvinient for the user we have set up an account with information that you can use to test and use the donating functionality

Open User PayPal Sandbox account Information:
sandbox email: personalteam218@gmail.com
sandbox password: Ilovecs!

### Read More
Clicking the Read More button will direct you to a page with more information about the organization in interest so that you can make a more informed decision before donating.

### Add to Favorites
Clicking the Add to Favorites button will add the organization to your favorites page which you can view and manage under the profile information tab.

### Adding Organizations
To add an organization you need to be logged in and then click on the Add Organization tab at the top of the page. This will direct you to a form on another page where you will need to provide valid information be clicking submit to add the organization.

## Task Page
The Task Page is very similar to Donations page in structure and is where users can post tasks they would like help with and view other user's tasks. It is helpful to list a general location of where the task would occur, about how long it might take, and suggest what is the best way for the user is to help aid in that task.

### Read More
The Read More is where the key information about the task can be viewed

### Done Task
The done task button is how a user can let the poster know the task has been complete. When the task is completed the poster will receive an email notification from who the task has been completed by.

## Profile Page
The profile page is where you view specifc information about both the app and personal information

### Profile
Clicking the profile tab takes you to a page allowing you to view your profile information. It also contains a link to a form to allow you to customize your information

### Favorited Organizations
Favorited organizations gives you access to view the organizations you have favorited so you have quicker access to them. Youcan remove any organizations that you are no longer interested in

### Spotlight
Spotlight shows a highlighted organization that has been selected for the admins for viewing for a particular outstanding reason or purpose.

### Leaderboard
Leaderboard shows the current top organizations, donaters, and task completers

# Project Licensing Information:
MIT License
© 2020

*Disclaimer*
If you are a student who has found this repo, using code from this repo in another UVA CS class makes you liable for a potential Honor Offense 

# Framework, Libraries, and APIs
## Django Framework
3-clause BSD
## jQuery
MIT License
## Bootstrap
MIT License and copyright 2018 Twitter
## Google Login 
Apache 2.0 License
## PayPal API
PayPal Developer Agreement

Code sourced from other sources such as incorporating css desgins is cited where due in the source where it is used
