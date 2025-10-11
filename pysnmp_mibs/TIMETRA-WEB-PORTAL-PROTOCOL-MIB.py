# SNMP MIB module (TIMETRA-WEB-PORTAL-PROTOCOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TIMETRA-WEB-PORTAL-PROTOCOL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:49:47 2025
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

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(iesIfIndex,
 svcId) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "iesIfIndex",
    "svcId")

(tmnxSubIpoeIndex,) = mibBuilder.importSymbols(
    "TIMETRA-SUBSCRIBER-MGMT-MIB",
    "tmnxSubIpoeIndex")

(TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TmnxAdminState,
 TmnxEnabledDisabled,
 TmnxServId,
 TmnxVRtrIDOrZero) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TmnxAdminState",
    "TmnxEnabledDisabled",
    "TmnxServId",
    "TmnxVRtrIDOrZero")

(vRtrID,) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID")


# MODULE-IDENTITY

timetraWppMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 80)
)
if mibBuilder.loadTexts:
    timetraWppMIBModule.setRevisions(
        ("2017-01-01 00:00",
         "2014-01-01 00:00",
         "2012-02-28 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxWppStatsType(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("event", 1),
          ("droppedMsgType", 2),
          ("acceptedMsgType", 3),
          ("originalTransmittedMsgType", 4),
          ("retransmittedMsgType", 5),
          ("forwardedToPeerMsgType", 6),
          ("receivedFromPeerMsgType", 7))
    )



class TmnxWppUserName(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 253),
    )



# MIB Managed Objects in the order of their OIDs

_TmnxWppConformance_ObjectIdentity = ObjectIdentity
tmnxWppConformance = _TmnxWppConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 80)
)
_TmnxWppCompliances_ObjectIdentity = ObjectIdentity
tmnxWppCompliances = _TmnxWppCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 80, 1)
)
_TmnxWppGroups_ObjectIdentity = ObjectIdentity
tmnxWppGroups = _TmnxWppGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 80, 2)
)
_TmnxWpp_ObjectIdentity = ObjectIdentity
tmnxWpp = _TmnxWpp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80)
)
_TmnxWppObjs_ObjectIdentity = ObjectIdentity
tmnxWppObjs = _TmnxWppObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1)
)
_TmnxWppPortalObjs_ObjectIdentity = ObjectIdentity
tmnxWppPortalObjs = _TmnxWppPortalObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1)
)
_TmnxWppPortalTable_Object = MibTable
tmnxWppPortalTable = _TmnxWppPortalTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxWppPortalTable.setStatus("current")
_TmnxWppPortalEntry_Object = MibTableRow
tmnxWppPortalEntry = _TmnxWppPortalEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 1, 1)
)
tmnxWppPortalEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (1, "TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalName"),
)
if mibBuilder.loadTexts:
    tmnxWppPortalEntry.setStatus("current")
_TmnxWppPortalName_Type = TNamedItem
_TmnxWppPortalName_Object = MibTableColumn
tmnxWppPortalName = _TmnxWppPortalName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 1, 1, 1),
    _TmnxWppPortalName_Type()
)
tmnxWppPortalName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWppPortalName.setStatus("current")
_TmnxWppPortalLastCh_Type = TimeStamp
_TmnxWppPortalLastCh_Object = MibTableColumn
tmnxWppPortalLastCh = _TmnxWppPortalLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 1, 1, 2),
    _TmnxWppPortalLastCh_Type()
)
tmnxWppPortalLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppPortalLastCh.setStatus("current")
_TmnxWppPortalRowStatus_Type = RowStatus
_TmnxWppPortalRowStatus_Object = MibTableColumn
tmnxWppPortalRowStatus = _TmnxWppPortalRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 1, 1, 3),
    _TmnxWppPortalRowStatus_Type()
)
tmnxWppPortalRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWppPortalRowStatus.setStatus("current")
_TmnxWppPortalAddrType_Type = InetAddressType
_TmnxWppPortalAddrType_Object = MibTableColumn
tmnxWppPortalAddrType = _TmnxWppPortalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 1, 1, 4),
    _TmnxWppPortalAddrType_Type()
)
tmnxWppPortalAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWppPortalAddrType.setStatus("current")


class _TmnxWppPortalAddr_Type(InetAddress):
    """Custom type tmnxWppPortalAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWppPortalAddr_Type.__name__ = "InetAddress"
_TmnxWppPortalAddr_Object = MibTableColumn
tmnxWppPortalAddr = _TmnxWppPortalAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 1, 1, 5),
    _TmnxWppPortalAddr_Type()
)
tmnxWppPortalAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWppPortalAddr.setStatus("current")


class _TmnxWppPortalAdminState_Type(TmnxAdminState):
    """Custom type tmnxWppPortalAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxWppPortalAdminState_Type.__name__ = "TmnxAdminState"
_TmnxWppPortalAdminState_Object = MibTableColumn
tmnxWppPortalAdminState = _TmnxWppPortalAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 1, 1, 6),
    _TmnxWppPortalAdminState_Type()
)
tmnxWppPortalAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWppPortalAdminState.setStatus("current")


class _TmnxWppPortalSecret_Type(DisplayString):
    """Custom type tmnxWppPortalSecret based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxWppPortalSecret_Type.__name__ = "DisplayString"
_TmnxWppPortalSecret_Object = MibTableColumn
tmnxWppPortalSecret = _TmnxWppPortalSecret_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 1, 1, 7),
    _TmnxWppPortalSecret_Type()
)
tmnxWppPortalSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWppPortalSecret.setStatus("current")


class _TmnxWppPortalVersion_Type(Unsigned32):
    """Custom type tmnxWppPortalVersion based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_TmnxWppPortalVersion_Type.__name__ = "Unsigned32"
_TmnxWppPortalVersion_Object = MibTableColumn
tmnxWppPortalVersion = _TmnxWppPortalVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 1, 1, 8),
    _TmnxWppPortalVersion_Type()
)
tmnxWppPortalVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWppPortalVersion.setStatus("current")


class _TmnxWppPortalRetryInterval_Type(Unsigned32):
    """Custom type tmnxWppPortalRetryInterval based on Unsigned32"""
    defaultValue = 2000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2000),
    )


_TmnxWppPortalRetryInterval_Type.__name__ = "Unsigned32"
_TmnxWppPortalRetryInterval_Object = MibTableColumn
tmnxWppPortalRetryInterval = _TmnxWppPortalRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 1, 1, 9),
    _TmnxWppPortalRetryInterval_Type()
)
tmnxWppPortalRetryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWppPortalRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWppPortalRetryInterval.setUnits("milliseconds")


class _TmnxWppPortalNtfLogoutRetries_Type(Unsigned32):
    """Custom type tmnxWppPortalNtfLogoutRetries based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_TmnxWppPortalNtfLogoutRetries_Type.__name__ = "Unsigned32"
_TmnxWppPortalNtfLogoutRetries_Object = MibTableColumn
tmnxWppPortalNtfLogoutRetries = _TmnxWppPortalNtfLogoutRetries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 1, 1, 10),
    _TmnxWppPortalNtfLogoutRetries_Type()
)
tmnxWppPortalNtfLogoutRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWppPortalNtfLogoutRetries.setStatus("current")


class _TmnxWppPortalAckAuthRetries_Type(Unsigned32):
    """Custom type tmnxWppPortalAckAuthRetries based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_TmnxWppPortalAckAuthRetries_Type.__name__ = "Unsigned32"
_TmnxWppPortalAckAuthRetries_Object = MibTableColumn
tmnxWppPortalAckAuthRetries = _TmnxWppPortalAckAuthRetries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 1, 1, 11),
    _TmnxWppPortalAckAuthRetries_Type()
)
tmnxWppPortalAckAuthRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWppPortalAckAuthRetries.setStatus("current")


class _TmnxWppPortalAckInfoPortFormat_Type(Integer32):
    """Custom type tmnxWppPortalAckInfoPortFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standard", 1),
          ("vendorSpecific", 2))
    )


_TmnxWppPortalAckInfoPortFormat_Type.__name__ = "Integer32"
_TmnxWppPortalAckInfoPortFormat_Object = MibTableColumn
tmnxWppPortalAckInfoPortFormat = _TmnxWppPortalAckInfoPortFormat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 1, 1, 12),
    _TmnxWppPortalAckInfoPortFormat_Type()
)
tmnxWppPortalAckInfoPortFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWppPortalAckInfoPortFormat.setStatus("current")
_TmnxWppPortalStatTable_Object = MibTable
tmnxWppPortalStatTable = _TmnxWppPortalStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxWppPortalStatTable.setStatus("current")
_TmnxWppPortalStatEntry_Object = MibTableRow
tmnxWppPortalStatEntry = _TmnxWppPortalStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxWppPortalStatEntry.setStatus("current")
_TmnxWppPortalStateControlledRtr_Type = TmnxVRtrIDOrZero
_TmnxWppPortalStateControlledRtr_Object = MibTableColumn
tmnxWppPortalStateControlledRtr = _TmnxWppPortalStateControlledRtr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 2, 1, 1),
    _TmnxWppPortalStateControlledRtr_Type()
)
tmnxWppPortalStateControlledRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppPortalStateControlledRtr.setStatus("current")
_TmnxWppPortalStateNumInterfaces_Type = Gauge32
_TmnxWppPortalStateNumInterfaces_Object = MibTableColumn
tmnxWppPortalStateNumInterfaces = _TmnxWppPortalStateNumInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 2, 1, 2),
    _TmnxWppPortalStateNumInterfaces_Type()
)
tmnxWppPortalStateNumInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppPortalStateNumInterfaces.setStatus("current")
_TmnxWppPortalStateTriggeredHosts_Type = TmnxEnabledDisabled
_TmnxWppPortalStateTriggeredHosts_Object = MibTableColumn
tmnxWppPortalStateTriggeredHosts = _TmnxWppPortalStateTriggeredHosts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 2, 1, 3),
    _TmnxWppPortalStateTriggeredHosts_Type()
)
tmnxWppPortalStateTriggeredHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppPortalStateTriggeredHosts.setStatus("current")
_TmnxWppPortalStatsTable_Object = MibTable
tmnxWppPortalStatsTable = _TmnxWppPortalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxWppPortalStatsTable.setStatus("current")
_TmnxWppPortalStatsEntry_Object = MibTableRow
tmnxWppPortalStatsEntry = _TmnxWppPortalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 3, 1)
)
tmnxWppPortalStatsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalName"),
    (0, "TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalStatsType"),
    (0, "TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalStatsInstance"),
)
if mibBuilder.loadTexts:
    tmnxWppPortalStatsEntry.setStatus("current")
_TmnxWppPortalStatsType_Type = TmnxWppStatsType
_TmnxWppPortalStatsType_Object = MibTableColumn
tmnxWppPortalStatsType = _TmnxWppPortalStatsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 3, 1, 1),
    _TmnxWppPortalStatsType_Type()
)
tmnxWppPortalStatsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWppPortalStatsType.setStatus("current")


class _TmnxWppPortalStatsInstance_Type(Unsigned32):
    """Custom type tmnxWppPortalStatsInstance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_TmnxWppPortalStatsInstance_Type.__name__ = "Unsigned32"
