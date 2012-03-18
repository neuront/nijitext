DOC_DIR=doc

ifndef PYTHON
	PYTHON=python
endif

doc:nijitext.html a-dive-to-source.html

%.html:$(DOC_DIR)/%.md
	cat $(DOC_DIR)/$*.md | $(PYTHON) docgen.py > $*.html || rm -f $*.html

test:
	$(PYTHON) test.py

clean:
	rm -rf $(TMP_DIR)
	rm -f *.html
	find | grep pyc | awk '{ print "rm", $$1 }' | sh
