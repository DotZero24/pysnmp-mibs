# SNMP MIB module (ELTEX-MSDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MSDP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:50:08 2025
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

(eltexLtd,) = mibBuilder.importSymbols(
    "ELTEX-SMI-ACTUAL",
    "eltexLtd")

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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

eltexMsdpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 51)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EltexMsdpSAFilterDirection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )



class EltexMsdpSAFilterAction(TextualConvention, Integer32):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_EltexMsdpObjects_ObjectIdentity = ObjectIdentity
eltexMsdpObjects = _EltexMsdpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1)
)
_EltexMsdp_ObjectIdentity = ObjectIdentity
eltexMsdp = _EltexMsdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1)
)
_EltexMsdpTraps_ObjectIdentity = ObjectIdentity
eltexMsdpTraps = _EltexMsdpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 0)
)


class _EltexMsdpCacheLifetime_Type(Integer32):
    """Custom type eltexMsdpCacheLifetime based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(150, 3600),
    )


_EltexMsdpCacheLifetime_Type.__name__ = "Integer32"
_EltexMsdpCacheLifetime_Object = MibScalar
eltexMsdpCacheLifetime = _EltexMsdpCacheLifetime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 2),
    _EltexMsdpCacheLifetime_Type()
)
eltexMsdpCacheLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexMsdpCacheLifetime.setStatus("current")
if mibBuilder.loadTexts:
    eltexMsdpCacheLifetime.setUnits("seconds")
_EltexMsdpSACacheTable_Object = MibTable
eltexMsdpSACacheTable = _EltexMsdpSACacheTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 6)
)
if mibBuilder.loadTexts:
    eltexMsdpSACacheTable.setStatus("current")
_EltexMsdpSACacheEntry_Object = MibTableRow
eltexMsdpSACacheEntry = _EltexMsdpSACacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 6, 1)
)
eltexMsdpSACacheEntry.setIndexNames(
    (0, "ELTEX-MSDP-MIB", "eltexMsdpSACacheGroupAddr"),
    (0, "ELTEX-MSDP-MIB", "eltexMsdpSACacheSourceAddr"),
)
if mibBuilder.loadTexts:
    eltexMsdpSACacheEntry.setStatus("current")
_EltexMsdpSACacheGroupAddr_Type = IpAddress
_EltexMsdpSACacheGroupAddr_Object = MibTableColumn
eltexMsdpSACacheGroupAddr = _EltexMsdpSACacheGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 6, 1, 1),
    _EltexMsdpSACacheGroupAddr_Type()
)
eltexMsdpSACacheGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexMsdpSACacheGroupAddr.setStatus("current")
_EltexMsdpSACacheSourceAddr_Type = IpAddress
_EltexMsdpSACacheSourceAddr_Object = MibTableColumn
eltexMsdpSACacheSourceAddr = _EltexMsdpSACacheSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 6, 1, 2),
    _EltexMsdpSACacheSourceAddr_Type()
)
eltexMsdpSACacheSourceAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexMsdpSACacheSourceAddr.setStatus("current")
_EltexMsdpSACacheOriginRP_Type = IpAddress
_EltexMsdpSACacheOriginRP_Object = MibTableColumn
eltexMsdpSACacheOriginRP = _EltexMsdpSACacheOriginRP_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 6, 1, 3),
    _EltexMsdpSACacheOriginRP_Type()
)
eltexMsdpSACacheOriginRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexMsdpSACacheOriginRP.setStatus("current")
_EltexMsdpSACachePeerLearnedFrom_Type = IpAddress
_EltexMsdpSACachePeerLearnedFrom_Object = MibTableColumn
eltexMsdpSACachePeerLearnedFrom = _EltexMsdpSACachePeerLearnedFrom_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 6, 1, 4),
    _EltexMsdpSACachePeerLearnedFrom_Type()
)
eltexMsdpSACachePeerLearnedFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexMsdpSACachePeerLearnedFrom.setStatus("current")
_EltexMsdpSACacheUpTime_Type = TimeTicks
_EltexMsdpSACacheUpTime_Object = MibTableColumn
eltexMsdpSACacheUpTime = _EltexMsdpSACacheUpTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 6, 1, 8),
    _EltexMsdpSACacheUpTime_Type()
)
eltexMsdpSACacheUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexMsdpSACacheUpTime.setStatus("current")
_EltexMsdpPeerTable_Object = MibTable
eltexMsdpPeerTable = _EltexMsdpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 10)
)
if mibBuilder.loadTexts:
    eltexMsdpPeerTable.setStatus("current")
_EltexMsdpPeerEntry_Object = MibTableRow
eltexMsdpPeerEntry = _EltexMsdpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 10, 1)
)
eltexMsdpPeerEntry.setIndexNames(
    (0, "ELTEX-MSDP-MIB", "eltexMsdpPeerRemoteAddress"),
)
if mibBuilder.loadTexts:
    eltexMsdpPeerEntry.setStatus("current")
_EltexMsdpPeerRemoteAddress_Type = IpAddress
_EltexMsdpPeerRemoteAddress_Object = MibTableColumn
eltexMsdpPeerRemoteAddress = _EltexMsdpPeerRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 10, 1, 1),
    _EltexMsdpPeerRemoteAddress_Type()
)
eltexMsdpPeerRemoteAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexMsdpPeerRemoteAddress.setStatus("current")


class _EltexMsdpPeerState_Type(Integer32):
    """Custom type eltexMsdpPeerState based on Integer32"""
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
        *(("inactive", 1),
          ("listen", 2),
          ("connecting", 3),
          ("established", 4),
          ("disabled", 5))
    )


_EltexMsdpPeerState_Type.__name__ = "Integer32"
_EltexMsdpPeerState_Object = MibTableColumn
eltexMsdpPeerState = _EltexMsdpPeerState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 10, 1, 3),
    _EltexMsdpPeerState_Type()
)
eltexMsdpPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexMsdpPeerState.setStatus("current")
_EltexMsdpPeerRPFFailures_Type = Counter32
_EltexMsdpPeerRPFFailures_Object = MibTableColumn
eltexMsdpPeerRPFFailures = _EltexMsdpPeerRPFFailures_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 10, 1, 4),
    _EltexMsdpPeerRPFFailures_Type()
)
eltexMsdpPeerRPFFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexMsdpPeerRPFFailures.setStatus("current")
_EltexMsdpPeerInSAs_Type = Counter32
_EltexMsdpPeerInSAs_Object = MibTableColumn
eltexMsdpPeerInSAs = _EltexMsdpPeerInSAs_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 10, 1, 5),
    _EltexMsdpPeerInSAs_Type()
)
eltexMsdpPeerInSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexMsdpPeerInSAs.setStatus("current")
_EltexMsdpPeerOutSAs_Type = Counter32
_EltexMsdpPeerOutSAs_Object = MibTableColumn
eltexMsdpPeerOutSAs = _EltexMsdpPeerOutSAs_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 10, 1, 6),
    _EltexMsdpPeerOutSAs_Type()
)
eltexMsdpPeerOutSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexMsdpPeerOutSAs.setStatus("current")
_EltexMsdpPeerInSARequests_Type = Counter32
_EltexMsdpPeerInSARequests_Object = MibTableColumn
eltexMsdpPeerInSARequests = _EltexMsdpPeerInSARequests_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 10, 1, 7),
    _EltexMsdpPeerInSARequests_Type()
)
eltexMsdpPeerInSARequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexMsdpPeerInSARequests.setStatus("current")
_EltexMsdpPeerOutSARequests_Type = Counter32
_EltexMsdpPeerOutSARequests_Object = MibTableColumn
eltexMsdpPeerOutSARequests = _EltexMsdpPeerOutSARequests_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 10, 1, 8),
    _EltexMsdpPeerOutSARequests_Type()
)
eltexMsdpPeerOutSARequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexMsdpPeerOutSARequests.setStatus("current")
_EltexMsdpPeerInSAResponses_Type = Counter32
_EltexMsdpPeerInSAResponses_Object = MibTableColumn
eltexMsdpPeerInSAResponses = _EltexMsdpPeerInSAResponses_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 10, 1, 9),
    _EltexMsdpPeerInSAResponses_Type()
)
eltexMsdpPeerInSAResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexMsdpPeerInSAResponses.setStatus("current")
_EltexMsdpPeerOutSAResponses_Type = Counter32
_EltexMsdpPeerOutSAResponses_Object = MibTableColumn
eltexMsdpPeerOutSAResponses = _EltexMsdpPeerOutSAResponses_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 10, 1, 10),
    _EltexMsdpPeerOutSAResponses_Type()
)
eltexMsdpPeerOutSAResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexMsdpPeerOutSAResponses.setStatus("current")
_EltexMsdpPeerInControlMessages_Type = Counter32
_EltexMsdpPeerInControlMessages_Object = MibTableColumn
eltexMsdpPeerInControlMessages = _EltexMsdpPeerInControlMessages_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 10, 1, 11),
    _EltexMsdpPeerInControlMessages_Type()
)
eltexMsdpPeerInControlMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexMsdpPeerInControlMessages.setStatus("current")
_EltexMsdpPeerOutControlMessages_Type = Counter32
_EltexMsdpPeerOutControlMessages_Object = MibTableColumn
eltexMsdpPeerOutControlMessages = _EltexMsdpPeerOutControlMessages_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 10, 1, 12),
    _EltexMsdpPeerOutControlMessages_Type()
)
eltexMsdpPeerOutControlMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexMsdpPeerOutControlMessages.setStatus("current")
_EltexMsdpPeerFsmEstablishedTime_Type = TimeStamp
_EltexMsdpPeerFsmEstablishedTime_Object = MibTableColumn
eltexMsdpPeerFsmEstablishedTime = _EltexMsdpPeerFsmEstablishedTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 10, 1, 16),
    _EltexMsdpPeerFsmEstablishedTime_Type()
)
eltexMsdpPeerFsmEstablishedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexMsdpPeerFsmEstablishedTime.setStatus("current")
_EltexMsdpPeerInMessageTime_Type = TimeStamp
_EltexMsdpPeerInMessageTime_Object = MibTableColumn
eltexMsdpPeerInMessageTime = _EltexMsdpPeerInMessageTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 10, 1, 17),
    _EltexMsdpPeerInMessageTime_Type()
)
eltexMsdpPeerInMessageTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexMsdpPeerInMessageTime.setStatus("current")
_EltexMsdpPeerLocalAddress_Type = IpAddress
_EltexMsdpPeerLocalAddress_Object = MibTableColumn
eltexMsdpPeerLocalAddress = _EltexMsdpPeerLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 10, 1, 18),
    _EltexMsdpPeerLocalAddress_Type()
)
eltexMsdpPeerLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexMsdpPeerLocalAddress.setStatus("current")
_EltexMsdpPeerRowStatus_Type = RowStatus
_EltexMsdpPeerRowStatus_Object = MibTableColumn
eltexMsdpPeerRowStatus = _EltexMsdpPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 10, 1, 25),
    _EltexMsdpPeerRowStatus_Type()
)
eltexMsdpPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexMsdpPeerRowStatus.setStatus("current")
_EltexMsdpPeerConnectionAttempts_Type = Counter32
_EltexMsdpPeerConnectionAttempts_Object = MibTableColumn
eltexMsdpPeerConnectionAttempts = _EltexMsdpPeerConnectionAttempts_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 10, 1, 30),
    _EltexMsdpPeerConnectionAttempts_Type()
)
eltexMsdpPeerConnectionAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexMsdpPeerConnectionAttempts.setStatus("current")
_EltexMsdpPeerEnabled_Type = TruthValue
_EltexMsdpPeerEnabled_Object = MibTableColumn
eltexMsdpPeerEnabled = _EltexMsdpPeerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 10, 1, 100),
    _EltexMsdpPeerEnabled_Type()
)
eltexMsdpPeerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexMsdpPeerEnabled.setStatus("current")


class _EltexMsdpPeerDescription_Type(DisplayString):
    """Custom type eltexMsdpPeerDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_EltexMsdpPeerDescription_Type.__name__ = "DisplayString"
