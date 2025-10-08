#
# PySNMP MIB module MX-SNMP-AGENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/media5/MX-SNMP-AGENT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:39:25 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
mediatrixConfig, = mibBuilder.importSymbols("MX-SMI", "mediatrixConfig")
MxEnableState, = mibBuilder.importSymbols("MX-TC", "MxEnableState")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
snmpAgentMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4935, 15, 150))
snmpAgentMIB.setRevisions(('2005-04-28 00:00', '2004-02-13 00:00',))
if mibBuilder.loadTexts: snmpAgentMIB.setLastUpdated('200504280000Z')
if mibBuilder.loadTexts: snmpAgentMIB.setOrganization('Mediatrix Telecom, Inc.')
snmpAgentMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 15, 150, 1))
snmpAgentConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 15, 150, 2))
snmpAgentEnable = MibScalar((1, 3, 6, 1, 4, 1, 4935, 15, 150, 1, 1), MxEnableState().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpAgentEnable.setStatus('current')
snmpAgentAccess = MibScalar((1, 3, 6, 1, 4, 1, 4935, 15, 150, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("lanOnly", 0), ("wanOnly", 1), ("all", 2))).clone('all')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpAgentAccess.setStatus('current')
snmpAgentCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 15, 150, 2, 1))
snmpAgentAccessComplVer1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4935, 15, 150, 2, 1, 1)).setObjects(("MX-SNMP-AGENT-MIB", "snmpAgentAccessGroupVer1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpAgentAccessComplVer1 = snmpAgentAccessComplVer1.setStatus('current')
snmpAgentGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 15, 150, 2, 5))
snmpAgentAccessGroupVer1 = ObjectGroup((1, 3, 6, 1, 4, 1, 4935, 15, 150, 2, 5, 5)).setObjects(("MX-SNMP-AGENT-MIB", "snmpAgentEnable"), ("MX-SNMP-AGENT-MIB", "snmpAgentAccess"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpAgentAccessGroupVer1 = snmpAgentAccessGroupVer1.setStatus('current')
mibBuilder.exportSymbols("MX-SNMP-AGENT-MIB", PYSNMP_MODULE_ID=snmpAgentMIB, snmpAgentAccessComplVer1=snmpAgentAccessComplVer1, snmpAgentCompliances=snmpAgentCompliances, snmpAgentEnable=snmpAgentEnable, snmpAgentAccessGroupVer1=snmpAgentAccessGroupVer1, snmpAgentMIBObjects=snmpAgentMIBObjects, snmpAgentGroups=snmpAgentGroups, snmpAgentAccess=snmpAgentAccess, snmpAgentMIB=snmpAgentMIB, snmpAgentConformance=snmpAgentConformance)
