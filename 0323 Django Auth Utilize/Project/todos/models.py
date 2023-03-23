from django.db import models

# Create your models here.
class Todo(models.Model):
    '''
    task = charfield 채택
    isCompleted = False 채택 (vs inProgress = True)
    created_at = datafield # 생성된 시간
    completed_at = datafield # 완료된 시간
    
    
    '''


    task         = models.CharField(max_length=300)     # todo 항목
    isCompleted  = models.BooleanField(default=False)   # 완료 여부
    created_at   = models.DateTimeField(auto_now_add=True) # 생성 시간
    completed_at = models.DateTimeField(auto_now=True)     # 완료 시간