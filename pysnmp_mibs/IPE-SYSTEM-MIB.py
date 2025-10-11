# SNMP MIB module (IPE-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nec/IPE-SYSTEM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:53:53 2025
# On host Robs-Air.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(BridgeId,
 Timeout) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId",
    "Timeout")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 Opaque,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class AlarmTypeValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("communicationsAlarm", 1),
          ("qualityOfServiceAlarm", 2),
          ("processingErrorAlarm", 3),
          ("equipmentAlarm", 4),
          ("environmentalAlarm", 5),
          ("integrityViolationAlarm", 6),
          ("operationalViolationAlarm", 7),
          ("physicalViolationAlarm", 8),
          ("securityViolationAlarm", 9),
          ("timeDomainViolationAlarm", 10))
    )



class ProbableCauseValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              500,
              501,
              502,
              503,
              504,
              505,
              506,
              507,
              508,
              509,
              510,
              511,
              512,
              513,
              514,
              515,
              516,
              517,
              518,
              519,
              520,
              521,
              522,
              523,
              524,
              525,
              526,
              527,
              528,
              529,
              530,
              531,
              532,
              533,
              534,
              535,
              536,
              537,
              538,
              539,
              540,
              541,
              542,
              543,
              544,
              545,
              546,
              547,
              548,
              549,
              550,
              551,
              552,
              553,
              554,
              555,
              600,
              601,
              602,
              603,
              604,
              605,
              606,
              607,
              608,
              609,
              610,
              611,
              612,
              613,
              614,
              615,
              1024)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("aIS", 1),
          ("callSetUpFailure", 2),
          ("degradedSignal", 3),
          ("farEndReceiverFailure", 4),
          ("framingError", 5),
          ("lossOfFrame", 6),
          ("lossOfPointer", 7),
          ("lossOfSignal", 8),
          ("payloadTypeMismatch", 9),
          ("transmissionError", 10),
          ("remoteAlarmInterface", 11),
          ("excessiveBER", 12),
          ("pathTraceMismatch", 13),
          ("unavailable", 14),
          ("signalLabelMismatch", 15),
          ("lossOfMultiFrame", 16),
          ("receiveFailure", 17),
          ("transmitFailure", 18),
          ("modulationFailure", 19),
          ("demodulationFailure", 20),
          ("broadcastChannelFailure", 21),
          ("connectionEstablishmentError", 22),
          ("invalidMessageReceived", 23),
          ("localNodeTransmissionError", 24),
          ("remoteNodeTransmissionError", 25),
          ("routingFailure", 26),
          ("backplaneFailure", 51),
          ("dataSetProblem", 52),
          ("equipmentIdentifierDuplication", 53),
          ("externalIFDeviceProblem", 54),
          ("lineCardProblem", 55),
          ("multiplexerProblem", 56),
          ("nEIdentifierDuplication", 57),
          ("powerProblem", 58),
          ("processorProblem", 59),
          ("protectionPathFailure", 60),
          ("receiverFailure", 61),
          ("replaceableUnitMissing", 62),
          ("replaceableUnitTypeMismatch", 63),
          ("synchronizationSourceMismatch", 64),
          ("terminalProblem", 65),
          ("timingProblem", 66),
          ("transmitterFailure", 67),
          ("trunkCardProblem", 68),
          ("replaceableUnitProblem", 69),
          ("realTimeClockFailure", 70),
          ("antennaFailure", 71),
          ("batteryChargingFailure", 72),
          ("diskFailure", 73),
          ("frequencyHoppingFailure", 74),
          ("iODeviceError", 75),
          ("lossOfSynchronisation", 76),
          ("lossOfRedundancy", 77),
          ("powerSupplyFailure", 78),
          ("signalQualityEvaluationFailure", 79),
          ("tranceiverFailure", 80),
          ("protectionMechanismFailure", 81),
          ("protectingResourceFailure", 82),
          ("airCompressorFailure", 101),
          ("airConditioningFailure", 102),
          ("airDryerFailure", 103),
          ("batteryDischarging", 104),
          ("batteryFailure", 105),
          ("commercialPowerFailure", 106),
          ("coolingFanFailure", 107),
          ("engineFailure", 108),
          ("fireDetectorFailure", 109),
          ("fuseFailure", 110),
          ("generatorFailure", 111),
          ("lowBatteryThreshold", 112),
          ("pumpFailure", 113),
          ("rectifierFailure", 114),
          ("rectifierHighVoltage", 115),
          ("rectifierLowFVoltage", 116),
          ("ventilationsSystemFailure", 117),
          ("enclosureDoorOpen", 118),
          ("explosiveGas", 119),
          ("fire", 120),
          ("flood", 121),
          ("highHumidity", 122),
          ("highTemperature", 123),
          ("highWind", 124),
          ("iceBuildUp", 125),
          ("intrusionDetection", 126),
          ("lowFuel", 127),
          ("lowHumidity", 128),
          ("lowCablePressure", 129),
          ("lowTemperatue", 130),
          ("lowWater", 131),
          ("smoke", 132),
          ("toxicGas", 133),
          ("coolingSystemFailure", 134),
          ("externalEquipmentFailure", 135),
          ("externalPointFailure", 136),
          ("storageCapacityProblem", 151),
          ("memoryMismatch", 152),
          ("corruptData", 153),
          ("outOfCPUCycles", 154),
          ("sfwrEnvironmentProblem", 155),
          ("sfwrDownloadFailure", 156),
          ("lossOfRealTimel", 157),
          ("applicationSubsystemFailure", 158),
          ("configurationOrCustomisationError", 159),
          ("databaseInconsistency", 160),
          ("fileError", 161),
          ("outOfMemory", 162),
          ("softwareError", 163),
          ("timeoutExpired", 164),
          ("underlayingResourceUnavailable", 165),
          ("versionMismatch", 166),
          ("bandwidthReduced", 201),
          ("congestion", 202),
          ("excessiveErrorRate", 203),
          ("excessiveResponseTime", 204),
          ("excessiveRetransmissionRate", 205),
          ("reducedLoggingCapability", 206),
          ("systemResourcesOverload", 207),
          ("adapterError", 500),
          ("applicationSubsystemFailture", 501),
          ("bandwidthReducedX733", 502),
          ("callEstablishmentError", 503),
          ("communicationsProtocolError", 504),
          ("communicationsSubsystemFailure", 505),
          ("configurationOrCustomizationError", 506),
          ("congestionX733", 507),
          ("coruptData", 508),
          ("cpuCyclesLimitExceeded", 509),
          ("dataSetOrModemError", 510),
          ("degradedSignalX733", 511),
          ("dteDceInterfaceError", 512),
          ("enclosureDoorOpenX733", 513),
          ("equipmentMalfunction", 514),
          ("excessiveVibration", 515),
          ("fileErrorX733", 516),
          ("fireDetected", 517),
          ("framingErrorX733", 518),
          ("heatingVentCoolingSystemProblem", 519),
          ("humidityUnacceptable", 520),
          ("inputOutputDeviceError", 521),
          ("inputDeviceError", 522),
          ("lanError", 523),
          ("leakDetected", 524),
          ("localNodeTransmissionErrorX733", 525),
          ("lossOfFrameX733", 526),
          ("lossOfSignalX733", 527),
          ("materialSupplyExhausted", 528),
          ("multiplexerProblemX733", 529),
          ("outOfMemoryX733", 530),
          ("ouputDeviceError", 531),
          ("performanceDegraded", 532),
          ("powerProblems", 533),
          ("pressureUnacceptable", 534),
          ("processorProblems", 535),
          ("pumpFailureX733", 536),
          ("queueSizeExceeded", 537),
          ("receiveFailureX733", 538),
          ("receiverFailureX733", 539),
          ("remoteNodeTransmissionErrorX733", 540),
          ("resourceAtOrNearingCapacity", 541),
          ("responseTimeExecessive", 542),
          ("retransmissionRateExcessive", 543),
          ("softwareErrorX733", 544),
          ("softwareProgramAbnormallyTerminated", 545),
          ("softwareProgramError", 546),
          ("storageCapacityProblemX733", 547),
          ("temperatureUnacceptable", 548),
          ("thresholdCrossed", 549),
          ("timingProblemX733", 550),
          ("toxicLeakDetected", 551),
          ("transmitFailureX733", 552),
          ("transmiterFailure", 553),
          ("underlyingResourceUnavailable", 554),
          ("versionMismatchX733", 555),
          ("authenticationFailure", 600),
          ("breachOfConfidentiality", 601),
          ("cableTamper", 602),
          ("delayedInformation", 603),
          ("denialOfService", 604),
          ("duplicateInformation", 605),
          ("informationMissing", 606),
          ("informationModificationDetected", 607),
          ("informationOutOfSequence", 608),
          ("keyExpired", 609),
          ("nonRepudiationFailure", 610),
          ("outOfHoursActivity", 611),
          ("outOfService", 612),
          ("proceduralError", 613),
          ("unauthorizedAccessAttempt", 614),
          ("unexpectedInformation", 615),
          ("other", 1024))
    )



# MIB Managed Objects in the order of their OIDs

_Nec_ObjectIdentity = ObjectIdentity
nec = _Nec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119)
)
_Nec_mib_ObjectIdentity = ObjectIdentity
nec_mib = _Nec_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2)
)
_NecProductDepend_ObjectIdentity = ObjectIdentity
necProductDepend = _NecProductDepend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3)
)
_RadioEquipment_ObjectIdentity = ObjectIdentity
radioEquipment = _RadioEquipment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69)
)
_System1_ObjectIdentity = ObjectIdentity
system1 = _System1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 1)
)
_PmSystem_ObjectIdentity = ObjectIdentity
pmSystem = _PmSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 1, 1)
)


class _SysPmType_Type(Integer32):
    """Custom type sysPmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("typeBranchNE", 13),
          ("typeNormal", 14))
    )


_SysPmType_Type.__name__ = "Integer32"
_SysPmType_Object = MibScalar
sysPmType = _SysPmType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 1, 1, 3),
    _SysPmType_Type()
)
sysPmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPmType.setStatus("current")
_SysPrimaryIpAddress_Type = IpAddress
_SysPrimaryIpAddress_Object = MibScalar
sysPrimaryIpAddress = _SysPrimaryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 1, 1, 5),
    _SysPrimaryIpAddress_Type()
)
sysPrimaryIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPrimaryIpAddress.setStatus("current")
_SysOppositeIpAddress_Type = IpAddress
_SysOppositeIpAddress_Object = MibScalar
sysOppositeIpAddress = _SysOppositeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 1, 1, 9),
    _SysOppositeIpAddress_Type()
)
sysOppositeIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysOppositeIpAddress.setStatus("current")
_SysEquipmentType_Type = Integer32
_SysEquipmentType_Object = MibScalar
sysEquipmentType = _SysEquipmentType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 1, 1, 13),
    _SysEquipmentType_Type()
)
sysEquipmentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysEquipmentType.setStatus("current")
_SysEquipmentConfig_Type = Integer32
_SysEquipmentConfig_Object = MibScalar
sysEquipmentConfig = _SysEquipmentConfig_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 1, 1, 14),
    _SysEquipmentConfig_Type()
)
sysEquipmentConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysEquipmentConfig.setStatus("current")
_System5_ObjectIdentity = ObjectIdentity
system5 = _System5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5)
)
_IpeSystemGroup_ObjectIdentity = ObjectIdentity
ipeSystemGroup = _IpeSystemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1)
)
_IpeSysInfoTable_Object = MibTable
ipeSysInfoTable = _IpeSysInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 1)
)
if mibBuilder.loadTexts:
    ipeSysInfoTable.setStatus("current")
_IpeSysInfoEntry_Object = MibTableRow
ipeSysInfoEntry = _IpeSysInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 1, 1)
)
ipeSysInfoEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeSysInfoIndex"),
)
if mibBuilder.loadTexts:
    ipeSysInfoEntry.setStatus("current")


class _IpeSysInfoIndex_Type(Integer32):
    """Custom type ipeSysInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_IpeSysInfoIndex_Type.__name__ = "Integer32"
_IpeSysInfoIndex_Object = MibTableColumn
ipeSysInfoIndex = _IpeSysInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 1, 1, 1),
    _IpeSysInfoIndex_Type()
)
ipeSysInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeSysInfoIndex.setStatus("current")
_IpeSysInfoNEAddress_Type = IpAddress
_IpeSysInfoNEAddress_Object = MibTableColumn
ipeSysInfoNEAddress = _IpeSysInfoNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 1, 1, 2),
    _IpeSysInfoNEAddress_Type()
)
ipeSysInfoNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeSysInfoNEAddress.setStatus("current")
_IpeSysNeName_Type = DisplayString
_IpeSysNeName_Object = MibTableColumn
ipeSysNeName = _IpeSysNeName_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 1, 1, 3),
    _IpeSysNeName_Type()
)
ipeSysNeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeSysNeName.setStatus("current")
_IpeSysAreaName_Type = DisplayString
_IpeSysAreaName_Object = MibTableColumn
ipeSysAreaName = _IpeSysAreaName_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 1, 1, 4),
    _IpeSysAreaName_Type()
)
ipeSysAreaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeSysAreaName.setStatus("current")
_IpeSysNote_Type = DisplayString
_IpeSysNote_Object = MibTableColumn
ipeSysNote = _IpeSysNote_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 1, 1, 5),
    _IpeSysNote_Type()
)
ipeSysNote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeSysNote.setStatus("current")
_IpeSysPrimaryIpAddress_Type = IpAddress
_IpeSysPrimaryIpAddress_Object = MibTableColumn
ipeSysPrimaryIpAddress = _IpeSysPrimaryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 1, 1, 6),
    _IpeSysPrimaryIpAddress_Type()
)
ipeSysPrimaryIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeSysPrimaryIpAddress.setStatus("current")
_IpeSysSubnetMask_Type = IpAddress
_IpeSysSubnetMask_Object = MibTableColumn
ipeSysSubnetMask = _IpeSysSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 1, 1, 7),
    _IpeSysSubnetMask_Type()
)
ipeSysSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeSysSubnetMask.setStatus("current")
_IpeSysDefaultGateway_Type = IpAddress
_IpeSysDefaultGateway_Object = MibTableColumn
ipeSysDefaultGateway = _IpeSysDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 1, 1, 8),
    _IpeSysDefaultGateway_Type()
)
ipeSysDefaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeSysDefaultGateway.setStatus("current")
_IpeSysMacAddress_Type = MacAddress
_IpeSysMacAddress_Object = MibTableColumn
ipeSysMacAddress = _IpeSysMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 1, 1, 9),
    _IpeSysMacAddress_Type()
)
ipeSysMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeSysMacAddress.setStatus("current")
_IpeSysMibVersion_Type = DisplayString
_IpeSysMibVersion_Object = MibTableColumn
ipeSysMibVersion = _IpeSysMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 1, 1, 10),
    _IpeSysMibVersion_Type()
)
ipeSysMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeSysMibVersion.setStatus("current")
_IpeSysEquipmentType_Type = Integer32
_IpeSysEquipmentType_Object = MibTableColumn
ipeSysEquipmentType = _IpeSysEquipmentType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 1, 1, 11),
    _IpeSysEquipmentType_Type()
)
ipeSysEquipmentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeSysEquipmentType.setStatus("current")


class _IpeSysPmType_Type(Integer32):
    """Custom type ipeSysPmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_IpeSysPmType_Type.__name__ = "Integer32"
_IpeSysPmType_Object = MibTableColumn
ipeSysPmType = _IpeSysPmType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 1, 1, 12),
    _IpeSysPmType_Type()
)
ipeSysPmType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeSysPmType.setStatus("current")
_IpeSysInventoryInfoTable_Object = MibTable
ipeSysInventoryInfoTable = _IpeSysInventoryInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 2)
)
if mibBuilder.loadTexts:
    ipeSysInventoryInfoTable.setStatus("current")
_IpeSysInventoryInfoEntry_Object = MibTableRow
ipeSysInventoryInfoEntry = _IpeSysInventoryInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 2, 1)
)
ipeSysInventoryInfoEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeSysInventoryInfoIndex"),
)
if mibBuilder.loadTexts:
    ipeSysInventoryInfoEntry.setStatus("current")


class _IpeSysInventoryInfoIndex_Type(Integer32):
    """Custom type ipeSysInventoryInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_IpeSysInventoryInfoIndex_Type.__name__ = "Integer32"
_IpeSysInventoryInfoIndex_Object = MibTableColumn
ipeSysInventoryInfoIndex = _IpeSysInventoryInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 2, 1, 1),
    _IpeSysInventoryInfoIndex_Type()
)
ipeSysInventoryInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeSysInventoryInfoIndex.setStatus("current")
_IpeSysInventoryInfoNEAddress_Type = IpAddress
_IpeSysInventoryInfoNEAddress_Object = MibTableColumn
ipeSysInventoryInfoNEAddress = _IpeSysInventoryInfoNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 2, 1, 2),
    _IpeSysInventoryInfoNEAddress_Type()
)
ipeSysInventoryInfoNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeSysInventoryInfoNEAddress.setStatus("current")
_IpeSysInvSoftwareVersion_Type = DisplayString
_IpeSysInvSoftwareVersion_Object = MibTableColumn
ipeSysInvSoftwareVersion = _IpeSysInvSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 2, 1, 3),
    _IpeSysInvSoftwareVersion_Type()
)
ipeSysInvSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeSysInvSoftwareVersion.setStatus("current")
_IpeSysInvSoftwareReleaseDate_Type = DateAndTime
_IpeSysInvSoftwareReleaseDate_Object = MibTableColumn
ipeSysInvSoftwareReleaseDate = _IpeSysInvSoftwareReleaseDate_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 2, 1, 4),
    _IpeSysInvSoftwareReleaseDate_Type()
)
ipeSysInvSoftwareReleaseDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeSysInvSoftwareReleaseDate.setStatus("current")
_IpeSysInvDlSoftwareVersion_Type = DisplayString
_IpeSysInvDlSoftwareVersion_Object = MibTableColumn
ipeSysInvDlSoftwareVersion = _IpeSysInvDlSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 2, 1, 5),
    _IpeSysInvDlSoftwareVersion_Type()
)
ipeSysInvDlSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeSysInvDlSoftwareVersion.setStatus("current")
_IpeSysInvOperationSide_Type = Integer32
_IpeSysInvOperationSide_Object = MibTableColumn
ipeSysInvOperationSide = _IpeSysInvOperationSide_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 2, 1, 6),
    _IpeSysInvOperationSide_Type()
)
ipeSysInvOperationSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeSysInvOperationSide.setStatus("current")
_IpeSysInvStandbySoftwareVersion_Type = DisplayString
_IpeSysInvStandbySoftwareVersion_Object = MibTableColumn
ipeSysInvStandbySoftwareVersion = _IpeSysInvStandbySoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 2, 1, 7),
    _IpeSysInvStandbySoftwareVersion_Type()
)
ipeSysInvStandbySoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeSysInvStandbySoftwareVersion.setStatus("current")
_IpeSysOperationGroup_ObjectIdentity = ObjectIdentity
ipeSysOperationGroup = _IpeSysOperationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 3)
)
_IpeSysOpTimeTable_Object = MibTable
ipeSysOpTimeTable = _IpeSysOpTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ipeSysOpTimeTable.setStatus("current")
_IpeSysOpTimeEntry_Object = MibTableRow
ipeSysOpTimeEntry = _IpeSysOpTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 3, 1, 1)
)
ipeSysOpTimeEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeSysOpTimeIndex"),
)
if mibBuilder.loadTexts:
    ipeSysOpTimeEntry.setStatus("current")


class _IpeSysOpTimeIndex_Type(Integer32):
    """Custom type ipeSysOpTimeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_IpeSysOpTimeIndex_Type.__name__ = "Integer32"
_IpeSysOpTimeIndex_Object = MibTableColumn
ipeSysOpTimeIndex = _IpeSysOpTimeIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 3, 1, 1, 1),
    _IpeSysOpTimeIndex_Type()
)
ipeSysOpTimeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeSysOpTimeIndex.setStatus("current")
_IpeSysOpTimeNEAddress_Type = IpAddress
_IpeSysOpTimeNEAddress_Object = MibTableColumn
ipeSysOpTimeNEAddress = _IpeSysOpTimeNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 3, 1, 1, 2),
    _IpeSysOpTimeNEAddress_Type()
)
ipeSysOpTimeNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeSysOpTimeNEAddress.setStatus("current")
_IpeSysOpCurrentTime_Type = DateAndTime
_IpeSysOpCurrentTime_Object = MibTableColumn
ipeSysOpCurrentTime = _IpeSysOpCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 3, 1, 1, 3),
    _IpeSysOpCurrentTime_Type()
)
ipeSysOpCurrentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeSysOpCurrentTime.setStatus("current")
_IpeSysOpStartTime_Type = DateAndTime
_IpeSysOpStartTime_Object = MibTableColumn
ipeSysOpStartTime = _IpeSysOpStartTime_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 3, 1, 1, 4),
    _IpeSysOpStartTime_Type()
)
ipeSysOpStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeSysOpStartTime.setStatus("current")
_IpeSysOpUpTime_Type = Counter32
_IpeSysOpUpTime_Object = MibTableColumn
ipeSysOpUpTime = _IpeSysOpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 3, 1, 1, 5),
    _IpeSysOpUpTime_Type()
)
ipeSysOpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeSysOpUpTime.setStatus("current")
_IpeSysOpFileDownloadTable_Object = MibTable
ipeSysOpFileDownloadTable = _IpeSysOpFileDownloadTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ipeSysOpFileDownloadTable.setStatus("current")
_IpeSysOpFileDownloadEntry_Object = MibTableRow
ipeSysOpFileDownloadEntry = _IpeSysOpFileDownloadEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 3, 2, 1)
)
ipeSysOpFileDownloadEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeSysOpFileDownloadIndex"),
)
if mibBuilder.loadTexts:
    ipeSysOpFileDownloadEntry.setStatus("current")


class _IpeSysOpFileDownloadIndex_Type(Integer32):
    """Custom type ipeSysOpFileDownloadIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_IpeSysOpFileDownloadIndex_Type.__name__ = "Integer32"
_IpeSysOpFileDownloadIndex_Object = MibTableColumn
ipeSysOpFileDownloadIndex = _IpeSysOpFileDownloadIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 3, 2, 1, 1),
    _IpeSysOpFileDownloadIndex_Type()
)
ipeSysOpFileDownloadIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeSysOpFileDownloadIndex.setStatus("current")
_IpeSysOpFileDownloadNEAddress_Type = IpAddress
_IpeSysOpFileDownloadNEAddress_Object = MibTableColumn
ipeSysOpFileDownloadNEAddress = _IpeSysOpFileDownloadNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 3, 2, 1, 2),
    _IpeSysOpFileDownloadNEAddress_Type()
)
ipeSysOpFileDownloadNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeSysOpFileDownloadNEAddress.setStatus("current")


class _IpeSysOpFileDownloadModule_Type(Integer32):
    """Custom type ipeSysOpFileDownloadModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("idu", 1),
          ("odu", 2),
          ("mdprm", 3),
          ("raFpga", 4),
          ("ipeFpga", 5),
          ("softkey", 7),
          ("cfgNet", 8),
          ("cfgEqu", 9),
          ("cfgUser", 10),
          ("https", 11))
    )


_IpeSysOpFileDownloadModule_Type.__name__ = "Integer32"
_IpeSysOpFileDownloadModule_Object = MibTableColumn
ipeSysOpFileDownloadModule = _IpeSysOpFileDownloadModule_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 3, 2, 1, 3),
    _IpeSysOpFileDownloadModule_Type()
)
ipeSysOpFileDownloadModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeSysOpFileDownloadModule.setStatus("current")


class _IpeSysOpFileDownloadCpuResetDetail_Type(Integer32):
    """Custom type ipeSysOpFileDownloadCpuResetDetail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("revertReset", 1),
          ("normReset", 2))
    )


_IpeSysOpFileDownloadCpuResetDetail_Type.__name__ = "Integer32"
_IpeSysOpFileDownloadCpuResetDetail_Object = MibTableColumn
ipeSysOpFileDownloadCpuResetDetail = _IpeSysOpFileDownloadCpuResetDetail_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 3, 2, 1, 4),
    _IpeSysOpFileDownloadCpuResetDetail_Type()
)
ipeSysOpFileDownloadCpuResetDetail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeSysOpFileDownloadCpuResetDetail.setStatus("current")


class _IpeSysOpFileDownloadStatus_Type(Integer32):
    """Custom type ipeSysOpFileDownloadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("downloadCompleted", 1),
          ("downloadFailed", 2),
          ("downloadExecuting", 3),
          ("downloadSuspending", 4))
    )


_IpeSysOpFileDownloadStatus_Type.__name__ = "Integer32"
_IpeSysOpFileDownloadStatus_Object = MibTableColumn
ipeSysOpFileDownloadStatus = _IpeSysOpFileDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 3, 2, 1, 5),
    _IpeSysOpFileDownloadStatus_Type()
)
ipeSysOpFileDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeSysOpFileDownloadStatus.setStatus("current")


class _IpeSysOpFileDownloadCtrl_Type(Integer32):
    """Custom type ipeSysOpFileDownloadCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("startDownload", 1),
          ("suspendDownload", 2),
          ("startUpload", 3),
          ("endUpload", 4),
          ("resetDownload", 5))
    )


_IpeSysOpFileDownloadCtrl_Type.__name__ = "Integer32"
_IpeSysOpFileDownloadCtrl_Object = MibTableColumn
ipeSysOpFileDownloadCtrl = _IpeSysOpFileDownloadCtrl_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 3, 2, 1, 6),
    _IpeSysOpFileDownloadCtrl_Type()
)
ipeSysOpFileDownloadCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeSysOpFileDownloadCtrl.setStatus("current")


class _IpeSysOpFileDownloadProtocolType_Type(Integer32):
    """Custom type ipeSysOpFileDownloadProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("ftp", 1),
          ("sftp", 2),
          ("http", 3))
    )


_IpeSysOpFileDownloadProtocolType_Type.__name__ = "Integer32"
_IpeSysOpFileDownloadProtocolType_Object = MibTableColumn
ipeSysOpFileDownloadProtocolType = _IpeSysOpFileDownloadProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 3, 2, 1, 7),
    _IpeSysOpFileDownloadProtocolType_Type()
)
ipeSysOpFileDownloadProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeSysOpFileDownloadProtocolType.setStatus("current")
_IpeSysOpProgramPmonRmonClearTable_Object = MibTable
ipeSysOpProgramPmonRmonClearTable = _IpeSysOpProgramPmonRmonClearTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 3, 3)
)
if mibBuilder.loadTexts:
    ipeSysOpProgramPmonRmonClearTable.setStatus("current")
_IpeSysOpProgramPmonRmonClearEntry_Object = MibTableRow
ipeSysOpProgramPmonRmonClearEntry = _IpeSysOpProgramPmonRmonClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 3, 3, 1)
)
ipeSysOpProgramPmonRmonClearEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeSysOpProgramPmonRmonClearIndex"),
)
if mibBuilder.loadTexts:
    ipeSysOpProgramPmonRmonClearEntry.setStatus("current")


class _IpeSysOpProgramPmonRmonClearIndex_Type(Integer32):
    """Custom type ipeSysOpProgramPmonRmonClearIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_IpeSysOpProgramPmonRmonClearIndex_Type.__name__ = "Integer32"
_IpeSysOpProgramPmonRmonClearIndex_Object = MibTableColumn
ipeSysOpProgramPmonRmonClearIndex = _IpeSysOpProgramPmonRmonClearIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 3, 3, 1, 1),
    _IpeSysOpProgramPmonRmonClearIndex_Type()
)
ipeSysOpProgramPmonRmonClearIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeSysOpProgramPmonRmonClearIndex.setStatus("current")
_IpeSysOpProgramPmonRmonClearNEAddress_Type = IpAddress
_IpeSysOpProgramPmonRmonClearNEAddress_Object = MibTableColumn
ipeSysOpProgramPmonRmonClearNEAddress = _IpeSysOpProgramPmonRmonClearNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 3, 3, 1, 2),
    _IpeSysOpProgramPmonRmonClearNEAddress_Type()
)
ipeSysOpProgramPmonRmonClearNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeSysOpProgramPmonRmonClearNEAddress.setStatus("current")
_IpeSysOpProgramPmonRmonClear_Type = Integer32
_IpeSysOpProgramPmonRmonClear_Object = MibTableColumn
ipeSysOpProgramPmonRmonClear = _IpeSysOpProgramPmonRmonClear_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 3, 3, 1, 3),
    _IpeSysOpProgramPmonRmonClear_Type()
)
ipeSysOpProgramPmonRmonClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeSysOpProgramPmonRmonClear.setStatus("current")


class _IpeSysOpProgramPmonRmonClearResult_Type(Integer32):
    """Custom type ipeSysOpProgramPmonRmonClearResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("completed", 1),
          ("failed", 2),
          ("executing", 3))
    )


_IpeSysOpProgramPmonRmonClearResult_Type.__name__ = "Integer32"
_IpeSysOpProgramPmonRmonClearResult_Object = MibTableColumn
ipeSysOpProgramPmonRmonClearResult = _IpeSysOpProgramPmonRmonClearResult_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 1, 3, 3, 1, 4),
    _IpeSysOpProgramPmonRmonClearResult_Type()
)
ipeSysOpProgramPmonRmonClearResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeSysOpProgramPmonRmonClearResult.setStatus("current")
_IpeFileSystemGroup_ObjectIdentity = ObjectIdentity
ipeFileSystemGroup = _IpeFileSystemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 2)
)
_IpeFsFileInfoTable_Object = MibTable
ipeFsFileInfoTable = _IpeFsFileInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 2, 1)
)
if mibBuilder.loadTexts:
    ipeFsFileInfoTable.setStatus("current")
_IpeFsFileInfoEntry_Object = MibTableRow
ipeFsFileInfoEntry = _IpeFsFileInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 2, 1, 1)
)
ipeFsFileInfoEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeFsFileInfoIndex"),
)
if mibBuilder.loadTexts:
    ipeFsFileInfoEntry.setStatus("current")


class _IpeFsFileInfoIndex_Type(Integer32):
    """Custom type ipeFsFileInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_IpeFsFileInfoIndex_Type.__name__ = "Integer32"
_IpeFsFileInfoIndex_Object = MibTableColumn
ipeFsFileInfoIndex = _IpeFsFileInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 2, 1, 1, 1),
    _IpeFsFileInfoIndex_Type()
)
ipeFsFileInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeFsFileInfoIndex.setStatus("current")
_IpeFsFileInfoNEAddress_Type = IpAddress
_IpeFsFileInfoNEAddress_Object = MibTableColumn
ipeFsFileInfoNEAddress = _IpeFsFileInfoNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 2, 1, 1, 2),
    _IpeFsFileInfoNEAddress_Type()
)
ipeFsFileInfoNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeFsFileInfoNEAddress.setStatus("current")


class _IpeFsFileListType_Type(Integer32):
    """Custom type ipeFsFileListType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("idu", 1),
          ("odu", 2),
          ("mdprm", 3),
          ("raFpga", 4),
          ("ipeFpga", 5),
          ("softkey", 7),
          ("cfgNet", 8),
          ("cfgEqu", 9),
          ("cfgUser", 10),
          ("https", 11),
          ("pmon", 12),
          ("rmon", 13),
          ("log", 14),
          ("inventory", 15),
          ("mac", 16),
          ("all", 17))
    )


_IpeFsFileListType_Type.__name__ = "Integer32"
_IpeFsFileListType_Object = MibTableColumn
ipeFsFileListType = _IpeFsFileListType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 2, 1, 1, 3),
    _IpeFsFileListType_Type()
)
ipeFsFileListType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeFsFileListType.setStatus("current")
_IpeFsFileListCurrent_Type = DisplayString
_IpeFsFileListCurrent_Object = MibTableColumn
ipeFsFileListCurrent = _IpeFsFileListCurrent_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 2, 1, 1, 4),
    _IpeFsFileListCurrent_Type()
)
ipeFsFileListCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeFsFileListCurrent.setStatus("current")
_IpeFsFileListTemp_Type = DisplayString
_IpeFsFileListTemp_Object = MibTableColumn
ipeFsFileListTemp = _IpeFsFileListTemp_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 2, 1, 1, 5),
    _IpeFsFileListTemp_Type()
)
ipeFsFileListTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeFsFileListTemp.setStatus("current")
_IpeFsUpdateFileDetail_Type = DisplayString
_IpeFsUpdateFileDetail_Object = MibTableColumn
ipeFsUpdateFileDetail = _IpeFsUpdateFileDetail_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 2, 1, 1, 6),
    _IpeFsUpdateFileDetail_Type()
)
ipeFsUpdateFileDetail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeFsUpdateFileDetail.setStatus("current")


class _IpeFsUpdateFileStatus_Type(Integer32):
    """Custom type ipeFsUpdateFileStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("success", 1),
          ("failure", 2),
          ("executing", 3),
          ("checking", 4),
          ("successWithoutRestrictedUser", 5))
    )


_IpeFsUpdateFileStatus_Type.__name__ = "Integer32"
_IpeFsUpdateFileStatus_Object = MibTableColumn
ipeFsUpdateFileStatus = _IpeFsUpdateFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 2, 1, 1, 7),
    _IpeFsUpdateFileStatus_Type()
)
ipeFsUpdateFileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeFsUpdateFileStatus.setStatus("current")


class _IpeFsUpdateFileStatusDetail_Type(OctetString):
    """Custom type ipeFsUpdateFileStatusDetail based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(42, 42),
    )
    fixed_length = 42


_IpeFsUpdateFileStatusDetail_Type.__name__ = "OctetString"
_IpeFsUpdateFileStatusDetail_Object = MibTableColumn
ipeFsUpdateFileStatusDetail = _IpeFsUpdateFileStatusDetail_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 2, 1, 1, 8),
    _IpeFsUpdateFileStatusDetail_Type()
)
ipeFsUpdateFileStatusDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeFsUpdateFileStatusDetail.setStatus("current")
_IpeFsUpdateFileProgressBase_Type = Integer32
_IpeFsUpdateFileProgressBase_Object = MibTableColumn
ipeFsUpdateFileProgressBase = _IpeFsUpdateFileProgressBase_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 2, 1, 1, 9),
    _IpeFsUpdateFileProgressBase_Type()
)
ipeFsUpdateFileProgressBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeFsUpdateFileProgressBase.setStatus("current")
_IpeFsUpdateFileProgress_Type = Integer32
_IpeFsUpdateFileProgress_Object = MibTableColumn
ipeFsUpdateFileProgress = _IpeFsUpdateFileProgress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 2, 1, 1, 10),
    _IpeFsUpdateFileProgress_Type()
)
ipeFsUpdateFileProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeFsUpdateFileProgress.setStatus("current")
_IpeFsUpdateFileUpdateList_Type = DisplayString
_IpeFsUpdateFileUpdateList_Object = MibTableColumn
ipeFsUpdateFileUpdateList = _IpeFsUpdateFileUpdateList_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 2, 1, 1, 11),
    _IpeFsUpdateFileUpdateList_Type()
)
ipeFsUpdateFileUpdateList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeFsUpdateFileUpdateList.setStatus("current")


class _IpeFsUpdateFileConfigPartial_Type(OctetString):
    """Custom type ipeFsUpdateFileConfigPartial based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_IpeFsUpdateFileConfigPartial_Type.__name__ = "OctetString"
