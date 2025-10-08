#
# PySNMP MIB module A3COM-HUAWEI-VRRP-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/a3com/A3COM-HUAWEI-VRRP-EXT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:33:25 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
vrrpOperVrId, = mibBuilder.importSymbols("VRRP-MIB", "vrrpOperVrId")
h3cVrrpExt = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 24))
if mibBuilder.loadTexts: h3cVrrpExt.setLastUpdated('200412090000Z')
if mibBuilder.loadTexts: h3cVrrpExt.setOrganization('Huawei-3Com Technologies Co.,Ltd.')
h3cVrrpExtMibObject = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 24, 1))
h3cVrrpExtTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 24, 1, 1), )
if mibBuilder.loadTexts: h3cVrrpExtTable.setStatus('current')
h3cVrrpExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 24, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "VRRP-MIB", "vrrpOperVrId"), (0, "A3COM-HUAWEI-VRRP-EXT-MIB", "h3cVrrpExtTrackInterface"))
if mibBuilder.loadTexts: h3cVrrpExtEntry.setStatus('current')
h3cVrrpExtTrackInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 24, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: h3cVrrpExtTrackInterface.setStatus('current')
h3cVrrpExtPriorityReduce = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 24, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(10)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVrrpExtPriorityReduce.setStatus('current')
h3cVrrpExtRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 24, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVrrpExtRowStatus.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-VRRP-EXT-MIB", h3cVrrpExtEntry=h3cVrrpExtEntry, h3cVrrpExtTable=h3cVrrpExtTable, h3cVrrpExtTrackInterface=h3cVrrpExtTrackInterface, PYSNMP_MODULE_ID=h3cVrrpExt, h3cVrrpExtMibObject=h3cVrrpExtMibObject, h3cVrrpExtRowStatus=h3cVrrpExtRowStatus, h3cVrrpExtPriorityReduce=h3cVrrpExtPriorityReduce, h3cVrrpExt=h3cVrrpExt)
