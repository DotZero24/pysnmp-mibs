#
# PySNMP MIB module NEWTEC-FANCONTROLLER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/newtec/NEWTEC-FANCONTROLLER-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:31 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ntcFunction, = mibBuilder.importSymbols("NEWTEC-MAIN-MIB", "ntcFunction")
NtcAlarmState, = mibBuilder.importSymbols("NEWTEC-TC-MIB", "NtcAlarmState")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ntcFanController = ModuleIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 3500))
ntcFanController.setRevisions(('2013-07-05 06:00',))
if mibBuilder.loadTexts: ntcFanController.setLastUpdated('201307050600Z')
if mibBuilder.loadTexts: ntcFanController.setOrganization('Newtec Cy')
ntcFanCObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 3500, 1))
if mibBuilder.loadTexts: ntcFanCObjects.setStatus('current')
ntcFanCConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 3500, 2))
if mibBuilder.loadTexts: ntcFanCConformance.setStatus('current')
ntcFanAlarm = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 3500, 1, 1))
if mibBuilder.loadTexts: ntcFanAlarm.setStatus('current')
ntcFanCConfCompliance = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 3500, 2, 1))
if mibBuilder.loadTexts: ntcFanCConfCompliance.setStatus('current')
ntcFanCConfGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 3500, 2, 2))
if mibBuilder.loadTexts: ntcFanCConfGroup.setStatus('current')
ntcFanCAlmFanFailure = MibScalar((1, 3, 6, 1, 4, 1, 5835, 5, 2, 3500, 1, 1, 1), NtcAlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcFanCAlmFanFailure.setStatus('current')
ntcFanCConfGrpV1Standard = ObjectGroup((1, 3, 6, 1, 4, 1, 5835, 5, 2, 3500, 2, 2, 1)).setObjects(("NEWTEC-FANCONTROLLER-MIB", "ntcFanCAlmFanFailure"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntcFanCConfGrpV1Standard = ntcFanCConfGrpV1Standard.setStatus('current')
ntcFanCConfCompV1Standard = ModuleCompliance((1, 3, 6, 1, 4, 1, 5835, 5, 2, 3500, 2, 1, 1)).setObjects(("NEWTEC-FANCONTROLLER-MIB", "ntcFanCConfGrpV1Standard"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntcFanCConfCompV1Standard = ntcFanCConfCompV1Standard.setStatus('current')
mibBuilder.exportSymbols("NEWTEC-FANCONTROLLER-MIB", ntcFanCObjects=ntcFanCObjects, PYSNMP_MODULE_ID=ntcFanController, ntcFanController=ntcFanController, ntcFanCConfGrpV1Standard=ntcFanCConfGrpV1Standard, ntcFanCConformance=ntcFanCConformance, ntcFanCConfCompliance=ntcFanCConfCompliance, ntcFanCConfCompV1Standard=ntcFanCConfCompV1Standard, ntcFanAlarm=ntcFanAlarm, ntcFanCAlmFanFailure=ntcFanCAlmFanFailure, ntcFanCConfGroup=ntcFanCConfGroup)
