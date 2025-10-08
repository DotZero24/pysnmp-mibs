#
# PySNMP MIB module NEWTEC-MORFBUC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/newtec/NEWTEC-MORFBUC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:27 2025
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
ntcMoRfBlockUpConv = ModuleIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 10000))
ntcMoRfBlockUpConv.setRevisions(('2016-05-17 09:00',))
if mibBuilder.loadTexts: ntcMoRfBlockUpConv.setLastUpdated('201605170900Z')
if mibBuilder.loadTexts: ntcMoRfBlockUpConv.setOrganization('Newtec Cy')
ntcMoRfBucObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 10000, 1))
if mibBuilder.loadTexts: ntcMoRfBucObjects.setStatus('current')
ntcMoRfBucConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 10000, 2))
if mibBuilder.loadTexts: ntcMoRfBucConformance.setStatus('current')
ntcMoRfBucAlarm = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 10000, 1, 1))
if mibBuilder.loadTexts: ntcMoRfBucAlarm.setStatus('current')
ntcMoRfBucConfCompliance = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 10000, 2, 1))
if mibBuilder.loadTexts: ntcMoRfBucConfCompliance.setStatus('current')
ntcMoRfBucConfGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 10000, 2, 2))
if mibBuilder.loadTexts: ntcMoRfBucConfGroup.setStatus('current')
ntcMoRfBucHardware = MibScalar((1, 3, 6, 1, 4, 1, 5835, 5, 2, 10000, 1, 1, 1), NtcAlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcMoRfBucHardware.setStatus('current')
ntcMoRfBucCommunication = MibScalar((1, 3, 6, 1, 4, 1, 5835, 5, 2, 10000, 1, 1, 2), NtcAlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcMoRfBucCommunication.setStatus('current')
ntcMoRfBucConfGrpV1Standard = ObjectGroup((1, 3, 6, 1, 4, 1, 5835, 5, 2, 10000, 2, 2, 1)).setObjects(("NEWTEC-MORFBUC-MIB", "ntcMoRfBucHardware"), ("NEWTEC-MORFBUC-MIB", "ntcMoRfBucCommunication"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntcMoRfBucConfGrpV1Standard = ntcMoRfBucConfGrpV1Standard.setStatus('current')
ntcMoRfBucConfCompV1Standard = ModuleCompliance((1, 3, 6, 1, 4, 1, 5835, 5, 2, 10000, 2, 1, 1)).setObjects(("NEWTEC-MORFBUC-MIB", "ntcMoRfBucConfGrpV1Standard"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntcMoRfBucConfCompV1Standard = ntcMoRfBucConfCompV1Standard.setStatus('current')
mibBuilder.exportSymbols("NEWTEC-MORFBUC-MIB", PYSNMP_MODULE_ID=ntcMoRfBlockUpConv, ntcMoRfBucConfGrpV1Standard=ntcMoRfBucConfGrpV1Standard, ntcMoRfBucObjects=ntcMoRfBucObjects, ntcMoRfBucAlarm=ntcMoRfBucAlarm, ntcMoRfBlockUpConv=ntcMoRfBlockUpConv, ntcMoRfBucConfCompV1Standard=ntcMoRfBucConfCompV1Standard, ntcMoRfBucHardware=ntcMoRfBucHardware, ntcMoRfBucConfCompliance=ntcMoRfBucConfCompliance, ntcMoRfBucCommunication=ntcMoRfBucCommunication, ntcMoRfBucConfGroup=ntcMoRfBucConfGroup, ntcMoRfBucConformance=ntcMoRfBucConformance)
