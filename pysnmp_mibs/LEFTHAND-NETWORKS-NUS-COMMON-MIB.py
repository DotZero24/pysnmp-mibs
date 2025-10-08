#
# PySNMP MIB module LEFTHAND-NETWORKS-NUS-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/LEFTHAND-NETWORKS-NUS-COMMON-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:28 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
lhnNusCommonMIB, lhnModules = mibBuilder.importSymbols("LEFTHAND-NETWORKS-GLOBAL-REG", "lhnNusCommonMIB", "lhnModules")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
leftHandNetworksNusCommonModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 9804, 1, 1, 2))
if mibBuilder.loadTexts: leftHandNetworksNusCommonModule.setLastUpdated('200106010000Z')
if mibBuilder.loadTexts: leftHandNetworksNusCommonModule.setOrganization('LeftHand Networks, Inc.')
lhnNusCommonConfs = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 1))
lhnNusCommonGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 1, 1))
lhnNusCommonCompl = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 1, 2))
lhnNusCommonObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2))
lhnNusCommonInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1))
lhnNusCommonNetwork = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2))
lhnNusCommonDNS = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 3))
lhnNusCommonStorage = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4))
lhnNusCommonNTP = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 5))
lhnNusCommonNIS = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 6))
lhnNusCommonAEBS = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 7))
lhnNusCommonShares = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 8))
lhnNusCommonNTDomain = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 9))
lhnNusCommonSysOptions = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 10))
lhnNusCommonSecurity = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11))
lhnNusCommonClustering = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12))
lhnNusCommonNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 13))
lhnNusCommonStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 99))
lhnNusCommonEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 3))
lhnNusCommonBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 1, 1, 1)).setObjects(("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonInfo"), ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonNetwork"), ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonDNS"), ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonStorage"), ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonNTP"), ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonNIS"), ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonAEBS"), ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonShares"), ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonNTDomain"), ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonSysOptions"), ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonSecurity"), ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonClustering"), ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonNotification"), ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lhnNusCommonBasicGroup = lhnNusCommonBasicGroup.setStatus('current')
lhnNusCommonComplianceV1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 1, 2, 1)).setObjects(("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonBasicGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lhnNusCommonComplianceV1 = lhnNusCommonComplianceV1.setStatus('current')
mibBuilder.exportSymbols("LEFTHAND-NETWORKS-NUS-COMMON-MIB", lhnNusCommonStatus=lhnNusCommonStatus, lhnNusCommonNTP=lhnNusCommonNTP, lhnNusCommonShares=lhnNusCommonShares, lhnNusCommonSysOptions=lhnNusCommonSysOptions, lhnNusCommonAEBS=lhnNusCommonAEBS, lhnNusCommonNTDomain=lhnNusCommonNTDomain, lhnNusCommonDNS=lhnNusCommonDNS, lhnNusCommonStorage=lhnNusCommonStorage, lhnNusCommonEvents=lhnNusCommonEvents, PYSNMP_MODULE_ID=leftHandNetworksNusCommonModule, lhnNusCommonNIS=lhnNusCommonNIS, lhnNusCommonCompl=lhnNusCommonCompl, lhnNusCommonNotification=lhnNusCommonNotification, lhnNusCommonComplianceV1=lhnNusCommonComplianceV1, leftHandNetworksNusCommonModule=leftHandNetworksNusCommonModule, lhnNusCommonClustering=lhnNusCommonClustering, lhnNusCommonGroups=lhnNusCommonGroups, lhnNusCommonSecurity=lhnNusCommonSecurity, lhnNusCommonObjs=lhnNusCommonObjs, lhnNusCommonConfs=lhnNusCommonConfs, lhnNusCommonInfo=lhnNusCommonInfo, lhnNusCommonNetwork=lhnNusCommonNetwork, lhnNusCommonBasicGroup=lhnNusCommonBasicGroup)
