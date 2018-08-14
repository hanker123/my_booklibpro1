# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
#年级模型类
class Grade(models.Model):
    g_id=models.AutoField(primary_key=True)
    gname=models.CharField(max_length=30,unique=True)

    def __unicode__(self):
        return u'%s'%self.gname

    class Meta:
        db_table='t_grade'
#专业模型类
class Major(models.Model):
    m_id=models.AutoField(primary_key=True)
    mname=models.CharField(max_length=30,unique=True)

    def __unicode__(self):
        return u'%s'%self.mname

    class Meta:
        db_table='t_major'

#借阅人类模型类
class UserCategory(models.Model):
    uc_id=models.AutoField(primary_key=True)
    uname=models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s'%self.uname

    class Meta:
        db_table='t_usercategory'

#借阅模型类
class User(models.Model):
    s_id=models.AutoField(primary_key=True)
    sname=models.CharField(max_length=30)
    sphone=models.CharField(max_length=30)#数据需要做预判，11位手机号，正则
    gender=models.CharField(max_length=30)#数据需要做预判，只能为男，女
    spwd=models.CharField(max_length=30)
    sIsDelete=models.BooleanField(default=False)
    grade=models.ForeignKey(Grade,related_name='user')
    major=models.ForeignKey(Major,related_name='user')
    usca=models.ForeignKey(UserCategory,related_name='user')
    sCreatedTime=models.DateTimeField(auto_now_add=True)
    s_img=models.ImageField(upload_to='imgs')

    def __unicode__(self):
        return u'%s'%self.sname

    class Meta:
        db_table='t_user'

#管理员职位模型类
class Position(models.Model):
    p_id=models.AutoField(primary_key=True)
    pname=models.CharField(max_length=100,unique=True)

    def __unicode__(self):
        return u'%s'%self.pname

    class Meta:
        db_table='t_position'
#管理员模型类
class BManager(models.Model):
    e_id=models.AutoField(primary_key=True)
    ename=models.CharField(max_length=30)
    ephone=models.CharField(max_length=30)
    mpwd = models.CharField(max_length=30)
    mIsDelete=models.BooleanField(default=False)
    eCreatedTime=models.DateTimeField(auto_now_add=True)
    m_img=models.ImageField(upload_to='imgs')
    position=models.ForeignKey(Position,related_name='bmanager')

    def __unicode__(self):
        return u'%s'%self.ename

    class Meta:
        db_table='t_manager'

#书架模型类
class BookRack(models.Model):
    br_id=models.AutoField(primary_key=True)
    brname=models.CharField(max_length=100,unique=True)

    def __unicode__(self):
        return u'%s'%self.brname

    class Meta:
        db_table='t_bookrack'

#图书类型模型类
class BookCategory(models.Model):
    bc_id=models.AutoField(primary_key=True)
    bcname=models.CharField(max_length=30,unique=True)

    def __unicode__(self):
        return u'%s'%self.bcname

    class Meta:
        db_table='t_bookcategory'

#图书学科模型类
class Subject(models.Model):
    sub_id=models.AutoField(primary_key=True)
    subname=models.CharField(max_length=30)
    bookcategory=models.ForeignKey(BookCategory,related_name='subject')

    def __unicode__(self):
        return u'%s'%self.subname

    class Meta:
        db_table='t_subject'
#图书模型类
class Book(models.Model):
    b_id=models.AutoField(primary_key=True)
    bname=models.CharField(max_length=100)
    publishing=models.CharField(max_length=100)
    author=models.CharField(max_length=50)
    pubTime=models.DateField()
    addTime=models.DateTimeField(auto_now_add=True)
    b_img=models.ImageField(upload_to='imgs')
    bookrack=models.ForeignKey(BookRack,related_name='book')
    subject=models.ForeignKey(Subject,related_name='book')

    def __unicode__(self):
        return u'%s'%self.bname

    class Meta:
        db_table='t_book'

#借阅模型类
class Borrow(models.Model):
    bor_id=models.AutoField(primary_key=True)
    bTime=models.DateTimeField(auto_now_add=True)
    rTime=models.DateTimeField()
    user=models.ForeignKey(User,related_name='borrow')
    book=models.ForeignKey(Book,related_name='borrow')

    def __unicode__(self):
        return u'%s'%self.bor_id

    class Meta:
        db_table='t_borrow'

class Unkownbook(models.Model):
    un_id=models.AutoField(primary_key=True)
    unkname=models.CharField(max_length=100,unique=True)
    unkauthor=models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s'%self.unkname

    class Meta:
        db_table='t_unkownbook'