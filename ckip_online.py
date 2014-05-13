#-*-coding:utf-8-*-
import urllib, urllib2, re

def ckipSeg(text):
	url_tar = 'http://sunlight.iis.sinica.edu.tw/cgi-bin/text.cgi'

	opener = urllib2.build_opener()
	postdata = urllib.urlencode({
		'query':text.decode('utf-8').encode('cp950'),
		'Submit':u'送出'.encode('cp950')
		})

	res = opener.open(url_tar, postdata).read()
	pat = re.compile("URL=\'/uwextract/pool/(\d*?).html\'")
	num = pat.search(res).group(1)

	url_fin = 'http://sunlight.iis.sinica.edu.tw/uwextract/show.php?id=%s&type=tag' % num

	seg = urllib2.urlopen(url_fin).read()
	break_sign = '-'*130

	seg_pat = re.compile('<pre>(.*?)</pre>', re.DOTALL)
	seg_clean = seg_pat.search(seg).group(1)
	seg_clean = seg_clean.replace(break_sign, '')
	seg_clean = seg_clean.decode('cp950', 'ignore')
	seg_clean = seg_clean.strip('\n')
	fs = u'\u3000' # fullwidth space
	seg_clean = seg_clean.strip(fs)
	seg_fin = seg_clean.split(fs)
	seg_fin_pat = re.compile('(.*?)\((\w*?)\)')
	con = []
	for i in seg_fin:
		o = seg_fin_pat.search(i)
		con.append((o.group(1), o.group(2)))
	return con







