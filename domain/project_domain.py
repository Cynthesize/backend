import models.project_models
import feconf
import string
from random import *

class ProjectDomain(object):
    """Domain objects for Project"""

    def __init__(
        self, project_id, name, category, checkpoint,
        comments,collaborators, description, is_public,
        owner, tags, upvotes):

        self.id = project_id
        self.name = name
        self.category = category
        self.checkpoint = checkpoint
        self.comments = comments
        self.collaborators = collaborators
        self.description = description
        self.is_public = is_public
        self.owner = owner
        self.tags = tags
        self.upvotes = upvotes
    
    @classmethod
    def generate_id(size = 6, chars = string.ascii_uppercase + string.digits):
        generated_id = []
        for _ in range(6):
            generated_id.append(choice(chars))
        project_id = 'project.' + ''.join(generated_id)
        return project_id

    @classmethod
    def create_default_project(cls, project_id, owner):
        return cls(
            project_id, feconf.NEW_PROJECT_NAME,
            feconf.DEFAULT_PROJECT_CATEGORY, None, [],
            [], feconf.DEFAULT_PROJECT_DESCRIPTION, False,
            owner, [], 0)
        