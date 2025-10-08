#
# PySNMP MIB module Juniper-UNI-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/junose/Juniper-UNI-IF-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:23:07 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifStackHigherLayer, ifStackLowerLayer, ifEntry = mibBuilder.importSymbols("IF-MIB", "ifStackHigherLayer", "ifStackLowerLayer", "ifEntry")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
juniIfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3))
juniIfMIB.setRevisions(('2014-03-25 21:30', '2005-10-11 20:40', '2003-07-16 21:40', '2003-02-06 15:57', '2002-01-22 16:52', '2001-03-28 15:12', '2000-11-22 23:41', '2000-09-29 18:35', '2000-07-27 15:45', '2000-05-05 15:08', '1999-12-21 15:18', '1999-09-03 14:16', '1998-11-13 20:19',))
if mibBuilder.loadTexts: juniIfMIB.setLastUpdated('200510112040Z')
if mibBuilder.loadTexts: juniIfMIB.setOrganization('Juniper Networks, Inc.')
class JuniIfType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50, 51, 52, 53, 54, 55, 145, 256, 257))
    namedValues = NamedValues(("ip", 0), ("ppp", 1), ("ds0", 2), ("ds1", 3), ("ds3", 4), ("frameRelay", 5), ("ethernet", 6), ("sonet", 7), ("sonetPath", 8), ("atm", 9), ("aal5", 10), ("atmSubInterface", 11), ("ft1", 12), ("hdlc", 13), ("ipLoopback", 14), ("ipVirtual", 15), ("frSubInterface", 16), ("pppoe", 17), ("pppoeSubInterface", 18), ("bridgedEthernet", 19), ("l2tpTunnelInterface", 20), ("l2tpSessionInterface", 21), ("mlPppLinkInterface", 22), ("slepInterface", 23), ("l2tpDestinationInterface", 24), ("mplsMajorInterface", 25), ("mplsMinorInterface", 26), ("mlPppNetworkInterface", 27), ("ethernetSubInterface", 28), ("multilinkFrameRelayInterface", 29), ("ipTunnelInterface", 30), ("serverPortInterface", 31), ("smdsInterface", 32), ("sonetVTInterface", 33), ("vlanMajorInterface", 34), ("vlanSubInterface", 35), ("cbfInterface", 36), ("gtpInterface", 37), ("smdsMajorInterface", 38), ("smdsSubInterface", 39), ("l2fTunnelInterface", 40), ("l2fSessionInterface", 41), ("l2fDestinationInterface", 42), ("ipsecInterface", 43), ("sgInterface", 44), ("mplsL2ShimInterface", 45), ("lacGenInterface", 47), ("bridgeInterface", 48), ("ipsecTransportInterface", 49), ("ipv6Interface", 50), ("ipv6TunnelInterface", 51), ("ipv6Loopback", 52), ("osi", 53), ("lag", 54), ("ipTunnelMdt", 55), ("atmVirtualCircuit", 145), ("pppLink", 256), ("atmActiveSubInterface", 257))

juniInterfaces = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1))
juniIf = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1))
juniIfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1))
juniIfTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 1), )
if mibBuilder.loadTexts: juniIfTable.setStatus('current')
juniIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 1, 1), )
ifEntry.registerAugmentions(("Juniper-UNI-IF-MIB", "juniIfEntry"))
juniIfEntry.setIndexNames(*ifEntry.getIndexNames())
if mibBuilder.loadTexts: juniIfEntry.setStatus('current')
juniIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 1, 1, 1), JuniIfType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniIfType.setStatus('current')
juniIfInvStackTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 2), )
if mibBuilder.loadTexts: juniIfInvStackTable.setStatus('current')
juniIfInvStackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifStackLowerLayer"), (0, "IF-MIB", "ifStackHigherLayer"))
if mibBuilder.loadTexts: juniIfInvStackEntry.setStatus('current')
juniIfInvStackStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 2, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniIfInvStackStatus.setStatus('current')
juniIfCountTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 3), )
if mibBuilder.loadTexts: juniIfCountTable.setStatus('current')
juniIfCountEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 3, 1), ).setIndexNames((0, "Juniper-UNI-IF-MIB", "juniIfCountIfType"))
if mibBuilder.loadTexts: juniIfCountEntry.setStatus('current')
juniIfCountIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 3, 1, 1), JuniIfType())
if mibBuilder.loadTexts: juniIfCountIfType.setStatus('current')
juniIfCountNumberOfInterfaces = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 3, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniIfCountNumberOfInterfaces.setStatus('current')
juniIfConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4))
juniIfCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 1))
juniIfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 2))
juniIfCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 1, 1)).setObjects(("Juniper-UNI-IF-MIB", "juniIfGroup"), ("Juniper-UNI-IF-MIB", "juniIfInvStackGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIfCompliance = juniIfCompliance.setStatus('current')
juniIfCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 1, 2)).setObjects(("Juniper-UNI-IF-MIB", "juniIfGroup"), ("Juniper-UNI-IF-MIB", "juniIfInvStackGroup"), ("Juniper-UNI-IF-MIB", "juniIfCountGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIfCompliance1 = juniIfCompliance1.setStatus('current')
juniIfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 2, 1)).setObjects(("Juniper-UNI-IF-MIB", "juniIfType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIfGroup = juniIfGroup.setStatus('current')
juniIfInvStackGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 2, 2)).setObjects(("Juniper-UNI-IF-MIB", "juniIfInvStackStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIfInvStackGroup = juniIfInvStackGroup.setStatus('current')
juniIfCountGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 2, 3)).setObjects(("Juniper-UNI-IF-MIB", "juniIfCountNumberOfInterfaces"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIfCountGroup = juniIfCountGroup.setStatus('current')
mibBuilder.exportSymbols("Juniper-UNI-IF-MIB", JuniIfType=JuniIfType, juniIfEntry=juniIfEntry, PYSNMP_MODULE_ID=juniIfMIB, juniIfType=juniIfType, juniInterfaces=juniInterfaces, juniIfCompliance=juniIfCompliance, juniIfTable=juniIfTable, juniIfConformance=juniIfConformance, juniIfObjects=juniIfObjects, juniIfCompliance1=juniIfCompliance1, juniIfInvStackEntry=juniIfInvStackEntry, juniIf=juniIf, juniIfInvStackStatus=juniIfInvStackStatus, juniIfCompliances=juniIfCompliances, juniIfMIB=juniIfMIB, juniIfCountTable=juniIfCountTable, juniIfInvStackTable=juniIfInvStackTable, juniIfCountEntry=juniIfCountEntry, juniIfCountGroup=juniIfCountGroup, juniIfCountIfType=juniIfCountIfType, juniIfGroup=juniIfGroup, juniIfInvStackGroup=juniIfInvStackGroup, juniIfGroups=juniIfGroups, juniIfCountNumberOfInterfaces=juniIfCountNumberOfInterfaces)
