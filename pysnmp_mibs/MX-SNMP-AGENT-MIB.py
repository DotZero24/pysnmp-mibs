#
# PySNMP MIB module MX-SNMP-AGENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/media5/MX-SNMP-AGENT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:05:58 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
mediatrixConfig, = mibBuilder.importSymbols("MX-SMI", "mediatrixConfig")
MxEnableState, = mibBuilder.importSymbols("MX-TC", "MxEnableState")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("MX-SNMP-AGENT-MIB", PYSNMP_MODULE_ID=snmpAgentMIB, snmpAgentConformance=snmpAgentConformance, snmpAgentMIB=snmpAgentMIB, snmpAgentAccess=snmpAgentAccess, snmpAgentAccessGroupVer1=snmpAgentAccessGroupVer1, snmpAgentMIBObjects=snmpAgentMIBObjects, snmpAgentCompliances=snmpAgentCompliances, snmpAgentEnable=snmpAgentEnable, snmpAgentAccessComplVer1=snmpAgentAccessComplVer1, snmpAgentGroups=snmpAgentGroups)
