# SNMP MIB module (TIMETRA-WLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TIMETRA-WLAN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:01:12 2025
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

(tmnxCardSlotNum,
 tmnxChassisIndex,
 tmnxMDASlotNum) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "tmnxCardSlotNum",
    "tmnxChassisIndex",
    "tmnxMDASlotNum")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(tmnxPortPortID,) = mibBuilder.importSymbols(
    "TIMETRA-PORT-MIB",
    "tmnxPortPortID")

(TPolicyStatementNameOrEmpty,
 TmnxAdminState) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TPolicyStatementNameOrEmpty",
    "TmnxAdminState")


# MODULE-IDENTITY

timetraWlanMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 117)
)
if mibBuilder.loadTexts:
    timetraWlanMIBModule.setRevisions(
        ("2017-07-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxWlanNetworkId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )



class TmnxWlanSSID(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class TmnxWlanWpaPassphrase(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 63),
    )



class TmnxWlanRadioType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("dualbandWifi", 1))
    )



class TmnxWlanRadioAdminStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("outOfService", 2))
    )



class TmnxWlanRadioOperStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("unknown", 0),
          ("down", 1),
          ("scanning", 2),
          ("up", 3))
    )



class TmnxWlanRadioFreqBand(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("band24Ghz", 1),
          ("band50Ghz", 2))
    )



class TmnxWlanRadioChBandwidth(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("width20mhz", 1),
          ("width40mhz", 2))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxWlanConformance_ObjectIdentity = ObjectIdentity
