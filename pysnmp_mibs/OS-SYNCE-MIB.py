# SNMP MIB module (OS-SYNCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/OS-SYNCE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:04:19 2025
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

(oaOptiSwitch,) = mibBuilder.importSymbols(
    "OS-COMMON-TC-MIB",
    "oaOptiSwitch")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

osSyncEMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 23)
)
if mibBuilder.loadTexts:
    osSyncEMIB.setRevisions(
        ("2012-08-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OsSyncEMIBNotifs_ObjectIdentity = ObjectIdentity
osSyncEMIBNotifs = _OsSyncEMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 23, 0)
)
_OsSyncEMIBObjects_ObjectIdentity = ObjectIdentity
osSyncEMIBObjects = _OsSyncEMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 23, 1)
)
_OsSyncEMIBInfo_ObjectIdentity = ObjectIdentity
osSyncEMIBInfo = _OsSyncEMIBInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 23, 1, 1)
)
_OsSyncEMIBEventParams_ObjectIdentity = ObjectIdentity
osSyncEMIBEventParams = _OsSyncEMIBEventParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 23, 1, 1, 1)
)


class _OsSyncEEventDescription_Type(DisplayString):
    """Custom type osSyncEEventDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 120),
    )


_OsSyncEEventDescription_Type.__name__ = "DisplayString"
_OsSyncEEventDescription_Object = MibScalar
osSyncEEventDescription = _OsSyncEEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 23, 1, 1, 1, 1),
    _OsSyncEEventDescription_Type()
)
osSyncEEventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osSyncEEventDescription.setStatus("current")
_OsSyncEMIBCfg_ObjectIdentity = ObjectIdentity
osSyncEMIBCfg = _OsSyncEMIBCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 23, 1, 2)
)
_OsSyncEMIBCapabilities_ObjectIdentity = ObjectIdentity
osSyncEMIBCapabilities = _OsSyncEMIBCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 23, 1, 2, 1)
)


class _OsSyncEMIBSupport_Type(Integer32):
    """Custom type osSyncEMIBSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("supported", 2))
    )


_OsSyncEMIBSupport_Type.__name__ = "Integer32"
_OsSyncEMIBSupport_Object = MibScalar
osSyncEMIBSupport = _OsSyncEMIBSupport_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 23, 1, 2, 1, 1),
    _OsSyncEMIBSupport_Type()
)
osSyncEMIBSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osSyncEMIBSupport.setStatus("current")
_OsSyncEMIBCfgGen_ObjectIdentity = ObjectIdentity
osSyncEMIBCfgGen = _OsSyncEMIBCfgGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 23, 1, 2, 2)
)


class _OsSyncEStatus_Type(TruthValue):
    """Custom type osSyncEStatus based on TruthValue"""
    defaultValue = 2


_OsSyncEStatus_Type.__name__ = "TruthValue"
_OsSyncEStatus_Object = MibScalar
osSyncEStatus = _OsSyncEStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 23, 1, 2, 2, 1),
    _OsSyncEStatus_Type()
)
osSyncEStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osSyncEStatus.setStatus("current")


class _OsSyncET1CableType_Type(Integer32):
    """Custom type osSyncET1CableType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("lengthNotApplicable", 0),
          ("length0To133", 1),
          ("length134To266", 2),
          ("length267To399", 3),
          ("length400To533", 4),
          ("length534To655", 5),
          ("lboNeg7p5dB", 6),
          ("lboNeg15p0dB", 7),
          ("lboNeg22p5dB", 8))
    )


_OsSyncET1CableType_Type.__name__ = "Integer32"
_OsSyncET1CableType_Object = MibScalar
osSyncET1CableType = _OsSyncET1CableType_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 23, 1, 2, 2, 2),
    _OsSyncET1CableType_Type()
)
osSyncET1CableType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osSyncET1CableType.setStatus("current")


class _OsSyncEDs1e1Type_Type(Integer32):
    """Custom type osSyncEDs1e1Type based on Integer32"""
    defaultValue = 0

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
        *(("notSet", 0),
          ("square1544", 1),
          ("square2048", 2),
          ("typeE1", 3),
          ("typeJ1", 4),
          ("typeT1", 5))
    )


_OsSyncEDs1e1Type_Type.__name__ = "Integer32"
_OsSyncEDs1e1Type_Object = MibScalar
osSyncEDs1e1Type = _OsSyncEDs1e1Type_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 23, 1, 2, 2, 3),
    _OsSyncEDs1e1Type_Type()
)
osSyncEDs1e1Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osSyncEDs1e1Type.setStatus("current")


class _OsSyncEDs1e1Connect_Type(Integer32):
    """Custom type osSyncEDs1e1Connect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSet", 0),
          ("sec", 1),
          ("ssu", 2))
    )


