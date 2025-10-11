# SNMP MIB module (HAWK-I2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/panduit/HAWK-I2-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:32:16 2025
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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hawki2MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24)
)
if mibBuilder.loadTexts:
    hawki2MIB.setRevisions(
        ("2020-06-03 12:00",
         "2019-02-08 12:00",
         "2017-10-18 12:00",
         "2017-02-09 12:00",
         "2017-01-31 12:00",
         "2017-01-17 12:00",
         "2016-12-06 12:00",
         "2016-08-25 12:00",
         "2016-05-19 12:00",
         "2016-05-18 12:00",
         "2015-06-30 12:00",
         "2015-06-18 12:00",
         "2015-04-08 12:00",
         "2014-06-18 00:00",
         "2014-04-01 12:00",
         "2010-07-15 12:00",
         "2009-05-01 12:00",
         "2008-06-18 12:00",
         "2008-02-27 12:00",
         "2007-09-07 12:00",
         "2007-09-06 12:00",
         "2007-07-20 12:00",
         "2007-05-11 12:00")
    )


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



class InetAddressType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              16)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ipv4", 1),
          ("ipv6", 2),
          ("ipv4z", 3),
          ("ipv6z", 4),
          ("dns", 16))
    )



class InetAddress(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class IpStackConfiguration(TextualConvention, Integer32):
    status = "current"
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
        *(("unknown", 0),
          ("ipv4Only", 1),
          ("ipv6Only", 2),
          ("ipv4AndIpv6", 3))
    )



class ContactState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("closed", 2))
    )



class InputContactState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("closed", 2),
          ("armed", 3),
          ("triggered", 4),
          ("unknown", 255))
    )



class RelayState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )



class OutputControlState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("deactivate", 2),
          ("logic", 3))
    )



class EnableState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )



class InputDataType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("autodetect", 1),
          ("temperature", 2),
          ("humidity", 3),
          ("analogue", 4),
          ("contact", 5),
          ("inactive", 255))
    )



class KeypadEnableState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("matrix2x5", 1),
          ("matrix3x4", 2),
          ("inactive", 255))
    )



class ExternalUnitType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              253,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("acu", 1),
          ("keypad", 2),
          ("pduEU", 3),
          ("enviroHawk2", 4),
          ("idm", 5),
          ("autoWithTraps", 253),
          ("auto", 254),
          ("inactive", 255))
    )



class UnsignedTimeTicks(TextualConvention, Unsigned32):
    status = "current"


class WiringTopologyType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("singlePhase", 2),
          ("twoPhase", 3),
          ("threePhaseStar", 4),
          ("threePhaseDelta", 5),
          ("deltaWithNeutral", 6),
          ("none", 254),
          ("unknown", 255))
    )



class CktRefName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )



class BranchCircuitStatusType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("closeOn", 1),
          ("openOff", 2),
          ("invalidFeature", 255))
    )



class BranchCircuitConfigType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("closeOn", 1),
          ("openOff", 2),
          ("invalidFeature", 255))
    )



class ControlledOutletStatusType(TextualConvention, Integer32):
    status = "current"
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
        *(("on", 1),
          ("off", 2),
          ("lastKnownState", 3),
          ("timeDelayOn", 4))
    )



# MIB Managed Objects in the order of their OIDs

_Sinetica_ObjectIdentity = ObjectIdentity
sinetica = _Sinetica_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711)
)
_V1_ObjectIdentity = ObjectIdentity
v1 = _V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1)
)
_Objects_ObjectIdentity = ObjectIdentity
objects = _Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1)
)
_Inputs_ObjectIdentity = ObjectIdentity
inputs = _Inputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1)
)
_IpCommon_ObjectIdentity = ObjectIdentity
ipCommon = _IpCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 1)
)
_IpEnable_ObjectIdentity = ObjectIdentity
ipEnable = _IpEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 1, 1)
)


class _IpSelect_Type(Integer32):
    """Custom type ipSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_IpSelect_Type.__name__ = "Integer32"
_IpSelect_Object = MibScalar
ipSelect = _IpSelect_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 1, 1, 1),
    _IpSelect_Type()
)
ipSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSelect.setStatus("current")
_IpInsert_Type = InputDataType
_IpInsert_Object = MibScalar
ipInsert = _IpInsert_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 1, 1, 2),
    _IpInsert_Type()
)
ipInsert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInsert.setStatus("current")
_IpTHA_ObjectIdentity = ObjectIdentity
ipTHA = _IpTHA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2)
)


class _IpTempScaleFlag_Type(Integer32):
    """Custom type ipTempScaleFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("celsius", 1),
          ("fahrenheit", 2),
          ("kelvin", 3))
    )


_IpTempScaleFlag_Type.__name__ = "Integer32"
_IpTempScaleFlag_Object = MibScalar
ipTempScaleFlag = _IpTempScaleFlag_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 1),
    _IpTempScaleFlag_Type()
)
ipTempScaleFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTempScaleFlag.setStatus("current")
_IpTHATable_Object = MibTable
ipTHATable = _IpTHATable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ipTHATable.setStatus("current")
_IpTHAEntry_Object = MibTableRow
ipTHAEntry = _IpTHAEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 2, 1)
)
ipTHAEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "ipTHAChan"),
)
if mibBuilder.loadTexts:
    ipTHAEntry.setStatus("current")


class _IpTHAChan_Type(Integer32):
    """Custom type ipTHAChan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_IpTHAChan_Type.__name__ = "Integer32"
_IpTHAChan_Object = MibTableColumn
ipTHAChan = _IpTHAChan_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 2, 1, 1),
    _IpTHAChan_Type()
)
ipTHAChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTHAChan.setStatus("current")
_IpTHARS_Type = RowStatus
_IpTHARS_Object = MibTableColumn
ipTHARS = _IpTHARS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 2, 1, 2),
    _IpTHARS_Type()
)
ipTHARS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTHARS.setStatus("current")
_IpTHAName_Type = DisplayString
_IpTHAName_Object = MibTableColumn
ipTHAName = _IpTHAName_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 2, 1, 3),
    _IpTHAName_Type()
)
ipTHAName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTHAName.setStatus("current")
_IpTHALocn_Type = DisplayString
_IpTHALocn_Object = MibTableColumn
ipTHALocn = _IpTHALocn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 2, 1, 4),
    _IpTHALocn_Type()
)
ipTHALocn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTHALocn.setStatus("current")
_IpTHAAutoDetect_Type = TruthValue
_IpTHAAutoDetect_Object = MibTableColumn
ipTHAAutoDetect = _IpTHAAutoDetect_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 2, 1, 5),
    _IpTHAAutoDetect_Type()
)
ipTHAAutoDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTHAAutoDetect.setStatus("current")
_IpTHAType_Type = InputDataType
_IpTHAType_Object = MibTableColumn
ipTHAType = _IpTHAType_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 2, 1, 6),
    _IpTHAType_Type()
)
ipTHAType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTHAType.setStatus("current")


class _IpTHAValue_Type(Integer32):
    """Custom type ipTHAValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999999999, -999999999),
        ValueRangeConstraint(-99999999, -99999999),
        ValueRangeConstraint(-17999680, -17999680),
        ValueRangeConstraint(-10000000, -10000000),
        ValueRangeConstraint(-9997268, -9997268),
        ValueRangeConstraint(-580, 120000),
        ValueRangeConstraint(10000000, 10000000),
        ValueRangeConstraint(10002732, 10002732),
        ValueRangeConstraint(18000320, 18000320),
        ValueRangeConstraint(99999999, 99999999),
    )


_IpTHAValue_Type.__name__ = "Integer32"
_IpTHAValue_Object = MibTableColumn
ipTHAValue = _IpTHAValue_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 2, 1, 7),
    _IpTHAValue_Type()
)
ipTHAValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTHAValue.setStatus("current")


class _IpTHAScaling_Type(Integer32):
    """Custom type ipTHAScaling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(1000, 1000),
        ValueRangeConstraint(10000, 10000),
    )


_IpTHAScaling_Type.__name__ = "Integer32"
_IpTHAScaling_Object = MibTableColumn
ipTHAScaling = _IpTHAScaling_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 2, 1, 8),
    _IpTHAScaling_Type()
)
ipTHAScaling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTHAScaling.setStatus("current")


class _IpTHAOffset_Type(Integer32):
    """Custom type ipTHAOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1479, 2119),
    )


_IpTHAOffset_Type.__name__ = "Integer32"
_IpTHAOffset_Object = MibTableColumn
ipTHAOffset = _IpTHAOffset_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 2, 1, 9),
    _IpTHAOffset_Type()
)
ipTHAOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTHAOffset.setStatus("current")


class _IpTHAHysteresis_Type(Integer32):
    """Custom type ipTHAHysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1479, 2119),
    )


_IpTHAHysteresis_Type.__name__ = "Integer32"
_IpTHAHysteresis_Object = MibTableColumn
ipTHAHysteresis = _IpTHAHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 2, 1, 10),
    _IpTHAHysteresis_Type()
)
ipTHAHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTHAHysteresis.setStatus("current")
_IpTHATrapsCfg_ObjectIdentity = ObjectIdentity
ipTHATrapsCfg = _IpTHATrapsCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3)
)
_IpTHAThreshTable_Object = MibTable
ipTHAThreshTable = _IpTHAThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ipTHAThreshTable.setStatus("current")
_IpTHAThreshEntry_Object = MibTableRow
ipTHAThreshEntry = _IpTHAThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 1, 1)
)
ipTHAThreshEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "ipTHAThreshChan"),
)
if mibBuilder.loadTexts:
    ipTHAThreshEntry.setStatus("current")


class _IpTHAThreshChan_Type(Integer32):
    """Custom type ipTHAThreshChan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_IpTHAThreshChan_Type.__name__ = "Integer32"
_IpTHAThreshChan_Object = MibTableColumn
ipTHAThreshChan = _IpTHAThreshChan_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 1, 1, 1),
    _IpTHAThreshChan_Type()
)
ipTHAThreshChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTHAThreshChan.setStatus("current")
_IpTHAThreshRS_Type = RowStatus
_IpTHAThreshRS_Object = MibTableColumn
ipTHAThreshRS = _IpTHAThreshRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 1, 1, 2),
    _IpTHAThreshRS_Type()
)
ipTHAThreshRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTHAThreshRS.setStatus("current")


class _IpTHAUCL_Type(Integer32):
    """Custom type ipTHAUCL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-300, 100000),
    )


_IpTHAUCL_Type.__name__ = "Integer32"
_IpTHAUCL_Object = MibTableColumn
ipTHAUCL = _IpTHAUCL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 1, 1, 3),
    _IpTHAUCL_Type()
)
ipTHAUCL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTHAUCL.setStatus("current")


class _IpTHAUWL_Type(Integer32):
    """Custom type ipTHAUWL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-300, 100000),
    )


_IpTHAUWL_Type.__name__ = "Integer32"
_IpTHAUWL_Object = MibTableColumn
ipTHAUWL = _IpTHAUWL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 1, 1, 4),
    _IpTHAUWL_Type()
)
ipTHAUWL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTHAUWL.setStatus("current")


class _IpTHALWL_Type(Integer32):
    """Custom type ipTHALWL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-300, 100000),
    )


_IpTHALWL_Type.__name__ = "Integer32"
_IpTHALWL_Object = MibTableColumn
ipTHALWL = _IpTHALWL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 1, 1, 5),
    _IpTHALWL_Type()
)
ipTHALWL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTHALWL.setStatus("current")


class _IpTHALCL_Type(Integer32):
    """Custom type ipTHALCL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-300, 100000),
    )


_IpTHALCL_Type.__name__ = "Integer32"
_IpTHALCL_Object = MibTableColumn
ipTHALCL = _IpTHALCL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 1, 1, 6),
    _IpTHALCL_Type()
)
ipTHALCL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTHALCL.setStatus("current")
_IpTHADeltaPos_Type = Unsigned32
_IpTHADeltaPos_Object = MibTableColumn
ipTHADeltaPos = _IpTHADeltaPos_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 1, 1, 7),
    _IpTHADeltaPos_Type()
)
ipTHADeltaPos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTHADeltaPos.setStatus("current")
_IpTHADeltaNeg_Type = Unsigned32
_IpTHADeltaNeg_Object = MibTableColumn
ipTHADeltaNeg = _IpTHADeltaNeg_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 1, 1, 8),
    _IpTHADeltaNeg_Type()
)
ipTHADeltaNeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTHADeltaNeg.setStatus("current")
_IpTHATrapEnTable_Object = MibTable
ipTHATrapEnTable = _IpTHATrapEnTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    ipTHATrapEnTable.setStatus("current")
_IpTHATrapEnEntry_Object = MibTableRow
ipTHATrapEnEntry = _IpTHATrapEnEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 2, 1)
)
ipTHATrapEnEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "ipTHATrapEnChan"),
)
if mibBuilder.loadTexts:
    ipTHATrapEnEntry.setStatus("current")


class _IpTHATrapEnChan_Type(Integer32):
    """Custom type ipTHATrapEnChan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_IpTHATrapEnChan_Type.__name__ = "Integer32"
_IpTHATrapEnChan_Object = MibTableColumn
ipTHATrapEnChan = _IpTHATrapEnChan_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 2, 1, 1),
    _IpTHATrapEnChan_Type()
)
ipTHATrapEnChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTHATrapEnChan.setStatus("current")
_IpTHATrapEnRS_Type = RowStatus
_IpTHATrapEnRS_Object = MibTableColumn
ipTHATrapEnRS = _IpTHATrapEnRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 2, 1, 2),
    _IpTHATrapEnRS_Type()
)
ipTHATrapEnRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTHATrapEnRS.setStatus("current")
_IpTHAUCLTrapEn_Type = TruthValue
_IpTHAUCLTrapEn_Object = MibTableColumn
ipTHAUCLTrapEn = _IpTHAUCLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 2, 1, 3),
    _IpTHAUCLTrapEn_Type()
)
ipTHAUCLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTHAUCLTrapEn.setStatus("current")
_IpTHAUWLTrapEn_Type = TruthValue
_IpTHAUWLTrapEn_Object = MibTableColumn
ipTHAUWLTrapEn = _IpTHAUWLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 2, 1, 4),
    _IpTHAUWLTrapEn_Type()
)
ipTHAUWLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTHAUWLTrapEn.setStatus("current")
_IpTHALWLTrapEn_Type = TruthValue
_IpTHALWLTrapEn_Object = MibTableColumn
ipTHALWLTrapEn = _IpTHALWLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 2, 1, 5),
    _IpTHALWLTrapEn_Type()
)
ipTHALWLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTHALWLTrapEn.setStatus("current")
_IpTHALCLTrapEn_Type = TruthValue
_IpTHALCLTrapEn_Object = MibTableColumn
ipTHALCLTrapEn = _IpTHALCLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 2, 1, 6),
    _IpTHALCLTrapEn_Type()
)
ipTHALCLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTHALCLTrapEn.setStatus("current")
_IpTHADeltaPosTrapEn_Type = TruthValue
_IpTHADeltaPosTrapEn_Object = MibTableColumn
ipTHADeltaPosTrapEn = _IpTHADeltaPosTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 2, 1, 7),
    _IpTHADeltaPosTrapEn_Type()
)
ipTHADeltaPosTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTHADeltaPosTrapEn.setStatus("current")
_IpTHADeltaNegTrapEn_Type = TruthValue
_IpTHADeltaNegTrapEn_Object = MibTableColumn
ipTHADeltaNegTrapEn = _IpTHADeltaNegTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 2, 1, 8),
    _IpTHADeltaNegTrapEn_Type()
)
ipTHADeltaNegTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTHADeltaNegTrapEn.setStatus("current")
_IpTHATrapPerTable_Object = MibTable
ipTHATrapPerTable = _IpTHATrapPerTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 3)
)
if mibBuilder.loadTexts:
    ipTHATrapPerTable.setStatus("current")
_IpTHATrapPerEntry_Object = MibTableRow
ipTHATrapPerEntry = _IpTHATrapPerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 3, 1)
)
ipTHATrapPerEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "ipTHATrapPerChan"),
)
if mibBuilder.loadTexts:
    ipTHATrapPerEntry.setStatus("current")


class _IpTHATrapPerChan_Type(Integer32):
    """Custom type ipTHATrapPerChan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_IpTHATrapPerChan_Type.__name__ = "Integer32"
_IpTHATrapPerChan_Object = MibTableColumn
ipTHATrapPerChan = _IpTHATrapPerChan_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 3, 1, 1),
    _IpTHATrapPerChan_Type()
)
ipTHATrapPerChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTHATrapPerChan.setStatus("current")
_IpTHATrapPerRS_Type = RowStatus
_IpTHATrapPerRS_Object = MibTableColumn
ipTHATrapPerRS = _IpTHATrapPerRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 3, 1, 2),
    _IpTHATrapPerRS_Type()
)
ipTHATrapPerRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTHATrapPerRS.setStatus("current")


class _IpTHATrapUCLPer_Type(Unsigned32):
    """Custom type ipTHATrapUCLPer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpTHATrapUCLPer_Type.__name__ = "Unsigned32"
_IpTHATrapUCLPer_Object = MibTableColumn
ipTHATrapUCLPer = _IpTHATrapUCLPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 3, 1, 3),
    _IpTHATrapUCLPer_Type()
)
ipTHATrapUCLPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTHATrapUCLPer.setStatus("current")


class _IpTHATrapUWLPer_Type(Unsigned32):
    """Custom type ipTHATrapUWLPer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpTHATrapUWLPer_Type.__name__ = "Unsigned32"
_IpTHATrapUWLPer_Object = MibTableColumn
ipTHATrapUWLPer = _IpTHATrapUWLPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 3, 1, 4),
    _IpTHATrapUWLPer_Type()
)
ipTHATrapUWLPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTHATrapUWLPer.setStatus("current")


class _IpTHATrapLWLPer_Type(Unsigned32):
    """Custom type ipTHATrapLWLPer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpTHATrapLWLPer_Type.__name__ = "Unsigned32"
_IpTHATrapLWLPer_Object = MibTableColumn
ipTHATrapLWLPer = _IpTHATrapLWLPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 3, 1, 5),
    _IpTHATrapLWLPer_Type()
)
ipTHATrapLWLPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTHATrapLWLPer.setStatus("current")


class _IpTHATrapLCLPer_Type(Unsigned32):
    """Custom type ipTHATrapLCLPer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpTHATrapLCLPer_Type.__name__ = "Unsigned32"
_IpTHATrapLCLPer_Object = MibTableColumn
ipTHATrapLCLPer = _IpTHATrapLCLPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 3, 1, 6),
    _IpTHATrapLCLPer_Type()
)
ipTHATrapLCLPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTHATrapLCLPer.setStatus("current")


class _IpTHATrapDeltaPosPer_Type(Unsigned32):
    """Custom type ipTHATrapDeltaPosPer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpTHATrapDeltaPosPer_Type.__name__ = "Unsigned32"
_IpTHATrapDeltaPosPer_Object = MibTableColumn
ipTHATrapDeltaPosPer = _IpTHATrapDeltaPosPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 3, 1, 7),
    _IpTHATrapDeltaPosPer_Type()
)
ipTHATrapDeltaPosPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTHATrapDeltaPosPer.setStatus("current")


class _IpTHATrapDeltaNegPer_Type(Unsigned32):
    """Custom type ipTHATrapDeltaNegPer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpTHATrapDeltaNegPer_Type.__name__ = "Unsigned32"
_IpTHATrapDeltaNegPer_Object = MibTableColumn
ipTHATrapDeltaNegPer = _IpTHATrapDeltaNegPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 3, 1, 8),
    _IpTHATrapDeltaNegPer_Type()
)
ipTHATrapDeltaNegPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTHATrapDeltaNegPer.setStatus("current")
_IpContact_ObjectIdentity = ObjectIdentity
ipContact = _IpContact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 3)
)
_IpContTable_Object = MibTable
ipContTable = _IpContTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ipContTable.setStatus("current")
_IpContEntry_Object = MibTableRow
ipContEntry = _IpContEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 3, 1, 1)
)
ipContEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "ipContChan"),
)
if mibBuilder.loadTexts:
    ipContEntry.setStatus("current")


class _IpContChan_Type(Integer32):
    """Custom type ipContChan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_IpContChan_Type.__name__ = "Integer32"
_IpContChan_Object = MibTableColumn
ipContChan = _IpContChan_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 3, 1, 1, 1),
    _IpContChan_Type()
)
ipContChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipContChan.setStatus("current")
_IpContRS_Type = RowStatus
_IpContRS_Object = MibTableColumn
ipContRS = _IpContRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 3, 1, 1, 2),
    _IpContRS_Type()
)
ipContRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipContRS.setStatus("current")
_IpContName_Type = DisplayString
_IpContName_Object = MibTableColumn
ipContName = _IpContName_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 3, 1, 1, 3),
    _IpContName_Type()
)
ipContName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipContName.setStatus("current")
_IpContLocn_Type = DisplayString
_IpContLocn_Object = MibTableColumn
ipContLocn = _IpContLocn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 3, 1, 1, 4),
    _IpContLocn_Type()
)
ipContLocn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipContLocn.setStatus("current")
_IpContAutoDetect_Type = TruthValue
_IpContAutoDetect_Object = MibTableColumn
ipContAutoDetect = _IpContAutoDetect_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 3, 1, 1, 5),
    _IpContAutoDetect_Type()
)
ipContAutoDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipContAutoDetect.setStatus("current")
_IpContNormState_Type = ContactState
_IpContNormState_Object = MibTableColumn
ipContNormState = _IpContNormState_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 3, 1, 1, 6),
    _IpContNormState_Type()
)
ipContNormState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipContNormState.setStatus("current")
_IpContCurrState_Type = InputContactState
_IpContCurrState_Object = MibTableColumn
ipContCurrState = _IpContCurrState_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 3, 1, 1, 7),
    _IpContCurrState_Type()
)
ipContCurrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipContCurrState.setStatus("current")


class _IpContTrigMode_Type(Integer32):
    """Custom type ipContTrigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("positiveEdge", 1),
          ("negativeEdge", 2),
          ("level", 3))
    )


_IpContTrigMode_Type.__name__ = "Integer32"
_IpContTrigMode_Object = MibTableColumn
ipContTrigMode = _IpContTrigMode_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 3, 1, 1, 8),
    _IpContTrigMode_Type()
)
ipContTrigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipContTrigMode.setStatus("current")
_IpContReset_Type = Unsigned32
_IpContReset_Object = MibTableColumn
ipContReset = _IpContReset_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 3, 1, 1, 9),
    _IpContReset_Type()
)
ipContReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipContReset.setStatus("current")


class _IpContTrapEn_Type(Integer32):
    """Custom type ipContTrapEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("warning", 2),
          ("information", 3),
          ("disabled", 255))
    )


_IpContTrapEn_Type.__name__ = "Integer32"
_IpContTrapEn_Object = MibTableColumn
ipContTrapEn = _IpContTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 3, 1, 1, 10),
    _IpContTrapEn_Type()
)
ipContTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipContTrapEn.setStatus("current")


class _IpContTrapPeriod_Type(Integer32):
    """Custom type ipContTrapPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpContTrapPeriod_Type.__name__ = "Integer32"
_IpContTrapPeriod_Object = MibTableColumn
ipContTrapPeriod = _IpContTrapPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 3, 1, 1, 11),
    _IpContTrapPeriod_Type()
)
ipContTrapPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipContTrapPeriod.setStatus("current")
_Outputs_ObjectIdentity = ObjectIdentity
outputs = _Outputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 2)
)
_OpEnable_ObjectIdentity = ObjectIdentity
opEnable = _OpEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 2, 1)
)


class _OpSelect_Type(Integer32):
    """Custom type opSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_OpSelect_Type.__name__ = "Integer32"
_OpSelect_Object = MibScalar
opSelect = _OpSelect_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 2, 1, 1),
    _OpSelect_Type()
)
opSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opSelect.setStatus("current")
_OpInsert_Type = EnableState
_OpInsert_Object = MibScalar
opInsert = _OpInsert_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 2, 1, 2),
    _OpInsert_Type()
)
opInsert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opInsert.setStatus("current")
_OpTable_Object = MibTable
opTable = _OpTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    opTable.setStatus("current")
_OpEntry_Object = MibTableRow
opEntry = _OpEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 2, 2, 1)
)
opEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "opChan"),
)
if mibBuilder.loadTexts:
    opEntry.setStatus("current")


class _OpChan_Type(Integer32):
    """Custom type opChan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_OpChan_Type.__name__ = "Integer32"
_OpChan_Object = MibTableColumn
opChan = _OpChan_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 2, 2, 1, 1),
    _OpChan_Type()
)
opChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opChan.setStatus("current")
_OpRS_Type = RowStatus
_OpRS_Object = MibTableColumn
opRS = _OpRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 2, 2, 1, 2),
    _OpRS_Type()
)
opRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opRS.setStatus("current")
_OpName_Type = DisplayString
_OpName_Object = MibTableColumn
opName = _OpName_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 2, 2, 1, 3),
    _OpName_Type()
)
opName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opName.setStatus("current")
_OpLocn_Type = DisplayString
_OpLocn_Object = MibTableColumn
opLocn = _OpLocn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 2, 2, 1, 4),
    _OpLocn_Type()
)
opLocn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opLocn.setStatus("current")
_OpNormState_Type = RelayState
_OpNormState_Object = MibTableColumn
opNormState = _OpNormState_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 2, 2, 1, 5),
    _OpNormState_Type()
)
opNormState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opNormState.setStatus("current")
_OpCurrState_Type = RelayState
_OpCurrState_Object = MibTableColumn
opCurrState = _OpCurrState_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 2, 2, 1, 6),
    _OpCurrState_Type()
)
opCurrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opCurrState.setStatus("current")
_OpOnDelTime_Type = Unsigned32
_OpOnDelTime_Object = MibTableColumn
opOnDelTime = _OpOnDelTime_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 2, 2, 1, 7),
    _OpOnDelTime_Type()
)
opOnDelTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opOnDelTime.setStatus("current")
_OpOffDelTime_Type = Unsigned32
_OpOffDelTime_Object = MibTableColumn
opOffDelTime = _OpOffDelTime_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 2, 2, 1, 8),
    _OpOffDelTime_Type()
)
opOffDelTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opOffDelTime.setStatus("current")
_OpBooleanEqn_Type = DisplayString
_OpBooleanEqn_Object = MibTableColumn
opBooleanEqn = _OpBooleanEqn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 2, 2, 1, 9),
    _OpBooleanEqn_Type()
)
opBooleanEqn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opBooleanEqn.setStatus("current")


class _OpTrapEn_Type(Integer32):
    """Custom type opTrapEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("warning", 2),
          ("information", 3),
          ("disabled", 255))
    )


_OpTrapEn_Type.__name__ = "Integer32"
_OpTrapEn_Object = MibTableColumn
opTrapEn = _OpTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 2, 2, 1, 10),
    _OpTrapEn_Type()
)
opTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opTrapEn.setStatus("current")


class _OpTrapPeriod_Type(Unsigned32):
    """Custom type opTrapPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OpTrapPeriod_Type.__name__ = "Unsigned32"
_OpTrapPeriod_Object = MibTableColumn
opTrapPeriod = _OpTrapPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 2, 2, 1, 11),
    _OpTrapPeriod_Type()
)
opTrapPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opTrapPeriod.setStatus("current")
_OpControlState_Type = OutputControlState
_OpControlState_Object = MibTableColumn
opControlState = _OpControlState_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 2, 2, 1, 12),
    _OpControlState_Type()
)
opControlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opControlState.setStatus("current")
_Keypads_ObjectIdentity = ObjectIdentity
keypads = _Keypads_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 4)
)
_KpEnable_ObjectIdentity = ObjectIdentity
kpEnable = _KpEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 4, 1)
)


class _KpSelect_Type(Integer32):
    """Custom type kpSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_KpSelect_Type.__name__ = "Integer32"
_KpSelect_Object = MibScalar
kpSelect = _KpSelect_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 4, 1, 1),
    _KpSelect_Type()
)
kpSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kpSelect.setStatus("current")
_KpInsert_Type = KeypadEnableState
_KpInsert_Object = MibScalar
kpInsert = _KpInsert_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 4, 1, 2),
    _KpInsert_Type()
)
kpInsert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kpInsert.setStatus("current")
_KpCtlTable_Object = MibTable
kpCtlTable = _KpCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    kpCtlTable.setStatus("current")
_KpCtlEntry_Object = MibTableRow
kpCtlEntry = _KpCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 4, 2, 1)
)
kpCtlEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "kpNumber"),
)
if mibBuilder.loadTexts:
    kpCtlEntry.setStatus("current")


class _KpNumber_Type(Integer32):
    """Custom type kpNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_KpNumber_Type.__name__ = "Integer32"