_IpeFsUpdateFileConfigPartial_Object = MibTableColumn
ipeFsUpdateFileConfigPartial = _IpeFsUpdateFileConfigPartial_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 2, 1, 1, 12),
    _IpeFsUpdateFileConfigPartial_Type()
)
ipeFsUpdateFileConfigPartial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeFsUpdateFileConfigPartial.setStatus("current")
_IpeFsUsbInfoTable_Object = MibTable
ipeFsUsbInfoTable = _IpeFsUsbInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 2, 2)
)
if mibBuilder.loadTexts:
    ipeFsUsbInfoTable.setStatus("current")
_IpeFsUsbInfoEntry_Object = MibTableRow
ipeFsUsbInfoEntry = _IpeFsUsbInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 2, 2, 1)
)
ipeFsUsbInfoEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeFsUsbInfoIndex"),
)
if mibBuilder.loadTexts:
    ipeFsUsbInfoEntry.setStatus("current")


class _IpeFsUsbInfoIndex_Type(Integer32):
    """Custom type ipeFsUsbInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_IpeFsUsbInfoIndex_Type.__name__ = "Integer32"
_IpeFsUsbInfoIndex_Object = MibTableColumn
ipeFsUsbInfoIndex = _IpeFsUsbInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 2, 2, 1, 1),
    _IpeFsUsbInfoIndex_Type()
)
ipeFsUsbInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeFsUsbInfoIndex.setStatus("current")
_IpeFsUsbInfoNEAddress_Type = IpAddress
_IpeFsUsbInfoNEAddress_Object = MibTableColumn
ipeFsUsbInfoNEAddress = _IpeFsUsbInfoNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 2, 2, 1, 2),
    _IpeFsUsbInfoNEAddress_Type()
)
ipeFsUsbInfoNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeFsUsbInfoNEAddress.setStatus("current")
_IpeFsUsbCommand_Type = DisplayString
_IpeFsUsbCommand_Object = MibTableColumn
ipeFsUsbCommand = _IpeFsUsbCommand_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 2, 2, 1, 3),
    _IpeFsUsbCommand_Type()
)
ipeFsUsbCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeFsUsbCommand.setStatus("current")


class _IpeFsUsbProcStatus_Type(Integer32):
    """Custom type ipeFsUsbProcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              98,
              99,
              101,
              102,
              103,
              127)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("completed", 1),
          ("executing", 2),
          ("diskFullError", 98),
          ("noSuchFileError", 99),
          ("unKnownFileError", 101),
          ("notInsertError", 102),
          ("accessError", 103),
          ("otherError", 127))
    )


_IpeFsUsbProcStatus_Type.__name__ = "Integer32"
_IpeFsUsbProcStatus_Object = MibTableColumn
ipeFsUsbProcStatus = _IpeFsUsbProcStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 2, 2, 1, 4),
    _IpeFsUsbProcStatus_Type()
)
ipeFsUsbProcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeFsUsbProcStatus.setStatus("current")
_IpeFsUsbList_Type = DisplayString
_IpeFsUsbList_Object = MibTableColumn
ipeFsUsbList = _IpeFsUsbList_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 2, 2, 1, 5),
    _IpeFsUsbList_Type()
)
ipeFsUsbList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeFsUsbList.setStatus("current")


class _IpeFsUsbConnectStatus_Type(Integer32):
    """Custom type ipeFsUsbConnectStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("usbConnect", 1),
          ("usbNoConnect", 2))
    )


_IpeFsUsbConnectStatus_Type.__name__ = "Integer32"
_IpeFsUsbConnectStatus_Object = MibTableColumn
ipeFsUsbConnectStatus = _IpeFsUsbConnectStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 2, 2, 1, 6),
    _IpeFsUsbConnectStatus_Type()
)
ipeFsUsbConnectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeFsUsbConnectStatus.setStatus("current")
_IpeConfigurationGroup_ObjectIdentity = ObjectIdentity
ipeConfigurationGroup = _IpeConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3)
)
_IpeCfgSystemTable_Object = MibTable
ipeCfgSystemTable = _IpeCfgSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 1)
)
if mibBuilder.loadTexts:
    ipeCfgSystemTable.setStatus("current")
_IpeCfgSystemEntry_Object = MibTableRow
ipeCfgSystemEntry = _IpeCfgSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 1, 1)
)
ipeCfgSystemEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeCfgSystemIndex"),
)
if mibBuilder.loadTexts:
    ipeCfgSystemEntry.setStatus("current")


class _IpeCfgSystemIndex_Type(Integer32):
    """Custom type ipeCfgSystemIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_IpeCfgSystemIndex_Type.__name__ = "Integer32"
_IpeCfgSystemIndex_Object = MibTableColumn
ipeCfgSystemIndex = _IpeCfgSystemIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 1, 1, 1),
    _IpeCfgSystemIndex_Type()
)
ipeCfgSystemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgSystemIndex.setStatus("current")
_IpeCfgSystemNEAddress_Type = IpAddress
_IpeCfgSystemNEAddress_Object = MibTableColumn
ipeCfgSystemNEAddress = _IpeCfgSystemNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 1, 1, 2),
    _IpeCfgSystemNEAddress_Type()
)
ipeCfgSystemNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgSystemNEAddress.setStatus("current")
_IpeCfgNeName_Type = DisplayString
_IpeCfgNeName_Object = MibTableColumn
ipeCfgNeName = _IpeCfgNeName_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 1, 1, 3),
    _IpeCfgNeName_Type()
)
ipeCfgNeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgNeName.setStatus("current")
_IpeCfgAreaName_Type = DisplayString
_IpeCfgAreaName_Object = MibTableColumn
ipeCfgAreaName = _IpeCfgAreaName_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 1, 1, 4),
    _IpeCfgAreaName_Type()
)
ipeCfgAreaName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgAreaName.setStatus("current")
_IpeCfgMemo_Type = DisplayString
_IpeCfgMemo_Object = MibTableColumn
ipeCfgMemo = _IpeCfgMemo_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 1, 1, 5),
    _IpeCfgMemo_Type()
)
ipeCfgMemo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgMemo.setStatus("current")
_IpeCfgOemTable_Object = MibTable
ipeCfgOemTable = _IpeCfgOemTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 2)
)
if mibBuilder.loadTexts:
    ipeCfgOemTable.setStatus("current")
_IpeCfgOemEntry_Object = MibTableRow
ipeCfgOemEntry = _IpeCfgOemEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 2, 1)
)
ipeCfgOemEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeCfgOemIndex"),
)
if mibBuilder.loadTexts:
    ipeCfgOemEntry.setStatus("current")


class _IpeCfgOemIndex_Type(Integer32):
    """Custom type ipeCfgOemIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_IpeCfgOemIndex_Type.__name__ = "Integer32"
_IpeCfgOemIndex_Object = MibTableColumn
ipeCfgOemIndex = _IpeCfgOemIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 2, 1, 1),
    _IpeCfgOemIndex_Type()
)
ipeCfgOemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgOemIndex.setStatus("current")
_IpeCfgOemNEAddress_Type = IpAddress
_IpeCfgOemNEAddress_Object = MibTableColumn
ipeCfgOemNEAddress = _IpeCfgOemNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 2, 1, 2),
    _IpeCfgOemNEAddress_Type()
)
ipeCfgOemNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgOemNEAddress.setStatus("current")
_IpeCfgOemSysDescr_Type = DisplayString
_IpeCfgOemSysDescr_Object = MibTableColumn
ipeCfgOemSysDescr = _IpeCfgOemSysDescr_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 2, 1, 3),
    _IpeCfgOemSysDescr_Type()
)
ipeCfgOemSysDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgOemSysDescr.setStatus("current")
_IpeCfgOemSysContact_Type = DisplayString
_IpeCfgOemSysContact_Object = MibTableColumn
ipeCfgOemSysContact = _IpeCfgOemSysContact_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 2, 1, 4),
    _IpeCfgOemSysContact_Type()
)
ipeCfgOemSysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgOemSysContact.setStatus("current")
_IpeCfgOemSysName_Type = DisplayString
_IpeCfgOemSysName_Object = MibTableColumn
ipeCfgOemSysName = _IpeCfgOemSysName_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 2, 1, 5),
    _IpeCfgOemSysName_Type()
)
ipeCfgOemSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgOemSysName.setStatus("current")
_IpeCfgOemSysLocation_Type = DisplayString
_IpeCfgOemSysLocation_Object = MibTableColumn
ipeCfgOemSysLocation = _IpeCfgOemSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 2, 1, 6),
    _IpeCfgOemSysLocation_Type()
)
ipeCfgOemSysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgOemSysLocation.setStatus("current")
_IpeCfgAux_ObjectIdentity = ObjectIdentity
ipeCfgAux = _IpeCfgAux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 3)
)
_IpeCfgAuxInTable_Object = MibTable
ipeCfgAuxInTable = _IpeCfgAuxInTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 3, 1)
)
if mibBuilder.loadTexts:
    ipeCfgAuxInTable.setStatus("current")
_IpeCfgAuxInEntry_Object = MibTableRow
ipeCfgAuxInEntry = _IpeCfgAuxInEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 3, 1, 1)
)
ipeCfgAuxInEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeCfgAuxInIndex"),
)
if mibBuilder.loadTexts:
    ipeCfgAuxInEntry.setStatus("current")
_IpeCfgAuxInIndex_Type = Integer32
_IpeCfgAuxInIndex_Object = MibTableColumn
ipeCfgAuxInIndex = _IpeCfgAuxInIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 3, 1, 1, 1),
    _IpeCfgAuxInIndex_Type()
)
ipeCfgAuxInIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgAuxInIndex.setStatus("current")
_IpeCfgAuxInNEAddress_Type = IpAddress
_IpeCfgAuxInNEAddress_Object = MibTableColumn
ipeCfgAuxInNEAddress = _IpeCfgAuxInNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 3, 1, 1, 2),
    _IpeCfgAuxInNEAddress_Type()
)
ipeCfgAuxInNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgAuxInNEAddress.setStatus("current")


class _IpeCfgAuxInItemName_Type(DisplayString):
    """Custom type ipeCfgAuxInItemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpeCfgAuxInItemName_Type.__name__ = "DisplayString"
_IpeCfgAuxInItemName_Object = MibTableColumn
ipeCfgAuxInItemName = _IpeCfgAuxInItemName_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 3, 1, 1, 3),
    _IpeCfgAuxInItemName_Type()
)
ipeCfgAuxInItemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgAuxInItemName.setStatus("current")


class _IpeCfgAuxInItemType_Type(Integer32):
    """Custom type ipeCfgAuxInItemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarmInOpen", 1),
          ("alarmInClose", 2),
          ("status", 3))
    )


_IpeCfgAuxInItemType_Type.__name__ = "Integer32"
_IpeCfgAuxInItemType_Object = MibTableColumn
ipeCfgAuxInItemType = _IpeCfgAuxInItemType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 3, 1, 1, 4),
    _IpeCfgAuxInItemType_Type()
)
ipeCfgAuxInItemType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgAuxInItemType.setStatus("current")


class _IpeCfgAuxInOpenState_Type(DisplayString):
    """Custom type ipeCfgAuxInOpenState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpeCfgAuxInOpenState_Type.__name__ = "DisplayString"
_IpeCfgAuxInOpenState_Object = MibTableColumn
ipeCfgAuxInOpenState = _IpeCfgAuxInOpenState_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 3, 1, 1, 5),
    _IpeCfgAuxInOpenState_Type()
)
ipeCfgAuxInOpenState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgAuxInOpenState.setStatus("current")


class _IpeCfgAuxInCloseState_Type(DisplayString):
    """Custom type ipeCfgAuxInCloseState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpeCfgAuxInCloseState_Type.__name__ = "DisplayString"
_IpeCfgAuxInCloseState_Object = MibTableColumn
ipeCfgAuxInCloseState = _IpeCfgAuxInCloseState_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 3, 1, 1, 6),
    _IpeCfgAuxInCloseState_Type()
)
ipeCfgAuxInCloseState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgAuxInCloseState.setStatus("current")


class _IpeCfgAuxInSeverity_Type(Integer32):
    """Custom type ipeCfgAuxInSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4))
    )


_IpeCfgAuxInSeverity_Type.__name__ = "Integer32"
_IpeCfgAuxInSeverity_Object = MibTableColumn
ipeCfgAuxInSeverity = _IpeCfgAuxInSeverity_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 3, 1, 1, 7),
    _IpeCfgAuxInSeverity_Type()
)
ipeCfgAuxInSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgAuxInSeverity.setStatus("current")
_IpeCfgAuxInAlarmType_Type = AlarmTypeValue
_IpeCfgAuxInAlarmType_Object = MibTableColumn
ipeCfgAuxInAlarmType = _IpeCfgAuxInAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 3, 1, 1, 8),
    _IpeCfgAuxInAlarmType_Type()
)
ipeCfgAuxInAlarmType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgAuxInAlarmType.setStatus("current")
_IpeCfgAuxInProbableCause_Type = ProbableCauseValue
_IpeCfgAuxInProbableCause_Object = MibTableColumn
ipeCfgAuxInProbableCause = _IpeCfgAuxInProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 3, 1, 1, 9),
    _IpeCfgAuxInProbableCause_Type()
)
ipeCfgAuxInProbableCause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgAuxInProbableCause.setStatus("current")
_IpeCfgAuxOutTable_Object = MibTable
ipeCfgAuxOutTable = _IpeCfgAuxOutTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 3, 2)
)
if mibBuilder.loadTexts:
    ipeCfgAuxOutTable.setStatus("current")
_IpeCfgAuxOutEntry_Object = MibTableRow
ipeCfgAuxOutEntry = _IpeCfgAuxOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 3, 2, 1)
)
ipeCfgAuxOutEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeCfgAuxOutIndex"),
)
if mibBuilder.loadTexts:
    ipeCfgAuxOutEntry.setStatus("current")
_IpeCfgAuxOutIndex_Type = Integer32
_IpeCfgAuxOutIndex_Object = MibTableColumn
ipeCfgAuxOutIndex = _IpeCfgAuxOutIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 3, 2, 1, 1),
    _IpeCfgAuxOutIndex_Type()
)
ipeCfgAuxOutIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgAuxOutIndex.setStatus("current")
_IpeCfgAuxOutNEAddress_Type = IpAddress
_IpeCfgAuxOutNEAddress_Object = MibTableColumn
ipeCfgAuxOutNEAddress = _IpeCfgAuxOutNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 3, 2, 1, 2),
    _IpeCfgAuxOutNEAddress_Type()
)
ipeCfgAuxOutNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgAuxOutNEAddress.setStatus("current")


class _IpeCfgAuxOutItemName_Type(DisplayString):
    """Custom type ipeCfgAuxOutItemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpeCfgAuxOutItemName_Type.__name__ = "DisplayString"
_IpeCfgAuxOutItemName_Object = MibTableColumn
ipeCfgAuxOutItemName = _IpeCfgAuxOutItemName_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 3, 2, 1, 3),
    _IpeCfgAuxOutItemName_Type()
)
ipeCfgAuxOutItemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgAuxOutItemName.setStatus("current")


class _IpeCfgAuxOutOpenState_Type(DisplayString):
    """Custom type ipeCfgAuxOutOpenState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpeCfgAuxOutOpenState_Type.__name__ = "DisplayString"
_IpeCfgAuxOutOpenState_Object = MibTableColumn
ipeCfgAuxOutOpenState = _IpeCfgAuxOutOpenState_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 3, 2, 1, 4),
    _IpeCfgAuxOutOpenState_Type()
)
ipeCfgAuxOutOpenState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgAuxOutOpenState.setStatus("current")


class _IpeCfgAuxOutCloseState_Type(DisplayString):
    """Custom type ipeCfgAuxOutCloseState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpeCfgAuxOutCloseState_Type.__name__ = "DisplayString"
_IpeCfgAuxOutCloseState_Object = MibTableColumn
ipeCfgAuxOutCloseState = _IpeCfgAuxOutCloseState_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 3, 2, 1, 5),
    _IpeCfgAuxOutCloseState_Type()
)
ipeCfgAuxOutCloseState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgAuxOutCloseState.setStatus("current")
_IpeCfgNtp_ObjectIdentity = ObjectIdentity
ipeCfgNtp = _IpeCfgNtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 4)
)
_IpeCfgNtpServiceTable_Object = MibTable
ipeCfgNtpServiceTable = _IpeCfgNtpServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 4, 1)
)
if mibBuilder.loadTexts:
    ipeCfgNtpServiceTable.setStatus("current")
_IpeCfgNtpServiceEntry_Object = MibTableRow
ipeCfgNtpServiceEntry = _IpeCfgNtpServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 4, 1, 1)
)
ipeCfgNtpServiceEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeCfgNtpServiceIndex"),
)
if mibBuilder.loadTexts:
    ipeCfgNtpServiceEntry.setStatus("current")


class _IpeCfgNtpServiceIndex_Type(Integer32):
    """Custom type ipeCfgNtpServiceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_IpeCfgNtpServiceIndex_Type.__name__ = "Integer32"
_IpeCfgNtpServiceIndex_Object = MibTableColumn
ipeCfgNtpServiceIndex = _IpeCfgNtpServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 4, 1, 1, 1),
    _IpeCfgNtpServiceIndex_Type()
)
ipeCfgNtpServiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgNtpServiceIndex.setStatus("current")
_IpeCfgNtpServiceNEAddress_Type = IpAddress
_IpeCfgNtpServiceNEAddress_Object = MibTableColumn
ipeCfgNtpServiceNEAddress = _IpeCfgNtpServiceNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 4, 1, 1, 2),
    _IpeCfgNtpServiceNEAddress_Type()
)
ipeCfgNtpServiceNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgNtpServiceNEAddress.setStatus("current")


class _IpeCfgNtpServiceEnable_Type(Integer32):
    """Custom type ipeCfgNtpServiceEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("disabled", 1),
          ("enabled", 2))
    )


_IpeCfgNtpServiceEnable_Type.__name__ = "Integer32"
_IpeCfgNtpServiceEnable_Object = MibTableColumn
ipeCfgNtpServiceEnable = _IpeCfgNtpServiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 4, 1, 1, 3),
    _IpeCfgNtpServiceEnable_Type()
)
ipeCfgNtpServiceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgNtpServiceEnable.setStatus("current")


class _IpeCfgNtpServerMode_Type(Integer32):
    """Custom type ipeCfgNtpServerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("unicast", 1),
          ("multicast", 2),
          ("disabled", 3))
    )


_IpeCfgNtpServerMode_Type.__name__ = "Integer32"
_IpeCfgNtpServerMode_Object = MibTableColumn
ipeCfgNtpServerMode = _IpeCfgNtpServerMode_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 4, 1, 1, 4),
    _IpeCfgNtpServerMode_Type()
)
ipeCfgNtpServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgNtpServerMode.setStatus("current")


class _IpeCfgNtpClientMode_Type(Integer32):
    """Custom type ipeCfgNtpClientMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("unicast", 1),
          ("multicast", 2),
          ("disabled", 3))
    )


_IpeCfgNtpClientMode_Type.__name__ = "Integer32"
_IpeCfgNtpClientMode_Object = MibTableColumn
ipeCfgNtpClientMode = _IpeCfgNtpClientMode_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 4, 1, 1, 5),
    _IpeCfgNtpClientMode_Type()
)
ipeCfgNtpClientMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgNtpClientMode.setStatus("current")


class _IpeCfgNtpServerStratum_Type(Integer32):
    """Custom type ipeCfgNtpServerStratum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 15),
    )


_IpeCfgNtpServerStratum_Type.__name__ = "Integer32"
_IpeCfgNtpServerStratum_Object = MibTableColumn
ipeCfgNtpServerStratum = _IpeCfgNtpServerStratum_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 4, 1, 1, 6),
    _IpeCfgNtpServerStratum_Type()
)
ipeCfgNtpServerStratum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgNtpServerStratum.setStatus("current")
_IpeCfgNtpServerMulticastPort_Type = Integer32
_IpeCfgNtpServerMulticastPort_Object = MibTableColumn
ipeCfgNtpServerMulticastPort = _IpeCfgNtpServerMulticastPort_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 4, 1, 1, 7),
    _IpeCfgNtpServerMulticastPort_Type()
)
ipeCfgNtpServerMulticastPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgNtpServerMulticastPort.setStatus("current")


class _IpeCfgNtpServerMulticastIntervalTime_Type(Integer32):
    """Custom type ipeCfgNtpServerMulticastIntervalTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 17),
    )


_IpeCfgNtpServerMulticastIntervalTime_Type.__name__ = "Integer32"
_IpeCfgNtpServerMulticastIntervalTime_Object = MibTableColumn
ipeCfgNtpServerMulticastIntervalTime = _IpeCfgNtpServerMulticastIntervalTime_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 4, 1, 1, 8),
    _IpeCfgNtpServerMulticastIntervalTime_Type()
)
ipeCfgNtpServerMulticastIntervalTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgNtpServerMulticastIntervalTime.setStatus("current")
_IpeCfgNtpServerTable_Object = MibTable
ipeCfgNtpServerTable = _IpeCfgNtpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 4, 2)
)
if mibBuilder.loadTexts:
    ipeCfgNtpServerTable.setStatus("current")
_IpeCfgNtpServerEntry_Object = MibTableRow
ipeCfgNtpServerEntry = _IpeCfgNtpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 4, 2, 1)
)
ipeCfgNtpServerEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeCfgNtpServerIndex"),
)
if mibBuilder.loadTexts:
    ipeCfgNtpServerEntry.setStatus("current")


class _IpeCfgNtpServerIndex_Type(Integer32):
    """Custom type ipeCfgNtpServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_IpeCfgNtpServerIndex_Type.__name__ = "Integer32"
_IpeCfgNtpServerIndex_Object = MibTableColumn
ipeCfgNtpServerIndex = _IpeCfgNtpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 4, 2, 1, 1),
    _IpeCfgNtpServerIndex_Type()
)
ipeCfgNtpServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgNtpServerIndex.setStatus("current")
_IpeCfgNtpServerNEAddress_Type = IpAddress
_IpeCfgNtpServerNEAddress_Object = MibTableColumn
ipeCfgNtpServerNEAddress = _IpeCfgNtpServerNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 4, 2, 1, 2),
    _IpeCfgNtpServerNEAddress_Type()
)
ipeCfgNtpServerNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgNtpServerNEAddress.setStatus("current")
_IpeCfgNtpServerAddress_Type = IpAddress
_IpeCfgNtpServerAddress_Object = MibTableColumn
ipeCfgNtpServerAddress = _IpeCfgNtpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 4, 2, 1, 3),
    _IpeCfgNtpServerAddress_Type()
)
ipeCfgNtpServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgNtpServerAddress.setStatus("current")


class _IpeCfgNtpVersion_Type(Integer32):
    """Custom type ipeCfgNtpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 4),
    )


_IpeCfgNtpVersion_Type.__name__ = "Integer32"
_IpeCfgNtpVersion_Object = MibTableColumn
ipeCfgNtpVersion = _IpeCfgNtpVersion_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 4, 2, 1, 4),
    _IpeCfgNtpVersion_Type()
)
ipeCfgNtpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgNtpVersion.setStatus("current")


class _IpeCfgNtpPollTime_Type(Integer32):
    """Custom type ipeCfgNtpPollTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 17),
    )


_IpeCfgNtpPollTime_Type.__name__ = "Integer32"
_IpeCfgNtpPollTime_Object = MibTableColumn
ipeCfgNtpPollTime = _IpeCfgNtpPollTime_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 4, 2, 1, 5),
    _IpeCfgNtpPollTime_Type()
)
ipeCfgNtpPollTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgNtpPollTime.setStatus("current")
_IpeCfgFtp_ObjectIdentity = ObjectIdentity
ipeCfgFtp = _IpeCfgFtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 7)
)
_IpeCfgFtpServerTable_Object = MibTable
ipeCfgFtpServerTable = _IpeCfgFtpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 7, 1)
)
if mibBuilder.loadTexts:
    ipeCfgFtpServerTable.setStatus("current")
_IpeCfgFtpServerEntry_Object = MibTableRow
ipeCfgFtpServerEntry = _IpeCfgFtpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 7, 1, 1)
)
ipeCfgFtpServerEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeCfgFtpServerIndex"),
)
if mibBuilder.loadTexts:
    ipeCfgFtpServerEntry.setStatus("current")


class _IpeCfgFtpServerIndex_Type(Integer32):
    """Custom type ipeCfgFtpServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_IpeCfgFtpServerIndex_Type.__name__ = "Integer32"
_IpeCfgFtpServerIndex_Object = MibTableColumn
ipeCfgFtpServerIndex = _IpeCfgFtpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 7, 1, 1, 1),
    _IpeCfgFtpServerIndex_Type()
)
ipeCfgFtpServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgFtpServerIndex.setStatus("current")
_IpeCfgFtpServerNEAddress_Type = IpAddress
_IpeCfgFtpServerNEAddress_Object = MibTableColumn
ipeCfgFtpServerNEAddress = _IpeCfgFtpServerNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 7, 1, 1, 2),
    _IpeCfgFtpServerNEAddress_Type()
)
ipeCfgFtpServerNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgFtpServerNEAddress.setStatus("current")


class _IpeCfgFtpServerEnable_Type(Integer32):
    """Custom type ipeCfgFtpServerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("serviceDisable", 1),
          ("serviceEnable", 2),
          ("alwaysEnable", 3))
    )


_IpeCfgFtpServerEnable_Type.__name__ = "Integer32"
_IpeCfgFtpServerEnable_Object = MibTableColumn
ipeCfgFtpServerEnable = _IpeCfgFtpServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 7, 1, 1, 3),
    _IpeCfgFtpServerEnable_Type()
)
ipeCfgFtpServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgFtpServerEnable.setStatus("current")


class _IpeCfgFtpServerCommandTcpPort_Type(Integer32):
    """Custom type ipeCfgFtpServerCommandTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpeCfgFtpServerCommandTcpPort_Type.__name__ = "Integer32"
_IpeCfgFtpServerCommandTcpPort_Object = MibTableColumn
ipeCfgFtpServerCommandTcpPort = _IpeCfgFtpServerCommandTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 7, 1, 1, 4),
    _IpeCfgFtpServerCommandTcpPort_Type()
)
ipeCfgFtpServerCommandTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgFtpServerCommandTcpPort.setStatus("current")


class _IpeCfgFtpServerDataTcpPort_Type(Integer32):
    """Custom type ipeCfgFtpServerDataTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpeCfgFtpServerDataTcpPort_Type.__name__ = "Integer32"
_IpeCfgFtpServerDataTcpPort_Object = MibTableColumn
ipeCfgFtpServerDataTcpPort = _IpeCfgFtpServerDataTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 7, 1, 1, 5),
    _IpeCfgFtpServerDataTcpPort_Type()
)
ipeCfgFtpServerDataTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgFtpServerDataTcpPort.setStatus("current")


class _IpeCfgFtpServerMaxSession_Type(Integer32):
    """Custom type ipeCfgFtpServerMaxSession based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_IpeCfgFtpServerMaxSession_Type.__name__ = "Integer32"
_IpeCfgFtpServerMaxSession_Object = MibTableColumn
ipeCfgFtpServerMaxSession = _IpeCfgFtpServerMaxSession_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 7, 1, 1, 6),
    _IpeCfgFtpServerMaxSession_Type()
)
ipeCfgFtpServerMaxSession.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgFtpServerMaxSession.setStatus("current")


class _IpeCfgFtpServerAutoDisable_Type(Integer32):
    """Custom type ipeCfgFtpServerAutoDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("disabled", 1),
          ("enabled", 2))
    )


_IpeCfgFtpServerAutoDisable_Type.__name__ = "Integer32"
_IpeCfgFtpServerAutoDisable_Object = MibTableColumn
ipeCfgFtpServerAutoDisable = _IpeCfgFtpServerAutoDisable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 7, 1, 1, 7),
    _IpeCfgFtpServerAutoDisable_Type()
)
ipeCfgFtpServerAutoDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgFtpServerAutoDisable.setStatus("current")
_IpeCfgSftp_ObjectIdentity = ObjectIdentity
ipeCfgSftp = _IpeCfgSftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 8)
)
_IpeCfgSftpServerTable_Object = MibTable
ipeCfgSftpServerTable = _IpeCfgSftpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 8, 1)
)
if mibBuilder.loadTexts:
    ipeCfgSftpServerTable.setStatus("current")
_IpeCfgSftpServerEntry_Object = MibTableRow
ipeCfgSftpServerEntry = _IpeCfgSftpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 8, 1, 1)
)
ipeCfgSftpServerEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeCfgSftpServerIndex"),
)
if mibBuilder.loadTexts:
    ipeCfgSftpServerEntry.setStatus("current")


class _IpeCfgSftpServerIndex_Type(Integer32):
    """Custom type ipeCfgSftpServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_IpeCfgSftpServerIndex_Type.__name__ = "Integer32"
_IpeCfgSftpServerIndex_Object = MibTableColumn
ipeCfgSftpServerIndex = _IpeCfgSftpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 8, 1, 1, 1),
    _IpeCfgSftpServerIndex_Type()
)
ipeCfgSftpServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgSftpServerIndex.setStatus("current")
_IpeCfgSftpServerNEAddress_Type = IpAddress
_IpeCfgSftpServerNEAddress_Object = MibTableColumn
ipeCfgSftpServerNEAddress = _IpeCfgSftpServerNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 8, 1, 1, 2),
    _IpeCfgSftpServerNEAddress_Type()
)
ipeCfgSftpServerNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgSftpServerNEAddress.setStatus("current")


class _IpeCfgSftpServerEnable_Type(Integer32):
    """Custom type ipeCfgSftpServerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("serviceDisable", 1),
          ("serviceEnable", 2),
          ("alwaysEnable", 3))
    )


_IpeCfgSftpServerEnable_Type.__name__ = "Integer32"
_IpeCfgSftpServerEnable_Object = MibTableColumn
ipeCfgSftpServerEnable = _IpeCfgSftpServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 8, 1, 1, 3),
    _IpeCfgSftpServerEnable_Type()
)
ipeCfgSftpServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgSftpServerEnable.setStatus("current")


class _IpeCfgSftpServerAutoDisable_Type(Integer32):
    """Custom type ipeCfgSftpServerAutoDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("disabled", 1),
          ("enabled", 2))
    )


_IpeCfgSftpServerAutoDisable_Type.__name__ = "Integer32"
_IpeCfgSftpServerAutoDisable_Object = MibTableColumn
ipeCfgSftpServerAutoDisable = _IpeCfgSftpServerAutoDisable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 8, 1, 1, 4),
    _IpeCfgSftpServerAutoDisable_Type()
)
ipeCfgSftpServerAutoDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgSftpServerAutoDisable.setStatus("current")
_IpeCfgHttp_ObjectIdentity = ObjectIdentity
ipeCfgHttp = _IpeCfgHttp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 9)
)
_IpeCfgHttpServerTable_Object = MibTable
ipeCfgHttpServerTable = _IpeCfgHttpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 9, 1)
)
if mibBuilder.loadTexts:
    ipeCfgHttpServerTable.setStatus("current")
_IpeCfgHttpServerEntry_Object = MibTableRow
ipeCfgHttpServerEntry = _IpeCfgHttpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 9, 1, 1)
)
ipeCfgHttpServerEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeCfgHttpServerIndex"),
)
if mibBuilder.loadTexts:
    ipeCfgHttpServerEntry.setStatus("current")


class _IpeCfgHttpServerIndex_Type(Integer32):
    """Custom type ipeCfgHttpServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_IpeCfgHttpServerIndex_Type.__name__ = "Integer32"
_IpeCfgHttpServerIndex_Object = MibTableColumn
ipeCfgHttpServerIndex = _IpeCfgHttpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 9, 1, 1, 1),
    _IpeCfgHttpServerIndex_Type()
)
ipeCfgHttpServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgHttpServerIndex.setStatus("current")
_IpeCfgHttpServerNEAddress_Type = IpAddress
_IpeCfgHttpServerNEAddress_Object = MibTableColumn
ipeCfgHttpServerNEAddress = _IpeCfgHttpServerNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 9, 1, 1, 2),
    _IpeCfgHttpServerNEAddress_Type()
)
ipeCfgHttpServerNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgHttpServerNEAddress.setStatus("current")


class _IpeCfgHttpServerEnable_Type(Integer32):
    """Custom type ipeCfgHttpServerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("disabled", 1),
          ("enabled", 2))
    )


_IpeCfgHttpServerEnable_Type.__name__ = "Integer32"
_IpeCfgHttpServerEnable_Object = MibTableColumn
ipeCfgHttpServerEnable = _IpeCfgHttpServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 9, 1, 1, 3),
    _IpeCfgHttpServerEnable_Type()
)
ipeCfgHttpServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgHttpServerEnable.setStatus("current")


class _IpeCfgHttpServerTcpPort_Type(Integer32):
    """Custom type ipeCfgHttpServerTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpeCfgHttpServerTcpPort_Type.__name__ = "Integer32"
_IpeCfgHttpServerTcpPort_Object = MibTableColumn
ipeCfgHttpServerTcpPort = _IpeCfgHttpServerTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 9, 1, 1, 4),
    _IpeCfgHttpServerTcpPort_Type()
)
ipeCfgHttpServerTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgHttpServerTcpPort.setStatus("current")
_IpeCfgHttps_ObjectIdentity = ObjectIdentity
ipeCfgHttps = _IpeCfgHttps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 10)
)
_IpeCfgHttpsServerTable_Object = MibTable
ipeCfgHttpsServerTable = _IpeCfgHttpsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 10, 1)
)
if mibBuilder.loadTexts:
    ipeCfgHttpsServerTable.setStatus("current")
_IpeCfgHttpsServerEntry_Object = MibTableRow
ipeCfgHttpsServerEntry = _IpeCfgHttpsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 10, 1, 1)
)
ipeCfgHttpsServerEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeCfgHttpsServerIndex"),
)
if mibBuilder.loadTexts:
    ipeCfgHttpsServerEntry.setStatus("current")


