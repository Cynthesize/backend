import models.project_models
import feconf

import string
import random

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
    def generate_id(size=6, chars=string.ascii_uppercase + string.digits):
        return 'project'.join(random.choice(chars) for _ in range(size))

    @classmethod
    def create_default_project(cls, project_id, owner):
        return cls(
            project_id, feconf.NEW_PROJECT_NAME,
            feconf.DEFAULT_PROJECT_CATEGORY, None, [],
            [], feconf.DEFAULT_PROJECT_DESCRIPTION, False,
            owner, [], 0)
        