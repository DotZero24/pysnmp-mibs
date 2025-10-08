#
# PySNMP MIB module OUTBOUNDTELNET-PRIVATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/quanta/OUTBOUNDTELNET-PRIVATE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:08:21 2025
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
outboundTelnetPrivate = ModuleIdentity((1, 3, 6, 1, 4, 1, 7244, 2, 19))
if mibBuilder.loadTexts: outboundTelnetPrivate.setLastUpdated('201108310000Z')
if mibBuilder.loadTexts: outboundTelnetPrivate.setOrganization('QCI')
agentOutboundTelnetGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 7244, 2, 19, 1))
agentOutboundTelnetAdminMode = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 19, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentOutboundTelnetAdminMode.setStatus('current')
agentOutboundTelnetMaxNoOfSessions = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 19, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 5)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentOutboundTelnetMaxNoOfSessions.setStatus('current')
agentOutboundTelnetTimeout = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 19, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 160)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentOutboundTelnetTimeout.setStatus('current')
mibBuilder.exportSymbols("OUTBOUNDTELNET-PRIVATE-MIB", PYSNMP_MODULE_ID=outboundTelnetPrivate, agentOutboundTelnetMaxNoOfSessions=agentOutboundTelnetMaxNoOfSessions, agentOutboundTelnetTimeout=agentOutboundTelnetTimeout, agentOutboundTelnetAdminMode=agentOutboundTelnetAdminMode, agentOutboundTelnetGroup=agentOutboundTelnetGroup, outboundTelnetPrivate=outboundTelnetPrivate)
