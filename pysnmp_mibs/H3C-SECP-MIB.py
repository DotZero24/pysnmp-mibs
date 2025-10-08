#
# PySNMP MIB module H3C-SECP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/h3c/H3C-SECP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:22:04 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("H3C-SECP-MIB", h3cSecpRunningInfoTable=h3cSecpRunningInfoTable, h3cSecpMatchPacketCount=h3cSecpMatchPacketCount, h3cSecpRuleID=h3cSecpRuleID, PYSNMP_MODULE_ID=h3cSecp, h3cSecpIPVersion=h3cSecpIPVersion, h3cSecpLastMatchTime=h3cSecpLastMatchTime, h3cSecpObjects=h3cSecpObjects, h3cSecpRunningInfoEntry=h3cSecpRunningInfoEntry, h3cSecp=h3cSecp)
