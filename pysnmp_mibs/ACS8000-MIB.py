# SNMP MIB module (ACS8000-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/vertiv/ACS8000-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:05:47 2025
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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

acs = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 26)
)
if mibBuilder.loadTexts:
    acs.setRevisions(
        ("2021-04-19 00:00",
         "2020-10-01 00:00",
         "2020-07-01 00:00",
         "2019-06-01 00:00",
         "2018-05-01 00:00",
         "2017-11-17 00:00",
         "2016-06-17 00:00",
         "2016-01-06 00:00",
         "2010-10-10 00:00",
         "2007-09-17 00:00")
    )


# Types definitions



class PowerSupplyState(Integer32):
    """Custom type PowerSupplyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              9999)
        )
    )
    namedValues = NamedValues(
        *(("statePowerOn", 1),
          ("statePowerOff", 2),
          ("powerNotInstaled", 9999))
    )





class SerialPortSpeed(Integer32):
    """Custom type SerialPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(300,
              600,
              1200,
              2400,
              4800,
              9600,
              19200,
              38400,
              57600,
              115200,
              230400,
              460800)
        )
    )
    namedValues = NamedValues(
        *(("speed300bps", 300),
          ("speed600bps", 600),
          ("speed1200bps", 1200),
          ("speed2400bps", 2400),
          ("speed4800bps", 4800),
          ("speed9600bps", 9600),
          ("speed19200bps", 19200),
          ("speed38400bps", 38400),
          ("speed57600bps", 57600),
          ("speed115200bps", 115200),
          ("speed230400bps", 230400),
          ("speed460800bps", 460800))
    )





class SerialPortSignalState(Integer32):
    """Custom type SerialPortSignalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )





class SerialPortPinOut(Integer32):
    """Custom type SerialPortPinOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cyclades", 1),
          ("cisco", 2),
          ("rs422", 3),
          ("rs485", 4),
          ("auto", 5))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcsProducts_ObjectIdentity = ObjectIdentity
acsProducts = _AcsProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 26, 1)
)
_Acs8048_ObjectIdentity = ObjectIdentity
acs8048 = _Acs8048_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 26, 1, 1)
)
_Acs8032_ObjectIdentity = ObjectIdentity
acs8032 = _Acs8032_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 26, 1, 2)
)
_Acs8016_ObjectIdentity = ObjectIdentity
acs8016 = _Acs8016_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 26, 1, 3)
)
_Acs8008_ObjectIdentity = ObjectIdentity
acs8008 = _Acs8008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 26, 1, 4)
)
_Acs808_ObjectIdentity = ObjectIdentity
acs808 = _Acs808_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 26, 1, 5)
)
_Acs804_ObjectIdentity = ObjectIdentity
acs804 = _Acs804_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 26, 1, 6)
)
_Acs802_ObjectIdentity = ObjectIdentity
acs802 = _Acs802_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 26, 1, 7)
)
_AcsManagement_ObjectIdentity = ObjectIdentity
acsManagement = _AcsManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2)
)
_AcsAppliance_ObjectIdentity = ObjectIdentity
acsAppliance = _AcsAppliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 1)
)


class _AcsHostName_Type(DisplayString):
    """Custom type acsHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcsHostName_Type.__name__ = "DisplayString"
_AcsHostName_Object = MibScalar
acsHostName = _AcsHostName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 1, 1),
    _AcsHostName_Type()
)
acsHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsHostName.setStatus("current")


class _AcsProductModel_Type(DisplayString):
    """Custom type acsProductModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_AcsProductModel_Type.__name__ = "DisplayString"
_AcsProductModel_Object = MibScalar
acsProductModel = _AcsProductModel_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 1, 2),
    _AcsProductModel_Type()
)
acsProductModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsProductModel.setStatus("current")


class _AcsPartNumber_Type(DisplayString):
    """Custom type acsPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcsPartNumber_Type.__name__ = "DisplayString"
_AcsPartNumber_Object = MibScalar
acsPartNumber = _AcsPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 1, 3),
    _AcsPartNumber_Type()
)
acsPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPartNumber.setStatus("current")


class _AcsSerialNumber_Type(DisplayString):
    """Custom type acsSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcsSerialNumber_Type.__name__ = "DisplayString"
_AcsSerialNumber_Object = MibScalar
acsSerialNumber = _AcsSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 1, 4),
    _AcsSerialNumber_Type()
)
acsSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialNumber.setStatus("current")


class _AcsEIDNumber_Type(DisplayString):
    """Custom type acsEIDNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcsEIDNumber_Type.__name__ = "DisplayString"
_AcsEIDNumber_Object = MibScalar
acsEIDNumber = _AcsEIDNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 1, 5),
    _AcsEIDNumber_Type()
)
acsEIDNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsEIDNumber.setStatus("current")


class _AcsBootcodeVersion_Type(DisplayString):
    """Custom type acsBootcodeVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcsBootcodeVersion_Type.__name__ = "DisplayString"
_AcsBootcodeVersion_Object = MibScalar
acsBootcodeVersion = _AcsBootcodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 1, 6),
    _AcsBootcodeVersion_Type()
)
acsBootcodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsBootcodeVersion.setStatus("current")


class _AcsFirmwareVersion_Type(DisplayString):
    """Custom type acsFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcsFirmwareVersion_Type.__name__ = "DisplayString"
_AcsFirmwareVersion_Object = MibScalar
acsFirmwareVersion = _AcsFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 1, 7),
    _AcsFirmwareVersion_Type()
)
acsFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsFirmwareVersion.setStatus("current")
_AcsPowerSupply_ObjectIdentity = ObjectIdentity
acsPowerSupply = _AcsPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 1, 8)
)
if mibBuilder.loadTexts:
    acsPowerSupply.setStatus("current")
_AcsPowerSupplyNumber_Type = Integer32
_AcsPowerSupplyNumber_Object = MibScalar
acsPowerSupplyNumber = _AcsPowerSupplyNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 1, 8, 1),
    _AcsPowerSupplyNumber_Type()
)
acsPowerSupplyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerSupplyNumber.setStatus("current")
_AcsPowerSupplyStatePw1_Type = PowerSupplyState
_AcsPowerSupplyStatePw1_Object = MibScalar
acsPowerSupplyStatePw1 = _AcsPowerSupplyStatePw1_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 1, 8, 2),
    _AcsPowerSupplyStatePw1_Type()
)
acsPowerSupplyStatePw1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerSupplyStatePw1.setStatus("current")
_AcsPowerSupplyStatePw2_Type = PowerSupplyState
_AcsPowerSupplyStatePw2_Object = MibScalar
acsPowerSupplyStatePw2 = _AcsPowerSupplyStatePw2_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 1, 8, 3),
    _AcsPowerSupplyStatePw2_Type()
)
acsPowerSupplyStatePw2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerSupplyStatePw2.setStatus("current")


class _AcsReboot_Type(Integer32):
    """Custom type acsReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("reboot", 2))
    )


_AcsReboot_Type.__name__ = "Integer32"
_AcsReboot_Object = MibScalar
acsReboot = _AcsReboot_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 1, 9),
    _AcsReboot_Type()
)
acsReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsReboot.setStatus("current")
_AcsScheduledTasksTable_Object = MibTable
acsScheduledTasksTable = _AcsScheduledTasksTable_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 1, 10)
)
if mibBuilder.loadTexts:
    acsScheduledTasksTable.setStatus("current")
_AcsScheduledTasksTableEntry_Object = MibTableRow
acsScheduledTasksTableEntry = _AcsScheduledTasksTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 1, 10, 1)
)
acsScheduledTasksTableEntry.setIndexNames(
    (0, "ACS8000-MIB", "acsScheduledTasksTableIndex"),
)
if mibBuilder.loadTexts:
    acsScheduledTasksTableEntry.setStatus("current")
_AcsScheduledTasksTableIndex_Type = InterfaceIndexOrZero
_AcsScheduledTasksTableIndex_Object = MibTableColumn
acsScheduledTasksTableIndex = _AcsScheduledTasksTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 1, 10, 1, 1),
    _AcsScheduledTasksTableIndex_Type()
)
acsScheduledTasksTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsScheduledTasksTableIndex.setStatus("current")


class _AcsScheduledTasksTableType_Type(Integer32):
    """Custom type acsScheduledTasksTableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("custom", 1),
          ("cell-modem-ip-test", 2),
          ("cell-modem-signal-check", 3),
          ("save-config-cli", 4))
    )


_AcsScheduledTasksTableType_Type.__name__ = "Integer32"
_AcsScheduledTasksTableType_Object = MibTableColumn
acsScheduledTasksTableType = _AcsScheduledTasksTableType_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 1, 10, 1, 2),
    _AcsScheduledTasksTableType_Type()
)
acsScheduledTasksTableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsScheduledTasksTableType.setStatus("current")


class _AcsScheduledTasksTableName_Type(DisplayString):
    """Custom type acsScheduledTasksTableName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcsScheduledTasksTableName_Type.__name__ = "DisplayString"
_AcsScheduledTasksTableName_Object = MibTableColumn
acsScheduledTasksTableName = _AcsScheduledTasksTableName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 1, 10, 1, 3),
    _AcsScheduledTasksTableName_Type()
)
acsScheduledTasksTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsScheduledTasksTableName.setStatus("current")


class _AcsScheduledTasksTableStatus_Type(Integer32):
    """Custom type acsScheduledTasksTableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AcsScheduledTasksTableStatus_Type.__name__ = "Integer32"
_AcsScheduledTasksTableStatus_Object = MibTableColumn
acsScheduledTasksTableStatus = _AcsScheduledTasksTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 1, 10, 1, 4),
    _AcsScheduledTasksTableStatus_Type()
)
acsScheduledTasksTableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsScheduledTasksTableStatus.setStatus("current")


class _AcsScheduledTasksTableFrequency_Type(Integer32):
    """Custom type acsScheduledTasksTableFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("hourly", 1),
          ("daily", 2),
          ("weekly", 3),
          ("monthly", 4))
    )


_AcsScheduledTasksTableFrequency_Type.__name__ = "Integer32"
_AcsScheduledTasksTableFrequency_Object = MibTableColumn
acsScheduledTasksTableFrequency = _AcsScheduledTasksTableFrequency_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 1, 10, 1, 5),
    _AcsScheduledTasksTableFrequency_Type()
)
acsScheduledTasksTableFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsScheduledTasksTableFrequency.setStatus("current")


class _AcsScheduledTasksTableDay_Type(Integer32):
    """Custom type acsScheduledTasksTableDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("sunday", 1),
          ("monday", 2),
          ("tuesday", 3),
          ("wednesday", 4),
          ("thursday", 5),
          ("friday", 6),
          ("saturday", 7))
    )


_AcsScheduledTasksTableDay_Type.__name__ = "Integer32"
_AcsScheduledTasksTableDay_Object = MibTableColumn
acsScheduledTasksTableDay = _AcsScheduledTasksTableDay_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 1, 10, 1, 6),
    _AcsScheduledTasksTableDay_Type()
)
acsScheduledTasksTableDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsScheduledTasksTableDay.setStatus("current")
_AcsScheduledTasksTableDate_Type = Integer32
_AcsScheduledTasksTableDate_Object = MibTableColumn
acsScheduledTasksTableDate = _AcsScheduledTasksTableDate_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 1, 10, 1, 7),
    _AcsScheduledTasksTableDate_Type()
)
acsScheduledTasksTableDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsScheduledTasksTableDate.setStatus("current")


class _AcsScheduledTasksTableTime_Type(DisplayString):
    """Custom type acsScheduledTasksTableTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcsScheduledTasksTableTime_Type.__name__ = "DisplayString"
_AcsScheduledTasksTableTime_Object = MibTableColumn
acsScheduledTasksTableTime = _AcsScheduledTasksTableTime_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 1, 10, 1, 8),
    _AcsScheduledTasksTableTime_Type()
)
acsScheduledTasksTableTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsScheduledTasksTableTime.setStatus("current")


class _AcsScheduledTasksTableLastStarted_Type(DisplayString):
    """Custom type acsScheduledTasksTableLastStarted based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcsScheduledTasksTableLastStarted_Type.__name__ = "DisplayString"
_AcsScheduledTasksTableLastStarted_Object = MibTableColumn
acsScheduledTasksTableLastStarted = _AcsScheduledTasksTableLastStarted_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 1, 10, 1, 9),
    _AcsScheduledTasksTableLastStarted_Type()
)
acsScheduledTasksTableLastStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsScheduledTasksTableLastStarted.setStatus("current")


class _AcsScheduledTasksTableLastResult_Type(DisplayString):
    """Custom type acsScheduledTasksTableLastResult based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_AcsScheduledTasksTableLastResult_Type.__name__ = "DisplayString"
_AcsScheduledTasksTableLastResult_Object = MibTableColumn
acsScheduledTasksTableLastResult = _AcsScheduledTasksTableLastResult_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 1, 10, 1, 10),
    _AcsScheduledTasksTableLastResult_Type()
)
acsScheduledTasksTableLastResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsScheduledTasksTableLastResult.setStatus("current")


class _AcsScheduledTasksTableScript_Type(DisplayString):
    """Custom type acsScheduledTasksTableScript based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AcsScheduledTasksTableScript_Type.__name__ = "DisplayString"
_AcsScheduledTasksTableScript_Object = MibTableColumn
acsScheduledTasksTableScript = _AcsScheduledTasksTableScript_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 1, 10, 1, 11),
    _AcsScheduledTasksTableScript_Type()
)
acsScheduledTasksTableScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsScheduledTasksTableScript.setStatus("current")


class _AcsScheduledTasksTableIpAddress_Type(DisplayString):
    """Custom type acsScheduledTasksTableIpAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcsScheduledTasksTableIpAddress_Type.__name__ = "DisplayString"
_AcsScheduledTasksTableIpAddress_Object = MibTableColumn
acsScheduledTasksTableIpAddress = _AcsScheduledTasksTableIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 1, 10, 1, 12),
    _AcsScheduledTasksTableIpAddress_Type()
)
acsScheduledTasksTableIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsScheduledTasksTableIpAddress.setStatus("current")
_AcsSessions_ObjectIdentity = ObjectIdentity
acsSessions = _AcsSessions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 2)
)
_AcsActiveSessionsNumberOfSession_Type = Integer32
_AcsActiveSessionsNumberOfSession_Object = MibScalar
acsActiveSessionsNumberOfSession = _AcsActiveSessionsNumberOfSession_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 2, 1),
    _AcsActiveSessionsNumberOfSession_Type()
)
acsActiveSessionsNumberOfSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsActiveSessionsNumberOfSession.setStatus("current")
_AcsActiveSessionsTable_Object = MibTable
acsActiveSessionsTable = _AcsActiveSessionsTable_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 2, 2)
)
if mibBuilder.loadTexts:
    acsActiveSessionsTable.setStatus("current")
_AcsActiveSessionsTableEntry_Object = MibTableRow
acsActiveSessionsTableEntry = _AcsActiveSessionsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 2, 2, 1)
)
acsActiveSessionsTableEntry.setIndexNames(
    (0, "ACS8000-MIB", "acsActiveSessionsTableIndex"),
)
if mibBuilder.loadTexts:
    acsActiveSessionsTableEntry.setStatus("current")
_AcsActiveSessionsTableIndex_Type = InterfaceIndexOrZero
_AcsActiveSessionsTableIndex_Object = MibTableColumn
acsActiveSessionsTableIndex = _AcsActiveSessionsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 2, 2, 1, 1),
    _AcsActiveSessionsTableIndex_Type()
)
acsActiveSessionsTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsActiveSessionsTableIndex.setStatus("current")


class _AcsActiveSessionsTableUser_Type(DisplayString):
    """Custom type acsActiveSessionsTableUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcsActiveSessionsTableUser_Type.__name__ = "DisplayString"
_AcsActiveSessionsTableUser_Object = MibTableColumn
acsActiveSessionsTableUser = _AcsActiveSessionsTableUser_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 2, 2, 1, 2),
    _AcsActiveSessionsTableUser_Type()
)
acsActiveSessionsTableUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsActiveSessionsTableUser.setStatus("current")


class _AcsActiveSessionsTableGroup_Type(DisplayString):
    """Custom type acsActiveSessionsTableGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcsActiveSessionsTableGroup_Type.__name__ = "DisplayString"
_AcsActiveSessionsTableGroup_Object = MibTableColumn
acsActiveSessionsTableGroup = _AcsActiveSessionsTableGroup_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 2, 2, 1, 3),
    _AcsActiveSessionsTableGroup_Type()
)
acsActiveSessionsTableGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsActiveSessionsTableGroup.setStatus("current")


class _AcsActiveSessionsTableType_Type(DisplayString):
    """Custom type acsActiveSessionsTableType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcsActiveSessionsTableType_Type.__name__ = "DisplayString"
_AcsActiveSessionsTableType_Object = MibTableColumn
acsActiveSessionsTableType = _AcsActiveSessionsTableType_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 2, 2, 1, 4),
    _AcsActiveSessionsTableType_Type()
)
acsActiveSessionsTableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsActiveSessionsTableType.setStatus("current")


class _AcsActiveSessionsTableConnection_Type(DisplayString):
    """Custom type acsActiveSessionsTableConnection based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcsActiveSessionsTableConnection_Type.__name__ = "DisplayString"
_AcsActiveSessionsTableConnection_Object = MibTableColumn
acsActiveSessionsTableConnection = _AcsActiveSessionsTableConnection_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 2, 2, 1, 5),
    _AcsActiveSessionsTableConnection_Type()
)
acsActiveSessionsTableConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsActiveSessionsTableConnection.setStatus("current")


class _AcsActiveSessionsTableSessionTime_Type(DisplayString):
    """Custom type acsActiveSessionsTableSessionTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcsActiveSessionsTableSessionTime_Type.__name__ = "DisplayString"
_AcsActiveSessionsTableSessionTime_Object = MibTableColumn
acsActiveSessionsTableSessionTime = _AcsActiveSessionsTableSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 2, 2, 1, 6),
    _AcsActiveSessionsTableSessionTime_Type()
)
acsActiveSessionsTableSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsActiveSessionsTableSessionTime.setStatus("current")


class _AcsActiveSessionsTableFrom_Type(DisplayString):
    """Custom type acsActiveSessionsTableFrom based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcsActiveSessionsTableFrom_Type.__name__ = "DisplayString"
_AcsActiveSessionsTableFrom_Object = MibTableColumn
acsActiveSessionsTableFrom = _AcsActiveSessionsTableFrom_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 2, 2, 1, 7),
    _AcsActiveSessionsTableFrom_Type()
)
acsActiveSessionsTableFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsActiveSessionsTableFrom.setStatus("current")


class _AcsActiveSessionsTableKill_Type(Integer32):
    """Custom type acsActiveSessionsTableKill based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("killSession", 2))
    )


_AcsActiveSessionsTableKill_Type.__name__ = "Integer32"
_AcsActiveSessionsTableKill_Object = MibTableColumn
acsActiveSessionsTableKill = _AcsActiveSessionsTableKill_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 2, 2, 1, 8),
    _AcsActiveSessionsTableKill_Type()
)
acsActiveSessionsTableKill.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsActiveSessionsTableKill.setStatus("current")
_AcsSerialPort_ObjectIdentity = ObjectIdentity
acsSerialPort = _AcsSerialPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 3)
)
_AcsSerialPortNumberOfPorts_Type = Integer32
_AcsSerialPortNumberOfPorts_Object = MibScalar
acsSerialPortNumberOfPorts = _AcsSerialPortNumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 3, 1),
    _AcsSerialPortNumberOfPorts_Type()
)
acsSerialPortNumberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortNumberOfPorts.setStatus("current")
_AcsSerialPortTable_Object = MibTable
acsSerialPortTable = _AcsSerialPortTable_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 3, 2)
)
if mibBuilder.loadTexts:
    acsSerialPortTable.setStatus("current")
_AcsSerialPortTableEntry_Object = MibTableRow
acsSerialPortTableEntry = _AcsSerialPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 3, 2, 1)
)
acsSerialPortTableEntry.setIndexNames(
    (0, "ACS8000-MIB", "acsSerialPortTableNumber"),
)
if mibBuilder.loadTexts:
    acsSerialPortTableEntry.setStatus("current")


class _AcsSerialPortTableNumber_Type(Integer32):
    """Custom type acsSerialPortTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 49),
    )


_AcsSerialPortTableNumber_Type.__name__ = "Integer32"
_AcsSerialPortTableNumber_Object = MibTableColumn
acsSerialPortTableNumber = _AcsSerialPortTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 3, 2, 1, 1),
    _AcsSerialPortTableNumber_Type()
)
acsSerialPortTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTableNumber.setStatus("current")


class _AcsSerialPortTableDeviceName_Type(DisplayString):
    """Custom type acsSerialPortTableDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_AcsSerialPortTableDeviceName_Type.__name__ = "DisplayString"
_AcsSerialPortTableDeviceName_Object = MibTableColumn
acsSerialPortTableDeviceName = _AcsSerialPortTableDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 3, 2, 1, 2),
    _AcsSerialPortTableDeviceName_Type()
)
acsSerialPortTableDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTableDeviceName.setStatus("current")


class _AcsSerialPortTableStatus_Type(Integer32):
    """Custom type acsSerialPortTableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("idle", 2),
          ("inUse", 3))
    )


_AcsSerialPortTableStatus_Type.__name__ = "Integer32"
_AcsSerialPortTableStatus_Object = MibTableColumn
acsSerialPortTableStatus = _AcsSerialPortTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 3, 2, 1, 3),
    _AcsSerialPortTableStatus_Type()
)
acsSerialPortTableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTableStatus.setStatus("current")


class _AcsSerialPortTableName_Type(DisplayString):
    """Custom type acsSerialPortTableName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_AcsSerialPortTableName_Type.__name__ = "DisplayString"
_AcsSerialPortTableName_Object = MibTableColumn
acsSerialPortTableName = _AcsSerialPortTableName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 3, 2, 1, 4),
    _AcsSerialPortTableName_Type()
)
acsSerialPortTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTableName.setStatus("current")


class _AcsSerialPortTableProfile_Type(Integer32):
    """Custom type acsSerialPortTableProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("casProfile", 1),
          ("tsProfile", 2),
          ("dialInProfile", 3),
          ("powerProfile", 4))
    )


_AcsSerialPortTableProfile_Type.__name__ = "Integer32"
_AcsSerialPortTableProfile_Object = MibTableColumn
acsSerialPortTableProfile = _AcsSerialPortTableProfile_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 3, 2, 1, 5),
    _AcsSerialPortTableProfile_Type()
)
acsSerialPortTableProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTableProfile.setStatus("current")
_AcsSerialPortTablePinOut_Type = SerialPortPinOut
_AcsSerialPortTablePinOut_Object = MibTableColumn
acsSerialPortTablePinOut = _AcsSerialPortTablePinOut_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 3, 2, 1, 6),
    _AcsSerialPortTablePinOut_Type()
)
acsSerialPortTablePinOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTablePinOut.setStatus("current")
_AcsSerialPortTableComSpeed_Type = SerialPortSpeed
_AcsSerialPortTableComSpeed_Object = MibTableColumn
acsSerialPortTableComSpeed = _AcsSerialPortTableComSpeed_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 3, 2, 1, 7),
    _AcsSerialPortTableComSpeed_Type()
)
acsSerialPortTableComSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTableComSpeed.setStatus("current")


class _AcsSerialPortTableComParity_Type(Integer32):
    """Custom type acsSerialPortTableComParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("odd", 2),
          ("even", 3))
    )


_AcsSerialPortTableComParity_Type.__name__ = "Integer32"
_AcsSerialPortTableComParity_Object = MibTableColumn
acsSerialPortTableComParity = _AcsSerialPortTableComParity_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 3, 2, 1, 8),
    _AcsSerialPortTableComParity_Type()
)
acsSerialPortTableComParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTableComParity.setStatus("current")
_AcsSerialPortTableComDataSize_Type = Integer32
_AcsSerialPortTableComDataSize_Object = MibTableColumn
acsSerialPortTableComDataSize = _AcsSerialPortTableComDataSize_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 3, 2, 1, 9),
    _AcsSerialPortTableComDataSize_Type()
)
acsSerialPortTableComDataSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTableComDataSize.setStatus("current")
_AcsSerialPortTableComStopBits_Type = Integer32
_AcsSerialPortTableComStopBits_Object = MibTableColumn
acsSerialPortTableComStopBits = _AcsSerialPortTableComStopBits_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 3, 2, 1, 10),
    _AcsSerialPortTableComStopBits_Type()
)
acsSerialPortTableComStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTableComStopBits.setStatus("current")


class _AcsSerialPortTableComFlowControl_Type(Integer32):
    """Custom type acsSerialPortTableComFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("hardware", 2),
          ("software", 3))
    )


_AcsSerialPortTableComFlowControl_Type.__name__ = "Integer32"
_AcsSerialPortTableComFlowControl_Object = MibTableColumn
acsSerialPortTableComFlowControl = _AcsSerialPortTableComFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 3, 2, 1, 11),
    _AcsSerialPortTableComFlowControl_Type()
)
acsSerialPortTableComFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTableComFlowControl.setStatus("current")
_AcsSerialPortTableSignalStateDTR_Type = SerialPortSignalState
_AcsSerialPortTableSignalStateDTR_Object = MibTableColumn
acsSerialPortTableSignalStateDTR = _AcsSerialPortTableSignalStateDTR_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 3, 2, 1, 12),
    _AcsSerialPortTableSignalStateDTR_Type()
)
acsSerialPortTableSignalStateDTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTableSignalStateDTR.setStatus("current")
_AcsSerialPortTableSignalStateDCD_Type = SerialPortSignalState
_AcsSerialPortTableSignalStateDCD_Object = MibTableColumn
acsSerialPortTableSignalStateDCD = _AcsSerialPortTableSignalStateDCD_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 3, 2, 1, 13),
    _AcsSerialPortTableSignalStateDCD_Type()
)
acsSerialPortTableSignalStateDCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTableSignalStateDCD.setStatus("current")
_AcsSerialPortTableSignalStateRTS_Type = SerialPortSignalState
_AcsSerialPortTableSignalStateRTS_Object = MibTableColumn
acsSerialPortTableSignalStateRTS = _AcsSerialPortTableSignalStateRTS_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 3, 2, 1, 14),
    _AcsSerialPortTableSignalStateRTS_Type()
)
acsSerialPortTableSignalStateRTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTableSignalStateRTS.setStatus("current")
_AcsSerialPortTableSignalStateCTS_Type = SerialPortSignalState
_AcsSerialPortTableSignalStateCTS_Object = MibTableColumn
acsSerialPortTableSignalStateCTS = _AcsSerialPortTableSignalStateCTS_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 3, 2, 1, 15),
    _AcsSerialPortTableSignalStateCTS_Type()
)
acsSerialPortTableSignalStateCTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTableSignalStateCTS.setStatus("current")
_AcsSerialPortTableTxBytes_Type = Integer32
_AcsSerialPortTableTxBytes_Object = MibTableColumn
acsSerialPortTableTxBytes = _AcsSerialPortTableTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 3, 2, 1, 16),
    _AcsSerialPortTableTxBytes_Type()
)
acsSerialPortTableTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTableTxBytes.setStatus("current")
_AcsSerialPortTableRxBytes_Type = Integer32
_AcsSerialPortTableRxBytes_Object = MibTableColumn
acsSerialPortTableRxBytes = _AcsSerialPortTableRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 3, 2, 1, 17),
    _AcsSerialPortTableRxBytes_Type()
)
acsSerialPortTableRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTableRxBytes.setStatus("current")
_AcsSerialPortTableFrameError_Type = Integer32
_AcsSerialPortTableFrameError_Object = MibTableColumn
acsSerialPortTableFrameError = _AcsSerialPortTableFrameError_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 3, 2, 1, 18),
    _AcsSerialPortTableFrameError_Type()
)
acsSerialPortTableFrameError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTableFrameError.setStatus("current")
_AcsSerialPortTableParityError_Type = Integer32
_AcsSerialPortTableParityError_Object = MibTableColumn
acsSerialPortTableParityError = _AcsSerialPortTableParityError_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 3, 2, 1, 19),
    _AcsSerialPortTableParityError_Type()
)
acsSerialPortTableParityError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTableParityError.setStatus("current")
_AcsSerialPortTableBreak_Type = Integer32
_AcsSerialPortTableBreak_Object = MibTableColumn
acsSerialPortTableBreak = _AcsSerialPortTableBreak_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 3, 2, 1, 20),
    _AcsSerialPortTableBreak_Type()
)
acsSerialPortTableBreak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTableBreak.setStatus("current")
_AcsSerialPortTableOverrun_Type = Integer32
_AcsSerialPortTableOverrun_Object = MibTableColumn
acsSerialPortTableOverrun = _AcsSerialPortTableOverrun_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 3, 2, 1, 21),
    _AcsSerialPortTableOverrun_Type()
)
acsSerialPortTableOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTableOverrun.setStatus("current")