tmnxWlanConformance = _TmnxWlanConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 117)
)
_TmnxWlanCompliances_ObjectIdentity = ObjectIdentity
tmnxWlanCompliances = _TmnxWlanCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 117, 1)
)
_TmnxWlanGroups_ObjectIdentity = ObjectIdentity
tmnxWlanGroups = _TmnxWlanGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 117, 2)
)
_TmnxWlanV15v0Groups_ObjectIdentity = ObjectIdentity
tmnxWlanV15v0Groups = _TmnxWlanV15v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 117, 2, 1)
)
_TmnxWlanV20Groups_ObjectIdentity = ObjectIdentity
tmnxWlanV20Groups = _TmnxWlanV20Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 117, 2, 2)
)
_TmnxWlanObjs_ObjectIdentity = ObjectIdentity
tmnxWlanObjs = _TmnxWlanObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117)
)
_TmnxWlanConfigObjs_ObjectIdentity = ObjectIdentity
tmnxWlanConfigObjs = _TmnxWlanConfigObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 2)
)
_TmnxWlanPortConfigObjs_ObjectIdentity = ObjectIdentity
tmnxWlanPortConfigObjs = _TmnxWlanPortConfigObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 2, 1)
)
_TmnxWlanPortTable_Object = MibTable
tmnxWlanPortTable = _TmnxWlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxWlanPortTable.setStatus("current")
_TmnxWlanPortEntry_Object = MibTableRow
tmnxWlanPortEntry = _TmnxWlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 2, 1, 1, 1)
)
tmnxWlanPortEntry.setIndexNames(
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxWlanPortEntry.setStatus("current")


class _TmnxWlanPortMode_Type(Integer32):
    """Custom type tmnxWlanPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("access-point", 1),
          ("reserved2", 2))
    )


_TmnxWlanPortMode_Type.__name__ = "Integer32"
_TmnxWlanPortMode_Object = MibTableColumn
tmnxWlanPortMode = _TmnxWlanPortMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 2, 1, 1, 1, 1),
    _TmnxWlanPortMode_Type()
)
tmnxWlanPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanPortMode.setStatus("current")
_TmnxWlanPortRadio_Type = Unsigned32
_TmnxWlanPortRadio_Object = MibTableColumn
tmnxWlanPortRadio = _TmnxWlanPortRadio_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 2, 1, 1, 1, 2),
    _TmnxWlanPortRadio_Type()
)
tmnxWlanPortRadio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanPortRadio.setStatus("current")


class _TmnxWlanPortOperFlags_Type(Bits):
    """Custom type tmnxWlanPortOperFlags based on Bits"""
    namedValues = NamedValues(
        *(("adminDown", 0),
          ("rfAdminDown", 1),
          ("rfChNotLocked", 2),
          ("noRadiusPlcyCfg", 3),
          ("dot1xDisabled", 4),
          ("radiusPlcyDisabled", 5),
          ("noRadiusAuthSvr", 6),
          ("noNasIpAddr", 7))
    )

_TmnxWlanPortOperFlags_Type.__name__ = "Bits"
_TmnxWlanPortOperFlags_Object = MibTableColumn
tmnxWlanPortOperFlags = _TmnxWlanPortOperFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 2, 1, 1, 1, 3),
    _TmnxWlanPortOperFlags_Type()
)
tmnxWlanPortOperFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanPortOperFlags.setStatus("current")
_TmnxWlanNetworkTable_Object = MibTable
tmnxWlanNetworkTable = _TmnxWlanNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 2, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxWlanNetworkTable.setStatus("current")
_TmnxWlanNetworkEntry_Object = MibTableRow
tmnxWlanNetworkEntry = _TmnxWlanNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 2, 1, 2, 1)
)
tmnxWlanNetworkEntry.setIndexNames(
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "TIMETRA-WLAN-MIB", "tmnxWlanNetworkId"),
)
if mibBuilder.loadTexts:
    tmnxWlanNetworkEntry.setStatus("current")
_TmnxWlanNetworkId_Type = TmnxWlanNetworkId
_TmnxWlanNetworkId_Object = MibTableColumn
tmnxWlanNetworkId = _TmnxWlanNetworkId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 2, 1, 2, 1, 1),
    _TmnxWlanNetworkId_Type()
)
tmnxWlanNetworkId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanNetworkId.setStatus("current")
_TmnxWlanNetworkRowStatus_Type = RowStatus
_TmnxWlanNetworkRowStatus_Object = MibTableColumn
tmnxWlanNetworkRowStatus = _TmnxWlanNetworkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 2, 1, 2, 1, 2),
    _TmnxWlanNetworkRowStatus_Type()
)
tmnxWlanNetworkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanNetworkRowStatus.setStatus("current")
_TmnxWlanNetworkSSID_Type = TmnxWlanSSID
_TmnxWlanNetworkSSID_Object = MibTableColumn
tmnxWlanNetworkSSID = _TmnxWlanNetworkSSID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 2, 1, 2, 1, 3),
    _TmnxWlanNetworkSSID_Type()
)
tmnxWlanNetworkSSID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanNetworkSSID.setStatus("current")
_TmnxWlanNetworkSecurityTable_Object = MibTable
tmnxWlanNetworkSecurityTable = _TmnxWlanNetworkSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 2, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxWlanNetworkSecurityTable.setStatus("current")
_TmnxWlanNetworkSecurityEntry_Object = MibTableRow
tmnxWlanNetworkSecurityEntry = _TmnxWlanNetworkSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxWlanNetworkSecurityEntry.setStatus("current")


class _TmnxWlanNetworkSecurity_Type(Integer32):
    """Custom type tmnxWlanNetworkSecurity based on Integer32"""
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
        *(("none", 0),
          ("wpa2-psk", 1),
          ("wpa2-enterprise", 2))
    )


_TmnxWlanNetworkSecurity_Type.__name__ = "Integer32"
_TmnxWlanNetworkSecurity_Object = MibTableColumn
tmnxWlanNetworkSecurity = _TmnxWlanNetworkSecurity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 2, 1, 3, 1, 1),
    _TmnxWlanNetworkSecurity_Type()
)
tmnxWlanNetworkSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxWlanNetworkSecurity.setStatus("current")


class _TmnxWlanNetworkWpaEncryption_Type(Integer32):
    """Custom type tmnxWlanNetworkWpaEncryption based on Integer32"""
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
        *(("none", 0),
          ("aes", 1),
          ("tkip", 2))
    )


_TmnxWlanNetworkWpaEncryption_Type.__name__ = "Integer32"
_TmnxWlanNetworkWpaEncryption_Object = MibTableColumn
tmnxWlanNetworkWpaEncryption = _TmnxWlanNetworkWpaEncryption_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 2, 1, 3, 1, 2),
    _TmnxWlanNetworkWpaEncryption_Type()
)
tmnxWlanNetworkWpaEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxWlanNetworkWpaEncryption.setStatus("current")


class _TmnxWlanNetworkWpaPassphrase_Type(TmnxWlanWpaPassphrase):
    """Custom type tmnxWlanNetworkWpaPassphrase based on TmnxWlanWpaPassphrase"""
    defaultValue = OctetString("")


_TmnxWlanNetworkWpaPassphrase_Type.__name__ = "TmnxWlanWpaPassphrase"
_TmnxWlanNetworkWpaPassphrase_Object = MibTableColumn
tmnxWlanNetworkWpaPassphrase = _TmnxWlanNetworkWpaPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 2, 1, 3, 1, 3),
    _TmnxWlanNetworkWpaPassphrase_Type()
)
tmnxWlanNetworkWpaPassphrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxWlanNetworkWpaPassphrase.setStatus("current")
_TmnxWlanAPTable_Object = MibTable
tmnxWlanAPTable = _TmnxWlanAPTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 2, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxWlanAPTable.setStatus("current")
_TmnxWlanAPEntry_Object = MibTableRow
tmnxWlanAPEntry = _TmnxWlanAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 2, 1, 4, 1)
)
tmnxWlanAPEntry.setIndexNames(
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxWlanAPEntry.setStatus("current")


class _TmnxWlanAPBroadcastSSID_Type(TruthValue):
    """Custom type tmnxWlanAPBroadcastSSID based on TruthValue"""
    defaultValue = 1


_TmnxWlanAPBroadcastSSID_Type.__name__ = "TruthValue"
_TmnxWlanAPBroadcastSSID_Object = MibTableColumn
tmnxWlanAPBroadcastSSID = _TmnxWlanAPBroadcastSSID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 2, 1, 4, 1, 1),
    _TmnxWlanAPBroadcastSSID_Type()
)
tmnxWlanAPBroadcastSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxWlanAPBroadcastSSID.setStatus("current")


class _TmnxWlanAPClientLimit_Type(Unsigned32):
    """Custom type tmnxWlanAPClientLimit based on Unsigned32"""
    defaultValue = 24

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_TmnxWlanAPClientLimit_Type.__name__ = "Unsigned32"
_TmnxWlanAPClientLimit_Object = MibTableColumn
tmnxWlanAPClientLimit = _TmnxWlanAPClientLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 2, 1, 4, 1, 2),
    _TmnxWlanAPClientLimit_Type()
)
tmnxWlanAPClientLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxWlanAPClientLimit.setStatus("current")


class _TmnxWlanAPClientTimeout_Type(Unsigned32):
    """Custom type tmnxWlanAPClientTimeout based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_TmnxWlanAPClientTimeout_Type.__name__ = "Unsigned32"
_TmnxWlanAPClientTimeout_Object = MibTableColumn
tmnxWlanAPClientTimeout = _TmnxWlanAPClientTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 2, 1, 4, 1, 3),
    _TmnxWlanAPClientTimeout_Type()
)
tmnxWlanAPClientTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxWlanAPClientTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanAPClientTimeout.setUnits("seconds")


