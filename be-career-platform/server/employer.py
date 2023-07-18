from .extensions import mongo
from flask import Blueprint,request, flash, jsonify
from flask_login import login_required, current_user
from .model import User, JobPosting

employer = Blueprint('employer', __name__)

# def home(id):
# 	user_manager.user.set_session(session, g)

# 	if id != None:
# 		b = book_manager.getBook(id)

# 		print('----------------------------')
# 		print(b)

# 		user_books={}
# 		if user_manager.user.isLoggedIn():
# 			user_books = book_manager.getReserverdBooksByUser(user_id=user_manager.user.uid())['user_books'].split(',')
		
# 		if b and len(b) <1:
# 			return render_template('book_view.html', error="No book found!")

# 		return render_template("book_view.html", books=b, g=g, user_books=user_books)
# 	else:
# 		b = book_manager.list()

# 		user_books=[]
# 		if user_manager.user.isLoggedIn():
# 			reserved_books = book_manager.getReserverdBooksByUser(user_id=user_manager.user.uid())
			
# 			if reserved_books is not None:
# 				user_books = reserved_books['user_books'].split(',')
		
# 		print("---------------------------------------")
# 		print(user_books)

# 		if b and len(b) <1:
# 			return render_template('books.html', error="No books found!")
	
# 		return render_template("books.html", books=b, g=g, user_books=user_books)


# 	return render_template("books.html", books=b, g=g)



def notEmployerRole():
    find_user =  User.get_by_id(current_user.get_id())
    if find_user.role != "employer":
        return True
    return False 

@employer.route('/employer/index')
@login_required
def index():
    if notEmployerRole():
        return "You are not an employer."
    return "in employer index"

@employer.route('/employer/profile')
@login_required
def profile():
    if notEmployerRole():
        return "You are not an employer."
    return "in employer profile"


@employer.route('/employer/post/<employerId>', methods=['POST'])
# @login_required
def postJob(employerId):
    #todo authentication
    try:
        jobTitle = request.json["jobTitle"]
        jobDescription = request.json["jobDescription"]
        companyName = request.json["companyName"]
        job = JobPosting(employerId,jobTitle,jobDescription,companyName)
        job.save_to_mongo()
        flash(f'Job created for {jobTitle}!', 'success')
        return {"jobId": job.get_jobId()}, 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@employer.route('/employer/<employer_id>/<job_id>', methods=['GET'])
def getJobByJobId(employer_id,job_id):
    #todo authentication
    user = mongo.db.users.find_one({"_id": employer_id})
    if user == None:
        flash('Not logined', 'danger')
        return "failed authentication"


    job = JobPosting.get_jobBYJobId(job_id)
    return jsonify(str(job)), 200

@employer.route('/employer/<employer_id>/jobs', methods=['GET'])
def getJobsByEmployerId(employer_id):
    jobLists = JobPosting.get_jobListsBYEmployerId(employer_id)
    return jsonify(list(jobLists)) , 200


@employer.route('/employer/<employer_id>/<job_id>', methods=['PUT'])
def updateJob(employer_id,job_id):
    #todo authentication
    # user = mongo.db.users.find_one({"_id": employer_id})
    # if user == None:
    #     flash('Not logined', 'danger')
    #     return "failed authentication"
    try: 
        fields = ["jobTitle","jobDescription","companyName"]
        updateInfo = {}
        json_keys = list(request.json.keys()) if request.is_json else []
        
        for key in json_keys:
            if key not in fields:
                raise Exception(key)
            else:
                updateInfo[key] = request.json[key]
        result = JobPosting.put(job_id,updateInfo)
        return {"jobId": job_id}, 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@employer.route('/employer/<employer_id>/<job_id>', methods=['DELETE'])
def deleteJob(employer_id,job_id):
    #todo do authentication
    try:
        JobPosting.delete(job_id)
        #todo delete associated application tracking  

        return {"jobId": job_id}, 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
