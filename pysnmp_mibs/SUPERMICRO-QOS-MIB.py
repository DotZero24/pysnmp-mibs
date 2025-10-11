# SNMP MIB module (SUPERMICRO-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-QOS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:02:18 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fsQoSMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6)
)
if mibBuilder.loadTexts:
    fsQoSMib.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Dscp(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )



class MeterColorMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("colorAware", 1),
          ("colorBlind", 2))
    )



class MeterType(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("simpleTokenBucket", 1),
          ("avgRate", 2),
          ("srTCM", 3),
          ("trTCM", 4),
          ("tswTCM", 5),
          ("mefDecoupledMeter", 6),
          ("mefCoupledMeter", 7))
    )



class EnableStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )



class SchedulerPriority(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )



class IndexInteger(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_FsQoSMIBObjects_ObjectIdentity = ObjectIdentity
fsQoSMIBObjects = _FsQoSMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1)
)
_FsQoSSystem_ObjectIdentity = ObjectIdentity
fsQoSSystem = _FsQoSSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 1)
)


class _FsQoSSystemControl_Type(Integer32):
    """Custom type fsQoSSystemControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("shutdown", 0),
          ("start", 1))
    )


_FsQoSSystemControl_Type.__name__ = "Integer32"
_FsQoSSystemControl_Object = MibScalar
fsQoSSystemControl = _FsQoSSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 1, 1),
    _FsQoSSystemControl_Type()
)
fsQoSSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSSystemControl.setStatus("current")


class _FsQoSStatus_Type(Integer32):
    """Custom type fsQoSStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_FsQoSStatus_Type.__name__ = "Integer32"
_FsQoSStatus_Object = MibScalar
fsQoSStatus = _FsQoSStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 1, 2),
    _FsQoSStatus_Type()
)
fsQoSStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSStatus.setStatus("current")


class _FsQoSTrcFlag_Type(Unsigned32):
    """Custom type fsQoSTrcFlag based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsQoSTrcFlag_Type.__name__ = "Unsigned32"
_FsQoSTrcFlag_Object = MibScalar
fsQoSTrcFlag = _FsQoSTrcFlag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 1, 3),
    _FsQoSTrcFlag_Type()
)
fsQoSTrcFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSTrcFlag.setStatus("current")


class _FsQoSRateUnit_Type(Integer32):
    """Custom type fsQoSRateUnit based on Integer32"""
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
        *(("bps", 1),
          ("kbps", 2),
          ("mbps", 3),
          ("gbps", 4))
    )


_FsQoSRateUnit_Type.__name__ = "Integer32"
_FsQoSRateUnit_Object = MibScalar
fsQoSRateUnit = _FsQoSRateUnit_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 1, 4),
    _FsQoSRateUnit_Type()
)
fsQoSRateUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQoSRateUnit.setStatus("current")
_FsQoSRateGranularity_Type = Unsigned32
_FsQoSRateGranularity_Object = MibScalar
fsQoSRateGranularity = _FsQoSRateGranularity_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 1, 5),
    _FsQoSRateGranularity_Type()
)
fsQoSRateGranularity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQoSRateGranularity.setStatus("current")
_FsQoSClass_ObjectIdentity = ObjectIdentity
fsQoSClass = _FsQoSClass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 2)
)
_FsQoSPriorityMapTable_Object = MibTable
fsQoSPriorityMapTable = _FsQoSPriorityMapTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fsQoSPriorityMapTable.setStatus("current")
_FsQoSPriorityMapEntry_Object = MibTableRow
fsQoSPriorityMapEntry = _FsQoSPriorityMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 2, 1, 1)
)
fsQoSPriorityMapEntry.setIndexNames(
    (0, "SUPERMICRO-QOS-MIB", "fsQoSPriorityMapID"),
)
if mibBuilder.loadTexts:
    fsQoSPriorityMapEntry.setStatus("current")
_FsQoSPriorityMapID_Type = IndexInteger
_FsQoSPriorityMapID_Object = MibTableColumn
fsQoSPriorityMapID = _FsQoSPriorityMapID_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 2, 1, 1, 1),
    _FsQoSPriorityMapID_Type()
)
fsQoSPriorityMapID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsQoSPriorityMapID.setStatus("current")


class _FsQoSPriorityMapName_Type(DisplayString):
    """Custom type fsQoSPriorityMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_FsQoSPriorityMapName_Type.__name__ = "DisplayString"
_FsQoSPriorityMapName_Object = MibTableColumn
fsQoSPriorityMapName = _FsQoSPriorityMapName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 2, 1, 1, 2),
    _FsQoSPriorityMapName_Type()
)
fsQoSPriorityMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPriorityMapName.setStatus("current")


class _FsQoSPriorityMapIfIndex_Type(Unsigned32):
    """Custom type fsQoSPriorityMapIfIndex based on Unsigned32"""
    defaultValue = 0


_FsQoSPriorityMapIfIndex_Type.__name__ = "Unsigned32"
_FsQoSPriorityMapIfIndex_Object = MibTableColumn
fsQoSPriorityMapIfIndex = _FsQoSPriorityMapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 2, 1, 1, 3),
    _FsQoSPriorityMapIfIndex_Type()
)
fsQoSPriorityMapIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPriorityMapIfIndex.setStatus("current")


class _FsQoSPriorityMapVlanId_Type(Unsigned32):
    """Custom type fsQoSPriorityMapVlanId based on Unsigned32"""
    defaultValue = 0


_FsQoSPriorityMapVlanId_Type.__name__ = "Unsigned32"
_FsQoSPriorityMapVlanId_Object = MibTableColumn
fsQoSPriorityMapVlanId = _FsQoSPriorityMapVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 2, 1, 1, 4),
    _FsQoSPriorityMapVlanId_Type()
)
fsQoSPriorityMapVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPriorityMapVlanId.setStatus("current")


class _FsQoSPriorityMapInPriority_Type(Integer32):
    """Custom type fsQoSPriorityMapInPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_FsQoSPriorityMapInPriority_Type.__name__ = "Integer32"
_FsQoSPriorityMapInPriority_Object = MibTableColumn
fsQoSPriorityMapInPriority = _FsQoSPriorityMapInPriority_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 2, 1, 1, 5),
    _FsQoSPriorityMapInPriority_Type()
)
fsQoSPriorityMapInPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPriorityMapInPriority.setStatus("current")


class _FsQoSPriorityMapInPriType_Type(Integer32):
    """Custom type fsQoSPriorityMapInPriType based on Integer32"""
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
        *(("vlanPri", 0),
          ("ipTos", 1),
          ("ipDscp", 2),
          ("mplsExp", 3),
          ("vlanDEI", 4))
    )


_FsQoSPriorityMapInPriType_Type.__name__ = "Integer32"
_FsQoSPriorityMapInPriType_Object = MibTableColumn
fsQoSPriorityMapInPriType = _FsQoSPriorityMapInPriType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 2, 1, 1, 6),
    _FsQoSPriorityMapInPriType_Type()
)
fsQoSPriorityMapInPriType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPriorityMapInPriType.setStatus("current")


class _FsQoSPriorityMapRegenPriority_Type(Unsigned32):
    """Custom type fsQoSPriorityMapRegenPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_FsQoSPriorityMapRegenPriority_Type.__name__ = "Unsigned32"
_FsQoSPriorityMapRegenPriority_Object = MibTableColumn
fsQoSPriorityMapRegenPriority = _FsQoSPriorityMapRegenPriority_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 2, 1, 1, 7),
    _FsQoSPriorityMapRegenPriority_Type()
)
fsQoSPriorityMapRegenPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPriorityMapRegenPriority.setStatus("current")


class _FsQoSPriorityMapRegenInnerPriority_Type(Unsigned32):
    """Custom type fsQoSPriorityMapRegenInnerPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_FsQoSPriorityMapRegenInnerPriority_Type.__name__ = "Unsigned32"
_FsQoSPriorityMapRegenInnerPriority_Object = MibTableColumn
fsQoSPriorityMapRegenInnerPriority = _FsQoSPriorityMapRegenInnerPriority_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 2, 1, 1, 8),
    _FsQoSPriorityMapRegenInnerPriority_Type()
)
fsQoSPriorityMapRegenInnerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPriorityMapRegenInnerPriority.setStatus("current")


class _FsQoSPriorityMapConfigStatus_Type(Integer32):
    """Custom type fsQoSPriorityMapConfigStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sysdefault", 1),
          ("management", 2))
    )


_FsQoSPriorityMapConfigStatus_Type.__name__ = "Integer32"
_FsQoSPriorityMapConfigStatus_Object = MibTableColumn
fsQoSPriorityMapConfigStatus = _FsQoSPriorityMapConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 2, 1, 1, 9),
    _FsQoSPriorityMapConfigStatus_Type()
)
fsQoSPriorityMapConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQoSPriorityMapConfigStatus.setStatus("current")
_FsQoSPriorityMapStatus_Type = RowStatus
_FsQoSPriorityMapStatus_Object = MibTableColumn
fsQoSPriorityMapStatus = _FsQoSPriorityMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 2, 1, 1, 10),
    _FsQoSPriorityMapStatus_Type()
)
fsQoSPriorityMapStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsQoSPriorityMapStatus.setStatus("current")
_FsQoSClassMapTable_Object = MibTable
fsQoSClassMapTable = _FsQoSClassMapTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 2, 2)
)
if mibBuilder.loadTexts:
    fsQoSClassMapTable.setStatus("current")
_FsQoSClassMapEntry_Object = MibTableRow
fsQoSClassMapEntry = _FsQoSClassMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 2, 2, 1)
)
fsQoSClassMapEntry.setIndexNames(
    (0, "SUPERMICRO-QOS-MIB", "fsQoSClassMapId"),
)
if mibBuilder.loadTexts:
    fsQoSClassMapEntry.setStatus("current")
_FsQoSClassMapId_Type = IndexInteger
_FsQoSClassMapId_Object = MibTableColumn
fsQoSClassMapId = _FsQoSClassMapId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 2, 2, 1, 1),
    _FsQoSClassMapId_Type()
)
fsQoSClassMapId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsQoSClassMapId.setStatus("current")


class _FsQoSClassMapName_Type(DisplayString):
    """Custom type fsQoSClassMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_FsQoSClassMapName_Type.__name__ = "DisplayString"
_FsQoSClassMapName_Object = MibTableColumn
fsQoSClassMapName = _FsQoSClassMapName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 2, 2, 1, 2),
    _FsQoSClassMapName_Type()
)
fsQoSClassMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSClassMapName.setStatus("current")


class _FsQoSClassMapL2FilterId_Type(Unsigned32):
    """Custom type fsQoSClassMapL2FilterId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsQoSClassMapL2FilterId_Type.__name__ = "Unsigned32"
_FsQoSClassMapL2FilterId_Object = MibTableColumn
fsQoSClassMapL2FilterId = _FsQoSClassMapL2FilterId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 2, 2, 1, 3),
    _FsQoSClassMapL2FilterId_Type()
)
fsQoSClassMapL2FilterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSClassMapL2FilterId.setStatus("current")


class _FsQoSClassMapL3FilterId_Type(Unsigned32):
    """Custom type fsQoSClassMapL3FilterId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsQoSClassMapL3FilterId_Type.__name__ = "Unsigned32"
_FsQoSClassMapL3FilterId_Object = MibTableColumn
fsQoSClassMapL3FilterId = _FsQoSClassMapL3FilterId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 2, 2, 1, 4),
    _FsQoSClassMapL3FilterId_Type()
)
fsQoSClassMapL3FilterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSClassMapL3FilterId.setStatus("current")


class _FsQoSClassMapPriorityMapId_Type(Unsigned32):
    """Custom type fsQoSClassMapPriorityMapId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsQoSClassMapPriorityMapId_Type.__name__ = "Unsigned32"
_FsQoSClassMapPriorityMapId_Object = MibTableColumn
fsQoSClassMapPriorityMapId = _FsQoSClassMapPriorityMapId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 2, 2, 1, 5),
    _FsQoSClassMapPriorityMapId_Type()
)
fsQoSClassMapPriorityMapId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSClassMapPriorityMapId.setStatus("current")


class _FsQoSClassMapCLASS_Type(Unsigned32):
    """Custom type fsQoSClassMapCLASS based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsQoSClassMapCLASS_Type.__name__ = "Unsigned32"
_FsQoSClassMapCLASS_Object = MibTableColumn
fsQoSClassMapCLASS = _FsQoSClassMapCLASS_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 2, 2, 1, 6),
    _FsQoSClassMapCLASS_Type()
)
fsQoSClassMapCLASS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSClassMapCLASS.setStatus("current")


class _FsQoSClassMapClfrId_Type(Unsigned32):
    """Custom type fsQoSClassMapClfrId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsQoSClassMapClfrId_Type.__name__ = "Unsigned32"
