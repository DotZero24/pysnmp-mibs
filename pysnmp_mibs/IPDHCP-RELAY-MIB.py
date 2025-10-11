# SNMP MIB module (IPDHCP-RELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/IPDHCP-RELAY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:35:53 2025
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

(iscomSwitch,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "iscomSwitch")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(EnableVar,) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar")


# MODULE-IDENTITY

rcIpDhcpRelay = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 30)
)
if mibBuilder.loadTexts:
    rcIpDhcpRelay.setRevisions(
        ("2007-10-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcIpDhcpRelayConfig_ObjectIdentity = ObjectIdentity
rcIpDhcpRelayConfig = _RcIpDhcpRelayConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 30, 1)
)


class _RcIpDhcpRelayEnable_Type(EnableVar):
    """Custom type rcIpDhcpRelayEnable based on EnableVar"""
    defaultValue = 2


_RcIpDhcpRelayEnable_Type.__name__ = "EnableVar"
_RcIpDhcpRelayEnable_Object = MibScalar
rcIpDhcpRelayEnable = _RcIpDhcpRelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 30, 1, 1),
    _RcIpDhcpRelayEnable_Type()
)
rcIpDhcpRelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIpDhcpRelayEnable.setStatus("current")
_RcIpDhcpRelayStartTime_Type = TimeTicks
_RcIpDhcpRelayStartTime_Object = MibScalar
rcIpDhcpRelayStartTime = _RcIpDhcpRelayStartTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 30, 1, 2),
    _RcIpDhcpRelayStartTime_Type()
)
rcIpDhcpRelayStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpRelayStartTime.setStatus("mandatory")
_RcIpDhcpRelayIpInterfaceTable_Object = MibTable
rcIpDhcpRelayIpInterfaceTable = _RcIpDhcpRelayIpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 30, 1, 3)
)
if mibBuilder.loadTexts:
    rcIpDhcpRelayIpInterfaceTable.setStatus("current")
_RcIpDhcpRelayIpInterfaceEntry_Object = MibTableRow
rcIpDhcpRelayIpInterfaceEntry = _RcIpDhcpRelayIpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 30, 1, 3, 1)
)
rcIpDhcpRelayIpInterfaceEntry.setIndexNames(
    (0, "IPDHCP-RELAY-MIB", "rcIpDhcpRelayIpInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    rcIpDhcpRelayIpInterfaceEntry.setStatus("current")
_RcIpDhcpRelayIpInterfaceIfIndex_Type = Integer32
_RcIpDhcpRelayIpInterfaceIfIndex_Object = MibTableColumn
rcIpDhcpRelayIpInterfaceIfIndex = _RcIpDhcpRelayIpInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 30, 1, 3, 1, 1),
    _RcIpDhcpRelayIpInterfaceIfIndex_Type()
)
rcIpDhcpRelayIpInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcIpDhcpRelayIpInterfaceIfIndex.setStatus("current")
_RcIpDhcpRelayIpInterfaceEnable_Type = EnableVar
_RcIpDhcpRelayIpInterfaceEnable_Object = MibTableColumn
rcIpDhcpRelayIpInterfaceEnable = _RcIpDhcpRelayIpInterfaceEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 30, 1, 3, 1, 2),
    _RcIpDhcpRelayIpInterfaceEnable_Type()
)
rcIpDhcpRelayIpInterfaceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIpDhcpRelayIpInterfaceEnable.setStatus("current")
_RcIpDhcpRelayTargetTable_Object = MibTable
rcIpDhcpRelayTargetTable = _RcIpDhcpRelayTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 30, 1, 4)
)
if mibBuilder.loadTexts:
    rcIpDhcpRelayTargetTable.setStatus("current")
_RcIpDhcpRelayTargetEntry_Object = MibTableRow
rcIpDhcpRelayTargetEntry = _RcIpDhcpRelayTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 30, 1, 4, 1)
)
rcIpDhcpRelayTargetEntry.setIndexNames(
    (0, "IPDHCP-RELAY-MIB", "rcIpDhcpRelayTargetIfIndex"),
    (0, "IPDHCP-RELAY-MIB", "rcIpDhcpRelayTargetAddress"),
)
if mibBuilder.loadTexts:
    rcIpDhcpRelayTargetEntry.setStatus("current")