class _IpeCfgHttpsServerIndex_Type(Integer32):
    """Custom type ipeCfgHttpsServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_IpeCfgHttpsServerIndex_Type.__name__ = "Integer32"
_IpeCfgHttpsServerIndex_Object = MibTableColumn
ipeCfgHttpsServerIndex = _IpeCfgHttpsServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 10, 1, 1, 1),
    _IpeCfgHttpsServerIndex_Type()
)
ipeCfgHttpsServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgHttpsServerIndex.setStatus("current")
_IpeCfgHttpsServerNEAddress_Type = IpAddress
_IpeCfgHttpsServerNEAddress_Object = MibTableColumn
ipeCfgHttpsServerNEAddress = _IpeCfgHttpsServerNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 10, 1, 1, 2),
    _IpeCfgHttpsServerNEAddress_Type()
)
ipeCfgHttpsServerNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgHttpsServerNEAddress.setStatus("current")


class _IpeCfgHttpsServerEnable_Type(Integer32):
    """Custom type ipeCfgHttpsServerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("disabled", 1),
          ("enabled", 2))
    )


_IpeCfgHttpsServerEnable_Type.__name__ = "Integer32"
_IpeCfgHttpsServerEnable_Object = MibTableColumn
ipeCfgHttpsServerEnable = _IpeCfgHttpsServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 10, 1, 1, 3),
    _IpeCfgHttpsServerEnable_Type()
)
ipeCfgHttpsServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgHttpsServerEnable.setStatus("current")


class _IpeCfgHttpsServerTcpPort_Type(Integer32):
    """Custom type ipeCfgHttpsServerTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpeCfgHttpsServerTcpPort_Type.__name__ = "Integer32"
_IpeCfgHttpsServerTcpPort_Object = MibTableColumn
ipeCfgHttpsServerTcpPort = _IpeCfgHttpsServerTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 10, 1, 1, 4),
    _IpeCfgHttpsServerTcpPort_Type()
)
ipeCfgHttpsServerTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgHttpsServerTcpPort.setStatus("current")
_IpeCfgSnmp_ObjectIdentity = ObjectIdentity
ipeCfgSnmp = _IpeCfgSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 11)
)
_IpeCfgSnmpServerTable_Object = MibTable
ipeCfgSnmpServerTable = _IpeCfgSnmpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 11, 1)
)
if mibBuilder.loadTexts:
    ipeCfgSnmpServerTable.setStatus("current")
_IpeCfgSnmpServerEntry_Object = MibTableRow
ipeCfgSnmpServerEntry = _IpeCfgSnmpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 11, 1, 1)
)
ipeCfgSnmpServerEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeCfgSnmpServerIndex"),
)
if mibBuilder.loadTexts:
    ipeCfgSnmpServerEntry.setStatus("current")


class _IpeCfgSnmpServerIndex_Type(Integer32):
    """Custom type ipeCfgSnmpServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_IpeCfgSnmpServerIndex_Type.__name__ = "Integer32"
_IpeCfgSnmpServerIndex_Object = MibTableColumn
ipeCfgSnmpServerIndex = _IpeCfgSnmpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 11, 1, 1, 1),
    _IpeCfgSnmpServerIndex_Type()
)
ipeCfgSnmpServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgSnmpServerIndex.setStatus("current")
_IpeCfgSnmpServerNEAddress_Type = IpAddress
_IpeCfgSnmpServerNEAddress_Object = MibTableColumn
ipeCfgSnmpServerNEAddress = _IpeCfgSnmpServerNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 11, 1, 1, 2),
    _IpeCfgSnmpServerNEAddress_Type()
)
ipeCfgSnmpServerNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgSnmpServerNEAddress.setStatus("current")


class _IpeCfgSnmpV1V2cEnable_Type(Integer32):
    """Custom type ipeCfgSnmpV1V2cEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("disabled", 1),
          ("enabled", 2))
    )


_IpeCfgSnmpV1V2cEnable_Type.__name__ = "Integer32"
_IpeCfgSnmpV1V2cEnable_Object = MibTableColumn
ipeCfgSnmpV1V2cEnable = _IpeCfgSnmpV1V2cEnable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 11, 1, 1, 3),
    _IpeCfgSnmpV1V2cEnable_Type()
)
ipeCfgSnmpV1V2cEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgSnmpV1V2cEnable.setStatus("current")


class _IpeCfgSnmpV3Enable_Type(Integer32):
    """Custom type ipeCfgSnmpV3Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("disabled", 1),
          ("enabled", 2))
    )


_IpeCfgSnmpV3Enable_Type.__name__ = "Integer32"
_IpeCfgSnmpV3Enable_Object = MibTableColumn
ipeCfgSnmpV3Enable = _IpeCfgSnmpV3Enable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 11, 1, 1, 4),
    _IpeCfgSnmpV3Enable_Type()
)
ipeCfgSnmpV3Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgSnmpV3Enable.setStatus("current")


class _IpeCfgSnmpServerPort_Type(Integer32):
    """Custom type ipeCfgSnmpServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpeCfgSnmpServerPort_Type.__name__ = "Integer32"
_IpeCfgSnmpServerPort_Object = MibTableColumn
ipeCfgSnmpServerPort = _IpeCfgSnmpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 11, 1, 1, 5),
    _IpeCfgSnmpServerPort_Type()
)
ipeCfgSnmpServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgSnmpServerPort.setStatus("current")
_IpeCfgSnmpCommunityTable_Object = MibTable
ipeCfgSnmpCommunityTable = _IpeCfgSnmpCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 11, 2)
)
if mibBuilder.loadTexts:
    ipeCfgSnmpCommunityTable.setStatus("current")
_IpeCfgSnmpCommunityEntry_Object = MibTableRow
ipeCfgSnmpCommunityEntry = _IpeCfgSnmpCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 11, 2, 1)
)
ipeCfgSnmpCommunityEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeCfgSnmpCommunityIndex"),
)
if mibBuilder.loadTexts:
    ipeCfgSnmpCommunityEntry.setStatus("current")


class _IpeCfgSnmpCommunityIndex_Type(Integer32):
    """Custom type ipeCfgSnmpCommunityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_IpeCfgSnmpCommunityIndex_Type.__name__ = "Integer32"
_IpeCfgSnmpCommunityIndex_Object = MibTableColumn
ipeCfgSnmpCommunityIndex = _IpeCfgSnmpCommunityIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 11, 2, 1, 1),
    _IpeCfgSnmpCommunityIndex_Type()
)
ipeCfgSnmpCommunityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgSnmpCommunityIndex.setStatus("current")
_IpeCfgSnmpCommunityNEAddress_Type = IpAddress
_IpeCfgSnmpCommunityNEAddress_Object = MibTableColumn
ipeCfgSnmpCommunityNEAddress = _IpeCfgSnmpCommunityNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 11, 2, 1, 2),
    _IpeCfgSnmpCommunityNEAddress_Type()
)
ipeCfgSnmpCommunityNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgSnmpCommunityNEAddress.setStatus("current")


class _IpeCfgSnmpCommunityName_Type(DisplayString):
    """Custom type ipeCfgSnmpCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_IpeCfgSnmpCommunityName_Type.__name__ = "DisplayString"
_IpeCfgSnmpCommunityName_Object = MibTableColumn
ipeCfgSnmpCommunityName = _IpeCfgSnmpCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 11, 2, 1, 3),
    _IpeCfgSnmpCommunityName_Type()
)
ipeCfgSnmpCommunityName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgSnmpCommunityName.setStatus("current")


class _IpeCfgSnmpCommunityAccessLevel_Type(Integer32):
    """Custom type ipeCfgSnmpCommunityAccessLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("operatorLevel", 1),
          ("configLevel", 2),
          ("adminLevel", 3))
    )


_IpeCfgSnmpCommunityAccessLevel_Type.__name__ = "Integer32"
_IpeCfgSnmpCommunityAccessLevel_Object = MibTableColumn
ipeCfgSnmpCommunityAccessLevel = _IpeCfgSnmpCommunityAccessLevel_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 11, 2, 1, 4),
    _IpeCfgSnmpCommunityAccessLevel_Type()
)
ipeCfgSnmpCommunityAccessLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgSnmpCommunityAccessLevel.setStatus("current")
_IpeCfgSnmpCommunityAccessAddress_Type = IpAddress
_IpeCfgSnmpCommunityAccessAddress_Object = MibTableColumn
ipeCfgSnmpCommunityAccessAddress = _IpeCfgSnmpCommunityAccessAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 11, 2, 1, 5),
    _IpeCfgSnmpCommunityAccessAddress_Type()
)
ipeCfgSnmpCommunityAccessAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgSnmpCommunityAccessAddress.setStatus("current")


class _IpeCfgSnmpCommunityAccessPrefixLength_Type(Integer32):
    """Custom type ipeCfgSnmpCommunityAccessPrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_IpeCfgSnmpCommunityAccessPrefixLength_Type.__name__ = "Integer32"
_IpeCfgSnmpCommunityAccessPrefixLength_Object = MibTableColumn
ipeCfgSnmpCommunityAccessPrefixLength = _IpeCfgSnmpCommunityAccessPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 11, 2, 1, 6),
    _IpeCfgSnmpCommunityAccessPrefixLength_Type()
)
ipeCfgSnmpCommunityAccessPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgSnmpCommunityAccessPrefixLength.setStatus("current")


class _IpeCfgSnmpCommunityRowStatus_Type(RowStatus):
    """Custom type ipeCfgSnmpCommunityRowStatus based on RowStatus"""
    subtypeSpec = RowStatus.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("destroy", 6))
    )


_IpeCfgSnmpCommunityRowStatus_Type.__name__ = "RowStatus"
_IpeCfgSnmpCommunityRowStatus_Object = MibTableColumn
ipeCfgSnmpCommunityRowStatus = _IpeCfgSnmpCommunityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 11, 2, 1, 7),
    _IpeCfgSnmpCommunityRowStatus_Type()
)
ipeCfgSnmpCommunityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgSnmpCommunityRowStatus.setStatus("current")
_IpeCfgSnmpTrapTable_Object = MibTable
ipeCfgSnmpTrapTable = _IpeCfgSnmpTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 11, 3)
)
if mibBuilder.loadTexts:
    ipeCfgSnmpTrapTable.setStatus("current")
_IpeCfgSnmpTrapEntry_Object = MibTableRow
ipeCfgSnmpTrapEntry = _IpeCfgSnmpTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 11, 3, 1)
)
ipeCfgSnmpTrapEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeCfgSnmpTrapEntryIndex"),
)
if mibBuilder.loadTexts:
    ipeCfgSnmpTrapEntry.setStatus("current")


class _IpeCfgSnmpTrapEntryIndex_Type(Integer32):
    """Custom type ipeCfgSnmpTrapEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_IpeCfgSnmpTrapEntryIndex_Type.__name__ = "Integer32"
_IpeCfgSnmpTrapEntryIndex_Object = MibTableColumn
ipeCfgSnmpTrapEntryIndex = _IpeCfgSnmpTrapEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 11, 3, 1, 1),
    _IpeCfgSnmpTrapEntryIndex_Type()
)
ipeCfgSnmpTrapEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgSnmpTrapEntryIndex.setStatus("current")
_IpeCfgSnmpTrapEntryNEAddress_Type = IpAddress
_IpeCfgSnmpTrapEntryNEAddress_Object = MibTableColumn
ipeCfgSnmpTrapEntryNEAddress = _IpeCfgSnmpTrapEntryNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 11, 3, 1, 2),
    _IpeCfgSnmpTrapEntryNEAddress_Type()
)
ipeCfgSnmpTrapEntryNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgSnmpTrapEntryNEAddress.setStatus("current")


class _IpeCfgSnmpTrapVersion_Type(Integer32):
    """Custom type ipeCfgSnmpTrapVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("v1", 1),
          ("v2c", 2),
          ("v3", 3))
    )


_IpeCfgSnmpTrapVersion_Type.__name__ = "Integer32"
_IpeCfgSnmpTrapVersion_Object = MibTableColumn
ipeCfgSnmpTrapVersion = _IpeCfgSnmpTrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 11, 3, 1, 3),
    _IpeCfgSnmpTrapVersion_Type()
)
ipeCfgSnmpTrapVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgSnmpTrapVersion.setStatus("current")


class _IpeCfgSnmpTrapNotifyType_Type(Integer32):
    """Custom type ipeCfgSnmpTrapNotifyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("trap", 1),
          ("inform", 2))
    )


_IpeCfgSnmpTrapNotifyType_Type.__name__ = "Integer32"
_IpeCfgSnmpTrapNotifyType_Object = MibTableColumn
ipeCfgSnmpTrapNotifyType = _IpeCfgSnmpTrapNotifyType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 11, 3, 1, 4),
    _IpeCfgSnmpTrapNotifyType_Type()
)
ipeCfgSnmpTrapNotifyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgSnmpTrapNotifyType.setStatus("current")
_IpeCfgSnmpTrapTargetAddress_Type = IpAddress
_IpeCfgSnmpTrapTargetAddress_Object = MibTableColumn
ipeCfgSnmpTrapTargetAddress = _IpeCfgSnmpTrapTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 11, 3, 1, 5),
    _IpeCfgSnmpTrapTargetAddress_Type()
)
ipeCfgSnmpTrapTargetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgSnmpTrapTargetAddress.setStatus("current")


class _IpeCfgSnmpTrapTargetPort_Type(Integer32):
    """Custom type ipeCfgSnmpTrapTargetPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpeCfgSnmpTrapTargetPort_Type.__name__ = "Integer32"
_IpeCfgSnmpTrapTargetPort_Object = MibTableColumn
ipeCfgSnmpTrapTargetPort = _IpeCfgSnmpTrapTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 11, 3, 1, 6),
    _IpeCfgSnmpTrapTargetPort_Type()
)
ipeCfgSnmpTrapTargetPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgSnmpTrapTargetPort.setStatus("current")


class _IpeCfgSnmpTrapSecurityName_Type(DisplayString):
    """Custom type ipeCfgSnmpTrapSecurityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_IpeCfgSnmpTrapSecurityName_Type.__name__ = "DisplayString"
_IpeCfgSnmpTrapSecurityName_Object = MibTableColumn
ipeCfgSnmpTrapSecurityName = _IpeCfgSnmpTrapSecurityName_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 11, 3, 1, 7),
    _IpeCfgSnmpTrapSecurityName_Type()
)
ipeCfgSnmpTrapSecurityName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgSnmpTrapSecurityName.setStatus("current")


class _IpeCfgSnmpTrapSecurityLevel_Type(Integer32):
    """Custom type ipeCfgSnmpTrapSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("noAuthNoPriv", 1),
          ("authNoPriv", 2),
          ("authPriv", 3))
    )


_IpeCfgSnmpTrapSecurityLevel_Type.__name__ = "Integer32"
_IpeCfgSnmpTrapSecurityLevel_Object = MibTableColumn
ipeCfgSnmpTrapSecurityLevel = _IpeCfgSnmpTrapSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 11, 3, 1, 8),
    _IpeCfgSnmpTrapSecurityLevel_Type()
)
ipeCfgSnmpTrapSecurityLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgSnmpTrapSecurityLevel.setStatus("current")


class _IpeCfgSnmpTrapEngineId_Type(OctetString):
    """Custom type ipeCfgSnmpTrapEngineId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 32),
    )


_IpeCfgSnmpTrapEngineId_Type.__name__ = "OctetString"
_IpeCfgSnmpTrapEngineId_Object = MibTableColumn
ipeCfgSnmpTrapEngineId = _IpeCfgSnmpTrapEngineId_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 11, 3, 1, 9),
    _IpeCfgSnmpTrapEngineId_Type()
)
ipeCfgSnmpTrapEngineId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgSnmpTrapEngineId.setStatus("current")


class _IpeCfgSnmpTrapAuthAlgorithm_Type(Integer32):
    """Custom type ipeCfgSnmpTrapAuthAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("md5", 1),
          ("sha", 2))
    )


_IpeCfgSnmpTrapAuthAlgorithm_Type.__name__ = "Integer32"
_IpeCfgSnmpTrapAuthAlgorithm_Object = MibTableColumn
ipeCfgSnmpTrapAuthAlgorithm = _IpeCfgSnmpTrapAuthAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 11, 3, 1, 10),
    _IpeCfgSnmpTrapAuthAlgorithm_Type()
)
ipeCfgSnmpTrapAuthAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgSnmpTrapAuthAlgorithm.setStatus("current")


class _IpeCfgSnmpTrapAuthKey_Type(DisplayString):
    """Custom type ipeCfgSnmpTrapAuthKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 128),
    )


_IpeCfgSnmpTrapAuthKey_Type.__name__ = "DisplayString"
_IpeCfgSnmpTrapAuthKey_Object = MibTableColumn
ipeCfgSnmpTrapAuthKey = _IpeCfgSnmpTrapAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 11, 3, 1, 11),
    _IpeCfgSnmpTrapAuthKey_Type()
)
ipeCfgSnmpTrapAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgSnmpTrapAuthKey.setStatus("current")


class _IpeCfgSnmpTrapPrivAlgorithm_Type(Integer32):
    """Custom type ipeCfgSnmpTrapPrivAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("des", 1),
          ("aes", 2))
    )


_IpeCfgSnmpTrapPrivAlgorithm_Type.__name__ = "Integer32"
_IpeCfgSnmpTrapPrivAlgorithm_Object = MibTableColumn
ipeCfgSnmpTrapPrivAlgorithm = _IpeCfgSnmpTrapPrivAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 11, 3, 1, 12),
    _IpeCfgSnmpTrapPrivAlgorithm_Type()
)
ipeCfgSnmpTrapPrivAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgSnmpTrapPrivAlgorithm.setStatus("current")


class _IpeCfgSnmpTrapPrivKey_Type(DisplayString):
    """Custom type ipeCfgSnmpTrapPrivKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 128),
    )


_IpeCfgSnmpTrapPrivKey_Type.__name__ = "DisplayString"
_IpeCfgSnmpTrapPrivKey_Object = MibTableColumn
ipeCfgSnmpTrapPrivKey = _IpeCfgSnmpTrapPrivKey_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 11, 3, 1, 13),
    _IpeCfgSnmpTrapPrivKey_Type()
)
ipeCfgSnmpTrapPrivKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgSnmpTrapPrivKey.setStatus("current")


class _IpeCfgSnmpTrapRowStatus_Type(RowStatus):
    """Custom type ipeCfgSnmpTrapRowStatus based on RowStatus"""
    subtypeSpec = RowStatus.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("destroy", 6))
    )


_IpeCfgSnmpTrapRowStatus_Type.__name__ = "RowStatus"
_IpeCfgSnmpTrapRowStatus_Object = MibTableColumn
ipeCfgSnmpTrapRowStatus = _IpeCfgSnmpTrapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 11, 3, 1, 14),
    _IpeCfgSnmpTrapRowStatus_Type()
)
ipeCfgSnmpTrapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgSnmpTrapRowStatus.setStatus("current")
_IpeCfgAccount_ObjectIdentity = ObjectIdentity
ipeCfgAccount = _IpeCfgAccount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 12)
)
_IpeCfgAccountUserInfoTable_Object = MibTable
ipeCfgAccountUserInfoTable = _IpeCfgAccountUserInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 12, 1)
)
if mibBuilder.loadTexts:
    ipeCfgAccountUserInfoTable.setStatus("current")
_IpeCfgAccountUserInfoEntry_Object = MibTableRow
ipeCfgAccountUserInfoEntry = _IpeCfgAccountUserInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 12, 1, 1)
)
ipeCfgAccountUserInfoEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeCfgAccountUserIndex"),
)
if mibBuilder.loadTexts:
    ipeCfgAccountUserInfoEntry.setStatus("current")


class _IpeCfgAccountUserIndex_Type(Integer32):
    """Custom type ipeCfgAccountUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 102),
    )


_IpeCfgAccountUserIndex_Type.__name__ = "Integer32"
_IpeCfgAccountUserIndex_Object = MibTableColumn
ipeCfgAccountUserIndex = _IpeCfgAccountUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 12, 1, 1, 1),
    _IpeCfgAccountUserIndex_Type()
)
ipeCfgAccountUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgAccountUserIndex.setStatus("current")
_IpeCfgAccountUserNEAddress_Type = IpAddress
_IpeCfgAccountUserNEAddress_Object = MibTableColumn
ipeCfgAccountUserNEAddress = _IpeCfgAccountUserNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 12, 1, 1, 2),
    _IpeCfgAccountUserNEAddress_Type()
)
ipeCfgAccountUserNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgAccountUserNEAddress.setStatus("current")


class _IpeCfgAccountUserName_Type(DisplayString):
    """Custom type ipeCfgAccountUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_IpeCfgAccountUserName_Type.__name__ = "DisplayString"
_IpeCfgAccountUserName_Object = MibTableColumn
ipeCfgAccountUserName = _IpeCfgAccountUserName_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 12, 1, 1, 3),
    _IpeCfgAccountUserName_Type()
)
ipeCfgAccountUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgAccountUserName.setStatus("current")


class _IpeCfgAccountUserKey_Type(DisplayString):
    """Custom type ipeCfgAccountUserKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 128),
    )


_IpeCfgAccountUserKey_Type.__name__ = "DisplayString"
_IpeCfgAccountUserKey_Object = MibTableColumn
ipeCfgAccountUserKey = _IpeCfgAccountUserKey_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 12, 1, 1, 4),
    _IpeCfgAccountUserKey_Type()
)
ipeCfgAccountUserKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgAccountUserKey.setStatus("current")


class _IpeCfgAccountUserGroup_Type(DisplayString):
    """Custom type ipeCfgAccountUserGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_IpeCfgAccountUserGroup_Type.__name__ = "DisplayString"
_IpeCfgAccountUserGroup_Object = MibTableColumn
ipeCfgAccountUserGroup = _IpeCfgAccountUserGroup_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 12, 1, 1, 5),
    _IpeCfgAccountUserGroup_Type()
)
ipeCfgAccountUserGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgAccountUserGroup.setStatus("current")


class _IpeCfgAccountUserSnmpV3SecurityLevel_Type(Integer32):
    """Custom type ipeCfgAccountUserSnmpV3SecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("noAuthNoPriv", 1),
          ("authNoPriv", 2),
          ("authPriv", 3))
    )


_IpeCfgAccountUserSnmpV3SecurityLevel_Type.__name__ = "Integer32"
_IpeCfgAccountUserSnmpV3SecurityLevel_Object = MibTableColumn
ipeCfgAccountUserSnmpV3SecurityLevel = _IpeCfgAccountUserSnmpV3SecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 12, 1, 1, 6),
    _IpeCfgAccountUserSnmpV3SecurityLevel_Type()
)
ipeCfgAccountUserSnmpV3SecurityLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgAccountUserSnmpV3SecurityLevel.setStatus("current")


class _IpeCfgAccountUserSnmpV3AuthAlgorithm_Type(Integer32):
    """Custom type ipeCfgAccountUserSnmpV3AuthAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("md5", 1),
          ("sha", 2))
    )


_IpeCfgAccountUserSnmpV3AuthAlgorithm_Type.__name__ = "Integer32"
_IpeCfgAccountUserSnmpV3AuthAlgorithm_Object = MibTableColumn
ipeCfgAccountUserSnmpV3AuthAlgorithm = _IpeCfgAccountUserSnmpV3AuthAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 12, 1, 1, 7),
    _IpeCfgAccountUserSnmpV3AuthAlgorithm_Type()
)
ipeCfgAccountUserSnmpV3AuthAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgAccountUserSnmpV3AuthAlgorithm.setStatus("current")


class _IpeCfgAccountUserSnmpV3AuthKey_Type(DisplayString):
    """Custom type ipeCfgAccountUserSnmpV3AuthKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 128),
    )


_IpeCfgAccountUserSnmpV3AuthKey_Type.__name__ = "DisplayString"
_IpeCfgAccountUserSnmpV3AuthKey_Object = MibTableColumn
ipeCfgAccountUserSnmpV3AuthKey = _IpeCfgAccountUserSnmpV3AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 12, 1, 1, 8),
    _IpeCfgAccountUserSnmpV3AuthKey_Type()
)
ipeCfgAccountUserSnmpV3AuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgAccountUserSnmpV3AuthKey.setStatus("current")


class _IpeCfgAccountUserSnmpV3PrivAlgorithm_Type(Integer32):
    """Custom type ipeCfgAccountUserSnmpV3PrivAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("des", 1),
          ("aes", 2))
    )


_IpeCfgAccountUserSnmpV3PrivAlgorithm_Type.__name__ = "Integer32"
_IpeCfgAccountUserSnmpV3PrivAlgorithm_Object = MibTableColumn
ipeCfgAccountUserSnmpV3PrivAlgorithm = _IpeCfgAccountUserSnmpV3PrivAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 12, 1, 1, 9),
    _IpeCfgAccountUserSnmpV3PrivAlgorithm_Type()
)
ipeCfgAccountUserSnmpV3PrivAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgAccountUserSnmpV3PrivAlgorithm.setStatus("current")


class _IpeCfgAccountUserSnmpV3PrivKey_Type(DisplayString):
    """Custom type ipeCfgAccountUserSnmpV3PrivKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 128),
    )


_IpeCfgAccountUserSnmpV3PrivKey_Type.__name__ = "DisplayString"
_IpeCfgAccountUserSnmpV3PrivKey_Object = MibTableColumn
ipeCfgAccountUserSnmpV3PrivKey = _IpeCfgAccountUserSnmpV3PrivKey_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 12, 1, 1, 10),
    _IpeCfgAccountUserSnmpV3PrivKey_Type()
)
ipeCfgAccountUserSnmpV3PrivKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgAccountUserSnmpV3PrivKey.setStatus("current")


class _IpeCfgAccountUserRowStatus_Type(RowStatus):
    """Custom type ipeCfgAccountUserRowStatus based on RowStatus"""
    subtypeSpec = RowStatus.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("destroy", 6))
    )


_IpeCfgAccountUserRowStatus_Type.__name__ = "RowStatus"
_IpeCfgAccountUserRowStatus_Object = MibTableColumn
ipeCfgAccountUserRowStatus = _IpeCfgAccountUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 12, 1, 1, 11),
    _IpeCfgAccountUserRowStatus_Type()
)
ipeCfgAccountUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgAccountUserRowStatus.setStatus("current")
_IpeCfgAccountGroupInfoTable_Object = MibTable
ipeCfgAccountGroupInfoTable = _IpeCfgAccountGroupInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 12, 2)
)
if mibBuilder.loadTexts:
    ipeCfgAccountGroupInfoTable.setStatus("current")
_IpeCfgAccountGroupInfoEntry_Object = MibTableRow
ipeCfgAccountGroupInfoEntry = _IpeCfgAccountGroupInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 12, 2, 1)
)
ipeCfgAccountGroupInfoEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeCfgAccountGroupIndex"),
)
if mibBuilder.loadTexts:
    ipeCfgAccountGroupInfoEntry.setStatus("current")


class _IpeCfgAccountGroupIndex_Type(Integer32):
    """Custom type ipeCfgAccountGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_IpeCfgAccountGroupIndex_Type.__name__ = "Integer32"
_IpeCfgAccountGroupIndex_Object = MibTableColumn
ipeCfgAccountGroupIndex = _IpeCfgAccountGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 12, 2, 1, 1),
    _IpeCfgAccountGroupIndex_Type()
)
ipeCfgAccountGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgAccountGroupIndex.setStatus("current")
_IpeCfgAccountGroupNEAddress_Type = IpAddress
_IpeCfgAccountGroupNEAddress_Object = MibTableColumn
ipeCfgAccountGroupNEAddress = _IpeCfgAccountGroupNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 12, 2, 1, 2),
    _IpeCfgAccountGroupNEAddress_Type()
)
ipeCfgAccountGroupNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgAccountGroupNEAddress.setStatus("current")


class _IpeCfgAccountGroupName_Type(DisplayString):
    """Custom type ipeCfgAccountGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_IpeCfgAccountGroupName_Type.__name__ = "DisplayString"
_IpeCfgAccountGroupName_Object = MibTableColumn
ipeCfgAccountGroupName = _IpeCfgAccountGroupName_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 12, 2, 1, 3),
    _IpeCfgAccountGroupName_Type()
)
ipeCfgAccountGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgAccountGroupName.setStatus("current")


class _IpeCfgAccountGroupTelnet_Type(Integer32):
    """Custom type ipeCfgAccountGroupTelnet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("disabled", 1),
          ("enabled", 2))
    )


_IpeCfgAccountGroupTelnet_Type.__name__ = "Integer32"
_IpeCfgAccountGroupTelnet_Object = MibTableColumn
ipeCfgAccountGroupTelnet = _IpeCfgAccountGroupTelnet_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 12, 2, 1, 4),
    _IpeCfgAccountGroupTelnet_Type()
)
ipeCfgAccountGroupTelnet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgAccountGroupTelnet.setStatus("current")


class _IpeCfgAccountGroupSsh_Type(Integer32):
    """Custom type ipeCfgAccountGroupSsh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("disabled", 1),
          ("enabled", 2))
    )


_IpeCfgAccountGroupSsh_Type.__name__ = "Integer32"
_IpeCfgAccountGroupSsh_Object = MibTableColumn
ipeCfgAccountGroupSsh = _IpeCfgAccountGroupSsh_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 12, 2, 1, 5),
    _IpeCfgAccountGroupSsh_Type()
)
ipeCfgAccountGroupSsh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgAccountGroupSsh.setStatus("current")


class _IpeCfgAccountGroupFtp_Type(Integer32):
    """Custom type ipeCfgAccountGroupFtp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("disabled", 1),
          ("enabled", 2))
    )


_IpeCfgAccountGroupFtp_Type.__name__ = "Integer32"
_IpeCfgAccountGroupFtp_Object = MibTableColumn
ipeCfgAccountGroupFtp = _IpeCfgAccountGroupFtp_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 12, 2, 1, 6),
    _IpeCfgAccountGroupFtp_Type()
)
ipeCfgAccountGroupFtp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgAccountGroupFtp.setStatus("current")


class _IpeCfgAccountGroupSftp_Type(Integer32):
    """Custom type ipeCfgAccountGroupSftp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("disabled", 1),
          ("enabled", 2))
    )


_IpeCfgAccountGroupSftp_Type.__name__ = "Integer32"
_IpeCfgAccountGroupSftp_Object = MibTableColumn
ipeCfgAccountGroupSftp = _IpeCfgAccountGroupSftp_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 12, 2, 1, 7),
    _IpeCfgAccountGroupSftp_Type()
)
ipeCfgAccountGroupSftp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgAccountGroupSftp.setStatus("current")


class _IpeCfgAccountGroupHttp_Type(Integer32):
    """Custom type ipeCfgAccountGroupHttp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("disabled", 1),
          ("enabled", 2))
    )


_IpeCfgAccountGroupHttp_Type.__name__ = "Integer32"
_IpeCfgAccountGroupHttp_Object = MibTableColumn
ipeCfgAccountGroupHttp = _IpeCfgAccountGroupHttp_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 12, 2, 1, 8),
    _IpeCfgAccountGroupHttp_Type()
)
ipeCfgAccountGroupHttp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgAccountGroupHttp.setStatus("current")


class _IpeCfgAccountGroupHttps_Type(Integer32):
    """Custom type ipeCfgAccountGroupHttps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("disabled", 1),
          ("enabled", 2))
    )


_IpeCfgAccountGroupHttps_Type.__name__ = "Integer32"
_IpeCfgAccountGroupHttps_Object = MibTableColumn
ipeCfgAccountGroupHttps = _IpeCfgAccountGroupHttps_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 12, 2, 1, 9),
    _IpeCfgAccountGroupHttps_Type()
)
ipeCfgAccountGroupHttps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgAccountGroupHttps.setStatus("current")


class _IpeCfgAccountGroupSnmp_Type(Integer32):
    """Custom type ipeCfgAccountGroupSnmp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("disabled", 1),
          ("enabled", 2))
    )


_IpeCfgAccountGroupSnmp_Type.__name__ = "Integer32"
_IpeCfgAccountGroupSnmp_Object = MibTableColumn
ipeCfgAccountGroupSnmp = _IpeCfgAccountGroupSnmp_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 12, 2, 1, 10),
    _IpeCfgAccountGroupSnmp_Type()
)
ipeCfgAccountGroupSnmp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgAccountGroupSnmp.setStatus("current")


class _IpeCfgAccountGroupAccessLevel_Type(Integer32):
    """Custom type ipeCfgAccountGroupAccessLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("operatorLevel", 1),
          ("configLevel", 2),
          ("adminLevel", 3))
    )


_IpeCfgAccountGroupAccessLevel_Type.__name__ = "Integer32"
_IpeCfgAccountGroupAccessLevel_Object = MibTableColumn
ipeCfgAccountGroupAccessLevel = _IpeCfgAccountGroupAccessLevel_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 12, 2, 1, 11),
    _IpeCfgAccountGroupAccessLevel_Type()
)
ipeCfgAccountGroupAccessLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgAccountGroupAccessLevel.setStatus("current")


class _IpeCfgAccountGroupRowStatus_Type(RowStatus):
    """Custom type ipeCfgAccountGroupRowStatus based on RowStatus"""
    subtypeSpec = RowStatus.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("destroy", 6))
    )


_IpeCfgAccountGroupRowStatus_Type.__name__ = "RowStatus"
_IpeCfgAccountGroupRowStatus_Object = MibTableColumn
ipeCfgAccountGroupRowStatus = _IpeCfgAccountGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 12, 2, 1, 12),
    _IpeCfgAccountGroupRowStatus_Type()
)
ipeCfgAccountGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgAccountGroupRowStatus.setStatus("current")
_IpeCfgUserAccountAuthTable_Object = MibTable
ipeCfgUserAccountAuthTable = _IpeCfgUserAccountAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 12, 4)
)
if mibBuilder.loadTexts:
    ipeCfgUserAccountAuthTable.setStatus("current")
_IpeCfgUserAccountAuthEntry_Object = MibTableRow
ipeCfgUserAccountAuthEntry = _IpeCfgUserAccountAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 12, 4, 1)
)
ipeCfgUserAccountAuthEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeCfgUserAccountAuthIndex"),
)
if mibBuilder.loadTexts:
    ipeCfgUserAccountAuthEntry.setStatus("current")


class _IpeCfgUserAccountAuthIndex_Type(Integer32):
    """Custom type ipeCfgUserAccountAuthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_IpeCfgUserAccountAuthIndex_Type.__name__ = "Integer32"
