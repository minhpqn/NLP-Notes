# http://takegue.hatenablog.com/entry/2015/01/25/045341

#Mecab implements for Python using subprocess
class MeCab():

    def __init__(self, opts=['-Owakati']):
        self.opts = opts
        self._process = subprocess.Popen(
            list(itt.chain(['mecab'], opts)),
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            universal_newlines =True,
        )

    def parse(self, iterable):
        for line in iterable:
            self._process.stdin.write(line+'\n')
            output = self._process.stdout.readline()
            yield output.strip().split()

parser = MeCab()
print next(parser.parse(['すもももももももものうち']))
# >>> ['すもも', 'も', 'もも', 'も', 'もも', 'の', 'うち']
