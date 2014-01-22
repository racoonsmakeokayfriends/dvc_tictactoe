dvc_tictactoe
=============

bottle from https://raw.github.com/defnull/bottle/master/bottle.py

testing:
curl -XPOST localhost:8080/write/ -d '{"ginger": "cool"}' --header "Content-Type:application/json"
curl -XGET localhost:8080/read/
