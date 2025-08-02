_N='hpnicfIgmpSnoopingVlanID'
_M='read-create'
_L='hpnicfIgmpSnoopingGroupPolicyVlanID'
_K='hpnicfIgmpSnoopingGroupPolicyIfIndex'
_J='hpnicfIgmpSnoopingFastLeaveIfIndex'
_I='hpnicfIgmpSnoopingGroupIfIndex'
_H='Unsigned32'
_G='EnabledStatus'
_F='not-accessible'
_E='HPN-ICF-LswIGSP-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicflswCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicflswCommon')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hpnicfLswIgmpsnoopingMib=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,8,35,7))
if mibBuilder.loadTexts:hpnicfLswIgmpsnoopingMib.setRevisions(('2001-06-29 00:00',))
class EnabledStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_HpnicfLswIgmpsnoopingMibObject_ObjectIdentity=ObjectIdentity
hpnicfLswIgmpsnoopingMibObject=_HpnicfLswIgmpsnoopingMibObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,35,7,1))
_HpnicfIgmpSnoopingStatus_Type=EnabledStatus
_HpnicfIgmpSnoopingStatus_Object=MibScalar
hpnicfIgmpSnoopingStatus=_HpnicfIgmpSnoopingStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,7,1,1),_HpnicfIgmpSnoopingStatus_Type())
hpnicfIgmpSnoopingStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIgmpSnoopingStatus.setStatus(_A)
class _HpnicfIgmpSnoopingRouterPortAge_Type(Integer32):defaultValue=105;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_HpnicfIgmpSnoopingRouterPortAge_Type.__name__=_C
_HpnicfIgmpSnoopingRouterPortAge_Object=MibScalar
hpnicfIgmpSnoopingRouterPortAge=_HpnicfIgmpSnoopingRouterPortAge_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,7,1,2),_HpnicfIgmpSnoopingRouterPortAge_Type())
hpnicfIgmpSnoopingRouterPortAge.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIgmpSnoopingRouterPortAge.setStatus(_A)
class _HpnicfIgmpSnoopingResponseTime_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,25))
_HpnicfIgmpSnoopingResponseTime_Type.__name__=_C
_HpnicfIgmpSnoopingResponseTime_Object=MibScalar
hpnicfIgmpSnoopingResponseTime=_HpnicfIgmpSnoopingResponseTime_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,7,1,3),_HpnicfIgmpSnoopingResponseTime_Type())
hpnicfIgmpSnoopingResponseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIgmpSnoopingResponseTime.setStatus(_A)
class _HpnicfIgmpSnoopingHostTime_Type(Integer32):defaultValue=260;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,1000))
_HpnicfIgmpSnoopingHostTime_Type.__name__=_C
_HpnicfIgmpSnoopingHostTime_Object=MibScalar
hpnicfIgmpSnoopingHostTime=_HpnicfIgmpSnoopingHostTime_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,7,1,4),_HpnicfIgmpSnoopingHostTime_Type())
hpnicfIgmpSnoopingHostTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIgmpSnoopingHostTime.setStatus(_A)
_HpnicfIgmpSnoopingGroupLimitTable_Object=MibTable
hpnicfIgmpSnoopingGroupLimitTable=_HpnicfIgmpSnoopingGroupLimitTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,7,1,5))
if mibBuilder.loadTexts:hpnicfIgmpSnoopingGroupLimitTable.setStatus(_A)
_HpnicfIgmpSnoopingGroupLimitEntry_Object=MibTableRow
hpnicfIgmpSnoopingGroupLimitEntry=_HpnicfIgmpSnoopingGroupLimitEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,7,1,5,1))
hpnicfIgmpSnoopingGroupLimitEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:hpnicfIgmpSnoopingGroupLimitEntry.setStatus(_A)
_HpnicfIgmpSnoopingGroupIfIndex_Type=InterfaceIndex
_HpnicfIgmpSnoopingGroupIfIndex_Object=MibTableColumn
hpnicfIgmpSnoopingGroupIfIndex=_HpnicfIgmpSnoopingGroupIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,7,1,5,1,1),_HpnicfIgmpSnoopingGroupIfIndex_Type())
hpnicfIgmpSnoopingGroupIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIgmpSnoopingGroupIfIndex.setStatus(_A)
class _HpnicfIgmpSnoopingGroupLimitNumber_Type(Unsigned32):defaultValue=4294967295
_HpnicfIgmpSnoopingGroupLimitNumber_Type.__name__=_H
_HpnicfIgmpSnoopingGroupLimitNumber_Object=MibTableColumn
hpnicfIgmpSnoopingGroupLimitNumber=_HpnicfIgmpSnoopingGroupLimitNumber_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,7,1,5,1,2),_HpnicfIgmpSnoopingGroupLimitNumber_Type())
hpnicfIgmpSnoopingGroupLimitNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIgmpSnoopingGroupLimitNumber.setStatus(_A)
_HpnicfIgmpSnoopingFastLeaveTable_Object=MibTable
hpnicfIgmpSnoopingFastLeaveTable=_HpnicfIgmpSnoopingFastLeaveTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,7,1,6))
if mibBuilder.loadTexts:hpnicfIgmpSnoopingFastLeaveTable.setStatus(_A)
_HpnicfIgmpSnoopingFastLeaveEntry_Object=MibTableRow
hpnicfIgmpSnoopingFastLeaveEntry=_HpnicfIgmpSnoopingFastLeaveEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,7,1,6,1))
hpnicfIgmpSnoopingFastLeaveEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:hpnicfIgmpSnoopingFastLeaveEntry.setStatus(_A)
_HpnicfIgmpSnoopingFastLeaveIfIndex_Type=InterfaceIndex
_HpnicfIgmpSnoopingFastLeaveIfIndex_Object=MibTableColumn
hpnicfIgmpSnoopingFastLeaveIfIndex=_HpnicfIgmpSnoopingFastLeaveIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,7,1,6,1,1),_HpnicfIgmpSnoopingFastLeaveIfIndex_Type())
hpnicfIgmpSnoopingFastLeaveIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIgmpSnoopingFastLeaveIfIndex.setStatus(_A)
class _HpnicfIgmpSnoopingFastLeaveStatus_Type(EnabledStatus):defaultValue=2
_HpnicfIgmpSnoopingFastLeaveStatus_Type.__name__=_G
_HpnicfIgmpSnoopingFastLeaveStatus_Object=MibTableColumn
hpnicfIgmpSnoopingFastLeaveStatus=_HpnicfIgmpSnoopingFastLeaveStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,7,1,6,1,2),_HpnicfIgmpSnoopingFastLeaveStatus_Type())
hpnicfIgmpSnoopingFastLeaveStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIgmpSnoopingFastLeaveStatus.setStatus(_A)
_HpnicfIgmpSnoopingGroupPolicyTable_Object=MibTable
hpnicfIgmpSnoopingGroupPolicyTable=_HpnicfIgmpSnoopingGroupPolicyTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,7,1,7))
if mibBuilder.loadTexts:hpnicfIgmpSnoopingGroupPolicyTable.setStatus(_A)
_HpnicfIgmpSnoopingGroupPolicyEntry_Object=MibTableRow
hpnicfIgmpSnoopingGroupPolicyEntry=_HpnicfIgmpSnoopingGroupPolicyEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,7,1,7,1))
hpnicfIgmpSnoopingGroupPolicyEntry.setIndexNames((0,_E,_K),(0,_E,_L))
if mibBuilder.loadTexts:hpnicfIgmpSnoopingGroupPolicyEntry.setStatus(_A)
_HpnicfIgmpSnoopingGroupPolicyIfIndex_Type=InterfaceIndex
_HpnicfIgmpSnoopingGroupPolicyIfIndex_Object=MibTableColumn
hpnicfIgmpSnoopingGroupPolicyIfIndex=_HpnicfIgmpSnoopingGroupPolicyIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,7,1,7,1,1),_HpnicfIgmpSnoopingGroupPolicyIfIndex_Type())
hpnicfIgmpSnoopingGroupPolicyIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIgmpSnoopingGroupPolicyIfIndex.setStatus(_A)
class _HpnicfIgmpSnoopingGroupPolicyVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_HpnicfIgmpSnoopingGroupPolicyVlanID_Type.__name__=_C
_HpnicfIgmpSnoopingGroupPolicyVlanID_Object=MibTableColumn
hpnicfIgmpSnoopingGroupPolicyVlanID=_HpnicfIgmpSnoopingGroupPolicyVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,7,1,7,1,2),_HpnicfIgmpSnoopingGroupPolicyVlanID_Type())
hpnicfIgmpSnoopingGroupPolicyVlanID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIgmpSnoopingGroupPolicyVlanID.setStatus(_A)
class _HpnicfIgmpSnoopingGroupPolicyParameter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2000,2999))
_HpnicfIgmpSnoopingGroupPolicyParameter_Type.__name__=_C
_HpnicfIgmpSnoopingGroupPolicyParameter_Object=MibTableColumn
hpnicfIgmpSnoopingGroupPolicyParameter=_HpnicfIgmpSnoopingGroupPolicyParameter_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,7,1,7,1,3),_HpnicfIgmpSnoopingGroupPolicyParameter_Type())
hpnicfIgmpSnoopingGroupPolicyParameter.setMaxAccess(_M)
if mibBuilder.loadTexts:hpnicfIgmpSnoopingGroupPolicyParameter.setStatus(_A)
_HpnicfIgmpSnoopingGroupPolicyStatus_Type=RowStatus
_HpnicfIgmpSnoopingGroupPolicyStatus_Object=MibTableColumn
hpnicfIgmpSnoopingGroupPolicyStatus=_HpnicfIgmpSnoopingGroupPolicyStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,7,1,7,1,4),_HpnicfIgmpSnoopingGroupPolicyStatus_Type())
hpnicfIgmpSnoopingGroupPolicyStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:hpnicfIgmpSnoopingGroupPolicyStatus.setStatus(_A)
_HpnicfIgmpSnoopingNonFloodingStatus_Type=EnabledStatus
_HpnicfIgmpSnoopingNonFloodingStatus_Object=MibScalar
hpnicfIgmpSnoopingNonFloodingStatus=_HpnicfIgmpSnoopingNonFloodingStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,7,1,8),_HpnicfIgmpSnoopingNonFloodingStatus_Type())
hpnicfIgmpSnoopingNonFloodingStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIgmpSnoopingNonFloodingStatus.setStatus(_A)
_HpnicfIgmpSnoopingVlanStatusTable_Object=MibTable
hpnicfIgmpSnoopingVlanStatusTable=_HpnicfIgmpSnoopingVlanStatusTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,7,1,9))
if mibBuilder.loadTexts:hpnicfIgmpSnoopingVlanStatusTable.setStatus(_A)
_HpnicfIgmpSnoopingVlanStatusEntry_Object=MibTableRow
hpnicfIgmpSnoopingVlanStatusEntry=_HpnicfIgmpSnoopingVlanStatusEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,7,1,9,1))
hpnicfIgmpSnoopingVlanStatusEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:hpnicfIgmpSnoopingVlanStatusEntry.setStatus(_A)
class _HpnicfIgmpSnoopingVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_HpnicfIgmpSnoopingVlanID_Type.__name__=_C
_HpnicfIgmpSnoopingVlanID_Object=MibTableColumn
hpnicfIgmpSnoopingVlanID=_HpnicfIgmpSnoopingVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,7,1,9,1,1),_HpnicfIgmpSnoopingVlanID_Type())
hpnicfIgmpSnoopingVlanID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIgmpSnoopingVlanID.setStatus(_A)
class _HpnicfIgmpSnoopingVlanEnabled_Type(EnabledStatus):defaultValue=2
_HpnicfIgmpSnoopingVlanEnabled_Type.__name__=_G
_HpnicfIgmpSnoopingVlanEnabled_Object=MibTableColumn
hpnicfIgmpSnoopingVlanEnabled=_HpnicfIgmpSnoopingVlanEnabled_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,7,1,9,1,2),_HpnicfIgmpSnoopingVlanEnabled_Type())
hpnicfIgmpSnoopingVlanEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIgmpSnoopingVlanEnabled.setStatus(_A)
_HpnicfIgmpSnoopingStatsObjects_ObjectIdentity=ObjectIdentity
hpnicfIgmpSnoopingStatsObjects=_HpnicfIgmpSnoopingStatsObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,35,7,1,10))
_HpnicfRecvIGMPGQueryNum_Type=Counter32
_HpnicfRecvIGMPGQueryNum_Object=MibScalar
hpnicfRecvIGMPGQueryNum=_HpnicfRecvIGMPGQueryNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,7,1,10,1),_HpnicfRecvIGMPGQueryNum_Type())
hpnicfRecvIGMPGQueryNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfRecvIGMPGQueryNum.setStatus(_A)
_HpnicfRecvIGMPSQueryNum_Type=Counter32
_HpnicfRecvIGMPSQueryNum_Object=MibScalar
hpnicfRecvIGMPSQueryNum=_HpnicfRecvIGMPSQueryNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,7,1,10,2),_HpnicfRecvIGMPSQueryNum_Type())
hpnicfRecvIGMPSQueryNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfRecvIGMPSQueryNum.setStatus(_A)
_HpnicfRecvIGMPV1ReportNum_Type=Counter32
_HpnicfRecvIGMPV1ReportNum_Object=MibScalar
hpnicfRecvIGMPV1ReportNum=_HpnicfRecvIGMPV1ReportNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,7,1,10,3),_HpnicfRecvIGMPV1ReportNum_Type())
hpnicfRecvIGMPV1ReportNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfRecvIGMPV1ReportNum.setStatus(_A)
_HpnicfRecvIGMPV2ReportNum_Type=Counter32
_HpnicfRecvIGMPV2ReportNum_Object=MibScalar
hpnicfRecvIGMPV2ReportNum=_HpnicfRecvIGMPV2ReportNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,7,1,10,4),_HpnicfRecvIGMPV2ReportNum_Type())
hpnicfRecvIGMPV2ReportNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfRecvIGMPV2ReportNum.setStatus(_A)
_HpnicfRecvIGMPLeaveNum_Type=Counter32
_HpnicfRecvIGMPLeaveNum_Object=MibScalar
hpnicfRecvIGMPLeaveNum=_HpnicfRecvIGMPLeaveNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,7,1,10,5),_HpnicfRecvIGMPLeaveNum_Type())
hpnicfRecvIGMPLeaveNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfRecvIGMPLeaveNum.setStatus(_A)
_HpnicfRecvErrorIGMPPacketNum_Type=Counter32
_HpnicfRecvErrorIGMPPacketNum_Object=MibScalar
hpnicfRecvErrorIGMPPacketNum=_HpnicfRecvErrorIGMPPacketNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,7,1,10,6),_HpnicfRecvErrorIGMPPacketNum_Type())
hpnicfRecvErrorIGMPPacketNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfRecvErrorIGMPPacketNum.setStatus(_A)
_HpnicfSentIGMPSQueryNum_Type=Counter32
_HpnicfSentIGMPSQueryNum_Object=MibScalar
hpnicfSentIGMPSQueryNum=_HpnicfSentIGMPSQueryNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,7,1,10,7),_HpnicfSentIGMPSQueryNum_Type())
hpnicfSentIGMPSQueryNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSentIGMPSQueryNum.setStatus(_A)
class _HpnicfIgmpSnoopingClearStats_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('clear',1),('counting',2)))
_HpnicfIgmpSnoopingClearStats_Type.__name__=_C
_HpnicfIgmpSnoopingClearStats_Object=MibScalar
hpnicfIgmpSnoopingClearStats=_HpnicfIgmpSnoopingClearStats_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,7,1,10,8),_HpnicfIgmpSnoopingClearStats_Type())
hpnicfIgmpSnoopingClearStats.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIgmpSnoopingClearStats.setStatus(_A)
mibBuilder.exportSymbols(_E,**{_G:EnabledStatus,'hpnicfLswIgmpsnoopingMib':hpnicfLswIgmpsnoopingMib,'hpnicfLswIgmpsnoopingMibObject':hpnicfLswIgmpsnoopingMibObject,'hpnicfIgmpSnoopingStatus':hpnicfIgmpSnoopingStatus,'hpnicfIgmpSnoopingRouterPortAge':hpnicfIgmpSnoopingRouterPortAge,'hpnicfIgmpSnoopingResponseTime':hpnicfIgmpSnoopingResponseTime,'hpnicfIgmpSnoopingHostTime':hpnicfIgmpSnoopingHostTime,'hpnicfIgmpSnoopingGroupLimitTable':hpnicfIgmpSnoopingGroupLimitTable,'hpnicfIgmpSnoopingGroupLimitEntry':hpnicfIgmpSnoopingGroupLimitEntry,_I:hpnicfIgmpSnoopingGroupIfIndex,'hpnicfIgmpSnoopingGroupLimitNumber':hpnicfIgmpSnoopingGroupLimitNumber,'hpnicfIgmpSnoopingFastLeaveTable':hpnicfIgmpSnoopingFastLeaveTable,'hpnicfIgmpSnoopingFastLeaveEntry':hpnicfIgmpSnoopingFastLeaveEntry,_J:hpnicfIgmpSnoopingFastLeaveIfIndex,'hpnicfIgmpSnoopingFastLeaveStatus':hpnicfIgmpSnoopingFastLeaveStatus,'hpnicfIgmpSnoopingGroupPolicyTable':hpnicfIgmpSnoopingGroupPolicyTable,'hpnicfIgmpSnoopingGroupPolicyEntry':hpnicfIgmpSnoopingGroupPolicyEntry,_K:hpnicfIgmpSnoopingGroupPolicyIfIndex,_L:hpnicfIgmpSnoopingGroupPolicyVlanID,'hpnicfIgmpSnoopingGroupPolicyParameter':hpnicfIgmpSnoopingGroupPolicyParameter,'hpnicfIgmpSnoopingGroupPolicyStatus':hpnicfIgmpSnoopingGroupPolicyStatus,'hpnicfIgmpSnoopingNonFloodingStatus':hpnicfIgmpSnoopingNonFloodingStatus,'hpnicfIgmpSnoopingVlanStatusTable':hpnicfIgmpSnoopingVlanStatusTable,'hpnicfIgmpSnoopingVlanStatusEntry':hpnicfIgmpSnoopingVlanStatusEntry,_N:hpnicfIgmpSnoopingVlanID,'hpnicfIgmpSnoopingVlanEnabled':hpnicfIgmpSnoopingVlanEnabled,'hpnicfIgmpSnoopingStatsObjects':hpnicfIgmpSnoopingStatsObjects,'hpnicfRecvIGMPGQueryNum':hpnicfRecvIGMPGQueryNum,'hpnicfRecvIGMPSQueryNum':hpnicfRecvIGMPSQueryNum,'hpnicfRecvIGMPV1ReportNum':hpnicfRecvIGMPV1ReportNum,'hpnicfRecvIGMPV2ReportNum':hpnicfRecvIGMPV2ReportNum,'hpnicfRecvIGMPLeaveNum':hpnicfRecvIGMPLeaveNum,'hpnicfRecvErrorIGMPPacketNum':hpnicfRecvErrorIGMPPacketNum,'hpnicfSentIGMPSQueryNum':hpnicfSentIGMPSQueryNum,'hpnicfIgmpSnoopingClearStats':hpnicfIgmpSnoopingClearStats})