_H='ifIndex'
_G='IF-MIB'
_F='OctetString'
_E='enable'
_D='disable'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkLldpMIBObjects,=mibBuilder.importSymbols('TPLINK-LLDP-MIB','tplinkLldpMIBObjects')
TPRowStatus,=mibBuilder.importSymbols('TPLINK-TC-MIB','TPRowStatus')
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_LldpConfig_ObjectIdentity=ObjectIdentity
lldpConfig=_LldpConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,35,1,1))
_LldpGlobalConfig_ObjectIdentity=ObjectIdentity
lldpGlobalConfig=_LldpGlobalConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,35,1,1,1))
class _LldpGlobalConfigEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_LldpGlobalConfigEnable_Type.__name__=_B
_LldpGlobalConfigEnable_Object=MibScalar
lldpGlobalConfigEnable=_LldpGlobalConfigEnable_Object((1,3,6,1,4,1,11863,6,35,1,1,1,1),_LldpGlobalConfigEnable_Type())
lldpGlobalConfigEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpGlobalConfigEnable.setStatus(_A)
class _LldpGlobalConfigForwardMessageEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_LldpGlobalConfigForwardMessageEnable_Type.__name__=_B
_LldpGlobalConfigForwardMessageEnable_Object=MibScalar
lldpGlobalConfigForwardMessageEnable=_LldpGlobalConfigForwardMessageEnable_Object((1,3,6,1,4,1,11863,6,35,1,1,1,2),_LldpGlobalConfigForwardMessageEnable_Type())
lldpGlobalConfigForwardMessageEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpGlobalConfigForwardMessageEnable.setStatus(_A)
class _LldpGlobalConfigTxInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,32768))
_LldpGlobalConfigTxInterval_Type.__name__=_B
_LldpGlobalConfigTxInterval_Object=MibScalar
lldpGlobalConfigTxInterval=_LldpGlobalConfigTxInterval_Object((1,3,6,1,4,1,11863,6,35,1,1,1,3),_LldpGlobalConfigTxInterval_Type())
lldpGlobalConfigTxInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpGlobalConfigTxInterval.setStatus(_A)
class _LldpGlobalConfigTtl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_LldpGlobalConfigTtl_Type.__name__=_B
_LldpGlobalConfigTtl_Object=MibScalar
lldpGlobalConfigTtl=_LldpGlobalConfigTtl_Object((1,3,6,1,4,1,11863,6,35,1,1,1,4),_LldpGlobalConfigTtl_Type())
lldpGlobalConfigTtl.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpGlobalConfigTtl.setStatus(_A)
class _LldpGlobalConfigTxDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8192))
_LldpGlobalConfigTxDelay_Type.__name__=_B
_LldpGlobalConfigTxDelay_Object=MibScalar
lldpGlobalConfigTxDelay=_LldpGlobalConfigTxDelay_Object((1,3,6,1,4,1,11863,6,35,1,1,1,5),_LldpGlobalConfigTxDelay_Type())
lldpGlobalConfigTxDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpGlobalConfigTxDelay.setStatus(_A)
class _LldpGlobalConfigInitDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_LldpGlobalConfigInitDelay_Type.__name__=_B
_LldpGlobalConfigInitDelay_Object=MibScalar
lldpGlobalConfigInitDelay=_LldpGlobalConfigInitDelay_Object((1,3,6,1,4,1,11863,6,35,1,1,1,6),_LldpGlobalConfigInitDelay_Type())
lldpGlobalConfigInitDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpGlobalConfigInitDelay.setStatus(_A)
class _LldpGlobalConfigTrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,3600))
_LldpGlobalConfigTrap_Type.__name__=_B
_LldpGlobalConfigTrap_Object=MibScalar
lldpGlobalConfigTrap=_LldpGlobalConfigTrap_Object((1,3,6,1,4,1,11863,6,35,1,1,1,7),_LldpGlobalConfigTrap_Type())
lldpGlobalConfigTrap.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpGlobalConfigTrap.setStatus(_A)
class _LldpGlobalConfigFastCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_LldpGlobalConfigFastCount_Type.__name__=_B
_LldpGlobalConfigFastCount_Object=MibScalar
lldpGlobalConfigFastCount=_LldpGlobalConfigFastCount_Object((1,3,6,1,4,1,11863,6,35,1,1,1,8),_LldpGlobalConfigFastCount_Type())
lldpGlobalConfigFastCount.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpGlobalConfigFastCount.setStatus(_A)
_LldpPortConfigTable_Object=MibTable
lldpPortConfigTable=_LldpPortConfigTable_Object((1,3,6,1,4,1,11863,6,35,1,1,2))
if mibBuilder.loadTexts:lldpPortConfigTable.setStatus(_A)
_LldpPortConfigEntry_Object=MibTableRow
lldpPortConfigEntry=_LldpPortConfigEntry_Object((1,3,6,1,4,1,11863,6,35,1,1,2,1))
lldpPortConfigEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:lldpPortConfigEntry.setStatus(_A)
class _LldpConfigPortId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpConfigPortId_Type.__name__=_F
_LldpConfigPortId_Object=MibTableColumn
lldpConfigPortId=_LldpConfigPortId_Object((1,3,6,1,4,1,11863,6,35,1,1,2,1,1),_LldpConfigPortId_Type())
lldpConfigPortId.setMaxAccess('read-only')
if mibBuilder.loadTexts:lldpConfigPortId.setStatus(_A)
class _LldpConfigPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_D,0),('enableTx',1),('enableRx',2),('enableRxTx',3)))
_LldpConfigPortStatus_Type.__name__=_B
_LldpConfigPortStatus_Object=MibTableColumn
lldpConfigPortStatus=_LldpConfigPortStatus_Object((1,3,6,1,4,1,11863,6,35,1,1,2,1,2),_LldpConfigPortStatus_Type())
lldpConfigPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpConfigPortStatus.setStatus(_A)
class _LldpConfigPortSnmpNotifyEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_LldpConfigPortSnmpNotifyEnable_Type.__name__=_B
_LldpConfigPortSnmpNotifyEnable_Object=MibTableColumn
lldpConfigPortSnmpNotifyEnable=_LldpConfigPortSnmpNotifyEnable_Object((1,3,6,1,4,1,11863,6,35,1,1,2,1,3),_LldpConfigPortSnmpNotifyEnable_Type())
lldpConfigPortSnmpNotifyEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpConfigPortSnmpNotifyEnable.setStatus(_A)
class _LldpConfigPortTlvDescr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_LldpConfigPortTlvDescr_Type.__name__=_B
_LldpConfigPortTlvDescr_Object=MibTableColumn
lldpConfigPortTlvDescr=_LldpConfigPortTlvDescr_Object((1,3,6,1,4,1,11863,6,35,1,1,2,1,4),_LldpConfigPortTlvDescr_Type())
lldpConfigPortTlvDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpConfigPortTlvDescr.setStatus(_A)
class _LldpConfigPortTlvSysCap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_LldpConfigPortTlvSysCap_Type.__name__=_B
_LldpConfigPortTlvSysCap_Object=MibTableColumn
lldpConfigPortTlvSysCap=_LldpConfigPortTlvSysCap_Object((1,3,6,1,4,1,11863,6,35,1,1,2,1,5),_LldpConfigPortTlvSysCap_Type())
lldpConfigPortTlvSysCap.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpConfigPortTlvSysCap.setStatus(_A)
class _LldpConfigPortTlvSysDescr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_LldpConfigPortTlvSysDescr_Type.__name__=_B
_LldpConfigPortTlvSysDescr_Object=MibTableColumn
lldpConfigPortTlvSysDescr=_LldpConfigPortTlvSysDescr_Object((1,3,6,1,4,1,11863,6,35,1,1,2,1,6),_LldpConfigPortTlvSysDescr_Type())
lldpConfigPortTlvSysDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpConfigPortTlvSysDescr.setStatus(_A)
class _LldpConfigPortTlvSysName_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_LldpConfigPortTlvSysName_Type.__name__=_B
_LldpConfigPortTlvSysName_Object=MibTableColumn
lldpConfigPortTlvSysName=_LldpConfigPortTlvSysName_Object((1,3,6,1,4,1,11863,6,35,1,1,2,1,7),_LldpConfigPortTlvSysName_Type())
lldpConfigPortTlvSysName.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpConfigPortTlvSysName.setStatus(_A)
class _LldpConfigPortTlvManageAddr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_LldpConfigPortTlvManageAddr_Type.__name__=_B
_LldpConfigPortTlvManageAddr_Object=MibTableColumn
lldpConfigPortTlvManageAddr=_LldpConfigPortTlvManageAddr_Object((1,3,6,1,4,1,11863,6,35,1,1,2,1,8),_LldpConfigPortTlvManageAddr_Type())
lldpConfigPortTlvManageAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpConfigPortTlvManageAddr.setStatus(_A)
class _LldpConfigPortTlvPortVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_LldpConfigPortTlvPortVlanId_Type.__name__=_B
_LldpConfigPortTlvPortVlanId_Object=MibTableColumn
lldpConfigPortTlvPortVlanId=_LldpConfigPortTlvPortVlanId_Object((1,3,6,1,4,1,11863,6,35,1,1,2,1,9),_LldpConfigPortTlvPortVlanId_Type())
lldpConfigPortTlvPortVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpConfigPortTlvPortVlanId.setStatus(_A)
class _LldpConfigPortTlvProtoVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_LldpConfigPortTlvProtoVlanId_Type.__name__=_B
_LldpConfigPortTlvProtoVlanId_Object=MibTableColumn
lldpConfigPortTlvProtoVlanId=_LldpConfigPortTlvProtoVlanId_Object((1,3,6,1,4,1,11863,6,35,1,1,2,1,10),_LldpConfigPortTlvProtoVlanId_Type())
lldpConfigPortTlvProtoVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpConfigPortTlvProtoVlanId.setStatus(_A)
class _LldpConfigPortTlvVlanName_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_LldpConfigPortTlvVlanName_Type.__name__=_B
_LldpConfigPortTlvVlanName_Object=MibTableColumn
lldpConfigPortTlvVlanName=_LldpConfigPortTlvVlanName_Object((1,3,6,1,4,1,11863,6,35,1,1,2,1,11),_LldpConfigPortTlvVlanName_Type())
lldpConfigPortTlvVlanName.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpConfigPortTlvVlanName.setStatus(_A)
class _LldpConfigPortTlvLinkAggre_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_LldpConfigPortTlvLinkAggre_Type.__name__=_B
_LldpConfigPortTlvLinkAggre_Object=MibTableColumn
lldpConfigPortTlvLinkAggre=_LldpConfigPortTlvLinkAggre_Object((1,3,6,1,4,1,11863,6,35,1,1,2,1,12),_LldpConfigPortTlvLinkAggre_Type())
lldpConfigPortTlvLinkAggre.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpConfigPortTlvLinkAggre.setStatus(_A)
class _LldpConfigPortTlvPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_LldpConfigPortTlvPortStatus_Type.__name__=_B
_LldpConfigPortTlvPortStatus_Object=MibTableColumn
lldpConfigPortTlvPortStatus=_LldpConfigPortTlvPortStatus_Object((1,3,6,1,4,1,11863,6,35,1,1,2,1,13),_LldpConfigPortTlvPortStatus_Type())
lldpConfigPortTlvPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpConfigPortTlvPortStatus.setStatus(_A)
class _LldpConfigPortTlvMaxFrame_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_LldpConfigPortTlvMaxFrame_Type.__name__=_B
_LldpConfigPortTlvMaxFrame_Object=MibTableColumn
lldpConfigPortTlvMaxFrame=_LldpConfigPortTlvMaxFrame_Object((1,3,6,1,4,1,11863,6,35,1,1,2,1,14),_LldpConfigPortTlvMaxFrame_Type())
lldpConfigPortTlvMaxFrame.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpConfigPortTlvMaxFrame.setStatus(_A)
class _LldpConfigPortTlvPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_LldpConfigPortTlvPower_Type.__name__=_B
_LldpConfigPortTlvPower_Object=MibTableColumn
lldpConfigPortTlvPower=_LldpConfigPortTlvPower_Object((1,3,6,1,4,1,11863,6,35,1,1,2,1,15),_LldpConfigPortTlvPower_Type())
lldpConfigPortTlvPower.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpConfigPortTlvPower.setStatus(_A)
class _LldpConfigPortManagementAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_LldpConfigPortManagementAddress_Type.__name__=_F
_LldpConfigPortManagementAddress_Object=MibTableColumn
lldpConfigPortManagementAddress=_LldpConfigPortManagementAddress_Object((1,3,6,1,4,1,11863,6,35,1,1,2,1,16),_LldpConfigPortManagementAddress_Type())
lldpConfigPortManagementAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpConfigPortManagementAddress.setStatus(_A)
mibBuilder.exportSymbols('TPLINK-LLDPCONFIG-MIB',**{'MacAddress':MacAddress,'lldpConfig':lldpConfig,'lldpGlobalConfig':lldpGlobalConfig,'lldpGlobalConfigEnable':lldpGlobalConfigEnable,'lldpGlobalConfigForwardMessageEnable':lldpGlobalConfigForwardMessageEnable,'lldpGlobalConfigTxInterval':lldpGlobalConfigTxInterval,'lldpGlobalConfigTtl':lldpGlobalConfigTtl,'lldpGlobalConfigTxDelay':lldpGlobalConfigTxDelay,'lldpGlobalConfigInitDelay':lldpGlobalConfigInitDelay,'lldpGlobalConfigTrap':lldpGlobalConfigTrap,'lldpGlobalConfigFastCount':lldpGlobalConfigFastCount,'lldpPortConfigTable':lldpPortConfigTable,'lldpPortConfigEntry':lldpPortConfigEntry,'lldpConfigPortId':lldpConfigPortId,'lldpConfigPortStatus':lldpConfigPortStatus,'lldpConfigPortSnmpNotifyEnable':lldpConfigPortSnmpNotifyEnable,'lldpConfigPortTlvDescr':lldpConfigPortTlvDescr,'lldpConfigPortTlvSysCap':lldpConfigPortTlvSysCap,'lldpConfigPortTlvSysDescr':lldpConfigPortTlvSysDescr,'lldpConfigPortTlvSysName':lldpConfigPortTlvSysName,'lldpConfigPortTlvManageAddr':lldpConfigPortTlvManageAddr,'lldpConfigPortTlvPortVlanId':lldpConfigPortTlvPortVlanId,'lldpConfigPortTlvProtoVlanId':lldpConfigPortTlvProtoVlanId,'lldpConfigPortTlvVlanName':lldpConfigPortTlvVlanName,'lldpConfigPortTlvLinkAggre':lldpConfigPortTlvLinkAggre,'lldpConfigPortTlvPortStatus':lldpConfigPortTlvPortStatus,'lldpConfigPortTlvMaxFrame':lldpConfigPortTlvMaxFrame,'lldpConfigPortTlvPower':lldpConfigPortTlvPower,'lldpConfigPortManagementAddress':lldpConfigPortManagementAddress})