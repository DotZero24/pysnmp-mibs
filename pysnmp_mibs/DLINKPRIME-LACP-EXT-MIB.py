#
# PySNMP MIB module DLINKPRIME-LACP-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/DLINKPRIME-LACP-EXT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:58:11 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dlinkPrimeCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkPrimeCommon")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
dlinkPrimeLacpExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 15, 6))
dlinkPrimeLacpExtMIB.setRevisions(('2014-04-26 00:00',))
if mibBuilder.loadTexts: dlinkPrimeLacpExtMIB.setLastUpdated('201404260000Z')
if mibBuilder.loadTexts: dlinkPrimeLacpExtMIB.setOrganization('D-Link Corp.')
dpLacpExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 6, 1))
dpLacpExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 6, 2))
dpLacpExtGroupTable = MibTable((1, 3, 6, 1, 4, 1, 171, 15, 6, 1, 1), )
if mibBuilder.loadTexts: dpLacpExtGroupTable.setStatus('current')
dpLacpExtGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 15, 6, 1, 1, 1), ).setIndexNames((0, "DLINKPRIME-LACP-EXT-MIB", "dpLacpExtGroupChannelNo"))
if mibBuilder.loadTexts: dpLacpExtGroupEntry.setStatus('current')
dpLacpExtGroupChannelNo = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 15, 6, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: dpLacpExtGroupChannelNo.setStatus('current')
dpLacpExtGroupType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 15, 6, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("static_on", 1), ("lacp_active", 2), ("lacp_passive", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dpLacpExtGroupType.setStatus('current')
dpLacpExtGroupMemberPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 15, 6, 1, 1, 1, 3), PortList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dpLacpExtGroupMemberPorts.setStatus('current')
dpLacpExtGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 15, 6, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dpLacpExtGroupRowStatus.setStatus('current')
dpLacpExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 6, 2, 1))
dpLacpExtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 15, 6, 2, 1, 1)).setObjects(("DLINKPRIME-LACP-EXT-MIB", "dpLacpExtChannelGrpInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dpLacpExtCompliance = dpLacpExtCompliance.setStatus('current')
dpLacpExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 6, 2, 2))
dpLacpExtChannelGrpInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 15, 6, 2, 2, 1)).setObjects(("DLINKPRIME-LACP-EXT-MIB", "dpLacpExtGroupType"), ("DLINKPRIME-LACP-EXT-MIB", "dpLacpExtGroupMemberPorts"), ("DLINKPRIME-LACP-EXT-MIB", "dpLacpExtGroupRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dpLacpExtChannelGrpInfoGroup = dpLacpExtChannelGrpInfoGroup.setStatus('current')
mibBuilder.exportSymbols("DLINKPRIME-LACP-EXT-MIB", dpLacpExtGroupEntry=dpLacpExtGroupEntry, dpLacpExtGroupType=dpLacpExtGroupType, PYSNMP_MODULE_ID=dlinkPrimeLacpExtMIB, dlinkPrimeLacpExtMIB=dlinkPrimeLacpExtMIB, dpLacpExtMIBObjects=dpLacpExtMIBObjects, dpLacpExtGroupTable=dpLacpExtGroupTable, dpLacpExtCompliances=dpLacpExtCompliances, dpLacpExtMIBConformance=dpLacpExtMIBConformance, dpLacpExtCompliance=dpLacpExtCompliance, dpLacpExtChannelGrpInfoGroup=dpLacpExtChannelGrpInfoGroup, dpLacpExtGroupRowStatus=dpLacpExtGroupRowStatus, dpLacpExtGroupMemberPorts=dpLacpExtGroupMemberPorts, dpLacpExtGroups=dpLacpExtGroups, dpLacpExtGroupChannelNo=dpLacpExtGroupChannelNo)