class _AcsSerialPortTableResetCounters_Type(Integer32):
    """Custom type acsSerialPortTableResetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-action", 1),
          ("resetCounters", 2))
    )


_AcsSerialPortTableResetCounters_Type.__name__ = "Integer32"
_AcsSerialPortTableResetCounters_Object = MibTableColumn
acsSerialPortTableResetCounters = _AcsSerialPortTableResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 3, 2, 1, 22),
    _AcsSerialPortTableResetCounters_Type()
)
acsSerialPortTableResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsSerialPortTableResetCounters.setStatus("current")
_AcsSerialPortTableXcvrStatus_Type = SerialPortSignalState
_AcsSerialPortTableXcvrStatus_Object = MibTableColumn
acsSerialPortTableXcvrStatus = _AcsSerialPortTableXcvrStatus_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 3, 2, 1, 23),
    _AcsSerialPortTableXcvrStatus_Type()
)
acsSerialPortTableXcvrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTableXcvrStatus.setStatus("current")
_AcsPowerMgmt_ObjectIdentity = ObjectIdentity
acsPowerMgmt = _AcsPowerMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5)
)
_AcsPowerMgmtNumSerialPorts_Type = Integer32
_AcsPowerMgmtNumSerialPorts_Object = MibScalar
acsPowerMgmtNumSerialPorts = _AcsPowerMgmtNumSerialPorts_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 1),
    _AcsPowerMgmtNumSerialPorts_Type()
)
acsPowerMgmtNumSerialPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtNumSerialPorts.setStatus("current")
_AcsPowerMgmtSerialTable_Object = MibTable
acsPowerMgmtSerialTable = _AcsPowerMgmtSerialTable_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 2)
)
if mibBuilder.loadTexts:
    acsPowerMgmtSerialTable.setStatus("current")
_AcsPowerMgmtSerialTableEntry_Object = MibTableRow
acsPowerMgmtSerialTableEntry = _AcsPowerMgmtSerialTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 2, 1)
)
acsPowerMgmtSerialTableEntry.setIndexNames(
    (0, "ACS8000-MIB", "acsPowerMgmtSerialTableIndex"),
)
if mibBuilder.loadTexts:
    acsPowerMgmtSerialTableEntry.setStatus("current")
_AcsPowerMgmtSerialTableIndex_Type = InterfaceIndex
_AcsPowerMgmtSerialTableIndex_Object = MibTableColumn
acsPowerMgmtSerialTableIndex = _AcsPowerMgmtSerialTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 2, 1, 1),
    _AcsPowerMgmtSerialTableIndex_Type()
)
acsPowerMgmtSerialTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtSerialTableIndex.setStatus("current")
_AcsPowerMgmtSerialTablePortNumber_Type = Integer32
_AcsPowerMgmtSerialTablePortNumber_Object = MibTableColumn
acsPowerMgmtSerialTablePortNumber = _AcsPowerMgmtSerialTablePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 2, 1, 2),
    _AcsPowerMgmtSerialTablePortNumber_Type()
)
acsPowerMgmtSerialTablePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtSerialTablePortNumber.setStatus("current")
_AcsPowerMgmtSerialTableDeviceName_Type = DisplayString
_AcsPowerMgmtSerialTableDeviceName_Object = MibTableColumn
acsPowerMgmtSerialTableDeviceName = _AcsPowerMgmtSerialTableDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 2, 1, 3),
    _AcsPowerMgmtSerialTableDeviceName_Type()
)
acsPowerMgmtSerialTableDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtSerialTableDeviceName.setStatus("current")
_AcsPowerMgmtSerialTableNumberPDUs_Type = Integer32
_AcsPowerMgmtSerialTableNumberPDUs_Object = MibTableColumn
acsPowerMgmtSerialTableNumberPDUs = _AcsPowerMgmtSerialTableNumberPDUs_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 2, 1, 4),
    _AcsPowerMgmtSerialTableNumberPDUs_Type()
)
acsPowerMgmtSerialTableNumberPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtSerialTableNumberPDUs.setStatus("current")
_AcsPowerMgmtSerialTableNumberUPS_Type = Integer32
_AcsPowerMgmtSerialTableNumberUPS_Object = MibTableColumn
acsPowerMgmtSerialTableNumberUPS = _AcsPowerMgmtSerialTableNumberUPS_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 2, 1, 5),
    _AcsPowerMgmtSerialTableNumberUPS_Type()
)
acsPowerMgmtSerialTableNumberUPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtSerialTableNumberUPS.setStatus("current")
_AcsPowerMgmtPDUTable_Object = MibTable
acsPowerMgmtPDUTable = _AcsPowerMgmtPDUTable_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3)
)
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTable.setStatus("current")
_AcsPowerMgmtPDUTableEntry_Object = MibTableRow
acsPowerMgmtPDUTableEntry = _AcsPowerMgmtPDUTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1)
)
acsPowerMgmtPDUTableEntry.setIndexNames(
    (0, "ACS8000-MIB", "acsPowerMgmtPDUTablePortNumber"),
    (0, "ACS8000-MIB", "acsPowerMgmtPDUTablePduIndex"),
)
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableEntry.setStatus("current")
_AcsPowerMgmtPDUTablePortNumber_Type = InterfaceIndex
_AcsPowerMgmtPDUTablePortNumber_Object = MibTableColumn
acsPowerMgmtPDUTablePortNumber = _AcsPowerMgmtPDUTablePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 1),
    _AcsPowerMgmtPDUTablePortNumber_Type()
)
acsPowerMgmtPDUTablePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTablePortNumber.setStatus("current")
_AcsPowerMgmtPDUTablePduIndex_Type = InterfaceIndexOrZero
_AcsPowerMgmtPDUTablePduIndex_Object = MibTableColumn
acsPowerMgmtPDUTablePduIndex = _AcsPowerMgmtPDUTablePduIndex_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 2),
    _AcsPowerMgmtPDUTablePduIndex_Type()
)
acsPowerMgmtPDUTablePduIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTablePduIndex.setStatus("current")
_AcsPowerMgmtPDUTablePduId_Type = DisplayString
_AcsPowerMgmtPDUTablePduId_Object = MibTableColumn
acsPowerMgmtPDUTablePduId = _AcsPowerMgmtPDUTablePduId_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 3),
    _AcsPowerMgmtPDUTablePduId_Type()
)
acsPowerMgmtPDUTablePduId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTablePduId.setStatus("current")
_AcsPowerMgmtPDUTablePortName_Type = DisplayString
_AcsPowerMgmtPDUTablePortName_Object = MibTableColumn
acsPowerMgmtPDUTablePortName = _AcsPowerMgmtPDUTablePortName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 4),
    _AcsPowerMgmtPDUTablePortName_Type()
)
acsPowerMgmtPDUTablePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTablePortName.setStatus("current")
_AcsPowerMgmtPDUTableModel_Type = DisplayString
_AcsPowerMgmtPDUTableModel_Object = MibTableColumn
acsPowerMgmtPDUTableModel = _AcsPowerMgmtPDUTableModel_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 5),
    _AcsPowerMgmtPDUTableModel_Type()
)
acsPowerMgmtPDUTableModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableModel.setStatus("current")
_AcsPowerMgmtPDUTableVendor_Type = DisplayString
_AcsPowerMgmtPDUTableVendor_Object = MibTableColumn
acsPowerMgmtPDUTableVendor = _AcsPowerMgmtPDUTableVendor_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 6),
    _AcsPowerMgmtPDUTableVendor_Type()
)
acsPowerMgmtPDUTableVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableVendor.setStatus("current")
_AcsPowerMgmtPDUTableFirmwareVersion_Type = DisplayString
_AcsPowerMgmtPDUTableFirmwareVersion_Object = MibTableColumn
acsPowerMgmtPDUTableFirmwareVersion = _AcsPowerMgmtPDUTableFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 7),
    _AcsPowerMgmtPDUTableFirmwareVersion_Type()
)
acsPowerMgmtPDUTableFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableFirmwareVersion.setStatus("current")
_AcsPowerMgmtPDUTableNumberOfOutlets_Type = Integer32
_AcsPowerMgmtPDUTableNumberOfOutlets_Object = MibTableColumn
acsPowerMgmtPDUTableNumberOfOutlets = _AcsPowerMgmtPDUTableNumberOfOutlets_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 8),
    _AcsPowerMgmtPDUTableNumberOfOutlets_Type()
)
acsPowerMgmtPDUTableNumberOfOutlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableNumberOfOutlets.setStatus("current")
_AcsPowerMgmtPDUTableCurrentNOS_Type = Integer32
_AcsPowerMgmtPDUTableCurrentNOS_Object = MibTableColumn
acsPowerMgmtPDUTableCurrentNOS = _AcsPowerMgmtPDUTableCurrentNOS_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 9),
    _AcsPowerMgmtPDUTableCurrentNOS_Type()
)
acsPowerMgmtPDUTableCurrentNOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableCurrentNOS.setStatus("obsolete")
_AcsPowerMgmtPDUTableCurrent1Value_Type = Integer32
_AcsPowerMgmtPDUTableCurrent1Value_Object = MibTableColumn
acsPowerMgmtPDUTableCurrent1Value = _AcsPowerMgmtPDUTableCurrent1Value_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 10),
    _AcsPowerMgmtPDUTableCurrent1Value_Type()
)
acsPowerMgmtPDUTableCurrent1Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableCurrent1Value.setStatus("obsolete")
_AcsPowerMgmtPDUTableCurrent1Max_Type = Integer32
_AcsPowerMgmtPDUTableCurrent1Max_Object = MibTableColumn
acsPowerMgmtPDUTableCurrent1Max = _AcsPowerMgmtPDUTableCurrent1Max_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 11),
    _AcsPowerMgmtPDUTableCurrent1Max_Type()
)
acsPowerMgmtPDUTableCurrent1Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableCurrent1Max.setStatus("obsolete")
_AcsPowerMgmtPDUTableCurrent2Value_Type = Integer32
_AcsPowerMgmtPDUTableCurrent2Value_Object = MibTableColumn
acsPowerMgmtPDUTableCurrent2Value = _AcsPowerMgmtPDUTableCurrent2Value_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 12),
    _AcsPowerMgmtPDUTableCurrent2Value_Type()
)
acsPowerMgmtPDUTableCurrent2Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableCurrent2Value.setStatus("obsolete")
_AcsPowerMgmtPDUTableCurrent2Max_Type = Integer32
_AcsPowerMgmtPDUTableCurrent2Max_Object = MibTableColumn
acsPowerMgmtPDUTableCurrent2Max = _AcsPowerMgmtPDUTableCurrent2Max_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 13),
    _AcsPowerMgmtPDUTableCurrent2Max_Type()
)
acsPowerMgmtPDUTableCurrent2Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableCurrent2Max.setStatus("obsolete")
_AcsPowerMgmtPDUTableCurrent3Value_Type = Integer32
_AcsPowerMgmtPDUTableCurrent3Value_Object = MibTableColumn
acsPowerMgmtPDUTableCurrent3Value = _AcsPowerMgmtPDUTableCurrent3Value_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 14),
    _AcsPowerMgmtPDUTableCurrent3Value_Type()
)
acsPowerMgmtPDUTableCurrent3Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableCurrent3Value.setStatus("obsolete")
_AcsPowerMgmtPDUTableCurrent3Max_Type = Integer32
_AcsPowerMgmtPDUTableCurrent3Max_Object = MibTableColumn
acsPowerMgmtPDUTableCurrent3Max = _AcsPowerMgmtPDUTableCurrent3Max_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 15),
    _AcsPowerMgmtPDUTableCurrent3Max_Type()
)
acsPowerMgmtPDUTableCurrent3Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableCurrent3Max.setStatus("obsolete")
_AcsPowerMgmtPDUTableTemperatureNOS_Type = Integer32
_AcsPowerMgmtPDUTableTemperatureNOS_Object = MibTableColumn
acsPowerMgmtPDUTableTemperatureNOS = _AcsPowerMgmtPDUTableTemperatureNOS_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 16),
    _AcsPowerMgmtPDUTableTemperatureNOS_Type()
)
acsPowerMgmtPDUTableTemperatureNOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableTemperatureNOS.setStatus("obsolete")
_AcsPowerMgmtPDUTableTemperature1Value_Type = Integer32
_AcsPowerMgmtPDUTableTemperature1Value_Object = MibTableColumn
acsPowerMgmtPDUTableTemperature1Value = _AcsPowerMgmtPDUTableTemperature1Value_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 17),
    _AcsPowerMgmtPDUTableTemperature1Value_Type()
)
acsPowerMgmtPDUTableTemperature1Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableTemperature1Value.setStatus("obsolete")
_AcsPowerMgmtPDUTableTemperature1Max_Type = Integer32
_AcsPowerMgmtPDUTableTemperature1Max_Object = MibTableColumn
acsPowerMgmtPDUTableTemperature1Max = _AcsPowerMgmtPDUTableTemperature1Max_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 18),
    _AcsPowerMgmtPDUTableTemperature1Max_Type()
)
acsPowerMgmtPDUTableTemperature1Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableTemperature1Max.setStatus("obsolete")
_AcsPowerMgmtPDUTableTemperature2Value_Type = Integer32
_AcsPowerMgmtPDUTableTemperature2Value_Object = MibTableColumn
acsPowerMgmtPDUTableTemperature2Value = _AcsPowerMgmtPDUTableTemperature2Value_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 19),
    _AcsPowerMgmtPDUTableTemperature2Value_Type()
)
acsPowerMgmtPDUTableTemperature2Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableTemperature2Value.setStatus("obsolete")
_AcsPowerMgmtPDUTableTemperature2Max_Type = Integer32
_AcsPowerMgmtPDUTableTemperature2Max_Object = MibTableColumn
acsPowerMgmtPDUTableTemperature2Max = _AcsPowerMgmtPDUTableTemperature2Max_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 20),
    _AcsPowerMgmtPDUTableTemperature2Max_Type()
)
acsPowerMgmtPDUTableTemperature2Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableTemperature2Max.setStatus("obsolete")
_AcsPowerMgmtPDUTableTemperature3Value_Type = Integer32
_AcsPowerMgmtPDUTableTemperature3Value_Object = MibTableColumn
acsPowerMgmtPDUTableTemperature3Value = _AcsPowerMgmtPDUTableTemperature3Value_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 21),
    _AcsPowerMgmtPDUTableTemperature3Value_Type()
)
acsPowerMgmtPDUTableTemperature3Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableTemperature3Value.setStatus("obsolete")
_AcsPowerMgmtPDUTableTemperature3Max_Type = Integer32
_AcsPowerMgmtPDUTableTemperature3Max_Object = MibTableColumn
acsPowerMgmtPDUTableTemperature3Max = _AcsPowerMgmtPDUTableTemperature3Max_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 22),
    _AcsPowerMgmtPDUTableTemperature3Max_Type()
)
acsPowerMgmtPDUTableTemperature3Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableTemperature3Max.setStatus("obsolete")
_AcsPowerMgmtPDUTableHumidityNOS_Type = Integer32
_AcsPowerMgmtPDUTableHumidityNOS_Object = MibTableColumn
acsPowerMgmtPDUTableHumidityNOS = _AcsPowerMgmtPDUTableHumidityNOS_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 23),
    _AcsPowerMgmtPDUTableHumidityNOS_Type()
)
acsPowerMgmtPDUTableHumidityNOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableHumidityNOS.setStatus("obsolete")
_AcsPowerMgmtPDUTableHumidity1Value_Type = Integer32
_AcsPowerMgmtPDUTableHumidity1Value_Object = MibTableColumn
acsPowerMgmtPDUTableHumidity1Value = _AcsPowerMgmtPDUTableHumidity1Value_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 24),
    _AcsPowerMgmtPDUTableHumidity1Value_Type()
)
acsPowerMgmtPDUTableHumidity1Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableHumidity1Value.setStatus("obsolete")
_AcsPowerMgmtPDUTableHumidity1Max_Type = Integer32
_AcsPowerMgmtPDUTableHumidity1Max_Object = MibTableColumn
acsPowerMgmtPDUTableHumidity1Max = _AcsPowerMgmtPDUTableHumidity1Max_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 25),
    _AcsPowerMgmtPDUTableHumidity1Max_Type()
)
acsPowerMgmtPDUTableHumidity1Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableHumidity1Max.setStatus("obsolete")
_AcsPowerMgmtPDUTableHumidity2Value_Type = Integer32
_AcsPowerMgmtPDUTableHumidity2Value_Object = MibTableColumn
acsPowerMgmtPDUTableHumidity2Value = _AcsPowerMgmtPDUTableHumidity2Value_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 26),
    _AcsPowerMgmtPDUTableHumidity2Value_Type()
)
acsPowerMgmtPDUTableHumidity2Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableHumidity2Value.setStatus("obsolete")
_AcsPowerMgmtPDUTableHumidity2Max_Type = Integer32
_AcsPowerMgmtPDUTableHumidity2Max_Object = MibTableColumn
acsPowerMgmtPDUTableHumidity2Max = _AcsPowerMgmtPDUTableHumidity2Max_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 27),
    _AcsPowerMgmtPDUTableHumidity2Max_Type()
)
acsPowerMgmtPDUTableHumidity2Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableHumidity2Max.setStatus("obsolete")
_AcsPowerMgmtPDUTableHumidity3Value_Type = Integer32
_AcsPowerMgmtPDUTableHumidity3Value_Object = MibTableColumn
acsPowerMgmtPDUTableHumidity3Value = _AcsPowerMgmtPDUTableHumidity3Value_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 28),
    _AcsPowerMgmtPDUTableHumidity3Value_Type()
)
acsPowerMgmtPDUTableHumidity3Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableHumidity3Value.setStatus("obsolete")
_AcsPowerMgmtPDUTableHumidity3Max_Type = Integer32
_AcsPowerMgmtPDUTableHumidity3Max_Object = MibTableColumn
acsPowerMgmtPDUTableHumidity3Max = _AcsPowerMgmtPDUTableHumidity3Max_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 29),
    _AcsPowerMgmtPDUTableHumidity3Max_Type()
)
acsPowerMgmtPDUTableHumidity3Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableHumidity3Max.setStatus("obsolete")
_AcsPowerMgmtPDUTableVoltageNOS_Type = Integer32
_AcsPowerMgmtPDUTableVoltageNOS_Object = MibTableColumn
acsPowerMgmtPDUTableVoltageNOS = _AcsPowerMgmtPDUTableVoltageNOS_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 30),
    _AcsPowerMgmtPDUTableVoltageNOS_Type()
)
acsPowerMgmtPDUTableVoltageNOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableVoltageNOS.setStatus("obsolete")
_AcsPowerMgmtPDUTableVoltage1Value_Type = Integer32
_AcsPowerMgmtPDUTableVoltage1Value_Object = MibTableColumn
acsPowerMgmtPDUTableVoltage1Value = _AcsPowerMgmtPDUTableVoltage1Value_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 31),
    _AcsPowerMgmtPDUTableVoltage1Value_Type()
)
acsPowerMgmtPDUTableVoltage1Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableVoltage1Value.setStatus("obsolete")
_AcsPowerMgmtPDUTableVoltage1Max_Type = Integer32
_AcsPowerMgmtPDUTableVoltage1Max_Object = MibTableColumn
acsPowerMgmtPDUTableVoltage1Max = _AcsPowerMgmtPDUTableVoltage1Max_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 32),
    _AcsPowerMgmtPDUTableVoltage1Max_Type()
)
acsPowerMgmtPDUTableVoltage1Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableVoltage1Max.setStatus("obsolete")
_AcsPowerMgmtPDUTableVoltage2Value_Type = Integer32
_AcsPowerMgmtPDUTableVoltage2Value_Object = MibTableColumn
acsPowerMgmtPDUTableVoltage2Value = _AcsPowerMgmtPDUTableVoltage2Value_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 33),
    _AcsPowerMgmtPDUTableVoltage2Value_Type()
)
acsPowerMgmtPDUTableVoltage2Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableVoltage2Value.setStatus("obsolete")
_AcsPowerMgmtPDUTableVoltage2Max_Type = Integer32
_AcsPowerMgmtPDUTableVoltage2Max_Object = MibTableColumn
acsPowerMgmtPDUTableVoltage2Max = _AcsPowerMgmtPDUTableVoltage2Max_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 34),
    _AcsPowerMgmtPDUTableVoltage2Max_Type()
)
acsPowerMgmtPDUTableVoltage2Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableVoltage2Max.setStatus("obsolete")
_AcsPowerMgmtPDUTableVoltage3Value_Type = Integer32
_AcsPowerMgmtPDUTableVoltage3Value_Object = MibTableColumn
acsPowerMgmtPDUTableVoltage3Value = _AcsPowerMgmtPDUTableVoltage3Value_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 35),
    _AcsPowerMgmtPDUTableVoltage3Value_Type()
)
acsPowerMgmtPDUTableVoltage3Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableVoltage3Value.setStatus("obsolete")
_AcsPowerMgmtPDUTableVoltage3Max_Type = Integer32
_AcsPowerMgmtPDUTableVoltage3Max_Object = MibTableColumn
acsPowerMgmtPDUTableVoltage3Max = _AcsPowerMgmtPDUTableVoltage3Max_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 36),
    _AcsPowerMgmtPDUTableVoltage3Max_Type()
)
acsPowerMgmtPDUTableVoltage3Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableVoltage3Max.setStatus("obsolete")


class _AcsPowerMgmtPDUTableNumberOfPhases_Type(Integer32):
    """Custom type acsPowerMgmtPDUTableNumberOfPhases based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3)
        )
    )
    namedValues = NamedValues(
        *(("single-phase", 0),
          ("three-phase", 3))
    )


_AcsPowerMgmtPDUTableNumberOfPhases_Type.__name__ = "Integer32"
_AcsPowerMgmtPDUTableNumberOfPhases_Object = MibTableColumn
acsPowerMgmtPDUTableNumberOfPhases = _AcsPowerMgmtPDUTableNumberOfPhases_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 37),
    _AcsPowerMgmtPDUTableNumberOfPhases_Type()
)
acsPowerMgmtPDUTableNumberOfPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableNumberOfPhases.setStatus("current")
_AcsPowerMgmtPDUTableNumberOfBanks_Type = Integer32
_AcsPowerMgmtPDUTableNumberOfBanks_Object = MibTableColumn
acsPowerMgmtPDUTableNumberOfBanks = _AcsPowerMgmtPDUTableNumberOfBanks_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 38),
    _AcsPowerMgmtPDUTableNumberOfBanks_Type()
)
acsPowerMgmtPDUTableNumberOfBanks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableNumberOfBanks.setStatus("current")
_AcsPowerMgmtPDUTableCurrentValue_Type = Integer32
_AcsPowerMgmtPDUTableCurrentValue_Object = MibTableColumn
acsPowerMgmtPDUTableCurrentValue = _AcsPowerMgmtPDUTableCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 39),
    _AcsPowerMgmtPDUTableCurrentValue_Type()
)
acsPowerMgmtPDUTableCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableCurrentValue.setStatus("current")
_AcsPowerMgmtPDUTableCurrentMax_Type = Integer32
_AcsPowerMgmtPDUTableCurrentMax_Object = MibTableColumn
acsPowerMgmtPDUTableCurrentMax = _AcsPowerMgmtPDUTableCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 40),
    _AcsPowerMgmtPDUTableCurrentMax_Type()
)
acsPowerMgmtPDUTableCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableCurrentMax.setStatus("current")
_AcsPowerMgmtPDUTableCurrentMin_Type = Integer32
_AcsPowerMgmtPDUTableCurrentMin_Object = MibTableColumn
acsPowerMgmtPDUTableCurrentMin = _AcsPowerMgmtPDUTableCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 41),
    _AcsPowerMgmtPDUTableCurrentMin_Type()
)
acsPowerMgmtPDUTableCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableCurrentMin.setStatus("current")
_AcsPowerMgmtPDUTableCurrentAvg_Type = Integer32
_AcsPowerMgmtPDUTableCurrentAvg_Object = MibTableColumn
acsPowerMgmtPDUTableCurrentAvg = _AcsPowerMgmtPDUTableCurrentAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 42),
    _AcsPowerMgmtPDUTableCurrentAvg_Type()
)
acsPowerMgmtPDUTableCurrentAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableCurrentAvg.setStatus("current")


class _AcsPowerMgmtPDUTableCurrentReset_Type(Integer32):
    """Custom type acsPowerMgmtPDUTableCurrentReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-action", 1),
          ("reset", 2))
    )


_AcsPowerMgmtPDUTableCurrentReset_Type.__name__ = "Integer32"
_AcsPowerMgmtPDUTableCurrentReset_Object = MibTableColumn
acsPowerMgmtPDUTableCurrentReset = _AcsPowerMgmtPDUTableCurrentReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 43),
    _AcsPowerMgmtPDUTableCurrentReset_Type()
)
acsPowerMgmtPDUTableCurrentReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableCurrentReset.setStatus("current")


class _AcsPowerMgmtPDUTableVoltageType_Type(Integer32):
    """Custom type acsPowerMgmtPDUTableVoltageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none-sensor", 0),
          ("estimated", 1),
          ("read", 2))
    )


_AcsPowerMgmtPDUTableVoltageType_Type.__name__ = "Integer32"
_AcsPowerMgmtPDUTableVoltageType_Object = MibTableColumn
acsPowerMgmtPDUTableVoltageType = _AcsPowerMgmtPDUTableVoltageType_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 44),
    _AcsPowerMgmtPDUTableVoltageType_Type()
)
acsPowerMgmtPDUTableVoltageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableVoltageType.setStatus("current")
_AcsPowerMgmtPDUTableVoltageValue_Type = Integer32
_AcsPowerMgmtPDUTableVoltageValue_Object = MibTableColumn
acsPowerMgmtPDUTableVoltageValue = _AcsPowerMgmtPDUTableVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 45),
    _AcsPowerMgmtPDUTableVoltageValue_Type()
)
acsPowerMgmtPDUTableVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableVoltageValue.setStatus("current")
_AcsPowerMgmtPDUTableVoltageMax_Type = Integer32
_AcsPowerMgmtPDUTableVoltageMax_Object = MibTableColumn
acsPowerMgmtPDUTableVoltageMax = _AcsPowerMgmtPDUTableVoltageMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 46),
    _AcsPowerMgmtPDUTableVoltageMax_Type()
)
acsPowerMgmtPDUTableVoltageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableVoltageMax.setStatus("current")
_AcsPowerMgmtPDUTableVoltageMin_Type = Integer32
_AcsPowerMgmtPDUTableVoltageMin_Object = MibTableColumn
acsPowerMgmtPDUTableVoltageMin = _AcsPowerMgmtPDUTableVoltageMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 47),
    _AcsPowerMgmtPDUTableVoltageMin_Type()
)
acsPowerMgmtPDUTableVoltageMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableVoltageMin.setStatus("current")
_AcsPowerMgmtPDUTableVoltageAvg_Type = Integer32
_AcsPowerMgmtPDUTableVoltageAvg_Object = MibTableColumn
acsPowerMgmtPDUTableVoltageAvg = _AcsPowerMgmtPDUTableVoltageAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 48),
    _AcsPowerMgmtPDUTableVoltageAvg_Type()
)
acsPowerMgmtPDUTableVoltageAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableVoltageAvg.setStatus("current")


class _AcsPowerMgmtPDUTableVoltageReset_Type(Integer32):
    """Custom type acsPowerMgmtPDUTableVoltageReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-action", 1),
          ("reset", 2))
    )


_AcsPowerMgmtPDUTableVoltageReset_Type.__name__ = "Integer32"
_AcsPowerMgmtPDUTableVoltageReset_Object = MibTableColumn
acsPowerMgmtPDUTableVoltageReset = _AcsPowerMgmtPDUTableVoltageReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 49),
    _AcsPowerMgmtPDUTableVoltageReset_Type()
)
acsPowerMgmtPDUTableVoltageReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableVoltageReset.setStatus("current")


class _AcsPowerMgmtPDUTablePowerType_Type(Integer32):
    """Custom type acsPowerMgmtPDUTablePowerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none-sensor", 0),
          ("estimated", 1),
          ("read", 2))
    )


_AcsPowerMgmtPDUTablePowerType_Type.__name__ = "Integer32"
_AcsPowerMgmtPDUTablePowerType_Object = MibTableColumn
acsPowerMgmtPDUTablePowerType = _AcsPowerMgmtPDUTablePowerType_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 50),
    _AcsPowerMgmtPDUTablePowerType_Type()
)
acsPowerMgmtPDUTablePowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTablePowerType.setStatus("current")
_AcsPowerMgmtPDUTablePowerValue_Type = Integer32
_AcsPowerMgmtPDUTablePowerValue_Object = MibTableColumn
acsPowerMgmtPDUTablePowerValue = _AcsPowerMgmtPDUTablePowerValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 51),
    _AcsPowerMgmtPDUTablePowerValue_Type()
)
acsPowerMgmtPDUTablePowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTablePowerValue.setStatus("current")
_AcsPowerMgmtPDUTablePowerMax_Type = Integer32
_AcsPowerMgmtPDUTablePowerMax_Object = MibTableColumn
acsPowerMgmtPDUTablePowerMax = _AcsPowerMgmtPDUTablePowerMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 52),
    _AcsPowerMgmtPDUTablePowerMax_Type()
)
acsPowerMgmtPDUTablePowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTablePowerMax.setStatus("current")
_AcsPowerMgmtPDUTablePowerMin_Type = Integer32
_AcsPowerMgmtPDUTablePowerMin_Object = MibTableColumn
acsPowerMgmtPDUTablePowerMin = _AcsPowerMgmtPDUTablePowerMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 53),
    _AcsPowerMgmtPDUTablePowerMin_Type()
)
acsPowerMgmtPDUTablePowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTablePowerMin.setStatus("current")
_AcsPowerMgmtPDUTablePowerAvg_Type = Integer32
_AcsPowerMgmtPDUTablePowerAvg_Object = MibTableColumn
acsPowerMgmtPDUTablePowerAvg = _AcsPowerMgmtPDUTablePowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 54),
    _AcsPowerMgmtPDUTablePowerAvg_Type()
)
acsPowerMgmtPDUTablePowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTablePowerAvg.setStatus("current")


class _AcsPowerMgmtPDUTablePowerReset_Type(Integer32):
    """Custom type acsPowerMgmtPDUTablePowerReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-action", 1),
          ("reset", 2))
    )


_AcsPowerMgmtPDUTablePowerReset_Type.__name__ = "Integer32"
_AcsPowerMgmtPDUTablePowerReset_Object = MibTableColumn
acsPowerMgmtPDUTablePowerReset = _AcsPowerMgmtPDUTablePowerReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 55),
    _AcsPowerMgmtPDUTablePowerReset_Type()
)
acsPowerMgmtPDUTablePowerReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTablePowerReset.setStatus("current")


class _AcsPowerMgmtPDUTablePowerFactorType_Type(Integer32):
    """Custom type acsPowerMgmtPDUTablePowerFactorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none-sensor", 0),
          ("estimated", 1),
          ("read", 2))
    )


_AcsPowerMgmtPDUTablePowerFactorType_Type.__name__ = "Integer32"
_AcsPowerMgmtPDUTablePowerFactorType_Object = MibTableColumn
acsPowerMgmtPDUTablePowerFactorType = _AcsPowerMgmtPDUTablePowerFactorType_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 56),
    _AcsPowerMgmtPDUTablePowerFactorType_Type()
)
acsPowerMgmtPDUTablePowerFactorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTablePowerFactorType.setStatus("current")
_AcsPowerMgmtPDUTablePowerFactorValue_Type = Integer32
_AcsPowerMgmtPDUTablePowerFactorValue_Object = MibTableColumn
acsPowerMgmtPDUTablePowerFactorValue = _AcsPowerMgmtPDUTablePowerFactorValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 57),
    _AcsPowerMgmtPDUTablePowerFactorValue_Type()
)
acsPowerMgmtPDUTablePowerFactorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTablePowerFactorValue.setStatus("current")
_AcsPowerMgmtPDUTablePowerFactorMax_Type = Integer32
_AcsPowerMgmtPDUTablePowerFactorMax_Object = MibTableColumn
acsPowerMgmtPDUTablePowerFactorMax = _AcsPowerMgmtPDUTablePowerFactorMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 58),
    _AcsPowerMgmtPDUTablePowerFactorMax_Type()
)
acsPowerMgmtPDUTablePowerFactorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTablePowerFactorMax.setStatus("current")
_AcsPowerMgmtPDUTablePowerFactorMin_Type = Integer32
_AcsPowerMgmtPDUTablePowerFactorMin_Object = MibTableColumn
acsPowerMgmtPDUTablePowerFactorMin = _AcsPowerMgmtPDUTablePowerFactorMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 59),
    _AcsPowerMgmtPDUTablePowerFactorMin_Type()
)
acsPowerMgmtPDUTablePowerFactorMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTablePowerFactorMin.setStatus("current")
_AcsPowerMgmtPDUTablePowerFactorAvg_Type = Integer32
_AcsPowerMgmtPDUTablePowerFactorAvg_Object = MibTableColumn
acsPowerMgmtPDUTablePowerFactorAvg = _AcsPowerMgmtPDUTablePowerFactorAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 60),
    _AcsPowerMgmtPDUTablePowerFactorAvg_Type()
)
acsPowerMgmtPDUTablePowerFactorAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTablePowerFactorAvg.setStatus("current")


class _AcsPowerMgmtPDUTablePowerFactorReset_Type(Integer32):
    """Custom type acsPowerMgmtPDUTablePowerFactorReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-action", 1),
          ("reset", 2))
    )


_AcsPowerMgmtPDUTablePowerFactorReset_Type.__name__ = "Integer32"
_AcsPowerMgmtPDUTablePowerFactorReset_Object = MibTableColumn
acsPowerMgmtPDUTablePowerFactorReset = _AcsPowerMgmtPDUTablePowerFactorReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 61),
    _AcsPowerMgmtPDUTablePowerFactorReset_Type()
)
acsPowerMgmtPDUTablePowerFactorReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTablePowerFactorReset.setStatus("current")


class _AcsPowerMgmtPDUTableAlarm_Type(Integer32):
    """Custom type acsPowerMgmtPDUTableAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("blow-fuse", 2),
          ("hw-ocp", 3),
          ("high-critical", 4),
          ("high-warning", 5),
          ("low-warning", 6),
          ("low-critical", 7))
    )


_AcsPowerMgmtPDUTableAlarm_Type.__name__ = "Integer32"
_AcsPowerMgmtPDUTableAlarm_Object = MibTableColumn
acsPowerMgmtPDUTableAlarm = _AcsPowerMgmtPDUTableAlarm_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 62),
    _AcsPowerMgmtPDUTableAlarm_Type()
)
acsPowerMgmtPDUTableAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableAlarm.setStatus("current")
_AcsPowerMgmtPDUTableEnvSensors_Type = Integer32
_AcsPowerMgmtPDUTableEnvSensors_Object = MibTableColumn
acsPowerMgmtPDUTableEnvSensors = _AcsPowerMgmtPDUTableEnvSensors_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 63),
    _AcsPowerMgmtPDUTableEnvSensors_Type()
)
acsPowerMgmtPDUTableEnvSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableEnvSensors.setStatus("current")
_AcsPowerMgmtPDUTableAgentSerialNumber_Type = DisplayString
_AcsPowerMgmtPDUTableAgentSerialNumber_Object = MibTableColumn
acsPowerMgmtPDUTableAgentSerialNumber = _AcsPowerMgmtPDUTableAgentSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 64),
    _AcsPowerMgmtPDUTableAgentSerialNumber_Type()
)
acsPowerMgmtPDUTableAgentSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableAgentSerialNumber.setStatus("current")
_AcsPowerMgmtPDUTablePduModelNumber_Type = DisplayString
_AcsPowerMgmtPDUTablePduModelNumber_Object = MibTableColumn
acsPowerMgmtPDUTablePduModelNumber = _AcsPowerMgmtPDUTablePduModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 65),
    _AcsPowerMgmtPDUTablePduModelNumber_Type()
)
acsPowerMgmtPDUTablePduModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTablePduModelNumber.setStatus("current")
_AcsPowerMgmtPDUTablePduSerialNumber_Type = DisplayString
_AcsPowerMgmtPDUTablePduSerialNumber_Object = MibTableColumn
acsPowerMgmtPDUTablePduSerialNumber = _AcsPowerMgmtPDUTablePduSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 66),
    _AcsPowerMgmtPDUTablePduSerialNumber_Type()
)
acsPowerMgmtPDUTablePduSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTablePduSerialNumber.setStatus("current")
_AcsPowerMgmtPDUTablePduPartNumber_Type = DisplayString
_AcsPowerMgmtPDUTablePduPartNumber_Object = MibTableColumn
acsPowerMgmtPDUTablePduPartNumber = _AcsPowerMgmtPDUTablePduPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 3, 1, 67),
    _AcsPowerMgmtPDUTablePduPartNumber_Type()
)
acsPowerMgmtPDUTablePduPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTablePduPartNumber.setStatus("current")
_AcsPowerMgmtTotalNumberOfOutlets_Type = Integer32
_AcsPowerMgmtTotalNumberOfOutlets_Object = MibScalar
acsPowerMgmtTotalNumberOfOutlets = _AcsPowerMgmtTotalNumberOfOutlets_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 4),
    _AcsPowerMgmtTotalNumberOfOutlets_Type()
)
acsPowerMgmtTotalNumberOfOutlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtTotalNumberOfOutlets.setStatus("current")
_AcsPowerMgmtOutletsTable_Object = MibTable
acsPowerMgmtOutletsTable = _AcsPowerMgmtOutletsTable_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 5)
)
if mibBuilder.loadTexts:
    acsPowerMgmtOutletsTable.setStatus("current")
_AcsPowerMgmtOutletsTableEntry_Object = MibTableRow
acsPowerMgmtOutletsTableEntry = _AcsPowerMgmtOutletsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 5, 1)
)
acsPowerMgmtOutletsTableEntry.setIndexNames(
    (0, "ACS8000-MIB", "acsPowerMgmtOutletsTablePortNumber"),
    (0, "ACS8000-MIB", "acsPowerMgmtOutletsTablePduNumber"),
    (0, "ACS8000-MIB", "acsPowerMgmtOutletsTableNumber"),
)
if mibBuilder.loadTexts:
    acsPowerMgmtOutletsTableEntry.setStatus("current")
_AcsPowerMgmtOutletsTablePortNumber_Type = InterfaceIndex
_AcsPowerMgmtOutletsTablePortNumber_Object = MibTableColumn
acsPowerMgmtOutletsTablePortNumber = _AcsPowerMgmtOutletsTablePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 5, 1, 1),
    _AcsPowerMgmtOutletsTablePortNumber_Type()
)
acsPowerMgmtOutletsTablePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutletsTablePortNumber.setStatus("current")
_AcsPowerMgmtOutletsTablePduNumber_Type = InterfaceIndex
_AcsPowerMgmtOutletsTablePduNumber_Object = MibTableColumn
acsPowerMgmtOutletsTablePduNumber = _AcsPowerMgmtOutletsTablePduNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 5, 1, 2),
    _AcsPowerMgmtOutletsTablePduNumber_Type()
)
acsPowerMgmtOutletsTablePduNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutletsTablePduNumber.setStatus("current")
_AcsPowerMgmtOutletsTableNumber_Type = InterfaceIndex
_AcsPowerMgmtOutletsTableNumber_Object = MibTableColumn
acsPowerMgmtOutletsTableNumber = _AcsPowerMgmtOutletsTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 5, 1, 3),
    _AcsPowerMgmtOutletsTableNumber_Type()
)
acsPowerMgmtOutletsTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutletsTableNumber.setStatus("current")
_AcsPowerMgmtOutletsTableName_Type = DisplayString
_AcsPowerMgmtOutletsTableName_Object = MibTableColumn
acsPowerMgmtOutletsTableName = _AcsPowerMgmtOutletsTableName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 5, 1, 4),
    _AcsPowerMgmtOutletsTableName_Type()
)
acsPowerMgmtOutletsTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutletsTableName.setStatus("current")


class _AcsPowerMgmtOutletsTableStatus_Type(Integer32):
    """Custom type acsPowerMgmtOutletsTableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_AcsPowerMgmtOutletsTableStatus_Type.__name__ = "Integer32"
_AcsPowerMgmtOutletsTableStatus_Object = MibTableColumn
acsPowerMgmtOutletsTableStatus = _AcsPowerMgmtOutletsTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 5, 1, 5),
    _AcsPowerMgmtOutletsTableStatus_Type()
)
acsPowerMgmtOutletsTableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutletsTableStatus.setStatus("current")


class _AcsPowerMgmtOutletsTablePowerControl_Type(Integer32):
    """Custom type acsPowerMgmtOutletsTablePowerControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("powerOn", 2),
          ("powerOff", 3),
          ("powerCycle", 4),
          ("powerLock", 5),
          ("powerUnlock", 6))
    )


_AcsPowerMgmtOutletsTablePowerControl_Type.__name__ = "Integer32"
_AcsPowerMgmtOutletsTablePowerControl_Object = MibTableColumn
acsPowerMgmtOutletsTablePowerControl = _AcsPowerMgmtOutletsTablePowerControl_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 5, 1, 6),
    _AcsPowerMgmtOutletsTablePowerControl_Type()
)
acsPowerMgmtOutletsTablePowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtOutletsTablePowerControl.setStatus("current")
_AcsPowerMgmtOutletsTablePortName_Type = DisplayString
_AcsPowerMgmtOutletsTablePortName_Object = MibTableColumn
acsPowerMgmtOutletsTablePortName = _AcsPowerMgmtOutletsTablePortName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 5, 1, 7),
    _AcsPowerMgmtOutletsTablePortName_Type()
)
acsPowerMgmtOutletsTablePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutletsTablePortName.setStatus("current")
_AcsPowerMgmtOutletsTablePduId_Type = DisplayString
_AcsPowerMgmtOutletsTablePduId_Object = MibTableColumn
acsPowerMgmtOutletsTablePduId = _AcsPowerMgmtOutletsTablePduId_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 5, 1, 8),
    _AcsPowerMgmtOutletsTablePduId_Type()
)
acsPowerMgmtOutletsTablePduId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutletsTablePduId.setStatus("current")
_AcsPowerMgmtNumberOfOutletGroup_Type = Integer32
_AcsPowerMgmtNumberOfOutletGroup_Object = MibScalar
acsPowerMgmtNumberOfOutletGroup = _AcsPowerMgmtNumberOfOutletGroup_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 6),
    _AcsPowerMgmtNumberOfOutletGroup_Type()
)
acsPowerMgmtNumberOfOutletGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtNumberOfOutletGroup.setStatus("current")
_AcsPowerMgmtGroupTable_Object = MibTable
acsPowerMgmtGroupTable = _AcsPowerMgmtGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 7)
)
if mibBuilder.loadTexts:
    acsPowerMgmtGroupTable.setStatus("current")
_AcsPowerMgmtGroupTableEntry_Object = MibTableRow
acsPowerMgmtGroupTableEntry = _AcsPowerMgmtGroupTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 7, 1)
)
acsPowerMgmtGroupTableEntry.setIndexNames(
    (0, "ACS8000-MIB", "acsPowerMgmtGroupTableIndex"),
)
if mibBuilder.loadTexts:
    acsPowerMgmtGroupTableEntry.setStatus("current")
_AcsPowerMgmtGroupTableIndex_Type = InterfaceIndexOrZero
_AcsPowerMgmtGroupTableIndex_Object = MibTableColumn
acsPowerMgmtGroupTableIndex = _AcsPowerMgmtGroupTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 7, 1, 1),
    _AcsPowerMgmtGroupTableIndex_Type()
)
acsPowerMgmtGroupTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtGroupTableIndex.setStatus("current")
_AcsPowerMgmtGroupTableName_Type = DisplayString
_AcsPowerMgmtGroupTableName_Object = MibTableColumn
acsPowerMgmtGroupTableName = _AcsPowerMgmtGroupTableName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 7, 1, 2),
    _AcsPowerMgmtGroupTableName_Type()
)
acsPowerMgmtGroupTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtGroupTableName.setStatus("current")


