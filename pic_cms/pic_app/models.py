# -*- coding: utf-8 -*-
from django.db import models
# from pic_cms.fields import ThumbnailImageField


class Course(models.Model):
    cid = models.CharField(max_length=100)
    cname = models.CharField(max_length=100)

    class Meta:
        ordering = ['cid']

    def __str__(self):
        return self.cid


class Photo(models.Model):
    pid = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos')
    is_checked = models.BooleanField(default=True, blank=True, verbose_name="是否人工校验")
    is_valid = models.BooleanField(default=True, verbose_name="是否有效图片")
    course = models.ForeignKey(Course)
    ocr_text = models.CharField(max_length=300, blank=True, verbose_name="OCR文本")
    correct_text = models.CharField(max_length=300, blank=True, verbose_name="精准文本")
    get_result = models.BooleanField(default=True, blank=True, verbose_name="是否正确结果")
    same_qid = models.CharField(max_length=300, blank=True, verbose_name="相同题目id")
    err_source = models.CharField(max_length=300, blank=True, verbose_name="错误原因")

    def __str__(self):
        return self.pid


