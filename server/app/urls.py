from django.urls import path
from .views import *

urlpatterns = [
    path("auth/register/", RegistrationAPI.as_view()),
    path("auth/login/", LoginAPI.as_view()),
    path("auth/user/", UserAPI.as_view()),
    path('main/project/', ProjectAPI.as_view()),
    path('explore/news/', NewsAPI.as_view()),
    path('main/project_recommend/', Project_recommendAPI.as_view()),
    path('explore/popular/', Popular_projectAPI.as_view()),
    path('main/group/', GroupAPI.as_view()),
    path('notify/', NotifyAPI.as_view()),
    path('notify/read/', Notify_readAPI.as_view()),
    path('request/', RequestAPI.as_view()),
    path('request_accept/', Reqeust_acceptAPI.as_view()),
    path("search/", SearchAPI.as_view()),
    path("check/", CheckAPI.as_view()),
    path("follow/", User_followAPI.as_view()),
    path('group_entry/', Group_entryAPI.as_view()),
    path('idea/create/', Idea_createAPI.as_view()),
    path('idea/update/', Idea_updateAPI.as_view()),
    path('idea/delete/', Idea_deleteAPI.as_view()),
    path('idea/loc/create/', Idea_locCreateAPI.as_view()),
    path('idea/loc/update/', Idea_locUpdateAPI.as_view()),
    path('project/create/', Project_createAPI.as_view()),
    path('project/update/', Project_updateAPI.as_view()),
    path('project/delete/', Project_deleteAPI.as_view()),
    path('person_tendency/update/', Person_tendencyUpdateAPI.as_view()),
    path('group_tendency/update/', Group_tendencyUpdateAPI.as_view()),
    path('group_tendency/create/', Group_tendencyCreateAPI.as_view()),
    path('person_tendency/create/', Person_tendencyCreateAPI.as_view()),
    path('page/index/', Page_indexAPI.as_view()),
    path('project/detail/', Project_detailAPI.as_view()),
    path('project_category/create/', Project_categoryAPI.as_view()),
    path('user_img/update/', UserImg_updateAPI.as_view()),
    path('group_img/update/', GroupImg_updateAPI.as_view()),
    path('idea/fork/history/', Idea_forkHistoryAPI.as_view()),
    path('idea/fork/create/', Idea_forkCreateAPI.as_view()),
    path('idea/keyword/create/', Idea_keywordCreateAPI.as_view()),
    path('idea/keyword/list/create/', Idea_keywordListCreateAPI.as_view()),
    path('project/like/', Project_likeCreateAPI.as_view()),
    path('project/hit/', Project_hitCreateAPI.as_view()),
    path('idea/load/', Idea_loadAPI.as_view()),
    path('idea/child/create/', Idea_childCreateAPI.as_view()),
    path('search/log/view/', Search_logViewAPI.as_view()),
    path('search/log/create/', Search_logCreateAPI.as_view()),
    path('project_img/update/', Project_PDFAPI.as_view()),
    path('idea/root/create/', Idea_rootCreateAPI.as_view()),
    path('project/like/delete/', Project_likeDelete.as_view()),
    path('follow/insert/', FollowingAPI.as_view()),
    path('follow/delete/', Following_deleteAPI.as_view()),
    # path('chat/', ChatAPI.as_view()),
    # path('chat_entry/', ChatEntryAPI.as_view()),
]