_RcIpDhcpRelayTargetIfIndex_Type = Integer32
_RcIpDhcpRelayTargetIfIndex_Object = MibTableColumn
rcIpDhcpRelayTargetIfIndex = _RcIpDhcpRelayTargetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 30, 1, 4, 1, 1),
    _RcIpDhcpRelayTargetIfIndex_Type()
)
rcIpDhcpRelayTargetIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcIpDhcpRelayTargetIfIndex.setStatus("current")
_RcIpDhcpRelayTargetAddress_Type = IpAddress
_RcIpDhcpRelayTargetAddress_Object = MibTableColumn
rcIpDhcpRelayTargetAddress = _RcIpDhcpRelayTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 30, 1, 4, 1, 2),
    _RcIpDhcpRelayTargetAddress_Type()
)
rcIpDhcpRelayTargetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcIpDhcpRelayTargetAddress.setStatus("current")
_RcIpDhcpRelayTargetRowStatus_Type = RowStatus
_RcIpDhcpRelayTargetRowStatus_Object = MibTableColumn
rcIpDhcpRelayTargetRowStatus = _RcIpDhcpRelayTargetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 30, 1, 4, 1, 3),
    _RcIpDhcpRelayTargetRowStatus_Type()
)
rcIpDhcpRelayTargetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcIpDhcpRelayTargetRowStatus.setStatus("current")
_RcIpDhcpRelayInformationOptionGroup_ObjectIdentity = ObjectIdentity
rcIpDhcpRelayInformationOptionGroup = _RcIpDhcpRelayInformationOptionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 30, 2)
)


class _RcIpDhcpRelayInformationOption_Type(EnableVar):
    """Custom type rcIpDhcpRelayInformationOption based on EnableVar"""
    defaultValue = 2


_RcIpDhcpRelayInformationOption_Type.__name__ = "EnableVar"
_RcIpDhcpRelayInformationOption_Object = MibScalar
rcIpDhcpRelayInformationOption = _RcIpDhcpRelayInformationOption_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 30, 2, 1),
    _RcIpDhcpRelayInformationOption_Type()
)
rcIpDhcpRelayInformationOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIpDhcpRelayInformationOption.setStatus("current")


class _RcIpDhcpRelayInformationPolicy_Type(Integer32):
    """Custom type rcIpDhcpRelayInformationPolicy based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("keep", 2),
          ("replace", 3))
    )


_RcIpDhcpRelayInformationPolicy_Type.__name__ = "Integer32"
_RcIpDhcpRelayInformationPolicy_Object = MibScalar
rcIpDhcpRelayInformationPolicy = _RcIpDhcpRelayInformationPolicy_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 30, 2, 2),
    _RcIpDhcpRelayInformationPolicy_Type()
)
rcIpDhcpRelayInformationPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIpDhcpRelayInformationPolicy.setStatus("current")
_RcIpDhcpRelayInformationOptionTrustTable_Object = MibTable
rcIpDhcpRelayInformationOptionTrustTable = _RcIpDhcpRelayInformationOptionTrustTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 30, 2, 3)
)
if mibBuilder.loadTexts:
    rcIpDhcpRelayInformationOptionTrustTable.setStatus("current")
_RcIpDhcpRelayInformationOptionTrustEntry_Object = MibTableRow
rcIpDhcpRelayInformationOptionTrustEntry = _RcIpDhcpRelayInformationOptionTrustEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 30, 2, 3, 1)
)
rcIpDhcpRelayInformationOptionTrustEntry.setIndexNames(
    (0, "IPDHCP-RELAY-MIB", "rcIpDhcpRelayInformationOptionTrustPortIfIndex"),
)
if mibBuilder.loadTexts:
    rcIpDhcpRelayInformationOptionTrustEntry.setStatus("current")
_RcIpDhcpRelayInformationOptionTrustPortIfIndex_Type = Integer32
_RcIpDhcpRelayInformationOptionTrustPortIfIndex_Object = MibTableColumn
rcIpDhcpRelayInformationOptionTrustPortIfIndex = _RcIpDhcpRelayInformationOptionTrustPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 30, 2, 3, 1, 1),
    _RcIpDhcpRelayInformationOptionTrustPortIfIndex_Type()
)
rcIpDhcpRelayInformationOptionTrustPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcIpDhcpRelayInformationOptionTrustPortIfIndex.setStatus("current")


class _RcIpDhcpRelayInformationOptionTrustState_Type(Integer32):
    """Custom type rcIpDhcpRelayInformationOptionTrustState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trusted", 1),
          ("untrusted", 2))
    )


