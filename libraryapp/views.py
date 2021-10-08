from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import BookForm


# Create your views here.

#책 리스트
def book_list(request):
    books = Book.objects               
    return render(request, 'libraryapp/book_list.html', {'books' : books})

#책 상세페이지 (R)
def book_detail(request, book_id):    
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'libraryapp/book_detail.html',{'book': book})


#책 등록 (C)
@login_required
def book_register(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('libraryapp:book_list')
    else : 
        form=BookForm()
        return render(request, 'libraryapp/book_register.html', {'form':form})


#책 수정(U)
@login_required
def book_update(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method=='POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('libraryapp:book_detail', book_id=book.pk)    
    else:
        form = BookForm(instance=book)
        return render(request, 'libraryapp/book_update.html', {'form':form})

#책 삭제(D)
@login_required
def book_delete(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect('libraryapp:book_list')

#책 필터링
def book_result(request):
    book_object = Book.objects
    query = request.GET.get('query','')
    
    if query:
        book_object = book_object.filter(title__contains=query)
        return render(request,'libraryapp/book_result.html',{'result':book_object} )
    else :
        return redirect('libraryapp:book_list')