_FsQoSClassMapClfrId_Object = MibTableColumn
fsQoSClassMapClfrId = _FsQoSClassMapClfrId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 2, 2, 1, 7),
    _FsQoSClassMapClfrId_Type()
)
fsQoSClassMapClfrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSClassMapClfrId.setStatus("current")


class _FsQoSClassMapPreColor_Type(Integer32):
    """Custom type fsQoSClassMapPreColor based on Integer32"""
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
        *(("none", 0),
          ("green", 1),
          ("yellow", 2),
          ("red", 3))
    )


_FsQoSClassMapPreColor_Type.__name__ = "Integer32"
_FsQoSClassMapPreColor_Object = MibTableColumn
fsQoSClassMapPreColor = _FsQoSClassMapPreColor_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 2, 2, 1, 8),
    _FsQoSClassMapPreColor_Type()
)
fsQoSClassMapPreColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSClassMapPreColor.setStatus("current")
_FsQoSClassMapStatus_Type = RowStatus
_FsQoSClassMapStatus_Object = MibTableColumn
fsQoSClassMapStatus = _FsQoSClassMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 2, 2, 1, 9),
    _FsQoSClassMapStatus_Type()
)
fsQoSClassMapStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsQoSClassMapStatus.setStatus("current")
_FsQoSClassToPriorityTable_Object = MibTable
fsQoSClassToPriorityTable = _FsQoSClassToPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 2, 3)
)
if mibBuilder.loadTexts:
    fsQoSClassToPriorityTable.setStatus("current")
_FsQoSClassToPriorityEntry_Object = MibTableRow
fsQoSClassToPriorityEntry = _FsQoSClassToPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 2, 3, 1)
)
fsQoSClassToPriorityEntry.setIndexNames(
    (0, "SUPERMICRO-QOS-MIB", "fsQoSClassToPriorityCLASS"),
)
if mibBuilder.loadTexts:
    fsQoSClassToPriorityEntry.setStatus("current")
_FsQoSClassToPriorityCLASS_Type = IndexInteger
_FsQoSClassToPriorityCLASS_Object = MibTableColumn
fsQoSClassToPriorityCLASS = _FsQoSClassToPriorityCLASS_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 2, 3, 1, 1),
    _FsQoSClassToPriorityCLASS_Type()
)
fsQoSClassToPriorityCLASS.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsQoSClassToPriorityCLASS.setStatus("current")


class _FsQoSClassToPriorityRegenPri_Type(Unsigned32):
    """Custom type fsQoSClassToPriorityRegenPri based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsQoSClassToPriorityRegenPri_Type.__name__ = "Unsigned32"
_FsQoSClassToPriorityRegenPri_Object = MibTableColumn
fsQoSClassToPriorityRegenPri = _FsQoSClassToPriorityRegenPri_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 2, 3, 1, 2),
    _FsQoSClassToPriorityRegenPri_Type()
)
fsQoSClassToPriorityRegenPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSClassToPriorityRegenPri.setStatus("current")


class _FsQoSClassToPriorityGroupName_Type(DisplayString):
    """Custom type fsQoSClassToPriorityGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_FsQoSClassToPriorityGroupName_Type.__name__ = "DisplayString"
_FsQoSClassToPriorityGroupName_Object = MibTableColumn
fsQoSClassToPriorityGroupName = _FsQoSClassToPriorityGroupName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 2, 3, 1, 3),
    _FsQoSClassToPriorityGroupName_Type()
)
fsQoSClassToPriorityGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSClassToPriorityGroupName.setStatus("current")
_FsQoSClassToPriorityStatus_Type = RowStatus
_FsQoSClassToPriorityStatus_Object = MibTableColumn
fsQoSClassToPriorityStatus = _FsQoSClassToPriorityStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 2, 3, 1, 4),
    _FsQoSClassToPriorityStatus_Type()
)
fsQoSClassToPriorityStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsQoSClassToPriorityStatus.setStatus("current")
_FsQoSPolicy_ObjectIdentity = ObjectIdentity
fsQoSPolicy = _FsQoSPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3)
)
_FsQoSMeterTable_Object = MibTable
fsQoSMeterTable = _FsQoSMeterTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 1)
)
if mibBuilder.loadTexts:
    fsQoSMeterTable.setStatus("current")
_FsQoSMeterEntry_Object = MibTableRow
fsQoSMeterEntry = _FsQoSMeterEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 1, 1)
)
fsQoSMeterEntry.setIndexNames(
    (0, "SUPERMICRO-QOS-MIB", "fsQoSMeterId"),
)
if mibBuilder.loadTexts:
    fsQoSMeterEntry.setStatus("current")
_FsQoSMeterId_Type = IndexInteger
_FsQoSMeterId_Object = MibTableColumn
fsQoSMeterId = _FsQoSMeterId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 1, 1, 1),
    _FsQoSMeterId_Type()
)
fsQoSMeterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsQoSMeterId.setStatus("current")


class _FsQoSMeterName_Type(DisplayString):
    """Custom type fsQoSMeterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_FsQoSMeterName_Type.__name__ = "DisplayString"
_FsQoSMeterName_Object = MibTableColumn
fsQoSMeterName = _FsQoSMeterName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 1, 1, 2),
    _FsQoSMeterName_Type()
)
fsQoSMeterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSMeterName.setStatus("current")
_FsQoSMeterType_Type = MeterType
_FsQoSMeterType_Object = MibTableColumn
fsQoSMeterType = _FsQoSMeterType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 1, 1, 3),
    _FsQoSMeterType_Type()
)
fsQoSMeterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSMeterType.setStatus("current")


class _FsQoSMeterInterval_Type(Unsigned32):
    """Custom type fsQoSMeterInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_FsQoSMeterInterval_Type.__name__ = "Unsigned32"
_FsQoSMeterInterval_Object = MibTableColumn
fsQoSMeterInterval = _FsQoSMeterInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 1, 1, 4),
    _FsQoSMeterInterval_Type()
)
fsQoSMeterInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSMeterInterval.setStatus("current")
if mibBuilder.loadTexts:
    fsQoSMeterInterval.setUnits("microseconds")


class _FsQoSMeterColorMode_Type(MeterColorMode):
    """Custom type fsQoSMeterColorMode based on MeterColorMode"""
    defaultValue = 2


_FsQoSMeterColorMode_Type.__name__ = "MeterColorMode"
_FsQoSMeterColorMode_Object = MibTableColumn
fsQoSMeterColorMode = _FsQoSMeterColorMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 1, 1, 5),
    _FsQoSMeterColorMode_Type()
)
fsQoSMeterColorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSMeterColorMode.setStatus("current")


class _FsQoSMeterCIR_Type(Unsigned32):
    """Custom type fsQoSMeterCIR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsQoSMeterCIR_Type.__name__ = "Unsigned32"
_FsQoSMeterCIR_Object = MibTableColumn
fsQoSMeterCIR = _FsQoSMeterCIR_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 1, 1, 6),
    _FsQoSMeterCIR_Type()
)
fsQoSMeterCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSMeterCIR.setStatus("current")


class _FsQoSMeterCBS_Type(Unsigned32):
    """Custom type fsQoSMeterCBS based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsQoSMeterCBS_Type.__name__ = "Unsigned32"
_FsQoSMeterCBS_Object = MibTableColumn
fsQoSMeterCBS = _FsQoSMeterCBS_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 1, 1, 7),
    _FsQoSMeterCBS_Type()
)
fsQoSMeterCBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSMeterCBS.setStatus("current")
if mibBuilder.loadTexts:
    fsQoSMeterCBS.setUnits("Bytes")


class _FsQoSMeterEIR_Type(Unsigned32):
    """Custom type fsQoSMeterEIR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsQoSMeterEIR_Type.__name__ = "Unsigned32"
_FsQoSMeterEIR_Object = MibTableColumn
fsQoSMeterEIR = _FsQoSMeterEIR_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 1, 1, 8),
    _FsQoSMeterEIR_Type()
)
fsQoSMeterEIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSMeterEIR.setStatus("current")


class _FsQoSMeterEBS_Type(Unsigned32):
    """Custom type fsQoSMeterEBS based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsQoSMeterEBS_Type.__name__ = "Unsigned32"
_FsQoSMeterEBS_Object = MibTableColumn
fsQoSMeterEBS = _FsQoSMeterEBS_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 1, 1, 9),
    _FsQoSMeterEBS_Type()
)
fsQoSMeterEBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSMeterEBS.setStatus("current")
if mibBuilder.loadTexts:
    fsQoSMeterEBS.setUnits("Bytes")


class _FsQoSMeterNext_Type(Unsigned32):
    """Custom type fsQoSMeterNext based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsQoSMeterNext_Type.__name__ = "Unsigned32"
_FsQoSMeterNext_Object = MibTableColumn
fsQoSMeterNext = _FsQoSMeterNext_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 1, 1, 10),
    _FsQoSMeterNext_Type()
)
fsQoSMeterNext.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSMeterNext.setStatus("current")
_FsQoSMeterStatus_Type = RowStatus
_FsQoSMeterStatus_Object = MibTableColumn
fsQoSMeterStatus = _FsQoSMeterStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 1, 1, 11),
    _FsQoSMeterStatus_Type()
)
fsQoSMeterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsQoSMeterStatus.setStatus("current")
_FsQoSPolicyMapTable_Object = MibTable
fsQoSPolicyMapTable = _FsQoSPolicyMapTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 2)
)
if mibBuilder.loadTexts:
    fsQoSPolicyMapTable.setStatus("current")
_FsQoSPolicyMapEntry_Object = MibTableRow
fsQoSPolicyMapEntry = _FsQoSPolicyMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 2, 1)
)
fsQoSPolicyMapEntry.setIndexNames(
    (0, "SUPERMICRO-QOS-MIB", "fsQoSPolicyMapId"),
)
if mibBuilder.loadTexts:
    fsQoSPolicyMapEntry.setStatus("current")
_FsQoSPolicyMapId_Type = IndexInteger
_FsQoSPolicyMapId_Object = MibTableColumn
fsQoSPolicyMapId = _FsQoSPolicyMapId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 2, 1, 1),
    _FsQoSPolicyMapId_Type()
)
fsQoSPolicyMapId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsQoSPolicyMapId.setStatus("current")


class _FsQoSPolicyMapName_Type(DisplayString):
    """Custom type fsQoSPolicyMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_FsQoSPolicyMapName_Type.__name__ = "DisplayString"
_FsQoSPolicyMapName_Object = MibTableColumn
fsQoSPolicyMapName = _FsQoSPolicyMapName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 2, 1, 2),
    _FsQoSPolicyMapName_Type()
)
fsQoSPolicyMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPolicyMapName.setStatus("current")


class _FsQoSPolicyMapIfIndex_Type(Unsigned32):
    """Custom type fsQoSPolicyMapIfIndex based on Unsigned32"""
    defaultValue = 0


_FsQoSPolicyMapIfIndex_Type.__name__ = "Unsigned32"
_FsQoSPolicyMapIfIndex_Object = MibTableColumn
fsQoSPolicyMapIfIndex = _FsQoSPolicyMapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 2, 1, 3),
    _FsQoSPolicyMapIfIndex_Type()
)
fsQoSPolicyMapIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPolicyMapIfIndex.setStatus("current")


class _FsQoSPolicyMapCLASS_Type(Unsigned32):
    """Custom type fsQoSPolicyMapCLASS based on Unsigned32"""
    defaultValue = 0


_FsQoSPolicyMapCLASS_Type.__name__ = "Unsigned32"
_FsQoSPolicyMapCLASS_Object = MibTableColumn
fsQoSPolicyMapCLASS = _FsQoSPolicyMapCLASS_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 2, 1, 4),
    _FsQoSPolicyMapCLASS_Type()
)
fsQoSPolicyMapCLASS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPolicyMapCLASS.setStatus("current")


class _FsQoSPolicyMapPHBType_Type(Integer32):
    """Custom type fsQoSPolicyMapPHBType based on Integer32"""
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
        *(("none", 0),
          ("vlanPri", 1),
          ("ipTos", 2),
          ("ipDscp", 3),
          ("mplsExp", 4))
    )


_FsQoSPolicyMapPHBType_Type.__name__ = "Integer32"
_FsQoSPolicyMapPHBType_Object = MibTableColumn
fsQoSPolicyMapPHBType = _FsQoSPolicyMapPHBType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 2, 1, 5),
    _FsQoSPolicyMapPHBType_Type()
)
fsQoSPolicyMapPHBType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPolicyMapPHBType.setStatus("current")


