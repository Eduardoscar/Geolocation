node {
    def app
    stage('Clone') {
        checkout scm 
    }
    stage('Build') {
        app = docker.build("geocoding:latest")
    }
    
    
    stage('Deploy') {
        sh 'set'
        sh 'docker stop geocoding || true && docker rm geocoding || true'
        sh 'docker run -p 5000:5000 -d --rm --name geocoding MYSQL_IP" -e GOOGLE_MAPS_API_KEY="$GOOGLE_MAPS_API_KEY" geocoding:latest'
    }
}