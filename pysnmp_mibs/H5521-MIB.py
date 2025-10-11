# SNMP MIB module (H5521-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/comet/H5521-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:16:13 2025
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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Comet_ObjectIdentity = ObjectIdentity
comet = _Comet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1)
)
_H5521_ObjectIdentity = ObjectIdentity
h5521 = _H5521_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2)
)
_Values_ObjectIdentity = ObjectIdentity
values = _Values_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1)
)


class _Co2_Type(DisplayString):
    """Custom type co2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Co2_Type.__name__ = "DisplayString"
_Co2_Object = MibScalar
co2 = _Co2_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 4),
    _Co2_Type()
)
co2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co2.setStatus("mandatory")


class _Re1_Type(DisplayString):
    """Custom type re1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Re1_Type.__name__ = "DisplayString"
_Re1_Object = MibScalar
re1 = _Re1_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 8),
    _Re1_Type()
)
re1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    re1.setStatus("mandatory")


class _Re2_Type(DisplayString):
    """Custom type re2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Re2_Type.__name__ = "DisplayString"
_Re2_Object = MibScalar
re2 = _Re2_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 9),
    _Re2_Type()
)
re2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    re2.setStatus("mandatory")


class _Co2Alarm1_Type(DisplayString):
    """Custom type co2Alarm1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Co2Alarm1_Type.__name__ = "DisplayString"
_Co2Alarm1_Object = MibScalar
co2Alarm1 = _Co2Alarm1_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 13),
    _Co2Alarm1_Type()
)
co2Alarm1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co2Alarm1.setStatus("mandatory")


class _Co2Alarm2_Type(DisplayString):
    """Custom type co2Alarm2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Co2Alarm2_Type.__name__ = "DisplayString"
_Co2Alarm2_Object = MibScalar
co2Alarm2 = _Co2Alarm2_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 17),
    _Co2Alarm2_Type()
)
co2Alarm2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co2Alarm2.setStatus("mandatory")


class _Co2Unit_Type(DisplayString):
    """Custom type co2Unit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Co2Unit_Type.__name__ = "DisplayString"
_Co2Unit_Object = MibScalar
co2Unit = _Co2Unit_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 24),
    _Co2Unit_Type()
)
co2Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co2Unit.setStatus("mandatory")
__pysmi_global_ObjectIdentity = ObjectIdentity
_pysmi_global = __pysmi_global_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 2)
)


class _SensorName_Type(DisplayString):
    """Custom type sensorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 68),
    )


_SensorName_Type.__name__ = "DisplayString"
_SensorName_Object = MibScalar
sensorName = _SensorName_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 1),
    _SensorName_Type()
)
sensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorName.setStatus("mandatory")


class _SerialNumber_Type(DisplayString):
    """Custom type serialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SerialNumber_Type.__name__ = "DisplayString"
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 2),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("mandatory")


class _DeviceType_Type(Integer32):
    """Custom type deviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_DeviceType_Type.__name__ = "Integer32"
_DeviceType_Object = MibScalar
deviceType = _DeviceType_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 3),
    _DeviceType_Type()
)
deviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceType.setStatus("mandatory")
_ValuesInt_ObjectIdentity = ObjectIdentity
valuesInt = _ValuesInt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 3)
)


class _Co2Int_Type(Integer32):
    """Custom type co2Int based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5000, 20000),
    )


_Co2Int_Type.__name__ = "Integer32"
_Co2Int_Object = MibScalar
co2Int = _Co2Int_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 4),
    _Co2Int_Type()
)
co2Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co2Int.setStatus("mandatory")


class _Re1Int_Type(Integer32):
    """Custom type re1Int based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Re1Int_Type.__name__ = "Integer32"
_Re1Int_Object = MibScalar
re1Int = _Re1Int_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 8),
    _Re1Int_Type()
)
re1Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    re1Int.setStatus("mandatory")


class _Re2Int_Type(Integer32):
    """Custom type re2Int based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Re2Int_Type.__name__ = "Integer32"
_Re2Int_Object = MibScalar
re2Int = _Re2Int_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 9),
    _Re2Int_Type()
)
re2Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    re2Int.setStatus("mandatory")


