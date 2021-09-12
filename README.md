# TechTrends
TechTrends is an online website used as a news sharing platform, that enables consumers to access the latest news within the cloud-native ecosystem. In addition to accessing the available articles, readers are able to create new media articles and share them with the wider community. In this project, you are taking the role of a platform engineer with the main role to package and deploy the application to a Kubernetes platform. Throughout this project, you have used Docker to package the application, and automated the Continuous Integration process with GitHub Actions. For the release process, you have used Kubernetes declarative manifests, which were templated using Helm. To automated the Continuous Delivery process, you have used ArgoCD.
# How to run this application?
   1. Clone the repository using the command:
```
git clone https://github.com/imran-mirza79/techtrends-project.git
```
   2. In the project directory, run the commands to initilize the database and run the python file. (Make sure you have python installed. All these files can be found in the techtrends directory)
      * To initilize the database use the command:
      ```python
      python init_db.py 
      ```
      * To start the application, use the command:
      ```python
      python app.py
      ```
  3. Open ```localhost:3111``` on your browser. You Should view a screen similar to this :-
  ![image](https://user-images.githubusercontent.com/62472000/132976460-f9268d02-0d1e-4e4e-bcad-fc200d715dbe.png)
