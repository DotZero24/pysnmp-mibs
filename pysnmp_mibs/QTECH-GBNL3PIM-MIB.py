# SNMP MIB module (QTECH-GBNL3PIM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-GBNL3PIM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:57:18 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
    "iso")

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

gbnL3PimMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 8)
)
if mibBuilder.loadTexts:
    gbnL3PimMib.setRevisions(
        ("1905-07-04 00:01",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GbnL3PimGroup_ObjectIdentity = ObjectIdentity
gbnL3PimGroup = _GbnL3PimGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 8, 1)
)
_PimCommonTraceOption_Type = Unsigned32
_PimCommonTraceOption_Object = MibScalar
pimCommonTraceOption = _PimCommonTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 8, 1, 1),
    _PimCommonTraceOption_Type()
)
pimCommonTraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pimCommonTraceOption.setStatus("current")
_PimDmTraceOption_Type = Unsigned32
_PimDmTraceOption_Object = MibScalar
pimDmTraceOption = _PimDmTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 8, 1, 2),
    _PimDmTraceOption_Type()
)
pimDmTraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pimDmTraceOption.setStatus("current")
_PimSmTraceOption_Type = Unsigned32
_PimSmTraceOption_Object = MibScalar
pimSmTraceOption = _PimSmTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 8, 1, 3),
    _PimSmTraceOption_Type()
)
pimSmTraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pimSmTraceOption.setStatus("current")


class _PimSourcePolicy_Type(Integer32):
    """Custom type pimSourcePolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_PimSourcePolicy_Type.__name__ = "Integer32"
_PimSourcePolicy_Object = MibScalar
pimSourcePolicy = _PimSourcePolicy_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 8, 1, 4),
    _PimSourcePolicy_Type()
)
pimSourcePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pimSourcePolicy.setStatus("current")
_PimInterfaceExtraTable_Object = MibTable
pimInterfaceExtraTable = _PimInterfaceExtraTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 8, 2)
)
if mibBuilder.loadTexts:
    pimInterfaceExtraTable.setStatus("current")
_PimInterfaceExtraEntry_Object = MibTableRow
pimInterfaceExtraEntry = _PimInterfaceExtraEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 8, 2, 1)
)
pimInterfaceExtraEntry.setIndexNames(
    (0, "QTECH-GBNL3PIM-MIB", "pimInterfaceIndex"),
)
if mibBuilder.loadTexts:
    pimInterfaceExtraEntry.setStatus("current")
_PimInterfaceIndex_Type = InterfaceIndex
_PimInterfaceIndex_Object = MibTableColumn
pimInterfaceIndex = _PimInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 8, 2, 1, 1),
    _PimInterfaceIndex_Type()
)
pimInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimInterfaceIndex.setStatus("current")


class _PimInterfaceNeighborLimit_Type(Integer32):
    """Custom type pimInterfaceNeighborLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_PimInterfaceNeighborLimit_Type.__name__ = "Integer32"
_PimInterfaceNeighborLimit_Object = MibTableColumn
pimInterfaceNeighborLimit = _PimInterfaceNeighborLimit_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 8, 2, 1, 2),
    _PimInterfaceNeighborLimit_Type()
)
pimInterfaceNeighborLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pimInterfaceNeighborLimit.setStatus("current")


class _PimInterfaceNeighborPolicy_Type(Integer32):
    """Custom type pimInterfaceNeighborPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_PimInterfaceNeighborPolicy_Type.__name__ = "Integer32"
_PimInterfaceNeighborPolicy_Object = MibTableColumn
pimInterfaceNeighborPolicy = _PimInterfaceNeighborPolicy_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 8, 2, 1, 3),
    _PimInterfaceNeighborPolicy_Type()
)
pimInterfaceNeighborPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pimInterfaceNeighborPolicy.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-GBNL3PIM-MIB",
    **{"gbnL3PimMib": gbnL3PimMib,
       "gbnL3PimGroup": gbnL3PimGroup,
       "pimCommonTraceOption": pimCommonTraceOption,
       "pimDmTraceOption": pimDmTraceOption,
       "pimSmTraceOption": pimSmTraceOption,
       "pimSourcePolicy": pimSourcePolicy,
       "pimInterfaceExtraTable": pimInterfaceExtraTable,
       "pimInterfaceExtraEntry": pimInterfaceExtraEntry,
       "pimInterfaceIndex": pimInterfaceIndex,
       "pimInterfaceNeighborLimit": pimInterfaceNeighborLimit,
       "pimInterfaceNeighborPolicy": pimInterfaceNeighborPolicy}
)
