#
# PySNMP MIB module SYNOLOGY-PORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/synology/SYNOLOGY-PORT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:56:53 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("SYNOLOGY-PORT-MIB", ethPortEntry=ethPortEntry, PYSNMP_MODULE_ID=synoEthPort, synoEthPort=synoEthPort, ethPortGroups=ethPortGroups, synology=synology, ethPortConformance=ethPortConformance, ethPortTable=ethPortTable, ethPortCompliance=ethPortCompliance, ethPortGroup=ethPortGroup, ethPortSpeed=ethPortSpeed, ethPortCompliances=ethPortCompliances, ethPortIndex=ethPortIndex, ethPortStatus=ethPortStatus)
