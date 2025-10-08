#
# PySNMP MIB module PORTGROUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/PORTGROUP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:59:14 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
swPortGroupMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 88))
if mibBuilder.loadTexts: swPortGroupMIB.setLastUpdated('1001110000Z')
if mibBuilder.loadTexts: swPortGroupMIB.setOrganization('D-Link Corp.')
swPortGroupMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 88, 1))
swPortGroupTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 88, 1, 1), )
if mibBuilder.loadTexts: swPortGroupTable.setStatus('current')
swPortGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 88, 1, 1, 1), ).setIndexNames((0, "PORTGROUP-MIB", "swPortGroupID"))
if mibBuilder.loadTexts: swPortGroupEntry.setStatus('current')
swPortGroupID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 88, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: swPortGroupID.setStatus('current')
swPortGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 88, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swPortGroupRowStatus.setStatus('current')
swPortGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 88, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swPortGroupName.setStatus('current')
swPortGroupPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 88, 1, 1, 1, 4), PortList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swPortGroupPorts.setStatus('current')
mibBuilder.exportSymbols("PORTGROUP-MIB", swPortGroupEntry=swPortGroupEntry, swPortGroupMIBObjects=swPortGroupMIBObjects, swPortGroupName=swPortGroupName, swPortGroupPorts=swPortGroupPorts, swPortGroupRowStatus=swPortGroupRowStatus, PYSNMP_MODULE_ID=swPortGroupMIB, swPortGroupMIB=swPortGroupMIB, swPortGroupTable=swPortGroupTable, swPortGroupID=swPortGroupID)
