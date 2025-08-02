_n='pmPowerMgmtSensorsTableNumber'
_m='pmPowerMgmtSensorsTablePduNumber'
_l='pmPowerMgmtSensorsTablePortNumber'
_k='pmPowerMgmtBanksTableNumber'
_j='pmPowerMgmtBanksTablePduNumber'
_i='pmPowerMgmtBanksTablePortNumber'
_h='pmPowerMgmtPhasesTableNumber'
_g='pmPowerMgmtPhasesTablePduNumber'
_f='pmPowerMgmtPhasesTablePortNumber'
_e='pmPowerMgmtGroupTableIndex'
_d='pmPowerMgmtOutletsTableNumber'
_c='pmPowerMgmtOutletsTablePduNumber'
_b='pmPowerMgmtOutletsTablePortNumber'
_a='pmPowerMgmtPDUTablePduIndex'
_Z='pmPowerMgmtPDUTablePortNumber'
_Y='pmPowerMgmtSerialTableIndex'
_X='pmActiveSessionsTableIndex'
_W='reboot'
_V='powerCycle'
_U='powerOff'
_T='powerOn'
_S='low-critical'
_R='low-warning'
_Q='high-warning'
_P='high-critical'
_O='hw-ocp'
_N='blow-fuse'
_M='normal'
_L='measured'
_K='estimated'
_J='none-sensor'
_I='DisplayString'
_H='PM-MIB'
_G='reset'
_F='obsolete'
_E='noAction'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention')
pm=ModuleIdentity((1,3,6,1,4,1,10418,17))
if mibBuilder.loadTexts:pm.setRevisions(('2010-11-24 00:00','2010-09-24 00:00','2010-04-14 00:00','2009-05-21 00:00'))
_PmProducts_ObjectIdentity=ObjectIdentity
pmProducts=_PmProducts_ObjectIdentity((1,3,6,1,4,1,10418,17,1))
_Pm1024_ObjectIdentity=ObjectIdentity
pm1024=_Pm1024_ObjectIdentity((1,3,6,1,4,1,10418,17,1,1))
_Pm2003_ObjectIdentity=ObjectIdentity
pm2003=_Pm2003_ObjectIdentity((1,3,6,1,4,1,10418,17,1,2))
_Pm2006_ObjectIdentity=ObjectIdentity
pm2006=_Pm2006_ObjectIdentity((1,3,6,1,4,1,10418,17,1,3))
_Pm2024_ObjectIdentity=ObjectIdentity
pm2024=_Pm2024_ObjectIdentity((1,3,6,1,4,1,10418,17,1,4))
_Pm3003_ObjectIdentity=ObjectIdentity
pm3003=_Pm3003_ObjectIdentity((1,3,6,1,4,1,10418,17,1,5))
_Pm3006_ObjectIdentity=ObjectIdentity
pm3006=_Pm3006_ObjectIdentity((1,3,6,1,4,1,10418,17,1,6))
_Pm3024_ObjectIdentity=ObjectIdentity
pm3024=_Pm3024_ObjectIdentity((1,3,6,1,4,1,10418,17,1,7))
_Pm1010_ObjectIdentity=ObjectIdentity
pm1010=_Pm1010_ObjectIdentity((1,3,6,1,4,1,10418,17,1,8))
_Pm2010_ObjectIdentity=ObjectIdentity
pm2010=_Pm2010_ObjectIdentity((1,3,6,1,4,1,10418,17,1,9))
_Pm3010_ObjectIdentity=ObjectIdentity
pm3010=_Pm3010_ObjectIdentity((1,3,6,1,4,1,10418,17,1,10))
_Pm1020_ObjectIdentity=ObjectIdentity
pm1020=_Pm1020_ObjectIdentity((1,3,6,1,4,1,10418,17,1,11))
_Pm2020_ObjectIdentity=ObjectIdentity
pm2020=_Pm2020_ObjectIdentity((1,3,6,1,4,1,10418,17,1,12))
_Pm3020_ObjectIdentity=ObjectIdentity
pm3020=_Pm3020_ObjectIdentity((1,3,6,1,4,1,10418,17,1,13))
_PmManagement_ObjectIdentity=ObjectIdentity
pmManagement=_PmManagement_ObjectIdentity((1,3,6,1,4,1,10418,17,2))
_PmAppliance_ObjectIdentity=ObjectIdentity
pmAppliance=_PmAppliance_ObjectIdentity((1,3,6,1,4,1,10418,17,2,1))
class _PmHostName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_PmHostName_Type.__name__=_I
_PmHostName_Object=MibScalar
pmHostName=_PmHostName_Object((1,3,6,1,4,1,10418,17,2,1,1),_PmHostName_Type())
pmHostName.setMaxAccess(_B)
if mibBuilder.loadTexts:pmHostName.setStatus(_A)
class _PmProductModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_PmProductModel_Type.__name__=_I
_PmProductModel_Object=MibScalar
pmProductModel=_PmProductModel_Object((1,3,6,1,4,1,10418,17,2,1,2),_PmProductModel_Type())
pmProductModel.setMaxAccess(_B)
if mibBuilder.loadTexts:pmProductModel.setStatus(_A)
class _PmPartNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_PmPartNumber_Type.__name__=_I
_PmPartNumber_Object=MibScalar
pmPartNumber=_PmPartNumber_Object((1,3,6,1,4,1,10418,17,2,1,3),_PmPartNumber_Type())
pmPartNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPartNumber.setStatus(_A)
class _PmSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_PmSerialNumber_Type.__name__=_I
_PmSerialNumber_Object=MibScalar
pmSerialNumber=_PmSerialNumber_Object((1,3,6,1,4,1,10418,17,2,1,4),_PmSerialNumber_Type())
pmSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pmSerialNumber.setStatus(_A)
class _PmEIDNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_PmEIDNumber_Type.__name__=_I
_PmEIDNumber_Object=MibScalar
pmEIDNumber=_PmEIDNumber_Object((1,3,6,1,4,1,10418,17,2,1,5),_PmEIDNumber_Type())
pmEIDNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pmEIDNumber.setStatus(_A)
class _PmBootcodeVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_PmBootcodeVersion_Type.__name__=_I
_PmBootcodeVersion_Object=MibScalar
pmBootcodeVersion=_PmBootcodeVersion_Object((1,3,6,1,4,1,10418,17,2,1,6),_PmBootcodeVersion_Type())
pmBootcodeVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:pmBootcodeVersion.setStatus(_A)
class _PmFirmwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_PmFirmwareVersion_Type.__name__=_I
_PmFirmwareVersion_Object=MibScalar
pmFirmwareVersion=_PmFirmwareVersion_Object((1,3,6,1,4,1,10418,17,2,1,7),_PmFirmwareVersion_Type())
pmFirmwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:pmFirmwareVersion.setStatus(_A)
class _PmReboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_W,2)))
_PmReboot_Type.__name__=_D
_PmReboot_Object=MibScalar
pmReboot=_PmReboot_Object((1,3,6,1,4,1,10418,17,2,1,9),_PmReboot_Type())
pmReboot.setMaxAccess(_C)
if mibBuilder.loadTexts:pmReboot.setStatus(_A)
_PmSessions_ObjectIdentity=ObjectIdentity
pmSessions=_PmSessions_ObjectIdentity((1,3,6,1,4,1,10418,17,2,2))
_PmActiveSessionsNumberOfSession_Type=Integer32
_PmActiveSessionsNumberOfSession_Object=MibScalar
pmActiveSessionsNumberOfSession=_PmActiveSessionsNumberOfSession_Object((1,3,6,1,4,1,10418,17,2,2,1),_PmActiveSessionsNumberOfSession_Type())
pmActiveSessionsNumberOfSession.setMaxAccess(_B)
if mibBuilder.loadTexts:pmActiveSessionsNumberOfSession.setStatus(_A)
_PmActiveSessionsTable_Object=MibTable
pmActiveSessionsTable=_PmActiveSessionsTable_Object((1,3,6,1,4,1,10418,17,2,2,2))
if mibBuilder.loadTexts:pmActiveSessionsTable.setStatus(_A)
_PmActiveSessionsTableEntry_Object=MibTableRow
pmActiveSessionsTableEntry=_PmActiveSessionsTableEntry_Object((1,3,6,1,4,1,10418,17,2,2,2,1))
pmActiveSessionsTableEntry.setIndexNames((0,_H,_X))
if mibBuilder.loadTexts:pmActiveSessionsTableEntry.setStatus(_A)
_PmActiveSessionsTableIndex_Type=InterfaceIndexOrZero
_PmActiveSessionsTableIndex_Object=MibTableColumn
pmActiveSessionsTableIndex=_PmActiveSessionsTableIndex_Object((1,3,6,1,4,1,10418,17,2,2,2,1,1),_PmActiveSessionsTableIndex_Type())
pmActiveSessionsTableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmActiveSessionsTableIndex.setStatus(_A)
class _PmActiveSessionsTableUser_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_PmActiveSessionsTableUser_Type.__name__=_I
_PmActiveSessionsTableUser_Object=MibTableColumn
pmActiveSessionsTableUser=_PmActiveSessionsTableUser_Object((1,3,6,1,4,1,10418,17,2,2,2,1,2),_PmActiveSessionsTableUser_Type())
pmActiveSessionsTableUser.setMaxAccess(_B)
if mibBuilder.loadTexts:pmActiveSessionsTableUser.setStatus(_A)
class _PmActiveSessionsTableGroup_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_PmActiveSessionsTableGroup_Type.__name__=_I
_PmActiveSessionsTableGroup_Object=MibTableColumn
pmActiveSessionsTableGroup=_PmActiveSessionsTableGroup_Object((1,3,6,1,4,1,10418,17,2,2,2,1,3),_PmActiveSessionsTableGroup_Type())
pmActiveSessionsTableGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:pmActiveSessionsTableGroup.setStatus(_A)
class _PmActiveSessionsTableType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_PmActiveSessionsTableType_Type.__name__=_I
_PmActiveSessionsTableType_Object=MibTableColumn
pmActiveSessionsTableType=_PmActiveSessionsTableType_Object((1,3,6,1,4,1,10418,17,2,2,2,1,4),_PmActiveSessionsTableType_Type())
pmActiveSessionsTableType.setMaxAccess(_B)
if mibBuilder.loadTexts:pmActiveSessionsTableType.setStatus(_A)
class _PmActiveSessionsTableConnection_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_PmActiveSessionsTableConnection_Type.__name__=_I
_PmActiveSessionsTableConnection_Object=MibTableColumn
pmActiveSessionsTableConnection=_PmActiveSessionsTableConnection_Object((1,3,6,1,4,1,10418,17,2,2,2,1,5),_PmActiveSessionsTableConnection_Type())
pmActiveSessionsTableConnection.setMaxAccess(_B)
if mibBuilder.loadTexts:pmActiveSessionsTableConnection.setStatus(_A)
class _PmActiveSessionsTableSessionTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_PmActiveSessionsTableSessionTime_Type.__name__=_I
_PmActiveSessionsTableSessionTime_Object=MibTableColumn
pmActiveSessionsTableSessionTime=_PmActiveSessionsTableSessionTime_Object((1,3,6,1,4,1,10418,17,2,2,2,1,6),_PmActiveSessionsTableSessionTime_Type())
pmActiveSessionsTableSessionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:pmActiveSessionsTableSessionTime.setStatus(_A)
class _PmActiveSessionsTableFrom_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_PmActiveSessionsTableFrom_Type.__name__=_I
_PmActiveSessionsTableFrom_Object=MibTableColumn
pmActiveSessionsTableFrom=_PmActiveSessionsTableFrom_Object((1,3,6,1,4,1,10418,17,2,2,2,1,7),_PmActiveSessionsTableFrom_Type())
pmActiveSessionsTableFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:pmActiveSessionsTableFrom.setStatus(_A)
class _PmActiveSessionsTableKill_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),('killSession',2)))
_PmActiveSessionsTableKill_Type.__name__=_D
_PmActiveSessionsTableKill_Object=MibTableColumn
pmActiveSessionsTableKill=_PmActiveSessionsTableKill_Object((1,3,6,1,4,1,10418,17,2,2,2,1,8),_PmActiveSessionsTableKill_Type())
pmActiveSessionsTableKill.setMaxAccess(_C)
if mibBuilder.loadTexts:pmActiveSessionsTableKill.setStatus(_A)
_PmPowerMgmt_ObjectIdentity=ObjectIdentity
pmPowerMgmt=_PmPowerMgmt_ObjectIdentity((1,3,6,1,4,1,10418,17,2,5))
_PmPowerMgmtNumSerialPorts_Type=Integer32
_PmPowerMgmtNumSerialPorts_Object=MibScalar
pmPowerMgmtNumSerialPorts=_PmPowerMgmtNumSerialPorts_Object((1,3,6,1,4,1,10418,17,2,5,1),_PmPowerMgmtNumSerialPorts_Type())
pmPowerMgmtNumSerialPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtNumSerialPorts.setStatus(_A)
_PmPowerMgmtSerialTable_Object=MibTable
pmPowerMgmtSerialTable=_PmPowerMgmtSerialTable_Object((1,3,6,1,4,1,10418,17,2,5,2))
if mibBuilder.loadTexts:pmPowerMgmtSerialTable.setStatus(_A)
_PmPowerMgmtSerialTableEntry_Object=MibTableRow
pmPowerMgmtSerialTableEntry=_PmPowerMgmtSerialTableEntry_Object((1,3,6,1,4,1,10418,17,2,5,2,1))
pmPowerMgmtSerialTableEntry.setIndexNames((0,_H,_Y))
if mibBuilder.loadTexts:pmPowerMgmtSerialTableEntry.setStatus(_A)
_PmPowerMgmtSerialTableIndex_Type=InterfaceIndex
_PmPowerMgmtSerialTableIndex_Object=MibTableColumn
pmPowerMgmtSerialTableIndex=_PmPowerMgmtSerialTableIndex_Object((1,3,6,1,4,1,10418,17,2,5,2,1,1),_PmPowerMgmtSerialTableIndex_Type())
pmPowerMgmtSerialTableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtSerialTableIndex.setStatus(_A)
_PmPowerMgmtSerialTablePortNumber_Type=Integer32
_PmPowerMgmtSerialTablePortNumber_Object=MibTableColumn
pmPowerMgmtSerialTablePortNumber=_PmPowerMgmtSerialTablePortNumber_Object((1,3,6,1,4,1,10418,17,2,5,2,1,2),_PmPowerMgmtSerialTablePortNumber_Type())
pmPowerMgmtSerialTablePortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtSerialTablePortNumber.setStatus(_A)
_PmPowerMgmtSerialTableDeviceName_Type=DisplayString
_PmPowerMgmtSerialTableDeviceName_Object=MibTableColumn
pmPowerMgmtSerialTableDeviceName=_PmPowerMgmtSerialTableDeviceName_Object((1,3,6,1,4,1,10418,17,2,5,2,1,3),_PmPowerMgmtSerialTableDeviceName_Type())
pmPowerMgmtSerialTableDeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtSerialTableDeviceName.setStatus(_A)
_PmPowerMgmtSerialTableNumberPDUs_Type=Integer32
_PmPowerMgmtSerialTableNumberPDUs_Object=MibTableColumn
pmPowerMgmtSerialTableNumberPDUs=_PmPowerMgmtSerialTableNumberPDUs_Object((1,3,6,1,4,1,10418,17,2,5,2,1,4),_PmPowerMgmtSerialTableNumberPDUs_Type())
pmPowerMgmtSerialTableNumberPDUs.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtSerialTableNumberPDUs.setStatus(_A)
_PmPowerMgmtSerialTableBuzzer_Type=Integer32
_PmPowerMgmtSerialTableBuzzer_Object=MibTableColumn
pmPowerMgmtSerialTableBuzzer=_PmPowerMgmtSerialTableBuzzer_Object((1,3,6,1,4,1,10418,17,2,5,2,1,10),_PmPowerMgmtSerialTableBuzzer_Type())
pmPowerMgmtSerialTableBuzzer.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtSerialTableBuzzer.setStatus(_A)
_PmPowerMgmtSerialTableSyslog_Type=Integer32
_PmPowerMgmtSerialTableSyslog_Object=MibTableColumn
pmPowerMgmtSerialTableSyslog=_PmPowerMgmtSerialTableSyslog_Object((1,3,6,1,4,1,10418,17,2,5,2,1,11),_PmPowerMgmtSerialTableSyslog_Type())
pmPowerMgmtSerialTableSyslog.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtSerialTableSyslog.setStatus(_A)
_PmPowerMgmtSerialTableOverCurrent_Type=Integer32
_PmPowerMgmtSerialTableOverCurrent_Object=MibTableColumn
pmPowerMgmtSerialTableOverCurrent=_PmPowerMgmtSerialTableOverCurrent_Object((1,3,6,1,4,1,10418,17,2,5,2,1,12),_PmPowerMgmtSerialTableOverCurrent_Type())
pmPowerMgmtSerialTableOverCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtSerialTableOverCurrent.setStatus(_A)
_PmPowerMgmtSerialTableCycleInterval_Type=Integer32
_PmPowerMgmtSerialTableCycleInterval_Object=MibTableColumn
pmPowerMgmtSerialTableCycleInterval=_PmPowerMgmtSerialTableCycleInterval_Object((1,3,6,1,4,1,10418,17,2,5,2,1,13),_PmPowerMgmtSerialTableCycleInterval_Type())
pmPowerMgmtSerialTableCycleInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtSerialTableCycleInterval.setStatus(_A)
_PmPowerMgmtSerialTablePollRate_Type=Integer32
_PmPowerMgmtSerialTablePollRate_Object=MibTableColumn
pmPowerMgmtSerialTablePollRate=_PmPowerMgmtSerialTablePollRate_Object((1,3,6,1,4,1,10418,17,2,5,2,1,14),_PmPowerMgmtSerialTablePollRate_Type())
pmPowerMgmtSerialTablePollRate.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtSerialTablePollRate.setStatus(_A)
_PmPowerMgmtSerialTablePassWord_Type=DisplayString
_PmPowerMgmtSerialTablePassWord_Object=MibTableColumn
pmPowerMgmtSerialTablePassWord=_PmPowerMgmtSerialTablePassWord_Object((1,3,6,1,4,1,10418,17,2,5,2,1,15),_PmPowerMgmtSerialTablePassWord_Type())
pmPowerMgmtSerialTablePassWord.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtSerialTablePassWord.setStatus(_A)
class _PmPowerMgmtSerialTableSave_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),('save',2)))
_PmPowerMgmtSerialTableSave_Type.__name__=_D
_PmPowerMgmtSerialTableSave_Object=MibTableColumn
pmPowerMgmtSerialTableSave=_PmPowerMgmtSerialTableSave_Object((1,3,6,1,4,1,10418,17,2,5,2,1,20),_PmPowerMgmtSerialTableSave_Type())
pmPowerMgmtSerialTableSave.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtSerialTableSave.setStatus(_A)
class _PmPowerMgmtSerialTableRestore_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),('restore',2)))
_PmPowerMgmtSerialTableRestore_Type.__name__=_D
_PmPowerMgmtSerialTableRestore_Object=MibTableColumn
pmPowerMgmtSerialTableRestore=_PmPowerMgmtSerialTableRestore_Object((1,3,6,1,4,1,10418,17,2,5,2,1,21),_PmPowerMgmtSerialTableRestore_Type())
pmPowerMgmtSerialTableRestore.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtSerialTableRestore.setStatus(_A)
_PmPowerMgmtPDUTable_Object=MibTable
pmPowerMgmtPDUTable=_PmPowerMgmtPDUTable_Object((1,3,6,1,4,1,10418,17,2,5,3))
if mibBuilder.loadTexts:pmPowerMgmtPDUTable.setStatus(_A)
_PmPowerMgmtPDUTableEntry_Object=MibTableRow
pmPowerMgmtPDUTableEntry=_PmPowerMgmtPDUTableEntry_Object((1,3,6,1,4,1,10418,17,2,5,3,1))
pmPowerMgmtPDUTableEntry.setIndexNames((0,_H,_Z),(0,_H,_a))
if mibBuilder.loadTexts:pmPowerMgmtPDUTableEntry.setStatus(_A)
_PmPowerMgmtPDUTablePortNumber_Type=InterfaceIndex
_PmPowerMgmtPDUTablePortNumber_Object=MibTableColumn
pmPowerMgmtPDUTablePortNumber=_PmPowerMgmtPDUTablePortNumber_Object((1,3,6,1,4,1,10418,17,2,5,3,1,1),_PmPowerMgmtPDUTablePortNumber_Type())
pmPowerMgmtPDUTablePortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTablePortNumber.setStatus(_A)
_PmPowerMgmtPDUTablePduIndex_Type=InterfaceIndexOrZero
_PmPowerMgmtPDUTablePduIndex_Object=MibTableColumn
pmPowerMgmtPDUTablePduIndex=_PmPowerMgmtPDUTablePduIndex_Object((1,3,6,1,4,1,10418,17,2,5,3,1,2),_PmPowerMgmtPDUTablePduIndex_Type())
pmPowerMgmtPDUTablePduIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTablePduIndex.setStatus(_A)
_PmPowerMgmtPDUTablePduId_Type=DisplayString
_PmPowerMgmtPDUTablePduId_Object=MibTableColumn
pmPowerMgmtPDUTablePduId=_PmPowerMgmtPDUTablePduId_Object((1,3,6,1,4,1,10418,17,2,5,3,1,3),_PmPowerMgmtPDUTablePduId_Type())
pmPowerMgmtPDUTablePduId.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtPDUTablePduId.setStatus(_A)
_PmPowerMgmtPDUTablePortName_Type=DisplayString
_PmPowerMgmtPDUTablePortName_Object=MibTableColumn
pmPowerMgmtPDUTablePortName=_PmPowerMgmtPDUTablePortName_Object((1,3,6,1,4,1,10418,17,2,5,3,1,4),_PmPowerMgmtPDUTablePortName_Type())
pmPowerMgmtPDUTablePortName.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTablePortName.setStatus(_A)
_PmPowerMgmtPDUTableModel_Type=DisplayString
_PmPowerMgmtPDUTableModel_Object=MibTableColumn
pmPowerMgmtPDUTableModel=_PmPowerMgmtPDUTableModel_Object((1,3,6,1,4,1,10418,17,2,5,3,1,5),_PmPowerMgmtPDUTableModel_Type())
pmPowerMgmtPDUTableModel.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableModel.setStatus(_A)
_PmPowerMgmtPDUTableVendor_Type=DisplayString
_PmPowerMgmtPDUTableVendor_Object=MibTableColumn
pmPowerMgmtPDUTableVendor=_PmPowerMgmtPDUTableVendor_Object((1,3,6,1,4,1,10418,17,2,5,3,1,6),_PmPowerMgmtPDUTableVendor_Type())
pmPowerMgmtPDUTableVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableVendor.setStatus(_A)
_PmPowerMgmtPDUTableFirmwareVersion_Type=DisplayString
_PmPowerMgmtPDUTableFirmwareVersion_Object=MibTableColumn
pmPowerMgmtPDUTableFirmwareVersion=_PmPowerMgmtPDUTableFirmwareVersion_Object((1,3,6,1,4,1,10418,17,2,5,3,1,7),_PmPowerMgmtPDUTableFirmwareVersion_Type())
pmPowerMgmtPDUTableFirmwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableFirmwareVersion.setStatus(_A)
_PmPowerMgmtPDUTableNumberOfOutlets_Type=Integer32
_PmPowerMgmtPDUTableNumberOfOutlets_Object=MibTableColumn
pmPowerMgmtPDUTableNumberOfOutlets=_PmPowerMgmtPDUTableNumberOfOutlets_Object((1,3,6,1,4,1,10418,17,2,5,3,1,8),_PmPowerMgmtPDUTableNumberOfOutlets_Type())
pmPowerMgmtPDUTableNumberOfOutlets.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableNumberOfOutlets.setStatus(_A)
_PmPowerMgmtPDUTableCurrentNOS_Type=Integer32
_PmPowerMgmtPDUTableCurrentNOS_Object=MibTableColumn
pmPowerMgmtPDUTableCurrentNOS=_PmPowerMgmtPDUTableCurrentNOS_Object((1,3,6,1,4,1,10418,17,2,5,3,1,9),_PmPowerMgmtPDUTableCurrentNOS_Type())
pmPowerMgmtPDUTableCurrentNOS.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableCurrentNOS.setStatus(_F)
_PmPowerMgmtPDUTableCurrent1Value_Type=Integer32
_PmPowerMgmtPDUTableCurrent1Value_Object=MibTableColumn
pmPowerMgmtPDUTableCurrent1Value=_PmPowerMgmtPDUTableCurrent1Value_Object((1,3,6,1,4,1,10418,17,2,5,3,1,10),_PmPowerMgmtPDUTableCurrent1Value_Type())
pmPowerMgmtPDUTableCurrent1Value.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableCurrent1Value.setStatus(_F)
_PmPowerMgmtPDUTableCurrent1Max_Type=Integer32
_PmPowerMgmtPDUTableCurrent1Max_Object=MibTableColumn
pmPowerMgmtPDUTableCurrent1Max=_PmPowerMgmtPDUTableCurrent1Max_Object((1,3,6,1,4,1,10418,17,2,5,3,1,11),_PmPowerMgmtPDUTableCurrent1Max_Type())
pmPowerMgmtPDUTableCurrent1Max.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableCurrent1Max.setStatus(_F)
_PmPowerMgmtPDUTableCurrent2Value_Type=Integer32
_PmPowerMgmtPDUTableCurrent2Value_Object=MibTableColumn
pmPowerMgmtPDUTableCurrent2Value=_PmPowerMgmtPDUTableCurrent2Value_Object((1,3,6,1,4,1,10418,17,2,5,3,1,12),_PmPowerMgmtPDUTableCurrent2Value_Type())
pmPowerMgmtPDUTableCurrent2Value.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableCurrent2Value.setStatus(_F)
_PmPowerMgmtPDUTableCurrent2Max_Type=Integer32
_PmPowerMgmtPDUTableCurrent2Max_Object=MibTableColumn
pmPowerMgmtPDUTableCurrent2Max=_PmPowerMgmtPDUTableCurrent2Max_Object((1,3,6,1,4,1,10418,17,2,5,3,1,13),_PmPowerMgmtPDUTableCurrent2Max_Type())
pmPowerMgmtPDUTableCurrent2Max.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableCurrent2Max.setStatus(_F)
_PmPowerMgmtPDUTableCurrent3Value_Type=Integer32
_PmPowerMgmtPDUTableCurrent3Value_Object=MibTableColumn
pmPowerMgmtPDUTableCurrent3Value=_PmPowerMgmtPDUTableCurrent3Value_Object((1,3,6,1,4,1,10418,17,2,5,3,1,14),_PmPowerMgmtPDUTableCurrent3Value_Type())
pmPowerMgmtPDUTableCurrent3Value.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableCurrent3Value.setStatus(_F)
_PmPowerMgmtPDUTableCurrent3Max_Type=Integer32
_PmPowerMgmtPDUTableCurrent3Max_Object=MibTableColumn
pmPowerMgmtPDUTableCurrent3Max=_PmPowerMgmtPDUTableCurrent3Max_Object((1,3,6,1,4,1,10418,17,2,5,3,1,15),_PmPowerMgmtPDUTableCurrent3Max_Type())
pmPowerMgmtPDUTableCurrent3Max.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableCurrent3Max.setStatus(_F)
_PmPowerMgmtPDUTableTemperatureNOS_Type=Integer32
_PmPowerMgmtPDUTableTemperatureNOS_Object=MibTableColumn
pmPowerMgmtPDUTableTemperatureNOS=_PmPowerMgmtPDUTableTemperatureNOS_Object((1,3,6,1,4,1,10418,17,2,5,3,1,16),_PmPowerMgmtPDUTableTemperatureNOS_Type())
pmPowerMgmtPDUTableTemperatureNOS.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableTemperatureNOS.setStatus(_F)
_PmPowerMgmtPDUTableTemperature1Value_Type=Integer32
_PmPowerMgmtPDUTableTemperature1Value_Object=MibTableColumn
pmPowerMgmtPDUTableTemperature1Value=_PmPowerMgmtPDUTableTemperature1Value_Object((1,3,6,1,4,1,10418,17,2,5,3,1,17),_PmPowerMgmtPDUTableTemperature1Value_Type())
pmPowerMgmtPDUTableTemperature1Value.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableTemperature1Value.setStatus(_F)
_PmPowerMgmtPDUTableTemperature1Max_Type=Integer32
_PmPowerMgmtPDUTableTemperature1Max_Object=MibTableColumn
pmPowerMgmtPDUTableTemperature1Max=_PmPowerMgmtPDUTableTemperature1Max_Object((1,3,6,1,4,1,10418,17,2,5,3,1,18),_PmPowerMgmtPDUTableTemperature1Max_Type())
pmPowerMgmtPDUTableTemperature1Max.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableTemperature1Max.setStatus(_F)
_PmPowerMgmtPDUTableTemperature2Value_Type=Integer32
_PmPowerMgmtPDUTableTemperature2Value_Object=MibTableColumn
pmPowerMgmtPDUTableTemperature2Value=_PmPowerMgmtPDUTableTemperature2Value_Object((1,3,6,1,4,1,10418,17,2,5,3,1,19),_PmPowerMgmtPDUTableTemperature2Value_Type())
pmPowerMgmtPDUTableTemperature2Value.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableTemperature2Value.setStatus(_F)
_PmPowerMgmtPDUTableTemperature2Max_Type=Integer32
_PmPowerMgmtPDUTableTemperature2Max_Object=MibTableColumn
pmPowerMgmtPDUTableTemperature2Max=_PmPowerMgmtPDUTableTemperature2Max_Object((1,3,6,1,4,1,10418,17,2,5,3,1,20),_PmPowerMgmtPDUTableTemperature2Max_Type())
pmPowerMgmtPDUTableTemperature2Max.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableTemperature2Max.setStatus(_F)
_PmPowerMgmtPDUTableTemperature3Value_Type=Integer32
_PmPowerMgmtPDUTableTemperature3Value_Object=MibTableColumn
pmPowerMgmtPDUTableTemperature3Value=_PmPowerMgmtPDUTableTemperature3Value_Object((1,3,6,1,4,1,10418,17,2,5,3,1,21),_PmPowerMgmtPDUTableTemperature3Value_Type())
pmPowerMgmtPDUTableTemperature3Value.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableTemperature3Value.setStatus(_F)
_PmPowerMgmtPDUTableTemperature3Max_Type=Integer32
_PmPowerMgmtPDUTableTemperature3Max_Object=MibTableColumn
pmPowerMgmtPDUTableTemperature3Max=_PmPowerMgmtPDUTableTemperature3Max_Object((1,3,6,1,4,1,10418,17,2,5,3,1,22),_PmPowerMgmtPDUTableTemperature3Max_Type())
pmPowerMgmtPDUTableTemperature3Max.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableTemperature3Max.setStatus(_F)
_PmPowerMgmtPDUTableHumidityNOS_Type=Integer32
_PmPowerMgmtPDUTableHumidityNOS_Object=MibTableColumn
pmPowerMgmtPDUTableHumidityNOS=_PmPowerMgmtPDUTableHumidityNOS_Object((1,3,6,1,4,1,10418,17,2,5,3,1,23),_PmPowerMgmtPDUTableHumidityNOS_Type())
pmPowerMgmtPDUTableHumidityNOS.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableHumidityNOS.setStatus(_F)
_PmPowerMgmtPDUTableHumidity1Value_Type=Integer32
_PmPowerMgmtPDUTableHumidity1Value_Object=MibTableColumn
pmPowerMgmtPDUTableHumidity1Value=_PmPowerMgmtPDUTableHumidity1Value_Object((1,3,6,1,4,1,10418,17,2,5,3,1,24),_PmPowerMgmtPDUTableHumidity1Value_Type())
pmPowerMgmtPDUTableHumidity1Value.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableHumidity1Value.setStatus(_F)
_PmPowerMgmtPDUTableHumidity1Max_Type=Integer32
_PmPowerMgmtPDUTableHumidity1Max_Object=MibTableColumn
pmPowerMgmtPDUTableHumidity1Max=_PmPowerMgmtPDUTableHumidity1Max_Object((1,3,6,1,4,1,10418,17,2,5,3,1,25),_PmPowerMgmtPDUTableHumidity1Max_Type())
pmPowerMgmtPDUTableHumidity1Max.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableHumidity1Max.setStatus(_F)
_PmPowerMgmtPDUTableHumidity2Value_Type=Integer32
_PmPowerMgmtPDUTableHumidity2Value_Object=MibTableColumn
pmPowerMgmtPDUTableHumidity2Value=_PmPowerMgmtPDUTableHumidity2Value_Object((1,3,6,1,4,1,10418,17,2,5,3,1,26),_PmPowerMgmtPDUTableHumidity2Value_Type())
pmPowerMgmtPDUTableHumidity2Value.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableHumidity2Value.setStatus(_F)
_PmPowerMgmtPDUTableHumidity2Max_Type=Integer32
_PmPowerMgmtPDUTableHumidity2Max_Object=MibTableColumn
pmPowerMgmtPDUTableHumidity2Max=_PmPowerMgmtPDUTableHumidity2Max_Object((1,3,6,1,4,1,10418,17,2,5,3,1,27),_PmPowerMgmtPDUTableHumidity2Max_Type())
pmPowerMgmtPDUTableHumidity2Max.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableHumidity2Max.setStatus(_F)
_PmPowerMgmtPDUTableHumidity3Value_Type=Integer32
_PmPowerMgmtPDUTableHumidity3Value_Object=MibTableColumn
pmPowerMgmtPDUTableHumidity3Value=_PmPowerMgmtPDUTableHumidity3Value_Object((1,3,6,1,4,1,10418,17,2,5,3,1,28),_PmPowerMgmtPDUTableHumidity3Value_Type())
pmPowerMgmtPDUTableHumidity3Value.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableHumidity3Value.setStatus(_F)
_PmPowerMgmtPDUTableHumidity3Max_Type=Integer32
_PmPowerMgmtPDUTableHumidity3Max_Object=MibTableColumn
pmPowerMgmtPDUTableHumidity3Max=_PmPowerMgmtPDUTableHumidity3Max_Object((1,3,6,1,4,1,10418,17,2,5,3,1,29),_PmPowerMgmtPDUTableHumidity3Max_Type())
pmPowerMgmtPDUTableHumidity3Max.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableHumidity3Max.setStatus(_F)
_PmPowerMgmtPDUTableVoltageNOS_Type=Integer32
_PmPowerMgmtPDUTableVoltageNOS_Object=MibTableColumn
pmPowerMgmtPDUTableVoltageNOS=_PmPowerMgmtPDUTableVoltageNOS_Object((1,3,6,1,4,1,10418,17,2,5,3,1,30),_PmPowerMgmtPDUTableVoltageNOS_Type())
pmPowerMgmtPDUTableVoltageNOS.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableVoltageNOS.setStatus(_F)
_PmPowerMgmtPDUTableVoltage1Value_Type=Integer32
_PmPowerMgmtPDUTableVoltage1Value_Object=MibTableColumn
pmPowerMgmtPDUTableVoltage1Value=_PmPowerMgmtPDUTableVoltage1Value_Object((1,3,6,1,4,1,10418,17,2,5,3,1,31),_PmPowerMgmtPDUTableVoltage1Value_Type())
pmPowerMgmtPDUTableVoltage1Value.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableVoltage1Value.setStatus(_F)
_PmPowerMgmtPDUTableVoltage1Max_Type=Integer32
_PmPowerMgmtPDUTableVoltage1Max_Object=MibTableColumn
pmPowerMgmtPDUTableVoltage1Max=_PmPowerMgmtPDUTableVoltage1Max_Object((1,3,6,1,4,1,10418,17,2,5,3,1,32),_PmPowerMgmtPDUTableVoltage1Max_Type())
pmPowerMgmtPDUTableVoltage1Max.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableVoltage1Max.setStatus(_F)
_PmPowerMgmtPDUTableVoltage2Value_Type=Integer32
_PmPowerMgmtPDUTableVoltage2Value_Object=MibTableColumn
pmPowerMgmtPDUTableVoltage2Value=_PmPowerMgmtPDUTableVoltage2Value_Object((1,3,6,1,4,1,10418,17,2,5,3,1,33),_PmPowerMgmtPDUTableVoltage2Value_Type())
pmPowerMgmtPDUTableVoltage2Value.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableVoltage2Value.setStatus(_F)
_PmPowerMgmtPDUTableVoltage2Max_Type=Integer32
_PmPowerMgmtPDUTableVoltage2Max_Object=MibTableColumn
pmPowerMgmtPDUTableVoltage2Max=_PmPowerMgmtPDUTableVoltage2Max_Object((1,3,6,1,4,1,10418,17,2,5,3,1,34),_PmPowerMgmtPDUTableVoltage2Max_Type())
pmPowerMgmtPDUTableVoltage2Max.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableVoltage2Max.setStatus(_F)
_PmPowerMgmtPDUTableVoltage3Value_Type=Integer32
_PmPowerMgmtPDUTableVoltage3Value_Object=MibTableColumn
pmPowerMgmtPDUTableVoltage3Value=_PmPowerMgmtPDUTableVoltage3Value_Object((1,3,6,1,4,1,10418,17,2,5,3,1,35),_PmPowerMgmtPDUTableVoltage3Value_Type())
pmPowerMgmtPDUTableVoltage3Value.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableVoltage3Value.setStatus(_F)
_PmPowerMgmtPDUTableVoltage3Max_Type=Integer32
_PmPowerMgmtPDUTableVoltage3Max_Object=MibTableColumn
pmPowerMgmtPDUTableVoltage3Max=_PmPowerMgmtPDUTableVoltage3Max_Object((1,3,6,1,4,1,10418,17,2,5,3,1,36),_PmPowerMgmtPDUTableVoltage3Max_Type())
pmPowerMgmtPDUTableVoltage3Max.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableVoltage3Max.setStatus(_F)
_PmPowerMgmtPDUTableNumberOfPhases_Type=Integer32
_PmPowerMgmtPDUTableNumberOfPhases_Object=MibTableColumn
pmPowerMgmtPDUTableNumberOfPhases=_PmPowerMgmtPDUTableNumberOfPhases_Object((1,3,6,1,4,1,10418,17,2,5,3,1,37),_PmPowerMgmtPDUTableNumberOfPhases_Type())
pmPowerMgmtPDUTableNumberOfPhases.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableNumberOfPhases.setStatus(_A)
_PmPowerMgmtPDUTableNumberOfBanks_Type=Integer32
_PmPowerMgmtPDUTableNumberOfBanks_Object=MibTableColumn
pmPowerMgmtPDUTableNumberOfBanks=_PmPowerMgmtPDUTableNumberOfBanks_Object((1,3,6,1,4,1,10418,17,2,5,3,1,38),_PmPowerMgmtPDUTableNumberOfBanks_Type())
pmPowerMgmtPDUTableNumberOfBanks.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableNumberOfBanks.setStatus(_A)
_PmPowerMgmtPDUTableNumberOfSensors_Type=Integer32
_PmPowerMgmtPDUTableNumberOfSensors_Object=MibTableColumn
pmPowerMgmtPDUTableNumberOfSensors=_PmPowerMgmtPDUTableNumberOfSensors_Object((1,3,6,1,4,1,10418,17,2,5,3,1,40),_PmPowerMgmtPDUTableNumberOfSensors_Type())
pmPowerMgmtPDUTableNumberOfSensors.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableNumberOfSensors.setStatus(_A)
class _PmPowerMgmtPDUTableFactoryDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_G,2)))
_PmPowerMgmtPDUTableFactoryDefault_Type.__name__=_D
_PmPowerMgmtPDUTableFactoryDefault_Object=MibTableColumn
pmPowerMgmtPDUTableFactoryDefault=_PmPowerMgmtPDUTableFactoryDefault_Object((1,3,6,1,4,1,10418,17,2,5,3,1,41),_PmPowerMgmtPDUTableFactoryDefault_Type())
pmPowerMgmtPDUTableFactoryDefault.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableFactoryDefault.setStatus(_A)
_PmPowerMgmtPDUTableColdStartDelay_Type=Integer32
_PmPowerMgmtPDUTableColdStartDelay_Object=MibTableColumn
pmPowerMgmtPDUTableColdStartDelay=_PmPowerMgmtPDUTableColdStartDelay_Object((1,3,6,1,4,1,10418,17,2,5,3,1,42),_PmPowerMgmtPDUTableColdStartDelay_Type())
pmPowerMgmtPDUTableColdStartDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableColdStartDelay.setStatus(_A)
class _PmPowerMgmtPDUTableReboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_W,2)))
_PmPowerMgmtPDUTableReboot_Type.__name__=_D
_PmPowerMgmtPDUTableReboot_Object=MibTableColumn
pmPowerMgmtPDUTableReboot=_PmPowerMgmtPDUTableReboot_Object((1,3,6,1,4,1,10418,17,2,5,3,1,43),_PmPowerMgmtPDUTableReboot_Type())
pmPowerMgmtPDUTableReboot.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableReboot.setStatus(_A)
_PmPowerMgmtPDUTableMaxCurrent_Type=Integer32
_PmPowerMgmtPDUTableMaxCurrent_Object=MibTableColumn
pmPowerMgmtPDUTableMaxCurrent=_PmPowerMgmtPDUTableMaxCurrent_Object((1,3,6,1,4,1,10418,17,2,5,3,1,44),_PmPowerMgmtPDUTableMaxCurrent_Type())
pmPowerMgmtPDUTableMaxCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableMaxCurrent.setStatus(_A)
class _PmPowerMgmtPDUTableAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3),(_P,4),(_Q,5),(_R,6),(_S,7)))
_PmPowerMgmtPDUTableAlarm_Type.__name__=_D
_PmPowerMgmtPDUTableAlarm_Object=MibTableColumn
pmPowerMgmtPDUTableAlarm=_PmPowerMgmtPDUTableAlarm_Object((1,3,6,1,4,1,10418,17,2,5,3,1,45),_PmPowerMgmtPDUTableAlarm_Type())
pmPowerMgmtPDUTableAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableAlarm.setStatus(_A)
_PmPowerMgmtPDUTableCurrentValue_Type=Integer32
_PmPowerMgmtPDUTableCurrentValue_Object=MibTableColumn
pmPowerMgmtPDUTableCurrentValue=_PmPowerMgmtPDUTableCurrentValue_Object((1,3,6,1,4,1,10418,17,2,5,3,1,50),_PmPowerMgmtPDUTableCurrentValue_Type())
pmPowerMgmtPDUTableCurrentValue.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableCurrentValue.setStatus(_A)
_PmPowerMgmtPDUTableCurrentMax_Type=Integer32
_PmPowerMgmtPDUTableCurrentMax_Object=MibTableColumn
pmPowerMgmtPDUTableCurrentMax=_PmPowerMgmtPDUTableCurrentMax_Object((1,3,6,1,4,1,10418,17,2,5,3,1,51),_PmPowerMgmtPDUTableCurrentMax_Type())
pmPowerMgmtPDUTableCurrentMax.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableCurrentMax.setStatus(_A)
_PmPowerMgmtPDUTableCurrentMin_Type=Integer32
_PmPowerMgmtPDUTableCurrentMin_Object=MibTableColumn
pmPowerMgmtPDUTableCurrentMin=_PmPowerMgmtPDUTableCurrentMin_Object((1,3,6,1,4,1,10418,17,2,5,3,1,52),_PmPowerMgmtPDUTableCurrentMin_Type())
pmPowerMgmtPDUTableCurrentMin.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableCurrentMin.setStatus(_A)
_PmPowerMgmtPDUTableCurrentAvg_Type=Integer32
_PmPowerMgmtPDUTableCurrentAvg_Object=MibTableColumn
pmPowerMgmtPDUTableCurrentAvg=_PmPowerMgmtPDUTableCurrentAvg_Object((1,3,6,1,4,1,10418,17,2,5,3,1,53),_PmPowerMgmtPDUTableCurrentAvg_Type())
pmPowerMgmtPDUTableCurrentAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableCurrentAvg.setStatus(_A)
class _PmPowerMgmtPDUTableCurrentReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_G,2)))
_PmPowerMgmtPDUTableCurrentReset_Type.__name__=_D
_PmPowerMgmtPDUTableCurrentReset_Object=MibTableColumn
pmPowerMgmtPDUTableCurrentReset=_PmPowerMgmtPDUTableCurrentReset_Object((1,3,6,1,4,1,10418,17,2,5,3,1,54),_PmPowerMgmtPDUTableCurrentReset_Type())
pmPowerMgmtPDUTableCurrentReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableCurrentReset.setStatus(_A)
_PmPowerMgmtPDUTablePowerValue_Type=Integer32
_PmPowerMgmtPDUTablePowerValue_Object=MibTableColumn
pmPowerMgmtPDUTablePowerValue=_PmPowerMgmtPDUTablePowerValue_Object((1,3,6,1,4,1,10418,17,2,5,3,1,60),_PmPowerMgmtPDUTablePowerValue_Type())
pmPowerMgmtPDUTablePowerValue.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTablePowerValue.setStatus(_A)
_PmPowerMgmtPDUTablePowerMax_Type=Integer32
_PmPowerMgmtPDUTablePowerMax_Object=MibTableColumn
pmPowerMgmtPDUTablePowerMax=_PmPowerMgmtPDUTablePowerMax_Object((1,3,6,1,4,1,10418,17,2,5,3,1,61),_PmPowerMgmtPDUTablePowerMax_Type())
pmPowerMgmtPDUTablePowerMax.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTablePowerMax.setStatus(_A)
_PmPowerMgmtPDUTablePowerMin_Type=Integer32
_PmPowerMgmtPDUTablePowerMin_Object=MibTableColumn
pmPowerMgmtPDUTablePowerMin=_PmPowerMgmtPDUTablePowerMin_Object((1,3,6,1,4,1,10418,17,2,5,3,1,62),_PmPowerMgmtPDUTablePowerMin_Type())
pmPowerMgmtPDUTablePowerMin.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTablePowerMin.setStatus(_A)
_PmPowerMgmtPDUTablePowerAvg_Type=Integer32
_PmPowerMgmtPDUTablePowerAvg_Object=MibTableColumn
pmPowerMgmtPDUTablePowerAvg=_PmPowerMgmtPDUTablePowerAvg_Object((1,3,6,1,4,1,10418,17,2,5,3,1,63),_PmPowerMgmtPDUTablePowerAvg_Type())
pmPowerMgmtPDUTablePowerAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTablePowerAvg.setStatus(_A)
class _PmPowerMgmtPDUTablePowerReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_G,2)))
_PmPowerMgmtPDUTablePowerReset_Type.__name__=_D
_PmPowerMgmtPDUTablePowerReset_Object=MibTableColumn
pmPowerMgmtPDUTablePowerReset=_PmPowerMgmtPDUTablePowerReset_Object((1,3,6,1,4,1,10418,17,2,5,3,1,64),_PmPowerMgmtPDUTablePowerReset_Type())
pmPowerMgmtPDUTablePowerReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtPDUTablePowerReset.setStatus(_A)
class _PmPowerMgmtPDUTablePowerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),(_K,1),(_L,2)))
_PmPowerMgmtPDUTablePowerType_Type.__name__=_D
_PmPowerMgmtPDUTablePowerType_Object=MibTableColumn
pmPowerMgmtPDUTablePowerType=_PmPowerMgmtPDUTablePowerType_Object((1,3,6,1,4,1,10418,17,2,5,3,1,65),_PmPowerMgmtPDUTablePowerType_Type())
pmPowerMgmtPDUTablePowerType.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTablePowerType.setStatus(_A)
_PmPowerMgmtPDUTableVoltageValue_Type=Integer32
_PmPowerMgmtPDUTableVoltageValue_Object=MibTableColumn
pmPowerMgmtPDUTableVoltageValue=_PmPowerMgmtPDUTableVoltageValue_Object((1,3,6,1,4,1,10418,17,2,5,3,1,70),_PmPowerMgmtPDUTableVoltageValue_Type())
pmPowerMgmtPDUTableVoltageValue.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableVoltageValue.setStatus(_A)
_PmPowerMgmtPDUTableVoltageMax_Type=Integer32
_PmPowerMgmtPDUTableVoltageMax_Object=MibTableColumn
pmPowerMgmtPDUTableVoltageMax=_PmPowerMgmtPDUTableVoltageMax_Object((1,3,6,1,4,1,10418,17,2,5,3,1,71),_PmPowerMgmtPDUTableVoltageMax_Type())
pmPowerMgmtPDUTableVoltageMax.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableVoltageMax.setStatus(_A)
_PmPowerMgmtPDUTableVoltageMin_Type=Integer32
_PmPowerMgmtPDUTableVoltageMin_Object=MibTableColumn
pmPowerMgmtPDUTableVoltageMin=_PmPowerMgmtPDUTableVoltageMin_Object((1,3,6,1,4,1,10418,17,2,5,3,1,72),_PmPowerMgmtPDUTableVoltageMin_Type())
pmPowerMgmtPDUTableVoltageMin.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableVoltageMin.setStatus(_A)
_PmPowerMgmtPDUTableVoltageAvg_Type=Integer32
_PmPowerMgmtPDUTableVoltageAvg_Object=MibTableColumn
pmPowerMgmtPDUTableVoltageAvg=_PmPowerMgmtPDUTableVoltageAvg_Object((1,3,6,1,4,1,10418,17,2,5,3,1,73),_PmPowerMgmtPDUTableVoltageAvg_Type())
pmPowerMgmtPDUTableVoltageAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableVoltageAvg.setStatus(_A)
class _PmPowerMgmtPDUTableVoltageReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_G,2)))
_PmPowerMgmtPDUTableVoltageReset_Type.__name__=_D
_PmPowerMgmtPDUTableVoltageReset_Object=MibTableColumn
pmPowerMgmtPDUTableVoltageReset=_PmPowerMgmtPDUTableVoltageReset_Object((1,3,6,1,4,1,10418,17,2,5,3,1,74),_PmPowerMgmtPDUTableVoltageReset_Type())
pmPowerMgmtPDUTableVoltageReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableVoltageReset.setStatus(_A)
class _PmPowerMgmtPDUTableVoltageType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),(_K,1),(_L,2)))
_PmPowerMgmtPDUTableVoltageType_Type.__name__=_D
_PmPowerMgmtPDUTableVoltageType_Object=MibTableColumn
pmPowerMgmtPDUTableVoltageType=_PmPowerMgmtPDUTableVoltageType_Object((1,3,6,1,4,1,10418,17,2,5,3,1,75),_PmPowerMgmtPDUTableVoltageType_Type())
pmPowerMgmtPDUTableVoltageType.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableVoltageType.setStatus(_A)
_PmPowerMgmtPDUTablePowerFactorValue_Type=Integer32
_PmPowerMgmtPDUTablePowerFactorValue_Object=MibTableColumn
pmPowerMgmtPDUTablePowerFactorValue=_PmPowerMgmtPDUTablePowerFactorValue_Object((1,3,6,1,4,1,10418,17,2,5,3,1,80),_PmPowerMgmtPDUTablePowerFactorValue_Type())
pmPowerMgmtPDUTablePowerFactorValue.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTablePowerFactorValue.setStatus(_A)
_PmPowerMgmtPDUTablePowerFactorMax_Type=Integer32
_PmPowerMgmtPDUTablePowerFactorMax_Object=MibTableColumn
pmPowerMgmtPDUTablePowerFactorMax=_PmPowerMgmtPDUTablePowerFactorMax_Object((1,3,6,1,4,1,10418,17,2,5,3,1,81),_PmPowerMgmtPDUTablePowerFactorMax_Type())
pmPowerMgmtPDUTablePowerFactorMax.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTablePowerFactorMax.setStatus(_A)
_PmPowerMgmtPDUTablePowerFactorMin_Type=Integer32
_PmPowerMgmtPDUTablePowerFactorMin_Object=MibTableColumn
pmPowerMgmtPDUTablePowerFactorMin=_PmPowerMgmtPDUTablePowerFactorMin_Object((1,3,6,1,4,1,10418,17,2,5,3,1,82),_PmPowerMgmtPDUTablePowerFactorMin_Type())
pmPowerMgmtPDUTablePowerFactorMin.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTablePowerFactorMin.setStatus(_A)
_PmPowerMgmtPDUTablePowerFactorAvg_Type=Integer32
_PmPowerMgmtPDUTablePowerFactorAvg_Object=MibTableColumn
pmPowerMgmtPDUTablePowerFactorAvg=_PmPowerMgmtPDUTablePowerFactorAvg_Object((1,3,6,1,4,1,10418,17,2,5,3,1,83),_PmPowerMgmtPDUTablePowerFactorAvg_Type())
pmPowerMgmtPDUTablePowerFactorAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTablePowerFactorAvg.setStatus(_A)
class _PmPowerMgmtPDUTablePowerFactorReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_G,2)))
_PmPowerMgmtPDUTablePowerFactorReset_Type.__name__=_D
_PmPowerMgmtPDUTablePowerFactorReset_Object=MibTableColumn
pmPowerMgmtPDUTablePowerFactorReset=_PmPowerMgmtPDUTablePowerFactorReset_Object((1,3,6,1,4,1,10418,17,2,5,3,1,84),_PmPowerMgmtPDUTablePowerFactorReset_Type())
pmPowerMgmtPDUTablePowerFactorReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtPDUTablePowerFactorReset.setStatus(_A)
class _PmPowerMgmtPDUTablePowerFactorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),(_K,1),(_L,2)))
_PmPowerMgmtPDUTablePowerFactorType_Type.__name__=_D
_PmPowerMgmtPDUTablePowerFactorType_Object=MibTableColumn
pmPowerMgmtPDUTablePowerFactorType=_PmPowerMgmtPDUTablePowerFactorType_Object((1,3,6,1,4,1,10418,17,2,5,3,1,85),_PmPowerMgmtPDUTablePowerFactorType_Type())
pmPowerMgmtPDUTablePowerFactorType.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTablePowerFactorType.setStatus(_A)
class _PmPowerMgmtPDUTablePowerControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_T,2),(_U,3),(_V,4)))
_PmPowerMgmtPDUTablePowerControl_Type.__name__=_D
_PmPowerMgmtPDUTablePowerControl_Object=MibTableColumn
pmPowerMgmtPDUTablePowerControl=_PmPowerMgmtPDUTablePowerControl_Object((1,3,6,1,4,1,10418,17,2,5,3,1,90),_PmPowerMgmtPDUTablePowerControl_Type())
pmPowerMgmtPDUTablePowerControl.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtPDUTablePowerControl.setStatus(_A)
class _PmPowerMgmtPDUTableResetOCP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_G,2)))
_PmPowerMgmtPDUTableResetOCP_Type.__name__=_D
_PmPowerMgmtPDUTableResetOCP_Object=MibTableColumn
pmPowerMgmtPDUTableResetOCP=_PmPowerMgmtPDUTableResetOCP_Object((1,3,6,1,4,1,10418,17,2,5,3,1,91),_PmPowerMgmtPDUTableResetOCP_Type())
pmPowerMgmtPDUTableResetOCP.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableResetOCP.setStatus(_A)
_PmPowerMgmtPDUTableCurrentHighCritical_Type=Integer32
_PmPowerMgmtPDUTableCurrentHighCritical_Object=MibTableColumn
pmPowerMgmtPDUTableCurrentHighCritical=_PmPowerMgmtPDUTableCurrentHighCritical_Object((1,3,6,1,4,1,10418,17,2,5,3,1,100),_PmPowerMgmtPDUTableCurrentHighCritical_Type())
pmPowerMgmtPDUTableCurrentHighCritical.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableCurrentHighCritical.setStatus(_A)
_PmPowerMgmtPDUTableCurrentHighWarning_Type=Integer32
_PmPowerMgmtPDUTableCurrentHighWarning_Object=MibTableColumn
pmPowerMgmtPDUTableCurrentHighWarning=_PmPowerMgmtPDUTableCurrentHighWarning_Object((1,3,6,1,4,1,10418,17,2,5,3,1,101),_PmPowerMgmtPDUTableCurrentHighWarning_Type())
pmPowerMgmtPDUTableCurrentHighWarning.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableCurrentHighWarning.setStatus(_A)
_PmPowerMgmtPDUTableCurrentLowWarning_Type=Integer32
_PmPowerMgmtPDUTableCurrentLowWarning_Object=MibTableColumn
pmPowerMgmtPDUTableCurrentLowWarning=_PmPowerMgmtPDUTableCurrentLowWarning_Object((1,3,6,1,4,1,10418,17,2,5,3,1,102),_PmPowerMgmtPDUTableCurrentLowWarning_Type())
pmPowerMgmtPDUTableCurrentLowWarning.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableCurrentLowWarning.setStatus(_A)
_PmPowerMgmtPDUTableCurrentLowCritical_Type=Integer32
_PmPowerMgmtPDUTableCurrentLowCritical_Object=MibTableColumn
pmPowerMgmtPDUTableCurrentLowCritical=_PmPowerMgmtPDUTableCurrentLowCritical_Object((1,3,6,1,4,1,10418,17,2,5,3,1,103),_PmPowerMgmtPDUTableCurrentLowCritical_Type())
pmPowerMgmtPDUTableCurrentLowCritical.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableCurrentLowCritical.setStatus(_A)
_PmPowerMgmtPDUTableEnergyValue_Type=Integer32
_PmPowerMgmtPDUTableEnergyValue_Object=MibTableColumn
pmPowerMgmtPDUTableEnergyValue=_PmPowerMgmtPDUTableEnergyValue_Object((1,3,6,1,4,1,10418,17,2,5,3,1,105),_PmPowerMgmtPDUTableEnergyValue_Type())
pmPowerMgmtPDUTableEnergyValue.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableEnergyValue.setStatus(_A)
_PmPowerMgmtPDUTableEnergyStartTime_Type=DisplayString
_PmPowerMgmtPDUTableEnergyStartTime_Object=MibTableColumn
pmPowerMgmtPDUTableEnergyStartTime=_PmPowerMgmtPDUTableEnergyStartTime_Object((1,3,6,1,4,1,10418,17,2,5,3,1,106),_PmPowerMgmtPDUTableEnergyStartTime_Type())
pmPowerMgmtPDUTableEnergyStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableEnergyStartTime.setStatus(_A)
class _PmPowerMgmtPDUTableEnergyReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_G,2)))
_PmPowerMgmtPDUTableEnergyReset_Type.__name__=_D
_PmPowerMgmtPDUTableEnergyReset_Object=MibTableColumn
pmPowerMgmtPDUTableEnergyReset=_PmPowerMgmtPDUTableEnergyReset_Object((1,3,6,1,4,1,10418,17,2,5,3,1,107),_PmPowerMgmtPDUTableEnergyReset_Type())
pmPowerMgmtPDUTableEnergyReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtPDUTableEnergyReset.setStatus(_A)
_PmPowerMgmtTotalNumberOfOutlets_Type=Integer32
_PmPowerMgmtTotalNumberOfOutlets_Object=MibScalar
pmPowerMgmtTotalNumberOfOutlets=_PmPowerMgmtTotalNumberOfOutlets_Object((1,3,6,1,4,1,10418,17,2,5,4),_PmPowerMgmtTotalNumberOfOutlets_Type())
pmPowerMgmtTotalNumberOfOutlets.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtTotalNumberOfOutlets.setStatus(_A)
_PmPowerMgmtOutletsTable_Object=MibTable
pmPowerMgmtOutletsTable=_PmPowerMgmtOutletsTable_Object((1,3,6,1,4,1,10418,17,2,5,5))
if mibBuilder.loadTexts:pmPowerMgmtOutletsTable.setStatus(_A)
_PmPowerMgmtOutletsTableEntry_Object=MibTableRow
pmPowerMgmtOutletsTableEntry=_PmPowerMgmtOutletsTableEntry_Object((1,3,6,1,4,1,10418,17,2,5,5,1))
pmPowerMgmtOutletsTableEntry.setIndexNames((0,_H,_b),(0,_H,_c),(0,_H,_d))
if mibBuilder.loadTexts:pmPowerMgmtOutletsTableEntry.setStatus(_A)
_PmPowerMgmtOutletsTablePortNumber_Type=InterfaceIndex
_PmPowerMgmtOutletsTablePortNumber_Object=MibTableColumn
pmPowerMgmtOutletsTablePortNumber=_PmPowerMgmtOutletsTablePortNumber_Object((1,3,6,1,4,1,10418,17,2,5,5,1,1),_PmPowerMgmtOutletsTablePortNumber_Type())
pmPowerMgmtOutletsTablePortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtOutletsTablePortNumber.setStatus(_A)
_PmPowerMgmtOutletsTablePduNumber_Type=InterfaceIndex
_PmPowerMgmtOutletsTablePduNumber_Object=MibTableColumn
pmPowerMgmtOutletsTablePduNumber=_PmPowerMgmtOutletsTablePduNumber_Object((1,3,6,1,4,1,10418,17,2,5,5,1,2),_PmPowerMgmtOutletsTablePduNumber_Type())
pmPowerMgmtOutletsTablePduNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtOutletsTablePduNumber.setStatus(_A)
_PmPowerMgmtOutletsTableNumber_Type=InterfaceIndex
_PmPowerMgmtOutletsTableNumber_Object=MibTableColumn
pmPowerMgmtOutletsTableNumber=_PmPowerMgmtOutletsTableNumber_Object((1,3,6,1,4,1,10418,17,2,5,5,1,3),_PmPowerMgmtOutletsTableNumber_Type())
pmPowerMgmtOutletsTableNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtOutletsTableNumber.setStatus(_A)
_PmPowerMgmtOutletsTableName_Type=DisplayString
_PmPowerMgmtOutletsTableName_Object=MibTableColumn
pmPowerMgmtOutletsTableName=_PmPowerMgmtOutletsTableName_Object((1,3,6,1,4,1,10418,17,2,5,5,1,4),_PmPowerMgmtOutletsTableName_Type())
pmPowerMgmtOutletsTableName.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtOutletsTableName.setStatus(_A)
class _PmPowerMgmtOutletsTableStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('off',1),('on',2),('offLocked',3),('onLocked',4),('offCycle',5),('onPendingOff',6),('offPendingOn',7),('onPendingCycle',8),('notSet',9),('onFixed',10),('offShutdown',11),('tripped',12)))
_PmPowerMgmtOutletsTableStatus_Type.__name__=_D
_PmPowerMgmtOutletsTableStatus_Object=MibTableColumn
pmPowerMgmtOutletsTableStatus=_PmPowerMgmtOutletsTableStatus_Object((1,3,6,1,4,1,10418,17,2,5,5,1,5),_PmPowerMgmtOutletsTableStatus_Type())
pmPowerMgmtOutletsTableStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtOutletsTableStatus.setStatus(_A)
class _PmPowerMgmtOutletsTablePowerControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_T,2),(_U,3),(_V,4),('powerLock',5),('powerUnlock',6)))
_PmPowerMgmtOutletsTablePowerControl_Type.__name__=_D
_PmPowerMgmtOutletsTablePowerControl_Object=MibTableColumn
pmPowerMgmtOutletsTablePowerControl=_PmPowerMgmtOutletsTablePowerControl_Object((1,3,6,1,4,1,10418,17,2,5,5,1,6),_PmPowerMgmtOutletsTablePowerControl_Type())
pmPowerMgmtOutletsTablePowerControl.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtOutletsTablePowerControl.setStatus(_A)
_PmPowerMgmtOutletsTablePortName_Type=DisplayString
_PmPowerMgmtOutletsTablePortName_Object=MibTableColumn
pmPowerMgmtOutletsTablePortName=_PmPowerMgmtOutletsTablePortName_Object((1,3,6,1,4,1,10418,17,2,5,5,1,7),_PmPowerMgmtOutletsTablePortName_Type())
pmPowerMgmtOutletsTablePortName.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtOutletsTablePortName.setStatus(_A)
_PmPowerMgmtOutletsTablePduId_Type=DisplayString
_PmPowerMgmtOutletsTablePduId_Object=MibTableColumn
pmPowerMgmtOutletsTablePduId=_PmPowerMgmtOutletsTablePduId_Object((1,3,6,1,4,1,10418,17,2,5,5,1,8),_PmPowerMgmtOutletsTablePduId_Type())
pmPowerMgmtOutletsTablePduId.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtOutletsTablePduId.setStatus(_A)
_PmPowerMgmtOutletsTablePostOnDelay_Type=Integer32
_PmPowerMgmtOutletsTablePostOnDelay_Object=MibTableColumn
pmPowerMgmtOutletsTablePostOnDelay=_PmPowerMgmtOutletsTablePostOnDelay_Object((1,3,6,1,4,1,10418,17,2,5,5,1,9),_PmPowerMgmtOutletsTablePostOnDelay_Type())
pmPowerMgmtOutletsTablePostOnDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtOutletsTablePostOnDelay.setStatus(_A)
_PmPowerMgmtOutletsTablePostOffDelay_Type=Integer32
_PmPowerMgmtOutletsTablePostOffDelay_Object=MibTableColumn
pmPowerMgmtOutletsTablePostOffDelay=_PmPowerMgmtOutletsTablePostOffDelay_Object((1,3,6,1,4,1,10418,17,2,5,5,1,10),_PmPowerMgmtOutletsTablePostOffDelay_Type())
pmPowerMgmtOutletsTablePostOffDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtOutletsTablePostOffDelay.setStatus(_A)
class _PmPowerMgmtOutletsTableAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3),(_P,4),(_Q,5),(_R,6),(_S,7)))
_PmPowerMgmtOutletsTableAlarm_Type.__name__=_D
_PmPowerMgmtOutletsTableAlarm_Object=MibTableColumn
pmPowerMgmtOutletsTableAlarm=_PmPowerMgmtOutletsTableAlarm_Object((1,3,6,1,4,1,10418,17,2,5,5,1,45),_PmPowerMgmtOutletsTableAlarm_Type())
pmPowerMgmtOutletsTableAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtOutletsTableAlarm.setStatus(_A)
_PmPowerMgmtOutletsTableCurrentValue_Type=Integer32
_PmPowerMgmtOutletsTableCurrentValue_Object=MibTableColumn
pmPowerMgmtOutletsTableCurrentValue=_PmPowerMgmtOutletsTableCurrentValue_Object((1,3,6,1,4,1,10418,17,2,5,5,1,50),_PmPowerMgmtOutletsTableCurrentValue_Type())
pmPowerMgmtOutletsTableCurrentValue.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtOutletsTableCurrentValue.setStatus(_A)
_PmPowerMgmtOutletsTableCurrentMax_Type=Integer32
_PmPowerMgmtOutletsTableCurrentMax_Object=MibTableColumn
pmPowerMgmtOutletsTableCurrentMax=_PmPowerMgmtOutletsTableCurrentMax_Object((1,3,6,1,4,1,10418,17,2,5,5,1,51),_PmPowerMgmtOutletsTableCurrentMax_Type())
pmPowerMgmtOutletsTableCurrentMax.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtOutletsTableCurrentMax.setStatus(_A)
_PmPowerMgmtOutletsTableCurrentMin_Type=Integer32
_PmPowerMgmtOutletsTableCurrentMin_Object=MibTableColumn
pmPowerMgmtOutletsTableCurrentMin=_PmPowerMgmtOutletsTableCurrentMin_Object((1,3,6,1,4,1,10418,17,2,5,5,1,52),_PmPowerMgmtOutletsTableCurrentMin_Type())
pmPowerMgmtOutletsTableCurrentMin.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtOutletsTableCurrentMin.setStatus(_A)
_PmPowerMgmtOutletsTableCurrentAvg_Type=Integer32
_PmPowerMgmtOutletsTableCurrentAvg_Object=MibTableColumn
pmPowerMgmtOutletsTableCurrentAvg=_PmPowerMgmtOutletsTableCurrentAvg_Object((1,3,6,1,4,1,10418,17,2,5,5,1,53),_PmPowerMgmtOutletsTableCurrentAvg_Type())
pmPowerMgmtOutletsTableCurrentAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtOutletsTableCurrentAvg.setStatus(_A)
class _PmPowerMgmtOutletsTableCurrentReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_G,2)))
_PmPowerMgmtOutletsTableCurrentReset_Type.__name__=_D
_PmPowerMgmtOutletsTableCurrentReset_Object=MibTableColumn
pmPowerMgmtOutletsTableCurrentReset=_PmPowerMgmtOutletsTableCurrentReset_Object((1,3,6,1,4,1,10418,17,2,5,5,1,54),_PmPowerMgmtOutletsTableCurrentReset_Type())
pmPowerMgmtOutletsTableCurrentReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtOutletsTableCurrentReset.setStatus(_A)
_PmPowerMgmtOutletsTablePowerValue_Type=Integer32
_PmPowerMgmtOutletsTablePowerValue_Object=MibTableColumn
pmPowerMgmtOutletsTablePowerValue=_PmPowerMgmtOutletsTablePowerValue_Object((1,3,6,1,4,1,10418,17,2,5,5,1,60),_PmPowerMgmtOutletsTablePowerValue_Type())
pmPowerMgmtOutletsTablePowerValue.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtOutletsTablePowerValue.setStatus(_A)
_PmPowerMgmtOutletsTablePowerMax_Type=Integer32
_PmPowerMgmtOutletsTablePowerMax_Object=MibTableColumn
pmPowerMgmtOutletsTablePowerMax=_PmPowerMgmtOutletsTablePowerMax_Object((1,3,6,1,4,1,10418,17,2,5,5,1,61),_PmPowerMgmtOutletsTablePowerMax_Type())
pmPowerMgmtOutletsTablePowerMax.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtOutletsTablePowerMax.setStatus(_A)
_PmPowerMgmtOutletsTablePowerMin_Type=Integer32
_PmPowerMgmtOutletsTablePowerMin_Object=MibTableColumn
pmPowerMgmtOutletsTablePowerMin=_PmPowerMgmtOutletsTablePowerMin_Object((1,3,6,1,4,1,10418,17,2,5,5,1,62),_PmPowerMgmtOutletsTablePowerMin_Type())
pmPowerMgmtOutletsTablePowerMin.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtOutletsTablePowerMin.setStatus(_A)
_PmPowerMgmtOutletsTablePowerAvg_Type=Integer32
_PmPowerMgmtOutletsTablePowerAvg_Object=MibTableColumn
pmPowerMgmtOutletsTablePowerAvg=_PmPowerMgmtOutletsTablePowerAvg_Object((1,3,6,1,4,1,10418,17,2,5,5,1,63),_PmPowerMgmtOutletsTablePowerAvg_Type())
pmPowerMgmtOutletsTablePowerAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtOutletsTablePowerAvg.setStatus(_A)
class _PmPowerMgmtOutletsTablePowerReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_G,2)))
_PmPowerMgmtOutletsTablePowerReset_Type.__name__=_D
_PmPowerMgmtOutletsTablePowerReset_Object=MibTableColumn
pmPowerMgmtOutletsTablePowerReset=_PmPowerMgmtOutletsTablePowerReset_Object((1,3,6,1,4,1,10418,17,2,5,5,1,64),_PmPowerMgmtOutletsTablePowerReset_Type())
pmPowerMgmtOutletsTablePowerReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtOutletsTablePowerReset.setStatus(_A)
class _PmPowerMgmtOutletsTablePowerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),(_K,1),(_L,2)))
_PmPowerMgmtOutletsTablePowerType_Type.__name__=_D
_PmPowerMgmtOutletsTablePowerType_Object=MibTableColumn
pmPowerMgmtOutletsTablePowerType=_PmPowerMgmtOutletsTablePowerType_Object((1,3,6,1,4,1,10418,17,2,5,5,1,65),_PmPowerMgmtOutletsTablePowerType_Type())
pmPowerMgmtOutletsTablePowerType.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtOutletsTablePowerType.setStatus(_A)
_PmPowerMgmtOutletsTableVoltageValue_Type=Integer32
_PmPowerMgmtOutletsTableVoltageValue_Object=MibTableColumn
pmPowerMgmtOutletsTableVoltageValue=_PmPowerMgmtOutletsTableVoltageValue_Object((1,3,6,1,4,1,10418,17,2,5,5,1,70),_PmPowerMgmtOutletsTableVoltageValue_Type())
pmPowerMgmtOutletsTableVoltageValue.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtOutletsTableVoltageValue.setStatus(_A)
_PmPowerMgmtOutletsTableVoltageMax_Type=Integer32
_PmPowerMgmtOutletsTableVoltageMax_Object=MibTableColumn
pmPowerMgmtOutletsTableVoltageMax=_PmPowerMgmtOutletsTableVoltageMax_Object((1,3,6,1,4,1,10418,17,2,5,5,1,71),_PmPowerMgmtOutletsTableVoltageMax_Type())
pmPowerMgmtOutletsTableVoltageMax.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtOutletsTableVoltageMax.setStatus(_A)
_PmPowerMgmtOutletsTableVoltageMin_Type=Integer32
_PmPowerMgmtOutletsTableVoltageMin_Object=MibTableColumn
pmPowerMgmtOutletsTableVoltageMin=_PmPowerMgmtOutletsTableVoltageMin_Object((1,3,6,1,4,1,10418,17,2,5,5,1,72),_PmPowerMgmtOutletsTableVoltageMin_Type())
pmPowerMgmtOutletsTableVoltageMin.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtOutletsTableVoltageMin.setStatus(_A)
_PmPowerMgmtOutletsTableVoltageAvg_Type=Integer32
_PmPowerMgmtOutletsTableVoltageAvg_Object=MibTableColumn
pmPowerMgmtOutletsTableVoltageAvg=_PmPowerMgmtOutletsTableVoltageAvg_Object((1,3,6,1,4,1,10418,17,2,5,5,1,73),_PmPowerMgmtOutletsTableVoltageAvg_Type())
pmPowerMgmtOutletsTableVoltageAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtOutletsTableVoltageAvg.setStatus(_A)
class _PmPowerMgmtOutletsTableVoltageReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_G,2)))
_PmPowerMgmtOutletsTableVoltageReset_Type.__name__=_D
_PmPowerMgmtOutletsTableVoltageReset_Object=MibTableColumn
pmPowerMgmtOutletsTableVoltageReset=_PmPowerMgmtOutletsTableVoltageReset_Object((1,3,6,1,4,1,10418,17,2,5,5,1,74),_PmPowerMgmtOutletsTableVoltageReset_Type())
pmPowerMgmtOutletsTableVoltageReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtOutletsTableVoltageReset.setStatus(_A)
class _PmPowerMgmtOutletsTableVoltageType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),(_K,1),(_L,2)))
_PmPowerMgmtOutletsTableVoltageType_Type.__name__=_D
_PmPowerMgmtOutletsTableVoltageType_Object=MibTableColumn
pmPowerMgmtOutletsTableVoltageType=_PmPowerMgmtOutletsTableVoltageType_Object((1,3,6,1,4,1,10418,17,2,5,5,1,75),_PmPowerMgmtOutletsTableVoltageType_Type())
pmPowerMgmtOutletsTableVoltageType.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtOutletsTableVoltageType.setStatus(_A)
_PmPowerMgmtOutletsTablePowerFactorValue_Type=Integer32
_PmPowerMgmtOutletsTablePowerFactorValue_Object=MibTableColumn
pmPowerMgmtOutletsTablePowerFactorValue=_PmPowerMgmtOutletsTablePowerFactorValue_Object((1,3,6,1,4,1,10418,17,2,5,5,1,80),_PmPowerMgmtOutletsTablePowerFactorValue_Type())
pmPowerMgmtOutletsTablePowerFactorValue.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtOutletsTablePowerFactorValue.setStatus(_A)
_PmPowerMgmtOutletsTablePowerFactorMax_Type=Integer32
_PmPowerMgmtOutletsTablePowerFactorMax_Object=MibTableColumn
pmPowerMgmtOutletsTablePowerFactorMax=_PmPowerMgmtOutletsTablePowerFactorMax_Object((1,3,6,1,4,1,10418,17,2,5,5,1,81),_PmPowerMgmtOutletsTablePowerFactorMax_Type())
pmPowerMgmtOutletsTablePowerFactorMax.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtOutletsTablePowerFactorMax.setStatus(_A)
_PmPowerMgmtOutletsTablePowerFactorMin_Type=Integer32
_PmPowerMgmtOutletsTablePowerFactorMin_Object=MibTableColumn
pmPowerMgmtOutletsTablePowerFactorMin=_PmPowerMgmtOutletsTablePowerFactorMin_Object((1,3,6,1,4,1,10418,17,2,5,5,1,82),_PmPowerMgmtOutletsTablePowerFactorMin_Type())
pmPowerMgmtOutletsTablePowerFactorMin.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtOutletsTablePowerFactorMin.setStatus(_A)
_PmPowerMgmtOutletsTablePowerFactorAvg_Type=Integer32
_PmPowerMgmtOutletsTablePowerFactorAvg_Object=MibTableColumn
pmPowerMgmtOutletsTablePowerFactorAvg=_PmPowerMgmtOutletsTablePowerFactorAvg_Object((1,3,6,1,4,1,10418,17,2,5,5,1,83),_PmPowerMgmtOutletsTablePowerFactorAvg_Type())
pmPowerMgmtOutletsTablePowerFactorAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtOutletsTablePowerFactorAvg.setStatus(_A)
class _PmPowerMgmtOutletsTablePowerFactorReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_G,2)))
_PmPowerMgmtOutletsTablePowerFactorReset_Type.__name__=_D
_PmPowerMgmtOutletsTablePowerFactorReset_Object=MibTableColumn
pmPowerMgmtOutletsTablePowerFactorReset=_PmPowerMgmtOutletsTablePowerFactorReset_Object((1,3,6,1,4,1,10418,17,2,5,5,1,84),_PmPowerMgmtOutletsTablePowerFactorReset_Type())
pmPowerMgmtOutletsTablePowerFactorReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtOutletsTablePowerFactorReset.setStatus(_A)
class _PmPowerMgmtOutletsTablePowerFactorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),(_K,1),(_L,2)))
_PmPowerMgmtOutletsTablePowerFactorType_Type.__name__=_D
_PmPowerMgmtOutletsTablePowerFactorType_Object=MibTableColumn
pmPowerMgmtOutletsTablePowerFactorType=_PmPowerMgmtOutletsTablePowerFactorType_Object((1,3,6,1,4,1,10418,17,2,5,5,1,85),_PmPowerMgmtOutletsTablePowerFactorType_Type())
pmPowerMgmtOutletsTablePowerFactorType.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtOutletsTablePowerFactorType.setStatus(_A)
_PmPowerMgmtOutletsTableCurrentHighCritical_Type=Integer32
_PmPowerMgmtOutletsTableCurrentHighCritical_Object=MibTableColumn
pmPowerMgmtOutletsTableCurrentHighCritical=_PmPowerMgmtOutletsTableCurrentHighCritical_Object((1,3,6,1,4,1,10418,17,2,5,5,1,100),_PmPowerMgmtOutletsTableCurrentHighCritical_Type())
pmPowerMgmtOutletsTableCurrentHighCritical.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtOutletsTableCurrentHighCritical.setStatus(_A)
_PmPowerMgmtOutletsTableCurrentHighWarning_Type=Integer32
_PmPowerMgmtOutletsTableCurrentHighWarning_Object=MibTableColumn
pmPowerMgmtOutletsTableCurrentHighWarning=_PmPowerMgmtOutletsTableCurrentHighWarning_Object((1,3,6,1,4,1,10418,17,2,5,5,1,101),_PmPowerMgmtOutletsTableCurrentHighWarning_Type())
pmPowerMgmtOutletsTableCurrentHighWarning.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtOutletsTableCurrentHighWarning.setStatus(_A)
_PmPowerMgmtOutletsTableCurrentLowWarning_Type=Integer32
_PmPowerMgmtOutletsTableCurrentLowWarning_Object=MibTableColumn
pmPowerMgmtOutletsTableCurrentLowWarning=_PmPowerMgmtOutletsTableCurrentLowWarning_Object((1,3,6,1,4,1,10418,17,2,5,5,1,102),_PmPowerMgmtOutletsTableCurrentLowWarning_Type())
pmPowerMgmtOutletsTableCurrentLowWarning.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtOutletsTableCurrentLowWarning.setStatus(_A)
_PmPowerMgmtOutletsTableCurrentLowCritical_Type=Integer32
_PmPowerMgmtOutletsTableCurrentLowCritical_Object=MibTableColumn
pmPowerMgmtOutletsTableCurrentLowCritical=_PmPowerMgmtOutletsTableCurrentLowCritical_Object((1,3,6,1,4,1,10418,17,2,5,5,1,103),_PmPowerMgmtOutletsTableCurrentLowCritical_Type())
pmPowerMgmtOutletsTableCurrentLowCritical.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtOutletsTableCurrentLowCritical.setStatus(_A)
_PmPowerMgmtOutletsTableEnergyValue_Type=Integer32
_PmPowerMgmtOutletsTableEnergyValue_Object=MibTableColumn
pmPowerMgmtOutletsTableEnergyValue=_PmPowerMgmtOutletsTableEnergyValue_Object((1,3,6,1,4,1,10418,17,2,5,5,1,105),_PmPowerMgmtOutletsTableEnergyValue_Type())
pmPowerMgmtOutletsTableEnergyValue.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtOutletsTableEnergyValue.setStatus(_A)
_PmPowerMgmtOutletsTableEnergyStartTime_Type=DisplayString
_PmPowerMgmtOutletsTableEnergyStartTime_Object=MibTableColumn
pmPowerMgmtOutletsTableEnergyStartTime=_PmPowerMgmtOutletsTableEnergyStartTime_Object((1,3,6,1,4,1,10418,17,2,5,5,1,106),_PmPowerMgmtOutletsTableEnergyStartTime_Type())
pmPowerMgmtOutletsTableEnergyStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtOutletsTableEnergyStartTime.setStatus(_A)
class _PmPowerMgmtOutletsTableEnergyReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_G,2)))
_PmPowerMgmtOutletsTableEnergyReset_Type.__name__=_D
_PmPowerMgmtOutletsTableEnergyReset_Object=MibTableColumn
pmPowerMgmtOutletsTableEnergyReset=_PmPowerMgmtOutletsTableEnergyReset_Object((1,3,6,1,4,1,10418,17,2,5,5,1,107),_PmPowerMgmtOutletsTableEnergyReset_Type())
pmPowerMgmtOutletsTableEnergyReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtOutletsTableEnergyReset.setStatus(_A)
_PmPowerMgmtNumberOfOutletGroup_Type=Integer32
_PmPowerMgmtNumberOfOutletGroup_Object=MibScalar
pmPowerMgmtNumberOfOutletGroup=_PmPowerMgmtNumberOfOutletGroup_Object((1,3,6,1,4,1,10418,17,2,5,6),_PmPowerMgmtNumberOfOutletGroup_Type())
pmPowerMgmtNumberOfOutletGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtNumberOfOutletGroup.setStatus(_A)
_PmPowerMgmtGroupTable_Object=MibTable
pmPowerMgmtGroupTable=_PmPowerMgmtGroupTable_Object((1,3,6,1,4,1,10418,17,2,5,7))
if mibBuilder.loadTexts:pmPowerMgmtGroupTable.setStatus(_A)
_PmPowerMgmtGroupTableEntry_Object=MibTableRow
pmPowerMgmtGroupTableEntry=_PmPowerMgmtGroupTableEntry_Object((1,3,6,1,4,1,10418,17,2,5,7,1))
pmPowerMgmtGroupTableEntry.setIndexNames((0,_H,_e))
if mibBuilder.loadTexts:pmPowerMgmtGroupTableEntry.setStatus(_A)
_PmPowerMgmtGroupTableIndex_Type=InterfaceIndexOrZero
_PmPowerMgmtGroupTableIndex_Object=MibTableColumn
pmPowerMgmtGroupTableIndex=_PmPowerMgmtGroupTableIndex_Object((1,3,6,1,4,1,10418,17,2,5,7,1,1),_PmPowerMgmtGroupTableIndex_Type())
pmPowerMgmtGroupTableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtGroupTableIndex.setStatus(_A)
_PmPowerMgmtGroupTableName_Type=DisplayString
_PmPowerMgmtGroupTableName_Object=MibTableColumn
pmPowerMgmtGroupTableName=_PmPowerMgmtGroupTableName_Object((1,3,6,1,4,1,10418,17,2,5,7,1,2),_PmPowerMgmtGroupTableName_Type())
pmPowerMgmtGroupTableName.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtGroupTableName.setStatus(_A)
class _PmPowerMgmtGroupTableStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_PmPowerMgmtGroupTableStatus_Type.__name__=_D
_PmPowerMgmtGroupTableStatus_Object=MibTableColumn
pmPowerMgmtGroupTableStatus=_PmPowerMgmtGroupTableStatus_Object((1,3,6,1,4,1,10418,17,2,5,7,1,3),_PmPowerMgmtGroupTableStatus_Type())
pmPowerMgmtGroupTableStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtGroupTableStatus.setStatus(_A)
class _PmPowerMgmtGroupTablePowerControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_T,2),(_U,3),(_V,4)))
_PmPowerMgmtGroupTablePowerControl_Type.__name__=_D
_PmPowerMgmtGroupTablePowerControl_Object=MibTableColumn
pmPowerMgmtGroupTablePowerControl=_PmPowerMgmtGroupTablePowerControl_Object((1,3,6,1,4,1,10418,17,2,5,7,1,4),_PmPowerMgmtGroupTablePowerControl_Type())
pmPowerMgmtGroupTablePowerControl.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtGroupTablePowerControl.setStatus(_A)
_PmPowerMgmtTotalNumberOfPhases_Type=Integer32
_PmPowerMgmtTotalNumberOfPhases_Object=MibScalar
pmPowerMgmtTotalNumberOfPhases=_PmPowerMgmtTotalNumberOfPhases_Object((1,3,6,1,4,1,10418,17,2,5,8),_PmPowerMgmtTotalNumberOfPhases_Type())
pmPowerMgmtTotalNumberOfPhases.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtTotalNumberOfPhases.setStatus(_A)
_PmPowerMgmtPhasesTable_Object=MibTable
pmPowerMgmtPhasesTable=_PmPowerMgmtPhasesTable_Object((1,3,6,1,4,1,10418,17,2,5,9))
if mibBuilder.loadTexts:pmPowerMgmtPhasesTable.setStatus(_A)
_PmPowerMgmtPhasesTableEntry_Object=MibTableRow
pmPowerMgmtPhasesTableEntry=_PmPowerMgmtPhasesTableEntry_Object((1,3,6,1,4,1,10418,17,2,5,9,1))
pmPowerMgmtPhasesTableEntry.setIndexNames((0,_H,_f),(0,_H,_g),(0,_H,_h))
if mibBuilder.loadTexts:pmPowerMgmtPhasesTableEntry.setStatus(_A)
_PmPowerMgmtPhasesTablePortNumber_Type=InterfaceIndex
_PmPowerMgmtPhasesTablePortNumber_Object=MibTableColumn
pmPowerMgmtPhasesTablePortNumber=_PmPowerMgmtPhasesTablePortNumber_Object((1,3,6,1,4,1,10418,17,2,5,9,1,1),_PmPowerMgmtPhasesTablePortNumber_Type())
pmPowerMgmtPhasesTablePortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPhasesTablePortNumber.setStatus(_A)
_PmPowerMgmtPhasesTablePduNumber_Type=InterfaceIndex
_PmPowerMgmtPhasesTablePduNumber_Object=MibTableColumn
pmPowerMgmtPhasesTablePduNumber=_PmPowerMgmtPhasesTablePduNumber_Object((1,3,6,1,4,1,10418,17,2,5,9,1,2),_PmPowerMgmtPhasesTablePduNumber_Type())
pmPowerMgmtPhasesTablePduNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPhasesTablePduNumber.setStatus(_A)
_PmPowerMgmtPhasesTableNumber_Type=InterfaceIndex
_PmPowerMgmtPhasesTableNumber_Object=MibTableColumn
pmPowerMgmtPhasesTableNumber=_PmPowerMgmtPhasesTableNumber_Object((1,3,6,1,4,1,10418,17,2,5,9,1,3),_PmPowerMgmtPhasesTableNumber_Type())
pmPowerMgmtPhasesTableNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPhasesTableNumber.setStatus(_A)
_PmPowerMgmtPhasesTableName_Type=DisplayString
_PmPowerMgmtPhasesTableName_Object=MibTableColumn
pmPowerMgmtPhasesTableName=_PmPowerMgmtPhasesTableName_Object((1,3,6,1,4,1,10418,17,2,5,9,1,4),_PmPowerMgmtPhasesTableName_Type())
pmPowerMgmtPhasesTableName.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPhasesTableName.setStatus(_A)
_PmPowerMgmtPhasesTablePortName_Type=DisplayString
_PmPowerMgmtPhasesTablePortName_Object=MibTableColumn
pmPowerMgmtPhasesTablePortName=_PmPowerMgmtPhasesTablePortName_Object((1,3,6,1,4,1,10418,17,2,5,9,1,5),_PmPowerMgmtPhasesTablePortName_Type())
pmPowerMgmtPhasesTablePortName.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPhasesTablePortName.setStatus(_A)
_PmPowerMgmtPhasesTablePduId_Type=DisplayString
_PmPowerMgmtPhasesTablePduId_Object=MibTableColumn
pmPowerMgmtPhasesTablePduId=_PmPowerMgmtPhasesTablePduId_Object((1,3,6,1,4,1,10418,17,2,5,9,1,6),_PmPowerMgmtPhasesTablePduId_Type())
pmPowerMgmtPhasesTablePduId.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPhasesTablePduId.setStatus(_A)
class _PmPowerMgmtPhasesTableAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3),(_P,4),(_Q,5),(_R,6),(_S,7)))
_PmPowerMgmtPhasesTableAlarm_Type.__name__=_D
_PmPowerMgmtPhasesTableAlarm_Object=MibTableColumn
pmPowerMgmtPhasesTableAlarm=_PmPowerMgmtPhasesTableAlarm_Object((1,3,6,1,4,1,10418,17,2,5,9,1,45),_PmPowerMgmtPhasesTableAlarm_Type())
pmPowerMgmtPhasesTableAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPhasesTableAlarm.setStatus(_A)
_PmPowerMgmtPhasesTableCurrentValue_Type=Integer32
_PmPowerMgmtPhasesTableCurrentValue_Object=MibTableColumn
pmPowerMgmtPhasesTableCurrentValue=_PmPowerMgmtPhasesTableCurrentValue_Object((1,3,6,1,4,1,10418,17,2,5,9,1,50),_PmPowerMgmtPhasesTableCurrentValue_Type())
pmPowerMgmtPhasesTableCurrentValue.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPhasesTableCurrentValue.setStatus(_A)
_PmPowerMgmtPhasesTableCurrentMax_Type=Integer32
_PmPowerMgmtPhasesTableCurrentMax_Object=MibTableColumn
pmPowerMgmtPhasesTableCurrentMax=_PmPowerMgmtPhasesTableCurrentMax_Object((1,3,6,1,4,1,10418,17,2,5,9,1,51),_PmPowerMgmtPhasesTableCurrentMax_Type())
pmPowerMgmtPhasesTableCurrentMax.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPhasesTableCurrentMax.setStatus(_A)
_PmPowerMgmtPhasesTableCurrentMin_Type=Integer32
_PmPowerMgmtPhasesTableCurrentMin_Object=MibTableColumn
pmPowerMgmtPhasesTableCurrentMin=_PmPowerMgmtPhasesTableCurrentMin_Object((1,3,6,1,4,1,10418,17,2,5,9,1,52),_PmPowerMgmtPhasesTableCurrentMin_Type())
pmPowerMgmtPhasesTableCurrentMin.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPhasesTableCurrentMin.setStatus(_A)
_PmPowerMgmtPhasesTableCurrentAvg_Type=Integer32
_PmPowerMgmtPhasesTableCurrentAvg_Object=MibTableColumn
pmPowerMgmtPhasesTableCurrentAvg=_PmPowerMgmtPhasesTableCurrentAvg_Object((1,3,6,1,4,1,10418,17,2,5,9,1,53),_PmPowerMgmtPhasesTableCurrentAvg_Type())
pmPowerMgmtPhasesTableCurrentAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPhasesTableCurrentAvg.setStatus(_A)
class _PmPowerMgmtPhasesTableCurrentReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_G,2)))
_PmPowerMgmtPhasesTableCurrentReset_Type.__name__=_D
_PmPowerMgmtPhasesTableCurrentReset_Object=MibTableColumn
pmPowerMgmtPhasesTableCurrentReset=_PmPowerMgmtPhasesTableCurrentReset_Object((1,3,6,1,4,1,10418,17,2,5,9,1,54),_PmPowerMgmtPhasesTableCurrentReset_Type())
pmPowerMgmtPhasesTableCurrentReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtPhasesTableCurrentReset.setStatus(_A)
_PmPowerMgmtPhasesTablePowerValue_Type=Integer32
_PmPowerMgmtPhasesTablePowerValue_Object=MibTableColumn
pmPowerMgmtPhasesTablePowerValue=_PmPowerMgmtPhasesTablePowerValue_Object((1,3,6,1,4,1,10418,17,2,5,9,1,60),_PmPowerMgmtPhasesTablePowerValue_Type())
pmPowerMgmtPhasesTablePowerValue.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPhasesTablePowerValue.setStatus(_A)
_PmPowerMgmtPhasesTablePowerMax_Type=Integer32
_PmPowerMgmtPhasesTablePowerMax_Object=MibTableColumn
pmPowerMgmtPhasesTablePowerMax=_PmPowerMgmtPhasesTablePowerMax_Object((1,3,6,1,4,1,10418,17,2,5,9,1,61),_PmPowerMgmtPhasesTablePowerMax_Type())
pmPowerMgmtPhasesTablePowerMax.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPhasesTablePowerMax.setStatus(_A)
_PmPowerMgmtPhasesTablePowerMin_Type=Integer32
_PmPowerMgmtPhasesTablePowerMin_Object=MibTableColumn
pmPowerMgmtPhasesTablePowerMin=_PmPowerMgmtPhasesTablePowerMin_Object((1,3,6,1,4,1,10418,17,2,5,9,1,62),_PmPowerMgmtPhasesTablePowerMin_Type())
pmPowerMgmtPhasesTablePowerMin.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPhasesTablePowerMin.setStatus(_A)
_PmPowerMgmtPhasesTablePowerAvg_Type=Integer32
_PmPowerMgmtPhasesTablePowerAvg_Object=MibTableColumn
pmPowerMgmtPhasesTablePowerAvg=_PmPowerMgmtPhasesTablePowerAvg_Object((1,3,6,1,4,1,10418,17,2,5,9,1,63),_PmPowerMgmtPhasesTablePowerAvg_Type())
pmPowerMgmtPhasesTablePowerAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPhasesTablePowerAvg.setStatus(_A)
class _PmPowerMgmtPhasesTablePowerReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_G,2)))
_PmPowerMgmtPhasesTablePowerReset_Type.__name__=_D
_PmPowerMgmtPhasesTablePowerReset_Object=MibTableColumn
pmPowerMgmtPhasesTablePowerReset=_PmPowerMgmtPhasesTablePowerReset_Object((1,3,6,1,4,1,10418,17,2,5,9,1,64),_PmPowerMgmtPhasesTablePowerReset_Type())
pmPowerMgmtPhasesTablePowerReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtPhasesTablePowerReset.setStatus(_A)
class _PmPowerMgmtPhasesTablePowerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),(_K,1),(_L,2)))
_PmPowerMgmtPhasesTablePowerType_Type.__name__=_D
_PmPowerMgmtPhasesTablePowerType_Object=MibTableColumn
pmPowerMgmtPhasesTablePowerType=_PmPowerMgmtPhasesTablePowerType_Object((1,3,6,1,4,1,10418,17,2,5,9,1,65),_PmPowerMgmtPhasesTablePowerType_Type())
pmPowerMgmtPhasesTablePowerType.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPhasesTablePowerType.setStatus(_A)
_PmPowerMgmtPhasesTableVoltageValue_Type=Integer32
_PmPowerMgmtPhasesTableVoltageValue_Object=MibTableColumn
pmPowerMgmtPhasesTableVoltageValue=_PmPowerMgmtPhasesTableVoltageValue_Object((1,3,6,1,4,1,10418,17,2,5,9,1,70),_PmPowerMgmtPhasesTableVoltageValue_Type())
pmPowerMgmtPhasesTableVoltageValue.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPhasesTableVoltageValue.setStatus(_A)
_PmPowerMgmtPhasesTableVoltageMax_Type=Integer32
_PmPowerMgmtPhasesTableVoltageMax_Object=MibTableColumn
pmPowerMgmtPhasesTableVoltageMax=_PmPowerMgmtPhasesTableVoltageMax_Object((1,3,6,1,4,1,10418,17,2,5,9,1,71),_PmPowerMgmtPhasesTableVoltageMax_Type())
pmPowerMgmtPhasesTableVoltageMax.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPhasesTableVoltageMax.setStatus(_A)
_PmPowerMgmtPhasesTableVoltageMin_Type=Integer32
_PmPowerMgmtPhasesTableVoltageMin_Object=MibTableColumn
pmPowerMgmtPhasesTableVoltageMin=_PmPowerMgmtPhasesTableVoltageMin_Object((1,3,6,1,4,1,10418,17,2,5,9,1,72),_PmPowerMgmtPhasesTableVoltageMin_Type())
pmPowerMgmtPhasesTableVoltageMin.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPhasesTableVoltageMin.setStatus(_A)
_PmPowerMgmtPhasesTableVoltageAvg_Type=Integer32
_PmPowerMgmtPhasesTableVoltageAvg_Object=MibTableColumn
pmPowerMgmtPhasesTableVoltageAvg=_PmPowerMgmtPhasesTableVoltageAvg_Object((1,3,6,1,4,1,10418,17,2,5,9,1,73),_PmPowerMgmtPhasesTableVoltageAvg_Type())
pmPowerMgmtPhasesTableVoltageAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPhasesTableVoltageAvg.setStatus(_A)
class _PmPowerMgmtPhasesTableVoltageReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_G,2)))
_PmPowerMgmtPhasesTableVoltageReset_Type.__name__=_D
_PmPowerMgmtPhasesTableVoltageReset_Object=MibTableColumn
pmPowerMgmtPhasesTableVoltageReset=_PmPowerMgmtPhasesTableVoltageReset_Object((1,3,6,1,4,1,10418,17,2,5,9,1,74),_PmPowerMgmtPhasesTableVoltageReset_Type())
pmPowerMgmtPhasesTableVoltageReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtPhasesTableVoltageReset.setStatus(_A)
class _PmPowerMgmtPhasesTableVoltageType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),(_K,1),(_L,2)))
_PmPowerMgmtPhasesTableVoltageType_Type.__name__=_D
_PmPowerMgmtPhasesTableVoltageType_Object=MibTableColumn
pmPowerMgmtPhasesTableVoltageType=_PmPowerMgmtPhasesTableVoltageType_Object((1,3,6,1,4,1,10418,17,2,5,9,1,75),_PmPowerMgmtPhasesTableVoltageType_Type())
pmPowerMgmtPhasesTableVoltageType.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPhasesTableVoltageType.setStatus(_A)
_PmPowerMgmtPhasesTablePowerFactorValue_Type=Integer32
_PmPowerMgmtPhasesTablePowerFactorValue_Object=MibTableColumn
pmPowerMgmtPhasesTablePowerFactorValue=_PmPowerMgmtPhasesTablePowerFactorValue_Object((1,3,6,1,4,1,10418,17,2,5,9,1,80),_PmPowerMgmtPhasesTablePowerFactorValue_Type())
pmPowerMgmtPhasesTablePowerFactorValue.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPhasesTablePowerFactorValue.setStatus(_A)
_PmPowerMgmtPhasesTablePowerFactorMax_Type=Integer32
_PmPowerMgmtPhasesTablePowerFactorMax_Object=MibTableColumn
pmPowerMgmtPhasesTablePowerFactorMax=_PmPowerMgmtPhasesTablePowerFactorMax_Object((1,3,6,1,4,1,10418,17,2,5,9,1,81),_PmPowerMgmtPhasesTablePowerFactorMax_Type())
pmPowerMgmtPhasesTablePowerFactorMax.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPhasesTablePowerFactorMax.setStatus(_A)
_PmPowerMgmtPhasesTablePowerFactorMin_Type=Integer32
_PmPowerMgmtPhasesTablePowerFactorMin_Object=MibTableColumn
pmPowerMgmtPhasesTablePowerFactorMin=_PmPowerMgmtPhasesTablePowerFactorMin_Object((1,3,6,1,4,1,10418,17,2,5,9,1,82),_PmPowerMgmtPhasesTablePowerFactorMin_Type())
pmPowerMgmtPhasesTablePowerFactorMin.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPhasesTablePowerFactorMin.setStatus(_A)
_PmPowerMgmtPhasesTablePowerFactorAvg_Type=Integer32
_PmPowerMgmtPhasesTablePowerFactorAvg_Object=MibTableColumn
pmPowerMgmtPhasesTablePowerFactorAvg=_PmPowerMgmtPhasesTablePowerFactorAvg_Object((1,3,6,1,4,1,10418,17,2,5,9,1,83),_PmPowerMgmtPhasesTablePowerFactorAvg_Type())
pmPowerMgmtPhasesTablePowerFactorAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPhasesTablePowerFactorAvg.setStatus(_A)
class _PmPowerMgmtPhasesTablePowerFactorReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_G,2)))
_PmPowerMgmtPhasesTablePowerFactorReset_Type.__name__=_D
_PmPowerMgmtPhasesTablePowerFactorReset_Object=MibTableColumn
pmPowerMgmtPhasesTablePowerFactorReset=_PmPowerMgmtPhasesTablePowerFactorReset_Object((1,3,6,1,4,1,10418,17,2,5,9,1,84),_PmPowerMgmtPhasesTablePowerFactorReset_Type())
pmPowerMgmtPhasesTablePowerFactorReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtPhasesTablePowerFactorReset.setStatus(_A)
class _PmPowerMgmtPhasesTablePowerFactorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),(_K,1),(_L,2)))
_PmPowerMgmtPhasesTablePowerFactorType_Type.__name__=_D
_PmPowerMgmtPhasesTablePowerFactorType_Object=MibTableColumn
pmPowerMgmtPhasesTablePowerFactorType=_PmPowerMgmtPhasesTablePowerFactorType_Object((1,3,6,1,4,1,10418,17,2,5,9,1,85),_PmPowerMgmtPhasesTablePowerFactorType_Type())
pmPowerMgmtPhasesTablePowerFactorType.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtPhasesTablePowerFactorType.setStatus(_A)
_PmPowerMgmtPhasesTableCurrentHighCritical_Type=Integer32
_PmPowerMgmtPhasesTableCurrentHighCritical_Object=MibTableColumn
pmPowerMgmtPhasesTableCurrentHighCritical=_PmPowerMgmtPhasesTableCurrentHighCritical_Object((1,3,6,1,4,1,10418,17,2,5,9,1,100),_PmPowerMgmtPhasesTableCurrentHighCritical_Type())
pmPowerMgmtPhasesTableCurrentHighCritical.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtPhasesTableCurrentHighCritical.setStatus(_A)
_PmPowerMgmtPhasesTableCurrentHighWarning_Type=Integer32
_PmPowerMgmtPhasesTableCurrentHighWarning_Object=MibTableColumn
pmPowerMgmtPhasesTableCurrentHighWarning=_PmPowerMgmtPhasesTableCurrentHighWarning_Object((1,3,6,1,4,1,10418,17,2,5,9,1,101),_PmPowerMgmtPhasesTableCurrentHighWarning_Type())
pmPowerMgmtPhasesTableCurrentHighWarning.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtPhasesTableCurrentHighWarning.setStatus(_A)
_PmPowerMgmtPhasesTableCurrentLowWarning_Type=Integer32
_PmPowerMgmtPhasesTableCurrentLowWarning_Object=MibTableColumn
pmPowerMgmtPhasesTableCurrentLowWarning=_PmPowerMgmtPhasesTableCurrentLowWarning_Object((1,3,6,1,4,1,10418,17,2,5,9,1,102),_PmPowerMgmtPhasesTableCurrentLowWarning_Type())
pmPowerMgmtPhasesTableCurrentLowWarning.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtPhasesTableCurrentLowWarning.setStatus(_A)
_PmPowerMgmtPhasesTableCurrentLowCritical_Type=Integer32
_PmPowerMgmtPhasesTableCurrentLowCritical_Object=MibTableColumn
pmPowerMgmtPhasesTableCurrentLowCritical=_PmPowerMgmtPhasesTableCurrentLowCritical_Object((1,3,6,1,4,1,10418,17,2,5,9,1,103),_PmPowerMgmtPhasesTableCurrentLowCritical_Type())
pmPowerMgmtPhasesTableCurrentLowCritical.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtPhasesTableCurrentLowCritical.setStatus(_A)
_PmPowerMgmtTotalNumberOfBanks_Type=Integer32
_PmPowerMgmtTotalNumberOfBanks_Object=MibScalar
pmPowerMgmtTotalNumberOfBanks=_PmPowerMgmtTotalNumberOfBanks_Object((1,3,6,1,4,1,10418,17,2,5,10),_PmPowerMgmtTotalNumberOfBanks_Type())
pmPowerMgmtTotalNumberOfBanks.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtTotalNumberOfBanks.setStatus(_A)
_PmPowerMgmtBanksTable_Object=MibTable
pmPowerMgmtBanksTable=_PmPowerMgmtBanksTable_Object((1,3,6,1,4,1,10418,17,2,5,11))
if mibBuilder.loadTexts:pmPowerMgmtBanksTable.setStatus(_A)
_PmPowerMgmtBanksTableEntry_Object=MibTableRow
pmPowerMgmtBanksTableEntry=_PmPowerMgmtBanksTableEntry_Object((1,3,6,1,4,1,10418,17,2,5,11,1))
pmPowerMgmtBanksTableEntry.setIndexNames((0,_H,_i),(0,_H,_j),(0,_H,_k))
if mibBuilder.loadTexts:pmPowerMgmtBanksTableEntry.setStatus(_A)
_PmPowerMgmtBanksTablePortNumber_Type=InterfaceIndex
_PmPowerMgmtBanksTablePortNumber_Object=MibTableColumn
pmPowerMgmtBanksTablePortNumber=_PmPowerMgmtBanksTablePortNumber_Object((1,3,6,1,4,1,10418,17,2,5,11,1,1),_PmPowerMgmtBanksTablePortNumber_Type())
pmPowerMgmtBanksTablePortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtBanksTablePortNumber.setStatus(_A)
_PmPowerMgmtBanksTablePduNumber_Type=InterfaceIndex
_PmPowerMgmtBanksTablePduNumber_Object=MibTableColumn
pmPowerMgmtBanksTablePduNumber=_PmPowerMgmtBanksTablePduNumber_Object((1,3,6,1,4,1,10418,17,2,5,11,1,2),_PmPowerMgmtBanksTablePduNumber_Type())
pmPowerMgmtBanksTablePduNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtBanksTablePduNumber.setStatus(_A)
_PmPowerMgmtBanksTableNumber_Type=InterfaceIndex
_PmPowerMgmtBanksTableNumber_Object=MibTableColumn
pmPowerMgmtBanksTableNumber=_PmPowerMgmtBanksTableNumber_Object((1,3,6,1,4,1,10418,17,2,5,11,1,3),_PmPowerMgmtBanksTableNumber_Type())
pmPowerMgmtBanksTableNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtBanksTableNumber.setStatus(_A)
_PmPowerMgmtBanksTableName_Type=DisplayString
_PmPowerMgmtBanksTableName_Object=MibTableColumn
pmPowerMgmtBanksTableName=_PmPowerMgmtBanksTableName_Object((1,3,6,1,4,1,10418,17,2,5,11,1,4),_PmPowerMgmtBanksTableName_Type())
pmPowerMgmtBanksTableName.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtBanksTableName.setStatus(_A)
_PmPowerMgmtBanksTablePortName_Type=DisplayString
_PmPowerMgmtBanksTablePortName_Object=MibTableColumn
pmPowerMgmtBanksTablePortName=_PmPowerMgmtBanksTablePortName_Object((1,3,6,1,4,1,10418,17,2,5,11,1,5),_PmPowerMgmtBanksTablePortName_Type())
pmPowerMgmtBanksTablePortName.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtBanksTablePortName.setStatus(_A)
_PmPowerMgmtBanksTablePduId_Type=DisplayString
_PmPowerMgmtBanksTablePduId_Object=MibTableColumn
pmPowerMgmtBanksTablePduId=_PmPowerMgmtBanksTablePduId_Object((1,3,6,1,4,1,10418,17,2,5,11,1,6),_PmPowerMgmtBanksTablePduId_Type())
pmPowerMgmtBanksTablePduId.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtBanksTablePduId.setStatus(_A)
class _PmPowerMgmtBanksTableAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3),(_P,4),(_Q,5),(_R,6),(_S,7)))
_PmPowerMgmtBanksTableAlarm_Type.__name__=_D
_PmPowerMgmtBanksTableAlarm_Object=MibTableColumn
pmPowerMgmtBanksTableAlarm=_PmPowerMgmtBanksTableAlarm_Object((1,3,6,1,4,1,10418,17,2,5,11,1,45),_PmPowerMgmtBanksTableAlarm_Type())
pmPowerMgmtBanksTableAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtBanksTableAlarm.setStatus(_A)
_PmPowerMgmtBanksTableCurrentValue_Type=Integer32
_PmPowerMgmtBanksTableCurrentValue_Object=MibTableColumn
pmPowerMgmtBanksTableCurrentValue=_PmPowerMgmtBanksTableCurrentValue_Object((1,3,6,1,4,1,10418,17,2,5,11,1,50),_PmPowerMgmtBanksTableCurrentValue_Type())
pmPowerMgmtBanksTableCurrentValue.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtBanksTableCurrentValue.setStatus(_A)
_PmPowerMgmtBanksTableCurrentMax_Type=Integer32
_PmPowerMgmtBanksTableCurrentMax_Object=MibTableColumn
pmPowerMgmtBanksTableCurrentMax=_PmPowerMgmtBanksTableCurrentMax_Object((1,3,6,1,4,1,10418,17,2,5,11,1,51),_PmPowerMgmtBanksTableCurrentMax_Type())
pmPowerMgmtBanksTableCurrentMax.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtBanksTableCurrentMax.setStatus(_A)
_PmPowerMgmtBanksTableCurrentMin_Type=Integer32
_PmPowerMgmtBanksTableCurrentMin_Object=MibTableColumn
pmPowerMgmtBanksTableCurrentMin=_PmPowerMgmtBanksTableCurrentMin_Object((1,3,6,1,4,1,10418,17,2,5,11,1,52),_PmPowerMgmtBanksTableCurrentMin_Type())
pmPowerMgmtBanksTableCurrentMin.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtBanksTableCurrentMin.setStatus(_A)
_PmPowerMgmtBanksTableCurrentAvg_Type=Integer32
_PmPowerMgmtBanksTableCurrentAvg_Object=MibTableColumn
pmPowerMgmtBanksTableCurrentAvg=_PmPowerMgmtBanksTableCurrentAvg_Object((1,3,6,1,4,1,10418,17,2,5,11,1,53),_PmPowerMgmtBanksTableCurrentAvg_Type())
pmPowerMgmtBanksTableCurrentAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtBanksTableCurrentAvg.setStatus(_A)
class _PmPowerMgmtBanksTableCurrentReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_G,2)))
_PmPowerMgmtBanksTableCurrentReset_Type.__name__=_D
_PmPowerMgmtBanksTableCurrentReset_Object=MibTableColumn
pmPowerMgmtBanksTableCurrentReset=_PmPowerMgmtBanksTableCurrentReset_Object((1,3,6,1,4,1,10418,17,2,5,11,1,54),_PmPowerMgmtBanksTableCurrentReset_Type())
pmPowerMgmtBanksTableCurrentReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtBanksTableCurrentReset.setStatus(_A)
_PmPowerMgmtBanksTablePowerValue_Type=Integer32
_PmPowerMgmtBanksTablePowerValue_Object=MibTableColumn
pmPowerMgmtBanksTablePowerValue=_PmPowerMgmtBanksTablePowerValue_Object((1,3,6,1,4,1,10418,17,2,5,11,1,60),_PmPowerMgmtBanksTablePowerValue_Type())
pmPowerMgmtBanksTablePowerValue.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtBanksTablePowerValue.setStatus(_A)
_PmPowerMgmtBanksTablePowerMax_Type=Integer32
_PmPowerMgmtBanksTablePowerMax_Object=MibTableColumn
pmPowerMgmtBanksTablePowerMax=_PmPowerMgmtBanksTablePowerMax_Object((1,3,6,1,4,1,10418,17,2,5,11,1,61),_PmPowerMgmtBanksTablePowerMax_Type())
pmPowerMgmtBanksTablePowerMax.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtBanksTablePowerMax.setStatus(_A)
_PmPowerMgmtBanksTablePowerMin_Type=Integer32
_PmPowerMgmtBanksTablePowerMin_Object=MibTableColumn
pmPowerMgmtBanksTablePowerMin=_PmPowerMgmtBanksTablePowerMin_Object((1,3,6,1,4,1,10418,17,2,5,11,1,62),_PmPowerMgmtBanksTablePowerMin_Type())
pmPowerMgmtBanksTablePowerMin.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtBanksTablePowerMin.setStatus(_A)
_PmPowerMgmtBanksTablePowerAvg_Type=Integer32
_PmPowerMgmtBanksTablePowerAvg_Object=MibTableColumn
pmPowerMgmtBanksTablePowerAvg=_PmPowerMgmtBanksTablePowerAvg_Object((1,3,6,1,4,1,10418,17,2,5,11,1,63),_PmPowerMgmtBanksTablePowerAvg_Type())
pmPowerMgmtBanksTablePowerAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtBanksTablePowerAvg.setStatus(_A)
class _PmPowerMgmtBanksTablePowerReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_G,2)))
_PmPowerMgmtBanksTablePowerReset_Type.__name__=_D
_PmPowerMgmtBanksTablePowerReset_Object=MibTableColumn
pmPowerMgmtBanksTablePowerReset=_PmPowerMgmtBanksTablePowerReset_Object((1,3,6,1,4,1,10418,17,2,5,11,1,64),_PmPowerMgmtBanksTablePowerReset_Type())
pmPowerMgmtBanksTablePowerReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtBanksTablePowerReset.setStatus(_A)
class _PmPowerMgmtBanksTablePowerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),(_K,1),(_L,2)))
_PmPowerMgmtBanksTablePowerType_Type.__name__=_D
_PmPowerMgmtBanksTablePowerType_Object=MibTableColumn
pmPowerMgmtBanksTablePowerType=_PmPowerMgmtBanksTablePowerType_Object((1,3,6,1,4,1,10418,17,2,5,11,1,65),_PmPowerMgmtBanksTablePowerType_Type())
pmPowerMgmtBanksTablePowerType.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtBanksTablePowerType.setStatus(_A)
_PmPowerMgmtBanksTableVoltageValue_Type=Integer32
_PmPowerMgmtBanksTableVoltageValue_Object=MibTableColumn
pmPowerMgmtBanksTableVoltageValue=_PmPowerMgmtBanksTableVoltageValue_Object((1,3,6,1,4,1,10418,17,2,5,11,1,70),_PmPowerMgmtBanksTableVoltageValue_Type())
pmPowerMgmtBanksTableVoltageValue.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtBanksTableVoltageValue.setStatus(_A)
_PmPowerMgmtBanksTableVoltageMax_Type=Integer32
_PmPowerMgmtBanksTableVoltageMax_Object=MibTableColumn
pmPowerMgmtBanksTableVoltageMax=_PmPowerMgmtBanksTableVoltageMax_Object((1,3,6,1,4,1,10418,17,2,5,11,1,71),_PmPowerMgmtBanksTableVoltageMax_Type())
pmPowerMgmtBanksTableVoltageMax.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtBanksTableVoltageMax.setStatus(_A)
_PmPowerMgmtBanksTableVoltageMin_Type=Integer32
_PmPowerMgmtBanksTableVoltageMin_Object=MibTableColumn
pmPowerMgmtBanksTableVoltageMin=_PmPowerMgmtBanksTableVoltageMin_Object((1,3,6,1,4,1,10418,17,2,5,11,1,72),_PmPowerMgmtBanksTableVoltageMin_Type())
pmPowerMgmtBanksTableVoltageMin.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtBanksTableVoltageMin.setStatus(_A)
_PmPowerMgmtBanksTableVoltageAvg_Type=Integer32
_PmPowerMgmtBanksTableVoltageAvg_Object=MibTableColumn
pmPowerMgmtBanksTableVoltageAvg=_PmPowerMgmtBanksTableVoltageAvg_Object((1,3,6,1,4,1,10418,17,2,5,11,1,73),_PmPowerMgmtBanksTableVoltageAvg_Type())
pmPowerMgmtBanksTableVoltageAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtBanksTableVoltageAvg.setStatus(_A)
class _PmPowerMgmtBanksTableVoltageReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_G,2)))
_PmPowerMgmtBanksTableVoltageReset_Type.__name__=_D
_PmPowerMgmtBanksTableVoltageReset_Object=MibTableColumn
pmPowerMgmtBanksTableVoltageReset=_PmPowerMgmtBanksTableVoltageReset_Object((1,3,6,1,4,1,10418,17,2,5,11,1,74),_PmPowerMgmtBanksTableVoltageReset_Type())
pmPowerMgmtBanksTableVoltageReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtBanksTableVoltageReset.setStatus(_A)
class _PmPowerMgmtBanksTableVoltageType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),(_K,1),(_L,2)))
_PmPowerMgmtBanksTableVoltageType_Type.__name__=_D
_PmPowerMgmtBanksTableVoltageType_Object=MibTableColumn
pmPowerMgmtBanksTableVoltageType=_PmPowerMgmtBanksTableVoltageType_Object((1,3,6,1,4,1,10418,17,2,5,11,1,75),_PmPowerMgmtBanksTableVoltageType_Type())
pmPowerMgmtBanksTableVoltageType.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtBanksTableVoltageType.setStatus(_A)
_PmPowerMgmtBanksTablePowerFactorValue_Type=Integer32
_PmPowerMgmtBanksTablePowerFactorValue_Object=MibTableColumn
pmPowerMgmtBanksTablePowerFactorValue=_PmPowerMgmtBanksTablePowerFactorValue_Object((1,3,6,1,4,1,10418,17,2,5,11,1,80),_PmPowerMgmtBanksTablePowerFactorValue_Type())
pmPowerMgmtBanksTablePowerFactorValue.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtBanksTablePowerFactorValue.setStatus(_A)
_PmPowerMgmtBanksTablePowerFactorMax_Type=Integer32
_PmPowerMgmtBanksTablePowerFactorMax_Object=MibTableColumn
pmPowerMgmtBanksTablePowerFactorMax=_PmPowerMgmtBanksTablePowerFactorMax_Object((1,3,6,1,4,1,10418,17,2,5,11,1,81),_PmPowerMgmtBanksTablePowerFactorMax_Type())
pmPowerMgmtBanksTablePowerFactorMax.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtBanksTablePowerFactorMax.setStatus(_A)
_PmPowerMgmtBanksTablePowerFactorMin_Type=Integer32
_PmPowerMgmtBanksTablePowerFactorMin_Object=MibTableColumn
pmPowerMgmtBanksTablePowerFactorMin=_PmPowerMgmtBanksTablePowerFactorMin_Object((1,3,6,1,4,1,10418,17,2,5,11,1,82),_PmPowerMgmtBanksTablePowerFactorMin_Type())
pmPowerMgmtBanksTablePowerFactorMin.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtBanksTablePowerFactorMin.setStatus(_A)
_PmPowerMgmtBanksTablePowerFactorAvg_Type=Integer32
_PmPowerMgmtBanksTablePowerFactorAvg_Object=MibTableColumn
pmPowerMgmtBanksTablePowerFactorAvg=_PmPowerMgmtBanksTablePowerFactorAvg_Object((1,3,6,1,4,1,10418,17,2,5,11,1,83),_PmPowerMgmtBanksTablePowerFactorAvg_Type())
pmPowerMgmtBanksTablePowerFactorAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtBanksTablePowerFactorAvg.setStatus(_A)
class _PmPowerMgmtBanksTablePowerFactorReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_G,2)))
_PmPowerMgmtBanksTablePowerFactorReset_Type.__name__=_D
_PmPowerMgmtBanksTablePowerFactorReset_Object=MibTableColumn
pmPowerMgmtBanksTablePowerFactorReset=_PmPowerMgmtBanksTablePowerFactorReset_Object((1,3,6,1,4,1,10418,17,2,5,11,1,84),_PmPowerMgmtBanksTablePowerFactorReset_Type())
pmPowerMgmtBanksTablePowerFactorReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtBanksTablePowerFactorReset.setStatus(_A)
class _PmPowerMgmtBanksTablePowerFactorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),(_K,1),(_L,2)))
_PmPowerMgmtBanksTablePowerFactorType_Type.__name__=_D
_PmPowerMgmtBanksTablePowerFactorType_Object=MibTableColumn
pmPowerMgmtBanksTablePowerFactorType=_PmPowerMgmtBanksTablePowerFactorType_Object((1,3,6,1,4,1,10418,17,2,5,11,1,85),_PmPowerMgmtBanksTablePowerFactorType_Type())
pmPowerMgmtBanksTablePowerFactorType.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtBanksTablePowerFactorType.setStatus(_A)
_PmPowerMgmtBanksTableCurrentHighCritical_Type=Integer32
_PmPowerMgmtBanksTableCurrentHighCritical_Object=MibTableColumn
pmPowerMgmtBanksTableCurrentHighCritical=_PmPowerMgmtBanksTableCurrentHighCritical_Object((1,3,6,1,4,1,10418,17,2,5,11,1,100),_PmPowerMgmtBanksTableCurrentHighCritical_Type())
pmPowerMgmtBanksTableCurrentHighCritical.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtBanksTableCurrentHighCritical.setStatus(_A)
_PmPowerMgmtBanksTableCurrentHighWarning_Type=Integer32
_PmPowerMgmtBanksTableCurrentHighWarning_Object=MibTableColumn
pmPowerMgmtBanksTableCurrentHighWarning=_PmPowerMgmtBanksTableCurrentHighWarning_Object((1,3,6,1,4,1,10418,17,2,5,11,1,101),_PmPowerMgmtBanksTableCurrentHighWarning_Type())
pmPowerMgmtBanksTableCurrentHighWarning.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtBanksTableCurrentHighWarning.setStatus(_A)
_PmPowerMgmtBanksTableCurrentLowWarning_Type=Integer32
_PmPowerMgmtBanksTableCurrentLowWarning_Object=MibTableColumn
pmPowerMgmtBanksTableCurrentLowWarning=_PmPowerMgmtBanksTableCurrentLowWarning_Object((1,3,6,1,4,1,10418,17,2,5,11,1,102),_PmPowerMgmtBanksTableCurrentLowWarning_Type())
pmPowerMgmtBanksTableCurrentLowWarning.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtBanksTableCurrentLowWarning.setStatus(_A)
_PmPowerMgmtBanksTableCurrentLowCritical_Type=Integer32
_PmPowerMgmtBanksTableCurrentLowCritical_Object=MibTableColumn
pmPowerMgmtBanksTableCurrentLowCritical=_PmPowerMgmtBanksTableCurrentLowCritical_Object((1,3,6,1,4,1,10418,17,2,5,11,1,103),_PmPowerMgmtBanksTableCurrentLowCritical_Type())
pmPowerMgmtBanksTableCurrentLowCritical.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtBanksTableCurrentLowCritical.setStatus(_A)
_PmPowerMgmtBanksTableEnergyValue_Type=Integer32
_PmPowerMgmtBanksTableEnergyValue_Object=MibTableColumn
pmPowerMgmtBanksTableEnergyValue=_PmPowerMgmtBanksTableEnergyValue_Object((1,3,6,1,4,1,10418,17,2,5,11,1,105),_PmPowerMgmtBanksTableEnergyValue_Type())
pmPowerMgmtBanksTableEnergyValue.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtBanksTableEnergyValue.setStatus(_A)
_PmPowerMgmtBanksTableEnergyStartTime_Type=DisplayString
_PmPowerMgmtBanksTableEnergyStartTime_Object=MibTableColumn
pmPowerMgmtBanksTableEnergyStartTime=_PmPowerMgmtBanksTableEnergyStartTime_Object((1,3,6,1,4,1,10418,17,2,5,11,1,106),_PmPowerMgmtBanksTableEnergyStartTime_Type())
pmPowerMgmtBanksTableEnergyStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtBanksTableEnergyStartTime.setStatus(_A)
class _PmPowerMgmtBanksTableEnergyReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_G,2)))
_PmPowerMgmtBanksTableEnergyReset_Type.__name__=_D
_PmPowerMgmtBanksTableEnergyReset_Object=MibTableColumn
pmPowerMgmtBanksTableEnergyReset=_PmPowerMgmtBanksTableEnergyReset_Object((1,3,6,1,4,1,10418,17,2,5,11,1,107),_PmPowerMgmtBanksTableEnergyReset_Type())
pmPowerMgmtBanksTableEnergyReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtBanksTableEnergyReset.setStatus(_A)
_PmPowerMgmtTotalNumberOfSensors_Type=Integer32
_PmPowerMgmtTotalNumberOfSensors_Object=MibScalar
pmPowerMgmtTotalNumberOfSensors=_PmPowerMgmtTotalNumberOfSensors_Object((1,3,6,1,4,1,10418,17,2,5,12),_PmPowerMgmtTotalNumberOfSensors_Type())
pmPowerMgmtTotalNumberOfSensors.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtTotalNumberOfSensors.setStatus(_A)
_PmPowerMgmtSensorsTable_Object=MibTable
pmPowerMgmtSensorsTable=_PmPowerMgmtSensorsTable_Object((1,3,6,1,4,1,10418,17,2,5,13))
if mibBuilder.loadTexts:pmPowerMgmtSensorsTable.setStatus(_A)
_PmPowerMgmtSensorsTableEntry_Object=MibTableRow
pmPowerMgmtSensorsTableEntry=_PmPowerMgmtSensorsTableEntry_Object((1,3,6,1,4,1,10418,17,2,5,13,1))
pmPowerMgmtSensorsTableEntry.setIndexNames((0,_H,_l),(0,_H,_m),(0,_H,_n))
if mibBuilder.loadTexts:pmPowerMgmtSensorsTableEntry.setStatus(_A)
_PmPowerMgmtSensorsTablePortNumber_Type=InterfaceIndex
_PmPowerMgmtSensorsTablePortNumber_Object=MibTableColumn
pmPowerMgmtSensorsTablePortNumber=_PmPowerMgmtSensorsTablePortNumber_Object((1,3,6,1,4,1,10418,17,2,5,13,1,1),_PmPowerMgmtSensorsTablePortNumber_Type())
pmPowerMgmtSensorsTablePortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtSensorsTablePortNumber.setStatus(_A)
_PmPowerMgmtSensorsTablePduNumber_Type=InterfaceIndex
_PmPowerMgmtSensorsTablePduNumber_Object=MibTableColumn
pmPowerMgmtSensorsTablePduNumber=_PmPowerMgmtSensorsTablePduNumber_Object((1,3,6,1,4,1,10418,17,2,5,13,1,2),_PmPowerMgmtSensorsTablePduNumber_Type())
pmPowerMgmtSensorsTablePduNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtSensorsTablePduNumber.setStatus(_A)
_PmPowerMgmtSensorsTableNumber_Type=InterfaceIndex
_PmPowerMgmtSensorsTableNumber_Object=MibTableColumn
pmPowerMgmtSensorsTableNumber=_PmPowerMgmtSensorsTableNumber_Object((1,3,6,1,4,1,10418,17,2,5,13,1,3),_PmPowerMgmtSensorsTableNumber_Type())
pmPowerMgmtSensorsTableNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtSensorsTableNumber.setStatus(_A)
_PmPowerMgmtSensorsTableName_Type=DisplayString
_PmPowerMgmtSensorsTableName_Object=MibTableColumn
pmPowerMgmtSensorsTableName=_PmPowerMgmtSensorsTableName_Object((1,3,6,1,4,1,10418,17,2,5,13,1,4),_PmPowerMgmtSensorsTableName_Type())
pmPowerMgmtSensorsTableName.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtSensorsTableName.setStatus(_A)
_PmPowerMgmtSensorsTablePortName_Type=DisplayString
_PmPowerMgmtSensorsTablePortName_Object=MibTableColumn
pmPowerMgmtSensorsTablePortName=_PmPowerMgmtSensorsTablePortName_Object((1,3,6,1,4,1,10418,17,2,5,13,1,5),_PmPowerMgmtSensorsTablePortName_Type())
pmPowerMgmtSensorsTablePortName.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtSensorsTablePortName.setStatus(_A)
_PmPowerMgmtSensorsTablePduId_Type=DisplayString
_PmPowerMgmtSensorsTablePduId_Object=MibTableColumn
pmPowerMgmtSensorsTablePduId=_PmPowerMgmtSensorsTablePduId_Object((1,3,6,1,4,1,10418,17,2,5,13,1,6),_PmPowerMgmtSensorsTablePduId_Type())
pmPowerMgmtSensorsTablePduId.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtSensorsTablePduId.setStatus(_A)
class _PmPowerMgmtSensorsTableType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('temp-internal',1),('temperature',2),('humidity',3),('air-flow',4),('smoke',5),('dry-concact',6),('water-level',7),('motion',8),('unplugged',9),('unknown',10)))
_PmPowerMgmtSensorsTableType_Type.__name__=_D
_PmPowerMgmtSensorsTableType_Object=MibTableColumn
pmPowerMgmtSensorsTableType=_PmPowerMgmtSensorsTableType_Object((1,3,6,1,4,1,10418,17,2,5,13,1,7),_PmPowerMgmtSensorsTableType_Type())
pmPowerMgmtSensorsTableType.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtSensorsTableType.setStatus(_A)
class _PmPowerMgmtSensorsTableStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_M,1),('triggered',2),('not-applicable',3),('opened',4),('closed',5)))
_PmPowerMgmtSensorsTableStatus_Type.__name__=_D
_PmPowerMgmtSensorsTableStatus_Object=MibTableColumn
pmPowerMgmtSensorsTableStatus=_PmPowerMgmtSensorsTableStatus_Object((1,3,6,1,4,1,10418,17,2,5,13,1,8),_PmPowerMgmtSensorsTableStatus_Type())
pmPowerMgmtSensorsTableStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtSensorsTableStatus.setStatus(_A)
_PmPowerMgmtSensorsTableValue_Type=DisplayString
_PmPowerMgmtSensorsTableValue_Object=MibTableColumn
pmPowerMgmtSensorsTableValue=_PmPowerMgmtSensorsTableValue_Object((1,3,6,1,4,1,10418,17,2,5,13,1,20),_PmPowerMgmtSensorsTableValue_Type())
pmPowerMgmtSensorsTableValue.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtSensorsTableValue.setStatus(_A)
_PmPowerMgmtSensorsTableValueMax_Type=DisplayString
_PmPowerMgmtSensorsTableValueMax_Object=MibTableColumn
pmPowerMgmtSensorsTableValueMax=_PmPowerMgmtSensorsTableValueMax_Object((1,3,6,1,4,1,10418,17,2,5,13,1,21),_PmPowerMgmtSensorsTableValueMax_Type())
pmPowerMgmtSensorsTableValueMax.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtSensorsTableValueMax.setStatus(_A)
_PmPowerMgmtSensorsTableValueMin_Type=DisplayString
_PmPowerMgmtSensorsTableValueMin_Object=MibTableColumn
pmPowerMgmtSensorsTableValueMin=_PmPowerMgmtSensorsTableValueMin_Object((1,3,6,1,4,1,10418,17,2,5,13,1,22),_PmPowerMgmtSensorsTableValueMin_Type())
pmPowerMgmtSensorsTableValueMin.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtSensorsTableValueMin.setStatus(_A)
_PmPowerMgmtSensorsTableValueAvg_Type=DisplayString
_PmPowerMgmtSensorsTableValueAvg_Object=MibTableColumn
pmPowerMgmtSensorsTableValueAvg=_PmPowerMgmtSensorsTableValueAvg_Object((1,3,6,1,4,1,10418,17,2,5,13,1,23),_PmPowerMgmtSensorsTableValueAvg_Type())
pmPowerMgmtSensorsTableValueAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtSensorsTableValueAvg.setStatus(_A)
_PmPowerMgmtSensorsTableValueInt_Type=Integer32
_PmPowerMgmtSensorsTableValueInt_Object=MibTableColumn
pmPowerMgmtSensorsTableValueInt=_PmPowerMgmtSensorsTableValueInt_Object((1,3,6,1,4,1,10418,17,2,5,13,1,25),_PmPowerMgmtSensorsTableValueInt_Type())
pmPowerMgmtSensorsTableValueInt.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtSensorsTableValueInt.setStatus(_A)
_PmPowerMgmtSensorsTableValueMaxInt_Type=Integer32
_PmPowerMgmtSensorsTableValueMaxInt_Object=MibTableColumn
pmPowerMgmtSensorsTableValueMaxInt=_PmPowerMgmtSensorsTableValueMaxInt_Object((1,3,6,1,4,1,10418,17,2,5,13,1,26),_PmPowerMgmtSensorsTableValueMaxInt_Type())
pmPowerMgmtSensorsTableValueMaxInt.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtSensorsTableValueMaxInt.setStatus(_A)
_PmPowerMgmtSensorsTableValueMinInt_Type=Integer32
_PmPowerMgmtSensorsTableValueMinInt_Object=MibTableColumn
pmPowerMgmtSensorsTableValueMinInt=_PmPowerMgmtSensorsTableValueMinInt_Object((1,3,6,1,4,1,10418,17,2,5,13,1,27),_PmPowerMgmtSensorsTableValueMinInt_Type())
pmPowerMgmtSensorsTableValueMinInt.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtSensorsTableValueMinInt.setStatus(_A)
_PmPowerMgmtSensorsTableValueAvgInt_Type=Integer32
_PmPowerMgmtSensorsTableValueAvgInt_Object=MibTableColumn
pmPowerMgmtSensorsTableValueAvgInt=_PmPowerMgmtSensorsTableValueAvgInt_Object((1,3,6,1,4,1,10418,17,2,5,13,1,28),_PmPowerMgmtSensorsTableValueAvgInt_Type())
pmPowerMgmtSensorsTableValueAvgInt.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtSensorsTableValueAvgInt.setStatus(_A)
class _PmPowerMgmtSensorsTableValueReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_G,2)))
_PmPowerMgmtSensorsTableValueReset_Type.__name__=_D
_PmPowerMgmtSensorsTableValueReset_Object=MibTableColumn
pmPowerMgmtSensorsTableValueReset=_PmPowerMgmtSensorsTableValueReset_Object((1,3,6,1,4,1,10418,17,2,5,13,1,30),_PmPowerMgmtSensorsTableValueReset_Type())
pmPowerMgmtSensorsTableValueReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtSensorsTableValueReset.setStatus(_A)
_PmPowerMgmtSensorsTableHighCritical_Type=Integer32
_PmPowerMgmtSensorsTableHighCritical_Object=MibTableColumn
pmPowerMgmtSensorsTableHighCritical=_PmPowerMgmtSensorsTableHighCritical_Object((1,3,6,1,4,1,10418,17,2,5,13,1,40),_PmPowerMgmtSensorsTableHighCritical_Type())
pmPowerMgmtSensorsTableHighCritical.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtSensorsTableHighCritical.setStatus(_A)
_PmPowerMgmtSensorsTableHighWarning_Type=Integer32
_PmPowerMgmtSensorsTableHighWarning_Object=MibTableColumn
pmPowerMgmtSensorsTableHighWarning=_PmPowerMgmtSensorsTableHighWarning_Object((1,3,6,1,4,1,10418,17,2,5,13,1,41),_PmPowerMgmtSensorsTableHighWarning_Type())
pmPowerMgmtSensorsTableHighWarning.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtSensorsTableHighWarning.setStatus(_A)
_PmPowerMgmtSensorsTableLowWarning_Type=Integer32
_PmPowerMgmtSensorsTableLowWarning_Object=MibTableColumn
pmPowerMgmtSensorsTableLowWarning=_PmPowerMgmtSensorsTableLowWarning_Object((1,3,6,1,4,1,10418,17,2,5,13,1,42),_PmPowerMgmtSensorsTableLowWarning_Type())
pmPowerMgmtSensorsTableLowWarning.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtSensorsTableLowWarning.setStatus(_A)
_PmPowerMgmtSensorsTableLowCritical_Type=Integer32
_PmPowerMgmtSensorsTableLowCritical_Object=MibTableColumn
pmPowerMgmtSensorsTableLowCritical=_PmPowerMgmtSensorsTableLowCritical_Object((1,3,6,1,4,1,10418,17,2,5,13,1,43),_PmPowerMgmtSensorsTableLowCritical_Type())
pmPowerMgmtSensorsTableLowCritical.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtSensorsTableLowCritical.setStatus(_A)
class _PmPowerMgmtSensorsTableUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('undefined',1),('fahrenheit',2),('celsius',3),('percent',4),('afu',5)))
_PmPowerMgmtSensorsTableUnit_Type.__name__=_D
_PmPowerMgmtSensorsTableUnit_Object=MibTableColumn
pmPowerMgmtSensorsTableUnit=_PmPowerMgmtSensorsTableUnit_Object((1,3,6,1,4,1,10418,17,2,5,13,1,45),_PmPowerMgmtSensorsTableUnit_Type())
pmPowerMgmtSensorsTableUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:pmPowerMgmtSensorsTableUnit.setStatus(_A)
_PmPowerMgmtSensorsTableHighCriticalC_Type=Integer32
_PmPowerMgmtSensorsTableHighCriticalC_Object=MibTableColumn
pmPowerMgmtSensorsTableHighCriticalC=_PmPowerMgmtSensorsTableHighCriticalC_Object((1,3,6,1,4,1,10418,17,2,5,13,1,50),_PmPowerMgmtSensorsTableHighCriticalC_Type())
pmPowerMgmtSensorsTableHighCriticalC.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtSensorsTableHighCriticalC.setStatus(_A)
_PmPowerMgmtSensorsTableHighWarningC_Type=Integer32
_PmPowerMgmtSensorsTableHighWarningC_Object=MibTableColumn
pmPowerMgmtSensorsTableHighWarningC=_PmPowerMgmtSensorsTableHighWarningC_Object((1,3,6,1,4,1,10418,17,2,5,13,1,51),_PmPowerMgmtSensorsTableHighWarningC_Type())
pmPowerMgmtSensorsTableHighWarningC.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtSensorsTableHighWarningC.setStatus(_A)
_PmPowerMgmtSensorsTableLowWarningC_Type=Integer32
_PmPowerMgmtSensorsTableLowWarningC_Object=MibTableColumn
pmPowerMgmtSensorsTableLowWarningC=_PmPowerMgmtSensorsTableLowWarningC_Object((1,3,6,1,4,1,10418,17,2,5,13,1,52),_PmPowerMgmtSensorsTableLowWarningC_Type())
pmPowerMgmtSensorsTableLowWarningC.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtSensorsTableLowWarningC.setStatus(_A)
_PmPowerMgmtSensorsTableLowCriticalC_Type=Integer32
_PmPowerMgmtSensorsTableLowCriticalC_Object=MibTableColumn
pmPowerMgmtSensorsTableLowCriticalC=_PmPowerMgmtSensorsTableLowCriticalC_Object((1,3,6,1,4,1,10418,17,2,5,13,1,53),_PmPowerMgmtSensorsTableLowCriticalC_Type())
pmPowerMgmtSensorsTableLowCriticalC.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtSensorsTableLowCriticalC.setStatus(_A)
_PmPowerMgmtSensorsTableHighCriticalF_Type=Integer32
_PmPowerMgmtSensorsTableHighCriticalF_Object=MibTableColumn
pmPowerMgmtSensorsTableHighCriticalF=_PmPowerMgmtSensorsTableHighCriticalF_Object((1,3,6,1,4,1,10418,17,2,5,13,1,60),_PmPowerMgmtSensorsTableHighCriticalF_Type())
pmPowerMgmtSensorsTableHighCriticalF.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtSensorsTableHighCriticalF.setStatus(_A)
_PmPowerMgmtSensorsTableHighWarningF_Type=Integer32
_PmPowerMgmtSensorsTableHighWarningF_Object=MibTableColumn
pmPowerMgmtSensorsTableHighWarningF=_PmPowerMgmtSensorsTableHighWarningF_Object((1,3,6,1,4,1,10418,17,2,5,13,1,61),_PmPowerMgmtSensorsTableHighWarningF_Type())
pmPowerMgmtSensorsTableHighWarningF.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtSensorsTableHighWarningF.setStatus(_A)
_PmPowerMgmtSensorsTableLowWarningF_Type=Integer32
_PmPowerMgmtSensorsTableLowWarningF_Object=MibTableColumn
pmPowerMgmtSensorsTableLowWarningF=_PmPowerMgmtSensorsTableLowWarningF_Object((1,3,6,1,4,1,10418,17,2,5,13,1,62),_PmPowerMgmtSensorsTableLowWarningF_Type())
pmPowerMgmtSensorsTableLowWarningF.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtSensorsTableLowWarningF.setStatus(_A)
_PmPowerMgmtSensorsTableLowCriticalF_Type=Integer32
_PmPowerMgmtSensorsTableLowCriticalF_Object=MibTableColumn
pmPowerMgmtSensorsTableLowCriticalF=_PmPowerMgmtSensorsTableLowCriticalF_Object((1,3,6,1,4,1,10418,17,2,5,13,1,63),_PmPowerMgmtSensorsTableLowCriticalF_Type())
pmPowerMgmtSensorsTableLowCriticalF.setMaxAccess(_B)
if mibBuilder.loadTexts:pmPowerMgmtSensorsTableLowCriticalF.setStatus(_A)
_PmTrapObject_ObjectIdentity=ObjectIdentity
pmTrapObject=_PmTrapObject_ObjectIdentity((1,3,6,1,4,1,10418,17,2,6))
mibBuilder.exportSymbols(_H,**{'pm':pm,'pmProducts':pmProducts,'pm1024':pm1024,'pm2003':pm2003,'pm2006':pm2006,'pm2024':pm2024,'pm3003':pm3003,'pm3006':pm3006,'pm3024':pm3024,'pm1010':pm1010,'pm2010':pm2010,'pm3010':pm3010,'pm1020':pm1020,'pm2020':pm2020,'pm3020':pm3020,'pmManagement':pmManagement,'pmAppliance':pmAppliance,'pmHostName':pmHostName,'pmProductModel':pmProductModel,'pmPartNumber':pmPartNumber,'pmSerialNumber':pmSerialNumber,'pmEIDNumber':pmEIDNumber,'pmBootcodeVersion':pmBootcodeVersion,'pmFirmwareVersion':pmFirmwareVersion,'pmReboot':pmReboot,'pmSessions':pmSessions,'pmActiveSessionsNumberOfSession':pmActiveSessionsNumberOfSession,'pmActiveSessionsTable':pmActiveSessionsTable,'pmActiveSessionsTableEntry':pmActiveSessionsTableEntry,_X:pmActiveSessionsTableIndex,'pmActiveSessionsTableUser':pmActiveSessionsTableUser,'pmActiveSessionsTableGroup':pmActiveSessionsTableGroup,'pmActiveSessionsTableType':pmActiveSessionsTableType,'pmActiveSessionsTableConnection':pmActiveSessionsTableConnection,'pmActiveSessionsTableSessionTime':pmActiveSessionsTableSessionTime,'pmActiveSessionsTableFrom':pmActiveSessionsTableFrom,'pmActiveSessionsTableKill':pmActiveSessionsTableKill,'pmPowerMgmt':pmPowerMgmt,'pmPowerMgmtNumSerialPorts':pmPowerMgmtNumSerialPorts,'pmPowerMgmtSerialTable':pmPowerMgmtSerialTable,'pmPowerMgmtSerialTableEntry':pmPowerMgmtSerialTableEntry,_Y:pmPowerMgmtSerialTableIndex,'pmPowerMgmtSerialTablePortNumber':pmPowerMgmtSerialTablePortNumber,'pmPowerMgmtSerialTableDeviceName':pmPowerMgmtSerialTableDeviceName,'pmPowerMgmtSerialTableNumberPDUs':pmPowerMgmtSerialTableNumberPDUs,'pmPowerMgmtSerialTableBuzzer':pmPowerMgmtSerialTableBuzzer,'pmPowerMgmtSerialTableSyslog':pmPowerMgmtSerialTableSyslog,'pmPowerMgmtSerialTableOverCurrent':pmPowerMgmtSerialTableOverCurrent,'pmPowerMgmtSerialTableCycleInterval':pmPowerMgmtSerialTableCycleInterval,'pmPowerMgmtSerialTablePollRate':pmPowerMgmtSerialTablePollRate,'pmPowerMgmtSerialTablePassWord':pmPowerMgmtSerialTablePassWord,'pmPowerMgmtSerialTableSave':pmPowerMgmtSerialTableSave,'pmPowerMgmtSerialTableRestore':pmPowerMgmtSerialTableRestore,'pmPowerMgmtPDUTable':pmPowerMgmtPDUTable,'pmPowerMgmtPDUTableEntry':pmPowerMgmtPDUTableEntry,_Z:pmPowerMgmtPDUTablePortNumber,_a:pmPowerMgmtPDUTablePduIndex,'pmPowerMgmtPDUTablePduId':pmPowerMgmtPDUTablePduId,'pmPowerMgmtPDUTablePortName':pmPowerMgmtPDUTablePortName,'pmPowerMgmtPDUTableModel':pmPowerMgmtPDUTableModel,'pmPowerMgmtPDUTableVendor':pmPowerMgmtPDUTableVendor,'pmPowerMgmtPDUTableFirmwareVersion':pmPowerMgmtPDUTableFirmwareVersion,'pmPowerMgmtPDUTableNumberOfOutlets':pmPowerMgmtPDUTableNumberOfOutlets,'pmPowerMgmtPDUTableCurrentNOS':pmPowerMgmtPDUTableCurrentNOS,'pmPowerMgmtPDUTableCurrent1Value':pmPowerMgmtPDUTableCurrent1Value,'pmPowerMgmtPDUTableCurrent1Max':pmPowerMgmtPDUTableCurrent1Max,'pmPowerMgmtPDUTableCurrent2Value':pmPowerMgmtPDUTableCurrent2Value,'pmPowerMgmtPDUTableCurrent2Max':pmPowerMgmtPDUTableCurrent2Max,'pmPowerMgmtPDUTableCurrent3Value':pmPowerMgmtPDUTableCurrent3Value,'pmPowerMgmtPDUTableCurrent3Max':pmPowerMgmtPDUTableCurrent3Max,'pmPowerMgmtPDUTableTemperatureNOS':pmPowerMgmtPDUTableTemperatureNOS,'pmPowerMgmtPDUTableTemperature1Value':pmPowerMgmtPDUTableTemperature1Value,'pmPowerMgmtPDUTableTemperature1Max':pmPowerMgmtPDUTableTemperature1Max,'pmPowerMgmtPDUTableTemperature2Value':pmPowerMgmtPDUTableTemperature2Value,'pmPowerMgmtPDUTableTemperature2Max':pmPowerMgmtPDUTableTemperature2Max,'pmPowerMgmtPDUTableTemperature3Value':pmPowerMgmtPDUTableTemperature3Value,'pmPowerMgmtPDUTableTemperature3Max':pmPowerMgmtPDUTableTemperature3Max,'pmPowerMgmtPDUTableHumidityNOS':pmPowerMgmtPDUTableHumidityNOS,'pmPowerMgmtPDUTableHumidity1Value':pmPowerMgmtPDUTableHumidity1Value,'pmPowerMgmtPDUTableHumidity1Max':pmPowerMgmtPDUTableHumidity1Max,'pmPowerMgmtPDUTableHumidity2Value':pmPowerMgmtPDUTableHumidity2Value,'pmPowerMgmtPDUTableHumidity2Max':pmPowerMgmtPDUTableHumidity2Max,'pmPowerMgmtPDUTableHumidity3Value':pmPowerMgmtPDUTableHumidity3Value,'pmPowerMgmtPDUTableHumidity3Max':pmPowerMgmtPDUTableHumidity3Max,'pmPowerMgmtPDUTableVoltageNOS':pmPowerMgmtPDUTableVoltageNOS,'pmPowerMgmtPDUTableVoltage1Value':pmPowerMgmtPDUTableVoltage1Value,'pmPowerMgmtPDUTableVoltage1Max':pmPowerMgmtPDUTableVoltage1Max,'pmPowerMgmtPDUTableVoltage2Value':pmPowerMgmtPDUTableVoltage2Value,'pmPowerMgmtPDUTableVoltage2Max':pmPowerMgmtPDUTableVoltage2Max,'pmPowerMgmtPDUTableVoltage3Value':pmPowerMgmtPDUTableVoltage3Value,'pmPowerMgmtPDUTableVoltage3Max':pmPowerMgmtPDUTableVoltage3Max,'pmPowerMgmtPDUTableNumberOfPhases':pmPowerMgmtPDUTableNumberOfPhases,'pmPowerMgmtPDUTableNumberOfBanks':pmPowerMgmtPDUTableNumberOfBanks,'pmPowerMgmtPDUTableNumberOfSensors':pmPowerMgmtPDUTableNumberOfSensors,'pmPowerMgmtPDUTableFactoryDefault':pmPowerMgmtPDUTableFactoryDefault,'pmPowerMgmtPDUTableColdStartDelay':pmPowerMgmtPDUTableColdStartDelay,'pmPowerMgmtPDUTableReboot':pmPowerMgmtPDUTableReboot,'pmPowerMgmtPDUTableMaxCurrent':pmPowerMgmtPDUTableMaxCurrent,'pmPowerMgmtPDUTableAlarm':pmPowerMgmtPDUTableAlarm,'pmPowerMgmtPDUTableCurrentValue':pmPowerMgmtPDUTableCurrentValue,'pmPowerMgmtPDUTableCurrentMax':pmPowerMgmtPDUTableCurrentMax,'pmPowerMgmtPDUTableCurrentMin':pmPowerMgmtPDUTableCurrentMin,'pmPowerMgmtPDUTableCurrentAvg':pmPowerMgmtPDUTableCurrentAvg,'pmPowerMgmtPDUTableCurrentReset':pmPowerMgmtPDUTableCurrentReset,'pmPowerMgmtPDUTablePowerValue':pmPowerMgmtPDUTablePowerValue,'pmPowerMgmtPDUTablePowerMax':pmPowerMgmtPDUTablePowerMax,'pmPowerMgmtPDUTablePowerMin':pmPowerMgmtPDUTablePowerMin,'pmPowerMgmtPDUTablePowerAvg':pmPowerMgmtPDUTablePowerAvg,'pmPowerMgmtPDUTablePowerReset':pmPowerMgmtPDUTablePowerReset,'pmPowerMgmtPDUTablePowerType':pmPowerMgmtPDUTablePowerType,'pmPowerMgmtPDUTableVoltageValue':pmPowerMgmtPDUTableVoltageValue,'pmPowerMgmtPDUTableVoltageMax':pmPowerMgmtPDUTableVoltageMax,'pmPowerMgmtPDUTableVoltageMin':pmPowerMgmtPDUTableVoltageMin,'pmPowerMgmtPDUTableVoltageAvg':pmPowerMgmtPDUTableVoltageAvg,'pmPowerMgmtPDUTableVoltageReset':pmPowerMgmtPDUTableVoltageReset,'pmPowerMgmtPDUTableVoltageType':pmPowerMgmtPDUTableVoltageType,'pmPowerMgmtPDUTablePowerFactorValue':pmPowerMgmtPDUTablePowerFactorValue,'pmPowerMgmtPDUTablePowerFactorMax':pmPowerMgmtPDUTablePowerFactorMax,'pmPowerMgmtPDUTablePowerFactorMin':pmPowerMgmtPDUTablePowerFactorMin,'pmPowerMgmtPDUTablePowerFactorAvg':pmPowerMgmtPDUTablePowerFactorAvg,'pmPowerMgmtPDUTablePowerFactorReset':pmPowerMgmtPDUTablePowerFactorReset,'pmPowerMgmtPDUTablePowerFactorType':pmPowerMgmtPDUTablePowerFactorType,'pmPowerMgmtPDUTablePowerControl':pmPowerMgmtPDUTablePowerControl,'pmPowerMgmtPDUTableResetOCP':pmPowerMgmtPDUTableResetOCP,'pmPowerMgmtPDUTableCurrentHighCritical':pmPowerMgmtPDUTableCurrentHighCritical,'pmPowerMgmtPDUTableCurrentHighWarning':pmPowerMgmtPDUTableCurrentHighWarning,'pmPowerMgmtPDUTableCurrentLowWarning':pmPowerMgmtPDUTableCurrentLowWarning,'pmPowerMgmtPDUTableCurrentLowCritical':pmPowerMgmtPDUTableCurrentLowCritical,'pmPowerMgmtPDUTableEnergyValue':pmPowerMgmtPDUTableEnergyValue,'pmPowerMgmtPDUTableEnergyStartTime':pmPowerMgmtPDUTableEnergyStartTime,'pmPowerMgmtPDUTableEnergyReset':pmPowerMgmtPDUTableEnergyReset,'pmPowerMgmtTotalNumberOfOutlets':pmPowerMgmtTotalNumberOfOutlets,'pmPowerMgmtOutletsTable':pmPowerMgmtOutletsTable,'pmPowerMgmtOutletsTableEntry':pmPowerMgmtOutletsTableEntry,_b:pmPowerMgmtOutletsTablePortNumber,_c:pmPowerMgmtOutletsTablePduNumber,_d:pmPowerMgmtOutletsTableNumber,'pmPowerMgmtOutletsTableName':pmPowerMgmtOutletsTableName,'pmPowerMgmtOutletsTableStatus':pmPowerMgmtOutletsTableStatus,'pmPowerMgmtOutletsTablePowerControl':pmPowerMgmtOutletsTablePowerControl,'pmPowerMgmtOutletsTablePortName':pmPowerMgmtOutletsTablePortName,'pmPowerMgmtOutletsTablePduId':pmPowerMgmtOutletsTablePduId,'pmPowerMgmtOutletsTablePostOnDelay':pmPowerMgmtOutletsTablePostOnDelay,'pmPowerMgmtOutletsTablePostOffDelay':pmPowerMgmtOutletsTablePostOffDelay,'pmPowerMgmtOutletsTableAlarm':pmPowerMgmtOutletsTableAlarm,'pmPowerMgmtOutletsTableCurrentValue':pmPowerMgmtOutletsTableCurrentValue,'pmPowerMgmtOutletsTableCurrentMax':pmPowerMgmtOutletsTableCurrentMax,'pmPowerMgmtOutletsTableCurrentMin':pmPowerMgmtOutletsTableCurrentMin,'pmPowerMgmtOutletsTableCurrentAvg':pmPowerMgmtOutletsTableCurrentAvg,'pmPowerMgmtOutletsTableCurrentReset':pmPowerMgmtOutletsTableCurrentReset,'pmPowerMgmtOutletsTablePowerValue':pmPowerMgmtOutletsTablePowerValue,'pmPowerMgmtOutletsTablePowerMax':pmPowerMgmtOutletsTablePowerMax,'pmPowerMgmtOutletsTablePowerMin':pmPowerMgmtOutletsTablePowerMin,'pmPowerMgmtOutletsTablePowerAvg':pmPowerMgmtOutletsTablePowerAvg,'pmPowerMgmtOutletsTablePowerReset':pmPowerMgmtOutletsTablePowerReset,'pmPowerMgmtOutletsTablePowerType':pmPowerMgmtOutletsTablePowerType,'pmPowerMgmtOutletsTableVoltageValue':pmPowerMgmtOutletsTableVoltageValue,'pmPowerMgmtOutletsTableVoltageMax':pmPowerMgmtOutletsTableVoltageMax,'pmPowerMgmtOutletsTableVoltageMin':pmPowerMgmtOutletsTableVoltageMin,'pmPowerMgmtOutletsTableVoltageAvg':pmPowerMgmtOutletsTableVoltageAvg,'pmPowerMgmtOutletsTableVoltageReset':pmPowerMgmtOutletsTableVoltageReset,'pmPowerMgmtOutletsTableVoltageType':pmPowerMgmtOutletsTableVoltageType,'pmPowerMgmtOutletsTablePowerFactorValue':pmPowerMgmtOutletsTablePowerFactorValue,'pmPowerMgmtOutletsTablePowerFactorMax':pmPowerMgmtOutletsTablePowerFactorMax,'pmPowerMgmtOutletsTablePowerFactorMin':pmPowerMgmtOutletsTablePowerFactorMin,'pmPowerMgmtOutletsTablePowerFactorAvg':pmPowerMgmtOutletsTablePowerFactorAvg,'pmPowerMgmtOutletsTablePowerFactorReset':pmPowerMgmtOutletsTablePowerFactorReset,'pmPowerMgmtOutletsTablePowerFactorType':pmPowerMgmtOutletsTablePowerFactorType,'pmPowerMgmtOutletsTableCurrentHighCritical':pmPowerMgmtOutletsTableCurrentHighCritical,'pmPowerMgmtOutletsTableCurrentHighWarning':pmPowerMgmtOutletsTableCurrentHighWarning,'pmPowerMgmtOutletsTableCurrentLowWarning':pmPowerMgmtOutletsTableCurrentLowWarning,'pmPowerMgmtOutletsTableCurrentLowCritical':pmPowerMgmtOutletsTableCurrentLowCritical,'pmPowerMgmtOutletsTableEnergyValue':pmPowerMgmtOutletsTableEnergyValue,'pmPowerMgmtOutletsTableEnergyStartTime':pmPowerMgmtOutletsTableEnergyStartTime,'pmPowerMgmtOutletsTableEnergyReset':pmPowerMgmtOutletsTableEnergyReset,'pmPowerMgmtNumberOfOutletGroup':pmPowerMgmtNumberOfOutletGroup,'pmPowerMgmtGroupTable':pmPowerMgmtGroupTable,'pmPowerMgmtGroupTableEntry':pmPowerMgmtGroupTableEntry,_e:pmPowerMgmtGroupTableIndex,'pmPowerMgmtGroupTableName':pmPowerMgmtGroupTableName,'pmPowerMgmtGroupTableStatus':pmPowerMgmtGroupTableStatus,'pmPowerMgmtGroupTablePowerControl':pmPowerMgmtGroupTablePowerControl,'pmPowerMgmtTotalNumberOfPhases':pmPowerMgmtTotalNumberOfPhases,'pmPowerMgmtPhasesTable':pmPowerMgmtPhasesTable,'pmPowerMgmtPhasesTableEntry':pmPowerMgmtPhasesTableEntry,_f:pmPowerMgmtPhasesTablePortNumber,_g:pmPowerMgmtPhasesTablePduNumber,_h:pmPowerMgmtPhasesTableNumber,'pmPowerMgmtPhasesTableName':pmPowerMgmtPhasesTableName,'pmPowerMgmtPhasesTablePortName':pmPowerMgmtPhasesTablePortName,'pmPowerMgmtPhasesTablePduId':pmPowerMgmtPhasesTablePduId,'pmPowerMgmtPhasesTableAlarm':pmPowerMgmtPhasesTableAlarm,'pmPowerMgmtPhasesTableCurrentValue':pmPowerMgmtPhasesTableCurrentValue,'pmPowerMgmtPhasesTableCurrentMax':pmPowerMgmtPhasesTableCurrentMax,'pmPowerMgmtPhasesTableCurrentMin':pmPowerMgmtPhasesTableCurrentMin,'pmPowerMgmtPhasesTableCurrentAvg':pmPowerMgmtPhasesTableCurrentAvg,'pmPowerMgmtPhasesTableCurrentReset':pmPowerMgmtPhasesTableCurrentReset,'pmPowerMgmtPhasesTablePowerValue':pmPowerMgmtPhasesTablePowerValue,'pmPowerMgmtPhasesTablePowerMax':pmPowerMgmtPhasesTablePowerMax,'pmPowerMgmtPhasesTablePowerMin':pmPowerMgmtPhasesTablePowerMin,'pmPowerMgmtPhasesTablePowerAvg':pmPowerMgmtPhasesTablePowerAvg,'pmPowerMgmtPhasesTablePowerReset':pmPowerMgmtPhasesTablePowerReset,'pmPowerMgmtPhasesTablePowerType':pmPowerMgmtPhasesTablePowerType,'pmPowerMgmtPhasesTableVoltageValue':pmPowerMgmtPhasesTableVoltageValue,'pmPowerMgmtPhasesTableVoltageMax':pmPowerMgmtPhasesTableVoltageMax,'pmPowerMgmtPhasesTableVoltageMin':pmPowerMgmtPhasesTableVoltageMin,'pmPowerMgmtPhasesTableVoltageAvg':pmPowerMgmtPhasesTableVoltageAvg,'pmPowerMgmtPhasesTableVoltageReset':pmPowerMgmtPhasesTableVoltageReset,'pmPowerMgmtPhasesTableVoltageType':pmPowerMgmtPhasesTableVoltageType,'pmPowerMgmtPhasesTablePowerFactorValue':pmPowerMgmtPhasesTablePowerFactorValue,'pmPowerMgmtPhasesTablePowerFactorMax':pmPowerMgmtPhasesTablePowerFactorMax,'pmPowerMgmtPhasesTablePowerFactorMin':pmPowerMgmtPhasesTablePowerFactorMin,'pmPowerMgmtPhasesTablePowerFactorAvg':pmPowerMgmtPhasesTablePowerFactorAvg,'pmPowerMgmtPhasesTablePowerFactorReset':pmPowerMgmtPhasesTablePowerFactorReset,'pmPowerMgmtPhasesTablePowerFactorType':pmPowerMgmtPhasesTablePowerFactorType,'pmPowerMgmtPhasesTableCurrentHighCritical':pmPowerMgmtPhasesTableCurrentHighCritical,'pmPowerMgmtPhasesTableCurrentHighWarning':pmPowerMgmtPhasesTableCurrentHighWarning,'pmPowerMgmtPhasesTableCurrentLowWarning':pmPowerMgmtPhasesTableCurrentLowWarning,'pmPowerMgmtPhasesTableCurrentLowCritical':pmPowerMgmtPhasesTableCurrentLowCritical,'pmPowerMgmtTotalNumberOfBanks':pmPowerMgmtTotalNumberOfBanks,'pmPowerMgmtBanksTable':pmPowerMgmtBanksTable,'pmPowerMgmtBanksTableEntry':pmPowerMgmtBanksTableEntry,_i:pmPowerMgmtBanksTablePortNumber,_j:pmPowerMgmtBanksTablePduNumber,_k:pmPowerMgmtBanksTableNumber,'pmPowerMgmtBanksTableName':pmPowerMgmtBanksTableName,'pmPowerMgmtBanksTablePortName':pmPowerMgmtBanksTablePortName,'pmPowerMgmtBanksTablePduId':pmPowerMgmtBanksTablePduId,'pmPowerMgmtBanksTableAlarm':pmPowerMgmtBanksTableAlarm,'pmPowerMgmtBanksTableCurrentValue':pmPowerMgmtBanksTableCurrentValue,'pmPowerMgmtBanksTableCurrentMax':pmPowerMgmtBanksTableCurrentMax,'pmPowerMgmtBanksTableCurrentMin':pmPowerMgmtBanksTableCurrentMin,'pmPowerMgmtBanksTableCurrentAvg':pmPowerMgmtBanksTableCurrentAvg,'pmPowerMgmtBanksTableCurrentReset':pmPowerMgmtBanksTableCurrentReset,'pmPowerMgmtBanksTablePowerValue':pmPowerMgmtBanksTablePowerValue,'pmPowerMgmtBanksTablePowerMax':pmPowerMgmtBanksTablePowerMax,'pmPowerMgmtBanksTablePowerMin':pmPowerMgmtBanksTablePowerMin,'pmPowerMgmtBanksTablePowerAvg':pmPowerMgmtBanksTablePowerAvg,'pmPowerMgmtBanksTablePowerReset':pmPowerMgmtBanksTablePowerReset,'pmPowerMgmtBanksTablePowerType':pmPowerMgmtBanksTablePowerType,'pmPowerMgmtBanksTableVoltageValue':pmPowerMgmtBanksTableVoltageValue,'pmPowerMgmtBanksTableVoltageMax':pmPowerMgmtBanksTableVoltageMax,'pmPowerMgmtBanksTableVoltageMin':pmPowerMgmtBanksTableVoltageMin,'pmPowerMgmtBanksTableVoltageAvg':pmPowerMgmtBanksTableVoltageAvg,'pmPowerMgmtBanksTableVoltageReset':pmPowerMgmtBanksTableVoltageReset,'pmPowerMgmtBanksTableVoltageType':pmPowerMgmtBanksTableVoltageType,'pmPowerMgmtBanksTablePowerFactorValue':pmPowerMgmtBanksTablePowerFactorValue,'pmPowerMgmtBanksTablePowerFactorMax':pmPowerMgmtBanksTablePowerFactorMax,'pmPowerMgmtBanksTablePowerFactorMin':pmPowerMgmtBanksTablePowerFactorMin,'pmPowerMgmtBanksTablePowerFactorAvg':pmPowerMgmtBanksTablePowerFactorAvg,'pmPowerMgmtBanksTablePowerFactorReset':pmPowerMgmtBanksTablePowerFactorReset,'pmPowerMgmtBanksTablePowerFactorType':pmPowerMgmtBanksTablePowerFactorType,'pmPowerMgmtBanksTableCurrentHighCritical':pmPowerMgmtBanksTableCurrentHighCritical,'pmPowerMgmtBanksTableCurrentHighWarning':pmPowerMgmtBanksTableCurrentHighWarning,'pmPowerMgmtBanksTableCurrentLowWarning':pmPowerMgmtBanksTableCurrentLowWarning,'pmPowerMgmtBanksTableCurrentLowCritical':pmPowerMgmtBanksTableCurrentLowCritical,'pmPowerMgmtBanksTableEnergyValue':pmPowerMgmtBanksTableEnergyValue,'pmPowerMgmtBanksTableEnergyStartTime':pmPowerMgmtBanksTableEnergyStartTime,'pmPowerMgmtBanksTableEnergyReset':pmPowerMgmtBanksTableEnergyReset,'pmPowerMgmtTotalNumberOfSensors':pmPowerMgmtTotalNumberOfSensors,'pmPowerMgmtSensorsTable':pmPowerMgmtSensorsTable,'pmPowerMgmtSensorsTableEntry':pmPowerMgmtSensorsTableEntry,_l:pmPowerMgmtSensorsTablePortNumber,_m:pmPowerMgmtSensorsTablePduNumber,_n:pmPowerMgmtSensorsTableNumber,'pmPowerMgmtSensorsTableName':pmPowerMgmtSensorsTableName,'pmPowerMgmtSensorsTablePortName':pmPowerMgmtSensorsTablePortName,'pmPowerMgmtSensorsTablePduId':pmPowerMgmtSensorsTablePduId,'pmPowerMgmtSensorsTableType':pmPowerMgmtSensorsTableType,'pmPowerMgmtSensorsTableStatus':pmPowerMgmtSensorsTableStatus,'pmPowerMgmtSensorsTableValue':pmPowerMgmtSensorsTableValue,'pmPowerMgmtSensorsTableValueMax':pmPowerMgmtSensorsTableValueMax,'pmPowerMgmtSensorsTableValueMin':pmPowerMgmtSensorsTableValueMin,'pmPowerMgmtSensorsTableValueAvg':pmPowerMgmtSensorsTableValueAvg,'pmPowerMgmtSensorsTableValueInt':pmPowerMgmtSensorsTableValueInt,'pmPowerMgmtSensorsTableValueMaxInt':pmPowerMgmtSensorsTableValueMaxInt,'pmPowerMgmtSensorsTableValueMinInt':pmPowerMgmtSensorsTableValueMinInt,'pmPowerMgmtSensorsTableValueAvgInt':pmPowerMgmtSensorsTableValueAvgInt,'pmPowerMgmtSensorsTableValueReset':pmPowerMgmtSensorsTableValueReset,'pmPowerMgmtSensorsTableHighCritical':pmPowerMgmtSensorsTableHighCritical,'pmPowerMgmtSensorsTableHighWarning':pmPowerMgmtSensorsTableHighWarning,'pmPowerMgmtSensorsTableLowWarning':pmPowerMgmtSensorsTableLowWarning,'pmPowerMgmtSensorsTableLowCritical':pmPowerMgmtSensorsTableLowCritical,'pmPowerMgmtSensorsTableUnit':pmPowerMgmtSensorsTableUnit,'pmPowerMgmtSensorsTableHighCriticalC':pmPowerMgmtSensorsTableHighCriticalC,'pmPowerMgmtSensorsTableHighWarningC':pmPowerMgmtSensorsTableHighWarningC,'pmPowerMgmtSensorsTableLowWarningC':pmPowerMgmtSensorsTableLowWarningC,'pmPowerMgmtSensorsTableLowCriticalC':pmPowerMgmtSensorsTableLowCriticalC,'pmPowerMgmtSensorsTableHighCriticalF':pmPowerMgmtSensorsTableHighCriticalF,'pmPowerMgmtSensorsTableHighWarningF':pmPowerMgmtSensorsTableHighWarningF,'pmPowerMgmtSensorsTableLowWarningF':pmPowerMgmtSensorsTableLowWarningF,'pmPowerMgmtSensorsTableLowCriticalF':pmPowerMgmtSensorsTableLowCriticalF,'pmTrapObject':pmTrapObject})