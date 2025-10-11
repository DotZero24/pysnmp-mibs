# SNMP MIB module (WebGraph-AnalogIO-57762-US-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/webgraph/WebGraph-AnalogIO-57762-US-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:17:09 2025
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Wut_ObjectIdentity = ObjectIdentity
wut = _Wut_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040)
)
_WtComServer_ObjectIdentity = ObjectIdentity
wtComServer = _WtComServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1)
)
_WtWebio_ObjectIdentity = ObjectIdentity
wtWebio = _WtWebio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2)
)
_WtWebGraphAnalog57762_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57762 = _WtWebGraphAnalog57762_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29)
)
_WtWebGraphAnalog57762Inventory_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57762Inventory = _WtWebGraphAnalog57762Inventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 1)
)


class _WtWebGraphAnalog57762Sensors_Type(Integer32):
    """Custom type wtWebGraphAnalog57762Sensors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WtWebGraphAnalog57762Sensors_Type.__name__ = "Integer32"
_WtWebGraphAnalog57762Sensors_Object = MibScalar
wtWebGraphAnalog57762Sensors = _WtWebGraphAnalog57762Sensors_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 1, 1),
    _WtWebGraphAnalog57762Sensors_Type()
)
wtWebGraphAnalog57762Sensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762Sensors.setStatus("mandatory")
_WtWebGraphAnalog57762SensorTable_Object = MibTable
wtWebGraphAnalog57762SensorTable = _WtWebGraphAnalog57762SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 1, 2)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762SensorTable.setStatus("mandatory")
_WtWebGraphAnalog57762SensorEntry_Object = MibTableRow
wtWebGraphAnalog57762SensorEntry = _WtWebGraphAnalog57762SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 1, 2, 1)
)
wtWebGraphAnalog57762SensorEntry.setIndexNames(
    (0, "WebGraph-AnalogIO-57762-US-MIB", "wtWebGraphAnalog57762SensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762SensorEntry.setStatus("mandatory")


class _WtWebGraphAnalog57762SensorNo_Type(Integer32):
    """Custom type wtWebGraphAnalog57762SensorNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WtWebGraphAnalog57762SensorNo_Type.__name__ = "Integer32"
_WtWebGraphAnalog57762SensorNo_Object = MibTableColumn
wtWebGraphAnalog57762SensorNo = _WtWebGraphAnalog57762SensorNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 1, 2, 1, 1),
    _WtWebGraphAnalog57762SensorNo_Type()
)
wtWebGraphAnalog57762SensorNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762SensorNo.setStatus("mandatory")
_WtWebGraphAnalog57762ValuesTable_Object = MibTable
wtWebGraphAnalog57762ValuesTable = _WtWebGraphAnalog57762ValuesTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 1, 3)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762ValuesTable.setStatus("mandatory")
_WtWebGraphAnalog57762ValuesEntry_Object = MibTableRow
wtWebGraphAnalog57762ValuesEntry = _WtWebGraphAnalog57762ValuesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 1, 3, 1)
)
wtWebGraphAnalog57762ValuesEntry.setIndexNames(
    (0, "WebGraph-AnalogIO-57762-US-MIB", "wtWebGraphAnalog57762SensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762ValuesEntry.setStatus("mandatory")


class _WtWebGraphAnalog57762Values_Type(OctetString):
    """Custom type wtWebGraphAnalog57762Values based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_WtWebGraphAnalog57762Values_Type.__name__ = "OctetString"
_WtWebGraphAnalog57762Values_Object = MibTableColumn
wtWebGraphAnalog57762Values = _WtWebGraphAnalog57762Values_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 1, 3, 1, 1),
    _WtWebGraphAnalog57762Values_Type()
)
wtWebGraphAnalog57762Values.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762Values.setStatus("mandatory")
_WtWebGraphAnalog57762BinaryValuesTable_Object = MibTable
wtWebGraphAnalog57762BinaryValuesTable = _WtWebGraphAnalog57762BinaryValuesTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 1, 4)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762BinaryValuesTable.setStatus("mandatory")
_WtWebGraphAnalog57762BinaryValuesEntry_Object = MibTableRow
wtWebGraphAnalog57762BinaryValuesEntry = _WtWebGraphAnalog57762BinaryValuesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 1, 4, 1)
)
wtWebGraphAnalog57762BinaryValuesEntry.setIndexNames(
    (0, "WebGraph-AnalogIO-57762-US-MIB", "wtWebGraphAnalog57762SensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762BinaryValuesEntry.setStatus("mandatory")
_WtWebGraphAnalog57762BinaryValues_Type = Integer32
_WtWebGraphAnalog57762BinaryValues_Object = MibTableColumn
wtWebGraphAnalog57762BinaryValues = _WtWebGraphAnalog57762BinaryValues_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 1, 4, 1, 1),
    _WtWebGraphAnalog57762BinaryValues_Type()
)
wtWebGraphAnalog57762BinaryValues.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762BinaryValues.setStatus("mandatory")
_WtWebGraphAnalog57762ValuesPointTable_Object = MibTable
wtWebGraphAnalog57762ValuesPointTable = _WtWebGraphAnalog57762ValuesPointTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 1, 8)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762ValuesPointTable.setStatus("mandatory")
_WtWebGraphAnalog57762ValuesPointEntry_Object = MibTableRow
wtWebGraphAnalog57762ValuesPointEntry = _WtWebGraphAnalog57762ValuesPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 1, 8, 1)
)
wtWebGraphAnalog57762ValuesPointEntry.setIndexNames(
    (0, "WebGraph-AnalogIO-57762-US-MIB", "wtWebGraphAnalog57762SensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762ValuesPointEntry.setStatus("mandatory")


class _WtWebGraphAnalog57762ValuesPoint_Type(OctetString):
    """Custom type wtWebGraphAnalog57762ValuesPoint based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_WtWebGraphAnalog57762ValuesPoint_Type.__name__ = "OctetString"
_WtWebGraphAnalog57762ValuesPoint_Object = MibTableColumn
wtWebGraphAnalog57762ValuesPoint = _WtWebGraphAnalog57762ValuesPoint_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 1, 8, 1, 1),
    _WtWebGraphAnalog57762ValuesPoint_Type()
)
wtWebGraphAnalog57762ValuesPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762ValuesPoint.setStatus("mandatory")
_WtWebGraphAnalog57762SessCntrl_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57762SessCntrl = _WtWebGraphAnalog57762SessCntrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 2)
)
_WtWebGraphAnalog57762SessCntrlPassword_Type = OctetString
_WtWebGraphAnalog57762SessCntrlPassword_Object = MibScalar
wtWebGraphAnalog57762SessCntrlPassword = _WtWebGraphAnalog57762SessCntrlPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 2, 1),
    _WtWebGraphAnalog57762SessCntrlPassword_Type()
)
wtWebGraphAnalog57762SessCntrlPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762SessCntrlPassword.setStatus("mandatory")


class _WtWebGraphAnalog57762SessCntrlConfigMode_Type(Integer32):
    """Custom type wtWebGraphAnalog57762SessCntrlConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("wtWebGraphAnalog57762SessCntrl-NoSession", 0),
          ("wtWebGraphAnalog57762SessCntrl-Session", 1))
    )


_WtWebGraphAnalog57762SessCntrlConfigMode_Type.__name__ = "Integer32"
_WtWebGraphAnalog57762SessCntrlConfigMode_Object = MibScalar
wtWebGraphAnalog57762SessCntrlConfigMode = _WtWebGraphAnalog57762SessCntrlConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 2, 2),
    _WtWebGraphAnalog57762SessCntrlConfigMode_Type()
)
wtWebGraphAnalog57762SessCntrlConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762SessCntrlConfigMode.setStatus("mandatory")
_WtWebGraphAnalog57762SessCntrlLogout_Type = Integer32
_WtWebGraphAnalog57762SessCntrlLogout_Object = MibScalar
wtWebGraphAnalog57762SessCntrlLogout = _WtWebGraphAnalog57762SessCntrlLogout_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 2, 3),
    _WtWebGraphAnalog57762SessCntrlLogout_Type()
)
wtWebGraphAnalog57762SessCntrlLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762SessCntrlLogout.setStatus("mandatory")
_WtWebGraphAnalog57762SessCntrlAdminPassword_Type = OctetString
_WtWebGraphAnalog57762SessCntrlAdminPassword_Object = MibScalar
wtWebGraphAnalog57762SessCntrlAdminPassword = _WtWebGraphAnalog57762SessCntrlAdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 2, 4),
    _WtWebGraphAnalog57762SessCntrlAdminPassword_Type()
)
wtWebGraphAnalog57762SessCntrlAdminPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762SessCntrlAdminPassword.setStatus("mandatory")
_WtWebGraphAnalog57762SessCntrlConfigPassword_Type = OctetString
_WtWebGraphAnalog57762SessCntrlConfigPassword_Object = MibScalar
wtWebGraphAnalog57762SessCntrlConfigPassword = _WtWebGraphAnalog57762SessCntrlConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 2, 5),
    _WtWebGraphAnalog57762SessCntrlConfigPassword_Type()
)
wtWebGraphAnalog57762SessCntrlConfigPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762SessCntrlConfigPassword.setStatus("mandatory")
_WtWebGraphAnalog57762Config_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57762Config = _WtWebGraphAnalog57762Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3)
)
_WtWebGraphAnalog57762Device_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57762Device = _WtWebGraphAnalog57762Device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1)
)
_WtWebGraphAnalog57762Text_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57762Text = _WtWebGraphAnalog57762Text_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 1)
)
_WtWebGraphAnalog57762DeviceName_Type = OctetString
_WtWebGraphAnalog57762DeviceName_Object = MibScalar
wtWebGraphAnalog57762DeviceName = _WtWebGraphAnalog57762DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 1, 1),
    _WtWebGraphAnalog57762DeviceName_Type()
)
wtWebGraphAnalog57762DeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762DeviceName.setStatus("mandatory")
_WtWebGraphAnalog57762DeviceText_Type = OctetString
_WtWebGraphAnalog57762DeviceText_Object = MibScalar
wtWebGraphAnalog57762DeviceText = _WtWebGraphAnalog57762DeviceText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 1, 2),
    _WtWebGraphAnalog57762DeviceText_Type()
)
wtWebGraphAnalog57762DeviceText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762DeviceText.setStatus("mandatory")
_WtWebGraphAnalog57762DeviceLocation_Type = OctetString
_WtWebGraphAnalog57762DeviceLocation_Object = MibScalar
wtWebGraphAnalog57762DeviceLocation = _WtWebGraphAnalog57762DeviceLocation_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 1, 3),
    _WtWebGraphAnalog57762DeviceLocation_Type()
)
wtWebGraphAnalog57762DeviceLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762DeviceLocation.setStatus("mandatory")
_WtWebGraphAnalog57762DeviceContact_Type = OctetString
_WtWebGraphAnalog57762DeviceContact_Object = MibScalar
wtWebGraphAnalog57762DeviceContact = _WtWebGraphAnalog57762DeviceContact_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 1, 4),
    _WtWebGraphAnalog57762DeviceContact_Type()
)
wtWebGraphAnalog57762DeviceContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762DeviceContact.setStatus("mandatory")
_WtWebGraphAnalog57762TimeDate_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57762TimeDate = _WtWebGraphAnalog57762TimeDate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2)
)
_WtWebGraphAnalog57762TimeZone_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57762TimeZone = _WtWebGraphAnalog57762TimeZone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 1)
)
_WtWebGraphAnalog57762TzOffsetHrs_Type = Integer32
_WtWebGraphAnalog57762TzOffsetHrs_Object = MibScalar
wtWebGraphAnalog57762TzOffsetHrs = _WtWebGraphAnalog57762TzOffsetHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 1, 1),
    _WtWebGraphAnalog57762TzOffsetHrs_Type()
)
wtWebGraphAnalog57762TzOffsetHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762TzOffsetHrs.setStatus("mandatory")
_WtWebGraphAnalog57762TzOffsetMin_Type = Integer32
_WtWebGraphAnalog57762TzOffsetMin_Object = MibScalar
wtWebGraphAnalog57762TzOffsetMin = _WtWebGraphAnalog57762TzOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 1, 2),
    _WtWebGraphAnalog57762TzOffsetMin_Type()
)
wtWebGraphAnalog57762TzOffsetMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762TzOffsetMin.setStatus("mandatory")


class _WtWebGraphAnalog57762TzEnable_Type(OctetString):
    """Custom type wtWebGraphAnalog57762TzEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphAnalog57762TzEnable_Type.__name__ = "OctetString"
_WtWebGraphAnalog57762TzEnable_Object = MibScalar
wtWebGraphAnalog57762TzEnable = _WtWebGraphAnalog57762TzEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 1, 3),
    _WtWebGraphAnalog57762TzEnable_Type()
)
wtWebGraphAnalog57762TzEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762TzEnable.setStatus("mandatory")
_WtWebGraphAnalog57762StTzOffsetHrs_Type = Integer32
_WtWebGraphAnalog57762StTzOffsetHrs_Object = MibScalar
wtWebGraphAnalog57762StTzOffsetHrs = _WtWebGraphAnalog57762StTzOffsetHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 1, 4),
    _WtWebGraphAnalog57762StTzOffsetHrs_Type()
)
wtWebGraphAnalog57762StTzOffsetHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762StTzOffsetHrs.setStatus("mandatory")
_WtWebGraphAnalog57762StTzOffsetMin_Type = Integer32
_WtWebGraphAnalog57762StTzOffsetMin_Object = MibScalar
wtWebGraphAnalog57762StTzOffsetMin = _WtWebGraphAnalog57762StTzOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 1, 5),
    _WtWebGraphAnalog57762StTzOffsetMin_Type()
)
wtWebGraphAnalog57762StTzOffsetMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762StTzOffsetMin.setStatus("mandatory")


class _WtWebGraphAnalog57762StTzEnable_Type(OctetString):
    """Custom type wtWebGraphAnalog57762StTzEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphAnalog57762StTzEnable_Type.__name__ = "OctetString"
_WtWebGraphAnalog57762StTzEnable_Object = MibScalar
wtWebGraphAnalog57762StTzEnable = _WtWebGraphAnalog57762StTzEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 1, 6),
    _WtWebGraphAnalog57762StTzEnable_Type()
)
wtWebGraphAnalog57762StTzEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762StTzEnable.setStatus("mandatory")


class _WtWebGraphAnalog57762StTzStartMonth_Type(Integer32):
    """Custom type wtWebGraphAnalog57762StTzStartMonth based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("wtWebGraphAnalog57762StartMonth-January", 1),
          ("wtWebGraphAnalog57762StartMonth-February", 2),
          ("wtWebGraphAnalog57762StartMonth-March", 3),
          ("wtWebGraphAnalog57762StartMonth-April", 4),
          ("wtWebGraphAnalog57762StartMonth-May", 5),
          ("wtWebGraphAnalog57762StartMonth-June", 6),
          ("wtWebGraphAnalog57762StartMonth-July", 7),
          ("wtWebGraphAnalog57762StartMonth-August", 8),
          ("wtWebGraphAnalog57762StartMonth-September", 9),
          ("wtWebGraphAnalog57762StartMonth-October", 10),
          ("wtWebGraphAnalog57762StartMonth-November", 11),
          ("wtWebGraphAnalog57762StartMonth-December", 12))
    )


_WtWebGraphAnalog57762StTzStartMonth_Type.__name__ = "Integer32"
_WtWebGraphAnalog57762StTzStartMonth_Object = MibScalar
wtWebGraphAnalog57762StTzStartMonth = _WtWebGraphAnalog57762StTzStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 1, 7),
    _WtWebGraphAnalog57762StTzStartMonth_Type()
)
wtWebGraphAnalog57762StTzStartMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762StTzStartMonth.setStatus("mandatory")


class _WtWebGraphAnalog57762StTzStartMode_Type(Integer32):
    """Custom type wtWebGraphAnalog57762StTzStartMode based on Integer32"""
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
        *(("wtWebGraphAnalog57762StartMode-first", 1),
          ("wtWebGraphAnalog57762StartMode-second", 2),
          ("wtWebGraphAnalog57762StartMode-third", 3),
          ("wtWebGraphAnalog57762StartMode-fourth", 4),
          ("wtWebGraphAnalog57762StartMode-last", 5))
    )


_WtWebGraphAnalog57762StTzStartMode_Type.__name__ = "Integer32"
_WtWebGraphAnalog57762StTzStartMode_Object = MibScalar
wtWebGraphAnalog57762StTzStartMode = _WtWebGraphAnalog57762StTzStartMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 1, 8),
    _WtWebGraphAnalog57762StTzStartMode_Type()
)
wtWebGraphAnalog57762StTzStartMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762StTzStartMode.setStatus("mandatory")


class _WtWebGraphAnalog57762StTzStartWday_Type(Integer32):
    """Custom type wtWebGraphAnalog57762StTzStartWday based on Integer32"""
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
        *(("wtWebGraphAnalog57762StartWday-Sunday", 1),
          ("wtWebGraphAnalog57762StartWday-Monday", 2),
          ("wtWebGraphAnalog57762StartWday-Tuesday", 3),
          ("wtWebGraphAnalog57762StartWday-Thursday", 4),
          ("wtWebGraphAnalog57762StartWday-Wednesday", 5),
          ("wtWebGraphAnalog57762StartWday-Friday", 6),
          ("wtWebGraphAnalog57762StartWday-Saturday", 7))
    )


_WtWebGraphAnalog57762StTzStartWday_Type.__name__ = "Integer32"
_WtWebGraphAnalog57762StTzStartWday_Object = MibScalar
wtWebGraphAnalog57762StTzStartWday = _WtWebGraphAnalog57762StTzStartWday_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 1, 9),
    _WtWebGraphAnalog57762StTzStartWday_Type()
)
wtWebGraphAnalog57762StTzStartWday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762StTzStartWday.setStatus("mandatory")
_WtWebGraphAnalog57762StTzStartHrs_Type = Integer32
_WtWebGraphAnalog57762StTzStartHrs_Object = MibScalar
wtWebGraphAnalog57762StTzStartHrs = _WtWebGraphAnalog57762StTzStartHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 1, 10),
    _WtWebGraphAnalog57762StTzStartHrs_Type()
)
wtWebGraphAnalog57762StTzStartHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762StTzStartHrs.setStatus("mandatory")
_WtWebGraphAnalog57762StTzStartMin_Type = Integer32
_WtWebGraphAnalog57762StTzStartMin_Object = MibScalar
wtWebGraphAnalog57762StTzStartMin = _WtWebGraphAnalog57762StTzStartMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 1, 11),
    _WtWebGraphAnalog57762StTzStartMin_Type()
)
wtWebGraphAnalog57762StTzStartMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762StTzStartMin.setStatus("mandatory")


