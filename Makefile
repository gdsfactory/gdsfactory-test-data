add:
	git config --unset-all http.https://github.com/.extraheader
	git config --global user.email 62731847+jmatres@users.noreply.github.com
	git config --global user.name "Joaquin Matres"
	git add .
	# git commit --amend -m "add data"
	git commit -m "add data" | echo 'no commit'
	gh repo sync
