#!/bin/bash
#usage sh automation.sh  nyc.trim.liwc(data) Words_all_sick.txt(sentiment dicitionary)
#output: nyc.trim.liwc.append.sentiment( Data with calculated sentiment values appended)
#        trainingSet.dat( features set for the training data)
#	 testSet.dat( features set for the test data set)	
#	 model_file, prediction_file ( generatd by SVMlight for predictted setiment values
#	 statfile_t_sqrt.dat ( tab separated file for R analysis)

if [ "$#" -ne 2 ]; then
   echo "Usage sh automation.sh  nyc.trim.liwc(data) Seniment_dictionary(e.g. Words_all_sick.txt)"
fi
echo "Execution Started......"


# segreagate the data into training and test data set 
python emoticons_n.py $1
#gzip $1
python emoticons_p.py $1.res
mv $1.res.positive $1.positive

#feature set generation
python makeWordList.py $2 $1.negative $1.positive
mv test_WORDS_all-sick.txt_normal.dat trainingSet.dat

python makeWordList.py $2 $1.res.final
mv test_WORDS_all-sick.txt_normal.dat testSet.dat

#training and classifying using the SVMlight
./svm_learn -z r trainingSet.dat model_file
./svm_classify testSet.dat model_file prediction_file

#appends the calculated sentiment values to the json file and generates the tab separated file
python StatAppend.py $1.res.final prediction_file
mv $1.res.final.append.sentiment $1.append.sentiment

python StatDatagen_t.py $1.res.final prediction_file 