class _WtWebGraphAnalog57762StTzStopMonth_Type(Integer32):
    """Custom type wtWebGraphAnalog57762StTzStopMonth based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("wtWebGraphAnalog57762StopMonth-January", 1),
          ("wtWebGraphAnalog57762StopMonth-February", 2),
          ("wtWebGraphAnalog57762StopMonth-March", 3),
          ("wtWebGraphAnalog57762StopMonth-April", 4),
          ("wtWebGraphAnalog57762StopMonth-May", 5),
          ("wtWebGraphAnalog57762StopMonth-June", 6),
          ("wtWebGraphAnalog57762StopMonth-July", 7),
          ("wtWebGraphAnalog57762StopMonth-August", 8),
          ("wtWebGraphAnalog57762StopMonth-September", 9),
          ("wtWebGraphAnalog57762StopMonth-October", 10),
          ("wtWebGraphAnalog57762StopMonth-November", 11),
          ("wtWebGraphAnalog57762StopMonth-December", 12))
    )


_WtWebGraphAnalog57762StTzStopMonth_Type.__name__ = "Integer32"
_WtWebGraphAnalog57762StTzStopMonth_Object = MibScalar
wtWebGraphAnalog57762StTzStopMonth = _WtWebGraphAnalog57762StTzStopMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 1, 12),
    _WtWebGraphAnalog57762StTzStopMonth_Type()
)
wtWebGraphAnalog57762StTzStopMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762StTzStopMonth.setStatus("mandatory")


class _WtWebGraphAnalog57762StTzStopMode_Type(Integer32):
    """Custom type wtWebGraphAnalog57762StTzStopMode based on Integer32"""
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
        *(("wtWebGraphAnalog57762StopMode-first", 1),
          ("wtWebGraphAnalog57762StopMode-second", 2),
          ("wtWebGraphAnalog57762StopMode-third", 3),
          ("wtWebGraphAnalog57762StopMode-fourth", 4),
          ("wtWebGraphAnalog57762StopMode-last", 5))
    )


_WtWebGraphAnalog57762StTzStopMode_Type.__name__ = "Integer32"
_WtWebGraphAnalog57762StTzStopMode_Object = MibScalar
wtWebGraphAnalog57762StTzStopMode = _WtWebGraphAnalog57762StTzStopMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 1, 13),
    _WtWebGraphAnalog57762StTzStopMode_Type()
)
wtWebGraphAnalog57762StTzStopMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762StTzStopMode.setStatus("mandatory")


class _WtWebGraphAnalog57762StTzStopWday_Type(Integer32):
    """Custom type wtWebGraphAnalog57762StTzStopWday based on Integer32"""
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
        *(("wtWebGraphAnalog57762StopWday-Sunday", 1),
          ("wtWebGraphAnalog57762StopWday-Monday", 2),
          ("wtWebGraphAnalog57762StopWday-Tuesday", 3),
          ("wtWebGraphAnalog57762StopWday-Thursday", 4),
          ("wtWebGraphAnalog57762StopWday-Wednesday", 5),
          ("wtWebGraphAnalog57762StopWday-Friday", 6),
          ("wtWebGraphAnalog57762StopWday-Saturday", 7))
    )


_WtWebGraphAnalog57762StTzStopWday_Type.__name__ = "Integer32"
_WtWebGraphAnalog57762StTzStopWday_Object = MibScalar
wtWebGraphAnalog57762StTzStopWday = _WtWebGraphAnalog57762StTzStopWday_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 1, 14),
    _WtWebGraphAnalog57762StTzStopWday_Type()
)
wtWebGraphAnalog57762StTzStopWday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762StTzStopWday.setStatus("mandatory")
_WtWebGraphAnalog57762StTzStopHrs_Type = Integer32
_WtWebGraphAnalog57762StTzStopHrs_Object = MibScalar
wtWebGraphAnalog57762StTzStopHrs = _WtWebGraphAnalog57762StTzStopHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 1, 15),
    _WtWebGraphAnalog57762StTzStopHrs_Type()
)
wtWebGraphAnalog57762StTzStopHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762StTzStopHrs.setStatus("mandatory")
_WtWebGraphAnalog57762StTzStopMin_Type = Integer32
_WtWebGraphAnalog57762StTzStopMin_Object = MibScalar
wtWebGraphAnalog57762StTzStopMin = _WtWebGraphAnalog57762StTzStopMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 1, 16),
    _WtWebGraphAnalog57762StTzStopMin_Type()
)
wtWebGraphAnalog57762StTzStopMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762StTzStopMin.setStatus("mandatory")
_WtWebGraphAnalog57762TimeServer_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57762TimeServer = _WtWebGraphAnalog57762TimeServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 2)
)
_WtWebGraphAnalog57762TimeServer1_Type = OctetString
_WtWebGraphAnalog57762TimeServer1_Object = MibScalar
wtWebGraphAnalog57762TimeServer1 = _WtWebGraphAnalog57762TimeServer1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 2, 1),
    _WtWebGraphAnalog57762TimeServer1_Type()
)
wtWebGraphAnalog57762TimeServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762TimeServer1.setStatus("mandatory")
_WtWebGraphAnalog57762TimeServer2_Type = OctetString
_WtWebGraphAnalog57762TimeServer2_Object = MibScalar
wtWebGraphAnalog57762TimeServer2 = _WtWebGraphAnalog57762TimeServer2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 2, 2),
    _WtWebGraphAnalog57762TimeServer2_Type()
)
wtWebGraphAnalog57762TimeServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762TimeServer2.setStatus("mandatory")


class _WtWebGraphAnalog57762TsEnable_Type(OctetString):
    """Custom type wtWebGraphAnalog57762TsEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphAnalog57762TsEnable_Type.__name__ = "OctetString"
_WtWebGraphAnalog57762TsEnable_Object = MibScalar
wtWebGraphAnalog57762TsEnable = _WtWebGraphAnalog57762TsEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 2, 3),
    _WtWebGraphAnalog57762TsEnable_Type()
)
wtWebGraphAnalog57762TsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762TsEnable.setStatus("mandatory")
_WtWebGraphAnalog57762TsSyncTime_Type = Integer32
_WtWebGraphAnalog57762TsSyncTime_Object = MibScalar
wtWebGraphAnalog57762TsSyncTime = _WtWebGraphAnalog57762TsSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 2, 4),
    _WtWebGraphAnalog57762TsSyncTime_Type()
)
wtWebGraphAnalog57762TsSyncTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762TsSyncTime.setStatus("mandatory")
_WtWebGraphAnalog57762DeviceClock_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57762DeviceClock = _WtWebGraphAnalog57762DeviceClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 3)
)


class _WtWebGraphAnalog57762ClockHrs_Type(Integer32):
    """Custom type wtWebGraphAnalog57762ClockHrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_WtWebGraphAnalog57762ClockHrs_Type.__name__ = "Integer32"
_WtWebGraphAnalog57762ClockHrs_Object = MibScalar
wtWebGraphAnalog57762ClockHrs = _WtWebGraphAnalog57762ClockHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 3, 1),
    _WtWebGraphAnalog57762ClockHrs_Type()
)
wtWebGraphAnalog57762ClockHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762ClockHrs.setStatus("mandatory")


class _WtWebGraphAnalog57762ClockMin_Type(Integer32):
    """Custom type wtWebGraphAnalog57762ClockMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_WtWebGraphAnalog57762ClockMin_Type.__name__ = "Integer32"
_WtWebGraphAnalog57762ClockMin_Object = MibScalar
wtWebGraphAnalog57762ClockMin = _WtWebGraphAnalog57762ClockMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 3, 2),
    _WtWebGraphAnalog57762ClockMin_Type()
)
wtWebGraphAnalog57762ClockMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762ClockMin.setStatus("mandatory")


class _WtWebGraphAnalog57762ClockDay_Type(Integer32):
    """Custom type wtWebGraphAnalog57762ClockDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_WtWebGraphAnalog57762ClockDay_Type.__name__ = "Integer32"
_WtWebGraphAnalog57762ClockDay_Object = MibScalar
wtWebGraphAnalog57762ClockDay = _WtWebGraphAnalog57762ClockDay_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 3, 3),
    _WtWebGraphAnalog57762ClockDay_Type()
)
wtWebGraphAnalog57762ClockDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762ClockDay.setStatus("mandatory")


class _WtWebGraphAnalog57762ClockMonth_Type(Integer32):
    """Custom type wtWebGraphAnalog57762ClockMonth based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("wtWebGraphAnalog57762ClockMonth-January", 1),
          ("wtWebGraphAnalog57762ClockMonth-February", 2),
          ("wtWebGraphAnalog57762ClockMonth-March", 3),
          ("wtWebGraphAnalog57762ClockMonth-April", 4),
          ("wtWebGraphAnalog57762ClockMonth-May", 5),
          ("wtWebGraphAnalog57762ClockMonth-June", 6),
          ("wtWebGraphAnalog57762ClockMonth-July", 7),
          ("wtWebGraphAnalog57762ClockMonth-August", 8),
          ("wtWebGraphAnalog57762ClockMonth-September", 9),
          ("wtWebGraphAnalog57762ClockMonth-October", 10),
          ("wtWebGraphAnalog57762ClockMonth-November", 11),
          ("wtWebGraphAnalog57762ClockMonth-December", 12))
    )


_WtWebGraphAnalog57762ClockMonth_Type.__name__ = "Integer32"
_WtWebGraphAnalog57762ClockMonth_Object = MibScalar
wtWebGraphAnalog57762ClockMonth = _WtWebGraphAnalog57762ClockMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 3, 4),
    _WtWebGraphAnalog57762ClockMonth_Type()
)
wtWebGraphAnalog57762ClockMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762ClockMonth.setStatus("mandatory")


class _WtWebGraphAnalog57762ClockYear_Type(Integer32):
    """Custom type wtWebGraphAnalog57762ClockYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtWebGraphAnalog57762ClockYear_Type.__name__ = "Integer32"
_WtWebGraphAnalog57762ClockYear_Object = MibScalar
wtWebGraphAnalog57762ClockYear = _WtWebGraphAnalog57762ClockYear_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 3, 5),
    _WtWebGraphAnalog57762ClockYear_Type()
)
wtWebGraphAnalog57762ClockYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762ClockYear.setStatus("mandatory")
_WtWebGraphAnalog57762Basic_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57762Basic = _WtWebGraphAnalog57762Basic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3)
)
_WtWebGraphAnalog57762Network_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57762Network = _WtWebGraphAnalog57762Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 1)
)
_WtWebGraphAnalog57762IpAddress_Type = IpAddress
_WtWebGraphAnalog57762IpAddress_Object = MibScalar
wtWebGraphAnalog57762IpAddress = _WtWebGraphAnalog57762IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 1, 1),
    _WtWebGraphAnalog57762IpAddress_Type()
)
wtWebGraphAnalog57762IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762IpAddress.setStatus("mandatory")
_WtWebGraphAnalog57762SubnetMask_Type = IpAddress
_WtWebGraphAnalog57762SubnetMask_Object = MibScalar
wtWebGraphAnalog57762SubnetMask = _WtWebGraphAnalog57762SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 1, 2),
    _WtWebGraphAnalog57762SubnetMask_Type()
)
wtWebGraphAnalog57762SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762SubnetMask.setStatus("mandatory")
_WtWebGraphAnalog57762Gateway_Type = IpAddress
_WtWebGraphAnalog57762Gateway_Object = MibScalar
wtWebGraphAnalog57762Gateway = _WtWebGraphAnalog57762Gateway_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 1, 3),
    _WtWebGraphAnalog57762Gateway_Type()
)
wtWebGraphAnalog57762Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762Gateway.setStatus("mandatory")
_WtWebGraphAnalog57762DnsServer1_Type = OctetString
_WtWebGraphAnalog57762DnsServer1_Object = MibScalar
wtWebGraphAnalog57762DnsServer1 = _WtWebGraphAnalog57762DnsServer1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 1, 4),
    _WtWebGraphAnalog57762DnsServer1_Type()
)
wtWebGraphAnalog57762DnsServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762DnsServer1.setStatus("mandatory")
_WtWebGraphAnalog57762DnsServer2_Type = OctetString
_WtWebGraphAnalog57762DnsServer2_Object = MibScalar
wtWebGraphAnalog57762DnsServer2 = _WtWebGraphAnalog57762DnsServer2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 1, 5),
    _WtWebGraphAnalog57762DnsServer2_Type()
)
wtWebGraphAnalog57762DnsServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762DnsServer2.setStatus("mandatory")
_WtWebGraphAnalog57762AddConfig_Type = OctetString
_WtWebGraphAnalog57762AddConfig_Object = MibScalar
wtWebGraphAnalog57762AddConfig = _WtWebGraphAnalog57762AddConfig_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 1, 6),
    _WtWebGraphAnalog57762AddConfig_Type()
)
wtWebGraphAnalog57762AddConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AddConfig.setStatus("mandatory")
_WtWebGraphAnalog57762HTTP_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57762HTTP = _WtWebGraphAnalog57762HTTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 2)
)
_WtWebGraphAnalog57762Startup_Type = OctetString
_WtWebGraphAnalog57762Startup_Object = MibScalar
wtWebGraphAnalog57762Startup = _WtWebGraphAnalog57762Startup_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 2, 1),
    _WtWebGraphAnalog57762Startup_Type()
)
wtWebGraphAnalog57762Startup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762Startup.setStatus("mandatory")
_WtWebGraphAnalog57762GetHeaderEnable_Type = OctetString
_WtWebGraphAnalog57762GetHeaderEnable_Object = MibScalar
wtWebGraphAnalog57762GetHeaderEnable = _WtWebGraphAnalog57762GetHeaderEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 2, 2),
    _WtWebGraphAnalog57762GetHeaderEnable_Type()
)
wtWebGraphAnalog57762GetHeaderEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762GetHeaderEnable.setStatus("mandatory")


class _WtWebGraphAnalog57762HttpPort_Type(Integer32):
    """Custom type wtWebGraphAnalog57762HttpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalog57762HttpPort_Type.__name__ = "Integer32"
_WtWebGraphAnalog57762HttpPort_Object = MibScalar
wtWebGraphAnalog57762HttpPort = _WtWebGraphAnalog57762HttpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 2, 3),
    _WtWebGraphAnalog57762HttpPort_Type()
)
wtWebGraphAnalog57762HttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762HttpPort.setStatus("mandatory")
_WtWebGraphAnalog57762Mail_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57762Mail = _WtWebGraphAnalog57762Mail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 3)
)
_WtWebGraphAnalog57762MailAdName_Type = OctetString
_WtWebGraphAnalog57762MailAdName_Object = MibScalar
wtWebGraphAnalog57762MailAdName = _WtWebGraphAnalog57762MailAdName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 3, 1),
    _WtWebGraphAnalog57762MailAdName_Type()
)
wtWebGraphAnalog57762MailAdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762MailAdName.setStatus("mandatory")
_WtWebGraphAnalog57762MailReply_Type = OctetString
_WtWebGraphAnalog57762MailReply_Object = MibScalar
wtWebGraphAnalog57762MailReply = _WtWebGraphAnalog57762MailReply_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 3, 2),
    _WtWebGraphAnalog57762MailReply_Type()
)
wtWebGraphAnalog57762MailReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762MailReply.setStatus("mandatory")
_WtWebGraphAnalog57762MailServer_Type = OctetString
_WtWebGraphAnalog57762MailServer_Object = MibScalar
wtWebGraphAnalog57762MailServer = _WtWebGraphAnalog57762MailServer_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 3, 3),
    _WtWebGraphAnalog57762MailServer_Type()
)
wtWebGraphAnalog57762MailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762MailServer.setStatus("mandatory")
_WtWebioAn1MailEnable_Type = OctetString
_WtWebioAn1MailEnable_Object = MibScalar
wtWebioAn1MailEnable = _WtWebioAn1MailEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 3, 4),
    _WtWebioAn1MailEnable_Type()
)
wtWebioAn1MailEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1MailEnable.setStatus("mandatory")


class _WtWebGraphAnalog57762MailAuthentication_Type(OctetString):
    """Custom type wtWebGraphAnalog57762MailAuthentication based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphAnalog57762MailAuthentication_Type.__name__ = "OctetString"
_WtWebGraphAnalog57762MailAuthentication_Object = MibScalar
wtWebGraphAnalog57762MailAuthentication = _WtWebGraphAnalog57762MailAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 3, 5),
    _WtWebGraphAnalog57762MailAuthentication_Type()
)
wtWebGraphAnalog57762MailAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762MailAuthentication.setStatus("mandatory")
_WtWebGraphAnalog57762MailAuthUser_Type = OctetString
_WtWebGraphAnalog57762MailAuthUser_Object = MibScalar
wtWebGraphAnalog57762MailAuthUser = _WtWebGraphAnalog57762MailAuthUser_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 3, 6),
    _WtWebGraphAnalog57762MailAuthUser_Type()
)
wtWebGraphAnalog57762MailAuthUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762MailAuthUser.setStatus("mandatory")
_WtWebGraphAnalog57762MailAuthPassword_Type = OctetString
_WtWebGraphAnalog57762MailAuthPassword_Object = MibScalar
wtWebGraphAnalog57762MailAuthPassword = _WtWebGraphAnalog57762MailAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 3, 7),
    _WtWebGraphAnalog57762MailAuthPassword_Type()
)
wtWebGraphAnalog57762MailAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762MailAuthPassword.setStatus("mandatory")
_WtWebGraphAnalog57762MailPop3Server_Type = OctetString
_WtWebGraphAnalog57762MailPop3Server_Object = MibScalar
wtWebGraphAnalog57762MailPop3Server = _WtWebGraphAnalog57762MailPop3Server_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 3, 8),
    _WtWebGraphAnalog57762MailPop3Server_Type()
)
wtWebGraphAnalog57762MailPop3Server.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762MailPop3Server.setStatus("mandatory")
_WtWebGraphAnalog57762SNMP_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57762SNMP = _WtWebGraphAnalog57762SNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 4)
)
_WtWebGraphAnalog57762SnmpCommunityStringRead_Type = OctetString
_WtWebGraphAnalog57762SnmpCommunityStringRead_Object = MibScalar
wtWebGraphAnalog57762SnmpCommunityStringRead = _WtWebGraphAnalog57762SnmpCommunityStringRead_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 4, 1),
    _WtWebGraphAnalog57762SnmpCommunityStringRead_Type()
)
wtWebGraphAnalog57762SnmpCommunityStringRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762SnmpCommunityStringRead.setStatus("mandatory")
_WtWebGraphAnalog57762SnmpCommunityStringReadWrite_Type = OctetString
_WtWebGraphAnalog57762SnmpCommunityStringReadWrite_Object = MibScalar
wtWebGraphAnalog57762SnmpCommunityStringReadWrite = _WtWebGraphAnalog57762SnmpCommunityStringReadWrite_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 4, 2),
    _WtWebGraphAnalog57762SnmpCommunityStringReadWrite_Type()
)
wtWebGraphAnalog57762SnmpCommunityStringReadWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762SnmpCommunityStringReadWrite.setStatus("mandatory")
_WtWebGraphAnalog57762SystemTrapManagerIP_Type = OctetString
_WtWebGraphAnalog57762SystemTrapManagerIP_Object = MibScalar
wtWebGraphAnalog57762SystemTrapManagerIP = _WtWebGraphAnalog57762SystemTrapManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 4, 3),
    _WtWebGraphAnalog57762SystemTrapManagerIP_Type()
)
wtWebGraphAnalog57762SystemTrapManagerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762SystemTrapManagerIP.setStatus("mandatory")


class _WtWebGraphAnalog57762SystemTrapEnable_Type(OctetString):
    """Custom type wtWebGraphAnalog57762SystemTrapEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphAnalog57762SystemTrapEnable_Type.__name__ = "OctetString"
_WtWebGraphAnalog57762SystemTrapEnable_Object = MibScalar
wtWebGraphAnalog57762SystemTrapEnable = _WtWebGraphAnalog57762SystemTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 4, 4),
    _WtWebGraphAnalog57762SystemTrapEnable_Type()
)
wtWebGraphAnalog57762SystemTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762SystemTrapEnable.setStatus("mandatory")
_WtWebGraphAnalog57762SnmpEnable_Type = OctetString
_WtWebGraphAnalog57762SnmpEnable_Object = MibScalar
wtWebGraphAnalog57762SnmpEnable = _WtWebGraphAnalog57762SnmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 4, 5),
    _WtWebGraphAnalog57762SnmpEnable_Type()
)
wtWebGraphAnalog57762SnmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762SnmpEnable.setStatus("mandatory")
_WtWebGraphAnalog57762SnmpCommunityStringTrap_Type = OctetString
_WtWebGraphAnalog57762SnmpCommunityStringTrap_Object = MibScalar
wtWebGraphAnalog57762SnmpCommunityStringTrap = _WtWebGraphAnalog57762SnmpCommunityStringTrap_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 4, 6),
    _WtWebGraphAnalog57762SnmpCommunityStringTrap_Type()
)
wtWebGraphAnalog57762SnmpCommunityStringTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762SnmpCommunityStringTrap.setStatus("mandatory")
_WtWebGraphAnalog57762SnmpSystemTrapManagerPort_Type = Integer32
_WtWebGraphAnalog57762SnmpSystemTrapManagerPort_Object = MibScalar
wtWebGraphAnalog57762SnmpSystemTrapManagerPort = _WtWebGraphAnalog57762SnmpSystemTrapManagerPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 4, 7),
    _WtWebGraphAnalog57762SnmpSystemTrapManagerPort_Type()
)
wtWebGraphAnalog57762SnmpSystemTrapManagerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762SnmpSystemTrapManagerPort.setStatus("mandatory")
_WtWebGraphAnalog57762UDP_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57762UDP = _WtWebGraphAnalog57762UDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 5)
)


