_T='smartSfpInstall'
_S='smartSfpType'
_R='SmartSfpModuleType'
_Q='not-accessible'
_P='smartSfpPortIdx'
_O='smartSfpSlotIdx'
_N='alarmEventReason'
_M='alarmEventLogSourceName'
_L='alarmEventLogSeverity'
_K='alarmEventLogDescription'
_J='alarmEventLogDateAndTime'
_I='alarmEventLogAlarmOrEventId'
_H='entPhysicalAlias'
_G='ENTITY-MIB'
_F='read-only'
_E='read-create'
_D='Integer32'
_C='RAD-SSFP-MIB'
_B='RAD-GEN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PhysicalIndexOrZero,entPhysicalAlias=mibBuilder.importSymbols(_G,'PhysicalIndexOrZero',_H)
alarmEventLogAlarmOrEventId,alarmEventLogDateAndTime,alarmEventLogDescription,alarmEventLogSeverity,alarmEventLogSourceName,alarmEventReason=mibBuilder.importSymbols(_B,_I,_J,_K,_L,_M,_N)
radSpecificDevices,=mibBuilder.importSymbols('RAD-SMI-MIB','radSpecificDevices')
SlotType,=mibBuilder.importSymbols('RAD-TC','SlotType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
smartSFP=ModuleIdentity((1,3,6,1,4,1,164,40,2))
class SmartSfpModuleType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('notApplicable',1),('miRIC-E1',2),('miRIC-T1',3),('miRIC-E3',4),('miRIC-T3',5),('miRICi-E1',6),('miRICi-T1',7),('miRICi-E3',8),('miRICi-T3',9),('miRICi-155',10),('miRICi-622',11),('miTOP-E1',12),('miTOP-E3',13),('miTOP-T1',14),('miTOP-T3',15),('sfp-VDSL-2W',16)))
_SmartSfpEvents_ObjectIdentity=ObjectIdentity
smartSfpEvents=_SmartSfpEvents_ObjectIdentity((1,3,6,1,4,1,164,40,2,0))
if mibBuilder.loadTexts:smartSfpEvents.setStatus(_A)
_SmartSfpTable_Object=MibTable
smartSfpTable=_SmartSfpTable_Object((1,3,6,1,4,1,164,40,2,1))
if mibBuilder.loadTexts:smartSfpTable.setStatus(_A)
_SmartSfpEntry_Object=MibTableRow
smartSfpEntry=_SmartSfpEntry_Object((1,3,6,1,4,1,164,40,2,1,1))
smartSfpEntry.setIndexNames((0,_C,_O),(0,_C,_P))
if mibBuilder.loadTexts:smartSfpEntry.setStatus(_A)
_SmartSfpSlotIdx_Type=SlotType
_SmartSfpSlotIdx_Object=MibTableColumn
smartSfpSlotIdx=_SmartSfpSlotIdx_Object((1,3,6,1,4,1,164,40,2,1,1,1),_SmartSfpSlotIdx_Type())
smartSfpSlotIdx.setMaxAccess(_Q)
if mibBuilder.loadTexts:smartSfpSlotIdx.setStatus(_A)
_SmartSfpPortIdx_Type=Integer32
_SmartSfpPortIdx_Object=MibTableColumn
smartSfpPortIdx=_SmartSfpPortIdx_Object((1,3,6,1,4,1,164,40,2,1,1,2),_SmartSfpPortIdx_Type())
smartSfpPortIdx.setMaxAccess(_Q)
if mibBuilder.loadTexts:smartSfpPortIdx.setStatus(_A)
_SmartSfpRowStatus_Type=RowStatus
_SmartSfpRowStatus_Object=MibTableColumn
smartSfpRowStatus=_SmartSfpRowStatus_Object((1,3,6,1,4,1,164,40,2,1,1,3),_SmartSfpRowStatus_Type())
smartSfpRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:smartSfpRowStatus.setStatus(_A)
class _SmartSfpType_Type(SmartSfpModuleType):defaultValue=1
_SmartSfpType_Type.__name__=_R
_SmartSfpType_Object=MibTableColumn
smartSfpType=_SmartSfpType_Object((1,3,6,1,4,1,164,40,2,1,1,4),_SmartSfpType_Type())
smartSfpType.setMaxAccess(_E)
if mibBuilder.loadTexts:smartSfpType.setStatus(_A)
class _SmartSfpAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_SmartSfpAdminStatus_Type.__name__=_D
_SmartSfpAdminStatus_Object=MibTableColumn
smartSfpAdminStatus=_SmartSfpAdminStatus_Object((1,3,6,1,4,1,164,40,2,1,1,5),_SmartSfpAdminStatus_Type())
smartSfpAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:smartSfpAdminStatus.setStatus('deprecated')
class _SmartSfpOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('onLine',1),('offLine',2),('notInstalled',3),('mismatch',4)))
_SmartSfpOperState_Type.__name__=_D
_SmartSfpOperState_Object=MibTableColumn
smartSfpOperState=_SmartSfpOperState_Object((1,3,6,1,4,1,164,40,2,1,1,6),_SmartSfpOperState_Type())
smartSfpOperState.setMaxAccess(_F)
if mibBuilder.loadTexts:smartSfpOperState.setStatus(_A)
class _SmartSfpResetCmd_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('off',2),('on',3)))
_SmartSfpResetCmd_Type.__name__=_D
_SmartSfpResetCmd_Object=MibTableColumn
smartSfpResetCmd=_SmartSfpResetCmd_Object((1,3,6,1,4,1,164,40,2,1,1,7),_SmartSfpResetCmd_Type())
smartSfpResetCmd.setMaxAccess(_E)
if mibBuilder.loadTexts:smartSfpResetCmd.setStatus(_A)
_SmartSfpInstall_Type=SmartSfpModuleType
_SmartSfpInstall_Object=MibTableColumn
smartSfpInstall=_SmartSfpInstall_Object((1,3,6,1,4,1,164,40,2,1,1,8),_SmartSfpInstall_Type())
smartSfpInstall.setMaxAccess(_F)
if mibBuilder.loadTexts:smartSfpInstall.setStatus(_A)
_SmartSfpPhysicalIndex_Type=PhysicalIndexOrZero
_SmartSfpPhysicalIndex_Object=MibTableColumn
smartSfpPhysicalIndex=_SmartSfpPhysicalIndex_Object((1,3,6,1,4,1,164,40,2,1,1,9),_SmartSfpPhysicalIndex_Type())
smartSfpPhysicalIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:smartSfpPhysicalIndex.setStatus(_A)
smartSfpMismatch=NotificationType((1,3,6,1,4,1,164,40,2,0,1))
smartSfpMismatch.setObjects(*((_B,_M),(_B,_I),(_B,_K),(_B,_L),(_B,_J),(_B,_N),(_G,_H),(_C,_S),(_C,_T)))
if mibBuilder.loadTexts:smartSfpMismatch.setStatus(_A)
mibBuilder.exportSymbols(_C,**{_R:SmartSfpModuleType,'smartSFP':smartSFP,'smartSfpEvents':smartSfpEvents,'smartSfpMismatch':smartSfpMismatch,'smartSfpTable':smartSfpTable,'smartSfpEntry':smartSfpEntry,_O:smartSfpSlotIdx,_P:smartSfpPortIdx,'smartSfpRowStatus':smartSfpRowStatus,_S:smartSfpType,'smartSfpAdminStatus':smartSfpAdminStatus,'smartSfpOperState':smartSfpOperState,'smartSfpResetCmd':smartSfpResetCmd,_T:smartSfpInstall,'smartSfpPhysicalIndex':smartSfpPhysicalIndex})