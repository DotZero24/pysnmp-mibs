#
# PySNMP MIB module ZHONE-COM-IP-RD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zhone/ZHONE-COM-IP-RD-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:19:53 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
zhoneModules, zhoneIp = mibBuilder.importSymbols("Zhone", "zhoneModules", "zhoneIp")
ZhoneRowStatus, = mibBuilder.importSymbols("Zhone-TC", "ZhoneRowStatus")
comIpRd = ModuleIdentity((1, 3, 6, 1, 4, 1, 5504, 6, 53))
comIpRd.setRevisions(('2000-09-12 10:02',))
if mibBuilder.loadTexts: comIpRd.setLastUpdated('200009111700Z')
if mibBuilder.loadTexts: comIpRd.setOrganization('Zhone Technologies, Inc.')
class ZhoneRDIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

rd = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 4, 1, 3))
if mibBuilder.loadTexts: rd.setStatus('current')
rdTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 4, 1, 3, 1), )
if mibBuilder.loadTexts: rdTable.setStatus('current')
rdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 4, 1, 3, 1, 1), ).setIndexNames((0, "ZHONE-COM-IP-RD-MIB", "rdIndex"))
if mibBuilder.loadTexts: rdEntry.setStatus('current')
rdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 3, 1, 1, 1), ZhoneRDIndex())
if mibBuilder.loadTexts: rdIndex.setStatus('current')
rdRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 3, 1, 1, 2), ZhoneRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rdRowStatus.setStatus('current')
mibBuilder.exportSymbols("ZHONE-COM-IP-RD-MIB", rdIndex=rdIndex, rdTable=rdTable, PYSNMP_MODULE_ID=comIpRd, rdRowStatus=rdRowStatus, rd=rd, comIpRd=comIpRd, rdEntry=rdEntry, ZhoneRDIndex=ZhoneRDIndex)
