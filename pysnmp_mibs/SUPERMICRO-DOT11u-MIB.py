# SNMP MIB module (SUPERMICRO-DOT11u-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-DOT11u-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:04:44 2025
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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dot11MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78)
)
if mibBuilder.loadTexts:
    dot11MIB.setRevisions(
        ("2012-12-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dot11MIBObjects_ObjectIdentity = ObjectIdentity
dot11MIBObjects = _Dot11MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1)
)
_Dot11GASAdvertisement_ObjectIdentity = ObjectIdentity
dot11GASAdvertisement = _Dot11GASAdvertisement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 1)
)
_Dot11GASAdvertisementTable_Object = MibTable
dot11GASAdvertisementTable = _Dot11GASAdvertisementTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dot11GASAdvertisementTable.setStatus("current")
_Dot11GASAdvertisementEntry_Object = MibTableRow
dot11GASAdvertisementEntry = _Dot11GASAdvertisementEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 1, 1, 1)
)
dot11GASAdvertisementEntry.setIndexNames(
    (0, "SUPERMICRO-DOT11u-MIB", "dot11GASAdvertisementId"),
)
if mibBuilder.loadTexts:
    dot11GASAdvertisementEntry.setStatus("current")


class _Dot11GASAdvertisementId_Type(Integer32):
    """Custom type dot11GASAdvertisementId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Dot11GASAdvertisementId_Type.__name__ = "Integer32"
_Dot11GASAdvertisementId_Object = MibTableColumn
dot11GASAdvertisementId = _Dot11GASAdvertisementId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 1, 1, 1, 1),
    _Dot11GASAdvertisementId_Type()
)
dot11GASAdvertisementId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11GASAdvertisementId.setStatus("current")


class _Dot11GASPauseForServerResponse_Type(TruthValue):
    """Custom type dot11GASPauseForServerResponse based on TruthValue"""
    defaultValue = 2


_Dot11GASPauseForServerResponse_Type.__name__ = "TruthValue"
_Dot11GASPauseForServerResponse_Object = MibTableColumn
dot11GASPauseForServerResponse = _Dot11GASPauseForServerResponse_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 1, 1, 1, 2),
    _Dot11GASPauseForServerResponse_Type()
)
dot11GASPauseForServerResponse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11GASPauseForServerResponse.setStatus("current")


class _Dot11GASResponseTimeout_Type(Integer32):
    """Custom type dot11GASResponseTimeout based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 65535),
    )


_Dot11GASResponseTimeout_Type.__name__ = "Integer32"
_Dot11GASResponseTimeout_Object = MibTableColumn
dot11GASResponseTimeout = _Dot11GASResponseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 1, 1, 1, 3),
    _Dot11GASResponseTimeout_Type()
)
dot11GASResponseTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11GASResponseTimeout.setStatus("current")


class _Dot11GASComebackDelay_Type(Integer32):
    """Custom type dot11GASComebackDelay based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot11GASComebackDelay_Type.__name__ = "Integer32"
_Dot11GASComebackDelay_Object = MibTableColumn
dot11GASComebackDelay = _Dot11GASComebackDelay_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 1, 1, 1, 4),
    _Dot11GASComebackDelay_Type()
)
dot11GASComebackDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11GASComebackDelay.setStatus("current")


class _Dot11GASResponseBufferingTime_Type(Integer32):
    """Custom type dot11GASResponseBufferingTime based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot11GASResponseBufferingTime_Type.__name__ = "Integer32"
_Dot11GASResponseBufferingTime_Object = MibTableColumn
dot11GASResponseBufferingTime = _Dot11GASResponseBufferingTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 1, 1, 1, 5),
    _Dot11GASResponseBufferingTime_Type()
)
dot11GASResponseBufferingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11GASResponseBufferingTime.setStatus("current")


