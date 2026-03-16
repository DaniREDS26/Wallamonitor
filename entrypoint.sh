#!/bin/bash
set -e

cat > /app/config.yaml <<EOF
telegram_channel: "${TELEGRAM_CHANNEL}"
telegram_token: "${TELEGRAM_TOKEN}"
EOF
echo "${ARGS_JSON}" > /app/args.json
exec "$@"
