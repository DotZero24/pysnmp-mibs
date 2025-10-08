#
# PySNMP MIB module LEFTHAND-NETWORKS-NUS-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/LEFTHAND-NETWORKS-NUS-COMMON-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:09:55 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
lhnModules, lhnNusCommonMIB = mibBuilder.importSymbols("LEFTHAND-NETWORKS-GLOBAL-REG", "lhnModules", "lhnNusCommonMIB")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("LEFTHAND-NETWORKS-NUS-COMMON-MIB", lhnNusCommonNTP=lhnNusCommonNTP, lhnNusCommonClustering=lhnNusCommonClustering, lhnNusCommonNetwork=lhnNusCommonNetwork, leftHandNetworksNusCommonModule=leftHandNetworksNusCommonModule, lhnNusCommonInfo=lhnNusCommonInfo, lhnNusCommonBasicGroup=lhnNusCommonBasicGroup, lhnNusCommonConfs=lhnNusCommonConfs, lhnNusCommonStatus=lhnNusCommonStatus, lhnNusCommonNIS=lhnNusCommonNIS, lhnNusCommonEvents=lhnNusCommonEvents, lhnNusCommonStorage=lhnNusCommonStorage, lhnNusCommonNotification=lhnNusCommonNotification, lhnNusCommonNTDomain=lhnNusCommonNTDomain, lhnNusCommonGroups=lhnNusCommonGroups, lhnNusCommonObjs=lhnNusCommonObjs, lhnNusCommonShares=lhnNusCommonShares, lhnNusCommonSecurity=lhnNusCommonSecurity, lhnNusCommonComplianceV1=lhnNusCommonComplianceV1, PYSNMP_MODULE_ID=leftHandNetworksNusCommonModule, lhnNusCommonAEBS=lhnNusCommonAEBS, lhnNusCommonCompl=lhnNusCommonCompl, lhnNusCommonDNS=lhnNusCommonDNS, lhnNusCommonSysOptions=lhnNusCommonSysOptions)
