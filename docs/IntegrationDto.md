# IntegrationDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**name_identifier** | **str** |  | [optional] 
**short_description** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**release_status** | **AllOfIntegrationDtoReleaseStatus** |   0 &#x3D; Released  1 &#x3D; Pending  2 &#x3D; NotPlanned | [optional] 
**launch_date** | **datetime** |  | [optional] 
**documentation_url** | **str** |  | [optional] 
**swagger_url** | **str** |  | [optional] 
**integration_endpoints** | [**list[IntegrationEndpointDto]**](IntegrationEndpointDto.md) |  | [optional] 
**integration_events** | [**list[IntegrationEventDto]**](IntegrationEventDto.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

