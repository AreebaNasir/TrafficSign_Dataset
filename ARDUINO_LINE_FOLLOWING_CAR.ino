

//ARDUINO LINE FOLLOWING CAR//
// YOU HAVE TO INSTALL THE AFMOTOR LIBRARY BEFORE UPLOAD THE CODE//
// GO TO SKETCH >> INCLUDE LIBRARY >> ADD .ZIP LIBRARY >> SELECT AF MOTOR ZIP FILE //
 
//including the libraries
#include <AFMotor.h>

//defining pins and variables
#define left A0
#define right A1

//defining motors
AF_DCMotor motor1(1, MOTOR12_1KHZ); 
AF_DCMotor motor2(2, MOTOR12_1KHZ);
AF_DCMotor motor3(3, MOTOR34_1KHZ);
AF_DCMotor motor4(4, MOTOR34_1KHZ);



void setup() {
  //declaring pin types
  pinMode(left,INPUT);
  pinMode(right,INPUT);
  //begin serial communication
  Serial.begin(9600);
  
}

void loop(){
  //printing values of the sensors to the serial monitor
  Serial.println(digitalRead(left));
  
  Serial.println(digitalRead(right));

  //line detected by both
  if(digitalRead(left)==0 && digitalRead(right)==0){
    //Forward
    motor1.run(BACKWARD);
    motor1.setSpeed(70);
    motor2.run(BACKWARD);
    motor2.setSpeed(85);
    motor3.run(BACKWARD);
    motor3.setSpeed(85);
    motor4.run(BACKWARD);
    motor4.setSpeed(70);
  }
  //line detected by left sensor
  else if(digitalRead(left)==0 && !digitalRead(right)==0){
    //turn left
    motor1.run(FORWARD);
    motor1.setSpeed(120);
    motor2.run(FORWARD);
    motor2.setSpeed(135);
    motor3.run(BACKWARD);
    motor3.setSpeed(135);
    motor4.run(BACKWARD);
    motor4.setSpeed(120);
    
  }
  //line detected by right sensor
  else if(!digitalRead(left)==0 && digitalRead(right)==0){
    //turn right
    motor1.run(BACKWARD);
    motor1.setSpeed(120);
    motor2.run(BACKWARD);
    motor2.setSpeed(135);
    motor3.run(FORWARD);
    motor3.setSpeed(135);
    motor4.run(FORWARD);
    motor4.setSpeed(120);
   
  }
  //line detected by none
  else if(!digitalRead(left)==0 && !digitalRead(right)==0){
    //stop
    motor1.run(RELEASE);
    motor1.setSpeed(0);
    motor2.run(RELEASE);
    motor2.setSpeed(0);
    motor3.run(RELEASE);
    motor3.setSpeed(0);
    motor4.run(RELEASE);
    motor4.setSpeed(0);
   
  }
  
}




// else if(RIGHT_SENSOR>36 && LEFT_SENSOR<36) //LEFT
// {
//            digitalWrite(Motor11, LOW);
//            digitalWrite(Motor12, HIGH);
//            digitalWrite(Motor21, HIGH);
//            digitalWrite(Motor22, LOW);
//            analogWrite(PWMmotor1, valuePWM2);
//            analogWrite(PWMmotor2, valuePWM2);
//}
//
//else if(RIGHT_SENSOR<36 && LEFT_SENSOR>35) //RIGHT
// {
//              digitalWrite(Motor11, HIGH);
//              digitalWrite(Motor12, LOW);
//              digitalWrite(Motor21, LOW);
//              digitalWrite(Motor22, HIGH);
//              analogWrite(PWMmotor1, valuePWM2);
//              analogWrite(PWMmotor2, valuePWM2);
//}
//
//else if(RIGHT_SENSOR>35 && LEFT_SENSOR>35) //BACK
//{
//              digitalWrite(Motor11, LOW);
//              digitalWrite(Motor12, LOW);
//              digitalWrite(Motor21, LOW);
//              digitalWrite(Motor22, LOW);
//              delay(10000);
// }
//}