class _TmnxWlanAPDot1xRadiusPlcy_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxWlanAPDot1xRadiusPlcy based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_TmnxWlanAPDot1xRadiusPlcy_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxWlanAPDot1xRadiusPlcy_Object = MibTableColumn
tmnxWlanAPDot1xRadiusPlcy = _TmnxWlanAPDot1xRadiusPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 2, 1, 4, 1, 4),
    _TmnxWlanAPDot1xRadiusPlcy_Type()
)
tmnxWlanAPDot1xRadiusPlcy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxWlanAPDot1xRadiusPlcy.setStatus("current")


class _TmnxWlanAPDot1xReauthPeriod_Type(Unsigned32):
    """Custom type tmnxWlanAPDot1xReauthPeriod based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9000),
    )


_TmnxWlanAPDot1xReauthPeriod_Type.__name__ = "Unsigned32"
_TmnxWlanAPDot1xReauthPeriod_Object = MibTableColumn
tmnxWlanAPDot1xReauthPeriod = _TmnxWlanAPDot1xReauthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 2, 1, 4, 1, 5),
    _TmnxWlanAPDot1xReauthPeriod_Type()
)
tmnxWlanAPDot1xReauthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxWlanAPDot1xReauthPeriod.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanAPDot1xReauthPeriod.setUnits("seconds")


class _TmnxWlanAPDhcpAdminState_Type(TmnxAdminState):
    """Custom type tmnxWlanAPDhcpAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxWlanAPDhcpAdminState_Type.__name__ = "TmnxAdminState"
_TmnxWlanAPDhcpAdminState_Object = MibTableColumn
tmnxWlanAPDhcpAdminState = _TmnxWlanAPDhcpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 2, 1, 4, 1, 6),
    _TmnxWlanAPDhcpAdminState_Type()
)
tmnxWlanAPDhcpAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxWlanAPDhcpAdminState.setStatus("current")
_TmnxWlanCardConfigObjs_ObjectIdentity = ObjectIdentity
tmnxWlanCardConfigObjs = _TmnxWlanCardConfigObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 2, 2)
)
_TmnxWlanRadioTable_Object = MibTable
tmnxWlanRadioTable = _TmnxWlanRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxWlanRadioTable.setStatus("current")
_TmnxWlanRadioEntry_Object = MibTableRow
tmnxWlanRadioEntry = _TmnxWlanRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 2, 2, 1, 1)
)
tmnxWlanRadioEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
    (0, "TIMETRA-WLAN-MIB", "tmnxMDARadioNum"),
)
if mibBuilder.loadTexts:
    tmnxWlanRadioEntry.setStatus("current")