class _WtWebGraphAnalog57762UdpPort_Type(Integer32):
    """Custom type wtWebGraphAnalog57762UdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalog57762UdpPort_Type.__name__ = "Integer32"
_WtWebGraphAnalog57762UdpPort_Object = MibScalar
wtWebGraphAnalog57762UdpPort = _WtWebGraphAnalog57762UdpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 5, 1),
    _WtWebGraphAnalog57762UdpPort_Type()
)
wtWebGraphAnalog57762UdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762UdpPort.setStatus("mandatory")
_WtWebGraphAnalog57762UdpEnable_Type = OctetString
_WtWebGraphAnalog57762UdpEnable_Object = MibScalar
wtWebGraphAnalog57762UdpEnable = _WtWebGraphAnalog57762UdpEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 5, 2),
    _WtWebGraphAnalog57762UdpEnable_Type()
)
wtWebGraphAnalog57762UdpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762UdpEnable.setStatus("mandatory")
_WtWebGraphAnalog57762Syslog_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57762Syslog = _WtWebGraphAnalog57762Syslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 6)
)
_WtWebGraphAnalog57762SyslogServerIP_Type = OctetString
_WtWebGraphAnalog57762SyslogServerIP_Object = MibScalar
wtWebGraphAnalog57762SyslogServerIP = _WtWebGraphAnalog57762SyslogServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 6, 1),
    _WtWebGraphAnalog57762SyslogServerIP_Type()
)
wtWebGraphAnalog57762SyslogServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762SyslogServerIP.setStatus("mandatory")
_WtWebGraphAnalog57762SyslogServerPort_Type = Integer32
_WtWebGraphAnalog57762SyslogServerPort_Object = MibScalar
wtWebGraphAnalog57762SyslogServerPort = _WtWebGraphAnalog57762SyslogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 6, 2),
    _WtWebGraphAnalog57762SyslogServerPort_Type()
)
wtWebGraphAnalog57762SyslogServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762SyslogServerPort.setStatus("mandatory")


class _WtWebGraphAnalog57762SyslogSystemMessagesEnable_Type(OctetString):
    """Custom type wtWebGraphAnalog57762SyslogSystemMessagesEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphAnalog57762SyslogSystemMessagesEnable_Type.__name__ = "OctetString"
_WtWebGraphAnalog57762SyslogSystemMessagesEnable_Object = MibScalar
wtWebGraphAnalog57762SyslogSystemMessagesEnable = _WtWebGraphAnalog57762SyslogSystemMessagesEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 6, 3),
    _WtWebGraphAnalog57762SyslogSystemMessagesEnable_Type()
)
wtWebGraphAnalog57762SyslogSystemMessagesEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762SyslogSystemMessagesEnable.setStatus("mandatory")
_WtWebGraphAnalog57762SyslogEnable_Type = OctetString
_WtWebGraphAnalog57762SyslogEnable_Object = MibScalar
wtWebGraphAnalog57762SyslogEnable = _WtWebGraphAnalog57762SyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 6, 4),
    _WtWebGraphAnalog57762SyslogEnable_Type()
)
wtWebGraphAnalog57762SyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762SyslogEnable.setStatus("mandatory")
_WtWebGraphAnalog57762FTP_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57762FTP = _WtWebGraphAnalog57762FTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 7)
)
_WtWebGraphAnalog57762FTPServerIP_Type = OctetString
_WtWebGraphAnalog57762FTPServerIP_Object = MibScalar
wtWebGraphAnalog57762FTPServerIP = _WtWebGraphAnalog57762FTPServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 7, 1),
    _WtWebGraphAnalog57762FTPServerIP_Type()
)
wtWebGraphAnalog57762FTPServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762FTPServerIP.setStatus("mandatory")
_WtWebGraphAnalog57762FTPServerControlPort_Type = Integer32
_WtWebGraphAnalog57762FTPServerControlPort_Object = MibScalar
wtWebGraphAnalog57762FTPServerControlPort = _WtWebGraphAnalog57762FTPServerControlPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 7, 2),
    _WtWebGraphAnalog57762FTPServerControlPort_Type()
)
wtWebGraphAnalog57762FTPServerControlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762FTPServerControlPort.setStatus("mandatory")
_WtWebGraphAnalog57762FTPUserName_Type = OctetString
_WtWebGraphAnalog57762FTPUserName_Object = MibScalar
wtWebGraphAnalog57762FTPUserName = _WtWebGraphAnalog57762FTPUserName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 7, 3),
    _WtWebGraphAnalog57762FTPUserName_Type()
)
wtWebGraphAnalog57762FTPUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762FTPUserName.setStatus("mandatory")
_WtWebGraphAnalog57762FTPPassword_Type = OctetString
_WtWebGraphAnalog57762FTPPassword_Object = MibScalar
wtWebGraphAnalog57762FTPPassword = _WtWebGraphAnalog57762FTPPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 7, 4),
    _WtWebGraphAnalog57762FTPPassword_Type()
)
wtWebGraphAnalog57762FTPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762FTPPassword.setStatus("mandatory")
_WtWebGraphAnalog57762FTPAccount_Type = OctetString
_WtWebGraphAnalog57762FTPAccount_Object = MibScalar
wtWebGraphAnalog57762FTPAccount = _WtWebGraphAnalog57762FTPAccount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 7, 5),
    _WtWebGraphAnalog57762FTPAccount_Type()
)
wtWebGraphAnalog57762FTPAccount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762FTPAccount.setStatus("mandatory")
_WtWebGraphAnalog57762FTPOption_Type = OctetString
_WtWebGraphAnalog57762FTPOption_Object = MibScalar
wtWebGraphAnalog57762FTPOption = _WtWebGraphAnalog57762FTPOption_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 7, 6),
    _WtWebGraphAnalog57762FTPOption_Type()
)
wtWebGraphAnalog57762FTPOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762FTPOption.setStatus("mandatory")
_WtWebGraphAnalog57762FTPEnable_Type = OctetString
_WtWebGraphAnalog57762FTPEnable_Object = MibScalar
wtWebGraphAnalog57762FTPEnable = _WtWebGraphAnalog57762FTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 7, 7),
    _WtWebGraphAnalog57762FTPEnable_Type()
)
wtWebGraphAnalog57762FTPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762FTPEnable.setStatus("mandatory")
_WtWebGraphAnalog57762Language_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57762Language = _WtWebGraphAnalog57762Language_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 8)
)
_WtWebGraphAnalog57762LanguageSelect_Type = OctetString
_WtWebGraphAnalog57762LanguageSelect_Object = MibScalar
wtWebGraphAnalog57762LanguageSelect = _WtWebGraphAnalog57762LanguageSelect_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 8, 1),
    _WtWebGraphAnalog57762LanguageSelect_Type()
)
wtWebGraphAnalog57762LanguageSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762LanguageSelect.setStatus("mandatory")
_WtWebGraphAnalog57762Binary_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57762Binary = _WtWebGraphAnalog57762Binary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9)
)


class _WtWebGraphAnalog57762BinaryModeCount_Type(Integer32):
    """Custom type wtWebGraphAnalog57762BinaryModeCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WtWebGraphAnalog57762BinaryModeCount_Type.__name__ = "Integer32"
_WtWebGraphAnalog57762BinaryModeCount_Object = MibScalar
wtWebGraphAnalog57762BinaryModeCount = _WtWebGraphAnalog57762BinaryModeCount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 1),
    _WtWebGraphAnalog57762BinaryModeCount_Type()
)
wtWebGraphAnalog57762BinaryModeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762BinaryModeCount.setStatus("mandatory")
_WtWebGraphAnalog57762BinaryIfTable_Object = MibTable
wtWebGraphAnalog57762BinaryIfTable = _WtWebGraphAnalog57762BinaryIfTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 2)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762BinaryIfTable.setStatus("mandatory")
_WtWebGraphAnalog57762BinaryIfEntry_Object = MibTableRow
wtWebGraphAnalog57762BinaryIfEntry = _WtWebGraphAnalog57762BinaryIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 2, 1)
)
wtWebGraphAnalog57762BinaryIfEntry.setIndexNames(
    (0, "WebGraph-AnalogIO-57762-US-MIB", "wtWebGraphAnalog57762BinaryModeNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762BinaryIfEntry.setStatus("mandatory")


class _WtWebGraphAnalog57762BinaryModeNo_Type(Integer32):
    """Custom type wtWebGraphAnalog57762BinaryModeNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WtWebGraphAnalog57762BinaryModeNo_Type.__name__ = "Integer32"
_WtWebGraphAnalog57762BinaryModeNo_Object = MibTableColumn
wtWebGraphAnalog57762BinaryModeNo = _WtWebGraphAnalog57762BinaryModeNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 2, 1, 1),
    _WtWebGraphAnalog57762BinaryModeNo_Type()
)
wtWebGraphAnalog57762BinaryModeNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762BinaryModeNo.setStatus("mandatory")
_WtWebGraphAnalog57762BinaryTable_Object = MibTable
wtWebGraphAnalog57762BinaryTable = _WtWebGraphAnalog57762BinaryTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762BinaryTable.setStatus("mandatory")
_WtWebGraphAnalog57762BinaryEntry_Object = MibTableRow
wtWebGraphAnalog57762BinaryEntry = _WtWebGraphAnalog57762BinaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1)
)
wtWebGraphAnalog57762BinaryEntry.setIndexNames(
    (0, "WebGraph-AnalogIO-57762-US-MIB", "wtWebGraphAnalog57762BinaryModeNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762BinaryEntry.setStatus("mandatory")


class _WtWebGraphAnalog57762BinaryOperationMode_Type(OctetString):
    """Custom type wtWebGraphAnalog57762BinaryOperationMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphAnalog57762BinaryOperationMode_Type.__name__ = "OctetString"
_WtWebGraphAnalog57762BinaryOperationMode_Object = MibTableColumn
wtWebGraphAnalog57762BinaryOperationMode = _WtWebGraphAnalog57762BinaryOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 1),
    _WtWebGraphAnalog57762BinaryOperationMode_Type()
)
wtWebGraphAnalog57762BinaryOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762BinaryOperationMode.setStatus("mandatory")


class _WtWebGraphAnalog57762BinaryTcpServerLocalPort_Type(Integer32):
    """Custom type wtWebGraphAnalog57762BinaryTcpServerLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalog57762BinaryTcpServerLocalPort_Type.__name__ = "Integer32"
_WtWebGraphAnalog57762BinaryTcpServerLocalPort_Object = MibTableColumn
wtWebGraphAnalog57762BinaryTcpServerLocalPort = _WtWebGraphAnalog57762BinaryTcpServerLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 2),
    _WtWebGraphAnalog57762BinaryTcpServerLocalPort_Type()
)
wtWebGraphAnalog57762BinaryTcpServerLocalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762BinaryTcpServerLocalPort.setStatus("mandatory")


class _WtWebGraphAnalog57762BinaryTcpServerInputTrigger_Type(OctetString):
    """Custom type wtWebGraphAnalog57762BinaryTcpServerInputTrigger based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphAnalog57762BinaryTcpServerInputTrigger_Type.__name__ = "OctetString"
_WtWebGraphAnalog57762BinaryTcpServerInputTrigger_Object = MibTableColumn
wtWebGraphAnalog57762BinaryTcpServerInputTrigger = _WtWebGraphAnalog57762BinaryTcpServerInputTrigger_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 3),
    _WtWebGraphAnalog57762BinaryTcpServerInputTrigger_Type()
)
wtWebGraphAnalog57762BinaryTcpServerInputTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762BinaryTcpServerInputTrigger.setStatus("mandatory")


class _WtWebGraphAnalog57762BinaryTcpServerApplicationMode_Type(OctetString):
    """Custom type wtWebGraphAnalog57762BinaryTcpServerApplicationMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphAnalog57762BinaryTcpServerApplicationMode_Type.__name__ = "OctetString"
_WtWebGraphAnalog57762BinaryTcpServerApplicationMode_Object = MibTableColumn
wtWebGraphAnalog57762BinaryTcpServerApplicationMode = _WtWebGraphAnalog57762BinaryTcpServerApplicationMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 4),
    _WtWebGraphAnalog57762BinaryTcpServerApplicationMode_Type()
)
wtWebGraphAnalog57762BinaryTcpServerApplicationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762BinaryTcpServerApplicationMode.setStatus("mandatory")


class _WtWebGraphAnalog57762BinaryTcpClientLocalPort_Type(Integer32):
    """Custom type wtWebGraphAnalog57762BinaryTcpClientLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalog57762BinaryTcpClientLocalPort_Type.__name__ = "Integer32"
_WtWebGraphAnalog57762BinaryTcpClientLocalPort_Object = MibTableColumn
wtWebGraphAnalog57762BinaryTcpClientLocalPort = _WtWebGraphAnalog57762BinaryTcpClientLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 5),
    _WtWebGraphAnalog57762BinaryTcpClientLocalPort_Type()
)
wtWebGraphAnalog57762BinaryTcpClientLocalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762BinaryTcpClientLocalPort.setStatus("mandatory")


class _WtWebGraphAnalog57762BinaryTcpClientServerPort_Type(Integer32):
    """Custom type wtWebGraphAnalog57762BinaryTcpClientServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalog57762BinaryTcpClientServerPort_Type.__name__ = "Integer32"
_WtWebGraphAnalog57762BinaryTcpClientServerPort_Object = MibTableColumn
wtWebGraphAnalog57762BinaryTcpClientServerPort = _WtWebGraphAnalog57762BinaryTcpClientServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 6),
    _WtWebGraphAnalog57762BinaryTcpClientServerPort_Type()
)
wtWebGraphAnalog57762BinaryTcpClientServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762BinaryTcpClientServerPort.setStatus("mandatory")
_WtWebGraphAnalog57762BinaryTcpClientServerIpAddr_Type = OctetString
_WtWebGraphAnalog57762BinaryTcpClientServerIpAddr_Object = MibTableColumn
wtWebGraphAnalog57762BinaryTcpClientServerIpAddr = _WtWebGraphAnalog57762BinaryTcpClientServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 7),
    _WtWebGraphAnalog57762BinaryTcpClientServerIpAddr_Type()
)
wtWebGraphAnalog57762BinaryTcpClientServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762BinaryTcpClientServerIpAddr.setStatus("mandatory")
_WtWebGraphAnalog57762BinaryTcpClientServerPassword_Type = OctetString
_WtWebGraphAnalog57762BinaryTcpClientServerPassword_Object = MibTableColumn
wtWebGraphAnalog57762BinaryTcpClientServerPassword = _WtWebGraphAnalog57762BinaryTcpClientServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 8),
    _WtWebGraphAnalog57762BinaryTcpClientServerPassword_Type()
)
wtWebGraphAnalog57762BinaryTcpClientServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762BinaryTcpClientServerPassword.setStatus("mandatory")
_WtWebGraphAnalog57762BinaryTcpClientInactivity_Type = Integer32
_WtWebGraphAnalog57762BinaryTcpClientInactivity_Object = MibTableColumn
wtWebGraphAnalog57762BinaryTcpClientInactivity = _WtWebGraphAnalog57762BinaryTcpClientInactivity_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 9),
    _WtWebGraphAnalog57762BinaryTcpClientInactivity_Type()
)
wtWebGraphAnalog57762BinaryTcpClientInactivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762BinaryTcpClientInactivity.setStatus("mandatory")


class _WtWebGraphAnalog57762BinaryTcpClientInputTrigger_Type(OctetString):
    """Custom type wtWebGraphAnalog57762BinaryTcpClientInputTrigger based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphAnalog57762BinaryTcpClientInputTrigger_Type.__name__ = "OctetString"
_WtWebGraphAnalog57762BinaryTcpClientInputTrigger_Object = MibTableColumn
wtWebGraphAnalog57762BinaryTcpClientInputTrigger = _WtWebGraphAnalog57762BinaryTcpClientInputTrigger_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 10),
    _WtWebGraphAnalog57762BinaryTcpClientInputTrigger_Type()
)
wtWebGraphAnalog57762BinaryTcpClientInputTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762BinaryTcpClientInputTrigger.setStatus("mandatory")


class _WtWebGraphAnalog57762BinaryTcpClientInterval_Type(Integer32):
    """Custom type wtWebGraphAnalog57762BinaryTcpClientInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtWebGraphAnalog57762BinaryTcpClientInterval_Type.__name__ = "Integer32"
_WtWebGraphAnalog57762BinaryTcpClientInterval_Object = MibTableColumn
wtWebGraphAnalog57762BinaryTcpClientInterval = _WtWebGraphAnalog57762BinaryTcpClientInterval_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 11),
    _WtWebGraphAnalog57762BinaryTcpClientInterval_Type()
)
wtWebGraphAnalog57762BinaryTcpClientInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762BinaryTcpClientInterval.setStatus("mandatory")


class _WtWebGraphAnalog57762BinaryTcpClientApplicationMode_Type(OctetString):
    """Custom type wtWebGraphAnalog57762BinaryTcpClientApplicationMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphAnalog57762BinaryTcpClientApplicationMode_Type.__name__ = "OctetString"
_WtWebGraphAnalog57762BinaryTcpClientApplicationMode_Object = MibTableColumn
wtWebGraphAnalog57762BinaryTcpClientApplicationMode = _WtWebGraphAnalog57762BinaryTcpClientApplicationMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 12),
    _WtWebGraphAnalog57762BinaryTcpClientApplicationMode_Type()
)
wtWebGraphAnalog57762BinaryTcpClientApplicationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762BinaryTcpClientApplicationMode.setStatus("mandatory")


class _WtWebGraphAnalog57762BinaryUdpPeerLocalPort_Type(Integer32):
    """Custom type wtWebGraphAnalog57762BinaryUdpPeerLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalog57762BinaryUdpPeerLocalPort_Type.__name__ = "Integer32"
_WtWebGraphAnalog57762BinaryUdpPeerLocalPort_Object = MibTableColumn
wtWebGraphAnalog57762BinaryUdpPeerLocalPort = _WtWebGraphAnalog57762BinaryUdpPeerLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 13),
    _WtWebGraphAnalog57762BinaryUdpPeerLocalPort_Type()
)
wtWebGraphAnalog57762BinaryUdpPeerLocalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762BinaryUdpPeerLocalPort.setStatus("mandatory")


class _WtWebGraphAnalog57762BinaryUdpPeerRemotePort_Type(Integer32):
    """Custom type wtWebGraphAnalog57762BinaryUdpPeerRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalog57762BinaryUdpPeerRemotePort_Type.__name__ = "Integer32"
_WtWebGraphAnalog57762BinaryUdpPeerRemotePort_Object = MibTableColumn
wtWebGraphAnalog57762BinaryUdpPeerRemotePort = _WtWebGraphAnalog57762BinaryUdpPeerRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 14),
    _WtWebGraphAnalog57762BinaryUdpPeerRemotePort_Type()
)
wtWebGraphAnalog57762BinaryUdpPeerRemotePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762BinaryUdpPeerRemotePort.setStatus("mandatory")
_WtWebGraphAnalog57762BinaryUdpPeerRemoteIpAddr_Type = OctetString
_WtWebGraphAnalog57762BinaryUdpPeerRemoteIpAddr_Object = MibTableColumn
wtWebGraphAnalog57762BinaryUdpPeerRemoteIpAddr = _WtWebGraphAnalog57762BinaryUdpPeerRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 15),
    _WtWebGraphAnalog57762BinaryUdpPeerRemoteIpAddr_Type()
)
wtWebGraphAnalog57762BinaryUdpPeerRemoteIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762BinaryUdpPeerRemoteIpAddr.setStatus("mandatory")


class _WtWebGraphAnalog57762BinaryUdpPeerInputTrigger_Type(OctetString):
    """Custom type wtWebGraphAnalog57762BinaryUdpPeerInputTrigger based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphAnalog57762BinaryUdpPeerInputTrigger_Type.__name__ = "OctetString"
_WtWebGraphAnalog57762BinaryUdpPeerInputTrigger_Object = MibTableColumn
wtWebGraphAnalog57762BinaryUdpPeerInputTrigger = _WtWebGraphAnalog57762BinaryUdpPeerInputTrigger_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 16),
    _WtWebGraphAnalog57762BinaryUdpPeerInputTrigger_Type()
)
wtWebGraphAnalog57762BinaryUdpPeerInputTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762BinaryUdpPeerInputTrigger.setStatus("mandatory")


class _WtWebGraphAnalog57762BinaryUdpPeerInterval_Type(Integer32):
    """Custom type wtWebGraphAnalog57762BinaryUdpPeerInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtWebGraphAnalog57762BinaryUdpPeerInterval_Type.__name__ = "Integer32"
_WtWebGraphAnalog57762BinaryUdpPeerInterval_Object = MibTableColumn
wtWebGraphAnalog57762BinaryUdpPeerInterval = _WtWebGraphAnalog57762BinaryUdpPeerInterval_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 17),
    _WtWebGraphAnalog57762BinaryUdpPeerInterval_Type()
)
wtWebGraphAnalog57762BinaryUdpPeerInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762BinaryUdpPeerInterval.setStatus("mandatory")


class _WtWebGraphAnalog57762BinaryUdpPeerApplicationMode_Type(OctetString):
    """Custom type wtWebGraphAnalog57762BinaryUdpPeerApplicationMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphAnalog57762BinaryUdpPeerApplicationMode_Type.__name__ = "OctetString"
_WtWebGraphAnalog57762BinaryUdpPeerApplicationMode_Object = MibTableColumn
wtWebGraphAnalog57762BinaryUdpPeerApplicationMode = _WtWebGraphAnalog57762BinaryUdpPeerApplicationMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 18),
    _WtWebGraphAnalog57762BinaryUdpPeerApplicationMode_Type()
)
wtWebGraphAnalog57762BinaryUdpPeerApplicationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762BinaryUdpPeerApplicationMode.setStatus("mandatory")


