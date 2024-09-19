from django.db import models

# Create your models here.
class Employee(models.Model):
    empid = models.CharField(max_length=8, primary_key=True)  # 自動生成される従業員ID
    fname = models.CharField(max_length=50)      # 名
    lname = models.CharField(max_length=50)       # 姓
    email = models.EmailField(unique=True)            # メールアドレス（ユニーク）
    role = models.CharField(max_length=100)       # 役職
    department = models.CharField(max_length=100)     # 部署
    hire_date = models.DateField()                    # 入社日

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)    # 従業員に対する外部キー
    clock_in_time = models.DateTimeField()  # 出勤時間
    clock_out_time = models.DateTimeField(null=True, blank=True)  # 退勤時間 # 退勤時間はまだ設定されていない可能性がある
    date = models.DateField()   # 日付
    created_at = models.DateTimeField(auto_now_add=True)    # レコード作成日時
    updated_at = models.DateTimeField(auto_now=True)    # レコード更新日時