_OsSyncEDs1e1Connect_Type.__name__ = "Integer32"
_OsSyncEDs1e1Connect_Object = MibScalar
osSyncEDs1e1Connect = _OsSyncEDs1e1Connect_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 23, 1, 2, 2, 4),
    _OsSyncEDs1e1Connect_Type()
)
osSyncEDs1e1Connect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osSyncEDs1e1Connect.setStatus("current")


class _OsSyncEFrequencyClkIn_Type(Integer32):
    """Custom type osSyncEFrequencyClkIn based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("notSet", 0),
          ("frequency1544KHz", 4),
          ("frequency2048KHz", 5),
          ("frequency6480KHz", 6),
          ("frequency19440KHz", 7))
    )


_OsSyncEFrequencyClkIn_Type.__name__ = "Integer32"
_OsSyncEFrequencyClkIn_Object = MibScalar
osSyncEFrequencyClkIn = _OsSyncEFrequencyClkIn_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 23, 1, 2, 2, 5),
    _OsSyncEFrequencyClkIn_Type()
)
osSyncEFrequencyClkIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osSyncEFrequencyClkIn.setStatus("current")


class _OsSyncEFrequencyClkOut_Type(Integer32):
    """Custom type osSyncEFrequencyClkOut based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("notSet", 0),
          ("frequency2KHz", 1),
          ("frequency4KHz", 2),
          ("frequency8KHz", 3),
          ("frequency1544KHz", 4),
          ("frequency2048KHz", 5),
          ("frequency6480KHz", 6),
          ("frequency19440KHz", 7),
          ("ptp", 8))
    )


_OsSyncEFrequencyClkOut_Type.__name__ = "Integer32"
_OsSyncEFrequencyClkOut_Object = MibScalar
osSyncEFrequencyClkOut = _OsSyncEFrequencyClkOut_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 23, 1, 2, 2, 6),
    _OsSyncEFrequencyClkOut_Type()
)
osSyncEFrequencyClkOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osSyncEFrequencyClkOut.setStatus("current")


class _OsSyncEFrequencyPtp_Type(Integer32):
    """Custom type osSyncEFrequencyPtp based on Integer32"""
    defaultValue = 0

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
        *(("notSet", 0),
          ("frequency1544KHz", 1),
          ("frequency2048KHz", 2),
          ("frequency6480KHz", 3),
          ("frequency19440KHz", 4))
    )


_OsSyncEFrequencyPtp_Type.__name__ = "Integer32"
_OsSyncEFrequencyPtp_Object = MibScalar
osSyncEFrequencyPtp = _OsSyncEFrequencyPtp_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 23, 1, 2, 2, 7),
    _OsSyncEFrequencyPtp_Type()
)
osSyncEFrequencyPtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osSyncEFrequencyPtp.setStatus("current")


class _OsSyncELineCode_Type(Integer32):
    """Custom type osSyncELineCode based on Integer32"""
    defaultValue = 0

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
        *(("notSet", 0),
          ("ami", 1),
          ("hdb3", 2),
          ("b8zs", 3))
    )


_OsSyncELineCode_Type.__name__ = "Integer32"
_OsSyncELineCode_Object = MibScalar
osSyncELineCode = _OsSyncELineCode_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 23, 1, 2, 2, 8),
    _OsSyncELineCode_Type()
)
osSyncELineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osSyncELineCode.setStatus("current")


