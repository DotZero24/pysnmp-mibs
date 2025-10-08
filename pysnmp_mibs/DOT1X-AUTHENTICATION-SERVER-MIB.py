#
# PySNMP MIB module DOT1X-AUTHENTICATION-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/quanta/DOT1X-AUTHENTICATION-SERVER-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:41:22 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
switch, = mibBuilder.importSymbols("QUANTA-SWITCH-MIB", "switch")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
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
mibBuilder.exportSymbols("DOT1X-AUTHENTICATION-SERVER-MIB", agentDot1xAuthServUserConfigGroup=agentDot1xAuthServUserConfigGroup, PYSNMP_MODULE_ID=dot1xAuthenticationServer, dot1xAuthenticationServer=dot1xAuthenticationServer, agentDot1xAuthServUserConfigEntry=agentDot1xAuthServUserConfigEntry, agentDot1xAuthServUserStatus=agentDot1xAuthServUserStatus, agentDot1xAuthServUserName=agentDot1xAuthServUserName, agentDot1xAuthServUserIndex=agentDot1xAuthServUserIndex, agentDot1xAuthServUserConfigTable=agentDot1xAuthServUserConfigTable, agentDot1xAuthServUserPassword=agentDot1xAuthServUserPassword, agentDot1xAuthServUserConfigCreate=agentDot1xAuthServUserConfigCreate)