_IpeCfgUserAccountAuthIndex_Object = MibTableColumn
ipeCfgUserAccountAuthIndex = _IpeCfgUserAccountAuthIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 12, 4, 1, 1),
    _IpeCfgUserAccountAuthIndex_Type()
)
ipeCfgUserAccountAuthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgUserAccountAuthIndex.setStatus("current")
_IpeCfgUserAccountAuthNEAddress_Type = IpAddress
_IpeCfgUserAccountAuthNEAddress_Object = MibTableColumn
ipeCfgUserAccountAuthNEAddress = _IpeCfgUserAccountAuthNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 12, 4, 1, 2),
    _IpeCfgUserAccountAuthNEAddress_Type()
)
ipeCfgUserAccountAuthNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgUserAccountAuthNEAddress.setStatus("current")


class _IpeCfgUserAccountAuthMode_Type(Integer32):
    """Custom type ipeCfgUserAccountAuthMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("mode1", 1),
          ("mode2", 2),
          ("mode3", 3))
    )


_IpeCfgUserAccountAuthMode_Type.__name__ = "Integer32"
_IpeCfgUserAccountAuthMode_Object = MibTableColumn
ipeCfgUserAccountAuthMode = _IpeCfgUserAccountAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 12, 4, 1, 3),
    _IpeCfgUserAccountAuthMode_Type()
)
ipeCfgUserAccountAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgUserAccountAuthMode.setStatus("current")


class _IpeCfgUserAccountAuthOrder_Type(Integer32):
    """Custom type ipeCfgUserAccountAuthOrder based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("localAuthFirst", 1),
          ("externalAuthFirst", 2))
    )


_IpeCfgUserAccountAuthOrder_Type.__name__ = "Integer32"
_IpeCfgUserAccountAuthOrder_Object = MibTableColumn
ipeCfgUserAccountAuthOrder = _IpeCfgUserAccountAuthOrder_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 12, 4, 1, 4),
    _IpeCfgUserAccountAuthOrder_Type()
)
ipeCfgUserAccountAuthOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgUserAccountAuthOrder.setStatus("current")


class _IpeCfgUserAccountAuthTrapEnable_Type(Integer32):
    """Custom type ipeCfgUserAccountAuthTrapEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("disable", 1),
          ("enable", 2))
    )


_IpeCfgUserAccountAuthTrapEnable_Type.__name__ = "Integer32"
_IpeCfgUserAccountAuthTrapEnable_Object = MibTableColumn
ipeCfgUserAccountAuthTrapEnable = _IpeCfgUserAccountAuthTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 12, 4, 1, 5),
    _IpeCfgUserAccountAuthTrapEnable_Type()
)
ipeCfgUserAccountAuthTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgUserAccountAuthTrapEnable.setStatus("current")


class _IpeCfgUserAccountAuthTrapLocal_Type(Integer32):
    """Custom type ipeCfgUserAccountAuthTrapLocal based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("success", 1),
          ("failure", 2))
    )


_IpeCfgUserAccountAuthTrapLocal_Type.__name__ = "Integer32"
_IpeCfgUserAccountAuthTrapLocal_Object = MibTableColumn
ipeCfgUserAccountAuthTrapLocal = _IpeCfgUserAccountAuthTrapLocal_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 12, 4, 1, 6),
    _IpeCfgUserAccountAuthTrapLocal_Type()
)
ipeCfgUserAccountAuthTrapLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeCfgUserAccountAuthTrapLocal.setStatus("current")


class _IpeCfgUserAccountAuthTrapExternal_Type(Integer32):
    """Custom type ipeCfgUserAccountAuthTrapExternal based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("success", 1),
          ("failure", 2))
    )


_IpeCfgUserAccountAuthTrapExternal_Type.__name__ = "Integer32"
_IpeCfgUserAccountAuthTrapExternal_Object = MibTableColumn
ipeCfgUserAccountAuthTrapExternal = _IpeCfgUserAccountAuthTrapExternal_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 12, 4, 1, 7),
    _IpeCfgUserAccountAuthTrapExternal_Type()
)
ipeCfgUserAccountAuthTrapExternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeCfgUserAccountAuthTrapExternal.setStatus("current")
_IpeCfgDhcpGroup_ObjectIdentity = ObjectIdentity
ipeCfgDhcpGroup = _IpeCfgDhcpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 13)
)
_IpeCfgDhcpServerTable_Object = MibTable
ipeCfgDhcpServerTable = _IpeCfgDhcpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 13, 1)
)
if mibBuilder.loadTexts:
    ipeCfgDhcpServerTable.setStatus("current")
_IpeCfgDhcpServerEntry_Object = MibTableRow
ipeCfgDhcpServerEntry = _IpeCfgDhcpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 13, 1, 1)
)
ipeCfgDhcpServerEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeCfgDhcpServerIndex"),
)
if mibBuilder.loadTexts:
    ipeCfgDhcpServerEntry.setStatus("current")


class _IpeCfgDhcpServerIndex_Type(Integer32):
    """Custom type ipeCfgDhcpServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_IpeCfgDhcpServerIndex_Type.__name__ = "Integer32"
_IpeCfgDhcpServerIndex_Object = MibTableColumn
ipeCfgDhcpServerIndex = _IpeCfgDhcpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 13, 1, 1, 1),
    _IpeCfgDhcpServerIndex_Type()
)
ipeCfgDhcpServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgDhcpServerIndex.setStatus("current")
_IpeCfgDhcpServerNEAddress_Type = IpAddress
_IpeCfgDhcpServerNEAddress_Object = MibTableColumn
ipeCfgDhcpServerNEAddress = _IpeCfgDhcpServerNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 13, 1, 1, 2),
    _IpeCfgDhcpServerNEAddress_Type()
)
ipeCfgDhcpServerNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgDhcpServerNEAddress.setStatus("current")


class _IpeCfgDhcpServerEnable_Type(Integer32):
    """Custom type ipeCfgDhcpServerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2),
          ("restart", 3))
    )


_IpeCfgDhcpServerEnable_Type.__name__ = "Integer32"
_IpeCfgDhcpServerEnable_Object = MibTableColumn
ipeCfgDhcpServerEnable = _IpeCfgDhcpServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 13, 1, 1, 3),
    _IpeCfgDhcpServerEnable_Type()
)
ipeCfgDhcpServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgDhcpServerEnable.setStatus("current")
_IpeCfgDhcpLeaseAddrRangeBegin_Type = IpAddress
_IpeCfgDhcpLeaseAddrRangeBegin_Object = MibTableColumn
ipeCfgDhcpLeaseAddrRangeBegin = _IpeCfgDhcpLeaseAddrRangeBegin_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 13, 1, 1, 4),
    _IpeCfgDhcpLeaseAddrRangeBegin_Type()
)
ipeCfgDhcpLeaseAddrRangeBegin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgDhcpLeaseAddrRangeBegin.setStatus("current")
_IpeCfgDhcpLeaseAddrRangeEnd_Type = IpAddress
_IpeCfgDhcpLeaseAddrRangeEnd_Object = MibTableColumn
ipeCfgDhcpLeaseAddrRangeEnd = _IpeCfgDhcpLeaseAddrRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 13, 1, 1, 5),
    _IpeCfgDhcpLeaseAddrRangeEnd_Type()
)
ipeCfgDhcpLeaseAddrRangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgDhcpLeaseAddrRangeEnd.setStatus("current")
_IpeCfgStpGroup_ObjectIdentity = ObjectIdentity
ipeCfgStpGroup = _IpeCfgStpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 14)
)
_IpeCfgStpBridgeTable_Object = MibTable
ipeCfgStpBridgeTable = _IpeCfgStpBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 14, 1)
)
if mibBuilder.loadTexts:
    ipeCfgStpBridgeTable.setStatus("current")
_IpeCfgStpBridgeEntry_Object = MibTableRow
ipeCfgStpBridgeEntry = _IpeCfgStpBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 14, 1, 1)
)
ipeCfgStpBridgeEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeCfgStpBridgeIndex"),
)
if mibBuilder.loadTexts:
    ipeCfgStpBridgeEntry.setStatus("current")


class _IpeCfgStpBridgeIndex_Type(Integer32):
    """Custom type ipeCfgStpBridgeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_IpeCfgStpBridgeIndex_Type.__name__ = "Integer32"
_IpeCfgStpBridgeIndex_Object = MibTableColumn
ipeCfgStpBridgeIndex = _IpeCfgStpBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 14, 1, 1, 1),
    _IpeCfgStpBridgeIndex_Type()
)
ipeCfgStpBridgeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgStpBridgeIndex.setStatus("current")
_IpeCfgStpBridgeNEAddress_Type = IpAddress
_IpeCfgStpBridgeNEAddress_Object = MibTableColumn
ipeCfgStpBridgeNEAddress = _IpeCfgStpBridgeNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 14, 1, 1, 2),
    _IpeCfgStpBridgeNEAddress_Type()
)
ipeCfgStpBridgeNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgStpBridgeNEAddress.setStatus("current")


class _IpeCfgStpEnable_Type(Integer32):
    """Custom type ipeCfgStpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_IpeCfgStpEnable_Type.__name__ = "Integer32"
_IpeCfgStpEnable_Object = MibTableColumn
ipeCfgStpEnable = _IpeCfgStpEnable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 14, 1, 1, 3),
    _IpeCfgStpEnable_Type()
)
ipeCfgStpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgStpEnable.setStatus("current")


class _IpeCfgStpPriority_Type(Integer32):
    """Custom type ipeCfgStpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpeCfgStpPriority_Type.__name__ = "Integer32"
_IpeCfgStpPriority_Object = MibTableColumn
ipeCfgStpPriority = _IpeCfgStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 14, 1, 1, 4),
    _IpeCfgStpPriority_Type()
)
ipeCfgStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgStpPriority.setStatus("current")


class _IpeCfgStpBridgeMaxAge_Type(Timeout):
    """Custom type ipeCfgStpBridgeMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_IpeCfgStpBridgeMaxAge_Type.__name__ = "Timeout"
_IpeCfgStpBridgeMaxAge_Object = MibTableColumn
ipeCfgStpBridgeMaxAge = _IpeCfgStpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 14, 1, 1, 5),
    _IpeCfgStpBridgeMaxAge_Type()
)
ipeCfgStpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgStpBridgeMaxAge.setStatus("current")


class _IpeCfgStpBridgeHelloTime_Type(Timeout):
    """Custom type ipeCfgStpBridgeHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_IpeCfgStpBridgeHelloTime_Type.__name__ = "Timeout"
_IpeCfgStpBridgeHelloTime_Object = MibTableColumn
ipeCfgStpBridgeHelloTime = _IpeCfgStpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 14, 1, 1, 6),
    _IpeCfgStpBridgeHelloTime_Type()
)
ipeCfgStpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgStpBridgeHelloTime.setStatus("current")


class _IpeCfgStpBridgeForwardDelay_Type(Timeout):
    """Custom type ipeCfgStpBridgeForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_IpeCfgStpBridgeForwardDelay_Type.__name__ = "Timeout"
_IpeCfgStpBridgeForwardDelay_Object = MibTableColumn
ipeCfgStpBridgeForwardDelay = _IpeCfgStpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 14, 1, 1, 7),
    _IpeCfgStpBridgeForwardDelay_Type()
)
ipeCfgStpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgStpBridgeForwardDelay.setStatus("current")
_IpeCfgStpPortTable_Object = MibTable
ipeCfgStpPortTable = _IpeCfgStpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 14, 2)
)
if mibBuilder.loadTexts:
    ipeCfgStpPortTable.setStatus("current")
_IpeCfgStpPortEntry_Object = MibTableRow
ipeCfgStpPortEntry = _IpeCfgStpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 14, 2, 1)
)
ipeCfgStpPortEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeCfgStpPortIfIndex"),
)
if mibBuilder.loadTexts:
    ipeCfgStpPortEntry.setStatus("current")
_IpeCfgStpPortIfIndex_Type = InterfaceIndex
_IpeCfgStpPortIfIndex_Object = MibTableColumn
ipeCfgStpPortIfIndex = _IpeCfgStpPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 14, 2, 1, 1),
    _IpeCfgStpPortIfIndex_Type()
)
ipeCfgStpPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgStpPortIfIndex.setStatus("current")
_IpeCfgStpPortNEAddress_Type = IpAddress
_IpeCfgStpPortNEAddress_Object = MibTableColumn
ipeCfgStpPortNEAddress = _IpeCfgStpPortNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 14, 2, 1, 2),
    _IpeCfgStpPortNEAddress_Type()
)
ipeCfgStpPortNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgStpPortNEAddress.setStatus("current")


class _IpeCfgStpPortPriority_Type(Integer32):
    """Custom type ipeCfgStpPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_IpeCfgStpPortPriority_Type.__name__ = "Integer32"
_IpeCfgStpPortPriority_Object = MibTableColumn
ipeCfgStpPortPriority = _IpeCfgStpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 14, 2, 1, 3),
    _IpeCfgStpPortPriority_Type()
)
ipeCfgStpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgStpPortPriority.setStatus("current")


class _IpeCfgStpPortPathCost_Type(Integer32):
    """Custom type ipeCfgStpPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpeCfgStpPortPathCost_Type.__name__ = "Integer32"
_IpeCfgStpPortPathCost_Object = MibTableColumn
ipeCfgStpPortPathCost = _IpeCfgStpPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 14, 2, 1, 4),
    _IpeCfgStpPortPathCost_Type()
)
ipeCfgStpPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgStpPortPathCost.setStatus("current")


class _IpeCfgStpPortEdgeEnable_Type(Integer32):
    """Custom type ipeCfgStpPortEdgeEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_IpeCfgStpPortEdgeEnable_Type.__name__ = "Integer32"
_IpeCfgStpPortEdgeEnable_Object = MibTableColumn
ipeCfgStpPortEdgeEnable = _IpeCfgStpPortEdgeEnable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 14, 2, 1, 5),
    _IpeCfgStpPortEdgeEnable_Type()
)
ipeCfgStpPortEdgeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgStpPortEdgeEnable.setStatus("current")
_IpeCfgPortGroup_ObjectIdentity = ObjectIdentity
ipeCfgPortGroup = _IpeCfgPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15)
)
_IpeCfgPortModemTable_Object = MibTable
ipeCfgPortModemTable = _IpeCfgPortModemTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 1)
)
if mibBuilder.loadTexts:
    ipeCfgPortModemTable.setStatus("current")
_IpeCfgPortModemEntry_Object = MibTableRow
ipeCfgPortModemEntry = _IpeCfgPortModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 1, 1)
)
ipeCfgPortModemEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeCfgPortModemIfIndex"),
)
if mibBuilder.loadTexts:
    ipeCfgPortModemEntry.setStatus("current")
_IpeCfgPortModemIfIndex_Type = InterfaceIndex
_IpeCfgPortModemIfIndex_Object = MibTableColumn
ipeCfgPortModemIfIndex = _IpeCfgPortModemIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 1, 1, 1),
    _IpeCfgPortModemIfIndex_Type()
)
ipeCfgPortModemIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgPortModemIfIndex.setStatus("current")
_IpeCfgPortModemNEAddress_Type = IpAddress
_IpeCfgPortModemNEAddress_Object = MibTableColumn
ipeCfgPortModemNEAddress = _IpeCfgPortModemNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 1, 1, 2),
    _IpeCfgPortModemNEAddress_Type()
)
ipeCfgPortModemNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgPortModemNEAddress.setStatus("current")


class _IpeCfgPortModemEnable_Type(Integer32):
    """Custom type ipeCfgPortModemEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_IpeCfgPortModemEnable_Type.__name__ = "Integer32"
_IpeCfgPortModemEnable_Object = MibTableColumn
ipeCfgPortModemEnable = _IpeCfgPortModemEnable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 1, 1, 3),
    _IpeCfgPortModemEnable_Type()
)
ipeCfgPortModemEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgPortModemEnable.setStatus("current")
_IpeCfgPortLctTable_Object = MibTable
ipeCfgPortLctTable = _IpeCfgPortLctTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 2)
)
if mibBuilder.loadTexts:
    ipeCfgPortLctTable.setStatus("current")
_IpeCfgPortLctEntry_Object = MibTableRow
ipeCfgPortLctEntry = _IpeCfgPortLctEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 2, 1)
)
ipeCfgPortLctEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeCfgPortLctIfIndex"),
)
if mibBuilder.loadTexts:
    ipeCfgPortLctEntry.setStatus("current")
_IpeCfgPortLctIfIndex_Type = InterfaceIndex
_IpeCfgPortLctIfIndex_Object = MibTableColumn
ipeCfgPortLctIfIndex = _IpeCfgPortLctIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 2, 1, 1),
    _IpeCfgPortLctIfIndex_Type()
)
ipeCfgPortLctIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgPortLctIfIndex.setStatus("current")
_IpeCfgPortLctNEAddress_Type = IpAddress
_IpeCfgPortLctNEAddress_Object = MibTableColumn
ipeCfgPortLctNEAddress = _IpeCfgPortLctNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 2, 1, 2),
    _IpeCfgPortLctNEAddress_Type()
)
ipeCfgPortLctNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgPortLctNEAddress.setStatus("current")
_IpeCfgPortLctIpAddress_Type = IpAddress
_IpeCfgPortLctIpAddress_Object = MibTableColumn
ipeCfgPortLctIpAddress = _IpeCfgPortLctIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 2, 1, 3),
    _IpeCfgPortLctIpAddress_Type()
)
ipeCfgPortLctIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgPortLctIpAddress.setStatus("current")
_IpeCfgPortLctNetMask_Type = IpAddress
_IpeCfgPortLctNetMask_Object = MibTableColumn
ipeCfgPortLctNetMask = _IpeCfgPortLctNetMask_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 2, 1, 4),
    _IpeCfgPortLctNetMask_Type()
)
ipeCfgPortLctNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgPortLctNetMask.setStatus("current")


class _IpeCfgPortLctEnable_Type(Integer32):
    """Custom type ipeCfgPortLctEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_IpeCfgPortLctEnable_Type.__name__ = "Integer32"
_IpeCfgPortLctEnable_Object = MibTableColumn
ipeCfgPortLctEnable = _IpeCfgPortLctEnable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 2, 1, 5),
    _IpeCfgPortLctEnable_Type()
)
ipeCfgPortLctEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgPortLctEnable.setStatus("current")


class _IpeCfgPortLctMtu_Type(Integer32):
    """Custom type ipeCfgPortLctMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 1500),
    )


_IpeCfgPortLctMtu_Type.__name__ = "Integer32"
_IpeCfgPortLctMtu_Object = MibTableColumn
ipeCfgPortLctMtu = _IpeCfgPortLctMtu_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 2, 1, 6),
    _IpeCfgPortLctMtu_Type()
)
ipeCfgPortLctMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgPortLctMtu.setStatus("current")


class _IpeCfgPortLctAutoNeg_Type(Integer32):
    """Custom type ipeCfgPortLctAutoNeg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_IpeCfgPortLctAutoNeg_Type.__name__ = "Integer32"
_IpeCfgPortLctAutoNeg_Object = MibTableColumn
ipeCfgPortLctAutoNeg = _IpeCfgPortLctAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 2, 1, 7),
    _IpeCfgPortLctAutoNeg_Type()
)
ipeCfgPortLctAutoNeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgPortLctAutoNeg.setStatus("current")
_IpeCfgPortEtherTable_Object = MibTable
ipeCfgPortEtherTable = _IpeCfgPortEtherTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 3)
)
if mibBuilder.loadTexts:
    ipeCfgPortEtherTable.setStatus("current")
_IpeCfgPortEtherEntry_Object = MibTableRow
ipeCfgPortEtherEntry = _IpeCfgPortEtherEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 3, 1)
)
ipeCfgPortEtherEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeCfgPortEtherIfIndex"),
)
if mibBuilder.loadTexts:
    ipeCfgPortEtherEntry.setStatus("current")
_IpeCfgPortEtherIfIndex_Type = InterfaceIndex
_IpeCfgPortEtherIfIndex_Object = MibTableColumn
ipeCfgPortEtherIfIndex = _IpeCfgPortEtherIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 3, 1, 1),
    _IpeCfgPortEtherIfIndex_Type()
)
ipeCfgPortEtherIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgPortEtherIfIndex.setStatus("current")
_IpeCfgPortEtherNEAddress_Type = IpAddress
_IpeCfgPortEtherNEAddress_Object = MibTableColumn
ipeCfgPortEtherNEAddress = _IpeCfgPortEtherNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 3, 1, 2),
    _IpeCfgPortEtherNEAddress_Type()
)
ipeCfgPortEtherNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgPortEtherNEAddress.setStatus("current")


class _IpeCfgPortEtherEnable_Type(Integer32):
    """Custom type ipeCfgPortEtherEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_IpeCfgPortEtherEnable_Type.__name__ = "Integer32"
_IpeCfgPortEtherEnable_Object = MibTableColumn
ipeCfgPortEtherEnable = _IpeCfgPortEtherEnable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 3, 1, 3),
    _IpeCfgPortEtherEnable_Type()
)
ipeCfgPortEtherEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgPortEtherEnable.setStatus("current")


class _IpeCfgPortEtherAutoNeg_Type(Integer32):
    """Custom type ipeCfgPortEtherAutoNeg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_IpeCfgPortEtherAutoNeg_Type.__name__ = "Integer32"
_IpeCfgPortEtherAutoNeg_Object = MibTableColumn
ipeCfgPortEtherAutoNeg = _IpeCfgPortEtherAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 3, 1, 4),
    _IpeCfgPortEtherAutoNeg_Type()
)
ipeCfgPortEtherAutoNeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgPortEtherAutoNeg.setStatus("current")


class _IpeCfgPortEtherSpecialFilter_Type(Integer32):
    """Custom type ipeCfgPortEtherSpecialFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_IpeCfgPortEtherSpecialFilter_Type.__name__ = "Integer32"
_IpeCfgPortEtherSpecialFilter_Object = MibTableColumn
ipeCfgPortEtherSpecialFilter = _IpeCfgPortEtherSpecialFilter_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 3, 1, 5),
    _IpeCfgPortEtherSpecialFilter_Type()
)
ipeCfgPortEtherSpecialFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgPortEtherSpecialFilter.setStatus("current")


class _IpeCfgPortEtherLldpMode_Type(Integer32):
    """Custom type ipeCfgPortEtherLldpMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("standardMode", 1),
          ("proprietaryMode", 2))
    )


_IpeCfgPortEtherLldpMode_Type.__name__ = "Integer32"
_IpeCfgPortEtherLldpMode_Object = MibTableColumn
ipeCfgPortEtherLldpMode = _IpeCfgPortEtherLldpMode_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 3, 1, 6),
    _IpeCfgPortEtherLldpMode_Type()
)
ipeCfgPortEtherLldpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgPortEtherLldpMode.setStatus("current")
_IpeCfgPortNe2Table_Object = MibTable
ipeCfgPortNe2Table = _IpeCfgPortNe2Table_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 4)
)
if mibBuilder.loadTexts:
    ipeCfgPortNe2Table.setStatus("current")
_IpeCfgPortNe2Entry_Object = MibTableRow
ipeCfgPortNe2Entry = _IpeCfgPortNe2Entry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 4, 1)
)
ipeCfgPortNe2Entry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeCfgPortNe2IfIndex"),
)
if mibBuilder.loadTexts:
    ipeCfgPortNe2Entry.setStatus("current")
_IpeCfgPortNe2IfIndex_Type = InterfaceIndex
_IpeCfgPortNe2IfIndex_Object = MibTableColumn
ipeCfgPortNe2IfIndex = _IpeCfgPortNe2IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 4, 1, 1),
    _IpeCfgPortNe2IfIndex_Type()
)
ipeCfgPortNe2IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgPortNe2IfIndex.setStatus("current")
_IpeCfgPortNe2NEAddress_Type = IpAddress
_IpeCfgPortNe2NEAddress_Object = MibTableColumn
ipeCfgPortNe2NEAddress = _IpeCfgPortNe2NEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 4, 1, 2),
    _IpeCfgPortNe2NEAddress_Type()
)
ipeCfgPortNe2NEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgPortNe2NEAddress.setStatus("current")
_IpeCfgPortNe2IpAddress_Type = IpAddress
_IpeCfgPortNe2IpAddress_Object = MibTableColumn
ipeCfgPortNe2IpAddress = _IpeCfgPortNe2IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 4, 1, 3),
    _IpeCfgPortNe2IpAddress_Type()
)
ipeCfgPortNe2IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgPortNe2IpAddress.setStatus("current")


class _IpeCfgPortNe2Enable_Type(Integer32):
    """Custom type ipeCfgPortNe2Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_IpeCfgPortNe2Enable_Type.__name__ = "Integer32"
_IpeCfgPortNe2Enable_Object = MibTableColumn
ipeCfgPortNe2Enable = _IpeCfgPortNe2Enable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 4, 1, 4),
    _IpeCfgPortNe2Enable_Type()
)
ipeCfgPortNe2Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgPortNe2Enable.setStatus("current")


class _IpeCfgPortNe2Speed_Type(Integer32):
    """Custom type ipeCfgPortNe2Speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(9600,
              19200)
        )
    )
    namedValues = NamedValues(
        *(("speed9600", 9600),
          ("speed19200", 19200))
    )


_IpeCfgPortNe2Speed_Type.__name__ = "Integer32"
_IpeCfgPortNe2Speed_Object = MibTableColumn
ipeCfgPortNe2Speed = _IpeCfgPortNe2Speed_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 4, 1, 5),
    _IpeCfgPortNe2Speed_Type()
)
ipeCfgPortNe2Speed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgPortNe2Speed.setStatus("current")


class _IpeCfgPortNe2NeighborMibEnable_Type(Integer32):
    """Custom type ipeCfgPortNe2NeighborMibEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_IpeCfgPortNe2NeighborMibEnable_Type.__name__ = "Integer32"
_IpeCfgPortNe2NeighborMibEnable_Object = MibTableColumn
ipeCfgPortNe2NeighborMibEnable = _IpeCfgPortNe2NeighborMibEnable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 4, 1, 6),
    _IpeCfgPortNe2NeighborMibEnable_Type()
)
ipeCfgPortNe2NeighborMibEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgPortNe2NeighborMibEnable.setStatus("current")
_IpeCfgPortE1Table_Object = MibTable
ipeCfgPortE1Table = _IpeCfgPortE1Table_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 5)
)
if mibBuilder.loadTexts:
    ipeCfgPortE1Table.setStatus("current")
_IpeCfgPortE1Entry_Object = MibTableRow
ipeCfgPortE1Entry = _IpeCfgPortE1Entry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 5, 1)
)
ipeCfgPortE1Entry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeCfgPortE1IfIndex"),
)
if mibBuilder.loadTexts:
    ipeCfgPortE1Entry.setStatus("current")
_IpeCfgPortE1IfIndex_Type = InterfaceIndex
_IpeCfgPortE1IfIndex_Object = MibTableColumn
ipeCfgPortE1IfIndex = _IpeCfgPortE1IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 5, 1, 1),
    _IpeCfgPortE1IfIndex_Type()
)
ipeCfgPortE1IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgPortE1IfIndex.setStatus("current")
_IpeCfgPortE1NEAddress_Type = IpAddress
_IpeCfgPortE1NEAddress_Object = MibTableColumn
ipeCfgPortE1NEAddress = _IpeCfgPortE1NEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 5, 1, 2),
    _IpeCfgPortE1NEAddress_Type()
)
ipeCfgPortE1NEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgPortE1NEAddress.setStatus("current")


class _IpeCfgPortE1Enable_Type(Integer32):
    """Custom type ipeCfgPortE1Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_IpeCfgPortE1Enable_Type.__name__ = "Integer32"
_IpeCfgPortE1Enable_Object = MibTableColumn
ipeCfgPortE1Enable = _IpeCfgPortE1Enable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 5, 1, 3),
    _IpeCfgPortE1Enable_Type()
)
ipeCfgPortE1Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgPortE1Enable.setStatus("current")


class _IpeCfgPortE1ChannelNumber_Type(Integer32):
    """Custom type ipeCfgPortE1ChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_IpeCfgPortE1ChannelNumber_Type.__name__ = "Integer32"
_IpeCfgPortE1ChannelNumber_Object = MibTableColumn
ipeCfgPortE1ChannelNumber = _IpeCfgPortE1ChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 5, 1, 4),
    _IpeCfgPortE1ChannelNumber_Type()
)
ipeCfgPortE1ChannelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgPortE1ChannelNumber.setStatus("current")
_IpeCfgPortInbandTable_Object = MibTable
ipeCfgPortInbandTable = _IpeCfgPortInbandTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 6)
)
if mibBuilder.loadTexts:
    ipeCfgPortInbandTable.setStatus("current")
_IpeCfgPortInbandEntry_Object = MibTableRow
ipeCfgPortInbandEntry = _IpeCfgPortInbandEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 6, 1)
)
ipeCfgPortInbandEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeCfgPortInbandIfIndex"),
)
if mibBuilder.loadTexts:
    ipeCfgPortInbandEntry.setStatus("current")
_IpeCfgPortInbandIfIndex_Type = InterfaceIndex
_IpeCfgPortInbandIfIndex_Object = MibTableColumn
ipeCfgPortInbandIfIndex = _IpeCfgPortInbandIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 6, 1, 1),
    _IpeCfgPortInbandIfIndex_Type()
)
ipeCfgPortInbandIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgPortInbandIfIndex.setStatus("current")
_IpeCfgPortInbandNEAddress_Type = IpAddress
_IpeCfgPortInbandNEAddress_Object = MibTableColumn
ipeCfgPortInbandNEAddress = _IpeCfgPortInbandNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 6, 1, 2),
    _IpeCfgPortInbandNEAddress_Type()
)
ipeCfgPortInbandNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgPortInbandNEAddress.setStatus("current")
_IpeCfgPortInbandIpAddress_Type = IpAddress
_IpeCfgPortInbandIpAddress_Object = MibTableColumn
ipeCfgPortInbandIpAddress = _IpeCfgPortInbandIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 6, 1, 3),
    _IpeCfgPortInbandIpAddress_Type()
)
ipeCfgPortInbandIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgPortInbandIpAddress.setStatus("obsolete")
_IpeCfgPortInbandNetMask_Type = IpAddress
_IpeCfgPortInbandNetMask_Object = MibTableColumn
ipeCfgPortInbandNetMask = _IpeCfgPortInbandNetMask_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 6, 1, 4),
    _IpeCfgPortInbandNetMask_Type()
)
ipeCfgPortInbandNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgPortInbandNetMask.setStatus("obsolete")


class _IpeCfgPortInbandEnable_Type(Integer32):
    """Custom type ipeCfgPortInbandEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_IpeCfgPortInbandEnable_Type.__name__ = "Integer32"
_IpeCfgPortInbandEnable_Object = MibTableColumn
ipeCfgPortInbandEnable = _IpeCfgPortInbandEnable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 6, 1, 5),
    _IpeCfgPortInbandEnable_Type()
)
ipeCfgPortInbandEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgPortInbandEnable.setStatus("current")


class _IpeCfgPortInbandVlanId_Type(Integer32):
    """Custom type ipeCfgPortInbandVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_IpeCfgPortInbandVlanId_Type.__name__ = "Integer32"
_IpeCfgPortInbandVlanId_Object = MibTableColumn
ipeCfgPortInbandVlanId = _IpeCfgPortInbandVlanId_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 6, 1, 6),
    _IpeCfgPortInbandVlanId_Type()
)
ipeCfgPortInbandVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgPortInbandVlanId.setStatus("current")


class _IpeCfgPortInbandMtu_Type(Integer32):
    """Custom type ipeCfgPortInbandMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 1500),
    )


_IpeCfgPortInbandMtu_Type.__name__ = "Integer32"
_IpeCfgPortInbandMtu_Object = MibTableColumn
ipeCfgPortInbandMtu = _IpeCfgPortInbandMtu_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 6, 1, 7),
    _IpeCfgPortInbandMtu_Type()
)
ipeCfgPortInbandMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgPortInbandMtu.setStatus("obsolete")


class _IpeCfgPortInbandCos_Type(Integer32):
    """Custom type ipeCfgPortInbandCos based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_IpeCfgPortInbandCos_Type.__name__ = "Integer32"
_IpeCfgPortInbandCos_Object = MibTableColumn
ipeCfgPortInbandCos = _IpeCfgPortInbandCos_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 6, 1, 8),
    _IpeCfgPortInbandCos_Type()
)
ipeCfgPortInbandCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgPortInbandCos.setStatus("current")
_IpeCfgPortMainEtherTable_Object = MibTable
ipeCfgPortMainEtherTable = _IpeCfgPortMainEtherTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 7)
)
if mibBuilder.loadTexts:
    ipeCfgPortMainEtherTable.setStatus("current")
_IpeCfgPortMainEtherEntry_Object = MibTableRow
ipeCfgPortMainEtherEntry = _IpeCfgPortMainEtherEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 7, 1)
)
ipeCfgPortMainEtherEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeCfgPortMainEtherIfIndex"),
)
if mibBuilder.loadTexts:
    ipeCfgPortMainEtherEntry.setStatus("current")
_IpeCfgPortMainEtherIfIndex_Type = InterfaceIndex
_IpeCfgPortMainEtherIfIndex_Object = MibTableColumn
ipeCfgPortMainEtherIfIndex = _IpeCfgPortMainEtherIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 7, 1, 1),
    _IpeCfgPortMainEtherIfIndex_Type()
)
ipeCfgPortMainEtherIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgPortMainEtherIfIndex.setStatus("current")
_IpeCfgPortMainEtherNEAddress_Type = IpAddress
_IpeCfgPortMainEtherNEAddress_Object = MibTableColumn
ipeCfgPortMainEtherNEAddress = _IpeCfgPortMainEtherNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 7, 1, 2),
    _IpeCfgPortMainEtherNEAddress_Type()
)
ipeCfgPortMainEtherNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgPortMainEtherNEAddress.setStatus("current")


class _IpeCfgPortMainEtherLldpMode_Type(Integer32):
    """Custom type ipeCfgPortMainEtherLldpMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("standardMode", 1),
          ("proprietaryMode", 2))
    )


_IpeCfgPortMainEtherLldpMode_Type.__name__ = "Integer32"
_IpeCfgPortMainEtherLldpMode_Object = MibTableColumn
ipeCfgPortMainEtherLldpMode = _IpeCfgPortMainEtherLldpMode_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 7, 1, 3),
    _IpeCfgPortMainEtherLldpMode_Type()
)
ipeCfgPortMainEtherLldpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgPortMainEtherLldpMode.setStatus("current")
_IpeCfgBridgeGroup_ObjectIdentity = ObjectIdentity
ipeCfgBridgeGroup = _IpeCfgBridgeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 16)
)
_IpeCfgBridgeTable_Object = MibTable
ipeCfgBridgeTable = _IpeCfgBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 16, 1)
)
if mibBuilder.loadTexts:
    ipeCfgBridgeTable.setStatus("current")
_IpeCfgBridgeEntry_Object = MibTableRow
ipeCfgBridgeEntry = _IpeCfgBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 16, 1, 1)
)
ipeCfgBridgeEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeCfgBridgeIndex"),
)
if mibBuilder.loadTexts:
    ipeCfgBridgeEntry.setStatus("current")


