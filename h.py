#print("hello")
from deepface import DeepFace
#co them phat trien them giao dien
import pandas as pd
print("chào bạn đã đến với nhận diện khuôn mặt")
print("Bạn vui lòng lựa chọn để thực hiện chương trình")
print("--------------------------------------------")
print("nhấn 1 ---> tiếp tục")
print("Nhấn 1 số bất kì để thoát")
print("--------------------------------------------")
a = int(input("Lựa chọn là: "))
if ((a-1)==0): 
	print("START")
	print("--------------------------------------------------------------------------------------------")
else:
	print("EXIT")
	quit()
pd.options.display.max_colwidth =100
# khúc này là nó sử dụng các giao diện he
recognition = ['VGG_Face', 'Facenet', 'Facenet512', 'openface', 'DeepFace', 'DeepID','ArcFace', 'Dlib']
detection = ['cd cdopencv', 'ssd', 'dlib','mtcnn', 'retinaface']

def face_recognition():
	# điều chỉnh về thời gian và đường dẫn tới data cần sử dụng
	# db_path ='data' là đường dẫn, có thể dùng tương đối hoặc tuyệt đối cái nào phù hợp tình huống thì mình áp dụng  

	info = DeepFace.find(img_path ='messi.jpg', db_path ='data',model_name = recognition[1], detector_backend =detector[4])
	#C:/Users/Admin/AI/data
	print(info)
def face_reg_on_camera():
	#mau: DeepFace.stream(db_path = "C:/User/Sefik/Desktop/database")
	#time_threshold: thời gian mấy giấy để quét
	DeepFace.stream(db_path ='data',)#enable_face_analysis = False, time_threshold =1, frame_threshold =1)
	#, enable_face_analysis = False, time_threshold =1, fram_threshold =1)
# cái camera cho phép sử dụng 
face_reg_on_camera()


