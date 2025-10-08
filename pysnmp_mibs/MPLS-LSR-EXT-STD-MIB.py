#
# PySNMP MIB module MPLS-LSR-EXT-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/rfc/MPLS-LSR-EXT-STD-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:49:53 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
mplsXCOutSegmentIndex, mplsInSegmentGroup, mplsOutSegmentGroup, mplsLsrNotificationGroup, mplsInterfaceGroup, mplsXCGroup, mplsXCInSegmentIndex, mplsXCIndex = mibBuilder.importSymbols("MPLS-LSR-STD-MIB", "mplsXCOutSegmentIndex", "mplsInSegmentGroup", "mplsOutSegmentGroup", "mplsLsrNotificationGroup", "mplsInterfaceGroup", "mplsXCGroup", "mplsXCInSegmentIndex", "mplsXCIndex")
mplsStdMIB, = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "mplsStdMIB")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, RowPointer, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowPointer", "DisplayString")
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
mibBuilder.exportSymbols("MPLS-LSR-EXT-STD-MIB", mplsLsrExtModuleFullCompliance=mplsLsrExtModuleFullCompliance, mplsXCExtGroup=mplsXCExtGroup, mplsLsrExtGroups=mplsLsrExtGroups, mplsLsrExtModuleReadOnlyCompliance=mplsLsrExtModuleReadOnlyCompliance, mplsLsrExtCompliances=mplsLsrExtCompliances, mplsLsrExtConformance=mplsLsrExtConformance, mplsXCExtEntry=mplsXCExtEntry, mplsXCExtTable=mplsXCExtTable, mplsLsrExtNotifications=mplsLsrExtNotifications, mplsXCExtReadOnlyObjectsGroup=mplsXCExtReadOnlyObjectsGroup, mplsXCExtTunnelPointer=mplsXCExtTunnelPointer, mplsLsrExtObjects=mplsLsrExtObjects, mplsXCExtOppositeDirXCPtr=mplsXCExtOppositeDirXCPtr, mplsLsrExtStdMIB=mplsLsrExtStdMIB, PYSNMP_MODULE_ID=mplsLsrExtStdMIB)
