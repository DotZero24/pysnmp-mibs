#
# PySNMP MIB module WESTERMO-INTERFACE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/westermo/WESTERMO-INTERFACE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:01:13 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
IANAifType, = mibBuilder.importSymbols("IANAifType-MIB", "IANAifType")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
common, = mibBuilder.importSymbols("WESTERMO-OID-MIB", "common")
wmoInterface = ModuleIdentity((1, 3, 6, 1, 4, 1, 16177, 2, 4))
wmoInterface.setRevisions(('2019-08-30 00:00',))
if mibBuilder.loadTexts: wmoInterface.setLastUpdated('201908300000Z')
if mibBuilder.loadTexts: wmoInterface.setOrganization('Westermo')
class IfaceRefIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 1000)

wmoInterfaceObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 16177, 2, 4, 1))
wmoInterfaceConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 16177, 2, 4, 2))
ifRefTable = MibTable((1, 3, 6, 1, 4, 1, 16177, 2, 4, 1, 1), )
if mibBuilder.loadTexts: ifRefTable.setStatus('current')
ifRefEntry = MibTableRow((1, 3, 6, 1, 4, 1, 16177, 2, 4, 1, 1, 1), ).setIndexNames((0, "WESTERMO-INTERFACE-MIB", "ifRefIndex"))
if mibBuilder.loadTexts: ifRefEntry.setStatus('current')
ifRefIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 16177, 2, 4, 1, 1, 1, 1), IfaceRefIndex())
if mibBuilder.loadTexts: ifRefIndex.setStatus('current')
ifRefifIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 16177, 2, 4, 1, 1, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifRefifIndex.setStatus('current')
ifRefifName = MibTableColumn((1, 3, 6, 1, 4, 1, 16177, 2, 4, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifRefifName.setStatus('current')
ifRefifDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 16177, 2, 4, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifRefifDescr.setStatus('current')
ifRefifType = MibTableColumn((1, 3, 6, 1, 4, 1, 16177, 2, 4, 1, 1, 1, 5), IANAifType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifRefifType.setStatus('current')
wmoInterfaceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 16177, 2, 4, 2, 1))
wmoInterfaceCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 16177, 2, 4, 2, 2))
wmoInterfaceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 16177, 2, 4, 2, 1, 1)).setObjects(("WESTERMO-INTERFACE-MIB", "ifRefifIndex"), ("WESTERMO-INTERFACE-MIB", "ifRefifName"), ("WESTERMO-INTERFACE-MIB", "ifRefifDescr"), ("WESTERMO-INTERFACE-MIB", "ifRefifType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    wmoInterfaceGroup = wmoInterfaceGroup.setStatus('current')
wmoInterfaceCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 16177, 2, 4, 2, 2, 1)).setObjects(("WESTERMO-INTERFACE-MIB", "wmoInterfaceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    wmoInterfaceCompliance = wmoInterfaceCompliance.setStatus('current')
mibBuilder.exportSymbols("WESTERMO-INTERFACE-MIB", ifRefifDescr=ifRefifDescr, wmoInterface=wmoInterface, ifRefifIndex=ifRefifIndex, IfaceRefIndex=IfaceRefIndex, wmoInterfaceCompliances=wmoInterfaceCompliances, wmoInterfaceConformance=wmoInterfaceConformance, wmoInterfaceObjects=wmoInterfaceObjects, PYSNMP_MODULE_ID=wmoInterface, ifRefIndex=ifRefIndex, wmoInterfaceGroup=wmoInterfaceGroup, wmoInterfaceCompliance=wmoInterfaceCompliance, ifRefTable=ifRefTable, wmoInterfaceGroups=wmoInterfaceGroups, ifRefEntry=ifRefEntry, ifRefifType=ifRefifType, ifRefifName=ifRefifName)
