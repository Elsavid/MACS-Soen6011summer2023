from .extensions import mongo
from flask_login import UserMixin
from .extensions import bcrypt
from flask import session
from datetime import datetime
import uuid

class User(UserMixin):

    def __init__(self, email, password, role, _id=None):
        self.email = email
        self.password = password
        self.role = role
        self._id = uuid.uuid4().hex if _id is None else _id

    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return self._id

    @classmethod
    def get_by_email(cls, email):
        data = mongo.db.users.find_one({"email": email})
        if data is not None:
            return cls(**data)

    @classmethod
    def get_by_id(cls, _id):
        data = mongo.db.users.find_one({"_id": _id})
        if data is not None:
            return cls(**data)
        return None

    @staticmethod
    def login_valid(email, password):
        verify_user = User.get_by_email(email)
        if verify_user is not None:
            return bcrypt.check_password_hash(verify_user.password, password)
        return False

    @classmethod
    def register(cls, email, password, role):
        user = cls.get_by_email(email)
        if user is None:
            new_user = cls(email, password, role)
            new_user.save_to_mongo()
            session['email'] = email
            return True
        else:
            return False

    def json(self):
        return {
            "email": self.email,
            "_id": self._id,
            "password": self.password,
            "role": self.role
        }

    def save_to_mongo(self):
        mongo.db.users.insert_one(self.json())

class JobPosting():
    def __init__(self, employerId, jobTitle, jobDescription, companyName, _id=None):
        self.employerId = employerId
        self.jobTitle = jobTitle
        self.jobDescription = jobDescription
        self.companyName = companyName
        self._id = uuid.uuid4().hex if _id is None else _id

    # def is_authenticated(self):
    #     return True
    # def is_active(self):
    #     return True
    # def is_anonymous(self):
    #     return False
    def get_jobId(self):
        return self._id

    @classmethod
    def get_jobBYJobId(cls,jobId):
        job = mongo.db.jobs.find_one({"_id":jobId})
        return job

    @classmethod
    def get_jobListsBYEmployerId(cls,employerId):
        job = mongo.db.jobs.find({"employerId":employerId})
        return job 
        
    def playloadToInsert(self):
        return {
            "employerId": self.employerId,
            "_id": self._id,
            "jobTitle": self.jobTitle,
            "jobDescription": self.jobDescription,
            "companyName":self.companyName,
            "creation_date": datetime.now()
        }

    def save_to_mongo(self):
        mongo.db.jobs.insert_one(self.playloadToInsert())