_KpNumber_Object = MibTableColumn
kpNumber = _KpNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 4, 2, 1, 1),
    _KpNumber_Type()
)
kpNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpNumber.setStatus("current")
_KpRS_Type = RowStatus
_KpRS_Object = MibTableColumn
kpRS = _KpRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 4, 2, 1, 2),
    _KpRS_Type()
)
kpRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpRS.setStatus("current")
_KpManufacturer_Type = DisplayString
_KpManufacturer_Object = MibTableColumn
kpManufacturer = _KpManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 4, 2, 1, 3),
    _KpManufacturer_Type()
)
kpManufacturer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kpManufacturer.setStatus("current")
_KpName_Type = DisplayString
_KpName_Object = MibTableColumn
kpName = _KpName_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 4, 2, 1, 4),
    _KpName_Type()
)
kpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kpName.setStatus("current")
_KpDoorLatchTimeOut_Type = Unsigned32
_KpDoorLatchTimeOut_Object = MibTableColumn
kpDoorLatchTimeOut = _KpDoorLatchTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 4, 2, 1, 5),
    _KpDoorLatchTimeOut_Type()
)
kpDoorLatchTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kpDoorLatchTimeOut.setStatus("current")


class _KpRtnToStndbyTimeOut_Type(Integer32):
    """Custom type kpRtnToStndbyTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_KpRtnToStndbyTimeOut_Type.__name__ = "Integer32"
_KpRtnToStndbyTimeOut_Object = MibTableColumn
kpRtnToStndbyTimeOut = _KpRtnToStndbyTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 4, 2, 1, 6),
    _KpRtnToStndbyTimeOut_Type()
)
kpRtnToStndbyTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kpRtnToStndbyTimeOut.setStatus("current")
_KpEntryCodeValid_Type = TruthValue
_KpEntryCodeValid_Object = MibTableColumn
kpEntryCodeValid = _KpEntryCodeValid_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 4, 2, 1, 7),
    _KpEntryCodeValid_Type()
)
kpEntryCodeValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpEntryCodeValid.setStatus("current")


class _KpDoorOpenTimeOut_Type(Integer32):
    """Custom type kpDoorOpenTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_KpDoorOpenTimeOut_Type.__name__ = "Integer32"
_KpDoorOpenTimeOut_Object = MibTableColumn
kpDoorOpenTimeOut = _KpDoorOpenTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 4, 2, 1, 8),
    _KpDoorOpenTimeOut_Type()
)
kpDoorOpenTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kpDoorOpenTimeOut.setStatus("current")
_KpRemoteDoorOpen_Type = TruthValue
_KpRemoteDoorOpen_Object = MibTableColumn
kpRemoteDoorOpen = _KpRemoteDoorOpen_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 4, 2, 1, 9),
    _KpRemoteDoorOpen_Type()
)
kpRemoteDoorOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kpRemoteDoorOpen.setStatus("current")


class _KpInUseTrapEn_Type(Integer32):
    """Custom type kpInUseTrapEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("warning", 2),
          ("information", 3),
          ("disabled", 255))
    )


_KpInUseTrapEn_Type.__name__ = "Integer32"
_KpInUseTrapEn_Object = MibTableColumn
kpInUseTrapEn = _KpInUseTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 4, 2, 1, 10),
    _KpInUseTrapEn_Type()
)
kpInUseTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kpInUseTrapEn.setStatus("current")
_Acus_ObjectIdentity = ObjectIdentity
acus = _Acus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 5)
)
_AcuEnable_ObjectIdentity = ObjectIdentity
acuEnable = _AcuEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 5, 1)
)


class _AcuSelect_Type(Integer32):
    """Custom type acuSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_AcuSelect_Type.__name__ = "Integer32"
_AcuSelect_Object = MibScalar
acuSelect = _AcuSelect_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 5, 1, 1),
    _AcuSelect_Type()
)
acuSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acuSelect.setStatus("current")
_AcuInsert_Type = EnableState
_AcuInsert_Object = MibScalar
acuInsert = _AcuInsert_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 5, 1, 2),
    _AcuInsert_Type()
)
acuInsert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acuInsert.setStatus("current")
_AcuCtlTable_Object = MibTable
acuCtlTable = _AcuCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    acuCtlTable.setStatus("current")
_AcuCtlEntry_Object = MibTableRow
acuCtlEntry = _AcuCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 5, 2, 1)
)
acuCtlEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "acuNumber"),
)
if mibBuilder.loadTexts:
    acuCtlEntry.setStatus("current")


class _AcuNumber_Type(Integer32):
    """Custom type acuNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_AcuNumber_Type.__name__ = "Integer32"
_AcuNumber_Object = MibTableColumn
acuNumber = _AcuNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 5, 2, 1, 1),
    _AcuNumber_Type()
)
acuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acuNumber.setStatus("current")
_AcuCtlRS_Type = RowStatus
_AcuCtlRS_Object = MibTableColumn
acuCtlRS = _AcuCtlRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 5, 2, 1, 2),
    _AcuCtlRS_Type()
)
acuCtlRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acuCtlRS.setStatus("current")
_AcuManufacturer_Type = DisplayString
_AcuManufacturer_Object = MibTableColumn
acuManufacturer = _AcuManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 5, 2, 1, 3),
    _AcuManufacturer_Type()
)
acuManufacturer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acuManufacturer.setStatus("current")
_AcuName_Type = DisplayString
_AcuName_Object = MibTableColumn
acuName = _AcuName_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 5, 2, 1, 4),
    _AcuName_Type()
)
acuName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acuName.setStatus("current")


class _AcuDoorLatchTimeOut_Type(Unsigned32):
    """Custom type acuDoorLatchTimeOut based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_AcuDoorLatchTimeOut_Type.__name__ = "Unsigned32"
_AcuDoorLatchTimeOut_Object = MibTableColumn
acuDoorLatchTimeOut = _AcuDoorLatchTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 5, 2, 1, 5),
    _AcuDoorLatchTimeOut_Type()
)
acuDoorLatchTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acuDoorLatchTimeOut.setStatus("current")


class _AcuRtnToStndbyTimeOut_Type(Integer32):
    """Custom type acuRtnToStndbyTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_AcuRtnToStndbyTimeOut_Type.__name__ = "Integer32"
_AcuRtnToStndbyTimeOut_Object = MibTableColumn
acuRtnToStndbyTimeOut = _AcuRtnToStndbyTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 5, 2, 1, 6),
    _AcuRtnToStndbyTimeOut_Type()
)
acuRtnToStndbyTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acuRtnToStndbyTimeOut.setStatus("current")
_AcuEntryCodeValid_Type = TruthValue
_AcuEntryCodeValid_Object = MibTableColumn
acuEntryCodeValid = _AcuEntryCodeValid_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 5, 2, 1, 7),
    _AcuEntryCodeValid_Type()
)
acuEntryCodeValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acuEntryCodeValid.setStatus("current")


class _AcuDoorOpenTimeOut_Type(Integer32):
    """Custom type acuDoorOpenTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_AcuDoorOpenTimeOut_Type.__name__ = "Integer32"
_AcuDoorOpenTimeOut_Object = MibTableColumn
acuDoorOpenTimeOut = _AcuDoorOpenTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 5, 2, 1, 8),
    _AcuDoorOpenTimeOut_Type()
)
acuDoorOpenTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acuDoorOpenTimeOut.setStatus("current")
_AcuRemoteDoorOpen_Type = TruthValue
_AcuRemoteDoorOpen_Object = MibTableColumn
acuRemoteDoorOpen = _AcuRemoteDoorOpen_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 5, 2, 1, 9),
    _AcuRemoteDoorOpen_Type()
)
acuRemoteDoorOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acuRemoteDoorOpen.setStatus("current")


class _AcuInUseTrapEn_Type(Integer32):
    """Custom type acuInUseTrapEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("warning", 2),
          ("information", 3),
          ("disabled", 255))
    )


_AcuInUseTrapEn_Type.__name__ = "Integer32"
_AcuInUseTrapEn_Object = MibTableColumn
acuInUseTrapEn = _AcuInUseTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 5, 2, 1, 10),
    _AcuInUseTrapEn_Type()
)
acuInUseTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acuInUseTrapEn.setStatus("current")
_AcuType_Type = DisplayString
_AcuType_Object = MibTableColumn
acuType = _AcuType_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 5, 2, 1, 11),
    _AcuType_Type()
)
acuType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acuType.setStatus("current")
_AcuAlarms_Type = Unsigned32
_AcuAlarms_Object = MibTableColumn
acuAlarms = _AcuAlarms_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 5, 2, 1, 12),
    _AcuAlarms_Type()
)
acuAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acuAlarms.setStatus("current")
_AcuLastCode_Type = DisplayString
_AcuLastCode_Object = MibTableColumn
acuLastCode = _AcuLastCode_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 5, 2, 1, 13),
    _AcuLastCode_Type()
)
acuLastCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acuLastCode.setStatus("current")
_Access_ObjectIdentity = ObjectIdentity
access = _Access_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 6)
)
_AccUserCtl_ObjectIdentity = ObjectIdentity
accUserCtl = _AccUserCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 6, 1)
)


class _AccUserInstance_Type(Integer32):
    """Custom type accUserInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_AccUserInstance_Type.__name__ = "Integer32"
_AccUserInstance_Object = MibScalar
accUserInstance = _AccUserInstance_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 6, 1, 1),
    _AccUserInstance_Type()
)
accUserInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accUserInstance.setStatus("current")
_AccUserTable_Object = MibTable
accUserTable = _AccUserTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 6, 1, 2)
)
if mibBuilder.loadTexts:
    accUserTable.setStatus("current")
_AccUserEntry_Object = MibTableRow
accUserEntry = _AccUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 6, 1, 2, 1)
)
accUserEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "accUserNumber"),
)
if mibBuilder.loadTexts:
    accUserEntry.setStatus("current")
_AccUserNumber_Type = Unsigned32
_AccUserNumber_Object = MibTableColumn
accUserNumber = _AccUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 6, 1, 2, 1, 1),
    _AccUserNumber_Type()
)
accUserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accUserNumber.setStatus("current")
_AccUserRS_Type = RowStatus
_AccUserRS_Object = MibTableColumn
accUserRS = _AccUserRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 6, 1, 2, 1, 2),
    _AccUserRS_Type()
)
accUserRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accUserRS.setStatus("current")
_AccUserName_Type = DisplayString
_AccUserName_Object = MibTableColumn
accUserName = _AccUserName_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 6, 1, 2, 1, 3),
    _AccUserName_Type()
)
accUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accUserName.setStatus("current")


class _AccUserCode_Type(OctetString):
    """Custom type accUserCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AccUserCode_Type.__name__ = "OctetString"
_AccUserCode_Object = MibTableColumn
accUserCode = _AccUserCode_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 6, 1, 2, 1, 4),
    _AccUserCode_Type()
)
accUserCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accUserCode.setStatus("current")
_AccUserPrivileges_Type = DisplayString
_AccUserPrivileges_Object = MibTableColumn
accUserPrivileges = _AccUserPrivileges_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 6, 1, 2, 1, 5),
    _AccUserPrivileges_Type()
)
accUserPrivileges.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accUserPrivileges.setStatus("current")
_AccUserExpires_Type = DisplayString
_AccUserExpires_Object = MibTableColumn
accUserExpires = _AccUserExpires_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 6, 1, 2, 1, 6),
    _AccUserExpires_Type()
)
accUserExpires.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accUserExpires.setStatus("current")
_AccUserSetup_Type = OctetString
_AccUserSetup_Object = MibScalar
accUserSetup = _AccUserSetup_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 6, 1, 3),
    _AccUserSetup_Type()
)
accUserSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accUserSetup.setStatus("current")


class _AccUserCodeLen_Type(Integer32):
    """Custom type accUserCodeLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_AccUserCodeLen_Type.__name__ = "Integer32"
_AccUserCodeLen_Object = MibScalar
accUserCodeLen = _AccUserCodeLen_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 6, 1, 4),
    _AccUserCodeLen_Type()
)
accUserCodeLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accUserCodeLen.setStatus("current")
_Pdus_ObjectIdentity = ObjectIdentity
pdus = _Pdus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7)
)
_PduCommon_ObjectIdentity = ObjectIdentity
pduCommon = _PduCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 1)
)
_PdusEnable_ObjectIdentity = ObjectIdentity
pdusEnable = _PdusEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 1, 1)
)


class _PduSelect_Type(Integer32):
    """Custom type pduSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_PduSelect_Type.__name__ = "Integer32"
_PduSelect_Object = MibScalar
pduSelect = _PduSelect_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 1, 1, 1),
    _PduSelect_Type()
)
pduSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSelect.setStatus("current")
_PduInsert_Type = EnableState
_PduInsert_Object = MibScalar
pduInsert = _PduInsert_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 1, 1, 2),
    _PduInsert_Type()
)
pduInsert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduInsert.setStatus("current")
_PduTable_Object = MibTable
pduTable = _PduTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 1, 2)
)
if mibBuilder.loadTexts:
    pduTable.setStatus("current")
_PduEntry_Object = MibTableRow
pduEntry = _PduEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 1, 2, 1)
)
pduEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "pduNumber"),
)
if mibBuilder.loadTexts:
    pduEntry.setStatus("current")
_PduNumber_Type = Unsigned32
_PduNumber_Object = MibTableColumn
pduNumber = _PduNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 1, 2, 1, 1),
    _PduNumber_Type()
)
pduNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNumber.setStatus("current")
_PduRS_Type = RowStatus
_PduRS_Object = MibTableColumn
pduRS = _PduRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 1, 2, 1, 2),
    _PduRS_Type()
)
pduRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduRS.setStatus("current")
_PduName_Type = DisplayString
_PduName_Object = MibTableColumn
pduName = _PduName_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 1, 2, 1, 3),
    _PduName_Type()
)
pduName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduName.setStatus("current")
_PduOutEn_Type = TruthValue
_PduOutEn_Object = MibTableColumn
pduOutEn = _PduOutEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 1, 2, 1, 4),
    _PduOutEn_Type()
)
pduOutEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutEn.setStatus("current")
_PduMonEn_Type = TruthValue
_PduMonEn_Object = MibTableColumn
pduMonEn = _PduMonEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 1, 2, 1, 5),
    _PduMonEn_Type()
)
pduMonEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMonEn.setStatus("current")


class _PduCommsFail_Type(Integer32):
    """Custom type pduCommsFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("commsGood", 1),
          ("commsFailed", 2),
          ("commsBadData", 3))
    )


_PduCommsFail_Type.__name__ = "Integer32"
_PduCommsFail_Object = MibTableColumn
pduCommsFail = _PduCommsFail_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 1, 2, 1, 6),
    _PduCommsFail_Type()
)
pduCommsFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCommsFail.setStatus("current")


class _PduType_Type(Integer32):
    """Custom type pduType based on Integer32"""
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
              253,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("rs232PduMk1", 1),
          ("rs232PduTpt", 2),
          ("rs485PduTpt", 3),
          ("rs232CLAmp", 4),
          ("rs485CLAmp", 5),
          ("rs232PduMk2", 6),
          ("rs485PduMk2", 7),
          ("rs485PduMk3", 8),
          ("rs232G5", 9),
          ("virtual", 253),
          ("none", 254),
          ("unknown", 255))
    )


_PduType_Type.__name__ = "Integer32"
_PduType_Object = MibTableColumn
pduType = _PduType_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 1, 2, 1, 7),
    _PduType_Type()
)
pduType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduType.setStatus("current")


class _PduMode_Type(Integer32):
    """Custom type pduMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              253,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("singlePhase", 1),
          ("twoPhase", 2),
          ("threePhaseStar", 3),
          ("threePhaseDelta", 4),
          ("aggregate", 253),
          ("none", 254),
          ("unknown", 255))
    )


_PduMode_Type.__name__ = "Integer32"
_PduMode_Object = MibTableColumn
pduMode = _PduMode_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 1, 2, 1, 8),
    _PduMode_Type()
)
pduMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduMode.setStatus("current")
_PduNumControl_Type = Unsigned32
_PduNumControl_Object = MibTableColumn
pduNumControl = _PduNumControl_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 1, 2, 1, 9),
    _PduNumControl_Type()
)
pduNumControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNumControl.setStatus("current")


class _PduOutletMonMode_Type(Integer32):
    """Custom type pduOutletMonMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("currentOnly", 1),
          ("allParameters", 2),
          ("none", 254),
          ("unknown", 255))
    )


_PduOutletMonMode_Type.__name__ = "Integer32"
_PduOutletMonMode_Object = MibTableColumn
pduOutletMonMode = _PduOutletMonMode_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 1, 2, 1, 10),
    _PduOutletMonMode_Type()
)
pduOutletMonMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMonMode.setStatus("current")
_PduNumOutlets_Type = Unsigned32
_PduNumOutlets_Object = MibTableColumn
pduNumOutlets = _PduNumOutlets_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 1, 2, 1, 11),
    _PduNumOutlets_Type()
)
pduNumOutlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNumOutlets.setStatus("current")
_PduFwVersCPU_Type = DisplayString
_PduFwVersCPU_Object = MibTableColumn
pduFwVersCPU = _PduFwVersCPU_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 1, 2, 1, 12),
    _PduFwVersCPU_Type()
)
pduFwVersCPU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduFwVersCPU.setStatus("current")
_PduFwVersMeter_Type = DisplayString
_PduFwVersMeter_Object = MibTableColumn
pduFwVersMeter = _PduFwVersMeter_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 1, 2, 1, 13),
    _PduFwVersMeter_Type()
)
pduFwVersMeter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduFwVersMeter.setStatus("current")


class _PduNumOfCctBrks_Type(Integer32):
    """Custom type pduNumOfCctBrks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_PduNumOfCctBrks_Type.__name__ = "Integer32"
_PduNumOfCctBrks_Object = MibTableColumn
pduNumOfCctBrks = _PduNumOfCctBrks_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 1, 2, 1, 14),
    _PduNumOfCctBrks_Type()
)
pduNumOfCctBrks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNumOfCctBrks.setStatus("current")


class _PdusMinMaxPeriod_Type(Integer32):
    """Custom type pdusMinMaxPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              15,
              30,
              60)
        )
    )
    namedValues = NamedValues(
        *(("periodNull", 0),
          ("period15Minutes", 15),
          ("period30Minutes", 30),
          ("period60Minutes", 60))
    )


_PdusMinMaxPeriod_Type.__name__ = "Integer32"
_PdusMinMaxPeriod_Object = MibScalar
pdusMinMaxPeriod = _PdusMinMaxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 1, 3),
    _PdusMinMaxPeriod_Type()
)
pdusMinMaxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdusMinMaxPeriod.setStatus("current")
_PduOutlets_ObjectIdentity = ObjectIdentity
pduOutlets = _PduOutlets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2)
)
_PduOutAll_ObjectIdentity = ObjectIdentity
pduOutAll = _PduOutAll_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 1)
)


class _PduOutCycleAll_Type(Integer32):
    """Custom type pduOutCycleAll based on Integer32"""
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


_PduOutCycleAll_Type.__name__ = "Integer32"
_PduOutCycleAll_Object = MibScalar
pduOutCycleAll = _PduOutCycleAll_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 1, 1),
    _PduOutCycleAll_Type()
)
pduOutCycleAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutCycleAll.setStatus("current")
_PduOutCycleAllPwd_Type = DisplayString
_PduOutCycleAllPwd_Object = MibScalar
pduOutCycleAllPwd = _PduOutCycleAllPwd_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 1, 2),
    _PduOutCycleAllPwd_Type()
)
pduOutCycleAllPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutCycleAllPwd.setStatus("current")
_PduOutCycleAllAbort_Type = Unsigned32
_PduOutCycleAllAbort_Object = MibScalar
pduOutCycleAllAbort = _PduOutCycleAllAbort_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 1, 3),
    _PduOutCycleAllAbort_Type()
)
pduOutCycleAllAbort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutCycleAllAbort.setStatus("current")


class _PduOutGlobalCycleDelay_Type(Unsigned32):
    """Custom type pduOutGlobalCycleDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_PduOutGlobalCycleDelay_Type.__name__ = "Unsigned32"
_PduOutGlobalCycleDelay_Object = MibScalar
pduOutGlobalCycleDelay = _PduOutGlobalCycleDelay_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 1, 4),
    _PduOutGlobalCycleDelay_Type()
)
pduOutGlobalCycleDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutGlobalCycleDelay.setStatus("current")


class _PduOutGlobalRebootTime_Type(Unsigned32):
    """Custom type pduOutGlobalRebootTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_PduOutGlobalRebootTime_Type.__name__ = "Unsigned32"
_PduOutGlobalRebootTime_Object = MibScalar
pduOutGlobalRebootTime = _PduOutGlobalRebootTime_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 1, 5),
    _PduOutGlobalRebootTime_Type()
)
pduOutGlobalRebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutGlobalRebootTime.setStatus("current")


class _PduOutGlobalCycleAbortTime_Type(Unsigned32):
    """Custom type pduOutGlobalCycleAbortTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_PduOutGlobalCycleAbortTime_Type.__name__ = "Unsigned32"
_PduOutGlobalCycleAbortTime_Object = MibScalar
pduOutGlobalCycleAbortTime = _PduOutGlobalCycleAbortTime_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 1, 6),
    _PduOutGlobalCycleAbortTime_Type()
)
pduOutGlobalCycleAbortTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutGlobalCycleAbortTime.setStatus("current")
_PduOutCmnTable_Object = MibTable
pduOutCmnTable = _PduOutCmnTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 2)
)
if mibBuilder.loadTexts:
    pduOutCmnTable.setStatus("current")
_PduOutCmnEntry_Object = MibTableRow
pduOutCmnEntry = _PduOutCmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 2, 1)
)
pduOutCmnEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "pduOutCmnPduNumber"),
)
if mibBuilder.loadTexts:
    pduOutCmnEntry.setStatus("current")
_PduOutCmnPduNumber_Type = Unsigned32
_PduOutCmnPduNumber_Object = MibTableColumn
pduOutCmnPduNumber = _PduOutCmnPduNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 2, 1, 1),
    _PduOutCmnPduNumber_Type()
)
pduOutCmnPduNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutCmnPduNumber.setStatus("current")
_PduOutCmnRS_Type = RowStatus
_PduOutCmnRS_Object = MibTableColumn
pduOutCmnRS = _PduOutCmnRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 2, 1, 2),
    _PduOutCmnRS_Type()
)
pduOutCmnRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutCmnRS.setStatus("current")
_PduNumOfOutlets_Type = Unsigned32
_PduNumOfOutlets_Object = MibTableColumn
pduNumOfOutlets = _PduNumOfOutlets_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 2, 1, 3),
    _PduNumOfOutlets_Type()
)
pduNumOfOutlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNumOfOutlets.setStatus("current")


class _PduOutCycle_Type(Integer32):
    """Custom type pduOutCycle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("unknown", 255))
    )


_PduOutCycle_Type.__name__ = "Integer32"
_PduOutCycle_Object = MibTableColumn
pduOutCycle = _PduOutCycle_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 2, 1, 4),
    _PduOutCycle_Type()
)
pduOutCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutCycle.setStatus("current")
_PduOutCyclePwd_Type = DisplayString
_PduOutCyclePwd_Object = MibTableColumn
pduOutCyclePwd = _PduOutCyclePwd_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 2, 1, 5),
    _PduOutCyclePwd_Type()
)
pduOutCyclePwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutCyclePwd.setStatus("current")
_PduOutCycleAbortTask_Type = Unsigned32
_PduOutCycleAbortTask_Object = MibTableColumn
pduOutCycleAbortTask = _PduOutCycleAbortTask_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 2, 1, 6),
    _PduOutCycleAbortTask_Type()
)
pduOutCycleAbortTask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutCycleAbortTask.setStatus("current")


class _PduOutCycleAbortTime_Type(Unsigned32):
    """Custom type pduOutCycleAbortTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_PduOutCycleAbortTime_Type.__name__ = "Unsigned32"
_PduOutCycleAbortTime_Object = MibTableColumn
pduOutCycleAbortTime = _PduOutCycleAbortTime_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 2, 1, 7),
    _PduOutCycleAbortTime_Type()
)
pduOutCycleAbortTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutCycleAbortTime.setStatus("current")
_PduOutTable_Object = MibTable
pduOutTable = _PduOutTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 3)
)
if mibBuilder.loadTexts:
    pduOutTable.setStatus("current")
_PduOutEntry_Object = MibTableRow
pduOutEntry = _PduOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 3, 1)
)
pduOutEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "pduOutPduNumber"),
    (0, "HAWK-I2-MIB", "pduOutNumber"),
)
if mibBuilder.loadTexts:
    pduOutEntry.setStatus("current")
_PduOutPduNumber_Type = Unsigned32
_PduOutPduNumber_Object = MibTableColumn
pduOutPduNumber = _PduOutPduNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 3, 1, 1),
    _PduOutPduNumber_Type()
)
pduOutPduNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutPduNumber.setStatus("current")
_PduOutNumber_Type = Unsigned32
_PduOutNumber_Object = MibTableColumn
pduOutNumber = _PduOutNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 3, 1, 2),
    _PduOutNumber_Type()
)
pduOutNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutNumber.setStatus("current")
_PduOutRS_Type = RowStatus
_PduOutRS_Object = MibTableColumn
pduOutRS = _PduOutRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 3, 1, 3),
    _PduOutRS_Type()
)
pduOutRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutRS.setStatus("current")
_PduOutName_Type = DisplayString
_PduOutName_Object = MibTableColumn
pduOutName = _PduOutName_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 3, 1, 4),
    _PduOutName_Type()
)
pduOutName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutName.setStatus("current")


class _PduOutOn_Type(Integer32):
    """Custom type pduOutOn based on Integer32"""
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
        *(("on", 1),
          ("off", 2),
          ("reboot", 3),
          ("unknown", 4),
          ("failedStuck", 5))
    )


_PduOutOn_Type.__name__ = "Integer32"
_PduOutOn_Object = MibTableColumn
pduOutOn = _PduOutOn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 3, 1, 5),
    _PduOutOn_Type()
)
pduOutOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutOn.setStatus("current")
_PduOutPwd_Type = DisplayString
_PduOutPwd_Object = MibTableColumn
pduOutPwd = _PduOutPwd_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 3, 1, 6),
    _PduOutPwd_Type()
)
pduOutPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutPwd.setStatus("current")
_PduOutCycleDelay_Type = Unsigned32
_PduOutCycleDelay_Object = MibTableColumn
pduOutCycleDelay = _PduOutCycleDelay_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 3, 1, 7),
    _PduOutCycleDelay_Type()
)
pduOutCycleDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutCycleDelay.setStatus("current")


class _PduOutRebootPeriod_Type(Unsigned32):
    """Custom type pduOutRebootPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_PduOutRebootPeriod_Type.__name__ = "Unsigned32"
_PduOutRebootPeriod_Object = MibTableColumn
pduOutRebootPeriod = _PduOutRebootPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 3, 1, 8),
    _PduOutRebootPeriod_Type()
)
pduOutRebootPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutRebootPeriod.setStatus("current")
_PduOutRMSAmpsValue_Type = Unsigned32
_PduOutRMSAmpsValue_Object = MibTableColumn
pduOutRMSAmpsValue = _PduOutRMSAmpsValue_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 3, 1, 9),
    _PduOutRMSAmpsValue_Type()
)
pduOutRMSAmpsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutRMSAmpsValue.setStatus("current")
_PduOutRMSAmpsSurge_Type = Unsigned32
_PduOutRMSAmpsSurge_Object = MibTableColumn
pduOutRMSAmpsSurge = _PduOutRMSAmpsSurge_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 3, 1, 10),
    _PduOutRMSAmpsSurge_Type()
)
pduOutRMSAmpsSurge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutRMSAmpsSurge.setStatus("current")
_PduOutRMSAmpsPeak_Type = Unsigned32
_PduOutRMSAmpsPeak_Object = MibTableColumn
pduOutRMSAmpsPeak = _PduOutRMSAmpsPeak_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 3, 1, 11),
    _PduOutRMSAmpsPeak_Type()
)
pduOutRMSAmpsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutRMSAmpsPeak.setStatus("current")
_PduOutRMSAmpsPkRst_Type = Unsigned32
_PduOutRMSAmpsPkRst_Object = MibTableColumn
pduOutRMSAmpsPkRst = _PduOutRMSAmpsPkRst_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 3, 1, 12),
    _PduOutRMSAmpsPkRst_Type()
)
pduOutRMSAmpsPkRst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutRMSAmpsPkRst.setStatus("current")
_PduOutMeanKVAValue_Type = Unsigned32
_PduOutMeanKVAValue_Object = MibTableColumn
pduOutMeanKVAValue = _PduOutMeanKVAValue_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 3, 1, 13),
    _PduOutMeanKVAValue_Type()
)
pduOutMeanKVAValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutMeanKVAValue.setStatus("current")
_PduOutKWHrValue_Type = Unsigned32
_PduOutKWHrValue_Object = MibTableColumn
pduOutKWHrValue = _PduOutKWHrValue_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 3, 1, 14),
    _PduOutKWHrValue_Type()
)
pduOutKWHrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutKWHrValue.setStatus("current")
_PduOutPFactorValue_Type = Unsigned32
_PduOutPFactorValue_Object = MibTableColumn
pduOutPFactorValue = _PduOutPFactorValue_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 3, 1, 15),
    _PduOutPFactorValue_Type()
)
pduOutPFactorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutPFactorValue.setStatus("current")


