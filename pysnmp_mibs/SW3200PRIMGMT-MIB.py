# SNMP MIB module (SW3200PRIMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/SW3200PRIMGMT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:53:15 2025
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

_Dlink_Dgs3200SeriesProd_ObjectIdentity = ObjectIdentity
dlink_Dgs3200SeriesProd = _Dlink_Dgs3200SeriesProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 101)
)
_Dgs3200_Prod_ObjectIdentity = ObjectIdentity
dgs3200_Prod = _Dgs3200_Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 101, 1)
)
_Dgs3216_Prod_ObjectIdentity = ObjectIdentity
dgs3216_Prod = _Dgs3216_Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 101, 2)
)
_Dgs3224_Prod_ObjectIdentity = ObjectIdentity
dgs3224_Prod = _Dgs3224_Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 101, 3)
)
_Dlink_Dgs3200Series_ObjectIdentity = ObjectIdentity
dlink_Dgs3200Series = _Dlink_Dgs3200Series_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 101)
)
_Dgs3200_ObjectIdentity = ObjectIdentity
dgs3200 = _Dgs3200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 1)
)
_Dgs3216_ObjectIdentity = ObjectIdentity
dgs3216 = _Dgs3216_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2)
)
_Dgs3224_ObjectIdentity = ObjectIdentity
dgs3224 = _Dgs3224_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SW3200PRIMGMT-MIB",
    **{"dlink-Dgs3200SeriesProd": dlink_Dgs3200SeriesProd,
       "dgs3200-Prod": dgs3200_Prod,
       "dgs3216-Prod": dgs3216_Prod,
       "dgs3224-Prod": dgs3224_Prod,
       "dlink-Dgs3200Series": dlink_Dgs3200Series,
       "dgs3200": dgs3200,
       "dgs3216": dgs3216,
       "dgs3224": dgs3224}
)