class _Dot11GASQueryResponseLengthLimit_Type(Integer32):
    """Custom type dot11GASQueryResponseLengthLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_Dot11GASQueryResponseLengthLimit_Type.__name__ = "Integer32"
_Dot11GASQueryResponseLengthLimit_Object = MibTableColumn
dot11GASQueryResponseLengthLimit = _Dot11GASQueryResponseLengthLimit_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 1, 1, 1, 6),
    _Dot11GASQueryResponseLengthLimit_Type()
)
dot11GASQueryResponseLengthLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11GASQueryResponseLengthLimit.setStatus("current")
_Dot11GASQueries_Type = Counter32
_Dot11GASQueries_Object = MibTableColumn
dot11GASQueries = _Dot11GASQueries_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 1, 1, 1, 7),
    _Dot11GASQueries_Type()
)
dot11GASQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11GASQueries.setStatus("current")
_Dot11GASQueryRate_Type = Unsigned32
_Dot11GASQueryRate_Object = MibTableColumn
dot11GASQueryRate = _Dot11GASQueryRate_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 1, 1, 1, 8),
    _Dot11GASQueryRate_Type()
)
dot11GASQueryRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11GASQueryRate.setStatus("current")
_Dot11GASResponses_Type = Counter32
_Dot11GASResponses_Object = MibTableColumn
dot11GASResponses = _Dot11GASResponses_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 1, 1, 1, 9),
    _Dot11GASResponses_Type()
)
dot11GASResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11GASResponses.setStatus("current")
_Dot11GASResponseRate_Type = Unsigned32
_Dot11GASResponseRate_Object = MibTableColumn
dot11GASResponseRate = _Dot11GASResponseRate_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 1, 1, 1, 10),
    _Dot11GASResponseRate_Type()
)
dot11GASResponseRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11GASResponseRate.setStatus("current")
_Dot11GASTransmittedFragmentCount_Type = Counter32
_Dot11GASTransmittedFragmentCount_Object = MibTableColumn
dot11GASTransmittedFragmentCount = _Dot11GASTransmittedFragmentCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 1, 1, 1, 11),
    _Dot11GASTransmittedFragmentCount_Type()
)
dot11GASTransmittedFragmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11GASTransmittedFragmentCount.setStatus("current")
_Dot11GASReceivedFragmentCount_Type = Counter32
_Dot11GASReceivedFragmentCount_Object = MibTableColumn
dot11GASReceivedFragmentCount = _Dot11GASReceivedFragmentCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 1, 1, 1, 12),
    _Dot11GASReceivedFragmentCount_Type()
)
dot11GASReceivedFragmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11GASReceivedFragmentCount.setStatus("current")
_Dot11GASNoRequestOutstanding_Type = Counter32
_Dot11GASNoRequestOutstanding_Object = MibTableColumn
dot11GASNoRequestOutstanding = _Dot11GASNoRequestOutstanding_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 1, 1, 1, 13),
    _Dot11GASNoRequestOutstanding_Type()
)
dot11GASNoRequestOutstanding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11GASNoRequestOutstanding.setStatus("current")
_Dot11GASResponsesDiscarded_Type = Counter32
_Dot11GASResponsesDiscarded_Object = MibTableColumn
dot11GASResponsesDiscarded = _Dot11GASResponsesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 1, 1, 1, 14),
    _Dot11GASResponsesDiscarded_Type()
)
dot11GASResponsesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11GASResponsesDiscarded.setStatus("current")
_Dot11GASFailedResponses_Type = Counter32
_Dot11GASFailedResponses_Object = MibTableColumn
dot11GASFailedResponses = _Dot11GASFailedResponses_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 1, 1, 1, 15),
    _Dot11GASFailedResponses_Type()
)
dot11GASFailedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11GASFailedResponses.setStatus("current")
_Dot11StationConfig_ObjectIdentity = ObjectIdentity
dot11StationConfig = _Dot11StationConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 2)
)
_Dot11StationConfigTable_Object = MibTable
dot11StationConfigTable = _Dot11StationConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dot11StationConfigTable.setStatus("current")
_Dot11StationConfigEntry_Object = MibTableRow
dot11StationConfigEntry = _Dot11StationConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 2, 1, 1)
)
dot11StationConfigEntry.setIndexNames(
    (0, "SUPERMICRO-DOT11u-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11StationConfigEntry.setStatus("current")


class _IfIndex_Type(Integer32):
    """Custom type ifIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IfIndex_Type.__name__ = "Integer32"
_IfIndex_Object = MibTableColumn
ifIndex = _IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 2, 1, 1, 1),
    _IfIndex_Type()
)
ifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifIndex.setStatus("current")


class _Dot11InterworkingServiceImplemented_Type(TruthValue):
    """Custom type dot11InterworkingServiceImplemented based on TruthValue"""
    defaultValue = 1