class _FsQoSPolicyMapDefaultPHB_Type(Unsigned32):
    """Custom type fsQoSPolicyMapDefaultPHB based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_FsQoSPolicyMapDefaultPHB_Type.__name__ = "Unsigned32"
_FsQoSPolicyMapDefaultPHB_Object = MibTableColumn
fsQoSPolicyMapDefaultPHB = _FsQoSPolicyMapDefaultPHB_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 2, 1, 6),
    _FsQoSPolicyMapDefaultPHB_Type()
)
fsQoSPolicyMapDefaultPHB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPolicyMapDefaultPHB.setStatus("current")


class _FsQoSPolicyMapMeterTableId_Type(Unsigned32):
    """Custom type fsQoSPolicyMapMeterTableId based on Unsigned32"""
    defaultValue = 0


_FsQoSPolicyMapMeterTableId_Type.__name__ = "Unsigned32"
_FsQoSPolicyMapMeterTableId_Object = MibTableColumn
fsQoSPolicyMapMeterTableId = _FsQoSPolicyMapMeterTableId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 2, 1, 7),
    _FsQoSPolicyMapMeterTableId_Type()
)
fsQoSPolicyMapMeterTableId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPolicyMapMeterTableId.setStatus("current")


class _FsQoSPolicyMapFailMeterTableId_Type(Unsigned32):
    """Custom type fsQoSPolicyMapFailMeterTableId based on Unsigned32"""
    defaultValue = 0


_FsQoSPolicyMapFailMeterTableId_Type.__name__ = "Unsigned32"
_FsQoSPolicyMapFailMeterTableId_Object = MibTableColumn
fsQoSPolicyMapFailMeterTableId = _FsQoSPolicyMapFailMeterTableId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 2, 1, 8),
    _FsQoSPolicyMapFailMeterTableId_Type()
)
fsQoSPolicyMapFailMeterTableId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPolicyMapFailMeterTableId.setStatus("current")


class _FsQoSPolicyMapInProfileConformActionFlag_Type(Bits):
    """Custom type fsQoSPolicyMapInProfileConformActionFlag based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("setFlagPort", 1),
          ("setFlagConfTos", 2),
          ("setFlagConfDscp", 3),
          ("setFlagConfVlanPrio", 4),
          ("setFlagConfVlanDE", 5),
          ("setFlagConfInnerVlanPrio", 6),
          ("setFlagConfMplsExp", 7))
    )

_FsQoSPolicyMapInProfileConformActionFlag_Type.__name__ = "Bits"
_FsQoSPolicyMapInProfileConformActionFlag_Object = MibTableColumn
fsQoSPolicyMapInProfileConformActionFlag = _FsQoSPolicyMapInProfileConformActionFlag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 2, 1, 9),
    _FsQoSPolicyMapInProfileConformActionFlag_Type()
)
fsQoSPolicyMapInProfileConformActionFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPolicyMapInProfileConformActionFlag.setStatus("current")


class _FsQoSPolicyMapInProfileConformActionId_Type(Unsigned32):
    """Custom type fsQoSPolicyMapInProfileConformActionId based on Unsigned32"""
    defaultValue = 0


_FsQoSPolicyMapInProfileConformActionId_Type.__name__ = "Unsigned32"
_FsQoSPolicyMapInProfileConformActionId_Object = MibTableColumn
fsQoSPolicyMapInProfileConformActionId = _FsQoSPolicyMapInProfileConformActionId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 2, 1, 10),
    _FsQoSPolicyMapInProfileConformActionId_Type()
)
fsQoSPolicyMapInProfileConformActionId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPolicyMapInProfileConformActionId.setStatus("current")
_FsQoSPolicyMapInProfileActionSetPort_Type = Unsigned32
_FsQoSPolicyMapInProfileActionSetPort_Object = MibTableColumn
fsQoSPolicyMapInProfileActionSetPort = _FsQoSPolicyMapInProfileActionSetPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 2, 1, 11),
    _FsQoSPolicyMapInProfileActionSetPort_Type()
)
fsQoSPolicyMapInProfileActionSetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPolicyMapInProfileActionSetPort.setStatus("current")
_FsQoSPolicyMapConformActionSetIpTOS_Type = Unsigned32
_FsQoSPolicyMapConformActionSetIpTOS_Object = MibTableColumn
fsQoSPolicyMapConformActionSetIpTOS = _FsQoSPolicyMapConformActionSetIpTOS_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 2, 1, 12),
    _FsQoSPolicyMapConformActionSetIpTOS_Type()
)
fsQoSPolicyMapConformActionSetIpTOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPolicyMapConformActionSetIpTOS.setStatus("current")
_FsQoSPolicyMapConformActionSetDscp_Type = Dscp
_FsQoSPolicyMapConformActionSetDscp_Object = MibTableColumn
fsQoSPolicyMapConformActionSetDscp = _FsQoSPolicyMapConformActionSetDscp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 2, 1, 13),
    _FsQoSPolicyMapConformActionSetDscp_Type()
)
fsQoSPolicyMapConformActionSetDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPolicyMapConformActionSetDscp.setStatus("current")


class _FsQoSPolicyMapConformActionSetVlanPrio_Type(Unsigned32):
    """Custom type fsQoSPolicyMapConformActionSetVlanPrio based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsQoSPolicyMapConformActionSetVlanPrio_Type.__name__ = "Unsigned32"
_FsQoSPolicyMapConformActionSetVlanPrio_Object = MibTableColumn
fsQoSPolicyMapConformActionSetVlanPrio = _FsQoSPolicyMapConformActionSetVlanPrio_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 2, 1, 14),
    _FsQoSPolicyMapConformActionSetVlanPrio_Type()
)
fsQoSPolicyMapConformActionSetVlanPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPolicyMapConformActionSetVlanPrio.setStatus("current")


class _FsQoSPolicyMapConformActionSetVlanDE_Type(Unsigned32):
    """Custom type fsQoSPolicyMapConformActionSetVlanDE based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FsQoSPolicyMapConformActionSetVlanDE_Type.__name__ = "Unsigned32"
_FsQoSPolicyMapConformActionSetVlanDE_Object = MibTableColumn
fsQoSPolicyMapConformActionSetVlanDE = _FsQoSPolicyMapConformActionSetVlanDE_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 2, 1, 15),
    _FsQoSPolicyMapConformActionSetVlanDE_Type()
)
fsQoSPolicyMapConformActionSetVlanDE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPolicyMapConformActionSetVlanDE.setStatus("current")


class _FsQoSPolicyMapConformActionSetInnerVlanPrio_Type(Unsigned32):
    """Custom type fsQoSPolicyMapConformActionSetInnerVlanPrio based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsQoSPolicyMapConformActionSetInnerVlanPrio_Type.__name__ = "Unsigned32"
_FsQoSPolicyMapConformActionSetInnerVlanPrio_Object = MibTableColumn
fsQoSPolicyMapConformActionSetInnerVlanPrio = _FsQoSPolicyMapConformActionSetInnerVlanPrio_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 2, 1, 16),
    _FsQoSPolicyMapConformActionSetInnerVlanPrio_Type()
)
fsQoSPolicyMapConformActionSetInnerVlanPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPolicyMapConformActionSetInnerVlanPrio.setStatus("current")


class _FsQoSPolicyMapConformActionSetMplsExp_Type(Unsigned32):
    """Custom type fsQoSPolicyMapConformActionSetMplsExp based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsQoSPolicyMapConformActionSetMplsExp_Type.__name__ = "Unsigned32"
_FsQoSPolicyMapConformActionSetMplsExp_Object = MibTableColumn
fsQoSPolicyMapConformActionSetMplsExp = _FsQoSPolicyMapConformActionSetMplsExp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 2, 1, 17),
    _FsQoSPolicyMapConformActionSetMplsExp_Type()
)
fsQoSPolicyMapConformActionSetMplsExp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPolicyMapConformActionSetMplsExp.setStatus("current")
_FsQoSPolicyMapConformActionSetNewCLASS_Type = Unsigned32
_FsQoSPolicyMapConformActionSetNewCLASS_Object = MibTableColumn
fsQoSPolicyMapConformActionSetNewCLASS = _FsQoSPolicyMapConformActionSetNewCLASS_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 2, 1, 18),
    _FsQoSPolicyMapConformActionSetNewCLASS_Type()
)
fsQoSPolicyMapConformActionSetNewCLASS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPolicyMapConformActionSetNewCLASS.setStatus("current")


class _FsQoSPolicyMapInProfileExceedActionFlag_Type(Bits):
    """Custom type fsQoSPolicyMapInProfileExceedActionFlag based on Bits"""
    namedValues = NamedValues(
        *(("setFlagExcDrop", 0),
          ("setFlagExcTos", 1),
          ("setFlagExcDscp", 2),
          ("setFlagExcVlanPrio", 3),
          ("setFlagExcVlanDE", 4),
          ("setFlagExcInnerVlanPrio", 5),
          ("setFlagExcMplsExp", 6))
    )

_FsQoSPolicyMapInProfileExceedActionFlag_Type.__name__ = "Bits"
_FsQoSPolicyMapInProfileExceedActionFlag_Object = MibTableColumn
fsQoSPolicyMapInProfileExceedActionFlag = _FsQoSPolicyMapInProfileExceedActionFlag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 2, 1, 19),
    _FsQoSPolicyMapInProfileExceedActionFlag_Type()
)
fsQoSPolicyMapInProfileExceedActionFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPolicyMapInProfileExceedActionFlag.setStatus("current")


class _FsQoSPolicyMapInProfileExceedActionId_Type(Unsigned32):
    """Custom type fsQoSPolicyMapInProfileExceedActionId based on Unsigned32"""
    defaultValue = 0


_FsQoSPolicyMapInProfileExceedActionId_Type.__name__ = "Unsigned32"
_FsQoSPolicyMapInProfileExceedActionId_Object = MibTableColumn
fsQoSPolicyMapInProfileExceedActionId = _FsQoSPolicyMapInProfileExceedActionId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 2, 1, 20),
    _FsQoSPolicyMapInProfileExceedActionId_Type()
)
fsQoSPolicyMapInProfileExceedActionId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPolicyMapInProfileExceedActionId.setStatus("current")
_FsQoSPolicyMapExceedActionSetIpTOS_Type = Unsigned32
_FsQoSPolicyMapExceedActionSetIpTOS_Object = MibTableColumn
fsQoSPolicyMapExceedActionSetIpTOS = _FsQoSPolicyMapExceedActionSetIpTOS_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 2, 1, 21),
    _FsQoSPolicyMapExceedActionSetIpTOS_Type()
)
fsQoSPolicyMapExceedActionSetIpTOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPolicyMapExceedActionSetIpTOS.setStatus("current")
_FsQoSPolicyMapExceedActionSetDscp_Type = Dscp
_FsQoSPolicyMapExceedActionSetDscp_Object = MibTableColumn
fsQoSPolicyMapExceedActionSetDscp = _FsQoSPolicyMapExceedActionSetDscp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 2, 1, 22),
    _FsQoSPolicyMapExceedActionSetDscp_Type()
)
fsQoSPolicyMapExceedActionSetDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPolicyMapExceedActionSetDscp.setStatus("current")


class _FsQoSPolicyMapExceedActionSetInnerVlanPrio_Type(Unsigned32):
    """Custom type fsQoSPolicyMapExceedActionSetInnerVlanPrio based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsQoSPolicyMapExceedActionSetInnerVlanPrio_Type.__name__ = "Unsigned32"
_FsQoSPolicyMapExceedActionSetInnerVlanPrio_Object = MibTableColumn
fsQoSPolicyMapExceedActionSetInnerVlanPrio = _FsQoSPolicyMapExceedActionSetInnerVlanPrio_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 2, 1, 23),
    _FsQoSPolicyMapExceedActionSetInnerVlanPrio_Type()
)
fsQoSPolicyMapExceedActionSetInnerVlanPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPolicyMapExceedActionSetInnerVlanPrio.setStatus("current")


class _FsQoSPolicyMapExceedActionSetVlanPrio_Type(Unsigned32):
    """Custom type fsQoSPolicyMapExceedActionSetVlanPrio based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsQoSPolicyMapExceedActionSetVlanPrio_Type.__name__ = "Unsigned32"
_FsQoSPolicyMapExceedActionSetVlanPrio_Object = MibTableColumn
fsQoSPolicyMapExceedActionSetVlanPrio = _FsQoSPolicyMapExceedActionSetVlanPrio_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 2, 1, 24),
    _FsQoSPolicyMapExceedActionSetVlanPrio_Type()
)
fsQoSPolicyMapExceedActionSetVlanPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPolicyMapExceedActionSetVlanPrio.setStatus("current")


