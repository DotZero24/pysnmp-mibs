# SNMP MIB module (H4531-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/comet/H4531-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:16:18 2025
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
_H4531_ObjectIdentity = ObjectIdentity
h4531 = _H4531_ObjectIdentity(
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


class _Bin1_Type(DisplayString):
    """Custom type bin1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Bin1_Type.__name__ = "DisplayString"
_Bin1_Object = MibScalar
bin1 = _Bin1_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 5),
    _Bin1_Type()
)
bin1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bin1.setStatus("mandatory")


class _Bin2_Type(DisplayString):
    """Custom type bin2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Bin2_Type.__name__ = "DisplayString"
_Bin2_Object = MibScalar
bin2 = _Bin2_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 6),
    _Bin2_Type()
)
bin2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bin2.setStatus("mandatory")


class _Bin3_Type(DisplayString):
    """Custom type bin3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Bin3_Type.__name__ = "DisplayString"
_Bin3_Object = MibScalar
bin3 = _Bin3_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 7),
    _Bin3_Type()
)
bin3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bin3.setStatus("mandatory")


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


class _TempAlarm1_Type(DisplayString):
    """Custom type tempAlarm1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TempAlarm1_Type.__name__ = "DisplayString"
_TempAlarm1_Object = MibScalar
tempAlarm1 = _TempAlarm1_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 10),
    _TempAlarm1_Type()
)
tempAlarm1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempAlarm1.setStatus("mandatory")


class _TempAlarm2_Type(DisplayString):
    """Custom type tempAlarm2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TempAlarm2_Type.__name__ = "DisplayString"
_TempAlarm2_Object = MibScalar
tempAlarm2 = _TempAlarm2_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 14),
    _TempAlarm2_Type()
)
tempAlarm2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempAlarm2.setStatus("mandatory")


class _Bin1Alarm_Type(DisplayString):
    """Custom type bin1Alarm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Bin1Alarm_Type.__name__ = "DisplayString"
_Bin1Alarm_Object = MibScalar
bin1Alarm = _Bin1Alarm_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 18),
    _Bin1Alarm_Type()
)
bin1Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bin1Alarm.setStatus("mandatory")


class _Bin2Alarm_Type(DisplayString):
    """Custom type bin2Alarm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Bin2Alarm_Type.__name__ = "DisplayString"
_Bin2Alarm_Object = MibScalar
bin2Alarm = _Bin2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 19),
    _Bin2Alarm_Type()
)
bin2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bin2Alarm.setStatus("mandatory")


class _Bin3Alarm_Type(DisplayString):
    """Custom type bin3Alarm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Bin3Alarm_Type.__name__ = "DisplayString"
_Bin3Alarm_Object = MibScalar
bin3Alarm = _Bin3Alarm_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 20),
    _Bin3Alarm_Type()
)
bin3Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bin3Alarm.setStatus("mandatory")


class _TempUnit_Type(DisplayString):
    """Custom type tempUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TempUnit_Type.__name__ = "DisplayString"
_TempUnit_Object = MibScalar
tempUnit = _TempUnit_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 21),
    _TempUnit_Type()
)
tempUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempUnit.setStatus("mandatory")
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


class _Bin1Int_Type(Integer32):
    """Custom type bin1Int based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Bin1Int_Type.__name__ = "Integer32"
_Bin1Int_Object = MibScalar
bin1Int = _Bin1Int_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 5),
    _Bin1Int_Type()
)
bin1Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bin1Int.setStatus("mandatory")


class _Bin2Int_Type(Integer32):
    """Custom type bin2Int based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Bin2Int_Type.__name__ = "Integer32"
_Bin2Int_Object = MibScalar
bin2Int = _Bin2Int_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 6),
    _Bin2Int_Type()
)
bin2Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bin2Int.setStatus("mandatory")


class _Bin3Int_Type(Integer32):
    """Custom type bin3Int based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Bin3Int_Type.__name__ = "Integer32"
_Bin3Int_Object = MibScalar
bin3Int = _Bin3Int_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 7),
    _Bin3Int_Type()
)
bin3Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bin3Int.setStatus("mandatory")


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


class _TempAlarm1Int_Type(Integer32):
    """Custom type tempAlarm1Int based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TempAlarm1Int_Type.__name__ = "Integer32"
_TempAlarm1Int_Object = MibScalar
tempAlarm1Int = _TempAlarm1Int_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 10),
    _TempAlarm1Int_Type()
)
tempAlarm1Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempAlarm1Int.setStatus("mandatory")


class _TempAlarm2Int_Type(Integer32):
    """Custom type tempAlarm2Int based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TempAlarm2Int_Type.__name__ = "Integer32"
