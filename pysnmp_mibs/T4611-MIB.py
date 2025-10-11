# SNMP MIB module (T4611-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/comet/T4611-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:16:12 2025
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
_T4611_ObjectIdentity = ObjectIdentity
t4611 = _T4611_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2)
)
_Values_ObjectIdentity = ObjectIdentity
values = _Values_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1)
)


class _Temp_Type(DisplayString):
    """Custom type temp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Temp_Type.__name__ = "DisplayString"
_Temp_Object = MibScalar
temp = _Temp_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 1),
    _Temp_Type()
)
temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temp.setStatus("mandatory")


class _TempAlarm_Type(DisplayString):
    """Custom type tempAlarm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TempAlarm_Type.__name__ = "DisplayString"
_TempAlarm_Object = MibScalar
tempAlarm = _TempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 5),
    _TempAlarm_Type()
)
tempAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempAlarm.setStatus("mandatory")


class _TempUnit_Type(DisplayString):
    """Custom type tempUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TempUnit_Type.__name__ = "DisplayString"
_TempUnit_Object = MibScalar
tempUnit = _TempUnit_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 9),
    _TempUnit_Type()
)
tempUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempUnit.setStatus("mandatory")


class _TempMin_Type(DisplayString):
    """Custom type tempMin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TempMin_Type.__name__ = "DisplayString"
_TempMin_Object = MibScalar
tempMin = _TempMin_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 13),
    _TempMin_Type()
)
tempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempMin.setStatus("mandatory")


class _TempMax_Type(DisplayString):
    """Custom type tempMax based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TempMax_Type.__name__ = "DisplayString"
_TempMax_Object = MibScalar
tempMax = _TempMax_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 17),
    _TempMax_Type()
)
tempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempMax.setStatus("mandatory")
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


class _TempInt_Type(Integer32):
    """Custom type tempInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5000, 20000),
    )


_TempInt_Type.__name__ = "Integer32"
_TempInt_Object = MibScalar
tempInt = _TempInt_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 1),
    _TempInt_Type()
)
tempInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempInt.setStatus("mandatory")


class _TempAlarmInt_Type(Integer32):
    """Custom type tempAlarmInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_TempAlarmInt_Type.__name__ = "Integer32"
_TempAlarmInt_Object = MibScalar
tempAlarmInt = _TempAlarmInt_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 5),
    _TempAlarmInt_Type()
)
tempAlarmInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempAlarmInt.setStatus("mandatory")
_Settings_ObjectIdentity = ObjectIdentity
settings = _Settings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4)
)


class _TempLowInt_Type(Integer32):
    """Custom type tempLowInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5000, 20000),
    )


_TempLowInt_Type.__name__ = "Integer32"
_TempLowInt_Object = MibScalar
tempLowInt = _TempLowInt_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 1),
    _TempLowInt_Type()
)
tempLowInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempLowInt.setStatus("mandatory")


class _TempHighInt_Type(Integer32):
    """Custom type tempHighInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5000, 20000),
    )


_TempHighInt_Type.__name__ = "Integer32"
_TempHighInt_Object = MibScalar
tempHighInt = _TempHighInt_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 2),
    _TempHighInt_Type()
)
tempHighInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempHighInt.setStatus("mandatory")


class _TempDelayInt_Type(Integer32):
    """Custom type tempDelayInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4500),
    )


_TempDelayInt_Type.__name__ = "Integer32"
_TempDelayInt_Object = MibScalar
tempDelayInt = _TempDelayInt_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 7),
    _TempDelayInt_Type()
)
tempDelayInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempDelayInt.setStatus("mandatory")


class _TempHystInt_Type(Integer32):
    """Custom type tempHystInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_TempHystInt_Type.__name__ = "Integer32"
_TempHystInt_Object = MibScalar
tempHystInt = _TempHystInt_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 10),
    _TempHystInt_Type()
)
tempHystInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempHystInt.setStatus("mandatory")
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
    (0, "T4611-MIB", "histTemp"),
)
if mibBuilder.loadTexts:
    historyEntry.setStatus("optional")


class _HistTemp_Type(Integer32):
    """Custom type histTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5000, 20000),
    )


