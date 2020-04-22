# Data Analysis Extension for StopSpot Application Developed for C-TRAN
**Contributors:** Marcus Kwong, Evan Brunswick, Meghan Mueller-Cox, Phuong Pham

## Project Design

### Project Goal
* Filter the data for C-TRAN to identify problem locations
* Implement features that analyze and visualize the data for C-TRAN.
* Draw correlations between clusters of data that exist outside C-TRAN’s accepted range.

### Project Summary
The StopSpot project is one where we work with data that C-TRAN of Vancouver, Washington has given to us. We would like to use that data to draw some conclusions about how C-TRAN buses operate. We seek to be able to analyze the data that they have given to us and identify issues with the outlying data points and any possible causes for their existence. This information in regards to outlier data will be very beneficial for C-TRAN because it will help them discover possible needs for new stops, identify issues with existing routes, and reduce C-TRAN’s financial expenses by removing the need to send operators to locations that don't need to be checked/analyzed. We will be executing our project by building onto a pre-existing model and implementing a new filter for data selection, analyzing said data, and modeling features to assist with analysis of this new data set. The specific goals we wish to accomplish in this project is to create a proof of concept for heat map visualizations to better analyze the distance distributions in the stop data and create visualizations to analyze stop distance distributions by time of day using open source python based tools. To develop these tasks, we will create proofs of concept models using visualization tools in order to test the new features planned for the web application.

### Project Tasks:
[Task List](https://docs.google.com/spreadsheets/d/1yQvNPGIrTbJYmvEP3dhnun-5BOvOYidJOPh_eNfEbGQ/edit#gid=0)

### Roles:
* Marcus:
  * Project Founder, Project Manager
  * Heat map visualizations: research tools and contribute to proof of concept
  * Manage integration of work into existing Web Application
* Evan:
  * Data cleaning
  * Data filtration
  * Contribute to visualizations efforts
* Meghan:
  * Time based visualizations effort: researching visualization options and tools
  * Collaboration on proof on concepts for time based visualizations
  * Investigate options for integrating time based visualizations into existing web application, assist with any integration effort
* Phuong:
  * Assist Marcus with researching on different tools for visualizations of the heat map
  * Implementing the visualization tools for the heat map feature
  * From the heat map, analyze the clustering of stop instances to perform variance analysis on the stop events
  * Help Meghan with time-based distribution of the problem stops
  * Help with anything else the team needs to accomplish our goals
 

### Presentations (located on PSU Google Drive, requires permission to access):
[Topic Presentation](https://drive.google.com/open?id=1anYrv2r58wyaZ7Tbpuwg6vwYmCM_qrfZgg-mYJmZlY8)

[Final Presentation](https://drive.google.com/open?id=15yqhLlrnHHhHzbIgviLQMe7k3bA1VMER9613zC2vkRw)

### Ancilary Documents Developed as a part of the CS410/510 Analysis and Data Science Course
* Code pertaining to this course see the commit history from 2/23/2020-3/15/2020
* See the CS410_510 Directory, contains Jupyter notes books proof of concepts and the videos linked to in the
  Final Presenation in case there is trouble with access
