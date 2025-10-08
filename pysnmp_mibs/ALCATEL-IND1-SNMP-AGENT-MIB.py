#
# PySNMP MIB module ALCATEL-IND1-SNMP-AGENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/alcatel/ALCATEL-IND1-SNMP-AGENT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:06:47 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
softentIND1SnmpAgt, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1SnmpAgt")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
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
mibBuilder.exportSymbols("ALCATEL-IND1-SNMP-AGENT-MIB", PYSNMP_MODULE_ID=alcatelIND1SNMPAgentMIB, alcatelIND1SNMPAgentMIB=alcatelIND1SNMPAgentMIB, snmpAgtCommunityMode=snmpAgtCommunityMode, snmpAgtConfigGroup=snmpAgtConfigGroup, alcatelIND1SNMPAgentMIBConformance=alcatelIND1SNMPAgentMIBConformance, snmpAgtConfig=snmpAgtConfig, alcatelIND1SNMPAgentMIBCompliance=alcatelIND1SNMPAgentMIBCompliance, snmpAgtSecurityLevel=snmpAgtSecurityLevel, alcatelIND1SNMPAgentMIBGroups=alcatelIND1SNMPAgentMIBGroups, alcatelIND1SNMPAgentMIBObjects=alcatelIND1SNMPAgentMIBObjects, snmpAgtCtlFiles=snmpAgtCtlFiles, snmpAgtCtlFilesGroup=snmpAgtCtlFilesGroup, SnmpAgtSecurityLevel=SnmpAgtSecurityLevel, alcatelIND1SNMPAgentMIBCompliances=alcatelIND1SNMPAgentMIBCompliances, snmpAgtSourceIpConfig=snmpAgtSourceIpConfig, snmpAgtSourceIp=snmpAgtSourceIp)
