#
# PySNMP MIB module NEWTEC-ALARMS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/newtec/NEWTEC-ALARMS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:04:48 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ntcFunction, = mibBuilder.importSymbols("NEWTEC-MAIN-MIB", "ntcFunction")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("NEWTEC-ALARMS-MIB", ntcAlmsConfigMask=ntcAlmsConfigMask, PYSNMP_MODULE_ID=ntcAlarms, ntcAlmsConfigGeneralDevice=ntcAlmsConfigGeneralDevice, ntcAlmsConfigGeneralInterface=ntcAlmsConfigGeneralInterface, ntcAlmsConfGroup=ntcAlmsConfGroup, ntcAlmsConfCompliance=ntcAlmsConfCompliance, ntcAlmsConfCompV1Standard=ntcAlmsConfCompV1Standard, ntcAlmsConfigName=ntcAlmsConfigName, ntcAlmsObjects=ntcAlmsObjects, ntcAlarms=ntcAlarms, ntcAlmsConfGrpV1Standard=ntcAlmsConfGrpV1Standard, ntcAlmsConfigTable=ntcAlmsConfigTable, ntcAlmsConfigEntry=ntcAlmsConfigEntry, ntcAlmsConformance=ntcAlmsConformance)
