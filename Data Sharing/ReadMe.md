# Data Sharing
Welcome to our section on sharing data in GDST. Here we will cover everything related to sharing data including covering the proposed Open REST API, and how to implement that.

 - [Events](#Events)
 - [Trade Items](#Trade%20Items)
 - [Locations](#Locations)
 - [Swagger.IO](#Using%20Swagger.IO)

# Events
Here we are going to cover how to pull and push EPCIS Events to/from a GDST compliant server. For the sake of the examples here, we will be using the following base URL, https://example.org/GDST/

## XML Schema
Events can be pulled in EPCIS Message format.

## Pulling Events
Here we will have an example of PULLING one or more events using a GET operation against the https://example.org/GDST/events/ REST API path. This REST API method requires that the first path parameter is the EPC for which we want all events pulled.

This is an example Request for pulling one or more EPCIS events in EPCIS format.

**Request**
**URL:** https://example.org/GDST/events/urn:gdst:product:lot:class:123.321
**HTTP Method:** GET

**Response**
```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<epcis:EPCISDocument schemaVersion="1.2" creationDate="2013-06-
04T14:59:02.099+02:00"
    xmlns:epcis="urn:epcglobal:epcis:xsd:1"
    xmlns:example="http://ns.example.com/epcis">
    <EPCISBody>
        <EventList>
            <ObjectEvent>
                <eventTime>2017-08-16T13:26:00.000+02:00</eventTime>
                <eventTimeZoneOffset>+02:00</eventTimeZoneOffset>
                <action>OBSERVE</action>
                <bizStep>urn:epcglobal:cbv:bizstep:receiving</bizStep>
                <disposition>urn:epcglobal:cbv:disp:in_transit</disposition>
                <readPoint>
                    <id>geo:34.100389,-117.537468</id>
                </readPoint>
                <bizLocation>
                    <id>urn:epc:id:sgln:0048000.00003.0</id>
                </bizLocation>
                <bizTransactionList>
                    <bizTransaction type="urn:epcglobal:cbv:btt:po">500127042</bizTransaction>
                    <bizTransaction type="urn:epcglobal:cbv:btt:inv">9992332</bizTransaction>
                    <bizTransaction type="urn:epcglobal:cbv:btt:cert">ABC123</bizTransaction>
                </bizTransactionList>
                <extension>
                    <quantityList>
                        <quantityElement>
                            <epcClass>urn:epc:class:lgtin:0048000.363267.YFT123</epcClass>
                            <quantity>5714</quantity>
                            <uom>KGM</uom>
                        </quantityElement>
                        <quantityElement>
                            <epcClass>urn:gdst:example.org:product:lot:class:123.456.789/epcClass>
                            <quantity>1234</quantity>
                            <uom>KGM</uom>
                        </quantityElement>
                    </quantityList>
                </extension>
                <gdst:productOwner>urn:epc:id:pgln:0048000.000001</gdst:productOwner>
                <cbvmda:informationProvider>urn:epc:id:pgln:0048000.00001</cbvmda:informationProvider>
            </ObjectEvent>
        </EventList>
    </EPCISBody>
</epcis:EPCISDocument>
```

## Pushing Events
Events can be posted to a GDST Compliant REST API using the POST Method against the "events" path on the REST API. When posting events, there is also an additional optional HTTP Header called **GDST-Response-URL** that can be used to indicate a GDST Compliant REST API that can be used to look up the Master Data used in the EPCIS Events.


**Request**
**URL:** https://example.org/GDST/events/
**HTTP Method:** POST
**GDST-Response-URL:** https://sender-example.org/GDST/

Request Content
```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<epcis:EPCISDocument schemaVersion="1.2" creationDate="2013-06-
04T14:59:02.099+02:00"
    xmlns:epcis="urn:epcglobal:epcis:xsd:1"
    xmlns:example="http://ns.example.com/epcis">
    <EPCISBody>
        <EventList>
            <ObjectEvent>
                <eventTime>2017-08-16T13:26:00.000+02:00</eventTime>
                <eventTimeZoneOffset>+02:00</eventTimeZoneOffset>
                <action>OBSERVE</action>
                <bizStep>urn:epcglobal:cbv:bizstep:receiving</bizStep>
                <disposition>urn:epcglobal:cbv:disp:in_transit</disposition>
                <readPoint>
                    <id>geo:34.100389,-117.537468</id>
                </readPoint>
                <bizLocation>
                    <id>urn:epc:id:sgln:0048000.00003.0</id>
                </bizLocation>
                <bizTransactionList>
                    <bizTransaction type="urn:epcglobal:cbv:btt:po">500127042</bizTransaction>
                    <bizTransaction type="urn:epcglobal:cbv:btt:inv">9992332</bizTransaction>
                    <bizTransaction type="urn:epcglobal:cbv:btt:cert">ABC123</bizTransaction>
                </bizTransactionList>
                <extension>
                    <quantityList>
                        <quantityElement>
                            <epcClass>urn:epc:class:lgtin:0048000.363267.YFT123</epcClass>
                            <quantity>5714</quantity>
                            <uom>KGM</uom>
                        </quantityElement>
                        <quantityElement>
                            <epcClass>urn:gdst:example.org:product:lot:class:123.456.789/epcClass>
                            <quantity>1234</quantity>
                            <uom>KGM</uom>
                        </quantityElement>
                    </quantityList>
                </extension>
                <gdst:productOwner>urn:epc:id:pgln:0048000.000001</gdst:productOwner>
                <cbvmda:informationProvider>urn:epc:id:pgln:0048000.00001</cbvmda:informationProvider>
            </ObjectEvent>
        </EventList>
    </EPCISBody>
</epcis:EPCISDocument>
```

**Response**
No response is received from the server. Simply a status code of 200.

# Trade Items
Here we are going to cover how to pull Trade Items from a GDST compliant REST server. For the sake of the examples here, we will be using the following base URL, https://example.org/GDST/

## XML Schema
Trade Items can be pulled in GDSN format and in EPCIS Master Data format.

## Pulling Trade Item in GDSN Format
Here we will have an example of PULLING a trade item using a GET operation against the https://example.org/GDST/gtin/ REST API path requesting GDSN format. Because the Catalogue Item for the XML is so big, I did not include the full XML in the example. It's possible that the server cannot provide the Trade Item in GDSN Format. If that is the case, then the server will return in EPCIS Master Data format.

This is an example Request for pulling a Trade Item in GDSN format.

**Request**
**URL:** https://example.org/GDST/gtin/29239439699003?format=gdsn
**HTTP Method:** GET

**Response**
```xml
<catalogue_item_notification:catalogueItemNotificationMessage
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:sh="http://www.unece.org/cefact/namespaces/StandardBusinessDocumentHeader"
    xmlns:catalogue_item_notification="urn:gs1:gdsn:catalogue_item_notification:xsd:3" xsi:schemaLocation="urn:gs1:gdsn:catalogue_item_notification:xsd:3 http://www.gdsregistry.org/3.1/schemas/gs1/gdsn/CatalogueItemNotification.xsd">
    <sh:StandardBusinessDocumentHeader>
        <sh:HeaderVersion>1.0</sh:HeaderVersion>
        <sh:Sender>
            <sh:Identifier Authority="GS1">9312345678907</sh:Identifier>
        </sh:Sender>
        <sh:Receiver>
            <sh:Identifier Authority="GS1">9312345678914</sh:Identifier>
        </sh:Receiver>
        <sh:DocumentIdentification>
            <sh:Standard>GS1</sh:Standard>
            <sh:TypeVersion>3.1</sh:TypeVersion>
            <sh:InstanceIdentifier>c01abb55-b824-4b46-add5-26a5a636a923</sh:InstanceIdentifier>
            <sh:Type>catalogueItemNotification</sh:Type>
            <sh:CreationDateAndTime>2016-06-24T05:55:15.068+10:00</sh:CreationDateAndTime>
        </sh:DocumentIdentification>
    </sh:StandardBusinessDocumentHeader>
    <transaction>
        <transactionIdentification>
            <entityIdentification>c01abb55-b824-4b46-add5-26a5a636a923_1</entityIdentification>
            <contentOwner>
                <gln>9312345527670</gln>
            </contentOwner>
        </transactionIdentification>
        <documentCommand>
            <documentCommandHeader type="CHANGE_BY_REFRESH">
                <documentCommandIdentification>
                    <entityIdentification>c01abb55-b824-4b46-add5-26a5a636a923_1</entityIdentification>
                    <contentOwner>
                        <gln>9312345527670</gln>
                    </contentOwner>
                </documentCommandIdentification>
            </documentCommandHeader>
            <catalogue_item_notification:catalogueItemNotification>
                <creationDateTime>2016-06-24T05:55:15.068+10:00</creationDateTime>
                <documentStatusCode>ORIGINAL</documentStatusCode>
                <documentStructureVersion>3.1</documentStructureVersion>
                <lastUpdateDateTime>2016-06-24T05:55:15.068+10:00</lastUpdateDateTime>
                <catalogueItemNotificationIdentification>
                    <entityIdentification>c01abb55-b824-4b46-add5-26a5a636a923_1</entityIdentification>
                    <contentOwner>
                        <gln>9312345527670</gln>
                    </contentOwner>
                </catalogueItemNotificationIdentification>
                <isReload>false</isReload>
                <catalogueItem>
                   ...
                </catalogueItem>
            </catalogue_item_notification:catalogueItemNotification>
        </documentCommand>
    </transaction>
</catalogue_item_notification:catalogueItemNotificationMessage>
```



## Pulling Trade Item in EPCIS Format
Here we will have an example of PULLING a trade item using a GET operation against the https://example.org/GDST/gtin/ REST API path requesting EPCIS format. Because the Catalogue Item for the XML is so big, I did not include the full XML in the example. Here we do not need to specify a format in the query parameters because by default the server will return EPCIS Master Data format.

This is an example Request for pulling a Trade Item in EPCIS format.

**Request**
**URL:** https://example.org/GDST/gtin/29239439699003
**HTTP Method:** GET

**Response**
```xml
<epcismd:EPCISMasterDataDocument
    xmlns:epcismd="urn:epcglobal:epcis-masterdata:xsd:1"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    schemaVersion="1.0"
    creationDate="2005-07-11T11:30:47.0Z">
    <EPCISBody>
        <VocabularyList>
            <Vocabulary type="urn:epcglobal:epcis:vtype:EPCClass">
                <VocabularyElementList>
                    <VocabularyElement id="urn:epc:idpat:sgtin:0048000.363267">
                        <attribute id="urn:epcglobal:cbv:mda#informationProvider">urn:epc:id:pgln:0048000.000001</attribute>
                        <attribute id="urn:epcglobal:cbv:mda#descriptionShort">Yellowfin Tuna</attribute>
                        <attribute id="urn:epcglobal:cbv:mda#speciesForFisheryStatisticsPurposesName">Thunnus albacares</attribute>
                        <attribute id="urn:epcglobal:cbv:mda#speciesForFisheryStatisticsPurposesCode">YFT</attribute>
                        <attribute id="urn:epcglobal:cbv:mda#tradeItemConditionCode">WHL</attribute>
                    </VocabularyElement>
                </VocabularyElementList>
            </Vocabulary>
        </VocabularyList>
    </EPCISBody>
</epcismd:EPCISMasterDataDocument>
```

# Locations
Here we are going to cover how to pull Locations from a GDST compliant REST server. For the sake of the examples here, we will be using the following base URL, https://example.org/GDST/

## XML Schema
Locations can be pulled in EPCIS Master Data format found {ENTER LINK TO SCHEMA HERE}.

## Pulling Location in EPCIS Format
Here we will have an example of PULLING a location using a GET operation against the https://example.org/GDST/gln/ REST API path requesting EPCIS format. 

This is an example Request for pulling a Location in EPCIS format.

**Request**
**URL:** https://example.org/GDST/gln/urn:gdst:location:loc:123.321
**HTTP Method:** GET

**Response**
```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<epcismd:EPCISMasterDataDocument
    xmlns:epcismd="urn:epcglobal:epcis-masterdata:xsd:1"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    schemaVersion="1.0"
    creationDate="2005-07-11T11:30:47.0Z">
    <EPCISBody>
        <VocabularyList>
            <Vocabulary type="urn:epcglobal:epcis:vtype:BusinessLocation">
                <VocabularyElementList>
                    <VocabularyElement id="urn:epc:id:sgln:0037000.00729.0">
                        <attribute id="http://epcis.example.com/mda/latitude">+18.0000</attribute>
                        <attribute id="http://epcis.example.com/mda/longitude">-70.0000</attribute>
                        <attribute id="http://epcis.example.com/mda/address">
                            <example:Address
                                xmlns:example="http://epcis.example.com/ns">
                                <Street>100 Nowhere Street</Street>
                                <City>Fancy</City>
                                <State>DC</State>
                                <Zip>99999</Zip>
                            </example:Address>
                        </attribute>
                    </VocabularyElement>
                </VocabularyElementList>
            </Vocabulary>
        </VocabularyList>
    </EPCISBody>
</epcismd:EPCISMasterDataDocument>
```

# Using Swagger.IO
With the introduction of an Open API, we have powerful tools like Swagger.IO that can be used to help us generate Client Side and Server Side code. In order to use this tool, the first step to sign-up [here]([https://app.swaggerhub.com/signup?channel=direct&_ga=2.150897974.140053702.1577923794-65358323.1576601843](https://app.swaggerhub.com/signup?channel=direct&_ga=2.150897974.140053702.1577923794-65358323.1576601843)). After you have successfully signed up, it's time to login to your Swagger Hub account. After logging in, you will need to create a new REST API:

![Screenshot of creating a new API on Swagger](https://i.imgur.com/3j8C0KT.png)

After you have created the API, you will be brought to an Editor screen. Here you can copy the contents of the GDST_OpenAPI.yaml into the editor window. The Open API  YAML file can be found here {ADD LINK TO OPEN API FILE HERE}. After you have copied in the YAML file, you can use the Export button at the top right to export the Open API into client and/or server sided codes with the supported programming languages.
![enter image description here](https://i.imgur.com/FQqLtmJ.png)
