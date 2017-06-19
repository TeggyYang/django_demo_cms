# --*-- coding:utf-8 --*--
from django.shortcuts import render
from pic_app.models import Course, Photo
from django.http.response import JsonResponse
# from pic_cms.fields import ThumbnailImageFieldFile,ThumbnailImageField


def index_view(request):
    return render(request, 'pic_app/index.html',)


def items_detail_view(request):
    pictures = Photo.objects.all()
    return render(request, 'pic_app/items_detail.html', {'pictures': pictures})


def pic_detail_view(request):
    pic_id = request.GET.get('pid')
    pic_detail = Photo.objects.get(pid=pic_id[:-1])
    return render(request, 'pic_app/photos_detail.html', {'pic_detail': pic_detail})


def pic_detail_view_update(request):
    pic_id = request.GET.get('pid')
    pic_update = Photo.objects.get(pid=pic_id[:-1])
    return render(request, 'pic_app/photos_view.html', {'pic_update': pic_update})


def pic_detail_update(request):
    course = Course.objects.all()
    pic_temp = request.GET.get('pid')
    # pic_update = Photo.objects.get(pid=pic_temp[:-1])
    pic_id =pic_temp[:-1]
    if request.method == "POST":
        pic_course = Course.objects.get(cid=request.POST['pic_course'])
        # Photo.objects.filter(pid=pic_id[:-1]).update(same_qid="eeeeeeeeeeeeeee")
        Photo.objects.filter(pid=pic_id).update(is_checked=request.POST['pic_ischecked'] == u'1')
        Photo.objects.filter(pid=pic_id).update(is_valid=request.POST['pic_isvalid'] == u'1')
        Photo.objects.filter(pid=pic_id).update(course=pic_course)
        Photo.objects.filter(pid=pic_id).update(ocr_text=request.POST['pic_ocr'])
        Photo.objects.filter(pid=pic_id).update(correct_text=request.POST['pic_correct'])
        Photo.objects.filter(pid=pic_id).update(get_result=request.POST['pic_result'] == u'1')
        Photo.objects.filter(pid=pic_id).update(same_qid=request.POST['pic_sameid'])
        Photo.objects.filter(pid=pic_id).update(err_source=request.POST['pic_err'])
        # print pic_id
        # print "DONE"
    pic_update = Photo.objects.get(pid=pic_temp[:-1])
    return render(request, 'pic_app/photos_update.html', {'pic_update': pic_update, 'course': course})


def pic_detail_delete(request):
    pic_id = request.GET.get("pic_id")
    Photo.objects.get(pid=pic_id).delete()
    return JsonResponse({"status": 200, "msg": 'OK'})


def pic_detail_add(request):
    course = Course.objects.all()
    pictures = Photo.objects.all()
    if request.method == "POST":
        f = request.FILES.get('pic')
        path = 'media/photos/' + request.FILES.get('pic').name
        des_origin_f = open(path, "ab")
        for chunk in f.chunks():
            des_origin_f.write(chunk)
        des_origin_f.close()
        pic_course = Course.objects.get(cid=request.POST['pic_course'])
        new_data = Photo(
            pid=request.POST['pic_pid'],
            image='photos/' + request.FILES.get('pic').name,
            is_checked=request.POST['pic_ischecked'] == u'1',
            is_valid=request.POST['pic_isvalid'] == u'1',
            course=pic_course,
            ocr_text=request.POST['pic_ocr'],
            correct_text=request.POST['pic_correct'],
            get_result=request.POST['pic_result'] == u'1',
            same_qid=request.POST['pic_sameid'],
            err_source=request.POST['pic_err'],
        )
        new_data.save()
    return render(request, 'pic_app/photos_add.html', {'course': course, 'pictures': pictures})


def items_checked_view(request):
    pictures = Photo.objects.filter(is_checked=1)
    return render(request, 'pic_app/items_detail.html', {'pictures': pictures})


def items_unchecked_view(request):
    pictures = Photo.objects.filter(is_checked=0)
    return render(request, 'pic_app/items_detail.html', {'pictures': pictures})


def items_valid_view(request):
    pictures = Photo.objects.filter(is_valid=1)
    return render(request, 'pic_app/items_detail.html', {'pictures': pictures})


def items_unvalid_view(request):
    pictures = Photo.objects.filter(is_valid=0)
    return render(request, 'pic_app/items_detail.html', {'pictures': pictures})


def items_filter(request):
    print request.GET.get("check")
    print request.GET.get("valid")
    Q1 = ()
    Q2 = ()
    pictures = []
    check_id = request.GET.get("check")
    valid_id = request.GET.get("valid")
    if check_id == u'0' and valid_id == u'3':
        pictures = Photo.objects.all()
    elif check_id != u'0' and valid_id == u'3':
        if check_id == u'1':
            Q1 += ('is_checked', 1)
        elif check_id == u'2':
            Q1 += ('is_checked', 0)
        pictures = Photo.objects.filter(Q1)
    elif check_id == u'0' and valid_id != u'3':
        if valid_id == u'4':
            Q2 += ('is_valid', 1)
        elif valid_id == u'5':
            Q2 += ('is_valid', 0)
        pictures = Photo.objects.filter(Q2)
    elif check_id != u'0' and valid_id != u'3':
        if check_id == u'1':
            Q1 += ('is_checked', 1)
        elif check_id == u'2':
            Q1 += ('is_checked', 0)
        if valid_id == u'4':
            Q2 += ('is_valid', 1)
        elif valid_id == u'5':
            Q2 += ('is_valid', 0)
        pictures = Photo.objects.filter(Q1, Q2)
    return render(request, 'pic_app/items_detail.html', {'pictures': pictures})