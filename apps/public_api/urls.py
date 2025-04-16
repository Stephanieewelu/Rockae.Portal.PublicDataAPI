from django.urls import path
from . import GetUserInformation, ListQuizzesInHallOfQuiz,ListUserFeedback,ListQuizFeedback

urlpatterns = [
    path('get-user-info/', GetUserInformation.get_user_info, name='get-user-info'),
    path('list-quizzes-in-hallofquiz/', ListQuizzesInHallOfQuiz.list_quizzes_in_hallofquiz, name='list-quizzes-in-hallofquiz'),
    path('list-user-feedback/', ListUserFeedback.list_user_feedback, name='list-user-feedback'),
    path('list-quiz-feedback/', ListQuizFeedback.list_quiz_feedback, name='list-quiz-feedback'),
    
]
