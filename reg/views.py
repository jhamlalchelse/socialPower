from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import *
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
@login_required(login_url='/account/login/')  
def home(request):
    user = User.objects.all()
    for i in user:
            if i == request.user:
                following = FollowingModel.objects.filter(fwinguserid=i.id)
    fwingid = [p.user.id for p in following]
    for usr in user:
        if usr == request.user:
            followinguser = FollowingModel.objects.filter(fwinguserid=usr.id)
            followeruser = FollowerModel.objects.filter(fweruserid=usr.id)
            fwinguser = [p.user.id for p in followinguser]
            fweruser = [p.user.id for p in followeruser]
    userid = list(set(fwinguser).union(set(fweruser)))
    C = []
    D = []
    for i in userid:
        followinguser = FollowingModel.objects.filter(fwinguserid=i)
        followeruser = FollowerModel.objects.filter(fweruserid=i)
        C = C + [p.user.id for p in followinguser]
        D = D + [p.user.id for p in followeruser]
    E = C + D + userid
    mutualuserid= sorted(list(dict.fromkeys(E)))
    data = {
        'users':user,
        'fwingid': fwingid,
        'mutualuserid':mutualuserid,
    }
    return render(request,'home.html')

@csrf_exempt
class CustomerRegistrationView(View):
    def get(self, request):
        form = UserRegistrationForms()
        return render(request, 'registration.html',{'forms':form})
    def post(self,request):
        form = UserRegistrationForms(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulation!! Registration Successfully')
            form.save()
        return redirect('login')

@csrf_exempt
@method_decorator(login_required(login_url='/account/login/'), name='dispatch')
class ProfileView(View):
    def get(self,request):
        user = User.objects.all()
        post = PostDetail.objects.filter(user=request.user)
        for i in user:
            if i == request.user:
                following = FollowingModel.objects.filter(fwinguserid=i.id)
                follower = FollowerModel.objects.filter(fweruserid=i.id)
        fwingid = [p.user.id for p in following]
        data = {
            'users':user,
            'posts':post,
            'followers':follower,
            'followings':following,
            'fwingid': fwingid,
        }
        return render(request, 'myprofile.html',data)

@login_required(login_url='/account/login/')  
def userprofile(request,pk):
    userprofile = User.objects.filter(id=pk)
    userid = pk
    for item in userprofile:
            # print(f' for user is {item}')
            username = item
            posts = PostDetail.objects.filter(user=item)
            for post in posts:
                print(post.desc)
                print(post.post_image)
    following = FollowingModel.objects.filter(fwinguserid=pk)
    follower = FollowerModel.objects.filter(fweruserid=pk)
    data={
        'username':username,
        'posts':posts,
        'followers':follower,
        'followings':following,
        "userid":userid
    } 
    return render(request, 'userprofile.html',data)

@login_required(login_url='/account/login/')  
def userpost(request,pk):
    post = PostDetail.objects.filter(user=pk)
    data = {
        'posts':post
    }
    return render(request, 'userpost.html',data)

@csrf_exempt
@login_required(login_url='/account/login/')  
def userpostdetail(request, pk):
    postd = PostDetail.objects.filter(id=pk)
    comnts = MessageModel.objects.filter(postid=pk)
    if request.method == 'POST':
        usr = request.user
        comment = request.POST.get('comnt')
        postid = pk
        MessageModel(user=usr, comment=comment, postid=postid).save()
    data = {
        'postd': postd,
        'comnts':comnts
    }
    return render(request, 'userpostdetail.html',data)

@login_required(login_url='/account/login/')  
def mypost(request):
    post = PostDetail.objects.filter(user=request.user)
    data = {
        'posts':post
    }
    return render(request, 'mypost.html',data)

@login_required(login_url='/account/login/')  
def mypostdetail(request, pk):
    postd = PostDetail.objects.filter(id=pk)
    comnts = MessageModel.objects.filter(postid=pk)
    data = {
        'postd': postd,
        'comnts':comnts
    }
    return render(request, 'mypostdetail.html',data)

@login_required(login_url='/account/login/')  
def follow(request,pk,userfwid=None):
    if request.method == 'GET':
        usr = User.objects.filter(id=pk)
        if userfwid is not None: 
            userid = userfwid
            fwuser = User.objects.filter(id=userid)
            for fw in fwuser:
                for user in usr:
                    FollowingModel(user = user, fwinguserid = userid ).save()
                FollowerModel(user = fw, fweruserid = pk ).save()
            return redirect('follower',userfwid)
        if userfwid is None:
            userid = request.user.id
            for user in usr:
                FollowingModel(user = user, fwinguserid = userid ).save()
            FollowerModel(user = request.user, fweruserid = pk ).save()
            return redirect('myprofile')
            
@login_required(login_url='/account/login/')  
def unfollow(request, pk, userfwid=None):
    if request.method == 'GET':
        if userfwid is None:
            FollowingModel.objects.filter(Q(user=pk) & Q(fwinguserid= request.user.id)).delete()
            FollowerModel.objects.filter(Q(user= request.user) & Q(fweruserid=pk)).delete()
            return redirect('myprofile')
        if userfwid is not None: 
            fwuser = User.objects.filter(id=userfwid)
            for fw in fwuser:
                FollowerModel.objects.filter(Q(user= fw) & Q(fweruserid=pk)).delete()
                FollowingModel.objects.filter(Q(user=pk) & Q(fwinguserid= userfwid)).delete()
            return redirect('following',userfwid)
            
@login_required(login_url='/account/login/')  
def follower(request, pk=None):
    if pk is None:
        follower = FollowerModel.objects.filter(fweruserid=request.user.id)
        following = FollowingModel.objects.filter(fwinguserid=request.user.id)
    if pk is not None:
        follower = FollowerModel.objects.filter(fweruserid=pk)
        following = FollowingModel.objects.filter(fwinguserid=pk)
    fw = [p.user.id for p in following]
    data = {
        'followers':follower,
        'userid':fw,
        'userfwid':pk,
    }
    return render(request,'follower.html',data)

@login_required(login_url='/account/login/')  
def following(request, pk):
    following = FollowingModel.objects.filter(fwinguserid=pk)
    data = {
        'followings':following,
        'userfwid':pk,
    }
    return render(request,'following.html',data)

@login_required(login_url='/account/login/')  
def deletefolloweruser(request, pk, userfwid=None):
    if userfwid is not None: 
            user = User.objects.filter(id=pk)
            fwuser = User.objects.filter(id=userfwid)
            for fw in user:
                FollowerModel.objects.filter(Q(user=fw) & Q(fweruserid=userfwid)).delete()
                for fuser in fwuser:
                    FollowingModel.objects.filter(Q(user=fuser) & Q(fwinguserid= pk)).delete()
            return redirect('follower',userfwid)

@csrf_exempt
@login_required(login_url='/account/login/')  
def searchuser(request):
    following = FollowingModel.objects.filter(fwinguserid=request.user.id)
    userid = [p.user.id for p in following]
    B = userid
    if request.method == 'POST':
        searchval = request.POST['search']
        usr = User.objects.filter(username__icontains=searchval)
        emailval = User.objects.filter(email__icontains=searchval)
        if usr:
            user = usr
            A = [p.id for p in user]
            C = [value for value in A if value in B]
            D = [value for value in A if not value in B ]
            E = (C+D)
            us = [us for us in user]
            i=0
            searchlist = []
            for j in us:
                if E[i] == j.id:
                    searchlist = searchlist + [j]
                    i = i+1
                else:
                    us.append(j)
        elif emailval:
            user = emailval
            A = [p.id for p in user]
            C = [value for value in A if value in B]
            D = [value for value in A if not value in B ]
            E = (C+D)
            us = [us for us in user]
            i=0
            searchlist = []
            for j in us:
                if E[i] == j.id:
                    searchlist = searchlist + [j]
                    i = i+1
                else:
                    us.append(j)
        else:
            return render(request,'searchuser.html')
        data={
            # 'users':user,
            'userid':userid,
            'searchlists':searchlist,
        }
        return render(request,'searchuser.html',data)
    return render(request,'searchuser.html')

@login_required(login_url='/account/login/')  
def searchfollow(request,userfwid,pk):
    if request.method == 'GET':
        usr = User.objects.filter(id=pk)
        if userfwid is not None: 
            userid = userfwid
            fwuser = User.objects.filter(id=userid)
            for fw in fwuser:
                for user in usr:
                    FollowingModel(user = user, fwinguserid = userid ).save()
                FollowerModel(user = fw, fweruserid = pk ).save()
        return redirect('userprofile',pk)

@login_required(login_url='/account/login/')  
def userfollower(request, pk):
    follower = FollowerModel.objects.filter(fweruserid=pk)
    following = FollowingModel.objects.filter(fwinguserid=request.user.id)
    fw = [p.user.id for p in following]
    data = {
        'followers':follower,
        'userid':fw,
        'userfwid':pk,
    }
    return render(request,'userfollower.html',data)

@login_required(login_url='/account/login/')  
def userfollowing(request, pk):
    following = FollowingModel.objects.filter(fwinguserid=pk)
    loginuserfolloeing = FollowingModel.objects.filter(fwinguserid=request.user.id)
    loginuserfolloeingid = [p.user.id for p in loginuserfolloeing]
    data = {
        'followings':following,
        'userfwid':pk,
        'loginuserfolloeingids':loginuserfolloeingid,
    }
    return render(request,'userfollowing.html',data)

@login_required(login_url='/account/login/')  
def userfollow(request,pk,userfwid):
        if request.method == 'GET':
            usr = User.objects.filter(id=pk)
            userid = request.user.id
            FollowerModel(user = request.user, fweruserid = pk ).save()
            for user in usr:
                FollowingModel(user = user, fwinguserid = userid ).save()
            return redirect('userfollowing',userfwid)

@login_required(login_url='/account/login/')      
def userunfollow(request, pk, userfwid):
    if request.method == 'GET':
        usr = User.objects.filter(id=pk)
        FollowerModel.objects.filter(Q(user= request.user) & Q(fweruserid=pk)).delete()
        for user in usr:
            FollowingModel.objects.filter(Q(user=user) & Q(fwinguserid= request.user.id)).delete()
        return redirect('userfollowing',userfwid)

@login_required(login_url='/account/login/')  
def userfollowinfollower(request,pk,userfwid):
        if request.method == 'GET':
            usr = User.objects.filter(id=pk)
            userid = request.user.id
            FollowerModel(user = request.user, fweruserid = pk ).save()
            for user in usr:
                FollowingModel(user = user, fwinguserid = userid ).save()
            return redirect('userfollower',userfwid)

@login_required(login_url='/account/login/')            
def userunfollowinfollower(request, pk, userfwid):
    if request.method == 'GET':
        usr = User.objects.filter(id=pk)
        FollowerModel.objects.filter(Q(user= request.user) & Q(fweruserid=pk)).delete()
        for user in usr:
            FollowingModel.objects.filter(Q(user=user) & Q(fwinguserid= request.user.id)).delete()
        return redirect('userfollower',userfwid)

@csrf_exempt
@login_required(login_url='/account/login/')  
def addpost(request):
    if request.method == 'POST':
        form = UploadPostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('addpost')
    else:
        form = UploadPostForm()
    return render(request, 'addpost.html', {'form': form})
    