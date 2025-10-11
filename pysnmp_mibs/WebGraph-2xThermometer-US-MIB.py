# SNMP MIB module (WebGraph-2xThermometer-US-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/webgraph/WebGraph-2xThermometer-US-MIB
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
_WtWebioAn2Graph_ObjectIdentity = ObjectIdentity
wtWebioAn2Graph = _WtWebioAn2Graph_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43)
)
_WtWebioAn2GraphTemp_ObjectIdentity = ObjectIdentity
wtWebioAn2GraphTemp = _WtWebioAn2GraphTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 1)
)


class _WtWebioAn2GraphSensors_Type(Integer32):
    """Custom type wtWebioAn2GraphSensors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WtWebioAn2GraphSensors_Type.__name__ = "Integer32"
_WtWebioAn2GraphSensors_Object = MibScalar
wtWebioAn2GraphSensors = _WtWebioAn2GraphSensors_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 1, 1),
    _WtWebioAn2GraphSensors_Type()
)
wtWebioAn2GraphSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn2GraphSensors.setStatus("mandatory")
_WtWebioAn2GraphSensorTable_Object = MibTable
wtWebioAn2GraphSensorTable = _WtWebioAn2GraphSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 1, 2)
)
if mibBuilder.loadTexts:
    wtWebioAn2GraphSensorTable.setStatus("mandatory")
_WtWebioAn2GraphSensorEntry_Object = MibTableRow
wtWebioAn2GraphSensorEntry = _WtWebioAn2GraphSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 1, 2, 1)
)
wtWebioAn2GraphSensorEntry.setIndexNames(
    (0, "WebGraph-2xThermometer-US-MIB", "wtWebioAn2GraphSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn2GraphSensorEntry.setStatus("mandatory")


class _WtWebioAn2GraphSensorNo_Type(Integer32):
    """Custom type wtWebioAn2GraphSensorNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WtWebioAn2GraphSensorNo_Type.__name__ = "Integer32"
_WtWebioAn2GraphSensorNo_Object = MibTableColumn
wtWebioAn2GraphSensorNo = _WtWebioAn2GraphSensorNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 1, 2, 1, 1),
    _WtWebioAn2GraphSensorNo_Type()
)
wtWebioAn2GraphSensorNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn2GraphSensorNo.setStatus("mandatory")
_WtWebioAn2GraphTempValueTable_Object = MibTable
wtWebioAn2GraphTempValueTable = _WtWebioAn2GraphTempValueTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 1, 3)
)
if mibBuilder.loadTexts:
    wtWebioAn2GraphTempValueTable.setStatus("mandatory")
_WtWebioAn2GraphTempValueEntry_Object = MibTableRow
wtWebioAn2GraphTempValueEntry = _WtWebioAn2GraphTempValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 1, 3, 1)
)
wtWebioAn2GraphTempValueEntry.setIndexNames(
    (0, "WebGraph-2xThermometer-US-MIB", "wtWebioAn2GraphSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn2GraphTempValueEntry.setStatus("mandatory")


class _WtWebioAn2GraphTempValue_Type(OctetString):
    """Custom type wtWebioAn2GraphTempValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_WtWebioAn2GraphTempValue_Type.__name__ = "OctetString"
_WtWebioAn2GraphTempValue_Object = MibTableColumn
wtWebioAn2GraphTempValue = _WtWebioAn2GraphTempValue_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 1, 3, 1, 1),
    _WtWebioAn2GraphTempValue_Type()
)
wtWebioAn2GraphTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn2GraphTempValue.setStatus("mandatory")
_WtWebioAn2GraphBinaryTempValueTable_Object = MibTable
wtWebioAn2GraphBinaryTempValueTable = _WtWebioAn2GraphBinaryTempValueTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 1, 4)
)
if mibBuilder.loadTexts:
    wtWebioAn2GraphBinaryTempValueTable.setStatus("mandatory")
_WtWebioAn2GraphBinaryTempValueEntry_Object = MibTableRow
wtWebioAn2GraphBinaryTempValueEntry = _WtWebioAn2GraphBinaryTempValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 1, 4, 1)
)
wtWebioAn2GraphBinaryTempValueEntry.setIndexNames(
    (0, "WebGraph-2xThermometer-US-MIB", "wtWebioAn2GraphSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn2GraphBinaryTempValueEntry.setStatus("mandatory")
_WtWebioAn2GraphBinaryTempValue_Type = Integer32
_WtWebioAn2GraphBinaryTempValue_Object = MibTableColumn
wtWebioAn2GraphBinaryTempValue = _WtWebioAn2GraphBinaryTempValue_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 1, 4, 1, 1),
    _WtWebioAn2GraphBinaryTempValue_Type()
)
wtWebioAn2GraphBinaryTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn2GraphBinaryTempValue.setStatus("mandatory")
_WtWebioAn2GraphTempValuePktTable_Object = MibTable
wtWebioAn2GraphTempValuePktTable = _WtWebioAn2GraphTempValuePktTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 1, 8)
)
if mibBuilder.loadTexts:
    wtWebioAn2GraphTempValuePktTable.setStatus("mandatory")
_WtWebioAn2GraphTempValuePktEntry_Object = MibTableRow
wtWebioAn2GraphTempValuePktEntry = _WtWebioAn2GraphTempValuePktEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 1, 8, 1)
)
wtWebioAn2GraphTempValuePktEntry.setIndexNames(
    (0, "WebGraph-2xThermometer-US-MIB", "wtWebioAn2GraphSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn2GraphTempValuePktEntry.setStatus("mandatory")


class _WtWebioAn2GraphTempValuePkt_Type(OctetString):
    """Custom type wtWebioAn2GraphTempValuePkt based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_WtWebioAn2GraphTempValuePkt_Type.__name__ = "OctetString"
_WtWebioAn2GraphTempValuePkt_Object = MibTableColumn
wtWebioAn2GraphTempValuePkt = _WtWebioAn2GraphTempValuePkt_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 1, 8, 1, 1),
    _WtWebioAn2GraphTempValuePkt_Type()
)
wtWebioAn2GraphTempValuePkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn2GraphTempValuePkt.setStatus("mandatory")
_WtWebioAn2GraphSessCntrl_ObjectIdentity = ObjectIdentity
wtWebioAn2GraphSessCntrl = _WtWebioAn2GraphSessCntrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 2)
)
_WtWebioAn2GraphSessCntrlPassword_Type = OctetString
_WtWebioAn2GraphSessCntrlPassword_Object = MibScalar
wtWebioAn2GraphSessCntrlPassword = _WtWebioAn2GraphSessCntrlPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 2, 1),
    _WtWebioAn2GraphSessCntrlPassword_Type()
)
wtWebioAn2GraphSessCntrlPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphSessCntrlPassword.setStatus("mandatory")


class _WtWebioAn2GraphSessCntrlConfigMode_Type(Integer32):
    """Custom type wtWebioAn2GraphSessCntrlConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("wtWebioAn2GraphSessCntrl-NoSession", 0),
          ("wtWebioAn2GraphSessCntrl-Session", 1))
    )


_WtWebioAn2GraphSessCntrlConfigMode_Type.__name__ = "Integer32"
_WtWebioAn2GraphSessCntrlConfigMode_Object = MibScalar
wtWebioAn2GraphSessCntrlConfigMode = _WtWebioAn2GraphSessCntrlConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 2, 2),
    _WtWebioAn2GraphSessCntrlConfigMode_Type()
)
wtWebioAn2GraphSessCntrlConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn2GraphSessCntrlConfigMode.setStatus("mandatory")
_WtWebioAn2GraphSessCntrlLogout_Type = Integer32
_WtWebioAn2GraphSessCntrlLogout_Object = MibScalar
wtWebioAn2GraphSessCntrlLogout = _WtWebioAn2GraphSessCntrlLogout_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 2, 3),
    _WtWebioAn2GraphSessCntrlLogout_Type()
)
wtWebioAn2GraphSessCntrlLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphSessCntrlLogout.setStatus("mandatory")
_WtWebioAn2GraphSessCntrlAdminPassword_Type = OctetString
_WtWebioAn2GraphSessCntrlAdminPassword_Object = MibScalar
wtWebioAn2GraphSessCntrlAdminPassword = _WtWebioAn2GraphSessCntrlAdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 2, 4),
    _WtWebioAn2GraphSessCntrlAdminPassword_Type()
)
wtWebioAn2GraphSessCntrlAdminPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphSessCntrlAdminPassword.setStatus("mandatory")
_WtWebioAn2GraphSessCntrlConfigPassword_Type = OctetString
_WtWebioAn2GraphSessCntrlConfigPassword_Object = MibScalar
wtWebioAn2GraphSessCntrlConfigPassword = _WtWebioAn2GraphSessCntrlConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 2, 5),
    _WtWebioAn2GraphSessCntrlConfigPassword_Type()
)
wtWebioAn2GraphSessCntrlConfigPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphSessCntrlConfigPassword.setStatus("mandatory")
_WtWebioAn2GraphConfig_ObjectIdentity = ObjectIdentity
wtWebioAn2GraphConfig = _WtWebioAn2GraphConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3)
)
_WtWebioAn2GraphDevice_ObjectIdentity = ObjectIdentity
wtWebioAn2GraphDevice = _WtWebioAn2GraphDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1)
)
_WtWebioAn2GraphText_ObjectIdentity = ObjectIdentity
wtWebioAn2GraphText = _WtWebioAn2GraphText_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 1)
)
_WtWebioAn2GraphDeviceName_Type = OctetString
_WtWebioAn2GraphDeviceName_Object = MibScalar
wtWebioAn2GraphDeviceName = _WtWebioAn2GraphDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 1, 1),
    _WtWebioAn2GraphDeviceName_Type()
)
wtWebioAn2GraphDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphDeviceName.setStatus("mandatory")
_WtWebioAn2GraphDeviceText_Type = OctetString
_WtWebioAn2GraphDeviceText_Object = MibScalar
wtWebioAn2GraphDeviceText = _WtWebioAn2GraphDeviceText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 1, 2),
    _WtWebioAn2GraphDeviceText_Type()
)
wtWebioAn2GraphDeviceText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphDeviceText.setStatus("mandatory")
_WtWebioAn2GraphDeviceLocation_Type = OctetString
_WtWebioAn2GraphDeviceLocation_Object = MibScalar
wtWebioAn2GraphDeviceLocation = _WtWebioAn2GraphDeviceLocation_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 1, 3),
    _WtWebioAn2GraphDeviceLocation_Type()
)
wtWebioAn2GraphDeviceLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphDeviceLocation.setStatus("mandatory")
_WtWebioAn2GraphDeviceContact_Type = OctetString
_WtWebioAn2GraphDeviceContact_Object = MibScalar
wtWebioAn2GraphDeviceContact = _WtWebioAn2GraphDeviceContact_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 1, 4),
    _WtWebioAn2GraphDeviceContact_Type()
)
wtWebioAn2GraphDeviceContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphDeviceContact.setStatus("mandatory")
_WtWebioAn2GraphTimeDate_ObjectIdentity = ObjectIdentity
wtWebioAn2GraphTimeDate = _WtWebioAn2GraphTimeDate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 2)
)
_WtWebioAn2GraphTimeZone_ObjectIdentity = ObjectIdentity
wtWebioAn2GraphTimeZone = _WtWebioAn2GraphTimeZone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 2, 1)
)
_WtWebioAn2GraphTzOffsetHrs_Type = Integer32
_WtWebioAn2GraphTzOffsetHrs_Object = MibScalar
wtWebioAn2GraphTzOffsetHrs = _WtWebioAn2GraphTzOffsetHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 2, 1, 1),
    _WtWebioAn2GraphTzOffsetHrs_Type()
)
wtWebioAn2GraphTzOffsetHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphTzOffsetHrs.setStatus("mandatory")
_WtWebioAn2GraphTzOffsetMin_Type = Integer32
_WtWebioAn2GraphTzOffsetMin_Object = MibScalar
wtWebioAn2GraphTzOffsetMin = _WtWebioAn2GraphTzOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 2, 1, 2),
    _WtWebioAn2GraphTzOffsetMin_Type()
)
wtWebioAn2GraphTzOffsetMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphTzOffsetMin.setStatus("mandatory")


class _WtWebioAn2GraphTzEnable_Type(OctetString):
    """Custom type wtWebioAn2GraphTzEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebioAn2GraphTzEnable_Type.__name__ = "OctetString"
_WtWebioAn2GraphTzEnable_Object = MibScalar
wtWebioAn2GraphTzEnable = _WtWebioAn2GraphTzEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 2, 1, 3),
    _WtWebioAn2GraphTzEnable_Type()
)
wtWebioAn2GraphTzEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphTzEnable.setStatus("mandatory")
_WtWebioAn2GraphStTzOffsetHrs_Type = Integer32
_WtWebioAn2GraphStTzOffsetHrs_Object = MibScalar
wtWebioAn2GraphStTzOffsetHrs = _WtWebioAn2GraphStTzOffsetHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 2, 1, 4),
    _WtWebioAn2GraphStTzOffsetHrs_Type()
)
wtWebioAn2GraphStTzOffsetHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphStTzOffsetHrs.setStatus("mandatory")
_WtWebioAn2GraphStTzOffsetMin_Type = Integer32
_WtWebioAn2GraphStTzOffsetMin_Object = MibScalar
wtWebioAn2GraphStTzOffsetMin = _WtWebioAn2GraphStTzOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 2, 1, 5),
    _WtWebioAn2GraphStTzOffsetMin_Type()
)
wtWebioAn2GraphStTzOffsetMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphStTzOffsetMin.setStatus("mandatory")


