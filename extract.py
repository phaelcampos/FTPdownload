import gzip
import shutil
import FileDownload

ano=str(input("type the year and the date"))
file=FileDownload.downloadfile(ano)

with open(file[:-3], 'wb') as f_out, gzip.open(file, 'r') as f_in:   #copy the file from the zip file to a text file
  shutil.copyfileobj(f_in, f_out)
