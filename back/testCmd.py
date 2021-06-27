import os
import subprocess


# r=os.popen("java -jar ./JavaProject/SoftwareTesting-MeetHere/target/meethere-0.0.1-SNAPSHOT-fat-tests.jar com.meethere.testService.MessageServiceImplTest")
# text = r.read()

b=subprocess.run(" java -jar ./JavaProject/SoftwareTesting-MeetHere/target/meethere-0.0.1-SNAPSHOT-fat-tests.jar com.meethere.testService.MessageServiceImplTest")
textb=b.read()

print(textb)


