# AnomalyDetectionSwat2019

# Description

Secure Water Treatment (SWaT), launched on 18 Mar 2015 by Chief Defense Scientist Prof. Quek Tong Boon, is a water treatment testbed for research in cyber security. There are currently seven versions of the Secure Water Treatment Dataset called A1 A2 (2015), A3 (2017), A4 A5 (2019), A6 (2019) and A77 (2019) (2020). The testbed serves as a key asset for researchers in Singapore and abroad who are aiming at the design of secure CPS. The project task is to visualize summaries of the data stream(s) and develop an ML model to detect anomalies in the data set. In this project work we will use SWaT2019.Which is consisted of 4 hours collected data from different sensors and actuators the dataset was collected from 39 actuators and 38 sensors distributed in all the stages of the test bed.

Data Collection at Secure Water Treatment (SWaT) Testbed

20 July 2019

• Plant start time: 12:35 PM (GMT +8)
• Plant normal run without any attacks: 12:35 PM to 2:50 PM
• Six attacks, described below, were carried out between 3:08 PM to 4:16 PM
• Plant stop time: 4:35 PM

1. Attack on FIT401: Spoof value from 0.8 to 0.5
   Intent: To stop de-chlorination by switching off UV401
   Start time: 3:08:46 PM
   End time: 3:10:31 PM
2. Attack on LIT301: Spoof value from 835 to 1024
   Intent: To eventually lead to underflow in T301
   Start time: 3:15 PM
   End time: 3:19:32 PM
3. Attack on P601: Switch from OFF to ON
   Intent: To increase water in raw water tank
   Start time: 3:26:57 PM
   End time: 3:30:48 PM
4. Multi-point Attack: Switch from CLOSE to OPEN (MV201) and OFF to ON (P101)
   Intent: To overflow tank T301
   Start time: 3:38:50 PM
   End time: 3:46:20 PM
5. Attack on MV501: Switch from OPEN to CLOSE
   Intent: To drain water from RO
   Start time: 3:54 PM
   End time: 3:56 PM
6. Attack on P301: Switch from ON to OFF
   Intent: To halt stage 3 (UF process)
   Start time: 4:02:56 PM
   End time: 4:16:18 PM

# Relted Aricles

- [Anomaly Detection for a Water Treatment System
  Using Unsupervised Machine Learning](https://arxiv.org/pdf/1709.05342.pdf)\
   Comparsion between two methods: Deep
  Neural Networks (DNN) adapted to time series data generated
  by a CPS, and one-class Support Vector Machines (SVM).\
   These methods are evaluated against data from the Secure Water
  Treatment (SWaT) testbed, a scaled-down but fully operational
  raw water purification plant.

# Team members

- Óscar Cabrera Rodríguez
- Elshan Gadimov
- Haddad Philip
- Yazgan Pinar
- Joao Pinherio
