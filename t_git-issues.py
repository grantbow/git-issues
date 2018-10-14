# -*- coding: utf-8 -*-

import sys
import re
import os
import os.path
import shutil
import unittest
import gitshelve
import exceptions

try:
    from cStringIO import StringIO
except:
    from StringIO import StringIO

class t_Person(unittest.TestCase):
    def setUp(self):
        if os.name == 'nt':
            self.tmpdir = os.getenv('TEMP')
        else:
            self.tmpdir = '/tmp'
        try: gitshelve.git('branch', '-D', 'test')
        except: pass

    def tearDown(self):
        try: gitshelve.git('branch', '-D', 'test')
        except: pass


class t_Comment(unittest.TestCase):
    def setUp(self):
        if os.name == 'nt':
            self.tmpdir = os.getenv('TEMP')
        else:
            self.tmpdir = '/tmp'
        try: gitshelve.git('branch', '-D', 'test')
        except: pass

    def tearDown(self):
        try: gitshelve.git('branch', '-D', 'test')
        except: pass


class t_Issue(unittest.TestCase):
    def setUp(self):
        if os.name == 'nt':
            self.tmpdir = os.getenv('TEMP')
        else:
            self.tmpdir = '/tmp'
        try: gitshelve.git('branch', '-D', 'test')
        except: pass

    def tearDown(self):
        try: gitshelve.git('branch', '-D', 'test')
        except: pass


class t_IssueSet(unittest.TestCase):
    def setUp(self):
        if os.name == 'nt':
            self.tmpdir = os.getenv('TEMP')
        else:
            self.tmpdir = '/tmp'
        try: gitshelve.git('branch', '-D', 'test')
        except: pass

    def tearDown(self):
        try: gitshelve.git('branch', '-D', 'test')
        except: pass
#Person:
#Comment:
#Issue:
#IssueSet:
#XmlReader:
#XmlStringRipper:
#XmlListRipper:
#XmlDateTimeRipper:
#XmlPersonRipper:
#XmlIssueRipper:
#XmlIssueSetRipper:
#XmlRipper:
#XmlWriter:
#XmlStringBuilder:
#XmlListBuilder:
#XmlDateTimeBuilder:
#XmlPersonBuilder:
#XmlIssueBuilder:
#XmlCommentBuilder:
#XmlIssueSetBuilder:
#XmlBuilder:
#GitIssue(Issue):
#GitComment(Comment):
#xml_gitbook(gitshelve.gitbook):
#GitIssueSet(IssueSet):


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(t_gitshelve)

if __name__ == '__main__':
    unittest.main()
