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
All html-like tags will be segmentated normally.
```
>>> print ckip.seg('html的tag(像是<h1>、<br>或<font>等等...)在原來ckip的線上展示中會出變的很奇怪，但是這個api可以解決這個問題！').text()
html/FW 的/DE tag/FW (/PARENTHESISCATEGORY 像是/SHI <h1>/FW 、/PAUSECATEGORY <br>/FW 或/Caa <font>/FW 等等/Cab ‧/PERIODCATEGORY ‧/PERIODCATEGORY ‧/PERIODCATEGORY )/PARENTHESISCATEGORY 在/P 原來/A ckip/FW 的/DE 線上/Nc 展示/VC 中會/Nc 出變/Na 的/DE 很/Dfa 奇怪/VK ，/COMMACATEGORY 但是/Cbb 這/Nep 個/Nf api/FW 可以/D 解決/VC 這/Nep 個/Nf 問題/Na ！/EXCLAMATIONCATEGORY 
```
<h2>Limitations</h2>
<strong>Input encoding should can only be CP950/BIG5</strong><br>
For example, words containing "堃" or "瑠" cannot be segmentated.
