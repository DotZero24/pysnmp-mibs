# SNMP MIB module (WebGraph-AnalogIn-57642-US-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/webgraph/WebGraph-AnalogIn-57642-US-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:17:06 2025
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
_WtWebGraphAnalogIn57642_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57642 = _WtWebGraphAnalogIn57642_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11)
)
_WtWebGraphAnalogIn57642Inventory_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57642Inventory = _WtWebGraphAnalogIn57642Inventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 1)
)


class _WtWebGraphAnalogIn57642Sensors_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57642Sensors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WtWebGraphAnalogIn57642Sensors_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57642Sensors_Object = MibScalar
wtWebGraphAnalogIn57642Sensors = _WtWebGraphAnalogIn57642Sensors_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 1, 1),
    _WtWebGraphAnalogIn57642Sensors_Type()
)
wtWebGraphAnalogIn57642Sensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642Sensors.setStatus("mandatory")
_WtWebGraphAnalogIn57642SensorTable_Object = MibTable
wtWebGraphAnalogIn57642SensorTable = _WtWebGraphAnalogIn57642SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 1, 2)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642SensorTable.setStatus("mandatory")
_WtWebGraphAnalogIn57642SensorEntry_Object = MibTableRow
wtWebGraphAnalogIn57642SensorEntry = _WtWebGraphAnalogIn57642SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 1, 2, 1)
)
wtWebGraphAnalogIn57642SensorEntry.setIndexNames(
    (0, "WebGraph-AnalogIn-57642-US-MIB", "wtWebGraphAnalogIn57642SensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642SensorEntry.setStatus("mandatory")


class _WtWebGraphAnalogIn57642SensorNo_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57642SensorNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WtWebGraphAnalogIn57642SensorNo_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57642SensorNo_Object = MibTableColumn
wtWebGraphAnalogIn57642SensorNo = _WtWebGraphAnalogIn57642SensorNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 1, 2, 1, 1),
    _WtWebGraphAnalogIn57642SensorNo_Type()
)
wtWebGraphAnalogIn57642SensorNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642SensorNo.setStatus("mandatory")
_WtWebGraphAnalogIn57642ValuesTable_Object = MibTable
wtWebGraphAnalogIn57642ValuesTable = _WtWebGraphAnalogIn57642ValuesTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 1, 3)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642ValuesTable.setStatus("mandatory")
_WtWebGraphAnalogIn57642ValuesEntry_Object = MibTableRow
wtWebGraphAnalogIn57642ValuesEntry = _WtWebGraphAnalogIn57642ValuesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 1, 3, 1)
)
wtWebGraphAnalogIn57642ValuesEntry.setIndexNames(
    (0, "WebGraph-AnalogIn-57642-US-MIB", "wtWebGraphAnalogIn57642SensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642ValuesEntry.setStatus("mandatory")


class _WtWebGraphAnalogIn57642Values_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57642Values based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_WtWebGraphAnalogIn57642Values_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57642Values_Object = MibTableColumn
wtWebGraphAnalogIn57642Values = _WtWebGraphAnalogIn57642Values_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 1, 3, 1, 1),
    _WtWebGraphAnalogIn57642Values_Type()
)
wtWebGraphAnalogIn57642Values.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642Values.setStatus("mandatory")
_WtWebGraphAnalogIn57642BinaryValuesTable_Object = MibTable
wtWebGraphAnalogIn57642BinaryValuesTable = _WtWebGraphAnalogIn57642BinaryValuesTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 1, 4)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642BinaryValuesTable.setStatus("mandatory")
_WtWebGraphAnalogIn57642BinaryValuesEntry_Object = MibTableRow
wtWebGraphAnalogIn57642BinaryValuesEntry = _WtWebGraphAnalogIn57642BinaryValuesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 1, 4, 1)
)
wtWebGraphAnalogIn57642BinaryValuesEntry.setIndexNames(
    (0, "WebGraph-AnalogIn-57642-US-MIB", "wtWebGraphAnalogIn57642SensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642BinaryValuesEntry.setStatus("mandatory")
_WtWebGraphAnalogIn57642BinaryValues_Type = Integer32
_WtWebGraphAnalogIn57642BinaryValues_Object = MibTableColumn
wtWebGraphAnalogIn57642BinaryValues = _WtWebGraphAnalogIn57642BinaryValues_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 1, 4, 1, 1),
    _WtWebGraphAnalogIn57642BinaryValues_Type()
)
wtWebGraphAnalogIn57642BinaryValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642BinaryValues.setStatus("mandatory")
_WtWebGraphAnalogIn57642SessCntrl_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57642SessCntrl = _WtWebGraphAnalogIn57642SessCntrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 2)
)
_WtWebGraphAnalogIn57642SessCntrlPassword_Type = OctetString
_WtWebGraphAnalogIn57642SessCntrlPassword_Object = MibScalar
wtWebGraphAnalogIn57642SessCntrlPassword = _WtWebGraphAnalogIn57642SessCntrlPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 2, 1),
    _WtWebGraphAnalogIn57642SessCntrlPassword_Type()
)
wtWebGraphAnalogIn57642SessCntrlPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642SessCntrlPassword.setStatus("mandatory")


class _WtWebGraphAnalogIn57642SessCntrlConfigMode_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57642SessCntrlConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("wtWebGraphAnalogIn57642SessCntrl-NoSession", 0),
          ("wtWebGraphAnalogIn57642SessCntrl-Session", 1))
    )


_WtWebGraphAnalogIn57642SessCntrlConfigMode_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57642SessCntrlConfigMode_Object = MibScalar
wtWebGraphAnalogIn57642SessCntrlConfigMode = _WtWebGraphAnalogIn57642SessCntrlConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 2, 2),
    _WtWebGraphAnalogIn57642SessCntrlConfigMode_Type()
)
wtWebGraphAnalogIn57642SessCntrlConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642SessCntrlConfigMode.setStatus("mandatory")
_WtWebGraphAnalogIn57642SessCntrlLogout_Type = Integer32
_WtWebGraphAnalogIn57642SessCntrlLogout_Object = MibScalar
wtWebGraphAnalogIn57642SessCntrlLogout = _WtWebGraphAnalogIn57642SessCntrlLogout_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 2, 3),
    _WtWebGraphAnalogIn57642SessCntrlLogout_Type()
)
wtWebGraphAnalogIn57642SessCntrlLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642SessCntrlLogout.setStatus("mandatory")
_WtWebGraphAnalogIn57642SessCntrlAdminPassword_Type = OctetString
_WtWebGraphAnalogIn57642SessCntrlAdminPassword_Object = MibScalar
wtWebGraphAnalogIn57642SessCntrlAdminPassword = _WtWebGraphAnalogIn57642SessCntrlAdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 2, 4),
    _WtWebGraphAnalogIn57642SessCntrlAdminPassword_Type()
)
wtWebGraphAnalogIn57642SessCntrlAdminPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642SessCntrlAdminPassword.setStatus("mandatory")
_WtWebGraphAnalogIn57642SessCntrlConfigPassword_Type = OctetString
_WtWebGraphAnalogIn57642SessCntrlConfigPassword_Object = MibScalar
wtWebGraphAnalogIn57642SessCntrlConfigPassword = _WtWebGraphAnalogIn57642SessCntrlConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 2, 5),
    _WtWebGraphAnalogIn57642SessCntrlConfigPassword_Type()
)
wtWebGraphAnalogIn57642SessCntrlConfigPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642SessCntrlConfigPassword.setStatus("mandatory")
_WtWebGraphAnalogIn57642Config_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57642Config = _WtWebGraphAnalogIn57642Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3)
)
_WtWebGraphAnalogIn57642Device_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57642Device = _WtWebGraphAnalogIn57642Device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1)
)
_WtWebGraphAnalogIn57642Text_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57642Text = _WtWebGraphAnalogIn57642Text_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 1)
)
_WtWebGraphAnalogIn57642DeviceName_Type = OctetString
_WtWebGraphAnalogIn57642DeviceName_Object = MibScalar
wtWebGraphAnalogIn57642DeviceName = _WtWebGraphAnalogIn57642DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 1, 1),
    _WtWebGraphAnalogIn57642DeviceName_Type()
)
wtWebGraphAnalogIn57642DeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642DeviceName.setStatus("mandatory")
_WtWebGraphAnalogIn57642DeviceText_Type = OctetString
_WtWebGraphAnalogIn57642DeviceText_Object = MibScalar
wtWebGraphAnalogIn57642DeviceText = _WtWebGraphAnalogIn57642DeviceText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 1, 2),
    _WtWebGraphAnalogIn57642DeviceText_Type()
)
wtWebGraphAnalogIn57642DeviceText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642DeviceText.setStatus("mandatory")
_WtWebGraphAnalogIn57642DeviceLocation_Type = OctetString
_WtWebGraphAnalogIn57642DeviceLocation_Object = MibScalar
wtWebGraphAnalogIn57642DeviceLocation = _WtWebGraphAnalogIn57642DeviceLocation_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 1, 3),
    _WtWebGraphAnalogIn57642DeviceLocation_Type()
)
wtWebGraphAnalogIn57642DeviceLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642DeviceLocation.setStatus("mandatory")
_WtWebGraphAnalogIn57642DeviceContact_Type = OctetString
_WtWebGraphAnalogIn57642DeviceContact_Object = MibScalar
wtWebGraphAnalogIn57642DeviceContact = _WtWebGraphAnalogIn57642DeviceContact_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 1, 4),
    _WtWebGraphAnalogIn57642DeviceContact_Type()
)
wtWebGraphAnalogIn57642DeviceContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642DeviceContact.setStatus("mandatory")
_WtWebGraphAnalogIn57642TimeDate_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57642TimeDate = _WtWebGraphAnalogIn57642TimeDate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 2)
)
_WtWebGraphAnalogIn57642TimeZone_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57642TimeZone = _WtWebGraphAnalogIn57642TimeZone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 2, 1)
)
_WtWebGraphAnalogIn57642TzOffsetHrs_Type = Integer32
_WtWebGraphAnalogIn57642TzOffsetHrs_Object = MibScalar
wtWebGraphAnalogIn57642TzOffsetHrs = _WtWebGraphAnalogIn57642TzOffsetHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 2, 1, 1),
    _WtWebGraphAnalogIn57642TzOffsetHrs_Type()
)
wtWebGraphAnalogIn57642TzOffsetHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642TzOffsetHrs.setStatus("mandatory")
_WtWebGraphAnalogIn57642TzOffsetMin_Type = Integer32
_WtWebGraphAnalogIn57642TzOffsetMin_Object = MibScalar
wtWebGraphAnalogIn57642TzOffsetMin = _WtWebGraphAnalogIn57642TzOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 2, 1, 2),
    _WtWebGraphAnalogIn57642TzOffsetMin_Type()
)
wtWebGraphAnalogIn57642TzOffsetMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642TzOffsetMin.setStatus("mandatory")


class _WtWebGraphAnalogIn57642TzEnable_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57642TzEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphAnalogIn57642TzEnable_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57642TzEnable_Object = MibScalar
wtWebGraphAnalogIn57642TzEnable = _WtWebGraphAnalogIn57642TzEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 2, 1, 3),
    _WtWebGraphAnalogIn57642TzEnable_Type()
)
wtWebGraphAnalogIn57642TzEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642TzEnable.setStatus("mandatory")
_WtWebGraphAnalogIn57642StTzOffsetHrs_Type = Integer32
_WtWebGraphAnalogIn57642StTzOffsetHrs_Object = MibScalar
wtWebGraphAnalogIn57642StTzOffsetHrs = _WtWebGraphAnalogIn57642StTzOffsetHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 2, 1, 4),
    _WtWebGraphAnalogIn57642StTzOffsetHrs_Type()
)
wtWebGraphAnalogIn57642StTzOffsetHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642StTzOffsetHrs.setStatus("mandatory")
_WtWebGraphAnalogIn57642StTzOffsetMin_Type = Integer32
_WtWebGraphAnalogIn57642StTzOffsetMin_Object = MibScalar
wtWebGraphAnalogIn57642StTzOffsetMin = _WtWebGraphAnalogIn57642StTzOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 2, 1, 5),
    _WtWebGraphAnalogIn57642StTzOffsetMin_Type()
)
wtWebGraphAnalogIn57642StTzOffsetMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642StTzOffsetMin.setStatus("mandatory")


class _WtWebGraphAnalogIn57642StTzEnable_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57642StTzEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphAnalogIn57642StTzEnable_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57642StTzEnable_Object = MibScalar
wtWebGraphAnalogIn57642StTzEnable = _WtWebGraphAnalogIn57642StTzEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 2, 1, 6),
    _WtWebGraphAnalogIn57642StTzEnable_Type()
)
wtWebGraphAnalogIn57642StTzEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642StTzEnable.setStatus("mandatory")


class _WtWebGraphAnalogIn57642StTzStartMonth_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57642StTzStartMonth based on Integer32"""
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
        *(("wtWebGraphAnalogIn57642StartMonth-January", 1),
          ("wtWebGraphAnalogIn57642StartMonth-February", 2),
          ("wtWebGraphAnalogIn57642StartMonth-March", 3),
          ("wtWebGraphAnalogIn57642StartMonth-April", 4),
          ("wtWebGraphAnalogIn57642StartMonth-May", 5),
          ("wtWebGraphAnalogIn57642StartMonth-June", 6),
          ("wtWebGraphAnalogIn57642StartMonth-July", 7),
          ("wtWebGraphAnalogIn57642StartMonth-August", 8),
          ("wtWebGraphAnalogIn57642StartMonth-September", 9),
          ("wtWebGraphAnalogIn57642StartMonth-October", 10),
          ("wtWebGraphAnalogIn57642StartMonth-November", 11),
          ("wtWebGraphAnalogIn57642StartMonth-December", 12))
    )


_WtWebGraphAnalogIn57642StTzStartMonth_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57642StTzStartMonth_Object = MibScalar
wtWebGraphAnalogIn57642StTzStartMonth = _WtWebGraphAnalogIn57642StTzStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 2, 1, 7),
    _WtWebGraphAnalogIn57642StTzStartMonth_Type()
)
wtWebGraphAnalogIn57642StTzStartMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642StTzStartMonth.setStatus("mandatory")


class _WtWebGraphAnalogIn57642StTzStartMode_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57642StTzStartMode based on Integer32"""
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
        *(("wtWebGraphAnalogIn57642StartMode-first", 1),
          ("wtWebGraphAnalogIn57642StartMode-second", 2),
          ("wtWebGraphAnalogIn57642StartMode-third", 3),
          ("wtWebGraphAnalogIn57642StartMode-fourth", 4),
          ("wtWebGraphAnalogIn57642StartMode-last", 5))
    )


_WtWebGraphAnalogIn57642StTzStartMode_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57642StTzStartMode_Object = MibScalar
wtWebGraphAnalogIn57642StTzStartMode = _WtWebGraphAnalogIn57642StTzStartMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 2, 1, 8),
    _WtWebGraphAnalogIn57642StTzStartMode_Type()
)
wtWebGraphAnalogIn57642StTzStartMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642StTzStartMode.setStatus("mandatory")


