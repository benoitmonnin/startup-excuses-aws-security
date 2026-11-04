# AWS lab cleanup — preserve portfolio evidence, then stop charges

**WARNING: these actions are destructive.** Nothing should be deleted until screenshots, application source and configuration notes have been backed up and checked. No deletion has been performed by this starter.

AWS Region for the lab: **Europe (Paris) `eu-west-3`**.

## Prepare (before teardown)

- [ ] Check the GitHub evidence list: 25 screenshots, including `25-public-route-table-internet-gateway.png`.
- [ ] Save a clean copy of application code, README, architecture diagram, and any non-secret configuration notes.
- [ ] Confirm whether the database contains data you need. Decide whether a **final snapshot** is required. A retained final snapshot can incur storage charges until you remove it.
- [ ] Check the account's **Billing / Cost Explorer** and create or review a budget alert.

## Delete compute and database, after the lab is finished

- [ ] In **EC2 → Instances**, find `StartupExcuses-WebServer` and confirm the instance ID and region. Terminate only when you no longer need it; this cannot be reversed.
- [ ] In **RDS → Databases**, find `startupexcuses-db`; if deletion protection is on, disable it only for the intended deletion. Delete the DB instance. Explicitly choose whether to create a **final DB snapshot** and whether to retain automated backups.
- [ ] Verify the EC2 instance reaches `Terminated` and RDS reaches deletion completion. Do not assume stopping a resource ends every charge.

## Review retained resources (possible ongoing costs)

- [ ] **EC2 → Volumes:** delete leftover EBS volumes you no longer need.
- [ ] **EC2 → Snapshots / AMIs:** keep only deliberately required backups; snapshots can continue to be charged.
- [ ] **EC2 → Elastic IPs / Public IPv4:** release any allocated IP addresses no longer required.
- [ ] **RDS → Snapshots / Automated backups:** remove unneeded retained backups and final/manual snapshots when safe.
- [ ] **EC2 → Load balancers**, **VPC → NAT gateways**, and other region resources: remove *only if actually created and unused*. This lab does not claim a load balancer or NAT gateway was configured.
- [ ] Optionally remove unused lab-specific security groups, subnet groups, VPC subnets, route tables, IGW and VPC **after** deleting dependent resources. These typically aren't the primary charging resources, so prioritize EC2, RDS, storage and IPs.
- [ ] Recheck billing / Cost Explorer after AWS usage data updates. Check other Regions too if you ran additional labs.

## Notes

- Terminating EC2 can permanently remove the root EBS volume depending on its 'delete on termination' setting.
- RDS manual/final snapshots and retained automated backups can generate storage charges after the DB instance is deleted.
- A stopped EC2 instance may still have EBS and public IPv4-related costs, and a stopped RDS instance is not equivalent to full cleanup.
- Use the AWS Console to identify **your specific resources**; never copy a bulk deletion command or assume everything in the account belongs to this lab.

## AWS documentation

- RDS deletion: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DeleteInstance.html
- EC2 termination: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-ec2-instance-termination-works.html
- EC2 cleanup resources: https://repost.aws/knowledge-center/delete-terminate-ec2
