# SNMP MIB module (ELECTROLINE-DHT-TEST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/electroline/ELECTROLINE-DHT-TEST-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:07:06 2025
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

(dhtPrivate,) = mibBuilder.importSymbols(
    "ELECTROLINE-DHT-ROOT-MIB",
    "dhtPrivate")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TimeTicks,
 Unsigned32,
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
    "TimeTicks",
    "Unsigned32",
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DhtTest_ObjectIdentity = ObjectIdentity
dhtTest = _DhtTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 4, 1)
)
_DhtAnalogPorts_ObjectIdentity = ObjectIdentity
dhtAnalogPorts = _DhtAnalogPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 4, 1, 1)
)
_CurrentAnalogValueTable_Object = MibTable
currentAnalogValueTable = _CurrentAnalogValueTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    currentAnalogValueTable.setStatus("current")
_CurrentAnalogValueEntry_Object = MibTableRow
currentAnalogValueEntry = _CurrentAnalogValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 4, 1, 1, 1, 1)
)
currentAnalogValueEntry.setIndexNames(
    (0, "ELECTROLINE-DHT-TEST-MIB", "analogPortId"),
)
if mibBuilder.loadTexts:
    currentAnalogValueEntry.setStatus("current")
_AnalogPortId_Type = Integer32
_AnalogPortId_Object = MibTableColumn
analogPortId = _AnalogPortId_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 4, 1, 1, 1, 1, 1),
    _AnalogPortId_Type()
)
analogPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analogPortId.setStatus("current")
_AnalogValue_Type = Integer32
_AnalogValue_Object = MibTableColumn
analogValue = _AnalogValue_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 4, 1, 1, 1, 1, 2),
    _AnalogValue_Type()
)
analogValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analogValue.setStatus("current")
_AnalogPortIdDesc_Type = OctetString
_AnalogPortIdDesc_Object = MibTableColumn
analogPortIdDesc = _AnalogPortIdDesc_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 4, 1, 1, 1, 1, 3),
    _AnalogPortIdDesc_Type()
)
analogPortIdDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analogPortIdDesc.setStatus("current")
_AnalogCalibrationValue_Type = Integer32
_AnalogCalibrationValue_Object = MibScalar
analogCalibrationValue = _AnalogCalibrationValue_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 4, 1, 1, 2),
    _AnalogCalibrationValue_Type()
)
analogCalibrationValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogCalibrationValue.setStatus("current")
_AnalogPortToCalibrate_Type = Integer32
_AnalogPortToCalibrate_Object = MibScalar
analogPortToCalibrate = _AnalogPortToCalibrate_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 4, 1, 1, 3),
    _AnalogPortToCalibrate_Type()
)
analogPortToCalibrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogPortToCalibrate.setStatus("current")


class _AnalogCalibrationCommit_Type(Integer32):
    """Custom type analogCalibrationCommit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AnalogCalibrationCommit_Type.__name__ = "Integer32"
_AnalogCalibrationCommit_Object = MibScalar
analogCalibrationCommit = _AnalogCalibrationCommit_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 4, 1, 1, 4),
    _AnalogCalibrationCommit_Type()
)
analogCalibrationCommit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogCalibrationCommit.setStatus("current")


class _AnalogCalibrationSetDefault_Type(Integer32):
    """Custom type analogCalibrationSetDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AnalogCalibrationSetDefault_Type.__name__ = "Integer32"
_AnalogCalibrationSetDefault_Object = MibScalar
analogCalibrationSetDefault = _AnalogCalibrationSetDefault_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 4, 1, 1, 5),
    _AnalogCalibrationSetDefault_Type()
)
analogCalibrationSetDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogCalibrationSetDefault.setStatus("current")
_CurrentCalibrationValueTable_Object = MibTable
currentCalibrationValueTable = _CurrentCalibrationValueTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 4, 1, 1, 6)
)
if mibBuilder.loadTexts:
    currentCalibrationValueTable.setStatus("current")
_CurrentCalibrationValueEntry_Object = MibTableRow
currentCalibrationValueEntry = _CurrentCalibrationValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 4, 1, 1, 6, 1)
)
currentCalibrationValueEntry.setIndexNames(
    (0, "ELECTROLINE-DHT-TEST-MIB", "analogCalibrationPortId"),
)
if mibBuilder.loadTexts:
    currentCalibrationValueEntry.setStatus("current")
