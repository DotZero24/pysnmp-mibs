#
# PySNMP MIB module HPN-ICF-VRRP-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HPN-ICF-VRRP-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:02:10 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
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
mibBuilder.exportSymbols("HPN-ICF-VRRP-EXT-MIB", hpnicfVrrpExtRowStatus=hpnicfVrrpExtRowStatus, hpnicfVrrpExtTrackInterface=hpnicfVrrpExtTrackInterface, hpnicfVrrpExtTable=hpnicfVrrpExtTable, PYSNMP_MODULE_ID=hpnicfVrrpExt, hpnicfVrrpExt=hpnicfVrrpExt, hpnicfVrrpExtPriorityReduce=hpnicfVrrpExtPriorityReduce, hpnicfVrrpExtEntry=hpnicfVrrpExtEntry, hpnicfVrrpExtMibObject=hpnicfVrrpExtMibObject)
