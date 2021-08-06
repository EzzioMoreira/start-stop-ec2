# Start and stop ec2
## _AWS Lambda to stop or start EC2 instances based on the instance tags._

First function will try to filter for EC2 instances that contain a tag named `Scheduled` which is set to `True`
 If that condition is meet function will compare current time (H:M) to a value of the additional tags which defines the trigger `ScheduleStop` or `ScheduleStart`.
 Value of the `ScheduleStop` or `ScheduleStart` must be in the following format `H:M` - example `09:00`
 
 In order to trigger this function make sure to setup CloudWatch event which will be executed every minute. 
 Following Lambda Function needs a role with permission to start and stop EC2 instances and writhe to CloudWatch logs.

- Scheduled     : True
- ScheduleStart : 06:00
- ScheduleStop  : 18:00
