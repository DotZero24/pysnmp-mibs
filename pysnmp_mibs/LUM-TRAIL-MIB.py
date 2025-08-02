_O='trailStatusGroupV2'
_N='trailStatusGroup'
_M='trailStatusDown'
_L='trailStatusDegraded'
_K='trailGeneralStatusTableSize'
_J='trailGeneralStateLastChangeTime'
_I='trailGeneralConfigLastChangeTime'
_H='Unsigned32'
_G='trailGeneralGroup'
_F='trailStatusIncomplete'
_E='deprecated'
_D='trailStatusIndex'
_C='read-only'
_B='current'
_A='LUM-TRAIL-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumModules,lumTrailMIB=mibBuilder.importSymbols('LUM-REG','lumModules','lumTrailMIB')
FaultStatus,=mibBuilder.importSymbols('LUM-TC','FaultStatus')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
lumTrailMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,38))
if mibBuilder.loadTexts:lumTrailMIBModule.setRevisions(('2017-06-15 00:00','2011-04-13 00:00'))
_LumTrailConfs_ObjectIdentity=ObjectIdentity
lumTrailConfs=_LumTrailConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,38,1))
_LumTrailGroups_ObjectIdentity=ObjectIdentity
lumTrailGroups=_LumTrailGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,38,1,1))
_LumTrailCompl_ObjectIdentity=ObjectIdentity
lumTrailCompl=_LumTrailCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,38,1,2))
_LumTrailMIBObjects_ObjectIdentity=ObjectIdentity
lumTrailMIBObjects=_LumTrailMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,38,2))
_TrailGeneral_ObjectIdentity=ObjectIdentity
trailGeneral=_TrailGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,38,2,1))
_TrailGeneralConfigLastChangeTime_Type=DateAndTime
_TrailGeneralConfigLastChangeTime_Object=MibScalar
trailGeneralConfigLastChangeTime=_TrailGeneralConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,38,2,1,1),_TrailGeneralConfigLastChangeTime_Type())
trailGeneralConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:trailGeneralConfigLastChangeTime.setStatus(_B)
_TrailGeneralStateLastChangeTime_Type=DateAndTime
_TrailGeneralStateLastChangeTime_Object=MibScalar
trailGeneralStateLastChangeTime=_TrailGeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,38,2,1,2),_TrailGeneralStateLastChangeTime_Type())
trailGeneralStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:trailGeneralStateLastChangeTime.setStatus(_B)
_TrailGeneralStatusTableSize_Type=Unsigned32
_TrailGeneralStatusTableSize_Object=MibScalar
trailGeneralStatusTableSize=_TrailGeneralStatusTableSize_Object((1,3,6,1,4,1,8708,2,38,2,1,3),_TrailGeneralStatusTableSize_Type())
trailGeneralStatusTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:trailGeneralStatusTableSize.setStatus(_B)
_TrailStatusList_ObjectIdentity=ObjectIdentity
trailStatusList=_TrailStatusList_ObjectIdentity((1,3,6,1,4,1,8708,2,38,2,2))
_TrailStatusTable_Object=MibTable
trailStatusTable=_TrailStatusTable_Object((1,3,6,1,4,1,8708,2,38,2,2,1))
if mibBuilder.loadTexts:trailStatusTable.setStatus(_B)
_TrailStatusEntry_Object=MibTableRow
trailStatusEntry=_TrailStatusEntry_Object((1,3,6,1,4,1,8708,2,38,2,2,1,1))
trailStatusEntry.setIndexNames((0,_A,_D))
if mibBuilder.loadTexts:trailStatusEntry.setStatus(_B)
class _TrailStatusIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_TrailStatusIndex_Type.__name__=_H
_TrailStatusIndex_Object=MibTableColumn
trailStatusIndex=_TrailStatusIndex_Object((1,3,6,1,4,1,8708,2,38,2,2,1,1,1),_TrailStatusIndex_Type())
trailStatusIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:trailStatusIndex.setStatus(_B)
_TrailStatusIncomplete_Type=FaultStatus
_TrailStatusIncomplete_Object=MibTableColumn
trailStatusIncomplete=_TrailStatusIncomplete_Object((1,3,6,1,4,1,8708,2,38,2,2,1,1,2),_TrailStatusIncomplete_Type())
trailStatusIncomplete.setMaxAccess(_C)
if mibBuilder.loadTexts:trailStatusIncomplete.setStatus(_B)
_TrailStatusDegraded_Type=FaultStatus
_TrailStatusDegraded_Object=MibTableColumn
trailStatusDegraded=_TrailStatusDegraded_Object((1,3,6,1,4,1,8708,2,38,2,2,1,1,3),_TrailStatusDegraded_Type())
trailStatusDegraded.setMaxAccess(_C)
if mibBuilder.loadTexts:trailStatusDegraded.setStatus(_E)
_TrailStatusDown_Type=FaultStatus
_TrailStatusDown_Object=MibTableColumn
trailStatusDown=_TrailStatusDown_Object((1,3,6,1,4,1,8708,2,38,2,2,1,1,4),_TrailStatusDown_Type())
trailStatusDown.setMaxAccess(_C)
if mibBuilder.loadTexts:trailStatusDown.setStatus(_E)
trailGeneralGroup=ObjectGroup((1,3,6,1,4,1,8708,2,38,1,1,1))
trailGeneralGroup.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:trailGeneralGroup.setStatus(_B)
trailStatusGroup=ObjectGroup((1,3,6,1,4,1,8708,2,38,1,1,2))
trailStatusGroup.setObjects(*((_A,_D),(_A,_L),(_A,_M),(_A,_F)))
if mibBuilder.loadTexts:trailStatusGroup.setStatus(_E)
trailStatusGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,38,1,1,3))
trailStatusGroupV2.setObjects(*((_A,_D),(_A,_F)))
if mibBuilder.loadTexts:trailStatusGroupV2.setStatus(_B)
lumTrailBasicComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,38,1,2,1))
lumTrailBasicComplV1.setObjects(*((_A,_G),(_A,_N)))
if mibBuilder.loadTexts:lumTrailBasicComplV1.setStatus(_E)
lumTrailBasicComplV2=ModuleCompliance((1,3,6,1,4,1,8708,2,38,1,2,2))
lumTrailBasicComplV2.setObjects(*((_A,_G),(_A,_O)))
if mibBuilder.loadTexts:lumTrailBasicComplV2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'lumTrailMIBModule':lumTrailMIBModule,'lumTrailConfs':lumTrailConfs,'lumTrailGroups':lumTrailGroups,_G:trailGeneralGroup,_N:trailStatusGroup,_O:trailStatusGroupV2,'lumTrailCompl':lumTrailCompl,'lumTrailBasicComplV1':lumTrailBasicComplV1,'lumTrailBasicComplV2':lumTrailBasicComplV2,'lumTrailMIBObjects':lumTrailMIBObjects,'trailGeneral':trailGeneral,_I:trailGeneralConfigLastChangeTime,_J:trailGeneralStateLastChangeTime,_K:trailGeneralStatusTableSize,'trailStatusList':trailStatusList,'trailStatusTable':trailStatusTable,'trailStatusEntry':trailStatusEntry,_D:trailStatusIndex,_F:trailStatusIncomplete,_L:trailStatusDegraded,_M:trailStatusDown})