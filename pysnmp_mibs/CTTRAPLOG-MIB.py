_P='filterLogId'
_O='filterFilterId'
_N='filterSlotInChassis'
_M='existing'
_L='severe'
_K='warning'
_J='informational'
_I='slotChassis'
_H='slotInChassis'
_G='read-write'
_F='DisplayString'
_E='OctetString'
_D='Integer32'
_C='CTTRAPLOG-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctTrapLog,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctTrapLog')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
_TotalNumberOfEntries_Type=Integer32
_TotalNumberOfEntries_Object=MibScalar
totalNumberOfEntries=_TotalNumberOfEntries_Object((1,3,6,1,4,1,52,4,1,44,1),_TotalNumberOfEntries_Type())
totalNumberOfEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:totalNumberOfEntries.setStatus(_A)
_ConfigTable_Object=MibTable
configTable=_ConfigTable_Object((1,3,6,1,4,1,52,4,1,44,2))
if mibBuilder.loadTexts:configTable.setStatus(_A)
_ConfigTableEntry_Object=MibTableRow
configTableEntry=_ConfigTableEntry_Object((1,3,6,1,4,1,52,4,1,44,2,1))
configTableEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:configTableEntry.setStatus(_A)
_SlotInChassis_Type=Integer32
_SlotInChassis_Object=MibTableColumn
slotInChassis=_SlotInChassis_Object((1,3,6,1,4,1,52,4,1,44,2,1,1),_SlotInChassis_Type())
slotInChassis.setMaxAccess(_B)
if mibBuilder.loadTexts:slotInChassis.setStatus(_A)
_NumEntriesLoggeds_Type=Counter32
_NumEntriesLoggeds_Object=MibTableColumn
numEntriesLoggeds=_NumEntriesLoggeds_Object((1,3,6,1,4,1,52,4,1,44,2,1,2),_NumEntriesLoggeds_Type())
numEntriesLoggeds.setMaxAccess(_B)
if mibBuilder.loadTexts:numEntriesLoggeds.setStatus(_A)
_NumEntriesRequested_Type=Integer32
_NumEntriesRequested_Object=MibTableColumn
numEntriesRequested=_NumEntriesRequested_Object((1,3,6,1,4,1,52,4,1,44,2,1,3),_NumEntriesRequested_Type())
numEntriesRequested.setMaxAccess(_G)
if mibBuilder.loadTexts:numEntriesRequested.setStatus(_A)
_NumEntriesAllocated_Type=Integer32
_NumEntriesAllocated_Object=MibTableColumn
numEntriesAllocated=_NumEntriesAllocated_Object((1,3,6,1,4,1,52,4,1,44,2,1,4),_NumEntriesAllocated_Type())
numEntriesAllocated.setMaxAccess(_B)
if mibBuilder.loadTexts:numEntriesAllocated.setStatus(_A)
_LastLoggedEntryLogId_Type=Integer32
_LastLoggedEntryLogId_Object=MibTableColumn
lastLoggedEntryLogId=_LastLoggedEntryLogId_Object((1,3,6,1,4,1,52,4,1,44,2,1,5),_LastLoggedEntryLogId_Type())
lastLoggedEntryLogId.setMaxAccess(_B)
if mibBuilder.loadTexts:lastLoggedEntryLogId.setStatus(_A)
class _LogCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('clearLog',1))
_LogCommand_Type.__name__=_D
_LogCommand_Object=MibTableColumn
logCommand=_LogCommand_Object((1,3,6,1,4,1,52,4,1,44,2,1,6),_LogCommand_Type())
logCommand.setMaxAccess(_G)
if mibBuilder.loadTexts:logCommand.setStatus(_A)
_Wrap_Type=Integer32
_Wrap_Object=MibTableColumn
wrap=_Wrap_Object((1,3,6,1,4,1,52,4,1,44,2,1,7),_Wrap_Type())
wrap.setMaxAccess(_B)
if mibBuilder.loadTexts:wrap.setStatus(_A)
_TrapLogTable_Object=MibTable
trapLogTable=_TrapLogTable_Object((1,3,6,1,4,1,52,4,1,44,3))
if mibBuilder.loadTexts:trapLogTable.setStatus(_A)
_TrapLogEntry_Object=MibTableRow
trapLogEntry=_TrapLogEntry_Object((1,3,6,1,4,1,52,4,1,44,3,1))
trapLogEntry.setIndexNames((0,_C,_I),(0,_C,'logId'))
if mibBuilder.loadTexts:trapLogEntry.setStatus(_A)
_LogId_Type=Integer32
_LogId_Object=MibTableColumn
logId=_LogId_Object((1,3,6,1,4,1,52,4,1,44,3,1,1),_LogId_Type())
logId.setMaxAccess(_B)
if mibBuilder.loadTexts:logId.setStatus(_A)
_NvmpId_Type=Integer32
_NvmpId_Object=MibTableColumn
nvmpId=_NvmpId_Object((1,3,6,1,4,1,52,4,1,44,3,1,2),_NvmpId_Type())
nvmpId.setMaxAccess(_B)
if mibBuilder.loadTexts:nvmpId.setStatus(_A)
_TrapLogAcknowledged_Type=Integer32
_TrapLogAcknowledged_Object=MibTableColumn
trapLogAcknowledged=_TrapLogAcknowledged_Object((1,3,6,1,4,1,52,4,1,44,3,1,3),_TrapLogAcknowledged_Type())
trapLogAcknowledged.setMaxAccess(_B)
if mibBuilder.loadTexts:trapLogAcknowledged.setStatus(_A)
class _TrapLogVarBind_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1500))
_TrapLogVarBind_Type.__name__=_E
_TrapLogVarBind_Object=MibTableColumn
trapLogVarBind=_TrapLogVarBind_Object((1,3,6,1,4,1,52,4,1,44,3,1,4),_TrapLogVarBind_Type())
trapLogVarBind.setMaxAccess(_B)
if mibBuilder.loadTexts:trapLogVarBind.setStatus(_A)
class _TrapLogDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_TrapLogDescription_Type.__name__=_F
_TrapLogDescription_Object=MibTableColumn
trapLogDescription=_TrapLogDescription_Object((1,3,6,1,4,1,52,4,1,44,3,1,5),_TrapLogDescription_Type())
trapLogDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:trapLogDescription.setStatus(_A)
_TimeLogged_Type=TimeTicks
_TimeLogged_Object=MibTableColumn
timeLogged=_TimeLogged_Object((1,3,6,1,4,1,52,4,1,44,3,1,6),_TimeLogged_Type())
timeLogged.setMaxAccess(_B)
if mibBuilder.loadTexts:timeLogged.setStatus(_A)
class _FilterId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),('fatal',4),(_M,5)))
_FilterId_Type.__name__=_D
_FilterId_Object=MibTableColumn
filterId=_FilterId_Object((1,3,6,1,4,1,52,4,1,44,3,1,7),_FilterId_Type())
filterId.setMaxAccess(_B)
if mibBuilder.loadTexts:filterId.setStatus(_A)
_SlotChassis_Type=Integer32
_SlotChassis_Object=MibTableColumn
slotChassis=_SlotChassis_Object((1,3,6,1,4,1,52,4,1,44,3,1,8),_SlotChassis_Type())
slotChassis.setMaxAccess(_B)
if mibBuilder.loadTexts:slotChassis.setStatus(_A)
_TrapOID_Type=ObjectIdentifier
_TrapOID_Object=MibTableColumn
trapOID=_TrapOID_Object((1,3,6,1,4,1,52,4,1,44,3,1,9),_TrapOID_Type())
trapOID.setMaxAccess(_B)
if mibBuilder.loadTexts:trapOID.setStatus(_A)
_Z80Time_Type=TimeTicks
_Z80Time_Object=MibTableColumn
z80Time=_Z80Time_Object((1,3,6,1,4,1,52,4,1,44,3,1,10),_Z80Time_Type())
z80Time.setMaxAccess(_B)
if mibBuilder.loadTexts:z80Time.setStatus(_A)
_FilterTable_Object=MibTable
filterTable=_FilterTable_Object((1,3,6,1,4,1,52,4,1,44,4))
if mibBuilder.loadTexts:filterTable.setStatus(_A)
_FilterEntry_Object=MibTableRow
filterEntry=_FilterEntry_Object((1,3,6,1,4,1,52,4,1,44,4,1))
filterEntry.setIndexNames((0,_C,_N),(0,_C,_O),(0,_C,_P))
if mibBuilder.loadTexts:filterEntry.setStatus(_A)
_FilterLogId_Type=Integer32
_FilterLogId_Object=MibTableColumn
filterLogId=_FilterLogId_Object((1,3,6,1,4,1,52,4,1,44,4,1,1),_FilterLogId_Type())
filterLogId.setMaxAccess(_B)
if mibBuilder.loadTexts:filterLogId.setStatus(_A)
_FilterNvmpId_Type=Integer32
_FilterNvmpId_Object=MibTableColumn
filterNvmpId=_FilterNvmpId_Object((1,3,6,1,4,1,52,4,1,44,4,1,2),_FilterNvmpId_Type())
filterNvmpId.setMaxAccess(_B)
if mibBuilder.loadTexts:filterNvmpId.setStatus(_A)
_FilterTrapLogAcknowledged_Type=Integer32
_FilterTrapLogAcknowledged_Object=MibTableColumn
filterTrapLogAcknowledged=_FilterTrapLogAcknowledged_Object((1,3,6,1,4,1,52,4,1,44,4,1,3),_FilterTrapLogAcknowledged_Type())
filterTrapLogAcknowledged.setMaxAccess(_B)
if mibBuilder.loadTexts:filterTrapLogAcknowledged.setStatus(_A)
class _FilterTrapLogVarBind_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1500))
_FilterTrapLogVarBind_Type.__name__=_E
_FilterTrapLogVarBind_Object=MibTableColumn
filterTrapLogVarBind=_FilterTrapLogVarBind_Object((1,3,6,1,4,1,52,4,1,44,4,1,4),_FilterTrapLogVarBind_Type())
filterTrapLogVarBind.setMaxAccess(_B)
if mibBuilder.loadTexts:filterTrapLogVarBind.setStatus(_A)
class _FilterTrapLogDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_FilterTrapLogDescription_Type.__name__=_F
_FilterTrapLogDescription_Object=MibTableColumn
filterTrapLogDescription=_FilterTrapLogDescription_Object((1,3,6,1,4,1,52,4,1,44,4,1,5),_FilterTrapLogDescription_Type())
filterTrapLogDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:filterTrapLogDescription.setStatus(_A)
_FilterTimeLogged_Type=TimeTicks
_FilterTimeLogged_Object=MibTableColumn
filterTimeLogged=_FilterTimeLogged_Object((1,3,6,1,4,1,52,4,1,44,4,1,6),_FilterTimeLogged_Type())
filterTimeLogged.setMaxAccess(_B)
if mibBuilder.loadTexts:filterTimeLogged.setStatus(_A)
class _FilterFilterId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),('fatal',4),(_M,5)))
_FilterFilterId_Type.__name__=_D
_FilterFilterId_Object=MibTableColumn
filterFilterId=_FilterFilterId_Object((1,3,6,1,4,1,52,4,1,44,4,1,7),_FilterFilterId_Type())
filterFilterId.setMaxAccess(_B)
if mibBuilder.loadTexts:filterFilterId.setStatus(_A)
_FilterSlotInChassis_Type=Integer32
_FilterSlotInChassis_Object=MibTableColumn
filterSlotInChassis=_FilterSlotInChassis_Object((1,3,6,1,4,1,52,4,1,44,4,1,8),_FilterSlotInChassis_Type())
filterSlotInChassis.setMaxAccess(_B)
if mibBuilder.loadTexts:filterSlotInChassis.setStatus(_A)
_FilterTrapOID_Type=ObjectIdentifier
_FilterTrapOID_Object=MibTableColumn
filterTrapOID=_FilterTrapOID_Object((1,3,6,1,4,1,52,4,1,44,4,1,9),_FilterTrapOID_Type())
filterTrapOID.setMaxAccess(_B)
if mibBuilder.loadTexts:filterTrapOID.setStatus(_A)
_FilterZ80Time_Type=TimeTicks
_FilterZ80Time_Object=MibTableColumn
filterZ80Time=_FilterZ80Time_Object((1,3,6,1,4,1,52,4,1,44,4,1,10),_FilterZ80Time_Type())
filterZ80Time.setMaxAccess(_B)
if mibBuilder.loadTexts:filterZ80Time.setStatus(_A)
class _TrapLoggerAgent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('disabled',1),('enabled',2),('standby',3),('elected',4)))
_TrapLoggerAgent_Type.__name__=_D
_TrapLoggerAgent_Object=MibScalar
trapLoggerAgent=_TrapLoggerAgent_Object((1,3,6,1,4,1,52,4,1,44,5),_TrapLoggerAgent_Type())
trapLoggerAgent.setMaxAccess(_G)
if mibBuilder.loadTexts:trapLoggerAgent.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'totalNumberOfEntries':totalNumberOfEntries,'configTable':configTable,'configTableEntry':configTableEntry,_H:slotInChassis,'numEntriesLoggeds':numEntriesLoggeds,'numEntriesRequested':numEntriesRequested,'numEntriesAllocated':numEntriesAllocated,'lastLoggedEntryLogId':lastLoggedEntryLogId,'logCommand':logCommand,'wrap':wrap,'trapLogTable':trapLogTable,'trapLogEntry':trapLogEntry,'logId':logId,'nvmpId':nvmpId,'trapLogAcknowledged':trapLogAcknowledged,'trapLogVarBind':trapLogVarBind,'trapLogDescription':trapLogDescription,'timeLogged':timeLogged,'filterId':filterId,_I:slotChassis,'trapOID':trapOID,'z80Time':z80Time,'filterTable':filterTable,'filterEntry':filterEntry,_P:filterLogId,'filterNvmpId':filterNvmpId,'filterTrapLogAcknowledged':filterTrapLogAcknowledged,'filterTrapLogVarBind':filterTrapLogVarBind,'filterTrapLogDescription':filterTrapLogDescription,'filterTimeLogged':filterTimeLogged,_O:filterFilterId,_N:filterSlotInChassis,'filterTrapOID':filterTrapOID,'filterZ80Time':filterZ80Time,'trapLoggerAgent':trapLoggerAgent})