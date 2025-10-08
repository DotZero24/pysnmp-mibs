#
# PySNMP MIB module OUTBAND-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/raisecom/OUTBAND-MGMT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:54:30 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
iscomEpon, = mibBuilder.importSymbols("RAISECOM-BASE-MIB", "iscomEpon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("OUTBAND-MGMT-MIB", rcOutbandIpSubnetRowStatus=rcOutbandIpSubnetRowStatus, rcOutbandIpSubnetEntry=rcOutbandIpSubnetEntry, PYSNMP_MODULE_ID=rcOutbandMgmt, rcOutbandIpSubnetIndex=rcOutbandIpSubnetIndex, rcOutbandIpSubnetIpAddress=rcOutbandIpSubnetIpAddress, rcOutbandMgmt=rcOutbandMgmt, rcOutbandIpSubnet=rcOutbandIpSubnet, rcOutbandIpSubnetTable=rcOutbandIpSubnetTable, rcOutbandIpSubnetMask=rcOutbandIpSubnetMask)
