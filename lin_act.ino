/*Sketch to ddrive Brushed DC-Motor in two directions*/

#define  IS_1  0
#define  IS_2  1
#define  IN_1  3
#define  IN_2  11
#define  INH_1 12
#define  INH_2 13

#define TCONST 50      //Delay Time between Steps
#define FULL_RANGE 271 // limit to limit 270 doesn't actuate the limit, 271 does. 
                       // I'm sure we can make it more accurate but this ought to work

int Motor_DC     = 0;    // actual DC
int Motor_DC_MAX = 120;   // 12 volt

int i = 0;

void setup() {

  // put your setup code here, to run once:
  pinMode(IN_1,OUTPUT);
  pinMode(IN_2,OUTPUT);
  pinMode(INH_1,OUTPUT);
  pinMode(INH_2,OUTPUT);
  
  reset_ports();
  
  digitalWrite(INH_1,1);
  digitalWrite(INH_2,1);
}

void drive_linear_actuator(int port, int distance)
{
  analogWrite( port , 255 );
  delay(TCONST * distance);
}


//Alle IOs zurücksetzen
void reset_ports()
{
  digitalWrite(IN_1,0);
  digitalWrite(IN_2,0);
}

void loop() {

 
  //Fade Motor in forward direction
  drive_linear_actuator(IN_2, FULL_RANGE);
  
  //Wait and Stop
  reset_ports();
  delay(1000);  //Wait for 1s
  
  //Fade Motor in backward direction
  drive_linear_actuator(IN_1, FULL_RANGE);
  
  //Wait and Stop
  reset_ports();
  delay(1000);  //Wait for 1s
  
}
