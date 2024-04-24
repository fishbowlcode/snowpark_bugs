#!/bin/bash

# Drop into the snowpark project, since the --project flag still doesnt work. Tracking here: https://github.com/snowflakedb/snowflake-cli/issues/906
cd langchain_demo/

# Build the snowpark project
printf "Building snowpark Project...\n\n"
snow snowpark build --pypi-download=yes --no-check-anaconda-for-pypi-deps --debug

# Deploy the snowpark project
printf "\nDeploying the snowpark project... "
snow snowpark deploy -x --account=$SNOWFLAKE_ACCOUNT --user=$SNOWFLAKE_USERNAME --database=$SNOWFLAKE_DATABASE --schema=$SNOWFLAKE_SCHEMA --replace --debug
printf "Harmonizer Project Deployed, Done.\n\n"
