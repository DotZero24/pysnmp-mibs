#
# PySNMP MIB module PORTGROUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/PORTGROUP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:34:27 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
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
mibBuilder.exportSymbols("PORTGROUP-MIB", swPortGroupMIBObjects=swPortGroupMIBObjects, swPortGroupTable=swPortGroupTable, swPortGroupMIB=swPortGroupMIB, swPortGroupID=swPortGroupID, swPortGroupRowStatus=swPortGroupRowStatus, swPortGroupName=swPortGroupName, swPortGroupEntry=swPortGroupEntry, swPortGroupPorts=swPortGroupPorts, PYSNMP_MODULE_ID=swPortGroupMIB)