class _WtWebioAn2GraphStTzEnable_Type(OctetString):
    """Custom type wtWebioAn2GraphStTzEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebioAn2GraphStTzEnable_Type.__name__ = "OctetString"
_WtWebioAn2GraphStTzEnable_Object = MibScalar
wtWebioAn2GraphStTzEnable = _WtWebioAn2GraphStTzEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 2, 1, 6),
    _WtWebioAn2GraphStTzEnable_Type()
)
wtWebioAn2GraphStTzEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphStTzEnable.setStatus("mandatory")


class _WtWebioAn2GraphStTzStartMonth_Type(Integer32):
    """Custom type wtWebioAn2GraphStTzStartMonth based on Integer32"""
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
        *(("wtWebioAn2GraphStartMonth-January", 1),
          ("wtWebioAn2GraphStartMonth-February", 2),
          ("wtWebioAn2GraphStartMonth-March", 3),
          ("wtWebioAn2GraphStartMonth-April", 4),
          ("wtWebioAn2GraphStartMonth-May", 5),
          ("wtWebioAn2GraphStartMonth-June", 6),
          ("wtWebioAn2GraphStartMonth-July", 7),
          ("wtWebioAn2GraphStartMonth-August", 8),
          ("wtWebioAn2GraphStartMonth-September", 9),
          ("wtWebioAn2GraphStartMonth-October", 10),
          ("wtWebioAn2GraphStartMonth-November", 11),
          ("wtWebioAn2GraphStartMonth-December", 12))
    )


_WtWebioAn2GraphStTzStartMonth_Type.__name__ = "Integer32"
_WtWebioAn2GraphStTzStartMonth_Object = MibScalar
wtWebioAn2GraphStTzStartMonth = _WtWebioAn2GraphStTzStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 2, 1, 7),
    _WtWebioAn2GraphStTzStartMonth_Type()
)
wtWebioAn2GraphStTzStartMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphStTzStartMonth.setStatus("mandatory")


class _WtWebioAn2GraphStTzStartMode_Type(Integer32):
    """Custom type wtWebioAn2GraphStTzStartMode based on Integer32"""
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
        *(("wtWebioAn2GraphStartMode-first", 1),
          ("wtWebioAn2GraphStartMode-second", 2),
          ("wtWebioAn2GraphStartMode-third", 3),
          ("wtWebioAn2GraphStartMode-fourth", 4),
          ("wtWebioAn2GraphStartMode-last", 5))
    )


_WtWebioAn2GraphStTzStartMode_Type.__name__ = "Integer32"
_WtWebioAn2GraphStTzStartMode_Object = MibScalar
wtWebioAn2GraphStTzStartMode = _WtWebioAn2GraphStTzStartMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 2, 1, 8),
    _WtWebioAn2GraphStTzStartMode_Type()
)
wtWebioAn2GraphStTzStartMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphStTzStartMode.setStatus("mandatory")


class _WtWebioAn2GraphStTzStartWday_Type(Integer32):
    """Custom type wtWebioAn2GraphStTzStartWday based on Integer32"""
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
        *(("wtWebioAn2GraphStartWday-Sunday", 1),
          ("wtWebioAn2GraphStartWday-Monday", 2),
          ("wtWebioAn2GraphStartWday-Tuesday", 3),
          ("wtWebioAn2GraphStartWday-Thursday", 4),
          ("wtWebioAn2GraphStartWday-Wednesday", 5),
          ("wtWebioAn2GraphStartWday-Friday", 6),
          ("wtWebioAn2GraphStartWday-Saturday", 7))
    )


_WtWebioAn2GraphStTzStartWday_Type.__name__ = "Integer32"
_WtWebioAn2GraphStTzStartWday_Object = MibScalar
wtWebioAn2GraphStTzStartWday = _WtWebioAn2GraphStTzStartWday_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 2, 1, 9),
    _WtWebioAn2GraphStTzStartWday_Type()
)
wtWebioAn2GraphStTzStartWday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphStTzStartWday.setStatus("mandatory")
_WtWebioAn2GraphStTzStartHrs_Type = Integer32
_WtWebioAn2GraphStTzStartHrs_Object = MibScalar
wtWebioAn2GraphStTzStartHrs = _WtWebioAn2GraphStTzStartHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 2, 1, 10),
    _WtWebioAn2GraphStTzStartHrs_Type()
)
wtWebioAn2GraphStTzStartHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphStTzStartHrs.setStatus("mandatory")
_WtWebioAn2GraphStTzStartMin_Type = Integer32
_WtWebioAn2GraphStTzStartMin_Object = MibScalar
wtWebioAn2GraphStTzStartMin = _WtWebioAn2GraphStTzStartMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 2, 1, 11),
    _WtWebioAn2GraphStTzStartMin_Type()
)
wtWebioAn2GraphStTzStartMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphStTzStartMin.setStatus("mandatory")


class _WtWebioAn2GraphStTzStopMonth_Type(Integer32):
    """Custom type wtWebioAn2GraphStTzStopMonth based on Integer32"""
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
        *(("wtWebioAn2GraphStopMonth-January", 1),
          ("wtWebioAn2GraphStopMonth-February", 2),
          ("wtWebioAn2GraphStopMonth-March", 3),
          ("wtWebioAn2GraphStopMonth-April", 4),
          ("wtWebioAn2GraphStopMonth-May", 5),
          ("wtWebioAn2GraphStopMonth-June", 6),
          ("wtWebioAn2GraphStopMonth-July", 7),
          ("wtWebioAn2GraphStopMonth-August", 8),
          ("wtWebioAn2GraphStopMonth-September", 9),
          ("wtWebioAn2GraphStopMonth-October", 10),
          ("wtWebioAn2GraphStopMonth-November", 11),
          ("wtWebioAn2GraphStopMonth-December", 12))
    )


_WtWebioAn2GraphStTzStopMonth_Type.__name__ = "Integer32"
_WtWebioAn2GraphStTzStopMonth_Object = MibScalar
wtWebioAn2GraphStTzStopMonth = _WtWebioAn2GraphStTzStopMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 2, 1, 12),
    _WtWebioAn2GraphStTzStopMonth_Type()
)
wtWebioAn2GraphStTzStopMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphStTzStopMonth.setStatus("mandatory")


class _WtWebioAn2GraphStTzStopMode_Type(Integer32):
    """Custom type wtWebioAn2GraphStTzStopMode based on Integer32"""
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
        *(("wtWebioAn2GraphStopMode-first", 1),
          ("wtWebioAn2GraphStopMode-second", 2),
          ("wtWebioAn2GraphStopMode-third", 3),
          ("wtWebioAn2GraphStopMode-fourth", 4),
          ("wtWebioAn2GraphStopMode-last", 5))
    )


_WtWebioAn2GraphStTzStopMode_Type.__name__ = "Integer32"
_WtWebioAn2GraphStTzStopMode_Object = MibScalar
wtWebioAn2GraphStTzStopMode = _WtWebioAn2GraphStTzStopMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 2, 1, 13),
    _WtWebioAn2GraphStTzStopMode_Type()
)
wtWebioAn2GraphStTzStopMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphStTzStopMode.setStatus("mandatory")


class _WtWebioAn2GraphStTzStopWday_Type(Integer32):
    """Custom type wtWebioAn2GraphStTzStopWday based on Integer32"""
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
        *(("wtWebioAn2GraphStopWday-Sunday", 1),
          ("wtWebioAn2GraphStopWday-Monday", 2),
          ("wtWebioAn2GraphStopWday-Tuesday", 3),
          ("wtWebioAn2GraphStopWday-Thursday", 4),
          ("wtWebioAn2GraphStopWday-Wednesday", 5),
          ("wtWebioAn2GraphStopWday-Friday", 6),
          ("wtWebioAn2GraphStopWday-Saturday", 7))
    )


_WtWebioAn2GraphStTzStopWday_Type.__name__ = "Integer32"
_WtWebioAn2GraphStTzStopWday_Object = MibScalar
wtWebioAn2GraphStTzStopWday = _WtWebioAn2GraphStTzStopWday_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 2, 1, 14),
    _WtWebioAn2GraphStTzStopWday_Type()
)
wtWebioAn2GraphStTzStopWday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphStTzStopWday.setStatus("mandatory")
_WtWebioAn2GraphStTzStopHrs_Type = Integer32
_WtWebioAn2GraphStTzStopHrs_Object = MibScalar
wtWebioAn2GraphStTzStopHrs = _WtWebioAn2GraphStTzStopHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 2, 1, 15),
    _WtWebioAn2GraphStTzStopHrs_Type()
)
wtWebioAn2GraphStTzStopHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphStTzStopHrs.setStatus("mandatory")
_WtWebioAn2GraphStTzStopMin_Type = Integer32
_WtWebioAn2GraphStTzStopMin_Object = MibScalar
wtWebioAn2GraphStTzStopMin = _WtWebioAn2GraphStTzStopMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 2, 1, 16),
    _WtWebioAn2GraphStTzStopMin_Type()
)
wtWebioAn2GraphStTzStopMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphStTzStopMin.setStatus("mandatory")
_WtWebioAn2GraphTimeServer_ObjectIdentity = ObjectIdentity
wtWebioAn2GraphTimeServer = _WtWebioAn2GraphTimeServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 2, 2)
)
_WtWebioAn2GraphTimeServer1_Type = OctetString
_WtWebioAn2GraphTimeServer1_Object = MibScalar
wtWebioAn2GraphTimeServer1 = _WtWebioAn2GraphTimeServer1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 2, 2, 1),
    _WtWebioAn2GraphTimeServer1_Type()
)
wtWebioAn2GraphTimeServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphTimeServer1.setStatus("mandatory")
_WtWebioAn2GraphTimeServer2_Type = OctetString
_WtWebioAn2GraphTimeServer2_Object = MibScalar
wtWebioAn2GraphTimeServer2 = _WtWebioAn2GraphTimeServer2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 2, 2, 2),
    _WtWebioAn2GraphTimeServer2_Type()
)
wtWebioAn2GraphTimeServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphTimeServer2.setStatus("mandatory")


class _WtWebioAn2GraphTsEnable_Type(OctetString):
    """Custom type wtWebioAn2GraphTsEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebioAn2GraphTsEnable_Type.__name__ = "OctetString"
_WtWebioAn2GraphTsEnable_Object = MibScalar
wtWebioAn2GraphTsEnable = _WtWebioAn2GraphTsEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 2, 2, 3),
    _WtWebioAn2GraphTsEnable_Type()
)
wtWebioAn2GraphTsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphTsEnable.setStatus("mandatory")
_WtWebioAn2GraphTsSyncTime_Type = Integer32
_WtWebioAn2GraphTsSyncTime_Object = MibScalar
wtWebioAn2GraphTsSyncTime = _WtWebioAn2GraphTsSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 2, 2, 4),
    _WtWebioAn2GraphTsSyncTime_Type()
)
wtWebioAn2GraphTsSyncTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphTsSyncTime.setStatus("mandatory")
_WtWebioAn2GraphDeviceClock_ObjectIdentity = ObjectIdentity
wtWebioAn2GraphDeviceClock = _WtWebioAn2GraphDeviceClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 2, 3)
)


class _WtWebioAn2GraphClockHrs_Type(Integer32):
    """Custom type wtWebioAn2GraphClockHrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_WtWebioAn2GraphClockHrs_Type.__name__ = "Integer32"
_WtWebioAn2GraphClockHrs_Object = MibScalar
wtWebioAn2GraphClockHrs = _WtWebioAn2GraphClockHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 2, 3, 1),
    _WtWebioAn2GraphClockHrs_Type()
)
wtWebioAn2GraphClockHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphClockHrs.setStatus("mandatory")


class _WtWebioAn2GraphClockMin_Type(Integer32):
    """Custom type wtWebioAn2GraphClockMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_WtWebioAn2GraphClockMin_Type.__name__ = "Integer32"
_WtWebioAn2GraphClockMin_Object = MibScalar
wtWebioAn2GraphClockMin = _WtWebioAn2GraphClockMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 2, 3, 2),
    _WtWebioAn2GraphClockMin_Type()
)
wtWebioAn2GraphClockMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphClockMin.setStatus("mandatory")


class _WtWebioAn2GraphClockDay_Type(Integer32):
    """Custom type wtWebioAn2GraphClockDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_WtWebioAn2GraphClockDay_Type.__name__ = "Integer32"
_WtWebioAn2GraphClockDay_Object = MibScalar
wtWebioAn2GraphClockDay = _WtWebioAn2GraphClockDay_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 2, 3, 3),
    _WtWebioAn2GraphClockDay_Type()
)
wtWebioAn2GraphClockDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphClockDay.setStatus("mandatory")


class _WtWebioAn2GraphClockMonth_Type(Integer32):
    """Custom type wtWebioAn2GraphClockMonth based on Integer32"""
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
        *(("wtWebioAn2GraphClockMonth-January", 1),
          ("wtWebioAn2GraphClockMonth-February", 2),
          ("wtWebioAn2GraphClockMonth-March", 3),
          ("wtWebioAn2GraphClockMonth-April", 4),
          ("wtWebioAn2GraphClockMonth-May", 5),
          ("wtWebioAn2GraphClockMonth-June", 6),
          ("wtWebioAn2GraphClockMonth-July", 7),
          ("wtWebioAn2GraphClockMonth-August", 8),
          ("wtWebioAn2GraphClockMonth-September", 9),
          ("wtWebioAn2GraphClockMonth-October", 10),
          ("wtWebioAn2GraphClockMonth-November", 11),
          ("wtWebioAn2GraphClockMonth-December", 12))
    )


_WtWebioAn2GraphClockMonth_Type.__name__ = "Integer32"
_WtWebioAn2GraphClockMonth_Object = MibScalar
wtWebioAn2GraphClockMonth = _WtWebioAn2GraphClockMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 2, 3, 4),
    _WtWebioAn2GraphClockMonth_Type()
)
wtWebioAn2GraphClockMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphClockMonth.setStatus("mandatory")


class _WtWebioAn2GraphClockYear_Type(Integer32):
    """Custom type wtWebioAn2GraphClockYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtWebioAn2GraphClockYear_Type.__name__ = "Integer32"
_WtWebioAn2GraphClockYear_Object = MibScalar
wtWebioAn2GraphClockYear = _WtWebioAn2GraphClockYear_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 2, 3, 5),
    _WtWebioAn2GraphClockYear_Type()
)
wtWebioAn2GraphClockYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphClockYear.setStatus("mandatory")
_WtWebioAn2GraphBasic_ObjectIdentity = ObjectIdentity
wtWebioAn2GraphBasic = _WtWebioAn2GraphBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3)
)
_WtWebioAn2GraphNetwork_ObjectIdentity = ObjectIdentity
wtWebioAn2GraphNetwork = _WtWebioAn2GraphNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 1)
)
_WtWebioAn2GraphIpAddress_Type = IpAddress
_WtWebioAn2GraphIpAddress_Object = MibScalar
wtWebioAn2GraphIpAddress = _WtWebioAn2GraphIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 1, 1),
    _WtWebioAn2GraphIpAddress_Type()
)
wtWebioAn2GraphIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphIpAddress.setStatus("mandatory")
_WtWebioAn2GraphSubnetMask_Type = IpAddress
_WtWebioAn2GraphSubnetMask_Object = MibScalar
wtWebioAn2GraphSubnetMask = _WtWebioAn2GraphSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 1, 2),
    _WtWebioAn2GraphSubnetMask_Type()
)
wtWebioAn2GraphSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphSubnetMask.setStatus("mandatory")
_WtWebioAn2GraphGateway_Type = IpAddress
_WtWebioAn2GraphGateway_Object = MibScalar
wtWebioAn2GraphGateway = _WtWebioAn2GraphGateway_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 1, 3),
    _WtWebioAn2GraphGateway_Type()
)
wtWebioAn2GraphGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphGateway.setStatus("mandatory")
_WtWebioAn2GraphDnsServer1_Type = OctetString
_WtWebioAn2GraphDnsServer1_Object = MibScalar
wtWebioAn2GraphDnsServer1 = _WtWebioAn2GraphDnsServer1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 1, 4),
    _WtWebioAn2GraphDnsServer1_Type()
)
wtWebioAn2GraphDnsServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphDnsServer1.setStatus("mandatory")
_WtWebioAn2GraphDnsServer2_Type = OctetString
_WtWebioAn2GraphDnsServer2_Object = MibScalar
wtWebioAn2GraphDnsServer2 = _WtWebioAn2GraphDnsServer2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 1, 5),
    _WtWebioAn2GraphDnsServer2_Type()
)
wtWebioAn2GraphDnsServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphDnsServer2.setStatus("mandatory")
_WtWebioAn2GraphAddConfig_Type = OctetString
_WtWebioAn2GraphAddConfig_Object = MibScalar
wtWebioAn2GraphAddConfig = _WtWebioAn2GraphAddConfig_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 1, 6),
    _WtWebioAn2GraphAddConfig_Type()
)
wtWebioAn2GraphAddConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAddConfig.setStatus("mandatory")
_WtWebioAn2GraphHTTP_ObjectIdentity = ObjectIdentity
wtWebioAn2GraphHTTP = _WtWebioAn2GraphHTTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 2)
)
_WtWebioAn2GraphStartup_Type = OctetString
_WtWebioAn2GraphStartup_Object = MibScalar
wtWebioAn2GraphStartup = _WtWebioAn2GraphStartup_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 2, 1),
    _WtWebioAn2GraphStartup_Type()
)
wtWebioAn2GraphStartup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphStartup.setStatus("mandatory")
_WtWebioAn2GraphGetHeaderEnable_Type = OctetString
_WtWebioAn2GraphGetHeaderEnable_Object = MibScalar
wtWebioAn2GraphGetHeaderEnable = _WtWebioAn2GraphGetHeaderEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 2, 2),
    _WtWebioAn2GraphGetHeaderEnable_Type()
)
wtWebioAn2GraphGetHeaderEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphGetHeaderEnable.setStatus("mandatory")


class _WtWebioAn2GraphHttpPort_Type(Integer32):
    """Custom type wtWebioAn2GraphHttpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebioAn2GraphHttpPort_Type.__name__ = "Integer32"
_WtWebioAn2GraphHttpPort_Object = MibScalar
wtWebioAn2GraphHttpPort = _WtWebioAn2GraphHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 2, 3),
    _WtWebioAn2GraphHttpPort_Type()
)
wtWebioAn2GraphHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphHttpPort.setStatus("mandatory")
_WtWebioAn2GraphMail_ObjectIdentity = ObjectIdentity
wtWebioAn2GraphMail = _WtWebioAn2GraphMail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 3)
)
_WtWebioAn2GraphMailAdName_Type = OctetString
_WtWebioAn2GraphMailAdName_Object = MibScalar
wtWebioAn2GraphMailAdName = _WtWebioAn2GraphMailAdName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 3, 1),
    _WtWebioAn2GraphMailAdName_Type()
)
wtWebioAn2GraphMailAdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphMailAdName.setStatus("mandatory")
_WtWebioAn2GraphMailReply_Type = OctetString
_WtWebioAn2GraphMailReply_Object = MibScalar
wtWebioAn2GraphMailReply = _WtWebioAn2GraphMailReply_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 3, 2),
    _WtWebioAn2GraphMailReply_Type()
)
wtWebioAn2GraphMailReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphMailReply.setStatus("mandatory")
_WtWebioAn2GraphMailServer_Type = OctetString
_WtWebioAn2GraphMailServer_Object = MibScalar
wtWebioAn2GraphMailServer = _WtWebioAn2GraphMailServer_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 3, 3),
    _WtWebioAn2GraphMailServer_Type()
)
wtWebioAn2GraphMailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphMailServer.setStatus("mandatory")
_WtWebioAn1MailEnable_Type = OctetString
_WtWebioAn1MailEnable_Object = MibScalar
wtWebioAn1MailEnable = _WtWebioAn1MailEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 3, 4),
    _WtWebioAn1MailEnable_Type()
)
wtWebioAn1MailEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1MailEnable.setStatus("mandatory")


class _WtWebioAn2GraphMailAuthentication_Type(OctetString):
    """Custom type wtWebioAn2GraphMailAuthentication based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebioAn2GraphMailAuthentication_Type.__name__ = "OctetString"
