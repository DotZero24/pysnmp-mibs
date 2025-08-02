_R='arcSettingGroup'
_Q='arcCDTimeInterval'
_P='arcTITimeInterval'
_O='arcStorageType'
_N='arcRowStatus'
_M='arcState'
_L='arcNotificationId'
_K='arcAlarmType'
_J='arcIndex'
_I='read-write'
_H='StorageType'
_G='Integer32'
_F='arcNalmTimeRemaining'
_E='not-accessible'
_D='seconds'
_C='read-create'
_B='ARC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ResourceId,=mibBuilder.importSymbols('ALARM-MIB','ResourceId')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_H,'TextualConvention')
arcMibModule=ModuleIdentity((1,3,6,1,2,1,117))
if mibBuilder.loadTexts:arcMibModule.setRevisions(('2004-09-09 00:00',))
class IANAItuProbableCauseOrZero(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ArcTimeIntervals_ObjectIdentity=ObjectIdentity
arcTimeIntervals=_ArcTimeIntervals_ObjectIdentity((1,3,6,1,2,1,117,1))
_ArcTITimeInterval_Type=Unsigned32
_ArcTITimeInterval_Object=MibScalar
arcTITimeInterval=_ArcTITimeInterval_Object((1,3,6,1,2,1,117,1,1),_ArcTITimeInterval_Type())
arcTITimeInterval.setMaxAccess(_I)
if mibBuilder.loadTexts:arcTITimeInterval.setStatus(_A)
if mibBuilder.loadTexts:arcTITimeInterval.setUnits(_D)
_ArcCDTimeInterval_Type=Unsigned32
_ArcCDTimeInterval_Object=MibScalar
arcCDTimeInterval=_ArcCDTimeInterval_Object((1,3,6,1,2,1,117,1,2),_ArcCDTimeInterval_Type())
arcCDTimeInterval.setMaxAccess(_I)
if mibBuilder.loadTexts:arcCDTimeInterval.setStatus(_A)
if mibBuilder.loadTexts:arcCDTimeInterval.setUnits(_D)
_ArcObjects_ObjectIdentity=ObjectIdentity
arcObjects=_ArcObjects_ObjectIdentity((1,3,6,1,2,1,117,2))
_ArcTable_Object=MibTable
arcTable=_ArcTable_Object((1,3,6,1,2,1,117,2,1))
if mibBuilder.loadTexts:arcTable.setStatus(_A)
_ArcEntry_Object=MibTableRow
arcEntry=_ArcEntry_Object((1,3,6,1,2,1,117,2,1,1))
arcEntry.setIndexNames((0,_B,_J),(0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:arcEntry.setStatus(_A)
_ArcIndex_Type=ResourceId
_ArcIndex_Object=MibTableColumn
arcIndex=_ArcIndex_Object((1,3,6,1,2,1,117,2,1,1,1),_ArcIndex_Type())
arcIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:arcIndex.setStatus(_A)
_ArcAlarmType_Type=IANAItuProbableCauseOrZero
_ArcAlarmType_Object=MibTableColumn
arcAlarmType=_ArcAlarmType_Object((1,3,6,1,2,1,117,2,1,1,2),_ArcAlarmType_Type())
arcAlarmType.setMaxAccess(_E)
if mibBuilder.loadTexts:arcAlarmType.setStatus(_A)
_ArcNotificationId_Type=ObjectIdentifier
_ArcNotificationId_Object=MibTableColumn
arcNotificationId=_ArcNotificationId_Object((1,3,6,1,2,1,117,2,1,1,3),_ArcNotificationId_Type())
arcNotificationId.setMaxAccess(_E)
if mibBuilder.loadTexts:arcNotificationId.setStatus(_A)
class _ArcState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('nalm',1),('nalmQI',2),('nalmTI',3),('nalmQICD',4)))
_ArcState_Type.__name__=_G
_ArcState_Object=MibTableColumn
arcState=_ArcState_Object((1,3,6,1,2,1,117,2,1,1,4),_ArcState_Type())
arcState.setMaxAccess(_C)
if mibBuilder.loadTexts:arcState.setStatus(_A)
_ArcNalmTimeRemaining_Type=Unsigned32
_ArcNalmTimeRemaining_Object=MibTableColumn
arcNalmTimeRemaining=_ArcNalmTimeRemaining_Object((1,3,6,1,2,1,117,2,1,1,5),_ArcNalmTimeRemaining_Type())
arcNalmTimeRemaining.setMaxAccess(_C)
if mibBuilder.loadTexts:arcNalmTimeRemaining.setStatus(_A)
if mibBuilder.loadTexts:arcNalmTimeRemaining.setUnits(_D)
_ArcRowStatus_Type=RowStatus
_ArcRowStatus_Object=MibTableColumn
arcRowStatus=_ArcRowStatus_Object((1,3,6,1,2,1,117,2,1,1,6),_ArcRowStatus_Type())
arcRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:arcRowStatus.setStatus(_A)
class _ArcStorageType_Type(StorageType):defaultValue=3
_ArcStorageType_Type.__name__=_H
_ArcStorageType_Object=MibTableColumn
arcStorageType=_ArcStorageType_Object((1,3,6,1,2,1,117,2,1,1,7),_ArcStorageType_Type())
arcStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:arcStorageType.setStatus(_A)
_ArcConformance_ObjectIdentity=ObjectIdentity
arcConformance=_ArcConformance_ObjectIdentity((1,3,6,1,2,1,117,3))
_ArcCompliances_ObjectIdentity=ObjectIdentity
arcCompliances=_ArcCompliances_ObjectIdentity((1,3,6,1,2,1,117,3,1))
_ArcGroups_ObjectIdentity=ObjectIdentity
arcGroups=_ArcGroups_ObjectIdentity((1,3,6,1,2,1,117,3,2))
arcSettingGroup=ObjectGroup((1,3,6,1,2,1,117,3,2,1))
arcSettingGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:arcSettingGroup.setStatus(_A)
arcTIGroup=ObjectGroup((1,3,6,1,2,1,117,3,2,2))
arcTIGroup.setObjects(*((_B,_P),(_B,_F)))
if mibBuilder.loadTexts:arcTIGroup.setStatus(_A)
arcQICDGroup=ObjectGroup((1,3,6,1,2,1,117,3,2,3))
arcQICDGroup.setObjects(*((_B,_Q),(_B,_F)))
if mibBuilder.loadTexts:arcQICDGroup.setStatus(_A)
arcCompliance=ModuleCompliance((1,3,6,1,2,1,117,3,1,1))
arcCompliance.setObjects((_B,_R))
if mibBuilder.loadTexts:arcCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'IANAItuProbableCauseOrZero':IANAItuProbableCauseOrZero,'arcMibModule':arcMibModule,'arcTimeIntervals':arcTimeIntervals,_P:arcTITimeInterval,_Q:arcCDTimeInterval,'arcObjects':arcObjects,'arcTable':arcTable,'arcEntry':arcEntry,_J:arcIndex,_K:arcAlarmType,_L:arcNotificationId,_M:arcState,_F:arcNalmTimeRemaining,_N:arcRowStatus,_O:arcStorageType,'arcConformance':arcConformance,'arcCompliances':arcCompliances,'arcCompliance':arcCompliance,'arcGroups':arcGroups,_R:arcSettingGroup,'arcTIGroup':arcTIGroup,'arcQICDGroup':arcQICDGroup})