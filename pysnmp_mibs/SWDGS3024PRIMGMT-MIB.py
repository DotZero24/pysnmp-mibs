# SNMP MIB module (SWDGS3024PRIMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/SWDGS3024PRIMGMT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:49:34 2025
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

(dlink_mgmt,
 dlink_products) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-mgmt",
    "dlink-products")

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

_Dgs_3024SeriesProd_ObjectIdentity = ObjectIdentity
dgs_3024SeriesProd = _Dgs_3024SeriesProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 68)
)
_Dgs_3024_ObjectIdentity = ObjectIdentity
dgs_3024 = _Dgs_3024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 68, 1)
)
_Dgs_3024SeriesProd_Mgmt_ObjectIdentity = ObjectIdentity
dgs_3024SeriesProd_Mgmt = _Dgs_3024SeriesProd_Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 68)
)
_Dgs_3024Mgmt_ObjectIdentity = ObjectIdentity
dgs_3024Mgmt = _Dgs_3024Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 68, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWDGS3024PRIMGMT-MIB",
    **{"dgs-3024SeriesProd": dgs_3024SeriesProd,
       "dgs-3024": dgs_3024,
       "dgs-3024SeriesProd-Mgmt": dgs_3024SeriesProd_Mgmt,
       "dgs-3024Mgmt": dgs_3024Mgmt}
)
