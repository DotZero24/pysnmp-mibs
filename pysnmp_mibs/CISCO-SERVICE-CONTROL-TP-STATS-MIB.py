_k='cscTpCounterDiscontinuityGroup'
_j='cscTpStatsMIBTrafficCntrsObjGroup'
_i='cscTpStatsMIBObjectGroup'
_h='cscTpCounterDiscontinuityTime'
_g='cscTpStatsTrafficCounterType'
_f='cscTpStatsTrafficCounterName'
_e='cscTpStatsTrafficCounterValue'
_d='cscTpServiceLoss'
_c='cscTpFlowsCapacityUtilization'
_b='cscTpHandledFlowsRate'
_a='cscTpHandledPacketsRate'
_Z='cscTpTotalTcpUdpChksumErrPackets'
_Y='cscTpTotalTTLErrPackets'
_X='cscTpTotalIpBroadcastPackets'
_W='cscTpTotalIpLengthErrPackets'
_V='cscTpTotalIpChecksumErrPackets'
_U='cscTpTotalNonIpPackets'
_T='cscTpTotalFragments'
_S='cscTpTotalWredDiscardedPackets'
_R='cscTpTotalBandwidthDiscardedPackets'
_Q='cscTpTotalBlockedFlows'
_P='cscTpTotalBlockedPackets'
_O='cscTpUdpActiveFlows'
_N='cscTpTcpActiveFlows'
_M='cscTpActiveFlows'
_L='cscTpTotalHandledFlows'
_K='cscTpTotalHandledPackets'
_J='cscTpStatsTrafficCounterIndex'
_I='Integer32'
_H='entPhysicalIndex'
_G='ENTITY-MIB'
_F='Unsigned32'
_E='flows'
_D='packets'
_C='read-only'
_B='CISCO-SERVICE-CONTROL-TP-STATS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
entPhysicalIndex,=mibBuilder.importSymbols(_G,_H)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
ciscoServiceControlTpStatsMIB=ModuleIdentity((1,3,6,1,4,1,9,9,634))
if mibBuilder.loadTexts:ciscoServiceControlTpStatsMIB.setRevisions(('2007-07-22 00:00',))
_CiscoSCTpStatsMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoSCTpStatsMIBNotifs=_CiscoSCTpStatsMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,634,0))
_CiscoSCTpStatsMIBObjects_ObjectIdentity=ObjectIdentity
ciscoSCTpStatsMIBObjects=_CiscoSCTpStatsMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,634,1))
_CscTpTable_Object=MibTable
cscTpTable=_CscTpTable_Object((1,3,6,1,4,1,9,9,634,1,1))
if mibBuilder.loadTexts:cscTpTable.setStatus(_A)
_CscTpEntry_Object=MibTableRow
cscTpEntry=_CscTpEntry_Object((1,3,6,1,4,1,9,9,634,1,1,1))
cscTpEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cscTpEntry.setStatus(_A)
_CscTpTotalHandledPackets_Type=Counter64
_CscTpTotalHandledPackets_Object=MibTableColumn
cscTpTotalHandledPackets=_CscTpTotalHandledPackets_Object((1,3,6,1,4,1,9,9,634,1,1,1,1),_CscTpTotalHandledPackets_Type())
cscTpTotalHandledPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cscTpTotalHandledPackets.setStatus(_A)
if mibBuilder.loadTexts:cscTpTotalHandledPackets.setUnits(_D)
_CscTpTotalHandledFlows_Type=Counter64
_CscTpTotalHandledFlows_Object=MibTableColumn
cscTpTotalHandledFlows=_CscTpTotalHandledFlows_Object((1,3,6,1,4,1,9,9,634,1,1,1,2),_CscTpTotalHandledFlows_Type())
cscTpTotalHandledFlows.setMaxAccess(_C)
if mibBuilder.loadTexts:cscTpTotalHandledFlows.setStatus(_A)
if mibBuilder.loadTexts:cscTpTotalHandledFlows.setUnits(_E)
_CscTpActiveFlows_Type=Gauge32
_CscTpActiveFlows_Object=MibTableColumn
cscTpActiveFlows=_CscTpActiveFlows_Object((1,3,6,1,4,1,9,9,634,1,1,1,3),_CscTpActiveFlows_Type())
cscTpActiveFlows.setMaxAccess(_C)
if mibBuilder.loadTexts:cscTpActiveFlows.setStatus(_A)
if mibBuilder.loadTexts:cscTpActiveFlows.setUnits(_E)
_CscTpTcpActiveFlows_Type=Gauge32
_CscTpTcpActiveFlows_Object=MibTableColumn
cscTpTcpActiveFlows=_CscTpTcpActiveFlows_Object((1,3,6,1,4,1,9,9,634,1,1,1,4),_CscTpTcpActiveFlows_Type())
cscTpTcpActiveFlows.setMaxAccess(_C)
if mibBuilder.loadTexts:cscTpTcpActiveFlows.setStatus(_A)
if mibBuilder.loadTexts:cscTpTcpActiveFlows.setUnits(_E)
_CscTpUdpActiveFlows_Type=Gauge32
_CscTpUdpActiveFlows_Object=MibTableColumn
cscTpUdpActiveFlows=_CscTpUdpActiveFlows_Object((1,3,6,1,4,1,9,9,634,1,1,1,5),_CscTpUdpActiveFlows_Type())
cscTpUdpActiveFlows.setMaxAccess(_C)
if mibBuilder.loadTexts:cscTpUdpActiveFlows.setStatus(_A)
if mibBuilder.loadTexts:cscTpUdpActiveFlows.setUnits(_E)
_CscTpTotalBlockedPackets_Type=Counter32
_CscTpTotalBlockedPackets_Object=MibTableColumn
cscTpTotalBlockedPackets=_CscTpTotalBlockedPackets_Object((1,3,6,1,4,1,9,9,634,1,1,1,6),_CscTpTotalBlockedPackets_Type())
cscTpTotalBlockedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cscTpTotalBlockedPackets.setStatus(_A)
if mibBuilder.loadTexts:cscTpTotalBlockedPackets.setUnits(_D)
_CscTpTotalBlockedFlows_Type=Counter32
_CscTpTotalBlockedFlows_Object=MibTableColumn
cscTpTotalBlockedFlows=_CscTpTotalBlockedFlows_Object((1,3,6,1,4,1,9,9,634,1,1,1,7),_CscTpTotalBlockedFlows_Type())
cscTpTotalBlockedFlows.setMaxAccess(_C)
if mibBuilder.loadTexts:cscTpTotalBlockedFlows.setStatus(_A)
if mibBuilder.loadTexts:cscTpTotalBlockedFlows.setUnits(_E)
_CscTpTotalBandwidthDiscardedPackets_Type=Counter32
_CscTpTotalBandwidthDiscardedPackets_Object=MibTableColumn
cscTpTotalBandwidthDiscardedPackets=_CscTpTotalBandwidthDiscardedPackets_Object((1,3,6,1,4,1,9,9,634,1,1,1,8),_CscTpTotalBandwidthDiscardedPackets_Type())
cscTpTotalBandwidthDiscardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cscTpTotalBandwidthDiscardedPackets.setStatus(_A)
if mibBuilder.loadTexts:cscTpTotalBandwidthDiscardedPackets.setUnits(_D)
_CscTpTotalWredDiscardedPackets_Type=Counter32
_CscTpTotalWredDiscardedPackets_Object=MibTableColumn
cscTpTotalWredDiscardedPackets=_CscTpTotalWredDiscardedPackets_Object((1,3,6,1,4,1,9,9,634,1,1,1,9),_CscTpTotalWredDiscardedPackets_Type())
cscTpTotalWredDiscardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cscTpTotalWredDiscardedPackets.setStatus(_A)
if mibBuilder.loadTexts:cscTpTotalWredDiscardedPackets.setUnits(_D)
_CscTpTotalFragments_Type=Counter64
_CscTpTotalFragments_Object=MibTableColumn
cscTpTotalFragments=_CscTpTotalFragments_Object((1,3,6,1,4,1,9,9,634,1,1,1,10),_CscTpTotalFragments_Type())
cscTpTotalFragments.setMaxAccess(_C)
if mibBuilder.loadTexts:cscTpTotalFragments.setStatus(_A)
if mibBuilder.loadTexts:cscTpTotalFragments.setUnits(_D)
_CscTpTotalNonIpPackets_Type=Counter64
_CscTpTotalNonIpPackets_Object=MibTableColumn
cscTpTotalNonIpPackets=_CscTpTotalNonIpPackets_Object((1,3,6,1,4,1,9,9,634,1,1,1,11),_CscTpTotalNonIpPackets_Type())
cscTpTotalNonIpPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cscTpTotalNonIpPackets.setStatus(_A)
if mibBuilder.loadTexts:cscTpTotalNonIpPackets.setUnits(_D)
_CscTpTotalIpChecksumErrPackets_Type=Counter32
_CscTpTotalIpChecksumErrPackets_Object=MibTableColumn
cscTpTotalIpChecksumErrPackets=_CscTpTotalIpChecksumErrPackets_Object((1,3,6,1,4,1,9,9,634,1,1,1,12),_CscTpTotalIpChecksumErrPackets_Type())
cscTpTotalIpChecksumErrPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cscTpTotalIpChecksumErrPackets.setStatus(_A)
if mibBuilder.loadTexts:cscTpTotalIpChecksumErrPackets.setUnits('num-of-packets')
_CscTpTotalIpLengthErrPackets_Type=Counter32
_CscTpTotalIpLengthErrPackets_Object=MibTableColumn
cscTpTotalIpLengthErrPackets=_CscTpTotalIpLengthErrPackets_Object((1,3,6,1,4,1,9,9,634,1,1,1,13),_CscTpTotalIpLengthErrPackets_Type())
cscTpTotalIpLengthErrPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cscTpTotalIpLengthErrPackets.setStatus(_A)
if mibBuilder.loadTexts:cscTpTotalIpLengthErrPackets.setUnits(_D)
_CscTpTotalIpBroadcastPackets_Type=Counter64
_CscTpTotalIpBroadcastPackets_Object=MibTableColumn
cscTpTotalIpBroadcastPackets=_CscTpTotalIpBroadcastPackets_Object((1,3,6,1,4,1,9,9,634,1,1,1,14),_CscTpTotalIpBroadcastPackets_Type())
cscTpTotalIpBroadcastPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cscTpTotalIpBroadcastPackets.setStatus(_A)
if mibBuilder.loadTexts:cscTpTotalIpBroadcastPackets.setUnits(_D)
_CscTpTotalTTLErrPackets_Type=Counter32
_CscTpTotalTTLErrPackets_Object=MibTableColumn
cscTpTotalTTLErrPackets=_CscTpTotalTTLErrPackets_Object((1,3,6,1,4,1,9,9,634,1,1,1,15),_CscTpTotalTTLErrPackets_Type())
cscTpTotalTTLErrPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cscTpTotalTTLErrPackets.setStatus(_A)
if mibBuilder.loadTexts:cscTpTotalTTLErrPackets.setUnits(_D)
_CscTpTotalTcpUdpChksumErrPackets_Type=Counter32
_CscTpTotalTcpUdpChksumErrPackets_Object=MibTableColumn
cscTpTotalTcpUdpChksumErrPackets=_CscTpTotalTcpUdpChksumErrPackets_Object((1,3,6,1,4,1,9,9,634,1,1,1,16),_CscTpTotalTcpUdpChksumErrPackets_Type())
cscTpTotalTcpUdpChksumErrPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cscTpTotalTcpUdpChksumErrPackets.setStatus(_A)
if mibBuilder.loadTexts:cscTpTotalTcpUdpChksumErrPackets.setUnits(_D)
_CscTpHandledPacketsRate_Type=Gauge32
_CscTpHandledPacketsRate_Object=MibTableColumn
cscTpHandledPacketsRate=_CscTpHandledPacketsRate_Object((1,3,6,1,4,1,9,9,634,1,1,1,17),_CscTpHandledPacketsRate_Type())
cscTpHandledPacketsRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cscTpHandledPacketsRate.setStatus(_A)
if mibBuilder.loadTexts:cscTpHandledPacketsRate.setUnits('packets per second')
_CscTpHandledFlowsRate_Type=Gauge32
_CscTpHandledFlowsRate_Object=MibTableColumn
cscTpHandledFlowsRate=_CscTpHandledFlowsRate_Object((1,3,6,1,4,1,9,9,634,1,1,1,18),_CscTpHandledFlowsRate_Type())
cscTpHandledFlowsRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cscTpHandledFlowsRate.setStatus(_A)
if mibBuilder.loadTexts:cscTpHandledFlowsRate.setUnits('flows per second')
class _CscTpFlowsCapacityUtilization_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CscTpFlowsCapacityUtilization_Type.__name__=_F
_CscTpFlowsCapacityUtilization_Object=MibTableColumn
cscTpFlowsCapacityUtilization=_CscTpFlowsCapacityUtilization_Object((1,3,6,1,4,1,9,9,634,1,1,1,19),_CscTpFlowsCapacityUtilization_Type())
cscTpFlowsCapacityUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:cscTpFlowsCapacityUtilization.setStatus(_A)
if mibBuilder.loadTexts:cscTpFlowsCapacityUtilization.setUnits('percent')
class _CscTpServiceLoss_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_CscTpServiceLoss_Type.__name__=_F
_CscTpServiceLoss_Object=MibTableColumn
cscTpServiceLoss=_CscTpServiceLoss_Object((1,3,6,1,4,1,9,9,634,1,1,1,20),_CscTpServiceLoss_Type())
cscTpServiceLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:cscTpServiceLoss.setStatus(_A)
if mibBuilder.loadTexts:cscTpServiceLoss.setUnits('0.001 percent')
_CscTpStatsTrafficCountersTable_Object=MibTable
cscTpStatsTrafficCountersTable=_CscTpStatsTrafficCountersTable_Object((1,3,6,1,4,1,9,9,634,1,2))
if mibBuilder.loadTexts:cscTpStatsTrafficCountersTable.setStatus(_A)
_CscTpStatsTrafficCountersEntry_Object=MibTableRow
cscTpStatsTrafficCountersEntry=_CscTpStatsTrafficCountersEntry_Object((1,3,6,1,4,1,9,9,634,1,2,1))
cscTpStatsTrafficCountersEntry.setIndexNames((0,_G,_H),(0,_B,_J))
if mibBuilder.loadTexts:cscTpStatsTrafficCountersEntry.setStatus(_A)
class _CscTpStatsTrafficCounterIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CscTpStatsTrafficCounterIndex_Type.__name__=_F
_CscTpStatsTrafficCounterIndex_Object=MibTableColumn
cscTpStatsTrafficCounterIndex=_CscTpStatsTrafficCounterIndex_Object((1,3,6,1,4,1,9,9,634,1,2,1,1),_CscTpStatsTrafficCounterIndex_Type())
cscTpStatsTrafficCounterIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cscTpStatsTrafficCounterIndex.setStatus(_A)
_CscTpStatsTrafficCounterName_Type=SnmpAdminString
_CscTpStatsTrafficCounterName_Object=MibTableColumn
cscTpStatsTrafficCounterName=_CscTpStatsTrafficCounterName_Object((1,3,6,1,4,1,9,9,634,1,2,1,2),_CscTpStatsTrafficCounterName_Type())
cscTpStatsTrafficCounterName.setMaxAccess(_C)
if mibBuilder.loadTexts:cscTpStatsTrafficCounterName.setStatus(_A)
_CscTpStatsTrafficCounterValue_Type=Counter64
_CscTpStatsTrafficCounterValue_Object=MibTableColumn
cscTpStatsTrafficCounterValue=_CscTpStatsTrafficCounterValue_Object((1,3,6,1,4,1,9,9,634,1,2,1,3),_CscTpStatsTrafficCounterValue_Type())
cscTpStatsTrafficCounterValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cscTpStatsTrafficCounterValue.setStatus(_A)
class _CscTpStatsTrafficCounterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('bytes',2),(_D,3)))
_CscTpStatsTrafficCounterType_Type.__name__=_I
_CscTpStatsTrafficCounterType_Object=MibTableColumn
cscTpStatsTrafficCounterType=_CscTpStatsTrafficCounterType_Object((1,3,6,1,4,1,9,9,634,1,2,1,4),_CscTpStatsTrafficCounterType_Type())
cscTpStatsTrafficCounterType.setMaxAccess(_C)
if mibBuilder.loadTexts:cscTpStatsTrafficCounterType.setStatus(_A)
_CscTpCounterDiscontinuityTime_Type=TimeStamp
_CscTpCounterDiscontinuityTime_Object=MibScalar
cscTpCounterDiscontinuityTime=_CscTpCounterDiscontinuityTime_Object((1,3,6,1,4,1,9,9,634,1,3),_CscTpCounterDiscontinuityTime_Type())
cscTpCounterDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cscTpCounterDiscontinuityTime.setStatus(_A)
_CiscoSCTpStatsMIBConform_ObjectIdentity=ObjectIdentity
ciscoSCTpStatsMIBConform=_CiscoSCTpStatsMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,634,2))
_CscTpStatsMIBCompliances_ObjectIdentity=ObjectIdentity
cscTpStatsMIBCompliances=_CscTpStatsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,634,2,1))
_CscTpStatsMIBGroups_ObjectIdentity=ObjectIdentity
cscTpStatsMIBGroups=_CscTpStatsMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,634,2,2))
cscTpStatsMIBObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,634,2,2,1))
cscTpStatsMIBObjectGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:cscTpStatsMIBObjectGroup.setStatus(_A)
cscTpStatsMIBTrafficCntrsObjGroup=ObjectGroup((1,3,6,1,4,1,9,9,634,2,2,2))
cscTpStatsMIBTrafficCntrsObjGroup.setObjects(*((_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:cscTpStatsMIBTrafficCntrsObjGroup.setStatus(_A)
cscTpCounterDiscontinuityGroup=ObjectGroup((1,3,6,1,4,1,9,9,634,2,2,3))
cscTpCounterDiscontinuityGroup.setObjects((_B,_h))
if mibBuilder.loadTexts:cscTpCounterDiscontinuityGroup.setStatus(_A)
cscTpStatsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,634,2,1,1))
cscTpStatsMIBCompliance.setObjects(*((_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:cscTpStatsMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoServiceControlTpStatsMIB':ciscoServiceControlTpStatsMIB,'ciscoSCTpStatsMIBNotifs':ciscoSCTpStatsMIBNotifs,'ciscoSCTpStatsMIBObjects':ciscoSCTpStatsMIBObjects,'cscTpTable':cscTpTable,'cscTpEntry':cscTpEntry,_K:cscTpTotalHandledPackets,_L:cscTpTotalHandledFlows,_M:cscTpActiveFlows,_N:cscTpTcpActiveFlows,_O:cscTpUdpActiveFlows,_P:cscTpTotalBlockedPackets,_Q:cscTpTotalBlockedFlows,_R:cscTpTotalBandwidthDiscardedPackets,_S:cscTpTotalWredDiscardedPackets,_T:cscTpTotalFragments,_U:cscTpTotalNonIpPackets,_V:cscTpTotalIpChecksumErrPackets,_W:cscTpTotalIpLengthErrPackets,_X:cscTpTotalIpBroadcastPackets,_Y:cscTpTotalTTLErrPackets,_Z:cscTpTotalTcpUdpChksumErrPackets,_a:cscTpHandledPacketsRate,_b:cscTpHandledFlowsRate,_c:cscTpFlowsCapacityUtilization,_d:cscTpServiceLoss,'cscTpStatsTrafficCountersTable':cscTpStatsTrafficCountersTable,'cscTpStatsTrafficCountersEntry':cscTpStatsTrafficCountersEntry,_J:cscTpStatsTrafficCounterIndex,_f:cscTpStatsTrafficCounterName,_e:cscTpStatsTrafficCounterValue,_g:cscTpStatsTrafficCounterType,_h:cscTpCounterDiscontinuityTime,'ciscoSCTpStatsMIBConform':ciscoSCTpStatsMIBConform,'cscTpStatsMIBCompliances':cscTpStatsMIBCompliances,'cscTpStatsMIBCompliance':cscTpStatsMIBCompliance,'cscTpStatsMIBGroups':cscTpStatsMIBGroups,_i:cscTpStatsMIBObjectGroup,_j:cscTpStatsMIBTrafficCntrsObjGroup,_k:cscTpCounterDiscontinuityGroup})