class _AcsPowerMgmtGroupTableStatus_Type(Integer32):
    """Custom type acsPowerMgmtGroupTableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_AcsPowerMgmtGroupTableStatus_Type.__name__ = "Integer32"
_AcsPowerMgmtGroupTableStatus_Object = MibTableColumn
acsPowerMgmtGroupTableStatus = _AcsPowerMgmtGroupTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 7, 1, 3),
    _AcsPowerMgmtGroupTableStatus_Type()
)
acsPowerMgmtGroupTableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtGroupTableStatus.setStatus("current")


class _AcsPowerMgmtGroupTablePowerControl_Type(Integer32):
    """Custom type acsPowerMgmtGroupTablePowerControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("powerOn", 2),
          ("powerOff", 3),
          ("powerCycle", 4))
    )


_AcsPowerMgmtGroupTablePowerControl_Type.__name__ = "Integer32"
_AcsPowerMgmtGroupTablePowerControl_Object = MibTableColumn
acsPowerMgmtGroupTablePowerControl = _AcsPowerMgmtGroupTablePowerControl_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 7, 1, 4),
    _AcsPowerMgmtGroupTablePowerControl_Type()
)
acsPowerMgmtGroupTablePowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtGroupTablePowerControl.setStatus("current")
_AcsPowerMgmtPhasesTable_Object = MibTable
acsPowerMgmtPhasesTable = _AcsPowerMgmtPhasesTable_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 8)
)
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTable.setStatus("current")
_AcsPowerMgmtPhasesTableEntry_Object = MibTableRow
acsPowerMgmtPhasesTableEntry = _AcsPowerMgmtPhasesTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 8, 1)
)
acsPowerMgmtPhasesTableEntry.setIndexNames(
    (0, "ACS8000-MIB", "acsPowerMgmtPhasesTablePortNumber"),
    (0, "ACS8000-MIB", "acsPowerMgmtPhasesTablePduIndex"),
    (0, "ACS8000-MIB", "acsPowerMgmtPhasesTablePhaseIndex"),
)
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTableEntry.setStatus("current")
_AcsPowerMgmtPhasesTablePortNumber_Type = InterfaceIndex
_AcsPowerMgmtPhasesTablePortNumber_Object = MibTableColumn
acsPowerMgmtPhasesTablePortNumber = _AcsPowerMgmtPhasesTablePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 8, 1, 1),
    _AcsPowerMgmtPhasesTablePortNumber_Type()
)
acsPowerMgmtPhasesTablePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTablePortNumber.setStatus("current")
_AcsPowerMgmtPhasesTablePduIndex_Type = InterfaceIndexOrZero
_AcsPowerMgmtPhasesTablePduIndex_Object = MibTableColumn
acsPowerMgmtPhasesTablePduIndex = _AcsPowerMgmtPhasesTablePduIndex_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 8, 1, 2),
    _AcsPowerMgmtPhasesTablePduIndex_Type()
)
acsPowerMgmtPhasesTablePduIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTablePduIndex.setStatus("current")
_AcsPowerMgmtPhasesTablePhaseIndex_Type = InterfaceIndexOrZero
_AcsPowerMgmtPhasesTablePhaseIndex_Object = MibTableColumn
acsPowerMgmtPhasesTablePhaseIndex = _AcsPowerMgmtPhasesTablePhaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 8, 1, 3),
    _AcsPowerMgmtPhasesTablePhaseIndex_Type()
)
acsPowerMgmtPhasesTablePhaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTablePhaseIndex.setStatus("current")
_AcsPowerMgmtPhasesTablePhaseName_Type = DisplayString
_AcsPowerMgmtPhasesTablePhaseName_Object = MibTableColumn
acsPowerMgmtPhasesTablePhaseName = _AcsPowerMgmtPhasesTablePhaseName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 8, 1, 4),
    _AcsPowerMgmtPhasesTablePhaseName_Type()
)
acsPowerMgmtPhasesTablePhaseName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTablePhaseName.setStatus("current")
_AcsPowerMgmtPhasesTablePduId_Type = DisplayString
_AcsPowerMgmtPhasesTablePduId_Object = MibTableColumn
acsPowerMgmtPhasesTablePduId = _AcsPowerMgmtPhasesTablePduId_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 8, 1, 5),
    _AcsPowerMgmtPhasesTablePduId_Type()
)
acsPowerMgmtPhasesTablePduId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTablePduId.setStatus("current")
_AcsPowerMgmtPhasesTablePortName_Type = DisplayString
_AcsPowerMgmtPhasesTablePortName_Object = MibTableColumn
acsPowerMgmtPhasesTablePortName = _AcsPowerMgmtPhasesTablePortName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 8, 1, 6),
    _AcsPowerMgmtPhasesTablePortName_Type()
)
acsPowerMgmtPhasesTablePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTablePortName.setStatus("current")
_AcsPowerMgmtPhasesTableCurrentValue_Type = Integer32
_AcsPowerMgmtPhasesTableCurrentValue_Object = MibTableColumn
acsPowerMgmtPhasesTableCurrentValue = _AcsPowerMgmtPhasesTableCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 8, 1, 7),
    _AcsPowerMgmtPhasesTableCurrentValue_Type()
)
acsPowerMgmtPhasesTableCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTableCurrentValue.setStatus("current")
_AcsPowerMgmtPhasesTableCurrentMax_Type = Integer32
_AcsPowerMgmtPhasesTableCurrentMax_Object = MibTableColumn
acsPowerMgmtPhasesTableCurrentMax = _AcsPowerMgmtPhasesTableCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 8, 1, 8),
    _AcsPowerMgmtPhasesTableCurrentMax_Type()
)
acsPowerMgmtPhasesTableCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTableCurrentMax.setStatus("current")
_AcsPowerMgmtPhasesTableCurrentMin_Type = Integer32
_AcsPowerMgmtPhasesTableCurrentMin_Object = MibTableColumn
acsPowerMgmtPhasesTableCurrentMin = _AcsPowerMgmtPhasesTableCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 8, 1, 9),
    _AcsPowerMgmtPhasesTableCurrentMin_Type()
)
acsPowerMgmtPhasesTableCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTableCurrentMin.setStatus("current")
_AcsPowerMgmtPhasesTableCurrentAvg_Type = Integer32
_AcsPowerMgmtPhasesTableCurrentAvg_Object = MibTableColumn
acsPowerMgmtPhasesTableCurrentAvg = _AcsPowerMgmtPhasesTableCurrentAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 8, 1, 10),
    _AcsPowerMgmtPhasesTableCurrentAvg_Type()
)
acsPowerMgmtPhasesTableCurrentAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTableCurrentAvg.setStatus("current")


class _AcsPowerMgmtPhasesTableCurrentReset_Type(Integer32):
    """Custom type acsPowerMgmtPhasesTableCurrentReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-action", 1),
          ("reset", 2))
    )


_AcsPowerMgmtPhasesTableCurrentReset_Type.__name__ = "Integer32"
_AcsPowerMgmtPhasesTableCurrentReset_Object = MibTableColumn
acsPowerMgmtPhasesTableCurrentReset = _AcsPowerMgmtPhasesTableCurrentReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 8, 1, 11),
    _AcsPowerMgmtPhasesTableCurrentReset_Type()
)
acsPowerMgmtPhasesTableCurrentReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTableCurrentReset.setStatus("current")


class _AcsPowerMgmtPhasesTableVoltageType_Type(Integer32):
    """Custom type acsPowerMgmtPhasesTableVoltageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none-sensor", 0),
          ("estimated", 1),
          ("read", 2))
    )


_AcsPowerMgmtPhasesTableVoltageType_Type.__name__ = "Integer32"
_AcsPowerMgmtPhasesTableVoltageType_Object = MibTableColumn
acsPowerMgmtPhasesTableVoltageType = _AcsPowerMgmtPhasesTableVoltageType_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 8, 1, 12),
    _AcsPowerMgmtPhasesTableVoltageType_Type()
)
acsPowerMgmtPhasesTableVoltageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTableVoltageType.setStatus("current")
_AcsPowerMgmtPhasesTableVoltageValue_Type = Integer32
_AcsPowerMgmtPhasesTableVoltageValue_Object = MibTableColumn
acsPowerMgmtPhasesTableVoltageValue = _AcsPowerMgmtPhasesTableVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 8, 1, 13),
    _AcsPowerMgmtPhasesTableVoltageValue_Type()
)
acsPowerMgmtPhasesTableVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTableVoltageValue.setStatus("current")
_AcsPowerMgmtPhasesTableVoltageMax_Type = Integer32
_AcsPowerMgmtPhasesTableVoltageMax_Object = MibTableColumn
acsPowerMgmtPhasesTableVoltageMax = _AcsPowerMgmtPhasesTableVoltageMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 8, 1, 14),
    _AcsPowerMgmtPhasesTableVoltageMax_Type()
)
acsPowerMgmtPhasesTableVoltageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTableVoltageMax.setStatus("current")
_AcsPowerMgmtPhasesTableVoltageMin_Type = Integer32
_AcsPowerMgmtPhasesTableVoltageMin_Object = MibTableColumn
acsPowerMgmtPhasesTableVoltageMin = _AcsPowerMgmtPhasesTableVoltageMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 8, 1, 15),
    _AcsPowerMgmtPhasesTableVoltageMin_Type()
)
acsPowerMgmtPhasesTableVoltageMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTableVoltageMin.setStatus("current")
_AcsPowerMgmtPhasesTableVoltageAvg_Type = Integer32
_AcsPowerMgmtPhasesTableVoltageAvg_Object = MibTableColumn
acsPowerMgmtPhasesTableVoltageAvg = _AcsPowerMgmtPhasesTableVoltageAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 8, 1, 16),
    _AcsPowerMgmtPhasesTableVoltageAvg_Type()
)
acsPowerMgmtPhasesTableVoltageAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTableVoltageAvg.setStatus("current")


class _AcsPowerMgmtPhasesTableVoltageReset_Type(Integer32):
    """Custom type acsPowerMgmtPhasesTableVoltageReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-action", 1),
          ("reset", 2))
    )


_AcsPowerMgmtPhasesTableVoltageReset_Type.__name__ = "Integer32"
_AcsPowerMgmtPhasesTableVoltageReset_Object = MibTableColumn
acsPowerMgmtPhasesTableVoltageReset = _AcsPowerMgmtPhasesTableVoltageReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 8, 1, 17),
    _AcsPowerMgmtPhasesTableVoltageReset_Type()
)
acsPowerMgmtPhasesTableVoltageReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTableVoltageReset.setStatus("current")


class _AcsPowerMgmtPhasesTablePowerType_Type(Integer32):
    """Custom type acsPowerMgmtPhasesTablePowerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none-sensor", 0),
          ("estimated", 1),
          ("read", 2))
    )


_AcsPowerMgmtPhasesTablePowerType_Type.__name__ = "Integer32"
_AcsPowerMgmtPhasesTablePowerType_Object = MibTableColumn
acsPowerMgmtPhasesTablePowerType = _AcsPowerMgmtPhasesTablePowerType_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 8, 1, 18),
    _AcsPowerMgmtPhasesTablePowerType_Type()
)
acsPowerMgmtPhasesTablePowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTablePowerType.setStatus("current")
_AcsPowerMgmtPhasesTablePowerValue_Type = Integer32
_AcsPowerMgmtPhasesTablePowerValue_Object = MibTableColumn
acsPowerMgmtPhasesTablePowerValue = _AcsPowerMgmtPhasesTablePowerValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 8, 1, 19),
    _AcsPowerMgmtPhasesTablePowerValue_Type()
)
acsPowerMgmtPhasesTablePowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTablePowerValue.setStatus("current")
_AcsPowerMgmtPhasesTablePowerMax_Type = Integer32
_AcsPowerMgmtPhasesTablePowerMax_Object = MibTableColumn
acsPowerMgmtPhasesTablePowerMax = _AcsPowerMgmtPhasesTablePowerMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 8, 1, 20),
    _AcsPowerMgmtPhasesTablePowerMax_Type()
)
acsPowerMgmtPhasesTablePowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTablePowerMax.setStatus("current")
_AcsPowerMgmtPhasesTablePowerMin_Type = Integer32
_AcsPowerMgmtPhasesTablePowerMin_Object = MibTableColumn
acsPowerMgmtPhasesTablePowerMin = _AcsPowerMgmtPhasesTablePowerMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 8, 1, 21),
    _AcsPowerMgmtPhasesTablePowerMin_Type()
)
acsPowerMgmtPhasesTablePowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTablePowerMin.setStatus("current")
_AcsPowerMgmtPhasesTablePowerAvg_Type = Integer32
_AcsPowerMgmtPhasesTablePowerAvg_Object = MibTableColumn
acsPowerMgmtPhasesTablePowerAvg = _AcsPowerMgmtPhasesTablePowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 8, 1, 22),
    _AcsPowerMgmtPhasesTablePowerAvg_Type()
)
acsPowerMgmtPhasesTablePowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTablePowerAvg.setStatus("current")


class _AcsPowerMgmtPhasesTablePowerReset_Type(Integer32):
    """Custom type acsPowerMgmtPhasesTablePowerReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-action", 1),
          ("reset", 2))
    )


_AcsPowerMgmtPhasesTablePowerReset_Type.__name__ = "Integer32"
_AcsPowerMgmtPhasesTablePowerReset_Object = MibTableColumn
acsPowerMgmtPhasesTablePowerReset = _AcsPowerMgmtPhasesTablePowerReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 8, 1, 23),
    _AcsPowerMgmtPhasesTablePowerReset_Type()
)
acsPowerMgmtPhasesTablePowerReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTablePowerReset.setStatus("current")


class _AcsPowerMgmtPhasesTablePowerFactorType_Type(Integer32):
    """Custom type acsPowerMgmtPhasesTablePowerFactorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none-sensor", 0),
          ("estimated", 1),
          ("read", 2))
    )


_AcsPowerMgmtPhasesTablePowerFactorType_Type.__name__ = "Integer32"
_AcsPowerMgmtPhasesTablePowerFactorType_Object = MibTableColumn
acsPowerMgmtPhasesTablePowerFactorType = _AcsPowerMgmtPhasesTablePowerFactorType_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 8, 1, 24),
    _AcsPowerMgmtPhasesTablePowerFactorType_Type()
)
acsPowerMgmtPhasesTablePowerFactorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTablePowerFactorType.setStatus("current")
_AcsPowerMgmtPhasesTablePowerFactorValue_Type = Integer32
_AcsPowerMgmtPhasesTablePowerFactorValue_Object = MibTableColumn
acsPowerMgmtPhasesTablePowerFactorValue = _AcsPowerMgmtPhasesTablePowerFactorValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 8, 1, 25),
    _AcsPowerMgmtPhasesTablePowerFactorValue_Type()
)
acsPowerMgmtPhasesTablePowerFactorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTablePowerFactorValue.setStatus("current")
_AcsPowerMgmtPhasesTablePowerFactorMax_Type = Integer32
_AcsPowerMgmtPhasesTablePowerFactorMax_Object = MibTableColumn
acsPowerMgmtPhasesTablePowerFactorMax = _AcsPowerMgmtPhasesTablePowerFactorMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 8, 1, 26),
    _AcsPowerMgmtPhasesTablePowerFactorMax_Type()
)
acsPowerMgmtPhasesTablePowerFactorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTablePowerFactorMax.setStatus("current")
_AcsPowerMgmtPhasesTablePowerFactorMin_Type = Integer32
_AcsPowerMgmtPhasesTablePowerFactorMin_Object = MibTableColumn
acsPowerMgmtPhasesTablePowerFactorMin = _AcsPowerMgmtPhasesTablePowerFactorMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 8, 1, 27),
    _AcsPowerMgmtPhasesTablePowerFactorMin_Type()
)
acsPowerMgmtPhasesTablePowerFactorMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTablePowerFactorMin.setStatus("current")
_AcsPowerMgmtPhasesTablePowerFactorAvg_Type = Integer32
_AcsPowerMgmtPhasesTablePowerFactorAvg_Object = MibTableColumn
acsPowerMgmtPhasesTablePowerFactorAvg = _AcsPowerMgmtPhasesTablePowerFactorAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 8, 1, 28),
    _AcsPowerMgmtPhasesTablePowerFactorAvg_Type()
)
acsPowerMgmtPhasesTablePowerFactorAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTablePowerFactorAvg.setStatus("current")


class _AcsPowerMgmtPhasesTablePowerFactorReset_Type(Integer32):
    """Custom type acsPowerMgmtPhasesTablePowerFactorReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-action", 1),
          ("reset", 2))
    )


_AcsPowerMgmtPhasesTablePowerFactorReset_Type.__name__ = "Integer32"
_AcsPowerMgmtPhasesTablePowerFactorReset_Object = MibTableColumn
acsPowerMgmtPhasesTablePowerFactorReset = _AcsPowerMgmtPhasesTablePowerFactorReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 8, 1, 29),
    _AcsPowerMgmtPhasesTablePowerFactorReset_Type()
)
acsPowerMgmtPhasesTablePowerFactorReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTablePowerFactorReset.setStatus("current")


class _AcsPowerMgmtPhasesTableAlarm_Type(Integer32):
    """Custom type acsPowerMgmtPhasesTableAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("blow-fuse", 2),
          ("hw-ocp", 3),
          ("high-critical", 4),
          ("high-warning", 5),
          ("low-warning", 6),
          ("low-critical", 7))
    )


_AcsPowerMgmtPhasesTableAlarm_Type.__name__ = "Integer32"
_AcsPowerMgmtPhasesTableAlarm_Object = MibTableColumn
acsPowerMgmtPhasesTableAlarm = _AcsPowerMgmtPhasesTableAlarm_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 8, 1, 30),
    _AcsPowerMgmtPhasesTableAlarm_Type()
)
acsPowerMgmtPhasesTableAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTableAlarm.setStatus("current")
_AcsPowerMgmtBanksTable_Object = MibTable
acsPowerMgmtBanksTable = _AcsPowerMgmtBanksTable_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 9)
)
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTable.setStatus("current")
_AcsPowerMgmtBanksTableEntry_Object = MibTableRow
acsPowerMgmtBanksTableEntry = _AcsPowerMgmtBanksTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 9, 1)
)
acsPowerMgmtBanksTableEntry.setIndexNames(
    (0, "ACS8000-MIB", "acsPowerMgmtBanksTablePortNumber"),
    (0, "ACS8000-MIB", "acsPowerMgmtBanksTablePduIndex"),
    (0, "ACS8000-MIB", "acsPowerMgmtBanksTableBankIndex"),
)
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTableEntry.setStatus("current")
_AcsPowerMgmtBanksTablePortNumber_Type = InterfaceIndex
_AcsPowerMgmtBanksTablePortNumber_Object = MibTableColumn
acsPowerMgmtBanksTablePortNumber = _AcsPowerMgmtBanksTablePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 9, 1, 1),
    _AcsPowerMgmtBanksTablePortNumber_Type()
)
acsPowerMgmtBanksTablePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTablePortNumber.setStatus("current")
_AcsPowerMgmtBanksTablePduIndex_Type = InterfaceIndexOrZero
_AcsPowerMgmtBanksTablePduIndex_Object = MibTableColumn
acsPowerMgmtBanksTablePduIndex = _AcsPowerMgmtBanksTablePduIndex_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 9, 1, 2),
    _AcsPowerMgmtBanksTablePduIndex_Type()
)
acsPowerMgmtBanksTablePduIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTablePduIndex.setStatus("current")
_AcsPowerMgmtBanksTableBankIndex_Type = InterfaceIndexOrZero
_AcsPowerMgmtBanksTableBankIndex_Object = MibTableColumn
acsPowerMgmtBanksTableBankIndex = _AcsPowerMgmtBanksTableBankIndex_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 9, 1, 3),
    _AcsPowerMgmtBanksTableBankIndex_Type()
)
acsPowerMgmtBanksTableBankIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTableBankIndex.setStatus("current")
_AcsPowerMgmtBanksTableBankName_Type = DisplayString
_AcsPowerMgmtBanksTableBankName_Object = MibTableColumn
acsPowerMgmtBanksTableBankName = _AcsPowerMgmtBanksTableBankName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 9, 1, 4),
    _AcsPowerMgmtBanksTableBankName_Type()
)
acsPowerMgmtBanksTableBankName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTableBankName.setStatus("current")
_AcsPowerMgmtBanksTablePduId_Type = DisplayString
_AcsPowerMgmtBanksTablePduId_Object = MibTableColumn
acsPowerMgmtBanksTablePduId = _AcsPowerMgmtBanksTablePduId_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 9, 1, 5),
    _AcsPowerMgmtBanksTablePduId_Type()
)
acsPowerMgmtBanksTablePduId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTablePduId.setStatus("current")
_AcsPowerMgmtBanksTablePortName_Type = DisplayString
_AcsPowerMgmtBanksTablePortName_Object = MibTableColumn
acsPowerMgmtBanksTablePortName = _AcsPowerMgmtBanksTablePortName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 9, 1, 6),
    _AcsPowerMgmtBanksTablePortName_Type()
)
acsPowerMgmtBanksTablePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTablePortName.setStatus("current")
_AcsPowerMgmtBanksTableCurrentValue_Type = Integer32
_AcsPowerMgmtBanksTableCurrentValue_Object = MibTableColumn
acsPowerMgmtBanksTableCurrentValue = _AcsPowerMgmtBanksTableCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 9, 1, 7),
    _AcsPowerMgmtBanksTableCurrentValue_Type()
)
acsPowerMgmtBanksTableCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTableCurrentValue.setStatus("current")
_AcsPowerMgmtBanksTableCurrentMax_Type = Integer32
_AcsPowerMgmtBanksTableCurrentMax_Object = MibTableColumn
acsPowerMgmtBanksTableCurrentMax = _AcsPowerMgmtBanksTableCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 9, 1, 8),
    _AcsPowerMgmtBanksTableCurrentMax_Type()
)
acsPowerMgmtBanksTableCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTableCurrentMax.setStatus("current")
_AcsPowerMgmtBanksTableCurrentMin_Type = Integer32
_AcsPowerMgmtBanksTableCurrentMin_Object = MibTableColumn
acsPowerMgmtBanksTableCurrentMin = _AcsPowerMgmtBanksTableCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 9, 1, 9),
    _AcsPowerMgmtBanksTableCurrentMin_Type()
)
acsPowerMgmtBanksTableCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTableCurrentMin.setStatus("current")
_AcsPowerMgmtBanksTableCurrentAvg_Type = Integer32
_AcsPowerMgmtBanksTableCurrentAvg_Object = MibTableColumn
acsPowerMgmtBanksTableCurrentAvg = _AcsPowerMgmtBanksTableCurrentAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 9, 1, 10),
    _AcsPowerMgmtBanksTableCurrentAvg_Type()
)
acsPowerMgmtBanksTableCurrentAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTableCurrentAvg.setStatus("current")


class _AcsPowerMgmtBanksTableCurrentReset_Type(Integer32):
    """Custom type acsPowerMgmtBanksTableCurrentReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-action", 1),
          ("reset", 2))
    )


_AcsPowerMgmtBanksTableCurrentReset_Type.__name__ = "Integer32"
_AcsPowerMgmtBanksTableCurrentReset_Object = MibTableColumn
acsPowerMgmtBanksTableCurrentReset = _AcsPowerMgmtBanksTableCurrentReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 9, 1, 11),
    _AcsPowerMgmtBanksTableCurrentReset_Type()
)
acsPowerMgmtBanksTableCurrentReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTableCurrentReset.setStatus("current")


class _AcsPowerMgmtBanksTableVoltageType_Type(Integer32):
    """Custom type acsPowerMgmtBanksTableVoltageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none-sensor", 0),
          ("estimated", 1),
          ("read", 2))
    )


_AcsPowerMgmtBanksTableVoltageType_Type.__name__ = "Integer32"
_AcsPowerMgmtBanksTableVoltageType_Object = MibTableColumn
acsPowerMgmtBanksTableVoltageType = _AcsPowerMgmtBanksTableVoltageType_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 9, 1, 12),
    _AcsPowerMgmtBanksTableVoltageType_Type()
)
acsPowerMgmtBanksTableVoltageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTableVoltageType.setStatus("current")
_AcsPowerMgmtBanksTableVoltageValue_Type = Integer32
_AcsPowerMgmtBanksTableVoltageValue_Object = MibTableColumn
acsPowerMgmtBanksTableVoltageValue = _AcsPowerMgmtBanksTableVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 9, 1, 13),
    _AcsPowerMgmtBanksTableVoltageValue_Type()
)
acsPowerMgmtBanksTableVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTableVoltageValue.setStatus("current")
_AcsPowerMgmtBanksTableVoltageMax_Type = Integer32
_AcsPowerMgmtBanksTableVoltageMax_Object = MibTableColumn
acsPowerMgmtBanksTableVoltageMax = _AcsPowerMgmtBanksTableVoltageMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 9, 1, 14),
    _AcsPowerMgmtBanksTableVoltageMax_Type()
)
acsPowerMgmtBanksTableVoltageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTableVoltageMax.setStatus("current")
_AcsPowerMgmtBanksTableVoltageMin_Type = Integer32
_AcsPowerMgmtBanksTableVoltageMin_Object = MibTableColumn
acsPowerMgmtBanksTableVoltageMin = _AcsPowerMgmtBanksTableVoltageMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 9, 1, 15),
    _AcsPowerMgmtBanksTableVoltageMin_Type()
)
acsPowerMgmtBanksTableVoltageMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTableVoltageMin.setStatus("current")
_AcsPowerMgmtBanksTableVoltageAvg_Type = Integer32
_AcsPowerMgmtBanksTableVoltageAvg_Object = MibTableColumn
acsPowerMgmtBanksTableVoltageAvg = _AcsPowerMgmtBanksTableVoltageAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 9, 1, 16),
    _AcsPowerMgmtBanksTableVoltageAvg_Type()
)
acsPowerMgmtBanksTableVoltageAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTableVoltageAvg.setStatus("current")


class _AcsPowerMgmtBanksTableVoltageReset_Type(Integer32):
    """Custom type acsPowerMgmtBanksTableVoltageReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-action", 1),
          ("reset", 2))
    )


_AcsPowerMgmtBanksTableVoltageReset_Type.__name__ = "Integer32"
_AcsPowerMgmtBanksTableVoltageReset_Object = MibTableColumn
acsPowerMgmtBanksTableVoltageReset = _AcsPowerMgmtBanksTableVoltageReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 9, 1, 17),
    _AcsPowerMgmtBanksTableVoltageReset_Type()
)
acsPowerMgmtBanksTableVoltageReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTableVoltageReset.setStatus("current")


class _AcsPowerMgmtBanksTablePowerType_Type(Integer32):
    """Custom type acsPowerMgmtBanksTablePowerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none-sensor", 0),
          ("estimated", 1),
          ("read", 2))
    )


_AcsPowerMgmtBanksTablePowerType_Type.__name__ = "Integer32"
_AcsPowerMgmtBanksTablePowerType_Object = MibTableColumn
acsPowerMgmtBanksTablePowerType = _AcsPowerMgmtBanksTablePowerType_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 9, 1, 18),
    _AcsPowerMgmtBanksTablePowerType_Type()
)
acsPowerMgmtBanksTablePowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTablePowerType.setStatus("current")
_AcsPowerMgmtBanksTablePowerValue_Type = Integer32
_AcsPowerMgmtBanksTablePowerValue_Object = MibTableColumn
acsPowerMgmtBanksTablePowerValue = _AcsPowerMgmtBanksTablePowerValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 9, 1, 19),
    _AcsPowerMgmtBanksTablePowerValue_Type()
)
acsPowerMgmtBanksTablePowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTablePowerValue.setStatus("current")
_AcsPowerMgmtBanksTablePowerMax_Type = Integer32
_AcsPowerMgmtBanksTablePowerMax_Object = MibTableColumn
acsPowerMgmtBanksTablePowerMax = _AcsPowerMgmtBanksTablePowerMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 9, 1, 20),
    _AcsPowerMgmtBanksTablePowerMax_Type()
)
acsPowerMgmtBanksTablePowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTablePowerMax.setStatus("current")
_AcsPowerMgmtBanksTablePowerMin_Type = Integer32
_AcsPowerMgmtBanksTablePowerMin_Object = MibTableColumn
acsPowerMgmtBanksTablePowerMin = _AcsPowerMgmtBanksTablePowerMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 9, 1, 21),
    _AcsPowerMgmtBanksTablePowerMin_Type()
)
acsPowerMgmtBanksTablePowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTablePowerMin.setStatus("current")
_AcsPowerMgmtBanksTablePowerAvg_Type = Integer32
_AcsPowerMgmtBanksTablePowerAvg_Object = MibTableColumn
acsPowerMgmtBanksTablePowerAvg = _AcsPowerMgmtBanksTablePowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 9, 1, 22),
    _AcsPowerMgmtBanksTablePowerAvg_Type()
)
acsPowerMgmtBanksTablePowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTablePowerAvg.setStatus("current")


class _AcsPowerMgmtBanksTablePowerReset_Type(Integer32):
    """Custom type acsPowerMgmtBanksTablePowerReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-action", 1),
          ("reset", 2))
    )


_AcsPowerMgmtBanksTablePowerReset_Type.__name__ = "Integer32"
_AcsPowerMgmtBanksTablePowerReset_Object = MibTableColumn
acsPowerMgmtBanksTablePowerReset = _AcsPowerMgmtBanksTablePowerReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 9, 1, 23),
    _AcsPowerMgmtBanksTablePowerReset_Type()
)
acsPowerMgmtBanksTablePowerReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTablePowerReset.setStatus("current")


class _AcsPowerMgmtBanksTablePowerFactorType_Type(Integer32):
    """Custom type acsPowerMgmtBanksTablePowerFactorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none-sensor", 0),
          ("estimated", 1),
          ("read", 2))
    )


_AcsPowerMgmtBanksTablePowerFactorType_Type.__name__ = "Integer32"
_AcsPowerMgmtBanksTablePowerFactorType_Object = MibTableColumn
acsPowerMgmtBanksTablePowerFactorType = _AcsPowerMgmtBanksTablePowerFactorType_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 9, 1, 24),
    _AcsPowerMgmtBanksTablePowerFactorType_Type()
)
acsPowerMgmtBanksTablePowerFactorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTablePowerFactorType.setStatus("current")
_AcsPowerMgmtBanksTablePowerFactorValue_Type = Integer32
_AcsPowerMgmtBanksTablePowerFactorValue_Object = MibTableColumn
acsPowerMgmtBanksTablePowerFactorValue = _AcsPowerMgmtBanksTablePowerFactorValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 9, 1, 25),
    _AcsPowerMgmtBanksTablePowerFactorValue_Type()
)
acsPowerMgmtBanksTablePowerFactorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTablePowerFactorValue.setStatus("current")
_AcsPowerMgmtBanksTablePowerFactorMax_Type = Integer32
_AcsPowerMgmtBanksTablePowerFactorMax_Object = MibTableColumn
acsPowerMgmtBanksTablePowerFactorMax = _AcsPowerMgmtBanksTablePowerFactorMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 9, 1, 26),
    _AcsPowerMgmtBanksTablePowerFactorMax_Type()
)
acsPowerMgmtBanksTablePowerFactorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTablePowerFactorMax.setStatus("current")
_AcsPowerMgmtBanksTablePowerFactorMin_Type = Integer32
_AcsPowerMgmtBanksTablePowerFactorMin_Object = MibTableColumn
acsPowerMgmtBanksTablePowerFactorMin = _AcsPowerMgmtBanksTablePowerFactorMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 9, 1, 27),
    _AcsPowerMgmtBanksTablePowerFactorMin_Type()
)
acsPowerMgmtBanksTablePowerFactorMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTablePowerFactorMin.setStatus("current")
_AcsPowerMgmtBanksTablePowerFactorAvg_Type = Integer32
_AcsPowerMgmtBanksTablePowerFactorAvg_Object = MibTableColumn
acsPowerMgmtBanksTablePowerFactorAvg = _AcsPowerMgmtBanksTablePowerFactorAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 9, 1, 28),
    _AcsPowerMgmtBanksTablePowerFactorAvg_Type()
)
acsPowerMgmtBanksTablePowerFactorAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTablePowerFactorAvg.setStatus("current")


class _AcsPowerMgmtBanksTablePowerFactorReset_Type(Integer32):
    """Custom type acsPowerMgmtBanksTablePowerFactorReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-action", 1),
          ("reset", 2))
    )


_AcsPowerMgmtBanksTablePowerFactorReset_Type.__name__ = "Integer32"
_AcsPowerMgmtBanksTablePowerFactorReset_Object = MibTableColumn
acsPowerMgmtBanksTablePowerFactorReset = _AcsPowerMgmtBanksTablePowerFactorReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 9, 1, 29),
    _AcsPowerMgmtBanksTablePowerFactorReset_Type()
)
acsPowerMgmtBanksTablePowerFactorReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTablePowerFactorReset.setStatus("current")


class _AcsPowerMgmtBanksTableAlarm_Type(Integer32):
    """Custom type acsPowerMgmtBanksTableAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("blow-fuse", 2),
          ("hw-ocp", 3),
          ("high-critical", 4),
          ("high-warning", 5),
          ("low-warning", 6),
          ("low-critical", 7))
    )


_AcsPowerMgmtBanksTableAlarm_Type.__name__ = "Integer32"
_AcsPowerMgmtBanksTableAlarm_Object = MibTableColumn
acsPowerMgmtBanksTableAlarm = _AcsPowerMgmtBanksTableAlarm_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 9, 1, 30),
    _AcsPowerMgmtBanksTableAlarm_Type()
)
acsPowerMgmtBanksTableAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTableAlarm.setStatus("current")
_AcsPowerMgmtEnvMonTable_Object = MibTable
acsPowerMgmtEnvMonTable = _AcsPowerMgmtEnvMonTable_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 10)
)
if mibBuilder.loadTexts:
    acsPowerMgmtEnvMonTable.setStatus("current")
_AcsPowerMgmtEnvMonTableEntry_Object = MibTableRow
acsPowerMgmtEnvMonTableEntry = _AcsPowerMgmtEnvMonTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 10, 1)
)
acsPowerMgmtEnvMonTableEntry.setIndexNames(
    (0, "ACS8000-MIB", "acsPowerMgmtEnvMonTablePortNumber"),
    (0, "ACS8000-MIB", "acsPowerMgmtEnvMonTablePduIndex"),
    (0, "ACS8000-MIB", "acsPowerMgmtEnvMonTableIndex"),
)
if mibBuilder.loadTexts:
    acsPowerMgmtEnvMonTableEntry.setStatus("current")
_AcsPowerMgmtEnvMonTablePortNumber_Type = InterfaceIndex
_AcsPowerMgmtEnvMonTablePortNumber_Object = MibTableColumn
acsPowerMgmtEnvMonTablePortNumber = _AcsPowerMgmtEnvMonTablePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 10, 1, 1),
    _AcsPowerMgmtEnvMonTablePortNumber_Type()
)
acsPowerMgmtEnvMonTablePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtEnvMonTablePortNumber.setStatus("current")
_AcsPowerMgmtEnvMonTablePduIndex_Type = InterfaceIndexOrZero
_AcsPowerMgmtEnvMonTablePduIndex_Object = MibTableColumn
acsPowerMgmtEnvMonTablePduIndex = _AcsPowerMgmtEnvMonTablePduIndex_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 10, 1, 2),
    _AcsPowerMgmtEnvMonTablePduIndex_Type()
)
acsPowerMgmtEnvMonTablePduIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtEnvMonTablePduIndex.setStatus("current")
_AcsPowerMgmtEnvMonTableIndex_Type = InterfaceIndexOrZero
_AcsPowerMgmtEnvMonTableIndex_Object = MibTableColumn
acsPowerMgmtEnvMonTableIndex = _AcsPowerMgmtEnvMonTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 10, 1, 3),
    _AcsPowerMgmtEnvMonTableIndex_Type()
)
acsPowerMgmtEnvMonTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtEnvMonTableIndex.setStatus("current")
_AcsPowerMgmtEnvMonTableName_Type = DisplayString
_AcsPowerMgmtEnvMonTableName_Object = MibTableColumn
acsPowerMgmtEnvMonTableName = _AcsPowerMgmtEnvMonTableName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 10, 1, 4),
    _AcsPowerMgmtEnvMonTableName_Type()
)
acsPowerMgmtEnvMonTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtEnvMonTableName.setStatus("current")
_AcsPowerMgmtEnvMonTablePduId_Type = DisplayString
_AcsPowerMgmtEnvMonTablePduId_Object = MibTableColumn
acsPowerMgmtEnvMonTablePduId = _AcsPowerMgmtEnvMonTablePduId_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 10, 1, 5),
    _AcsPowerMgmtEnvMonTablePduId_Type()
)
acsPowerMgmtEnvMonTablePduId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtEnvMonTablePduId.setStatus("current")
_AcsPowerMgmtEnvMonTablePortName_Type = DisplayString
_AcsPowerMgmtEnvMonTablePortName_Object = MibTableColumn
acsPowerMgmtEnvMonTablePortName = _AcsPowerMgmtEnvMonTablePortName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 10, 1, 6),
    _AcsPowerMgmtEnvMonTablePortName_Type()
)
acsPowerMgmtEnvMonTablePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtEnvMonTablePortName.setStatus("current")


