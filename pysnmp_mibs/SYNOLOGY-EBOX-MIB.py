#
# PySNMP MIB module SYNOLOGY-EBOX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/synology/SYNOLOGY-EBOX-MIB
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
synologyEbox = ModuleIdentity((1, 3, 6, 1, 4, 1, 6574, 105))
synologyEbox.setRevisions(('2017-06-26 00:00',))
if mibBuilder.loadTexts: synologyEbox.setLastUpdated('201706260000Z')
if mibBuilder.loadTexts: synologyEbox.setOrganization('www.synology.com')
synology = MibIdentifier((1, 3, 6, 1, 4, 1, 6574))
eboxTable = MibTable((1, 3, 6, 1, 4, 1, 6574, 105, 1), )
if mibBuilder.loadTexts: eboxTable.setStatus('current')
eboxEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6574, 105, 1, 1), ).setIndexNames((0, "SYNOLOGY-EBOX-MIB", "eboxIndex"))
if mibBuilder.loadTexts: eboxEntry.setStatus('current')
eboxIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 105, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eboxIndex.setStatus('current')
eboxModel = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 105, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eboxModel.setStatus('current')
eboxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 105, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eboxPower.setStatus('current')
eboxRedundantPower = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 105, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eboxRedundantPower.setStatus('current')
synologyEboxConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 105, 2))
synologyEboxCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 105, 2, 1))
synologyEboxGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 105, 2, 2))
synologyEboxCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6574, 105, 2, 1, 1)).setObjects(("SYNOLOGY-EBOX-MIB", "synologyEboxGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    synologyEboxCompliance = synologyEboxCompliance.setStatus('current')
synologyEboxGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6574, 105, 2, 2, 1)).setObjects(("SYNOLOGY-EBOX-MIB", "eboxIndex"), ("SYNOLOGY-EBOX-MIB", "eboxModel"), ("SYNOLOGY-EBOX-MIB", "eboxPower"), ("SYNOLOGY-EBOX-MIB", "eboxRedundantPower"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    synologyEboxGroup = synologyEboxGroup.setStatus('current')
mibBuilder.exportSymbols("SYNOLOGY-EBOX-MIB", eboxTable=eboxTable, synologyEboxCompliances=synologyEboxCompliances, synologyEboxGroups=synologyEboxGroups, eboxEntry=eboxEntry, eboxModel=eboxModel, synologyEboxCompliance=synologyEboxCompliance, eboxRedundantPower=eboxRedundantPower, synologyEbox=synologyEbox, eboxPower=eboxPower, PYSNMP_MODULE_ID=synologyEbox, synologyEboxConformance=synologyEboxConformance, synology=synology, eboxIndex=eboxIndex, synologyEboxGroup=synologyEboxGroup)
