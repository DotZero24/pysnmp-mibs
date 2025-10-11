# SNMP MIB module (MITEL-IPNETDATABASE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mitel/MITEL-IPNETDATABASE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:04:38 2025
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

mitelRouterDatabaseVersion = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 8)
)
if mibBuilder.loadTexts:
    mitelRouterDatabaseVersion.setRevisions(
        ("2003-03-24 09:26",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mitel_ObjectIdentity = ObjectIdentity
mitel = _Mitel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027)
)
_MitelProprietary_ObjectIdentity = ObjectIdentity
mitelProprietary = _MitelProprietary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4)
)
_MitelPropIpNetworking_ObjectIdentity = ObjectIdentity
mitelPropIpNetworking = _MitelPropIpNetworking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8)
)
_MitelIpNetRouter_ObjectIdentity = ObjectIdentity
mitelIpNetRouter = _MitelIpNetRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1)
)
_MitelRouterDatabaseMajorVersion_Type = Integer32
_MitelRouterDatabaseMajorVersion_Object = MibScalar
mitelRouterDatabaseMajorVersion = _MitelRouterDatabaseMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 8, 1),
    _MitelRouterDatabaseMajorVersion_Type()
)
mitelRouterDatabaseMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelRouterDatabaseMajorVersion.setStatus("current")
_MitelRouterDatabaseMinorVersion_Type = Integer32
_MitelRouterDatabaseMinorVersion_Object = MibScalar
mitelRouterDatabaseMinorVersion = _MitelRouterDatabaseMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 8, 2),
    _MitelRouterDatabaseMinorVersion_Type()
)
mitelRouterDatabaseMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelRouterDatabaseMinorVersion.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MITEL-IPNETDATABASE-MIB",
    **{"mitel": mitel,
       "mitelProprietary": mitelProprietary,
       "mitelPropIpNetworking": mitelPropIpNetworking,
       "mitelIpNetRouter": mitelIpNetRouter,
       "mitelRouterDatabaseVersion": mitelRouterDatabaseVersion,
       "mitelRouterDatabaseMajorVersion": mitelRouterDatabaseMajorVersion,
       "mitelRouterDatabaseMinorVersion": mitelRouterDatabaseMinorVersion}
)