class _WtWebGraphAnalog57762BinaryConnectedPort_Type(Integer32):
    """Custom type wtWebGraphAnalog57762BinaryConnectedPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalog57762BinaryConnectedPort_Type.__name__ = "Integer32"
_WtWebGraphAnalog57762BinaryConnectedPort_Object = MibTableColumn
wtWebGraphAnalog57762BinaryConnectedPort = _WtWebGraphAnalog57762BinaryConnectedPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 19),
    _WtWebGraphAnalog57762BinaryConnectedPort_Type()
)
wtWebGraphAnalog57762BinaryConnectedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762BinaryConnectedPort.setStatus("mandatory")
_WtWebGraphAnalog57762BinaryConnectedIpAddr_Type = IpAddress
_WtWebGraphAnalog57762BinaryConnectedIpAddr_Object = MibTableColumn
wtWebGraphAnalog57762BinaryConnectedIpAddr = _WtWebGraphAnalog57762BinaryConnectedIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 20),
    _WtWebGraphAnalog57762BinaryConnectedIpAddr_Type()
)
wtWebGraphAnalog57762BinaryConnectedIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762BinaryConnectedIpAddr.setStatus("mandatory")


class _WtWebGraphAnalog57762BinaryTcpServerClientHttpPort_Type(Integer32):
    """Custom type wtWebGraphAnalog57762BinaryTcpServerClientHttpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalog57762BinaryTcpServerClientHttpPort_Type.__name__ = "Integer32"
_WtWebGraphAnalog57762BinaryTcpServerClientHttpPort_Object = MibTableColumn
wtWebGraphAnalog57762BinaryTcpServerClientHttpPort = _WtWebGraphAnalog57762BinaryTcpServerClientHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 21),
    _WtWebGraphAnalog57762BinaryTcpServerClientHttpPort_Type()
)
wtWebGraphAnalog57762BinaryTcpServerClientHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762BinaryTcpServerClientHttpPort.setStatus("mandatory")


class _WtWebGraphAnalog57762BinaryTcpClientServerHttpPort_Type(Integer32):
    """Custom type wtWebGraphAnalog57762BinaryTcpClientServerHttpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalog57762BinaryTcpClientServerHttpPort_Type.__name__ = "Integer32"
_WtWebGraphAnalog57762BinaryTcpClientServerHttpPort_Object = MibTableColumn
wtWebGraphAnalog57762BinaryTcpClientServerHttpPort = _WtWebGraphAnalog57762BinaryTcpClientServerHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 22),
    _WtWebGraphAnalog57762BinaryTcpClientServerHttpPort_Type()
)
wtWebGraphAnalog57762BinaryTcpClientServerHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762BinaryTcpClientServerHttpPort.setStatus("mandatory")
_WtWebGraphAnalog57762BinaryTcpServerHysteresis1_Type = OctetString
_WtWebGraphAnalog57762BinaryTcpServerHysteresis1_Object = MibTableColumn
wtWebGraphAnalog57762BinaryTcpServerHysteresis1 = _WtWebGraphAnalog57762BinaryTcpServerHysteresis1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 23),
    _WtWebGraphAnalog57762BinaryTcpServerHysteresis1_Type()
)
wtWebGraphAnalog57762BinaryTcpServerHysteresis1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762BinaryTcpServerHysteresis1.setStatus("mandatory")
_WtWebGraphAnalog57762BinaryTcpServerHysteresis2_Type = OctetString
_WtWebGraphAnalog57762BinaryTcpServerHysteresis2_Object = MibTableColumn
wtWebGraphAnalog57762BinaryTcpServerHysteresis2 = _WtWebGraphAnalog57762BinaryTcpServerHysteresis2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 24),
    _WtWebGraphAnalog57762BinaryTcpServerHysteresis2_Type()
)
wtWebGraphAnalog57762BinaryTcpServerHysteresis2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762BinaryTcpServerHysteresis2.setStatus("mandatory")
_WtWebGraphAnalog57762BinaryTcpClientHysteresis1_Type = OctetString
_WtWebGraphAnalog57762BinaryTcpClientHysteresis1_Object = MibTableColumn
wtWebGraphAnalog57762BinaryTcpClientHysteresis1 = _WtWebGraphAnalog57762BinaryTcpClientHysteresis1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 25),
    _WtWebGraphAnalog57762BinaryTcpClientHysteresis1_Type()
)
wtWebGraphAnalog57762BinaryTcpClientHysteresis1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762BinaryTcpClientHysteresis1.setStatus("mandatory")
_WtWebGraphAnalog57762BinaryTcpClientHysteresis2_Type = OctetString
_WtWebGraphAnalog57762BinaryTcpClientHysteresis2_Object = MibTableColumn
wtWebGraphAnalog57762BinaryTcpClientHysteresis2 = _WtWebGraphAnalog57762BinaryTcpClientHysteresis2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 26),
    _WtWebGraphAnalog57762BinaryTcpClientHysteresis2_Type()
)
wtWebGraphAnalog57762BinaryTcpClientHysteresis2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762BinaryTcpClientHysteresis2.setStatus("mandatory")
_WtWebGraphAnalog57762BinaryUdpPeerHysteresis1_Type = OctetString
_WtWebGraphAnalog57762BinaryUdpPeerHysteresis1_Object = MibTableColumn
wtWebGraphAnalog57762BinaryUdpPeerHysteresis1 = _WtWebGraphAnalog57762BinaryUdpPeerHysteresis1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 27),
    _WtWebGraphAnalog57762BinaryUdpPeerHysteresis1_Type()
)
wtWebGraphAnalog57762BinaryUdpPeerHysteresis1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762BinaryUdpPeerHysteresis1.setStatus("mandatory")
_WtWebGraphAnalog57762BinaryUdpPeerHysteresis2_Type = OctetString
_WtWebGraphAnalog57762BinaryUdpPeerHysteresis2_Object = MibTableColumn
wtWebGraphAnalog57762BinaryUdpPeerHysteresis2 = _WtWebGraphAnalog57762BinaryUdpPeerHysteresis2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 28),
    _WtWebGraphAnalog57762BinaryUdpPeerHysteresis2_Type()
)
wtWebGraphAnalog57762BinaryUdpPeerHysteresis2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762BinaryUdpPeerHysteresis2.setStatus("mandatory")
_WtWebGraphAnalog57762BinaryTcpClientServerUserName_Type = OctetString
_WtWebGraphAnalog57762BinaryTcpClientServerUserName_Object = MibTableColumn
wtWebGraphAnalog57762BinaryTcpClientServerUserName = _WtWebGraphAnalog57762BinaryTcpClientServerUserName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 29),
    _WtWebGraphAnalog57762BinaryTcpClientServerUserName_Type()
)
wtWebGraphAnalog57762BinaryTcpClientServerUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762BinaryTcpClientServerUserName.setStatus("mandatory")
_WtWebGraphAnalog57762MQTT_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57762MQTT = _WtWebGraphAnalog57762MQTT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 12)
)
_WtWebGraphAnalog57762MQTTEnable_Type = OctetString
_WtWebGraphAnalog57762MQTTEnable_Object = MibScalar
wtWebGraphAnalog57762MQTTEnable = _WtWebGraphAnalog57762MQTTEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 12, 1),
    _WtWebGraphAnalog57762MQTTEnable_Type()
)
wtWebGraphAnalog57762MQTTEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762MQTTEnable.setStatus("mandatory")
_WtWebGraphAnalog57762MQTTBrockerIP_Type = OctetString
_WtWebGraphAnalog57762MQTTBrockerIP_Object = MibScalar
wtWebGraphAnalog57762MQTTBrockerIP = _WtWebGraphAnalog57762MQTTBrockerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 12, 2),
    _WtWebGraphAnalog57762MQTTBrockerIP_Type()
)
wtWebGraphAnalog57762MQTTBrockerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762MQTTBrockerIP.setStatus("mandatory")
_WtWebGraphAnalog57762MQTTUserName_Type = OctetString
_WtWebGraphAnalog57762MQTTUserName_Object = MibScalar
wtWebGraphAnalog57762MQTTUserName = _WtWebGraphAnalog57762MQTTUserName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 12, 3),
    _WtWebGraphAnalog57762MQTTUserName_Type()
)
wtWebGraphAnalog57762MQTTUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762MQTTUserName.setStatus("mandatory")
_WtWebGraphAnalog57762MQTTPassword_Type = OctetString
_WtWebGraphAnalog57762MQTTPassword_Object = MibScalar
wtWebGraphAnalog57762MQTTPassword = _WtWebGraphAnalog57762MQTTPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 12, 4),
    _WtWebGraphAnalog57762MQTTPassword_Type()
)
wtWebGraphAnalog57762MQTTPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762MQTTPassword.setStatus("mandatory")
_WtWebGraphAnalog57762MQTTLocalPort_Type = Integer32
_WtWebGraphAnalog57762MQTTLocalPort_Object = MibScalar
wtWebGraphAnalog57762MQTTLocalPort = _WtWebGraphAnalog57762MQTTLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 12, 5),
    _WtWebGraphAnalog57762MQTTLocalPort_Type()
)
wtWebGraphAnalog57762MQTTLocalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762MQTTLocalPort.setStatus("mandatory")
_WtWebGraphAnalog57762MQTTBrokerServerPort_Type = Integer32
_WtWebGraphAnalog57762MQTTBrokerServerPort_Object = MibScalar
wtWebGraphAnalog57762MQTTBrokerServerPort = _WtWebGraphAnalog57762MQTTBrokerServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 12, 6),
    _WtWebGraphAnalog57762MQTTBrokerServerPort_Type()
)
wtWebGraphAnalog57762MQTTBrokerServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762MQTTBrokerServerPort.setStatus("mandatory")
_WtWebGraphAnalog57762MQTTInterval_Type = Integer32
_WtWebGraphAnalog57762MQTTInterval_Object = MibScalar
wtWebGraphAnalog57762MQTTInterval = _WtWebGraphAnalog57762MQTTInterval_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 12, 7),
    _WtWebGraphAnalog57762MQTTInterval_Type()
)
wtWebGraphAnalog57762MQTTInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762MQTTInterval.setStatus("mandatory")
_WtWebGraphAnalog57762MQTTLastWillEnable_Type = OctetString
_WtWebGraphAnalog57762MQTTLastWillEnable_Object = MibScalar
wtWebGraphAnalog57762MQTTLastWillEnable = _WtWebGraphAnalog57762MQTTLastWillEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 12, 8),
    _WtWebGraphAnalog57762MQTTLastWillEnable_Type()
)
wtWebGraphAnalog57762MQTTLastWillEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762MQTTLastWillEnable.setStatus("mandatory")
_WtWebGraphAnalog57762MQTTLastWillTopic_Type = OctetString
_WtWebGraphAnalog57762MQTTLastWillTopic_Object = MibScalar
wtWebGraphAnalog57762MQTTLastWillTopic = _WtWebGraphAnalog57762MQTTLastWillTopic_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 12, 9),
    _WtWebGraphAnalog57762MQTTLastWillTopic_Type()
)
wtWebGraphAnalog57762MQTTLastWillTopic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762MQTTLastWillTopic.setStatus("mandatory")
_WtWebGraphAnalog57762MQTTLastWillMsg_Type = OctetString
_WtWebGraphAnalog57762MQTTLastWillMsg_Object = MibScalar
wtWebGraphAnalog57762MQTTLastWillMsg = _WtWebGraphAnalog57762MQTTLastWillMsg_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 12, 10),
    _WtWebGraphAnalog57762MQTTLastWillMsg_Type()
)
wtWebGraphAnalog57762MQTTLastWillMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762MQTTLastWillMsg.setStatus("mandatory")


class _WtWebGraphAnalog57762MQTTLastWillQoS_Type(OctetString):
    """Custom type wtWebGraphAnalog57762MQTTLastWillQoS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphAnalog57762MQTTLastWillQoS_Type.__name__ = "OctetString"
_WtWebGraphAnalog57762MQTTLastWillQoS_Object = MibScalar
wtWebGraphAnalog57762MQTTLastWillQoS = _WtWebGraphAnalog57762MQTTLastWillQoS_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 12, 11),
    _WtWebGraphAnalog57762MQTTLastWillQoS_Type()
)
wtWebGraphAnalog57762MQTTLastWillQoS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762MQTTLastWillQoS.setStatus("mandatory")


class _WtWebGraphAnalog57762MQTTLastWillRetain_Type(OctetString):
    """Custom type wtWebGraphAnalog57762MQTTLastWillRetain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphAnalog57762MQTTLastWillRetain_Type.__name__ = "OctetString"
_WtWebGraphAnalog57762MQTTLastWillRetain_Object = MibScalar
wtWebGraphAnalog57762MQTTLastWillRetain = _WtWebGraphAnalog57762MQTTLastWillRetain_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 12, 12),
    _WtWebGraphAnalog57762MQTTLastWillRetain_Type()
)
wtWebGraphAnalog57762MQTTLastWillRetain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762MQTTLastWillRetain.setStatus("mandatory")
_WtWebGraphAnalog57762MQTTLastWillConnectEnable_Type = OctetString
_WtWebGraphAnalog57762MQTTLastWillConnectEnable_Object = MibScalar
wtWebGraphAnalog57762MQTTLastWillConnectEnable = _WtWebGraphAnalog57762MQTTLastWillConnectEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 12, 13),
    _WtWebGraphAnalog57762MQTTLastWillConnectEnable_Type()
)
wtWebGraphAnalog57762MQTTLastWillConnectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762MQTTLastWillConnectEnable.setStatus("mandatory")
_WtWebGraphAnalog57762MQTTLastWillConnectMsg_Type = OctetString
_WtWebGraphAnalog57762MQTTLastWillConnectMsg_Object = MibScalar
wtWebGraphAnalog57762MQTTLastWillConnectMsg = _WtWebGraphAnalog57762MQTTLastWillConnectMsg_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 12, 14),
    _WtWebGraphAnalog57762MQTTLastWillConnectMsg_Type()
)
wtWebGraphAnalog57762MQTTLastWillConnectMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762MQTTLastWillConnectMsg.setStatus("mandatory")
_WtWebGraphAnalog57762REST_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57762REST = _WtWebGraphAnalog57762REST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 13)
)
_WtWebGraphAnalog57762RESTEnable_Type = OctetString
_WtWebGraphAnalog57762RESTEnable_Object = MibScalar
wtWebGraphAnalog57762RESTEnable = _WtWebGraphAnalog57762RESTEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 13, 1),
    _WtWebGraphAnalog57762RESTEnable_Type()
)
wtWebGraphAnalog57762RESTEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762RESTEnable.setStatus("mandatory")
_WtWebGraphAnalog57762RESTDigestAuthEnable_Type = OctetString
_WtWebGraphAnalog57762RESTDigestAuthEnable_Object = MibScalar
wtWebGraphAnalog57762RESTDigestAuthEnable = _WtWebGraphAnalog57762RESTDigestAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 13, 2),
    _WtWebGraphAnalog57762RESTDigestAuthEnable_Type()
)
wtWebGraphAnalog57762RESTDigestAuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762RESTDigestAuthEnable.setStatus("mandatory")
_WtWebGraphAnalog57762Datalogger_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57762Datalogger = _WtWebGraphAnalog57762Datalogger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 4)
)


class _WtWebGraphAnalog57762LoggerTimebase_Type(Integer32):
    """Custom type wtWebGraphAnalog57762LoggerTimebase based on Integer32"""
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
        *(("wtWebGraphAnalog57762Datalogger-15Sec", 1),
          ("wtWebGraphAnalog57762Datalogger-30Sec", 2),
          ("wtWebGraphAnalog57762Datalogger-1Min", 3),
          ("wtWebGraphAnalog57762Datalogger-5Min", 4),
          ("wtWebGraphAnalog57762Datalogger-15Min", 5),
          ("wtWebGraphAnalog57762Datalogger-60Min", 6))
    )


_WtWebGraphAnalog57762LoggerTimebase_Type.__name__ = "Integer32"
_WtWebGraphAnalog57762LoggerTimebase_Object = MibScalar
wtWebGraphAnalog57762LoggerTimebase = _WtWebGraphAnalog57762LoggerTimebase_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 4, 1),
    _WtWebGraphAnalog57762LoggerTimebase_Type()
)
wtWebGraphAnalog57762LoggerTimebase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762LoggerTimebase.setStatus("mandatory")


class _WtWebGraphAnalog57762LoggerSensorSel_Type(OctetString):
    """Custom type wtWebGraphAnalog57762LoggerSensorSel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphAnalog57762LoggerSensorSel_Type.__name__ = "OctetString"
_WtWebGraphAnalog57762LoggerSensorSel_Object = MibScalar
wtWebGraphAnalog57762LoggerSensorSel = _WtWebGraphAnalog57762LoggerSensorSel_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 4, 2),
    _WtWebGraphAnalog57762LoggerSensorSel_Type()
)
wtWebGraphAnalog57762LoggerSensorSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762LoggerSensorSel.setStatus("mandatory")
_WtWebGraphAnalog57762Alarm_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57762Alarm = _WtWebGraphAnalog57762Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5)
)


class _WtWebGraphAnalog57762AlarmCount_Type(Integer32):
    """Custom type wtWebGraphAnalog57762AlarmCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WtWebGraphAnalog57762AlarmCount_Type.__name__ = "Integer32"
_WtWebGraphAnalog57762AlarmCount_Object = MibScalar
wtWebGraphAnalog57762AlarmCount = _WtWebGraphAnalog57762AlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 1),
    _WtWebGraphAnalog57762AlarmCount_Type()
)
wtWebGraphAnalog57762AlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmCount.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmIfTable_Object = MibTable
wtWebGraphAnalog57762AlarmIfTable = _WtWebGraphAnalog57762AlarmIfTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 2)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmIfTable.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmIfEntry_Object = MibTableRow
wtWebGraphAnalog57762AlarmIfEntry = _WtWebGraphAnalog57762AlarmIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 2, 1)
)
wtWebGraphAnalog57762AlarmIfEntry.setIndexNames(
    (0, "WebGraph-AnalogIO-57762-US-MIB", "wtWebGraphAnalog57762AlarmNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmIfEntry.setStatus("mandatory")


class _WtWebGraphAnalog57762AlarmNo_Type(Integer32):
    """Custom type wtWebGraphAnalog57762AlarmNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WtWebGraphAnalog57762AlarmNo_Type.__name__ = "Integer32"
