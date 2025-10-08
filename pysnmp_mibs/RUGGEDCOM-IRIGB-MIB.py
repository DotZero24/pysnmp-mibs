#
# PySNMP MIB module RUGGEDCOM-IRIGB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/siemens/RUGGEDCOM-IRIGB-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:08:00 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ruggedcomTraps, ruggedcomMgmt = mibBuilder.importSymbols("RUGGEDCOM-MIB", "ruggedcomTraps", "ruggedcomMgmt")
RcTimeSyncStatus, = mibBuilder.importSymbols("RUGGEDCOM-TIMECONFIG-MIB", "RcTimeSyncStatus")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rcIrigb = ModuleIdentity((1, 3, 6, 1, 4, 1, 15004, 4, 10))
rcIrigb.setRevisions(('2015-10-30 17:00', '2014-12-01 17:00',))
if mibBuilder.loadTexts: rcIrigb.setLastUpdated('201510301700Z')
if mibBuilder.loadTexts: rcIrigb.setOrganization('Siemens Canada Limited')
class RcTimeStamp(TextualConvention, OctetString):
    status = 'current'
    displayHint = '4d.4d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

rcIrigbBase = MibIdentifier((1, 3, 6, 1, 4, 1, 15004, 4, 10, 1))
rcIrigbConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 15004, 4, 10, 2))
rcIrigbGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 15004, 4, 10, 2, 2))
rcIrigbStatus = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 10, 1, 1), RcTimeSyncStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcIrigbStatus.setStatus('current')
rcIrigbAMOutput = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 4))).clone(namedValues=NamedValues(("off", 1), ("am", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcIrigbAMOutput.setStatus('current')
rcIrigbTimeCode = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("bxx0", 1), ("bxx1", 2), ("bxx2", 3), ("bxx3", 4), ("bxx4", 5), ("bxx5", 6), ("bxx6", 7), ("bxx7", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcIrigbTimeCode.setStatus('current')
rcIrigbExt = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 10, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("off", 1), ("ieee1344", 2), ("c37-118-2005", 3), ("c37-118-2011", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcIrigbExt.setStatus('current')
rcIrigbInput = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 10, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("off", 1), ("pwm", 2), ("pps", 3), ("am", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcIrigbInput.setStatus('current')
rcIrigbLockInt = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 10, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 120))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcIrigbLockInt.setStatus('current')
rcIrigbCableComp = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 10, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 50000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcIrigbCableComp.setStatus('current')
rcIrigbOFM = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 10, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483647, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcIrigbOFM.setStatus('current')
rcIrigbFreqAdj = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 10, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483647, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcIrigbFreqAdj.setStatus('current')
rcIrigbOutputPWM1 = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 10, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 5))).clone(namedValues=NamedValues(("off", 1), ("pwm", 2), ("pps", 3), ("ppx", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcIrigbOutputPWM1.setStatus('current')
rcIrigbPulseInterval1 = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 10, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 86400))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcIrigbPulseInterval1.setStatus('current')
rcIrigbPulseWidth1 = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 10, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 200))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcIrigbPulseWidth1.setStatus('current')
rcIrigbStartTime1 = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 10, 1, 13), RcTimeStamp()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcIrigbStartTime1.setStatus('current')
rcIrigbOutputPWM2 = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 10, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 5))).clone(namedValues=NamedValues(("off", 1), ("pwm", 2), ("pps", 3), ("ppx", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcIrigbOutputPWM2.setStatus('current')
rcIrigbPulseInterval2 = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 10, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 86400))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcIrigbPulseInterval2.setStatus('current')
rcIrigbPulseWidth2 = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 10, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 200))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcIrigbPulseWidth2.setStatus('current')
rcIrigbStartTime2 = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 10, 1, 17), RcTimeStamp()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcIrigbStartTime2.setStatus('current')
rcIrigbStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 15004, 5, 35)).setObjects(("RUGGEDCOM-IRIGB-MIB", "rcIrigbStatus"))
if mibBuilder.loadTexts: rcIrigbStatusChange.setStatus('current')
rcIrigbBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 15004, 4, 10, 2, 2, 1)).setObjects(("RUGGEDCOM-IRIGB-MIB", "rcIrigbStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rcIrigbBaseGroup = rcIrigbBaseGroup.setStatus('current')
rcIrigbNotifyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 15004, 4, 10, 2, 2, 2)).setObjects(("RUGGEDCOM-IRIGB-MIB", "rcIrigbStatusChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rcIrigbNotifyGroup = rcIrigbNotifyGroup.setStatus('current')
rcIrigbCommonGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 15004, 4, 10, 2, 2, 3)).setObjects(("RUGGEDCOM-IRIGB-MIB", "rcIrigbStatus"), ("RUGGEDCOM-IRIGB-MIB", "rcIrigbTimeCode"), ("RUGGEDCOM-IRIGB-MIB", "rcIrigbExt"), ("RUGGEDCOM-IRIGB-MIB", "rcIrigbLockInt"), ("RUGGEDCOM-IRIGB-MIB", "rcIrigbCableComp"), ("RUGGEDCOM-IRIGB-MIB", "rcIrigbOFM"), ("RUGGEDCOM-IRIGB-MIB", "rcIrigbFreqAdj"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rcIrigbCommonGroup = rcIrigbCommonGroup.setStatus('current')
rcIrigbAMOutGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 15004, 4, 10, 2, 2, 4)).setObjects(("RUGGEDCOM-IRIGB-MIB", "rcIrigbAMOutput"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rcIrigbAMOutGroup = rcIrigbAMOutGroup.setStatus('current')
rcIrigbInputGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 15004, 4, 10, 2, 2, 5)).setObjects(("RUGGEDCOM-IRIGB-MIB", "rcIrigbInput"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rcIrigbInputGroup = rcIrigbInputGroup.setStatus('current')
rcIrigbTTLOutput01Group = ObjectGroup((1, 3, 6, 1, 4, 1, 15004, 4, 10, 2, 2, 6)).setObjects(("RUGGEDCOM-IRIGB-MIB", "rcIrigbOutputPWM1"), ("RUGGEDCOM-IRIGB-MIB", "rcIrigbPulseInterval1"), ("RUGGEDCOM-IRIGB-MIB", "rcIrigbPulseWidth1"), ("RUGGEDCOM-IRIGB-MIB", "rcIrigbStartTime1"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rcIrigbTTLOutput01Group = rcIrigbTTLOutput01Group.setStatus('current')
rcIrigbTTLOutput02Group = ObjectGroup((1, 3, 6, 1, 4, 1, 15004, 4, 10, 2, 2, 7)).setObjects(("RUGGEDCOM-IRIGB-MIB", "rcIrigbOutputPWM2"), ("RUGGEDCOM-IRIGB-MIB", "rcIrigbPulseInterval2"), ("RUGGEDCOM-IRIGB-MIB", "rcIrigbPulseWidth2"), ("RUGGEDCOM-IRIGB-MIB", "rcIrigbStartTime2"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rcIrigbTTLOutput02Group = rcIrigbTTLOutput02Group.setStatus('current')
mibBuilder.exportSymbols("RUGGEDCOM-IRIGB-MIB", rcIrigbPulseWidth2=rcIrigbPulseWidth2, rcIrigbStartTime2=rcIrigbStartTime2, rcIrigbGroups=rcIrigbGroups, rcIrigbConformance=rcIrigbConformance, rcIrigbExt=rcIrigbExt, rcIrigbStartTime1=rcIrigbStartTime1, rcIrigbOutputPWM1=rcIrigbOutputPWM1, rcIrigbTTLOutput02Group=rcIrigbTTLOutput02Group, rcIrigbTimeCode=rcIrigbTimeCode, rcIrigbCommonGroup=rcIrigbCommonGroup, rcIrigbPulseInterval2=rcIrigbPulseInterval2, rcIrigbBase=rcIrigbBase, rcIrigbInput=rcIrigbInput, rcIrigbOFM=rcIrigbOFM, rcIrigbPulseWidth1=rcIrigbPulseWidth1, rcIrigbNotifyGroup=rcIrigbNotifyGroup, rcIrigbAMOutput=rcIrigbAMOutput, rcIrigbAMOutGroup=rcIrigbAMOutGroup, rcIrigbStatus=rcIrigbStatus, rcIrigbOutputPWM2=rcIrigbOutputPWM2, rcIrigbPulseInterval1=rcIrigbPulseInterval1, rcIrigbLockInt=rcIrigbLockInt, RcTimeStamp=RcTimeStamp, rcIrigb=rcIrigb, rcIrigbBaseGroup=rcIrigbBaseGroup, rcIrigbStatusChange=rcIrigbStatusChange, rcIrigbInputGroup=rcIrigbInputGroup, rcIrigbCableComp=rcIrigbCableComp, PYSNMP_MODULE_ID=rcIrigb, rcIrigbFreqAdj=rcIrigbFreqAdj, rcIrigbTTLOutput01Group=rcIrigbTTLOutput01Group)
