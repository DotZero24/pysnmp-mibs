_p='hhmsCompressedSummaryIndex'
_o='hhmsSensorArrayCameraIndex'
_n='hhmsSensorArrayHighDriveIndex'
_m='hhmsSensorArrayPowerMonitorIndex'
_l='hhmsSensorArrayPowerControlIndex'
_k='hhmsSensorArraySerialIndex'
_j='closed'
_i='hhmsSensorArraySwitchIndex'
_h='hhmsSensorArrayHumidityIndex'
_g='testLowCritical'
_f='testLowWarning'
_e='testHighCritical'
_d='testHighWarning'
_c='testNormal'
_b='testNoStatus'
_a='hhmsSensorArrayTempIndex'
_Z='NotificationType'
_Y='lowCritical'
_X='lowWarning'
_W='highCritical'
_V='highWarning'
_U='critical'
_T='hhmsSensorDescription'
_S='hhmsSensorName'
_R='hhmsSensorIndex'
_Q='hhmsSensorLevelExceeded'
_P='hhmsSensorValue'
_O='hhmsSensorStatus'
_N='goOffline'
_M='goOnline'
_L='offline'
_K='online'
_J='off'
_I='on'
_H='normal'
_G='noStatus'
_F='sensorError'
_E='HHMSAGENT-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_Z,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_Z,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Akcp_ObjectIdentity=ObjectIdentity
akcp=_Akcp_ObjectIdentity((1,3,6,1,4,1,3854))
_Hhmsagent_ObjectIdentity=ObjectIdentity
hhmsagent=_Hhmsagent_ObjectIdentity((1,3,6,1,4,1,3854,1))
_HhmsAgentSummary_ObjectIdentity=ObjectIdentity
hhmsAgentSummary=_HhmsAgentSummary_ObjectIdentity((1,3,6,1,4,1,3854,1,1))
_HhmsAgentLocation_Type=DisplayString
_HhmsAgentLocation_Object=MibScalar
hhmsAgentLocation=_HhmsAgentLocation_Object((1,3,6,1,4,1,3854,1,1,1),_HhmsAgentLocation_Type())
hhmsAgentLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsAgentLocation.setStatus(_A)
class _HhmsAgentStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_G,1),(_H,2),('warning',3),(_U,4),(_F,5)))
_HhmsAgentStatus_Type.__name__=_C
_HhmsAgentStatus_Object=MibScalar
hhmsAgentStatus=_HhmsAgentStatus_Object((1,3,6,1,4,1,3854,1,1,2),_HhmsAgentStatus_Type())
hhmsAgentStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsAgentStatus.setStatus(_A)
_HhmsNumberBadSensors_Type=Integer32
_HhmsNumberBadSensors_Object=MibScalar
hhmsNumberBadSensors=_HhmsNumberBadSensors_Object((1,3,6,1,4,1,3854,1,1,4),_HhmsNumberBadSensors_Type())
hhmsNumberBadSensors.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsNumberBadSensors.setStatus(_A)
_HhmsLocationBadSensor_Type=DisplayString
_HhmsLocationBadSensor_Object=MibScalar
hhmsLocationBadSensor=_HhmsLocationBadSensor_Object((1,3,6,1,4,1,3854,1,1,5),_HhmsLocationBadSensor_Type())
hhmsLocationBadSensor.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsLocationBadSensor.setStatus(_A)
_HhmsAgentManufName_Type=DisplayString
_HhmsAgentManufName_Object=MibScalar
hhmsAgentManufName=_HhmsAgentManufName_Object((1,3,6,1,4,1,3854,1,1,6),_HhmsAgentManufName_Type())
hhmsAgentManufName.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsAgentManufName.setStatus(_A)
_HhmsAgentHelpUrl_Type=DisplayString
_HhmsAgentHelpUrl_Object=MibScalar
hhmsAgentHelpUrl=_HhmsAgentHelpUrl_Object((1,3,6,1,4,1,3854,1,1,7),_HhmsAgentHelpUrl_Type())
hhmsAgentHelpUrl.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsAgentHelpUrl.setStatus(_A)
class _HhmsAgentHtmlView_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('sensorArray',1),('sensorArrayPro',2),('advanced',3)))
_HhmsAgentHtmlView_Type.__name__=_C
_HhmsAgentHtmlView_Object=MibScalar
hhmsAgentHtmlView=_HhmsAgentHtmlView_Object((1,3,6,1,4,1,3854,1,1,8),_HhmsAgentHtmlView_Type())
hhmsAgentHtmlView.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsAgentHtmlView.setStatus(_A)
_HhmsAgentHtmlStandardTitle_Type=DisplayString
_HhmsAgentHtmlStandardTitle_Object=MibScalar
hhmsAgentHtmlStandardTitle=_HhmsAgentHtmlStandardTitle_Object((1,3,6,1,4,1,3854,1,1,9),_HhmsAgentHtmlStandardTitle_Type())
hhmsAgentHtmlStandardTitle.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsAgentHtmlStandardTitle.setStatus(_A)
_HhmsAgentHtmlStandardButton_Type=DisplayString
_HhmsAgentHtmlStandardButton_Object=MibScalar
hhmsAgentHtmlStandardButton=_HhmsAgentHtmlStandardButton_Object((1,3,6,1,4,1,3854,1,1,10),_HhmsAgentHtmlStandardButton_Type())
hhmsAgentHtmlStandardButton.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsAgentHtmlStandardButton.setStatus(_A)
_HhmsSensor_ObjectIdentity=ObjectIdentity
hhmsSensor=_HhmsSensor_ObjectIdentity((1,3,6,1,4,1,3854,1,2))
_HhmsSensorArrayTable_ObjectIdentity=ObjectIdentity
hhmsSensorArrayTable=_HhmsSensorArrayTable_ObjectIdentity((1,3,6,1,4,1,3854,1,2,2))
_HhmsSensorArrayEntry_ObjectIdentity=ObjectIdentity
hhmsSensorArrayEntry=_HhmsSensorArrayEntry_ObjectIdentity((1,3,6,1,4,1,3854,1,2,2,1))
_HhmsSensorArrayHost_Type=IpAddress
_HhmsSensorArrayHost_Object=MibScalar
hhmsSensorArrayHost=_HhmsSensorArrayHost_Object((1,3,6,1,4,1,3854,1,2,2,1,1),_HhmsSensorArrayHost_Type())
hhmsSensorArrayHost.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayHost.setStatus(_A)
class _HhmsSensorArrayUseDHCP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_HhmsSensorArrayUseDHCP_Type.__name__=_C
_HhmsSensorArrayUseDHCP_Object=MibScalar
hhmsSensorArrayUseDHCP=_HhmsSensorArrayUseDHCP_Object((1,3,6,1,4,1,3854,1,2,2,1,2),_HhmsSensorArrayUseDHCP_Type())
hhmsSensorArrayUseDHCP.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayUseDHCP.setStatus(_A)
_HhmsSensorArrayMAC_Type=DisplayString
_HhmsSensorArrayMAC_Object=MibScalar
hhmsSensorArrayMAC=_HhmsSensorArrayMAC_Object((1,3,6,1,4,1,3854,1,2,2,1,3),_HhmsSensorArrayMAC_Type())
hhmsSensorArrayMAC.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsSensorArrayMAC.setStatus(_A)
_HhmsSensorArraySetCommunity_Type=DisplayString
_HhmsSensorArraySetCommunity_Object=MibScalar
hhmsSensorArraySetCommunity=_HhmsSensorArraySetCommunity_Object((1,3,6,1,4,1,3854,1,2,2,1,4),_HhmsSensorArraySetCommunity_Type())
hhmsSensorArraySetCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArraySetCommunity.setStatus(_A)
_HhmsSensorArrayGetCommunity_Type=DisplayString
_HhmsSensorArrayGetCommunity_Object=MibScalar
hhmsSensorArrayGetCommunity=_HhmsSensorArrayGetCommunity_Object((1,3,6,1,4,1,3854,1,2,2,1,5),_HhmsSensorArrayGetCommunity_Type())
hhmsSensorArrayGetCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayGetCommunity.setStatus(_A)
_HhmsSensorArrayDescription_Type=DisplayString
_HhmsSensorArrayDescription_Object=MibScalar
hhmsSensorArrayDescription=_HhmsSensorArrayDescription_Object((1,3,6,1,4,1,3854,1,2,2,1,6),_HhmsSensorArrayDescription_Type())
hhmsSensorArrayDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayDescription.setStatus(_A)
_HhmsSensorArrayLocation_Type=DisplayString
_HhmsSensorArrayLocation_Object=MibScalar
hhmsSensorArrayLocation=_HhmsSensorArrayLocation_Object((1,3,6,1,4,1,3854,1,2,2,1,7),_HhmsSensorArrayLocation_Type())
hhmsSensorArrayLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayLocation.setStatus(_A)
_HhmsSensorArrayLastUpdate_Type=DisplayString
_HhmsSensorArrayLastUpdate_Object=MibScalar
hhmsSensorArrayLastUpdate=_HhmsSensorArrayLastUpdate_Object((1,3,6,1,4,1,3854,1,2,2,1,8),_HhmsSensorArrayLastUpdate_Type())
hhmsSensorArrayLastUpdate.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsSensorArrayLastUpdate.setStatus(_A)
class _HhmsSensorArrayStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,7)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,7)))
_HhmsSensorArrayStatus_Type.__name__=_C
_HhmsSensorArrayStatus_Object=MibScalar
hhmsSensorArrayStatus=_HhmsSensorArrayStatus_Object((1,3,6,1,4,1,3854,1,2,2,1,9),_HhmsSensorArrayStatus_Type())
hhmsSensorArrayStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsSensorArrayStatus.setStatus(_A)
class _HhmsSensorArrayOnline_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_HhmsSensorArrayOnline_Type.__name__=_C
_HhmsSensorArrayOnline_Object=MibScalar
hhmsSensorArrayOnline=_HhmsSensorArrayOnline_Object((1,3,6,1,4,1,3854,1,2,2,1,10),_HhmsSensorArrayOnline_Type())
hhmsSensorArrayOnline.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsSensorArrayOnline.setStatus(_A)
class _HhmsSensorArrayGoOnline_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_HhmsSensorArrayGoOnline_Type.__name__=_C
_HhmsSensorArrayGoOnline_Object=MibScalar
hhmsSensorArrayGoOnline=_HhmsSensorArrayGoOnline_Object((1,3,6,1,4,1,3854,1,2,2,1,11),_HhmsSensorArrayGoOnline_Type())
hhmsSensorArrayGoOnline.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayGoOnline.setStatus(_A)
_HhmsSensorArrayReadInterval_Type=Integer32
_HhmsSensorArrayReadInterval_Object=MibScalar
hhmsSensorArrayReadInterval=_HhmsSensorArrayReadInterval_Object((1,3,6,1,4,1,3854,1,2,2,1,12),_HhmsSensorArrayReadInterval_Type())
hhmsSensorArrayReadInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayReadInterval.setStatus(_A)
_HhmsSensorArrayReceiveTimeout_Type=Integer32
_HhmsSensorArrayReceiveTimeout_Object=MibScalar
hhmsSensorArrayReceiveTimeout=_HhmsSensorArrayReceiveTimeout_Object((1,3,6,1,4,1,3854,1,2,2,1,13),_HhmsSensorArrayReceiveTimeout_Type())
hhmsSensorArrayReceiveTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayReceiveTimeout.setStatus(_A)
_HhmsSensorArrayReceiveRetries_Type=Integer32
_HhmsSensorArrayReceiveRetries_Object=MibScalar
hhmsSensorArrayReceiveRetries=_HhmsSensorArrayReceiveRetries_Object((1,3,6,1,4,1,3854,1,2,2,1,14),_HhmsSensorArrayReceiveRetries_Type())
hhmsSensorArrayReceiveRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayReceiveRetries.setStatus(_A)
_HhmsSensorArrayVersion_Type=Integer32
_HhmsSensorArrayVersion_Object=MibScalar
hhmsSensorArrayVersion=_HhmsSensorArrayVersion_Object((1,3,6,1,4,1,3854,1,2,2,1,15),_HhmsSensorArrayVersion_Type())
hhmsSensorArrayVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsSensorArrayVersion.setStatus(_A)
_HhmsSensorArrayTempTable_Object=MibTable
hhmsSensorArrayTempTable=_HhmsSensorArrayTempTable_Object((1,3,6,1,4,1,3854,1,2,2,1,16))
if mibBuilder.loadTexts:hhmsSensorArrayTempTable.setStatus(_A)
_HhmsSensorArrayTempEntry_Object=MibTableRow
hhmsSensorArrayTempEntry=_HhmsSensorArrayTempEntry_Object((1,3,6,1,4,1,3854,1,2,2,1,16,1))
hhmsSensorArrayTempEntry.setIndexNames((0,_E,_a))
if mibBuilder.loadTexts:hhmsSensorArrayTempEntry.setStatus(_A)
_HhmsSensorArrayTempDescription_Type=DisplayString
_HhmsSensorArrayTempDescription_Object=MibTableColumn
hhmsSensorArrayTempDescription=_HhmsSensorArrayTempDescription_Object((1,3,6,1,4,1,3854,1,2,2,1,16,1,1),_HhmsSensorArrayTempDescription_Type())
hhmsSensorArrayTempDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayTempDescription.setStatus(_A)
_HhmsSensorArrayTempLocation_Type=DisplayString
_HhmsSensorArrayTempLocation_Object=MibTableColumn
hhmsSensorArrayTempLocation=_HhmsSensorArrayTempLocation_Object((1,3,6,1,4,1,3854,1,2,2,1,16,1,2),_HhmsSensorArrayTempLocation_Type())
hhmsSensorArrayTempLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayTempLocation.setStatus(_A)
_HhmsSensorArrayTempDegree_Type=Integer32
_HhmsSensorArrayTempDegree_Object=MibTableColumn
hhmsSensorArrayTempDegree=_HhmsSensorArrayTempDegree_Object((1,3,6,1,4,1,3854,1,2,2,1,16,1,3),_HhmsSensorArrayTempDegree_Type())
hhmsSensorArrayTempDegree.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsSensorArrayTempDegree.setStatus(_A)
class _HhmsSensorArrayTempStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_G,1),(_H,2),(_V,3),(_W,4),(_X,5),(_Y,6),(_F,7)))
_HhmsSensorArrayTempStatus_Type.__name__=_C
_HhmsSensorArrayTempStatus_Object=MibTableColumn
hhmsSensorArrayTempStatus=_HhmsSensorArrayTempStatus_Object((1,3,6,1,4,1,3854,1,2,2,1,16,1,4),_HhmsSensorArrayTempStatus_Type())
hhmsSensorArrayTempStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsSensorArrayTempStatus.setStatus(_A)
class _HhmsSensorArrayTempOnline_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_HhmsSensorArrayTempOnline_Type.__name__=_C
_HhmsSensorArrayTempOnline_Object=MibTableColumn
hhmsSensorArrayTempOnline=_HhmsSensorArrayTempOnline_Object((1,3,6,1,4,1,3854,1,2,2,1,16,1,5),_HhmsSensorArrayTempOnline_Type())
hhmsSensorArrayTempOnline.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsSensorArrayTempOnline.setStatus(_A)
class _HhmsSensorArrayTempGoOnline_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_HhmsSensorArrayTempGoOnline_Type.__name__=_C
_HhmsSensorArrayTempGoOnline_Object=MibTableColumn
hhmsSensorArrayTempGoOnline=_HhmsSensorArrayTempGoOnline_Object((1,3,6,1,4,1,3854,1,2,2,1,16,1,6),_HhmsSensorArrayTempGoOnline_Type())
hhmsSensorArrayTempGoOnline.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayTempGoOnline.setStatus(_A)
_HhmsSensorArrayTempHighWarning_Type=Integer32
_HhmsSensorArrayTempHighWarning_Object=MibTableColumn
hhmsSensorArrayTempHighWarning=_HhmsSensorArrayTempHighWarning_Object((1,3,6,1,4,1,3854,1,2,2,1,16,1,7),_HhmsSensorArrayTempHighWarning_Type())
hhmsSensorArrayTempHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayTempHighWarning.setStatus(_A)
_HhmsSensorArrayTempHighCritical_Type=Integer32
_HhmsSensorArrayTempHighCritical_Object=MibTableColumn
hhmsSensorArrayTempHighCritical=_HhmsSensorArrayTempHighCritical_Object((1,3,6,1,4,1,3854,1,2,2,1,16,1,8),_HhmsSensorArrayTempHighCritical_Type())
hhmsSensorArrayTempHighCritical.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayTempHighCritical.setStatus(_A)
_HhmsSensorArrayTempLowWarning_Type=Integer32
_HhmsSensorArrayTempLowWarning_Object=MibTableColumn
hhmsSensorArrayTempLowWarning=_HhmsSensorArrayTempLowWarning_Object((1,3,6,1,4,1,3854,1,2,2,1,16,1,9),_HhmsSensorArrayTempLowWarning_Type())
hhmsSensorArrayTempLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayTempLowWarning.setStatus(_A)
_HhmsSensorArrayTempLowCritical_Type=Integer32
_HhmsSensorArrayTempLowCritical_Object=MibTableColumn
hhmsSensorArrayTempLowCritical=_HhmsSensorArrayTempLowCritical_Object((1,3,6,1,4,1,3854,1,2,2,1,16,1,10),_HhmsSensorArrayTempLowCritical_Type())
hhmsSensorArrayTempLowCritical.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayTempLowCritical.setStatus(_A)
_HhmsSensorArrayTempRearm_Type=Integer32
_HhmsSensorArrayTempRearm_Object=MibTableColumn
hhmsSensorArrayTempRearm=_HhmsSensorArrayTempRearm_Object((1,3,6,1,4,1,3854,1,2,2,1,16,1,11),_HhmsSensorArrayTempRearm_Type())
hhmsSensorArrayTempRearm.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayTempRearm.setStatus(_A)
class _HhmsSensorArrayTempDegreeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('fahr',0),('celsius',1)))
_HhmsSensorArrayTempDegreeType_Type.__name__=_C
_HhmsSensorArrayTempDegreeType_Object=MibTableColumn
hhmsSensorArrayTempDegreeType=_HhmsSensorArrayTempDegreeType_Object((1,3,6,1,4,1,3854,1,2,2,1,16,1,12),_HhmsSensorArrayTempDegreeType_Type())
hhmsSensorArrayTempDegreeType.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayTempDegreeType.setStatus(_A)
class _HhmsSensorArrayTempSensorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('type1',0),('type2',1)))
_HhmsSensorArrayTempSensorType_Type.__name__=_C
_HhmsSensorArrayTempSensorType_Object=MibTableColumn
hhmsSensorArrayTempSensorType=_HhmsSensorArrayTempSensorType_Object((1,3,6,1,4,1,3854,1,2,2,1,16,1,13),_HhmsSensorArrayTempSensorType_Type())
hhmsSensorArrayTempSensorType.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayTempSensorType.setStatus(_A)
class _HhmsSensorArrayTempTestStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_b,1),(_c,2),(_d,3),(_e,4),(_f,5),(_g,6),(_F,7)))
_HhmsSensorArrayTempTestStatus_Type.__name__=_C
_HhmsSensorArrayTempTestStatus_Object=MibTableColumn
hhmsSensorArrayTempTestStatus=_HhmsSensorArrayTempTestStatus_Object((1,3,6,1,4,1,3854,1,2,2,1,16,1,14),_HhmsSensorArrayTempTestStatus_Type())
hhmsSensorArrayTempTestStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayTempTestStatus.setStatus(_A)
_HhmsSensorArrayTempTestDegree_Type=Integer32
_HhmsSensorArrayTempTestDegree_Object=MibTableColumn
hhmsSensorArrayTempTestDegree=_HhmsSensorArrayTempTestDegree_Object((1,3,6,1,4,1,3854,1,2,2,1,16,1,15),_HhmsSensorArrayTempTestDegree_Type())
hhmsSensorArrayTempTestDegree.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayTempTestDegree.setStatus(_A)
class _HhmsSensorArrayTempIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_HhmsSensorArrayTempIndex_Type.__name__=_C
_HhmsSensorArrayTempIndex_Object=MibTableColumn
hhmsSensorArrayTempIndex=_HhmsSensorArrayTempIndex_Object((1,3,6,1,4,1,3854,1,2,2,1,16,1,16),_HhmsSensorArrayTempIndex_Type())
hhmsSensorArrayTempIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsSensorArrayTempIndex.setStatus(_A)
_HhmsSensorArrayHumidityTable_Object=MibTable
hhmsSensorArrayHumidityTable=_HhmsSensorArrayHumidityTable_Object((1,3,6,1,4,1,3854,1,2,2,1,17))
if mibBuilder.loadTexts:hhmsSensorArrayHumidityTable.setStatus(_A)
_HhmsSensorArrayHumidityEntry_Object=MibTableRow
hhmsSensorArrayHumidityEntry=_HhmsSensorArrayHumidityEntry_Object((1,3,6,1,4,1,3854,1,2,2,1,17,1))
hhmsSensorArrayHumidityEntry.setIndexNames((0,_E,_h))
if mibBuilder.loadTexts:hhmsSensorArrayHumidityEntry.setStatus(_A)
_HhmsSensorArrayHumidityDescription_Type=DisplayString
_HhmsSensorArrayHumidityDescription_Object=MibTableColumn
hhmsSensorArrayHumidityDescription=_HhmsSensorArrayHumidityDescription_Object((1,3,6,1,4,1,3854,1,2,2,1,17,1,1),_HhmsSensorArrayHumidityDescription_Type())
hhmsSensorArrayHumidityDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayHumidityDescription.setStatus(_A)
_HhmsSensorArrayHumidityLocation_Type=DisplayString
_HhmsSensorArrayHumidityLocation_Object=MibTableColumn
hhmsSensorArrayHumidityLocation=_HhmsSensorArrayHumidityLocation_Object((1,3,6,1,4,1,3854,1,2,2,1,17,1,2),_HhmsSensorArrayHumidityLocation_Type())
hhmsSensorArrayHumidityLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayHumidityLocation.setStatus(_A)
_HhmsSensorArrayHumidityPercent_Type=Integer32
_HhmsSensorArrayHumidityPercent_Object=MibTableColumn
hhmsSensorArrayHumidityPercent=_HhmsSensorArrayHumidityPercent_Object((1,3,6,1,4,1,3854,1,2,2,1,17,1,3),_HhmsSensorArrayHumidityPercent_Type())
hhmsSensorArrayHumidityPercent.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsSensorArrayHumidityPercent.setStatus(_A)
class _HhmsSensorArrayHumidityStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_G,1),(_H,2),(_V,3),(_W,4),(_X,5),(_Y,6),(_F,7)))
_HhmsSensorArrayHumidityStatus_Type.__name__=_C
_HhmsSensorArrayHumidityStatus_Object=MibTableColumn
hhmsSensorArrayHumidityStatus=_HhmsSensorArrayHumidityStatus_Object((1,3,6,1,4,1,3854,1,2,2,1,17,1,4),_HhmsSensorArrayHumidityStatus_Type())
hhmsSensorArrayHumidityStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsSensorArrayHumidityStatus.setStatus(_A)
class _HhmsSensorArrayHumidityOnline_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_HhmsSensorArrayHumidityOnline_Type.__name__=_C
_HhmsSensorArrayHumidityOnline_Object=MibTableColumn
hhmsSensorArrayHumidityOnline=_HhmsSensorArrayHumidityOnline_Object((1,3,6,1,4,1,3854,1,2,2,1,17,1,5),_HhmsSensorArrayHumidityOnline_Type())
hhmsSensorArrayHumidityOnline.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsSensorArrayHumidityOnline.setStatus(_A)
class _HhmsSensorArrayHumidityGoOnline_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_HhmsSensorArrayHumidityGoOnline_Type.__name__=_C
_HhmsSensorArrayHumidityGoOnline_Object=MibTableColumn
hhmsSensorArrayHumidityGoOnline=_HhmsSensorArrayHumidityGoOnline_Object((1,3,6,1,4,1,3854,1,2,2,1,17,1,6),_HhmsSensorArrayHumidityGoOnline_Type())
hhmsSensorArrayHumidityGoOnline.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayHumidityGoOnline.setStatus(_A)
_HhmsSensorArrayHumidityHighWarning_Type=Integer32
_HhmsSensorArrayHumidityHighWarning_Object=MibTableColumn
hhmsSensorArrayHumidityHighWarning=_HhmsSensorArrayHumidityHighWarning_Object((1,3,6,1,4,1,3854,1,2,2,1,17,1,7),_HhmsSensorArrayHumidityHighWarning_Type())
hhmsSensorArrayHumidityHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayHumidityHighWarning.setStatus(_A)
_HhmsSensorArrayHumidityHighCritical_Type=Integer32
_HhmsSensorArrayHumidityHighCritical_Object=MibTableColumn
hhmsSensorArrayHumidityHighCritical=_HhmsSensorArrayHumidityHighCritical_Object((1,3,6,1,4,1,3854,1,2,2,1,17,1,8),_HhmsSensorArrayHumidityHighCritical_Type())
hhmsSensorArrayHumidityHighCritical.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayHumidityHighCritical.setStatus(_A)
_HhmsSensorArrayHumidityLowWarning_Type=Integer32
_HhmsSensorArrayHumidityLowWarning_Object=MibTableColumn
hhmsSensorArrayHumidityLowWarning=_HhmsSensorArrayHumidityLowWarning_Object((1,3,6,1,4,1,3854,1,2,2,1,17,1,9),_HhmsSensorArrayHumidityLowWarning_Type())
hhmsSensorArrayHumidityLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayHumidityLowWarning.setStatus(_A)
_HhmsSensorArrayHumidityLowCritical_Type=Integer32
_HhmsSensorArrayHumidityLowCritical_Object=MibTableColumn
hhmsSensorArrayHumidityLowCritical=_HhmsSensorArrayHumidityLowCritical_Object((1,3,6,1,4,1,3854,1,2,2,1,17,1,10),_HhmsSensorArrayHumidityLowCritical_Type())
hhmsSensorArrayHumidityLowCritical.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayHumidityLowCritical.setStatus(_A)
_HhmsSensorArrayHumidityRearm_Type=Integer32
_HhmsSensorArrayHumidityRearm_Object=MibTableColumn
hhmsSensorArrayHumidityRearm=_HhmsSensorArrayHumidityRearm_Object((1,3,6,1,4,1,3854,1,2,2,1,17,1,11),_HhmsSensorArrayHumidityRearm_Type())
hhmsSensorArrayHumidityRearm.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayHumidityRearm.setStatus(_A)
class _HhmsSensorArrayHumidityTestStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_b,1),(_c,2),(_d,3),(_e,4),(_f,5),(_g,6),(_F,7)))
_HhmsSensorArrayHumidityTestStatus_Type.__name__=_C
_HhmsSensorArrayHumidityTestStatus_Object=MibTableColumn
hhmsSensorArrayHumidityTestStatus=_HhmsSensorArrayHumidityTestStatus_Object((1,3,6,1,4,1,3854,1,2,2,1,17,1,12),_HhmsSensorArrayHumidityTestStatus_Type())
hhmsSensorArrayHumidityTestStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayHumidityTestStatus.setStatus(_A)
_HhmsSensorArrayHumidityTestPercent_Type=Integer32
_HhmsSensorArrayHumidityTestPercent_Object=MibTableColumn
hhmsSensorArrayHumidityTestPercent=_HhmsSensorArrayHumidityTestPercent_Object((1,3,6,1,4,1,3854,1,2,2,1,17,1,13),_HhmsSensorArrayHumidityTestPercent_Type())
hhmsSensorArrayHumidityTestPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayHumidityTestPercent.setStatus(_A)
class _HhmsSensorArrayHumidityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_HhmsSensorArrayHumidityIndex_Type.__name__=_C
_HhmsSensorArrayHumidityIndex_Object=MibTableColumn
hhmsSensorArrayHumidityIndex=_HhmsSensorArrayHumidityIndex_Object((1,3,6,1,4,1,3854,1,2,2,1,17,1,14),_HhmsSensorArrayHumidityIndex_Type())
hhmsSensorArrayHumidityIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsSensorArrayHumidityIndex.setStatus(_A)
_HhmsSensorArraySwitchTable_Object=MibTable
hhmsSensorArraySwitchTable=_HhmsSensorArraySwitchTable_Object((1,3,6,1,4,1,3854,1,2,2,1,18))
if mibBuilder.loadTexts:hhmsSensorArraySwitchTable.setStatus(_A)
_HhmsSensorArraySwitchEntry_Object=MibTableRow
hhmsSensorArraySwitchEntry=_HhmsSensorArraySwitchEntry_Object((1,3,6,1,4,1,3854,1,2,2,1,18,1))
hhmsSensorArraySwitchEntry.setIndexNames((0,_E,_i))
if mibBuilder.loadTexts:hhmsSensorArraySwitchEntry.setStatus(_A)
_HhmsSensorArraySwitchDescription_Type=DisplayString
_HhmsSensorArraySwitchDescription_Object=MibTableColumn
hhmsSensorArraySwitchDescription=_HhmsSensorArraySwitchDescription_Object((1,3,6,1,4,1,3854,1,2,2,1,18,1,1),_HhmsSensorArraySwitchDescription_Type())
hhmsSensorArraySwitchDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArraySwitchDescription.setStatus(_A)
_HhmsSensorArraySwitchLocation_Type=DisplayString
_HhmsSensorArraySwitchLocation_Object=MibTableColumn
hhmsSensorArraySwitchLocation=_HhmsSensorArraySwitchLocation_Object((1,3,6,1,4,1,3854,1,2,2,1,18,1,2),_HhmsSensorArraySwitchLocation_Type())
hhmsSensorArraySwitchLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArraySwitchLocation.setStatus(_A)
class _HhmsSensorArraySwitchStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,7)));namedValues=NamedValues(*((_G,1),(_H,2),(_U,4),(_F,7)))
_HhmsSensorArraySwitchStatus_Type.__name__=_C
_HhmsSensorArraySwitchStatus_Object=MibTableColumn
hhmsSensorArraySwitchStatus=_HhmsSensorArraySwitchStatus_Object((1,3,6,1,4,1,3854,1,2,2,1,18,1,3),_HhmsSensorArraySwitchStatus_Type())
hhmsSensorArraySwitchStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsSensorArraySwitchStatus.setStatus(_A)
class _HhmsSensorArraySwitchOnline_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_HhmsSensorArraySwitchOnline_Type.__name__=_C
_HhmsSensorArraySwitchOnline_Object=MibTableColumn
hhmsSensorArraySwitchOnline=_HhmsSensorArraySwitchOnline_Object((1,3,6,1,4,1,3854,1,2,2,1,18,1,4),_HhmsSensorArraySwitchOnline_Type())
hhmsSensorArraySwitchOnline.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsSensorArraySwitchOnline.setStatus(_A)
class _HhmsSensorArraySwitchGoOnline_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_HhmsSensorArraySwitchGoOnline_Type.__name__=_C
_HhmsSensorArraySwitchGoOnline_Object=MibTableColumn
hhmsSensorArraySwitchGoOnline=_HhmsSensorArraySwitchGoOnline_Object((1,3,6,1,4,1,3854,1,2,2,1,18,1,5),_HhmsSensorArraySwitchGoOnline_Type())
hhmsSensorArraySwitchGoOnline.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArraySwitchGoOnline.setStatus(_A)
class _HhmsSensorArraySwitchDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('input',0),('output',1)))
_HhmsSensorArraySwitchDirection_Type.__name__=_C
_HhmsSensorArraySwitchDirection_Object=MibTableColumn
hhmsSensorArraySwitchDirection=_HhmsSensorArraySwitchDirection_Object((1,3,6,1,4,1,3854,1,2,2,1,18,1,6),_HhmsSensorArraySwitchDirection_Type())
hhmsSensorArraySwitchDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArraySwitchDirection.setStatus(_A)
class _HhmsSensorArraySwitchNormalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_j,0),('open',1)))
_HhmsSensorArraySwitchNormalState_Type.__name__=_C
_HhmsSensorArraySwitchNormalState_Object=MibTableColumn
hhmsSensorArraySwitchNormalState=_HhmsSensorArraySwitchNormalState_Object((1,3,6,1,4,1,3854,1,2,2,1,18,1,7),_HhmsSensorArraySwitchNormalState_Type())
hhmsSensorArraySwitchNormalState.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArraySwitchNormalState.setStatus(_A)
class _HhmsSensorArraySwitchOutputLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('low',0),('high',1)))
_HhmsSensorArraySwitchOutputLevel_Type.__name__=_C
_HhmsSensorArraySwitchOutputLevel_Object=MibTableColumn
hhmsSensorArraySwitchOutputLevel=_HhmsSensorArraySwitchOutputLevel_Object((1,3,6,1,4,1,3854,1,2,2,1,18,1,8),_HhmsSensorArraySwitchOutputLevel_Type())
hhmsSensorArraySwitchOutputLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArraySwitchOutputLevel.setStatus(_A)
class _HhmsSensorArraySwitchTestState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,7)));namedValues=NamedValues(*((_G,1),(_H,2),(_U,4),(_F,7)))
_HhmsSensorArraySwitchTestState_Type.__name__=_C
_HhmsSensorArraySwitchTestState_Object=MibTableColumn
hhmsSensorArraySwitchTestState=_HhmsSensorArraySwitchTestState_Object((1,3,6,1,4,1,3854,1,2,2,1,18,1,9),_HhmsSensorArraySwitchTestState_Type())
hhmsSensorArraySwitchTestState.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsSensorArraySwitchTestState.setStatus(_A)
class _HhmsSensorArraySwitchIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_HhmsSensorArraySwitchIndex_Type.__name__=_C
_HhmsSensorArraySwitchIndex_Object=MibTableColumn
hhmsSensorArraySwitchIndex=_HhmsSensorArraySwitchIndex_Object((1,3,6,1,4,1,3854,1,2,2,1,18,1,10),_HhmsSensorArraySwitchIndex_Type())
hhmsSensorArraySwitchIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsSensorArraySwitchIndex.setStatus(_A)
_HhmsSensorArraySerialTable_Object=MibTable
hhmsSensorArraySerialTable=_HhmsSensorArraySerialTable_Object((1,3,6,1,4,1,3854,1,2,2,1,19))
if mibBuilder.loadTexts:hhmsSensorArraySerialTable.setStatus(_A)
_HhmsSensorArraySerialEntry_Object=MibTableRow
hhmsSensorArraySerialEntry=_HhmsSensorArraySerialEntry_Object((1,3,6,1,4,1,3854,1,2,2,1,19,1))
hhmsSensorArraySerialEntry.setIndexNames((0,_E,_k))
if mibBuilder.loadTexts:hhmsSensorArraySerialEntry.setStatus(_A)
_HhmsSensorArraySerialDescription_Type=DisplayString
_HhmsSensorArraySerialDescription_Object=MibTableColumn
hhmsSensorArraySerialDescription=_HhmsSensorArraySerialDescription_Object((1,3,6,1,4,1,3854,1,2,2,1,19,1,1),_HhmsSensorArraySerialDescription_Type())
hhmsSensorArraySerialDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArraySerialDescription.setStatus(_A)
_HhmsSensorArraySerialLocation_Type=DisplayString
_HhmsSensorArraySerialLocation_Object=MibTableColumn
hhmsSensorArraySerialLocation=_HhmsSensorArraySerialLocation_Object((1,3,6,1,4,1,3854,1,2,2,1,19,1,2),_HhmsSensorArraySerialLocation_Type())
hhmsSensorArraySerialLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArraySerialLocation.setStatus(_A)
class _HhmsSensorArraySerialStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,7)));namedValues=NamedValues(*((_G,1),(_H,2),(_U,4),(_F,7)))
_HhmsSensorArraySerialStatus_Type.__name__=_C
_HhmsSensorArraySerialStatus_Object=MibTableColumn
hhmsSensorArraySerialStatus=_HhmsSensorArraySerialStatus_Object((1,3,6,1,4,1,3854,1,2,2,1,19,1,3),_HhmsSensorArraySerialStatus_Type())
hhmsSensorArraySerialStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsSensorArraySerialStatus.setStatus(_A)
class _HhmsSensorArraySerialOnline_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_HhmsSensorArraySerialOnline_Type.__name__=_C
_HhmsSensorArraySerialOnline_Object=MibTableColumn
hhmsSensorArraySerialOnline=_HhmsSensorArraySerialOnline_Object((1,3,6,1,4,1,3854,1,2,2,1,19,1,4),_HhmsSensorArraySerialOnline_Type())
hhmsSensorArraySerialOnline.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsSensorArraySerialOnline.setStatus(_A)
class _HhmsSensorArraySerialGoOnline_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_HhmsSensorArraySerialGoOnline_Type.__name__=_C
_HhmsSensorArraySerialGoOnline_Object=MibTableColumn
hhmsSensorArraySerialGoOnline=_HhmsSensorArraySerialGoOnline_Object((1,3,6,1,4,1,3854,1,2,2,1,19,1,5),_HhmsSensorArraySerialGoOnline_Type())
hhmsSensorArraySerialGoOnline.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArraySerialGoOnline.setStatus(_A)
_HhmsSensorArraySerialData_Type=DisplayString
_HhmsSensorArraySerialData_Object=MibTableColumn
hhmsSensorArraySerialData=_HhmsSensorArraySerialData_Object((1,3,6,1,4,1,3854,1,2,2,1,19,1,6),_HhmsSensorArraySerialData_Type())
hhmsSensorArraySerialData.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArraySerialData.setStatus(_A)
class _HhmsSensorArraySerialBaud_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,4,7,10,15,32,64,129,255)));namedValues=NamedValues(*(('baud115200',2),('baud57600',4),('baud38400',7),('baud28800',10),('baud19200',15),('baud9600',32),('baud4800',64),('baud2400',129),('baud1200',255)))
_HhmsSensorArraySerialBaud_Type.__name__=_C
_HhmsSensorArraySerialBaud_Object=MibTableColumn
hhmsSensorArraySerialBaud=_HhmsSensorArraySerialBaud_Object((1,3,6,1,4,1,3854,1,2,2,1,19,1,7),_HhmsSensorArraySerialBaud_Type())
hhmsSensorArraySerialBaud.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArraySerialBaud.setStatus(_A)
class _HhmsSensorArraySerialDataBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(8));namedValues=NamedValues(('eight',8))
_HhmsSensorArraySerialDataBits_Type.__name__=_C
_HhmsSensorArraySerialDataBits_Object=MibTableColumn
hhmsSensorArraySerialDataBits=_HhmsSensorArraySerialDataBits_Object((1,3,6,1,4,1,3854,1,2,2,1,19,1,8),_HhmsSensorArraySerialDataBits_Type())
hhmsSensorArraySerialDataBits.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArraySerialDataBits.setStatus(_A)
class _HhmsSensorArraySerialParity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('none',1))
_HhmsSensorArraySerialParity_Type.__name__=_C
_HhmsSensorArraySerialParity_Object=MibTableColumn
hhmsSensorArraySerialParity=_HhmsSensorArraySerialParity_Object((1,3,6,1,4,1,3854,1,2,2,1,19,1,9),_HhmsSensorArraySerialParity_Type())
hhmsSensorArraySerialParity.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArraySerialParity.setStatus(_A)
class _HhmsSensorArraySerialStop_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('one',1))
_HhmsSensorArraySerialStop_Type.__name__=_C
_HhmsSensorArraySerialStop_Object=MibTableColumn
hhmsSensorArraySerialStop=_HhmsSensorArraySerialStop_Object((1,3,6,1,4,1,3854,1,2,2,1,19,1,10),_HhmsSensorArraySerialStop_Type())
hhmsSensorArraySerialStop.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArraySerialStop.setStatus(_A)
class _HhmsSensorArraySerialCTS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_HhmsSensorArraySerialCTS_Type.__name__=_C
_HhmsSensorArraySerialCTS_Object=MibTableColumn
hhmsSensorArraySerialCTS=_HhmsSensorArraySerialCTS_Object((1,3,6,1,4,1,3854,1,2,2,1,19,1,11),_HhmsSensorArraySerialCTS_Type())
hhmsSensorArraySerialCTS.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArraySerialCTS.setStatus(_A)
class _HhmsSensorArraySerialRTS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_HhmsSensorArraySerialRTS_Type.__name__=_C
_HhmsSensorArraySerialRTS_Object=MibTableColumn
hhmsSensorArraySerialRTS=_HhmsSensorArraySerialRTS_Object((1,3,6,1,4,1,3854,1,2,2,1,19,1,12),_HhmsSensorArraySerialRTS_Type())
hhmsSensorArraySerialRTS.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArraySerialRTS.setStatus(_A)
_HhmsSensorArraySerialConfig_Type=DisplayString
_HhmsSensorArraySerialConfig_Object=MibTableColumn
hhmsSensorArraySerialConfig=_HhmsSensorArraySerialConfig_Object((1,3,6,1,4,1,3854,1,2,2,1,19,1,13),_HhmsSensorArraySerialConfig_Type())
hhmsSensorArraySerialConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArraySerialConfig.setStatus(_A)
class _HhmsSensorArraySerialIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_HhmsSensorArraySerialIndex_Type.__name__=_C
_HhmsSensorArraySerialIndex_Object=MibTableColumn
hhmsSensorArraySerialIndex=_HhmsSensorArraySerialIndex_Object((1,3,6,1,4,1,3854,1,2,2,1,19,1,14),_HhmsSensorArraySerialIndex_Type())
hhmsSensorArraySerialIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsSensorArraySerialIndex.setStatus(_A)
class _HhmsSensorArrayDebug_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_I,1)))
_HhmsSensorArrayDebug_Type.__name__=_C
_HhmsSensorArrayDebug_Object=MibScalar
hhmsSensorArrayDebug=_HhmsSensorArrayDebug_Object((1,3,6,1,4,1,3854,1,2,2,1,20),_HhmsSensorArrayDebug_Type())
hhmsSensorArrayDebug.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayDebug.setStatus(_A)
_HhmsSensorArrayDebugIP_Type=DisplayString
_HhmsSensorArrayDebugIP_Object=MibScalar
hhmsSensorArrayDebugIP=_HhmsSensorArrayDebugIP_Object((1,3,6,1,4,1,3854,1,2,2,1,21),_HhmsSensorArrayDebugIP_Type())
hhmsSensorArrayDebugIP.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayDebugIP.setStatus(_A)
class _HhmsSensorArrayTrapResend_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_I,1)))
_HhmsSensorArrayTrapResend_Type.__name__=_C
_HhmsSensorArrayTrapResend_Object=MibScalar
hhmsSensorArrayTrapResend=_HhmsSensorArrayTrapResend_Object((1,3,6,1,4,1,3854,1,2,2,1,22),_HhmsSensorArrayTrapResend_Type())
hhmsSensorArrayTrapResend.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayTrapResend.setStatus(_A)
_HhmsSensorArrayTrapResendInterval_Type=Integer32
_HhmsSensorArrayTrapResendInterval_Object=MibScalar
hhmsSensorArrayTrapResendInterval=_HhmsSensorArrayTrapResendInterval_Object((1,3,6,1,4,1,3854,1,2,2,1,23),_HhmsSensorArrayTrapResendInterval_Type())
hhmsSensorArrayTrapResendInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayTrapResendInterval.setStatus(_A)
class _HhmsSensorArraySendTraps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_HhmsSensorArraySendTraps_Type.__name__=_C
_HhmsSensorArraySendTraps_Object=MibScalar
hhmsSensorArraySendTraps=_HhmsSensorArraySendTraps_Object((1,3,6,1,4,1,3854,1,2,2,1,24),_HhmsSensorArraySendTraps_Type())
hhmsSensorArraySendTraps.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArraySendTraps.setStatus(_A)
_HhmsSensorArrayTrapDestination_Type=IpAddress
_HhmsSensorArrayTrapDestination_Object=MibScalar
hhmsSensorArrayTrapDestination=_HhmsSensorArrayTrapDestination_Object((1,3,6,1,4,1,3854,1,2,2,1,25),_HhmsSensorArrayTrapDestination_Type())
hhmsSensorArrayTrapDestination.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayTrapDestination.setStatus(_A)
_HhmsSensorArrayTrapCommunity_Type=DisplayString
_HhmsSensorArrayTrapCommunity_Object=MibScalar
hhmsSensorArrayTrapCommunity=_HhmsSensorArrayTrapCommunity_Object((1,3,6,1,4,1,3854,1,2,2,1,26),_HhmsSensorArrayTrapCommunity_Type())
hhmsSensorArrayTrapCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayTrapCommunity.setStatus(_A)
_HhmsSensorArrayTrapDefaultGateway_Type=IpAddress
_HhmsSensorArrayTrapDefaultGateway_Object=MibScalar
hhmsSensorArrayTrapDefaultGateway=_HhmsSensorArrayTrapDefaultGateway_Object((1,3,6,1,4,1,3854,1,2,2,1,27),_HhmsSensorArrayTrapDefaultGateway_Type())
hhmsSensorArrayTrapDefaultGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayTrapDefaultGateway.setStatus(_A)
class _HhmsSensorArrayTrapUseDefaultGateway_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_HhmsSensorArrayTrapUseDefaultGateway_Type.__name__=_C
_HhmsSensorArrayTrapUseDefaultGateway_Object=MibScalar
hhmsSensorArrayTrapUseDefaultGateway=_HhmsSensorArrayTrapUseDefaultGateway_Object((1,3,6,1,4,1,3854,1,2,2,1,28),_HhmsSensorArrayTrapUseDefaultGateway_Type())
hhmsSensorArrayTrapUseDefaultGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayTrapUseDefaultGateway.setStatus(_A)
_HhmsSensorArrayTrapDestinationMac_Type=DisplayString
_HhmsSensorArrayTrapDestinationMac_Object=MibScalar
hhmsSensorArrayTrapDestinationMac=_HhmsSensorArrayTrapDestinationMac_Object((1,3,6,1,4,1,3854,1,2,2,1,29),_HhmsSensorArrayTrapDestinationMac_Type())
hhmsSensorArrayTrapDestinationMac.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayTrapDestinationMac.setStatus(_A)
class _HhmsSensorArraySendMail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_HhmsSensorArraySendMail_Type.__name__=_C
_HhmsSensorArraySendMail_Object=MibScalar
hhmsSensorArraySendMail=_HhmsSensorArraySendMail_Object((1,3,6,1,4,1,3854,1,2,2,1,30),_HhmsSensorArraySendMail_Type())
hhmsSensorArraySendMail.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArraySendMail.setStatus(_A)
_HhmsSensorArrayMailRecpt_Type=DisplayString
_HhmsSensorArrayMailRecpt_Object=MibScalar
hhmsSensorArrayMailRecpt=_HhmsSensorArrayMailRecpt_Object((1,3,6,1,4,1,3854,1,2,2,1,31),_HhmsSensorArrayMailRecpt_Type())
hhmsSensorArrayMailRecpt.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayMailRecpt.setStatus(_A)
_HhmsSensorArrayMailFrom_Type=DisplayString
_HhmsSensorArrayMailFrom_Object=MibScalar
hhmsSensorArrayMailFrom=_HhmsSensorArrayMailFrom_Object((1,3,6,1,4,1,3854,1,2,2,1,32),_HhmsSensorArrayMailFrom_Type())
hhmsSensorArrayMailFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayMailFrom.setStatus(_A)
_HhmsSensorArrayMailSmpt_Type=IpAddress
_HhmsSensorArrayMailSmpt_Object=MibScalar
hhmsSensorArrayMailSmpt=_HhmsSensorArrayMailSmpt_Object((1,3,6,1,4,1,3854,1,2,2,1,33),_HhmsSensorArrayMailSmpt_Type())
hhmsSensorArrayMailSmpt.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayMailSmpt.setStatus(_A)
_HhmsSensorArrayMailGateway_Type=IpAddress
_HhmsSensorArrayMailGateway_Object=MibScalar
hhmsSensorArrayMailGateway=_HhmsSensorArrayMailGateway_Object((1,3,6,1,4,1,3854,1,2,2,1,34),_HhmsSensorArrayMailGateway_Type())
hhmsSensorArrayMailGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayMailGateway.setStatus(_A)
class _HhmsSensorArrayMailUseGateway_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_HhmsSensorArrayMailUseGateway_Type.__name__=_C
_HhmsSensorArrayMailUseGateway_Object=MibScalar
hhmsSensorArrayMailUseGateway=_HhmsSensorArrayMailUseGateway_Object((1,3,6,1,4,1,3854,1,2,2,1,35),_HhmsSensorArrayMailUseGateway_Type())
hhmsSensorArrayMailUseGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayMailUseGateway.setStatus(_A)
_HhmsSensorArrayMailResendInterval_Type=Integer32
_HhmsSensorArrayMailResendInterval_Object=MibScalar
hhmsSensorArrayMailResendInterval=_HhmsSensorArrayMailResendInterval_Object((1,3,6,1,4,1,3854,1,2,2,1,36),_HhmsSensorArrayMailResendInterval_Type())
hhmsSensorArrayMailResendInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayMailResendInterval.setStatus(_A)
_HhmsSensorArrayMailMaxResend_Type=Integer32
_HhmsSensorArrayMailMaxResend_Object=MibScalar
hhmsSensorArrayMailMaxResend=_HhmsSensorArrayMailMaxResend_Object((1,3,6,1,4,1,3854,1,2,2,1,37),_HhmsSensorArrayMailMaxResend_Type())
hhmsSensorArrayMailMaxResend.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayMailMaxResend.setStatus(_A)
_HhmsSensorArrayMailDestinationMac_Type=DisplayString
_HhmsSensorArrayMailDestinationMac_Object=MibScalar
hhmsSensorArrayMailDestinationMac=_HhmsSensorArrayMailDestinationMac_Object((1,3,6,1,4,1,3854,1,2,2,1,38),_HhmsSensorArrayMailDestinationMac_Type())
hhmsSensorArrayMailDestinationMac.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayMailDestinationMac.setStatus(_A)
_HhmsSensorArrayMailLastStatus_Type=DisplayString
_HhmsSensorArrayMailLastStatus_Object=MibScalar
hhmsSensorArrayMailLastStatus=_HhmsSensorArrayMailLastStatus_Object((1,3,6,1,4,1,3854,1,2,2,1,39),_HhmsSensorArrayMailLastStatus_Type())
hhmsSensorArrayMailLastStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsSensorArrayMailLastStatus.setStatus(_A)
_HhmsSensorArrayPowerControlTable_Object=MibTable
hhmsSensorArrayPowerControlTable=_HhmsSensorArrayPowerControlTable_Object((1,3,6,1,4,1,3854,1,2,2,1,40))
if mibBuilder.loadTexts:hhmsSensorArrayPowerControlTable.setStatus(_A)
_HhmsSensorArrayPowerControlEntry_Object=MibTableRow
hhmsSensorArrayPowerControlEntry=_HhmsSensorArrayPowerControlEntry_Object((1,3,6,1,4,1,3854,1,2,2,1,40,1))
hhmsSensorArrayPowerControlEntry.setIndexNames((0,_E,_l))
if mibBuilder.loadTexts:hhmsSensorArrayPowerControlEntry.setStatus(_A)
_HhmsSensorArrayPowerModuleDescription_Type=DisplayString
_HhmsSensorArrayPowerModuleDescription_Object=MibTableColumn
hhmsSensorArrayPowerModuleDescription=_HhmsSensorArrayPowerModuleDescription_Object((1,3,6,1,4,1,3854,1,2,2,1,40,1,1),_HhmsSensorArrayPowerModuleDescription_Type())
hhmsSensorArrayPowerModuleDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayPowerModuleDescription.setStatus(_A)
class _HhmsSensorArrayPowerModuleStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,7)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,7)))
_HhmsSensorArrayPowerModuleStatus_Type.__name__=_C
_HhmsSensorArrayPowerModuleStatus_Object=MibTableColumn
hhmsSensorArrayPowerModuleStatus=_HhmsSensorArrayPowerModuleStatus_Object((1,3,6,1,4,1,3854,1,2,2,1,40,1,2),_HhmsSensorArrayPowerModuleStatus_Type())
hhmsSensorArrayPowerModuleStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsSensorArrayPowerModuleStatus.setStatus(_A)
class _HhmsSensorArrayPowerModuleOnline_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_HhmsSensorArrayPowerModuleOnline_Type.__name__=_C
_HhmsSensorArrayPowerModuleOnline_Object=MibTableColumn
hhmsSensorArrayPowerModuleOnline=_HhmsSensorArrayPowerModuleOnline_Object((1,3,6,1,4,1,3854,1,2,2,1,40,1,3),_HhmsSensorArrayPowerModuleOnline_Type())
hhmsSensorArrayPowerModuleOnline.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsSensorArrayPowerModuleOnline.setStatus(_A)
class _HhmsSensorArrayPowerModuleGoOnline_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_HhmsSensorArrayPowerModuleGoOnline_Type.__name__=_C
_HhmsSensorArrayPowerModuleGoOnline_Object=MibTableColumn
hhmsSensorArrayPowerModuleGoOnline=_HhmsSensorArrayPowerModuleGoOnline_Object((1,3,6,1,4,1,3854,1,2,2,1,40,1,4),_HhmsSensorArrayPowerModuleGoOnline_Type())
hhmsSensorArrayPowerModuleGoOnline.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayPowerModuleGoOnline.setStatus(_A)
_HhmsSensorArrayPowerOutletDescription_Type=DisplayString
_HhmsSensorArrayPowerOutletDescription_Object=MibTableColumn
hhmsSensorArrayPowerOutletDescription=_HhmsSensorArrayPowerOutletDescription_Object((1,3,6,1,4,1,3854,1,2,2,1,40,1,5),_HhmsSensorArrayPowerOutletDescription_Type())
hhmsSensorArrayPowerOutletDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayPowerOutletDescription.setStatus(_A)
class _HhmsSensorArrayPowerOutletStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,7)));namedValues=NamedValues(*((_G,1),(_I,2),(_J,3),(_F,7)))
_HhmsSensorArrayPowerOutletStatus_Type.__name__=_C
_HhmsSensorArrayPowerOutletStatus_Object=MibTableColumn
hhmsSensorArrayPowerOutletStatus=_HhmsSensorArrayPowerOutletStatus_Object((1,3,6,1,4,1,3854,1,2,2,1,40,1,6),_HhmsSensorArrayPowerOutletStatus_Type())
hhmsSensorArrayPowerOutletStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsSensorArrayPowerOutletStatus.setStatus(_A)
class _HhmsSensorArrayPowerOutletSet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,7)));namedValues=NamedValues(*((_G,1),(_I,2),(_J,3),('reboot',4),(_F,7)))
_HhmsSensorArrayPowerOutletSet_Type.__name__=_C
_HhmsSensorArrayPowerOutletSet_Object=MibTableColumn
hhmsSensorArrayPowerOutletSet=_HhmsSensorArrayPowerOutletSet_Object((1,3,6,1,4,1,3854,1,2,2,1,40,1,7),_HhmsSensorArrayPowerOutletSet_Type())
hhmsSensorArrayPowerOutletSet.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayPowerOutletSet.setStatus(_A)
class _HhmsSensorArrayPowerControlIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_HhmsSensorArrayPowerControlIndex_Type.__name__=_C
_HhmsSensorArrayPowerControlIndex_Object=MibTableColumn
hhmsSensorArrayPowerControlIndex=_HhmsSensorArrayPowerControlIndex_Object((1,3,6,1,4,1,3854,1,2,2,1,40,1,8),_HhmsSensorArrayPowerControlIndex_Type())
hhmsSensorArrayPowerControlIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsSensorArrayPowerControlIndex.setStatus(_A)
_HhmsSensorArrayPowerMonitorTable_Object=MibTable
hhmsSensorArrayPowerMonitorTable=_HhmsSensorArrayPowerMonitorTable_Object((1,3,6,1,4,1,3854,1,2,2,1,41))
if mibBuilder.loadTexts:hhmsSensorArrayPowerMonitorTable.setStatus(_A)
_HhmsSensorArrayPowerMonitorEntry_Object=MibTableRow
hhmsSensorArrayPowerMonitorEntry=_HhmsSensorArrayPowerMonitorEntry_Object((1,3,6,1,4,1,3854,1,2,2,1,41,1))
hhmsSensorArrayPowerMonitorEntry.setIndexNames((0,_E,_m))
if mibBuilder.loadTexts:hhmsSensorArrayPowerMonitorEntry.setStatus(_A)
_HhmsSensorArrayPowerMonitorDescription_Type=DisplayString
_HhmsSensorArrayPowerMonitorDescription_Object=MibTableColumn
hhmsSensorArrayPowerMonitorDescription=_HhmsSensorArrayPowerMonitorDescription_Object((1,3,6,1,4,1,3854,1,2,2,1,41,1,1),_HhmsSensorArrayPowerMonitorDescription_Type())
hhmsSensorArrayPowerMonitorDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayPowerMonitorDescription.setStatus(_A)
_HhmsSensorArrayPowerMonitorCurrent_Type=Integer32
_HhmsSensorArrayPowerMonitorCurrent_Object=MibTableColumn
hhmsSensorArrayPowerMonitorCurrent=_HhmsSensorArrayPowerMonitorCurrent_Object((1,3,6,1,4,1,3854,1,2,2,1,41,1,2),_HhmsSensorArrayPowerMonitorCurrent_Type())
hhmsSensorArrayPowerMonitorCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayPowerMonitorCurrent.setStatus(_A)
_HhmsSensorArrayPowerMonitorVoltage_Type=Integer32
_HhmsSensorArrayPowerMonitorVoltage_Object=MibTableColumn
hhmsSensorArrayPowerMonitorVoltage=_HhmsSensorArrayPowerMonitorVoltage_Object((1,3,6,1,4,1,3854,1,2,2,1,41,1,3),_HhmsSensorArrayPowerMonitorVoltage_Type())
hhmsSensorArrayPowerMonitorVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayPowerMonitorVoltage.setStatus(_A)
_HhmsSensorArrayPowerMonitorPower_Type=DisplayString
_HhmsSensorArrayPowerMonitorPower_Object=MibTableColumn
hhmsSensorArrayPowerMonitorPower=_HhmsSensorArrayPowerMonitorPower_Object((1,3,6,1,4,1,3854,1,2,2,1,41,1,4),_HhmsSensorArrayPowerMonitorPower_Type())
hhmsSensorArrayPowerMonitorPower.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayPowerMonitorPower.setStatus(_A)
class _HhmsSensorArrayPowerMonitorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_G,1),(_H,2),(_V,3),(_W,4),(_X,5),(_Y,6),(_F,7)))
_HhmsSensorArrayPowerMonitorStatus_Type.__name__=_C
_HhmsSensorArrayPowerMonitorStatus_Object=MibTableColumn
hhmsSensorArrayPowerMonitorStatus=_HhmsSensorArrayPowerMonitorStatus_Object((1,3,6,1,4,1,3854,1,2,2,1,41,1,5),_HhmsSensorArrayPowerMonitorStatus_Type())
hhmsSensorArrayPowerMonitorStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsSensorArrayPowerMonitorStatus.setStatus(_A)
class _HhmsSensorArrayPowerMonitorOnline_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_HhmsSensorArrayPowerMonitorOnline_Type.__name__=_C
_HhmsSensorArrayPowerMonitorOnline_Object=MibTableColumn
hhmsSensorArrayPowerMonitorOnline=_HhmsSensorArrayPowerMonitorOnline_Object((1,3,6,1,4,1,3854,1,2,2,1,41,1,6),_HhmsSensorArrayPowerMonitorOnline_Type())
hhmsSensorArrayPowerMonitorOnline.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsSensorArrayPowerMonitorOnline.setStatus(_A)
class _HhmsSensorArrayPowerMonitorGoOnline_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_HhmsSensorArrayPowerMonitorGoOnline_Type.__name__=_C
_HhmsSensorArrayPowerMonitorGoOnline_Object=MibTableColumn
hhmsSensorArrayPowerMonitorGoOnline=_HhmsSensorArrayPowerMonitorGoOnline_Object((1,3,6,1,4,1,3854,1,2,2,1,41,1,7),_HhmsSensorArrayPowerMonitorGoOnline_Type())
hhmsSensorArrayPowerMonitorGoOnline.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayPowerMonitorGoOnline.setStatus(_A)
_HhmsSensorArrayPowerMonitorHighWarning_Type=Integer32
_HhmsSensorArrayPowerMonitorHighWarning_Object=MibTableColumn
hhmsSensorArrayPowerMonitorHighWarning=_HhmsSensorArrayPowerMonitorHighWarning_Object((1,3,6,1,4,1,3854,1,2,2,1,41,1,8),_HhmsSensorArrayPowerMonitorHighWarning_Type())
hhmsSensorArrayPowerMonitorHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayPowerMonitorHighWarning.setStatus(_A)
_HhmsSensorArrayPowerMonitorHighCritical_Type=Integer32
_HhmsSensorArrayPowerMonitorHighCritical_Object=MibTableColumn
hhmsSensorArrayPowerMonitorHighCritical=_HhmsSensorArrayPowerMonitorHighCritical_Object((1,3,6,1,4,1,3854,1,2,2,1,41,1,9),_HhmsSensorArrayPowerMonitorHighCritical_Type())
hhmsSensorArrayPowerMonitorHighCritical.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayPowerMonitorHighCritical.setStatus(_A)
_HhmsSensorArrayPowerMonitorLowWarning_Type=Integer32
_HhmsSensorArrayPowerMonitorLowWarning_Object=MibTableColumn
hhmsSensorArrayPowerMonitorLowWarning=_HhmsSensorArrayPowerMonitorLowWarning_Object((1,3,6,1,4,1,3854,1,2,2,1,41,1,10),_HhmsSensorArrayPowerMonitorLowWarning_Type())
hhmsSensorArrayPowerMonitorLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayPowerMonitorLowWarning.setStatus(_A)
_HhmsSensorArrayPowerMonitorLowCritical_Type=Integer32
_HhmsSensorArrayPowerMonitorLowCritical_Object=MibTableColumn
hhmsSensorArrayPowerMonitorLowCritical=_HhmsSensorArrayPowerMonitorLowCritical_Object((1,3,6,1,4,1,3854,1,2,2,1,41,1,11),_HhmsSensorArrayPowerMonitorLowCritical_Type())
hhmsSensorArrayPowerMonitorLowCritical.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayPowerMonitorLowCritical.setStatus(_A)
_HhmsSensorArrayPowerMonitorRearm_Type=Integer32
_HhmsSensorArrayPowerMonitorRearm_Object=MibTableColumn
hhmsSensorArrayPowerMonitorRearm=_HhmsSensorArrayPowerMonitorRearm_Object((1,3,6,1,4,1,3854,1,2,2,1,41,1,12),_HhmsSensorArrayPowerMonitorRearm_Type())
hhmsSensorArrayPowerMonitorRearm.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayPowerMonitorRearm.setStatus(_A)
class _HhmsSensorArrayPowerMonitorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_HhmsSensorArrayPowerMonitorIndex_Type.__name__=_C
_HhmsSensorArrayPowerMonitorIndex_Object=MibTableColumn
hhmsSensorArrayPowerMonitorIndex=_HhmsSensorArrayPowerMonitorIndex_Object((1,3,6,1,4,1,3854,1,2,2,1,41,1,13),_HhmsSensorArrayPowerMonitorIndex_Type())
hhmsSensorArrayPowerMonitorIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsSensorArrayPowerMonitorIndex.setStatus(_A)
_HhmsSensorArrayHighDriveTable_Object=MibTable
hhmsSensorArrayHighDriveTable=_HhmsSensorArrayHighDriveTable_Object((1,3,6,1,4,1,3854,1,2,2,1,42))
if mibBuilder.loadTexts:hhmsSensorArrayHighDriveTable.setStatus(_A)
_HhmsSensorArrayHighDriveEntry_Object=MibTableRow
hhmsSensorArrayHighDriveEntry=_HhmsSensorArrayHighDriveEntry_Object((1,3,6,1,4,1,3854,1,2,2,1,42,1))
hhmsSensorArrayHighDriveEntry.setIndexNames((0,_E,_n))
if mibBuilder.loadTexts:hhmsSensorArrayHighDriveEntry.setStatus(_A)
_HhmsSensorArrayHighDriveDescription_Type=DisplayString
_HhmsSensorArrayHighDriveDescription_Object=MibTableColumn
hhmsSensorArrayHighDriveDescription=_HhmsSensorArrayHighDriveDescription_Object((1,3,6,1,4,1,3854,1,2,2,1,42,1,1),_HhmsSensorArrayHighDriveDescription_Type())
hhmsSensorArrayHighDriveDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayHighDriveDescription.setStatus(_A)
class _HhmsSensorArrayHighDriveOutputLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_j,0),('open',1)))
_HhmsSensorArrayHighDriveOutputLevel_Type.__name__=_C
_HhmsSensorArrayHighDriveOutputLevel_Object=MibTableColumn
hhmsSensorArrayHighDriveOutputLevel=_HhmsSensorArrayHighDriveOutputLevel_Object((1,3,6,1,4,1,3854,1,2,2,1,42,1,2),_HhmsSensorArrayHighDriveOutputLevel_Type())
hhmsSensorArrayHighDriveOutputLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayHighDriveOutputLevel.setStatus(_A)
class _HhmsSensorArrayHighDriveIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_HhmsSensorArrayHighDriveIndex_Type.__name__=_C
_HhmsSensorArrayHighDriveIndex_Object=MibTableColumn
hhmsSensorArrayHighDriveIndex=_HhmsSensorArrayHighDriveIndex_Object((1,3,6,1,4,1,3854,1,2,2,1,42,1,3),_HhmsSensorArrayHighDriveIndex_Type())
hhmsSensorArrayHighDriveIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsSensorArrayHighDriveIndex.setStatus(_A)
_HhmsSensorArrayCameraTable_Object=MibTable
hhmsSensorArrayCameraTable=_HhmsSensorArrayCameraTable_Object((1,3,6,1,4,1,3854,1,2,2,1,43))
if mibBuilder.loadTexts:hhmsSensorArrayCameraTable.setStatus(_A)
_HhmsSensorArrayCameraEntry_Object=MibTableRow
hhmsSensorArrayCameraEntry=_HhmsSensorArrayCameraEntry_Object((1,3,6,1,4,1,3854,1,2,2,1,43,1))
hhmsSensorArrayCameraEntry.setIndexNames((0,_E,_o))
if mibBuilder.loadTexts:hhmsSensorArrayCameraEntry.setStatus(_A)
_HhmsSensorArrayCameraDescription_Type=DisplayString
_HhmsSensorArrayCameraDescription_Object=MibTableColumn
hhmsSensorArrayCameraDescription=_HhmsSensorArrayCameraDescription_Object((1,3,6,1,4,1,3854,1,2,2,1,43,1,1),_HhmsSensorArrayCameraDescription_Type())
hhmsSensorArrayCameraDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayCameraDescription.setStatus(_A)
class _HhmsSensorArrayCameraOnline_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_HhmsSensorArrayCameraOnline_Type.__name__=_C
_HhmsSensorArrayCameraOnline_Object=MibTableColumn
hhmsSensorArrayCameraOnline=_HhmsSensorArrayCameraOnline_Object((1,3,6,1,4,1,3854,1,2,2,1,43,1,2),_HhmsSensorArrayCameraOnline_Type())
hhmsSensorArrayCameraOnline.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsSensorArrayCameraOnline.setStatus(_A)
class _HhmsSensorArrayCameraGoOnline_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_HhmsSensorArrayCameraGoOnline_Type.__name__=_C
_HhmsSensorArrayCameraGoOnline_Object=MibTableColumn
hhmsSensorArrayCameraGoOnline=_HhmsSensorArrayCameraGoOnline_Object((1,3,6,1,4,1,3854,1,2,2,1,43,1,3),_HhmsSensorArrayCameraGoOnline_Type())
hhmsSensorArrayCameraGoOnline.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayCameraGoOnline.setStatus(_A)
_HhmsSensorArrayCameraUrlMain_Type=DisplayString
_HhmsSensorArrayCameraUrlMain_Object=MibTableColumn
hhmsSensorArrayCameraUrlMain=_HhmsSensorArrayCameraUrlMain_Object((1,3,6,1,4,1,3854,1,2,2,1,43,1,4),_HhmsSensorArrayCameraUrlMain_Type())
hhmsSensorArrayCameraUrlMain.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayCameraUrlMain.setStatus(_A)
_HhmsSensorArrayCameraUrlExtension_Type=DisplayString
_HhmsSensorArrayCameraUrlExtension_Object=MibTableColumn
hhmsSensorArrayCameraUrlExtension=_HhmsSensorArrayCameraUrlExtension_Object((1,3,6,1,4,1,3854,1,2,2,1,43,1,5),_HhmsSensorArrayCameraUrlExtension_Type())
hhmsSensorArrayCameraUrlExtension.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayCameraUrlExtension.setStatus(_A)
_HhmsSensorArrayCameraRefreshRate_Type=Integer32
_HhmsSensorArrayCameraRefreshRate_Object=MibTableColumn
hhmsSensorArrayCameraRefreshRate=_HhmsSensorArrayCameraRefreshRate_Object((1,3,6,1,4,1,3854,1,2,2,1,43,1,6),_HhmsSensorArrayCameraRefreshRate_Type())
hhmsSensorArrayCameraRefreshRate.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayCameraRefreshRate.setStatus(_A)
class _HhmsSensorArrayCameraIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_HhmsSensorArrayCameraIndex_Type.__name__=_C
_HhmsSensorArrayCameraIndex_Object=MibTableColumn
hhmsSensorArrayCameraIndex=_HhmsSensorArrayCameraIndex_Object((1,3,6,1,4,1,3854,1,2,2,1,43,1,7),_HhmsSensorArrayCameraIndex_Type())
hhmsSensorArrayCameraIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsSensorArrayCameraIndex.setStatus(_A)
_HhmsSensorArrayTrapMailPollInterval_Type=Integer32
_HhmsSensorArrayTrapMailPollInterval_Object=MibScalar
hhmsSensorArrayTrapMailPollInterval=_HhmsSensorArrayTrapMailPollInterval_Object((1,3,6,1,4,1,3854,1,2,2,1,50),_HhmsSensorArrayTrapMailPollInterval_Type())
hhmsSensorArrayTrapMailPollInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayTrapMailPollInterval.setStatus(_A)
_HhmsSensorArraySendTestMail_Type=Integer32
_HhmsSensorArraySendTestMail_Object=MibScalar
hhmsSensorArraySendTestMail=_HhmsSensorArraySendTestMail_Object((1,3,6,1,4,1,3854,1,2,2,1,51),_HhmsSensorArraySendTestMail_Type())
hhmsSensorArraySendTestMail.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArraySendTestMail.setStatus(_A)
_HhmsSensorArrayLastSystemError_Type=DisplayString
_HhmsSensorArrayLastSystemError_Object=MibScalar
hhmsSensorArrayLastSystemError=_HhmsSensorArrayLastSystemError_Object((1,3,6,1,4,1,3854,1,2,2,1,52),_HhmsSensorArrayLastSystemError_Type())
hhmsSensorArrayLastSystemError.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsSensorArrayLastSystemError.setStatus(_A)
_HhmsSensorArrayDataCollectionPeriod_Type=Integer32
_HhmsSensorArrayDataCollectionPeriod_Object=MibScalar
hhmsSensorArrayDataCollectionPeriod=_HhmsSensorArrayDataCollectionPeriod_Object((1,3,6,1,4,1,3854,1,2,2,1,53),_HhmsSensorArrayDataCollectionPeriod_Type())
hhmsSensorArrayDataCollectionPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayDataCollectionPeriod.setStatus(_A)
_HhmsSensorArrayMailTimeout_Type=Integer32
_HhmsSensorArrayMailTimeout_Object=MibScalar
hhmsSensorArrayMailTimeout=_HhmsSensorArrayMailTimeout_Object((1,3,6,1,4,1,3854,1,2,2,1,54),_HhmsSensorArrayMailTimeout_Type())
hhmsSensorArrayMailTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:hhmsSensorArrayMailTimeout.setStatus(_A)
_HhmsAgentConfig_ObjectIdentity=ObjectIdentity
hhmsAgentConfig=_HhmsAgentConfig_ObjectIdentity((1,3,6,1,4,1,3854,1,5))
_HhmsAgentVersion_Type=DisplayString
_HhmsAgentVersion_Object=MibScalar
hhmsAgentVersion=_HhmsAgentVersion_Object((1,3,6,1,4,1,3854,1,5,1),_HhmsAgentVersion_Type())
hhmsAgentVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsAgentVersion.setStatus(_A)
_HhmsCompressedSummaryTable_Object=MibTable
hhmsCompressedSummaryTable=_HhmsCompressedSummaryTable_Object((1,3,6,1,4,1,3854,1,5,7))
if mibBuilder.loadTexts:hhmsCompressedSummaryTable.setStatus(_A)
_HhmsCompressedSummaryEntry_Object=MibTableRow
hhmsCompressedSummaryEntry=_HhmsCompressedSummaryEntry_Object((1,3,6,1,4,1,3854,1,5,7,1))
hhmsCompressedSummaryEntry.setIndexNames((0,_E,_p))
if mibBuilder.loadTexts:hhmsCompressedSummaryEntry.setStatus(_A)
_HhmsCompressedSummaryGet_Type=DisplayString
_HhmsCompressedSummaryGet_Object=MibTableColumn
hhmsCompressedSummaryGet=_HhmsCompressedSummaryGet_Object((1,3,6,1,4,1,3854,1,5,7,1,1),_HhmsCompressedSummaryGet_Type())
hhmsCompressedSummaryGet.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsCompressedSummaryGet.setStatus(_A)
class _HhmsCompressedSummaryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_HhmsCompressedSummaryIndex_Type.__name__=_C
_HhmsCompressedSummaryIndex_Object=MibTableColumn
hhmsCompressedSummaryIndex=_HhmsCompressedSummaryIndex_Object((1,3,6,1,4,1,3854,1,5,7,1,2),_HhmsCompressedSummaryIndex_Type())
hhmsCompressedSummaryIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsCompressedSummaryIndex.setStatus(_A)
_HhmsAgentTraps_ObjectIdentity=ObjectIdentity
hhmsAgentTraps=_HhmsAgentTraps_ObjectIdentity((1,3,6,1,4,1,3854,1,7))
class _HhmsSensorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_G,1),(_H,2),(_V,3),(_W,4),(_X,5),(_Y,6),(_F,7)))
_HhmsSensorStatus_Type.__name__=_C
_HhmsSensorStatus_Object=MibScalar
hhmsSensorStatus=_HhmsSensorStatus_Object((1,3,6,1,4,1,3854,1,7,1),_HhmsSensorStatus_Type())
hhmsSensorStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsSensorStatus.setStatus(_A)
_HhmsSensorValue_Type=Integer32
_HhmsSensorValue_Object=MibScalar
hhmsSensorValue=_HhmsSensorValue_Object((1,3,6,1,4,1,3854,1,7,2),_HhmsSensorValue_Type())
hhmsSensorValue.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsSensorValue.setStatus(_A)
_HhmsSensorLevelExceeded_Type=Integer32
_HhmsSensorLevelExceeded_Object=MibScalar
hhmsSensorLevelExceeded=_HhmsSensorLevelExceeded_Object((1,3,6,1,4,1,3854,1,7,3),_HhmsSensorLevelExceeded_Type())
hhmsSensorLevelExceeded.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsSensorLevelExceeded.setStatus(_A)
_HhmsSensorIndex_Type=Integer32
_HhmsSensorIndex_Object=MibScalar
hhmsSensorIndex=_HhmsSensorIndex_Object((1,3,6,1,4,1,3854,1,7,4),_HhmsSensorIndex_Type())
hhmsSensorIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsSensorIndex.setStatus(_A)
_HhmsSensorName_Type=DisplayString
_HhmsSensorName_Object=MibScalar
hhmsSensorName=_HhmsSensorName_Object((1,3,6,1,4,1,3854,1,7,5),_HhmsSensorName_Type())
hhmsSensorName.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsSensorName.setStatus(_A)
_HhmsSensorDescription_Type=DisplayString
_HhmsSensorDescription_Object=MibScalar
hhmsSensorDescription=_HhmsSensorDescription_Object((1,3,6,1,4,1,3854,1,7,6),_HhmsSensorDescription_Type())
hhmsSensorDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:hhmsSensorDescription.setStatus(_A)
hhmsUnknownStatus=NotificationType((1,3,6,1,4,1,3854,1,0,0))
if mibBuilder.loadTexts:hhmsUnknownStatus.setStatus('')
hhmsNormalStatus=NotificationType((1,3,6,1,4,1,3854,1,0,1))
if mibBuilder.loadTexts:hhmsNormalStatus.setStatus('')
hhmsWarningStatus=NotificationType((1,3,6,1,4,1,3854,1,0,2))
if mibBuilder.loadTexts:hhmsWarningStatus.setStatus('')
hhmsCriticalStatus=NotificationType((1,3,6,1,4,1,3854,1,0,3))
if mibBuilder.loadTexts:hhmsCriticalStatus.setStatus('')
hhmsDownStatus=NotificationType((1,3,6,1,4,1,3854,1,0,4))
if mibBuilder.loadTexts:hhmsDownStatus.setStatus('')
hhmsTemperatureStatus=NotificationType((1,3,6,1,4,1,3854,1,0,10))
hhmsTemperatureStatus.setObjects(*((_E,_O),(_E,_P),(_E,_Q),(_E,_R),(_E,_S),(_E,_T)))
if mibBuilder.loadTexts:hhmsTemperatureStatus.setStatus('')
hhmsHumidityStatus=NotificationType((1,3,6,1,4,1,3854,1,0,20))
hhmsHumidityStatus.setObjects(*((_E,_O),(_E,_P),(_E,_Q),(_E,_R),(_E,_S),(_E,_T)))
if mibBuilder.loadTexts:hhmsHumidityStatus.setStatus('')
hhmsSwitchStatus=NotificationType((1,3,6,1,4,1,3854,1,0,30))
hhmsSwitchStatus.setObjects(*((_E,_O),(_E,_P),(_E,_Q),(_E,_R),(_E,_S),(_E,_T)))
if mibBuilder.loadTexts:hhmsSwitchStatus.setStatus('')
hhmsPowerMonitorStatus=NotificationType((1,3,6,1,4,1,3854,1,0,40))
hhmsPowerMonitorStatus.setObjects(*((_E,_O),(_E,_P),(_E,_Q),(_E,_R),(_E,_S),(_E,_T)))
if mibBuilder.loadTexts:hhmsPowerMonitorStatus.setStatus('')
mibBuilder.exportSymbols(_E,**{'akcp':akcp,'hhmsagent':hhmsagent,'hhmsUnknownStatus':hhmsUnknownStatus,'hhmsNormalStatus':hhmsNormalStatus,'hhmsWarningStatus':hhmsWarningStatus,'hhmsCriticalStatus':hhmsCriticalStatus,'hhmsDownStatus':hhmsDownStatus,'hhmsTemperatureStatus':hhmsTemperatureStatus,'hhmsHumidityStatus':hhmsHumidityStatus,'hhmsSwitchStatus':hhmsSwitchStatus,'hhmsPowerMonitorStatus':hhmsPowerMonitorStatus,'hhmsAgentSummary':hhmsAgentSummary,'hhmsAgentLocation':hhmsAgentLocation,'hhmsAgentStatus':hhmsAgentStatus,'hhmsNumberBadSensors':hhmsNumberBadSensors,'hhmsLocationBadSensor':hhmsLocationBadSensor,'hhmsAgentManufName':hhmsAgentManufName,'hhmsAgentHelpUrl':hhmsAgentHelpUrl,'hhmsAgentHtmlView':hhmsAgentHtmlView,'hhmsAgentHtmlStandardTitle':hhmsAgentHtmlStandardTitle,'hhmsAgentHtmlStandardButton':hhmsAgentHtmlStandardButton,'hhmsSensor':hhmsSensor,'hhmsSensorArrayTable':hhmsSensorArrayTable,'hhmsSensorArrayEntry':hhmsSensorArrayEntry,'hhmsSensorArrayHost':hhmsSensorArrayHost,'hhmsSensorArrayUseDHCP':hhmsSensorArrayUseDHCP,'hhmsSensorArrayMAC':hhmsSensorArrayMAC,'hhmsSensorArraySetCommunity':hhmsSensorArraySetCommunity,'hhmsSensorArrayGetCommunity':hhmsSensorArrayGetCommunity,'hhmsSensorArrayDescription':hhmsSensorArrayDescription,'hhmsSensorArrayLocation':hhmsSensorArrayLocation,'hhmsSensorArrayLastUpdate':hhmsSensorArrayLastUpdate,'hhmsSensorArrayStatus':hhmsSensorArrayStatus,'hhmsSensorArrayOnline':hhmsSensorArrayOnline,'hhmsSensorArrayGoOnline':hhmsSensorArrayGoOnline,'hhmsSensorArrayReadInterval':hhmsSensorArrayReadInterval,'hhmsSensorArrayReceiveTimeout':hhmsSensorArrayReceiveTimeout,'hhmsSensorArrayReceiveRetries':hhmsSensorArrayReceiveRetries,'hhmsSensorArrayVersion':hhmsSensorArrayVersion,'hhmsSensorArrayTempTable':hhmsSensorArrayTempTable,'hhmsSensorArrayTempEntry':hhmsSensorArrayTempEntry,'hhmsSensorArrayTempDescription':hhmsSensorArrayTempDescription,'hhmsSensorArrayTempLocation':hhmsSensorArrayTempLocation,'hhmsSensorArrayTempDegree':hhmsSensorArrayTempDegree,'hhmsSensorArrayTempStatus':hhmsSensorArrayTempStatus,'hhmsSensorArrayTempOnline':hhmsSensorArrayTempOnline,'hhmsSensorArrayTempGoOnline':hhmsSensorArrayTempGoOnline,'hhmsSensorArrayTempHighWarning':hhmsSensorArrayTempHighWarning,'hhmsSensorArrayTempHighCritical':hhmsSensorArrayTempHighCritical,'hhmsSensorArrayTempLowWarning':hhmsSensorArrayTempLowWarning,'hhmsSensorArrayTempLowCritical':hhmsSensorArrayTempLowCritical,'hhmsSensorArrayTempRearm':hhmsSensorArrayTempRearm,'hhmsSensorArrayTempDegreeType':hhmsSensorArrayTempDegreeType,'hhmsSensorArrayTempSensorType':hhmsSensorArrayTempSensorType,'hhmsSensorArrayTempTestStatus':hhmsSensorArrayTempTestStatus,'hhmsSensorArrayTempTestDegree':hhmsSensorArrayTempTestDegree,_a:hhmsSensorArrayTempIndex,'hhmsSensorArrayHumidityTable':hhmsSensorArrayHumidityTable,'hhmsSensorArrayHumidityEntry':hhmsSensorArrayHumidityEntry,'hhmsSensorArrayHumidityDescription':hhmsSensorArrayHumidityDescription,'hhmsSensorArrayHumidityLocation':hhmsSensorArrayHumidityLocation,'hhmsSensorArrayHumidityPercent':hhmsSensorArrayHumidityPercent,'hhmsSensorArrayHumidityStatus':hhmsSensorArrayHumidityStatus,'hhmsSensorArrayHumidityOnline':hhmsSensorArrayHumidityOnline,'hhmsSensorArrayHumidityGoOnline':hhmsSensorArrayHumidityGoOnline,'hhmsSensorArrayHumidityHighWarning':hhmsSensorArrayHumidityHighWarning,'hhmsSensorArrayHumidityHighCritical':hhmsSensorArrayHumidityHighCritical,'hhmsSensorArrayHumidityLowWarning':hhmsSensorArrayHumidityLowWarning,'hhmsSensorArrayHumidityLowCritical':hhmsSensorArrayHumidityLowCritical,'hhmsSensorArrayHumidityRearm':hhmsSensorArrayHumidityRearm,'hhmsSensorArrayHumidityTestStatus':hhmsSensorArrayHumidityTestStatus,'hhmsSensorArrayHumidityTestPercent':hhmsSensorArrayHumidityTestPercent,_h:hhmsSensorArrayHumidityIndex,'hhmsSensorArraySwitchTable':hhmsSensorArraySwitchTable,'hhmsSensorArraySwitchEntry':hhmsSensorArraySwitchEntry,'hhmsSensorArraySwitchDescription':hhmsSensorArraySwitchDescription,'hhmsSensorArraySwitchLocation':hhmsSensorArraySwitchLocation,'hhmsSensorArraySwitchStatus':hhmsSensorArraySwitchStatus,'hhmsSensorArraySwitchOnline':hhmsSensorArraySwitchOnline,'hhmsSensorArraySwitchGoOnline':hhmsSensorArraySwitchGoOnline,'hhmsSensorArraySwitchDirection':hhmsSensorArraySwitchDirection,'hhmsSensorArraySwitchNormalState':hhmsSensorArraySwitchNormalState,'hhmsSensorArraySwitchOutputLevel':hhmsSensorArraySwitchOutputLevel,'hhmsSensorArraySwitchTestState':hhmsSensorArraySwitchTestState,_i:hhmsSensorArraySwitchIndex,'hhmsSensorArraySerialTable':hhmsSensorArraySerialTable,'hhmsSensorArraySerialEntry':hhmsSensorArraySerialEntry,'hhmsSensorArraySerialDescription':hhmsSensorArraySerialDescription,'hhmsSensorArraySerialLocation':hhmsSensorArraySerialLocation,'hhmsSensorArraySerialStatus':hhmsSensorArraySerialStatus,'hhmsSensorArraySerialOnline':hhmsSensorArraySerialOnline,'hhmsSensorArraySerialGoOnline':hhmsSensorArraySerialGoOnline,'hhmsSensorArraySerialData':hhmsSensorArraySerialData,'hhmsSensorArraySerialBaud':hhmsSensorArraySerialBaud,'hhmsSensorArraySerialDataBits':hhmsSensorArraySerialDataBits,'hhmsSensorArraySerialParity':hhmsSensorArraySerialParity,'hhmsSensorArraySerialStop':hhmsSensorArraySerialStop,'hhmsSensorArraySerialCTS':hhmsSensorArraySerialCTS,'hhmsSensorArraySerialRTS':hhmsSensorArraySerialRTS,'hhmsSensorArraySerialConfig':hhmsSensorArraySerialConfig,_k:hhmsSensorArraySerialIndex,'hhmsSensorArrayDebug':hhmsSensorArrayDebug,'hhmsSensorArrayDebugIP':hhmsSensorArrayDebugIP,'hhmsSensorArrayTrapResend':hhmsSensorArrayTrapResend,'hhmsSensorArrayTrapResendInterval':hhmsSensorArrayTrapResendInterval,'hhmsSensorArraySendTraps':hhmsSensorArraySendTraps,'hhmsSensorArrayTrapDestination':hhmsSensorArrayTrapDestination,'hhmsSensorArrayTrapCommunity':hhmsSensorArrayTrapCommunity,'hhmsSensorArrayTrapDefaultGateway':hhmsSensorArrayTrapDefaultGateway,'hhmsSensorArrayTrapUseDefaultGateway':hhmsSensorArrayTrapUseDefaultGateway,'hhmsSensorArrayTrapDestinationMac':hhmsSensorArrayTrapDestinationMac,'hhmsSensorArraySendMail':hhmsSensorArraySendMail,'hhmsSensorArrayMailRecpt':hhmsSensorArrayMailRecpt,'hhmsSensorArrayMailFrom':hhmsSensorArrayMailFrom,'hhmsSensorArrayMailSmpt':hhmsSensorArrayMailSmpt,'hhmsSensorArrayMailGateway':hhmsSensorArrayMailGateway,'hhmsSensorArrayMailUseGateway':hhmsSensorArrayMailUseGateway,'hhmsSensorArrayMailResendInterval':hhmsSensorArrayMailResendInterval,'hhmsSensorArrayMailMaxResend':hhmsSensorArrayMailMaxResend,'hhmsSensorArrayMailDestinationMac':hhmsSensorArrayMailDestinationMac,'hhmsSensorArrayMailLastStatus':hhmsSensorArrayMailLastStatus,'hhmsSensorArrayPowerControlTable':hhmsSensorArrayPowerControlTable,'hhmsSensorArrayPowerControlEntry':hhmsSensorArrayPowerControlEntry,'hhmsSensorArrayPowerModuleDescription':hhmsSensorArrayPowerModuleDescription,'hhmsSensorArrayPowerModuleStatus':hhmsSensorArrayPowerModuleStatus,'hhmsSensorArrayPowerModuleOnline':hhmsSensorArrayPowerModuleOnline,'hhmsSensorArrayPowerModuleGoOnline':hhmsSensorArrayPowerModuleGoOnline,'hhmsSensorArrayPowerOutletDescription':hhmsSensorArrayPowerOutletDescription,'hhmsSensorArrayPowerOutletStatus':hhmsSensorArrayPowerOutletStatus,'hhmsSensorArrayPowerOutletSet':hhmsSensorArrayPowerOutletSet,_l:hhmsSensorArrayPowerControlIndex,'hhmsSensorArrayPowerMonitorTable':hhmsSensorArrayPowerMonitorTable,'hhmsSensorArrayPowerMonitorEntry':hhmsSensorArrayPowerMonitorEntry,'hhmsSensorArrayPowerMonitorDescription':hhmsSensorArrayPowerMonitorDescription,'hhmsSensorArrayPowerMonitorCurrent':hhmsSensorArrayPowerMonitorCurrent,'hhmsSensorArrayPowerMonitorVoltage':hhmsSensorArrayPowerMonitorVoltage,'hhmsSensorArrayPowerMonitorPower':hhmsSensorArrayPowerMonitorPower,'hhmsSensorArrayPowerMonitorStatus':hhmsSensorArrayPowerMonitorStatus,'hhmsSensorArrayPowerMonitorOnline':hhmsSensorArrayPowerMonitorOnline,'hhmsSensorArrayPowerMonitorGoOnline':hhmsSensorArrayPowerMonitorGoOnline,'hhmsSensorArrayPowerMonitorHighWarning':hhmsSensorArrayPowerMonitorHighWarning,'hhmsSensorArrayPowerMonitorHighCritical':hhmsSensorArrayPowerMonitorHighCritical,'hhmsSensorArrayPowerMonitorLowWarning':hhmsSensorArrayPowerMonitorLowWarning,'hhmsSensorArrayPowerMonitorLowCritical':hhmsSensorArrayPowerMonitorLowCritical,'hhmsSensorArrayPowerMonitorRearm':hhmsSensorArrayPowerMonitorRearm,_m:hhmsSensorArrayPowerMonitorIndex,'hhmsSensorArrayHighDriveTable':hhmsSensorArrayHighDriveTable,'hhmsSensorArrayHighDriveEntry':hhmsSensorArrayHighDriveEntry,'hhmsSensorArrayHighDriveDescription':hhmsSensorArrayHighDriveDescription,'hhmsSensorArrayHighDriveOutputLevel':hhmsSensorArrayHighDriveOutputLevel,_n:hhmsSensorArrayHighDriveIndex,'hhmsSensorArrayCameraTable':hhmsSensorArrayCameraTable,'hhmsSensorArrayCameraEntry':hhmsSensorArrayCameraEntry,'hhmsSensorArrayCameraDescription':hhmsSensorArrayCameraDescription,'hhmsSensorArrayCameraOnline':hhmsSensorArrayCameraOnline,'hhmsSensorArrayCameraGoOnline':hhmsSensorArrayCameraGoOnline,'hhmsSensorArrayCameraUrlMain':hhmsSensorArrayCameraUrlMain,'hhmsSensorArrayCameraUrlExtension':hhmsSensorArrayCameraUrlExtension,'hhmsSensorArrayCameraRefreshRate':hhmsSensorArrayCameraRefreshRate,_o:hhmsSensorArrayCameraIndex,'hhmsSensorArrayTrapMailPollInterval':hhmsSensorArrayTrapMailPollInterval,'hhmsSensorArraySendTestMail':hhmsSensorArraySendTestMail,'hhmsSensorArrayLastSystemError':hhmsSensorArrayLastSystemError,'hhmsSensorArrayDataCollectionPeriod':hhmsSensorArrayDataCollectionPeriod,'hhmsSensorArrayMailTimeout':hhmsSensorArrayMailTimeout,'hhmsAgentConfig':hhmsAgentConfig,'hhmsAgentVersion':hhmsAgentVersion,'hhmsCompressedSummaryTable':hhmsCompressedSummaryTable,'hhmsCompressedSummaryEntry':hhmsCompressedSummaryEntry,'hhmsCompressedSummaryGet':hhmsCompressedSummaryGet,_p:hhmsCompressedSummaryIndex,'hhmsAgentTraps':hhmsAgentTraps,_O:hhmsSensorStatus,_P:hhmsSensorValue,_Q:hhmsSensorLevelExceeded,_R:hhmsSensorIndex,_S:hhmsSensorName,_T:hhmsSensorDescription})