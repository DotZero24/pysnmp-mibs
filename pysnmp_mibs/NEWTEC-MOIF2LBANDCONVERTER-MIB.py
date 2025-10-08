#
# PySNMP MIB module NEWTEC-MOIF2LBANDCONVERTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/newtec/NEWTEC-MOIF2LBANDCONVERTER-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:04:42 2025
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
mibBuilder.exportSymbols("NEWTEC-MOIF2LBANDCONVERTER-MIB", ntcMoIF2LConvConformance=ntcMoIF2LConvConformance, ntcMoIF2LConvConfCompliance=ntcMoIF2LConvConfCompliance, ntcMoIF2LConvHardware=ntcMoIF2LConvHardware, ntcMoIF2LConvObjects=ntcMoIF2LConvObjects, ntcMoIF2LConvCommunication=ntcMoIF2LConvCommunication, ntcMoIF2LConvConfCompV1Standard=ntcMoIF2LConvConfCompV1Standard, ntcMoIF2LbandConverter=ntcMoIF2LbandConverter, ntcMoIF2LConvAlarm=ntcMoIF2LConvAlarm, PYSNMP_MODULE_ID=ntcMoIF2LbandConverter, ntcMoIF2LConvConfGrpV1Standard=ntcMoIF2LConvConfGrpV1Standard, ntcMoIF2LConvConfGroup=ntcMoIF2LConvConfGroup)