_Dot11InterworkingServiceImplemented_Type.__name__ = "TruthValue"
_Dot11InterworkingServiceImplemented_Object = MibTableColumn
dot11InterworkingServiceImplemented = _Dot11InterworkingServiceImplemented_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 2, 1, 1, 2),
    _Dot11InterworkingServiceImplemented_Type()
)
dot11InterworkingServiceImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11InterworkingServiceImplemented.setStatus("current")


class _Dot11InterworkingServiceActivated_Type(TruthValue):
    """Custom type dot11InterworkingServiceActivated based on TruthValue"""
    defaultValue = 1


_Dot11InterworkingServiceActivated_Type.__name__ = "TruthValue"
_Dot11InterworkingServiceActivated_Object = MibTableColumn
dot11InterworkingServiceActivated = _Dot11InterworkingServiceActivated_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 2, 1, 1, 3),
    _Dot11InterworkingServiceActivated_Type()
)
dot11InterworkingServiceActivated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11InterworkingServiceActivated.setStatus("current")


class _Dot11QosmapImplemented_Type(TruthValue):
    """Custom type dot11QosmapImplemented based on TruthValue"""
    defaultValue = 2


_Dot11QosmapImplemented_Type.__name__ = "TruthValue"
_Dot11QosmapImplemented_Object = MibTableColumn
dot11QosmapImplemented = _Dot11QosmapImplemented_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 2, 1, 1, 4),
    _Dot11QosmapImplemented_Type()
)
dot11QosmapImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11QosmapImplemented.setStatus("current")


class _Dot11QosMapActivated_Type(TruthValue):
    """Custom type dot11QosMapActivated based on TruthValue"""
    defaultValue = 2


_Dot11QosMapActivated_Type.__name__ = "TruthValue"
_Dot11QosMapActivated_Object = MibTableColumn
dot11QosMapActivated = _Dot11QosMapActivated_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 2, 1, 1, 5),
    _Dot11QosMapActivated_Type()
)
dot11QosMapActivated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11QosMapActivated.setStatus("current")


class _Dot11EBRImplemented_Type(TruthValue):
    """Custom type dot11EBRImplemented based on TruthValue"""
    defaultValue = 2


_Dot11EBRImplemented_Type.__name__ = "TruthValue"
_Dot11EBRImplemented_Object = MibTableColumn
dot11EBRImplemented = _Dot11EBRImplemented_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 2, 1, 1, 6),
    _Dot11EBRImplemented_Type()
)
dot11EBRImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11EBRImplemented.setStatus("current")


class _Dot11EBRActivated_Type(TruthValue):
    """Custom type dot11EBRActivated based on TruthValue"""
    defaultValue = 2


_Dot11EBRActivated_Type.__name__ = "TruthValue"
_Dot11EBRActivated_Object = MibTableColumn
dot11EBRActivated = _Dot11EBRActivated_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 2, 1, 1, 7),
    _Dot11EBRActivated_Type()
)
dot11EBRActivated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11EBRActivated.setStatus("current")
_Dot11ESNetwork_Type = TruthValue
_Dot11ESNetwork_Object = MibTableColumn
dot11ESNetwork = _Dot11ESNetwork_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 2, 1, 1, 8),
    _Dot11ESNetwork_Type()
)
dot11ESNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ESNetwork.setStatus("current")


class _Dot11SSPNInterfaceImplemented_Type(TruthValue):
    """Custom type dot11SSPNInterfaceImplemented based on TruthValue"""
    defaultValue = 2


_Dot11SSPNInterfaceImplemented_Type.__name__ = "TruthValue"
_Dot11SSPNInterfaceImplemented_Object = MibTableColumn
dot11SSPNInterfaceImplemented = _Dot11SSPNInterfaceImplemented_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 2, 1, 1, 9),
    _Dot11SSPNInterfaceImplemented_Type()
)
dot11SSPNInterfaceImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11SSPNInterfaceImplemented.setStatus("current")


class _Dot11SSPNInterfaceActivated_Type(TruthValue):
    """Custom type dot11SSPNInterfaceActivated based on TruthValue"""
    defaultValue = 2


