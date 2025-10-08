#
# PySNMP MIB module NEWTEC-ALARMS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/newtec/NEWTEC-ALARMS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:33 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ntcFunction, = mibBuilder.importSymbols("NEWTEC-MAIN-MIB", "ntcFunction")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ntcAlarms = ModuleIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 5600))
ntcAlarms.setRevisions(('2013-09-20 10:00', '2013-09-20 08:00',))
if mibBuilder.loadTexts: ntcAlarms.setLastUpdated('201309201000Z')
if mibBuilder.loadTexts: ntcAlarms.setOrganization('Newtec Cy')
ntcAlmsObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 5600, 1))
if mibBuilder.loadTexts: ntcAlmsObjects.setStatus('current')
ntcAlmsConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 5600, 2))
if mibBuilder.loadTexts: ntcAlmsConformance.setStatus('current')
ntcAlmsConfCompliance = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 5600, 2, 1))
if mibBuilder.loadTexts: ntcAlmsConfCompliance.setStatus('current')
ntcAlmsConfGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 5600, 2, 2))
if mibBuilder.loadTexts: ntcAlmsConfGroup.setStatus('current')
ntcAlmsConfigTable = MibTable((1, 3, 6, 1, 4, 1, 5835, 5, 2, 5600, 1, 1), )
if mibBuilder.loadTexts: ntcAlmsConfigTable.setStatus('current')
ntcAlmsConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5835, 5, 2, 5600, 1, 1, 1), ).setIndexNames((0, "NEWTEC-ALARMS-MIB", "ntcAlmsConfigName"))
if mibBuilder.loadTexts: ntcAlmsConfigEntry.setStatus('current')
ntcAlmsConfigName = MibTableColumn((1, 3, 6, 1, 4, 1, 5835, 5, 2, 5600, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30)))
if mibBuilder.loadTexts: ntcAlmsConfigName.setStatus('current')
ntcAlmsConfigMask = MibTableColumn((1, 3, 6, 1, 4, 1, 5835, 5, 2, 5600, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1))).clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntcAlmsConfigMask.setStatus('current')
ntcAlmsConfigGeneralInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 5835, 5, 2, 5600, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1))).clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntcAlmsConfigGeneralInterface.setStatus('current')
ntcAlmsConfigGeneralDevice = MibTableColumn((1, 3, 6, 1, 4, 1, 5835, 5, 2, 5600, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1))).clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntcAlmsConfigGeneralDevice.setStatus('current')
ntcAlmsConfGrpV1Standard = ObjectGroup((1, 3, 6, 1, 4, 1, 5835, 5, 2, 5600, 2, 2, 1)).setObjects(("NEWTEC-ALARMS-MIB", "ntcAlmsConfigMask"), ("NEWTEC-ALARMS-MIB", "ntcAlmsConfigGeneralInterface"), ("NEWTEC-ALARMS-MIB", "ntcAlmsConfigGeneralDevice"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntcAlmsConfGrpV1Standard = ntcAlmsConfGrpV1Standard.setStatus('current')
ntcAlmsConfCompV1Standard = ModuleCompliance((1, 3, 6, 1, 4, 1, 5835, 5, 2, 5600, 2, 1, 1)).setObjects(("NEWTEC-ALARMS-MIB", "ntcAlmsConfGrpV1Standard"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntcAlmsConfCompV1Standard = ntcAlmsConfCompV1Standard.setStatus('current')
mibBuilder.exportSymbols("NEWTEC-ALARMS-MIB", ntcAlmsConfigTable=ntcAlmsConfigTable, ntcAlmsConfigMask=ntcAlmsConfigMask, ntcAlmsConfigGeneralDevice=ntcAlmsConfigGeneralDevice, ntcAlmsConfGrpV1Standard=ntcAlmsConfGrpV1Standard, ntcAlmsConfigEntry=ntcAlmsConfigEntry, ntcAlmsConfigName=ntcAlmsConfigName, ntcAlmsObjects=ntcAlmsObjects, ntcAlmsConformance=ntcAlmsConformance, PYSNMP_MODULE_ID=ntcAlarms, ntcAlmsConfCompV1Standard=ntcAlmsConfCompV1Standard, ntcAlarms=ntcAlarms, ntcAlmsConfCompliance=ntcAlmsConfCompliance, ntcAlmsConfigGeneralInterface=ntcAlmsConfigGeneralInterface, ntcAlmsConfGroup=ntcAlmsConfGroup)
