rem msxsl.exe %xml% %xsl%  -o %out% -u '4.0' -t %param[ name="value"

rem basic working pattern=> msxsl.exe "ITGeneralist4 - Base.xml" "ITGeneralistWithJavaScript4-Base-SecurityAdmin.xslt" -o test.html

msxsl.exe "ITGeneralist4 - Base.xml" ITGeneralistWithJavaScript4.xslt -o index.html 

msxsl.exe "ITGeneralist4 - Base.xml" ITGeneralistWithJavaScript4-Base.xslt -o ITGeneralist4-Base.xml.html
msxsl.exe "ITGeneralist4 - Base.xml" ITGeneralistWithJavaScript4-Base-SecurityAdmin.xslt -o ITGeneralist4-Base-SecurityAdmin.xml.html

msxsl.exe "ITGeneralist4 - Base.xml" ITGeneralistWithJavaScript4-Base-Sales.xslt -o ITGeneralist4-Base-Sales.xml.html

msxsl.exe "ITGeneralist4 - Base.xml" XMLResume2Jobs.xslt -o jobs.csv

msxsl.exe "ITGeneralist4 - Base.xml" XMLResume2Item.xslt -o item.csv
  
