#
# PySNMP MIB module NEWTEC-MODEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/newtec/NEWTEC-MODEM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:32 2025
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
ntcModem = ModuleIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 6500))
ntcModem.setRevisions(('2014-02-03 12:00',))
if mibBuilder.loadTexts: ntcModem.setLastUpdated('201402031200Z')
if mibBuilder.loadTexts: ntcModem.setOrganization('Newtec Cy')
ntcModemObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 6500, 1))
if mibBuilder.loadTexts: ntcModemObjects.setStatus('current')
ntcModemConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 6500, 2))
if mibBuilder.loadTexts: ntcModemConformance.setStatus('current')
ntcModemConfCompliance = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 6500, 2, 1))
if mibBuilder.loadTexts: ntcModemConfCompliance.setStatus('current')
ntcModemConfGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 6500, 2, 2))
if mibBuilder.loadTexts: ntcModemConfGroup.setStatus('current')
ntcModemTxCtrlDemodLockAlarm = MibScalar((1, 3, 6, 1, 4, 1, 5835, 5, 2, 6500, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disableTransmit", 0), ("noImpact", 1))).clone('noImpact')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntcModemTxCtrlDemodLockAlarm.setStatus('current')
ntcModemConfGrpV1Standard = ObjectGroup((1, 3, 6, 1, 4, 1, 5835, 5, 2, 6500, 2, 2, 1)).setObjects(("NEWTEC-MODEM-MIB", "ntcModemTxCtrlDemodLockAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntcModemConfGrpV1Standard = ntcModemConfGrpV1Standard.setStatus('current')
ntcModemConfCompV1Standard = ModuleCompliance((1, 3, 6, 1, 4, 1, 5835, 5, 2, 6500, 2, 1, 1)).setObjects(("NEWTEC-MODEM-MIB", "ntcModemConfGrpV1Standard"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntcModemConfCompV1Standard = ntcModemConfCompV1Standard.setStatus('current')
mibBuilder.exportSymbols("NEWTEC-MODEM-MIB", ntcModemConfCompliance=ntcModemConfCompliance, ntcModemTxCtrlDemodLockAlarm=ntcModemTxCtrlDemodLockAlarm, ntcModemConfGroup=ntcModemConfGroup, ntcModemConfCompV1Standard=ntcModemConfCompV1Standard, ntcModemObjects=ntcModemObjects, ntcModem=ntcModem, ntcModemConfGrpV1Standard=ntcModemConfGrpV1Standard, PYSNMP_MODULE_ID=ntcModem, ntcModemConformance=ntcModemConformance)
