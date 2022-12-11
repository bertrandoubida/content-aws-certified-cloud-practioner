def lambda_handler(event, context):
    message = 'Salut {} {}! Tu es Magnifique!'.format(event['first_name'], event['last_name'])  

    #print to CloudWatch logs
    print(message)

    return { 
        'message' : message
    }   