class _IpeCfgBridgeIndex_Type(Integer32):
    """Custom type ipeCfgBridgeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_IpeCfgBridgeIndex_Type.__name__ = "Integer32"
_IpeCfgBridgeIndex_Object = MibTableColumn
ipeCfgBridgeIndex = _IpeCfgBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 16, 1, 1, 1),
    _IpeCfgBridgeIndex_Type()
)
ipeCfgBridgeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgBridgeIndex.setStatus("current")
_IpeCfgBridgeNEAddress_Type = IpAddress
_IpeCfgBridgeNEAddress_Object = MibTableColumn
ipeCfgBridgeNEAddress = _IpeCfgBridgeNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 16, 1, 1, 2),
    _IpeCfgBridgeNEAddress_Type()
)
ipeCfgBridgeNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgBridgeNEAddress.setStatus("current")
_IpeCfgBridgeIpAddress_Type = IpAddress
_IpeCfgBridgeIpAddress_Object = MibTableColumn
ipeCfgBridgeIpAddress = _IpeCfgBridgeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 16, 1, 1, 3),
    _IpeCfgBridgeIpAddress_Type()
)
ipeCfgBridgeIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgBridgeIpAddress.setStatus("current")
_IpeCfgBridgeNetMask_Type = IpAddress
_IpeCfgBridgeNetMask_Object = MibTableColumn
ipeCfgBridgeNetMask = _IpeCfgBridgeNetMask_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 16, 1, 1, 4),
    _IpeCfgBridgeNetMask_Type()
)
ipeCfgBridgeNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgBridgeNetMask.setStatus("current")


class _IpeCfgBridgeMtu_Type(Integer32):
    """Custom type ipeCfgBridgeMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 1500),
    )


_IpeCfgBridgeMtu_Type.__name__ = "Integer32"
_IpeCfgBridgeMtu_Object = MibTableColumn
ipeCfgBridgeMtu = _IpeCfgBridgeMtu_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 16, 1, 1, 5),
    _IpeCfgBridgeMtu_Type()
)
ipeCfgBridgeMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgBridgeMtu.setStatus("current")
_IpeCfgBridgePortTable_Object = MibTable
ipeCfgBridgePortTable = _IpeCfgBridgePortTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 16, 2)
)
if mibBuilder.loadTexts:
    ipeCfgBridgePortTable.setStatus("current")
_IpeCfgBridgePortEntry_Object = MibTableRow
ipeCfgBridgePortEntry = _IpeCfgBridgePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 16, 2, 1)
)
ipeCfgBridgePortEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeCfgBridgePortIfIndex"),
)
if mibBuilder.loadTexts:
    ipeCfgBridgePortEntry.setStatus("current")
_IpeCfgBridgePortIfIndex_Type = InterfaceIndex
_IpeCfgBridgePortIfIndex_Object = MibTableColumn
ipeCfgBridgePortIfIndex = _IpeCfgBridgePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 16, 2, 1, 1),
    _IpeCfgBridgePortIfIndex_Type()
)
ipeCfgBridgePortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgBridgePortIfIndex.setStatus("current")
_IpeCfgBridgePortNEAddress_Type = IpAddress
_IpeCfgBridgePortNEAddress_Object = MibTableColumn
ipeCfgBridgePortNEAddress = _IpeCfgBridgePortNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 16, 2, 1, 2),
    _IpeCfgBridgePortNEAddress_Type()
)
ipeCfgBridgePortNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgBridgePortNEAddress.setStatus("current")


class _IpeCfgBridgePortBridgeIndex_Type(Integer32):
    """Custom type ipeCfgBridgePortBridgeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_IpeCfgBridgePortBridgeIndex_Type.__name__ = "Integer32"
_IpeCfgBridgePortBridgeIndex_Object = MibTableColumn
ipeCfgBridgePortBridgeIndex = _IpeCfgBridgePortBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 16, 2, 1, 3),
    _IpeCfgBridgePortBridgeIndex_Type()
)
ipeCfgBridgePortBridgeIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgBridgePortBridgeIndex.setStatus("current")
_IpeCfgPripGroup_ObjectIdentity = ObjectIdentity
ipeCfgPripGroup = _IpeCfgPripGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 17)
)
_IpeCfgPripTable_Object = MibTable
ipeCfgPripTable = _IpeCfgPripTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 17, 1)
)
if mibBuilder.loadTexts:
    ipeCfgPripTable.setStatus("current")
_IpeCfgPripEntry_Object = MibTableRow
ipeCfgPripEntry = _IpeCfgPripEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 17, 1, 1)
)
ipeCfgPripEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeCfgPripIndex"),
)
if mibBuilder.loadTexts:
    ipeCfgPripEntry.setStatus("current")


class _IpeCfgPripIndex_Type(Integer32):
    """Custom type ipeCfgPripIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_IpeCfgPripIndex_Type.__name__ = "Integer32"
_IpeCfgPripIndex_Object = MibTableColumn
ipeCfgPripIndex = _IpeCfgPripIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 17, 1, 1, 1),
    _IpeCfgPripIndex_Type()
)
ipeCfgPripIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgPripIndex.setStatus("current")
_IpeCfgPripNEAddress_Type = IpAddress
_IpeCfgPripNEAddress_Object = MibTableColumn
ipeCfgPripNEAddress = _IpeCfgPripNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 17, 1, 1, 2),
    _IpeCfgPripNEAddress_Type()
)
ipeCfgPripNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgPripNEAddress.setStatus("current")


class _IpeCfgPripRouteEnable_Type(Integer32):
    """Custom type ipeCfgPripRouteEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("enabled", 1),
          ("disabled", 2))
    )


_IpeCfgPripRouteEnable_Type.__name__ = "Integer32"
_IpeCfgPripRouteEnable_Object = MibTableColumn
ipeCfgPripRouteEnable = _IpeCfgPripRouteEnable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 17, 1, 1, 3),
    _IpeCfgPripRouteEnable_Type()
)
ipeCfgPripRouteEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgPripRouteEnable.setStatus("current")


class _IpeCfgPripUdpPort_Type(Integer32):
    """Custom type ipeCfgPripUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(520,
              8520)
        )
    )
    namedValues = NamedValues(
        *(("ripdefaultport", 520),
          ("pripdefaultport", 8520))
    )


_IpeCfgPripUdpPort_Type.__name__ = "Integer32"
_IpeCfgPripUdpPort_Object = MibTableColumn
ipeCfgPripUdpPort = _IpeCfgPripUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 17, 1, 1, 4),
    _IpeCfgPripUdpPort_Type()
)
ipeCfgPripUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgPripUdpPort.setStatus("current")
_IpeCfgPripPortTable_Object = MibTable
ipeCfgPripPortTable = _IpeCfgPripPortTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 17, 2)
)
if mibBuilder.loadTexts:
    ipeCfgPripPortTable.setStatus("current")
_IpeCfgPripPortEntry_Object = MibTableRow
ipeCfgPripPortEntry = _IpeCfgPripPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 17, 2, 1)
)
ipeCfgPripPortEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeCfgPripPortIfIndex"),
)
if mibBuilder.loadTexts:
    ipeCfgPripPortEntry.setStatus("current")
_IpeCfgPripPortIfIndex_Type = InterfaceIndex
_IpeCfgPripPortIfIndex_Object = MibTableColumn
ipeCfgPripPortIfIndex = _IpeCfgPripPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 17, 2, 1, 1),
    _IpeCfgPripPortIfIndex_Type()
)
ipeCfgPripPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgPripPortIfIndex.setStatus("current")
_IpeCfgPripPortNEAddress_Type = IpAddress
_IpeCfgPripPortNEAddress_Object = MibTableColumn
ipeCfgPripPortNEAddress = _IpeCfgPripPortNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 17, 2, 1, 2),
    _IpeCfgPripPortNEAddress_Type()
)
ipeCfgPripPortNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgPripPortNEAddress.setStatus("current")


class _IpeCfgPripPortEnable_Type(Integer32):
    """Custom type ipeCfgPripPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("enabled", 1),
          ("disabled", 2))
    )


_IpeCfgPripPortEnable_Type.__name__ = "Integer32"
_IpeCfgPripPortEnable_Object = MibTableColumn
ipeCfgPripPortEnable = _IpeCfgPripPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 17, 2, 1, 3),
    _IpeCfgPripPortEnable_Type()
)
ipeCfgPripPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgPripPortEnable.setStatus("current")


class _IpeCfgPripPortPropagateNetEnable_Type(Integer32):
    """Custom type ipeCfgPripPortPropagateNetEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("enabled", 1),
          ("disabled", 2))
    )


_IpeCfgPripPortPropagateNetEnable_Type.__name__ = "Integer32"
_IpeCfgPripPortPropagateNetEnable_Object = MibTableColumn
ipeCfgPripPortPropagateNetEnable = _IpeCfgPripPortPropagateNetEnable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 17, 2, 1, 4),
    _IpeCfgPripPortPropagateNetEnable_Type()
)
ipeCfgPripPortPropagateNetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgPripPortPropagateNetEnable.setStatus("current")
_IpeCfgNaptGroup_ObjectIdentity = ObjectIdentity
ipeCfgNaptGroup = _IpeCfgNaptGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 18)
)
_IpeCfgNaptTable_Object = MibTable
ipeCfgNaptTable = _IpeCfgNaptTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 18, 1)
)
if mibBuilder.loadTexts:
    ipeCfgNaptTable.setStatus("current")
_IpeCfgNaptEntry_Object = MibTableRow
ipeCfgNaptEntry = _IpeCfgNaptEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 18, 1, 1)
)
ipeCfgNaptEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeCfgNaptIndex"),
)
if mibBuilder.loadTexts:
    ipeCfgNaptEntry.setStatus("current")


class _IpeCfgNaptIndex_Type(Integer32):
    """Custom type ipeCfgNaptIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_IpeCfgNaptIndex_Type.__name__ = "Integer32"
_IpeCfgNaptIndex_Object = MibTableColumn
ipeCfgNaptIndex = _IpeCfgNaptIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 18, 1, 1, 1),
    _IpeCfgNaptIndex_Type()
)
ipeCfgNaptIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgNaptIndex.setStatus("current")
_IpeCfgNaptNEAddress_Type = IpAddress
_IpeCfgNaptNEAddress_Object = MibTableColumn
ipeCfgNaptNEAddress = _IpeCfgNaptNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 18, 1, 1, 2),
    _IpeCfgNaptNEAddress_Type()
)
ipeCfgNaptNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgNaptNEAddress.setStatus("current")


class _IpeCfgNaptEnable_Type(Integer32):
    """Custom type ipeCfgNaptEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_IpeCfgNaptEnable_Type.__name__ = "Integer32"
_IpeCfgNaptEnable_Object = MibTableColumn
ipeCfgNaptEnable = _IpeCfgNaptEnable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 18, 1, 1, 3),
    _IpeCfgNaptEnable_Type()
)
ipeCfgNaptEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgNaptEnable.setStatus("current")
_IpeCfgStaticRouteGroup_ObjectIdentity = ObjectIdentity
ipeCfgStaticRouteGroup = _IpeCfgStaticRouteGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 19)
)
_IpeCfgStaticRouteTable_Object = MibTable
ipeCfgStaticRouteTable = _IpeCfgStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 19, 1)
)
if mibBuilder.loadTexts:
    ipeCfgStaticRouteTable.setStatus("current")
_IpeCfgStaticRouteEntry_Object = MibTableRow
ipeCfgStaticRouteEntry = _IpeCfgStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 19, 1, 1)
)
ipeCfgStaticRouteEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeCfgRouteIndex"),
)
if mibBuilder.loadTexts:
    ipeCfgStaticRouteEntry.setStatus("current")


class _IpeCfgRouteIndex_Type(Integer32):
    """Custom type ipeCfgRouteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_IpeCfgRouteIndex_Type.__name__ = "Integer32"
_IpeCfgRouteIndex_Object = MibTableColumn
ipeCfgRouteIndex = _IpeCfgRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 19, 1, 1, 1),
    _IpeCfgRouteIndex_Type()
)
ipeCfgRouteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgRouteIndex.setStatus("current")
_IpeCfgRouteNEAddress_Type = IpAddress
_IpeCfgRouteNEAddress_Object = MibTableColumn
ipeCfgRouteNEAddress = _IpeCfgRouteNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 19, 1, 1, 2),
    _IpeCfgRouteNEAddress_Type()
)
ipeCfgRouteNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgRouteNEAddress.setStatus("current")
_IpeCfgRouteDest_Type = IpAddress
_IpeCfgRouteDest_Object = MibTableColumn
ipeCfgRouteDest = _IpeCfgRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 19, 1, 1, 3),
    _IpeCfgRouteDest_Type()
)
ipeCfgRouteDest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgRouteDest.setStatus("current")
_IpeCfgRouteMask_Type = IpAddress
_IpeCfgRouteMask_Object = MibTableColumn
ipeCfgRouteMask = _IpeCfgRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 19, 1, 1, 4),
    _IpeCfgRouteMask_Type()
)
ipeCfgRouteMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgRouteMask.setStatus("current")
_IpeCfgRouteNextHop_Type = IpAddress
_IpeCfgRouteNextHop_Object = MibTableColumn
ipeCfgRouteNextHop = _IpeCfgRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 19, 1, 1, 5),
    _IpeCfgRouteNextHop_Type()
)
ipeCfgRouteNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgRouteNextHop.setStatus("current")


class _IpeCfgRouteRowStatus_Type(RowStatus):
    """Custom type ipeCfgRouteRowStatus based on RowStatus"""
    subtypeSpec = RowStatus.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("destroy", 6))
    )


_IpeCfgRouteRowStatus_Type.__name__ = "RowStatus"
_IpeCfgRouteRowStatus_Object = MibTableColumn
ipeCfgRouteRowStatus = _IpeCfgRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 19, 1, 1, 6),
    _IpeCfgRouteRowStatus_Type()
)
ipeCfgRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgRouteRowStatus.setStatus("current")
_IpeCfgAccessListGroup_ObjectIdentity = ObjectIdentity
ipeCfgAccessListGroup = _IpeCfgAccessListGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 21)
)
_IpeCfgAccessListRuleTable_Object = MibTable
ipeCfgAccessListRuleTable = _IpeCfgAccessListRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 21, 1)
)
if mibBuilder.loadTexts:
    ipeCfgAccessListRuleTable.setStatus("current")
_IpeCfgAccessListRuleEntry_Object = MibTableRow
ipeCfgAccessListRuleEntry = _IpeCfgAccessListRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 21, 1, 1)
)
ipeCfgAccessListRuleEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeCfgAccessListRuleEnableIndex"),
)
if mibBuilder.loadTexts:
    ipeCfgAccessListRuleEntry.setStatus("current")


class _IpeCfgAccessListRuleEnableIndex_Type(Integer32):
    """Custom type ipeCfgAccessListRuleEnableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_IpeCfgAccessListRuleEnableIndex_Type.__name__ = "Integer32"
_IpeCfgAccessListRuleEnableIndex_Object = MibTableColumn
ipeCfgAccessListRuleEnableIndex = _IpeCfgAccessListRuleEnableIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 21, 1, 1, 1),
    _IpeCfgAccessListRuleEnableIndex_Type()
)
ipeCfgAccessListRuleEnableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgAccessListRuleEnableIndex.setStatus("current")
_IpeCfgAccessListRuleNEAddress_Type = IpAddress
_IpeCfgAccessListRuleNEAddress_Object = MibTableColumn
ipeCfgAccessListRuleNEAddress = _IpeCfgAccessListRuleNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 21, 1, 1, 2),
    _IpeCfgAccessListRuleNEAddress_Type()
)
ipeCfgAccessListRuleNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgAccessListRuleNEAddress.setStatus("current")


class _IpeCfgAccessListInputRuleEnable_Type(Integer32):
    """Custom type ipeCfgAccessListInputRuleEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("disable", 1),
          ("enable", 2))
    )


_IpeCfgAccessListInputRuleEnable_Type.__name__ = "Integer32"
_IpeCfgAccessListInputRuleEnable_Object = MibTableColumn
ipeCfgAccessListInputRuleEnable = _IpeCfgAccessListInputRuleEnable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 21, 1, 1, 3),
    _IpeCfgAccessListInputRuleEnable_Type()
)
ipeCfgAccessListInputRuleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgAccessListInputRuleEnable.setStatus("current")


class _IpeCfgAccessListForwardRuleEnable_Type(Integer32):
    """Custom type ipeCfgAccessListForwardRuleEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("disable", 1),
          ("enable", 2))
    )


_IpeCfgAccessListForwardRuleEnable_Type.__name__ = "Integer32"
_IpeCfgAccessListForwardRuleEnable_Object = MibTableColumn
ipeCfgAccessListForwardRuleEnable = _IpeCfgAccessListForwardRuleEnable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 21, 1, 1, 4),
    _IpeCfgAccessListForwardRuleEnable_Type()
)
ipeCfgAccessListForwardRuleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgAccessListForwardRuleEnable.setStatus("current")


class _IpeCfgAccessListInputDefaultAction_Type(Integer32):
    """Custom type ipeCfgAccessListInputDefaultAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_IpeCfgAccessListInputDefaultAction_Type.__name__ = "Integer32"
_IpeCfgAccessListInputDefaultAction_Object = MibTableColumn
ipeCfgAccessListInputDefaultAction = _IpeCfgAccessListInputDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 21, 1, 1, 5),
    _IpeCfgAccessListInputDefaultAction_Type()
)
ipeCfgAccessListInputDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgAccessListInputDefaultAction.setStatus("current")


class _IpeCfgAccessListForwardDefaultAction_Type(Integer32):
    """Custom type ipeCfgAccessListForwardDefaultAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_IpeCfgAccessListForwardDefaultAction_Type.__name__ = "Integer32"
_IpeCfgAccessListForwardDefaultAction_Object = MibTableColumn
ipeCfgAccessListForwardDefaultAction = _IpeCfgAccessListForwardDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 21, 1, 1, 6),
    _IpeCfgAccessListForwardDefaultAction_Type()
)
ipeCfgAccessListForwardDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgAccessListForwardDefaultAction.setStatus("current")
_IpeCfgAccessListInputTable_Object = MibTable
ipeCfgAccessListInputTable = _IpeCfgAccessListInputTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 21, 2)
)
if mibBuilder.loadTexts:
    ipeCfgAccessListInputTable.setStatus("current")
_IpeCfgAccessListInputEntry_Object = MibTableRow
ipeCfgAccessListInputEntry = _IpeCfgAccessListInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 21, 2, 1)
)
ipeCfgAccessListInputEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeCfgAccessListInputOrderNum"),
)
if mibBuilder.loadTexts:
    ipeCfgAccessListInputEntry.setStatus("current")


class _IpeCfgAccessListInputOrderNum_Type(Integer32):
    """Custom type ipeCfgAccessListInputOrderNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_IpeCfgAccessListInputOrderNum_Type.__name__ = "Integer32"
_IpeCfgAccessListInputOrderNum_Object = MibTableColumn
ipeCfgAccessListInputOrderNum = _IpeCfgAccessListInputOrderNum_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 21, 2, 1, 1),
    _IpeCfgAccessListInputOrderNum_Type()
)
ipeCfgAccessListInputOrderNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgAccessListInputOrderNum.setStatus("current")
_IpeCfgAccessListInputNEAddress_Type = IpAddress
_IpeCfgAccessListInputNEAddress_Object = MibTableColumn
ipeCfgAccessListInputNEAddress = _IpeCfgAccessListInputNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 21, 2, 1, 2),
    _IpeCfgAccessListInputNEAddress_Type()
)
ipeCfgAccessListInputNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgAccessListInputNEAddress.setStatus("current")


class _IpeCfgAccessListInputInIfIndex_Type(Integer32):
    """Custom type ipeCfgAccessListInputInIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("inband", 3),
          ("ne2", 4),
          ("bridge1", 11),
          ("bridge2", 12),
          ("bridge3", 13),
          ("bridge4", 14),
          ("bridge5", 15),
          ("bridge6", 16),
          ("bridge7", 17),
          ("bridge8", 18),
          ("bridge9", 19),
          ("bridge10", 20),
          ("bridge11", 21),
          ("bridge12", 22),
          ("bridge13", 23),
          ("bridge14", 24),
          ("bridge15", 25),
          ("bridge16", 26),
          ("bridge17", 27),
          ("bridge18", 28),
          ("bridge19", 29),
          ("bridge20", 30))
    )


_IpeCfgAccessListInputInIfIndex_Type.__name__ = "Integer32"
_IpeCfgAccessListInputInIfIndex_Object = MibTableColumn
ipeCfgAccessListInputInIfIndex = _IpeCfgAccessListInputInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 21, 2, 1, 3),
    _IpeCfgAccessListInputInIfIndex_Type()
)
ipeCfgAccessListInputInIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgAccessListInputInIfIndex.setStatus("current")
_IpeCfgAccessListInputSrcIpAddress_Type = IpAddress
_IpeCfgAccessListInputSrcIpAddress_Object = MibTableColumn
ipeCfgAccessListInputSrcIpAddress = _IpeCfgAccessListInputSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 21, 2, 1, 4),
    _IpeCfgAccessListInputSrcIpAddress_Type()
)
ipeCfgAccessListInputSrcIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgAccessListInputSrcIpAddress.setStatus("current")
_IpeCfgAccessListInputSrcNetMask_Type = IpAddress
_IpeCfgAccessListInputSrcNetMask_Object = MibTableColumn
ipeCfgAccessListInputSrcNetMask = _IpeCfgAccessListInputSrcNetMask_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 21, 2, 1, 5),
    _IpeCfgAccessListInputSrcNetMask_Type()
)
ipeCfgAccessListInputSrcNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgAccessListInputSrcNetMask.setStatus("current")
_IpeCfgAccessListInputProtocol_Type = Integer32
_IpeCfgAccessListInputProtocol_Object = MibTableColumn
ipeCfgAccessListInputProtocol = _IpeCfgAccessListInputProtocol_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 21, 2, 1, 6),
    _IpeCfgAccessListInputProtocol_Type()
)
ipeCfgAccessListInputProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgAccessListInputProtocol.setStatus("current")
_IpeCfgAccessListInputDstPortNum_Type = Integer32
_IpeCfgAccessListInputDstPortNum_Object = MibTableColumn
ipeCfgAccessListInputDstPortNum = _IpeCfgAccessListInputDstPortNum_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 21, 2, 1, 7),
    _IpeCfgAccessListInputDstPortNum_Type()
)
ipeCfgAccessListInputDstPortNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgAccessListInputDstPortNum.setStatus("current")


class _IpeCfgAccessListInputAction_Type(Integer32):
    """Custom type ipeCfgAccessListInputAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_IpeCfgAccessListInputAction_Type.__name__ = "Integer32"
_IpeCfgAccessListInputAction_Object = MibTableColumn
ipeCfgAccessListInputAction = _IpeCfgAccessListInputAction_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 21, 2, 1, 8),
    _IpeCfgAccessListInputAction_Type()
)
ipeCfgAccessListInputAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgAccessListInputAction.setStatus("current")


class _IpeCfgAccessListInputRowStatus_Type(RowStatus):
    """Custom type ipeCfgAccessListInputRowStatus based on RowStatus"""
    subtypeSpec = RowStatus.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("destroy", 6))
    )


_IpeCfgAccessListInputRowStatus_Type.__name__ = "RowStatus"
_IpeCfgAccessListInputRowStatus_Object = MibTableColumn
ipeCfgAccessListInputRowStatus = _IpeCfgAccessListInputRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 21, 2, 1, 9),
    _IpeCfgAccessListInputRowStatus_Type()
)
ipeCfgAccessListInputRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgAccessListInputRowStatus.setStatus("current")
_IpeCfgAccessListForwardTable_Object = MibTable
ipeCfgAccessListForwardTable = _IpeCfgAccessListForwardTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 21, 3)
)
if mibBuilder.loadTexts:
    ipeCfgAccessListForwardTable.setStatus("current")
_IpeCfgAccessListForwardEntry_Object = MibTableRow
ipeCfgAccessListForwardEntry = _IpeCfgAccessListForwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 21, 3, 1)
)
ipeCfgAccessListForwardEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeCfgAccessListForwardOrderNum"),
)
if mibBuilder.loadTexts:
    ipeCfgAccessListForwardEntry.setStatus("current")


class _IpeCfgAccessListForwardOrderNum_Type(Integer32):
    """Custom type ipeCfgAccessListForwardOrderNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_IpeCfgAccessListForwardOrderNum_Type.__name__ = "Integer32"
_IpeCfgAccessListForwardOrderNum_Object = MibTableColumn
ipeCfgAccessListForwardOrderNum = _IpeCfgAccessListForwardOrderNum_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 21, 3, 1, 1),
    _IpeCfgAccessListForwardOrderNum_Type()
)
ipeCfgAccessListForwardOrderNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgAccessListForwardOrderNum.setStatus("current")
_IpeCfgAccessListForwardNEAddress_Type = IpAddress
_IpeCfgAccessListForwardNEAddress_Object = MibTableColumn
ipeCfgAccessListForwardNEAddress = _IpeCfgAccessListForwardNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 21, 3, 1, 2),
    _IpeCfgAccessListForwardNEAddress_Type()
)
ipeCfgAccessListForwardNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgAccessListForwardNEAddress.setStatus("current")


class _IpeCfgAccessListForwardInIfIndex_Type(Integer32):
    """Custom type ipeCfgAccessListForwardInIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("inband", 3),
          ("ne2", 4),
          ("bridge1", 11),
          ("bridge2", 12),
          ("bridge3", 13),
          ("bridge4", 14),
          ("bridge5", 15),
          ("bridge6", 16),
          ("bridge7", 17),
          ("bridge8", 18),
          ("bridge9", 19),
          ("bridge10", 20),
          ("bridge11", 21),
          ("bridge12", 22),
          ("bridge13", 23),
          ("bridge14", 24),
          ("bridge15", 25),
          ("bridge16", 26),
          ("bridge17", 27),
          ("bridge18", 28),
          ("bridge19", 29),
          ("bridge20", 30))
    )


_IpeCfgAccessListForwardInIfIndex_Type.__name__ = "Integer32"
_IpeCfgAccessListForwardInIfIndex_Object = MibTableColumn
ipeCfgAccessListForwardInIfIndex = _IpeCfgAccessListForwardInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 21, 3, 1, 3),
    _IpeCfgAccessListForwardInIfIndex_Type()
)
ipeCfgAccessListForwardInIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgAccessListForwardInIfIndex.setStatus("current")


class _IpeCfgAccessListForwardOutIfIndex_Type(Integer32):
    """Custom type ipeCfgAccessListForwardOutIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("inband", 3),
          ("ne2", 4),
          ("bridge1", 11),
          ("bridge2", 12),
          ("bridge3", 13),
          ("bridge4", 14),
          ("bridge5", 15),
          ("bridge6", 16),
          ("bridge7", 17),
          ("bridge8", 18),
          ("bridge9", 19),
          ("bridge10", 20),
          ("bridge11", 21),
          ("bridge12", 22),
          ("bridge13", 23),
          ("bridge14", 24),
          ("bridge15", 25),
          ("bridge16", 26),
          ("bridge17", 27),
          ("bridge18", 28),
          ("bridge19", 29),
          ("bridge20", 30))
    )


_IpeCfgAccessListForwardOutIfIndex_Type.__name__ = "Integer32"
_IpeCfgAccessListForwardOutIfIndex_Object = MibTableColumn
ipeCfgAccessListForwardOutIfIndex = _IpeCfgAccessListForwardOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 21, 3, 1, 4),
    _IpeCfgAccessListForwardOutIfIndex_Type()
)
ipeCfgAccessListForwardOutIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgAccessListForwardOutIfIndex.setStatus("current")
_IpeCfgAccessListForwardSrcIpAddress_Type = IpAddress
_IpeCfgAccessListForwardSrcIpAddress_Object = MibTableColumn
ipeCfgAccessListForwardSrcIpAddress = _IpeCfgAccessListForwardSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 21, 3, 1, 5),
    _IpeCfgAccessListForwardSrcIpAddress_Type()
)
ipeCfgAccessListForwardSrcIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgAccessListForwardSrcIpAddress.setStatus("current")
_IpeCfgAccessListForwardSrcNetMask_Type = IpAddress
_IpeCfgAccessListForwardSrcNetMask_Object = MibTableColumn
ipeCfgAccessListForwardSrcNetMask = _IpeCfgAccessListForwardSrcNetMask_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 21, 3, 1, 6),
    _IpeCfgAccessListForwardSrcNetMask_Type()
)
ipeCfgAccessListForwardSrcNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgAccessListForwardSrcNetMask.setStatus("current")
_IpeCfgAccessListForwardDstIpAddress_Type = IpAddress
_IpeCfgAccessListForwardDstIpAddress_Object = MibTableColumn
ipeCfgAccessListForwardDstIpAddress = _IpeCfgAccessListForwardDstIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 21, 3, 1, 7),
    _IpeCfgAccessListForwardDstIpAddress_Type()
)
ipeCfgAccessListForwardDstIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgAccessListForwardDstIpAddress.setStatus("current")
_IpeCfgAccessListForwardDstNetMask_Type = IpAddress
_IpeCfgAccessListForwardDstNetMask_Object = MibTableColumn
ipeCfgAccessListForwardDstNetMask = _IpeCfgAccessListForwardDstNetMask_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 21, 3, 1, 8),
    _IpeCfgAccessListForwardDstNetMask_Type()
)
ipeCfgAccessListForwardDstNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgAccessListForwardDstNetMask.setStatus("current")
_IpeCfgAccessListForwardProtocol_Type = Integer32
_IpeCfgAccessListForwardProtocol_Object = MibTableColumn
ipeCfgAccessListForwardProtocol = _IpeCfgAccessListForwardProtocol_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 21, 3, 1, 9),
    _IpeCfgAccessListForwardProtocol_Type()
)
ipeCfgAccessListForwardProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgAccessListForwardProtocol.setStatus("current")
_IpeCfgAccessListForwardSrcPortNum_Type = Integer32
_IpeCfgAccessListForwardSrcPortNum_Object = MibTableColumn
ipeCfgAccessListForwardSrcPortNum = _IpeCfgAccessListForwardSrcPortNum_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 21, 3, 1, 10),
    _IpeCfgAccessListForwardSrcPortNum_Type()
)
ipeCfgAccessListForwardSrcPortNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgAccessListForwardSrcPortNum.setStatus("current")
_IpeCfgAccessListForwardDstPortNum_Type = Integer32
_IpeCfgAccessListForwardDstPortNum_Object = MibTableColumn
ipeCfgAccessListForwardDstPortNum = _IpeCfgAccessListForwardDstPortNum_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 21, 3, 1, 11),
    _IpeCfgAccessListForwardDstPortNum_Type()
)
ipeCfgAccessListForwardDstPortNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgAccessListForwardDstPortNum.setStatus("current")


class _IpeCfgAccessListForwardAction_Type(Integer32):
    """Custom type ipeCfgAccessListForwardAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_IpeCfgAccessListForwardAction_Type.__name__ = "Integer32"
_IpeCfgAccessListForwardAction_Object = MibTableColumn
ipeCfgAccessListForwardAction = _IpeCfgAccessListForwardAction_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 21, 3, 1, 12),
    _IpeCfgAccessListForwardAction_Type()
)
ipeCfgAccessListForwardAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgAccessListForwardAction.setStatus("current")


class _IpeCfgAccessListForwardRowStatus_Type(RowStatus):
    """Custom type ipeCfgAccessListForwardRowStatus based on RowStatus"""
    subtypeSpec = RowStatus.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("destroy", 6))
    )


_IpeCfgAccessListForwardRowStatus_Type.__name__ = "RowStatus"
_IpeCfgAccessListForwardRowStatus_Object = MibTableColumn
ipeCfgAccessListForwardRowStatus = _IpeCfgAccessListForwardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 21, 3, 1, 13),
    _IpeCfgAccessListForwardRowStatus_Type()
)
ipeCfgAccessListForwardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgAccessListForwardRowStatus.setStatus("current")
_IpeCfgAutoIpGroup_ObjectIdentity = ObjectIdentity
ipeCfgAutoIpGroup = _IpeCfgAutoIpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 22)
)
_IpeCfgAutoIpTable_Object = MibTable
ipeCfgAutoIpTable = _IpeCfgAutoIpTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 22, 1)
)
if mibBuilder.loadTexts:
    ipeCfgAutoIpTable.setStatus("current")
_IpeCfgAutoIpEntry_Object = MibTableRow
ipeCfgAutoIpEntry = _IpeCfgAutoIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 22, 1, 1)
)
ipeCfgAutoIpEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeCfgAutoIpIndex"),
)
if mibBuilder.loadTexts:
    ipeCfgAutoIpEntry.setStatus("current")


class _IpeCfgAutoIpIndex_Type(Integer32):
    """Custom type ipeCfgAutoIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_IpeCfgAutoIpIndex_Type.__name__ = "Integer32"
_IpeCfgAutoIpIndex_Object = MibTableColumn
ipeCfgAutoIpIndex = _IpeCfgAutoIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 22, 1, 1, 1),
    _IpeCfgAutoIpIndex_Type()
)
ipeCfgAutoIpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgAutoIpIndex.setStatus("current")
_IpeCfgAutoIpNEAddress_Type = IpAddress
_IpeCfgAutoIpNEAddress_Object = MibTableColumn
ipeCfgAutoIpNEAddress = _IpeCfgAutoIpNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 22, 1, 1, 2),
    _IpeCfgAutoIpNEAddress_Type()
)
ipeCfgAutoIpNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgAutoIpNEAddress.setStatus("current")
_IpeCfgAutoIpNetworkAddress_Type = IpAddress
_IpeCfgAutoIpNetworkAddress_Object = MibTableColumn
ipeCfgAutoIpNetworkAddress = _IpeCfgAutoIpNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 22, 1, 1, 3),
    _IpeCfgAutoIpNetworkAddress_Type()
)
ipeCfgAutoIpNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgAutoIpNetworkAddress.setStatus("current")
_IpeCfgAutoIpNetMask_Type = IpAddress
_IpeCfgAutoIpNetMask_Object = MibTableColumn
ipeCfgAutoIpNetMask = _IpeCfgAutoIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 22, 1, 1, 4),
    _IpeCfgAutoIpNetMask_Type()
)
ipeCfgAutoIpNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgAutoIpNetMask.setStatus("current")
_IpeCfgSysNE1PortTable_Object = MibTable
ipeCfgSysNE1PortTable = _IpeCfgSysNE1PortTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 25)
)
if mibBuilder.loadTexts:
    ipeCfgSysNE1PortTable.setStatus("current")