class _Co2Alarm1Int_Type(Integer32):
    """Custom type co2Alarm1Int based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Co2Alarm1Int_Type.__name__ = "Integer32"
_Co2Alarm1Int_Object = MibScalar
co2Alarm1Int = _Co2Alarm1Int_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 13),
    _Co2Alarm1Int_Type()
)
co2Alarm1Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co2Alarm1Int.setStatus("mandatory")


class _Co2Alarm2Int_Type(Integer32):
    """Custom type co2Alarm2Int based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Co2Alarm2Int_Type.__name__ = "Integer32"
_Co2Alarm2Int_Object = MibScalar
co2Alarm2Int = _Co2Alarm2Int_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 17),
    _Co2Alarm2Int_Type()
)
co2Alarm2Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co2Alarm2Int.setStatus("mandatory")
_Settings_ObjectIdentity = ObjectIdentity
settings = _Settings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4)
)


class _Co2Lim1Int_Type(Integer32):
    """Custom type co2Lim1Int based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5000, 20000),
    )


_Co2Lim1Int_Type.__name__ = "Integer32"
_Co2Lim1Int_Object = MibScalar
co2Lim1Int = _Co2Lim1Int_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 4),
    _Co2Lim1Int_Type()
)
co2Lim1Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co2Lim1Int.setStatus("mandatory")


class _Co2Lim2Int_Type(Integer32):
    """Custom type co2Lim2Int based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5000, 20000),
    )


_Co2Lim2Int_Type.__name__ = "Integer32"
_Co2Lim2Int_Object = MibScalar
co2Lim2Int = _Co2Lim2Int_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 8),
    _Co2Lim2Int_Type()
)
co2Lim2Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co2Lim2Int.setStatus("mandatory")


class _Co2Hyst1Int_Type(Integer32):
    """Custom type co2Hyst1Int based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Co2Hyst1Int_Type.__name__ = "Integer32"
_Co2Hyst1Int_Object = MibScalar
co2Hyst1Int = _Co2Hyst1Int_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 12),
    _Co2Hyst1Int_Type()
)
co2Hyst1Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co2Hyst1Int.setStatus("mandatory")


class _Co2Hyst2Int_Type(Integer32):
    """Custom type co2Hyst2Int based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Co2Hyst2Int_Type.__name__ = "Integer32"
_Co2Hyst2Int_Object = MibScalar
co2Hyst2Int = _Co2Hyst2Int_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 16),
    _Co2Hyst2Int_Type()
)
co2Hyst2Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co2Hyst2Int.setStatus("mandatory")


class _Co2Delay1Int_Type(Integer32):
    """Custom type co2Delay1Int based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_Co2Delay1Int_Type.__name__ = "Integer32"
_Co2Delay1Int_Object = MibScalar
co2Delay1Int = _Co2Delay1Int_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 20),
    _Co2Delay1Int_Type()
)
co2Delay1Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co2Delay1Int.setStatus("mandatory")


class _Co2Delay2Int_Type(Integer32):
    """Custom type co2Delay2Int based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_Co2Delay2Int_Type.__name__ = "Integer32"
_Co2Delay2Int_Object = MibScalar
co2Delay2Int = _Co2Delay2Int_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 24),
    _Co2Delay2Int_Type()
)
co2Delay2Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co2Delay2Int.setStatus("mandatory")


class _Co2Type1Int_Type(Integer32):
    """Custom type co2Type1Int based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Co2Type1Int_Type.__name__ = "Integer32"
_Co2Type1Int_Object = MibScalar
co2Type1Int = _Co2Type1Int_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 28),
    _Co2Type1Int_Type()
)
co2Type1Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co2Type1Int.setStatus("mandatory")


class _Co2Type2Int_Type(Integer32):
    """Custom type co2Type2Int based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Co2Type2Int_Type.__name__ = "Integer32"
_Co2Type2Int_Object = MibScalar
co2Type2Int = _Co2Type2Int_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 32),
    _Co2Type2Int_Type()
)
co2Type2Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co2Type2Int.setStatus("mandatory")
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 5)
)


class _MessageString_Type(DisplayString):
    """Custom type messageString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MessageString_Type.__name__ = "DisplayString"
_MessageString_Object = MibScalar
messageString = _MessageString_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 5, 1),
    _MessageString_Type()
)
messageString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    messageString.setStatus("mandatory")
_Tables_ObjectIdentity = ObjectIdentity
tables = _Tables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 6)
)
_HistoryTable_Object = MibTable
historyTable = _HistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    historyTable.setStatus("mandatory")
_HistoryEntry_Object = MibTableRow
historyEntry = _HistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1, 1)
)
historyEntry.setIndexNames(
    (0, "H5521-MIB", "histCO2"),
)
if mibBuilder.loadTexts:
    historyEntry.setStatus("optional")


class _HistCO2_Type(Integer32):
    """Custom type histCO2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5000, 20000),
    )


