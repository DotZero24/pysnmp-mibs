# SNMP MIB module (RDN-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/riverdelta/RDN-PRODUCTS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:03:40 2025
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

(rdnDefinitions,) = mibBuilder.importSymbols(
    "RDN-DEFINITIONS-MIB",
    "rdnDefinitions")

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

rdnProducts = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 1)
)
if mibBuilder.loadTexts:
    rdnProducts.setRevisions(
        ("2008-08-08 00:00",
         "2003-11-05 00:00",
         "2003-04-29 00:00",
         "2001-04-17 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RdnProductsUnknown_ObjectIdentity = ObjectIdentity
rdnProductsUnknown = _RdnProductsUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 1, 0)
)
_RdnProductsBSR64000_ObjectIdentity = ObjectIdentity
rdnProductsBSR64000 = _RdnProductsBSR64000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 1, 1)
)
_RdnProductsBSR1000B_ObjectIdentity = ObjectIdentity
rdnProductsBSR1000B = _RdnProductsBSR1000B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 1, 2)
)
_RdnProductsBSR1000R_ObjectIdentity = ObjectIdentity
rdnProductsBSR1000R = _RdnProductsBSR1000R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 1, 3)
)
_RdnProductsOSR2000_ObjectIdentity = ObjectIdentity
rdnProductsOSR2000 = _RdnProductsOSR2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 1, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RDN-PRODUCTS-MIB",
    **{"rdnProducts": rdnProducts,
       "rdnProductsUnknown": rdnProductsUnknown,
       "rdnProductsBSR64000": rdnProductsBSR64000,
       "rdnProductsBSR1000B": rdnProductsBSR1000B,
       "rdnProductsBSR1000R": rdnProductsBSR1000R,
       "rdnProductsOSR2000": rdnProductsOSR2000}
)
