# SNMP MIB module (H3C-MPLSTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-MPLSTE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:17:31 2025
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cMplsTe = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 143)
)
if mibBuilder.loadTexts:
    h3cMplsTe.setRevisions(
        ("2013-06-13 18:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cMplsTeObjects_ObjectIdentity = ObjectIdentity
h3cMplsTeObjects = _H3cMplsTeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 143, 1)
)
_H3cMplsTeScalarGroup_ObjectIdentity = ObjectIdentity
h3cMplsTeScalarGroup = _H3cMplsTeScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 143, 1, 1)
)
_H3cMplsTeStatus_Type = TruthValue
_H3cMplsTeStatus_Object = MibScalar
h3cMplsTeStatus = _H3cMplsTeStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 143, 1, 1, 1),
    _H3cMplsTeStatus_Type()
)
h3cMplsTeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMplsTeStatus.setStatus("current")
_H3cMplsTeRsvpStatus_Type = TruthValue
_H3cMplsTeRsvpStatus_Object = MibScalar
h3cMplsTeRsvpStatus = _H3cMplsTeRsvpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 143, 1, 1, 2),
    _H3cMplsTeRsvpStatus_Type()
)
h3cMplsTeRsvpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMplsTeRsvpStatus.setStatus("current")
_H3cMplsTeTable_Object = MibTable
h3cMplsTeTable = _H3cMplsTeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 143, 1, 2)
)
if mibBuilder.loadTexts:
    h3cMplsTeTable.setStatus("current")
_H3cMplsTeEntry_Object = MibTableRow
h3cMplsTeEntry = _H3cMplsTeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 143, 1, 2, 1)
)
h3cMplsTeEntry.setIndexNames(
    (0, "H3C-MPLSTE-MIB", "h3cMplsTeIndex"),
)
if mibBuilder.loadTexts:
    h3cMplsTeEntry.setStatus("current")


class _H3cMplsTeIndex_Type(Unsigned32):
    """Custom type h3cMplsTeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_H3cMplsTeIndex_Type.__name__ = "Unsigned32"
_H3cMplsTeIndex_Object = MibTableColumn
h3cMplsTeIndex = _H3cMplsTeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 143, 1, 2, 1, 1),
    _H3cMplsTeIndex_Type()
)
h3cMplsTeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMplsTeIndex.setStatus("current")


class _H3cMplsTeCapability_Type(TruthValue):
    """Custom type h3cMplsTeCapability based on TruthValue"""
    defaultValue = 2


_H3cMplsTeCapability_Type.__name__ = "TruthValue"
_H3cMplsTeCapability_Object = MibTableColumn
h3cMplsTeCapability = _H3cMplsTeCapability_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 143, 1, 2, 1, 2),
    _H3cMplsTeCapability_Type()
)
h3cMplsTeCapability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMplsTeCapability.setStatus("current")
_H3cMplsTeRowStatus_Type = RowStatus
_H3cMplsTeRowStatus_Object = MibTableColumn
h3cMplsTeRowStatus = _H3cMplsTeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 143, 1, 2, 1, 3),
    _H3cMplsTeRowStatus_Type()
)
h3cMplsTeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMplsTeRowStatus.setStatus("current")
_H3cMplsTeRsvpTable_Object = MibTable
h3cMplsTeRsvpTable = _H3cMplsTeRsvpTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 143, 1, 3)
)
if mibBuilder.loadTexts:
    h3cMplsTeRsvpTable.setStatus("current")
_H3cMplsTeRsvpEntry_Object = MibTableRow
h3cMplsTeRsvpEntry = _H3cMplsTeRsvpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 143, 1, 3, 1)
)
h3cMplsTeRsvpEntry.setIndexNames(
    (0, "H3C-MPLSTE-MIB", "h3cMplsTeRsvpIndex"),
)
if mibBuilder.loadTexts:
    h3cMplsTeRsvpEntry.setStatus("current")


class _H3cMplsTeRsvpIndex_Type(Unsigned32):
    """Custom type h3cMplsTeRsvpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_H3cMplsTeRsvpIndex_Type.__name__ = "Unsigned32"
_H3cMplsTeRsvpIndex_Object = MibTableColumn
h3cMplsTeRsvpIndex = _H3cMplsTeRsvpIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 143, 1, 3, 1, 1),
    _H3cMplsTeRsvpIndex_Type()
)
h3cMplsTeRsvpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMplsTeRsvpIndex.setStatus("current")


class _H3cMplsTeRsvpCapability_Type(TruthValue):
    """Custom type h3cMplsTeRsvpCapability based on TruthValue"""
    defaultValue = 2


_H3cMplsTeRsvpCapability_Type.__name__ = "TruthValue"
_H3cMplsTeRsvpCapability_Object = MibTableColumn
h3cMplsTeRsvpCapability = _H3cMplsTeRsvpCapability_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 143, 1, 3, 1, 2),
    _H3cMplsTeRsvpCapability_Type()
)
h3cMplsTeRsvpCapability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMplsTeRsvpCapability.setStatus("current")
_H3cMplsTeRsvpRowStatus_Type = RowStatus
_H3cMplsTeRsvpRowStatus_Object = MibTableColumn
h3cMplsTeRsvpRowStatus = _H3cMplsTeRsvpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 143, 1, 3, 1, 3),
    _H3cMplsTeRsvpRowStatus_Type()
)
h3cMplsTeRsvpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMplsTeRsvpRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-MPLSTE-MIB",
    **{"h3cMplsTe": h3cMplsTe,
       "h3cMplsTeObjects": h3cMplsTeObjects,
       "h3cMplsTeScalarGroup": h3cMplsTeScalarGroup,
       "h3cMplsTeStatus": h3cMplsTeStatus,
       "h3cMplsTeRsvpStatus": h3cMplsTeRsvpStatus,
       "h3cMplsTeTable": h3cMplsTeTable,
       "h3cMplsTeEntry": h3cMplsTeEntry,
       "h3cMplsTeIndex": h3cMplsTeIndex,
       "h3cMplsTeCapability": h3cMplsTeCapability,
       "h3cMplsTeRowStatus": h3cMplsTeRowStatus,
       "h3cMplsTeRsvpTable": h3cMplsTeRsvpTable,
       "h3cMplsTeRsvpEntry": h3cMplsTeRsvpEntry,
       "h3cMplsTeRsvpIndex": h3cMplsTeRsvpIndex,
       "h3cMplsTeRsvpCapability": h3cMplsTeRsvpCapability,
       "h3cMplsTeRsvpRowStatus": h3cMplsTeRsvpRowStatus}
)
