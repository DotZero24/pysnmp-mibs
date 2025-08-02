_U='camUsageL3ExtPipeId'
_T='camUsageL3ExtSlot'
_S='camUsageL3PipeLine'
_R='camUsageL3PipeId'
_Q='camUsageL3Slot'
_P='camUsageL2PipeLine'
_O='camUsageL2PipeId'
_N='camUsageL2Slot'
_M='camUsagePartId'
_L='camUsagePipeNum'
_K='camUsageSlot'
_J='sysCompCamPartId'
_I='sysCompPortPipe'
_H='sysCompSlotId'
_G='sysCompAlarmVarString'
_F='sysCompAlarmLevel'
_E='accessible-for-notify'
_D='not-accessible'
_C='DELL-NETWORKING-SYSTEM-COMPONENT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dellNetMgmt,=mibBuilder.importSymbols('DELL-NETWORKING-SMI','dellNetMgmt')
DellNetCamPartitionType,=mibBuilder.importSymbols('DELL-NETWORKING-TC','DellNetCamPartitionType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
dellNetSysComponentMib=ModuleIdentity((1,3,6,1,4,1,6027,3,7))
_DellNetSysComponentObjects_ObjectIdentity=ObjectIdentity
dellNetSysComponentObjects=_DellNetSysComponentObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,7,1))
_DellNetCamEntries_ObjectIdentity=ObjectIdentity
dellNetCamEntries=_DellNetCamEntries_ObjectIdentity((1,3,6,1,4,1,6027,3,7,1,1))
_CamUsageTable_Object=MibTable
camUsageTable=_CamUsageTable_Object((1,3,6,1,4,1,6027,3,7,1,1,1))
if mibBuilder.loadTexts:camUsageTable.setStatus(_A)
_CamUsageEntry_Object=MibTableRow
camUsageEntry=_CamUsageEntry_Object((1,3,6,1,4,1,6027,3,7,1,1,1,1))
camUsageEntry.setIndexNames((0,_C,_K),(0,_C,_L),(0,_C,_M))
if mibBuilder.loadTexts:camUsageEntry.setStatus(_A)
_CamUsageSlot_Type=Integer32
_CamUsageSlot_Object=MibTableColumn
camUsageSlot=_CamUsageSlot_Object((1,3,6,1,4,1,6027,3,7,1,1,1,1,1),_CamUsageSlot_Type())
camUsageSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:camUsageSlot.setStatus(_A)
_CamUsagePipeNum_Type=Integer32
_CamUsagePipeNum_Object=MibTableColumn
camUsagePipeNum=_CamUsagePipeNum_Object((1,3,6,1,4,1,6027,3,7,1,1,1,1,2),_CamUsagePipeNum_Type())
camUsagePipeNum.setMaxAccess(_D)
if mibBuilder.loadTexts:camUsagePipeNum.setStatus(_A)
_CamUsagePartId_Type=DellNetCamPartitionType
_CamUsagePartId_Object=MibTableColumn
camUsagePartId=_CamUsagePartId_Object((1,3,6,1,4,1,6027,3,7,1,1,1,1,3),_CamUsagePartId_Type())
camUsagePartId.setMaxAccess(_D)
if mibBuilder.loadTexts:camUsagePartId.setStatus(_A)
_CamUsagePartDesc_Type=DisplayString
_CamUsagePartDesc_Object=MibTableColumn
camUsagePartDesc=_CamUsagePartDesc_Object((1,3,6,1,4,1,6027,3,7,1,1,1,1,4),_CamUsagePartDesc_Type())
camUsagePartDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:camUsagePartDesc.setStatus(_A)
_CamUsageTotal_Type=Integer32
_CamUsageTotal_Object=MibTableColumn
camUsageTotal=_CamUsageTotal_Object((1,3,6,1,4,1,6027,3,7,1,1,1,1,5),_CamUsageTotal_Type())
camUsageTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:camUsageTotal.setStatus(_A)
_CamUsageUsed_Type=Integer32
_CamUsageUsed_Object=MibTableColumn
camUsageUsed=_CamUsageUsed_Object((1,3,6,1,4,1,6027,3,7,1,1,1,1,6),_CamUsageUsed_Type())
camUsageUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:camUsageUsed.setStatus(_A)
_CamUsageL2Table_Object=MibTable
camUsageL2Table=_CamUsageL2Table_Object((1,3,6,1,4,1,6027,3,7,1,1,2))
if mibBuilder.loadTexts:camUsageL2Table.setStatus(_A)
_CamUsageL2Entry_Object=MibTableRow
camUsageL2Entry=_CamUsageL2Entry_Object((1,3,6,1,4,1,6027,3,7,1,1,2,1))
camUsageL2Entry.setIndexNames((0,_C,_N),(0,_C,_O),(0,_C,_P))
if mibBuilder.loadTexts:camUsageL2Entry.setStatus(_A)
_CamUsageL2Slot_Type=Integer32
_CamUsageL2Slot_Object=MibTableColumn
camUsageL2Slot=_CamUsageL2Slot_Object((1,3,6,1,4,1,6027,3,7,1,1,2,1,1),_CamUsageL2Slot_Type())
camUsageL2Slot.setMaxAccess(_D)
if mibBuilder.loadTexts:camUsageL2Slot.setStatus(_A)
_CamUsageL2PipeId_Type=Integer32
_CamUsageL2PipeId_Object=MibTableColumn
camUsageL2PipeId=_CamUsageL2PipeId_Object((1,3,6,1,4,1,6027,3,7,1,1,2,1,2),_CamUsageL2PipeId_Type())
camUsageL2PipeId.setMaxAccess(_D)
if mibBuilder.loadTexts:camUsageL2PipeId.setStatus(_A)
_CamUsageL2IngAclTotal_Type=Integer32
_CamUsageL2IngAclTotal_Object=MibTableColumn
camUsageL2IngAclTotal=_CamUsageL2IngAclTotal_Object((1,3,6,1,4,1,6027,3,7,1,1,2,1,3),_CamUsageL2IngAclTotal_Type())
camUsageL2IngAclTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:camUsageL2IngAclTotal.setStatus(_A)
_CamUsageL2IngAclUsed_Type=Integer32
_CamUsageL2IngAclUsed_Object=MibTableColumn
camUsageL2IngAclUsed=_CamUsageL2IngAclUsed_Object((1,3,6,1,4,1,6027,3,7,1,1,2,1,4),_CamUsageL2IngAclUsed_Type())
camUsageL2IngAclUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:camUsageL2IngAclUsed.setStatus(_A)
_CamUsageL2IngFibTotal_Type=Integer32
_CamUsageL2IngFibTotal_Object=MibTableColumn
camUsageL2IngFibTotal=_CamUsageL2IngFibTotal_Object((1,3,6,1,4,1,6027,3,7,1,1,2,1,7),_CamUsageL2IngFibTotal_Type())
camUsageL2IngFibTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:camUsageL2IngFibTotal.setStatus(_A)
_CamUsageL2IngFibUsed_Type=Integer32
_CamUsageL2IngFibUsed_Object=MibTableColumn
camUsageL2IngFibUsed=_CamUsageL2IngFibUsed_Object((1,3,6,1,4,1,6027,3,7,1,1,2,1,8),_CamUsageL2IngFibUsed_Type())
camUsageL2IngFibUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:camUsageL2IngFibUsed.setStatus(_A)
_CamUsageL2EgrAclTotal_Type=Integer32
_CamUsageL2EgrAclTotal_Object=MibTableColumn
camUsageL2EgrAclTotal=_CamUsageL2EgrAclTotal_Object((1,3,6,1,4,1,6027,3,7,1,1,2,1,9),_CamUsageL2EgrAclTotal_Type())
camUsageL2EgrAclTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:camUsageL2EgrAclTotal.setStatus(_A)
_CamUsageL2EgrAclUsed_Type=Integer32
_CamUsageL2EgrAclUsed_Object=MibTableColumn
camUsageL2EgrAclUsed=_CamUsageL2EgrAclUsed_Object((1,3,6,1,4,1,6027,3,7,1,1,2,1,10),_CamUsageL2EgrAclUsed_Type())
camUsageL2EgrAclUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:camUsageL2EgrAclUsed.setStatus(_A)
_CamUsageL2PipeLine_Type=Integer32
_CamUsageL2PipeLine_Object=MibTableColumn
camUsageL2PipeLine=_CamUsageL2PipeLine_Object((1,3,6,1,4,1,6027,3,7,1,1,2,1,11),_CamUsageL2PipeLine_Type())
camUsageL2PipeLine.setMaxAccess(_D)
if mibBuilder.loadTexts:camUsageL2PipeLine.setStatus(_A)
_CamUsageL3Table_Object=MibTable
camUsageL3Table=_CamUsageL3Table_Object((1,3,6,1,4,1,6027,3,7,1,1,3))
if mibBuilder.loadTexts:camUsageL3Table.setStatus(_A)
_CamUsageL3Entry_Object=MibTableRow
camUsageL3Entry=_CamUsageL3Entry_Object((1,3,6,1,4,1,6027,3,7,1,1,3,1))
camUsageL3Entry.setIndexNames((0,_C,_Q),(0,_C,_R),(0,_C,_S))
if mibBuilder.loadTexts:camUsageL3Entry.setStatus(_A)
_CamUsageL3Slot_Type=Integer32
_CamUsageL3Slot_Object=MibTableColumn
camUsageL3Slot=_CamUsageL3Slot_Object((1,3,6,1,4,1,6027,3,7,1,1,3,1,1),_CamUsageL3Slot_Type())
camUsageL3Slot.setMaxAccess(_D)
if mibBuilder.loadTexts:camUsageL3Slot.setStatus(_A)
_CamUsageL3PipeId_Type=Integer32
_CamUsageL3PipeId_Object=MibTableColumn
camUsageL3PipeId=_CamUsageL3PipeId_Object((1,3,6,1,4,1,6027,3,7,1,1,3,1,2),_CamUsageL3PipeId_Type())
camUsageL3PipeId.setMaxAccess(_D)
if mibBuilder.loadTexts:camUsageL3PipeId.setStatus(_A)
_CamUsageL3IngFibTotal_Type=Integer32
_CamUsageL3IngFibTotal_Object=MibTableColumn
camUsageL3IngFibTotal=_CamUsageL3IngFibTotal_Object((1,3,6,1,4,1,6027,3,7,1,1,3,1,3),_CamUsageL3IngFibTotal_Type())
camUsageL3IngFibTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:camUsageL3IngFibTotal.setStatus(_A)
_CamUsageL3IngFibUsed_Type=Integer32
_CamUsageL3IngFibUsed_Object=MibTableColumn
camUsageL3IngFibUsed=_CamUsageL3IngFibUsed_Object((1,3,6,1,4,1,6027,3,7,1,1,3,1,4),_CamUsageL3IngFibUsed_Type())
camUsageL3IngFibUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:camUsageL3IngFibUsed.setStatus(_A)
_CamUsageL3IngSysFlowTotal_Type=Integer32
_CamUsageL3IngSysFlowTotal_Object=MibTableColumn
camUsageL3IngSysFlowTotal=_CamUsageL3IngSysFlowTotal_Object((1,3,6,1,4,1,6027,3,7,1,1,3,1,5),_CamUsageL3IngSysFlowTotal_Type())
camUsageL3IngSysFlowTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:camUsageL3IngSysFlowTotal.setStatus(_A)
_CamUsageL3IngSysFlowUsed_Type=Integer32
_CamUsageL3IngSysFlowUsed_Object=MibTableColumn
camUsageL3IngSysFlowUsed=_CamUsageL3IngSysFlowUsed_Object((1,3,6,1,4,1,6027,3,7,1,1,3,1,6),_CamUsageL3IngSysFlowUsed_Type())
camUsageL3IngSysFlowUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:camUsageL3IngSysFlowUsed.setStatus(_A)
_CamUsageL3IngTrcListTotal_Type=Integer32
_CamUsageL3IngTrcListTotal_Object=MibTableColumn
camUsageL3IngTrcListTotal=_CamUsageL3IngTrcListTotal_Object((1,3,6,1,4,1,6027,3,7,1,1,3,1,7),_CamUsageL3IngTrcListTotal_Type())
camUsageL3IngTrcListTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:camUsageL3IngTrcListTotal.setStatus(_A)
_CamUsageL3IngTrcListUsed_Type=Integer32
_CamUsageL3IngTrcListUsed_Object=MibTableColumn
camUsageL3IngTrcListUsed=_CamUsageL3IngTrcListUsed_Object((1,3,6,1,4,1,6027,3,7,1,1,3,1,8),_CamUsageL3IngTrcListUsed_Type())
camUsageL3IngTrcListUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:camUsageL3IngTrcListUsed.setStatus(_A)
_CamUsageL3IngMcastFibTotal_Type=Integer32
_CamUsageL3IngMcastFibTotal_Object=MibTableColumn
camUsageL3IngMcastFibTotal=_CamUsageL3IngMcastFibTotal_Object((1,3,6,1,4,1,6027,3,7,1,1,3,1,9),_CamUsageL3IngMcastFibTotal_Type())
camUsageL3IngMcastFibTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:camUsageL3IngMcastFibTotal.setStatus(_A)
_CamUsageL3IngMcastFibUsed_Type=Integer32
_CamUsageL3IngMcastFibUsed_Object=MibTableColumn
camUsageL3IngMcastFibUsed=_CamUsageL3IngMcastFibUsed_Object((1,3,6,1,4,1,6027,3,7,1,1,3,1,10),_CamUsageL3IngMcastFibUsed_Type())
camUsageL3IngMcastFibUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:camUsageL3IngMcastFibUsed.setStatus(_A)
_CamUsageL3IngQosTotal_Type=Integer32
_CamUsageL3IngQosTotal_Object=MibTableColumn
camUsageL3IngQosTotal=_CamUsageL3IngQosTotal_Object((1,3,6,1,4,1,6027,3,7,1,1,3,1,11),_CamUsageL3IngQosTotal_Type())
camUsageL3IngQosTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:camUsageL3IngQosTotal.setStatus(_A)
_CamUsageL3IngQosUsed_Type=Integer32
_CamUsageL3IngQosUsed_Object=MibTableColumn
camUsageL3IngQosUsed=_CamUsageL3IngQosUsed_Object((1,3,6,1,4,1,6027,3,7,1,1,3,1,12),_CamUsageL3IngQosUsed_Type())
camUsageL3IngQosUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:camUsageL3IngQosUsed.setStatus(_A)
_CamUsageL3IngPbrTotal_Type=Integer32
_CamUsageL3IngPbrTotal_Object=MibTableColumn
camUsageL3IngPbrTotal=_CamUsageL3IngPbrTotal_Object((1,3,6,1,4,1,6027,3,7,1,1,3,1,13),_CamUsageL3IngPbrTotal_Type())
camUsageL3IngPbrTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:camUsageL3IngPbrTotal.setStatus(_A)
_CamUsageL3IngPbrUsed_Type=Integer32
_CamUsageL3IngPbrUsed_Object=MibTableColumn
camUsageL3IngPbrUsed=_CamUsageL3IngPbrUsed_Object((1,3,6,1,4,1,6027,3,7,1,1,3,1,14),_CamUsageL3IngPbrUsed_Type())
camUsageL3IngPbrUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:camUsageL3IngPbrUsed.setStatus(_A)
_CamUsageL3IngAclTotal_Type=Integer32
_CamUsageL3IngAclTotal_Object=MibTableColumn
camUsageL3IngAclTotal=_CamUsageL3IngAclTotal_Object((1,3,6,1,4,1,6027,3,7,1,1,3,1,15),_CamUsageL3IngAclTotal_Type())
camUsageL3IngAclTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:camUsageL3IngAclTotal.setStatus(_A)
_CamUsageL3IngAclUsed_Type=Integer32
_CamUsageL3IngAclUsed_Object=MibTableColumn
camUsageL3IngAclUsed=_CamUsageL3IngAclUsed_Object((1,3,6,1,4,1,6027,3,7,1,1,3,1,16),_CamUsageL3IngAclUsed_Type())
camUsageL3IngAclUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:camUsageL3IngAclUsed.setStatus(_A)
_CamUsageL3EgrAclTotal_Type=Integer32
_CamUsageL3EgrAclTotal_Object=MibTableColumn
camUsageL3EgrAclTotal=_CamUsageL3EgrAclTotal_Object((1,3,6,1,4,1,6027,3,7,1,1,3,1,17),_CamUsageL3EgrAclTotal_Type())
camUsageL3EgrAclTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:camUsageL3EgrAclTotal.setStatus(_A)
_CamUsageL3EgrAclUsed_Type=Integer32
_CamUsageL3EgrAclUsed_Object=MibTableColumn
camUsageL3EgrAclUsed=_CamUsageL3EgrAclUsed_Object((1,3,6,1,4,1,6027,3,7,1,1,3,1,18),_CamUsageL3EgrAclUsed_Type())
camUsageL3EgrAclUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:camUsageL3EgrAclUsed.setStatus(_A)
_CamUsageL3PipeLine_Type=Integer32
_CamUsageL3PipeLine_Object=MibTableColumn
camUsageL3PipeLine=_CamUsageL3PipeLine_Object((1,3,6,1,4,1,6027,3,7,1,1,3,1,19),_CamUsageL3PipeLine_Type())
camUsageL3PipeLine.setMaxAccess(_D)
if mibBuilder.loadTexts:camUsageL3PipeLine.setStatus(_A)
_CamUsageL3ExtTable_Object=MibTable
camUsageL3ExtTable=_CamUsageL3ExtTable_Object((1,3,6,1,4,1,6027,3,7,1,1,4))
if mibBuilder.loadTexts:camUsageL3ExtTable.setStatus(_A)
_CamUsageL3ExtEntry_Object=MibTableRow
camUsageL3ExtEntry=_CamUsageL3ExtEntry_Object((1,3,6,1,4,1,6027,3,7,1,1,4,1))
camUsageL3ExtEntry.setIndexNames((0,_C,_T),(0,_C,_U))
if mibBuilder.loadTexts:camUsageL3ExtEntry.setStatus(_A)
_CamUsageL3ExtSlot_Type=Integer32
_CamUsageL3ExtSlot_Object=MibTableColumn
camUsageL3ExtSlot=_CamUsageL3ExtSlot_Object((1,3,6,1,4,1,6027,3,7,1,1,4,1,1),_CamUsageL3ExtSlot_Type())
camUsageL3ExtSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:camUsageL3ExtSlot.setStatus(_A)
_CamUsageL3ExtPipeId_Type=Integer32
_CamUsageL3ExtPipeId_Object=MibTableColumn
camUsageL3ExtPipeId=_CamUsageL3ExtPipeId_Object((1,3,6,1,4,1,6027,3,7,1,1,4,1,2),_CamUsageL3ExtPipeId_Type())
camUsageL3ExtPipeId.setMaxAccess(_D)
if mibBuilder.loadTexts:camUsageL3ExtPipeId.setStatus(_A)
_CamUsageL3ExtHostTotal_Type=Integer32
_CamUsageL3ExtHostTotal_Object=MibTableColumn
camUsageL3ExtHostTotal=_CamUsageL3ExtHostTotal_Object((1,3,6,1,4,1,6027,3,7,1,1,4,1,3),_CamUsageL3ExtHostTotal_Type())
camUsageL3ExtHostTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:camUsageL3ExtHostTotal.setStatus(_A)
_CamUsageL3ExtHostUsed_Type=Integer32
_CamUsageL3ExtHostUsed_Object=MibTableColumn
camUsageL3ExtHostUsed=_CamUsageL3ExtHostUsed_Object((1,3,6,1,4,1,6027,3,7,1,1,4,1,4),_CamUsageL3ExtHostUsed_Type())
camUsageL3ExtHostUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:camUsageL3ExtHostUsed.setStatus(_A)
_CamUsageL3ExtLPMTotal_Type=Integer32
_CamUsageL3ExtLPMTotal_Object=MibTableColumn
camUsageL3ExtLPMTotal=_CamUsageL3ExtLPMTotal_Object((1,3,6,1,4,1,6027,3,7,1,1,4,1,5),_CamUsageL3ExtLPMTotal_Type())
camUsageL3ExtLPMTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:camUsageL3ExtLPMTotal.setStatus(_A)
_CamUsageL3ExtLPMUsed_Type=Integer32
_CamUsageL3ExtLPMUsed_Object=MibTableColumn
camUsageL3ExtLPMUsed=_CamUsageL3ExtLPMUsed_Object((1,3,6,1,4,1,6027,3,7,1,1,4,1,6),_CamUsageL3ExtLPMUsed_Type())
camUsageL3ExtLPMUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:camUsageL3ExtLPMUsed.setStatus(_A)
_DellNetSysComponentTrap_ObjectIdentity=ObjectIdentity
dellNetSysComponentTrap=_DellNetSysComponentTrap_ObjectIdentity((1,3,6,1,4,1,6027,3,7,1,2))
_SysCompAlarmMibNotifications_ObjectIdentity=ObjectIdentity
sysCompAlarmMibNotifications=_SysCompAlarmMibNotifications_ObjectIdentity((1,3,6,1,4,1,6027,3,7,1,2,0))
_SysCompAlarmVariable_ObjectIdentity=ObjectIdentity
sysCompAlarmVariable=_SysCompAlarmVariable_ObjectIdentity((1,3,6,1,4,1,6027,3,7,1,2,1))
_SysCompAlarmLevel_Type=Integer32
_SysCompAlarmLevel_Object=MibScalar
sysCompAlarmLevel=_SysCompAlarmLevel_Object((1,3,6,1,4,1,6027,3,7,1,2,1,1),_SysCompAlarmLevel_Type())
sysCompAlarmLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:sysCompAlarmLevel.setStatus(_A)
_SysCompAlarmVarString_Type=OctetString
_SysCompAlarmVarString_Object=MibScalar
sysCompAlarmVarString=_SysCompAlarmVarString_Object((1,3,6,1,4,1,6027,3,7,1,2,1,2),_SysCompAlarmVarString_Type())
sysCompAlarmVarString.setMaxAccess(_E)
if mibBuilder.loadTexts:sysCompAlarmVarString.setStatus(_A)
_SysCompSlotId_Type=Integer32
_SysCompSlotId_Object=MibScalar
sysCompSlotId=_SysCompSlotId_Object((1,3,6,1,4,1,6027,3,7,1,2,1,3),_SysCompSlotId_Type())
sysCompSlotId.setMaxAccess(_E)
if mibBuilder.loadTexts:sysCompSlotId.setStatus(_A)
_SysCompPortPipe_Type=Integer32
_SysCompPortPipe_Object=MibScalar
sysCompPortPipe=_SysCompPortPipe_Object((1,3,6,1,4,1,6027,3,7,1,2,1,4),_SysCompPortPipe_Type())
sysCompPortPipe.setMaxAccess(_E)
if mibBuilder.loadTexts:sysCompPortPipe.setStatus(_A)
_SysCompCamPartId_Type=DisplayString
_SysCompCamPartId_Object=MibScalar
sysCompCamPartId=_SysCompCamPartId_Object((1,3,6,1,4,1,6027,3,7,1,2,1,5),_SysCompCamPartId_Type())
sysCompCamPartId.setMaxAccess(_E)
if mibBuilder.loadTexts:sysCompCamPartId.setStatus(_A)
camUsageThresholdExceed=NotificationType((1,3,6,1,4,1,6027,3,7,1,2,0,1))
camUsageThresholdExceed.setObjects(*((_C,_F),(_C,_G),(_C,_H),(_C,_I),(_C,_J)))
if mibBuilder.loadTexts:camUsageThresholdExceed.setStatus(_A)
camIsFull=NotificationType((1,3,6,1,4,1,6027,3,7,1,2,0,2))
camIsFull.setObjects(*((_C,_F),(_C,_G),(_C,_H),(_C,_I),(_C,_J)))
if mibBuilder.loadTexts:camIsFull.setStatus(_A)
camAuditError=NotificationType((1,3,6,1,4,1,6027,3,7,1,2,0,3))
camAuditError.setObjects(*((_C,_F),(_C,_G),(_C,_H),(_C,_I),(_C,_J)))
if mibBuilder.loadTexts:camAuditError.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'dellNetSysComponentMib':dellNetSysComponentMib,'dellNetSysComponentObjects':dellNetSysComponentObjects,'dellNetCamEntries':dellNetCamEntries,'camUsageTable':camUsageTable,'camUsageEntry':camUsageEntry,_K:camUsageSlot,_L:camUsagePipeNum,_M:camUsagePartId,'camUsagePartDesc':camUsagePartDesc,'camUsageTotal':camUsageTotal,'camUsageUsed':camUsageUsed,'camUsageL2Table':camUsageL2Table,'camUsageL2Entry':camUsageL2Entry,_N:camUsageL2Slot,_O:camUsageL2PipeId,'camUsageL2IngAclTotal':camUsageL2IngAclTotal,'camUsageL2IngAclUsed':camUsageL2IngAclUsed,'camUsageL2IngFibTotal':camUsageL2IngFibTotal,'camUsageL2IngFibUsed':camUsageL2IngFibUsed,'camUsageL2EgrAclTotal':camUsageL2EgrAclTotal,'camUsageL2EgrAclUsed':camUsageL2EgrAclUsed,_P:camUsageL2PipeLine,'camUsageL3Table':camUsageL3Table,'camUsageL3Entry':camUsageL3Entry,_Q:camUsageL3Slot,_R:camUsageL3PipeId,'camUsageL3IngFibTotal':camUsageL3IngFibTotal,'camUsageL3IngFibUsed':camUsageL3IngFibUsed,'camUsageL3IngSysFlowTotal':camUsageL3IngSysFlowTotal,'camUsageL3IngSysFlowUsed':camUsageL3IngSysFlowUsed,'camUsageL3IngTrcListTotal':camUsageL3IngTrcListTotal,'camUsageL3IngTrcListUsed':camUsageL3IngTrcListUsed,'camUsageL3IngMcastFibTotal':camUsageL3IngMcastFibTotal,'camUsageL3IngMcastFibUsed':camUsageL3IngMcastFibUsed,'camUsageL3IngQosTotal':camUsageL3IngQosTotal,'camUsageL3IngQosUsed':camUsageL3IngQosUsed,'camUsageL3IngPbrTotal':camUsageL3IngPbrTotal,'camUsageL3IngPbrUsed':camUsageL3IngPbrUsed,'camUsageL3IngAclTotal':camUsageL3IngAclTotal,'camUsageL3IngAclUsed':camUsageL3IngAclUsed,'camUsageL3EgrAclTotal':camUsageL3EgrAclTotal,'camUsageL3EgrAclUsed':camUsageL3EgrAclUsed,_S:camUsageL3PipeLine,'camUsageL3ExtTable':camUsageL3ExtTable,'camUsageL3ExtEntry':camUsageL3ExtEntry,_T:camUsageL3ExtSlot,_U:camUsageL3ExtPipeId,'camUsageL3ExtHostTotal':camUsageL3ExtHostTotal,'camUsageL3ExtHostUsed':camUsageL3ExtHostUsed,'camUsageL3ExtLPMTotal':camUsageL3ExtLPMTotal,'camUsageL3ExtLPMUsed':camUsageL3ExtLPMUsed,'dellNetSysComponentTrap':dellNetSysComponentTrap,'sysCompAlarmMibNotifications':sysCompAlarmMibNotifications,'camUsageThresholdExceed':camUsageThresholdExceed,'camIsFull':camIsFull,'camAuditError':camAuditError,'sysCompAlarmVariable':sysCompAlarmVariable,_F:sysCompAlarmLevel,_G:sysCompAlarmVarString,_H:sysCompSlotId,_I:sysCompPortPipe,_J:sysCompCamPartId})