_HistCO2_Type.__name__ = "Integer32"
_HistCO2_Object = MibTableColumn
histCO2 = _HistCO2_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1, 1, 4),
    _HistCO2_Type()
)
histCO2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histCO2.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trapTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 0)
)
trapTest.setObjects(
      *(("H5521-MIB", "sensorName"),
        ("H5521-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapTest.setStatus(
        ""
    )

trapNTPError = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 1)
)
trapNTPError.setObjects(
      *(("H5521-MIB", "sensorName"),
        ("H5521-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapNTPError.setStatus(
        ""
    )

trapEmailErrLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 2)
)
trapEmailErrLogin.setObjects(
      *(("H5521-MIB", "sensorName"),
        ("H5521-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapEmailErrLogin.setStatus(
        ""
    )

trapEmailErrAuth = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 3)
)
trapEmailErrAuth.setObjects(
      *(("H5521-MIB", "sensorName"),
        ("H5521-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapEmailErrAuth.setStatus(
        ""
    )

trapEmailErrSome = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 4)
)
trapEmailErrSome.setObjects(
      *(("H5521-MIB", "sensorName"),
        ("H5521-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapEmailErrSome.setStatus(
        ""
    )

trapEmailErrSocket = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 5)
)
trapEmailErrSocket.setObjects(
      *(("H5521-MIB", "sensorName"),
        ("H5521-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapEmailErrSocket.setStatus(
        ""
    )

trapEmailErrDNS = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 6)
)
trapEmailErrDNS.setObjects(
      *(("H5521-MIB", "sensorName"),
        ("H5521-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapEmailErrDNS.setStatus(
        ""
    )

trapSOAPErrFile = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 7)
)
trapSOAPErrFile.setObjects(
      *(("H5521-MIB", "sensorName"),
        ("H5521-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapSOAPErrFile.setStatus(
        ""
    )

trapSOAPErrDNS = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 8)
)
trapSOAPErrDNS.setObjects(
      *(("H5521-MIB", "sensorName"),
        ("H5521-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapSOAPErrDNS.setStatus(
        ""
    )

trapSOAPErrSocket = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 9)
)
trapSOAPErrSocket.setObjects(
      *(("H5521-MIB", "sensorName"),
        ("H5521-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapSOAPErrSocket.setStatus(
        ""
    )

trapSOAPErrDelivery = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 10)
)
trapSOAPErrDelivery.setObjects(
      *(("H5521-MIB", "sensorName"),
        ("H5521-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapSOAPErrDelivery.setStatus(
        ""
    )

trapCO2Alarm1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 14)
)
trapCO2Alarm1.setObjects(
      *(("H5521-MIB", "sensorName"),
        ("H5521-MIB", "messageString"),
        ("H5521-MIB", "co2"),
        ("H5521-MIB", "co2Alarm1Int"))
)
if mibBuilder.loadTexts:
    trapCO2Alarm1.setStatus(
        ""
    )

trapCO2Alarm2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 24)
)
trapCO2Alarm2.setObjects(
      *(("H5521-MIB", "sensorName"),
        ("H5521-MIB", "messageString"),
        ("H5521-MIB", "co2"),
        ("H5521-MIB", "co2Alarm2Int"))
)
if mibBuilder.loadTexts:
    trapCO2Alarm2.setStatus(
        ""
    )

trapCO2ClrAlarm1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 34)
)
trapCO2ClrAlarm1.setObjects(
      *(("H5521-MIB", "sensorName"),
        ("H5521-MIB", "messageString"),
        ("H5521-MIB", "co2"),
        ("H5521-MIB", "co2Alarm1Int"))
)
if mibBuilder.loadTexts:
    trapCO2ClrAlarm1.setStatus(
        ""
    )

trapCO2ClrAlarm2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 44)
)
trapCO2ClrAlarm2.setObjects(
      *(("H5521-MIB", "sensorName"),
        ("H5521-MIB", "messageString"),
        ("H5521-MIB", "co2"),
        ("H5521-MIB", "co2Alarm2Int"))
)
if mibBuilder.loadTexts:
    trapCO2ClrAlarm2.setStatus(
        ""
    )

