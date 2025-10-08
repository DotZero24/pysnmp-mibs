#
# PySNMP MIB module SYNOLOGY-PORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/synology/SYNOLOGY-PORT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:30 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
synoEthPort = ModuleIdentity((1, 3, 6, 1, 4, 1, 6574, 109))
synoEthPort.setRevisions(('2020-12-20 00:00',))
if mibBuilder.loadTexts: synoEthPort.setLastUpdated('202012200000Z')
if mibBuilder.loadTexts: synoEthPort.setOrganization('www.synology.com')
synology = MibIdentifier((1, 3, 6, 1, 4, 1, 6574))
ethPortTable = MibTable((1, 3, 6, 1, 4, 1, 6574, 109, 1), )
if mibBuilder.loadTexts: ethPortTable.setStatus('current')
ethPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6574, 109, 1, 1), ).setIndexNames((0, "SYNOLOGY-PORT-MIB", "ethPortIndex"))
if mibBuilder.loadTexts: ethPortEntry.setStatus('current')
ethPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 109, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ethPortIndex.setStatus('current')
ethPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 109, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("up", 2), ("down", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethPortStatus.setStatus('current')
ethPortSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 109, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethPortSpeed.setStatus('current')
ethPortConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 109, 2))
ethPortCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 109, 2, 1))
ethPortGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 109, 2, 2))
ethPortCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6574, 109, 2, 1, 1)).setObjects(("SYNOLOGY-PORT-MIB", "ethPortGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ethPortCompliance = ethPortCompliance.setStatus('current')
ethPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6574, 109, 2, 2, 1)).setObjects(("SYNOLOGY-PORT-MIB", "ethPortStatus"), ("SYNOLOGY-PORT-MIB", "ethPortSpeed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ethPortGroup = ethPortGroup.setStatus('current')
mibBuilder.exportSymbols("SYNOLOGY-PORT-MIB", ethPortConformance=ethPortConformance, ethPortGroups=ethPortGroups, ethPortCompliance=ethPortCompliance, ethPortEntry=ethPortEntry, synoEthPort=synoEthPort, ethPortGroup=ethPortGroup, ethPortStatus=ethPortStatus, ethPortTable=ethPortTable, ethPortSpeed=ethPortSpeed, ethPortIndex=ethPortIndex, synology=synology, ethPortCompliances=ethPortCompliances, PYSNMP_MODULE_ID=synoEthPort)
