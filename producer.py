import time
import cv2
from kafka import KafkaProducer

#connect to kafka
producer = KafkaProducer(bootstrap_servers='localhost:9092')
#create a topic
topic = 'video_streaming'

def video_emitter(video):
    #Open the video
    video = cv2.VideoCapture(video)
    print('Emitting...')

    while(video.isOpened):
        success, image = video.read()
        if not success:
            break
        #convert the image png
        ret, jpeg = cv2.imencode('.png', image)
        #convert the image to bytes and send to kafka
        producer.send(topic, jpeg.tobytes())
        #To reduce CPU usage create sleep time of 0.2sec
        time.sleep(0.2);

    video.release()
    print('Done Emitting...')

if __name__ == '__main__':
    video_emitter('video.mp4')
