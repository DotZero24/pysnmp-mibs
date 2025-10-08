#
# PySNMP MIB module GSM7224-MGMT-SECURITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/netgear/GSM7224-MGMT-SECURITY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:28:51 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
gsm7224, = mibBuilder.importSymbols("GSM7224-REF-MIB", "gsm7224")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
gsm7224MgmtSecurity = ModuleIdentity((1, 3, 6, 1, 4, 1, 4526, 1, 8, 11))
gsm7224MgmtSecurity.setRevisions(('2003-11-21 00:00',))
if mibBuilder.loadTexts: gsm7224MgmtSecurity.setLastUpdated('200311210000Z')
if mibBuilder.loadTexts: gsm7224MgmtSecurity.setOrganization('Netgear')
agentSSLConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 1, 8, 11, 1))
agentSSLAdminMode = MibScalar((1, 3, 6, 1, 4, 1, 4526, 1, 8, 11, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSLAdminMode.setStatus('current')
agentSSLSecurePort = MibScalar((1, 3, 6, 1, 4, 1, 4526, 1, 8, 11, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSLSecurePort.setStatus('current')
agentSSLProtocolLevel = MibScalar((1, 3, 6, 1, 4, 1, 4526, 1, 8, 11, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ssl30", 1), ("tls10", 2), ("both", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSLProtocolLevel.setStatus('current')
agentSSHConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 1, 8, 11, 2))
agentSSHAdminMode = MibScalar((1, 3, 6, 1, 4, 1, 4526, 1, 8, 11, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSHAdminMode.setStatus('current')
agentSSHProtocolLevel = MibScalar((1, 3, 6, 1, 4, 1, 4526, 1, 8, 11, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ssh10", 1), ("ssh20", 2), ("both", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSHProtocolLevel.setStatus('current')
agentSSHSessionsCount = MibScalar((1, 3, 6, 1, 4, 1, 4526, 1, 8, 11, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSSHSessionsCount.setStatus('current')
mibBuilder.exportSymbols("GSM7224-MGMT-SECURITY-MIB", agentSSHAdminMode=agentSSHAdminMode, agentSSLAdminMode=agentSSLAdminMode, agentSSLConfigGroup=agentSSLConfigGroup, agentSSHProtocolLevel=agentSSHProtocolLevel, agentSSLSecurePort=agentSSLSecurePort, gsm7224MgmtSecurity=gsm7224MgmtSecurity, agentSSHConfigGroup=agentSSHConfigGroup, agentSSHSessionsCount=agentSSHSessionsCount, PYSNMP_MODULE_ID=gsm7224MgmtSecurity, agentSSLProtocolLevel=agentSSLProtocolLevel)