class _PduOutRMSAmpsUTL_Type(Integer32):
    """Custom type pduOutRMSAmpsUTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 500),
    )


_PduOutRMSAmpsUTL_Type.__name__ = "Integer32"
_PduOutRMSAmpsUTL_Object = MibTableColumn
pduOutRMSAmpsUTL = _PduOutRMSAmpsUTL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 3, 1, 16),
    _PduOutRMSAmpsUTL_Type()
)
pduOutRMSAmpsUTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutRMSAmpsUTL.setStatus("current")


class _PduOutRMSAmpsLTL_Type(Integer32):
    """Custom type pduOutRMSAmpsLTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 500),
    )


_PduOutRMSAmpsLTL_Type.__name__ = "Integer32"
_PduOutRMSAmpsLTL_Object = MibTableColumn
pduOutRMSAmpsLTL = _PduOutRMSAmpsLTL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 3, 1, 17),
    _PduOutRMSAmpsLTL_Type()
)
pduOutRMSAmpsLTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutRMSAmpsLTL.setStatus("current")
_PduOutRMSAmpsUTLTrapEn_Type = TruthValue
_PduOutRMSAmpsUTLTrapEn_Object = MibTableColumn
pduOutRMSAmpsUTLTrapEn = _PduOutRMSAmpsUTLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 3, 1, 18),
    _PduOutRMSAmpsUTLTrapEn_Type()
)
pduOutRMSAmpsUTLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutRMSAmpsUTLTrapEn.setStatus("current")
_PduOutRMSAmpsLTLTrapEn_Type = TruthValue
_PduOutRMSAmpsLTLTrapEn_Object = MibTableColumn
pduOutRMSAmpsLTLTrapEn = _PduOutRMSAmpsLTLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 3, 1, 19),
    _PduOutRMSAmpsLTLTrapEn_Type()
)
pduOutRMSAmpsLTLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutRMSAmpsLTLTrapEn.setStatus("current")


class _PduOutRMSAmpsUTLTrapPer_Type(Unsigned32):
    """Custom type pduOutRMSAmpsUTLTrapPer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PduOutRMSAmpsUTLTrapPer_Type.__name__ = "Unsigned32"
_PduOutRMSAmpsUTLTrapPer_Object = MibTableColumn
pduOutRMSAmpsUTLTrapPer = _PduOutRMSAmpsUTLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 3, 1, 20),
    _PduOutRMSAmpsUTLTrapPer_Type()
)
pduOutRMSAmpsUTLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutRMSAmpsUTLTrapPer.setStatus("current")


class _PduOutRMSAmpsLTLTrapPer_Type(Unsigned32):
    """Custom type pduOutRMSAmpsLTLTrapPer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PduOutRMSAmpsLTLTrapPer_Type.__name__ = "Unsigned32"
_PduOutRMSAmpsLTLTrapPer_Object = MibTableColumn
pduOutRMSAmpsLTLTrapPer = _PduOutRMSAmpsLTLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 3, 1, 21),
    _PduOutRMSAmpsLTLTrapPer_Type()
)
pduOutRMSAmpsLTLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutRMSAmpsLTLTrapPer.setStatus("current")
_PduMonitor_ObjectIdentity = ObjectIdentity
pduMonitor = _PduMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3)
)
_PduMonTable_Object = MibTable
pduMonTable = _PduMonTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1)
)
if mibBuilder.loadTexts:
    pduMonTable.setStatus("current")
_PduMonEntry_Object = MibTableRow
pduMonEntry = _PduMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1)
)
pduMonEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "pduMonPduNumber"),
)
if mibBuilder.loadTexts:
    pduMonEntry.setStatus("current")
_PduMonPduNumber_Type = Unsigned32
_PduMonPduNumber_Object = MibTableColumn
pduMonPduNumber = _PduMonPduNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 1),
    _PduMonPduNumber_Type()
)
pduMonPduNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduMonPduNumber.setStatus("current")
_PduMonRS_Type = RowStatus
_PduMonRS_Object = MibTableColumn
pduMonRS = _PduMonRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 2),
    _PduMonRS_Type()
)
pduMonRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduMonRS.setStatus("current")
_PduRMSVoltsValue_Type = Integer32
_PduRMSVoltsValue_Object = MibTableColumn
pduRMSVoltsValue = _PduRMSVoltsValue_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 3),
    _PduRMSVoltsValue_Type()
)
pduRMSVoltsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduRMSVoltsValue.setStatus("current")
_PduRMSAmpsValue_Type = Integer32
_PduRMSAmpsValue_Object = MibTableColumn
pduRMSAmpsValue = _PduRMSAmpsValue_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 4),
    _PduRMSAmpsValue_Type()
)
pduRMSAmpsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduRMSAmpsValue.setStatus("current")
_PduTotalEnergyValue_Type = Integer32
_PduTotalEnergyValue_Object = MibTableColumn
pduTotalEnergyValue = _PduTotalEnergyValue_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 5),
    _PduTotalEnergyValue_Type()
)
pduTotalEnergyValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduTotalEnergyValue.setStatus("current")
_PduMeanKVAValue_Type = Integer32
_PduMeanKVAValue_Object = MibTableColumn
pduMeanKVAValue = _PduMeanKVAValue_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 6),
    _PduMeanKVAValue_Type()
)
pduMeanKVAValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduMeanKVAValue.setStatus("current")
_PduMeanKWattsValue_Type = Integer32
_PduMeanKWattsValue_Object = MibTableColumn
pduMeanKWattsValue = _PduMeanKWattsValue_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 7),
    _PduMeanKWattsValue_Type()
)
pduMeanKWattsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduMeanKWattsValue.setStatus("current")
_PduPwrFactorValue_Type = Integer32
_PduPwrFactorValue_Object = MibTableColumn
pduPwrFactorValue = _PduPwrFactorValue_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 8),
    _PduPwrFactorValue_Type()
)
pduPwrFactorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPwrFactorValue.setStatus("current")
_PduPwrSupplyFreq_Type = Integer32
_PduPwrSupplyFreq_Object = MibTableColumn
pduPwrSupplyFreq = _PduPwrSupplyFreq_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 9),
    _PduPwrSupplyFreq_Type()
)
pduPwrSupplyFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPwrSupplyFreq.setStatus("current")
_PduPhaseVoltsValue_Type = Integer32
_PduPhaseVoltsValue_Object = MibTableColumn
pduPhaseVoltsValue = _PduPhaseVoltsValue_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 10),
    _PduPhaseVoltsValue_Type()
)
pduPhaseVoltsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPhaseVoltsValue.setStatus("current")
_PduPhaseAmpsValue_Type = Integer32
_PduPhaseAmpsValue_Object = MibTableColumn
pduPhaseAmpsValue = _PduPhaseAmpsValue_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 11),
    _PduPhaseAmpsValue_Type()
)
pduPhaseAmpsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPhaseAmpsValue.setStatus("current")
_PduPhaseEnergyValue_Type = Integer32
_PduPhaseEnergyValue_Object = MibTableColumn
pduPhaseEnergyValue = _PduPhaseEnergyValue_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 12),
    _PduPhaseEnergyValue_Type()
)
pduPhaseEnergyValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPhaseEnergyValue.setStatus("current")
_PduPhaseKVAValue_Type = Integer32
_PduPhaseKVAValue_Object = MibTableColumn
pduPhaseKVAValue = _PduPhaseKVAValue_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 13),
    _PduPhaseKVAValue_Type()
)
pduPhaseKVAValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPhaseKVAValue.setStatus("current")
_PduPhaseKWattsValue_Type = Integer32
_PduPhaseKWattsValue_Object = MibTableColumn
pduPhaseKWattsValue = _PduPhaseKWattsValue_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 14),
    _PduPhaseKWattsValue_Type()
)
pduPhaseKWattsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPhaseKWattsValue.setStatus("current")
_PduPhasePwrFactorValue_Type = Integer32
_PduPhasePwrFactorValue_Object = MibTableColumn
pduPhasePwrFactorValue = _PduPhasePwrFactorValue_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 15),
    _PduPhasePwrFactorValue_Type()
)
pduPhasePwrFactorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPhasePwrFactorValue.setStatus("current")
_PduCircuitName_Type = DisplayString
_PduCircuitName_Object = MibTableColumn
pduCircuitName = _PduCircuitName_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 16),
    _PduCircuitName_Type()
)
pduCircuitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduCircuitName.setStatus("current")
_PduCctKVAMax_Type = Integer32
_PduCctKVAMax_Object = MibTableColumn
pduCctKVAMax = _PduCctKVAMax_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 17),
    _PduCctKVAMax_Type()
)
pduCctKVAMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCctKVAMax.setStatus("current")
_PduCctKVAMaxTime_Type = DisplayString
_PduCctKVAMaxTime_Object = MibTableColumn
pduCctKVAMaxTime = _PduCctKVAMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 18),
    _PduCctKVAMaxTime_Type()
)
pduCctKVAMaxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCctKVAMaxTime.setStatus("current")
_PduCctKVAMin_Type = Integer32
_PduCctKVAMin_Object = MibTableColumn
pduCctKVAMin = _PduCctKVAMin_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 19),
    _PduCctKVAMin_Type()
)
pduCctKVAMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCctKVAMin.setStatus("current")
_PduCctKVAMinTime_Type = DisplayString
_PduCctKVAMinTime_Object = MibTableColumn
pduCctKVAMinTime = _PduCctKVAMinTime_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 20),
    _PduCctKVAMinTime_Type()
)
pduCctKVAMinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCctKVAMinTime.setStatus("current")
_PduCctAmpsMax_Type = Integer32
_PduCctAmpsMax_Object = MibTableColumn
pduCctAmpsMax = _PduCctAmpsMax_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 21),
    _PduCctAmpsMax_Type()
)
pduCctAmpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCctAmpsMax.setStatus("current")
_PduCctAmpsMaxTime_Type = DisplayString
_PduCctAmpsMaxTime_Object = MibTableColumn
pduCctAmpsMaxTime = _PduCctAmpsMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 22),
    _PduCctAmpsMaxTime_Type()
)
pduCctAmpsMaxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCctAmpsMaxTime.setStatus("current")
_PduCctAmpsMin_Type = Integer32
_PduCctAmpsMin_Object = MibTableColumn
pduCctAmpsMin = _PduCctAmpsMin_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 23),
    _PduCctAmpsMin_Type()
)
pduCctAmpsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCctAmpsMin.setStatus("current")
_PduCctAmpsMinTime_Type = DisplayString
_PduCctAmpsMinTime_Object = MibTableColumn
pduCctAmpsMinTime = _PduCctAmpsMinTime_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 24),
    _PduCctAmpsMinTime_Type()
)
pduCctAmpsMinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCctAmpsMinTime.setStatus("current")
_PduCctStatSagSet_Type = TruthValue
_PduCctStatSagSet_Object = MibTableColumn
pduCctStatSagSet = _PduCctStatSagSet_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 25),
    _PduCctStatSagSet_Type()
)
pduCctStatSagSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCctStatSagSet.setStatus("current")
_PduCctStatSagCount_Type = Unsigned32
_PduCctStatSagCount_Object = MibTableColumn
pduCctStatSagCount = _PduCctStatSagCount_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 26),
    _PduCctStatSagCount_Type()
)
pduCctStatSagCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCctStatSagCount.setStatus("current")
_PduCctStatSagTime_Type = DisplayString
_PduCctStatSagTime_Object = MibTableColumn
pduCctStatSagTime = _PduCctStatSagTime_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 27),
    _PduCctStatSagTime_Type()
)
pduCctStatSagTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCctStatSagTime.setStatus("current")
_PduCctStatPkVoltsSet_Type = TruthValue
_PduCctStatPkVoltsSet_Object = MibTableColumn
pduCctStatPkVoltsSet = _PduCctStatPkVoltsSet_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 28),
    _PduCctStatPkVoltsSet_Type()
)
pduCctStatPkVoltsSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCctStatPkVoltsSet.setStatus("current")
_PduCctStatPkVoltsCount_Type = Unsigned32
_PduCctStatPkVoltsCount_Object = MibTableColumn
pduCctStatPkVoltsCount = _PduCctStatPkVoltsCount_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 29),
    _PduCctStatPkVoltsCount_Type()
)
pduCctStatPkVoltsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCctStatPkVoltsCount.setStatus("current")
_PduCctStatPkVoltsTime_Type = DisplayString
_PduCctStatPkVoltsTime_Object = MibTableColumn
pduCctStatPkVoltsTime = _PduCctStatPkVoltsTime_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 30),
    _PduCctStatPkVoltsTime_Type()
)
pduCctStatPkVoltsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCctStatPkVoltsTime.setStatus("current")
_PduCctStatPwrLossSet_Type = TruthValue
_PduCctStatPwrLossSet_Object = MibTableColumn
pduCctStatPwrLossSet = _PduCctStatPwrLossSet_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 31),
    _PduCctStatPwrLossSet_Type()
)
pduCctStatPwrLossSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCctStatPwrLossSet.setStatus("current")
_PduCctStatPwrLossCount_Type = Unsigned32
_PduCctStatPwrLossCount_Object = MibTableColumn
pduCctStatPwrLossCount = _PduCctStatPwrLossCount_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 32),
    _PduCctStatPwrLossCount_Type()
)
pduCctStatPwrLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCctStatPwrLossCount.setStatus("current")
_PduCctStatPwrLossTime_Type = DisplayString
_PduCctStatPwrLossTime_Object = MibTableColumn
pduCctStatPwrLossTime = _PduCctStatPwrLossTime_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 33),
    _PduCctStatPwrLossTime_Type()
)
pduCctStatPwrLossTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCctStatPwrLossTime.setStatus("current")
_PduCctPermKVAMax_Type = Integer32
_PduCctPermKVAMax_Object = MibTableColumn
pduCctPermKVAMax = _PduCctPermKVAMax_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 34),
    _PduCctPermKVAMax_Type()
)
pduCctPermKVAMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCctPermKVAMax.setStatus("current")
_PduCctPermKVAMaxTime_Type = DisplayString
_PduCctPermKVAMaxTime_Object = MibTableColumn
pduCctPermKVAMaxTime = _PduCctPermKVAMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 35),
    _PduCctPermKVAMaxTime_Type()
)
pduCctPermKVAMaxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCctPermKVAMaxTime.setStatus("current")
_PduCctPermAmpsMax_Type = Integer32
_PduCctPermAmpsMax_Object = MibTableColumn
pduCctPermAmpsMax = _PduCctPermAmpsMax_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 36),
    _PduCctPermAmpsMax_Type()
)
pduCctPermAmpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCctPermAmpsMax.setStatus("current")
_PduCctPermAmpsMaxTime_Type = DisplayString
_PduCctPermAmpsMaxTime_Object = MibTableColumn
pduCctPermAmpsMaxTime = _PduCctPermAmpsMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 37),
    _PduCctPermAmpsMaxTime_Type()
)
pduCctPermAmpsMaxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCctPermAmpsMaxTime.setStatus("current")
_PduTrapThreshTable_Object = MibTable
pduTrapThreshTable = _PduTrapThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2)
)
if mibBuilder.loadTexts:
    pduTrapThreshTable.setStatus("current")
_PduTrapThreshEntry_Object = MibTableRow
pduTrapThreshEntry = _PduTrapThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1)
)
pduTrapThreshEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "pduTrapThreshPduNumber"),
)
if mibBuilder.loadTexts:
    pduTrapThreshEntry.setStatus("current")
_PduTrapThreshPduNumber_Type = Unsigned32
_PduTrapThreshPduNumber_Object = MibTableColumn
pduTrapThreshPduNumber = _PduTrapThreshPduNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 1),
    _PduTrapThreshPduNumber_Type()
)
pduTrapThreshPduNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduTrapThreshPduNumber.setStatus("current")
_PduTrapThreshRS_Type = RowStatus
_PduTrapThreshRS_Object = MibTableColumn
pduTrapThreshRS = _PduTrapThreshRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 2),
    _PduTrapThreshRS_Type()
)
pduTrapThreshRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduTrapThreshRS.setStatus("current")


class _PduRMSVoltsUCL_Type(Integer32):
    """Custom type pduRMSVoltsUCL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 500),
    )


_PduRMSVoltsUCL_Type.__name__ = "Integer32"
_PduRMSVoltsUCL_Object = MibTableColumn
pduRMSVoltsUCL = _PduRMSVoltsUCL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 3),
    _PduRMSVoltsUCL_Type()
)
pduRMSVoltsUCL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSVoltsUCL.setStatus("current")


class _PduRMSVoltsUWL_Type(Integer32):
    """Custom type pduRMSVoltsUWL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 500),
    )


_PduRMSVoltsUWL_Type.__name__ = "Integer32"
_PduRMSVoltsUWL_Object = MibTableColumn
pduRMSVoltsUWL = _PduRMSVoltsUWL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 4),
    _PduRMSVoltsUWL_Type()
)
pduRMSVoltsUWL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSVoltsUWL.setStatus("current")


class _PduRMSVoltsLWL_Type(Integer32):
    """Custom type pduRMSVoltsLWL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 500),
    )


_PduRMSVoltsLWL_Type.__name__ = "Integer32"
_PduRMSVoltsLWL_Object = MibTableColumn
pduRMSVoltsLWL = _PduRMSVoltsLWL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 5),
    _PduRMSVoltsLWL_Type()
)
pduRMSVoltsLWL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSVoltsLWL.setStatus("current")


class _PduRMSVoltsLCL_Type(Integer32):
    """Custom type pduRMSVoltsLCL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 500),
    )


_PduRMSVoltsLCL_Type.__name__ = "Integer32"
_PduRMSVoltsLCL_Object = MibTableColumn
pduRMSVoltsLCL = _PduRMSVoltsLCL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 6),
    _PduRMSVoltsLCL_Type()
)
pduRMSVoltsLCL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSVoltsLCL.setStatus("current")


class _PduRMSAmpsUCL_Type(Integer32):
    """Custom type pduRMSAmpsUCL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 5000),
    )


_PduRMSAmpsUCL_Type.__name__ = "Integer32"
_PduRMSAmpsUCL_Object = MibTableColumn
pduRMSAmpsUCL = _PduRMSAmpsUCL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 7),
    _PduRMSAmpsUCL_Type()
)
pduRMSAmpsUCL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSAmpsUCL.setStatus("current")


class _PduRMSAmpsUWL_Type(Integer32):
    """Custom type pduRMSAmpsUWL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 5000),
    )


_PduRMSAmpsUWL_Type.__name__ = "Integer32"
_PduRMSAmpsUWL_Object = MibTableColumn
pduRMSAmpsUWL = _PduRMSAmpsUWL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 8),
    _PduRMSAmpsUWL_Type()
)
pduRMSAmpsUWL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSAmpsUWL.setStatus("current")


class _PduRMSAmpsLWL_Type(Integer32):
    """Custom type pduRMSAmpsLWL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 5000),
    )


_PduRMSAmpsLWL_Type.__name__ = "Integer32"
_PduRMSAmpsLWL_Object = MibTableColumn
pduRMSAmpsLWL = _PduRMSAmpsLWL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 9),
    _PduRMSAmpsLWL_Type()
)
pduRMSAmpsLWL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSAmpsLWL.setStatus("current")


class _PduRMSAmpsLCL_Type(Integer32):
    """Custom type pduRMSAmpsLCL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 5000),
    )


_PduRMSAmpsLCL_Type.__name__ = "Integer32"
_PduRMSAmpsLCL_Object = MibTableColumn
pduRMSAmpsLCL = _PduRMSAmpsLCL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 10),
    _PduRMSAmpsLCL_Type()
)
pduRMSAmpsLCL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSAmpsLCL.setStatus("current")


class _PduEnergyUCL_Type(Unsigned32):
    """Custom type pduEnergyUCL based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967290),
    )


_PduEnergyUCL_Type.__name__ = "Unsigned32"
_PduEnergyUCL_Object = MibTableColumn
pduEnergyUCL = _PduEnergyUCL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 11),
    _PduEnergyUCL_Type()
)
pduEnergyUCL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEnergyUCL.setStatus("current")


class _PduEnergyUWL_Type(Unsigned32):
    """Custom type pduEnergyUWL based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967290),
    )


_PduEnergyUWL_Type.__name__ = "Unsigned32"
_PduEnergyUWL_Object = MibTableColumn
pduEnergyUWL = _PduEnergyUWL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 12),
    _PduEnergyUWL_Type()
)
pduEnergyUWL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEnergyUWL.setStatus("current")


class _PduMeanKVAUCL_Type(Integer32):
    """Custom type pduMeanKVAUCL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999990),
    )


_PduMeanKVAUCL_Type.__name__ = "Integer32"
_PduMeanKVAUCL_Object = MibTableColumn
pduMeanKVAUCL = _PduMeanKVAUCL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 13),
    _PduMeanKVAUCL_Type()
)
pduMeanKVAUCL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKVAUCL.setStatus("current")


class _PduMeanKVAUWL_Type(Integer32):
    """Custom type pduMeanKVAUWL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999990),
    )


_PduMeanKVAUWL_Type.__name__ = "Integer32"
_PduMeanKVAUWL_Object = MibTableColumn
pduMeanKVAUWL = _PduMeanKVAUWL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 14),
    _PduMeanKVAUWL_Type()
)
pduMeanKVAUWL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKVAUWL.setStatus("current")


class _PduMeanKVALWL_Type(Integer32):
    """Custom type pduMeanKVALWL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999990),
    )


_PduMeanKVALWL_Type.__name__ = "Integer32"
_PduMeanKVALWL_Object = MibTableColumn
pduMeanKVALWL = _PduMeanKVALWL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 15),
    _PduMeanKVALWL_Type()
)
pduMeanKVALWL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKVALWL.setStatus("current")


class _PduMeanKVALCL_Type(Integer32):
    """Custom type pduMeanKVALCL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999990),
    )


_PduMeanKVALCL_Type.__name__ = "Integer32"
_PduMeanKVALCL_Object = MibTableColumn
pduMeanKVALCL = _PduMeanKVALCL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 16),
    _PduMeanKVALCL_Type()
)
pduMeanKVALCL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKVALCL.setStatus("current")


class _PduMeanKWattsUCL_Type(Integer32):
    """Custom type pduMeanKWattsUCL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_PduMeanKWattsUCL_Type.__name__ = "Integer32"
_PduMeanKWattsUCL_Object = MibTableColumn
pduMeanKWattsUCL = _PduMeanKWattsUCL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 17),
    _PduMeanKWattsUCL_Type()
)
pduMeanKWattsUCL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKWattsUCL.setStatus("current")


class _PduMeanKWattsUWL_Type(Integer32):
    """Custom type pduMeanKWattsUWL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_PduMeanKWattsUWL_Type.__name__ = "Integer32"
_PduMeanKWattsUWL_Object = MibTableColumn
pduMeanKWattsUWL = _PduMeanKWattsUWL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 18),
    _PduMeanKWattsUWL_Type()
)
pduMeanKWattsUWL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKWattsUWL.setStatus("current")


class _PduMeanKWattsLWL_Type(Integer32):
    """Custom type pduMeanKWattsLWL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_PduMeanKWattsLWL_Type.__name__ = "Integer32"
_PduMeanKWattsLWL_Object = MibTableColumn
pduMeanKWattsLWL = _PduMeanKWattsLWL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 19),
    _PduMeanKWattsLWL_Type()
)
pduMeanKWattsLWL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKWattsLWL.setStatus("current")


class _PduMeanKWattsLCL_Type(Integer32):
    """Custom type pduMeanKWattsLCL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_PduMeanKWattsLCL_Type.__name__ = "Integer32"
_PduMeanKWattsLCL_Object = MibTableColumn
pduMeanKWattsLCL = _PduMeanKWattsLCL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 20),
    _PduMeanKWattsLCL_Type()
)
pduMeanKWattsLCL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKWattsLCL.setStatus("current")


class _PduPwrFactorUTL_Type(Integer32):
    """Custom type pduPwrFactorUTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PduPwrFactorUTL_Type.__name__ = "Integer32"
_PduPwrFactorUTL_Object = MibTableColumn
pduPwrFactorUTL = _PduPwrFactorUTL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 21),
    _PduPwrFactorUTL_Type()
)
pduPwrFactorUTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduPwrFactorUTL.setStatus("current")


class _PduPwrFactorLTL_Type(Integer32):
    """Custom type pduPwrFactorLTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PduPwrFactorLTL_Type.__name__ = "Integer32"
_PduPwrFactorLTL_Object = MibTableColumn
pduPwrFactorLTL = _PduPwrFactorLTL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 22),
    _PduPwrFactorLTL_Type()
)
pduPwrFactorLTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduPwrFactorLTL.setStatus("current")
_PduTrapEnTable_Object = MibTable
pduTrapEnTable = _PduTrapEnTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3)
)
if mibBuilder.loadTexts:
    pduTrapEnTable.setStatus("current")
_PduTrapEnEntry_Object = MibTableRow
pduTrapEnEntry = _PduTrapEnEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1)
)
pduTrapEnEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "pduTrapEnPduNumber"),
)
if mibBuilder.loadTexts:
    pduTrapEnEntry.setStatus("current")
_PduTrapEnPduNumber_Type = Unsigned32
_PduTrapEnPduNumber_Object = MibTableColumn
pduTrapEnPduNumber = _PduTrapEnPduNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 1),
    _PduTrapEnPduNumber_Type()
)
pduTrapEnPduNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduTrapEnPduNumber.setStatus("current")
_PduTrapEnRS_Type = RowStatus
_PduTrapEnRS_Object = MibTableColumn
pduTrapEnRS = _PduTrapEnRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 2),
    _PduTrapEnRS_Type()
)
pduTrapEnRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduTrapEnRS.setStatus("current")
_PduRMSVoltsUCLTrapEn_Type = TruthValue
_PduRMSVoltsUCLTrapEn_Object = MibTableColumn
pduRMSVoltsUCLTrapEn = _PduRMSVoltsUCLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 3),
    _PduRMSVoltsUCLTrapEn_Type()
)
pduRMSVoltsUCLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSVoltsUCLTrapEn.setStatus("current")
_PduRMSVoltsUWLTrapEn_Type = TruthValue
_PduRMSVoltsUWLTrapEn_Object = MibTableColumn
pduRMSVoltsUWLTrapEn = _PduRMSVoltsUWLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 4),
    _PduRMSVoltsUWLTrapEn_Type()
)
pduRMSVoltsUWLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSVoltsUWLTrapEn.setStatus("current")
_PduRMSVoltsLWLTrapEn_Type = TruthValue
_PduRMSVoltsLWLTrapEn_Object = MibTableColumn
pduRMSVoltsLWLTrapEn = _PduRMSVoltsLWLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 5),
    _PduRMSVoltsLWLTrapEn_Type()
)
pduRMSVoltsLWLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSVoltsLWLTrapEn.setStatus("current")
_PduRMSVoltsLCLTrapEn_Type = TruthValue
_PduRMSVoltsLCLTrapEn_Object = MibTableColumn
pduRMSVoltsLCLTrapEn = _PduRMSVoltsLCLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 6),
    _PduRMSVoltsLCLTrapEn_Type()
)
pduRMSVoltsLCLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSVoltsLCLTrapEn.setStatus("current")
_PduRMSAmpsUCLTrapEn_Type = TruthValue
_PduRMSAmpsUCLTrapEn_Object = MibTableColumn
pduRMSAmpsUCLTrapEn = _PduRMSAmpsUCLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 7),
    _PduRMSAmpsUCLTrapEn_Type()
)
pduRMSAmpsUCLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSAmpsUCLTrapEn.setStatus("current")
_PduRMSAmpsUWLTrapEn_Type = TruthValue
_PduRMSAmpsUWLTrapEn_Object = MibTableColumn
pduRMSAmpsUWLTrapEn = _PduRMSAmpsUWLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 8),
    _PduRMSAmpsUWLTrapEn_Type()
)
pduRMSAmpsUWLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSAmpsUWLTrapEn.setStatus("current")
_PduRMSAmpsLWLTrapEn_Type = TruthValue
_PduRMSAmpsLWLTrapEn_Object = MibTableColumn
pduRMSAmpsLWLTrapEn = _PduRMSAmpsLWLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 9),
    _PduRMSAmpsLWLTrapEn_Type()
)
pduRMSAmpsLWLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSAmpsLWLTrapEn.setStatus("current")
_PduRMSAmpsLCLTrapEn_Type = TruthValue
_PduRMSAmpsLCLTrapEn_Object = MibTableColumn
pduRMSAmpsLCLTrapEn = _PduRMSAmpsLCLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 10),
    _PduRMSAmpsLCLTrapEn_Type()
)
pduRMSAmpsLCLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSAmpsLCLTrapEn.setStatus("current")
_PduEnergyUCLTrapEn_Type = TruthValue
_PduEnergyUCLTrapEn_Object = MibTableColumn
pduEnergyUCLTrapEn = _PduEnergyUCLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 11),
    _PduEnergyUCLTrapEn_Type()
)
pduEnergyUCLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEnergyUCLTrapEn.setStatus("current")
_PduEnergyUWLTrapEn_Type = TruthValue
_PduEnergyUWLTrapEn_Object = MibTableColumn
pduEnergyUWLTrapEn = _PduEnergyUWLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 12),
    _PduEnergyUWLTrapEn_Type()
)
pduEnergyUWLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEnergyUWLTrapEn.setStatus("current")
_PduMeanKVAUCLTrapEn_Type = TruthValue
_PduMeanKVAUCLTrapEn_Object = MibTableColumn
pduMeanKVAUCLTrapEn = _PduMeanKVAUCLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 13),
    _PduMeanKVAUCLTrapEn_Type()
)
pduMeanKVAUCLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKVAUCLTrapEn.setStatus("current")
_PduMeanKVAUWLTrapEn_Type = TruthValue
_PduMeanKVAUWLTrapEn_Object = MibTableColumn
pduMeanKVAUWLTrapEn = _PduMeanKVAUWLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 14),
    _PduMeanKVAUWLTrapEn_Type()
)
pduMeanKVAUWLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKVAUWLTrapEn.setStatus("current")
_PduMeanKVALWLTrapEn_Type = TruthValue
_PduMeanKVALWLTrapEn_Object = MibTableColumn
pduMeanKVALWLTrapEn = _PduMeanKVALWLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 15),
    _PduMeanKVALWLTrapEn_Type()
)
pduMeanKVALWLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKVALWLTrapEn.setStatus("current")
_PduMeanKVALCLTrapEn_Type = TruthValue
_PduMeanKVALCLTrapEn_Object = MibTableColumn
pduMeanKVALCLTrapEn = _PduMeanKVALCLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 16),
    _PduMeanKVALCLTrapEn_Type()
)
pduMeanKVALCLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKVALCLTrapEn.setStatus("current")
_PduMeanKWattsUCLTrapEn_Type = TruthValue
_PduMeanKWattsUCLTrapEn_Object = MibTableColumn
pduMeanKWattsUCLTrapEn = _PduMeanKWattsUCLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 17),
    _PduMeanKWattsUCLTrapEn_Type()
)
pduMeanKWattsUCLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKWattsUCLTrapEn.setStatus("current")
_PduMeanKWattsUWLTrapEn_Type = TruthValue
_PduMeanKWattsUWLTrapEn_Object = MibTableColumn
pduMeanKWattsUWLTrapEn = _PduMeanKWattsUWLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 18),
    _PduMeanKWattsUWLTrapEn_Type()
)
pduMeanKWattsUWLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKWattsUWLTrapEn.setStatus("current")
_PduMeanKWattsLWLTrapEn_Type = TruthValue
_PduMeanKWattsLWLTrapEn_Object = MibTableColumn
pduMeanKWattsLWLTrapEn = _PduMeanKWattsLWLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 19),
    _PduMeanKWattsLWLTrapEn_Type()
)
pduMeanKWattsLWLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKWattsLWLTrapEn.setStatus("current")
_PduMeanKWattsLCLTrapEn_Type = TruthValue
_PduMeanKWattsLCLTrapEn_Object = MibTableColumn
pduMeanKWattsLCLTrapEn = _PduMeanKWattsLCLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 20),
    _PduMeanKWattsLCLTrapEn_Type()
)
pduMeanKWattsLCLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKWattsLCLTrapEn.setStatus("current")
_PduPwrFactorUTLTrapEn_Type = TruthValue
_PduPwrFactorUTLTrapEn_Object = MibTableColumn
pduPwrFactorUTLTrapEn = _PduPwrFactorUTLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 21),
    _PduPwrFactorUTLTrapEn_Type()
)
pduPwrFactorUTLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduPwrFactorUTLTrapEn.setStatus("current")
_PduPwrFactorLTLTrapEn_Type = TruthValue
_PduPwrFactorLTLTrapEn_Object = MibTableColumn
pduPwrFactorLTLTrapEn = _PduPwrFactorLTLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 22),
    _PduPwrFactorLTLTrapEn_Type()
)
pduPwrFactorLTLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduPwrFactorLTLTrapEn.setStatus("current")
_PduTrapPerTable_Object = MibTable
pduTrapPerTable = _PduTrapPerTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4)
)
if mibBuilder.loadTexts:
    pduTrapPerTable.setStatus("current")
