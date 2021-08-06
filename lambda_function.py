import boto3
import time

#define boto3 the connection
ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    
    # Get current time in format H:M
    current_time = time.strftime("%H:%M")
    
    # Find all the instances that are tagged with Scheduled:True
    filters = [{
            'Name': 'tag:Scheduled',
            'Values': ['True']
        }
    ]

    # Search all the instances which contains scheduled filter 
    instances = ec2.instances.filter(Filters=filters)

    stopInstances = []   
    startInstances = []   

    # Locate all instances that are tagged to start or stop.
    for instance in instances:
            
        for tag in instance.tags:

            if tag['Key'] == 'ScheduleStop':

                if tag['Value'] == current_time:

                    stopInstances.append(instance.id)

                    pass

                pass

            if tag['Key'] == 'ScheduleStart':

                if tag['Value'] == current_time:

                    startInstances.append(instance.id)

                    pass

                pass

            pass

        pass
    
    print current_time
    
    # shut down all instances tagged to stop. 
    if len(stopInstances) > 0:
        # perform the shutdown
        stop = ec2.instances.filter(InstanceIds=stopInstances).stop()
        print stop
    else:
        print "No instances to shutdown."

    # start instances tagged to stop. 
    if len(startInstances) > 0:
        # perform the start
        start = ec2.instances.filter(InstanceIds=startInstances).start()
        print start
    else:
        print "No instances to start."
