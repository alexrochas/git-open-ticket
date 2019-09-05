# git-open-ticket
> minor python function to open Jira ticket in browser from a branch name

## How?

Add a new alias to your zsh/bash/fish:

```bash
alias git-open-ticket='[path_to_script]/git_open_ticket.py'
```

Now just use it as you would with *git commit*.

```bash
~/[some_path]$ git-open-ticket  
```

OR

Add an alias to your git global configuration:

```bash
~/$ git config --global alias.open-ticket '!python3 /[path_to_script]/git-open-ticket/git_open_ticket.py'
```

And the usage:

```bash
~/[some_path]$ git open-ticket 
```

Important to notice that to maintain your Jira url *safe* you need to add a dotenv file in the project root directory as below:

```bash
JIRA_URL=[your.jira.url]
```


## Meta

Alex Rocha - [about.me](http://about.me/alex.rochas) -
