# SNMP MIB module (QTECH-TUNNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-TUNNEL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:57:42 2025
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

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

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

qtechTunnelMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 114)
)
if mibBuilder.loadTexts:
    qtechTunnelMib.setRevisions(
        ("2012-06-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechTunnelObjects_ObjectIdentity = ObjectIdentity
qtechTunnelObjects = _QtechTunnelObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 114, 1)
)
_QtechTunnelTable_Object = MibTable
qtechTunnelTable = _QtechTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 114, 1, 1)
)
if mibBuilder.loadTexts:
    qtechTunnelTable.setStatus("current")
_QtechTunnelEntry_Object = MibTableRow
qtechTunnelEntry = _QtechTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 114, 1, 1, 1)
)
qtechTunnelEntry.setIndexNames(
    (0, "QTECH-TUNNEL-MIB", "qtechTunnelIp"),
)
if mibBuilder.loadTexts:
    qtechTunnelEntry.setStatus("current")
_QtechTunnelIp_Type = IpAddress
_QtechTunnelIp_Object = MibTableColumn
qtechTunnelIp = _QtechTunnelIp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 114, 1, 1, 1, 1),
    _QtechTunnelIp_Type()
)
qtechTunnelIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechTunnelIp.setStatus("current")
_QtechTunnelOutIfindex_Type = Integer32
_QtechTunnelOutIfindex_Object = MibTableColumn
qtechTunnelOutIfindex = _QtechTunnelOutIfindex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 114, 1, 1, 1, 2),
    _QtechTunnelOutIfindex_Type()
)
qtechTunnelOutIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechTunnelOutIfindex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-TUNNEL-MIB",
    **{"qtechTunnelMib": qtechTunnelMib,
       "qtechTunnelObjects": qtechTunnelObjects,
       "qtechTunnelTable": qtechTunnelTable,
       "qtechTunnelEntry": qtechTunnelEntry,
       "qtechTunnelIp": qtechTunnelIp,
       "qtechTunnelOutIfindex": qtechTunnelOutIfindex}
)
