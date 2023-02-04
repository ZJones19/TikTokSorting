# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import requests
import json

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def main():
    #Use refresh token (unchanging) to get a new access token (need new one every time) also using client id and client secret
    newToken = requests.post('https://accounts.google.com/o/oauth2/token',data={'client_id':'620677125812-ccds23d5gqu0fu41uqvmur2s9crjts31.apps.googleusercontent.com','client_secret':'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','refresh_token':'1//01Lxp9upwVcXrCgYIARAAGAESNwF-L9IrKfX_2jk4ddpBWVP6mDLKgzZYiOvkinHlljgPpMdpDjXn8AiT1aMfbv44QQhuDgWosjk','grant_type':'refresh_token'})
    newToken = json.loads(newToken.text)
    newToken = newToken.get('access_token')
    #make the request to the api using api key and token 
    p = {"myRating": "like", "key": "AIzaSyBEDqAaPKfAOqKvw8EjTLlI7A4JE1cmR9M", 'part':'snippet,contentDetails,statistics'}
    myHeaders = {'Authorization' : 'Bearer ' + newToken, 'Accept':'application/json'}
    request = requests.get("https://youtube.googleapis.com/youtube/v3/videos", headers=myHeaders, params = p)

    print(request.text)


if __name__ == "__main__":
    main()