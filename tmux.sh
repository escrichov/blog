#!/bin/bash

SESSIONNAME="blog"

TAB3="browser"
TAB2="server"
TAB1="shell"

DEFAULTTAB=$TAB1

tmux has-session -t $SESSIONNAME &> /dev/null

#if not existing, lets create one
if [ $? != 0 ]
 then
    tmux new-session -s $SESSIONNAME -n $TAB1 -d
    tmux send-keys -t 0 C-m

    #open a second window(tab)
    tmux new-window -t $SESSIONNAME:1 -n $TAB2
    tmux send-keys -t 0 "pipenv run make devserver" C-m

    tmux new-window -t $SESSIONNAME:2 -n $TAB3
    tmux send-keys -t 0 "sleep 1 && google-chrome http://localhost:8000" C-m

    #default window you want to see when entering the session
    tmux select-window -t $SESSIONNAME:$DEFAULTTAB
fi

tmux attach -t $SESSIONNAME