_TmnxWppPortalStatsInstance_Object = MibTableColumn
tmnxWppPortalStatsInstance = _TmnxWppPortalStatsInstance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 3, 1, 2),
    _TmnxWppPortalStatsInstance_Type()
)
tmnxWppPortalStatsInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWppPortalStatsInstance.setStatus("current")


class _TmnxWppPortalStatsName_Type(DisplayString):
    """Custom type tmnxWppPortalStatsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmnxWppPortalStatsName_Type.__name__ = "DisplayString"
_TmnxWppPortalStatsName_Object = MibTableColumn
tmnxWppPortalStatsName = _TmnxWppPortalStatsName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 3, 1, 3),
    _TmnxWppPortalStatsName_Type()
)
tmnxWppPortalStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppPortalStatsName.setStatus("current")
_TmnxWppPortalStatsVal_Type = Counter32
_TmnxWppPortalStatsVal_Object = MibTableColumn
tmnxWppPortalStatsVal = _TmnxWppPortalStatsVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 3, 1, 4),
    _TmnxWppPortalStatsVal_Type()
)
tmnxWppPortalStatsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppPortalStatsVal.setStatus("current")
_TmnxWppHostTable_Object = MibTable
tmnxWppHostTable = _TmnxWppHostTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxWppHostTable.setStatus("current")
_TmnxWppHostEntry_Object = MibTableRow
tmnxWppHostEntry = _TmnxWppHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 4, 1)
)
tmnxWppHostEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalName"),
    (0, "TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppHostAddrType"),
    (0, "TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppHostAddr"),
)
if mibBuilder.loadTexts:
    tmnxWppHostEntry.setStatus("current")
_TmnxWppHostAddrType_Type = InetAddressType
_TmnxWppHostAddrType_Object = MibTableColumn
tmnxWppHostAddrType = _TmnxWppHostAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 4, 1, 1),
    _TmnxWppHostAddrType_Type()
)
tmnxWppHostAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWppHostAddrType.setStatus("current")


class _TmnxWppHostAddr_Type(InetAddress):
    """Custom type tmnxWppHostAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWppHostAddr_Type.__name__ = "InetAddress"
_TmnxWppHostAddr_Object = MibTableColumn
tmnxWppHostAddr = _TmnxWppHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 4, 1, 2),
    _TmnxWppHostAddr_Type()
)
tmnxWppHostAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWppHostAddr.setStatus("current")


class _TmnxWppHostStatus_Type(Integer32):
    """Custom type tmnxWppHostStatus based on Integer32"""
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
        *(("idle", 1),
          ("challenged", 2),
          ("authenticating", 3),
          ("authenticated", 4),
          ("established", 5),
          ("loggingOut", 6))
    )


_TmnxWppHostStatus_Type.__name__ = "Integer32"
_TmnxWppHostStatus_Object = MibTableColumn
tmnxWppHostStatus = _TmnxWppHostStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 4, 1, 3),
    _TmnxWppHostStatus_Type()
)
tmnxWppHostStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppHostStatus.setStatus("current")
_TmnxWppHostSerialNumber_Type = Unsigned32
_TmnxWppHostSerialNumber_Object = MibTableColumn
tmnxWppHostSerialNumber = _TmnxWppHostSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 4, 1, 4),
    _TmnxWppHostSerialNumber_Type()
)
tmnxWppHostSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppHostSerialNumber.setStatus("current")
_TmnxWppHostRequestId_Type = Unsigned32
_TmnxWppHostRequestId_Object = MibTableColumn
tmnxWppHostRequestId = _TmnxWppHostRequestId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 4, 1, 5),
    _TmnxWppHostRequestId_Type()
)
tmnxWppHostRequestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppHostRequestId.setStatus("current")
_TmnxWppHostPortalRemotePort_Type = InetPortNumber
_TmnxWppHostPortalRemotePort_Object = MibTableColumn
tmnxWppHostPortalRemotePort = _TmnxWppHostPortalRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 4, 1, 6),
    _TmnxWppHostPortalRemotePort_Type()
)
tmnxWppHostPortalRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppHostPortalRemotePort.setStatus("current")
_TmnxWppHostPortalLclIpAddrType_Type = InetAddressType
_TmnxWppHostPortalLclIpAddrType_Object = MibTableColumn
tmnxWppHostPortalLclIpAddrType = _TmnxWppHostPortalLclIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 4, 1, 7),
    _TmnxWppHostPortalLclIpAddrType_Type()
)
tmnxWppHostPortalLclIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppHostPortalLclIpAddrType.setStatus("current")


class _TmnxWppHostPortalLclIpAddr_Type(InetAddress):
    """Custom type tmnxWppHostPortalLclIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWppHostPortalLclIpAddr_Type.__name__ = "InetAddress"
_TmnxWppHostPortalLclIpAddr_Object = MibTableColumn
tmnxWppHostPortalLclIpAddr = _TmnxWppHostPortalLclIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 4, 1, 8),
    _TmnxWppHostPortalLclIpAddr_Type()
)
tmnxWppHostPortalLclIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppHostPortalLclIpAddr.setStatus("current")
_TmnxWppHostUserName_Type = TmnxWppUserName
_TmnxWppHostUserName_Object = MibTableColumn
tmnxWppHostUserName = _TmnxWppHostUserName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 4, 1, 9),
    _TmnxWppHostUserName_Type()
)
tmnxWppHostUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppHostUserName.setStatus("current")
_TmnxWppHostService_Type = TmnxServId
_TmnxWppHostService_Object = MibTableColumn
tmnxWppHostService = _TmnxWppHostService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 4, 1, 10),
    _TmnxWppHostService_Type()
)
tmnxWppHostService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppHostService.setStatus("current")
_TmnxWppHostMacAddress_Type = MacAddress
_TmnxWppHostMacAddress_Object = MibTableColumn
tmnxWppHostMacAddress = _TmnxWppHostMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 4, 1, 11),
    _TmnxWppHostMacAddress_Type()
)
tmnxWppHostMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppHostMacAddress.setStatus("current")
_TmnxWppHostIsTriggered_Type = TruthValue
_TmnxWppHostIsTriggered_Object = MibTableColumn
tmnxWppHostIsTriggered = _TmnxWppHostIsTriggered_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 4, 1, 12),
    _TmnxWppHostIsTriggered_Type()
)
tmnxWppHostIsTriggered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppHostIsTriggered.setStatus("current")
_TmnxWppHostTrackSrrpInst_Type = Unsigned32
_TmnxWppHostTrackSrrpInst_Object = MibTableColumn
tmnxWppHostTrackSrrpInst = _TmnxWppHostTrackSrrpInst_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 4, 1, 13),
    _TmnxWppHostTrackSrrpInst_Type()
)
tmnxWppHostTrackSrrpInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppHostTrackSrrpInst.setStatus("current")
_TmnxWppHostIsMCBackup_Type = TruthValue
_TmnxWppHostIsMCBackup_Object = MibTableColumn
tmnxWppHostIsMCBackup = _TmnxWppHostIsMCBackup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 4, 1, 14),
    _TmnxWppHostIsMCBackup_Type()
)
tmnxWppHostIsMCBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppHostIsMCBackup.setStatus("current")
_TmnxWppSessTable_Object = MibTable
tmnxWppSessTable = _TmnxWppSessTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxWppSessTable.setStatus("current")
_TmnxWppSessEntry_Object = MibTableRow
tmnxWppSessEntry = _TmnxWppSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 5, 1)
)
tmnxWppSessEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalName"),
    (0, "TIMETRA-SUBSCRIBER-MGMT-MIB", "tmnxSubIpoeIndex"),
)
if mibBuilder.loadTexts:
    tmnxWppSessEntry.setStatus("current")


class _TmnxWppSessStatus_Type(Integer32):
    """Custom type tmnxWppSessStatus based on Integer32"""
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
        *(("idle", 1),
          ("challenged", 2),
          ("authenticating", 3),
          ("authenticated", 4),
          ("established", 5),
          ("loggingOut", 6))
    )


_TmnxWppSessStatus_Type.__name__ = "Integer32"
_TmnxWppSessStatus_Object = MibTableColumn
tmnxWppSessStatus = _TmnxWppSessStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 5, 1, 1),
    _TmnxWppSessStatus_Type()
)
tmnxWppSessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppSessStatus.setStatus("current")
_TmnxWppSessSerialNumber_Type = Unsigned32
_TmnxWppSessSerialNumber_Object = MibTableColumn
tmnxWppSessSerialNumber = _TmnxWppSessSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 5, 1, 2),
    _TmnxWppSessSerialNumber_Type()
)
tmnxWppSessSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppSessSerialNumber.setStatus("current")
_TmnxWppSessRequestId_Type = Unsigned32
_TmnxWppSessRequestId_Object = MibTableColumn
tmnxWppSessRequestId = _TmnxWppSessRequestId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 5, 1, 3),
    _TmnxWppSessRequestId_Type()
)
tmnxWppSessRequestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppSessRequestId.setStatus("current")
_TmnxWppSessPortalRemotePort_Type = InetPortNumber
_TmnxWppSessPortalRemotePort_Object = MibTableColumn
tmnxWppSessPortalRemotePort = _TmnxWppSessPortalRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 5, 1, 4),
    _TmnxWppSessPortalRemotePort_Type()
)
tmnxWppSessPortalRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppSessPortalRemotePort.setStatus("current")
_TmnxWppSessPortalLclIpAddrType_Type = InetAddressType
_TmnxWppSessPortalLclIpAddrType_Object = MibTableColumn
tmnxWppSessPortalLclIpAddrType = _TmnxWppSessPortalLclIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 5, 1, 5),
    _TmnxWppSessPortalLclIpAddrType_Type()
)
tmnxWppSessPortalLclIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppSessPortalLclIpAddrType.setStatus("current")


class _TmnxWppSessPortalLclIpAddr_Type(InetAddress):
    """Custom type tmnxWppSessPortalLclIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWppSessPortalLclIpAddr_Type.__name__ = "InetAddress"