class _AcsPowerMgmtEnvMonTableType_Type(Integer32):
    """Custom type acsPowerMgmtEnvMonTableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("temp-internal", 1),
          ("temperature", 2),
          ("humidity", 3),
          ("air-flow", 4),
          ("smoke", 5),
          ("dry-contact", 6),
          ("water-level", 7),
          ("motion", 8),
          ("unplugged", 9),
          ("unknown", 10),
          ("air-pressure", 11),
          ("vibration", 12),
          ("vibration-contact", 13),
          ("leak", 14),
          ("door-contact", 15),
          ("dewpoint", 16),
          ("ad-converter", 17),
          ("voltage", 18),
          ("current", 19))
    )


_AcsPowerMgmtEnvMonTableType_Type.__name__ = "Integer32"
_AcsPowerMgmtEnvMonTableType_Object = MibTableColumn
acsPowerMgmtEnvMonTableType = _AcsPowerMgmtEnvMonTableType_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 10, 1, 7),
    _AcsPowerMgmtEnvMonTableType_Type()
)
acsPowerMgmtEnvMonTableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtEnvMonTableType.setStatus("current")


class _AcsPowerMgmtEnvMonTableStatus_Type(Integer32):
    """Custom type acsPowerMgmtEnvMonTableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("triggered", 2),
          ("not-applicable", 3),
          ("leak", 4),
          ("cableFault", 5))
    )


_AcsPowerMgmtEnvMonTableStatus_Type.__name__ = "Integer32"
_AcsPowerMgmtEnvMonTableStatus_Object = MibTableColumn
acsPowerMgmtEnvMonTableStatus = _AcsPowerMgmtEnvMonTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 10, 1, 8),
    _AcsPowerMgmtEnvMonTableStatus_Type()
)
acsPowerMgmtEnvMonTableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtEnvMonTableStatus.setStatus("current")
_AcsPowerMgmtEnvMonTableValue_Type = Integer32
_AcsPowerMgmtEnvMonTableValue_Object = MibTableColumn
acsPowerMgmtEnvMonTableValue = _AcsPowerMgmtEnvMonTableValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 10, 1, 9),
    _AcsPowerMgmtEnvMonTableValue_Type()
)
acsPowerMgmtEnvMonTableValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtEnvMonTableValue.setStatus("current")
_AcsPowerMgmtEnvMonTableMaxValue_Type = Integer32
_AcsPowerMgmtEnvMonTableMaxValue_Object = MibTableColumn
acsPowerMgmtEnvMonTableMaxValue = _AcsPowerMgmtEnvMonTableMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 10, 1, 10),
    _AcsPowerMgmtEnvMonTableMaxValue_Type()
)
acsPowerMgmtEnvMonTableMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtEnvMonTableMaxValue.setStatus("current")
_AcsPowerMgmtOutElecMonTable_Object = MibTable
acsPowerMgmtOutElecMonTable = _AcsPowerMgmtOutElecMonTable_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 11)
)
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTable.setStatus("current")
_AcsPowerMgmtOutElecMonTableEntry_Object = MibTableRow
acsPowerMgmtOutElecMonTableEntry = _AcsPowerMgmtOutElecMonTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 11, 1)
)
acsPowerMgmtOutElecMonTableEntry.setIndexNames(
    (0, "ACS8000-MIB", "acsPowerMgmtOutElecMonTablePortNumber"),
    (0, "ACS8000-MIB", "acsPowerMgmtOutElecMonTablePduNumber"),
    (0, "ACS8000-MIB", "acsPowerMgmtOutElecMonTableNumber"),
)
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTableEntry.setStatus("current")
_AcsPowerMgmtOutElecMonTablePortNumber_Type = InterfaceIndex
_AcsPowerMgmtOutElecMonTablePortNumber_Object = MibTableColumn
acsPowerMgmtOutElecMonTablePortNumber = _AcsPowerMgmtOutElecMonTablePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 11, 1, 1),
    _AcsPowerMgmtOutElecMonTablePortNumber_Type()
)
acsPowerMgmtOutElecMonTablePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTablePortNumber.setStatus("current")
_AcsPowerMgmtOutElecMonTablePduNumber_Type = InterfaceIndex
_AcsPowerMgmtOutElecMonTablePduNumber_Object = MibTableColumn
acsPowerMgmtOutElecMonTablePduNumber = _AcsPowerMgmtOutElecMonTablePduNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 11, 1, 2),
    _AcsPowerMgmtOutElecMonTablePduNumber_Type()
)
acsPowerMgmtOutElecMonTablePduNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTablePduNumber.setStatus("current")
_AcsPowerMgmtOutElecMonTableNumber_Type = InterfaceIndex
_AcsPowerMgmtOutElecMonTableNumber_Object = MibTableColumn
acsPowerMgmtOutElecMonTableNumber = _AcsPowerMgmtOutElecMonTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 11, 1, 3),
    _AcsPowerMgmtOutElecMonTableNumber_Type()
)
acsPowerMgmtOutElecMonTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTableNumber.setStatus("current")
_AcsPowerMgmtOutElecMonTableCurrentValue_Type = Integer32
_AcsPowerMgmtOutElecMonTableCurrentValue_Object = MibTableColumn
acsPowerMgmtOutElecMonTableCurrentValue = _AcsPowerMgmtOutElecMonTableCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 11, 1, 4),
    _AcsPowerMgmtOutElecMonTableCurrentValue_Type()
)
acsPowerMgmtOutElecMonTableCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTableCurrentValue.setStatus("current")
_AcsPowerMgmtOutElecMonTableCurrentMax_Type = Integer32
_AcsPowerMgmtOutElecMonTableCurrentMax_Object = MibTableColumn
acsPowerMgmtOutElecMonTableCurrentMax = _AcsPowerMgmtOutElecMonTableCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 11, 1, 5),
    _AcsPowerMgmtOutElecMonTableCurrentMax_Type()
)
acsPowerMgmtOutElecMonTableCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTableCurrentMax.setStatus("current")
_AcsPowerMgmtOutElecMonTableCurrentMin_Type = Integer32
_AcsPowerMgmtOutElecMonTableCurrentMin_Object = MibTableColumn
acsPowerMgmtOutElecMonTableCurrentMin = _AcsPowerMgmtOutElecMonTableCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 11, 1, 6),
    _AcsPowerMgmtOutElecMonTableCurrentMin_Type()
)
acsPowerMgmtOutElecMonTableCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTableCurrentMin.setStatus("current")
_AcsPowerMgmtOutElecMonTableCurrentAvg_Type = Integer32
_AcsPowerMgmtOutElecMonTableCurrentAvg_Object = MibTableColumn
acsPowerMgmtOutElecMonTableCurrentAvg = _AcsPowerMgmtOutElecMonTableCurrentAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 11, 1, 7),
    _AcsPowerMgmtOutElecMonTableCurrentAvg_Type()
)
acsPowerMgmtOutElecMonTableCurrentAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTableCurrentAvg.setStatus("current")


class _AcsPowerMgmtOutElecMonTableCurrentReset_Type(Integer32):
    """Custom type acsPowerMgmtOutElecMonTableCurrentReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("reset", 2))
    )


_AcsPowerMgmtOutElecMonTableCurrentReset_Type.__name__ = "Integer32"
_AcsPowerMgmtOutElecMonTableCurrentReset_Object = MibTableColumn
acsPowerMgmtOutElecMonTableCurrentReset = _AcsPowerMgmtOutElecMonTableCurrentReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 11, 1, 8),
    _AcsPowerMgmtOutElecMonTableCurrentReset_Type()
)
acsPowerMgmtOutElecMonTableCurrentReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTableCurrentReset.setStatus("current")
_AcsPowerMgmtOutElecMonTablePowerValue_Type = Integer32
_AcsPowerMgmtOutElecMonTablePowerValue_Object = MibTableColumn
acsPowerMgmtOutElecMonTablePowerValue = _AcsPowerMgmtOutElecMonTablePowerValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 11, 1, 9),
    _AcsPowerMgmtOutElecMonTablePowerValue_Type()
)
acsPowerMgmtOutElecMonTablePowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTablePowerValue.setStatus("current")
_AcsPowerMgmtOutElecMonTablePowerMax_Type = Integer32
_AcsPowerMgmtOutElecMonTablePowerMax_Object = MibTableColumn
acsPowerMgmtOutElecMonTablePowerMax = _AcsPowerMgmtOutElecMonTablePowerMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 11, 1, 10),
    _AcsPowerMgmtOutElecMonTablePowerMax_Type()
)
acsPowerMgmtOutElecMonTablePowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTablePowerMax.setStatus("current")
_AcsPowerMgmtOutElecMonTablePowerMin_Type = Integer32
_AcsPowerMgmtOutElecMonTablePowerMin_Object = MibTableColumn
acsPowerMgmtOutElecMonTablePowerMin = _AcsPowerMgmtOutElecMonTablePowerMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 11, 1, 11),
    _AcsPowerMgmtOutElecMonTablePowerMin_Type()
)
acsPowerMgmtOutElecMonTablePowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTablePowerMin.setStatus("current")
_AcsPowerMgmtOutElecMonTablePowerAvg_Type = Integer32
_AcsPowerMgmtOutElecMonTablePowerAvg_Object = MibTableColumn
acsPowerMgmtOutElecMonTablePowerAvg = _AcsPowerMgmtOutElecMonTablePowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 11, 1, 12),
    _AcsPowerMgmtOutElecMonTablePowerAvg_Type()
)
acsPowerMgmtOutElecMonTablePowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTablePowerAvg.setStatus("current")


class _AcsPowerMgmtOutElecMonTablePowerReset_Type(Integer32):
    """Custom type acsPowerMgmtOutElecMonTablePowerReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("reset", 2))
    )


_AcsPowerMgmtOutElecMonTablePowerReset_Type.__name__ = "Integer32"
_AcsPowerMgmtOutElecMonTablePowerReset_Object = MibTableColumn
acsPowerMgmtOutElecMonTablePowerReset = _AcsPowerMgmtOutElecMonTablePowerReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 11, 1, 13),
    _AcsPowerMgmtOutElecMonTablePowerReset_Type()
)
acsPowerMgmtOutElecMonTablePowerReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTablePowerReset.setStatus("current")
_AcsPowerMgmtOutElecMonTableVoltageValue_Type = Integer32
_AcsPowerMgmtOutElecMonTableVoltageValue_Object = MibTableColumn
acsPowerMgmtOutElecMonTableVoltageValue = _AcsPowerMgmtOutElecMonTableVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 11, 1, 14),
    _AcsPowerMgmtOutElecMonTableVoltageValue_Type()
)
acsPowerMgmtOutElecMonTableVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTableVoltageValue.setStatus("current")
_AcsPowerMgmtOutElecMonTableVoltageMax_Type = Integer32
_AcsPowerMgmtOutElecMonTableVoltageMax_Object = MibTableColumn
acsPowerMgmtOutElecMonTableVoltageMax = _AcsPowerMgmtOutElecMonTableVoltageMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 11, 1, 15),
    _AcsPowerMgmtOutElecMonTableVoltageMax_Type()
)
acsPowerMgmtOutElecMonTableVoltageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTableVoltageMax.setStatus("current")
_AcsPowerMgmtOutElecMonTableVoltageMin_Type = Integer32
_AcsPowerMgmtOutElecMonTableVoltageMin_Object = MibTableColumn
acsPowerMgmtOutElecMonTableVoltageMin = _AcsPowerMgmtOutElecMonTableVoltageMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 11, 1, 16),
    _AcsPowerMgmtOutElecMonTableVoltageMin_Type()
)
acsPowerMgmtOutElecMonTableVoltageMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTableVoltageMin.setStatus("current")
_AcsPowerMgmtOutElecMonTableVoltageAvg_Type = Integer32
_AcsPowerMgmtOutElecMonTableVoltageAvg_Object = MibTableColumn
acsPowerMgmtOutElecMonTableVoltageAvg = _AcsPowerMgmtOutElecMonTableVoltageAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 11, 1, 17),
    _AcsPowerMgmtOutElecMonTableVoltageAvg_Type()
)
acsPowerMgmtOutElecMonTableVoltageAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTableVoltageAvg.setStatus("current")


class _AcsPowerMgmtOutElecMonTableVoltageReset_Type(Integer32):
    """Custom type acsPowerMgmtOutElecMonTableVoltageReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("reset", 2))
    )


_AcsPowerMgmtOutElecMonTableVoltageReset_Type.__name__ = "Integer32"
_AcsPowerMgmtOutElecMonTableVoltageReset_Object = MibTableColumn
acsPowerMgmtOutElecMonTableVoltageReset = _AcsPowerMgmtOutElecMonTableVoltageReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 11, 1, 18),
    _AcsPowerMgmtOutElecMonTableVoltageReset_Type()
)
acsPowerMgmtOutElecMonTableVoltageReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTableVoltageReset.setStatus("current")
_AcsPowerMgmtOutElecMonTablePowerFactorValue_Type = Integer32
_AcsPowerMgmtOutElecMonTablePowerFactorValue_Object = MibTableColumn
acsPowerMgmtOutElecMonTablePowerFactorValue = _AcsPowerMgmtOutElecMonTablePowerFactorValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 11, 1, 19),
    _AcsPowerMgmtOutElecMonTablePowerFactorValue_Type()
)
acsPowerMgmtOutElecMonTablePowerFactorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTablePowerFactorValue.setStatus("current")
_AcsPowerMgmtOutElecMonTablePowerFactorMax_Type = Integer32
_AcsPowerMgmtOutElecMonTablePowerFactorMax_Object = MibTableColumn
acsPowerMgmtOutElecMonTablePowerFactorMax = _AcsPowerMgmtOutElecMonTablePowerFactorMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 11, 1, 20),
    _AcsPowerMgmtOutElecMonTablePowerFactorMax_Type()
)
acsPowerMgmtOutElecMonTablePowerFactorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTablePowerFactorMax.setStatus("current")
_AcsPowerMgmtOutElecMonTablePowerFactorMin_Type = Integer32
_AcsPowerMgmtOutElecMonTablePowerFactorMin_Object = MibTableColumn
acsPowerMgmtOutElecMonTablePowerFactorMin = _AcsPowerMgmtOutElecMonTablePowerFactorMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 11, 1, 21),
    _AcsPowerMgmtOutElecMonTablePowerFactorMin_Type()
)
acsPowerMgmtOutElecMonTablePowerFactorMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTablePowerFactorMin.setStatus("current")
_AcsPowerMgmtOutElecMonTablePowerFactorAvg_Type = Integer32
_AcsPowerMgmtOutElecMonTablePowerFactorAvg_Object = MibTableColumn
acsPowerMgmtOutElecMonTablePowerFactorAvg = _AcsPowerMgmtOutElecMonTablePowerFactorAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 11, 1, 22),
    _AcsPowerMgmtOutElecMonTablePowerFactorAvg_Type()
)
acsPowerMgmtOutElecMonTablePowerFactorAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTablePowerFactorAvg.setStatus("current")


class _AcsPowerMgmtOutElecMonTablePowerFactorReset_Type(Integer32):
    """Custom type acsPowerMgmtOutElecMonTablePowerFactorReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("reset", 2))
    )


_AcsPowerMgmtOutElecMonTablePowerFactorReset_Type.__name__ = "Integer32"
_AcsPowerMgmtOutElecMonTablePowerFactorReset_Object = MibTableColumn
acsPowerMgmtOutElecMonTablePowerFactorReset = _AcsPowerMgmtOutElecMonTablePowerFactorReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 11, 1, 23),
    _AcsPowerMgmtOutElecMonTablePowerFactorReset_Type()
)
acsPowerMgmtOutElecMonTablePowerFactorReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTablePowerFactorReset.setStatus("current")


class _AcsPowerMgmtOutElecMonTableAlarm_Type(Integer32):
    """Custom type acsPowerMgmtOutElecMonTableAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("blow-fuse", 2),
          ("hw-ocp", 3),
          ("high-critical", 4),
          ("high-warning", 5),
          ("low-warning", 6),
          ("low-critical", 7))
    )


_AcsPowerMgmtOutElecMonTableAlarm_Type.__name__ = "Integer32"
_AcsPowerMgmtOutElecMonTableAlarm_Object = MibTableColumn
acsPowerMgmtOutElecMonTableAlarm = _AcsPowerMgmtOutElecMonTableAlarm_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 11, 1, 24),
    _AcsPowerMgmtOutElecMonTableAlarm_Type()
)
acsPowerMgmtOutElecMonTableAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTableAlarm.setStatus("current")
_AcsPowerMgmtUPSTable_Object = MibTable
acsPowerMgmtUPSTable = _AcsPowerMgmtUPSTable_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 12)
)
if mibBuilder.loadTexts:
    acsPowerMgmtUPSTable.setStatus("current")
_AcsPowerMgmtUPSTableEntry_Object = MibTableRow
acsPowerMgmtUPSTableEntry = _AcsPowerMgmtUPSTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 12, 1)
)
acsPowerMgmtUPSTableEntry.setIndexNames(
    (0, "ACS8000-MIB", "acsPowerMgmtUPSTablePortNumber"),
    (0, "ACS8000-MIB", "acsPowerMgmtUPSTableUpsIndex"),
)
if mibBuilder.loadTexts:
    acsPowerMgmtUPSTableEntry.setStatus("current")
_AcsPowerMgmtUPSTablePortNumber_Type = InterfaceIndex
_AcsPowerMgmtUPSTablePortNumber_Object = MibTableColumn
acsPowerMgmtUPSTablePortNumber = _AcsPowerMgmtUPSTablePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 12, 1, 1),
    _AcsPowerMgmtUPSTablePortNumber_Type()
)
acsPowerMgmtUPSTablePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSTablePortNumber.setStatus("current")
_AcsPowerMgmtUPSTableUpsIndex_Type = InterfaceIndexOrZero
_AcsPowerMgmtUPSTableUpsIndex_Object = MibTableColumn
acsPowerMgmtUPSTableUpsIndex = _AcsPowerMgmtUPSTableUpsIndex_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 12, 1, 2),
    _AcsPowerMgmtUPSTableUpsIndex_Type()
)
acsPowerMgmtUPSTableUpsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSTableUpsIndex.setStatus("current")
_AcsPowerMgmtUPSTableUpsId_Type = DisplayString
_AcsPowerMgmtUPSTableUpsId_Object = MibTableColumn
acsPowerMgmtUPSTableUpsId = _AcsPowerMgmtUPSTableUpsId_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 12, 1, 3),
    _AcsPowerMgmtUPSTableUpsId_Type()
)
acsPowerMgmtUPSTableUpsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSTableUpsId.setStatus("current")
_AcsPowerMgmtUPSTablePortName_Type = DisplayString
_AcsPowerMgmtUPSTablePortName_Object = MibTableColumn
acsPowerMgmtUPSTablePortName = _AcsPowerMgmtUPSTablePortName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 12, 1, 4),
    _AcsPowerMgmtUPSTablePortName_Type()
)
acsPowerMgmtUPSTablePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSTablePortName.setStatus("current")
_AcsPowerMgmtUPSTableModel_Type = DisplayString
_AcsPowerMgmtUPSTableModel_Object = MibTableColumn
acsPowerMgmtUPSTableModel = _AcsPowerMgmtUPSTableModel_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 12, 1, 5),
    _AcsPowerMgmtUPSTableModel_Type()
)
acsPowerMgmtUPSTableModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSTableModel.setStatus("current")
_AcsPowerMgmtUPSTableVendor_Type = DisplayString
_AcsPowerMgmtUPSTableVendor_Object = MibTableColumn
acsPowerMgmtUPSTableVendor = _AcsPowerMgmtUPSTableVendor_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 12, 1, 6),
    _AcsPowerMgmtUPSTableVendor_Type()
)
acsPowerMgmtUPSTableVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSTableVendor.setStatus("current")
_AcsPowerMgmtUPSTableFirmwareVersion_Type = DisplayString
_AcsPowerMgmtUPSTableFirmwareVersion_Object = MibTableColumn
acsPowerMgmtUPSTableFirmwareVersion = _AcsPowerMgmtUPSTableFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 12, 1, 7),
    _AcsPowerMgmtUPSTableFirmwareVersion_Type()
)
acsPowerMgmtUPSTableFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSTableFirmwareVersion.setStatus("current")
_AcsPowerMgmtUPSTableAgentFirmwareVersion_Type = DisplayString
_AcsPowerMgmtUPSTableAgentFirmwareVersion_Object = MibTableColumn
acsPowerMgmtUPSTableAgentFirmwareVersion = _AcsPowerMgmtUPSTableAgentFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 12, 1, 8),
    _AcsPowerMgmtUPSTableAgentFirmwareVersion_Type()
)
acsPowerMgmtUPSTableAgentFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSTableAgentFirmwareVersion.setStatus("current")
_AcsPowerMgmtUPSTableSystemStatus_Type = DisplayString
_AcsPowerMgmtUPSTableSystemStatus_Object = MibTableColumn
acsPowerMgmtUPSTableSystemStatus = _AcsPowerMgmtUPSTableSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 12, 1, 9),
    _AcsPowerMgmtUPSTableSystemStatus_Type()
)
acsPowerMgmtUPSTableSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSTableSystemStatus.setStatus("current")
_AcsPowerMgmtUPSTableInputBlackOutCount_Type = Integer32
_AcsPowerMgmtUPSTableInputBlackOutCount_Object = MibTableColumn
acsPowerMgmtUPSTableInputBlackOutCount = _AcsPowerMgmtUPSTableInputBlackOutCount_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 12, 1, 10),
    _AcsPowerMgmtUPSTableInputBlackOutCount_Type()
)
acsPowerMgmtUPSTableInputBlackOutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSTableInputBlackOutCount.setStatus("current")
_AcsPowerMgmtUPSTableInputBrownOutCount_Type = Integer32
_AcsPowerMgmtUPSTableInputBrownOutCount_Object = MibTableColumn
acsPowerMgmtUPSTableInputBrownOutCount = _AcsPowerMgmtUPSTableInputBrownOutCount_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 12, 1, 11),
    _AcsPowerMgmtUPSTableInputBrownOutCount_Type()
)
acsPowerMgmtUPSTableInputBrownOutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSTableInputBrownOutCount.setStatus("current")
_AcsPowerMgmtUPSTableInletAirTemperature_Type = DisplayString
_AcsPowerMgmtUPSTableInletAirTemperature_Object = MibTableColumn
acsPowerMgmtUPSTableInletAirTemperature = _AcsPowerMgmtUPSTableInletAirTemperature_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 12, 1, 12),
    _AcsPowerMgmtUPSTableInletAirTemperature_Type()
)
acsPowerMgmtUPSTableInletAirTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSTableInletAirTemperature.setStatus("current")
_AcsPowerMgmtUPSTableNumberOutletGroups_Type = Integer32
_AcsPowerMgmtUPSTableNumberOutletGroups_Object = MibTableColumn
acsPowerMgmtUPSTableNumberOutletGroups = _AcsPowerMgmtUPSTableNumberOutletGroups_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 12, 1, 13),
    _AcsPowerMgmtUPSTableNumberOutletGroups_Type()
)
acsPowerMgmtUPSTableNumberOutletGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSTableNumberOutletGroups.setStatus("current")
_AcsPowerMgmtUPSTableUPSSerialNumber_Type = DisplayString
_AcsPowerMgmtUPSTableUPSSerialNumber_Object = MibTableColumn
acsPowerMgmtUPSTableUPSSerialNumber = _AcsPowerMgmtUPSTableUPSSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 12, 1, 14),
    _AcsPowerMgmtUPSTableUPSSerialNumber_Type()
)
acsPowerMgmtUPSTableUPSSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSTableUPSSerialNumber.setStatus("current")
_AcsPowerMgmtUPSTableUPSManufactureDate_Type = DisplayString
_AcsPowerMgmtUPSTableUPSManufactureDate_Object = MibTableColumn
acsPowerMgmtUPSTableUPSManufactureDate = _AcsPowerMgmtUPSTableUPSManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 12, 1, 15),
    _AcsPowerMgmtUPSTableUPSManufactureDate_Type()
)
acsPowerMgmtUPSTableUPSManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSTableUPSManufactureDate.setStatus("current")
_AcsPowerMgmtUPSTableAutoRestartDelay_Type = Integer32
_AcsPowerMgmtUPSTableAutoRestartDelay_Object = MibTableColumn
acsPowerMgmtUPSTableAutoRestartDelay = _AcsPowerMgmtUPSTableAutoRestartDelay_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 12, 1, 16),
    _AcsPowerMgmtUPSTableAutoRestartDelay_Type()
)
acsPowerMgmtUPSTableAutoRestartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSTableAutoRestartDelay.setStatus("current")


class _AcsPowerMgmtUPSTableAutoRestartControl_Type(Integer32):
    """Custom type acsPowerMgmtUPSTableAutoRestartControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AcsPowerMgmtUPSTableAutoRestartControl_Type.__name__ = "Integer32"
_AcsPowerMgmtUPSTableAutoRestartControl_Object = MibTableColumn
acsPowerMgmtUPSTableAutoRestartControl = _AcsPowerMgmtUPSTableAutoRestartControl_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 12, 1, 17),
    _AcsPowerMgmtUPSTableAutoRestartControl_Type()
)
acsPowerMgmtUPSTableAutoRestartControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSTableAutoRestartControl.setStatus("current")


class _AcsPowerMgmtUPSTableAudibleAlarmControl_Type(Integer32):
    """Custom type acsPowerMgmtUPSTableAudibleAlarmControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_AcsPowerMgmtUPSTableAudibleAlarmControl_Type.__name__ = "Integer32"
_AcsPowerMgmtUPSTableAudibleAlarmControl_Object = MibTableColumn
acsPowerMgmtUPSTableAudibleAlarmControl = _AcsPowerMgmtUPSTableAudibleAlarmControl_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 12, 1, 18),
    _AcsPowerMgmtUPSTableAudibleAlarmControl_Type()
)
acsPowerMgmtUPSTableAudibleAlarmControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSTableAudibleAlarmControl.setStatus("current")


class _AcsPowerMgmtUPSTableSilenceAlarm_Type(Integer32):
    """Custom type acsPowerMgmtUPSTableSilenceAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 0),
          ("silenceAlarm", 1))
    )


_AcsPowerMgmtUPSTableSilenceAlarm_Type.__name__ = "Integer32"
_AcsPowerMgmtUPSTableSilenceAlarm_Object = MibTableColumn
acsPowerMgmtUPSTableSilenceAlarm = _AcsPowerMgmtUPSTableSilenceAlarm_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 12, 1, 19),
    _AcsPowerMgmtUPSTableSilenceAlarm_Type()
)
acsPowerMgmtUPSTableSilenceAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSTableSilenceAlarm.setStatus("current")
_AcsPowerMgmtUPSTableInverterState_Type = DisplayString
_AcsPowerMgmtUPSTableInverterState_Object = MibTableColumn
acsPowerMgmtUPSTableInverterState = _AcsPowerMgmtUPSTableInverterState_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 12, 1, 20),
    _AcsPowerMgmtUPSTableInverterState_Type()
)
acsPowerMgmtUPSTableInverterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSTableInverterState.setStatus("current")
_AcsPowerMgmtUPSTableDCConverterStatus_Type = DisplayString
_AcsPowerMgmtUPSTableDCConverterStatus_Object = MibTableColumn
acsPowerMgmtUPSTableDCConverterStatus = _AcsPowerMgmtUPSTableDCConverterStatus_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 12, 1, 21),
    _AcsPowerMgmtUPSTableDCConverterStatus_Type()
)
acsPowerMgmtUPSTableDCConverterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSTableDCConverterStatus.setStatus("current")
_AcsPowerMgmtUPSTableShutdownReason_Type = DisplayString
_AcsPowerMgmtUPSTableShutdownReason_Object = MibTableColumn
acsPowerMgmtUPSTableShutdownReason = _AcsPowerMgmtUPSTableShutdownReason_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 12, 1, 22),
    _AcsPowerMgmtUPSTableShutdownReason_Type()
)
acsPowerMgmtUPSTableShutdownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSTableShutdownReason.setStatus("current")
_AcsPowerMgmtUPSTableUPSTopology_Type = DisplayString
_AcsPowerMgmtUPSTableUPSTopology_Object = MibTableColumn
acsPowerMgmtUPSTableUPSTopology = _AcsPowerMgmtUPSTableUPSTopology_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 12, 1, 23),
    _AcsPowerMgmtUPSTableUPSTopology_Type()
)
acsPowerMgmtUPSTableUPSTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSTableUPSTopology.setStatus("current")
_AcsPowerMgmtUPSTableBypassInverterInputConfig_Type = DisplayString
_AcsPowerMgmtUPSTableBypassInverterInputConfig_Object = MibTableColumn
acsPowerMgmtUPSTableBypassInverterInputConfig = _AcsPowerMgmtUPSTableBypassInverterInputConfig_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 12, 1, 24),
    _AcsPowerMgmtUPSTableBypassInverterInputConfig_Type()
)
acsPowerMgmtUPSTableBypassInverterInputConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSTableBypassInverterInputConfig.setStatus("current")
_AcsPowerMgmtUPSInputTable_Object = MibTable
acsPowerMgmtUPSInputTable = _AcsPowerMgmtUPSInputTable_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 13)
)
if mibBuilder.loadTexts:
    acsPowerMgmtUPSInputTable.setStatus("current")
_AcsPowerMgmtUPSInputTableEntry_Object = MibTableRow
acsPowerMgmtUPSInputTableEntry = _AcsPowerMgmtUPSInputTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 13, 1)
)
acsPowerMgmtUPSInputTableEntry.setIndexNames(
    (0, "ACS8000-MIB", "acsPowerMgmtUPSInputTablePortNumber"),
    (0, "ACS8000-MIB", "acsPowerMgmtUPSInputTableUpsIndex"),
)
if mibBuilder.loadTexts:
    acsPowerMgmtUPSInputTableEntry.setStatus("current")
_AcsPowerMgmtUPSInputTablePortNumber_Type = InterfaceIndex
_AcsPowerMgmtUPSInputTablePortNumber_Object = MibTableColumn
acsPowerMgmtUPSInputTablePortNumber = _AcsPowerMgmtUPSInputTablePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 13, 1, 1),
    _AcsPowerMgmtUPSInputTablePortNumber_Type()
)
acsPowerMgmtUPSInputTablePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSInputTablePortNumber.setStatus("current")
_AcsPowerMgmtUPSInputTableUpsIndex_Type = InterfaceIndex
_AcsPowerMgmtUPSInputTableUpsIndex_Object = MibTableColumn
acsPowerMgmtUPSInputTableUpsIndex = _AcsPowerMgmtUPSInputTableUpsIndex_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 13, 1, 2),
    _AcsPowerMgmtUPSInputTableUpsIndex_Type()
)
acsPowerMgmtUPSInputTableUpsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSInputTableUpsIndex.setStatus("current")
_AcsPowerMgmtUPSInputTableFrequency_Type = DisplayString
_AcsPowerMgmtUPSInputTableFrequency_Object = MibTableColumn
acsPowerMgmtUPSInputTableFrequency = _AcsPowerMgmtUPSInputTableFrequency_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 13, 1, 3),
    _AcsPowerMgmtUPSInputTableFrequency_Type()
)
acsPowerMgmtUPSInputTableFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSInputTableFrequency.setStatus("current")
_AcsPowerMgmtUPSInputTableRMSVoltageL1N_Type = DisplayString
_AcsPowerMgmtUPSInputTableRMSVoltageL1N_Object = MibTableColumn
acsPowerMgmtUPSInputTableRMSVoltageL1N = _AcsPowerMgmtUPSInputTableRMSVoltageL1N_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 13, 1, 4),
    _AcsPowerMgmtUPSInputTableRMSVoltageL1N_Type()
)
acsPowerMgmtUPSInputTableRMSVoltageL1N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSInputTableRMSVoltageL1N.setStatus("current")
_AcsPowerMgmtUPSInputTableRMSVoltageL1L2_Type = DisplayString
_AcsPowerMgmtUPSInputTableRMSVoltageL1L2_Object = MibTableColumn
acsPowerMgmtUPSInputTableRMSVoltageL1L2 = _AcsPowerMgmtUPSInputTableRMSVoltageL1L2_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 13, 1, 5),
    _AcsPowerMgmtUPSInputTableRMSVoltageL1L2_Type()
)
acsPowerMgmtUPSInputTableRMSVoltageL1L2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSInputTableRMSVoltageL1L2.setStatus("current")
_AcsPowerMgmtUPSInputTableRMSVoltageL2N_Type = DisplayString
_AcsPowerMgmtUPSInputTableRMSVoltageL2N_Object = MibTableColumn
acsPowerMgmtUPSInputTableRMSVoltageL2N = _AcsPowerMgmtUPSInputTableRMSVoltageL2N_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 13, 1, 6),
    _AcsPowerMgmtUPSInputTableRMSVoltageL2N_Type()
)
acsPowerMgmtUPSInputTableRMSVoltageL2N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSInputTableRMSVoltageL2N.setStatus("current")
_AcsPowerMgmtUPSInputTableRMSCurrentL1_Type = DisplayString
_AcsPowerMgmtUPSInputTableRMSCurrentL1_Object = MibTableColumn
acsPowerMgmtUPSInputTableRMSCurrentL1 = _AcsPowerMgmtUPSInputTableRMSCurrentL1_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 13, 1, 7),
    _AcsPowerMgmtUPSInputTableRMSCurrentL1_Type()
)
acsPowerMgmtUPSInputTableRMSCurrentL1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSInputTableRMSCurrentL1.setStatus("current")
_AcsPowerMgmtUPSInputTableRMSCurrentL2_Type = DisplayString
_AcsPowerMgmtUPSInputTableRMSCurrentL2_Object = MibTableColumn
acsPowerMgmtUPSInputTableRMSCurrentL2 = _AcsPowerMgmtUPSInputTableRMSCurrentL2_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 13, 1, 8),
    _AcsPowerMgmtUPSInputTableRMSCurrentL2_Type()
)
acsPowerMgmtUPSInputTableRMSCurrentL2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSInputTableRMSCurrentL2.setStatus("current")
_AcsPowerMgmtUPSInputTableMaxVoltageL1N_Type = DisplayString
_AcsPowerMgmtUPSInputTableMaxVoltageL1N_Object = MibTableColumn
acsPowerMgmtUPSInputTableMaxVoltageL1N = _AcsPowerMgmtUPSInputTableMaxVoltageL1N_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 13, 1, 9),
    _AcsPowerMgmtUPSInputTableMaxVoltageL1N_Type()
)
acsPowerMgmtUPSInputTableMaxVoltageL1N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSInputTableMaxVoltageL1N.setStatus("current")
_AcsPowerMgmtUPSInputTableMinVoltageL1N_Type = DisplayString
_AcsPowerMgmtUPSInputTableMinVoltageL1N_Object = MibTableColumn
acsPowerMgmtUPSInputTableMinVoltageL1N = _AcsPowerMgmtUPSInputTableMinVoltageL1N_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 13, 1, 10),
    _AcsPowerMgmtUPSInputTableMinVoltageL1N_Type()
)
acsPowerMgmtUPSInputTableMinVoltageL1N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSInputTableMinVoltageL1N.setStatus("current")
_AcsPowerMgmtUPSInputTableMaxVoltageL2N_Type = DisplayString
_AcsPowerMgmtUPSInputTableMaxVoltageL2N_Object = MibTableColumn
acsPowerMgmtUPSInputTableMaxVoltageL2N = _AcsPowerMgmtUPSInputTableMaxVoltageL2N_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 13, 1, 11),
    _AcsPowerMgmtUPSInputTableMaxVoltageL2N_Type()
)
acsPowerMgmtUPSInputTableMaxVoltageL2N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSInputTableMaxVoltageL2N.setStatus("current")
_AcsPowerMgmtUPSInputTableMinVoltageL2N_Type = DisplayString
_AcsPowerMgmtUPSInputTableMinVoltageL2N_Object = MibTableColumn
acsPowerMgmtUPSInputTableMinVoltageL2N = _AcsPowerMgmtUPSInputTableMinVoltageL2N_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 13, 1, 12),
    _AcsPowerMgmtUPSInputTableMinVoltageL2N_Type()
)
acsPowerMgmtUPSInputTableMinVoltageL2N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSInputTableMinVoltageL2N.setStatus("current")
_AcsPowerMgmtUPSInputTableNominalVoltage_Type = DisplayString
_AcsPowerMgmtUPSInputTableNominalVoltage_Object = MibTableColumn
acsPowerMgmtUPSInputTableNominalVoltage = _AcsPowerMgmtUPSInputTableNominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 13, 1, 13),
    _AcsPowerMgmtUPSInputTableNominalVoltage_Type()
)
acsPowerMgmtUPSInputTableNominalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSInputTableNominalVoltage.setStatus("current")
_AcsPowerMgmtUPSInputTableNominalFrequency_Type = DisplayString
_AcsPowerMgmtUPSInputTableNominalFrequency_Object = MibTableColumn
acsPowerMgmtUPSInputTableNominalFrequency = _AcsPowerMgmtUPSInputTableNominalFrequency_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 13, 1, 14),
    _AcsPowerMgmtUPSInputTableNominalFrequency_Type()
)
acsPowerMgmtUPSInputTableNominalFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSInputTableNominalFrequency.setStatus("current")
_AcsPowerMgmtUPSInputTableNominalCurrent_Type = DisplayString
_AcsPowerMgmtUPSInputTableNominalCurrent_Object = MibTableColumn
acsPowerMgmtUPSInputTableNominalCurrent = _AcsPowerMgmtUPSInputTableNominalCurrent_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 13, 1, 15),
    _AcsPowerMgmtUPSInputTableNominalCurrent_Type()
)
acsPowerMgmtUPSInputTableNominalCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSInputTableNominalCurrent.setStatus("current")
_AcsPowerMgmtUPSInputTableEnergy_Type = DisplayString
_AcsPowerMgmtUPSInputTableEnergy_Object = MibTableColumn
acsPowerMgmtUPSInputTableEnergy = _AcsPowerMgmtUPSInputTableEnergy_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 13, 1, 16),
    _AcsPowerMgmtUPSInputTableEnergy_Type()
)
acsPowerMgmtUPSInputTableEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSInputTableEnergy.setStatus("current")
_AcsPowerMgmtUPSInputTablePowerFactorL1N_Type = DisplayString
_AcsPowerMgmtUPSInputTablePowerFactorL1N_Object = MibTableColumn
acsPowerMgmtUPSInputTablePowerFactorL1N = _AcsPowerMgmtUPSInputTablePowerFactorL1N_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 13, 1, 17),
    _AcsPowerMgmtUPSInputTablePowerFactorL1N_Type()
)
acsPowerMgmtUPSInputTablePowerFactorL1N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSInputTablePowerFactorL1N.setStatus("current")
_AcsPowerMgmtUPSInputTablePowerFactorL2N_Type = DisplayString
_AcsPowerMgmtUPSInputTablePowerFactorL2N_Object = MibTableColumn
acsPowerMgmtUPSInputTablePowerFactorL2N = _AcsPowerMgmtUPSInputTablePowerFactorL2N_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 13, 1, 18),
    _AcsPowerMgmtUPSInputTablePowerFactorL2N_Type()
)
acsPowerMgmtUPSInputTablePowerFactorL2N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSInputTablePowerFactorL2N.setStatus("current")
_AcsPowerMgmtUPSBypassTable_Object = MibTable
acsPowerMgmtUPSBypassTable = _AcsPowerMgmtUPSBypassTable_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 14)
)
if mibBuilder.loadTexts:
    acsPowerMgmtUPSBypassTable.setStatus("current")