_AnalogCalibrationPortId_Type = Integer32
_AnalogCalibrationPortId_Object = MibTableColumn
analogCalibrationPortId = _AnalogCalibrationPortId_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 4, 1, 1, 6, 1, 1),
    _AnalogCalibrationPortId_Type()
)
analogCalibrationPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analogCalibrationPortId.setStatus("current")
_RawValue_Type = Integer32
_RawValue_Object = MibTableColumn
rawValue = _RawValue_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 4, 1, 1, 6, 1, 2),
    _RawValue_Type()
)
rawValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rawValue.setStatus("current")
_CalibratedValue_Type = Integer32
_CalibratedValue_Object = MibTableColumn
calibratedValue = _CalibratedValue_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 4, 1, 1, 6, 1, 3),
    _CalibratedValue_Type()
)
calibratedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calibratedValue.setStatus("current")
_CalibratedPortIdDesc_Type = OctetString
_CalibratedPortIdDesc_Object = MibTableColumn
calibratedPortIdDesc = _CalibratedPortIdDesc_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 4, 1, 1, 6, 1, 4),
    _CalibratedPortIdDesc_Type()
)
calibratedPortIdDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calibratedPortIdDesc.setStatus("current")
_DhtDigitalPorts_ObjectIdentity = ObjectIdentity
dhtDigitalPorts = _DhtDigitalPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 4, 1, 2)
)
_CurrentDigitalStatusTable_Object = MibTable
currentDigitalStatusTable = _CurrentDigitalStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    currentDigitalStatusTable.setStatus("current")
_CurrentDigitalStatusEntry_Object = MibTableRow
currentDigitalStatusEntry = _CurrentDigitalStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 4, 1, 2, 1, 1)
)
currentDigitalStatusEntry.setIndexNames(
    (0, "ELECTROLINE-DHT-TEST-MIB", "statusPortId"),
)
if mibBuilder.loadTexts:
    currentDigitalStatusEntry.setStatus("current")
_StatusPortId_Type = Integer32
_StatusPortId_Object = MibTableColumn
statusPortId = _StatusPortId_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 4, 1, 2, 1, 1, 1),
    _StatusPortId_Type()
)
statusPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPortId.setStatus("current")
_StatusValue_Type = Integer32
_StatusValue_Object = MibTableColumn
statusValue = _StatusValue_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 4, 1, 2, 1, 1, 2),
    _StatusValue_Type()
)
statusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusValue.setStatus("current")
_StatusPortIdDesc_Type = OctetString
_StatusPortIdDesc_Object = MibTableColumn
statusPortIdDesc = _StatusPortIdDesc_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 4, 1, 2, 1, 1, 3),
    _StatusPortIdDesc_Type()
)
statusPortIdDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPortIdDesc.setStatus("current")
_CurrentDigitalControlTable_Object = MibTable
currentDigitalControlTable = _CurrentDigitalControlTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 4, 1, 2, 2)
)
if mibBuilder.loadTexts:
    currentDigitalControlTable.setStatus("current")
_CurrentDigitalControlEntry_Object = MibTableRow
currentDigitalControlEntry = _CurrentDigitalControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 4, 1, 2, 2, 1)
)
currentDigitalControlEntry.setIndexNames(
    (0, "ELECTROLINE-DHT-TEST-MIB", "controlPortId"),
)
if mibBuilder.loadTexts:
    currentDigitalControlEntry.setStatus("current")
_ControlPortId_Type = Integer32
_ControlPortId_Object = MibTableColumn
controlPortId = _ControlPortId_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 4, 1, 2, 2, 1, 1),
    _ControlPortId_Type()
)
controlPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlPortId.setStatus("current")
_ControlValue_Type = Integer32
_ControlValue_Object = MibTableColumn
controlValue = _ControlValue_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 4, 1, 2, 2, 1, 2),
    _ControlValue_Type()
)
controlValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlValue.setStatus("current")
_ControlPortIdDesc_Type = OctetString
_ControlPortIdDesc_Object = MibTableColumn
controlPortIdDesc = _ControlPortIdDesc_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 4, 1, 2, 2, 1, 3),
    _ControlPortIdDesc_Type()
)
controlPortIdDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlPortIdDesc.setStatus("current")
_DhtMicroControllers_ObjectIdentity = ObjectIdentity
dhtMicroControllers = _DhtMicroControllers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 4, 1, 3)
)
_UsmFirmwareVersion_Type = OctetString
_UsmFirmwareVersion_Object = MibScalar
usmFirmwareVersion = _UsmFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 4, 1, 3, 1),
    _UsmFirmwareVersion_Type()
)
usmFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usmFirmwareVersion.setStatus("current")
_BatFirmwareVersion_Type = OctetString
_BatFirmwareVersion_Object = MibScalar
batFirmwareVersion = _BatFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 4, 1, 3, 2),
    _BatFirmwareVersion_Type()
)
batFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batFirmwareVersion.setStatus("current")