_EltexMsdpPeerDescription_Object = MibTableColumn
eltexMsdpPeerDescription = _EltexMsdpPeerDescription_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 10, 1, 101),
    _EltexMsdpPeerDescription_Type()
)
eltexMsdpPeerDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexMsdpPeerDescription.setStatus("current")
_EltexMsdpPeerFsmLastChangeTime_Type = TimeStamp
_EltexMsdpPeerFsmLastChangeTime_Object = MibTableColumn
eltexMsdpPeerFsmLastChangeTime = _EltexMsdpPeerFsmLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 10, 1, 102),
    _EltexMsdpPeerFsmLastChangeTime_Type()
)
eltexMsdpPeerFsmLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexMsdpPeerFsmLastChangeTime.setStatus("current")
_EltexMsdpPeerNumSACacheEntries_Type = Gauge32
_EltexMsdpPeerNumSACacheEntries_Object = MibTableColumn
eltexMsdpPeerNumSACacheEntries = _EltexMsdpPeerNumSACacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 10, 1, 103),
    _EltexMsdpPeerNumSACacheEntries_Type()
)
eltexMsdpPeerNumSACacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexMsdpPeerNumSACacheEntries.setStatus("current")
_EltexMsdpRPAddress_Type = IpAddress
_EltexMsdpRPAddress_Object = MibScalar
eltexMsdpRPAddress = _EltexMsdpRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 11),
    _EltexMsdpRPAddress_Type()
)
eltexMsdpRPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexMsdpRPAddress.setStatus("current")
_EltexMsdpMeshGroupTable_Object = MibTable
eltexMsdpMeshGroupTable = _EltexMsdpMeshGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 12)
)
if mibBuilder.loadTexts:
    eltexMsdpMeshGroupTable.setStatus("current")
