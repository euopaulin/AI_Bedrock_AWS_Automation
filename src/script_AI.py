import boto3
import json
import os
import requests
import time
import logging

client = boto3.client('bedrock-runtime', region_name='us-east-1')