_WtWebioAn2GraphMailAuthentication_Object = MibScalar
wtWebioAn2GraphMailAuthentication = _WtWebioAn2GraphMailAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 3, 5),
    _WtWebioAn2GraphMailAuthentication_Type()
)
wtWebioAn2GraphMailAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphMailAuthentication.setStatus("mandatory")
_WtWebioAn2GraphMailAuthUser_Type = OctetString
_WtWebioAn2GraphMailAuthUser_Object = MibScalar
wtWebioAn2GraphMailAuthUser = _WtWebioAn2GraphMailAuthUser_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 3, 6),
    _WtWebioAn2GraphMailAuthUser_Type()
)
wtWebioAn2GraphMailAuthUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphMailAuthUser.setStatus("mandatory")
_WtWebioAn2GraphMailAuthPassword_Type = OctetString
_WtWebioAn2GraphMailAuthPassword_Object = MibScalar
wtWebioAn2GraphMailAuthPassword = _WtWebioAn2GraphMailAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 3, 7),
    _WtWebioAn2GraphMailAuthPassword_Type()
)
wtWebioAn2GraphMailAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphMailAuthPassword.setStatus("mandatory")
_WtWebioAn2GraphMailPop3Server_Type = OctetString
_WtWebioAn2GraphMailPop3Server_Object = MibScalar
wtWebioAn2GraphMailPop3Server = _WtWebioAn2GraphMailPop3Server_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 3, 8),
    _WtWebioAn2GraphMailPop3Server_Type()
)
wtWebioAn2GraphMailPop3Server.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphMailPop3Server.setStatus("mandatory")
_WtWebioAn2GraphSNMP_ObjectIdentity = ObjectIdentity
wtWebioAn2GraphSNMP = _WtWebioAn2GraphSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 4)
)
_WtWebioAn2GraphSnmpCommunityStringRead_Type = OctetString
_WtWebioAn2GraphSnmpCommunityStringRead_Object = MibScalar
wtWebioAn2GraphSnmpCommunityStringRead = _WtWebioAn2GraphSnmpCommunityStringRead_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 4, 1),
    _WtWebioAn2GraphSnmpCommunityStringRead_Type()
)
wtWebioAn2GraphSnmpCommunityStringRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphSnmpCommunityStringRead.setStatus("mandatory")
_WtWebioAn2GraphSnmpCommunityStringReadWrite_Type = OctetString
_WtWebioAn2GraphSnmpCommunityStringReadWrite_Object = MibScalar
wtWebioAn2GraphSnmpCommunityStringReadWrite = _WtWebioAn2GraphSnmpCommunityStringReadWrite_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 4, 2),
    _WtWebioAn2GraphSnmpCommunityStringReadWrite_Type()
)
wtWebioAn2GraphSnmpCommunityStringReadWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphSnmpCommunityStringReadWrite.setStatus("mandatory")
_WtWebioAn2GraphSystemTrapManagerIP_Type = OctetString
_WtWebioAn2GraphSystemTrapManagerIP_Object = MibScalar
wtWebioAn2GraphSystemTrapManagerIP = _WtWebioAn2GraphSystemTrapManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 4, 3),
    _WtWebioAn2GraphSystemTrapManagerIP_Type()
)
wtWebioAn2GraphSystemTrapManagerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphSystemTrapManagerIP.setStatus("mandatory")


class _WtWebioAn2GraphSystemTrapEnable_Type(OctetString):
    """Custom type wtWebioAn2GraphSystemTrapEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebioAn2GraphSystemTrapEnable_Type.__name__ = "OctetString"
_WtWebioAn2GraphSystemTrapEnable_Object = MibScalar
wtWebioAn2GraphSystemTrapEnable = _WtWebioAn2GraphSystemTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 4, 4),
    _WtWebioAn2GraphSystemTrapEnable_Type()
)
wtWebioAn2GraphSystemTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphSystemTrapEnable.setStatus("mandatory")
_WtWebioAn2GraphSnmpEnable_Type = OctetString
_WtWebioAn2GraphSnmpEnable_Object = MibScalar
wtWebioAn2GraphSnmpEnable = _WtWebioAn2GraphSnmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 4, 5),
    _WtWebioAn2GraphSnmpEnable_Type()
)
wtWebioAn2GraphSnmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphSnmpEnable.setStatus("mandatory")
_WtWebioAn2GraphSnmpCommunityStringTrap_Type = OctetString
_WtWebioAn2GraphSnmpCommunityStringTrap_Object = MibScalar
wtWebioAn2GraphSnmpCommunityStringTrap = _WtWebioAn2GraphSnmpCommunityStringTrap_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 4, 6),
    _WtWebioAn2GraphSnmpCommunityStringTrap_Type()
)
wtWebioAn2GraphSnmpCommunityStringTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphSnmpCommunityStringTrap.setStatus("mandatory")
_WtWebioAn2GraphSnmpSystemTrapManagerPort_Type = Integer32
_WtWebioAn2GraphSnmpSystemTrapManagerPort_Object = MibScalar
wtWebioAn2GraphSnmpSystemTrapManagerPort = _WtWebioAn2GraphSnmpSystemTrapManagerPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 4, 7),
    _WtWebioAn2GraphSnmpSystemTrapManagerPort_Type()
)
wtWebioAn2GraphSnmpSystemTrapManagerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphSnmpSystemTrapManagerPort.setStatus("mandatory")
_WtWebioAn2GraphUDP_ObjectIdentity = ObjectIdentity
wtWebioAn2GraphUDP = _WtWebioAn2GraphUDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 5)
)


class _WtWebioAn2GraphUdpPort_Type(Integer32):
    """Custom type wtWebioAn2GraphUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebioAn2GraphUdpPort_Type.__name__ = "Integer32"
_WtWebioAn2GraphUdpPort_Object = MibScalar
wtWebioAn2GraphUdpPort = _WtWebioAn2GraphUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 5, 1),
    _WtWebioAn2GraphUdpPort_Type()
)
wtWebioAn2GraphUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphUdpPort.setStatus("mandatory")
_WtWebioAn2GraphUdpEnable_Type = OctetString
_WtWebioAn2GraphUdpEnable_Object = MibScalar
wtWebioAn2GraphUdpEnable = _WtWebioAn2GraphUdpEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 5, 2),
    _WtWebioAn2GraphUdpEnable_Type()
)
wtWebioAn2GraphUdpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphUdpEnable.setStatus("mandatory")
_WtWebioAn2GraphSyslog_ObjectIdentity = ObjectIdentity
wtWebioAn2GraphSyslog = _WtWebioAn2GraphSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 6)
)
_WtWebioAn2GraphSyslogServerIP_Type = OctetString
_WtWebioAn2GraphSyslogServerIP_Object = MibScalar
wtWebioAn2GraphSyslogServerIP = _WtWebioAn2GraphSyslogServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 6, 1),
    _WtWebioAn2GraphSyslogServerIP_Type()
)
wtWebioAn2GraphSyslogServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphSyslogServerIP.setStatus("mandatory")
_WtWebioAn2GraphSyslogServerPort_Type = Integer32
_WtWebioAn2GraphSyslogServerPort_Object = MibScalar
wtWebioAn2GraphSyslogServerPort = _WtWebioAn2GraphSyslogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 6, 2),
    _WtWebioAn2GraphSyslogServerPort_Type()
)
wtWebioAn2GraphSyslogServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphSyslogServerPort.setStatus("mandatory")


class _WtWebioAn2GraphSyslogSystemMessagesEnable_Type(OctetString):
    """Custom type wtWebioAn2GraphSyslogSystemMessagesEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebioAn2GraphSyslogSystemMessagesEnable_Type.__name__ = "OctetString"
_WtWebioAn2GraphSyslogSystemMessagesEnable_Object = MibScalar
wtWebioAn2GraphSyslogSystemMessagesEnable = _WtWebioAn2GraphSyslogSystemMessagesEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 6, 3),
    _WtWebioAn2GraphSyslogSystemMessagesEnable_Type()
)
wtWebioAn2GraphSyslogSystemMessagesEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphSyslogSystemMessagesEnable.setStatus("mandatory")
_WtWebioAn2GraphSyslogEnable_Type = OctetString
_WtWebioAn2GraphSyslogEnable_Object = MibScalar
wtWebioAn2GraphSyslogEnable = _WtWebioAn2GraphSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 6, 4),
    _WtWebioAn2GraphSyslogEnable_Type()
)
wtWebioAn2GraphSyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphSyslogEnable.setStatus("mandatory")
_WtWebioAn2GraphFTP_ObjectIdentity = ObjectIdentity
wtWebioAn2GraphFTP = _WtWebioAn2GraphFTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 7)
)
_WtWebioAn2GraphFTPServerIP_Type = OctetString
_WtWebioAn2GraphFTPServerIP_Object = MibScalar
wtWebioAn2GraphFTPServerIP = _WtWebioAn2GraphFTPServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 7, 1),
    _WtWebioAn2GraphFTPServerIP_Type()
)
wtWebioAn2GraphFTPServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphFTPServerIP.setStatus("mandatory")
_WtWebioAn2GraphFTPServerControlPort_Type = Integer32
_WtWebioAn2GraphFTPServerControlPort_Object = MibScalar
wtWebioAn2GraphFTPServerControlPort = _WtWebioAn2GraphFTPServerControlPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 7, 2),
    _WtWebioAn2GraphFTPServerControlPort_Type()
)
wtWebioAn2GraphFTPServerControlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphFTPServerControlPort.setStatus("mandatory")
_WtWebioAn2GraphFTPUserName_Type = OctetString
_WtWebioAn2GraphFTPUserName_Object = MibScalar
wtWebioAn2GraphFTPUserName = _WtWebioAn2GraphFTPUserName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 7, 3),
    _WtWebioAn2GraphFTPUserName_Type()
)
wtWebioAn2GraphFTPUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphFTPUserName.setStatus("mandatory")
_WtWebioAn2GraphFTPPassword_Type = OctetString
_WtWebioAn2GraphFTPPassword_Object = MibScalar
wtWebioAn2GraphFTPPassword = _WtWebioAn2GraphFTPPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 7, 4),
    _WtWebioAn2GraphFTPPassword_Type()
)
wtWebioAn2GraphFTPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphFTPPassword.setStatus("mandatory")
_WtWebioAn2GraphFTPAccount_Type = OctetString
_WtWebioAn2GraphFTPAccount_Object = MibScalar
wtWebioAn2GraphFTPAccount = _WtWebioAn2GraphFTPAccount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 7, 5),
    _WtWebioAn2GraphFTPAccount_Type()
)
wtWebioAn2GraphFTPAccount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphFTPAccount.setStatus("mandatory")
_WtWebioAn2GraphFTPOption_Type = OctetString
_WtWebioAn2GraphFTPOption_Object = MibScalar
wtWebioAn2GraphFTPOption = _WtWebioAn2GraphFTPOption_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 7, 6),
    _WtWebioAn2GraphFTPOption_Type()
)
wtWebioAn2GraphFTPOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphFTPOption.setStatus("mandatory")
_WtWebioAn2GraphFTPEnable_Type = OctetString
_WtWebioAn2GraphFTPEnable_Object = MibScalar
wtWebioAn2GraphFTPEnable = _WtWebioAn2GraphFTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 7, 7),
    _WtWebioAn2GraphFTPEnable_Type()
)
wtWebioAn2GraphFTPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphFTPEnable.setStatus("mandatory")
_WtWebioAn2GraphLanguage_ObjectIdentity = ObjectIdentity
wtWebioAn2GraphLanguage = _WtWebioAn2GraphLanguage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 9)
)
_WtWebioAn2GraphLanguageSelect_Type = OctetString
_WtWebioAn2GraphLanguageSelect_Object = MibScalar
wtWebioAn2GraphLanguageSelect = _WtWebioAn2GraphLanguageSelect_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 9, 1),
    _WtWebioAn2GraphLanguageSelect_Type()
)
wtWebioAn2GraphLanguageSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphLanguageSelect.setStatus("mandatory")
_WtWebioAn2GraphMQTT_ObjectIdentity = ObjectIdentity
wtWebioAn2GraphMQTT = _WtWebioAn2GraphMQTT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 12)
)
_WtWebioAn2GraphMQTTEnable_Type = OctetString
_WtWebioAn2GraphMQTTEnable_Object = MibScalar
wtWebioAn2GraphMQTTEnable = _WtWebioAn2GraphMQTTEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 12, 1),
    _WtWebioAn2GraphMQTTEnable_Type()
)
wtWebioAn2GraphMQTTEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphMQTTEnable.setStatus("mandatory")
_WtWebioAn2GraphMQTTBrockerIP_Type = OctetString
_WtWebioAn2GraphMQTTBrockerIP_Object = MibScalar
wtWebioAn2GraphMQTTBrockerIP = _WtWebioAn2GraphMQTTBrockerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 12, 2),
    _WtWebioAn2GraphMQTTBrockerIP_Type()
)
wtWebioAn2GraphMQTTBrockerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphMQTTBrockerIP.setStatus("mandatory")
_WtWebioAn2GraphMQTTUserName_Type = OctetString
_WtWebioAn2GraphMQTTUserName_Object = MibScalar
wtWebioAn2GraphMQTTUserName = _WtWebioAn2GraphMQTTUserName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 12, 3),
    _WtWebioAn2GraphMQTTUserName_Type()
)
wtWebioAn2GraphMQTTUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphMQTTUserName.setStatus("mandatory")
_WtWebioAn2GraphMQTTPassword_Type = OctetString
_WtWebioAn2GraphMQTTPassword_Object = MibScalar
wtWebioAn2GraphMQTTPassword = _WtWebioAn2GraphMQTTPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 12, 4),
    _WtWebioAn2GraphMQTTPassword_Type()
)
wtWebioAn2GraphMQTTPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphMQTTPassword.setStatus("mandatory")
_WtWebioAn2GraphMQTTLocalPort_Type = Integer32
_WtWebioAn2GraphMQTTLocalPort_Object = MibScalar
wtWebioAn2GraphMQTTLocalPort = _WtWebioAn2GraphMQTTLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 12, 5),
    _WtWebioAn2GraphMQTTLocalPort_Type()
)
wtWebioAn2GraphMQTTLocalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphMQTTLocalPort.setStatus("mandatory")
_WtWebioAn2GraphMQTTBrokerServerPort_Type = Integer32
_WtWebioAn2GraphMQTTBrokerServerPort_Object = MibScalar
wtWebioAn2GraphMQTTBrokerServerPort = _WtWebioAn2GraphMQTTBrokerServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 12, 6),
    _WtWebioAn2GraphMQTTBrokerServerPort_Type()
)
wtWebioAn2GraphMQTTBrokerServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphMQTTBrokerServerPort.setStatus("mandatory")
_WtWebioAn2GraphMQTTInterval_Type = Integer32
_WtWebioAn2GraphMQTTInterval_Object = MibScalar
wtWebioAn2GraphMQTTInterval = _WtWebioAn2GraphMQTTInterval_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 12, 7),
    _WtWebioAn2GraphMQTTInterval_Type()
)
wtWebioAn2GraphMQTTInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphMQTTInterval.setStatus("mandatory")
_WtWebioAn2GraphMQTTLastWillEnable_Type = OctetString
_WtWebioAn2GraphMQTTLastWillEnable_Object = MibScalar
wtWebioAn2GraphMQTTLastWillEnable = _WtWebioAn2GraphMQTTLastWillEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 12, 8),
    _WtWebioAn2GraphMQTTLastWillEnable_Type()
)
wtWebioAn2GraphMQTTLastWillEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphMQTTLastWillEnable.setStatus("mandatory")
_WtWebioAn2GraphMQTTLastWillTopic_Type = OctetString
_WtWebioAn2GraphMQTTLastWillTopic_Object = MibScalar
wtWebioAn2GraphMQTTLastWillTopic = _WtWebioAn2GraphMQTTLastWillTopic_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 12, 9),
    _WtWebioAn2GraphMQTTLastWillTopic_Type()
)
wtWebioAn2GraphMQTTLastWillTopic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphMQTTLastWillTopic.setStatus("mandatory")
_WtWebioAn2GraphMQTTLastWillMsg_Type = OctetString
_WtWebioAn2GraphMQTTLastWillMsg_Object = MibScalar
wtWebioAn2GraphMQTTLastWillMsg = _WtWebioAn2GraphMQTTLastWillMsg_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 12, 10),
    _WtWebioAn2GraphMQTTLastWillMsg_Type()
)
wtWebioAn2GraphMQTTLastWillMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphMQTTLastWillMsg.setStatus("mandatory")


class _WtWebioAn2GraphMQTTLastWillQoS_Type(OctetString):
    """Custom type wtWebioAn2GraphMQTTLastWillQoS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebioAn2GraphMQTTLastWillQoS_Type.__name__ = "OctetString"
_WtWebioAn2GraphMQTTLastWillQoS_Object = MibScalar
wtWebioAn2GraphMQTTLastWillQoS = _WtWebioAn2GraphMQTTLastWillQoS_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 12, 11),
    _WtWebioAn2GraphMQTTLastWillQoS_Type()
)
wtWebioAn2GraphMQTTLastWillQoS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphMQTTLastWillQoS.setStatus("mandatory")