_AcsPowerMgmtUPSBypassTableEntry_Object = MibTableRow
acsPowerMgmtUPSBypassTableEntry = _AcsPowerMgmtUPSBypassTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 14, 1)
)
acsPowerMgmtUPSBypassTableEntry.setIndexNames(
    (0, "ACS8000-MIB", "acsPowerMgmtUPSBypassTablePortNumber"),
    (0, "ACS8000-MIB", "acsPowerMgmtUPSBypassTableUpsIndex"),
)
if mibBuilder.loadTexts:
    acsPowerMgmtUPSBypassTableEntry.setStatus("current")
_AcsPowerMgmtUPSBypassTablePortNumber_Type = InterfaceIndex
_AcsPowerMgmtUPSBypassTablePortNumber_Object = MibTableColumn
acsPowerMgmtUPSBypassTablePortNumber = _AcsPowerMgmtUPSBypassTablePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 14, 1, 1),
    _AcsPowerMgmtUPSBypassTablePortNumber_Type()
)
acsPowerMgmtUPSBypassTablePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSBypassTablePortNumber.setStatus("current")
_AcsPowerMgmtUPSBypassTableUpsIndex_Type = InterfaceIndex
_AcsPowerMgmtUPSBypassTableUpsIndex_Object = MibTableColumn
acsPowerMgmtUPSBypassTableUpsIndex = _AcsPowerMgmtUPSBypassTableUpsIndex_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 14, 1, 2),
    _AcsPowerMgmtUPSBypassTableUpsIndex_Type()
)
acsPowerMgmtUPSBypassTableUpsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSBypassTableUpsIndex.setStatus("current")
_AcsPowerMgmtUPSBypassTableRMSVoltageL1N_Type = DisplayString
_AcsPowerMgmtUPSBypassTableRMSVoltageL1N_Object = MibTableColumn
acsPowerMgmtUPSBypassTableRMSVoltageL1N = _AcsPowerMgmtUPSBypassTableRMSVoltageL1N_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 14, 1, 3),
    _AcsPowerMgmtUPSBypassTableRMSVoltageL1N_Type()
)
acsPowerMgmtUPSBypassTableRMSVoltageL1N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSBypassTableRMSVoltageL1N.setStatus("current")
_AcsPowerMgmtUPSBypassTableRMSVoltageL1L2_Type = DisplayString
_AcsPowerMgmtUPSBypassTableRMSVoltageL1L2_Object = MibTableColumn
acsPowerMgmtUPSBypassTableRMSVoltageL1L2 = _AcsPowerMgmtUPSBypassTableRMSVoltageL1L2_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 14, 1, 4),
    _AcsPowerMgmtUPSBypassTableRMSVoltageL1L2_Type()
)
acsPowerMgmtUPSBypassTableRMSVoltageL1L2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSBypassTableRMSVoltageL1L2.setStatus("current")
_AcsPowerMgmtUPSBypassTableRMSVoltageL2N_Type = DisplayString
_AcsPowerMgmtUPSBypassTableRMSVoltageL2N_Object = MibTableColumn
acsPowerMgmtUPSBypassTableRMSVoltageL2N = _AcsPowerMgmtUPSBypassTableRMSVoltageL2N_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 14, 1, 5),
    _AcsPowerMgmtUPSBypassTableRMSVoltageL2N_Type()
)
acsPowerMgmtUPSBypassTableRMSVoltageL2N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSBypassTableRMSVoltageL2N.setStatus("current")
_AcsPowerMgmtUPSBypassTableRMSCurrent_Type = DisplayString
_AcsPowerMgmtUPSBypassTableRMSCurrent_Object = MibTableColumn
acsPowerMgmtUPSBypassTableRMSCurrent = _AcsPowerMgmtUPSBypassTableRMSCurrent_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 14, 1, 6),
    _AcsPowerMgmtUPSBypassTableRMSCurrent_Type()
)
acsPowerMgmtUPSBypassTableRMSCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSBypassTableRMSCurrent.setStatus("current")
_AcsPowerMgmtUPSBypassTableRMSCurrentL2_Type = DisplayString
_AcsPowerMgmtUPSBypassTableRMSCurrentL2_Object = MibTableColumn
acsPowerMgmtUPSBypassTableRMSCurrentL2 = _AcsPowerMgmtUPSBypassTableRMSCurrentL2_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 14, 1, 7),
    _AcsPowerMgmtUPSBypassTableRMSCurrentL2_Type()
)
acsPowerMgmtUPSBypassTableRMSCurrentL2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSBypassTableRMSCurrentL2.setStatus("current")
_AcsPowerMgmtUPSBypassTableInputFrequency_Type = DisplayString
_AcsPowerMgmtUPSBypassTableInputFrequency_Object = MibTableColumn
acsPowerMgmtUPSBypassTableInputFrequency = _AcsPowerMgmtUPSBypassTableInputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 14, 1, 8),
    _AcsPowerMgmtUPSBypassTableInputFrequency_Type()
)
acsPowerMgmtUPSBypassTableInputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSBypassTableInputFrequency.setStatus("current")
_AcsPowerMgmtUPSBypassTableNominalVoltage_Type = DisplayString
_AcsPowerMgmtUPSBypassTableNominalVoltage_Object = MibTableColumn
acsPowerMgmtUPSBypassTableNominalVoltage = _AcsPowerMgmtUPSBypassTableNominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 14, 1, 9),
    _AcsPowerMgmtUPSBypassTableNominalVoltage_Type()
)
acsPowerMgmtUPSBypassTableNominalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSBypassTableNominalVoltage.setStatus("current")
_AcsPowerMgmtUPSBatteryTable_Object = MibTable
acsPowerMgmtUPSBatteryTable = _AcsPowerMgmtUPSBatteryTable_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 15)
)
if mibBuilder.loadTexts:
    acsPowerMgmtUPSBatteryTable.setStatus("current")
_AcsPowerMgmtUPSBatteryTableEntry_Object = MibTableRow
acsPowerMgmtUPSBatteryTableEntry = _AcsPowerMgmtUPSBatteryTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 15, 1)
)
acsPowerMgmtUPSBatteryTableEntry.setIndexNames(
    (0, "ACS8000-MIB", "acsPowerMgmtUPSBatteryTablePortNumber"),
    (0, "ACS8000-MIB", "acsPowerMgmtUPSBatteryTableUpsIndex"),
)
if mibBuilder.loadTexts:
    acsPowerMgmtUPSBatteryTableEntry.setStatus("current")
_AcsPowerMgmtUPSBatteryTablePortNumber_Type = InterfaceIndex
_AcsPowerMgmtUPSBatteryTablePortNumber_Object = MibTableColumn
acsPowerMgmtUPSBatteryTablePortNumber = _AcsPowerMgmtUPSBatteryTablePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 15, 1, 1),
    _AcsPowerMgmtUPSBatteryTablePortNumber_Type()
)
acsPowerMgmtUPSBatteryTablePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSBatteryTablePortNumber.setStatus("current")
_AcsPowerMgmtUPSBatteryTableUpsIndex_Type = InterfaceIndex
_AcsPowerMgmtUPSBatteryTableUpsIndex_Object = MibTableColumn
acsPowerMgmtUPSBatteryTableUpsIndex = _AcsPowerMgmtUPSBatteryTableUpsIndex_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 15, 1, 2),
    _AcsPowerMgmtUPSBatteryTableUpsIndex_Type()
)
acsPowerMgmtUPSBatteryTableUpsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSBatteryTableUpsIndex.setStatus("current")
_AcsPowerMgmtUPSBatteryTableDCBusVoltage_Type = DisplayString
_AcsPowerMgmtUPSBatteryTableDCBusVoltage_Object = MibTableColumn
acsPowerMgmtUPSBatteryTableDCBusVoltage = _AcsPowerMgmtUPSBatteryTableDCBusVoltage_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 15, 1, 3),
    _AcsPowerMgmtUPSBatteryTableDCBusVoltage_Type()
)
acsPowerMgmtUPSBatteryTableDCBusVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSBatteryTableDCBusVoltage.setStatus("current")
_AcsPowerMgmtUPSBatteryTableTimeRemaining_Type = DisplayString
_AcsPowerMgmtUPSBatteryTableTimeRemaining_Object = MibTableColumn
acsPowerMgmtUPSBatteryTableTimeRemaining = _AcsPowerMgmtUPSBatteryTableTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 15, 1, 4),
    _AcsPowerMgmtUPSBatteryTableTimeRemaining_Type()
)
acsPowerMgmtUPSBatteryTableTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSBatteryTableTimeRemaining.setStatus("current")
_AcsPowerMgmtUPSBatteryTablePercentageCharge_Type = DisplayString
_AcsPowerMgmtUPSBatteryTablePercentageCharge_Object = MibTableColumn
acsPowerMgmtUPSBatteryTablePercentageCharge = _AcsPowerMgmtUPSBatteryTablePercentageCharge_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 15, 1, 5),
    _AcsPowerMgmtUPSBatteryTablePercentageCharge_Type()
)
acsPowerMgmtUPSBatteryTablePercentageCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSBatteryTablePercentageCharge.setStatus("current")
_AcsPowerMgmtUPSBatteryTableChargeStatus_Type = DisplayString
_AcsPowerMgmtUPSBatteryTableChargeStatus_Object = MibTableColumn
acsPowerMgmtUPSBatteryTableChargeStatus = _AcsPowerMgmtUPSBatteryTableChargeStatus_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 15, 1, 6),
    _AcsPowerMgmtUPSBatteryTableChargeStatus_Type()
)
acsPowerMgmtUPSBatteryTableChargeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSBatteryTableChargeStatus.setStatus("current")


class _AcsPowerMgmtUPSBatteryTableLowBatteryWarningTime_Type(Integer32):
    """Custom type acsPowerMgmtUPSBatteryTableLowBatteryWarningTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 30),
    )


_AcsPowerMgmtUPSBatteryTableLowBatteryWarningTime_Type.__name__ = "Integer32"
_AcsPowerMgmtUPSBatteryTableLowBatteryWarningTime_Object = MibTableColumn
acsPowerMgmtUPSBatteryTableLowBatteryWarningTime = _AcsPowerMgmtUPSBatteryTableLowBatteryWarningTime_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 15, 1, 7),
    _AcsPowerMgmtUPSBatteryTableLowBatteryWarningTime_Type()
)
acsPowerMgmtUPSBatteryTableLowBatteryWarningTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSBatteryTableLowBatteryWarningTime.setStatus("current")
_AcsPowerMgmtUPSBatteryTableTestResult_Type = DisplayString
_AcsPowerMgmtUPSBatteryTableTestResult_Object = MibTableColumn
acsPowerMgmtUPSBatteryTableTestResult = _AcsPowerMgmtUPSBatteryTableTestResult_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 15, 1, 8),
    _AcsPowerMgmtUPSBatteryTableTestResult_Type()
)
acsPowerMgmtUPSBatteryTableTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSBatteryTableTestResult.setStatus("current")
_AcsPowerMgmtUPSBatteryTableDCBusNominalVoltage_Type = DisplayString
_AcsPowerMgmtUPSBatteryTableDCBusNominalVoltage_Object = MibTableColumn
acsPowerMgmtUPSBatteryTableDCBusNominalVoltage = _AcsPowerMgmtUPSBatteryTableDCBusNominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 15, 1, 9),
    _AcsPowerMgmtUPSBatteryTableDCBusNominalVoltage_Type()
)
acsPowerMgmtUPSBatteryTableDCBusNominalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSBatteryTableDCBusNominalVoltage.setStatus("current")
_AcsPowerMgmtUPSBatteryTableNominalBatteryCapacity_Type = DisplayString
_AcsPowerMgmtUPSBatteryTableNominalBatteryCapacity_Object = MibTableColumn
acsPowerMgmtUPSBatteryTableNominalBatteryCapacity = _AcsPowerMgmtUPSBatteryTableNominalBatteryCapacity_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 15, 1, 10),
    _AcsPowerMgmtUPSBatteryTableNominalBatteryCapacity_Type()
)
acsPowerMgmtUPSBatteryTableNominalBatteryCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSBatteryTableNominalBatteryCapacity.setStatus("current")
_AcsPowerMgmtUPSBatteryTableBatteryFloatVoltage_Type = DisplayString
_AcsPowerMgmtUPSBatteryTableBatteryFloatVoltage_Object = MibTableColumn
acsPowerMgmtUPSBatteryTableBatteryFloatVoltage = _AcsPowerMgmtUPSBatteryTableBatteryFloatVoltage_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 15, 1, 11),
    _AcsPowerMgmtUPSBatteryTableBatteryFloatVoltage_Type()
)
acsPowerMgmtUPSBatteryTableBatteryFloatVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSBatteryTableBatteryFloatVoltage.setStatus("current")
_AcsPowerMgmtUPSBatteryTableBatteryCabinetType_Type = DisplayString
_AcsPowerMgmtUPSBatteryTableBatteryCabinetType_Object = MibTableColumn
acsPowerMgmtUPSBatteryTableBatteryCabinetType = _AcsPowerMgmtUPSBatteryTableBatteryCabinetType_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 15, 1, 12),
    _AcsPowerMgmtUPSBatteryTableBatteryCabinetType_Type()
)
acsPowerMgmtUPSBatteryTableBatteryCabinetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSBatteryTableBatteryCabinetType.setStatus("current")
_AcsPowerMgmtUPSBatteryTableBatteryNumberOfEBC_Type = DisplayString
_AcsPowerMgmtUPSBatteryTableBatteryNumberOfEBC_Object = MibTableColumn
acsPowerMgmtUPSBatteryTableBatteryNumberOfEBC = _AcsPowerMgmtUPSBatteryTableBatteryNumberOfEBC_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 15, 1, 13),
    _AcsPowerMgmtUPSBatteryTableBatteryNumberOfEBC_Type()
)
acsPowerMgmtUPSBatteryTableBatteryNumberOfEBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSBatteryTableBatteryNumberOfEBC.setStatus("current")
_AcsPowerMgmtUPSBatteryTableBatteryRating_Type = DisplayString
_AcsPowerMgmtUPSBatteryTableBatteryRating_Object = MibTableColumn
acsPowerMgmtUPSBatteryTableBatteryRating = _AcsPowerMgmtUPSBatteryTableBatteryRating_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 15, 1, 14),
    _AcsPowerMgmtUPSBatteryTableBatteryRating_Type()
)
acsPowerMgmtUPSBatteryTableBatteryRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSBatteryTableBatteryRating.setStatus("current")
_AcsPowerMgmtUPSBatteryTableBatteryDischargeTime_Type = DisplayString
_AcsPowerMgmtUPSBatteryTableBatteryDischargeTime_Object = MibTableColumn
acsPowerMgmtUPSBatteryTableBatteryDischargeTime = _AcsPowerMgmtUPSBatteryTableBatteryDischargeTime_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 15, 1, 15),
    _AcsPowerMgmtUPSBatteryTableBatteryDischargeTime_Type()
)
acsPowerMgmtUPSBatteryTableBatteryDischargeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSBatteryTableBatteryDischargeTime.setStatus("current")
_AcsPowerMgmtUPSBatteryTableBatteryChargeCompensating_Type = DisplayString
_AcsPowerMgmtUPSBatteryTableBatteryChargeCompensating_Object = MibTableColumn
acsPowerMgmtUPSBatteryTableBatteryChargeCompensating = _AcsPowerMgmtUPSBatteryTableBatteryChargeCompensating_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 15, 1, 16),
    _AcsPowerMgmtUPSBatteryTableBatteryChargeCompensating_Type()
)
acsPowerMgmtUPSBatteryTableBatteryChargeCompensating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSBatteryTableBatteryChargeCompensating.setStatus("current")
_AcsPowerMgmtUPSBatteryTableBatteryChargerState_Type = DisplayString
_AcsPowerMgmtUPSBatteryTableBatteryChargerState_Object = MibTableColumn
acsPowerMgmtUPSBatteryTableBatteryChargerState = _AcsPowerMgmtUPSBatteryTableBatteryChargerState_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 15, 1, 17),
    _AcsPowerMgmtUPSBatteryTableBatteryChargerState_Type()
)
acsPowerMgmtUPSBatteryTableBatteryChargerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSBatteryTableBatteryChargerState.setStatus("current")


class _AcsPowerMgmtUPSBatteryTableStartBatteryTest_Type(Integer32):
    """Custom type acsPowerMgmtUPSBatteryTableStartBatteryTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("start", 2))
    )


_AcsPowerMgmtUPSBatteryTableStartBatteryTest_Type.__name__ = "Integer32"
_AcsPowerMgmtUPSBatteryTableStartBatteryTest_Object = MibTableColumn
acsPowerMgmtUPSBatteryTableStartBatteryTest = _AcsPowerMgmtUPSBatteryTableStartBatteryTest_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 15, 1, 18),
    _AcsPowerMgmtUPSBatteryTableStartBatteryTest_Type()
)
acsPowerMgmtUPSBatteryTableStartBatteryTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSBatteryTableStartBatteryTest.setStatus("current")
_AcsPowerMgmtUPSBatteryTableBatteryStatus_Type = DisplayString
_AcsPowerMgmtUPSBatteryTableBatteryStatus_Object = MibTableColumn
acsPowerMgmtUPSBatteryTableBatteryStatus = _AcsPowerMgmtUPSBatteryTableBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 15, 1, 19),
    _AcsPowerMgmtUPSBatteryTableBatteryStatus_Type()
)
acsPowerMgmtUPSBatteryTableBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSBatteryTableBatteryStatus.setStatus("current")
_AcsPowerMgmtUPSBatteryTableBatteryTotalDischargeTime_Type = DisplayString
_AcsPowerMgmtUPSBatteryTableBatteryTotalDischargeTime_Object = MibTableColumn
acsPowerMgmtUPSBatteryTableBatteryTotalDischargeTime = _AcsPowerMgmtUPSBatteryTableBatteryTotalDischargeTime_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 15, 1, 20),
    _AcsPowerMgmtUPSBatteryTableBatteryTotalDischargeTime_Type()
)
acsPowerMgmtUPSBatteryTableBatteryTotalDischargeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSBatteryTableBatteryTotalDischargeTime.setStatus("current")
_AcsPowerMgmtUPSBatteryTableBatteryDischargeCount_Type = DisplayString
_AcsPowerMgmtUPSBatteryTableBatteryDischargeCount_Object = MibTableColumn
acsPowerMgmtUPSBatteryTableBatteryDischargeCount = _AcsPowerMgmtUPSBatteryTableBatteryDischargeCount_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 15, 1, 21),
    _AcsPowerMgmtUPSBatteryTableBatteryDischargeCount_Type()
)
acsPowerMgmtUPSBatteryTableBatteryDischargeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSBatteryTableBatteryDischargeCount.setStatus("current")
_AcsPowerMgmtUPSBatteryTableBatteryCurrent_Type = DisplayString
_AcsPowerMgmtUPSBatteryTableBatteryCurrent_Object = MibTableColumn
acsPowerMgmtUPSBatteryTableBatteryCurrent = _AcsPowerMgmtUPSBatteryTableBatteryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 15, 1, 22),
    _AcsPowerMgmtUPSBatteryTableBatteryCurrent_Type()
)
acsPowerMgmtUPSBatteryTableBatteryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSBatteryTableBatteryCurrent.setStatus("current")
_AcsPowerMgmtUPSOutputTable_Object = MibTable
acsPowerMgmtUPSOutputTable = _AcsPowerMgmtUPSOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 16)
)
if mibBuilder.loadTexts:
    acsPowerMgmtUPSOutputTable.setStatus("current")
_AcsPowerMgmtUPSOutputTableEntry_Object = MibTableRow
acsPowerMgmtUPSOutputTableEntry = _AcsPowerMgmtUPSOutputTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 16, 1)
)
acsPowerMgmtUPSOutputTableEntry.setIndexNames(
    (0, "ACS8000-MIB", "acsPowerMgmtUPSOutputTablePortNumber"),
    (0, "ACS8000-MIB", "acsPowerMgmtUPSOutputTableUpsIndex"),
)
if mibBuilder.loadTexts:
    acsPowerMgmtUPSOutputTableEntry.setStatus("current")
_AcsPowerMgmtUPSOutputTablePortNumber_Type = InterfaceIndex
_AcsPowerMgmtUPSOutputTablePortNumber_Object = MibTableColumn
acsPowerMgmtUPSOutputTablePortNumber = _AcsPowerMgmtUPSOutputTablePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 16, 1, 1),
    _AcsPowerMgmtUPSOutputTablePortNumber_Type()
)
acsPowerMgmtUPSOutputTablePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSOutputTablePortNumber.setStatus("current")
_AcsPowerMgmtUPSOutputTableUpsIndex_Type = InterfaceIndex
_AcsPowerMgmtUPSOutputTableUpsIndex_Object = MibTableColumn
acsPowerMgmtUPSOutputTableUpsIndex = _AcsPowerMgmtUPSOutputTableUpsIndex_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 16, 1, 2),
    _AcsPowerMgmtUPSOutputTableUpsIndex_Type()
)
acsPowerMgmtUPSOutputTableUpsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSOutputTableUpsIndex.setStatus("current")
_AcsPowerMgmtUPSOutputTableApparentPower_Type = DisplayString
_AcsPowerMgmtUPSOutputTableApparentPower_Object = MibTableColumn
acsPowerMgmtUPSOutputTableApparentPower = _AcsPowerMgmtUPSOutputTableApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 16, 1, 3),
    _AcsPowerMgmtUPSOutputTableApparentPower_Type()
)
acsPowerMgmtUPSOutputTableApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSOutputTableApparentPower.setStatus("current")
_AcsPowerMgmtUPSOutputTableFrequency_Type = DisplayString
_AcsPowerMgmtUPSOutputTableFrequency_Object = MibTableColumn
acsPowerMgmtUPSOutputTableFrequency = _AcsPowerMgmtUPSOutputTableFrequency_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 16, 1, 4),
    _AcsPowerMgmtUPSOutputTableFrequency_Type()
)
acsPowerMgmtUPSOutputTableFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSOutputTableFrequency.setStatus("current")
_AcsPowerMgmtUPSOutputTablePercentPower_Type = DisplayString
_AcsPowerMgmtUPSOutputTablePercentPower_Object = MibTableColumn
acsPowerMgmtUPSOutputTablePercentPower = _AcsPowerMgmtUPSOutputTablePercentPower_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 16, 1, 5),
    _AcsPowerMgmtUPSOutputTablePercentPower_Type()
)
acsPowerMgmtUPSOutputTablePercentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSOutputTablePercentPower.setStatus("current")
_AcsPowerMgmtUPSOutputTablePercentPowerL1_Type = DisplayString
_AcsPowerMgmtUPSOutputTablePercentPowerL1_Object = MibTableColumn
acsPowerMgmtUPSOutputTablePercentPowerL1 = _AcsPowerMgmtUPSOutputTablePercentPowerL1_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 16, 1, 6),
    _AcsPowerMgmtUPSOutputTablePercentPowerL1_Type()
)
acsPowerMgmtUPSOutputTablePercentPowerL1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSOutputTablePercentPowerL1.setStatus("current")
_AcsPowerMgmtUPSOutputTablePercentPowerL2_Type = DisplayString
_AcsPowerMgmtUPSOutputTablePercentPowerL2_Object = MibTableColumn
acsPowerMgmtUPSOutputTablePercentPowerL2 = _AcsPowerMgmtUPSOutputTablePercentPowerL2_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 16, 1, 7),
    _AcsPowerMgmtUPSOutputTablePercentPowerL2_Type()
)
acsPowerMgmtUPSOutputTablePercentPowerL2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSOutputTablePercentPowerL2.setStatus("current")
_AcsPowerMgmtUPSOutputTablePower_Type = DisplayString
_AcsPowerMgmtUPSOutputTablePower_Object = MibTableColumn
acsPowerMgmtUPSOutputTablePower = _AcsPowerMgmtUPSOutputTablePower_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 16, 1, 8),
    _AcsPowerMgmtUPSOutputTablePower_Type()
)
acsPowerMgmtUPSOutputTablePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSOutputTablePower.setStatus("current")
_AcsPowerMgmtUPSOutputTableRMSCurrentL1_Type = DisplayString
_AcsPowerMgmtUPSOutputTableRMSCurrentL1_Object = MibTableColumn
acsPowerMgmtUPSOutputTableRMSCurrentL1 = _AcsPowerMgmtUPSOutputTableRMSCurrentL1_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 16, 1, 9),
    _AcsPowerMgmtUPSOutputTableRMSCurrentL1_Type()
)
acsPowerMgmtUPSOutputTableRMSCurrentL1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSOutputTableRMSCurrentL1.setStatus("current")
_AcsPowerMgmtUPSOutputTableRMSCurrentL2_Type = DisplayString
_AcsPowerMgmtUPSOutputTableRMSCurrentL2_Object = MibTableColumn
acsPowerMgmtUPSOutputTableRMSCurrentL2 = _AcsPowerMgmtUPSOutputTableRMSCurrentL2_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 16, 1, 10),
    _AcsPowerMgmtUPSOutputTableRMSCurrentL2_Type()
)
acsPowerMgmtUPSOutputTableRMSCurrentL2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSOutputTableRMSCurrentL2.setStatus("current")
_AcsPowerMgmtUPSOutputTableRMSVoltageL1N_Type = DisplayString
_AcsPowerMgmtUPSOutputTableRMSVoltageL1N_Object = MibTableColumn
acsPowerMgmtUPSOutputTableRMSVoltageL1N = _AcsPowerMgmtUPSOutputTableRMSVoltageL1N_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 16, 1, 11),
    _AcsPowerMgmtUPSOutputTableRMSVoltageL1N_Type()
)
acsPowerMgmtUPSOutputTableRMSVoltageL1N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSOutputTableRMSVoltageL1N.setStatus("current")
_AcsPowerMgmtUPSOutputTableRMSVoltageL2N_Type = DisplayString
_AcsPowerMgmtUPSOutputTableRMSVoltageL2N_Object = MibTableColumn
acsPowerMgmtUPSOutputTableRMSVoltageL2N = _AcsPowerMgmtUPSOutputTableRMSVoltageL2N_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 16, 1, 12),
    _AcsPowerMgmtUPSOutputTableRMSVoltageL2N_Type()
)
acsPowerMgmtUPSOutputTableRMSVoltageL2N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSOutputTableRMSVoltageL2N.setStatus("current")
_AcsPowerMgmtUPSOutputTableRMSVoltageL1L2_Type = DisplayString
_AcsPowerMgmtUPSOutputTableRMSVoltageL1L2_Object = MibTableColumn
acsPowerMgmtUPSOutputTableRMSVoltageL1L2 = _AcsPowerMgmtUPSOutputTableRMSVoltageL1L2_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 16, 1, 13),
    _AcsPowerMgmtUPSOutputTableRMSVoltageL1L2_Type()
)
acsPowerMgmtUPSOutputTableRMSVoltageL1L2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSOutputTableRMSVoltageL1L2.setStatus("current")


class _AcsPowerMgmtUPSOutputOffDelay_Type(Integer32):
    """Custom type acsPowerMgmtUPSOutputOffDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_AcsPowerMgmtUPSOutputOffDelay_Type.__name__ = "Integer32"
_AcsPowerMgmtUPSOutputOffDelay_Object = MibTableColumn
acsPowerMgmtUPSOutputOffDelay = _AcsPowerMgmtUPSOutputOffDelay_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 16, 1, 14),
    _AcsPowerMgmtUPSOutputOffDelay_Type()
)
acsPowerMgmtUPSOutputOffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSOutputOffDelay.setStatus("current")


class _AcsPowerMgmtUPSOutputOnDelay_Type(Integer32):
    """Custom type acsPowerMgmtUPSOutputOnDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_AcsPowerMgmtUPSOutputOnDelay_Type.__name__ = "Integer32"
_AcsPowerMgmtUPSOutputOnDelay_Object = MibTableColumn
acsPowerMgmtUPSOutputOnDelay = _AcsPowerMgmtUPSOutputOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 16, 1, 15),
    _AcsPowerMgmtUPSOutputOnDelay_Type()
)
acsPowerMgmtUPSOutputOnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSOutputOnDelay.setStatus("current")


