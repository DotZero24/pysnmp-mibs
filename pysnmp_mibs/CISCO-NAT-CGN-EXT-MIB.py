_AF='cNatCgnServiceNameGroup'
_AE='cNatCgnALGCountersGroup'
_AD='cNatCgnFragmentsGroup'
_AC='cNatCgnSyslogLoggingGroup'
_AB='cNatCgnNetflowLoggingGroup'
_AA='cNatCgnSessionGroup'
_A9='cNatCgnBulkAllocGroup'
_A8='cNatCgnOptionConfigGroup'
_A7='cNatCgnNotificationsGroup'
_A6='cNatCgnCountersGroup'
_A5='cNatCgnConfigGroup'
_A4='cNatCgnNotifPortUsageWatermarkHighClear'
_A3='cNatCgnNotifPortUsageWatermarkHigh'
_A2='cNatCgnNotifPortUsageWatermarkLowClear'
_A1='cNatCgnNotifPortUsageWatermarkLow'
_A0='cNatCgnInstanceServiceName'
_z='cNatCgnALGProtocolErrors'
_y='cNatCgnALGUnsupportedErrors'
_x='cNatCgnALGMappingRemovals'
_w='cNatCgnALGMappingCreations'
_v='cNatCgnALGStatus'
_u='cNatCgnCounterFragmentPktsOutToInDrops'
_t='cNatCgnCounterFragmentPktsInToOutDrops'
_s='cNatCgnLogStatSyslogPacketDrops'
_r='cNatCgnLogStatSyslogPackets'
_q='cNatCgnLogStatNetflowPacketDrops'
_p='cNatCgnLogStatNetflowPackets'
_o='cNatCgnCounterAverageBulkPortUsage'
_n='cNatCgnInstanceProtocolPortBulkAllocControl'
_m='cNatCgnCounterSessionLimitDrops'
_l='cNatCgnCounterOutOfSessionDrops'
_k='cNatCgnCounterSessionRemovals'
_j='cNatCgnCounterSessionCreations'
_i='cNatCgnCounterTCPMappingDrops'
_h='cNatCgnCounterTCPSequenceDrops'
_g='cNatCgnCounterSourceIPOutOfRangeDrops'
_f='cNatCgnCounterNoMappingEntryDrops'
_e='cNatCgnInstanceProtocolPortLimit'
_d='cNatCgnInstancePoolingType'
_c='cNatCgnInstanceBehaviorType'
_b='cNatCgnInstanceVrf'
_a='cNatCgnInstanceInterface'
_Z='cNatCgnInstanceType'
_Y='cNatCgnCounterEntry'
_X='cNatCgnInstanceEntry'
_W='cNatCgnALGType'
_V='Gauge32'
_U='cNatCgnLogStatSessionDeleteRecords'
_T='cNatCgnLogStatSessionCreateRecords'
_S='cNatCgnLogStatMappingDeleteRecords'
_R='cNatCgnLogStatMappingCreateRecords'
_Q='cNatCgnCounterPortUsageClearHighThreshold'
_P='cNatCgnCounterPortUsageHighThreshold'
_O='cNatCgnCounterPortUsageClearLowThreshold'
_N='cNatCgnCounterPortUsageLowThreshold'
_M='cNatCgnCounterEndPointFilteringDrops'
_L='Unsigned32'
_K='natInstanceIndex'
_J='NAT-MIB'
_I='percent'
_H='SnmpAdminString'
_G='cNatCgnCounterCurrentPortAllocation'
_F='Integer32'
_E='packets'
_D='read-write'
_C='read-only'
_B='current'
_A='CISCO-NAT-CGN-EXT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
NatBehaviorType,NatPoolingType,natCountersEntry,natInstanceEntry,natInstanceIndex=mibBuilder.importSymbols(_J,'NatBehaviorType','NatPoolingType','natCountersEntry','natInstanceEntry',_K)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_V,_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoNatCgnExtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,818))
if mibBuilder.loadTexts:ciscoNatCgnExtMIB.setRevisions(('2014-04-03 00:00',))
class NatCgnInstanceType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('nat44',1),('nat64Stateful',2),('dsLite',3)))
class NatCgnALGType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*(('algActiveFTP',1),('algDNS',2),('algH323',3),('algHTTP',4),('algLDAP',5),('algMSRPC',6),('algNetBIOS',7),('algPCP',8),('algPPTP',9),('algRCMD',10),('algRTSP',11),('algSCCP',12),('algSIP',13),('algSunRPC',14)))
_CiscoNatCgnExtMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoNatCgnExtMIBNotifs=_CiscoNatCgnExtMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,818,0))
_CiscoNatCgnExtMIBObjects_ObjectIdentity=ObjectIdentity
ciscoNatCgnExtMIBObjects=_CiscoNatCgnExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,818,1))
_CNatCgnInstanceTable_Object=MibTable
cNatCgnInstanceTable=_CNatCgnInstanceTable_Object((1,3,6,1,4,1,9,9,818,1,1))
if mibBuilder.loadTexts:cNatCgnInstanceTable.setStatus(_B)
_CNatCgnInstanceEntry_Object=MibTableRow
cNatCgnInstanceEntry=_CNatCgnInstanceEntry_Object((1,3,6,1,4,1,9,9,818,1,1,1))
if mibBuilder.loadTexts:cNatCgnInstanceEntry.setStatus(_B)
_CNatCgnInstanceType_Type=NatCgnInstanceType
_CNatCgnInstanceType_Object=MibTableColumn
cNatCgnInstanceType=_CNatCgnInstanceType_Object((1,3,6,1,4,1,9,9,818,1,1,1,1),_CNatCgnInstanceType_Type())
cNatCgnInstanceType.setMaxAccess(_D)
if mibBuilder.loadTexts:cNatCgnInstanceType.setStatus(_B)
class _CNatCgnInstanceServiceName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CNatCgnInstanceServiceName_Type.__name__=_H
_CNatCgnInstanceServiceName_Object=MibTableColumn
cNatCgnInstanceServiceName=_CNatCgnInstanceServiceName_Object((1,3,6,1,4,1,9,9,818,1,1,1,2),_CNatCgnInstanceServiceName_Type())
cNatCgnInstanceServiceName.setMaxAccess(_D)
if mibBuilder.loadTexts:cNatCgnInstanceServiceName.setStatus(_B)
class _CNatCgnInstanceVrf_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CNatCgnInstanceVrf_Type.__name__=_H
_CNatCgnInstanceVrf_Object=MibTableColumn
cNatCgnInstanceVrf=_CNatCgnInstanceVrf_Object((1,3,6,1,4,1,9,9,818,1,1,1,3),_CNatCgnInstanceVrf_Type())
cNatCgnInstanceVrf.setMaxAccess(_D)
if mibBuilder.loadTexts:cNatCgnInstanceVrf.setStatus(_B)
class _CNatCgnInstanceInterface_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CNatCgnInstanceInterface_Type.__name__=_H
_CNatCgnInstanceInterface_Object=MibTableColumn
cNatCgnInstanceInterface=_CNatCgnInstanceInterface_Object((1,3,6,1,4,1,9,9,818,1,1,1,4),_CNatCgnInstanceInterface_Type())
cNatCgnInstanceInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:cNatCgnInstanceInterface.setStatus(_B)
_CNatCgnInstanceBehaviorType_Type=NatBehaviorType
_CNatCgnInstanceBehaviorType_Object=MibTableColumn
cNatCgnInstanceBehaviorType=_CNatCgnInstanceBehaviorType_Object((1,3,6,1,4,1,9,9,818,1,1,1,5),_CNatCgnInstanceBehaviorType_Type())
cNatCgnInstanceBehaviorType.setMaxAccess(_D)
if mibBuilder.loadTexts:cNatCgnInstanceBehaviorType.setStatus(_B)
_CNatCgnInstancePoolingType_Type=NatPoolingType
_CNatCgnInstancePoolingType_Object=MibTableColumn
cNatCgnInstancePoolingType=_CNatCgnInstancePoolingType_Object((1,3,6,1,4,1,9,9,818,1,1,1,6),_CNatCgnInstancePoolingType_Type())
cNatCgnInstancePoolingType.setMaxAccess(_D)
if mibBuilder.loadTexts:cNatCgnInstancePoolingType.setStatus(_B)
class _CNatCgnInstanceProtocolPortLimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CNatCgnInstanceProtocolPortLimit_Type.__name__=_L
_CNatCgnInstanceProtocolPortLimit_Object=MibTableColumn
cNatCgnInstanceProtocolPortLimit=_CNatCgnInstanceProtocolPortLimit_Object((1,3,6,1,4,1,9,9,818,1,1,1,7),_CNatCgnInstanceProtocolPortLimit_Type())
cNatCgnInstanceProtocolPortLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:cNatCgnInstanceProtocolPortLimit.setStatus(_B)
class _CNatCgnInstanceProtocolPortBulkAllocControl_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CNatCgnInstanceProtocolPortBulkAllocControl_Type.__name__=_L
_CNatCgnInstanceProtocolPortBulkAllocControl_Object=MibTableColumn
cNatCgnInstanceProtocolPortBulkAllocControl=_CNatCgnInstanceProtocolPortBulkAllocControl_Object((1,3,6,1,4,1,9,9,818,1,1,1,8),_CNatCgnInstanceProtocolPortBulkAllocControl_Type())
cNatCgnInstanceProtocolPortBulkAllocControl.setMaxAccess(_D)
if mibBuilder.loadTexts:cNatCgnInstanceProtocolPortBulkAllocControl.setStatus(_B)
_CNatCgnCounters_ObjectIdentity=ObjectIdentity
cNatCgnCounters=_CNatCgnCounters_ObjectIdentity((1,3,6,1,4,1,9,9,818,1,2))
_CNatCgnCounterTable_Object=MibTable
cNatCgnCounterTable=_CNatCgnCounterTable_Object((1,3,6,1,4,1,9,9,818,1,2,1))
if mibBuilder.loadTexts:cNatCgnCounterTable.setStatus(_B)
_CNatCgnCounterEntry_Object=MibTableRow
cNatCgnCounterEntry=_CNatCgnCounterEntry_Object((1,3,6,1,4,1,9,9,818,1,2,1,1))
if mibBuilder.loadTexts:cNatCgnCounterEntry.setStatus(_B)
_CNatCgnCounterSessionCreations_Type=Counter64
_CNatCgnCounterSessionCreations_Object=MibTableColumn
cNatCgnCounterSessionCreations=_CNatCgnCounterSessionCreations_Object((1,3,6,1,4,1,9,9,818,1,2,1,1,1),_CNatCgnCounterSessionCreations_Type())
cNatCgnCounterSessionCreations.setMaxAccess(_C)
if mibBuilder.loadTexts:cNatCgnCounterSessionCreations.setStatus(_B)
_CNatCgnCounterSessionRemovals_Type=Counter64
_CNatCgnCounterSessionRemovals_Object=MibTableColumn
cNatCgnCounterSessionRemovals=_CNatCgnCounterSessionRemovals_Object((1,3,6,1,4,1,9,9,818,1,2,1,1,2),_CNatCgnCounterSessionRemovals_Type())
cNatCgnCounterSessionRemovals.setMaxAccess(_C)
if mibBuilder.loadTexts:cNatCgnCounterSessionRemovals.setStatus(_B)
_CNatCgnCounterOutOfSessionDrops_Type=Counter64
_CNatCgnCounterOutOfSessionDrops_Object=MibTableColumn
cNatCgnCounterOutOfSessionDrops=_CNatCgnCounterOutOfSessionDrops_Object((1,3,6,1,4,1,9,9,818,1,2,1,1,3),_CNatCgnCounterOutOfSessionDrops_Type())
cNatCgnCounterOutOfSessionDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:cNatCgnCounterOutOfSessionDrops.setStatus(_B)
if mibBuilder.loadTexts:cNatCgnCounterOutOfSessionDrops.setUnits(_E)
_CNatCgnCounterSessionLimitDrops_Type=Counter64
_CNatCgnCounterSessionLimitDrops_Object=MibTableColumn
cNatCgnCounterSessionLimitDrops=_CNatCgnCounterSessionLimitDrops_Object((1,3,6,1,4,1,9,9,818,1,2,1,1,4),_CNatCgnCounterSessionLimitDrops_Type())
cNatCgnCounterSessionLimitDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:cNatCgnCounterSessionLimitDrops.setStatus(_B)
if mibBuilder.loadTexts:cNatCgnCounterSessionLimitDrops.setUnits(_E)
_CNatCgnCounterNoMappingEntryDrops_Type=Counter64
_CNatCgnCounterNoMappingEntryDrops_Object=MibTableColumn
cNatCgnCounterNoMappingEntryDrops=_CNatCgnCounterNoMappingEntryDrops_Object((1,3,6,1,4,1,9,9,818,1,2,1,1,5),_CNatCgnCounterNoMappingEntryDrops_Type())
cNatCgnCounterNoMappingEntryDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:cNatCgnCounterNoMappingEntryDrops.setStatus(_B)
if mibBuilder.loadTexts:cNatCgnCounterNoMappingEntryDrops.setUnits(_E)
_CNatCgnCounterSourceIPOutOfRangeDrops_Type=Counter64
_CNatCgnCounterSourceIPOutOfRangeDrops_Object=MibTableColumn
cNatCgnCounterSourceIPOutOfRangeDrops=_CNatCgnCounterSourceIPOutOfRangeDrops_Object((1,3,6,1,4,1,9,9,818,1,2,1,1,6),_CNatCgnCounterSourceIPOutOfRangeDrops_Type())
cNatCgnCounterSourceIPOutOfRangeDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:cNatCgnCounterSourceIPOutOfRangeDrops.setStatus(_B)
if mibBuilder.loadTexts:cNatCgnCounterSourceIPOutOfRangeDrops.setUnits(_E)
_CNatCgnCounterEndPointFilteringDrops_Type=Counter64
_CNatCgnCounterEndPointFilteringDrops_Object=MibTableColumn
cNatCgnCounterEndPointFilteringDrops=_CNatCgnCounterEndPointFilteringDrops_Object((1,3,6,1,4,1,9,9,818,1,2,1,1,7),_CNatCgnCounterEndPointFilteringDrops_Type())
cNatCgnCounterEndPointFilteringDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:cNatCgnCounterEndPointFilteringDrops.setStatus(_B)
if mibBuilder.loadTexts:cNatCgnCounterEndPointFilteringDrops.setUnits(_E)
_CNatCgnCounterTCPSequenceDrops_Type=Counter64
_CNatCgnCounterTCPSequenceDrops_Object=MibTableColumn
cNatCgnCounterTCPSequenceDrops=_CNatCgnCounterTCPSequenceDrops_Object((1,3,6,1,4,1,9,9,818,1,2,1,1,8),_CNatCgnCounterTCPSequenceDrops_Type())
cNatCgnCounterTCPSequenceDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:cNatCgnCounterTCPSequenceDrops.setStatus(_B)
if mibBuilder.loadTexts:cNatCgnCounterTCPSequenceDrops.setUnits(_E)
_CNatCgnCounterTCPMappingDrops_Type=Counter64
_CNatCgnCounterTCPMappingDrops_Object=MibTableColumn
cNatCgnCounterTCPMappingDrops=_CNatCgnCounterTCPMappingDrops_Object((1,3,6,1,4,1,9,9,818,1,2,1,1,9),_CNatCgnCounterTCPMappingDrops_Type())
cNatCgnCounterTCPMappingDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:cNatCgnCounterTCPMappingDrops.setStatus(_B)
if mibBuilder.loadTexts:cNatCgnCounterTCPMappingDrops.setUnits(_E)
_CNatCgnCounterFragmentPktsInToOutDrops_Type=Counter64
_CNatCgnCounterFragmentPktsInToOutDrops_Object=MibTableColumn
cNatCgnCounterFragmentPktsInToOutDrops=_CNatCgnCounterFragmentPktsInToOutDrops_Object((1,3,6,1,4,1,9,9,818,1,2,1,1,10),_CNatCgnCounterFragmentPktsInToOutDrops_Type())
cNatCgnCounterFragmentPktsInToOutDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:cNatCgnCounterFragmentPktsInToOutDrops.setStatus(_B)
if mibBuilder.loadTexts:cNatCgnCounterFragmentPktsInToOutDrops.setUnits(_E)
_CNatCgnCounterFragmentPktsOutToInDrops_Type=Counter64
_CNatCgnCounterFragmentPktsOutToInDrops_Object=MibTableColumn
cNatCgnCounterFragmentPktsOutToInDrops=_CNatCgnCounterFragmentPktsOutToInDrops_Object((1,3,6,1,4,1,9,9,818,1,2,1,1,11),_CNatCgnCounterFragmentPktsOutToInDrops_Type())
cNatCgnCounterFragmentPktsOutToInDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:cNatCgnCounterFragmentPktsOutToInDrops.setStatus(_B)
if mibBuilder.loadTexts:cNatCgnCounterFragmentPktsOutToInDrops.setUnits(_E)
class _CNatCgnCounterCurrentPortAllocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CNatCgnCounterCurrentPortAllocation_Type.__name__=_F
_CNatCgnCounterCurrentPortAllocation_Object=MibTableColumn
cNatCgnCounterCurrentPortAllocation=_CNatCgnCounterCurrentPortAllocation_Object((1,3,6,1,4,1,9,9,818,1,2,1,1,12),_CNatCgnCounterCurrentPortAllocation_Type())
cNatCgnCounterCurrentPortAllocation.setMaxAccess(_C)
if mibBuilder.loadTexts:cNatCgnCounterCurrentPortAllocation.setStatus(_B)
class _CNatCgnCounterPortUsageLowThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CNatCgnCounterPortUsageLowThreshold_Type.__name__=_F
_CNatCgnCounterPortUsageLowThreshold_Object=MibTableColumn
cNatCgnCounterPortUsageLowThreshold=_CNatCgnCounterPortUsageLowThreshold_Object((1,3,6,1,4,1,9,9,818,1,2,1,1,13),_CNatCgnCounterPortUsageLowThreshold_Type())
cNatCgnCounterPortUsageLowThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cNatCgnCounterPortUsageLowThreshold.setStatus(_B)
if mibBuilder.loadTexts:cNatCgnCounterPortUsageLowThreshold.setUnits(_I)
class _CNatCgnCounterPortUsageClearLowThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CNatCgnCounterPortUsageClearLowThreshold_Type.__name__=_F
_CNatCgnCounterPortUsageClearLowThreshold_Object=MibTableColumn
cNatCgnCounterPortUsageClearLowThreshold=_CNatCgnCounterPortUsageClearLowThreshold_Object((1,3,6,1,4,1,9,9,818,1,2,1,1,14),_CNatCgnCounterPortUsageClearLowThreshold_Type())
cNatCgnCounterPortUsageClearLowThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cNatCgnCounterPortUsageClearLowThreshold.setStatus(_B)
if mibBuilder.loadTexts:cNatCgnCounterPortUsageClearLowThreshold.setUnits(_I)
class _CNatCgnCounterPortUsageHighThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CNatCgnCounterPortUsageHighThreshold_Type.__name__=_F
_CNatCgnCounterPortUsageHighThreshold_Object=MibTableColumn
cNatCgnCounterPortUsageHighThreshold=_CNatCgnCounterPortUsageHighThreshold_Object((1,3,6,1,4,1,9,9,818,1,2,1,1,15),_CNatCgnCounterPortUsageHighThreshold_Type())
cNatCgnCounterPortUsageHighThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cNatCgnCounterPortUsageHighThreshold.setStatus(_B)
if mibBuilder.loadTexts:cNatCgnCounterPortUsageHighThreshold.setUnits(_I)
class _CNatCgnCounterPortUsageClearHighThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CNatCgnCounterPortUsageClearHighThreshold_Type.__name__=_F
_CNatCgnCounterPortUsageClearHighThreshold_Object=MibTableColumn
cNatCgnCounterPortUsageClearHighThreshold=_CNatCgnCounterPortUsageClearHighThreshold_Object((1,3,6,1,4,1,9,9,818,1,2,1,1,16),_CNatCgnCounterPortUsageClearHighThreshold_Type())
cNatCgnCounterPortUsageClearHighThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cNatCgnCounterPortUsageClearHighThreshold.setStatus(_B)
if mibBuilder.loadTexts:cNatCgnCounterPortUsageClearHighThreshold.setUnits(_I)
class _CNatCgnCounterAverageBulkPortUsage_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CNatCgnCounterAverageBulkPortUsage_Type.__name__=_V
_CNatCgnCounterAverageBulkPortUsage_Object=MibTableColumn
cNatCgnCounterAverageBulkPortUsage=_CNatCgnCounterAverageBulkPortUsage_Object((1,3,6,1,4,1,9,9,818,1,2,1,1,17),_CNatCgnCounterAverageBulkPortUsage_Type())
cNatCgnCounterAverageBulkPortUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cNatCgnCounterAverageBulkPortUsage.setStatus(_B)
_CNatCgnLogStatTable_Object=MibTable
cNatCgnLogStatTable=_CNatCgnLogStatTable_Object((1,3,6,1,4,1,9,9,818,1,2,2))
if mibBuilder.loadTexts:cNatCgnLogStatTable.setStatus(_B)
_CNatCgnLogStatEntry_Object=MibTableRow
cNatCgnLogStatEntry=_CNatCgnLogStatEntry_Object((1,3,6,1,4,1,9,9,818,1,2,2,1))
cNatCgnLogStatEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:cNatCgnLogStatEntry.setStatus(_B)
_CNatCgnLogStatMappingCreateRecords_Type=Counter64
_CNatCgnLogStatMappingCreateRecords_Object=MibTableColumn
cNatCgnLogStatMappingCreateRecords=_CNatCgnLogStatMappingCreateRecords_Object((1,3,6,1,4,1,9,9,818,1,2,2,1,1),_CNatCgnLogStatMappingCreateRecords_Type())
cNatCgnLogStatMappingCreateRecords.setMaxAccess(_C)
if mibBuilder.loadTexts:cNatCgnLogStatMappingCreateRecords.setStatus(_B)
_CNatCgnLogStatMappingDeleteRecords_Type=Counter64
_CNatCgnLogStatMappingDeleteRecords_Object=MibTableColumn
cNatCgnLogStatMappingDeleteRecords=_CNatCgnLogStatMappingDeleteRecords_Object((1,3,6,1,4,1,9,9,818,1,2,2,1,2),_CNatCgnLogStatMappingDeleteRecords_Type())
cNatCgnLogStatMappingDeleteRecords.setMaxAccess(_C)
if mibBuilder.loadTexts:cNatCgnLogStatMappingDeleteRecords.setStatus(_B)
_CNatCgnLogStatSessionCreateRecords_Type=Counter64
_CNatCgnLogStatSessionCreateRecords_Object=MibTableColumn
cNatCgnLogStatSessionCreateRecords=_CNatCgnLogStatSessionCreateRecords_Object((1,3,6,1,4,1,9,9,818,1,2,2,1,3),_CNatCgnLogStatSessionCreateRecords_Type())
cNatCgnLogStatSessionCreateRecords.setMaxAccess(_C)
if mibBuilder.loadTexts:cNatCgnLogStatSessionCreateRecords.setStatus(_B)
_CNatCgnLogStatSessionDeleteRecords_Type=Counter64
_CNatCgnLogStatSessionDeleteRecords_Object=MibTableColumn
cNatCgnLogStatSessionDeleteRecords=_CNatCgnLogStatSessionDeleteRecords_Object((1,3,6,1,4,1,9,9,818,1,2,2,1,4),_CNatCgnLogStatSessionDeleteRecords_Type())
cNatCgnLogStatSessionDeleteRecords.setMaxAccess(_C)
if mibBuilder.loadTexts:cNatCgnLogStatSessionDeleteRecords.setStatus(_B)
_CNatCgnLogStatNetflowPackets_Type=Counter64
_CNatCgnLogStatNetflowPackets_Object=MibTableColumn
cNatCgnLogStatNetflowPackets=_CNatCgnLogStatNetflowPackets_Object((1,3,6,1,4,1,9,9,818,1,2,2,1,5),_CNatCgnLogStatNetflowPackets_Type())
cNatCgnLogStatNetflowPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cNatCgnLogStatNetflowPackets.setStatus(_B)
_CNatCgnLogStatNetflowPacketDrops_Type=Counter64
_CNatCgnLogStatNetflowPacketDrops_Object=MibTableColumn
cNatCgnLogStatNetflowPacketDrops=_CNatCgnLogStatNetflowPacketDrops_Object((1,3,6,1,4,1,9,9,818,1,2,2,1,6),_CNatCgnLogStatNetflowPacketDrops_Type())
cNatCgnLogStatNetflowPacketDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:cNatCgnLogStatNetflowPacketDrops.setStatus(_B)
_CNatCgnLogStatSyslogPackets_Type=Counter64
_CNatCgnLogStatSyslogPackets_Object=MibTableColumn
cNatCgnLogStatSyslogPackets=_CNatCgnLogStatSyslogPackets_Object((1,3,6,1,4,1,9,9,818,1,2,2,1,7),_CNatCgnLogStatSyslogPackets_Type())
cNatCgnLogStatSyslogPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cNatCgnLogStatSyslogPackets.setStatus(_B)
_CNatCgnLogStatSyslogPacketDrops_Type=Counter64
_CNatCgnLogStatSyslogPacketDrops_Object=MibTableColumn
cNatCgnLogStatSyslogPacketDrops=_CNatCgnLogStatSyslogPacketDrops_Object((1,3,6,1,4,1,9,9,818,1,2,2,1,8),_CNatCgnLogStatSyslogPacketDrops_Type())
cNatCgnLogStatSyslogPacketDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:cNatCgnLogStatSyslogPacketDrops.setStatus(_B)
_CNatCgnALGCountersTable_Object=MibTable
cNatCgnALGCountersTable=_CNatCgnALGCountersTable_Object((1,3,6,1,4,1,9,9,818,1,2,3))
if mibBuilder.loadTexts:cNatCgnALGCountersTable.setStatus(_B)
_CNatCgnALGCountersEntry_Object=MibTableRow
cNatCgnALGCountersEntry=_CNatCgnALGCountersEntry_Object((1,3,6,1,4,1,9,9,818,1,2,3,1))
cNatCgnALGCountersEntry.setIndexNames((0,_J,_K),(0,_A,_W))
if mibBuilder.loadTexts:cNatCgnALGCountersEntry.setStatus(_B)
_CNatCgnALGType_Type=NatCgnALGType
_CNatCgnALGType_Object=MibTableColumn
cNatCgnALGType=_CNatCgnALGType_Object((1,3,6,1,4,1,9,9,818,1,2,3,1,1),_CNatCgnALGType_Type())
cNatCgnALGType.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cNatCgnALGType.setStatus(_B)
class _CNatCgnALGStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notApplicable',1),('unSupported',2),('notEnabled',3),('enabled',4)))
_CNatCgnALGStatus_Type.__name__=_F
_CNatCgnALGStatus_Object=MibTableColumn
cNatCgnALGStatus=_CNatCgnALGStatus_Object((1,3,6,1,4,1,9,9,818,1,2,3,1,2),_CNatCgnALGStatus_Type())
cNatCgnALGStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cNatCgnALGStatus.setStatus(_B)
_CNatCgnALGMappingCreations_Type=Counter64
_CNatCgnALGMappingCreations_Object=MibTableColumn
cNatCgnALGMappingCreations=_CNatCgnALGMappingCreations_Object((1,3,6,1,4,1,9,9,818,1,2,3,1,3),_CNatCgnALGMappingCreations_Type())
cNatCgnALGMappingCreations.setMaxAccess(_C)
if mibBuilder.loadTexts:cNatCgnALGMappingCreations.setStatus(_B)
_CNatCgnALGMappingRemovals_Type=Counter64
_CNatCgnALGMappingRemovals_Object=MibTableColumn
cNatCgnALGMappingRemovals=_CNatCgnALGMappingRemovals_Object((1,3,6,1,4,1,9,9,818,1,2,3,1,4),_CNatCgnALGMappingRemovals_Type())
cNatCgnALGMappingRemovals.setMaxAccess(_C)
if mibBuilder.loadTexts:cNatCgnALGMappingRemovals.setStatus(_B)
_CNatCgnALGUnsupportedErrors_Type=Counter64
_CNatCgnALGUnsupportedErrors_Object=MibTableColumn
cNatCgnALGUnsupportedErrors=_CNatCgnALGUnsupportedErrors_Object((1,3,6,1,4,1,9,9,818,1,2,3,1,5),_CNatCgnALGUnsupportedErrors_Type())
cNatCgnALGUnsupportedErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cNatCgnALGUnsupportedErrors.setStatus(_B)
_CNatCgnALGProtocolErrors_Type=Counter64
_CNatCgnALGProtocolErrors_Object=MibTableColumn
cNatCgnALGProtocolErrors=_CNatCgnALGProtocolErrors_Object((1,3,6,1,4,1,9,9,818,1,2,3,1,6),_CNatCgnALGProtocolErrors_Type())
cNatCgnALGProtocolErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cNatCgnALGProtocolErrors.setStatus(_B)
_CiscoNatCgnExtMIBConform_ObjectIdentity=ObjectIdentity
ciscoNatCgnExtMIBConform=_CiscoNatCgnExtMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,818,2))
_CNatCgnMIBCompliances_ObjectIdentity=ObjectIdentity
cNatCgnMIBCompliances=_CNatCgnMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,818,2,1))
_CNatCgnMIBGroups_ObjectIdentity=ObjectIdentity
cNatCgnMIBGroups=_CNatCgnMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,818,2,2))
natInstanceEntry.registerAugmentions((_A,_X))
cNatCgnInstanceEntry.setIndexNames(*natInstanceEntry.getIndexNames())
natCountersEntry.registerAugmentions((_A,_Y))
cNatCgnCounterEntry.setIndexNames(*natCountersEntry.getIndexNames())
cNatCgnConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,818,2,2,1))
cNatCgnConfigGroup.setObjects(*((_A,_Z),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:cNatCgnConfigGroup.setStatus(_B)
cNatCgnOptionConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,818,2,2,2))
cNatCgnOptionConfigGroup.setObjects(*((_A,_c),(_A,_d),(_A,_e)))
if mibBuilder.loadTexts:cNatCgnOptionConfigGroup.setStatus(_B)
cNatCgnCountersGroup=ObjectGroup((1,3,6,1,4,1,9,9,818,2,2,3))
cNatCgnCountersGroup.setObjects(*((_A,_f),(_A,_g),(_A,_M),(_A,_h),(_A,_i),(_A,_G),(_A,_N),(_A,_O),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:cNatCgnCountersGroup.setStatus(_B)
cNatCgnSessionGroup=ObjectGroup((1,3,6,1,4,1,9,9,818,2,2,4))
cNatCgnSessionGroup.setObjects(*((_A,_j),(_A,_k),(_A,_l),(_A,_M),(_A,_m)))
if mibBuilder.loadTexts:cNatCgnSessionGroup.setStatus(_B)
cNatCgnBulkAllocGroup=ObjectGroup((1,3,6,1,4,1,9,9,818,2,2,5))
cNatCgnBulkAllocGroup.setObjects(*((_A,_n),(_A,_o)))
if mibBuilder.loadTexts:cNatCgnBulkAllocGroup.setStatus(_B)
cNatCgnNetflowLoggingGroup=ObjectGroup((1,3,6,1,4,1,9,9,818,2,2,6))
cNatCgnNetflowLoggingGroup.setObjects(*((_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_p),(_A,_q)))
if mibBuilder.loadTexts:cNatCgnNetflowLoggingGroup.setStatus(_B)
cNatCgnSyslogLoggingGroup=ObjectGroup((1,3,6,1,4,1,9,9,818,2,2,7))
cNatCgnSyslogLoggingGroup.setObjects(*((_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:cNatCgnSyslogLoggingGroup.setStatus(_B)
cNatCgnFragmentsGroup=ObjectGroup((1,3,6,1,4,1,9,9,818,2,2,8))
cNatCgnFragmentsGroup.setObjects(*((_A,_t),(_A,_u)))
if mibBuilder.loadTexts:cNatCgnFragmentsGroup.setStatus(_B)
cNatCgnALGCountersGroup=ObjectGroup((1,3,6,1,4,1,9,9,818,2,2,9))
cNatCgnALGCountersGroup.setObjects(*((_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z)))
if mibBuilder.loadTexts:cNatCgnALGCountersGroup.setStatus(_B)
cNatCgnServiceNameGroup=ObjectGroup((1,3,6,1,4,1,9,9,818,2,2,11))
cNatCgnServiceNameGroup.setObjects((_A,_A0))
if mibBuilder.loadTexts:cNatCgnServiceNameGroup.setStatus(_B)
cNatCgnNotifPortUsageWatermarkLow=NotificationType((1,3,6,1,4,1,9,9,818,0,1))
cNatCgnNotifPortUsageWatermarkLow.setObjects(*((_A,_G),(_A,_N)))
if mibBuilder.loadTexts:cNatCgnNotifPortUsageWatermarkLow.setStatus(_B)
cNatCgnNotifPortUsageWatermarkLowClear=NotificationType((1,3,6,1,4,1,9,9,818,0,2))
cNatCgnNotifPortUsageWatermarkLowClear.setObjects(*((_A,_G),(_A,_O)))
if mibBuilder.loadTexts:cNatCgnNotifPortUsageWatermarkLowClear.setStatus(_B)
cNatCgnNotifPortUsageWatermarkHigh=NotificationType((1,3,6,1,4,1,9,9,818,0,3))
cNatCgnNotifPortUsageWatermarkHigh.setObjects(*((_A,_G),(_A,_P)))
if mibBuilder.loadTexts:cNatCgnNotifPortUsageWatermarkHigh.setStatus(_B)
cNatCgnNotifPortUsageWatermarkHighClear=NotificationType((1,3,6,1,4,1,9,9,818,0,4))
cNatCgnNotifPortUsageWatermarkHighClear.setObjects(*((_A,_G),(_A,_Q)))
if mibBuilder.loadTexts:cNatCgnNotifPortUsageWatermarkHighClear.setStatus(_B)
cNatCgnNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,9,818,2,2,15))
cNatCgnNotificationsGroup.setObjects(*((_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4)))
if mibBuilder.loadTexts:cNatCgnNotificationsGroup.setStatus(_B)
cNatCgnModuleCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,818,2,1,1))
cNatCgnModuleCompliance.setObjects(*((_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF)))
if mibBuilder.loadTexts:cNatCgnModuleCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'NatCgnInstanceType':NatCgnInstanceType,'NatCgnALGType':NatCgnALGType,'ciscoNatCgnExtMIB':ciscoNatCgnExtMIB,'ciscoNatCgnExtMIBNotifs':ciscoNatCgnExtMIBNotifs,_A1:cNatCgnNotifPortUsageWatermarkLow,_A2:cNatCgnNotifPortUsageWatermarkLowClear,_A3:cNatCgnNotifPortUsageWatermarkHigh,_A4:cNatCgnNotifPortUsageWatermarkHighClear,'ciscoNatCgnExtMIBObjects':ciscoNatCgnExtMIBObjects,'cNatCgnInstanceTable':cNatCgnInstanceTable,_X:cNatCgnInstanceEntry,_Z:cNatCgnInstanceType,_A0:cNatCgnInstanceServiceName,_b:cNatCgnInstanceVrf,_a:cNatCgnInstanceInterface,_c:cNatCgnInstanceBehaviorType,_d:cNatCgnInstancePoolingType,_e:cNatCgnInstanceProtocolPortLimit,_n:cNatCgnInstanceProtocolPortBulkAllocControl,'cNatCgnCounters':cNatCgnCounters,'cNatCgnCounterTable':cNatCgnCounterTable,_Y:cNatCgnCounterEntry,_j:cNatCgnCounterSessionCreations,_k:cNatCgnCounterSessionRemovals,_l:cNatCgnCounterOutOfSessionDrops,_m:cNatCgnCounterSessionLimitDrops,_f:cNatCgnCounterNoMappingEntryDrops,_g:cNatCgnCounterSourceIPOutOfRangeDrops,_M:cNatCgnCounterEndPointFilteringDrops,_h:cNatCgnCounterTCPSequenceDrops,_i:cNatCgnCounterTCPMappingDrops,_t:cNatCgnCounterFragmentPktsInToOutDrops,_u:cNatCgnCounterFragmentPktsOutToInDrops,_G:cNatCgnCounterCurrentPortAllocation,_N:cNatCgnCounterPortUsageLowThreshold,_O:cNatCgnCounterPortUsageClearLowThreshold,_P:cNatCgnCounterPortUsageHighThreshold,_Q:cNatCgnCounterPortUsageClearHighThreshold,_o:cNatCgnCounterAverageBulkPortUsage,'cNatCgnLogStatTable':cNatCgnLogStatTable,'cNatCgnLogStatEntry':cNatCgnLogStatEntry,_R:cNatCgnLogStatMappingCreateRecords,_S:cNatCgnLogStatMappingDeleteRecords,_T:cNatCgnLogStatSessionCreateRecords,_U:cNatCgnLogStatSessionDeleteRecords,_p:cNatCgnLogStatNetflowPackets,_q:cNatCgnLogStatNetflowPacketDrops,_r:cNatCgnLogStatSyslogPackets,_s:cNatCgnLogStatSyslogPacketDrops,'cNatCgnALGCountersTable':cNatCgnALGCountersTable,'cNatCgnALGCountersEntry':cNatCgnALGCountersEntry,_W:cNatCgnALGType,_v:cNatCgnALGStatus,_w:cNatCgnALGMappingCreations,_x:cNatCgnALGMappingRemovals,_y:cNatCgnALGUnsupportedErrors,_z:cNatCgnALGProtocolErrors,'ciscoNatCgnExtMIBConform':ciscoNatCgnExtMIBConform,'cNatCgnMIBCompliances':cNatCgnMIBCompliances,'cNatCgnModuleCompliance':cNatCgnModuleCompliance,'cNatCgnMIBGroups':cNatCgnMIBGroups,_A5:cNatCgnConfigGroup,_A8:cNatCgnOptionConfigGroup,_A6:cNatCgnCountersGroup,_AA:cNatCgnSessionGroup,_A9:cNatCgnBulkAllocGroup,_AB:cNatCgnNetflowLoggingGroup,_AC:cNatCgnSyslogLoggingGroup,_AD:cNatCgnFragmentsGroup,_AE:cNatCgnALGCountersGroup,_AF:cNatCgnServiceNameGroup,_A7:cNatCgnNotificationsGroup})