class _WtWebioAn2GraphMQTTLastWillRetain_Type(OctetString):
    """Custom type wtWebioAn2GraphMQTTLastWillRetain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebioAn2GraphMQTTLastWillRetain_Type.__name__ = "OctetString"
_WtWebioAn2GraphMQTTLastWillRetain_Object = MibScalar
wtWebioAn2GraphMQTTLastWillRetain = _WtWebioAn2GraphMQTTLastWillRetain_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 12, 12),
    _WtWebioAn2GraphMQTTLastWillRetain_Type()
)
wtWebioAn2GraphMQTTLastWillRetain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphMQTTLastWillRetain.setStatus("mandatory")
_WtWebioAn2GraphMQTTLastWillConnectEnable_Type = OctetString
_WtWebioAn2GraphMQTTLastWillConnectEnable_Object = MibScalar
wtWebioAn2GraphMQTTLastWillConnectEnable = _WtWebioAn2GraphMQTTLastWillConnectEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 12, 13),
    _WtWebioAn2GraphMQTTLastWillConnectEnable_Type()
)
wtWebioAn2GraphMQTTLastWillConnectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphMQTTLastWillConnectEnable.setStatus("mandatory")
_WtWebioAn2GraphMQTTLastWillConnectMsg_Type = OctetString
_WtWebioAn2GraphMQTTLastWillConnectMsg_Object = MibScalar
wtWebioAn2GraphMQTTLastWillConnectMsg = _WtWebioAn2GraphMQTTLastWillConnectMsg_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 12, 14),
    _WtWebioAn2GraphMQTTLastWillConnectMsg_Type()
)
wtWebioAn2GraphMQTTLastWillConnectMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphMQTTLastWillConnectMsg.setStatus("mandatory")
_WtWebioAn2GraphREST_ObjectIdentity = ObjectIdentity
wtWebioAn2GraphREST = _WtWebioAn2GraphREST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 13)
)
_WtWebioAn2GraphRESTEnable_Type = OctetString
_WtWebioAn2GraphRESTEnable_Object = MibScalar
wtWebioAn2GraphRESTEnable = _WtWebioAn2GraphRESTEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 13, 1),
    _WtWebioAn2GraphRESTEnable_Type()
)
wtWebioAn2GraphRESTEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphRESTEnable.setStatus("mandatory")
_WtWebioAn2GraphRESTDigestAuthEnable_Type = OctetString
_WtWebioAn2GraphRESTDigestAuthEnable_Object = MibScalar
wtWebioAn2GraphRESTDigestAuthEnable = _WtWebioAn2GraphRESTDigestAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 3, 13, 2),
    _WtWebioAn2GraphRESTDigestAuthEnable_Type()
)
wtWebioAn2GraphRESTDigestAuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphRESTDigestAuthEnable.setStatus("mandatory")
_WtWebioAn2GraphDatalogger_ObjectIdentity = ObjectIdentity
wtWebioAn2GraphDatalogger = _WtWebioAn2GraphDatalogger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 4)
)


class _WtWebioAn2GraphLoggerTimebase_Type(Integer32):
    """Custom type wtWebioAn2GraphLoggerTimebase based on Integer32"""
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
        *(("wtWebioAn2GraphDatalogger-1Min", 1),
          ("wtWebioAn2GraphDatalogger-5Min", 2),
          ("wtWebioAn2GraphDatalogger-15Min", 3),
          ("wtWebioAn2GraphDatalogger-60Min", 4))
    )


_WtWebioAn2GraphLoggerTimebase_Type.__name__ = "Integer32"
_WtWebioAn2GraphLoggerTimebase_Object = MibScalar
wtWebioAn2GraphLoggerTimebase = _WtWebioAn2GraphLoggerTimebase_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 4, 1),
    _WtWebioAn2GraphLoggerTimebase_Type()
)
wtWebioAn2GraphLoggerTimebase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphLoggerTimebase.setStatus("mandatory")


class _WtWebioAn2GraphLoggerSensorSel_Type(OctetString):
    """Custom type wtWebioAn2GraphLoggerSensorSel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebioAn2GraphLoggerSensorSel_Type.__name__ = "OctetString"
_WtWebioAn2GraphLoggerSensorSel_Object = MibScalar
wtWebioAn2GraphLoggerSensorSel = _WtWebioAn2GraphLoggerSensorSel_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 4, 2),
    _WtWebioAn2GraphLoggerSensorSel_Type()
)
wtWebioAn2GraphLoggerSensorSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphLoggerSensorSel.setStatus("mandatory")


class _WtWebioAn2GraphDisplaySensorSel_Type(OctetString):
    """Custom type wtWebioAn2GraphDisplaySensorSel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebioAn2GraphDisplaySensorSel_Type.__name__ = "OctetString"
_WtWebioAn2GraphDisplaySensorSel_Object = MibScalar
wtWebioAn2GraphDisplaySensorSel = _WtWebioAn2GraphDisplaySensorSel_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 4, 3),
    _WtWebioAn2GraphDisplaySensorSel_Type()
)
wtWebioAn2GraphDisplaySensorSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphDisplaySensorSel.setStatus("mandatory")
_WtWebioAn2GraphSensorColorTable_Object = MibTable
wtWebioAn2GraphSensorColorTable = _WtWebioAn2GraphSensorColorTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 4, 4)
)
if mibBuilder.loadTexts:
    wtWebioAn2GraphSensorColorTable.setStatus("mandatory")
_WtWebioAn2GraphSensorColorEntry_Object = MibTableRow
wtWebioAn2GraphSensorColorEntry = _WtWebioAn2GraphSensorColorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 4, 4, 1)
)
wtWebioAn2GraphSensorColorEntry.setIndexNames(
    (0, "WebGraph-2xThermometer-US-MIB", "wtWebioAn2GraphSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn2GraphSensorColorEntry.setStatus("mandatory")


class _WtWebioAn2GraphSensorColor_Type(OctetString):
    """Custom type wtWebioAn2GraphSensorColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_WtWebioAn2GraphSensorColor_Type.__name__ = "OctetString"
_WtWebioAn2GraphSensorColor_Object = MibTableColumn
wtWebioAn2GraphSensorColor = _WtWebioAn2GraphSensorColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 4, 4, 1, 1),
    _WtWebioAn2GraphSensorColor_Type()
)
wtWebioAn2GraphSensorColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphSensorColor.setStatus("mandatory")
_WtWebioAn2GraphAutoScaleEnable_Type = OctetString
_WtWebioAn2GraphAutoScaleEnable_Object = MibScalar
wtWebioAn2GraphAutoScaleEnable = _WtWebioAn2GraphAutoScaleEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 4, 5),
    _WtWebioAn2GraphAutoScaleEnable_Type()
)
wtWebioAn2GraphAutoScaleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAutoScaleEnable.setStatus("mandatory")
_WtWebioAn2GraphVerticalUpperLimit_Type = OctetString
_WtWebioAn2GraphVerticalUpperLimit_Object = MibScalar
wtWebioAn2GraphVerticalUpperLimit = _WtWebioAn2GraphVerticalUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 4, 6),
    _WtWebioAn2GraphVerticalUpperLimit_Type()
)
wtWebioAn2GraphVerticalUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphVerticalUpperLimit.setStatus("mandatory")
_WtWebioAn2GraphVerticalLowerLimit_Type = OctetString
_WtWebioAn2GraphVerticalLowerLimit_Object = MibScalar
wtWebioAn2GraphVerticalLowerLimit = _WtWebioAn2GraphVerticalLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 4, 7),
    _WtWebioAn2GraphVerticalLowerLimit_Type()
)
wtWebioAn2GraphVerticalLowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphVerticalLowerLimit.setStatus("mandatory")


class _WtWebioAn2GraphHorizontalZoom_Type(Integer32):
    """Custom type wtWebioAn2GraphHorizontalZoom based on Integer32"""
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
        *(("wtWebioAn2GraphZoom-25min", 1),
          ("wtWebioAn2GraphZoom-75min", 2),
          ("wtWebioAn2GraphZoom-5hrs", 3),
          ("wtWebioAn2GraphZoom-30hrs", 4),
          ("wtWebioAn2GraphZoom-5days", 5),
          ("wtWebioAn2GraphZoom-25days", 6))
    )


_WtWebioAn2GraphHorizontalZoom_Type.__name__ = "Integer32"
_WtWebioAn2GraphHorizontalZoom_Object = MibScalar
wtWebioAn2GraphHorizontalZoom = _WtWebioAn2GraphHorizontalZoom_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 4, 8),
    _WtWebioAn2GraphHorizontalZoom_Type()
)
wtWebioAn2GraphHorizontalZoom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphHorizontalZoom.setStatus("mandatory")
_WtWebioAn2GraphAlarm_ObjectIdentity = ObjectIdentity
wtWebioAn2GraphAlarm = _WtWebioAn2GraphAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5)
)


class _WtWebioAn2GraphAlarmCount_Type(Integer32):
    """Custom type wtWebioAn2GraphAlarmCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WtWebioAn2GraphAlarmCount_Type.__name__ = "Integer32"
_WtWebioAn2GraphAlarmCount_Object = MibScalar
wtWebioAn2GraphAlarmCount = _WtWebioAn2GraphAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 1),
    _WtWebioAn2GraphAlarmCount_Type()
)
wtWebioAn2GraphAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmCount.setStatus("mandatory")
_WtWebioAn2GraphAlarmIfTable_Object = MibTable
wtWebioAn2GraphAlarmIfTable = _WtWebioAn2GraphAlarmIfTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 2)
)
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmIfTable.setStatus("mandatory")
_WtWebioAn2GraphAlarmIfEntry_Object = MibTableRow
wtWebioAn2GraphAlarmIfEntry = _WtWebioAn2GraphAlarmIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 2, 1)
)
wtWebioAn2GraphAlarmIfEntry.setIndexNames(
    (0, "WebGraph-2xThermometer-US-MIB", "wtWebioAn2GraphAlarmNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmIfEntry.setStatus("mandatory")


class _WtWebioAn2GraphAlarmNo_Type(Integer32):
    """Custom type wtWebioAn2GraphAlarmNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WtWebioAn2GraphAlarmNo_Type.__name__ = "Integer32"
_WtWebioAn2GraphAlarmNo_Object = MibTableColumn
wtWebioAn2GraphAlarmNo = _WtWebioAn2GraphAlarmNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 2, 1, 1),
    _WtWebioAn2GraphAlarmNo_Type()
)
wtWebioAn2GraphAlarmNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmNo.setStatus("mandatory")
_WtWebioAn2GraphAlarmTable_Object = MibTable
wtWebioAn2GraphAlarmTable = _WtWebioAn2GraphAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3)
)
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmTable.setStatus("mandatory")
_WtWebioAn2GraphAlarmEntry_Object = MibTableRow
wtWebioAn2GraphAlarmEntry = _WtWebioAn2GraphAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1)
)
wtWebioAn2GraphAlarmEntry.setIndexNames(
    (0, "WebGraph-2xThermometer-US-MIB", "wtWebioAn2GraphAlarmNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmEntry.setStatus("mandatory")


class _WtWebioAn2GraphAlarmTrigger_Type(OctetString):
    """Custom type wtWebioAn2GraphAlarmTrigger based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebioAn2GraphAlarmTrigger_Type.__name__ = "OctetString"
_WtWebioAn2GraphAlarmTrigger_Object = MibTableColumn
wtWebioAn2GraphAlarmTrigger = _WtWebioAn2GraphAlarmTrigger_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 1),
    _WtWebioAn2GraphAlarmTrigger_Type()
)
wtWebioAn2GraphAlarmTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmTrigger.setStatus("mandatory")
_WtWebioAn2GraphAlarmMin_Type = OctetString
_WtWebioAn2GraphAlarmMin_Object = MibTableColumn
wtWebioAn2GraphAlarmMin = _WtWebioAn2GraphAlarmMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 2),
    _WtWebioAn2GraphAlarmMin_Type()
)
wtWebioAn2GraphAlarmMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmMin.setStatus("mandatory")
_WtWebioAn2GraphAlarmMax_Type = OctetString
_WtWebioAn2GraphAlarmMax_Object = MibTableColumn
wtWebioAn2GraphAlarmMax = _WtWebioAn2GraphAlarmMax_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 3),
    _WtWebioAn2GraphAlarmMax_Type()
)
wtWebioAn2GraphAlarmMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmMax.setStatus("mandatory")
_WtWebioAn2GraphAlarmHysteresis_Type = OctetString
_WtWebioAn2GraphAlarmHysteresis_Object = MibTableColumn
wtWebioAn2GraphAlarmHysteresis = _WtWebioAn2GraphAlarmHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 4),
    _WtWebioAn2GraphAlarmHysteresis_Type()
)
wtWebioAn2GraphAlarmHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmHysteresis.setStatus("mandatory")
_WtWebioAn2GraphAlarmDelay_Type = OctetString
_WtWebioAn2GraphAlarmDelay_Object = MibTableColumn
wtWebioAn2GraphAlarmDelay = _WtWebioAn2GraphAlarmDelay_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 5),
    _WtWebioAn2GraphAlarmDelay_Type()
)
wtWebioAn2GraphAlarmDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmDelay.setStatus("mandatory")
_WtWebioAn2GraphAlarmInterval_Type = OctetString
_WtWebioAn2GraphAlarmInterval_Object = MibTableColumn
wtWebioAn2GraphAlarmInterval = _WtWebioAn2GraphAlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 6),
    _WtWebioAn2GraphAlarmInterval_Type()
)
wtWebioAn2GraphAlarmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmInterval.setStatus("mandatory")


class _WtWebioAn2GraphAlarmEnable_Type(OctetString):
    """Custom type wtWebioAn2GraphAlarmEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebioAn2GraphAlarmEnable_Type.__name__ = "OctetString"
_WtWebioAn2GraphAlarmEnable_Object = MibTableColumn
wtWebioAn2GraphAlarmEnable = _WtWebioAn2GraphAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 7),
    _WtWebioAn2GraphAlarmEnable_Type()
)
wtWebioAn2GraphAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmEnable.setStatus("mandatory")
_WtWebioAn2GraphAlarmEMailAddr_Type = OctetString
_WtWebioAn2GraphAlarmEMailAddr_Object = MibTableColumn
wtWebioAn2GraphAlarmEMailAddr = _WtWebioAn2GraphAlarmEMailAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 8),
    _WtWebioAn2GraphAlarmEMailAddr_Type()
)
wtWebioAn2GraphAlarmEMailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmEMailAddr.setStatus("mandatory")
_WtWebioAn2GraphAlarmMailSubject_Type = OctetString
_WtWebioAn2GraphAlarmMailSubject_Object = MibTableColumn
wtWebioAn2GraphAlarmMailSubject = _WtWebioAn2GraphAlarmMailSubject_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 9),
    _WtWebioAn2GraphAlarmMailSubject_Type()
)
wtWebioAn2GraphAlarmMailSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmMailSubject.setStatus("mandatory")
_WtWebioAn2GraphAlarmMailText_Type = OctetString
_WtWebioAn2GraphAlarmMailText_Object = MibTableColumn
wtWebioAn2GraphAlarmMailText = _WtWebioAn2GraphAlarmMailText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 10),
    _WtWebioAn2GraphAlarmMailText_Type()
)
wtWebioAn2GraphAlarmMailText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmMailText.setStatus("mandatory")
_WtWebioAn2GraphAlarmManagerIP_Type = OctetString
_WtWebioAn2GraphAlarmManagerIP_Object = MibTableColumn
wtWebioAn2GraphAlarmManagerIP = _WtWebioAn2GraphAlarmManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 11),
    _WtWebioAn2GraphAlarmManagerIP_Type()
)
wtWebioAn2GraphAlarmManagerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmManagerIP.setStatus("mandatory")
_WtWebioAn2GraphAlarmTrapText_Type = OctetString
_WtWebioAn2GraphAlarmTrapText_Object = MibTableColumn
wtWebioAn2GraphAlarmTrapText = _WtWebioAn2GraphAlarmTrapText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 12),
    _WtWebioAn2GraphAlarmTrapText_Type()
)
wtWebioAn2GraphAlarmTrapText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmTrapText.setStatus("mandatory")


class _WtWebioAn2GraphAlarmMailOptions_Type(OctetString):
    """Custom type wtWebioAn2GraphAlarmMailOptions based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebioAn2GraphAlarmMailOptions_Type.__name__ = "OctetString"
_WtWebioAn2GraphAlarmMailOptions_Object = MibTableColumn
wtWebioAn2GraphAlarmMailOptions = _WtWebioAn2GraphAlarmMailOptions_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 13),
    _WtWebioAn2GraphAlarmMailOptions_Type()
)
wtWebioAn2GraphAlarmMailOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmMailOptions.setStatus("mandatory")
_WtWebioAn2GraphAlarmTcpIpAddr_Type = OctetString
_WtWebioAn2GraphAlarmTcpIpAddr_Object = MibTableColumn
wtWebioAn2GraphAlarmTcpIpAddr = _WtWebioAn2GraphAlarmTcpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 14),
    _WtWebioAn2GraphAlarmTcpIpAddr_Type()
)
wtWebioAn2GraphAlarmTcpIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmTcpIpAddr.setStatus("mandatory")


class _WtWebioAn2GraphAlarmTcpPort_Type(Integer32):
    """Custom type wtWebioAn2GraphAlarmTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebioAn2GraphAlarmTcpPort_Type.__name__ = "Integer32"
