from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Notice
from .forms import NoticeForm
from .crawling import transportPrasing


# Create your views here.

##메인페이지
def home(request):
        return render(request, 'mainapp/home.html')

#공지 리스트
def notice_list(request):
    notices = Notice.objects               
    return render(request, 'mainapp/notice_list.html', {'notices' : notices})

#공지 상세페이지 (R)
def notice_detail(request, notice_id):
    notice = get_object_or_404(Notice, pk=notice_id)
    return render(request, 'mainapp/notice_detail.html',{'notice': notice})

#공지 등록 (C)
@login_required
def notice_register(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.save()
            return redirect('mainapp:notice_list')
    else : 
        form=NoticeForm()
        return render(request, 'mainapp/notice_register.html', {'form':form})


#공지 수정(U)
@login_required
def notice_update(request, notice_id):
    notice = get_object_or_404(Notice, pk=notice_id)
    if request.method=='POST':
        form = NoticeForm(request.POST, instance=notice)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.save()
            return redirect('mainapp:notice_detail', notice_id=notice.pk)    
    else:
        form = NoticeForm(instance=notice)
        return render(request, 'mainapp/notice_update.html', {'form':form})


#공지 삭제(D)
@login_required
def notice_delete(request, notice_id):
    notice = get_object_or_404(Notice, pk=notice_id)
    notice.delete()
    return redirect('mainapp:notice_list')

def weather(request):
    return render(request, 'mainapp/weather.html')

def transport(request):
    ys04 = "101900002" ##용산04

    ys_smlibrary = "102000137"  ##숙명여대 도서관앞
    ys_smlibrary_ord="21"
    ys_smforntdoor = "102000140"  ##숙명여대정문
    ys_smforntdoor_ord = "22"
    ys_smbackgate = "102000141"  ##숙명여대 후문
    ys_smbackgate_ord = "23"

    bus400 = "100100596" ##400번 버스
    d_smfrontdoor = "102000139"  ##숙명여대 정문
    d_smfrontdoor_ord = "41"  
    d_smlibrary = "102000138"  ##숙명여대도서관앞
    d_smlibrary_ord = "42"
    u_smlibrary = "102000137"  ##숙명여대도서관앞
    u_smlibrary_ord = "63"
    u_smfrontdoor = "102000140"  ##숙명여대정문
    u_smfrontdoor_ord = "64"
    u_smbackgate = "102000141"  ##숙명여대후문
    u_smbackgate_ord = "65"
    
    ys04_smlibrary = transportPrasing(ys04, ys_smlibrary, ys_smlibrary_ord)
    ys04_smfrontdoor = transportPrasing(ys04, ys_smforntdoor, ys_smforntdoor_ord)
    ys04_smbackgate = transportPrasing(ys04, ys_smbackgate, ys_smbackgate_ord)

    bus400_d_smfrontdoor = transportPrasing(bus400, d_smfrontdoor, d_smfrontdoor_ord)
    bus400_d_smlibrary = transportPrasing(bus400, d_smlibrary, d_smlibrary_ord)
    bus400_u_smlibrary = transportPrasing(bus400, u_smlibrary, u_smlibrary_ord)
    bus400_u_smfrontdoor = transportPrasing(bus400, u_smfrontdoor, u_smfrontdoor_ord)
    bus400_u_smbackgate = transportPrasing(bus400, u_smbackgate, u_smbackgate_ord)

    return render(request, 'mainapp/transport.html', {'ys04_smlibrary':ys04_smlibrary, 'ys04_smfrontdoor':ys04_smfrontdoor, 'ys04_smbackgate':ys04_smbackgate, 
    'bus400_d_smfrontdoor':bus400_d_smfrontdoor, 'bus400_d_smlibrary':bus400_d_smlibrary, 
    'bus400_u_smlibrary':bus400_u_smlibrary, 'bus400_u_smfrontdoor':bus400_u_smfrontdoor, 'bus400_u_smbackgate':bus400_u_smbackgate}
)