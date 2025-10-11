# SNMP MIB module (SW3700PRIMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/SW3700PRIMGMT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:53:21 2025
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

_Dlink_Dgs3700SeriesProd_ObjectIdentity = ObjectIdentity
dlink_Dgs3700SeriesProd = _Dlink_Dgs3700SeriesProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 102)
)
_Dgs3712Prod_ObjectIdentity = ObjectIdentity
dgs3712Prod = _Dgs3712Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 102, 1)
)
_Dgs3712pProd_ObjectIdentity = ObjectIdentity
dgs3712pProd = _Dgs3712pProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 102, 2)
)
_Dlink_Dgs3700Series_ObjectIdentity = ObjectIdentity
dlink_Dgs3700Series = _Dlink_Dgs3700Series_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 102)
)
_Dgs3700_ObjectIdentity = ObjectIdentity
dgs3700 = _Dgs3700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1)
)
_Dgs3712_ObjectIdentity = ObjectIdentity
dgs3712 = _Dgs3712_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 1)
)
_Dgs3712g_ObjectIdentity = ObjectIdentity
dgs3712g = _Dgs3712g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 2)
)
_Dgs3710_ObjectIdentity = ObjectIdentity
dgs3710 = _Dgs3710_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 3)
)
_Dgs3710s_ObjectIdentity = ObjectIdentity
dgs3710s = _Dgs3710s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 4)
)
_Dgs3712c_ObjectIdentity = ObjectIdentity
dgs3712c = _Dgs3712c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SW3700PRIMGMT-MIB",
    **{"dlink-Dgs3700SeriesProd": dlink_Dgs3700SeriesProd,
       "dgs3712Prod": dgs3712Prod,
       "dgs3712pProd": dgs3712pProd,
       "dlink-Dgs3700Series": dlink_Dgs3700Series,
       "dgs3700": dgs3700,
       "dgs3712": dgs3712,
       "dgs3712g": dgs3712g,
       "dgs3710": dgs3710,
       "dgs3710s": dgs3710s,
       "dgs3712c": dgs3712c}
)