_TempAlarm2Int_Object = MibScalar
tempAlarm2Int = _TempAlarm2Int_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 14),
    _TempAlarm2Int_Type()
)
tempAlarm2Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempAlarm2Int.setStatus("mandatory")


class _Bin1AlarmInt_Type(Integer32):
    """Custom type bin1AlarmInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Bin1AlarmInt_Type.__name__ = "Integer32"
_Bin1AlarmInt_Object = MibScalar
bin1AlarmInt = _Bin1AlarmInt_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 18),
    _Bin1AlarmInt_Type()
)
bin1AlarmInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bin1AlarmInt.setStatus("mandatory")


class _Bin2AlarmInt_Type(Integer32):
    """Custom type bin2AlarmInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Bin2AlarmInt_Type.__name__ = "Integer32"
_Bin2AlarmInt_Object = MibScalar
bin2AlarmInt = _Bin2AlarmInt_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 19),
    _Bin2AlarmInt_Type()
)
bin2AlarmInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bin2AlarmInt.setStatus("mandatory")


class _Bin3AlarmInt_Type(Integer32):
    """Custom type bin3AlarmInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Bin3AlarmInt_Type.__name__ = "Integer32"
_Bin3AlarmInt_Object = MibScalar
bin3AlarmInt = _Bin3AlarmInt_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 20),
    _Bin3AlarmInt_Type()
)
bin3AlarmInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bin3AlarmInt.setStatus("mandatory")
_Settings_ObjectIdentity = ObjectIdentity
settings = _Settings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4)
)


class _TempLim1Int_Type(Integer32):
    """Custom type tempLim1Int based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5000, 20000),
    )


_TempLim1Int_Type.__name__ = "Integer32"
_TempLim1Int_Object = MibScalar
tempLim1Int = _TempLim1Int_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 1),
    _TempLim1Int_Type()
)
tempLim1Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempLim1Int.setStatus("mandatory")


class _TempLim2Int_Type(Integer32):
    """Custom type tempLim2Int based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5000, 20000),
    )


_TempLim2Int_Type.__name__ = "Integer32"
_TempLim2Int_Object = MibScalar
tempLim2Int = _TempLim2Int_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 5),
    _TempLim2Int_Type()
)
tempLim2Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempLim2Int.setStatus("mandatory")


class _TempHyst1Int_Type(Integer32):
    """Custom type tempHyst1Int based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_TempHyst1Int_Type.__name__ = "Integer32"
_TempHyst1Int_Object = MibScalar
tempHyst1Int = _TempHyst1Int_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 9),
    _TempHyst1Int_Type()
)
tempHyst1Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempHyst1Int.setStatus("mandatory")


class _TempHyst2Int_Type(Integer32):
    """Custom type tempHyst2Int based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_TempHyst2Int_Type.__name__ = "Integer32"
_TempHyst2Int_Object = MibScalar
tempHyst2Int = _TempHyst2Int_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 13),
    _TempHyst2Int_Type()
)
tempHyst2Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempHyst2Int.setStatus("mandatory")


class _TempDelay1Int_Type(Integer32):
    """Custom type tempDelay1Int based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_TempDelay1Int_Type.__name__ = "Integer32"
_TempDelay1Int_Object = MibScalar
tempDelay1Int = _TempDelay1Int_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 17),
    _TempDelay1Int_Type()
)
tempDelay1Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempDelay1Int.setStatus("mandatory")


class _TempDelay2Int_Type(Integer32):
    """Custom type tempDelay2Int based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_TempDelay2Int_Type.__name__ = "Integer32"
_TempDelay2Int_Object = MibScalar
tempDelay2Int = _TempDelay2Int_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 21),
    _TempDelay2Int_Type()
)
tempDelay2Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempDelay2Int.setStatus("mandatory")


class _TempType1Int_Type(Integer32):
    """Custom type tempType1Int based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_TempType1Int_Type.__name__ = "Integer32"
_TempType1Int_Object = MibScalar
tempType1Int = _TempType1Int_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 25),
    _TempType1Int_Type()
)
tempType1Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempType1Int.setStatus("mandatory")