_EltexMsdpMeshGroupEntry_Object = MibTableRow
eltexMsdpMeshGroupEntry = _EltexMsdpMeshGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 12, 1)
)
eltexMsdpMeshGroupEntry.setIndexNames(
    (0, "ELTEX-MSDP-MIB", "eltexMsdpMeshGroupName"),
    (0, "ELTEX-MSDP-MIB", "eltexMsdpMeshGroupPeerAddress"),
)
if mibBuilder.loadTexts:
    eltexMsdpMeshGroupEntry.setStatus("current")


class _EltexMsdpMeshGroupName_Type(DisplayString):
    """Custom type eltexMsdpMeshGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_EltexMsdpMeshGroupName_Type.__name__ = "DisplayString"
_EltexMsdpMeshGroupName_Object = MibTableColumn
eltexMsdpMeshGroupName = _EltexMsdpMeshGroupName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 12, 1, 1),
    _EltexMsdpMeshGroupName_Type()
)
eltexMsdpMeshGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexMsdpMeshGroupName.setStatus("current")
_EltexMsdpMeshGroupPeerAddress_Type = IpAddress
_EltexMsdpMeshGroupPeerAddress_Object = MibTableColumn
eltexMsdpMeshGroupPeerAddress = _EltexMsdpMeshGroupPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 12, 1, 2),
    _EltexMsdpMeshGroupPeerAddress_Type()
)
eltexMsdpMeshGroupPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexMsdpMeshGroupPeerAddress.setStatus("current")
_EltexMsdpMeshGroupRowStatus_Type = RowStatus
_EltexMsdpMeshGroupRowStatus_Object = MibTableColumn
eltexMsdpMeshGroupRowStatus = _EltexMsdpMeshGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 12, 1, 3),
    _EltexMsdpMeshGroupRowStatus_Type()
)
eltexMsdpMeshGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexMsdpMeshGroupRowStatus.setStatus("current")


class _EltexMsdpHoldTime_Type(Integer32):
    """Custom type eltexMsdpHoldTime based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 150),
    )


