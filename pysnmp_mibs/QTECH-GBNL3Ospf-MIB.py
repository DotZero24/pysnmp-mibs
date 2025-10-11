# SNMP MIB module (QTECH-GBNL3Ospf-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-GBNL3Ospf-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:58:02 2025
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

(gbnL3,) = mibBuilder.importSymbols(
    "QTECH-MASTER-MIB",
    "gbnL3")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

gbnL3OspfMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 3)
)
if mibBuilder.loadTexts:
    gbnL3OspfMib.setRevisions(
        ("1903-08-18 00:01",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Metric(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )



# MIB Managed Objects in the order of their OIDs

_GbnL3OspfGroup_ObjectIdentity = ObjectIdentity
gbnL3OspfGroup = _GbnL3OspfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 3, 1)
)


class _OspfRedistriDefaultMetric_Type(Metric):
    """Custom type ospfRedistriDefaultMetric based on Metric"""
    defaultValue = 1


_OspfRedistriDefaultMetric_Type.__name__ = "Metric"
_OspfRedistriDefaultMetric_Object = MibScalar
ospfRedistriDefaultMetric = _OspfRedistriDefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 3, 1, 1),
    _OspfRedistriDefaultMetric_Type()
)
ospfRedistriDefaultMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfRedistriDefaultMetric.setStatus("current")


class _OspfRedistriDefaultType_Type(Integer32):
    """Custom type ospfRedistriDefaultType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("type1", 1),
          ("type2", 2))
    )


_OspfRedistriDefaultType_Type.__name__ = "Integer32"
_OspfRedistriDefaultType_Object = MibScalar
ospfRedistriDefaultType = _OspfRedistriDefaultType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 3, 1, 2),
    _OspfRedistriDefaultType_Type()
)
ospfRedistriDefaultType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfRedistriDefaultType.setStatus("current")


class _OspfRedistriDefaultTag_Type(Integer32):
    """Custom type ospfRedistriDefaultTag based on Integer32"""
    defaultValue = 10


_OspfRedistriDefaultTag_Type.__name__ = "Integer32"
_OspfRedistriDefaultTag_Object = MibScalar
ospfRedistriDefaultTag = _OspfRedistriDefaultTag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 3, 1, 3),
    _OspfRedistriDefaultTag_Type()
)
ospfRedistriDefaultTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfRedistriDefaultTag.setStatus("current")


class _OspfRedistriDefaultInterval_Type(Integer32):
    """Custom type ospfRedistriDefaultInterval based on Integer32"""
    defaultValue = 1


_OspfRedistriDefaultInterval_Type.__name__ = "Integer32"
_OspfRedistriDefaultInterval_Object = MibScalar
ospfRedistriDefaultInterval = _OspfRedistriDefaultInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 3, 1, 4),
    _OspfRedistriDefaultInterval_Type()
)
ospfRedistriDefaultInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfRedistriDefaultInterval.setStatus("current")


class _OspfRedistriDefaultLimit_Type(Integer32):
    """Custom type ospfRedistriDefaultLimit based on Integer32"""
    defaultValue = 1000


_OspfRedistriDefaultLimit_Type.__name__ = "Integer32"
_OspfRedistriDefaultLimit_Object = MibScalar
ospfRedistriDefaultLimit = _OspfRedistriDefaultLimit_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 3, 1, 5),
    _OspfRedistriDefaultLimit_Type()
)
ospfRedistriDefaultLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfRedistriDefaultLimit.setStatus("current")
_OspfRedistributeTable_Object = MibTable
ospfRedistributeTable = _OspfRedistributeTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 3, 2)
)
if mibBuilder.loadTexts:
    ospfRedistributeTable.setStatus("current")
_OspfRedistributeEntry_Object = MibTableRow
ospfRedistributeEntry = _OspfRedistributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 3, 2, 1)
)
ospfRedistributeEntry.setIndexNames(
    (0, "QTECH-GBNL3Ospf-MIB", "ospfRedistributeProtocal"),
)
if mibBuilder.loadTexts:
    ospfRedistributeEntry.setStatus("current")
_OspfRedistributeProtocal_Type = Integer32
_OspfRedistributeProtocal_Object = MibTableColumn
ospfRedistributeProtocal = _OspfRedistributeProtocal_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 3, 2, 1, 1),
    _OspfRedistributeProtocal_Type()
)
ospfRedistributeProtocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfRedistributeProtocal.setStatus("current")
_OspfRedistributeMetric_Type = Metric
_OspfRedistributeMetric_Object = MibTableColumn
ospfRedistributeMetric = _OspfRedistributeMetric_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 3, 2, 1, 2),
    _OspfRedistributeMetric_Type()
)
ospfRedistributeMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfRedistributeMetric.setStatus("current")


class _OspfRedistributeType_Type(Integer32):
    """Custom type ospfRedistributeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("type1", 1),
          ("type2", 2))
    )


_OspfRedistributeType_Type.__name__ = "Integer32"
_OspfRedistributeType_Object = MibTableColumn
ospfRedistributeType = _OspfRedistributeType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 3, 2, 1, 3),
    _OspfRedistributeType_Type()
)
ospfRedistributeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfRedistributeType.setStatus("current")
_OspfRedistributeTag_Type = Integer32
_OspfRedistributeTag_Object = MibTableColumn
ospfRedistributeTag = _OspfRedistributeTag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 3, 2, 1, 4),
    _OspfRedistributeTag_Type()
)
ospfRedistributeTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfRedistributeTag.setStatus("current")
_OspfRedistributeStatus_Type = RowStatus
_OspfRedistributeStatus_Object = MibTableColumn
ospfRedistributeStatus = _OspfRedistributeStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 3, 2, 1, 5),
    _OspfRedistributeStatus_Type()
)
ospfRedistributeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfRedistributeStatus.setStatus("current")
_OspfRedistributeAlways_Type = TruthValue
_OspfRedistributeAlways_Object = MibTableColumn
ospfRedistributeAlways = _OspfRedistributeAlways_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 3, 2, 1, 6),
    _OspfRedistributeAlways_Type()
)
ospfRedistributeAlways.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfRedistributeAlways.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-GBNL3Ospf-MIB",
    **{"Metric": Metric,
       "gbnL3OspfMib": gbnL3OspfMib,
       "gbnL3OspfGroup": gbnL3OspfGroup,
       "ospfRedistriDefaultMetric": ospfRedistriDefaultMetric,
       "ospfRedistriDefaultType": ospfRedistriDefaultType,
       "ospfRedistriDefaultTag": ospfRedistriDefaultTag,
       "ospfRedistriDefaultInterval": ospfRedistriDefaultInterval,
       "ospfRedistriDefaultLimit": ospfRedistriDefaultLimit,
       "ospfRedistributeTable": ospfRedistributeTable,
       "ospfRedistributeEntry": ospfRedistributeEntry,
       "ospfRedistributeProtocal": ospfRedistributeProtocal,
       "ospfRedistributeMetric": ospfRedistributeMetric,
       "ospfRedistributeType": ospfRedistributeType,
       "ospfRedistributeTag": ospfRedistributeTag,
       "ospfRedistributeStatus": ospfRedistributeStatus,
       "ospfRedistributeAlways": ospfRedistributeAlways}
)