_RcIpDhcpRelayInformationOptionTrustState_Type.__name__ = "Integer32"
_RcIpDhcpRelayInformationOptionTrustState_Object = MibTableColumn
rcIpDhcpRelayInformationOptionTrustState = _RcIpDhcpRelayInformationOptionTrustState_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 30, 2, 3, 1, 2),
    _RcIpDhcpRelayInformationOptionTrustState_Type()
)
rcIpDhcpRelayInformationOptionTrustState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIpDhcpRelayInformationOptionTrustState.setStatus("current")
_RcIpDhcpRelayStatistics_ObjectIdentity = ObjectIdentity
rcIpDhcpRelayStatistics = _RcIpDhcpRelayStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 30, 3)
)
_RcIpDhcpRelayStatsBootpsRcv_Type = Counter32
_RcIpDhcpRelayStatsBootpsRcv_Object = MibScalar
rcIpDhcpRelayStatsBootpsRcv = _RcIpDhcpRelayStatsBootpsRcv_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 30, 3, 1),
    _RcIpDhcpRelayStatsBootpsRcv_Type()
)
rcIpDhcpRelayStatsBootpsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpRelayStatsBootpsRcv.setStatus("mandatory")
_RcIpDhcpRelayStatsBootpsSnd_Type = Counter32
_RcIpDhcpRelayStatsBootpsSnd_Object = MibScalar
rcIpDhcpRelayStatsBootpsSnd = _RcIpDhcpRelayStatsBootpsSnd_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 30, 3, 2),
    _RcIpDhcpRelayStatsBootpsSnd_Type()
)
rcIpDhcpRelayStatsBootpsSnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpRelayStatsBootpsSnd.setStatus("mandatory")
_RcIpDhcpRelayStatsDiscoversRcv_Type = Counter32
_RcIpDhcpRelayStatsDiscoversRcv_Object = MibScalar
rcIpDhcpRelayStatsDiscoversRcv = _RcIpDhcpRelayStatsDiscoversRcv_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 30, 3, 3),
    _RcIpDhcpRelayStatsDiscoversRcv_Type()
)
rcIpDhcpRelayStatsDiscoversRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpRelayStatsDiscoversRcv.setStatus("mandatory")
_RcIpDhcpRelayStatsDiscoversSnd_Type = Counter32
_RcIpDhcpRelayStatsDiscoversSnd_Object = MibScalar
rcIpDhcpRelayStatsDiscoversSnd = _RcIpDhcpRelayStatsDiscoversSnd_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 30, 3, 4),
    _RcIpDhcpRelayStatsDiscoversSnd_Type()
)
rcIpDhcpRelayStatsDiscoversSnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpRelayStatsDiscoversSnd.setStatus("mandatory")
_RcIpDhcpRelayStatsRequestsRcv_Type = Counter32
_RcIpDhcpRelayStatsRequestsRcv_Object = MibScalar
rcIpDhcpRelayStatsRequestsRcv = _RcIpDhcpRelayStatsRequestsRcv_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 30, 3, 5),
    _RcIpDhcpRelayStatsRequestsRcv_Type()
)
rcIpDhcpRelayStatsRequestsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpRelayStatsRequestsRcv.setStatus("mandatory")
_RcIpDhcpRelayStatsRequestsSnd_Type = Counter32
_RcIpDhcpRelayStatsRequestsSnd_Object = MibScalar
rcIpDhcpRelayStatsRequestsSnd = _RcIpDhcpRelayStatsRequestsSnd_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 30, 3, 6),
    _RcIpDhcpRelayStatsRequestsSnd_Type()
)
rcIpDhcpRelayStatsRequestsSnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpRelayStatsRequestsSnd.setStatus("mandatory")
_RcIpDhcpRelayStatsReleasesRcv_Type = Counter32
_RcIpDhcpRelayStatsReleasesRcv_Object = MibScalar
rcIpDhcpRelayStatsReleasesRcv = _RcIpDhcpRelayStatsReleasesRcv_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 30, 3, 7),
    _RcIpDhcpRelayStatsReleasesRcv_Type()
)
rcIpDhcpRelayStatsReleasesRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpRelayStatsReleasesRcv.setStatus("mandatory")
_RcIpDhcpRelayStatsReleasesSnd_Type = Counter32
_RcIpDhcpRelayStatsReleasesSnd_Object = MibScalar
rcIpDhcpRelayStatsReleasesSnd = _RcIpDhcpRelayStatsReleasesSnd_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 30, 3, 8),
    _RcIpDhcpRelayStatsReleasesSnd_Type()
)
rcIpDhcpRelayStatsReleasesSnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpRelayStatsReleasesSnd.setStatus("mandatory")
_RcIpDhcpRelayStatsOffersRcv_Type = Counter32
_RcIpDhcpRelayStatsOffersRcv_Object = MibScalar
rcIpDhcpRelayStatsOffersRcv = _RcIpDhcpRelayStatsOffersRcv_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 30, 3, 9),
    _RcIpDhcpRelayStatsOffersRcv_Type()
)
rcIpDhcpRelayStatsOffersRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpRelayStatsOffersRcv.setStatus("mandatory")
_RcIpDhcpRelayStatsOffersSnd_Type = Counter32
_RcIpDhcpRelayStatsOffersSnd_Object = MibScalar
rcIpDhcpRelayStatsOffersSnd = _RcIpDhcpRelayStatsOffersSnd_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 30, 3, 10),
    _RcIpDhcpRelayStatsOffersSnd_Type()
)
rcIpDhcpRelayStatsOffersSnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpRelayStatsOffersSnd.setStatus("mandatory")
_RcIpDhcpRelayStatsAcksRcv_Type = Counter32
_RcIpDhcpRelayStatsAcksRcv_Object = MibScalar
rcIpDhcpRelayStatsAcksRcv = _RcIpDhcpRelayStatsAcksRcv_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 30, 3, 11),
    _RcIpDhcpRelayStatsAcksRcv_Type()
)
rcIpDhcpRelayStatsAcksRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpRelayStatsAcksRcv.setStatus("mandatory")
_RcIpDhcpRelayStatsAcksSnd_Type = Counter32
_RcIpDhcpRelayStatsAcksSnd_Object = MibScalar
rcIpDhcpRelayStatsAcksSnd = _RcIpDhcpRelayStatsAcksSnd_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 30, 3, 12),
    _RcIpDhcpRelayStatsAcksSnd_Type()
)
rcIpDhcpRelayStatsAcksSnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpRelayStatsAcksSnd.setStatus("mandatory")
_RcIpDhcpRelayStatsNacksRcv_Type = Counter32
_RcIpDhcpRelayStatsNacksRcv_Object = MibScalar
rcIpDhcpRelayStatsNacksRcv = _RcIpDhcpRelayStatsNacksRcv_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 30, 3, 13),
    _RcIpDhcpRelayStatsNacksRcv_Type()
)
rcIpDhcpRelayStatsNacksRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpRelayStatsNacksRcv.setStatus("mandatory")
_RcIpDhcpRelayStatsNacksSnd_Type = Counter32
_RcIpDhcpRelayStatsNacksSnd_Object = MibScalar
rcIpDhcpRelayStatsNacksSnd = _RcIpDhcpRelayStatsNacksSnd_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 30, 3, 14),
    _RcIpDhcpRelayStatsNacksSnd_Type()
)
rcIpDhcpRelayStatsNacksSnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpRelayStatsNacksSnd.setStatus("mandatory")
_RcIpDhcpRelayStatsDeclinesRcv_Type = Counter32
_RcIpDhcpRelayStatsDeclinesRcv_Object = MibScalar
rcIpDhcpRelayStatsDeclinesRcv = _RcIpDhcpRelayStatsDeclinesRcv_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 30, 3, 15),
    _RcIpDhcpRelayStatsDeclinesRcv_Type()
)
rcIpDhcpRelayStatsDeclinesRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpRelayStatsDeclinesRcv.setStatus("mandatory")
_RcIpDhcpRelayStatsDeclinesSnd_Type = Counter32
_RcIpDhcpRelayStatsDeclinesSnd_Object = MibScalar
rcIpDhcpRelayStatsDeclinesSnd = _RcIpDhcpRelayStatsDeclinesSnd_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 30, 3, 16),
    _RcIpDhcpRelayStatsDeclinesSnd_Type()
)
rcIpDhcpRelayStatsDeclinesSnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpRelayStatsDeclinesSnd.setStatus("mandatory")
_RcIpDhcpRelayStatsInformationsRcv_Type = Counter32
_RcIpDhcpRelayStatsInformationsRcv_Object = MibScalar
rcIpDhcpRelayStatsInformationsRcv = _RcIpDhcpRelayStatsInformationsRcv_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 30, 3, 17),
    _RcIpDhcpRelayStatsInformationsRcv_Type()
)
rcIpDhcpRelayStatsInformationsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpRelayStatsInformationsRcv.setStatus("mandatory")
_RcIpDhcpRelayStatsInformationsSnd_Type = Counter32
_RcIpDhcpRelayStatsInformationsSnd_Object = MibScalar
rcIpDhcpRelayStatsInformationsSnd = _RcIpDhcpRelayStatsInformationsSnd_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 30, 3, 18),
    _RcIpDhcpRelayStatsInformationsSnd_Type()
)
rcIpDhcpRelayStatsInformationsSnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpRelayStatsInformationsSnd.setStatus("mandatory")
_RcIpDhcpRelayStatsUnknowns_Type = Counter32
_RcIpDhcpRelayStatsUnknowns_Object = MibScalar
rcIpDhcpRelayStatsUnknowns = _RcIpDhcpRelayStatsUnknowns_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 30, 3, 19),
    _RcIpDhcpRelayStatsUnknowns_Type()
)
rcIpDhcpRelayStatsUnknowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpRelayStatsUnknowns.setStatus("mandatory")
_RcIpDhcpRelayStatsPacketsRcv_Type = Counter32
_RcIpDhcpRelayStatsPacketsRcv_Object = MibScalar
rcIpDhcpRelayStatsPacketsRcv = _RcIpDhcpRelayStatsPacketsRcv_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 30, 3, 20),
    _RcIpDhcpRelayStatsPacketsRcv_Type()
)
rcIpDhcpRelayStatsPacketsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpRelayStatsPacketsRcv.setStatus("mandatory")
_RcIpDhcpRelayStatsPacketsSnd_Type = Counter32
_RcIpDhcpRelayStatsPacketsSnd_Object = MibScalar
rcIpDhcpRelayStatsPacketsSnd = _RcIpDhcpRelayStatsPacketsSnd_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 30, 3, 21),
    _RcIpDhcpRelayStatsPacketsSnd_Type()
)
rcIpDhcpRelayStatsPacketsSnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpRelayStatsPacketsSnd.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPDHCP-RELAY-MIB",
    **{"rcIpDhcpRelay": rcIpDhcpRelay,
       "rcIpDhcpRelayConfig": rcIpDhcpRelayConfig,
       "rcIpDhcpRelayEnable": rcIpDhcpRelayEnable,
       "rcIpDhcpRelayStartTime": rcIpDhcpRelayStartTime,
       "rcIpDhcpRelayIpInterfaceTable": rcIpDhcpRelayIpInterfaceTable,
       "rcIpDhcpRelayIpInterfaceEntry": rcIpDhcpRelayIpInterfaceEntry,
       "rcIpDhcpRelayIpInterfaceIfIndex": rcIpDhcpRelayIpInterfaceIfIndex,
       "rcIpDhcpRelayIpInterfaceEnable": rcIpDhcpRelayIpInterfaceEnable,
       "rcIpDhcpRelayTargetTable": rcIpDhcpRelayTargetTable,
       "rcIpDhcpRelayTargetEntry": rcIpDhcpRelayTargetEntry,
       "rcIpDhcpRelayTargetIfIndex": rcIpDhcpRelayTargetIfIndex,
       "rcIpDhcpRelayTargetAddress": rcIpDhcpRelayTargetAddress,
       "rcIpDhcpRelayTargetRowStatus": rcIpDhcpRelayTargetRowStatus,
       "rcIpDhcpRelayInformationOptionGroup": rcIpDhcpRelayInformationOptionGroup,
       "rcIpDhcpRelayInformationOption": rcIpDhcpRelayInformationOption,
       "rcIpDhcpRelayInformationPolicy": rcIpDhcpRelayInformationPolicy,
       "rcIpDhcpRelayInformationOptionTrustTable": rcIpDhcpRelayInformationOptionTrustTable,
       "rcIpDhcpRelayInformationOptionTrustEntry": rcIpDhcpRelayInformationOptionTrustEntry,
       "rcIpDhcpRelayInformationOptionTrustPortIfIndex": rcIpDhcpRelayInformationOptionTrustPortIfIndex,
       "rcIpDhcpRelayInformationOptionTrustState": rcIpDhcpRelayInformationOptionTrustState,
       "rcIpDhcpRelayStatistics": rcIpDhcpRelayStatistics,
       "rcIpDhcpRelayStatsBootpsRcv": rcIpDhcpRelayStatsBootpsRcv,
       "rcIpDhcpRelayStatsBootpsSnd": rcIpDhcpRelayStatsBootpsSnd,
       "rcIpDhcpRelayStatsDiscoversRcv": rcIpDhcpRelayStatsDiscoversRcv,
       "rcIpDhcpRelayStatsDiscoversSnd": rcIpDhcpRelayStatsDiscoversSnd,
       "rcIpDhcpRelayStatsRequestsRcv": rcIpDhcpRelayStatsRequestsRcv,
       "rcIpDhcpRelayStatsRequestsSnd": rcIpDhcpRelayStatsRequestsSnd,
       "rcIpDhcpRelayStatsReleasesRcv": rcIpDhcpRelayStatsReleasesRcv,
       "rcIpDhcpRelayStatsReleasesSnd": rcIpDhcpRelayStatsReleasesSnd,
       "rcIpDhcpRelayStatsOffersRcv": rcIpDhcpRelayStatsOffersRcv,
       "rcIpDhcpRelayStatsOffersSnd": rcIpDhcpRelayStatsOffersSnd,
       "rcIpDhcpRelayStatsAcksRcv": rcIpDhcpRelayStatsAcksRcv,
       "rcIpDhcpRelayStatsAcksSnd": rcIpDhcpRelayStatsAcksSnd,
       "rcIpDhcpRelayStatsNacksRcv": rcIpDhcpRelayStatsNacksRcv,
       "rcIpDhcpRelayStatsNacksSnd": rcIpDhcpRelayStatsNacksSnd,
       "rcIpDhcpRelayStatsDeclinesRcv": rcIpDhcpRelayStatsDeclinesRcv,
       "rcIpDhcpRelayStatsDeclinesSnd": rcIpDhcpRelayStatsDeclinesSnd,
       "rcIpDhcpRelayStatsInformationsRcv": rcIpDhcpRelayStatsInformationsRcv,
       "rcIpDhcpRelayStatsInformationsSnd": rcIpDhcpRelayStatsInformationsSnd,
       "rcIpDhcpRelayStatsUnknowns": rcIpDhcpRelayStatsUnknowns,
       "rcIpDhcpRelayStatsPacketsRcv": rcIpDhcpRelayStatsPacketsRcv,
       "rcIpDhcpRelayStatsPacketsSnd": rcIpDhcpRelayStatsPacketsSnd}
)
