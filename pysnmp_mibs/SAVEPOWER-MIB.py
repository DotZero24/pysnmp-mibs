_g='hpicfPHYGroups'
_f='hpicfSavepowerEntPHYGroup'
_e='hpicfSavepowerPHYGroup'
_d='hpicfSavepowerGreenFeaturesGroup'
_c='hpicfSavepowerLEDScalarsGroup'
_b='hpicfSavepowerScalarsGroup'
_a='hpicfSavepowerEntPHYOperStatus'
_Z='hpicfSavepowerEntPHYAdminStatus'
_Y='hpicfSavepowerBlockPorts'
_X='hpicfSavepowerControl'
_W='hpicfSavepowerPHYOperStatus'
_V='hpicfSavepowerPHYAdminStatus'
_U='hpicfSavepowerEntityLEDOperStatus'
_T='hpicfSavepowerEntityLEDAdminStatus'
_S='hpicfSavepowerEntityPowerOperStatus'
_R='hpicfSavepowerEntityPowerAdminStatus'
_Q='hpicfSavePowerLEDOffAlarmRecur'
_P='hpicfSavePowerLEDOffAlarmDuration'
_O='hpicfSavePowerLEDOffAlarmStartTime'
_N='hpicfSavepowerEnabledPorts'
_M='hpicfSavepowerMaxBlocks'
_L='hpicfSavepowerPortNum'
_K='hpicfSavepowerSlotNum'
_J='hpicfSavepowerBlockID'
_I='Unsigned32'
_H='hpicfSavepowerGroup'
_G='not-accessible'
_F='entPhysicalIndex'
_E='ENTITY-MIB'
_D='read-only'
_C='read-write'
_B='SAVEPOWER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_E,_F)
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TruthValue')
hpicfSavepowerMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,56))
if mibBuilder.loadTexts:hpicfSavepowerMIB.setRevisions(('2010-08-12 00:00','2008-10-17 14:30'))
class SavepowerBlockIndex(TextualConvention,Unsigned32):status=_A;displayHint='d'
class SavepowerControl(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('powerOn',1),('powerOff',2)))
_HpicfSavepowerScalars_ObjectIdentity=ObjectIdentity
hpicfSavepowerScalars=_HpicfSavepowerScalars_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,56,1))
_HpicfSavepowerMaxBlocks_Type=Unsigned32
_HpicfSavepowerMaxBlocks_Object=MibScalar
hpicfSavepowerMaxBlocks=_HpicfSavepowerMaxBlocks_Object((1,3,6,1,4,1,11,2,14,11,5,1,56,1,1),_HpicfSavepowerMaxBlocks_Type())
hpicfSavepowerMaxBlocks.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfSavepowerMaxBlocks.setStatus(_A)
class _HpicfSavepowerEnabledPorts_Type(Unsigned32):defaultValue=0
_HpicfSavepowerEnabledPorts_Type.__name__=_I
_HpicfSavepowerEnabledPorts_Object=MibScalar
hpicfSavepowerEnabledPorts=_HpicfSavepowerEnabledPorts_Object((1,3,6,1,4,1,11,2,14,11,5,1,56,1,2),_HpicfSavepowerEnabledPorts_Type())
hpicfSavepowerEnabledPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfSavepowerEnabledPorts.setStatus(_A)
_HpicfSavepowerLEDScalars_ObjectIdentity=ObjectIdentity
hpicfSavepowerLEDScalars=_HpicfSavepowerLEDScalars_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,56,1,3))
_HpicfSavePowerLEDOffAlarmStartTime_Type=DateAndTime
_HpicfSavePowerLEDOffAlarmStartTime_Object=MibScalar
hpicfSavePowerLEDOffAlarmStartTime=_HpicfSavePowerLEDOffAlarmStartTime_Object((1,3,6,1,4,1,11,2,14,11,5,1,56,1,3,1),_HpicfSavePowerLEDOffAlarmStartTime_Type())
hpicfSavePowerLEDOffAlarmStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSavePowerLEDOffAlarmStartTime.setStatus(_A)
_HpicfSavePowerLEDOffAlarmDuration_Type=Unsigned32
_HpicfSavePowerLEDOffAlarmDuration_Object=MibScalar
hpicfSavePowerLEDOffAlarmDuration=_HpicfSavePowerLEDOffAlarmDuration_Object((1,3,6,1,4,1,11,2,14,11,5,1,56,1,3,2),_HpicfSavePowerLEDOffAlarmDuration_Type())
hpicfSavePowerLEDOffAlarmDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSavePowerLEDOffAlarmDuration.setStatus(_A)
_HpicfSavePowerLEDOffAlarmRecur_Type=TruthValue
_HpicfSavePowerLEDOffAlarmRecur_Object=MibScalar
hpicfSavePowerLEDOffAlarmRecur=_HpicfSavePowerLEDOffAlarmRecur_Object((1,3,6,1,4,1,11,2,14,11,5,1,56,1,3,3),_HpicfSavePowerLEDOffAlarmRecur_Type())
hpicfSavePowerLEDOffAlarmRecur.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSavePowerLEDOffAlarmRecur.setStatus(_A)
_HpicfEntitySavepower_ObjectIdentity=ObjectIdentity
hpicfEntitySavepower=_HpicfEntitySavepower_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,56,2))
_HpicfSavepowerTable_Object=MibTable
hpicfSavepowerTable=_HpicfSavepowerTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,56,2,1))
if mibBuilder.loadTexts:hpicfSavepowerTable.setStatus(_A)
_HpicfSavepowerEntry_Object=MibTableRow
hpicfSavepowerEntry=_HpicfSavepowerEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,56,2,1,1))
hpicfSavepowerEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:hpicfSavepowerEntry.setStatus(_A)
_HpicfSavepowerBlockID_Type=SavepowerBlockIndex
_HpicfSavepowerBlockID_Object=MibTableColumn
hpicfSavepowerBlockID=_HpicfSavepowerBlockID_Object((1,3,6,1,4,1,11,2,14,11,5,1,56,2,1,1,1),_HpicfSavepowerBlockID_Type())
hpicfSavepowerBlockID.setMaxAccess(_G)
if mibBuilder.loadTexts:hpicfSavepowerBlockID.setStatus(_A)
_HpicfSavepowerControl_Type=SavepowerControl
_HpicfSavepowerControl_Object=MibTableColumn
hpicfSavepowerControl=_HpicfSavepowerControl_Object((1,3,6,1,4,1,11,2,14,11,5,1,56,2,1,1,2),_HpicfSavepowerControl_Type())
hpicfSavepowerControl.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSavepowerControl.setStatus(_A)
_HpicfSavepowerBlockPorts_Type=DisplayString
_HpicfSavepowerBlockPorts_Object=MibTableColumn
hpicfSavepowerBlockPorts=_HpicfSavepowerBlockPorts_Object((1,3,6,1,4,1,11,2,14,11,5,1,56,2,1,1,3),_HpicfSavepowerBlockPorts_Type())
hpicfSavepowerBlockPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfSavepowerBlockPorts.setStatus(_A)
_HpicfSavepowerGreenFeaturesTable_Object=MibTable
hpicfSavepowerGreenFeaturesTable=_HpicfSavepowerGreenFeaturesTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,56,2,2))
if mibBuilder.loadTexts:hpicfSavepowerGreenFeaturesTable.setStatus(_A)
_HpicfSavepowerGreenFeaturesEntry_Object=MibTableRow
hpicfSavepowerGreenFeaturesEntry=_HpicfSavepowerGreenFeaturesEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,56,2,2,1))
hpicfSavepowerGreenFeaturesEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:hpicfSavepowerGreenFeaturesEntry.setStatus(_A)
_HpicfSavepowerEntityPowerAdminStatus_Type=TruthValue
_HpicfSavepowerEntityPowerAdminStatus_Object=MibTableColumn
hpicfSavepowerEntityPowerAdminStatus=_HpicfSavepowerEntityPowerAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,56,2,2,1,1),_HpicfSavepowerEntityPowerAdminStatus_Type())
hpicfSavepowerEntityPowerAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSavepowerEntityPowerAdminStatus.setStatus(_A)
_HpicfSavepowerEntityPowerOperStatus_Type=SavepowerControl
_HpicfSavepowerEntityPowerOperStatus_Object=MibTableColumn
hpicfSavepowerEntityPowerOperStatus=_HpicfSavepowerEntityPowerOperStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,56,2,2,1,2),_HpicfSavepowerEntityPowerOperStatus_Type())
hpicfSavepowerEntityPowerOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfSavepowerEntityPowerOperStatus.setStatus(_A)
_HpicfSavepowerEntityLEDAdminStatus_Type=TruthValue
_HpicfSavepowerEntityLEDAdminStatus_Object=MibTableColumn
hpicfSavepowerEntityLEDAdminStatus=_HpicfSavepowerEntityLEDAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,56,2,2,1,3),_HpicfSavepowerEntityLEDAdminStatus_Type())
hpicfSavepowerEntityLEDAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSavepowerEntityLEDAdminStatus.setStatus(_A)
_HpicfSavepowerEntityLEDOperStatus_Type=SavepowerControl
_HpicfSavepowerEntityLEDOperStatus_Object=MibTableColumn
hpicfSavepowerEntityLEDOperStatus=_HpicfSavepowerEntityLEDOperStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,56,2,2,1,4),_HpicfSavepowerEntityLEDOperStatus_Type())
hpicfSavepowerEntityLEDOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfSavepowerEntityLEDOperStatus.setStatus(_A)
_HpicfSavepowerPHYTable_Object=MibTable
hpicfSavepowerPHYTable=_HpicfSavepowerPHYTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,56,2,3))
if mibBuilder.loadTexts:hpicfSavepowerPHYTable.setStatus(_A)
_HpicfSavepowerPHYEntry_Object=MibTableRow
hpicfSavepowerPHYEntry=_HpicfSavepowerPHYEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,56,2,3,1))
hpicfSavepowerPHYEntry.setIndexNames((0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:hpicfSavepowerPHYEntry.setStatus(_A)
_HpicfSavepowerSlotNum_Type=Unsigned32
_HpicfSavepowerSlotNum_Object=MibTableColumn
hpicfSavepowerSlotNum=_HpicfSavepowerSlotNum_Object((1,3,6,1,4,1,11,2,14,11,5,1,56,2,3,1,1),_HpicfSavepowerSlotNum_Type())
hpicfSavepowerSlotNum.setMaxAccess(_G)
if mibBuilder.loadTexts:hpicfSavepowerSlotNum.setStatus(_A)
_HpicfSavepowerPortNum_Type=Unsigned32
_HpicfSavepowerPortNum_Object=MibTableColumn
hpicfSavepowerPortNum=_HpicfSavepowerPortNum_Object((1,3,6,1,4,1,11,2,14,11,5,1,56,2,3,1,2),_HpicfSavepowerPortNum_Type())
hpicfSavepowerPortNum.setMaxAccess(_G)
if mibBuilder.loadTexts:hpicfSavepowerPortNum.setStatus(_A)
_HpicfSavepowerPHYAdminStatus_Type=TruthValue
_HpicfSavepowerPHYAdminStatus_Object=MibTableColumn
hpicfSavepowerPHYAdminStatus=_HpicfSavepowerPHYAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,56,2,3,1,3),_HpicfSavepowerPHYAdminStatus_Type())
hpicfSavepowerPHYAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSavepowerPHYAdminStatus.setStatus(_A)
_HpicfSavepowerPHYOperStatus_Type=SavepowerControl
_HpicfSavepowerPHYOperStatus_Object=MibTableColumn
hpicfSavepowerPHYOperStatus=_HpicfSavepowerPHYOperStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,56,2,3,1,4),_HpicfSavepowerPHYOperStatus_Type())
hpicfSavepowerPHYOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfSavepowerPHYOperStatus.setStatus(_A)
_HpicfSavepowerEntPHYTable_Object=MibTable
hpicfSavepowerEntPHYTable=_HpicfSavepowerEntPHYTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,56,2,4))
if mibBuilder.loadTexts:hpicfSavepowerEntPHYTable.setStatus(_A)
_HpicfSavepowerEntPHYEntry_Object=MibTableRow
hpicfSavepowerEntPHYEntry=_HpicfSavepowerEntPHYEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,56,2,4,1))
hpicfSavepowerEntPHYEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:hpicfSavepowerEntPHYEntry.setStatus(_A)
_HpicfSavepowerEntPHYAdminStatus_Type=TruthValue
_HpicfSavepowerEntPHYAdminStatus_Object=MibTableColumn
hpicfSavepowerEntPHYAdminStatus=_HpicfSavepowerEntPHYAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,56,2,4,1,1),_HpicfSavepowerEntPHYAdminStatus_Type())
hpicfSavepowerEntPHYAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSavepowerEntPHYAdminStatus.setStatus(_A)
_HpicfSavepowerEntPHYOperStatus_Type=SavepowerControl
_HpicfSavepowerEntPHYOperStatus_Object=MibTableColumn
hpicfSavepowerEntPHYOperStatus=_HpicfSavepowerEntPHYOperStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,56,2,4,1,2),_HpicfSavepowerEntPHYOperStatus_Type())
hpicfSavepowerEntPHYOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfSavepowerEntPHYOperStatus.setStatus(_A)
_HpicfSavepowerConformance_ObjectIdentity=ObjectIdentity
hpicfSavepowerConformance=_HpicfSavepowerConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,56,3))
_HpicfSavepowerCompliance_ObjectIdentity=ObjectIdentity
hpicfSavepowerCompliance=_HpicfSavepowerCompliance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,56,3,1))
_HpicfSavepowerGroups_ObjectIdentity=ObjectIdentity
hpicfSavepowerGroups=_HpicfSavepowerGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,56,3,2))
_HpicfPHYConformance_ObjectIdentity=ObjectIdentity
hpicfPHYConformance=_HpicfPHYConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,56,4))
_HpicfPHYCompliance_ObjectIdentity=ObjectIdentity
hpicfPHYCompliance=_HpicfPHYCompliance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,56,4,1))
_HpicfPHYGroups_ObjectIdentity=ObjectIdentity
hpicfPHYGroups=_HpicfPHYGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,56,4,2))
hpicfSavepowerScalarsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,56,3,2,1))
hpicfSavepowerScalarsGroup.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:hpicfSavepowerScalarsGroup.setStatus(_A)
hpicfSavepowerLEDScalarsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,56,3,2,2))
hpicfSavepowerLEDScalarsGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:hpicfSavepowerLEDScalarsGroup.setStatus(_A)
hpicfSavepowerGreenFeaturesGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,56,3,2,3))
hpicfSavepowerGreenFeaturesGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:hpicfSavepowerGreenFeaturesGroup.setStatus(_A)
hpicfSavepowerPHYGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,56,3,2,4))
hpicfSavepowerPHYGroup.setObjects(*((_B,_V),(_B,_W)))
if mibBuilder.loadTexts:hpicfSavepowerPHYGroup.setStatus(_A)
hpicfSavepowerGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,56,3,2,5))
hpicfSavepowerGroup.setObjects(*((_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:hpicfSavepowerGroup.setStatus(_A)
hpicfSavepowerEntPHYGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,56,4,2,1))
hpicfSavepowerEntPHYGroup.setObjects(*((_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:hpicfSavepowerEntPHYGroup.setStatus(_A)
hpicfSavepowerComplianceInfo=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,56,3,1,1))
hpicfSavepowerComplianceInfo.setObjects(*((_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_H),(_B,_H)))
if mibBuilder.loadTexts:hpicfSavepowerComplianceInfo.setStatus(_A)
hpicfPHYComplianceInfo=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,56,4,1,1))
hpicfPHYComplianceInfo.setObjects(*((_B,_f),(_B,_g)))
if mibBuilder.loadTexts:hpicfPHYComplianceInfo.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'SavepowerBlockIndex':SavepowerBlockIndex,'SavepowerControl':SavepowerControl,'hpicfSavepowerMIB':hpicfSavepowerMIB,'hpicfSavepowerScalars':hpicfSavepowerScalars,_M:hpicfSavepowerMaxBlocks,_N:hpicfSavepowerEnabledPorts,'hpicfSavepowerLEDScalars':hpicfSavepowerLEDScalars,_O:hpicfSavePowerLEDOffAlarmStartTime,_P:hpicfSavePowerLEDOffAlarmDuration,_Q:hpicfSavePowerLEDOffAlarmRecur,'hpicfEntitySavepower':hpicfEntitySavepower,'hpicfSavepowerTable':hpicfSavepowerTable,'hpicfSavepowerEntry':hpicfSavepowerEntry,_J:hpicfSavepowerBlockID,_X:hpicfSavepowerControl,_Y:hpicfSavepowerBlockPorts,'hpicfSavepowerGreenFeaturesTable':hpicfSavepowerGreenFeaturesTable,'hpicfSavepowerGreenFeaturesEntry':hpicfSavepowerGreenFeaturesEntry,_R:hpicfSavepowerEntityPowerAdminStatus,_S:hpicfSavepowerEntityPowerOperStatus,_T:hpicfSavepowerEntityLEDAdminStatus,_U:hpicfSavepowerEntityLEDOperStatus,'hpicfSavepowerPHYTable':hpicfSavepowerPHYTable,'hpicfSavepowerPHYEntry':hpicfSavepowerPHYEntry,_K:hpicfSavepowerSlotNum,_L:hpicfSavepowerPortNum,_V:hpicfSavepowerPHYAdminStatus,_W:hpicfSavepowerPHYOperStatus,'hpicfSavepowerEntPHYTable':hpicfSavepowerEntPHYTable,'hpicfSavepowerEntPHYEntry':hpicfSavepowerEntPHYEntry,_Z:hpicfSavepowerEntPHYAdminStatus,_a:hpicfSavepowerEntPHYOperStatus,'hpicfSavepowerConformance':hpicfSavepowerConformance,'hpicfSavepowerCompliance':hpicfSavepowerCompliance,'hpicfSavepowerComplianceInfo':hpicfSavepowerComplianceInfo,'hpicfSavepowerGroups':hpicfSavepowerGroups,_b:hpicfSavepowerScalarsGroup,_c:hpicfSavepowerLEDScalarsGroup,_d:hpicfSavepowerGreenFeaturesGroup,_e:hpicfSavepowerPHYGroup,_H:hpicfSavepowerGroup,'hpicfPHYConformance':hpicfPHYConformance,'hpicfPHYCompliance':hpicfPHYCompliance,'hpicfPHYComplianceInfo':hpicfPHYComplianceInfo,_g:hpicfPHYGroups,_f:hpicfSavepowerEntPHYGroup})