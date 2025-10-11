# SNMP MIB module (T2514-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/comet/T2514-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:16:14 2025
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
_T2514_ObjectIdentity = ObjectIdentity
t2514 = _T2514_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2)
)
_Values_ObjectIdentity = ObjectIdentity
values = _Values_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1)
)


class _Press_Type(DisplayString):
    """Custom type press based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Press_Type.__name__ = "DisplayString"
_Press_Object = MibScalar
press = _Press_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 4),
    _Press_Type()
)
press.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    press.setStatus("mandatory")


class _PressAlarm_Type(DisplayString):
    """Custom type pressAlarm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_PressAlarm_Type.__name__ = "DisplayString"
_PressAlarm_Object = MibScalar
pressAlarm = _PressAlarm_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 8),
    _PressAlarm_Type()
)
pressAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pressAlarm.setStatus("mandatory")


class _PressUnit_Type(DisplayString):
    """Custom type pressUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_PressUnit_Type.__name__ = "DisplayString"
_PressUnit_Object = MibScalar
pressUnit = _PressUnit_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 12),
    _PressUnit_Type()
)
pressUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pressUnit.setStatus("mandatory")


class _PressMin_Type(DisplayString):
    """Custom type pressMin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_PressMin_Type.__name__ = "DisplayString"
_PressMin_Object = MibScalar
pressMin = _PressMin_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 16),
    _PressMin_Type()
)
pressMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pressMin.setStatus("mandatory")


class _PressMax_Type(DisplayString):
    """Custom type pressMax based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_PressMax_Type.__name__ = "DisplayString"
_PressMax_Object = MibScalar
pressMax = _PressMax_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 20),
    _PressMax_Type()
)
pressMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pressMax.setStatus("mandatory")
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


class _PressInt_Type(Integer32):
    """Custom type pressInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5000, 20000),
    )


_PressInt_Type.__name__ = "Integer32"
_PressInt_Object = MibScalar
pressInt = _PressInt_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 4),
    _PressInt_Type()
)
pressInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pressInt.setStatus("mandatory")


class _PressAlarmInt_Type(Integer32):
    """Custom type pressAlarmInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_PressAlarmInt_Type.__name__ = "Integer32"
_PressAlarmInt_Object = MibScalar
pressAlarmInt = _PressAlarmInt_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 8),
    _PressAlarmInt_Type()
)
pressAlarmInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pressAlarmInt.setStatus("mandatory")
_Settings_ObjectIdentity = ObjectIdentity
settings = _Settings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4)
)


class _PressLowInt_Type(Integer32):
    """Custom type pressLowInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5000, 20000),
    )


_PressLowInt_Type.__name__ = "Integer32"
_PressLowInt_Object = MibScalar
pressLowInt = _PressLowInt_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 13),
    _PressLowInt_Type()
)
pressLowInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pressLowInt.setStatus("mandatory")


class _PressHighInt_Type(Integer32):
    """Custom type pressHighInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5000, 20000),
    )


_PressHighInt_Type.__name__ = "Integer32"
_PressHighInt_Object = MibScalar
pressHighInt = _PressHighInt_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 14),
    _PressHighInt_Type()
)
pressHighInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pressHighInt.setStatus("mandatory")


class _PressDelayInt_Type(Integer32):
    """Custom type pressDelayInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4500),
    )


_PressDelayInt_Type.__name__ = "Integer32"
_PressDelayInt_Object = MibScalar
pressDelayInt = _PressDelayInt_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 15),
    _PressDelayInt_Type()
)
pressDelayInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pressDelayInt.setStatus("mandatory")


class _PressHystInt_Type(Integer32):
    """Custom type pressHystInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_PressHystInt_Type.__name__ = "Integer32"
_PressHystInt_Object = MibScalar
pressHystInt = _PressHystInt_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 16),
    _PressHystInt_Type()
)
pressHystInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pressHystInt.setStatus("mandatory")
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
    (0, "T2514-MIB", "histPress"),
)
if mibBuilder.loadTexts:
    historyEntry.setStatus("optional")


class _HistPress_Type(Integer32):
    """Custom type histPress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5000, 20000),
    )