_EltexMsdpHoldTime_Type.__name__ = "Integer32"
_EltexMsdpHoldTime_Object = MibScalar
eltexMsdpHoldTime = _EltexMsdpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 100),
    _EltexMsdpHoldTime_Type()
)
eltexMsdpHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexMsdpHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    eltexMsdpHoldTime.setUnits("seconds")


class _EltexMsdpKeepAlive_Type(Integer32):
    """Custom type eltexMsdpKeepAlive based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_EltexMsdpKeepAlive_Type.__name__ = "Integer32"
_EltexMsdpKeepAlive_Object = MibScalar
eltexMsdpKeepAlive = _EltexMsdpKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 101),
    _EltexMsdpKeepAlive_Type()
)
eltexMsdpKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexMsdpKeepAlive.setStatus("current")
if mibBuilder.loadTexts:
    eltexMsdpKeepAlive.setUnits("seconds")
_EltexMsdpLocalAddress_Type = IpAddress
_EltexMsdpLocalAddress_Object = MibScalar
eltexMsdpLocalAddress = _EltexMsdpLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 102),
    _EltexMsdpLocalAddress_Type()
)
eltexMsdpLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexMsdpLocalAddress.setStatus("current")
_EltexMsdpPeerCountersClear_Type = IpAddress
_EltexMsdpPeerCountersClear_Object = MibScalar
eltexMsdpPeerCountersClear = _EltexMsdpPeerCountersClear_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 103),
    _EltexMsdpPeerCountersClear_Type()
)
eltexMsdpPeerCountersClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexMsdpPeerCountersClear.setStatus("current")
_EltexMsdpSAFilterTable_Object = MibTable
eltexMsdpSAFilterTable = _EltexMsdpSAFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 104)
)
if mibBuilder.loadTexts:
    eltexMsdpSAFilterTable.setStatus("current")
_EltexMsdpSAFilterEntry_Object = MibTableRow
eltexMsdpSAFilterEntry = _EltexMsdpSAFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 104, 1)
)
eltexMsdpSAFilterEntry.setIndexNames(
    (0, "ELTEX-MSDP-MIB", "eltexMsdpSAFilterPeerRemoteAddress"),
    (0, "ELTEX-MSDP-MIB", "eltexMsdpSAFilterDirection"),
    (0, "ELTEX-MSDP-MIB", "eltexMsdpSAFilterIndex"),
)
if mibBuilder.loadTexts:
    eltexMsdpSAFilterEntry.setStatus("current")
_EltexMsdpSAFilterPeerRemoteAddress_Type = IpAddress
_EltexMsdpSAFilterPeerRemoteAddress_Object = MibTableColumn
eltexMsdpSAFilterPeerRemoteAddress = _EltexMsdpSAFilterPeerRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 104, 1, 1),
    _EltexMsdpSAFilterPeerRemoteAddress_Type()
)
eltexMsdpSAFilterPeerRemoteAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexMsdpSAFilterPeerRemoteAddress.setStatus("current")
_EltexMsdpSAFilterDirection_Type = EltexMsdpSAFilterDirection
_EltexMsdpSAFilterDirection_Object = MibTableColumn
eltexMsdpSAFilterDirection = _EltexMsdpSAFilterDirection_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 104, 1, 2),
    _EltexMsdpSAFilterDirection_Type()
)
eltexMsdpSAFilterDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexMsdpSAFilterDirection.setStatus("current")


class _EltexMsdpSAFilterIndex_Type(Unsigned32):
    """Custom type eltexMsdpSAFilterIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967294),
    )


