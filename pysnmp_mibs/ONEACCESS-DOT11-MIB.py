#
# PySNMP MIB module ONEACCESS-DOT11-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/oneaccess/ONEACCESS-DOT11-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:36:05 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
oacExpIMDot11, oacMIBModules, oacRequirements = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oacExpIMDot11", "oacMIBModules", "oacRequirements")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention")
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
mibBuilder.exportSymbols("ONEACCESS-DOT11-MIB", oacExpIMDot11Objects=oacExpIMDot11Objects, oacExpIMDot11GeneralGroup=oacExpIMDot11GeneralGroup, oacExpIMDot11Conformance=oacExpIMDot11Conformance, oacExpIMDot11InterfaceTable=oacExpIMDot11InterfaceTable, oacExpIMDot11MACAddress=oacExpIMDot11MACAddress, oacExpIMDot11Compliance=oacExpIMDot11Compliance, PYSNMP_MODULE_ID=oacDot11MIBModule, oacExpIMDot11AssociatedStations=oacExpIMDot11AssociatedStations, oacExpIMDot11Groups=oacExpIMDot11Groups, oacExpIMDot11Compliances=oacExpIMDot11Compliances, oacExpIMDot11InterfaceEntry=oacExpIMDot11InterfaceEntry, oacDot11MIBModule=oacDot11MIBModule, InterfaceType=InterfaceType, oacExpIMDot11EntryType=oacExpIMDot11EntryType, oacExpIMDot11SSID=oacExpIMDot11SSID)
