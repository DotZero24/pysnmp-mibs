# SNMP MIB module (P8510-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/comet/P8510-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:16:20 2025
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
_P8510_ObjectIdentity = ObjectIdentity
p8510 = _P8510_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5)
)
__pysmi_global_ObjectIdentity = ObjectIdentity
_pysmi_global = __pysmi_global_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 1)
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
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 1, 3),
    _DeviceType_Type()
)
deviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceType.setStatus("mandatory")
_Channels_ObjectIdentity = ObjectIdentity
channels = _Channels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2)
)
_Channel1_ObjectIdentity = ObjectIdentity
channel1 = _Channel1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 1)
)


class _Ch1Name_Type(DisplayString):
    """Custom type ch1Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Ch1Name_Type.__name__ = "DisplayString"
_Ch1Name_Object = MibScalar
ch1Name = _Ch1Name_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 1, 1),
    _Ch1Name_Type()
)
ch1Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch1Name.setStatus("mandatory")


class _Ch1Val_Type(DisplayString):
    """Custom type ch1Val based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Ch1Val_Type.__name__ = "DisplayString"
_Ch1Val_Object = MibScalar
ch1Val = _Ch1Val_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 1, 2),
    _Ch1Val_Type()
)
ch1Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch1Val.setStatus("mandatory")


class _Ch1IntVal_Type(Integer32):
    """Custom type ch1IntVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-550, 1250),
    )


_Ch1IntVal_Type.__name__ = "Integer32"
_Ch1IntVal_Object = MibScalar
ch1IntVal = _Ch1IntVal_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 1, 3),
    _Ch1IntVal_Type()
)
ch1IntVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch1IntVal.setStatus("mandatory")


class _Ch1Alarm_Type(Integer32):
    """Custom type ch1Alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Ch1Alarm_Type.__name__ = "Integer32"
_Ch1Alarm_Object = MibScalar
ch1Alarm = _Ch1Alarm_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 1, 4),
    _Ch1Alarm_Type()
)
ch1Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch1Alarm.setStatus("mandatory")


class _Ch1LimHi_Type(Integer32):
    """Custom type ch1LimHi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-550, 1250),
    )


_Ch1LimHi_Type.__name__ = "Integer32"
_Ch1LimHi_Object = MibScalar
ch1LimHi = _Ch1LimHi_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 1, 5),
    _Ch1LimHi_Type()
)
ch1LimHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch1LimHi.setStatus("mandatory")


class _Ch1LimLo_Type(Integer32):
    """Custom type ch1LimLo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-550, 1250),
    )


_Ch1LimLo_Type.__name__ = "Integer32"
_Ch1LimLo_Object = MibScalar
ch1LimLo = _Ch1LimLo_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 1, 6),
    _Ch1LimLo_Type()
)
ch1LimLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch1LimLo.setStatus("mandatory")


class _Ch1LimHyst_Type(Integer32):
    """Custom type ch1LimHyst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-550, 1250),
    )


_Ch1LimHyst_Type.__name__ = "Integer32"
_Ch1LimHyst_Object = MibScalar
ch1LimHyst = _Ch1LimHyst_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 1, 7),
    _Ch1LimHyst_Type()
)
ch1LimHyst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch1LimHyst.setStatus("mandatory")


class _Ch1LimDelay_Type(Integer32):
    """Custom type ch1LimDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_Ch1LimDelay_Type.__name__ = "Integer32"
_Ch1LimDelay_Object = MibScalar
ch1LimDelay = _Ch1LimDelay_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 1, 8),
    _Ch1LimDelay_Type()
)
ch1LimDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch1LimDelay.setStatus("mandatory")


class _Ch1Unit_Type(DisplayString):
    """Custom type ch1Unit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Ch1Unit_Type.__name__ = "DisplayString"
_Ch1Unit_Object = MibScalar
ch1Unit = _Ch1Unit_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 1, 9),
    _Ch1Unit_Type()
)
ch1Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch1Unit.setStatus("mandatory")


class _Ch1AlarmStr_Type(DisplayString):
    """Custom type ch1AlarmStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Ch1AlarmStr_Type.__name__ = "DisplayString"
_Ch1AlarmStr_Object = MibScalar
ch1AlarmStr = _Ch1AlarmStr_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 1, 10),
    _Ch1AlarmStr_Type()
)
ch1AlarmStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch1AlarmStr.setStatus("mandatory")


class _Ch1Min_Type(DisplayString):
    """Custom type ch1Min based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Ch1Min_Type.__name__ = "DisplayString"
_Ch1Min_Object = MibScalar
ch1Min = _Ch1Min_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 1, 11),
    _Ch1Min_Type()
)
ch1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch1Min.setStatus("mandatory")


class _Ch1Max_Type(DisplayString):
    """Custom type ch1Max based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Ch1Max_Type.__name__ = "DisplayString"
_Ch1Max_Object = MibScalar
ch1Max = _Ch1Max_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 1, 12),
    _Ch1Max_Type()
)
ch1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch1Max.setStatus("mandatory")
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 3)
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
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 3, 1),
    _MessageString_Type()
)
messageString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    messageString.setStatus("mandatory")
_Tables_ObjectIdentity = ObjectIdentity
tables = _Tables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 4)
)
_HistoryTable_Object = MibTable
historyTable = _HistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 4, 1)
)
if mibBuilder.loadTexts:
    historyTable.setStatus("mandatory")