class _OsSyncEFreeRunMode_Type(Integer32):
    """Custom type osSyncEFreeRunMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dnu", 1),
          ("eec", 2))
    )


_OsSyncEFreeRunMode_Type.__name__ = "Integer32"
_OsSyncEFreeRunMode_Object = MibScalar
osSyncEFreeRunMode = _OsSyncEFreeRunMode_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 23, 1, 2, 2, 9),
    _OsSyncEFreeRunMode_Type()
)
osSyncEFreeRunMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osSyncEFreeRunMode.setStatus("current")
_OsSyncEClockSourceTable_Object = MibTable
osSyncEClockSourceTable = _OsSyncEClockSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 23, 1, 2, 3)
)
if mibBuilder.loadTexts:
    osSyncEClockSourceTable.setStatus("current")
_OsSyncEClockSourceEntry_Object = MibTableRow
osSyncEClockSourceEntry = _OsSyncEClockSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 23, 1, 2, 3, 1)
)
osSyncEClockSourceEntry.setIndexNames(
    (0, "OS-SYNCE-MIB", "osSyncEClockSourceEntryId"),
)
if mibBuilder.loadTexts:
    osSyncEClockSourceEntry.setStatus("current")


class _OsSyncEClockSourceEntryId_Type(Integer32):
    """Custom type osSyncEClockSourceEntryId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OsSyncEClockSourceEntryId_Type.__name__ = "Integer32"
_OsSyncEClockSourceEntryId_Object = MibTableColumn
osSyncEClockSourceEntryId = _OsSyncEClockSourceEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 23, 1, 2, 3, 1, 1),
    _OsSyncEClockSourceEntryId_Type()
)
osSyncEClockSourceEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osSyncEClockSourceEntryId.setStatus("current")


class _OsSyncEClockSourceEntryType_Type(Integer32):
    """Custom type osSyncEClockSourceEntryType based on Integer32"""
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
        *(("clkIn", 1),
          ("ds1e1", 2),
          ("ptp", 3),
          ("ethPort", 4))
    )


_OsSyncEClockSourceEntryType_Type.__name__ = "Integer32"
_OsSyncEClockSourceEntryType_Object = MibTableColumn
osSyncEClockSourceEntryType = _OsSyncEClockSourceEntryType_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 23, 1, 2, 3, 1, 2),
    _OsSyncEClockSourceEntryType_Type()
)
osSyncEClockSourceEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osSyncEClockSourceEntryType.setStatus("current")


