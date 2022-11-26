node {
    def app
    stage('Clone') {
        checkout scm 
    }
    stage('Build') {
        app = docker.build("Geocoding:latest")
    }
    stage('Test') {
        withPythonEnv('python3'){
            sh 'pytest --template=html/index.html --report=informe.html'
        }

    stage('Publish Unit Test results report') {
            steps {
                echo 'Report'
                publishHTML([allowMissing: false, alwaysLinkToLastBuild: true, keepAll: false, reportDir: 'target/site/jacoco/', reportFiles: 'informe.html', reportName: 'jacaco report', reportTitles: ''])

             }
        }
    }
    stage('Deploy') {
        sh 'set'
        sh 'docker stop Geocoding || true && docker rm Geocoding || true'
        sh 'docker run -p 5000:5000 -d --rm --name Geocoding MYSQL_IP" -e GOOGLE_MAPS_API_KEY="$GOOGLE_MAPS_API_KEY" Geocoding:latest'
    }
}