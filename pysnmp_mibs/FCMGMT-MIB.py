_z='connUnitPortState'
_y='connUnitPortStatus'
_x='connUnitSensorStatus'
_w='connUnitEventDescr'
_v='connUnitEventObject'
_u='connUnitEventType'
_t='connUnitEventId'
_s='connUnitState'
_r='connUnitStatus'
_q='connUnitPlatformNodeIndex'
_p='connUnitPlatformIndex'
_o='connUnitSnsPortIdentifier'
_n='connUnitSnsPortName'
_m='connUnitSnsId'
_l='connUnitPortStatIndex'
_k='connUnitPortStatUnitId'
_j='trapRegPort'
_i='trapRegIpAddress'
_h='connUnitZoningAliasMemberIndex'
_g='connUnitZoningAliasIndex'
_f='connUnitZoneMemberIndex'
_e='connUnitZoneIndex'
_d='connUnitLinkIndex'
_c='connUnitLinkUnitId'
_b='connUnitEventIndex'
_a='connUnitEventUnitId'
_Z='deprecated'
_Y='bypassed'
_X='connUnitPortIndex'
_W='connUnitPortUnitId'
_V='connUnitSensorIndex'
_U='connUnitSensorUnitId'
_T='connUnitRevsIndex'
_S='connUnitRevsUnitId'
_R='invalid'
_Q='offline'
_P='online'
_O='NotificationType'
_N='failed'
_M='unused'
_L='connUnitId'
_K='warning'
_J='obsolete'
_I='other'
_H='read-write'
_G='unknown'
_F='DisplayString'
_E='Integer32'
_D='FCMGMT-MIB'
_C='OctetString'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,experimental,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier',_O,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_O,'TimeTicks','Unsigned32','experimental','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
class FcNameId(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class FcGlobalId(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
class FcAddressId(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
class FcEventSeverity(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_G,1),('emergency',2),('alert',3),('critical',4),('error',5),(_K,6),('notify',7),('info',8),('debug',9),('mark',10)))
class FcUnitType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*((_G,1),(_I,2),('hub',3),('switch',4),('gateway',5),('converter',6),('hba',7),('proxy-agent',8),('storage-device',9),('host',10),('storage-subsystem',11),('module',12),('swdriver',13),('storage-access-device',14),('wdm',15),('ups',16),('nas',17)))
_Fcmgmt_ObjectIdentity=ObjectIdentity
fcmgmt=_Fcmgmt_ObjectIdentity((1,3,6,1,3,94))
_ConnSet_ObjectIdentity=ObjectIdentity
connSet=_ConnSet_ObjectIdentity((1,3,6,1,3,94,1))
class _UNumber_Type(Integer32):defaultValue=1
_UNumber_Type.__name__=_E
_UNumber_Object=MibScalar
uNumber=_UNumber_Object((1,3,6,1,3,94,1,1),_UNumber_Type())
uNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:uNumber.setStatus(_A)
class _SystemURL_Type(DisplayString):defaultValue=OctetString('')
_SystemURL_Type.__name__=_F
_SystemURL_Object=MibScalar
systemURL=_SystemURL_Object((1,3,6,1,3,94,1,2),_SystemURL_Type())
systemURL.setMaxAccess(_H)
if mibBuilder.loadTexts:systemURL.setStatus(_A)
_StatusChangeTime_Type=TimeTicks
_StatusChangeTime_Object=MibScalar
statusChangeTime=_StatusChangeTime_Object((1,3,6,1,3,94,1,3),_StatusChangeTime_Type())
statusChangeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:statusChangeTime.setStatus(_J)
_ConfigurationChangeTime_Type=TimeTicks
_ConfigurationChangeTime_Object=MibScalar
configurationChangeTime=_ConfigurationChangeTime_Object((1,3,6,1,3,94,1,4),_ConfigurationChangeTime_Type())
configurationChangeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:configurationChangeTime.setStatus(_J)
_ConnUnitTableChangeTime_Type=TimeTicks
_ConnUnitTableChangeTime_Object=MibScalar
connUnitTableChangeTime=_ConnUnitTableChangeTime_Object((1,3,6,1,3,94,1,5),_ConnUnitTableChangeTime_Type())
connUnitTableChangeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitTableChangeTime.setStatus(_J)
_ConnUnitTable_Object=MibTable
connUnitTable=_ConnUnitTable_Object((1,3,6,1,3,94,1,6))
if mibBuilder.loadTexts:connUnitTable.setStatus(_A)
_ConnUnitEntry_Object=MibTableRow
connUnitEntry=_ConnUnitEntry_Object((1,3,6,1,3,94,1,6,1))
connUnitEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:connUnitEntry.setStatus(_A)
_ConnUnitId_Type=FcGlobalId
_ConnUnitId_Object=MibTableColumn
connUnitId=_ConnUnitId_Object((1,3,6,1,3,94,1,6,1,1),_ConnUnitId_Type())
connUnitId.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitId.setStatus(_A)
_ConnUnitGlobalId_Type=FcGlobalId
_ConnUnitGlobalId_Object=MibTableColumn
connUnitGlobalId=_ConnUnitGlobalId_Object((1,3,6,1,3,94,1,6,1,2),_ConnUnitGlobalId_Type())
connUnitGlobalId.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitGlobalId.setStatus(_A)
_ConnUnitType_Type=FcUnitType
_ConnUnitType_Object=MibTableColumn
connUnitType=_ConnUnitType_Object((1,3,6,1,3,94,1,6,1,3),_ConnUnitType_Type())
connUnitType.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitType.setStatus(_A)
_ConnUnitNumports_Type=Integer32
_ConnUnitNumports_Object=MibTableColumn
connUnitNumports=_ConnUnitNumports_Object((1,3,6,1,3,94,1,6,1,4),_ConnUnitNumports_Type())
connUnitNumports.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitNumports.setStatus(_A)
class _ConnUnitState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_P,2),(_Q,3)))
_ConnUnitState_Type.__name__=_E
_ConnUnitState_Object=MibTableColumn
connUnitState=_ConnUnitState_Object((1,3,6,1,3,94,1,6,1,5),_ConnUnitState_Type())
connUnitState.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitState.setStatus(_A)
class _ConnUnitStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_G,1),(_M,2),('ok',3),(_K,4),(_N,5)))
_ConnUnitStatus_Type.__name__=_E
_ConnUnitStatus_Object=MibTableColumn
connUnitStatus=_ConnUnitStatus_Object((1,3,6,1,3,94,1,6,1,6),_ConnUnitStatus_Type())
connUnitStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitStatus.setStatus(_A)
class _ConnUnitProduct_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_ConnUnitProduct_Type.__name__=_F
_ConnUnitProduct_Object=MibTableColumn
connUnitProduct=_ConnUnitProduct_Object((1,3,6,1,3,94,1,6,1,7),_ConnUnitProduct_Type())
connUnitProduct.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitProduct.setStatus(_A)
class _ConnUnitSn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_ConnUnitSn_Type.__name__=_F
_ConnUnitSn_Object=MibTableColumn
connUnitSn=_ConnUnitSn_Object((1,3,6,1,3,94,1,6,1,8),_ConnUnitSn_Type())
connUnitSn.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitSn.setStatus(_A)
_ConnUnitUpTime_Type=TimeTicks
_ConnUnitUpTime_Object=MibTableColumn
connUnitUpTime=_ConnUnitUpTime_Object((1,3,6,1,3,94,1,6,1,9),_ConnUnitUpTime_Type())
connUnitUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitUpTime.setStatus(_A)
_ConnUnitUrl_Type=DisplayString
_ConnUnitUrl_Object=MibTableColumn
connUnitUrl=_ConnUnitUrl_Object((1,3,6,1,3,94,1,6,1,10),_ConnUnitUrl_Type())
connUnitUrl.setMaxAccess(_H)
if mibBuilder.loadTexts:connUnitUrl.setStatus(_A)
class _ConnUnitDomainId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_ConnUnitDomainId_Type.__name__=_C
_ConnUnitDomainId_Object=MibTableColumn
connUnitDomainId=_ConnUnitDomainId_Object((1,3,6,1,3,94,1,6,1,11),_ConnUnitDomainId_Type())
connUnitDomainId.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitDomainId.setStatus(_A)
class _ConnUnitProxyMaster_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('no',2),('yes',3)))
_ConnUnitProxyMaster_Type.__name__=_E
_ConnUnitProxyMaster_Object=MibTableColumn
connUnitProxyMaster=_ConnUnitProxyMaster_Object((1,3,6,1,3,94,1,6,1,12),_ConnUnitProxyMaster_Type())
connUnitProxyMaster.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitProxyMaster.setStatus(_A)
class _ConnUnitPrincipal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('no',2),('yes',3)))
_ConnUnitPrincipal_Type.__name__=_E
_ConnUnitPrincipal_Object=MibTableColumn
connUnitPrincipal=_ConnUnitPrincipal_Object((1,3,6,1,3,94,1,6,1,13),_ConnUnitPrincipal_Type())
connUnitPrincipal.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPrincipal.setStatus(_A)
_ConnUnitNumSensors_Type=Integer32
_ConnUnitNumSensors_Object=MibTableColumn
connUnitNumSensors=_ConnUnitNumSensors_Object((1,3,6,1,3,94,1,6,1,14),_ConnUnitNumSensors_Type())
connUnitNumSensors.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitNumSensors.setStatus(_A)
_ConnUnitStatusChangeTime_Type=TimeTicks
_ConnUnitStatusChangeTime_Object=MibTableColumn
connUnitStatusChangeTime=_ConnUnitStatusChangeTime_Object((1,3,6,1,3,94,1,6,1,15),_ConnUnitStatusChangeTime_Type())
connUnitStatusChangeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitStatusChangeTime.setStatus(_J)
_ConnUnitConfigurationChangeTime_Type=TimeTicks
_ConnUnitConfigurationChangeTime_Object=MibTableColumn
connUnitConfigurationChangeTime=_ConnUnitConfigurationChangeTime_Object((1,3,6,1,3,94,1,6,1,16),_ConnUnitConfigurationChangeTime_Type())
connUnitConfigurationChangeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitConfigurationChangeTime.setStatus(_J)
class _ConnUnitNumRevs_Type(Integer32):defaultValue=1
_ConnUnitNumRevs_Type.__name__=_E
_ConnUnitNumRevs_Object=MibTableColumn
connUnitNumRevs=_ConnUnitNumRevs_Object((1,3,6,1,3,94,1,6,1,17),_ConnUnitNumRevs_Type())
connUnitNumRevs.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitNumRevs.setStatus(_A)
_ConnUnitNumZones_Type=Integer32
_ConnUnitNumZones_Object=MibTableColumn
connUnitNumZones=_ConnUnitNumZones_Object((1,3,6,1,3,94,1,6,1,18),_ConnUnitNumZones_Type())
connUnitNumZones.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitNumZones.setStatus(_J)
_ConnUnitModuleId_Type=FcGlobalId
_ConnUnitModuleId_Object=MibTableColumn
connUnitModuleId=_ConnUnitModuleId_Object((1,3,6,1,3,94,1,6,1,19),_ConnUnitModuleId_Type())
connUnitModuleId.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitModuleId.setStatus(_A)
class _ConnUnitName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_ConnUnitName_Type.__name__=_F
_ConnUnitName_Object=MibTableColumn
connUnitName=_ConnUnitName_Object((1,3,6,1,3,94,1,6,1,20),_ConnUnitName_Type())
connUnitName.setMaxAccess(_H)
if mibBuilder.loadTexts:connUnitName.setStatus(_A)
_ConnUnitInfo_Type=DisplayString
_ConnUnitInfo_Object=MibTableColumn
connUnitInfo=_ConnUnitInfo_Object((1,3,6,1,3,94,1,6,1,21),_ConnUnitInfo_Type())
connUnitInfo.setMaxAccess(_H)
if mibBuilder.loadTexts:connUnitInfo.setStatus(_A)
class _ConnUnitControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_G,1),(_R,2),('resetConnUnitColdStart',3),('resetConnUnitWarmStart',4),('offlineConnUnit',5),('onlineConnUnit',6)))
_ConnUnitControl_Type.__name__=_E
_ConnUnitControl_Object=MibTableColumn
connUnitControl=_ConnUnitControl_Object((1,3,6,1,3,94,1,6,1,22),_ConnUnitControl_Type())
connUnitControl.setMaxAccess(_H)
if mibBuilder.loadTexts:connUnitControl.setStatus(_A)
class _ConnUnitContact_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_ConnUnitContact_Type.__name__=_F
_ConnUnitContact_Object=MibTableColumn
connUnitContact=_ConnUnitContact_Object((1,3,6,1,3,94,1,6,1,23),_ConnUnitContact_Type())
connUnitContact.setMaxAccess(_H)
if mibBuilder.loadTexts:connUnitContact.setStatus(_A)
class _ConnUnitLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_ConnUnitLocation_Type.__name__=_F
_ConnUnitLocation_Object=MibTableColumn
connUnitLocation=_ConnUnitLocation_Object((1,3,6,1,3,94,1,6,1,24),_ConnUnitLocation_Type())
connUnitLocation.setMaxAccess(_H)
if mibBuilder.loadTexts:connUnitLocation.setStatus(_A)
_ConnUnitEventFilter_Type=FcEventSeverity
_ConnUnitEventFilter_Object=MibTableColumn
connUnitEventFilter=_ConnUnitEventFilter_Object((1,3,6,1,3,94,1,6,1,25),_ConnUnitEventFilter_Type())
connUnitEventFilter.setMaxAccess(_H)
if mibBuilder.loadTexts:connUnitEventFilter.setStatus(_A)
_ConnUnitNumEvents_Type=Integer32
_ConnUnitNumEvents_Object=MibTableColumn
connUnitNumEvents=_ConnUnitNumEvents_Object((1,3,6,1,3,94,1,6,1,26),_ConnUnitNumEvents_Type())
connUnitNumEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitNumEvents.setStatus(_A)
_ConnUnitMaxEvents_Type=Integer32
_ConnUnitMaxEvents_Object=MibTableColumn
connUnitMaxEvents=_ConnUnitMaxEvents_Object((1,3,6,1,3,94,1,6,1,27),_ConnUnitMaxEvents_Type())
connUnitMaxEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitMaxEvents.setStatus(_A)
_ConnUnitEventCurrID_Type=Integer32
_ConnUnitEventCurrID_Object=MibTableColumn
connUnitEventCurrID=_ConnUnitEventCurrID_Object((1,3,6,1,3,94,1,6,1,28),_ConnUnitEventCurrID_Type())
connUnitEventCurrID.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitEventCurrID.setStatus(_A)
_ConnUnitFabricID_Type=FcGlobalId
_ConnUnitFabricID_Object=MibTableColumn
connUnitFabricID=_ConnUnitFabricID_Object((1,3,6,1,3,94,1,6,1,29),_ConnUnitFabricID_Type())
connUnitFabricID.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitFabricID.setStatus(_A)
_ConnUnitNumLinks_Type=Integer32
_ConnUnitNumLinks_Object=MibTableColumn
connUnitNumLinks=_ConnUnitNumLinks_Object((1,3,6,1,3,94,1,6,1,30),_ConnUnitNumLinks_Type())
connUnitNumLinks.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitNumLinks.setStatus(_A)
class _ConnUnitVendorId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_ConnUnitVendorId_Type.__name__=_F
_ConnUnitVendorId_Object=MibTableColumn
connUnitVendorId=_ConnUnitVendorId_Object((1,3,6,1,3,94,1,6,1,31),_ConnUnitVendorId_Type())
connUnitVendorId.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitVendorId.setStatus(_A)
_ConnUnitRevsTable_Object=MibTable
connUnitRevsTable=_ConnUnitRevsTable_Object((1,3,6,1,3,94,1,7))
if mibBuilder.loadTexts:connUnitRevsTable.setStatus(_A)
_ConnUnitRevsEntry_Object=MibTableRow
connUnitRevsEntry=_ConnUnitRevsEntry_Object((1,3,6,1,3,94,1,7,1))
connUnitRevsEntry.setIndexNames((0,_D,_S),(0,_D,_T))
if mibBuilder.loadTexts:connUnitRevsEntry.setStatus(_A)
_ConnUnitRevsUnitId_Type=FcGlobalId
_ConnUnitRevsUnitId_Object=MibTableColumn
connUnitRevsUnitId=_ConnUnitRevsUnitId_Object((1,3,6,1,3,94,1,7,1,1),_ConnUnitRevsUnitId_Type())
connUnitRevsUnitId.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitRevsUnitId.setStatus(_A)
class _ConnUnitRevsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ConnUnitRevsIndex_Type.__name__=_E
_ConnUnitRevsIndex_Object=MibTableColumn
connUnitRevsIndex=_ConnUnitRevsIndex_Object((1,3,6,1,3,94,1,7,1,2),_ConnUnitRevsIndex_Type())
connUnitRevsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitRevsIndex.setStatus(_A)
_ConnUnitRevsRevId_Type=DisplayString
_ConnUnitRevsRevId_Object=MibTableColumn
connUnitRevsRevId=_ConnUnitRevsRevId_Object((1,3,6,1,3,94,1,7,1,3),_ConnUnitRevsRevId_Type())
connUnitRevsRevId.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitRevsRevId.setStatus(_A)
_ConnUnitRevsDescription_Type=DisplayString
_ConnUnitRevsDescription_Object=MibTableColumn
connUnitRevsDescription=_ConnUnitRevsDescription_Object((1,3,6,1,3,94,1,7,1,4),_ConnUnitRevsDescription_Type())
connUnitRevsDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitRevsDescription.setStatus(_A)
_ConnUnitSensorTable_Object=MibTable
connUnitSensorTable=_ConnUnitSensorTable_Object((1,3,6,1,3,94,1,8))
if mibBuilder.loadTexts:connUnitSensorTable.setStatus(_A)
_ConnUnitSensorEntry_Object=MibTableRow
connUnitSensorEntry=_ConnUnitSensorEntry_Object((1,3,6,1,3,94,1,8,1))
connUnitSensorEntry.setIndexNames((0,_D,_U),(0,_D,_V))
if mibBuilder.loadTexts:connUnitSensorEntry.setStatus(_A)
_ConnUnitSensorUnitId_Type=FcGlobalId
_ConnUnitSensorUnitId_Object=MibTableColumn
connUnitSensorUnitId=_ConnUnitSensorUnitId_Object((1,3,6,1,3,94,1,8,1,1),_ConnUnitSensorUnitId_Type())
connUnitSensorUnitId.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitSensorUnitId.setStatus(_A)
class _ConnUnitSensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ConnUnitSensorIndex_Type.__name__=_E
_ConnUnitSensorIndex_Object=MibTableColumn
connUnitSensorIndex=_ConnUnitSensorIndex_Object((1,3,6,1,3,94,1,8,1,2),_ConnUnitSensorIndex_Type())
connUnitSensorIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitSensorIndex.setStatus(_A)
_ConnUnitSensorName_Type=DisplayString
_ConnUnitSensorName_Object=MibTableColumn
connUnitSensorName=_ConnUnitSensorName_Object((1,3,6,1,3,94,1,8,1,3),_ConnUnitSensorName_Type())
connUnitSensorName.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitSensorName.setStatus(_A)
class _ConnUnitSensorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_G,1),(_I,2),('ok',3),(_K,4),(_N,5)))
_ConnUnitSensorStatus_Type.__name__=_E
_ConnUnitSensorStatus_Object=MibTableColumn
connUnitSensorStatus=_ConnUnitSensorStatus_Object((1,3,6,1,3,94,1,8,1,4),_ConnUnitSensorStatus_Type())
connUnitSensorStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitSensorStatus.setStatus(_A)
_ConnUnitSensorInfo_Type=DisplayString
_ConnUnitSensorInfo_Object=MibTableColumn
connUnitSensorInfo=_ConnUnitSensorInfo_Object((1,3,6,1,3,94,1,8,1,5),_ConnUnitSensorInfo_Type())
connUnitSensorInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitSensorInfo.setStatus(_A)
_ConnUnitSensorMessage_Type=DisplayString
_ConnUnitSensorMessage_Object=MibTableColumn
connUnitSensorMessage=_ConnUnitSensorMessage_Object((1,3,6,1,3,94,1,8,1,6),_ConnUnitSensorMessage_Type())
connUnitSensorMessage.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitSensorMessage.setStatus(_A)
class _ConnUnitSensorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_G,1),(_I,2),('battery',3),('fan',4),('power-supply',5),('transmitter',6),('enclosure',7),('board',8),('receiver',9)))
_ConnUnitSensorType_Type.__name__=_E
_ConnUnitSensorType_Object=MibTableColumn
connUnitSensorType=_ConnUnitSensorType_Object((1,3,6,1,3,94,1,8,1,7),_ConnUnitSensorType_Type())
connUnitSensorType.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitSensorType.setStatus(_A)
class _ConnUnitSensorCharacteristic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_G,1),(_I,2),('temperature',3),('pressure',4),('emf',5),('currentValue',6),('airflow',7),('frequency',8),('power',9),('door',10)))
_ConnUnitSensorCharacteristic_Type.__name__=_E
_ConnUnitSensorCharacteristic_Object=MibTableColumn
connUnitSensorCharacteristic=_ConnUnitSensorCharacteristic_Object((1,3,6,1,3,94,1,8,1,8),_ConnUnitSensorCharacteristic_Type())
connUnitSensorCharacteristic.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitSensorCharacteristic.setStatus(_A)
_ConnUnitPortTable_Object=MibTable
connUnitPortTable=_ConnUnitPortTable_Object((1,3,6,1,3,94,1,10))
if mibBuilder.loadTexts:connUnitPortTable.setStatus(_A)
_ConnUnitPortEntry_Object=MibTableRow
connUnitPortEntry=_ConnUnitPortEntry_Object((1,3,6,1,3,94,1,10,1))
connUnitPortEntry.setIndexNames((0,_D,_W),(0,_D,_X))
if mibBuilder.loadTexts:connUnitPortEntry.setStatus(_A)
_ConnUnitPortUnitId_Type=FcGlobalId
_ConnUnitPortUnitId_Object=MibTableColumn
connUnitPortUnitId=_ConnUnitPortUnitId_Object((1,3,6,1,3,94,1,10,1,1),_ConnUnitPortUnitId_Type())
connUnitPortUnitId.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortUnitId.setStatus(_A)
class _ConnUnitPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ConnUnitPortIndex_Type.__name__=_E
_ConnUnitPortIndex_Object=MibTableColumn
connUnitPortIndex=_ConnUnitPortIndex_Object((1,3,6,1,3,94,1,10,1,2),_ConnUnitPortIndex_Type())
connUnitPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortIndex.setStatus(_A)
class _ConnUnitPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22)));namedValues=NamedValues(*((_G,1),(_I,2),('not-present',3),('hub-port',4),('n-port',5),('nl-port',6),('fl-port',7),('f-port',8),('e-port',9),('g-port',10),('domain-ctl',11),('hub-controller',12),('scsi',13),('escon',14),('lan',15),('wan',16),('ac',17),('dc',18),('ssa',19),('wdm',20),('ib',21),('ipstore',22)))
_ConnUnitPortType_Type.__name__=_E
_ConnUnitPortType_Object=MibTableColumn
connUnitPortType=_ConnUnitPortType_Object((1,3,6,1,3,94,1,10,1,3),_ConnUnitPortType_Type())
connUnitPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortType.setStatus(_A)
class _ConnUnitPortFCClassCap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_ConnUnitPortFCClassCap_Type.__name__=_C
_ConnUnitPortFCClassCap_Object=MibTableColumn
connUnitPortFCClassCap=_ConnUnitPortFCClassCap_Object((1,3,6,1,3,94,1,10,1,4),_ConnUnitPortFCClassCap_Type())
connUnitPortFCClassCap.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortFCClassCap.setStatus(_A)
class _ConnUnitPortFCClassOp_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_ConnUnitPortFCClassOp_Type.__name__=_C
_ConnUnitPortFCClassOp_Object=MibTableColumn
connUnitPortFCClassOp=_ConnUnitPortFCClassOp_Object((1,3,6,1,3,94,1,10,1,5),_ConnUnitPortFCClassOp_Type())
connUnitPortFCClassOp.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortFCClassOp.setStatus(_A)
class _ConnUnitPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_G,1),(_P,2),(_Q,3),(_Y,4),('diagnostics',5)))
_ConnUnitPortState_Type.__name__=_E
_ConnUnitPortState_Object=MibTableColumn
connUnitPortState=_ConnUnitPortState_Object((1,3,6,1,3,94,1,10,1,6),_ConnUnitPortState_Type())
connUnitPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortState.setStatus(_A)
class _ConnUnitPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_G,1),(_M,2),('ready',3),(_K,4),('failure',5),('notparticipating',6),('initializing',7),('bypass',8),('ols',9),(_I,10)))
_ConnUnitPortStatus_Type.__name__=_E
_ConnUnitPortStatus_Object=MibTableColumn
connUnitPortStatus=_ConnUnitPortStatus_Object((1,3,6,1,3,94,1,10,1,7),_ConnUnitPortStatus_Type())
connUnitPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatus.setStatus(_A)
class _ConnUnitPortTransmitterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_G,1),(_I,2),(_M,3),('shortwave',4),('longwave',5),('copper',6),('scsi',7),('longwaveNoOFC',8),('shortwaveNoOFC',9),('longwaveLED',10),('ssa',11)))
_ConnUnitPortTransmitterType_Type.__name__=_E
_ConnUnitPortTransmitterType_Object=MibTableColumn
connUnitPortTransmitterType=_ConnUnitPortTransmitterType_Object((1,3,6,1,3,94,1,10,1,8),_ConnUnitPortTransmitterType_Type())
connUnitPortTransmitterType.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortTransmitterType.setStatus(_A)
class _ConnUnitPortModuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_G,1),(_I,2),('gbic',3),('embedded',4),('glm',5),('gbicSerialId',6),('gbicNoSerialId',7),('gbicNotInstalled',8),('smallFormFactor',9)))
_ConnUnitPortModuleType_Type.__name__=_E
_ConnUnitPortModuleType_Object=MibTableColumn
connUnitPortModuleType=_ConnUnitPortModuleType_Object((1,3,6,1,3,94,1,10,1,9),_ConnUnitPortModuleType_Type())
connUnitPortModuleType.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortModuleType.setStatus(_A)
_ConnUnitPortWwn_Type=FcGlobalId
_ConnUnitPortWwn_Object=MibTableColumn
connUnitPortWwn=_ConnUnitPortWwn_Object((1,3,6,1,3,94,1,10,1,10),_ConnUnitPortWwn_Type())
connUnitPortWwn.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortWwn.setStatus(_A)
_ConnUnitPortFCId_Type=FcAddressId
_ConnUnitPortFCId_Object=MibTableColumn
connUnitPortFCId=_ConnUnitPortFCId_Object((1,3,6,1,3,94,1,10,1,11),_ConnUnitPortFCId_Type())
connUnitPortFCId.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortFCId.setStatus(_A)
class _ConnUnitPortSn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_ConnUnitPortSn_Type.__name__=_F
_ConnUnitPortSn_Object=MibTableColumn
connUnitPortSn=_ConnUnitPortSn_Object((1,3,6,1,3,94,1,10,1,12),_ConnUnitPortSn_Type())
connUnitPortSn.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortSn.setStatus(_A)
class _ConnUnitPortRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_ConnUnitPortRevision_Type.__name__=_F
_ConnUnitPortRevision_Object=MibTableColumn
connUnitPortRevision=_ConnUnitPortRevision_Object((1,3,6,1,3,94,1,10,1,13),_ConnUnitPortRevision_Type())
connUnitPortRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortRevision.setStatus(_A)
class _ConnUnitPortVendor_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_ConnUnitPortVendor_Type.__name__=_F
_ConnUnitPortVendor_Object=MibTableColumn
connUnitPortVendor=_ConnUnitPortVendor_Object((1,3,6,1,3,94,1,10,1,14),_ConnUnitPortVendor_Type())
connUnitPortVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortVendor.setStatus(_A)
_ConnUnitPortSpeed_Type=Integer32
_ConnUnitPortSpeed_Object=MibTableColumn
connUnitPortSpeed=_ConnUnitPortSpeed_Object((1,3,6,1,3,94,1,10,1,15),_ConnUnitPortSpeed_Type())
connUnitPortSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortSpeed.setStatus(_A)
class _ConnUnitPortControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_G,1),(_R,2),('resetConnUnitPort',3),('bypassConnUnitPort',4),('unbypassConnUnitPort',5),('offlineConnUnitPort',6),('onlineConnUnitPort',7),('resetConnUnitPortCounters',8)))
_ConnUnitPortControl_Type.__name__=_E
_ConnUnitPortControl_Object=MibTableColumn
connUnitPortControl=_ConnUnitPortControl_Object((1,3,6,1,3,94,1,10,1,16),_ConnUnitPortControl_Type())
connUnitPortControl.setMaxAccess(_H)
if mibBuilder.loadTexts:connUnitPortControl.setStatus(_A)
_ConnUnitPortName_Type=DisplayString
_ConnUnitPortName_Object=MibTableColumn
connUnitPortName=_ConnUnitPortName_Object((1,3,6,1,3,94,1,10,1,17),_ConnUnitPortName_Type())
connUnitPortName.setMaxAccess(_H)
if mibBuilder.loadTexts:connUnitPortName.setStatus(_A)
_ConnUnitPortPhysicalNumber_Type=Integer32
_ConnUnitPortPhysicalNumber_Object=MibTableColumn
connUnitPortPhysicalNumber=_ConnUnitPortPhysicalNumber_Object((1,3,6,1,3,94,1,10,1,18),_ConnUnitPortPhysicalNumber_Type())
connUnitPortPhysicalNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortPhysicalNumber.setStatus(_A)
_ConnUnitPortStatObject_Type=ObjectIdentifier
_ConnUnitPortStatObject_Object=MibTableColumn
connUnitPortStatObject=_ConnUnitPortStatObject_Object((1,3,6,1,3,94,1,10,1,19),_ConnUnitPortStatObject_Type())
connUnitPortStatObject.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatObject.setStatus(_Z)
class _ConnUnitPortProtocolCap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_ConnUnitPortProtocolCap_Type.__name__=_C
_ConnUnitPortProtocolCap_Object=MibTableColumn
connUnitPortProtocolCap=_ConnUnitPortProtocolCap_Object((1,3,6,1,3,94,1,10,1,20),_ConnUnitPortProtocolCap_Type())
connUnitPortProtocolCap.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortProtocolCap.setStatus(_A)
class _ConnUnitPortProtocolOp_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_ConnUnitPortProtocolOp_Type.__name__=_C
_ConnUnitPortProtocolOp_Object=MibTableColumn
connUnitPortProtocolOp=_ConnUnitPortProtocolOp_Object((1,3,6,1,3,94,1,10,1,21),_ConnUnitPortProtocolOp_Type())
connUnitPortProtocolOp.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortProtocolOp.setStatus(_A)
_ConnUnitPortNodeWwn_Type=FcNameId
_ConnUnitPortNodeWwn_Object=MibTableColumn
connUnitPortNodeWwn=_ConnUnitPortNodeWwn_Object((1,3,6,1,3,94,1,10,1,22),_ConnUnitPortNodeWwn_Type())
connUnitPortNodeWwn.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortNodeWwn.setStatus(_A)
class _ConnUnitPortHWState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_G,1),(_N,2),(_Y,3),('active',4),('loopback',5),('txfault',6),('noMedia',7),('linkDown',8)))
_ConnUnitPortHWState_Type.__name__=_E
_ConnUnitPortHWState_Object=MibTableColumn
connUnitPortHWState=_ConnUnitPortHWState_Object((1,3,6,1,3,94,1,10,1,23),_ConnUnitPortHWState_Type())
connUnitPortHWState.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortHWState.setStatus(_A)
_ConnUnitEventTable_Object=MibTable
connUnitEventTable=_ConnUnitEventTable_Object((1,3,6,1,3,94,1,11))
if mibBuilder.loadTexts:connUnitEventTable.setStatus(_A)
_ConnUnitEventEntry_Object=MibTableRow
connUnitEventEntry=_ConnUnitEventEntry_Object((1,3,6,1,3,94,1,11,1))
connUnitEventEntry.setIndexNames((0,_D,_a),(0,_D,_b))
if mibBuilder.loadTexts:connUnitEventEntry.setStatus(_A)
_ConnUnitEventUnitId_Type=FcGlobalId
_ConnUnitEventUnitId_Object=MibTableColumn
connUnitEventUnitId=_ConnUnitEventUnitId_Object((1,3,6,1,3,94,1,11,1,1),_ConnUnitEventUnitId_Type())
connUnitEventUnitId.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitEventUnitId.setStatus(_A)
class _ConnUnitEventIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ConnUnitEventIndex_Type.__name__=_E
_ConnUnitEventIndex_Object=MibTableColumn
connUnitEventIndex=_ConnUnitEventIndex_Object((1,3,6,1,3,94,1,11,1,2),_ConnUnitEventIndex_Type())
connUnitEventIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitEventIndex.setStatus(_A)
_ConnUnitEventId_Type=Integer32
_ConnUnitEventId_Object=MibTableColumn
connUnitEventId=_ConnUnitEventId_Object((1,3,6,1,3,94,1,11,1,3),_ConnUnitEventId_Type())
connUnitEventId.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitEventId.setStatus(_Z)
class _ConnUnitREventTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_ConnUnitREventTime_Type.__name__=_F
_ConnUnitREventTime_Object=MibTableColumn
connUnitREventTime=_ConnUnitREventTime_Object((1,3,6,1,3,94,1,11,1,4),_ConnUnitREventTime_Type())
connUnitREventTime.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitREventTime.setStatus(_A)
_ConnUnitSEventTime_Type=TimeTicks
_ConnUnitSEventTime_Object=MibTableColumn
connUnitSEventTime=_ConnUnitSEventTime_Object((1,3,6,1,3,94,1,11,1,5),_ConnUnitSEventTime_Type())
connUnitSEventTime.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitSEventTime.setStatus(_A)
_ConnUnitEventSeverity_Type=FcEventSeverity
_ConnUnitEventSeverity_Object=MibTableColumn
connUnitEventSeverity=_ConnUnitEventSeverity_Object((1,3,6,1,3,94,1,11,1,6),_ConnUnitEventSeverity_Type())
connUnitEventSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitEventSeverity.setStatus(_A)
class _ConnUnitEventType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_G,1),(_I,2),('status',3),('configuration',4),('topology',5)))
_ConnUnitEventType_Type.__name__=_E
_ConnUnitEventType_Object=MibTableColumn
connUnitEventType=_ConnUnitEventType_Object((1,3,6,1,3,94,1,11,1,7),_ConnUnitEventType_Type())
connUnitEventType.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitEventType.setStatus(_A)
_ConnUnitEventObject_Type=ObjectIdentifier
_ConnUnitEventObject_Object=MibTableColumn
connUnitEventObject=_ConnUnitEventObject_Object((1,3,6,1,3,94,1,11,1,8),_ConnUnitEventObject_Type())
connUnitEventObject.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitEventObject.setStatus(_A)
_ConnUnitEventDescr_Type=DisplayString
_ConnUnitEventDescr_Object=MibTableColumn
connUnitEventDescr=_ConnUnitEventDescr_Object((1,3,6,1,3,94,1,11,1,9),_ConnUnitEventDescr_Type())
connUnitEventDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitEventDescr.setStatus(_A)
_ConnUnitLinkTable_Object=MibTable
connUnitLinkTable=_ConnUnitLinkTable_Object((1,3,6,1,3,94,1,12))
if mibBuilder.loadTexts:connUnitLinkTable.setStatus(_A)
_ConnUnitLinkEntry_Object=MibTableRow
connUnitLinkEntry=_ConnUnitLinkEntry_Object((1,3,6,1,3,94,1,12,1))
connUnitLinkEntry.setIndexNames((0,_D,_c),(0,_D,_d))
if mibBuilder.loadTexts:connUnitLinkEntry.setStatus(_A)
_ConnUnitLinkUnitId_Type=FcGlobalId
_ConnUnitLinkUnitId_Object=MibTableColumn
connUnitLinkUnitId=_ConnUnitLinkUnitId_Object((1,3,6,1,3,94,1,12,1,1),_ConnUnitLinkUnitId_Type())
connUnitLinkUnitId.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitLinkUnitId.setStatus(_A)
class _ConnUnitLinkIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ConnUnitLinkIndex_Type.__name__=_E
_ConnUnitLinkIndex_Object=MibTableColumn
connUnitLinkIndex=_ConnUnitLinkIndex_Object((1,3,6,1,3,94,1,12,1,2),_ConnUnitLinkIndex_Type())
connUnitLinkIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitLinkIndex.setStatus(_A)
class _ConnUnitLinkNodeIdX_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_ConnUnitLinkNodeIdX_Type.__name__=_C
_ConnUnitLinkNodeIdX_Object=MibTableColumn
connUnitLinkNodeIdX=_ConnUnitLinkNodeIdX_Object((1,3,6,1,3,94,1,12,1,3),_ConnUnitLinkNodeIdX_Type())
connUnitLinkNodeIdX.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitLinkNodeIdX.setStatus(_A)
_ConnUnitLinkPortNumberX_Type=Integer32
_ConnUnitLinkPortNumberX_Object=MibTableColumn
connUnitLinkPortNumberX=_ConnUnitLinkPortNumberX_Object((1,3,6,1,3,94,1,12,1,4),_ConnUnitLinkPortNumberX_Type())
connUnitLinkPortNumberX.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitLinkPortNumberX.setStatus(_A)
_ConnUnitLinkPortWwnX_Type=FcGlobalId
_ConnUnitLinkPortWwnX_Object=MibTableColumn
connUnitLinkPortWwnX=_ConnUnitLinkPortWwnX_Object((1,3,6,1,3,94,1,12,1,5),_ConnUnitLinkPortWwnX_Type())
connUnitLinkPortWwnX.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitLinkPortWwnX.setStatus(_A)
class _ConnUnitLinkNodeIdY_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_ConnUnitLinkNodeIdY_Type.__name__=_C
_ConnUnitLinkNodeIdY_Object=MibTableColumn
connUnitLinkNodeIdY=_ConnUnitLinkNodeIdY_Object((1,3,6,1,3,94,1,12,1,6),_ConnUnitLinkNodeIdY_Type())
connUnitLinkNodeIdY.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitLinkNodeIdY.setStatus(_A)
_ConnUnitLinkPortNumberY_Type=Integer32
_ConnUnitLinkPortNumberY_Object=MibTableColumn
connUnitLinkPortNumberY=_ConnUnitLinkPortNumberY_Object((1,3,6,1,3,94,1,12,1,7),_ConnUnitLinkPortNumberY_Type())
connUnitLinkPortNumberY.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitLinkPortNumberY.setStatus(_A)
_ConnUnitLinkPortWwnY_Type=FcGlobalId
_ConnUnitLinkPortWwnY_Object=MibTableColumn
connUnitLinkPortWwnY=_ConnUnitLinkPortWwnY_Object((1,3,6,1,3,94,1,12,1,8),_ConnUnitLinkPortWwnY_Type())
connUnitLinkPortWwnY.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitLinkPortWwnY.setStatus(_A)
class _ConnUnitLinkAgentAddressY_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_ConnUnitLinkAgentAddressY_Type.__name__=_C
_ConnUnitLinkAgentAddressY_Object=MibTableColumn
connUnitLinkAgentAddressY=_ConnUnitLinkAgentAddressY_Object((1,3,6,1,3,94,1,12,1,9),_ConnUnitLinkAgentAddressY_Type())
connUnitLinkAgentAddressY.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitLinkAgentAddressY.setStatus(_A)
_ConnUnitLinkAgentAddressTypeY_Type=Integer32
_ConnUnitLinkAgentAddressTypeY_Object=MibTableColumn
connUnitLinkAgentAddressTypeY=_ConnUnitLinkAgentAddressTypeY_Object((1,3,6,1,3,94,1,12,1,10),_ConnUnitLinkAgentAddressTypeY_Type())
connUnitLinkAgentAddressTypeY.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitLinkAgentAddressTypeY.setStatus(_A)
_ConnUnitLinkAgentPortY_Type=Integer32
_ConnUnitLinkAgentPortY_Object=MibTableColumn
connUnitLinkAgentPortY=_ConnUnitLinkAgentPortY_Object((1,3,6,1,3,94,1,12,1,11),_ConnUnitLinkAgentPortY_Type())
connUnitLinkAgentPortY.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitLinkAgentPortY.setStatus(_A)
_ConnUnitLinkUnitTypeY_Type=FcUnitType
_ConnUnitLinkUnitTypeY_Object=MibTableColumn
connUnitLinkUnitTypeY=_ConnUnitLinkUnitTypeY_Object((1,3,6,1,3,94,1,12,1,12),_ConnUnitLinkUnitTypeY_Type())
connUnitLinkUnitTypeY.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitLinkUnitTypeY.setStatus(_A)
class _ConnUnitLinkConnIdY_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_ConnUnitLinkConnIdY_Type.__name__=_C
_ConnUnitLinkConnIdY_Object=MibTableColumn
connUnitLinkConnIdY=_ConnUnitLinkConnIdY_Object((1,3,6,1,3,94,1,12,1,13),_ConnUnitLinkConnIdY_Type())
connUnitLinkConnIdY.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitLinkConnIdY.setStatus(_A)
_ConnUnitLinkCurrIndex_Type=Integer32
_ConnUnitLinkCurrIndex_Object=MibTableColumn
connUnitLinkCurrIndex=_ConnUnitLinkCurrIndex_Object((1,3,6,1,3,94,1,12,1,14),_ConnUnitLinkCurrIndex_Type())
connUnitLinkCurrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitLinkCurrIndex.setStatus(_A)
_ConnUnitZoneTable_Object=MibTable
connUnitZoneTable=_ConnUnitZoneTable_Object((1,3,6,1,3,94,1,13))
if mibBuilder.loadTexts:connUnitZoneTable.setStatus(_A)
_ConnUnitZoneEntry_Object=MibTableRow
connUnitZoneEntry=_ConnUnitZoneEntry_Object((1,3,6,1,3,94,1,13,1))
connUnitZoneEntry.setIndexNames((0,_D,_e),(0,_D,_f))
if mibBuilder.loadTexts:connUnitZoneEntry.setStatus(_A)
class _ConnUnitZoneIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ConnUnitZoneIndex_Type.__name__=_E
_ConnUnitZoneIndex_Object=MibTableColumn
connUnitZoneIndex=_ConnUnitZoneIndex_Object((1,3,6,1,3,94,1,13,1,1),_ConnUnitZoneIndex_Type())
connUnitZoneIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitZoneIndex.setStatus(_A)
class _ConnUnitZoneMemberIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ConnUnitZoneMemberIndex_Type.__name__=_E
_ConnUnitZoneMemberIndex_Object=MibTableColumn
connUnitZoneMemberIndex=_ConnUnitZoneMemberIndex_Object((1,3,6,1,3,94,1,13,1,2),_ConnUnitZoneMemberIndex_Type())
connUnitZoneMemberIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitZoneMemberIndex.setStatus(_A)
class _ConnUnitZoneSetName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_ConnUnitZoneSetName_Type.__name__=_F
_ConnUnitZoneSetName_Object=MibTableColumn
connUnitZoneSetName=_ConnUnitZoneSetName_Object((1,3,6,1,3,94,1,13,1,3),_ConnUnitZoneSetName_Type())
connUnitZoneSetName.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitZoneSetName.setStatus(_A)
_ConnUnitZoneSetNumZones_Type=Integer32
_ConnUnitZoneSetNumZones_Object=MibTableColumn
connUnitZoneSetNumZones=_ConnUnitZoneSetNumZones_Object((1,3,6,1,3,94,1,13,1,4),_ConnUnitZoneSetNumZones_Type())
connUnitZoneSetNumZones.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitZoneSetNumZones.setStatus(_A)
class _ConnUnitZoneName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_ConnUnitZoneName_Type.__name__=_F
_ConnUnitZoneName_Object=MibTableColumn
connUnitZoneName=_ConnUnitZoneName_Object((1,3,6,1,3,94,1,13,1,5),_ConnUnitZoneName_Type())
connUnitZoneName.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitZoneName.setStatus(_A)
class _ConnUnitZoneCapabilities_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_ConnUnitZoneCapabilities_Type.__name__=_C
_ConnUnitZoneCapabilities_Object=MibTableColumn
connUnitZoneCapabilities=_ConnUnitZoneCapabilities_Object((1,3,6,1,3,94,1,13,1,6),_ConnUnitZoneCapabilities_Type())
connUnitZoneCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitZoneCapabilities.setStatus(_A)
class _ConnUnitZoneEnforcementState_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_ConnUnitZoneEnforcementState_Type.__name__=_C
_ConnUnitZoneEnforcementState_Object=MibTableColumn
connUnitZoneEnforcementState=_ConnUnitZoneEnforcementState_Object((1,3,6,1,3,94,1,13,1,7),_ConnUnitZoneEnforcementState_Type())
connUnitZoneEnforcementState.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitZoneEnforcementState.setStatus(_A)
class _ConnUnitZoneAttributeBlock_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(80,80));fixedLength=80
_ConnUnitZoneAttributeBlock_Type.__name__=_C
_ConnUnitZoneAttributeBlock_Object=MibTableColumn
connUnitZoneAttributeBlock=_ConnUnitZoneAttributeBlock_Object((1,3,6,1,3,94,1,13,1,8),_ConnUnitZoneAttributeBlock_Type())
connUnitZoneAttributeBlock.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitZoneAttributeBlock.setStatus(_A)
_ConnUnitZoneNumMembers_Type=Integer32
_ConnUnitZoneNumMembers_Object=MibTableColumn
connUnitZoneNumMembers=_ConnUnitZoneNumMembers_Object((1,3,6,1,3,94,1,13,1,9),_ConnUnitZoneNumMembers_Type())
connUnitZoneNumMembers.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitZoneNumMembers.setStatus(_A)
_ConnUnitZoneMemberIdType_Type=Integer32
_ConnUnitZoneMemberIdType_Object=MibTableColumn
connUnitZoneMemberIdType=_ConnUnitZoneMemberIdType_Object((1,3,6,1,3,94,1,13,1,10),_ConnUnitZoneMemberIdType_Type())
connUnitZoneMemberIdType.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitZoneMemberIdType.setStatus(_A)
_ConnUnitZoneMemberID_Type=FcGlobalId
_ConnUnitZoneMemberID_Object=MibTableColumn
connUnitZoneMemberID=_ConnUnitZoneMemberID_Object((1,3,6,1,3,94,1,13,1,11),_ConnUnitZoneMemberID_Type())
connUnitZoneMemberID.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitZoneMemberID.setStatus(_A)
_ConnUnitZoningAliasTable_Object=MibTable
connUnitZoningAliasTable=_ConnUnitZoningAliasTable_Object((1,3,6,1,3,94,1,14))
if mibBuilder.loadTexts:connUnitZoningAliasTable.setStatus(_A)
_ConnUnitZoningAliasEntry_Object=MibTableRow
connUnitZoningAliasEntry=_ConnUnitZoningAliasEntry_Object((1,3,6,1,3,94,1,14,1))
connUnitZoningAliasEntry.setIndexNames((0,_D,_g),(0,_D,_h))
if mibBuilder.loadTexts:connUnitZoningAliasEntry.setStatus(_A)
class _ConnUnitZoningAliasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ConnUnitZoningAliasIndex_Type.__name__=_E
_ConnUnitZoningAliasIndex_Object=MibTableColumn
connUnitZoningAliasIndex=_ConnUnitZoningAliasIndex_Object((1,3,6,1,3,94,1,14,1,1),_ConnUnitZoningAliasIndex_Type())
connUnitZoningAliasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitZoningAliasIndex.setStatus(_A)
class _ConnUnitZoningAliasMemberIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ConnUnitZoningAliasMemberIndex_Type.__name__=_E
_ConnUnitZoningAliasMemberIndex_Object=MibTableColumn
connUnitZoningAliasMemberIndex=_ConnUnitZoningAliasMemberIndex_Object((1,3,6,1,3,94,1,14,1,2),_ConnUnitZoningAliasMemberIndex_Type())
connUnitZoningAliasMemberIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitZoningAliasMemberIndex.setStatus(_A)
_ConnUnitZoningAliasNumAliases_Type=Integer32
_ConnUnitZoningAliasNumAliases_Object=MibTableColumn
connUnitZoningAliasNumAliases=_ConnUnitZoningAliasNumAliases_Object((1,3,6,1,3,94,1,14,1,3),_ConnUnitZoningAliasNumAliases_Type())
connUnitZoningAliasNumAliases.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitZoningAliasNumAliases.setStatus(_A)
class _ConnUnitZoningAliasName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_ConnUnitZoningAliasName_Type.__name__=_F
_ConnUnitZoningAliasName_Object=MibTableColumn
connUnitZoningAliasName=_ConnUnitZoningAliasName_Object((1,3,6,1,3,94,1,14,1,4),_ConnUnitZoningAliasName_Type())
connUnitZoningAliasName.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitZoningAliasName.setStatus(_A)
_ConnUnitZoningAliasNumMembers_Type=Integer32
_ConnUnitZoningAliasNumMembers_Object=MibTableColumn
connUnitZoningAliasNumMembers=_ConnUnitZoningAliasNumMembers_Object((1,3,6,1,3,94,1,14,1,5),_ConnUnitZoningAliasNumMembers_Type())
connUnitZoningAliasNumMembers.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitZoningAliasNumMembers.setStatus(_A)
_ConnUnitZoningAliasMemberIdType_Type=Integer32
_ConnUnitZoningAliasMemberIdType_Object=MibTableColumn
connUnitZoningAliasMemberIdType=_ConnUnitZoningAliasMemberIdType_Object((1,3,6,1,3,94,1,14,1,6),_ConnUnitZoningAliasMemberIdType_Type())
connUnitZoningAliasMemberIdType.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitZoningAliasMemberIdType.setStatus(_A)
_ConnUnitZoningAliasMemberID_Type=FcGlobalId
_ConnUnitZoningAliasMemberID_Object=MibTableColumn
connUnitZoningAliasMemberID=_ConnUnitZoningAliasMemberID_Object((1,3,6,1,3,94,1,14,1,7),_ConnUnitZoningAliasMemberID_Type())
connUnitZoningAliasMemberID.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitZoningAliasMemberID.setStatus(_A)
_TrapReg_ObjectIdentity=ObjectIdentity
trapReg=_TrapReg_ObjectIdentity((1,3,6,1,3,94,2))
_TrapMaxClients_Type=Integer32
_TrapMaxClients_Object=MibScalar
trapMaxClients=_TrapMaxClients_Object((1,3,6,1,3,94,2,1),_TrapMaxClients_Type())
trapMaxClients.setMaxAccess(_B)
if mibBuilder.loadTexts:trapMaxClients.setStatus(_A)
_TrapClientCount_Type=Integer32
_TrapClientCount_Object=MibScalar
trapClientCount=_TrapClientCount_Object((1,3,6,1,3,94,2,2),_TrapClientCount_Type())
trapClientCount.setMaxAccess(_B)
if mibBuilder.loadTexts:trapClientCount.setStatus(_A)
_TrapRegTable_Object=MibTable
trapRegTable=_TrapRegTable_Object((1,3,6,1,3,94,2,3))
if mibBuilder.loadTexts:trapRegTable.setStatus(_A)
_TrapRegEntry_Object=MibTableRow
trapRegEntry=_TrapRegEntry_Object((1,3,6,1,3,94,2,3,1))
trapRegEntry.setIndexNames((0,_D,_i),(0,_D,_j))
if mibBuilder.loadTexts:trapRegEntry.setStatus(_A)
_TrapRegIpAddress_Type=IpAddress
_TrapRegIpAddress_Object=MibTableColumn
trapRegIpAddress=_TrapRegIpAddress_Object((1,3,6,1,3,94,2,3,1,1),_TrapRegIpAddress_Type())
trapRegIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:trapRegIpAddress.setStatus(_A)
class _TrapRegPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_TrapRegPort_Type.__name__=_E
_TrapRegPort_Object=MibTableColumn
trapRegPort=_TrapRegPort_Object((1,3,6,1,3,94,2,3,1,2),_TrapRegPort_Type())
trapRegPort.setMaxAccess(_B)
if mibBuilder.loadTexts:trapRegPort.setStatus(_A)
_TrapRegFilter_Type=FcEventSeverity
_TrapRegFilter_Object=MibTableColumn
trapRegFilter=_TrapRegFilter_Object((1,3,6,1,3,94,2,3,1,3),_TrapRegFilter_Type())
trapRegFilter.setMaxAccess(_H)
if mibBuilder.loadTexts:trapRegFilter.setStatus(_A)
class _TrapRegRowState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('rowDestroy',1),('rowInactive',2),('rowActive',3)))
_TrapRegRowState_Type.__name__=_E
_TrapRegRowState_Object=MibTableColumn
trapRegRowState=_TrapRegRowState_Object((1,3,6,1,3,94,2,3,1,4),_TrapRegRowState_Type())
trapRegRowState.setMaxAccess(_H)
if mibBuilder.loadTexts:trapRegRowState.setStatus(_A)
class _RevisionNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_RevisionNumber_Type.__name__=_F
_RevisionNumber_Object=MibScalar
revisionNumber=_RevisionNumber_Object((1,3,6,1,3,94,3),_RevisionNumber_Type())
revisionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:revisionNumber.setStatus(_A)
_StatSet_ObjectIdentity=ObjectIdentity
statSet=_StatSet_ObjectIdentity((1,3,6,1,3,94,4))
_ConnUnitPortStatTable_Object=MibTable
connUnitPortStatTable=_ConnUnitPortStatTable_Object((1,3,6,1,3,94,4,5))
if mibBuilder.loadTexts:connUnitPortStatTable.setStatus(_A)
_ConnUnitPortStatEntry_Object=MibTableRow
connUnitPortStatEntry=_ConnUnitPortStatEntry_Object((1,3,6,1,3,94,4,5,1))
connUnitPortStatEntry.setIndexNames((0,_D,_k),(0,_D,_l))
if mibBuilder.loadTexts:connUnitPortStatEntry.setStatus(_A)
_ConnUnitPortStatUnitId_Type=FcGlobalId
_ConnUnitPortStatUnitId_Object=MibTableColumn
connUnitPortStatUnitId=_ConnUnitPortStatUnitId_Object((1,3,6,1,3,94,4,5,1,1),_ConnUnitPortStatUnitId_Type())
connUnitPortStatUnitId.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatUnitId.setStatus(_A)
class _ConnUnitPortStatIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ConnUnitPortStatIndex_Type.__name__=_E
_ConnUnitPortStatIndex_Object=MibTableColumn
connUnitPortStatIndex=_ConnUnitPortStatIndex_Object((1,3,6,1,3,94,4,5,1,2),_ConnUnitPortStatIndex_Type())
connUnitPortStatIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatIndex.setStatus(_A)
class _ConnUnitPortStatCountError_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountError_Type.__name__=_C
_ConnUnitPortStatCountError_Object=MibTableColumn
connUnitPortStatCountError=_ConnUnitPortStatCountError_Object((1,3,6,1,3,94,4,5,1,3),_ConnUnitPortStatCountError_Type())
connUnitPortStatCountError.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountError.setStatus(_A)
class _ConnUnitPortStatCountTxObjects_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountTxObjects_Type.__name__=_C
_ConnUnitPortStatCountTxObjects_Object=MibTableColumn
connUnitPortStatCountTxObjects=_ConnUnitPortStatCountTxObjects_Object((1,3,6,1,3,94,4,5,1,4),_ConnUnitPortStatCountTxObjects_Type())
connUnitPortStatCountTxObjects.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountTxObjects.setStatus(_A)
class _ConnUnitPortStatCountRxObjects_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountRxObjects_Type.__name__=_C
_ConnUnitPortStatCountRxObjects_Object=MibTableColumn
connUnitPortStatCountRxObjects=_ConnUnitPortStatCountRxObjects_Object((1,3,6,1,3,94,4,5,1,5),_ConnUnitPortStatCountRxObjects_Type())
connUnitPortStatCountRxObjects.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountRxObjects.setStatus(_A)
class _ConnUnitPortStatCountTxElements_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountTxElements_Type.__name__=_C
_ConnUnitPortStatCountTxElements_Object=MibTableColumn
connUnitPortStatCountTxElements=_ConnUnitPortStatCountTxElements_Object((1,3,6,1,3,94,4,5,1,6),_ConnUnitPortStatCountTxElements_Type())
connUnitPortStatCountTxElements.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountTxElements.setStatus(_A)
class _ConnUnitPortStatCountRxElements_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountRxElements_Type.__name__=_C
_ConnUnitPortStatCountRxElements_Object=MibTableColumn
connUnitPortStatCountRxElements=_ConnUnitPortStatCountRxElements_Object((1,3,6,1,3,94,4,5,1,7),_ConnUnitPortStatCountRxElements_Type())
connUnitPortStatCountRxElements.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountRxElements.setStatus(_A)
class _ConnUnitPortStatCountBBCreditZero_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountBBCreditZero_Type.__name__=_C
_ConnUnitPortStatCountBBCreditZero_Object=MibTableColumn
connUnitPortStatCountBBCreditZero=_ConnUnitPortStatCountBBCreditZero_Object((1,3,6,1,3,94,4,5,1,8),_ConnUnitPortStatCountBBCreditZero_Type())
connUnitPortStatCountBBCreditZero.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountBBCreditZero.setStatus(_A)
class _ConnUnitPortStatCountInputBuffersFull_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountInputBuffersFull_Type.__name__=_C
_ConnUnitPortStatCountInputBuffersFull_Object=MibTableColumn
connUnitPortStatCountInputBuffersFull=_ConnUnitPortStatCountInputBuffersFull_Object((1,3,6,1,3,94,4,5,1,9),_ConnUnitPortStatCountInputBuffersFull_Type())
connUnitPortStatCountInputBuffersFull.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountInputBuffersFull.setStatus(_A)
class _ConnUnitPortStatCountFBSYFrames_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountFBSYFrames_Type.__name__=_C
_ConnUnitPortStatCountFBSYFrames_Object=MibTableColumn
connUnitPortStatCountFBSYFrames=_ConnUnitPortStatCountFBSYFrames_Object((1,3,6,1,3,94,4,5,1,10),_ConnUnitPortStatCountFBSYFrames_Type())
connUnitPortStatCountFBSYFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountFBSYFrames.setStatus(_A)
class _ConnUnitPortStatCountPBSYFrames_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountPBSYFrames_Type.__name__=_C
_ConnUnitPortStatCountPBSYFrames_Object=MibTableColumn
connUnitPortStatCountPBSYFrames=_ConnUnitPortStatCountPBSYFrames_Object((1,3,6,1,3,94,4,5,1,11),_ConnUnitPortStatCountPBSYFrames_Type())
connUnitPortStatCountPBSYFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountPBSYFrames.setStatus(_A)
class _ConnUnitPortStatCountFRJTFrames_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountFRJTFrames_Type.__name__=_C
_ConnUnitPortStatCountFRJTFrames_Object=MibTableColumn
connUnitPortStatCountFRJTFrames=_ConnUnitPortStatCountFRJTFrames_Object((1,3,6,1,3,94,4,5,1,12),_ConnUnitPortStatCountFRJTFrames_Type())
connUnitPortStatCountFRJTFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountFRJTFrames.setStatus(_A)
class _ConnUnitPortStatCountPRJTFrames_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountPRJTFrames_Type.__name__=_C
_ConnUnitPortStatCountPRJTFrames_Object=MibTableColumn
connUnitPortStatCountPRJTFrames=_ConnUnitPortStatCountPRJTFrames_Object((1,3,6,1,3,94,4,5,1,13),_ConnUnitPortStatCountPRJTFrames_Type())
connUnitPortStatCountPRJTFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountPRJTFrames.setStatus(_A)
class _ConnUnitPortStatCountClass1RxFrames_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountClass1RxFrames_Type.__name__=_C
_ConnUnitPortStatCountClass1RxFrames_Object=MibTableColumn
connUnitPortStatCountClass1RxFrames=_ConnUnitPortStatCountClass1RxFrames_Object((1,3,6,1,3,94,4,5,1,14),_ConnUnitPortStatCountClass1RxFrames_Type())
connUnitPortStatCountClass1RxFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountClass1RxFrames.setStatus(_A)
class _ConnUnitPortStatCountClass1TxFrames_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountClass1TxFrames_Type.__name__=_C
_ConnUnitPortStatCountClass1TxFrames_Object=MibTableColumn
connUnitPortStatCountClass1TxFrames=_ConnUnitPortStatCountClass1TxFrames_Object((1,3,6,1,3,94,4,5,1,15),_ConnUnitPortStatCountClass1TxFrames_Type())
connUnitPortStatCountClass1TxFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountClass1TxFrames.setStatus(_A)
class _ConnUnitPortStatCountClass1FBSYFrames_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountClass1FBSYFrames_Type.__name__=_C
_ConnUnitPortStatCountClass1FBSYFrames_Object=MibTableColumn
connUnitPortStatCountClass1FBSYFrames=_ConnUnitPortStatCountClass1FBSYFrames_Object((1,3,6,1,3,94,4,5,1,16),_ConnUnitPortStatCountClass1FBSYFrames_Type())
connUnitPortStatCountClass1FBSYFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountClass1FBSYFrames.setStatus(_A)
class _ConnUnitPortStatCountClass1PBSYFrames_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountClass1PBSYFrames_Type.__name__=_C
_ConnUnitPortStatCountClass1PBSYFrames_Object=MibTableColumn
connUnitPortStatCountClass1PBSYFrames=_ConnUnitPortStatCountClass1PBSYFrames_Object((1,3,6,1,3,94,4,5,1,17),_ConnUnitPortStatCountClass1PBSYFrames_Type())
connUnitPortStatCountClass1PBSYFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountClass1PBSYFrames.setStatus(_A)
class _ConnUnitPortStatCountClass1FRJTFrames_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountClass1FRJTFrames_Type.__name__=_C
_ConnUnitPortStatCountClass1FRJTFrames_Object=MibTableColumn
connUnitPortStatCountClass1FRJTFrames=_ConnUnitPortStatCountClass1FRJTFrames_Object((1,3,6,1,3,94,4,5,1,18),_ConnUnitPortStatCountClass1FRJTFrames_Type())
connUnitPortStatCountClass1FRJTFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountClass1FRJTFrames.setStatus(_A)
class _ConnUnitPortStatCountClass1PRJTFrames_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountClass1PRJTFrames_Type.__name__=_C
_ConnUnitPortStatCountClass1PRJTFrames_Object=MibTableColumn
connUnitPortStatCountClass1PRJTFrames=_ConnUnitPortStatCountClass1PRJTFrames_Object((1,3,6,1,3,94,4,5,1,19),_ConnUnitPortStatCountClass1PRJTFrames_Type())
connUnitPortStatCountClass1PRJTFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountClass1PRJTFrames.setStatus(_A)
class _ConnUnitPortStatCountClass2RxFrames_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountClass2RxFrames_Type.__name__=_C
_ConnUnitPortStatCountClass2RxFrames_Object=MibTableColumn
connUnitPortStatCountClass2RxFrames=_ConnUnitPortStatCountClass2RxFrames_Object((1,3,6,1,3,94,4,5,1,20),_ConnUnitPortStatCountClass2RxFrames_Type())
connUnitPortStatCountClass2RxFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountClass2RxFrames.setStatus(_A)
class _ConnUnitPortStatCountClass2TxFrames_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountClass2TxFrames_Type.__name__=_C
_ConnUnitPortStatCountClass2TxFrames_Object=MibTableColumn
connUnitPortStatCountClass2TxFrames=_ConnUnitPortStatCountClass2TxFrames_Object((1,3,6,1,3,94,4,5,1,21),_ConnUnitPortStatCountClass2TxFrames_Type())
connUnitPortStatCountClass2TxFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountClass2TxFrames.setStatus(_A)
class _ConnUnitPortStatCountClass2FBSYFrames_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountClass2FBSYFrames_Type.__name__=_C
_ConnUnitPortStatCountClass2FBSYFrames_Object=MibTableColumn
connUnitPortStatCountClass2FBSYFrames=_ConnUnitPortStatCountClass2FBSYFrames_Object((1,3,6,1,3,94,4,5,1,22),_ConnUnitPortStatCountClass2FBSYFrames_Type())
connUnitPortStatCountClass2FBSYFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountClass2FBSYFrames.setStatus(_A)
class _ConnUnitPortStatCountClass2PBSYFrames_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountClass2PBSYFrames_Type.__name__=_C
_ConnUnitPortStatCountClass2PBSYFrames_Object=MibTableColumn
connUnitPortStatCountClass2PBSYFrames=_ConnUnitPortStatCountClass2PBSYFrames_Object((1,3,6,1,3,94,4,5,1,23),_ConnUnitPortStatCountClass2PBSYFrames_Type())
connUnitPortStatCountClass2PBSYFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountClass2PBSYFrames.setStatus(_A)
class _ConnUnitPortStatCountClass2FRJTFrames_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountClass2FRJTFrames_Type.__name__=_C
_ConnUnitPortStatCountClass2FRJTFrames_Object=MibTableColumn
connUnitPortStatCountClass2FRJTFrames=_ConnUnitPortStatCountClass2FRJTFrames_Object((1,3,6,1,3,94,4,5,1,24),_ConnUnitPortStatCountClass2FRJTFrames_Type())
connUnitPortStatCountClass2FRJTFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountClass2FRJTFrames.setStatus(_A)
class _ConnUnitPortStatCountClass2PRJTFrames_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountClass2PRJTFrames_Type.__name__=_C
_ConnUnitPortStatCountClass2PRJTFrames_Object=MibTableColumn
connUnitPortStatCountClass2PRJTFrames=_ConnUnitPortStatCountClass2PRJTFrames_Object((1,3,6,1,3,94,4,5,1,25),_ConnUnitPortStatCountClass2PRJTFrames_Type())
connUnitPortStatCountClass2PRJTFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountClass2PRJTFrames.setStatus(_A)
class _ConnUnitPortStatCountClass3RxFrames_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountClass3RxFrames_Type.__name__=_C
_ConnUnitPortStatCountClass3RxFrames_Object=MibTableColumn
connUnitPortStatCountClass3RxFrames=_ConnUnitPortStatCountClass3RxFrames_Object((1,3,6,1,3,94,4,5,1,26),_ConnUnitPortStatCountClass3RxFrames_Type())
connUnitPortStatCountClass3RxFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountClass3RxFrames.setStatus(_A)
class _ConnUnitPortStatCountClass3TxFrames_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountClass3TxFrames_Type.__name__=_C
_ConnUnitPortStatCountClass3TxFrames_Object=MibTableColumn
connUnitPortStatCountClass3TxFrames=_ConnUnitPortStatCountClass3TxFrames_Object((1,3,6,1,3,94,4,5,1,27),_ConnUnitPortStatCountClass3TxFrames_Type())
connUnitPortStatCountClass3TxFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountClass3TxFrames.setStatus(_A)
class _ConnUnitPortStatCountClass3Discards_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountClass3Discards_Type.__name__=_C
_ConnUnitPortStatCountClass3Discards_Object=MibTableColumn
connUnitPortStatCountClass3Discards=_ConnUnitPortStatCountClass3Discards_Object((1,3,6,1,3,94,4,5,1,28),_ConnUnitPortStatCountClass3Discards_Type())
connUnitPortStatCountClass3Discards.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountClass3Discards.setStatus(_A)
class _ConnUnitPortStatCountRxMulticastObjects_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountRxMulticastObjects_Type.__name__=_C
_ConnUnitPortStatCountRxMulticastObjects_Object=MibTableColumn
connUnitPortStatCountRxMulticastObjects=_ConnUnitPortStatCountRxMulticastObjects_Object((1,3,6,1,3,94,4,5,1,29),_ConnUnitPortStatCountRxMulticastObjects_Type())
connUnitPortStatCountRxMulticastObjects.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountRxMulticastObjects.setStatus(_A)
class _ConnUnitPortStatCountTxMulticastObjects_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountTxMulticastObjects_Type.__name__=_C
_ConnUnitPortStatCountTxMulticastObjects_Object=MibTableColumn
connUnitPortStatCountTxMulticastObjects=_ConnUnitPortStatCountTxMulticastObjects_Object((1,3,6,1,3,94,4,5,1,30),_ConnUnitPortStatCountTxMulticastObjects_Type())
connUnitPortStatCountTxMulticastObjects.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountTxMulticastObjects.setStatus(_A)
class _ConnUnitPortStatCountRxBroadcastObjects_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountRxBroadcastObjects_Type.__name__=_C
_ConnUnitPortStatCountRxBroadcastObjects_Object=MibTableColumn
connUnitPortStatCountRxBroadcastObjects=_ConnUnitPortStatCountRxBroadcastObjects_Object((1,3,6,1,3,94,4,5,1,31),_ConnUnitPortStatCountRxBroadcastObjects_Type())
connUnitPortStatCountRxBroadcastObjects.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountRxBroadcastObjects.setStatus(_A)
class _ConnUnitPortStatCountTxBroadcastObjects_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountTxBroadcastObjects_Type.__name__=_C
_ConnUnitPortStatCountTxBroadcastObjects_Object=MibTableColumn
connUnitPortStatCountTxBroadcastObjects=_ConnUnitPortStatCountTxBroadcastObjects_Object((1,3,6,1,3,94,4,5,1,32),_ConnUnitPortStatCountTxBroadcastObjects_Type())
connUnitPortStatCountTxBroadcastObjects.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountTxBroadcastObjects.setStatus(_A)
class _ConnUnitPortStatCountRxLinkResets_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountRxLinkResets_Type.__name__=_C
_ConnUnitPortStatCountRxLinkResets_Object=MibTableColumn
connUnitPortStatCountRxLinkResets=_ConnUnitPortStatCountRxLinkResets_Object((1,3,6,1,3,94,4,5,1,33),_ConnUnitPortStatCountRxLinkResets_Type())
connUnitPortStatCountRxLinkResets.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountRxLinkResets.setStatus(_A)
class _ConnUnitPortStatCountTxLinkResets_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountTxLinkResets_Type.__name__=_C
_ConnUnitPortStatCountTxLinkResets_Object=MibTableColumn
connUnitPortStatCountTxLinkResets=_ConnUnitPortStatCountTxLinkResets_Object((1,3,6,1,3,94,4,5,1,34),_ConnUnitPortStatCountTxLinkResets_Type())
connUnitPortStatCountTxLinkResets.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountTxLinkResets.setStatus(_A)
class _ConnUnitPortStatCountNumberLinkResets_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountNumberLinkResets_Type.__name__=_C
_ConnUnitPortStatCountNumberLinkResets_Object=MibTableColumn
connUnitPortStatCountNumberLinkResets=_ConnUnitPortStatCountNumberLinkResets_Object((1,3,6,1,3,94,4,5,1,35),_ConnUnitPortStatCountNumberLinkResets_Type())
connUnitPortStatCountNumberLinkResets.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountNumberLinkResets.setStatus(_A)
class _ConnUnitPortStatCountRxOfflineSequences_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountRxOfflineSequences_Type.__name__=_C
_ConnUnitPortStatCountRxOfflineSequences_Object=MibTableColumn
connUnitPortStatCountRxOfflineSequences=_ConnUnitPortStatCountRxOfflineSequences_Object((1,3,6,1,3,94,4,5,1,36),_ConnUnitPortStatCountRxOfflineSequences_Type())
connUnitPortStatCountRxOfflineSequences.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountRxOfflineSequences.setStatus(_A)
class _ConnUnitPortStatCountTxOfflineSequences_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountTxOfflineSequences_Type.__name__=_C
_ConnUnitPortStatCountTxOfflineSequences_Object=MibTableColumn
connUnitPortStatCountTxOfflineSequences=_ConnUnitPortStatCountTxOfflineSequences_Object((1,3,6,1,3,94,4,5,1,37),_ConnUnitPortStatCountTxOfflineSequences_Type())
connUnitPortStatCountTxOfflineSequences.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountTxOfflineSequences.setStatus(_A)
class _ConnUnitPortStatCountNumberOfflineSequences_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountNumberOfflineSequences_Type.__name__=_C
_ConnUnitPortStatCountNumberOfflineSequences_Object=MibTableColumn
connUnitPortStatCountNumberOfflineSequences=_ConnUnitPortStatCountNumberOfflineSequences_Object((1,3,6,1,3,94,4,5,1,38),_ConnUnitPortStatCountNumberOfflineSequences_Type())
connUnitPortStatCountNumberOfflineSequences.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountNumberOfflineSequences.setStatus(_A)
class _ConnUnitPortStatCountLinkFailures_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountLinkFailures_Type.__name__=_C
_ConnUnitPortStatCountLinkFailures_Object=MibTableColumn
connUnitPortStatCountLinkFailures=_ConnUnitPortStatCountLinkFailures_Object((1,3,6,1,3,94,4,5,1,39),_ConnUnitPortStatCountLinkFailures_Type())
connUnitPortStatCountLinkFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountLinkFailures.setStatus(_A)
class _ConnUnitPortStatCountInvalidCRC_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountInvalidCRC_Type.__name__=_C
_ConnUnitPortStatCountInvalidCRC_Object=MibTableColumn
connUnitPortStatCountInvalidCRC=_ConnUnitPortStatCountInvalidCRC_Object((1,3,6,1,3,94,4,5,1,40),_ConnUnitPortStatCountInvalidCRC_Type())
connUnitPortStatCountInvalidCRC.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountInvalidCRC.setStatus(_A)
class _ConnUnitPortStatCountInvalidTxWords_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountInvalidTxWords_Type.__name__=_C
_ConnUnitPortStatCountInvalidTxWords_Object=MibTableColumn
connUnitPortStatCountInvalidTxWords=_ConnUnitPortStatCountInvalidTxWords_Object((1,3,6,1,3,94,4,5,1,41),_ConnUnitPortStatCountInvalidTxWords_Type())
connUnitPortStatCountInvalidTxWords.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountInvalidTxWords.setStatus(_A)
class _ConnUnitPortStatCountPrimitiveSequenceProtocolErrors_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountPrimitiveSequenceProtocolErrors_Type.__name__=_C
_ConnUnitPortStatCountPrimitiveSequenceProtocolErrors_Object=MibTableColumn
connUnitPortStatCountPrimitiveSequenceProtocolErrors=_ConnUnitPortStatCountPrimitiveSequenceProtocolErrors_Object((1,3,6,1,3,94,4,5,1,42),_ConnUnitPortStatCountPrimitiveSequenceProtocolErrors_Type())
connUnitPortStatCountPrimitiveSequenceProtocolErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountPrimitiveSequenceProtocolErrors.setStatus(_A)
class _ConnUnitPortStatCountLossofSignal_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountLossofSignal_Type.__name__=_C
_ConnUnitPortStatCountLossofSignal_Object=MibTableColumn
connUnitPortStatCountLossofSignal=_ConnUnitPortStatCountLossofSignal_Object((1,3,6,1,3,94,4,5,1,43),_ConnUnitPortStatCountLossofSignal_Type())
connUnitPortStatCountLossofSignal.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountLossofSignal.setStatus(_A)
class _ConnUnitPortStatCountLossofSynchronization_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountLossofSynchronization_Type.__name__=_C
_ConnUnitPortStatCountLossofSynchronization_Object=MibTableColumn
connUnitPortStatCountLossofSynchronization=_ConnUnitPortStatCountLossofSynchronization_Object((1,3,6,1,3,94,4,5,1,44),_ConnUnitPortStatCountLossofSynchronization_Type())
connUnitPortStatCountLossofSynchronization.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountLossofSynchronization.setStatus(_A)
class _ConnUnitPortStatCountInvalidOrderedSets_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountInvalidOrderedSets_Type.__name__=_C
_ConnUnitPortStatCountInvalidOrderedSets_Object=MibTableColumn
connUnitPortStatCountInvalidOrderedSets=_ConnUnitPortStatCountInvalidOrderedSets_Object((1,3,6,1,3,94,4,5,1,45),_ConnUnitPortStatCountInvalidOrderedSets_Type())
connUnitPortStatCountInvalidOrderedSets.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountInvalidOrderedSets.setStatus(_A)
class _ConnUnitPortStatCountFramesTooLong_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountFramesTooLong_Type.__name__=_C
_ConnUnitPortStatCountFramesTooLong_Object=MibTableColumn
connUnitPortStatCountFramesTooLong=_ConnUnitPortStatCountFramesTooLong_Object((1,3,6,1,3,94,4,5,1,46),_ConnUnitPortStatCountFramesTooLong_Type())
connUnitPortStatCountFramesTooLong.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountFramesTooLong.setStatus(_A)
class _ConnUnitPortStatCountFramesTruncated_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountFramesTruncated_Type.__name__=_C
_ConnUnitPortStatCountFramesTruncated_Object=MibTableColumn
connUnitPortStatCountFramesTruncated=_ConnUnitPortStatCountFramesTruncated_Object((1,3,6,1,3,94,4,5,1,47),_ConnUnitPortStatCountFramesTruncated_Type())
connUnitPortStatCountFramesTruncated.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountFramesTruncated.setStatus(_A)
class _ConnUnitPortStatCountAddressErrors_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountAddressErrors_Type.__name__=_C
_ConnUnitPortStatCountAddressErrors_Object=MibTableColumn
connUnitPortStatCountAddressErrors=_ConnUnitPortStatCountAddressErrors_Object((1,3,6,1,3,94,4,5,1,48),_ConnUnitPortStatCountAddressErrors_Type())
connUnitPortStatCountAddressErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountAddressErrors.setStatus(_A)
class _ConnUnitPortStatCountDelimiterErrors_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountDelimiterErrors_Type.__name__=_C
_ConnUnitPortStatCountDelimiterErrors_Object=MibTableColumn
connUnitPortStatCountDelimiterErrors=_ConnUnitPortStatCountDelimiterErrors_Object((1,3,6,1,3,94,4,5,1,49),_ConnUnitPortStatCountDelimiterErrors_Type())
connUnitPortStatCountDelimiterErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountDelimiterErrors.setStatus(_A)
class _ConnUnitPortStatCountEncodingDisparityErrors_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitPortStatCountEncodingDisparityErrors_Type.__name__=_C
_ConnUnitPortStatCountEncodingDisparityErrors_Object=MibTableColumn
connUnitPortStatCountEncodingDisparityErrors=_ConnUnitPortStatCountEncodingDisparityErrors_Object((1,3,6,1,3,94,4,5,1,50),_ConnUnitPortStatCountEncodingDisparityErrors_Type())
connUnitPortStatCountEncodingDisparityErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPortStatCountEncodingDisparityErrors.setStatus(_A)
_ConnUnitServiceSet_ObjectIdentity=ObjectIdentity
connUnitServiceSet=_ConnUnitServiceSet_ObjectIdentity((1,3,6,1,3,94,5))
_ConnUnitServiceScalars_ObjectIdentity=ObjectIdentity
connUnitServiceScalars=_ConnUnitServiceScalars_ObjectIdentity((1,3,6,1,3,94,5,1))
_ConnUnitSnsMaxEntry_Type=Integer32
_ConnUnitSnsMaxEntry_Object=MibScalar
connUnitSnsMaxEntry=_ConnUnitSnsMaxEntry_Object((1,3,6,1,3,94,5,1,1),_ConnUnitSnsMaxEntry_Type())
connUnitSnsMaxEntry.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitSnsMaxEntry.setStatus(_A)
_ConnUnitPlatformMaxEntry_Type=Integer32
_ConnUnitPlatformMaxEntry_Object=MibScalar
connUnitPlatformMaxEntry=_ConnUnitPlatformMaxEntry_Object((1,3,6,1,3,94,5,1,2),_ConnUnitPlatformMaxEntry_Type())
connUnitPlatformMaxEntry.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPlatformMaxEntry.setStatus(_A)
_ConnUnitServiceTables_ObjectIdentity=ObjectIdentity
connUnitServiceTables=_ConnUnitServiceTables_ObjectIdentity((1,3,6,1,3,94,5,2))
_ConnUnitSnsTable_Object=MibTable
connUnitSnsTable=_ConnUnitSnsTable_Object((1,3,6,1,3,94,5,2,1))
if mibBuilder.loadTexts:connUnitSnsTable.setStatus(_A)
_ConnUnitSnsEntry_Object=MibTableRow
connUnitSnsEntry=_ConnUnitSnsEntry_Object((1,3,6,1,3,94,5,2,1,1))
connUnitSnsEntry.setIndexNames((0,_D,_m),(0,_D,_n),(0,_D,_o))
if mibBuilder.loadTexts:connUnitSnsEntry.setStatus(_A)
class _ConnUnitSnsId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_ConnUnitSnsId_Type.__name__=_C
_ConnUnitSnsId_Object=MibTableColumn
connUnitSnsId=_ConnUnitSnsId_Object((1,3,6,1,3,94,5,2,1,1,1),_ConnUnitSnsId_Type())
connUnitSnsId.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitSnsId.setStatus(_A)
_ConnUnitSnsPortIndex_Type=Integer32
_ConnUnitSnsPortIndex_Object=MibTableColumn
connUnitSnsPortIndex=_ConnUnitSnsPortIndex_Object((1,3,6,1,3,94,5,2,1,1,2),_ConnUnitSnsPortIndex_Type())
connUnitSnsPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitSnsPortIndex.setStatus(_A)
_ConnUnitSnsPortIdentifier_Type=FcAddressId
_ConnUnitSnsPortIdentifier_Object=MibTableColumn
connUnitSnsPortIdentifier=_ConnUnitSnsPortIdentifier_Object((1,3,6,1,3,94,5,2,1,1,3),_ConnUnitSnsPortIdentifier_Type())
connUnitSnsPortIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitSnsPortIdentifier.setStatus(_A)
_ConnUnitSnsPortName_Type=FcNameId
_ConnUnitSnsPortName_Object=MibTableColumn
connUnitSnsPortName=_ConnUnitSnsPortName_Object((1,3,6,1,3,94,5,2,1,1,4),_ConnUnitSnsPortName_Type())
connUnitSnsPortName.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitSnsPortName.setStatus(_A)
_ConnUnitSnsNodeName_Type=FcNameId
_ConnUnitSnsNodeName_Object=MibTableColumn
connUnitSnsNodeName=_ConnUnitSnsNodeName_Object((1,3,6,1,3,94,5,2,1,1,5),_ConnUnitSnsNodeName_Type())
connUnitSnsNodeName.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitSnsNodeName.setStatus(_A)
class _ConnUnitSnsClassOfSvc_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_ConnUnitSnsClassOfSvc_Type.__name__=_C
_ConnUnitSnsClassOfSvc_Object=MibTableColumn
connUnitSnsClassOfSvc=_ConnUnitSnsClassOfSvc_Object((1,3,6,1,3,94,5,2,1,1,6),_ConnUnitSnsClassOfSvc_Type())
connUnitSnsClassOfSvc.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitSnsClassOfSvc.setStatus(_A)
class _ConnUnitSnsNodeIPAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_ConnUnitSnsNodeIPAddress_Type.__name__=_C
_ConnUnitSnsNodeIPAddress_Object=MibTableColumn
connUnitSnsNodeIPAddress=_ConnUnitSnsNodeIPAddress_Object((1,3,6,1,3,94,5,2,1,1,7),_ConnUnitSnsNodeIPAddress_Type())
connUnitSnsNodeIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitSnsNodeIPAddress.setStatus(_A)
class _ConnUnitSnsProcAssoc_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ConnUnitSnsProcAssoc_Type.__name__=_C
_ConnUnitSnsProcAssoc_Object=MibTableColumn
connUnitSnsProcAssoc=_ConnUnitSnsProcAssoc_Object((1,3,6,1,3,94,5,2,1,1,8),_ConnUnitSnsProcAssoc_Type())
connUnitSnsProcAssoc.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitSnsProcAssoc.setStatus(_A)
class _ConnUnitSnsFC4Type_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_ConnUnitSnsFC4Type_Type.__name__=_C
_ConnUnitSnsFC4Type_Object=MibTableColumn
connUnitSnsFC4Type=_ConnUnitSnsFC4Type_Object((1,3,6,1,3,94,5,2,1,1,9),_ConnUnitSnsFC4Type_Type())
connUnitSnsFC4Type.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitSnsFC4Type.setStatus(_A)
class _ConnUnitSnsPortType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_ConnUnitSnsPortType_Type.__name__=_C
_ConnUnitSnsPortType_Object=MibTableColumn
connUnitSnsPortType=_ConnUnitSnsPortType_Object((1,3,6,1,3,94,5,2,1,1,10),_ConnUnitSnsPortType_Type())
connUnitSnsPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitSnsPortType.setStatus(_A)
class _ConnUnitSnsPortIPAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_ConnUnitSnsPortIPAddress_Type.__name__=_C
_ConnUnitSnsPortIPAddress_Object=MibTableColumn
connUnitSnsPortIPAddress=_ConnUnitSnsPortIPAddress_Object((1,3,6,1,3,94,5,2,1,1,11),_ConnUnitSnsPortIPAddress_Type())
connUnitSnsPortIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitSnsPortIPAddress.setStatus(_A)
_ConnUnitSnsFabricPortName_Type=FcNameId
_ConnUnitSnsFabricPortName_Object=MibTableColumn
connUnitSnsFabricPortName=_ConnUnitSnsFabricPortName_Object((1,3,6,1,3,94,5,2,1,1,12),_ConnUnitSnsFabricPortName_Type())
connUnitSnsFabricPortName.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitSnsFabricPortName.setStatus(_A)
_ConnUnitSnsHardAddress_Type=FcGlobalId
_ConnUnitSnsHardAddress_Object=MibTableColumn
connUnitSnsHardAddress=_ConnUnitSnsHardAddress_Object((1,3,6,1,3,94,5,2,1,1,13),_ConnUnitSnsHardAddress_Type())
connUnitSnsHardAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitSnsHardAddress.setStatus(_A)
class _ConnUnitSnsSymbolicPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_ConnUnitSnsSymbolicPortName_Type.__name__=_F
_ConnUnitSnsSymbolicPortName_Object=MibTableColumn
connUnitSnsSymbolicPortName=_ConnUnitSnsSymbolicPortName_Object((1,3,6,1,3,94,5,2,1,1,14),_ConnUnitSnsSymbolicPortName_Type())
connUnitSnsSymbolicPortName.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitSnsSymbolicPortName.setStatus(_A)
class _ConnUnitSnsSymbolicNodeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_ConnUnitSnsSymbolicNodeName_Type.__name__=_F
_ConnUnitSnsSymbolicNodeName_Object=MibTableColumn
connUnitSnsSymbolicNodeName=_ConnUnitSnsSymbolicNodeName_Object((1,3,6,1,3,94,5,2,1,1,15),_ConnUnitSnsSymbolicNodeName_Type())
connUnitSnsSymbolicNodeName.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitSnsSymbolicNodeName.setStatus(_A)
_ConnUnitPlatformTable_Object=MibTable
connUnitPlatformTable=_ConnUnitPlatformTable_Object((1,3,6,1,3,94,5,2,2))
if mibBuilder.loadTexts:connUnitPlatformTable.setStatus(_A)
_ConnUnitPlatformEntry_Object=MibTableRow
connUnitPlatformEntry=_ConnUnitPlatformEntry_Object((1,3,6,1,3,94,5,2,2,1))
connUnitPlatformEntry.setIndexNames((0,_D,_p),(0,_D,_q))
if mibBuilder.loadTexts:connUnitPlatformEntry.setStatus(_A)
class _ConnUnitPlatformIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ConnUnitPlatformIndex_Type.__name__=_E
_ConnUnitPlatformIndex_Object=MibTableColumn
connUnitPlatformIndex=_ConnUnitPlatformIndex_Object((1,3,6,1,3,94,5,2,2,1,1),_ConnUnitPlatformIndex_Type())
connUnitPlatformIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPlatformIndex.setStatus(_A)
class _ConnUnitPlatformNodeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ConnUnitPlatformNodeIndex_Type.__name__=_E
_ConnUnitPlatformNodeIndex_Object=MibTableColumn
connUnitPlatformNodeIndex=_ConnUnitPlatformNodeIndex_Object((1,3,6,1,3,94,5,2,2,1,2),_ConnUnitPlatformNodeIndex_Type())
connUnitPlatformNodeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPlatformNodeIndex.setStatus(_A)
_ConnUnitPlatformUnitID_Type=FcGlobalId
_ConnUnitPlatformUnitID_Object=MibTableColumn
connUnitPlatformUnitID=_ConnUnitPlatformUnitID_Object((1,3,6,1,3,94,5,2,2,1,3),_ConnUnitPlatformUnitID_Type())
connUnitPlatformUnitID.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPlatformUnitID.setStatus(_A)
class _ConnUnitPlatformName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(79,79));fixedLength=79
_ConnUnitPlatformName_Type.__name__=_C
_ConnUnitPlatformName_Object=MibTableColumn
connUnitPlatformName=_ConnUnitPlatformName_Object((1,3,6,1,3,94,5,2,2,1,4),_ConnUnitPlatformName_Type())
connUnitPlatformName.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPlatformName.setStatus(_A)
_ConnUnitPlatformType_Type=FcUnitType
_ConnUnitPlatformType_Object=MibTableColumn
connUnitPlatformType=_ConnUnitPlatformType_Object((1,3,6,1,3,94,5,2,2,1,6),_ConnUnitPlatformType_Type())
connUnitPlatformType.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPlatformType.setStatus(_A)
class _ConnUnitPlatformLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_ConnUnitPlatformLabel_Type.__name__=_F
_ConnUnitPlatformLabel_Object=MibTableColumn
connUnitPlatformLabel=_ConnUnitPlatformLabel_Object((1,3,6,1,3,94,5,2,2,1,7),_ConnUnitPlatformLabel_Type())
connUnitPlatformLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPlatformLabel.setStatus(_A)
class _ConnUnitPlatformDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_ConnUnitPlatformDescription_Type.__name__=_F
_ConnUnitPlatformDescription_Object=MibTableColumn
connUnitPlatformDescription=_ConnUnitPlatformDescription_Object((1,3,6,1,3,94,5,2,2,1,8),_ConnUnitPlatformDescription_Type())
connUnitPlatformDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPlatformDescription.setStatus(_A)
class _ConnUnitPlatformLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_ConnUnitPlatformLocation_Type.__name__=_F
_ConnUnitPlatformLocation_Object=MibTableColumn
connUnitPlatformLocation=_ConnUnitPlatformLocation_Object((1,3,6,1,3,94,5,2,2,1,9),_ConnUnitPlatformLocation_Type())
connUnitPlatformLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPlatformLocation.setStatus(_A)
class _ConnUnitPlatformManagementUrl_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_ConnUnitPlatformManagementUrl_Type.__name__=_F
_ConnUnitPlatformManagementUrl_Object=MibTableColumn
connUnitPlatformManagementUrl=_ConnUnitPlatformManagementUrl_Object((1,3,6,1,3,94,5,2,2,1,10),_ConnUnitPlatformManagementUrl_Type())
connUnitPlatformManagementUrl.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPlatformManagementUrl.setStatus(_A)
_ConnUnitPlatformNumNodes_Type=Integer32
_ConnUnitPlatformNumNodes_Object=MibTableColumn
connUnitPlatformNumNodes=_ConnUnitPlatformNumNodes_Object((1,3,6,1,3,94,5,2,2,1,11),_ConnUnitPlatformNumNodes_Type())
connUnitPlatformNumNodes.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPlatformNumNodes.setStatus(_A)
_ConnUnitPlatformNodeName_Type=FcGlobalId
_ConnUnitPlatformNodeName_Object=MibTableColumn
connUnitPlatformNodeName=_ConnUnitPlatformNodeName_Object((1,3,6,1,3,94,5,2,2,1,12),_ConnUnitPlatformNodeName_Type())
connUnitPlatformNodeName.setMaxAccess(_B)
if mibBuilder.loadTexts:connUnitPlatformNodeName.setStatus(_A)
connUnitStatusChange=NotificationType((1,3,6,1,3,94,0,1))
connUnitStatusChange.setObjects(*((_D,_r),(_D,_s)))
if mibBuilder.loadTexts:connUnitStatusChange.setStatus('')
connUnitDeletedTrap=NotificationType((1,3,6,1,3,94,0,3))
connUnitDeletedTrap.setObjects((_D,_L))
if mibBuilder.loadTexts:connUnitDeletedTrap.setStatus('')
connUnitEventTrap=NotificationType((1,3,6,1,3,94,0,4))
connUnitEventTrap.setObjects(*((_D,_t),(_D,_u),(_D,_v),(_D,_w)))
if mibBuilder.loadTexts:connUnitEventTrap.setStatus('')
connUnitSensorStatusChange=NotificationType((1,3,6,1,3,94,0,5))
connUnitSensorStatusChange.setObjects((_D,_x))
if mibBuilder.loadTexts:connUnitSensorStatusChange.setStatus('')
connUnitPortStatusChange=NotificationType((1,3,6,1,3,94,0,6))
connUnitPortStatusChange.setObjects(*((_D,_y),(_D,_z)))
if mibBuilder.loadTexts:connUnitPortStatusChange.setStatus('')
mibBuilder.exportSymbols(_D,**{'FcNameId':FcNameId,'FcGlobalId':FcGlobalId,'FcAddressId':FcAddressId,'FcEventSeverity':FcEventSeverity,'FcUnitType':FcUnitType,'fcmgmt':fcmgmt,'connUnitStatusChange':connUnitStatusChange,'connUnitDeletedTrap':connUnitDeletedTrap,'connUnitEventTrap':connUnitEventTrap,'connUnitSensorStatusChange':connUnitSensorStatusChange,'connUnitPortStatusChange':connUnitPortStatusChange,'connSet':connSet,'uNumber':uNumber,'systemURL':systemURL,'statusChangeTime':statusChangeTime,'configurationChangeTime':configurationChangeTime,'connUnitTableChangeTime':connUnitTableChangeTime,'connUnitTable':connUnitTable,'connUnitEntry':connUnitEntry,_L:connUnitId,'connUnitGlobalId':connUnitGlobalId,'connUnitType':connUnitType,'connUnitNumports':connUnitNumports,_s:connUnitState,_r:connUnitStatus,'connUnitProduct':connUnitProduct,'connUnitSn':connUnitSn,'connUnitUpTime':connUnitUpTime,'connUnitUrl':connUnitUrl,'connUnitDomainId':connUnitDomainId,'connUnitProxyMaster':connUnitProxyMaster,'connUnitPrincipal':connUnitPrincipal,'connUnitNumSensors':connUnitNumSensors,'connUnitStatusChangeTime':connUnitStatusChangeTime,'connUnitConfigurationChangeTime':connUnitConfigurationChangeTime,'connUnitNumRevs':connUnitNumRevs,'connUnitNumZones':connUnitNumZones,'connUnitModuleId':connUnitModuleId,'connUnitName':connUnitName,'connUnitInfo':connUnitInfo,'connUnitControl':connUnitControl,'connUnitContact':connUnitContact,'connUnitLocation':connUnitLocation,'connUnitEventFilter':connUnitEventFilter,'connUnitNumEvents':connUnitNumEvents,'connUnitMaxEvents':connUnitMaxEvents,'connUnitEventCurrID':connUnitEventCurrID,'connUnitFabricID':connUnitFabricID,'connUnitNumLinks':connUnitNumLinks,'connUnitVendorId':connUnitVendorId,'connUnitRevsTable':connUnitRevsTable,'connUnitRevsEntry':connUnitRevsEntry,_S:connUnitRevsUnitId,_T:connUnitRevsIndex,'connUnitRevsRevId':connUnitRevsRevId,'connUnitRevsDescription':connUnitRevsDescription,'connUnitSensorTable':connUnitSensorTable,'connUnitSensorEntry':connUnitSensorEntry,_U:connUnitSensorUnitId,_V:connUnitSensorIndex,'connUnitSensorName':connUnitSensorName,_x:connUnitSensorStatus,'connUnitSensorInfo':connUnitSensorInfo,'connUnitSensorMessage':connUnitSensorMessage,'connUnitSensorType':connUnitSensorType,'connUnitSensorCharacteristic':connUnitSensorCharacteristic,'connUnitPortTable':connUnitPortTable,'connUnitPortEntry':connUnitPortEntry,_W:connUnitPortUnitId,_X:connUnitPortIndex,'connUnitPortType':connUnitPortType,'connUnitPortFCClassCap':connUnitPortFCClassCap,'connUnitPortFCClassOp':connUnitPortFCClassOp,_z:connUnitPortState,_y:connUnitPortStatus,'connUnitPortTransmitterType':connUnitPortTransmitterType,'connUnitPortModuleType':connUnitPortModuleType,'connUnitPortWwn':connUnitPortWwn,'connUnitPortFCId':connUnitPortFCId,'connUnitPortSn':connUnitPortSn,'connUnitPortRevision':connUnitPortRevision,'connUnitPortVendor':connUnitPortVendor,'connUnitPortSpeed':connUnitPortSpeed,'connUnitPortControl':connUnitPortControl,'connUnitPortName':connUnitPortName,'connUnitPortPhysicalNumber':connUnitPortPhysicalNumber,'connUnitPortStatObject':connUnitPortStatObject,'connUnitPortProtocolCap':connUnitPortProtocolCap,'connUnitPortProtocolOp':connUnitPortProtocolOp,'connUnitPortNodeWwn':connUnitPortNodeWwn,'connUnitPortHWState':connUnitPortHWState,'connUnitEventTable':connUnitEventTable,'connUnitEventEntry':connUnitEventEntry,_a:connUnitEventUnitId,_b:connUnitEventIndex,_t:connUnitEventId,'connUnitREventTime':connUnitREventTime,'connUnitSEventTime':connUnitSEventTime,'connUnitEventSeverity':connUnitEventSeverity,_u:connUnitEventType,_v:connUnitEventObject,_w:connUnitEventDescr,'connUnitLinkTable':connUnitLinkTable,'connUnitLinkEntry':connUnitLinkEntry,_c:connUnitLinkUnitId,_d:connUnitLinkIndex,'connUnitLinkNodeIdX':connUnitLinkNodeIdX,'connUnitLinkPortNumberX':connUnitLinkPortNumberX,'connUnitLinkPortWwnX':connUnitLinkPortWwnX,'connUnitLinkNodeIdY':connUnitLinkNodeIdY,'connUnitLinkPortNumberY':connUnitLinkPortNumberY,'connUnitLinkPortWwnY':connUnitLinkPortWwnY,'connUnitLinkAgentAddressY':connUnitLinkAgentAddressY,'connUnitLinkAgentAddressTypeY':connUnitLinkAgentAddressTypeY,'connUnitLinkAgentPortY':connUnitLinkAgentPortY,'connUnitLinkUnitTypeY':connUnitLinkUnitTypeY,'connUnitLinkConnIdY':connUnitLinkConnIdY,'connUnitLinkCurrIndex':connUnitLinkCurrIndex,'connUnitZoneTable':connUnitZoneTable,'connUnitZoneEntry':connUnitZoneEntry,_e:connUnitZoneIndex,_f:connUnitZoneMemberIndex,'connUnitZoneSetName':connUnitZoneSetName,'connUnitZoneSetNumZones':connUnitZoneSetNumZones,'connUnitZoneName':connUnitZoneName,'connUnitZoneCapabilities':connUnitZoneCapabilities,'connUnitZoneEnforcementState':connUnitZoneEnforcementState,'connUnitZoneAttributeBlock':connUnitZoneAttributeBlock,'connUnitZoneNumMembers':connUnitZoneNumMembers,'connUnitZoneMemberIdType':connUnitZoneMemberIdType,'connUnitZoneMemberID':connUnitZoneMemberID,'connUnitZoningAliasTable':connUnitZoningAliasTable,'connUnitZoningAliasEntry':connUnitZoningAliasEntry,_g:connUnitZoningAliasIndex,_h:connUnitZoningAliasMemberIndex,'connUnitZoningAliasNumAliases':connUnitZoningAliasNumAliases,'connUnitZoningAliasName':connUnitZoningAliasName,'connUnitZoningAliasNumMembers':connUnitZoningAliasNumMembers,'connUnitZoningAliasMemberIdType':connUnitZoningAliasMemberIdType,'connUnitZoningAliasMemberID':connUnitZoningAliasMemberID,'trapReg':trapReg,'trapMaxClients':trapMaxClients,'trapClientCount':trapClientCount,'trapRegTable':trapRegTable,'trapRegEntry':trapRegEntry,_i:trapRegIpAddress,_j:trapRegPort,'trapRegFilter':trapRegFilter,'trapRegRowState':trapRegRowState,'revisionNumber':revisionNumber,'statSet':statSet,'connUnitPortStatTable':connUnitPortStatTable,'connUnitPortStatEntry':connUnitPortStatEntry,_k:connUnitPortStatUnitId,_l:connUnitPortStatIndex,'connUnitPortStatCountError':connUnitPortStatCountError,'connUnitPortStatCountTxObjects':connUnitPortStatCountTxObjects,'connUnitPortStatCountRxObjects':connUnitPortStatCountRxObjects,'connUnitPortStatCountTxElements':connUnitPortStatCountTxElements,'connUnitPortStatCountRxElements':connUnitPortStatCountRxElements,'connUnitPortStatCountBBCreditZero':connUnitPortStatCountBBCreditZero,'connUnitPortStatCountInputBuffersFull':connUnitPortStatCountInputBuffersFull,'connUnitPortStatCountFBSYFrames':connUnitPortStatCountFBSYFrames,'connUnitPortStatCountPBSYFrames':connUnitPortStatCountPBSYFrames,'connUnitPortStatCountFRJTFrames':connUnitPortStatCountFRJTFrames,'connUnitPortStatCountPRJTFrames':connUnitPortStatCountPRJTFrames,'connUnitPortStatCountClass1RxFrames':connUnitPortStatCountClass1RxFrames,'connUnitPortStatCountClass1TxFrames':connUnitPortStatCountClass1TxFrames,'connUnitPortStatCountClass1FBSYFrames':connUnitPortStatCountClass1FBSYFrames,'connUnitPortStatCountClass1PBSYFrames':connUnitPortStatCountClass1PBSYFrames,'connUnitPortStatCountClass1FRJTFrames':connUnitPortStatCountClass1FRJTFrames,'connUnitPortStatCountClass1PRJTFrames':connUnitPortStatCountClass1PRJTFrames,'connUnitPortStatCountClass2RxFrames':connUnitPortStatCountClass2RxFrames,'connUnitPortStatCountClass2TxFrames':connUnitPortStatCountClass2TxFrames,'connUnitPortStatCountClass2FBSYFrames':connUnitPortStatCountClass2FBSYFrames,'connUnitPortStatCountClass2PBSYFrames':connUnitPortStatCountClass2PBSYFrames,'connUnitPortStatCountClass2FRJTFrames':connUnitPortStatCountClass2FRJTFrames,'connUnitPortStatCountClass2PRJTFrames':connUnitPortStatCountClass2PRJTFrames,'connUnitPortStatCountClass3RxFrames':connUnitPortStatCountClass3RxFrames,'connUnitPortStatCountClass3TxFrames':connUnitPortStatCountClass3TxFrames,'connUnitPortStatCountClass3Discards':connUnitPortStatCountClass3Discards,'connUnitPortStatCountRxMulticastObjects':connUnitPortStatCountRxMulticastObjects,'connUnitPortStatCountTxMulticastObjects':connUnitPortStatCountTxMulticastObjects,'connUnitPortStatCountRxBroadcastObjects':connUnitPortStatCountRxBroadcastObjects,'connUnitPortStatCountTxBroadcastObjects':connUnitPortStatCountTxBroadcastObjects,'connUnitPortStatCountRxLinkResets':connUnitPortStatCountRxLinkResets,'connUnitPortStatCountTxLinkResets':connUnitPortStatCountTxLinkResets,'connUnitPortStatCountNumberLinkResets':connUnitPortStatCountNumberLinkResets,'connUnitPortStatCountRxOfflineSequences':connUnitPortStatCountRxOfflineSequences,'connUnitPortStatCountTxOfflineSequences':connUnitPortStatCountTxOfflineSequences,'connUnitPortStatCountNumberOfflineSequences':connUnitPortStatCountNumberOfflineSequences,'connUnitPortStatCountLinkFailures':connUnitPortStatCountLinkFailures,'connUnitPortStatCountInvalidCRC':connUnitPortStatCountInvalidCRC,'connUnitPortStatCountInvalidTxWords':connUnitPortStatCountInvalidTxWords,'connUnitPortStatCountPrimitiveSequenceProtocolErrors':connUnitPortStatCountPrimitiveSequenceProtocolErrors,'connUnitPortStatCountLossofSignal':connUnitPortStatCountLossofSignal,'connUnitPortStatCountLossofSynchronization':connUnitPortStatCountLossofSynchronization,'connUnitPortStatCountInvalidOrderedSets':connUnitPortStatCountInvalidOrderedSets,'connUnitPortStatCountFramesTooLong':connUnitPortStatCountFramesTooLong,'connUnitPortStatCountFramesTruncated':connUnitPortStatCountFramesTruncated,'connUnitPortStatCountAddressErrors':connUnitPortStatCountAddressErrors,'connUnitPortStatCountDelimiterErrors':connUnitPortStatCountDelimiterErrors,'connUnitPortStatCountEncodingDisparityErrors':connUnitPortStatCountEncodingDisparityErrors,'connUnitServiceSet':connUnitServiceSet,'connUnitServiceScalars':connUnitServiceScalars,'connUnitSnsMaxEntry':connUnitSnsMaxEntry,'connUnitPlatformMaxEntry':connUnitPlatformMaxEntry,'connUnitServiceTables':connUnitServiceTables,'connUnitSnsTable':connUnitSnsTable,'connUnitSnsEntry':connUnitSnsEntry,_m:connUnitSnsId,'connUnitSnsPortIndex':connUnitSnsPortIndex,_o:connUnitSnsPortIdentifier,_n:connUnitSnsPortName,'connUnitSnsNodeName':connUnitSnsNodeName,'connUnitSnsClassOfSvc':connUnitSnsClassOfSvc,'connUnitSnsNodeIPAddress':connUnitSnsNodeIPAddress,'connUnitSnsProcAssoc':connUnitSnsProcAssoc,'connUnitSnsFC4Type':connUnitSnsFC4Type,'connUnitSnsPortType':connUnitSnsPortType,'connUnitSnsPortIPAddress':connUnitSnsPortIPAddress,'connUnitSnsFabricPortName':connUnitSnsFabricPortName,'connUnitSnsHardAddress':connUnitSnsHardAddress,'connUnitSnsSymbolicPortName':connUnitSnsSymbolicPortName,'connUnitSnsSymbolicNodeName':connUnitSnsSymbolicNodeName,'connUnitPlatformTable':connUnitPlatformTable,'connUnitPlatformEntry':connUnitPlatformEntry,_p:connUnitPlatformIndex,_q:connUnitPlatformNodeIndex,'connUnitPlatformUnitID':connUnitPlatformUnitID,'connUnitPlatformName':connUnitPlatformName,'connUnitPlatformType':connUnitPlatformType,'connUnitPlatformLabel':connUnitPlatformLabel,'connUnitPlatformDescription':connUnitPlatformDescription,'connUnitPlatformLocation':connUnitPlatformLocation,'connUnitPlatformManagementUrl':connUnitPlatformManagementUrl,'connUnitPlatformNumNodes':connUnitPlatformNumNodes,'connUnitPlatformNodeName':connUnitPlatformNodeName})