class _AcsPowerMgmtUPSOutputCycleDelay_Type(Integer32):
    """Custom type acsPowerMgmtUPSOutputCycleDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_AcsPowerMgmtUPSOutputCycleDelay_Type.__name__ = "Integer32"
_AcsPowerMgmtUPSOutputCycleDelay_Object = MibTableColumn
acsPowerMgmtUPSOutputCycleDelay = _AcsPowerMgmtUPSOutputCycleDelay_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 16, 1, 16),
    _AcsPowerMgmtUPSOutputCycleDelay_Type()
)
acsPowerMgmtUPSOutputCycleDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSOutputCycleDelay.setStatus("current")
_AcsPowerMgmtUPSOutputTableMaxVoltageL1_Type = DisplayString
_AcsPowerMgmtUPSOutputTableMaxVoltageL1_Object = MibTableColumn
acsPowerMgmtUPSOutputTableMaxVoltageL1 = _AcsPowerMgmtUPSOutputTableMaxVoltageL1_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 16, 1, 17),
    _AcsPowerMgmtUPSOutputTableMaxVoltageL1_Type()
)
acsPowerMgmtUPSOutputTableMaxVoltageL1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSOutputTableMaxVoltageL1.setStatus("current")
_AcsPowerMgmtUPSOutputTableMinVoltageL1_Type = DisplayString
_AcsPowerMgmtUPSOutputTableMinVoltageL1_Object = MibTableColumn
acsPowerMgmtUPSOutputTableMinVoltageL1 = _AcsPowerMgmtUPSOutputTableMinVoltageL1_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 16, 1, 18),
    _AcsPowerMgmtUPSOutputTableMinVoltageL1_Type()
)
acsPowerMgmtUPSOutputTableMinVoltageL1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSOutputTableMinVoltageL1.setStatus("current")
_AcsPowerMgmtUPSOutputTableMaxVoltageL2_Type = DisplayString
_AcsPowerMgmtUPSOutputTableMaxVoltageL2_Object = MibTableColumn
acsPowerMgmtUPSOutputTableMaxVoltageL2 = _AcsPowerMgmtUPSOutputTableMaxVoltageL2_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 16, 1, 19),
    _AcsPowerMgmtUPSOutputTableMaxVoltageL2_Type()
)
acsPowerMgmtUPSOutputTableMaxVoltageL2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSOutputTableMaxVoltageL2.setStatus("current")
_AcsPowerMgmtUPSOutputTableMinVoltageL2_Type = DisplayString
_AcsPowerMgmtUPSOutputTableMinVoltageL2_Object = MibTableColumn
acsPowerMgmtUPSOutputTableMinVoltageL2 = _AcsPowerMgmtUPSOutputTableMinVoltageL2_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 16, 1, 20),
    _AcsPowerMgmtUPSOutputTableMinVoltageL2_Type()
)
acsPowerMgmtUPSOutputTableMinVoltageL2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSOutputTableMinVoltageL2.setStatus("current")
_AcsPowerMgmtUPSOutputTableNominalVoltage_Type = DisplayString
_AcsPowerMgmtUPSOutputTableNominalVoltage_Object = MibTableColumn
acsPowerMgmtUPSOutputTableNominalVoltage = _AcsPowerMgmtUPSOutputTableNominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 16, 1, 21),
    _AcsPowerMgmtUPSOutputTableNominalVoltage_Type()
)
acsPowerMgmtUPSOutputTableNominalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSOutputTableNominalVoltage.setStatus("current")
_AcsPowerMgmtUPSOutputTablePowerNominalFrequency_Type = DisplayString
_AcsPowerMgmtUPSOutputTablePowerNominalFrequency_Object = MibTableColumn
acsPowerMgmtUPSOutputTablePowerNominalFrequency = _AcsPowerMgmtUPSOutputTablePowerNominalFrequency_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 16, 1, 22),
    _AcsPowerMgmtUPSOutputTablePowerNominalFrequency_Type()
)
acsPowerMgmtUPSOutputTablePowerNominalFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSOutputTablePowerNominalFrequency.setStatus("current")
_AcsPowerMgmtUPSOutputTablePowerApparentPowerRating_Type = DisplayString
_AcsPowerMgmtUPSOutputTablePowerApparentPowerRating_Object = MibTableColumn
acsPowerMgmtUPSOutputTablePowerApparentPowerRating = _AcsPowerMgmtUPSOutputTablePowerApparentPowerRating_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 16, 1, 23),
    _AcsPowerMgmtUPSOutputTablePowerApparentPowerRating_Type()
)
acsPowerMgmtUPSOutputTablePowerApparentPowerRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSOutputTablePowerApparentPowerRating.setStatus("current")
_AcsPowerMgmtUPSOutputTablePowerNominalPowerFactor_Type = DisplayString
_AcsPowerMgmtUPSOutputTablePowerNominalPowerFactor_Object = MibTableColumn
acsPowerMgmtUPSOutputTablePowerNominalPowerFactor = _AcsPowerMgmtUPSOutputTablePowerNominalPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 16, 1, 24),
    _AcsPowerMgmtUPSOutputTablePowerNominalPowerFactor_Type()
)
acsPowerMgmtUPSOutputTablePowerNominalPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSOutputTablePowerNominalPowerFactor.setStatus("current")
_AcsPowerMgmtUPSOutputTablePowerPowerFactorCorrection_Type = DisplayString
_AcsPowerMgmtUPSOutputTablePowerPowerFactorCorrection_Object = MibTableColumn
acsPowerMgmtUPSOutputTablePowerPowerFactorCorrection = _AcsPowerMgmtUPSOutputTablePowerPowerFactorCorrection_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 16, 1, 25),
    _AcsPowerMgmtUPSOutputTablePowerPowerFactorCorrection_Type()
)
acsPowerMgmtUPSOutputTablePowerPowerFactorCorrection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSOutputTablePowerPowerFactorCorrection.setStatus("current")
_AcsPowerMgmtUPSOutputTablePowerL1_Type = DisplayString
_AcsPowerMgmtUPSOutputTablePowerL1_Object = MibTableColumn
acsPowerMgmtUPSOutputTablePowerL1 = _AcsPowerMgmtUPSOutputTablePowerL1_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 16, 1, 26),
    _AcsPowerMgmtUPSOutputTablePowerL1_Type()
)
acsPowerMgmtUPSOutputTablePowerL1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSOutputTablePowerL1.setStatus("current")
_AcsPowerMgmtUPSOutputTablePowerL2_Type = DisplayString
_AcsPowerMgmtUPSOutputTablePowerL2_Object = MibTableColumn
acsPowerMgmtUPSOutputTablePowerL2 = _AcsPowerMgmtUPSOutputTablePowerL2_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 16, 1, 27),
    _AcsPowerMgmtUPSOutputTablePowerL2_Type()
)
acsPowerMgmtUPSOutputTablePowerL2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSOutputTablePowerL2.setStatus("current")
_AcsPowerMgmtUPSOutputTableApparentPowerL1_Type = DisplayString
_AcsPowerMgmtUPSOutputTableApparentPowerL1_Object = MibTableColumn
acsPowerMgmtUPSOutputTableApparentPowerL1 = _AcsPowerMgmtUPSOutputTableApparentPowerL1_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 16, 1, 28),
    _AcsPowerMgmtUPSOutputTableApparentPowerL1_Type()
)
acsPowerMgmtUPSOutputTableApparentPowerL1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSOutputTableApparentPowerL1.setStatus("current")
_AcsPowerMgmtUPSOutputTableApparentPowerL2_Type = DisplayString
_AcsPowerMgmtUPSOutputTableApparentPowerL2_Object = MibTableColumn
acsPowerMgmtUPSOutputTableApparentPowerL2 = _AcsPowerMgmtUPSOutputTableApparentPowerL2_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 16, 1, 29),
    _AcsPowerMgmtUPSOutputTableApparentPowerL2_Type()
)
acsPowerMgmtUPSOutputTableApparentPowerL2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSOutputTableApparentPowerL2.setStatus("current")
_AcsPowerMgmtUPSOutputTablePowerFactorL1_Type = DisplayString
_AcsPowerMgmtUPSOutputTablePowerFactorL1_Object = MibTableColumn
acsPowerMgmtUPSOutputTablePowerFactorL1 = _AcsPowerMgmtUPSOutputTablePowerFactorL1_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 16, 1, 30),
    _AcsPowerMgmtUPSOutputTablePowerFactorL1_Type()
)
acsPowerMgmtUPSOutputTablePowerFactorL1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSOutputTablePowerFactorL1.setStatus("current")
_AcsPowerMgmtUPSOutputTablePowerFactorL2_Type = DisplayString
_AcsPowerMgmtUPSOutputTablePowerFactorL2_Object = MibTableColumn
acsPowerMgmtUPSOutputTablePowerFactorL2 = _AcsPowerMgmtUPSOutputTablePowerFactorL2_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 16, 1, 31),
    _AcsPowerMgmtUPSOutputTablePowerFactorL2_Type()
)
acsPowerMgmtUPSOutputTablePowerFactorL2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSOutputTablePowerFactorL2.setStatus("current")
_AcsPowerMgmtUPSEcoModeTable_Object = MibTable
acsPowerMgmtUPSEcoModeTable = _AcsPowerMgmtUPSEcoModeTable_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 17)
)
if mibBuilder.loadTexts:
    acsPowerMgmtUPSEcoModeTable.setStatus("current")
_AcsPowerMgmtUPSEcoModeTableEntry_Object = MibTableRow
acsPowerMgmtUPSEcoModeTableEntry = _AcsPowerMgmtUPSEcoModeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 17, 1)
)
acsPowerMgmtUPSEcoModeTableEntry.setIndexNames(
    (0, "ACS8000-MIB", "acsPowerMgmtUPSBypassTablePortNumber"),
    (0, "ACS8000-MIB", "acsPowerMgmtUPSBypassTableUpsIndex"),
)
if mibBuilder.loadTexts:
    acsPowerMgmtUPSEcoModeTableEntry.setStatus("current")
_AcsPowerMgmtUPSEcoModeTablePortNumber_Type = InterfaceIndex
_AcsPowerMgmtUPSEcoModeTablePortNumber_Object = MibTableColumn
acsPowerMgmtUPSEcoModeTablePortNumber = _AcsPowerMgmtUPSEcoModeTablePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 17, 1, 1),
    _AcsPowerMgmtUPSEcoModeTablePortNumber_Type()
)
acsPowerMgmtUPSEcoModeTablePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSEcoModeTablePortNumber.setStatus("current")
_AcsPowerMgmtUPSEcoModeTableUpsIndex_Type = InterfaceIndex
_AcsPowerMgmtUPSEcoModeTableUpsIndex_Object = MibTableColumn
acsPowerMgmtUPSEcoModeTableUpsIndex = _AcsPowerMgmtUPSEcoModeTableUpsIndex_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 17, 1, 2),
    _AcsPowerMgmtUPSEcoModeTableUpsIndex_Type()
)
acsPowerMgmtUPSEcoModeTableUpsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSEcoModeTableUpsIndex.setStatus("current")
_AcsPowerMgmtUPSEcoModeTableStatus_Type = DisplayString
_AcsPowerMgmtUPSEcoModeTableStatus_Object = MibTableColumn
acsPowerMgmtUPSEcoModeTableStatus = _AcsPowerMgmtUPSEcoModeTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 17, 1, 3),
    _AcsPowerMgmtUPSEcoModeTableStatus_Type()
)
acsPowerMgmtUPSEcoModeTableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSEcoModeTableStatus.setStatus("current")


class _AcsPowerMgmtUPSEcoModeTableStateControl_Type(Integer32):
    """Custom type acsPowerMgmtUPSEcoModeTableStateControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("enable", 2),
          ("disable", 3))
    )


_AcsPowerMgmtUPSEcoModeTableStateControl_Type.__name__ = "Integer32"
_AcsPowerMgmtUPSEcoModeTableStateControl_Object = MibTableColumn
acsPowerMgmtUPSEcoModeTableStateControl = _AcsPowerMgmtUPSEcoModeTableStateControl_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 17, 1, 4),
    _AcsPowerMgmtUPSEcoModeTableStateControl_Type()
)
acsPowerMgmtUPSEcoModeTableStateControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSEcoModeTableStateControl.setStatus("current")
_AcsPowerMgmtUPSOutletGroupTable_Object = MibTable
acsPowerMgmtUPSOutletGroupTable = _AcsPowerMgmtUPSOutletGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 18)
)
if mibBuilder.loadTexts:
    acsPowerMgmtUPSOutletGroupTable.setStatus("current")
_AcsPowerMgmtUPSOutletGroupTableEntry_Object = MibTableRow
acsPowerMgmtUPSOutletGroupTableEntry = _AcsPowerMgmtUPSOutletGroupTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 18, 1)
)
acsPowerMgmtUPSOutletGroupTableEntry.setIndexNames(
    (0, "ACS8000-MIB", "acsPowerMgmtUPSOutletGroupTablePortNumber"),
    (0, "ACS8000-MIB", "acsPowerMgmtUPSOutletGroupTableUpsIndex"),
    (0, "ACS8000-MIB", "acsPowerMgmtUPSOutletGroupTableNumber"),
)
if mibBuilder.loadTexts:
    acsPowerMgmtUPSOutletGroupTableEntry.setStatus("current")
_AcsPowerMgmtUPSOutletGroupTablePortNumber_Type = InterfaceIndex
_AcsPowerMgmtUPSOutletGroupTablePortNumber_Object = MibTableColumn
acsPowerMgmtUPSOutletGroupTablePortNumber = _AcsPowerMgmtUPSOutletGroupTablePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 18, 1, 1),
    _AcsPowerMgmtUPSOutletGroupTablePortNumber_Type()
)
acsPowerMgmtUPSOutletGroupTablePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSOutletGroupTablePortNumber.setStatus("current")
_AcsPowerMgmtUPSOutletGroupTableUpsIndex_Type = InterfaceIndex
_AcsPowerMgmtUPSOutletGroupTableUpsIndex_Object = MibTableColumn
acsPowerMgmtUPSOutletGroupTableUpsIndex = _AcsPowerMgmtUPSOutletGroupTableUpsIndex_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 18, 1, 2),
    _AcsPowerMgmtUPSOutletGroupTableUpsIndex_Type()
)
acsPowerMgmtUPSOutletGroupTableUpsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSOutletGroupTableUpsIndex.setStatus("current")
_AcsPowerMgmtUPSOutletGroupTableNumber_Type = InterfaceIndex
_AcsPowerMgmtUPSOutletGroupTableNumber_Object = MibTableColumn
acsPowerMgmtUPSOutletGroupTableNumber = _AcsPowerMgmtUPSOutletGroupTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 18, 1, 3),
    _AcsPowerMgmtUPSOutletGroupTableNumber_Type()
)
acsPowerMgmtUPSOutletGroupTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSOutletGroupTableNumber.setStatus("current")
_AcsPowerMgmtUPSOutletGroupTableLabel_Type = DisplayString
_AcsPowerMgmtUPSOutletGroupTableLabel_Object = MibTableColumn
acsPowerMgmtUPSOutletGroupTableLabel = _AcsPowerMgmtUPSOutletGroupTableLabel_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 18, 1, 4),
    _AcsPowerMgmtUPSOutletGroupTableLabel_Type()
)
acsPowerMgmtUPSOutletGroupTableLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSOutletGroupTableLabel.setStatus("current")
_AcsPowerMgmtUPSOutletGroupTableState_Type = DisplayString
_AcsPowerMgmtUPSOutletGroupTableState_Object = MibTableColumn
acsPowerMgmtUPSOutletGroupTableState = _AcsPowerMgmtUPSOutletGroupTableState_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 18, 1, 5),
    _AcsPowerMgmtUPSOutletGroupTableState_Type()
)
acsPowerMgmtUPSOutletGroupTableState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSOutletGroupTableState.setStatus("current")


class _AcsPowerMgmtUPSOutletGroupTablePowerControl_Type(Integer32):
    """Custom type acsPowerMgmtUPSOutletGroupTablePowerControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("powerOn", 2),
          ("powerOff", 3),
          ("powerCycle", 4))
    )


_AcsPowerMgmtUPSOutletGroupTablePowerControl_Type.__name__ = "Integer32"
_AcsPowerMgmtUPSOutletGroupTablePowerControl_Object = MibTableColumn
acsPowerMgmtUPSOutletGroupTablePowerControl = _AcsPowerMgmtUPSOutletGroupTablePowerControl_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 5, 18, 1, 6),
    _AcsPowerMgmtUPSOutletGroupTablePowerControl_Type()
)
acsPowerMgmtUPSOutletGroupTablePowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtUPSOutletGroupTablePowerControl.setStatus("current")
_AcsTrapObject_ObjectIdentity = ObjectIdentity
acsTrapObject = _AcsTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 6)
)
_AcsSensors_ObjectIdentity = ObjectIdentity
acsSensors = _AcsSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7)
)
_AcsSensorsInternalCurrentCPUTemperature_Type = Integer32
_AcsSensorsInternalCurrentCPUTemperature_Object = MibScalar
acsSensorsInternalCurrentCPUTemperature = _AcsSensorsInternalCurrentCPUTemperature_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 1),
    _AcsSensorsInternalCurrentCPUTemperature_Type()
)
acsSensorsInternalCurrentCPUTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSensorsInternalCurrentCPUTemperature.setStatus("current")
_AcsSensorsInternalMaxCPUTemperature_Type = Integer32
_AcsSensorsInternalMaxCPUTemperature_Object = MibScalar
acsSensorsInternalMaxCPUTemperature = _AcsSensorsInternalMaxCPUTemperature_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 2),
    _AcsSensorsInternalMaxCPUTemperature_Type()
)
acsSensorsInternalMaxCPUTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsSensorsInternalMaxCPUTemperature.setStatus("current")


class _AcsSensorsInternalMaxCPUTemperatureThreshold_Type(Integer32):
    """Custom type acsSensorsInternalMaxCPUTemperatureThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AcsSensorsInternalMaxCPUTemperatureThreshold_Type.__name__ = "Integer32"
_AcsSensorsInternalMaxCPUTemperatureThreshold_Object = MibScalar
acsSensorsInternalMaxCPUTemperatureThreshold = _AcsSensorsInternalMaxCPUTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 3),
    _AcsSensorsInternalMaxCPUTemperatureThreshold_Type()
)
acsSensorsInternalMaxCPUTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsSensorsInternalMaxCPUTemperatureThreshold.setStatus("current")
_AcsSensorsInternalMinCPUTemperature_Type = Integer32
_AcsSensorsInternalMinCPUTemperature_Object = MibScalar
acsSensorsInternalMinCPUTemperature = _AcsSensorsInternalMinCPUTemperature_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 4),
    _AcsSensorsInternalMinCPUTemperature_Type()
)
acsSensorsInternalMinCPUTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsSensorsInternalMinCPUTemperature.setStatus("current")


class _AcsSensorsInternalMinCPUTemperatureThreshold_Type(Integer32):
    """Custom type acsSensorsInternalMinCPUTemperatureThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AcsSensorsInternalMinCPUTemperatureThreshold_Type.__name__ = "Integer32"
_AcsSensorsInternalMinCPUTemperatureThreshold_Object = MibScalar
acsSensorsInternalMinCPUTemperatureThreshold = _AcsSensorsInternalMinCPUTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 5),
    _AcsSensorsInternalMinCPUTemperatureThreshold_Type()
)
acsSensorsInternalMinCPUTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsSensorsInternalMinCPUTemperatureThreshold.setStatus("current")
_AcsSensorsInternalCurrentBoardTemperature_Type = Integer32
_AcsSensorsInternalCurrentBoardTemperature_Object = MibScalar
acsSensorsInternalCurrentBoardTemperature = _AcsSensorsInternalCurrentBoardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 6),
    _AcsSensorsInternalCurrentBoardTemperature_Type()
)
acsSensorsInternalCurrentBoardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSensorsInternalCurrentBoardTemperature.setStatus("current")
_AcsSensorsInternalMaxBoardTemperature_Type = Integer32
_AcsSensorsInternalMaxBoardTemperature_Object = MibScalar
acsSensorsInternalMaxBoardTemperature = _AcsSensorsInternalMaxBoardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 7),
    _AcsSensorsInternalMaxBoardTemperature_Type()
)
acsSensorsInternalMaxBoardTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsSensorsInternalMaxBoardTemperature.setStatus("current")


class _AcsSensorsInternalMaxBoardTemperatureThreshold_Type(Integer32):
    """Custom type acsSensorsInternalMaxBoardTemperatureThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AcsSensorsInternalMaxBoardTemperatureThreshold_Type.__name__ = "Integer32"
_AcsSensorsInternalMaxBoardTemperatureThreshold_Object = MibScalar
acsSensorsInternalMaxBoardTemperatureThreshold = _AcsSensorsInternalMaxBoardTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 8),
    _AcsSensorsInternalMaxBoardTemperatureThreshold_Type()
)
acsSensorsInternalMaxBoardTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsSensorsInternalMaxBoardTemperatureThreshold.setStatus("current")
_AcsSensorsInternalMinBoardTemperature_Type = Integer32
_AcsSensorsInternalMinBoardTemperature_Object = MibScalar
acsSensorsInternalMinBoardTemperature = _AcsSensorsInternalMinBoardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 9),
    _AcsSensorsInternalMinBoardTemperature_Type()
)
acsSensorsInternalMinBoardTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsSensorsInternalMinBoardTemperature.setStatus("current")


class _AcsSensorsInternalMinBoardTemperatureThreshold_Type(Integer32):
    """Custom type acsSensorsInternalMinBoardTemperatureThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AcsSensorsInternalMinBoardTemperatureThreshold_Type.__name__ = "Integer32"
_AcsSensorsInternalMinBoardTemperatureThreshold_Object = MibScalar
acsSensorsInternalMinBoardTemperatureThreshold = _AcsSensorsInternalMinBoardTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 10),
    _AcsSensorsInternalMinBoardTemperatureThreshold_Type()
)
acsSensorsInternalMinBoardTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsSensorsInternalMinBoardTemperatureThreshold.setStatus("current")
_AcsSensorsVoltagePSInternal_Type = Integer32
_AcsSensorsVoltagePSInternal_Object = MibScalar
acsSensorsVoltagePSInternal = _AcsSensorsVoltagePSInternal_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 11),
    _AcsSensorsVoltagePSInternal_Type()
)
acsSensorsVoltagePSInternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSensorsVoltagePSInternal.setStatus("current")
_AcsSensorsVoltagePLInternal_Type = Integer32
_AcsSensorsVoltagePLInternal_Object = MibScalar
acsSensorsVoltagePLInternal = _AcsSensorsVoltagePLInternal_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 12),
    _AcsSensorsVoltagePLInternal_Type()
)
acsSensorsVoltagePLInternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSensorsVoltagePLInternal.setStatus("current")
_AcsSensorsVoltagePSAuxiliary_Type = Integer32
_AcsSensorsVoltagePSAuxiliary_Object = MibScalar
acsSensorsVoltagePSAuxiliary = _AcsSensorsVoltagePSAuxiliary_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 13),
    _AcsSensorsVoltagePSAuxiliary_Type()
)
acsSensorsVoltagePSAuxiliary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSensorsVoltagePSAuxiliary.setStatus("current")
_AcsSensorsVoltagePLAuxiliary_Type = Integer32
_AcsSensorsVoltagePLAuxiliary_Object = MibScalar
acsSensorsVoltagePLAuxiliary = _AcsSensorsVoltagePLAuxiliary_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 14),
    _AcsSensorsVoltagePLAuxiliary_Type()
)
acsSensorsVoltagePLAuxiliary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSensorsVoltagePLAuxiliary.setStatus("current")
_AcsSensorsVoltagePSDDR3_Type = Integer32
_AcsSensorsVoltagePSDDR3_Object = MibScalar
acsSensorsVoltagePSDDR3 = _AcsSensorsVoltagePSDDR3_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 15),
    _AcsSensorsVoltagePSDDR3_Type()
)
acsSensorsVoltagePSDDR3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSensorsVoltagePSDDR3.setStatus("current")
_AcsSensorsVoltagePLBlockRam_Type = Integer32
_AcsSensorsVoltagePLBlockRam_Object = MibScalar
acsSensorsVoltagePLBlockRam = _AcsSensorsVoltagePLBlockRam_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 16),
    _AcsSensorsVoltagePLBlockRam_Type()
)
acsSensorsVoltagePLBlockRam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSensorsVoltagePLBlockRam.setStatus("current")
_AcsSensorsVoltagePowerSupply1_Type = Integer32
_AcsSensorsVoltagePowerSupply1_Object = MibScalar
acsSensorsVoltagePowerSupply1 = _AcsSensorsVoltagePowerSupply1_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 17),
    _AcsSensorsVoltagePowerSupply1_Type()
)
acsSensorsVoltagePowerSupply1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSensorsVoltagePowerSupply1.setStatus("current")
_AcsSensorsVoltagePowerSupply2_Type = Integer32
_AcsSensorsVoltagePowerSupply2_Object = MibScalar
acsSensorsVoltagePowerSupply2 = _AcsSensorsVoltagePowerSupply2_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 18),
    _AcsSensorsVoltagePowerSupply2_Type()
)
acsSensorsVoltagePowerSupply2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSensorsVoltagePowerSupply2.setStatus("current")


class _AcsSensors1WireUpdateControl_Type(Integer32):
    """Custom type acsSensors1WireUpdateControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("update", 2))
    )


_AcsSensors1WireUpdateControl_Type.__name__ = "Integer32"
_AcsSensors1WireUpdateControl_Object = MibScalar
acsSensors1WireUpdateControl = _AcsSensors1WireUpdateControl_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 19),
    _AcsSensors1WireUpdateControl_Type()
)
acsSensors1WireUpdateControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsSensors1WireUpdateControl.setStatus("current")
_AcsSensors1WireTable_Object = MibTable
acsSensors1WireTable = _AcsSensors1WireTable_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 20)
)
if mibBuilder.loadTexts:
    acsSensors1WireTable.setStatus("current")
_AcsSensors1WireTableEntry_Object = MibTableRow
acsSensors1WireTableEntry = _AcsSensors1WireTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 20, 1)
)
acsSensors1WireTableEntry.setIndexNames(
    (0, "ACS8000-MIB", "acsSensors1WireTableIndex"),
)
if mibBuilder.loadTexts:
    acsSensors1WireTableEntry.setStatus("current")


class _AcsSensors1WireTableIndex_Type(Integer32):
    """Custom type acsSensors1WireTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_AcsSensors1WireTableIndex_Type.__name__ = "Integer32"
_AcsSensors1WireTableIndex_Object = MibTableColumn
acsSensors1WireTableIndex = _AcsSensors1WireTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 20, 1, 1),
    _AcsSensors1WireTableIndex_Type()
)
acsSensors1WireTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSensors1WireTableIndex.setStatus("current")
_AcsSensors1WireTableName_Type = DisplayString
_AcsSensors1WireTableName_Object = MibTableColumn
acsSensors1WireTableName = _AcsSensors1WireTableName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 20, 1, 2),
    _AcsSensors1WireTableName_Type()
)
acsSensors1WireTableName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsSensors1WireTableName.setStatus("current")
_AcsSensors1WireTableLocation_Type = DisplayString
_AcsSensors1WireTableLocation_Object = MibTableColumn
acsSensors1WireTableLocation = _AcsSensors1WireTableLocation_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 20, 1, 3),
    _AcsSensors1WireTableLocation_Type()
)
acsSensors1WireTableLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsSensors1WireTableLocation.setStatus("current")
_AcsSensors1WireTableAddress_Type = DisplayString
_AcsSensors1WireTableAddress_Object = MibTableColumn
acsSensors1WireTableAddress = _AcsSensors1WireTableAddress_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 20, 1, 4),
    _AcsSensors1WireTableAddress_Type()
)
acsSensors1WireTableAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSensors1WireTableAddress.setStatus("current")


class _AcsSensors1WireTableType_Type(Integer32):
    """Custom type acsSensors1WireTableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("sensor-unknown", 0),
          ("external-temperature", 1),
          ("external-humidity", 2),
          ("door-contact", 3),
          ("dry-contact", 4),
          ("leak", 5),
          ("differential-pressure", 6))
    )


_AcsSensors1WireTableType_Type.__name__ = "Integer32"
_AcsSensors1WireTableType_Object = MibTableColumn
acsSensors1WireTableType = _AcsSensors1WireTableType_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 20, 1, 5),
    _AcsSensors1WireTableType_Type()
)
acsSensors1WireTableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSensors1WireTableType.setStatus("current")


class _AcsSensors1WireTableUnit_Type(Integer32):
    """Custom type acsSensors1WireTableUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("celsius", 1),
          ("fahrenheit", 2),
          ("percent", 3),
          ("pa", 4))
    )


_AcsSensors1WireTableUnit_Type.__name__ = "Integer32"
_AcsSensors1WireTableUnit_Object = MibTableColumn
acsSensors1WireTableUnit = _AcsSensors1WireTableUnit_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 20, 1, 6),
    _AcsSensors1WireTableUnit_Type()
)
acsSensors1WireTableUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSensors1WireTableUnit.setStatus("current")
_AcsSensors1WireTableValue_Type = DisplayString
_AcsSensors1WireTableValue_Object = MibTableColumn
acsSensors1WireTableValue = _AcsSensors1WireTableValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 20, 1, 7),
    _AcsSensors1WireTableValue_Type()
)
acsSensors1WireTableValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSensors1WireTableValue.setStatus("current")
_AcsSensors1WireTableValueMax_Type = Integer32
_AcsSensors1WireTableValueMax_Object = MibTableColumn
acsSensors1WireTableValueMax = _AcsSensors1WireTableValueMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 20, 1, 8),
    _AcsSensors1WireTableValueMax_Type()
)
acsSensors1WireTableValueMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSensors1WireTableValueMax.setStatus("current")
_AcsSensors1WireTableValueMin_Type = Integer32
_AcsSensors1WireTableValueMin_Object = MibTableColumn
acsSensors1WireTableValueMin = _AcsSensors1WireTableValueMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 20, 1, 9),
    _AcsSensors1WireTableValueMin_Type()
)
acsSensors1WireTableValueMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSensors1WireTableValueMin.setStatus("current")
_AcsSensors1WireTableValueAvg_Type = Integer32
_AcsSensors1WireTableValueAvg_Object = MibTableColumn
acsSensors1WireTableValueAvg = _AcsSensors1WireTableValueAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 20, 1, 10),
    _AcsSensors1WireTableValueAvg_Type()
)
acsSensors1WireTableValueAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSensors1WireTableValueAvg.setStatus("current")
_AcsSensors1WireTableValueLowWarning_Type = Integer32
_AcsSensors1WireTableValueLowWarning_Object = MibTableColumn
acsSensors1WireTableValueLowWarning = _AcsSensors1WireTableValueLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 20, 1, 11),
    _AcsSensors1WireTableValueLowWarning_Type()
)
acsSensors1WireTableValueLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSensors1WireTableValueLowWarning.setStatus("current")
_AcsSensors1WireTableValueLowCritical_Type = Integer32
_AcsSensors1WireTableValueLowCritical_Object = MibTableColumn
acsSensors1WireTableValueLowCritical = _AcsSensors1WireTableValueLowCritical_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 20, 1, 12),
    _AcsSensors1WireTableValueLowCritical_Type()
)
acsSensors1WireTableValueLowCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsSensors1WireTableValueLowCritical.setStatus("current")
_AcsSensors1WireTableValueHighWarning_Type = Integer32
_AcsSensors1WireTableValueHighWarning_Object = MibTableColumn
acsSensors1WireTableValueHighWarning = _AcsSensors1WireTableValueHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 20, 1, 13),
    _AcsSensors1WireTableValueHighWarning_Type()
)
acsSensors1WireTableValueHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsSensors1WireTableValueHighWarning.setStatus("current")
_AcsSensors1WireTableValueHighCritical_Type = Integer32
_AcsSensors1WireTableValueHighCritical_Object = MibTableColumn
acsSensors1WireTableValueHighCritical = _AcsSensors1WireTableValueHighCritical_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 20, 1, 14),
    _AcsSensors1WireTableValueHighCritical_Type()
)
acsSensors1WireTableValueHighCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsSensors1WireTableValueHighCritical.setStatus("current")


class _AcsSensors1WireTableReset_Type(Integer32):
    """Custom type acsSensors1WireTableReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("reset", 2))
    )


_AcsSensors1WireTableReset_Type.__name__ = "Integer32"
_AcsSensors1WireTableReset_Object = MibTableColumn
acsSensors1WireTableReset = _AcsSensors1WireTableReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 20, 1, 15),
    _AcsSensors1WireTableReset_Type()
)
acsSensors1WireTableReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsSensors1WireTableReset.setStatus("current")


class _AcsSensors1WireTableAnalogAlarm_Type(Integer32):
    """Custom type acsSensors1WireTableAnalogAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("disabled", 1),
          ("enabled", 2))
    )


_AcsSensors1WireTableAnalogAlarm_Type.__name__ = "Integer32"
_AcsSensors1WireTableAnalogAlarm_Object = MibTableColumn
acsSensors1WireTableAnalogAlarm = _AcsSensors1WireTableAnalogAlarm_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 20, 1, 16),
    _AcsSensors1WireTableAnalogAlarm_Type()
)
acsSensors1WireTableAnalogAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsSensors1WireTableAnalogAlarm.setStatus("current")


class _AcsSensors1WireTableContactAlarm1_Type(Integer32):
    """Custom type acsSensors1WireTableContactAlarm1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("disabled", 1),
          ("alarmWhenOpen", 2),
          ("alarmWhenClosed", 3))
    )


_AcsSensors1WireTableContactAlarm1_Type.__name__ = "Integer32"
_AcsSensors1WireTableContactAlarm1_Object = MibTableColumn
acsSensors1WireTableContactAlarm1 = _AcsSensors1WireTableContactAlarm1_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 20, 1, 17),
    _AcsSensors1WireTableContactAlarm1_Type()
)
acsSensors1WireTableContactAlarm1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsSensors1WireTableContactAlarm1.setStatus("current")


class _AcsSensors1WireTableContactAlarm2_Type(Integer32):
    """Custom type acsSensors1WireTableContactAlarm2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("disabled", 1),
          ("alarmWhenOpen", 2),
          ("alarmWhenClosed", 3))
    )


_AcsSensors1WireTableContactAlarm2_Type.__name__ = "Integer32"
_AcsSensors1WireTableContactAlarm2_Object = MibTableColumn
acsSensors1WireTableContactAlarm2 = _AcsSensors1WireTableContactAlarm2_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 20, 1, 18),
    _AcsSensors1WireTableContactAlarm2_Type()
)
acsSensors1WireTableContactAlarm2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsSensors1WireTableContactAlarm2.setStatus("current")


class _AcsSensors1WireTableContactAlarm3_Type(Integer32):
    """Custom type acsSensors1WireTableContactAlarm3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("disabled", 1),
          ("alarmWhenOpen", 2),
          ("alarmWhenClosed", 3))
    )


_AcsSensors1WireTableContactAlarm3_Type.__name__ = "Integer32"
_AcsSensors1WireTableContactAlarm3_Object = MibTableColumn
acsSensors1WireTableContactAlarm3 = _AcsSensors1WireTableContactAlarm3_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 20, 1, 19),
    _AcsSensors1WireTableContactAlarm3_Type()
)
acsSensors1WireTableContactAlarm3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsSensors1WireTableContactAlarm3.setStatus("current")


class _AcsSensors1WireTableLeakFilterTime_Type(Integer32):
    """Custom type acsSensors1WireTableLeakFilterTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("filter-time-15", 1),
          ("filter-time-30", 2),
          ("filter-time-60", 3),
          ("filter-time-120", 4))
    )


_AcsSensors1WireTableLeakFilterTime_Type.__name__ = "Integer32"
_AcsSensors1WireTableLeakFilterTime_Object = MibTableColumn
acsSensors1WireTableLeakFilterTime = _AcsSensors1WireTableLeakFilterTime_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 20, 1, 20),
    _AcsSensors1WireTableLeakFilterTime_Type()
)
acsSensors1WireTableLeakFilterTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsSensors1WireTableLeakFilterTime.setStatus("current")


class _AcsSensors1WireTableLeakAlarm_Type(Integer32):
    """Custom type acsSensors1WireTableLeakAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("disabled", 1),
          ("enabled", 2))
    )


_AcsSensors1WireTableLeakAlarm_Type.__name__ = "Integer32"
_AcsSensors1WireTableLeakAlarm_Object = MibTableColumn
acsSensors1WireTableLeakAlarm = _AcsSensors1WireTableLeakAlarm_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 20, 1, 21),
    _AcsSensors1WireTableLeakAlarm_Type()
)
acsSensors1WireTableLeakAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsSensors1WireTableLeakAlarm.setStatus("current")


class _AcsSensors1WireTableLeakCableFailAlarm_Type(Integer32):
    """Custom type acsSensors1WireTableLeakCableFailAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("disabled", 1),
          ("enabled", 2))
    )


_AcsSensors1WireTableLeakCableFailAlarm_Type.__name__ = "Integer32"
_AcsSensors1WireTableLeakCableFailAlarm_Object = MibTableColumn
acsSensors1WireTableLeakCableFailAlarm = _AcsSensors1WireTableLeakCableFailAlarm_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 20, 1, 22),
    _AcsSensors1WireTableLeakCableFailAlarm_Type()
)
acsSensors1WireTableLeakCableFailAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsSensors1WireTableLeakCableFailAlarm.setStatus("current")
_AcsSensorsDigitalInTable_Object = MibTable
acsSensorsDigitalInTable = _AcsSensorsDigitalInTable_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 21)
)
if mibBuilder.loadTexts:
    acsSensorsDigitalInTable.setStatus("current")
_AcsSensorsDigitalInTableEntry_Object = MibTableRow
acsSensorsDigitalInTableEntry = _AcsSensorsDigitalInTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 21, 1)
)
acsSensorsDigitalInTableEntry.setIndexNames(
    (0, "ACS8000-MIB", "acsSensorsDigitalInTablePosition"),
)
if mibBuilder.loadTexts:
    acsSensorsDigitalInTableEntry.setStatus("current")


class _AcsSensorsDigitalInTablePosition_Type(Integer32):
    """Custom type acsSensorsDigitalInTablePosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AcsSensorsDigitalInTablePosition_Type.__name__ = "Integer32"
_AcsSensorsDigitalInTablePosition_Object = MibTableColumn
acsSensorsDigitalInTablePosition = _AcsSensorsDigitalInTablePosition_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 21, 1, 1),
    _AcsSensorsDigitalInTablePosition_Type()
)
acsSensorsDigitalInTablePosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSensorsDigitalInTablePosition.setStatus("current")
_AcsSensorsDigitalInTableName_Type = DisplayString
_AcsSensorsDigitalInTableName_Object = MibTableColumn
acsSensorsDigitalInTableName = _AcsSensorsDigitalInTableName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 21, 1, 2),
    _AcsSensorsDigitalInTableName_Type()
)
acsSensorsDigitalInTableName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsSensorsDigitalInTableName.setStatus("current")
_AcsSensorsDigitalInTableLocation_Type = DisplayString
_AcsSensorsDigitalInTableLocation_Object = MibTableColumn
acsSensorsDigitalInTableLocation = _AcsSensorsDigitalInTableLocation_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 21, 1, 3),
    _AcsSensorsDigitalInTableLocation_Type()
)
acsSensorsDigitalInTableLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsSensorsDigitalInTableLocation.setStatus("current")


class _AcsSensorsDigitalInTableType_Type(Integer32):
    """Custom type acsSensorsDigitalInTableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("custom", 0),
          ("vibration", 1),
          ("smoke-ad-s", 2),
          ("leak-sn-l", 3),
          ("door", 4),
          ("motion-ad-im", 5))
    )


_AcsSensorsDigitalInTableType_Type.__name__ = "Integer32"
_AcsSensorsDigitalInTableType_Object = MibTableColumn
acsSensorsDigitalInTableType = _AcsSensorsDigitalInTableType_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 21, 1, 4),
    _AcsSensorsDigitalInTableType_Type()
)
acsSensorsDigitalInTableType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsSensorsDigitalInTableType.setStatus("current")


class _AcsSensorsDigitalInTableValue_Type(Integer32):
    """Custom type acsSensorsDigitalInTableValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("open", 1),
          ("closed", 2))
    )


