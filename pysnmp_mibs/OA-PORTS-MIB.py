#
# PySNMP MIB module OA-PORTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/mrv/OA-PORTS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:16:49 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
nbSwitchG1Il, = mibBuilder.importSymbols("OS-COMMON-TC-MIB", "nbSwitchG1Il")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nbPortMediaSelectMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 10))
nbPortMediaSelectMIB.setRevisions(('2006-03-08 00:00',))
if mibBuilder.loadTexts: nbPortMediaSelectMIB.setLastUpdated('200603080000Z')
if mibBuilder.loadTexts: nbPortMediaSelectMIB.setOrganization('MRV Communications, Inc.')
nbPortParams = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50, 10))
nbPortMediaSelectConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 10, 101))
nbPortMediaSelectTable = MibTable((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 10, 5), )
if mibBuilder.loadTexts: nbPortMediaSelectTable.setStatus('current')
nbPortMediaSelectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 10, 5, 1), ).setIndexNames((0, "OA-PORTS-MIB", "nbPortMediaSelectPort"))
if mibBuilder.loadTexts: nbPortMediaSelectEntry.setStatus('current')
nbPortMediaSelectPort = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 10, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: nbPortMediaSelectPort.setStatus('current')
nbPortMediaSelectMode = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 10, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("autoSelect", 2), ("forceRJ45", 3), ("forceSFP", 4), ("forceSFP100", 5))).clone('autoSelect')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbPortMediaSelectMode.setStatus('current')
nbPortMediaSelectStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 10, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("rj45", 2), ("sfp", 3), ("sfp100", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbPortMediaSelectStatus.setStatus('current')
nbPortMediaSelectMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 10, 101, 1))
nbPortMediaSelectMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 10, 101, 2))
nbPortMediaSelectMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 10, 101, 1, 1)).setObjects(("OA-PORTS-MIB", "nbPortMediaSelectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nbPortMediaSelectMIBCompliance = nbPortMediaSelectMIBCompliance.setStatus('current')
nbPortMediaSelectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 10, 101, 2, 2)).setObjects(("OA-PORTS-MIB", "nbPortMediaSelectMode"), ("OA-PORTS-MIB", "nbPortMediaSelectStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nbPortMediaSelectGroup = nbPortMediaSelectGroup.setStatus('current')
mibBuilder.exportSymbols("OA-PORTS-MIB", nbPortMediaSelectMIBGroups=nbPortMediaSelectMIBGroups, nbPortMediaSelectGroup=nbPortMediaSelectGroup, nbPortMediaSelectMIB=nbPortMediaSelectMIB, nbPortMediaSelectEntry=nbPortMediaSelectEntry, PYSNMP_MODULE_ID=nbPortMediaSelectMIB, nbPortMediaSelectMode=nbPortMediaSelectMode, nbPortMediaSelectTable=nbPortMediaSelectTable, nbPortMediaSelectPort=nbPortMediaSelectPort, nbPortMediaSelectMIBCompliances=nbPortMediaSelectMIBCompliances, nbPortMediaSelectConformance=nbPortMediaSelectConformance, nbPortParams=nbPortParams, nbPortMediaSelectMIBCompliance=nbPortMediaSelectMIBCompliance, nbPortMediaSelectStatus=nbPortMediaSelectStatus)
