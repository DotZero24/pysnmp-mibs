# SNMP MIB module (SWDES3528-52PRIMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/SWDES3528-52PRIMGMT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:53:10 2025
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

_Dlink_Des3500SeriesProd_ObjectIdentity = ObjectIdentity
dlink_Des3500SeriesProd = _Dlink_Des3500SeriesProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 105)
)
_Des3528Prod_ObjectIdentity = ObjectIdentity
des3528Prod = _Des3528Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 105, 1)
)
_Des3528pProd_ObjectIdentity = ObjectIdentity
des3528pProd = _Des3528pProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 105, 2)
)
_Des3552Prod_ObjectIdentity = ObjectIdentity
des3552Prod = _Des3552Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 105, 3)
)
_Des3552pProd_ObjectIdentity = ObjectIdentity
des3552pProd = _Des3552pProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 105, 4)
)
_Des3528dcProd_ObjectIdentity = ObjectIdentity
des3528dcProd = _Des3528dcProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 105, 5)
)
_Dlink_Des3500Series_ObjectIdentity = ObjectIdentity
dlink_Des3500Series = _Dlink_Des3500Series_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 105)
)
_Des3528_ObjectIdentity = ObjectIdentity
des3528 = _Des3528_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 105, 1)
)
_Des3528p_ObjectIdentity = ObjectIdentity
des3528p = _Des3528p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 105, 2)
)
_Des3552_ObjectIdentity = ObjectIdentity
des3552 = _Des3552_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 105, 3)
)
_Des3552p_ObjectIdentity = ObjectIdentity
des3552p = _Des3552p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 105, 4)
)
_Des3528dc_ObjectIdentity = ObjectIdentity
des3528dc = _Des3528dc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 105, 5)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWDES3528-52PRIMGMT-MIB",
    **{"dlink-Des3500SeriesProd": dlink_Des3500SeriesProd,
       "des3528Prod": des3528Prod,
       "des3528pProd": des3528pProd,
       "des3552Prod": des3552Prod,
       "des3552pProd": des3552pProd,
       "des3528dcProd": des3528dcProd,
       "dlink-Des3500Series": dlink_Des3500Series,
       "des3528": des3528,
       "des3528p": des3528p,
       "des3552": des3552,
       "des3552p": des3552p,
       "des3528dc": des3528dc}
)
