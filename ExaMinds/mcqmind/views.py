from django.shortcuts import render
from mcqmind.models import Student_Info
from mcqmind.models import Questions, Result, Admin_Info
from django.contrib.auth import logout

# Create your views here.

def MainPage(request):
    return render(request, "mainpage.html")

def HomePage(request):
    return render(request, "home.html")

def AdminPage(request):
    return render(request, 'Admin/adminpage.html')

def LoginAdminPage(request):
    return render(request, 'Admin/adminlogin.html')

def RegisterPage(request):
    return render(request, 'Students/addstudent.html')

def ViewUserPage(request):
    return render(request, 'Students/viewstudent.html')

def UpdateUserPage(request):
    return render(request, 'Students/updatestudent.html')

def DeleteUserPage(request):
    return render(request, 'Students/deletestudent.html')

def CrudUserPage(request):
    return render(request, 'Students/studentcrud.html')

def AddquestionPage(request):
    return render(request, 'Questions/addque.html')

def LoginUserPage(request):
    return render(request, 'Students/login.html')

def UpdateQuesPage(request):
    return render(request, 'Questions/updateque.html')

def CrudQuesPage(request):
    return render(request, 'Questions/quecrud.html')



def AddUser(request):
    uname = request.POST['username']
    psw = request.POST['password']
    mobno = request.POST['mobile_no']

    Student_Info.objects.create(
        username = uname,
        password = psw,
        mobile_no = mobno
    )


    request.session['username'] = uname
    request.session['answer'] = {}
    request.session['qid'] = 0

    return render(request, 'home.html', {'msg': 'User Registered Successfully!!'})

def LoginUser(request):
    uname = request.POST['username']
    psw = request.POST['password']
    

    try:
        userdb = Student_Info.objects.get(username = uname)
    
        if userdb.username == uname and userdb.password == psw:
            request.session['username'] = uname
            request.session['answer'] = {}
            request.session['score'] = 0
            request.session['qid'] = 0
            # return render(request, '')
            return Home(request)
        
        else:
            return render(request, 'Students/login.html', {"msg": 'Invalid username or password'})
        
    except Student_Info.DoesNotExist:
        return render(request, 'Students/login.html', {'msg': "User Does Not Exist / Register First"})


def Home(request):
    uname = request.session['username']
    return render(request, 'home.html', {'username': uname})


def ViewUser(request):
    uname = request.POST['username']

    userdb = Student_Info.objects.get(username=uname)

    return render(request, 'Students/viewstudent.html', {'userdata': userdb})


def UpdateUser(request):
    uname = request.POST['username']
    psw = request.POST['password']
    mobno = request.POST['mobile_no']

    userdb = Student_Info.objects.filter(username = uname)

    userdb.update(
        password = psw,
        mobile_no = mobno
    )

    return render(request, 'Students/updatestudent.html', {'msg': 'User Updated Successfully!!'})


def DeleteUser(request):
    uname = request.POST['username']

    Student_Info.objects.get(username=uname).delete()

    return render(request, 'Students/deletestudent.html', {'msg': "User Deleted Successfully!!"})


def CrudAddUser(request):
    uname = request.POST['username']
    psw = request.POST['password']
    mobno = request.POST['mobile_no']

    Student_Info.objects.create(
        username = uname,
        password = psw,
        mobile_no = mobno
    )

    return render(request, 'Students/studentcrud.html', {'msg': 'User Registered Successfully!!'})


def CrudViewUser(request):
    uname = request.POST['username']

    userdb = Student_Info.objects.get(username=uname)

    return render(request, 'Students/studentcrud.html', {'userdata': userdb})


def CrudUpdateUser(request):
    uname = request.POST['username']
    psw = request.POST['password']
    mobno = request.POST['mobile_no']

    userdb = Student_Info.objects.filter(username = uname)

    userdb.update(
        password = psw,
        mobile_no = mobno
    )

    return render(request, 'Students/studentcrud.html', {'msg': 'User Updated Successfully!!'})

def CrudDeleteUser(request):
    uname = request.POST['username']

    Student_Info.objects.get(username=uname).delete()

    return render(request, 'Students/studentcrud.html', {'msg': "User Deleted Successfully!!"})

def ShowallUSer(request):
    userdb = Student_Info.objects.all()

    return render(request, 'Students/showallstudents.html', {'userdb': userdb})


##############  Questions #############

def Addquestion(request):
    que = request.POST['questions']
    opt1 = request.POST['option1']
    opt2 = request.POST['option2']
    opt3 = request.POST['option3']
    opt4 = request.POST['option4']
    correct_ans = request.POST['answer']
    sub = request.POST['subject']


    Questions.objects.create(
        qtext = que,
        qoption1 = opt1,
        qoption2 = opt2,
        qoption3 = opt3,
        qoption4 = opt4,
        correct_answer = correct_ans,
        subject = sub
    )

    return render(request, 'Questions/addque.html', {'msg': 'Question Added Successfully!!'})

def ShowallQuestions(request):
    userdb = Questions.objects.all()

    return render(request, 'Questions/showallque.html', {'userdb': userdb})


def DeleteQue(request):
    que = request.POST['questions']

    Questions.objects.get(qtext=que).delete()

    return render(request, 'Questions/deleteque.html', {'msg': "User Deleted Successfully!!"})


def UpdateQues(request):
    que = request.POST['questions']
    opt1 = request.POST['option1']
    opt2 = request.POST['option2']
    opt3 = request.POST['option3']
    opt4 = request.POST['option4']
    correct_ans = request.POST['answer']
    sub = request.POST['subject']

    userdb = Questions.objects.filter(qtext = que)

    userdb.update(
    qtext = que,
    qoption1 = opt1,
    qoption2 = opt2,
    qoption3 = opt3,
    qoption4 = opt4,
    correct_answer = correct_ans,
    subject = sub,
    )

    return render(request, 'Questions/updateque.html', {'msg': 'Question Updated Successfully!!'})

