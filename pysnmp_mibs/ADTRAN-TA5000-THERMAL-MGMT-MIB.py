_M='adTA5kThermalManagementSensorId'
_L='adTA5kThermalManagementSensorCurrTemp'
_K='read-only'
_J='ifIndex'
_I='IF-MIB'
_H='ADTRAN-TA5000-THERMAL-MGMT-MIB'
_G='sysName'
_F='SNMPv2-MIB'
_E='adTrapInformSeqNum'
_D='ADTRAN-GENTRAPINFORM-MIB'
_C='adGenSlotInfoIndex'
_B='ADTRAN-GENSLOT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenSlotInfoIndex,=mibBuilder.importSymbols(_B,_C)
adTa5kThermalManagement,adTa5kThermalManagementID=mibBuilder.importSymbols('ADTRAN-GENTA5K-MIB','adTa5kThermalManagement','adTa5kThermalManagementID')
adTrapInformSeqNum,=mibBuilder.importSymbols(_D,_E)
adIdentity,adMgmt,adProducts=mibBuilder.importSymbols('ADTRAN-MIB','adIdentity','adMgmt','adProducts')
ifIndex,=mibBuilder.importSymbols(_I,_J)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_F,_G)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
adTa5kThermalMgmtModuleIdentity=ModuleIdentity((1,3,6,1,4,1,664,6,10000,67,1,39,1))
if mibBuilder.loadTexts:adTa5kThermalMgmtModuleIdentity.setRevisions(('2013-11-25 00:00','2013-08-01 21:00'))
_AdTA5kThermalMgmtmg_ObjectIdentity=ObjectIdentity
adTA5kThermalMgmtmg=_AdTA5kThermalMgmtmg_ObjectIdentity((1,3,6,1,4,1,664,5,67,1,39,1))
_AdTA5kThermal_ObjectIdentity=ObjectIdentity
adTA5kThermal=_AdTA5kThermal_ObjectIdentity((1,3,6,1,4,1,664,5,67,1,39,1,1))
_AdTA5kThermalSlotTable_Object=MibTable
adTA5kThermalSlotTable=_AdTA5kThermalSlotTable_Object((1,3,6,1,4,1,664,5,67,1,39,1,1,1))
if mibBuilder.loadTexts:adTA5kThermalSlotTable.setStatus(_A)
_AdTA5kThermalSlotEntry_Object=MibTableRow
adTA5kThermalSlotEntry=_AdTA5kThermalSlotEntry_Object((1,3,6,1,4,1,664,5,67,1,39,1,1,1,1))
adTA5kThermalSlotEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:adTA5kThermalSlotEntry.setStatus(_A)
_AdTA5kThermalSlotNumSensors_Type=Integer32
_AdTA5kThermalSlotNumSensors_Object=MibTableColumn
adTA5kThermalSlotNumSensors=_AdTA5kThermalSlotNumSensors_Object((1,3,6,1,4,1,664,5,67,1,39,1,1,1,1,1),_AdTA5kThermalSlotNumSensors_Type())
adTA5kThermalSlotNumSensors.setMaxAccess(_K)
if mibBuilder.loadTexts:adTA5kThermalSlotNumSensors.setStatus(_A)
_AdTA5kThermalManagementTable_Object=MibTable
adTA5kThermalManagementTable=_AdTA5kThermalManagementTable_Object((1,3,6,1,4,1,664,5,67,1,39,1,1,2))
if mibBuilder.loadTexts:adTA5kThermalManagementTable.setStatus(_A)
_AdTA5kThermalManagementEntry_Object=MibTableRow
adTA5kThermalManagementEntry=_AdTA5kThermalManagementEntry_Object((1,3,6,1,4,1,664,5,67,1,39,1,1,2,1))
adTA5kThermalManagementEntry.setIndexNames((0,_B,_C),(0,_H,_M))
if mibBuilder.loadTexts:adTA5kThermalManagementEntry.setStatus(_A)
_AdTA5kThermalManagementSensorId_Type=Integer32
_AdTA5kThermalManagementSensorId_Object=MibTableColumn
adTA5kThermalManagementSensorId=_AdTA5kThermalManagementSensorId_Object((1,3,6,1,4,1,664,5,67,1,39,1,1,2,1,1),_AdTA5kThermalManagementSensorId_Type())
adTA5kThermalManagementSensorId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:adTA5kThermalManagementSensorId.setStatus(_A)
_AdTA5kThermalManagementSensorName_Type=DisplayString
_AdTA5kThermalManagementSensorName_Object=MibTableColumn
adTA5kThermalManagementSensorName=_AdTA5kThermalManagementSensorName_Object((1,3,6,1,4,1,664,5,67,1,39,1,1,2,1,2),_AdTA5kThermalManagementSensorName_Type())
adTA5kThermalManagementSensorName.setMaxAccess(_K)
if mibBuilder.loadTexts:adTA5kThermalManagementSensorName.setStatus(_A)
_AdTA5kThermalManagementSensorCurrTemp_Type=Integer32
_AdTA5kThermalManagementSensorCurrTemp_Object=MibTableColumn
adTA5kThermalManagementSensorCurrTemp=_AdTA5kThermalManagementSensorCurrTemp_Object((1,3,6,1,4,1,664,5,67,1,39,1,1,2,1,3),_AdTA5kThermalManagementSensorCurrTemp_Type())
adTA5kThermalManagementSensorCurrTemp.setMaxAccess(_K)
if mibBuilder.loadTexts:adTA5kThermalManagementSensorCurrTemp.setStatus(_A)
if mibBuilder.loadTexts:adTA5kThermalManagementSensorCurrTemp.setUnits('0.1C')
_AdTA5kThermalEventsFix_ObjectIdentity=ObjectIdentity
adTA5kThermalEventsFix=_AdTA5kThermalEventsFix_ObjectIdentity((1,3,6,1,4,1,664,5,67,1,39,2))
_AdTa5kThermalEvents_ObjectIdentity=ObjectIdentity
adTa5kThermalEvents=_AdTa5kThermalEvents_ObjectIdentity((1,3,6,1,4,1,664,5,67,1,39,2,0))
adTA5kSlotCriticalTempActive=NotificationType((1,3,6,1,4,1,664,5,67,1,39,2,0,1))
adTA5kSlotCriticalTempActive.setObjects(*((_D,_E),(_F,_G),(_B,_C),(_H,_L)))
if mibBuilder.loadTexts:adTA5kSlotCriticalTempActive.setStatus(_A)
adTA5kSlotCriticalTempClear=NotificationType((1,3,6,1,4,1,664,5,67,1,39,2,0,2))
adTA5kSlotCriticalTempClear.setObjects(*((_D,_E),(_F,_G),(_B,_C),(_H,_L)))
if mibBuilder.loadTexts:adTA5kSlotCriticalTempClear.setStatus(_A)
adTa5kRemoteDeviceCriticalTempActive=NotificationType((1,3,6,1,4,1,664,5,67,1,39,2,0,3))
adTa5kRemoteDeviceCriticalTempActive.setObjects(*((_D,_E),(_F,_G),(_I,_J)))
if mibBuilder.loadTexts:adTa5kRemoteDeviceCriticalTempActive.setStatus(_A)
adTa5kRemoteDeviceCriticalTempClear=NotificationType((1,3,6,1,4,1,664,5,67,1,39,2,0,4))
adTa5kRemoteDeviceCriticalTempClear.setObjects(*((_D,_E),(_F,_G),(_I,_J)))
if mibBuilder.loadTexts:adTa5kRemoteDeviceCriticalTempClear.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'adTA5kThermalMgmtmg':adTA5kThermalMgmtmg,'adTA5kThermal':adTA5kThermal,'adTA5kThermalSlotTable':adTA5kThermalSlotTable,'adTA5kThermalSlotEntry':adTA5kThermalSlotEntry,'adTA5kThermalSlotNumSensors':adTA5kThermalSlotNumSensors,'adTA5kThermalManagementTable':adTA5kThermalManagementTable,'adTA5kThermalManagementEntry':adTA5kThermalManagementEntry,_M:adTA5kThermalManagementSensorId,'adTA5kThermalManagementSensorName':adTA5kThermalManagementSensorName,_L:adTA5kThermalManagementSensorCurrTemp,'adTA5kThermalEventsFix':adTA5kThermalEventsFix,'adTa5kThermalEvents':adTa5kThermalEvents,'adTA5kSlotCriticalTempActive':adTA5kSlotCriticalTempActive,'adTA5kSlotCriticalTempClear':adTA5kSlotCriticalTempClear,'adTa5kRemoteDeviceCriticalTempActive':adTa5kRemoteDeviceCriticalTempActive,'adTa5kRemoteDeviceCriticalTempClear':adTa5kRemoteDeviceCriticalTempClear,'adTa5kThermalMgmtModuleIdentity':adTa5kThermalMgmtModuleIdentity})