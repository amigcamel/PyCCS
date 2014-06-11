<h1>PyCCS (CKIP Chinese Segmentator)</h1>
<p> A Python API for CKIP Chinese Segmentator

<p>CKIP (Chinese Knowledge and Information Processing Group) provides a online Chinese segmentation tool (http://ckipsvr.iis.sinica.edu.tw/).<br>
</p>

<hr>
<h2>Usage</h2>
```
from PyCCS import ckip
result = ckip.seg('台灣大學語言學研究所')
print result.text()
```
