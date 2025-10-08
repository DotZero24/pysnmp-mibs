#
# PySNMP MIB module INFINERA-TP-GAMOCGPTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-TP-GAMOCGPTP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:21:43 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
terminationPoint, = mibBuilder.importSymbols("INFINERA-REG-MIB", "terminationPoint")
InfnDcmType, = mibBuilder.importSymbols("INFINERA-TC-MIB", "InfnDcmType")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
gamOcgPtpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 8))
gamOcgPtpMIB.setRevisions(('2008-10-20 00:00',))
if mibBuilder.loadTexts: gamOcgPtpMIB.setLastUpdated('200810200000Z')
if mibBuilder.loadTexts: gamOcgPtpMIB.setOrganization('Infinera')
gamOcgPtpTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 8, 1), )
if mibBuilder.loadTexts: gamOcgPtpTable.setStatus('current')
gamOcgPtpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 8, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: gamOcgPtpEntry.setStatus('current')
gamOcgPtpDiscoveredOcgTP = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 8, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gamOcgPtpDiscoveredOcgTP.setStatus('current')
gamOcgPtpProvisionedOcgTP = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 8, 1, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gamOcgPtpProvisionedOcgTP.setStatus('current')
gamOcgPtpDiscoveredRemoteTP = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 8, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gamOcgPtpDiscoveredRemoteTP.setStatus('current')
gamOcgPtpPmHistStatsEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 8, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gamOcgPtpPmHistStatsEnable.setStatus('current')
gamOcgPtpInlineDcmType = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 8, 1, 1, 5), InfnDcmType().clone('unspecified')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gamOcgPtpInlineDcmType.setStatus('obsolete')
gamOcgPtpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 8, 3))
gamOcgPtpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 8, 3, 1))
gamOcgPtpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 8, 3, 2))
gamOcgPtpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 8, 3, 1, 1)).setObjects(("INFINERA-TP-GAMOCGPTP-MIB", "gamOcgPtpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gamOcgPtpCompliance = gamOcgPtpCompliance.setStatus('current')
gamOcgPtpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 8, 3, 2, 1)).setObjects(("INFINERA-TP-GAMOCGPTP-MIB", "gamOcgPtpDiscoveredOcgTP"), ("INFINERA-TP-GAMOCGPTP-MIB", "gamOcgPtpProvisionedOcgTP"), ("INFINERA-TP-GAMOCGPTP-MIB", "gamOcgPtpDiscoveredRemoteTP"), ("INFINERA-TP-GAMOCGPTP-MIB", "gamOcgPtpPmHistStatsEnable"), ("INFINERA-TP-GAMOCGPTP-MIB", "gamOcgPtpInlineDcmType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gamOcgPtpGroup = gamOcgPtpGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-TP-GAMOCGPTP-MIB", gamOcgPtpMIB=gamOcgPtpMIB, gamOcgPtpEntry=gamOcgPtpEntry, gamOcgPtpInlineDcmType=gamOcgPtpInlineDcmType, gamOcgPtpPmHistStatsEnable=gamOcgPtpPmHistStatsEnable, gamOcgPtpTable=gamOcgPtpTable, gamOcgPtpCompliance=gamOcgPtpCompliance, PYSNMP_MODULE_ID=gamOcgPtpMIB, gamOcgPtpDiscoveredOcgTP=gamOcgPtpDiscoveredOcgTP, gamOcgPtpProvisionedOcgTP=gamOcgPtpProvisionedOcgTP, gamOcgPtpGroup=gamOcgPtpGroup, gamOcgPtpConformance=gamOcgPtpConformance, gamOcgPtpDiscoveredRemoteTP=gamOcgPtpDiscoveredRemoteTP, gamOcgPtpCompliances=gamOcgPtpCompliances, gamOcgPtpGroups=gamOcgPtpGroups)
