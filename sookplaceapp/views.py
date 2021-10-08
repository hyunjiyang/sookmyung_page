from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Sookplace
from .forms import SookplaceForm
from django.contrib.auth.models import User



# Create your views here.
#게시물 리스트
def sookplace_list(request):
    sookplaces = Sookplace.objects               
    return render(request, 'sookplaceapp/sookplace_list.html', {'sookplaces' : sookplaces})


#게시물 상세페이지 (R)
def sookplace_detail(request, sookplace_id):
    sookplace = get_object_or_404(Sookplace, pk=sookplace_id)
    return render(request, 'sookplaceapp/sookplace_detail.html', {'sookplace':sookplace})

#게시물 등록 (C)
@login_required
def sookplace_register(request):
    if request.method == 'POST':
        form = SookplaceForm(request.POST, request.FILES)
        if form.is_valid():
            sookplace = form.save(commit=False)
            sookplace.user = request.user  ##username 자동 설정
            sookplace.save()
            return redirect('sookplaceapp:sookplace_list')
    else : 
        form=SookplaceForm()
        return render(request, 'sookplaceapp/sookplace_register.html', {'form':form})

#게시물 수정(U)
@login_required
def sookplace_update(request, sookplace_id):
    sookplace = get_object_or_404(Sookplace, pk=sookplace_id)
    if request.method=='POST':
        form = SookplaceForm(request.POST, instance=sookplace)
        if form.is_valid():
            sookplace = form.save(commit=False)
            sookplace.user = request.user  ##username 자동 설정
            sookplace.save()
            return redirect('sookplaceapp:sookplace_detail', sookplace_id=sookplace.pk)    
    else:
        if sookplace.user == User.objects.get(username=request.user.get_username()) :  ##자신의 글일때만 수정 가능
            form = SookplaceForm(instance=sookplace)
            return render(request, 'sookplaceapp/sookplace_update.html', {'form':form})

        else :
            return redirect('sookplaceapp:sookplace_detail', sookplace_id=sookplace.pk)    ##자신의 글 아니면 해당글 detail로 redirect


#게시물 삭제(D)
@login_required
def sookplace_delete(request, sookplace_id):
    sookplace = get_object_or_404(Sookplace, pk=sookplace_id)
    if sookplace.user == User.objects.get(username=request.user.get_username()) : ##자신의 글일때만 삭제 가능
        sookplace.delete()
        return redirect('sookplaceapp:sookplace_list')
    else:
        return redirect('sookplaceapp:sookplace_detail', sookplace_id=sookplace.pk)   ##자신의 글 아니면 해당글 detail로 redirect