class _WtWebGraphAnalogIn57642StTzStartWday_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57642StTzStartWday based on Integer32"""
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
        *(("wtWebGraphAnalogIn57642StartWday-Sunday", 1),
          ("wtWebGraphAnalogIn57642StartWday-Monday", 2),
          ("wtWebGraphAnalogIn57642StartWday-Tuesday", 3),
          ("wtWebGraphAnalogIn57642StartWday-Thursday", 4),
          ("wtWebGraphAnalogIn57642StartWday-Wednesday", 5),
          ("wtWebGraphAnalogIn57642StartWday-Friday", 6),
          ("wtWebGraphAnalogIn57642StartWday-Saturday", 7))
    )


_WtWebGraphAnalogIn57642StTzStartWday_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57642StTzStartWday_Object = MibScalar
wtWebGraphAnalogIn57642StTzStartWday = _WtWebGraphAnalogIn57642StTzStartWday_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 2, 1, 9),
    _WtWebGraphAnalogIn57642StTzStartWday_Type()
)
wtWebGraphAnalogIn57642StTzStartWday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642StTzStartWday.setStatus("mandatory")
_WtWebGraphAnalogIn57642StTzStartHrs_Type = Integer32
_WtWebGraphAnalogIn57642StTzStartHrs_Object = MibScalar
wtWebGraphAnalogIn57642StTzStartHrs = _WtWebGraphAnalogIn57642StTzStartHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 2, 1, 10),
    _WtWebGraphAnalogIn57642StTzStartHrs_Type()
)
wtWebGraphAnalogIn57642StTzStartHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642StTzStartHrs.setStatus("mandatory")
_WtWebGraphAnalogIn57642StTzStartMin_Type = Integer32
_WtWebGraphAnalogIn57642StTzStartMin_Object = MibScalar
wtWebGraphAnalogIn57642StTzStartMin = _WtWebGraphAnalogIn57642StTzStartMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 2, 1, 11),
    _WtWebGraphAnalogIn57642StTzStartMin_Type()
)
wtWebGraphAnalogIn57642StTzStartMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642StTzStartMin.setStatus("mandatory")


class _WtWebGraphAnalogIn57642StTzStopMonth_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57642StTzStopMonth based on Integer32"""
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
        *(("wtWebGraphAnalogIn57642StopMonth-January", 1),
          ("wtWebGraphAnalogIn57642StopMonth-February", 2),
          ("wtWebGraphAnalogIn57642StopMonth-March", 3),
          ("wtWebGraphAnalogIn57642StopMonth-April", 4),
          ("wtWebGraphAnalogIn57642StopMonth-May", 5),
          ("wtWebGraphAnalogIn57642StopMonth-June", 6),
          ("wtWebGraphAnalogIn57642StopMonth-July", 7),
          ("wtWebGraphAnalogIn57642StopMonth-August", 8),
          ("wtWebGraphAnalogIn57642StopMonth-September", 9),
          ("wtWebGraphAnalogIn57642StopMonth-October", 10),
          ("wtWebGraphAnalogIn57642StopMonth-November", 11),
          ("wtWebGraphAnalogIn57642StopMonth-December", 12))
    )


_WtWebGraphAnalogIn57642StTzStopMonth_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57642StTzStopMonth_Object = MibScalar
wtWebGraphAnalogIn57642StTzStopMonth = _WtWebGraphAnalogIn57642StTzStopMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 2, 1, 12),
    _WtWebGraphAnalogIn57642StTzStopMonth_Type()
)
wtWebGraphAnalogIn57642StTzStopMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642StTzStopMonth.setStatus("mandatory")


class _WtWebGraphAnalogIn57642StTzStopMode_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57642StTzStopMode based on Integer32"""
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
        *(("wtWebGraphAnalogIn57642StopMode-first", 1),
          ("wtWebGraphAnalogIn57642StopMode-second", 2),
          ("wtWebGraphAnalogIn57642StopMode-third", 3),
          ("wtWebGraphAnalogIn57642StopMode-fourth", 4),
          ("wtWebGraphAnalogIn57642StopMode-last", 5))
    )


_WtWebGraphAnalogIn57642StTzStopMode_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57642StTzStopMode_Object = MibScalar
wtWebGraphAnalogIn57642StTzStopMode = _WtWebGraphAnalogIn57642StTzStopMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 2, 1, 13),
    _WtWebGraphAnalogIn57642StTzStopMode_Type()
)
wtWebGraphAnalogIn57642StTzStopMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642StTzStopMode.setStatus("mandatory")


class _WtWebGraphAnalogIn57642StTzStopWday_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57642StTzStopWday based on Integer32"""
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
        *(("wtWebGraphAnalogIn57642StopWday-Sunday", 1),
          ("wtWebGraphAnalogIn57642StopWday-Monday", 2),
          ("wtWebGraphAnalogIn57642StopWday-Tuesday", 3),
          ("wtWebGraphAnalogIn57642StopWday-Thursday", 4),
          ("wtWebGraphAnalogIn57642StopWday-Wednesday", 5),
          ("wtWebGraphAnalogIn57642StopWday-Friday", 6),
          ("wtWebGraphAnalogIn57642StopWday-Saturday", 7))
    )


_WtWebGraphAnalogIn57642StTzStopWday_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57642StTzStopWday_Object = MibScalar
wtWebGraphAnalogIn57642StTzStopWday = _WtWebGraphAnalogIn57642StTzStopWday_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 2, 1, 14),
    _WtWebGraphAnalogIn57642StTzStopWday_Type()
)
wtWebGraphAnalogIn57642StTzStopWday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642StTzStopWday.setStatus("mandatory")
_WtWebGraphAnalogIn57642StTzStopHrs_Type = Integer32
_WtWebGraphAnalogIn57642StTzStopHrs_Object = MibScalar
wtWebGraphAnalogIn57642StTzStopHrs = _WtWebGraphAnalogIn57642StTzStopHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 2, 1, 15),
    _WtWebGraphAnalogIn57642StTzStopHrs_Type()
)
wtWebGraphAnalogIn57642StTzStopHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642StTzStopHrs.setStatus("mandatory")
_WtWebGraphAnalogIn57642StTzStopMin_Type = Integer32
_WtWebGraphAnalogIn57642StTzStopMin_Object = MibScalar
wtWebGraphAnalogIn57642StTzStopMin = _WtWebGraphAnalogIn57642StTzStopMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 2, 1, 16),
    _WtWebGraphAnalogIn57642StTzStopMin_Type()
)
wtWebGraphAnalogIn57642StTzStopMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642StTzStopMin.setStatus("mandatory")
_WtWebGraphAnalogIn57642TimeServer_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57642TimeServer = _WtWebGraphAnalogIn57642TimeServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 2, 2)
)
_WtWebGraphAnalogIn57642TimeServer1_Type = OctetString
_WtWebGraphAnalogIn57642TimeServer1_Object = MibScalar
wtWebGraphAnalogIn57642TimeServer1 = _WtWebGraphAnalogIn57642TimeServer1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 2, 2, 1),
    _WtWebGraphAnalogIn57642TimeServer1_Type()
)
wtWebGraphAnalogIn57642TimeServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642TimeServer1.setStatus("mandatory")
_WtWebGraphAnalogIn57642TimeServer2_Type = OctetString
_WtWebGraphAnalogIn57642TimeServer2_Object = MibScalar
wtWebGraphAnalogIn57642TimeServer2 = _WtWebGraphAnalogIn57642TimeServer2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 2, 2, 2),
    _WtWebGraphAnalogIn57642TimeServer2_Type()
)
wtWebGraphAnalogIn57642TimeServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642TimeServer2.setStatus("mandatory")


class _WtWebGraphAnalogIn57642TsEnable_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57642TsEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphAnalogIn57642TsEnable_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57642TsEnable_Object = MibScalar
wtWebGraphAnalogIn57642TsEnable = _WtWebGraphAnalogIn57642TsEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 2, 2, 3),
    _WtWebGraphAnalogIn57642TsEnable_Type()
)
wtWebGraphAnalogIn57642TsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642TsEnable.setStatus("mandatory")
_WtWebGraphAnalogIn57642TsSyncTime_Type = Integer32
_WtWebGraphAnalogIn57642TsSyncTime_Object = MibScalar
wtWebGraphAnalogIn57642TsSyncTime = _WtWebGraphAnalogIn57642TsSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 2, 2, 4),
    _WtWebGraphAnalogIn57642TsSyncTime_Type()
)
wtWebGraphAnalogIn57642TsSyncTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642TsSyncTime.setStatus("mandatory")
_WtWebGraphAnalogIn57642DeviceClock_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57642DeviceClock = _WtWebGraphAnalogIn57642DeviceClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 2, 3)
)


class _WtWebGraphAnalogIn57642ClockHrs_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57642ClockHrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_WtWebGraphAnalogIn57642ClockHrs_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57642ClockHrs_Object = MibScalar
wtWebGraphAnalogIn57642ClockHrs = _WtWebGraphAnalogIn57642ClockHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 2, 3, 1),
    _WtWebGraphAnalogIn57642ClockHrs_Type()
)
wtWebGraphAnalogIn57642ClockHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642ClockHrs.setStatus("mandatory")


class _WtWebGraphAnalogIn57642ClockMin_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57642ClockMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_WtWebGraphAnalogIn57642ClockMin_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57642ClockMin_Object = MibScalar
wtWebGraphAnalogIn57642ClockMin = _WtWebGraphAnalogIn57642ClockMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 2, 3, 2),
    _WtWebGraphAnalogIn57642ClockMin_Type()
)
wtWebGraphAnalogIn57642ClockMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642ClockMin.setStatus("mandatory")


class _WtWebGraphAnalogIn57642ClockDay_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57642ClockDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_WtWebGraphAnalogIn57642ClockDay_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57642ClockDay_Object = MibScalar
wtWebGraphAnalogIn57642ClockDay = _WtWebGraphAnalogIn57642ClockDay_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 2, 3, 3),
    _WtWebGraphAnalogIn57642ClockDay_Type()
)
wtWebGraphAnalogIn57642ClockDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642ClockDay.setStatus("mandatory")


