#
# PySNMP MIB module ARUBAWIRED-INTERFACE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/aruba/ARUBAWIRED-INTERFACE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:12:27 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
wndFeatures, = mibBuilder.importSymbols("ARUBAWIRED-NETWORKING-OID", "wndFeatures")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ARUBAWIRED-INTERFACE-MIB", arubaWiredInterfaceAutoneg=arubaWiredInterfaceAutoneg, arubaWiredInterfaceMIB=arubaWiredInterfaceMIB, arubaWiredInterfaceConformance=arubaWiredInterfaceConformance, arubaWiredInterfaceConfig=arubaWiredInterfaceConfig, arubaWiredInterfaceDuplex=arubaWiredInterfaceDuplex, arubaWiredInterfaceSpeeds=arubaWiredInterfaceSpeeds, arubaWiredInterfaceGroups=arubaWiredInterfaceGroups, arubaWiredInterfaceSettings=arubaWiredInterfaceSettings, arubaWiredInterfaceCompliances=arubaWiredInterfaceCompliances, PYSNMP_MODULE_ID=arubaWiredInterfaceMIB, arubaWiredInterfaceIndex=arubaWiredInterfaceIndex, arubaWiredInterfaceCompliance=arubaWiredInterfaceCompliance, arubaWiredInterfaceTable=arubaWiredInterfaceTable, arubaWiredInterfaceEntry=arubaWiredInterfaceEntry)
