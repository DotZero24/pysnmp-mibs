_r='fsLldpStatsRemTablesUpdates'
_q='fsLldpStatsTaggedTxPortEntry'
_p='fsLldpManAddrConfigEntry'
_o='fslldpV2AddressTableIndex'
_n='fslldpv2ConfigPortMapDestMacAddress'
_m='fslldpv2ConfigPortMapIfIndex'
_l='ifname'
_k='nwaddr'
_j='macaddr'
_i='portcomp'
_h='ifalias'
_g='TruthValue'
_f='MacAddress'
_e='DisplayString'
_d='lldpStatsRemTablesInserts'
_c='lldpStatsRemTablesDrops'
_b='lldpStatsRemTablesDeletes'
_a='lldpStatsRemTablesAgeouts'
_Z='lldpRemSysName'
_Y='lldpRemManAddrIfId'
_X='lldpLocPortNum'
_W='lldpLocPortId'
_V='lldpXdot3RemPowerClass'
_U='lldpXdot3RemPortOperMauType'
_T='lldpXdot3RemMaxFrameSize'
_S='lldpXdot3RemLinkAggStatus'
_R='lldpXdot1RemVlanName'
_Q='lldpXdot1RemProtocolId'
_P='lldpXdot1RemProtoVlanSupported'
_O='lldpXdot1RemPortVlanId'
_N='not-accessible'
_M='disabled'
_L='enabled'
_K='OctetString'
_J='LLDP-EXT-DOT3-MIB'
_I='LLDP-EXT-DOT1-MIB'
_H='ARICENT-LLDP-MIB'
_G='read-only'
_F='Integer32'
_E='lldpRemPortId'
_D='lldpRemChassisId'
_C='read-write'
_B='LLDP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
lldpXdot1RemPortVlanId,lldpXdot1RemProtoVlanSupported,lldpXdot1RemProtocolId,lldpXdot1RemVlanName=mibBuilder.importSymbols(_I,_O,_P,_Q,_R)
lldpXdot3RemLinkAggStatus,lldpXdot3RemMaxFrameSize,lldpXdot3RemPortOperMauType,lldpXdot3RemPowerClass=mibBuilder.importSymbols(_J,_S,_T,_U,_V)
LldpPortNumber,lldpLocManAddrEntry,lldpLocPortId,lldpLocPortNum,lldpRemChassisId,lldpRemManAddrIfId,lldpRemPortId,lldpRemSysName,lldpStatsRemTablesAgeouts,lldpStatsRemTablesDeletes,lldpStatsRemTablesDrops,lldpStatsRemTablesInserts=mibBuilder.importSymbols(_B,'LldpPortNumber','lldpLocManAddrEntry',_W,_X,_D,_Y,_E,_Z,_a,_b,_c,_d)
lldpV2StatsTxPortEntry,=mibBuilder.importSymbols('LLDP-V2-MIB','lldpV2StatsTxPortEntry')
LldpV2DestAddressTableIndex,=mibBuilder.importSymbols('LLDP-V2-TC-MIB','LldpV2DestAddressTableIndex')
ZeroBasedCounter32,=mibBuilder.importSymbols('RMON2-MIB','ZeroBasedCounter32')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_e,_f,'PhysAddress','RowStatus','TextualConvention',_g)
fslldp=ModuleIdentity((1,3,6,1,4,1,2076,158))
if mibBuilder.loadTexts:fslldp.setRevisions(('2012-09-05 00:00',))
_FsLldpSystem_ObjectIdentity=ObjectIdentity
fsLldpSystem=_FsLldpSystem_ObjectIdentity((1,3,6,1,4,1,2076,158,1))
class _FsLldpSystemControl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('start',1),('shutdownInProgress',2),('shutdown',3)))
_FsLldpSystemControl_Type.__name__=_F
_FsLldpSystemControl_Object=MibScalar
fsLldpSystemControl=_FsLldpSystemControl_Object((1,3,6,1,4,1,2076,158,1,1),_FsLldpSystemControl_Type())
fsLldpSystemControl.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLldpSystemControl.setStatus(_A)
class _FsLldpModuleStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_FsLldpModuleStatus_Type.__name__=_F
_FsLldpModuleStatus_Object=MibScalar
fsLldpModuleStatus=_FsLldpModuleStatus_Object((1,3,6,1,4,1,2076,158,1,2),_FsLldpModuleStatus_Type())
fsLldpModuleStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLldpModuleStatus.setStatus(_A)
class _FsLldpTraceInput_Type(DisplayString):defaultValue=OctetString('critical');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,288))
_FsLldpTraceInput_Type.__name__=_e
_FsLldpTraceInput_Object=MibScalar
fsLldpTraceInput=_FsLldpTraceInput_Object((1,3,6,1,4,1,2076,158,1,3),_FsLldpTraceInput_Type())
fsLldpTraceInput.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLldpTraceInput.setStatus(_A)
class _FsLldpTraceOption_Type(Integer32):defaultValue=8192
_FsLldpTraceOption_Type.__name__=_F
_FsLldpTraceOption_Object=MibScalar
fsLldpTraceOption=_FsLldpTraceOption_Object((1,3,6,1,4,1,2076,158,1,4),_FsLldpTraceOption_Type())
fsLldpTraceOption.setMaxAccess(_G)
if mibBuilder.loadTexts:fsLldpTraceOption.setStatus(_A)
class _FsLldpTraceLevel_Type(Integer32):defaultValue=8192
_FsLldpTraceLevel_Type.__name__=_F
_FsLldpTraceLevel_Object=MibScalar
fsLldpTraceLevel=_FsLldpTraceLevel_Object((1,3,6,1,4,1,2076,158,1,5),_FsLldpTraceLevel_Type())
fsLldpTraceLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLldpTraceLevel.setStatus(_A)
class _FsLldpTagStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_FsLldpTagStatus_Type.__name__=_F
_FsLldpTagStatus_Object=MibScalar
fsLldpTagStatus=_FsLldpTagStatus_Object((1,3,6,1,4,1,2076,158,1,6),_FsLldpTagStatus_Type())
fsLldpTagStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLldpTagStatus.setStatus(_A)
_FsLldpConfiguredMgmtIpv4Address_Type=InetAddressIPv4
_FsLldpConfiguredMgmtIpv4Address_Object=MibScalar
fsLldpConfiguredMgmtIpv4Address=_FsLldpConfiguredMgmtIpv4Address_Object((1,3,6,1,4,1,2076,158,1,7),_FsLldpConfiguredMgmtIpv4Address_Type())
fsLldpConfiguredMgmtIpv4Address.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLldpConfiguredMgmtIpv4Address.setStatus(_A)
_FsLldpConfiguredMgmtIpv6Address_Type=InetAddressIPv6
_FsLldpConfiguredMgmtIpv6Address_Object=MibScalar
fsLldpConfiguredMgmtIpv6Address=_FsLldpConfiguredMgmtIpv6Address_Object((1,3,6,1,4,1,2076,158,1,8),_FsLldpConfiguredMgmtIpv6Address_Type())
fsLldpConfiguredMgmtIpv6Address.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLldpConfiguredMgmtIpv6Address.setStatus(_A)
_FsLldpTLV_ObjectIdentity=ObjectIdentity
fsLldpTLV=_FsLldpTLV_ObjectIdentity((1,3,6,1,4,1,2076,158,2))
class _FsLldpLocChassisIdSubtype_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('chassiscomp',1),(_h,2),(_i,3),(_j,4),(_k,5),(_l,6),('local',7)))
_FsLldpLocChassisIdSubtype_Type.__name__=_F
_FsLldpLocChassisIdSubtype_Object=MibScalar
fsLldpLocChassisIdSubtype=_FsLldpLocChassisIdSubtype_Object((1,3,6,1,4,1,2076,158,2,1),_FsLldpLocChassisIdSubtype_Type())
fsLldpLocChassisIdSubtype.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLldpLocChassisIdSubtype.setStatus(_A)
class _FsLldpLocChassisId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_FsLldpLocChassisId_Type.__name__=_K
_FsLldpLocChassisId_Object=MibScalar
fsLldpLocChassisId=_FsLldpLocChassisId_Object((1,3,6,1,4,1,2076,158,2,2),_FsLldpLocChassisId_Type())
fsLldpLocChassisId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLldpLocChassisId.setStatus(_A)
_FsLldpLocPortTable_Object=MibTable
fsLldpLocPortTable=_FsLldpLocPortTable_Object((1,3,6,1,4,1,2076,158,2,3))
if mibBuilder.loadTexts:fsLldpLocPortTable.setStatus(_A)
_FsLldpLocPortEntry_Object=MibTableRow
fsLldpLocPortEntry=_FsLldpLocPortEntry_Object((1,3,6,1,4,1,2076,158,2,3,1))
fsLldpLocPortEntry.setIndexNames((0,_B,_X))
if mibBuilder.loadTexts:fsLldpLocPortEntry.setStatus(_A)
class _FsLldpLocPortIdSubtype_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_h,1),(_i,2),(_j,3),(_k,4),(_l,5),('agentcircuitid',6),('local',7)))
_FsLldpLocPortIdSubtype_Type.__name__=_F
_FsLldpLocPortIdSubtype_Object=MibTableColumn
fsLldpLocPortIdSubtype=_FsLldpLocPortIdSubtype_Object((1,3,6,1,4,1,2076,158,2,3,1,1),_FsLldpLocPortIdSubtype_Type())
fsLldpLocPortIdSubtype.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLldpLocPortIdSubtype.setStatus(_A)
class _FsLldpLocPortId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_FsLldpLocPortId_Type.__name__=_K
_FsLldpLocPortId_Object=MibTableColumn
fsLldpLocPortId=_FsLldpLocPortId_Object((1,3,6,1,4,1,2076,158,2,3,1,2),_FsLldpLocPortId_Type())
fsLldpLocPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLldpLocPortId.setStatus(_A)
class _FsLldpPortConfigNotificationType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('remTabChg',1),('misCfg',2),('remTabChgAndMisCfg',3)))
_FsLldpPortConfigNotificationType_Type.__name__=_F
_FsLldpPortConfigNotificationType_Object=MibTableColumn
fsLldpPortConfigNotificationType=_FsLldpPortConfigNotificationType_Object((1,3,6,1,4,1,2076,158,2,3,1,3),_FsLldpPortConfigNotificationType_Type())
fsLldpPortConfigNotificationType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLldpPortConfigNotificationType.setStatus(_A)
class _FsLldpLocPortDstMac_Type(MacAddress):defaultHexValue='0180C200000E'
_FsLldpLocPortDstMac_Type.__name__=_f
_FsLldpLocPortDstMac_Object=MibTableColumn
fsLldpLocPortDstMac=_FsLldpLocPortDstMac_Object((1,3,6,1,4,1,2076,158,2,3,1,4),_FsLldpLocPortDstMac_Type())
fsLldpLocPortDstMac.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLldpLocPortDstMac.setStatus(_A)
class _FsLldpMedAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_FsLldpMedAdminStatus_Type.__name__=_F
_FsLldpMedAdminStatus_Object=MibTableColumn
fsLldpMedAdminStatus=_FsLldpMedAdminStatus_Object((1,3,6,1,4,1,2076,158,2,3,1,5),_FsLldpMedAdminStatus_Type())
fsLldpMedAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLldpMedAdminStatus.setStatus(_A)
_FsLldpManAddrConfigTable_Object=MibTable
fsLldpManAddrConfigTable=_FsLldpManAddrConfigTable_Object((1,3,6,1,4,1,2076,158,2,4))
if mibBuilder.loadTexts:fsLldpManAddrConfigTable.setStatus(_A)
_FsLldpManAddrConfigEntry_Object=MibTableRow
fsLldpManAddrConfigEntry=_FsLldpManAddrConfigEntry_Object((1,3,6,1,4,1,2076,158,2,4,1))
if mibBuilder.loadTexts:fsLldpManAddrConfigEntry.setStatus(_A)
class _FsLldpManAddrConfigOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_FsLldpManAddrConfigOperStatus_Type.__name__=_F
_FsLldpManAddrConfigOperStatus_Object=MibTableColumn
fsLldpManAddrConfigOperStatus=_FsLldpManAddrConfigOperStatus_Object((1,3,6,1,4,1,2076,158,2,4,1,1),_FsLldpManAddrConfigOperStatus_Type())
fsLldpManAddrConfigOperStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:fsLldpManAddrConfigOperStatus.setStatus(_A)
_FsLldpStatistics_ObjectIdentity=ObjectIdentity
fsLldpStatistics=_FsLldpStatistics_ObjectIdentity((1,3,6,1,4,1,2076,158,3))
_FsLldpMemAllocFailure_Type=Integer32
_FsLldpMemAllocFailure_Object=MibScalar
fsLldpMemAllocFailure=_FsLldpMemAllocFailure_Object((1,3,6,1,4,1,2076,158,3,1),_FsLldpMemAllocFailure_Type())
fsLldpMemAllocFailure.setMaxAccess(_G)
if mibBuilder.loadTexts:fsLldpMemAllocFailure.setStatus(_A)
_FsLldpInputQOverFlows_Type=Integer32
_FsLldpInputQOverFlows_Object=MibScalar
fsLldpInputQOverFlows=_FsLldpInputQOverFlows_Object((1,3,6,1,4,1,2076,158,3,2),_FsLldpInputQOverFlows_Type())
fsLldpInputQOverFlows.setMaxAccess(_G)
if mibBuilder.loadTexts:fsLldpInputQOverFlows.setStatus(_A)
_FsLldpStatsRemTablesUpdates_Type=ZeroBasedCounter32
_FsLldpStatsRemTablesUpdates_Object=MibScalar
fsLldpStatsRemTablesUpdates=_FsLldpStatsRemTablesUpdates_Object((1,3,6,1,4,1,2076,158,3,3),_FsLldpStatsRemTablesUpdates_Type())
fsLldpStatsRemTablesUpdates.setMaxAccess(_G)
if mibBuilder.loadTexts:fsLldpStatsRemTablesUpdates.setStatus(_A)
if mibBuilder.loadTexts:fsLldpStatsRemTablesUpdates.setUnits('table entries')
class _FsLldpClearStats_Type(TruthValue):defaultValue=2
_FsLldpClearStats_Type.__name__=_g
_FsLldpClearStats_Object=MibScalar
fsLldpClearStats=_FsLldpClearStats_Object((1,3,6,1,4,1,2076,158,3,4),_FsLldpClearStats_Type())
fsLldpClearStats.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLldpClearStats.setStatus(_A)
_FsLldpNotification_ObjectIdentity=ObjectIdentity
fsLldpNotification=_FsLldpNotification_ObjectIdentity((1,3,6,1,4,1,2076,158,4))
_FsLldpTraps_ObjectIdentity=ObjectIdentity
fsLldpTraps=_FsLldpTraps_ObjectIdentity((1,3,6,1,4,1,2076,158,4,0))
_Fslldpv2Config_ObjectIdentity=ObjectIdentity
fslldpv2Config=_Fslldpv2Config_ObjectIdentity((1,3,6,1,4,1,2076,158,5))
class _Fslldpv2Version_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('lldpv1',1),('lldpv2',2)))
_Fslldpv2Version_Type.__name__=_F
_Fslldpv2Version_Object=MibScalar
fslldpv2Version=_Fslldpv2Version_Object((1,3,6,1,4,1,2076,158,5,1),_Fslldpv2Version_Type())
fslldpv2Version.setMaxAccess(_C)
if mibBuilder.loadTexts:fslldpv2Version.setStatus(_A)
_Fslldpv2ConfigPortMapTable_Object=MibTable
fslldpv2ConfigPortMapTable=_Fslldpv2ConfigPortMapTable_Object((1,3,6,1,4,1,2076,158,5,2))
if mibBuilder.loadTexts:fslldpv2ConfigPortMapTable.setStatus(_A)
_Fslldpv2ConfigPortMapEntry_Object=MibTableRow
fslldpv2ConfigPortMapEntry=_Fslldpv2ConfigPortMapEntry_Object((1,3,6,1,4,1,2076,158,5,2,1))
fslldpv2ConfigPortMapEntry.setIndexNames((0,_H,_m),(0,_H,_n))
if mibBuilder.loadTexts:fslldpv2ConfigPortMapEntry.setStatus(_A)
_Fslldpv2ConfigPortMapIfIndex_Type=InterfaceIndex
_Fslldpv2ConfigPortMapIfIndex_Object=MibTableColumn
fslldpv2ConfigPortMapIfIndex=_Fslldpv2ConfigPortMapIfIndex_Object((1,3,6,1,4,1,2076,158,5,2,1,1),_Fslldpv2ConfigPortMapIfIndex_Type())
fslldpv2ConfigPortMapIfIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:fslldpv2ConfigPortMapIfIndex.setStatus(_A)
_Fslldpv2ConfigPortMapDestMacAddress_Type=MacAddress
_Fslldpv2ConfigPortMapDestMacAddress_Object=MibTableColumn
fslldpv2ConfigPortMapDestMacAddress=_Fslldpv2ConfigPortMapDestMacAddress_Object((1,3,6,1,4,1,2076,158,5,2,1,2),_Fslldpv2ConfigPortMapDestMacAddress_Type())
fslldpv2ConfigPortMapDestMacAddress.setMaxAccess(_N)
if mibBuilder.loadTexts:fslldpv2ConfigPortMapDestMacAddress.setStatus(_A)
_Fslldpv2ConfigPortMapNum_Type=LldpPortNumber
_Fslldpv2ConfigPortMapNum_Object=MibTableColumn
fslldpv2ConfigPortMapNum=_Fslldpv2ConfigPortMapNum_Object((1,3,6,1,4,1,2076,158,5,2,1,3),_Fslldpv2ConfigPortMapNum_Type())
fslldpv2ConfigPortMapNum.setMaxAccess(_G)
if mibBuilder.loadTexts:fslldpv2ConfigPortMapNum.setStatus(_A)
_Fslldpv2ConfigPortRowStatus_Type=RowStatus
_Fslldpv2ConfigPortRowStatus_Object=MibTableColumn
fslldpv2ConfigPortRowStatus=_Fslldpv2ConfigPortRowStatus_Object((1,3,6,1,4,1,2076,158,5,2,1,4),_Fslldpv2ConfigPortRowStatus_Type())
fslldpv2ConfigPortRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fslldpv2ConfigPortRowStatus.setStatus(_A)
_FslldpV2DestAddressTable_Object=MibTable
fslldpV2DestAddressTable=_FslldpV2DestAddressTable_Object((1,3,6,1,4,1,2076,158,5,3))
if mibBuilder.loadTexts:fslldpV2DestAddressTable.setStatus(_A)
_FslldpV2DestAddressTableEntry_Object=MibTableRow
fslldpV2DestAddressTableEntry=_FslldpV2DestAddressTableEntry_Object((1,3,6,1,4,1,2076,158,5,3,1))
fslldpV2DestAddressTableEntry.setIndexNames((0,_H,_o))
if mibBuilder.loadTexts:fslldpV2DestAddressTableEntry.setStatus(_A)
_FslldpV2AddressTableIndex_Type=LldpV2DestAddressTableIndex
_FslldpV2AddressTableIndex_Object=MibTableColumn
fslldpV2AddressTableIndex=_FslldpV2AddressTableIndex_Object((1,3,6,1,4,1,2076,158,5,3,1,1),_FslldpV2AddressTableIndex_Type())
fslldpV2AddressTableIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:fslldpV2AddressTableIndex.setStatus(_A)
_FslldpV2DestMacAddress_Type=MacAddress
_FslldpV2DestMacAddress_Object=MibTableColumn
fslldpV2DestMacAddress=_FslldpV2DestMacAddress_Object((1,3,6,1,4,1,2076,158,5,3,1,2),_FslldpV2DestMacAddress_Type())
fslldpV2DestMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fslldpV2DestMacAddress.setStatus(_A)
_Fslldpv2DestRowStatus_Type=RowStatus
_Fslldpv2DestRowStatus_Object=MibTableColumn
fslldpv2DestRowStatus=_Fslldpv2DestRowStatus_Object((1,3,6,1,4,1,2076,158,5,3,1,3),_Fslldpv2DestRowStatus_Type())
fslldpv2DestRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fslldpv2DestRowStatus.setStatus(_A)
_FsLldpStatsTaggedTxPortTable_Object=MibTable
fsLldpStatsTaggedTxPortTable=_FsLldpStatsTaggedTxPortTable_Object((1,3,6,1,4,1,2076,158,5,4))
if mibBuilder.loadTexts:fsLldpStatsTaggedTxPortTable.setStatus(_A)
_FsLldpStatsTaggedTxPortEntry_Object=MibTableRow
fsLldpStatsTaggedTxPortEntry=_FsLldpStatsTaggedTxPortEntry_Object((1,3,6,1,4,1,2076,158,5,4,1))
if mibBuilder.loadTexts:fsLldpStatsTaggedTxPortEntry.setStatus(_A)
_FsLldpStatsTaggedTxPortFramesTotal_Type=Counter32
_FsLldpStatsTaggedTxPortFramesTotal_Object=MibTableColumn
fsLldpStatsTaggedTxPortFramesTotal=_FsLldpStatsTaggedTxPortFramesTotal_Object((1,3,6,1,4,1,2076,158,5,4,1,1),_FsLldpStatsTaggedTxPortFramesTotal_Type())
fsLldpStatsTaggedTxPortFramesTotal.setMaxAccess(_G)
if mibBuilder.loadTexts:fsLldpStatsTaggedTxPortFramesTotal.setStatus(_A)
if mibBuilder.loadTexts:fsLldpStatsTaggedTxPortFramesTotal.setUnits('LLDP frames')
lldpLocManAddrEntry.registerAugmentions((_H,_p))
fsLldpManAddrConfigEntry.setIndexNames(*lldpLocManAddrEntry.getIndexNames())
lldpV2StatsTxPortEntry.registerAugmentions((_H,_q))
fsLldpStatsTaggedTxPortEntry.setIndexNames(*lldpV2StatsTxPortEntry.getIndexNames())
fsLldpRemTablesChange=NotificationType((1,3,6,1,4,1,2076,158,4,0,1))
fsLldpRemTablesChange.setObjects(*((_B,_d),(_B,_b),(_B,_c),(_B,_a),(_H,_r)))
if mibBuilder.loadTexts:fsLldpRemTablesChange.setStatus(_A)
fsLldpExceedsMaxFrameSize=NotificationType((1,3,6,1,4,1,2076,158,4,0,2))
fsLldpExceedsMaxFrameSize.setObjects((_B,_W))
if mibBuilder.loadTexts:fsLldpExceedsMaxFrameSize.setStatus(_A)
fsLldpDupChassisId=NotificationType((1,3,6,1,4,1,2076,158,4,0,3))
fsLldpDupChassisId.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:fsLldpDupChassisId.setStatus(_A)
fsLldpDupSystemName=NotificationType((1,3,6,1,4,1,2076,158,4,0,4))
fsLldpDupSystemName.setObjects(*((_B,_D),(_B,_E),(_B,_Z)))
if mibBuilder.loadTexts:fsLldpDupSystemName.setStatus(_A)
fsLldpDupManagmentAddress=NotificationType((1,3,6,1,4,1,2076,158,4,0,5))
fsLldpDupManagmentAddress.setObjects(*((_B,_D),(_B,_E),(_B,_Y)))
if mibBuilder.loadTexts:fsLldpDupManagmentAddress.setStatus(_A)
fsLldpMisConfigPortVlanID=NotificationType((1,3,6,1,4,1,2076,158,4,0,6))
fsLldpMisConfigPortVlanID.setObjects(*((_B,_D),(_B,_E),(_I,_O)))
if mibBuilder.loadTexts:fsLldpMisConfigPortVlanID.setStatus(_A)
fsLldpMisConfigPortProtoVlanID=NotificationType((1,3,6,1,4,1,2076,158,4,0,7))
fsLldpMisConfigPortProtoVlanID.setObjects(*((_B,_D),(_B,_E),(_I,_P)))
if mibBuilder.loadTexts:fsLldpMisConfigPortProtoVlanID.setStatus(_A)
fsLldpMisConfigVlanName=NotificationType((1,3,6,1,4,1,2076,158,4,0,8))
fsLldpMisConfigVlanName.setObjects(*((_B,_D),(_B,_E),(_I,_R)))
if mibBuilder.loadTexts:fsLldpMisConfigVlanName.setStatus(_A)
fsLldpMisConfigProtocolIdentity=NotificationType((1,3,6,1,4,1,2076,158,4,0,9))
fsLldpMisConfigProtocolIdentity.setObjects(*((_B,_D),(_B,_E),(_I,_Q)))
if mibBuilder.loadTexts:fsLldpMisConfigProtocolIdentity.setStatus(_A)
fsLldpMisConfigLinkAggStatus=NotificationType((1,3,6,1,4,1,2076,158,4,0,10))
fsLldpMisConfigLinkAggStatus.setObjects(*((_B,_D),(_B,_E),(_J,_S)))
if mibBuilder.loadTexts:fsLldpMisConfigLinkAggStatus.setStatus(_A)
fsLldpMisConfigPowerMDI=NotificationType((1,3,6,1,4,1,2076,158,4,0,11))
fsLldpMisConfigPowerMDI.setObjects(*((_B,_D),(_B,_E),(_J,_V)))
if mibBuilder.loadTexts:fsLldpMisConfigPowerMDI.setStatus(_A)
fsLldpMisConfigMaxFrameSize=NotificationType((1,3,6,1,4,1,2076,158,4,0,12))
fsLldpMisConfigMaxFrameSize.setObjects(*((_B,_D),(_B,_E),(_J,_T)))
if mibBuilder.loadTexts:fsLldpMisConfigMaxFrameSize.setStatus(_A)
fsLldpMisConfigOperMauType=NotificationType((1,3,6,1,4,1,2076,158,4,0,13))
fsLldpMisConfigOperMauType.setObjects(*((_B,_D),(_B,_E),(_J,_U)))
if mibBuilder.loadTexts:fsLldpMisConfigOperMauType.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'fslldp':fslldp,'fsLldpSystem':fsLldpSystem,'fsLldpSystemControl':fsLldpSystemControl,'fsLldpModuleStatus':fsLldpModuleStatus,'fsLldpTraceInput':fsLldpTraceInput,'fsLldpTraceOption':fsLldpTraceOption,'fsLldpTraceLevel':fsLldpTraceLevel,'fsLldpTagStatus':fsLldpTagStatus,'fsLldpConfiguredMgmtIpv4Address':fsLldpConfiguredMgmtIpv4Address,'fsLldpConfiguredMgmtIpv6Address':fsLldpConfiguredMgmtIpv6Address,'fsLldpTLV':fsLldpTLV,'fsLldpLocChassisIdSubtype':fsLldpLocChassisIdSubtype,'fsLldpLocChassisId':fsLldpLocChassisId,'fsLldpLocPortTable':fsLldpLocPortTable,'fsLldpLocPortEntry':fsLldpLocPortEntry,'fsLldpLocPortIdSubtype':fsLldpLocPortIdSubtype,'fsLldpLocPortId':fsLldpLocPortId,'fsLldpPortConfigNotificationType':fsLldpPortConfigNotificationType,'fsLldpLocPortDstMac':fsLldpLocPortDstMac,'fsLldpMedAdminStatus':fsLldpMedAdminStatus,'fsLldpManAddrConfigTable':fsLldpManAddrConfigTable,_p:fsLldpManAddrConfigEntry,'fsLldpManAddrConfigOperStatus':fsLldpManAddrConfigOperStatus,'fsLldpStatistics':fsLldpStatistics,'fsLldpMemAllocFailure':fsLldpMemAllocFailure,'fsLldpInputQOverFlows':fsLldpInputQOverFlows,_r:fsLldpStatsRemTablesUpdates,'fsLldpClearStats':fsLldpClearStats,'fsLldpNotification':fsLldpNotification,'fsLldpTraps':fsLldpTraps,'fsLldpRemTablesChange':fsLldpRemTablesChange,'fsLldpExceedsMaxFrameSize':fsLldpExceedsMaxFrameSize,'fsLldpDupChassisId':fsLldpDupChassisId,'fsLldpDupSystemName':fsLldpDupSystemName,'fsLldpDupManagmentAddress':fsLldpDupManagmentAddress,'fsLldpMisConfigPortVlanID':fsLldpMisConfigPortVlanID,'fsLldpMisConfigPortProtoVlanID':fsLldpMisConfigPortProtoVlanID,'fsLldpMisConfigVlanName':fsLldpMisConfigVlanName,'fsLldpMisConfigProtocolIdentity':fsLldpMisConfigProtocolIdentity,'fsLldpMisConfigLinkAggStatus':fsLldpMisConfigLinkAggStatus,'fsLldpMisConfigPowerMDI':fsLldpMisConfigPowerMDI,'fsLldpMisConfigMaxFrameSize':fsLldpMisConfigMaxFrameSize,'fsLldpMisConfigOperMauType':fsLldpMisConfigOperMauType,'fslldpv2Config':fslldpv2Config,'fslldpv2Version':fslldpv2Version,'fslldpv2ConfigPortMapTable':fslldpv2ConfigPortMapTable,'fslldpv2ConfigPortMapEntry':fslldpv2ConfigPortMapEntry,_m:fslldpv2ConfigPortMapIfIndex,_n:fslldpv2ConfigPortMapDestMacAddress,'fslldpv2ConfigPortMapNum':fslldpv2ConfigPortMapNum,'fslldpv2ConfigPortRowStatus':fslldpv2ConfigPortRowStatus,'fslldpV2DestAddressTable':fslldpV2DestAddressTable,'fslldpV2DestAddressTableEntry':fslldpV2DestAddressTableEntry,_o:fslldpV2AddressTableIndex,'fslldpV2DestMacAddress':fslldpV2DestMacAddress,'fslldpv2DestRowStatus':fslldpv2DestRowStatus,'fsLldpStatsTaggedTxPortTable':fsLldpStatsTaggedTxPortTable,_q:fsLldpStatsTaggedTxPortEntry,'fsLldpStatsTaggedTxPortFramesTotal':fsLldpStatsTaggedTxPortFramesTotal})