_WtWebioAn2GraphAlarmTcpPort_Object = MibTableColumn
wtWebioAn2GraphAlarmTcpPort = _WtWebioAn2GraphAlarmTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 15),
    _WtWebioAn2GraphAlarmTcpPort_Type()
)
wtWebioAn2GraphAlarmTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmTcpPort.setStatus("mandatory")
_WtWebioAn2GraphAlarmTcpText_Type = OctetString
_WtWebioAn2GraphAlarmTcpText_Object = MibTableColumn
wtWebioAn2GraphAlarmTcpText = _WtWebioAn2GraphAlarmTcpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 16),
    _WtWebioAn2GraphAlarmTcpText_Type()
)
wtWebioAn2GraphAlarmTcpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmTcpText.setStatus("mandatory")
_WtWebioAn2GraphAlarmClearMailSubject_Type = OctetString
_WtWebioAn2GraphAlarmClearMailSubject_Object = MibTableColumn
wtWebioAn2GraphAlarmClearMailSubject = _WtWebioAn2GraphAlarmClearMailSubject_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 17),
    _WtWebioAn2GraphAlarmClearMailSubject_Type()
)
wtWebioAn2GraphAlarmClearMailSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmClearMailSubject.setStatus("mandatory")
_WtWebioAn2GraphAlarmClearMailText_Type = OctetString
_WtWebioAn2GraphAlarmClearMailText_Object = MibTableColumn
wtWebioAn2GraphAlarmClearMailText = _WtWebioAn2GraphAlarmClearMailText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 18),
    _WtWebioAn2GraphAlarmClearMailText_Type()
)
wtWebioAn2GraphAlarmClearMailText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmClearMailText.setStatus("mandatory")
_WtWebioAn2GraphAlarmClearTrapText_Type = OctetString
_WtWebioAn2GraphAlarmClearTrapText_Object = MibTableColumn
wtWebioAn2GraphAlarmClearTrapText = _WtWebioAn2GraphAlarmClearTrapText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 19),
    _WtWebioAn2GraphAlarmClearTrapText_Type()
)
wtWebioAn2GraphAlarmClearTrapText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmClearTrapText.setStatus("mandatory")
_WtWebioAn2GraphAlarmClearTcpText_Type = OctetString
_WtWebioAn2GraphAlarmClearTcpText_Object = MibTableColumn
wtWebioAn2GraphAlarmClearTcpText = _WtWebioAn2GraphAlarmClearTcpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 20),
    _WtWebioAn2GraphAlarmClearTcpText_Type()
)
wtWebioAn2GraphAlarmClearTcpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmClearTcpText.setStatus("mandatory")
_WtWebioAn2GraphAlarmSyslogIpAddr_Type = OctetString
_WtWebioAn2GraphAlarmSyslogIpAddr_Object = MibTableColumn
wtWebioAn2GraphAlarmSyslogIpAddr = _WtWebioAn2GraphAlarmSyslogIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 21),
    _WtWebioAn2GraphAlarmSyslogIpAddr_Type()
)
wtWebioAn2GraphAlarmSyslogIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmSyslogIpAddr.setStatus("mandatory")


class _WtWebioAn2GraphAlarmSyslogPort_Type(Integer32):
    """Custom type wtWebioAn2GraphAlarmSyslogPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebioAn2GraphAlarmSyslogPort_Type.__name__ = "Integer32"
_WtWebioAn2GraphAlarmSyslogPort_Object = MibTableColumn
wtWebioAn2GraphAlarmSyslogPort = _WtWebioAn2GraphAlarmSyslogPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 22),
    _WtWebioAn2GraphAlarmSyslogPort_Type()
)
wtWebioAn2GraphAlarmSyslogPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmSyslogPort.setStatus("mandatory")
_WtWebioAn2GraphAlarmSyslogText_Type = OctetString
_WtWebioAn2GraphAlarmSyslogText_Object = MibTableColumn
wtWebioAn2GraphAlarmSyslogText = _WtWebioAn2GraphAlarmSyslogText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 23),
    _WtWebioAn2GraphAlarmSyslogText_Type()
)
wtWebioAn2GraphAlarmSyslogText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmSyslogText.setStatus("mandatory")
_WtWebioAn2GraphAlarmSyslogClearText_Type = OctetString
_WtWebioAn2GraphAlarmSyslogClearText_Object = MibTableColumn
wtWebioAn2GraphAlarmSyslogClearText = _WtWebioAn2GraphAlarmSyslogClearText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 24),
    _WtWebioAn2GraphAlarmSyslogClearText_Type()
)
wtWebioAn2GraphAlarmSyslogClearText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmSyslogClearText.setStatus("mandatory")
_WtWebioAn2GraphAlarmFtpDataPort_Type = OctetString
_WtWebioAn2GraphAlarmFtpDataPort_Object = MibTableColumn
wtWebioAn2GraphAlarmFtpDataPort = _WtWebioAn2GraphAlarmFtpDataPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 25),
    _WtWebioAn2GraphAlarmFtpDataPort_Type()
)
wtWebioAn2GraphAlarmFtpDataPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmFtpDataPort.setStatus("mandatory")
_WtWebioAn2GraphAlarmFtpFileName_Type = OctetString
_WtWebioAn2GraphAlarmFtpFileName_Object = MibTableColumn
wtWebioAn2GraphAlarmFtpFileName = _WtWebioAn2GraphAlarmFtpFileName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 26),
    _WtWebioAn2GraphAlarmFtpFileName_Type()
)
wtWebioAn2GraphAlarmFtpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmFtpFileName.setStatus("mandatory")
_WtWebioAn2GraphAlarmFtpText_Type = OctetString
_WtWebioAn2GraphAlarmFtpText_Object = MibTableColumn
wtWebioAn2GraphAlarmFtpText = _WtWebioAn2GraphAlarmFtpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 27),
    _WtWebioAn2GraphAlarmFtpText_Type()
)
wtWebioAn2GraphAlarmFtpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmFtpText.setStatus("mandatory")
_WtWebioAn2GraphAlarmFtpClearText_Type = OctetString
_WtWebioAn2GraphAlarmFtpClearText_Object = MibTableColumn
wtWebioAn2GraphAlarmFtpClearText = _WtWebioAn2GraphAlarmFtpClearText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 28),
    _WtWebioAn2GraphAlarmFtpClearText_Type()
)
wtWebioAn2GraphAlarmFtpClearText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmFtpClearText.setStatus("mandatory")


class _WtWebioAn2GraphAlarmFtpOption_Type(OctetString):
    """Custom type wtWebioAn2GraphAlarmFtpOption based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebioAn2GraphAlarmFtpOption_Type.__name__ = "OctetString"
_WtWebioAn2GraphAlarmFtpOption_Object = MibTableColumn
wtWebioAn2GraphAlarmFtpOption = _WtWebioAn2GraphAlarmFtpOption_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 29),
    _WtWebioAn2GraphAlarmFtpOption_Type()
)
wtWebioAn2GraphAlarmFtpOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmFtpOption.setStatus("mandatory")
_WtWebioAn2GraphAlarmTimerCron_Type = OctetString
_WtWebioAn2GraphAlarmTimerCron_Object = MibTableColumn
wtWebioAn2GraphAlarmTimerCron = _WtWebioAn2GraphAlarmTimerCron_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 30),
    _WtWebioAn2GraphAlarmTimerCron_Type()
)
wtWebioAn2GraphAlarmTimerCron.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmTimerCron.setStatus("mandatory")
_WtWebioAn2GraphAlarmName_Type = OctetString
_WtWebioAn2GraphAlarmName_Object = MibTableColumn
wtWebioAn2GraphAlarmName = _WtWebioAn2GraphAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 39),
    _WtWebioAn2GraphAlarmName_Type()
)
wtWebioAn2GraphAlarmName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmName.setStatus("mandatory")
_WtWebioAn2GraphAlarmActive_Type = OctetString
_WtWebioAn2GraphAlarmActive_Object = MibTableColumn
wtWebioAn2GraphAlarmActive = _WtWebioAn2GraphAlarmActive_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 40),
    _WtWebioAn2GraphAlarmActive_Type()
)
wtWebioAn2GraphAlarmActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmActive.setStatus("mandatory")
_WtWebioAn2GraphAlarmHttpReqAuthEnable_Type = OctetString
_WtWebioAn2GraphAlarmHttpReqAuthEnable_Object = MibTableColumn
wtWebioAn2GraphAlarmHttpReqAuthEnable = _WtWebioAn2GraphAlarmHttpReqAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 61),
    _WtWebioAn2GraphAlarmHttpReqAuthEnable_Type()
)
wtWebioAn2GraphAlarmHttpReqAuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmHttpReqAuthEnable.setStatus("mandatory")
_WtWebioAn2GraphAlarmHttpReqAuthUser_Type = OctetString
_WtWebioAn2GraphAlarmHttpReqAuthUser_Object = MibTableColumn
wtWebioAn2GraphAlarmHttpReqAuthUser = _WtWebioAn2GraphAlarmHttpReqAuthUser_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 62),
    _WtWebioAn2GraphAlarmHttpReqAuthUser_Type()
)
wtWebioAn2GraphAlarmHttpReqAuthUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmHttpReqAuthUser.setStatus("mandatory")
_WtWebioAn2GraphAlarmHttpReqAuthPassword_Type = OctetString
_WtWebioAn2GraphAlarmHttpReqAuthPassword_Object = MibTableColumn
wtWebioAn2GraphAlarmHttpReqAuthPassword = _WtWebioAn2GraphAlarmHttpReqAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 63),
    _WtWebioAn2GraphAlarmHttpReqAuthPassword_Type()
)
wtWebioAn2GraphAlarmHttpReqAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmHttpReqAuthPassword.setStatus("mandatory")
_WtWebioAn2GraphAlarmHttpReqSetUrl_Type = OctetString
_WtWebioAn2GraphAlarmHttpReqSetUrl_Object = MibTableColumn
wtWebioAn2GraphAlarmHttpReqSetUrl = _WtWebioAn2GraphAlarmHttpReqSetUrl_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 64),
    _WtWebioAn2GraphAlarmHttpReqSetUrl_Type()
)
wtWebioAn2GraphAlarmHttpReqSetUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmHttpReqSetUrl.setStatus("mandatory")
_WtWebioAn2GraphAlarmHttpReqClearUrl_Type = OctetString
_WtWebioAn2GraphAlarmHttpReqClearUrl_Object = MibTableColumn
wtWebioAn2GraphAlarmHttpReqClearUrl = _WtWebioAn2GraphAlarmHttpReqClearUrl_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 65),
    _WtWebioAn2GraphAlarmHttpReqClearUrl_Type()
)
wtWebioAn2GraphAlarmHttpReqClearUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmHttpReqClearUrl.setStatus("mandatory")


class _WtWebioAn2GraphAlarmHttpReqServerPort_Type(Integer32):
    """Custom type wtWebioAn2GraphAlarmHttpReqServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebioAn2GraphAlarmHttpReqServerPort_Type.__name__ = "Integer32"
_WtWebioAn2GraphAlarmHttpReqServerPort_Object = MibTableColumn
wtWebioAn2GraphAlarmHttpReqServerPort = _WtWebioAn2GraphAlarmHttpReqServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 66),
    _WtWebioAn2GraphAlarmHttpReqServerPort_Type()
)
wtWebioAn2GraphAlarmHttpReqServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmHttpReqServerPort.setStatus("mandatory")
_WtWebioAn2GraphAlarmMqttTopicPath_Type = OctetString
_WtWebioAn2GraphAlarmMqttTopicPath_Object = MibTableColumn
wtWebioAn2GraphAlarmMqttTopicPath = _WtWebioAn2GraphAlarmMqttTopicPath_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 67),
    _WtWebioAn2GraphAlarmMqttTopicPath_Type()
)
wtWebioAn2GraphAlarmMqttTopicPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmMqttTopicPath.setStatus("mandatory")
_WtWebioAn2GraphAlarmMqttTopicSetTopic_Type = OctetString
_WtWebioAn2GraphAlarmMqttTopicSetTopic_Object = MibTableColumn
wtWebioAn2GraphAlarmMqttTopicSetTopic = _WtWebioAn2GraphAlarmMqttTopicSetTopic_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 68),
    _WtWebioAn2GraphAlarmMqttTopicSetTopic_Type()
)
wtWebioAn2GraphAlarmMqttTopicSetTopic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmMqttTopicSetTopic.setStatus("mandatory")
_WtWebioAn2GraphAlarmMqttTopicClear_Type = OctetString
_WtWebioAn2GraphAlarmMqttTopicClear_Object = MibTableColumn
wtWebioAn2GraphAlarmMqttTopicClear = _WtWebioAn2GraphAlarmMqttTopicClear_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 69),
    _WtWebioAn2GraphAlarmMqttTopicClear_Type()
)
wtWebioAn2GraphAlarmMqttTopicClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmMqttTopicClear.setStatus("mandatory")
_WtWebioAn2GraphAlarmSensorLostSelection_Type = OctetString
_WtWebioAn2GraphAlarmSensorLostSelection_Object = MibTableColumn
wtWebioAn2GraphAlarmSensorLostSelection = _WtWebioAn2GraphAlarmSensorLostSelection_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 70),
    _WtWebioAn2GraphAlarmSensorLostSelection_Type()
)
wtWebioAn2GraphAlarmSensorLostSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmSensorLostSelection.setStatus("mandatory")
_WtWebioAn2GraphAlarmLimitWindow_Type = OctetString
_WtWebioAn2GraphAlarmLimitWindow_Object = MibTableColumn
wtWebioAn2GraphAlarmLimitWindow = _WtWebioAn2GraphAlarmLimitWindow_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 71),
    _WtWebioAn2GraphAlarmLimitWindow_Type()
)
wtWebioAn2GraphAlarmLimitWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmLimitWindow.setStatus("mandatory")
_WtWebioAn2GraphAlarmSnmpManagerPort_Type = Integer32
_WtWebioAn2GraphAlarmSnmpManagerPort_Object = MibTableColumn
wtWebioAn2GraphAlarmSnmpManagerPort = _WtWebioAn2GraphAlarmSnmpManagerPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 76),
    _WtWebioAn2GraphAlarmSnmpManagerPort_Type()
)
wtWebioAn2GraphAlarmSnmpManagerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmSnmpManagerPort.setStatus("mandatory")


class _WtWebioAn2GraphAlarmMqttQoS_Type(OctetString):
    """Custom type wtWebioAn2GraphAlarmMqttQoS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebioAn2GraphAlarmMqttQoS_Type.__name__ = "OctetString"
_WtWebioAn2GraphAlarmMqttQoS_Object = MibTableColumn
wtWebioAn2GraphAlarmMqttQoS = _WtWebioAn2GraphAlarmMqttQoS_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 77),
    _WtWebioAn2GraphAlarmMqttQoS_Type()
)
wtWebioAn2GraphAlarmMqttQoS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmMqttQoS.setStatus("mandatory")


class _WtWebioAn2GraphAlarmMqttRetain_Type(OctetString):
    """Custom type wtWebioAn2GraphAlarmMqttRetain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebioAn2GraphAlarmMqttRetain_Type.__name__ = "OctetString"
_WtWebioAn2GraphAlarmMqttRetain_Object = MibTableColumn
wtWebioAn2GraphAlarmMqttRetain = _WtWebioAn2GraphAlarmMqttRetain_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 5, 3, 1, 78),
    _WtWebioAn2GraphAlarmMqttRetain_Type()
)
wtWebioAn2GraphAlarmMqttRetain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlarmMqttRetain.setStatus("mandatory")
_WtWebioAn2GraphGraphics_ObjectIdentity = ObjectIdentity
wtWebioAn2GraphGraphics = _WtWebioAn2GraphGraphics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 6)
)
_WtWebioAn2GraphGraphicsBase_ObjectIdentity = ObjectIdentity
wtWebioAn2GraphGraphicsBase = _WtWebioAn2GraphGraphicsBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 6, 1)
)
_WtWebioAn2GraphGraphicsBaseEnable_Type = OctetString
_WtWebioAn2GraphGraphicsBaseEnable_Object = MibScalar
wtWebioAn2GraphGraphicsBaseEnable = _WtWebioAn2GraphGraphicsBaseEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 6, 1, 1),
    _WtWebioAn2GraphGraphicsBaseEnable_Type()
)
wtWebioAn2GraphGraphicsBaseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphGraphicsBaseEnable.setStatus("mandatory")
_WtWebioAn2GraphGraphicsBaseWidth_Type = Integer32
_WtWebioAn2GraphGraphicsBaseWidth_Object = MibScalar
wtWebioAn2GraphGraphicsBaseWidth = _WtWebioAn2GraphGraphicsBaseWidth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 6, 1, 2),
    _WtWebioAn2GraphGraphicsBaseWidth_Type()
)
wtWebioAn2GraphGraphicsBaseWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphGraphicsBaseWidth.setStatus("mandatory")
_WtWebioAn2GraphGraphicsBaseHeight_Type = Integer32
_WtWebioAn2GraphGraphicsBaseHeight_Object = MibScalar
wtWebioAn2GraphGraphicsBaseHeight = _WtWebioAn2GraphGraphicsBaseHeight_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 6, 1, 3),
    _WtWebioAn2GraphGraphicsBaseHeight_Type()
)
wtWebioAn2GraphGraphicsBaseHeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphGraphicsBaseHeight.setStatus("mandatory")


class _WtWebioAn2GraphGraphicsBaseFrameColor_Type(OctetString):
    """Custom type wtWebioAn2GraphGraphicsBaseFrameColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_WtWebioAn2GraphGraphicsBaseFrameColor_Type.__name__ = "OctetString"
_WtWebioAn2GraphGraphicsBaseFrameColor_Object = MibScalar
wtWebioAn2GraphGraphicsBaseFrameColor = _WtWebioAn2GraphGraphicsBaseFrameColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 6, 1, 4),
    _WtWebioAn2GraphGraphicsBaseFrameColor_Type()
)
wtWebioAn2GraphGraphicsBaseFrameColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphGraphicsBaseFrameColor.setStatus("mandatory")