_TmnxWppSessPortalLclIpAddr_Object = MibTableColumn
tmnxWppSessPortalLclIpAddr = _TmnxWppSessPortalLclIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 5, 1, 6),
    _TmnxWppSessPortalLclIpAddr_Type()
)
tmnxWppSessPortalLclIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppSessPortalLclIpAddr.setStatus("current")
_TmnxWppSessUserName_Type = TmnxWppUserName
_TmnxWppSessUserName_Object = MibTableColumn
tmnxWppSessUserName = _TmnxWppSessUserName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 5, 1, 7),
    _TmnxWppSessUserName_Type()
)
tmnxWppSessUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppSessUserName.setStatus("current")
_TmnxWppSessService_Type = TmnxServId
_TmnxWppSessService_Object = MibTableColumn
tmnxWppSessService = _TmnxWppSessService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 5, 1, 8),
    _TmnxWppSessService_Type()
)
tmnxWppSessService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppSessService.setStatus("current")
_TmnxWppSessMacAddress_Type = MacAddress
_TmnxWppSessMacAddress_Object = MibTableColumn
tmnxWppSessMacAddress = _TmnxWppSessMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 5, 1, 9),
    _TmnxWppSessMacAddress_Type()
)
tmnxWppSessMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppSessMacAddress.setStatus("current")
_TmnxWppSessIsTriggered_Type = TruthValue
_TmnxWppSessIsTriggered_Object = MibTableColumn
tmnxWppSessIsTriggered = _TmnxWppSessIsTriggered_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 5, 1, 10),
    _TmnxWppSessIsTriggered_Type()
)
tmnxWppSessIsTriggered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppSessIsTriggered.setStatus("current")
_TmnxWppSessTrackSrrpInst_Type = Unsigned32
_TmnxWppSessTrackSrrpInst_Object = MibTableColumn
tmnxWppSessTrackSrrpInst = _TmnxWppSessTrackSrrpInst_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 5, 1, 11),
    _TmnxWppSessTrackSrrpInst_Type()
)
tmnxWppSessTrackSrrpInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppSessTrackSrrpInst.setStatus("current")
_TmnxWppSessIsMCBackup_Type = TruthValue
_TmnxWppSessIsMCBackup_Object = MibTableColumn
tmnxWppSessIsMCBackup = _TmnxWppSessIsMCBackup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 5, 1, 12),
    _TmnxWppSessIsMCBackup_Type()
)
tmnxWppSessIsMCBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppSessIsMCBackup.setStatus("current")
_TmnxWppSessClientAddrType_Type = InetAddressType
_TmnxWppSessClientAddrType_Object = MibTableColumn
tmnxWppSessClientAddrType = _TmnxWppSessClientAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 5, 1, 13),
    _TmnxWppSessClientAddrType_Type()
)
tmnxWppSessClientAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppSessClientAddrType.setStatus("current")


class _TmnxWppSessClientAddr_Type(InetAddress):
    """Custom type tmnxWppSessClientAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWppSessClientAddr_Type.__name__ = "InetAddress"
_TmnxWppSessClientAddr_Object = MibTableColumn
tmnxWppSessClientAddr = _TmnxWppSessClientAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 1, 5, 1, 14),
    _TmnxWppSessClientAddr_Type()
)
tmnxWppSessClientAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppSessClientAddr.setStatus("current")
_TmnxWppTable_Object = MibTable
tmnxWppTable = _TmnxWppTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxWppTable.setStatus("current")
_TmnxWppEntry_Object = MibTableRow
tmnxWppEntry = _TmnxWppEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 2, 1)
)
tmnxWppEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    tmnxWppEntry.setStatus("current")
_TmnxWppRowStatus_Type = RowStatus
_TmnxWppRowStatus_Object = MibTableColumn
tmnxWppRowStatus = _TmnxWppRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 2, 1, 1),
    _TmnxWppRowStatus_Type()
)
tmnxWppRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWppRowStatus.setStatus("current")
_TmnxWppLastCh_Type = TimeStamp
_TmnxWppLastCh_Object = MibTableColumn
tmnxWppLastCh = _TmnxWppLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 2, 1, 2),
    _TmnxWppLastCh_Type()
)
tmnxWppLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppLastCh.setStatus("current")


class _TmnxWppAdminState_Type(TmnxAdminState):
    """Custom type tmnxWppAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxWppAdminState_Type.__name__ = "TmnxAdminState"
_TmnxWppAdminState_Object = MibTableColumn
tmnxWppAdminState = _TmnxWppAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 2, 1, 3),
    _TmnxWppAdminState_Type()
)
tmnxWppAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWppAdminState.setStatus("current")
_TmnxWppStatsTable_Object = MibTable
tmnxWppStatsTable = _TmnxWppStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxWppStatsTable.setStatus("current")
_TmnxWppStatsEntry_Object = MibTableRow
tmnxWppStatsEntry = _TmnxWppStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 3, 1)
)
tmnxWppStatsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppStatsType"),
    (0, "TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppStatsInstance"),
)
if mibBuilder.loadTexts:
    tmnxWppStatsEntry.setStatus("current")
_TmnxWppStatsType_Type = TmnxWppStatsType
_TmnxWppStatsType_Object = MibTableColumn
tmnxWppStatsType = _TmnxWppStatsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 3, 1, 1),
    _TmnxWppStatsType_Type()
)
tmnxWppStatsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWppStatsType.setStatus("current")


class _TmnxWppStatsInstance_Type(Unsigned32):
    """Custom type tmnxWppStatsInstance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_TmnxWppStatsInstance_Type.__name__ = "Unsigned32"
_TmnxWppStatsInstance_Object = MibTableColumn
tmnxWppStatsInstance = _TmnxWppStatsInstance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 3, 1, 2),
    _TmnxWppStatsInstance_Type()
)
tmnxWppStatsInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWppStatsInstance.setStatus("current")


class _TmnxWppStatsName_Type(DisplayString):
    """Custom type tmnxWppStatsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmnxWppStatsName_Type.__name__ = "DisplayString"
_TmnxWppStatsName_Object = MibTableColumn
tmnxWppStatsName = _TmnxWppStatsName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 3, 1, 3),
    _TmnxWppStatsName_Type()
)
tmnxWppStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppStatsName.setStatus("current")
_TmnxWppStatsVal_Type = Counter32
_TmnxWppStatsVal_Object = MibTableColumn
tmnxWppStatsVal = _TmnxWppStatsVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 3, 1, 4),
    _TmnxWppStatsVal_Type()
)
tmnxWppStatsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppStatsVal.setStatus("current")
_TmnxWppIfTable_Object = MibTable
tmnxWppIfTable = _TmnxWppIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxWppIfTable.setStatus("current")
_TmnxWppIfEntry_Object = MibTableRow
tmnxWppIfEntry = _TmnxWppIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 4, 1)
)
tmnxWppIfEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "iesIfIndex"),
)
if mibBuilder.loadTexts:
    tmnxWppIfEntry.setStatus("current")
_TmnxWppIfLastCh_Type = TimeStamp
_TmnxWppIfLastCh_Object = MibTableColumn
tmnxWppIfLastCh = _TmnxWppIfLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 4, 1, 1),
    _TmnxWppIfLastCh_Type()
)
tmnxWppIfLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppIfLastCh.setStatus("current")
_TmnxWppIfRowStatus_Type = RowStatus
_TmnxWppIfRowStatus_Object = MibTableColumn
tmnxWppIfRowStatus = _TmnxWppIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 4, 1, 2),
    _TmnxWppIfRowStatus_Type()
)
tmnxWppIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWppIfRowStatus.setStatus("current")


class _TmnxWppIfAdminState_Type(TmnxAdminState):
    """Custom type tmnxWppIfAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxWppIfAdminState_Type.__name__ = "TmnxAdminState"
_TmnxWppIfAdminState_Object = MibTableColumn
tmnxWppIfAdminState = _TmnxWppIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 4, 1, 3),
    _TmnxWppIfAdminState_Type()
)
tmnxWppIfAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWppIfAdminState.setStatus("current")


class _TmnxWppIfPortalRouter_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxWppIfPortalRouter based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TmnxWppIfPortalRouter_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxWppIfPortalRouter_Object = MibTableColumn
tmnxWppIfPortalRouter = _TmnxWppIfPortalRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 4, 1, 4),
    _TmnxWppIfPortalRouter_Type()
)
tmnxWppIfPortalRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWppIfPortalRouter.setStatus("current")


class _TmnxWppIfPortalName_Type(TNamedItemOrEmpty):
    """Custom type tmnxWppIfPortalName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxWppIfPortalName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWppIfPortalName_Object = MibTableColumn
tmnxWppIfPortalName = _TmnxWppIfPortalName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 4, 1, 5),
    _TmnxWppIfPortalName_Type()
)
tmnxWppIfPortalName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWppIfPortalName.setStatus("current")