class _FsQoSPolicyMapExceedActionSetVlanDE_Type(Unsigned32):
    """Custom type fsQoSPolicyMapExceedActionSetVlanDE based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FsQoSPolicyMapExceedActionSetVlanDE_Type.__name__ = "Unsigned32"
_FsQoSPolicyMapExceedActionSetVlanDE_Object = MibTableColumn
fsQoSPolicyMapExceedActionSetVlanDE = _FsQoSPolicyMapExceedActionSetVlanDE_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 2, 1, 25),
    _FsQoSPolicyMapExceedActionSetVlanDE_Type()
)
fsQoSPolicyMapExceedActionSetVlanDE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPolicyMapExceedActionSetVlanDE.setStatus("current")


class _FsQoSPolicyMapExceedActionSetMplsExp_Type(Unsigned32):
    """Custom type fsQoSPolicyMapExceedActionSetMplsExp based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsQoSPolicyMapExceedActionSetMplsExp_Type.__name__ = "Unsigned32"
_FsQoSPolicyMapExceedActionSetMplsExp_Object = MibTableColumn
fsQoSPolicyMapExceedActionSetMplsExp = _FsQoSPolicyMapExceedActionSetMplsExp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 2, 1, 26),
    _FsQoSPolicyMapExceedActionSetMplsExp_Type()
)
fsQoSPolicyMapExceedActionSetMplsExp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPolicyMapExceedActionSetMplsExp.setStatus("current")
_FsQoSPolicyMapExceedActionSetNewCLASS_Type = Unsigned32
_FsQoSPolicyMapExceedActionSetNewCLASS_Object = MibTableColumn
fsQoSPolicyMapExceedActionSetNewCLASS = _FsQoSPolicyMapExceedActionSetNewCLASS_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 2, 1, 27),
    _FsQoSPolicyMapExceedActionSetNewCLASS_Type()
)
fsQoSPolicyMapExceedActionSetNewCLASS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPolicyMapExceedActionSetNewCLASS.setStatus("current")


class _FsQoSPolicyMapOutProfileActionFlag_Type(Bits):
    """Custom type fsQoSPolicyMapOutProfileActionFlag based on Bits"""
    namedValues = NamedValues(
        *(("setFlagDrop", 0),
          ("setFlagTos", 1),
          ("setFlagDscp", 2),
          ("setFlagVlanPrio", 3),
          ("setFlagVlanDE", 4),
          ("setFlagConfInnerVlanPrio", 5),
          ("setFlagMplsExp", 6))
    )

_FsQoSPolicyMapOutProfileActionFlag_Type.__name__ = "Bits"
_FsQoSPolicyMapOutProfileActionFlag_Object = MibTableColumn
fsQoSPolicyMapOutProfileActionFlag = _FsQoSPolicyMapOutProfileActionFlag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 2, 1, 28),
    _FsQoSPolicyMapOutProfileActionFlag_Type()
)
fsQoSPolicyMapOutProfileActionFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPolicyMapOutProfileActionFlag.setStatus("current")


class _FsQoSPolicyMapOutProfileActionId_Type(Unsigned32):
    """Custom type fsQoSPolicyMapOutProfileActionId based on Unsigned32"""
    defaultValue = 0


_FsQoSPolicyMapOutProfileActionId_Type.__name__ = "Unsigned32"
_FsQoSPolicyMapOutProfileActionId_Object = MibTableColumn
fsQoSPolicyMapOutProfileActionId = _FsQoSPolicyMapOutProfileActionId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 2, 1, 29),
    _FsQoSPolicyMapOutProfileActionId_Type()
)
fsQoSPolicyMapOutProfileActionId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPolicyMapOutProfileActionId.setStatus("current")
_FsQoSPolicyMapOutProfileActionSetIPTOS_Type = Unsigned32
_FsQoSPolicyMapOutProfileActionSetIPTOS_Object = MibTableColumn
fsQoSPolicyMapOutProfileActionSetIPTOS = _FsQoSPolicyMapOutProfileActionSetIPTOS_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 2, 1, 30),
    _FsQoSPolicyMapOutProfileActionSetIPTOS_Type()
)
fsQoSPolicyMapOutProfileActionSetIPTOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPolicyMapOutProfileActionSetIPTOS.setStatus("current")
_FsQoSPolicyMapOutProfileActionSetDscp_Type = Dscp
_FsQoSPolicyMapOutProfileActionSetDscp_Object = MibTableColumn
fsQoSPolicyMapOutProfileActionSetDscp = _FsQoSPolicyMapOutProfileActionSetDscp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 2, 1, 31),
    _FsQoSPolicyMapOutProfileActionSetDscp_Type()
)
fsQoSPolicyMapOutProfileActionSetDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPolicyMapOutProfileActionSetDscp.setStatus("current")


class _FsQoSPolicyMapOutProfileActionSetInnerVlanPrio_Type(Unsigned32):
    """Custom type fsQoSPolicyMapOutProfileActionSetInnerVlanPrio based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsQoSPolicyMapOutProfileActionSetInnerVlanPrio_Type.__name__ = "Unsigned32"
_FsQoSPolicyMapOutProfileActionSetInnerVlanPrio_Object = MibTableColumn
fsQoSPolicyMapOutProfileActionSetInnerVlanPrio = _FsQoSPolicyMapOutProfileActionSetInnerVlanPrio_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 2, 1, 32),
    _FsQoSPolicyMapOutProfileActionSetInnerVlanPrio_Type()
)
fsQoSPolicyMapOutProfileActionSetInnerVlanPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPolicyMapOutProfileActionSetInnerVlanPrio.setStatus("current")


class _FsQoSPolicyMapOutProfileActionSetVlanPrio_Type(Unsigned32):
    """Custom type fsQoSPolicyMapOutProfileActionSetVlanPrio based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsQoSPolicyMapOutProfileActionSetVlanPrio_Type.__name__ = "Unsigned32"
_FsQoSPolicyMapOutProfileActionSetVlanPrio_Object = MibTableColumn
fsQoSPolicyMapOutProfileActionSetVlanPrio = _FsQoSPolicyMapOutProfileActionSetVlanPrio_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 2, 1, 33),
    _FsQoSPolicyMapOutProfileActionSetVlanPrio_Type()
)
fsQoSPolicyMapOutProfileActionSetVlanPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPolicyMapOutProfileActionSetVlanPrio.setStatus("current")


class _FsQoSPolicyMapOutProfileActionSetVlanDE_Type(Unsigned32):
    """Custom type fsQoSPolicyMapOutProfileActionSetVlanDE based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FsQoSPolicyMapOutProfileActionSetVlanDE_Type.__name__ = "Unsigned32"
_FsQoSPolicyMapOutProfileActionSetVlanDE_Object = MibTableColumn
fsQoSPolicyMapOutProfileActionSetVlanDE = _FsQoSPolicyMapOutProfileActionSetVlanDE_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 2, 1, 34),
    _FsQoSPolicyMapOutProfileActionSetVlanDE_Type()
)
fsQoSPolicyMapOutProfileActionSetVlanDE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPolicyMapOutProfileActionSetVlanDE.setStatus("current")


class _FsQoSPolicyMapOutProfileActionSetMplsExp_Type(Unsigned32):
    """Custom type fsQoSPolicyMapOutProfileActionSetMplsExp based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsQoSPolicyMapOutProfileActionSetMplsExp_Type.__name__ = "Unsigned32"
_FsQoSPolicyMapOutProfileActionSetMplsExp_Object = MibTableColumn
fsQoSPolicyMapOutProfileActionSetMplsExp = _FsQoSPolicyMapOutProfileActionSetMplsExp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 2, 1, 35),
    _FsQoSPolicyMapOutProfileActionSetMplsExp_Type()
)
fsQoSPolicyMapOutProfileActionSetMplsExp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPolicyMapOutProfileActionSetMplsExp.setStatus("current")
_FsQoSPolicyMapOutProfileActionSetNewCLASS_Type = Unsigned32
_FsQoSPolicyMapOutProfileActionSetNewCLASS_Object = MibTableColumn
fsQoSPolicyMapOutProfileActionSetNewCLASS = _FsQoSPolicyMapOutProfileActionSetNewCLASS_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 2, 1, 36),
    _FsQoSPolicyMapOutProfileActionSetNewCLASS_Type()
)
fsQoSPolicyMapOutProfileActionSetNewCLASS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPolicyMapOutProfileActionSetNewCLASS.setStatus("current")
_FsQoSPolicyMapStatus_Type = RowStatus
_FsQoSPolicyMapStatus_Object = MibTableColumn
fsQoSPolicyMapStatus = _FsQoSPolicyMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 3, 2, 1, 37),
    _FsQoSPolicyMapStatus_Type()
)
fsQoSPolicyMapStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsQoSPolicyMapStatus.setStatus("current")
_FsQoSTrafficMgmt_ObjectIdentity = ObjectIdentity
fsQoSTrafficMgmt = _FsQoSTrafficMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4)
)
_FsQoSQTemplateTable_Object = MibTable
fsQoSQTemplateTable = _FsQoSQTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 1)
)
if mibBuilder.loadTexts:
    fsQoSQTemplateTable.setStatus("current")
_FsQoSQTemplateEntry_Object = MibTableRow
fsQoSQTemplateEntry = _FsQoSQTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 1, 1)
)
fsQoSQTemplateEntry.setIndexNames(
    (0, "SUPERMICRO-QOS-MIB", "fsQoSQTemplateId"),
)
if mibBuilder.loadTexts:
    fsQoSQTemplateEntry.setStatus("current")
_FsQoSQTemplateId_Type = IndexInteger
_FsQoSQTemplateId_Object = MibTableColumn
fsQoSQTemplateId = _FsQoSQTemplateId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 1, 1, 1),
    _FsQoSQTemplateId_Type()
)
fsQoSQTemplateId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsQoSQTemplateId.setStatus("current")


class _FsQoSQTemplateName_Type(DisplayString):
    """Custom type fsQoSQTemplateName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_FsQoSQTemplateName_Type.__name__ = "DisplayString"
_FsQoSQTemplateName_Object = MibTableColumn
fsQoSQTemplateName = _FsQoSQTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 1, 1, 2),
    _FsQoSQTemplateName_Type()
)
fsQoSQTemplateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSQTemplateName.setStatus("current")


class _FsQoSQTemplateDropType_Type(Integer32):
    """Custom type fsQoSQTemplateDropType based on Integer32"""
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
        *(("other", 1),
          ("tailDrop", 2),
          ("headDrop", 3),
          ("red", 4),
          ("alwaysDrop", 5),
          ("wred", 6))
    )


_FsQoSQTemplateDropType_Type.__name__ = "Integer32"
_FsQoSQTemplateDropType_Object = MibTableColumn
fsQoSQTemplateDropType = _FsQoSQTemplateDropType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 1, 1, 3),
    _FsQoSQTemplateDropType_Type()
)
fsQoSQTemplateDropType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSQTemplateDropType.setStatus("current")


class _FsQoSQTemplateDropAlgoEnableFlag_Type(EnableStatus):
    """Custom type fsQoSQTemplateDropAlgoEnableFlag based on EnableStatus"""
    defaultValue = 1


_FsQoSQTemplateDropAlgoEnableFlag_Type.__name__ = "EnableStatus"
_FsQoSQTemplateDropAlgoEnableFlag_Object = MibTableColumn
fsQoSQTemplateDropAlgoEnableFlag = _FsQoSQTemplateDropAlgoEnableFlag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 1, 1, 4),
    _FsQoSQTemplateDropAlgoEnableFlag_Type()
)
fsQoSQTemplateDropAlgoEnableFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSQTemplateDropAlgoEnableFlag.setStatus("current")


class _FsQoSQTemplateSize_Type(Unsigned32):
    """Custom type fsQoSQTemplateSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsQoSQTemplateSize_Type.__name__ = "Unsigned32"
_FsQoSQTemplateSize_Object = MibTableColumn
fsQoSQTemplateSize = _FsQoSQTemplateSize_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 1, 1, 5),
    _FsQoSQTemplateSize_Type()
)
fsQoSQTemplateSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSQTemplateSize.setStatus("current")
if mibBuilder.loadTexts:
    fsQoSQTemplateSize.setUnits("bytes")
_FsQoSQTemplateStatus_Type = RowStatus
_FsQoSQTemplateStatus_Object = MibTableColumn
fsQoSQTemplateStatus = _FsQoSQTemplateStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 1, 1, 6),
    _FsQoSQTemplateStatus_Type()
)
fsQoSQTemplateStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsQoSQTemplateStatus.setStatus("current")
_FsQoSRandomDetectCfgTable_Object = MibTable
fsQoSRandomDetectCfgTable = _FsQoSRandomDetectCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 2)
)
if mibBuilder.loadTexts:
    fsQoSRandomDetectCfgTable.setStatus("current")
_FsQoSRandomDetectCfgEntry_Object = MibTableRow
fsQoSRandomDetectCfgEntry = _FsQoSRandomDetectCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 2, 1)
)
fsQoSRandomDetectCfgEntry.setIndexNames(
    (0, "SUPERMICRO-QOS-MIB", "fsQoSQTemplateId"),
    (0, "SUPERMICRO-QOS-MIB", "fsQoSRandomDetectCfgDP"),
)
if mibBuilder.loadTexts:
    fsQoSRandomDetectCfgEntry.setStatus("current")


