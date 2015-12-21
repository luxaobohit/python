#-*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import xml.etree.ElementTree as ET
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class SendResultEmail(object):
    def __init__(self, xml_dir):
        self.xml_dir = xml_dir
        self.__load_output_xml()

    def __percentage(self, succ, fail):
        try:
            numerator = float(succ)
            denominator = float(succ) + float(fail)
        except Exception as e:
            raise Exception(e)
        return '%.2f%%' % (numerator*100 / denominator)

    # load the output.xml
    def __load_output_xml(self):
        root = ET.parse(self.xml_dir).getroot()
        total_list = root.findall('./statistics/total/stat')
        tag_list = root.findall('./statistics/tag/stat')
        suite_list = root.findall('./statistics/suite/stat')
        re = ''
        for tag in suite_list:
            re += 'pass: %s, fail: %s, percentage: %s. Testsuite: %s \n'.decode('gbk').encode('utf-8') % (tag.attrib['pass'], tag.attrib['fail'], self.__percentage(tag.attrib['pass'], tag.attrib['fail']), tag.text)
        print re
        with open('C:\\Users\\10192928\\Desktop\\a.txt', 'w') as fo:
            fo.write(re)
        return total_list, tag_list, suite_list

    def __read_output_content(self):
        total_list, tag_list, suite_list = self.__load_output_xml()
        re = ''
        for tag in suite_list:
            re += 'pass: %s, fail: %s, percentage: %s. Testsuite: %s\n'.decode('gbk').encode('utf-8') % (tag.attrib['pass'], tag.attrib['fail'], self.__percentage(tag.attrib['pass'], tag.attrib['fail']), tag.text)
        return re

    def __read_output_subject(self):
        total_list, tag_list, suite_list = self.__load_output_xml()
        re = ''
        for tag in total_list:
            re += 'pass: %s, fail: %s, percentage: %s. Testsuite: %s '.decode('gbk').encode('utf-8') % (tag.attrib['pass'], tag.attrib['fail'], self.__percentage(tag.attrib['pass'], tag.attrib['fail']), tag.text)
        return re

    def __format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    def send_result(self):
        smtp_server = 'smtp.zte.com.cn'
        port = 25
        from_addr = 'lu.xiaobo@zte.com.cn'
        to_addr = ['lu.xiaobo@zte.com.cn',] # better to read from external file

        email_content = self.__read_output_content()
        email_header = self.__read_output_subject()

        msg = MIMEText(email_content, 'plain', 'utf-8')
        msg['From'] = 'lu.xiaobo@zte.com.cn'
        msg['To'] = 'lu.xiaobo@zte.com.cn'
        msg['Subject'] = Header(email_header, 'utf-8').encode()

        try:
            smtp = smtplib.SMTP(smtp_server, port)
            smtp.set_debuglevel(1)
            smtp.login(from_addr, password)
            smtp.sendmail(from_addr, to_addr, msg.as_string())
            smtp.quit()
            return True
        except Exception as e:
            raise Exception(e)
            return False


if __name__ == '__main__':
    sre = SendResultEmail('C:\\Users\\10192928\\AppData\\Local\\Temp\\RIDEpbk1m9.d\\output.xml')
    #sre.load_output_xml()
    sre.send_result()
