#
# PySNMP MIB module DOT1X-AUTHENTICATION-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/quanta/DOT1X-AUTHENTICATION-SERVER-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:08:25 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
switch, = mibBuilder.importSymbols("QUANTA-SWITCH-MIB", "switch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
dot1xAuthenticationServer = ModuleIdentity((1, 3, 6, 1, 4, 1, 7244, 2, 49))
if mibBuilder.loadTexts: dot1xAuthenticationServer.setLastUpdated('201108310000Z')
if mibBuilder.loadTexts: dot1xAuthenticationServer.setOrganization('QCI')
agentDot1xAuthServUserConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 7244, 2, 49, 1))
agentDot1xAuthServUserConfigCreate = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 49, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1xAuthServUserConfigCreate.setStatus('current')
agentDot1xAuthServUserConfigTable = MibTable((1, 3, 6, 1, 4, 1, 7244, 2, 49, 1, 2), )
if mibBuilder.loadTexts: agentDot1xAuthServUserConfigTable.setStatus('current')
agentDot1xAuthServUserConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7244, 2, 49, 1, 2, 1), ).setIndexNames((0, "DOT1X-AUTHENTICATION-SERVER-MIB", "agentDot1xAuthServUserIndex"))
if mibBuilder.loadTexts: agentDot1xAuthServUserConfigEntry.setStatus('current')
agentDot1xAuthServUserIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 49, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99)))
if mibBuilder.loadTexts: agentDot1xAuthServUserIndex.setStatus('current')
agentDot1xAuthServUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 49, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1xAuthServUserName.setStatus('current')
agentDot1xAuthServUserPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 49, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1xAuthServUserPassword.setStatus('current')
agentDot1xAuthServUserStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 49, 1, 2, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1xAuthServUserStatus.setStatus('current')
mibBuilder.exportSymbols("DOT1X-AUTHENTICATION-SERVER-MIB", dot1xAuthenticationServer=dot1xAuthenticationServer, agentDot1xAuthServUserConfigTable=agentDot1xAuthServUserConfigTable, agentDot1xAuthServUserStatus=agentDot1xAuthServUserStatus, agentDot1xAuthServUserName=agentDot1xAuthServUserName, agentDot1xAuthServUserIndex=agentDot1xAuthServUserIndex, agentDot1xAuthServUserConfigCreate=agentDot1xAuthServUserConfigCreate, agentDot1xAuthServUserPassword=agentDot1xAuthServUserPassword, PYSNMP_MODULE_ID=dot1xAuthenticationServer, agentDot1xAuthServUserConfigEntry=agentDot1xAuthServUserConfigEntry, agentDot1xAuthServUserConfigGroup=agentDot1xAuthServUserConfigGroup)
