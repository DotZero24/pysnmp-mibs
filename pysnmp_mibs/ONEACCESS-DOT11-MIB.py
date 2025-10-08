#
# PySNMP MIB module ONEACCESS-DOT11-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/oneaccess/ONEACCESS-DOT11-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:01:23 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
oacRequirements, oacMIBModules, oacExpIMDot11 = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oacRequirements", "oacMIBModules", "oacExpIMDot11")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
MacAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TextualConvention")
oacDot11MIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 1, 100, 900))
oacDot11MIBModule.setRevisions(('2011-10-27 00:00', '2010-07-08 00:01',))
if mibBuilder.loadTexts: oacDot11MIBModule.setLastUpdated('201110270000Z')
if mibBuilder.loadTexts: oacDot11MIBModule.setOrganization(' OneAccess ')
class InterfaceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("mainInterface", 1), ("subInterface", 2))

oacExpIMDot11Objects = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 8, 1))
oacExpIMDot11InterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 8, 1, 1), )
if mibBuilder.loadTexts: oacExpIMDot11InterfaceTable.setStatus('current')
oacExpIMDot11InterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 8, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: oacExpIMDot11InterfaceEntry.setStatus('current')
oacExpIMDot11EntryType = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 8, 1, 1, 1, 1), InterfaceType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacExpIMDot11EntryType.setStatus('current')
oacExpIMDot11MACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 8, 1, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacExpIMDot11MACAddress.setStatus('current')
oacExpIMDot11SSID = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 8, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacExpIMDot11SSID.setStatus('current')
oacExpIMDot11AssociatedStations = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 8, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacExpIMDot11AssociatedStations.setStatus('current')
oacExpIMDot11Conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 5, 900))
oacExpIMDot11Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 5, 900, 1))
oacExpIMDot11Compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 5, 900, 2))
oacExpIMDot11Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 13191, 5, 900, 2, 1)).setObjects(("ONEACCESS-DOT11-MIB", "oacExpIMDot11GeneralGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oacExpIMDot11Compliance = oacExpIMDot11Compliance.setStatus('current')
oacExpIMDot11GeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13191, 5, 900, 1, 1)).setObjects(("ONEACCESS-DOT11-MIB", "oacExpIMDot11EntryType"), ("ONEACCESS-DOT11-MIB", "oacExpIMDot11MACAddress"), ("ONEACCESS-DOT11-MIB", "oacExpIMDot11SSID"), ("ONEACCESS-DOT11-MIB", "oacExpIMDot11AssociatedStations"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oacExpIMDot11GeneralGroup = oacExpIMDot11GeneralGroup.setStatus('current')
mibBuilder.exportSymbols("ONEACCESS-DOT11-MIB", oacExpIMDot11InterfaceTable=oacExpIMDot11InterfaceTable, oacExpIMDot11Compliances=oacExpIMDot11Compliances, oacExpIMDot11AssociatedStations=oacExpIMDot11AssociatedStations, oacExpIMDot11GeneralGroup=oacExpIMDot11GeneralGroup, oacExpIMDot11Conformance=oacExpIMDot11Conformance, PYSNMP_MODULE_ID=oacDot11MIBModule, oacExpIMDot11EntryType=oacExpIMDot11EntryType, oacExpIMDot11MACAddress=oacExpIMDot11MACAddress, oacExpIMDot11Compliance=oacExpIMDot11Compliance, oacExpIMDot11Objects=oacExpIMDot11Objects, oacExpIMDot11InterfaceEntry=oacExpIMDot11InterfaceEntry, oacExpIMDot11SSID=oacExpIMDot11SSID, oacExpIMDot11Groups=oacExpIMDot11Groups, InterfaceType=InterfaceType, oacDot11MIBModule=oacDot11MIBModule)