class _TmnxWppIfSubProfile_Type(TNamedItemOrEmpty):
    """Custom type tmnxWppIfSubProfile based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxWppIfSubProfile_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWppIfSubProfile_Object = MibTableColumn
tmnxWppIfSubProfile = _TmnxWppIfSubProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 4, 1, 6),
    _TmnxWppIfSubProfile_Type()
)
tmnxWppIfSubProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWppIfSubProfile.setStatus("current")


class _TmnxWppIfSLAProfile_Type(TNamedItemOrEmpty):
    """Custom type tmnxWppIfSLAProfile based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxWppIfSLAProfile_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWppIfSLAProfile_Object = MibTableColumn
tmnxWppIfSLAProfile = _TmnxWppIfSLAProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 4, 1, 7),
    _TmnxWppIfSLAProfile_Type()
)
tmnxWppIfSLAProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWppIfSLAProfile.setStatus("current")


class _TmnxWppIfAppProfile_Type(TNamedItemOrEmpty):
    """Custom type tmnxWppIfAppProfile based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxWppIfAppProfile_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWppIfAppProfile_Object = MibTableColumn
tmnxWppIfAppProfile = _TmnxWppIfAppProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 4, 1, 8),
    _TmnxWppIfAppProfile_Type()
)
tmnxWppIfAppProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWppIfAppProfile.setStatus("current")


class _TmnxWppIfRestoreDisconnected_Type(TruthValue):
    """Custom type tmnxWppIfRestoreDisconnected based on TruthValue"""
    defaultValue = 1


_TmnxWppIfRestoreDisconnected_Type.__name__ = "TruthValue"
_TmnxWppIfRestoreDisconnected_Object = MibTableColumn
tmnxWppIfRestoreDisconnected = _TmnxWppIfRestoreDisconnected_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 4, 1, 9),
    _TmnxWppIfRestoreDisconnected_Type()
)
tmnxWppIfRestoreDisconnected.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWppIfRestoreDisconnected.setStatus("current")


class _TmnxWppIfUserDb_Type(TNamedItemOrEmpty):
    """Custom type tmnxWppIfUserDb based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxWppIfUserDb_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWppIfUserDb_Object = MibTableColumn
tmnxWppIfUserDb = _TmnxWppIfUserDb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 4, 1, 10),
    _TmnxWppIfUserDb_Type()
)
tmnxWppIfUserDb.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWppIfUserDb.setStatus("current")


class _TmnxWppIfLeaseTime_Type(Unsigned32):
    """Custom type tmnxWppIfLeaseTime based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 315446399),
    )


_TmnxWppIfLeaseTime_Type.__name__ = "Unsigned32"
_TmnxWppIfLeaseTime_Object = MibTableColumn
tmnxWppIfLeaseTime = _TmnxWppIfLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 4, 1, 11),
    _TmnxWppIfLeaseTime_Type()
)
tmnxWppIfLeaseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWppIfLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWppIfLeaseTime.setUnits("seconds")


class _TmnxWppIfEnableTriggeredHosts_Type(TruthValue):
    """Custom type tmnxWppIfEnableTriggeredHosts based on TruthValue"""
    defaultValue = 2


_TmnxWppIfEnableTriggeredHosts_Type.__name__ = "TruthValue"
_TmnxWppIfEnableTriggeredHosts_Object = MibTableColumn
tmnxWppIfEnableTriggeredHosts = _TmnxWppIfEnableTriggeredHosts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 4, 1, 12),
    _TmnxWppIfEnableTriggeredHosts_Type()
)
tmnxWppIfEnableTriggeredHosts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWppIfEnableTriggeredHosts.setStatus("current")


class _TmnxWppIfPortalGroupName_Type(TNamedItemOrEmpty):
    """Custom type tmnxWppIfPortalGroupName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxWppIfPortalGroupName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWppIfPortalGroupName_Object = MibTableColumn
tmnxWppIfPortalGroupName = _TmnxWppIfPortalGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 4, 1, 13),
    _TmnxWppIfPortalGroupName_Type()
)
tmnxWppIfPortalGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWppIfPortalGroupName.setStatus("current")
_TmnxWppPortalGroupTable_Object = MibTable
tmnxWppPortalGroupTable = _TmnxWppPortalGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxWppPortalGroupTable.setStatus("current")
_TmnxWppPortalGroupEntry_Object = MibTableRow
tmnxWppPortalGroupEntry = _TmnxWppPortalGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 5, 1)
)
tmnxWppPortalGroupEntry.setIndexNames(
    (1, "TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalGroupName"),
)
if mibBuilder.loadTexts:
    tmnxWppPortalGroupEntry.setStatus("current")
_TmnxWppPortalGroupName_Type = TNamedItem
_TmnxWppPortalGroupName_Object = MibTableColumn
tmnxWppPortalGroupName = _TmnxWppPortalGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 5, 1, 1),
    _TmnxWppPortalGroupName_Type()
)
tmnxWppPortalGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWppPortalGroupName.setStatus("current")
_TmnxWppPortalGroupLastCh_Type = TimeStamp
_TmnxWppPortalGroupLastCh_Object = MibTableColumn
tmnxWppPortalGroupLastCh = _TmnxWppPortalGroupLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 5, 1, 2),
    _TmnxWppPortalGroupLastCh_Type()
)
tmnxWppPortalGroupLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppPortalGroupLastCh.setStatus("current")
_TmnxWppPortalGroupRowStatus_Type = RowStatus
_TmnxWppPortalGroupRowStatus_Object = MibTableColumn
tmnxWppPortalGroupRowStatus = _TmnxWppPortalGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 5, 1, 3),
    _TmnxWppPortalGroupRowStatus_Type()
)
tmnxWppPortalGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWppPortalGroupRowStatus.setStatus("current")


class _TmnxWppPortalGroupDescription_Type(TItemDescription):
    """Custom type tmnxWppPortalGroupDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxWppPortalGroupDescription_Type.__name__ = "TItemDescription"
_TmnxWppPortalGroupDescription_Object = MibTableColumn
tmnxWppPortalGroupDescription = _TmnxWppPortalGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 5, 1, 4),
    _TmnxWppPortalGroupDescription_Type()
)
tmnxWppPortalGroupDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWppPortalGroupDescription.setStatus("current")


class _TmnxWppPortalGroupAdminState_Type(TmnxAdminState):
    """Custom type tmnxWppPortalGroupAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxWppPortalGroupAdminState_Type.__name__ = "TmnxAdminState"
_TmnxWppPortalGroupAdminState_Object = MibTableColumn
tmnxWppPortalGroupAdminState = _TmnxWppPortalGroupAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 5, 1, 5),
    _TmnxWppPortalGroupAdminState_Type()
)
tmnxWppPortalGroupAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWppPortalGroupAdminState.setStatus("current")
_TmnxWppPortalGroupPortalTable_Object = MibTable
tmnxWppPortalGroupPortalTable = _TmnxWppPortalGroupPortalTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxWppPortalGroupPortalTable.setStatus("current")
_TmnxWppPortalGroupPortalEntry_Object = MibTableRow
tmnxWppPortalGroupPortalEntry = _TmnxWppPortalGroupPortalEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 6, 1)
)
tmnxWppPortalGroupPortalEntry.setIndexNames(
    (0, "TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalGroupName"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (1, "TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalGroupPortalName"),
)
if mibBuilder.loadTexts:
    tmnxWppPortalGroupPortalEntry.setStatus("current")
_TmnxWppPortalGroupPortalName_Type = TNamedItem
_TmnxWppPortalGroupPortalName_Object = MibTableColumn
tmnxWppPortalGroupPortalName = _TmnxWppPortalGroupPortalName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 6, 1, 1),
    _TmnxWppPortalGroupPortalName_Type()
)
tmnxWppPortalGroupPortalName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWppPortalGroupPortalName.setStatus("current")
_TmnxWppPortalGroupPortalLastCh_Type = TimeStamp
_TmnxWppPortalGroupPortalLastCh_Object = MibTableColumn
tmnxWppPortalGroupPortalLastCh = _TmnxWppPortalGroupPortalLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 6, 1, 2),
    _TmnxWppPortalGroupPortalLastCh_Type()
)
tmnxWppPortalGroupPortalLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppPortalGroupPortalLastCh.setStatus("current")
_TmnxWppPortalGroupPortalRowStat_Type = RowStatus
_TmnxWppPortalGroupPortalRowStat_Object = MibTableColumn
tmnxWppPortalGroupPortalRowStat = _TmnxWppPortalGroupPortalRowStat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 6, 1, 3),
    _TmnxWppPortalGroupPortalRowStat_Type()
)
tmnxWppPortalGroupPortalRowStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWppPortalGroupPortalRowStat.setStatus("current")
_TmnxWppPortalGroupStatTable_Object = MibTable
tmnxWppPortalGroupStatTable = _TmnxWppPortalGroupStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 7)
)
if mibBuilder.loadTexts:
    tmnxWppPortalGroupStatTable.setStatus("current")
_TmnxWppPortalGroupStatEntry_Object = MibTableRow
tmnxWppPortalGroupStatEntry = _TmnxWppPortalGroupStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 7, 1)
)
if mibBuilder.loadTexts:
    tmnxWppPortalGroupStatEntry.setStatus("current")
_TmnxWppPortalGroupStateContrRtr_Type = TmnxVRtrIDOrZero
_TmnxWppPortalGroupStateContrRtr_Object = MibTableColumn
tmnxWppPortalGroupStateContrRtr = _TmnxWppPortalGroupStateContrRtr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 7, 1, 1),
    _TmnxWppPortalGroupStateContrRtr_Type()
)
tmnxWppPortalGroupStateContrRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppPortalGroupStateContrRtr.setStatus("current")
_TmnxWppPortalGroupStateNumItfs_Type = Gauge32
_TmnxWppPortalGroupStateNumItfs_Object = MibTableColumn
tmnxWppPortalGroupStateNumItfs = _TmnxWppPortalGroupStateNumItfs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 7, 1, 2),
    _TmnxWppPortalGroupStateNumItfs_Type()
)
tmnxWppPortalGroupStateNumItfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppPortalGroupStateNumItfs.setStatus("current")
_TmnxWppPortalGroupStateTrigHosts_Type = TmnxEnabledDisabled
_TmnxWppPortalGroupStateTrigHosts_Object = MibTableColumn
tmnxWppPortalGroupStateTrigHosts = _TmnxWppPortalGroupStateTrigHosts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 7, 1, 3),
    _TmnxWppPortalGroupStateTrigHosts_Type()
)
tmnxWppPortalGroupStateTrigHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppPortalGroupStateTrigHosts.setStatus("current")
_TmnxWppPGHostTable_Object = MibTable
tmnxWppPGHostTable = _TmnxWppPGHostTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 8)
)
if mibBuilder.loadTexts:
    tmnxWppPGHostTable.setStatus("current")