_HistPress_Type.__name__ = "Integer32"
_HistPress_Object = MibTableColumn
histPress = _HistPress_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1, 1, 4),
    _HistPress_Type()
)
histPress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histPress.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trapTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 0)
)
trapTest.setObjects(
      *(("T2514-MIB", "sensorName"),
        ("T2514-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapTest.setStatus(
        ""
    )

trapNTPError = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 1)
)
trapNTPError.setObjects(
      *(("T2514-MIB", "sensorName"),
        ("T2514-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapNTPError.setStatus(
        ""
    )

trapEmailErrLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 2)
)
trapEmailErrLogin.setObjects(
      *(("T2514-MIB", "sensorName"),
        ("T2514-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapEmailErrLogin.setStatus(
        ""
    )

trapEmailErrAuth = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 3)
)
trapEmailErrAuth.setObjects(
      *(("T2514-MIB", "sensorName"),
        ("T2514-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapEmailErrAuth.setStatus(
        ""
    )

trapEmailErrSome = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 4)
)
trapEmailErrSome.setObjects(
      *(("T2514-MIB", "sensorName"),
        ("T2514-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapEmailErrSome.setStatus(
        ""
    )

trapEmailErrSocket = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 5)
)
trapEmailErrSocket.setObjects(
      *(("T2514-MIB", "sensorName"),
        ("T2514-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapEmailErrSocket.setStatus(
        ""
    )

trapEmailErrDNS = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 6)
)
trapEmailErrDNS.setObjects(
      *(("T2514-MIB", "sensorName"),
        ("T2514-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapEmailErrDNS.setStatus(
        ""
    )

trapSOAPErrFile = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 7)
)
trapSOAPErrFile.setObjects(
      *(("T2514-MIB", "sensorName"),
        ("T2514-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapSOAPErrFile.setStatus(
        ""
    )

trapSOAPErrDNS = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 8)
)
trapSOAPErrDNS.setObjects(
      *(("T2514-MIB", "sensorName"),
        ("T2514-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapSOAPErrDNS.setStatus(
        ""
    )

trapSOAPErrSocket = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 9)
)
trapSOAPErrSocket.setObjects(
      *(("T2514-MIB", "sensorName"),
        ("T2514-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapSOAPErrSocket.setStatus(
        ""
    )

trapSOAPErrDelivery = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 10)
)
trapSOAPErrDelivery.setObjects(
      *(("T2514-MIB", "sensorName"),
        ("T2514-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapSOAPErrDelivery.setStatus(
        ""
    )

trapPressHighAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 14)
)
trapPressHighAlarm.setObjects(
      *(("T2514-MIB", "sensorName"),
        ("T2514-MIB", "messageString"),
        ("T2514-MIB", "press"),
        ("T2514-MIB", "pressAlarmInt"))
)
if mibBuilder.loadTexts:
    trapPressHighAlarm.setStatus(
        ""
    )

trapPressLowAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 24)
)
trapPressLowAlarm.setObjects(
      *(("T2514-MIB", "sensorName"),
        ("T2514-MIB", "messageString"),
        ("T2514-MIB", "press"),
        ("T2514-MIB", "pressAlarmInt"))
)
if mibBuilder.loadTexts:
    trapPressLowAlarm.setStatus(
        ""
    )

trapPressClrAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 34)
)
trapPressClrAlarm.setObjects(
      *(("T2514-MIB", "sensorName"),
        ("T2514-MIB", "messageString"),
        ("T2514-MIB", "press"),
        ("T2514-MIB", "pressAlarmInt"))
)
if mibBuilder.loadTexts:
    trapPressClrAlarm.setStatus(
        ""
    )

trapPressError = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 44)
)
trapPressError.setObjects(
      *(("T2514-MIB", "sensorName"),
        ("T2514-MIB", "messageString"),
        ("T2514-MIB", "press"),
        ("T2514-MIB", "pressAlarmInt"))
)
if mibBuilder.loadTexts:
    trapPressError.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "T2514-MIB",
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
       "trapPressHighAlarm": trapPressHighAlarm,
       "trapPressLowAlarm": trapPressLowAlarm,
       "trapPressClrAlarm": trapPressClrAlarm,
       "trapPressError": trapPressError,
       "products": products,
       "t2514": t2514,
       "values": values,
       "press": press,
       "pressAlarm": pressAlarm,
       "pressUnit": pressUnit,
       "pressMin": pressMin,
       "pressMax": pressMax,
       "global": _pysmi_global,
       "sensorName": sensorName,
       "serialNumber": serialNumber,
       "deviceType": deviceType,
       "valuesInt": valuesInt,
       "pressInt": pressInt,
       "pressAlarmInt": pressAlarmInt,
       "settings": settings,
       "pressLowInt": pressLowInt,
       "pressHighInt": pressHighInt,
       "pressDelayInt": pressDelayInt,
       "pressHystInt": pressHystInt,
       "traps": traps,
       "messageString": messageString,
       "tables": tables,
       "historyTable": historyTable,
       "historyEntry": historyEntry,
       "histPress": histPress}
)
