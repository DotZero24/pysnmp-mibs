#
# PySNMP MIB module SNMP-TSM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/SNMP-TSM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:27:43 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, TimeTicks, MibIdentifier, Integer32, Bits, mib_2, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "TimeTicks", "MibIdentifier", "Integer32", "Bits", "mib-2", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("SNMP-TSM-MIB", snmpTsmMIB=snmpTsmMIB, snmpTsmConfigurationUsePrefix=snmpTsmConfigurationUsePrefix, snmpTsmMIBObjects=snmpTsmMIBObjects, snmpTsmConformance=snmpTsmConformance, PYSNMP_MODULE_ID=snmpTsmMIB, snmpTsmStats=snmpTsmStats, snmpTsmGroup=snmpTsmGroup, snmpTsmInadequateSecurityLevels=snmpTsmInadequateSecurityLevels, snmpTsmConfiguration=snmpTsmConfiguration, snmpTsmGroups=snmpTsmGroups, snmpTsmUnknownPrefixes=snmpTsmUnknownPrefixes, snmpTsmInvalidPrefixes=snmpTsmInvalidPrefixes, snmpTsmNotifications=snmpTsmNotifications, snmpTsmCompliances=snmpTsmCompliances, snmpTsmCompliance=snmpTsmCompliance, snmpTsmInvalidCaches=snmpTsmInvalidCaches)