_HistTemp_Type.__name__ = "Integer32"
_HistTemp_Object = MibTableColumn
histTemp = _HistTemp_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1, 1, 1),
    _HistTemp_Type()
)
histTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histTemp.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trapTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 0)
)
trapTest.setObjects(
      *(("T4611-MIB", "sensorName"),
        ("T4611-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapTest.setStatus(
        ""
    )

trapNTPError = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 1)
)
trapNTPError.setObjects(
      *(("T4611-MIB", "sensorName"),
        ("T4611-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapNTPError.setStatus(
        ""
    )

trapEmailErrLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 2)
)
trapEmailErrLogin.setObjects(
      *(("T4611-MIB", "sensorName"),
        ("T4611-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapEmailErrLogin.setStatus(
        ""
    )

trapEmailErrAuth = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 3)
)
trapEmailErrAuth.setObjects(
      *(("T4611-MIB", "sensorName"),
        ("T4611-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapEmailErrAuth.setStatus(
        ""
    )

trapEmailErrSome = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 4)
)
trapEmailErrSome.setObjects(
      *(("T4611-MIB", "sensorName"),
        ("T4611-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapEmailErrSome.setStatus(
        ""
    )

trapEmailErrSocket = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 5)
)
trapEmailErrSocket.setObjects(
      *(("T4611-MIB", "sensorName"),
        ("T4611-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapEmailErrSocket.setStatus(
        ""
    )

trapEmailErrDNS = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 6)
)
trapEmailErrDNS.setObjects(
      *(("T4611-MIB", "sensorName"),
        ("T4611-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapEmailErrDNS.setStatus(
        ""
    )

trapSOAPErrFile = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 7)
)
trapSOAPErrFile.setObjects(
      *(("T4611-MIB", "sensorName"),
        ("T4611-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapSOAPErrFile.setStatus(
        ""
    )

trapSOAPErrDNS = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 8)
)
trapSOAPErrDNS.setObjects(
      *(("T4611-MIB", "sensorName"),
        ("T4611-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapSOAPErrDNS.setStatus(
        ""
    )

trapSOAPErrSocket = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 9)
)
trapSOAPErrSocket.setObjects(
      *(("T4611-MIB", "sensorName"),
        ("T4611-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapSOAPErrSocket.setStatus(
        ""
    )

trapSOAPErrDelivery = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 10)
)
trapSOAPErrDelivery.setObjects(
      *(("T4611-MIB", "sensorName"),
        ("T4611-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapSOAPErrDelivery.setStatus(
        ""
    )

trapTempHighAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 11)
)
trapTempHighAlarm.setObjects(
      *(("T4611-MIB", "sensorName"),
        ("T4611-MIB", "messageString"),
        ("T4611-MIB", "temp"),
        ("T4611-MIB", "tempAlarmInt"))
)
if mibBuilder.loadTexts:
    trapTempHighAlarm.setStatus(
        ""
    )

trapTempLowAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 21)
)
trapTempLowAlarm.setObjects(
      *(("T4611-MIB", "sensorName"),
        ("T4611-MIB", "messageString"),
        ("T4611-MIB", "temp"),
        ("T4611-MIB", "tempAlarmInt"))
)
if mibBuilder.loadTexts:
    trapTempLowAlarm.setStatus(
        ""
    )

trapTempClrAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 31)
)
trapTempClrAlarm.setObjects(
      *(("T4611-MIB", "sensorName"),
        ("T4611-MIB", "messageString"),
        ("T4611-MIB", "temp"),
        ("T4611-MIB", "tempAlarmInt"))
)
if mibBuilder.loadTexts:
    trapTempClrAlarm.setStatus(
        ""
    )

trapTempError = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 41)
)
trapTempError.setObjects(
      *(("T4611-MIB", "sensorName"),
        ("T4611-MIB", "messageString"),
        ("T4611-MIB", "temp"),
        ("T4611-MIB", "tempAlarmInt"))
)
if mibBuilder.loadTexts:
    trapTempError.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "T4611-MIB",
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
       "trapTempHighAlarm": trapTempHighAlarm,
       "trapTempLowAlarm": trapTempLowAlarm,
       "trapTempClrAlarm": trapTempClrAlarm,
       "trapTempError": trapTempError,
       "products": products,
       "t4611": t4611,
       "values": values,
       "temp": temp,
       "tempAlarm": tempAlarm,
       "tempUnit": tempUnit,
       "tempMin": tempMin,
       "tempMax": tempMax,
       "global": _pysmi_global,
       "sensorName": sensorName,
       "serialNumber": serialNumber,
       "deviceType": deviceType,
       "valuesInt": valuesInt,
       "tempInt": tempInt,
       "tempAlarmInt": tempAlarmInt,
       "settings": settings,
       "tempLowInt": tempLowInt,
       "tempHighInt": tempHighInt,
       "tempDelayInt": tempDelayInt,
       "tempHystInt": tempHystInt,
       "traps": traps,
       "messageString": messageString,
       "tables": tables,
       "historyTable": historyTable,
       "historyEntry": historyEntry,
       "histTemp": histTemp}
)