_IpeCfgSysNE1PortEntry_Object = MibTableRow
ipeCfgSysNE1PortEntry = _IpeCfgSysNE1PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 25, 1)
)
ipeCfgSysNE1PortEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeCfgSysNE1PortIndex"),
)
if mibBuilder.loadTexts:
    ipeCfgSysNE1PortEntry.setStatus("current")


class _IpeCfgSysNE1PortIndex_Type(Integer32):
    """Custom type ipeCfgSysNE1PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_IpeCfgSysNE1PortIndex_Type.__name__ = "Integer32"
_IpeCfgSysNE1PortIndex_Object = MibTableColumn
ipeCfgSysNE1PortIndex = _IpeCfgSysNE1PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 25, 1, 1),
    _IpeCfgSysNE1PortIndex_Type()
)
ipeCfgSysNE1PortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgSysNE1PortIndex.setStatus("current")
_IpeCfgSysNE1PortNEAddress_Type = IpAddress
_IpeCfgSysNE1PortNEAddress_Object = MibTableColumn
ipeCfgSysNE1PortNEAddress = _IpeCfgSysNE1PortNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 25, 1, 2),
    _IpeCfgSysNE1PortNEAddress_Type()
)
ipeCfgSysNE1PortNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgSysNE1PortNEAddress.setStatus("current")


class _IpeCfgSysNE1PortMode_Type(Integer32):
    """Custom type ipeCfgSysNE1PortMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("userPort", 1),
          ("mgmtPort", 2))
    )


_IpeCfgSysNE1PortMode_Type.__name__ = "Integer32"
_IpeCfgSysNE1PortMode_Object = MibTableColumn
ipeCfgSysNE1PortMode = _IpeCfgSysNE1PortMode_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 25, 1, 3),
    _IpeCfgSysNE1PortMode_Type()
)
ipeCfgSysNE1PortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgSysNE1PortMode.setStatus("current")
_IpeCfgRadiusGroup_ObjectIdentity = ObjectIdentity
ipeCfgRadiusGroup = _IpeCfgRadiusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 27)
)
_IpeCfgRadiusGeneralTable_Object = MibTable
ipeCfgRadiusGeneralTable = _IpeCfgRadiusGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 27, 1)
)
if mibBuilder.loadTexts:
    ipeCfgRadiusGeneralTable.setStatus("current")
_IpeCfgRadiusGeneralEntry_Object = MibTableRow
ipeCfgRadiusGeneralEntry = _IpeCfgRadiusGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 27, 1, 1)
)
ipeCfgRadiusGeneralEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeCfgRadiusGeneralIndex"),
)
if mibBuilder.loadTexts:
    ipeCfgRadiusGeneralEntry.setStatus("current")


class _IpeCfgRadiusGeneralIndex_Type(Integer32):
    """Custom type ipeCfgRadiusGeneralIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_IpeCfgRadiusGeneralIndex_Type.__name__ = "Integer32"
_IpeCfgRadiusGeneralIndex_Object = MibTableColumn
ipeCfgRadiusGeneralIndex = _IpeCfgRadiusGeneralIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 27, 1, 1, 1),
    _IpeCfgRadiusGeneralIndex_Type()
)
ipeCfgRadiusGeneralIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgRadiusGeneralIndex.setStatus("current")
_IpeCfgRadiusGeneralNEAddress_Type = IpAddress
_IpeCfgRadiusGeneralNEAddress_Object = MibTableColumn
ipeCfgRadiusGeneralNEAddress = _IpeCfgRadiusGeneralNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 27, 1, 1, 2),
    _IpeCfgRadiusGeneralNEAddress_Type()
)
ipeCfgRadiusGeneralNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgRadiusGeneralNEAddress.setStatus("current")


class _IpeCfgRadiusGeneralAuthClientRetransmit_Type(Integer32):
    """Custom type ipeCfgRadiusGeneralAuthClientRetransmit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpeCfgRadiusGeneralAuthClientRetransmit_Type.__name__ = "Integer32"
_IpeCfgRadiusGeneralAuthClientRetransmit_Object = MibTableColumn
ipeCfgRadiusGeneralAuthClientRetransmit = _IpeCfgRadiusGeneralAuthClientRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 27, 1, 1, 3),
    _IpeCfgRadiusGeneralAuthClientRetransmit_Type()
)
ipeCfgRadiusGeneralAuthClientRetransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgRadiusGeneralAuthClientRetransmit.setStatus("current")


class _IpeCfgRadiusGeneralAuthClientTimeout_Type(Integer32):
    """Custom type ipeCfgRadiusGeneralAuthClientTimeout based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpeCfgRadiusGeneralAuthClientTimeout_Type.__name__ = "Integer32"
_IpeCfgRadiusGeneralAuthClientTimeout_Object = MibTableColumn
ipeCfgRadiusGeneralAuthClientTimeout = _IpeCfgRadiusGeneralAuthClientTimeout_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 27, 1, 1, 4),
    _IpeCfgRadiusGeneralAuthClientTimeout_Type()
)
ipeCfgRadiusGeneralAuthClientTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgRadiusGeneralAuthClientTimeout.setStatus("current")
if mibBuilder.loadTexts:
    ipeCfgRadiusGeneralAuthClientTimeout.setUnits("seconds")
_IpeCfgRadiusAuthServerExtTable_Object = MibTable
ipeCfgRadiusAuthServerExtTable = _IpeCfgRadiusAuthServerExtTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 27, 2)
)
if mibBuilder.loadTexts:
    ipeCfgRadiusAuthServerExtTable.setStatus("current")
_IpeCfgRadiusAuthServerExtEntry_Object = MibTableRow
ipeCfgRadiusAuthServerExtEntry = _IpeCfgRadiusAuthServerExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 27, 2, 1)
)
ipeCfgRadiusAuthServerExtEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeCfgRadiusAuthServerExtIndex"),
)
if mibBuilder.loadTexts:
    ipeCfgRadiusAuthServerExtEntry.setStatus("current")


class _IpeCfgRadiusAuthServerExtIndex_Type(Integer32):
    """Custom type ipeCfgRadiusAuthServerExtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_IpeCfgRadiusAuthServerExtIndex_Type.__name__ = "Integer32"
_IpeCfgRadiusAuthServerExtIndex_Object = MibTableColumn
ipeCfgRadiusAuthServerExtIndex = _IpeCfgRadiusAuthServerExtIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 27, 2, 1, 1),
    _IpeCfgRadiusAuthServerExtIndex_Type()
)
ipeCfgRadiusAuthServerExtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgRadiusAuthServerExtIndex.setStatus("current")
_IpeCfgRadiusAuthServerNEAddress_Type = IpAddress
_IpeCfgRadiusAuthServerNEAddress_Object = MibTableColumn
ipeCfgRadiusAuthServerNEAddress = _IpeCfgRadiusAuthServerNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 27, 2, 1, 2),
    _IpeCfgRadiusAuthServerNEAddress_Type()
)
ipeCfgRadiusAuthServerNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgRadiusAuthServerNEAddress.setStatus("current")


class _IpeCfgRadiusAuthServerAddressType_Type(Integer32):
    """Custom type ipeCfgRadiusAuthServerAddressType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("ipv4", 1),
          ("ipv6", 2))
    )


_IpeCfgRadiusAuthServerAddressType_Type.__name__ = "Integer32"
_IpeCfgRadiusAuthServerAddressType_Object = MibTableColumn
ipeCfgRadiusAuthServerAddressType = _IpeCfgRadiusAuthServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 27, 2, 1, 3),
    _IpeCfgRadiusAuthServerAddressType_Type()
)
ipeCfgRadiusAuthServerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgRadiusAuthServerAddressType.setStatus("current")
_IpeCfgRadiusAuthServerAddress_Type = IpAddress
_IpeCfgRadiusAuthServerAddress_Object = MibTableColumn
ipeCfgRadiusAuthServerAddress = _IpeCfgRadiusAuthServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 27, 2, 1, 4),
    _IpeCfgRadiusAuthServerAddress_Type()
)
ipeCfgRadiusAuthServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgRadiusAuthServerAddress.setStatus("current")


class _IpeCfgRadiusAuthClientServerPortNumber_Type(Integer32):
    """Custom type ipeCfgRadiusAuthClientServerPortNumber based on Integer32"""
    defaultValue = 1812

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpeCfgRadiusAuthClientServerPortNumber_Type.__name__ = "Integer32"
_IpeCfgRadiusAuthClientServerPortNumber_Object = MibTableColumn
ipeCfgRadiusAuthClientServerPortNumber = _IpeCfgRadiusAuthClientServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 27, 2, 1, 5),
    _IpeCfgRadiusAuthClientServerPortNumber_Type()
)
ipeCfgRadiusAuthClientServerPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgRadiusAuthClientServerPortNumber.setStatus("current")


class _IpeCfgRadiusAuthClientPasswordType_Type(Integer32):
    """Custom type ipeCfgRadiusAuthClientPasswordType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("user", 1),
          ("chap", 2))
    )


_IpeCfgRadiusAuthClientPasswordType_Type.__name__ = "Integer32"
_IpeCfgRadiusAuthClientPasswordType_Object = MibTableColumn
ipeCfgRadiusAuthClientPasswordType = _IpeCfgRadiusAuthClientPasswordType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 27, 2, 1, 6),
    _IpeCfgRadiusAuthClientPasswordType_Type()
)
ipeCfgRadiusAuthClientPasswordType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgRadiusAuthClientPasswordType.setStatus("current")


class _IpeCfgRadiusAuthClientSecretKey_Type(DisplayString):
    """Custom type ipeCfgRadiusAuthClientSecretKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 128),
    )


_IpeCfgRadiusAuthClientSecretKey_Type.__name__ = "DisplayString"
_IpeCfgRadiusAuthClientSecretKey_Object = MibTableColumn
ipeCfgRadiusAuthClientSecretKey = _IpeCfgRadiusAuthClientSecretKey_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 27, 2, 1, 7),
    _IpeCfgRadiusAuthClientSecretKey_Type()
)
ipeCfgRadiusAuthClientSecretKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgRadiusAuthClientSecretKey.setStatus("current")
_IpeCfgRadiusAuthServerExtRowStatus_Type = RowStatus
_IpeCfgRadiusAuthServerExtRowStatus_Object = MibTableColumn
ipeCfgRadiusAuthServerExtRowStatus = _IpeCfgRadiusAuthServerExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 27, 2, 1, 8),
    _IpeCfgRadiusAuthServerExtRowStatus_Type()
)
ipeCfgRadiusAuthServerExtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgRadiusAuthServerExtRowStatus.setStatus("current")
_IpeCfgRadiusPrivLevelGeneralTable_Object = MibTable
ipeCfgRadiusPrivLevelGeneralTable = _IpeCfgRadiusPrivLevelGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 27, 3)
)
if mibBuilder.loadTexts:
    ipeCfgRadiusPrivLevelGeneralTable.setStatus("current")
_IpeCfgRadiusPrivLevelGeneralEntry_Object = MibTableRow
ipeCfgRadiusPrivLevelGeneralEntry = _IpeCfgRadiusPrivLevelGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 27, 3, 1)
)
ipeCfgRadiusPrivLevelGeneralEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeCfgRadiusPrivLevelGeneralIndex"),
)
if mibBuilder.loadTexts:
    ipeCfgRadiusPrivLevelGeneralEntry.setStatus("current")


class _IpeCfgRadiusPrivLevelGeneralIndex_Type(Integer32):
    """Custom type ipeCfgRadiusPrivLevelGeneralIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_IpeCfgRadiusPrivLevelGeneralIndex_Type.__name__ = "Integer32"
_IpeCfgRadiusPrivLevelGeneralIndex_Object = MibTableColumn
ipeCfgRadiusPrivLevelGeneralIndex = _IpeCfgRadiusPrivLevelGeneralIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 27, 3, 1, 1),
    _IpeCfgRadiusPrivLevelGeneralIndex_Type()
)
ipeCfgRadiusPrivLevelGeneralIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgRadiusPrivLevelGeneralIndex.setStatus("current")
_IpeCfgRadiusPrivLevelGeneralNEAddress_Type = IpAddress
_IpeCfgRadiusPrivLevelGeneralNEAddress_Object = MibTableColumn
ipeCfgRadiusPrivLevelGeneralNEAddress = _IpeCfgRadiusPrivLevelGeneralNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 27, 3, 1, 2),
    _IpeCfgRadiusPrivLevelGeneralNEAddress_Type()
)
ipeCfgRadiusPrivLevelGeneralNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgRadiusPrivLevelGeneralNEAddress.setStatus("current")


class _IpeCfgRadiusPrivLevelGeneralDefaultAction_Type(Integer32):
    """Custom type ipeCfgRadiusPrivLevelGeneralDefaultAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("denyLogin", 1),
          ("useDefaultGroup", 2))
    )


_IpeCfgRadiusPrivLevelGeneralDefaultAction_Type.__name__ = "Integer32"
_IpeCfgRadiusPrivLevelGeneralDefaultAction_Object = MibTableColumn
ipeCfgRadiusPrivLevelGeneralDefaultAction = _IpeCfgRadiusPrivLevelGeneralDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 27, 3, 1, 3),
    _IpeCfgRadiusPrivLevelGeneralDefaultAction_Type()
)
ipeCfgRadiusPrivLevelGeneralDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgRadiusPrivLevelGeneralDefaultAction.setStatus("current")


class _IpeCfgRadiusPrivLevelGeneralDefaultGroup_Type(DisplayString):
    """Custom type ipeCfgRadiusPrivLevelGeneralDefaultGroup based on DisplayString"""
    defaultValue = OctetString("Operator")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpeCfgRadiusPrivLevelGeneralDefaultGroup_Type.__name__ = "DisplayString"
_IpeCfgRadiusPrivLevelGeneralDefaultGroup_Object = MibTableColumn
ipeCfgRadiusPrivLevelGeneralDefaultGroup = _IpeCfgRadiusPrivLevelGeneralDefaultGroup_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 27, 3, 1, 4),
    _IpeCfgRadiusPrivLevelGeneralDefaultGroup_Type()
)
ipeCfgRadiusPrivLevelGeneralDefaultGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgRadiusPrivLevelGeneralDefaultGroup.setStatus("current")
_IpeCfgRadiusGroupPrivLevelMappingTable_Object = MibTable
ipeCfgRadiusGroupPrivLevelMappingTable = _IpeCfgRadiusGroupPrivLevelMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 27, 4)
)
if mibBuilder.loadTexts:
    ipeCfgRadiusGroupPrivLevelMappingTable.setStatus("current")
_IpeCfgRadiusGroupPrivLevelMappingEntry_Object = MibTableRow
ipeCfgRadiusGroupPrivLevelMappingEntry = _IpeCfgRadiusGroupPrivLevelMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 27, 4, 1)
)
ipeCfgRadiusGroupPrivLevelMappingEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeCfgRadiusGroupPrivLevelMappingPrivLevel"),
)
if mibBuilder.loadTexts:
    ipeCfgRadiusGroupPrivLevelMappingEntry.setStatus("current")


class _IpeCfgRadiusGroupPrivLevelMappingPrivLevel_Type(Integer32):
    """Custom type ipeCfgRadiusGroupPrivLevelMappingPrivLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_IpeCfgRadiusGroupPrivLevelMappingPrivLevel_Type.__name__ = "Integer32"
_IpeCfgRadiusGroupPrivLevelMappingPrivLevel_Object = MibTableColumn
ipeCfgRadiusGroupPrivLevelMappingPrivLevel = _IpeCfgRadiusGroupPrivLevelMappingPrivLevel_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 27, 4, 1, 1),
    _IpeCfgRadiusGroupPrivLevelMappingPrivLevel_Type()
)
ipeCfgRadiusGroupPrivLevelMappingPrivLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgRadiusGroupPrivLevelMappingPrivLevel.setStatus("current")
_IpeCfgRadiusGroupPrivLevelMappingNEAddress_Type = IpAddress
_IpeCfgRadiusGroupPrivLevelMappingNEAddress_Object = MibTableColumn
ipeCfgRadiusGroupPrivLevelMappingNEAddress = _IpeCfgRadiusGroupPrivLevelMappingNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 27, 4, 1, 2),
    _IpeCfgRadiusGroupPrivLevelMappingNEAddress_Type()
)
ipeCfgRadiusGroupPrivLevelMappingNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgRadiusGroupPrivLevelMappingNEAddress.setStatus("current")


class _IpeCfgRadiusGroupPrivLevelMappingEnable_Type(Integer32):
    """Custom type ipeCfgRadiusGroupPrivLevelMappingEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("disable", 1),
          ("enable", 2))
    )


_IpeCfgRadiusGroupPrivLevelMappingEnable_Type.__name__ = "Integer32"
_IpeCfgRadiusGroupPrivLevelMappingEnable_Object = MibTableColumn
ipeCfgRadiusGroupPrivLevelMappingEnable = _IpeCfgRadiusGroupPrivLevelMappingEnable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 27, 4, 1, 3),
    _IpeCfgRadiusGroupPrivLevelMappingEnable_Type()
)
ipeCfgRadiusGroupPrivLevelMappingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgRadiusGroupPrivLevelMappingEnable.setStatus("current")


class _IpeCfgRadiusGroupPrivLevelMappingGroup_Type(DisplayString):
    """Custom type ipeCfgRadiusGroupPrivLevelMappingGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpeCfgRadiusGroupPrivLevelMappingGroup_Type.__name__ = "DisplayString"
_IpeCfgRadiusGroupPrivLevelMappingGroup_Object = MibTableColumn
ipeCfgRadiusGroupPrivLevelMappingGroup = _IpeCfgRadiusGroupPrivLevelMappingGroup_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 27, 4, 1, 4),
    _IpeCfgRadiusGroupPrivLevelMappingGroup_Type()
)
ipeCfgRadiusGroupPrivLevelMappingGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgRadiusGroupPrivLevelMappingGroup.setStatus("current")
_IpeCfgLldpGroup_ObjectIdentity = ObjectIdentity
ipeCfgLldpGroup = _IpeCfgLldpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 28)
)
_IpeCfgLldpTable_Object = MibTable
ipeCfgLldpTable = _IpeCfgLldpTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 28, 1)
)
if mibBuilder.loadTexts:
    ipeCfgLldpTable.setStatus("current")
_IpeCfgLldpEntry_Object = MibTableRow
ipeCfgLldpEntry = _IpeCfgLldpEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 28, 1, 1)
)
ipeCfgLldpEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeCfgLldpIndex"),
)
if mibBuilder.loadTexts:
    ipeCfgLldpEntry.setStatus("current")


class _IpeCfgLldpIndex_Type(Integer32):
    """Custom type ipeCfgLldpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_IpeCfgLldpIndex_Type.__name__ = "Integer32"
_IpeCfgLldpIndex_Object = MibTableColumn
ipeCfgLldpIndex = _IpeCfgLldpIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 28, 1, 1, 1),
    _IpeCfgLldpIndex_Type()
)
ipeCfgLldpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgLldpIndex.setStatus("current")
_IpeCfgLldpNEAddress_Type = IpAddress
_IpeCfgLldpNEAddress_Object = MibTableColumn
ipeCfgLldpNEAddress = _IpeCfgLldpNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 28, 1, 1, 2),
    _IpeCfgLldpNEAddress_Type()
)
ipeCfgLldpNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgLldpNEAddress.setStatus("current")


class _IpeCfgLldpProprietaryModeMacAddress_Type(MacAddress):
    """Custom type ipeCfgLldpProprietaryModeMacAddress based on MacAddress"""
    defaultHexValue = "01004c01da50"


_IpeCfgLldpProprietaryModeMacAddress_Type.__name__ = "MacAddress"
_IpeCfgLldpProprietaryModeMacAddress_Object = MibTableColumn
ipeCfgLldpProprietaryModeMacAddress = _IpeCfgLldpProprietaryModeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 28, 1, 1, 3),
    _IpeCfgLldpProprietaryModeMacAddress_Type()
)
ipeCfgLldpProprietaryModeMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgLldpProprietaryModeMacAddress.setStatus("current")
_IpeCommunicationsGroup_ObjectIdentity = ObjectIdentity
ipeCommunicationsGroup = _IpeCommunicationsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 4)
)
_IpeNeighborInfoTable_Object = MibTable
ipeNeighborInfoTable = _IpeNeighborInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 4, 1)
)
if mibBuilder.loadTexts:
    ipeNeighborInfoTable.setStatus("current")
_IpeNeighborInfoEntry_Object = MibTableRow
ipeNeighborInfoEntry = _IpeNeighborInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 4, 1, 1)
)
ipeNeighborInfoEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeNeighborInfoIndex"),
)
if mibBuilder.loadTexts:
    ipeNeighborInfoEntry.setStatus("current")
_IpeNeighborInfoIndex_Type = InterfaceIndex
_IpeNeighborInfoIndex_Object = MibTableColumn
ipeNeighborInfoIndex = _IpeNeighborInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 4, 1, 1, 1),
    _IpeNeighborInfoIndex_Type()
)
ipeNeighborInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeNeighborInfoIndex.setStatus("current")
_IpeNeighborInfoNEAddress_Type = IpAddress
_IpeNeighborInfoNEAddress_Object = MibTableColumn
ipeNeighborInfoNEAddress = _IpeNeighborInfoNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 4, 1, 1, 2),
    _IpeNeighborInfoNEAddress_Type()
)
ipeNeighborInfoNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeNeighborInfoNEAddress.setStatus("current")


class _IpeNeighborIpAddress_Type(OctetString):
    """Custom type ipeNeighborIpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 240),
    )


_IpeNeighborIpAddress_Type.__name__ = "OctetString"
_IpeNeighborIpAddress_Object = MibTableColumn
ipeNeighborIpAddress = _IpeNeighborIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 4, 1, 1, 3),
    _IpeNeighborIpAddress_Type()
)
ipeNeighborIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeNeighborIpAddress.setStatus("current")
_IpeStatusGroup_ObjectIdentity = ObjectIdentity
ipeStatusGroup = _IpeStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6)
)
_IpeStsNtp_ObjectIdentity = ObjectIdentity
ipeStsNtp = _IpeStsNtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 1)
)
_IpeStsNtpStatisticsTable_Object = MibTable
ipeStsNtpStatisticsTable = _IpeStsNtpStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 1, 1)
)
if mibBuilder.loadTexts:
    ipeStsNtpStatisticsTable.setStatus("current")
_IpeStsNtpStatisticsEntry_Object = MibTableRow
ipeStsNtpStatisticsEntry = _IpeStsNtpStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 1, 1, 1)
)
ipeStsNtpStatisticsEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeStsNtpStatisticsIndex"),
)
if mibBuilder.loadTexts:
    ipeStsNtpStatisticsEntry.setStatus("current")


class _IpeStsNtpStatisticsIndex_Type(Integer32):
    """Custom type ipeStsNtpStatisticsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_IpeStsNtpStatisticsIndex_Type.__name__ = "Integer32"
_IpeStsNtpStatisticsIndex_Object = MibTableColumn
ipeStsNtpStatisticsIndex = _IpeStsNtpStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 1, 1, 1, 1),
    _IpeStsNtpStatisticsIndex_Type()
)
ipeStsNtpStatisticsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeStsNtpStatisticsIndex.setStatus("current")
_IpeStsNtpStatisticsNEAddress_Type = IpAddress
_IpeStsNtpStatisticsNEAddress_Object = MibTableColumn
ipeStsNtpStatisticsNEAddress = _IpeStsNtpStatisticsNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 1, 1, 1, 2),
    _IpeStsNtpStatisticsNEAddress_Type()
)
ipeStsNtpStatisticsNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeStsNtpStatisticsNEAddress.setStatus("current")


class _IpeStsNtpSyncStatusInfo_Type(OctetString):
    """Custom type ipeStsNtpSyncStatusInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_IpeStsNtpSyncStatusInfo_Type.__name__ = "OctetString"
_IpeStsNtpSyncStatusInfo_Object = MibTableColumn
ipeStsNtpSyncStatusInfo = _IpeStsNtpSyncStatusInfo_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 1, 1, 1, 3),
    _IpeStsNtpSyncStatusInfo_Type()
)
ipeStsNtpSyncStatusInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeStsNtpSyncStatusInfo.setStatus("current")


class _IpeStsNtpSetTime_Type(Integer32):
    """Custom type ipeStsNtpSetTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notSetManually", 0),
          ("setManually", 1))
    )


_IpeStsNtpSetTime_Type.__name__ = "Integer32"
_IpeStsNtpSetTime_Object = MibTableColumn
ipeStsNtpSetTime = _IpeStsNtpSetTime_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 1, 1, 1, 4),
    _IpeStsNtpSetTime_Type()
)
ipeStsNtpSetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeStsNtpSetTime.setStatus("current")
_IpeStsFtp_ObjectIdentity = ObjectIdentity
ipeStsFtp = _IpeStsFtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 2)
)
_IpeStsFtpStatusTable_Object = MibTable
ipeStsFtpStatusTable = _IpeStsFtpStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 2, 1)
)
if mibBuilder.loadTexts:
    ipeStsFtpStatusTable.setStatus("current")
_IpeStsFtpStatusEntry_Object = MibTableRow
ipeStsFtpStatusEntry = _IpeStsFtpStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 2, 1, 1)
)
ipeStsFtpStatusEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeStsFtpStatusIndex"),
)
if mibBuilder.loadTexts:
    ipeStsFtpStatusEntry.setStatus("current")


class _IpeStsFtpStatusIndex_Type(Integer32):
    """Custom type ipeStsFtpStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_IpeStsFtpStatusIndex_Type.__name__ = "Integer32"
_IpeStsFtpStatusIndex_Object = MibTableColumn
ipeStsFtpStatusIndex = _IpeStsFtpStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 2, 1, 1, 1),
    _IpeStsFtpStatusIndex_Type()
)
ipeStsFtpStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeStsFtpStatusIndex.setStatus("current")
_IpeStsFtpStatusNEAddress_Type = IpAddress
_IpeStsFtpStatusNEAddress_Object = MibTableColumn
ipeStsFtpStatusNEAddress = _IpeStsFtpStatusNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 2, 1, 1, 2),
    _IpeStsFtpStatusNEAddress_Type()
)
ipeStsFtpStatusNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeStsFtpStatusNEAddress.setStatus("current")


class _IpeStsFtpStatusLoginUser_Type(DisplayString):
    """Custom type ipeStsFtpStatusLoginUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_IpeStsFtpStatusLoginUser_Type.__name__ = "DisplayString"
_IpeStsFtpStatusLoginUser_Object = MibTableColumn
ipeStsFtpStatusLoginUser = _IpeStsFtpStatusLoginUser_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 2, 1, 1, 3),
    _IpeStsFtpStatusLoginUser_Type()
)
ipeStsFtpStatusLoginUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeStsFtpStatusLoginUser.setStatus("current")
_IpeStsFtpStatusLoginIpAddress_Type = IpAddress
_IpeStsFtpStatusLoginIpAddress_Object = MibTableColumn
ipeStsFtpStatusLoginIpAddress = _IpeStsFtpStatusLoginIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 2, 1, 1, 4),
    _IpeStsFtpStatusLoginIpAddress_Type()
)
ipeStsFtpStatusLoginIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeStsFtpStatusLoginIpAddress.setStatus("current")
_IpeStsFtpStatusSessionId_Type = Integer32
_IpeStsFtpStatusSessionId_Object = MibTableColumn
ipeStsFtpStatusSessionId = _IpeStsFtpStatusSessionId_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 2, 1, 1, 5),
    _IpeStsFtpStatusSessionId_Type()
)
ipeStsFtpStatusSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeStsFtpStatusSessionId.setStatus("current")
_IpeStsSftp_ObjectIdentity = ObjectIdentity
ipeStsSftp = _IpeStsSftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 3)
)
_IpeStsSftpStatusTable_Object = MibTable
ipeStsSftpStatusTable = _IpeStsSftpStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 3, 1)
)
if mibBuilder.loadTexts:
    ipeStsSftpStatusTable.setStatus("current")
_IpeStsSftpStatusEntry_Object = MibTableRow
ipeStsSftpStatusEntry = _IpeStsSftpStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 3, 1, 1)
)
ipeStsSftpStatusEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeStsSftpStatusIndex"),
)
if mibBuilder.loadTexts:
    ipeStsSftpStatusEntry.setStatus("current")


class _IpeStsSftpStatusIndex_Type(Integer32):
    """Custom type ipeStsSftpStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_IpeStsSftpStatusIndex_Type.__name__ = "Integer32"
_IpeStsSftpStatusIndex_Object = MibTableColumn
ipeStsSftpStatusIndex = _IpeStsSftpStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 3, 1, 1, 1),
    _IpeStsSftpStatusIndex_Type()
)
ipeStsSftpStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeStsSftpStatusIndex.setStatus("current")
_IpeStsSftpStatusNEAddress_Type = IpAddress
_IpeStsSftpStatusNEAddress_Object = MibTableColumn
ipeStsSftpStatusNEAddress = _IpeStsSftpStatusNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 3, 1, 1, 2),
    _IpeStsSftpStatusNEAddress_Type()
)
ipeStsSftpStatusNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeStsSftpStatusNEAddress.setStatus("current")


class _IpeStsSftpStatusLoginUser_Type(DisplayString):
    """Custom type ipeStsSftpStatusLoginUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_IpeStsSftpStatusLoginUser_Type.__name__ = "DisplayString"
_IpeStsSftpStatusLoginUser_Object = MibTableColumn
ipeStsSftpStatusLoginUser = _IpeStsSftpStatusLoginUser_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 3, 1, 1, 3),
    _IpeStsSftpStatusLoginUser_Type()
)
ipeStsSftpStatusLoginUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeStsSftpStatusLoginUser.setStatus("current")
_IpeStsSftpStatusLoginIpAddress_Type = IpAddress
_IpeStsSftpStatusLoginIpAddress_Object = MibTableColumn
ipeStsSftpStatusLoginIpAddress = _IpeStsSftpStatusLoginIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 3, 1, 1, 4),
    _IpeStsSftpStatusLoginIpAddress_Type()
)
ipeStsSftpStatusLoginIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeStsSftpStatusLoginIpAddress.setStatus("current")
_IpeStsSftpStatusSessionId_Type = Integer32
_IpeStsSftpStatusSessionId_Object = MibTableColumn
ipeStsSftpStatusSessionId = _IpeStsSftpStatusSessionId_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 3, 1, 1, 5),
    _IpeStsSftpStatusSessionId_Type()
)
ipeStsSftpStatusSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeStsSftpStatusSessionId.setStatus("current")
_IpeStsHttp_ObjectIdentity = ObjectIdentity
ipeStsHttp = _IpeStsHttp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 4)
)
_IpeStsHttpStatusTable_Object = MibTable
ipeStsHttpStatusTable = _IpeStsHttpStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 4, 1)
)
if mibBuilder.loadTexts:
    ipeStsHttpStatusTable.setStatus("current")
_IpeStsHttpStatusEntry_Object = MibTableRow
ipeStsHttpStatusEntry = _IpeStsHttpStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 4, 1, 1)
)
ipeStsHttpStatusEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeStsHttpStatusIndex"),
)
if mibBuilder.loadTexts:
    ipeStsHttpStatusEntry.setStatus("current")


class _IpeStsHttpStatusIndex_Type(Integer32):
    """Custom type ipeStsHttpStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_IpeStsHttpStatusIndex_Type.__name__ = "Integer32"
_IpeStsHttpStatusIndex_Object = MibTableColumn
ipeStsHttpStatusIndex = _IpeStsHttpStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 4, 1, 1, 1),
    _IpeStsHttpStatusIndex_Type()
)
ipeStsHttpStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeStsHttpStatusIndex.setStatus("current")
_IpeStsHttpStatusNEAddress_Type = IpAddress
_IpeStsHttpStatusNEAddress_Object = MibTableColumn
ipeStsHttpStatusNEAddress = _IpeStsHttpStatusNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 4, 1, 1, 2),
    _IpeStsHttpStatusNEAddress_Type()
)
ipeStsHttpStatusNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeStsHttpStatusNEAddress.setStatus("current")


class _IpeStsHttpStatusLoginUser_Type(DisplayString):
    """Custom type ipeStsHttpStatusLoginUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_IpeStsHttpStatusLoginUser_Type.__name__ = "DisplayString"
_IpeStsHttpStatusLoginUser_Object = MibTableColumn
ipeStsHttpStatusLoginUser = _IpeStsHttpStatusLoginUser_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 4, 1, 1, 3),
    _IpeStsHttpStatusLoginUser_Type()
)
ipeStsHttpStatusLoginUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeStsHttpStatusLoginUser.setStatus("current")
_IpeStsHttpStatusLoginIpAddress_Type = IpAddress
_IpeStsHttpStatusLoginIpAddress_Object = MibTableColumn
ipeStsHttpStatusLoginIpAddress = _IpeStsHttpStatusLoginIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 4, 1, 1, 4),
    _IpeStsHttpStatusLoginIpAddress_Type()
)
ipeStsHttpStatusLoginIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeStsHttpStatusLoginIpAddress.setStatus("current")
_IpeStsHttpStatusSessionId_Type = Integer32
_IpeStsHttpStatusSessionId_Object = MibTableColumn
ipeStsHttpStatusSessionId = _IpeStsHttpStatusSessionId_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 4, 1, 1, 5),
    _IpeStsHttpStatusSessionId_Type()
)
ipeStsHttpStatusSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeStsHttpStatusSessionId.setStatus("current")
_IpeStsHttps_ObjectIdentity = ObjectIdentity
ipeStsHttps = _IpeStsHttps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 5)
)
_IpeStsHttpsStatusTable_Object = MibTable
ipeStsHttpsStatusTable = _IpeStsHttpsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 5, 1)
)
if mibBuilder.loadTexts:
    ipeStsHttpsStatusTable.setStatus("current")
_IpeStsHttpsStatusEntry_Object = MibTableRow
ipeStsHttpsStatusEntry = _IpeStsHttpsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 5, 1, 1)
)
ipeStsHttpsStatusEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeStsHttpsStatusIndex"),
)
if mibBuilder.loadTexts:
    ipeStsHttpsStatusEntry.setStatus("current")


class _IpeStsHttpsStatusIndex_Type(Integer32):
    """Custom type ipeStsHttpsStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_IpeStsHttpsStatusIndex_Type.__name__ = "Integer32"
_IpeStsHttpsStatusIndex_Object = MibTableColumn
ipeStsHttpsStatusIndex = _IpeStsHttpsStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 5, 1, 1, 1),
    _IpeStsHttpsStatusIndex_Type()
)
ipeStsHttpsStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeStsHttpsStatusIndex.setStatus("current")
_IpeStsHttpsStatusNEAddress_Type = IpAddress
_IpeStsHttpsStatusNEAddress_Object = MibTableColumn
ipeStsHttpsStatusNEAddress = _IpeStsHttpsStatusNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 5, 1, 1, 2),
    _IpeStsHttpsStatusNEAddress_Type()
)
ipeStsHttpsStatusNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeStsHttpsStatusNEAddress.setStatus("current")


