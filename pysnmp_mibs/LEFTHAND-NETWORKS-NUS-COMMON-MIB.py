# SNMP MIB module (LEFTHAND-NETWORKS-NUS-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/LEFTHAND-NETWORKS-NUS-COMMON-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:42:38 2025
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

(lhnModules,
 lhnNusCommonMIB) = mibBuilder.importSymbols(
    "LEFTHAND-NETWORKS-GLOBAL-REG",
    "lhnModules",
    "lhnNusCommonMIB")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

leftHandNetworksNusCommonModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 1, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LhnNusCommonConfs_ObjectIdentity = ObjectIdentity
lhnNusCommonConfs = _LhnNusCommonConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 1)
)
_LhnNusCommonGroups_ObjectIdentity = ObjectIdentity
lhnNusCommonGroups = _LhnNusCommonGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 1, 1)
)
_LhnNusCommonCompl_ObjectIdentity = ObjectIdentity
lhnNusCommonCompl = _LhnNusCommonCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 1, 2)
)
_LhnNusCommonObjs_ObjectIdentity = ObjectIdentity
lhnNusCommonObjs = _LhnNusCommonObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2)
)
_LhnNusCommonInfo_ObjectIdentity = ObjectIdentity
lhnNusCommonInfo = _LhnNusCommonInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1)
)
_LhnNusCommonNetwork_ObjectIdentity = ObjectIdentity
lhnNusCommonNetwork = _LhnNusCommonNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2)
)
_LhnNusCommonDNS_ObjectIdentity = ObjectIdentity
lhnNusCommonDNS = _LhnNusCommonDNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 3)
)
_LhnNusCommonStorage_ObjectIdentity = ObjectIdentity
lhnNusCommonStorage = _LhnNusCommonStorage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4)
)
_LhnNusCommonNTP_ObjectIdentity = ObjectIdentity
lhnNusCommonNTP = _LhnNusCommonNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 5)
)
_LhnNusCommonNIS_ObjectIdentity = ObjectIdentity
lhnNusCommonNIS = _LhnNusCommonNIS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 6)
)
_LhnNusCommonAEBS_ObjectIdentity = ObjectIdentity
lhnNusCommonAEBS = _LhnNusCommonAEBS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 7)
)
_LhnNusCommonShares_ObjectIdentity = ObjectIdentity
lhnNusCommonShares = _LhnNusCommonShares_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 8)
)
_LhnNusCommonNTDomain_ObjectIdentity = ObjectIdentity
lhnNusCommonNTDomain = _LhnNusCommonNTDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 9)
)
_LhnNusCommonSysOptions_ObjectIdentity = ObjectIdentity
lhnNusCommonSysOptions = _LhnNusCommonSysOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 10)
)
_LhnNusCommonSecurity_ObjectIdentity = ObjectIdentity
lhnNusCommonSecurity = _LhnNusCommonSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11)
)
_LhnNusCommonClustering_ObjectIdentity = ObjectIdentity
lhnNusCommonClustering = _LhnNusCommonClustering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12)
)
_LhnNusCommonNotification_ObjectIdentity = ObjectIdentity
lhnNusCommonNotification = _LhnNusCommonNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 13)
)
_LhnNusCommonStatus_ObjectIdentity = ObjectIdentity
lhnNusCommonStatus = _LhnNusCommonStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 99)
)
_LhnNusCommonEvents_ObjectIdentity = ObjectIdentity
lhnNusCommonEvents = _LhnNusCommonEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 3)
)

# Managed Objects groups

lhnNusCommonBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 1, 1, 1)
)
lhnNusCommonBasicGroup.setObjects(
      *(("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonInfo"),
        ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonNetwork"),
        ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonDNS"),
        ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonStorage"),
        ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonNTP"),
        ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonNIS"),
        ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonAEBS"),
        ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonShares"),
        ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonNTDomain"),
        ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonSysOptions"),
        ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonSecurity"),
        ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonClustering"),
        ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonNotification"),
        ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonStatus"))
)
if mibBuilder.loadTexts:
    lhnNusCommonBasicGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lhnNusCommonComplianceV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 1, 2, 1)
)
lhnNusCommonComplianceV1.setObjects(
    ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonBasicGroup")
)
if mibBuilder.loadTexts:
    lhnNusCommonComplianceV1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LEFTHAND-NETWORKS-NUS-COMMON-MIB",
    **{"leftHandNetworksNusCommonModule": leftHandNetworksNusCommonModule,
       "lhnNusCommonConfs": lhnNusCommonConfs,
       "lhnNusCommonGroups": lhnNusCommonGroups,
       "lhnNusCommonBasicGroup": lhnNusCommonBasicGroup,
       "lhnNusCommonCompl": lhnNusCommonCompl,
       "lhnNusCommonComplianceV1": lhnNusCommonComplianceV1,
       "lhnNusCommonObjs": lhnNusCommonObjs,
       "lhnNusCommonInfo": lhnNusCommonInfo,
       "lhnNusCommonNetwork": lhnNusCommonNetwork,
       "lhnNusCommonDNS": lhnNusCommonDNS,
       "lhnNusCommonStorage": lhnNusCommonStorage,
       "lhnNusCommonNTP": lhnNusCommonNTP,
       "lhnNusCommonNIS": lhnNusCommonNIS,
       "lhnNusCommonAEBS": lhnNusCommonAEBS,
       "lhnNusCommonShares": lhnNusCommonShares,
       "lhnNusCommonNTDomain": lhnNusCommonNTDomain,
       "lhnNusCommonSysOptions": lhnNusCommonSysOptions,
       "lhnNusCommonSecurity": lhnNusCommonSecurity,
       "lhnNusCommonClustering": lhnNusCommonClustering,
       "lhnNusCommonNotification": lhnNusCommonNotification,
       "lhnNusCommonStatus": lhnNusCommonStatus,
       "lhnNusCommonEvents": lhnNusCommonEvents}
)
