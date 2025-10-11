# SNMP MIB module (ZIPLOCK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/cabletron/ZIPLOCK-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:56:25 2025
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

(ctResource,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctResource")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtZiplock_ObjectIdentity = ObjectIdentity
ctZiplock = _CtZiplock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 3)
)
_CtZiplockTable_Object = MibTable
ctZiplockTable = _CtZiplockTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 3, 1)
)
if mibBuilder.loadTexts:
    ctZiplockTable.setStatus("mandatory")
_CtZiplockEntry_Object = MibTableRow
ctZiplockEntry = _CtZiplockEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 3, 1, 1)
)
ctZiplockEntry.setIndexNames(
    (0, "ZIPLOCK-MIB", "ctZiplockNumber"),
)
if mibBuilder.loadTexts:
    ctZiplockEntry.setStatus("mandatory")
_CtZiplockNumber_Type = Integer32
_CtZiplockNumber_Object = MibTableColumn
ctZiplockNumber = _CtZiplockNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 3, 1, 1, 1),
    _CtZiplockNumber_Type()
)
ctZiplockNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctZiplockNumber.setStatus("mandatory")
_CtZiplockPresence_Type = Integer32
_CtZiplockPresence_Object = MibTableColumn
ctZiplockPresence = _CtZiplockPresence_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 3, 1, 1, 2),
    _CtZiplockPresence_Type()
)
ctZiplockPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctZiplockPresence.setStatus("mandatory")
_CtZiplockRevision_Type = Integer32
_CtZiplockRevision_Object = MibTableColumn
ctZiplockRevision = _CtZiplockRevision_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 3, 1, 1, 3),
    _CtZiplockRevision_Type()
)
ctZiplockRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctZiplockRevision.setStatus("mandatory")
_CtZiplockStatus_Type = Integer32
_CtZiplockStatus_Object = MibTableColumn
ctZiplockStatus = _CtZiplockStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 3, 1, 1, 4),
    _CtZiplockStatus_Type()
)
ctZiplockStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctZiplockStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZIPLOCK-MIB",
    **{"ctZiplock": ctZiplock,
       "ctZiplockTable": ctZiplockTable,
       "ctZiplockEntry": ctZiplockEntry,
       "ctZiplockNumber": ctZiplockNumber,
       "ctZiplockPresence": ctZiplockPresence,
       "ctZiplockRevision": ctZiplockRevision,
       "ctZiplockStatus": ctZiplockStatus}
)
