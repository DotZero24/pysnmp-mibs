#
# PySNMP MIB module Juniper-DISMAN-EVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/junose/Juniper-DISMAN-EVENT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:42:23 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
mteTriggerEntry, = mibBuilder.importSymbols("DISMAN-EVENT-MIB", "mteTriggerEntry")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("Juniper-DISMAN-EVENT-MIB", juniDismanEventCompliance=juniDismanEventCompliance, juniDismanEventMIBNotificationObjects=juniDismanEventMIBNotificationObjects, juniDismanEventGroups=juniDismanEventGroups, juniMteTriggerTable=juniMteTriggerTable, juniMteTriggerTableGroup=juniMteTriggerTableGroup, PYSNMP_MODULE_ID=juniDismanEventMIB, juniMteTrigger=juniMteTrigger, juniMteTriggerEntry=juniMteTriggerEntry, juniDismanEventCompliances=juniDismanEventCompliances, juniDismanEventMIBObjects=juniDismanEventMIBObjects, juniDismanEventMIB=juniDismanEventMIB, juniMteExistenceTestResult=juniMteExistenceTestResult, juniDismanEventMIBNotificationPrefix=juniDismanEventMIBNotificationPrefix, juniDismanEventConformance=juniDismanEventConformance, juniMteTriggerContextNameLimit=juniMteTriggerContextNameLimit)
