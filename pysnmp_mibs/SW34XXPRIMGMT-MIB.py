# SNMP MIB module (SW34XXPRIMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/SW34XXPRIMGMT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:53:13 2025
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

_Dlink_ProjectXStackIISeriesProd_ObjectIdentity = ObjectIdentity
dlink_ProjectXStackIISeriesProd = _Dlink_ProjectXStackIISeriesProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 70)
)
_Dlink_Dgs3426_ObjectIdentity = ObjectIdentity
dlink_Dgs3426 = _Dlink_Dgs3426_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 70, 1)
)
_Dlink_Dgs3427_ObjectIdentity = ObjectIdentity
dlink_Dgs3427 = _Dlink_Dgs3427_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 70, 2)
)
_Dlink_Dgs3450_ObjectIdentity = ObjectIdentity
dlink_Dgs3450 = _Dlink_Dgs3450_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 70, 3)
)
_Dlink_Dgs3426p_ObjectIdentity = ObjectIdentity
dlink_Dgs3426p = _Dlink_Dgs3426p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 70, 7)
)
_DgsProjectXStackIISeriesProd_ObjectIdentity = ObjectIdentity
dgsProjectXStackIISeriesProd = _DgsProjectXStackIISeriesProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70)
)
_Dgs3426_ObjectIdentity = ObjectIdentity
dgs3426 = _Dgs3426_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 1)
)
_Dgs3427_ObjectIdentity = ObjectIdentity
dgs3427 = _Dgs3427_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2)
)
_Dgs3450_ObjectIdentity = ObjectIdentity
dgs3450 = _Dgs3450_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 3)
)
_Dgs3426p_ObjectIdentity = ObjectIdentity
dgs3426p = _Dgs3426p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 7)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SW34XXPRIMGMT-MIB",
    **{"dlink-ProjectXStackIISeriesProd": dlink_ProjectXStackIISeriesProd,
       "dlink-Dgs3426": dlink_Dgs3426,
       "dlink-Dgs3427": dlink_Dgs3427,
       "dlink-Dgs3450": dlink_Dgs3450,
       "dlink-Dgs3426p": dlink_Dgs3426p,
       "dgsProjectXStackIISeriesProd": dgsProjectXStackIISeriesProd,
       "dgs3426": dgs3426,
       "dgs3427": dgs3427,
       "dgs3450": dgs3450,
       "dgs3426p": dgs3426p}
)
