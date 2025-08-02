_p='cApsChanAssociationGroup'
_o='cApsChanConfigExt'
_n='cApsChanAssociationIpAddress'
_m='cApsChanAssociationIpAddressType'
_l='cApsChanConfigReflectorMode'
_k='cApsChanStatusExtRequest'
_j='cApsStatusMessageTransport'
_i='cApsConfigFarEndIpAddress'
_h='cApsConfigFarEndIpAddressType'
_g='cApsConfigFarEndGroupName'
_f='cApsConfigMessageMaxInterval'
_e='cApsConfigMessageHolddownCount'
_d='cApsConfigMessageHolddown'
_c='cApsConfigMessageTransport'
_b='cApsConfigSwitchoverEnableInterval'
_a='cApsStatusCdlApsBytesTrans'
_Z='cApsStatusCdlApsBytesRcv'
_Y='cApsConfigMaxSearchUpInterval'
_X='cApsConfigMinSearchUpInterval'
_W='cApsConfigYcable'
_V='cApsConfigSpan'
_U='cApsNotifiesEnable'
_T='cApsChanConfigExtEntry'
_S='cApsChanStatusExtEntry'
_R='cApsStatusExtEntry'
_Q='cApsConfigExtEntry'
_P='cApsChanAssociationMapNumber'
_O='cApsChanAssociationNumber'
_N='cApsChanAssociationGroupName'
_M='milliseconds'
_L='CApsMessageTransport'
_K='seconds'
_J='InetAddressType'
_I='cApsConfigPathExt'
_H='cApsNotifiesEnableGroup'
_G='not-accessible'
_F='SnmpAdminString'
_E='read-only'
_D='Integer32'
_C='read-create'
_B='CISCO-APS-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CApsK1K2,cApsChanConfigEntry,cApsChanStatusEntry,cApsConfigEntry,cApsStatusEntry=mibBuilder.importSymbols('CISCO-APS-MIB','CApsK1K2','cApsChanConfigEntry','cApsChanStatusEntry','cApsConfigEntry','cApsStatusEntry')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_J)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
cApsExtMIB=ModuleIdentity((1,3,6,1,4,1,9,10,72))
if mibBuilder.loadTexts:cApsExtMIB.setRevisions(('2003-01-31 00:00','2002-05-31 00:00','2002-05-20 00:00','2001-05-21 00:00'))
class CdlApsBytes(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
class CApsMessageTransport(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('none',1),('autoSelect',2),('dcc',3),('apsChannel',4),('ip',5),('osc',6)))
class CApsChannelConfigNumber(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,14))
_CApsExtMIBObjects_ObjectIdentity=ObjectIdentity
cApsExtMIBObjects=_CApsExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,72,1))
_CApsNotifiesEnable_Type=TruthValue
_CApsNotifiesEnable_Object=MibScalar
cApsNotifiesEnable=_CApsNotifiesEnable_Object((1,3,6,1,4,1,9,10,72,1,1),_CApsNotifiesEnable_Type())
cApsNotifiesEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:cApsNotifiesEnable.setStatus(_A)
_CApsConfigExtTable_Object=MibTable
cApsConfigExtTable=_CApsConfigExtTable_Object((1,3,6,1,4,1,9,10,72,1,2))
if mibBuilder.loadTexts:cApsConfigExtTable.setStatus(_A)
_CApsConfigExtEntry_Object=MibTableRow
cApsConfigExtEntry=_CApsConfigExtEntry_Object((1,3,6,1,4,1,9,10,72,1,2,1))
if mibBuilder.loadTexts:cApsConfigExtEntry.setStatus(_A)
class _CApsConfigSpan_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('hopByHop',1),('endToEnd',2)))
_CApsConfigSpan_Type.__name__=_D
_CApsConfigSpan_Object=MibTableColumn
cApsConfigSpan=_CApsConfigSpan_Object((1,3,6,1,4,1,9,10,72,1,2,1,1),_CApsConfigSpan_Type())
cApsConfigSpan.setMaxAccess(_C)
if mibBuilder.loadTexts:cApsConfigSpan.setStatus(_A)
class _CApsConfigYcable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noYcable',1),('ycable',2),('ycableXconnectCommon',3)))
_CApsConfigYcable_Type.__name__=_D
_CApsConfigYcable_Object=MibTableColumn
cApsConfigYcable=_CApsConfigYcable_Object((1,3,6,1,4,1,9,10,72,1,2,1,2),_CApsConfigYcable_Type())
cApsConfigYcable.setMaxAccess(_C)
if mibBuilder.loadTexts:cApsConfigYcable.setStatus(_A)
class _CApsConfigMinSearchUpInterval_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,120))
_CApsConfigMinSearchUpInterval_Type.__name__=_D
_CApsConfigMinSearchUpInterval_Object=MibTableColumn
cApsConfigMinSearchUpInterval=_CApsConfigMinSearchUpInterval_Object((1,3,6,1,4,1,9,10,72,1,2,1,3),_CApsConfigMinSearchUpInterval_Type())
cApsConfigMinSearchUpInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cApsConfigMinSearchUpInterval.setStatus(_A)
class _CApsConfigMaxSearchUpInterval_Type(Integer32):defaultValue=32;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,120))
_CApsConfigMaxSearchUpInterval_Type.__name__=_D
_CApsConfigMaxSearchUpInterval_Object=MibTableColumn
cApsConfigMaxSearchUpInterval=_CApsConfigMaxSearchUpInterval_Object((1,3,6,1,4,1,9,10,72,1,2,1,4),_CApsConfigMaxSearchUpInterval_Type())
cApsConfigMaxSearchUpInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cApsConfigMaxSearchUpInterval.setStatus(_A)
if mibBuilder.loadTexts:cApsConfigMaxSearchUpInterval.setUnits(_K)
class _CApsConfigSwitchoverEnableInterval_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,120))
_CApsConfigSwitchoverEnableInterval_Type.__name__=_D
_CApsConfigSwitchoverEnableInterval_Object=MibTableColumn
cApsConfigSwitchoverEnableInterval=_CApsConfigSwitchoverEnableInterval_Object((1,3,6,1,4,1,9,10,72,1,2,1,5),_CApsConfigSwitchoverEnableInterval_Type())
cApsConfigSwitchoverEnableInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cApsConfigSwitchoverEnableInterval.setStatus(_A)
if mibBuilder.loadTexts:cApsConfigSwitchoverEnableInterval.setUnits(_K)
class _CApsConfigMessageTransport_Type(CApsMessageTransport):defaultValue=2
_CApsConfigMessageTransport_Type.__name__=_L
_CApsConfigMessageTransport_Object=MibTableColumn
cApsConfigMessageTransport=_CApsConfigMessageTransport_Object((1,3,6,1,4,1,9,10,72,1,2,1,6),_CApsConfigMessageTransport_Type())
cApsConfigMessageTransport.setMaxAccess(_C)
if mibBuilder.loadTexts:cApsConfigMessageTransport.setStatus(_A)
class _CApsConfigMessageHolddown_Type(Integer32):defaultValue=5000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,10000))
_CApsConfigMessageHolddown_Type.__name__=_D
_CApsConfigMessageHolddown_Object=MibTableColumn
cApsConfigMessageHolddown=_CApsConfigMessageHolddown_Object((1,3,6,1,4,1,9,10,72,1,2,1,7),_CApsConfigMessageHolddown_Type())
cApsConfigMessageHolddown.setMaxAccess(_C)
if mibBuilder.loadTexts:cApsConfigMessageHolddown.setStatus(_A)
if mibBuilder.loadTexts:cApsConfigMessageHolddown.setUnits(_M)
class _CApsConfigMessageHolddownCount_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_CApsConfigMessageHolddownCount_Type.__name__=_D
_CApsConfigMessageHolddownCount_Object=MibTableColumn
cApsConfigMessageHolddownCount=_CApsConfigMessageHolddownCount_Object((1,3,6,1,4,1,9,10,72,1,2,1,8),_CApsConfigMessageHolddownCount_Type())
cApsConfigMessageHolddownCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cApsConfigMessageHolddownCount.setStatus(_A)
class _CApsConfigMessageMaxInterval_Type(Integer32):defaultValue=15000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,120000))
_CApsConfigMessageMaxInterval_Type.__name__=_D
_CApsConfigMessageMaxInterval_Object=MibTableColumn
cApsConfigMessageMaxInterval=_CApsConfigMessageMaxInterval_Object((1,3,6,1,4,1,9,10,72,1,2,1,9),_CApsConfigMessageMaxInterval_Type())
cApsConfigMessageMaxInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cApsConfigMessageMaxInterval.setStatus(_A)
if mibBuilder.loadTexts:cApsConfigMessageMaxInterval.setUnits(_M)
class _CApsConfigFarEndGroupName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CApsConfigFarEndGroupName_Type.__name__=_F
_CApsConfigFarEndGroupName_Object=MibTableColumn
cApsConfigFarEndGroupName=_CApsConfigFarEndGroupName_Object((1,3,6,1,4,1,9,10,72,1,2,1,10),_CApsConfigFarEndGroupName_Type())
cApsConfigFarEndGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:cApsConfigFarEndGroupName.setStatus(_A)
class _CApsConfigFarEndIpAddressType_Type(InetAddressType):defaultValue=1
_CApsConfigFarEndIpAddressType_Type.__name__=_J
_CApsConfigFarEndIpAddressType_Object=MibTableColumn
cApsConfigFarEndIpAddressType=_CApsConfigFarEndIpAddressType_Object((1,3,6,1,4,1,9,10,72,1,2,1,11),_CApsConfigFarEndIpAddressType_Type())
cApsConfigFarEndIpAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cApsConfigFarEndIpAddressType.setStatus(_A)
_CApsConfigFarEndIpAddress_Type=InetAddress
_CApsConfigFarEndIpAddress_Object=MibTableColumn
cApsConfigFarEndIpAddress=_CApsConfigFarEndIpAddress_Object((1,3,6,1,4,1,9,10,72,1,2,1,12),_CApsConfigFarEndIpAddress_Type())
cApsConfigFarEndIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cApsConfigFarEndIpAddress.setStatus(_A)
_CApsStatusExtTable_Object=MibTable
cApsStatusExtTable=_CApsStatusExtTable_Object((1,3,6,1,4,1,9,10,72,1,3))
if mibBuilder.loadTexts:cApsStatusExtTable.setStatus(_A)
_CApsStatusExtEntry_Object=MibTableRow
cApsStatusExtEntry=_CApsStatusExtEntry_Object((1,3,6,1,4,1,9,10,72,1,3,1))
if mibBuilder.loadTexts:cApsStatusExtEntry.setStatus(_A)
_CApsStatusCdlApsBytesRcv_Type=CdlApsBytes
_CApsStatusCdlApsBytesRcv_Object=MibTableColumn
cApsStatusCdlApsBytesRcv=_CApsStatusCdlApsBytesRcv_Object((1,3,6,1,4,1,9,10,72,1,3,1,1),_CApsStatusCdlApsBytesRcv_Type())
cApsStatusCdlApsBytesRcv.setMaxAccess(_E)
if mibBuilder.loadTexts:cApsStatusCdlApsBytesRcv.setStatus(_A)
_CApsStatusCdlApsBytesTrans_Type=CdlApsBytes
_CApsStatusCdlApsBytesTrans_Object=MibTableColumn
cApsStatusCdlApsBytesTrans=_CApsStatusCdlApsBytesTrans_Object((1,3,6,1,4,1,9,10,72,1,3,1,2),_CApsStatusCdlApsBytesTrans_Type())
cApsStatusCdlApsBytesTrans.setMaxAccess(_E)
if mibBuilder.loadTexts:cApsStatusCdlApsBytesTrans.setStatus(_A)
_CApsStatusMessageTransport_Type=CApsMessageTransport
_CApsStatusMessageTransport_Object=MibTableColumn
cApsStatusMessageTransport=_CApsStatusMessageTransport_Object((1,3,6,1,4,1,9,10,72,1,3,1,3),_CApsStatusMessageTransport_Type())
cApsStatusMessageTransport.setMaxAccess(_E)
if mibBuilder.loadTexts:cApsStatusMessageTransport.setStatus(_A)
_CApsChanStatusExtTable_Object=MibTable
cApsChanStatusExtTable=_CApsChanStatusExtTable_Object((1,3,6,1,4,1,9,10,72,1,4))
if mibBuilder.loadTexts:cApsChanStatusExtTable.setStatus(_A)
_CApsChanStatusExtEntry_Object=MibTableRow
cApsChanStatusExtEntry=_CApsChanStatusExtEntry_Object((1,3,6,1,4,1,9,10,72,1,4,1))
if mibBuilder.loadTexts:cApsChanStatusExtEntry.setStatus(_A)
_CApsChanStatusExtRequest_Type=CApsK1K2
_CApsChanStatusExtRequest_Object=MibTableColumn
cApsChanStatusExtRequest=_CApsChanStatusExtRequest_Object((1,3,6,1,4,1,9,10,72,1,4,1,1),_CApsChanStatusExtRequest_Type())
cApsChanStatusExtRequest.setMaxAccess(_E)
if mibBuilder.loadTexts:cApsChanStatusExtRequest.setStatus(_A)
_CApsChanConfigExtTable_Object=MibTable
cApsChanConfigExtTable=_CApsChanConfigExtTable_Object((1,3,6,1,4,1,9,10,72,1,5))
if mibBuilder.loadTexts:cApsChanConfigExtTable.setStatus(_A)
_CApsChanConfigExtEntry_Object=MibTableRow
cApsChanConfigExtEntry=_CApsChanConfigExtEntry_Object((1,3,6,1,4,1,9,10,72,1,5,1))
if mibBuilder.loadTexts:cApsChanConfigExtEntry.setStatus(_A)
_CApsChanConfigReflectorMode_Type=TruthValue
_CApsChanConfigReflectorMode_Object=MibTableColumn
cApsChanConfigReflectorMode=_CApsChanConfigReflectorMode_Object((1,3,6,1,4,1,9,10,72,1,5,1,1),_CApsChanConfigReflectorMode_Type())
cApsChanConfigReflectorMode.setMaxAccess(_E)
if mibBuilder.loadTexts:cApsChanConfigReflectorMode.setStatus(_A)
_CApsChanAssociationTable_Object=MibTable
cApsChanAssociationTable=_CApsChanAssociationTable_Object((1,3,6,1,4,1,9,10,72,1,6))
if mibBuilder.loadTexts:cApsChanAssociationTable.setStatus(_A)
_CApsChanAssociationEntry_Object=MibTableRow
cApsChanAssociationEntry=_CApsChanAssociationEntry_Object((1,3,6,1,4,1,9,10,72,1,6,1))
cApsChanAssociationEntry.setIndexNames((0,_B,_N),(0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:cApsChanAssociationEntry.setStatus(_A)
class _CApsChanAssociationGroupName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CApsChanAssociationGroupName_Type.__name__=_F
_CApsChanAssociationGroupName_Object=MibTableColumn
cApsChanAssociationGroupName=_CApsChanAssociationGroupName_Object((1,3,6,1,4,1,9,10,72,1,6,1,1),_CApsChanAssociationGroupName_Type())
cApsChanAssociationGroupName.setMaxAccess(_G)
if mibBuilder.loadTexts:cApsChanAssociationGroupName.setStatus(_A)
_CApsChanAssociationNumber_Type=CApsChannelConfigNumber
_CApsChanAssociationNumber_Object=MibTableColumn
cApsChanAssociationNumber=_CApsChanAssociationNumber_Object((1,3,6,1,4,1,9,10,72,1,6,1,2),_CApsChanAssociationNumber_Type())
cApsChanAssociationNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:cApsChanAssociationNumber.setStatus(_A)
_CApsChanAssociationMapNumber_Type=CApsChannelConfigNumber
_CApsChanAssociationMapNumber_Object=MibTableColumn
cApsChanAssociationMapNumber=_CApsChanAssociationMapNumber_Object((1,3,6,1,4,1,9,10,72,1,6,1,3),_CApsChanAssociationMapNumber_Type())
cApsChanAssociationMapNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:cApsChanAssociationMapNumber.setStatus(_A)
_CApsChanAssociationIpAddressType_Type=InetAddressType
_CApsChanAssociationIpAddressType_Object=MibTableColumn
cApsChanAssociationIpAddressType=_CApsChanAssociationIpAddressType_Object((1,3,6,1,4,1,9,10,72,1,6,1,4),_CApsChanAssociationIpAddressType_Type())
cApsChanAssociationIpAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:cApsChanAssociationIpAddressType.setStatus(_A)
_CApsChanAssociationIpAddress_Type=InetAddress
_CApsChanAssociationIpAddress_Object=MibTableColumn
cApsChanAssociationIpAddress=_CApsChanAssociationIpAddress_Object((1,3,6,1,4,1,9,10,72,1,6,1,5),_CApsChanAssociationIpAddress_Type())
cApsChanAssociationIpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:cApsChanAssociationIpAddress.setStatus(_A)
_CApsExtMIBConformance_ObjectIdentity=ObjectIdentity
cApsExtMIBConformance=_CApsExtMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,10,72,2))
_CApsExtGroups_ObjectIdentity=ObjectIdentity
cApsExtGroups=_CApsExtGroups_ObjectIdentity((1,3,6,1,4,1,9,10,72,2,1))
_CApsExtCompliances_ObjectIdentity=ObjectIdentity
cApsExtCompliances=_CApsExtCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,72,2,2))
cApsConfigEntry.registerAugmentions((_B,_Q))
cApsConfigExtEntry.setIndexNames(*cApsConfigEntry.getIndexNames())
cApsStatusEntry.registerAugmentions((_B,_R))
cApsStatusExtEntry.setIndexNames(*cApsStatusEntry.getIndexNames())
cApsChanStatusEntry.registerAugmentions((_B,_S))
cApsChanStatusExtEntry.setIndexNames(*cApsChanStatusEntry.getIndexNames())
cApsChanConfigEntry.registerAugmentions((_B,_T))
cApsChanConfigExtEntry.setIndexNames(*cApsChanConfigEntry.getIndexNames())
cApsNotifiesEnableGroup=ObjectGroup((1,3,6,1,4,1,9,10,72,2,1,1))
cApsNotifiesEnableGroup.setObjects((_B,_U))
if mibBuilder.loadTexts:cApsNotifiesEnableGroup.setStatus(_A)
cApsConfigPathExt=ObjectGroup((1,3,6,1,4,1,9,10,72,2,1,2))
cApsConfigPathExt.setObjects((_B,_V))
if mibBuilder.loadTexts:cApsConfigPathExt.setStatus(_A)
cApsConfigYcableExt=ObjectGroup((1,3,6,1,4,1,9,10,72,2,1,3))
cApsConfigYcableExt.setObjects((_B,_W))
if mibBuilder.loadTexts:cApsConfigYcableExt.setStatus(_A)
cApsConfigSearchExt=ObjectGroup((1,3,6,1,4,1,9,10,72,2,1,4))
cApsConfigSearchExt.setObjects(*((_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:cApsConfigSearchExt.setStatus(_A)
cApsStatusCdlExt=ObjectGroup((1,3,6,1,4,1,9,10,72,2,1,5))
cApsStatusCdlExt.setObjects(*((_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:cApsStatusCdlExt.setStatus(_A)
cApsConfigSwitchoverTimerExt=ObjectGroup((1,3,6,1,4,1,9,10,72,2,1,6))
cApsConfigSwitchoverTimerExt.setObjects((_B,_b))
if mibBuilder.loadTexts:cApsConfigSwitchoverTimerExt.setStatus(_A)
cApsConfigMessageExt=ObjectGroup((1,3,6,1,4,1,9,10,72,2,1,7))
cApsConfigMessageExt.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:cApsConfigMessageExt.setStatus(_A)
cApsConfigIPExt=ObjectGroup((1,3,6,1,4,1,9,10,72,2,1,8))
cApsConfigIPExt.setObjects(*((_B,_h),(_B,_i)))
if mibBuilder.loadTexts:cApsConfigIPExt.setStatus(_A)
cApsStatusMessageExt=ObjectGroup((1,3,6,1,4,1,9,10,72,2,1,9))
cApsStatusMessageExt.setObjects((_B,_j))
if mibBuilder.loadTexts:cApsStatusMessageExt.setStatus(_A)
cApsChanStatusRequestExt=ObjectGroup((1,3,6,1,4,1,9,10,72,2,1,10))
cApsChanStatusRequestExt.setObjects((_B,_k))
if mibBuilder.loadTexts:cApsChanStatusRequestExt.setStatus(_A)
cApsChanConfigExt=ObjectGroup((1,3,6,1,4,1,9,10,72,2,1,11))
cApsChanConfigExt.setObjects((_B,_l))
if mibBuilder.loadTexts:cApsChanConfigExt.setStatus(_A)
cApsChanAssociationGroup=ObjectGroup((1,3,6,1,4,1,9,10,72,2,1,12))
cApsChanAssociationGroup.setObjects(*((_B,_m),(_B,_n)))
if mibBuilder.loadTexts:cApsChanAssociationGroup.setStatus(_A)
cApsExtCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,72,2,2,1))
cApsExtCompliance.setObjects(*((_B,_H),(_B,_I)))
if mibBuilder.loadTexts:cApsExtCompliance.setStatus('deprecated')
cApsExtCompliance2=ModuleCompliance((1,3,6,1,4,1,9,10,72,2,2,2))
cApsExtCompliance2.setObjects(*((_B,_H),(_B,_I)))
if mibBuilder.loadTexts:cApsExtCompliance2.setStatus(_A)
cApsExtComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,10,72,2,2,3))
cApsExtComplianceRev1.setObjects(*((_B,_o),(_B,_p)))
if mibBuilder.loadTexts:cApsExtComplianceRev1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CdlApsBytes':CdlApsBytes,_L:CApsMessageTransport,'CApsChannelConfigNumber':CApsChannelConfigNumber,'cApsExtMIB':cApsExtMIB,'cApsExtMIBObjects':cApsExtMIBObjects,_U:cApsNotifiesEnable,'cApsConfigExtTable':cApsConfigExtTable,_Q:cApsConfigExtEntry,_V:cApsConfigSpan,_W:cApsConfigYcable,_X:cApsConfigMinSearchUpInterval,_Y:cApsConfigMaxSearchUpInterval,_b:cApsConfigSwitchoverEnableInterval,_c:cApsConfigMessageTransport,_d:cApsConfigMessageHolddown,_e:cApsConfigMessageHolddownCount,_f:cApsConfigMessageMaxInterval,_g:cApsConfigFarEndGroupName,_h:cApsConfigFarEndIpAddressType,_i:cApsConfigFarEndIpAddress,'cApsStatusExtTable':cApsStatusExtTable,_R:cApsStatusExtEntry,_Z:cApsStatusCdlApsBytesRcv,_a:cApsStatusCdlApsBytesTrans,_j:cApsStatusMessageTransport,'cApsChanStatusExtTable':cApsChanStatusExtTable,_S:cApsChanStatusExtEntry,_k:cApsChanStatusExtRequest,'cApsChanConfigExtTable':cApsChanConfigExtTable,_T:cApsChanConfigExtEntry,_l:cApsChanConfigReflectorMode,'cApsChanAssociationTable':cApsChanAssociationTable,'cApsChanAssociationEntry':cApsChanAssociationEntry,_N:cApsChanAssociationGroupName,_O:cApsChanAssociationNumber,_P:cApsChanAssociationMapNumber,_m:cApsChanAssociationIpAddressType,_n:cApsChanAssociationIpAddress,'cApsExtMIBConformance':cApsExtMIBConformance,'cApsExtGroups':cApsExtGroups,_H:cApsNotifiesEnableGroup,_I:cApsConfigPathExt,'cApsConfigYcableExt':cApsConfigYcableExt,'cApsConfigSearchExt':cApsConfigSearchExt,'cApsStatusCdlExt':cApsStatusCdlExt,'cApsConfigSwitchoverTimerExt':cApsConfigSwitchoverTimerExt,'cApsConfigMessageExt':cApsConfigMessageExt,'cApsConfigIPExt':cApsConfigIPExt,'cApsStatusMessageExt':cApsStatusMessageExt,'cApsChanStatusRequestExt':cApsChanStatusRequestExt,_o:cApsChanConfigExt,_p:cApsChanAssociationGroup,'cApsExtCompliances':cApsExtCompliances,'cApsExtCompliance':cApsExtCompliance,'cApsExtCompliance2':cApsExtCompliance2,'cApsExtComplianceRev1':cApsExtComplianceRev1})