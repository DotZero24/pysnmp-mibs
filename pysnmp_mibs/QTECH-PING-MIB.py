_W='qtechPingMIBGroup'
_V='qtechPingTypeOfService'
_U='qtechPingSourceInterfaceIndex'
_T='qtechPingSourceIp'
_S='qtechPingEntryStauts'
_R='qtechPingCompleted'
_Q='qtechPingMinTime'
_P='qtechPingAvTime'
_O='qtechPingMaxTime'
_N='qtechPingReturns'
_M='qtechPingTimeOuts'
_L='qtechPingTimes'
_K='qtechPingDataLength'
_J='qtechPingAddress'
_I='traceRouteHopIndex'
_H='Integer32'
_G='traceRouteIndex'
_F='qtechPingIndex'
_E='Unsigned32'
_D='read-create'
_C='read-only'
_B='QTECH-PING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
IfIndex,=mibBuilder.importSymbols('QTECH-TC','IfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
qtechPingMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,3))
if mibBuilder.loadTexts:qtechPingMIB.setRevisions(('2002-03-20 00:00',))
_QtechPingMIBObjects_ObjectIdentity=ObjectIdentity
qtechPingMIBObjects=_QtechPingMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,3,1))
_QtechPingTable_Object=MibTable
qtechPingTable=_QtechPingTable_Object((1,3,6,1,4,1,27514,1,1,10,2,3,1,1))
if mibBuilder.loadTexts:qtechPingTable.setStatus(_A)
_QtechPingEntry_Object=MibTableRow
qtechPingEntry=_QtechPingEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,3,1,1,1))
qtechPingEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:qtechPingEntry.setStatus(_A)
class _QtechPingIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_QtechPingIndex_Type.__name__=_H
_QtechPingIndex_Object=MibTableColumn
qtechPingIndex=_QtechPingIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,3,1,1,1,1),_QtechPingIndex_Type())
qtechPingIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPingIndex.setStatus(_A)
_QtechPingAddress_Type=IpAddress
_QtechPingAddress_Object=MibTableColumn
qtechPingAddress=_QtechPingAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,3,1,1,1,2),_QtechPingAddress_Type())
qtechPingAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechPingAddress.setStatus(_A)
class _QtechPingDataLength_Type(Unsigned32):defaultValue=100
_QtechPingDataLength_Type.__name__=_E
_QtechPingDataLength_Object=MibTableColumn
qtechPingDataLength=_QtechPingDataLength_Object((1,3,6,1,4,1,27514,1,1,10,2,3,1,1,1,3),_QtechPingDataLength_Type())
qtechPingDataLength.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechPingDataLength.setStatus(_A)
class _QtechPingTimes_Type(Unsigned32):defaultValue=5
_QtechPingTimes_Type.__name__=_E
_QtechPingTimes_Object=MibTableColumn
qtechPingTimes=_QtechPingTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,3,1,1,1,4),_QtechPingTimes_Type())
qtechPingTimes.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechPingTimes.setStatus(_A)
class _QtechPingTimeOuts_Type(Unsigned32):defaultValue=2000
_QtechPingTimeOuts_Type.__name__=_E
_QtechPingTimeOuts_Object=MibTableColumn
qtechPingTimeOuts=_QtechPingTimeOuts_Object((1,3,6,1,4,1,27514,1,1,10,2,3,1,1,1,5),_QtechPingTimeOuts_Type())
qtechPingTimeOuts.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechPingTimeOuts.setStatus(_A)
_QtechPingReturns_Type=Unsigned32
_QtechPingReturns_Object=MibTableColumn
qtechPingReturns=_QtechPingReturns_Object((1,3,6,1,4,1,27514,1,1,10,2,3,1,1,1,6),_QtechPingReturns_Type())
qtechPingReturns.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPingReturns.setStatus(_A)
_QtechPingMaxTime_Type=Unsigned32
_QtechPingMaxTime_Object=MibTableColumn
qtechPingMaxTime=_QtechPingMaxTime_Object((1,3,6,1,4,1,27514,1,1,10,2,3,1,1,1,7),_QtechPingMaxTime_Type())
qtechPingMaxTime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPingMaxTime.setStatus(_A)
_QtechPingAvTime_Type=Unsigned32
_QtechPingAvTime_Object=MibTableColumn
qtechPingAvTime=_QtechPingAvTime_Object((1,3,6,1,4,1,27514,1,1,10,2,3,1,1,1,8),_QtechPingAvTime_Type())
qtechPingAvTime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPingAvTime.setStatus(_A)
_QtechPingMinTime_Type=Unsigned32
_QtechPingMinTime_Object=MibTableColumn
qtechPingMinTime=_QtechPingMinTime_Object((1,3,6,1,4,1,27514,1,1,10,2,3,1,1,1,9),_QtechPingMinTime_Type())
qtechPingMinTime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPingMinTime.setStatus(_A)
_QtechPingCompleted_Type=TruthValue
_QtechPingCompleted_Object=MibTableColumn
qtechPingCompleted=_QtechPingCompleted_Object((1,3,6,1,4,1,27514,1,1,10,2,3,1,1,1,10),_QtechPingCompleted_Type())
qtechPingCompleted.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPingCompleted.setStatus(_A)
_QtechPingEntryStauts_Type=RowStatus
_QtechPingEntryStauts_Object=MibTableColumn
qtechPingEntryStauts=_QtechPingEntryStauts_Object((1,3,6,1,4,1,27514,1,1,10,2,3,1,1,1,11),_QtechPingEntryStauts_Type())
qtechPingEntryStauts.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechPingEntryStauts.setStatus(_A)
_QtechPingSourceIp_Type=IpAddress
_QtechPingSourceIp_Object=MibTableColumn
qtechPingSourceIp=_QtechPingSourceIp_Object((1,3,6,1,4,1,27514,1,1,10,2,3,1,1,1,12),_QtechPingSourceIp_Type())
qtechPingSourceIp.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechPingSourceIp.setStatus(_A)
_QtechPingSourceInterfaceIndex_Type=IfIndex
_QtechPingSourceInterfaceIndex_Object=MibTableColumn
qtechPingSourceInterfaceIndex=_QtechPingSourceInterfaceIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,3,1,1,1,13),_QtechPingSourceInterfaceIndex_Type())
qtechPingSourceInterfaceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechPingSourceInterfaceIndex.setStatus(_A)
class _QtechPingTypeOfService_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_QtechPingTypeOfService_Type.__name__=_E
_QtechPingTypeOfService_Object=MibTableColumn
qtechPingTypeOfService=_QtechPingTypeOfService_Object((1,3,6,1,4,1,27514,1,1,10,2,3,1,1,1,14),_QtechPingTypeOfService_Type())
qtechPingTypeOfService.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechPingTypeOfService.setStatus(_A)
_QtechPingMIBConformance_ObjectIdentity=ObjectIdentity
qtechPingMIBConformance=_QtechPingMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,3,2))
_QtechPingMIBCompliances_ObjectIdentity=ObjectIdentity
qtechPingMIBCompliances=_QtechPingMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,3,2,1))
_QtechPingMIBGroups_ObjectIdentity=ObjectIdentity
qtechPingMIBGroups=_QtechPingMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,3,2,2))
_TraceRouteMIBObjects_ObjectIdentity=ObjectIdentity
traceRouteMIBObjects=_TraceRouteMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,3,3))
_TraceRouteTable_Object=MibTable
traceRouteTable=_TraceRouteTable_Object((1,3,6,1,4,1,27514,1,1,10,2,3,3,1))
if mibBuilder.loadTexts:traceRouteTable.setStatus(_A)
_TraceRouteEntry_Object=MibTableRow
traceRouteEntry=_TraceRouteEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,3,3,1,1))
traceRouteEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:traceRouteEntry.setStatus(_A)
class _TraceRouteIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_TraceRouteIndex_Type.__name__=_E
_TraceRouteIndex_Object=MibTableColumn
traceRouteIndex=_TraceRouteIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,3,3,1,1,1),_TraceRouteIndex_Type())
traceRouteIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:traceRouteIndex.setStatus(_A)
_TraceRouteTargetAddr_Type=IpAddress
_TraceRouteTargetAddr_Object=MibTableColumn
traceRouteTargetAddr=_TraceRouteTargetAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,3,3,1,1,2),_TraceRouteTargetAddr_Type())
traceRouteTargetAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:traceRouteTargetAddr.setStatus(_A)
class _TraceRouteHopCount_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_TraceRouteHopCount_Type.__name__=_E
_TraceRouteHopCount_Object=MibTableColumn
traceRouteHopCount=_TraceRouteHopCount_Object((1,3,6,1,4,1,27514,1,1,10,2,3,3,1,1,3),_TraceRouteHopCount_Type())
traceRouteHopCount.setMaxAccess(_D)
if mibBuilder.loadTexts:traceRouteHopCount.setStatus(_A)
class _TraceRoutePingCount_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_TraceRoutePingCount_Type.__name__=_E
_TraceRoutePingCount_Object=MibTableColumn
traceRoutePingCount=_TraceRoutePingCount_Object((1,3,6,1,4,1,27514,1,1,10,2,3,3,1,1,4),_TraceRoutePingCount_Type())
traceRoutePingCount.setMaxAccess(_D)
if mibBuilder.loadTexts:traceRoutePingCount.setStatus(_A)
class _TraceRoutePingTimeout_Type(Unsigned32):defaultValue=2000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60000))
_TraceRoutePingTimeout_Type.__name__=_E
_TraceRoutePingTimeout_Object=MibTableColumn
traceRoutePingTimeout=_TraceRoutePingTimeout_Object((1,3,6,1,4,1,27514,1,1,10,2,3,3,1,1,5),_TraceRoutePingTimeout_Type())
traceRoutePingTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:traceRoutePingTimeout.setStatus(_A)
_TraceRouteRowStatus_Type=RowStatus
_TraceRouteRowStatus_Object=MibTableColumn
traceRouteRowStatus=_TraceRouteRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,3,3,1,1,6),_TraceRouteRowStatus_Type())
traceRouteRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:traceRouteRowStatus.setStatus(_A)
_TraceRouteHopsTable_Object=MibTable
traceRouteHopsTable=_TraceRouteHopsTable_Object((1,3,6,1,4,1,27514,1,1,10,2,3,3,2))
if mibBuilder.loadTexts:traceRouteHopsTable.setStatus(_A)
_TraceRouteHopsEntry_Object=MibTableRow
traceRouteHopsEntry=_TraceRouteHopsEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,3,3,2,1))
traceRouteHopsEntry.setIndexNames((0,_B,_G),(0,_B,_I))
if mibBuilder.loadTexts:traceRouteHopsEntry.setStatus(_A)
_TraceRouteHopIndex_Type=Unsigned32
_TraceRouteHopIndex_Object=MibTableColumn
traceRouteHopIndex=_TraceRouteHopIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,3,3,2,1,1),_TraceRouteHopIndex_Type())
traceRouteHopIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:traceRouteHopIndex.setStatus(_A)
_TraceRouteHopPingIndex_Type=Unsigned32
_TraceRouteHopPingIndex_Object=MibTableColumn
traceRouteHopPingIndex=_TraceRouteHopPingIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,3,3,2,1,2),_TraceRouteHopPingIndex_Type())
traceRouteHopPingIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:traceRouteHopPingIndex.setStatus(_A)
_TraceRouteHopPingCompleted_Type=TruthValue
_TraceRouteHopPingCompleted_Object=MibTableColumn
traceRouteHopPingCompleted=_TraceRouteHopPingCompleted_Object((1,3,6,1,4,1,27514,1,1,10,2,3,3,2,1,3),_TraceRouteHopPingCompleted_Type())
traceRouteHopPingCompleted.setMaxAccess(_C)
if mibBuilder.loadTexts:traceRouteHopPingCompleted.setStatus(_A)
_TraceRouteHopPingResult_Type=TruthValue
_TraceRouteHopPingResult_Object=MibTableColumn
traceRouteHopPingResult=_TraceRouteHopPingResult_Object((1,3,6,1,4,1,27514,1,1,10,2,3,3,2,1,4),_TraceRouteHopPingResult_Type())
traceRouteHopPingResult.setMaxAccess(_C)
if mibBuilder.loadTexts:traceRouteHopPingResult.setStatus(_A)
_TraceRouteHopPingReturnTime_Type=Unsigned32
_TraceRouteHopPingReturnTime_Object=MibTableColumn
traceRouteHopPingReturnTime=_TraceRouteHopPingReturnTime_Object((1,3,6,1,4,1,27514,1,1,10,2,3,3,2,1,5),_TraceRouteHopPingReturnTime_Type())
traceRouteHopPingReturnTime.setMaxAccess(_C)
if mibBuilder.loadTexts:traceRouteHopPingReturnTime.setStatus(_A)
_TraceRouteHopAddr_Type=IpAddress
_TraceRouteHopAddr_Object=MibTableColumn
traceRouteHopAddr=_TraceRouteHopAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,3,3,2,1,6),_TraceRouteHopAddr_Type())
traceRouteHopAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:traceRouteHopAddr.setStatus(_A)
qtechPingMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,3,2,2,1))
qtechPingMIBGroup.setObjects(*((_B,_F),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:qtechPingMIBGroup.setStatus(_A)
qtechPingMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,3,2,1,1))
qtechPingMIBCompliance.setObjects((_B,_W))
if mibBuilder.loadTexts:qtechPingMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechPingMIB':qtechPingMIB,'qtechPingMIBObjects':qtechPingMIBObjects,'qtechPingTable':qtechPingTable,'qtechPingEntry':qtechPingEntry,_F:qtechPingIndex,_J:qtechPingAddress,_K:qtechPingDataLength,_L:qtechPingTimes,_M:qtechPingTimeOuts,_N:qtechPingReturns,_O:qtechPingMaxTime,_P:qtechPingAvTime,_Q:qtechPingMinTime,_R:qtechPingCompleted,_S:qtechPingEntryStauts,_T:qtechPingSourceIp,_U:qtechPingSourceInterfaceIndex,_V:qtechPingTypeOfService,'qtechPingMIBConformance':qtechPingMIBConformance,'qtechPingMIBCompliances':qtechPingMIBCompliances,'qtechPingMIBCompliance':qtechPingMIBCompliance,'qtechPingMIBGroups':qtechPingMIBGroups,_W:qtechPingMIBGroup,'traceRouteMIBObjects':traceRouteMIBObjects,'traceRouteTable':traceRouteTable,'traceRouteEntry':traceRouteEntry,_G:traceRouteIndex,'traceRouteTargetAddr':traceRouteTargetAddr,'traceRouteHopCount':traceRouteHopCount,'traceRoutePingCount':traceRoutePingCount,'traceRoutePingTimeout':traceRoutePingTimeout,'traceRouteRowStatus':traceRouteRowStatus,'traceRouteHopsTable':traceRouteHopsTable,'traceRouteHopsEntry':traceRouteHopsEntry,_I:traceRouteHopIndex,'traceRouteHopPingIndex':traceRouteHopPingIndex,'traceRouteHopPingCompleted':traceRouteHopPingCompleted,'traceRouteHopPingResult':traceRouteHopPingResult,'traceRouteHopPingReturnTime':traceRouteHopPingReturnTime,'traceRouteHopAddr':traceRouteHopAddr})