_WtWebGraphAnalog57762AlarmNo_Object = MibTableColumn
wtWebGraphAnalog57762AlarmNo = _WtWebGraphAnalog57762AlarmNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 2, 1, 1),
    _WtWebGraphAnalog57762AlarmNo_Type()
)
wtWebGraphAnalog57762AlarmNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmNo.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmTable_Object = MibTable
wtWebGraphAnalog57762AlarmTable = _WtWebGraphAnalog57762AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmTable.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmEntry_Object = MibTableRow
wtWebGraphAnalog57762AlarmEntry = _WtWebGraphAnalog57762AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1)
)
wtWebGraphAnalog57762AlarmEntry.setIndexNames(
    (0, "WebGraph-AnalogIO-57762-US-MIB", "wtWebGraphAnalog57762AlarmNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmEntry.setStatus("mandatory")


class _WtWebGraphAnalog57762AlarmTrigger_Type(OctetString):
    """Custom type wtWebGraphAnalog57762AlarmTrigger based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphAnalog57762AlarmTrigger_Type.__name__ = "OctetString"
_WtWebGraphAnalog57762AlarmTrigger_Object = MibTableColumn
wtWebGraphAnalog57762AlarmTrigger = _WtWebGraphAnalog57762AlarmTrigger_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 1),
    _WtWebGraphAnalog57762AlarmTrigger_Type()
)
wtWebGraphAnalog57762AlarmTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmTrigger.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmMin1_Type = OctetString
_WtWebGraphAnalog57762AlarmMin1_Object = MibTableColumn
wtWebGraphAnalog57762AlarmMin1 = _WtWebGraphAnalog57762AlarmMin1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 2),
    _WtWebGraphAnalog57762AlarmMin1_Type()
)
wtWebGraphAnalog57762AlarmMin1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmMin1.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmMax1_Type = OctetString
_WtWebGraphAnalog57762AlarmMax1_Object = MibTableColumn
wtWebGraphAnalog57762AlarmMax1 = _WtWebGraphAnalog57762AlarmMax1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 3),
    _WtWebGraphAnalog57762AlarmMax1_Type()
)
wtWebGraphAnalog57762AlarmMax1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmMax1.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmHysteresis1_Type = OctetString
_WtWebGraphAnalog57762AlarmHysteresis1_Object = MibTableColumn
wtWebGraphAnalog57762AlarmHysteresis1 = _WtWebGraphAnalog57762AlarmHysteresis1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 4),
    _WtWebGraphAnalog57762AlarmHysteresis1_Type()
)
wtWebGraphAnalog57762AlarmHysteresis1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmHysteresis1.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmDelay_Type = OctetString
_WtWebGraphAnalog57762AlarmDelay_Object = MibTableColumn
wtWebGraphAnalog57762AlarmDelay = _WtWebGraphAnalog57762AlarmDelay_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 5),
    _WtWebGraphAnalog57762AlarmDelay_Type()
)
wtWebGraphAnalog57762AlarmDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmDelay.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmInterval_Type = OctetString
_WtWebGraphAnalog57762AlarmInterval_Object = MibTableColumn
wtWebGraphAnalog57762AlarmInterval = _WtWebGraphAnalog57762AlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 6),
    _WtWebGraphAnalog57762AlarmInterval_Type()
)
wtWebGraphAnalog57762AlarmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmInterval.setStatus("mandatory")


class _WtWebGraphAnalog57762AlarmEnable_Type(OctetString):
    """Custom type wtWebGraphAnalog57762AlarmEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphAnalog57762AlarmEnable_Type.__name__ = "OctetString"
_WtWebGraphAnalog57762AlarmEnable_Object = MibTableColumn
wtWebGraphAnalog57762AlarmEnable = _WtWebGraphAnalog57762AlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 7),
    _WtWebGraphAnalog57762AlarmEnable_Type()
)
wtWebGraphAnalog57762AlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmEnable.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmEMailAddr_Type = OctetString
_WtWebGraphAnalog57762AlarmEMailAddr_Object = MibTableColumn
wtWebGraphAnalog57762AlarmEMailAddr = _WtWebGraphAnalog57762AlarmEMailAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 8),
    _WtWebGraphAnalog57762AlarmEMailAddr_Type()
)
wtWebGraphAnalog57762AlarmEMailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmEMailAddr.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmMailSubject_Type = OctetString
_WtWebGraphAnalog57762AlarmMailSubject_Object = MibTableColumn
wtWebGraphAnalog57762AlarmMailSubject = _WtWebGraphAnalog57762AlarmMailSubject_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 9),
    _WtWebGraphAnalog57762AlarmMailSubject_Type()
)
wtWebGraphAnalog57762AlarmMailSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmMailSubject.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmMailText_Type = OctetString
_WtWebGraphAnalog57762AlarmMailText_Object = MibTableColumn
wtWebGraphAnalog57762AlarmMailText = _WtWebGraphAnalog57762AlarmMailText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 10),
    _WtWebGraphAnalog57762AlarmMailText_Type()
)
wtWebGraphAnalog57762AlarmMailText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmMailText.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmManagerIP_Type = OctetString
_WtWebGraphAnalog57762AlarmManagerIP_Object = MibTableColumn
wtWebGraphAnalog57762AlarmManagerIP = _WtWebGraphAnalog57762AlarmManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 11),
    _WtWebGraphAnalog57762AlarmManagerIP_Type()
)
wtWebGraphAnalog57762AlarmManagerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmManagerIP.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmTrapText_Type = OctetString
_WtWebGraphAnalog57762AlarmTrapText_Object = MibTableColumn
wtWebGraphAnalog57762AlarmTrapText = _WtWebGraphAnalog57762AlarmTrapText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 12),
    _WtWebGraphAnalog57762AlarmTrapText_Type()
)
wtWebGraphAnalog57762AlarmTrapText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmTrapText.setStatus("mandatory")


class _WtWebGraphAnalog57762AlarmMailOptions_Type(OctetString):
    """Custom type wtWebGraphAnalog57762AlarmMailOptions based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphAnalog57762AlarmMailOptions_Type.__name__ = "OctetString"
_WtWebGraphAnalog57762AlarmMailOptions_Object = MibTableColumn
wtWebGraphAnalog57762AlarmMailOptions = _WtWebGraphAnalog57762AlarmMailOptions_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 13),
    _WtWebGraphAnalog57762AlarmMailOptions_Type()
)
wtWebGraphAnalog57762AlarmMailOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmMailOptions.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmTcpIpAddr_Type = OctetString
_WtWebGraphAnalog57762AlarmTcpIpAddr_Object = MibTableColumn
wtWebGraphAnalog57762AlarmTcpIpAddr = _WtWebGraphAnalog57762AlarmTcpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 14),
    _WtWebGraphAnalog57762AlarmTcpIpAddr_Type()
)
wtWebGraphAnalog57762AlarmTcpIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmTcpIpAddr.setStatus("mandatory")


class _WtWebGraphAnalog57762AlarmTcpPort_Type(Integer32):
    """Custom type wtWebGraphAnalog57762AlarmTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalog57762AlarmTcpPort_Type.__name__ = "Integer32"
_WtWebGraphAnalog57762AlarmTcpPort_Object = MibTableColumn
wtWebGraphAnalog57762AlarmTcpPort = _WtWebGraphAnalog57762AlarmTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 15),
    _WtWebGraphAnalog57762AlarmTcpPort_Type()
)
wtWebGraphAnalog57762AlarmTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmTcpPort.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmTcpText_Type = OctetString
_WtWebGraphAnalog57762AlarmTcpText_Object = MibTableColumn
wtWebGraphAnalog57762AlarmTcpText = _WtWebGraphAnalog57762AlarmTcpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 16),
    _WtWebGraphAnalog57762AlarmTcpText_Type()
)
wtWebGraphAnalog57762AlarmTcpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmTcpText.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmClearMailSubject_Type = OctetString
_WtWebGraphAnalog57762AlarmClearMailSubject_Object = MibTableColumn
wtWebGraphAnalog57762AlarmClearMailSubject = _WtWebGraphAnalog57762AlarmClearMailSubject_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 17),
    _WtWebGraphAnalog57762AlarmClearMailSubject_Type()
)
wtWebGraphAnalog57762AlarmClearMailSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmClearMailSubject.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmClearMailText_Type = OctetString
_WtWebGraphAnalog57762AlarmClearMailText_Object = MibTableColumn
wtWebGraphAnalog57762AlarmClearMailText = _WtWebGraphAnalog57762AlarmClearMailText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 18),
    _WtWebGraphAnalog57762AlarmClearMailText_Type()
)
wtWebGraphAnalog57762AlarmClearMailText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmClearMailText.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmClearTrapText_Type = OctetString
_WtWebGraphAnalog57762AlarmClearTrapText_Object = MibTableColumn
wtWebGraphAnalog57762AlarmClearTrapText = _WtWebGraphAnalog57762AlarmClearTrapText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 19),
    _WtWebGraphAnalog57762AlarmClearTrapText_Type()
)
wtWebGraphAnalog57762AlarmClearTrapText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmClearTrapText.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmClearTcpText_Type = OctetString
_WtWebGraphAnalog57762AlarmClearTcpText_Object = MibTableColumn
wtWebGraphAnalog57762AlarmClearTcpText = _WtWebGraphAnalog57762AlarmClearTcpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 20),
    _WtWebGraphAnalog57762AlarmClearTcpText_Type()
)
wtWebGraphAnalog57762AlarmClearTcpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmClearTcpText.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmMin2_Type = OctetString
_WtWebGraphAnalog57762AlarmMin2_Object = MibTableColumn
wtWebGraphAnalog57762AlarmMin2 = _WtWebGraphAnalog57762AlarmMin2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 21),
    _WtWebGraphAnalog57762AlarmMin2_Type()
)
wtWebGraphAnalog57762AlarmMin2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmMin2.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmMax2_Type = OctetString
_WtWebGraphAnalog57762AlarmMax2_Object = MibTableColumn
wtWebGraphAnalog57762AlarmMax2 = _WtWebGraphAnalog57762AlarmMax2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 22),
    _WtWebGraphAnalog57762AlarmMax2_Type()
)
wtWebGraphAnalog57762AlarmMax2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmMax2.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmHysteresis2_Type = OctetString
_WtWebGraphAnalog57762AlarmHysteresis2_Object = MibTableColumn
wtWebGraphAnalog57762AlarmHysteresis2 = _WtWebGraphAnalog57762AlarmHysteresis2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 23),
    _WtWebGraphAnalog57762AlarmHysteresis2_Type()
)
wtWebGraphAnalog57762AlarmHysteresis2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmHysteresis2.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmSyslogIpAddr_Type = OctetString
_WtWebGraphAnalog57762AlarmSyslogIpAddr_Object = MibTableColumn
wtWebGraphAnalog57762AlarmSyslogIpAddr = _WtWebGraphAnalog57762AlarmSyslogIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 24),
    _WtWebGraphAnalog57762AlarmSyslogIpAddr_Type()
)
wtWebGraphAnalog57762AlarmSyslogIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmSyslogIpAddr.setStatus("mandatory")


class _WtWebGraphAnalog57762AlarmSyslogPort_Type(Integer32):
    """Custom type wtWebGraphAnalog57762AlarmSyslogPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalog57762AlarmSyslogPort_Type.__name__ = "Integer32"
_WtWebGraphAnalog57762AlarmSyslogPort_Object = MibTableColumn
wtWebGraphAnalog57762AlarmSyslogPort = _WtWebGraphAnalog57762AlarmSyslogPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 25),
    _WtWebGraphAnalog57762AlarmSyslogPort_Type()
)
wtWebGraphAnalog57762AlarmSyslogPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmSyslogPort.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmSyslogText_Type = OctetString
_WtWebGraphAnalog57762AlarmSyslogText_Object = MibTableColumn
wtWebGraphAnalog57762AlarmSyslogText = _WtWebGraphAnalog57762AlarmSyslogText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 26),
    _WtWebGraphAnalog57762AlarmSyslogText_Type()
)
wtWebGraphAnalog57762AlarmSyslogText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmSyslogText.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmSyslogClearText_Type = OctetString
_WtWebGraphAnalog57762AlarmSyslogClearText_Object = MibTableColumn
wtWebGraphAnalog57762AlarmSyslogClearText = _WtWebGraphAnalog57762AlarmSyslogClearText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 27),
    _WtWebGraphAnalog57762AlarmSyslogClearText_Type()
)
wtWebGraphAnalog57762AlarmSyslogClearText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmSyslogClearText.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmFtpDataPort_Type = OctetString
_WtWebGraphAnalog57762AlarmFtpDataPort_Object = MibTableColumn
wtWebGraphAnalog57762AlarmFtpDataPort = _WtWebGraphAnalog57762AlarmFtpDataPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 28),
    _WtWebGraphAnalog57762AlarmFtpDataPort_Type()
)
wtWebGraphAnalog57762AlarmFtpDataPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmFtpDataPort.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmFtpFileName_Type = OctetString
_WtWebGraphAnalog57762AlarmFtpFileName_Object = MibTableColumn
wtWebGraphAnalog57762AlarmFtpFileName = _WtWebGraphAnalog57762AlarmFtpFileName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 29),
    _WtWebGraphAnalog57762AlarmFtpFileName_Type()
)
wtWebGraphAnalog57762AlarmFtpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmFtpFileName.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmFtpText_Type = OctetString
_WtWebGraphAnalog57762AlarmFtpText_Object = MibTableColumn
wtWebGraphAnalog57762AlarmFtpText = _WtWebGraphAnalog57762AlarmFtpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 30),
    _WtWebGraphAnalog57762AlarmFtpText_Type()
)
wtWebGraphAnalog57762AlarmFtpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmFtpText.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmFtpClearText_Type = OctetString
_WtWebGraphAnalog57762AlarmFtpClearText_Object = MibTableColumn
wtWebGraphAnalog57762AlarmFtpClearText = _WtWebGraphAnalog57762AlarmFtpClearText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 31),
    _WtWebGraphAnalog57762AlarmFtpClearText_Type()
)
wtWebGraphAnalog57762AlarmFtpClearText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmFtpClearText.setStatus("mandatory")


class _WtWebGraphAnalog57762AlarmFtpOption_Type(OctetString):
    """Custom type wtWebGraphAnalog57762AlarmFtpOption based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphAnalog57762AlarmFtpOption_Type.__name__ = "OctetString"
_WtWebGraphAnalog57762AlarmFtpOption_Object = MibTableColumn
wtWebGraphAnalog57762AlarmFtpOption = _WtWebGraphAnalog57762AlarmFtpOption_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 32),
    _WtWebGraphAnalog57762AlarmFtpOption_Type()
)
wtWebGraphAnalog57762AlarmFtpOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmFtpOption.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmTimerCron_Type = OctetString
_WtWebGraphAnalog57762AlarmTimerCron_Object = MibTableColumn
wtWebGraphAnalog57762AlarmTimerCron = _WtWebGraphAnalog57762AlarmTimerCron_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 33),
    _WtWebGraphAnalog57762AlarmTimerCron_Type()
)
wtWebGraphAnalog57762AlarmTimerCron.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmTimerCron.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmName_Type = OctetString
_WtWebGraphAnalog57762AlarmName_Object = MibTableColumn
wtWebGraphAnalog57762AlarmName = _WtWebGraphAnalog57762AlarmName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 39),
    _WtWebGraphAnalog57762AlarmName_Type()
)
wtWebGraphAnalog57762AlarmName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmName.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmActive_Type = OctetString
_WtWebGraphAnalog57762AlarmActive_Object = MibTableColumn
wtWebGraphAnalog57762AlarmActive = _WtWebGraphAnalog57762AlarmActive_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 40),
    _WtWebGraphAnalog57762AlarmActive_Type()
)
wtWebGraphAnalog57762AlarmActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmActive.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmHttpReqAuthEnable_Type = OctetString
_WtWebGraphAnalog57762AlarmHttpReqAuthEnable_Object = MibTableColumn
wtWebGraphAnalog57762AlarmHttpReqAuthEnable = _WtWebGraphAnalog57762AlarmHttpReqAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 61),
    _WtWebGraphAnalog57762AlarmHttpReqAuthEnable_Type()
)
wtWebGraphAnalog57762AlarmHttpReqAuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmHttpReqAuthEnable.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmHttpReqAuthUser_Type = OctetString
_WtWebGraphAnalog57762AlarmHttpReqAuthUser_Object = MibTableColumn
wtWebGraphAnalog57762AlarmHttpReqAuthUser = _WtWebGraphAnalog57762AlarmHttpReqAuthUser_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 62),
    _WtWebGraphAnalog57762AlarmHttpReqAuthUser_Type()
)
wtWebGraphAnalog57762AlarmHttpReqAuthUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmHttpReqAuthUser.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmHttpReqAuthPassword_Type = OctetString
_WtWebGraphAnalog57762AlarmHttpReqAuthPassword_Object = MibTableColumn
wtWebGraphAnalog57762AlarmHttpReqAuthPassword = _WtWebGraphAnalog57762AlarmHttpReqAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 63),
    _WtWebGraphAnalog57762AlarmHttpReqAuthPassword_Type()
)
wtWebGraphAnalog57762AlarmHttpReqAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmHttpReqAuthPassword.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmHttpReqSetUrl_Type = OctetString
_WtWebGraphAnalog57762AlarmHttpReqSetUrl_Object = MibTableColumn
wtWebGraphAnalog57762AlarmHttpReqSetUrl = _WtWebGraphAnalog57762AlarmHttpReqSetUrl_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 64),
    _WtWebGraphAnalog57762AlarmHttpReqSetUrl_Type()
)
wtWebGraphAnalog57762AlarmHttpReqSetUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmHttpReqSetUrl.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmHttpReqClearUrl_Type = OctetString
_WtWebGraphAnalog57762AlarmHttpReqClearUrl_Object = MibTableColumn
wtWebGraphAnalog57762AlarmHttpReqClearUrl = _WtWebGraphAnalog57762AlarmHttpReqClearUrl_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 65),
    _WtWebGraphAnalog57762AlarmHttpReqClearUrl_Type()
)
wtWebGraphAnalog57762AlarmHttpReqClearUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmHttpReqClearUrl.setStatus("mandatory")


class _WtWebGraphAnalog57762AlarmHttpReqServerPort_Type(Integer32):
    """Custom type wtWebGraphAnalog57762AlarmHttpReqServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalog57762AlarmHttpReqServerPort_Type.__name__ = "Integer32"
_WtWebGraphAnalog57762AlarmHttpReqServerPort_Object = MibTableColumn
wtWebGraphAnalog57762AlarmHttpReqServerPort = _WtWebGraphAnalog57762AlarmHttpReqServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 66),
    _WtWebGraphAnalog57762AlarmHttpReqServerPort_Type()
)
wtWebGraphAnalog57762AlarmHttpReqServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmHttpReqServerPort.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmMqttTopicPath_Type = OctetString
_WtWebGraphAnalog57762AlarmMqttTopicPath_Object = MibTableColumn
wtWebGraphAnalog57762AlarmMqttTopicPath = _WtWebGraphAnalog57762AlarmMqttTopicPath_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 67),
    _WtWebGraphAnalog57762AlarmMqttTopicPath_Type()
)
wtWebGraphAnalog57762AlarmMqttTopicPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmMqttTopicPath.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmMqttTopicSetTopic_Type = OctetString
_WtWebGraphAnalog57762AlarmMqttTopicSetTopic_Object = MibTableColumn
wtWebGraphAnalog57762AlarmMqttTopicSetTopic = _WtWebGraphAnalog57762AlarmMqttTopicSetTopic_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 68),
    _WtWebGraphAnalog57762AlarmMqttTopicSetTopic_Type()
)
wtWebGraphAnalog57762AlarmMqttTopicSetTopic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmMqttTopicSetTopic.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmMqttTopicClear_Type = OctetString
_WtWebGraphAnalog57762AlarmMqttTopicClear_Object = MibTableColumn
wtWebGraphAnalog57762AlarmMqttTopicClear = _WtWebGraphAnalog57762AlarmMqttTopicClear_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 69),
    _WtWebGraphAnalog57762AlarmMqttTopicClear_Type()
)
wtWebGraphAnalog57762AlarmMqttTopicClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmMqttTopicClear.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmSensorLostSelection_Type = OctetString
_WtWebGraphAnalog57762AlarmSensorLostSelection_Object = MibTableColumn
wtWebGraphAnalog57762AlarmSensorLostSelection = _WtWebGraphAnalog57762AlarmSensorLostSelection_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 70),
    _WtWebGraphAnalog57762AlarmSensorLostSelection_Type()
)
wtWebGraphAnalog57762AlarmSensorLostSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmSensorLostSelection.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmLimitWindow_Type = OctetString
_WtWebGraphAnalog57762AlarmLimitWindow_Object = MibTableColumn
wtWebGraphAnalog57762AlarmLimitWindow = _WtWebGraphAnalog57762AlarmLimitWindow_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 71),
    _WtWebGraphAnalog57762AlarmLimitWindow_Type()
)
wtWebGraphAnalog57762AlarmLimitWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmLimitWindow.setStatus("mandatory")
_WtWebGraphAnalog57762AlarmSnmpManagerPort_Type = Integer32
_WtWebGraphAnalog57762AlarmSnmpManagerPort_Object = MibTableColumn
wtWebGraphAnalog57762AlarmSnmpManagerPort = _WtWebGraphAnalog57762AlarmSnmpManagerPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 76),
    _WtWebGraphAnalog57762AlarmSnmpManagerPort_Type()
)
wtWebGraphAnalog57762AlarmSnmpManagerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmSnmpManagerPort.setStatus("mandatory")


class _WtWebGraphAnalog57762AlarmMqttQoS_Type(OctetString):
    """Custom type wtWebGraphAnalog57762AlarmMqttQoS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphAnalog57762AlarmMqttQoS_Type.__name__ = "OctetString"
_WtWebGraphAnalog57762AlarmMqttQoS_Object = MibTableColumn
wtWebGraphAnalog57762AlarmMqttQoS = _WtWebGraphAnalog57762AlarmMqttQoS_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 77),
    _WtWebGraphAnalog57762AlarmMqttQoS_Type()
)
wtWebGraphAnalog57762AlarmMqttQoS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmMqttQoS.setStatus("mandatory")


