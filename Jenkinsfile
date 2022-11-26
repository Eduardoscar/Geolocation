node {
    def app
    stage('Clone') {
        checkout scm 
    }
    stage('Build') {
        app = docker.build("geocoding:latest")
    }
    stage('Publish Unit Test results report') {
            steps {
                echo 'Report'
                publishHTML([allowMissing: false, alwaysLinkToLastBuild: true, keepAll: false, reportDir: 'target/site/jacoco/', reportFiles: 'informe.html', reportName: 'jacaco report', reportTitles: ''])

             }
        }
    
    stage('Deploy') {
        sh 'set'
        sh 'docker stop geocoding || true && docker rm geocoding || true'
        sh 'docker run -p 5000:5000 -d --rm --name geocoding MYSQL_IP" -e GOOGLE_MAPS_API_KEY="$GOOGLE_MAPS_API_KEY" geocoding:latest'
    }
}