f = open("index.html",'w',encoding='utf-8')
HTML_INDEX="""
<?xml version=\"1.0\" encoding=\"UTF-8\" ?>
<!DOCTYPE html>
<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"fr\" lang=\"fr\" dir=\"ltr\">
<style>
   table, th, td {
   border:1px solid black;
   }
</style>
<head>
<title> Mon titre </title>
</head>
<body>
 Bonjour HTML
</body>
</html>"""
f.write(HTML_INDEX)
f.close
