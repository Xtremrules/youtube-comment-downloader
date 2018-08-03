import json
from main import download_comments

info = json.load(open('info.json'))
comments = []

for video_id in info['video_list']:
    print('video %s' % video_id)
    count = 0
    for comment in download_comments(video_id):

        # this part prints the specified user, have fun
        if comment['username'] == info['username']:
            comments.append({'v_id': video_id, 'comment': comment})

        count += 1
        if info['limit'] <= count:
            break

with open('results.json', 'w') as fp:
    print(json.dumps(comments), file=fp)
