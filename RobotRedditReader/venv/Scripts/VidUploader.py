
import praw
userAgent="Reddit reader 1.0 by /u/Cthulhus_Cuck"

reddit = praw.Reddit(client_id='EpM-tm-knvhoNQ',
                     client_secret='Rl8lhuns5hJGE5fv1wpxrPn6Xww',
                     user_agent=userAgent,
                     username = 'Rcube_Bot',
                     password = 'm6K3KA3jybH07SRivw#hi*ldH4z8ykBKBc233*NwWVM4h*1$FRr5$rxImzRXOUOwg3JGtS^g1QBiYycLsP8EejKGmR3OHvHDu2T')


reditname = praw.models.Redditor(reddit, name='Cthulhus_Cuck', _data=None)
reditname.message('testsub', 'Hello!\n I am contacting you as you have recently made one of the top comments in an askreddit thread.  '
                                                                                                  'I am a bot who scrapes that sub every day and attemps to make youtube videos out of it.\n\n I know that '
                                                                                                  'these reddit videos are despised in the community, and that is why I have come to it with a new idea: A portion '
                                                                                                  'of the video profits will be re-destributed to the members that made the posts!\n\n All I need from you is that you reply '
                                                                                                  'with a paypal email, and in about a month 50% of the profits will be split between the accepting commenters and the OP.\n\n'
                                                                                                  'If you do not want to be in the video please ignore this and you will not be included.\nThank you!\n\n'
                                                                                                  '**Please message /u/' + username + ' with any concerns.', from_subreddit=None)