class _WtWebGraphAnalog57762AlarmMqttRetain_Type(OctetString):
    """Custom type wtWebGraphAnalog57762AlarmMqttRetain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphAnalog57762AlarmMqttRetain_Type.__name__ = "OctetString"
_WtWebGraphAnalog57762AlarmMqttRetain_Object = MibTableColumn
wtWebGraphAnalog57762AlarmMqttRetain = _WtWebGraphAnalog57762AlarmMqttRetain_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 78),
    _WtWebGraphAnalog57762AlarmMqttRetain_Type()
)
wtWebGraphAnalog57762AlarmMqttRetain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlarmMqttRetain.setStatus("mandatory")
_WtWebGraphAnalog57762Graphics_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57762Graphics = _WtWebGraphAnalog57762Graphics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6)
)
_WtWebGraphAnalog57762GraphicsBase_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57762GraphicsBase = _WtWebGraphAnalog57762GraphicsBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 1)
)
_WtWebGraphAnalog57762GraphicsBaseEnable_Type = OctetString
_WtWebGraphAnalog57762GraphicsBaseEnable_Object = MibScalar
wtWebGraphAnalog57762GraphicsBaseEnable = _WtWebGraphAnalog57762GraphicsBaseEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 1, 1),
    _WtWebGraphAnalog57762GraphicsBaseEnable_Type()
)
wtWebGraphAnalog57762GraphicsBaseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762GraphicsBaseEnable.setStatus("mandatory")
_WtWebGraphAnalog57762GraphicsBaseWidth_Type = Integer32
_WtWebGraphAnalog57762GraphicsBaseWidth_Object = MibScalar
wtWebGraphAnalog57762GraphicsBaseWidth = _WtWebGraphAnalog57762GraphicsBaseWidth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 1, 2),
    _WtWebGraphAnalog57762GraphicsBaseWidth_Type()
)
wtWebGraphAnalog57762GraphicsBaseWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762GraphicsBaseWidth.setStatus("mandatory")
_WtWebGraphAnalog57762GraphicsBaseHeight_Type = Integer32
_WtWebGraphAnalog57762GraphicsBaseHeight_Object = MibScalar
wtWebGraphAnalog57762GraphicsBaseHeight = _WtWebGraphAnalog57762GraphicsBaseHeight_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 1, 3),
    _WtWebGraphAnalog57762GraphicsBaseHeight_Type()
)
wtWebGraphAnalog57762GraphicsBaseHeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762GraphicsBaseHeight.setStatus("mandatory")


class _WtWebGraphAnalog57762GraphicsBaseFrameColor_Type(OctetString):
    """Custom type wtWebGraphAnalog57762GraphicsBaseFrameColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_WtWebGraphAnalog57762GraphicsBaseFrameColor_Type.__name__ = "OctetString"
_WtWebGraphAnalog57762GraphicsBaseFrameColor_Object = MibScalar
wtWebGraphAnalog57762GraphicsBaseFrameColor = _WtWebGraphAnalog57762GraphicsBaseFrameColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 1, 4),
    _WtWebGraphAnalog57762GraphicsBaseFrameColor_Type()
)
wtWebGraphAnalog57762GraphicsBaseFrameColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762GraphicsBaseFrameColor.setStatus("mandatory")


class _WtWebGraphAnalog57762GraphicsBaseBackgroundColor_Type(OctetString):
    """Custom type wtWebGraphAnalog57762GraphicsBaseBackgroundColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_WtWebGraphAnalog57762GraphicsBaseBackgroundColor_Type.__name__ = "OctetString"
_WtWebGraphAnalog57762GraphicsBaseBackgroundColor_Object = MibScalar
wtWebGraphAnalog57762GraphicsBaseBackgroundColor = _WtWebGraphAnalog57762GraphicsBaseBackgroundColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 1, 5),
    _WtWebGraphAnalog57762GraphicsBaseBackgroundColor_Type()
)
wtWebGraphAnalog57762GraphicsBaseBackgroundColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762GraphicsBaseBackgroundColor.setStatus("mandatory")
_WtWebGraphAnalog57762GraphicsBasePollingrate_Type = Integer32
_WtWebGraphAnalog57762GraphicsBasePollingrate_Object = MibScalar
wtWebGraphAnalog57762GraphicsBasePollingrate = _WtWebGraphAnalog57762GraphicsBasePollingrate_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 1, 6),
    _WtWebGraphAnalog57762GraphicsBasePollingrate_Type()
)
wtWebGraphAnalog57762GraphicsBasePollingrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762GraphicsBasePollingrate.setStatus("mandatory")
_WtWebGraphAnalog57762GraphicsSelect_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57762GraphicsSelect = _WtWebGraphAnalog57762GraphicsSelect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 2)
)


class _WtWebGraphAnalog57762GraphicsSelectDisplaySensorSel_Type(OctetString):
    """Custom type wtWebGraphAnalog57762GraphicsSelectDisplaySensorSel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphAnalog57762GraphicsSelectDisplaySensorSel_Type.__name__ = "OctetString"
_WtWebGraphAnalog57762GraphicsSelectDisplaySensorSel_Object = MibScalar
wtWebGraphAnalog57762GraphicsSelectDisplaySensorSel = _WtWebGraphAnalog57762GraphicsSelectDisplaySensorSel_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 2, 1),
    _WtWebGraphAnalog57762GraphicsSelectDisplaySensorSel_Type()
)
wtWebGraphAnalog57762GraphicsSelectDisplaySensorSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762GraphicsSelectDisplaySensorSel.setStatus("mandatory")


class _WtWebGraphAnalog57762GraphicsSelectDisplayShowExtrem_Type(OctetString):
    """Custom type wtWebGraphAnalog57762GraphicsSelectDisplayShowExtrem based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphAnalog57762GraphicsSelectDisplayShowExtrem_Type.__name__ = "OctetString"
_WtWebGraphAnalog57762GraphicsSelectDisplayShowExtrem_Object = MibScalar
wtWebGraphAnalog57762GraphicsSelectDisplayShowExtrem = _WtWebGraphAnalog57762GraphicsSelectDisplayShowExtrem_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 2, 2),
    _WtWebGraphAnalog57762GraphicsSelectDisplayShowExtrem_Type()
)
wtWebGraphAnalog57762GraphicsSelectDisplayShowExtrem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762GraphicsSelectDisplayShowExtrem.setStatus("mandatory")
_WtWebGraphAnalog57762SensorColor2Table_Object = MibTable
wtWebGraphAnalog57762SensorColor2Table = _WtWebGraphAnalog57762SensorColor2Table_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 2, 3)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762SensorColor2Table.setStatus("mandatory")
_WtWebGraphAnalog57762SensorColor2Entry_Object = MibTableRow
wtWebGraphAnalog57762SensorColor2Entry = _WtWebGraphAnalog57762SensorColor2Entry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 2, 3, 1)
)
wtWebGraphAnalog57762SensorColor2Entry.setIndexNames(
    (0, "WebGraph-AnalogIO-57762-US-MIB", "wtWebGraphAnalog57762SensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762SensorColor2Entry.setStatus("mandatory")


class _WtWebGraphAnalog57762GraphicsSensorColor_Type(OctetString):
    """Custom type wtWebGraphAnalog57762GraphicsSensorColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_WtWebGraphAnalog57762GraphicsSensorColor_Type.__name__ = "OctetString"
_WtWebGraphAnalog57762GraphicsSensorColor_Object = MibTableColumn
wtWebGraphAnalog57762GraphicsSensorColor = _WtWebGraphAnalog57762GraphicsSensorColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 2, 3, 1, 1),
    _WtWebGraphAnalog57762GraphicsSensorColor_Type()
)
wtWebGraphAnalog57762GraphicsSensorColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762GraphicsSensorColor.setStatus("mandatory")
_WtWebGraphAnalog57762GraphicsSelectScale_Type = OctetString
_WtWebGraphAnalog57762GraphicsSelectScale_Object = MibTableColumn
wtWebGraphAnalog57762GraphicsSelectScale = _WtWebGraphAnalog57762GraphicsSelectScale_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 2, 3, 1, 2),
    _WtWebGraphAnalog57762GraphicsSelectScale_Type()
)
wtWebGraphAnalog57762GraphicsSelectScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762GraphicsSelectScale.setStatus("mandatory")
_WtWebGraphAnalog57762GraphicsScale_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57762GraphicsScale = _WtWebGraphAnalog57762GraphicsScale_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 3)
)
_WtWebGraphAnalog57762GraphicsScaleAutoScaleEnable_Type = OctetString
_WtWebGraphAnalog57762GraphicsScaleAutoScaleEnable_Object = MibScalar
wtWebGraphAnalog57762GraphicsScaleAutoScaleEnable = _WtWebGraphAnalog57762GraphicsScaleAutoScaleEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 3, 1),
    _WtWebGraphAnalog57762GraphicsScaleAutoScaleEnable_Type()
)
wtWebGraphAnalog57762GraphicsScaleAutoScaleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762GraphicsScaleAutoScaleEnable.setStatus("mandatory")
_WtWebGraphAnalog57762GraphicsScaleAutoFitEnable_Type = OctetString
_WtWebGraphAnalog57762GraphicsScaleAutoFitEnable_Object = MibScalar
wtWebGraphAnalog57762GraphicsScaleAutoFitEnable = _WtWebGraphAnalog57762GraphicsScaleAutoFitEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 3, 2),
    _WtWebGraphAnalog57762GraphicsScaleAutoFitEnable_Type()
)
wtWebGraphAnalog57762GraphicsScaleAutoFitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762GraphicsScaleAutoFitEnable.setStatus("mandatory")
_WtWebGraphAnalog57762GraphicsScale1Min_Type = Integer32
_WtWebGraphAnalog57762GraphicsScale1Min_Object = MibScalar
wtWebGraphAnalog57762GraphicsScale1Min = _WtWebGraphAnalog57762GraphicsScale1Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 3, 3),
    _WtWebGraphAnalog57762GraphicsScale1Min_Type()
)
wtWebGraphAnalog57762GraphicsScale1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762GraphicsScale1Min.setStatus("mandatory")
_WtWebGraphAnalog57762GraphicsScale2Min_Type = Integer32
_WtWebGraphAnalog57762GraphicsScale2Min_Object = MibScalar
wtWebGraphAnalog57762GraphicsScale2Min = _WtWebGraphAnalog57762GraphicsScale2Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 3, 4),
    _WtWebGraphAnalog57762GraphicsScale2Min_Type()
)
wtWebGraphAnalog57762GraphicsScale2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762GraphicsScale2Min.setStatus("mandatory")
_WtWebGraphAnalog57762GraphicsScale1Max_Type = Integer32
_WtWebGraphAnalog57762GraphicsScale1Max_Object = MibScalar
wtWebGraphAnalog57762GraphicsScale1Max = _WtWebGraphAnalog57762GraphicsScale1Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 3, 7),
    _WtWebGraphAnalog57762GraphicsScale1Max_Type()
)
wtWebGraphAnalog57762GraphicsScale1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762GraphicsScale1Max.setStatus("mandatory")
_WtWebGraphAnalog57762GraphicsScale2Max_Type = Integer32
_WtWebGraphAnalog57762GraphicsScale2Max_Object = MibScalar
wtWebGraphAnalog57762GraphicsScale2Max = _WtWebGraphAnalog57762GraphicsScale2Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 3, 8),
    _WtWebGraphAnalog57762GraphicsScale2Max_Type()
)
wtWebGraphAnalog57762GraphicsScale2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762GraphicsScale2Max.setStatus("mandatory")
_WtWebGraphAnalog57762GraphicsScale1Unit_Type = OctetString
_WtWebGraphAnalog57762GraphicsScale1Unit_Object = MibScalar
wtWebGraphAnalog57762GraphicsScale1Unit = _WtWebGraphAnalog57762GraphicsScale1Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 3, 11),
    _WtWebGraphAnalog57762GraphicsScale1Unit_Type()
)
wtWebGraphAnalog57762GraphicsScale1Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762GraphicsScale1Unit.setStatus("mandatory")
_WtWebGraphAnalog57762GraphicsScale2Unit_Type = OctetString
_WtWebGraphAnalog57762GraphicsScale2Unit_Object = MibScalar
wtWebGraphAnalog57762GraphicsScale2Unit = _WtWebGraphAnalog57762GraphicsScale2Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 3, 12),
    _WtWebGraphAnalog57762GraphicsScale2Unit_Type()
)
wtWebGraphAnalog57762GraphicsScale2Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762GraphicsScale2Unit.setStatus("mandatory")
_WtWebGraphAnalog57762Ports_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57762Ports = _WtWebGraphAnalog57762Ports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 2)
)
_WtWebGraphAnalog57762PortTable_Object = MibTable
wtWebGraphAnalog57762PortTable = _WtWebGraphAnalog57762PortTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 2, 1)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762PortTable.setStatus("mandatory")
_WtWebGraphAnalog57762PortEntry_Object = MibTableRow
wtWebGraphAnalog57762PortEntry = _WtWebGraphAnalog57762PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 2, 1, 1)
)
wtWebGraphAnalog57762PortEntry.setIndexNames(
    (0, "WebGraph-AnalogIO-57762-US-MIB", "wtWebGraphAnalog57762SensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762PortEntry.setStatus("mandatory")
_WtWebGraphAnalog57762PortName_Type = OctetString
_WtWebGraphAnalog57762PortName_Object = MibTableColumn
wtWebGraphAnalog57762PortName = _WtWebGraphAnalog57762PortName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 2, 1, 1, 1),
    _WtWebGraphAnalog57762PortName_Type()
)
wtWebGraphAnalog57762PortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762PortName.setStatus("mandatory")
_WtWebGraphAnalog57762PortText_Type = OctetString
_WtWebGraphAnalog57762PortText_Object = MibTableColumn
wtWebGraphAnalog57762PortText = _WtWebGraphAnalog57762PortText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 2, 1, 1, 2),
    _WtWebGraphAnalog57762PortText_Type()
)
wtWebGraphAnalog57762PortText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762PortText.setStatus("mandatory")
_WtWebGraphAnalog57762PortOffset1_Type = OctetString
_WtWebGraphAnalog57762PortOffset1_Object = MibTableColumn
wtWebGraphAnalog57762PortOffset1 = _WtWebGraphAnalog57762PortOffset1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 2, 1, 1, 3),
    _WtWebGraphAnalog57762PortOffset1_Type()
)
wtWebGraphAnalog57762PortOffset1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762PortOffset1.setStatus("mandatory")
_WtWebGraphAnalog57762SetPoint1_Type = OctetString
_WtWebGraphAnalog57762SetPoint1_Object = MibTableColumn
wtWebGraphAnalog57762SetPoint1 = _WtWebGraphAnalog57762SetPoint1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 2, 1, 1, 4),
    _WtWebGraphAnalog57762SetPoint1_Type()
)
wtWebGraphAnalog57762SetPoint1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762SetPoint1.setStatus("mandatory")
_WtWebGraphAnalog57762PortOffset2_Type = OctetString
_WtWebGraphAnalog57762PortOffset2_Object = MibTableColumn
wtWebGraphAnalog57762PortOffset2 = _WtWebGraphAnalog57762PortOffset2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 2, 1, 1, 5),
    _WtWebGraphAnalog57762PortOffset2_Type()
)
wtWebGraphAnalog57762PortOffset2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762PortOffset2.setStatus("mandatory")
_WtWebGraphAnalog57762SetPoint2_Type = OctetString
_WtWebGraphAnalog57762SetPoint2_Object = MibTableColumn
wtWebGraphAnalog57762SetPoint2 = _WtWebGraphAnalog57762SetPoint2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 2, 1, 1, 6),
    _WtWebGraphAnalog57762SetPoint2_Type()
)
wtWebGraphAnalog57762SetPoint2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762SetPoint2.setStatus("mandatory")
_WtWebGraphAnalog57762PortComment_Type = OctetString
_WtWebGraphAnalog57762PortComment_Object = MibTableColumn
wtWebGraphAnalog57762PortComment = _WtWebGraphAnalog57762PortComment_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 2, 1, 1, 7),
    _WtWebGraphAnalog57762PortComment_Type()
)
wtWebGraphAnalog57762PortComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762PortComment.setStatus("mandatory")


class _WtWebGraphAnalog57762PortSensorSelect_Type(OctetString):
    """Custom type wtWebGraphAnalog57762PortSensorSelect based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphAnalog57762PortSensorSelect_Type.__name__ = "OctetString"
_WtWebGraphAnalog57762PortSensorSelect_Object = MibTableColumn
wtWebGraphAnalog57762PortSensorSelect = _WtWebGraphAnalog57762PortSensorSelect_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 2, 1, 1, 8),
    _WtWebGraphAnalog57762PortSensorSelect_Type()
)
wtWebGraphAnalog57762PortSensorSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762PortSensorSelect.setStatus("mandatory")
_WtWebGraphAnalog57762PortUnit_Type = OctetString
_WtWebGraphAnalog57762PortUnit_Object = MibTableColumn
wtWebGraphAnalog57762PortUnit = _WtWebGraphAnalog57762PortUnit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 2, 1, 1, 9),
    _WtWebGraphAnalog57762PortUnit_Type()
)
wtWebGraphAnalog57762PortUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762PortUnit.setStatus("mandatory")
_WtWebGraphAnalog57762PortScale0_Type = OctetString
_WtWebGraphAnalog57762PortScale0_Object = MibTableColumn
wtWebGraphAnalog57762PortScale0 = _WtWebGraphAnalog57762PortScale0_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 2, 1, 1, 10),
    _WtWebGraphAnalog57762PortScale0_Type()
)
wtWebGraphAnalog57762PortScale0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762PortScale0.setStatus("mandatory")
_WtWebGraphAnalog57762PortScale100_Type = OctetString
_WtWebGraphAnalog57762PortScale100_Object = MibTableColumn
wtWebGraphAnalog57762PortScale100 = _WtWebGraphAnalog57762PortScale100_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 2, 1, 1, 11),
    _WtWebGraphAnalog57762PortScale100_Type()
)
wtWebGraphAnalog57762PortScale100.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762PortScale100.setStatus("mandatory")


class _WtWebGraphAnalog57762PortOutputMode_Type(OctetString):
    """Custom type wtWebGraphAnalog57762PortOutputMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphAnalog57762PortOutputMode_Type.__name__ = "OctetString"
_WtWebGraphAnalog57762PortOutputMode_Object = MibTableColumn
wtWebGraphAnalog57762PortOutputMode = _WtWebGraphAnalog57762PortOutputMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 2, 1, 1, 12),
    _WtWebGraphAnalog57762PortOutputMode_Type()
)
wtWebGraphAnalog57762PortOutputMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762PortOutputMode.setStatus("mandatory")