class _TempType2Int_Type(Integer32):
    """Custom type tempType2Int based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_TempType2Int_Type.__name__ = "Integer32"
_TempType2Int_Object = MibScalar
tempType2Int = _TempType2Int_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 29),
    _TempType2Int_Type()
)
tempType2Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempType2Int.setStatus("mandatory")


class _Bin1DelayInt_Type(Integer32):
    """Custom type bin1DelayInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_Bin1DelayInt_Type.__name__ = "Integer32"
_Bin1DelayInt_Object = MibScalar
bin1DelayInt = _Bin1DelayInt_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 33),
    _Bin1DelayInt_Type()
)
bin1DelayInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bin1DelayInt.setStatus("mandatory")


class _Bin2DelayInt_Type(Integer32):
    """Custom type bin2DelayInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_Bin2DelayInt_Type.__name__ = "Integer32"
_Bin2DelayInt_Object = MibScalar
bin2DelayInt = _Bin2DelayInt_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 34),
    _Bin2DelayInt_Type()
)
bin2DelayInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bin2DelayInt.setStatus("mandatory")


class _Bin3DelayInt_Type(Integer32):
    """Custom type bin3DelayInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_Bin3DelayInt_Type.__name__ = "Integer32"
_Bin3DelayInt_Object = MibScalar
bin3DelayInt = _Bin3DelayInt_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 35),
    _Bin3DelayInt_Type()
)
bin3DelayInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bin3DelayInt.setStatus("mandatory")


class _Bin1TypeInt_Type(Integer32):
    """Custom type bin1TypeInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Bin1TypeInt_Type.__name__ = "Integer32"
_Bin1TypeInt_Object = MibScalar
bin1TypeInt = _Bin1TypeInt_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 36),
    _Bin1TypeInt_Type()
)
bin1TypeInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bin1TypeInt.setStatus("mandatory")


class _Bin2TypeInt_Type(Integer32):
    """Custom type bin2TypeInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Bin2TypeInt_Type.__name__ = "Integer32"
_Bin2TypeInt_Object = MibScalar
bin2TypeInt = _Bin2TypeInt_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 37),
    _Bin2TypeInt_Type()
)
bin2TypeInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bin2TypeInt.setStatus("mandatory")


