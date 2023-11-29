int x; 
int led=LED_BUILTIN;

void setup() { 

	Serial.begin(115200); 
	Serial.setTimeout(1); 
	pinMode(led, OUTPUT);
} 
void loop() { 
	while (!Serial.available()); 
	x = Serial.readString().toInt(); 
	if (x == 1) 
		{digitalWrite(led, HIGH);} 
	else if (x == 0) 
		{digitalWrite(led, LOW);}
	Serial.print(x + 1); 
} 

