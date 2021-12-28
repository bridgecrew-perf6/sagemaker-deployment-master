def predict_fn(input_data, model):
    print('Inferring sentiment of input data.')

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    if model.word_dict is None:
        raise Exception('Model has not been loaded properly, no word_dict.')
    
    # TODO: Process input_data so that it is ready to be sent to our model.
    #       You should produce two variables:
    #         data_X   - A sequence of length 500 which represents the converted review
    #         data_len - The length of the review

    data_X = None
    data_len = None
    test_data_raw = review_to_words(input_data)
    #NOTE embed the convert_and_pad_data in here....
#    data_X = []
#    data_len = []
#    print('print test data raw type:',type(test_data_raw))
#    print('print test data raw len:',len(test_data_raw))
# NOTE 12/28/2021 KAE: based on the above prints in the log, the test_data_raw is a single sentiment, so 
#   we don't need to parse it as we did below in the convert_and_pad_data function. we can deal with it one at a time..
#    for sentence in test_data_raw:
#        print('print sentence type:',type(sentence))
#        print('print sentence len:',len(sentence))
# 
# NOTE 12/28/2021 KAE: so now the question is do we append the output to a list or just set our values equal to those values...
    converted, leng = convert_and_pad(model.word_dict, test_data_raw)       
    data_X = converted
    data_len = leng
#    data_X.append(converted)
#    data_len.append(leng)
#    data_X, data_len = convert_and_pad_data(model.word_dict, [test_data_raw])

    # Using data_X and data_len we construct an appropriate input tensor. Remember
    # that our model expects input data of the form 'len, review[500]'.
    data_pack = np.hstack((data_len, data_X))
    data_pack = data_pack.reshape(1, -1)
    
    data = torch.from_numpy(data_pack)
    data = data.to(device)

    # Make sure to put the model into evaluation mode
    model.eval()

    # TODO: Compute the result of applying the model to the input data. The variable `result` should
    #       be a numpy array which contains a single integer which is either 1 or 0

#    result = None
#    print('print data_X type:',type(data_X))
#    print('print data_X len:',len(data_X))
#    print('print datalen:',data_len)
#    print('print data_pack type:',type(data_pack))
#    print('print data_pack len:',len(data_pack))
#    print('print data type:',type(data))
#    print('print data len:',len(data))
    result_raw = model(data)
    #NOTE 12/28/2021 KAE: key discovery is that the model is just an integer(?) of 1 or 0 (NO LEN), so just print result
#    print('print result_raw type:',type(result_raw))
    print('print result_raw:',result_raw)
#    print(result_raw)
#    print(np.array(result_raw[0]))
#    predictor.predict(test_data)
    result = None
    # NOTE 12/28/2021 KAE: as above, scaler integer not iterable
#    result = np.array(result_raw[0])
# NOTE 12/28/2021 KAE: got below error in log, followed their directions and seemed to work
#RuntimeError: Can't call numpy() on Variable that requires grad. Use var.detach().numpy() instead.
#    result = np.array(result_raw)
    result = result_raw.detach().numpy()
#    print('print result type:',type(result))
#    print('print result:',result)
#    print('print result len:',len(result))

    return result
