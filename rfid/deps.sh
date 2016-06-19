sudo apt-get install python-dev
git clone https://github.com/lthiery/SPI-Py.git
cd SPI-Py
sudo python setup.py install

git clone https://github.com/ondryaso/pi-rc522.git
#cd pi-rc522

wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.35.tag.gz
tar -zxf bcm2835-1.35.tar.gz
cd bcm2835-1.35
./configure
sudo make install



