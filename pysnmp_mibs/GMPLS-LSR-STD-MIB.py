#
# PySNMP MIB module GMPLS-LSR-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/GMPLS-LSR-STD-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:27:14 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
GmplsSegmentDirectionTC, = mibBuilder.importSymbols("GMPLS-TC-STD-MIB", "GmplsSegmentDirectionTC")
ifCounterDiscontinuityGroup, ifGeneralInformationGroup = mibBuilder.importSymbols("IF-MIB", "ifCounterDiscontinuityGroup", "ifGeneralInformationGroup")
mplsOutSegmentIndex, mplsInterfaceIndex, mplsInSegmentGroup, mplsInterfaceGroup, mplsInSegmentIndex, mplsPerfGroup, mplsLsrNotificationGroup, mplsXCGroup, mplsOutSegmentGroup = mibBuilder.importSymbols("MPLS-LSR-STD-MIB", "mplsOutSegmentIndex", "mplsInterfaceIndex", "mplsInSegmentGroup", "mplsInterfaceGroup", "mplsInSegmentIndex", "mplsPerfGroup", "mplsLsrNotificationGroup", "mplsXCGroup", "mplsOutSegmentGroup")
mplsStdMIB, = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "mplsStdMIB")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, zeroDotZero, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, ObjectIdentity, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "zeroDotZero", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "ObjectIdentity", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowPointer, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowPointer", "TextualConvention")
gmplsLsrStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 166, 15))
gmplsLsrStdMIB.setRevisions(('2007-02-27 00:00',))
if mibBuilder.loadTexts: gmplsLsrStdMIB.setLastUpdated('200702270000Z')
if mibBuilder.loadTexts: gmplsLsrStdMIB.setOrganization('IETF Common Control And Measurement Plane (CCAMP) Working Group')
gmplsLsrObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 15, 1))
gmplsLsrConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 15, 2))
gmplsInterfaceTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 15, 1, 1), )
if mibBuilder.loadTexts: gmplsInterfaceTable.setStatus('current')
gmplsInterfaceEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 15, 1, 1, 1), ).setIndexNames((0, "MPLS-LSR-STD-MIB", "mplsInterfaceIndex"))
if mibBuilder.loadTexts: gmplsInterfaceEntry.setStatus('current')
gmplsInterfaceSignalingCaps = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 15, 1, 1, 1, 1), Bits().clone(namedValues=NamedValues(("unknown", 0), ("rsvpGmpls", 1), ("crldpGmpls", 2), ("otherGmpls", 3))).clone(namedValues=NamedValues(("rsvpGmpls", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gmplsInterfaceSignalingCaps.setStatus('current')
gmplsInterfaceRsvpHelloPeriod = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 15, 1, 1, 1, 2), Unsigned32().clone(3000)).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: gmplsInterfaceRsvpHelloPeriod.setStatus('current')
gmplsInSegmentTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 15, 1, 2), )
if mibBuilder.loadTexts: gmplsInSegmentTable.setStatus('current')
gmplsInSegmentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 15, 1, 2, 1), ).setIndexNames((0, "MPLS-LSR-STD-MIB", "mplsInSegmentIndex"))
if mibBuilder.loadTexts: gmplsInSegmentEntry.setStatus('current')
gmplsInSegmentDirection = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 15, 1, 2, 1, 1), GmplsSegmentDirectionTC().clone('forward')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gmplsInSegmentDirection.setStatus('current')
gmplsInSegmentExtraParamsPtr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 15, 1, 2, 1, 2), RowPointer().clone((0, 0))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gmplsInSegmentExtraParamsPtr.setStatus('current')
gmplsOutSegmentTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 15, 1, 3), )
if mibBuilder.loadTexts: gmplsOutSegmentTable.setStatus('current')
gmplsOutSegmentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 15, 1, 3, 1), ).setIndexNames((0, "MPLS-LSR-STD-MIB", "mplsOutSegmentIndex"))
if mibBuilder.loadTexts: gmplsOutSegmentEntry.setStatus('current')
gmplsOutSegmentDirection = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 15, 1, 3, 1, 1), GmplsSegmentDirectionTC().clone('forward')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gmplsOutSegmentDirection.setStatus('current')
gmplsOutSegmentTTLDecrement = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 15, 1, 3, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gmplsOutSegmentTTLDecrement.setStatus('current')
gmplsOutSegmentExtraParamsPtr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 15, 1, 3, 1, 3), RowPointer().clone((0, 0))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gmplsOutSegmentExtraParamsPtr.setStatus('current')
gmplsLsrGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 15, 2, 1))
gmplsLsrCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 15, 2, 2))
gmplsLsrModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 166, 15, 2, 2, 1)).setObjects(("IF-MIB", "ifGeneralInformationGroup"), ("IF-MIB", "ifCounterDiscontinuityGroup"), ("MPLS-LSR-STD-MIB", "mplsInterfaceGroup"), ("MPLS-LSR-STD-MIB", "mplsInSegmentGroup"), ("MPLS-LSR-STD-MIB", "mplsOutSegmentGroup"), ("MPLS-LSR-STD-MIB", "mplsXCGroup"), ("MPLS-LSR-STD-MIB", "mplsPerfGroup"), ("MPLS-LSR-STD-MIB", "mplsLsrNotificationGroup"), ("GMPLS-LSR-STD-MIB", "gmplsInterfaceGroup"), ("GMPLS-LSR-STD-MIB", "gmplsInSegmentGroup"), ("GMPLS-LSR-STD-MIB", "gmplsOutSegmentGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gmplsLsrModuleFullCompliance = gmplsLsrModuleFullCompliance.setStatus('current')
gmplsLsrModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 166, 15, 2, 2, 2)).setObjects(("IF-MIB", "ifGeneralInformationGroup"), ("IF-MIB", "ifCounterDiscontinuityGroup"), ("MPLS-LSR-STD-MIB", "mplsInterfaceGroup"), ("MPLS-LSR-STD-MIB", "mplsInSegmentGroup"), ("MPLS-LSR-STD-MIB", "mplsOutSegmentGroup"), ("MPLS-LSR-STD-MIB", "mplsXCGroup"), ("MPLS-LSR-STD-MIB", "mplsPerfGroup"), ("GMPLS-LSR-STD-MIB", "gmplsInterfaceGroup"), ("GMPLS-LSR-STD-MIB", "gmplsInSegmentGroup"), ("GMPLS-LSR-STD-MIB", "gmplsOutSegmentGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gmplsLsrModuleReadOnlyCompliance = gmplsLsrModuleReadOnlyCompliance.setStatus('current')
gmplsInterfaceGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 15, 2, 1, 1)).setObjects(("GMPLS-LSR-STD-MIB", "gmplsInterfaceSignalingCaps"), ("GMPLS-LSR-STD-MIB", "gmplsInterfaceRsvpHelloPeriod"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gmplsInterfaceGroup = gmplsInterfaceGroup.setStatus('current')
gmplsInSegmentGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 15, 2, 1, 2)).setObjects(("GMPLS-LSR-STD-MIB", "gmplsInSegmentDirection"), ("GMPLS-LSR-STD-MIB", "gmplsInSegmentExtraParamsPtr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gmplsInSegmentGroup = gmplsInSegmentGroup.setStatus('current')
gmplsOutSegmentGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 15, 2, 1, 3)).setObjects(("GMPLS-LSR-STD-MIB", "gmplsOutSegmentDirection"), ("GMPLS-LSR-STD-MIB", "gmplsOutSegmentTTLDecrement"), ("GMPLS-LSR-STD-MIB", "gmplsOutSegmentExtraParamsPtr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gmplsOutSegmentGroup = gmplsOutSegmentGroup.setStatus('current')
mibBuilder.exportSymbols("GMPLS-LSR-STD-MIB", gmplsOutSegmentTable=gmplsOutSegmentTable, gmplsLsrModuleReadOnlyCompliance=gmplsLsrModuleReadOnlyCompliance, gmplsLsrGroups=gmplsLsrGroups, gmplsOutSegmentGroup=gmplsOutSegmentGroup, gmplsLsrConformance=gmplsLsrConformance, gmplsLsrObjects=gmplsLsrObjects, gmplsLsrCompliances=gmplsLsrCompliances, PYSNMP_MODULE_ID=gmplsLsrStdMIB, gmplsInSegmentTable=gmplsInSegmentTable, gmplsInterfaceEntry=gmplsInterfaceEntry, gmplsInterfaceTable=gmplsInterfaceTable, gmplsInterfaceGroup=gmplsInterfaceGroup, gmplsInSegmentExtraParamsPtr=gmplsInSegmentExtraParamsPtr, gmplsOutSegmentExtraParamsPtr=gmplsOutSegmentExtraParamsPtr, gmplsOutSegmentEntry=gmplsOutSegmentEntry, gmplsInSegmentDirection=gmplsInSegmentDirection, gmplsLsrModuleFullCompliance=gmplsLsrModuleFullCompliance, gmplsInSegmentEntry=gmplsInSegmentEntry, gmplsInterfaceRsvpHelloPeriod=gmplsInterfaceRsvpHelloPeriod, gmplsOutSegmentDirection=gmplsOutSegmentDirection, gmplsInterfaceSignalingCaps=gmplsInterfaceSignalingCaps, gmplsLsrStdMIB=gmplsLsrStdMIB, gmplsOutSegmentTTLDecrement=gmplsOutSegmentTTLDecrement, gmplsInSegmentGroup=gmplsInSegmentGroup)
