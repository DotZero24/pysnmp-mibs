_J='obsolete'
_I='rlQcnIfStateIfIndex'
_H='read-only'
_G='not-accessible'
_F='rlQcnPriorityStatePriority'
_E='NETGEAR-RADLAN-QCN-MIB'
_D='TruthValue'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
Percents,rnd=mibBuilder.importSymbols('NETGEAR-RADLAN-MIB','Percents','rnd')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowPointer,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowPointer','RowStatus','TextualConvention',_D)
rlQcnMib=ModuleIdentity((1,3,6,1,4,1,4526,17,202))
class _RlQcnFeatureStatus_Type(TruthValue):defaultValue=2
_RlQcnFeatureStatus_Type.__name__=_D
_RlQcnFeatureStatus_Object=MibScalar
rlQcnFeatureStatus=_RlQcnFeatureStatus_Object((1,3,6,1,4,1,4526,17,202,1),_RlQcnFeatureStatus_Type())
rlQcnFeatureStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQcnFeatureStatus.setStatus(_A)
_RlQcnPriorityStateTable_Object=MibTable
rlQcnPriorityStateTable=_RlQcnPriorityStateTable_Object((1,3,6,1,4,1,4526,17,202,2))
if mibBuilder.loadTexts:rlQcnPriorityStateTable.setStatus(_A)
_RlQcnPriorityStateEntry_Object=MibTableRow
rlQcnPriorityStateEntry=_RlQcnPriorityStateEntry_Object((1,3,6,1,4,1,4526,17,202,2,1))
rlQcnPriorityStateEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:rlQcnPriorityStateEntry.setStatus(_A)
class _RlQcnPriorityStatePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RlQcnPriorityStatePriority_Type.__name__=_C
_RlQcnPriorityStatePriority_Object=MibTableColumn
rlQcnPriorityStatePriority=_RlQcnPriorityStatePriority_Object((1,3,6,1,4,1,4526,17,202,2,1,1),_RlQcnPriorityStatePriority_Type())
rlQcnPriorityStatePriority.setMaxAccess(_G)
if mibBuilder.loadTexts:rlQcnPriorityStatePriority.setStatus(_A)
class _RlQcnPriorityAdminStateEnable_Type(TruthValue):defaultValue=2
_RlQcnPriorityAdminStateEnable_Type.__name__=_D
_RlQcnPriorityAdminStateEnable_Object=MibTableColumn
rlQcnPriorityAdminStateEnable=_RlQcnPriorityAdminStateEnable_Object((1,3,6,1,4,1,4526,17,202,2,1,2),_RlQcnPriorityAdminStateEnable_Type())
rlQcnPriorityAdminStateEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQcnPriorityAdminStateEnable.setStatus(_A)
class _RlQcnPriorityOperStateEnable_Type(TruthValue):defaultValue=2
_RlQcnPriorityOperStateEnable_Type.__name__=_D
_RlQcnPriorityOperStateEnable_Object=MibTableColumn
rlQcnPriorityOperStateEnable=_RlQcnPriorityOperStateEnable_Object((1,3,6,1,4,1,4526,17,202,2,1,3),_RlQcnPriorityOperStateEnable_Type())
rlQcnPriorityOperStateEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:rlQcnPriorityOperStateEnable.setStatus(_A)
class _RlQcnPriorityAdminStateReason_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ok',1),('queue0',2),('sharedQueue',3)))
_RlQcnPriorityAdminStateReason_Type.__name__=_C
_RlQcnPriorityAdminStateReason_Object=MibTableColumn
rlQcnPriorityAdminStateReason=_RlQcnPriorityAdminStateReason_Object((1,3,6,1,4,1,4526,17,202,2,1,4),_RlQcnPriorityAdminStateReason_Type())
rlQcnPriorityAdminStateReason.setMaxAccess(_H)
if mibBuilder.loadTexts:rlQcnPriorityAdminStateReason.setStatus(_A)
_RlQcnPriorityStateStatus_Type=RowStatus
_RlQcnPriorityStateStatus_Object=MibTableColumn
rlQcnPriorityStateStatus=_RlQcnPriorityStateStatus_Object((1,3,6,1,4,1,4526,17,202,2,1,5),_RlQcnPriorityStateStatus_Type())
rlQcnPriorityStateStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQcnPriorityStateStatus.setStatus(_A)
_RlQcnIfStateTable_Object=MibTable
rlQcnIfStateTable=_RlQcnIfStateTable_Object((1,3,6,1,4,1,4526,17,202,3))
if mibBuilder.loadTexts:rlQcnIfStateTable.setStatus(_A)
_RlQcnIfStateEntry_Object=MibTableRow
rlQcnIfStateEntry=_RlQcnIfStateEntry_Object((1,3,6,1,4,1,4526,17,202,3,1))
rlQcnIfStateEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:rlQcnIfStateEntry.setStatus(_A)
_RlQcnIfStateIfIndex_Type=Integer32
_RlQcnIfStateIfIndex_Object=MibTableColumn
rlQcnIfStateIfIndex=_RlQcnIfStateIfIndex_Object((1,3,6,1,4,1,4526,17,202,3,1,1),_RlQcnIfStateIfIndex_Type())
rlQcnIfStateIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:rlQcnIfStateIfIndex.setStatus(_A)
class _RlQcnIfStateCpCreationEn_Type(TruthValue):defaultValue=2
_RlQcnIfStateCpCreationEn_Type.__name__=_D
_RlQcnIfStateCpCreationEn_Object=MibTableColumn
rlQcnIfStateCpCreationEn=_RlQcnIfStateCpCreationEn_Object((1,3,6,1,4,1,4526,17,202,3,1,2),_RlQcnIfStateCpCreationEn_Type())
rlQcnIfStateCpCreationEn.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQcnIfStateCpCreationEn.setStatus(_A)
_RlQcnIfStateStatus_Type=RowStatus
_RlQcnIfStateStatus_Object=MibTableColumn
rlQcnIfStateStatus=_RlQcnIfStateStatus_Object((1,3,6,1,4,1,4526,17,202,3,1,3),_RlQcnIfStateStatus_Type())
rlQcnIfStateStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQcnIfStateStatus.setStatus(_A)
class _RlQcnCmnPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RlQcnCmnPriority_Type.__name__=_C
_RlQcnCmnPriority_Object=MibScalar
rlQcnCmnPriority=_RlQcnCmnPriority_Object((1,3,6,1,4,1,4526,17,202,4),_RlQcnCmnPriority_Type())
rlQcnCmnPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQcnCmnPriority.setStatus(_A)
class _RlQcnCpPfcSetPoint_Type(Integer32):defaultValue=26112
_RlQcnCpPfcSetPoint_Type.__name__=_C
_RlQcnCpPfcSetPoint_Object=MibScalar
rlQcnCpPfcSetPoint=_RlQcnCpPfcSetPoint_Object((1,3,6,1,4,1,4526,17,202,5),_RlQcnCpPfcSetPoint_Type())
rlQcnCpPfcSetPoint.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQcnCpPfcSetPoint.setStatus(_J)
class _RlQcnCpNonPfcSetPoint_Type(Integer32):defaultValue=26112
_RlQcnCpNonPfcSetPoint_Type.__name__=_C
_RlQcnCpNonPfcSetPoint_Object=MibScalar
rlQcnCpNonPfcSetPoint=_RlQcnCpNonPfcSetPoint_Object((1,3,6,1,4,1,4526,17,202,6),_RlQcnCpNonPfcSetPoint_Type())
rlQcnCpNonPfcSetPoint.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQcnCpNonPfcSetPoint.setStatus(_J)
class _RlQcnCpFeedbackWeight_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-10,10))
_RlQcnCpFeedbackWeight_Type.__name__=_C
_RlQcnCpFeedbackWeight_Object=MibScalar
rlQcnCpFeedbackWeight=_RlQcnCpFeedbackWeight_Object((1,3,6,1,4,1,4526,17,202,7),_RlQcnCpFeedbackWeight_Type())
rlQcnCpFeedbackWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQcnCpFeedbackWeight.setStatus(_A)
class _RlQcnCpMinSampleBase_Type(Integer32):defaultValue=150000
_RlQcnCpMinSampleBase_Type.__name__=_C
_RlQcnCpMinSampleBase_Object=MibScalar
rlQcnCpMinSampleBase=_RlQcnCpMinSampleBase_Object((1,3,6,1,4,1,4526,17,202,8),_RlQcnCpMinSampleBase_Type())
rlQcnCpMinSampleBase.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQcnCpMinSampleBase.setStatus(_A)
class _RlQcnCpSetPoint_Type(Integer32):defaultValue=26112
_RlQcnCpSetPoint_Type.__name__=_C
_RlQcnCpSetPoint_Object=MibScalar
rlQcnCpSetPoint=_RlQcnCpSetPoint_Object((1,3,6,1,4,1,4526,17,202,9),_RlQcnCpSetPoint_Type())
rlQcnCpSetPoint.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQcnCpSetPoint.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'rlQcnMib':rlQcnMib,'rlQcnFeatureStatus':rlQcnFeatureStatus,'rlQcnPriorityStateTable':rlQcnPriorityStateTable,'rlQcnPriorityStateEntry':rlQcnPriorityStateEntry,_F:rlQcnPriorityStatePriority,'rlQcnPriorityAdminStateEnable':rlQcnPriorityAdminStateEnable,'rlQcnPriorityOperStateEnable':rlQcnPriorityOperStateEnable,'rlQcnPriorityAdminStateReason':rlQcnPriorityAdminStateReason,'rlQcnPriorityStateStatus':rlQcnPriorityStateStatus,'rlQcnIfStateTable':rlQcnIfStateTable,'rlQcnIfStateEntry':rlQcnIfStateEntry,_I:rlQcnIfStateIfIndex,'rlQcnIfStateCpCreationEn':rlQcnIfStateCpCreationEn,'rlQcnIfStateStatus':rlQcnIfStateStatus,'rlQcnCmnPriority':rlQcnCmnPriority,'rlQcnCpPfcSetPoint':rlQcnCpPfcSetPoint,'rlQcnCpNonPfcSetPoint':rlQcnCpNonPfcSetPoint,'rlQcnCpFeedbackWeight':rlQcnCpFeedbackWeight,'rlQcnCpMinSampleBase':rlQcnCpMinSampleBase,'rlQcnCpSetPoint':rlQcnCpSetPoint})