_PduTrapPerEntry_Object = MibTableRow
pduTrapPerEntry = _PduTrapPerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1)
)
pduTrapPerEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "pduTrapPduNumber"),
)
if mibBuilder.loadTexts:
    pduTrapPerEntry.setStatus("current")
_PduTrapPduNumber_Type = Unsigned32
_PduTrapPduNumber_Object = MibTableColumn
pduTrapPduNumber = _PduTrapPduNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 1),
    _PduTrapPduNumber_Type()
)
pduTrapPduNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduTrapPduNumber.setStatus("current")
_PduTrapPerRS_Type = RowStatus
_PduTrapPerRS_Object = MibTableColumn
pduTrapPerRS = _PduTrapPerRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 2),
    _PduTrapPerRS_Type()
)
pduTrapPerRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduTrapPerRS.setStatus("current")


class _PduRMSVoltsUCLTrapPer_Type(Unsigned32):
    """Custom type pduRMSVoltsUCLTrapPer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PduRMSVoltsUCLTrapPer_Type.__name__ = "Unsigned32"
_PduRMSVoltsUCLTrapPer_Object = MibTableColumn
pduRMSVoltsUCLTrapPer = _PduRMSVoltsUCLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 3),
    _PduRMSVoltsUCLTrapPer_Type()
)
pduRMSVoltsUCLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSVoltsUCLTrapPer.setStatus("current")


class _PduRMSVoltsUWLTrapPer_Type(Unsigned32):
    """Custom type pduRMSVoltsUWLTrapPer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PduRMSVoltsUWLTrapPer_Type.__name__ = "Unsigned32"
_PduRMSVoltsUWLTrapPer_Object = MibTableColumn
pduRMSVoltsUWLTrapPer = _PduRMSVoltsUWLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 4),
    _PduRMSVoltsUWLTrapPer_Type()
)
pduRMSVoltsUWLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSVoltsUWLTrapPer.setStatus("current")


class _PduRMSVoltsLWLTrapPer_Type(Unsigned32):
    """Custom type pduRMSVoltsLWLTrapPer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PduRMSVoltsLWLTrapPer_Type.__name__ = "Unsigned32"
_PduRMSVoltsLWLTrapPer_Object = MibTableColumn
pduRMSVoltsLWLTrapPer = _PduRMSVoltsLWLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 5),
    _PduRMSVoltsLWLTrapPer_Type()
)
pduRMSVoltsLWLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSVoltsLWLTrapPer.setStatus("current")


class _PduRMSVoltsLCLTrapPer_Type(Unsigned32):
    """Custom type pduRMSVoltsLCLTrapPer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PduRMSVoltsLCLTrapPer_Type.__name__ = "Unsigned32"
_PduRMSVoltsLCLTrapPer_Object = MibTableColumn
pduRMSVoltsLCLTrapPer = _PduRMSVoltsLCLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 6),
    _PduRMSVoltsLCLTrapPer_Type()
)
pduRMSVoltsLCLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSVoltsLCLTrapPer.setStatus("current")


class _PduRMSAmpsUCLTrapPer_Type(Unsigned32):
    """Custom type pduRMSAmpsUCLTrapPer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PduRMSAmpsUCLTrapPer_Type.__name__ = "Unsigned32"
_PduRMSAmpsUCLTrapPer_Object = MibTableColumn
pduRMSAmpsUCLTrapPer = _PduRMSAmpsUCLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 7),
    _PduRMSAmpsUCLTrapPer_Type()
)
pduRMSAmpsUCLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSAmpsUCLTrapPer.setStatus("current")


class _PduRMSAmpsUWLTrapPer_Type(Unsigned32):
    """Custom type pduRMSAmpsUWLTrapPer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PduRMSAmpsUWLTrapPer_Type.__name__ = "Unsigned32"
_PduRMSAmpsUWLTrapPer_Object = MibTableColumn
pduRMSAmpsUWLTrapPer = _PduRMSAmpsUWLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 8),
    _PduRMSAmpsUWLTrapPer_Type()
)
pduRMSAmpsUWLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSAmpsUWLTrapPer.setStatus("current")


class _PduRMSAmpsLWLTrapPer_Type(Unsigned32):
    """Custom type pduRMSAmpsLWLTrapPer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PduRMSAmpsLWLTrapPer_Type.__name__ = "Unsigned32"
_PduRMSAmpsLWLTrapPer_Object = MibTableColumn
pduRMSAmpsLWLTrapPer = _PduRMSAmpsLWLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 9),
    _PduRMSAmpsLWLTrapPer_Type()
)
pduRMSAmpsLWLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSAmpsLWLTrapPer.setStatus("current")


class _PduRMSAmpsLCLTrapPer_Type(Unsigned32):
    """Custom type pduRMSAmpsLCLTrapPer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PduRMSAmpsLCLTrapPer_Type.__name__ = "Unsigned32"
_PduRMSAmpsLCLTrapPer_Object = MibTableColumn
pduRMSAmpsLCLTrapPer = _PduRMSAmpsLCLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 10),
    _PduRMSAmpsLCLTrapPer_Type()
)
pduRMSAmpsLCLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSAmpsLCLTrapPer.setStatus("current")


class _PduEnergyUCLTrapPer_Type(Unsigned32):
    """Custom type pduEnergyUCLTrapPer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PduEnergyUCLTrapPer_Type.__name__ = "Unsigned32"
_PduEnergyUCLTrapPer_Object = MibTableColumn
pduEnergyUCLTrapPer = _PduEnergyUCLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 11),
    _PduEnergyUCLTrapPer_Type()
)
pduEnergyUCLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEnergyUCLTrapPer.setStatus("current")


class _PduEnergyUWLTrapPer_Type(Unsigned32):
    """Custom type pduEnergyUWLTrapPer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PduEnergyUWLTrapPer_Type.__name__ = "Unsigned32"
_PduEnergyUWLTrapPer_Object = MibTableColumn
pduEnergyUWLTrapPer = _PduEnergyUWLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 12),
    _PduEnergyUWLTrapPer_Type()
)
pduEnergyUWLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEnergyUWLTrapPer.setStatus("current")


class _PduMeanKVAUCLTrapPer_Type(Unsigned32):
    """Custom type pduMeanKVAUCLTrapPer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PduMeanKVAUCLTrapPer_Type.__name__ = "Unsigned32"
_PduMeanKVAUCLTrapPer_Object = MibTableColumn
pduMeanKVAUCLTrapPer = _PduMeanKVAUCLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 13),
    _PduMeanKVAUCLTrapPer_Type()
)
pduMeanKVAUCLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKVAUCLTrapPer.setStatus("current")


class _PduMeanKVAUWLTrapPer_Type(Unsigned32):
    """Custom type pduMeanKVAUWLTrapPer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PduMeanKVAUWLTrapPer_Type.__name__ = "Unsigned32"
_PduMeanKVAUWLTrapPer_Object = MibTableColumn
pduMeanKVAUWLTrapPer = _PduMeanKVAUWLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 14),
    _PduMeanKVAUWLTrapPer_Type()
)
pduMeanKVAUWLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKVAUWLTrapPer.setStatus("current")


class _PduMeanKVALWLTrapPer_Type(Unsigned32):
    """Custom type pduMeanKVALWLTrapPer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PduMeanKVALWLTrapPer_Type.__name__ = "Unsigned32"
_PduMeanKVALWLTrapPer_Object = MibTableColumn
pduMeanKVALWLTrapPer = _PduMeanKVALWLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 15),
    _PduMeanKVALWLTrapPer_Type()
)
pduMeanKVALWLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKVALWLTrapPer.setStatus("current")


class _PduMeanKVALCLTrapPer_Type(Unsigned32):
    """Custom type pduMeanKVALCLTrapPer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PduMeanKVALCLTrapPer_Type.__name__ = "Unsigned32"
_PduMeanKVALCLTrapPer_Object = MibTableColumn
pduMeanKVALCLTrapPer = _PduMeanKVALCLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 16),
    _PduMeanKVALCLTrapPer_Type()
)
pduMeanKVALCLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKVALCLTrapPer.setStatus("current")


class _PduMeanKWattsUCLTrapPer_Type(Unsigned32):
    """Custom type pduMeanKWattsUCLTrapPer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PduMeanKWattsUCLTrapPer_Type.__name__ = "Unsigned32"
_PduMeanKWattsUCLTrapPer_Object = MibTableColumn
pduMeanKWattsUCLTrapPer = _PduMeanKWattsUCLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 17),
    _PduMeanKWattsUCLTrapPer_Type()
)
pduMeanKWattsUCLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKWattsUCLTrapPer.setStatus("current")


class _PduMeanKWattsUWLTrapPer_Type(Unsigned32):
    """Custom type pduMeanKWattsUWLTrapPer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PduMeanKWattsUWLTrapPer_Type.__name__ = "Unsigned32"
_PduMeanKWattsUWLTrapPer_Object = MibTableColumn
pduMeanKWattsUWLTrapPer = _PduMeanKWattsUWLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 18),
    _PduMeanKWattsUWLTrapPer_Type()
)
pduMeanKWattsUWLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKWattsUWLTrapPer.setStatus("current")


class _PduMeanKWattsLWLTrapPer_Type(Unsigned32):
    """Custom type pduMeanKWattsLWLTrapPer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PduMeanKWattsLWLTrapPer_Type.__name__ = "Unsigned32"
_PduMeanKWattsLWLTrapPer_Object = MibTableColumn
pduMeanKWattsLWLTrapPer = _PduMeanKWattsLWLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 19),
    _PduMeanKWattsLWLTrapPer_Type()
)
pduMeanKWattsLWLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKWattsLWLTrapPer.setStatus("current")


class _PduMeanKWattsLCLTrapPer_Type(Unsigned32):
    """Custom type pduMeanKWattsLCLTrapPer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PduMeanKWattsLCLTrapPer_Type.__name__ = "Unsigned32"
_PduMeanKWattsLCLTrapPer_Object = MibTableColumn
pduMeanKWattsLCLTrapPer = _PduMeanKWattsLCLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 20),
    _PduMeanKWattsLCLTrapPer_Type()
)
pduMeanKWattsLCLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKWattsLCLTrapPer.setStatus("current")


class _PduPwrFactorUTLTrapPer_Type(Unsigned32):
    """Custom type pduPwrFactorUTLTrapPer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PduPwrFactorUTLTrapPer_Type.__name__ = "Unsigned32"
_PduPwrFactorUTLTrapPer_Object = MibTableColumn
pduPwrFactorUTLTrapPer = _PduPwrFactorUTLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 21),
    _PduPwrFactorUTLTrapPer_Type()
)
pduPwrFactorUTLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduPwrFactorUTLTrapPer.setStatus("current")


class _PduPwrFactorLTLTrapPer_Type(Unsigned32):
    """Custom type pduPwrFactorLTLTrapPer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PduPwrFactorLTLTrapPer_Type.__name__ = "Unsigned32"
_PduPwrFactorLTLTrapPer_Object = MibTableColumn
pduPwrFactorLTLTrapPer = _PduPwrFactorLTLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 22),
    _PduPwrFactorLTLTrapPer_Type()
)
pduPwrFactorLTLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduPwrFactorLTLTrapPer.setStatus("current")
_PduMon3PhTable_Object = MibTable
pduMon3PhTable = _PduMon3PhTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 5)
)
if mibBuilder.loadTexts:
    pduMon3PhTable.setStatus("current")
_PduMon3PhEntry_Object = MibTableRow
pduMon3PhEntry = _PduMon3PhEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 5, 1)
)
pduMon3PhEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "pdu3PhPduNumber"),
)
if mibBuilder.loadTexts:
    pduMon3PhEntry.setStatus("current")
_Pdu3PhPduNumber_Type = Unsigned32
_Pdu3PhPduNumber_Object = MibTableColumn
pdu3PhPduNumber = _Pdu3PhPduNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 5, 1, 1),
    _Pdu3PhPduNumber_Type()
)
pdu3PhPduNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3PhPduNumber.setStatus("current")
_Pdu3PhRS_Type = RowStatus
_Pdu3PhRS_Object = MibTableColumn
pdu3PhRS = _Pdu3PhRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 5, 1, 2),
    _Pdu3PhRS_Type()
)
pdu3PhRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3PhRS.setStatus("current")


class _Pdu3PhMode_Type(Integer32):
    """Custom type pdu3PhMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              253,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("star", 1),
          ("delta", 2),
          ("aggregate", 253),
          ("none", 254),
          ("unknown", 255))
    )


_Pdu3PhMode_Type.__name__ = "Integer32"
_Pdu3PhMode_Object = MibTableColumn
pdu3PhMode = _Pdu3PhMode_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 5, 1, 3),
    _Pdu3PhMode_Type()
)
pdu3PhMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3PhMode.setStatus("current")
_Pdu3PhVoltsC1_Type = Integer32
_Pdu3PhVoltsC1_Object = MibTableColumn
pdu3PhVoltsC1 = _Pdu3PhVoltsC1_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 5, 1, 4),
    _Pdu3PhVoltsC1_Type()
)
pdu3PhVoltsC1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3PhVoltsC1.setStatus("current")
_Pdu3PhAmpsL1_Type = Integer32
_Pdu3PhAmpsL1_Object = MibTableColumn
pdu3PhAmpsL1 = _Pdu3PhAmpsL1_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 5, 1, 5),
    _Pdu3PhAmpsL1_Type()
)
pdu3PhAmpsL1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3PhAmpsL1.setStatus("current")
_Pdu3PhVoltsC2_Type = Integer32
_Pdu3PhVoltsC2_Object = MibTableColumn
pdu3PhVoltsC2 = _Pdu3PhVoltsC2_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 5, 1, 6),
    _Pdu3PhVoltsC2_Type()
)
pdu3PhVoltsC2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3PhVoltsC2.setStatus("current")
_Pdu3PhAmpsL2_Type = Integer32
_Pdu3PhAmpsL2_Object = MibTableColumn
pdu3PhAmpsL2 = _Pdu3PhAmpsL2_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 5, 1, 7),
    _Pdu3PhAmpsL2_Type()
)
pdu3PhAmpsL2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3PhAmpsL2.setStatus("current")
_Pdu3PhVoltsC3_Type = Integer32
_Pdu3PhVoltsC3_Object = MibTableColumn
pdu3PhVoltsC3 = _Pdu3PhVoltsC3_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 5, 1, 8),
    _Pdu3PhVoltsC3_Type()
)
pdu3PhVoltsC3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3PhVoltsC3.setStatus("current")
_Pdu3PhAmpsL3_Type = Integer32
_Pdu3PhAmpsL3_Object = MibTableColumn
pdu3PhAmpsL3 = _Pdu3PhAmpsL3_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 5, 1, 9),
    _Pdu3PhAmpsL3_Type()
)
pdu3PhAmpsL3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3PhAmpsL3.setStatus("current")
_Pdu3PhAmpsAgg_Type = Integer32
_Pdu3PhAmpsAgg_Object = MibTableColumn
pdu3PhAmpsAgg = _Pdu3PhAmpsAgg_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 5, 1, 10),
    _Pdu3PhAmpsAgg_Type()
)
pdu3PhAmpsAgg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3PhAmpsAgg.setStatus("current")
_Pdu3PhkVAAgg_Type = Integer32
_Pdu3PhkVAAgg_Object = MibTableColumn
pdu3PhkVAAgg = _Pdu3PhkVAAgg_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 5, 1, 11),
    _Pdu3PhkVAAgg_Type()
)
pdu3PhkVAAgg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3PhkVAAgg.setStatus("current")
_Pdu3PhkWAgg_Type = Integer32
_Pdu3PhkWAgg_Object = MibTableColumn
pdu3PhkWAgg = _Pdu3PhkWAgg_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 5, 1, 12),
    _Pdu3PhkWAgg_Type()
)
pdu3PhkWAgg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3PhkWAgg.setStatus("current")
_Pdu3PhkVArhAgg_Type = Unsigned32
_Pdu3PhkVArhAgg_Object = MibTableColumn
pdu3PhkVArhAgg = _Pdu3PhkVArhAgg_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 5, 1, 13),
    _Pdu3PhkVArhAgg_Type()
)
pdu3PhkVArhAgg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3PhkVArhAgg.setStatus("current")
_Pdu3PhkWhAgg_Type = Unsigned32
_Pdu3PhkWhAgg_Object = MibTableColumn
pdu3PhkWhAgg = _Pdu3PhkWhAgg_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 5, 1, 14),
    _Pdu3PhkWhAgg_Type()
)
pdu3PhkWhAgg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3PhkWhAgg.setStatus("current")
_PduGangs_ObjectIdentity = ObjectIdentity
pduGangs = _PduGangs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 4)
)
_PduGangsEnable_ObjectIdentity = ObjectIdentity
pduGangsEnable = _PduGangsEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 4, 1)
)


class _PduGangsSelect_Type(Integer32):
    """Custom type pduGangsSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_PduGangsSelect_Type.__name__ = "Integer32"
_PduGangsSelect_Object = MibScalar
pduGangsSelect = _PduGangsSelect_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 4, 1, 1),
    _PduGangsSelect_Type()
)
pduGangsSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduGangsSelect.setStatus("current")
_PduGangsInsert_Type = EnableState
_PduGangsInsert_Object = MibScalar
pduGangsInsert = _PduGangsInsert_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 4, 1, 2),
    _PduGangsInsert_Type()
)
pduGangsInsert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduGangsInsert.setStatus("current")
_PduGangTable_Object = MibTable
pduGangTable = _PduGangTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 4, 2)
)
if mibBuilder.loadTexts:
    pduGangTable.setStatus("current")
_PduGangEntry_Object = MibTableRow
pduGangEntry = _PduGangEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 4, 2, 1)
)
pduGangEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "pduGangNumber"),
)
if mibBuilder.loadTexts:
    pduGangEntry.setStatus("current")


class _PduGangNumber_Type(Integer32):
    """Custom type pduGangNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_PduGangNumber_Type.__name__ = "Integer32"
_PduGangNumber_Object = MibTableColumn
pduGangNumber = _PduGangNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 4, 2, 1, 1),
    _PduGangNumber_Type()
)
pduGangNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduGangNumber.setStatus("current")
_PduGangRS_Type = RowStatus
_PduGangRS_Object = MibTableColumn
pduGangRS = _PduGangRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 4, 2, 1, 2),
    _PduGangRS_Type()
)
pduGangRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduGangRS.setStatus("current")


class _PduGangEn_Type(Integer32):
    """Custom type pduGangEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("suspended", 3))
    )


_PduGangEn_Type.__name__ = "Integer32"
_PduGangEn_Object = MibTableColumn
pduGangEn = _PduGangEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 4, 2, 1, 3),
    _PduGangEn_Type()
)
pduGangEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduGangEn.setStatus("current")


class _PduGangName_Type(DisplayString):
    """Custom type pduGangName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PduGangName_Type.__name__ = "DisplayString"
_PduGangName_Object = MibTableColumn
pduGangName = _PduGangName_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 4, 2, 1, 4),
    _PduGangName_Type()
)
pduGangName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduGangName.setStatus("current")


class _PduGangOn_Type(Integer32):
    """Custom type pduGangOn based on Integer32"""
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
        *(("on", 1),
          ("off", 2),
          ("mixed", 3),
          ("reboot", 4),
          ("na", 5))
    )


_PduGangOn_Type.__name__ = "Integer32"
_PduGangOn_Object = MibTableColumn
pduGangOn = _PduGangOn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 4, 2, 1, 5),
    _PduGangOn_Type()
)
pduGangOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduGangOn.setStatus("current")


class _PduGangPassword_Type(DisplayString):
    """Custom type pduGangPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PduGangPassword_Type.__name__ = "DisplayString"
_PduGangPassword_Object = MibTableColumn
pduGangPassword = _PduGangPassword_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 4, 2, 1, 6),
    _PduGangPassword_Type()
)
pduGangPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduGangPassword.setStatus("current")
_PduGangAbortTask_Type = Unsigned32
_PduGangAbortTask_Object = MibTableColumn
pduGangAbortTask = _PduGangAbortTask_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 4, 2, 1, 7),
    _PduGangAbortTask_Type()
)
pduGangAbortTask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduGangAbortTask.setStatus("current")


class _PduGangMembers_Type(DisplayString):
    """Custom type pduGangMembers based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 37),
    )


_PduGangMembers_Type.__name__ = "DisplayString"
_PduGangMembers_Object = MibTableColumn
pduGangMembers = _PduGangMembers_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 4, 2, 1, 8),
    _PduGangMembers_Type()
)
pduGangMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduGangMembers.setStatus("current")
_Expansion_ObjectIdentity = ObjectIdentity
expansion = _Expansion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 8)
)
_ExpEnable_ObjectIdentity = ObjectIdentity
expEnable = _ExpEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 8, 1)
)


class _ExpSelect_Type(Integer32):
    """Custom type expSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExpSelect_Type.__name__ = "Integer32"
_ExpSelect_Object = MibScalar
expSelect = _ExpSelect_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 8, 1, 1),
    _ExpSelect_Type()
)
expSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expSelect.setStatus("current")
_ExpInsert_Type = ExternalUnitType
_ExpInsert_Object = MibScalar
expInsert = _ExpInsert_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 8, 1, 2),
    _ExpInsert_Type()
)
expInsert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expInsert.setStatus("current")
_ExpTable_Object = MibTable
expTable = _ExpTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 8, 2)
)
if mibBuilder.loadTexts:
    expTable.setStatus("current")
_ExpEntry_Object = MibTableRow
expEntry = _ExpEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 8, 2, 1)
)
expEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "expNumber"),
)
if mibBuilder.loadTexts:
    expEntry.setStatus("current")


class _ExpNumber_Type(Integer32):
    """Custom type expNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ExpNumber_Type.__name__ = "Integer32"
_ExpNumber_Object = MibTableColumn
expNumber = _ExpNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 8, 2, 1, 1),
    _ExpNumber_Type()
)
expNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expNumber.setStatus("current")
_ExpRS_Type = RowStatus
_ExpRS_Object = MibTableColumn
expRS = _ExpRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 8, 2, 1, 2),
    _ExpRS_Type()
)
expRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expRS.setStatus("current")
_ExpName_Type = DisplayString
_ExpName_Object = MibTableColumn
expName = _ExpName_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 8, 2, 1, 3),
    _ExpName_Type()
)
expName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expName.setStatus("current")
_ExpType_Type = ExternalUnitType
_ExpType_Object = MibTableColumn
expType = _ExpType_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 8, 2, 1, 4),
    _ExpType_Type()
)
expType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expType.setStatus("current")


class _ExpCommsFail_Type(Integer32):
    """Custom type expCommsFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("commsGood", 1),
          ("commsFailed", 2),
          ("commsBadData", 3))
    )


_ExpCommsFail_Type.__name__ = "Integer32"
_ExpCommsFail_Object = MibTableColumn
expCommsFail = _ExpCommsFail_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 8, 2, 1, 5),
    _ExpCommsFail_Type()
)
expCommsFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expCommsFail.setStatus("current")
_Clamp_ObjectIdentity = ObjectIdentity
clamp = _Clamp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 9)
)
_ClampTable_Object = MibTable
clampTable = _ClampTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 9, 1)
)
if mibBuilder.loadTexts:
    clampTable.setStatus("current")
_ClampEntry_Object = MibTableRow
clampEntry = _ClampEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 9, 1, 1)
)
clampEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "clampNumber"),
)
if mibBuilder.loadTexts:
    clampEntry.setStatus("current")


class _ClampNumber_Type(Integer32):
    """Custom type clampNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_ClampNumber_Type.__name__ = "Integer32"
_ClampNumber_Object = MibTableColumn
clampNumber = _ClampNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 9, 1, 1, 1),
    _ClampNumber_Type()
)
clampNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clampNumber.setStatus("current")
_ClampRS_Type = RowStatus
_ClampRS_Object = MibTableColumn
clampRS = _ClampRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 9, 1, 1, 2),
    _ClampRS_Type()
)
clampRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clampRS.setStatus("current")


class _ClampBValue_Type(Unsigned32):
    """Custom type clampBValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20000, 150000),
    )


_ClampBValue_Type.__name__ = "Unsigned32"
_ClampBValue_Object = MibTableColumn
clampBValue = _ClampBValue_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 9, 1, 1, 3),
    _ClampBValue_Type()
)
clampBValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clampBValue.setStatus("current")


class _ClampVolts_Type(Unsigned32):
    """Custom type clampVolts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(90, 250),
    )


_ClampVolts_Type.__name__ = "Unsigned32"
_ClampVolts_Object = MibTableColumn
clampVolts = _ClampVolts_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 9, 1, 1, 4),
    _ClampVolts_Type()
)
clampVolts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clampVolts.setStatus("current")


class _ClampPwrFactor_Type(Unsigned32):
    """Custom type clampPwrFactor based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ClampPwrFactor_Type.__name__ = "Unsigned32"
_ClampPwrFactor_Object = MibTableColumn
clampPwrFactor = _ClampPwrFactor_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 9, 1, 1, 5),
    _ClampPwrFactor_Type()
)
clampPwrFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clampPwrFactor.setStatus("current")


