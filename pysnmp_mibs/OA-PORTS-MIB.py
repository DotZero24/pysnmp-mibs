#
# PySNMP MIB module OA-PORTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/mrv/OA-PORTS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:40 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
nbSwitchG1Il, = mibBuilder.importSymbols("OS-COMMON-TC-MIB", "nbSwitchG1Il")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("OA-PORTS-MIB", nbPortParams=nbPortParams, nbPortMediaSelectPort=nbPortMediaSelectPort, nbPortMediaSelectEntry=nbPortMediaSelectEntry, nbPortMediaSelectGroup=nbPortMediaSelectGroup, nbPortMediaSelectTable=nbPortMediaSelectTable, nbPortMediaSelectMode=nbPortMediaSelectMode, nbPortMediaSelectMIBCompliance=nbPortMediaSelectMIBCompliance, PYSNMP_MODULE_ID=nbPortMediaSelectMIB, nbPortMediaSelectMIBGroups=nbPortMediaSelectMIBGroups, nbPortMediaSelectMIB=nbPortMediaSelectMIB, nbPortMediaSelectMIBCompliances=nbPortMediaSelectMIBCompliances, nbPortMediaSelectStatus=nbPortMediaSelectStatus, nbPortMediaSelectConformance=nbPortMediaSelectConformance)