class _FsQoSRandomDetectCfgDP_Type(Integer32):
    """Custom type fsQoSRandomDetectCfgDP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_FsQoSRandomDetectCfgDP_Type.__name__ = "Integer32"
_FsQoSRandomDetectCfgDP_Object = MibTableColumn
fsQoSRandomDetectCfgDP = _FsQoSRandomDetectCfgDP_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 2, 1, 1),
    _FsQoSRandomDetectCfgDP_Type()
)
fsQoSRandomDetectCfgDP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsQoSRandomDetectCfgDP.setStatus("current")


class _FsQoSRandomDetectCfgMinAvgThresh_Type(Unsigned32):
    """Custom type fsQoSRandomDetectCfgMinAvgThresh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsQoSRandomDetectCfgMinAvgThresh_Type.__name__ = "Unsigned32"
_FsQoSRandomDetectCfgMinAvgThresh_Object = MibTableColumn
fsQoSRandomDetectCfgMinAvgThresh = _FsQoSRandomDetectCfgMinAvgThresh_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 2, 1, 2),
    _FsQoSRandomDetectCfgMinAvgThresh_Type()
)
fsQoSRandomDetectCfgMinAvgThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSRandomDetectCfgMinAvgThresh.setStatus("current")


class _FsQoSRandomDetectCfgMaxAvgThresh_Type(Unsigned32):
    """Custom type fsQoSRandomDetectCfgMaxAvgThresh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsQoSRandomDetectCfgMaxAvgThresh_Type.__name__ = "Unsigned32"
_FsQoSRandomDetectCfgMaxAvgThresh_Object = MibTableColumn
fsQoSRandomDetectCfgMaxAvgThresh = _FsQoSRandomDetectCfgMaxAvgThresh_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 2, 1, 3),
    _FsQoSRandomDetectCfgMaxAvgThresh_Type()
)
fsQoSRandomDetectCfgMaxAvgThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSRandomDetectCfgMaxAvgThresh.setStatus("current")


class _FsQoSRandomDetectCfgMaxPktSize_Type(Unsigned32):
    """Custom type fsQoSRandomDetectCfgMaxPktSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsQoSRandomDetectCfgMaxPktSize_Type.__name__ = "Unsigned32"
_FsQoSRandomDetectCfgMaxPktSize_Object = MibTableColumn
fsQoSRandomDetectCfgMaxPktSize = _FsQoSRandomDetectCfgMaxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 2, 1, 4),
    _FsQoSRandomDetectCfgMaxPktSize_Type()
)
fsQoSRandomDetectCfgMaxPktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSRandomDetectCfgMaxPktSize.setStatus("current")


class _FsQoSRandomDetectCfgMaxProb_Type(Unsigned32):
    """Custom type fsQoSRandomDetectCfgMaxProb based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_FsQoSRandomDetectCfgMaxProb_Type.__name__ = "Unsigned32"
_FsQoSRandomDetectCfgMaxProb_Object = MibTableColumn
fsQoSRandomDetectCfgMaxProb = _FsQoSRandomDetectCfgMaxProb_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 2, 1, 5),
    _FsQoSRandomDetectCfgMaxProb_Type()
)
fsQoSRandomDetectCfgMaxProb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSRandomDetectCfgMaxProb.setStatus("current")


class _FsQoSRandomDetectCfgExpWeight_Type(Unsigned32):
    """Custom type fsQoSRandomDetectCfgExpWeight based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_FsQoSRandomDetectCfgExpWeight_Type.__name__ = "Unsigned32"
_FsQoSRandomDetectCfgExpWeight_Object = MibTableColumn
fsQoSRandomDetectCfgExpWeight = _FsQoSRandomDetectCfgExpWeight_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 2, 1, 6),
    _FsQoSRandomDetectCfgExpWeight_Type()
)
fsQoSRandomDetectCfgExpWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSRandomDetectCfgExpWeight.setStatus("current")
_FsQoSRandomDetectCfgStatus_Type = RowStatus
_FsQoSRandomDetectCfgStatus_Object = MibTableColumn
fsQoSRandomDetectCfgStatus = _FsQoSRandomDetectCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 2, 1, 7),
    _FsQoSRandomDetectCfgStatus_Type()
)
fsQoSRandomDetectCfgStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsQoSRandomDetectCfgStatus.setStatus("current")
_FsQoSShapeTemplateTable_Object = MibTable
fsQoSShapeTemplateTable = _FsQoSShapeTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 3)
)
if mibBuilder.loadTexts:
    fsQoSShapeTemplateTable.setStatus("current")
_FsQoSShapeTemplateEntry_Object = MibTableRow
fsQoSShapeTemplateEntry = _FsQoSShapeTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 3, 1)
)
fsQoSShapeTemplateEntry.setIndexNames(
    (0, "SUPERMICRO-QOS-MIB", "fsQoSShapeTemplateId"),
)
if mibBuilder.loadTexts:
    fsQoSShapeTemplateEntry.setStatus("current")
_FsQoSShapeTemplateId_Type = IndexInteger
_FsQoSShapeTemplateId_Object = MibTableColumn
fsQoSShapeTemplateId = _FsQoSShapeTemplateId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 3, 1, 1),
    _FsQoSShapeTemplateId_Type()
)
fsQoSShapeTemplateId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsQoSShapeTemplateId.setStatus("current")


class _FsQoSShapeTemplateName_Type(DisplayString):
    """Custom type fsQoSShapeTemplateName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_FsQoSShapeTemplateName_Type.__name__ = "DisplayString"
_FsQoSShapeTemplateName_Object = MibTableColumn
fsQoSShapeTemplateName = _FsQoSShapeTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 3, 1, 2),
    _FsQoSShapeTemplateName_Type()
)
fsQoSShapeTemplateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSShapeTemplateName.setStatus("current")


class _FsQoSShapeTemplateCIR_Type(Unsigned32):
    """Custom type fsQoSShapeTemplateCIR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsQoSShapeTemplateCIR_Type.__name__ = "Unsigned32"
_FsQoSShapeTemplateCIR_Object = MibTableColumn
fsQoSShapeTemplateCIR = _FsQoSShapeTemplateCIR_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 3, 1, 3),
    _FsQoSShapeTemplateCIR_Type()
)
fsQoSShapeTemplateCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSShapeTemplateCIR.setStatus("current")


class _FsQoSShapeTemplateCBS_Type(Unsigned32):
    """Custom type fsQoSShapeTemplateCBS based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsQoSShapeTemplateCBS_Type.__name__ = "Unsigned32"
_FsQoSShapeTemplateCBS_Object = MibTableColumn
fsQoSShapeTemplateCBS = _FsQoSShapeTemplateCBS_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 3, 1, 4),
    _FsQoSShapeTemplateCBS_Type()
)
fsQoSShapeTemplateCBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSShapeTemplateCBS.setStatus("current")
if mibBuilder.loadTexts:
    fsQoSShapeTemplateCBS.setUnits("Bytes")


class _FsQoSShapeTemplateEIR_Type(Unsigned32):
    """Custom type fsQoSShapeTemplateEIR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsQoSShapeTemplateEIR_Type.__name__ = "Unsigned32"
_FsQoSShapeTemplateEIR_Object = MibTableColumn
fsQoSShapeTemplateEIR = _FsQoSShapeTemplateEIR_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 3, 1, 5),
    _FsQoSShapeTemplateEIR_Type()
)
fsQoSShapeTemplateEIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSShapeTemplateEIR.setStatus("current")


class _FsQoSShapeTemplateEBS_Type(Unsigned32):
    """Custom type fsQoSShapeTemplateEBS based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsQoSShapeTemplateEBS_Type.__name__ = "Unsigned32"
_FsQoSShapeTemplateEBS_Object = MibTableColumn
fsQoSShapeTemplateEBS = _FsQoSShapeTemplateEBS_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 3, 1, 6),
    _FsQoSShapeTemplateEBS_Type()
)
fsQoSShapeTemplateEBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSShapeTemplateEBS.setStatus("current")
if mibBuilder.loadTexts:
    fsQoSShapeTemplateEBS.setUnits("Bytes")
_FsQoSShapeTemplateStatus_Type = RowStatus
_FsQoSShapeTemplateStatus_Object = MibTableColumn
fsQoSShapeTemplateStatus = _FsQoSShapeTemplateStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 3, 1, 7),
    _FsQoSShapeTemplateStatus_Type()
)
fsQoSShapeTemplateStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsQoSShapeTemplateStatus.setStatus("current")
_FsQoSQMapTable_Object = MibTable
fsQoSQMapTable = _FsQoSQMapTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 4)
)
if mibBuilder.loadTexts:
    fsQoSQMapTable.setStatus("current")
_FsQoSQMapEntry_Object = MibTableRow
fsQoSQMapEntry = _FsQoSQMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 4, 1)
)
fsQoSQMapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SUPERMICRO-QOS-MIB", "fsQoSQMapCLASS"),
    (0, "SUPERMICRO-QOS-MIB", "fsQoSQMapRegenPriType"),
    (0, "SUPERMICRO-QOS-MIB", "fsQoSQMapRegenPriority"),
)
if mibBuilder.loadTexts:
    fsQoSQMapEntry.setStatus("current")


class _FsQoSQMapCLASS_Type(Unsigned32):
    """Custom type fsQoSQMapCLASS based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsQoSQMapCLASS_Type.__name__ = "Unsigned32"
_FsQoSQMapCLASS_Object = MibTableColumn
fsQoSQMapCLASS = _FsQoSQMapCLASS_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 4, 1, 1),
    _FsQoSQMapCLASS_Type()
)
fsQoSQMapCLASS.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsQoSQMapCLASS.setStatus("current")


class _FsQoSQMapRegenPriType_Type(Integer32):
    """Custom type fsQoSQMapRegenPriType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("vlanPri", 1),
          ("ipTos", 2),
          ("ipDscp", 3),
          ("mplsExp", 4),
          ("vlanDEI", 5),
          ("internalPrio", 6))
    )


_FsQoSQMapRegenPriType_Type.__name__ = "Integer32"
_FsQoSQMapRegenPriType_Object = MibTableColumn
fsQoSQMapRegenPriType = _FsQoSQMapRegenPriType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 4, 1, 2),
    _FsQoSQMapRegenPriType_Type()
)
fsQoSQMapRegenPriType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsQoSQMapRegenPriType.setStatus("current")


class _FsQoSQMapRegenPriority_Type(Unsigned32):
    """Custom type fsQoSQMapRegenPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_FsQoSQMapRegenPriority_Type.__name__ = "Unsigned32"
_FsQoSQMapRegenPriority_Object = MibTableColumn
fsQoSQMapRegenPriority = _FsQoSQMapRegenPriority_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 4, 1, 3),
    _FsQoSQMapRegenPriority_Type()
)
fsQoSQMapRegenPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsQoSQMapRegenPriority.setStatus("current")


class _FsQoSQMapQId_Type(Unsigned32):
    """Custom type fsQoSQMapQId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsQoSQMapQId_Type.__name__ = "Unsigned32"
_FsQoSQMapQId_Object = MibTableColumn
fsQoSQMapQId = _FsQoSQMapQId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 4, 1, 4),
    _FsQoSQMapQId_Type()
)
fsQoSQMapQId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSQMapQId.setStatus("current")
_FsQoSQMapStatus_Type = RowStatus
_FsQoSQMapStatus_Object = MibTableColumn
fsQoSQMapStatus = _FsQoSQMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 4, 1, 5),
    _FsQoSQMapStatus_Type()
)
fsQoSQMapStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsQoSQMapStatus.setStatus("current")
_FsQoSQTable_Object = MibTable
fsQoSQTable = _FsQoSQTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 5)
)
if mibBuilder.loadTexts:
    fsQoSQTable.setStatus("current")
_FsQoSQEntry_Object = MibTableRow
fsQoSQEntry = _FsQoSQEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 5, 1)
)
fsQoSQEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SUPERMICRO-QOS-MIB", "fsQoSQId"),
)
if mibBuilder.loadTexts:
    fsQoSQEntry.setStatus("current")


class _FsQoSQId_Type(Unsigned32):
    """Custom type fsQoSQId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsQoSQId_Type.__name__ = "Unsigned32"
_FsQoSQId_Object = MibTableColumn
fsQoSQId = _FsQoSQId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 5, 1, 1),
    _FsQoSQId_Type()
)
fsQoSQId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsQoSQId.setStatus("current")


class _FsQoSQCfgTemplateId_Type(Unsigned32):
    """Custom type fsQoSQCfgTemplateId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsQoSQCfgTemplateId_Type.__name__ = "Unsigned32"
_FsQoSQCfgTemplateId_Object = MibTableColumn
fsQoSQCfgTemplateId = _FsQoSQCfgTemplateId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 5, 1, 2),
    _FsQoSQCfgTemplateId_Type()
)
fsQoSQCfgTemplateId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSQCfgTemplateId.setStatus("current")


class _FsQoSQSchedulerId_Type(Unsigned32):
    """Custom type fsQoSQSchedulerId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsQoSQSchedulerId_Type.__name__ = "Unsigned32"