class _ClampFrequency_Type(Unsigned32):
    """Custom type clampFrequency based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(450, 650),
    )


_ClampFrequency_Type.__name__ = "Unsigned32"
_ClampFrequency_Object = MibTableColumn
clampFrequency = _ClampFrequency_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 9, 1, 1, 6),
    _ClampFrequency_Type()
)
clampFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clampFrequency.setStatus("current")
_ClampWriteParams_Type = Unsigned32
_ClampWriteParams_Object = MibTableColumn
clampWriteParams = _ClampWriteParams_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 9, 1, 1, 15),
    _ClampWriteParams_Type()
)
clampWriteParams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clampWriteParams.setStatus("current")
_Idm_ObjectIdentity = ObjectIdentity
idm = _Idm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 10)
)
_IdmTable_Object = MibTable
idmTable = _IdmTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 10, 1)
)
if mibBuilder.loadTexts:
    idmTable.setStatus("current")
_IdmEntry_Object = MibTableRow
idmEntry = _IdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 10, 1, 1)
)
idmEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "idmNumber"),
)
if mibBuilder.loadTexts:
    idmEntry.setStatus("current")


class _IdmNumber_Type(Integer32):
    """Custom type idmNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_IdmNumber_Type.__name__ = "Integer32"
_IdmNumber_Object = MibTableColumn
idmNumber = _IdmNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 10, 1, 1, 1),
    _IdmNumber_Type()
)
idmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idmNumber.setStatus("current")
_IdmRS_Type = RowStatus
_IdmRS_Object = MibTableColumn
idmRS = _IdmRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 10, 1, 1, 2),
    _IdmRS_Type()
)
idmRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idmRS.setStatus("current")
_IdmVersion_Type = DisplayString
_IdmVersion_Object = MibTableColumn
idmVersion = _IdmVersion_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 10, 1, 1, 3),
    _IdmVersion_Type()
)
idmVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idmVersion.setStatus("current")


class _IdmStatus_Type(Integer32):
    """Custom type idmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("unknown", 255))
    )


_IdmStatus_Type.__name__ = "Integer32"
_IdmStatus_Object = MibTableColumn
idmStatus = _IdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 10, 1, 1, 4),
    _IdmStatus_Type()
)
idmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idmStatus.setStatus("current")
_PdusP2_ObjectIdentity = ObjectIdentity
pdusP2 = _PdusP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 11)
)
_PduP2BrCct_ObjectIdentity = ObjectIdentity
pduP2BrCct = _PduP2BrCct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 11, 1)
)
_PduP2BrCctMonitorTable_Object = MibTable
pduP2BrCctMonitorTable = _PduP2BrCctMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 11, 1, 1)
)
if mibBuilder.loadTexts:
    pduP2BrCctMonitorTable.setStatus("current")
_PduP2BrCctMonitorEntry_Object = MibTableRow
pduP2BrCctMonitorEntry = _PduP2BrCctMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 11, 1, 1, 1)
)
pduP2BrCctMonitorEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "pduP2BrCktMonPduNumber"),
    (0, "HAWK-I2-MIB", "pduP2BrCktMonBrCctNumber"),
)
if mibBuilder.loadTexts:
    pduP2BrCctMonitorEntry.setStatus("current")
_PduP2BrCktMonPduNumber_Type = Unsigned32
_PduP2BrCktMonPduNumber_Object = MibTableColumn
pduP2BrCktMonPduNumber = _PduP2BrCktMonPduNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 11, 1, 1, 1, 1),
    _PduP2BrCktMonPduNumber_Type()
)
pduP2BrCktMonPduNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduP2BrCktMonPduNumber.setStatus("current")


class _PduP2BrCktMonBrCctNumber_Type(Unsigned32):
    """Custom type pduP2BrCktMonBrCctNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_PduP2BrCktMonBrCctNumber_Type.__name__ = "Unsigned32"
_PduP2BrCktMonBrCctNumber_Object = MibTableColumn
pduP2BrCktMonBrCctNumber = _PduP2BrCktMonBrCctNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 11, 1, 1, 1, 2),
    _PduP2BrCktMonBrCctNumber_Type()
)
pduP2BrCktMonBrCctNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduP2BrCktMonBrCctNumber.setStatus("current")
_PduP2BrCktMonRS_Type = RowStatus
_PduP2BrCktMonRS_Object = MibTableColumn
pduP2BrCktMonRS = _PduP2BrCktMonRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 11, 1, 1, 1, 3),
    _PduP2BrCktMonRS_Type()
)
pduP2BrCktMonRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduP2BrCktMonRS.setStatus("current")
_PduP2BrCktMonBrCctID_Type = DisplayString
_PduP2BrCktMonBrCctID_Object = MibTableColumn
pduP2BrCktMonBrCctID = _PduP2BrCktMonBrCctID_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 11, 1, 1, 1, 4),
    _PduP2BrCktMonBrCctID_Type()
)
pduP2BrCktMonBrCctID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduP2BrCktMonBrCctID.setStatus("current")
_PduP2BrCktMonBrCctPhases_Type = DisplayString
_PduP2BrCktMonBrCctPhases_Object = MibTableColumn
pduP2BrCktMonBrCctPhases = _PduP2BrCktMonBrCctPhases_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 11, 1, 1, 1, 5),
    _PduP2BrCktMonBrCctPhases_Type()
)
pduP2BrCktMonBrCctPhases.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduP2BrCktMonBrCctPhases.setStatus("current")
_PduP2BrCktMonBrCctCurrent_Type = Unsigned32
_PduP2BrCktMonBrCctCurrent_Object = MibTableColumn
pduP2BrCktMonBrCctCurrent = _PduP2BrCktMonBrCctCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 11, 1, 1, 1, 6),
    _PduP2BrCktMonBrCctCurrent_Type()
)
pduP2BrCktMonBrCctCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduP2BrCktMonBrCctCurrent.setStatus("current")
_PduP2BrCktMonBrCctPeakCurrent_Type = Unsigned32
_PduP2BrCktMonBrCctPeakCurrent_Object = MibTableColumn
pduP2BrCktMonBrCctPeakCurrent = _PduP2BrCktMonBrCctPeakCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 11, 1, 1, 1, 7),
    _PduP2BrCktMonBrCctPeakCurrent_Type()
)
pduP2BrCktMonBrCctPeakCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduP2BrCktMonBrCctPeakCurrent.setStatus("current")
_PduP2BrCktMonBrCctPeakCurrentTimestamp_Type = UnsignedTimeTicks
_PduP2BrCktMonBrCctPeakCurrentTimestamp_Object = MibTableColumn
pduP2BrCktMonBrCctPeakCurrentTimestamp = _PduP2BrCktMonBrCctPeakCurrentTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 11, 1, 1, 1, 8),
    _PduP2BrCktMonBrCctPeakCurrentTimestamp_Type()
)
pduP2BrCktMonBrCctPeakCurrentTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduP2BrCktMonBrCctPeakCurrentTimestamp.setStatus("current")
_PduP2BrCktMonBrCctBreakerStatus_Type = BranchCircuitStatusType
_PduP2BrCktMonBrCctBreakerStatus_Object = MibTableColumn
pduP2BrCktMonBrCctBreakerStatus = _PduP2BrCktMonBrCctBreakerStatus_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 11, 1, 1, 1, 9),
    _PduP2BrCktMonBrCctBreakerStatus_Type()
)
pduP2BrCktMonBrCctBreakerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduP2BrCktMonBrCctBreakerStatus.setStatus("current")
_PduP2BrCktMonBrCctBreakerConfig_Type = BranchCircuitConfigType
_PduP2BrCktMonBrCctBreakerConfig_Object = MibTableColumn
pduP2BrCktMonBrCctBreakerConfig = _PduP2BrCktMonBrCctBreakerConfig_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 11, 1, 1, 1, 10),
    _PduP2BrCktMonBrCctBreakerConfig_Type()
)
pduP2BrCktMonBrCctBreakerConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduP2BrCktMonBrCctBreakerConfig.setStatus("current")
_PduP2BrCktMonBrCctBreakerTripState_Type = BranchCircuitStatusType
_PduP2BrCktMonBrCctBreakerTripState_Object = MibTableColumn
pduP2BrCktMonBrCctBreakerTripState = _PduP2BrCktMonBrCctBreakerTripState_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 11, 1, 1, 1, 11),
    _PduP2BrCktMonBrCctBreakerTripState_Type()
)
pduP2BrCktMonBrCctBreakerTripState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduP2BrCktMonBrCctBreakerTripState.setStatus("current")


class _PduP2BrCktMonBrCctBreakerContinuousLoadRatingAmps_Type(Unsigned32):
    """Custom type pduP2BrCktMonBrCctBreakerContinuousLoadRatingAmps based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_PduP2BrCktMonBrCctBreakerContinuousLoadRatingAmps_Type.__name__ = "Unsigned32"
_PduP2BrCktMonBrCctBreakerContinuousLoadRatingAmps_Object = MibTableColumn
pduP2BrCktMonBrCctBreakerContinuousLoadRatingAmps = _PduP2BrCktMonBrCctBreakerContinuousLoadRatingAmps_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 11, 1, 1, 1, 12),
    _PduP2BrCktMonBrCctBreakerContinuousLoadRatingAmps_Type()
)
pduP2BrCktMonBrCctBreakerContinuousLoadRatingAmps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduP2BrCktMonBrCctBreakerContinuousLoadRatingAmps.setStatus("current")


class _PduP2BrCktMonBrCctBreakerTripRatingAmps_Type(Unsigned32):
    """Custom type pduP2BrCktMonBrCctBreakerTripRatingAmps based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_PduP2BrCktMonBrCctBreakerTripRatingAmps_Type.__name__ = "Unsigned32"
_PduP2BrCktMonBrCctBreakerTripRatingAmps_Object = MibTableColumn
pduP2BrCktMonBrCctBreakerTripRatingAmps = _PduP2BrCktMonBrCctBreakerTripRatingAmps_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 11, 1, 1, 1, 13),
    _PduP2BrCktMonBrCctBreakerTripRatingAmps_Type()
)
pduP2BrCktMonBrCctBreakerTripRatingAmps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduP2BrCktMonBrCctBreakerTripRatingAmps.setStatus("current")
_PduP2BrCktMonBrCctBreakerOutletMap_Type = DisplayString
_PduP2BrCktMonBrCctBreakerOutletMap_Object = MibTableColumn
pduP2BrCktMonBrCctBreakerOutletMap = _PduP2BrCktMonBrCctBreakerOutletMap_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 11, 1, 1, 1, 14),
    _PduP2BrCktMonBrCctBreakerOutletMap_Type()
)
pduP2BrCktMonBrCctBreakerOutletMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduP2BrCktMonBrCctBreakerOutletMap.setStatus("current")


class _PduP2BrCktCircuitCurrentUCL_Type(Integer32):
    """Custom type pduP2BrCktCircuitCurrentUCL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 100000),
    )


_PduP2BrCktCircuitCurrentUCL_Type.__name__ = "Integer32"
_PduP2BrCktCircuitCurrentUCL_Object = MibTableColumn
pduP2BrCktCircuitCurrentUCL = _PduP2BrCktCircuitCurrentUCL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 11, 1, 1, 1, 15),
    _PduP2BrCktCircuitCurrentUCL_Type()
)
pduP2BrCktCircuitCurrentUCL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduP2BrCktCircuitCurrentUCL.setStatus("current")


class _PduP2BrCktCircuitCurrentUWL_Type(Integer32):
    """Custom type pduP2BrCktCircuitCurrentUWL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 100000),
    )


_PduP2BrCktCircuitCurrentUWL_Type.__name__ = "Integer32"
_PduP2BrCktCircuitCurrentUWL_Object = MibTableColumn
pduP2BrCktCircuitCurrentUWL = _PduP2BrCktCircuitCurrentUWL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 11, 1, 1, 1, 16),
    _PduP2BrCktCircuitCurrentUWL_Type()
)
pduP2BrCktCircuitCurrentUWL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduP2BrCktCircuitCurrentUWL.setStatus("current")


class _PduP2BrCktCircuitCurrentLWL_Type(Integer32):
    """Custom type pduP2BrCktCircuitCurrentLWL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 100000),
    )


_PduP2BrCktCircuitCurrentLWL_Type.__name__ = "Integer32"
_PduP2BrCktCircuitCurrentLWL_Object = MibTableColumn
pduP2BrCktCircuitCurrentLWL = _PduP2BrCktCircuitCurrentLWL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 11, 1, 1, 1, 17),
    _PduP2BrCktCircuitCurrentLWL_Type()
)
pduP2BrCktCircuitCurrentLWL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduP2BrCktCircuitCurrentLWL.setStatus("current")


class _PduP2BrCktCircuitCurrentLCL_Type(Integer32):
    """Custom type pduP2BrCktCircuitCurrentLCL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 100000),
    )


_PduP2BrCktCircuitCurrentLCL_Type.__name__ = "Integer32"
_PduP2BrCktCircuitCurrentLCL_Object = MibTableColumn
pduP2BrCktCircuitCurrentLCL = _PduP2BrCktCircuitCurrentLCL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 11, 1, 1, 1, 18),
    _PduP2BrCktCircuitCurrentLCL_Type()
)
pduP2BrCktCircuitCurrentLCL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduP2BrCktCircuitCurrentLCL.setStatus("current")
_PduP2BrCktCircuitCurrentUCLTrapEn_Type = TruthValue
_PduP2BrCktCircuitCurrentUCLTrapEn_Object = MibTableColumn
pduP2BrCktCircuitCurrentUCLTrapEn = _PduP2BrCktCircuitCurrentUCLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 11, 1, 1, 1, 19),
    _PduP2BrCktCircuitCurrentUCLTrapEn_Type()
)
pduP2BrCktCircuitCurrentUCLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduP2BrCktCircuitCurrentUCLTrapEn.setStatus("current")
_PduP2BrCktCircuitCurrentUWLTrapEn_Type = TruthValue
_PduP2BrCktCircuitCurrentUWLTrapEn_Object = MibTableColumn
pduP2BrCktCircuitCurrentUWLTrapEn = _PduP2BrCktCircuitCurrentUWLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 11, 1, 1, 1, 20),
    _PduP2BrCktCircuitCurrentUWLTrapEn_Type()
)
pduP2BrCktCircuitCurrentUWLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduP2BrCktCircuitCurrentUWLTrapEn.setStatus("current")
_PduP2BrCktCircuitCurrentLWLTrapEn_Type = TruthValue
_PduP2BrCktCircuitCurrentLWLTrapEn_Object = MibTableColumn
pduP2BrCktCircuitCurrentLWLTrapEn = _PduP2BrCktCircuitCurrentLWLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 11, 1, 1, 1, 21),
    _PduP2BrCktCircuitCurrentLWLTrapEn_Type()
)
pduP2BrCktCircuitCurrentLWLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduP2BrCktCircuitCurrentLWLTrapEn.setStatus("current")
_PduP2BrCktCircuitCurrentLCLTrapEn_Type = TruthValue
_PduP2BrCktCircuitCurrentLCLTrapEn_Object = MibTableColumn
pduP2BrCktCircuitCurrentLCLTrapEn = _PduP2BrCktCircuitCurrentLCLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 11, 1, 1, 1, 22),
    _PduP2BrCktCircuitCurrentLCLTrapEn_Type()
)
pduP2BrCktCircuitCurrentLCLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduP2BrCktCircuitCurrentLCLTrapEn.setStatus("current")


class _PduP2BrCktCircuitCurrentUCLTrapPer_Type(Unsigned32):
    """Custom type pduP2BrCktCircuitCurrentUCLTrapPer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PduP2BrCktCircuitCurrentUCLTrapPer_Type.__name__ = "Unsigned32"
_PduP2BrCktCircuitCurrentUCLTrapPer_Object = MibTableColumn
pduP2BrCktCircuitCurrentUCLTrapPer = _PduP2BrCktCircuitCurrentUCLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 11, 1, 1, 1, 23),
    _PduP2BrCktCircuitCurrentUCLTrapPer_Type()
)
pduP2BrCktCircuitCurrentUCLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduP2BrCktCircuitCurrentUCLTrapPer.setStatus("current")


class _PduP2BrCktCircuitCurrentUWLTrapPer_Type(Unsigned32):
    """Custom type pduP2BrCktCircuitCurrentUWLTrapPer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PduP2BrCktCircuitCurrentUWLTrapPer_Type.__name__ = "Unsigned32"
_PduP2BrCktCircuitCurrentUWLTrapPer_Object = MibTableColumn
pduP2BrCktCircuitCurrentUWLTrapPer = _PduP2BrCktCircuitCurrentUWLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 11, 1, 1, 1, 24),
    _PduP2BrCktCircuitCurrentUWLTrapPer_Type()
)
pduP2BrCktCircuitCurrentUWLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduP2BrCktCircuitCurrentUWLTrapPer.setStatus("current")


class _PduP2BrCktCircuitCurrentLWLTrapPer_Type(Unsigned32):
    """Custom type pduP2BrCktCircuitCurrentLWLTrapPer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PduP2BrCktCircuitCurrentLWLTrapPer_Type.__name__ = "Unsigned32"
_PduP2BrCktCircuitCurrentLWLTrapPer_Object = MibTableColumn
pduP2BrCktCircuitCurrentLWLTrapPer = _PduP2BrCktCircuitCurrentLWLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 11, 1, 1, 1, 25),
    _PduP2BrCktCircuitCurrentLWLTrapPer_Type()
)
pduP2BrCktCircuitCurrentLWLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduP2BrCktCircuitCurrentLWLTrapPer.setStatus("current")


class _PduP2BrCktCircuitCurrentLCLTrapPer_Type(Unsigned32):
    """Custom type pduP2BrCktCircuitCurrentLCLTrapPer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PduP2BrCktCircuitCurrentLCLTrapPer_Type.__name__ = "Unsigned32"
_PduP2BrCktCircuitCurrentLCLTrapPer_Object = MibTableColumn
pduP2BrCktCircuitCurrentLCLTrapPer = _PduP2BrCktCircuitCurrentLCLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 11, 1, 1, 1, 26),
    _PduP2BrCktCircuitCurrentLCLTrapPer_Type()
)
pduP2BrCktCircuitCurrentLCLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduP2BrCktCircuitCurrentLCLTrapPer.setStatus("current")
_PlatformData_ObjectIdentity = ObjectIdentity
platformData = _PlatformData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 98)
)
_PlatHwType_Type = DisplayString
_PlatHwType_Object = MibScalar
platHwType = _PlatHwType_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 98, 1),
    _PlatHwType_Type()
)
platHwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platHwType.setStatus("current")
_PlatFwRev_Type = DisplayString
_PlatFwRev_Object = MibScalar
platFwRev = _PlatFwRev_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 98, 2),
    _PlatFwRev_Type()
)
platFwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platFwRev.setStatus("current")
_PlatBootldrRev_Type = DisplayString
_PlatBootldrRev_Object = MibScalar
platBootldrRev = _PlatBootldrRev_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 98, 3),
    _PlatBootldrRev_Type()
)
platBootldrRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platBootldrRev.setStatus("current")
_PlatModelName_Type = DisplayString
_PlatModelName_Object = MibScalar
platModelName = _PlatModelName_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 98, 4),
    _PlatModelName_Type()
)
platModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platModelName.setStatus("current")
_Inventory_ObjectIdentity = ObjectIdentity
inventory = _Inventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99)
)
_InvProdSignature_Type = DisplayString
_InvProdSignature_Object = MibScalar
invProdSignature = _InvProdSignature_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 1),
    _InvProdSignature_Type()
)
invProdSignature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invProdSignature.setStatus("current")
_InvProdFormatVer_Type = DisplayString
_InvProdFormatVer_Object = MibScalar
invProdFormatVer = _InvProdFormatVer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 2),
    _InvProdFormatVer_Type()
)
invProdFormatVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invProdFormatVer.setStatus("current")
_InvManufCode_Type = DisplayString
_InvManufCode_Object = MibScalar
invManufCode = _InvManufCode_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 3),
    _InvManufCode_Type()
)
invManufCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invManufCode.setStatus("current")
_InvOrderNum_Type = DisplayString
_InvOrderNum_Object = MibScalar
invOrderNum = _InvOrderNum_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 4),
    _InvOrderNum_Type()
)
invOrderNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invOrderNum.setStatus("current")
_InvBatchNum_Type = DisplayString
_InvBatchNum_Object = MibScalar
invBatchNum = _InvBatchNum_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 5),
    _InvBatchNum_Type()
)
invBatchNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invBatchNum.setStatus("current")
_InvProdTestTime_Type = DisplayString
_InvProdTestTime_Object = MibScalar
invProdTestTime = _InvProdTestTime_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 6),
    _InvProdTestTime_Type()
)
invProdTestTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invProdTestTime.setStatus("current")
_InvUnitName_Type = DisplayString
_InvUnitName_Object = MibScalar
invUnitName = _InvUnitName_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 7),
    _InvUnitName_Type()
)
invUnitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invUnitName.setStatus("current")
_InvUnitPartNum_Type = DisplayString
_InvUnitPartNum_Object = MibScalar
invUnitPartNum = _InvUnitPartNum_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 8),
    _InvUnitPartNum_Type()
)
invUnitPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invUnitPartNum.setStatus("current")
_InvHwRevision_Type = DisplayString
_InvHwRevision_Object = MibScalar
invHwRevision = _InvHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 9),
    _InvHwRevision_Type()
)
invHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invHwRevision.setStatus("current")
_InvFwRevision_Type = DisplayString
_InvFwRevision_Object = MibScalar
invFwRevision = _InvFwRevision_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 10),
    _InvFwRevision_Type()
)
invFwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invFwRevision.setStatus("current")
_InvSerialNum_Type = DisplayString
_InvSerialNum_Object = MibScalar
invSerialNum = _InvSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 11),
    _InvSerialNum_Type()
)
invSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSerialNum.setStatus("current")
_InvDefaultIPAddrType_Type = IpStackConfiguration
_InvDefaultIPAddrType_Object = MibScalar
invDefaultIPAddrType = _InvDefaultIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 12),
    _InvDefaultIPAddrType_Type()
)
invDefaultIPAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invDefaultIPAddrType.setStatus("current")
_InvDefaultIPAddr_Type = InetAddress
_InvDefaultIPAddr_Object = MibScalar
invDefaultIPAddr = _InvDefaultIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 13),
    _InvDefaultIPAddr_Type()
)
invDefaultIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invDefaultIPAddr.setStatus("current")
_InvDefaultSubNetMask_Type = InetAddress
_InvDefaultSubNetMask_Object = MibScalar
invDefaultSubNetMask = _InvDefaultSubNetMask_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 14),
    _InvDefaultSubNetMask_Type()
)
invDefaultSubNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invDefaultSubNetMask.setStatus("current")
_InvDefaultGWAddr_Type = InetAddress
_InvDefaultGWAddr_Object = MibScalar
invDefaultGWAddr = _InvDefaultGWAddr_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 15),
    _InvDefaultGWAddr_Type()
)
invDefaultGWAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invDefaultGWAddr.setStatus("current")
_InvMacAddr_Type = MacAddress
_InvMacAddr_Object = MibScalar
invMacAddr = _InvMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 16),
    _InvMacAddr_Type()
)
invMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invMacAddr.setStatus("current")
_InvOk_Type = TruthValue
_InvOk_Object = MibScalar
invOk = _InvOk_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 20),
    _InvOk_Type()
)
invOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invOk.setStatus("current")


class _InvInputCount_Type(Integer32):
    """Custom type invInputCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_InvInputCount_Type.__name__ = "Integer32"
_InvInputCount_Object = MibScalar
invInputCount = _InvInputCount_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 50),
    _InvInputCount_Type()
)
invInputCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invInputCount.setStatus("current")


class _InvOutputCount_Type(Integer32):
    """Custom type invOutputCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_InvOutputCount_Type.__name__ = "Integer32"
_InvOutputCount_Object = MibScalar
invOutputCount = _InvOutputCount_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 51),
    _InvOutputCount_Type()
)
invOutputCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invOutputCount.setStatus("current")


class _InvKeypadCount_Type(Integer32):
    """Custom type invKeypadCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_InvKeypadCount_Type.__name__ = "Integer32"
_InvKeypadCount_Object = MibScalar
invKeypadCount = _InvKeypadCount_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 52),
    _InvKeypadCount_Type()
)
invKeypadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invKeypadCount.setStatus("current")


class _InvAcuCount_Type(Integer32):
    """Custom type invAcuCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_InvAcuCount_Type.__name__ = "Integer32"
_InvAcuCount_Object = MibScalar
invAcuCount = _InvAcuCount_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 53),
    _InvAcuCount_Type()
)
invAcuCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invAcuCount.setStatus("current")


class _InvAccessUserCount_Type(Integer32):
    """Custom type invAccessUserCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_InvAccessUserCount_Type.__name__ = "Integer32"
_InvAccessUserCount_Object = MibScalar
invAccessUserCount = _InvAccessUserCount_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 54),
    _InvAccessUserCount_Type()
)
invAccessUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invAccessUserCount.setStatus("current")


class _InvPduCount_Type(Integer32):
    """Custom type invPduCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_InvPduCount_Type.__name__ = "Integer32"
_InvPduCount_Object = MibScalar
invPduCount = _InvPduCount_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 55),
    _InvPduCount_Type()
)
invPduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invPduCount.setStatus("current")
_TrapInfo_ObjectIdentity = ObjectIdentity
trapInfo = _TrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 100)
)
_TrapCode_Type = Integer32
_TrapCode_Object = MibScalar
trapCode = _TrapCode_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 100, 1),
    _TrapCode_Type()
)
trapCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapCode.setStatus("current")
_TrapDescription_Type = DisplayString
_TrapDescription_Object = MibScalar
trapDescription = _TrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 100, 2),
    _TrapDescription_Type()
)
trapDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDescription.setStatus("current")
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 2)
)
_V2_ObjectIdentity = ObjectIdentity
v2 = _V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2)
)
_Objects2_ObjectIdentity = ObjectIdentity
objects2 = _Objects2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1)
)
_Pdus2_ObjectIdentity = ObjectIdentity
pdus2 = _Pdus2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1)
)
_Pdu2Common_ObjectIdentity = ObjectIdentity
pdu2Common = _Pdu2Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1)
)
_Pdu2Table_Object = MibTable
pdu2Table = _Pdu2Table_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    pdu2Table.setStatus("current")
_Pdu2Entry_Object = MibTableRow
pdu2Entry = _Pdu2Entry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 1, 1)
)
pdu2Entry.setIndexNames(
    (0, "HAWK-I2-MIB", "pdu2PduNumber"),
)
if mibBuilder.loadTexts:
    pdu2Entry.setStatus("current")
_Pdu2PduNumber_Type = Unsigned32
_Pdu2PduNumber_Object = MibTableColumn
pdu2PduNumber = _Pdu2PduNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 1, 1, 1),
    _Pdu2PduNumber_Type()
)
pdu2PduNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2PduNumber.setStatus("current")
_Pdu2RS_Type = RowStatus
_Pdu2RS_Object = MibTableColumn
pdu2RS = _Pdu2RS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 1, 1, 2),
    _Pdu2RS_Type()
)
pdu2RS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2RS.setStatus("current")
_Pdu2WiringTopology_Type = WiringTopologyType
_Pdu2WiringTopology_Object = MibTableColumn
pdu2WiringTopology = _Pdu2WiringTopology_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 1, 1, 3),
    _Pdu2WiringTopology_Type()
)
pdu2WiringTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2WiringTopology.setStatus("current")
_Pdu2PhaseTopology_Type = DisplayString
_Pdu2PhaseTopology_Object = MibTableColumn
pdu2PhaseTopology = _Pdu2PhaseTopology_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 1, 1, 4),
    _Pdu2PhaseTopology_Type()
)
pdu2PhaseTopology.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu2PhaseTopology.setStatus("current")
_Pdu2CustDataTable_Object = MibTable
pdu2CustDataTable = _Pdu2CustDataTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    pdu2CustDataTable.setStatus("current")
_Pdu2CustDataEntry_Object = MibTableRow
pdu2CustDataEntry = _Pdu2CustDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 2, 1)
)
pdu2CustDataEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "pdu2CustDataPduNumber"),
)
if mibBuilder.loadTexts:
    pdu2CustDataEntry.setStatus("current")
