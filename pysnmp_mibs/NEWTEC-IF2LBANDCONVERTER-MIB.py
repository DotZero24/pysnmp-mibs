#
# PySNMP MIB module NEWTEC-IF2LBANDCONVERTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/newtec/NEWTEC-IF2LBANDCONVERTER-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:04:41 2025
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
mibBuilder.exportSymbols("NEWTEC-IF2LBANDCONVERTER-MIB", ntcIF2LConvConfCompV1Standard=ntcIF2LConvConfCompV1Standard, ntcIF2LbandConverter=ntcIF2LbandConverter, ntcIF2LConvConfCompliance=ntcIF2LConvConfCompliance, ntcIF2LConvConformance=ntcIF2LConvConformance, ntcIF2LConvObjects=ntcIF2LConvObjects, ntcIF2LConvConfGroup=ntcIF2LConvConfGroup, ntcIF2LConvCommunication=ntcIF2LConvCommunication, ntcIF2LConvAlarm=ntcIF2LConvAlarm, ntcIF2LConvHardware=ntcIF2LConvHardware, PYSNMP_MODULE_ID=ntcIF2LbandConverter, ntcIF2LConvConfGrpV1Standard=ntcIF2LConvConfGrpV1Standard)
