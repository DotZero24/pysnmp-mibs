_N='hwIgmpSnoopingVlanID'
_M='read-create'
_L='hwIgmpSnoopingGroupPolicyVlanID'
_K='hwIgmpSnoopingGroupPolicyIfIndex'
_J='hwIgmpSnoopingFastLeaveIfIndex'
_I='hwIgmpSnoopingGroupIfIndex'
_H='Unsigned32'
_G='EnabledStatus'
_F='not-accessible'
_E='A3COM-HUAWEI-LswIGSP-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lswCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','lswCommon')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hwLswIgmpsnoopingMib=ModuleIdentity((1,3,6,1,4,1,43,45,1,2,23,1,7))
if mibBuilder.loadTexts:hwLswIgmpsnoopingMib.setRevisions(('2001-06-29 00:00',))
class EnabledStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_HwLswIgmpsnoopingMibObject_ObjectIdentity=ObjectIdentity
hwLswIgmpsnoopingMibObject=_HwLswIgmpsnoopingMibObject_ObjectIdentity((1,3,6,1,4,1,43,45,1,2,23,1,7,1))
_HwIgmpSnoopingStatus_Type=EnabledStatus
_HwIgmpSnoopingStatus_Object=MibScalar
hwIgmpSnoopingStatus=_HwIgmpSnoopingStatus_Object((1,3,6,1,4,1,43,45,1,2,23,1,7,1,1),_HwIgmpSnoopingStatus_Type())
hwIgmpSnoopingStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hwIgmpSnoopingStatus.setStatus(_A)
class _HwIgmpSnoopingRouterPortAge_Type(Integer32):defaultValue=105;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_HwIgmpSnoopingRouterPortAge_Type.__name__=_C
_HwIgmpSnoopingRouterPortAge_Object=MibScalar
hwIgmpSnoopingRouterPortAge=_HwIgmpSnoopingRouterPortAge_Object((1,3,6,1,4,1,43,45,1,2,23,1,7,1,2),_HwIgmpSnoopingRouterPortAge_Type())
hwIgmpSnoopingRouterPortAge.setMaxAccess(_B)
if mibBuilder.loadTexts:hwIgmpSnoopingRouterPortAge.setStatus(_A)
class _HwIgmpSnoopingResponseTime_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,25))
_HwIgmpSnoopingResponseTime_Type.__name__=_C
_HwIgmpSnoopingResponseTime_Object=MibScalar
hwIgmpSnoopingResponseTime=_HwIgmpSnoopingResponseTime_Object((1,3,6,1,4,1,43,45,1,2,23,1,7,1,3),_HwIgmpSnoopingResponseTime_Type())
hwIgmpSnoopingResponseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hwIgmpSnoopingResponseTime.setStatus(_A)
class _HwIgmpSnoopingHostTime_Type(Integer32):defaultValue=260;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,1000))
_HwIgmpSnoopingHostTime_Type.__name__=_C
_HwIgmpSnoopingHostTime_Object=MibScalar
hwIgmpSnoopingHostTime=_HwIgmpSnoopingHostTime_Object((1,3,6,1,4,1,43,45,1,2,23,1,7,1,4),_HwIgmpSnoopingHostTime_Type())
hwIgmpSnoopingHostTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hwIgmpSnoopingHostTime.setStatus(_A)
_HwIgmpSnoopingGroupLimitTable_Object=MibTable
hwIgmpSnoopingGroupLimitTable=_HwIgmpSnoopingGroupLimitTable_Object((1,3,6,1,4,1,43,45,1,2,23,1,7,1,5))
if mibBuilder.loadTexts:hwIgmpSnoopingGroupLimitTable.setStatus(_A)
_HwIgmpSnoopingGroupLimitEntry_Object=MibTableRow
hwIgmpSnoopingGroupLimitEntry=_HwIgmpSnoopingGroupLimitEntry_Object((1,3,6,1,4,1,43,45,1,2,23,1,7,1,5,1))
hwIgmpSnoopingGroupLimitEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:hwIgmpSnoopingGroupLimitEntry.setStatus(_A)
_HwIgmpSnoopingGroupIfIndex_Type=InterfaceIndex
_HwIgmpSnoopingGroupIfIndex_Object=MibTableColumn
hwIgmpSnoopingGroupIfIndex=_HwIgmpSnoopingGroupIfIndex_Object((1,3,6,1,4,1,43,45,1,2,23,1,7,1,5,1,1),_HwIgmpSnoopingGroupIfIndex_Type())
hwIgmpSnoopingGroupIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hwIgmpSnoopingGroupIfIndex.setStatus(_A)
class _HwIgmpSnoopingGroupLimitNumber_Type(Unsigned32):defaultValue=4294967295
_HwIgmpSnoopingGroupLimitNumber_Type.__name__=_H
_HwIgmpSnoopingGroupLimitNumber_Object=MibTableColumn
hwIgmpSnoopingGroupLimitNumber=_HwIgmpSnoopingGroupLimitNumber_Object((1,3,6,1,4,1,43,45,1,2,23,1,7,1,5,1,2),_HwIgmpSnoopingGroupLimitNumber_Type())
hwIgmpSnoopingGroupLimitNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hwIgmpSnoopingGroupLimitNumber.setStatus(_A)
_HwIgmpSnoopingFastLeaveTable_Object=MibTable
hwIgmpSnoopingFastLeaveTable=_HwIgmpSnoopingFastLeaveTable_Object((1,3,6,1,4,1,43,45,1,2,23,1,7,1,6))
if mibBuilder.loadTexts:hwIgmpSnoopingFastLeaveTable.setStatus(_A)
_HwIgmpSnoopingFastLeaveEntry_Object=MibTableRow
hwIgmpSnoopingFastLeaveEntry=_HwIgmpSnoopingFastLeaveEntry_Object((1,3,6,1,4,1,43,45,1,2,23,1,7,1,6,1))
hwIgmpSnoopingFastLeaveEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:hwIgmpSnoopingFastLeaveEntry.setStatus(_A)
_HwIgmpSnoopingFastLeaveIfIndex_Type=InterfaceIndex
_HwIgmpSnoopingFastLeaveIfIndex_Object=MibTableColumn
hwIgmpSnoopingFastLeaveIfIndex=_HwIgmpSnoopingFastLeaveIfIndex_Object((1,3,6,1,4,1,43,45,1,2,23,1,7,1,6,1,1),_HwIgmpSnoopingFastLeaveIfIndex_Type())
hwIgmpSnoopingFastLeaveIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hwIgmpSnoopingFastLeaveIfIndex.setStatus(_A)
class _HwIgmpSnoopingFastLeaveStatus_Type(EnabledStatus):defaultValue=2
_HwIgmpSnoopingFastLeaveStatus_Type.__name__=_G
_HwIgmpSnoopingFastLeaveStatus_Object=MibTableColumn
hwIgmpSnoopingFastLeaveStatus=_HwIgmpSnoopingFastLeaveStatus_Object((1,3,6,1,4,1,43,45,1,2,23,1,7,1,6,1,2),_HwIgmpSnoopingFastLeaveStatus_Type())
hwIgmpSnoopingFastLeaveStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hwIgmpSnoopingFastLeaveStatus.setStatus(_A)
_HwIgmpSnoopingGroupPolicyTable_Object=MibTable
hwIgmpSnoopingGroupPolicyTable=_HwIgmpSnoopingGroupPolicyTable_Object((1,3,6,1,4,1,43,45,1,2,23,1,7,1,7))
if mibBuilder.loadTexts:hwIgmpSnoopingGroupPolicyTable.setStatus(_A)
_HwIgmpSnoopingGroupPolicyEntry_Object=MibTableRow
hwIgmpSnoopingGroupPolicyEntry=_HwIgmpSnoopingGroupPolicyEntry_Object((1,3,6,1,4,1,43,45,1,2,23,1,7,1,7,1))
hwIgmpSnoopingGroupPolicyEntry.setIndexNames((0,_E,_K),(0,_E,_L))
if mibBuilder.loadTexts:hwIgmpSnoopingGroupPolicyEntry.setStatus(_A)
_HwIgmpSnoopingGroupPolicyIfIndex_Type=InterfaceIndex
_HwIgmpSnoopingGroupPolicyIfIndex_Object=MibTableColumn
hwIgmpSnoopingGroupPolicyIfIndex=_HwIgmpSnoopingGroupPolicyIfIndex_Object((1,3,6,1,4,1,43,45,1,2,23,1,7,1,7,1,1),_HwIgmpSnoopingGroupPolicyIfIndex_Type())
hwIgmpSnoopingGroupPolicyIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hwIgmpSnoopingGroupPolicyIfIndex.setStatus(_A)
class _HwIgmpSnoopingGroupPolicyVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_HwIgmpSnoopingGroupPolicyVlanID_Type.__name__=_C
_HwIgmpSnoopingGroupPolicyVlanID_Object=MibTableColumn
hwIgmpSnoopingGroupPolicyVlanID=_HwIgmpSnoopingGroupPolicyVlanID_Object((1,3,6,1,4,1,43,45,1,2,23,1,7,1,7,1,2),_HwIgmpSnoopingGroupPolicyVlanID_Type())
hwIgmpSnoopingGroupPolicyVlanID.setMaxAccess(_F)
if mibBuilder.loadTexts:hwIgmpSnoopingGroupPolicyVlanID.setStatus(_A)
class _HwIgmpSnoopingGroupPolicyParameter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2000,2999))
_HwIgmpSnoopingGroupPolicyParameter_Type.__name__=_C
_HwIgmpSnoopingGroupPolicyParameter_Object=MibTableColumn
hwIgmpSnoopingGroupPolicyParameter=_HwIgmpSnoopingGroupPolicyParameter_Object((1,3,6,1,4,1,43,45,1,2,23,1,7,1,7,1,3),_HwIgmpSnoopingGroupPolicyParameter_Type())
hwIgmpSnoopingGroupPolicyParameter.setMaxAccess(_M)
if mibBuilder.loadTexts:hwIgmpSnoopingGroupPolicyParameter.setStatus(_A)
_HwIgmpSnoopingGroupPolicyStatus_Type=RowStatus
_HwIgmpSnoopingGroupPolicyStatus_Object=MibTableColumn
hwIgmpSnoopingGroupPolicyStatus=_HwIgmpSnoopingGroupPolicyStatus_Object((1,3,6,1,4,1,43,45,1,2,23,1,7,1,7,1,4),_HwIgmpSnoopingGroupPolicyStatus_Type())
hwIgmpSnoopingGroupPolicyStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:hwIgmpSnoopingGroupPolicyStatus.setStatus(_A)
_HwIgmpSnoopingNonFloodingStatus_Type=EnabledStatus
_HwIgmpSnoopingNonFloodingStatus_Object=MibScalar
hwIgmpSnoopingNonFloodingStatus=_HwIgmpSnoopingNonFloodingStatus_Object((1,3,6,1,4,1,43,45,1,2,23,1,7,1,8),_HwIgmpSnoopingNonFloodingStatus_Type())
hwIgmpSnoopingNonFloodingStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hwIgmpSnoopingNonFloodingStatus.setStatus(_A)
_HwIgmpSnoopingVlanStatusTable_Object=MibTable
hwIgmpSnoopingVlanStatusTable=_HwIgmpSnoopingVlanStatusTable_Object((1,3,6,1,4,1,43,45,1,2,23,1,7,1,9))
if mibBuilder.loadTexts:hwIgmpSnoopingVlanStatusTable.setStatus(_A)
_HwIgmpSnoopingVlanStatusEntry_Object=MibTableRow
hwIgmpSnoopingVlanStatusEntry=_HwIgmpSnoopingVlanStatusEntry_Object((1,3,6,1,4,1,43,45,1,2,23,1,7,1,9,1))
hwIgmpSnoopingVlanStatusEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:hwIgmpSnoopingVlanStatusEntry.setStatus(_A)
class _HwIgmpSnoopingVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_HwIgmpSnoopingVlanID_Type.__name__=_C
_HwIgmpSnoopingVlanID_Object=MibTableColumn
hwIgmpSnoopingVlanID=_HwIgmpSnoopingVlanID_Object((1,3,6,1,4,1,43,45,1,2,23,1,7,1,9,1,1),_HwIgmpSnoopingVlanID_Type())
hwIgmpSnoopingVlanID.setMaxAccess(_F)
if mibBuilder.loadTexts:hwIgmpSnoopingVlanID.setStatus(_A)
class _HwIgmpSnoopingVlanEnabled_Type(EnabledStatus):defaultValue=2
_HwIgmpSnoopingVlanEnabled_Type.__name__=_G
_HwIgmpSnoopingVlanEnabled_Object=MibTableColumn
hwIgmpSnoopingVlanEnabled=_HwIgmpSnoopingVlanEnabled_Object((1,3,6,1,4,1,43,45,1,2,23,1,7,1,9,1,2),_HwIgmpSnoopingVlanEnabled_Type())
hwIgmpSnoopingVlanEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:hwIgmpSnoopingVlanEnabled.setStatus(_A)
_HwIgmpSnoopingStatsObjects_ObjectIdentity=ObjectIdentity
hwIgmpSnoopingStatsObjects=_HwIgmpSnoopingStatsObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,2,23,1,7,1,10))
_HwRecvIGMPGQueryNum_Type=Counter32
_HwRecvIGMPGQueryNum_Object=MibScalar
hwRecvIGMPGQueryNum=_HwRecvIGMPGQueryNum_Object((1,3,6,1,4,1,43,45,1,2,23,1,7,1,10,1),_HwRecvIGMPGQueryNum_Type())
hwRecvIGMPGQueryNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwRecvIGMPGQueryNum.setStatus(_A)
_HwRecvIGMPSQueryNum_Type=Counter32
_HwRecvIGMPSQueryNum_Object=MibScalar
hwRecvIGMPSQueryNum=_HwRecvIGMPSQueryNum_Object((1,3,6,1,4,1,43,45,1,2,23,1,7,1,10,2),_HwRecvIGMPSQueryNum_Type())
hwRecvIGMPSQueryNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwRecvIGMPSQueryNum.setStatus(_A)
_HwRecvIGMPV1ReportNum_Type=Counter32
_HwRecvIGMPV1ReportNum_Object=MibScalar
hwRecvIGMPV1ReportNum=_HwRecvIGMPV1ReportNum_Object((1,3,6,1,4,1,43,45,1,2,23,1,7,1,10,3),_HwRecvIGMPV1ReportNum_Type())
hwRecvIGMPV1ReportNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwRecvIGMPV1ReportNum.setStatus(_A)
_HwRecvIGMPV2ReportNum_Type=Counter32
_HwRecvIGMPV2ReportNum_Object=MibScalar
hwRecvIGMPV2ReportNum=_HwRecvIGMPV2ReportNum_Object((1,3,6,1,4,1,43,45,1,2,23,1,7,1,10,4),_HwRecvIGMPV2ReportNum_Type())
hwRecvIGMPV2ReportNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwRecvIGMPV2ReportNum.setStatus(_A)
_HwRecvIGMPLeaveNum_Type=Counter32
_HwRecvIGMPLeaveNum_Object=MibScalar
hwRecvIGMPLeaveNum=_HwRecvIGMPLeaveNum_Object((1,3,6,1,4,1,43,45,1,2,23,1,7,1,10,5),_HwRecvIGMPLeaveNum_Type())
hwRecvIGMPLeaveNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwRecvIGMPLeaveNum.setStatus(_A)
_HwRecvErrorIGMPPacketNum_Type=Counter32
_HwRecvErrorIGMPPacketNum_Object=MibScalar
hwRecvErrorIGMPPacketNum=_HwRecvErrorIGMPPacketNum_Object((1,3,6,1,4,1,43,45,1,2,23,1,7,1,10,6),_HwRecvErrorIGMPPacketNum_Type())
hwRecvErrorIGMPPacketNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwRecvErrorIGMPPacketNum.setStatus(_A)
_HwSentIGMPSQueryNum_Type=Counter32
_HwSentIGMPSQueryNum_Object=MibScalar
hwSentIGMPSQueryNum=_HwSentIGMPSQueryNum_Object((1,3,6,1,4,1,43,45,1,2,23,1,7,1,10,7),_HwSentIGMPSQueryNum_Type())
hwSentIGMPSQueryNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSentIGMPSQueryNum.setStatus(_A)
class _HwIgmpSnoopingClearStats_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('clear',1),('counting',2)))
_HwIgmpSnoopingClearStats_Type.__name__=_C
_HwIgmpSnoopingClearStats_Object=MibScalar
hwIgmpSnoopingClearStats=_HwIgmpSnoopingClearStats_Object((1,3,6,1,4,1,43,45,1,2,23,1,7,1,10,8),_HwIgmpSnoopingClearStats_Type())
hwIgmpSnoopingClearStats.setMaxAccess(_B)
if mibBuilder.loadTexts:hwIgmpSnoopingClearStats.setStatus(_A)
mibBuilder.exportSymbols(_E,**{_G:EnabledStatus,'hwLswIgmpsnoopingMib':hwLswIgmpsnoopingMib,'hwLswIgmpsnoopingMibObject':hwLswIgmpsnoopingMibObject,'hwIgmpSnoopingStatus':hwIgmpSnoopingStatus,'hwIgmpSnoopingRouterPortAge':hwIgmpSnoopingRouterPortAge,'hwIgmpSnoopingResponseTime':hwIgmpSnoopingResponseTime,'hwIgmpSnoopingHostTime':hwIgmpSnoopingHostTime,'hwIgmpSnoopingGroupLimitTable':hwIgmpSnoopingGroupLimitTable,'hwIgmpSnoopingGroupLimitEntry':hwIgmpSnoopingGroupLimitEntry,_I:hwIgmpSnoopingGroupIfIndex,'hwIgmpSnoopingGroupLimitNumber':hwIgmpSnoopingGroupLimitNumber,'hwIgmpSnoopingFastLeaveTable':hwIgmpSnoopingFastLeaveTable,'hwIgmpSnoopingFastLeaveEntry':hwIgmpSnoopingFastLeaveEntry,_J:hwIgmpSnoopingFastLeaveIfIndex,'hwIgmpSnoopingFastLeaveStatus':hwIgmpSnoopingFastLeaveStatus,'hwIgmpSnoopingGroupPolicyTable':hwIgmpSnoopingGroupPolicyTable,'hwIgmpSnoopingGroupPolicyEntry':hwIgmpSnoopingGroupPolicyEntry,_K:hwIgmpSnoopingGroupPolicyIfIndex,_L:hwIgmpSnoopingGroupPolicyVlanID,'hwIgmpSnoopingGroupPolicyParameter':hwIgmpSnoopingGroupPolicyParameter,'hwIgmpSnoopingGroupPolicyStatus':hwIgmpSnoopingGroupPolicyStatus,'hwIgmpSnoopingNonFloodingStatus':hwIgmpSnoopingNonFloodingStatus,'hwIgmpSnoopingVlanStatusTable':hwIgmpSnoopingVlanStatusTable,'hwIgmpSnoopingVlanStatusEntry':hwIgmpSnoopingVlanStatusEntry,_N:hwIgmpSnoopingVlanID,'hwIgmpSnoopingVlanEnabled':hwIgmpSnoopingVlanEnabled,'hwIgmpSnoopingStatsObjects':hwIgmpSnoopingStatsObjects,'hwRecvIGMPGQueryNum':hwRecvIGMPGQueryNum,'hwRecvIGMPSQueryNum':hwRecvIGMPSQueryNum,'hwRecvIGMPV1ReportNum':hwRecvIGMPV1ReportNum,'hwRecvIGMPV2ReportNum':hwRecvIGMPV2ReportNum,'hwRecvIGMPLeaveNum':hwRecvIGMPLeaveNum,'hwRecvErrorIGMPPacketNum':hwRecvErrorIGMPPacketNum,'hwSentIGMPSQueryNum':hwSentIGMPSQueryNum,'hwIgmpSnoopingClearStats':hwIgmpSnoopingClearStats})