_TmnxWppPGHostEntry_Object = MibTableRow
tmnxWppPGHostEntry = _TmnxWppPGHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 8, 1)
)
tmnxWppPGHostEntry.setIndexNames(
    (0, "TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalGroupName"),
    (0, "TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPGHostAddrType"),
    (0, "TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPGHostAddr"),
)
if mibBuilder.loadTexts:
    tmnxWppPGHostEntry.setStatus("current")
_TmnxWppPGHostAddrType_Type = InetAddressType
_TmnxWppPGHostAddrType_Object = MibTableColumn
tmnxWppPGHostAddrType = _TmnxWppPGHostAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 8, 1, 1),
    _TmnxWppPGHostAddrType_Type()
)
tmnxWppPGHostAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWppPGHostAddrType.setStatus("current")


class _TmnxWppPGHostAddr_Type(InetAddress):
    """Custom type tmnxWppPGHostAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWppPGHostAddr_Type.__name__ = "InetAddress"
_TmnxWppPGHostAddr_Object = MibTableColumn
tmnxWppPGHostAddr = _TmnxWppPGHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 8, 1, 2),
    _TmnxWppPGHostAddr_Type()
)
tmnxWppPGHostAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWppPGHostAddr.setStatus("current")


class _TmnxWppPGHostStatus_Type(Integer32):
    """Custom type tmnxWppPGHostStatus based on Integer32"""
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
        *(("idle", 1),
          ("challenged", 2),
          ("authenticating", 3),
          ("authenticated", 4),
          ("established", 5),
          ("loggingOut", 6))
    )


_TmnxWppPGHostStatus_Type.__name__ = "Integer32"
_TmnxWppPGHostStatus_Object = MibTableColumn
tmnxWppPGHostStatus = _TmnxWppPGHostStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 8, 1, 3),
    _TmnxWppPGHostStatus_Type()
)
tmnxWppPGHostStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppPGHostStatus.setStatus("current")
_TmnxWppPGHostSerialNumber_Type = Unsigned32
_TmnxWppPGHostSerialNumber_Object = MibTableColumn
tmnxWppPGHostSerialNumber = _TmnxWppPGHostSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 8, 1, 4),
    _TmnxWppPGHostSerialNumber_Type()
)
tmnxWppPGHostSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppPGHostSerialNumber.setStatus("current")
_TmnxWppPGHostRequestId_Type = Unsigned32
_TmnxWppPGHostRequestId_Object = MibTableColumn
tmnxWppPGHostRequestId = _TmnxWppPGHostRequestId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 8, 1, 5),
    _TmnxWppPGHostRequestId_Type()
)
tmnxWppPGHostRequestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppPGHostRequestId.setStatus("current")
_TmnxWppPGHostPortalRemotePort_Type = InetPortNumber
_TmnxWppPGHostPortalRemotePort_Object = MibTableColumn
tmnxWppPGHostPortalRemotePort = _TmnxWppPGHostPortalRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 8, 1, 6),
    _TmnxWppPGHostPortalRemotePort_Type()
)
tmnxWppPGHostPortalRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppPGHostPortalRemotePort.setStatus("current")
_TmnxWppPGHostPortalLclIpAddrType_Type = InetAddressType
_TmnxWppPGHostPortalLclIpAddrType_Object = MibTableColumn
tmnxWppPGHostPortalLclIpAddrType = _TmnxWppPGHostPortalLclIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 8, 1, 7),
    _TmnxWppPGHostPortalLclIpAddrType_Type()
)
tmnxWppPGHostPortalLclIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppPGHostPortalLclIpAddrType.setStatus("current")


class _TmnxWppPGHostPortalLclIpAddr_Type(InetAddress):
    """Custom type tmnxWppPGHostPortalLclIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWppPGHostPortalLclIpAddr_Type.__name__ = "InetAddress"
_TmnxWppPGHostPortalLclIpAddr_Object = MibTableColumn
tmnxWppPGHostPortalLclIpAddr = _TmnxWppPGHostPortalLclIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 8, 1, 8),
    _TmnxWppPGHostPortalLclIpAddr_Type()
)
tmnxWppPGHostPortalLclIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppPGHostPortalLclIpAddr.setStatus("current")
_TmnxWppPGHostUserName_Type = TmnxWppUserName
_TmnxWppPGHostUserName_Object = MibTableColumn
tmnxWppPGHostUserName = _TmnxWppPGHostUserName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 8, 1, 9),
    _TmnxWppPGHostUserName_Type()
)
tmnxWppPGHostUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppPGHostUserName.setStatus("current")
_TmnxWppPGHostService_Type = TmnxServId
_TmnxWppPGHostService_Object = MibTableColumn
tmnxWppPGHostService = _TmnxWppPGHostService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 8, 1, 10),
    _TmnxWppPGHostService_Type()
)
tmnxWppPGHostService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppPGHostService.setStatus("current")
_TmnxWppPGHostMacAddress_Type = MacAddress
_TmnxWppPGHostMacAddress_Object = MibTableColumn
tmnxWppPGHostMacAddress = _TmnxWppPGHostMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 8, 1, 11),
    _TmnxWppPGHostMacAddress_Type()
)
tmnxWppPGHostMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppPGHostMacAddress.setStatus("current")
_TmnxWppPGHostIsTriggered_Type = TruthValue
_TmnxWppPGHostIsTriggered_Object = MibTableColumn
tmnxWppPGHostIsTriggered = _TmnxWppPGHostIsTriggered_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 8, 1, 12),
    _TmnxWppPGHostIsTriggered_Type()
)
tmnxWppPGHostIsTriggered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppPGHostIsTriggered.setStatus("current")
_TmnxWppPGHostTrackSrrpInst_Type = Unsigned32
_TmnxWppPGHostTrackSrrpInst_Object = MibTableColumn
tmnxWppPGHostTrackSrrpInst = _TmnxWppPGHostTrackSrrpInst_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 8, 1, 13),
    _TmnxWppPGHostTrackSrrpInst_Type()
)
tmnxWppPGHostTrackSrrpInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppPGHostTrackSrrpInst.setStatus("current")
_TmnxWppPGHostIsMCBackup_Type = TruthValue
_TmnxWppPGHostIsMCBackup_Object = MibTableColumn
tmnxWppPGHostIsMCBackup = _TmnxWppPGHostIsMCBackup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 8, 1, 14),
    _TmnxWppPGHostIsMCBackup_Type()
)
tmnxWppPGHostIsMCBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppPGHostIsMCBackup.setStatus("current")
_TmnxWppPGHostActivePortalRouter_Type = TmnxVRtrIDOrZero
_TmnxWppPGHostActivePortalRouter_Object = MibTableColumn
tmnxWppPGHostActivePortalRouter = _TmnxWppPGHostActivePortalRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 8, 1, 15),
    _TmnxWppPGHostActivePortalRouter_Type()
)
tmnxWppPGHostActivePortalRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppPGHostActivePortalRouter.setStatus("current")
_TmnxWppPGHostActivePortalName_Type = TNamedItemOrEmpty
_TmnxWppPGHostActivePortalName_Object = MibTableColumn
tmnxWppPGHostActivePortalName = _TmnxWppPGHostActivePortalName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 8, 1, 16),
    _TmnxWppPGHostActivePortalName_Type()
)
tmnxWppPGHostActivePortalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppPGHostActivePortalName.setStatus("current")
_TmnxWppPGSessTable_Object = MibTable
tmnxWppPGSessTable = _TmnxWppPGSessTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 9)
)
if mibBuilder.loadTexts:
    tmnxWppPGSessTable.setStatus("current")
_TmnxWppPGSessEntry_Object = MibTableRow
tmnxWppPGSessEntry = _TmnxWppPGSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 9, 1)
)
tmnxWppPGSessEntry.setIndexNames(
    (0, "TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalGroupName"),
    (0, "TIMETRA-SUBSCRIBER-MGMT-MIB", "tmnxSubIpoeIndex"),
)
if mibBuilder.loadTexts:
    tmnxWppPGSessEntry.setStatus("current")


class _TmnxWppPGSessStatus_Type(Integer32):
    """Custom type tmnxWppPGSessStatus based on Integer32"""
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
        *(("idle", 1),
          ("challenged", 2),
          ("authenticating", 3),
          ("authenticated", 4),
          ("established", 5),
          ("loggingOut", 6))
    )