_FsQoSQSchedulerId_Object = MibTableColumn
fsQoSQSchedulerId = _FsQoSQSchedulerId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 5, 1, 3),
    _FsQoSQSchedulerId_Type()
)
fsQoSQSchedulerId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSQSchedulerId.setStatus("current")


class _FsQoSQWeight_Type(Unsigned32):
    """Custom type fsQoSQWeight based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_FsQoSQWeight_Type.__name__ = "Unsigned32"
_FsQoSQWeight_Object = MibTableColumn
fsQoSQWeight = _FsQoSQWeight_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 5, 1, 4),
    _FsQoSQWeight_Type()
)
fsQoSQWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSQWeight.setStatus("current")


class _FsQoSQPriority_Type(Unsigned32):
    """Custom type fsQoSQPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FsQoSQPriority_Type.__name__ = "Unsigned32"
_FsQoSQPriority_Object = MibTableColumn
fsQoSQPriority = _FsQoSQPriority_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 5, 1, 5),
    _FsQoSQPriority_Type()
)
fsQoSQPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSQPriority.setStatus("current")


class _FsQoSQShapeId_Type(Unsigned32):
    """Custom type fsQoSQShapeId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsQoSQShapeId_Type.__name__ = "Unsigned32"
_FsQoSQShapeId_Object = MibTableColumn
fsQoSQShapeId = _FsQoSQShapeId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 5, 1, 6),
    _FsQoSQShapeId_Type()
)
fsQoSQShapeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSQShapeId.setStatus("current")
_FsQoSQStatus_Type = RowStatus
_FsQoSQStatus_Object = MibTableColumn
fsQoSQStatus = _FsQoSQStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 5, 1, 7),
    _FsQoSQStatus_Type()
)
fsQoSQStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsQoSQStatus.setStatus("current")


class _FsQoSQType_Type(Unsigned32):
    """Custom type fsQoSQType based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_FsQoSQType_Type.__name__ = "Unsigned32"
_FsQoSQType_Object = MibTableColumn
fsQoSQType = _FsQoSQType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 5, 1, 8),
    _FsQoSQType_Type()
)
fsQoSQType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSQType.setStatus("current")
_FsQoSSchedulerTable_Object = MibTable
fsQoSSchedulerTable = _FsQoSSchedulerTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 6)
)
if mibBuilder.loadTexts:
    fsQoSSchedulerTable.setStatus("current")
_FsQoSSchedulerEntry_Object = MibTableRow
fsQoSSchedulerEntry = _FsQoSSchedulerEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 6, 1)
)
fsQoSSchedulerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SUPERMICRO-QOS-MIB", "fsQoSSchedulerId"),
)
if mibBuilder.loadTexts:
    fsQoSSchedulerEntry.setStatus("current")


class _FsQoSSchedulerId_Type(Unsigned32):
    """Custom type fsQoSSchedulerId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsQoSSchedulerId_Type.__name__ = "Unsigned32"
_FsQoSSchedulerId_Object = MibTableColumn
fsQoSSchedulerId = _FsQoSSchedulerId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 6, 1, 1),
    _FsQoSSchedulerId_Type()
)
fsQoSSchedulerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsQoSSchedulerId.setStatus("current")


class _FsQoSSchedulerSchedAlgorithm_Type(Integer32):
    """Custom type fsQoSSchedulerSchedAlgorithm based on Integer32"""
    defaultValue = 1

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("strictPriority", 1),
          ("roundRobin", 2),
          ("weightedRoundRobin", 3),
          ("weightedFairQueing", 4),
          ("strictRoundRobin", 5),
          ("strictWeightedRoundRobin", 6),
          ("strictWeightedFairQueing", 7),
          ("deficitRoundRobin", 8))
    )


_FsQoSSchedulerSchedAlgorithm_Type.__name__ = "Integer32"
_FsQoSSchedulerSchedAlgorithm_Object = MibTableColumn
fsQoSSchedulerSchedAlgorithm = _FsQoSSchedulerSchedAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 6, 1, 2),
    _FsQoSSchedulerSchedAlgorithm_Type()
)
fsQoSSchedulerSchedAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSSchedulerSchedAlgorithm.setStatus("current")


class _FsQoSSchedulerShapeId_Type(Unsigned32):
    """Custom type fsQoSSchedulerShapeId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsQoSSchedulerShapeId_Type.__name__ = "Unsigned32"
_FsQoSSchedulerShapeId_Object = MibTableColumn
fsQoSSchedulerShapeId = _FsQoSSchedulerShapeId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 6, 1, 3),
    _FsQoSSchedulerShapeId_Type()
)
fsQoSSchedulerShapeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSSchedulerShapeId.setStatus("current")


class _FsQoSSchedulerHierarchyLevel_Type(Unsigned32):
    """Custom type fsQoSSchedulerHierarchyLevel based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_FsQoSSchedulerHierarchyLevel_Type.__name__ = "Unsigned32"
_FsQoSSchedulerHierarchyLevel_Object = MibTableColumn
fsQoSSchedulerHierarchyLevel = _FsQoSSchedulerHierarchyLevel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 6, 1, 4),
    _FsQoSSchedulerHierarchyLevel_Type()
)
fsQoSSchedulerHierarchyLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSSchedulerHierarchyLevel.setStatus("current")


class _FsQoSSchedulerGlobalId_Type(Unsigned32):
    """Custom type fsQoSSchedulerGlobalId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsQoSSchedulerGlobalId_Type.__name__ = "Unsigned32"
_FsQoSSchedulerGlobalId_Object = MibTableColumn
fsQoSSchedulerGlobalId = _FsQoSSchedulerGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 6, 1, 5),
    _FsQoSSchedulerGlobalId_Type()
)
fsQoSSchedulerGlobalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSSchedulerGlobalId.setStatus("current")
_FsQoSSchedulerStatus_Type = RowStatus
_FsQoSSchedulerStatus_Object = MibTableColumn
fsQoSSchedulerStatus = _FsQoSSchedulerStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 6, 1, 6),
    _FsQoSSchedulerStatus_Type()
)
fsQoSSchedulerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsQoSSchedulerStatus.setStatus("current")
_FsQoSHierarchyTable_Object = MibTable
fsQoSHierarchyTable = _FsQoSHierarchyTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 7)
)
if mibBuilder.loadTexts:
    fsQoSHierarchyTable.setStatus("current")
_FsQoSHierarchyEntry_Object = MibTableRow
fsQoSHierarchyEntry = _FsQoSHierarchyEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 7, 1)
)
fsQoSHierarchyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SUPERMICRO-QOS-MIB", "fsQoSHierarchyLevel"),
    (0, "SUPERMICRO-QOS-MIB", "fsQoSSchedulerId"),
)
if mibBuilder.loadTexts:
    fsQoSHierarchyEntry.setStatus("current")


class _FsQoSHierarchyLevel_Type(Unsigned32):
    """Custom type fsQoSHierarchyLevel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_FsQoSHierarchyLevel_Type.__name__ = "Unsigned32"
_FsQoSHierarchyLevel_Object = MibTableColumn
fsQoSHierarchyLevel = _FsQoSHierarchyLevel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 7, 1, 1),
    _FsQoSHierarchyLevel_Type()
)
fsQoSHierarchyLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsQoSHierarchyLevel.setStatus("current")


class _FsQoSHierarchyQNext_Type(Unsigned32):
    """Custom type fsQoSHierarchyQNext based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsQoSHierarchyQNext_Type.__name__ = "Unsigned32"
_FsQoSHierarchyQNext_Object = MibTableColumn
fsQoSHierarchyQNext = _FsQoSHierarchyQNext_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 7, 1, 2),
    _FsQoSHierarchyQNext_Type()
)
fsQoSHierarchyQNext.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSHierarchyQNext.setStatus("current")


class _FsQoSHierarchySchedNext_Type(Unsigned32):
    """Custom type fsQoSHierarchySchedNext based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsQoSHierarchySchedNext_Type.__name__ = "Unsigned32"
_FsQoSHierarchySchedNext_Object = MibTableColumn
fsQoSHierarchySchedNext = _FsQoSHierarchySchedNext_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 7, 1, 3),
    _FsQoSHierarchySchedNext_Type()
)
fsQoSHierarchySchedNext.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSHierarchySchedNext.setStatus("current")


class _FsQoSHierarchyWeight_Type(Unsigned32):
    """Custom type fsQoSHierarchyWeight based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_FsQoSHierarchyWeight_Type.__name__ = "Unsigned32"
_FsQoSHierarchyWeight_Object = MibTableColumn
fsQoSHierarchyWeight = _FsQoSHierarchyWeight_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 7, 1, 4),
    _FsQoSHierarchyWeight_Type()
)
fsQoSHierarchyWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSHierarchyWeight.setStatus("current")
if mibBuilder.loadTexts:
    fsQoSHierarchyWeight.setUnits("Percentage")


class _FsQoSHierarchyPriority_Type(SchedulerPriority):
    """Custom type fsQoSHierarchyPriority based on SchedulerPriority"""
    defaultValue = 0


_FsQoSHierarchyPriority_Type.__name__ = "SchedulerPriority"
_FsQoSHierarchyPriority_Object = MibTableColumn
fsQoSHierarchyPriority = _FsQoSHierarchyPriority_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 7, 1, 5),
    _FsQoSHierarchyPriority_Type()
)
fsQoSHierarchyPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSHierarchyPriority.setStatus("current")
_FsQoSHierarchyStatus_Type = RowStatus
_FsQoSHierarchyStatus_Object = MibTableColumn
fsQoSHierarchyStatus = _FsQoSHierarchyStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 7, 1, 6),
    _FsQoSHierarchyStatus_Type()
)
fsQoSHierarchyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsQoSHierarchyStatus.setStatus("current")
_FsQoSDefUserPriorityTable_Object = MibTable
fsQoSDefUserPriorityTable = _FsQoSDefUserPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 8)
)
if mibBuilder.loadTexts:
    fsQoSDefUserPriorityTable.setStatus("current")
_FsQoSDefUserPriorityEntry_Object = MibTableRow
fsQoSDefUserPriorityEntry = _FsQoSDefUserPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 8, 1)
)
fsQoSDefUserPriorityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsQoSDefUserPriorityEntry.setStatus("current")


