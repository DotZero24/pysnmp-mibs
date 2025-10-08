#
# PySNMP MIB module NEWTEC-FANCONTROLLER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/newtec/NEWTEC-FANCONTROLLER-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:04:44 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ntcFunction, = mibBuilder.importSymbols("NEWTEC-MAIN-MIB", "ntcFunction")
NtcAlarmState, = mibBuilder.importSymbols("NEWTEC-TC-MIB", "NtcAlarmState")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("NEWTEC-FANCONTROLLER-MIB", ntcFanController=ntcFanController, ntcFanCObjects=ntcFanCObjects, ntcFanCConfGrpV1Standard=ntcFanCConfGrpV1Standard, ntcFanAlarm=ntcFanAlarm, PYSNMP_MODULE_ID=ntcFanController, ntcFanCConfGroup=ntcFanCConfGroup, ntcFanCConformance=ntcFanCConformance, ntcFanCConfCompliance=ntcFanCConfCompliance, ntcFanCAlmFanFailure=ntcFanCAlmFanFailure, ntcFanCConfCompV1Standard=ntcFanCConfCompV1Standard)