def CrudAddque(request):
    que = request.POST['questions']
    opt1 = request.POST['option1']
    opt2 = request.POST['option2']
    opt3 = request.POST['option3']
    opt4 = request.POST['option4']
    correct_ans = request.POST['answer']
    sub = request.POST['subject']


    Questions.objects.create(
        qtext = que,
        qoption1 = opt1,
        qoption2 = opt2,
        qoption3 = opt3,
        qoption4 = opt4,
        correct_answer = correct_ans,
        subject = sub
    )

    return render(request, 'Questions/quecrud.html', {'msg': 'Question Added Successfully!!'})

def CrudUpdateQues(request):
    que = request.POST['questions']
    opt1 = request.POST['option1']
    opt2 = request.POST['option2']
    opt3 = request.POST['option3']
    opt4 = request.POST['option4']
    correct_ans = request.POST['answer']
    sub = request.POST['subject']

    userdb = Questions.objects.filter(qtext = que)

    userdb.update(
    qtext = que,
    qoption1 = opt1,
    qoption2 = opt2,
    qoption3 = opt3,
    qoption4 = opt4,
    correct_answer = correct_ans,
    subject = sub,
    )

    return render(request, 'Questions/quecrud.html', {'msg': 'Question Updated Successfully!!'})

def CrudDeleteQue(request):
    que = request.POST['questions']

    Questions.objects.get(qtext=que).delete()

    return render(request, 'Questions/quecrud.html', {'msg': "User Deleted Successfully!!"})

def CrudViewQue(request):
    que = request.POST['questions']

    userdb = Questions.objects.get(qtext=que)

    return render(request, 'Questions/quecrud.html', {'userque': userdb})


def LogoutUser(request):
    logout(request)
    return render(request, 'mainpage.html')

##*************** Test **************##

def StartTest(request):
    sub = request.GET['subject']
    
    request.session['subject'] = sub

    questions = Questions.objects.filter(subject = sub).values()

    allquestions = list(questions)

    request.session['allquestions'] = allquestions


    return render(request, 'starttest.html', {'question':allquestions[0]})


def NextQuestion(request):
    allquestions =  request.session['allquestions']

    queindex = request.session['qid']

    if 'user_ans' in request.GET:
        answer = request.session['answer']
        answer[request.GET['qid']] = [request.GET['qid'], request.GET['qtext'], request.GET['user_ans'], request.GET['answer']]

    
    try:
        if queindex < len(allquestions):
            request.session['qid'] = request.session['qid']+1
            queindex = request.session['qid']
            question = allquestions[queindex]

            return render(request, 'starttest.html', {'question': question})
        
    except:
        return render(request, 'starttest.html', {'msg': 'Test Completed'})
    

def PreviousQuestion(request):
    allquestions =  request.session['allquestions']

    queindex = request.session['qid']

    if 'user_ans' in request.GET:
        answer = request.session['answer']
        answer[request.GET['qid']] = [request.GET['qid'], request.GET['qtext'], request.GET['user_ans'], request.GET['answer']]

    
    try:
        if queindex > 0:
            request.session['qid'] = request.session['qid']-1
            queindex = request.session['qid']
            question = allquestions[queindex]

            return render(request, 'starttest.html', {'question': question})
        else:
            return render(request, 'starttest.html')
        
    except:
        return render(request, 'starttest.html')
 


def EndTest(request):

    if 'user_ans' in request.GET:
        answer = request.session['answer']
        answer[request.GET['qid']] = [request.POST['qid'], request.POST['qtext'], request.POST['user_ans'], request.POST['answer']]

    response = request.session['answer'].values()

    for res in response:
        if res[2] == res[3]:
            request.session['score'] += 1
        
    finalscore = request.session['score']

    uname = request.session['username']

    userdb = Student_Info.objects.get(username = uname)

    sub = request.session['subject']

    
    Result.objects.create(
        username = userdb,
        subject = sub,
        score = finalscore
    )

    return render(request, 'result/scorecard.html', {'response': response, 'finalscore': finalscore})

##*********************Admin *********************##

def LoginAdmin(request):
    aduname = request.POST['adminname']
    adpsw = request.POST['adminpassword']
    admail = request.POST['adminemail']


    try:
        userdb = Admin_Info.objects.get(adminname = aduname, adminemail=admail)
    
        if userdb.adminpassword == adpsw:
            request.session['adminname'] = aduname
            # return Home(request)
            return render(request, 'Admin/adminpage.html')
        
        else:
            return render(request, 'Admin/adminlogin.html', {"msg": 'Invalid Admin Name or password'})
        
    except Admin_Info.DoesNotExist:
        return render(request, 'mainpage.html', {'msg': "Admin Does Not Exist"}) 


def ShowallUserResult(request):
    userdb = Result.objects.all()

    return render(request, 'Result/showalluserresult.html', {'userdb': userdb})

def LogoutAdmin(request):
    logout(request)
    return render(request, 'mainpage.html')


def ShowUserResult(request):
   uname = request.session['username']

   userdb = Student_Info.objects.get(username = uname)

   results = Result.objects.filter(username = userdb)

   return render(request, 'Students/showuserresult.html', {'results': results})



def QuesOp(request):
    return render(request, 'Admin/questionsoperation.html')

def StudOp(request):
    return render(request, 'Admin/studentoperation.html')

def ResultOp(request):
    return render(request, 'Admin/resultop.html')