class _FsQoSPortDefaultUserPriority_Type(Integer32):
    """Custom type fsQoSPortDefaultUserPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsQoSPortDefaultUserPriority_Type.__name__ = "Integer32"
_FsQoSPortDefaultUserPriority_Object = MibTableColumn
fsQoSPortDefaultUserPriority = _FsQoSPortDefaultUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 8, 1, 1),
    _FsQoSPortDefaultUserPriority_Type()
)
fsQoSPortDefaultUserPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPortDefaultUserPriority.setStatus("current")


class _FsQoSPortPbitPrefOverDscp_Type(Integer32):
    """Custom type fsQoSPortPbitPrefOverDscp based on Integer32"""
    defaultValue = 1

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


_FsQoSPortPbitPrefOverDscp_Type.__name__ = "Integer32"
_FsQoSPortPbitPrefOverDscp_Object = MibTableColumn
fsQoSPortPbitPrefOverDscp = _FsQoSPortPbitPrefOverDscp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 4, 8, 1, 2),
    _FsQoSPortPbitPrefOverDscp_Type()
)
fsQoSPortPbitPrefOverDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSPortPbitPrefOverDscp.setStatus("current")
_FsQoSStats_ObjectIdentity = ObjectIdentity
fsQoSStats = _FsQoSStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 5)
)
_FsQoSPolicerStatsTable_Object = MibTable
fsQoSPolicerStatsTable = _FsQoSPolicerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 5, 1)
)
if mibBuilder.loadTexts:
    fsQoSPolicerStatsTable.setStatus("current")
_FsQoSPolicerStatsEntry_Object = MibTableRow
fsQoSPolicerStatsEntry = _FsQoSPolicerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 5, 1, 1)
)
fsQoSPolicerStatsEntry.setIndexNames(
    (0, "SUPERMICRO-QOS-MIB", "fsQoSMeterId"),
)
if mibBuilder.loadTexts:
    fsQoSPolicerStatsEntry.setStatus("current")
_FsQoSPolicerStatsConformPkts_Type = Counter64
_FsQoSPolicerStatsConformPkts_Object = MibTableColumn
fsQoSPolicerStatsConformPkts = _FsQoSPolicerStatsConformPkts_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 5, 1, 1, 1),
    _FsQoSPolicerStatsConformPkts_Type()
)
fsQoSPolicerStatsConformPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQoSPolicerStatsConformPkts.setStatus("current")
_FsQoSPolicerStatsConformOctets_Type = Counter64
_FsQoSPolicerStatsConformOctets_Object = MibTableColumn
fsQoSPolicerStatsConformOctets = _FsQoSPolicerStatsConformOctets_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 5, 1, 1, 2),
    _FsQoSPolicerStatsConformOctets_Type()
)
fsQoSPolicerStatsConformOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQoSPolicerStatsConformOctets.setStatus("current")
_FsQoSPolicerStatsExceedPkts_Type = Counter64
_FsQoSPolicerStatsExceedPkts_Object = MibTableColumn
fsQoSPolicerStatsExceedPkts = _FsQoSPolicerStatsExceedPkts_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 5, 1, 1, 3),
    _FsQoSPolicerStatsExceedPkts_Type()
)
fsQoSPolicerStatsExceedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQoSPolicerStatsExceedPkts.setStatus("current")
_FsQoSPolicerStatsExceedOctets_Type = Counter64
_FsQoSPolicerStatsExceedOctets_Object = MibTableColumn
fsQoSPolicerStatsExceedOctets = _FsQoSPolicerStatsExceedOctets_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 5, 1, 1, 4),
    _FsQoSPolicerStatsExceedOctets_Type()
)
fsQoSPolicerStatsExceedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQoSPolicerStatsExceedOctets.setStatus("current")
_FsQoSPolicerStatsViolatePkts_Type = Counter64
_FsQoSPolicerStatsViolatePkts_Object = MibTableColumn
fsQoSPolicerStatsViolatePkts = _FsQoSPolicerStatsViolatePkts_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 5, 1, 1, 5),
    _FsQoSPolicerStatsViolatePkts_Type()
)
fsQoSPolicerStatsViolatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQoSPolicerStatsViolatePkts.setStatus("current")
_FsQoSPolicerStatsViolateOctets_Type = Counter64
_FsQoSPolicerStatsViolateOctets_Object = MibTableColumn
fsQoSPolicerStatsViolateOctets = _FsQoSPolicerStatsViolateOctets_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 5, 1, 1, 6),
    _FsQoSPolicerStatsViolateOctets_Type()
)
fsQoSPolicerStatsViolateOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQoSPolicerStatsViolateOctets.setStatus("current")
_FsQoSCoSQStatsTable_Object = MibTable
fsQoSCoSQStatsTable = _FsQoSCoSQStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 5, 2)
)
if mibBuilder.loadTexts:
    fsQoSCoSQStatsTable.setStatus("current")
_FsQoSCoSQStatsEntry_Object = MibTableRow
fsQoSCoSQStatsEntry = _FsQoSCoSQStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 5, 2, 1)
)
fsQoSCoSQStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SUPERMICRO-QOS-MIB", "fsQoSCoSQId"),
)
if mibBuilder.loadTexts:
    fsQoSCoSQStatsEntry.setStatus("current")


class _FsQoSCoSQId_Type(Unsigned32):
    """Custom type fsQoSCoSQId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsQoSCoSQId_Type.__name__ = "Unsigned32"
_FsQoSCoSQId_Object = MibTableColumn
fsQoSCoSQId = _FsQoSCoSQId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 5, 2, 1, 1),
    _FsQoSCoSQId_Type()
)
fsQoSCoSQId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsQoSCoSQId.setStatus("current")
_FsQoSCoSQStatsEnQPkts_Type = Counter64
_FsQoSCoSQStatsEnQPkts_Object = MibTableColumn
fsQoSCoSQStatsEnQPkts = _FsQoSCoSQStatsEnQPkts_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 5, 2, 1, 2),
    _FsQoSCoSQStatsEnQPkts_Type()
)
fsQoSCoSQStatsEnQPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQoSCoSQStatsEnQPkts.setStatus("current")
_FsQoSCoSQStatsEnQBytes_Type = Counter64
_FsQoSCoSQStatsEnQBytes_Object = MibTableColumn
fsQoSCoSQStatsEnQBytes = _FsQoSCoSQStatsEnQBytes_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 5, 2, 1, 3),
    _FsQoSCoSQStatsEnQBytes_Type()
)
fsQoSCoSQStatsEnQBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQoSCoSQStatsEnQBytes.setStatus("current")
_FsQoSCoSQStatsDeQPkts_Type = Counter64
_FsQoSCoSQStatsDeQPkts_Object = MibTableColumn
fsQoSCoSQStatsDeQPkts = _FsQoSCoSQStatsDeQPkts_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 5, 2, 1, 4),
    _FsQoSCoSQStatsDeQPkts_Type()
)
fsQoSCoSQStatsDeQPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQoSCoSQStatsDeQPkts.setStatus("current")
_FsQoSCoSQStatsDeQBytes_Type = Counter64
_FsQoSCoSQStatsDeQBytes_Object = MibTableColumn
fsQoSCoSQStatsDeQBytes = _FsQoSCoSQStatsDeQBytes_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 5, 2, 1, 5),
    _FsQoSCoSQStatsDeQBytes_Type()
)
fsQoSCoSQStatsDeQBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQoSCoSQStatsDeQBytes.setStatus("current")
_FsQoSCoSQStatsDiscardPkts_Type = Counter64
_FsQoSCoSQStatsDiscardPkts_Object = MibTableColumn
fsQoSCoSQStatsDiscardPkts = _FsQoSCoSQStatsDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 5, 2, 1, 6),
    _FsQoSCoSQStatsDiscardPkts_Type()
)
fsQoSCoSQStatsDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQoSCoSQStatsDiscardPkts.setStatus("current")
_FsQoSCoSQStatsDiscardBytes_Type = Counter64
_FsQoSCoSQStatsDiscardBytes_Object = MibTableColumn
fsQoSCoSQStatsDiscardBytes = _FsQoSCoSQStatsDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 5, 2, 1, 7),
    _FsQoSCoSQStatsDiscardBytes_Type()
)
fsQoSCoSQStatsDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQoSCoSQStatsDiscardBytes.setStatus("current")
_FsQoSCoSQStatsOccupancy_Type = Counter64
_FsQoSCoSQStatsOccupancy_Object = MibTableColumn
fsQoSCoSQStatsOccupancy = _FsQoSCoSQStatsOccupancy_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 5, 2, 1, 8),
    _FsQoSCoSQStatsOccupancy_Type()
)
fsQoSCoSQStatsOccupancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQoSCoSQStatsOccupancy.setStatus("current")
_FsQoSCoSQStatsCongMgntAlgoDrop_Type = Counter64
_FsQoSCoSQStatsCongMgntAlgoDrop_Object = MibTableColumn
fsQoSCoSQStatsCongMgntAlgoDrop = _FsQoSCoSQStatsCongMgntAlgoDrop_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 5, 2, 1, 9),
    _FsQoSCoSQStatsCongMgntAlgoDrop_Type()
)
fsQoSCoSQStatsCongMgntAlgoDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQoSCoSQStatsCongMgntAlgoDrop.setStatus("current")
_FsQosHwCpuRateControl_ObjectIdentity = ObjectIdentity
fsQosHwCpuRateControl = _FsQosHwCpuRateControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 6)
)
_FsQosHwCpuRateLimitTable_Object = MibTable
fsQosHwCpuRateLimitTable = _FsQosHwCpuRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 6, 1)
)
if mibBuilder.loadTexts:
    fsQosHwCpuRateLimitTable.setStatus("current")
_FsQosHwCpuRateLimitEntry_Object = MibTableRow
fsQosHwCpuRateLimitEntry = _FsQosHwCpuRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 6, 1, 1)
)
fsQosHwCpuRateLimitEntry.setIndexNames(
    (0, "SUPERMICRO-QOS-MIB", "fsQosHwCpuQId"),
)
if mibBuilder.loadTexts:
    fsQosHwCpuRateLimitEntry.setStatus("current")


class _FsQosHwCpuQId_Type(Unsigned32):
    """Custom type fsQosHwCpuQId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsQosHwCpuQId_Type.__name__ = "Unsigned32"
_FsQosHwCpuQId_Object = MibTableColumn
fsQosHwCpuQId = _FsQosHwCpuQId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 6, 1, 1, 1),
    _FsQosHwCpuQId_Type()
)
fsQosHwCpuQId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsQosHwCpuQId.setStatus("current")


class _FsQosHwCpuMinRate_Type(Unsigned32):
    """Custom type fsQosHwCpuMinRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsQosHwCpuMinRate_Type.__name__ = "Unsigned32"
_FsQosHwCpuMinRate_Object = MibTableColumn
fsQosHwCpuMinRate = _FsQosHwCpuMinRate_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 6, 1, 1, 2),
    _FsQosHwCpuMinRate_Type()
)
fsQosHwCpuMinRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQosHwCpuMinRate.setStatus("current")


