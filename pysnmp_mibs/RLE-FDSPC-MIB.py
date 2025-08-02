_I='modbusDeviceRegisterIndex'
_H='registerIndex'
_G='NotificationType'
_F='fdsPcTrapRegisterLabel'
_E='fdsPcTrapRegisterNumber'
_D='not-accessible'
_C='RLE-FDSPC-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
TruthValue,=mibBuilder.importSymbols('RFC1253-MIB','TruthValue')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier',_G,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_G,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Rle_ObjectIdentity=ObjectIdentity
rle=_Rle_ObjectIdentity((1,3,6,1,4,1,3184))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,3184,1))
_Fds_ObjectIdentity=ObjectIdentity
fds=_Fds_ObjectIdentity((1,3,6,1,4,1,3184,1,10))
_FdsPc_ObjectIdentity=ObjectIdentity
fdsPc=_FdsPc_ObjectIdentity((1,3,6,1,4,1,3184,1,10,3))
_FdsIdent_ObjectIdentity=ObjectIdentity
fdsIdent=_FdsIdent_ObjectIdentity((1,3,6,1,4,1,3184,1,10,3,1))
_FdsIdentManufacturer_Type=DisplayString
_FdsIdentManufacturer_Object=MibScalar
fdsIdentManufacturer=_FdsIdentManufacturer_Object((1,3,6,1,4,1,3184,1,10,3,1,1),_FdsIdentManufacturer_Type())
fdsIdentManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:fdsIdentManufacturer.setStatus(_A)
_FdsIdentModel_Type=DisplayString
_FdsIdentModel_Object=MibScalar
fdsIdentModel=_FdsIdentModel_Object((1,3,6,1,4,1,3184,1,10,3,1,2),_FdsIdentModel_Type())
fdsIdentModel.setMaxAccess(_B)
if mibBuilder.loadTexts:fdsIdentModel.setStatus(_A)
_FdsIdentSoftwareVersion_Type=DisplayString
_FdsIdentSoftwareVersion_Object=MibScalar
fdsIdentSoftwareVersion=_FdsIdentSoftwareVersion_Object((1,3,6,1,4,1,3184,1,10,3,1,3),_FdsIdentSoftwareVersion_Type())
fdsIdentSoftwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:fdsIdentSoftwareVersion.setStatus(_A)
_FdsRegisters_ObjectIdentity=ObjectIdentity
fdsRegisters=_FdsRegisters_ObjectIdentity((1,3,6,1,4,1,3184,1,10,3,2))
_RegisterTable_Object=MibTable
registerTable=_RegisterTable_Object((1,3,6,1,4,1,3184,1,10,3,2,1))
if mibBuilder.loadTexts:registerTable.setStatus(_A)
_RegisterTableEntry_Object=MibTableRow
registerTableEntry=_RegisterTableEntry_Object((1,3,6,1,4,1,3184,1,10,3,2,1,1))
registerTableEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:registerTableEntry.setStatus(_A)
_RegisterIndex_Type=Integer32
_RegisterIndex_Object=MibTableColumn
registerIndex=_RegisterIndex_Object((1,3,6,1,4,1,3184,1,10,3,2,1,1,1),_RegisterIndex_Type())
registerIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:registerIndex.setStatus(_A)
_RegisterIntData_Type=Integer32
_RegisterIntData_Object=MibTableColumn
registerIntData=_RegisterIntData_Object((1,3,6,1,4,1,3184,1,10,3,2,1,1,2),_RegisterIntData_Type())
registerIntData.setMaxAccess(_B)
if mibBuilder.loadTexts:registerIntData.setStatus(_A)
_RegisterFloatData_Type=DisplayString
_RegisterFloatData_Object=MibTableColumn
registerFloatData=_RegisterFloatData_Object((1,3,6,1,4,1,3184,1,10,3,2,1,1,3),_RegisterFloatData_Type())
registerFloatData.setMaxAccess(_B)
if mibBuilder.loadTexts:registerFloatData.setStatus(_A)
_RegisterName_Type=DisplayString
_RegisterName_Object=MibTableColumn
registerName=_RegisterName_Object((1,3,6,1,4,1,3184,1,10,3,2,1,1,4),_RegisterName_Type())
registerName.setMaxAccess(_B)
if mibBuilder.loadTexts:registerName.setStatus(_A)
_FdsModbusDeviceRegisters_ObjectIdentity=ObjectIdentity
fdsModbusDeviceRegisters=_FdsModbusDeviceRegisters_ObjectIdentity((1,3,6,1,4,1,3184,1,10,3,3))
_ModbusDeviceRegisterTable_Object=MibTable
modbusDeviceRegisterTable=_ModbusDeviceRegisterTable_Object((1,3,6,1,4,1,3184,1,10,3,3,1))
if mibBuilder.loadTexts:modbusDeviceRegisterTable.setStatus(_A)
_ModbusDeviceRegisterTableEntry_Object=MibTableRow
modbusDeviceRegisterTableEntry=_ModbusDeviceRegisterTableEntry_Object((1,3,6,1,4,1,3184,1,10,3,3,1,1))
modbusDeviceRegisterTableEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:modbusDeviceRegisterTableEntry.setStatus(_A)
_ModbusDeviceRegisterIndex_Type=Integer32
_ModbusDeviceRegisterIndex_Object=MibTableColumn
modbusDeviceRegisterIndex=_ModbusDeviceRegisterIndex_Object((1,3,6,1,4,1,3184,1,10,3,3,1,1,1),_ModbusDeviceRegisterIndex_Type())
modbusDeviceRegisterIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:modbusDeviceRegisterIndex.setStatus(_A)
_ModbusDeviceRegisterIntData_Type=Integer32
_ModbusDeviceRegisterIntData_Object=MibTableColumn
modbusDeviceRegisterIntData=_ModbusDeviceRegisterIntData_Object((1,3,6,1,4,1,3184,1,10,3,3,1,1,2),_ModbusDeviceRegisterIntData_Type())
modbusDeviceRegisterIntData.setMaxAccess(_B)
if mibBuilder.loadTexts:modbusDeviceRegisterIntData.setStatus(_A)
_ModbusDeviceRegisterFloatData_Type=DisplayString
_ModbusDeviceRegisterFloatData_Object=MibTableColumn
modbusDeviceRegisterFloatData=_ModbusDeviceRegisterFloatData_Object((1,3,6,1,4,1,3184,1,10,3,3,1,1,3),_ModbusDeviceRegisterFloatData_Type())
modbusDeviceRegisterFloatData.setMaxAccess(_B)
if mibBuilder.loadTexts:modbusDeviceRegisterFloatData.setStatus(_A)
_ModbusDeviceRegisterName_Type=DisplayString
_ModbusDeviceRegisterName_Object=MibTableColumn
modbusDeviceRegisterName=_ModbusDeviceRegisterName_Object((1,3,6,1,4,1,3184,1,10,3,3,1,1,4),_ModbusDeviceRegisterName_Type())
modbusDeviceRegisterName.setMaxAccess(_B)
if mibBuilder.loadTexts:modbusDeviceRegisterName.setStatus(_A)
_FdsPcTrapData_ObjectIdentity=ObjectIdentity
fdsPcTrapData=_FdsPcTrapData_ObjectIdentity((1,3,6,1,4,1,3184,1,10,3,10))
_FdsPcTrapRegisterNumber_Type=Integer32
_FdsPcTrapRegisterNumber_Object=MibScalar
fdsPcTrapRegisterNumber=_FdsPcTrapRegisterNumber_Object((1,3,6,1,4,1,3184,1,10,3,10,1),_FdsPcTrapRegisterNumber_Type())
fdsPcTrapRegisterNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:fdsPcTrapRegisterNumber.setStatus(_A)
_FdsPcTrapRegisterLabel_Type=DisplayString
_FdsPcTrapRegisterLabel_Object=MibScalar
fdsPcTrapRegisterLabel=_FdsPcTrapRegisterLabel_Object((1,3,6,1,4,1,3184,1,10,3,10,2),_FdsPcTrapRegisterLabel_Type())
fdsPcTrapRegisterLabel.setMaxAccess(_D)
if mibBuilder.loadTexts:fdsPcTrapRegisterLabel.setStatus(_A)
_FdsPcTraps_ObjectIdentity=ObjectIdentity
fdsPcTraps=_FdsPcTraps_ObjectIdentity((1,3,6,1,4,1,3184,1,10,3,11))
fdsPcAlarmTrap=NotificationType((1,3,6,1,4,1,3184,1,10,3,11,0,1))
fdsPcAlarmTrap.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:fdsPcAlarmTrap.setStatus('')
fdsPcOfflineTrap=NotificationType((1,3,6,1,4,1,3184,1,10,3,11,0,2))
fdsPcOfflineTrap.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:fdsPcOfflineTrap.setStatus('')
mibBuilder.exportSymbols(_C,**{'rle':rle,'products':products,'fds':fds,'fdsPc':fdsPc,'fdsIdent':fdsIdent,'fdsIdentManufacturer':fdsIdentManufacturer,'fdsIdentModel':fdsIdentModel,'fdsIdentSoftwareVersion':fdsIdentSoftwareVersion,'fdsRegisters':fdsRegisters,'registerTable':registerTable,'registerTableEntry':registerTableEntry,_H:registerIndex,'registerIntData':registerIntData,'registerFloatData':registerFloatData,'registerName':registerName,'fdsModbusDeviceRegisters':fdsModbusDeviceRegisters,'modbusDeviceRegisterTable':modbusDeviceRegisterTable,'modbusDeviceRegisterTableEntry':modbusDeviceRegisterTableEntry,_I:modbusDeviceRegisterIndex,'modbusDeviceRegisterIntData':modbusDeviceRegisterIntData,'modbusDeviceRegisterFloatData':modbusDeviceRegisterFloatData,'modbusDeviceRegisterName':modbusDeviceRegisterName,'fdsPcTrapData':fdsPcTrapData,_E:fdsPcTrapRegisterNumber,_F:fdsPcTrapRegisterLabel,'fdsPcTraps':fdsPcTraps,'fdsPcAlarmTrap':fdsPcAlarmTrap,'fdsPcOfflineTrap':fdsPcOfflineTrap})