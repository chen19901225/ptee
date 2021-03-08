ptee
=============================================

something like `tee` but support rotate logs




Usage
-------------------------------------------------


* save to path


   ptee --path=/tmp/log/one.log

* set backup count

   ptee --path=/tmp/log/one.log --backup=7

 set file size

   ptee --path=/tmp/log/one.log --max_byte=50m

* with debug

   ptee --path=/tmp/log/one.log --debug=1