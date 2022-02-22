pipeline
{
    agent any
    stages{

        stage('bulid and publish Docker image'){
            steps{
                build 'Project-z'
            }  
        }
        stage('Deploy on K8s'){
            steps{
                sh "kubectl apply -f pro-deployment.yaml"
                // sshagent(['K8s-rsa']) {
                //     sh "scp -o StrictHostKeyChecking=no pro-deployment.yaml BALAJISTARK@172.17.0.5:/users/BALAJISTARK"
                //     script{
                //         try{
                //             sh "ssh BALAJISTARK@172.17.0.5 kubectl apply -f ."
                //         }catch(error){
                //             sh "ssh BALAJISTARK@172.17.0.5 kubectl create -f ."
                //         }
                        
                //     }
    
                // }
                
            }
        }
    }

}
