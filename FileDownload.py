from ftplib import FTP
def downloadfile(ano):

    ftp = FTP('cddis.gsfc.nasa.gov')   # connect to host, default port
    ftp.login()               # user anonymous, passwd anonymous@
    ftp.cwd('/pub/gps/products/mgex/dcb/2018/')     #change the directory on the ftp link

    ###### create a variable to replace the year, and then reuse this variable to search in the files in ftp
    lista=ftp.retrlines('LIST')     # list directory contents
    filename=('CAS0MGXRAP_{}0000_01D_01D_DCB.BSX.gz').format(ano) #recives the name of the file, and format the filename variable

    localfile=open(filename,'wb')

    ftp.retrbinary('RETR '+filename,localfile.write,1024)

    ftp.quit()

    localfile.close()
    return filename