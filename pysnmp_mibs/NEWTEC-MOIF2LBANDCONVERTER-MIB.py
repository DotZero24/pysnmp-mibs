#
# PySNMP MIB module NEWTEC-MOIF2LBANDCONVERTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/newtec/NEWTEC-MOIF2LBANDCONVERTER-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:30 2025
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
ntcMoIF2LbandConverter = ModuleIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 8600))
ntcMoIF2LbandConverter.setRevisions(('2015-02-19 09:00',))
if mibBuilder.loadTexts: ntcMoIF2LbandConverter.setLastUpdated('201502190900Z')
if mibBuilder.loadTexts: ntcMoIF2LbandConverter.setOrganization('Newtec Cy')
ntcMoIF2LConvObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 8600, 1))
if mibBuilder.loadTexts: ntcMoIF2LConvObjects.setStatus('current')
ntcMoIF2LConvConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 8600, 2))
if mibBuilder.loadTexts: ntcMoIF2LConvConformance.setStatus('current')
ntcMoIF2LConvAlarm = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 8600, 1, 1))
if mibBuilder.loadTexts: ntcMoIF2LConvAlarm.setStatus('current')
ntcMoIF2LConvConfCompliance = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 8600, 2, 1))
if mibBuilder.loadTexts: ntcMoIF2LConvConfCompliance.setStatus('current')
ntcMoIF2LConvConfGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 8600, 2, 2))
if mibBuilder.loadTexts: ntcMoIF2LConvConfGroup.setStatus('current')
ntcMoIF2LConvHardware = MibScalar((1, 3, 6, 1, 4, 1, 5835, 5, 2, 8600, 1, 1, 1), NtcAlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcMoIF2LConvHardware.setStatus('current')
ntcMoIF2LConvCommunication = MibScalar((1, 3, 6, 1, 4, 1, 5835, 5, 2, 8600, 1, 1, 2), NtcAlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcMoIF2LConvCommunication.setStatus('current')
ntcMoIF2LConvConfGrpV1Standard = ObjectGroup((1, 3, 6, 1, 4, 1, 5835, 5, 2, 8600, 2, 2, 1)).setObjects(("NEWTEC-MOIF2LBANDCONVERTER-MIB", "ntcMoIF2LConvHardware"), ("NEWTEC-MOIF2LBANDCONVERTER-MIB", "ntcMoIF2LConvCommunication"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntcMoIF2LConvConfGrpV1Standard = ntcMoIF2LConvConfGrpV1Standard.setStatus('current')
ntcMoIF2LConvConfCompV1Standard = ModuleCompliance((1, 3, 6, 1, 4, 1, 5835, 5, 2, 8600, 2, 1, 1)).setObjects(("NEWTEC-MOIF2LBANDCONVERTER-MIB", "ntcMoIF2LConvConfGrpV1Standard"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntcMoIF2LConvConfCompV1Standard = ntcMoIF2LConvConfCompV1Standard.setStatus('current')
mibBuilder.exportSymbols("NEWTEC-MOIF2LBANDCONVERTER-MIB", PYSNMP_MODULE_ID=ntcMoIF2LbandConverter, ntcMoIF2LConvAlarm=ntcMoIF2LConvAlarm, ntcMoIF2LConvCommunication=ntcMoIF2LConvCommunication, ntcMoIF2LConvConformance=ntcMoIF2LConvConformance, ntcMoIF2LConvConfCompliance=ntcMoIF2LConvConfCompliance, ntcMoIF2LConvConfGroup=ntcMoIF2LConvConfGroup, ntcMoIF2LbandConverter=ntcMoIF2LbandConverter, ntcMoIF2LConvConfCompV1Standard=ntcMoIF2LConvConfCompV1Standard, ntcMoIF2LConvHardware=ntcMoIF2LConvHardware, ntcMoIF2LConvConfGrpV1Standard=ntcMoIF2LConvConfGrpV1Standard, ntcMoIF2LConvObjects=ntcMoIF2LConvObjects)
