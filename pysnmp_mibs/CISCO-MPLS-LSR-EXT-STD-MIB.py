#
# PySNMP MIB module CISCO-MPLS-LSR-EXT-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-MPLS-LSR-EXT-STD-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:25:56 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
mplsXCOutSegmentIndex, mplsInSegmentGroup, mplsPerfGroup, mplsOutSegmentGroup, mplsLsrNotificationGroup, mplsXCGroup, mplsXCInSegmentIndex, mplsXCIndex = mibBuilder.importSymbols("MPLS-LSR-STD-MIB", "mplsXCOutSegmentIndex", "mplsInSegmentGroup", "mplsPerfGroup", "mplsOutSegmentGroup", "mplsLsrNotificationGroup", "mplsXCGroup", "mplsXCInSegmentIndex", "mplsXCIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, RowPointer, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowPointer", "DisplayString")
cmplsLsrExtStdMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 145))
cmplsLsrExtStdMIB.setRevisions(('2012-02-22 00:00',))
if mibBuilder.loadTexts: cmplsLsrExtStdMIB.setLastUpdated('201204300000Z')
if mibBuilder.loadTexts: cmplsLsrExtStdMIB.setOrganization('Multiprotocol Label Switching (MPLS) Working Group')
cmplsLsrExtNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 145, 0))
cmplsLsrExtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 145, 1))
cmplsLsrExtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 145, 2))
cmplsXCExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 145, 1, 1), )
if mibBuilder.loadTexts: cmplsXCExtTable.setStatus('current')
cmplsXCExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 145, 1, 1, 1), ).setIndexNames((0, "MPLS-LSR-STD-MIB", "mplsXCIndex"), (0, "MPLS-LSR-STD-MIB", "mplsXCInSegmentIndex"), (0, "MPLS-LSR-STD-MIB", "mplsXCOutSegmentIndex"))
if mibBuilder.loadTexts: cmplsXCExtEntry.setStatus('current')
cmplsXCExtTunnelPointer = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 145, 1, 1, 1, 1), RowPointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmplsXCExtTunnelPointer.setStatus('current')
cmplsXCOppositeDirXCPtr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 145, 1, 1, 1, 2), RowPointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmplsXCOppositeDirXCPtr.setStatus('current')
cmplsLsrExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 145, 2, 1))
cmplsLsrExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 145, 2, 2))
cmplsLsrExtModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 145, 2, 2, 1)).setObjects(("MPLS-LSR-STD-MIB", "mplsInSegmentGroup"), ("MPLS-LSR-STD-MIB", "mplsOutSegmentGroup"), ("MPLS-LSR-STD-MIB", "mplsXCGroup"), ("MPLS-LSR-STD-MIB", "mplsPerfGroup"), ("MPLS-LSR-STD-MIB", "mplsLsrNotificationGroup"), ("CISCO-MPLS-LSR-EXT-STD-MIB", "cmplsXCExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmplsLsrExtModuleFullCompliance = cmplsLsrExtModuleFullCompliance.setStatus('current')
cmplsLsrExtModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 145, 2, 2, 2)).setObjects(("MPLS-LSR-STD-MIB", "mplsInterfaceGroup"), ("MPLS-LSR-STD-MIB", "mplsInSegmentGroup"), ("MPLS-LSR-STD-MIB", "mplsOutSegmentGroup"), ("MPLS-LSR-STD-MIB", "mplsXCGroup"), ("MPLS-LSR-STD-MIB", "mplsPerfGroup"), ("CISCO-MPLS-LSR-EXT-STD-MIB", "cmplsXCExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmplsLsrExtModuleReadOnlyCompliance = cmplsLsrExtModuleReadOnlyCompliance.setStatus('current')
cmplsXCExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 145, 2, 1, 1)).setObjects(("CISCO-MPLS-LSR-EXT-STD-MIB", "cmplsXCExtTunnelPointer"), ("CISCO-MPLS-LSR-EXT-STD-MIB", "cmplsXCOppositeDirXCPtr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmplsXCExtGroup = cmplsXCExtGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-MPLS-LSR-EXT-STD-MIB", cmplsXCExtGroup=cmplsXCExtGroup, cmplsLsrExtNotifications=cmplsLsrExtNotifications, cmplsLsrExtObjects=cmplsLsrExtObjects, PYSNMP_MODULE_ID=cmplsLsrExtStdMIB, cmplsLsrExtModuleReadOnlyCompliance=cmplsLsrExtModuleReadOnlyCompliance, cmplsXCExtEntry=cmplsXCExtEntry, cmplsLsrExtModuleFullCompliance=cmplsLsrExtModuleFullCompliance, cmplsLsrExtConformance=cmplsLsrExtConformance, cmplsLsrExtGroups=cmplsLsrExtGroups, cmplsXCExtTunnelPointer=cmplsXCExtTunnelPointer, cmplsLsrExtStdMIB=cmplsLsrExtStdMIB, cmplsXCExtTable=cmplsXCExtTable, cmplsLsrExtCompliances=cmplsLsrExtCompliances, cmplsXCOppositeDirXCPtr=cmplsXCOppositeDirXCPtr)
