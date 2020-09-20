#include <Wire.h>  // Wire library - used for I2C communication
int ADXL345 = 0x53; // The ADXL345 sensor I2C address
float X_out, Y_out, Z_out;  // Outputs
float x, y, z;
void setup() {
  Serial.begin(9600); // Initiate serial communication for printing the results on the Serial monitor
  Serial1.begin(57600);  // open internal serial connection to MT7688AN
  
  Wire.begin(); // Initiate the Wire library
  // Set ADXL345 in measuring mode
  Wire.beginTransmission(ADXL345); // Start communicating with the device
  Wire.write(0x2D); // Access/ talk to POWER_CTL Register - 0x2D
  // Enable measurement
  Wire.write(8); // (8dec -> 0000 1000 binary) Bit D3 High for measuring enable
  Wire.endTransmission();
  delay(10);
}
void loop() {
  // === Read acceleromter data === //
  Wire.beginTransmission(ADXL345);
  Wire.write(0x32); // Start with register 0x32 (ACCEL_XOUT_H)
  Wire.endTransmission(false);
  Wire.requestFrom(ADXL345, 6, true); // Read 6 registers total, each axis value is stored in 2 registers

 
  X_out = ( Wire.read() | Wire.read() << 8); // X-axis value
  x = X_out / 256; //For a range of +-2g, we need to divide the raw values by 256, according to the datasheet
  Y_out = ( Wire.read() | Wire.read() << 8); // Y-axis value
  y = Y_out / 256;
  Z_out = ( Wire.read() | Wire.read() << 8); // Z-axis value
  z = Z_out / 256;
  // === END of Reading acceleromter data === //
  Serial.print(x);
  Serial.print(",");
  Serial.print(y);
  Serial.print(",");
  Serial.print(z);
  Serial.println();

  Serial1.print(x);
  Serial1.print(",");
  Serial1.print(y);
  Serial1.print(",");
  Serial1.print(z);
  Serial1.print(",end\n");
  delay(500);
}
