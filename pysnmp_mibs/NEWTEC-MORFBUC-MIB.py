#
# PySNMP MIB module NEWTEC-MORFBUC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/newtec/NEWTEC-MORFBUC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:04:37 2025
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
mibBuilder.exportSymbols("NEWTEC-MORFBUC-MIB", ntcMoRfBucObjects=ntcMoRfBucObjects, ntcMoRfBucAlarm=ntcMoRfBucAlarm, ntcMoRfBucConfGroup=ntcMoRfBucConfGroup, ntcMoRfBlockUpConv=ntcMoRfBlockUpConv, ntcMoRfBucHardware=ntcMoRfBucHardware, ntcMoRfBucConfCompV1Standard=ntcMoRfBucConfCompV1Standard, ntcMoRfBucConformance=ntcMoRfBucConformance, ntcMoRfBucCommunication=ntcMoRfBucCommunication, ntcMoRfBucConfCompliance=ntcMoRfBucConfCompliance, PYSNMP_MODULE_ID=ntcMoRfBlockUpConv, ntcMoRfBucConfGrpV1Standard=ntcMoRfBucConfGrpV1Standard)
