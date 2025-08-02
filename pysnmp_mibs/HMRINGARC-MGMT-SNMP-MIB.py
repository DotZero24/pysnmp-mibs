_M='hmArcCheckStatusDeviceMac'
_L='hmArcCheckStatusIndex'
_K='configFailed'
_J='openRing'
_I='noAction'
_H='disabled'
_G='enabled'
_F='HMRINGARC-MGMT-SNMP-MIB'
_E='OctetString'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hmRingRedundancy,=mibBuilder.importSymbols('HMRING-MGMT-SNMP-MIB','hmRingRedundancy')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hmARC=ModuleIdentity((1,3,6,1,4,1,248,14,5,7))
if mibBuilder.loadTexts:hmARC.setRevisions(('2010-09-01 12:00',))
_HmArcManagerConfig_ObjectIdentity=ObjectIdentity
hmArcManagerConfig=_HmArcManagerConfig_ObjectIdentity((1,3,6,1,4,1,248,14,5,7,1))
class _HmArcManagerAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_HmArcManagerAdminStatus_Type.__name__=_C
_HmArcManagerAdminStatus_Object=MibScalar
hmArcManagerAdminStatus=_HmArcManagerAdminStatus_Object((1,3,6,1,4,1,248,14,5,7,1,1),_HmArcManagerAdminStatus_Type())
hmArcManagerAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hmArcManagerAdminStatus.setStatus(_A)
class _HmArcManagerRedProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('mrp',1))
_HmArcManagerRedProtocol_Type.__name__=_C
_HmArcManagerRedProtocol_Object=MibScalar
hmArcManagerRedProtocol=_HmArcManagerRedProtocol_Object((1,3,6,1,4,1,248,14,5,7,1,2),_HmArcManagerRedProtocol_Type())
hmArcManagerRedProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:hmArcManagerRedProtocol.setStatus(_A)
_HmArcManagerPrimGroupID_Type=Integer32
_HmArcManagerPrimGroupID_Object=MibScalar
hmArcManagerPrimGroupID=_HmArcManagerPrimGroupID_Object((1,3,6,1,4,1,248,14,5,7,1,3),_HmArcManagerPrimGroupID_Type())
hmArcManagerPrimGroupID.setMaxAccess(_B)
if mibBuilder.loadTexts:hmArcManagerPrimGroupID.setStatus(_A)
_HmArcManagerPrimIfIndex_Type=Integer32
_HmArcManagerPrimIfIndex_Object=MibScalar
hmArcManagerPrimIfIndex=_HmArcManagerPrimIfIndex_Object((1,3,6,1,4,1,248,14,5,7,1,4),_HmArcManagerPrimIfIndex_Type())
hmArcManagerPrimIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hmArcManagerPrimIfIndex.setStatus(_A)
_HmArcManagerRedGroupID_Type=Integer32
_HmArcManagerRedGroupID_Object=MibScalar
hmArcManagerRedGroupID=_HmArcManagerRedGroupID_Object((1,3,6,1,4,1,248,14,5,7,1,5),_HmArcManagerRedGroupID_Type())
hmArcManagerRedGroupID.setMaxAccess(_B)
if mibBuilder.loadTexts:hmArcManagerRedGroupID.setStatus(_A)
_HmArcManagerRedIfIndex_Type=Integer32
_HmArcManagerRedIfIndex_Object=MibScalar
hmArcManagerRedIfIndex=_HmArcManagerRedIfIndex_Object((1,3,6,1,4,1,248,14,5,7,1,6),_HmArcManagerRedIfIndex_Type())
hmArcManagerRedIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hmArcManagerRedIfIndex.setStatus(_A)
_HmArcManagerVlanID_Type=Integer32
_HmArcManagerVlanID_Object=MibScalar
hmArcManagerVlanID=_HmArcManagerVlanID_Object((1,3,6,1,4,1,248,14,5,7,1,7),_HmArcManagerVlanID_Type())
hmArcManagerVlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:hmArcManagerVlanID.setStatus(_A)
class _HmArcManagerAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),('checkTopology',2),('configureRing',3)))
_HmArcManagerAction_Type.__name__=_C
_HmArcManagerAction_Object=MibScalar
hmArcManagerAction=_HmArcManagerAction_Object((1,3,6,1,4,1,248,14,5,7,1,8),_HmArcManagerAction_Type())
hmArcManagerAction.setMaxAccess(_D)
if mibBuilder.loadTexts:hmArcManagerAction.setStatus(_A)
class _HmArcManagerActionResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_I,1),('pending',2),('closedRing',3),('configuredRing',4),(_J,5),('invalidTopology',6),(_K,7),('configSuccessful',8)))
_HmArcManagerActionResult_Type.__name__=_C
_HmArcManagerActionResult_Object=MibScalar
hmArcManagerActionResult=_HmArcManagerActionResult_Object((1,3,6,1,4,1,248,14,5,7,1,9),_HmArcManagerActionResult_Type())
hmArcManagerActionResult.setMaxAccess(_B)
if mibBuilder.loadTexts:hmArcManagerActionResult.setStatus(_A)
_HmArcManagerStatus_ObjectIdentity=ObjectIdentity
hmArcManagerStatus=_HmArcManagerStatus_ObjectIdentity((1,3,6,1,4,1,248,14,5,7,2))
_HmArcCheckResultTable_Object=MibTable
hmArcCheckResultTable=_HmArcCheckResultTable_Object((1,3,6,1,4,1,248,14,5,7,2,1))
if mibBuilder.loadTexts:hmArcCheckResultTable.setStatus(_A)
_HmArcCheckResultEntry_Object=MibTableRow
hmArcCheckResultEntry=_HmArcCheckResultEntry_Object((1,3,6,1,4,1,248,14,5,7,2,1,1))
hmArcCheckResultEntry.setIndexNames((0,_F,_L),(0,_F,_M))
if mibBuilder.loadTexts:hmArcCheckResultEntry.setStatus(_A)
_HmArcCheckStatusIndex_Type=Integer32
_HmArcCheckStatusIndex_Object=MibTableColumn
hmArcCheckStatusIndex=_HmArcCheckStatusIndex_Object((1,3,6,1,4,1,248,14,5,7,2,1,1,1),_HmArcCheckStatusIndex_Type())
hmArcCheckStatusIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hmArcCheckStatusIndex.setStatus(_A)
class _HmArcCheckStatusDeviceMac_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_HmArcCheckStatusDeviceMac_Type.__name__=_E
_HmArcCheckStatusDeviceMac_Object=MibTableColumn
hmArcCheckStatusDeviceMac=_HmArcCheckStatusDeviceMac_Object((1,3,6,1,4,1,248,14,5,7,2,1,1,2),_HmArcCheckStatusDeviceMac_Type())
hmArcCheckStatusDeviceMac.setMaxAccess(_B)
if mibBuilder.loadTexts:hmArcCheckStatusDeviceMac.setStatus(_A)
_HmArcCheckStatusDeviceIp_Type=IpAddress
_HmArcCheckStatusDeviceIp_Object=MibTableColumn
hmArcCheckStatusDeviceIp=_HmArcCheckStatusDeviceIp_Object((1,3,6,1,4,1,248,14,5,7,2,1,1,3),_HmArcCheckStatusDeviceIp_Type())
hmArcCheckStatusDeviceIp.setMaxAccess(_B)
if mibBuilder.loadTexts:hmArcCheckStatusDeviceIp.setStatus(_A)
class _HmArcCheckStatusType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('otherRm',1),('loop',2),('alreadyConfigured',3),('unsupportedOption',4),(_J,5),(_K,6),('duplexMode',7),('noArcDevices',8),('portState',9),('info',10)))
_HmArcCheckStatusType_Type.__name__=_C
_HmArcCheckStatusType_Object=MibTableColumn
hmArcCheckStatusType=_HmArcCheckStatusType_Object((1,3,6,1,4,1,248,14,5,7,2,1,1,4),_HmArcCheckStatusType_Type())
hmArcCheckStatusType.setMaxAccess(_B)
if mibBuilder.loadTexts:hmArcCheckStatusType.setStatus(_A)
_HmArcCheckStatusInfo_Type=DisplayString
_HmArcCheckStatusInfo_Object=MibTableColumn
hmArcCheckStatusInfo=_HmArcCheckStatusInfo_Object((1,3,6,1,4,1,248,14,5,7,2,1,1,5),_HmArcCheckStatusInfo_Type())
hmArcCheckStatusInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:hmArcCheckStatusInfo.setStatus(_A)
class _HmArcCheckStatusClassification_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('error',1),('warning',2),('ok',3)))
_HmArcCheckStatusClassification_Type.__name__=_C
_HmArcCheckStatusClassification_Object=MibTableColumn
hmArcCheckStatusClassification=_HmArcCheckStatusClassification_Object((1,3,6,1,4,1,248,14,5,7,2,1,1,6),_HmArcCheckStatusClassification_Type())
hmArcCheckStatusClassification.setMaxAccess(_B)
if mibBuilder.loadTexts:hmArcCheckStatusClassification.setStatus(_A)
_HmArcClientConfig_ObjectIdentity=ObjectIdentity
hmArcClientConfig=_HmArcClientConfig_ObjectIdentity((1,3,6,1,4,1,248,14,5,7,3))
class _HmArcClientAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),('checkOnly',3)))
_HmArcClientAdminStatus_Type.__name__=_C
_HmArcClientAdminStatus_Object=MibScalar
hmArcClientAdminStatus=_HmArcClientAdminStatus_Object((1,3,6,1,4,1,248,14,5,7,3,1),_HmArcClientAdminStatus_Type())
hmArcClientAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hmArcClientAdminStatus.setStatus(_A)
_HmArcClientStatus_ObjectIdentity=ObjectIdentity
hmArcClientStatus=_HmArcClientStatus_ObjectIdentity((1,3,6,1,4,1,248,14,5,7,4))
class _HmArcClientManagerDeviceMac_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_HmArcClientManagerDeviceMac_Type.__name__=_E
_HmArcClientManagerDeviceMac_Object=MibScalar
hmArcClientManagerDeviceMac=_HmArcClientManagerDeviceMac_Object((1,3,6,1,4,1,248,14,5,7,4,1),_HmArcClientManagerDeviceMac_Type())
hmArcClientManagerDeviceMac.setMaxAccess(_B)
if mibBuilder.loadTexts:hmArcClientManagerDeviceMac.setStatus(_A)
_HmArcClientManagerDeviceIp_Type=IpAddress
_HmArcClientManagerDeviceIp_Object=MibScalar
hmArcClientManagerDeviceIp=_HmArcClientManagerDeviceIp_Object((1,3,6,1,4,1,248,14,5,7,4,2),_HmArcClientManagerDeviceIp_Type())
hmArcClientManagerDeviceIp.setMaxAccess(_B)
if mibBuilder.loadTexts:hmArcClientManagerDeviceIp.setStatus(_A)
_HmArcClientPrimGroupID_Type=Integer32
_HmArcClientPrimGroupID_Object=MibScalar
hmArcClientPrimGroupID=_HmArcClientPrimGroupID_Object((1,3,6,1,4,1,248,14,5,7,4,3),_HmArcClientPrimGroupID_Type())
hmArcClientPrimGroupID.setMaxAccess(_B)
if mibBuilder.loadTexts:hmArcClientPrimGroupID.setStatus(_A)
_HmArcClientPrimIfIndex_Type=Integer32
_HmArcClientPrimIfIndex_Object=MibScalar
hmArcClientPrimIfIndex=_HmArcClientPrimIfIndex_Object((1,3,6,1,4,1,248,14,5,7,4,4),_HmArcClientPrimIfIndex_Type())
hmArcClientPrimIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hmArcClientPrimIfIndex.setStatus(_A)
_HmArcClientRedGroupID_Type=Integer32
_HmArcClientRedGroupID_Object=MibScalar
hmArcClientRedGroupID=_HmArcClientRedGroupID_Object((1,3,6,1,4,1,248,14,5,7,4,5),_HmArcClientRedGroupID_Type())
hmArcClientRedGroupID.setMaxAccess(_B)
if mibBuilder.loadTexts:hmArcClientRedGroupID.setStatus(_A)
_HmArcClientRedIfIndex_Type=Integer32
_HmArcClientRedIfIndex_Object=MibScalar
hmArcClientRedIfIndex=_HmArcClientRedIfIndex_Object((1,3,6,1,4,1,248,14,5,7,4,6),_HmArcClientRedIfIndex_Type())
hmArcClientRedIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hmArcClientRedIfIndex.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'hmARC':hmARC,'hmArcManagerConfig':hmArcManagerConfig,'hmArcManagerAdminStatus':hmArcManagerAdminStatus,'hmArcManagerRedProtocol':hmArcManagerRedProtocol,'hmArcManagerPrimGroupID':hmArcManagerPrimGroupID,'hmArcManagerPrimIfIndex':hmArcManagerPrimIfIndex,'hmArcManagerRedGroupID':hmArcManagerRedGroupID,'hmArcManagerRedIfIndex':hmArcManagerRedIfIndex,'hmArcManagerVlanID':hmArcManagerVlanID,'hmArcManagerAction':hmArcManagerAction,'hmArcManagerActionResult':hmArcManagerActionResult,'hmArcManagerStatus':hmArcManagerStatus,'hmArcCheckResultTable':hmArcCheckResultTable,'hmArcCheckResultEntry':hmArcCheckResultEntry,_L:hmArcCheckStatusIndex,_M:hmArcCheckStatusDeviceMac,'hmArcCheckStatusDeviceIp':hmArcCheckStatusDeviceIp,'hmArcCheckStatusType':hmArcCheckStatusType,'hmArcCheckStatusInfo':hmArcCheckStatusInfo,'hmArcCheckStatusClassification':hmArcCheckStatusClassification,'hmArcClientConfig':hmArcClientConfig,'hmArcClientAdminStatus':hmArcClientAdminStatus,'hmArcClientStatus':hmArcClientStatus,'hmArcClientManagerDeviceMac':hmArcClientManagerDeviceMac,'hmArcClientManagerDeviceIp':hmArcClientManagerDeviceIp,'hmArcClientPrimGroupID':hmArcClientPrimGroupID,'hmArcClientPrimIfIndex':hmArcClientPrimIfIndex,'hmArcClientRedGroupID':hmArcClientRedGroupID,'hmArcClientRedIfIndex':hmArcClientRedIfIndex})