class _FsQosHwCpuMaxRate_Type(Unsigned32):
    """Custom type fsQosHwCpuMaxRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsQosHwCpuMaxRate_Type.__name__ = "Unsigned32"
_FsQosHwCpuMaxRate_Object = MibTableColumn
fsQosHwCpuMaxRate = _FsQosHwCpuMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 6, 1, 1, 3),
    _FsQosHwCpuMaxRate_Type()
)
fsQosHwCpuMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQosHwCpuMaxRate.setStatus("current")
_FsQosHwCpuRowStatus_Type = RowStatus
_FsQosHwCpuRowStatus_Object = MibTableColumn
fsQosHwCpuRowStatus = _FsQosHwCpuRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 6, 1, 6, 1, 1, 4),
    _FsQosHwCpuRowStatus_Type()
)
fsQosHwCpuRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsQosHwCpuRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-QOS-MIB",
    **{"Dscp": Dscp,
       "MeterColorMode": MeterColorMode,
       "MeterType": MeterType,
       "EnableStatus": EnableStatus,
       "SchedulerPriority": SchedulerPriority,
       "IndexInteger": IndexInteger,
       "fsQoSMib": fsQoSMib,
       "fsQoSMIBObjects": fsQoSMIBObjects,
       "fsQoSSystem": fsQoSSystem,
       "fsQoSSystemControl": fsQoSSystemControl,
       "fsQoSStatus": fsQoSStatus,
       "fsQoSTrcFlag": fsQoSTrcFlag,
       "fsQoSRateUnit": fsQoSRateUnit,
       "fsQoSRateGranularity": fsQoSRateGranularity,
       "fsQoSClass": fsQoSClass,
       "fsQoSPriorityMapTable": fsQoSPriorityMapTable,
       "fsQoSPriorityMapEntry": fsQoSPriorityMapEntry,
       "fsQoSPriorityMapID": fsQoSPriorityMapID,
       "fsQoSPriorityMapName": fsQoSPriorityMapName,
       "fsQoSPriorityMapIfIndex": fsQoSPriorityMapIfIndex,
       "fsQoSPriorityMapVlanId": fsQoSPriorityMapVlanId,
       "fsQoSPriorityMapInPriority": fsQoSPriorityMapInPriority,
       "fsQoSPriorityMapInPriType": fsQoSPriorityMapInPriType,
       "fsQoSPriorityMapRegenPriority": fsQoSPriorityMapRegenPriority,
       "fsQoSPriorityMapRegenInnerPriority": fsQoSPriorityMapRegenInnerPriority,
       "fsQoSPriorityMapConfigStatus": fsQoSPriorityMapConfigStatus,
       "fsQoSPriorityMapStatus": fsQoSPriorityMapStatus,
       "fsQoSClassMapTable": fsQoSClassMapTable,
       "fsQoSClassMapEntry": fsQoSClassMapEntry,
       "fsQoSClassMapId": fsQoSClassMapId,
       "fsQoSClassMapName": fsQoSClassMapName,
       "fsQoSClassMapL2FilterId": fsQoSClassMapL2FilterId,
       "fsQoSClassMapL3FilterId": fsQoSClassMapL3FilterId,
       "fsQoSClassMapPriorityMapId": fsQoSClassMapPriorityMapId,
       "fsQoSClassMapCLASS": fsQoSClassMapCLASS,
       "fsQoSClassMapClfrId": fsQoSClassMapClfrId,
       "fsQoSClassMapPreColor": fsQoSClassMapPreColor,
       "fsQoSClassMapStatus": fsQoSClassMapStatus,
       "fsQoSClassToPriorityTable": fsQoSClassToPriorityTable,
       "fsQoSClassToPriorityEntry": fsQoSClassToPriorityEntry,
       "fsQoSClassToPriorityCLASS": fsQoSClassToPriorityCLASS,
       "fsQoSClassToPriorityRegenPri": fsQoSClassToPriorityRegenPri,
       "fsQoSClassToPriorityGroupName": fsQoSClassToPriorityGroupName,
       "fsQoSClassToPriorityStatus": fsQoSClassToPriorityStatus,
       "fsQoSPolicy": fsQoSPolicy,
       "fsQoSMeterTable": fsQoSMeterTable,
       "fsQoSMeterEntry": fsQoSMeterEntry,
       "fsQoSMeterId": fsQoSMeterId,
       "fsQoSMeterName": fsQoSMeterName,
       "fsQoSMeterType": fsQoSMeterType,
       "fsQoSMeterInterval": fsQoSMeterInterval,
       "fsQoSMeterColorMode": fsQoSMeterColorMode,
       "fsQoSMeterCIR": fsQoSMeterCIR,
       "fsQoSMeterCBS": fsQoSMeterCBS,
       "fsQoSMeterEIR": fsQoSMeterEIR,
       "fsQoSMeterEBS": fsQoSMeterEBS,
       "fsQoSMeterNext": fsQoSMeterNext,
       "fsQoSMeterStatus": fsQoSMeterStatus,
       "fsQoSPolicyMapTable": fsQoSPolicyMapTable,
       "fsQoSPolicyMapEntry": fsQoSPolicyMapEntry,
       "fsQoSPolicyMapId": fsQoSPolicyMapId,
       "fsQoSPolicyMapName": fsQoSPolicyMapName,
       "fsQoSPolicyMapIfIndex": fsQoSPolicyMapIfIndex,
       "fsQoSPolicyMapCLASS": fsQoSPolicyMapCLASS,
       "fsQoSPolicyMapPHBType": fsQoSPolicyMapPHBType,
       "fsQoSPolicyMapDefaultPHB": fsQoSPolicyMapDefaultPHB,
       "fsQoSPolicyMapMeterTableId": fsQoSPolicyMapMeterTableId,
       "fsQoSPolicyMapFailMeterTableId": fsQoSPolicyMapFailMeterTableId,
       "fsQoSPolicyMapInProfileConformActionFlag": fsQoSPolicyMapInProfileConformActionFlag,
       "fsQoSPolicyMapInProfileConformActionId": fsQoSPolicyMapInProfileConformActionId,
       "fsQoSPolicyMapInProfileActionSetPort": fsQoSPolicyMapInProfileActionSetPort,
       "fsQoSPolicyMapConformActionSetIpTOS": fsQoSPolicyMapConformActionSetIpTOS,
       "fsQoSPolicyMapConformActionSetDscp": fsQoSPolicyMapConformActionSetDscp,
       "fsQoSPolicyMapConformActionSetVlanPrio": fsQoSPolicyMapConformActionSetVlanPrio,
       "fsQoSPolicyMapConformActionSetVlanDE": fsQoSPolicyMapConformActionSetVlanDE,
       "fsQoSPolicyMapConformActionSetInnerVlanPrio": fsQoSPolicyMapConformActionSetInnerVlanPrio,
       "fsQoSPolicyMapConformActionSetMplsExp": fsQoSPolicyMapConformActionSetMplsExp,
       "fsQoSPolicyMapConformActionSetNewCLASS": fsQoSPolicyMapConformActionSetNewCLASS,
       "fsQoSPolicyMapInProfileExceedActionFlag": fsQoSPolicyMapInProfileExceedActionFlag,
       "fsQoSPolicyMapInProfileExceedActionId": fsQoSPolicyMapInProfileExceedActionId,
       "fsQoSPolicyMapExceedActionSetIpTOS": fsQoSPolicyMapExceedActionSetIpTOS,
       "fsQoSPolicyMapExceedActionSetDscp": fsQoSPolicyMapExceedActionSetDscp,
       "fsQoSPolicyMapExceedActionSetInnerVlanPrio": fsQoSPolicyMapExceedActionSetInnerVlanPrio,
       "fsQoSPolicyMapExceedActionSetVlanPrio": fsQoSPolicyMapExceedActionSetVlanPrio,
       "fsQoSPolicyMapExceedActionSetVlanDE": fsQoSPolicyMapExceedActionSetVlanDE,
       "fsQoSPolicyMapExceedActionSetMplsExp": fsQoSPolicyMapExceedActionSetMplsExp,
       "fsQoSPolicyMapExceedActionSetNewCLASS": fsQoSPolicyMapExceedActionSetNewCLASS,
       "fsQoSPolicyMapOutProfileActionFlag": fsQoSPolicyMapOutProfileActionFlag,
       "fsQoSPolicyMapOutProfileActionId": fsQoSPolicyMapOutProfileActionId,
       "fsQoSPolicyMapOutProfileActionSetIPTOS": fsQoSPolicyMapOutProfileActionSetIPTOS,
       "fsQoSPolicyMapOutProfileActionSetDscp": fsQoSPolicyMapOutProfileActionSetDscp,
       "fsQoSPolicyMapOutProfileActionSetInnerVlanPrio": fsQoSPolicyMapOutProfileActionSetInnerVlanPrio,
       "fsQoSPolicyMapOutProfileActionSetVlanPrio": fsQoSPolicyMapOutProfileActionSetVlanPrio,
       "fsQoSPolicyMapOutProfileActionSetVlanDE": fsQoSPolicyMapOutProfileActionSetVlanDE,
       "fsQoSPolicyMapOutProfileActionSetMplsExp": fsQoSPolicyMapOutProfileActionSetMplsExp,
       "fsQoSPolicyMapOutProfileActionSetNewCLASS": fsQoSPolicyMapOutProfileActionSetNewCLASS,
       "fsQoSPolicyMapStatus": fsQoSPolicyMapStatus,
       "fsQoSTrafficMgmt": fsQoSTrafficMgmt,
       "fsQoSQTemplateTable": fsQoSQTemplateTable,
       "fsQoSQTemplateEntry": fsQoSQTemplateEntry,
       "fsQoSQTemplateId": fsQoSQTemplateId,
       "fsQoSQTemplateName": fsQoSQTemplateName,
       "fsQoSQTemplateDropType": fsQoSQTemplateDropType,
       "fsQoSQTemplateDropAlgoEnableFlag": fsQoSQTemplateDropAlgoEnableFlag,
       "fsQoSQTemplateSize": fsQoSQTemplateSize,
       "fsQoSQTemplateStatus": fsQoSQTemplateStatus,
       "fsQoSRandomDetectCfgTable": fsQoSRandomDetectCfgTable,
       "fsQoSRandomDetectCfgEntry": fsQoSRandomDetectCfgEntry,
       "fsQoSRandomDetectCfgDP": fsQoSRandomDetectCfgDP,
       "fsQoSRandomDetectCfgMinAvgThresh": fsQoSRandomDetectCfgMinAvgThresh,
       "fsQoSRandomDetectCfgMaxAvgThresh": fsQoSRandomDetectCfgMaxAvgThresh,
       "fsQoSRandomDetectCfgMaxPktSize": fsQoSRandomDetectCfgMaxPktSize,
       "fsQoSRandomDetectCfgMaxProb": fsQoSRandomDetectCfgMaxProb,
       "fsQoSRandomDetectCfgExpWeight": fsQoSRandomDetectCfgExpWeight,
       "fsQoSRandomDetectCfgStatus": fsQoSRandomDetectCfgStatus,
       "fsQoSShapeTemplateTable": fsQoSShapeTemplateTable,
       "fsQoSShapeTemplateEntry": fsQoSShapeTemplateEntry,
       "fsQoSShapeTemplateId": fsQoSShapeTemplateId,
       "fsQoSShapeTemplateName": fsQoSShapeTemplateName,
       "fsQoSShapeTemplateCIR": fsQoSShapeTemplateCIR,
       "fsQoSShapeTemplateCBS": fsQoSShapeTemplateCBS,
       "fsQoSShapeTemplateEIR": fsQoSShapeTemplateEIR,
       "fsQoSShapeTemplateEBS": fsQoSShapeTemplateEBS,
       "fsQoSShapeTemplateStatus": fsQoSShapeTemplateStatus,
       "fsQoSQMapTable": fsQoSQMapTable,
       "fsQoSQMapEntry": fsQoSQMapEntry,
       "fsQoSQMapCLASS": fsQoSQMapCLASS,
       "fsQoSQMapRegenPriType": fsQoSQMapRegenPriType,
       "fsQoSQMapRegenPriority": fsQoSQMapRegenPriority,
       "fsQoSQMapQId": fsQoSQMapQId,
       "fsQoSQMapStatus": fsQoSQMapStatus,
       "fsQoSQTable": fsQoSQTable,
       "fsQoSQEntry": fsQoSQEntry,
       "fsQoSQId": fsQoSQId,
       "fsQoSQCfgTemplateId": fsQoSQCfgTemplateId,
       "fsQoSQSchedulerId": fsQoSQSchedulerId,
       "fsQoSQWeight": fsQoSQWeight,
       "fsQoSQPriority": fsQoSQPriority,
       "fsQoSQShapeId": fsQoSQShapeId,
       "fsQoSQStatus": fsQoSQStatus,
       "fsQoSQType": fsQoSQType,
       "fsQoSSchedulerTable": fsQoSSchedulerTable,
       "fsQoSSchedulerEntry": fsQoSSchedulerEntry,
       "fsQoSSchedulerId": fsQoSSchedulerId,
       "fsQoSSchedulerSchedAlgorithm": fsQoSSchedulerSchedAlgorithm,
       "fsQoSSchedulerShapeId": fsQoSSchedulerShapeId,
       "fsQoSSchedulerHierarchyLevel": fsQoSSchedulerHierarchyLevel,
       "fsQoSSchedulerGlobalId": fsQoSSchedulerGlobalId,
       "fsQoSSchedulerStatus": fsQoSSchedulerStatus,
       "fsQoSHierarchyTable": fsQoSHierarchyTable,
       "fsQoSHierarchyEntry": fsQoSHierarchyEntry,
       "fsQoSHierarchyLevel": fsQoSHierarchyLevel,
       "fsQoSHierarchyQNext": fsQoSHierarchyQNext,
       "fsQoSHierarchySchedNext": fsQoSHierarchySchedNext,
       "fsQoSHierarchyWeight": fsQoSHierarchyWeight,
       "fsQoSHierarchyPriority": fsQoSHierarchyPriority,
       "fsQoSHierarchyStatus": fsQoSHierarchyStatus,
       "fsQoSDefUserPriorityTable": fsQoSDefUserPriorityTable,
       "fsQoSDefUserPriorityEntry": fsQoSDefUserPriorityEntry,
       "fsQoSPortDefaultUserPriority": fsQoSPortDefaultUserPriority,
       "fsQoSPortPbitPrefOverDscp": fsQoSPortPbitPrefOverDscp,
       "fsQoSStats": fsQoSStats,
       "fsQoSPolicerStatsTable": fsQoSPolicerStatsTable,
       "fsQoSPolicerStatsEntry": fsQoSPolicerStatsEntry,
       "fsQoSPolicerStatsConformPkts": fsQoSPolicerStatsConformPkts,
       "fsQoSPolicerStatsConformOctets": fsQoSPolicerStatsConformOctets,
       "fsQoSPolicerStatsExceedPkts": fsQoSPolicerStatsExceedPkts,
       "fsQoSPolicerStatsExceedOctets": fsQoSPolicerStatsExceedOctets,
       "fsQoSPolicerStatsViolatePkts": fsQoSPolicerStatsViolatePkts,
       "fsQoSPolicerStatsViolateOctets": fsQoSPolicerStatsViolateOctets,
       "fsQoSCoSQStatsTable": fsQoSCoSQStatsTable,
       "fsQoSCoSQStatsEntry": fsQoSCoSQStatsEntry,
       "fsQoSCoSQId": fsQoSCoSQId,
       "fsQoSCoSQStatsEnQPkts": fsQoSCoSQStatsEnQPkts,
       "fsQoSCoSQStatsEnQBytes": fsQoSCoSQStatsEnQBytes,
       "fsQoSCoSQStatsDeQPkts": fsQoSCoSQStatsDeQPkts,
       "fsQoSCoSQStatsDeQBytes": fsQoSCoSQStatsDeQBytes,
       "fsQoSCoSQStatsDiscardPkts": fsQoSCoSQStatsDiscardPkts,
       "fsQoSCoSQStatsDiscardBytes": fsQoSCoSQStatsDiscardBytes,
       "fsQoSCoSQStatsOccupancy": fsQoSCoSQStatsOccupancy,
       "fsQoSCoSQStatsCongMgntAlgoDrop": fsQoSCoSQStatsCongMgntAlgoDrop,
       "fsQosHwCpuRateControl": fsQosHwCpuRateControl,
       "fsQosHwCpuRateLimitTable": fsQosHwCpuRateLimitTable,
       "fsQosHwCpuRateLimitEntry": fsQosHwCpuRateLimitEntry,
       "fsQosHwCpuQId": fsQosHwCpuQId,
       "fsQosHwCpuMinRate": fsQosHwCpuMinRate,
       "fsQosHwCpuMaxRate": fsQosHwCpuMaxRate,
       "fsQosHwCpuRowStatus": fsQosHwCpuRowStatus}
)
