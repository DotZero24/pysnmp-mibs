#
# PySNMP MIB module OUTBAND-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/raisecom/OUTBAND-MGMT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:30:44 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
iscomEpon, = mibBuilder.importSymbols("RAISECOM-BASE-MIB", "iscomEpon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
rcOutbandMgmt = ModuleIdentity((1, 3, 6, 1, 4, 1, 8886, 6, 24, 3))
rcOutbandMgmt.setRevisions(('2007-02-09 00:00',))
if mibBuilder.loadTexts: rcOutbandMgmt.setLastUpdated('200702090000Z')
if mibBuilder.loadTexts: rcOutbandMgmt.setOrganization('Raisecom Science & Technology Co., ltd')
rcOutbandIpSubnet = MibIdentifier((1, 3, 6, 1, 4, 1, 8886, 6, 24, 3, 1))
rcOutbandIpSubnetTable = MibTable((1, 3, 6, 1, 4, 1, 8886, 6, 24, 3, 1, 1), )
if mibBuilder.loadTexts: rcOutbandIpSubnetTable.setStatus('current')
rcOutbandIpSubnetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8886, 6, 24, 3, 1, 1, 1), ).setIndexNames((0, "OUTBAND-MGMT-MIB", "rcOutbandIpSubnetIndex"))
if mibBuilder.loadTexts: rcOutbandIpSubnetEntry.setStatus('current')
rcOutbandIpSubnetIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 24, 3, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: rcOutbandIpSubnetIndex.setStatus('current')
rcOutbandIpSubnetIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 24, 3, 1, 1, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rcOutbandIpSubnetIpAddress.setStatus('current')
rcOutbandIpSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 24, 3, 1, 1, 1, 3), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rcOutbandIpSubnetMask.setStatus('current')
rcOutbandIpSubnetRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 24, 3, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rcOutbandIpSubnetRowStatus.setStatus('current')
mibBuilder.exportSymbols("OUTBAND-MGMT-MIB", rcOutbandIpSubnetIndex=rcOutbandIpSubnetIndex, PYSNMP_MODULE_ID=rcOutbandMgmt, rcOutbandMgmt=rcOutbandMgmt, rcOutbandIpSubnet=rcOutbandIpSubnet, rcOutbandIpSubnetMask=rcOutbandIpSubnetMask, rcOutbandIpSubnetTable=rcOutbandIpSubnetTable, rcOutbandIpSubnetEntry=rcOutbandIpSubnetEntry, rcOutbandIpSubnetIpAddress=rcOutbandIpSubnetIpAddress, rcOutbandIpSubnetRowStatus=rcOutbandIpSubnetRowStatus)