class _WtWebGraphAnalog57762PortInputMode_Type(OctetString):
    """Custom type wtWebGraphAnalog57762PortInputMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphAnalog57762PortInputMode_Type.__name__ = "OctetString"
_WtWebGraphAnalog57762PortInputMode_Object = MibTableColumn
wtWebGraphAnalog57762PortInputMode = _WtWebGraphAnalog57762PortInputMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 2, 1, 1, 13),
    _WtWebGraphAnalog57762PortInputMode_Type()
)
wtWebGraphAnalog57762PortInputMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762PortInputMode.setStatus("mandatory")
_WtWebGraphAnalog57762PortPresetValue_Type = OctetString
_WtWebGraphAnalog57762PortPresetValue_Object = MibTableColumn
wtWebGraphAnalog57762PortPresetValue = _WtWebGraphAnalog57762PortPresetValue_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 2, 1, 1, 16),
    _WtWebGraphAnalog57762PortPresetValue_Type()
)
wtWebGraphAnalog57762PortPresetValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762PortPresetValue.setStatus("mandatory")
_WtWebGraphAnalog57762Manufact_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57762Manufact = _WtWebGraphAnalog57762Manufact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 3)
)
_WtWebGraphAnalog57762MfName_Type = OctetString
_WtWebGraphAnalog57762MfName_Object = MibScalar
wtWebGraphAnalog57762MfName = _WtWebGraphAnalog57762MfName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 3, 1),
    _WtWebGraphAnalog57762MfName_Type()
)
wtWebGraphAnalog57762MfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762MfName.setStatus("mandatory")
_WtWebGraphAnalog57762MfAddr_Type = OctetString
_WtWebGraphAnalog57762MfAddr_Object = MibScalar
wtWebGraphAnalog57762MfAddr = _WtWebGraphAnalog57762MfAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 3, 2),
    _WtWebGraphAnalog57762MfAddr_Type()
)
wtWebGraphAnalog57762MfAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762MfAddr.setStatus("mandatory")
_WtWebGraphAnalog57762MfHotline_Type = OctetString
_WtWebGraphAnalog57762MfHotline_Object = MibScalar
wtWebGraphAnalog57762MfHotline = _WtWebGraphAnalog57762MfHotline_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 3, 3),
    _WtWebGraphAnalog57762MfHotline_Type()
)
wtWebGraphAnalog57762MfHotline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762MfHotline.setStatus("mandatory")
_WtWebGraphAnalog57762MfInternet_Type = OctetString
_WtWebGraphAnalog57762MfInternet_Object = MibScalar
wtWebGraphAnalog57762MfInternet = _WtWebGraphAnalog57762MfInternet_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 3, 4),
    _WtWebGraphAnalog57762MfInternet_Type()
)
wtWebGraphAnalog57762MfInternet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762MfInternet.setStatus("mandatory")
_WtWebGraphAnalog57762MfDeviceTyp_Type = OctetString
_WtWebGraphAnalog57762MfDeviceTyp_Object = MibScalar
wtWebGraphAnalog57762MfDeviceTyp = _WtWebGraphAnalog57762MfDeviceTyp_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 3, 5),
    _WtWebGraphAnalog57762MfDeviceTyp_Type()
)
wtWebGraphAnalog57762MfDeviceTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762MfDeviceTyp.setStatus("mandatory")
_WtWebGraphAnalog57762MfOrderNo_Type = OctetString
_WtWebGraphAnalog57762MfOrderNo_Object = MibScalar
wtWebGraphAnalog57762MfOrderNo = _WtWebGraphAnalog57762MfOrderNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 3, 6),
    _WtWebGraphAnalog57762MfOrderNo_Type()
)
wtWebGraphAnalog57762MfOrderNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762MfOrderNo.setStatus("mandatory")
_WtWebGraphAnalog57762Diag_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57762Diag = _WtWebGraphAnalog57762Diag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 4)
)
_WtWebGraphAnalog57762DiagErrorCount_Type = Integer32
_WtWebGraphAnalog57762DiagErrorCount_Object = MibScalar
wtWebGraphAnalog57762DiagErrorCount = _WtWebGraphAnalog57762DiagErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 4, 1),
    _WtWebGraphAnalog57762DiagErrorCount_Type()
)
wtWebGraphAnalog57762DiagErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762DiagErrorCount.setStatus("mandatory")
_WtWebGraphAnalog57762DiagBinaryError_Type = OctetString
_WtWebGraphAnalog57762DiagBinaryError_Object = MibScalar
wtWebGraphAnalog57762DiagBinaryError = _WtWebGraphAnalog57762DiagBinaryError_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 4, 2),
    _WtWebGraphAnalog57762DiagBinaryError_Type()
)
wtWebGraphAnalog57762DiagBinaryError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762DiagBinaryError.setStatus("mandatory")
_WtWebGraphAnalog57762DiagErrorIndex_Type = Integer32
_WtWebGraphAnalog57762DiagErrorIndex_Object = MibScalar
wtWebGraphAnalog57762DiagErrorIndex = _WtWebGraphAnalog57762DiagErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 4, 3),
    _WtWebGraphAnalog57762DiagErrorIndex_Type()
)
wtWebGraphAnalog57762DiagErrorIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762DiagErrorIndex.setStatus("mandatory")
_WtWebGraphAnalog57762DiagErrorMessage_Type = OctetString
_WtWebGraphAnalog57762DiagErrorMessage_Object = MibScalar
wtWebGraphAnalog57762DiagErrorMessage = _WtWebGraphAnalog57762DiagErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 4, 4),
    _WtWebGraphAnalog57762DiagErrorMessage_Type()
)
wtWebGraphAnalog57762DiagErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762DiagErrorMessage.setStatus("mandatory")
_WtWebGraphAnalog57762DiagErrorClear_Type = Integer32
_WtWebGraphAnalog57762DiagErrorClear_Object = MibScalar
wtWebGraphAnalog57762DiagErrorClear = _WtWebGraphAnalog57762DiagErrorClear_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 4, 5),
    _WtWebGraphAnalog57762DiagErrorClear_Type()
)
wtWebGraphAnalog57762DiagErrorClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762DiagErrorClear.setStatus("mandatory")

# Managed Objects groups


# Notification objects

wtWebGraphAnalog57762Alert1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 0, 31)
)
wtWebGraphAnalog57762Alert1.setObjects(
    ("WebGraph-AnalogIO-57762-US-MIB", "wtWebGraphAnalog57762AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762Alert1.setStatus(
        ""
    )

wtWebGraphAnalog57762Alert2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 0, 32)
)
wtWebGraphAnalog57762Alert2.setObjects(
    ("WebGraph-AnalogIO-57762-US-MIB", "wtWebGraphAnalog57762AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762Alert2.setStatus(
        ""
    )

wtWebGraphAnalog57762Alert3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 0, 33)
)
wtWebGraphAnalog57762Alert3.setObjects(
    ("WebGraph-AnalogIO-57762-US-MIB", "wtWebGraphAnalog57762AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762Alert3.setStatus(
        ""
    )

wtWebGraphAnalog57762Alert4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 0, 34)
)
wtWebGraphAnalog57762Alert4.setObjects(
    ("WebGraph-AnalogIO-57762-US-MIB", "wtWebGraphAnalog57762AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762Alert4.setStatus(
        ""
    )

wtWebGraphAnalog57762Alert5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 0, 35)
)
wtWebGraphAnalog57762Alert5.setObjects(
    ("WebGraph-AnalogIO-57762-US-MIB", "wtWebGraphAnalog57762AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762Alert5.setStatus(
        ""
    )

wtWebGraphAnalog57762Alert6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 0, 36)
)
wtWebGraphAnalog57762Alert6.setObjects(
    ("WebGraph-AnalogIO-57762-US-MIB", "wtWebGraphAnalog57762AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762Alert6.setStatus(
        ""
    )

wtWebGraphAnalog57762Alert7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 0, 37)
)
wtWebGraphAnalog57762Alert7.setObjects(
    ("WebGraph-AnalogIO-57762-US-MIB", "wtWebGraphAnalog57762AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762Alert7.setStatus(
        ""
    )

wtWebGraphAnalog57762Alert8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 0, 38)
)
wtWebGraphAnalog57762Alert8.setObjects(
    ("WebGraph-AnalogIO-57762-US-MIB", "wtWebGraphAnalog57762AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762Alert8.setStatus(
        ""
    )

wtWebGraphAnalog57762AlertReport = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 0, 39)
)
wtWebGraphAnalog57762AlertReport.setObjects(
    ("WebGraph-AnalogIO-57762-US-MIB", "wtWebGraphAnalog57762AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlertReport.setStatus(
        ""
    )

wtWebGraphAnalog57762Alert9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 0, 91)
)
wtWebGraphAnalog57762Alert9.setObjects(
    ("WebGraph-AnalogIO-57762-US-MIB", "wtWebGraphAnalog57762AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762Alert9.setStatus(
        ""
    )

wtWebGraphAnalog57762Alert10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 0, 92)
)
wtWebGraphAnalog57762Alert10.setObjects(
    ("WebGraph-AnalogIO-57762-US-MIB", "wtWebGraphAnalog57762AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762Alert10.setStatus(
        ""
    )

wtWebGraphAnalog57762Alert11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 0, 93)
)
wtWebGraphAnalog57762Alert11.setObjects(
    ("WebGraph-AnalogIO-57762-US-MIB", "wtWebGraphAnalog57762AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762Alert11.setStatus(
        ""
    )

wtWebGraphAnalog57762Alert12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 0, 94)
)
wtWebGraphAnalog57762Alert12.setObjects(
    ("WebGraph-AnalogIO-57762-US-MIB", "wtWebGraphAnalog57762AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762Alert12.setStatus(
        ""
    )

wtWebGraphAnalog57762Alert13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 0, 95)
)
wtWebGraphAnalog57762Alert13.setObjects(
    ("WebGraph-AnalogIO-57762-US-MIB", "wtWebGraphAnalog57762AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762Alert13.setStatus(
        ""
    )

wtWebGraphAnalog57762Alert14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 0, 96)
)
wtWebGraphAnalog57762Alert14.setObjects(
    ("WebGraph-AnalogIO-57762-US-MIB", "wtWebGraphAnalog57762AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762Alert14.setStatus(
        ""
    )

wtWebGraphAnalog57762Alert15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 0, 97)
)
wtWebGraphAnalog57762Alert15.setObjects(
    ("WebGraph-AnalogIO-57762-US-MIB", "wtWebGraphAnalog57762AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762Alert15.setStatus(
        ""
    )

wtWebGraphAnalog57762Alert16 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 0, 98)
)
wtWebGraphAnalog57762Alert16.setObjects(
    ("WebGraph-AnalogIO-57762-US-MIB", "wtWebGraphAnalog57762AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762Alert16.setStatus(
        ""
    )

wtWebGraphAnalog57762AlertDiag = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 0, 110)
)
wtWebGraphAnalog57762AlertDiag.setObjects(
      *(("WebGraph-AnalogIO-57762-US-MIB", "wtWebGraphAnalog57762DiagErrorIndex"),
        ("WebGraph-AnalogIO-57762-US-MIB", "wtWebGraphAnalog57762DiagErrorMessage"))
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57762AlertDiag.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WebGraph-AnalogIO-57762-US-MIB",
    **{"wut": wut,
       "wtComServer": wtComServer,
       "wtWebio": wtWebio,
       "wtWebGraphAnalog57762": wtWebGraphAnalog57762,
       "wtWebGraphAnalog57762Alert1": wtWebGraphAnalog57762Alert1,
       "wtWebGraphAnalog57762Alert2": wtWebGraphAnalog57762Alert2,
       "wtWebGraphAnalog57762Alert3": wtWebGraphAnalog57762Alert3,
       "wtWebGraphAnalog57762Alert4": wtWebGraphAnalog57762Alert4,
       "wtWebGraphAnalog57762Alert5": wtWebGraphAnalog57762Alert5,
       "wtWebGraphAnalog57762Alert6": wtWebGraphAnalog57762Alert6,
       "wtWebGraphAnalog57762Alert7": wtWebGraphAnalog57762Alert7,
       "wtWebGraphAnalog57762Alert8": wtWebGraphAnalog57762Alert8,
       "wtWebGraphAnalog57762AlertReport": wtWebGraphAnalog57762AlertReport,
       "wtWebGraphAnalog57762Alert9": wtWebGraphAnalog57762Alert9,
       "wtWebGraphAnalog57762Alert10": wtWebGraphAnalog57762Alert10,
       "wtWebGraphAnalog57762Alert11": wtWebGraphAnalog57762Alert11,
       "wtWebGraphAnalog57762Alert12": wtWebGraphAnalog57762Alert12,
       "wtWebGraphAnalog57762Alert13": wtWebGraphAnalog57762Alert13,
       "wtWebGraphAnalog57762Alert14": wtWebGraphAnalog57762Alert14,
       "wtWebGraphAnalog57762Alert15": wtWebGraphAnalog57762Alert15,
       "wtWebGraphAnalog57762Alert16": wtWebGraphAnalog57762Alert16,
       "wtWebGraphAnalog57762AlertDiag": wtWebGraphAnalog57762AlertDiag,
       "wtWebGraphAnalog57762Inventory": wtWebGraphAnalog57762Inventory,
       "wtWebGraphAnalog57762Sensors": wtWebGraphAnalog57762Sensors,
       "wtWebGraphAnalog57762SensorTable": wtWebGraphAnalog57762SensorTable,
       "wtWebGraphAnalog57762SensorEntry": wtWebGraphAnalog57762SensorEntry,
       "wtWebGraphAnalog57762SensorNo": wtWebGraphAnalog57762SensorNo,
       "wtWebGraphAnalog57762ValuesTable": wtWebGraphAnalog57762ValuesTable,
       "wtWebGraphAnalog57762ValuesEntry": wtWebGraphAnalog57762ValuesEntry,
       "wtWebGraphAnalog57762Values": wtWebGraphAnalog57762Values,
       "wtWebGraphAnalog57762BinaryValuesTable": wtWebGraphAnalog57762BinaryValuesTable,
       "wtWebGraphAnalog57762BinaryValuesEntry": wtWebGraphAnalog57762BinaryValuesEntry,
       "wtWebGraphAnalog57762BinaryValues": wtWebGraphAnalog57762BinaryValues,
       "wtWebGraphAnalog57762ValuesPointTable": wtWebGraphAnalog57762ValuesPointTable,
       "wtWebGraphAnalog57762ValuesPointEntry": wtWebGraphAnalog57762ValuesPointEntry,
       "wtWebGraphAnalog57762ValuesPoint": wtWebGraphAnalog57762ValuesPoint,
       "wtWebGraphAnalog57762SessCntrl": wtWebGraphAnalog57762SessCntrl,
       "wtWebGraphAnalog57762SessCntrlPassword": wtWebGraphAnalog57762SessCntrlPassword,
       "wtWebGraphAnalog57762SessCntrlConfigMode": wtWebGraphAnalog57762SessCntrlConfigMode,
       "wtWebGraphAnalog57762SessCntrlLogout": wtWebGraphAnalog57762SessCntrlLogout,
       "wtWebGraphAnalog57762SessCntrlAdminPassword": wtWebGraphAnalog57762SessCntrlAdminPassword,
       "wtWebGraphAnalog57762SessCntrlConfigPassword": wtWebGraphAnalog57762SessCntrlConfigPassword,
       "wtWebGraphAnalog57762Config": wtWebGraphAnalog57762Config,
       "wtWebGraphAnalog57762Device": wtWebGraphAnalog57762Device,
       "wtWebGraphAnalog57762Text": wtWebGraphAnalog57762Text,
       "wtWebGraphAnalog57762DeviceName": wtWebGraphAnalog57762DeviceName,
       "wtWebGraphAnalog57762DeviceText": wtWebGraphAnalog57762DeviceText,
       "wtWebGraphAnalog57762DeviceLocation": wtWebGraphAnalog57762DeviceLocation,
       "wtWebGraphAnalog57762DeviceContact": wtWebGraphAnalog57762DeviceContact,
       "wtWebGraphAnalog57762TimeDate": wtWebGraphAnalog57762TimeDate,
       "wtWebGraphAnalog57762TimeZone": wtWebGraphAnalog57762TimeZone,
       "wtWebGraphAnalog57762TzOffsetHrs": wtWebGraphAnalog57762TzOffsetHrs,
       "wtWebGraphAnalog57762TzOffsetMin": wtWebGraphAnalog57762TzOffsetMin,
       "wtWebGraphAnalog57762TzEnable": wtWebGraphAnalog57762TzEnable,
       "wtWebGraphAnalog57762StTzOffsetHrs": wtWebGraphAnalog57762StTzOffsetHrs,
       "wtWebGraphAnalog57762StTzOffsetMin": wtWebGraphAnalog57762StTzOffsetMin,
       "wtWebGraphAnalog57762StTzEnable": wtWebGraphAnalog57762StTzEnable,
       "wtWebGraphAnalog57762StTzStartMonth": wtWebGraphAnalog57762StTzStartMonth,
       "wtWebGraphAnalog57762StTzStartMode": wtWebGraphAnalog57762StTzStartMode,
       "wtWebGraphAnalog57762StTzStartWday": wtWebGraphAnalog57762StTzStartWday,
       "wtWebGraphAnalog57762StTzStartHrs": wtWebGraphAnalog57762StTzStartHrs,
       "wtWebGraphAnalog57762StTzStartMin": wtWebGraphAnalog57762StTzStartMin,
       "wtWebGraphAnalog57762StTzStopMonth": wtWebGraphAnalog57762StTzStopMonth,
       "wtWebGraphAnalog57762StTzStopMode": wtWebGraphAnalog57762StTzStopMode,
       "wtWebGraphAnalog57762StTzStopWday": wtWebGraphAnalog57762StTzStopWday,
       "wtWebGraphAnalog57762StTzStopHrs": wtWebGraphAnalog57762StTzStopHrs,
       "wtWebGraphAnalog57762StTzStopMin": wtWebGraphAnalog57762StTzStopMin,
       "wtWebGraphAnalog57762TimeServer": wtWebGraphAnalog57762TimeServer,
       "wtWebGraphAnalog57762TimeServer1": wtWebGraphAnalog57762TimeServer1,
       "wtWebGraphAnalog57762TimeServer2": wtWebGraphAnalog57762TimeServer2,
       "wtWebGraphAnalog57762TsEnable": wtWebGraphAnalog57762TsEnable,
       "wtWebGraphAnalog57762TsSyncTime": wtWebGraphAnalog57762TsSyncTime,
       "wtWebGraphAnalog57762DeviceClock": wtWebGraphAnalog57762DeviceClock,
       "wtWebGraphAnalog57762ClockHrs": wtWebGraphAnalog57762ClockHrs,
       "wtWebGraphAnalog57762ClockMin": wtWebGraphAnalog57762ClockMin,
       "wtWebGraphAnalog57762ClockDay": wtWebGraphAnalog57762ClockDay,
       "wtWebGraphAnalog57762ClockMonth": wtWebGraphAnalog57762ClockMonth,
       "wtWebGraphAnalog57762ClockYear": wtWebGraphAnalog57762ClockYear,
       "wtWebGraphAnalog57762Basic": wtWebGraphAnalog57762Basic,
       "wtWebGraphAnalog57762Network": wtWebGraphAnalog57762Network,
       "wtWebGraphAnalog57762IpAddress": wtWebGraphAnalog57762IpAddress,
       "wtWebGraphAnalog57762SubnetMask": wtWebGraphAnalog57762SubnetMask,
       "wtWebGraphAnalog57762Gateway": wtWebGraphAnalog57762Gateway,
       "wtWebGraphAnalog57762DnsServer1": wtWebGraphAnalog57762DnsServer1,
       "wtWebGraphAnalog57762DnsServer2": wtWebGraphAnalog57762DnsServer2,
       "wtWebGraphAnalog57762AddConfig": wtWebGraphAnalog57762AddConfig,
       "wtWebGraphAnalog57762HTTP": wtWebGraphAnalog57762HTTP,
       "wtWebGraphAnalog57762Startup": wtWebGraphAnalog57762Startup,
       "wtWebGraphAnalog57762GetHeaderEnable": wtWebGraphAnalog57762GetHeaderEnable,
       "wtWebGraphAnalog57762HttpPort": wtWebGraphAnalog57762HttpPort,
       "wtWebGraphAnalog57762Mail": wtWebGraphAnalog57762Mail,
       "wtWebGraphAnalog57762MailAdName": wtWebGraphAnalog57762MailAdName,
       "wtWebGraphAnalog57762MailReply": wtWebGraphAnalog57762MailReply,
       "wtWebGraphAnalog57762MailServer": wtWebGraphAnalog57762MailServer,
       "wtWebioAn1MailEnable": wtWebioAn1MailEnable,
       "wtWebGraphAnalog57762MailAuthentication": wtWebGraphAnalog57762MailAuthentication,
       "wtWebGraphAnalog57762MailAuthUser": wtWebGraphAnalog57762MailAuthUser,
       "wtWebGraphAnalog57762MailAuthPassword": wtWebGraphAnalog57762MailAuthPassword,
       "wtWebGraphAnalog57762MailPop3Server": wtWebGraphAnalog57762MailPop3Server,
       "wtWebGraphAnalog57762SNMP": wtWebGraphAnalog57762SNMP,
       "wtWebGraphAnalog57762SnmpCommunityStringRead": wtWebGraphAnalog57762SnmpCommunityStringRead,
       "wtWebGraphAnalog57762SnmpCommunityStringReadWrite": wtWebGraphAnalog57762SnmpCommunityStringReadWrite,
       "wtWebGraphAnalog57762SystemTrapManagerIP": wtWebGraphAnalog57762SystemTrapManagerIP,
       "wtWebGraphAnalog57762SystemTrapEnable": wtWebGraphAnalog57762SystemTrapEnable,
       "wtWebGraphAnalog57762SnmpEnable": wtWebGraphAnalog57762SnmpEnable,
       "wtWebGraphAnalog57762SnmpCommunityStringTrap": wtWebGraphAnalog57762SnmpCommunityStringTrap,
       "wtWebGraphAnalog57762SnmpSystemTrapManagerPort": wtWebGraphAnalog57762SnmpSystemTrapManagerPort,
       "wtWebGraphAnalog57762UDP": wtWebGraphAnalog57762UDP,
       "wtWebGraphAnalog57762UdpPort": wtWebGraphAnalog57762UdpPort,
       "wtWebGraphAnalog57762UdpEnable": wtWebGraphAnalog57762UdpEnable,
       "wtWebGraphAnalog57762Syslog": wtWebGraphAnalog57762Syslog,
       "wtWebGraphAnalog57762SyslogServerIP": wtWebGraphAnalog57762SyslogServerIP,
       "wtWebGraphAnalog57762SyslogServerPort": wtWebGraphAnalog57762SyslogServerPort,
       "wtWebGraphAnalog57762SyslogSystemMessagesEnable": wtWebGraphAnalog57762SyslogSystemMessagesEnable,
       "wtWebGraphAnalog57762SyslogEnable": wtWebGraphAnalog57762SyslogEnable,
       "wtWebGraphAnalog57762FTP": wtWebGraphAnalog57762FTP,
       "wtWebGraphAnalog57762FTPServerIP": wtWebGraphAnalog57762FTPServerIP,
       "wtWebGraphAnalog57762FTPServerControlPort": wtWebGraphAnalog57762FTPServerControlPort,
       "wtWebGraphAnalog57762FTPUserName": wtWebGraphAnalog57762FTPUserName,
       "wtWebGraphAnalog57762FTPPassword": wtWebGraphAnalog57762FTPPassword,
       "wtWebGraphAnalog57762FTPAccount": wtWebGraphAnalog57762FTPAccount,
       "wtWebGraphAnalog57762FTPOption": wtWebGraphAnalog57762FTPOption,
       "wtWebGraphAnalog57762FTPEnable": wtWebGraphAnalog57762FTPEnable,
       "wtWebGraphAnalog57762Language": wtWebGraphAnalog57762Language,
       "wtWebGraphAnalog57762LanguageSelect": wtWebGraphAnalog57762LanguageSelect,
       "wtWebGraphAnalog57762Binary": wtWebGraphAnalog57762Binary,
       "wtWebGraphAnalog57762BinaryModeCount": wtWebGraphAnalog57762BinaryModeCount,
       "wtWebGraphAnalog57762BinaryIfTable": wtWebGraphAnalog57762BinaryIfTable,
       "wtWebGraphAnalog57762BinaryIfEntry": wtWebGraphAnalog57762BinaryIfEntry,
       "wtWebGraphAnalog57762BinaryModeNo": wtWebGraphAnalog57762BinaryModeNo,
       "wtWebGraphAnalog57762BinaryTable": wtWebGraphAnalog57762BinaryTable,
       "wtWebGraphAnalog57762BinaryEntry": wtWebGraphAnalog57762BinaryEntry,
       "wtWebGraphAnalog57762BinaryOperationMode": wtWebGraphAnalog57762BinaryOperationMode,
       "wtWebGraphAnalog57762BinaryTcpServerLocalPort": wtWebGraphAnalog57762BinaryTcpServerLocalPort,
       "wtWebGraphAnalog57762BinaryTcpServerInputTrigger": wtWebGraphAnalog57762BinaryTcpServerInputTrigger,
       "wtWebGraphAnalog57762BinaryTcpServerApplicationMode": wtWebGraphAnalog57762BinaryTcpServerApplicationMode,
       "wtWebGraphAnalog57762BinaryTcpClientLocalPort": wtWebGraphAnalog57762BinaryTcpClientLocalPort,
       "wtWebGraphAnalog57762BinaryTcpClientServerPort": wtWebGraphAnalog57762BinaryTcpClientServerPort,
       "wtWebGraphAnalog57762BinaryTcpClientServerIpAddr": wtWebGraphAnalog57762BinaryTcpClientServerIpAddr,
       "wtWebGraphAnalog57762BinaryTcpClientServerPassword": wtWebGraphAnalog57762BinaryTcpClientServerPassword,
       "wtWebGraphAnalog57762BinaryTcpClientInactivity": wtWebGraphAnalog57762BinaryTcpClientInactivity,
       "wtWebGraphAnalog57762BinaryTcpClientInputTrigger": wtWebGraphAnalog57762BinaryTcpClientInputTrigger,
       "wtWebGraphAnalog57762BinaryTcpClientInterval": wtWebGraphAnalog57762BinaryTcpClientInterval,
       "wtWebGraphAnalog57762BinaryTcpClientApplicationMode": wtWebGraphAnalog57762BinaryTcpClientApplicationMode,
       "wtWebGraphAnalog57762BinaryUdpPeerLocalPort": wtWebGraphAnalog57762BinaryUdpPeerLocalPort,
       "wtWebGraphAnalog57762BinaryUdpPeerRemotePort": wtWebGraphAnalog57762BinaryUdpPeerRemotePort,
       "wtWebGraphAnalog57762BinaryUdpPeerRemoteIpAddr": wtWebGraphAnalog57762BinaryUdpPeerRemoteIpAddr,
       "wtWebGraphAnalog57762BinaryUdpPeerInputTrigger": wtWebGraphAnalog57762BinaryUdpPeerInputTrigger,
       "wtWebGraphAnalog57762BinaryUdpPeerInterval": wtWebGraphAnalog57762BinaryUdpPeerInterval,
       "wtWebGraphAnalog57762BinaryUdpPeerApplicationMode": wtWebGraphAnalog57762BinaryUdpPeerApplicationMode,
       "wtWebGraphAnalog57762BinaryConnectedPort": wtWebGraphAnalog57762BinaryConnectedPort,
       "wtWebGraphAnalog57762BinaryConnectedIpAddr": wtWebGraphAnalog57762BinaryConnectedIpAddr,
       "wtWebGraphAnalog57762BinaryTcpServerClientHttpPort": wtWebGraphAnalog57762BinaryTcpServerClientHttpPort,
       "wtWebGraphAnalog57762BinaryTcpClientServerHttpPort": wtWebGraphAnalog57762BinaryTcpClientServerHttpPort,
       "wtWebGraphAnalog57762BinaryTcpServerHysteresis1": wtWebGraphAnalog57762BinaryTcpServerHysteresis1,
       "wtWebGraphAnalog57762BinaryTcpServerHysteresis2": wtWebGraphAnalog57762BinaryTcpServerHysteresis2,
       "wtWebGraphAnalog57762BinaryTcpClientHysteresis1": wtWebGraphAnalog57762BinaryTcpClientHysteresis1,
       "wtWebGraphAnalog57762BinaryTcpClientHysteresis2": wtWebGraphAnalog57762BinaryTcpClientHysteresis2,
       "wtWebGraphAnalog57762BinaryUdpPeerHysteresis1": wtWebGraphAnalog57762BinaryUdpPeerHysteresis1,
       "wtWebGraphAnalog57762BinaryUdpPeerHysteresis2": wtWebGraphAnalog57762BinaryUdpPeerHysteresis2,
       "wtWebGraphAnalog57762BinaryTcpClientServerUserName": wtWebGraphAnalog57762BinaryTcpClientServerUserName,
       "wtWebGraphAnalog57762MQTT": wtWebGraphAnalog57762MQTT,
       "wtWebGraphAnalog57762MQTTEnable": wtWebGraphAnalog57762MQTTEnable,
       "wtWebGraphAnalog57762MQTTBrockerIP": wtWebGraphAnalog57762MQTTBrockerIP,
       "wtWebGraphAnalog57762MQTTUserName": wtWebGraphAnalog57762MQTTUserName,
       "wtWebGraphAnalog57762MQTTPassword": wtWebGraphAnalog57762MQTTPassword,
       "wtWebGraphAnalog57762MQTTLocalPort": wtWebGraphAnalog57762MQTTLocalPort,
       "wtWebGraphAnalog57762MQTTBrokerServerPort": wtWebGraphAnalog57762MQTTBrokerServerPort,
       "wtWebGraphAnalog57762MQTTInterval": wtWebGraphAnalog57762MQTTInterval,
       "wtWebGraphAnalog57762MQTTLastWillEnable": wtWebGraphAnalog57762MQTTLastWillEnable,
       "wtWebGraphAnalog57762MQTTLastWillTopic": wtWebGraphAnalog57762MQTTLastWillTopic,
       "wtWebGraphAnalog57762MQTTLastWillMsg": wtWebGraphAnalog57762MQTTLastWillMsg,
       "wtWebGraphAnalog57762MQTTLastWillQoS": wtWebGraphAnalog57762MQTTLastWillQoS,
       "wtWebGraphAnalog57762MQTTLastWillRetain": wtWebGraphAnalog57762MQTTLastWillRetain,
       "wtWebGraphAnalog57762MQTTLastWillConnectEnable": wtWebGraphAnalog57762MQTTLastWillConnectEnable,
       "wtWebGraphAnalog57762MQTTLastWillConnectMsg": wtWebGraphAnalog57762MQTTLastWillConnectMsg,
       "wtWebGraphAnalog57762REST": wtWebGraphAnalog57762REST,
       "wtWebGraphAnalog57762RESTEnable": wtWebGraphAnalog57762RESTEnable,
       "wtWebGraphAnalog57762RESTDigestAuthEnable": wtWebGraphAnalog57762RESTDigestAuthEnable,
       "wtWebGraphAnalog57762Datalogger": wtWebGraphAnalog57762Datalogger,
       "wtWebGraphAnalog57762LoggerTimebase": wtWebGraphAnalog57762LoggerTimebase,
       "wtWebGraphAnalog57762LoggerSensorSel": wtWebGraphAnalog57762LoggerSensorSel,
       "wtWebGraphAnalog57762Alarm": wtWebGraphAnalog57762Alarm,
       "wtWebGraphAnalog57762AlarmCount": wtWebGraphAnalog57762AlarmCount,
       "wtWebGraphAnalog57762AlarmIfTable": wtWebGraphAnalog57762AlarmIfTable,
       "wtWebGraphAnalog57762AlarmIfEntry": wtWebGraphAnalog57762AlarmIfEntry,
       "wtWebGraphAnalog57762AlarmNo": wtWebGraphAnalog57762AlarmNo,
       "wtWebGraphAnalog57762AlarmTable": wtWebGraphAnalog57762AlarmTable,
       "wtWebGraphAnalog57762AlarmEntry": wtWebGraphAnalog57762AlarmEntry,
       "wtWebGraphAnalog57762AlarmTrigger": wtWebGraphAnalog57762AlarmTrigger,
       "wtWebGraphAnalog57762AlarmMin1": wtWebGraphAnalog57762AlarmMin1,
       "wtWebGraphAnalog57762AlarmMax1": wtWebGraphAnalog57762AlarmMax1,
       "wtWebGraphAnalog57762AlarmHysteresis1": wtWebGraphAnalog57762AlarmHysteresis1,
       "wtWebGraphAnalog57762AlarmDelay": wtWebGraphAnalog57762AlarmDelay,
       "wtWebGraphAnalog57762AlarmInterval": wtWebGraphAnalog57762AlarmInterval,
       "wtWebGraphAnalog57762AlarmEnable": wtWebGraphAnalog57762AlarmEnable,
       "wtWebGraphAnalog57762AlarmEMailAddr": wtWebGraphAnalog57762AlarmEMailAddr,
       "wtWebGraphAnalog57762AlarmMailSubject": wtWebGraphAnalog57762AlarmMailSubject,
       "wtWebGraphAnalog57762AlarmMailText": wtWebGraphAnalog57762AlarmMailText,
       "wtWebGraphAnalog57762AlarmManagerIP": wtWebGraphAnalog57762AlarmManagerIP,
       "wtWebGraphAnalog57762AlarmTrapText": wtWebGraphAnalog57762AlarmTrapText,
       "wtWebGraphAnalog57762AlarmMailOptions": wtWebGraphAnalog57762AlarmMailOptions,
       "wtWebGraphAnalog57762AlarmTcpIpAddr": wtWebGraphAnalog57762AlarmTcpIpAddr,
       "wtWebGraphAnalog57762AlarmTcpPort": wtWebGraphAnalog57762AlarmTcpPort,
       "wtWebGraphAnalog57762AlarmTcpText": wtWebGraphAnalog57762AlarmTcpText,
       "wtWebGraphAnalog57762AlarmClearMailSubject": wtWebGraphAnalog57762AlarmClearMailSubject,
       "wtWebGraphAnalog57762AlarmClearMailText": wtWebGraphAnalog57762AlarmClearMailText,
       "wtWebGraphAnalog57762AlarmClearTrapText": wtWebGraphAnalog57762AlarmClearTrapText,
       "wtWebGraphAnalog57762AlarmClearTcpText": wtWebGraphAnalog57762AlarmClearTcpText,
       "wtWebGraphAnalog57762AlarmMin2": wtWebGraphAnalog57762AlarmMin2,
       "wtWebGraphAnalog57762AlarmMax2": wtWebGraphAnalog57762AlarmMax2,
       "wtWebGraphAnalog57762AlarmHysteresis2": wtWebGraphAnalog57762AlarmHysteresis2,
       "wtWebGraphAnalog57762AlarmSyslogIpAddr": wtWebGraphAnalog57762AlarmSyslogIpAddr,
       "wtWebGraphAnalog57762AlarmSyslogPort": wtWebGraphAnalog57762AlarmSyslogPort,
       "wtWebGraphAnalog57762AlarmSyslogText": wtWebGraphAnalog57762AlarmSyslogText,
       "wtWebGraphAnalog57762AlarmSyslogClearText": wtWebGraphAnalog57762AlarmSyslogClearText,
       "wtWebGraphAnalog57762AlarmFtpDataPort": wtWebGraphAnalog57762AlarmFtpDataPort,
       "wtWebGraphAnalog57762AlarmFtpFileName": wtWebGraphAnalog57762AlarmFtpFileName,
       "wtWebGraphAnalog57762AlarmFtpText": wtWebGraphAnalog57762AlarmFtpText,
       "wtWebGraphAnalog57762AlarmFtpClearText": wtWebGraphAnalog57762AlarmFtpClearText,
       "wtWebGraphAnalog57762AlarmFtpOption": wtWebGraphAnalog57762AlarmFtpOption,
       "wtWebGraphAnalog57762AlarmTimerCron": wtWebGraphAnalog57762AlarmTimerCron,
       "wtWebGraphAnalog57762AlarmName": wtWebGraphAnalog57762AlarmName,
       "wtWebGraphAnalog57762AlarmActive": wtWebGraphAnalog57762AlarmActive,
       "wtWebGraphAnalog57762AlarmHttpReqAuthEnable": wtWebGraphAnalog57762AlarmHttpReqAuthEnable,
       "wtWebGraphAnalog57762AlarmHttpReqAuthUser": wtWebGraphAnalog57762AlarmHttpReqAuthUser,
       "wtWebGraphAnalog57762AlarmHttpReqAuthPassword": wtWebGraphAnalog57762AlarmHttpReqAuthPassword,
       "wtWebGraphAnalog57762AlarmHttpReqSetUrl": wtWebGraphAnalog57762AlarmHttpReqSetUrl,
       "wtWebGraphAnalog57762AlarmHttpReqClearUrl": wtWebGraphAnalog57762AlarmHttpReqClearUrl,
       "wtWebGraphAnalog57762AlarmHttpReqServerPort": wtWebGraphAnalog57762AlarmHttpReqServerPort,
       "wtWebGraphAnalog57762AlarmMqttTopicPath": wtWebGraphAnalog57762AlarmMqttTopicPath,
       "wtWebGraphAnalog57762AlarmMqttTopicSetTopic": wtWebGraphAnalog57762AlarmMqttTopicSetTopic,
       "wtWebGraphAnalog57762AlarmMqttTopicClear": wtWebGraphAnalog57762AlarmMqttTopicClear,
       "wtWebGraphAnalog57762AlarmSensorLostSelection": wtWebGraphAnalog57762AlarmSensorLostSelection,
       "wtWebGraphAnalog57762AlarmLimitWindow": wtWebGraphAnalog57762AlarmLimitWindow,
       "wtWebGraphAnalog57762AlarmSnmpManagerPort": wtWebGraphAnalog57762AlarmSnmpManagerPort,
       "wtWebGraphAnalog57762AlarmMqttQoS": wtWebGraphAnalog57762AlarmMqttQoS,
       "wtWebGraphAnalog57762AlarmMqttRetain": wtWebGraphAnalog57762AlarmMqttRetain,
       "wtWebGraphAnalog57762Graphics": wtWebGraphAnalog57762Graphics,
       "wtWebGraphAnalog57762GraphicsBase": wtWebGraphAnalog57762GraphicsBase,
       "wtWebGraphAnalog57762GraphicsBaseEnable": wtWebGraphAnalog57762GraphicsBaseEnable,
       "wtWebGraphAnalog57762GraphicsBaseWidth": wtWebGraphAnalog57762GraphicsBaseWidth,
       "wtWebGraphAnalog57762GraphicsBaseHeight": wtWebGraphAnalog57762GraphicsBaseHeight,
       "wtWebGraphAnalog57762GraphicsBaseFrameColor": wtWebGraphAnalog57762GraphicsBaseFrameColor,
       "wtWebGraphAnalog57762GraphicsBaseBackgroundColor": wtWebGraphAnalog57762GraphicsBaseBackgroundColor,
       "wtWebGraphAnalog57762GraphicsBasePollingrate": wtWebGraphAnalog57762GraphicsBasePollingrate,
       "wtWebGraphAnalog57762GraphicsSelect": wtWebGraphAnalog57762GraphicsSelect,
       "wtWebGraphAnalog57762GraphicsSelectDisplaySensorSel": wtWebGraphAnalog57762GraphicsSelectDisplaySensorSel,
       "wtWebGraphAnalog57762GraphicsSelectDisplayShowExtrem": wtWebGraphAnalog57762GraphicsSelectDisplayShowExtrem,
       "wtWebGraphAnalog57762SensorColor2Table": wtWebGraphAnalog57762SensorColor2Table,
       "wtWebGraphAnalog57762SensorColor2Entry": wtWebGraphAnalog57762SensorColor2Entry,
       "wtWebGraphAnalog57762GraphicsSensorColor": wtWebGraphAnalog57762GraphicsSensorColor,
       "wtWebGraphAnalog57762GraphicsSelectScale": wtWebGraphAnalog57762GraphicsSelectScale,
       "wtWebGraphAnalog57762GraphicsScale": wtWebGraphAnalog57762GraphicsScale,
       "wtWebGraphAnalog57762GraphicsScaleAutoScaleEnable": wtWebGraphAnalog57762GraphicsScaleAutoScaleEnable,
       "wtWebGraphAnalog57762GraphicsScaleAutoFitEnable": wtWebGraphAnalog57762GraphicsScaleAutoFitEnable,
       "wtWebGraphAnalog57762GraphicsScale1Min": wtWebGraphAnalog57762GraphicsScale1Min,
       "wtWebGraphAnalog57762GraphicsScale2Min": wtWebGraphAnalog57762GraphicsScale2Min,
       "wtWebGraphAnalog57762GraphicsScale1Max": wtWebGraphAnalog57762GraphicsScale1Max,
       "wtWebGraphAnalog57762GraphicsScale2Max": wtWebGraphAnalog57762GraphicsScale2Max,
       "wtWebGraphAnalog57762GraphicsScale1Unit": wtWebGraphAnalog57762GraphicsScale1Unit,
       "wtWebGraphAnalog57762GraphicsScale2Unit": wtWebGraphAnalog57762GraphicsScale2Unit,
       "wtWebGraphAnalog57762Ports": wtWebGraphAnalog57762Ports,
       "wtWebGraphAnalog57762PortTable": wtWebGraphAnalog57762PortTable,
       "wtWebGraphAnalog57762PortEntry": wtWebGraphAnalog57762PortEntry,
       "wtWebGraphAnalog57762PortName": wtWebGraphAnalog57762PortName,
       "wtWebGraphAnalog57762PortText": wtWebGraphAnalog57762PortText,
       "wtWebGraphAnalog57762PortOffset1": wtWebGraphAnalog57762PortOffset1,
       "wtWebGraphAnalog57762SetPoint1": wtWebGraphAnalog57762SetPoint1,
       "wtWebGraphAnalog57762PortOffset2": wtWebGraphAnalog57762PortOffset2,
       "wtWebGraphAnalog57762SetPoint2": wtWebGraphAnalog57762SetPoint2,
       "wtWebGraphAnalog57762PortComment": wtWebGraphAnalog57762PortComment,
       "wtWebGraphAnalog57762PortSensorSelect": wtWebGraphAnalog57762PortSensorSelect,
       "wtWebGraphAnalog57762PortUnit": wtWebGraphAnalog57762PortUnit,
       "wtWebGraphAnalog57762PortScale0": wtWebGraphAnalog57762PortScale0,
       "wtWebGraphAnalog57762PortScale100": wtWebGraphAnalog57762PortScale100,
       "wtWebGraphAnalog57762PortOutputMode": wtWebGraphAnalog57762PortOutputMode,
       "wtWebGraphAnalog57762PortInputMode": wtWebGraphAnalog57762PortInputMode,
       "wtWebGraphAnalog57762PortPresetValue": wtWebGraphAnalog57762PortPresetValue,
       "wtWebGraphAnalog57762Manufact": wtWebGraphAnalog57762Manufact,
       "wtWebGraphAnalog57762MfName": wtWebGraphAnalog57762MfName,
       "wtWebGraphAnalog57762MfAddr": wtWebGraphAnalog57762MfAddr,
       "wtWebGraphAnalog57762MfHotline": wtWebGraphAnalog57762MfHotline,
       "wtWebGraphAnalog57762MfInternet": wtWebGraphAnalog57762MfInternet,
       "wtWebGraphAnalog57762MfDeviceTyp": wtWebGraphAnalog57762MfDeviceTyp,
       "wtWebGraphAnalog57762MfOrderNo": wtWebGraphAnalog57762MfOrderNo,
       "wtWebGraphAnalog57762Diag": wtWebGraphAnalog57762Diag,
       "wtWebGraphAnalog57762DiagErrorCount": wtWebGraphAnalog57762DiagErrorCount,
       "wtWebGraphAnalog57762DiagBinaryError": wtWebGraphAnalog57762DiagBinaryError,
       "wtWebGraphAnalog57762DiagErrorIndex": wtWebGraphAnalog57762DiagErrorIndex,
       "wtWebGraphAnalog57762DiagErrorMessage": wtWebGraphAnalog57762DiagErrorMessage,
       "wtWebGraphAnalog57762DiagErrorClear": wtWebGraphAnalog57762DiagErrorClear}
)