class _WtWebioAn2GraphGraphicsBaseBackgroundColor_Type(OctetString):
    """Custom type wtWebioAn2GraphGraphicsBaseBackgroundColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_WtWebioAn2GraphGraphicsBaseBackgroundColor_Type.__name__ = "OctetString"
_WtWebioAn2GraphGraphicsBaseBackgroundColor_Object = MibScalar
wtWebioAn2GraphGraphicsBaseBackgroundColor = _WtWebioAn2GraphGraphicsBaseBackgroundColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 6, 1, 5),
    _WtWebioAn2GraphGraphicsBaseBackgroundColor_Type()
)
wtWebioAn2GraphGraphicsBaseBackgroundColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphGraphicsBaseBackgroundColor.setStatus("mandatory")
_WtWebioAn2GraphGraphicsBasePollingrate_Type = Integer32
_WtWebioAn2GraphGraphicsBasePollingrate_Object = MibScalar
wtWebioAn2GraphGraphicsBasePollingrate = _WtWebioAn2GraphGraphicsBasePollingrate_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 6, 1, 6),
    _WtWebioAn2GraphGraphicsBasePollingrate_Type()
)
wtWebioAn2GraphGraphicsBasePollingrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphGraphicsBasePollingrate.setStatus("mandatory")
_WtWebioAn2GraphGraphicsSelect_ObjectIdentity = ObjectIdentity
wtWebioAn2GraphGraphicsSelect = _WtWebioAn2GraphGraphicsSelect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 6, 2)
)


class _WtWebioAn2GraphGraphicsSelectDisplaySensorSel_Type(OctetString):
    """Custom type wtWebioAn2GraphGraphicsSelectDisplaySensorSel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebioAn2GraphGraphicsSelectDisplaySensorSel_Type.__name__ = "OctetString"
_WtWebioAn2GraphGraphicsSelectDisplaySensorSel_Object = MibScalar
wtWebioAn2GraphGraphicsSelectDisplaySensorSel = _WtWebioAn2GraphGraphicsSelectDisplaySensorSel_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 6, 2, 1),
    _WtWebioAn2GraphGraphicsSelectDisplaySensorSel_Type()
)
wtWebioAn2GraphGraphicsSelectDisplaySensorSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphGraphicsSelectDisplaySensorSel.setStatus("mandatory")


class _WtWebioAn2GraphGraphicsSelectDisplayShowExtrem_Type(OctetString):
    """Custom type wtWebioAn2GraphGraphicsSelectDisplayShowExtrem based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebioAn2GraphGraphicsSelectDisplayShowExtrem_Type.__name__ = "OctetString"
_WtWebioAn2GraphGraphicsSelectDisplayShowExtrem_Object = MibScalar
wtWebioAn2GraphGraphicsSelectDisplayShowExtrem = _WtWebioAn2GraphGraphicsSelectDisplayShowExtrem_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 6, 2, 2),
    _WtWebioAn2GraphGraphicsSelectDisplayShowExtrem_Type()
)
wtWebioAn2GraphGraphicsSelectDisplayShowExtrem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphGraphicsSelectDisplayShowExtrem.setStatus("mandatory")
_WtWebioAn2GraphSelectSensorColorTable_Object = MibTable
wtWebioAn2GraphSelectSensorColorTable = _WtWebioAn2GraphSelectSensorColorTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 6, 2, 3)
)
if mibBuilder.loadTexts:
    wtWebioAn2GraphSelectSensorColorTable.setStatus("mandatory")
_WtWebioAn2GraphSelectSensorColorEntry_Object = MibTableRow
wtWebioAn2GraphSelectSensorColorEntry = _WtWebioAn2GraphSelectSensorColorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 6, 2, 3, 1)
)
wtWebioAn2GraphSelectSensorColorEntry.setIndexNames(
    (0, "WebGraph-2xThermometer-US-MIB", "wtWebioAn2GraphSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn2GraphSelectSensorColorEntry.setStatus("mandatory")


class _WtWebioAn2GraphSelectGraphicsSensorColor_Type(OctetString):
    """Custom type wtWebioAn2GraphSelectGraphicsSensorColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_WtWebioAn2GraphSelectGraphicsSensorColor_Type.__name__ = "OctetString"
_WtWebioAn2GraphSelectGraphicsSensorColor_Object = MibTableColumn
wtWebioAn2GraphSelectGraphicsSensorColor = _WtWebioAn2GraphSelectGraphicsSensorColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 6, 2, 3, 1, 1),
    _WtWebioAn2GraphSelectGraphicsSensorColor_Type()
)
wtWebioAn2GraphSelectGraphicsSensorColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphSelectGraphicsSensorColor.setStatus("mandatory")
_WtWebioAn2GraphSelectGraphicsSelectScale_Type = OctetString
_WtWebioAn2GraphSelectGraphicsSelectScale_Object = MibTableColumn
wtWebioAn2GraphSelectGraphicsSelectScale = _WtWebioAn2GraphSelectGraphicsSelectScale_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 6, 2, 3, 1, 2),
    _WtWebioAn2GraphSelectGraphicsSelectScale_Type()
)
wtWebioAn2GraphSelectGraphicsSelectScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphSelectGraphicsSelectScale.setStatus("mandatory")
_WtWebioAn2GraphGraphicsScale_ObjectIdentity = ObjectIdentity
wtWebioAn2GraphGraphicsScale = _WtWebioAn2GraphGraphicsScale_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 6, 3)
)
_WtWebioAn2GraphGraphicsScaleAutoScaleEnable_Type = OctetString
_WtWebioAn2GraphGraphicsScaleAutoScaleEnable_Object = MibScalar
wtWebioAn2GraphGraphicsScaleAutoScaleEnable = _WtWebioAn2GraphGraphicsScaleAutoScaleEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 6, 3, 1),
    _WtWebioAn2GraphGraphicsScaleAutoScaleEnable_Type()
)
wtWebioAn2GraphGraphicsScaleAutoScaleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphGraphicsScaleAutoScaleEnable.setStatus("mandatory")
_WtWebioAn2GraphGraphicsScaleAutoFitEnable_Type = OctetString
_WtWebioAn2GraphGraphicsScaleAutoFitEnable_Object = MibScalar
wtWebioAn2GraphGraphicsScaleAutoFitEnable = _WtWebioAn2GraphGraphicsScaleAutoFitEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 6, 3, 2),
    _WtWebioAn2GraphGraphicsScaleAutoFitEnable_Type()
)
wtWebioAn2GraphGraphicsScaleAutoFitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphGraphicsScaleAutoFitEnable.setStatus("mandatory")
_WtWebioAn2GraphGraphicsScale1Min_Type = Integer32
_WtWebioAn2GraphGraphicsScale1Min_Object = MibScalar
wtWebioAn2GraphGraphicsScale1Min = _WtWebioAn2GraphGraphicsScale1Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 6, 3, 3),
    _WtWebioAn2GraphGraphicsScale1Min_Type()
)
wtWebioAn2GraphGraphicsScale1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn2GraphGraphicsScale1Min.setStatus("mandatory")
_WtWebioAn2GraphGraphicsScale2Min_Type = Integer32
_WtWebioAn2GraphGraphicsScale2Min_Object = MibScalar
wtWebioAn2GraphGraphicsScale2Min = _WtWebioAn2GraphGraphicsScale2Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 6, 3, 4),
    _WtWebioAn2GraphGraphicsScale2Min_Type()
)
wtWebioAn2GraphGraphicsScale2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn2GraphGraphicsScale2Min.setStatus("mandatory")
_WtWebioAn2GraphGraphicsScale3Min_Type = Integer32
_WtWebioAn2GraphGraphicsScale3Min_Object = MibScalar
wtWebioAn2GraphGraphicsScale3Min = _WtWebioAn2GraphGraphicsScale3Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 6, 3, 5),
    _WtWebioAn2GraphGraphicsScale3Min_Type()
)
wtWebioAn2GraphGraphicsScale3Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn2GraphGraphicsScale3Min.setStatus("mandatory")
_WtWebioAn2GraphGraphicsScale4Min_Type = Integer32
_WtWebioAn2GraphGraphicsScale4Min_Object = MibScalar
wtWebioAn2GraphGraphicsScale4Min = _WtWebioAn2GraphGraphicsScale4Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 6, 3, 6),
    _WtWebioAn2GraphGraphicsScale4Min_Type()
)
wtWebioAn2GraphGraphicsScale4Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn2GraphGraphicsScale4Min.setStatus("mandatory")
_WtWebioAn2GraphGraphicsScale1Max_Type = Integer32
_WtWebioAn2GraphGraphicsScale1Max_Object = MibScalar
wtWebioAn2GraphGraphicsScale1Max = _WtWebioAn2GraphGraphicsScale1Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 6, 3, 7),
    _WtWebioAn2GraphGraphicsScale1Max_Type()
)
wtWebioAn2GraphGraphicsScale1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn2GraphGraphicsScale1Max.setStatus("mandatory")
_WtWebioAn2GraphGraphicsScale2Max_Type = Integer32
_WtWebioAn2GraphGraphicsScale2Max_Object = MibScalar
wtWebioAn2GraphGraphicsScale2Max = _WtWebioAn2GraphGraphicsScale2Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 6, 3, 8),
    _WtWebioAn2GraphGraphicsScale2Max_Type()
)
wtWebioAn2GraphGraphicsScale2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn2GraphGraphicsScale2Max.setStatus("mandatory")
_WtWebioAn2GraphGraphicsScale3Max_Type = Integer32
_WtWebioAn2GraphGraphicsScale3Max_Object = MibScalar
wtWebioAn2GraphGraphicsScale3Max = _WtWebioAn2GraphGraphicsScale3Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 6, 3, 9),
    _WtWebioAn2GraphGraphicsScale3Max_Type()
)
wtWebioAn2GraphGraphicsScale3Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn2GraphGraphicsScale3Max.setStatus("mandatory")
_WtWebioAn2GraphGraphicsScale4Max_Type = Integer32
_WtWebioAn2GraphGraphicsScale4Max_Object = MibScalar
wtWebioAn2GraphGraphicsScale4Max = _WtWebioAn2GraphGraphicsScale4Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 6, 3, 10),
    _WtWebioAn2GraphGraphicsScale4Max_Type()
)
wtWebioAn2GraphGraphicsScale4Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn2GraphGraphicsScale4Max.setStatus("mandatory")
_WtWebioAn2GraphGraphicsScale1Unit_Type = OctetString
_WtWebioAn2GraphGraphicsScale1Unit_Object = MibScalar
wtWebioAn2GraphGraphicsScale1Unit = _WtWebioAn2GraphGraphicsScale1Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 6, 3, 11),
    _WtWebioAn2GraphGraphicsScale1Unit_Type()
)
wtWebioAn2GraphGraphicsScale1Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn2GraphGraphicsScale1Unit.setStatus("mandatory")
_WtWebioAn2GraphGraphicsScale2Unit_Type = OctetString
_WtWebioAn2GraphGraphicsScale2Unit_Object = MibScalar
wtWebioAn2GraphGraphicsScale2Unit = _WtWebioAn2GraphGraphicsScale2Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 6, 3, 12),
    _WtWebioAn2GraphGraphicsScale2Unit_Type()
)
wtWebioAn2GraphGraphicsScale2Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn2GraphGraphicsScale2Unit.setStatus("mandatory")
_WtWebioAn2GraphGraphicsScale3Unit_Type = OctetString
_WtWebioAn2GraphGraphicsScale3Unit_Object = MibScalar
wtWebioAn2GraphGraphicsScale3Unit = _WtWebioAn2GraphGraphicsScale3Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 6, 3, 13),
    _WtWebioAn2GraphGraphicsScale3Unit_Type()
)
wtWebioAn2GraphGraphicsScale3Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn2GraphGraphicsScale3Unit.setStatus("mandatory")
_WtWebioAn2GraphGraphicsScale4Unit_Type = OctetString
_WtWebioAn2GraphGraphicsScale4Unit_Object = MibScalar
wtWebioAn2GraphGraphicsScale4Unit = _WtWebioAn2GraphGraphicsScale4Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 1, 6, 3, 14),
    _WtWebioAn2GraphGraphicsScale4Unit_Type()
)
wtWebioAn2GraphGraphicsScale4Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn2GraphGraphicsScale4Unit.setStatus("mandatory")
_WtWebioAn2GraphPorts_ObjectIdentity = ObjectIdentity
wtWebioAn2GraphPorts = _WtWebioAn2GraphPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 2)
)
_WtWebioAn2GraphPortTable_Object = MibTable
wtWebioAn2GraphPortTable = _WtWebioAn2GraphPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 2, 1)
)
if mibBuilder.loadTexts:
    wtWebioAn2GraphPortTable.setStatus("mandatory")
_WtWebioAn2GraphPortEntry_Object = MibTableRow
wtWebioAn2GraphPortEntry = _WtWebioAn2GraphPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 2, 1, 1)
)
wtWebioAn2GraphPortEntry.setIndexNames(
    (0, "WebGraph-2xThermometer-US-MIB", "wtWebioAn2GraphSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn2GraphPortEntry.setStatus("mandatory")
_WtWebioAn2GraphPortName_Type = OctetString
_WtWebioAn2GraphPortName_Object = MibTableColumn
wtWebioAn2GraphPortName = _WtWebioAn2GraphPortName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 2, 1, 1, 1),
    _WtWebioAn2GraphPortName_Type()
)
wtWebioAn2GraphPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphPortName.setStatus("mandatory")
_WtWebioAn2GraphPortText_Type = OctetString
_WtWebioAn2GraphPortText_Object = MibTableColumn
wtWebioAn2GraphPortText = _WtWebioAn2GraphPortText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 2, 1, 1, 2),
    _WtWebioAn2GraphPortText_Type()
)
wtWebioAn2GraphPortText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphPortText.setStatus("mandatory")
_WtWebioAn2GraphPortOffset1_Type = OctetString
_WtWebioAn2GraphPortOffset1_Object = MibTableColumn
wtWebioAn2GraphPortOffset1 = _WtWebioAn2GraphPortOffset1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 2, 1, 1, 3),
    _WtWebioAn2GraphPortOffset1_Type()
)
wtWebioAn2GraphPortOffset1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphPortOffset1.setStatus("mandatory")
_WtWebioAn2GraphPortTemperature1_Type = OctetString
_WtWebioAn2GraphPortTemperature1_Object = MibTableColumn
wtWebioAn2GraphPortTemperature1 = _WtWebioAn2GraphPortTemperature1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 2, 1, 1, 4),
    _WtWebioAn2GraphPortTemperature1_Type()
)
wtWebioAn2GraphPortTemperature1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphPortTemperature1.setStatus("mandatory")
_WtWebioAn2GraphPortOffset2_Type = OctetString
_WtWebioAn2GraphPortOffset2_Object = MibTableColumn
wtWebioAn2GraphPortOffset2 = _WtWebioAn2GraphPortOffset2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 2, 1, 1, 5),
    _WtWebioAn2GraphPortOffset2_Type()
)
wtWebioAn2GraphPortOffset2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphPortOffset2.setStatus("mandatory")
_WtWebioAn2GraphPortTemperature2_Type = OctetString
_WtWebioAn2GraphPortTemperature2_Object = MibTableColumn
wtWebioAn2GraphPortTemperature2 = _WtWebioAn2GraphPortTemperature2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 2, 1, 1, 6),
    _WtWebioAn2GraphPortTemperature2_Type()
)
wtWebioAn2GraphPortTemperature2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphPortTemperature2.setStatus("mandatory")
_WtWebioAn2GraphPortComment_Type = OctetString
_WtWebioAn2GraphPortComment_Object = MibTableColumn
wtWebioAn2GraphPortComment = _WtWebioAn2GraphPortComment_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 2, 1, 1, 7),
    _WtWebioAn2GraphPortComment_Type()
)
wtWebioAn2GraphPortComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphPortComment.setStatus("mandatory")


