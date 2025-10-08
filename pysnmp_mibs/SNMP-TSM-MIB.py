#
# PySNMP MIB module SNMP-TSM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/rfc/SNMP-TSM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:50:13 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Gauge32, MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "mib-2")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
snmpTsmMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 190))
snmpTsmMIB.setRevisions(('2009-06-09 00:00',))
if mibBuilder.loadTexts: snmpTsmMIB.setLastUpdated('200906090000Z')
if mibBuilder.loadTexts: snmpTsmMIB.setOrganization('ISMS Working Group')
snmpTsmNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 190, 0))
snmpTsmMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 190, 1))
snmpTsmConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 190, 2))
snmpTsmStats = MibIdentifier((1, 3, 6, 1, 2, 1, 190, 1, 1))
snmpTsmInvalidCaches = MibScalar((1, 3, 6, 1, 2, 1, 190, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpTsmInvalidCaches.setStatus('current')
snmpTsmInadequateSecurityLevels = MibScalar((1, 3, 6, 1, 2, 1, 190, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpTsmInadequateSecurityLevels.setStatus('current')
snmpTsmUnknownPrefixes = MibScalar((1, 3, 6, 1, 2, 1, 190, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpTsmUnknownPrefixes.setStatus('current')
snmpTsmInvalidPrefixes = MibScalar((1, 3, 6, 1, 2, 1, 190, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpTsmInvalidPrefixes.setStatus('current')
snmpTsmConfiguration = MibIdentifier((1, 3, 6, 1, 2, 1, 190, 1, 2))
snmpTsmConfigurationUsePrefix = MibScalar((1, 3, 6, 1, 2, 1, 190, 1, 2, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpTsmConfigurationUsePrefix.setStatus('current')
snmpTsmCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 190, 2, 1))
snmpTsmGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 190, 2, 2))
snmpTsmCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 190, 2, 1, 1)).setObjects(("SNMP-TSM-MIB", "snmpTsmGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpTsmCompliance = snmpTsmCompliance.setStatus('current')
snmpTsmGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 190, 2, 2, 2)).setObjects(("SNMP-TSM-MIB", "snmpTsmInvalidCaches"), ("SNMP-TSM-MIB", "snmpTsmInadequateSecurityLevels"), ("SNMP-TSM-MIB", "snmpTsmUnknownPrefixes"), ("SNMP-TSM-MIB", "snmpTsmInvalidPrefixes"), ("SNMP-TSM-MIB", "snmpTsmConfigurationUsePrefix"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpTsmGroup = snmpTsmGroup.setStatus('current')
mibBuilder.exportSymbols("SNMP-TSM-MIB", snmpTsmInvalidPrefixes=snmpTsmInvalidPrefixes, snmpTsmCompliances=snmpTsmCompliances, snmpTsmStats=snmpTsmStats, snmpTsmConfigurationUsePrefix=snmpTsmConfigurationUsePrefix, snmpTsmConformance=snmpTsmConformance, snmpTsmCompliance=snmpTsmCompliance, snmpTsmMIB=snmpTsmMIB, PYSNMP_MODULE_ID=snmpTsmMIB, snmpTsmInvalidCaches=snmpTsmInvalidCaches, snmpTsmUnknownPrefixes=snmpTsmUnknownPrefixes, snmpTsmGroups=snmpTsmGroups, snmpTsmGroup=snmpTsmGroup, snmpTsmMIBObjects=snmpTsmMIBObjects, snmpTsmInadequateSecurityLevels=snmpTsmInadequateSecurityLevels, snmpTsmConfiguration=snmpTsmConfiguration, snmpTsmNotifications=snmpTsmNotifications)