_HistoryEntry_Object = MibTableRow
historyEntry = _HistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 4, 1, 1)
)
historyEntry.setIndexNames(
    (0, "P8510-MIB", "ch1value"),
)
if mibBuilder.loadTexts:
    historyEntry.setStatus("optional")


class _Ch1value_Type(Integer32):
    """Custom type ch1value based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-550, 1250),
    )


_Ch1value_Type.__name__ = "Integer32"
_Ch1value_Object = MibTableColumn
ch1value = _Ch1value_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 4, 1, 1, 1),
    _Ch1value_Type()
)
ch1value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch1value.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trapTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 0)
)
trapTest.setObjects(
      *(("P8510-MIB", "sensorName"),
        ("P8510-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapTest.setStatus(
        ""
    )

trapNTPError = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 1)
)
trapNTPError.setObjects(
      *(("P8510-MIB", "sensorName"),
        ("P8510-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapNTPError.setStatus(
        ""
    )

trapEmailErrLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 2)
)
trapEmailErrLogin.setObjects(
      *(("P8510-MIB", "sensorName"),
        ("P8510-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapEmailErrLogin.setStatus(
        ""
    )

trapEmailErrAuth = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 3)
)
trapEmailErrAuth.setObjects(
      *(("P8510-MIB", "sensorName"),
        ("P8510-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapEmailErrAuth.setStatus(
        ""
    )

trapEmailErrSome = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 4)
)
trapEmailErrSome.setObjects(
      *(("P8510-MIB", "sensorName"),
        ("P8510-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapEmailErrSome.setStatus(
        ""
    )

trapEmailErrSocket = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 5)
)
trapEmailErrSocket.setObjects(
      *(("P8510-MIB", "sensorName"),
        ("P8510-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapEmailErrSocket.setStatus(
        ""
    )

trapEmailErrDNS = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 6)
)
trapEmailErrDNS.setObjects(
      *(("P8510-MIB", "sensorName"),
        ("P8510-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapEmailErrDNS.setStatus(
        ""
    )

trapSOAPErrFile = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 7)
)
trapSOAPErrFile.setObjects(
      *(("P8510-MIB", "sensorName"),
        ("P8510-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapSOAPErrFile.setStatus(
        ""
    )

trapSOAPErrDNS = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 8)
)
trapSOAPErrDNS.setObjects(
      *(("P8510-MIB", "sensorName"),
        ("P8510-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapSOAPErrDNS.setStatus(
        ""
    )

trapSOAPErrSocket = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 9)
)
trapSOAPErrSocket.setObjects(
      *(("P8510-MIB", "sensorName"),
        ("P8510-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapSOAPErrSocket.setStatus(
        ""
    )

trapSOAPErrDelivery = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 10)
)
trapSOAPErrDelivery.setObjects(
      *(("P8510-MIB", "sensorName"),
        ("P8510-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapSOAPErrDelivery.setStatus(
        ""
    )

trapCh1HighAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 11)
)
trapCh1HighAlarm.setObjects(
      *(("P8510-MIB", "ch1Name"),
        ("P8510-MIB", "ch1Val"),
        ("P8510-MIB", "ch1Alarm"),
        ("P8510-MIB", "sensorName"),
        ("P8510-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapCh1HighAlarm.setStatus(
        ""
    )

trapCh1LowAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 21)
)
trapCh1LowAlarm.setObjects(
      *(("P8510-MIB", "ch1Name"),
        ("P8510-MIB", "ch1Val"),
        ("P8510-MIB", "ch1Alarm"),
        ("P8510-MIB", "sensorName"),
        ("P8510-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapCh1LowAlarm.setStatus(
        ""
    )

trapCh1ClrAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 31)
)
trapCh1ClrAlarm.setObjects(
      *(("P8510-MIB", "ch1Name"),
        ("P8510-MIB", "ch1Val"),
        ("P8510-MIB", "ch1Alarm"),
        ("P8510-MIB", "sensorName"),
        ("P8510-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapCh1ClrAlarm.setStatus(
        ""
    )

trapCh1Error = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 41)
)
trapCh1Error.setObjects(
      *(("P8510-MIB", "ch1Name"),
        ("P8510-MIB", "ch1Val"),
        ("P8510-MIB", "ch1Alarm"),
        ("P8510-MIB", "sensorName"),
        ("P8510-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapCh1Error.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "P8510-MIB",
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
       "trapCh1HighAlarm": trapCh1HighAlarm,
       "trapCh1LowAlarm": trapCh1LowAlarm,
       "trapCh1ClrAlarm": trapCh1ClrAlarm,
       "trapCh1Error": trapCh1Error,
       "products": products,
       "p8510": p8510,
       "global": _pysmi_global,
       "sensorName": sensorName,
       "serialNumber": serialNumber,
       "deviceType": deviceType,
       "channels": channels,
       "channel1": channel1,
       "ch1Name": ch1Name,
       "ch1Val": ch1Val,
       "ch1IntVal": ch1IntVal,
       "ch1Alarm": ch1Alarm,
       "ch1LimHi": ch1LimHi,
       "ch1LimLo": ch1LimLo,
       "ch1LimHyst": ch1LimHyst,
       "ch1LimDelay": ch1LimDelay,
       "ch1Unit": ch1Unit,
       "ch1AlarmStr": ch1AlarmStr,
       "ch1Min": ch1Min,
       "ch1Max": ch1Max,
       "traps": traps,
       "messageString": messageString,
       "tables": tables,
       "historyTable": historyTable,
       "historyEntry": historyEntry,
       "ch1value": ch1value}
)
