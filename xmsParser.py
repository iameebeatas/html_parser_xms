# -*- coding: utf-8 -*-









from xhs import FeedType, XhsClient

cookie = "xhsTrackerId=6de830e6-5db9-431c-8d4e-8005046b6530; xhsTrackerId.sig=QBeznnahHZY4E-avcAsclayg8oemuQrLbf1c27Igxvo; xhsTracker=url=explore&searchengine=google; xhsTracker.sig=MRMGzEloSNQs_DaToApEcOmFVQk1-ZoSYnPAaimmG8E; webBuild=2.0.5; a1=187735822e03o1gzi7ffersqmj0mbjv06tgru79f330000566482; webId=29c6a475a9c8204a4ac627cd643ce926; gid=yYWWq2YqKqK0yYWWq2YJJ9Wjd8qlyku3WiidkiqFMA6V8Fq86DVh878882KK4YJ8WKq8yqf8; gid.sign=Lr6cHgb9xmdt5bhvi6g8N6mIh5k=; xsecappid=xhs-pc-web; cache_feeds=[]; extra_exp_ids=yamcha_0327_clt,h5_1208_exp3,ques_clt2; extra_exp_ids.sig=-9P_FIY9nRpp4czlpi3JlPCL_zdr5ZMYd73Vy8sdzzY; websectiga=3fff3a6f9f07284b62c0f2ebf91a3b10193175c06e4f71492b60e056edcdebb2; sec_poison_id=87547850-7936-4bc6-a042-2be4bd480dba; web_session=040069b3b0459e3e7b5f286403364b393faac0"
xhs_client = XhsClient(cookie)

# get note info
note_info = xhs_client.get_note_by_id("63db8819000000001a01ead1")
print('-note_info-',note_info)

# get user info
user_info = xhs_client.get_user_info("5ff0e6410000000001008400")
print('-user_info-',user_info)
user_info = xhs_client.get_user_info("5fe35d34000000000101dc95")
print('-user_info-',user_info)


# get user notes
user_notes = xhs_client.get_user_notes("63273a77000000002303cc9b")
print('-user_notes-',user_notes)


# search note
notes = xhs_client.get_note_by_keyword("小红书")
print('-search_notes-',notes)


# get home recommend feed
recommend_type = FeedType.RECOMMEND
recommend_notes = xhs_client.get_home_feed(recommend_type)
print('-recommend_notes-',recommend_notes)


# more functions in development




