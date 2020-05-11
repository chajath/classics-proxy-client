# classics_proxy_client.DefaultApi

All URIs are relative to *https://snappy-frame-253402.appspot.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**itkc_all_text_meta**](DefaultApi.md#itkc_all_text_meta) | **GET** /corpora/itkc/{seriesId}/all_text_meta/{dataId} | 
[**itkc_corpora**](DefaultApi.md#itkc_corpora) | **GET** /corpora/itkc | 
[**itkc_meta**](DefaultApi.md#itkc_meta) | **GET** /corpora/itkc/{seriesId}/meta/{dataId} | 
[**itkc_series**](DefaultApi.md#itkc_series) | **GET** /corpora/itkc/{seriesId} | 
[**itkc_text**](DefaultApi.md#itkc_text) | **GET** /corpora/itkc/{seriesId}/text/{dataId} | 


# **itkc_all_text_meta**
> InlineResponse2002 itkc_all_text_meta(series_id, data_id)



Recursively list all text nodes under the given `dataId`

### Example

```python
from __future__ import print_function
import time
import classics_proxy_client
from classics_proxy_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with classics_proxy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = classics_proxy_client.DefaultApi(api_client)
    series_id = 'series_id_example' # str | Id of the corpora from `/corpora/itkc`
data_id = 'data_id_example' # str | Id for the node as given in the `data_id` field

    try:
        api_response = api_instance.itkc_all_text_meta(series_id, data_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->itkc_all_text_meta: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **str**| Id of the corpora from &#x60;/corpora/itkc&#x60; | 
 **data_id** | **str**| Id for the node as given in the &#x60;data_id&#x60; field | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **itkc_corpora**
> InlineResponse200 itkc_corpora()



List all supported itkc corpora

### Example

```python
from __future__ import print_function
import time
import classics_proxy_client
from classics_proxy_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with classics_proxy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = classics_proxy_client.DefaultApi(api_client)
    
    try:
        api_response = api_instance.itkc_corpora()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->itkc_corpora: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **itkc_meta**
> InlineResponse2002 itkc_meta(series_id, data_id)



List subsections and articles belonging to the given `dataId`.

### Example

```python
from __future__ import print_function
import time
import classics_proxy_client
from classics_proxy_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with classics_proxy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = classics_proxy_client.DefaultApi(api_client)
    series_id = 'series_id_example' # str | Id of the corpora from `/corpora/itkc`
data_id = 'data_id_example' # str | Id for the node as given in the `data_id` field

    try:
        api_response = api_instance.itkc_meta(series_id, data_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->itkc_meta: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **str**| Id of the corpora from &#x60;/corpora/itkc&#x60; | 
 **data_id** | **str**| Id for the node as given in the &#x60;data_id&#x60; field | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **itkc_series**
> InlineResponse2001 itkc_series(series_id)



List all volumns for the corpus

### Example

```python
from __future__ import print_function
import time
import classics_proxy_client
from classics_proxy_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with classics_proxy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = classics_proxy_client.DefaultApi(api_client)
    series_id = 'series_id_example' # str | Id of the corpora from `/corpora/itkc`

    try:
        api_response = api_instance.itkc_series(series_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->itkc_series: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **str**| Id of the corpora from &#x60;/corpora/itkc&#x60; | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **itkc_text**
> InlineResponse2003 itkc_text(series_id, data_id)



Get the text content

### Example

```python
from __future__ import print_function
import time
import classics_proxy_client
from classics_proxy_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with classics_proxy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = classics_proxy_client.DefaultApi(api_client)
    series_id = 'series_id_example' # str | Id of the corpora from `/corpora/itkc`
data_id = 'data_id_example' # str | Id for the node as given in the `data_id` field

    try:
        api_response = api_instance.itkc_text(series_id, data_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->itkc_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **str**| Id of the corpora from &#x60;/corpora/itkc&#x60; | 
 **data_id** | **str**| Id for the node as given in the &#x60;data_id&#x60; field | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