_TmnxWppPGSessStatus_Type.__name__ = "Integer32"
_TmnxWppPGSessStatus_Object = MibTableColumn
tmnxWppPGSessStatus = _TmnxWppPGSessStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 9, 1, 1),
    _TmnxWppPGSessStatus_Type()
)
tmnxWppPGSessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppPGSessStatus.setStatus("current")
_TmnxWppPGSessSerialNumber_Type = Unsigned32
_TmnxWppPGSessSerialNumber_Object = MibTableColumn
tmnxWppPGSessSerialNumber = _TmnxWppPGSessSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 9, 1, 2),
    _TmnxWppPGSessSerialNumber_Type()
)
tmnxWppPGSessSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppPGSessSerialNumber.setStatus("current")
_TmnxWppPGSessRequestId_Type = Unsigned32
_TmnxWppPGSessRequestId_Object = MibTableColumn
tmnxWppPGSessRequestId = _TmnxWppPGSessRequestId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 9, 1, 3),
    _TmnxWppPGSessRequestId_Type()
)
tmnxWppPGSessRequestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppPGSessRequestId.setStatus("current")
_TmnxWppPGSessPortalRemotePort_Type = InetPortNumber
_TmnxWppPGSessPortalRemotePort_Object = MibTableColumn
tmnxWppPGSessPortalRemotePort = _TmnxWppPGSessPortalRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 9, 1, 4),
    _TmnxWppPGSessPortalRemotePort_Type()
)
tmnxWppPGSessPortalRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppPGSessPortalRemotePort.setStatus("current")
_TmnxWppPGSessPortalLclIpAddrType_Type = InetAddressType
_TmnxWppPGSessPortalLclIpAddrType_Object = MibTableColumn
tmnxWppPGSessPortalLclIpAddrType = _TmnxWppPGSessPortalLclIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 9, 1, 5),
    _TmnxWppPGSessPortalLclIpAddrType_Type()
)
tmnxWppPGSessPortalLclIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppPGSessPortalLclIpAddrType.setStatus("current")


class _TmnxWppPGSessPortalLclIpAddr_Type(InetAddress):
    """Custom type tmnxWppPGSessPortalLclIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWppPGSessPortalLclIpAddr_Type.__name__ = "InetAddress"
_TmnxWppPGSessPortalLclIpAddr_Object = MibTableColumn
tmnxWppPGSessPortalLclIpAddr = _TmnxWppPGSessPortalLclIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 9, 1, 6),
    _TmnxWppPGSessPortalLclIpAddr_Type()
)
tmnxWppPGSessPortalLclIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppPGSessPortalLclIpAddr.setStatus("current")
_TmnxWppPGSessUserName_Type = TmnxWppUserName
_TmnxWppPGSessUserName_Object = MibTableColumn
tmnxWppPGSessUserName = _TmnxWppPGSessUserName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 9, 1, 7),
    _TmnxWppPGSessUserName_Type()
)
tmnxWppPGSessUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppPGSessUserName.setStatus("current")
_TmnxWppPGSessService_Type = TmnxServId
_TmnxWppPGSessService_Object = MibTableColumn
tmnxWppPGSessService = _TmnxWppPGSessService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 9, 1, 8),
    _TmnxWppPGSessService_Type()
)
tmnxWppPGSessService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppPGSessService.setStatus("current")
_TmnxWppPGSessMacAddress_Type = MacAddress
_TmnxWppPGSessMacAddress_Object = MibTableColumn
tmnxWppPGSessMacAddress = _TmnxWppPGSessMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 9, 1, 9),
    _TmnxWppPGSessMacAddress_Type()
)
tmnxWppPGSessMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppPGSessMacAddress.setStatus("current")
_TmnxWppPGSessIsTriggered_Type = TruthValue
_TmnxWppPGSessIsTriggered_Object = MibTableColumn
tmnxWppPGSessIsTriggered = _TmnxWppPGSessIsTriggered_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 9, 1, 10),
    _TmnxWppPGSessIsTriggered_Type()
)
tmnxWppPGSessIsTriggered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppPGSessIsTriggered.setStatus("current")
_TmnxWppPGSessTrackSrrpInst_Type = Unsigned32
_TmnxWppPGSessTrackSrrpInst_Object = MibTableColumn
tmnxWppPGSessTrackSrrpInst = _TmnxWppPGSessTrackSrrpInst_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 9, 1, 11),
    _TmnxWppPGSessTrackSrrpInst_Type()
)
tmnxWppPGSessTrackSrrpInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppPGSessTrackSrrpInst.setStatus("current")
_TmnxWppPGSessIsMCBackup_Type = TruthValue
_TmnxWppPGSessIsMCBackup_Object = MibTableColumn
tmnxWppPGSessIsMCBackup = _TmnxWppPGSessIsMCBackup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 9, 1, 12),
    _TmnxWppPGSessIsMCBackup_Type()
)
tmnxWppPGSessIsMCBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppPGSessIsMCBackup.setStatus("current")
_TmnxWppPGSessActivePortalRouter_Type = TmnxVRtrIDOrZero
_TmnxWppPGSessActivePortalRouter_Object = MibTableColumn
tmnxWppPGSessActivePortalRouter = _TmnxWppPGSessActivePortalRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 9, 1, 13),
    _TmnxWppPGSessActivePortalRouter_Type()
)
tmnxWppPGSessActivePortalRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppPGSessActivePortalRouter.setStatus("current")
_TmnxWppPGSessActivePortalName_Type = TNamedItemOrEmpty
_TmnxWppPGSessActivePortalName_Object = MibTableColumn
tmnxWppPGSessActivePortalName = _TmnxWppPGSessActivePortalName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 9, 1, 14),
    _TmnxWppPGSessActivePortalName_Type()
)
tmnxWppPGSessActivePortalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppPGSessActivePortalName.setStatus("current")
_TmnxWppPGSessClientAddrType_Type = InetAddressType
_TmnxWppPGSessClientAddrType_Object = MibTableColumn
tmnxWppPGSessClientAddrType = _TmnxWppPGSessClientAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 9, 1, 15),
    _TmnxWppPGSessClientAddrType_Type()
)
tmnxWppPGSessClientAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppPGSessClientAddrType.setStatus("current")


class _TmnxWppPGSessClientAddr_Type(InetAddress):
    """Custom type tmnxWppPGSessClientAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWppPGSessClientAddr_Type.__name__ = "InetAddress"
_TmnxWppPGSessClientAddr_Object = MibTableColumn
tmnxWppPGSessClientAddr = _TmnxWppPGSessClientAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 9, 1, 16),
    _TmnxWppPGSessClientAddr_Type()
)
tmnxWppPGSessClientAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppPGSessClientAddr.setStatus("current")
_TmnxWppSysObjs_ObjectIdentity = ObjectIdentity
tmnxWppSysObjs = _TmnxWppSysObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 99)
)


class _TmnxWppSysName_Type(DisplayString):
    """Custom type tmnxWppSysName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TmnxWppSysName_Type.__name__ = "DisplayString"
_TmnxWppSysName_Object = MibScalar
tmnxWppSysName = _TmnxWppSysName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 99, 1),
    _TmnxWppSysName_Type()
)
tmnxWppSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxWppSysName.setStatus("current")
_TmnxWppTableLastCh_Type = TimeStamp
_TmnxWppTableLastCh_Object = MibScalar
tmnxWppTableLastCh = _TmnxWppTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 100),
    _TmnxWppTableLastCh_Type()
)
tmnxWppTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppTableLastCh.setStatus("current")
_TmnxWppPortalTableLastCh_Type = TimeStamp
_TmnxWppPortalTableLastCh_Object = MibScalar
tmnxWppPortalTableLastCh = _TmnxWppPortalTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 101),
    _TmnxWppPortalTableLastCh_Type()
)
tmnxWppPortalTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppPortalTableLastCh.setStatus("current")
_TmnxWppIfTableLastCh_Type = TimeStamp
_TmnxWppIfTableLastCh_Object = MibScalar
tmnxWppIfTableLastCh = _TmnxWppIfTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 1, 102),
    _TmnxWppIfTableLastCh_Type()
)
tmnxWppIfTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWppIfTableLastCh.setStatus("current")
_TmnxWppNotificationObjs_ObjectIdentity = ObjectIdentity
tmnxWppNotificationObjs = _TmnxWppNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 2)
)


class _TmnxWppNotifyDescription_Type(DisplayString):
    """Custom type tmnxWppNotifyDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxWppNotifyDescription_Type.__name__ = "DisplayString"
_TmnxWppNotifyDescription_Object = MibScalar
tmnxWppNotifyDescription = _TmnxWppNotifyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 80, 2, 1),
    _TmnxWppNotifyDescription_Type()
)
tmnxWppNotifyDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxWppNotifyDescription.setStatus("current")
_TmnxWppNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxWppNotifyPrefix = _TmnxWppNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 80)
)
_TmnxWppNotifications_ObjectIdentity = ObjectIdentity
tmnxWppNotifications = _TmnxWppNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 80, 0)
)
tmnxWppPortalEntry.registerAugmentions(
    ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB",
     "tmnxWppPortalStatEntry")
)
tmnxWppPortalStatEntry.setIndexNames(*tmnxWppPortalEntry.getIndexNames())
tmnxWppPortalGroupEntry.registerAugmentions(
    ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB",
     "tmnxWppPortalGroupStatEntry")
)
tmnxWppPortalGroupStatEntry.setIndexNames(*tmnxWppPortalGroupEntry.getIndexNames())

# Managed Objects groups

tmnxWppGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 80, 2, 1)
)
tmnxWppGroup.setObjects(
      *(("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppRowStatus"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppLastCh"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppAdminState"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppStatsName"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppStatsVal"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalLastCh"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalRowStatus"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalAddrType"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalAddr"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalAdminState"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalStateControlledRtr"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalStateNumInterfaces"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalStatsName"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalStatsVal"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppHostStatus"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppHostSerialNumber"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppHostRequestId"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppHostPortalRemotePort"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppHostPortalLclIpAddrType"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppHostPortalLclIpAddr"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppHostUserName"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppHostService"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppHostMacAddress"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppIfLastCh"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppIfRowStatus"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppIfAdminState"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppIfPortalRouter"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppIfPortalName"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppIfSubProfile"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppIfSLAProfile"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppIfAppProfile"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppIfRestoreDisconnected"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppTableLastCh"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalTableLastCh"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppIfTableLastCh"))
)
if mibBuilder.loadTexts:
    tmnxWppGroup.setStatus("current")

tmnxWppV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 80, 2, 2)
)
tmnxWppV12v0Group.setObjects(
      *(("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalSecret"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalVersion"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppIfUserDb"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppIfLeaseTime"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppIfEnableTriggeredHosts"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppHostIsTriggered"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalStateTriggeredHosts"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppHostTrackSrrpInst"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppHostIsMCBackup"))
)
if mibBuilder.loadTexts:
    tmnxWppV12v0Group.setStatus("current")

tmnxWppNtfLogoutGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 80, 2, 3)
)
tmnxWppNtfLogoutGroup.setObjects(
      *(("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalRetryInterval"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalNtfLogoutRetries"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalAckAuthRetries"))
)
if mibBuilder.loadTexts:
    tmnxWppNtfLogoutGroup.setStatus("current")

tmnxWppV15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 80, 2, 4)
)
tmnxWppV15v0Group.setObjects(
      *(("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalGroupLastCh"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalGroupRowStatus"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalGroupDescription"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalGroupAdminState"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalGroupPortalLastCh"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalGroupPortalRowStat"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppIfPortalGroupName"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalGroupStateContrRtr"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalGroupStateNumItfs"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalGroupStateTrigHosts"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPGHostStatus"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPGHostSerialNumber"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPGHostRequestId"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPGHostPortalRemotePort"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPGHostPortalLclIpAddrType"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPGHostPortalLclIpAddr"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPGHostUserName"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPGHostService"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPGHostMacAddress"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPGHostIsTriggered"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPGHostTrackSrrpInst"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPGHostIsMCBackup"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPGHostActivePortalRouter"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPGHostActivePortalName"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalAckInfoPortFormat"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppSysName"))
)
if mibBuilder.loadTexts:
    tmnxWppV15v0Group.setStatus("current")

tmnxWppV20v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 80, 2, 5)
)
tmnxWppV20v0Group.setObjects(
      *(("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppSessStatus"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppSessSerialNumber"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppSessRequestId"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppSessPortalRemotePort"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppSessPortalLclIpAddrType"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppSessPortalLclIpAddr"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppSessUserName"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppSessService"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppSessMacAddress"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppSessIsTriggered"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppSessTrackSrrpInst"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppSessIsMCBackup"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppSessClientAddrType"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppSessClientAddr"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPGSessStatus"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPGSessSerialNumber"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPGSessRequestId"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPGSessPortalRemotePort"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPGSessPortalLclIpAddrType"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPGSessPortalLclIpAddr"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPGSessUserName"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPGSessService"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPGSessMacAddress"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPGSessIsTriggered"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPGSessTrackSrrpInst"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPGSessIsMCBackup"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPGSessActivePortalRouter"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPGSessActivePortalName"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPGSessClientAddrType"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPGSessClientAddr"))
)
if mibBuilder.loadTexts:
    tmnxWppV20v0Group.setStatus("current")

tmnxWppNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 80, 2, 99)
)
tmnxWppNotifyObjsGroup.setObjects(
    ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppNotifyDescription")
)
if mibBuilder.loadTexts:
    tmnxWppNotifyObjsGroup.setStatus("current")


# Notification objects

tmnxWppPortalStatChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 80, 0, 1)
)
tmnxWppPortalStatChanged.setObjects(
      *(("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalStateControlledRtr"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalStateNumInterfaces"))
)
if mibBuilder.loadTexts:
    tmnxWppPortalStatChanged.setStatus(
        "current"
    )

tmnxWppHostAuthenticationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 80, 0, 2)
)
tmnxWppHostAuthenticationFailed.setObjects(
      *(("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppHostStatus"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxWppHostAuthenticationFailed.setStatus(
        "current"
    )

tmnxWppPortalUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 80, 0, 3)
)
tmnxWppPortalUnreachable.setObjects(
      *(("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalLastCh"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxWppPortalUnreachable.setStatus(
        "current"
    )

tmnxWppPortalGroupStatChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 80, 0, 4)
)
tmnxWppPortalGroupStatChanged.setObjects(
      *(("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalGroupStateContrRtr"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalGroupStateNumItfs"))
)
if mibBuilder.loadTexts:
    tmnxWppPortalGroupStatChanged.setStatus(
        "current"
    )

tmnxWppPGHostAuthFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 80, 0, 5)
)
tmnxWppPGHostAuthFailed.setObjects(
      *(("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPGHostStatus"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxWppPGHostAuthFailed.setStatus(
        "current"
    )


# Notifications groups

tmnxWppNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 80, 2, 100)
)
tmnxWppNotifyGroup.setObjects(
      *(("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalStatChanged"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppHostAuthenticationFailed"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalUnreachable"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPortalGroupStatChanged"))
)
if mibBuilder.loadTexts:
    tmnxWppNotifyGroup.setStatus(
        "current"
    )

tmnxWppNotifyV16v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 80, 2, 101)
)
tmnxWppNotifyV16v0Group.setObjects(
    ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppPGHostAuthFailed")
)
if mibBuilder.loadTexts:
    tmnxWppNotifyV16v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxWppCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 80, 1, 1)
)
tmnxWppCompliance.setObjects(
    ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppGroup")
)
if mibBuilder.loadTexts:
    tmnxWppCompliance.setStatus(
        "obsolete"
    )

tmnxWppNotifyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 80, 1, 2)
)
tmnxWppNotifyCompliance.setObjects(
    ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppNotifyGroup")
)
if mibBuilder.loadTexts:
    tmnxWppNotifyCompliance.setStatus(
        "obsolete"
    )

tmnxWppV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 80, 1, 3)
)
tmnxWppV12v0Compliance.setObjects(
      *(("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppGroup"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppV12v0Group"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppNtfLogoutGroup"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppNotifyGroup"))
)
if mibBuilder.loadTexts:
    tmnxWppV12v0Compliance.setStatus(
        "current"
    )

tmnxWppV15v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 80, 1, 4)
)
tmnxWppV15v0Compliance.setObjects(
      *(("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppGroup"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppV12v0Group"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppV15v0Group"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppNtfLogoutGroup"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppNotifyGroup"))
)
if mibBuilder.loadTexts:
    tmnxWppV15v0Compliance.setStatus(
        "current"
    )

