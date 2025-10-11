# SNMP MIB module (SUPERMICRO-MPLS-LSR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-MPLS-LSR-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:03:22 2025
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

(mplsInSegmentEntry,
 mplsOutSegmentEntry) = mibBuilder.importSymbols(
    "MPLS-LSR-STD-MIB",
    "mplsInSegmentEntry",
    "mplsOutSegmentEntry")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsMplsLsrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 13)
)
if mibBuilder.loadTexts:
    fsMplsLsrMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsMplsLsrNotifications_ObjectIdentity = ObjectIdentity
fsMplsLsrNotifications = _FsMplsLsrNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 13, 0)
)
_FsMplsLsrObjects_ObjectIdentity = ObjectIdentity
fsMplsLsrObjects = _FsMplsLsrObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 13, 1)
)
_FsMplsLsrScalarObjects_ObjectIdentity = ObjectIdentity
fsMplsLsrScalarObjects = _FsMplsLsrScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 13, 1, 1)
)


class _FsMplsLsrRfc6428CompatibleCodePoint_Type(TruthValue):
    """Custom type fsMplsLsrRfc6428CompatibleCodePoint based on TruthValue"""
    defaultValue = 2


_FsMplsLsrRfc6428CompatibleCodePoint_Type.__name__ = "TruthValue"
_FsMplsLsrRfc6428CompatibleCodePoint_Object = MibScalar
fsMplsLsrRfc6428CompatibleCodePoint = _FsMplsLsrRfc6428CompatibleCodePoint_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 13, 1, 1, 1),
    _FsMplsLsrRfc6428CompatibleCodePoint_Type()
)
fsMplsLsrRfc6428CompatibleCodePoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsLsrRfc6428CompatibleCodePoint.setStatus("current")
_FsMplsInSegmentTable_Object = MibTable
fsMplsInSegmentTable = _FsMplsInSegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 13, 1, 2)
)
if mibBuilder.loadTexts:
    fsMplsInSegmentTable.setStatus("current")
_FsMplsInSegmentEntry_Object = MibTableRow
fsMplsInSegmentEntry = _FsMplsInSegmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 13, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fsMplsInSegmentEntry.setStatus("current")


class _FsMplsInSegmentDirection_Type(Integer32):
    """Custom type fsMplsInSegmentDirection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("reverse", 2))
    )


_FsMplsInSegmentDirection_Type.__name__ = "Integer32"
_FsMplsInSegmentDirection_Object = MibTableColumn
fsMplsInSegmentDirection = _FsMplsInSegmentDirection_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 13, 1, 2, 1, 1),
    _FsMplsInSegmentDirection_Type()
)
fsMplsInSegmentDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsInSegmentDirection.setStatus("current")
_FsMplsOutSegmentTable_Object = MibTable
fsMplsOutSegmentTable = _FsMplsOutSegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 13, 1, 3)
)
if mibBuilder.loadTexts:
    fsMplsOutSegmentTable.setStatus("current")
_FsMplsOutSegmentEntry_Object = MibTableRow
fsMplsOutSegmentEntry = _FsMplsOutSegmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 13, 1, 3, 1)
)
if mibBuilder.loadTexts:
    fsMplsOutSegmentEntry.setStatus("current")


class _FsMplsOutSegmentDirection_Type(Integer32):
    """Custom type fsMplsOutSegmentDirection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("reverse", 2))
    )


_FsMplsOutSegmentDirection_Type.__name__ = "Integer32"
_FsMplsOutSegmentDirection_Object = MibTableColumn
fsMplsOutSegmentDirection = _FsMplsOutSegmentDirection_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 13, 1, 3, 1, 1),
    _FsMplsOutSegmentDirection_Type()
)
fsMplsOutSegmentDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsOutSegmentDirection.setStatus("current")
_FsMplsLsrConformance_ObjectIdentity = ObjectIdentity
fsMplsLsrConformance = _FsMplsLsrConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 13, 2)
)
mplsInSegmentEntry.registerAugmentions(
    ("SUPERMICRO-MPLS-LSR-MIB",
     "fsMplsInSegmentEntry")
)
fsMplsInSegmentEntry.setIndexNames(*mplsInSegmentEntry.getIndexNames())
mplsOutSegmentEntry.registerAugmentions(
    ("SUPERMICRO-MPLS-LSR-MIB",
     "fsMplsOutSegmentEntry")
)
fsMplsOutSegmentEntry.setIndexNames(*mplsOutSegmentEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-MPLS-LSR-MIB",
    **{"fsMplsLsrMIB": fsMplsLsrMIB,
       "fsMplsLsrNotifications": fsMplsLsrNotifications,
       "fsMplsLsrObjects": fsMplsLsrObjects,
       "fsMplsLsrScalarObjects": fsMplsLsrScalarObjects,
       "fsMplsLsrRfc6428CompatibleCodePoint": fsMplsLsrRfc6428CompatibleCodePoint,
       "fsMplsInSegmentTable": fsMplsInSegmentTable,
       "fsMplsInSegmentEntry": fsMplsInSegmentEntry,
       "fsMplsInSegmentDirection": fsMplsInSegmentDirection,
       "fsMplsOutSegmentTable": fsMplsOutSegmentTable,
       "fsMplsOutSegmentEntry": fsMplsOutSegmentEntry,
       "fsMplsOutSegmentDirection": fsMplsOutSegmentDirection,
       "fsMplsLsrConformance": fsMplsLsrConformance}
)
