

grantPermissions:
	chmod 766 ../bin/*

run:
	../bin/run.sh

runA:
	../bin/run.sh -a

# This is a quick check for timming.
# For thorough results, use the profile
# option
runT:
	echo "Simple timing analysis"
	../bin/run.sh -t

clean:
	../bin/clean.sh

# ---- Easy way of checking the functions ---------
checkLog:
	../bin/checkLog.sh

checkTime:
	../bin/checkTime.sh

test:
	python3 -m pytest ../tests

docInit:
	@echo 'Generating a fresh copy of the docs ...'
	@rm -rf ../docs
	@mkdir ../docs
	@sphinx-apidoc -F -o ../docs .
	@echo '+------------------------------------------------------------+'
	@echo '|Do the folliowing to generate docs:                         |'
	@echo '+------------------------------------------------------------+'
	@echo '|1. make sure to insert the system path in the right folder  |'
	@echo '|2. add the `sphinx.ext.napoleon` extention                  |'
	@echo '|3. Add the specs for the napoleon extension:                |'
	@echo '     napoleon_google_docstring = True                         '
	@echo '     napoleon_numpy_docstring = True                          '
	@echo '     napoleon_include_init_with_doc = False                   '
	@echo '     napoleon_include_private_with_doc = False                '
	@echo '     napoleon_include_special_with_doc = True                 '
	@echo '     napoleon_use_admonition_for_examples = False             '
	@echo '     napoleon_use_admonition_for_notes = False                '
	@echo '     napoleon_use_admonition_for_references = False           '
	@echo '     napoleon_use_ivar = False                                '
	@echo '     napoleon_use_param = True                                '
	@echo '     napoleon_use_rtype = True                                '
	@echo '|4. build the documentation with the `make doc`      command |'
	@echo '+------------------------------------------------------------+'

doc:
	sphinx-build -b html -aE -d ../docs/doctrees -c ../docs ../docs ../docs/_build/html

