# SNMP MIB module (SW3810PRIMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/SW3810PRIMGMT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:53:20 2025
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

_Dlink_Des3810Series_ObjectIdentity = ObjectIdentity
dlink_Des3810Series = _Dlink_Des3810Series_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 114)
)
_Des3810_ObjectIdentity = ObjectIdentity
des3810 = _Des3810_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1)
)
_Des3810_28_ObjectIdentity = ObjectIdentity
des3810_28 = _Des3810_28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 1)
)
_Des3810_28DC_ObjectIdentity = ObjectIdentity
des3810_28DC = _Des3810_28DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 2)
)
_Des3810_52_ObjectIdentity = ObjectIdentity
des3810_52 = _Des3810_52_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SW3810PRIMGMT-MIB",
    **{"dlink-Des3810Series": dlink_Des3810Series,
       "des3810": des3810,
       "des3810-28": des3810_28,
       "des3810-28DC": des3810_28DC,
       "des3810-52": des3810_52}
)
