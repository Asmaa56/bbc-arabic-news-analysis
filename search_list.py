#!/usr/bin/python
import os #new

import google.oauth2.credentials #new
import google_auth_oauthlib.flow #new
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
from google_auth_oauthlib.flow import InstalledAppFlow #new



# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyDEolnH_lnjnWHty9T5rF31LO5vUtKLr7Q"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(q, max_results=50,order="relevance", token=None, location=None, location_radius=None):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
    search_response = youtube.search().list(
    q=q,
    type="video",
    pageToken=token,    
    order=order,
    location=location,    
    part="id,snippet",
    maxResults=max_results).execute()
    
    videos = []
    channelId = []
    title = []
    videoId = []
    categoryId = []
    favoriteCount = []
    viewCount = []
    likeCount = []
    dislikeCount = []
    commentCount = []
    #category = []
    #tags = []
    channels = []
    playlists = []
    
    

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append("%s (%s)" % (search_result["snippet"]["title"],
                                 search_result["id"]["videoId"]))
            response = youtube.videos().list(
                part=('statistics, snippet'),id=search_result['id']['videoId']).execute()
            
            channelId.append(response['items'][0]['snippet']['channelId'])
            title.append(search_result['snippet']['title']) 
            videoId.append(search_result['id']['videoId'])
            categoryId.append(response['items'][0]['snippet']['categoryId'])
            favoriteCount.append(response['items'][0]['statistics']['favoriteCount'])
            viewCount.append(response['items'][0]['statistics']['viewCount'])
            #likeCount.append(response['items'][0]['statistics']['likeCount'])
            #dislikeCount.append(response['items'][0]['statistics']['dislikeCount'])
    video_response = youtube.videos().list(id=videoId,part="statistics").execute()
    for search_result in video_response.get("items",[]):    
            
        if 'commentCount' not in search_result["statistics"]:
            commentCount = 0
        else:
             commentCount = search_result["statistics"]["commentCount"]
        if 'favoriteCount' not in search_result["statistics"]:
            favoriteCount = 0
        else:
             favoriteCount = search_result["statistics"]["favoriteCount"]
 
        #if 'tags' not in response['items'][0]['snippet'].keys():
            #tags.append(response['items'][0]['snippet']['tags'])
        #else:
           # tags.append([])
        
        if 'likeCount' not in search_result["statistics"]:
            likeCount = 0
        else:
             likeCount = search_result["statistics"]["likeCount"]
        if 'dislikeCount' not in search_result["statistics"]:
            dislikeCount = 0
        else:
             dislikeCount = search_result["statistics"]["dislikeCount"]  

    youtube_dict =    {'channelId':channelId,'categoryId':categoryId,'title':title,'videoId':videoId,'viewCount':
                    viewCount,'commentCount':commentCount,'favoriteCount':favoriteCount,'likeCount':likeCount,
                       'dislikeCount':dislikeCount}
    
    
    
    #if __name__ == "__main__":
       # argparser.add_argument("--q", help="Search term", default="Google")
       # argparser.add_argument("--max-results", help="Max results", default=25)
       # args = argparser.parse_args()

    #try:
       # youtube_search(args)
    #except HttpError :
       # print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
    return youtube_dict





