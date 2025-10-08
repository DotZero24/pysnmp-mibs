#
# PySNMP MIB module ALCATEL-IND1-SNMP-AGENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/alcatel/ALCATEL-IND1-SNMP-AGENT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:40:02 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
softentIND1SnmpAgt, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1SnmpAgt")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
alcatelIND1SNMPAgentMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1))
alcatelIND1SNMPAgentMIB.setRevisions(('2007-04-03 00:00',))
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIB.setLastUpdated('200704030000Z')
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIB.setOrganization('Alcatel-Lucent')
alcatelIND1SNMPAgentMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 1))
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIBObjects.setStatus('current')
alcatelIND1SNMPAgentMIBConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 2))
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIBConformance.setStatus('current')
alcatelIND1SNMPAgentMIBGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 2, 1))
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIBGroups.setStatus('current')
alcatelIND1SNMPAgentMIBCompliances = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 2, 2))
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIBCompliances.setStatus('current')
snmpAgtConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 1, 1))
class SnmpAgtSecurityLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("noSec", 1), ("authSet", 2), ("authAll", 3), ("privSet", 4), ("privAll", 5), ("trapOnly", 6))

snmpAgtSecurityLevel = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 1, 1, 1), SnmpAgtSecurityLevel().clone('noSec')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpAgtSecurityLevel.setStatus('current')
snmpAgtCommunityMode = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpAgtCommunityMode.setStatus('current')
snmpAgtCtlFiles = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 1, 3))
if mibBuilder.loadTexts: snmpAgtCtlFiles.setStatus('current')
snmpAgtSourceIpConfig = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("default", 1), ("noLoopback0", 2), ("ipInterface", 3))).clone('default')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpAgtSourceIpConfig.setStatus('current')
snmpAgtSourceIp = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpAgtSourceIp.setStatus('current')
alcatelIND1SNMPAgentMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-SNMP-AGENT-MIB", "snmpAgtConfigGroup"), ("ALCATEL-IND1-SNMP-AGENT-MIB", "snmpAgtCtlFilesGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alcatelIND1SNMPAgentMIBCompliance = alcatelIND1SNMPAgentMIBCompliance.setStatus('current')
snmpAgtConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-SNMP-AGENT-MIB", "snmpAgtSecurityLevel"), ("ALCATEL-IND1-SNMP-AGENT-MIB", "snmpAgtCommunityMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpAgtConfigGroup = snmpAgtConfigGroup.setStatus('current')
snmpAgtCtlFilesGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 2, 1, 2)).setObjects(("ALCATEL-IND1-SNMP-AGENT-MIB", "snmpAgtSourceIpConfig"), ("ALCATEL-IND1-SNMP-AGENT-MIB", "snmpAgtSourceIp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpAgtCtlFilesGroup = snmpAgtCtlFilesGroup.setStatus('current')
mibBuilder.exportSymbols("ALCATEL-IND1-SNMP-AGENT-MIB", snmpAgtSourceIpConfig=snmpAgtSourceIpConfig, snmpAgtCtlFiles=snmpAgtCtlFiles, snmpAgtCtlFilesGroup=snmpAgtCtlFilesGroup, snmpAgtSecurityLevel=snmpAgtSecurityLevel, alcatelIND1SNMPAgentMIBCompliance=alcatelIND1SNMPAgentMIBCompliance, alcatelIND1SNMPAgentMIBObjects=alcatelIND1SNMPAgentMIBObjects, snmpAgtCommunityMode=snmpAgtCommunityMode, alcatelIND1SNMPAgentMIBConformance=alcatelIND1SNMPAgentMIBConformance, PYSNMP_MODULE_ID=alcatelIND1SNMPAgentMIB, alcatelIND1SNMPAgentMIBCompliances=alcatelIND1SNMPAgentMIBCompliances, SnmpAgtSecurityLevel=SnmpAgtSecurityLevel, alcatelIND1SNMPAgentMIB=alcatelIND1SNMPAgentMIB, snmpAgtSourceIp=snmpAgtSourceIp, snmpAgtConfigGroup=snmpAgtConfigGroup, alcatelIND1SNMPAgentMIBGroups=alcatelIND1SNMPAgentMIBGroups, snmpAgtConfig=snmpAgtConfig)
