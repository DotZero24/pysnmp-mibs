# SNMP MIB module (NORTEL-NMI-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nortel/NORTEL-NMI-TC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:20:18 2025
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

(nortelNetworkManagementInterfaceMIBs,) = mibBuilder.importSymbols(
    "NORTEL-GENERIC-MIB",
    "nortelNetworkManagementInterfaceMIBs")

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
 TimeTicks,
 Unsigned32,
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
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

nortelNMItextConvMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 3)
)
if mibBuilder.loadTexts:
    nortelNMItextConvMIB.setRevisions(
        ("1999-07-19 00:00",
         "1999-06-24 00:00",
         "1999-05-31 00:00",
         "1999-04-12 00:00",
         "1999-03-22 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class NortelNMItimeStampDef(TextualConvention, Unsigned32):
    status = "current"


class NortelNMIneType(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class NortelNMIadminState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("shuttingDown", 2),
          ("unlocked", 3))
    )



class NortelNMIoperState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )



class NortelNMIunknownStatusValue(TruthValue):
    status = "current"


class NortelNMIalarmProblemCategory(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("communications", 1),
          ("qualityOfService", 2),
          ("processingError", 3),
          ("equipment", 4),
          ("environmental", 5))
    )



class NortelNMInotificationTypes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trap", 1),
          ("inform", 2))
    )



class NortelNMIalarmProbableCause(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
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
              118)
        )
    )
    namedValues = NamedValues(
        *(("adapterError", 1),
          ("applicationSubsystemFailure", 2),
          ("bandwidthReduced", 3),
          ("callEstablishmentError", 4),
          ("communicationsProtocolError", 5),
          ("communicationsSubsystemFailure", 6),
          ("configurationOrCustomizationError", 7),
          ("congestion", 8),
          ("corruptData", 9),
          ("cpuCyclesLimitExceeded", 10),
          ("dataSetOrModemError", 11),
          ("degradedSignal", 12),
          ("dteDCEInterfaceError", 13),
          ("enclosureDoorOpen", 14),
          ("equipmentMalfunction", 15),
          ("excessiveVibration", 16),
          ("fileError", 17),
          ("fireDetected", 18),
          ("floodDetected", 19),
          ("framingError", 20),
          ("heatingOrVentilationOrCoolingSystemProblem", 21),
          ("humidityUnacceptable", 22),
          ("inputOutputDeviceError", 23),
          ("inputDeviceError", 24),
          ("lANError", 25),
          ("leakDetected", 26),
          ("localNodeTransmissionError", 27),
          ("lossOfFrame", 28),
          ("lossOfSignal", 29),
          ("materialSupplyExhausted", 30),
          ("multiplexerProblem", 31),
          ("outOfMemory", 32),
          ("ouputDeviceError", 33),
          ("performanceDegraded", 34),
          ("powerProblem", 35),
          ("pressureUnacceptable", 36),
          ("processorProblem", 37),
          ("pumpFailure", 38),
          ("queueSizeExceeded", 39),
          ("receiveFailure", 40),
          ("receiverFailure", 41),
          ("remoteNodeTransmissionError", 42),
          ("resourceAtOrNearingCapacity", 43),
          ("responseTimeExecessive", 44),
          ("retransmissionRateExcessive", 45),
          ("softwareError", 46),
          ("softwareProgramAbnormallyTerminated", 47),
          ("softwareProgramError", 48),
          ("storageCapacityProblem", 49),
          ("temperatureUnacceptable", 50),
          ("thresholdCrossed", 51),
          ("timingProblem", 52),
          ("toxicLeakDetected", 53),
          ("transmitFailure", 54),
          ("transmitterFailure", 55),
          ("underlyingResourceUnavailable", 56),
          ("versionMismatch", 57),
          ("authenticationFailure", 101),
          ("breachOfConfidentiality", 102),
          ("cableTamper", 103),
          ("delayedInformation", 104),
          ("denialOfService", 105),
          ("duplicateInformation", 106),
          ("informationMissing", 107),
          ("informationModificationDetected", 108),
          ("informationOutOfSequence", 109),
          ("intrusionDetection", 110),
          ("keyExpired", 111),
          ("nonRepudiationFailure", 112),
          ("outOfHoursActivity", 113),
          ("outOfService", 114),
          ("proceduralError", 115),
          ("unauthorizedAccessAttempt", 116),
          ("unexpectedInformation", 117),
          ("unspecifiedReason", 118))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NORTEL-NMI-TC-MIB",
    **{"NortelNMItimeStampDef": NortelNMItimeStampDef,
       "NortelNMIneType": NortelNMIneType,
       "NortelNMIadminState": NortelNMIadminState,
       "NortelNMIoperState": NortelNMIoperState,
       "NortelNMIunknownStatusValue": NortelNMIunknownStatusValue,
       "NortelNMIalarmProblemCategory": NortelNMIalarmProblemCategory,
       "NortelNMInotificationTypes": NortelNMInotificationTypes,
       "NortelNMIalarmProbableCause": NortelNMIalarmProbableCause,
       "nortelNMItextConvMIB": nortelNMItextConvMIB}
)
