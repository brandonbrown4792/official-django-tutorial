from models import Question, Choice
from django.utils import timezone

q = Question(question_text="What's up?", pub_date=timezone.now())
q.save()

c1 = Choice(question=q, choice_text="The sky")
c1.save()
c2 = Choice(question=q, choice_text="Ur mom")
c2.save()