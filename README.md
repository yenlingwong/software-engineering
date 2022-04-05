# SE-Sprint01-Team09

# README for Corona Archive

## Contributors-
### Sprint 1-
    1. Nimesh Acharya
    2. Sinem Bilge Güler

This project was created to build a web service for Corona Pandemic management, which enables citizen to register a place they enetered in specific time, place owners to register the place and get automatically generated QR code. Further, Hospitals that are verified from an agent can mark the citizen as infected or not. The agent or the owner of the application can see all the insights including how many people were in contact with someone who was already visited during certain time at certain place.To conclude this application is the effective measure to track the ongoing covid situation digitally.

## File Structure:
	\main 	(github's branch)
	
		\run.py
		
		\main
		
			\static
			
				\....	(CSS files and Images' folder)
			
			\templates
			
				\....	(HTML files)	
			
			\__init.py__	
			
			\database.db
			
			\forms.py	(includes the forms created within flask)
			
			\models.py	(includes the database created)
			
			\routes.py	(includes the routes to various pages)
		
		\test_main.py
		
		\environments\env	(created during installation of env)
		
			\...		(several files required for env)    
		
		\required.txt     
			

## Required Installation:

## Prerequisites:

	Python

## Install virtualenv

	$pip install virtualenv
   
   Open a terminal in the project dir and run following command to create separate env for the project. This make sure your project files are isolated to other installed libraries

	$virtualenv env

	#if u are using windows
	$ .\env\Scripts\activate
	#Or if u are using linux or macOS
	$ source env\bin\activate
	
	To deactivate
	$deactivate
	
# Install dependencies

	$pip install -r required
	$pip install unittest
	
And now start the server by running run.py file
	$(env) python3 run.py

The server will by default start on port 5000.

## Running Test

	$python -m unittest test_main.py

## Tasks Done:
	1. Created GUI of different pages by extending from the layout named "base.html" using pure HTML, and CSS
	2. Created Login, Register, After Successful Login pages for different users.
	3. Created routes on routes.py for different URL
	4. Created models on models.py for data storage in database
	5. Created forms using flask_wtf and wtforms
	6. Linked form with respective HTML pages
	7. Created Authentication with the help of flask_login library
	8. Created test cases for landing pages, and different pages including the login and register function on test_main.py
	9. Created the required redirects, flash message with respect to successful or unsuccessful login or register.
	
## Tasks to improve(Our Perception):
	1. It would be good if Hospital while registering don't provide password and agent manually(later can be made automatically) adds the password in database which will then only be considered as verified.
		In our case, till now the hospital can request agent to register after which agent must manually add the password for the hospital in database which then only allows hospital to login. So, we thought this would be good way to verify the hospital by agent. 	
		
### Sprint 2-
    1. Yen Ling Wong
    2. Sindi Tasellari
    
### Additional Technologies
 	1. Javascript

## Tasks Done:
	1. Removed unused libraries and imports
	2. Created additional account pages for Visitors and Places to view their account information
	3. Created forms in the Visitor and Places accounts for the respective users/account holders to update their account information.
		a. The database fields from the previous sprint's implemention has been kept the same; we have added an additional field 'image_file' in the visitor's 			  model. A default image is provided for each visitor upon registration, and visitors have the option to upload their own profile picture. Additional 
		   checks have been implemented to make sure that only jpg and png files are uploaded.
		b. The current data in the user's account is stored in the form fields, so that the user will not have to refill their information. Any changes made to 		   the form will update the data in the database.
		c. An additional function 'save_picture' in the routes.py file has been implemented to store the image with a random hexadecimal filename, while 		    retaining its original file extension. This is to avoid having collisions of images with the same name. This function also limits the image size to 		   125 x 125.
		d. To view this, go to static/Images 
		e. Additionally, sessions have been used to determine whether the current user is a visitor or a place, so that the page is redirected to the correct 			 routes.
		f. The uniqueness checks have been implemented for unique data such as email, device id and phone number where applicable.
	4. Created additional boolean field for visitors: is_infected. Upon registering, this field is set to false. The infection status of each visitor is displayed
	   in the visitors home page. 
	5. Created additional boolean field for hospitals: is_approved. 
	6. In the agent page, there are three tables that display all of the registered users of this application, including visitors, hospitals and places. The    	       infection status of visitors and approval status of places can be seen as well. The data has been queried in the routes and then passed into the template as 	       arguments.
	7. To improve upon the implementation of the previous sprint, links to the registration pages have been added to the login forms and links to the login pages 		 have been added to the registartion forms so that users can easily switch between the two.
	8. Created the button to generate the QRcode.
	9. Displayed the QRcode to the places page.
	10. The button has been edited and designed.
	11. In the places page, created the button and functionality to download the QRcode. Upon clicking 'Generate QR code', a QR code image is displayed and the 		button disappears. Instead, a button to download the QR code as a file appears. This is done so that places can print the QR code to be used in their 	   	       establishments.
	12. Connected a camera scanner functionality to the visitor page. The scanner is open upon entering the home page. To access this feature, please select 	     'allow' when the browser prompts, and place an image of the qr code in front of your web cam.
	13. The scanner reads the value contained in the QR code into the text box. 
	14. 'Remember Me' checkbox added to the user login form.
	15. Improved styling for all pages to make texts more readable
	16. Environment Variable added to gitignore.
	17. The installation guide had some errors, and this has been updated to ensure a smoother installation process.
		
		
		
		
### Agent Credentials-
    email: agent@jacobs-university.de
    password: agent12345
    
    Please use this to login to the admin portal.
	

## References:
	1. Python Flask Tutorial: Full-Featured Web App by Corey Schafer
	
## To be improved on:
	1. Complete the logic for the 'forget password' fields.
	2. Store the data from the QR code into the database.
	3. Complete the 'Remember me Functionality'

	

	
	
