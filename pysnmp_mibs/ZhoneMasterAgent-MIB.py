#
# PySNMP MIB module ZhoneMasterAgent-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zhone/ZhoneMasterAgent-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:19:36 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
zhoneModules, zhoneMasterAgent = mibBuilder.importSymbols("Zhone", "zhoneModules", "zhoneMasterAgent")
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
mibBuilder.exportSymbols("ZhoneMasterAgent-MIB", maRequestPort=maRequestPort, maTrapPort=maTrapPort, maPerfSaRequests=maPerfSaRequests, maPerfSaResponses=maPerfSaResponses, PYSNMP_MODULE_ID=zhoneMasterAgentMIB, maPerfSaTimeouts=maPerfSaTimeouts, zhoneMasterAgentMIB=zhoneMasterAgentMIB, maPerfSnmpErrors=maPerfSnmpErrors)
