# SNMP MIB module (MULTI-MEDIA-MIB-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rfc/MULTI-MEDIA-MIB-TC
# Produced by pysmi-1.6.2 at Fri Oct 10 21:53:55 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class MmUtf8String(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class MmE164String(TextualConvention, OctetString):
    status = "current"
    displayHint = "128a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )



class MmTAddressTag(TextualConvention, Integer32):
    status = "current"
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
        *(("other", 0),
          ("ipv4", 1),
          ("ipv6", 2),
          ("ipx", 3),
          ("nsap", 4),
          ("netbios", 5))
    )



class MmGlobalIdentifier(TextualConvention, OctetString):
    status = "current"
    displayHint = "8d-9,3x,1d,2x:2x:2x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16



class MmAliasTag(TextualConvention, Integer32):
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("e164", 1),
          ("h323Id", 2),
          ("urlId", 3),
          ("transportId", 4),
          ("emailId", 5),
          ("partyNumber", 6))
    )



class MmAliasAddress(TextualConvention, OctetString):
    status = "current"
    displayHint = "512a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )



class MmEndpointID(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )



class MmGatekeeperID(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )



class MmH225Crv(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class MmTerminalAudioCapability(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("g711ALaw64KAudio", 0),
          ("g711ALaw56KAudio", 1),
          ("g711ULaw64KAudio", 2),
          ("g711ULaw56KAudio", 3),
          ("g722d64KAudio", 4),
          ("g722d56KAudio", 5),
          ("g722d48KAudio", 6),
          ("g728Audio", 7),
          ("g723d1d5d3KAudio", 8),
          ("g723d1d6d4KAudio", 9),
          ("g729Audio", 10))
    )


class MmTerminalDataCapability(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("t120", 0),
          ("dsmCc", 1),
          ("userData", 2),
          ("t84", 3),
          ("t434", 4),
          ("h224", 5),
          ("nlpid", 6),
          ("dsvdControl", 7),
          ("h222DataPartitioning", 8),
          ("t30fax", 9),
          ("t140", 10),
          ("others", 11))
    )


class MmTerminalVideoCapability(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("h261CIFVideo", 0),
          ("h261QCIFVideo", 1),
          ("h263SQCIFVideo", 2),
          ("h263QCIFVideo", 3),
          ("h263CIFVideo", 4),
          ("h263CIF4Video", 5),
          ("h263CIF16Video", 6),
          ("h262SPMLSIFVideo", 7),
          ("h262SPML2SIFVideo", 8),
          ("h262SPML4SIFVideo", 9),
          ("h262MPMLSIFVideo", 10),
          ("h262MPML2SIFVideo", 11),
          ("h262MPML4SIFVideo", 12))
    )


class MmTerminalLineRateCapability(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("bps64K", 0),
          ("bps2x64K", 1),
          ("bps3x64K", 2),
          ("bps4x64K", 3),
          ("bps5x64K", 4),
          ("bps6x64K", 5),
          ("bps384K", 6),
          ("bps2x384K", 7),
          ("bps3x384K", 8),
          ("bps5x384K", 9),
          ("bps1536K", 10),
          ("bps1920K", 11),
          ("bps128K", 12),
          ("bps192K", 13),
          ("bps256K", 14),
          ("bps320K", 15),
          ("bps512K", 16),
          ("bps768K", 17),
          ("bps1152K", 18),
          ("bps1452K", 19))
    )


class MmControlsCommands(TextualConvention, Integer32):
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("abruptRestart", 2),
          ("gracefulRestart", 3),
          ("abruptShutdown", 4),
          ("gracefulShutdown", 5),
          ("enterQuiescence", 6),
          ("exitQuiescence", 7),
          ("startLog", 8),
          ("stopLog", 9),
          ("resetStatistics", 10),
          ("runDiagnostic", 11))
    )



class MmErrorSeverity(TextualConvention, Integer32):
    status = "current"
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
        *(("cleared", 0),
          ("indeterminate", 1),
          ("critical", 2),
          ("major", 3),
          ("minor", 4),
          ("warning", 5))
    )



class MmErrorProbableCause(TextualConvention, Integer32):
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
              16,
              17,
              18,
              19,
              20,
              30,
              31,
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("qoSDegraded", 2),
          ("lossOfConn", 3),
          ("commProtocolError", 4),
          ("alarmSignal", 5),
          ("performanceDegraded", 6),
          ("callEstablishmentError", 16),
          ("alarmOnIncomingConn", 17),
          ("alarmOnOutgoingConn", 18),
          ("lossOfIncomingConn", 19),
          ("lossOfOutgoingConn", 20),
          ("componentFailure", 30),
          ("processingError", 31),
          ("congestion", 32),
          ("powerProblem", 33))
    )



class MmH323EndpointType(TextualConvention, Integer32):
    status = "current"


class MmCallType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("pointToPoint", 1),
          ("oneToN", 2),
          ("nToOne", 3),
          ("nToN", 4))
    )



# MIB Managed Objects in the order of their OIDs

_MmRoot_ObjectIdentity = ObjectIdentity
mmRoot = _MmRoot_ObjectIdentity(
    (0, 0, 8, 341, 1)
)
_MmH323Root_ObjectIdentity = ObjectIdentity
mmH323Root = _MmH323Root_ObjectIdentity(
    (0, 0, 8, 341, 1, 1)
)
if mibBuilder.loadTexts:
    mmH323Root.setStatus("current")
_MmH320Root_ObjectIdentity = ObjectIdentity
mmH320Root = _MmH320Root_ObjectIdentity(
    (0, 0, 8, 341, 1, 2)
)
if mibBuilder.loadTexts:
    mmH320Root.setStatus("current")
_MmH245Root_ObjectIdentity = ObjectIdentity
mmH245Root = _MmH245Root_ObjectIdentity(
    (0, 0, 8, 341, 1, 3)
)
if mibBuilder.loadTexts:
    mmH245Root.setStatus("current")
_MmH323GatewayRoot_ObjectIdentity = ObjectIdentity
mmH323GatewayRoot = _MmH323GatewayRoot_ObjectIdentity(
    (0, 0, 8, 341, 1, 4)
)
if mibBuilder.loadTexts:
    mmH323GatewayRoot.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MULTI-MEDIA-MIB-TC",
    **{"MmUtf8String": MmUtf8String,
       "MmE164String": MmE164String,
       "MmTAddressTag": MmTAddressTag,
       "MmGlobalIdentifier": MmGlobalIdentifier,
       "MmAliasTag": MmAliasTag,
       "MmAliasAddress": MmAliasAddress,
       "MmEndpointID": MmEndpointID,
       "MmGatekeeperID": MmGatekeeperID,
       "MmH225Crv": MmH225Crv,
       "MmTerminalAudioCapability": MmTerminalAudioCapability,
       "MmTerminalDataCapability": MmTerminalDataCapability,
       "MmTerminalVideoCapability": MmTerminalVideoCapability,
       "MmTerminalLineRateCapability": MmTerminalLineRateCapability,
       "MmControlsCommands": MmControlsCommands,
       "MmErrorSeverity": MmErrorSeverity,
       "MmErrorProbableCause": MmErrorProbableCause,
       "MmH323EndpointType": MmH323EndpointType,
       "MmCallType": MmCallType,
       "mmRoot": mmRoot,
       "mmH323Root": mmH323Root,
       "mmH320Root": mmH320Root,
       "mmH245Root": mmH245Root,
       "mmH323GatewayRoot": mmH323GatewayRoot}
)
