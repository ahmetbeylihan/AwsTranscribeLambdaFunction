import boto3

def lambda_handler(event, context):
    s3bucket = 'audio-output-storage'
    s3object = 'output.mp3'

    s3Path = "s3://" + s3bucket + "/" + s3object
    jobName = "output"

    client = boto3.client('transcribe')

    response = client.start_transcription_job(
        TranscriptionJobName=jobName,
        LanguageCode='en-US',
        MediaFormat='mp3',
        Media={
            'MediaFileUri': s3Path
        },
        OutputBucketName="audio-output-storage"
    )
