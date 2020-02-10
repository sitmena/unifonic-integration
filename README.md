# Getting started

## Introduction

Send SMS messages using Unifonic Messaging API. Get your dedicated Universal number, and start sending messages today.

Unifonic NextGen Restful and HTTP **API's** uses The basic Authentication protocol. All request and response bodies are formatted in JSON.


## Get an account
To start using  the API you need to send an email to Unifonic to create Appsid for you.

## Base URL
All URLs referenced in the documentation have the following base:

**basic.unifonic.com**

## Usage

`from unifonicnextgen.unifonicnextgen_client import UnifonicnextgenClient`
`from unifonicnextgen.exceptions.api_exception import APIException`

`client = UnifonicnextgenClient(UNIFONIC_USER, UNIFONIC_PASSWORD)`

`try:
   sender_controller = client.rest
   sender_controller.create_send_message(UNIFONIC_APP_SID,
                                         UNIFONIC_SENDER_ID,
                                         'Your Message',
                                         recipient_phone_number)
 except APIException as error_message:
     print(error_message)
     logger.error(error_message)`
