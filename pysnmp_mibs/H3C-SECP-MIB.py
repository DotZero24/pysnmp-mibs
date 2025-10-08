#
# PySNMP MIB module H3C-SECP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/h3c/H3C-SECP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:10:21 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Integer32, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Counter64, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Counter64", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
h3cSecp = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 166))
h3cSecp.setRevisions(('2016-12-19 16:05',))
if mibBuilder.loadTexts: h3cSecp.setLastUpdated('201612191605Z')
if mibBuilder.loadTexts: h3cSecp.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
h3cSecpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 166, 1))
h3cSecpRunningInfoTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 166, 1, 1), )
if mibBuilder.loadTexts: h3cSecpRunningInfoTable.setStatus('current')
h3cSecpRunningInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 166, 1, 1, 1), ).setIndexNames((0, "H3C-SECP-MIB", "h3cSecpIPVersion"), (0, "H3C-SECP-MIB", "h3cSecpRuleID"))
if mibBuilder.loadTexts: h3cSecpRunningInfoEntry.setStatus('current')
h3cSecpIPVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 166, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ipv4", 1), ("ipv6", 2))))
if mibBuilder.loadTexts: h3cSecpIPVersion.setStatus('current')
h3cSecpRuleID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 166, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65534)))
if mibBuilder.loadTexts: h3cSecpRuleID.setStatus('current')
h3cSecpMatchPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 166, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSecpMatchPacketCount.setStatus('current')
h3cSecpLastMatchTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 166, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSecpLastMatchTime.setStatus('current')
mibBuilder.exportSymbols("H3C-SECP-MIB", PYSNMP_MODULE_ID=h3cSecp, h3cSecpObjects=h3cSecpObjects, h3cSecpLastMatchTime=h3cSecpLastMatchTime, h3cSecpMatchPacketCount=h3cSecpMatchPacketCount, h3cSecpRuleID=h3cSecpRuleID, h3cSecpRunningInfoTable=h3cSecpRunningInfoTable, h3cSecp=h3cSecp, h3cSecpIPVersion=h3cSecpIPVersion, h3cSecpRunningInfoEntry=h3cSecpRunningInfoEntry)
