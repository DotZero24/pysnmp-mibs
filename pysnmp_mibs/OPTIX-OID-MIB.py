# SNMP MIB module (OPTIX-OID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/huawei/OPTIX-OID-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:30:16 2025
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Huawei_ObjectIdentity = ObjectIdentity
huawei = _Huawei_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2)
)
_Transmission_ObjectIdentity = ObjectIdentity
transmission = _Transmission_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25)
)
_OptixCommon_ObjectIdentity = ObjectIdentity
optixCommon = _OptixCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3)
)
_OptixCommonSnmp_ObjectIdentity = ObjectIdentity
optixCommonSnmp = _OptixCommonSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 1)
)
_OptixCommonGlobal_ObjectIdentity = ObjectIdentity
optixCommonGlobal = _OptixCommonGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40)
)
_OptixProvision_ObjectIdentity = ObjectIdentity
optixProvision = _OptixProvision_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4)
)
_OptixProvisionWDM_ObjectIdentity = ObjectIdentity
optixProvisionWDM = _OptixProvisionWDM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 70)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPTIX-OID-MIB",
    **{"huawei": huawei,
       "products": products,
       "transmission": transmission,
       "optixCommon": optixCommon,
       "optixCommonSnmp": optixCommonSnmp,
       "optixCommonGlobal": optixCommonGlobal,
       "optixProvision": optixProvision,
       "optixProvisionWDM": optixProvisionWDM}
)
