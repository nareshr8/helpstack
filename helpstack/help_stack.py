# AUTOGENERATED! DO NOT EDIT! File to edit: 00_help_stack.ipynb (unless otherwise specified).

__all__ = ['help_stack', 'api']

# Cell
from functools import wraps
from IPython.display import display, Markdown
from ipywidgets import Tab,Text,Label,Output
import pkg_resources
import traceback
from ghapi.all import GhApi


api = GhApi()

def help_stack(func):
    '''
    The Decorator to be added on top of the function that provides useful insights when an issue occurs in the function
    '''
#     @wraps
    def hs(*args,**kwargs):
        import requests
        val = -1
        try:
            return func(*args, **kwargs)
        except Exception as e:
            tab=Tab()

            search_terms=e.__str__()
            exception_msg = Output()
            with exception_msg:
                print(traceback.format_exc())
            response=requests.get(f'https://api.stackexchange.com/2.3/search?order=desc&sort=activity&tagged=python&intitle={search_terms}&site=stackoverflow')
            stack_overflow_msg = Output()
            with stack_overflow_msg:
                for item in response.json()['items']:
                    if item['is_answered']:
                        display(Markdown(f"- [{item['title']}]({item['link']})"))
            github_msg = Output()
            packages=[p.project_name for p in pkg_resources.working_set]
            github_tabs=Tab()
            github_outputs=[]
            i=0
            for package in packages:
                pypi_resp=requests.get(f'https://pypi.org/pypi/{package}/json')
                if pypi_resp.json()['info']['home_page'].startswith('https://github.com/'):
                    repo=pypi_resp.json()['info']['home_page'].split('https://github.com/')[1].strip()
                    try:
                        result=api.search.issues_and_pull_requests(f'{search_terms}+repo:{repo}')
                        if result['total_count']>0:
                            github_tabs.set_title(i,package)
                            output_val=Output()
                            with output_val:
                                for item in result['items']:
                                    display(Markdown(f"- [{item['title']}]({item['html_url']})"))
                            github_outputs.append(output_val)
                            i+=1
                    except Exception as e:
                        pass
            github_tabs.children=github_outputs
            with github_msg:
                display(github_tabs)

            tab.children = [exception_msg,stack_overflow_msg,github_msg]
            tab.set_title(0,"Stack Trace")
            tab.set_title(1,"Stack Overflow")
            tab.set_title(2,"Github Issues")
            display(tab)
    return hs