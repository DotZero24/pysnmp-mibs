#
# PySNMP MIB module Juniper-DISMAN-EVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/junose/Juniper-DISMAN-EVENT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:22:52 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
mteTriggerEntry, = mibBuilder.importSymbols("DISMAN-EVENT-MIB", "mteTriggerEntry")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniDismanEventMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 66))
juniDismanEventMIB.setRevisions(('2003-10-30 15:35',))
if mibBuilder.loadTexts: juniDismanEventMIB.setLastUpdated('200310301535Z')
if mibBuilder.loadTexts: juniDismanEventMIB.setOrganization('Juniper Networks, Inc.')
juniDismanEventMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 1))
juniMteTrigger = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 1, 1))
juniMteTriggerTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 1, 1, 1), )
if mibBuilder.loadTexts: juniMteTriggerTable.setStatus('current')
juniMteTriggerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 1, 1, 1, 1), )
mteTriggerEntry.registerAugmentions(("Juniper-DISMAN-EVENT-MIB", "juniMteTriggerEntry"))
juniMteTriggerEntry.setIndexNames(*mteTriggerEntry.getIndexNames())
if mibBuilder.loadTexts: juniMteTriggerEntry.setStatus('current')
juniMteTriggerContextNameLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 1, 1, 1, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniMteTriggerContextNameLimit.setStatus('current')
juniDismanEventMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 2))
juniDismanEventMIBNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 2, 1))
juniMteExistenceTestResult = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("present", 0), ("absent", 1), ("changed", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: juniMteExistenceTestResult.setStatus('current')
juniDismanEventConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 3))
juniDismanEventCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 3, 1))
juniDismanEventGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 3, 2))
juniDismanEventCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 3, 1, 1)).setObjects(("Juniper-DISMAN-EVENT-MIB", "juniMteTriggerTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDismanEventCompliance = juniDismanEventCompliance.setStatus('current')
juniMteTriggerTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 3, 2, 1)).setObjects(("Juniper-DISMAN-EVENT-MIB", "juniMteTriggerContextNameLimit"), ("Juniper-DISMAN-EVENT-MIB", "juniMteExistenceTestResult"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniMteTriggerTableGroup = juniMteTriggerTableGroup.setStatus('current')
mibBuilder.exportSymbols("Juniper-DISMAN-EVENT-MIB", juniDismanEventCompliance=juniDismanEventCompliance, juniMteTriggerContextNameLimit=juniMteTriggerContextNameLimit, juniDismanEventCompliances=juniDismanEventCompliances, juniDismanEventMIB=juniDismanEventMIB, juniDismanEventMIBNotificationPrefix=juniDismanEventMIBNotificationPrefix, juniDismanEventMIBObjects=juniDismanEventMIBObjects, PYSNMP_MODULE_ID=juniDismanEventMIB, juniMteTriggerEntry=juniMteTriggerEntry, juniMteTriggerTable=juniMteTriggerTable, juniDismanEventMIBNotificationObjects=juniDismanEventMIBNotificationObjects, juniMteExistenceTestResult=juniMteExistenceTestResult, juniDismanEventConformance=juniDismanEventConformance, juniDismanEventGroups=juniDismanEventGroups, juniMteTrigger=juniMteTrigger, juniMteTriggerTableGroup=juniMteTriggerTableGroup)