_Dot11SSPNInterfaceActivated_Type.__name__ = "TruthValue"
_Dot11SSPNInterfaceActivated_Object = MibTableColumn
dot11SSPNInterfaceActivated = _Dot11SSPNInterfaceActivated_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 2, 1, 1, 10),
    _Dot11SSPNInterfaceActivated_Type()
)
dot11SSPNInterfaceActivated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11SSPNInterfaceActivated.setStatus("current")
_Dot11HESSID_Type = MacAddress
_Dot11HESSID_Object = MibTableColumn
dot11HESSID = _Dot11HESSID_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 2, 1, 1, 11),
    _Dot11HESSID_Type()
)
dot11HESSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11HESSID.setStatus("current")


class _Dot11EASImplemented_Type(TruthValue):
    """Custom type dot11EASImplemented based on TruthValue"""
    defaultValue = 2


_Dot11EASImplemented_Type.__name__ = "TruthValue"
_Dot11EASImplemented_Object = MibTableColumn
dot11EASImplemented = _Dot11EASImplemented_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 2, 1, 1, 12),
    _Dot11EASImplemented_Type()
)
dot11EASImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11EASImplemented.setStatus("current")


class _Dot11EASActivated_Type(TruthValue):
    """Custom type dot11EASActivated based on TruthValue"""
    defaultValue = 2


_Dot11EASActivated_Type.__name__ = "TruthValue"
_Dot11EASActivated_Object = MibTableColumn
dot11EASActivated = _Dot11EASActivated_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 2, 1, 1, 13),
    _Dot11EASActivated_Type()
)
dot11EASActivated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11EASActivated.setStatus("current")


class _Dot11MSGCFImplemented_Type(TruthValue):
    """Custom type dot11MSGCFImplemented based on TruthValue"""
    defaultValue = 2


_Dot11MSGCFImplemented_Type.__name__ = "TruthValue"
_Dot11MSGCFImplemented_Object = MibTableColumn
dot11MSGCFImplemented = _Dot11MSGCFImplemented_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 2, 1, 1, 14),
    _Dot11MSGCFImplemented_Type()
)
dot11MSGCFImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11MSGCFImplemented.setStatus("current")


class _Dot11MSGCFActivated_Type(TruthValue):
    """Custom type dot11MSGCFActivated based on TruthValue"""
    defaultValue = 2


_Dot11MSGCFActivated_Type.__name__ = "TruthValue"
_Dot11MSGCFActivated_Object = MibTableColumn
dot11MSGCFActivated = _Dot11MSGCFActivated_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 2, 1, 1, 15),
    _Dot11MSGCFActivated_Type()
)
dot11MSGCFActivated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MSGCFActivated.setStatus("current")
_Dot11StationID_Type = MacAddress
_Dot11StationID_Object = MibTableColumn
dot11StationID = _Dot11StationID_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 2, 1, 1, 16),
    _Dot11StationID_Type()
)
dot11StationID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11StationID.setStatus("deprecated")


class _Dot11MediumOccupancyLimit_Type(Integer32):
    """Custom type dot11MediumOccupancyLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dot11MediumOccupancyLimit_Type.__name__ = "Integer32"
_Dot11MediumOccupancyLimit_Object = MibTableColumn
dot11MediumOccupancyLimit = _Dot11MediumOccupancyLimit_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 2, 1, 1, 17),
    _Dot11MediumOccupancyLimit_Type()
)
dot11MediumOccupancyLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MediumOccupancyLimit.setStatus("current")
_Dot11CFPollable_Type = TruthValue
_Dot11CFPollable_Object = MibTableColumn
dot11CFPollable = _Dot11CFPollable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 2, 1, 1, 18),
    _Dot11CFPollable_Type()
)
dot11CFPollable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11CFPollable.setStatus("current")


class _Dot11CFPPeriod_Type(Integer32):
    """Custom type dot11CFPPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Dot11CFPPeriod_Type.__name__ = "Integer32"
_Dot11CFPPeriod_Object = MibTableColumn
dot11CFPPeriod = _Dot11CFPPeriod_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 2, 1, 1, 19),
    _Dot11CFPPeriod_Type()
)
dot11CFPPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CFPPeriod.setStatus("current")