class _IpeStsHttpsStatusLoginUser_Type(DisplayString):
    """Custom type ipeStsHttpsStatusLoginUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_IpeStsHttpsStatusLoginUser_Type.__name__ = "DisplayString"
_IpeStsHttpsStatusLoginUser_Object = MibTableColumn
ipeStsHttpsStatusLoginUser = _IpeStsHttpsStatusLoginUser_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 5, 1, 1, 3),
    _IpeStsHttpsStatusLoginUser_Type()
)
ipeStsHttpsStatusLoginUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeStsHttpsStatusLoginUser.setStatus("current")
_IpeStsHttpsStatusLoginIpAddress_Type = IpAddress
_IpeStsHttpsStatusLoginIpAddress_Object = MibTableColumn
ipeStsHttpsStatusLoginIpAddress = _IpeStsHttpsStatusLoginIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 5, 1, 1, 4),
    _IpeStsHttpsStatusLoginIpAddress_Type()
)
ipeStsHttpsStatusLoginIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeStsHttpsStatusLoginIpAddress.setStatus("current")
_IpeStsHttpsStatusSessionId_Type = Integer32
_IpeStsHttpsStatusSessionId_Object = MibTableColumn
ipeStsHttpsStatusSessionId = _IpeStsHttpsStatusSessionId_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 5, 1, 1, 5),
    _IpeStsHttpsStatusSessionId_Type()
)
ipeStsHttpsStatusSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeStsHttpsStatusSessionId.setStatus("current")
_IpeStsStp_ObjectIdentity = ObjectIdentity
ipeStsStp = _IpeStsStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 6)
)
_IpeStsStpBridgeTable_Object = MibTable
ipeStsStpBridgeTable = _IpeStsStpBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 6, 1)
)
if mibBuilder.loadTexts:
    ipeStsStpBridgeTable.setStatus("current")
_IpeStsStpBridgeEntry_Object = MibTableRow
ipeStsStpBridgeEntry = _IpeStsStpBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 6, 1, 1)
)
ipeStsStpBridgeEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeStsStpBridgeIndex"),
)
if mibBuilder.loadTexts:
    ipeStsStpBridgeEntry.setStatus("current")


class _IpeStsStpBridgeIndex_Type(Integer32):
    """Custom type ipeStsStpBridgeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_IpeStsStpBridgeIndex_Type.__name__ = "Integer32"
_IpeStsStpBridgeIndex_Object = MibTableColumn
ipeStsStpBridgeIndex = _IpeStsStpBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 6, 1, 1, 1),
    _IpeStsStpBridgeIndex_Type()
)
ipeStsStpBridgeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeStsStpBridgeIndex.setStatus("current")
_IpeStsStpBridgeNEAddress_Type = IpAddress
_IpeStsStpBridgeNEAddress_Object = MibTableColumn
ipeStsStpBridgeNEAddress = _IpeStsStpBridgeNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 6, 1, 1, 2),
    _IpeStsStpBridgeNEAddress_Type()
)
ipeStsStpBridgeNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeStsStpBridgeNEAddress.setStatus("current")


class _IpeStsStpBridgeProtocolSpecification_Type(Integer32):
    """Custom type ipeStsStpBridgeProtocolSpecification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("decLb100", 2),
          ("ieee8021d", 3))
    )


_IpeStsStpBridgeProtocolSpecification_Type.__name__ = "Integer32"
_IpeStsStpBridgeProtocolSpecification_Object = MibTableColumn
ipeStsStpBridgeProtocolSpecification = _IpeStsStpBridgeProtocolSpecification_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 6, 1, 1, 3),
    _IpeStsStpBridgeProtocolSpecification_Type()
)
ipeStsStpBridgeProtocolSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeStsStpBridgeProtocolSpecification.setStatus("current")
_IpeStsStpBridgeDesignatedRoot_Type = BridgeId
_IpeStsStpBridgeDesignatedRoot_Object = MibTableColumn
ipeStsStpBridgeDesignatedRoot = _IpeStsStpBridgeDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 6, 1, 1, 4),
    _IpeStsStpBridgeDesignatedRoot_Type()
)
ipeStsStpBridgeDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeStsStpBridgeDesignatedRoot.setStatus("current")
_IpeStsStpBridgeRootCost_Type = Integer32
_IpeStsStpBridgeRootCost_Object = MibTableColumn
ipeStsStpBridgeRootCost = _IpeStsStpBridgeRootCost_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 6, 1, 1, 5),
    _IpeStsStpBridgeRootCost_Type()
)
ipeStsStpBridgeRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeStsStpBridgeRootCost.setStatus("current")
_IpeStsStpBridgeRootPort_Type = Integer32
_IpeStsStpBridgeRootPort_Object = MibTableColumn
ipeStsStpBridgeRootPort = _IpeStsStpBridgeRootPort_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 6, 1, 1, 6),
    _IpeStsStpBridgeRootPort_Type()
)
ipeStsStpBridgeRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeStsStpBridgeRootPort.setStatus("current")
_IpeStsStpBridgeMaxAge_Type = Timeout
_IpeStsStpBridgeMaxAge_Object = MibTableColumn
ipeStsStpBridgeMaxAge = _IpeStsStpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 6, 1, 1, 7),
    _IpeStsStpBridgeMaxAge_Type()
)
ipeStsStpBridgeMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeStsStpBridgeMaxAge.setStatus("current")
_IpeStsStpBridgeHelloTime_Type = Timeout
_IpeStsStpBridgeHelloTime_Object = MibTableColumn
ipeStsStpBridgeHelloTime = _IpeStsStpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 6, 1, 1, 8),
    _IpeStsStpBridgeHelloTime_Type()
)
ipeStsStpBridgeHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeStsStpBridgeHelloTime.setStatus("current")
_IpeStsStpBridgeForwardDelay_Type = Timeout
_IpeStsStpBridgeForwardDelay_Object = MibTableColumn
ipeStsStpBridgeForwardDelay = _IpeStsStpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 6, 1, 1, 9),
    _IpeStsStpBridgeForwardDelay_Type()
)
ipeStsStpBridgeForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeStsStpBridgeForwardDelay.setStatus("current")
_IpeStsStpPortTable_Object = MibTable
ipeStsStpPortTable = _IpeStsStpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 6, 2)
)
if mibBuilder.loadTexts:
    ipeStsStpPortTable.setStatus("current")
_IpeStsStpPortEntry_Object = MibTableRow
ipeStsStpPortEntry = _IpeStsStpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 6, 2, 1)
)
ipeStsStpPortEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeStsStpPortIfIndex"),
    (0, "IPE-SYSTEM-MIB", "ipeStsStpPortBridgeIndex"),
)
if mibBuilder.loadTexts:
    ipeStsStpPortEntry.setStatus("current")
_IpeStsStpPortIfIndex_Type = InterfaceIndex
_IpeStsStpPortIfIndex_Object = MibTableColumn
ipeStsStpPortIfIndex = _IpeStsStpPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 6, 2, 1, 1),
    _IpeStsStpPortIfIndex_Type()
)
ipeStsStpPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeStsStpPortIfIndex.setStatus("current")


class _IpeStsStpPortBridgeIndex_Type(Integer32):
    """Custom type ipeStsStpPortBridgeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_IpeStsStpPortBridgeIndex_Type.__name__ = "Integer32"
_IpeStsStpPortBridgeIndex_Object = MibTableColumn
ipeStsStpPortBridgeIndex = _IpeStsStpPortBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 6, 2, 1, 2),
    _IpeStsStpPortBridgeIndex_Type()
)
ipeStsStpPortBridgeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeStsStpPortBridgeIndex.setStatus("current")
_IpeStsStpPortNEAddress_Type = IpAddress
_IpeStsStpPortNEAddress_Object = MibTableColumn
ipeStsStpPortNEAddress = _IpeStsStpPortNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 6, 2, 1, 3),
    _IpeStsStpPortNEAddress_Type()
)
ipeStsStpPortNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeStsStpPortNEAddress.setStatus("current")


class _IpeStsStpPortPortState_Type(Integer32):
    """Custom type ipeStsStpPortPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("blocking", 2),
          ("listening", 3),
          ("learning", 4),
          ("forwarding", 5),
          ("broken", 6))
    )


_IpeStsStpPortPortState_Type.__name__ = "Integer32"
_IpeStsStpPortPortState_Object = MibTableColumn
ipeStsStpPortPortState = _IpeStsStpPortPortState_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 6, 2, 1, 4),
    _IpeStsStpPortPortState_Type()
)
ipeStsStpPortPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeStsStpPortPortState.setStatus("current")
_IpeStsStpPortDesignatedRoot_Type = BridgeId
_IpeStsStpPortDesignatedRoot_Object = MibTableColumn
ipeStsStpPortDesignatedRoot = _IpeStsStpPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 6, 2, 1, 5),
    _IpeStsStpPortDesignatedRoot_Type()
)
ipeStsStpPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeStsStpPortDesignatedRoot.setStatus("current")
_IpeStsStpPortDesignatedCost_Type = Integer32
_IpeStsStpPortDesignatedCost_Object = MibTableColumn
ipeStsStpPortDesignatedCost = _IpeStsStpPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 6, 2, 1, 6),
    _IpeStsStpPortDesignatedCost_Type()
)
ipeStsStpPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeStsStpPortDesignatedCost.setStatus("current")
_IpeStsStpPortDesignatedBridge_Type = BridgeId
_IpeStsStpPortDesignatedBridge_Object = MibTableColumn
ipeStsStpPortDesignatedBridge = _IpeStsStpPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 6, 2, 1, 7),
    _IpeStsStpPortDesignatedBridge_Type()
)
ipeStsStpPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeStsStpPortDesignatedBridge.setStatus("current")


class _IpeStsStpPortDesignatedPort_Type(OctetString):
    """Custom type ipeStsStpPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_IpeStsStpPortDesignatedPort_Type.__name__ = "OctetString"
_IpeStsStpPortDesignatedPort_Object = MibTableColumn
ipeStsStpPortDesignatedPort = _IpeStsStpPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 6, 2, 1, 8),
    _IpeStsStpPortDesignatedPort_Type()
)
ipeStsStpPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeStsStpPortDesignatedPort.setStatus("current")
_IpeStsPort_ObjectIdentity = ObjectIdentity
ipeStsPort = _IpeStsPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 7)
)
_IpeStsPortEtherTable_Object = MibTable
ipeStsPortEtherTable = _IpeStsPortEtherTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 7, 1)
)
if mibBuilder.loadTexts:
    ipeStsPortEtherTable.setStatus("current")
_IpeStsPortEtherEntry_Object = MibTableRow
ipeStsPortEtherEntry = _IpeStsPortEtherEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 7, 1, 1)
)
ipeStsPortEtherEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeStsPortEtherIfIndex"),
)
if mibBuilder.loadTexts:
    ipeStsPortEtherEntry.setStatus("current")
_IpeStsPortEtherIfIndex_Type = InterfaceIndex
_IpeStsPortEtherIfIndex_Object = MibTableColumn
ipeStsPortEtherIfIndex = _IpeStsPortEtherIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 7, 1, 1, 1),
    _IpeStsPortEtherIfIndex_Type()
)
ipeStsPortEtherIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeStsPortEtherIfIndex.setStatus("current")
_IpeStsPortEtherNEAddress_Type = IpAddress
_IpeStsPortEtherNEAddress_Object = MibTableColumn
ipeStsPortEtherNEAddress = _IpeStsPortEtherNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 7, 1, 1, 2),
    _IpeStsPortEtherNEAddress_Type()
)
ipeStsPortEtherNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeStsPortEtherNEAddress.setStatus("current")
_IpeStsPortEtherLinkUp_Type = Integer32
_IpeStsPortEtherLinkUp_Object = MibTableColumn
ipeStsPortEtherLinkUp = _IpeStsPortEtherLinkUp_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 7, 1, 1, 3),
    _IpeStsPortEtherLinkUp_Type()
)
ipeStsPortEtherLinkUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeStsPortEtherLinkUp.setStatus("current")
_IpeStsPortEtherSpeed_Type = Integer32
_IpeStsPortEtherSpeed_Object = MibTableColumn
ipeStsPortEtherSpeed = _IpeStsPortEtherSpeed_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 7, 1, 1, 4),
    _IpeStsPortEtherSpeed_Type()
)
ipeStsPortEtherSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeStsPortEtherSpeed.setStatus("current")
_IpeStsPortEtherDuplex_Type = Integer32
_IpeStsPortEtherDuplex_Object = MibTableColumn
ipeStsPortEtherDuplex = _IpeStsPortEtherDuplex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 7, 1, 1, 5),
    _IpeStsPortEtherDuplex_Type()
)
ipeStsPortEtherDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeStsPortEtherDuplex.setStatus("current")
_IpeStsPortEtherFlowControl_Type = Integer32
_IpeStsPortEtherFlowControl_Object = MibTableColumn
ipeStsPortEtherFlowControl = _IpeStsPortEtherFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 7, 1, 1, 6),
    _IpeStsPortEtherFlowControl_Type()
)
ipeStsPortEtherFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeStsPortEtherFlowControl.setStatus("current")
_IpeStsPortNe2Table_Object = MibTable
ipeStsPortNe2Table = _IpeStsPortNe2Table_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 7, 2)
)
if mibBuilder.loadTexts:
    ipeStsPortNe2Table.setStatus("current")
_IpeStsPortNe2Entry_Object = MibTableRow
ipeStsPortNe2Entry = _IpeStsPortNe2Entry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 7, 2, 1)
)
ipeStsPortNe2Entry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeStsPortNe2IfIndex"),
)
if mibBuilder.loadTexts:
    ipeStsPortNe2Entry.setStatus("current")
_IpeStsPortNe2IfIndex_Type = InterfaceIndex
_IpeStsPortNe2IfIndex_Object = MibTableColumn
ipeStsPortNe2IfIndex = _IpeStsPortNe2IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 7, 2, 1, 1),
    _IpeStsPortNe2IfIndex_Type()
)
ipeStsPortNe2IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeStsPortNe2IfIndex.setStatus("current")
_IpeStsPortNe2NEAddress_Type = IpAddress
_IpeStsPortNe2NEAddress_Object = MibTableColumn
ipeStsPortNe2NEAddress = _IpeStsPortNe2NEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 7, 2, 1, 2),
    _IpeStsPortNe2NEAddress_Type()
)
ipeStsPortNe2NEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeStsPortNe2NEAddress.setStatus("current")
_IpeStsPortNe2LinkUp_Type = Integer32
_IpeStsPortNe2LinkUp_Object = MibTableColumn
ipeStsPortNe2LinkUp = _IpeStsPortNe2LinkUp_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 7, 2, 1, 3),
    _IpeStsPortNe2LinkUp_Type()
)
ipeStsPortNe2LinkUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeStsPortNe2LinkUp.setStatus("current")
_IpeStsBridge_ObjectIdentity = ObjectIdentity
ipeStsBridge = _IpeStsBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 8)
)
_IpeStsBridgeFdbTable_Object = MibTable
ipeStsBridgeFdbTable = _IpeStsBridgeFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 8, 1)
)
if mibBuilder.loadTexts:
    ipeStsBridgeFdbTable.setStatus("obsolete")
_IpeStsBridgeFdbEntry_Object = MibTableRow
ipeStsBridgeFdbEntry = _IpeStsBridgeFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 8, 1, 1)
)
ipeStsBridgeFdbEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeStsBridgeFdbBridgeIndex"),
    (0, "IPE-SYSTEM-MIB", "ipeStsBridgeFdbIfIndex"),
    (0, "IPE-SYSTEM-MIB", "ipeStsBridgeFdbIndex"),
)
if mibBuilder.loadTexts:
    ipeStsBridgeFdbEntry.setStatus("obsolete")


class _IpeStsBridgeFdbBridgeIndex_Type(Integer32):
    """Custom type ipeStsBridgeFdbBridgeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_IpeStsBridgeFdbBridgeIndex_Type.__name__ = "Integer32"
_IpeStsBridgeFdbBridgeIndex_Object = MibTableColumn
ipeStsBridgeFdbBridgeIndex = _IpeStsBridgeFdbBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 8, 1, 1, 1),
    _IpeStsBridgeFdbBridgeIndex_Type()
)
ipeStsBridgeFdbBridgeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeStsBridgeFdbBridgeIndex.setStatus("obsolete")
_IpeStsBridgeFdbIfIndex_Type = InterfaceIndex
_IpeStsBridgeFdbIfIndex_Object = MibTableColumn
ipeStsBridgeFdbIfIndex = _IpeStsBridgeFdbIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 8, 1, 1, 2),
    _IpeStsBridgeFdbIfIndex_Type()
)
ipeStsBridgeFdbIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeStsBridgeFdbIfIndex.setStatus("obsolete")


class _IpeStsBridgeFdbIndex_Type(Integer32):
    """Custom type ipeStsBridgeFdbIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_IpeStsBridgeFdbIndex_Type.__name__ = "Integer32"
_IpeStsBridgeFdbIndex_Object = MibTableColumn
ipeStsBridgeFdbIndex = _IpeStsBridgeFdbIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 8, 1, 1, 3),
    _IpeStsBridgeFdbIndex_Type()
)
ipeStsBridgeFdbIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeStsBridgeFdbIndex.setStatus("obsolete")
_IpeStsBridgeFdbNEAddress_Type = IpAddress
_IpeStsBridgeFdbNEAddress_Object = MibTableColumn
ipeStsBridgeFdbNEAddress = _IpeStsBridgeFdbNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 8, 1, 1, 4),
    _IpeStsBridgeFdbNEAddress_Type()
)
ipeStsBridgeFdbNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeStsBridgeFdbNEAddress.setStatus("obsolete")
_IpeStsBridgeFdbAddress_Type = MacAddress
_IpeStsBridgeFdbAddress_Object = MibTableColumn
ipeStsBridgeFdbAddress = _IpeStsBridgeFdbAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 8, 1, 1, 5),
    _IpeStsBridgeFdbAddress_Type()
)
ipeStsBridgeFdbAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeStsBridgeFdbAddress.setStatus("obsolete")
_IpeStsAutoIp_ObjectIdentity = ObjectIdentity
ipeStsAutoIp = _IpeStsAutoIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 9)
)
_IpeStsAutoIpTable_Object = MibTable
ipeStsAutoIpTable = _IpeStsAutoIpTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 9, 1)
)
if mibBuilder.loadTexts:
    ipeStsAutoIpTable.setStatus("current")
_IpeStsAutoIpEntry_Object = MibTableRow
ipeStsAutoIpEntry = _IpeStsAutoIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 9, 1, 1)
)
ipeStsAutoIpEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeStsAutoIpIndex"),
)
if mibBuilder.loadTexts:
    ipeStsAutoIpEntry.setStatus("current")


class _IpeStsAutoIpIndex_Type(Integer32):
    """Custom type ipeStsAutoIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_IpeStsAutoIpIndex_Type.__name__ = "Integer32"
_IpeStsAutoIpIndex_Object = MibTableColumn
ipeStsAutoIpIndex = _IpeStsAutoIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 9, 1, 1, 1),
    _IpeStsAutoIpIndex_Type()
)
ipeStsAutoIpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeStsAutoIpIndex.setStatus("current")
_IpeStsAutoIpNEAddress_Type = IpAddress
_IpeStsAutoIpNEAddress_Object = MibTableColumn
ipeStsAutoIpNEAddress = _IpeStsAutoIpNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 9, 1, 1, 2),
    _IpeStsAutoIpNEAddress_Type()
)
ipeStsAutoIpNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeStsAutoIpNEAddress.setStatus("current")
_IpeStsAutoIpState_Type = Integer32
_IpeStsAutoIpState_Object = MibTableColumn
ipeStsAutoIpState = _IpeStsAutoIpState_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 9, 1, 1, 3),
    _IpeStsAutoIpState_Type()
)
ipeStsAutoIpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeStsAutoIpState.setStatus("current")
_IpeStsAutoIpTempAddress_Type = IpAddress
_IpeStsAutoIpTempAddress_Object = MibTableColumn
ipeStsAutoIpTempAddress = _IpeStsAutoIpTempAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 9, 1, 1, 4),
    _IpeStsAutoIpTempAddress_Type()
)
ipeStsAutoIpTempAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeStsAutoIpTempAddress.setStatus("current")
_IpeAccessGroup_ObjectIdentity = ObjectIdentity
ipeAccessGroup = _IpeAccessGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 7)
)
_IpeAccessTable_Object = MibTable
ipeAccessTable = _IpeAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 7, 1)
)
if mibBuilder.loadTexts:
    ipeAccessTable.setStatus("current")
_IpeAccessEntry_Object = MibTableRow
ipeAccessEntry = _IpeAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 7, 1, 1)
)
ipeAccessEntry.setIndexNames(
    (0, "IPE-SYSTEM-MIB", "ipeAccessIndex"),
)
if mibBuilder.loadTexts:
    ipeAccessEntry.setStatus("current")


class _IpeAccessIndex_Type(Integer32):
    """Custom type ipeAccessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_IpeAccessIndex_Type.__name__ = "Integer32"
_IpeAccessIndex_Object = MibTableColumn
ipeAccessIndex = _IpeAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 7, 1, 1, 1),
    _IpeAccessIndex_Type()
)
ipeAccessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeAccessIndex.setStatus("current")
_IpeAccessNEAddress_Type = IpAddress
_IpeAccessNEAddress_Object = MibTableColumn
ipeAccessNEAddress = _IpeAccessNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 7, 1, 1, 2),
    _IpeAccessNEAddress_Type()
)
ipeAccessNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeAccessNEAddress.setStatus("current")


class _IpeAccessUserName_Type(DisplayString):
    """Custom type ipeAccessUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpeAccessUserName_Type.__name__ = "DisplayString"
_IpeAccessUserName_Object = MibTableColumn
ipeAccessUserName = _IpeAccessUserName_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 7, 1, 1, 3),
    _IpeAccessUserName_Type()
)
ipeAccessUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeAccessUserName.setStatus("current")
_IpeAccessFromAddress_Type = IpAddress
_IpeAccessFromAddress_Object = MibTableColumn
ipeAccessFromAddress = _IpeAccessFromAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 7, 1, 1, 4),
    _IpeAccessFromAddress_Type()
)
ipeAccessFromAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeAccessFromAddress.setStatus("current")


class _IpeAccessType_Type(Integer32):
    """Custom type ipeAccessType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("nms", 1),
          ("webLct", 2),
          ("cli", 3),
          ("internal", 4))
    )


