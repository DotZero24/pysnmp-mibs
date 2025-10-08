#
# PySNMP MIB module OUTBOUNDSSH-PRIVATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/quanta/OUTBOUNDSSH-PRIVATE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:08:28 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
switch, = mibBuilder.importSymbols("QUANTA-SWITCH-MIB", "switch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
outboundSSHPrivate = ModuleIdentity((1, 3, 6, 1, 4, 1, 7244, 2, 21))
if mibBuilder.loadTexts: outboundSSHPrivate.setLastUpdated('201108310000Z')
if mibBuilder.loadTexts: outboundSSHPrivate.setOrganization('QCI')
agentOutboundSSHGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 7244, 2, 21, 1))
agentOutboundSSHAdminMode = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 21, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentOutboundSSHAdminMode.setStatus('current')
agentOutboundSSHMaxNoOfSessions = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 21, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 5)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentOutboundSSHMaxNoOfSessions.setStatus('current')
agentOutboundSSHTimeout = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 21, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 160)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentOutboundSSHTimeout.setStatus('current')
mibBuilder.exportSymbols("OUTBOUNDSSH-PRIVATE-MIB", PYSNMP_MODULE_ID=outboundSSHPrivate, agentOutboundSSHTimeout=agentOutboundSSHTimeout, agentOutboundSSHGroup=agentOutboundSSHGroup, agentOutboundSSHAdminMode=agentOutboundSSHAdminMode, outboundSSHPrivate=outboundSSHPrivate, agentOutboundSSHMaxNoOfSessions=agentOutboundSSHMaxNoOfSessions)