class _Dot11CFPMaxDuration_Type(Integer32):
    """Custom type dot11CFPMaxDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot11CFPMaxDuration_Type.__name__ = "Integer32"
_Dot11CFPMaxDuration_Object = MibTableColumn
dot11CFPMaxDuration = _Dot11CFPMaxDuration_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 2, 1, 1, 20),
    _Dot11CFPMaxDuration_Type()
)
dot11CFPMaxDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CFPMaxDuration.setStatus("current")


class _Dot11AuthenticationResponseTimeOut_Type(Unsigned32):
    """Custom type dot11AuthenticationResponseTimeOut based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Dot11AuthenticationResponseTimeOut_Type.__name__ = "Unsigned32"
_Dot11AuthenticationResponseTimeOut_Object = MibTableColumn
dot11AuthenticationResponseTimeOut = _Dot11AuthenticationResponseTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 2, 1, 1, 21),
    _Dot11AuthenticationResponseTimeOut_Type()
)
dot11AuthenticationResponseTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11AuthenticationResponseTimeOut.setStatus("current")
_Dot11PrivacyOptionImplemented_Type = TruthValue
_Dot11PrivacyOptionImplemented_Object = MibTableColumn
dot11PrivacyOptionImplemented = _Dot11PrivacyOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 2, 1, 1, 22),
    _Dot11PrivacyOptionImplemented_Type()
)
dot11PrivacyOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11PrivacyOptionImplemented.setStatus("current")


class _Dot11PowerManagementMode_Type(Integer32):
    """Custom type dot11PowerManagementMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("powersave", 2))
    )


_Dot11PowerManagementMode_Type.__name__ = "Integer32"
_Dot11PowerManagementMode_Object = MibTableColumn
dot11PowerManagementMode = _Dot11PowerManagementMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 2, 1, 1, 23),
    _Dot11PowerManagementMode_Type()
)
dot11PowerManagementMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11PowerManagementMode.setStatus("current")


class _Dot11DesiredSSID_Type(OctetString):
    """Custom type dot11DesiredSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Dot11DesiredSSID_Type.__name__ = "OctetString"
_Dot11DesiredSSID_Object = MibTableColumn
dot11DesiredSSID = _Dot11DesiredSSID_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 2, 1, 1, 24),
    _Dot11DesiredSSID_Type()
)
dot11DesiredSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DesiredSSID.setStatus("current")


class _Dot11DesiredBSSType_Type(Integer32):
    """Custom type dot11DesiredBSSType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("infrastructure", 1),
          ("independent", 2),
          ("any", 3))
    )


_Dot11DesiredBSSType_Type.__name__ = "Integer32"
_Dot11DesiredBSSType_Object = MibTableColumn
dot11DesiredBSSType = _Dot11DesiredBSSType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 2, 1, 1, 25),
    _Dot11DesiredBSSType_Type()
)
dot11DesiredBSSType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DesiredBSSType.setStatus("current")


class _Dot11OperationalRateSet_Type(OctetString):
    """Custom type dot11OperationalRateSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 126),
    )


_Dot11OperationalRateSet_Type.__name__ = "OctetString"
_Dot11OperationalRateSet_Object = MibTableColumn
dot11OperationalRateSet = _Dot11OperationalRateSet_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 2, 1, 1, 26),
    _Dot11OperationalRateSet_Type()
)
dot11OperationalRateSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11OperationalRateSet.setStatus("current")


class _Dot11BeaconPeriod_Type(Integer32):
    """Custom type dot11BeaconPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot11BeaconPeriod_Type.__name__ = "Integer32"
_Dot11BeaconPeriod_Object = MibTableColumn
dot11BeaconPeriod = _Dot11BeaconPeriod_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 2, 1, 1, 27),
    _Dot11BeaconPeriod_Type()
)
dot11BeaconPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11BeaconPeriod.setStatus("current")


class _Dot11DTIMPeriod_Type(Integer32):
    """Custom type dot11DTIMPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Dot11DTIMPeriod_Type.__name__ = "Integer32"
_Dot11DTIMPeriod_Object = MibTableColumn
dot11DTIMPeriod = _Dot11DTIMPeriod_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 2, 1, 1, 28),
    _Dot11DTIMPeriod_Type()
)
dot11DTIMPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DTIMPeriod.setStatus("current")