trapRelay1Closed = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 70)
)
trapRelay1Closed.setObjects(
      *(("H5521-MIB", "sensorName"),
        ("H5521-MIB", "messageString"),
        ("H5521-MIB", "re1Int"))
)
if mibBuilder.loadTexts:
    trapRelay1Closed.setStatus(
        ""
    )

trapRelay2Closed = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 71)
)
trapRelay2Closed.setObjects(
      *(("H5521-MIB", "sensorName"),
        ("H5521-MIB", "messageString"),
        ("H5521-MIB", "re2Int"))
)
if mibBuilder.loadTexts:
    trapRelay2Closed.setStatus(
        ""
    )

trapRelay1Open = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 72)
)
trapRelay1Open.setObjects(
      *(("H5521-MIB", "sensorName"),
        ("H5521-MIB", "messageString"),
        ("H5521-MIB", "re1Int"))
)
if mibBuilder.loadTexts:
    trapRelay1Open.setStatus(
        ""
    )

trapRelay2Open = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 73)
)
trapRelay2Open.setObjects(
      *(("H5521-MIB", "sensorName"),
        ("H5521-MIB", "messageString"),
        ("H5521-MIB", "re2Int"))
)
if mibBuilder.loadTexts:
    trapRelay2Open.setStatus(
        ""
    )

trapAcousticActivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 74)
)
trapAcousticActivated.setObjects(
      *(("H5521-MIB", "sensorName"),
        ("H5521-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapAcousticActivated.setStatus(
        ""
    )

trapAcousticDeactivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 75)
)
trapAcousticDeactivated.setObjects(
      *(("H5521-MIB", "sensorName"),
        ("H5521-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapAcousticDeactivated.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H5521-MIB",
    **{"DisplayString": DisplayString,
       "comet": comet,
       "trapTest": trapTest,
       "trapNTPError": trapNTPError,
       "trapEmailErrLogin": trapEmailErrLogin,
       "trapEmailErrAuth": trapEmailErrAuth,
       "trapEmailErrSome": trapEmailErrSome,
       "trapEmailErrSocket": trapEmailErrSocket,
       "trapEmailErrDNS": trapEmailErrDNS,
       "trapSOAPErrFile": trapSOAPErrFile,
       "trapSOAPErrDNS": trapSOAPErrDNS,
       "trapSOAPErrSocket": trapSOAPErrSocket,
       "trapSOAPErrDelivery": trapSOAPErrDelivery,
       "trapCO2Alarm1": trapCO2Alarm1,
       "trapCO2Alarm2": trapCO2Alarm2,
       "trapCO2ClrAlarm1": trapCO2ClrAlarm1,
       "trapCO2ClrAlarm2": trapCO2ClrAlarm2,
       "trapRelay1Closed": trapRelay1Closed,
       "trapRelay2Closed": trapRelay2Closed,
       "trapRelay1Open": trapRelay1Open,
       "trapRelay2Open": trapRelay2Open,
       "trapAcousticActivated": trapAcousticActivated,
       "trapAcousticDeactivated": trapAcousticDeactivated,
       "products": products,
       "h5521": h5521,
       "values": values,
       "co2": co2,
       "re1": re1,
       "re2": re2,
       "co2Alarm1": co2Alarm1,
       "co2Alarm2": co2Alarm2,
       "co2Unit": co2Unit,
       "global": _pysmi_global,
       "sensorName": sensorName,
       "serialNumber": serialNumber,
       "deviceType": deviceType,
       "valuesInt": valuesInt,
       "co2Int": co2Int,
       "re1Int": re1Int,
       "re2Int": re2Int,
       "co2Alarm1Int": co2Alarm1Int,
       "co2Alarm2Int": co2Alarm2Int,
       "settings": settings,
       "co2Lim1Int": co2Lim1Int,
       "co2Lim2Int": co2Lim2Int,
       "co2Hyst1Int": co2Hyst1Int,
       "co2Hyst2Int": co2Hyst2Int,
       "co2Delay1Int": co2Delay1Int,
       "co2Delay2Int": co2Delay2Int,
       "co2Type1Int": co2Type1Int,
       "co2Type2Int": co2Type2Int,
       "traps": traps,
       "messageString": messageString,
       "tables": tables,
       "historyTable": historyTable,
       "historyEntry": historyEntry,
       "histCO2": histCO2}
)
