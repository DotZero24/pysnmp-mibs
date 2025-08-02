_L='snDhcpServerPoolExcludedAddressRangeIndex'
_K='snDhcpServerPoolExcludedAddressIndex'
_J='snDhcpServerPoolOptionCode'
_I='2018-08-07 00:00'
_H='not-accessible'
_G='snDhcpServerPoolName'
_F='FOUNDRY-DHCPSERVER-MIB'
_E='read-write'
_D='Integer32'
_C='OctetString'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
snSwitch,=mibBuilder.importSymbols('FOUNDRY-SN-SWITCH-GROUP-MIB','snSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
snDhcpServer=ModuleIdentity((1,3,6,1,4,1,1991,1,1,3,42))
if mibBuilder.loadTexts:snDhcpServer.setRevisions((_I,_I))
_SnDhcpServerGlobalObjects_ObjectIdentity=ObjectIdentity
snDhcpServerGlobalObjects=_SnDhcpServerGlobalObjects_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,42,1))
class _SnDhcpServerGlobalConfigState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disabled',0),('enabled',1)))
_SnDhcpServerGlobalConfigState_Type.__name__=_D
_SnDhcpServerGlobalConfigState_Object=MibScalar
snDhcpServerGlobalConfigState=_SnDhcpServerGlobalConfigState_Object((1,3,6,1,4,1,1991,1,1,3,42,1,1),_SnDhcpServerGlobalConfigState_Type())
snDhcpServerGlobalConfigState.setMaxAccess(_E)
if mibBuilder.loadTexts:snDhcpServerGlobalConfigState.setStatus(_A)
_SnDhcpServerTableObjects_ObjectIdentity=ObjectIdentity
snDhcpServerTableObjects=_SnDhcpServerTableObjects_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,42,2))
_SnDhcpServerPoolConfigTable_Object=MibTable
snDhcpServerPoolConfigTable=_SnDhcpServerPoolConfigTable_Object((1,3,6,1,4,1,1991,1,1,3,42,2,1))
if mibBuilder.loadTexts:snDhcpServerPoolConfigTable.setStatus(_A)
_SnDhcpServerPoolConfigEntry_Object=MibTableRow
snDhcpServerPoolConfigEntry=_SnDhcpServerPoolConfigEntry_Object((1,3,6,1,4,1,1991,1,1,3,42,2,1,1))
snDhcpServerPoolConfigEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:snDhcpServerPoolConfigEntry.setStatus(_A)
class _SnDhcpServerPoolName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SnDhcpServerPoolName_Type.__name__=_C
_SnDhcpServerPoolName_Object=MibTableColumn
snDhcpServerPoolName=_SnDhcpServerPoolName_Object((1,3,6,1,4,1,1991,1,1,3,42,2,1,1,1),_SnDhcpServerPoolName_Type())
snDhcpServerPoolName.setMaxAccess(_H)
if mibBuilder.loadTexts:snDhcpServerPoolName.setStatus(_A)
_SnDhcpServerPoolNetwork_Type=IpAddress
_SnDhcpServerPoolNetwork_Object=MibTableColumn
snDhcpServerPoolNetwork=_SnDhcpServerPoolNetwork_Object((1,3,6,1,4,1,1991,1,1,3,42,2,1,1,2),_SnDhcpServerPoolNetwork_Type())
snDhcpServerPoolNetwork.setMaxAccess(_E)
if mibBuilder.loadTexts:snDhcpServerPoolNetwork.setStatus(_A)
_SnDhcpServerPoolNetworkMask_Type=IpAddress
_SnDhcpServerPoolNetworkMask_Object=MibTableColumn
snDhcpServerPoolNetworkMask=_SnDhcpServerPoolNetworkMask_Object((1,3,6,1,4,1,1991,1,1,3,42,2,1,1,3),_SnDhcpServerPoolNetworkMask_Type())
snDhcpServerPoolNetworkMask.setMaxAccess(_E)
if mibBuilder.loadTexts:snDhcpServerPoolNetworkMask.setStatus(_A)
_SnDhcpServerPoolStartAddr_Type=IpAddress
_SnDhcpServerPoolStartAddr_Object=MibTableColumn
snDhcpServerPoolStartAddr=_SnDhcpServerPoolStartAddr_Object((1,3,6,1,4,1,1991,1,1,3,42,2,1,1,4),_SnDhcpServerPoolStartAddr_Type())
snDhcpServerPoolStartAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:snDhcpServerPoolStartAddr.setStatus(_A)
_SnDhcpServerPoolEndAddr_Type=IpAddress
_SnDhcpServerPoolEndAddr_Object=MibTableColumn
snDhcpServerPoolEndAddr=_SnDhcpServerPoolEndAddr_Object((1,3,6,1,4,1,1991,1,1,3,42,2,1,1,5),_SnDhcpServerPoolEndAddr_Type())
snDhcpServerPoolEndAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:snDhcpServerPoolEndAddr.setStatus(_A)
class _SnDhcpServerPoolLeaseDay_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,365))
_SnDhcpServerPoolLeaseDay_Type.__name__=_D
_SnDhcpServerPoolLeaseDay_Object=MibTableColumn
snDhcpServerPoolLeaseDay=_SnDhcpServerPoolLeaseDay_Object((1,3,6,1,4,1,1991,1,1,3,42,2,1,1,6),_SnDhcpServerPoolLeaseDay_Type())
snDhcpServerPoolLeaseDay.setMaxAccess(_E)
if mibBuilder.loadTexts:snDhcpServerPoolLeaseDay.setStatus(_A)
class _SnDhcpServerPoolLeaseHour_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_SnDhcpServerPoolLeaseHour_Type.__name__=_D
_SnDhcpServerPoolLeaseHour_Object=MibTableColumn
snDhcpServerPoolLeaseHour=_SnDhcpServerPoolLeaseHour_Object((1,3,6,1,4,1,1991,1,1,3,42,2,1,1,7),_SnDhcpServerPoolLeaseHour_Type())
snDhcpServerPoolLeaseHour.setMaxAccess(_E)
if mibBuilder.loadTexts:snDhcpServerPoolLeaseHour.setStatus(_A)
class _SnDhcpServerPoolLeaseMinute_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_SnDhcpServerPoolLeaseMinute_Type.__name__=_D
_SnDhcpServerPoolLeaseMinute_Object=MibTableColumn
snDhcpServerPoolLeaseMinute=_SnDhcpServerPoolLeaseMinute_Object((1,3,6,1,4,1,1991,1,1,3,42,2,1,1,8),_SnDhcpServerPoolLeaseMinute_Type())
snDhcpServerPoolLeaseMinute.setMaxAccess(_E)
if mibBuilder.loadTexts:snDhcpServerPoolLeaseMinute.setStatus(_A)
class _SnDhcpServerPoolDeploy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('nodeploy',0),('deploy',1)))
_SnDhcpServerPoolDeploy_Type.__name__=_D
_SnDhcpServerPoolDeploy_Object=MibTableColumn
snDhcpServerPoolDeploy=_SnDhcpServerPoolDeploy_Object((1,3,6,1,4,1,1991,1,1,3,42,2,1,1,9),_SnDhcpServerPoolDeploy_Type())
snDhcpServerPoolDeploy.setMaxAccess(_E)
if mibBuilder.loadTexts:snDhcpServerPoolDeploy.setStatus(_A)
class _SnDhcpServerPoolRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('valid',2),('delete',3),('create',4)))
_SnDhcpServerPoolRowStatus_Type.__name__=_D
_SnDhcpServerPoolRowStatus_Object=MibTableColumn
snDhcpServerPoolRowStatus=_SnDhcpServerPoolRowStatus_Object((1,3,6,1,4,1,1991,1,1,3,42,2,1,1,10),_SnDhcpServerPoolRowStatus_Type())
snDhcpServerPoolRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:snDhcpServerPoolRowStatus.setStatus(_A)
_SnDhcpServerPoolOptionConfigTable_Object=MibTable
snDhcpServerPoolOptionConfigTable=_SnDhcpServerPoolOptionConfigTable_Object((1,3,6,1,4,1,1991,1,1,3,42,2,2))
if mibBuilder.loadTexts:snDhcpServerPoolOptionConfigTable.setStatus(_A)
_SnDhcpServerPoolOptionConfigEntry_Object=MibTableRow
snDhcpServerPoolOptionConfigEntry=_SnDhcpServerPoolOptionConfigEntry_Object((1,3,6,1,4,1,1991,1,1,3,42,2,2,1))
snDhcpServerPoolOptionConfigEntry.setIndexNames((0,_F,_G),(0,_F,_J))
if mibBuilder.loadTexts:snDhcpServerPoolOptionConfigEntry.setStatus(_A)
class _SnDhcpServerPoolOptionCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_SnDhcpServerPoolOptionCode_Type.__name__=_D
_SnDhcpServerPoolOptionCode_Object=MibTableColumn
snDhcpServerPoolOptionCode=_SnDhcpServerPoolOptionCode_Object((1,3,6,1,4,1,1991,1,1,3,42,2,2,1,1),_SnDhcpServerPoolOptionCode_Type())
snDhcpServerPoolOptionCode.setMaxAccess(_H)
if mibBuilder.loadTexts:snDhcpServerPoolOptionCode.setStatus(_A)
class _SnDhcpServerPoolOptionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('ascii',0),('hex',1),('ip',2),('bool',3),('integer',4),('telephony',5),('ipaddrpair',6),('staticroute',7),('slpdiragent',8),('slpsrvscope',9),('pxeintfid',10),('pxeclientid',11)))
_SnDhcpServerPoolOptionType_Type.__name__=_D
_SnDhcpServerPoolOptionType_Object=MibTableColumn
snDhcpServerPoolOptionType=_SnDhcpServerPoolOptionType_Object((1,3,6,1,4,1,1991,1,1,3,42,2,2,1,2),_SnDhcpServerPoolOptionType_Type())
snDhcpServerPoolOptionType.setMaxAccess(_B)
if mibBuilder.loadTexts:snDhcpServerPoolOptionType.setStatus(_A)
class _SnDhcpServerPoolOptionAscii_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_SnDhcpServerPoolOptionAscii_Type.__name__=_C
_SnDhcpServerPoolOptionAscii_Object=MibTableColumn
snDhcpServerPoolOptionAscii=_SnDhcpServerPoolOptionAscii_Object((1,3,6,1,4,1,1991,1,1,3,42,2,2,1,3),_SnDhcpServerPoolOptionAscii_Type())
snDhcpServerPoolOptionAscii.setMaxAccess(_B)
if mibBuilder.loadTexts:snDhcpServerPoolOptionAscii.setStatus(_A)
class _SnDhcpServerPoolOptionHexString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_SnDhcpServerPoolOptionHexString_Type.__name__=_C
_SnDhcpServerPoolOptionHexString_Object=MibTableColumn
snDhcpServerPoolOptionHexString=_SnDhcpServerPoolOptionHexString_Object((1,3,6,1,4,1,1991,1,1,3,42,2,2,1,4),_SnDhcpServerPoolOptionHexString_Type())
snDhcpServerPoolOptionHexString.setMaxAccess(_B)
if mibBuilder.loadTexts:snDhcpServerPoolOptionHexString.setStatus(_A)
class _SnDhcpServerPoolOptionIPString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,12))
_SnDhcpServerPoolOptionIPString_Type.__name__=_C
_SnDhcpServerPoolOptionIPString_Object=MibTableColumn
snDhcpServerPoolOptionIPString=_SnDhcpServerPoolOptionIPString_Object((1,3,6,1,4,1,1991,1,1,3,42,2,2,1,5),_SnDhcpServerPoolOptionIPString_Type())
snDhcpServerPoolOptionIPString.setMaxAccess(_B)
if mibBuilder.loadTexts:snDhcpServerPoolOptionIPString.setStatus(_A)
_SnDhcpServerPoolOptionRowStatus_Type=RowStatus
_SnDhcpServerPoolOptionRowStatus_Object=MibTableColumn
snDhcpServerPoolOptionRowStatus=_SnDhcpServerPoolOptionRowStatus_Object((1,3,6,1,4,1,1991,1,1,3,42,2,2,1,6),_SnDhcpServerPoolOptionRowStatus_Type())
snDhcpServerPoolOptionRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snDhcpServerPoolOptionRowStatus.setStatus(_A)
class _SnDhcpServerPoolOptionBoolString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,12))
_SnDhcpServerPoolOptionBoolString_Type.__name__=_C
_SnDhcpServerPoolOptionBoolString_Object=MibTableColumn
snDhcpServerPoolOptionBoolString=_SnDhcpServerPoolOptionBoolString_Object((1,3,6,1,4,1,1991,1,1,3,42,2,2,1,7),_SnDhcpServerPoolOptionBoolString_Type())
snDhcpServerPoolOptionBoolString.setMaxAccess(_B)
if mibBuilder.loadTexts:snDhcpServerPoolOptionBoolString.setStatus(_A)
class _SnDhcpServerPoolOptionIntString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,12))
_SnDhcpServerPoolOptionIntString_Type.__name__=_C
_SnDhcpServerPoolOptionIntString_Object=MibTableColumn
snDhcpServerPoolOptionIntString=_SnDhcpServerPoolOptionIntString_Object((1,3,6,1,4,1,1991,1,1,3,42,2,2,1,8),_SnDhcpServerPoolOptionIntString_Type())
snDhcpServerPoolOptionIntString.setMaxAccess(_B)
if mibBuilder.loadTexts:snDhcpServerPoolOptionIntString.setStatus(_A)
class _SnDhcpServerPoolOptionIPAddrPairString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,16))
_SnDhcpServerPoolOptionIPAddrPairString_Type.__name__=_C
_SnDhcpServerPoolOptionIPAddrPairString_Object=MibTableColumn
snDhcpServerPoolOptionIPAddrPairString=_SnDhcpServerPoolOptionIPAddrPairString_Object((1,3,6,1,4,1,1991,1,1,3,42,2,2,1,9),_SnDhcpServerPoolOptionIPAddrPairString_Type())
snDhcpServerPoolOptionIPAddrPairString.setMaxAccess(_B)
if mibBuilder.loadTexts:snDhcpServerPoolOptionIPAddrPairString.setStatus(_A)
class _SnDhcpServerPoolOptionStaticRouteString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,16))
_SnDhcpServerPoolOptionStaticRouteString_Type.__name__=_C
_SnDhcpServerPoolOptionStaticRouteString_Object=MibTableColumn
snDhcpServerPoolOptionStaticRouteString=_SnDhcpServerPoolOptionStaticRouteString_Object((1,3,6,1,4,1,1991,1,1,3,42,2,2,1,10),_SnDhcpServerPoolOptionStaticRouteString_Type())
snDhcpServerPoolOptionStaticRouteString.setMaxAccess(_B)
if mibBuilder.loadTexts:snDhcpServerPoolOptionStaticRouteString.setStatus(_A)
class _SnDhcpServerPoolOptionSlpDirAgentString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,54))
_SnDhcpServerPoolOptionSlpDirAgentString_Type.__name__=_C
_SnDhcpServerPoolOptionSlpDirAgentString_Object=MibTableColumn
snDhcpServerPoolOptionSlpDirAgentString=_SnDhcpServerPoolOptionSlpDirAgentString_Object((1,3,6,1,4,1,1991,1,1,3,42,2,2,1,11),_SnDhcpServerPoolOptionSlpDirAgentString_Type())
snDhcpServerPoolOptionSlpDirAgentString.setMaxAccess(_B)
if mibBuilder.loadTexts:snDhcpServerPoolOptionSlpDirAgentString.setStatus(_A)
class _SnDhcpServerPoolOptionSlpSrvScopeString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,135))
_SnDhcpServerPoolOptionSlpSrvScopeString_Type.__name__=_C
_SnDhcpServerPoolOptionSlpSrvScopeString_Object=MibTableColumn
snDhcpServerPoolOptionSlpSrvScopeString=_SnDhcpServerPoolOptionSlpSrvScopeString_Object((1,3,6,1,4,1,1991,1,1,3,42,2,2,1,12),_SnDhcpServerPoolOptionSlpSrvScopeString_Type())
snDhcpServerPoolOptionSlpSrvScopeString.setMaxAccess(_B)
if mibBuilder.loadTexts:snDhcpServerPoolOptionSlpSrvScopeString.setStatus(_A)
class _SnDhcpServerPoolOptionPxeIntfIdString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_SnDhcpServerPoolOptionPxeIntfIdString_Type.__name__=_C
_SnDhcpServerPoolOptionPxeIntfIdString_Object=MibTableColumn
snDhcpServerPoolOptionPxeIntfIdString=_SnDhcpServerPoolOptionPxeIntfIdString_Object((1,3,6,1,4,1,1991,1,1,3,42,2,2,1,13),_SnDhcpServerPoolOptionPxeIntfIdString_Type())
snDhcpServerPoolOptionPxeIntfIdString.setMaxAccess(_B)
if mibBuilder.loadTexts:snDhcpServerPoolOptionPxeIntfIdString.setStatus(_A)
class _SnDhcpServerPoolOptionPxeClientIdString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,132))
_SnDhcpServerPoolOptionPxeClientIdString_Type.__name__=_C
_SnDhcpServerPoolOptionPxeClientIdString_Object=MibTableColumn
snDhcpServerPoolOptionPxeClientIdString=_SnDhcpServerPoolOptionPxeClientIdString_Object((1,3,6,1,4,1,1991,1,1,3,42,2,2,1,14),_SnDhcpServerPoolOptionPxeClientIdString_Type())
snDhcpServerPoolOptionPxeClientIdString.setMaxAccess(_B)
if mibBuilder.loadTexts:snDhcpServerPoolOptionPxeClientIdString.setStatus(_A)
_SnDhcpServerPoolExcludedSingleAddressTable_Object=MibTable
snDhcpServerPoolExcludedSingleAddressTable=_SnDhcpServerPoolExcludedSingleAddressTable_Object((1,3,6,1,4,1,1991,1,1,3,42,2,3))
if mibBuilder.loadTexts:snDhcpServerPoolExcludedSingleAddressTable.setStatus(_A)
_SnDhcpServerPoolExcludedSingleAddressEntry_Object=MibTableRow
snDhcpServerPoolExcludedSingleAddressEntry=_SnDhcpServerPoolExcludedSingleAddressEntry_Object((1,3,6,1,4,1,1991,1,1,3,42,2,3,1))
snDhcpServerPoolExcludedSingleAddressEntry.setIndexNames((0,_F,_G),(0,_F,_K))
if mibBuilder.loadTexts:snDhcpServerPoolExcludedSingleAddressEntry.setStatus(_A)
class _SnDhcpServerPoolExcludedAddressIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_SnDhcpServerPoolExcludedAddressIndex_Type.__name__=_D
_SnDhcpServerPoolExcludedAddressIndex_Object=MibTableColumn
snDhcpServerPoolExcludedAddressIndex=_SnDhcpServerPoolExcludedAddressIndex_Object((1,3,6,1,4,1,1991,1,1,3,42,2,3,1,1),_SnDhcpServerPoolExcludedAddressIndex_Type())
snDhcpServerPoolExcludedAddressIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:snDhcpServerPoolExcludedAddressIndex.setStatus(_A)
_SnDhcpServerPoolExcludedSingleAddress_Type=IpAddress
_SnDhcpServerPoolExcludedSingleAddress_Object=MibTableColumn
snDhcpServerPoolExcludedSingleAddress=_SnDhcpServerPoolExcludedSingleAddress_Object((1,3,6,1,4,1,1991,1,1,3,42,2,3,1,2),_SnDhcpServerPoolExcludedSingleAddress_Type())
snDhcpServerPoolExcludedSingleAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:snDhcpServerPoolExcludedSingleAddress.setStatus(_A)
_SnDhcpServerPoolExcludedSingleAddressRowStatus_Type=RowStatus
_SnDhcpServerPoolExcludedSingleAddressRowStatus_Object=MibTableColumn
snDhcpServerPoolExcludedSingleAddressRowStatus=_SnDhcpServerPoolExcludedSingleAddressRowStatus_Object((1,3,6,1,4,1,1991,1,1,3,42,2,3,1,3),_SnDhcpServerPoolExcludedSingleAddressRowStatus_Type())
snDhcpServerPoolExcludedSingleAddressRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snDhcpServerPoolExcludedSingleAddressRowStatus.setStatus(_A)
_SnDhcpServerPoolExcludedAddressRangeTable_Object=MibTable
snDhcpServerPoolExcludedAddressRangeTable=_SnDhcpServerPoolExcludedAddressRangeTable_Object((1,3,6,1,4,1,1991,1,1,3,42,2,4))
if mibBuilder.loadTexts:snDhcpServerPoolExcludedAddressRangeTable.setStatus(_A)
_SnDhcpServerPoolExcludedAddressRangeEntry_Object=MibTableRow
snDhcpServerPoolExcludedAddressRangeEntry=_SnDhcpServerPoolExcludedAddressRangeEntry_Object((1,3,6,1,4,1,1991,1,1,3,42,2,4,1))
snDhcpServerPoolExcludedAddressRangeEntry.setIndexNames((0,_F,_G),(0,_F,_L))
if mibBuilder.loadTexts:snDhcpServerPoolExcludedAddressRangeEntry.setStatus(_A)
class _SnDhcpServerPoolExcludedAddressRangeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,85))
_SnDhcpServerPoolExcludedAddressRangeIndex_Type.__name__=_D
_SnDhcpServerPoolExcludedAddressRangeIndex_Object=MibTableColumn
snDhcpServerPoolExcludedAddressRangeIndex=_SnDhcpServerPoolExcludedAddressRangeIndex_Object((1,3,6,1,4,1,1991,1,1,3,42,2,4,1,1),_SnDhcpServerPoolExcludedAddressRangeIndex_Type())
snDhcpServerPoolExcludedAddressRangeIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:snDhcpServerPoolExcludedAddressRangeIndex.setStatus(_A)
_SnDhcpServerPoolExcludedStartAddress_Type=IpAddress
_SnDhcpServerPoolExcludedStartAddress_Object=MibTableColumn
snDhcpServerPoolExcludedStartAddress=_SnDhcpServerPoolExcludedStartAddress_Object((1,3,6,1,4,1,1991,1,1,3,42,2,4,1,2),_SnDhcpServerPoolExcludedStartAddress_Type())
snDhcpServerPoolExcludedStartAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:snDhcpServerPoolExcludedStartAddress.setStatus(_A)
_SnDhcpServerPoolExcludedEndAddress_Type=IpAddress
_SnDhcpServerPoolExcludedEndAddress_Object=MibTableColumn
snDhcpServerPoolExcludedEndAddress=_SnDhcpServerPoolExcludedEndAddress_Object((1,3,6,1,4,1,1991,1,1,3,42,2,4,1,3),_SnDhcpServerPoolExcludedEndAddress_Type())
snDhcpServerPoolExcludedEndAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:snDhcpServerPoolExcludedEndAddress.setStatus(_A)
_SnDhcpServerPoolExcludedAddressRowStatus_Type=RowStatus
_SnDhcpServerPoolExcludedAddressRowStatus_Object=MibTableColumn
snDhcpServerPoolExcludedAddressRowStatus=_SnDhcpServerPoolExcludedAddressRowStatus_Object((1,3,6,1,4,1,1991,1,1,3,42,2,4,1,4),_SnDhcpServerPoolExcludedAddressRowStatus_Type())
snDhcpServerPoolExcludedAddressRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snDhcpServerPoolExcludedAddressRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'snDhcpServer':snDhcpServer,'snDhcpServerGlobalObjects':snDhcpServerGlobalObjects,'snDhcpServerGlobalConfigState':snDhcpServerGlobalConfigState,'snDhcpServerTableObjects':snDhcpServerTableObjects,'snDhcpServerPoolConfigTable':snDhcpServerPoolConfigTable,'snDhcpServerPoolConfigEntry':snDhcpServerPoolConfigEntry,_G:snDhcpServerPoolName,'snDhcpServerPoolNetwork':snDhcpServerPoolNetwork,'snDhcpServerPoolNetworkMask':snDhcpServerPoolNetworkMask,'snDhcpServerPoolStartAddr':snDhcpServerPoolStartAddr,'snDhcpServerPoolEndAddr':snDhcpServerPoolEndAddr,'snDhcpServerPoolLeaseDay':snDhcpServerPoolLeaseDay,'snDhcpServerPoolLeaseHour':snDhcpServerPoolLeaseHour,'snDhcpServerPoolLeaseMinute':snDhcpServerPoolLeaseMinute,'snDhcpServerPoolDeploy':snDhcpServerPoolDeploy,'snDhcpServerPoolRowStatus':snDhcpServerPoolRowStatus,'snDhcpServerPoolOptionConfigTable':snDhcpServerPoolOptionConfigTable,'snDhcpServerPoolOptionConfigEntry':snDhcpServerPoolOptionConfigEntry,_J:snDhcpServerPoolOptionCode,'snDhcpServerPoolOptionType':snDhcpServerPoolOptionType,'snDhcpServerPoolOptionAscii':snDhcpServerPoolOptionAscii,'snDhcpServerPoolOptionHexString':snDhcpServerPoolOptionHexString,'snDhcpServerPoolOptionIPString':snDhcpServerPoolOptionIPString,'snDhcpServerPoolOptionRowStatus':snDhcpServerPoolOptionRowStatus,'snDhcpServerPoolOptionBoolString':snDhcpServerPoolOptionBoolString,'snDhcpServerPoolOptionIntString':snDhcpServerPoolOptionIntString,'snDhcpServerPoolOptionIPAddrPairString':snDhcpServerPoolOptionIPAddrPairString,'snDhcpServerPoolOptionStaticRouteString':snDhcpServerPoolOptionStaticRouteString,'snDhcpServerPoolOptionSlpDirAgentString':snDhcpServerPoolOptionSlpDirAgentString,'snDhcpServerPoolOptionSlpSrvScopeString':snDhcpServerPoolOptionSlpSrvScopeString,'snDhcpServerPoolOptionPxeIntfIdString':snDhcpServerPoolOptionPxeIntfIdString,'snDhcpServerPoolOptionPxeClientIdString':snDhcpServerPoolOptionPxeClientIdString,'snDhcpServerPoolExcludedSingleAddressTable':snDhcpServerPoolExcludedSingleAddressTable,'snDhcpServerPoolExcludedSingleAddressEntry':snDhcpServerPoolExcludedSingleAddressEntry,_K:snDhcpServerPoolExcludedAddressIndex,'snDhcpServerPoolExcludedSingleAddress':snDhcpServerPoolExcludedSingleAddress,'snDhcpServerPoolExcludedSingleAddressRowStatus':snDhcpServerPoolExcludedSingleAddressRowStatus,'snDhcpServerPoolExcludedAddressRangeTable':snDhcpServerPoolExcludedAddressRangeTable,'snDhcpServerPoolExcludedAddressRangeEntry':snDhcpServerPoolExcludedAddressRangeEntry,_L:snDhcpServerPoolExcludedAddressRangeIndex,'snDhcpServerPoolExcludedStartAddress':snDhcpServerPoolExcludedStartAddress,'snDhcpServerPoolExcludedEndAddress':snDhcpServerPoolExcludedEndAddress,'snDhcpServerPoolExcludedAddressRowStatus':snDhcpServerPoolExcludedAddressRowStatus})