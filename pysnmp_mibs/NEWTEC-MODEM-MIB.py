#
# PySNMP MIB module NEWTEC-MODEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/newtec/NEWTEC-MODEM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:04:45 2025
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
mibBuilder.exportSymbols("NEWTEC-MODEM-MIB", ntcModemConfGrpV1Standard=ntcModemConfGrpV1Standard, ntcModemConfCompliance=ntcModemConfCompliance, ntcModemConformance=ntcModemConformance, ntcModem=ntcModem, ntcModemConfGroup=ntcModemConfGroup, ntcModemTxCtrlDemodLockAlarm=ntcModemTxCtrlDemodLockAlarm, PYSNMP_MODULE_ID=ntcModem, ntcModemObjects=ntcModemObjects, ntcModemConfCompV1Standard=ntcModemConfCompV1Standard)