class _WtWebGraphAnalogIn57642ClockMonth_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57642ClockMonth based on Integer32"""
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
        *(("wtWebGraphAnalogIn57642ClockMonth-January", 1),
          ("wtWebGraphAnalogIn57642ClockMonth-February", 2),
          ("wtWebGraphAnalogIn57642ClockMonth-March", 3),
          ("wtWebGraphAnalogIn57642ClockMonth-April", 4),
          ("wtWebGraphAnalogIn57642ClockMonth-May", 5),
          ("wtWebGraphAnalogIn57642ClockMonth-June", 6),
          ("wtWebGraphAnalogIn57642ClockMonth-July", 7),
          ("wtWebGraphAnalogIn57642ClockMonth-August", 8),
          ("wtWebGraphAnalogIn57642ClockMonth-September", 9),
          ("wtWebGraphAnalogIn57642ClockMonth-October", 10),
          ("wtWebGraphAnalogIn57642ClockMonth-November", 11),
          ("wtWebGraphAnalogIn57642ClockMonth-December", 12))
    )


_WtWebGraphAnalogIn57642ClockMonth_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57642ClockMonth_Object = MibScalar
wtWebGraphAnalogIn57642ClockMonth = _WtWebGraphAnalogIn57642ClockMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 2, 3, 4),
    _WtWebGraphAnalogIn57642ClockMonth_Type()
)
wtWebGraphAnalogIn57642ClockMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642ClockMonth.setStatus("mandatory")


class _WtWebGraphAnalogIn57642ClockYear_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57642ClockYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtWebGraphAnalogIn57642ClockYear_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57642ClockYear_Object = MibScalar
wtWebGraphAnalogIn57642ClockYear = _WtWebGraphAnalogIn57642ClockYear_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 2, 3, 5),
    _WtWebGraphAnalogIn57642ClockYear_Type()
)
wtWebGraphAnalogIn57642ClockYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642ClockYear.setStatus("mandatory")
_WtWebGraphAnalogIn57642Basic_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57642Basic = _WtWebGraphAnalogIn57642Basic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3)
)
_WtWebGraphAnalogIn57642Network_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57642Network = _WtWebGraphAnalogIn57642Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 1)
)
_WtWebGraphAnalogIn57642IpAddress_Type = IpAddress
_WtWebGraphAnalogIn57642IpAddress_Object = MibScalar
wtWebGraphAnalogIn57642IpAddress = _WtWebGraphAnalogIn57642IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 1, 1),
    _WtWebGraphAnalogIn57642IpAddress_Type()
)
wtWebGraphAnalogIn57642IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642IpAddress.setStatus("mandatory")
_WtWebGraphAnalogIn57642SubnetMask_Type = IpAddress
_WtWebGraphAnalogIn57642SubnetMask_Object = MibScalar
wtWebGraphAnalogIn57642SubnetMask = _WtWebGraphAnalogIn57642SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 1, 2),
    _WtWebGraphAnalogIn57642SubnetMask_Type()
)
wtWebGraphAnalogIn57642SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642SubnetMask.setStatus("mandatory")
_WtWebGraphAnalogIn57642Gateway_Type = IpAddress
_WtWebGraphAnalogIn57642Gateway_Object = MibScalar
wtWebGraphAnalogIn57642Gateway = _WtWebGraphAnalogIn57642Gateway_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 1, 3),
    _WtWebGraphAnalogIn57642Gateway_Type()
)
wtWebGraphAnalogIn57642Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642Gateway.setStatus("mandatory")
_WtWebGraphAnalogIn57642DnsServer1_Type = OctetString
_WtWebGraphAnalogIn57642DnsServer1_Object = MibScalar
wtWebGraphAnalogIn57642DnsServer1 = _WtWebGraphAnalogIn57642DnsServer1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 1, 4),
    _WtWebGraphAnalogIn57642DnsServer1_Type()
)
wtWebGraphAnalogIn57642DnsServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642DnsServer1.setStatus("mandatory")
_WtWebGraphAnalogIn57642DnsServer2_Type = OctetString
_WtWebGraphAnalogIn57642DnsServer2_Object = MibScalar
wtWebGraphAnalogIn57642DnsServer2 = _WtWebGraphAnalogIn57642DnsServer2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 1, 5),
    _WtWebGraphAnalogIn57642DnsServer2_Type()
)
wtWebGraphAnalogIn57642DnsServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642DnsServer2.setStatus("mandatory")
_WtWebGraphAnalogIn57642AddConfig_Type = OctetString
_WtWebGraphAnalogIn57642AddConfig_Object = MibScalar
wtWebGraphAnalogIn57642AddConfig = _WtWebGraphAnalogIn57642AddConfig_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 1, 6),
    _WtWebGraphAnalogIn57642AddConfig_Type()
)
wtWebGraphAnalogIn57642AddConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642AddConfig.setStatus("mandatory")
_WtWebGraphAnalogIn57642HTTP_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57642HTTP = _WtWebGraphAnalogIn57642HTTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 2)
)
_WtWebGraphAnalogIn57642Startup_Type = OctetString
_WtWebGraphAnalogIn57642Startup_Object = MibScalar
wtWebGraphAnalogIn57642Startup = _WtWebGraphAnalogIn57642Startup_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 2, 1),
    _WtWebGraphAnalogIn57642Startup_Type()
)
wtWebGraphAnalogIn57642Startup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642Startup.setStatus("mandatory")
_WtWebGraphAnalogIn57642GetHeaderEnable_Type = OctetString
_WtWebGraphAnalogIn57642GetHeaderEnable_Object = MibScalar
wtWebGraphAnalogIn57642GetHeaderEnable = _WtWebGraphAnalogIn57642GetHeaderEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 2, 2),
    _WtWebGraphAnalogIn57642GetHeaderEnable_Type()
)
wtWebGraphAnalogIn57642GetHeaderEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642GetHeaderEnable.setStatus("mandatory")


class _WtWebGraphAnalogIn57642HttpPort_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57642HttpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalogIn57642HttpPort_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57642HttpPort_Object = MibScalar
wtWebGraphAnalogIn57642HttpPort = _WtWebGraphAnalogIn57642HttpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 2, 3),
    _WtWebGraphAnalogIn57642HttpPort_Type()
)
wtWebGraphAnalogIn57642HttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642HttpPort.setStatus("mandatory")
_WtWebGraphAnalogIn57642Mail_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57642Mail = _WtWebGraphAnalogIn57642Mail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 3)
)
_WtWebGraphAnalogIn57642MailAdName_Type = OctetString
_WtWebGraphAnalogIn57642MailAdName_Object = MibScalar
wtWebGraphAnalogIn57642MailAdName = _WtWebGraphAnalogIn57642MailAdName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 3, 1),
    _WtWebGraphAnalogIn57642MailAdName_Type()
)
wtWebGraphAnalogIn57642MailAdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642MailAdName.setStatus("mandatory")
_WtWebGraphAnalogIn57642MailReply_Type = OctetString
_WtWebGraphAnalogIn57642MailReply_Object = MibScalar
wtWebGraphAnalogIn57642MailReply = _WtWebGraphAnalogIn57642MailReply_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 3, 2),
    _WtWebGraphAnalogIn57642MailReply_Type()
)
wtWebGraphAnalogIn57642MailReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642MailReply.setStatus("mandatory")
_WtWebGraphAnalogIn57642MailServer_Type = OctetString
_WtWebGraphAnalogIn57642MailServer_Object = MibScalar
wtWebGraphAnalogIn57642MailServer = _WtWebGraphAnalogIn57642MailServer_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 3, 3),
    _WtWebGraphAnalogIn57642MailServer_Type()
)
wtWebGraphAnalogIn57642MailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642MailServer.setStatus("mandatory")
_WtWebioAn1MailEnable_Type = OctetString
_WtWebioAn1MailEnable_Object = MibScalar
wtWebioAn1MailEnable = _WtWebioAn1MailEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 3, 4),
    _WtWebioAn1MailEnable_Type()
)
wtWebioAn1MailEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1MailEnable.setStatus("mandatory")


class _WtWebGraphAnalogIn57642MailAuthentication_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57642MailAuthentication based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphAnalogIn57642MailAuthentication_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57642MailAuthentication_Object = MibScalar
wtWebGraphAnalogIn57642MailAuthentication = _WtWebGraphAnalogIn57642MailAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 3, 5),
    _WtWebGraphAnalogIn57642MailAuthentication_Type()
)
wtWebGraphAnalogIn57642MailAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642MailAuthentication.setStatus("mandatory")
_WtWebGraphAnalogIn57642MailAuthUser_Type = OctetString
_WtWebGraphAnalogIn57642MailAuthUser_Object = MibScalar
wtWebGraphAnalogIn57642MailAuthUser = _WtWebGraphAnalogIn57642MailAuthUser_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 3, 6),
    _WtWebGraphAnalogIn57642MailAuthUser_Type()
)
wtWebGraphAnalogIn57642MailAuthUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642MailAuthUser.setStatus("mandatory")
_WtWebGraphAnalogIn57642MailAuthPassword_Type = OctetString
_WtWebGraphAnalogIn57642MailAuthPassword_Object = MibScalar
wtWebGraphAnalogIn57642MailAuthPassword = _WtWebGraphAnalogIn57642MailAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 3, 7),
    _WtWebGraphAnalogIn57642MailAuthPassword_Type()
)
wtWebGraphAnalogIn57642MailAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642MailAuthPassword.setStatus("mandatory")
_WtWebGraphAnalogIn57642MailPop3Server_Type = OctetString
_WtWebGraphAnalogIn57642MailPop3Server_Object = MibScalar
wtWebGraphAnalogIn57642MailPop3Server = _WtWebGraphAnalogIn57642MailPop3Server_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 3, 8),
    _WtWebGraphAnalogIn57642MailPop3Server_Type()
)
wtWebGraphAnalogIn57642MailPop3Server.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642MailPop3Server.setStatus("mandatory")
_WtWebGraphAnalogIn57642SNMP_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57642SNMP = _WtWebGraphAnalogIn57642SNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 4)
)
_WtWebGraphAnalogIn57642SnmpCommunityStringRead_Type = OctetString
_WtWebGraphAnalogIn57642SnmpCommunityStringRead_Object = MibScalar
wtWebGraphAnalogIn57642SnmpCommunityStringRead = _WtWebGraphAnalogIn57642SnmpCommunityStringRead_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 4, 1),
    _WtWebGraphAnalogIn57642SnmpCommunityStringRead_Type()
)
wtWebGraphAnalogIn57642SnmpCommunityStringRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642SnmpCommunityStringRead.setStatus("mandatory")
_WtWebGraphAnalogIn57642SnmpCommunityStringReadWrite_Type = OctetString
_WtWebGraphAnalogIn57642SnmpCommunityStringReadWrite_Object = MibScalar
wtWebGraphAnalogIn57642SnmpCommunityStringReadWrite = _WtWebGraphAnalogIn57642SnmpCommunityStringReadWrite_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 4, 2),
    _WtWebGraphAnalogIn57642SnmpCommunityStringReadWrite_Type()
)
wtWebGraphAnalogIn57642SnmpCommunityStringReadWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642SnmpCommunityStringReadWrite.setStatus("mandatory")
_WtWebGraphAnalogIn57642SystemTrapManagerIP_Type = OctetString
_WtWebGraphAnalogIn57642SystemTrapManagerIP_Object = MibScalar
wtWebGraphAnalogIn57642SystemTrapManagerIP = _WtWebGraphAnalogIn57642SystemTrapManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 4, 3),
    _WtWebGraphAnalogIn57642SystemTrapManagerIP_Type()
)
wtWebGraphAnalogIn57642SystemTrapManagerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642SystemTrapManagerIP.setStatus("mandatory")


class _WtWebGraphAnalogIn57642SystemTrapEnable_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57642SystemTrapEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphAnalogIn57642SystemTrapEnable_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57642SystemTrapEnable_Object = MibScalar
wtWebGraphAnalogIn57642SystemTrapEnable = _WtWebGraphAnalogIn57642SystemTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 4, 4),
    _WtWebGraphAnalogIn57642SystemTrapEnable_Type()
)
wtWebGraphAnalogIn57642SystemTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642SystemTrapEnable.setStatus("mandatory")
_WtWebGraphAnalogIn57642SnmpEnable_Type = OctetString
_WtWebGraphAnalogIn57642SnmpEnable_Object = MibScalar
wtWebGraphAnalogIn57642SnmpEnable = _WtWebGraphAnalogIn57642SnmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 4, 5),
    _WtWebGraphAnalogIn57642SnmpEnable_Type()
)
wtWebGraphAnalogIn57642SnmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642SnmpEnable.setStatus("mandatory")
_WtWebGraphAnalogIn57642SnmpCommunityStringTrap_Type = OctetString
_WtWebGraphAnalogIn57642SnmpCommunityStringTrap_Object = MibScalar
wtWebGraphAnalogIn57642SnmpCommunityStringTrap = _WtWebGraphAnalogIn57642SnmpCommunityStringTrap_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 4, 6),
    _WtWebGraphAnalogIn57642SnmpCommunityStringTrap_Type()
)
wtWebGraphAnalogIn57642SnmpCommunityStringTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642SnmpCommunityStringTrap.setStatus("mandatory")
_WtWebGraphAnalogIn57642UDP_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57642UDP = _WtWebGraphAnalogIn57642UDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 5)
)


class _WtWebGraphAnalogIn57642UdpPort_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57642UdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalogIn57642UdpPort_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57642UdpPort_Object = MibScalar
wtWebGraphAnalogIn57642UdpPort = _WtWebGraphAnalogIn57642UdpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 5, 1),
    _WtWebGraphAnalogIn57642UdpPort_Type()
)
wtWebGraphAnalogIn57642UdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642UdpPort.setStatus("mandatory")
_WtWebGraphAnalogIn57642UdpEnable_Type = OctetString
_WtWebGraphAnalogIn57642UdpEnable_Object = MibScalar
wtWebGraphAnalogIn57642UdpEnable = _WtWebGraphAnalogIn57642UdpEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 5, 2),
    _WtWebGraphAnalogIn57642UdpEnable_Type()
)
wtWebGraphAnalogIn57642UdpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642UdpEnable.setStatus("mandatory")
_WtWebGraphAnalogIn57642Syslog_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57642Syslog = _WtWebGraphAnalogIn57642Syslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 6)
)
_WtWebGraphAnalogIn57642SyslogServerIP_Type = OctetString
_WtWebGraphAnalogIn57642SyslogServerIP_Object = MibScalar
wtWebGraphAnalogIn57642SyslogServerIP = _WtWebGraphAnalogIn57642SyslogServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 6, 1),
    _WtWebGraphAnalogIn57642SyslogServerIP_Type()
)
wtWebGraphAnalogIn57642SyslogServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642SyslogServerIP.setStatus("mandatory")
_WtWebGraphAnalogIn57642SyslogServerPort_Type = Integer32
_WtWebGraphAnalogIn57642SyslogServerPort_Object = MibScalar
wtWebGraphAnalogIn57642SyslogServerPort = _WtWebGraphAnalogIn57642SyslogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 6, 2),
    _WtWebGraphAnalogIn57642SyslogServerPort_Type()
)
wtWebGraphAnalogIn57642SyslogServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642SyslogServerPort.setStatus("mandatory")


class _WtWebGraphAnalogIn57642SyslogSystemMessagesEnable_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57642SyslogSystemMessagesEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphAnalogIn57642SyslogSystemMessagesEnable_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57642SyslogSystemMessagesEnable_Object = MibScalar
wtWebGraphAnalogIn57642SyslogSystemMessagesEnable = _WtWebGraphAnalogIn57642SyslogSystemMessagesEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 6, 3),
    _WtWebGraphAnalogIn57642SyslogSystemMessagesEnable_Type()
)
wtWebGraphAnalogIn57642SyslogSystemMessagesEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642SyslogSystemMessagesEnable.setStatus("mandatory")
_WtWebGraphAnalogIn57642SyslogEnable_Type = OctetString
_WtWebGraphAnalogIn57642SyslogEnable_Object = MibScalar
wtWebGraphAnalogIn57642SyslogEnable = _WtWebGraphAnalogIn57642SyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 6, 4),
    _WtWebGraphAnalogIn57642SyslogEnable_Type()
)
wtWebGraphAnalogIn57642SyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642SyslogEnable.setStatus("mandatory")
_WtWebGraphAnalogIn57642FTP_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57642FTP = _WtWebGraphAnalogIn57642FTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 7)
)
_WtWebGraphAnalogIn57642FTPServerIP_Type = OctetString
_WtWebGraphAnalogIn57642FTPServerIP_Object = MibScalar
wtWebGraphAnalogIn57642FTPServerIP = _WtWebGraphAnalogIn57642FTPServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 7, 1),
    _WtWebGraphAnalogIn57642FTPServerIP_Type()
)
wtWebGraphAnalogIn57642FTPServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642FTPServerIP.setStatus("mandatory")
_WtWebGraphAnalogIn57642FTPServerControlPort_Type = Integer32
_WtWebGraphAnalogIn57642FTPServerControlPort_Object = MibScalar
wtWebGraphAnalogIn57642FTPServerControlPort = _WtWebGraphAnalogIn57642FTPServerControlPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 7, 2),
    _WtWebGraphAnalogIn57642FTPServerControlPort_Type()
)
wtWebGraphAnalogIn57642FTPServerControlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642FTPServerControlPort.setStatus("mandatory")
_WtWebGraphAnalogIn57642FTPUserName_Type = OctetString
_WtWebGraphAnalogIn57642FTPUserName_Object = MibScalar
wtWebGraphAnalogIn57642FTPUserName = _WtWebGraphAnalogIn57642FTPUserName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 7, 3),
    _WtWebGraphAnalogIn57642FTPUserName_Type()
)
wtWebGraphAnalogIn57642FTPUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642FTPUserName.setStatus("mandatory")
_WtWebGraphAnalogIn57642FTPPassword_Type = OctetString
_WtWebGraphAnalogIn57642FTPPassword_Object = MibScalar
wtWebGraphAnalogIn57642FTPPassword = _WtWebGraphAnalogIn57642FTPPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 7, 4),
    _WtWebGraphAnalogIn57642FTPPassword_Type()
)
wtWebGraphAnalogIn57642FTPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642FTPPassword.setStatus("mandatory")
_WtWebGraphAnalogIn57642FTPAccount_Type = OctetString
_WtWebGraphAnalogIn57642FTPAccount_Object = MibScalar
wtWebGraphAnalogIn57642FTPAccount = _WtWebGraphAnalogIn57642FTPAccount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 7, 5),
    _WtWebGraphAnalogIn57642FTPAccount_Type()
)
wtWebGraphAnalogIn57642FTPAccount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642FTPAccount.setStatus("mandatory")
_WtWebGraphAnalogIn57642FTPOption_Type = OctetString
_WtWebGraphAnalogIn57642FTPOption_Object = MibScalar
wtWebGraphAnalogIn57642FTPOption = _WtWebGraphAnalogIn57642FTPOption_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 7, 6),
    _WtWebGraphAnalogIn57642FTPOption_Type()
)
wtWebGraphAnalogIn57642FTPOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642FTPOption.setStatus("mandatory")
_WtWebGraphAnalogIn57642FTPEnable_Type = OctetString
_WtWebGraphAnalogIn57642FTPEnable_Object = MibScalar
wtWebGraphAnalogIn57642FTPEnable = _WtWebGraphAnalogIn57642FTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 3, 7, 7),
    _WtWebGraphAnalogIn57642FTPEnable_Type()
)
wtWebGraphAnalogIn57642FTPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642FTPEnable.setStatus("mandatory")
_WtWebGraphAnalogIn57642Datalogger_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57642Datalogger = _WtWebGraphAnalogIn57642Datalogger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 4)
)


class _WtWebGraphAnalogIn57642LoggerTimebase_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57642LoggerTimebase based on Integer32"""
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
        *(("wtWebGraphAnalogIn57642Datalogger-1Min", 1),
          ("wtWebGraphAnalogIn57642Datalogger-5Min", 2),
          ("wtWebGraphAnalogIn57642Datalogger-15Min", 3),
          ("wtWebGraphAnalogIn57642Datalogger-60Min", 4))
    )


_WtWebGraphAnalogIn57642LoggerTimebase_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57642LoggerTimebase_Object = MibScalar
wtWebGraphAnalogIn57642LoggerTimebase = _WtWebGraphAnalogIn57642LoggerTimebase_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 4, 1),
    _WtWebGraphAnalogIn57642LoggerTimebase_Type()
)
wtWebGraphAnalogIn57642LoggerTimebase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642LoggerTimebase.setStatus("mandatory")


class _WtWebGraphAnalogIn57642LoggerSensorSel_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57642LoggerSensorSel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphAnalogIn57642LoggerSensorSel_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57642LoggerSensorSel_Object = MibScalar
wtWebGraphAnalogIn57642LoggerSensorSel = _WtWebGraphAnalogIn57642LoggerSensorSel_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 4, 2),
    _WtWebGraphAnalogIn57642LoggerSensorSel_Type()
)
wtWebGraphAnalogIn57642LoggerSensorSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642LoggerSensorSel.setStatus("mandatory")


class _WtWebGraphAnalogIn57642DisplaySensorSel_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57642DisplaySensorSel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphAnalogIn57642DisplaySensorSel_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57642DisplaySensorSel_Object = MibScalar
wtWebGraphAnalogIn57642DisplaySensorSel = _WtWebGraphAnalogIn57642DisplaySensorSel_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 4, 3),
    _WtWebGraphAnalogIn57642DisplaySensorSel_Type()
)
wtWebGraphAnalogIn57642DisplaySensorSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642DisplaySensorSel.setStatus("mandatory")
_WtWebGraphAnalogIn57642SensorColorTable_Object = MibTable
wtWebGraphAnalogIn57642SensorColorTable = _WtWebGraphAnalogIn57642SensorColorTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 4, 4)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642SensorColorTable.setStatus("mandatory")
_WtWebGraphAnalogIn57642SensorColorEntry_Object = MibTableRow
wtWebGraphAnalogIn57642SensorColorEntry = _WtWebGraphAnalogIn57642SensorColorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 4, 4, 1)
)
wtWebGraphAnalogIn57642SensorColorEntry.setIndexNames(
    (0, "WebGraph-AnalogIn-57642-US-MIB", "wtWebGraphAnalogIn57642SensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642SensorColorEntry.setStatus("mandatory")


class _WtWebGraphAnalogIn57642SensorColor_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57642SensorColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_WtWebGraphAnalogIn57642SensorColor_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57642SensorColor_Object = MibTableColumn
wtWebGraphAnalogIn57642SensorColor = _WtWebGraphAnalogIn57642SensorColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 4, 4, 1, 1),
    _WtWebGraphAnalogIn57642SensorColor_Type()
)
wtWebGraphAnalogIn57642SensorColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642SensorColor.setStatus("mandatory")
_WtWebGraphAnalogIn57642AutoScaleEnable_Type = OctetString
_WtWebGraphAnalogIn57642AutoScaleEnable_Object = MibScalar
wtWebGraphAnalogIn57642AutoScaleEnable = _WtWebGraphAnalogIn57642AutoScaleEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 4, 5),
    _WtWebGraphAnalogIn57642AutoScaleEnable_Type()
)
wtWebGraphAnalogIn57642AutoScaleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642AutoScaleEnable.setStatus("mandatory")
_WtWebGraphAnalogIn57642VerticalUpperLimit_Type = OctetString
_WtWebGraphAnalogIn57642VerticalUpperLimit_Object = MibScalar
wtWebGraphAnalogIn57642VerticalUpperLimit = _WtWebGraphAnalogIn57642VerticalUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 4, 6),
    _WtWebGraphAnalogIn57642VerticalUpperLimit_Type()
)
wtWebGraphAnalogIn57642VerticalUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642VerticalUpperLimit.setStatus("mandatory")
_WtWebGraphAnalogIn57642VerticalLowerLimit_Type = OctetString
_WtWebGraphAnalogIn57642VerticalLowerLimit_Object = MibScalar
wtWebGraphAnalogIn57642VerticalLowerLimit = _WtWebGraphAnalogIn57642VerticalLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 4, 7),
    _WtWebGraphAnalogIn57642VerticalLowerLimit_Type()
)
wtWebGraphAnalogIn57642VerticalLowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642VerticalLowerLimit.setStatus("mandatory")