class _OsSyncEClockSourceEthPortNum_Type(Integer32):
    """Custom type osSyncEClockSourceEthPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OsSyncEClockSourceEthPortNum_Type.__name__ = "Integer32"
_OsSyncEClockSourceEthPortNum_Object = MibTableColumn
osSyncEClockSourceEthPortNum = _OsSyncEClockSourceEthPortNum_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 23, 1, 2, 3, 1, 3),
    _OsSyncEClockSourceEthPortNum_Type()
)
osSyncEClockSourceEthPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osSyncEClockSourceEthPortNum.setStatus("current")


class _OsSyncEClockSourceEthPriority_Type(Integer32):
    """Custom type osSyncEClockSourceEthPriority based on Integer32"""
    defaultValue = 127

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_OsSyncEClockSourceEthPriority_Type.__name__ = "Integer32"
_OsSyncEClockSourceEthPriority_Object = MibTableColumn
osSyncEClockSourceEthPriority = _OsSyncEClockSourceEthPriority_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 23, 1, 2, 3, 1, 4),
    _OsSyncEClockSourceEthPriority_Type()
)
osSyncEClockSourceEthPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osSyncEClockSourceEthPriority.setStatus("current")


class _OsSyncEClockSourceE1QL_Type(Integer32):
    """Custom type osSyncEClockSourceE1QL based on Integer32"""
    defaultValue = 127

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              8,
              11,
              15,
              127)
        )
    )
    namedValues = NamedValues(
        *(("prc", 2),
          ("ssuA", 4),
          ("ssuB", 8),
          ("eec1", 11),
          ("dnu", 15),
          ("notDefined", 127))
    )


_OsSyncEClockSourceE1QL_Type.__name__ = "Integer32"
_OsSyncEClockSourceE1QL_Object = MibTableColumn
osSyncEClockSourceE1QL = _OsSyncEClockSourceE1QL_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 23, 1, 2, 3, 1, 5),
    _OsSyncEClockSourceE1QL_Type()
)
osSyncEClockSourceE1QL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osSyncEClockSourceE1QL.setStatus("current")


class _OsSyncEClockSourceT1QL_Type(Integer32):
    """Custom type osSyncEClockSourceT1QL based on Integer32"""
    defaultValue = 127

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              7,
              10,
              13,
              14,
              15,
              127)
        )
    )
    namedValues = NamedValues(
        *(("stu", 0),
          ("prs", 1),
          ("tnc", 4),
          ("st2", 7),
          ("st3", 10),
          ("st3e", 13),
          ("prov", 14),
          ("dnu", 15),
          ("notDefined", 127))
    )


_OsSyncEClockSourceT1QL_Type.__name__ = "Integer32"
_OsSyncEClockSourceT1QL_Object = MibTableColumn
osSyncEClockSourceT1QL = _OsSyncEClockSourceT1QL_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 23, 1, 2, 3, 1, 6),
    _OsSyncEClockSourceT1QL_Type()
)
osSyncEClockSourceT1QL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osSyncEClockSourceT1QL.setStatus("current")


class _OsSyncEClockSourceJ1QL_Type(Integer32):
    """Custom type osSyncEClockSourceJ1QL based on Integer32"""
    defaultValue = 127

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              11,
              127)
        )
    )
    namedValues = NamedValues(
        *(("unk", 0),
          ("eec1", 11),
          ("notDefined", 127))
    )


_OsSyncEClockSourceJ1QL_Type.__name__ = "Integer32"
_OsSyncEClockSourceJ1QL_Object = MibTableColumn
osSyncEClockSourceJ1QL = _OsSyncEClockSourceJ1QL_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 23, 1, 2, 3, 1, 7),
    _OsSyncEClockSourceJ1QL_Type()
)
osSyncEClockSourceJ1QL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osSyncEClockSourceJ1QL.setStatus("current")
_OsSyncEMIBConformance_ObjectIdentity = ObjectIdentity
osSyncEMIBConformance = _OsSyncEMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 23, 101)
)
_OsSyncEMIBCompliances_ObjectIdentity = ObjectIdentity
osSyncEMIBCompliances = _OsSyncEMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 23, 101, 1)
)
_OsSyncEMIBGroups_ObjectIdentity = ObjectIdentity
osSyncEMIBGroups = _OsSyncEMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 23, 101, 2)
)

# Managed Objects groups

osSyncEMibMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 2, 23, 101, 2, 1)
)
osSyncEMibMandatoryGroup.setObjects(
      *(("OS-SYNCE-MIB", "osSyncEMIBSupport"),
        ("OS-SYNCE-MIB", "osSyncEStatus"),
        ("OS-SYNCE-MIB", "osSyncET1CableType"),
        ("OS-SYNCE-MIB", "osSyncEDs1e1Type"),
        ("OS-SYNCE-MIB", "osSyncEDs1e1Connect"),
        ("OS-SYNCE-MIB", "osSyncEFrequencyClkIn"),
        ("OS-SYNCE-MIB", "osSyncEFrequencyClkOut"),
        ("OS-SYNCE-MIB", "osSyncEFrequencyPtp"),
        ("OS-SYNCE-MIB", "osSyncELineCode"),
        ("OS-SYNCE-MIB", "osSyncEFreeRunMode"),
        ("OS-SYNCE-MIB", "osSyncEEventDescription"),
        ("OS-SYNCE-MIB", "osSyncEClockSourceEntryType"),
        ("OS-SYNCE-MIB", "osSyncEClockSourceEthPortNum"),
        ("OS-SYNCE-MIB", "osSyncEClockSourceEthPriority"),
        ("OS-SYNCE-MIB", "osSyncEClockSourceE1QL"),
        ("OS-SYNCE-MIB", "osSyncEClockSourceT1QL"),
        ("OS-SYNCE-MIB", "osSyncEClockSourceJ1QL"))
)
if mibBuilder.loadTexts:
    osSyncEMibMandatoryGroup.setStatus("current")


# Notification objects

osSyncEClockAlarmLock = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 2, 23, 0, 1)
)
osSyncEClockAlarmLock.setObjects(
    ("OS-SYNCE-MIB", "osSyncEClockSourceEntryType")
)
if mibBuilder.loadTexts:
    osSyncEClockAlarmLock.setStatus(
        "current"
    )

osSyncEClockAlarmUnLock = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 2, 23, 0, 2)
)
osSyncEClockAlarmUnLock.setObjects(
    ("OS-SYNCE-MIB", "osSyncEClockSourceEntryType")
)
if mibBuilder.loadTexts:
    osSyncEClockAlarmUnLock.setStatus(
        "current"
    )

osSyncEPtpAlarmLock = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 2, 23, 0, 3)
)
osSyncEPtpAlarmLock.setObjects(
    ("OS-SYNCE-MIB", "osSyncEEventDescription")
)
if mibBuilder.loadTexts:
    osSyncEPtpAlarmLock.setStatus(
        "current"
    )

osSyncEPtpAlarmUnLock = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 2, 23, 0, 4)
)
osSyncEPtpAlarmUnLock.setObjects(
    ("OS-SYNCE-MIB", "osSyncEEventDescription")
)
if mibBuilder.loadTexts:
    osSyncEPtpAlarmUnLock.setStatus(
        "current"
    )


# Notifications groups

osSyncEMIBNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6926, 2, 23, 101, 2, 2)
)
osSyncEMIBNotificationsGroup.setObjects(
      *(("OS-SYNCE-MIB", "osSyncEClockAlarmLock"),
        ("OS-SYNCE-MIB", "osSyncEClockAlarmUnLock"),
        ("OS-SYNCE-MIB", "osSyncEPtpAlarmLock"),
        ("OS-SYNCE-MIB", "osSyncEPtpAlarmUnLock"))
)
if mibBuilder.loadTexts:
    osSyncEMIBNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

osSyncEMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6926, 2, 23, 101, 1, 1)
)
osSyncEMIBCompliance.setObjects(
      *(("OS-SYNCE-MIB", "osSyncEMibMandatoryGroup"),
        ("OS-SYNCE-MIB", "osSyncEMIBNotificationsGroup"))
)
if mibBuilder.loadTexts:
    osSyncEMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OS-SYNCE-MIB",
    **{"osSyncEMIB": osSyncEMIB,
       "osSyncEMIBNotifs": osSyncEMIBNotifs,
       "osSyncEClockAlarmLock": osSyncEClockAlarmLock,
       "osSyncEClockAlarmUnLock": osSyncEClockAlarmUnLock,
       "osSyncEPtpAlarmLock": osSyncEPtpAlarmLock,
       "osSyncEPtpAlarmUnLock": osSyncEPtpAlarmUnLock,
       "osSyncEMIBObjects": osSyncEMIBObjects,
       "osSyncEMIBInfo": osSyncEMIBInfo,
       "osSyncEMIBEventParams": osSyncEMIBEventParams,
       "osSyncEEventDescription": osSyncEEventDescription,
       "osSyncEMIBCfg": osSyncEMIBCfg,
       "osSyncEMIBCapabilities": osSyncEMIBCapabilities,
       "osSyncEMIBSupport": osSyncEMIBSupport,
       "osSyncEMIBCfgGen": osSyncEMIBCfgGen,
       "osSyncEStatus": osSyncEStatus,
       "osSyncET1CableType": osSyncET1CableType,
       "osSyncEDs1e1Type": osSyncEDs1e1Type,
       "osSyncEDs1e1Connect": osSyncEDs1e1Connect,
       "osSyncEFrequencyClkIn": osSyncEFrequencyClkIn,
       "osSyncEFrequencyClkOut": osSyncEFrequencyClkOut,
       "osSyncEFrequencyPtp": osSyncEFrequencyPtp,
       "osSyncELineCode": osSyncELineCode,
       "osSyncEFreeRunMode": osSyncEFreeRunMode,
       "osSyncEClockSourceTable": osSyncEClockSourceTable,
       "osSyncEClockSourceEntry": osSyncEClockSourceEntry,
       "osSyncEClockSourceEntryId": osSyncEClockSourceEntryId,
       "osSyncEClockSourceEntryType": osSyncEClockSourceEntryType,
       "osSyncEClockSourceEthPortNum": osSyncEClockSourceEthPortNum,
       "osSyncEClockSourceEthPriority": osSyncEClockSourceEthPriority,
       "osSyncEClockSourceE1QL": osSyncEClockSourceE1QL,
       "osSyncEClockSourceT1QL": osSyncEClockSourceT1QL,
       "osSyncEClockSourceJ1QL": osSyncEClockSourceJ1QL,
       "osSyncEMIBConformance": osSyncEMIBConformance,
       "osSyncEMIBCompliances": osSyncEMIBCompliances,
       "osSyncEMIBCompliance": osSyncEMIBCompliance,
       "osSyncEMIBGroups": osSyncEMIBGroups,
       "osSyncEMibMandatoryGroup": osSyncEMibMandatoryGroup,
       "osSyncEMIBNotificationsGroup": osSyncEMIBNotificationsGroup}
)
