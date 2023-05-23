SHELL:=/bin/bash
define backup_data
	echo "" # Empty line
	-mkdir back 2> /dev/null
	mv ./input.txt ./back/
	mv ./answers.txt ./back/
endef

define restore_data
	#Restore data
	cp ./back/input.txt ./input.txt
	cp ./back/answers.txt ./answers.txt
	echo "" # Empty line
endef


define test_input
	set -e ;\
	TEST_RESULTS=$$(make tests 2> /dev/null | grep "[0-9]*[0-9]/[0-9][0-9]*" -o ); \
	TEST_PERCENTAGE=$$((100*$$TEST_RESULTS)); \
	if [ "$(1)" == "1" ]; then \
		if [ $$TEST_PERCENTAGE  -lt 25 ]; then \
			/bin/bash -c "echo  -e '\033[31m$$TEST_RESULTS'"; \
		elif [ $$TEST_PERCENTAGE  -lt 50 ]; then \
			/bin/bash -c "echo  -e '\033[35m$$TEST_RESULTS'"; \
		elif [ $$TEST_PERCENTAGE  -lt 75 ]; then \
			/bin/bash -c "echo  -e '\033[33m$$TEST_RESULTS'"; \
		elif [ $$TEST_PERCENTAGE  -lt 100 ]; then \
			/bin/bash -c "echo  -e '\033[36m$$TEST_RESULTS'"; \
		else  \
			/bin/bash -c "echo  -e '\033[32m$$TEST_RESULTS'"; \
		fi ;\
	fi
	/bin/bash -c 'echo -n -e "\033[0m"'
endef

define prepare_input
	cp ./unittests/$(1).txt ./input.txt
	cp ./unittests/$(1).answers.txt ./answers.txt
endef

define perform_test
	$(call prepare_input,$(1))
	/bin/echo -n $(2)" input tests: "
	$(call test_input,1)
endef

define generate_answers
	echo "dummy" >  ./unittests/$(1).answers.txt
	$(call prepare_input,$(1)) &> /dev/null
	$(call test_input) &> /dev/null
	cp ./output.txt ./unittests/$(1).answers.txt
	/bin/echo "Output for "$(1)".txt tests generated."
	/bin/bash -c 'echo -n -e "\033[0m"'
endef

define merge_test
	cat ./unittests/$(1).txt >> ./input.txt
	cat ./unittests/$(1).answers.txt >> ./answers.txt
endef

.SILENT all:
	$(call backup_data)	
	
	# perform_test,INPUT_FILE_NAME_WOUT_EXTENSION,TEST_NAME
	
	$(call perform_test,noparam,"No param")
	$(call perform_test,lowercase,"Lower to upper")
	$(call perform_test,uppercase,"Upper to lower")
	$(call perform_test,mixedcase,"Mixed swap")
	$(call perform_test,numeric,"Numerics")
	$(call perform_test,toolong,"Cut to limit")
	$(call perform_test,tooshort,"Expand to limit")

	$(call restore_data)

generate:
	$(call backup_data)

	# generate_output,INPUT_FILE_NAME_WOUT_EXTENSION
	
	$(call generate_answers,noparam)
	$(call generate_answers,lowercase)
	$(call generate_answers,uppercase)
	$(call generate_answers,mixedcase)
	$(call generate_answers,numeric)
	$(call generate_answers,toolong)
	$(call generate_answers,tooshort)

	$(call restore_data)

merge:
	-rm ./input.txt 2>/dev/null
	-rm ./answers.txt 2>/dev/null

	$(call merge_test,noparam)
	$(call merge_test,lowercase)
	$(call merge_test,uppercase)
	$(call merge_test,mixedcase)
	$(call merge_test,toolong)
	$(call merge_test,tooshort)
