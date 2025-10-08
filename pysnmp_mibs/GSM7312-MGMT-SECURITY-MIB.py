#
# PySNMP MIB module GSM7312-MGMT-SECURITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/netgear/GSM7312-MGMT-SECURITY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:51:25 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
gsm7312, = mibBuilder.importSymbols("GSM7312-REF-MIB", "gsm7312")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
gsm7312MgmtSecurity = ModuleIdentity((1, 3, 6, 1, 4, 1, 4526, 1, 6, 11))
gsm7312MgmtSecurity.setRevisions(('2003-11-21 00:00',))
if mibBuilder.loadTexts: gsm7312MgmtSecurity.setLastUpdated('200311210000Z')
if mibBuilder.loadTexts: gsm7312MgmtSecurity.setOrganization('Netgear')
agentSSLConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 1, 6, 11, 1))
agentSSLAdminMode = MibScalar((1, 3, 6, 1, 4, 1, 4526, 1, 6, 11, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSLAdminMode.setStatus('current')
agentSSLSecurePort = MibScalar((1, 3, 6, 1, 4, 1, 4526, 1, 6, 11, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSLSecurePort.setStatus('current')
agentSSLProtocolLevel = MibScalar((1, 3, 6, 1, 4, 1, 4526, 1, 6, 11, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ssl30", 1), ("tls10", 2), ("both", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSLProtocolLevel.setStatus('current')
agentSSHConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 1, 6, 11, 2))
agentSSHAdminMode = MibScalar((1, 3, 6, 1, 4, 1, 4526, 1, 6, 11, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSHAdminMode.setStatus('current')
agentSSHProtocolLevel = MibScalar((1, 3, 6, 1, 4, 1, 4526, 1, 6, 11, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ssh10", 1), ("ssh20", 2), ("both", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSHProtocolLevel.setStatus('current')
agentSSHSessionsCount = MibScalar((1, 3, 6, 1, 4, 1, 4526, 1, 6, 11, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSSHSessionsCount.setStatus('current')
mibBuilder.exportSymbols("GSM7312-MGMT-SECURITY-MIB", agentSSLProtocolLevel=agentSSLProtocolLevel, agentSSLAdminMode=agentSSLAdminMode, agentSSLConfigGroup=agentSSLConfigGroup, gsm7312MgmtSecurity=gsm7312MgmtSecurity, agentSSHAdminMode=agentSSHAdminMode, agentSSHSessionsCount=agentSSHSessionsCount, agentSSLSecurePort=agentSSLSecurePort, agentSSHConfigGroup=agentSSHConfigGroup, agentSSHProtocolLevel=agentSSHProtocolLevel, PYSNMP_MODULE_ID=gsm7312MgmtSecurity)
