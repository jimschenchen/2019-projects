from jpype import *
import os

#ָ��jar��λ��
jarpath = os.path.join(os.path.abspath('.'), '/EngStudy/')
#����JVM����ָ��jar��λ��
jpype.startJVM(jpype.getDefaultJVMPath(), "-Djava.ext.dirs=%s" % jarpath)
#����java�����е���.·��Ӧ������Ŀ�е�package��·��
javaClass = jpype.JClass('cilin.CiLin')
#��һ�����Ǿ���ִ�����еĺ�����
javaInstance = javaClass.calcWordsSimilarity(u"����", u"����")
print(javaInstance)
jpype.shutdownJVM()