_Pdu2CustDataPduNumber_Type = Unsigned32
_Pdu2CustDataPduNumber_Object = MibTableColumn
pdu2CustDataPduNumber = _Pdu2CustDataPduNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 2, 1, 1),
    _Pdu2CustDataPduNumber_Type()
)
pdu2CustDataPduNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2CustDataPduNumber.setStatus("current")
_Pdu2CustDataRS_Type = RowStatus
_Pdu2CustDataRS_Object = MibTableColumn
pdu2CustDataRS = _Pdu2CustDataRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 2, 1, 2),
    _Pdu2CustDataRS_Type()
)
pdu2CustDataRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2CustDataRS.setStatus("current")
_Pdu2CustDataMainCktRefOverall_Type = CktRefName
_Pdu2CustDataMainCktRefOverall_Object = MibTableColumn
pdu2CustDataMainCktRefOverall = _Pdu2CustDataMainCktRefOverall_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 2, 1, 3),
    _Pdu2CustDataMainCktRefOverall_Type()
)
pdu2CustDataMainCktRefOverall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu2CustDataMainCktRefOverall.setStatus("current")
_Pdu2CustDataMainCktRefCktA_Type = CktRefName
_Pdu2CustDataMainCktRefCktA_Object = MibTableColumn
pdu2CustDataMainCktRefCktA = _Pdu2CustDataMainCktRefCktA_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 2, 1, 4),
    _Pdu2CustDataMainCktRefCktA_Type()
)
pdu2CustDataMainCktRefCktA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu2CustDataMainCktRefCktA.setStatus("current")
_Pdu2CustDataMainCktRefCktB_Type = CktRefName
_Pdu2CustDataMainCktRefCktB_Object = MibTableColumn
pdu2CustDataMainCktRefCktB = _Pdu2CustDataMainCktRefCktB_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 2, 1, 5),
    _Pdu2CustDataMainCktRefCktB_Type()
)
pdu2CustDataMainCktRefCktB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu2CustDataMainCktRefCktB.setStatus("current")
_Pdu2CustDataMainCktRefCktC_Type = CktRefName
_Pdu2CustDataMainCktRefCktC_Object = MibTableColumn
pdu2CustDataMainCktRefCktC = _Pdu2CustDataMainCktRefCktC_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 2, 1, 6),
    _Pdu2CustDataMainCktRefCktC_Type()
)
pdu2CustDataMainCktRefCktC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu2CustDataMainCktRefCktC.setStatus("current")
_Pdu2InputAggregateTable_Object = MibTable
pdu2InputAggregateTable = _Pdu2InputAggregateTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    pdu2InputAggregateTable.setStatus("current")
_Pdu2InputAggregateEntry_Object = MibTableRow
pdu2InputAggregateEntry = _Pdu2InputAggregateEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 3, 1)
)
pdu2InputAggregateEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "pdu2IpAggPduNumber"),
)
if mibBuilder.loadTexts:
    pdu2InputAggregateEntry.setStatus("current")
_Pdu2IpAggPduNumber_Type = Unsigned32
_Pdu2IpAggPduNumber_Object = MibTableColumn
pdu2IpAggPduNumber = _Pdu2IpAggPduNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 3, 1, 1),
    _Pdu2IpAggPduNumber_Type()
)
pdu2IpAggPduNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2IpAggPduNumber.setStatus("current")
_Pdu2IpAggRS_Type = RowStatus
_Pdu2IpAggRS_Object = MibTableColumn
pdu2IpAggRS = _Pdu2IpAggRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 3, 1, 2),
    _Pdu2IpAggRS_Type()
)
pdu2IpAggRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2IpAggRS.setStatus("current")
_Pdu2IpAggAggregatekWh_Type = Unsigned32
_Pdu2IpAggAggregatekWh_Object = MibTableColumn
pdu2IpAggAggregatekWh = _Pdu2IpAggAggregatekWh_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 3, 1, 3),
    _Pdu2IpAggAggregatekWh_Type()
)
pdu2IpAggAggregatekWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2IpAggAggregatekWh.setStatus("current")
_Pdu2IpAggAggregatekVA_Type = Unsigned32
_Pdu2IpAggAggregatekVA_Object = MibTableColumn
pdu2IpAggAggregatekVA = _Pdu2IpAggAggregatekVA_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 3, 1, 4),
    _Pdu2IpAggAggregatekVA_Type()
)
pdu2IpAggAggregatekVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2IpAggAggregatekVA.setStatus("current")
_Pdu2IpAggAggregatekW_Type = Unsigned32
_Pdu2IpAggAggregatekW_Object = MibTableColumn
pdu2IpAggAggregatekW = _Pdu2IpAggAggregatekW_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 3, 1, 5),
    _Pdu2IpAggAggregatekW_Type()
)
pdu2IpAggAggregatekW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2IpAggAggregatekW.setStatus("current")
_Pdu2IpAggAggregatePF_Type = Unsigned32
_Pdu2IpAggAggregatePF_Object = MibTableColumn
pdu2IpAggAggregatePF = _Pdu2IpAggAggregatePF_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 3, 1, 6),
    _Pdu2IpAggAggregatePF_Type()
)
pdu2IpAggAggregatePF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2IpAggAggregatePF.setStatus("current")
_Pdu2IpAggAggregateCurrent_Type = Unsigned32
_Pdu2IpAggAggregateCurrent_Object = MibTableColumn
pdu2IpAggAggregateCurrent = _Pdu2IpAggAggregateCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 3, 1, 7),
    _Pdu2IpAggAggregateCurrent_Type()
)
pdu2IpAggAggregateCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2IpAggAggregateCurrent.setStatus("current")
_Pdu2IpAggAggregateNeutralCurrent_Type = Unsigned32
_Pdu2IpAggAggregateNeutralCurrent_Object = MibTableColumn
pdu2IpAggAggregateNeutralCurrent = _Pdu2IpAggAggregateNeutralCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 3, 1, 8),
    _Pdu2IpAggAggregateNeutralCurrent_Type()
)
pdu2IpAggAggregateNeutralCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2IpAggAggregateNeutralCurrent.setStatus("current")
_Pdu2IpAggAggregateEarthCurrent_Type = Unsigned32
_Pdu2IpAggAggregateEarthCurrent_Object = MibTableColumn
pdu2IpAggAggregateEarthCurrent = _Pdu2IpAggAggregateEarthCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 3, 1, 9),
    _Pdu2IpAggAggregateEarthCurrent_Type()
)
pdu2IpAggAggregateEarthCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2IpAggAggregateEarthCurrent.setStatus("current")
_Pdu2PhaseMonitorTable_Object = MibTable
pdu2PhaseMonitorTable = _Pdu2PhaseMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    pdu2PhaseMonitorTable.setStatus("current")
_Pdu2PhaseMonitorEntry_Object = MibTableRow
pdu2PhaseMonitorEntry = _Pdu2PhaseMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 4, 1)
)
pdu2PhaseMonitorEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "pdu2PhMonPduNumber"),
    (0, "HAWK-I2-MIB", "pdu2PhMonPhaseNumber"),
)
if mibBuilder.loadTexts:
    pdu2PhaseMonitorEntry.setStatus("current")
_Pdu2PhMonPduNumber_Type = Unsigned32
_Pdu2PhMonPduNumber_Object = MibTableColumn
pdu2PhMonPduNumber = _Pdu2PhMonPduNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 4, 1, 1),
    _Pdu2PhMonPduNumber_Type()
)
pdu2PhMonPduNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2PhMonPduNumber.setStatus("current")
_Pdu2PhMonPhaseNumber_Type = Unsigned32
_Pdu2PhMonPhaseNumber_Object = MibTableColumn
pdu2PhMonPhaseNumber = _Pdu2PhMonPhaseNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 4, 1, 2),
    _Pdu2PhMonPhaseNumber_Type()
)
pdu2PhMonPhaseNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2PhMonPhaseNumber.setStatus("current")
_Pdu2PhMonRS_Type = RowStatus
_Pdu2PhMonRS_Object = MibTableColumn
pdu2PhMonRS = _Pdu2PhMonRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 4, 1, 3),
    _Pdu2PhMonRS_Type()
)
pdu2PhMonRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2PhMonRS.setStatus("current")
_Pdu2PhMonLineID_Type = DisplayString
_Pdu2PhMonLineID_Object = MibTableColumn
pdu2PhMonLineID = _Pdu2PhMonLineID_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 4, 1, 4),
    _Pdu2PhMonLineID_Type()
)
pdu2PhMonLineID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2PhMonLineID.setStatus("current")
_Pdu2PhMonPhaseToNeutralVoltage_Type = Unsigned32
_Pdu2PhMonPhaseToNeutralVoltage_Object = MibTableColumn
pdu2PhMonPhaseToNeutralVoltage = _Pdu2PhMonPhaseToNeutralVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 4, 1, 5),
    _Pdu2PhMonPhaseToNeutralVoltage_Type()
)
pdu2PhMonPhaseToNeutralVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2PhMonPhaseToNeutralVoltage.setStatus("current")
_Pdu2PhMonPhaseCurrent_Type = Unsigned32
_Pdu2PhMonPhaseCurrent_Object = MibTableColumn
pdu2PhMonPhaseCurrent = _Pdu2PhMonPhaseCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 4, 1, 6),
    _Pdu2PhMonPhaseCurrent_Type()
)
pdu2PhMonPhaseCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2PhMonPhaseCurrent.setStatus("current")
_Pdu2PhMonPhasekVA_Type = Unsigned32
_Pdu2PhMonPhasekVA_Object = MibTableColumn
pdu2PhMonPhasekVA = _Pdu2PhMonPhasekVA_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 4, 1, 7),
    _Pdu2PhMonPhasekVA_Type()
)
pdu2PhMonPhasekVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2PhMonPhasekVA.setStatus("current")
_Pdu2PhMonPhasePeakkVA_Type = Unsigned32
_Pdu2PhMonPhasePeakkVA_Object = MibTableColumn
pdu2PhMonPhasePeakkVA = _Pdu2PhMonPhasePeakkVA_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 4, 1, 8),
    _Pdu2PhMonPhasePeakkVA_Type()
)
pdu2PhMonPhasePeakkVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2PhMonPhasePeakkVA.setStatus("current")
_Pdu2PhMonPhasePeakkVATimestamp_Type = UnsignedTimeTicks
_Pdu2PhMonPhasePeakkVATimestamp_Object = MibTableColumn
pdu2PhMonPhasePeakkVATimestamp = _Pdu2PhMonPhasePeakkVATimestamp_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 4, 1, 9),
    _Pdu2PhMonPhasePeakkVATimestamp_Type()
)
pdu2PhMonPhasePeakkVATimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2PhMonPhasePeakkVATimestamp.setStatus("current")
_Pdu2PhMonPhasekW_Type = Unsigned32
_Pdu2PhMonPhasekW_Object = MibTableColumn
pdu2PhMonPhasekW = _Pdu2PhMonPhasekW_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 4, 1, 10),
    _Pdu2PhMonPhasekW_Type()
)
pdu2PhMonPhasekW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2PhMonPhasekW.setStatus("current")
_Pdu2PhMonPhasePF_Type = Unsigned32
_Pdu2PhMonPhasePF_Object = MibTableColumn
pdu2PhMonPhasePF = _Pdu2PhMonPhasePF_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 4, 1, 11),
    _Pdu2PhMonPhasePF_Type()
)
pdu2PhMonPhasePF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2PhMonPhasePF.setStatus("current")
_Pdu2PhMonPhasekWh_Type = Unsigned32
_Pdu2PhMonPhasekWh_Object = MibTableColumn
pdu2PhMonPhasekWh = _Pdu2PhMonPhasekWh_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 4, 1, 12),
    _Pdu2PhMonPhasekWh_Type()
)
pdu2PhMonPhasekWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2PhMonPhasekWh.setStatus("current")
_Pdu2PhMonPhasekVAr_Type = Unsigned32
_Pdu2PhMonPhasekVAr_Object = MibTableColumn
pdu2PhMonPhasekVAr = _Pdu2PhMonPhasekVAr_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 4, 1, 13),
    _Pdu2PhMonPhasekVAr_Type()
)
pdu2PhMonPhasekVAr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2PhMonPhasekVAr.setStatus("current")
_Pdu2PhMonPhaseCrestFactor_Type = Unsigned32
_Pdu2PhMonPhaseCrestFactor_Object = MibTableColumn
pdu2PhMonPhaseCrestFactor = _Pdu2PhMonPhaseCrestFactor_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 4, 1, 14),
    _Pdu2PhMonPhaseCrestFactor_Type()
)
pdu2PhMonPhaseCrestFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2PhMonPhaseCrestFactor.setStatus("current")
_Pdu2PhMonPhaseTHD_Type = Unsigned32
_Pdu2PhMonPhaseTHD_Object = MibTableColumn
pdu2PhMonPhaseTHD = _Pdu2PhMonPhaseTHD_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 4, 1, 15),
    _Pdu2PhMonPhaseTHD_Type()
)
pdu2PhMonPhaseTHD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2PhMonPhaseTHD.setStatus("current")
_Pdu2CircuitMonitorTable_Object = MibTable
pdu2CircuitMonitorTable = _Pdu2CircuitMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    pdu2CircuitMonitorTable.setStatus("current")
_Pdu2CircuitMonitorEntry_Object = MibTableRow
pdu2CircuitMonitorEntry = _Pdu2CircuitMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 5, 1)
)
pdu2CircuitMonitorEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "pdu2CktMonPduNumber"),
    (0, "HAWK-I2-MIB", "pdu2CktMonCircuitNumber"),
)
if mibBuilder.loadTexts:
    pdu2CircuitMonitorEntry.setStatus("current")
_Pdu2CktMonPduNumber_Type = Unsigned32
_Pdu2CktMonPduNumber_Object = MibTableColumn
pdu2CktMonPduNumber = _Pdu2CktMonPduNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 5, 1, 1),
    _Pdu2CktMonPduNumber_Type()
)
pdu2CktMonPduNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2CktMonPduNumber.setStatus("current")
_Pdu2CktMonCircuitNumber_Type = Unsigned32
_Pdu2CktMonCircuitNumber_Object = MibTableColumn
pdu2CktMonCircuitNumber = _Pdu2CktMonCircuitNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 5, 1, 2),
    _Pdu2CktMonCircuitNumber_Type()
)
pdu2CktMonCircuitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2CktMonCircuitNumber.setStatus("current")
_Pdu2CktMonRS_Type = RowStatus
_Pdu2CktMonRS_Object = MibTableColumn
pdu2CktMonRS = _Pdu2CktMonRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 5, 1, 3),
    _Pdu2CktMonRS_Type()
)
pdu2CktMonRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2CktMonRS.setStatus("current")
_Pdu2CktMonLineID_Type = DisplayString
_Pdu2CktMonLineID_Object = MibTableColumn
pdu2CktMonLineID = _Pdu2CktMonLineID_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 5, 1, 4),
    _Pdu2CktMonLineID_Type()
)
pdu2CktMonLineID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2CktMonLineID.setStatus("current")
_Pdu2CktMonLineToLineVoltage_Type = Unsigned32
_Pdu2CktMonLineToLineVoltage_Object = MibTableColumn
pdu2CktMonLineToLineVoltage = _Pdu2CktMonLineToLineVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 5, 1, 5),
    _Pdu2CktMonLineToLineVoltage_Type()
)
pdu2CktMonLineToLineVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2CktMonLineToLineVoltage.setStatus("current")
_Pdu2CktMonLineToLineCurrent_Type = Unsigned32
_Pdu2CktMonLineToLineCurrent_Object = MibTableColumn
pdu2CktMonLineToLineCurrent = _Pdu2CktMonLineToLineCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 5, 1, 6),
    _Pdu2CktMonLineToLineCurrent_Type()
)
pdu2CktMonLineToLineCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2CktMonLineToLineCurrent.setStatus("current")
_Pdu2CktMonLineToLineKVA_Type = Unsigned32
_Pdu2CktMonLineToLineKVA_Object = MibTableColumn
pdu2CktMonLineToLineKVA = _Pdu2CktMonLineToLineKVA_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 5, 1, 7),
    _Pdu2CktMonLineToLineKVA_Type()
)
pdu2CktMonLineToLineKVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2CktMonLineToLineKVA.setStatus("current")
_Pdu2CktMonLineToLinePeakkVA_Type = Unsigned32
_Pdu2CktMonLineToLinePeakkVA_Object = MibTableColumn
pdu2CktMonLineToLinePeakkVA = _Pdu2CktMonLineToLinePeakkVA_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 5, 1, 8),
    _Pdu2CktMonLineToLinePeakkVA_Type()
)
pdu2CktMonLineToLinePeakkVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2CktMonLineToLinePeakkVA.setStatus("current")
_Pdu2CktMonLineToLinePeakkVATimestamp_Type = UnsignedTimeTicks
_Pdu2CktMonLineToLinePeakkVATimestamp_Object = MibTableColumn
pdu2CktMonLineToLinePeakkVATimestamp = _Pdu2CktMonLineToLinePeakkVATimestamp_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 5, 1, 9),
    _Pdu2CktMonLineToLinePeakkVATimestamp_Type()
)
pdu2CktMonLineToLinePeakkVATimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2CktMonLineToLinePeakkVATimestamp.setStatus("current")
_Pdu2CktMonLineToLinekW_Type = Unsigned32
_Pdu2CktMonLineToLinekW_Object = MibTableColumn
pdu2CktMonLineToLinekW = _Pdu2CktMonLineToLinekW_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 5, 1, 10),
    _Pdu2CktMonLineToLinekW_Type()
)
pdu2CktMonLineToLinekW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2CktMonLineToLinekW.setStatus("current")
_Pdu2CktMonLineToLinePF_Type = Unsigned32
_Pdu2CktMonLineToLinePF_Object = MibTableColumn
pdu2CktMonLineToLinePF = _Pdu2CktMonLineToLinePF_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 5, 1, 11),
    _Pdu2CktMonLineToLinePF_Type()
)
pdu2CktMonLineToLinePF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2CktMonLineToLinePF.setStatus("current")
_Pdu2CktMonLineToLinekVAr_Type = Unsigned32
_Pdu2CktMonLineToLinekVAr_Object = MibTableColumn
pdu2CktMonLineToLinekVAr = _Pdu2CktMonLineToLinekVAr_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 5, 1, 12),
    _Pdu2CktMonLineToLinekVAr_Type()
)
pdu2CktMonLineToLinekVAr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2CktMonLineToLinekVAr.setStatus("current")
_Pdu2BranchCircuitMonitorTable_Object = MibTable
pdu2BranchCircuitMonitorTable = _Pdu2BranchCircuitMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    pdu2BranchCircuitMonitorTable.setStatus("current")
_Pdu2BranchCircuitMonitorEntry_Object = MibTableRow
pdu2BranchCircuitMonitorEntry = _Pdu2BranchCircuitMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 6, 1)
)
pdu2BranchCircuitMonitorEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "pdu2BrCktMonPduNumber"),
    (0, "HAWK-I2-MIB", "pdu2BrCktMonBranchCircuitNumber"),
)
if mibBuilder.loadTexts:
    pdu2BranchCircuitMonitorEntry.setStatus("current")
_Pdu2BrCktMonPduNumber_Type = Unsigned32
_Pdu2BrCktMonPduNumber_Object = MibTableColumn
pdu2BrCktMonPduNumber = _Pdu2BrCktMonPduNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 6, 1, 1),
    _Pdu2BrCktMonPduNumber_Type()
)
pdu2BrCktMonPduNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2BrCktMonPduNumber.setStatus("current")
_Pdu2BrCktMonBranchCircuitNumber_Type = Unsigned32
_Pdu2BrCktMonBranchCircuitNumber_Object = MibTableColumn
pdu2BrCktMonBranchCircuitNumber = _Pdu2BrCktMonBranchCircuitNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 6, 1, 2),
    _Pdu2BrCktMonBranchCircuitNumber_Type()
)
pdu2BrCktMonBranchCircuitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2BrCktMonBranchCircuitNumber.setStatus("current")
_Pdu2BrCktMonRS_Type = RowStatus
_Pdu2BrCktMonRS_Object = MibTableColumn
pdu2BrCktMonRS = _Pdu2BrCktMonRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 6, 1, 3),
    _Pdu2BrCktMonRS_Type()
)
pdu2BrCktMonRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2BrCktMonRS.setStatus("current")
_Pdu2BrCktMonBranchCircuitID_Type = DisplayString
_Pdu2BrCktMonBranchCircuitID_Object = MibTableColumn
pdu2BrCktMonBranchCircuitID = _Pdu2BrCktMonBranchCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 6, 1, 4),
    _Pdu2BrCktMonBranchCircuitID_Type()
)
pdu2BrCktMonBranchCircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2BrCktMonBranchCircuitID.setStatus("current")
_Pdu2BrCktMonBranchCircuitPhases_Type = DisplayString
_Pdu2BrCktMonBranchCircuitPhases_Object = MibTableColumn
pdu2BrCktMonBranchCircuitPhases = _Pdu2BrCktMonBranchCircuitPhases_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 6, 1, 5),
    _Pdu2BrCktMonBranchCircuitPhases_Type()
)
pdu2BrCktMonBranchCircuitPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2BrCktMonBranchCircuitPhases.setStatus("current")
_Pdu2BrCktMonBranchCircuitCurrent_Type = Unsigned32
_Pdu2BrCktMonBranchCircuitCurrent_Object = MibTableColumn
pdu2BrCktMonBranchCircuitCurrent = _Pdu2BrCktMonBranchCircuitCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 6, 1, 6),
    _Pdu2BrCktMonBranchCircuitCurrent_Type()
)
pdu2BrCktMonBranchCircuitCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2BrCktMonBranchCircuitCurrent.setStatus("current")
_Pdu2BrCktMonBranchCircuitPeakCurrent_Type = Unsigned32
_Pdu2BrCktMonBranchCircuitPeakCurrent_Object = MibTableColumn
pdu2BrCktMonBranchCircuitPeakCurrent = _Pdu2BrCktMonBranchCircuitPeakCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 6, 1, 7),
    _Pdu2BrCktMonBranchCircuitPeakCurrent_Type()
)
pdu2BrCktMonBranchCircuitPeakCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2BrCktMonBranchCircuitPeakCurrent.setStatus("current")
_Pdu2BrCktMonBranchCircuitPeakCurrentTimestamp_Type = UnsignedTimeTicks
_Pdu2BrCktMonBranchCircuitPeakCurrentTimestamp_Object = MibTableColumn
pdu2BrCktMonBranchCircuitPeakCurrentTimestamp = _Pdu2BrCktMonBranchCircuitPeakCurrentTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 6, 1, 8),
    _Pdu2BrCktMonBranchCircuitPeakCurrentTimestamp_Type()
)
pdu2BrCktMonBranchCircuitPeakCurrentTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2BrCktMonBranchCircuitPeakCurrentTimestamp.setStatus("current")
_Pdu2BrCktMonBranchCircuitBreakerStatus_Type = BranchCircuitStatusType
_Pdu2BrCktMonBranchCircuitBreakerStatus_Object = MibTableColumn
pdu2BrCktMonBranchCircuitBreakerStatus = _Pdu2BrCktMonBranchCircuitBreakerStatus_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 6, 1, 9),
    _Pdu2BrCktMonBranchCircuitBreakerStatus_Type()
)
pdu2BrCktMonBranchCircuitBreakerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2BrCktMonBranchCircuitBreakerStatus.setStatus("current")
_Pdu2BrCktMonBranchCircuitBreakerConfig_Type = BranchCircuitConfigType
_Pdu2BrCktMonBranchCircuitBreakerConfig_Object = MibTableColumn
pdu2BrCktMonBranchCircuitBreakerConfig = _Pdu2BrCktMonBranchCircuitBreakerConfig_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 6, 1, 10),
    _Pdu2BrCktMonBranchCircuitBreakerConfig_Type()
)
pdu2BrCktMonBranchCircuitBreakerConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu2BrCktMonBranchCircuitBreakerConfig.setStatus("current")
_Pdu2BrCktMonBranchCircuitBreakerTripState_Type = BranchCircuitStatusType
_Pdu2BrCktMonBranchCircuitBreakerTripState_Object = MibTableColumn
pdu2BrCktMonBranchCircuitBreakerTripState = _Pdu2BrCktMonBranchCircuitBreakerTripState_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 6, 1, 11),
    _Pdu2BrCktMonBranchCircuitBreakerTripState_Type()
)
pdu2BrCktMonBranchCircuitBreakerTripState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2BrCktMonBranchCircuitBreakerTripState.setStatus("current")
_Pdu2BrCktMonBranchCircuitBreakerContinuousLoadRatingAmps_Type = Unsigned32
_Pdu2BrCktMonBranchCircuitBreakerContinuousLoadRatingAmps_Object = MibTableColumn
pdu2BrCktMonBranchCircuitBreakerContinuousLoadRatingAmps = _Pdu2BrCktMonBranchCircuitBreakerContinuousLoadRatingAmps_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 6, 1, 12),
    _Pdu2BrCktMonBranchCircuitBreakerContinuousLoadRatingAmps_Type()
)
pdu2BrCktMonBranchCircuitBreakerContinuousLoadRatingAmps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2BrCktMonBranchCircuitBreakerContinuousLoadRatingAmps.setStatus("current")
_Pdu2BrCktMonBranchCircuitBreakerTripRatingAmps_Type = Unsigned32
_Pdu2BrCktMonBranchCircuitBreakerTripRatingAmps_Object = MibTableColumn
pdu2BrCktMonBranchCircuitBreakerTripRatingAmps = _Pdu2BrCktMonBranchCircuitBreakerTripRatingAmps_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 6, 1, 13),
    _Pdu2BrCktMonBranchCircuitBreakerTripRatingAmps_Type()
)
pdu2BrCktMonBranchCircuitBreakerTripRatingAmps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2BrCktMonBranchCircuitBreakerTripRatingAmps.setStatus("current")
_Pdu2OutletMonitorTable_Object = MibTable
pdu2OutletMonitorTable = _Pdu2OutletMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    pdu2OutletMonitorTable.setStatus("current")
_Pdu2OutletMonitorEntry_Object = MibTableRow
pdu2OutletMonitorEntry = _Pdu2OutletMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 7, 1)
)
pdu2OutletMonitorEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "pdu2OutMonPduNumber"),
    (0, "HAWK-I2-MIB", "pdu2OutMonOutletNumber"),
)
if mibBuilder.loadTexts:
    pdu2OutletMonitorEntry.setStatus("current")
_Pdu2OutMonPduNumber_Type = Unsigned32
_Pdu2OutMonPduNumber_Object = MibTableColumn
pdu2OutMonPduNumber = _Pdu2OutMonPduNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 7, 1, 1),
    _Pdu2OutMonPduNumber_Type()
)
pdu2OutMonPduNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2OutMonPduNumber.setStatus("current")
_Pdu2OutMonOutletNumber_Type = Unsigned32
_Pdu2OutMonOutletNumber_Object = MibTableColumn
pdu2OutMonOutletNumber = _Pdu2OutMonOutletNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 7, 1, 2),
    _Pdu2OutMonOutletNumber_Type()
)
pdu2OutMonOutletNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2OutMonOutletNumber.setStatus("current")
_Pdu2OutMonRS_Type = RowStatus
_Pdu2OutMonRS_Object = MibTableColumn
pdu2OutMonRS = _Pdu2OutMonRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 7, 1, 3),
    _Pdu2OutMonRS_Type()
)
pdu2OutMonRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2OutMonRS.setStatus("current")
_Pdu2OutMonOutletID_Type = DisplayString
_Pdu2OutMonOutletID_Object = MibTableColumn
pdu2OutMonOutletID = _Pdu2OutMonOutletID_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 7, 1, 4),
    _Pdu2OutMonOutletID_Type()
)
pdu2OutMonOutletID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2OutMonOutletID.setStatus("current")
_Pdu2OutMonOutletVoltage_Type = Unsigned32
_Pdu2OutMonOutletVoltage_Object = MibTableColumn
pdu2OutMonOutletVoltage = _Pdu2OutMonOutletVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 7, 1, 5),
    _Pdu2OutMonOutletVoltage_Type()
)
pdu2OutMonOutletVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2OutMonOutletVoltage.setStatus("current")
_Pdu2OutMonOutletCurrent_Type = Unsigned32
_Pdu2OutMonOutletCurrent_Object = MibTableColumn
pdu2OutMonOutletCurrent = _Pdu2OutMonOutletCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 7, 1, 6),
    _Pdu2OutMonOutletCurrent_Type()
)
pdu2OutMonOutletCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2OutMonOutletCurrent.setStatus("current")
_Pdu2OutMonOutletkVA_Type = Unsigned32
_Pdu2OutMonOutletkVA_Object = MibTableColumn
pdu2OutMonOutletkVA = _Pdu2OutMonOutletkVA_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 7, 1, 7),
    _Pdu2OutMonOutletkVA_Type()
)
pdu2OutMonOutletkVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2OutMonOutletkVA.setStatus("current")
_Pdu2OutMonOutletPeakkVA_Type = Unsigned32
_Pdu2OutMonOutletPeakkVA_Object = MibTableColumn
pdu2OutMonOutletPeakkVA = _Pdu2OutMonOutletPeakkVA_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 7, 1, 8),
    _Pdu2OutMonOutletPeakkVA_Type()
)
pdu2OutMonOutletPeakkVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2OutMonOutletPeakkVA.setStatus("current")
_Pdu2OutMonOutletPeakkVATimestamp_Type = UnsignedTimeTicks
_Pdu2OutMonOutletPeakkVATimestamp_Object = MibTableColumn
pdu2OutMonOutletPeakkVATimestamp = _Pdu2OutMonOutletPeakkVATimestamp_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 7, 1, 9),
    _Pdu2OutMonOutletPeakkVATimestamp_Type()
)
pdu2OutMonOutletPeakkVATimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2OutMonOutletPeakkVATimestamp.setStatus("current")
_Pdu2OutMonOutletkW_Type = Unsigned32
_Pdu2OutMonOutletkW_Object = MibTableColumn
pdu2OutMonOutletkW = _Pdu2OutMonOutletkW_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 7, 1, 10),
    _Pdu2OutMonOutletkW_Type()
)
pdu2OutMonOutletkW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2OutMonOutletkW.setStatus("current")
_Pdu2OutMonOutletPF_Type = Unsigned32
_Pdu2OutMonOutletPF_Object = MibTableColumn
pdu2OutMonOutletPF = _Pdu2OutMonOutletPF_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 7, 1, 11),
    _Pdu2OutMonOutletPF_Type()
)
pdu2OutMonOutletPF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2OutMonOutletPF.setStatus("current")
_Pdu2OutMonOutletkWh_Type = Unsigned32
_Pdu2OutMonOutletkWh_Object = MibTableColumn
pdu2OutMonOutletkWh = _Pdu2OutMonOutletkWh_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 7, 1, 12),
    _Pdu2OutMonOutletkWh_Type()
)
pdu2OutMonOutletkWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2OutMonOutletkWh.setStatus("current")
_Pdu2OutMonOutletBranchCircuitID_Type = DisplayString
_Pdu2OutMonOutletBranchCircuitID_Object = MibTableColumn
pdu2OutMonOutletBranchCircuitID = _Pdu2OutMonOutletBranchCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 7, 1, 13),
    _Pdu2OutMonOutletBranchCircuitID_Type()
)
pdu2OutMonOutletBranchCircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2OutMonOutletBranchCircuitID.setStatus("current")
_Pdu2OutMonOutletPhaseID_Type = DisplayString
_Pdu2OutMonOutletPhaseID_Object = MibTableColumn
pdu2OutMonOutletPhaseID = _Pdu2OutMonOutletPhaseID_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 7, 1, 14),
    _Pdu2OutMonOutletPhaseID_Type()
)
pdu2OutMonOutletPhaseID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2OutMonOutletPhaseID.setStatus("current")
_Pdu2OutletControlTable_Object = MibTable
pdu2OutletControlTable = _Pdu2OutletControlTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 8)
)
if mibBuilder.loadTexts:
    pdu2OutletControlTable.setStatus("current")
