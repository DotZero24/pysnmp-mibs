# SNMP MIB module (ADTRAN-GENGPONCONTAINER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENGPONCONTAINER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:32:46 2025
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

(adComplianceShared,
 adIdentityShared,
 adShared) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adComplianceShared",
    "adIdentityShared",
    "adShared")

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

adGenGponModuleIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenGpon_ObjectIdentity = ObjectIdentity
adGenGpon = _AdGenGpon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 76)
)
_AdGenGponProduct_ObjectIdentity = ObjectIdentity
adGenGponProduct = _AdGenGponProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 76, 1)
)
_AdGenGponProductID_ObjectIdentity = ObjectIdentity
adGenGponProductID = _AdGenGponProductID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1)
)
_AdGenGponConformance_ObjectIdentity = ObjectIdentity
adGenGponConformance = _AdGenGponConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 99, 10000, 76)
)
_AdGenGponProductConformance_ObjectIdentity = ObjectIdentity
adGenGponProductConformance = _AdGenGponProductConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 99, 10000, 76, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENGPONCONTAINER-MIB",
    **{"adGenGpon": adGenGpon,
       "adGenGponProduct": adGenGponProduct,
       "adGenGponModuleIdentity": adGenGponModuleIdentity,
       "adGenGponProductID": adGenGponProductID,
       "adGenGponConformance": adGenGponConformance,
       "adGenGponProductConformance": adGenGponProductConformance}
)
