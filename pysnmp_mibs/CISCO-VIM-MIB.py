#
# PySNMP MIB module CISCO-VIM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-VIM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:27:06 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention")
ciscoVimMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 855))
ciscoVimMIB.setRevisions(('2018-07-16 00:00',))
if mibBuilder.loadTexts: ciscoVimMIB.setLastUpdated('201807160000Z')
if mibBuilder.loadTexts: ciscoVimMIB.setOrganization('Cisco Systems, Inc.')
class CFaultSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("emergency", 1), ("critical", 2), ("major", 3), ("alert", 4), ("informational", 5))

class CFaultCode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("resourceUsage", 2), ("resourceThreshold", 3), ("serviceFailure", 4), ("hardwareFailure", 5), ("networkConnectivity", 6))

ciscoVimMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 855, 0))
ciscoVimMIBFaults = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 855, 1))
ciscoVimMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 855, 2))
cvimPodId = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 855, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 100)))
if mibBuilder.loadTexts: cvimPodId.setStatus('current')
cvimFaultCreationTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 855, 1, 2), DateAndTime())
if mibBuilder.loadTexts: cvimFaultCreationTime.setStatus('current')
cvimNodeId = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 855, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512)))
if mibBuilder.loadTexts: cvimNodeId.setStatus('current')
cvimFaultSource = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 855, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 100)))
if mibBuilder.loadTexts: cvimFaultSource.setStatus('current')
cvimFaultSeverity = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 855, 1, 5), CFaultSeverity())
if mibBuilder.loadTexts: cvimFaultSeverity.setStatus('current')
cvimFaultCode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 855, 1, 6), CFaultCode())
if mibBuilder.loadTexts: cvimFaultCode.setStatus('current')
cvimFaultDescription = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 855, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 2048)))
if mibBuilder.loadTexts: cvimFaultDescription.setStatus('current')
cvimFaultActiveNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 855, 0, 1)).setObjects(("CISCO-VIM-MIB", "cvimPodId"), ("CISCO-VIM-MIB", "cvimFaultCreationTime"), ("CISCO-VIM-MIB", "cvimNodeId"), ("CISCO-VIM-MIB", "cvimFaultSource"), ("CISCO-VIM-MIB", "cvimFaultSeverity"), ("CISCO-VIM-MIB", "cvimFaultCode"), ("CISCO-VIM-MIB", "cvimFaultDescription"))
if mibBuilder.loadTexts: cvimFaultActiveNotif.setStatus('current')
cvimFaultClearNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 855, 0, 2)).setObjects(("CISCO-VIM-MIB", "cvimPodId"), ("CISCO-VIM-MIB", "cvimFaultCreationTime"), ("CISCO-VIM-MIB", "cvimNodeId"), ("CISCO-VIM-MIB", "cvimFaultSource"), ("CISCO-VIM-MIB", "cvimFaultSeverity"), ("CISCO-VIM-MIB", "cvimFaultCode"), ("CISCO-VIM-MIB", "cvimFaultDescription"))
if mibBuilder.loadTexts: cvimFaultClearNotif.setStatus('current')
ciscoVimMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 855, 2, 1))
ciscoVimMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 855, 2, 2))
cvimMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 855, 2, 1, 1)).setObjects(("CISCO-VIM-MIB", "cvimMIBFaultGroup"), ("CISCO-VIM-MIB", "cvimMIBNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvimMIBCompliance = cvimMIBCompliance.setStatus('current')
cvimMIBFaultGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 855, 2, 2, 1)).setObjects(("CISCO-VIM-MIB", "cvimPodId"), ("CISCO-VIM-MIB", "cvimFaultSource"), ("CISCO-VIM-MIB", "cvimFaultCreationTime"), ("CISCO-VIM-MIB", "cvimFaultSeverity"), ("CISCO-VIM-MIB", "cvimFaultCode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvimMIBFaultGroup = cvimMIBFaultGroup.setStatus('current')
cvimMIBNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 855, 2, 2, 2)).setObjects(("CISCO-VIM-MIB", "cvimFaultActiveNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvimMIBNotificationGroup = cvimMIBNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VIM-MIB", cvimFaultDescription=cvimFaultDescription, cvimPodId=cvimPodId, CFaultSeverity=CFaultSeverity, cvimFaultSeverity=cvimFaultSeverity, cvimFaultCode=cvimFaultCode, cvimMIBCompliance=cvimMIBCompliance, cvimFaultCreationTime=cvimFaultCreationTime, ciscoVimMIBCompliances=ciscoVimMIBCompliances, cvimMIBFaultGroup=cvimMIBFaultGroup, cvimFaultClearNotif=cvimFaultClearNotif, cvimFaultSource=cvimFaultSource, CFaultCode=CFaultCode, ciscoVimMIBNotifs=ciscoVimMIBNotifs, ciscoVimMIBFaults=ciscoVimMIBFaults, PYSNMP_MODULE_ID=ciscoVimMIB, cvimFaultActiveNotif=cvimFaultActiveNotif, ciscoVimMIB=ciscoVimMIB, cvimNodeId=cvimNodeId, cvimMIBNotificationGroup=cvimMIBNotificationGroup, ciscoVimMIBConform=ciscoVimMIBConform, ciscoVimMIBGroups=ciscoVimMIBGroups)