class _Dot11AssociationResponseTimeOut_Type(Unsigned32):
    """Custom type dot11AssociationResponseTimeOut based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Dot11AssociationResponseTimeOut_Type.__name__ = "Unsigned32"
_Dot11AssociationResponseTimeOut_Object = MibTableColumn
dot11AssociationResponseTimeOut = _Dot11AssociationResponseTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 2, 1, 1, 29),
    _Dot11AssociationResponseTimeOut_Type()
)
dot11AssociationResponseTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11AssociationResponseTimeOut.setStatus("current")


class _Dot11DisassociateReason_Type(Integer32):
    """Custom type dot11DisassociateReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot11DisassociateReason_Type.__name__ = "Integer32"
_Dot11DisassociateReason_Object = MibTableColumn
dot11DisassociateReason = _Dot11DisassociateReason_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 2, 1, 1, 30),
    _Dot11DisassociateReason_Type()
)
dot11DisassociateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11DisassociateReason.setStatus("current")
_Dot11DisassociateStation_Type = MacAddress
_Dot11DisassociateStation_Object = MibTableColumn
dot11DisassociateStation = _Dot11DisassociateStation_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 2, 1, 1, 31),
    _Dot11DisassociateStation_Type()
)
dot11DisassociateStation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11DisassociateStation.setStatus("current")


class _Dot11DeauthenticateReason_Type(Integer32):
    """Custom type dot11DeauthenticateReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot11DeauthenticateReason_Type.__name__ = "Integer32"
_Dot11DeauthenticateReason_Object = MibTableColumn
dot11DeauthenticateReason = _Dot11DeauthenticateReason_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 2, 1, 1, 32),
    _Dot11DeauthenticateReason_Type()
)
dot11DeauthenticateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11DeauthenticateReason.setStatus("current")
_Dot11DeauthenticateStation_Type = MacAddress
_Dot11DeauthenticateStation_Object = MibTableColumn
dot11DeauthenticateStation = _Dot11DeauthenticateStation_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 2, 1, 1, 33),
    _Dot11DeauthenticateStation_Type()
)
dot11DeauthenticateStation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11DeauthenticateStation.setStatus("current")


class _Dot11AuthenticateFailStatus_Type(Integer32):
    """Custom type dot11AuthenticateFailStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot11AuthenticateFailStatus_Type.__name__ = "Integer32"
_Dot11AuthenticateFailStatus_Object = MibTableColumn
dot11AuthenticateFailStatus = _Dot11AuthenticateFailStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 2, 1, 1, 34),
    _Dot11AuthenticateFailStatus_Type()
)
dot11AuthenticateFailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11AuthenticateFailStatus.setStatus("current")
_Dot11AuthenticateFailStation_Type = MacAddress
_Dot11AuthenticateFailStation_Object = MibTableColumn
dot11AuthenticateFailStation = _Dot11AuthenticateFailStation_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 2, 1, 1, 35),
    _Dot11AuthenticateFailStation_Type()
)
dot11AuthenticateFailStation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11AuthenticateFailStation.setStatus("current")
_Dot11MultiDomainCapabilityImplemented_Type = TruthValue
_Dot11MultiDomainCapabilityImplemented_Object = MibTableColumn
dot11MultiDomainCapabilityImplemented = _Dot11MultiDomainCapabilityImplemented_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 2, 1, 1, 36),
    _Dot11MultiDomainCapabilityImplemented_Type()
)
dot11MultiDomainCapabilityImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11MultiDomainCapabilityImplemented.setStatus("current")
_Dot11MultiDomainCapabilityEnabled_Type = TruthValue
_Dot11MultiDomainCapabilityEnabled_Object = MibTableColumn
dot11MultiDomainCapabilityEnabled = _Dot11MultiDomainCapabilityEnabled_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 2, 1, 1, 37),
    _Dot11MultiDomainCapabilityEnabled_Type()
)
dot11MultiDomainCapabilityEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MultiDomainCapabilityEnabled.setStatus("current")


