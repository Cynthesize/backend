# Warehaus

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

