# SNMP MIB module (IPI-HQOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ipinfusion/IPI-HQOS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:34:22 2025
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

(ipi,) = mibBuilder.importSymbols(
    "OCNOS-IPI-MODULE-MIB",
    "ipi")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ipiHqosMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 36673, 107)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpiHqosTable_ObjectIdentity = ObjectIdentity
ipiHqosTable = _IpiHqosTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36673, 107, 1)
)
_IpiHqosCmapTable_Object = MibTable
ipiHqosCmapTable = _IpiHqosCmapTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 107, 1, 1)
)
if mibBuilder.loadTexts:
    ipiHqosCmapTable.setStatus("current")
_IpiHqosCmapEntry_Object = MibTableRow
ipiHqosCmapEntry = _IpiHqosCmapEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 107, 1, 1, 1)
)
ipiHqosCmapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IPI-HQOS-MIB", "hqosDirection"),
    (0, "IPI-HQOS-MIB", "hqosCmapId"),
)
if mibBuilder.loadTexts:
    ipiHqosCmapEntry.setStatus("current")
_HqosDirection_Type = Unsigned32
_HqosDirection_Object = MibTableColumn
hqosDirection = _HqosDirection_Object(
    (1, 3, 6, 1, 4, 1, 36673, 107, 1, 1, 1, 1),
    _HqosDirection_Type()
)
hqosDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosDirection.setStatus("current")
_HqosCmapId_Type = Unsigned32
_HqosCmapId_Object = MibTableColumn
hqosCmapId = _HqosCmapId_Object(
    (1, 3, 6, 1, 4, 1, 36673, 107, 1, 1, 1, 2),
    _HqosCmapId_Type()
)
hqosCmapId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosCmapId.setStatus("current")
_HqosCmapMatchPkts_Type = Counter64
_HqosCmapMatchPkts_Object = MibTableColumn
hqosCmapMatchPkts = _HqosCmapMatchPkts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 107, 1, 1, 1, 3),
    _HqosCmapMatchPkts_Type()
)
hqosCmapMatchPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosCmapMatchPkts.setStatus("current")
_HqosCmapMatchBytes_Type = Counter64
_HqosCmapMatchBytes_Object = MibTableColumn
hqosCmapMatchBytes = _HqosCmapMatchBytes_Object(
    (1, 3, 6, 1, 4, 1, 36673, 107, 1, 1, 1, 4),
    _HqosCmapMatchBytes_Type()
)
hqosCmapMatchBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosCmapMatchBytes.setStatus("current")
_HqosCmapDropPkts_Type = Counter64
_HqosCmapDropPkts_Object = MibTableColumn
hqosCmapDropPkts = _HqosCmapDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 107, 1, 1, 1, 5),
    _HqosCmapDropPkts_Type()
)
hqosCmapDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosCmapDropPkts.setStatus("current")
_HqosCmapDropBytes_Type = Counter64
_HqosCmapDropBytes_Object = MibTableColumn
hqosCmapDropBytes = _HqosCmapDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 36673, 107, 1, 1, 1, 6),
    _HqosCmapDropBytes_Type()
)
hqosCmapDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosCmapDropBytes.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPI-HQOS-MIB",
    **{"ipiHqosMib": ipiHqosMib,
       "ipiHqosTable": ipiHqosTable,
       "ipiHqosCmapTable": ipiHqosCmapTable,
       "ipiHqosCmapEntry": ipiHqosCmapEntry,
       "hqosDirection": hqosDirection,
       "hqosCmapId": hqosCmapId,
       "hqosCmapMatchPkts": hqosCmapMatchPkts,
       "hqosCmapMatchBytes": hqosCmapMatchBytes,
       "hqosCmapDropPkts": hqosCmapDropPkts,
       "hqosCmapDropBytes": hqosCmapDropBytes}
)
