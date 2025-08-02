_J='EtsAdminStatusReasonType'
_I='rlEtsPriorityGroupMapping8021QPrio'
_H='NETGEAR-RADLAN-ETS-MIB'
_G='TruthValue'
_F='OctetString'
_E='read-only'
_D='EtsPriorityGroupType'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
Percents,rnd=mibBuilder.importSymbols('NETGEAR-RADLAN-MIB','Percents','rnd')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowPointer,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowPointer','RowStatus','TextualConvention',_G)
rlEtsMib=ModuleIdentity((1,3,6,1,4,1,4526,17,201))
class EtsPriorityGroupType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,15)));namedValues=NamedValues(*(('priorityGroup0',0),('priorityGroup1',1),('priorityGroup2',2),('priorityGroup3',3),('priorityGroup4',4),('priorityGroup5',5),('priorityGroup6',6),('priorityGroup7',7),('priorityGroup15',15)))
class EtsAdminStatusReasonType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ok',1),('too-many-groups',2),('too-many-queues',3),('not-highest-queue',4)))
class _RlEtsFeatureStatus_Type(TruthValue):defaultValue=2
_RlEtsFeatureStatus_Type.__name__=_G
_RlEtsFeatureStatus_Object=MibScalar
rlEtsFeatureStatus=_RlEtsFeatureStatus_Object((1,3,6,1,4,1,4526,17,201,1),_RlEtsFeatureStatus_Type())
rlEtsFeatureStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlEtsFeatureStatus.setStatus(_A)
_RlEtsPriorityGroupMappingTable_Object=MibTable
rlEtsPriorityGroupMappingTable=_RlEtsPriorityGroupMappingTable_Object((1,3,6,1,4,1,4526,17,201,2))
if mibBuilder.loadTexts:rlEtsPriorityGroupMappingTable.setStatus(_A)
_RlEtsPriorityGroupMappingEntry_Object=MibTableRow
rlEtsPriorityGroupMappingEntry=_RlEtsPriorityGroupMappingEntry_Object((1,3,6,1,4,1,4526,17,201,2,1))
rlEtsPriorityGroupMappingEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:rlEtsPriorityGroupMappingEntry.setStatus(_A)
class _RlEtsPriorityGroupMapping8021QPrio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RlEtsPriorityGroupMapping8021QPrio_Type.__name__=_C
_RlEtsPriorityGroupMapping8021QPrio_Object=MibTableColumn
rlEtsPriorityGroupMapping8021QPrio=_RlEtsPriorityGroupMapping8021QPrio_Object((1,3,6,1,4,1,4526,17,201,2,1,1),_RlEtsPriorityGroupMapping8021QPrio_Type())
rlEtsPriorityGroupMapping8021QPrio.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rlEtsPriorityGroupMapping8021QPrio.setStatus(_A)
class _RlEtsPriorityGroupMappingAdminPG_Type(EtsPriorityGroupType):defaultValue=15
_RlEtsPriorityGroupMappingAdminPG_Type.__name__=_D
_RlEtsPriorityGroupMappingAdminPG_Object=MibTableColumn
rlEtsPriorityGroupMappingAdminPG=_RlEtsPriorityGroupMappingAdminPG_Object((1,3,6,1,4,1,4526,17,201,2,1,2),_RlEtsPriorityGroupMappingAdminPG_Type())
rlEtsPriorityGroupMappingAdminPG.setMaxAccess(_B)
if mibBuilder.loadTexts:rlEtsPriorityGroupMappingAdminPG.setStatus(_A)
class _RlEtsPriorityGroupMappingOperPG_Type(EtsPriorityGroupType):defaultValue=15
_RlEtsPriorityGroupMappingOperPG_Type.__name__=_D
_RlEtsPriorityGroupMappingOperPG_Object=MibTableColumn
rlEtsPriorityGroupMappingOperPG=_RlEtsPriorityGroupMappingOperPG_Object((1,3,6,1,4,1,4526,17,201,2,1,3),_RlEtsPriorityGroupMappingOperPG_Type())
rlEtsPriorityGroupMappingOperPG.setMaxAccess(_E)
if mibBuilder.loadTexts:rlEtsPriorityGroupMappingOperPG.setStatus(_A)
_RlEtsPriorityGroupMappingStatus_Type=RowStatus
_RlEtsPriorityGroupMappingStatus_Object=MibTableColumn
rlEtsPriorityGroupMappingStatus=_RlEtsPriorityGroupMappingStatus_Object((1,3,6,1,4,1,4526,17,201,2,1,4),_RlEtsPriorityGroupMappingStatus_Type())
rlEtsPriorityGroupMappingStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlEtsPriorityGroupMappingStatus.setStatus(_A)
class _RlEtsPriorityGroupMappingProblemReason_Type(EtsAdminStatusReasonType):defaultValue=1
_RlEtsPriorityGroupMappingProblemReason_Type.__name__=_J
_RlEtsPriorityGroupMappingProblemReason_Object=MibScalar
rlEtsPriorityGroupMappingProblemReason=_RlEtsPriorityGroupMappingProblemReason_Object((1,3,6,1,4,1,4526,17,201,3),_RlEtsPriorityGroupMappingProblemReason_Type())
rlEtsPriorityGroupMappingProblemReason.setMaxAccess(_E)
if mibBuilder.loadTexts:rlEtsPriorityGroupMappingProblemReason.setStatus(_A)
class _RlEtsPriorityGroupMappingProblemIndex_Type(Integer32):defaultValue=0
_RlEtsPriorityGroupMappingProblemIndex_Type.__name__=_C
_RlEtsPriorityGroupMappingProblemIndex_Object=MibScalar
rlEtsPriorityGroupMappingProblemIndex=_RlEtsPriorityGroupMappingProblemIndex_Object((1,3,6,1,4,1,4526,17,201,4),_RlEtsPriorityGroupMappingProblemIndex_Type())
rlEtsPriorityGroupMappingProblemIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rlEtsPriorityGroupMappingProblemIndex.setStatus(_A)
class _RlEtsPriorityGroupBwAlloc_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_RlEtsPriorityGroupBwAlloc_Type.__name__=_F
_RlEtsPriorityGroupBwAlloc_Object=MibScalar
rlEtsPriorityGroupBwAlloc=_RlEtsPriorityGroupBwAlloc_Object((1,3,6,1,4,1,4526,17,201,5),_RlEtsPriorityGroupBwAlloc_Type())
rlEtsPriorityGroupBwAlloc.setMaxAccess(_B)
if mibBuilder.loadTexts:rlEtsPriorityGroupBwAlloc.setStatus(_A)
mibBuilder.exportSymbols(_H,**{_D:EtsPriorityGroupType,_J:EtsAdminStatusReasonType,'rlEtsMib':rlEtsMib,'rlEtsFeatureStatus':rlEtsFeatureStatus,'rlEtsPriorityGroupMappingTable':rlEtsPriorityGroupMappingTable,'rlEtsPriorityGroupMappingEntry':rlEtsPriorityGroupMappingEntry,_I:rlEtsPriorityGroupMapping8021QPrio,'rlEtsPriorityGroupMappingAdminPG':rlEtsPriorityGroupMappingAdminPG,'rlEtsPriorityGroupMappingOperPG':rlEtsPriorityGroupMappingOperPG,'rlEtsPriorityGroupMappingStatus':rlEtsPriorityGroupMappingStatus,'rlEtsPriorityGroupMappingProblemReason':rlEtsPriorityGroupMappingProblemReason,'rlEtsPriorityGroupMappingProblemIndex':rlEtsPriorityGroupMappingProblemIndex,'rlEtsPriorityGroupBwAlloc':rlEtsPriorityGroupBwAlloc})