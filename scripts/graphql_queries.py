org_all_repos = """
query ($owner: String!, $endCursor: String) {
  organization(login: $owner) {
    repositories(first: 100, after: $endCursor) {
      pageInfo {
        hasNextPage
        endCursor
      }
      totalCount
      edges {
        node {
          nameWithOwner
          name
          descriptionHTML
          homepageUrl
          isPrivate
          repositoryTopics(first: 50) {
            edges {
              node {
                topic {
                  name
                }
                url
              }
            }
          }
          primaryLanguage {
            name
            color
          }
          languages (first: 50) {
            edges {
              node {
                name
              }
              size
            }
          }
          pushedAt
          forkCount
          stargazers {
            totalCount
          }
          watchers {
            totalCount
          }
        }
      }
    }
    members {
      totalCount
    }
  }
}
"""

repo_wise = """
query ($owner:String!, $repo:String!) {
  repository(owner: $owner, name: $repo) {
    nameWithOwner
    name
    descriptionHTML
    homepageUrl
    isPrivate
    repositoryTopics(first: 50) {
      edges {
        node {
          topic {
            name
          }
          url
        }
      }
    }
    primaryLanguage {
      name
      color
    }
    languages (first: 50) {
      edges {
        node {
          name
        }
        size
      }
    }
    pushedAt
    forkCount
    stargazers {
      totalCount
    }
    watchers {
      totalCount
    }
  }
}
"""
