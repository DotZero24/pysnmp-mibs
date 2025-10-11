# SNMP MIB module (Aricent-MSPW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/Aricent-MSPW-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:43:12 2025
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

(PwIndexType,
 PwOperStatusTC) = mibBuilder.importSymbols(
    "PW-TC-STD-MIB",
    "PwIndexType",
    "PwOperStatusTC")

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

fsMspwMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 57)
)
if mibBuilder.loadTexts:
    fsMspwMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsMsPwConfigObjects_ObjectIdentity = ObjectIdentity
fsMsPwConfigObjects = _FsMsPwConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 57, 1)
)


class _FsMsPwMaxEntries_Type(Unsigned32):
    """Custom type fsMsPwMaxEntries based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32766),
    )


_FsMsPwMaxEntries_Type.__name__ = "Unsigned32"
_FsMsPwMaxEntries_Object = MibScalar
fsMsPwMaxEntries = _FsMsPwMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 57, 1, 1),
    _FsMsPwMaxEntries_Type()
)
fsMsPwMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMsPwMaxEntries.setStatus("current")
_FsMsPwConfigTable_Object = MibTable
fsMsPwConfigTable = _FsMsPwConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 57, 1, 2)
)
if mibBuilder.loadTexts:
    fsMsPwConfigTable.setStatus("current")
_FsMsPwConfigEntry_Object = MibTableRow
fsMsPwConfigEntry = _FsMsPwConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 57, 1, 2, 1)
)
fsMsPwConfigEntry.setIndexNames(
    (0, "Aricent-MSPW-MIB", "fsMsPwIndex1"),
    (0, "Aricent-MSPW-MIB", "fsMsPwIndex2"),
)
if mibBuilder.loadTexts:
    fsMsPwConfigEntry.setStatus("current")
_FsMsPwIndex1_Type = PwIndexType
_FsMsPwIndex1_Object = MibTableColumn
fsMsPwIndex1 = _FsMsPwIndex1_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 57, 1, 2, 1, 1),
    _FsMsPwIndex1_Type()
)
fsMsPwIndex1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMsPwIndex1.setStatus("current")
_FsMsPwIndex2_Type = PwIndexType
_FsMsPwIndex2_Object = MibTableColumn
fsMsPwIndex2 = _FsMsPwIndex2_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 57, 1, 2, 1, 2),
    _FsMsPwIndex2_Type()
)
fsMsPwIndex2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMsPwIndex2.setStatus("current")
_FsMsPwOperStatus_Type = PwOperStatusTC
_FsMsPwOperStatus_Object = MibTableColumn
fsMsPwOperStatus = _FsMsPwOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 57, 1, 2, 1, 3),
    _FsMsPwOperStatus_Type()
)
fsMsPwOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMsPwOperStatus.setStatus("current")
_FsMsPwRowStatus_Type = RowStatus
_FsMsPwRowStatus_Object = MibTableColumn
fsMsPwRowStatus = _FsMsPwRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 57, 1, 2, 1, 4),
    _FsMsPwRowStatus_Type()
)
fsMsPwRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMsPwRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Aricent-MSPW-MIB",
    **{"fsMspwMIB": fsMspwMIB,
       "fsMsPwConfigObjects": fsMsPwConfigObjects,
       "fsMsPwMaxEntries": fsMsPwMaxEntries,
       "fsMsPwConfigTable": fsMsPwConfigTable,
       "fsMsPwConfigEntry": fsMsPwConfigEntry,
       "fsMsPwIndex1": fsMsPwIndex1,
       "fsMsPwIndex2": fsMsPwIndex2,
       "fsMsPwOperStatus": fsMsPwOperStatus,
       "fsMsPwRowStatus": fsMsPwRowStatus}
)
