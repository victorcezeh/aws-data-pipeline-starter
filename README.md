aws-data-pipeline-starter/
│
├── infra/                         # Infrastructure as code
│   ├── s3.yaml                     # S3 buckets
│   ├── lambda.yaml                 # Lambda setup + triggers
│   ├── redshift.yaml               # Redshift cluster / tables
│   ├── iam.yaml                    # Roles and permissions
│   └── main_stack.yaml             # Root stack including all other stacks
│
├── lambdas/                        # Lambda handlers (entrypoints)
│   ├── ingest_handler.py           # API → S3
│   └── process_handler.py          # S3 → transform → Redshift
│
├── src/                            # Reusable logic
│   ├── __init__.py                 # makes src a package
│   ├── api_fetcher.py              # API fetch logic
│   ├── s3_writer.py                # writes raw or transformed data to S3
│   ├── s3_reader.py                # reads S3 objects
│   ├── transformer.py              # pure transform logic
│   ├── redshift_writer.py          # Redshift COPY logic
│   ├── config.py                   # constants or env var helpers
│   └── logging_config.py           # logging setup
│
└── requirements.txt                # Python dependencies