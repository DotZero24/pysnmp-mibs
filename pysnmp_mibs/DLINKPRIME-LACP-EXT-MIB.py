#
# PySNMP MIB module DLINKPRIME-LACP-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/DLINKPRIME-LACP-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:33:38 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dlinkPrimeCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkPrimeCommon")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
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
mibBuilder.exportSymbols("DLINKPRIME-LACP-EXT-MIB", dpLacpExtGroupTable=dpLacpExtGroupTable, dlinkPrimeLacpExtMIB=dlinkPrimeLacpExtMIB, dpLacpExtGroupMemberPorts=dpLacpExtGroupMemberPorts, dpLacpExtChannelGrpInfoGroup=dpLacpExtChannelGrpInfoGroup, dpLacpExtGroupType=dpLacpExtGroupType, dpLacpExtGroups=dpLacpExtGroups, dpLacpExtMIBConformance=dpLacpExtMIBConformance, dpLacpExtGroupEntry=dpLacpExtGroupEntry, dpLacpExtGroupRowStatus=dpLacpExtGroupRowStatus, dpLacpExtGroupChannelNo=dpLacpExtGroupChannelNo, dpLacpExtCompliance=dpLacpExtCompliance, dpLacpExtMIBObjects=dpLacpExtMIBObjects, PYSNMP_MODULE_ID=dlinkPrimeLacpExtMIB, dpLacpExtCompliances=dpLacpExtCompliances)