_Pdu2OutletControlEntry_Object = MibTableRow
pdu2OutletControlEntry = _Pdu2OutletControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 8, 1)
)
pdu2OutletControlEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "pdu2OutCtlPduNumber"),
    (0, "HAWK-I2-MIB", "pdu2OutCtlOutletNumber"),
)
if mibBuilder.loadTexts:
    pdu2OutletControlEntry.setStatus("current")
_Pdu2OutCtlPduNumber_Type = Unsigned32
_Pdu2OutCtlPduNumber_Object = MibTableColumn
pdu2OutCtlPduNumber = _Pdu2OutCtlPduNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 8, 1, 1),
    _Pdu2OutCtlPduNumber_Type()
)
pdu2OutCtlPduNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2OutCtlPduNumber.setStatus("current")
_Pdu2OutCtlOutletNumber_Type = Unsigned32
_Pdu2OutCtlOutletNumber_Object = MibTableColumn
pdu2OutCtlOutletNumber = _Pdu2OutCtlOutletNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 8, 1, 2),
    _Pdu2OutCtlOutletNumber_Type()
)
pdu2OutCtlOutletNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2OutCtlOutletNumber.setStatus("current")
_Pdu2OutCtlRS_Type = RowStatus
_Pdu2OutCtlRS_Object = MibTableColumn
pdu2OutCtlRS = _Pdu2OutCtlRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 8, 1, 3),
    _Pdu2OutCtlRS_Type()
)
pdu2OutCtlRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2OutCtlRS.setStatus("current")
_Pdu2OutCtlControlledOutletID_Type = DisplayString
_Pdu2OutCtlControlledOutletID_Object = MibTableColumn
pdu2OutCtlControlledOutletID = _Pdu2OutCtlControlledOutletID_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 8, 1, 4),
    _Pdu2OutCtlControlledOutletID_Type()
)
pdu2OutCtlControlledOutletID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2OutCtlControlledOutletID.setStatus("current")
_Pdu2OutCtlControlledOutletState_Type = ControlledOutletStatusType
_Pdu2OutCtlControlledOutletState_Object = MibTableColumn
pdu2OutCtlControlledOutletState = _Pdu2OutCtlControlledOutletState_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 8, 1, 5),
    _Pdu2OutCtlControlledOutletState_Type()
)
pdu2OutCtlControlledOutletState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2OutCtlControlledOutletState.setStatus("current")
_Pdu2OutCtlControlledOutletPowerUpState_Type = ControlledOutletStatusType
_Pdu2OutCtlControlledOutletPowerUpState_Object = MibTableColumn
pdu2OutCtlControlledOutletPowerUpState = _Pdu2OutCtlControlledOutletPowerUpState_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 8, 1, 6),
    _Pdu2OutCtlControlledOutletPowerUpState_Type()
)
pdu2OutCtlControlledOutletPowerUpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2OutCtlControlledOutletPowerUpState.setStatus("current")
_Pdu2OutCtlControlledOutletPowerUpTimeDelay_Type = Unsigned32
_Pdu2OutCtlControlledOutletPowerUpTimeDelay_Object = MibTableColumn
pdu2OutCtlControlledOutletPowerUpTimeDelay = _Pdu2OutCtlControlledOutletPowerUpTimeDelay_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 8, 1, 7),
    _Pdu2OutCtlControlledOutletPowerUpTimeDelay_Type()
)
pdu2OutCtlControlledOutletPowerUpTimeDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2OutCtlControlledOutletPowerUpTimeDelay.setStatus("current")
_Pdu2BranchCircuitThreshTable_Object = MibTable
pdu2BranchCircuitThreshTable = _Pdu2BranchCircuitThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 9)
)
if mibBuilder.loadTexts:
    pdu2BranchCircuitThreshTable.setStatus("current")
_Pdu2BranchCircuitThreshEntry_Object = MibTableRow
pdu2BranchCircuitThreshEntry = _Pdu2BranchCircuitThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 9, 1)
)
pdu2BranchCircuitThreshEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "pdu2BrCktThreshPduNumber"),
    (0, "HAWK-I2-MIB", "pdu2BrCktThreshBranchCircuitNumber"),
)
if mibBuilder.loadTexts:
    pdu2BranchCircuitThreshEntry.setStatus("current")
_Pdu2BrCktThreshPduNumber_Type = Unsigned32
_Pdu2BrCktThreshPduNumber_Object = MibTableColumn
pdu2BrCktThreshPduNumber = _Pdu2BrCktThreshPduNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 9, 1, 1),
    _Pdu2BrCktThreshPduNumber_Type()
)
pdu2BrCktThreshPduNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2BrCktThreshPduNumber.setStatus("current")
_Pdu2BrCktThreshBranchCircuitNumber_Type = Unsigned32
_Pdu2BrCktThreshBranchCircuitNumber_Object = MibTableColumn
pdu2BrCktThreshBranchCircuitNumber = _Pdu2BrCktThreshBranchCircuitNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 9, 1, 2),
    _Pdu2BrCktThreshBranchCircuitNumber_Type()
)
pdu2BrCktThreshBranchCircuitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2BrCktThreshBranchCircuitNumber.setStatus("current")
_Pdu2BrCktThreshRS_Type = RowStatus
_Pdu2BrCktThreshRS_Object = MibTableColumn
pdu2BrCktThreshRS = _Pdu2BrCktThreshRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 9, 1, 3),
    _Pdu2BrCktThreshRS_Type()
)
pdu2BrCktThreshRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2BrCktThreshRS.setStatus("current")
_Pdu2BrCktBranchCircuitCurrentUCL_Type = Unsigned32
_Pdu2BrCktBranchCircuitCurrentUCL_Object = MibTableColumn
pdu2BrCktBranchCircuitCurrentUCL = _Pdu2BrCktBranchCircuitCurrentUCL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 9, 1, 4),
    _Pdu2BrCktBranchCircuitCurrentUCL_Type()
)
pdu2BrCktBranchCircuitCurrentUCL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu2BrCktBranchCircuitCurrentUCL.setStatus("current")
_Pdu2BrCktBranchCircuitCurrentUWL_Type = Unsigned32
_Pdu2BrCktBranchCircuitCurrentUWL_Object = MibTableColumn
pdu2BrCktBranchCircuitCurrentUWL = _Pdu2BrCktBranchCircuitCurrentUWL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 9, 1, 5),
    _Pdu2BrCktBranchCircuitCurrentUWL_Type()
)
pdu2BrCktBranchCircuitCurrentUWL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu2BrCktBranchCircuitCurrentUWL.setStatus("current")
_Pdu2BrCktBranchCircuitCurrentLWL_Type = Unsigned32
_Pdu2BrCktBranchCircuitCurrentLWL_Object = MibTableColumn
pdu2BrCktBranchCircuitCurrentLWL = _Pdu2BrCktBranchCircuitCurrentLWL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 9, 1, 6),
    _Pdu2BrCktBranchCircuitCurrentLWL_Type()
)
pdu2BrCktBranchCircuitCurrentLWL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu2BrCktBranchCircuitCurrentLWL.setStatus("current")
_Pdu2BrCktBranchCircuitCurrentLCL_Type = Unsigned32
_Pdu2BrCktBranchCircuitCurrentLCL_Object = MibTableColumn
pdu2BrCktBranchCircuitCurrentLCL = _Pdu2BrCktBranchCircuitCurrentLCL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 9, 1, 7),
    _Pdu2BrCktBranchCircuitCurrentLCL_Type()
)
pdu2BrCktBranchCircuitCurrentLCL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu2BrCktBranchCircuitCurrentLCL.setStatus("current")
_Pdu2BranchCircuitTrapEnTable_Object = MibTable
pdu2BranchCircuitTrapEnTable = _Pdu2BranchCircuitTrapEnTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 10)
)
if mibBuilder.loadTexts:
    pdu2BranchCircuitTrapEnTable.setStatus("current")
_Pdu2BranchCircuitTrapEnEntry_Object = MibTableRow
pdu2BranchCircuitTrapEnEntry = _Pdu2BranchCircuitTrapEnEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 10, 1)
)
pdu2BranchCircuitTrapEnEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "pdu2BrCktTrapEnPduNumber"),
    (0, "HAWK-I2-MIB", "pdu2BrCktTrapEnBranchCircuitNumber"),
)
if mibBuilder.loadTexts:
    pdu2BranchCircuitTrapEnEntry.setStatus("current")
_Pdu2BrCktTrapEnPduNumber_Type = Unsigned32
_Pdu2BrCktTrapEnPduNumber_Object = MibTableColumn
pdu2BrCktTrapEnPduNumber = _Pdu2BrCktTrapEnPduNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 10, 1, 1),
    _Pdu2BrCktTrapEnPduNumber_Type()
)
pdu2BrCktTrapEnPduNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2BrCktTrapEnPduNumber.setStatus("current")
_Pdu2BrCktTrapEnBranchCircuitNumber_Type = Unsigned32
_Pdu2BrCktTrapEnBranchCircuitNumber_Object = MibTableColumn
pdu2BrCktTrapEnBranchCircuitNumber = _Pdu2BrCktTrapEnBranchCircuitNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 10, 1, 2),
    _Pdu2BrCktTrapEnBranchCircuitNumber_Type()
)
pdu2BrCktTrapEnBranchCircuitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2BrCktTrapEnBranchCircuitNumber.setStatus("current")
_Pdu2BrCktTrapEnRS_Type = RowStatus
_Pdu2BrCktTrapEnRS_Object = MibTableColumn
pdu2BrCktTrapEnRS = _Pdu2BrCktTrapEnRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 10, 1, 3),
    _Pdu2BrCktTrapEnRS_Type()
)
pdu2BrCktTrapEnRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2BrCktTrapEnRS.setStatus("current")
_Pdu2BrCktBranchCircuitCurrentUCLTrapEn_Type = TruthValue
_Pdu2BrCktBranchCircuitCurrentUCLTrapEn_Object = MibTableColumn
pdu2BrCktBranchCircuitCurrentUCLTrapEn = _Pdu2BrCktBranchCircuitCurrentUCLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 10, 1, 4),
    _Pdu2BrCktBranchCircuitCurrentUCLTrapEn_Type()
)
pdu2BrCktBranchCircuitCurrentUCLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu2BrCktBranchCircuitCurrentUCLTrapEn.setStatus("current")
_Pdu2BrCktBranchCircuitCurrentUWLTrapEn_Type = TruthValue
_Pdu2BrCktBranchCircuitCurrentUWLTrapEn_Object = MibTableColumn
pdu2BrCktBranchCircuitCurrentUWLTrapEn = _Pdu2BrCktBranchCircuitCurrentUWLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 10, 1, 5),
    _Pdu2BrCktBranchCircuitCurrentUWLTrapEn_Type()
)
pdu2BrCktBranchCircuitCurrentUWLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu2BrCktBranchCircuitCurrentUWLTrapEn.setStatus("current")
_Pdu2BrCktBranchCircuitCurrentLWLTrapEn_Type = TruthValue
_Pdu2BrCktBranchCircuitCurrentLWLTrapEn_Object = MibTableColumn
pdu2BrCktBranchCircuitCurrentLWLTrapEn = _Pdu2BrCktBranchCircuitCurrentLWLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 10, 1, 6),
    _Pdu2BrCktBranchCircuitCurrentLWLTrapEn_Type()
)
pdu2BrCktBranchCircuitCurrentLWLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu2BrCktBranchCircuitCurrentLWLTrapEn.setStatus("current")
_Pdu2BrCktBranchCircuitCurrentLCLTrapEn_Type = TruthValue
_Pdu2BrCktBranchCircuitCurrentLCLTrapEn_Object = MibTableColumn
pdu2BrCktBranchCircuitCurrentLCLTrapEn = _Pdu2BrCktBranchCircuitCurrentLCLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 10, 1, 7),
    _Pdu2BrCktBranchCircuitCurrentLCLTrapEn_Type()
)
pdu2BrCktBranchCircuitCurrentLCLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu2BrCktBranchCircuitCurrentLCLTrapEn.setStatus("current")
_Pdu2BranchCircuitTrapPerTable_Object = MibTable
pdu2BranchCircuitTrapPerTable = _Pdu2BranchCircuitTrapPerTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 11)
)
if mibBuilder.loadTexts:
    pdu2BranchCircuitTrapPerTable.setStatus("current")
_Pdu2BranchCircuitTrapPerEntry_Object = MibTableRow
pdu2BranchCircuitTrapPerEntry = _Pdu2BranchCircuitTrapPerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 11, 1)
)
pdu2BranchCircuitTrapPerEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "pdu2BrCktTrapPerPduNumber"),
    (0, "HAWK-I2-MIB", "pdu2BrCktTrapPerBranchCircuitNumber"),
)
if mibBuilder.loadTexts:
    pdu2BranchCircuitTrapPerEntry.setStatus("current")
_Pdu2BrCktTrapPerPduNumber_Type = Unsigned32
_Pdu2BrCktTrapPerPduNumber_Object = MibTableColumn
pdu2BrCktTrapPerPduNumber = _Pdu2BrCktTrapPerPduNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 11, 1, 1),
    _Pdu2BrCktTrapPerPduNumber_Type()
)
pdu2BrCktTrapPerPduNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2BrCktTrapPerPduNumber.setStatus("current")
_Pdu2BrCktTrapPerBranchCircuitNumber_Type = Unsigned32
_Pdu2BrCktTrapPerBranchCircuitNumber_Object = MibTableColumn
pdu2BrCktTrapPerBranchCircuitNumber = _Pdu2BrCktTrapPerBranchCircuitNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 11, 1, 2),
    _Pdu2BrCktTrapPerBranchCircuitNumber_Type()
)
pdu2BrCktTrapPerBranchCircuitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2BrCktTrapPerBranchCircuitNumber.setStatus("current")
_Pdu2BrCktTrapPerRS_Type = RowStatus
_Pdu2BrCktTrapPerRS_Object = MibTableColumn
pdu2BrCktTrapPerRS = _Pdu2BrCktTrapPerRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 11, 1, 3),
    _Pdu2BrCktTrapPerRS_Type()
)
pdu2BrCktTrapPerRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2BrCktTrapPerRS.setStatus("current")
_Pdu2BrCktBranchCircuitCurrentUCLTrapPer_Type = Unsigned32
_Pdu2BrCktBranchCircuitCurrentUCLTrapPer_Object = MibTableColumn
pdu2BrCktBranchCircuitCurrentUCLTrapPer = _Pdu2BrCktBranchCircuitCurrentUCLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 11, 1, 4),
    _Pdu2BrCktBranchCircuitCurrentUCLTrapPer_Type()
)
pdu2BrCktBranchCircuitCurrentUCLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu2BrCktBranchCircuitCurrentUCLTrapPer.setStatus("current")
_Pdu2BrCktBranchCircuitCurrentUWLTrapPer_Type = Unsigned32
_Pdu2BrCktBranchCircuitCurrentUWLTrapPer_Object = MibTableColumn
pdu2BrCktBranchCircuitCurrentUWLTrapPer = _Pdu2BrCktBranchCircuitCurrentUWLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 11, 1, 5),
    _Pdu2BrCktBranchCircuitCurrentUWLTrapPer_Type()
)
pdu2BrCktBranchCircuitCurrentUWLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu2BrCktBranchCircuitCurrentUWLTrapPer.setStatus("current")
_Pdu2BrCktBranchCircuitCurrentLWLTrapPer_Type = Unsigned32
_Pdu2BrCktBranchCircuitCurrentLWLTrapPer_Object = MibTableColumn
pdu2BrCktBranchCircuitCurrentLWLTrapPer = _Pdu2BrCktBranchCircuitCurrentLWLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 11, 1, 6),
    _Pdu2BrCktBranchCircuitCurrentLWLTrapPer_Type()
)
pdu2BrCktBranchCircuitCurrentLWLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu2BrCktBranchCircuitCurrentLWLTrapPer.setStatus("current")
_Pdu2BrCktBranchCircuitCurrentLCLTrapPer_Type = Unsigned32
_Pdu2BrCktBranchCircuitCurrentLCLTrapPer_Object = MibTableColumn
pdu2BrCktBranchCircuitCurrentLCLTrapPer = _Pdu2BrCktBranchCircuitCurrentLCLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 1, 1, 1, 11, 1, 7),
    _Pdu2BrCktBranchCircuitCurrentLCLTrapPer_Type()
)
pdu2BrCktBranchCircuitCurrentLCLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu2BrCktBranchCircuitCurrentLCLTrapPer.setStatus("current")
_Traps2_ObjectIdentity = ObjectIdentity
traps2 = _Traps2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 2, 2)
)

# Managed Objects groups


# Notification objects

alarmCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 2, 1)
)
alarmCritical.setObjects(
      *(("HAWK-I2-MIB", "trapCode"),
        ("HAWK-I2-MIB", "trapDescription"))
)
if mibBuilder.loadTexts:
    alarmCritical.setStatus(
        "current"
    )

alarmWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 2, 2)
)
alarmWarning.setObjects(
      *(("HAWK-I2-MIB", "trapCode"),
        ("HAWK-I2-MIB", "trapDescription"))
)
if mibBuilder.loadTexts:
    alarmWarning.setStatus(
        "current"
    )

alarmInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 2, 3)
)
alarmInformation.setObjects(
      *(("HAWK-I2-MIB", "trapCode"),
        ("HAWK-I2-MIB", "trapDescription"))
)
if mibBuilder.loadTexts:
    alarmInformation.setStatus(
        "current"
    )

alarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 2, 4)
)
alarmCleared.setObjects(
      *(("HAWK-I2-MIB", "trapCode"),
        ("HAWK-I2-MIB", "trapDescription"))
)
if mibBuilder.loadTexts:
    alarmCleared.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HAWK-I2-MIB",
    **{"DisplayString": DisplayString,
       "InetAddressType": InetAddressType,
       "InetAddress": InetAddress,
       "IpStackConfiguration": IpStackConfiguration,
       "ContactState": ContactState,
       "InputContactState": InputContactState,
       "RelayState": RelayState,
       "OutputControlState": OutputControlState,
       "EnableState": EnableState,
       "InputDataType": InputDataType,
       "KeypadEnableState": KeypadEnableState,
       "ExternalUnitType": ExternalUnitType,
       "UnsignedTimeTicks": UnsignedTimeTicks,
       "WiringTopologyType": WiringTopologyType,
       "CktRefName": CktRefName,
       "BranchCircuitStatusType": BranchCircuitStatusType,
       "BranchCircuitConfigType": BranchCircuitConfigType,
       "ControlledOutletStatusType": ControlledOutletStatusType,
       "sinetica": sinetica,
       "hawki2MIB": hawki2MIB,
       "v1": v1,
       "objects": objects,
       "inputs": inputs,
       "ipCommon": ipCommon,
       "ipEnable": ipEnable,
       "ipSelect": ipSelect,
       "ipInsert": ipInsert,
       "ipTHA": ipTHA,
       "ipTempScaleFlag": ipTempScaleFlag,
       "ipTHATable": ipTHATable,
       "ipTHAEntry": ipTHAEntry,
       "ipTHAChan": ipTHAChan,
       "ipTHARS": ipTHARS,
       "ipTHAName": ipTHAName,
       "ipTHALocn": ipTHALocn,
       "ipTHAAutoDetect": ipTHAAutoDetect,
       "ipTHAType": ipTHAType,
       "ipTHAValue": ipTHAValue,
       "ipTHAScaling": ipTHAScaling,
       "ipTHAOffset": ipTHAOffset,
       "ipTHAHysteresis": ipTHAHysteresis,
       "ipTHATrapsCfg": ipTHATrapsCfg,
       "ipTHAThreshTable": ipTHAThreshTable,
       "ipTHAThreshEntry": ipTHAThreshEntry,
       "ipTHAThreshChan": ipTHAThreshChan,
       "ipTHAThreshRS": ipTHAThreshRS,
       "ipTHAUCL": ipTHAUCL,
       "ipTHAUWL": ipTHAUWL,
       "ipTHALWL": ipTHALWL,
       "ipTHALCL": ipTHALCL,
       "ipTHADeltaPos": ipTHADeltaPos,
       "ipTHADeltaNeg": ipTHADeltaNeg,
       "ipTHATrapEnTable": ipTHATrapEnTable,
       "ipTHATrapEnEntry": ipTHATrapEnEntry,
       "ipTHATrapEnChan": ipTHATrapEnChan,
       "ipTHATrapEnRS": ipTHATrapEnRS,
       "ipTHAUCLTrapEn": ipTHAUCLTrapEn,
       "ipTHAUWLTrapEn": ipTHAUWLTrapEn,
       "ipTHALWLTrapEn": ipTHALWLTrapEn,
       "ipTHALCLTrapEn": ipTHALCLTrapEn,
       "ipTHADeltaPosTrapEn": ipTHADeltaPosTrapEn,
       "ipTHADeltaNegTrapEn": ipTHADeltaNegTrapEn,
       "ipTHATrapPerTable": ipTHATrapPerTable,
       "ipTHATrapPerEntry": ipTHATrapPerEntry,
       "ipTHATrapPerChan": ipTHATrapPerChan,
       "ipTHATrapPerRS": ipTHATrapPerRS,
       "ipTHATrapUCLPer": ipTHATrapUCLPer,
       "ipTHATrapUWLPer": ipTHATrapUWLPer,
       "ipTHATrapLWLPer": ipTHATrapLWLPer,
       "ipTHATrapLCLPer": ipTHATrapLCLPer,
       "ipTHATrapDeltaPosPer": ipTHATrapDeltaPosPer,
       "ipTHATrapDeltaNegPer": ipTHATrapDeltaNegPer,
       "ipContact": ipContact,
       "ipContTable": ipContTable,
       "ipContEntry": ipContEntry,
       "ipContChan": ipContChan,
       "ipContRS": ipContRS,
       "ipContName": ipContName,
       "ipContLocn": ipContLocn,
       "ipContAutoDetect": ipContAutoDetect,
       "ipContNormState": ipContNormState,
       "ipContCurrState": ipContCurrState,
       "ipContTrigMode": ipContTrigMode,
       "ipContReset": ipContReset,
       "ipContTrapEn": ipContTrapEn,
       "ipContTrapPeriod": ipContTrapPeriod,
       "outputs": outputs,
       "opEnable": opEnable,
       "opSelect": opSelect,
       "opInsert": opInsert,
       "opTable": opTable,
       "opEntry": opEntry,
       "opChan": opChan,
       "opRS": opRS,
       "opName": opName,
       "opLocn": opLocn,
       "opNormState": opNormState,
       "opCurrState": opCurrState,
       "opOnDelTime": opOnDelTime,
       "opOffDelTime": opOffDelTime,
       "opBooleanEqn": opBooleanEqn,
       "opTrapEn": opTrapEn,
       "opTrapPeriod": opTrapPeriod,
       "opControlState": opControlState,
       "keypads": keypads,
       "kpEnable": kpEnable,
       "kpSelect": kpSelect,
       "kpInsert": kpInsert,
       "kpCtlTable": kpCtlTable,
       "kpCtlEntry": kpCtlEntry,
       "kpNumber": kpNumber,
       "kpRS": kpRS,
       "kpManufacturer": kpManufacturer,
       "kpName": kpName,
       "kpDoorLatchTimeOut": kpDoorLatchTimeOut,
       "kpRtnToStndbyTimeOut": kpRtnToStndbyTimeOut,
       "kpEntryCodeValid": kpEntryCodeValid,
       "kpDoorOpenTimeOut": kpDoorOpenTimeOut,
       "kpRemoteDoorOpen": kpRemoteDoorOpen,
       "kpInUseTrapEn": kpInUseTrapEn,
       "acus": acus,
       "acuEnable": acuEnable,
       "acuSelect": acuSelect,
       "acuInsert": acuInsert,
       "acuCtlTable": acuCtlTable,
       "acuCtlEntry": acuCtlEntry,
       "acuNumber": acuNumber,
       "acuCtlRS": acuCtlRS,
       "acuManufacturer": acuManufacturer,
       "acuName": acuName,
       "acuDoorLatchTimeOut": acuDoorLatchTimeOut,
       "acuRtnToStndbyTimeOut": acuRtnToStndbyTimeOut,
       "acuEntryCodeValid": acuEntryCodeValid,
       "acuDoorOpenTimeOut": acuDoorOpenTimeOut,
       "acuRemoteDoorOpen": acuRemoteDoorOpen,
       "acuInUseTrapEn": acuInUseTrapEn,
       "acuType": acuType,
       "acuAlarms": acuAlarms,
       "acuLastCode": acuLastCode,
       "access": access,
       "accUserCtl": accUserCtl,
       "accUserInstance": accUserInstance,
       "accUserTable": accUserTable,
       "accUserEntry": accUserEntry,
       "accUserNumber": accUserNumber,
       "accUserRS": accUserRS,
       "accUserName": accUserName,
       "accUserCode": accUserCode,
       "accUserPrivileges": accUserPrivileges,
       "accUserExpires": accUserExpires,
       "accUserSetup": accUserSetup,
       "accUserCodeLen": accUserCodeLen,
       "pdus": pdus,
       "pduCommon": pduCommon,
       "pdusEnable": pdusEnable,
       "pduSelect": pduSelect,
       "pduInsert": pduInsert,
       "pduTable": pduTable,
       "pduEntry": pduEntry,
       "pduNumber": pduNumber,
       "pduRS": pduRS,
       "pduName": pduName,
       "pduOutEn": pduOutEn,
       "pduMonEn": pduMonEn,
       "pduCommsFail": pduCommsFail,
       "pduType": pduType,
       "pduMode": pduMode,
       "pduNumControl": pduNumControl,
       "pduOutletMonMode": pduOutletMonMode,
       "pduNumOutlets": pduNumOutlets,
       "pduFwVersCPU": pduFwVersCPU,
       "pduFwVersMeter": pduFwVersMeter,
       "pduNumOfCctBrks": pduNumOfCctBrks,
       "pdusMinMaxPeriod": pdusMinMaxPeriod,
       "pduOutlets": pduOutlets,
       "pduOutAll": pduOutAll,
       "pduOutCycleAll": pduOutCycleAll,
       "pduOutCycleAllPwd": pduOutCycleAllPwd,
       "pduOutCycleAllAbort": pduOutCycleAllAbort,
       "pduOutGlobalCycleDelay": pduOutGlobalCycleDelay,
       "pduOutGlobalRebootTime": pduOutGlobalRebootTime,
       "pduOutGlobalCycleAbortTime": pduOutGlobalCycleAbortTime,
       "pduOutCmnTable": pduOutCmnTable,
       "pduOutCmnEntry": pduOutCmnEntry,
       "pduOutCmnPduNumber": pduOutCmnPduNumber,
       "pduOutCmnRS": pduOutCmnRS,
       "pduNumOfOutlets": pduNumOfOutlets,
       "pduOutCycle": pduOutCycle,
       "pduOutCyclePwd": pduOutCyclePwd,
       "pduOutCycleAbortTask": pduOutCycleAbortTask,
       "pduOutCycleAbortTime": pduOutCycleAbortTime,
       "pduOutTable": pduOutTable,
       "pduOutEntry": pduOutEntry,
       "pduOutPduNumber": pduOutPduNumber,
       "pduOutNumber": pduOutNumber,
       "pduOutRS": pduOutRS,
       "pduOutName": pduOutName,
       "pduOutOn": pduOutOn,
       "pduOutPwd": pduOutPwd,
       "pduOutCycleDelay": pduOutCycleDelay,
       "pduOutRebootPeriod": pduOutRebootPeriod,
       "pduOutRMSAmpsValue": pduOutRMSAmpsValue,
       "pduOutRMSAmpsSurge": pduOutRMSAmpsSurge,
       "pduOutRMSAmpsPeak": pduOutRMSAmpsPeak,
       "pduOutRMSAmpsPkRst": pduOutRMSAmpsPkRst,
       "pduOutMeanKVAValue": pduOutMeanKVAValue,
       "pduOutKWHrValue": pduOutKWHrValue,
       "pduOutPFactorValue": pduOutPFactorValue,
       "pduOutRMSAmpsUTL": pduOutRMSAmpsUTL,
       "pduOutRMSAmpsLTL": pduOutRMSAmpsLTL,
       "pduOutRMSAmpsUTLTrapEn": pduOutRMSAmpsUTLTrapEn,
       "pduOutRMSAmpsLTLTrapEn": pduOutRMSAmpsLTLTrapEn,
       "pduOutRMSAmpsUTLTrapPer": pduOutRMSAmpsUTLTrapPer,
       "pduOutRMSAmpsLTLTrapPer": pduOutRMSAmpsLTLTrapPer,
       "pduMonitor": pduMonitor,
       "pduMonTable": pduMonTable,
       "pduMonEntry": pduMonEntry,
       "pduMonPduNumber": pduMonPduNumber,
       "pduMonRS": pduMonRS,
       "pduRMSVoltsValue": pduRMSVoltsValue,
       "pduRMSAmpsValue": pduRMSAmpsValue,
       "pduTotalEnergyValue": pduTotalEnergyValue,
       "pduMeanKVAValue": pduMeanKVAValue,
       "pduMeanKWattsValue": pduMeanKWattsValue,
       "pduPwrFactorValue": pduPwrFactorValue,
       "pduPwrSupplyFreq": pduPwrSupplyFreq,
       "pduPhaseVoltsValue": pduPhaseVoltsValue,
       "pduPhaseAmpsValue": pduPhaseAmpsValue,
       "pduPhaseEnergyValue": pduPhaseEnergyValue,
       "pduPhaseKVAValue": pduPhaseKVAValue,
       "pduPhaseKWattsValue": pduPhaseKWattsValue,
       "pduPhasePwrFactorValue": pduPhasePwrFactorValue,
       "pduCircuitName": pduCircuitName,
       "pduCctKVAMax": pduCctKVAMax,
       "pduCctKVAMaxTime": pduCctKVAMaxTime,
       "pduCctKVAMin": pduCctKVAMin,
       "pduCctKVAMinTime": pduCctKVAMinTime,
       "pduCctAmpsMax": pduCctAmpsMax,
       "pduCctAmpsMaxTime": pduCctAmpsMaxTime,
       "pduCctAmpsMin": pduCctAmpsMin,
       "pduCctAmpsMinTime": pduCctAmpsMinTime,
       "pduCctStatSagSet": pduCctStatSagSet,
       "pduCctStatSagCount": pduCctStatSagCount,
       "pduCctStatSagTime": pduCctStatSagTime,
       "pduCctStatPkVoltsSet": pduCctStatPkVoltsSet,
       "pduCctStatPkVoltsCount": pduCctStatPkVoltsCount,
       "pduCctStatPkVoltsTime": pduCctStatPkVoltsTime,
       "pduCctStatPwrLossSet": pduCctStatPwrLossSet,
       "pduCctStatPwrLossCount": pduCctStatPwrLossCount,
       "pduCctStatPwrLossTime": pduCctStatPwrLossTime,
       "pduCctPermKVAMax": pduCctPermKVAMax,
       "pduCctPermKVAMaxTime": pduCctPermKVAMaxTime,
       "pduCctPermAmpsMax": pduCctPermAmpsMax,
       "pduCctPermAmpsMaxTime": pduCctPermAmpsMaxTime,
       "pduTrapThreshTable": pduTrapThreshTable,
       "pduTrapThreshEntry": pduTrapThreshEntry,
       "pduTrapThreshPduNumber": pduTrapThreshPduNumber,
       "pduTrapThreshRS": pduTrapThreshRS,
       "pduRMSVoltsUCL": pduRMSVoltsUCL,
       "pduRMSVoltsUWL": pduRMSVoltsUWL,
       "pduRMSVoltsLWL": pduRMSVoltsLWL,
       "pduRMSVoltsLCL": pduRMSVoltsLCL,
       "pduRMSAmpsUCL": pduRMSAmpsUCL,
       "pduRMSAmpsUWL": pduRMSAmpsUWL,
       "pduRMSAmpsLWL": pduRMSAmpsLWL,
       "pduRMSAmpsLCL": pduRMSAmpsLCL,
       "pduEnergyUCL": pduEnergyUCL,
       "pduEnergyUWL": pduEnergyUWL,
       "pduMeanKVAUCL": pduMeanKVAUCL,
       "pduMeanKVAUWL": pduMeanKVAUWL,
       "pduMeanKVALWL": pduMeanKVALWL,
       "pduMeanKVALCL": pduMeanKVALCL,
       "pduMeanKWattsUCL": pduMeanKWattsUCL,
       "pduMeanKWattsUWL": pduMeanKWattsUWL,
       "pduMeanKWattsLWL": pduMeanKWattsLWL,
       "pduMeanKWattsLCL": pduMeanKWattsLCL,
       "pduPwrFactorUTL": pduPwrFactorUTL,
       "pduPwrFactorLTL": pduPwrFactorLTL,
       "pduTrapEnTable": pduTrapEnTable,
       "pduTrapEnEntry": pduTrapEnEntry,
       "pduTrapEnPduNumber": pduTrapEnPduNumber,
       "pduTrapEnRS": pduTrapEnRS,
       "pduRMSVoltsUCLTrapEn": pduRMSVoltsUCLTrapEn,
       "pduRMSVoltsUWLTrapEn": pduRMSVoltsUWLTrapEn,
       "pduRMSVoltsLWLTrapEn": pduRMSVoltsLWLTrapEn,
       "pduRMSVoltsLCLTrapEn": pduRMSVoltsLCLTrapEn,
       "pduRMSAmpsUCLTrapEn": pduRMSAmpsUCLTrapEn,
       "pduRMSAmpsUWLTrapEn": pduRMSAmpsUWLTrapEn,
       "pduRMSAmpsLWLTrapEn": pduRMSAmpsLWLTrapEn,
       "pduRMSAmpsLCLTrapEn": pduRMSAmpsLCLTrapEn,
       "pduEnergyUCLTrapEn": pduEnergyUCLTrapEn,
       "pduEnergyUWLTrapEn": pduEnergyUWLTrapEn,
       "pduMeanKVAUCLTrapEn": pduMeanKVAUCLTrapEn,
       "pduMeanKVAUWLTrapEn": pduMeanKVAUWLTrapEn,
       "pduMeanKVALWLTrapEn": pduMeanKVALWLTrapEn,
       "pduMeanKVALCLTrapEn": pduMeanKVALCLTrapEn,
       "pduMeanKWattsUCLTrapEn": pduMeanKWattsUCLTrapEn,
       "pduMeanKWattsUWLTrapEn": pduMeanKWattsUWLTrapEn,
       "pduMeanKWattsLWLTrapEn": pduMeanKWattsLWLTrapEn,
       "pduMeanKWattsLCLTrapEn": pduMeanKWattsLCLTrapEn,
       "pduPwrFactorUTLTrapEn": pduPwrFactorUTLTrapEn,
       "pduPwrFactorLTLTrapEn": pduPwrFactorLTLTrapEn,
       "pduTrapPerTable": pduTrapPerTable,
       "pduTrapPerEntry": pduTrapPerEntry,
       "pduTrapPduNumber": pduTrapPduNumber,
       "pduTrapPerRS": pduTrapPerRS,
       "pduRMSVoltsUCLTrapPer": pduRMSVoltsUCLTrapPer,
       "pduRMSVoltsUWLTrapPer": pduRMSVoltsUWLTrapPer,
       "pduRMSVoltsLWLTrapPer": pduRMSVoltsLWLTrapPer,
       "pduRMSVoltsLCLTrapPer": pduRMSVoltsLCLTrapPer,
       "pduRMSAmpsUCLTrapPer": pduRMSAmpsUCLTrapPer,
       "pduRMSAmpsUWLTrapPer": pduRMSAmpsUWLTrapPer,
       "pduRMSAmpsLWLTrapPer": pduRMSAmpsLWLTrapPer,
       "pduRMSAmpsLCLTrapPer": pduRMSAmpsLCLTrapPer,
       "pduEnergyUCLTrapPer": pduEnergyUCLTrapPer,
       "pduEnergyUWLTrapPer": pduEnergyUWLTrapPer,
       "pduMeanKVAUCLTrapPer": pduMeanKVAUCLTrapPer,
       "pduMeanKVAUWLTrapPer": pduMeanKVAUWLTrapPer,
       "pduMeanKVALWLTrapPer": pduMeanKVALWLTrapPer,
       "pduMeanKVALCLTrapPer": pduMeanKVALCLTrapPer,
       "pduMeanKWattsUCLTrapPer": pduMeanKWattsUCLTrapPer,
       "pduMeanKWattsUWLTrapPer": pduMeanKWattsUWLTrapPer,
       "pduMeanKWattsLWLTrapPer": pduMeanKWattsLWLTrapPer,
       "pduMeanKWattsLCLTrapPer": pduMeanKWattsLCLTrapPer,
       "pduPwrFactorUTLTrapPer": pduPwrFactorUTLTrapPer,
       "pduPwrFactorLTLTrapPer": pduPwrFactorLTLTrapPer,
       "pduMon3PhTable": pduMon3PhTable,
       "pduMon3PhEntry": pduMon3PhEntry,
       "pdu3PhPduNumber": pdu3PhPduNumber,
       "pdu3PhRS": pdu3PhRS,
       "pdu3PhMode": pdu3PhMode,
       "pdu3PhVoltsC1": pdu3PhVoltsC1,
       "pdu3PhAmpsL1": pdu3PhAmpsL1,
       "pdu3PhVoltsC2": pdu3PhVoltsC2,
       "pdu3PhAmpsL2": pdu3PhAmpsL2,
       "pdu3PhVoltsC3": pdu3PhVoltsC3,
       "pdu3PhAmpsL3": pdu3PhAmpsL3,
       "pdu3PhAmpsAgg": pdu3PhAmpsAgg,
       "pdu3PhkVAAgg": pdu3PhkVAAgg,
       "pdu3PhkWAgg": pdu3PhkWAgg,
       "pdu3PhkVArhAgg": pdu3PhkVArhAgg,
       "pdu3PhkWhAgg": pdu3PhkWhAgg,
       "pduGangs": pduGangs,
       "pduGangsEnable": pduGangsEnable,
       "pduGangsSelect": pduGangsSelect,
       "pduGangsInsert": pduGangsInsert,
       "pduGangTable": pduGangTable,
       "pduGangEntry": pduGangEntry,
       "pduGangNumber": pduGangNumber,
       "pduGangRS": pduGangRS,
       "pduGangEn": pduGangEn,
       "pduGangName": pduGangName,
       "pduGangOn": pduGangOn,
       "pduGangPassword": pduGangPassword,
       "pduGangAbortTask": pduGangAbortTask,
       "pduGangMembers": pduGangMembers,
       "expansion": expansion,
       "expEnable": expEnable,
       "expSelect": expSelect,
       "expInsert": expInsert,
       "expTable": expTable,
       "expEntry": expEntry,
       "expNumber": expNumber,
       "expRS": expRS,
       "expName": expName,
       "expType": expType,
       "expCommsFail": expCommsFail,
       "clamp": clamp,
       "clampTable": clampTable,
       "clampEntry": clampEntry,
       "clampNumber": clampNumber,
       "clampRS": clampRS,
       "clampBValue": clampBValue,
       "clampVolts": clampVolts,
       "clampPwrFactor": clampPwrFactor,
       "clampFrequency": clampFrequency,
       "clampWriteParams": clampWriteParams,
       "idm": idm,
       "idmTable": idmTable,
       "idmEntry": idmEntry,
       "idmNumber": idmNumber,
       "idmRS": idmRS,
       "idmVersion": idmVersion,
       "idmStatus": idmStatus,
       "pdusP2": pdusP2,
       "pduP2BrCct": pduP2BrCct,
       "pduP2BrCctMonitorTable": pduP2BrCctMonitorTable,
       "pduP2BrCctMonitorEntry": pduP2BrCctMonitorEntry,
       "pduP2BrCktMonPduNumber": pduP2BrCktMonPduNumber,
       "pduP2BrCktMonBrCctNumber": pduP2BrCktMonBrCctNumber,
       "pduP2BrCktMonRS": pduP2BrCktMonRS,
       "pduP2BrCktMonBrCctID": pduP2BrCktMonBrCctID,
       "pduP2BrCktMonBrCctPhases": pduP2BrCktMonBrCctPhases,
       "pduP2BrCktMonBrCctCurrent": pduP2BrCktMonBrCctCurrent,
       "pduP2BrCktMonBrCctPeakCurrent": pduP2BrCktMonBrCctPeakCurrent,
       "pduP2BrCktMonBrCctPeakCurrentTimestamp": pduP2BrCktMonBrCctPeakCurrentTimestamp,
       "pduP2BrCktMonBrCctBreakerStatus": pduP2BrCktMonBrCctBreakerStatus,
       "pduP2BrCktMonBrCctBreakerConfig": pduP2BrCktMonBrCctBreakerConfig,
       "pduP2BrCktMonBrCctBreakerTripState": pduP2BrCktMonBrCctBreakerTripState,
       "pduP2BrCktMonBrCctBreakerContinuousLoadRatingAmps": pduP2BrCktMonBrCctBreakerContinuousLoadRatingAmps,
       "pduP2BrCktMonBrCctBreakerTripRatingAmps": pduP2BrCktMonBrCctBreakerTripRatingAmps,
       "pduP2BrCktMonBrCctBreakerOutletMap": pduP2BrCktMonBrCctBreakerOutletMap,
       "pduP2BrCktCircuitCurrentUCL": pduP2BrCktCircuitCurrentUCL,
       "pduP2BrCktCircuitCurrentUWL": pduP2BrCktCircuitCurrentUWL,
       "pduP2BrCktCircuitCurrentLWL": pduP2BrCktCircuitCurrentLWL,
       "pduP2BrCktCircuitCurrentLCL": pduP2BrCktCircuitCurrentLCL,
       "pduP2BrCktCircuitCurrentUCLTrapEn": pduP2BrCktCircuitCurrentUCLTrapEn,
       "pduP2BrCktCircuitCurrentUWLTrapEn": pduP2BrCktCircuitCurrentUWLTrapEn,
       "pduP2BrCktCircuitCurrentLWLTrapEn": pduP2BrCktCircuitCurrentLWLTrapEn,
       "pduP2BrCktCircuitCurrentLCLTrapEn": pduP2BrCktCircuitCurrentLCLTrapEn,
       "pduP2BrCktCircuitCurrentUCLTrapPer": pduP2BrCktCircuitCurrentUCLTrapPer,
       "pduP2BrCktCircuitCurrentUWLTrapPer": pduP2BrCktCircuitCurrentUWLTrapPer,
       "pduP2BrCktCircuitCurrentLWLTrapPer": pduP2BrCktCircuitCurrentLWLTrapPer,
       "pduP2BrCktCircuitCurrentLCLTrapPer": pduP2BrCktCircuitCurrentLCLTrapPer,
       "platformData": platformData,
       "platHwType": platHwType,
       "platFwRev": platFwRev,
       "platBootldrRev": platBootldrRev,
       "platModelName": platModelName,
       "inventory": inventory,
       "invProdSignature": invProdSignature,
       "invProdFormatVer": invProdFormatVer,
       "invManufCode": invManufCode,
       "invOrderNum": invOrderNum,
       "invBatchNum": invBatchNum,
       "invProdTestTime": invProdTestTime,
       "invUnitName": invUnitName,
       "invUnitPartNum": invUnitPartNum,
       "invHwRevision": invHwRevision,
       "invFwRevision": invFwRevision,
       "invSerialNum": invSerialNum,
       "invDefaultIPAddrType": invDefaultIPAddrType,
       "invDefaultIPAddr": invDefaultIPAddr,
       "invDefaultSubNetMask": invDefaultSubNetMask,
       "invDefaultGWAddr": invDefaultGWAddr,
       "invMacAddr": invMacAddr,
       "invOk": invOk,
       "invInputCount": invInputCount,
       "invOutputCount": invOutputCount,
       "invKeypadCount": invKeypadCount,
       "invAcuCount": invAcuCount,
       "invAccessUserCount": invAccessUserCount,
       "invPduCount": invPduCount,
       "trapInfo": trapInfo,
       "trapCode": trapCode,
       "trapDescription": trapDescription,
       "traps": traps,
       "alarmCritical": alarmCritical,
       "alarmWarning": alarmWarning,
       "alarmInformation": alarmInformation,
       "alarmCleared": alarmCleared,
       "v2": v2,
       "objects2": objects2,
       "pdus2": pdus2,
       "pdu2Common": pdu2Common,
       "pdu2Table": pdu2Table,
       "pdu2Entry": pdu2Entry,
       "pdu2PduNumber": pdu2PduNumber,
       "pdu2RS": pdu2RS,
       "pdu2WiringTopology": pdu2WiringTopology,
       "pdu2PhaseTopology": pdu2PhaseTopology,
       "pdu2CustDataTable": pdu2CustDataTable,
       "pdu2CustDataEntry": pdu2CustDataEntry,
       "pdu2CustDataPduNumber": pdu2CustDataPduNumber,
       "pdu2CustDataRS": pdu2CustDataRS,
       "pdu2CustDataMainCktRefOverall": pdu2CustDataMainCktRefOverall,
       "pdu2CustDataMainCktRefCktA": pdu2CustDataMainCktRefCktA,
       "pdu2CustDataMainCktRefCktB": pdu2CustDataMainCktRefCktB,
       "pdu2CustDataMainCktRefCktC": pdu2CustDataMainCktRefCktC,
       "pdu2InputAggregateTable": pdu2InputAggregateTable,
       "pdu2InputAggregateEntry": pdu2InputAggregateEntry,
       "pdu2IpAggPduNumber": pdu2IpAggPduNumber,
       "pdu2IpAggRS": pdu2IpAggRS,
       "pdu2IpAggAggregatekWh": pdu2IpAggAggregatekWh,
       "pdu2IpAggAggregatekVA": pdu2IpAggAggregatekVA,
       "pdu2IpAggAggregatekW": pdu2IpAggAggregatekW,
       "pdu2IpAggAggregatePF": pdu2IpAggAggregatePF,
       "pdu2IpAggAggregateCurrent": pdu2IpAggAggregateCurrent,
       "pdu2IpAggAggregateNeutralCurrent": pdu2IpAggAggregateNeutralCurrent,
       "pdu2IpAggAggregateEarthCurrent": pdu2IpAggAggregateEarthCurrent,
       "pdu2PhaseMonitorTable": pdu2PhaseMonitorTable,
       "pdu2PhaseMonitorEntry": pdu2PhaseMonitorEntry,
       "pdu2PhMonPduNumber": pdu2PhMonPduNumber,
       "pdu2PhMonPhaseNumber": pdu2PhMonPhaseNumber,
       "pdu2PhMonRS": pdu2PhMonRS,
       "pdu2PhMonLineID": pdu2PhMonLineID,
       "pdu2PhMonPhaseToNeutralVoltage": pdu2PhMonPhaseToNeutralVoltage,
       "pdu2PhMonPhaseCurrent": pdu2PhMonPhaseCurrent,
       "pdu2PhMonPhasekVA": pdu2PhMonPhasekVA,
       "pdu2PhMonPhasePeakkVA": pdu2PhMonPhasePeakkVA,
       "pdu2PhMonPhasePeakkVATimestamp": pdu2PhMonPhasePeakkVATimestamp,
       "pdu2PhMonPhasekW": pdu2PhMonPhasekW,
       "pdu2PhMonPhasePF": pdu2PhMonPhasePF,
       "pdu2PhMonPhasekWh": pdu2PhMonPhasekWh,
       "pdu2PhMonPhasekVAr": pdu2PhMonPhasekVAr,
       "pdu2PhMonPhaseCrestFactor": pdu2PhMonPhaseCrestFactor,
       "pdu2PhMonPhaseTHD": pdu2PhMonPhaseTHD,
       "pdu2CircuitMonitorTable": pdu2CircuitMonitorTable,
       "pdu2CircuitMonitorEntry": pdu2CircuitMonitorEntry,
       "pdu2CktMonPduNumber": pdu2CktMonPduNumber,
       "pdu2CktMonCircuitNumber": pdu2CktMonCircuitNumber,
       "pdu2CktMonRS": pdu2CktMonRS,
       "pdu2CktMonLineID": pdu2CktMonLineID,
       "pdu2CktMonLineToLineVoltage": pdu2CktMonLineToLineVoltage,
       "pdu2CktMonLineToLineCurrent": pdu2CktMonLineToLineCurrent,
       "pdu2CktMonLineToLineKVA": pdu2CktMonLineToLineKVA,
       "pdu2CktMonLineToLinePeakkVA": pdu2CktMonLineToLinePeakkVA,
       "pdu2CktMonLineToLinePeakkVATimestamp": pdu2CktMonLineToLinePeakkVATimestamp,
       "pdu2CktMonLineToLinekW": pdu2CktMonLineToLinekW,
       "pdu2CktMonLineToLinePF": pdu2CktMonLineToLinePF,
       "pdu2CktMonLineToLinekVAr": pdu2CktMonLineToLinekVAr,
       "pdu2BranchCircuitMonitorTable": pdu2BranchCircuitMonitorTable,
       "pdu2BranchCircuitMonitorEntry": pdu2BranchCircuitMonitorEntry,
       "pdu2BrCktMonPduNumber": pdu2BrCktMonPduNumber,
       "pdu2BrCktMonBranchCircuitNumber": pdu2BrCktMonBranchCircuitNumber,
       "pdu2BrCktMonRS": pdu2BrCktMonRS,
       "pdu2BrCktMonBranchCircuitID": pdu2BrCktMonBranchCircuitID,
       "pdu2BrCktMonBranchCircuitPhases": pdu2BrCktMonBranchCircuitPhases,
       "pdu2BrCktMonBranchCircuitCurrent": pdu2BrCktMonBranchCircuitCurrent,
       "pdu2BrCktMonBranchCircuitPeakCurrent": pdu2BrCktMonBranchCircuitPeakCurrent,
       "pdu2BrCktMonBranchCircuitPeakCurrentTimestamp": pdu2BrCktMonBranchCircuitPeakCurrentTimestamp,
       "pdu2BrCktMonBranchCircuitBreakerStatus": pdu2BrCktMonBranchCircuitBreakerStatus,
       "pdu2BrCktMonBranchCircuitBreakerConfig": pdu2BrCktMonBranchCircuitBreakerConfig,
       "pdu2BrCktMonBranchCircuitBreakerTripState": pdu2BrCktMonBranchCircuitBreakerTripState,
       "pdu2BrCktMonBranchCircuitBreakerContinuousLoadRatingAmps": pdu2BrCktMonBranchCircuitBreakerContinuousLoadRatingAmps,
       "pdu2BrCktMonBranchCircuitBreakerTripRatingAmps": pdu2BrCktMonBranchCircuitBreakerTripRatingAmps,
       "pdu2OutletMonitorTable": pdu2OutletMonitorTable,
       "pdu2OutletMonitorEntry": pdu2OutletMonitorEntry,
       "pdu2OutMonPduNumber": pdu2OutMonPduNumber,
       "pdu2OutMonOutletNumber": pdu2OutMonOutletNumber,
       "pdu2OutMonRS": pdu2OutMonRS,
       "pdu2OutMonOutletID": pdu2OutMonOutletID,
       "pdu2OutMonOutletVoltage": pdu2OutMonOutletVoltage,
       "pdu2OutMonOutletCurrent": pdu2OutMonOutletCurrent,
       "pdu2OutMonOutletkVA": pdu2OutMonOutletkVA,
       "pdu2OutMonOutletPeakkVA": pdu2OutMonOutletPeakkVA,
       "pdu2OutMonOutletPeakkVATimestamp": pdu2OutMonOutletPeakkVATimestamp,
       "pdu2OutMonOutletkW": pdu2OutMonOutletkW,
       "pdu2OutMonOutletPF": pdu2OutMonOutletPF,
       "pdu2OutMonOutletkWh": pdu2OutMonOutletkWh,
       "pdu2OutMonOutletBranchCircuitID": pdu2OutMonOutletBranchCircuitID,
       "pdu2OutMonOutletPhaseID": pdu2OutMonOutletPhaseID,
       "pdu2OutletControlTable": pdu2OutletControlTable,
       "pdu2OutletControlEntry": pdu2OutletControlEntry,
       "pdu2OutCtlPduNumber": pdu2OutCtlPduNumber,
       "pdu2OutCtlOutletNumber": pdu2OutCtlOutletNumber,
       "pdu2OutCtlRS": pdu2OutCtlRS,
       "pdu2OutCtlControlledOutletID": pdu2OutCtlControlledOutletID,
       "pdu2OutCtlControlledOutletState": pdu2OutCtlControlledOutletState,
       "pdu2OutCtlControlledOutletPowerUpState": pdu2OutCtlControlledOutletPowerUpState,
       "pdu2OutCtlControlledOutletPowerUpTimeDelay": pdu2OutCtlControlledOutletPowerUpTimeDelay,
       "pdu2BranchCircuitThreshTable": pdu2BranchCircuitThreshTable,
       "pdu2BranchCircuitThreshEntry": pdu2BranchCircuitThreshEntry,
       "pdu2BrCktThreshPduNumber": pdu2BrCktThreshPduNumber,
       "pdu2BrCktThreshBranchCircuitNumber": pdu2BrCktThreshBranchCircuitNumber,
       "pdu2BrCktThreshRS": pdu2BrCktThreshRS,
       "pdu2BrCktBranchCircuitCurrentUCL": pdu2BrCktBranchCircuitCurrentUCL,
       "pdu2BrCktBranchCircuitCurrentUWL": pdu2BrCktBranchCircuitCurrentUWL,
       "pdu2BrCktBranchCircuitCurrentLWL": pdu2BrCktBranchCircuitCurrentLWL,
       "pdu2BrCktBranchCircuitCurrentLCL": pdu2BrCktBranchCircuitCurrentLCL,
       "pdu2BranchCircuitTrapEnTable": pdu2BranchCircuitTrapEnTable,
       "pdu2BranchCircuitTrapEnEntry": pdu2BranchCircuitTrapEnEntry,
       "pdu2BrCktTrapEnPduNumber": pdu2BrCktTrapEnPduNumber,
       "pdu2BrCktTrapEnBranchCircuitNumber": pdu2BrCktTrapEnBranchCircuitNumber,
       "pdu2BrCktTrapEnRS": pdu2BrCktTrapEnRS,
       "pdu2BrCktBranchCircuitCurrentUCLTrapEn": pdu2BrCktBranchCircuitCurrentUCLTrapEn,
       "pdu2BrCktBranchCircuitCurrentUWLTrapEn": pdu2BrCktBranchCircuitCurrentUWLTrapEn,
       "pdu2BrCktBranchCircuitCurrentLWLTrapEn": pdu2BrCktBranchCircuitCurrentLWLTrapEn,
       "pdu2BrCktBranchCircuitCurrentLCLTrapEn": pdu2BrCktBranchCircuitCurrentLCLTrapEn,
       "pdu2BranchCircuitTrapPerTable": pdu2BranchCircuitTrapPerTable,
       "pdu2BranchCircuitTrapPerEntry": pdu2BranchCircuitTrapPerEntry,
       "pdu2BrCktTrapPerPduNumber": pdu2BrCktTrapPerPduNumber,
       "pdu2BrCktTrapPerBranchCircuitNumber": pdu2BrCktTrapPerBranchCircuitNumber,
       "pdu2BrCktTrapPerRS": pdu2BrCktTrapPerRS,
       "pdu2BrCktBranchCircuitCurrentUCLTrapPer": pdu2BrCktBranchCircuitCurrentUCLTrapPer,
       "pdu2BrCktBranchCircuitCurrentUWLTrapPer": pdu2BrCktBranchCircuitCurrentUWLTrapPer,
       "pdu2BrCktBranchCircuitCurrentLWLTrapPer": pdu2BrCktBranchCircuitCurrentLWLTrapPer,
       "pdu2BrCktBranchCircuitCurrentLCLTrapPer": pdu2BrCktBranchCircuitCurrentLCLTrapPer,
       "traps2": traps2}
)
