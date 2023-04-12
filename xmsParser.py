# -*- coding: utf-8 -*-









from xhs import FeedType, XhsClient
import json
import time


cookie = "xhsTrackerId=6de830e6-5db9-431c-8d4e-8005046b6530; xhsTrackerId.sig=QBeznnahHZY4E-avcAsclayg8oemuQrLbf1c27Igxvo; xhsTracker=url=explore&searchengine=google; xhsTracker.sig=MRMGzEloSNQs_DaToApEcOmFVQk1-ZoSYnPAaimmG8E; webBuild=2.0.5; a1=187735822e03o1gzi7ffersqmj0mbjv06tgru79f330000566482; webId=29c6a475a9c8204a4ac627cd643ce926; gid=yYWWq2YqKqK0yYWWq2YJJ9Wjd8qlyku3WiidkiqFMA6V8Fq86DVh878882KK4YJ8WKq8yqf8; gid.sign=Lr6cHgb9xmdt5bhvi6g8N6mIh5k=; xsecappid=xhs-pc-web; cache_feeds=[]; extra_exp_ids=yamcha_0327_clt,h5_1208_exp3,ques_clt2; extra_exp_ids.sig=-9P_FIY9nRpp4czlpi3JlPCL_zdr5ZMYd73Vy8sdzzY; websectiga=3fff3a6f9f07284b62c0f2ebf91a3b10193175c06e4f71492b60e056edcdebb2; sec_poison_id=87547850-7936-4bc6-a042-2be4bd480dba; web_session=040069b3b0459e3e7b5f286403364b393faac0"
xhs_client = XhsClient(cookie)



# https://www.xiaohongshu.com/api/sec/v1/sbtsource
# {"data":{"desVersion":"2","validate":true,"commonPatch":["/fe_api/burdock/v2/note/post","/api/sns/web/v1/comment/post","/api/sns/web/v1/note/like","/api/sns/web/v1/note/collect","/api/sns/web/v1/user/follow","/api/sns/web/v1/feed","/api/sns/web/v1/login/activate","/api/sns/web/v1/note/metrics_report"],"url":"https://fe-video-qc.xhscdn.com/fe-platform/e5ef966ee6fa0a0c7c82a9cb9e1feed4435f8331.js","reportUrl":"/fe_api/burdock/v2/shield/profile"},"code":0,"success":true,"msg":"成功"}

  

# user_profile = '5fe35d34000000000101dc95'
user_profile = '60c083cd0000000001004031'




# note_address = '63db8819000000001a01ead1'
# note_address = '643568840000000013008920'
# note_address = '63f31eab00000000130307a0'
note_address = '641af50a0000000013008d2a'


# https://www.xiaohongshu.com/explore/63db8819000000001a01ead1
# https://www.xiaohongshu.com/user/profile/5fe35d34000000000101dc95/643568840000000013008920
# get note info
# note_info = xhs_client.get_note_by_id("63db8819000000001a01ead1")
note_info = xhs_client.get_note_by_id(note_address)
print('-note_info-',note_info)

print('')
print('')
print('')

# get user info
# user_info = xhs_client.get_user_info("5ff0e6410000000001008400")
# print('-user_info-',user_info)
user_info = xhs_client.get_user_info(user_profile)
print('-user_info-',user_info)

print('')
print('')
print('')

# get user notes
# user_notes = xhs_client.get_user_notes("63273a77000000002303cc9b")
user_notes = xhs_client.get_user_notes(user_profile)
print('-user_notes-',user_notes)
print('')
userNotesList = json.loads(user_notes)
print('-userNotesList-',userNotesList)
print('')
print('-cursor-',userNotesList['cursor'])
print('-has_more-',userNotesList['has_more'])
page = 2
while True:
  if userNotesList['has_more'] :
    print('还有用户的笔记',page)
    time.sleep(1)
    user_new_notes = xhs_client.get_user_notes(user_id=user_profile,cursor=userNotesList['cursor'])
    print('-user_new_notes-',user_new_notes)
    userNotesList = json.loads(user_new_notes)
    print('')
    print('-page-',page,'-cursor-',userNotesList['cursor'],'-has_more-',userNotesList['has_more'],'-len[notes]-',len(userNotesList['notes']))
    print('')
    page += 1
    if page == 12 :
      print('-防止死循环-退出了-')
      break
  else :
    break



print('')
print('')
print('')
print('')
print('')
print('')
print('')


# search note
# notes = xhs_client.get_note_by_keyword("小红书")
# print('-search_notes-',notes)

print('')
print('')
print('')

# # get home recommend feed
# recommend_type = FeedType.RECOMMEND
# recommend_notes = xhs_client.get_home_feed(recommend_type)
# print('-recommend_notes-',recommend_notes)


# more functions in development