class _WtWebioAn2GraphPortSensorSelect_Type(OctetString):
    """Custom type wtWebioAn2GraphPortSensorSelect based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebioAn2GraphPortSensorSelect_Type.__name__ = "OctetString"
_WtWebioAn2GraphPortSensorSelect_Object = MibTableColumn
wtWebioAn2GraphPortSensorSelect = _WtWebioAn2GraphPortSensorSelect_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 2, 1, 1, 8),
    _WtWebioAn2GraphPortSensorSelect_Type()
)
wtWebioAn2GraphPortSensorSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphPortSensorSelect.setStatus("mandatory")
_WtWebioAn2GraphManufact_ObjectIdentity = ObjectIdentity
wtWebioAn2GraphManufact = _WtWebioAn2GraphManufact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 3)
)
_WtWebioAn2GraphMfName_Type = OctetString
_WtWebioAn2GraphMfName_Object = MibScalar
wtWebioAn2GraphMfName = _WtWebioAn2GraphMfName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 3, 1),
    _WtWebioAn2GraphMfName_Type()
)
wtWebioAn2GraphMfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphMfName.setStatus("mandatory")
_WtWebioAn2GraphMfAddr_Type = OctetString
_WtWebioAn2GraphMfAddr_Object = MibScalar
wtWebioAn2GraphMfAddr = _WtWebioAn2GraphMfAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 3, 2),
    _WtWebioAn2GraphMfAddr_Type()
)
wtWebioAn2GraphMfAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphMfAddr.setStatus("mandatory")
_WtWebioAn2GraphMfHotline_Type = OctetString
_WtWebioAn2GraphMfHotline_Object = MibScalar
wtWebioAn2GraphMfHotline = _WtWebioAn2GraphMfHotline_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 3, 3),
    _WtWebioAn2GraphMfHotline_Type()
)
wtWebioAn2GraphMfHotline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphMfHotline.setStatus("mandatory")
_WtWebioAn2GraphMfInternet_Type = OctetString
_WtWebioAn2GraphMfInternet_Object = MibScalar
wtWebioAn2GraphMfInternet = _WtWebioAn2GraphMfInternet_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 3, 4),
    _WtWebioAn2GraphMfInternet_Type()
)
wtWebioAn2GraphMfInternet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphMfInternet.setStatus("mandatory")
_WtWebioAn2GraphMfDeviceTyp_Type = OctetString
_WtWebioAn2GraphMfDeviceTyp_Object = MibScalar
wtWebioAn2GraphMfDeviceTyp = _WtWebioAn2GraphMfDeviceTyp_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 3, 5),
    _WtWebioAn2GraphMfDeviceTyp_Type()
)
wtWebioAn2GraphMfDeviceTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphMfDeviceTyp.setStatus("mandatory")
_WtWebioAn2GraphMfOrderNo_Type = OctetString
_WtWebioAn2GraphMfOrderNo_Object = MibScalar
wtWebioAn2GraphMfOrderNo = _WtWebioAn2GraphMfOrderNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 3, 3, 6),
    _WtWebioAn2GraphMfOrderNo_Type()
)
wtWebioAn2GraphMfOrderNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphMfOrderNo.setStatus("mandatory")
_WtWebioAn2GraphDiag_ObjectIdentity = ObjectIdentity
wtWebioAn2GraphDiag = _WtWebioAn2GraphDiag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 4)
)
_WtWebioAn2GraphDiagErrorCount_Type = Integer32
_WtWebioAn2GraphDiagErrorCount_Object = MibScalar
wtWebioAn2GraphDiagErrorCount = _WtWebioAn2GraphDiagErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 4, 1),
    _WtWebioAn2GraphDiagErrorCount_Type()
)
wtWebioAn2GraphDiagErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn2GraphDiagErrorCount.setStatus("mandatory")
_WtWebioAn2GraphDiagBinaryError_Type = OctetString
_WtWebioAn2GraphDiagBinaryError_Object = MibScalar
wtWebioAn2GraphDiagBinaryError = _WtWebioAn2GraphDiagBinaryError_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 4, 2),
    _WtWebioAn2GraphDiagBinaryError_Type()
)
wtWebioAn2GraphDiagBinaryError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn2GraphDiagBinaryError.setStatus("mandatory")
_WtWebioAn2GraphDiagErrorIndex_Type = Integer32
_WtWebioAn2GraphDiagErrorIndex_Object = MibScalar
wtWebioAn2GraphDiagErrorIndex = _WtWebioAn2GraphDiagErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 4, 3),
    _WtWebioAn2GraphDiagErrorIndex_Type()
)
wtWebioAn2GraphDiagErrorIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn2GraphDiagErrorIndex.setStatus("mandatory")
_WtWebioAn2GraphDiagErrorMessage_Type = OctetString
_WtWebioAn2GraphDiagErrorMessage_Object = MibScalar
wtWebioAn2GraphDiagErrorMessage = _WtWebioAn2GraphDiagErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 4, 4),
    _WtWebioAn2GraphDiagErrorMessage_Type()
)
wtWebioAn2GraphDiagErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn2GraphDiagErrorMessage.setStatus("mandatory")
_WtWebioAn2GraphDiagErrorClear_Type = Integer32
_WtWebioAn2GraphDiagErrorClear_Object = MibScalar
wtWebioAn2GraphDiagErrorClear = _WtWebioAn2GraphDiagErrorClear_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 4, 5),
    _WtWebioAn2GraphDiagErrorClear_Type()
)
wtWebioAn2GraphDiagErrorClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    wtWebioAn2GraphDiagErrorClear.setStatus("mandatory")

# Managed Objects groups


# Notification objects

wtWebioAn2GraphAlert1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 0, 21)
)
wtWebioAn2GraphAlert1.setObjects(
    ("WebGraph-2xThermometer-US-MIB", "wtWebioAn2GraphAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlert1.setStatus(
        ""
    )

wtWebioAn2GraphAlert2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 0, 22)
)
wtWebioAn2GraphAlert2.setObjects(
    ("WebGraph-2xThermometer-US-MIB", "wtWebioAn2GraphAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlert2.setStatus(
        ""
    )

wtWebioAn2GraphAlert3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 0, 23)
)
wtWebioAn2GraphAlert3.setObjects(
    ("WebGraph-2xThermometer-US-MIB", "wtWebioAn2GraphAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlert3.setStatus(
        ""
    )

wtWebioAn2GraphAlert4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 0, 24)
)
wtWebioAn2GraphAlert4.setObjects(
    ("WebGraph-2xThermometer-US-MIB", "wtWebioAn2GraphAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlert4.setStatus(
        ""
    )

wtWebioAn2GraphAlert5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 0, 25)
)
wtWebioAn2GraphAlert5.setObjects(
    ("WebGraph-2xThermometer-US-MIB", "wtWebioAn2GraphAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlert5.setStatus(
        ""
    )

wtWebioAn2GraphAlert6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 0, 26)
)
wtWebioAn2GraphAlert6.setObjects(
    ("WebGraph-2xThermometer-US-MIB", "wtWebioAn2GraphAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlert6.setStatus(
        ""
    )

wtWebioAn2GraphAlert7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 0, 27)
)
wtWebioAn2GraphAlert7.setObjects(
    ("WebGraph-2xThermometer-US-MIB", "wtWebioAn2GraphAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlert7.setStatus(
        ""
    )

wtWebioAn2GraphAlert8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 0, 28)
)
wtWebioAn2GraphAlert8.setObjects(
    ("WebGraph-2xThermometer-US-MIB", "wtWebioAn2GraphAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlert8.setStatus(
        ""
    )

wtWebioAn2GraphAlert9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 0, 81)
)
wtWebioAn2GraphAlert9.setObjects(
    ("WebGraph-2xThermometer-US-MIB", "wtWebioAn2GraphAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlert9.setStatus(
        ""
    )

wtWebioAn2GraphAlert10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 0, 82)
)
wtWebioAn2GraphAlert10.setObjects(
    ("WebGraph-2xThermometer-US-MIB", "wtWebioAn2GraphAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlert10.setStatus(
        ""
    )

wtWebioAn2GraphAlert11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 0, 83)
)
wtWebioAn2GraphAlert11.setObjects(
    ("WebGraph-2xThermometer-US-MIB", "wtWebioAn2GraphAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlert11.setStatus(
        ""
    )

wtWebioAn2GraphAlert12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 0, 84)
)
wtWebioAn2GraphAlert12.setObjects(
    ("WebGraph-2xThermometer-US-MIB", "wtWebioAn2GraphAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlert12.setStatus(
        ""
    )

wtWebioAn2GraphAlert13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 0, 85)
)
wtWebioAn2GraphAlert13.setObjects(
    ("WebGraph-2xThermometer-US-MIB", "wtWebioAn2GraphAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlert13.setStatus(
        ""
    )

wtWebioAn2GraphAlert14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 0, 86)
)
wtWebioAn2GraphAlert14.setObjects(
    ("WebGraph-2xThermometer-US-MIB", "wtWebioAn2GraphAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlert14.setStatus(
        ""
    )

wtWebioAn2GraphAlert15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 0, 87)
)
wtWebioAn2GraphAlert15.setObjects(
    ("WebGraph-2xThermometer-US-MIB", "wtWebioAn2GraphAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlert15.setStatus(
        ""
    )

wtWebioAn2GraphAlert16 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 0, 88)
)
wtWebioAn2GraphAlert16.setObjects(
    ("WebGraph-2xThermometer-US-MIB", "wtWebioAn2GraphAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlert16.setStatus(
        ""
    )

wtWebioAn2GraphAlertDiag = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 43, 0, 110)
)
wtWebioAn2GraphAlertDiag.setObjects(
      *(("WebGraph-2xThermometer-US-MIB", "wtWebioAn2GraphDiagErrorIndex"),
        ("WebGraph-2xThermometer-US-MIB", "wtWebioAn2GraphDiagErrorMessage"))
)
if mibBuilder.loadTexts:
    wtWebioAn2GraphAlertDiag.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WebGraph-2xThermometer-US-MIB",
    **{"wut": wut,
       "wtComServer": wtComServer,
       "wtWebio": wtWebio,
       "wtWebioAn2Graph": wtWebioAn2Graph,
       "wtWebioAn2GraphAlert1": wtWebioAn2GraphAlert1,
       "wtWebioAn2GraphAlert2": wtWebioAn2GraphAlert2,
       "wtWebioAn2GraphAlert3": wtWebioAn2GraphAlert3,
       "wtWebioAn2GraphAlert4": wtWebioAn2GraphAlert4,
       "wtWebioAn2GraphAlert5": wtWebioAn2GraphAlert5,
       "wtWebioAn2GraphAlert6": wtWebioAn2GraphAlert6,
       "wtWebioAn2GraphAlert7": wtWebioAn2GraphAlert7,
       "wtWebioAn2GraphAlert8": wtWebioAn2GraphAlert8,
       "wtWebioAn2GraphAlert9": wtWebioAn2GraphAlert9,
       "wtWebioAn2GraphAlert10": wtWebioAn2GraphAlert10,
       "wtWebioAn2GraphAlert11": wtWebioAn2GraphAlert11,
       "wtWebioAn2GraphAlert12": wtWebioAn2GraphAlert12,
       "wtWebioAn2GraphAlert13": wtWebioAn2GraphAlert13,
       "wtWebioAn2GraphAlert14": wtWebioAn2GraphAlert14,
       "wtWebioAn2GraphAlert15": wtWebioAn2GraphAlert15,
       "wtWebioAn2GraphAlert16": wtWebioAn2GraphAlert16,
       "wtWebioAn2GraphAlertDiag": wtWebioAn2GraphAlertDiag,
       "wtWebioAn2GraphTemp": wtWebioAn2GraphTemp,
       "wtWebioAn2GraphSensors": wtWebioAn2GraphSensors,
       "wtWebioAn2GraphSensorTable": wtWebioAn2GraphSensorTable,
       "wtWebioAn2GraphSensorEntry": wtWebioAn2GraphSensorEntry,
       "wtWebioAn2GraphSensorNo": wtWebioAn2GraphSensorNo,
       "wtWebioAn2GraphTempValueTable": wtWebioAn2GraphTempValueTable,
       "wtWebioAn2GraphTempValueEntry": wtWebioAn2GraphTempValueEntry,
       "wtWebioAn2GraphTempValue": wtWebioAn2GraphTempValue,
       "wtWebioAn2GraphBinaryTempValueTable": wtWebioAn2GraphBinaryTempValueTable,
       "wtWebioAn2GraphBinaryTempValueEntry": wtWebioAn2GraphBinaryTempValueEntry,
       "wtWebioAn2GraphBinaryTempValue": wtWebioAn2GraphBinaryTempValue,
       "wtWebioAn2GraphTempValuePktTable": wtWebioAn2GraphTempValuePktTable,
       "wtWebioAn2GraphTempValuePktEntry": wtWebioAn2GraphTempValuePktEntry,
       "wtWebioAn2GraphTempValuePkt": wtWebioAn2GraphTempValuePkt,
       "wtWebioAn2GraphSessCntrl": wtWebioAn2GraphSessCntrl,
       "wtWebioAn2GraphSessCntrlPassword": wtWebioAn2GraphSessCntrlPassword,
       "wtWebioAn2GraphSessCntrlConfigMode": wtWebioAn2GraphSessCntrlConfigMode,
       "wtWebioAn2GraphSessCntrlLogout": wtWebioAn2GraphSessCntrlLogout,
       "wtWebioAn2GraphSessCntrlAdminPassword": wtWebioAn2GraphSessCntrlAdminPassword,
       "wtWebioAn2GraphSessCntrlConfigPassword": wtWebioAn2GraphSessCntrlConfigPassword,
       "wtWebioAn2GraphConfig": wtWebioAn2GraphConfig,
       "wtWebioAn2GraphDevice": wtWebioAn2GraphDevice,
       "wtWebioAn2GraphText": wtWebioAn2GraphText,
       "wtWebioAn2GraphDeviceName": wtWebioAn2GraphDeviceName,
       "wtWebioAn2GraphDeviceText": wtWebioAn2GraphDeviceText,
       "wtWebioAn2GraphDeviceLocation": wtWebioAn2GraphDeviceLocation,
       "wtWebioAn2GraphDeviceContact": wtWebioAn2GraphDeviceContact,
       "wtWebioAn2GraphTimeDate": wtWebioAn2GraphTimeDate,
       "wtWebioAn2GraphTimeZone": wtWebioAn2GraphTimeZone,
       "wtWebioAn2GraphTzOffsetHrs": wtWebioAn2GraphTzOffsetHrs,
       "wtWebioAn2GraphTzOffsetMin": wtWebioAn2GraphTzOffsetMin,
       "wtWebioAn2GraphTzEnable": wtWebioAn2GraphTzEnable,
       "wtWebioAn2GraphStTzOffsetHrs": wtWebioAn2GraphStTzOffsetHrs,
       "wtWebioAn2GraphStTzOffsetMin": wtWebioAn2GraphStTzOffsetMin,
       "wtWebioAn2GraphStTzEnable": wtWebioAn2GraphStTzEnable,
       "wtWebioAn2GraphStTzStartMonth": wtWebioAn2GraphStTzStartMonth,
       "wtWebioAn2GraphStTzStartMode": wtWebioAn2GraphStTzStartMode,
       "wtWebioAn2GraphStTzStartWday": wtWebioAn2GraphStTzStartWday,
       "wtWebioAn2GraphStTzStartHrs": wtWebioAn2GraphStTzStartHrs,
       "wtWebioAn2GraphStTzStartMin": wtWebioAn2GraphStTzStartMin,
       "wtWebioAn2GraphStTzStopMonth": wtWebioAn2GraphStTzStopMonth,
       "wtWebioAn2GraphStTzStopMode": wtWebioAn2GraphStTzStopMode,
       "wtWebioAn2GraphStTzStopWday": wtWebioAn2GraphStTzStopWday,
       "wtWebioAn2GraphStTzStopHrs": wtWebioAn2GraphStTzStopHrs,
       "wtWebioAn2GraphStTzStopMin": wtWebioAn2GraphStTzStopMin,
       "wtWebioAn2GraphTimeServer": wtWebioAn2GraphTimeServer,
       "wtWebioAn2GraphTimeServer1": wtWebioAn2GraphTimeServer1,
       "wtWebioAn2GraphTimeServer2": wtWebioAn2GraphTimeServer2,
       "wtWebioAn2GraphTsEnable": wtWebioAn2GraphTsEnable,
       "wtWebioAn2GraphTsSyncTime": wtWebioAn2GraphTsSyncTime,
       "wtWebioAn2GraphDeviceClock": wtWebioAn2GraphDeviceClock,
       "wtWebioAn2GraphClockHrs": wtWebioAn2GraphClockHrs,
       "wtWebioAn2GraphClockMin": wtWebioAn2GraphClockMin,
       "wtWebioAn2GraphClockDay": wtWebioAn2GraphClockDay,
       "wtWebioAn2GraphClockMonth": wtWebioAn2GraphClockMonth,
       "wtWebioAn2GraphClockYear": wtWebioAn2GraphClockYear,
       "wtWebioAn2GraphBasic": wtWebioAn2GraphBasic,
       "wtWebioAn2GraphNetwork": wtWebioAn2GraphNetwork,
       "wtWebioAn2GraphIpAddress": wtWebioAn2GraphIpAddress,
       "wtWebioAn2GraphSubnetMask": wtWebioAn2GraphSubnetMask,
       "wtWebioAn2GraphGateway": wtWebioAn2GraphGateway,
       "wtWebioAn2GraphDnsServer1": wtWebioAn2GraphDnsServer1,
       "wtWebioAn2GraphDnsServer2": wtWebioAn2GraphDnsServer2,
       "wtWebioAn2GraphAddConfig": wtWebioAn2GraphAddConfig,
       "wtWebioAn2GraphHTTP": wtWebioAn2GraphHTTP,
       "wtWebioAn2GraphStartup": wtWebioAn2GraphStartup,
       "wtWebioAn2GraphGetHeaderEnable": wtWebioAn2GraphGetHeaderEnable,
       "wtWebioAn2GraphHttpPort": wtWebioAn2GraphHttpPort,
       "wtWebioAn2GraphMail": wtWebioAn2GraphMail,
       "wtWebioAn2GraphMailAdName": wtWebioAn2GraphMailAdName,
       "wtWebioAn2GraphMailReply": wtWebioAn2GraphMailReply,
       "wtWebioAn2GraphMailServer": wtWebioAn2GraphMailServer,
       "wtWebioAn1MailEnable": wtWebioAn1MailEnable,
       "wtWebioAn2GraphMailAuthentication": wtWebioAn2GraphMailAuthentication,
       "wtWebioAn2GraphMailAuthUser": wtWebioAn2GraphMailAuthUser,
       "wtWebioAn2GraphMailAuthPassword": wtWebioAn2GraphMailAuthPassword,
       "wtWebioAn2GraphMailPop3Server": wtWebioAn2GraphMailPop3Server,
       "wtWebioAn2GraphSNMP": wtWebioAn2GraphSNMP,
       "wtWebioAn2GraphSnmpCommunityStringRead": wtWebioAn2GraphSnmpCommunityStringRead,
       "wtWebioAn2GraphSnmpCommunityStringReadWrite": wtWebioAn2GraphSnmpCommunityStringReadWrite,
       "wtWebioAn2GraphSystemTrapManagerIP": wtWebioAn2GraphSystemTrapManagerIP,
       "wtWebioAn2GraphSystemTrapEnable": wtWebioAn2GraphSystemTrapEnable,
       "wtWebioAn2GraphSnmpEnable": wtWebioAn2GraphSnmpEnable,
       "wtWebioAn2GraphSnmpCommunityStringTrap": wtWebioAn2GraphSnmpCommunityStringTrap,
       "wtWebioAn2GraphSnmpSystemTrapManagerPort": wtWebioAn2GraphSnmpSystemTrapManagerPort,
       "wtWebioAn2GraphUDP": wtWebioAn2GraphUDP,
       "wtWebioAn2GraphUdpPort": wtWebioAn2GraphUdpPort,
       "wtWebioAn2GraphUdpEnable": wtWebioAn2GraphUdpEnable,
       "wtWebioAn2GraphSyslog": wtWebioAn2GraphSyslog,
       "wtWebioAn2GraphSyslogServerIP": wtWebioAn2GraphSyslogServerIP,
       "wtWebioAn2GraphSyslogServerPort": wtWebioAn2GraphSyslogServerPort,
       "wtWebioAn2GraphSyslogSystemMessagesEnable": wtWebioAn2GraphSyslogSystemMessagesEnable,
       "wtWebioAn2GraphSyslogEnable": wtWebioAn2GraphSyslogEnable,
       "wtWebioAn2GraphFTP": wtWebioAn2GraphFTP,
       "wtWebioAn2GraphFTPServerIP": wtWebioAn2GraphFTPServerIP,
       "wtWebioAn2GraphFTPServerControlPort": wtWebioAn2GraphFTPServerControlPort,
       "wtWebioAn2GraphFTPUserName": wtWebioAn2GraphFTPUserName,
       "wtWebioAn2GraphFTPPassword": wtWebioAn2GraphFTPPassword,
       "wtWebioAn2GraphFTPAccount": wtWebioAn2GraphFTPAccount,
       "wtWebioAn2GraphFTPOption": wtWebioAn2GraphFTPOption,
       "wtWebioAn2GraphFTPEnable": wtWebioAn2GraphFTPEnable,
       "wtWebioAn2GraphLanguage": wtWebioAn2GraphLanguage,
       "wtWebioAn2GraphLanguageSelect": wtWebioAn2GraphLanguageSelect,
       "wtWebioAn2GraphMQTT": wtWebioAn2GraphMQTT,
       "wtWebioAn2GraphMQTTEnable": wtWebioAn2GraphMQTTEnable,
       "wtWebioAn2GraphMQTTBrockerIP": wtWebioAn2GraphMQTTBrockerIP,
       "wtWebioAn2GraphMQTTUserName": wtWebioAn2GraphMQTTUserName,
       "wtWebioAn2GraphMQTTPassword": wtWebioAn2GraphMQTTPassword,
       "wtWebioAn2GraphMQTTLocalPort": wtWebioAn2GraphMQTTLocalPort,
       "wtWebioAn2GraphMQTTBrokerServerPort": wtWebioAn2GraphMQTTBrokerServerPort,
       "wtWebioAn2GraphMQTTInterval": wtWebioAn2GraphMQTTInterval,
       "wtWebioAn2GraphMQTTLastWillEnable": wtWebioAn2GraphMQTTLastWillEnable,
       "wtWebioAn2GraphMQTTLastWillTopic": wtWebioAn2GraphMQTTLastWillTopic,
       "wtWebioAn2GraphMQTTLastWillMsg": wtWebioAn2GraphMQTTLastWillMsg,
       "wtWebioAn2GraphMQTTLastWillQoS": wtWebioAn2GraphMQTTLastWillQoS,
       "wtWebioAn2GraphMQTTLastWillRetain": wtWebioAn2GraphMQTTLastWillRetain,
       "wtWebioAn2GraphMQTTLastWillConnectEnable": wtWebioAn2GraphMQTTLastWillConnectEnable,
       "wtWebioAn2GraphMQTTLastWillConnectMsg": wtWebioAn2GraphMQTTLastWillConnectMsg,
       "wtWebioAn2GraphREST": wtWebioAn2GraphREST,
       "wtWebioAn2GraphRESTEnable": wtWebioAn2GraphRESTEnable,
       "wtWebioAn2GraphRESTDigestAuthEnable": wtWebioAn2GraphRESTDigestAuthEnable,
       "wtWebioAn2GraphDatalogger": wtWebioAn2GraphDatalogger,
       "wtWebioAn2GraphLoggerTimebase": wtWebioAn2GraphLoggerTimebase,
       "wtWebioAn2GraphLoggerSensorSel": wtWebioAn2GraphLoggerSensorSel,
       "wtWebioAn2GraphDisplaySensorSel": wtWebioAn2GraphDisplaySensorSel,
       "wtWebioAn2GraphSensorColorTable": wtWebioAn2GraphSensorColorTable,
       "wtWebioAn2GraphSensorColorEntry": wtWebioAn2GraphSensorColorEntry,
       "wtWebioAn2GraphSensorColor": wtWebioAn2GraphSensorColor,
       "wtWebioAn2GraphAutoScaleEnable": wtWebioAn2GraphAutoScaleEnable,
       "wtWebioAn2GraphVerticalUpperLimit": wtWebioAn2GraphVerticalUpperLimit,
       "wtWebioAn2GraphVerticalLowerLimit": wtWebioAn2GraphVerticalLowerLimit,
       "wtWebioAn2GraphHorizontalZoom": wtWebioAn2GraphHorizontalZoom,
       "wtWebioAn2GraphAlarm": wtWebioAn2GraphAlarm,
       "wtWebioAn2GraphAlarmCount": wtWebioAn2GraphAlarmCount,
       "wtWebioAn2GraphAlarmIfTable": wtWebioAn2GraphAlarmIfTable,
       "wtWebioAn2GraphAlarmIfEntry": wtWebioAn2GraphAlarmIfEntry,
       "wtWebioAn2GraphAlarmNo": wtWebioAn2GraphAlarmNo,
       "wtWebioAn2GraphAlarmTable": wtWebioAn2GraphAlarmTable,
       "wtWebioAn2GraphAlarmEntry": wtWebioAn2GraphAlarmEntry,
       "wtWebioAn2GraphAlarmTrigger": wtWebioAn2GraphAlarmTrigger,
       "wtWebioAn2GraphAlarmMin": wtWebioAn2GraphAlarmMin,
       "wtWebioAn2GraphAlarmMax": wtWebioAn2GraphAlarmMax,
       "wtWebioAn2GraphAlarmHysteresis": wtWebioAn2GraphAlarmHysteresis,
       "wtWebioAn2GraphAlarmDelay": wtWebioAn2GraphAlarmDelay,
       "wtWebioAn2GraphAlarmInterval": wtWebioAn2GraphAlarmInterval,
       "wtWebioAn2GraphAlarmEnable": wtWebioAn2GraphAlarmEnable,
       "wtWebioAn2GraphAlarmEMailAddr": wtWebioAn2GraphAlarmEMailAddr,
       "wtWebioAn2GraphAlarmMailSubject": wtWebioAn2GraphAlarmMailSubject,
       "wtWebioAn2GraphAlarmMailText": wtWebioAn2GraphAlarmMailText,
       "wtWebioAn2GraphAlarmManagerIP": wtWebioAn2GraphAlarmManagerIP,
       "wtWebioAn2GraphAlarmTrapText": wtWebioAn2GraphAlarmTrapText,
       "wtWebioAn2GraphAlarmMailOptions": wtWebioAn2GraphAlarmMailOptions,
       "wtWebioAn2GraphAlarmTcpIpAddr": wtWebioAn2GraphAlarmTcpIpAddr,
       "wtWebioAn2GraphAlarmTcpPort": wtWebioAn2GraphAlarmTcpPort,
       "wtWebioAn2GraphAlarmTcpText": wtWebioAn2GraphAlarmTcpText,
       "wtWebioAn2GraphAlarmClearMailSubject": wtWebioAn2GraphAlarmClearMailSubject,
       "wtWebioAn2GraphAlarmClearMailText": wtWebioAn2GraphAlarmClearMailText,
       "wtWebioAn2GraphAlarmClearTrapText": wtWebioAn2GraphAlarmClearTrapText,
       "wtWebioAn2GraphAlarmClearTcpText": wtWebioAn2GraphAlarmClearTcpText,
       "wtWebioAn2GraphAlarmSyslogIpAddr": wtWebioAn2GraphAlarmSyslogIpAddr,
       "wtWebioAn2GraphAlarmSyslogPort": wtWebioAn2GraphAlarmSyslogPort,
       "wtWebioAn2GraphAlarmSyslogText": wtWebioAn2GraphAlarmSyslogText,
       "wtWebioAn2GraphAlarmSyslogClearText": wtWebioAn2GraphAlarmSyslogClearText,
       "wtWebioAn2GraphAlarmFtpDataPort": wtWebioAn2GraphAlarmFtpDataPort,
       "wtWebioAn2GraphAlarmFtpFileName": wtWebioAn2GraphAlarmFtpFileName,
       "wtWebioAn2GraphAlarmFtpText": wtWebioAn2GraphAlarmFtpText,
       "wtWebioAn2GraphAlarmFtpClearText": wtWebioAn2GraphAlarmFtpClearText,
       "wtWebioAn2GraphAlarmFtpOption": wtWebioAn2GraphAlarmFtpOption,
       "wtWebioAn2GraphAlarmTimerCron": wtWebioAn2GraphAlarmTimerCron,
       "wtWebioAn2GraphAlarmName": wtWebioAn2GraphAlarmName,
       "wtWebioAn2GraphAlarmActive": wtWebioAn2GraphAlarmActive,
       "wtWebioAn2GraphAlarmHttpReqAuthEnable": wtWebioAn2GraphAlarmHttpReqAuthEnable,
       "wtWebioAn2GraphAlarmHttpReqAuthUser": wtWebioAn2GraphAlarmHttpReqAuthUser,
       "wtWebioAn2GraphAlarmHttpReqAuthPassword": wtWebioAn2GraphAlarmHttpReqAuthPassword,
       "wtWebioAn2GraphAlarmHttpReqSetUrl": wtWebioAn2GraphAlarmHttpReqSetUrl,
       "wtWebioAn2GraphAlarmHttpReqClearUrl": wtWebioAn2GraphAlarmHttpReqClearUrl,
       "wtWebioAn2GraphAlarmHttpReqServerPort": wtWebioAn2GraphAlarmHttpReqServerPort,
       "wtWebioAn2GraphAlarmMqttTopicPath": wtWebioAn2GraphAlarmMqttTopicPath,
       "wtWebioAn2GraphAlarmMqttTopicSetTopic": wtWebioAn2GraphAlarmMqttTopicSetTopic,
       "wtWebioAn2GraphAlarmMqttTopicClear": wtWebioAn2GraphAlarmMqttTopicClear,
       "wtWebioAn2GraphAlarmSensorLostSelection": wtWebioAn2GraphAlarmSensorLostSelection,
       "wtWebioAn2GraphAlarmLimitWindow": wtWebioAn2GraphAlarmLimitWindow,
       "wtWebioAn2GraphAlarmSnmpManagerPort": wtWebioAn2GraphAlarmSnmpManagerPort,
       "wtWebioAn2GraphAlarmMqttQoS": wtWebioAn2GraphAlarmMqttQoS,
       "wtWebioAn2GraphAlarmMqttRetain": wtWebioAn2GraphAlarmMqttRetain,
       "wtWebioAn2GraphGraphics": wtWebioAn2GraphGraphics,
       "wtWebioAn2GraphGraphicsBase": wtWebioAn2GraphGraphicsBase,
       "wtWebioAn2GraphGraphicsBaseEnable": wtWebioAn2GraphGraphicsBaseEnable,
       "wtWebioAn2GraphGraphicsBaseWidth": wtWebioAn2GraphGraphicsBaseWidth,
       "wtWebioAn2GraphGraphicsBaseHeight": wtWebioAn2GraphGraphicsBaseHeight,
       "wtWebioAn2GraphGraphicsBaseFrameColor": wtWebioAn2GraphGraphicsBaseFrameColor,
       "wtWebioAn2GraphGraphicsBaseBackgroundColor": wtWebioAn2GraphGraphicsBaseBackgroundColor,
       "wtWebioAn2GraphGraphicsBasePollingrate": wtWebioAn2GraphGraphicsBasePollingrate,
       "wtWebioAn2GraphGraphicsSelect": wtWebioAn2GraphGraphicsSelect,
       "wtWebioAn2GraphGraphicsSelectDisplaySensorSel": wtWebioAn2GraphGraphicsSelectDisplaySensorSel,
       "wtWebioAn2GraphGraphicsSelectDisplayShowExtrem": wtWebioAn2GraphGraphicsSelectDisplayShowExtrem,
       "wtWebioAn2GraphSelectSensorColorTable": wtWebioAn2GraphSelectSensorColorTable,
       "wtWebioAn2GraphSelectSensorColorEntry": wtWebioAn2GraphSelectSensorColorEntry,
       "wtWebioAn2GraphSelectGraphicsSensorColor": wtWebioAn2GraphSelectGraphicsSensorColor,
       "wtWebioAn2GraphSelectGraphicsSelectScale": wtWebioAn2GraphSelectGraphicsSelectScale,
       "wtWebioAn2GraphGraphicsScale": wtWebioAn2GraphGraphicsScale,
       "wtWebioAn2GraphGraphicsScaleAutoScaleEnable": wtWebioAn2GraphGraphicsScaleAutoScaleEnable,
       "wtWebioAn2GraphGraphicsScaleAutoFitEnable": wtWebioAn2GraphGraphicsScaleAutoFitEnable,
       "wtWebioAn2GraphGraphicsScale1Min": wtWebioAn2GraphGraphicsScale1Min,
       "wtWebioAn2GraphGraphicsScale2Min": wtWebioAn2GraphGraphicsScale2Min,
       "wtWebioAn2GraphGraphicsScale3Min": wtWebioAn2GraphGraphicsScale3Min,
       "wtWebioAn2GraphGraphicsScale4Min": wtWebioAn2GraphGraphicsScale4Min,
       "wtWebioAn2GraphGraphicsScale1Max": wtWebioAn2GraphGraphicsScale1Max,
       "wtWebioAn2GraphGraphicsScale2Max": wtWebioAn2GraphGraphicsScale2Max,
       "wtWebioAn2GraphGraphicsScale3Max": wtWebioAn2GraphGraphicsScale3Max,
       "wtWebioAn2GraphGraphicsScale4Max": wtWebioAn2GraphGraphicsScale4Max,
       "wtWebioAn2GraphGraphicsScale1Unit": wtWebioAn2GraphGraphicsScale1Unit,
       "wtWebioAn2GraphGraphicsScale2Unit": wtWebioAn2GraphGraphicsScale2Unit,
       "wtWebioAn2GraphGraphicsScale3Unit": wtWebioAn2GraphGraphicsScale3Unit,
       "wtWebioAn2GraphGraphicsScale4Unit": wtWebioAn2GraphGraphicsScale4Unit,
       "wtWebioAn2GraphPorts": wtWebioAn2GraphPorts,
       "wtWebioAn2GraphPortTable": wtWebioAn2GraphPortTable,
       "wtWebioAn2GraphPortEntry": wtWebioAn2GraphPortEntry,
       "wtWebioAn2GraphPortName": wtWebioAn2GraphPortName,
       "wtWebioAn2GraphPortText": wtWebioAn2GraphPortText,
       "wtWebioAn2GraphPortOffset1": wtWebioAn2GraphPortOffset1,
       "wtWebioAn2GraphPortTemperature1": wtWebioAn2GraphPortTemperature1,
       "wtWebioAn2GraphPortOffset2": wtWebioAn2GraphPortOffset2,
       "wtWebioAn2GraphPortTemperature2": wtWebioAn2GraphPortTemperature2,
       "wtWebioAn2GraphPortComment": wtWebioAn2GraphPortComment,
       "wtWebioAn2GraphPortSensorSelect": wtWebioAn2GraphPortSensorSelect,
       "wtWebioAn2GraphManufact": wtWebioAn2GraphManufact,
       "wtWebioAn2GraphMfName": wtWebioAn2GraphMfName,
       "wtWebioAn2GraphMfAddr": wtWebioAn2GraphMfAddr,
       "wtWebioAn2GraphMfHotline": wtWebioAn2GraphMfHotline,
       "wtWebioAn2GraphMfInternet": wtWebioAn2GraphMfInternet,
       "wtWebioAn2GraphMfDeviceTyp": wtWebioAn2GraphMfDeviceTyp,
       "wtWebioAn2GraphMfOrderNo": wtWebioAn2GraphMfOrderNo,
       "wtWebioAn2GraphDiag": wtWebioAn2GraphDiag,
       "wtWebioAn2GraphDiagErrorCount": wtWebioAn2GraphDiagErrorCount,
       "wtWebioAn2GraphDiagBinaryError": wtWebioAn2GraphDiagBinaryError,
       "wtWebioAn2GraphDiagErrorIndex": wtWebioAn2GraphDiagErrorIndex,
       "wtWebioAn2GraphDiagErrorMessage": wtWebioAn2GraphDiagErrorMessage,
       "wtWebioAn2GraphDiagErrorClear": wtWebioAn2GraphDiagErrorClear}
)
