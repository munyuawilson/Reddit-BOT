
import praw

class RedditBOT:
    def __init__(self,password,client_secret,user_agent="testing",client_id="KIL2-_1Iu_ITUF2oCnVgYA",username="munyua1"):
        self.password=password
        self.client_secret=client_secret
        self.user_agent=user_agent
        self.client_id=client_id
        self.username=username


    def auth(self):
        
        reddit = praw.Reddit(
            client_id=self.client_id,
            client_secret=self.client_secret,
            user_agent=self.user_agent,
            username=self.username,
            password=self.password
        )

        return reddit
    
    def get_sub_reddit(self,subreddit, keyword,limit=10):
        Reddit=self.auth()
        subreddit_blob=Reddit.subreddit(subreddit).top(limit=limit,time_filter="week")

        for i in subreddit_blob:
            title=i.title
            print(title)
            if keyword in title:
                print(i.title)
                print(i.url)

                print("\n******\t END \t ******")



if __name__=="__main__":
    #example
    saas=RedditBOT("hdhhhdwa1$","hF7KZFgAwMQFXUviBDqCcaxFtrbkDg")
    saas.get_sub_reddit("saas","huge")



