def lambda_handler(event, context):
    message = 'Salut {} {}! Tu es Magnifique!'.format(event['Prénom'], event['Nom'])  

    #print to CloudWatch logs
    print(message)

    return { 
        'message' : message
    }   
