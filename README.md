# Warehaus

Who is Warehaus? 
At Warehaus: 
- We incubate projects.
= We help students convert their ideas and projects into a fully fledged product by giving them continuous follow-up and feedback.
- We will account a review based system in which our professional mentors will be able to provide feedback with comments.
- We aim at building a community where anyone can post their ideas. This community will feed in the requirements for the project to product portal.

## Technologies in play: 
- 1. **Frontend tech**: Angular 6. 
- 2. **Backend tech**: Flask. 
- 3. **Databases to use**: TBD. MongoDB is first in line to be selected. 


### Project Flow
- Stage 1: Pre-launch. The idea page has to be online before the startup officially launches. 
- Stage 2: Post-launch. As much functionality has to be integrated as possible. 
- Stage 3: TBD. 

### Project Design 
We’ll be having four main folders or layers: 	
	1. Models 	2. Object 	3. Services 	4. Controllers

**Model**: There will be one file for user related models in the user_models.py file. This file will have different classes which will contain different info. Eg: UserInfoModel and UserProjectModel are the classes which will be in the user_model.py

**Object**: Objects for the classes of the model will be defined in this layer. This will be defined under user_domain.py. This file will contain classes like UserInfoDomainObject and UserProjectDomainObject.

**Services**: This is the layer in which all the functions will be written. This layer will include all the logic and will be interacting with the database. The file name will be of type user_services.py.

**Controller**: This layer will use functions defined in service layer. Here all the API requests will be made. All the routes will be served here.