_TmnxMDARadioNum_Type = Unsigned32
_TmnxMDARadioNum_Object = MibTableColumn
tmnxMDARadioNum = _TmnxMDARadioNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 2, 2, 1, 1, 1),
    _TmnxMDARadioNum_Type()
)
tmnxMDARadioNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMDARadioNum.setStatus("current")
_TmnxWlanRadioType_Type = TmnxWlanRadioType
_TmnxWlanRadioType_Object = MibTableColumn
tmnxWlanRadioType = _TmnxWlanRadioType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 2, 2, 1, 1, 2),
    _TmnxWlanRadioType_Type()
)
tmnxWlanRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanRadioType.setStatus("current")


class _TmnxWlanRadioAdminStatus_Type(TmnxWlanRadioAdminStatus):
    """Custom type tmnxWlanRadioAdminStatus based on TmnxWlanRadioAdminStatus"""
    defaultValue = 2


_TmnxWlanRadioAdminStatus_Type.__name__ = "TmnxWlanRadioAdminStatus"
_TmnxWlanRadioAdminStatus_Object = MibTableColumn
tmnxWlanRadioAdminStatus = _TmnxWlanRadioAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 2, 2, 1, 1, 3),
    _TmnxWlanRadioAdminStatus_Type()
)
tmnxWlanRadioAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxWlanRadioAdminStatus.setStatus("current")


class _TmnxWlanRadioCountry_Type(Integer32):
    """Custom type tmnxWlanRadioCountry based on Integer32"""
    defaultValue = 0

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
              22)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("australia", 1),
          ("belgium", 2),
          ("bolivia", 3),
          ("brazil", 4),
          ("canada", 5),
          ("chile", 6),
          ("colombia", 7),
          ("france", 8),
          ("germany", 9),
          ("india", 10),
          ("iran", 11),
          ("italy", 12),
          ("japan", 13),
          ("malaysia", 14),
          ("mexico", 15),
          ("newZealand", 16),
          ("peru", 17),
          ("russia", 18),
          ("singapore", 19),
          ("southAfrica", 20),
          ("usa", 21),
          ("venezuela", 22))
    )


_TmnxWlanRadioCountry_Type.__name__ = "Integer32"
_TmnxWlanRadioCountry_Object = MibTableColumn
tmnxWlanRadioCountry = _TmnxWlanRadioCountry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 2, 2, 1, 1, 4),
    _TmnxWlanRadioCountry_Type()
)
tmnxWlanRadioCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxWlanRadioCountry.setStatus("current")


class _TmnxWlanRadioCfgFreqBand_Type(TmnxWlanRadioFreqBand):
    """Custom type tmnxWlanRadioCfgFreqBand based on TmnxWlanRadioFreqBand"""
    defaultValue = 1


_TmnxWlanRadioCfgFreqBand_Type.__name__ = "TmnxWlanRadioFreqBand"
_TmnxWlanRadioCfgFreqBand_Object = MibTableColumn
tmnxWlanRadioCfgFreqBand = _TmnxWlanRadioCfgFreqBand_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 2, 2, 1, 1, 5),
    _TmnxWlanRadioCfgFreqBand_Type()
)
tmnxWlanRadioCfgFreqBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxWlanRadioCfgFreqBand.setStatus("current")


class _TmnxWlanRadioCfgChannel_Type(Unsigned32):
    """Custom type tmnxWlanRadioCfgChannel based on Unsigned32"""
    defaultValue = 0


_TmnxWlanRadioCfgChannel_Type.__name__ = "Unsigned32"
_TmnxWlanRadioCfgChannel_Object = MibTableColumn
tmnxWlanRadioCfgChannel = _TmnxWlanRadioCfgChannel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 2, 2, 1, 1, 6),
    _TmnxWlanRadioCfgChannel_Type()
)
tmnxWlanRadioCfgChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxWlanRadioCfgChannel.setStatus("current")


class _TmnxWlanRadioCfgChBandwidth_Type(TmnxWlanRadioChBandwidth):
    """Custom type tmnxWlanRadioCfgChBandwidth based on TmnxWlanRadioChBandwidth"""
    defaultValue = 1


_TmnxWlanRadioCfgChBandwidth_Type.__name__ = "TmnxWlanRadioChBandwidth"
_TmnxWlanRadioCfgChBandwidth_Object = MibTableColumn
tmnxWlanRadioCfgChBandwidth = _TmnxWlanRadioCfgChBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 2, 2, 1, 1, 7),
    _TmnxWlanRadioCfgChBandwidth_Type()
)
tmnxWlanRadioCfgChBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxWlanRadioCfgChBandwidth.setStatus("current")