class _WtWebGraphAnalogIn57642HorizontalZoom_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57642HorizontalZoom based on Integer32"""
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
        *(("wtWebGraphAnalogIn57642Zoom-25min", 1),
          ("wtWebGraphAnalogIn57642Zoom-75min", 2),
          ("wtWebGraphAnalogIn57642Zoom-5hrs", 3),
          ("wtWebGraphAnalogIn57642Zoom-30hrs", 4),
          ("wtWebGraphAnalogIn57642Zoom-5days", 5),
          ("wtWebGraphAnalogIn57642Zoom-25days", 6))
    )


_WtWebGraphAnalogIn57642HorizontalZoom_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57642HorizontalZoom_Object = MibScalar
wtWebGraphAnalogIn57642HorizontalZoom = _WtWebGraphAnalogIn57642HorizontalZoom_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 4, 8),
    _WtWebGraphAnalogIn57642HorizontalZoom_Type()
)
wtWebGraphAnalogIn57642HorizontalZoom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642HorizontalZoom.setStatus("mandatory")
_WtWebGraphAnalogIn57642Alarm_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57642Alarm = _WtWebGraphAnalogIn57642Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 5)
)


class _WtWebGraphAnalogIn57642AlarmCount_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57642AlarmCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WtWebGraphAnalogIn57642AlarmCount_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57642AlarmCount_Object = MibScalar
wtWebGraphAnalogIn57642AlarmCount = _WtWebGraphAnalogIn57642AlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 5, 1),
    _WtWebGraphAnalogIn57642AlarmCount_Type()
)
wtWebGraphAnalogIn57642AlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642AlarmCount.setStatus("mandatory")
_WtWebGraphAnalogIn57642AlarmIfTable_Object = MibTable
wtWebGraphAnalogIn57642AlarmIfTable = _WtWebGraphAnalogIn57642AlarmIfTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 5, 2)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642AlarmIfTable.setStatus("mandatory")
_WtWebGraphAnalogIn57642AlarmIfEntry_Object = MibTableRow
wtWebGraphAnalogIn57642AlarmIfEntry = _WtWebGraphAnalogIn57642AlarmIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 5, 2, 1)
)
wtWebGraphAnalogIn57642AlarmIfEntry.setIndexNames(
    (0, "WebGraph-AnalogIn-57642-US-MIB", "wtWebGraphAnalogIn57642AlarmNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642AlarmIfEntry.setStatus("mandatory")


class _WtWebGraphAnalogIn57642AlarmNo_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57642AlarmNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WtWebGraphAnalogIn57642AlarmNo_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57642AlarmNo_Object = MibTableColumn
wtWebGraphAnalogIn57642AlarmNo = _WtWebGraphAnalogIn57642AlarmNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 5, 2, 1, 1),
    _WtWebGraphAnalogIn57642AlarmNo_Type()
)
wtWebGraphAnalogIn57642AlarmNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642AlarmNo.setStatus("mandatory")
_WtWebGraphAnalogIn57642AlarmTable_Object = MibTable
wtWebGraphAnalogIn57642AlarmTable = _WtWebGraphAnalogIn57642AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 5, 3)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642AlarmTable.setStatus("mandatory")
_WtWebGraphAnalogIn57642AlarmEntry_Object = MibTableRow
wtWebGraphAnalogIn57642AlarmEntry = _WtWebGraphAnalogIn57642AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 5, 3, 1)
)
wtWebGraphAnalogIn57642AlarmEntry.setIndexNames(
    (0, "WebGraph-AnalogIn-57642-US-MIB", "wtWebGraphAnalogIn57642AlarmNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642AlarmEntry.setStatus("mandatory")


class _WtWebGraphAnalogIn57642AlarmTrigger_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57642AlarmTrigger based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphAnalogIn57642AlarmTrigger_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57642AlarmTrigger_Object = MibTableColumn
wtWebGraphAnalogIn57642AlarmTrigger = _WtWebGraphAnalogIn57642AlarmTrigger_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 5, 3, 1, 1),
    _WtWebGraphAnalogIn57642AlarmTrigger_Type()
)
wtWebGraphAnalogIn57642AlarmTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642AlarmTrigger.setStatus("mandatory")
_WtWebGraphAnalogIn57642AlarmMin_Type = OctetString
_WtWebGraphAnalogIn57642AlarmMin_Object = MibTableColumn
wtWebGraphAnalogIn57642AlarmMin = _WtWebGraphAnalogIn57642AlarmMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 5, 3, 1, 2),
    _WtWebGraphAnalogIn57642AlarmMin_Type()
)
wtWebGraphAnalogIn57642AlarmMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642AlarmMin.setStatus("mandatory")
_WtWebGraphAnalogIn57642AlarmMax_Type = OctetString
_WtWebGraphAnalogIn57642AlarmMax_Object = MibTableColumn
wtWebGraphAnalogIn57642AlarmMax = _WtWebGraphAnalogIn57642AlarmMax_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 5, 3, 1, 3),
    _WtWebGraphAnalogIn57642AlarmMax_Type()
)
wtWebGraphAnalogIn57642AlarmMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642AlarmMax.setStatus("mandatory")
_WtWebGraphAnalogIn57642AlarmHysteresis_Type = OctetString
_WtWebGraphAnalogIn57642AlarmHysteresis_Object = MibTableColumn
wtWebGraphAnalogIn57642AlarmHysteresis = _WtWebGraphAnalogIn57642AlarmHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 5, 3, 1, 4),
    _WtWebGraphAnalogIn57642AlarmHysteresis_Type()
)
wtWebGraphAnalogIn57642AlarmHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642AlarmHysteresis.setStatus("mandatory")
_WtWebGraphAnalogIn57642AlarmDelay_Type = OctetString
_WtWebGraphAnalogIn57642AlarmDelay_Object = MibTableColumn
wtWebGraphAnalogIn57642AlarmDelay = _WtWebGraphAnalogIn57642AlarmDelay_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 5, 3, 1, 5),
    _WtWebGraphAnalogIn57642AlarmDelay_Type()
)
wtWebGraphAnalogIn57642AlarmDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642AlarmDelay.setStatus("mandatory")
_WtWebGraphAnalogIn57642AlarmInterval_Type = OctetString
_WtWebGraphAnalogIn57642AlarmInterval_Object = MibTableColumn
wtWebGraphAnalogIn57642AlarmInterval = _WtWebGraphAnalogIn57642AlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 5, 3, 1, 6),
    _WtWebGraphAnalogIn57642AlarmInterval_Type()
)
wtWebGraphAnalogIn57642AlarmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642AlarmInterval.setStatus("mandatory")


class _WtWebGraphAnalogIn57642AlarmEnable_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57642AlarmEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphAnalogIn57642AlarmEnable_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57642AlarmEnable_Object = MibTableColumn
wtWebGraphAnalogIn57642AlarmEnable = _WtWebGraphAnalogIn57642AlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 5, 3, 1, 7),
    _WtWebGraphAnalogIn57642AlarmEnable_Type()
)
wtWebGraphAnalogIn57642AlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642AlarmEnable.setStatus("mandatory")
_WtWebGraphAnalogIn57642AlarmEMailAddr_Type = OctetString
_WtWebGraphAnalogIn57642AlarmEMailAddr_Object = MibTableColumn
wtWebGraphAnalogIn57642AlarmEMailAddr = _WtWebGraphAnalogIn57642AlarmEMailAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 5, 3, 1, 8),
    _WtWebGraphAnalogIn57642AlarmEMailAddr_Type()
)
wtWebGraphAnalogIn57642AlarmEMailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642AlarmEMailAddr.setStatus("mandatory")
_WtWebGraphAnalogIn57642AlarmMailSubject_Type = OctetString
_WtWebGraphAnalogIn57642AlarmMailSubject_Object = MibTableColumn
wtWebGraphAnalogIn57642AlarmMailSubject = _WtWebGraphAnalogIn57642AlarmMailSubject_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 5, 3, 1, 9),
    _WtWebGraphAnalogIn57642AlarmMailSubject_Type()
)
wtWebGraphAnalogIn57642AlarmMailSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642AlarmMailSubject.setStatus("mandatory")
_WtWebGraphAnalogIn57642AlarmMailText_Type = OctetString
_WtWebGraphAnalogIn57642AlarmMailText_Object = MibTableColumn
wtWebGraphAnalogIn57642AlarmMailText = _WtWebGraphAnalogIn57642AlarmMailText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 5, 3, 1, 10),
    _WtWebGraphAnalogIn57642AlarmMailText_Type()
)
wtWebGraphAnalogIn57642AlarmMailText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642AlarmMailText.setStatus("mandatory")
_WtWebGraphAnalogIn57642AlarmManagerIP_Type = OctetString
_WtWebGraphAnalogIn57642AlarmManagerIP_Object = MibTableColumn
wtWebGraphAnalogIn57642AlarmManagerIP = _WtWebGraphAnalogIn57642AlarmManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 5, 3, 1, 11),
    _WtWebGraphAnalogIn57642AlarmManagerIP_Type()
)
wtWebGraphAnalogIn57642AlarmManagerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642AlarmManagerIP.setStatus("mandatory")
_WtWebGraphAnalogIn57642AlarmTrapText_Type = OctetString
_WtWebGraphAnalogIn57642AlarmTrapText_Object = MibTableColumn
wtWebGraphAnalogIn57642AlarmTrapText = _WtWebGraphAnalogIn57642AlarmTrapText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 5, 3, 1, 12),
    _WtWebGraphAnalogIn57642AlarmTrapText_Type()
)
wtWebGraphAnalogIn57642AlarmTrapText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642AlarmTrapText.setStatus("mandatory")


class _WtWebGraphAnalogIn57642AlarmMailOptions_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57642AlarmMailOptions based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphAnalogIn57642AlarmMailOptions_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57642AlarmMailOptions_Object = MibTableColumn
wtWebGraphAnalogIn57642AlarmMailOptions = _WtWebGraphAnalogIn57642AlarmMailOptions_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 5, 3, 1, 13),
    _WtWebGraphAnalogIn57642AlarmMailOptions_Type()
)
wtWebGraphAnalogIn57642AlarmMailOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642AlarmMailOptions.setStatus("mandatory")
_WtWebGraphAnalogIn57642AlarmTcpIpAddr_Type = OctetString
_WtWebGraphAnalogIn57642AlarmTcpIpAddr_Object = MibTableColumn
wtWebGraphAnalogIn57642AlarmTcpIpAddr = _WtWebGraphAnalogIn57642AlarmTcpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 5, 3, 1, 14),
    _WtWebGraphAnalogIn57642AlarmTcpIpAddr_Type()
)
wtWebGraphAnalogIn57642AlarmTcpIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642AlarmTcpIpAddr.setStatus("mandatory")


class _WtWebGraphAnalogIn57642AlarmTcpPort_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57642AlarmTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalogIn57642AlarmTcpPort_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57642AlarmTcpPort_Object = MibTableColumn
wtWebGraphAnalogIn57642AlarmTcpPort = _WtWebGraphAnalogIn57642AlarmTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 5, 3, 1, 15),
    _WtWebGraphAnalogIn57642AlarmTcpPort_Type()
)
wtWebGraphAnalogIn57642AlarmTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642AlarmTcpPort.setStatus("mandatory")
_WtWebGraphAnalogIn57642AlarmTcpText_Type = OctetString
_WtWebGraphAnalogIn57642AlarmTcpText_Object = MibTableColumn
wtWebGraphAnalogIn57642AlarmTcpText = _WtWebGraphAnalogIn57642AlarmTcpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 5, 3, 1, 16),
    _WtWebGraphAnalogIn57642AlarmTcpText_Type()
)
wtWebGraphAnalogIn57642AlarmTcpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642AlarmTcpText.setStatus("mandatory")
_WtWebGraphAnalogIn57642AlarmClearMailSubject_Type = OctetString
_WtWebGraphAnalogIn57642AlarmClearMailSubject_Object = MibTableColumn
wtWebGraphAnalogIn57642AlarmClearMailSubject = _WtWebGraphAnalogIn57642AlarmClearMailSubject_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 5, 3, 1, 17),
    _WtWebGraphAnalogIn57642AlarmClearMailSubject_Type()
)
wtWebGraphAnalogIn57642AlarmClearMailSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642AlarmClearMailSubject.setStatus("mandatory")
_WtWebGraphAnalogIn57642AlarmClearMailText_Type = OctetString
_WtWebGraphAnalogIn57642AlarmClearMailText_Object = MibTableColumn
wtWebGraphAnalogIn57642AlarmClearMailText = _WtWebGraphAnalogIn57642AlarmClearMailText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 5, 3, 1, 18),
    _WtWebGraphAnalogIn57642AlarmClearMailText_Type()
)
wtWebGraphAnalogIn57642AlarmClearMailText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642AlarmClearMailText.setStatus("mandatory")
_WtWebGraphAnalogIn57642AlarmClearTrapText_Type = OctetString
_WtWebGraphAnalogIn57642AlarmClearTrapText_Object = MibTableColumn
wtWebGraphAnalogIn57642AlarmClearTrapText = _WtWebGraphAnalogIn57642AlarmClearTrapText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 5, 3, 1, 19),
    _WtWebGraphAnalogIn57642AlarmClearTrapText_Type()
)
wtWebGraphAnalogIn57642AlarmClearTrapText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642AlarmClearTrapText.setStatus("mandatory")
_WtWebGraphAnalogIn57642AlarmClearTcpText_Type = OctetString
_WtWebGraphAnalogIn57642AlarmClearTcpText_Object = MibTableColumn
wtWebGraphAnalogIn57642AlarmClearTcpText = _WtWebGraphAnalogIn57642AlarmClearTcpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 5, 3, 1, 20),
    _WtWebGraphAnalogIn57642AlarmClearTcpText_Type()
)
wtWebGraphAnalogIn57642AlarmClearTcpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642AlarmClearTcpText.setStatus("mandatory")
_WtWebGraphAnalogIn57642Alarm2Min_Type = OctetString
_WtWebGraphAnalogIn57642Alarm2Min_Object = MibTableColumn
wtWebGraphAnalogIn57642Alarm2Min = _WtWebGraphAnalogIn57642Alarm2Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 5, 3, 1, 21),
    _WtWebGraphAnalogIn57642Alarm2Min_Type()
)
wtWebGraphAnalogIn57642Alarm2Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642Alarm2Min.setStatus("mandatory")
_WtWebGraphAnalogIn57642Alarm2Max_Type = OctetString
_WtWebGraphAnalogIn57642Alarm2Max_Object = MibTableColumn
wtWebGraphAnalogIn57642Alarm2Max = _WtWebGraphAnalogIn57642Alarm2Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 5, 3, 1, 22),
    _WtWebGraphAnalogIn57642Alarm2Max_Type()
)
wtWebGraphAnalogIn57642Alarm2Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642Alarm2Max.setStatus("mandatory")
_WtWebGraphAnalogIn57642Alarm2Hysteresis_Type = OctetString
_WtWebGraphAnalogIn57642Alarm2Hysteresis_Object = MibTableColumn
wtWebGraphAnalogIn57642Alarm2Hysteresis = _WtWebGraphAnalogIn57642Alarm2Hysteresis_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 5, 3, 1, 23),
    _WtWebGraphAnalogIn57642Alarm2Hysteresis_Type()
)
wtWebGraphAnalogIn57642Alarm2Hysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642Alarm2Hysteresis.setStatus("mandatory")
_WtWebGraphAnalogIn57642AlarmSyslogIpAddr_Type = OctetString
_WtWebGraphAnalogIn57642AlarmSyslogIpAddr_Object = MibTableColumn
wtWebGraphAnalogIn57642AlarmSyslogIpAddr = _WtWebGraphAnalogIn57642AlarmSyslogIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 5, 3, 1, 24),
    _WtWebGraphAnalogIn57642AlarmSyslogIpAddr_Type()
)
wtWebGraphAnalogIn57642AlarmSyslogIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642AlarmSyslogIpAddr.setStatus("mandatory")


class _WtWebGraphAnalogIn57642AlarmSyslogPort_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57642AlarmSyslogPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalogIn57642AlarmSyslogPort_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57642AlarmSyslogPort_Object = MibTableColumn
wtWebGraphAnalogIn57642AlarmSyslogPort = _WtWebGraphAnalogIn57642AlarmSyslogPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 5, 3, 1, 25),
    _WtWebGraphAnalogIn57642AlarmSyslogPort_Type()
)
wtWebGraphAnalogIn57642AlarmSyslogPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642AlarmSyslogPort.setStatus("mandatory")
_WtWebGraphAnalogIn57642AlarmSyslogText_Type = OctetString
_WtWebGraphAnalogIn57642AlarmSyslogText_Object = MibTableColumn
wtWebGraphAnalogIn57642AlarmSyslogText = _WtWebGraphAnalogIn57642AlarmSyslogText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 5, 3, 1, 26),
    _WtWebGraphAnalogIn57642AlarmSyslogText_Type()
)
wtWebGraphAnalogIn57642AlarmSyslogText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642AlarmSyslogText.setStatus("mandatory")
_WtWebGraphAnalogIn57642AlarmSyslogClearText_Type = OctetString
_WtWebGraphAnalogIn57642AlarmSyslogClearText_Object = MibTableColumn
wtWebGraphAnalogIn57642AlarmSyslogClearText = _WtWebGraphAnalogIn57642AlarmSyslogClearText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 5, 3, 1, 27),
    _WtWebGraphAnalogIn57642AlarmSyslogClearText_Type()
)
wtWebGraphAnalogIn57642AlarmSyslogClearText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642AlarmSyslogClearText.setStatus("mandatory")
_WtWebGraphAnalogIn57642AlarmFtpDataPort_Type = OctetString
_WtWebGraphAnalogIn57642AlarmFtpDataPort_Object = MibTableColumn
wtWebGraphAnalogIn57642AlarmFtpDataPort = _WtWebGraphAnalogIn57642AlarmFtpDataPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 5, 3, 1, 28),
    _WtWebGraphAnalogIn57642AlarmFtpDataPort_Type()
)
wtWebGraphAnalogIn57642AlarmFtpDataPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642AlarmFtpDataPort.setStatus("mandatory")
_WtWebGraphAnalogIn57642AlarmFtpFileName_Type = OctetString
_WtWebGraphAnalogIn57642AlarmFtpFileName_Object = MibTableColumn
wtWebGraphAnalogIn57642AlarmFtpFileName = _WtWebGraphAnalogIn57642AlarmFtpFileName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 5, 3, 1, 29),
    _WtWebGraphAnalogIn57642AlarmFtpFileName_Type()
)
wtWebGraphAnalogIn57642AlarmFtpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642AlarmFtpFileName.setStatus("mandatory")
_WtWebGraphAnalogIn57642AlarmFtpText_Type = OctetString
_WtWebGraphAnalogIn57642AlarmFtpText_Object = MibTableColumn
wtWebGraphAnalogIn57642AlarmFtpText = _WtWebGraphAnalogIn57642AlarmFtpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 5, 3, 1, 30),
    _WtWebGraphAnalogIn57642AlarmFtpText_Type()
)
wtWebGraphAnalogIn57642AlarmFtpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642AlarmFtpText.setStatus("mandatory")
_WtWebGraphAnalogIn57642AlarmFtpClearText_Type = OctetString
_WtWebGraphAnalogIn57642AlarmFtpClearText_Object = MibTableColumn
wtWebGraphAnalogIn57642AlarmFtpClearText = _WtWebGraphAnalogIn57642AlarmFtpClearText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 5, 3, 1, 31),
    _WtWebGraphAnalogIn57642AlarmFtpClearText_Type()
)
wtWebGraphAnalogIn57642AlarmFtpClearText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642AlarmFtpClearText.setStatus("mandatory")


class _WtWebGraphAnalogIn57642AlarmFtpOption_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57642AlarmFtpOption based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphAnalogIn57642AlarmFtpOption_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57642AlarmFtpOption_Object = MibTableColumn
wtWebGraphAnalogIn57642AlarmFtpOption = _WtWebGraphAnalogIn57642AlarmFtpOption_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 5, 3, 1, 32),
    _WtWebGraphAnalogIn57642AlarmFtpOption_Type()
)
wtWebGraphAnalogIn57642AlarmFtpOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642AlarmFtpOption.setStatus("mandatory")
_WtWebGraphAnalogIn57642AlarmTimerCron_Type = OctetString
_WtWebGraphAnalogIn57642AlarmTimerCron_Object = MibTableColumn
wtWebGraphAnalogIn57642AlarmTimerCron = _WtWebGraphAnalogIn57642AlarmTimerCron_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 5, 3, 1, 33),
    _WtWebGraphAnalogIn57642AlarmTimerCron_Type()
)
wtWebGraphAnalogIn57642AlarmTimerCron.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642AlarmTimerCron.setStatus("mandatory")
_WtWebGraphAnalogIn57642Graphics_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57642Graphics = _WtWebGraphAnalogIn57642Graphics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 6)
)
_WtWebGraphAnalogIn57642GraphicsBase_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57642GraphicsBase = _WtWebGraphAnalogIn57642GraphicsBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 6, 1)
)
_WtWebGraphAnalogIn57642GraphicsBaseEnable_Type = OctetString
_WtWebGraphAnalogIn57642GraphicsBaseEnable_Object = MibScalar
wtWebGraphAnalogIn57642GraphicsBaseEnable = _WtWebGraphAnalogIn57642GraphicsBaseEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 6, 1, 1),
    _WtWebGraphAnalogIn57642GraphicsBaseEnable_Type()
)
wtWebGraphAnalogIn57642GraphicsBaseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642GraphicsBaseEnable.setStatus("mandatory")
_WtWebGraphAnalogIn57642GraphicsBaseWidth_Type = Integer32
_WtWebGraphAnalogIn57642GraphicsBaseWidth_Object = MibScalar
wtWebGraphAnalogIn57642GraphicsBaseWidth = _WtWebGraphAnalogIn57642GraphicsBaseWidth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 6, 1, 2),
    _WtWebGraphAnalogIn57642GraphicsBaseWidth_Type()
)
wtWebGraphAnalogIn57642GraphicsBaseWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642GraphicsBaseWidth.setStatus("mandatory")
_WtWebGraphAnalogIn57642GraphicsBaseHeight_Type = Integer32
_WtWebGraphAnalogIn57642GraphicsBaseHeight_Object = MibScalar
wtWebGraphAnalogIn57642GraphicsBaseHeight = _WtWebGraphAnalogIn57642GraphicsBaseHeight_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 6, 1, 3),
    _WtWebGraphAnalogIn57642GraphicsBaseHeight_Type()
)
wtWebGraphAnalogIn57642GraphicsBaseHeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642GraphicsBaseHeight.setStatus("mandatory")


class _WtWebGraphAnalogIn57642GraphicsBaseFrameColor_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57642GraphicsBaseFrameColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_WtWebGraphAnalogIn57642GraphicsBaseFrameColor_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57642GraphicsBaseFrameColor_Object = MibScalar
wtWebGraphAnalogIn57642GraphicsBaseFrameColor = _WtWebGraphAnalogIn57642GraphicsBaseFrameColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 6, 1, 4),
    _WtWebGraphAnalogIn57642GraphicsBaseFrameColor_Type()
)
wtWebGraphAnalogIn57642GraphicsBaseFrameColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642GraphicsBaseFrameColor.setStatus("mandatory")


class _WtWebGraphAnalogIn57642GraphicsBaseBackgroundColor_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57642GraphicsBaseBackgroundColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_WtWebGraphAnalogIn57642GraphicsBaseBackgroundColor_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57642GraphicsBaseBackgroundColor_Object = MibScalar
wtWebGraphAnalogIn57642GraphicsBaseBackgroundColor = _WtWebGraphAnalogIn57642GraphicsBaseBackgroundColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 6, 1, 5),
    _WtWebGraphAnalogIn57642GraphicsBaseBackgroundColor_Type()
)
wtWebGraphAnalogIn57642GraphicsBaseBackgroundColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642GraphicsBaseBackgroundColor.setStatus("mandatory")
_WtWebGraphAnalogIn57642GraphicsBasePollingrate_Type = Integer32
_WtWebGraphAnalogIn57642GraphicsBasePollingrate_Object = MibScalar
wtWebGraphAnalogIn57642GraphicsBasePollingrate = _WtWebGraphAnalogIn57642GraphicsBasePollingrate_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 6, 1, 6),
    _WtWebGraphAnalogIn57642GraphicsBasePollingrate_Type()
)
wtWebGraphAnalogIn57642GraphicsBasePollingrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642GraphicsBasePollingrate.setStatus("mandatory")
_WtWebGraphAnalogIn57642GraphicsSelect_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57642GraphicsSelect = _WtWebGraphAnalogIn57642GraphicsSelect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 6, 2)
)


class _WtWebGraphAnalogIn57642GraphicsSelectDisplaySensorSel_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57642GraphicsSelectDisplaySensorSel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphAnalogIn57642GraphicsSelectDisplaySensorSel_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57642GraphicsSelectDisplaySensorSel_Object = MibScalar
wtWebGraphAnalogIn57642GraphicsSelectDisplaySensorSel = _WtWebGraphAnalogIn57642GraphicsSelectDisplaySensorSel_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 6, 2, 1),
    _WtWebGraphAnalogIn57642GraphicsSelectDisplaySensorSel_Type()
)
wtWebGraphAnalogIn57642GraphicsSelectDisplaySensorSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642GraphicsSelectDisplaySensorSel.setStatus("mandatory")


class _WtWebGraphAnalogIn57642GraphicsSelectDisplayShowExtrem_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57642GraphicsSelectDisplayShowExtrem based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphAnalogIn57642GraphicsSelectDisplayShowExtrem_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57642GraphicsSelectDisplayShowExtrem_Object = MibScalar
wtWebGraphAnalogIn57642GraphicsSelectDisplayShowExtrem = _WtWebGraphAnalogIn57642GraphicsSelectDisplayShowExtrem_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 6, 2, 2),
    _WtWebGraphAnalogIn57642GraphicsSelectDisplayShowExtrem_Type()
)
wtWebGraphAnalogIn57642GraphicsSelectDisplayShowExtrem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642GraphicsSelectDisplayShowExtrem.setStatus("mandatory")
_WtWebGraphAnalogIn57642SensorColor2Table_Object = MibTable
wtWebGraphAnalogIn57642SensorColor2Table = _WtWebGraphAnalogIn57642SensorColor2Table_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 6, 2, 3)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642SensorColor2Table.setStatus("mandatory")
_WtWebGraphAnalogIn57642SensorColor2Entry_Object = MibTableRow
wtWebGraphAnalogIn57642SensorColor2Entry = _WtWebGraphAnalogIn57642SensorColor2Entry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 6, 2, 3, 1)
)
wtWebGraphAnalogIn57642SensorColor2Entry.setIndexNames(
    (0, "WebGraph-AnalogIn-57642-US-MIB", "wtWebGraphAnalogIn57642SensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642SensorColor2Entry.setStatus("mandatory")


class _WtWebGraphAnalogIn57642GraphicsSensorColor_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57642GraphicsSensorColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_WtWebGraphAnalogIn57642GraphicsSensorColor_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57642GraphicsSensorColor_Object = MibTableColumn
wtWebGraphAnalogIn57642GraphicsSensorColor = _WtWebGraphAnalogIn57642GraphicsSensorColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 6, 2, 3, 1, 1),
    _WtWebGraphAnalogIn57642GraphicsSensorColor_Type()
)
wtWebGraphAnalogIn57642GraphicsSensorColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642GraphicsSensorColor.setStatus("mandatory")
_WtWebGraphAnalogIn57642GraphicsSelectScale_Type = OctetString
_WtWebGraphAnalogIn57642GraphicsSelectScale_Object = MibTableColumn
wtWebGraphAnalogIn57642GraphicsSelectScale = _WtWebGraphAnalogIn57642GraphicsSelectScale_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 6, 2, 3, 1, 2),
    _WtWebGraphAnalogIn57642GraphicsSelectScale_Type()
)
wtWebGraphAnalogIn57642GraphicsSelectScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642GraphicsSelectScale.setStatus("mandatory")
_WtWebGraphAnalogIn57642GraphicsScale_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57642GraphicsScale = _WtWebGraphAnalogIn57642GraphicsScale_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 6, 3)
)
_WtWebGraphAnalogIn57642GraphicsScaleAutoScaleEnable_Type = OctetString
_WtWebGraphAnalogIn57642GraphicsScaleAutoScaleEnable_Object = MibScalar
wtWebGraphAnalogIn57642GraphicsScaleAutoScaleEnable = _WtWebGraphAnalogIn57642GraphicsScaleAutoScaleEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 6, 3, 1),
    _WtWebGraphAnalogIn57642GraphicsScaleAutoScaleEnable_Type()
)
wtWebGraphAnalogIn57642GraphicsScaleAutoScaleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642GraphicsScaleAutoScaleEnable.setStatus("mandatory")
_WtWebGraphAnalogIn57642GraphicsScaleAutoFitEnable_Type = OctetString
_WtWebGraphAnalogIn57642GraphicsScaleAutoFitEnable_Object = MibScalar
wtWebGraphAnalogIn57642GraphicsScaleAutoFitEnable = _WtWebGraphAnalogIn57642GraphicsScaleAutoFitEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 6, 3, 2),
    _WtWebGraphAnalogIn57642GraphicsScaleAutoFitEnable_Type()
)
wtWebGraphAnalogIn57642GraphicsScaleAutoFitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642GraphicsScaleAutoFitEnable.setStatus("mandatory")
_WtWebGraphAnalogIn57642GraphicsScale1Min_Type = Integer32
_WtWebGraphAnalogIn57642GraphicsScale1Min_Object = MibScalar
wtWebGraphAnalogIn57642GraphicsScale1Min = _WtWebGraphAnalogIn57642GraphicsScale1Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 6, 3, 3),
    _WtWebGraphAnalogIn57642GraphicsScale1Min_Type()
)
wtWebGraphAnalogIn57642GraphicsScale1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642GraphicsScale1Min.setStatus("mandatory")
_WtWebGraphAnalogIn57642GraphicsScale2Min_Type = Integer32
_WtWebGraphAnalogIn57642GraphicsScale2Min_Object = MibScalar
wtWebGraphAnalogIn57642GraphicsScale2Min = _WtWebGraphAnalogIn57642GraphicsScale2Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 6, 3, 4),
    _WtWebGraphAnalogIn57642GraphicsScale2Min_Type()
)
wtWebGraphAnalogIn57642GraphicsScale2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642GraphicsScale2Min.setStatus("mandatory")
_WtWebGraphAnalogIn57642GraphicsScale3Min_Type = Integer32
_WtWebGraphAnalogIn57642GraphicsScale3Min_Object = MibScalar
wtWebGraphAnalogIn57642GraphicsScale3Min = _WtWebGraphAnalogIn57642GraphicsScale3Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 6, 3, 5),
    _WtWebGraphAnalogIn57642GraphicsScale3Min_Type()
)
wtWebGraphAnalogIn57642GraphicsScale3Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642GraphicsScale3Min.setStatus("mandatory")
_WtWebGraphAnalogIn57642GraphicsScale4Min_Type = Integer32
_WtWebGraphAnalogIn57642GraphicsScale4Min_Object = MibScalar
wtWebGraphAnalogIn57642GraphicsScale4Min = _WtWebGraphAnalogIn57642GraphicsScale4Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 6, 3, 6),
    _WtWebGraphAnalogIn57642GraphicsScale4Min_Type()
)
wtWebGraphAnalogIn57642GraphicsScale4Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642GraphicsScale4Min.setStatus("mandatory")
_WtWebGraphAnalogIn57642GraphicsScale1Max_Type = Integer32
_WtWebGraphAnalogIn57642GraphicsScale1Max_Object = MibScalar
wtWebGraphAnalogIn57642GraphicsScale1Max = _WtWebGraphAnalogIn57642GraphicsScale1Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 6, 3, 7),
    _WtWebGraphAnalogIn57642GraphicsScale1Max_Type()
)
wtWebGraphAnalogIn57642GraphicsScale1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642GraphicsScale1Max.setStatus("mandatory")
_WtWebGraphAnalogIn57642GraphicsScale2Max_Type = Integer32
_WtWebGraphAnalogIn57642GraphicsScale2Max_Object = MibScalar
wtWebGraphAnalogIn57642GraphicsScale2Max = _WtWebGraphAnalogIn57642GraphicsScale2Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 6, 3, 8),
    _WtWebGraphAnalogIn57642GraphicsScale2Max_Type()
)
wtWebGraphAnalogIn57642GraphicsScale2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642GraphicsScale2Max.setStatus("mandatory")
_WtWebGraphAnalogIn57642GraphicsScale3Max_Type = Integer32
_WtWebGraphAnalogIn57642GraphicsScale3Max_Object = MibScalar
wtWebGraphAnalogIn57642GraphicsScale3Max = _WtWebGraphAnalogIn57642GraphicsScale3Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 6, 3, 9),
    _WtWebGraphAnalogIn57642GraphicsScale3Max_Type()
)
wtWebGraphAnalogIn57642GraphicsScale3Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642GraphicsScale3Max.setStatus("mandatory")
_WtWebGraphAnalogIn57642GraphicsScale4Max_Type = Integer32
_WtWebGraphAnalogIn57642GraphicsScale4Max_Object = MibScalar
wtWebGraphAnalogIn57642GraphicsScale4Max = _WtWebGraphAnalogIn57642GraphicsScale4Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 6, 3, 10),
    _WtWebGraphAnalogIn57642GraphicsScale4Max_Type()
)
wtWebGraphAnalogIn57642GraphicsScale4Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642GraphicsScale4Max.setStatus("mandatory")
_WtWebGraphAnalogIn57642GraphicsScale1Unit_Type = OctetString
_WtWebGraphAnalogIn57642GraphicsScale1Unit_Object = MibScalar
wtWebGraphAnalogIn57642GraphicsScale1Unit = _WtWebGraphAnalogIn57642GraphicsScale1Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 6, 3, 11),
    _WtWebGraphAnalogIn57642GraphicsScale1Unit_Type()
)
wtWebGraphAnalogIn57642GraphicsScale1Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642GraphicsScale1Unit.setStatus("mandatory")
_WtWebGraphAnalogIn57642GraphicsScale2Unit_Type = OctetString
_WtWebGraphAnalogIn57642GraphicsScale2Unit_Object = MibScalar
wtWebGraphAnalogIn57642GraphicsScale2Unit = _WtWebGraphAnalogIn57642GraphicsScale2Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 6, 3, 12),
    _WtWebGraphAnalogIn57642GraphicsScale2Unit_Type()
)
wtWebGraphAnalogIn57642GraphicsScale2Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642GraphicsScale2Unit.setStatus("mandatory")
_WtWebGraphAnalogIn57642GraphicsScale3Unit_Type = OctetString
_WtWebGraphAnalogIn57642GraphicsScale3Unit_Object = MibScalar
wtWebGraphAnalogIn57642GraphicsScale3Unit = _WtWebGraphAnalogIn57642GraphicsScale3Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 6, 3, 13),
    _WtWebGraphAnalogIn57642GraphicsScale3Unit_Type()
)
wtWebGraphAnalogIn57642GraphicsScale3Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642GraphicsScale3Unit.setStatus("mandatory")
_WtWebGraphAnalogIn57642GraphicsScale4Unit_Type = OctetString
_WtWebGraphAnalogIn57642GraphicsScale4Unit_Object = MibScalar
wtWebGraphAnalogIn57642GraphicsScale4Unit = _WtWebGraphAnalogIn57642GraphicsScale4Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 1, 6, 3, 14),
    _WtWebGraphAnalogIn57642GraphicsScale4Unit_Type()
)
wtWebGraphAnalogIn57642GraphicsScale4Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642GraphicsScale4Unit.setStatus("mandatory")
_WtWebGraphAnalogIn57642Ports_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57642Ports = _WtWebGraphAnalogIn57642Ports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 2)
)
_WtWebGraphAnalogIn57642PortTable_Object = MibTable
wtWebGraphAnalogIn57642PortTable = _WtWebGraphAnalogIn57642PortTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 2, 1)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642PortTable.setStatus("mandatory")
_WtWebGraphAnalogIn57642PortEntry_Object = MibTableRow
wtWebGraphAnalogIn57642PortEntry = _WtWebGraphAnalogIn57642PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 2, 1, 1)
)
wtWebGraphAnalogIn57642PortEntry.setIndexNames(
    (0, "WebGraph-AnalogIn-57642-US-MIB", "wtWebGraphAnalogIn57642SensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642PortEntry.setStatus("mandatory")
_WtWebGraphAnalogIn57642PortName_Type = OctetString
_WtWebGraphAnalogIn57642PortName_Object = MibTableColumn
wtWebGraphAnalogIn57642PortName = _WtWebGraphAnalogIn57642PortName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 2, 1, 1, 1),
    _WtWebGraphAnalogIn57642PortName_Type()
)
wtWebGraphAnalogIn57642PortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642PortName.setStatus("mandatory")
_WtWebGraphAnalogIn57642PortText_Type = OctetString
_WtWebGraphAnalogIn57642PortText_Object = MibTableColumn
wtWebGraphAnalogIn57642PortText = _WtWebGraphAnalogIn57642PortText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 2, 1, 1, 2),
    _WtWebGraphAnalogIn57642PortText_Type()
)
wtWebGraphAnalogIn57642PortText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642PortText.setStatus("mandatory")
_WtWebGraphAnalogIn57642PortOffset1_Type = OctetString
_WtWebGraphAnalogIn57642PortOffset1_Object = MibTableColumn
wtWebGraphAnalogIn57642PortOffset1 = _WtWebGraphAnalogIn57642PortOffset1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 2, 1, 1, 3),
    _WtWebGraphAnalogIn57642PortOffset1_Type()
)
wtWebGraphAnalogIn57642PortOffset1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642PortOffset1.setStatus("mandatory")
_WtWebGraphAnalogIn57642SetPoint1_Type = OctetString
_WtWebGraphAnalogIn57642SetPoint1_Object = MibTableColumn
wtWebGraphAnalogIn57642SetPoint1 = _WtWebGraphAnalogIn57642SetPoint1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 2, 1, 1, 4),
    _WtWebGraphAnalogIn57642SetPoint1_Type()
)
wtWebGraphAnalogIn57642SetPoint1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642SetPoint1.setStatus("mandatory")
_WtWebGraphAnalogIn57642PortOffset2_Type = OctetString
_WtWebGraphAnalogIn57642PortOffset2_Object = MibTableColumn
wtWebGraphAnalogIn57642PortOffset2 = _WtWebGraphAnalogIn57642PortOffset2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 2, 1, 1, 5),
    _WtWebGraphAnalogIn57642PortOffset2_Type()
)
wtWebGraphAnalogIn57642PortOffset2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642PortOffset2.setStatus("mandatory")
_WtWebGraphAnalogIn57642SetPoint2_Type = OctetString
_WtWebGraphAnalogIn57642SetPoint2_Object = MibTableColumn
wtWebGraphAnalogIn57642SetPoint2 = _WtWebGraphAnalogIn57642SetPoint2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 2, 1, 1, 6),
    _WtWebGraphAnalogIn57642SetPoint2_Type()
)
wtWebGraphAnalogIn57642SetPoint2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642SetPoint2.setStatus("mandatory")
_WtWebGraphAnalogIn57642PortComment_Type = OctetString
_WtWebGraphAnalogIn57642PortComment_Object = MibTableColumn
wtWebGraphAnalogIn57642PortComment = _WtWebGraphAnalogIn57642PortComment_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 2, 1, 1, 7),
    _WtWebGraphAnalogIn57642PortComment_Type()
)
wtWebGraphAnalogIn57642PortComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642PortComment.setStatus("mandatory")


class _WtWebGraphAnalogIn57642PortSensorSelect_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57642PortSensorSelect based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphAnalogIn57642PortSensorSelect_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57642PortSensorSelect_Object = MibTableColumn
wtWebGraphAnalogIn57642PortSensorSelect = _WtWebGraphAnalogIn57642PortSensorSelect_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 2, 1, 1, 8),
    _WtWebGraphAnalogIn57642PortSensorSelect_Type()
)
wtWebGraphAnalogIn57642PortSensorSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642PortSensorSelect.setStatus("mandatory")
_WtWebGraphAnalogIn57642PortUnit_Type = OctetString
_WtWebGraphAnalogIn57642PortUnit_Object = MibTableColumn
wtWebGraphAnalogIn57642PortUnit = _WtWebGraphAnalogIn57642PortUnit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 2, 1, 1, 9),
    _WtWebGraphAnalogIn57642PortUnit_Type()
)
wtWebGraphAnalogIn57642PortUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642PortUnit.setStatus("mandatory")
_WtWebGraphAnalogIn57642PortScale0_Type = OctetString
_WtWebGraphAnalogIn57642PortScale0_Object = MibTableColumn
wtWebGraphAnalogIn57642PortScale0 = _WtWebGraphAnalogIn57642PortScale0_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 2, 1, 1, 10),
    _WtWebGraphAnalogIn57642PortScale0_Type()
)
wtWebGraphAnalogIn57642PortScale0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642PortScale0.setStatus("mandatory")
_WtWebGraphAnalogIn57642PortScale100_Type = OctetString
_WtWebGraphAnalogIn57642PortScale100_Object = MibTableColumn
wtWebGraphAnalogIn57642PortScale100 = _WtWebGraphAnalogIn57642PortScale100_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 2, 1, 1, 11),
    _WtWebGraphAnalogIn57642PortScale100_Type()
)
wtWebGraphAnalogIn57642PortScale100.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642PortScale100.setStatus("mandatory")
_WtWebGraphAnalogIn57642Manufact_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57642Manufact = _WtWebGraphAnalogIn57642Manufact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 3)
)
_WtWebGraphAnalogIn57642MfName_Type = OctetString
_WtWebGraphAnalogIn57642MfName_Object = MibScalar
wtWebGraphAnalogIn57642MfName = _WtWebGraphAnalogIn57642MfName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 3, 1),
    _WtWebGraphAnalogIn57642MfName_Type()
)
wtWebGraphAnalogIn57642MfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642MfName.setStatus("mandatory")
_WtWebGraphAnalogIn57642MfAddr_Type = OctetString
_WtWebGraphAnalogIn57642MfAddr_Object = MibScalar
wtWebGraphAnalogIn57642MfAddr = _WtWebGraphAnalogIn57642MfAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 3, 2),
    _WtWebGraphAnalogIn57642MfAddr_Type()
)
wtWebGraphAnalogIn57642MfAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642MfAddr.setStatus("mandatory")
_WtWebGraphAnalogIn57642MfHotline_Type = OctetString
_WtWebGraphAnalogIn57642MfHotline_Object = MibScalar
wtWebGraphAnalogIn57642MfHotline = _WtWebGraphAnalogIn57642MfHotline_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 3, 3),
    _WtWebGraphAnalogIn57642MfHotline_Type()
)
wtWebGraphAnalogIn57642MfHotline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642MfHotline.setStatus("mandatory")
_WtWebGraphAnalogIn57642MfInternet_Type = OctetString
_WtWebGraphAnalogIn57642MfInternet_Object = MibScalar
wtWebGraphAnalogIn57642MfInternet = _WtWebGraphAnalogIn57642MfInternet_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 3, 4),
    _WtWebGraphAnalogIn57642MfInternet_Type()
)
wtWebGraphAnalogIn57642MfInternet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642MfInternet.setStatus("mandatory")
_WtWebGraphAnalogIn57642MfDeviceTyp_Type = OctetString
_WtWebGraphAnalogIn57642MfDeviceTyp_Object = MibScalar
wtWebGraphAnalogIn57642MfDeviceTyp = _WtWebGraphAnalogIn57642MfDeviceTyp_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 3, 5),
    _WtWebGraphAnalogIn57642MfDeviceTyp_Type()
)
wtWebGraphAnalogIn57642MfDeviceTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642MfDeviceTyp.setStatus("mandatory")
_WtWebGraphAnalogIn57642MfOrderNo_Type = OctetString
_WtWebGraphAnalogIn57642MfOrderNo_Object = MibScalar
wtWebGraphAnalogIn57642MfOrderNo = _WtWebGraphAnalogIn57642MfOrderNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 3, 3, 6),
    _WtWebGraphAnalogIn57642MfOrderNo_Type()
)
wtWebGraphAnalogIn57642MfOrderNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642MfOrderNo.setStatus("mandatory")
_WtWebGraphAnalogIn57642Diag_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57642Diag = _WtWebGraphAnalogIn57642Diag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 4)
)
_WtWebGraphAnalogIn57642DiagErrorCount_Type = Integer32
_WtWebGraphAnalogIn57642DiagErrorCount_Object = MibScalar
wtWebGraphAnalogIn57642DiagErrorCount = _WtWebGraphAnalogIn57642DiagErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 4, 1),
    _WtWebGraphAnalogIn57642DiagErrorCount_Type()
)
wtWebGraphAnalogIn57642DiagErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642DiagErrorCount.setStatus("mandatory")
_WtWebGraphAnalogIn57642DiagBinaryError_Type = OctetString
_WtWebGraphAnalogIn57642DiagBinaryError_Object = MibScalar
wtWebGraphAnalogIn57642DiagBinaryError = _WtWebGraphAnalogIn57642DiagBinaryError_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 4, 2),
    _WtWebGraphAnalogIn57642DiagBinaryError_Type()
)
wtWebGraphAnalogIn57642DiagBinaryError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642DiagBinaryError.setStatus("mandatory")
_WtWebGraphAnalogIn57642DiagErrorIndex_Type = Integer32
_WtWebGraphAnalogIn57642DiagErrorIndex_Object = MibScalar
wtWebGraphAnalogIn57642DiagErrorIndex = _WtWebGraphAnalogIn57642DiagErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 4, 3),
    _WtWebGraphAnalogIn57642DiagErrorIndex_Type()
)
wtWebGraphAnalogIn57642DiagErrorIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642DiagErrorIndex.setStatus("mandatory")
_WtWebGraphAnalogIn57642DiagErrorMessage_Type = OctetString
_WtWebGraphAnalogIn57642DiagErrorMessage_Object = MibScalar
wtWebGraphAnalogIn57642DiagErrorMessage = _WtWebGraphAnalogIn57642DiagErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 4, 4),
    _WtWebGraphAnalogIn57642DiagErrorMessage_Type()
)
wtWebGraphAnalogIn57642DiagErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642DiagErrorMessage.setStatus("mandatory")
_WtWebGraphAnalogIn57642DiagErrorClear_Type = Integer32
_WtWebGraphAnalogIn57642DiagErrorClear_Object = MibScalar
wtWebGraphAnalogIn57642DiagErrorClear = _WtWebGraphAnalogIn57642DiagErrorClear_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 4, 5),
    _WtWebGraphAnalogIn57642DiagErrorClear_Type()
)
wtWebGraphAnalogIn57642DiagErrorClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642DiagErrorClear.setStatus("mandatory")

# Managed Objects groups


# Notification objects

wtWebGraphAnalogIn57642Alert1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 0, 31)
)
wtWebGraphAnalogIn57642Alert1.setObjects(
    ("WebGraph-AnalogIn-57642-US-MIB", "wtWebGraphAnalogIn57642AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642Alert1.setStatus(
        ""
    )

wtWebGraphAnalogIn57642Alert2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 0, 32)
)
wtWebGraphAnalogIn57642Alert2.setObjects(
    ("WebGraph-AnalogIn-57642-US-MIB", "wtWebGraphAnalogIn57642AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642Alert2.setStatus(
        ""
    )

wtWebGraphAnalogIn57642Alert3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 0, 33)
)
wtWebGraphAnalogIn57642Alert3.setObjects(
    ("WebGraph-AnalogIn-57642-US-MIB", "wtWebGraphAnalogIn57642AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642Alert3.setStatus(
        ""
    )

wtWebGraphAnalogIn57642Alert4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 0, 34)
)
wtWebGraphAnalogIn57642Alert4.setObjects(
    ("WebGraph-AnalogIn-57642-US-MIB", "wtWebGraphAnalogIn57642AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642Alert4.setStatus(
        ""
    )

wtWebGraphAnalogIn57642Alert5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 0, 35)
)
wtWebGraphAnalogIn57642Alert5.setObjects(
    ("WebGraph-AnalogIn-57642-US-MIB", "wtWebGraphAnalogIn57642AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642Alert5.setStatus(
        ""
    )

wtWebGraphAnalogIn57642Alert6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 0, 36)
)
wtWebGraphAnalogIn57642Alert6.setObjects(
    ("WebGraph-AnalogIn-57642-US-MIB", "wtWebGraphAnalogIn57642AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642Alert6.setStatus(
        ""
    )

wtWebGraphAnalogIn57642Alert7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 0, 37)
)
wtWebGraphAnalogIn57642Alert7.setObjects(
    ("WebGraph-AnalogIn-57642-US-MIB", "wtWebGraphAnalogIn57642AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642Alert7.setStatus(
        ""
    )

wtWebGraphAnalogIn57642Alert8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 0, 38)
)
wtWebGraphAnalogIn57642Alert8.setObjects(
    ("WebGraph-AnalogIn-57642-US-MIB", "wtWebGraphAnalogIn57642AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642Alert8.setStatus(
        ""
    )

wtWebGraphAnalogIn57642Alert9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 0, 91)
)
wtWebGraphAnalogIn57642Alert9.setObjects(
    ("WebGraph-AnalogIn-57642-US-MIB", "wtWebGraphAnalogIn57642AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642Alert9.setStatus(
        ""
    )

wtWebGraphAnalogIn57642Alert10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 0, 92)
)
wtWebGraphAnalogIn57642Alert10.setObjects(
    ("WebGraph-AnalogIn-57642-US-MIB", "wtWebGraphAnalogIn57642AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642Alert10.setStatus(
        ""
    )

wtWebGraphAnalogIn57642Alert11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 0, 93)
)
wtWebGraphAnalogIn57642Alert11.setObjects(
    ("WebGraph-AnalogIn-57642-US-MIB", "wtWebGraphAnalogIn57642AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642Alert11.setStatus(
        ""
    )

wtWebGraphAnalogIn57642Alert12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 0, 94)
)
wtWebGraphAnalogIn57642Alert12.setObjects(
    ("WebGraph-AnalogIn-57642-US-MIB", "wtWebGraphAnalogIn57642AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642Alert12.setStatus(
        ""
    )

wtWebGraphAnalogIn57642Alert13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 0, 95)
)
wtWebGraphAnalogIn57642Alert13.setObjects(
    ("WebGraph-AnalogIn-57642-US-MIB", "wtWebGraphAnalogIn57642AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642Alert13.setStatus(
        ""
    )

wtWebGraphAnalogIn57642Alert14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 0, 96)
)
wtWebGraphAnalogIn57642Alert14.setObjects(
    ("WebGraph-AnalogIn-57642-US-MIB", "wtWebGraphAnalogIn57642AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642Alert14.setStatus(
        ""
    )

wtWebGraphAnalogIn57642Alert15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 0, 97)
)
wtWebGraphAnalogIn57642Alert15.setObjects(
    ("WebGraph-AnalogIn-57642-US-MIB", "wtWebGraphAnalogIn57642AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642Alert15.setStatus(
        ""
    )

wtWebGraphAnalogIn57642Alert16 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 0, 98)
)
wtWebGraphAnalogIn57642Alert16.setObjects(
    ("WebGraph-AnalogIn-57642-US-MIB", "wtWebGraphAnalogIn57642AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642Alert16.setStatus(
        ""
    )

wtWebGraphAnalogIn57642AlertDiag = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 11, 0, 110)
)
wtWebGraphAnalogIn57642AlertDiag.setObjects(
      *(("WebGraph-AnalogIn-57642-US-MIB", "wtWebGraphAnalogIn57642DiagErrorIndex"),
        ("WebGraph-AnalogIn-57642-US-MIB", "wtWebGraphAnalogIn57642DiagErrorMessage"))
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57642AlertDiag.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WebGraph-AnalogIn-57642-US-MIB",
    **{"wut": wut,
       "wtComServer": wtComServer,
       "wtWebio": wtWebio,
       "wtWebGraphAnalogIn57642": wtWebGraphAnalogIn57642,
       "wtWebGraphAnalogIn57642Alert1": wtWebGraphAnalogIn57642Alert1,
       "wtWebGraphAnalogIn57642Alert2": wtWebGraphAnalogIn57642Alert2,
       "wtWebGraphAnalogIn57642Alert3": wtWebGraphAnalogIn57642Alert3,
       "wtWebGraphAnalogIn57642Alert4": wtWebGraphAnalogIn57642Alert4,
       "wtWebGraphAnalogIn57642Alert5": wtWebGraphAnalogIn57642Alert5,
       "wtWebGraphAnalogIn57642Alert6": wtWebGraphAnalogIn57642Alert6,
       "wtWebGraphAnalogIn57642Alert7": wtWebGraphAnalogIn57642Alert7,
       "wtWebGraphAnalogIn57642Alert8": wtWebGraphAnalogIn57642Alert8,
       "wtWebGraphAnalogIn57642Alert9": wtWebGraphAnalogIn57642Alert9,
       "wtWebGraphAnalogIn57642Alert10": wtWebGraphAnalogIn57642Alert10,
       "wtWebGraphAnalogIn57642Alert11": wtWebGraphAnalogIn57642Alert11,
       "wtWebGraphAnalogIn57642Alert12": wtWebGraphAnalogIn57642Alert12,
       "wtWebGraphAnalogIn57642Alert13": wtWebGraphAnalogIn57642Alert13,
       "wtWebGraphAnalogIn57642Alert14": wtWebGraphAnalogIn57642Alert14,
       "wtWebGraphAnalogIn57642Alert15": wtWebGraphAnalogIn57642Alert15,
       "wtWebGraphAnalogIn57642Alert16": wtWebGraphAnalogIn57642Alert16,
       "wtWebGraphAnalogIn57642AlertDiag": wtWebGraphAnalogIn57642AlertDiag,
       "wtWebGraphAnalogIn57642Inventory": wtWebGraphAnalogIn57642Inventory,
       "wtWebGraphAnalogIn57642Sensors": wtWebGraphAnalogIn57642Sensors,
       "wtWebGraphAnalogIn57642SensorTable": wtWebGraphAnalogIn57642SensorTable,
       "wtWebGraphAnalogIn57642SensorEntry": wtWebGraphAnalogIn57642SensorEntry,
       "wtWebGraphAnalogIn57642SensorNo": wtWebGraphAnalogIn57642SensorNo,
       "wtWebGraphAnalogIn57642ValuesTable": wtWebGraphAnalogIn57642ValuesTable,
       "wtWebGraphAnalogIn57642ValuesEntry": wtWebGraphAnalogIn57642ValuesEntry,
       "wtWebGraphAnalogIn57642Values": wtWebGraphAnalogIn57642Values,
       "wtWebGraphAnalogIn57642BinaryValuesTable": wtWebGraphAnalogIn57642BinaryValuesTable,
       "wtWebGraphAnalogIn57642BinaryValuesEntry": wtWebGraphAnalogIn57642BinaryValuesEntry,
       "wtWebGraphAnalogIn57642BinaryValues": wtWebGraphAnalogIn57642BinaryValues,
       "wtWebGraphAnalogIn57642SessCntrl": wtWebGraphAnalogIn57642SessCntrl,
       "wtWebGraphAnalogIn57642SessCntrlPassword": wtWebGraphAnalogIn57642SessCntrlPassword,
       "wtWebGraphAnalogIn57642SessCntrlConfigMode": wtWebGraphAnalogIn57642SessCntrlConfigMode,
       "wtWebGraphAnalogIn57642SessCntrlLogout": wtWebGraphAnalogIn57642SessCntrlLogout,
       "wtWebGraphAnalogIn57642SessCntrlAdminPassword": wtWebGraphAnalogIn57642SessCntrlAdminPassword,
       "wtWebGraphAnalogIn57642SessCntrlConfigPassword": wtWebGraphAnalogIn57642SessCntrlConfigPassword,
       "wtWebGraphAnalogIn57642Config": wtWebGraphAnalogIn57642Config,
       "wtWebGraphAnalogIn57642Device": wtWebGraphAnalogIn57642Device,
       "wtWebGraphAnalogIn57642Text": wtWebGraphAnalogIn57642Text,
       "wtWebGraphAnalogIn57642DeviceName": wtWebGraphAnalogIn57642DeviceName,
       "wtWebGraphAnalogIn57642DeviceText": wtWebGraphAnalogIn57642DeviceText,
       "wtWebGraphAnalogIn57642DeviceLocation": wtWebGraphAnalogIn57642DeviceLocation,
       "wtWebGraphAnalogIn57642DeviceContact": wtWebGraphAnalogIn57642DeviceContact,
       "wtWebGraphAnalogIn57642TimeDate": wtWebGraphAnalogIn57642TimeDate,
       "wtWebGraphAnalogIn57642TimeZone": wtWebGraphAnalogIn57642TimeZone,
       "wtWebGraphAnalogIn57642TzOffsetHrs": wtWebGraphAnalogIn57642TzOffsetHrs,
       "wtWebGraphAnalogIn57642TzOffsetMin": wtWebGraphAnalogIn57642TzOffsetMin,
       "wtWebGraphAnalogIn57642TzEnable": wtWebGraphAnalogIn57642TzEnable,
       "wtWebGraphAnalogIn57642StTzOffsetHrs": wtWebGraphAnalogIn57642StTzOffsetHrs,
       "wtWebGraphAnalogIn57642StTzOffsetMin": wtWebGraphAnalogIn57642StTzOffsetMin,
       "wtWebGraphAnalogIn57642StTzEnable": wtWebGraphAnalogIn57642StTzEnable,
       "wtWebGraphAnalogIn57642StTzStartMonth": wtWebGraphAnalogIn57642StTzStartMonth,
       "wtWebGraphAnalogIn57642StTzStartMode": wtWebGraphAnalogIn57642StTzStartMode,
       "wtWebGraphAnalogIn57642StTzStartWday": wtWebGraphAnalogIn57642StTzStartWday,
       "wtWebGraphAnalogIn57642StTzStartHrs": wtWebGraphAnalogIn57642StTzStartHrs,
       "wtWebGraphAnalogIn57642StTzStartMin": wtWebGraphAnalogIn57642StTzStartMin,
       "wtWebGraphAnalogIn57642StTzStopMonth": wtWebGraphAnalogIn57642StTzStopMonth,
       "wtWebGraphAnalogIn57642StTzStopMode": wtWebGraphAnalogIn57642StTzStopMode,
       "wtWebGraphAnalogIn57642StTzStopWday": wtWebGraphAnalogIn57642StTzStopWday,
       "wtWebGraphAnalogIn57642StTzStopHrs": wtWebGraphAnalogIn57642StTzStopHrs,
       "wtWebGraphAnalogIn57642StTzStopMin": wtWebGraphAnalogIn57642StTzStopMin,
       "wtWebGraphAnalogIn57642TimeServer": wtWebGraphAnalogIn57642TimeServer,
       "wtWebGraphAnalogIn57642TimeServer1": wtWebGraphAnalogIn57642TimeServer1,
       "wtWebGraphAnalogIn57642TimeServer2": wtWebGraphAnalogIn57642TimeServer2,
       "wtWebGraphAnalogIn57642TsEnable": wtWebGraphAnalogIn57642TsEnable,
       "wtWebGraphAnalogIn57642TsSyncTime": wtWebGraphAnalogIn57642TsSyncTime,
       "wtWebGraphAnalogIn57642DeviceClock": wtWebGraphAnalogIn57642DeviceClock,
       "wtWebGraphAnalogIn57642ClockHrs": wtWebGraphAnalogIn57642ClockHrs,
       "wtWebGraphAnalogIn57642ClockMin": wtWebGraphAnalogIn57642ClockMin,
       "wtWebGraphAnalogIn57642ClockDay": wtWebGraphAnalogIn57642ClockDay,
       "wtWebGraphAnalogIn57642ClockMonth": wtWebGraphAnalogIn57642ClockMonth,
       "wtWebGraphAnalogIn57642ClockYear": wtWebGraphAnalogIn57642ClockYear,
       "wtWebGraphAnalogIn57642Basic": wtWebGraphAnalogIn57642Basic,
       "wtWebGraphAnalogIn57642Network": wtWebGraphAnalogIn57642Network,
       "wtWebGraphAnalogIn57642IpAddress": wtWebGraphAnalogIn57642IpAddress,
       "wtWebGraphAnalogIn57642SubnetMask": wtWebGraphAnalogIn57642SubnetMask,
       "wtWebGraphAnalogIn57642Gateway": wtWebGraphAnalogIn57642Gateway,
       "wtWebGraphAnalogIn57642DnsServer1": wtWebGraphAnalogIn57642DnsServer1,
       "wtWebGraphAnalogIn57642DnsServer2": wtWebGraphAnalogIn57642DnsServer2,
       "wtWebGraphAnalogIn57642AddConfig": wtWebGraphAnalogIn57642AddConfig,
       "wtWebGraphAnalogIn57642HTTP": wtWebGraphAnalogIn57642HTTP,
       "wtWebGraphAnalogIn57642Startup": wtWebGraphAnalogIn57642Startup,
       "wtWebGraphAnalogIn57642GetHeaderEnable": wtWebGraphAnalogIn57642GetHeaderEnable,
       "wtWebGraphAnalogIn57642HttpPort": wtWebGraphAnalogIn57642HttpPort,
       "wtWebGraphAnalogIn57642Mail": wtWebGraphAnalogIn57642Mail,
       "wtWebGraphAnalogIn57642MailAdName": wtWebGraphAnalogIn57642MailAdName,
       "wtWebGraphAnalogIn57642MailReply": wtWebGraphAnalogIn57642MailReply,
       "wtWebGraphAnalogIn57642MailServer": wtWebGraphAnalogIn57642MailServer,
       "wtWebioAn1MailEnable": wtWebioAn1MailEnable,
       "wtWebGraphAnalogIn57642MailAuthentication": wtWebGraphAnalogIn57642MailAuthentication,
       "wtWebGraphAnalogIn57642MailAuthUser": wtWebGraphAnalogIn57642MailAuthUser,
       "wtWebGraphAnalogIn57642MailAuthPassword": wtWebGraphAnalogIn57642MailAuthPassword,
       "wtWebGraphAnalogIn57642MailPop3Server": wtWebGraphAnalogIn57642MailPop3Server,
       "wtWebGraphAnalogIn57642SNMP": wtWebGraphAnalogIn57642SNMP,
       "wtWebGraphAnalogIn57642SnmpCommunityStringRead": wtWebGraphAnalogIn57642SnmpCommunityStringRead,
       "wtWebGraphAnalogIn57642SnmpCommunityStringReadWrite": wtWebGraphAnalogIn57642SnmpCommunityStringReadWrite,
       "wtWebGraphAnalogIn57642SystemTrapManagerIP": wtWebGraphAnalogIn57642SystemTrapManagerIP,
       "wtWebGraphAnalogIn57642SystemTrapEnable": wtWebGraphAnalogIn57642SystemTrapEnable,
       "wtWebGraphAnalogIn57642SnmpEnable": wtWebGraphAnalogIn57642SnmpEnable,
       "wtWebGraphAnalogIn57642SnmpCommunityStringTrap": wtWebGraphAnalogIn57642SnmpCommunityStringTrap,
       "wtWebGraphAnalogIn57642UDP": wtWebGraphAnalogIn57642UDP,
       "wtWebGraphAnalogIn57642UdpPort": wtWebGraphAnalogIn57642UdpPort,
       "wtWebGraphAnalogIn57642UdpEnable": wtWebGraphAnalogIn57642UdpEnable,
       "wtWebGraphAnalogIn57642Syslog": wtWebGraphAnalogIn57642Syslog,
       "wtWebGraphAnalogIn57642SyslogServerIP": wtWebGraphAnalogIn57642SyslogServerIP,
       "wtWebGraphAnalogIn57642SyslogServerPort": wtWebGraphAnalogIn57642SyslogServerPort,
       "wtWebGraphAnalogIn57642SyslogSystemMessagesEnable": wtWebGraphAnalogIn57642SyslogSystemMessagesEnable,
       "wtWebGraphAnalogIn57642SyslogEnable": wtWebGraphAnalogIn57642SyslogEnable,
       "wtWebGraphAnalogIn57642FTP": wtWebGraphAnalogIn57642FTP,
       "wtWebGraphAnalogIn57642FTPServerIP": wtWebGraphAnalogIn57642FTPServerIP,
       "wtWebGraphAnalogIn57642FTPServerControlPort": wtWebGraphAnalogIn57642FTPServerControlPort,
       "wtWebGraphAnalogIn57642FTPUserName": wtWebGraphAnalogIn57642FTPUserName,
       "wtWebGraphAnalogIn57642FTPPassword": wtWebGraphAnalogIn57642FTPPassword,
       "wtWebGraphAnalogIn57642FTPAccount": wtWebGraphAnalogIn57642FTPAccount,
       "wtWebGraphAnalogIn57642FTPOption": wtWebGraphAnalogIn57642FTPOption,
       "wtWebGraphAnalogIn57642FTPEnable": wtWebGraphAnalogIn57642FTPEnable,
       "wtWebGraphAnalogIn57642Datalogger": wtWebGraphAnalogIn57642Datalogger,
       "wtWebGraphAnalogIn57642LoggerTimebase": wtWebGraphAnalogIn57642LoggerTimebase,
       "wtWebGraphAnalogIn57642LoggerSensorSel": wtWebGraphAnalogIn57642LoggerSensorSel,
       "wtWebGraphAnalogIn57642DisplaySensorSel": wtWebGraphAnalogIn57642DisplaySensorSel,
       "wtWebGraphAnalogIn57642SensorColorTable": wtWebGraphAnalogIn57642SensorColorTable,
       "wtWebGraphAnalogIn57642SensorColorEntry": wtWebGraphAnalogIn57642SensorColorEntry,
       "wtWebGraphAnalogIn57642SensorColor": wtWebGraphAnalogIn57642SensorColor,
       "wtWebGraphAnalogIn57642AutoScaleEnable": wtWebGraphAnalogIn57642AutoScaleEnable,
       "wtWebGraphAnalogIn57642VerticalUpperLimit": wtWebGraphAnalogIn57642VerticalUpperLimit,
       "wtWebGraphAnalogIn57642VerticalLowerLimit": wtWebGraphAnalogIn57642VerticalLowerLimit,
       "wtWebGraphAnalogIn57642HorizontalZoom": wtWebGraphAnalogIn57642HorizontalZoom,
       "wtWebGraphAnalogIn57642Alarm": wtWebGraphAnalogIn57642Alarm,
       "wtWebGraphAnalogIn57642AlarmCount": wtWebGraphAnalogIn57642AlarmCount,
       "wtWebGraphAnalogIn57642AlarmIfTable": wtWebGraphAnalogIn57642AlarmIfTable,
       "wtWebGraphAnalogIn57642AlarmIfEntry": wtWebGraphAnalogIn57642AlarmIfEntry,
       "wtWebGraphAnalogIn57642AlarmNo": wtWebGraphAnalogIn57642AlarmNo,
       "wtWebGraphAnalogIn57642AlarmTable": wtWebGraphAnalogIn57642AlarmTable,
       "wtWebGraphAnalogIn57642AlarmEntry": wtWebGraphAnalogIn57642AlarmEntry,
       "wtWebGraphAnalogIn57642AlarmTrigger": wtWebGraphAnalogIn57642AlarmTrigger,
       "wtWebGraphAnalogIn57642AlarmMin": wtWebGraphAnalogIn57642AlarmMin,
       "wtWebGraphAnalogIn57642AlarmMax": wtWebGraphAnalogIn57642AlarmMax,
       "wtWebGraphAnalogIn57642AlarmHysteresis": wtWebGraphAnalogIn57642AlarmHysteresis,
       "wtWebGraphAnalogIn57642AlarmDelay": wtWebGraphAnalogIn57642AlarmDelay,
       "wtWebGraphAnalogIn57642AlarmInterval": wtWebGraphAnalogIn57642AlarmInterval,
       "wtWebGraphAnalogIn57642AlarmEnable": wtWebGraphAnalogIn57642AlarmEnable,
       "wtWebGraphAnalogIn57642AlarmEMailAddr": wtWebGraphAnalogIn57642AlarmEMailAddr,
       "wtWebGraphAnalogIn57642AlarmMailSubject": wtWebGraphAnalogIn57642AlarmMailSubject,
       "wtWebGraphAnalogIn57642AlarmMailText": wtWebGraphAnalogIn57642AlarmMailText,
       "wtWebGraphAnalogIn57642AlarmManagerIP": wtWebGraphAnalogIn57642AlarmManagerIP,
       "wtWebGraphAnalogIn57642AlarmTrapText": wtWebGraphAnalogIn57642AlarmTrapText,
       "wtWebGraphAnalogIn57642AlarmMailOptions": wtWebGraphAnalogIn57642AlarmMailOptions,
       "wtWebGraphAnalogIn57642AlarmTcpIpAddr": wtWebGraphAnalogIn57642AlarmTcpIpAddr,
       "wtWebGraphAnalogIn57642AlarmTcpPort": wtWebGraphAnalogIn57642AlarmTcpPort,
       "wtWebGraphAnalogIn57642AlarmTcpText": wtWebGraphAnalogIn57642AlarmTcpText,
       "wtWebGraphAnalogIn57642AlarmClearMailSubject": wtWebGraphAnalogIn57642AlarmClearMailSubject,
       "wtWebGraphAnalogIn57642AlarmClearMailText": wtWebGraphAnalogIn57642AlarmClearMailText,
       "wtWebGraphAnalogIn57642AlarmClearTrapText": wtWebGraphAnalogIn57642AlarmClearTrapText,
       "wtWebGraphAnalogIn57642AlarmClearTcpText": wtWebGraphAnalogIn57642AlarmClearTcpText,
       "wtWebGraphAnalogIn57642Alarm2Min": wtWebGraphAnalogIn57642Alarm2Min,
       "wtWebGraphAnalogIn57642Alarm2Max": wtWebGraphAnalogIn57642Alarm2Max,
       "wtWebGraphAnalogIn57642Alarm2Hysteresis": wtWebGraphAnalogIn57642Alarm2Hysteresis,
       "wtWebGraphAnalogIn57642AlarmSyslogIpAddr": wtWebGraphAnalogIn57642AlarmSyslogIpAddr,
       "wtWebGraphAnalogIn57642AlarmSyslogPort": wtWebGraphAnalogIn57642AlarmSyslogPort,
       "wtWebGraphAnalogIn57642AlarmSyslogText": wtWebGraphAnalogIn57642AlarmSyslogText,
       "wtWebGraphAnalogIn57642AlarmSyslogClearText": wtWebGraphAnalogIn57642AlarmSyslogClearText,
       "wtWebGraphAnalogIn57642AlarmFtpDataPort": wtWebGraphAnalogIn57642AlarmFtpDataPort,
       "wtWebGraphAnalogIn57642AlarmFtpFileName": wtWebGraphAnalogIn57642AlarmFtpFileName,
       "wtWebGraphAnalogIn57642AlarmFtpText": wtWebGraphAnalogIn57642AlarmFtpText,
       "wtWebGraphAnalogIn57642AlarmFtpClearText": wtWebGraphAnalogIn57642AlarmFtpClearText,
       "wtWebGraphAnalogIn57642AlarmFtpOption": wtWebGraphAnalogIn57642AlarmFtpOption,
       "wtWebGraphAnalogIn57642AlarmTimerCron": wtWebGraphAnalogIn57642AlarmTimerCron,
       "wtWebGraphAnalogIn57642Graphics": wtWebGraphAnalogIn57642Graphics,
       "wtWebGraphAnalogIn57642GraphicsBase": wtWebGraphAnalogIn57642GraphicsBase,
       "wtWebGraphAnalogIn57642GraphicsBaseEnable": wtWebGraphAnalogIn57642GraphicsBaseEnable,
       "wtWebGraphAnalogIn57642GraphicsBaseWidth": wtWebGraphAnalogIn57642GraphicsBaseWidth,
       "wtWebGraphAnalogIn57642GraphicsBaseHeight": wtWebGraphAnalogIn57642GraphicsBaseHeight,
       "wtWebGraphAnalogIn57642GraphicsBaseFrameColor": wtWebGraphAnalogIn57642GraphicsBaseFrameColor,
       "wtWebGraphAnalogIn57642GraphicsBaseBackgroundColor": wtWebGraphAnalogIn57642GraphicsBaseBackgroundColor,
       "wtWebGraphAnalogIn57642GraphicsBasePollingrate": wtWebGraphAnalogIn57642GraphicsBasePollingrate,
       "wtWebGraphAnalogIn57642GraphicsSelect": wtWebGraphAnalogIn57642GraphicsSelect,
       "wtWebGraphAnalogIn57642GraphicsSelectDisplaySensorSel": wtWebGraphAnalogIn57642GraphicsSelectDisplaySensorSel,
       "wtWebGraphAnalogIn57642GraphicsSelectDisplayShowExtrem": wtWebGraphAnalogIn57642GraphicsSelectDisplayShowExtrem,
       "wtWebGraphAnalogIn57642SensorColor2Table": wtWebGraphAnalogIn57642SensorColor2Table,
       "wtWebGraphAnalogIn57642SensorColor2Entry": wtWebGraphAnalogIn57642SensorColor2Entry,
       "wtWebGraphAnalogIn57642GraphicsSensorColor": wtWebGraphAnalogIn57642GraphicsSensorColor,
       "wtWebGraphAnalogIn57642GraphicsSelectScale": wtWebGraphAnalogIn57642GraphicsSelectScale,
       "wtWebGraphAnalogIn57642GraphicsScale": wtWebGraphAnalogIn57642GraphicsScale,
       "wtWebGraphAnalogIn57642GraphicsScaleAutoScaleEnable": wtWebGraphAnalogIn57642GraphicsScaleAutoScaleEnable,
       "wtWebGraphAnalogIn57642GraphicsScaleAutoFitEnable": wtWebGraphAnalogIn57642GraphicsScaleAutoFitEnable,
       "wtWebGraphAnalogIn57642GraphicsScale1Min": wtWebGraphAnalogIn57642GraphicsScale1Min,
       "wtWebGraphAnalogIn57642GraphicsScale2Min": wtWebGraphAnalogIn57642GraphicsScale2Min,
       "wtWebGraphAnalogIn57642GraphicsScale3Min": wtWebGraphAnalogIn57642GraphicsScale3Min,
       "wtWebGraphAnalogIn57642GraphicsScale4Min": wtWebGraphAnalogIn57642GraphicsScale4Min,
       "wtWebGraphAnalogIn57642GraphicsScale1Max": wtWebGraphAnalogIn57642GraphicsScale1Max,
       "wtWebGraphAnalogIn57642GraphicsScale2Max": wtWebGraphAnalogIn57642GraphicsScale2Max,
       "wtWebGraphAnalogIn57642GraphicsScale3Max": wtWebGraphAnalogIn57642GraphicsScale3Max,
       "wtWebGraphAnalogIn57642GraphicsScale4Max": wtWebGraphAnalogIn57642GraphicsScale4Max,
       "wtWebGraphAnalogIn57642GraphicsScale1Unit": wtWebGraphAnalogIn57642GraphicsScale1Unit,
       "wtWebGraphAnalogIn57642GraphicsScale2Unit": wtWebGraphAnalogIn57642GraphicsScale2Unit,
       "wtWebGraphAnalogIn57642GraphicsScale3Unit": wtWebGraphAnalogIn57642GraphicsScale3Unit,
       "wtWebGraphAnalogIn57642GraphicsScale4Unit": wtWebGraphAnalogIn57642GraphicsScale4Unit,
       "wtWebGraphAnalogIn57642Ports": wtWebGraphAnalogIn57642Ports,
       "wtWebGraphAnalogIn57642PortTable": wtWebGraphAnalogIn57642PortTable,
       "wtWebGraphAnalogIn57642PortEntry": wtWebGraphAnalogIn57642PortEntry,
       "wtWebGraphAnalogIn57642PortName": wtWebGraphAnalogIn57642PortName,
       "wtWebGraphAnalogIn57642PortText": wtWebGraphAnalogIn57642PortText,
       "wtWebGraphAnalogIn57642PortOffset1": wtWebGraphAnalogIn57642PortOffset1,
       "wtWebGraphAnalogIn57642SetPoint1": wtWebGraphAnalogIn57642SetPoint1,
       "wtWebGraphAnalogIn57642PortOffset2": wtWebGraphAnalogIn57642PortOffset2,
       "wtWebGraphAnalogIn57642SetPoint2": wtWebGraphAnalogIn57642SetPoint2,
       "wtWebGraphAnalogIn57642PortComment": wtWebGraphAnalogIn57642PortComment,
       "wtWebGraphAnalogIn57642PortSensorSelect": wtWebGraphAnalogIn57642PortSensorSelect,
       "wtWebGraphAnalogIn57642PortUnit": wtWebGraphAnalogIn57642PortUnit,
       "wtWebGraphAnalogIn57642PortScale0": wtWebGraphAnalogIn57642PortScale0,
       "wtWebGraphAnalogIn57642PortScale100": wtWebGraphAnalogIn57642PortScale100,
       "wtWebGraphAnalogIn57642Manufact": wtWebGraphAnalogIn57642Manufact,
       "wtWebGraphAnalogIn57642MfName": wtWebGraphAnalogIn57642MfName,
       "wtWebGraphAnalogIn57642MfAddr": wtWebGraphAnalogIn57642MfAddr,
       "wtWebGraphAnalogIn57642MfHotline": wtWebGraphAnalogIn57642MfHotline,
       "wtWebGraphAnalogIn57642MfInternet": wtWebGraphAnalogIn57642MfInternet,
       "wtWebGraphAnalogIn57642MfDeviceTyp": wtWebGraphAnalogIn57642MfDeviceTyp,
       "wtWebGraphAnalogIn57642MfOrderNo": wtWebGraphAnalogIn57642MfOrderNo,
       "wtWebGraphAnalogIn57642Diag": wtWebGraphAnalogIn57642Diag,
       "wtWebGraphAnalogIn57642DiagErrorCount": wtWebGraphAnalogIn57642DiagErrorCount,
       "wtWebGraphAnalogIn57642DiagBinaryError": wtWebGraphAnalogIn57642DiagBinaryError,
       "wtWebGraphAnalogIn57642DiagErrorIndex": wtWebGraphAnalogIn57642DiagErrorIndex,
       "wtWebGraphAnalogIn57642DiagErrorMessage": wtWebGraphAnalogIn57642DiagErrorMessage,
       "wtWebGraphAnalogIn57642DiagErrorClear": wtWebGraphAnalogIn57642DiagErrorClear}
)
