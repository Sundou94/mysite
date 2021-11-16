from django.shortcuts import render, redirect
from django.http import HttpResponse #http 요청을 받으면 반응하는 도구
from .models import Board, Comment
from django.utils import timezone
from .forms import BoardForm
from django.core.paginator import Paginator

# Create your views here.
def index(request):
     #입력 인자
    page = request.GET.get('page', 1)
    #조회
    #return HttpResponse("bbsnote에 오신것을 환영합니다. ");
    board_list = Board.objects.order_by('-create_date')
    context = {'board_list' :  board_list} #딕셔너리로 선언
    #페이징 처리
    paginator = Paginator(board_list, 5) 
    page_obj = paginator.get_page(page)
    context = {'board_list' : page_obj}
    return render(request, 'bbsnote/board_list.html', context) #board_list.html 요청이 들어오면 context를 바인딩 해줘라
    #쿼리문은 사용하지 않았지만 스프링에서 select를 사용한것과 비슷함 

def detail(request, board_id):
    board = Board.objects.get(id=board_id)
    context = {'board' : board}
    return render(request, 'bbsnote/board_detail.html', context)

def comment_create(request, board_id):
    board = Board.objects.get(id=board_id)
    # comment = Comment(board=board, content=request.POST.get('content'), create_date=timezone.now())
    # comment.save()
    board.comment_set.creat(content=request.POST.get('content'), create_date=timezone.now()) #comment.set을 사용해서 위에와 동일하게 할수도 있다
    return redirect('bbsnote:detail', board_id=board.id)
    
def board_create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.create_date = timezone.now()
            board.save()
            return redirect('bbsnote:index')
    else: #get방식으로 호출이 되면 
        form = BoardForm() #BoardForm방식으로 호출을 해라 
    return render(request, 'bbsnote/board_form.html', {'form':form}) #그리고 여기 주소로 보내고 form 데이터를 form으로 넘긴다 
