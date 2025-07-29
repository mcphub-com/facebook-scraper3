import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/krasnoludkolo/api/facebook-scraper3'

mcp = FastMCP('facebook-scraper3')

@mcp.tool()
def locations(query: Annotated[str, Field(description='')]) -> dict: 
    '''Search for facebook locations id. If you get strange results, try add country to query and/or try without diacritic'''
    url = 'https://facebook-scraper3.p.rapidapi.com/search/locations'
    headers = {'x-rapidapi-host': 'facebook-scraper3.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_video(query: Annotated[str, Field(description='')],
                 cursor: Annotated[Union[str, None], Field(description='')] = None,
                 recent_videos: Annotated[Union[bool, None], Field(description=' Example: rapid_do_not_include_in_request_key')] = None,
                 location_uid: Annotated[Union[str, None], Field(description='')] = None,
                 start_date: Annotated[Union[str, datetime, None], Field(description='Date (yyyy-mm-dd)')] = None,
                 end_date: Annotated[Union[str, datetime, None], Field(description='Date (yyyy-mm-dd)')] = None) -> dict:
    '''Performs facebook videos search'''
    url = 'https://facebook-scraper3.p.rapidapi.com/search/videos'
    headers = {'x-rapidapi-host': 'facebook-scraper3.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'cursor': cursor,
        'recent_videos': recent_videos,
        'location_uid': location_uid,
        'start_date': start_date,
        'end_date': end_date,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_post(query: Annotated[str, Field(description='')],
                cursor: Annotated[Union[str, None], Field(description='')] = None,
                recent_posts: Annotated[Union[bool, None], Field(description=' Example: rapid_do_not_include_in_request_key')] = None,
                location_uid: Annotated[Union[str, None], Field(description='')] = None,
                start_date: Annotated[Union[str, datetime, None], Field(description='Date (yyyy-mm-dd)')] = None,
                end_date: Annotated[Union[str, datetime, None], Field(description='Date (yyyy-mm-dd)')] = None) -> dict:
    '''Performs facebook posts search'''
    url = 'https://facebook-scraper3.p.rapidapi.com/search/posts'
    headers = {'x-rapidapi-host': 'facebook-scraper3.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'cursor': cursor,
        'recent_posts': recent_posts,
        'location_uid': location_uid,
        'start_date': start_date,
        'end_date': end_date,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_place(query: Annotated[str, Field(description='')],
                 cursor: Annotated[Union[str, None], Field(description='')] = None,
                 location_uid: Annotated[Union[str, None], Field(description='')] = None) -> dict:
    '''Search for fb place'''
    url = 'https://facebook-scraper3.p.rapidapi.com/search/places'
    headers = {'x-rapidapi-host': 'facebook-scraper3.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'cursor': cursor,
        'location_uid': location_uid,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_pages(query: Annotated[str, Field(description='')],
                 cursor: Annotated[Union[str, None], Field(description='')] = None,
                 location_uid: Annotated[Union[str, None], Field(description='')] = None) -> dict:
    '''Searches for facebook pages'''
    url = 'https://facebook-scraper3.p.rapidapi.com/search/pages'
    headers = {'x-rapidapi-host': 'facebook-scraper3.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'cursor': cursor,
        'location_uid': location_uid,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_events(query: Annotated[str, Field(description='')],
                  cursor: Annotated[Union[str, None], Field(description='')] = None,
                  location_uid: Annotated[Union[str, None], Field(description='')] = None,
                  start_date: Annotated[Union[str, datetime, None], Field(description='Date (yyyy-mm-dd)')] = None,
                  end_date: Annotated[Union[str, datetime, None], Field(description='Date (yyyy-mm-dd)')] = None) -> dict:
    '''Searches for facebook events'''
    url = 'https://facebook-scraper3.p.rapidapi.com/search/events'
    headers = {'x-rapidapi-host': 'facebook-scraper3.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'cursor': cursor,
        'location_uid': location_uid,
        'start_date': start_date,
        'end_date': end_date,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def page_details(url: Annotated[str, Field(description='')]) -> dict:
    '''Read page details'''
    url = 'https://facebook-scraper3.p.rapidapi.com/page/details'
    headers = {'x-rapidapi-host': 'facebook-scraper3.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'url': url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def pages_posts(page_id: Annotated[str, Field(description='')],
                cursor: Annotated[Union[str, None], Field(description='')] = None,
                start_date: Annotated[Union[str, datetime, None], Field(description='Date (yyyy-mm-dd)')] = None,
                end_date: Annotated[Union[str, datetime, None], Field(description='Date (yyyy-mm-dd)')] = None) -> dict:
    '''Read page posts (from recent)'''
    url = 'https://facebook-scraper3.p.rapidapi.com/page/posts'
    headers = {'x-rapidapi-host': 'facebook-scraper3.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page_id': page_id,
        'cursor': cursor,
        'start_date': start_date,
        'end_date': end_date,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def pages_photos(page_id: Annotated[str, Field(description='')],
                 cursor: Annotated[Union[str, None], Field(description='')] = None) -> dict:
    '''Read page photos (from recent) Use cursor to get next page of results'''
    url = 'https://facebook-scraper3.p.rapidapi.com/page/photos'
    headers = {'x-rapidapi-host': 'facebook-scraper3.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page_id': page_id,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def page_reviews(page_id: Annotated[str, Field(description='')],
                 cursor: Annotated[Union[str, None], Field(description='')] = None) -> dict:
    '''Get page reviews. Use cursor to get next page'''
    url = 'https://facebook-scraper3.p.rapidapi.com/page/reviews'
    headers = {'x-rapidapi-host': 'facebook-scraper3.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page_id': page_id,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def page_reels(page_id: Annotated[str, Field(description='')],
               cursor: Annotated[Union[str, None], Field(description='')] = None) -> dict:
    '''Get page reels by page id'''
    url = 'https://facebook-scraper3.p.rapidapi.com/page/reels'
    headers = {'x-rapidapi-host': 'facebook-scraper3.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page_id': page_id,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def page_future_events(page_id: Annotated[str, Field(description='')],
                       cursor: Annotated[Union[str, None], Field(description='')] = None) -> dict:
    '''Get all future events created by page'''
    url = 'https://facebook-scraper3.p.rapidapi.com/page/events/future'
    headers = {'x-rapidapi-host': 'facebook-scraper3.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page_id': page_id,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def page_past_events(page_id: Annotated[str, Field(description='')],
                     cursor: Annotated[Union[str, None], Field(description='')] = None) -> dict:
    '''Get all past events created by page. Use cursor to get next page of results.'''
    url = 'https://facebook-scraper3.p.rapidapi.com/page/events/past'
    headers = {'x-rapidapi-host': 'facebook-scraper3.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page_id': page_id,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def comments(post_id: Annotated[str, Field(description='')],
             cursor: Annotated[Union[str, None], Field(description='')] = None) -> dict:
    '''Get post comments'''
    url = 'https://facebook-scraper3.p.rapidapi.com/post/comments'
    headers = {'x-rapidapi-host': 'facebook-scraper3.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'post_id': post_id,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def comments_nested(post_id: Annotated[Union[str, None], Field(description='')] = None,
                    comment_id: Annotated[Union[str, None], Field(description='')] = None,
                    expansion_token: Annotated[Union[str, None], Field(description='')] = None) -> dict:
    '''Get nested comments. You need to use legacy fb id'''
    url = 'https://facebook-scraper3.p.rapidapi.com/post/comments_nested'
    headers = {'x-rapidapi-host': 'facebook-scraper3.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'post_id': post_id,
        'comment_id': comment_id,
        'expansion_token': expansion_token,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_post_details(post_id: Annotated[Union[str, None], Field(description='')] = None,
                     post_url: Annotated[Union[str, None], Field(description='')] = None) -> dict:
    '''Get post details by url or post id. If both are set, post id is used.'''
    url = 'https://facebook-scraper3.p.rapidapi.com/post'
    headers = {'x-rapidapi-host': 'facebook-scraper3.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'post_id': post_id,
        'post_url': post_url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def reshares(post_id: Annotated[Union[str, None], Field(description='')] = None,
             cursor: Annotated[Union[str, None], Field(description='')] = None) -> dict:
    '''Get post reshares'''
    url = 'https://facebook-scraper3.p.rapidapi.com/post/share'
    headers = {'x-rapidapi-host': 'facebook-scraper3.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'post_id': post_id,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def events_details_by_url(url: Annotated[str, Field(description='')]) -> dict:
    '''Get events details'''
    url = 'https://facebook-scraper3.p.rapidapi.com/event/details'
    headers = {'x-rapidapi-host': 'facebook-scraper3.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'url': url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def events_details_by_id(event_id: Annotated[str, Field(description='')]) -> dict:
    '''Get events details by event id'''
    url = 'https://facebook-scraper3.p.rapidapi.com/event/details_id'
    headers = {'x-rapidapi-host': 'facebook-scraper3.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'event_id': event_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def page_events(page_id: Annotated[str, Field(description='')],
                cursor: Annotated[Union[str, None], Field(description='')] = None) -> dict:
    '''Get all future events created by page'''
    url = 'https://facebook-scraper3.p.rapidapi.com/page/events/future'
    headers = {'x-rapidapi-host': 'facebook-scraper3.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page_id': page_id,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_group_future_events(group_id: Annotated[str, Field(description='')],
                            cursor: Annotated[Union[str, None], Field(description='')] = None) -> dict:
    '''Get group future events. Only PUBLIC groups can be scrapped! If there are no post response, check if group is not private. Use cursor to get next page of events!'''
    url = 'https://facebook-scraper3.p.rapidapi.com/group/future_events'
    headers = {'x-rapidapi-host': 'facebook-scraper3.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'group_id': group_id,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_group_posts(group_id: Annotated[str, Field(description='')],
                    cursor: Annotated[Union[str, None], Field(description='')] = None,
                    sorting_order: Annotated[Literal['CHRONOLOGICAL', 'TOP_POSTS', None], Field(description=' Example: CHRONOLOGICAL')] = None) -> dict:
    '''Get group posts. Only PUBLIC groups can be scrapped! If there are no post response, check if group is not private.'''
    url = 'https://facebook-scraper3.p.rapidapi.com/group/posts'
    headers = {'x-rapidapi-host': 'facebook-scraper3.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'group_id': group_id,
        'cursor': cursor,
        'sorting_order': sorting_order,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_group_details(url: Annotated[str, Field(description='')]) -> dict:
    '''Get group summary'''
    url = 'https://facebook-scraper3.p.rapidapi.com/group/details'
    headers = {'x-rapidapi-host': 'facebook-scraper3.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'url': url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_group_id(url: Annotated[str, Field(description='')]) -> dict:
    '''Getting group facebook id'''
    url = 'https://facebook-scraper3.p.rapidapi.com/group/id'
    headers = {'x-rapidapi-host': 'facebook-scraper3.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'url': url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def profile_posts(profile_id: Annotated[str, Field(description='')],
                  cursor: Annotated[Union[str, None], Field(description='')] = None,
                  start_date: Annotated[Union[str, datetime, None], Field(description='Date (yyyy-mm-dd)')] = None,
                  end_date: Annotated[Union[str, datetime, None], Field(description='Date (yyyy-mm-dd)')] = None) -> dict:
    '''Read profile posts (from recent), if public'''
    url = 'https://facebook-scraper3.p.rapidapi.com/profile/posts'
    headers = {'x-rapidapi-host': 'facebook-scraper3.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'profile_id': profile_id,
        'cursor': cursor,
        'start_date': start_date,
        'end_date': end_date,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def profiles_details_by_id(profile_id: Annotated[str, Field(description='')]) -> dict:
    '''Get profiles details by id'''
    url = 'https://facebook-scraper3.p.rapidapi.com/profile/details_id'
    headers = {'x-rapidapi-host': 'facebook-scraper3.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'profile_id': profile_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def profile_details_by_url(url: Annotated[str, Field(description='')]) -> dict:
    '''Get profile details by url'''
    url = 'https://facebook-scraper3.p.rapidapi.com/profile/details_url'
    headers = {'x-rapidapi-host': 'facebook-scraper3.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'url': url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def profile_id(url: Annotated[str, Field(description='')]) -> dict:
    '''Get profile id by url'''
    url = 'https://facebook-scraper3.p.rapidapi.com/profile/profile_id'
    headers = {'x-rapidapi-host': 'facebook-scraper3.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'url': url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def game_lives(game_id: Annotated[str, Field(description='')],
               sort_order: Annotated[Literal['VIEWERS', 'SUGGESTED'], Field(description=' Example: VIEWERS')],
               cursor: Annotated[Union[str, None], Field(description='')] = None) -> dict:
    '''Get game live videos Use cursor to get next page.'''
    url = 'https://facebook-scraper3.p.rapidapi.com/gaming/live'
    headers = {'x-rapidapi-host': 'facebook-scraper3.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'game_id': game_id,
        'sort_order': sort_order,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def browse_games(query: Annotated[str, Field(description='')],
                 sort_order: Annotated[Literal['VIEWERS', 'SUGGESTED'], Field(description=' Example: VIEWERS')],
                 cursor: Annotated[Union[str, None], Field(description='')] = None) -> dict:
    '''Browse games. Use empty query for browse all games. Use cursor to get next page.'''
    url = 'https://facebook-scraper3.p.rapidapi.com/gaming/games'
    headers = {'x-rapidapi-host': 'facebook-scraper3.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'sort_order': sort_order,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()


if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
