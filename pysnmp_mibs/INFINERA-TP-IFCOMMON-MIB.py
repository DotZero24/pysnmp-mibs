_O='ifCommonGroup'
_N='ifCommonAlarmInhibitState'
_M='ifCommonOpStateQualifierList'
_L='ifCommonAlarmReportControl'
_K='ifCommonAvailabilityState'
_J='ifCommonMoId'
_I='inhibited'
_H='allowed'
_G='InfnAvailabilityState'
_F='ifIndex'
_E='IF-MIB'
_D='Integer32'
_C='read-only'
_B='INFINERA-TP-IFCOMMON-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
commonTerminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','commonTerminationPoint')
InfnAvailabilityState,InfnOpsQualifierList=mibBuilder.importSymbols('INFINERA-TC-MIB',_G,'InfnOpsQualifierList')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ifCommonMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,1,10,1))
if mibBuilder.loadTexts:ifCommonMIB.setRevisions(('2008-10-20 00:00',))
_IfCommonTable_Object=MibTable
ifCommonTable=_IfCommonTable_Object((1,3,6,1,4,1,21296,2,2,1,10,1,1))
if mibBuilder.loadTexts:ifCommonTable.setStatus(_A)
_IfCommonEntry_Object=MibTableRow
ifCommonEntry=_IfCommonEntry_Object((1,3,6,1,4,1,21296,2,2,1,10,1,1,1))
ifCommonEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:ifCommonEntry.setStatus(_A)
_IfCommonMoId_Type=DisplayString
_IfCommonMoId_Object=MibTableColumn
ifCommonMoId=_IfCommonMoId_Object((1,3,6,1,4,1,21296,2,2,1,10,1,1,1,1),_IfCommonMoId_Type())
ifCommonMoId.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCommonMoId.setStatus(_A)
class _IfCommonAvailabilityState_Type(InfnAvailabilityState):defaultValue=3
_IfCommonAvailabilityState_Type.__name__=_G
_IfCommonAvailabilityState_Object=MibTableColumn
ifCommonAvailabilityState=_IfCommonAvailabilityState_Object((1,3,6,1,4,1,21296,2,2,1,10,1,1,1,2),_IfCommonAvailabilityState_Type())
ifCommonAvailabilityState.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCommonAvailabilityState.setStatus(_A)
class _IfCommonAlarmReportControl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_IfCommonAlarmReportControl_Type.__name__=_D
_IfCommonAlarmReportControl_Object=MibTableColumn
ifCommonAlarmReportControl=_IfCommonAlarmReportControl_Object((1,3,6,1,4,1,21296,2,2,1,10,1,1,1,3),_IfCommonAlarmReportControl_Type())
ifCommonAlarmReportControl.setMaxAccess('read-write')
if mibBuilder.loadTexts:ifCommonAlarmReportControl.setStatus(_A)
_IfCommonOpStateQualifierList_Type=InfnOpsQualifierList
_IfCommonOpStateQualifierList_Object=MibTableColumn
ifCommonOpStateQualifierList=_IfCommonOpStateQualifierList_Object((1,3,6,1,4,1,21296,2,2,1,10,1,1,1,4),_IfCommonOpStateQualifierList_Type())
ifCommonOpStateQualifierList.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCommonOpStateQualifierList.setStatus(_A)
class _IfCommonAlarmInhibitState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_IfCommonAlarmInhibitState_Type.__name__=_D
_IfCommonAlarmInhibitState_Object=MibTableColumn
ifCommonAlarmInhibitState=_IfCommonAlarmInhibitState_Object((1,3,6,1,4,1,21296,2,2,1,10,1,1,1,5),_IfCommonAlarmInhibitState_Type())
ifCommonAlarmInhibitState.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCommonAlarmInhibitState.setStatus(_A)
_IfCommonConformance_ObjectIdentity=ObjectIdentity
ifCommonConformance=_IfCommonConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,1,10,1,3))
_IfCommonCompliances_ObjectIdentity=ObjectIdentity
ifCommonCompliances=_IfCommonCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,1,10,1,3,1))
_IfCommonGroups_ObjectIdentity=ObjectIdentity
ifCommonGroups=_IfCommonGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,1,10,1,3,2))
ifCommonGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,1,10,1,3,2,1))
ifCommonGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:ifCommonGroup.setStatus(_A)
ifCommonCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,1,10,1,3,1,1))
ifCommonCompliance.setObjects((_B,_O))
if mibBuilder.loadTexts:ifCommonCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ifCommonMIB':ifCommonMIB,'ifCommonTable':ifCommonTable,'ifCommonEntry':ifCommonEntry,_J:ifCommonMoId,_K:ifCommonAvailabilityState,_L:ifCommonAlarmReportControl,_M:ifCommonOpStateQualifierList,_N:ifCommonAlarmInhibitState,'ifCommonConformance':ifCommonConformance,'ifCommonCompliances':ifCommonCompliances,'ifCommonCompliance':ifCommonCompliance,'ifCommonGroups':ifCommonGroups,_O:ifCommonGroup})