tmnxWppV20v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 80, 1, 5)
)
tmnxWppV20v0Compliance.setObjects(
      *(("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppV20v0Group"),
        ("TIMETRA-WEB-PORTAL-PROTOCOL-MIB", "tmnxWppNotifyV16v0Group"))
)
if mibBuilder.loadTexts:
    tmnxWppV20v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-WEB-PORTAL-PROTOCOL-MIB",
    **{"TmnxWppStatsType": TmnxWppStatsType,
       "TmnxWppUserName": TmnxWppUserName,
       "timetraWppMIBModule": timetraWppMIBModule,
       "tmnxWppConformance": tmnxWppConformance,
       "tmnxWppCompliances": tmnxWppCompliances,
       "tmnxWppCompliance": tmnxWppCompliance,
       "tmnxWppNotifyCompliance": tmnxWppNotifyCompliance,
       "tmnxWppV12v0Compliance": tmnxWppV12v0Compliance,
       "tmnxWppV15v0Compliance": tmnxWppV15v0Compliance,
       "tmnxWppV20v0Compliance": tmnxWppV20v0Compliance,
       "tmnxWppGroups": tmnxWppGroups,
       "tmnxWppGroup": tmnxWppGroup,
       "tmnxWppV12v0Group": tmnxWppV12v0Group,
       "tmnxWppNtfLogoutGroup": tmnxWppNtfLogoutGroup,
       "tmnxWppV15v0Group": tmnxWppV15v0Group,
       "tmnxWppV20v0Group": tmnxWppV20v0Group,
       "tmnxWppNotifyObjsGroup": tmnxWppNotifyObjsGroup,
       "tmnxWppNotifyGroup": tmnxWppNotifyGroup,
       "tmnxWppNotifyV16v0Group": tmnxWppNotifyV16v0Group,
       "tmnxWpp": tmnxWpp,
       "tmnxWppObjs": tmnxWppObjs,
       "tmnxWppPortalObjs": tmnxWppPortalObjs,
       "tmnxWppPortalTable": tmnxWppPortalTable,
       "tmnxWppPortalEntry": tmnxWppPortalEntry,
       "tmnxWppPortalName": tmnxWppPortalName,
       "tmnxWppPortalLastCh": tmnxWppPortalLastCh,
       "tmnxWppPortalRowStatus": tmnxWppPortalRowStatus,
       "tmnxWppPortalAddrType": tmnxWppPortalAddrType,
       "tmnxWppPortalAddr": tmnxWppPortalAddr,
       "tmnxWppPortalAdminState": tmnxWppPortalAdminState,
       "tmnxWppPortalSecret": tmnxWppPortalSecret,
       "tmnxWppPortalVersion": tmnxWppPortalVersion,
       "tmnxWppPortalRetryInterval": tmnxWppPortalRetryInterval,
       "tmnxWppPortalNtfLogoutRetries": tmnxWppPortalNtfLogoutRetries,
       "tmnxWppPortalAckAuthRetries": tmnxWppPortalAckAuthRetries,
       "tmnxWppPortalAckInfoPortFormat": tmnxWppPortalAckInfoPortFormat,
       "tmnxWppPortalStatTable": tmnxWppPortalStatTable,
       "tmnxWppPortalStatEntry": tmnxWppPortalStatEntry,
       "tmnxWppPortalStateControlledRtr": tmnxWppPortalStateControlledRtr,
       "tmnxWppPortalStateNumInterfaces": tmnxWppPortalStateNumInterfaces,
       "tmnxWppPortalStateTriggeredHosts": tmnxWppPortalStateTriggeredHosts,
       "tmnxWppPortalStatsTable": tmnxWppPortalStatsTable,
       "tmnxWppPortalStatsEntry": tmnxWppPortalStatsEntry,
       "tmnxWppPortalStatsType": tmnxWppPortalStatsType,
       "tmnxWppPortalStatsInstance": tmnxWppPortalStatsInstance,
       "tmnxWppPortalStatsName": tmnxWppPortalStatsName,
       "tmnxWppPortalStatsVal": tmnxWppPortalStatsVal,
       "tmnxWppHostTable": tmnxWppHostTable,
       "tmnxWppHostEntry": tmnxWppHostEntry,
       "tmnxWppHostAddrType": tmnxWppHostAddrType,
       "tmnxWppHostAddr": tmnxWppHostAddr,
       "tmnxWppHostStatus": tmnxWppHostStatus,
       "tmnxWppHostSerialNumber": tmnxWppHostSerialNumber,
       "tmnxWppHostRequestId": tmnxWppHostRequestId,
       "tmnxWppHostPortalRemotePort": tmnxWppHostPortalRemotePort,
       "tmnxWppHostPortalLclIpAddrType": tmnxWppHostPortalLclIpAddrType,
       "tmnxWppHostPortalLclIpAddr": tmnxWppHostPortalLclIpAddr,
       "tmnxWppHostUserName": tmnxWppHostUserName,
       "tmnxWppHostService": tmnxWppHostService,
       "tmnxWppHostMacAddress": tmnxWppHostMacAddress,
       "tmnxWppHostIsTriggered": tmnxWppHostIsTriggered,
       "tmnxWppHostTrackSrrpInst": tmnxWppHostTrackSrrpInst,
       "tmnxWppHostIsMCBackup": tmnxWppHostIsMCBackup,
       "tmnxWppSessTable": tmnxWppSessTable,
       "tmnxWppSessEntry": tmnxWppSessEntry,
       "tmnxWppSessStatus": tmnxWppSessStatus,
       "tmnxWppSessSerialNumber": tmnxWppSessSerialNumber,
       "tmnxWppSessRequestId": tmnxWppSessRequestId,
       "tmnxWppSessPortalRemotePort": tmnxWppSessPortalRemotePort,
       "tmnxWppSessPortalLclIpAddrType": tmnxWppSessPortalLclIpAddrType,
       "tmnxWppSessPortalLclIpAddr": tmnxWppSessPortalLclIpAddr,
       "tmnxWppSessUserName": tmnxWppSessUserName,
       "tmnxWppSessService": tmnxWppSessService,
       "tmnxWppSessMacAddress": tmnxWppSessMacAddress,
       "tmnxWppSessIsTriggered": tmnxWppSessIsTriggered,
       "tmnxWppSessTrackSrrpInst": tmnxWppSessTrackSrrpInst,
       "tmnxWppSessIsMCBackup": tmnxWppSessIsMCBackup,
       "tmnxWppSessClientAddrType": tmnxWppSessClientAddrType,
       "tmnxWppSessClientAddr": tmnxWppSessClientAddr,
       "tmnxWppTable": tmnxWppTable,
       "tmnxWppEntry": tmnxWppEntry,
       "tmnxWppRowStatus": tmnxWppRowStatus,
       "tmnxWppLastCh": tmnxWppLastCh,
       "tmnxWppAdminState": tmnxWppAdminState,
       "tmnxWppStatsTable": tmnxWppStatsTable,
       "tmnxWppStatsEntry": tmnxWppStatsEntry,
       "tmnxWppStatsType": tmnxWppStatsType,
       "tmnxWppStatsInstance": tmnxWppStatsInstance,
       "tmnxWppStatsName": tmnxWppStatsName,
       "tmnxWppStatsVal": tmnxWppStatsVal,
       "tmnxWppIfTable": tmnxWppIfTable,
       "tmnxWppIfEntry": tmnxWppIfEntry,
       "tmnxWppIfLastCh": tmnxWppIfLastCh,
       "tmnxWppIfRowStatus": tmnxWppIfRowStatus,
       "tmnxWppIfAdminState": tmnxWppIfAdminState,
       "tmnxWppIfPortalRouter": tmnxWppIfPortalRouter,
       "tmnxWppIfPortalName": tmnxWppIfPortalName,
       "tmnxWppIfSubProfile": tmnxWppIfSubProfile,
       "tmnxWppIfSLAProfile": tmnxWppIfSLAProfile,
       "tmnxWppIfAppProfile": tmnxWppIfAppProfile,
       "tmnxWppIfRestoreDisconnected": tmnxWppIfRestoreDisconnected,
       "tmnxWppIfUserDb": tmnxWppIfUserDb,
       "tmnxWppIfLeaseTime": tmnxWppIfLeaseTime,
       "tmnxWppIfEnableTriggeredHosts": tmnxWppIfEnableTriggeredHosts,
       "tmnxWppIfPortalGroupName": tmnxWppIfPortalGroupName,
       "tmnxWppPortalGroupTable": tmnxWppPortalGroupTable,
       "tmnxWppPortalGroupEntry": tmnxWppPortalGroupEntry,
       "tmnxWppPortalGroupName": tmnxWppPortalGroupName,
       "tmnxWppPortalGroupLastCh": tmnxWppPortalGroupLastCh,
       "tmnxWppPortalGroupRowStatus": tmnxWppPortalGroupRowStatus,
       "tmnxWppPortalGroupDescription": tmnxWppPortalGroupDescription,
       "tmnxWppPortalGroupAdminState": tmnxWppPortalGroupAdminState,
       "tmnxWppPortalGroupPortalTable": tmnxWppPortalGroupPortalTable,
       "tmnxWppPortalGroupPortalEntry": tmnxWppPortalGroupPortalEntry,
       "tmnxWppPortalGroupPortalName": tmnxWppPortalGroupPortalName,
       "tmnxWppPortalGroupPortalLastCh": tmnxWppPortalGroupPortalLastCh,
       "tmnxWppPortalGroupPortalRowStat": tmnxWppPortalGroupPortalRowStat,
       "tmnxWppPortalGroupStatTable": tmnxWppPortalGroupStatTable,
       "tmnxWppPortalGroupStatEntry": tmnxWppPortalGroupStatEntry,
       "tmnxWppPortalGroupStateContrRtr": tmnxWppPortalGroupStateContrRtr,
       "tmnxWppPortalGroupStateNumItfs": tmnxWppPortalGroupStateNumItfs,
       "tmnxWppPortalGroupStateTrigHosts": tmnxWppPortalGroupStateTrigHosts,
       "tmnxWppPGHostTable": tmnxWppPGHostTable,
       "tmnxWppPGHostEntry": tmnxWppPGHostEntry,
       "tmnxWppPGHostAddrType": tmnxWppPGHostAddrType,
       "tmnxWppPGHostAddr": tmnxWppPGHostAddr,
       "tmnxWppPGHostStatus": tmnxWppPGHostStatus,
       "tmnxWppPGHostSerialNumber": tmnxWppPGHostSerialNumber,
       "tmnxWppPGHostRequestId": tmnxWppPGHostRequestId,
       "tmnxWppPGHostPortalRemotePort": tmnxWppPGHostPortalRemotePort,
       "tmnxWppPGHostPortalLclIpAddrType": tmnxWppPGHostPortalLclIpAddrType,
       "tmnxWppPGHostPortalLclIpAddr": tmnxWppPGHostPortalLclIpAddr,
       "tmnxWppPGHostUserName": tmnxWppPGHostUserName,
       "tmnxWppPGHostService": tmnxWppPGHostService,
       "tmnxWppPGHostMacAddress": tmnxWppPGHostMacAddress,
       "tmnxWppPGHostIsTriggered": tmnxWppPGHostIsTriggered,
       "tmnxWppPGHostTrackSrrpInst": tmnxWppPGHostTrackSrrpInst,
       "tmnxWppPGHostIsMCBackup": tmnxWppPGHostIsMCBackup,
       "tmnxWppPGHostActivePortalRouter": tmnxWppPGHostActivePortalRouter,
       "tmnxWppPGHostActivePortalName": tmnxWppPGHostActivePortalName,
       "tmnxWppPGSessTable": tmnxWppPGSessTable,
       "tmnxWppPGSessEntry": tmnxWppPGSessEntry,
       "tmnxWppPGSessStatus": tmnxWppPGSessStatus,
       "tmnxWppPGSessSerialNumber": tmnxWppPGSessSerialNumber,
       "tmnxWppPGSessRequestId": tmnxWppPGSessRequestId,
       "tmnxWppPGSessPortalRemotePort": tmnxWppPGSessPortalRemotePort,
       "tmnxWppPGSessPortalLclIpAddrType": tmnxWppPGSessPortalLclIpAddrType,
       "tmnxWppPGSessPortalLclIpAddr": tmnxWppPGSessPortalLclIpAddr,
       "tmnxWppPGSessUserName": tmnxWppPGSessUserName,
       "tmnxWppPGSessService": tmnxWppPGSessService,
       "tmnxWppPGSessMacAddress": tmnxWppPGSessMacAddress,
       "tmnxWppPGSessIsTriggered": tmnxWppPGSessIsTriggered,
       "tmnxWppPGSessTrackSrrpInst": tmnxWppPGSessTrackSrrpInst,
       "tmnxWppPGSessIsMCBackup": tmnxWppPGSessIsMCBackup,
       "tmnxWppPGSessActivePortalRouter": tmnxWppPGSessActivePortalRouter,
       "tmnxWppPGSessActivePortalName": tmnxWppPGSessActivePortalName,
       "tmnxWppPGSessClientAddrType": tmnxWppPGSessClientAddrType,
       "tmnxWppPGSessClientAddr": tmnxWppPGSessClientAddr,
       "tmnxWppSysObjs": tmnxWppSysObjs,
       "tmnxWppSysName": tmnxWppSysName,
       "tmnxWppTableLastCh": tmnxWppTableLastCh,
       "tmnxWppPortalTableLastCh": tmnxWppPortalTableLastCh,
       "tmnxWppIfTableLastCh": tmnxWppIfTableLastCh,
       "tmnxWppNotificationObjs": tmnxWppNotificationObjs,
       "tmnxWppNotifyDescription": tmnxWppNotifyDescription,
       "tmnxWppNotifyPrefix": tmnxWppNotifyPrefix,
       "tmnxWppNotifications": tmnxWppNotifications,
       "tmnxWppPortalStatChanged": tmnxWppPortalStatChanged,
       "tmnxWppHostAuthenticationFailed": tmnxWppHostAuthenticationFailed,
       "tmnxWppPortalUnreachable": tmnxWppPortalUnreachable,
       "tmnxWppPortalGroupStatChanged": tmnxWppPortalGroupStatChanged,
       "tmnxWppPGHostAuthFailed": tmnxWppPGHostAuthFailed}
)