_AcsSensorsDigitalInTableValue_Type.__name__ = "Integer32"
_AcsSensorsDigitalInTableValue_Object = MibTableColumn
acsSensorsDigitalInTableValue = _AcsSensorsDigitalInTableValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 21, 1, 5),
    _AcsSensorsDigitalInTableValue_Type()
)
acsSensorsDigitalInTableValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSensorsDigitalInTableValue.setStatus("current")


class _AcsSensorsDigitalInTableAlarm_Type(Integer32):
    """Custom type acsSensorsDigitalInTableAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("alarmWhenOpen", 2),
          ("alarmWhenClosed", 3))
    )


_AcsSensorsDigitalInTableAlarm_Type.__name__ = "Integer32"
_AcsSensorsDigitalInTableAlarm_Object = MibTableColumn
acsSensorsDigitalInTableAlarm = _AcsSensorsDigitalInTableAlarm_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 7, 21, 1, 6),
    _AcsSensorsDigitalInTableAlarm_Type()
)
acsSensorsDigitalInTableAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsSensorsDigitalInTableAlarm.setStatus("current")
_AcsModems_ObjectIdentity = ObjectIdentity
acsModems = _AcsModems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 8)
)


class _AcsModemsNumberOfModems_Type(Integer32):
    """Custom type acsModemsNumberOfModems based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_AcsModemsNumberOfModems_Type.__name__ = "Integer32"
_AcsModemsNumberOfModems_Object = MibScalar
acsModemsNumberOfModems = _AcsModemsNumberOfModems_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 8, 1),
    _AcsModemsNumberOfModems_Type()
)
acsModemsNumberOfModems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsModemsNumberOfModems.setStatus("current")
_AcsModemsTable_Object = MibTable
acsModemsTable = _AcsModemsTable_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 8, 2)
)
if mibBuilder.loadTexts:
    acsModemsTable.setStatus("current")
_AcsModemsTableEntry_Object = MibTableRow
acsModemsTableEntry = _AcsModemsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 8, 2, 1)
)
acsModemsTableEntry.setIndexNames(
    (0, "ACS8000-MIB", "acsModemsTableNumber"),
)
if mibBuilder.loadTexts:
    acsModemsTableEntry.setStatus("current")


class _AcsModemsTableNumber_Type(Integer32):
    """Custom type acsModemsTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 49),
    )


_AcsModemsTableNumber_Type.__name__ = "Integer32"
_AcsModemsTableNumber_Object = MibTableColumn
acsModemsTableNumber = _AcsModemsTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 8, 2, 1, 1),
    _AcsModemsTableNumber_Type()
)
acsModemsTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsModemsTableNumber.setStatus("current")


class _AcsModemsTableDeviceName_Type(DisplayString):
    """Custom type acsModemsTableDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_AcsModemsTableDeviceName_Type.__name__ = "DisplayString"
_AcsModemsTableDeviceName_Object = MibTableColumn
acsModemsTableDeviceName = _AcsModemsTableDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 8, 2, 1, 2),
    _AcsModemsTableDeviceName_Type()
)
acsModemsTableDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsModemsTableDeviceName.setStatus("current")


class _AcsModemsTableStatus_Type(Integer32):
    """Custom type acsModemsTableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AcsModemsTableStatus_Type.__name__ = "Integer32"
_AcsModemsTableStatus_Object = MibTableColumn
acsModemsTableStatus = _AcsModemsTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 8, 2, 1, 3),
    _AcsModemsTableStatus_Type()
)
acsModemsTableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsModemsTableStatus.setStatus("current")


class _AcsModemsTableProfile_Type(Integer32):
    """Custom type acsModemsTableProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unconfigured", 1),
          ("dialIn", 2),
          ("dialOut", 3))
    )


_AcsModemsTableProfile_Type.__name__ = "Integer32"
_AcsModemsTableProfile_Object = MibTableColumn
acsModemsTableProfile = _AcsModemsTableProfile_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 8, 2, 1, 4),
    _AcsModemsTableProfile_Type()
)
acsModemsTableProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsModemsTableProfile.setStatus("current")


class _AcsModemsTablePhoneNumber_Type(DisplayString):
    """Custom type acsModemsTablePhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_AcsModemsTablePhoneNumber_Type.__name__ = "DisplayString"
_AcsModemsTablePhoneNumber_Object = MibTableColumn
acsModemsTablePhoneNumber = _AcsModemsTablePhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 8, 2, 1, 5),
    _AcsModemsTablePhoneNumber_Type()
)
acsModemsTablePhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsModemsTablePhoneNumber.setStatus("current")


class _AcsModemsTableComSpeed_Type(Integer32):
    """Custom type acsModemsTableComSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1200,
              2400,
              4800,
              9600,
              19200,
              38400,
              57600,
              115200,
              230400,
              460800,
              921600)
        )
    )
    namedValues = NamedValues(
        *(("speed1200", 1200),
          ("speed2400", 2400),
          ("speed4800", 4800),
          ("speed9600", 9600),
          ("speed19200", 19200),
          ("speed38400", 38400),
          ("speed57600", 57600),
          ("speed115200", 115200),
          ("speed230400", 230400),
          ("speed460800", 460800),
          ("speed921600", 921600))
    )


_AcsModemsTableComSpeed_Type.__name__ = "Integer32"
_AcsModemsTableComSpeed_Object = MibTableColumn
acsModemsTableComSpeed = _AcsModemsTableComSpeed_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 8, 2, 1, 6),
    _AcsModemsTableComSpeed_Type()
)
acsModemsTableComSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsModemsTableComSpeed.setStatus("current")


class _AcsModemsTableInitChat_Type(DisplayString):
    """Custom type acsModemsTableInitChat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1200),
    )


_AcsModemsTableInitChat_Type.__name__ = "DisplayString"
_AcsModemsTableInitChat_Object = MibTableColumn
acsModemsTableInitChat = _AcsModemsTableInitChat_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 8, 2, 1, 7),
    _AcsModemsTableInitChat_Type()
)
acsModemsTableInitChat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsModemsTableInitChat.setStatus("current")


class _AcsModemsTablePppAddressConfig_Type(Integer32):
    """Custom type acsModemsTablePppAddressConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("none", 1),
          ("local", 2),
          ("remote", 3))
    )


_AcsModemsTablePppAddressConfig_Type.__name__ = "Integer32"
_AcsModemsTablePppAddressConfig_Object = MibTableColumn
acsModemsTablePppAddressConfig = _AcsModemsTablePppAddressConfig_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 8, 2, 1, 8),
    _AcsModemsTablePppAddressConfig_Type()
)
acsModemsTablePppAddressConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsModemsTablePppAddressConfig.setStatus("current")


class _AcsModemsTableLocalIpv4Address_Type(DisplayString):
    """Custom type acsModemsTableLocalIpv4Address based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_AcsModemsTableLocalIpv4Address_Type.__name__ = "DisplayString"
_AcsModemsTableLocalIpv4Address_Object = MibTableColumn
acsModemsTableLocalIpv4Address = _AcsModemsTableLocalIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 8, 2, 1, 9),
    _AcsModemsTableLocalIpv4Address_Type()
)
acsModemsTableLocalIpv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsModemsTableLocalIpv4Address.setStatus("current")


class _AcsModemsTableRemoteIpv4Address_Type(DisplayString):
    """Custom type acsModemsTableRemoteIpv4Address based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_AcsModemsTableRemoteIpv4Address_Type.__name__ = "DisplayString"
_AcsModemsTableRemoteIpv4Address_Object = MibTableColumn
acsModemsTableRemoteIpv4Address = _AcsModemsTableRemoteIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 8, 2, 1, 10),
    _AcsModemsTableRemoteIpv4Address_Type()
)
acsModemsTableRemoteIpv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsModemsTableRemoteIpv4Address.setStatus("current")


class _AcsModemsTableLocalIPv6Address_Type(DisplayString):
    """Custom type acsModemsTableLocalIPv6Address based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_AcsModemsTableLocalIPv6Address_Type.__name__ = "DisplayString"
_AcsModemsTableLocalIPv6Address_Object = MibTableColumn
acsModemsTableLocalIPv6Address = _AcsModemsTableLocalIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 8, 2, 1, 11),
    _AcsModemsTableLocalIPv6Address_Type()
)
acsModemsTableLocalIPv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsModemsTableLocalIPv6Address.setStatus("current")


class _AcsModemsTableRemoteIPv6Address_Type(DisplayString):
    """Custom type acsModemsTableRemoteIPv6Address based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_AcsModemsTableRemoteIPv6Address_Type.__name__ = "DisplayString"
_AcsModemsTableRemoteIPv6Address_Object = MibTableColumn
acsModemsTableRemoteIPv6Address = _AcsModemsTableRemoteIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 8, 2, 1, 12),
    _AcsModemsTableRemoteIPv6Address_Type()
)
acsModemsTableRemoteIPv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsModemsTableRemoteIPv6Address.setStatus("current")


class _AcsModemsTablePppAuthentication_Type(Integer32):
    """Custom type acsModemsTablePppAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noAuth", 1),
          ("localPap", 2),
          ("localChap", 3),
          ("localEap", 4),
          ("remoteChap", 5),
          ("remotePap", 6))
    )


_AcsModemsTablePppAuthentication_Type.__name__ = "Integer32"
_AcsModemsTablePppAuthentication_Object = MibTableColumn
acsModemsTablePppAuthentication = _AcsModemsTablePppAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 8, 2, 1, 13),
    _AcsModemsTablePppAuthentication_Type()
)
acsModemsTablePppAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsModemsTablePppAuthentication.setStatus("current")


class _AcsModemsTablePppRemoteUsername_Type(DisplayString):
    """Custom type acsModemsTablePppRemoteUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcsModemsTablePppRemoteUsername_Type.__name__ = "DisplayString"
_AcsModemsTablePppRemoteUsername_Object = MibTableColumn
acsModemsTablePppRemoteUsername = _AcsModemsTablePppRemoteUsername_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 8, 2, 1, 14),
    _AcsModemsTablePppRemoteUsername_Type()
)
acsModemsTablePppRemoteUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsModemsTablePppRemoteUsername.setStatus("current")


class _AcsModemsTablePppRemotePassphrase_Type(DisplayString):
    """Custom type acsModemsTablePppRemotePassphrase based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcsModemsTablePppRemotePassphrase_Type.__name__ = "DisplayString"
_AcsModemsTablePppRemotePassphrase_Object = MibTableColumn
acsModemsTablePppRemotePassphrase = _AcsModemsTablePppRemotePassphrase_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 8, 2, 1, 15),
    _AcsModemsTablePppRemotePassphrase_Type()
)
acsModemsTablePppRemotePassphrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsModemsTablePppRemotePassphrase.setStatus("current")
_AcsModemsTableChapInterval_Type = Integer32
_AcsModemsTableChapInterval_Object = MibTableColumn
acsModemsTableChapInterval = _AcsModemsTableChapInterval_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 8, 2, 1, 16),
    _AcsModemsTableChapInterval_Type()
)
acsModemsTableChapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsModemsTableChapInterval.setStatus("current")
_AcsModemsTableChapMaxChallenge_Type = Integer32
_AcsModemsTableChapMaxChallenge_Object = MibTableColumn
acsModemsTableChapMaxChallenge = _AcsModemsTableChapMaxChallenge_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 8, 2, 1, 17),
    _AcsModemsTableChapMaxChallenge_Type()
)
acsModemsTableChapMaxChallenge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsModemsTableChapMaxChallenge.setStatus("current")
_AcsModemsTableChapRestart_Type = Integer32
_AcsModemsTableChapRestart_Object = MibTableColumn
acsModemsTableChapRestart = _AcsModemsTableChapRestart_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 8, 2, 1, 18),
    _AcsModemsTableChapRestart_Type()
)
acsModemsTableChapRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsModemsTableChapRestart.setStatus("current")
_AcsModemsTablePppIdleTimeout_Type = Integer32
_AcsModemsTablePppIdleTimeout_Object = MibTableColumn
acsModemsTablePppIdleTimeout = _AcsModemsTablePppIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 8, 2, 1, 19),
    _AcsModemsTablePppIdleTimeout_Type()
)
acsModemsTablePppIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsModemsTablePppIdleTimeout.setStatus("current")


class _AcsModemsTableModel_Type(DisplayString):
    """Custom type acsModemsTableModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcsModemsTableModel_Type.__name__ = "DisplayString"
_AcsModemsTableModel_Object = MibTableColumn
acsModemsTableModel = _AcsModemsTableModel_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 8, 2, 1, 20),
    _AcsModemsTableModel_Type()
)
acsModemsTableModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsModemsTableModel.setStatus("current")


class _AcsModemsTableCellProvider_Type(DisplayString):
    """Custom type acsModemsTableCellProvider based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcsModemsTableCellProvider_Type.__name__ = "DisplayString"
_AcsModemsTableCellProvider_Object = MibTableColumn
acsModemsTableCellProvider = _AcsModemsTableCellProvider_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 8, 2, 1, 21),
    _AcsModemsTableCellProvider_Type()
)
acsModemsTableCellProvider.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsModemsTableCellProvider.setStatus("current")


class _AcsModemsTableCellRegistration_Type(DisplayString):
    """Custom type acsModemsTableCellRegistration based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcsModemsTableCellRegistration_Type.__name__ = "DisplayString"
_AcsModemsTableCellRegistration_Object = MibTableColumn
acsModemsTableCellRegistration = _AcsModemsTableCellRegistration_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 8, 2, 1, 22),
    _AcsModemsTableCellRegistration_Type()
)
acsModemsTableCellRegistration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsModemsTableCellRegistration.setStatus("current")


class _AcsModemsTableCCID_Type(DisplayString):
    """Custom type acsModemsTableCCID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcsModemsTableCCID_Type.__name__ = "DisplayString"
_AcsModemsTableCCID_Object = MibTableColumn
acsModemsTableCCID = _AcsModemsTableCCID_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 8, 2, 1, 23),
    _AcsModemsTableCCID_Type()
)
acsModemsTableCCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsModemsTableCCID.setStatus("current")


class _AcsModemsTableIMSI_Type(DisplayString):
    """Custom type acsModemsTableIMSI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcsModemsTableIMSI_Type.__name__ = "DisplayString"
_AcsModemsTableIMSI_Object = MibTableColumn
acsModemsTableIMSI = _AcsModemsTableIMSI_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 8, 2, 1, 24),
    _AcsModemsTableIMSI_Type()
)
acsModemsTableIMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsModemsTableIMSI.setStatus("current")


class _AcsModemsTableIMEI_Type(DisplayString):
    """Custom type acsModemsTableIMEI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcsModemsTableIMEI_Type.__name__ = "DisplayString"
_AcsModemsTableIMEI_Object = MibTableColumn
acsModemsTableIMEI = _AcsModemsTableIMEI_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 8, 2, 1, 25),
    _AcsModemsTableIMEI_Type()
)
acsModemsTableIMEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsModemsTableIMEI.setStatus("current")


class _AcsModemsTableCellStatus_Type(DisplayString):
    """Custom type acsModemsTableCellStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AcsModemsTableCellStatus_Type.__name__ = "DisplayString"
_AcsModemsTableCellStatus_Object = MibTableColumn
acsModemsTableCellStatus = _AcsModemsTableCellStatus_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 8, 2, 1, 26),
    _AcsModemsTableCellStatus_Type()
)
acsModemsTableCellStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsModemsTableCellStatus.setStatus("current")


class _AcsModemsTableAPN_Type(DisplayString):
    """Custom type acsModemsTableAPN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AcsModemsTableAPN_Type.__name__ = "DisplayString"
_AcsModemsTableAPN_Object = MibTableColumn
acsModemsTableAPN = _AcsModemsTableAPN_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 8, 2, 1, 27),
    _AcsModemsTableAPN_Type()
)
acsModemsTableAPN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsModemsTableAPN.setStatus("current")
_AcsModemsTableMtuSize_Type = Integer32
_AcsModemsTableMtuSize_Object = MibTableColumn
acsModemsTableMtuSize = _AcsModemsTableMtuSize_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 8, 2, 1, 28),
    _AcsModemsTableMtuSize_Type()
)
acsModemsTableMtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsModemsTableMtuSize.setStatus("current")


class _AcsModemsTableReplaceDefaultRoute_Type(Integer32):
    """Custom type acsModemsTableReplaceDefaultRoute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("disabled", 1),
          ("enabled", 2))
    )


_AcsModemsTableReplaceDefaultRoute_Type.__name__ = "Integer32"
_AcsModemsTableReplaceDefaultRoute_Object = MibTableColumn
acsModemsTableReplaceDefaultRoute = _AcsModemsTableReplaceDefaultRoute_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 8, 2, 1, 29),
    _AcsModemsTableReplaceDefaultRoute_Type()
)
acsModemsTableReplaceDefaultRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsModemsTableReplaceDefaultRoute.setStatus("current")


class _AcsModemsTablePersistMode_Type(Integer32):
    """Custom type acsModemsTablePersistMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("disabled", 1),
          ("enabled", 2))
    )


_AcsModemsTablePersistMode_Type.__name__ = "Integer32"
_AcsModemsTablePersistMode_Object = MibTableColumn
acsModemsTablePersistMode = _AcsModemsTablePersistMode_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 8, 2, 1, 30),
    _AcsModemsTablePersistMode_Type()
)
acsModemsTablePersistMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsModemsTablePersistMode.setStatus("current")


class _AcsModemsTableSignalQualityCheck_Type(Integer32):
    """Custom type acsModemsTableSignalQualityCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("no-action", 1),
          ("signalCheck", 2))
    )


_AcsModemsTableSignalQualityCheck_Type.__name__ = "Integer32"
_AcsModemsTableSignalQualityCheck_Object = MibTableColumn
acsModemsTableSignalQualityCheck = _AcsModemsTableSignalQualityCheck_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 8, 2, 1, 31),
    _AcsModemsTableSignalQualityCheck_Type()
)
acsModemsTableSignalQualityCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsModemsTableSignalQualityCheck.setStatus("current")


class _AcsModemsTableSignalQualityDisplay_Type(DisplayString):
    """Custom type acsModemsTableSignalQualityDisplay based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AcsModemsTableSignalQualityDisplay_Type.__name__ = "DisplayString"
_AcsModemsTableSignalQualityDisplay_Object = MibTableColumn
acsModemsTableSignalQualityDisplay = _AcsModemsTableSignalQualityDisplay_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 8, 2, 1, 32),
    _AcsModemsTableSignalQualityDisplay_Type()
)
acsModemsTableSignalQualityDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsModemsTableSignalQualityDisplay.setStatus("current")


class _AcsModemsTableSIMStatus_Type(Integer32):
    """Custom type acsModemsTableSIMStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ready", 1),
          ("waitingForPIN", 2),
          ("waitingForUnlockCode", 3),
          ("errorReadingSIM", 4))
    )


_AcsModemsTableSIMStatus_Type.__name__ = "Integer32"
_AcsModemsTableSIMStatus_Object = MibTableColumn
acsModemsTableSIMStatus = _AcsModemsTableSIMStatus_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 8, 2, 1, 33),
    _AcsModemsTableSIMStatus_Type()
)
acsModemsTableSIMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsModemsTableSIMStatus.setStatus("current")


class _AcsModemsTableSIMPINEntry_Type(DisplayString):
    """Custom type acsModemsTableSIMPINEntry based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AcsModemsTableSIMPINEntry_Type.__name__ = "DisplayString"
_AcsModemsTableSIMPINEntry_Object = MibTableColumn
acsModemsTableSIMPINEntry = _AcsModemsTableSIMPINEntry_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 8, 2, 1, 34),
    _AcsModemsTableSIMPINEntry_Type()
)
acsModemsTableSIMPINEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsModemsTableSIMPINEntry.setStatus("current")


class _AcsModemsTableSIMUnlockCodeEntry_Type(DisplayString):
    """Custom type acsModemsTableSIMUnlockCodeEntry based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AcsModemsTableSIMUnlockCodeEntry_Type.__name__ = "DisplayString"
_AcsModemsTableSIMUnlockCodeEntry_Object = MibTableColumn
acsModemsTableSIMUnlockCodeEntry = _AcsModemsTableSIMUnlockCodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 8, 2, 1, 35),
    _AcsModemsTableSIMUnlockCodeEntry_Type()
)
acsModemsTableSIMUnlockCodeEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsModemsTableSIMUnlockCodeEntry.setStatus("current")


class _AcsModemsTableCellTestLastStarted_Type(DisplayString):
    """Custom type acsModemsTableCellTestLastStarted based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcsModemsTableCellTestLastStarted_Type.__name__ = "DisplayString"
_AcsModemsTableCellTestLastStarted_Object = MibTableColumn
acsModemsTableCellTestLastStarted = _AcsModemsTableCellTestLastStarted_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 8, 2, 1, 36),
    _AcsModemsTableCellTestLastStarted_Type()
)
acsModemsTableCellTestLastStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsModemsTableCellTestLastStarted.setStatus("current")


class _AcsModemsTableCellTestLastResult_Type(DisplayString):
    """Custom type acsModemsTableCellTestLastResult based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_AcsModemsTableCellTestLastResult_Type.__name__ = "DisplayString"
