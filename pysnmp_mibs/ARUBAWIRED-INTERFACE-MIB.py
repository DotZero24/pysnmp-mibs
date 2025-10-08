#
# PySNMP MIB module ARUBAWIRED-INTERFACE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/aruba/ARUBAWIRED-INTERFACE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:44:19 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
wndFeatures, = mibBuilder.importSymbols("ARUBAWIRED-NETWORKING-OID", "wndFeatures")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
arubaWiredInterfaceMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24))
arubaWiredInterfaceMIB.setRevisions(('2021-11-23 00:00',))
if mibBuilder.loadTexts: arubaWiredInterfaceMIB.setLastUpdated('202111230000Z')
if mibBuilder.loadTexts: arubaWiredInterfaceMIB.setOrganization('HPE/Aruba Networking Division')
arubaWiredInterfaceSettings = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 1))
arubaWiredInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 1, 1), )
if mibBuilder.loadTexts: arubaWiredInterfaceTable.setStatus('current')
arubaWiredInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 1, 1, 1), ).setIndexNames((0, "ARUBAWIRED-INTERFACE-MIB", "arubaWiredInterfaceIndex"))
if mibBuilder.loadTexts: arubaWiredInterfaceEntry.setStatus('current')
arubaWiredInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: arubaWiredInterfaceIndex.setStatus('current')
arubaWiredInterfaceAutoneg = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arubaWiredInterfaceAutoneg.setStatus('current')
arubaWiredInterfaceDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("full", 1), ("half", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arubaWiredInterfaceDuplex.setStatus('current')
arubaWiredInterfaceSpeeds = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 1, 1, 1, 4), Bits().clone(namedValues=NamedValues(("speed10M", 0), ("speed100M", 1), ("speed1G", 2), ("speed2p5G", 3), ("speed5G", 4), ("speed10G", 5), ("speed25G", 6), ("speed40G", 7), ("speed50G", 8), ("speed100G", 9), ("speed200G", 10), ("speed400G", 11), ("speed800G", 12)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arubaWiredInterfaceSpeeds.setStatus('current')
arubaWiredInterfaceConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 2))
arubaWiredInterfaceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 2, 1))
arubaWiredInterfaceCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 2, 2))
arubaWiredInterfaceConfig = ObjectGroup((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 2, 1, 1)).setObjects(("ARUBAWIRED-INTERFACE-MIB", "arubaWiredInterfaceAutoneg"), ("ARUBAWIRED-INTERFACE-MIB", "arubaWiredInterfaceDuplex"), ("ARUBAWIRED-INTERFACE-MIB", "arubaWiredInterfaceSpeeds"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    arubaWiredInterfaceConfig = arubaWiredInterfaceConfig.setStatus('current')
arubaWiredInterfaceCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 2, 2, 1)).setObjects(("ARUBAWIRED-INTERFACE-MIB", "arubaWiredInterfaceConfig"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    arubaWiredInterfaceCompliance = arubaWiredInterfaceCompliance.setStatus('current')
mibBuilder.exportSymbols("ARUBAWIRED-INTERFACE-MIB", arubaWiredInterfaceGroups=arubaWiredInterfaceGroups, arubaWiredInterfaceConfig=arubaWiredInterfaceConfig, arubaWiredInterfaceCompliance=arubaWiredInterfaceCompliance, arubaWiredInterfaceSettings=arubaWiredInterfaceSettings, arubaWiredInterfaceEntry=arubaWiredInterfaceEntry, arubaWiredInterfaceCompliances=arubaWiredInterfaceCompliances, arubaWiredInterfaceIndex=arubaWiredInterfaceIndex, arubaWiredInterfaceAutoneg=arubaWiredInterfaceAutoneg, arubaWiredInterfaceDuplex=arubaWiredInterfaceDuplex, arubaWiredInterfaceMIB=arubaWiredInterfaceMIB, PYSNMP_MODULE_ID=arubaWiredInterfaceMIB, arubaWiredInterfaceConformance=arubaWiredInterfaceConformance, arubaWiredInterfaceTable=arubaWiredInterfaceTable, arubaWiredInterfaceSpeeds=arubaWiredInterfaceSpeeds)
