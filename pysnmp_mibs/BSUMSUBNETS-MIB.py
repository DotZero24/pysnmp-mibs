# SNMP MIB module (BSUMSUBNETS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aperto/BSUMSUBNETS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:06:13 2025
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

(bsu,) = mibBuilder.importSymbols(
    "ANIROOT-MIB",
    "bsu")

(aniBsuWirelessPort,) = mibBuilder.importSymbols(
    "BSUWIRELESSIF-MIB",
    "aniBsuWirelessPort")

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

aniBsuMultSubnets = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 3, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AniBsuSubnetConfTable_Object = MibTable
aniBsuSubnetConfTable = _AniBsuSubnetConfTable_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 6, 1)
)
if mibBuilder.loadTexts:
    aniBsuSubnetConfTable.setStatus("current")
_AniBsuSubnetConfEntry_Object = MibTableRow
aniBsuSubnetConfEntry = _AniBsuSubnetConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 6, 1, 1)
)
aniBsuSubnetConfEntry.setIndexNames(
    (0, "BSUWIRELESSIF-MIB", "aniBsuWirelessPort"),
    (0, "BSUMSUBNETS-MIB", "aniBsuSubnetConfAddr"),
)
if mibBuilder.loadTexts:
    aniBsuSubnetConfEntry.setStatus("current")
_AniBsuSubnetConfAddr_Type = IpAddress
_AniBsuSubnetConfAddr_Object = MibTableColumn
aniBsuSubnetConfAddr = _AniBsuSubnetConfAddr_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 6, 1, 1, 1),
    _AniBsuSubnetConfAddr_Type()
)
aniBsuSubnetConfAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aniBsuSubnetConfAddr.setStatus("current")
_AniBsuSubnetConfMask_Type = IpAddress
_AniBsuSubnetConfMask_Object = MibTableColumn
aniBsuSubnetConfMask = _AniBsuSubnetConfMask_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 6, 1, 1, 2),
    _AniBsuSubnetConfMask_Type()
)
aniBsuSubnetConfMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aniBsuSubnetConfMask.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BSUMSUBNETS-MIB",
    **{"aniBsuMultSubnets": aniBsuMultSubnets,
       "aniBsuSubnetConfTable": aniBsuSubnetConfTable,
       "aniBsuSubnetConfEntry": aniBsuSubnetConfEntry,
       "aniBsuSubnetConfAddr": aniBsuSubnetConfAddr,
       "aniBsuSubnetConfMask": aniBsuSubnetConfMask}
)