_AcsModemsTableCellTestLastResult_Object = MibTableColumn
acsModemsTableCellTestLastResult = _AcsModemsTableCellTestLastResult_Object(
    (1, 3, 6, 1, 4, 1, 10418, 26, 2, 8, 2, 1, 37),
    _AcsModemsTableCellTestLastResult_Type()
)
acsModemsTableCellTestLastResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsModemsTableCellTestLastResult.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACS8000-MIB",
    **{"PowerSupplyState": PowerSupplyState,
       "SerialPortSpeed": SerialPortSpeed,
       "SerialPortSignalState": SerialPortSignalState,
       "SerialPortPinOut": SerialPortPinOut,
       "acs": acs,
       "acsProducts": acsProducts,
       "acs8048": acs8048,
       "acs8032": acs8032,
       "acs8016": acs8016,
       "acs8008": acs8008,
       "acs808": acs808,
       "acs804": acs804,
       "acs802": acs802,
       "acsManagement": acsManagement,
       "acsAppliance": acsAppliance,
       "acsHostName": acsHostName,
       "acsProductModel": acsProductModel,
       "acsPartNumber": acsPartNumber,
       "acsSerialNumber": acsSerialNumber,
       "acsEIDNumber": acsEIDNumber,
       "acsBootcodeVersion": acsBootcodeVersion,
       "acsFirmwareVersion": acsFirmwareVersion,
       "acsPowerSupply": acsPowerSupply,
       "acsPowerSupplyNumber": acsPowerSupplyNumber,
       "acsPowerSupplyStatePw1": acsPowerSupplyStatePw1,
       "acsPowerSupplyStatePw2": acsPowerSupplyStatePw2,
       "acsReboot": acsReboot,
       "acsScheduledTasksTable": acsScheduledTasksTable,
       "acsScheduledTasksTableEntry": acsScheduledTasksTableEntry,
       "acsScheduledTasksTableIndex": acsScheduledTasksTableIndex,
       "acsScheduledTasksTableType": acsScheduledTasksTableType,
       "acsScheduledTasksTableName": acsScheduledTasksTableName,
       "acsScheduledTasksTableStatus": acsScheduledTasksTableStatus,
       "acsScheduledTasksTableFrequency": acsScheduledTasksTableFrequency,
       "acsScheduledTasksTableDay": acsScheduledTasksTableDay,
       "acsScheduledTasksTableDate": acsScheduledTasksTableDate,
       "acsScheduledTasksTableTime": acsScheduledTasksTableTime,
       "acsScheduledTasksTableLastStarted": acsScheduledTasksTableLastStarted,
       "acsScheduledTasksTableLastResult": acsScheduledTasksTableLastResult,
       "acsScheduledTasksTableScript": acsScheduledTasksTableScript,
       "acsScheduledTasksTableIpAddress": acsScheduledTasksTableIpAddress,
       "acsSessions": acsSessions,
       "acsActiveSessionsNumberOfSession": acsActiveSessionsNumberOfSession,
       "acsActiveSessionsTable": acsActiveSessionsTable,
       "acsActiveSessionsTableEntry": acsActiveSessionsTableEntry,
       "acsActiveSessionsTableIndex": acsActiveSessionsTableIndex,
       "acsActiveSessionsTableUser": acsActiveSessionsTableUser,
       "acsActiveSessionsTableGroup": acsActiveSessionsTableGroup,
       "acsActiveSessionsTableType": acsActiveSessionsTableType,
       "acsActiveSessionsTableConnection": acsActiveSessionsTableConnection,
       "acsActiveSessionsTableSessionTime": acsActiveSessionsTableSessionTime,
       "acsActiveSessionsTableFrom": acsActiveSessionsTableFrom,
       "acsActiveSessionsTableKill": acsActiveSessionsTableKill,
       "acsSerialPort": acsSerialPort,
       "acsSerialPortNumberOfPorts": acsSerialPortNumberOfPorts,
       "acsSerialPortTable": acsSerialPortTable,
       "acsSerialPortTableEntry": acsSerialPortTableEntry,
       "acsSerialPortTableNumber": acsSerialPortTableNumber,
       "acsSerialPortTableDeviceName": acsSerialPortTableDeviceName,
       "acsSerialPortTableStatus": acsSerialPortTableStatus,
       "acsSerialPortTableName": acsSerialPortTableName,
       "acsSerialPortTableProfile": acsSerialPortTableProfile,
       "acsSerialPortTablePinOut": acsSerialPortTablePinOut,
       "acsSerialPortTableComSpeed": acsSerialPortTableComSpeed,
       "acsSerialPortTableComParity": acsSerialPortTableComParity,
       "acsSerialPortTableComDataSize": acsSerialPortTableComDataSize,
       "acsSerialPortTableComStopBits": acsSerialPortTableComStopBits,
       "acsSerialPortTableComFlowControl": acsSerialPortTableComFlowControl,
       "acsSerialPortTableSignalStateDTR": acsSerialPortTableSignalStateDTR,
       "acsSerialPortTableSignalStateDCD": acsSerialPortTableSignalStateDCD,
       "acsSerialPortTableSignalStateRTS": acsSerialPortTableSignalStateRTS,
       "acsSerialPortTableSignalStateCTS": acsSerialPortTableSignalStateCTS,
       "acsSerialPortTableTxBytes": acsSerialPortTableTxBytes,
       "acsSerialPortTableRxBytes": acsSerialPortTableRxBytes,
       "acsSerialPortTableFrameError": acsSerialPortTableFrameError,
       "acsSerialPortTableParityError": acsSerialPortTableParityError,
       "acsSerialPortTableBreak": acsSerialPortTableBreak,
       "acsSerialPortTableOverrun": acsSerialPortTableOverrun,
       "acsSerialPortTableResetCounters": acsSerialPortTableResetCounters,
       "acsSerialPortTableXcvrStatus": acsSerialPortTableXcvrStatus,
       "acsPowerMgmt": acsPowerMgmt,
       "acsPowerMgmtNumSerialPorts": acsPowerMgmtNumSerialPorts,
       "acsPowerMgmtSerialTable": acsPowerMgmtSerialTable,
       "acsPowerMgmtSerialTableEntry": acsPowerMgmtSerialTableEntry,
       "acsPowerMgmtSerialTableIndex": acsPowerMgmtSerialTableIndex,
       "acsPowerMgmtSerialTablePortNumber": acsPowerMgmtSerialTablePortNumber,
       "acsPowerMgmtSerialTableDeviceName": acsPowerMgmtSerialTableDeviceName,
       "acsPowerMgmtSerialTableNumberPDUs": acsPowerMgmtSerialTableNumberPDUs,
       "acsPowerMgmtSerialTableNumberUPS": acsPowerMgmtSerialTableNumberUPS,
       "acsPowerMgmtPDUTable": acsPowerMgmtPDUTable,
       "acsPowerMgmtPDUTableEntry": acsPowerMgmtPDUTableEntry,
       "acsPowerMgmtPDUTablePortNumber": acsPowerMgmtPDUTablePortNumber,
       "acsPowerMgmtPDUTablePduIndex": acsPowerMgmtPDUTablePduIndex,
       "acsPowerMgmtPDUTablePduId": acsPowerMgmtPDUTablePduId,
       "acsPowerMgmtPDUTablePortName": acsPowerMgmtPDUTablePortName,
       "acsPowerMgmtPDUTableModel": acsPowerMgmtPDUTableModel,
       "acsPowerMgmtPDUTableVendor": acsPowerMgmtPDUTableVendor,
       "acsPowerMgmtPDUTableFirmwareVersion": acsPowerMgmtPDUTableFirmwareVersion,
       "acsPowerMgmtPDUTableNumberOfOutlets": acsPowerMgmtPDUTableNumberOfOutlets,
       "acsPowerMgmtPDUTableCurrentNOS": acsPowerMgmtPDUTableCurrentNOS,
       "acsPowerMgmtPDUTableCurrent1Value": acsPowerMgmtPDUTableCurrent1Value,
       "acsPowerMgmtPDUTableCurrent1Max": acsPowerMgmtPDUTableCurrent1Max,
       "acsPowerMgmtPDUTableCurrent2Value": acsPowerMgmtPDUTableCurrent2Value,
       "acsPowerMgmtPDUTableCurrent2Max": acsPowerMgmtPDUTableCurrent2Max,
       "acsPowerMgmtPDUTableCurrent3Value": acsPowerMgmtPDUTableCurrent3Value,
       "acsPowerMgmtPDUTableCurrent3Max": acsPowerMgmtPDUTableCurrent3Max,
       "acsPowerMgmtPDUTableTemperatureNOS": acsPowerMgmtPDUTableTemperatureNOS,
       "acsPowerMgmtPDUTableTemperature1Value": acsPowerMgmtPDUTableTemperature1Value,
       "acsPowerMgmtPDUTableTemperature1Max": acsPowerMgmtPDUTableTemperature1Max,
       "acsPowerMgmtPDUTableTemperature2Value": acsPowerMgmtPDUTableTemperature2Value,
       "acsPowerMgmtPDUTableTemperature2Max": acsPowerMgmtPDUTableTemperature2Max,
       "acsPowerMgmtPDUTableTemperature3Value": acsPowerMgmtPDUTableTemperature3Value,
       "acsPowerMgmtPDUTableTemperature3Max": acsPowerMgmtPDUTableTemperature3Max,
       "acsPowerMgmtPDUTableHumidityNOS": acsPowerMgmtPDUTableHumidityNOS,
       "acsPowerMgmtPDUTableHumidity1Value": acsPowerMgmtPDUTableHumidity1Value,
       "acsPowerMgmtPDUTableHumidity1Max": acsPowerMgmtPDUTableHumidity1Max,
       "acsPowerMgmtPDUTableHumidity2Value": acsPowerMgmtPDUTableHumidity2Value,
       "acsPowerMgmtPDUTableHumidity2Max": acsPowerMgmtPDUTableHumidity2Max,
       "acsPowerMgmtPDUTableHumidity3Value": acsPowerMgmtPDUTableHumidity3Value,
       "acsPowerMgmtPDUTableHumidity3Max": acsPowerMgmtPDUTableHumidity3Max,
       "acsPowerMgmtPDUTableVoltageNOS": acsPowerMgmtPDUTableVoltageNOS,
       "acsPowerMgmtPDUTableVoltage1Value": acsPowerMgmtPDUTableVoltage1Value,
       "acsPowerMgmtPDUTableVoltage1Max": acsPowerMgmtPDUTableVoltage1Max,
       "acsPowerMgmtPDUTableVoltage2Value": acsPowerMgmtPDUTableVoltage2Value,
       "acsPowerMgmtPDUTableVoltage2Max": acsPowerMgmtPDUTableVoltage2Max,
       "acsPowerMgmtPDUTableVoltage3Value": acsPowerMgmtPDUTableVoltage3Value,
       "acsPowerMgmtPDUTableVoltage3Max": acsPowerMgmtPDUTableVoltage3Max,
       "acsPowerMgmtPDUTableNumberOfPhases": acsPowerMgmtPDUTableNumberOfPhases,
       "acsPowerMgmtPDUTableNumberOfBanks": acsPowerMgmtPDUTableNumberOfBanks,
       "acsPowerMgmtPDUTableCurrentValue": acsPowerMgmtPDUTableCurrentValue,
       "acsPowerMgmtPDUTableCurrentMax": acsPowerMgmtPDUTableCurrentMax,
       "acsPowerMgmtPDUTableCurrentMin": acsPowerMgmtPDUTableCurrentMin,
       "acsPowerMgmtPDUTableCurrentAvg": acsPowerMgmtPDUTableCurrentAvg,
       "acsPowerMgmtPDUTableCurrentReset": acsPowerMgmtPDUTableCurrentReset,
       "acsPowerMgmtPDUTableVoltageType": acsPowerMgmtPDUTableVoltageType,
       "acsPowerMgmtPDUTableVoltageValue": acsPowerMgmtPDUTableVoltageValue,
       "acsPowerMgmtPDUTableVoltageMax": acsPowerMgmtPDUTableVoltageMax,
       "acsPowerMgmtPDUTableVoltageMin": acsPowerMgmtPDUTableVoltageMin,
       "acsPowerMgmtPDUTableVoltageAvg": acsPowerMgmtPDUTableVoltageAvg,
       "acsPowerMgmtPDUTableVoltageReset": acsPowerMgmtPDUTableVoltageReset,
       "acsPowerMgmtPDUTablePowerType": acsPowerMgmtPDUTablePowerType,
       "acsPowerMgmtPDUTablePowerValue": acsPowerMgmtPDUTablePowerValue,
       "acsPowerMgmtPDUTablePowerMax": acsPowerMgmtPDUTablePowerMax,
       "acsPowerMgmtPDUTablePowerMin": acsPowerMgmtPDUTablePowerMin,
       "acsPowerMgmtPDUTablePowerAvg": acsPowerMgmtPDUTablePowerAvg,
       "acsPowerMgmtPDUTablePowerReset": acsPowerMgmtPDUTablePowerReset,
       "acsPowerMgmtPDUTablePowerFactorType": acsPowerMgmtPDUTablePowerFactorType,
       "acsPowerMgmtPDUTablePowerFactorValue": acsPowerMgmtPDUTablePowerFactorValue,
       "acsPowerMgmtPDUTablePowerFactorMax": acsPowerMgmtPDUTablePowerFactorMax,
       "acsPowerMgmtPDUTablePowerFactorMin": acsPowerMgmtPDUTablePowerFactorMin,
       "acsPowerMgmtPDUTablePowerFactorAvg": acsPowerMgmtPDUTablePowerFactorAvg,
       "acsPowerMgmtPDUTablePowerFactorReset": acsPowerMgmtPDUTablePowerFactorReset,
       "acsPowerMgmtPDUTableAlarm": acsPowerMgmtPDUTableAlarm,
       "acsPowerMgmtPDUTableEnvSensors": acsPowerMgmtPDUTableEnvSensors,
       "acsPowerMgmtPDUTableAgentSerialNumber": acsPowerMgmtPDUTableAgentSerialNumber,
       "acsPowerMgmtPDUTablePduModelNumber": acsPowerMgmtPDUTablePduModelNumber,
       "acsPowerMgmtPDUTablePduSerialNumber": acsPowerMgmtPDUTablePduSerialNumber,
       "acsPowerMgmtPDUTablePduPartNumber": acsPowerMgmtPDUTablePduPartNumber,
       "acsPowerMgmtTotalNumberOfOutlets": acsPowerMgmtTotalNumberOfOutlets,
       "acsPowerMgmtOutletsTable": acsPowerMgmtOutletsTable,
       "acsPowerMgmtOutletsTableEntry": acsPowerMgmtOutletsTableEntry,
       "acsPowerMgmtOutletsTablePortNumber": acsPowerMgmtOutletsTablePortNumber,
       "acsPowerMgmtOutletsTablePduNumber": acsPowerMgmtOutletsTablePduNumber,
       "acsPowerMgmtOutletsTableNumber": acsPowerMgmtOutletsTableNumber,
       "acsPowerMgmtOutletsTableName": acsPowerMgmtOutletsTableName,
       "acsPowerMgmtOutletsTableStatus": acsPowerMgmtOutletsTableStatus,
       "acsPowerMgmtOutletsTablePowerControl": acsPowerMgmtOutletsTablePowerControl,
       "acsPowerMgmtOutletsTablePortName": acsPowerMgmtOutletsTablePortName,
       "acsPowerMgmtOutletsTablePduId": acsPowerMgmtOutletsTablePduId,
       "acsPowerMgmtNumberOfOutletGroup": acsPowerMgmtNumberOfOutletGroup,
       "acsPowerMgmtGroupTable": acsPowerMgmtGroupTable,
       "acsPowerMgmtGroupTableEntry": acsPowerMgmtGroupTableEntry,
       "acsPowerMgmtGroupTableIndex": acsPowerMgmtGroupTableIndex,
       "acsPowerMgmtGroupTableName": acsPowerMgmtGroupTableName,
       "acsPowerMgmtGroupTableStatus": acsPowerMgmtGroupTableStatus,
       "acsPowerMgmtGroupTablePowerControl": acsPowerMgmtGroupTablePowerControl,
       "acsPowerMgmtPhasesTable": acsPowerMgmtPhasesTable,
       "acsPowerMgmtPhasesTableEntry": acsPowerMgmtPhasesTableEntry,
       "acsPowerMgmtPhasesTablePortNumber": acsPowerMgmtPhasesTablePortNumber,
       "acsPowerMgmtPhasesTablePduIndex": acsPowerMgmtPhasesTablePduIndex,
       "acsPowerMgmtPhasesTablePhaseIndex": acsPowerMgmtPhasesTablePhaseIndex,
       "acsPowerMgmtPhasesTablePhaseName": acsPowerMgmtPhasesTablePhaseName,
       "acsPowerMgmtPhasesTablePduId": acsPowerMgmtPhasesTablePduId,
       "acsPowerMgmtPhasesTablePortName": acsPowerMgmtPhasesTablePortName,
       "acsPowerMgmtPhasesTableCurrentValue": acsPowerMgmtPhasesTableCurrentValue,
       "acsPowerMgmtPhasesTableCurrentMax": acsPowerMgmtPhasesTableCurrentMax,
       "acsPowerMgmtPhasesTableCurrentMin": acsPowerMgmtPhasesTableCurrentMin,
       "acsPowerMgmtPhasesTableCurrentAvg": acsPowerMgmtPhasesTableCurrentAvg,
       "acsPowerMgmtPhasesTableCurrentReset": acsPowerMgmtPhasesTableCurrentReset,
       "acsPowerMgmtPhasesTableVoltageType": acsPowerMgmtPhasesTableVoltageType,
       "acsPowerMgmtPhasesTableVoltageValue": acsPowerMgmtPhasesTableVoltageValue,
       "acsPowerMgmtPhasesTableVoltageMax": acsPowerMgmtPhasesTableVoltageMax,
       "acsPowerMgmtPhasesTableVoltageMin": acsPowerMgmtPhasesTableVoltageMin,
       "acsPowerMgmtPhasesTableVoltageAvg": acsPowerMgmtPhasesTableVoltageAvg,
       "acsPowerMgmtPhasesTableVoltageReset": acsPowerMgmtPhasesTableVoltageReset,
       "acsPowerMgmtPhasesTablePowerType": acsPowerMgmtPhasesTablePowerType,
       "acsPowerMgmtPhasesTablePowerValue": acsPowerMgmtPhasesTablePowerValue,
       "acsPowerMgmtPhasesTablePowerMax": acsPowerMgmtPhasesTablePowerMax,
       "acsPowerMgmtPhasesTablePowerMin": acsPowerMgmtPhasesTablePowerMin,
       "acsPowerMgmtPhasesTablePowerAvg": acsPowerMgmtPhasesTablePowerAvg,
       "acsPowerMgmtPhasesTablePowerReset": acsPowerMgmtPhasesTablePowerReset,
       "acsPowerMgmtPhasesTablePowerFactorType": acsPowerMgmtPhasesTablePowerFactorType,
       "acsPowerMgmtPhasesTablePowerFactorValue": acsPowerMgmtPhasesTablePowerFactorValue,
       "acsPowerMgmtPhasesTablePowerFactorMax": acsPowerMgmtPhasesTablePowerFactorMax,
       "acsPowerMgmtPhasesTablePowerFactorMin": acsPowerMgmtPhasesTablePowerFactorMin,
       "acsPowerMgmtPhasesTablePowerFactorAvg": acsPowerMgmtPhasesTablePowerFactorAvg,
       "acsPowerMgmtPhasesTablePowerFactorReset": acsPowerMgmtPhasesTablePowerFactorReset,
       "acsPowerMgmtPhasesTableAlarm": acsPowerMgmtPhasesTableAlarm,
       "acsPowerMgmtBanksTable": acsPowerMgmtBanksTable,
       "acsPowerMgmtBanksTableEntry": acsPowerMgmtBanksTableEntry,
       "acsPowerMgmtBanksTablePortNumber": acsPowerMgmtBanksTablePortNumber,
       "acsPowerMgmtBanksTablePduIndex": acsPowerMgmtBanksTablePduIndex,
       "acsPowerMgmtBanksTableBankIndex": acsPowerMgmtBanksTableBankIndex,
       "acsPowerMgmtBanksTableBankName": acsPowerMgmtBanksTableBankName,
       "acsPowerMgmtBanksTablePduId": acsPowerMgmtBanksTablePduId,
       "acsPowerMgmtBanksTablePortName": acsPowerMgmtBanksTablePortName,
       "acsPowerMgmtBanksTableCurrentValue": acsPowerMgmtBanksTableCurrentValue,
       "acsPowerMgmtBanksTableCurrentMax": acsPowerMgmtBanksTableCurrentMax,
       "acsPowerMgmtBanksTableCurrentMin": acsPowerMgmtBanksTableCurrentMin,
       "acsPowerMgmtBanksTableCurrentAvg": acsPowerMgmtBanksTableCurrentAvg,
       "acsPowerMgmtBanksTableCurrentReset": acsPowerMgmtBanksTableCurrentReset,
       "acsPowerMgmtBanksTableVoltageType": acsPowerMgmtBanksTableVoltageType,
       "acsPowerMgmtBanksTableVoltageValue": acsPowerMgmtBanksTableVoltageValue,
       "acsPowerMgmtBanksTableVoltageMax": acsPowerMgmtBanksTableVoltageMax,
       "acsPowerMgmtBanksTableVoltageMin": acsPowerMgmtBanksTableVoltageMin,
       "acsPowerMgmtBanksTableVoltageAvg": acsPowerMgmtBanksTableVoltageAvg,
       "acsPowerMgmtBanksTableVoltageReset": acsPowerMgmtBanksTableVoltageReset,
       "acsPowerMgmtBanksTablePowerType": acsPowerMgmtBanksTablePowerType,
       "acsPowerMgmtBanksTablePowerValue": acsPowerMgmtBanksTablePowerValue,
       "acsPowerMgmtBanksTablePowerMax": acsPowerMgmtBanksTablePowerMax,
       "acsPowerMgmtBanksTablePowerMin": acsPowerMgmtBanksTablePowerMin,
       "acsPowerMgmtBanksTablePowerAvg": acsPowerMgmtBanksTablePowerAvg,
       "acsPowerMgmtBanksTablePowerReset": acsPowerMgmtBanksTablePowerReset,
       "acsPowerMgmtBanksTablePowerFactorType": acsPowerMgmtBanksTablePowerFactorType,
       "acsPowerMgmtBanksTablePowerFactorValue": acsPowerMgmtBanksTablePowerFactorValue,
       "acsPowerMgmtBanksTablePowerFactorMax": acsPowerMgmtBanksTablePowerFactorMax,
       "acsPowerMgmtBanksTablePowerFactorMin": acsPowerMgmtBanksTablePowerFactorMin,
       "acsPowerMgmtBanksTablePowerFactorAvg": acsPowerMgmtBanksTablePowerFactorAvg,
       "acsPowerMgmtBanksTablePowerFactorReset": acsPowerMgmtBanksTablePowerFactorReset,
       "acsPowerMgmtBanksTableAlarm": acsPowerMgmtBanksTableAlarm,
       "acsPowerMgmtEnvMonTable": acsPowerMgmtEnvMonTable,
       "acsPowerMgmtEnvMonTableEntry": acsPowerMgmtEnvMonTableEntry,
       "acsPowerMgmtEnvMonTablePortNumber": acsPowerMgmtEnvMonTablePortNumber,
       "acsPowerMgmtEnvMonTablePduIndex": acsPowerMgmtEnvMonTablePduIndex,
       "acsPowerMgmtEnvMonTableIndex": acsPowerMgmtEnvMonTableIndex,
       "acsPowerMgmtEnvMonTableName": acsPowerMgmtEnvMonTableName,
       "acsPowerMgmtEnvMonTablePduId": acsPowerMgmtEnvMonTablePduId,
       "acsPowerMgmtEnvMonTablePortName": acsPowerMgmtEnvMonTablePortName,
       "acsPowerMgmtEnvMonTableType": acsPowerMgmtEnvMonTableType,
       "acsPowerMgmtEnvMonTableStatus": acsPowerMgmtEnvMonTableStatus,
       "acsPowerMgmtEnvMonTableValue": acsPowerMgmtEnvMonTableValue,
       "acsPowerMgmtEnvMonTableMaxValue": acsPowerMgmtEnvMonTableMaxValue,
       "acsPowerMgmtOutElecMonTable": acsPowerMgmtOutElecMonTable,
       "acsPowerMgmtOutElecMonTableEntry": acsPowerMgmtOutElecMonTableEntry,
       "acsPowerMgmtOutElecMonTablePortNumber": acsPowerMgmtOutElecMonTablePortNumber,
       "acsPowerMgmtOutElecMonTablePduNumber": acsPowerMgmtOutElecMonTablePduNumber,
       "acsPowerMgmtOutElecMonTableNumber": acsPowerMgmtOutElecMonTableNumber,
       "acsPowerMgmtOutElecMonTableCurrentValue": acsPowerMgmtOutElecMonTableCurrentValue,
       "acsPowerMgmtOutElecMonTableCurrentMax": acsPowerMgmtOutElecMonTableCurrentMax,
       "acsPowerMgmtOutElecMonTableCurrentMin": acsPowerMgmtOutElecMonTableCurrentMin,
       "acsPowerMgmtOutElecMonTableCurrentAvg": acsPowerMgmtOutElecMonTableCurrentAvg,
       "acsPowerMgmtOutElecMonTableCurrentReset": acsPowerMgmtOutElecMonTableCurrentReset,
       "acsPowerMgmtOutElecMonTablePowerValue": acsPowerMgmtOutElecMonTablePowerValue,
       "acsPowerMgmtOutElecMonTablePowerMax": acsPowerMgmtOutElecMonTablePowerMax,
       "acsPowerMgmtOutElecMonTablePowerMin": acsPowerMgmtOutElecMonTablePowerMin,
       "acsPowerMgmtOutElecMonTablePowerAvg": acsPowerMgmtOutElecMonTablePowerAvg,
       "acsPowerMgmtOutElecMonTablePowerReset": acsPowerMgmtOutElecMonTablePowerReset,
       "acsPowerMgmtOutElecMonTableVoltageValue": acsPowerMgmtOutElecMonTableVoltageValue,
       "acsPowerMgmtOutElecMonTableVoltageMax": acsPowerMgmtOutElecMonTableVoltageMax,
       "acsPowerMgmtOutElecMonTableVoltageMin": acsPowerMgmtOutElecMonTableVoltageMin,
       "acsPowerMgmtOutElecMonTableVoltageAvg": acsPowerMgmtOutElecMonTableVoltageAvg,
       "acsPowerMgmtOutElecMonTableVoltageReset": acsPowerMgmtOutElecMonTableVoltageReset,
       "acsPowerMgmtOutElecMonTablePowerFactorValue": acsPowerMgmtOutElecMonTablePowerFactorValue,
       "acsPowerMgmtOutElecMonTablePowerFactorMax": acsPowerMgmtOutElecMonTablePowerFactorMax,
       "acsPowerMgmtOutElecMonTablePowerFactorMin": acsPowerMgmtOutElecMonTablePowerFactorMin,
       "acsPowerMgmtOutElecMonTablePowerFactorAvg": acsPowerMgmtOutElecMonTablePowerFactorAvg,
       "acsPowerMgmtOutElecMonTablePowerFactorReset": acsPowerMgmtOutElecMonTablePowerFactorReset,
       "acsPowerMgmtOutElecMonTableAlarm": acsPowerMgmtOutElecMonTableAlarm,
       "acsPowerMgmtUPSTable": acsPowerMgmtUPSTable,
       "acsPowerMgmtUPSTableEntry": acsPowerMgmtUPSTableEntry,
       "acsPowerMgmtUPSTablePortNumber": acsPowerMgmtUPSTablePortNumber,
       "acsPowerMgmtUPSTableUpsIndex": acsPowerMgmtUPSTableUpsIndex,
       "acsPowerMgmtUPSTableUpsId": acsPowerMgmtUPSTableUpsId,
       "acsPowerMgmtUPSTablePortName": acsPowerMgmtUPSTablePortName,
       "acsPowerMgmtUPSTableModel": acsPowerMgmtUPSTableModel,
       "acsPowerMgmtUPSTableVendor": acsPowerMgmtUPSTableVendor,
       "acsPowerMgmtUPSTableFirmwareVersion": acsPowerMgmtUPSTableFirmwareVersion,
       "acsPowerMgmtUPSTableAgentFirmwareVersion": acsPowerMgmtUPSTableAgentFirmwareVersion,
       "acsPowerMgmtUPSTableSystemStatus": acsPowerMgmtUPSTableSystemStatus,
       "acsPowerMgmtUPSTableInputBlackOutCount": acsPowerMgmtUPSTableInputBlackOutCount,
       "acsPowerMgmtUPSTableInputBrownOutCount": acsPowerMgmtUPSTableInputBrownOutCount,
       "acsPowerMgmtUPSTableInletAirTemperature": acsPowerMgmtUPSTableInletAirTemperature,
       "acsPowerMgmtUPSTableNumberOutletGroups": acsPowerMgmtUPSTableNumberOutletGroups,
       "acsPowerMgmtUPSTableUPSSerialNumber": acsPowerMgmtUPSTableUPSSerialNumber,
       "acsPowerMgmtUPSTableUPSManufactureDate": acsPowerMgmtUPSTableUPSManufactureDate,
       "acsPowerMgmtUPSTableAutoRestartDelay": acsPowerMgmtUPSTableAutoRestartDelay,
       "acsPowerMgmtUPSTableAutoRestartControl": acsPowerMgmtUPSTableAutoRestartControl,
       "acsPowerMgmtUPSTableAudibleAlarmControl": acsPowerMgmtUPSTableAudibleAlarmControl,
       "acsPowerMgmtUPSTableSilenceAlarm": acsPowerMgmtUPSTableSilenceAlarm,
       "acsPowerMgmtUPSTableInverterState": acsPowerMgmtUPSTableInverterState,
       "acsPowerMgmtUPSTableDCConverterStatus": acsPowerMgmtUPSTableDCConverterStatus,
       "acsPowerMgmtUPSTableShutdownReason": acsPowerMgmtUPSTableShutdownReason,
       "acsPowerMgmtUPSTableUPSTopology": acsPowerMgmtUPSTableUPSTopology,
       "acsPowerMgmtUPSTableBypassInverterInputConfig": acsPowerMgmtUPSTableBypassInverterInputConfig,
       "acsPowerMgmtUPSInputTable": acsPowerMgmtUPSInputTable,
       "acsPowerMgmtUPSInputTableEntry": acsPowerMgmtUPSInputTableEntry,
       "acsPowerMgmtUPSInputTablePortNumber": acsPowerMgmtUPSInputTablePortNumber,
       "acsPowerMgmtUPSInputTableUpsIndex": acsPowerMgmtUPSInputTableUpsIndex,
       "acsPowerMgmtUPSInputTableFrequency": acsPowerMgmtUPSInputTableFrequency,
       "acsPowerMgmtUPSInputTableRMSVoltageL1N": acsPowerMgmtUPSInputTableRMSVoltageL1N,
       "acsPowerMgmtUPSInputTableRMSVoltageL1L2": acsPowerMgmtUPSInputTableRMSVoltageL1L2,
       "acsPowerMgmtUPSInputTableRMSVoltageL2N": acsPowerMgmtUPSInputTableRMSVoltageL2N,
       "acsPowerMgmtUPSInputTableRMSCurrentL1": acsPowerMgmtUPSInputTableRMSCurrentL1,
       "acsPowerMgmtUPSInputTableRMSCurrentL2": acsPowerMgmtUPSInputTableRMSCurrentL2,
       "acsPowerMgmtUPSInputTableMaxVoltageL1N": acsPowerMgmtUPSInputTableMaxVoltageL1N,
       "acsPowerMgmtUPSInputTableMinVoltageL1N": acsPowerMgmtUPSInputTableMinVoltageL1N,
       "acsPowerMgmtUPSInputTableMaxVoltageL2N": acsPowerMgmtUPSInputTableMaxVoltageL2N,
       "acsPowerMgmtUPSInputTableMinVoltageL2N": acsPowerMgmtUPSInputTableMinVoltageL2N,
       "acsPowerMgmtUPSInputTableNominalVoltage": acsPowerMgmtUPSInputTableNominalVoltage,
       "acsPowerMgmtUPSInputTableNominalFrequency": acsPowerMgmtUPSInputTableNominalFrequency,
       "acsPowerMgmtUPSInputTableNominalCurrent": acsPowerMgmtUPSInputTableNominalCurrent,
       "acsPowerMgmtUPSInputTableEnergy": acsPowerMgmtUPSInputTableEnergy,
       "acsPowerMgmtUPSInputTablePowerFactorL1N": acsPowerMgmtUPSInputTablePowerFactorL1N,
       "acsPowerMgmtUPSInputTablePowerFactorL2N": acsPowerMgmtUPSInputTablePowerFactorL2N,
       "acsPowerMgmtUPSBypassTable": acsPowerMgmtUPSBypassTable,
       "acsPowerMgmtUPSBypassTableEntry": acsPowerMgmtUPSBypassTableEntry,
       "acsPowerMgmtUPSBypassTablePortNumber": acsPowerMgmtUPSBypassTablePortNumber,
       "acsPowerMgmtUPSBypassTableUpsIndex": acsPowerMgmtUPSBypassTableUpsIndex,
       "acsPowerMgmtUPSBypassTableRMSVoltageL1N": acsPowerMgmtUPSBypassTableRMSVoltageL1N,
       "acsPowerMgmtUPSBypassTableRMSVoltageL1L2": acsPowerMgmtUPSBypassTableRMSVoltageL1L2,
       "acsPowerMgmtUPSBypassTableRMSVoltageL2N": acsPowerMgmtUPSBypassTableRMSVoltageL2N,
       "acsPowerMgmtUPSBypassTableRMSCurrent": acsPowerMgmtUPSBypassTableRMSCurrent,
       "acsPowerMgmtUPSBypassTableRMSCurrentL2": acsPowerMgmtUPSBypassTableRMSCurrentL2,
       "acsPowerMgmtUPSBypassTableInputFrequency": acsPowerMgmtUPSBypassTableInputFrequency,
       "acsPowerMgmtUPSBypassTableNominalVoltage": acsPowerMgmtUPSBypassTableNominalVoltage,
       "acsPowerMgmtUPSBatteryTable": acsPowerMgmtUPSBatteryTable,
       "acsPowerMgmtUPSBatteryTableEntry": acsPowerMgmtUPSBatteryTableEntry,
       "acsPowerMgmtUPSBatteryTablePortNumber": acsPowerMgmtUPSBatteryTablePortNumber,
       "acsPowerMgmtUPSBatteryTableUpsIndex": acsPowerMgmtUPSBatteryTableUpsIndex,
       "acsPowerMgmtUPSBatteryTableDCBusVoltage": acsPowerMgmtUPSBatteryTableDCBusVoltage,
       "acsPowerMgmtUPSBatteryTableTimeRemaining": acsPowerMgmtUPSBatteryTableTimeRemaining,
       "acsPowerMgmtUPSBatteryTablePercentageCharge": acsPowerMgmtUPSBatteryTablePercentageCharge,
       "acsPowerMgmtUPSBatteryTableChargeStatus": acsPowerMgmtUPSBatteryTableChargeStatus,
       "acsPowerMgmtUPSBatteryTableLowBatteryWarningTime": acsPowerMgmtUPSBatteryTableLowBatteryWarningTime,
       "acsPowerMgmtUPSBatteryTableTestResult": acsPowerMgmtUPSBatteryTableTestResult,
       "acsPowerMgmtUPSBatteryTableDCBusNominalVoltage": acsPowerMgmtUPSBatteryTableDCBusNominalVoltage,
       "acsPowerMgmtUPSBatteryTableNominalBatteryCapacity": acsPowerMgmtUPSBatteryTableNominalBatteryCapacity,
       "acsPowerMgmtUPSBatteryTableBatteryFloatVoltage": acsPowerMgmtUPSBatteryTableBatteryFloatVoltage,
       "acsPowerMgmtUPSBatteryTableBatteryCabinetType": acsPowerMgmtUPSBatteryTableBatteryCabinetType,
       "acsPowerMgmtUPSBatteryTableBatteryNumberOfEBC": acsPowerMgmtUPSBatteryTableBatteryNumberOfEBC,
       "acsPowerMgmtUPSBatteryTableBatteryRating": acsPowerMgmtUPSBatteryTableBatteryRating,
       "acsPowerMgmtUPSBatteryTableBatteryDischargeTime": acsPowerMgmtUPSBatteryTableBatteryDischargeTime,
       "acsPowerMgmtUPSBatteryTableBatteryChargeCompensating": acsPowerMgmtUPSBatteryTableBatteryChargeCompensating,
       "acsPowerMgmtUPSBatteryTableBatteryChargerState": acsPowerMgmtUPSBatteryTableBatteryChargerState,
       "acsPowerMgmtUPSBatteryTableStartBatteryTest": acsPowerMgmtUPSBatteryTableStartBatteryTest,
       "acsPowerMgmtUPSBatteryTableBatteryStatus": acsPowerMgmtUPSBatteryTableBatteryStatus,
       "acsPowerMgmtUPSBatteryTableBatteryTotalDischargeTime": acsPowerMgmtUPSBatteryTableBatteryTotalDischargeTime,
       "acsPowerMgmtUPSBatteryTableBatteryDischargeCount": acsPowerMgmtUPSBatteryTableBatteryDischargeCount,
       "acsPowerMgmtUPSBatteryTableBatteryCurrent": acsPowerMgmtUPSBatteryTableBatteryCurrent,
       "acsPowerMgmtUPSOutputTable": acsPowerMgmtUPSOutputTable,
       "acsPowerMgmtUPSOutputTableEntry": acsPowerMgmtUPSOutputTableEntry,
       "acsPowerMgmtUPSOutputTablePortNumber": acsPowerMgmtUPSOutputTablePortNumber,
       "acsPowerMgmtUPSOutputTableUpsIndex": acsPowerMgmtUPSOutputTableUpsIndex,
       "acsPowerMgmtUPSOutputTableApparentPower": acsPowerMgmtUPSOutputTableApparentPower,
       "acsPowerMgmtUPSOutputTableFrequency": acsPowerMgmtUPSOutputTableFrequency,
       "acsPowerMgmtUPSOutputTablePercentPower": acsPowerMgmtUPSOutputTablePercentPower,
       "acsPowerMgmtUPSOutputTablePercentPowerL1": acsPowerMgmtUPSOutputTablePercentPowerL1,
       "acsPowerMgmtUPSOutputTablePercentPowerL2": acsPowerMgmtUPSOutputTablePercentPowerL2,
       "acsPowerMgmtUPSOutputTablePower": acsPowerMgmtUPSOutputTablePower,
       "acsPowerMgmtUPSOutputTableRMSCurrentL1": acsPowerMgmtUPSOutputTableRMSCurrentL1,
       "acsPowerMgmtUPSOutputTableRMSCurrentL2": acsPowerMgmtUPSOutputTableRMSCurrentL2,
       "acsPowerMgmtUPSOutputTableRMSVoltageL1N": acsPowerMgmtUPSOutputTableRMSVoltageL1N,
       "acsPowerMgmtUPSOutputTableRMSVoltageL2N": acsPowerMgmtUPSOutputTableRMSVoltageL2N,
       "acsPowerMgmtUPSOutputTableRMSVoltageL1L2": acsPowerMgmtUPSOutputTableRMSVoltageL1L2,
       "acsPowerMgmtUPSOutputOffDelay": acsPowerMgmtUPSOutputOffDelay,
       "acsPowerMgmtUPSOutputOnDelay": acsPowerMgmtUPSOutputOnDelay,
       "acsPowerMgmtUPSOutputCycleDelay": acsPowerMgmtUPSOutputCycleDelay,
       "acsPowerMgmtUPSOutputTableMaxVoltageL1": acsPowerMgmtUPSOutputTableMaxVoltageL1,
       "acsPowerMgmtUPSOutputTableMinVoltageL1": acsPowerMgmtUPSOutputTableMinVoltageL1,
       "acsPowerMgmtUPSOutputTableMaxVoltageL2": acsPowerMgmtUPSOutputTableMaxVoltageL2,
       "acsPowerMgmtUPSOutputTableMinVoltageL2": acsPowerMgmtUPSOutputTableMinVoltageL2,
       "acsPowerMgmtUPSOutputTableNominalVoltage": acsPowerMgmtUPSOutputTableNominalVoltage,
       "acsPowerMgmtUPSOutputTablePowerNominalFrequency": acsPowerMgmtUPSOutputTablePowerNominalFrequency,
       "acsPowerMgmtUPSOutputTablePowerApparentPowerRating": acsPowerMgmtUPSOutputTablePowerApparentPowerRating,
       "acsPowerMgmtUPSOutputTablePowerNominalPowerFactor": acsPowerMgmtUPSOutputTablePowerNominalPowerFactor,
       "acsPowerMgmtUPSOutputTablePowerPowerFactorCorrection": acsPowerMgmtUPSOutputTablePowerPowerFactorCorrection,
       "acsPowerMgmtUPSOutputTablePowerL1": acsPowerMgmtUPSOutputTablePowerL1,
       "acsPowerMgmtUPSOutputTablePowerL2": acsPowerMgmtUPSOutputTablePowerL2,
       "acsPowerMgmtUPSOutputTableApparentPowerL1": acsPowerMgmtUPSOutputTableApparentPowerL1,
       "acsPowerMgmtUPSOutputTableApparentPowerL2": acsPowerMgmtUPSOutputTableApparentPowerL2,
       "acsPowerMgmtUPSOutputTablePowerFactorL1": acsPowerMgmtUPSOutputTablePowerFactorL1,
       "acsPowerMgmtUPSOutputTablePowerFactorL2": acsPowerMgmtUPSOutputTablePowerFactorL2,
       "acsPowerMgmtUPSEcoModeTable": acsPowerMgmtUPSEcoModeTable,
       "acsPowerMgmtUPSEcoModeTableEntry": acsPowerMgmtUPSEcoModeTableEntry,
       "acsPowerMgmtUPSEcoModeTablePortNumber": acsPowerMgmtUPSEcoModeTablePortNumber,
       "acsPowerMgmtUPSEcoModeTableUpsIndex": acsPowerMgmtUPSEcoModeTableUpsIndex,
       "acsPowerMgmtUPSEcoModeTableStatus": acsPowerMgmtUPSEcoModeTableStatus,
       "acsPowerMgmtUPSEcoModeTableStateControl": acsPowerMgmtUPSEcoModeTableStateControl,
       "acsPowerMgmtUPSOutletGroupTable": acsPowerMgmtUPSOutletGroupTable,
       "acsPowerMgmtUPSOutletGroupTableEntry": acsPowerMgmtUPSOutletGroupTableEntry,
       "acsPowerMgmtUPSOutletGroupTablePortNumber": acsPowerMgmtUPSOutletGroupTablePortNumber,
       "acsPowerMgmtUPSOutletGroupTableUpsIndex": acsPowerMgmtUPSOutletGroupTableUpsIndex,
       "acsPowerMgmtUPSOutletGroupTableNumber": acsPowerMgmtUPSOutletGroupTableNumber,
       "acsPowerMgmtUPSOutletGroupTableLabel": acsPowerMgmtUPSOutletGroupTableLabel,
       "acsPowerMgmtUPSOutletGroupTableState": acsPowerMgmtUPSOutletGroupTableState,
       "acsPowerMgmtUPSOutletGroupTablePowerControl": acsPowerMgmtUPSOutletGroupTablePowerControl,
       "acsTrapObject": acsTrapObject,
       "acsSensors": acsSensors,
       "acsSensorsInternalCurrentCPUTemperature": acsSensorsInternalCurrentCPUTemperature,
       "acsSensorsInternalMaxCPUTemperature": acsSensorsInternalMaxCPUTemperature,
       "acsSensorsInternalMaxCPUTemperatureThreshold": acsSensorsInternalMaxCPUTemperatureThreshold,
       "acsSensorsInternalMinCPUTemperature": acsSensorsInternalMinCPUTemperature,
       "acsSensorsInternalMinCPUTemperatureThreshold": acsSensorsInternalMinCPUTemperatureThreshold,
       "acsSensorsInternalCurrentBoardTemperature": acsSensorsInternalCurrentBoardTemperature,
       "acsSensorsInternalMaxBoardTemperature": acsSensorsInternalMaxBoardTemperature,
       "acsSensorsInternalMaxBoardTemperatureThreshold": acsSensorsInternalMaxBoardTemperatureThreshold,
       "acsSensorsInternalMinBoardTemperature": acsSensorsInternalMinBoardTemperature,
       "acsSensorsInternalMinBoardTemperatureThreshold": acsSensorsInternalMinBoardTemperatureThreshold,
       "acsSensorsVoltagePSInternal": acsSensorsVoltagePSInternal,
       "acsSensorsVoltagePLInternal": acsSensorsVoltagePLInternal,
       "acsSensorsVoltagePSAuxiliary": acsSensorsVoltagePSAuxiliary,
       "acsSensorsVoltagePLAuxiliary": acsSensorsVoltagePLAuxiliary,
       "acsSensorsVoltagePSDDR3": acsSensorsVoltagePSDDR3,
       "acsSensorsVoltagePLBlockRam": acsSensorsVoltagePLBlockRam,
       "acsSensorsVoltagePowerSupply1": acsSensorsVoltagePowerSupply1,
       "acsSensorsVoltagePowerSupply2": acsSensorsVoltagePowerSupply2,
       "acsSensors1WireUpdateControl": acsSensors1WireUpdateControl,
       "acsSensors1WireTable": acsSensors1WireTable,
       "acsSensors1WireTableEntry": acsSensors1WireTableEntry,
       "acsSensors1WireTableIndex": acsSensors1WireTableIndex,
       "acsSensors1WireTableName": acsSensors1WireTableName,
       "acsSensors1WireTableLocation": acsSensors1WireTableLocation,
       "acsSensors1WireTableAddress": acsSensors1WireTableAddress,
       "acsSensors1WireTableType": acsSensors1WireTableType,
       "acsSensors1WireTableUnit": acsSensors1WireTableUnit,
       "acsSensors1WireTableValue": acsSensors1WireTableValue,
       "acsSensors1WireTableValueMax": acsSensors1WireTableValueMax,
       "acsSensors1WireTableValueMin": acsSensors1WireTableValueMin,
       "acsSensors1WireTableValueAvg": acsSensors1WireTableValueAvg,
       "acsSensors1WireTableValueLowWarning": acsSensors1WireTableValueLowWarning,
       "acsSensors1WireTableValueLowCritical": acsSensors1WireTableValueLowCritical,
       "acsSensors1WireTableValueHighWarning": acsSensors1WireTableValueHighWarning,
       "acsSensors1WireTableValueHighCritical": acsSensors1WireTableValueHighCritical,
       "acsSensors1WireTableReset": acsSensors1WireTableReset,
       "acsSensors1WireTableAnalogAlarm": acsSensors1WireTableAnalogAlarm,
       "acsSensors1WireTableContactAlarm1": acsSensors1WireTableContactAlarm1,
       "acsSensors1WireTableContactAlarm2": acsSensors1WireTableContactAlarm2,
       "acsSensors1WireTableContactAlarm3": acsSensors1WireTableContactAlarm3,
       "acsSensors1WireTableLeakFilterTime": acsSensors1WireTableLeakFilterTime,
       "acsSensors1WireTableLeakAlarm": acsSensors1WireTableLeakAlarm,
       "acsSensors1WireTableLeakCableFailAlarm": acsSensors1WireTableLeakCableFailAlarm,
       "acsSensorsDigitalInTable": acsSensorsDigitalInTable,
       "acsSensorsDigitalInTableEntry": acsSensorsDigitalInTableEntry,
       "acsSensorsDigitalInTablePosition": acsSensorsDigitalInTablePosition,
       "acsSensorsDigitalInTableName": acsSensorsDigitalInTableName,
       "acsSensorsDigitalInTableLocation": acsSensorsDigitalInTableLocation,
       "acsSensorsDigitalInTableType": acsSensorsDigitalInTableType,
       "acsSensorsDigitalInTableValue": acsSensorsDigitalInTableValue,
       "acsSensorsDigitalInTableAlarm": acsSensorsDigitalInTableAlarm,
       "acsModems": acsModems,
       "acsModemsNumberOfModems": acsModemsNumberOfModems,
       "acsModemsTable": acsModemsTable,
       "acsModemsTableEntry": acsModemsTableEntry,
       "acsModemsTableNumber": acsModemsTableNumber,
       "acsModemsTableDeviceName": acsModemsTableDeviceName,
       "acsModemsTableStatus": acsModemsTableStatus,
       "acsModemsTableProfile": acsModemsTableProfile,
       "acsModemsTablePhoneNumber": acsModemsTablePhoneNumber,
       "acsModemsTableComSpeed": acsModemsTableComSpeed,
       "acsModemsTableInitChat": acsModemsTableInitChat,
       "acsModemsTablePppAddressConfig": acsModemsTablePppAddressConfig,
       "acsModemsTableLocalIpv4Address": acsModemsTableLocalIpv4Address,
       "acsModemsTableRemoteIpv4Address": acsModemsTableRemoteIpv4Address,
       "acsModemsTableLocalIPv6Address": acsModemsTableLocalIPv6Address,
       "acsModemsTableRemoteIPv6Address": acsModemsTableRemoteIPv6Address,
       "acsModemsTablePppAuthentication": acsModemsTablePppAuthentication,
       "acsModemsTablePppRemoteUsername": acsModemsTablePppRemoteUsername,
       "acsModemsTablePppRemotePassphrase": acsModemsTablePppRemotePassphrase,
       "acsModemsTableChapInterval": acsModemsTableChapInterval,
       "acsModemsTableChapMaxChallenge": acsModemsTableChapMaxChallenge,
       "acsModemsTableChapRestart": acsModemsTableChapRestart,
       "acsModemsTablePppIdleTimeout": acsModemsTablePppIdleTimeout,
       "acsModemsTableModel": acsModemsTableModel,
       "acsModemsTableCellProvider": acsModemsTableCellProvider,
       "acsModemsTableCellRegistration": acsModemsTableCellRegistration,
       "acsModemsTableCCID": acsModemsTableCCID,
       "acsModemsTableIMSI": acsModemsTableIMSI,
       "acsModemsTableIMEI": acsModemsTableIMEI,
       "acsModemsTableCellStatus": acsModemsTableCellStatus,
       "acsModemsTableAPN": acsModemsTableAPN,
       "acsModemsTableMtuSize": acsModemsTableMtuSize,
       "acsModemsTableReplaceDefaultRoute": acsModemsTableReplaceDefaultRoute,
       "acsModemsTablePersistMode": acsModemsTablePersistMode,
       "acsModemsTableSignalQualityCheck": acsModemsTableSignalQualityCheck,
       "acsModemsTableSignalQualityDisplay": acsModemsTableSignalQualityDisplay,
       "acsModemsTableSIMStatus": acsModemsTableSIMStatus,
       "acsModemsTableSIMPINEntry": acsModemsTableSIMPINEntry,
       "acsModemsTableSIMUnlockCodeEntry": acsModemsTableSIMUnlockCodeEntry,
       "acsModemsTableCellTestLastStarted": acsModemsTableCellTestLastStarted,
       "acsModemsTableCellTestLastResult": acsModemsTableCellTestLastResult}
)
