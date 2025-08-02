_S='adta5kSCMAlarmIndex'
_R='adta5kSCMShelfNumberAddress'
_Q='DisplayString'
_P='adTAeSCUTrapAlarmLevel'
_O='ADTRAN-TAeSCUEXT1-MIB'
_N='adGenSlotInfoIndex'
_M='ADTRAN-GENSLOT-MIB'
_L='read-write'
_K='Integer32'
_J='adta5kSCMEnvAlarmInputLevel'
_I='adta5kSCMEnvAlarmUserName'
_H='sysName'
_G='SNMPv2-MIB'
_F='adTrapInformSeqNum'
_E='ADTRAN-GENTRAPINFORM-MIB'
_D='adta5kSCMShelfNumber'
_C='read-only'
_B='ADTRAN-5KSCM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenSlotInfoIndex,=mibBuilder.importSymbols(_M,_N)
adTrapInformSeqNum,=mibBuilder.importSymbols(_E,_F)
adMgmt,adProducts=mibBuilder.importSymbols('ADTRAN-MIB','adMgmt','adProducts')
adTAeSCUTrapAlarmLevel,=mibBuilder.importSymbols(_O,_P)
AdPresence,=mibBuilder.importSymbols('ADTRAN-TC','AdPresence')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_G,_H)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_Q,'PhysAddress','TextualConvention')
adTA5kSCMmg=ModuleIdentity((1,3,6,1,4,1,664,2,749))
if mibBuilder.loadTexts:adTA5kSCMmg.setRevisions(('2013-09-13 07:52','2011-04-25 13:00','2010-02-24 13:00'))
class Adta5kSCMShelfNumber(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AdTA5kSCM_ObjectIdentity=ObjectIdentity
adTA5kSCM=_AdTA5kSCM_ObjectIdentity((1,3,6,1,4,1,664,1,749))
_AdTA5kSCMNotificationEvents_ObjectIdentity=ObjectIdentity
adTA5kSCMNotificationEvents=_AdTA5kSCMNotificationEvents_ObjectIdentity((1,3,6,1,4,1,664,1,749,0))
if mibBuilder.loadTexts:adTA5kSCMNotificationEvents.setStatus(_A)
_Adta5kSCMMgmt_ObjectIdentity=ObjectIdentity
adta5kSCMMgmt=_Adta5kSCMMgmt_ObjectIdentity((1,3,6,1,4,1,664,2,749,1))
_Adta5kSCMLastChanged_Type=TimeTicks
_Adta5kSCMLastChanged_Object=MibScalar
adta5kSCMLastChanged=_Adta5kSCMLastChanged_Object((1,3,6,1,4,1,664,2,749,1,2),_Adta5kSCMLastChanged_Type())
adta5kSCMLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:adta5kSCMLastChanged.setStatus(_A)
_Adta5kSCMNumberOfShelves_Type=Adta5kSCMShelfNumber
_Adta5kSCMNumberOfShelves_Object=MibScalar
adta5kSCMNumberOfShelves=_Adta5kSCMNumberOfShelves_Object((1,3,6,1,4,1,664,2,749,1,10),_Adta5kSCMNumberOfShelves_Type())
adta5kSCMNumberOfShelves.setMaxAccess(_C)
if mibBuilder.loadTexts:adta5kSCMNumberOfShelves.setStatus(_A)
_Adta5kSCMShelfStatusMgmt_ObjectIdentity=ObjectIdentity
adta5kSCMShelfStatusMgmt=_Adta5kSCMShelfStatusMgmt_ObjectIdentity((1,3,6,1,4,1,664,2,749,1,12))
_Adta5kSCMShelfStatusTable_Object=MibTable
adta5kSCMShelfStatusTable=_Adta5kSCMShelfStatusTable_Object((1,3,6,1,4,1,664,2,749,1,12,1))
if mibBuilder.loadTexts:adta5kSCMShelfStatusTable.setStatus(_A)
_Adta5kSCMShelfStatusEntry_Object=MibTableRow
adta5kSCMShelfStatusEntry=_Adta5kSCMShelfStatusEntry_Object((1,3,6,1,4,1,664,2,749,1,12,1,1))
adta5kSCMShelfStatusEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:adta5kSCMShelfStatusEntry.setStatus(_A)
_Adta5kSCMShelfNumber_Type=Adta5kSCMShelfNumber
_Adta5kSCMShelfNumber_Object=MibTableColumn
adta5kSCMShelfNumber=_Adta5kSCMShelfNumber_Object((1,3,6,1,4,1,664,2,749,1,12,1,1,1),_Adta5kSCMShelfNumber_Type())
adta5kSCMShelfNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:adta5kSCMShelfNumber.setStatus(_A)
_Adta5kSCMShelfInfoState_Type=AdPresence
_Adta5kSCMShelfInfoState_Object=MibTableColumn
adta5kSCMShelfInfoState=_Adta5kSCMShelfInfoState_Object((1,3,6,1,4,1,664,2,749,1,12,1,1,2),_Adta5kSCMShelfInfoState_Type())
adta5kSCMShelfInfoState.setMaxAccess(_C)
if mibBuilder.loadTexts:adta5kSCMShelfInfoState.setStatus(_A)
_Adta5kSCMShelfAlarmStatus_Type=OctetString
_Adta5kSCMShelfAlarmStatus_Object=MibTableColumn
adta5kSCMShelfAlarmStatus=_Adta5kSCMShelfAlarmStatus_Object((1,3,6,1,4,1,664,2,749,1,12,1,1,3),_Adta5kSCMShelfAlarmStatus_Type())
adta5kSCMShelfAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:adta5kSCMShelfAlarmStatus.setStatus(_A)
_Adta5kSCMShelfProvVersion_Type=Integer32
_Adta5kSCMShelfProvVersion_Object=MibTableColumn
adta5kSCMShelfProvVersion=_Adta5kSCMShelfProvVersion_Object((1,3,6,1,4,1,664,2,749,1,12,1,1,4),_Adta5kSCMShelfProvVersion_Type())
adta5kSCMShelfProvVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:adta5kSCMShelfProvVersion.setStatus(_A)
_Adta5kSCMShelfViewAll_Type=OctetString
_Adta5kSCMShelfViewAll_Object=MibTableColumn
adta5kSCMShelfViewAll=_Adta5kSCMShelfViewAll_Object((1,3,6,1,4,1,664,2,749,1,12,1,1,5),_Adta5kSCMShelfViewAll_Type())
adta5kSCMShelfViewAll.setMaxAccess(_C)
if mibBuilder.loadTexts:adta5kSCMShelfViewAll.setStatus(_A)
_Adta5kSCMShelfRelatedAlarmStatus_Type=OctetString
_Adta5kSCMShelfRelatedAlarmStatus_Object=MibTableColumn
adta5kSCMShelfRelatedAlarmStatus=_Adta5kSCMShelfRelatedAlarmStatus_Object((1,3,6,1,4,1,664,2,749,1,12,1,1,6),_Adta5kSCMShelfRelatedAlarmStatus_Type())
adta5kSCMShelfRelatedAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:adta5kSCMShelfRelatedAlarmStatus.setStatus(_A)
_Adta5kSCMShelfXlateFromSlotTable_Object=MibTable
adta5kSCMShelfXlateFromSlotTable=_Adta5kSCMShelfXlateFromSlotTable_Object((1,3,6,1,4,1,664,2,749,1,12,2))
if mibBuilder.loadTexts:adta5kSCMShelfXlateFromSlotTable.setStatus(_A)
_Adta5kSCMShelfXlateFromSlotEntry_Object=MibTableRow
adta5kSCMShelfXlateFromSlotEntry=_Adta5kSCMShelfXlateFromSlotEntry_Object((1,3,6,1,4,1,664,2,749,1,12,2,1))
adta5kSCMShelfXlateFromSlotEntry.setIndexNames((0,_M,_N))
if mibBuilder.loadTexts:adta5kSCMShelfXlateFromSlotEntry.setStatus(_A)
_Adta5kSCMShelfOrdinal_Type=Adta5kSCMShelfNumber
_Adta5kSCMShelfOrdinal_Object=MibTableColumn
adta5kSCMShelfOrdinal=_Adta5kSCMShelfOrdinal_Object((1,3,6,1,4,1,664,2,749,1,12,2,1,1),_Adta5kSCMShelfOrdinal_Type())
adta5kSCMShelfOrdinal.setMaxAccess(_C)
if mibBuilder.loadTexts:adta5kSCMShelfOrdinal.setStatus(_A)
class _Adta5kSCMShelfSlotAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Adta5kSCMShelfSlotAddress_Type.__name__=_K
_Adta5kSCMShelfSlotAddress_Object=MibTableColumn
adta5kSCMShelfSlotAddress=_Adta5kSCMShelfSlotAddress_Object((1,3,6,1,4,1,664,2,749,1,12,2,1,2),_Adta5kSCMShelfSlotAddress_Type())
adta5kSCMShelfSlotAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:adta5kSCMShelfSlotAddress.setStatus(_A)
_Adta5kSCMShelfXlateToSlotTable_Object=MibTable
adta5kSCMShelfXlateToSlotTable=_Adta5kSCMShelfXlateToSlotTable_Object((1,3,6,1,4,1,664,2,749,1,12,3))
if mibBuilder.loadTexts:adta5kSCMShelfXlateToSlotTable.setStatus(_A)
_Adta5kSCMShelfXlateToSlotEntry_Object=MibTableRow
adta5kSCMShelfXlateToSlotEntry=_Adta5kSCMShelfXlateToSlotEntry_Object((1,3,6,1,4,1,664,2,749,1,12,3,1))
adta5kSCMShelfXlateToSlotEntry.setIndexNames((0,_M,_N),(0,_B,_R))
if mibBuilder.loadTexts:adta5kSCMShelfXlateToSlotEntry.setStatus(_A)
class _Adta5kSCMSystemSlotAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Adta5kSCMSystemSlotAddress_Type.__name__=_K
_Adta5kSCMSystemSlotAddress_Object=MibTableColumn
adta5kSCMSystemSlotAddress=_Adta5kSCMSystemSlotAddress_Object((1,3,6,1,4,1,664,2,749,1,12,3,1,1),_Adta5kSCMSystemSlotAddress_Type())
adta5kSCMSystemSlotAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:adta5kSCMSystemSlotAddress.setStatus(_A)
class _Adta5kSCMShelfNumberAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Adta5kSCMShelfNumberAddress_Type.__name__=_K
_Adta5kSCMShelfNumberAddress_Object=MibTableColumn
adta5kSCMShelfNumberAddress=_Adta5kSCMShelfNumberAddress_Object((1,3,6,1,4,1,664,2,749,1,12,3,1,2),_Adta5kSCMShelfNumberAddress_Type())
adta5kSCMShelfNumberAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:adta5kSCMShelfNumberAddress.setStatus(_A)
_Adta5kSCMShelfSlotAlarmStatusTable_Object=MibTable
adta5kSCMShelfSlotAlarmStatusTable=_Adta5kSCMShelfSlotAlarmStatusTable_Object((1,3,6,1,4,1,664,2,749,1,12,4))
if mibBuilder.loadTexts:adta5kSCMShelfSlotAlarmStatusTable.setStatus(_A)
_Adta5kSCMShelfSlotAlarmStatusEntry_Object=MibTableRow
adta5kSCMShelfSlotAlarmStatusEntry=_Adta5kSCMShelfSlotAlarmStatusEntry_Object((1,3,6,1,4,1,664,2,749,1,12,4,1))
adta5kSCMShelfSlotAlarmStatusEntry.setIndexNames((0,_M,_N))
if mibBuilder.loadTexts:adta5kSCMShelfSlotAlarmStatusEntry.setStatus(_A)
_Adta5kSCMShelfSlotAlarmStatus_Type=OctetString
_Adta5kSCMShelfSlotAlarmStatus_Object=MibTableColumn
adta5kSCMShelfSlotAlarmStatus=_Adta5kSCMShelfSlotAlarmStatus_Object((1,3,6,1,4,1,664,2,749,1,12,4,1,1),_Adta5kSCMShelfSlotAlarmStatus_Type())
adta5kSCMShelfSlotAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:adta5kSCMShelfSlotAlarmStatus.setStatus(_A)
_Adta5kSCMUserDefinableAlarm_ObjectIdentity=ObjectIdentity
adta5kSCMUserDefinableAlarm=_Adta5kSCMUserDefinableAlarm_ObjectIdentity((1,3,6,1,4,1,664,2,749,1,15))
_Adta5kSCMEnvAlarmsTable_Object=MibTable
adta5kSCMEnvAlarmsTable=_Adta5kSCMEnvAlarmsTable_Object((1,3,6,1,4,1,664,2,749,1,15,1))
if mibBuilder.loadTexts:adta5kSCMEnvAlarmsTable.setStatus(_A)
_Adta5kSCMEnvAlarmsEntry_Object=MibTableRow
adta5kSCMEnvAlarmsEntry=_Adta5kSCMEnvAlarmsEntry_Object((1,3,6,1,4,1,664,2,749,1,15,1,1))
adta5kSCMEnvAlarmsEntry.setIndexNames((0,_B,_D),(0,_B,_S))
if mibBuilder.loadTexts:adta5kSCMEnvAlarmsEntry.setStatus(_A)
_Adta5kSCMAlarmIndex_Type=Integer32
_Adta5kSCMAlarmIndex_Object=MibTableColumn
adta5kSCMAlarmIndex=_Adta5kSCMAlarmIndex_Object((1,3,6,1,4,1,664,2,749,1,15,1,1,1),_Adta5kSCMAlarmIndex_Type())
adta5kSCMAlarmIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:adta5kSCMAlarmIndex.setStatus(_A)
_Adta5kSCMEnvAlarmDefaultName_Type=DisplayString
_Adta5kSCMEnvAlarmDefaultName_Object=MibTableColumn
adta5kSCMEnvAlarmDefaultName=_Adta5kSCMEnvAlarmDefaultName_Object((1,3,6,1,4,1,664,2,749,1,15,1,1,2),_Adta5kSCMEnvAlarmDefaultName_Type())
adta5kSCMEnvAlarmDefaultName.setMaxAccess(_C)
if mibBuilder.loadTexts:adta5kSCMEnvAlarmDefaultName.setStatus(_A)
class _Adta5kSCMEnvAlarmUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Adta5kSCMEnvAlarmUserName_Type.__name__=_Q
_Adta5kSCMEnvAlarmUserName_Object=MibTableColumn
adta5kSCMEnvAlarmUserName=_Adta5kSCMEnvAlarmUserName_Object((1,3,6,1,4,1,664,2,749,1,15,1,1,3),_Adta5kSCMEnvAlarmUserName_Type())
adta5kSCMEnvAlarmUserName.setMaxAccess(_L)
if mibBuilder.loadTexts:adta5kSCMEnvAlarmUserName.setStatus(_A)
class _Adta5kSCMEnvAlarmInputLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6)));namedValues=NamedValues(*(('info',2),('alert',3),('minor',4),('major',5),('critical',6)))
_Adta5kSCMEnvAlarmInputLevel_Type.__name__=_K
_Adta5kSCMEnvAlarmInputLevel_Object=MibTableColumn
adta5kSCMEnvAlarmInputLevel=_Adta5kSCMEnvAlarmInputLevel_Object((1,3,6,1,4,1,664,2,749,1,15,1,1,4),_Adta5kSCMEnvAlarmInputLevel_Type())
adta5kSCMEnvAlarmInputLevel.setMaxAccess(_L)
if mibBuilder.loadTexts:adta5kSCMEnvAlarmInputLevel.setStatus(_A)
class _Adta5kSCMAIDIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_Adta5kSCMAIDIndex_Type.__name__=_K
_Adta5kSCMAIDIndex_Object=MibTableColumn
adta5kSCMAIDIndex=_Adta5kSCMAIDIndex_Object((1,3,6,1,4,1,664,2,749,1,15,1,1,5),_Adta5kSCMAIDIndex_Type())
adta5kSCMAIDIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:adta5kSCMAIDIndex.setStatus(_A)
class _Adta5kSCMConditionCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,11))
_Adta5kSCMConditionCode_Type.__name__=_Q
_Adta5kSCMConditionCode_Object=MibTableColumn
adta5kSCMConditionCode=_Adta5kSCMConditionCode_Object((1,3,6,1,4,1,664,2,749,1,15,1,1,6),_Adta5kSCMConditionCode_Type())
adta5kSCMConditionCode.setMaxAccess(_L)
if mibBuilder.loadTexts:adta5kSCMConditionCode.setStatus(_A)
_Adta5kSCMScaMgmt_ObjectIdentity=ObjectIdentity
adta5kSCMScaMgmt=_Adta5kSCMScaMgmt_ObjectIdentity((1,3,6,1,4,1,664,2,749,1,16))
_Adta5kSCMScaTable_Object=MibTable
adta5kSCMScaTable=_Adta5kSCMScaTable_Object((1,3,6,1,4,1,664,2,749,1,16,1))
if mibBuilder.loadTexts:adta5kSCMScaTable.setStatus(_A)
_Adta5kSCMScaEntry_Object=MibTableRow
adta5kSCMScaEntry=_Adta5kSCMScaEntry_Object((1,3,6,1,4,1,664,2,749,1,16,1,1))
adta5kSCMScaEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:adta5kSCMScaEntry.setStatus(_A)
_AdTAe5kSCMSCAProvItemChanged_Type=Integer32
_AdTAe5kSCMSCAProvItemChanged_Object=MibTableColumn
adTAe5kSCMSCAProvItemChanged=_AdTAe5kSCMSCAProvItemChanged_Object((1,3,6,1,4,1,664,2,749,1,16,1,1,1),_AdTAe5kSCMSCAProvItemChanged_Type())
adTAe5kSCMSCAProvItemChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:adTAe5kSCMSCAProvItemChanged.setStatus(_A)
_AdTAe5kSCMSCAPresentCards_Type=Integer32
_AdTAe5kSCMSCAPresentCards_Object=MibTableColumn
adTAe5kSCMSCAPresentCards=_AdTAe5kSCMSCAPresentCards_Object((1,3,6,1,4,1,664,2,749,1,16,1,1,2),_AdTAe5kSCMSCAPresentCards_Type())
adTAe5kSCMSCAPresentCards.setMaxAccess(_C)
if mibBuilder.loadTexts:adTAe5kSCMSCAPresentCards.setStatus(_A)
_AdTAe5kSCMSCASlotsWithProvData_Type=Integer32
_AdTAe5kSCMSCASlotsWithProvData_Object=MibTableColumn
adTAe5kSCMSCASlotsWithProvData=_AdTAe5kSCMSCASlotsWithProvData_Object((1,3,6,1,4,1,664,2,749,1,16,1,1,3),_AdTAe5kSCMSCASlotsWithProvData_Type())
adTAe5kSCMSCASlotsWithProvData.setMaxAccess(_C)
if mibBuilder.loadTexts:adTAe5kSCMSCASlotsWithProvData.setStatus(_A)
_AdTAe5kSCMSCAoptRestoreCardBitmask_Type=Integer32
_AdTAe5kSCMSCAoptRestoreCardBitmask_Object=MibTableColumn
adTAe5kSCMSCAoptRestoreCardBitmask=_AdTAe5kSCMSCAoptRestoreCardBitmask_Object((1,3,6,1,4,1,664,2,749,1,16,1,1,4),_AdTAe5kSCMSCAoptRestoreCardBitmask_Type())
adTAe5kSCMSCAoptRestoreCardBitmask.setMaxAccess(_L)
if mibBuilder.loadTexts:adTAe5kSCMSCAoptRestoreCardBitmask.setStatus(_A)
adSCM5kExternalAlmClear=NotificationType((1,3,6,1,4,1,664,1,749,0,74902))
adSCM5kExternalAlmClear.setObjects(*((_E,_F),(_G,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:adSCM5kExternalAlmClear.setStatus(_A)
adSCM5kExternalAlm=NotificationType((1,3,6,1,4,1,664,1,749,0,74903))
adSCM5kExternalAlm.setObjects(*((_E,_F),(_G,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:adSCM5kExternalAlm.setStatus(_A)
adTASCM5kBusApwrAlmClear=NotificationType((1,3,6,1,4,1,664,1,749,0,74904))
adTASCM5kBusApwrAlmClear.setObjects(*((_E,_F),(_G,_H),(_B,_D),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:adTASCM5kBusApwrAlmClear.setStatus(_A)
adTASCM5kBusApowerAlm=NotificationType((1,3,6,1,4,1,664,1,749,0,74905))
adTASCM5kBusApowerAlm.setObjects(*((_E,_F),(_G,_H),(_B,_D),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:adTASCM5kBusApowerAlm.setStatus(_A)
adTASCM5kBusBpwrAlmClear=NotificationType((1,3,6,1,4,1,664,1,749,0,74906))
adTASCM5kBusBpwrAlmClear.setObjects(*((_E,_F),(_G,_H),(_B,_D),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:adTASCM5kBusBpwrAlmClear.setStatus(_A)
adTASCM5kBusBpowerAlm=NotificationType((1,3,6,1,4,1,664,1,749,0,74907))
adTASCM5kBusBpowerAlm.setObjects(*((_E,_F),(_G,_H),(_B,_D),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:adTASCM5kBusBpowerAlm.setStatus(_A)
adTASCM5kChassisLinkStatusUp=NotificationType((1,3,6,1,4,1,664,1,749,0,74908))
adTASCM5kChassisLinkStatusUp.setObjects(*((_E,_F),(_G,_H),(_B,_D),(_O,_P)))
if mibBuilder.loadTexts:adTASCM5kChassisLinkStatusUp.setStatus(_A)
adTASCM5kChassisLinkStatusDown=NotificationType((1,3,6,1,4,1,664,1,749,0,74909))
adTASCM5kChassisLinkStatusDown.setObjects(*((_E,_F),(_G,_H),(_B,_D),(_O,_P)))
if mibBuilder.loadTexts:adTASCM5kChassisLinkStatusDown.setStatus(_A)
adTASCM5kChassisRemoved=NotificationType((1,3,6,1,4,1,664,1,749,0,74910))
adTASCM5kChassisRemoved.setObjects(*((_E,_F),(_G,_H),(_B,_D),(_O,_P)))
if mibBuilder.loadTexts:adTASCM5kChassisRemoved.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'Adta5kSCMShelfNumber':Adta5kSCMShelfNumber,'adTA5kSCM':adTA5kSCM,'adTA5kSCMNotificationEvents':adTA5kSCMNotificationEvents,'adSCM5kExternalAlmClear':adSCM5kExternalAlmClear,'adSCM5kExternalAlm':adSCM5kExternalAlm,'adTASCM5kBusApwrAlmClear':adTASCM5kBusApwrAlmClear,'adTASCM5kBusApowerAlm':adTASCM5kBusApowerAlm,'adTASCM5kBusBpwrAlmClear':adTASCM5kBusBpwrAlmClear,'adTASCM5kBusBpowerAlm':adTASCM5kBusBpowerAlm,'adTASCM5kChassisLinkStatusUp':adTASCM5kChassisLinkStatusUp,'adTASCM5kChassisLinkStatusDown':adTASCM5kChassisLinkStatusDown,'adTASCM5kChassisRemoved':adTASCM5kChassisRemoved,'adTA5kSCMmg':adTA5kSCMmg,'adta5kSCMMgmt':adta5kSCMMgmt,'adta5kSCMLastChanged':adta5kSCMLastChanged,'adta5kSCMNumberOfShelves':adta5kSCMNumberOfShelves,'adta5kSCMShelfStatusMgmt':adta5kSCMShelfStatusMgmt,'adta5kSCMShelfStatusTable':adta5kSCMShelfStatusTable,'adta5kSCMShelfStatusEntry':adta5kSCMShelfStatusEntry,_D:adta5kSCMShelfNumber,'adta5kSCMShelfInfoState':adta5kSCMShelfInfoState,'adta5kSCMShelfAlarmStatus':adta5kSCMShelfAlarmStatus,'adta5kSCMShelfProvVersion':adta5kSCMShelfProvVersion,'adta5kSCMShelfViewAll':adta5kSCMShelfViewAll,'adta5kSCMShelfRelatedAlarmStatus':adta5kSCMShelfRelatedAlarmStatus,'adta5kSCMShelfXlateFromSlotTable':adta5kSCMShelfXlateFromSlotTable,'adta5kSCMShelfXlateFromSlotEntry':adta5kSCMShelfXlateFromSlotEntry,'adta5kSCMShelfOrdinal':adta5kSCMShelfOrdinal,'adta5kSCMShelfSlotAddress':adta5kSCMShelfSlotAddress,'adta5kSCMShelfXlateToSlotTable':adta5kSCMShelfXlateToSlotTable,'adta5kSCMShelfXlateToSlotEntry':adta5kSCMShelfXlateToSlotEntry,'adta5kSCMSystemSlotAddress':adta5kSCMSystemSlotAddress,_R:adta5kSCMShelfNumberAddress,'adta5kSCMShelfSlotAlarmStatusTable':adta5kSCMShelfSlotAlarmStatusTable,'adta5kSCMShelfSlotAlarmStatusEntry':adta5kSCMShelfSlotAlarmStatusEntry,'adta5kSCMShelfSlotAlarmStatus':adta5kSCMShelfSlotAlarmStatus,'adta5kSCMUserDefinableAlarm':adta5kSCMUserDefinableAlarm,'adta5kSCMEnvAlarmsTable':adta5kSCMEnvAlarmsTable,'adta5kSCMEnvAlarmsEntry':adta5kSCMEnvAlarmsEntry,_S:adta5kSCMAlarmIndex,'adta5kSCMEnvAlarmDefaultName':adta5kSCMEnvAlarmDefaultName,_I:adta5kSCMEnvAlarmUserName,_J:adta5kSCMEnvAlarmInputLevel,'adta5kSCMAIDIndex':adta5kSCMAIDIndex,'adta5kSCMConditionCode':adta5kSCMConditionCode,'adta5kSCMScaMgmt':adta5kSCMScaMgmt,'adta5kSCMScaTable':adta5kSCMScaTable,'adta5kSCMScaEntry':adta5kSCMScaEntry,'adTAe5kSCMSCAProvItemChanged':adTAe5kSCMSCAProvItemChanged,'adTAe5kSCMSCAPresentCards':adTAe5kSCMSCAPresentCards,'adTAe5kSCMSCASlotsWithProvData':adTAe5kSCMSCASlotsWithProvData,'adTAe5kSCMSCAoptRestoreCardBitmask':adTAe5kSCMSCAoptRestoreCardBitmask})