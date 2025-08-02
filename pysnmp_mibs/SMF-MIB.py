_AZ='smfNotificationsGroup'
_AY='smfNotifObjectsGroup'
_AX='smfPerfObjectsGroup'
_AW='smfStateObjectsGroup'
_AV='smfNotifDpdMemoryOverflowEvent'
_AU='smfNotifIfAdminStatusChange'
_AT='smfNotifConfiguredOpModeChange'
_AS='smfNotifAdminStatusChange'
_AR='smfNotifDpdMemoryOverflowWindow'
_AQ='smfNotifDpdMemoryOverflowThreshold'
_AP='smfPerfIpv6DpdHeaderInsertionsPerIf'
_AO='smfPerfIpv6HAVAssistsReqdPerIf'
_AN='smfPerfIpv6TTLLargerThanPreviousPerIf'
_AM='smfPerfIpv6DroppedMultiPktsTTLExceededPerIf'
_AL='smfPerfIpv6DuplMultiPktsDetectedPerIf'
_AK='smfPerfIpv6MultiPktsForwardedPerIf'
_AJ='smfPerfIpv6MultiPktsRecvPerIf'
_AI='smfPerfIpv4TTLLargerThanPreviousPerIf'
_AH='smfPerfIpv4DroppedMultiPktsTTLExceededPerIf'
_AG='smfPerfIpv4DuplMultiPktsDetectedPerIf'
_AF='smfPerfIpv4MultiPktsForwardedPerIf'
_AE='smfPerfIpv4MultiPktsRecvPerIf'
_AD='smfPerfIpv6DpdHeaderInsertionsTotal'
_AC='smfPerfIpv6HAVAssistsReqdTotal'
_AB='smfPerfIpv6TTLLargerThanPreviousTotal'
_AA='smfPerfIpv6DroppedMultiPktsTTLExceededTotal'
_A9='smfPerfIpv6DuplMultiPktsDetectedTotal'
_A8='smfPerfIpv6MultiPktsForwardedTotal'
_A7='smfPerfIpv6MultiPktsRecvTotal'
_A6='smfPerfIpv4TTLLargerThanPreviousTotal'
_A5='smfPerfIpv4DroppedMultiPktsTTLExceededTotal'
_A4='smfPerfIpv4DuplMultiPktsDetectedTotal'
_A3='smfPerfIpv4MultiPktsForwardedTotal'
_A2='smfPerfIpv4MultiPktsRecvTotal'
_A1='smfStateNeighborNextHopInterface'
_A0='smfStateNeighborRSSA'
_z='smfStateNodeRsStatusIncluded'
_y='smfCfgIfRowStatus'
_x='smfCfgIfSmfUpTime'
_w='smfCfgAddrForwardingStatus'
_v='smfCfgAddrForwardingAddrPrefixLength'
_u='smfCfgAddrForwardingAddress'
_t='smfCfgAddrForwardingAddrType'
_s='smfCfgAddrForwardingGroupName'
_r='smfCfgNhdpRssaAddrBlockTLVIncluded'
_q='smfCfgNhdpRssaMesgTLVIncluded'
_p='smfCfgDpdEntryMaxLifetime'
_o='smfCfgMaxPktLifetime'
_n='smfCfgIpv6Dpd'
_m='smfCfgIpv4Dpd'
_l='smfCfgRssaMember'
_k='smfCfgSmfSysUpTime'
_j='smfCapabilitiesRssaID'
_i='smfCapabilitiesOpModeID'
_h='smfStateNeighborPrefixLen'
_g='smfStateNeighborIpAddr'
_f='smfStateNeighborIpAddrType'
_e='smfCfgAddrForwardingIndex'
_d='Seconds'
_c='identificationBased'
_b='hashBased'
_a='smfCapabilitiesIndex'
_Z='TimeTicks'
_Y='ifName'
_X='IF-MIB'
_W='smfConfigObjectsGroup'
_V='smfCapabObjectsGroup'
_U='smfStateDpdMemoryOverflow'
_T='smfCfgIfAdminStatus'
_S='smfCfgOperationalMode'
_R='smfCfgAdminStatus'
_Q='ipv6'
_P='ipv4'
_O='SmfStatus'
_N='TruthValue'
_M='smfCfgIfIndex'
_L='InetAddressType'
_K='InetAddress'
_J='smfCfgRouterID'
_I='smfCfgRouterIDAddrType'
_H='not-accessible'
_G='read-create'
_F='Integer32'
_E='read-write'
_D='Packets'
_C='read-only'
_B='current'
_A='SMF-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IANAsmfOpModeIdTC,IANAsmfRssaIdTC=mibBuilder.importSymbols('IANA-SMF-MIB','IANAsmfOpModeIdTC','IANAsmfRssaIdTC')
InterfaceIndexOrZero,ifName=mibBuilder.importSymbols(_X,'InterfaceIndexOrZero',_Y)
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_K,'InetAddressPrefixLength',_L)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,experimental,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_Z,'Unsigned32','experimental','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_N)
smfMIB=ModuleIdentity((1,3,6,1,3,126))
if mibBuilder.loadTexts:smfMIB.setRevisions(('2014-10-10 00:00',))
class SmfStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_SmfMIBNotifications_ObjectIdentity=ObjectIdentity
smfMIBNotifications=_SmfMIBNotifications_ObjectIdentity((1,3,6,1,3,126,0))
_SmfMIBNotifObjects_ObjectIdentity=ObjectIdentity
smfMIBNotifObjects=_SmfMIBNotifObjects_ObjectIdentity((1,3,6,1,3,126,0,0))
_SmfMIBNotifControl_ObjectIdentity=ObjectIdentity
smfMIBNotifControl=_SmfMIBNotifControl_ObjectIdentity((1,3,6,1,3,126,0,1))
class _SmfNotifDpdMemoryOverflowThreshold_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SmfNotifDpdMemoryOverflowThreshold_Type.__name__=_F
_SmfNotifDpdMemoryOverflowThreshold_Object=MibScalar
smfNotifDpdMemoryOverflowThreshold=_SmfNotifDpdMemoryOverflowThreshold_Object((1,3,6,1,3,126,0,1,1),_SmfNotifDpdMemoryOverflowThreshold_Type())
smfNotifDpdMemoryOverflowThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:smfNotifDpdMemoryOverflowThreshold.setStatus(_B)
if mibBuilder.loadTexts:smfNotifDpdMemoryOverflowThreshold.setUnits('Events')
class _SmfNotifDpdMemoryOverflowWindow_Type(TimeTicks):defaultValue=1
_SmfNotifDpdMemoryOverflowWindow_Type.__name__=_Z
_SmfNotifDpdMemoryOverflowWindow_Object=MibScalar
smfNotifDpdMemoryOverflowWindow=_SmfNotifDpdMemoryOverflowWindow_Object((1,3,6,1,3,126,0,1,2),_SmfNotifDpdMemoryOverflowWindow_Type())
smfNotifDpdMemoryOverflowWindow.setMaxAccess(_E)
if mibBuilder.loadTexts:smfNotifDpdMemoryOverflowWindow.setStatus(_B)
_SmfMIBObjects_ObjectIdentity=ObjectIdentity
smfMIBObjects=_SmfMIBObjects_ObjectIdentity((1,3,6,1,3,126,1))
_SmfCapabilitiesGroup_ObjectIdentity=ObjectIdentity
smfCapabilitiesGroup=_SmfCapabilitiesGroup_ObjectIdentity((1,3,6,1,3,126,1,1))
_SmfCapabilitiesTable_Object=MibTable
smfCapabilitiesTable=_SmfCapabilitiesTable_Object((1,3,6,1,3,126,1,1,1))
if mibBuilder.loadTexts:smfCapabilitiesTable.setStatus(_B)
_SmfCapabilitiesEntry_Object=MibTableRow
smfCapabilitiesEntry=_SmfCapabilitiesEntry_Object((1,3,6,1,3,126,1,1,1,1))
smfCapabilitiesEntry.setIndexNames((0,_A,_a))
if mibBuilder.loadTexts:smfCapabilitiesEntry.setStatus(_B)
class _SmfCapabilitiesIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SmfCapabilitiesIndex_Type.__name__=_F
_SmfCapabilitiesIndex_Object=MibTableColumn
smfCapabilitiesIndex=_SmfCapabilitiesIndex_Object((1,3,6,1,3,126,1,1,1,1,1),_SmfCapabilitiesIndex_Type())
smfCapabilitiesIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:smfCapabilitiesIndex.setStatus(_B)
_SmfCapabilitiesOpModeID_Type=IANAsmfOpModeIdTC
_SmfCapabilitiesOpModeID_Object=MibTableColumn
smfCapabilitiesOpModeID=_SmfCapabilitiesOpModeID_Object((1,3,6,1,3,126,1,1,1,1,2),_SmfCapabilitiesOpModeID_Type())
smfCapabilitiesOpModeID.setMaxAccess(_C)
if mibBuilder.loadTexts:smfCapabilitiesOpModeID.setStatus(_B)
_SmfCapabilitiesRssaID_Type=IANAsmfRssaIdTC
_SmfCapabilitiesRssaID_Object=MibTableColumn
smfCapabilitiesRssaID=_SmfCapabilitiesRssaID_Object((1,3,6,1,3,126,1,1,1,1,3),_SmfCapabilitiesRssaID_Type())
smfCapabilitiesRssaID.setMaxAccess(_C)
if mibBuilder.loadTexts:smfCapabilitiesRssaID.setStatus(_B)
_SmfConfigurationGroup_ObjectIdentity=ObjectIdentity
smfConfigurationGroup=_SmfConfigurationGroup_ObjectIdentity((1,3,6,1,3,126,1,2))
class _SmfCfgAdminStatus_Type(SmfStatus):defaultValue=1
_SmfCfgAdminStatus_Type.__name__=_O
_SmfCfgAdminStatus_Object=MibScalar
smfCfgAdminStatus=_SmfCfgAdminStatus_Object((1,3,6,1,3,126,1,2,1),_SmfCfgAdminStatus_Type())
smfCfgAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:smfCfgAdminStatus.setStatus(_B)
_SmfCfgSmfSysUpTime_Type=TimeTicks
_SmfCfgSmfSysUpTime_Object=MibScalar
smfCfgSmfSysUpTime=_SmfCfgSmfSysUpTime_Object((1,3,6,1,3,126,1,2,2),_SmfCfgSmfSysUpTime_Type())
smfCfgSmfSysUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:smfCfgSmfSysUpTime.setStatus(_B)
class _SmfCfgRouterIDAddrType_Type(InetAddressType):defaultValue=1;subtypeSpec=InetAddressType.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_SmfCfgRouterIDAddrType_Type.__name__=_L
_SmfCfgRouterIDAddrType_Object=MibScalar
smfCfgRouterIDAddrType=_SmfCfgRouterIDAddrType_Object((1,3,6,1,3,126,1,2,3),_SmfCfgRouterIDAddrType_Type())
smfCfgRouterIDAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:smfCfgRouterIDAddrType.setStatus(_B)
class _SmfCfgRouterID_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_SmfCfgRouterID_Type.__name__=_K
_SmfCfgRouterID_Object=MibScalar
smfCfgRouterID=_SmfCfgRouterID_Object((1,3,6,1,3,126,1,2,4),_SmfCfgRouterID_Type())
smfCfgRouterID.setMaxAccess(_E)
if mibBuilder.loadTexts:smfCfgRouterID.setStatus(_B)
class _SmfCfgOperationalMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SmfCfgOperationalMode_Type.__name__=_F
_SmfCfgOperationalMode_Object=MibScalar
smfCfgOperationalMode=_SmfCfgOperationalMode_Object((1,3,6,1,3,126,1,2,5),_SmfCfgOperationalMode_Type())
smfCfgOperationalMode.setMaxAccess(_E)
if mibBuilder.loadTexts:smfCfgOperationalMode.setStatus(_B)
class _SmfCfgRssaMember_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('potential',1),('always',2),('never',3)))
_SmfCfgRssaMember_Type.__name__=_F
_SmfCfgRssaMember_Object=MibScalar
smfCfgRssaMember=_SmfCfgRssaMember_Object((1,3,6,1,3,126,1,2,6),_SmfCfgRssaMember_Type())
smfCfgRssaMember.setMaxAccess(_E)
if mibBuilder.loadTexts:smfCfgRssaMember.setStatus(_B)
class _SmfCfgIpv4Dpd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_b,1),(_c,2)))
_SmfCfgIpv4Dpd_Type.__name__=_F
_SmfCfgIpv4Dpd_Object=MibScalar
smfCfgIpv4Dpd=_SmfCfgIpv4Dpd_Object((1,3,6,1,3,126,1,2,7),_SmfCfgIpv4Dpd_Type())
smfCfgIpv4Dpd.setMaxAccess(_E)
if mibBuilder.loadTexts:smfCfgIpv4Dpd.setStatus(_B)
class _SmfCfgIpv6Dpd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_b,1),(_c,2)))
_SmfCfgIpv6Dpd_Type.__name__=_F
_SmfCfgIpv6Dpd_Object=MibScalar
smfCfgIpv6Dpd=_SmfCfgIpv6Dpd_Object((1,3,6,1,3,126,1,2,8),_SmfCfgIpv6Dpd_Type())
smfCfgIpv6Dpd.setMaxAccess(_E)
if mibBuilder.loadTexts:smfCfgIpv6Dpd.setStatus(_B)
class _SmfCfgMaxPktLifetime_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SmfCfgMaxPktLifetime_Type.__name__=_F
_SmfCfgMaxPktLifetime_Object=MibScalar
smfCfgMaxPktLifetime=_SmfCfgMaxPktLifetime_Object((1,3,6,1,3,126,1,2,9),_SmfCfgMaxPktLifetime_Type())
smfCfgMaxPktLifetime.setMaxAccess(_E)
if mibBuilder.loadTexts:smfCfgMaxPktLifetime.setStatus(_B)
if mibBuilder.loadTexts:smfCfgMaxPktLifetime.setUnits(_d)
class _SmfCfgDpdEntryMaxLifetime_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65525))
_SmfCfgDpdEntryMaxLifetime_Type.__name__=_F
_SmfCfgDpdEntryMaxLifetime_Object=MibScalar
smfCfgDpdEntryMaxLifetime=_SmfCfgDpdEntryMaxLifetime_Object((1,3,6,1,3,126,1,2,10),_SmfCfgDpdEntryMaxLifetime_Type())
smfCfgDpdEntryMaxLifetime.setMaxAccess(_E)
if mibBuilder.loadTexts:smfCfgDpdEntryMaxLifetime.setStatus(_B)
if mibBuilder.loadTexts:smfCfgDpdEntryMaxLifetime.setUnits(_d)
class _SmfCfgNhdpRssaMesgTLVIncluded_Type(TruthValue):defaultValue=1
_SmfCfgNhdpRssaMesgTLVIncluded_Type.__name__=_N
_SmfCfgNhdpRssaMesgTLVIncluded_Object=MibScalar
smfCfgNhdpRssaMesgTLVIncluded=_SmfCfgNhdpRssaMesgTLVIncluded_Object((1,3,6,1,3,126,1,2,11),_SmfCfgNhdpRssaMesgTLVIncluded_Type())
smfCfgNhdpRssaMesgTLVIncluded.setMaxAccess(_E)
if mibBuilder.loadTexts:smfCfgNhdpRssaMesgTLVIncluded.setStatus(_B)
class _SmfCfgNhdpRssaAddrBlockTLVIncluded_Type(TruthValue):defaultValue=1
_SmfCfgNhdpRssaAddrBlockTLVIncluded_Type.__name__=_N
_SmfCfgNhdpRssaAddrBlockTLVIncluded_Object=MibScalar
smfCfgNhdpRssaAddrBlockTLVIncluded=_SmfCfgNhdpRssaAddrBlockTLVIncluded_Object((1,3,6,1,3,126,1,2,12),_SmfCfgNhdpRssaAddrBlockTLVIncluded_Type())
smfCfgNhdpRssaAddrBlockTLVIncluded.setMaxAccess(_E)
if mibBuilder.loadTexts:smfCfgNhdpRssaAddrBlockTLVIncluded.setStatus(_B)
_SmfCfgAddrForwardingTable_Object=MibTable
smfCfgAddrForwardingTable=_SmfCfgAddrForwardingTable_Object((1,3,6,1,3,126,1,2,13))
if mibBuilder.loadTexts:smfCfgAddrForwardingTable.setStatus(_B)
_SmfCfgAddrForwardingEntry_Object=MibTableRow
smfCfgAddrForwardingEntry=_SmfCfgAddrForwardingEntry_Object((1,3,6,1,3,126,1,2,13,1))
smfCfgAddrForwardingEntry.setIndexNames((0,_A,_e))
if mibBuilder.loadTexts:smfCfgAddrForwardingEntry.setStatus(_B)
class _SmfCfgAddrForwardingIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SmfCfgAddrForwardingIndex_Type.__name__=_F
_SmfCfgAddrForwardingIndex_Object=MibTableColumn
smfCfgAddrForwardingIndex=_SmfCfgAddrForwardingIndex_Object((1,3,6,1,3,126,1,2,13,1,1),_SmfCfgAddrForwardingIndex_Type())
smfCfgAddrForwardingIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:smfCfgAddrForwardingIndex.setStatus(_B)
_SmfCfgAddrForwardingGroupName_Type=SnmpAdminString
_SmfCfgAddrForwardingGroupName_Object=MibTableColumn
smfCfgAddrForwardingGroupName=_SmfCfgAddrForwardingGroupName_Object((1,3,6,1,3,126,1,2,13,1,2),_SmfCfgAddrForwardingGroupName_Type())
smfCfgAddrForwardingGroupName.setMaxAccess(_G)
if mibBuilder.loadTexts:smfCfgAddrForwardingGroupName.setStatus(_B)
class _SmfCfgAddrForwardingAddrType_Type(InetAddressType):subtypeSpec=InetAddressType.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_SmfCfgAddrForwardingAddrType_Type.__name__=_L
_SmfCfgAddrForwardingAddrType_Object=MibTableColumn
smfCfgAddrForwardingAddrType=_SmfCfgAddrForwardingAddrType_Object((1,3,6,1,3,126,1,2,13,1,3),_SmfCfgAddrForwardingAddrType_Type())
smfCfgAddrForwardingAddrType.setMaxAccess(_G)
if mibBuilder.loadTexts:smfCfgAddrForwardingAddrType.setStatus(_B)
class _SmfCfgAddrForwardingAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_SmfCfgAddrForwardingAddress_Type.__name__=_K
_SmfCfgAddrForwardingAddress_Object=MibTableColumn
smfCfgAddrForwardingAddress=_SmfCfgAddrForwardingAddress_Object((1,3,6,1,3,126,1,2,13,1,4),_SmfCfgAddrForwardingAddress_Type())
smfCfgAddrForwardingAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:smfCfgAddrForwardingAddress.setStatus(_B)
_SmfCfgAddrForwardingAddrPrefixLength_Type=InetAddressPrefixLength
_SmfCfgAddrForwardingAddrPrefixLength_Object=MibTableColumn
smfCfgAddrForwardingAddrPrefixLength=_SmfCfgAddrForwardingAddrPrefixLength_Object((1,3,6,1,3,126,1,2,13,1,5),_SmfCfgAddrForwardingAddrPrefixLength_Type())
smfCfgAddrForwardingAddrPrefixLength.setMaxAccess(_G)
if mibBuilder.loadTexts:smfCfgAddrForwardingAddrPrefixLength.setStatus(_B)
_SmfCfgAddrForwardingStatus_Type=RowStatus
_SmfCfgAddrForwardingStatus_Object=MibTableColumn
smfCfgAddrForwardingStatus=_SmfCfgAddrForwardingStatus_Object((1,3,6,1,3,126,1,2,13,1,6),_SmfCfgAddrForwardingStatus_Type())
smfCfgAddrForwardingStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:smfCfgAddrForwardingStatus.setStatus(_B)
_SmfCfgInterfaceTable_Object=MibTable
smfCfgInterfaceTable=_SmfCfgInterfaceTable_Object((1,3,6,1,3,126,1,2,14))
if mibBuilder.loadTexts:smfCfgInterfaceTable.setStatus(_B)
_SmfCfgInterfaceEntry_Object=MibTableRow
smfCfgInterfaceEntry=_SmfCfgInterfaceEntry_Object((1,3,6,1,3,126,1,2,14,1))
smfCfgInterfaceEntry.setIndexNames((0,_A,_M))
if mibBuilder.loadTexts:smfCfgInterfaceEntry.setStatus(_B)
_SmfCfgIfIndex_Type=InterfaceIndexOrZero
_SmfCfgIfIndex_Object=MibTableColumn
smfCfgIfIndex=_SmfCfgIfIndex_Object((1,3,6,1,3,126,1,2,14,1,1),_SmfCfgIfIndex_Type())
smfCfgIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:smfCfgIfIndex.setStatus(_B)
class _SmfCfgIfAdminStatus_Type(SmfStatus):defaultValue=1
_SmfCfgIfAdminStatus_Type.__name__=_O
_SmfCfgIfAdminStatus_Object=MibTableColumn
smfCfgIfAdminStatus=_SmfCfgIfAdminStatus_Object((1,3,6,1,3,126,1,2,14,1,2),_SmfCfgIfAdminStatus_Type())
smfCfgIfAdminStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:smfCfgIfAdminStatus.setStatus(_B)
_SmfCfgIfSmfUpTime_Type=TimeTicks
_SmfCfgIfSmfUpTime_Object=MibTableColumn
smfCfgIfSmfUpTime=_SmfCfgIfSmfUpTime_Object((1,3,6,1,3,126,1,2,14,1,3),_SmfCfgIfSmfUpTime_Type())
smfCfgIfSmfUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:smfCfgIfSmfUpTime.setStatus(_B)
_SmfCfgIfRowStatus_Type=RowStatus
_SmfCfgIfRowStatus_Object=MibTableColumn
smfCfgIfRowStatus=_SmfCfgIfRowStatus_Object((1,3,6,1,3,126,1,2,14,1,4),_SmfCfgIfRowStatus_Type())
smfCfgIfRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:smfCfgIfRowStatus.setStatus(_B)
_SmfStateGroup_ObjectIdentity=ObjectIdentity
smfStateGroup=_SmfStateGroup_ObjectIdentity((1,3,6,1,3,126,1,3))
_SmfStateNodeRsStatusIncluded_Type=TruthValue
_SmfStateNodeRsStatusIncluded_Object=MibScalar
smfStateNodeRsStatusIncluded=_SmfStateNodeRsStatusIncluded_Object((1,3,6,1,3,126,1,3,1),_SmfStateNodeRsStatusIncluded_Type())
smfStateNodeRsStatusIncluded.setMaxAccess(_C)
if mibBuilder.loadTexts:smfStateNodeRsStatusIncluded.setStatus(_B)
_SmfStateDpdMemoryOverflow_Type=Counter32
_SmfStateDpdMemoryOverflow_Object=MibScalar
smfStateDpdMemoryOverflow=_SmfStateDpdMemoryOverflow_Object((1,3,6,1,3,126,1,3,2),_SmfStateDpdMemoryOverflow_Type())
smfStateDpdMemoryOverflow.setMaxAccess(_C)
if mibBuilder.loadTexts:smfStateDpdMemoryOverflow.setStatus(_B)
if mibBuilder.loadTexts:smfStateDpdMemoryOverflow.setUnits('DPD Records')
_SmfStateNeighborTable_Object=MibTable
smfStateNeighborTable=_SmfStateNeighborTable_Object((1,3,6,1,3,126,1,3,3))
if mibBuilder.loadTexts:smfStateNeighborTable.setStatus(_B)
_SmfStateNeighborEntry_Object=MibTableRow
smfStateNeighborEntry=_SmfStateNeighborEntry_Object((1,3,6,1,3,126,1,3,3,1))
smfStateNeighborEntry.setIndexNames((0,_A,_f),(0,_A,_g),(0,_A,_h))
if mibBuilder.loadTexts:smfStateNeighborEntry.setStatus(_B)
class _SmfStateNeighborIpAddrType_Type(InetAddressType):subtypeSpec=InetAddressType.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_SmfStateNeighborIpAddrType_Type.__name__=_L
_SmfStateNeighborIpAddrType_Object=MibTableColumn
smfStateNeighborIpAddrType=_SmfStateNeighborIpAddrType_Object((1,3,6,1,3,126,1,3,3,1,1),_SmfStateNeighborIpAddrType_Type())
smfStateNeighborIpAddrType.setMaxAccess(_H)
if mibBuilder.loadTexts:smfStateNeighborIpAddrType.setStatus(_B)
class _SmfStateNeighborIpAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_SmfStateNeighborIpAddr_Type.__name__=_K
_SmfStateNeighborIpAddr_Object=MibTableColumn
smfStateNeighborIpAddr=_SmfStateNeighborIpAddr_Object((1,3,6,1,3,126,1,3,3,1,2),_SmfStateNeighborIpAddr_Type())
smfStateNeighborIpAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:smfStateNeighborIpAddr.setStatus(_B)
_SmfStateNeighborPrefixLen_Type=InetAddressPrefixLength
_SmfStateNeighborPrefixLen_Object=MibTableColumn
smfStateNeighborPrefixLen=_SmfStateNeighborPrefixLen_Object((1,3,6,1,3,126,1,3,3,1,3),_SmfStateNeighborPrefixLen_Type())
smfStateNeighborPrefixLen.setMaxAccess(_H)
if mibBuilder.loadTexts:smfStateNeighborPrefixLen.setStatus(_B)
if mibBuilder.loadTexts:smfStateNeighborPrefixLen.setUnits('bits')
_SmfStateNeighborRSSA_Type=IANAsmfRssaIdTC
_SmfStateNeighborRSSA_Object=MibTableColumn
smfStateNeighborRSSA=_SmfStateNeighborRSSA_Object((1,3,6,1,3,126,1,3,3,1,4),_SmfStateNeighborRSSA_Type())
smfStateNeighborRSSA.setMaxAccess(_C)
if mibBuilder.loadTexts:smfStateNeighborRSSA.setStatus(_B)
_SmfStateNeighborNextHopInterface_Type=InterfaceIndexOrZero
_SmfStateNeighborNextHopInterface_Object=MibTableColumn
smfStateNeighborNextHopInterface=_SmfStateNeighborNextHopInterface_Object((1,3,6,1,3,126,1,3,3,1,6),_SmfStateNeighborNextHopInterface_Type())
smfStateNeighborNextHopInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:smfStateNeighborNextHopInterface.setStatus(_B)
_SmfPerformanceGroup_ObjectIdentity=ObjectIdentity
smfPerformanceGroup=_SmfPerformanceGroup_ObjectIdentity((1,3,6,1,3,126,1,4))
_SmfPerfGobalGroup_ObjectIdentity=ObjectIdentity
smfPerfGobalGroup=_SmfPerfGobalGroup_ObjectIdentity((1,3,6,1,3,126,1,4,1))
_SmfPerfIpv4MultiPktsRecvTotal_Type=Counter32
_SmfPerfIpv4MultiPktsRecvTotal_Object=MibScalar
smfPerfIpv4MultiPktsRecvTotal=_SmfPerfIpv4MultiPktsRecvTotal_Object((1,3,6,1,3,126,1,4,1,1),_SmfPerfIpv4MultiPktsRecvTotal_Type())
smfPerfIpv4MultiPktsRecvTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:smfPerfIpv4MultiPktsRecvTotal.setStatus(_B)
if mibBuilder.loadTexts:smfPerfIpv4MultiPktsRecvTotal.setUnits(_D)
_SmfPerfIpv4MultiPktsForwardedTotal_Type=Counter32
_SmfPerfIpv4MultiPktsForwardedTotal_Object=MibScalar
smfPerfIpv4MultiPktsForwardedTotal=_SmfPerfIpv4MultiPktsForwardedTotal_Object((1,3,6,1,3,126,1,4,1,2),_SmfPerfIpv4MultiPktsForwardedTotal_Type())
smfPerfIpv4MultiPktsForwardedTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:smfPerfIpv4MultiPktsForwardedTotal.setStatus(_B)
if mibBuilder.loadTexts:smfPerfIpv4MultiPktsForwardedTotal.setUnits(_D)
_SmfPerfIpv4DuplMultiPktsDetectedTotal_Type=Counter32
_SmfPerfIpv4DuplMultiPktsDetectedTotal_Object=MibScalar
smfPerfIpv4DuplMultiPktsDetectedTotal=_SmfPerfIpv4DuplMultiPktsDetectedTotal_Object((1,3,6,1,3,126,1,4,1,3),_SmfPerfIpv4DuplMultiPktsDetectedTotal_Type())
smfPerfIpv4DuplMultiPktsDetectedTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:smfPerfIpv4DuplMultiPktsDetectedTotal.setStatus(_B)
if mibBuilder.loadTexts:smfPerfIpv4DuplMultiPktsDetectedTotal.setUnits(_D)
_SmfPerfIpv4DroppedMultiPktsTTLExceededTotal_Type=Counter32
_SmfPerfIpv4DroppedMultiPktsTTLExceededTotal_Object=MibScalar
smfPerfIpv4DroppedMultiPktsTTLExceededTotal=_SmfPerfIpv4DroppedMultiPktsTTLExceededTotal_Object((1,3,6,1,3,126,1,4,1,4),_SmfPerfIpv4DroppedMultiPktsTTLExceededTotal_Type())
smfPerfIpv4DroppedMultiPktsTTLExceededTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:smfPerfIpv4DroppedMultiPktsTTLExceededTotal.setStatus(_B)
if mibBuilder.loadTexts:smfPerfIpv4DroppedMultiPktsTTLExceededTotal.setUnits(_D)
_SmfPerfIpv4TTLLargerThanPreviousTotal_Type=Counter32
_SmfPerfIpv4TTLLargerThanPreviousTotal_Object=MibScalar
smfPerfIpv4TTLLargerThanPreviousTotal=_SmfPerfIpv4TTLLargerThanPreviousTotal_Object((1,3,6,1,3,126,1,4,1,5),_SmfPerfIpv4TTLLargerThanPreviousTotal_Type())
smfPerfIpv4TTLLargerThanPreviousTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:smfPerfIpv4TTLLargerThanPreviousTotal.setStatus(_B)
if mibBuilder.loadTexts:smfPerfIpv4TTLLargerThanPreviousTotal.setUnits(_D)
_SmfPerfIpv6MultiPktsRecvTotal_Type=Counter32
_SmfPerfIpv6MultiPktsRecvTotal_Object=MibScalar
smfPerfIpv6MultiPktsRecvTotal=_SmfPerfIpv6MultiPktsRecvTotal_Object((1,3,6,1,3,126,1,4,1,6),_SmfPerfIpv6MultiPktsRecvTotal_Type())
smfPerfIpv6MultiPktsRecvTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:smfPerfIpv6MultiPktsRecvTotal.setStatus(_B)
if mibBuilder.loadTexts:smfPerfIpv6MultiPktsRecvTotal.setUnits(_D)
_SmfPerfIpv6MultiPktsForwardedTotal_Type=Counter32
_SmfPerfIpv6MultiPktsForwardedTotal_Object=MibScalar
smfPerfIpv6MultiPktsForwardedTotal=_SmfPerfIpv6MultiPktsForwardedTotal_Object((1,3,6,1,3,126,1,4,1,7),_SmfPerfIpv6MultiPktsForwardedTotal_Type())
smfPerfIpv6MultiPktsForwardedTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:smfPerfIpv6MultiPktsForwardedTotal.setStatus(_B)
if mibBuilder.loadTexts:smfPerfIpv6MultiPktsForwardedTotal.setUnits(_D)
_SmfPerfIpv6DuplMultiPktsDetectedTotal_Type=Counter32
_SmfPerfIpv6DuplMultiPktsDetectedTotal_Object=MibScalar
smfPerfIpv6DuplMultiPktsDetectedTotal=_SmfPerfIpv6DuplMultiPktsDetectedTotal_Object((1,3,6,1,3,126,1,4,1,8),_SmfPerfIpv6DuplMultiPktsDetectedTotal_Type())
smfPerfIpv6DuplMultiPktsDetectedTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:smfPerfIpv6DuplMultiPktsDetectedTotal.setStatus(_B)
if mibBuilder.loadTexts:smfPerfIpv6DuplMultiPktsDetectedTotal.setUnits(_D)
_SmfPerfIpv6DroppedMultiPktsTTLExceededTotal_Type=Counter32
_SmfPerfIpv6DroppedMultiPktsTTLExceededTotal_Object=MibScalar
smfPerfIpv6DroppedMultiPktsTTLExceededTotal=_SmfPerfIpv6DroppedMultiPktsTTLExceededTotal_Object((1,3,6,1,3,126,1,4,1,9),_SmfPerfIpv6DroppedMultiPktsTTLExceededTotal_Type())
smfPerfIpv6DroppedMultiPktsTTLExceededTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:smfPerfIpv6DroppedMultiPktsTTLExceededTotal.setStatus(_B)
if mibBuilder.loadTexts:smfPerfIpv6DroppedMultiPktsTTLExceededTotal.setUnits(_D)
_SmfPerfIpv6TTLLargerThanPreviousTotal_Type=Counter32
_SmfPerfIpv6TTLLargerThanPreviousTotal_Object=MibScalar
smfPerfIpv6TTLLargerThanPreviousTotal=_SmfPerfIpv6TTLLargerThanPreviousTotal_Object((1,3,6,1,3,126,1,4,1,10),_SmfPerfIpv6TTLLargerThanPreviousTotal_Type())
smfPerfIpv6TTLLargerThanPreviousTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:smfPerfIpv6TTLLargerThanPreviousTotal.setStatus(_B)
if mibBuilder.loadTexts:smfPerfIpv6TTLLargerThanPreviousTotal.setUnits(_D)
_SmfPerfIpv6HAVAssistsReqdTotal_Type=Counter32
_SmfPerfIpv6HAVAssistsReqdTotal_Object=MibScalar
smfPerfIpv6HAVAssistsReqdTotal=_SmfPerfIpv6HAVAssistsReqdTotal_Object((1,3,6,1,3,126,1,4,1,11),_SmfPerfIpv6HAVAssistsReqdTotal_Type())
smfPerfIpv6HAVAssistsReqdTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:smfPerfIpv6HAVAssistsReqdTotal.setStatus(_B)
if mibBuilder.loadTexts:smfPerfIpv6HAVAssistsReqdTotal.setUnits(_D)
_SmfPerfIpv6DpdHeaderInsertionsTotal_Type=Counter32
_SmfPerfIpv6DpdHeaderInsertionsTotal_Object=MibScalar
smfPerfIpv6DpdHeaderInsertionsTotal=_SmfPerfIpv6DpdHeaderInsertionsTotal_Object((1,3,6,1,3,126,1,4,1,12),_SmfPerfIpv6DpdHeaderInsertionsTotal_Type())
smfPerfIpv6DpdHeaderInsertionsTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:smfPerfIpv6DpdHeaderInsertionsTotal.setStatus(_B)
if mibBuilder.loadTexts:smfPerfIpv6DpdHeaderInsertionsTotal.setUnits(_D)
_SmfPerfInterfaceGroup_ObjectIdentity=ObjectIdentity
smfPerfInterfaceGroup=_SmfPerfInterfaceGroup_ObjectIdentity((1,3,6,1,3,126,1,4,2))
_SmfPerfIpv4InterfacePerfTable_Object=MibTable
smfPerfIpv4InterfacePerfTable=_SmfPerfIpv4InterfacePerfTable_Object((1,3,6,1,3,126,1,4,2,1))
if mibBuilder.loadTexts:smfPerfIpv4InterfacePerfTable.setStatus(_B)
_SmfPerfIpv4InterfacePerfEntry_Object=MibTableRow
smfPerfIpv4InterfacePerfEntry=_SmfPerfIpv4InterfacePerfEntry_Object((1,3,6,1,3,126,1,4,2,1,1))
smfPerfIpv4InterfacePerfEntry.setIndexNames((0,_A,_M))
if mibBuilder.loadTexts:smfPerfIpv4InterfacePerfEntry.setStatus(_B)
_SmfPerfIpv4MultiPktsRecvPerIf_Type=Counter32
_SmfPerfIpv4MultiPktsRecvPerIf_Object=MibTableColumn
smfPerfIpv4MultiPktsRecvPerIf=_SmfPerfIpv4MultiPktsRecvPerIf_Object((1,3,6,1,3,126,1,4,2,1,1,1),_SmfPerfIpv4MultiPktsRecvPerIf_Type())
smfPerfIpv4MultiPktsRecvPerIf.setMaxAccess(_C)
if mibBuilder.loadTexts:smfPerfIpv4MultiPktsRecvPerIf.setStatus(_B)
if mibBuilder.loadTexts:smfPerfIpv4MultiPktsRecvPerIf.setUnits(_D)
_SmfPerfIpv4MultiPktsForwardedPerIf_Type=Counter32
_SmfPerfIpv4MultiPktsForwardedPerIf_Object=MibTableColumn
smfPerfIpv4MultiPktsForwardedPerIf=_SmfPerfIpv4MultiPktsForwardedPerIf_Object((1,3,6,1,3,126,1,4,2,1,1,2),_SmfPerfIpv4MultiPktsForwardedPerIf_Type())
smfPerfIpv4MultiPktsForwardedPerIf.setMaxAccess(_C)
if mibBuilder.loadTexts:smfPerfIpv4MultiPktsForwardedPerIf.setStatus(_B)
if mibBuilder.loadTexts:smfPerfIpv4MultiPktsForwardedPerIf.setUnits(_D)
_SmfPerfIpv4DuplMultiPktsDetectedPerIf_Type=Counter32
_SmfPerfIpv4DuplMultiPktsDetectedPerIf_Object=MibTableColumn
smfPerfIpv4DuplMultiPktsDetectedPerIf=_SmfPerfIpv4DuplMultiPktsDetectedPerIf_Object((1,3,6,1,3,126,1,4,2,1,1,3),_SmfPerfIpv4DuplMultiPktsDetectedPerIf_Type())
smfPerfIpv4DuplMultiPktsDetectedPerIf.setMaxAccess(_C)
if mibBuilder.loadTexts:smfPerfIpv4DuplMultiPktsDetectedPerIf.setStatus(_B)
if mibBuilder.loadTexts:smfPerfIpv4DuplMultiPktsDetectedPerIf.setUnits(_D)
_SmfPerfIpv4DroppedMultiPktsTTLExceededPerIf_Type=Counter32
_SmfPerfIpv4DroppedMultiPktsTTLExceededPerIf_Object=MibTableColumn
smfPerfIpv4DroppedMultiPktsTTLExceededPerIf=_SmfPerfIpv4DroppedMultiPktsTTLExceededPerIf_Object((1,3,6,1,3,126,1,4,2,1,1,4),_SmfPerfIpv4DroppedMultiPktsTTLExceededPerIf_Type())
smfPerfIpv4DroppedMultiPktsTTLExceededPerIf.setMaxAccess(_C)
if mibBuilder.loadTexts:smfPerfIpv4DroppedMultiPktsTTLExceededPerIf.setStatus(_B)
if mibBuilder.loadTexts:smfPerfIpv4DroppedMultiPktsTTLExceededPerIf.setUnits(_D)
_SmfPerfIpv4TTLLargerThanPreviousPerIf_Type=Counter32
_SmfPerfIpv4TTLLargerThanPreviousPerIf_Object=MibTableColumn
smfPerfIpv4TTLLargerThanPreviousPerIf=_SmfPerfIpv4TTLLargerThanPreviousPerIf_Object((1,3,6,1,3,126,1,4,2,1,1,5),_SmfPerfIpv4TTLLargerThanPreviousPerIf_Type())
smfPerfIpv4TTLLargerThanPreviousPerIf.setMaxAccess(_C)
if mibBuilder.loadTexts:smfPerfIpv4TTLLargerThanPreviousPerIf.setStatus(_B)
if mibBuilder.loadTexts:smfPerfIpv4TTLLargerThanPreviousPerIf.setUnits(_D)
_SmfPerfIpv6InterfacePerfTable_Object=MibTable
smfPerfIpv6InterfacePerfTable=_SmfPerfIpv6InterfacePerfTable_Object((1,3,6,1,3,126,1,4,2,2))
if mibBuilder.loadTexts:smfPerfIpv6InterfacePerfTable.setStatus(_B)
_SmfPerfIpv6InterfacePerfEntry_Object=MibTableRow
smfPerfIpv6InterfacePerfEntry=_SmfPerfIpv6InterfacePerfEntry_Object((1,3,6,1,3,126,1,4,2,2,1))
smfPerfIpv6InterfacePerfEntry.setIndexNames((0,_A,_M))
if mibBuilder.loadTexts:smfPerfIpv6InterfacePerfEntry.setStatus(_B)
_SmfPerfIpv6MultiPktsRecvPerIf_Type=Counter32
_SmfPerfIpv6MultiPktsRecvPerIf_Object=MibTableColumn
smfPerfIpv6MultiPktsRecvPerIf=_SmfPerfIpv6MultiPktsRecvPerIf_Object((1,3,6,1,3,126,1,4,2,2,1,1),_SmfPerfIpv6MultiPktsRecvPerIf_Type())
smfPerfIpv6MultiPktsRecvPerIf.setMaxAccess(_C)
if mibBuilder.loadTexts:smfPerfIpv6MultiPktsRecvPerIf.setStatus(_B)
if mibBuilder.loadTexts:smfPerfIpv6MultiPktsRecvPerIf.setUnits(_D)
_SmfPerfIpv6MultiPktsForwardedPerIf_Type=Counter32
_SmfPerfIpv6MultiPktsForwardedPerIf_Object=MibTableColumn
smfPerfIpv6MultiPktsForwardedPerIf=_SmfPerfIpv6MultiPktsForwardedPerIf_Object((1,3,6,1,3,126,1,4,2,2,1,2),_SmfPerfIpv6MultiPktsForwardedPerIf_Type())
smfPerfIpv6MultiPktsForwardedPerIf.setMaxAccess(_C)
if mibBuilder.loadTexts:smfPerfIpv6MultiPktsForwardedPerIf.setStatus(_B)
if mibBuilder.loadTexts:smfPerfIpv6MultiPktsForwardedPerIf.setUnits(_D)
_SmfPerfIpv6DuplMultiPktsDetectedPerIf_Type=Counter32
_SmfPerfIpv6DuplMultiPktsDetectedPerIf_Object=MibTableColumn
smfPerfIpv6DuplMultiPktsDetectedPerIf=_SmfPerfIpv6DuplMultiPktsDetectedPerIf_Object((1,3,6,1,3,126,1,4,2,2,1,3),_SmfPerfIpv6DuplMultiPktsDetectedPerIf_Type())
smfPerfIpv6DuplMultiPktsDetectedPerIf.setMaxAccess(_C)
if mibBuilder.loadTexts:smfPerfIpv6DuplMultiPktsDetectedPerIf.setStatus(_B)
if mibBuilder.loadTexts:smfPerfIpv6DuplMultiPktsDetectedPerIf.setUnits(_D)
_SmfPerfIpv6DroppedMultiPktsTTLExceededPerIf_Type=Counter32
_SmfPerfIpv6DroppedMultiPktsTTLExceededPerIf_Object=MibTableColumn
smfPerfIpv6DroppedMultiPktsTTLExceededPerIf=_SmfPerfIpv6DroppedMultiPktsTTLExceededPerIf_Object((1,3,6,1,3,126,1,4,2,2,1,4),_SmfPerfIpv6DroppedMultiPktsTTLExceededPerIf_Type())
smfPerfIpv6DroppedMultiPktsTTLExceededPerIf.setMaxAccess(_C)
if mibBuilder.loadTexts:smfPerfIpv6DroppedMultiPktsTTLExceededPerIf.setStatus(_B)
if mibBuilder.loadTexts:smfPerfIpv6DroppedMultiPktsTTLExceededPerIf.setUnits(_D)
_SmfPerfIpv6TTLLargerThanPreviousPerIf_Type=Counter32
_SmfPerfIpv6TTLLargerThanPreviousPerIf_Object=MibTableColumn
smfPerfIpv6TTLLargerThanPreviousPerIf=_SmfPerfIpv6TTLLargerThanPreviousPerIf_Object((1,3,6,1,3,126,1,4,2,2,1,5),_SmfPerfIpv6TTLLargerThanPreviousPerIf_Type())
smfPerfIpv6TTLLargerThanPreviousPerIf.setMaxAccess(_C)
if mibBuilder.loadTexts:smfPerfIpv6TTLLargerThanPreviousPerIf.setStatus(_B)
if mibBuilder.loadTexts:smfPerfIpv6TTLLargerThanPreviousPerIf.setUnits(_D)
_SmfPerfIpv6HAVAssistsReqdPerIf_Type=Counter32
_SmfPerfIpv6HAVAssistsReqdPerIf_Object=MibTableColumn
smfPerfIpv6HAVAssistsReqdPerIf=_SmfPerfIpv6HAVAssistsReqdPerIf_Object((1,3,6,1,3,126,1,4,2,2,1,6),_SmfPerfIpv6HAVAssistsReqdPerIf_Type())
smfPerfIpv6HAVAssistsReqdPerIf.setMaxAccess(_C)
if mibBuilder.loadTexts:smfPerfIpv6HAVAssistsReqdPerIf.setStatus(_B)
if mibBuilder.loadTexts:smfPerfIpv6HAVAssistsReqdPerIf.setUnits(_D)
_SmfPerfIpv6DpdHeaderInsertionsPerIf_Type=Counter32
_SmfPerfIpv6DpdHeaderInsertionsPerIf_Object=MibTableColumn
smfPerfIpv6DpdHeaderInsertionsPerIf=_SmfPerfIpv6DpdHeaderInsertionsPerIf_Object((1,3,6,1,3,126,1,4,2,2,1,7),_SmfPerfIpv6DpdHeaderInsertionsPerIf_Type())
smfPerfIpv6DpdHeaderInsertionsPerIf.setMaxAccess(_C)
if mibBuilder.loadTexts:smfPerfIpv6DpdHeaderInsertionsPerIf.setStatus(_B)
if mibBuilder.loadTexts:smfPerfIpv6DpdHeaderInsertionsPerIf.setUnits(_D)
_SmfMIBConformance_ObjectIdentity=ObjectIdentity
smfMIBConformance=_SmfMIBConformance_ObjectIdentity((1,3,6,1,3,126,2))
_SmfCompliances_ObjectIdentity=ObjectIdentity
smfCompliances=_SmfCompliances_ObjectIdentity((1,3,6,1,3,126,2,1))
_SmfMIBGroups_ObjectIdentity=ObjectIdentity
smfMIBGroups=_SmfMIBGroups_ObjectIdentity((1,3,6,1,3,126,2,2))
smfCapabObjectsGroup=ObjectGroup((1,3,6,1,3,126,2,2,1))
smfCapabObjectsGroup.setObjects(*((_A,_i),(_A,_j)))
if mibBuilder.loadTexts:smfCapabObjectsGroup.setStatus(_B)
smfConfigObjectsGroup=ObjectGroup((1,3,6,1,3,126,2,2,2))
smfConfigObjectsGroup.setObjects(*((_A,_R),(_A,_k),(_A,_I),(_A,_J),(_A,_S),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_T),(_A,_x),(_A,_y)))
if mibBuilder.loadTexts:smfConfigObjectsGroup.setStatus(_B)
smfStateObjectsGroup=ObjectGroup((1,3,6,1,3,126,2,2,3))
smfStateObjectsGroup.setObjects(*((_A,_z),(_A,_U),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:smfStateObjectsGroup.setStatus(_B)
smfPerfObjectsGroup=ObjectGroup((1,3,6,1,3,126,2,2,4))
smfPerfObjectsGroup.setObjects(*((_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP)))
if mibBuilder.loadTexts:smfPerfObjectsGroup.setStatus(_B)
smfNotifObjectsGroup=ObjectGroup((1,3,6,1,3,126,2,2,5))
smfNotifObjectsGroup.setObjects(*((_A,_AQ),(_A,_AR)))
if mibBuilder.loadTexts:smfNotifObjectsGroup.setStatus(_B)
smfNotifAdminStatusChange=NotificationType((1,3,6,1,3,126,0,0,1))
smfNotifAdminStatusChange.setObjects(*((_A,_I),(_A,_J),(_A,_R)))
if mibBuilder.loadTexts:smfNotifAdminStatusChange.setStatus(_B)
smfNotifConfiguredOpModeChange=NotificationType((1,3,6,1,3,126,0,0,2))
smfNotifConfiguredOpModeChange.setObjects(*((_A,_I),(_A,_J),(_A,_S)))
if mibBuilder.loadTexts:smfNotifConfiguredOpModeChange.setStatus(_B)
smfNotifIfAdminStatusChange=NotificationType((1,3,6,1,3,126,0,0,3))
smfNotifIfAdminStatusChange.setObjects(*((_A,_I),(_A,_J),(_X,_Y),(_A,_T)))
if mibBuilder.loadTexts:smfNotifIfAdminStatusChange.setStatus(_B)
smfNotifDpdMemoryOverflowEvent=NotificationType((1,3,6,1,3,126,0,0,4))
smfNotifDpdMemoryOverflowEvent.setObjects(*((_A,_I),(_A,_J),(_A,_U)))
if mibBuilder.loadTexts:smfNotifDpdMemoryOverflowEvent.setStatus(_B)
smfNotificationsGroup=NotificationGroup((1,3,6,1,3,126,2,2,6))
smfNotificationsGroup.setObjects(*((_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV)))
if mibBuilder.loadTexts:smfNotificationsGroup.setStatus(_B)
smfBasicCompliance=ModuleCompliance((1,3,6,1,3,126,2,1,1))
smfBasicCompliance.setObjects(*((_A,_V),(_A,_W)))
if mibBuilder.loadTexts:smfBasicCompliance.setStatus(_B)
smfFullCompliance=ModuleCompliance((1,3,6,1,3,126,2,1,2))
smfFullCompliance.setObjects(*((_A,_V),(_A,_W),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ)))
if mibBuilder.loadTexts:smfFullCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_O:SmfStatus,'smfMIB':smfMIB,'smfMIBNotifications':smfMIBNotifications,'smfMIBNotifObjects':smfMIBNotifObjects,_AS:smfNotifAdminStatusChange,_AT:smfNotifConfiguredOpModeChange,_AU:smfNotifIfAdminStatusChange,_AV:smfNotifDpdMemoryOverflowEvent,'smfMIBNotifControl':smfMIBNotifControl,_AQ:smfNotifDpdMemoryOverflowThreshold,_AR:smfNotifDpdMemoryOverflowWindow,'smfMIBObjects':smfMIBObjects,'smfCapabilitiesGroup':smfCapabilitiesGroup,'smfCapabilitiesTable':smfCapabilitiesTable,'smfCapabilitiesEntry':smfCapabilitiesEntry,_a:smfCapabilitiesIndex,_i:smfCapabilitiesOpModeID,_j:smfCapabilitiesRssaID,'smfConfigurationGroup':smfConfigurationGroup,_R:smfCfgAdminStatus,_k:smfCfgSmfSysUpTime,_I:smfCfgRouterIDAddrType,_J:smfCfgRouterID,_S:smfCfgOperationalMode,_l:smfCfgRssaMember,_m:smfCfgIpv4Dpd,_n:smfCfgIpv6Dpd,_o:smfCfgMaxPktLifetime,_p:smfCfgDpdEntryMaxLifetime,_q:smfCfgNhdpRssaMesgTLVIncluded,_r:smfCfgNhdpRssaAddrBlockTLVIncluded,'smfCfgAddrForwardingTable':smfCfgAddrForwardingTable,'smfCfgAddrForwardingEntry':smfCfgAddrForwardingEntry,_e:smfCfgAddrForwardingIndex,_s:smfCfgAddrForwardingGroupName,_t:smfCfgAddrForwardingAddrType,_u:smfCfgAddrForwardingAddress,_v:smfCfgAddrForwardingAddrPrefixLength,_w:smfCfgAddrForwardingStatus,'smfCfgInterfaceTable':smfCfgInterfaceTable,'smfCfgInterfaceEntry':smfCfgInterfaceEntry,_M:smfCfgIfIndex,_T:smfCfgIfAdminStatus,_x:smfCfgIfSmfUpTime,_y:smfCfgIfRowStatus,'smfStateGroup':smfStateGroup,_z:smfStateNodeRsStatusIncluded,_U:smfStateDpdMemoryOverflow,'smfStateNeighborTable':smfStateNeighborTable,'smfStateNeighborEntry':smfStateNeighborEntry,_f:smfStateNeighborIpAddrType,_g:smfStateNeighborIpAddr,_h:smfStateNeighborPrefixLen,_A0:smfStateNeighborRSSA,_A1:smfStateNeighborNextHopInterface,'smfPerformanceGroup':smfPerformanceGroup,'smfPerfGobalGroup':smfPerfGobalGroup,_A2:smfPerfIpv4MultiPktsRecvTotal,_A3:smfPerfIpv4MultiPktsForwardedTotal,_A4:smfPerfIpv4DuplMultiPktsDetectedTotal,_A5:smfPerfIpv4DroppedMultiPktsTTLExceededTotal,_A6:smfPerfIpv4TTLLargerThanPreviousTotal,_A7:smfPerfIpv6MultiPktsRecvTotal,_A8:smfPerfIpv6MultiPktsForwardedTotal,_A9:smfPerfIpv6DuplMultiPktsDetectedTotal,_AA:smfPerfIpv6DroppedMultiPktsTTLExceededTotal,_AB:smfPerfIpv6TTLLargerThanPreviousTotal,_AC:smfPerfIpv6HAVAssistsReqdTotal,_AD:smfPerfIpv6DpdHeaderInsertionsTotal,'smfPerfInterfaceGroup':smfPerfInterfaceGroup,'smfPerfIpv4InterfacePerfTable':smfPerfIpv4InterfacePerfTable,'smfPerfIpv4InterfacePerfEntry':smfPerfIpv4InterfacePerfEntry,_AE:smfPerfIpv4MultiPktsRecvPerIf,_AF:smfPerfIpv4MultiPktsForwardedPerIf,_AG:smfPerfIpv4DuplMultiPktsDetectedPerIf,_AH:smfPerfIpv4DroppedMultiPktsTTLExceededPerIf,_AI:smfPerfIpv4TTLLargerThanPreviousPerIf,'smfPerfIpv6InterfacePerfTable':smfPerfIpv6InterfacePerfTable,'smfPerfIpv6InterfacePerfEntry':smfPerfIpv6InterfacePerfEntry,_AJ:smfPerfIpv6MultiPktsRecvPerIf,_AK:smfPerfIpv6MultiPktsForwardedPerIf,_AL:smfPerfIpv6DuplMultiPktsDetectedPerIf,_AM:smfPerfIpv6DroppedMultiPktsTTLExceededPerIf,_AN:smfPerfIpv6TTLLargerThanPreviousPerIf,_AO:smfPerfIpv6HAVAssistsReqdPerIf,_AP:smfPerfIpv6DpdHeaderInsertionsPerIf,'smfMIBConformance':smfMIBConformance,'smfCompliances':smfCompliances,'smfBasicCompliance':smfBasicCompliance,'smfFullCompliance':smfFullCompliance,'smfMIBGroups':smfMIBGroups,_V:smfCapabObjectsGroup,_W:smfConfigObjectsGroup,_AW:smfStateObjectsGroup,_AX:smfPerfObjectsGroup,_AY:smfNotifObjectsGroup,_AZ:smfNotificationsGroup})