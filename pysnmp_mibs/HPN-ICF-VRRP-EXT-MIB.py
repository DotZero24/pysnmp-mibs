#
# PySNMP MIB module HPN-ICF-VRRP-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HPN-ICF-VRRP-EXT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:07:48 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
vrrpOperVrId, = mibBuilder.importSymbols("VRRP-MIB", "vrrpOperVrId")
hpnicfVrrpExt = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 24))
if mibBuilder.loadTexts: hpnicfVrrpExt.setLastUpdated('200412090000Z')
if mibBuilder.loadTexts: hpnicfVrrpExt.setOrganization('')
hpnicfVrrpExtMibObject = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 24, 1))
hpnicfVrrpExtTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 24, 1, 1), )
if mibBuilder.loadTexts: hpnicfVrrpExtTable.setStatus('current')
hpnicfVrrpExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 24, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "VRRP-MIB", "vrrpOperVrId"), (0, "HPN-ICF-VRRP-EXT-MIB", "hpnicfVrrpExtTrackInterface"))
if mibBuilder.loadTexts: hpnicfVrrpExtEntry.setStatus('current')
hpnicfVrrpExtTrackInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 24, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: hpnicfVrrpExtTrackInterface.setStatus('current')
hpnicfVrrpExtPriorityReduce = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 24, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(10)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVrrpExtPriorityReduce.setStatus('current')
hpnicfVrrpExtRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 24, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVrrpExtRowStatus.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-VRRP-EXT-MIB", hpnicfVrrpExtEntry=hpnicfVrrpExtEntry, PYSNMP_MODULE_ID=hpnicfVrrpExt, hpnicfVrrpExtTable=hpnicfVrrpExtTable, hpnicfVrrpExtRowStatus=hpnicfVrrpExtRowStatus, hpnicfVrrpExt=hpnicfVrrpExt, hpnicfVrrpExtTrackInterface=hpnicfVrrpExtTrackInterface, hpnicfVrrpExtPriorityReduce=hpnicfVrrpExtPriorityReduce, hpnicfVrrpExtMibObject=hpnicfVrrpExtMibObject)