class _Dot11CountryString_Type(OctetString):
    """Custom type dot11CountryString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_Dot11CountryString_Type.__name__ = "OctetString"
_Dot11CountryString_Object = MibTableColumn
dot11CountryString = _Dot11CountryString_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 78, 1, 2, 1, 1, 38),
    _Dot11CountryString_Type()
)
dot11CountryString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11CountryString.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-DOT11u-MIB",
    **{"dot11MIB": dot11MIB,
       "dot11MIBObjects": dot11MIBObjects,
       "dot11GASAdvertisement": dot11GASAdvertisement,
       "dot11GASAdvertisementTable": dot11GASAdvertisementTable,
       "dot11GASAdvertisementEntry": dot11GASAdvertisementEntry,
       "dot11GASAdvertisementId": dot11GASAdvertisementId,
       "dot11GASPauseForServerResponse": dot11GASPauseForServerResponse,
       "dot11GASResponseTimeout": dot11GASResponseTimeout,
       "dot11GASComebackDelay": dot11GASComebackDelay,
       "dot11GASResponseBufferingTime": dot11GASResponseBufferingTime,
       "dot11GASQueryResponseLengthLimit": dot11GASQueryResponseLengthLimit,
       "dot11GASQueries": dot11GASQueries,
       "dot11GASQueryRate": dot11GASQueryRate,
       "dot11GASResponses": dot11GASResponses,
       "dot11GASResponseRate": dot11GASResponseRate,
       "dot11GASTransmittedFragmentCount": dot11GASTransmittedFragmentCount,
       "dot11GASReceivedFragmentCount": dot11GASReceivedFragmentCount,
       "dot11GASNoRequestOutstanding": dot11GASNoRequestOutstanding,
       "dot11GASResponsesDiscarded": dot11GASResponsesDiscarded,
       "dot11GASFailedResponses": dot11GASFailedResponses,
       "dot11StationConfig": dot11StationConfig,
       "dot11StationConfigTable": dot11StationConfigTable,
       "dot11StationConfigEntry": dot11StationConfigEntry,
       "ifIndex": ifIndex,
       "dot11InterworkingServiceImplemented": dot11InterworkingServiceImplemented,
       "dot11InterworkingServiceActivated": dot11InterworkingServiceActivated,
       "dot11QosmapImplemented": dot11QosmapImplemented,
       "dot11QosMapActivated": dot11QosMapActivated,
       "dot11EBRImplemented": dot11EBRImplemented,
       "dot11EBRActivated": dot11EBRActivated,
       "dot11ESNetwork": dot11ESNetwork,
       "dot11SSPNInterfaceImplemented": dot11SSPNInterfaceImplemented,
       "dot11SSPNInterfaceActivated": dot11SSPNInterfaceActivated,
       "dot11HESSID": dot11HESSID,
       "dot11EASImplemented": dot11EASImplemented,
       "dot11EASActivated": dot11EASActivated,
       "dot11MSGCFImplemented": dot11MSGCFImplemented,
       "dot11MSGCFActivated": dot11MSGCFActivated,
       "dot11StationID": dot11StationID,
       "dot11MediumOccupancyLimit": dot11MediumOccupancyLimit,
       "dot11CFPollable": dot11CFPollable,
       "dot11CFPPeriod": dot11CFPPeriod,
       "dot11CFPMaxDuration": dot11CFPMaxDuration,
       "dot11AuthenticationResponseTimeOut": dot11AuthenticationResponseTimeOut,
       "dot11PrivacyOptionImplemented": dot11PrivacyOptionImplemented,
       "dot11PowerManagementMode": dot11PowerManagementMode,
       "dot11DesiredSSID": dot11DesiredSSID,
       "dot11DesiredBSSType": dot11DesiredBSSType,
       "dot11OperationalRateSet": dot11OperationalRateSet,
       "dot11BeaconPeriod": dot11BeaconPeriod,
       "dot11DTIMPeriod": dot11DTIMPeriod,
       "dot11AssociationResponseTimeOut": dot11AssociationResponseTimeOut,
       "dot11DisassociateReason": dot11DisassociateReason,
       "dot11DisassociateStation": dot11DisassociateStation,
       "dot11DeauthenticateReason": dot11DeauthenticateReason,
       "dot11DeauthenticateStation": dot11DeauthenticateStation,
       "dot11AuthenticateFailStatus": dot11AuthenticateFailStatus,
       "dot11AuthenticateFailStation": dot11AuthenticateFailStation,
       "dot11MultiDomainCapabilityImplemented": dot11MultiDomainCapabilityImplemented,
       "dot11MultiDomainCapabilityEnabled": dot11MultiDomainCapabilityEnabled,
       "dot11CountryString": dot11CountryString}
)
