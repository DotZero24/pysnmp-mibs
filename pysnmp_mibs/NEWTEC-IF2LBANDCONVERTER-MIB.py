#
# PySNMP MIB module NEWTEC-IF2LBANDCONVERTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/newtec/NEWTEC-IF2LBANDCONVERTER-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:29 2025
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
ntcIF2LbandConverter = ModuleIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 4600))
ntcIF2LbandConverter.setRevisions(('2012-06-28 12:00',))
if mibBuilder.loadTexts: ntcIF2LbandConverter.setLastUpdated('201206281200Z')
if mibBuilder.loadTexts: ntcIF2LbandConverter.setOrganization('Newtec Cy')
ntcIF2LConvObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 4600, 1))
if mibBuilder.loadTexts: ntcIF2LConvObjects.setStatus('current')
ntcIF2LConvConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 4600, 2))
if mibBuilder.loadTexts: ntcIF2LConvConformance.setStatus('current')
ntcIF2LConvAlarm = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 4600, 1, 1))
if mibBuilder.loadTexts: ntcIF2LConvAlarm.setStatus('current')
ntcIF2LConvConfCompliance = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 4600, 2, 1))
if mibBuilder.loadTexts: ntcIF2LConvConfCompliance.setStatus('current')
ntcIF2LConvConfGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 4600, 2, 2))
if mibBuilder.loadTexts: ntcIF2LConvConfGroup.setStatus('current')
ntcIF2LConvHardware = MibScalar((1, 3, 6, 1, 4, 1, 5835, 5, 2, 4600, 1, 1, 1), NtcAlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcIF2LConvHardware.setStatus('current')
ntcIF2LConvCommunication = MibScalar((1, 3, 6, 1, 4, 1, 5835, 5, 2, 4600, 1, 1, 2), NtcAlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcIF2LConvCommunication.setStatus('current')
ntcIF2LConvConfGrpV1Standard = ObjectGroup((1, 3, 6, 1, 4, 1, 5835, 5, 2, 4600, 2, 2, 1)).setObjects(("NEWTEC-IF2LBANDCONVERTER-MIB", "ntcIF2LConvHardware"), ("NEWTEC-IF2LBANDCONVERTER-MIB", "ntcIF2LConvCommunication"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntcIF2LConvConfGrpV1Standard = ntcIF2LConvConfGrpV1Standard.setStatus('current')
ntcIF2LConvConfCompV1Standard = ModuleCompliance((1, 3, 6, 1, 4, 1, 5835, 5, 2, 4600, 2, 1, 1)).setObjects(("NEWTEC-IF2LBANDCONVERTER-MIB", "ntcIF2LConvConfGrpV1Standard"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntcIF2LConvConfCompV1Standard = ntcIF2LConvConfCompV1Standard.setStatus('current')
mibBuilder.exportSymbols("NEWTEC-IF2LBANDCONVERTER-MIB", ntcIF2LConvCommunication=ntcIF2LConvCommunication, ntcIF2LConvConfCompV1Standard=ntcIF2LConvConfCompV1Standard, ntcIF2LConvHardware=ntcIF2LConvHardware, ntcIF2LConvConformance=ntcIF2LConvConformance, ntcIF2LbandConverter=ntcIF2LbandConverter, PYSNMP_MODULE_ID=ntcIF2LbandConverter, ntcIF2LConvAlarm=ntcIF2LConvAlarm, ntcIF2LConvConfGrpV1Standard=ntcIF2LConvConfGrpV1Standard, ntcIF2LConvConfCompliance=ntcIF2LConvConfCompliance, ntcIF2LConvObjects=ntcIF2LConvObjects, ntcIF2LConvConfGroup=ntcIF2LConvConfGroup)
