_H='rcAclFilterStatisticsEntry'
_G='rcAclFilterIndex'
_F='SWITCH-FILTER-MIB'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
EnableVar,PortList=mibBuilder.importSymbols('SWITCH-TC','EnableVar','PortList')
rcFilter=ModuleIdentity((1,3,6,1,4,1,8886,6,1,14))
_RcAclFilter_ObjectIdentity=ObjectIdentity
rcAclFilter=_RcAclFilter_ObjectIdentity((1,3,6,1,4,1,8886,6,1,14,1))
_RcAclFilterAction_Type=EnableVar
_RcAclFilterAction_Object=MibScalar
rcAclFilterAction=_RcAclFilterAction_Object((1,3,6,1,4,1,8886,6,1,14,1,1),_RcAclFilterAction_Type())
rcAclFilterAction.setMaxAccess(_E)
if mibBuilder.loadTexts:rcAclFilterAction.setStatus(_A)
_RcAclFilterNextIndex_Type=Integer32
_RcAclFilterNextIndex_Object=MibScalar
rcAclFilterNextIndex=_RcAclFilterNextIndex_Object((1,3,6,1,4,1,8886,6,1,14,1,2),_RcAclFilterNextIndex_Type())
rcAclFilterNextIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rcAclFilterNextIndex.setStatus(_A)
_RcAclFilterTable_Object=MibTable
rcAclFilterTable=_RcAclFilterTable_Object((1,3,6,1,4,1,8886,6,1,14,1,3))
if mibBuilder.loadTexts:rcAclFilterTable.setStatus(_A)
_RcAclFilterEntry_Object=MibTableRow
rcAclFilterEntry=_RcAclFilterEntry_Object((1,3,6,1,4,1,8886,6,1,14,1,3,1))
rcAclFilterEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:rcAclFilterEntry.setStatus(_A)
_RcAclFilterIndex_Type=Integer32
_RcAclFilterIndex_Object=MibTableColumn
rcAclFilterIndex=_RcAclFilterIndex_Object((1,3,6,1,4,1,8886,6,1,14,1,3,1,1),_RcAclFilterIndex_Type())
rcAclFilterIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rcAclFilterIndex.setStatus(_A)
class _RcAclFilterAclType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ip-acl',1),('mac-acl',2),('user-acl',3)))
_RcAclFilterAclType_Type.__name__=_D
_RcAclFilterAclType_Object=MibTableColumn
rcAclFilterAclType=_RcAclFilterAclType_Object((1,3,6,1,4,1,8886,6,1,14,1,3,1,2),_RcAclFilterAclType_Type())
rcAclFilterAclType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcAclFilterAclType.setStatus(_A)
_RcAclFilterAclNumber_Type=Integer32
_RcAclFilterAclNumber_Object=MibTableColumn
rcAclFilterAclNumber=_RcAclFilterAclNumber_Object((1,3,6,1,4,1,8886,6,1,14,1,3,1,3),_RcAclFilterAclNumber_Type())
rcAclFilterAclNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rcAclFilterAclNumber.setStatus(_A)
_RcAclFilterIngressPort_Type=Integer32
_RcAclFilterIngressPort_Object=MibTableColumn
rcAclFilterIngressPort=_RcAclFilterIngressPort_Object((1,3,6,1,4,1,8886,6,1,14,1,3,1,4),_RcAclFilterIngressPort_Type())
rcAclFilterIngressPort.setMaxAccess(_B)
if mibBuilder.loadTexts:rcAclFilterIngressPort.setStatus(_A)
_RcAclFilterEgressPort_Type=Integer32
_RcAclFilterEgressPort_Object=MibTableColumn
rcAclFilterEgressPort=_RcAclFilterEgressPort_Object((1,3,6,1,4,1,8886,6,1,14,1,3,1,5),_RcAclFilterEgressPort_Type())
rcAclFilterEgressPort.setMaxAccess(_B)
if mibBuilder.loadTexts:rcAclFilterEgressPort.setStatus(_A)
class _RcAclFilterVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_RcAclFilterVlan_Type.__name__=_D
_RcAclFilterVlan_Object=MibTableColumn
rcAclFilterVlan=_RcAclFilterVlan_Object((1,3,6,1,4,1,8886,6,1,14,1,3,1,6),_RcAclFilterVlan_Type())
rcAclFilterVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:rcAclFilterVlan.setStatus(_A)
_RcAclFilterStatus_Type=RowStatus
_RcAclFilterStatus_Object=MibTableColumn
rcAclFilterStatus=_RcAclFilterStatus_Object((1,3,6,1,4,1,8886,6,1,14,1,3,1,7),_RcAclFilterStatus_Type())
rcAclFilterStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcAclFilterStatus.setStatus(_A)
_RcAclFilterHwStatus_Type=EnableVar
_RcAclFilterHwStatus_Object=MibTableColumn
rcAclFilterHwStatus=_RcAclFilterHwStatus_Object((1,3,6,1,4,1,8886,6,1,14,1,3,1,8),_RcAclFilterHwStatus_Type())
rcAclFilterHwStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rcAclFilterHwStatus.setStatus(_A)
_RcAclFilterDoubleTagging_Type=TruthValue
_RcAclFilterDoubleTagging_Object=MibTableColumn
rcAclFilterDoubleTagging=_RcAclFilterDoubleTagging_Object((1,3,6,1,4,1,8886,6,1,14,1,3,1,9),_RcAclFilterDoubleTagging_Type())
rcAclFilterDoubleTagging.setMaxAccess(_B)
if mibBuilder.loadTexts:rcAclFilterDoubleTagging.setStatus(_A)
class _RcAclFilterVlanType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inner',1),('outer',2)))
_RcAclFilterVlanType_Type.__name__=_D
_RcAclFilterVlanType_Object=MibTableColumn
rcAclFilterVlanType=_RcAclFilterVlanType_Object((1,3,6,1,4,1,8886,6,1,14,1,3,1,10),_RcAclFilterVlanType_Type())
rcAclFilterVlanType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcAclFilterVlanType.setStatus(_A)
_RcAclFilterStatEnable_Type=EnableVar
_RcAclFilterStatEnable_Object=MibTableColumn
rcAclFilterStatEnable=_RcAclFilterStatEnable_Object((1,3,6,1,4,1,8886,6,1,14,1,3,1,11),_RcAclFilterStatEnable_Type())
rcAclFilterStatEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rcAclFilterStatEnable.setStatus(_A)
_RcAclFilterStatHwStatus_Type=EnableVar
_RcAclFilterStatHwStatus_Object=MibTableColumn
rcAclFilterStatHwStatus=_RcAclFilterStatHwStatus_Object((1,3,6,1,4,1,8886,6,1,14,1,3,1,12),_RcAclFilterStatHwStatus_Type())
rcAclFilterStatHwStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rcAclFilterStatHwStatus.setStatus(_A)
_RcAclFilterIngressPortList_Type=PortList
_RcAclFilterIngressPortList_Object=MibTableColumn
rcAclFilterIngressPortList=_RcAclFilterIngressPortList_Object((1,3,6,1,4,1,8886,6,1,14,1,3,1,14),_RcAclFilterIngressPortList_Type())
rcAclFilterIngressPortList.setMaxAccess(_E)
if mibBuilder.loadTexts:rcAclFilterIngressPortList.setStatus(_A)
_RcAclFilterStatisticsTable_Object=MibTable
rcAclFilterStatisticsTable=_RcAclFilterStatisticsTable_Object((1,3,6,1,4,1,8886,6,1,14,1,4))
if mibBuilder.loadTexts:rcAclFilterStatisticsTable.setStatus(_A)
_RcAclFilterStatisticsEntry_Object=MibTableRow
rcAclFilterStatisticsEntry=_RcAclFilterStatisticsEntry_Object((1,3,6,1,4,1,8886,6,1,14,1,4,1))
if mibBuilder.loadTexts:rcAclFilterStatisticsEntry.setStatus(_A)
_RcAclFilterCounterReset_Type=EnableVar
_RcAclFilterCounterReset_Object=MibTableColumn
rcAclFilterCounterReset=_RcAclFilterCounterReset_Object((1,3,6,1,4,1,8886,6,1,14,1,4,1,1),_RcAclFilterCounterReset_Type())
rcAclFilterCounterReset.setMaxAccess(_E)
if mibBuilder.loadTexts:rcAclFilterCounterReset.setStatus(_A)
_RcAclFilterCounterPkt64_Type=Counter64
_RcAclFilterCounterPkt64_Object=MibTableColumn
rcAclFilterCounterPkt64=_RcAclFilterCounterPkt64_Object((1,3,6,1,4,1,8886,6,1,14,1,4,1,2),_RcAclFilterCounterPkt64_Type())
rcAclFilterCounterPkt64.setMaxAccess(_C)
if mibBuilder.loadTexts:rcAclFilterCounterPkt64.setStatus(_A)
_RcAclFilterCounterByte64_Type=Counter64
_RcAclFilterCounterByte64_Object=MibTableColumn
rcAclFilterCounterByte64=_RcAclFilterCounterByte64_Object((1,3,6,1,4,1,8886,6,1,14,1,4,1,3),_RcAclFilterCounterByte64_Type())
rcAclFilterCounterByte64.setMaxAccess(_C)
if mibBuilder.loadTexts:rcAclFilterCounterByte64.setStatus(_A)
_RcAclFilterCounterStatisticUnit_Type=Integer32
_RcAclFilterCounterStatisticUnit_Object=MibTableColumn
rcAclFilterCounterStatisticUnit=_RcAclFilterCounterStatisticUnit_Object((1,3,6,1,4,1,8886,6,1,14,1,4,1,4),_RcAclFilterCounterStatisticUnit_Type())
rcAclFilterCounterStatisticUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:rcAclFilterCounterStatisticUnit.setStatus(_A)
rcAclFilterEntry.registerAugmentions((_F,_H))
rcAclFilterStatisticsEntry.setIndexNames(*rcAclFilterEntry.getIndexNames())
mibBuilder.exportSymbols(_F,**{'rcFilter':rcFilter,'rcAclFilter':rcAclFilter,'rcAclFilterAction':rcAclFilterAction,'rcAclFilterNextIndex':rcAclFilterNextIndex,'rcAclFilterTable':rcAclFilterTable,'rcAclFilterEntry':rcAclFilterEntry,_G:rcAclFilterIndex,'rcAclFilterAclType':rcAclFilterAclType,'rcAclFilterAclNumber':rcAclFilterAclNumber,'rcAclFilterIngressPort':rcAclFilterIngressPort,'rcAclFilterEgressPort':rcAclFilterEgressPort,'rcAclFilterVlan':rcAclFilterVlan,'rcAclFilterStatus':rcAclFilterStatus,'rcAclFilterHwStatus':rcAclFilterHwStatus,'rcAclFilterDoubleTagging':rcAclFilterDoubleTagging,'rcAclFilterVlanType':rcAclFilterVlanType,'rcAclFilterStatEnable':rcAclFilterStatEnable,'rcAclFilterStatHwStatus':rcAclFilterStatHwStatus,'rcAclFilterIngressPortList':rcAclFilterIngressPortList,'rcAclFilterStatisticsTable':rcAclFilterStatisticsTable,_H:rcAclFilterStatisticsEntry,'rcAclFilterCounterReset':rcAclFilterCounterReset,'rcAclFilterCounterPkt64':rcAclFilterCounterPkt64,'rcAclFilterCounterByte64':rcAclFilterCounterByte64,'rcAclFilterCounterStatisticUnit':rcAclFilterCounterStatisticUnit})