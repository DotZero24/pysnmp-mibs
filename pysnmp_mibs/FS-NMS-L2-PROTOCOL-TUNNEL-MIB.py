# SNMP MIB module (FS-NMS-L2-PROTOCOL-TUNNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-NMS-L2-PROTOCOL-TUNNEL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:15:32 2025
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

(nmsMgmt,) = mibBuilder.importSymbols(
    "FS-NMS-SMI",
    "nmsMgmt")

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

nmsL2ProtocolTunnelMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 9, 357)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_L2ptMIBObjects_ObjectIdentity = ObjectIdentity
l2ptMIBObjects = _L2ptMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 9, 357, 1)
)
_L2ptGlobal_ObjectIdentity = ObjectIdentity
l2ptGlobal = _L2ptGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 9, 357, 1, 1)
)
_L2ptIntfTable_Object = MibTable
l2ptIntfTable = _L2ptIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 9, 357, 1, 2)
)
if mibBuilder.loadTexts:
    l2ptIntfTable.setStatus("current")
_L2ptIntfEntry_Object = MibTableRow
l2ptIntfEntry = _L2ptIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 9, 357, 1, 2, 1)
)
l2ptIntfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    l2ptIntfEntry.setStatus("current")


class _L2ptIntfStpTnl_Type(Integer32):
    """Custom type l2ptIntfStpTnl based on Integer32"""
    defaultValue = 2

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


_L2ptIntfStpTnl_Type.__name__ = "Integer32"
_L2ptIntfStpTnl_Object = MibTableColumn
l2ptIntfStpTnl = _L2ptIntfStpTnl_Object(
    (1, 3, 6, 1, 4, 1, 52642, 9, 357, 1, 2, 1, 1),
    _L2ptIntfStpTnl_Type()
)
l2ptIntfStpTnl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2ptIntfStpTnl.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-NMS-L2-PROTOCOL-TUNNEL-MIB",
    **{"nmsL2ProtocolTunnelMIB": nmsL2ProtocolTunnelMIB,
       "l2ptMIBObjects": l2ptMIBObjects,
       "l2ptGlobal": l2ptGlobal,
       "l2ptIntfTable": l2ptIntfTable,
       "l2ptIntfEntry": l2ptIntfEntry,
       "l2ptIntfStpTnl": l2ptIntfStpTnl}
)
