Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> const int pinA = 2;
... const int pinB = 3;
... 
... int lastStateA;
... int displacement = 0;
... 
... void setup() {
...   pinMode(pinA, INPUT);
...   pinMode(pinB, INPUT);
...   Serial.begin(9600);
...   lastStateA = digitalRead(pinA);
... }
... 
... void loop() {
...   int currentStateA = digitalRead(pinA);
...   if (currentStateA != lastStateA) {
...     if (digitalRead(pinB) != currentStateA) {
...       displacement++;
...       Serial.println("+1");
...     } else {
...       displacement--;
...       Serial.println("-1");
...     }
...   }
...   lastStateA = currentStateA;
... }