class _TmnxWlanRadioApBeaconInterval_Type(Unsigned32):
    """Custom type tmnxWlanRadioApBeaconInterval based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(75, 999),
    )


_TmnxWlanRadioApBeaconInterval_Type.__name__ = "Unsigned32"
_TmnxWlanRadioApBeaconInterval_Object = MibTableColumn
tmnxWlanRadioApBeaconInterval = _TmnxWlanRadioApBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 2, 2, 1, 1, 8),
    _TmnxWlanRadioApBeaconInterval_Type()
)
tmnxWlanRadioApBeaconInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxWlanRadioApBeaconInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanRadioApBeaconInterval.setUnits("msecs")
_TmnxWlanOperObjs_ObjectIdentity = ObjectIdentity
tmnxWlanOperObjs = _TmnxWlanOperObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 3)
)
_TmnxWlanRadioOperTable_Object = MibTable
tmnxWlanRadioOperTable = _TmnxWlanRadioOperTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 3, 2)
)
if mibBuilder.loadTexts:
    tmnxWlanRadioOperTable.setStatus("current")
_TmnxWlanRadioOperEntry_Object = MibTableRow
tmnxWlanRadioOperEntry = _TmnxWlanRadioOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 3, 2, 1)
)
tmnxWlanRadioOperEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
    (0, "TIMETRA-WLAN-MIB", "tmnxMDARadioNum"),
)
if mibBuilder.loadTexts:
    tmnxWlanRadioOperEntry.setStatus("current")
_TmnxWlanRadioOperStatus_Type = TmnxWlanRadioOperStatus
_TmnxWlanRadioOperStatus_Object = MibTableColumn
tmnxWlanRadioOperStatus = _TmnxWlanRadioOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 3, 2, 1, 1),
    _TmnxWlanRadioOperStatus_Type()
)
tmnxWlanRadioOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanRadioOperStatus.setStatus("current")
_TmnxWlanRadioOperFreqBand_Type = TmnxWlanRadioFreqBand
_TmnxWlanRadioOperFreqBand_Object = MibTableColumn
tmnxWlanRadioOperFreqBand = _TmnxWlanRadioOperFreqBand_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 3, 2, 1, 2),
    _TmnxWlanRadioOperFreqBand_Type()
)
tmnxWlanRadioOperFreqBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanRadioOperFreqBand.setStatus("current")
_TmnxWlanRadioOperChannel_Type = Unsigned32
_TmnxWlanRadioOperChannel_Object = MibTableColumn
tmnxWlanRadioOperChannel = _TmnxWlanRadioOperChannel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 3, 2, 1, 3),
    _TmnxWlanRadioOperChannel_Type()
)
tmnxWlanRadioOperChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanRadioOperChannel.setStatus("current")
_TmnxWlanRadioOperChBandwidth_Type = TmnxWlanRadioChBandwidth
_TmnxWlanRadioOperChBandwidth_Object = MibTableColumn
tmnxWlanRadioOperChBandwidth = _TmnxWlanRadioOperChBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 3, 2, 1, 4),
    _TmnxWlanRadioOperChBandwidth_Type()
)
tmnxWlanRadioOperChBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanRadioOperChBandwidth.setStatus("current")
_TmnxWlanRadioOperCentreFreq_Type = Unsigned32
_TmnxWlanRadioOperCentreFreq_Object = MibTableColumn
tmnxWlanRadioOperCentreFreq = _TmnxWlanRadioOperCentreFreq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 3, 2, 1, 5),
    _TmnxWlanRadioOperCentreFreq_Type()
)
tmnxWlanRadioOperCentreFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanRadioOperCentreFreq.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanRadioOperCentreFreq.setUnits("MHz")
_TmnxWlanAPOperTable_Object = MibTable
tmnxWlanAPOperTable = _TmnxWlanAPOperTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 3, 3)
)
if mibBuilder.loadTexts:
    tmnxWlanAPOperTable.setStatus("current")
_TmnxWlanAPOperEntry_Object = MibTableRow
tmnxWlanAPOperEntry = _TmnxWlanAPOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 3, 3, 1)
)
tmnxWlanAPOperEntry.setIndexNames(
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxWlanAPOperEntry.setStatus("current")
_TmnxWlanAPConnectedClients_Type = Unsigned32
_TmnxWlanAPConnectedClients_Object = MibTableColumn
tmnxWlanAPConnectedClients = _TmnxWlanAPConnectedClients_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 3, 3, 1, 1),
    _TmnxWlanAPConnectedClients_Type()
)
tmnxWlanAPConnectedClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanAPConnectedClients.setStatus("current")
_TmnxWlanAPTotalAttaches_Type = Counter64
_TmnxWlanAPTotalAttaches_Object = MibTableColumn
tmnxWlanAPTotalAttaches = _TmnxWlanAPTotalAttaches_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 3, 3, 1, 2),
    _TmnxWlanAPTotalAttaches_Type()
)
tmnxWlanAPTotalAttaches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanAPTotalAttaches.setStatus("current")
_TmnxWlanAPTotalDetaches_Type = Counter64
_TmnxWlanAPTotalDetaches_Object = MibTableColumn
tmnxWlanAPTotalDetaches = _TmnxWlanAPTotalDetaches_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 3, 3, 1, 3),
    _TmnxWlanAPTotalDetaches_Type()
)
tmnxWlanAPTotalDetaches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanAPTotalDetaches.setStatus("current")
_TmnxWlanAPTotalAuthSuccess_Type = Counter64
_TmnxWlanAPTotalAuthSuccess_Object = MibTableColumn
tmnxWlanAPTotalAuthSuccess = _TmnxWlanAPTotalAuthSuccess_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 3, 3, 1, 4),
    _TmnxWlanAPTotalAuthSuccess_Type()
)
tmnxWlanAPTotalAuthSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanAPTotalAuthSuccess.setStatus("current")
_TmnxWlanAPTotalAuthFails_Type = Counter64
_TmnxWlanAPTotalAuthFails_Object = MibTableColumn
tmnxWlanAPTotalAuthFails = _TmnxWlanAPTotalAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 3, 3, 1, 5),
    _TmnxWlanAPTotalAuthFails_Type()
)
tmnxWlanAPTotalAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanAPTotalAuthFails.setStatus("current")
_TmnxWlanAPClientTable_Object = MibTable
tmnxWlanAPClientTable = _TmnxWlanAPClientTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 3, 4)
)
if mibBuilder.loadTexts:
    tmnxWlanAPClientTable.setStatus("current")
_TmnxWlanAPClientEntry_Object = MibTableRow
tmnxWlanAPClientEntry = _TmnxWlanAPClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 3, 4, 1)
)
tmnxWlanAPClientEntry.setIndexNames(
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "TIMETRA-WLAN-MIB", "tmnxWlanAPClientMacAddress"),
)
if mibBuilder.loadTexts:
    tmnxWlanAPClientEntry.setStatus("current")
_TmnxWlanAPClientMacAddress_Type = MacAddress
_TmnxWlanAPClientMacAddress_Object = MibTableColumn
tmnxWlanAPClientMacAddress = _TmnxWlanAPClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 3, 4, 1, 1),
    _TmnxWlanAPClientMacAddress_Type()
)
tmnxWlanAPClientMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanAPClientMacAddress.setStatus("current")
_TmnxWlanAPClientConnectTime_Type = TimeStamp
_TmnxWlanAPClientConnectTime_Object = MibTableColumn
tmnxWlanAPClientConnectTime = _TmnxWlanAPClientConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 3, 4, 1, 2),
    _TmnxWlanAPClientConnectTime_Type()
)
tmnxWlanAPClientConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanAPClientConnectTime.setStatus("current")
_TmnxWlanAPClientAuthorized_Type = TruthValue
_TmnxWlanAPClientAuthorized_Object = MibTableColumn
tmnxWlanAPClientAuthorized = _TmnxWlanAPClientAuthorized_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 117, 3, 4, 1, 3),
    _TmnxWlanAPClientAuthorized_Type()
)
tmnxWlanAPClientAuthorized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanAPClientAuthorized.setStatus("current")
_TmnxWlanNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxWlanNotifyPrefix = _TmnxWlanNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 117)
)
_TmnxWlanNotifications_ObjectIdentity = ObjectIdentity
tmnxWlanNotifications = _TmnxWlanNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 117, 0)
)
tmnxWlanNetworkEntry.registerAugmentions(
    ("TIMETRA-WLAN-MIB",
     "tmnxWlanNetworkSecurityEntry")
)
tmnxWlanNetworkSecurityEntry.setIndexNames(*tmnxWlanNetworkEntry.getIndexNames())

# Managed Objects groups

tmnxWlanConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 117, 2, 1, 1)
)
tmnxWlanConfigGroup.setObjects(
      *(("TIMETRA-WLAN-MIB", "tmnxWlanPortMode"),
        ("TIMETRA-WLAN-MIB", "tmnxWlanPortRadio"),
        ("TIMETRA-WLAN-MIB", "tmnxWlanPortOperFlags"),
        ("TIMETRA-WLAN-MIB", "tmnxWlanNetworkRowStatus"),
        ("TIMETRA-WLAN-MIB", "tmnxWlanNetworkSSID"),
        ("TIMETRA-WLAN-MIB", "tmnxWlanNetworkSecurity"),
        ("TIMETRA-WLAN-MIB", "tmnxWlanNetworkWpaEncryption"),
        ("TIMETRA-WLAN-MIB", "tmnxWlanNetworkWpaPassphrase"),
        ("TIMETRA-WLAN-MIB", "tmnxWlanAPBroadcastSSID"),
        ("TIMETRA-WLAN-MIB", "tmnxWlanAPClientLimit"),
        ("TIMETRA-WLAN-MIB", "tmnxWlanAPClientTimeout"),
        ("TIMETRA-WLAN-MIB", "tmnxWlanAPDot1xRadiusPlcy"),
        ("TIMETRA-WLAN-MIB", "tmnxWlanAPDot1xReauthPeriod"),
        ("TIMETRA-WLAN-MIB", "tmnxWlanAPDhcpAdminState"),
        ("TIMETRA-WLAN-MIB", "tmnxWlanRadioType"),
        ("TIMETRA-WLAN-MIB", "tmnxWlanRadioAdminStatus"),
        ("TIMETRA-WLAN-MIB", "tmnxWlanRadioCfgChBandwidth"),
        ("TIMETRA-WLAN-MIB", "tmnxWlanRadioCfgChannel"),
        ("TIMETRA-WLAN-MIB", "tmnxWlanRadioCountry"),
        ("TIMETRA-WLAN-MIB", "tmnxWlanRadioCfgFreqBand"),
        ("TIMETRA-WLAN-MIB", "tmnxWlanRadioApBeaconInterval"))
)
if mibBuilder.loadTexts:
    tmnxWlanConfigGroup.setStatus("current")

tmnxWlanOperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 117, 2, 1, 2)
)
tmnxWlanOperGroup.setObjects(
      *(("TIMETRA-WLAN-MIB", "tmnxWlanAPConnectedClients"),
        ("TIMETRA-WLAN-MIB", "tmnxWlanAPTotalAttaches"),
        ("TIMETRA-WLAN-MIB", "tmnxWlanAPTotalDetaches"),
        ("TIMETRA-WLAN-MIB", "tmnxWlanAPTotalAuthSuccess"),
        ("TIMETRA-WLAN-MIB", "tmnxWlanAPTotalAuthFails"),
        ("TIMETRA-WLAN-MIB", "tmnxWlanRadioOperStatus"),
        ("TIMETRA-WLAN-MIB", "tmnxWlanRadioOperChBandwidth"),
        ("TIMETRA-WLAN-MIB", "tmnxWlanRadioOperChannel"),
        ("TIMETRA-WLAN-MIB", "tmnxWlanRadioOperFreqBand"),
        ("TIMETRA-WLAN-MIB", "tmnxWlanAPClientConnectTime"),
        ("TIMETRA-WLAN-MIB", "tmnxWlanAPClientAuthorized"),
        ("TIMETRA-WLAN-MIB", "tmnxWlanRadioOperCentreFreq"))
)
if mibBuilder.loadTexts:
    tmnxWlanOperGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tmnxWlanrCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 117, 1, 1)
)
tmnxWlanrCompliance.setObjects(
      *(("TIMETRA-WLAN-MIB", "tmnxWlanConfigGroup"),
        ("TIMETRA-WLAN-MIB", "tmnxWlanOperGroup"))
)
if mibBuilder.loadTexts:
    tmnxWlanrCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-WLAN-MIB",
    **{"TmnxWlanNetworkId": TmnxWlanNetworkId,
       "TmnxWlanSSID": TmnxWlanSSID,
       "TmnxWlanWpaPassphrase": TmnxWlanWpaPassphrase,
       "TmnxWlanRadioType": TmnxWlanRadioType,
       "TmnxWlanRadioAdminStatus": TmnxWlanRadioAdminStatus,
       "TmnxWlanRadioOperStatus": TmnxWlanRadioOperStatus,
       "TmnxWlanRadioFreqBand": TmnxWlanRadioFreqBand,
       "TmnxWlanRadioChBandwidth": TmnxWlanRadioChBandwidth,
       "timetraWlanMIBModule": timetraWlanMIBModule,
       "tmnxWlanConformance": tmnxWlanConformance,
       "tmnxWlanCompliances": tmnxWlanCompliances,
       "tmnxWlanrCompliance": tmnxWlanrCompliance,
       "tmnxWlanGroups": tmnxWlanGroups,
       "tmnxWlanV15v0Groups": tmnxWlanV15v0Groups,
       "tmnxWlanConfigGroup": tmnxWlanConfigGroup,
       "tmnxWlanOperGroup": tmnxWlanOperGroup,
       "tmnxWlanV20Groups": tmnxWlanV20Groups,
       "tmnxWlanObjs": tmnxWlanObjs,
       "tmnxWlanConfigObjs": tmnxWlanConfigObjs,
       "tmnxWlanPortConfigObjs": tmnxWlanPortConfigObjs,
       "tmnxWlanPortTable": tmnxWlanPortTable,
       "tmnxWlanPortEntry": tmnxWlanPortEntry,
       "tmnxWlanPortMode": tmnxWlanPortMode,
       "tmnxWlanPortRadio": tmnxWlanPortRadio,
       "tmnxWlanPortOperFlags": tmnxWlanPortOperFlags,
       "tmnxWlanNetworkTable": tmnxWlanNetworkTable,
       "tmnxWlanNetworkEntry": tmnxWlanNetworkEntry,
       "tmnxWlanNetworkId": tmnxWlanNetworkId,
       "tmnxWlanNetworkRowStatus": tmnxWlanNetworkRowStatus,
       "tmnxWlanNetworkSSID": tmnxWlanNetworkSSID,
       "tmnxWlanNetworkSecurityTable": tmnxWlanNetworkSecurityTable,
       "tmnxWlanNetworkSecurityEntry": tmnxWlanNetworkSecurityEntry,
       "tmnxWlanNetworkSecurity": tmnxWlanNetworkSecurity,
       "tmnxWlanNetworkWpaEncryption": tmnxWlanNetworkWpaEncryption,
       "tmnxWlanNetworkWpaPassphrase": tmnxWlanNetworkWpaPassphrase,
       "tmnxWlanAPTable": tmnxWlanAPTable,
       "tmnxWlanAPEntry": tmnxWlanAPEntry,
       "tmnxWlanAPBroadcastSSID": tmnxWlanAPBroadcastSSID,
       "tmnxWlanAPClientLimit": tmnxWlanAPClientLimit,
       "tmnxWlanAPClientTimeout": tmnxWlanAPClientTimeout,
       "tmnxWlanAPDot1xRadiusPlcy": tmnxWlanAPDot1xRadiusPlcy,
       "tmnxWlanAPDot1xReauthPeriod": tmnxWlanAPDot1xReauthPeriod,
       "tmnxWlanAPDhcpAdminState": tmnxWlanAPDhcpAdminState,
       "tmnxWlanCardConfigObjs": tmnxWlanCardConfigObjs,
       "tmnxWlanRadioTable": tmnxWlanRadioTable,
       "tmnxWlanRadioEntry": tmnxWlanRadioEntry,
       "tmnxMDARadioNum": tmnxMDARadioNum,
       "tmnxWlanRadioType": tmnxWlanRadioType,
       "tmnxWlanRadioAdminStatus": tmnxWlanRadioAdminStatus,
       "tmnxWlanRadioCountry": tmnxWlanRadioCountry,
       "tmnxWlanRadioCfgFreqBand": tmnxWlanRadioCfgFreqBand,
       "tmnxWlanRadioCfgChannel": tmnxWlanRadioCfgChannel,
       "tmnxWlanRadioCfgChBandwidth": tmnxWlanRadioCfgChBandwidth,
       "tmnxWlanRadioApBeaconInterval": tmnxWlanRadioApBeaconInterval,
       "tmnxWlanOperObjs": tmnxWlanOperObjs,
       "tmnxWlanRadioOperTable": tmnxWlanRadioOperTable,
       "tmnxWlanRadioOperEntry": tmnxWlanRadioOperEntry,
       "tmnxWlanRadioOperStatus": tmnxWlanRadioOperStatus,
       "tmnxWlanRadioOperFreqBand": tmnxWlanRadioOperFreqBand,
       "tmnxWlanRadioOperChannel": tmnxWlanRadioOperChannel,
       "tmnxWlanRadioOperChBandwidth": tmnxWlanRadioOperChBandwidth,
       "tmnxWlanRadioOperCentreFreq": tmnxWlanRadioOperCentreFreq,
       "tmnxWlanAPOperTable": tmnxWlanAPOperTable,
       "tmnxWlanAPOperEntry": tmnxWlanAPOperEntry,
       "tmnxWlanAPConnectedClients": tmnxWlanAPConnectedClients,
       "tmnxWlanAPTotalAttaches": tmnxWlanAPTotalAttaches,
       "tmnxWlanAPTotalDetaches": tmnxWlanAPTotalDetaches,
       "tmnxWlanAPTotalAuthSuccess": tmnxWlanAPTotalAuthSuccess,
       "tmnxWlanAPTotalAuthFails": tmnxWlanAPTotalAuthFails,
       "tmnxWlanAPClientTable": tmnxWlanAPClientTable,
       "tmnxWlanAPClientEntry": tmnxWlanAPClientEntry,
       "tmnxWlanAPClientMacAddress": tmnxWlanAPClientMacAddress,
       "tmnxWlanAPClientConnectTime": tmnxWlanAPClientConnectTime,
       "tmnxWlanAPClientAuthorized": tmnxWlanAPClientAuthorized,
       "tmnxWlanNotifyPrefix": tmnxWlanNotifyPrefix,
       "tmnxWlanNotifications": tmnxWlanNotifications}
)
