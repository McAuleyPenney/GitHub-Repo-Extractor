from github import Github
import csv

#establish connection
git = Github("token")

# repos to mined
repoList = ["Facebook/react","StuckInsideJake/386_Team_7","JabRef/jabref","StuckInsideJake/EricAndreDiscordBot"]
repo = repoList[0]

#rApi = git.get_repo(repoList[0])

#apis
api = git.get_repo(repo)


limit = 5


# pull request related apis
pr = api.get_pulls()
pulls = api.get_pulls(state='open', sort='created', base='master')

# issue related apis
issue = api.get_issues()
issues = api.get_issues(state="closed")

#complete list
data = []

#Pull request related lists
prNumL = []

#Issue related lists
issueClosedDates = []
issueAuthors = []
issueTitles = []
issueBodies = []
isssueComments = []


def main():
   #
    with open("github.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_NONE, delimiter='|', quotechar='', escapechar='\\',lineterminator='\n')
        descriptors = "PR_Number,Issue_Closed_Date, Issue_Author, Issue_Title, Issue_Body, Issue_comments, PR_Closed_Date,PR_Author, PR_Title, PR_Body, PR_Comments, Commit_Author, Commit_Date, Commit_Message, isPR"
        cont_pulls = 0
        cont_issues = 0

        # sets up the table
        writer.writerow([descriptors])

        prData = getPRNumber(limit)
        closedDates = getIssueClosedDate(limit)
        issueAuthors = getIssueAuthor(limit)
        issueTitles = getIssueTitle(limit)
        issueBodies = getIssueBody(limit)

        data = [prNumL, issueClosedDates, issueAuthors, issueTitles, issueBodies]

        for prIndex in prData:
            writer.writerow([prIndex])


   #
def getPRNumber(inLimit):
    #
    outList = []
    index = 0

    for pr in pulls:

       if index < inLimit:
          ftitle = ''
          print(pr.number)
          prStr = str(pr.number) + "," + ftitle
          print(prStr)
          outList.append(prStr)
          index+=1
       else:
           print("---------------------")
           print("loop exit-PRNumber")
           print("---------------------")
           break
    return outList
   #

def getIssueClosedDate(inLimit):
    #
    outList = []
    index = 0

    for issue in issues:

        if index < inLimit:
           issueDateStr = str(issue.closed_at)
           print(issueDateStr)
           outList.append(issueDateStr)
           index+=1
        else:
            print("---------------------")
            print("loop exit-closedDates")
            print("---------------------")
            break

    return outList
    #

def getIssueAuthor(inLimit):
    #
    outList = []
    index = 0

    for issue in issues:
        if index < inLimit:
           issueAuthorStr = str(issue.user.name)
           print(issueAuthorStr)
           outList.append(issueAuthorStr)
           index+=1
        else:
            print("---------------------")
            print("loop exit-IssueAuthor")
            print("---------------------")
            break
    return outList
    #

def getIssueTitle(inLimit):
    #
    outList = []
    index = 0

    for issue in issues:
        if index < inLimit:
           issueTitleStr = str(issue.title)
           print("Getting issue title at index: "+str(index))
           index+=1
           outList.append(issueTitleStr)
        else:
            print("-----------------")
            print("loop exit-IssueTitle")
            print("-----------------")
            break
    return outList
    #


def getIssueBody(inLimit):
    #
    outList = []
    index = 0

    for issue in issues:
        if index < inLimit:
           issueBodyStr = str(issue.body)
           print("getting body at index:" + str(index))
           index+=1
           outList.append(issueBodyStr)
        else:
            print("---------------")
            print("loop exit-IssueBody")
            print("---------------")
            break
    return outList
    #

def getIssueComments(inLimit):
    #
    outList = []
    index = 0

    for issue in issues:
        if index < inLimit:
           issueCommentStr = str(issue.comments)
           print("getting comments at index:"+str(index))
           index+=1
           outList.append(issueCommentStr)
        else:
            print("--------------")
            print("loop exit-IssueComments")
            print("--------------")
            break
    return outList
    #


if __name__ == '__main__':
    main()
