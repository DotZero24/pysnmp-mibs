#
# PySNMP MIB module MPLS-LSR-EXT-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/MPLS-LSR-EXT-STD-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:27:31 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
mplsXCOutSegmentIndex, mplsXCInSegmentIndex, mplsInSegmentGroup, mplsInterfaceGroup, mplsLsrNotificationGroup, mplsXCGroup, mplsOutSegmentGroup, mplsXCIndex = mibBuilder.importSymbols("MPLS-LSR-STD-MIB", "mplsXCOutSegmentIndex", "mplsXCInSegmentIndex", "mplsInSegmentGroup", "mplsInterfaceGroup", "mplsLsrNotificationGroup", "mplsXCGroup", "mplsOutSegmentGroup", "mplsXCIndex")
mplsStdMIB, = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "mplsStdMIB")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowPointer, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowPointer", "TextualConvention")
mplsLsrExtStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 166, 19))
mplsLsrExtStdMIB.setRevisions(('2015-02-02 00:00',))
if mibBuilder.loadTexts: mplsLsrExtStdMIB.setLastUpdated('201502020000Z')
if mibBuilder.loadTexts: mplsLsrExtStdMIB.setOrganization('Multiprotocol Label Switching (MPLS) Working Group')
mplsLsrExtNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 19, 0))
mplsLsrExtObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 19, 1))
mplsLsrExtConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 19, 2))
mplsXCExtTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 19, 1, 1), )
if mibBuilder.loadTexts: mplsXCExtTable.setStatus('current')
mplsXCExtEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 19, 1, 1, 1), ).setIndexNames((0, "MPLS-LSR-STD-MIB", "mplsXCIndex"), (0, "MPLS-LSR-STD-MIB", "mplsXCInSegmentIndex"), (0, "MPLS-LSR-STD-MIB", "mplsXCOutSegmentIndex"))
if mibBuilder.loadTexts: mplsXCExtEntry.setStatus('current')
mplsXCExtTunnelPointer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 19, 1, 1, 1, 1), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsXCExtTunnelPointer.setStatus('current')
mplsXCExtOppositeDirXCPtr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 19, 1, 1, 1, 2), RowPointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsXCExtOppositeDirXCPtr.setStatus('current')
mplsLsrExtCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 19, 2, 1))
mplsLsrExtGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 19, 2, 2))
mplsLsrExtModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 166, 19, 2, 1, 1)).setObjects(("MPLS-LSR-STD-MIB", "mplsInSegmentGroup"), ("MPLS-LSR-STD-MIB", "mplsOutSegmentGroup"), ("MPLS-LSR-STD-MIB", "mplsXCGroup"), ("MPLS-LSR-STD-MIB", "mplsLsrNotificationGroup"), ("MPLS-LSR-EXT-STD-MIB", "mplsXCExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsLsrExtModuleFullCompliance = mplsLsrExtModuleFullCompliance.setStatus('current')
mplsLsrExtModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 166, 19, 2, 1, 2)).setObjects(("MPLS-LSR-STD-MIB", "mplsInterfaceGroup"), ("MPLS-LSR-STD-MIB", "mplsInSegmentGroup"), ("MPLS-LSR-STD-MIB", "mplsOutSegmentGroup"), ("MPLS-LSR-EXT-STD-MIB", "mplsXCExtReadOnlyObjectsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsLsrExtModuleReadOnlyCompliance = mplsLsrExtModuleReadOnlyCompliance.setStatus('current')
mplsXCExtGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 19, 2, 2, 1)).setObjects(("MPLS-LSR-EXT-STD-MIB", "mplsXCExtTunnelPointer"), ("MPLS-LSR-EXT-STD-MIB", "mplsXCExtOppositeDirXCPtr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsXCExtGroup = mplsXCExtGroup.setStatus('current')
mplsXCExtReadOnlyObjectsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 19, 2, 2, 2)).setObjects(("MPLS-LSR-EXT-STD-MIB", "mplsXCExtTunnelPointer"), ("MPLS-LSR-EXT-STD-MIB", "mplsXCExtOppositeDirXCPtr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsXCExtReadOnlyObjectsGroup = mplsXCExtReadOnlyObjectsGroup.setStatus('current')
mibBuilder.exportSymbols("MPLS-LSR-EXT-STD-MIB", mplsLsrExtStdMIB=mplsLsrExtStdMIB, mplsLsrExtModuleReadOnlyCompliance=mplsLsrExtModuleReadOnlyCompliance, mplsXCExtReadOnlyObjectsGroup=mplsXCExtReadOnlyObjectsGroup, mplsLsrExtObjects=mplsLsrExtObjects, mplsXCExtEntry=mplsXCExtEntry, mplsLsrExtGroups=mplsLsrExtGroups, mplsLsrExtConformance=mplsLsrExtConformance, mplsXCExtTable=mplsXCExtTable, mplsXCExtTunnelPointer=mplsXCExtTunnelPointer, mplsXCExtGroup=mplsXCExtGroup, mplsLsrExtCompliances=mplsLsrExtCompliances, mplsLsrExtModuleFullCompliance=mplsLsrExtModuleFullCompliance, PYSNMP_MODULE_ID=mplsLsrExtStdMIB, mplsXCExtOppositeDirXCPtr=mplsXCExtOppositeDirXCPtr, mplsLsrExtNotifications=mplsLsrExtNotifications)
