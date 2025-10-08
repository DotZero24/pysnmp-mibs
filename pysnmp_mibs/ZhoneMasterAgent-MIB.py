#
# PySNMP MIB module ZhoneMasterAgent-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zhone/ZhoneMasterAgent-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:05 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
zhoneMasterAgent, zhoneModules = mibBuilder.importSymbols("Zhone", "zhoneMasterAgent", "zhoneModules")
zhoneMasterAgentMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5504, 6, 10))
zhoneMasterAgentMIB.setRevisions(('2000-09-12 11:16',))
if mibBuilder.loadTexts: zhoneMasterAgentMIB.setLastUpdated('200009121459Z')
if mibBuilder.loadTexts: zhoneMasterAgentMIB.setOrganization('Zhone Technogogies, Inc.')
maRequestPort = MibScalar((1, 3, 6, 1, 4, 1, 5504, 3, 7, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: maRequestPort.setStatus('current')
maTrapPort = MibScalar((1, 3, 6, 1, 4, 1, 5504, 3, 7, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: maTrapPort.setStatus('current')
maPerfSaRequests = MibScalar((1, 3, 6, 1, 4, 1, 5504, 3, 7, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maPerfSaRequests.setStatus('current')
maPerfSaResponses = MibScalar((1, 3, 6, 1, 4, 1, 5504, 3, 7, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maPerfSaResponses.setStatus('current')
maPerfSnmpErrors = MibScalar((1, 3, 6, 1, 4, 1, 5504, 3, 7, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maPerfSnmpErrors.setStatus('current')
maPerfSaTimeouts = MibScalar((1, 3, 6, 1, 4, 1, 5504, 3, 7, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maPerfSaTimeouts.setStatus('current')
mibBuilder.exportSymbols("ZhoneMasterAgent-MIB", zhoneMasterAgentMIB=zhoneMasterAgentMIB, maRequestPort=maRequestPort, maPerfSaResponses=maPerfSaResponses, maPerfSnmpErrors=maPerfSnmpErrors, maPerfSaTimeouts=maPerfSaTimeouts, PYSNMP_MODULE_ID=zhoneMasterAgentMIB, maPerfSaRequests=maPerfSaRequests, maTrapPort=maTrapPort)
