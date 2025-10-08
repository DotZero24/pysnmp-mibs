#
# PySNMP MIB module H3C-VRRP-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/h3c/H3C-VRRP-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:10:45 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
vrrpOperVrId, = mibBuilder.importSymbols("VRRP-MIB", "vrrpOperVrId")
h3cVrrpExt = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 24))
if mibBuilder.loadTexts: h3cVrrpExt.setLastUpdated('200412090000Z')
if mibBuilder.loadTexts: h3cVrrpExt.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
h3cVrrpExtMibObject = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 24, 1))
h3cVrrpExtTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 24, 1, 1), )
if mibBuilder.loadTexts: h3cVrrpExtTable.setStatus('current')
h3cVrrpExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 24, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "VRRP-MIB", "vrrpOperVrId"), (0, "H3C-VRRP-EXT-MIB", "h3cVrrpExtTrackInterface"))
if mibBuilder.loadTexts: h3cVrrpExtEntry.setStatus('current')
h3cVrrpExtTrackInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 24, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: h3cVrrpExtTrackInterface.setStatus('current')
h3cVrrpExtPriorityReduce = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 24, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(10)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVrrpExtPriorityReduce.setStatus('current')
h3cVrrpExtRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 24, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVrrpExtRowStatus.setStatus('current')
mibBuilder.exportSymbols("H3C-VRRP-EXT-MIB", h3cVrrpExtEntry=h3cVrrpExtEntry, h3cVrrpExtPriorityReduce=h3cVrrpExtPriorityReduce, h3cVrrpExtRowStatus=h3cVrrpExtRowStatus, PYSNMP_MODULE_ID=h3cVrrpExt, h3cVrrpExt=h3cVrrpExt, h3cVrrpExtMibObject=h3cVrrpExtMibObject, h3cVrrpExtTrackInterface=h3cVrrpExtTrackInterface, h3cVrrpExtTable=h3cVrrpExtTable)
