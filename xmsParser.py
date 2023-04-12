# -*- coding: utf-8 -*-









from xhs import FeedType, XhsClient

cookie = ""
xhs_client = XhsClient()

# get note info
note_info = xhs_client.get_note_by_id("63db8819000000001a01ead1")
print('-note_info-',note_info)

# get user info
user_info = xhs_client.get_user_info("5ff0e6410000000001008400")
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




