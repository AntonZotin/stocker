
# In this directory, run the following command to build this builder.
# $ gcloud builds submit . --config=cloudbuild.yaml

steps:
- name: 'gcr.io/cloud-builders/docker'
  args: ['build', '--tag=gcloud-slim', '--tag=gcr.io/$PROJECT_ID/gcloud-slim', '-f', 'Dockerfile.slim', '.']

# Simple sanity check: invoke the new gcloud container to confirm that it was
# built correctly.
- name: 'gcr.io/$PROJECT_ID/gcloud-slim'
  args: ['info']

# Confirm that auth is piped through correctly.
- name: 'gcr.io/$PROJECT_ID/gcloud-slim'
  args: ['builds', 'list']

images:
- 'gcr.io/$PROJECT_ID/gcloud-slim'

timeout: 1200s
