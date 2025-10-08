#
# PySNMP MIB module ZHONE-COM-IP-RD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zhone/ZHONE-COM-IP-RD-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:12 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
zhoneIp, zhoneModules = mibBuilder.importSymbols("Zhone", "zhoneIp", "zhoneModules")
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
mibBuilder.exportSymbols("ZHONE-COM-IP-RD-MIB", PYSNMP_MODULE_ID=comIpRd, rdRowStatus=rdRowStatus, rdTable=rdTable, ZhoneRDIndex=ZhoneRDIndex, rdIndex=rdIndex, rdEntry=rdEntry, comIpRd=comIpRd, rd=rd)
