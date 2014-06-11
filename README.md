<h1>PyCCS (CKIP Chinese Segmentator)</h1>
<p> A Python API for CKIP Chinese Segmentator

<p>CKIP (Chinese Knowledge and Information Processing Group) provides a online Chinese segmentation tool (http://ckipsvr.iis.sinica.edu.tw/).<br>
</p>

<hr>
<h2>Usage</h2>
```
>>> from PyCCS import ckip
>>> result = ckip.seg('台灣大學語言學研究所')
>>> print result.text()
台灣/Nc 大學/Nc 語言學/Na 研究所/Nc 
>>> result.raw
[(u'\u53f0\u7063', u'Nc'),
 (u'\u5927\u5b78', u'Nc'),
 (u'\u8a9e\u8a00\u5b78', u'Na'),
 (u'\u7814\u7a76\u6240', u'Nc')]
```
<h2>Limitations</h2>
<strong>Input encoding should can only be CP950/BIG5</strong><br>
For example, words containing "堃" or "瑠" cannot be segmentated.
