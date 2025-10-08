#
# PySNMP MIB module PTPBASE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/PTPBASE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:27:12 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Integer32, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, TimeTicks, MibIdentifier, Counter64, Bits, mib_2, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "TimeTicks", "MibIdentifier", "Counter64", "Bits", "mib-2", "IpAddress")
DisplayString, TruthValue, TextualConvention, AutonomousType = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention", "AutonomousType")
ptpbaseMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 241))
ptpbaseMIB.setRevisions(('2017-05-30 00:00',))
if mibBuilder.loadTexts: ptpbaseMIB.setLastUpdated('201705300000Z')
if mibBuilder.loadTexts: ptpbaseMIB.setOrganization('TICTOC Working Group')
class PtpClockDomainType(TextualConvention, Unsigned32):
    reference = "Section 7.1 ('Domains') and Table 2 ('domainNumber') of [IEEE-1588-2008]"
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class PtpClockIdentity(TextualConvention, OctetString):
    reference = "Section 7.5.2.2.1 ('General') of [IEEE-1588-2008]"
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class PtpClockInstanceType(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class PtpClockIntervalBase2(TextualConvention, Integer32):
    reference = "Section 7.7.2.1 ('General interval specification') of [IEEE-1588-2008]"
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-128, 127)

class PtpClockMechanismType(TextualConvention, Integer32):
    reference = "Sections 8.2.5.4.4 ('portDS.delayMechanism'), 6.6.4 ('Measuring link propagation delay in clocks supporting peer-to-peer path correction'), and 7.4.2 ('communication Path asymmetry') of [IEEE-1588-2008]."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 254))
    namedValues = NamedValues(("e2e", 1), ("p2p", 2), ("disabled", 254))

class PtpClockPortNumber(TextualConvention, Unsigned32):
    reference = "Sections 7.5.2.3 ('portNumber') and 5.3.5 ('PortIdentity') of [IEEE-1588-2008]"
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class PtpClockPortState(TextualConvention, Integer32):
    reference = "Sections 8.2.5.3.1 ('portState') and 9.2.5 ('State machines') of [IEEE-1588-2008]"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("initializing", 1), ("faulty", 2), ("disabled", 3), ("listening", 4), ("preMaster", 5), ("master", 6), ("passive", 7), ("uncalibrated", 8), ("slave", 9))

class PtpClockPortTransportTypeAddress(TextualConvention, OctetString):
    reference = 'Annex D (IPv4), Annex E (IPv6), Annex F (Ethernet), Annex G (DeviceNET), Annex H (ControlNET), and Annex I (IEC61158) of [IEEE-1588-2008]'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class PtpClockProfileType(TextualConvention, Integer32):
    reference = "Sections 3.1.30 ('profile') and 19.3 ('PTP profiles') of [IEEE-1588-2008]"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("default", 1), ("telecom", 2), ("vendorspecific", 3))

class PtpClockQualityAccuracyType(TextualConvention, Integer32):
    reference = "Section 5.3.7 ('ClockQuality'), Section 7.6.2.5 ('clockAccuracy'), and Table 6 ('clockAccuracy enumeration') of [IEEE-1588-2008]"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 254))
    namedValues = NamedValues(("nanoSecond25", 32), ("nanoSecond100", 33), ("nanoSecond250", 34), ("microSec1", 35), ("microSec2dot5", 36), ("microSec10", 37), ("microSec25", 38), ("microSec100", 39), ("microSec250", 40), ("milliSec1", 41), ("milliSec2dot5", 42), ("milliSec10", 43), ("milliSec25", 44), ("milliSec100", 45), ("milliSec250", 46), ("second1", 47), ("second10", 48), ("secondGreater10", 49), ("unknown", 254))

class PtpClockQualityClassType(TextualConvention, Integer32):
    reference = "Section 5.3.7 ('ClockQuality'), Section 7.6.2.4 ('clockClass'), and Table 5 ('clockClass specifications') of [IEEE-1588-2008]."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(6, 7, 13, 14, 52, 58))
    namedValues = NamedValues(("clockclass6", 6), ("clockclass7", 7), ("clockclass13", 13), ("clockclass14", 14), ("clockclass52", 52), ("clockclass58", 58))

class PtpClockRoleType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("master", 1), ("slave", 2))

class PtpClockStateType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("freerun", 1), ("holdover", 2), ("acquiring", 3), ("frequencyLocked", 4), ("phaseAligned", 5))

class PtpClockTimeInterval(TextualConvention, OctetString):
    reference = "Sections 5.3.2 ('TimeInterval') and 7.7.2.1 ('Timer interval specification') of [IEEE-1588-2008]"
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class PtpClockTimeSourceType(TextualConvention, Integer32):
    reference = "Section 5.3.7 ('ClockQuality'), Section 7.6.2.6 ('timeSource'), and Table 7 ('timeSource enumeration') of [IEEE-1588-2008]."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(16, 32, 48, 64, 80, 96, 144, 160))
    namedValues = NamedValues(("atomicClock", 16), ("gps", 32), ("terrestrialRadio", 48), ("ptp", 64), ("ntp", 80), ("handSet", 96), ("other", 144), ("internalOscillator", 160))

class PtpClockTxModeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unicast", 1), ("multicast", 2), ("multicastmix", 3))

class PtpClockType(TextualConvention, Integer32):
    reference = "Section 6.5.1 ('PTP device types') of [IEEE-1588-2008]."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("ordinaryClock", 1), ("boundaryClock", 2), ("transparentClock", 3), ("boundaryNode", 4))

