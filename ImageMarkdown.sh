
# get the file directory
INSTALL_DIR=$(dirname $0)
cd $INSTALL_DIR

# adding lib dir to PYHTONPATH
export PYTHONPATH=$INSTALL_DIR/lib/:$PYTHONPATH


python src/main.py
#python src/test_exif.py
#python src/test_configParser.py
