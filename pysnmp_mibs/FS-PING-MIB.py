_W='fsPingMIBGroup'
_V='fsPingTypeOfService'
_U='fsPingSourceInterfaceIndex'
_T='fsPingSourceIp'
_S='fsPingEntryStauts'
_R='fsPingCompleted'
_Q='fsPingMinTime'
_P='fsPingAvTime'
_O='fsPingMaxTime'
_N='fsPingReturns'
_M='fsPingTimeOuts'
_L='fsPingTimes'
_K='fsPingDataLength'
_J='fsPingAddress'
_I='traceRouteHopIndex'
_H='Integer32'
_G='traceRouteIndex'
_F='fsPingIndex'
_E='Unsigned32'
_D='read-create'
_C='read-only'
_B='FS-PING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
IfIndex,=mibBuilder.importSymbols('FS-TC','IfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
fsPingMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,3))
if mibBuilder.loadTexts:fsPingMIB.setRevisions(('2002-03-20 00:00',))
_FsPingMIBObjects_ObjectIdentity=ObjectIdentity
fsPingMIBObjects=_FsPingMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,3,1))
_FsPingTable_Object=MibTable
fsPingTable=_FsPingTable_Object((1,3,6,1,4,1,52642,1,1,10,2,3,1,1))
if mibBuilder.loadTexts:fsPingTable.setStatus(_A)
_FsPingEntry_Object=MibTableRow
fsPingEntry=_FsPingEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,3,1,1,1))
fsPingEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:fsPingEntry.setStatus(_A)
class _FsPingIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsPingIndex_Type.__name__=_H
_FsPingIndex_Object=MibTableColumn
fsPingIndex=_FsPingIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,3,1,1,1,1),_FsPingIndex_Type())
fsPingIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPingIndex.setStatus(_A)
_FsPingAddress_Type=IpAddress
_FsPingAddress_Object=MibTableColumn
fsPingAddress=_FsPingAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,3,1,1,1,2),_FsPingAddress_Type())
fsPingAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPingAddress.setStatus(_A)
class _FsPingDataLength_Type(Unsigned32):defaultValue=100
_FsPingDataLength_Type.__name__=_E
_FsPingDataLength_Object=MibTableColumn
fsPingDataLength=_FsPingDataLength_Object((1,3,6,1,4,1,52642,1,1,10,2,3,1,1,1,3),_FsPingDataLength_Type())
fsPingDataLength.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPingDataLength.setStatus(_A)
class _FsPingTimes_Type(Unsigned32):defaultValue=5
_FsPingTimes_Type.__name__=_E
_FsPingTimes_Object=MibTableColumn
fsPingTimes=_FsPingTimes_Object((1,3,6,1,4,1,52642,1,1,10,2,3,1,1,1,4),_FsPingTimes_Type())
fsPingTimes.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPingTimes.setStatus(_A)
class _FsPingTimeOuts_Type(Unsigned32):defaultValue=2000
_FsPingTimeOuts_Type.__name__=_E
_FsPingTimeOuts_Object=MibTableColumn
fsPingTimeOuts=_FsPingTimeOuts_Object((1,3,6,1,4,1,52642,1,1,10,2,3,1,1,1,5),_FsPingTimeOuts_Type())
fsPingTimeOuts.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPingTimeOuts.setStatus(_A)
_FsPingReturns_Type=Unsigned32
_FsPingReturns_Object=MibTableColumn
fsPingReturns=_FsPingReturns_Object((1,3,6,1,4,1,52642,1,1,10,2,3,1,1,1,6),_FsPingReturns_Type())
fsPingReturns.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPingReturns.setStatus(_A)
_FsPingMaxTime_Type=Unsigned32
_FsPingMaxTime_Object=MibTableColumn
fsPingMaxTime=_FsPingMaxTime_Object((1,3,6,1,4,1,52642,1,1,10,2,3,1,1,1,7),_FsPingMaxTime_Type())
fsPingMaxTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPingMaxTime.setStatus(_A)
_FsPingAvTime_Type=Unsigned32
_FsPingAvTime_Object=MibTableColumn
fsPingAvTime=_FsPingAvTime_Object((1,3,6,1,4,1,52642,1,1,10,2,3,1,1,1,8),_FsPingAvTime_Type())
fsPingAvTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPingAvTime.setStatus(_A)
_FsPingMinTime_Type=Unsigned32
_FsPingMinTime_Object=MibTableColumn
fsPingMinTime=_FsPingMinTime_Object((1,3,6,1,4,1,52642,1,1,10,2,3,1,1,1,9),_FsPingMinTime_Type())
fsPingMinTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPingMinTime.setStatus(_A)
_FsPingCompleted_Type=TruthValue
_FsPingCompleted_Object=MibTableColumn
fsPingCompleted=_FsPingCompleted_Object((1,3,6,1,4,1,52642,1,1,10,2,3,1,1,1,10),_FsPingCompleted_Type())
fsPingCompleted.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPingCompleted.setStatus(_A)
_FsPingEntryStauts_Type=RowStatus
_FsPingEntryStauts_Object=MibTableColumn
fsPingEntryStauts=_FsPingEntryStauts_Object((1,3,6,1,4,1,52642,1,1,10,2,3,1,1,1,11),_FsPingEntryStauts_Type())
fsPingEntryStauts.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPingEntryStauts.setStatus(_A)
_FsPingSourceIp_Type=IpAddress
_FsPingSourceIp_Object=MibTableColumn
fsPingSourceIp=_FsPingSourceIp_Object((1,3,6,1,4,1,52642,1,1,10,2,3,1,1,1,12),_FsPingSourceIp_Type())
fsPingSourceIp.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPingSourceIp.setStatus(_A)
_FsPingSourceInterfaceIndex_Type=IfIndex
_FsPingSourceInterfaceIndex_Object=MibTableColumn
fsPingSourceInterfaceIndex=_FsPingSourceInterfaceIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,3,1,1,1,13),_FsPingSourceInterfaceIndex_Type())
fsPingSourceInterfaceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPingSourceInterfaceIndex.setStatus(_A)
class _FsPingTypeOfService_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsPingTypeOfService_Type.__name__=_E
_FsPingTypeOfService_Object=MibTableColumn
fsPingTypeOfService=_FsPingTypeOfService_Object((1,3,6,1,4,1,52642,1,1,10,2,3,1,1,1,14),_FsPingTypeOfService_Type())
fsPingTypeOfService.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPingTypeOfService.setStatus(_A)
_FsPingMIBConformance_ObjectIdentity=ObjectIdentity
fsPingMIBConformance=_FsPingMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,3,2))
_FsPingMIBCompliances_ObjectIdentity=ObjectIdentity
fsPingMIBCompliances=_FsPingMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,3,2,1))
_FsPingMIBGroups_ObjectIdentity=ObjectIdentity
fsPingMIBGroups=_FsPingMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,3,2,2))
_TraceRouteMIBObjects_ObjectIdentity=ObjectIdentity
traceRouteMIBObjects=_TraceRouteMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,3,3))
_TraceRouteTable_Object=MibTable
traceRouteTable=_TraceRouteTable_Object((1,3,6,1,4,1,52642,1,1,10,2,3,3,1))
if mibBuilder.loadTexts:traceRouteTable.setStatus(_A)
_TraceRouteEntry_Object=MibTableRow
traceRouteEntry=_TraceRouteEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,3,3,1,1))
traceRouteEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:traceRouteEntry.setStatus(_A)
class _TraceRouteIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_TraceRouteIndex_Type.__name__=_E
_TraceRouteIndex_Object=MibTableColumn
traceRouteIndex=_TraceRouteIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,3,3,1,1,1),_TraceRouteIndex_Type())
traceRouteIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:traceRouteIndex.setStatus(_A)
_TraceRouteTargetAddr_Type=IpAddress
_TraceRouteTargetAddr_Object=MibTableColumn
traceRouteTargetAddr=_TraceRouteTargetAddr_Object((1,3,6,1,4,1,52642,1,1,10,2,3,3,1,1,2),_TraceRouteTargetAddr_Type())
traceRouteTargetAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:traceRouteTargetAddr.setStatus(_A)
class _TraceRouteHopCount_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_TraceRouteHopCount_Type.__name__=_E
_TraceRouteHopCount_Object=MibTableColumn
traceRouteHopCount=_TraceRouteHopCount_Object((1,3,6,1,4,1,52642,1,1,10,2,3,3,1,1,3),_TraceRouteHopCount_Type())
traceRouteHopCount.setMaxAccess(_D)
if mibBuilder.loadTexts:traceRouteHopCount.setStatus(_A)
class _TraceRoutePingCount_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_TraceRoutePingCount_Type.__name__=_E
_TraceRoutePingCount_Object=MibTableColumn
traceRoutePingCount=_TraceRoutePingCount_Object((1,3,6,1,4,1,52642,1,1,10,2,3,3,1,1,4),_TraceRoutePingCount_Type())
traceRoutePingCount.setMaxAccess(_D)
if mibBuilder.loadTexts:traceRoutePingCount.setStatus(_A)
class _TraceRoutePingTimeout_Type(Unsigned32):defaultValue=2000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60000))
_TraceRoutePingTimeout_Type.__name__=_E
_TraceRoutePingTimeout_Object=MibTableColumn
traceRoutePingTimeout=_TraceRoutePingTimeout_Object((1,3,6,1,4,1,52642,1,1,10,2,3,3,1,1,5),_TraceRoutePingTimeout_Type())
traceRoutePingTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:traceRoutePingTimeout.setStatus(_A)
_TraceRouteRowStatus_Type=RowStatus
_TraceRouteRowStatus_Object=MibTableColumn
traceRouteRowStatus=_TraceRouteRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,3,3,1,1,6),_TraceRouteRowStatus_Type())
traceRouteRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:traceRouteRowStatus.setStatus(_A)
_TraceRouteHopsTable_Object=MibTable
traceRouteHopsTable=_TraceRouteHopsTable_Object((1,3,6,1,4,1,52642,1,1,10,2,3,3,2))
if mibBuilder.loadTexts:traceRouteHopsTable.setStatus(_A)
_TraceRouteHopsEntry_Object=MibTableRow
traceRouteHopsEntry=_TraceRouteHopsEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,3,3,2,1))
traceRouteHopsEntry.setIndexNames((0,_B,_G),(0,_B,_I))
if mibBuilder.loadTexts:traceRouteHopsEntry.setStatus(_A)
_TraceRouteHopIndex_Type=Unsigned32
_TraceRouteHopIndex_Object=MibTableColumn
traceRouteHopIndex=_TraceRouteHopIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,3,3,2,1,1),_TraceRouteHopIndex_Type())
traceRouteHopIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:traceRouteHopIndex.setStatus(_A)
_TraceRouteHopPingIndex_Type=Unsigned32
_TraceRouteHopPingIndex_Object=MibTableColumn
traceRouteHopPingIndex=_TraceRouteHopPingIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,3,3,2,1,2),_TraceRouteHopPingIndex_Type())
traceRouteHopPingIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:traceRouteHopPingIndex.setStatus(_A)
_TraceRouteHopPingCompleted_Type=TruthValue
_TraceRouteHopPingCompleted_Object=MibTableColumn
traceRouteHopPingCompleted=_TraceRouteHopPingCompleted_Object((1,3,6,1,4,1,52642,1,1,10,2,3,3,2,1,3),_TraceRouteHopPingCompleted_Type())
traceRouteHopPingCompleted.setMaxAccess(_C)
if mibBuilder.loadTexts:traceRouteHopPingCompleted.setStatus(_A)
_TraceRouteHopPingResult_Type=TruthValue
_TraceRouteHopPingResult_Object=MibTableColumn
traceRouteHopPingResult=_TraceRouteHopPingResult_Object((1,3,6,1,4,1,52642,1,1,10,2,3,3,2,1,4),_TraceRouteHopPingResult_Type())
traceRouteHopPingResult.setMaxAccess(_C)
if mibBuilder.loadTexts:traceRouteHopPingResult.setStatus(_A)
_TraceRouteHopPingReturnTime_Type=Unsigned32
_TraceRouteHopPingReturnTime_Object=MibTableColumn
traceRouteHopPingReturnTime=_TraceRouteHopPingReturnTime_Object((1,3,6,1,4,1,52642,1,1,10,2,3,3,2,1,5),_TraceRouteHopPingReturnTime_Type())
traceRouteHopPingReturnTime.setMaxAccess(_C)
if mibBuilder.loadTexts:traceRouteHopPingReturnTime.setStatus(_A)
_TraceRouteHopAddr_Type=IpAddress
_TraceRouteHopAddr_Object=MibTableColumn
traceRouteHopAddr=_TraceRouteHopAddr_Object((1,3,6,1,4,1,52642,1,1,10,2,3,3,2,1,6),_TraceRouteHopAddr_Type())
traceRouteHopAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:traceRouteHopAddr.setStatus(_A)
fsPingMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,3,2,2,1))
fsPingMIBGroup.setObjects(*((_B,_F),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:fsPingMIBGroup.setStatus(_A)
fsPingMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,3,2,1,1))
fsPingMIBCompliance.setObjects((_B,_W))
if mibBuilder.loadTexts:fsPingMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsPingMIB':fsPingMIB,'fsPingMIBObjects':fsPingMIBObjects,'fsPingTable':fsPingTable,'fsPingEntry':fsPingEntry,_F:fsPingIndex,_J:fsPingAddress,_K:fsPingDataLength,_L:fsPingTimes,_M:fsPingTimeOuts,_N:fsPingReturns,_O:fsPingMaxTime,_P:fsPingAvTime,_Q:fsPingMinTime,_R:fsPingCompleted,_S:fsPingEntryStauts,_T:fsPingSourceIp,_U:fsPingSourceInterfaceIndex,_V:fsPingTypeOfService,'fsPingMIBConformance':fsPingMIBConformance,'fsPingMIBCompliances':fsPingMIBCompliances,'fsPingMIBCompliance':fsPingMIBCompliance,'fsPingMIBGroups':fsPingMIBGroups,_W:fsPingMIBGroup,'traceRouteMIBObjects':traceRouteMIBObjects,'traceRouteTable':traceRouteTable,'traceRouteEntry':traceRouteEntry,_G:traceRouteIndex,'traceRouteTargetAddr':traceRouteTargetAddr,'traceRouteHopCount':traceRouteHopCount,'traceRoutePingCount':traceRoutePingCount,'traceRoutePingTimeout':traceRoutePingTimeout,'traceRouteRowStatus':traceRouteRowStatus,'traceRouteHopsTable':traceRouteHopsTable,'traceRouteHopsEntry':traceRouteHopsEntry,_I:traceRouteHopIndex,'traceRouteHopPingIndex':traceRouteHopPingIndex,'traceRouteHopPingCompleted':traceRouteHopPingCompleted,'traceRouteHopPingResult':traceRouteHopPingResult,'traceRouteHopPingReturnTime':traceRouteHopPingReturnTime,'traceRouteHopAddr':traceRouteHopAddr})