_EltexMsdpSAFilterIndex_Type.__name__ = "Unsigned32"
_EltexMsdpSAFilterIndex_Object = MibTableColumn
eltexMsdpSAFilterIndex = _EltexMsdpSAFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 104, 1, 3),
    _EltexMsdpSAFilterIndex_Type()
)
eltexMsdpSAFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexMsdpSAFilterIndex.setStatus("current")
_EltexMsdpSAFilterAction_Type = EltexMsdpSAFilterAction
_EltexMsdpSAFilterAction_Object = MibTableColumn
eltexMsdpSAFilterAction = _EltexMsdpSAFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 104, 1, 4),
    _EltexMsdpSAFilterAction_Type()
)
eltexMsdpSAFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexMsdpSAFilterAction.setStatus("current")
_EltexMsdpSAFilterGroupAddr_Type = IpAddress
_EltexMsdpSAFilterGroupAddr_Object = MibTableColumn
eltexMsdpSAFilterGroupAddr = _EltexMsdpSAFilterGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 104, 1, 5),
    _EltexMsdpSAFilterGroupAddr_Type()
)
eltexMsdpSAFilterGroupAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexMsdpSAFilterGroupAddr.setStatus("current")
_EltexMsdpSAFilterGroupAddrPrefixLen_Type = Integer32
_EltexMsdpSAFilterGroupAddrPrefixLen_Object = MibTableColumn
eltexMsdpSAFilterGroupAddrPrefixLen = _EltexMsdpSAFilterGroupAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 104, 1, 6),
    _EltexMsdpSAFilterGroupAddrPrefixLen_Type()
)
eltexMsdpSAFilterGroupAddrPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexMsdpSAFilterGroupAddrPrefixLen.setStatus("current")
_EltexMsdpSAFilterSourceAddr_Type = IpAddress
_EltexMsdpSAFilterSourceAddr_Object = MibTableColumn
eltexMsdpSAFilterSourceAddr = _EltexMsdpSAFilterSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 104, 1, 7),
    _EltexMsdpSAFilterSourceAddr_Type()
)
eltexMsdpSAFilterSourceAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexMsdpSAFilterSourceAddr.setStatus("current")
_EltexMsdpSAFilterSourceAddrPrefixLen_Type = Integer32
_EltexMsdpSAFilterSourceAddrPrefixLen_Object = MibTableColumn
eltexMsdpSAFilterSourceAddrPrefixLen = _EltexMsdpSAFilterSourceAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 104, 1, 8),
    _EltexMsdpSAFilterSourceAddrPrefixLen_Type()
)
eltexMsdpSAFilterSourceAddrPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexMsdpSAFilterSourceAddrPrefixLen.setStatus("current")
_EltexMsdpSAFilterOriginRP_Type = IpAddress
_EltexMsdpSAFilterOriginRP_Object = MibTableColumn
eltexMsdpSAFilterOriginRP = _EltexMsdpSAFilterOriginRP_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 104, 1, 9),
    _EltexMsdpSAFilterOriginRP_Type()
)
eltexMsdpSAFilterOriginRP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexMsdpSAFilterOriginRP.setStatus("current")
_EltexMsdpSAFilterOriginRPPrefixLen_Type = Integer32
_EltexMsdpSAFilterOriginRPPrefixLen_Object = MibTableColumn
eltexMsdpSAFilterOriginRPPrefixLen = _EltexMsdpSAFilterOriginRPPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 104, 1, 10),
    _EltexMsdpSAFilterOriginRPPrefixLen_Type()
)
eltexMsdpSAFilterOriginRPPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexMsdpSAFilterOriginRPPrefixLen.setStatus("current")
_EltexMsdpSAFilterRowStatus_Type = RowStatus
_EltexMsdpSAFilterRowStatus_Object = MibTableColumn
eltexMsdpSAFilterRowStatus = _EltexMsdpSAFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 51, 1, 1, 104, 1, 11),
    _EltexMsdpSAFilterRowStatus_Type()
)
eltexMsdpSAFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexMsdpSAFilterRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MSDP-MIB",
    **{"EltexMsdpSAFilterDirection": EltexMsdpSAFilterDirection,
       "EltexMsdpSAFilterAction": EltexMsdpSAFilterAction,
       "eltexMsdpMIB": eltexMsdpMIB,
       "eltexMsdpObjects": eltexMsdpObjects,
       "eltexMsdp": eltexMsdp,
       "eltexMsdpTraps": eltexMsdpTraps,
       "eltexMsdpCacheLifetime": eltexMsdpCacheLifetime,
       "eltexMsdpSACacheTable": eltexMsdpSACacheTable,
       "eltexMsdpSACacheEntry": eltexMsdpSACacheEntry,
       "eltexMsdpSACacheGroupAddr": eltexMsdpSACacheGroupAddr,
       "eltexMsdpSACacheSourceAddr": eltexMsdpSACacheSourceAddr,
       "eltexMsdpSACacheOriginRP": eltexMsdpSACacheOriginRP,
       "eltexMsdpSACachePeerLearnedFrom": eltexMsdpSACachePeerLearnedFrom,
       "eltexMsdpSACacheUpTime": eltexMsdpSACacheUpTime,
       "eltexMsdpPeerTable": eltexMsdpPeerTable,
       "eltexMsdpPeerEntry": eltexMsdpPeerEntry,
       "eltexMsdpPeerRemoteAddress": eltexMsdpPeerRemoteAddress,
       "eltexMsdpPeerState": eltexMsdpPeerState,
       "eltexMsdpPeerRPFFailures": eltexMsdpPeerRPFFailures,
       "eltexMsdpPeerInSAs": eltexMsdpPeerInSAs,
       "eltexMsdpPeerOutSAs": eltexMsdpPeerOutSAs,
       "eltexMsdpPeerInSARequests": eltexMsdpPeerInSARequests,
       "eltexMsdpPeerOutSARequests": eltexMsdpPeerOutSARequests,
       "eltexMsdpPeerInSAResponses": eltexMsdpPeerInSAResponses,
       "eltexMsdpPeerOutSAResponses": eltexMsdpPeerOutSAResponses,
       "eltexMsdpPeerInControlMessages": eltexMsdpPeerInControlMessages,
       "eltexMsdpPeerOutControlMessages": eltexMsdpPeerOutControlMessages,
       "eltexMsdpPeerFsmEstablishedTime": eltexMsdpPeerFsmEstablishedTime,
       "eltexMsdpPeerInMessageTime": eltexMsdpPeerInMessageTime,
       "eltexMsdpPeerLocalAddress": eltexMsdpPeerLocalAddress,
       "eltexMsdpPeerRowStatus": eltexMsdpPeerRowStatus,
       "eltexMsdpPeerConnectionAttempts": eltexMsdpPeerConnectionAttempts,
       "eltexMsdpPeerEnabled": eltexMsdpPeerEnabled,
       "eltexMsdpPeerDescription": eltexMsdpPeerDescription,
       "eltexMsdpPeerFsmLastChangeTime": eltexMsdpPeerFsmLastChangeTime,
       "eltexMsdpPeerNumSACacheEntries": eltexMsdpPeerNumSACacheEntries,
       "eltexMsdpRPAddress": eltexMsdpRPAddress,
       "eltexMsdpMeshGroupTable": eltexMsdpMeshGroupTable,
       "eltexMsdpMeshGroupEntry": eltexMsdpMeshGroupEntry,
       "eltexMsdpMeshGroupName": eltexMsdpMeshGroupName,
       "eltexMsdpMeshGroupPeerAddress": eltexMsdpMeshGroupPeerAddress,
       "eltexMsdpMeshGroupRowStatus": eltexMsdpMeshGroupRowStatus,
       "eltexMsdpHoldTime": eltexMsdpHoldTime,
       "eltexMsdpKeepAlive": eltexMsdpKeepAlive,
       "eltexMsdpLocalAddress": eltexMsdpLocalAddress,
       "eltexMsdpPeerCountersClear": eltexMsdpPeerCountersClear,
       "eltexMsdpSAFilterTable": eltexMsdpSAFilterTable,
       "eltexMsdpSAFilterEntry": eltexMsdpSAFilterEntry,
       "eltexMsdpSAFilterPeerRemoteAddress": eltexMsdpSAFilterPeerRemoteAddress,
       "eltexMsdpSAFilterDirection": eltexMsdpSAFilterDirection,
       "eltexMsdpSAFilterIndex": eltexMsdpSAFilterIndex,
       "eltexMsdpSAFilterAction": eltexMsdpSAFilterAction,
       "eltexMsdpSAFilterGroupAddr": eltexMsdpSAFilterGroupAddr,
       "eltexMsdpSAFilterGroupAddrPrefixLen": eltexMsdpSAFilterGroupAddrPrefixLen,
       "eltexMsdpSAFilterSourceAddr": eltexMsdpSAFilterSourceAddr,
       "eltexMsdpSAFilterSourceAddrPrefixLen": eltexMsdpSAFilterSourceAddrPrefixLen,
       "eltexMsdpSAFilterOriginRP": eltexMsdpSAFilterOriginRP,
       "eltexMsdpSAFilterOriginRPPrefixLen": eltexMsdpSAFilterOriginRPPrefixLen,
       "eltexMsdpSAFilterRowStatus": eltexMsdpSAFilterRowStatus}
)
