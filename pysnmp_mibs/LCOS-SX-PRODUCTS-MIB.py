# SNMP MIB module (LCOS-SX-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/lancom/LCOS-SX-PRODUCTS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:20:06 2025
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

(lcosSX2,) = mibBuilder.importSymbols(
    "LANCOM-REF-MIB",
    "lcosSX2")

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

lcosSxProducts = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 16, 8)
)
if mibBuilder.loadTexts:
    lcosSxProducts.setRevisions(
        ("2021-11-19 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LcosSxProductsGS4530X_ObjectIdentity = ObjectIdentity
lcosSxProductsGS4530X = _LcosSxProductsGS4530X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 16, 8, 4530)
)
_LcosSxProductsGS4530XP_ObjectIdentity = ObjectIdentity
lcosSxProductsGS4530XP = _LcosSxProductsGS4530XP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 16, 8, 4531)
)
_LcosSxProductsGS4554X_ObjectIdentity = ObjectIdentity
lcosSxProductsGS4554X = _LcosSxProductsGS4554X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 16, 8, 4554)
)
_LcosSxProductsGS4554XP_ObjectIdentity = ObjectIdentity
lcosSxProductsGS4554XP = _LcosSxProductsGS4554XP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 16, 8, 4555)
)
_LcosSxProductsXS5110F_ObjectIdentity = ObjectIdentity
lcosSxProductsXS5110F = _LcosSxProductsXS5110F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 16, 8, 5110)
)
_LcosSxProductsXS5116QF_ObjectIdentity = ObjectIdentity
lcosSxProductsXS5116QF = _LcosSxProductsXS5116QF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 16, 8, 5116)
)
_LcosSxProductsXS6128QF_ObjectIdentity = ObjectIdentity
lcosSxProductsXS6128QF = _LcosSxProductsXS6128QF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 16, 8, 6128)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LCOS-SX-PRODUCTS-MIB",
    **{"lcosSxProducts": lcosSxProducts,
       "lcosSxProductsGS4530X": lcosSxProductsGS4530X,
       "lcosSxProductsGS4530XP": lcosSxProductsGS4530XP,
       "lcosSxProductsGS4554X": lcosSxProductsGS4554X,
       "lcosSxProductsGS4554XP": lcosSxProductsGS4554XP,
       "lcosSxProductsXS5110F": lcosSxProductsXS5110F,
       "lcosSxProductsXS5116QF": lcosSxProductsXS5116QF,
       "lcosSxProductsXS6128QF": lcosSxProductsXS6128QF}
)