class _Reset_Type(Integer32):
    """Custom type reset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Reset_Type.__name__ = "Integer32"
_Reset_Object = MibScalar
reset = _Reset_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 4, 1, 3, 3),
    _Reset_Type()
)
reset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reset.setStatus("current")
_WakeUpVoltage_Type = Integer32
_WakeUpVoltage_Object = MibScalar
wakeUpVoltage = _WakeUpVoltage_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 4, 1, 3, 4),
    _WakeUpVoltage_Type()
)
wakeUpVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wakeUpVoltage.setStatus("current")
_WakeUpPortId_Type = Integer32
_WakeUpPortId_Object = MibScalar
wakeUpPortId = _WakeUpPortId_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 4, 1, 3, 5),
    _WakeUpPortId_Type()
)
wakeUpPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wakeUpPortId.setStatus("current")
_DhtExternalDevices_ObjectIdentity = ObjectIdentity
dhtExternalDevices = _DhtExternalDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 4, 1, 4)
)


class _SpiExternalTest_Type(Integer32):
    """Custom type spiExternalTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("passed", 2))
    )


_SpiExternalTest_Type.__name__ = "Integer32"
_SpiExternalTest_Object = MibScalar
spiExternalTest = _SpiExternalTest_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 4, 1, 4, 1),
    _SpiExternalTest_Type()
)
spiExternalTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spiExternalTest.setStatus("current")


class _CprTest_Type(Integer32):
    """Custom type cprTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("passed", 2))
    )


_CprTest_Type.__name__ = "Integer32"
_CprTest_Object = MibScalar
cprTest = _CprTest_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 4, 1, 4, 2),
    _CprTest_Type()
)
cprTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cprTest.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELECTROLINE-DHT-TEST-MIB",
    **{"dhtTest": dhtTest,
       "dhtAnalogPorts": dhtAnalogPorts,
       "currentAnalogValueTable": currentAnalogValueTable,
       "currentAnalogValueEntry": currentAnalogValueEntry,
       "analogPortId": analogPortId,
       "analogValue": analogValue,
       "analogPortIdDesc": analogPortIdDesc,
       "analogCalibrationValue": analogCalibrationValue,
       "analogPortToCalibrate": analogPortToCalibrate,
       "analogCalibrationCommit": analogCalibrationCommit,
       "analogCalibrationSetDefault": analogCalibrationSetDefault,
       "currentCalibrationValueTable": currentCalibrationValueTable,
       "currentCalibrationValueEntry": currentCalibrationValueEntry,
       "analogCalibrationPortId": analogCalibrationPortId,
       "rawValue": rawValue,
       "calibratedValue": calibratedValue,
       "calibratedPortIdDesc": calibratedPortIdDesc,
       "dhtDigitalPorts": dhtDigitalPorts,
       "currentDigitalStatusTable": currentDigitalStatusTable,
       "currentDigitalStatusEntry": currentDigitalStatusEntry,
       "statusPortId": statusPortId,
       "statusValue": statusValue,
       "statusPortIdDesc": statusPortIdDesc,
       "currentDigitalControlTable": currentDigitalControlTable,
       "currentDigitalControlEntry": currentDigitalControlEntry,
       "controlPortId": controlPortId,
       "controlValue": controlValue,
       "controlPortIdDesc": controlPortIdDesc,
       "dhtMicroControllers": dhtMicroControllers,
       "usmFirmwareVersion": usmFirmwareVersion,
       "batFirmwareVersion": batFirmwareVersion,
       "reset": reset,
       "wakeUpVoltage": wakeUpVoltage,
       "wakeUpPortId": wakeUpPortId,
       "dhtExternalDevices": dhtExternalDevices,
       "spiExternalTest": spiExternalTest,
       "cprTest": cprTest}
)
