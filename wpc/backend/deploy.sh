BUCKET_NAME="${BUCKET_NAME:-200532}"
FUNTION_NAME="${FUNCTION_NAME:-200532-wpc-5_place-order}"


rm lambda.zip || true

zip -r lambda.zip ./* --exclude 'deploy.sh' --exclude 'lambda.zip'

aws s3 cp lambda.zip s3://${BUCKET_NAME}/code?${FUNCTION_NAME}/lambda.zip

aws lambda update-function-code --function-name ${FUNCTION_NAME} --s3-bucket ${BUCKET_NAME}
--s3-key code/${FUNCTION_NAME}/lambda.zip --publish

echo "Yeah deploy is done"