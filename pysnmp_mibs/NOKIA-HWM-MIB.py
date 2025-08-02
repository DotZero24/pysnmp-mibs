_P='ntcHWUnits'
_O='ntcHWUnitEntryChanged'
_N='ntcHWProductionDate'
_M='ntcHWSerialNumber'
_L='ntcHWLedState'
_K='ntcHWRestart'
_J='ntcHWAvailabilityStatus'
_I='ntcHWOperState'
_H='ntcHWAdminState'
_G='entPhysicalIndex'
_F='read-write'
_E='ENTITY-MIB'
_D='Integer32'
_C='read-only'
_B='NOKIA-HWM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_E,_G)
ntcCommonModules,ntcHWMibs,ntcHWReqs=mibBuilder.importSymbols('NOKIA-COMMON-MIB-OID-REGISTRATION-MIB','ntcCommonModules','ntcHWMibs','ntcHWReqs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
AutonomousType,DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType','DisplayString','PhysAddress','TextualConvention','TimeStamp')
ntcHWModule=ModuleIdentity((1,3,6,1,4,1,94,1,16,5,1))
if mibBuilder.loadTexts:ntcHWModule.setRevisions(('1998-08-24 00:00','1998-09-03 00:00','1998-09-24 00:00','1998-10-04 00:00','1999-01-08 00:00','1999-08-05 00:00','1999-10-25 00:00'))
_NtcHWObjs_ObjectIdentity=ObjectIdentity
ntcHWObjs=_NtcHWObjs_ObjectIdentity((1,3,6,1,4,1,94,1,16,7,1,1))
_NtcHWUnitTable_Object=MibTable
ntcHWUnitTable=_NtcHWUnitTable_Object((1,3,6,1,4,1,94,1,16,7,1,1,1))
if mibBuilder.loadTexts:ntcHWUnitTable.setStatus(_A)
_NtcHWUnitEntry_Object=MibTableRow
ntcHWUnitEntry=_NtcHWUnitEntry_Object((1,3,6,1,4,1,94,1,16,7,1,1,1,1))
ntcHWUnitEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:ntcHWUnitEntry.setStatus(_A)
class _NtcHWAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('inService',1),('outOfService',2),('inTest',3),('missing',4)))
_NtcHWAdminState_Type.__name__=_D
_NtcHWAdminState_Object=MibTableColumn
ntcHWAdminState=_NtcHWAdminState_Object((1,3,6,1,4,1,94,1,16,7,1,1,1,1,1),_NtcHWAdminState_Type())
ntcHWAdminState.setMaxAccess(_F)
if mibBuilder.loadTexts:ntcHWAdminState.setStatus(_A)
class _NtcHWOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('down',1),('up',2)))
_NtcHWOperState_Type.__name__=_D
_NtcHWOperState_Object=MibTableColumn
ntcHWOperState=_NtcHWOperState_Object((1,3,6,1,4,1,94,1,16,7,1,1,1,1,2),_NtcHWOperState_Type())
ntcHWOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcHWOperState.setStatus(_A)
class _NtcHWAvailabilityStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('inCharge',1),('applicationStarting',2),('applicationShutdown',3),('platformStarting',4),('resetting',5),('separated',6),('unconfigured',7),('testing',8),('standby',9),('dormant',10),('unavailable',11)))
_NtcHWAvailabilityStatus_Type.__name__=_D
_NtcHWAvailabilityStatus_Object=MibTableColumn
ntcHWAvailabilityStatus=_NtcHWAvailabilityStatus_Object((1,3,6,1,4,1,94,1,16,7,1,1,1,1,3),_NtcHWAvailabilityStatus_Type())
ntcHWAvailabilityStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcHWAvailabilityStatus.setStatus(_A)
class _NtcHWRestart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('reset',1),('hotRestart',2),('detach',3)))
_NtcHWRestart_Type.__name__=_D
_NtcHWRestart_Object=MibTableColumn
ntcHWRestart=_NtcHWRestart_Object((1,3,6,1,4,1,94,1,16,7,1,1,1,1,4),_NtcHWRestart_Type())
ntcHWRestart.setMaxAccess(_F)
if mibBuilder.loadTexts:ntcHWRestart.setStatus(_A)
class _NtcHWLedState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('red',1),('yellow',2),('black',3),('green',4)))
_NtcHWLedState_Type.__name__=_D
_NtcHWLedState_Object=MibTableColumn
ntcHWLedState=_NtcHWLedState_Object((1,3,6,1,4,1,94,1,16,7,1,1,1,1,5),_NtcHWLedState_Type())
ntcHWLedState.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcHWLedState.setStatus(_A)
_NtcHWSerialNumber_Type=DisplayString
_NtcHWSerialNumber_Object=MibTableColumn
ntcHWSerialNumber=_NtcHWSerialNumber_Object((1,3,6,1,4,1,94,1,16,7,1,1,1,1,6),_NtcHWSerialNumber_Type())
ntcHWSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcHWSerialNumber.setStatus(_A)
_NtcHWProductionDate_Type=DisplayString
_NtcHWProductionDate_Object=MibTableColumn
ntcHWProductionDate=_NtcHWProductionDate_Object((1,3,6,1,4,1,94,1,16,7,1,1,1,1,7),_NtcHWProductionDate_Type())
ntcHWProductionDate.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcHWProductionDate.setStatus(_A)
_NtcHWUnitEntryChanged_Type=TimeStamp
_NtcHWUnitEntryChanged_Object=MibTableColumn
ntcHWUnitEntryChanged=_NtcHWUnitEntryChanged_Object((1,3,6,1,4,1,94,1,16,7,1,1,1,1,8),_NtcHWUnitEntryChanged_Type())
ntcHWUnitEntryChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcHWUnitEntryChanged.setStatus(_A)
_NtcHWSlotTable_Object=MibTable
ntcHWSlotTable=_NtcHWSlotTable_Object((1,3,6,1,4,1,94,1,16,7,1,1,2))
if mibBuilder.loadTexts:ntcHWSlotTable.setStatus(_A)
_NtcHWSlotEntry_Object=MibTableRow
ntcHWSlotEntry=_NtcHWSlotEntry_Object((1,3,6,1,4,1,94,1,16,7,1,1,2,1))
ntcHWSlotEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:ntcHWSlotEntry.setStatus(_A)
_NtcHWDesiredUnitType_Type=AutonomousType
_NtcHWDesiredUnitType_Object=MibTableColumn
ntcHWDesiredUnitType=_NtcHWDesiredUnitType_Object((1,3,6,1,4,1,94,1,16,7,1,1,2,1,2),_NtcHWDesiredUnitType_Type())
ntcHWDesiredUnitType.setMaxAccess(_F)
if mibBuilder.loadTexts:ntcHWDesiredUnitType.setStatus(_A)
_NtcHWLastChangedTime_Type=TimeStamp
_NtcHWLastChangedTime_Object=MibScalar
ntcHWLastChangedTime=_NtcHWLastChangedTime_Object((1,3,6,1,4,1,94,1,16,7,1,1,3),_NtcHWLastChangedTime_Type())
ntcHWLastChangedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcHWLastChangedTime.setStatus(_A)
_NtcHWLoadInventoryContainer_Type=Integer32
_NtcHWLoadInventoryContainer_Object=MibScalar
ntcHWLoadInventoryContainer=_NtcHWLoadInventoryContainer_Object((1,3,6,1,4,1,94,1,16,7,1,1,4),_NtcHWLoadInventoryContainer_Type())
ntcHWLoadInventoryContainer.setMaxAccess(_F)
if mibBuilder.loadTexts:ntcHWLoadInventoryContainer.setStatus(_A)
_NtcHWEvents_ObjectIdentity=ObjectIdentity
ntcHWEvents=_NtcHWEvents_ObjectIdentity((1,3,6,1,4,1,94,1,16,7,1,2,0))
_NtcHWGroups_ObjectIdentity=ObjectIdentity
ntcHWGroups=_NtcHWGroups_ObjectIdentity((1,3,6,1,4,1,94,1,16,8,1,1))
_NtcHWCompliances_ObjectIdentity=ObjectIdentity
ntcHWCompliances=_NtcHWCompliances_ObjectIdentity((1,3,6,1,4,1,94,1,16,8,1,2))
ntcHWUnits=ObjectGroup((1,3,6,1,4,1,94,1,16,8,1,1,1))
ntcHWUnits.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:ntcHWUnits.setStatus(_A)
ntcHWCompliance=ModuleCompliance((1,3,6,1,4,1,94,1,16,8,1,2,1))
ntcHWCompliance.setObjects(*((_E,'entityPhysicalGroup'),(_B,_P)))
if mibBuilder.loadTexts:ntcHWCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcHWModule':ntcHWModule,'ntcHWObjs':ntcHWObjs,'ntcHWUnitTable':ntcHWUnitTable,'ntcHWUnitEntry':ntcHWUnitEntry,_H:ntcHWAdminState,_I:ntcHWOperState,_J:ntcHWAvailabilityStatus,_K:ntcHWRestart,_L:ntcHWLedState,_M:ntcHWSerialNumber,_N:ntcHWProductionDate,_O:ntcHWUnitEntryChanged,'ntcHWSlotTable':ntcHWSlotTable,'ntcHWSlotEntry':ntcHWSlotEntry,'ntcHWDesiredUnitType':ntcHWDesiredUnitType,'ntcHWLastChangedTime':ntcHWLastChangedTime,'ntcHWLoadInventoryContainer':ntcHWLoadInventoryContainer,'ntcHWEvents':ntcHWEvents,'ntcHWGroups':ntcHWGroups,_P:ntcHWUnits,'ntcHWCompliances':ntcHWCompliances,'ntcHWCompliance':ntcHWCompliance})