class _Bin3TypeInt_Type(Integer32):
    """Custom type bin3TypeInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Bin3TypeInt_Type.__name__ = "Integer32"
_Bin3TypeInt_Object = MibScalar
bin3TypeInt = _Bin3TypeInt_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 38),
    _Bin3TypeInt_Type()
)
bin3TypeInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bin3TypeInt.setStatus("mandatory")
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
    (0, "H4531-MIB", "histTemp"),
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
      *(("H4531-MIB", "sensorName"),
        ("H4531-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapTest.setStatus(
        ""
    )

trapNTPError = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 1)
)
trapNTPError.setObjects(
      *(("H4531-MIB", "sensorName"),
        ("H4531-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapNTPError.setStatus(
        ""
    )

trapEmailErrLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 2)
)
trapEmailErrLogin.setObjects(
      *(("H4531-MIB", "sensorName"),
        ("H4531-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapEmailErrLogin.setStatus(
        ""
    )

trapEmailErrAuth = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 3)
)
trapEmailErrAuth.setObjects(
      *(("H4531-MIB", "sensorName"),
        ("H4531-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapEmailErrAuth.setStatus(
        ""
    )

trapEmailErrSome = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 4)
)
trapEmailErrSome.setObjects(
      *(("H4531-MIB", "sensorName"),
        ("H4531-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapEmailErrSome.setStatus(
        ""
    )

trapEmailErrSocket = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 5)
)
trapEmailErrSocket.setObjects(
      *(("H4531-MIB", "sensorName"),
        ("H4531-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapEmailErrSocket.setStatus(
        ""
    )

trapEmailErrDNS = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 6)
)
trapEmailErrDNS.setObjects(
      *(("H4531-MIB", "sensorName"),
        ("H4531-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapEmailErrDNS.setStatus(
        ""
    )

trapSOAPErrFile = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 7)
)
trapSOAPErrFile.setObjects(
      *(("H4531-MIB", "sensorName"),
        ("H4531-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapSOAPErrFile.setStatus(
        ""
    )

trapSOAPErrDNS = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 8)
)
trapSOAPErrDNS.setObjects(
      *(("H4531-MIB", "sensorName"),
        ("H4531-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapSOAPErrDNS.setStatus(
        ""
    )

trapSOAPErrSocket = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 9)
)
trapSOAPErrSocket.setObjects(
      *(("H4531-MIB", "sensorName"),
        ("H4531-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapSOAPErrSocket.setStatus(
        ""
    )

trapSOAPErrDelivery = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 10)
)
trapSOAPErrDelivery.setObjects(
      *(("H4531-MIB", "sensorName"),
        ("H4531-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapSOAPErrDelivery.setStatus(
        ""
    )

trapTempAlarm1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 11)
)
trapTempAlarm1.setObjects(
      *(("H4531-MIB", "sensorName"),
        ("H4531-MIB", "messageString"),
        ("H4531-MIB", "temp"),
        ("H4531-MIB", "tempAlarm1Int"))
)
if mibBuilder.loadTexts:
    trapTempAlarm1.setStatus(
        ""
    )

trapTempAlarm2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 21)
)
trapTempAlarm2.setObjects(
      *(("H4531-MIB", "sensorName"),
        ("H4531-MIB", "messageString"),
        ("H4531-MIB", "temp"),
        ("H4531-MIB", "tempAlarm2Int"))
)
if mibBuilder.loadTexts:
    trapTempAlarm2.setStatus(
        ""
    )

trapTempClrAlarm1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 31)
)
trapTempClrAlarm1.setObjects(
      *(("H4531-MIB", "sensorName"),
        ("H4531-MIB", "messageString"),
        ("H4531-MIB", "temp"),
        ("H4531-MIB", "tempAlarm1Int"))
)
if mibBuilder.loadTexts:
    trapTempClrAlarm1.setStatus(
        ""
    )

trapTempClrAlarm2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 41)
)
trapTempClrAlarm2.setObjects(
      *(("H4531-MIB", "sensorName"),
        ("H4531-MIB", "messageString"),
        ("H4531-MIB", "temp"),
        ("H4531-MIB", "tempAlarm2Int"))
)
if mibBuilder.loadTexts:
    trapTempClrAlarm2.setStatus(
        ""
    )

trapBin1Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 51)
)
trapBin1Alarm.setObjects(
      *(("H4531-MIB", "sensorName"),
        ("H4531-MIB", "messageString"),
        ("H4531-MIB", "bin1Int"),
        ("H4531-MIB", "bin1AlarmInt"))
)
if mibBuilder.loadTexts:
    trapBin1Alarm.setStatus(
        ""
    )

trapBin2Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 52)
)
trapBin2Alarm.setObjects(
      *(("H4531-MIB", "sensorName"),
        ("H4531-MIB", "messageString"),
        ("H4531-MIB", "bin2Int"),
        ("H4531-MIB", "bin2AlarmInt"))
)
if mibBuilder.loadTexts:
    trapBin2Alarm.setStatus(
        ""
    )

trapBin3Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 53)
)
trapBin3Alarm.setObjects(
      *(("H4531-MIB", "sensorName"),
        ("H4531-MIB", "messageString"),
        ("H4531-MIB", "bin3Int"),
        ("H4531-MIB", "bin3AlarmInt"))
)
if mibBuilder.loadTexts:
    trapBin3Alarm.setStatus(
        ""
    )

trapBin1ClrAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 61)
)
trapBin1ClrAlarm.setObjects(
      *(("H4531-MIB", "sensorName"),
        ("H4531-MIB", "messageString"),
        ("H4531-MIB", "bin1Int"),
        ("H4531-MIB", "bin1AlarmInt"))
)
if mibBuilder.loadTexts:
    trapBin1ClrAlarm.setStatus(
        ""
    )

trapBin2ClrAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 62)
)
trapBin2ClrAlarm.setObjects(
      *(("H4531-MIB", "sensorName"),
        ("H4531-MIB", "messageString"),
        ("H4531-MIB", "bin2Int"),
        ("H4531-MIB", "bin2AlarmInt"))
)
if mibBuilder.loadTexts:
    trapBin2ClrAlarm.setStatus(
        ""
    )

trapBin3ClrAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 63)
)
trapBin3ClrAlarm.setObjects(
      *(("H4531-MIB", "sensorName"),
        ("H4531-MIB", "messageString"),
        ("H4531-MIB", "bin3Int"),
        ("H4531-MIB", "bin3AlarmInt"))
)
if mibBuilder.loadTexts:
    trapBin3ClrAlarm.setStatus(
        ""
    )

trapRelay1Closed = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 70)
)
trapRelay1Closed.setObjects(
      *(("H4531-MIB", "sensorName"),
        ("H4531-MIB", "messageString"),
        ("H4531-MIB", "re1Int"))
)
if mibBuilder.loadTexts:
    trapRelay1Closed.setStatus(
        ""
    )

trapRelay2Closed = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 71)
)
trapRelay2Closed.setObjects(
      *(("H4531-MIB", "sensorName"),
        ("H4531-MIB", "messageString"),
        ("H4531-MIB", "re2Int"))
)
if mibBuilder.loadTexts:
    trapRelay2Closed.setStatus(
        ""
    )

trapRelay1Open = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 72)
)
trapRelay1Open.setObjects(
      *(("H4531-MIB", "sensorName"),
        ("H4531-MIB", "messageString"),
        ("H4531-MIB", "re1Int"))
)
if mibBuilder.loadTexts:
    trapRelay1Open.setStatus(
        ""
    )

trapRelay2Open = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 73)
)
trapRelay2Open.setObjects(
      *(("H4531-MIB", "sensorName"),
        ("H4531-MIB", "messageString"),
        ("H4531-MIB", "re2Int"))
)
if mibBuilder.loadTexts:
    trapRelay2Open.setStatus(
        ""
    )

trapAcousticActivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 74)
)
trapAcousticActivated.setObjects(
      *(("H4531-MIB", "sensorName"),
        ("H4531-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapAcousticActivated.setStatus(
        ""
    )

trapAcousticDeactivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 75)
)
trapAcousticDeactivated.setObjects(
      *(("H4531-MIB", "sensorName"),
        ("H4531-MIB", "messageString"))
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
    "H4531-MIB",
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
       "trapTempAlarm1": trapTempAlarm1,
       "trapTempAlarm2": trapTempAlarm2,
       "trapTempClrAlarm1": trapTempClrAlarm1,
       "trapTempClrAlarm2": trapTempClrAlarm2,
       "trapBin1Alarm": trapBin1Alarm,
       "trapBin2Alarm": trapBin2Alarm,
       "trapBin3Alarm": trapBin3Alarm,
       "trapBin1ClrAlarm": trapBin1ClrAlarm,
       "trapBin2ClrAlarm": trapBin2ClrAlarm,
       "trapBin3ClrAlarm": trapBin3ClrAlarm,
       "trapRelay1Closed": trapRelay1Closed,
       "trapRelay2Closed": trapRelay2Closed,
       "trapRelay1Open": trapRelay1Open,
       "trapRelay2Open": trapRelay2Open,
       "trapAcousticActivated": trapAcousticActivated,
       "trapAcousticDeactivated": trapAcousticDeactivated,
       "products": products,
       "h4531": h4531,
       "values": values,
       "temp": temp,
       "bin1": bin1,
       "bin2": bin2,
       "bin3": bin3,
       "re1": re1,
       "re2": re2,
       "tempAlarm1": tempAlarm1,
       "tempAlarm2": tempAlarm2,
       "bin1Alarm": bin1Alarm,
       "bin2Alarm": bin2Alarm,
       "bin3Alarm": bin3Alarm,
       "tempUnit": tempUnit,
       "global": _pysmi_global,
       "sensorName": sensorName,
       "serialNumber": serialNumber,
       "deviceType": deviceType,
       "valuesInt": valuesInt,
       "tempInt": tempInt,
       "bin1Int": bin1Int,
       "bin2Int": bin2Int,
       "bin3Int": bin3Int,
       "re1Int": re1Int,
       "re2Int": re2Int,
       "tempAlarm1Int": tempAlarm1Int,
       "tempAlarm2Int": tempAlarm2Int,
       "bin1AlarmInt": bin1AlarmInt,
       "bin2AlarmInt": bin2AlarmInt,
       "bin3AlarmInt": bin3AlarmInt,
       "settings": settings,
       "tempLim1Int": tempLim1Int,
       "tempLim2Int": tempLim2Int,
       "tempHyst1Int": tempHyst1Int,
       "tempHyst2Int": tempHyst2Int,
       "tempDelay1Int": tempDelay1Int,
       "tempDelay2Int": tempDelay2Int,
       "tempType1Int": tempType1Int,
       "tempType2Int": tempType2Int,
       "bin1DelayInt": bin1DelayInt,
       "bin2DelayInt": bin2DelayInt,
       "bin3DelayInt": bin3DelayInt,
       "bin1TypeInt": bin1TypeInt,
       "bin2TypeInt": bin2TypeInt,
       "bin3TypeInt": bin3TypeInt,
       "traps": traps,
       "messageString": messageString,
       "tables": tables,
       "historyTable": historyTable,
       "historyEntry": historyEntry,
       "histTemp": histTemp}
)