ptpbaseMIBNotifs = MibIdentifier((1, 3, 6, 1, 2, 1, 241, 0))
ptpbaseMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 241, 1))
ptpbaseMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 241, 2))
ptpbaseMIBSystemInfo = MibIdentifier((1, 3, 6, 1, 2, 1, 241, 1, 1))
ptpbaseMIBClockInfo = MibIdentifier((1, 3, 6, 1, 2, 1, 241, 1, 2))
ptpbaseSystemTable = MibTable((1, 3, 6, 1, 2, 1, 241, 1, 1, 1), )
if mibBuilder.loadTexts: ptpbaseSystemTable.setStatus('current')
ptpbaseSystemEntry = MibTableRow((1, 3, 6, 1, 2, 1, 241, 1, 1, 1, 1), ).setIndexNames((0, "PTPBASE-MIB", "ptpDomainIndex"), (0, "PTPBASE-MIB", "ptpInstanceIndex"))
if mibBuilder.loadTexts: ptpbaseSystemEntry.setStatus('current')
ptpDomainIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 1, 1, 1, 1), PtpClockDomainType())
if mibBuilder.loadTexts: ptpDomainIndex.setStatus('current')
ptpInstanceIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 1, 1, 1, 2), PtpClockInstanceType())
if mibBuilder.loadTexts: ptpInstanceIndex.setStatus('current')
ptpDomainClockPortsTotal = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 1, 1, 1, 3), Gauge32()).setUnits('ptp ports').setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpDomainClockPortsTotal.setStatus('current')
ptpbaseSystemDomainTable = MibTable((1, 3, 6, 1, 2, 1, 241, 1, 1, 2), )
if mibBuilder.loadTexts: ptpbaseSystemDomainTable.setStatus('current')
ptpbaseSystemDomainEntry = MibTableRow((1, 3, 6, 1, 2, 1, 241, 1, 1, 2, 1), ).setIndexNames((0, "PTPBASE-MIB", "ptpbaseSystemDomainClockTypeIndex"))
if mibBuilder.loadTexts: ptpbaseSystemDomainEntry.setStatus('current')
ptpbaseSystemDomainClockTypeIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 1, 2, 1, 1), PtpClockType())
if mibBuilder.loadTexts: ptpbaseSystemDomainClockTypeIndex.setStatus('current')
ptpbaseSystemDomainTotals = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 1, 2, 1, 2), Unsigned32()).setUnits('domains').setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseSystemDomainTotals.setStatus('current')
ptpbaseSystemProfile = MibScalar((1, 3, 6, 1, 2, 1, 241, 1, 1, 3), PtpClockProfileType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseSystemProfile.setStatus('current')
ptpbaseClockCurrentDSTable = MibTable((1, 3, 6, 1, 2, 1, 241, 1, 2, 1), )
if mibBuilder.loadTexts: ptpbaseClockCurrentDSTable.setStatus('current')
ptpbaseClockCurrentDSEntry = MibTableRow((1, 3, 6, 1, 2, 1, 241, 1, 2, 1, 1), ).setIndexNames((0, "PTPBASE-MIB", "ptpbaseClockCurrentDSDomainIndex"), (0, "PTPBASE-MIB", "ptpbaseClockCurrentDSClockTypeIndex"), (0, "PTPBASE-MIB", "ptpbaseClockCurrentDSInstanceIndex"))
if mibBuilder.loadTexts: ptpbaseClockCurrentDSEntry.setStatus('current')
ptpbaseClockCurrentDSDomainIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 1, 1, 1), PtpClockDomainType())
if mibBuilder.loadTexts: ptpbaseClockCurrentDSDomainIndex.setStatus('current')
ptpbaseClockCurrentDSClockTypeIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 1, 1, 2), PtpClockType())
if mibBuilder.loadTexts: ptpbaseClockCurrentDSClockTypeIndex.setStatus('current')
ptpbaseClockCurrentDSInstanceIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 1, 1, 3), PtpClockInstanceType())
if mibBuilder.loadTexts: ptpbaseClockCurrentDSInstanceIndex.setStatus('current')
ptpbaseClockCurrentDSStepsRemoved = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 1, 1, 4), Unsigned32()).setUnits('Steps').setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockCurrentDSStepsRemoved.setStatus('current')
ptpbaseClockCurrentDSOffsetFromMaster = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 1, 1, 5), PtpClockTimeInterval()).setUnits('Time Interval').setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockCurrentDSOffsetFromMaster.setStatus('current')
ptpbaseClockCurrentDSMeanPathDelay = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 1, 1, 6), PtpClockTimeInterval()).setUnits('Time Interval').setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockCurrentDSMeanPathDelay.setStatus('current')
ptpbaseClockParentDSTable = MibTable((1, 3, 6, 1, 2, 1, 241, 1, 2, 2), )
if mibBuilder.loadTexts: ptpbaseClockParentDSTable.setStatus('current')
ptpbaseClockParentDSEntry = MibTableRow((1, 3, 6, 1, 2, 1, 241, 1, 2, 2, 1), ).setIndexNames((0, "PTPBASE-MIB", "ptpbaseClockParentDSDomainIndex"), (0, "PTPBASE-MIB", "ptpbaseClockParentDSClockTypeIndex"), (0, "PTPBASE-MIB", "ptpbaseClockParentDSInstanceIndex"))
if mibBuilder.loadTexts: ptpbaseClockParentDSEntry.setStatus('current')
ptpbaseClockParentDSDomainIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 2, 1, 1), PtpClockDomainType())
if mibBuilder.loadTexts: ptpbaseClockParentDSDomainIndex.setStatus('current')
ptpbaseClockParentDSClockTypeIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 2, 1, 2), PtpClockType())
if mibBuilder.loadTexts: ptpbaseClockParentDSClockTypeIndex.setStatus('current')
ptpbaseClockParentDSInstanceIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 2, 1, 3), PtpClockInstanceType())
if mibBuilder.loadTexts: ptpbaseClockParentDSInstanceIndex.setStatus('current')
ptpbaseClockParentDSParentPortIdentity = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockParentDSParentPortIdentity.setStatus('current')
ptpbaseClockParentDSParentStats = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 2, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockParentDSParentStats.setStatus('current')
ptpbaseClockParentDSOffset = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 2, 1, 6), PtpClockIntervalBase2().subtype(subtypeSpec=ValueRangeConstraint(-128, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockParentDSOffset.setStatus('current')
ptpbaseClockParentDSClockPhChRate = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockParentDSClockPhChRate.setStatus('current')
ptpbaseClockParentDSGMClockIdentity = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 2, 1, 8), PtpClockIdentity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockParentDSGMClockIdentity.setStatus('current')
ptpbaseClockParentDSGMClockPriority1 = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 2, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockParentDSGMClockPriority1.setStatus('current')
ptpbaseClockParentDSGMClockPriority2 = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 2, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockParentDSGMClockPriority2.setStatus('current')
ptpbaseClockParentDSGMClockQualityClass = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 2, 1, 11), PtpClockQualityClassType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockParentDSGMClockQualityClass.setStatus('current')
ptpbaseClockParentDSGMClockQualityAccuracy = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 2, 1, 12), PtpClockQualityAccuracyType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockParentDSGMClockQualityAccuracy.setStatus('current')
ptpbaseClockParentDSGMClockQualityOffset = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 2, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockParentDSGMClockQualityOffset.setStatus('current')
ptpbaseClockDefaultDSTable = MibTable((1, 3, 6, 1, 2, 1, 241, 1, 2, 3), )
if mibBuilder.loadTexts: ptpbaseClockDefaultDSTable.setStatus('current')
ptpbaseClockDefaultDSEntry = MibTableRow((1, 3, 6, 1, 2, 1, 241, 1, 2, 3, 1), ).setIndexNames((0, "PTPBASE-MIB", "ptpbaseClockDefaultDSDomainIndex"), (0, "PTPBASE-MIB", "ptpbaseClockDefaultDSClockTypeIndex"), (0, "PTPBASE-MIB", "ptpbaseClockDefaultDSInstanceIndex"))
if mibBuilder.loadTexts: ptpbaseClockDefaultDSEntry.setStatus('current')
ptpbaseClockDefaultDSDomainIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 3, 1, 1), PtpClockDomainType())
if mibBuilder.loadTexts: ptpbaseClockDefaultDSDomainIndex.setStatus('current')
ptpbaseClockDefaultDSClockTypeIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 3, 1, 2), PtpClockType())
if mibBuilder.loadTexts: ptpbaseClockDefaultDSClockTypeIndex.setStatus('current')
ptpbaseClockDefaultDSInstanceIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 3, 1, 3), PtpClockInstanceType())
if mibBuilder.loadTexts: ptpbaseClockDefaultDSInstanceIndex.setStatus('current')
ptpbaseClockDefaultDSTwoStepFlag = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 3, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockDefaultDSTwoStepFlag.setStatus('current')
ptpbaseClockDefaultDSClockIdentity = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 3, 1, 5), PtpClockIdentity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockDefaultDSClockIdentity.setStatus('current')
ptpbaseClockDefaultDSPriority1 = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockDefaultDSPriority1.setStatus('current')
ptpbaseClockDefaultDSPriority2 = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 3, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockDefaultDSPriority2.setStatus('current')
ptpbaseClockDefaultDSSlaveOnly = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 3, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockDefaultDSSlaveOnly.setStatus('current')
ptpbaseClockDefaultDSQualityClass = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 3, 1, 9), PtpClockQualityClassType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockDefaultDSQualityClass.setStatus('current')
ptpbaseClockDefaultDSQualityAccuracy = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 3, 1, 10), PtpClockQualityAccuracyType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockDefaultDSQualityAccuracy.setStatus('current')
ptpbaseClockDefaultDSQualityOffset = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 3, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockDefaultDSQualityOffset.setStatus('current')
ptpbaseClockRunningTable = MibTable((1, 3, 6, 1, 2, 1, 241, 1, 2, 4), )
if mibBuilder.loadTexts: ptpbaseClockRunningTable.setStatus('current')
ptpbaseClockRunningEntry = MibTableRow((1, 3, 6, 1, 2, 1, 241, 1, 2, 4, 1), ).setIndexNames((0, "PTPBASE-MIB", "ptpbaseClockRunningDomainIndex"), (0, "PTPBASE-MIB", "ptpbaseClockRunningClockTypeIndex"), (0, "PTPBASE-MIB", "ptpbaseClockRunningInstanceIndex"))
if mibBuilder.loadTexts: ptpbaseClockRunningEntry.setStatus('current')
ptpbaseClockRunningDomainIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 4, 1, 1), PtpClockDomainType())
if mibBuilder.loadTexts: ptpbaseClockRunningDomainIndex.setStatus('current')
ptpbaseClockRunningClockTypeIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 4, 1, 2), PtpClockType())
if mibBuilder.loadTexts: ptpbaseClockRunningClockTypeIndex.setStatus('current')
ptpbaseClockRunningInstanceIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 4, 1, 3), PtpClockInstanceType())
if mibBuilder.loadTexts: ptpbaseClockRunningInstanceIndex.setStatus('current')
ptpbaseClockRunningState = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 4, 1, 4), PtpClockStateType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockRunningState.setStatus('current')
ptpbaseClockRunningPacketsSent = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 4, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockRunningPacketsSent.setStatus('current')
ptpbaseClockRunningPacketsReceived = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 4, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockRunningPacketsReceived.setStatus('current')
ptpbaseClockTimePropertiesDSTable = MibTable((1, 3, 6, 1, 2, 1, 241, 1, 2, 5), )
if mibBuilder.loadTexts: ptpbaseClockTimePropertiesDSTable.setStatus('current')
ptpbaseClockTimePropertiesDSEntry = MibTableRow((1, 3, 6, 1, 2, 1, 241, 1, 2, 5, 1), ).setIndexNames((0, "PTPBASE-MIB", "ptpbaseClockTimePropertiesDSDomainIndex"), (0, "PTPBASE-MIB", "ptpbaseClockTimePropertiesDSClockTypeIndex"), (0, "PTPBASE-MIB", "ptpbaseClockTimePropertiesDSInstanceIndex"))
if mibBuilder.loadTexts: ptpbaseClockTimePropertiesDSEntry.setStatus('current')
ptpbaseClockTimePropertiesDSDomainIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 5, 1, 1), PtpClockDomainType())
if mibBuilder.loadTexts: ptpbaseClockTimePropertiesDSDomainIndex.setStatus('current')
ptpbaseClockTimePropertiesDSClockTypeIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 5, 1, 2), PtpClockType())
if mibBuilder.loadTexts: ptpbaseClockTimePropertiesDSClockTypeIndex.setStatus('current')
ptpbaseClockTimePropertiesDSInstanceIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 5, 1, 3), PtpClockInstanceType())
if mibBuilder.loadTexts: ptpbaseClockTimePropertiesDSInstanceIndex.setStatus('current')
ptpbaseClockTimePropertiesDSCurrentUTCOffsetValid = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 5, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockTimePropertiesDSCurrentUTCOffsetValid.setStatus('current')
ptpbaseClockTimePropertiesDSCurrentUTCOffset = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 5, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockTimePropertiesDSCurrentUTCOffset.setStatus('current')
ptpbaseClockTimePropertiesDSLeap59 = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 5, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockTimePropertiesDSLeap59.setStatus('current')
ptpbaseClockTimePropertiesDSLeap61 = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 5, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockTimePropertiesDSLeap61.setStatus('current')
ptpbaseClockTimePropertiesDSTimeTraceable = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 5, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockTimePropertiesDSTimeTraceable.setStatus('current')
ptpbaseClockTimePropertiesDSFreqTraceable = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 5, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockTimePropertiesDSFreqTraceable.setStatus('current')
ptpbaseClockTimePropertiesDSPTPTimescale = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 5, 1, 10), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockTimePropertiesDSPTPTimescale.setStatus('current')
ptpbaseClockTimePropertiesDSSource = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 5, 1, 11), PtpClockTimeSourceType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockTimePropertiesDSSource.setStatus('current')
ptpbaseClockTransDefaultDSTable = MibTable((1, 3, 6, 1, 2, 1, 241, 1, 2, 6), )
if mibBuilder.loadTexts: ptpbaseClockTransDefaultDSTable.setStatus('current')
ptpbaseClockTransDefaultDSEntry = MibTableRow((1, 3, 6, 1, 2, 1, 241, 1, 2, 6, 1), ).setIndexNames((0, "PTPBASE-MIB", "ptpbaseClockTransDefaultDSDomainIndex"), (0, "PTPBASE-MIB", "ptpbaseClockTransDefaultDSInstanceIndex"))
if mibBuilder.loadTexts: ptpbaseClockTransDefaultDSEntry.setStatus('current')
ptpbaseClockTransDefaultDSDomainIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 6, 1, 1), PtpClockDomainType())
if mibBuilder.loadTexts: ptpbaseClockTransDefaultDSDomainIndex.setStatus('current')
ptpbaseClockTransDefaultDSInstanceIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 6, 1, 2), PtpClockInstanceType())
if mibBuilder.loadTexts: ptpbaseClockTransDefaultDSInstanceIndex.setStatus('current')
ptpbaseClockTransDefaultDSClockIdentity = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 6, 1, 3), PtpClockIdentity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockTransDefaultDSClockIdentity.setStatus('current')
ptpbaseClockTransDefaultDSNumOfPorts = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 6, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockTransDefaultDSNumOfPorts.setStatus('current')
ptpbaseClockTransDefaultDSDelay = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 6, 1, 5), PtpClockMechanismType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockTransDefaultDSDelay.setStatus('current')
ptpbaseClockTransDefaultDSPrimaryDomain = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 6, 1, 6), PtpClockDomainType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockTransDefaultDSPrimaryDomain.setStatus('current')
ptpbaseClockPortTable = MibTable((1, 3, 6, 1, 2, 1, 241, 1, 2, 7), )
if mibBuilder.loadTexts: ptpbaseClockPortTable.setStatus('current')
ptpbaseClockPortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 241, 1, 2, 7, 1), ).setIndexNames((0, "PTPBASE-MIB", "ptpbaseClockPortDomainIndex"), (0, "PTPBASE-MIB", "ptpbaseClockPortClockTypeIndex"), (0, "PTPBASE-MIB", "ptpbaseClockPortClockInstanceIndex"), (0, "PTPBASE-MIB", "ptpbaseClockPortTablePortNumberIndex"))
if mibBuilder.loadTexts: ptpbaseClockPortEntry.setStatus('current')
ptpbaseClockPortDomainIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 7, 1, 1), PtpClockDomainType())
if mibBuilder.loadTexts: ptpbaseClockPortDomainIndex.setStatus('current')
ptpbaseClockPortClockTypeIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 7, 1, 2), PtpClockType())
if mibBuilder.loadTexts: ptpbaseClockPortClockTypeIndex.setStatus('current')
ptpbaseClockPortClockInstanceIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 7, 1, 3), PtpClockInstanceType())
if mibBuilder.loadTexts: ptpbaseClockPortClockInstanceIndex.setStatus('current')
ptpbaseClockPortTablePortNumberIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 7, 1, 4), PtpClockPortNumber())
if mibBuilder.loadTexts: ptpbaseClockPortTablePortNumberIndex.setStatus('current')
ptpbaseClockPortName = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 7, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockPortName.setStatus('current')
ptpbaseClockPortRole = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 7, 1, 6), PtpClockRoleType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockPortRole.setStatus('current')
ptpbaseClockPortSyncTwoStep = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 7, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockPortSyncTwoStep.setStatus('current')
ptpbaseClockPortCurrentPeerAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 7, 1, 8), AutonomousType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockPortCurrentPeerAddressType.setStatus('current')
ptpbaseClockPortCurrentPeerAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 7, 1, 9), PtpClockPortTransportTypeAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockPortCurrentPeerAddress.setStatus('current')
ptpbaseClockPortNumOfAssociatedPorts = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 7, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockPortNumOfAssociatedPorts.setStatus('current')
ptpbaseClockPortDSTable = MibTable((1, 3, 6, 1, 2, 1, 241, 1, 2, 8), )
if mibBuilder.loadTexts: ptpbaseClockPortDSTable.setStatus('current')
ptpbaseClockPortDSEntry = MibTableRow((1, 3, 6, 1, 2, 1, 241, 1, 2, 8, 1), ).setIndexNames((0, "PTPBASE-MIB", "ptpbaseClockPortDSDomainIndex"), (0, "PTPBASE-MIB", "ptpbaseClockPortDSClockTypeIndex"), (0, "PTPBASE-MIB", "ptpbaseClockPortDSClockInstanceIndex"), (0, "PTPBASE-MIB", "ptpbaseClockPortDSPortNumberIndex"))
if mibBuilder.loadTexts: ptpbaseClockPortDSEntry.setStatus('current')
ptpbaseClockPortDSDomainIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 8, 1, 1), PtpClockDomainType())
if mibBuilder.loadTexts: ptpbaseClockPortDSDomainIndex.setStatus('current')
ptpbaseClockPortDSClockTypeIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 8, 1, 2), PtpClockType())
if mibBuilder.loadTexts: ptpbaseClockPortDSClockTypeIndex.setStatus('current')
ptpbaseClockPortDSClockInstanceIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 8, 1, 3), PtpClockInstanceType())
if mibBuilder.loadTexts: ptpbaseClockPortDSClockInstanceIndex.setStatus('current')
ptpbaseClockPortDSPortNumberIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 8, 1, 4), PtpClockPortNumber())
if mibBuilder.loadTexts: ptpbaseClockPortDSPortNumberIndex.setStatus('current')
ptpbaseClockPortDSName = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 8, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockPortDSName.setStatus('current')
ptpbaseClockPortDSPortIdentity = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 8, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockPortDSPortIdentity.setStatus('current')
ptpbaseClockPortDSlogAnnouncementInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 8, 1, 7), PtpClockIntervalBase2()).setUnits('Time Interval').setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockPortDSlogAnnouncementInterval.setStatus('current')
ptpbaseClockPortDSAnnounceRctTimeout = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 8, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockPortDSAnnounceRctTimeout.setStatus('current')
ptpbaseClockPortDSlogSyncInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 8, 1, 9), PtpClockIntervalBase2()).setUnits('Time Interval').setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockPortDSlogSyncInterval.setStatus('current')
ptpbaseClockPortDSMinDelayReqInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 8, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockPortDSMinDelayReqInterval.setStatus('current')
ptpbaseClockPortDSPeerDelayReqInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 8, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockPortDSPeerDelayReqInterval.setStatus('current')
ptpbaseClockPortDSDelayMech = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 8, 1, 12), PtpClockMechanismType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockPortDSDelayMech.setStatus('current')
ptpbaseClockPortDSPeerMeanPathDelay = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 8, 1, 13), PtpClockTimeInterval()).setUnits('Time Interval').setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockPortDSPeerMeanPathDelay.setStatus('current')
ptpbaseClockPortDSGrantDuration = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 8, 1, 14), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockPortDSGrantDuration.setStatus('current')
ptpbaseClockPortDSPTPVersion = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 8, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockPortDSPTPVersion.setStatus('current')
ptpbaseClockPortRunningTable = MibTable((1, 3, 6, 1, 2, 1, 241, 1, 2, 9), )
if mibBuilder.loadTexts: ptpbaseClockPortRunningTable.setStatus('current')
ptpbaseClockPortRunningEntry = MibTableRow((1, 3, 6, 1, 2, 1, 241, 1, 2, 9, 1), ).setIndexNames((0, "PTPBASE-MIB", "ptpbaseClockPortRunningDomainIndex"), (0, "PTPBASE-MIB", "ptpbaseClockPortRunningClockTypeIndex"), (0, "PTPBASE-MIB", "ptpbaseClockPortRunningClockInstanceIndex"), (0, "PTPBASE-MIB", "ptpbaseClockPortRunningPortNumberIndex"))
if mibBuilder.loadTexts: ptpbaseClockPortRunningEntry.setStatus('current')
ptpbaseClockPortRunningDomainIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 9, 1, 1), PtpClockDomainType())
if mibBuilder.loadTexts: ptpbaseClockPortRunningDomainIndex.setStatus('current')
ptpbaseClockPortRunningClockTypeIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 9, 1, 2), PtpClockType())
if mibBuilder.loadTexts: ptpbaseClockPortRunningClockTypeIndex.setStatus('current')
ptpbaseClockPortRunningClockInstanceIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 9, 1, 3), PtpClockInstanceType())
if mibBuilder.loadTexts: ptpbaseClockPortRunningClockInstanceIndex.setStatus('current')
ptpbaseClockPortRunningPortNumberIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 9, 1, 4), PtpClockPortNumber())
if mibBuilder.loadTexts: ptpbaseClockPortRunningPortNumberIndex.setStatus('current')
ptpbaseClockPortRunningName = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 9, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockPortRunningName.setStatus('current')
ptpbaseClockPortRunningState = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 9, 1, 6), PtpClockPortState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockPortRunningState.setStatus('current')
ptpbaseClockPortRunningRole = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 9, 1, 7), PtpClockRoleType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockPortRunningRole.setStatus('current')
ptpbaseClockPortRunningInterfaceIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 9, 1, 8), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockPortRunningInterfaceIndex.setStatus('current')
ptpbaseClockPortRunningTransport = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 9, 1, 9), AutonomousType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockPortRunningTransport.setStatus('current')
ptpbaseClockPortRunningEncapsulationType = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 9, 1, 10), AutonomousType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockPortRunningEncapsulationType.setStatus('current')
ptpbaseClockPortRunningTxMode = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 9, 1, 11), PtpClockTxModeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockPortRunningTxMode.setStatus('current')
ptpbaseClockPortRunningRxMode = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 9, 1, 12), PtpClockTxModeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockPortRunningRxMode.setStatus('current')
ptpbaseClockPortRunningPacketsReceived = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 9, 1, 13), Counter64()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockPortRunningPacketsReceived.setStatus('current')
ptpbaseClockPortRunningPacketsSent = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 9, 1, 14), Counter64()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockPortRunningPacketsSent.setStatus('current')
ptpbaseClockPortTransDSTable = MibTable((1, 3, 6, 1, 2, 1, 241, 1, 2, 10), )
if mibBuilder.loadTexts: ptpbaseClockPortTransDSTable.setStatus('current')
ptpbaseClockPortTransDSEntry = MibTableRow((1, 3, 6, 1, 2, 1, 241, 1, 2, 10, 1), ).setIndexNames((0, "PTPBASE-MIB", "ptpbaseClockPortTransDSDomainIndex"), (0, "PTPBASE-MIB", "ptpbaseClockPortTransDSInstanceIndex"), (0, "PTPBASE-MIB", "ptpbaseClockPortTransDSPortNumberIndex"))
if mibBuilder.loadTexts: ptpbaseClockPortTransDSEntry.setStatus('current')
ptpbaseClockPortTransDSDomainIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 10, 1, 1), PtpClockDomainType())
if mibBuilder.loadTexts: ptpbaseClockPortTransDSDomainIndex.setStatus('current')
ptpbaseClockPortTransDSInstanceIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 10, 1, 2), PtpClockInstanceType())
if mibBuilder.loadTexts: ptpbaseClockPortTransDSInstanceIndex.setStatus('current')
ptpbaseClockPortTransDSPortNumberIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 10, 1, 3), PtpClockPortNumber())
if mibBuilder.loadTexts: ptpbaseClockPortTransDSPortNumberIndex.setStatus('current')
ptpbaseClockPortTransDSPortIdentity = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 10, 1, 4), PtpClockIdentity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockPortTransDSPortIdentity.setStatus('current')
ptpbaseClockPortTransDSlogMinPdelayReqInt = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 10, 1, 5), PtpClockIntervalBase2()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockPortTransDSlogMinPdelayReqInt.setStatus('current')
ptpbaseClockPortTransDSFaultyFlag = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 10, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockPortTransDSFaultyFlag.setStatus('current')
ptpbaseClockPortTransDSPeerMeanPathDelay = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 10, 1, 7), PtpClockTimeInterval()).setUnits('Time Interval').setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockPortTransDSPeerMeanPathDelay.setStatus('current')
ptpbaseClockPortAssociateTable = MibTable((1, 3, 6, 1, 2, 1, 241, 1, 2, 11), )
if mibBuilder.loadTexts: ptpbaseClockPortAssociateTable.setStatus('current')
ptpbaseWellKnownTransportTypes = MibIdentifier((1, 3, 6, 1, 2, 1, 241, 1, 2, 12))
ptpbaseTransportTypeIPversion4 = ObjectIdentity((1, 3, 6, 1, 2, 1, 241, 1, 2, 12, 1))
if mibBuilder.loadTexts: ptpbaseTransportTypeIPversion4.setStatus('current')
ptpbaseTransportTypeIPversion6 = ObjectIdentity((1, 3, 6, 1, 2, 1, 241, 1, 2, 12, 2))
if mibBuilder.loadTexts: ptpbaseTransportTypeIPversion6.setStatus('current')
ptpbaseTransportTypeEthernet = ObjectIdentity((1, 3, 6, 1, 2, 1, 241, 1, 2, 12, 3))
if mibBuilder.loadTexts: ptpbaseTransportTypeEthernet.setStatus('current')
ptpbaseTransportTypeDeviceNET = ObjectIdentity((1, 3, 6, 1, 2, 1, 241, 1, 2, 12, 4))
if mibBuilder.loadTexts: ptpbaseTransportTypeDeviceNET.setStatus('current')
ptpbaseTransportTypeControlNET = ObjectIdentity((1, 3, 6, 1, 2, 1, 241, 1, 2, 12, 5))
if mibBuilder.loadTexts: ptpbaseTransportTypeControlNET.setStatus('current')
ptpbaseTransportTypeIEC61158 = ObjectIdentity((1, 3, 6, 1, 2, 1, 241, 1, 2, 12, 6))
if mibBuilder.loadTexts: ptpbaseTransportTypeIEC61158.setStatus('current')
ptpbaseWellKnownEncapsulationTypes = MibIdentifier((1, 3, 6, 1, 2, 1, 241, 1, 2, 13))
ptpbaseEncapsulationTypeEthernet = ObjectIdentity((1, 3, 6, 1, 2, 1, 241, 1, 2, 13, 1))
if mibBuilder.loadTexts: ptpbaseEncapsulationTypeEthernet.setStatus('current')
ptpbaseEncapsulationTypeVLAN = ObjectIdentity((1, 3, 6, 1, 2, 1, 241, 1, 2, 13, 2))
if mibBuilder.loadTexts: ptpbaseEncapsulationTypeVLAN.setStatus('current')
ptpbaseEncapsulationTypeUDPIPLSP = ObjectIdentity((1, 3, 6, 1, 2, 1, 241, 1, 2, 13, 3))
if mibBuilder.loadTexts: ptpbaseEncapsulationTypeUDPIPLSP.setStatus('current')
ptpbaseEncapsulationTypePWUDPIPLSP = ObjectIdentity((1, 3, 6, 1, 2, 1, 241, 1, 2, 13, 4))
if mibBuilder.loadTexts: ptpbaseEncapsulationTypePWUDPIPLSP.setStatus('current')
ptpbaseEncapsulationTypePWEthernetLSP = ObjectIdentity((1, 3, 6, 1, 2, 1, 241, 1, 2, 13, 5))
if mibBuilder.loadTexts: ptpbaseEncapsulationTypePWEthernetLSP.setStatus('current')
ptpbaseClockPortAssociateEntry = MibTableRow((1, 3, 6, 1, 2, 1, 241, 1, 2, 11, 1), ).setIndexNames((0, "PTPBASE-MIB", "ptpClockPortCurrentDomainIndex"), (0, "PTPBASE-MIB", "ptpClockPortCurrentClockTypeIndex"), (0, "PTPBASE-MIB", "ptpClockPortCurrentClockInstanceIndex"), (0, "PTPBASE-MIB", "ptpClockPortCurrentPortNumberIndex"), (0, "PTPBASE-MIB", "ptpbaseClockPortAssociatePortIndex"))
if mibBuilder.loadTexts: ptpbaseClockPortAssociateEntry.setStatus('current')
ptpClockPortCurrentDomainIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 11, 1, 1), PtpClockDomainType())
if mibBuilder.loadTexts: ptpClockPortCurrentDomainIndex.setStatus('current')
ptpClockPortCurrentClockTypeIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 11, 1, 2), PtpClockType())
if mibBuilder.loadTexts: ptpClockPortCurrentClockTypeIndex.setStatus('current')
ptpClockPortCurrentClockInstanceIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 11, 1, 3), PtpClockInstanceType())
if mibBuilder.loadTexts: ptpClockPortCurrentClockInstanceIndex.setStatus('current')
ptpClockPortCurrentPortNumberIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 11, 1, 4), PtpClockPortNumber())
if mibBuilder.loadTexts: ptpClockPortCurrentPortNumberIndex.setStatus('current')
ptpbaseClockPortAssociatePortIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 11, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: ptpbaseClockPortAssociatePortIndex.setStatus('current')
ptpbaseClockPortAssociateAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 11, 1, 6), AutonomousType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockPortAssociateAddressType.setStatus('current')
ptpbaseClockPortAssociateAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 11, 1, 7), PtpClockPortTransportTypeAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockPortAssociateAddress.setStatus('current')
ptpbaseClockPortAssociatePacketsSent = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 11, 1, 8), Counter64()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockPortAssociatePacketsSent.setStatus('current')
ptpbaseClockPortAssociatePacketsReceived = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 11, 1, 9), Counter64()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockPortAssociatePacketsReceived.setStatus('current')
ptpbaseClockPortAssociateInErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 11, 1, 10), Counter64()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockPortAssociateInErrors.setStatus('current')
ptpbaseClockPortAssociateOutErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 241, 1, 2, 11, 1, 11), Counter64()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpbaseClockPortAssociateOutErrors.setStatus('current')
ptpbaseMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 241, 2, 1))
ptpbaseMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 241, 2, 2))
ptpbaseMIBCompliancesSystemInfo = ModuleCompliance((1, 3, 6, 1, 2, 1, 241, 2, 1, 1)).setObjects(("PTPBASE-MIB", "ptpbaseMIBSystemInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptpbaseMIBCompliancesSystemInfo = ptpbaseMIBCompliancesSystemInfo.setStatus('current')
ptpbaseMIBCompliancesClockInfo = ModuleCompliance((1, 3, 6, 1, 2, 1, 241, 2, 1, 2)).setObjects(("PTPBASE-MIB", "ptpbaseMIBClockCurrentDSGroup"), ("PTPBASE-MIB", "ptpbaseMIBClockParentDSGroup"), ("PTPBASE-MIB", "ptpbaseMIBClockDefaultDSGroup"), ("PTPBASE-MIB", "ptpbaseMIBClockRunningGroup"), ("PTPBASE-MIB", "ptpbaseMIBClockTimepropertiesGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptpbaseMIBCompliancesClockInfo = ptpbaseMIBCompliancesClockInfo.setStatus('current')
ptpbaseMIBCompliancesClockPortInfo = ModuleCompliance((1, 3, 6, 1, 2, 1, 241, 2, 1, 3)).setObjects(("PTPBASE-MIB", "ptpbaseMIBClockPortGroup"), ("PTPBASE-MIB", "ptpbaseMIBClockPortDSGroup"), ("PTPBASE-MIB", "ptpbaseMIBClockPortRunningGroup"), ("PTPBASE-MIB", "ptpbaseMIBClockPortAssociateGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptpbaseMIBCompliancesClockPortInfo = ptpbaseMIBCompliancesClockPortInfo.setStatus('current')
ptpbaseMIBCompliancesTransparentClockInfo = ModuleCompliance((1, 3, 6, 1, 2, 1, 241, 2, 1, 4)).setObjects(("PTPBASE-MIB", "ptpbaseMIBClockTranparentDSGroup"), ("PTPBASE-MIB", "ptpbaseMIBClockPortTransDSGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptpbaseMIBCompliancesTransparentClockInfo = ptpbaseMIBCompliancesTransparentClockInfo.setStatus('current')
ptpbaseMIBSystemInfoGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 241, 2, 2, 1)).setObjects(("PTPBASE-MIB", "ptpbaseSystemDomainTotals"), ("PTPBASE-MIB", "ptpDomainClockPortsTotal"), ("PTPBASE-MIB", "ptpbaseSystemProfile"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptpbaseMIBSystemInfoGroup = ptpbaseMIBSystemInfoGroup.setStatus('current')
ptpbaseMIBClockCurrentDSGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 241, 2, 2, 2)).setObjects(("PTPBASE-MIB", "ptpbaseClockCurrentDSStepsRemoved"), ("PTPBASE-MIB", "ptpbaseClockCurrentDSOffsetFromMaster"), ("PTPBASE-MIB", "ptpbaseClockCurrentDSMeanPathDelay"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptpbaseMIBClockCurrentDSGroup = ptpbaseMIBClockCurrentDSGroup.setStatus('current')
ptpbaseMIBClockParentDSGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 241, 2, 2, 3)).setObjects(("PTPBASE-MIB", "ptpbaseClockParentDSParentPortIdentity"), ("PTPBASE-MIB", "ptpbaseClockParentDSParentStats"), ("PTPBASE-MIB", "ptpbaseClockParentDSOffset"), ("PTPBASE-MIB", "ptpbaseClockParentDSClockPhChRate"), ("PTPBASE-MIB", "ptpbaseClockParentDSGMClockIdentity"), ("PTPBASE-MIB", "ptpbaseClockParentDSGMClockPriority1"), ("PTPBASE-MIB", "ptpbaseClockParentDSGMClockPriority2"), ("PTPBASE-MIB", "ptpbaseClockParentDSGMClockQualityClass"), ("PTPBASE-MIB", "ptpbaseClockParentDSGMClockQualityAccuracy"), ("PTPBASE-MIB", "ptpbaseClockParentDSGMClockQualityOffset"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptpbaseMIBClockParentDSGroup = ptpbaseMIBClockParentDSGroup.setStatus('current')
ptpbaseMIBClockDefaultDSGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 241, 2, 2, 4)).setObjects(("PTPBASE-MIB", "ptpbaseClockDefaultDSTwoStepFlag"), ("PTPBASE-MIB", "ptpbaseClockDefaultDSClockIdentity"), ("PTPBASE-MIB", "ptpbaseClockDefaultDSPriority1"), ("PTPBASE-MIB", "ptpbaseClockDefaultDSPriority2"), ("PTPBASE-MIB", "ptpbaseClockDefaultDSSlaveOnly"), ("PTPBASE-MIB", "ptpbaseClockDefaultDSQualityClass"), ("PTPBASE-MIB", "ptpbaseClockDefaultDSQualityAccuracy"), ("PTPBASE-MIB", "ptpbaseClockDefaultDSQualityOffset"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptpbaseMIBClockDefaultDSGroup = ptpbaseMIBClockDefaultDSGroup.setStatus('current')
ptpbaseMIBClockRunningGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 241, 2, 2, 5)).setObjects(("PTPBASE-MIB", "ptpbaseClockRunningState"), ("PTPBASE-MIB", "ptpbaseClockRunningPacketsSent"), ("PTPBASE-MIB", "ptpbaseClockRunningPacketsReceived"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptpbaseMIBClockRunningGroup = ptpbaseMIBClockRunningGroup.setStatus('current')
ptpbaseMIBClockTimepropertiesGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 241, 2, 2, 6)).setObjects(("PTPBASE-MIB", "ptpbaseClockTimePropertiesDSCurrentUTCOffsetValid"), ("PTPBASE-MIB", "ptpbaseClockTimePropertiesDSCurrentUTCOffset"), ("PTPBASE-MIB", "ptpbaseClockTimePropertiesDSLeap59"), ("PTPBASE-MIB", "ptpbaseClockTimePropertiesDSLeap61"), ("PTPBASE-MIB", "ptpbaseClockTimePropertiesDSTimeTraceable"), ("PTPBASE-MIB", "ptpbaseClockTimePropertiesDSFreqTraceable"), ("PTPBASE-MIB", "ptpbaseClockTimePropertiesDSPTPTimescale"), ("PTPBASE-MIB", "ptpbaseClockTimePropertiesDSSource"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptpbaseMIBClockTimepropertiesGroup = ptpbaseMIBClockTimepropertiesGroup.setStatus('current')
ptpbaseMIBClockTranparentDSGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 241, 2, 2, 7)).setObjects(("PTPBASE-MIB", "ptpbaseClockTransDefaultDSClockIdentity"), ("PTPBASE-MIB", "ptpbaseClockTransDefaultDSNumOfPorts"), ("PTPBASE-MIB", "ptpbaseClockTransDefaultDSDelay"), ("PTPBASE-MIB", "ptpbaseClockTransDefaultDSPrimaryDomain"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptpbaseMIBClockTranparentDSGroup = ptpbaseMIBClockTranparentDSGroup.setStatus('current')
ptpbaseMIBClockPortGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 241, 2, 2, 8)).setObjects(("PTPBASE-MIB", "ptpbaseClockPortName"), ("PTPBASE-MIB", "ptpbaseClockPortSyncTwoStep"), ("PTPBASE-MIB", "ptpbaseClockPortCurrentPeerAddress"), ("PTPBASE-MIB", "ptpbaseClockPortNumOfAssociatedPorts"), ("PTPBASE-MIB", "ptpbaseClockPortCurrentPeerAddressType"), ("PTPBASE-MIB", "ptpbaseClockPortRole"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptpbaseMIBClockPortGroup = ptpbaseMIBClockPortGroup.setStatus('current')
ptpbaseMIBClockPortDSGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 241, 2, 2, 9)).setObjects(("PTPBASE-MIB", "ptpbaseClockPortDSName"), ("PTPBASE-MIB", "ptpbaseClockPortDSPortIdentity"), ("PTPBASE-MIB", "ptpbaseClockPortDSlogAnnouncementInterval"), ("PTPBASE-MIB", "ptpbaseClockPortDSAnnounceRctTimeout"), ("PTPBASE-MIB", "ptpbaseClockPortDSlogSyncInterval"), ("PTPBASE-MIB", "ptpbaseClockPortDSMinDelayReqInterval"), ("PTPBASE-MIB", "ptpbaseClockPortDSPeerDelayReqInterval"), ("PTPBASE-MIB", "ptpbaseClockPortDSDelayMech"), ("PTPBASE-MIB", "ptpbaseClockPortDSPeerMeanPathDelay"), ("PTPBASE-MIB", "ptpbaseClockPortDSGrantDuration"), ("PTPBASE-MIB", "ptpbaseClockPortDSPTPVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptpbaseMIBClockPortDSGroup = ptpbaseMIBClockPortDSGroup.setStatus('current')
ptpbaseMIBClockPortRunningGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 241, 2, 2, 10)).setObjects(("PTPBASE-MIB", "ptpbaseClockPortRunningName"), ("PTPBASE-MIB", "ptpbaseClockPortRunningState"), ("PTPBASE-MIB", "ptpbaseClockPortRunningRole"), ("PTPBASE-MIB", "ptpbaseClockPortRunningInterfaceIndex"), ("PTPBASE-MIB", "ptpbaseClockPortRunningTransport"), ("PTPBASE-MIB", "ptpbaseClockPortRunningEncapsulationType"), ("PTPBASE-MIB", "ptpbaseClockPortRunningTxMode"), ("PTPBASE-MIB", "ptpbaseClockPortRunningRxMode"), ("PTPBASE-MIB", "ptpbaseClockPortRunningPacketsReceived"), ("PTPBASE-MIB", "ptpbaseClockPortRunningPacketsSent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptpbaseMIBClockPortRunningGroup = ptpbaseMIBClockPortRunningGroup.setStatus('current')
ptpbaseMIBClockPortTransDSGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 241, 2, 2, 11)).setObjects(("PTPBASE-MIB", "ptpbaseClockPortTransDSPortIdentity"), ("PTPBASE-MIB", "ptpbaseClockPortTransDSlogMinPdelayReqInt"), ("PTPBASE-MIB", "ptpbaseClockPortTransDSFaultyFlag"), ("PTPBASE-MIB", "ptpbaseClockPortTransDSPeerMeanPathDelay"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptpbaseMIBClockPortTransDSGroup = ptpbaseMIBClockPortTransDSGroup.setStatus('current')
ptpbaseMIBClockPortAssociateGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 241, 2, 2, 12)).setObjects(("PTPBASE-MIB", "ptpbaseClockPortAssociatePacketsSent"), ("PTPBASE-MIB", "ptpbaseClockPortAssociatePacketsReceived"), ("PTPBASE-MIB", "ptpbaseClockPortAssociateAddress"), ("PTPBASE-MIB", "ptpbaseClockPortAssociateAddressType"), ("PTPBASE-MIB", "ptpbaseClockPortAssociateInErrors"), ("PTPBASE-MIB", "ptpbaseClockPortAssociateOutErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptpbaseMIBClockPortAssociateGroup = ptpbaseMIBClockPortAssociateGroup.setStatus('current')
mibBuilder.exportSymbols("PTPBASE-MIB", PtpClockIntervalBase2=PtpClockIntervalBase2, ptpbaseClockRunningState=ptpbaseClockRunningState, ptpbaseClockParentDSGMClockPriority1=ptpbaseClockParentDSGMClockPriority1, ptpbaseClockTimePropertiesDSEntry=ptpbaseClockTimePropertiesDSEntry, ptpbaseClockCurrentDSDomainIndex=ptpbaseClockCurrentDSDomainIndex, ptpbaseClockParentDSParentPortIdentity=ptpbaseClockParentDSParentPortIdentity, PtpClockInstanceType=PtpClockInstanceType, ptpbaseMIBClockDefaultDSGroup=ptpbaseMIBClockDefaultDSGroup, PtpClockQualityAccuracyType=PtpClockQualityAccuracyType, ptpbaseClockPortRunningName=ptpbaseClockPortRunningName, PtpClockQualityClassType=PtpClockQualityClassType, ptpbaseClockPortTransDSDomainIndex=ptpbaseClockPortTransDSDomainIndex, ptpbaseClockPortDSMinDelayReqInterval=ptpbaseClockPortDSMinDelayReqInterval, ptpbaseClockTimePropertiesDSClockTypeIndex=ptpbaseClockTimePropertiesDSClockTypeIndex, ptpbaseClockPortDSPortIdentity=ptpbaseClockPortDSPortIdentity, ptpDomainClockPortsTotal=ptpDomainClockPortsTotal, ptpbaseClockCurrentDSEntry=ptpbaseClockCurrentDSEntry, ptpbaseClockPortAssociatePacketsReceived=ptpbaseClockPortAssociatePacketsReceived, ptpbaseClockDefaultDSDomainIndex=ptpbaseClockDefaultDSDomainIndex, ptpbaseClockPortTransDSEntry=ptpbaseClockPortTransDSEntry, ptpbaseClockTransDefaultDSClockIdentity=ptpbaseClockTransDefaultDSClockIdentity, ptpbaseClockTransDefaultDSNumOfPorts=ptpbaseClockTransDefaultDSNumOfPorts, PtpClockPortNumber=PtpClockPortNumber, ptpbaseClockPortDSClockTypeIndex=ptpbaseClockPortDSClockTypeIndex, ptpbaseClockPortAssociateInErrors=ptpbaseClockPortAssociateInErrors, PtpClockTxModeType=PtpClockTxModeType, ptpClockPortCurrentPortNumberIndex=ptpClockPortCurrentPortNumberIndex, ptpbaseClockTimePropertiesDSFreqTraceable=ptpbaseClockTimePropertiesDSFreqTraceable, ptpbaseSystemTable=ptpbaseSystemTable, ptpbaseClockPortRunningTransport=ptpbaseClockPortRunningTransport, ptpbaseWellKnownEncapsulationTypes=ptpbaseWellKnownEncapsulationTypes, ptpbaseClockTimePropertiesDSDomainIndex=ptpbaseClockTimePropertiesDSDomainIndex, ptpbaseClockDefaultDSClockTypeIndex=ptpbaseClockDefaultDSClockTypeIndex, PtpClockTimeSourceType=PtpClockTimeSourceType, ptpbaseClockPortRunningEncapsulationType=ptpbaseClockPortRunningEncapsulationType, ptpbaseTransportTypeEthernet=ptpbaseTransportTypeEthernet, ptpbaseClockPortDSDomainIndex=ptpbaseClockPortDSDomainIndex, ptpbaseClockDefaultDSEntry=ptpbaseClockDefaultDSEntry, ptpbaseClockPortDSPeerMeanPathDelay=ptpbaseClockPortDSPeerMeanPathDelay, ptpbaseClockTimePropertiesDSPTPTimescale=ptpbaseClockTimePropertiesDSPTPTimescale, ptpbaseClockParentDSTable=ptpbaseClockParentDSTable, PtpClockProfileType=PtpClockProfileType, ptpbaseMIBConformance=ptpbaseMIBConformance, ptpbaseClockPortDSGrantDuration=ptpbaseClockPortDSGrantDuration, ptpbaseClockCurrentDSMeanPathDelay=ptpbaseClockCurrentDSMeanPathDelay, ptpbaseClockPortDSTable=ptpbaseClockPortDSTable, PtpClockMechanismType=PtpClockMechanismType, ptpbaseClockCurrentDSOffsetFromMaster=ptpbaseClockCurrentDSOffsetFromMaster, ptpbaseClockRunningEntry=ptpbaseClockRunningEntry, ptpbaseClockPortRunningPacketsSent=ptpbaseClockPortRunningPacketsSent, PtpClockTimeInterval=PtpClockTimeInterval, ptpbaseClockCurrentDSStepsRemoved=ptpbaseClockCurrentDSStepsRemoved, ptpbaseClockPortRunningEntry=ptpbaseClockPortRunningEntry, ptpbaseClockPortTransDSTable=ptpbaseClockPortTransDSTable, ptpbaseEncapsulationTypeVLAN=ptpbaseEncapsulationTypeVLAN, ptpbaseEncapsulationTypeEthernet=ptpbaseEncapsulationTypeEthernet, ptpbaseSystemDomainTotals=ptpbaseSystemDomainTotals, ptpbaseClockRunningPacketsReceived=ptpbaseClockRunningPacketsReceived, ptpbaseClockPortClockTypeIndex=ptpbaseClockPortClockTypeIndex, ptpbaseClockPortNumOfAssociatedPorts=ptpbaseClockPortNumOfAssociatedPorts, ptpbaseClockDefaultDSQualityOffset=ptpbaseClockDefaultDSQualityOffset, ptpbaseClockPortSyncTwoStep=ptpbaseClockPortSyncTwoStep, ptpbaseMIBClockPortGroup=ptpbaseMIBClockPortGroup, ptpbaseTransportTypeDeviceNET=ptpbaseTransportTypeDeviceNET, ptpbaseClockParentDSGMClockQualityOffset=ptpbaseClockParentDSGMClockQualityOffset, ptpbaseClockPortRunningClockInstanceIndex=ptpbaseClockPortRunningClockInstanceIndex, ptpbaseClockPortTransDSPortIdentity=ptpbaseClockPortTransDSPortIdentity, ptpbaseClockParentDSGMClockQualityAccuracy=ptpbaseClockParentDSGMClockQualityAccuracy, ptpbaseClockTimePropertiesDSTimeTraceable=ptpbaseClockTimePropertiesDSTimeTraceable, ptpbaseSystemDomainEntry=ptpbaseSystemDomainEntry, PtpClockStateType=PtpClockStateType, ptpbaseClockTransDefaultDSEntry=ptpbaseClockTransDefaultDSEntry, ptpbaseMIBSystemInfo=ptpbaseMIBSystemInfo, ptpbaseClockPortDSClockInstanceIndex=ptpbaseClockPortDSClockInstanceIndex, ptpbaseClockPortClockInstanceIndex=ptpbaseClockPortClockInstanceIndex, ptpbaseClockParentDSGMClockIdentity=ptpbaseClockParentDSGMClockIdentity, ptpbaseMIBCompliancesClockPortInfo=ptpbaseMIBCompliancesClockPortInfo, ptpbaseClockPortRole=ptpbaseClockPortRole, ptpbaseClockPortDSlogSyncInterval=ptpbaseClockPortDSlogSyncInterval, ptpbaseClockDefaultDSQualityAccuracy=ptpbaseClockDefaultDSQualityAccuracy, ptpbaseClockPortAssociateTable=ptpbaseClockPortAssociateTable, ptpbaseClockTransDefaultDSInstanceIndex=ptpbaseClockTransDefaultDSInstanceIndex, ptpbaseClockDefaultDSPriority1=ptpbaseClockDefaultDSPriority1, PYSNMP_MODULE_ID=ptpbaseMIB, ptpbaseClockTimePropertiesDSLeap61=ptpbaseClockTimePropertiesDSLeap61, ptpbaseClockPortRunningPortNumberIndex=ptpbaseClockPortRunningPortNumberIndex, ptpbaseClockTimePropertiesDSCurrentUTCOffsetValid=ptpbaseClockTimePropertiesDSCurrentUTCOffsetValid, ptpbaseClockParentDSClockPhChRate=ptpbaseClockParentDSClockPhChRate, ptpbaseClockPortName=ptpbaseClockPortName, ptpbaseClockPortTransDSPortNumberIndex=ptpbaseClockPortTransDSPortNumberIndex, ptpbaseClockPortTransDSFaultyFlag=ptpbaseClockPortTransDSFaultyFlag, ptpbaseSystemEntry=ptpbaseSystemEntry, ptpbaseSystemDomainClockTypeIndex=ptpbaseSystemDomainClockTypeIndex, ptpbaseClockPortCurrentPeerAddressType=ptpbaseClockPortCurrentPeerAddressType, ptpInstanceIndex=ptpInstanceIndex, ptpbaseClockPortDSDelayMech=ptpbaseClockPortDSDelayMech, ptpbaseMIBCompliancesSystemInfo=ptpbaseMIBCompliancesSystemInfo, ptpbaseMIBCompliances=ptpbaseMIBCompliances, ptpbaseClockRunningTable=ptpbaseClockRunningTable, ptpbaseClockParentDSDomainIndex=ptpbaseClockParentDSDomainIndex, ptpbaseClockTimePropertiesDSLeap59=ptpbaseClockTimePropertiesDSLeap59, ptpbaseClockPortRunningPacketsReceived=ptpbaseClockPortRunningPacketsReceived, ptpbaseClockRunningClockTypeIndex=ptpbaseClockRunningClockTypeIndex, ptpbaseClockPortRunningInterfaceIndex=ptpbaseClockPortRunningInterfaceIndex, ptpDomainIndex=ptpDomainIndex, ptpbaseClockTimePropertiesDSInstanceIndex=ptpbaseClockTimePropertiesDSInstanceIndex, ptpbaseClockPortRunningDomainIndex=ptpbaseClockPortRunningDomainIndex, ptpbaseMIBCompliancesClockInfo=ptpbaseMIBCompliancesClockInfo, ptpbaseClockPortCurrentPeerAddress=ptpbaseClockPortCurrentPeerAddress, ptpClockPortCurrentClockTypeIndex=ptpClockPortCurrentClockTypeIndex, ptpbaseClockPortDSlogAnnouncementInterval=ptpbaseClockPortDSlogAnnouncementInterval, ptpbaseClockPortAssociatePacketsSent=ptpbaseClockPortAssociatePacketsSent, ptpbaseClockParentDSGMClockPriority2=ptpbaseClockParentDSGMClockPriority2, ptpbaseClockTransDefaultDSTable=ptpbaseClockTransDefaultDSTable, ptpbaseEncapsulationTypePWUDPIPLSP=ptpbaseEncapsulationTypePWUDPIPLSP, ptpbaseClockPortRunningState=ptpbaseClockPortRunningState, ptpbaseWellKnownTransportTypes=ptpbaseWellKnownTransportTypes, ptpbaseClockTimePropertiesDSTable=ptpbaseClockTimePropertiesDSTable, ptpbaseClockParentDSParentStats=ptpbaseClockParentDSParentStats, ptpbaseClockPortRunningTable=ptpbaseClockPortRunningTable, ptpbaseTransportTypeIPversion6=ptpbaseTransportTypeIPversion6, ptpbaseClockPortRunningTxMode=ptpbaseClockPortRunningTxMode, ptpbaseClockTimePropertiesDSSource=ptpbaseClockTimePropertiesDSSource, ptpbaseClockRunningPacketsSent=ptpbaseClockRunningPacketsSent, ptpbaseClockDefaultDSPriority2=ptpbaseClockDefaultDSPriority2, ptpbaseClockPortAssociateOutErrors=ptpbaseClockPortAssociateOutErrors, ptpbaseMIBClockRunningGroup=ptpbaseMIBClockRunningGroup, ptpbaseMIBObjects=ptpbaseMIBObjects, ptpbaseClockDefaultDSInstanceIndex=ptpbaseClockDefaultDSInstanceIndex, ptpbaseClockPortTransDSInstanceIndex=ptpbaseClockPortTransDSInstanceIndex, ptpbaseClockTransDefaultDSDomainIndex=ptpbaseClockTransDefaultDSDomainIndex, ptpbaseMIBClockTranparentDSGroup=ptpbaseMIBClockTranparentDSGroup, ptpbaseClockTransDefaultDSPrimaryDomain=ptpbaseClockTransDefaultDSPrimaryDomain, ptpbaseClockPortDSPeerDelayReqInterval=ptpbaseClockPortDSPeerDelayReqInterval, ptpbaseClockRunningDomainIndex=ptpbaseClockRunningDomainIndex, ptpbaseClockPortRunningRole=ptpbaseClockPortRunningRole, ptpbaseClockPortDomainIndex=ptpbaseClockPortDomainIndex, ptpbaseMIBClockTimepropertiesGroup=ptpbaseMIBClockTimepropertiesGroup, ptpClockPortCurrentDomainIndex=ptpClockPortCurrentDomainIndex, ptpbaseClockCurrentDSTable=ptpbaseClockCurrentDSTable, ptpbaseClockPortDSPTPVersion=ptpbaseClockPortDSPTPVersion, ptpbaseClockPortAssociateAddressType=ptpbaseClockPortAssociateAddressType, ptpbaseMIBNotifs=ptpbaseMIBNotifs, ptpbaseClockParentDSOffset=ptpbaseClockParentDSOffset, PtpClockPortState=PtpClockPortState, ptpClockPortCurrentClockInstanceIndex=ptpClockPortCurrentClockInstanceIndex, ptpbaseClockRunningInstanceIndex=ptpbaseClockRunningInstanceIndex, ptpbaseClockParentDSInstanceIndex=ptpbaseClockParentDSInstanceIndex, ptpbaseClockPortDSName=ptpbaseClockPortDSName, PtpClockPortTransportTypeAddress=PtpClockPortTransportTypeAddress, ptpbaseMIBClockPortDSGroup=ptpbaseMIBClockPortDSGroup, ptpbaseSystemProfile=ptpbaseSystemProfile, ptpbaseClockTransDefaultDSDelay=ptpbaseClockTransDefaultDSDelay, ptpbaseClockPortAssociateEntry=ptpbaseClockPortAssociateEntry, ptpbaseSystemDomainTable=ptpbaseSystemDomainTable, ptpbaseClockPortTransDSPeerMeanPathDelay=ptpbaseClockPortTransDSPeerMeanPathDelay, ptpbaseClockParentDSEntry=ptpbaseClockParentDSEntry, ptpbaseMIBClockPortAssociateGroup=ptpbaseMIBClockPortAssociateGroup, ptpbaseMIBClockParentDSGroup=ptpbaseMIBClockParentDSGroup, ptpbaseMIBClockInfo=ptpbaseMIBClockInfo, ptpbaseClockPortAssociatePortIndex=ptpbaseClockPortAssociatePortIndex, ptpbaseMIBClockPortTransDSGroup=ptpbaseMIBClockPortTransDSGroup, ptpbaseClockPortTablePortNumberIndex=ptpbaseClockPortTablePortNumberIndex, ptpbaseClockPortTransDSlogMinPdelayReqInt=ptpbaseClockPortTransDSlogMinPdelayReqInt, ptpbaseTransportTypeIEC61158=ptpbaseTransportTypeIEC61158, ptpbaseClockDefaultDSSlaveOnly=ptpbaseClockDefaultDSSlaveOnly, ptpbaseClockPortRunningRxMode=ptpbaseClockPortRunningRxMode, ptpbaseMIBGroups=ptpbaseMIBGroups, ptpbaseClockPortDSPortNumberIndex=ptpbaseClockPortDSPortNumberIndex, ptpbaseClockParentDSClockTypeIndex=ptpbaseClockParentDSClockTypeIndex, PtpClockType=PtpClockType, ptpbaseClockPortRunningClockTypeIndex=ptpbaseClockPortRunningClockTypeIndex, ptpbaseClockPortDSEntry=ptpbaseClockPortDSEntry, ptpbaseClockPortTable=ptpbaseClockPortTable, ptpbaseClockDefaultDSTwoStepFlag=ptpbaseClockDefaultDSTwoStepFlag, ptpbaseClockPortDSAnnounceRctTimeout=ptpbaseClockPortDSAnnounceRctTimeout, ptpbaseMIBClockCurrentDSGroup=ptpbaseMIBClockCurrentDSGroup, ptpbaseMIBSystemInfoGroup=ptpbaseMIBSystemInfoGroup, ptpbaseClockCurrentDSInstanceIndex=ptpbaseClockCurrentDSInstanceIndex, ptpbaseTransportTypeIPversion4=ptpbaseTransportTypeIPversion4, ptpbaseClockTimePropertiesDSCurrentUTCOffset=ptpbaseClockTimePropertiesDSCurrentUTCOffset, ptpbaseEncapsulationTypeUDPIPLSP=ptpbaseEncapsulationTypeUDPIPLSP, ptpbaseMIBCompliancesTransparentClockInfo=ptpbaseMIBCompliancesTransparentClockInfo, PtpClockRoleType=PtpClockRoleType, ptpbaseClockDefaultDSTable=ptpbaseClockDefaultDSTable, PtpClockIdentity=PtpClockIdentity, ptpbaseClockPortAssociateAddress=ptpbaseClockPortAssociateAddress, ptpbaseMIBClockPortRunningGroup=ptpbaseMIBClockPortRunningGroup, PtpClockDomainType=PtpClockDomainType, ptpbaseClockDefaultDSQualityClass=ptpbaseClockDefaultDSQualityClass, ptpbaseClockCurrentDSClockTypeIndex=ptpbaseClockCurrentDSClockTypeIndex, ptpbaseEncapsulationTypePWEthernetLSP=ptpbaseEncapsulationTypePWEthernetLSP, ptpbaseClockPortEntry=ptpbaseClockPortEntry, ptpbaseTransportTypeControlNET=ptpbaseTransportTypeControlNET, ptpbaseMIB=ptpbaseMIB, ptpbaseClockParentDSGMClockQualityClass=ptpbaseClockParentDSGMClockQualityClass, ptpbaseClockDefaultDSClockIdentity=ptpbaseClockDefaultDSClockIdentity)
