#
# PySNMP MIB module ENTERASYS-RS-232-MIB-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/enterasys/ENTERASYS-RS-232-MIB-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:17:24 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
rs232PortEntry, = mibBuilder.importSymbols("RS-232-MIB", "rs232PortEntry")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
etsysRs232MibExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 77))
etsysRs232MibExtMIB.setRevisions(('2011-06-22 14:50', '2010-11-09 20:07',))
if mibBuilder.loadTexts: etsysRs232MibExtMIB.setLastUpdated('201106221450Z')
if mibBuilder.loadTexts: etsysRs232MibExtMIB.setOrganization('Enterasys Networks, Inc.')
etsysRs232MibExtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 77, 1))
etsysRs232MibExtVt100 = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 77, 1, 1))
etsysRs232MibExtCtsLink = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 77, 1, 2))
etsysRs232Vt100ExtTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 77, 1, 1, 1), )
if mibBuilder.loadTexts: etsysRs232Vt100ExtTable.setStatus('current')
etsysRs232Vt100ExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 77, 1, 1, 1, 1), )
rs232PortEntry.registerAugmentions(("ENTERASYS-RS-232-MIB-EXT-MIB", "etsysRs232Vt100ExtEntry"))
etsysRs232Vt100ExtEntry.setIndexNames(*rs232PortEntry.getIndexNames())
if mibBuilder.loadTexts: etsysRs232Vt100ExtEntry.setStatus('current')
etsysRs232Vt100DsrEnableState = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 77, 1, 1, 1, 1, 1), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysRs232Vt100DsrEnableState.setStatus('current')
etsysRs232Vt100DsrTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 77, 1, 1, 1, 1, 2), Integer32().clone(3)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysRs232Vt100DsrTimeout.setStatus('current')
etsysRs232CtsLinkExtTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 77, 1, 2, 1), )
if mibBuilder.loadTexts: etsysRs232CtsLinkExtTable.setStatus('current')
etsysRs232CtsLinkExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 77, 1, 2, 1, 1), )
rs232PortEntry.registerAugmentions(("ENTERASYS-RS-232-MIB-EXT-MIB", "etsysRs232CtsLinkExtEntry"))
etsysRs232CtsLinkExtEntry.setIndexNames(*rs232PortEntry.getIndexNames())
if mibBuilder.loadTexts: etsysRs232CtsLinkExtEntry.setStatus('current')
etsysRs232CtsLinkEnableState = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 77, 1, 2, 1, 1, 1), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysRs232CtsLinkEnableState.setStatus('current')
etsysRs232MibExtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 77, 2))
etsysRs232MibExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 77, 2, 1))
etsysRs232MibExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 77, 2, 2))
etsysRs232MibExtVt100DsrGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 77, 2, 1, 1)).setObjects(("ENTERASYS-RS-232-MIB-EXT-MIB", "etsysRs232Vt100DsrEnableState"), ("ENTERASYS-RS-232-MIB-EXT-MIB", "etsysRs232Vt100DsrTimeout"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysRs232MibExtVt100DsrGroup = etsysRs232MibExtVt100DsrGroup.setStatus('current')
etsysRs232MibExtCtsLinkGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 77, 2, 1, 2)).setObjects(("ENTERASYS-RS-232-MIB-EXT-MIB", "etsysRs232CtsLinkEnableState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysRs232MibExtCtsLinkGroup = etsysRs232MibExtCtsLinkGroup.setStatus('current')
etsysRs232MibExtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 77, 2, 2, 1)).setObjects(("ENTERASYS-RS-232-MIB-EXT-MIB", "etsysRs232MibExtVt100DsrGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysRs232MibExtCompliance = etsysRs232MibExtCompliance.setStatus('current')
etsysRs232MibCtsExtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 77, 2, 2, 2)).setObjects(("ENTERASYS-RS-232-MIB-EXT-MIB", "etsysRs232MibExtCtsLinkGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysRs232MibCtsExtCompliance = etsysRs232MibCtsExtCompliance.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-RS-232-MIB-EXT-MIB", etsysRs232MibExtObjects=etsysRs232MibExtObjects, etsysRs232MibExtConformance=etsysRs232MibExtConformance, etsysRs232Vt100ExtTable=etsysRs232Vt100ExtTable, etsysRs232Vt100DsrEnableState=etsysRs232Vt100DsrEnableState, etsysRs232MibCtsExtCompliance=etsysRs232MibCtsExtCompliance, etsysRs232MibExtGroups=etsysRs232MibExtGroups, etsysRs232MibExtCtsLink=etsysRs232MibExtCtsLink, etsysRs232CtsLinkEnableState=etsysRs232CtsLinkEnableState, PYSNMP_MODULE_ID=etsysRs232MibExtMIB, etsysRs232CtsLinkExtEntry=etsysRs232CtsLinkExtEntry, etsysRs232MibExtCompliance=etsysRs232MibExtCompliance, etsysRs232MibExtVt100=etsysRs232MibExtVt100, etsysRs232Vt100ExtEntry=etsysRs232Vt100ExtEntry, etsysRs232CtsLinkExtTable=etsysRs232CtsLinkExtTable, etsysRs232MibExtMIB=etsysRs232MibExtMIB, etsysRs232Vt100DsrTimeout=etsysRs232Vt100DsrTimeout, etsysRs232MibExtCompliances=etsysRs232MibExtCompliances, etsysRs232MibExtCtsLinkGroup=etsysRs232MibExtCtsLinkGroup, etsysRs232MibExtVt100DsrGroup=etsysRs232MibExtVt100DsrGroup)
