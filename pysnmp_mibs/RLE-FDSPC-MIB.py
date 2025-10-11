# SNMP MIB module (RLE-FDSPC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/chatsworth/RLE-FDSPC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:52:00 2025
# On host Robs-Air.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(TruthValue,) = mibBuilder.importSymbols(
    "RFC1253-MIB",
    "TruthValue")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Rle_ObjectIdentity = ObjectIdentity
rle = _Rle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1)
)
_Fds_ObjectIdentity = ObjectIdentity
fds = _Fds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 10)
)
_FdsPc_ObjectIdentity = ObjectIdentity
fdsPc = _FdsPc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 10, 3)
)
_FdsIdent_ObjectIdentity = ObjectIdentity
fdsIdent = _FdsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 10, 3, 1)
)
_FdsIdentManufacturer_Type = DisplayString
_FdsIdentManufacturer_Object = MibScalar
fdsIdentManufacturer = _FdsIdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 10, 3, 1, 1),
    _FdsIdentManufacturer_Type()
)
fdsIdentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdsIdentManufacturer.setStatus("mandatory")
_FdsIdentModel_Type = DisplayString
_FdsIdentModel_Object = MibScalar
fdsIdentModel = _FdsIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 10, 3, 1, 2),
    _FdsIdentModel_Type()
)
fdsIdentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdsIdentModel.setStatus("mandatory")
_FdsIdentSoftwareVersion_Type = DisplayString
_FdsIdentSoftwareVersion_Object = MibScalar
fdsIdentSoftwareVersion = _FdsIdentSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 10, 3, 1, 3),
    _FdsIdentSoftwareVersion_Type()
)
fdsIdentSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdsIdentSoftwareVersion.setStatus("mandatory")
_FdsRegisters_ObjectIdentity = ObjectIdentity
fdsRegisters = _FdsRegisters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 10, 3, 2)
)
_RegisterTable_Object = MibTable
registerTable = _RegisterTable_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 10, 3, 2, 1)
)
if mibBuilder.loadTexts:
    registerTable.setStatus("mandatory")
_RegisterTableEntry_Object = MibTableRow
registerTableEntry = _RegisterTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 10, 3, 2, 1, 1)
)
registerTableEntry.setIndexNames(
    (0, "RLE-FDSPC-MIB", "registerIndex"),
)
if mibBuilder.loadTexts:
    registerTableEntry.setStatus("mandatory")
_RegisterIndex_Type = Integer32
_RegisterIndex_Object = MibTableColumn
registerIndex = _RegisterIndex_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 10, 3, 2, 1, 1, 1),
    _RegisterIndex_Type()
)
registerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    registerIndex.setStatus("mandatory")
_RegisterIntData_Type = Integer32
_RegisterIntData_Object = MibTableColumn
registerIntData = _RegisterIntData_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 10, 3, 2, 1, 1, 2),
    _RegisterIntData_Type()
)
registerIntData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    registerIntData.setStatus("mandatory")
_RegisterFloatData_Type = DisplayString
_RegisterFloatData_Object = MibTableColumn
registerFloatData = _RegisterFloatData_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 10, 3, 2, 1, 1, 3),
    _RegisterFloatData_Type()
)
registerFloatData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    registerFloatData.setStatus("mandatory")
_RegisterName_Type = DisplayString
_RegisterName_Object = MibTableColumn
registerName = _RegisterName_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 10, 3, 2, 1, 1, 4),
    _RegisterName_Type()
)
registerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    registerName.setStatus("mandatory")
_FdsModbusDeviceRegisters_ObjectIdentity = ObjectIdentity
fdsModbusDeviceRegisters = _FdsModbusDeviceRegisters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 10, 3, 3)
)
_ModbusDeviceRegisterTable_Object = MibTable
modbusDeviceRegisterTable = _ModbusDeviceRegisterTable_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 10, 3, 3, 1)
)
if mibBuilder.loadTexts:
    modbusDeviceRegisterTable.setStatus("mandatory")
_ModbusDeviceRegisterTableEntry_Object = MibTableRow
modbusDeviceRegisterTableEntry = _ModbusDeviceRegisterTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 10, 3, 3, 1, 1)
)
modbusDeviceRegisterTableEntry.setIndexNames(
    (0, "RLE-FDSPC-MIB", "modbusDeviceRegisterIndex"),
)
if mibBuilder.loadTexts:
    modbusDeviceRegisterTableEntry.setStatus("mandatory")
