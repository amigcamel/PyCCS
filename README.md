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
All html-like tags will be segmentated normally.<br>
(At <a href="http://sunlight.iis.sinica.edu.tw/uwextract/demo.htm">CKIP Online Demo</a>, if you input strings containing html-like tag, the results might be weird)
```
>>> print ckip.seg('<h1>這是html tag</h1>').text()
<h1>/FW 這/Nep 是/SHI html/FW tag</h1>/FW 
```
<h2>Limitations</h2>
<strong>Input encoding should can only be CP950/BIG5</strong><br>
For example, words containing "堃" or "瑠" cannot be segmentated.