_IpeAccessType_Type.__name__ = "Integer32"
_IpeAccessType_Object = MibTableColumn
ipeAccessType = _IpeAccessType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 7, 1, 1, 5),
    _IpeAccessType_Type()
)
ipeAccessType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeAccessType.setStatus("current")
_IpeAccessSessionId_Type = Integer32
_IpeAccessSessionId_Object = MibTableColumn
ipeAccessSessionId = _IpeAccessSessionId_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 7, 1, 1, 6),
    _IpeAccessSessionId_Type()
)
ipeAccessSessionId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeAccessSessionId.setStatus("current")
_IpeAccessErrorCode_Type = Integer32
_IpeAccessErrorCode_Object = MibTableColumn
ipeAccessErrorCode = _IpeAccessErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 7, 1, 1, 7),
    _IpeAccessErrorCode_Type()
)
ipeAccessErrorCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeAccessErrorCode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPE-SYSTEM-MIB",
    **{"AlarmTypeValue": AlarmTypeValue,
       "ProbableCauseValue": ProbableCauseValue,
       "nec": nec,
       "nec-mib": nec_mib,
       "necProductDepend": necProductDepend,
       "radioEquipment": radioEquipment,
       "system1": system1,
       "pmSystem": pmSystem,
       "sysPmType": sysPmType,
       "sysPrimaryIpAddress": sysPrimaryIpAddress,
       "sysOppositeIpAddress": sysOppositeIpAddress,
       "sysEquipmentType": sysEquipmentType,
       "sysEquipmentConfig": sysEquipmentConfig,
       "system5": system5,
       "ipeSystemGroup": ipeSystemGroup,
       "ipeSysInfoTable": ipeSysInfoTable,
       "ipeSysInfoEntry": ipeSysInfoEntry,
       "ipeSysInfoIndex": ipeSysInfoIndex,
       "ipeSysInfoNEAddress": ipeSysInfoNEAddress,
       "ipeSysNeName": ipeSysNeName,
       "ipeSysAreaName": ipeSysAreaName,
       "ipeSysNote": ipeSysNote,
       "ipeSysPrimaryIpAddress": ipeSysPrimaryIpAddress,
       "ipeSysSubnetMask": ipeSysSubnetMask,
       "ipeSysDefaultGateway": ipeSysDefaultGateway,
       "ipeSysMacAddress": ipeSysMacAddress,
       "ipeSysMibVersion": ipeSysMibVersion,
       "ipeSysEquipmentType": ipeSysEquipmentType,
       "ipeSysPmType": ipeSysPmType,
       "ipeSysInventoryInfoTable": ipeSysInventoryInfoTable,
       "ipeSysInventoryInfoEntry": ipeSysInventoryInfoEntry,
       "ipeSysInventoryInfoIndex": ipeSysInventoryInfoIndex,
       "ipeSysInventoryInfoNEAddress": ipeSysInventoryInfoNEAddress,
       "ipeSysInvSoftwareVersion": ipeSysInvSoftwareVersion,
       "ipeSysInvSoftwareReleaseDate": ipeSysInvSoftwareReleaseDate,
       "ipeSysInvDlSoftwareVersion": ipeSysInvDlSoftwareVersion,
       "ipeSysInvOperationSide": ipeSysInvOperationSide,
       "ipeSysInvStandbySoftwareVersion": ipeSysInvStandbySoftwareVersion,
       "ipeSysOperationGroup": ipeSysOperationGroup,
       "ipeSysOpTimeTable": ipeSysOpTimeTable,
       "ipeSysOpTimeEntry": ipeSysOpTimeEntry,
       "ipeSysOpTimeIndex": ipeSysOpTimeIndex,
       "ipeSysOpTimeNEAddress": ipeSysOpTimeNEAddress,
       "ipeSysOpCurrentTime": ipeSysOpCurrentTime,
       "ipeSysOpStartTime": ipeSysOpStartTime,
       "ipeSysOpUpTime": ipeSysOpUpTime,
       "ipeSysOpFileDownloadTable": ipeSysOpFileDownloadTable,
       "ipeSysOpFileDownloadEntry": ipeSysOpFileDownloadEntry,
       "ipeSysOpFileDownloadIndex": ipeSysOpFileDownloadIndex,
       "ipeSysOpFileDownloadNEAddress": ipeSysOpFileDownloadNEAddress,
       "ipeSysOpFileDownloadModule": ipeSysOpFileDownloadModule,
       "ipeSysOpFileDownloadCpuResetDetail": ipeSysOpFileDownloadCpuResetDetail,
       "ipeSysOpFileDownloadStatus": ipeSysOpFileDownloadStatus,
       "ipeSysOpFileDownloadCtrl": ipeSysOpFileDownloadCtrl,
       "ipeSysOpFileDownloadProtocolType": ipeSysOpFileDownloadProtocolType,
       "ipeSysOpProgramPmonRmonClearTable": ipeSysOpProgramPmonRmonClearTable,
       "ipeSysOpProgramPmonRmonClearEntry": ipeSysOpProgramPmonRmonClearEntry,
       "ipeSysOpProgramPmonRmonClearIndex": ipeSysOpProgramPmonRmonClearIndex,
       "ipeSysOpProgramPmonRmonClearNEAddress": ipeSysOpProgramPmonRmonClearNEAddress,
       "ipeSysOpProgramPmonRmonClear": ipeSysOpProgramPmonRmonClear,
       "ipeSysOpProgramPmonRmonClearResult": ipeSysOpProgramPmonRmonClearResult,
       "ipeFileSystemGroup": ipeFileSystemGroup,
       "ipeFsFileInfoTable": ipeFsFileInfoTable,
       "ipeFsFileInfoEntry": ipeFsFileInfoEntry,
       "ipeFsFileInfoIndex": ipeFsFileInfoIndex,
       "ipeFsFileInfoNEAddress": ipeFsFileInfoNEAddress,
       "ipeFsFileListType": ipeFsFileListType,
       "ipeFsFileListCurrent": ipeFsFileListCurrent,
       "ipeFsFileListTemp": ipeFsFileListTemp,
       "ipeFsUpdateFileDetail": ipeFsUpdateFileDetail,
       "ipeFsUpdateFileStatus": ipeFsUpdateFileStatus,
       "ipeFsUpdateFileStatusDetail": ipeFsUpdateFileStatusDetail,
       "ipeFsUpdateFileProgressBase": ipeFsUpdateFileProgressBase,
       "ipeFsUpdateFileProgress": ipeFsUpdateFileProgress,
       "ipeFsUpdateFileUpdateList": ipeFsUpdateFileUpdateList,
       "ipeFsUpdateFileConfigPartial": ipeFsUpdateFileConfigPartial,
       "ipeFsUsbInfoTable": ipeFsUsbInfoTable,
       "ipeFsUsbInfoEntry": ipeFsUsbInfoEntry,
       "ipeFsUsbInfoIndex": ipeFsUsbInfoIndex,
       "ipeFsUsbInfoNEAddress": ipeFsUsbInfoNEAddress,
       "ipeFsUsbCommand": ipeFsUsbCommand,
       "ipeFsUsbProcStatus": ipeFsUsbProcStatus,
       "ipeFsUsbList": ipeFsUsbList,
       "ipeFsUsbConnectStatus": ipeFsUsbConnectStatus,
       "ipeConfigurationGroup": ipeConfigurationGroup,
       "ipeCfgSystemTable": ipeCfgSystemTable,
       "ipeCfgSystemEntry": ipeCfgSystemEntry,
       "ipeCfgSystemIndex": ipeCfgSystemIndex,
       "ipeCfgSystemNEAddress": ipeCfgSystemNEAddress,
       "ipeCfgNeName": ipeCfgNeName,
       "ipeCfgAreaName": ipeCfgAreaName,
       "ipeCfgMemo": ipeCfgMemo,
       "ipeCfgOemTable": ipeCfgOemTable,
       "ipeCfgOemEntry": ipeCfgOemEntry,
       "ipeCfgOemIndex": ipeCfgOemIndex,
       "ipeCfgOemNEAddress": ipeCfgOemNEAddress,
       "ipeCfgOemSysDescr": ipeCfgOemSysDescr,
       "ipeCfgOemSysContact": ipeCfgOemSysContact,
       "ipeCfgOemSysName": ipeCfgOemSysName,
       "ipeCfgOemSysLocation": ipeCfgOemSysLocation,
       "ipeCfgAux": ipeCfgAux,
       "ipeCfgAuxInTable": ipeCfgAuxInTable,
       "ipeCfgAuxInEntry": ipeCfgAuxInEntry,
       "ipeCfgAuxInIndex": ipeCfgAuxInIndex,
       "ipeCfgAuxInNEAddress": ipeCfgAuxInNEAddress,
       "ipeCfgAuxInItemName": ipeCfgAuxInItemName,
       "ipeCfgAuxInItemType": ipeCfgAuxInItemType,
       "ipeCfgAuxInOpenState": ipeCfgAuxInOpenState,
       "ipeCfgAuxInCloseState": ipeCfgAuxInCloseState,
       "ipeCfgAuxInSeverity": ipeCfgAuxInSeverity,
       "ipeCfgAuxInAlarmType": ipeCfgAuxInAlarmType,
       "ipeCfgAuxInProbableCause": ipeCfgAuxInProbableCause,
       "ipeCfgAuxOutTable": ipeCfgAuxOutTable,
       "ipeCfgAuxOutEntry": ipeCfgAuxOutEntry,
       "ipeCfgAuxOutIndex": ipeCfgAuxOutIndex,
       "ipeCfgAuxOutNEAddress": ipeCfgAuxOutNEAddress,
       "ipeCfgAuxOutItemName": ipeCfgAuxOutItemName,
       "ipeCfgAuxOutOpenState": ipeCfgAuxOutOpenState,
       "ipeCfgAuxOutCloseState": ipeCfgAuxOutCloseState,
       "ipeCfgNtp": ipeCfgNtp,
       "ipeCfgNtpServiceTable": ipeCfgNtpServiceTable,
       "ipeCfgNtpServiceEntry": ipeCfgNtpServiceEntry,
       "ipeCfgNtpServiceIndex": ipeCfgNtpServiceIndex,
       "ipeCfgNtpServiceNEAddress": ipeCfgNtpServiceNEAddress,
       "ipeCfgNtpServiceEnable": ipeCfgNtpServiceEnable,
       "ipeCfgNtpServerMode": ipeCfgNtpServerMode,
       "ipeCfgNtpClientMode": ipeCfgNtpClientMode,
       "ipeCfgNtpServerStratum": ipeCfgNtpServerStratum,
       "ipeCfgNtpServerMulticastPort": ipeCfgNtpServerMulticastPort,
       "ipeCfgNtpServerMulticastIntervalTime": ipeCfgNtpServerMulticastIntervalTime,
       "ipeCfgNtpServerTable": ipeCfgNtpServerTable,
       "ipeCfgNtpServerEntry": ipeCfgNtpServerEntry,
       "ipeCfgNtpServerIndex": ipeCfgNtpServerIndex,
       "ipeCfgNtpServerNEAddress": ipeCfgNtpServerNEAddress,
       "ipeCfgNtpServerAddress": ipeCfgNtpServerAddress,
       "ipeCfgNtpVersion": ipeCfgNtpVersion,
       "ipeCfgNtpPollTime": ipeCfgNtpPollTime,
       "ipeCfgFtp": ipeCfgFtp,
       "ipeCfgFtpServerTable": ipeCfgFtpServerTable,
       "ipeCfgFtpServerEntry": ipeCfgFtpServerEntry,
       "ipeCfgFtpServerIndex": ipeCfgFtpServerIndex,
       "ipeCfgFtpServerNEAddress": ipeCfgFtpServerNEAddress,
       "ipeCfgFtpServerEnable": ipeCfgFtpServerEnable,
       "ipeCfgFtpServerCommandTcpPort": ipeCfgFtpServerCommandTcpPort,
       "ipeCfgFtpServerDataTcpPort": ipeCfgFtpServerDataTcpPort,
       "ipeCfgFtpServerMaxSession": ipeCfgFtpServerMaxSession,
       "ipeCfgFtpServerAutoDisable": ipeCfgFtpServerAutoDisable,
       "ipeCfgSftp": ipeCfgSftp,
       "ipeCfgSftpServerTable": ipeCfgSftpServerTable,
       "ipeCfgSftpServerEntry": ipeCfgSftpServerEntry,
       "ipeCfgSftpServerIndex": ipeCfgSftpServerIndex,
       "ipeCfgSftpServerNEAddress": ipeCfgSftpServerNEAddress,
       "ipeCfgSftpServerEnable": ipeCfgSftpServerEnable,
       "ipeCfgSftpServerAutoDisable": ipeCfgSftpServerAutoDisable,
       "ipeCfgHttp": ipeCfgHttp,
       "ipeCfgHttpServerTable": ipeCfgHttpServerTable,
       "ipeCfgHttpServerEntry": ipeCfgHttpServerEntry,
       "ipeCfgHttpServerIndex": ipeCfgHttpServerIndex,
       "ipeCfgHttpServerNEAddress": ipeCfgHttpServerNEAddress,
       "ipeCfgHttpServerEnable": ipeCfgHttpServerEnable,
       "ipeCfgHttpServerTcpPort": ipeCfgHttpServerTcpPort,
       "ipeCfgHttps": ipeCfgHttps,
       "ipeCfgHttpsServerTable": ipeCfgHttpsServerTable,
       "ipeCfgHttpsServerEntry": ipeCfgHttpsServerEntry,
       "ipeCfgHttpsServerIndex": ipeCfgHttpsServerIndex,
       "ipeCfgHttpsServerNEAddress": ipeCfgHttpsServerNEAddress,
       "ipeCfgHttpsServerEnable": ipeCfgHttpsServerEnable,
       "ipeCfgHttpsServerTcpPort": ipeCfgHttpsServerTcpPort,
       "ipeCfgSnmp": ipeCfgSnmp,
       "ipeCfgSnmpServerTable": ipeCfgSnmpServerTable,
       "ipeCfgSnmpServerEntry": ipeCfgSnmpServerEntry,
       "ipeCfgSnmpServerIndex": ipeCfgSnmpServerIndex,
       "ipeCfgSnmpServerNEAddress": ipeCfgSnmpServerNEAddress,
       "ipeCfgSnmpV1V2cEnable": ipeCfgSnmpV1V2cEnable,
       "ipeCfgSnmpV3Enable": ipeCfgSnmpV3Enable,
       "ipeCfgSnmpServerPort": ipeCfgSnmpServerPort,
       "ipeCfgSnmpCommunityTable": ipeCfgSnmpCommunityTable,
       "ipeCfgSnmpCommunityEntry": ipeCfgSnmpCommunityEntry,
       "ipeCfgSnmpCommunityIndex": ipeCfgSnmpCommunityIndex,
       "ipeCfgSnmpCommunityNEAddress": ipeCfgSnmpCommunityNEAddress,
       "ipeCfgSnmpCommunityName": ipeCfgSnmpCommunityName,
       "ipeCfgSnmpCommunityAccessLevel": ipeCfgSnmpCommunityAccessLevel,
       "ipeCfgSnmpCommunityAccessAddress": ipeCfgSnmpCommunityAccessAddress,
       "ipeCfgSnmpCommunityAccessPrefixLength": ipeCfgSnmpCommunityAccessPrefixLength,
       "ipeCfgSnmpCommunityRowStatus": ipeCfgSnmpCommunityRowStatus,
       "ipeCfgSnmpTrapTable": ipeCfgSnmpTrapTable,
       "ipeCfgSnmpTrapEntry": ipeCfgSnmpTrapEntry,
       "ipeCfgSnmpTrapEntryIndex": ipeCfgSnmpTrapEntryIndex,
       "ipeCfgSnmpTrapEntryNEAddress": ipeCfgSnmpTrapEntryNEAddress,
       "ipeCfgSnmpTrapVersion": ipeCfgSnmpTrapVersion,
       "ipeCfgSnmpTrapNotifyType": ipeCfgSnmpTrapNotifyType,
       "ipeCfgSnmpTrapTargetAddress": ipeCfgSnmpTrapTargetAddress,
       "ipeCfgSnmpTrapTargetPort": ipeCfgSnmpTrapTargetPort,
       "ipeCfgSnmpTrapSecurityName": ipeCfgSnmpTrapSecurityName,
       "ipeCfgSnmpTrapSecurityLevel": ipeCfgSnmpTrapSecurityLevel,
       "ipeCfgSnmpTrapEngineId": ipeCfgSnmpTrapEngineId,
       "ipeCfgSnmpTrapAuthAlgorithm": ipeCfgSnmpTrapAuthAlgorithm,
       "ipeCfgSnmpTrapAuthKey": ipeCfgSnmpTrapAuthKey,
       "ipeCfgSnmpTrapPrivAlgorithm": ipeCfgSnmpTrapPrivAlgorithm,
       "ipeCfgSnmpTrapPrivKey": ipeCfgSnmpTrapPrivKey,
       "ipeCfgSnmpTrapRowStatus": ipeCfgSnmpTrapRowStatus,
       "ipeCfgAccount": ipeCfgAccount,
       "ipeCfgAccountUserInfoTable": ipeCfgAccountUserInfoTable,
       "ipeCfgAccountUserInfoEntry": ipeCfgAccountUserInfoEntry,
       "ipeCfgAccountUserIndex": ipeCfgAccountUserIndex,
       "ipeCfgAccountUserNEAddress": ipeCfgAccountUserNEAddress,
       "ipeCfgAccountUserName": ipeCfgAccountUserName,
       "ipeCfgAccountUserKey": ipeCfgAccountUserKey,
       "ipeCfgAccountUserGroup": ipeCfgAccountUserGroup,
       "ipeCfgAccountUserSnmpV3SecurityLevel": ipeCfgAccountUserSnmpV3SecurityLevel,
       "ipeCfgAccountUserSnmpV3AuthAlgorithm": ipeCfgAccountUserSnmpV3AuthAlgorithm,
       "ipeCfgAccountUserSnmpV3AuthKey": ipeCfgAccountUserSnmpV3AuthKey,
       "ipeCfgAccountUserSnmpV3PrivAlgorithm": ipeCfgAccountUserSnmpV3PrivAlgorithm,
       "ipeCfgAccountUserSnmpV3PrivKey": ipeCfgAccountUserSnmpV3PrivKey,
       "ipeCfgAccountUserRowStatus": ipeCfgAccountUserRowStatus,
       "ipeCfgAccountGroupInfoTable": ipeCfgAccountGroupInfoTable,
       "ipeCfgAccountGroupInfoEntry": ipeCfgAccountGroupInfoEntry,
       "ipeCfgAccountGroupIndex": ipeCfgAccountGroupIndex,
       "ipeCfgAccountGroupNEAddress": ipeCfgAccountGroupNEAddress,
       "ipeCfgAccountGroupName": ipeCfgAccountGroupName,
       "ipeCfgAccountGroupTelnet": ipeCfgAccountGroupTelnet,
       "ipeCfgAccountGroupSsh": ipeCfgAccountGroupSsh,
       "ipeCfgAccountGroupFtp": ipeCfgAccountGroupFtp,
       "ipeCfgAccountGroupSftp": ipeCfgAccountGroupSftp,
       "ipeCfgAccountGroupHttp": ipeCfgAccountGroupHttp,
       "ipeCfgAccountGroupHttps": ipeCfgAccountGroupHttps,
       "ipeCfgAccountGroupSnmp": ipeCfgAccountGroupSnmp,
       "ipeCfgAccountGroupAccessLevel": ipeCfgAccountGroupAccessLevel,
       "ipeCfgAccountGroupRowStatus": ipeCfgAccountGroupRowStatus,
       "ipeCfgUserAccountAuthTable": ipeCfgUserAccountAuthTable,
       "ipeCfgUserAccountAuthEntry": ipeCfgUserAccountAuthEntry,
       "ipeCfgUserAccountAuthIndex": ipeCfgUserAccountAuthIndex,
       "ipeCfgUserAccountAuthNEAddress": ipeCfgUserAccountAuthNEAddress,
       "ipeCfgUserAccountAuthMode": ipeCfgUserAccountAuthMode,
       "ipeCfgUserAccountAuthOrder": ipeCfgUserAccountAuthOrder,
       "ipeCfgUserAccountAuthTrapEnable": ipeCfgUserAccountAuthTrapEnable,
       "ipeCfgUserAccountAuthTrapLocal": ipeCfgUserAccountAuthTrapLocal,
       "ipeCfgUserAccountAuthTrapExternal": ipeCfgUserAccountAuthTrapExternal,
       "ipeCfgDhcpGroup": ipeCfgDhcpGroup,
       "ipeCfgDhcpServerTable": ipeCfgDhcpServerTable,
       "ipeCfgDhcpServerEntry": ipeCfgDhcpServerEntry,
       "ipeCfgDhcpServerIndex": ipeCfgDhcpServerIndex,
       "ipeCfgDhcpServerNEAddress": ipeCfgDhcpServerNEAddress,
       "ipeCfgDhcpServerEnable": ipeCfgDhcpServerEnable,
       "ipeCfgDhcpLeaseAddrRangeBegin": ipeCfgDhcpLeaseAddrRangeBegin,
       "ipeCfgDhcpLeaseAddrRangeEnd": ipeCfgDhcpLeaseAddrRangeEnd,
       "ipeCfgStpGroup": ipeCfgStpGroup,
       "ipeCfgStpBridgeTable": ipeCfgStpBridgeTable,
       "ipeCfgStpBridgeEntry": ipeCfgStpBridgeEntry,
       "ipeCfgStpBridgeIndex": ipeCfgStpBridgeIndex,
       "ipeCfgStpBridgeNEAddress": ipeCfgStpBridgeNEAddress,
       "ipeCfgStpEnable": ipeCfgStpEnable,
       "ipeCfgStpPriority": ipeCfgStpPriority,
       "ipeCfgStpBridgeMaxAge": ipeCfgStpBridgeMaxAge,
       "ipeCfgStpBridgeHelloTime": ipeCfgStpBridgeHelloTime,
       "ipeCfgStpBridgeForwardDelay": ipeCfgStpBridgeForwardDelay,
       "ipeCfgStpPortTable": ipeCfgStpPortTable,
       "ipeCfgStpPortEntry": ipeCfgStpPortEntry,
       "ipeCfgStpPortIfIndex": ipeCfgStpPortIfIndex,
       "ipeCfgStpPortNEAddress": ipeCfgStpPortNEAddress,
       "ipeCfgStpPortPriority": ipeCfgStpPortPriority,
       "ipeCfgStpPortPathCost": ipeCfgStpPortPathCost,
       "ipeCfgStpPortEdgeEnable": ipeCfgStpPortEdgeEnable,
       "ipeCfgPortGroup": ipeCfgPortGroup,
       "ipeCfgPortModemTable": ipeCfgPortModemTable,
       "ipeCfgPortModemEntry": ipeCfgPortModemEntry,
       "ipeCfgPortModemIfIndex": ipeCfgPortModemIfIndex,
       "ipeCfgPortModemNEAddress": ipeCfgPortModemNEAddress,
       "ipeCfgPortModemEnable": ipeCfgPortModemEnable,
       "ipeCfgPortLctTable": ipeCfgPortLctTable,
       "ipeCfgPortLctEntry": ipeCfgPortLctEntry,
       "ipeCfgPortLctIfIndex": ipeCfgPortLctIfIndex,
       "ipeCfgPortLctNEAddress": ipeCfgPortLctNEAddress,
       "ipeCfgPortLctIpAddress": ipeCfgPortLctIpAddress,
       "ipeCfgPortLctNetMask": ipeCfgPortLctNetMask,
       "ipeCfgPortLctEnable": ipeCfgPortLctEnable,
       "ipeCfgPortLctMtu": ipeCfgPortLctMtu,
       "ipeCfgPortLctAutoNeg": ipeCfgPortLctAutoNeg,
       "ipeCfgPortEtherTable": ipeCfgPortEtherTable,
       "ipeCfgPortEtherEntry": ipeCfgPortEtherEntry,
       "ipeCfgPortEtherIfIndex": ipeCfgPortEtherIfIndex,
       "ipeCfgPortEtherNEAddress": ipeCfgPortEtherNEAddress,
       "ipeCfgPortEtherEnable": ipeCfgPortEtherEnable,
       "ipeCfgPortEtherAutoNeg": ipeCfgPortEtherAutoNeg,
       "ipeCfgPortEtherSpecialFilter": ipeCfgPortEtherSpecialFilter,
       "ipeCfgPortEtherLldpMode": ipeCfgPortEtherLldpMode,
       "ipeCfgPortNe2Table": ipeCfgPortNe2Table,
       "ipeCfgPortNe2Entry": ipeCfgPortNe2Entry,
       "ipeCfgPortNe2IfIndex": ipeCfgPortNe2IfIndex,
       "ipeCfgPortNe2NEAddress": ipeCfgPortNe2NEAddress,
       "ipeCfgPortNe2IpAddress": ipeCfgPortNe2IpAddress,
       "ipeCfgPortNe2Enable": ipeCfgPortNe2Enable,
       "ipeCfgPortNe2Speed": ipeCfgPortNe2Speed,
       "ipeCfgPortNe2NeighborMibEnable": ipeCfgPortNe2NeighborMibEnable,
       "ipeCfgPortE1Table": ipeCfgPortE1Table,
       "ipeCfgPortE1Entry": ipeCfgPortE1Entry,
       "ipeCfgPortE1IfIndex": ipeCfgPortE1IfIndex,
       "ipeCfgPortE1NEAddress": ipeCfgPortE1NEAddress,
       "ipeCfgPortE1Enable": ipeCfgPortE1Enable,
       "ipeCfgPortE1ChannelNumber": ipeCfgPortE1ChannelNumber,
       "ipeCfgPortInbandTable": ipeCfgPortInbandTable,
       "ipeCfgPortInbandEntry": ipeCfgPortInbandEntry,
       "ipeCfgPortInbandIfIndex": ipeCfgPortInbandIfIndex,
       "ipeCfgPortInbandNEAddress": ipeCfgPortInbandNEAddress,
       "ipeCfgPortInbandIpAddress": ipeCfgPortInbandIpAddress,
       "ipeCfgPortInbandNetMask": ipeCfgPortInbandNetMask,
       "ipeCfgPortInbandEnable": ipeCfgPortInbandEnable,
       "ipeCfgPortInbandVlanId": ipeCfgPortInbandVlanId,
       "ipeCfgPortInbandMtu": ipeCfgPortInbandMtu,
       "ipeCfgPortInbandCos": ipeCfgPortInbandCos,
       "ipeCfgPortMainEtherTable": ipeCfgPortMainEtherTable,
       "ipeCfgPortMainEtherEntry": ipeCfgPortMainEtherEntry,
       "ipeCfgPortMainEtherIfIndex": ipeCfgPortMainEtherIfIndex,
       "ipeCfgPortMainEtherNEAddress": ipeCfgPortMainEtherNEAddress,
       "ipeCfgPortMainEtherLldpMode": ipeCfgPortMainEtherLldpMode,
       "ipeCfgBridgeGroup": ipeCfgBridgeGroup,
       "ipeCfgBridgeTable": ipeCfgBridgeTable,
       "ipeCfgBridgeEntry": ipeCfgBridgeEntry,
       "ipeCfgBridgeIndex": ipeCfgBridgeIndex,
       "ipeCfgBridgeNEAddress": ipeCfgBridgeNEAddress,
       "ipeCfgBridgeIpAddress": ipeCfgBridgeIpAddress,
       "ipeCfgBridgeNetMask": ipeCfgBridgeNetMask,
       "ipeCfgBridgeMtu": ipeCfgBridgeMtu,
       "ipeCfgBridgePortTable": ipeCfgBridgePortTable,
       "ipeCfgBridgePortEntry": ipeCfgBridgePortEntry,
       "ipeCfgBridgePortIfIndex": ipeCfgBridgePortIfIndex,
       "ipeCfgBridgePortNEAddress": ipeCfgBridgePortNEAddress,
       "ipeCfgBridgePortBridgeIndex": ipeCfgBridgePortBridgeIndex,
       "ipeCfgPripGroup": ipeCfgPripGroup,
       "ipeCfgPripTable": ipeCfgPripTable,
       "ipeCfgPripEntry": ipeCfgPripEntry,
       "ipeCfgPripIndex": ipeCfgPripIndex,
       "ipeCfgPripNEAddress": ipeCfgPripNEAddress,
       "ipeCfgPripRouteEnable": ipeCfgPripRouteEnable,
       "ipeCfgPripUdpPort": ipeCfgPripUdpPort,
       "ipeCfgPripPortTable": ipeCfgPripPortTable,
       "ipeCfgPripPortEntry": ipeCfgPripPortEntry,
       "ipeCfgPripPortIfIndex": ipeCfgPripPortIfIndex,
       "ipeCfgPripPortNEAddress": ipeCfgPripPortNEAddress,
       "ipeCfgPripPortEnable": ipeCfgPripPortEnable,
       "ipeCfgPripPortPropagateNetEnable": ipeCfgPripPortPropagateNetEnable,
       "ipeCfgNaptGroup": ipeCfgNaptGroup,
       "ipeCfgNaptTable": ipeCfgNaptTable,
       "ipeCfgNaptEntry": ipeCfgNaptEntry,
       "ipeCfgNaptIndex": ipeCfgNaptIndex,
       "ipeCfgNaptNEAddress": ipeCfgNaptNEAddress,
       "ipeCfgNaptEnable": ipeCfgNaptEnable,
       "ipeCfgStaticRouteGroup": ipeCfgStaticRouteGroup,
       "ipeCfgStaticRouteTable": ipeCfgStaticRouteTable,
       "ipeCfgStaticRouteEntry": ipeCfgStaticRouteEntry,
       "ipeCfgRouteIndex": ipeCfgRouteIndex,
       "ipeCfgRouteNEAddress": ipeCfgRouteNEAddress,
       "ipeCfgRouteDest": ipeCfgRouteDest,
       "ipeCfgRouteMask": ipeCfgRouteMask,
       "ipeCfgRouteNextHop": ipeCfgRouteNextHop,
       "ipeCfgRouteRowStatus": ipeCfgRouteRowStatus,
       "ipeCfgAccessListGroup": ipeCfgAccessListGroup,
       "ipeCfgAccessListRuleTable": ipeCfgAccessListRuleTable,
       "ipeCfgAccessListRuleEntry": ipeCfgAccessListRuleEntry,
       "ipeCfgAccessListRuleEnableIndex": ipeCfgAccessListRuleEnableIndex,
       "ipeCfgAccessListRuleNEAddress": ipeCfgAccessListRuleNEAddress,
       "ipeCfgAccessListInputRuleEnable": ipeCfgAccessListInputRuleEnable,
       "ipeCfgAccessListForwardRuleEnable": ipeCfgAccessListForwardRuleEnable,
       "ipeCfgAccessListInputDefaultAction": ipeCfgAccessListInputDefaultAction,
       "ipeCfgAccessListForwardDefaultAction": ipeCfgAccessListForwardDefaultAction,
       "ipeCfgAccessListInputTable": ipeCfgAccessListInputTable,
       "ipeCfgAccessListInputEntry": ipeCfgAccessListInputEntry,
       "ipeCfgAccessListInputOrderNum": ipeCfgAccessListInputOrderNum,
       "ipeCfgAccessListInputNEAddress": ipeCfgAccessListInputNEAddress,
       "ipeCfgAccessListInputInIfIndex": ipeCfgAccessListInputInIfIndex,
       "ipeCfgAccessListInputSrcIpAddress": ipeCfgAccessListInputSrcIpAddress,
       "ipeCfgAccessListInputSrcNetMask": ipeCfgAccessListInputSrcNetMask,
       "ipeCfgAccessListInputProtocol": ipeCfgAccessListInputProtocol,
       "ipeCfgAccessListInputDstPortNum": ipeCfgAccessListInputDstPortNum,
       "ipeCfgAccessListInputAction": ipeCfgAccessListInputAction,
       "ipeCfgAccessListInputRowStatus": ipeCfgAccessListInputRowStatus,
       "ipeCfgAccessListForwardTable": ipeCfgAccessListForwardTable,
       "ipeCfgAccessListForwardEntry": ipeCfgAccessListForwardEntry,
       "ipeCfgAccessListForwardOrderNum": ipeCfgAccessListForwardOrderNum,
       "ipeCfgAccessListForwardNEAddress": ipeCfgAccessListForwardNEAddress,
       "ipeCfgAccessListForwardInIfIndex": ipeCfgAccessListForwardInIfIndex,
       "ipeCfgAccessListForwardOutIfIndex": ipeCfgAccessListForwardOutIfIndex,
       "ipeCfgAccessListForwardSrcIpAddress": ipeCfgAccessListForwardSrcIpAddress,
       "ipeCfgAccessListForwardSrcNetMask": ipeCfgAccessListForwardSrcNetMask,
       "ipeCfgAccessListForwardDstIpAddress": ipeCfgAccessListForwardDstIpAddress,
       "ipeCfgAccessListForwardDstNetMask": ipeCfgAccessListForwardDstNetMask,
       "ipeCfgAccessListForwardProtocol": ipeCfgAccessListForwardProtocol,
       "ipeCfgAccessListForwardSrcPortNum": ipeCfgAccessListForwardSrcPortNum,
       "ipeCfgAccessListForwardDstPortNum": ipeCfgAccessListForwardDstPortNum,
       "ipeCfgAccessListForwardAction": ipeCfgAccessListForwardAction,
       "ipeCfgAccessListForwardRowStatus": ipeCfgAccessListForwardRowStatus,
       "ipeCfgAutoIpGroup": ipeCfgAutoIpGroup,
       "ipeCfgAutoIpTable": ipeCfgAutoIpTable,
       "ipeCfgAutoIpEntry": ipeCfgAutoIpEntry,
       "ipeCfgAutoIpIndex": ipeCfgAutoIpIndex,
       "ipeCfgAutoIpNEAddress": ipeCfgAutoIpNEAddress,
       "ipeCfgAutoIpNetworkAddress": ipeCfgAutoIpNetworkAddress,
       "ipeCfgAutoIpNetMask": ipeCfgAutoIpNetMask,
       "ipeCfgSysNE1PortTable": ipeCfgSysNE1PortTable,
       "ipeCfgSysNE1PortEntry": ipeCfgSysNE1PortEntry,
       "ipeCfgSysNE1PortIndex": ipeCfgSysNE1PortIndex,
       "ipeCfgSysNE1PortNEAddress": ipeCfgSysNE1PortNEAddress,
       "ipeCfgSysNE1PortMode": ipeCfgSysNE1PortMode,
       "ipeCfgRadiusGroup": ipeCfgRadiusGroup,
       "ipeCfgRadiusGeneralTable": ipeCfgRadiusGeneralTable,
       "ipeCfgRadiusGeneralEntry": ipeCfgRadiusGeneralEntry,
       "ipeCfgRadiusGeneralIndex": ipeCfgRadiusGeneralIndex,
       "ipeCfgRadiusGeneralNEAddress": ipeCfgRadiusGeneralNEAddress,
       "ipeCfgRadiusGeneralAuthClientRetransmit": ipeCfgRadiusGeneralAuthClientRetransmit,
       "ipeCfgRadiusGeneralAuthClientTimeout": ipeCfgRadiusGeneralAuthClientTimeout,
       "ipeCfgRadiusAuthServerExtTable": ipeCfgRadiusAuthServerExtTable,
       "ipeCfgRadiusAuthServerExtEntry": ipeCfgRadiusAuthServerExtEntry,
       "ipeCfgRadiusAuthServerExtIndex": ipeCfgRadiusAuthServerExtIndex,
       "ipeCfgRadiusAuthServerNEAddress": ipeCfgRadiusAuthServerNEAddress,
       "ipeCfgRadiusAuthServerAddressType": ipeCfgRadiusAuthServerAddressType,
       "ipeCfgRadiusAuthServerAddress": ipeCfgRadiusAuthServerAddress,
       "ipeCfgRadiusAuthClientServerPortNumber": ipeCfgRadiusAuthClientServerPortNumber,
       "ipeCfgRadiusAuthClientPasswordType": ipeCfgRadiusAuthClientPasswordType,
       "ipeCfgRadiusAuthClientSecretKey": ipeCfgRadiusAuthClientSecretKey,
       "ipeCfgRadiusAuthServerExtRowStatus": ipeCfgRadiusAuthServerExtRowStatus,
       "ipeCfgRadiusPrivLevelGeneralTable": ipeCfgRadiusPrivLevelGeneralTable,
       "ipeCfgRadiusPrivLevelGeneralEntry": ipeCfgRadiusPrivLevelGeneralEntry,
       "ipeCfgRadiusPrivLevelGeneralIndex": ipeCfgRadiusPrivLevelGeneralIndex,
       "ipeCfgRadiusPrivLevelGeneralNEAddress": ipeCfgRadiusPrivLevelGeneralNEAddress,
       "ipeCfgRadiusPrivLevelGeneralDefaultAction": ipeCfgRadiusPrivLevelGeneralDefaultAction,
       "ipeCfgRadiusPrivLevelGeneralDefaultGroup": ipeCfgRadiusPrivLevelGeneralDefaultGroup,
       "ipeCfgRadiusGroupPrivLevelMappingTable": ipeCfgRadiusGroupPrivLevelMappingTable,
       "ipeCfgRadiusGroupPrivLevelMappingEntry": ipeCfgRadiusGroupPrivLevelMappingEntry,
       "ipeCfgRadiusGroupPrivLevelMappingPrivLevel": ipeCfgRadiusGroupPrivLevelMappingPrivLevel,
       "ipeCfgRadiusGroupPrivLevelMappingNEAddress": ipeCfgRadiusGroupPrivLevelMappingNEAddress,
       "ipeCfgRadiusGroupPrivLevelMappingEnable": ipeCfgRadiusGroupPrivLevelMappingEnable,
       "ipeCfgRadiusGroupPrivLevelMappingGroup": ipeCfgRadiusGroupPrivLevelMappingGroup,
       "ipeCfgLldpGroup": ipeCfgLldpGroup,
       "ipeCfgLldpTable": ipeCfgLldpTable,
       "ipeCfgLldpEntry": ipeCfgLldpEntry,
       "ipeCfgLldpIndex": ipeCfgLldpIndex,
       "ipeCfgLldpNEAddress": ipeCfgLldpNEAddress,
       "ipeCfgLldpProprietaryModeMacAddress": ipeCfgLldpProprietaryModeMacAddress,
       "ipeCommunicationsGroup": ipeCommunicationsGroup,
       "ipeNeighborInfoTable": ipeNeighborInfoTable,
       "ipeNeighborInfoEntry": ipeNeighborInfoEntry,
       "ipeNeighborInfoIndex": ipeNeighborInfoIndex,
       "ipeNeighborInfoNEAddress": ipeNeighborInfoNEAddress,
       "ipeNeighborIpAddress": ipeNeighborIpAddress,
       "ipeStatusGroup": ipeStatusGroup,
       "ipeStsNtp": ipeStsNtp,
       "ipeStsNtpStatisticsTable": ipeStsNtpStatisticsTable,
       "ipeStsNtpStatisticsEntry": ipeStsNtpStatisticsEntry,
       "ipeStsNtpStatisticsIndex": ipeStsNtpStatisticsIndex,
       "ipeStsNtpStatisticsNEAddress": ipeStsNtpStatisticsNEAddress,
       "ipeStsNtpSyncStatusInfo": ipeStsNtpSyncStatusInfo,
       "ipeStsNtpSetTime": ipeStsNtpSetTime,
       "ipeStsFtp": ipeStsFtp,
       "ipeStsFtpStatusTable": ipeStsFtpStatusTable,
       "ipeStsFtpStatusEntry": ipeStsFtpStatusEntry,
       "ipeStsFtpStatusIndex": ipeStsFtpStatusIndex,
       "ipeStsFtpStatusNEAddress": ipeStsFtpStatusNEAddress,
       "ipeStsFtpStatusLoginUser": ipeStsFtpStatusLoginUser,
       "ipeStsFtpStatusLoginIpAddress": ipeStsFtpStatusLoginIpAddress,
       "ipeStsFtpStatusSessionId": ipeStsFtpStatusSessionId,
       "ipeStsSftp": ipeStsSftp,
       "ipeStsSftpStatusTable": ipeStsSftpStatusTable,
       "ipeStsSftpStatusEntry": ipeStsSftpStatusEntry,
       "ipeStsSftpStatusIndex": ipeStsSftpStatusIndex,
       "ipeStsSftpStatusNEAddress": ipeStsSftpStatusNEAddress,
       "ipeStsSftpStatusLoginUser": ipeStsSftpStatusLoginUser,
       "ipeStsSftpStatusLoginIpAddress": ipeStsSftpStatusLoginIpAddress,
       "ipeStsSftpStatusSessionId": ipeStsSftpStatusSessionId,
       "ipeStsHttp": ipeStsHttp,
       "ipeStsHttpStatusTable": ipeStsHttpStatusTable,
       "ipeStsHttpStatusEntry": ipeStsHttpStatusEntry,
       "ipeStsHttpStatusIndex": ipeStsHttpStatusIndex,
       "ipeStsHttpStatusNEAddress": ipeStsHttpStatusNEAddress,
       "ipeStsHttpStatusLoginUser": ipeStsHttpStatusLoginUser,
       "ipeStsHttpStatusLoginIpAddress": ipeStsHttpStatusLoginIpAddress,
       "ipeStsHttpStatusSessionId": ipeStsHttpStatusSessionId,
       "ipeStsHttps": ipeStsHttps,
       "ipeStsHttpsStatusTable": ipeStsHttpsStatusTable,
       "ipeStsHttpsStatusEntry": ipeStsHttpsStatusEntry,
       "ipeStsHttpsStatusIndex": ipeStsHttpsStatusIndex,
       "ipeStsHttpsStatusNEAddress": ipeStsHttpsStatusNEAddress,
       "ipeStsHttpsStatusLoginUser": ipeStsHttpsStatusLoginUser,
       "ipeStsHttpsStatusLoginIpAddress": ipeStsHttpsStatusLoginIpAddress,
       "ipeStsHttpsStatusSessionId": ipeStsHttpsStatusSessionId,
       "ipeStsStp": ipeStsStp,
       "ipeStsStpBridgeTable": ipeStsStpBridgeTable,
       "ipeStsStpBridgeEntry": ipeStsStpBridgeEntry,
       "ipeStsStpBridgeIndex": ipeStsStpBridgeIndex,
       "ipeStsStpBridgeNEAddress": ipeStsStpBridgeNEAddress,
       "ipeStsStpBridgeProtocolSpecification": ipeStsStpBridgeProtocolSpecification,
       "ipeStsStpBridgeDesignatedRoot": ipeStsStpBridgeDesignatedRoot,
       "ipeStsStpBridgeRootCost": ipeStsStpBridgeRootCost,
       "ipeStsStpBridgeRootPort": ipeStsStpBridgeRootPort,
       "ipeStsStpBridgeMaxAge": ipeStsStpBridgeMaxAge,
       "ipeStsStpBridgeHelloTime": ipeStsStpBridgeHelloTime,
       "ipeStsStpBridgeForwardDelay": ipeStsStpBridgeForwardDelay,
       "ipeStsStpPortTable": ipeStsStpPortTable,
       "ipeStsStpPortEntry": ipeStsStpPortEntry,
       "ipeStsStpPortIfIndex": ipeStsStpPortIfIndex,
       "ipeStsStpPortBridgeIndex": ipeStsStpPortBridgeIndex,
       "ipeStsStpPortNEAddress": ipeStsStpPortNEAddress,
       "ipeStsStpPortPortState": ipeStsStpPortPortState,
       "ipeStsStpPortDesignatedRoot": ipeStsStpPortDesignatedRoot,
       "ipeStsStpPortDesignatedCost": ipeStsStpPortDesignatedCost,
       "ipeStsStpPortDesignatedBridge": ipeStsStpPortDesignatedBridge,
       "ipeStsStpPortDesignatedPort": ipeStsStpPortDesignatedPort,
       "ipeStsPort": ipeStsPort,
       "ipeStsPortEtherTable": ipeStsPortEtherTable,
       "ipeStsPortEtherEntry": ipeStsPortEtherEntry,
       "ipeStsPortEtherIfIndex": ipeStsPortEtherIfIndex,
       "ipeStsPortEtherNEAddress": ipeStsPortEtherNEAddress,
       "ipeStsPortEtherLinkUp": ipeStsPortEtherLinkUp,
       "ipeStsPortEtherSpeed": ipeStsPortEtherSpeed,
       "ipeStsPortEtherDuplex": ipeStsPortEtherDuplex,
       "ipeStsPortEtherFlowControl": ipeStsPortEtherFlowControl,
       "ipeStsPortNe2Table": ipeStsPortNe2Table,
       "ipeStsPortNe2Entry": ipeStsPortNe2Entry,
       "ipeStsPortNe2IfIndex": ipeStsPortNe2IfIndex,
       "ipeStsPortNe2NEAddress": ipeStsPortNe2NEAddress,
       "ipeStsPortNe2LinkUp": ipeStsPortNe2LinkUp,
       "ipeStsBridge": ipeStsBridge,
       "ipeStsBridgeFdbTable": ipeStsBridgeFdbTable,
       "ipeStsBridgeFdbEntry": ipeStsBridgeFdbEntry,
       "ipeStsBridgeFdbBridgeIndex": ipeStsBridgeFdbBridgeIndex,
       "ipeStsBridgeFdbIfIndex": ipeStsBridgeFdbIfIndex,
       "ipeStsBridgeFdbIndex": ipeStsBridgeFdbIndex,
       "ipeStsBridgeFdbNEAddress": ipeStsBridgeFdbNEAddress,
       "ipeStsBridgeFdbAddress": ipeStsBridgeFdbAddress,
       "ipeStsAutoIp": ipeStsAutoIp,
       "ipeStsAutoIpTable": ipeStsAutoIpTable,
       "ipeStsAutoIpEntry": ipeStsAutoIpEntry,
       "ipeStsAutoIpIndex": ipeStsAutoIpIndex,
       "ipeStsAutoIpNEAddress": ipeStsAutoIpNEAddress,
       "ipeStsAutoIpState": ipeStsAutoIpState,
       "ipeStsAutoIpTempAddress": ipeStsAutoIpTempAddress,
       "ipeAccessGroup": ipeAccessGroup,
       "ipeAccessTable": ipeAccessTable,
       "ipeAccessEntry": ipeAccessEntry,
       "ipeAccessIndex": ipeAccessIndex,
       "ipeAccessNEAddress": ipeAccessNEAddress,
       "ipeAccessUserName": ipeAccessUserName,
       "ipeAccessFromAddress": ipeAccessFromAddress,
       "ipeAccessType": ipeAccessType,
       "ipeAccessSessionId": ipeAccessSessionId,
       "ipeAccessErrorCode": ipeAccessErrorCode}
)