_ModbusDeviceRegisterIndex_Type = Integer32
_ModbusDeviceRegisterIndex_Object = MibTableColumn
modbusDeviceRegisterIndex = _ModbusDeviceRegisterIndex_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 10, 3, 3, 1, 1, 1),
    _ModbusDeviceRegisterIndex_Type()
)
modbusDeviceRegisterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    modbusDeviceRegisterIndex.setStatus("mandatory")
_ModbusDeviceRegisterIntData_Type = Integer32
_ModbusDeviceRegisterIntData_Object = MibTableColumn
modbusDeviceRegisterIntData = _ModbusDeviceRegisterIntData_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 10, 3, 3, 1, 1, 2),
    _ModbusDeviceRegisterIntData_Type()
)
modbusDeviceRegisterIntData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modbusDeviceRegisterIntData.setStatus("mandatory")
_ModbusDeviceRegisterFloatData_Type = DisplayString
_ModbusDeviceRegisterFloatData_Object = MibTableColumn
modbusDeviceRegisterFloatData = _ModbusDeviceRegisterFloatData_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 10, 3, 3, 1, 1, 3),
    _ModbusDeviceRegisterFloatData_Type()
)
modbusDeviceRegisterFloatData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modbusDeviceRegisterFloatData.setStatus("mandatory")
_ModbusDeviceRegisterName_Type = DisplayString
_ModbusDeviceRegisterName_Object = MibTableColumn
modbusDeviceRegisterName = _ModbusDeviceRegisterName_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 10, 3, 3, 1, 1, 4),
    _ModbusDeviceRegisterName_Type()
)
modbusDeviceRegisterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modbusDeviceRegisterName.setStatus("mandatory")
_FdsPcTrapData_ObjectIdentity = ObjectIdentity
fdsPcTrapData = _FdsPcTrapData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 10, 3, 10)
)
_FdsPcTrapRegisterNumber_Type = Integer32
_FdsPcTrapRegisterNumber_Object = MibScalar
fdsPcTrapRegisterNumber = _FdsPcTrapRegisterNumber_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 10, 3, 10, 1),
    _FdsPcTrapRegisterNumber_Type()
)
fdsPcTrapRegisterNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdsPcTrapRegisterNumber.setStatus("mandatory")
_FdsPcTrapRegisterLabel_Type = DisplayString
_FdsPcTrapRegisterLabel_Object = MibScalar
fdsPcTrapRegisterLabel = _FdsPcTrapRegisterLabel_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 10, 3, 10, 2),
    _FdsPcTrapRegisterLabel_Type()
)
fdsPcTrapRegisterLabel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdsPcTrapRegisterLabel.setStatus("mandatory")
_FdsPcTraps_ObjectIdentity = ObjectIdentity
fdsPcTraps = _FdsPcTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 10, 3, 11)
)

# Managed Objects groups


# Notification objects

fdsPcAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 10, 3, 11, 0, 1)
)
fdsPcAlarmTrap.setObjects(
      *(("RLE-FDSPC-MIB", "fdsPcTrapRegisterNumber"),
        ("RLE-FDSPC-MIB", "fdsPcTrapRegisterLabel"))
)
if mibBuilder.loadTexts:
    fdsPcAlarmTrap.setStatus(
        ""
    )

fdsPcOfflineTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 10, 3, 11, 0, 2)
)
fdsPcOfflineTrap.setObjects(
      *(("RLE-FDSPC-MIB", "fdsPcTrapRegisterNumber"),
        ("RLE-FDSPC-MIB", "fdsPcTrapRegisterLabel"))
)
if mibBuilder.loadTexts:
    fdsPcOfflineTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RLE-FDSPC-MIB",
    **{"rle": rle,
       "products": products,
       "fds": fds,
       "fdsPc": fdsPc,
       "fdsIdent": fdsIdent,
       "fdsIdentManufacturer": fdsIdentManufacturer,
       "fdsIdentModel": fdsIdentModel,
       "fdsIdentSoftwareVersion": fdsIdentSoftwareVersion,
       "fdsRegisters": fdsRegisters,
       "registerTable": registerTable,
       "registerTableEntry": registerTableEntry,
       "registerIndex": registerIndex,
       "registerIntData": registerIntData,
       "registerFloatData": registerFloatData,
       "registerName": registerName,
       "fdsModbusDeviceRegisters": fdsModbusDeviceRegisters,
       "modbusDeviceRegisterTable": modbusDeviceRegisterTable,
       "modbusDeviceRegisterTableEntry": modbusDeviceRegisterTableEntry,
       "modbusDeviceRegisterIndex": modbusDeviceRegisterIndex,
       "modbusDeviceRegisterIntData": modbusDeviceRegisterIntData,
       "modbusDeviceRegisterFloatData": modbusDeviceRegisterFloatData,
       "modbusDeviceRegisterName": modbusDeviceRegisterName,
       "fdsPcTrapData": fdsPcTrapData,
       "fdsPcTrapRegisterNumber": fdsPcTrapRegisterNumber,
       "fdsPcTrapRegisterLabel": fdsPcTrapRegisterLabel,
       "fdsPcTraps": fdsPcTraps,
       "fdsPcAlarmTrap": fdsPcAlarmTrap,
       "fdsPcOfflineTrap": fdsPcOfflineTrap}
)
