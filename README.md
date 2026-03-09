# Project Structure
```
aws-data-pipeline-starter/
│
├── infrastructure/                # Infrastructure as code
│   ├── main_stack.yaml            # Root stack including all other stacks
│   ├── iam.yaml                   # Roles and permissions
│   ├── redshift.yaml              # Redshift cluster / tables
│   ├── s3.yaml                    # S3 buckets
│   └── lambda.yaml                # Lambda setup + triggers
│   └── vpc.yaml                   # For Isolated Network env in AWS
├── lambdas/                       # Lambda handlers (entrypoints)
│   ├── ingest_handler.py          # API → S3
│   └── process_handler.py         # S3 → transform → Redshift
│
├── logs/
│   └── log_file
│
├── src/                           # Reusable logic
│   ├── __pycache__/
│   ├── __init__.py                # makes src a package
│   ├── api_fetcher.py             # API fetch logic
│   ├── config.py                  # constants or env var helpers
│   ├── logging_config.py          # logging setup
│   ├── redshift_writer.py         # Redshift COPY logic
│   ├── s3_reader.py               # reads S3 objects
│   ├── s3_writer.py               # writes raw or transformed data to S3
│   └── transformer.py             # pure transform logic
│
├── .env
├── .gitignore
├── architecture.txt
├── README.md
└── requirements.txt               # Python dependencies
```
main_stack orchestrator
 ├── vpc_stack
 ├── iam_stack
 ├── s3_stack
 ├── lambda_stack (uses VPC outputs)
 └── redshift_stack (uses VPC outputs)

 VpcId Ouputs
PrivateSubnetIds
PublicSubnetIds
LambdaSecurityGroup
RedshiftSecurityGroup