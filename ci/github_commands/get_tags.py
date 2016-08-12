import github
import urllib


def get_tags(org_name, repo_name, username, password, start_label=None):
    """returns all the tags in a certain repo filtered on start_label"""
    g = login_github(username, password)
    org = get_github_organization(g, org_name)
    repo = org.get_repo(repo_name)
    tags = get_tags_from_repo(repo, start_label)
    return tags


def login_github(username, password):
    return github.Github(username, password)


def get_github_organization(gh, org_name):
    try:
        org = gh.get_organization(org_name)
    except:
        org = gh.get_user(org_name)
    return org


def get_tags_from_repo(repo, start_label=None):
    refs = repo.get_git_refs()
    if start_label:
        f = lambda ref: (ref.object.type == "tag") & (ref.ref.startswith("refs/tags/" + urllib.quote_plus(start_label)))
    else:
        f = lambda ref: (ref.object.type == "tag")
    tags = filter(f, refs)
    return tags

