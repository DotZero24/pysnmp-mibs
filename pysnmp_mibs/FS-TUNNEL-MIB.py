# SNMP MIB module (FS-TUNNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-TUNNEL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:14:43 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

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

fsTunnelMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 114)
)
if mibBuilder.loadTexts:
    fsTunnelMib.setRevisions(
        ("2012-06-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsTunnelObjects_ObjectIdentity = ObjectIdentity
fsTunnelObjects = _FsTunnelObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 114, 1)
)
_FsTunnelTable_Object = MibTable
fsTunnelTable = _FsTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 114, 1, 1)
)
if mibBuilder.loadTexts:
    fsTunnelTable.setStatus("current")
_FsTunnelEntry_Object = MibTableRow
fsTunnelEntry = _FsTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 114, 1, 1, 1)
)
fsTunnelEntry.setIndexNames(
    (0, "FS-TUNNEL-MIB", "fsTunnelIp"),
)
if mibBuilder.loadTexts:
    fsTunnelEntry.setStatus("current")
_FsTunnelIp_Type = IpAddress
_FsTunnelIp_Object = MibTableColumn
fsTunnelIp = _FsTunnelIp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 114, 1, 1, 1, 1),
    _FsTunnelIp_Type()
)
fsTunnelIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTunnelIp.setStatus("current")
_FsTunnelOutIfindex_Type = Integer32
_FsTunnelOutIfindex_Object = MibTableColumn
fsTunnelOutIfindex = _FsTunnelOutIfindex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 114, 1, 1, 1, 2),
    _FsTunnelOutIfindex_Type()
)
fsTunnelOutIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTunnelOutIfindex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-TUNNEL-MIB",
    **{"fsTunnelMib": fsTunnelMib,
       "fsTunnelObjects": fsTunnelObjects,
       "fsTunnelTable": fsTunnelTable,
       "fsTunnelEntry": fsTunnelEntry,
       "fsTunnelIp": fsTunnelIp,
       "fsTunnelOutIfindex": fsTunnelOutIfindex}
)
