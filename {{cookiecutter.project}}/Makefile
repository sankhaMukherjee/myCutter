

firstRun:

	@# Make sure that everything in the bin
	@# folder has the right permissions
	@# --------------------------------------
	@chmod 744 bin/*

	# Create the virtual environment
	# --------------------------------------
	@bin/vEnv.sh

	# generate the first commit
	# --------------------------------------
	git init
	git add *
	git remote add origin {{cookiecutter.remote}}
	git commit -m 'This is the first commit'
	# Geenerate the master branch
	# ......................................
	git push origin master
	# Geenerate the rest of the branches
	# ......................................
	git checkout -b dev
	git push origin dev

