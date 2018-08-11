#指定したユーザーのフォロイングを全部フォローする
# Tweepyライブラリをインポート
import tweepy
# 各種キーをセット
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_SECRET = ""
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
#APIインスタンスを作成
api = tweepy.API(auth)
userid = "" #ここに自分のuseridを入れる
targetid = "" #フォロワーが欲しいユーザーのuseridを入れる
following_id = api.friends_ids(userid) #自分のアカウントのフォロイングをすべて取得する
target_following_id = api.friends_ids(targetid)#ターゲットのアカウントのフォロイングを全て取得する
for target_following in target_following_id:
   if target_following not in following_id: #ターゲットがフォローしているユーザーだけ取得する
     print("フォローするユーザー名")
     targetname = api.get_user(target_following).name
     print(targetname)
     api.create_friendship(target_following)
