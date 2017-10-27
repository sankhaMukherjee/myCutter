

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
	@git init
	@git add *
	@git commit -m 'This is the first commit'

