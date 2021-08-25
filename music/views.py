from music.models import Answer, Mbti, Question, Result
import music
from django.shortcuts import get_object_or_404, redirect, render
from random import randint

# Create your views here.


def main(request):
    return render(request, 'music/main.html')


def more(request):
    return render(request, 'music/more.html')


def start(request):
    question = get_object_or_404(Question, q_number=1)
    answers = question.answer_set.all()
    this_mbti = Mbti(order=2, e_i=0, s_n=0, t_f=0, p_j=0)
    this_mbti.save()
    ctx = {
        'question': question,
        'answers': answers,
        'this_user': this_mbti.pk
    }
    return render(request, 'music/question.html', context=ctx)


def question(request, this_user):
    choice = request.POST['choice']

    if this_user == 0:
        this_mbti = Mbti(order=1, e_i=0, s_n=0, t_f=0, p_j=0)
    else:
        this_mbti = get_object_or_404(Mbti, pk=this_user)
    # try:
    #     this_mbti = get_object_or_404(Mbti, pk=this_user)
    #     print('try 실행')
    # except:
    #     this_mbti = Mbti(order=1, e_i=0, s_n=0, t_f=0, p_j=0)

    question = get_object_or_404(Question, q_number=this_mbti.order)
    answers = question.answer_set.all()
    this_mbti.order += 1

    if choice == 'e':
        this_mbti.e_i += 1
    elif choice == 'i':
        this_mbti.e_i -= 1
    elif choice == 's':
        this_mbti.s_n += 1
    elif choice == 'n':
        this_mbti.s_n -= 1
    elif choice == 't':
        this_mbti.t_f += 1
    elif choice == 'f':
        this_mbti.t_f -= 1
    elif choice == 'p':
        this_mbti.p_j += 1
    elif choice == 'j':
        this_mbti.p_j -= 1
    else:
        print('mbti select error!')

    this_mbti.save()
    print(question)

    ctx = {
        'question': question,
        'answers': answers,
        'this_user': this_mbti.pk
    }

    if this_mbti.order == 13:
        return redirect('music:end', this_mbti.pk)
    else:
        return render(request, 'music/question.html', context=ctx)

    # if this_mbti.order == 13:
    #     return render(request, 'music/endstory.html', {'this_user': this_mbti.pk})
    # else:
    #     return render(request, 'music/question.html', context=ctx)


def end_story(request, this_user):
    return render(request, 'music/endstory.html', {'this_user': this_user})


def calc_result(request, this_user):
    this_mbti = get_object_or_404(Mbti, pk=this_user)

    result = ""
    if this_mbti.e_i > 0:
        result += "e"
    elif this_mbti.e_i == 0:
        x = randint(0, 1)
        if x == 1:
            result += "e"
        else:
            result += "i"
    else:
        result += "i"

    if this_mbti.s_n > 0:
        result += "s"
    elif this_mbti.s_n == 0:
        x = randint(0, 1)
        if x == 1:
            result += "s"
        else:
            result += "n"
    else:
        result += "n"

    if this_mbti.t_f > 0:
        result += "t"
    elif this_mbti.t_f == 0:
        x = randint(0, 1)
        if x == 1:
            result += "t"
        else:
            result += "f"
    else:
        result += "f"

    if this_mbti.p_j > 0:
        result += "p"
    elif this_mbti.p_j == 0:
        x = randint(0, 1)
        if x == 1:
            result += "p"
        else:
            result += "j"
    else:
        result += "j"

    print(result)
    rslt_content = get_object_or_404(Result, mbti=result)

    return render(request, 'music/result.html', {'result': rslt_content})
