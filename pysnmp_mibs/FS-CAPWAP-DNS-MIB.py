# SNMP MIB module (FS-CAPWAP-DNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-CAPWAP-DNS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:14:35 2025
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

(fsIfIndex,) = mibBuilder.importSymbols(
    "FS-INTERFACE-MIB",
    "fsIfIndex")

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsCapwapDnsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 88)
)
if mibBuilder.loadTexts:
    fsCapwapDnsMIB.setRevisions(
        ("2010-07-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsCapwapDnsMIBObjects_ObjectIdentity = ObjectIdentity
fsCapwapDnsMIBObjects = _FsCapwapDnsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 88, 0)
)
_FsCapwapDnsGlobalConfig_ObjectIdentity = ObjectIdentity
fsCapwapDnsGlobalConfig = _FsCapwapDnsGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 88, 0, 1)
)
_FsLDnsFirstServer_Type = IpAddress
_FsLDnsFirstServer_Object = MibScalar
fsLDnsFirstServer = _FsLDnsFirstServer_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 88, 0, 1, 1),
    _FsLDnsFirstServer_Type()
)
fsLDnsFirstServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLDnsFirstServer.setStatus("current")
_FsLDnsSecondServer_Type = IpAddress
_FsLDnsSecondServer_Object = MibScalar
fsLDnsSecondServer = _FsLDnsSecondServer_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 88, 0, 1, 2),
    _FsLDnsSecondServer_Type()
)
fsLDnsSecondServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLDnsSecondServer.setStatus("current")
_FsCapwapDnsMIBConformance_ObjectIdentity = ObjectIdentity
fsCapwapDnsMIBConformance = _FsCapwapDnsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 88, 2)
)
_FsCapwapDnsMIBCompliances_ObjectIdentity = ObjectIdentity
fsCapwapDnsMIBCompliances = _FsCapwapDnsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 88, 2, 1)
)
_FsCapwapDnsMIBGroups_ObjectIdentity = ObjectIdentity
fsCapwapDnsMIBGroups = _FsCapwapDnsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 88, 2, 2)
)

# Managed Objects groups

fsCapwapDnsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 88, 2, 2, 1)
)
fsCapwapDnsMIBGroup.setObjects(
      *(("FS-CAPWAP-DNS-MIB", "fsLDnsFirstServer"),
        ("FS-CAPWAP-DNS-MIB", "fsLDnsSecondServer"))
)
if mibBuilder.loadTexts:
    fsCapwapDnsMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsCapwapDnsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 88, 2, 1, 1)
)
fsCapwapDnsMIBCompliance.setObjects(
    ("FS-CAPWAP-DNS-MIB", "fsCapwapDnsMIBGroup")
)
if mibBuilder.loadTexts:
    fsCapwapDnsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-CAPWAP-DNS-MIB",
    **{"fsCapwapDnsMIB": fsCapwapDnsMIB,
       "fsCapwapDnsMIBObjects": fsCapwapDnsMIBObjects,
       "fsCapwapDnsGlobalConfig": fsCapwapDnsGlobalConfig,
       "fsLDnsFirstServer": fsLDnsFirstServer,
       "fsLDnsSecondServer": fsLDnsSecondServer,
       "fsCapwapDnsMIBConformance": fsCapwapDnsMIBConformance,
       "fsCapwapDnsMIBCompliances": fsCapwapDnsMIBCompliances,
       "fsCapwapDnsMIBCompliance": fsCapwapDnsMIBCompliance,
       "fsCapwapDnsMIBGroups": fsCapwapDnsMIBGroups,
       "fsCapwapDnsMIBGroup": fsCapwapDnsMIBGroup}
)
