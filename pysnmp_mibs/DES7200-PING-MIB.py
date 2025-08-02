_W='myPingMIBGroup'
_V='myPingTypeOfService'
_U='myPingSourceInterfaceIndex'
_T='myPingSourceIp'
_S='myPingEntryStauts'
_R='myPingCompleted'
_Q='myPingMinTime'
_P='myPingAvTime'
_O='myPingMaxTime'
_N='myPingReturns'
_M='myPingTimeOuts'
_L='myPingTimes'
_K='myPingDataLength'
_J='myPingAddress'
_I='traceRouteHopIndex'
_H='Integer32'
_G='traceRouteIndex'
_F='myPingIndex'
_E='Unsigned32'
_D='read-create'
_C='read-only'
_B='DES7200-PING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
myMgmt,=mibBuilder.importSymbols('DES7200-SMI','myMgmt')
IfIndex,=mibBuilder.importSymbols('DES7200-TC','IfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
myPingMIB=ModuleIdentity((1,3,6,1,4,1,171,10,97,2,3))
if mibBuilder.loadTexts:myPingMIB.setRevisions(('2002-03-20 00:00',))
_MyPingMIBObjects_ObjectIdentity=ObjectIdentity
myPingMIBObjects=_MyPingMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,3,1))
_MyPingTable_Object=MibTable
myPingTable=_MyPingTable_Object((1,3,6,1,4,1,171,10,97,2,3,1,1))
if mibBuilder.loadTexts:myPingTable.setStatus(_A)
_MyPingEntry_Object=MibTableRow
myPingEntry=_MyPingEntry_Object((1,3,6,1,4,1,171,10,97,2,3,1,1,1))
myPingEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:myPingEntry.setStatus(_A)
class _MyPingIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MyPingIndex_Type.__name__=_H
_MyPingIndex_Object=MibTableColumn
myPingIndex=_MyPingIndex_Object((1,3,6,1,4,1,171,10,97,2,3,1,1,1,1),_MyPingIndex_Type())
myPingIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:myPingIndex.setStatus(_A)
_MyPingAddress_Type=IpAddress
_MyPingAddress_Object=MibTableColumn
myPingAddress=_MyPingAddress_Object((1,3,6,1,4,1,171,10,97,2,3,1,1,1,2),_MyPingAddress_Type())
myPingAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:myPingAddress.setStatus(_A)
class _MyPingDataLength_Type(Unsigned32):defaultValue=100
_MyPingDataLength_Type.__name__=_E
_MyPingDataLength_Object=MibTableColumn
myPingDataLength=_MyPingDataLength_Object((1,3,6,1,4,1,171,10,97,2,3,1,1,1,3),_MyPingDataLength_Type())
myPingDataLength.setMaxAccess(_D)
if mibBuilder.loadTexts:myPingDataLength.setStatus(_A)
class _MyPingTimes_Type(Unsigned32):defaultValue=5
_MyPingTimes_Type.__name__=_E
_MyPingTimes_Object=MibTableColumn
myPingTimes=_MyPingTimes_Object((1,3,6,1,4,1,171,10,97,2,3,1,1,1,4),_MyPingTimes_Type())
myPingTimes.setMaxAccess(_D)
if mibBuilder.loadTexts:myPingTimes.setStatus(_A)
class _MyPingTimeOuts_Type(Unsigned32):defaultValue=2000
_MyPingTimeOuts_Type.__name__=_E
_MyPingTimeOuts_Object=MibTableColumn
myPingTimeOuts=_MyPingTimeOuts_Object((1,3,6,1,4,1,171,10,97,2,3,1,1,1,5),_MyPingTimeOuts_Type())
myPingTimeOuts.setMaxAccess(_D)
if mibBuilder.loadTexts:myPingTimeOuts.setStatus(_A)
_MyPingReturns_Type=Unsigned32
_MyPingReturns_Object=MibTableColumn
myPingReturns=_MyPingReturns_Object((1,3,6,1,4,1,171,10,97,2,3,1,1,1,6),_MyPingReturns_Type())
myPingReturns.setMaxAccess(_C)
if mibBuilder.loadTexts:myPingReturns.setStatus(_A)
_MyPingMaxTime_Type=Unsigned32
_MyPingMaxTime_Object=MibTableColumn
myPingMaxTime=_MyPingMaxTime_Object((1,3,6,1,4,1,171,10,97,2,3,1,1,1,7),_MyPingMaxTime_Type())
myPingMaxTime.setMaxAccess(_C)
if mibBuilder.loadTexts:myPingMaxTime.setStatus(_A)
_MyPingAvTime_Type=Unsigned32
_MyPingAvTime_Object=MibTableColumn
myPingAvTime=_MyPingAvTime_Object((1,3,6,1,4,1,171,10,97,2,3,1,1,1,8),_MyPingAvTime_Type())
myPingAvTime.setMaxAccess(_C)
if mibBuilder.loadTexts:myPingAvTime.setStatus(_A)
_MyPingMinTime_Type=Unsigned32
_MyPingMinTime_Object=MibTableColumn
myPingMinTime=_MyPingMinTime_Object((1,3,6,1,4,1,171,10,97,2,3,1,1,1,9),_MyPingMinTime_Type())
myPingMinTime.setMaxAccess(_C)
if mibBuilder.loadTexts:myPingMinTime.setStatus(_A)
_MyPingCompleted_Type=TruthValue
_MyPingCompleted_Object=MibTableColumn
myPingCompleted=_MyPingCompleted_Object((1,3,6,1,4,1,171,10,97,2,3,1,1,1,10),_MyPingCompleted_Type())
myPingCompleted.setMaxAccess(_C)
if mibBuilder.loadTexts:myPingCompleted.setStatus(_A)
_MyPingEntryStauts_Type=RowStatus
_MyPingEntryStauts_Object=MibTableColumn
myPingEntryStauts=_MyPingEntryStauts_Object((1,3,6,1,4,1,171,10,97,2,3,1,1,1,11),_MyPingEntryStauts_Type())
myPingEntryStauts.setMaxAccess(_D)
if mibBuilder.loadTexts:myPingEntryStauts.setStatus(_A)
_MyPingSourceIp_Type=IpAddress
_MyPingSourceIp_Object=MibTableColumn
myPingSourceIp=_MyPingSourceIp_Object((1,3,6,1,4,1,171,10,97,2,3,1,1,1,12),_MyPingSourceIp_Type())
myPingSourceIp.setMaxAccess(_D)
if mibBuilder.loadTexts:myPingSourceIp.setStatus(_A)
_MyPingSourceInterfaceIndex_Type=IfIndex
_MyPingSourceInterfaceIndex_Object=MibTableColumn
myPingSourceInterfaceIndex=_MyPingSourceInterfaceIndex_Object((1,3,6,1,4,1,171,10,97,2,3,1,1,1,13),_MyPingSourceInterfaceIndex_Type())
myPingSourceInterfaceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:myPingSourceInterfaceIndex.setStatus(_A)
class _MyPingTypeOfService_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MyPingTypeOfService_Type.__name__=_E
_MyPingTypeOfService_Object=MibTableColumn
myPingTypeOfService=_MyPingTypeOfService_Object((1,3,6,1,4,1,171,10,97,2,3,1,1,1,14),_MyPingTypeOfService_Type())
myPingTypeOfService.setMaxAccess(_D)
if mibBuilder.loadTexts:myPingTypeOfService.setStatus(_A)
_MyPingMIBConformance_ObjectIdentity=ObjectIdentity
myPingMIBConformance=_MyPingMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,3,2))
_MyPingMIBCompliances_ObjectIdentity=ObjectIdentity
myPingMIBCompliances=_MyPingMIBCompliances_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,3,2,1))
_MyPingMIBGroups_ObjectIdentity=ObjectIdentity
myPingMIBGroups=_MyPingMIBGroups_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,3,2,2))
_TraceRouteMIBObjects_ObjectIdentity=ObjectIdentity
traceRouteMIBObjects=_TraceRouteMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,3,3))
_TraceRouteTable_Object=MibTable
traceRouteTable=_TraceRouteTable_Object((1,3,6,1,4,1,171,10,97,2,3,3,1))
if mibBuilder.loadTexts:traceRouteTable.setStatus(_A)
_TraceRouteEntry_Object=MibTableRow
traceRouteEntry=_TraceRouteEntry_Object((1,3,6,1,4,1,171,10,97,2,3,3,1,1))
traceRouteEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:traceRouteEntry.setStatus(_A)
class _TraceRouteIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_TraceRouteIndex_Type.__name__=_E
_TraceRouteIndex_Object=MibTableColumn
traceRouteIndex=_TraceRouteIndex_Object((1,3,6,1,4,1,171,10,97,2,3,3,1,1,1),_TraceRouteIndex_Type())
traceRouteIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:traceRouteIndex.setStatus(_A)
_TraceRouteTargetAddr_Type=IpAddress
_TraceRouteTargetAddr_Object=MibTableColumn
traceRouteTargetAddr=_TraceRouteTargetAddr_Object((1,3,6,1,4,1,171,10,97,2,3,3,1,1,2),_TraceRouteTargetAddr_Type())
traceRouteTargetAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:traceRouteTargetAddr.setStatus(_A)
class _TraceRouteHopCount_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_TraceRouteHopCount_Type.__name__=_E
_TraceRouteHopCount_Object=MibTableColumn
traceRouteHopCount=_TraceRouteHopCount_Object((1,3,6,1,4,1,171,10,97,2,3,3,1,1,3),_TraceRouteHopCount_Type())
traceRouteHopCount.setMaxAccess(_D)
if mibBuilder.loadTexts:traceRouteHopCount.setStatus(_A)
class _TraceRoutePingCount_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_TraceRoutePingCount_Type.__name__=_E
_TraceRoutePingCount_Object=MibTableColumn
traceRoutePingCount=_TraceRoutePingCount_Object((1,3,6,1,4,1,171,10,97,2,3,3,1,1,4),_TraceRoutePingCount_Type())
traceRoutePingCount.setMaxAccess(_D)
if mibBuilder.loadTexts:traceRoutePingCount.setStatus(_A)
class _TraceRoutePingTimeout_Type(Unsigned32):defaultValue=2000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60000))
_TraceRoutePingTimeout_Type.__name__=_E
_TraceRoutePingTimeout_Object=MibTableColumn
traceRoutePingTimeout=_TraceRoutePingTimeout_Object((1,3,6,1,4,1,171,10,97,2,3,3,1,1,5),_TraceRoutePingTimeout_Type())
traceRoutePingTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:traceRoutePingTimeout.setStatus(_A)
_TraceRouteRowStatus_Type=RowStatus
_TraceRouteRowStatus_Object=MibTableColumn
traceRouteRowStatus=_TraceRouteRowStatus_Object((1,3,6,1,4,1,171,10,97,2,3,3,1,1,6),_TraceRouteRowStatus_Type())
traceRouteRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:traceRouteRowStatus.setStatus(_A)
_TraceRouteHopsTable_Object=MibTable
traceRouteHopsTable=_TraceRouteHopsTable_Object((1,3,6,1,4,1,171,10,97,2,3,3,2))
if mibBuilder.loadTexts:traceRouteHopsTable.setStatus(_A)
_TraceRouteHopsEntry_Object=MibTableRow
traceRouteHopsEntry=_TraceRouteHopsEntry_Object((1,3,6,1,4,1,171,10,97,2,3,3,2,1))
traceRouteHopsEntry.setIndexNames((0,_B,_G),(0,_B,_I))
if mibBuilder.loadTexts:traceRouteHopsEntry.setStatus(_A)
_TraceRouteHopIndex_Type=Unsigned32
_TraceRouteHopIndex_Object=MibTableColumn
traceRouteHopIndex=_TraceRouteHopIndex_Object((1,3,6,1,4,1,171,10,97,2,3,3,2,1,1),_TraceRouteHopIndex_Type())
traceRouteHopIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:traceRouteHopIndex.setStatus(_A)
_TraceRouteHopPingIndex_Type=Unsigned32
_TraceRouteHopPingIndex_Object=MibTableColumn
traceRouteHopPingIndex=_TraceRouteHopPingIndex_Object((1,3,6,1,4,1,171,10,97,2,3,3,2,1,2),_TraceRouteHopPingIndex_Type())
traceRouteHopPingIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:traceRouteHopPingIndex.setStatus(_A)
_TraceRouteHopPingCompleted_Type=TruthValue
_TraceRouteHopPingCompleted_Object=MibTableColumn
traceRouteHopPingCompleted=_TraceRouteHopPingCompleted_Object((1,3,6,1,4,1,171,10,97,2,3,3,2,1,3),_TraceRouteHopPingCompleted_Type())
traceRouteHopPingCompleted.setMaxAccess(_C)
if mibBuilder.loadTexts:traceRouteHopPingCompleted.setStatus(_A)
_TraceRouteHopPingResult_Type=TruthValue
_TraceRouteHopPingResult_Object=MibTableColumn
traceRouteHopPingResult=_TraceRouteHopPingResult_Object((1,3,6,1,4,1,171,10,97,2,3,3,2,1,4),_TraceRouteHopPingResult_Type())
traceRouteHopPingResult.setMaxAccess(_C)
if mibBuilder.loadTexts:traceRouteHopPingResult.setStatus(_A)
_TraceRouteHopPingReturnTime_Type=Unsigned32
_TraceRouteHopPingReturnTime_Object=MibTableColumn
traceRouteHopPingReturnTime=_TraceRouteHopPingReturnTime_Object((1,3,6,1,4,1,171,10,97,2,3,3,2,1,5),_TraceRouteHopPingReturnTime_Type())
traceRouteHopPingReturnTime.setMaxAccess(_C)
if mibBuilder.loadTexts:traceRouteHopPingReturnTime.setStatus(_A)
_TraceRouteHopAddr_Type=IpAddress
_TraceRouteHopAddr_Object=MibTableColumn
traceRouteHopAddr=_TraceRouteHopAddr_Object((1,3,6,1,4,1,171,10,97,2,3,3,2,1,6),_TraceRouteHopAddr_Type())
traceRouteHopAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:traceRouteHopAddr.setStatus(_A)
myPingMIBGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,3,2,2,1))
myPingMIBGroup.setObjects(*((_B,_F),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:myPingMIBGroup.setStatus(_A)
myPingMIBCompliance=ModuleCompliance((1,3,6,1,4,1,171,10,97,2,3,2,1,1))
myPingMIBCompliance.setObjects((_B,_W))
if mibBuilder.loadTexts:myPingMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'myPingMIB':myPingMIB,'myPingMIBObjects':myPingMIBObjects,'myPingTable':myPingTable,'myPingEntry':myPingEntry,_F:myPingIndex,_J:myPingAddress,_K:myPingDataLength,_L:myPingTimes,_M:myPingTimeOuts,_N:myPingReturns,_O:myPingMaxTime,_P:myPingAvTime,_Q:myPingMinTime,_R:myPingCompleted,_S:myPingEntryStauts,_T:myPingSourceIp,_U:myPingSourceInterfaceIndex,_V:myPingTypeOfService,'myPingMIBConformance':myPingMIBConformance,'myPingMIBCompliances':myPingMIBCompliances,'myPingMIBCompliance':myPingMIBCompliance,'myPingMIBGroups':myPingMIBGroups,_W:myPingMIBGroup,'traceRouteMIBObjects':traceRouteMIBObjects,'traceRouteTable':traceRouteTable,'traceRouteEntry':traceRouteEntry,_G:traceRouteIndex,'traceRouteTargetAddr':traceRouteTargetAddr,'traceRouteHopCount':traceRouteHopCount,'traceRoutePingCount':traceRoutePingCount,'traceRoutePingTimeout':traceRoutePingTimeout,'traceRouteRowStatus':traceRouteRowStatus,'traceRouteHopsTable':traceRouteHopsTable,'traceRouteHopsEntry':traceRouteHopsEntry,_I:traceRouteHopIndex,'traceRouteHopPingIndex':traceRouteHopPingIndex,'traceRouteHopPingCompleted':traceRouteHopPingCompleted,'traceRouteHopPingResult':traceRouteHopPingResult,'traceRouteHopPingReturnTime':traceRouteHopPingReturnTime,'traceRouteHopAddr':traceRouteHopAddr})