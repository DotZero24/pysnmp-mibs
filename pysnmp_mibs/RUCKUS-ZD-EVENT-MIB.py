# SNMP MIB module (RUCKUS-ZD-EVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ruckus/RUCKUS-ZD-EVENT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:13:46 2025
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(ruckusEvents,) = mibBuilder.importSymbols(
    "RUCKUS-ROOT-MIB",
    "ruckusEvents")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ruckusZDEventMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuckusZDEventTraps_ObjectIdentity = ObjectIdentity
ruckusZDEventTraps = _RuckusZDEventTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1)
)
_RuckusZDEventObjects_ObjectIdentity = ObjectIdentity
ruckusZDEventObjects = _RuckusZDEventObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 2)
)
_RuckusZDEventSerial_Type = OctetString
_RuckusZDEventSerial_Object = MibScalar
ruckusZDEventSerial = _RuckusZDEventSerial_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 2, 1),
    _RuckusZDEventSerial_Type()
)
ruckusZDEventSerial.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusZDEventSerial.setStatus("current")
_RuckusZDEventNEID_Type = OctetString
_RuckusZDEventNEID_Object = MibScalar
ruckusZDEventNEID = _RuckusZDEventNEID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 2, 2),
    _RuckusZDEventNEID_Type()
)
ruckusZDEventNEID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusZDEventNEID.setStatus("current")
_RuckusZDEventSeverity_Type = OctetString
_RuckusZDEventSeverity_Object = MibScalar
ruckusZDEventSeverity = _RuckusZDEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 2, 3),
    _RuckusZDEventSeverity_Type()
)
ruckusZDEventSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusZDEventSeverity.setStatus("current")
_RuckusZDEventType_Type = OctetString
_RuckusZDEventType_Object = MibScalar
ruckusZDEventType = _RuckusZDEventType_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 2, 4),
    _RuckusZDEventType_Type()
)
ruckusZDEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusZDEventType.setStatus("current")
_RuckusZDEventTime_Type = OctetString
_RuckusZDEventTime_Object = MibScalar
ruckusZDEventTime = _RuckusZDEventTime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 2, 5),
    _RuckusZDEventTime_Type()
)
ruckusZDEventTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusZDEventTime.setStatus("current")


class _RuckusZDEventStatus_Type(Integer32):
    """Custom type ruckusZDEventStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("raise", 1),
          ("clear", 2))
    )


_RuckusZDEventStatus_Type.__name__ = "Integer32"
_RuckusZDEventStatus_Object = MibScalar
ruckusZDEventStatus = _RuckusZDEventStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 2, 6),
    _RuckusZDEventStatus_Type()
)
ruckusZDEventStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusZDEventStatus.setStatus("current")
_RuckusZDEventTitle_Type = OctetString
_RuckusZDEventTitle_Object = MibScalar
ruckusZDEventTitle = _RuckusZDEventTitle_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 2, 7),
    _RuckusZDEventTitle_Type()
)
ruckusZDEventTitle.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusZDEventTitle.setStatus("current")
_RuckusZDEventContent_Type = OctetString
_RuckusZDEventContent_Object = MibScalar
ruckusZDEventContent = _RuckusZDEventContent_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 2, 8),
    _RuckusZDEventContent_Type()
)
ruckusZDEventContent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusZDEventContent.setStatus("current")
_RuckusZDEventClientMacAddr_Type = OctetString
_RuckusZDEventClientMacAddr_Object = MibScalar
ruckusZDEventClientMacAddr = _RuckusZDEventClientMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 2, 15),
    _RuckusZDEventClientMacAddr_Type()
)
ruckusZDEventClientMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusZDEventClientMacAddr.setStatus("current")
_RuckusZDEventAPMacAddr_Type = OctetString
_RuckusZDEventAPMacAddr_Object = MibScalar
ruckusZDEventAPMacAddr = _RuckusZDEventAPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 2, 18),
    _RuckusZDEventAPMacAddr_Type()
)
ruckusZDEventAPMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusZDEventAPMacAddr.setStatus("current")
_RuckusZDEventRogueMacAddr_Type = OctetString
_RuckusZDEventRogueMacAddr_Object = MibScalar
ruckusZDEventRogueMacAddr = _RuckusZDEventRogueMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 2, 20),
    _RuckusZDEventRogueMacAddr_Type()
)
ruckusZDEventRogueMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusZDEventRogueMacAddr.setStatus("current")
_RuckusZDEventSSID_Type = OctetString
_RuckusZDEventSSID_Object = MibScalar
ruckusZDEventSSID = _RuckusZDEventSSID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 2, 23),
    _RuckusZDEventSSID_Type()
)
ruckusZDEventSSID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusZDEventSSID.setStatus("current")
_RuckusZDEventChannel_Type = Unsigned32
_RuckusZDEventChannel_Object = MibScalar
ruckusZDEventChannel = _RuckusZDEventChannel_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 2, 25),
    _RuckusZDEventChannel_Type()
)
ruckusZDEventChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusZDEventChannel.setStatus("current")
_RuckusZDEventReason_Type = OctetString
_RuckusZDEventReason_Object = MibScalar
ruckusZDEventReason = _RuckusZDEventReason_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 2, 28),
    _RuckusZDEventReason_Type()
)
ruckusZDEventReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusZDEventReason.setStatus("current")
_RuckusZDEventIpAddr_Type = OctetString
_RuckusZDEventIpAddr_Object = MibScalar
ruckusZDEventIpAddr = _RuckusZDEventIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 2, 30),
    _RuckusZDEventIpAddr_Type()
)
ruckusZDEventIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusZDEventIpAddr.setStatus("current")
_RuckusZDEventTrapSwitchCmd_ObjectIdentity = ObjectIdentity
ruckusZDEventTrapSwitchCmd = _RuckusZDEventTrapSwitchCmd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3)
)


class _RuckusZDEventAPJoinTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventAPJoinTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventAPJoinTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventAPJoinTrapSwitchCmd_Object = MibScalar
ruckusZDEventAPJoinTrapSwitchCmd = _RuckusZDEventAPJoinTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 1),
    _RuckusZDEventAPJoinTrapSwitchCmd_Type()
)
ruckusZDEventAPJoinTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventAPJoinTrapSwitchCmd.setStatus("current")


class _RuckusZDEventSSIDSpoofTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventSSIDSpoofTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventSSIDSpoofTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventSSIDSpoofTrapSwitchCmd_Object = MibScalar
ruckusZDEventSSIDSpoofTrapSwitchCmd = _RuckusZDEventSSIDSpoofTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 2),
    _RuckusZDEventSSIDSpoofTrapSwitchCmd_Type()
)
ruckusZDEventSSIDSpoofTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventSSIDSpoofTrapSwitchCmd.setStatus("current")


class _RuckusZDEventMACSpoofTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventMACSpoofTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventMACSpoofTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventMACSpoofTrapSwitchCmd_Object = MibScalar
ruckusZDEventMACSpoofTrapSwitchCmd = _RuckusZDEventMACSpoofTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 3),
    _RuckusZDEventMACSpoofTrapSwitchCmd_Type()
)
ruckusZDEventMACSpoofTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventMACSpoofTrapSwitchCmd.setStatus("current")


class _RuckusZDEventRogueAPTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventRogueAPTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventRogueAPTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventRogueAPTrapSwitchCmd_Object = MibScalar
ruckusZDEventRogueAPTrapSwitchCmd = _RuckusZDEventRogueAPTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 4),
    _RuckusZDEventRogueAPTrapSwitchCmd_Type()
)
ruckusZDEventRogueAPTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventRogueAPTrapSwitchCmd.setStatus("current")


class _RuckusZDEventAPLostTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventAPLostTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventAPLostTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventAPLostTrapSwitchCmd_Object = MibScalar
ruckusZDEventAPLostTrapSwitchCmd = _RuckusZDEventAPLostTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 5),
    _RuckusZDEventAPLostTrapSwitchCmd_Type()
)
ruckusZDEventAPLostTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventAPLostTrapSwitchCmd.setStatus("current")


class _RuckusZDEventAPLostHeartbeatTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventAPLostHeartbeatTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventAPLostHeartbeatTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventAPLostHeartbeatTrapSwitchCmd_Object = MibScalar
ruckusZDEventAPLostHeartbeatTrapSwitchCmd = _RuckusZDEventAPLostHeartbeatTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 6),
    _RuckusZDEventAPLostHeartbeatTrapSwitchCmd_Type()
)
ruckusZDEventAPLostHeartbeatTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventAPLostHeartbeatTrapSwitchCmd.setStatus("current")


class _RuckusZDEventClientAuthFailBlockTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventClientAuthFailBlockTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventClientAuthFailBlockTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventClientAuthFailBlockTrapSwitchCmd_Object = MibScalar
ruckusZDEventClientAuthFailBlockTrapSwitchCmd = _RuckusZDEventClientAuthFailBlockTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 7),
    _RuckusZDEventClientAuthFailBlockTrapSwitchCmd_Type()
)
ruckusZDEventClientAuthFailBlockTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventClientAuthFailBlockTrapSwitchCmd.setStatus("current")


class _RuckusZDEventAPResetSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventAPResetSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventAPResetSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventAPResetSwitchCmd_Object = MibScalar
ruckusZDEventAPResetSwitchCmd = _RuckusZDEventAPResetSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 8),
    _RuckusZDEventAPResetSwitchCmd_Type()
)
ruckusZDEventAPResetSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventAPResetSwitchCmd.setStatus("current")


class _RuckusZDEventIPChangeSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventIPChangeSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventIPChangeSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventIPChangeSwitchCmd_Object = MibScalar
ruckusZDEventIPChangeSwitchCmd = _RuckusZDEventIPChangeSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 9),
    _RuckusZDEventIPChangeSwitchCmd_Type()
)
ruckusZDEventIPChangeSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventIPChangeSwitchCmd.setStatus("current")


class _RuckusZDEventSystemColdStartTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventSystemColdStartTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventSystemColdStartTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventSystemColdStartTrapSwitchCmd_Object = MibScalar
ruckusZDEventSystemColdStartTrapSwitchCmd = _RuckusZDEventSystemColdStartTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 10),
    _RuckusZDEventSystemColdStartTrapSwitchCmd_Type()
)
ruckusZDEventSystemColdStartTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventSystemColdStartTrapSwitchCmd.setStatus("current")


class _RuckusZDEventAPChannelChangeTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventAPChannelChangeTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventAPChannelChangeTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventAPChannelChangeTrapSwitchCmd_Object = MibScalar
ruckusZDEventAPChannelChangeTrapSwitchCmd = _RuckusZDEventAPChannelChangeTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 11),
    _RuckusZDEventAPChannelChangeTrapSwitchCmd_Type()
)
ruckusZDEventAPChannelChangeTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventAPChannelChangeTrapSwitchCmd.setStatus("current")


class _RuckusZDEventRadiusAuthUnavailableTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventRadiusAuthUnavailableTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventRadiusAuthUnavailableTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventRadiusAuthUnavailableTrapSwitchCmd_Object = MibScalar
ruckusZDEventRadiusAuthUnavailableTrapSwitchCmd = _RuckusZDEventRadiusAuthUnavailableTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 12),
    _RuckusZDEventRadiusAuthUnavailableTrapSwitchCmd_Type()
)
ruckusZDEventRadiusAuthUnavailableTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventRadiusAuthUnavailableTrapSwitchCmd.setStatus("current")


class _RuckusZDEventRadiusAcctUnavailableTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventRadiusAcctUnavailableTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventRadiusAcctUnavailableTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventRadiusAcctUnavailableTrapSwitchCmd_Object = MibScalar
ruckusZDEventRadiusAcctUnavailableTrapSwitchCmd = _RuckusZDEventRadiusAcctUnavailableTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 13),
    _RuckusZDEventRadiusAcctUnavailableTrapSwitchCmd_Type()
)
ruckusZDEventRadiusAcctUnavailableTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventRadiusAcctUnavailableTrapSwitchCmd.setStatus("current")


class _RuckusZDEventClientJoinFailAPBusyTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventClientJoinFailAPBusyTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventClientJoinFailAPBusyTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventClientJoinFailAPBusyTrapSwitchCmd_Object = MibScalar
ruckusZDEventClientJoinFailAPBusyTrapSwitchCmd = _RuckusZDEventClientJoinFailAPBusyTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 14),
    _RuckusZDEventClientJoinFailAPBusyTrapSwitchCmd_Type()
)
ruckusZDEventClientJoinFailAPBusyTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventClientJoinFailAPBusyTrapSwitchCmd.setStatus("current")


class _RuckusZDEventInterferenceADHocTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventInterferenceADHocTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventInterferenceADHocTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventInterferenceADHocTrapSwitchCmd_Object = MibScalar
ruckusZDEventInterferenceADHocTrapSwitchCmd = _RuckusZDEventInterferenceADHocTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 15),
    _RuckusZDEventInterferenceADHocTrapSwitchCmd_Type()
)
ruckusZDEventInterferenceADHocTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventInterferenceADHocTrapSwitchCmd.setStatus("current")


class _RuckusZDEventImageUpgradeFailTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventImageUpgradeFailTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventImageUpgradeFailTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventImageUpgradeFailTrapSwitchCmd_Object = MibScalar
ruckusZDEventImageUpgradeFailTrapSwitchCmd = _RuckusZDEventImageUpgradeFailTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 16),
    _RuckusZDEventImageUpgradeFailTrapSwitchCmd_Type()
)
ruckusZDEventImageUpgradeFailTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventImageUpgradeFailTrapSwitchCmd.setStatus("current")


class _RuckusZDEventHeartbeatTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventHeartbeatTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventHeartbeatTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventHeartbeatTrapSwitchCmd_Object = MibScalar
ruckusZDEventHeartbeatTrapSwitchCmd = _RuckusZDEventHeartbeatTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 22),
    _RuckusZDEventHeartbeatTrapSwitchCmd_Type()
)
ruckusZDEventHeartbeatTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventHeartbeatTrapSwitchCmd.setStatus("current")


class _RuckusZDEventAttackedTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventAttackedTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventAttackedTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventAttackedTrapSwitchCmd_Object = MibScalar
ruckusZDEventAttackedTrapSwitchCmd = _RuckusZDEventAttackedTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 24),
    _RuckusZDEventAttackedTrapSwitchCmd_Type()
)
ruckusZDEventAttackedTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventAttackedTrapSwitchCmd.setStatus("current")


class _RuckusZDEventSystemWarmStartTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventSystemWarmStartTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventSystemWarmStartTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventSystemWarmStartTrapSwitchCmd_Object = MibScalar
ruckusZDEventSystemWarmStartTrapSwitchCmd = _RuckusZDEventSystemWarmStartTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 25),
    _RuckusZDEventSystemWarmStartTrapSwitchCmd_Type()
)
ruckusZDEventSystemWarmStartTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventSystemWarmStartTrapSwitchCmd.setStatus("current")


class _RuckusZDEventInterfereAPTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventInterfereAPTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventInterfereAPTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventInterfereAPTrapSwitchCmd_Object = MibScalar
ruckusZDEventInterfereAPTrapSwitchCmd = _RuckusZDEventInterfereAPTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 26),
    _RuckusZDEventInterfereAPTrapSwitchCmd_Type()
)
ruckusZDEventInterfereAPTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventInterfereAPTrapSwitchCmd.setStatus("current")


class _RuckusZDEventAPSystemColdStartTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventAPSystemColdStartTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventAPSystemColdStartTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventAPSystemColdStartTrapSwitchCmd_Object = MibScalar
ruckusZDEventAPSystemColdStartTrapSwitchCmd = _RuckusZDEventAPSystemColdStartTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 31),
    _RuckusZDEventAPSystemColdStartTrapSwitchCmd_Type()
)
ruckusZDEventAPSystemColdStartTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventAPSystemColdStartTrapSwitchCmd.setStatus("current")


class _RuckusZDEventAPSystemWarmStartTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventAPSystemWarmStartTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventAPSystemWarmStartTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventAPSystemWarmStartTrapSwitchCmd_Object = MibScalar
ruckusZDEventAPSystemWarmStartTrapSwitchCmd = _RuckusZDEventAPSystemWarmStartTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 32),
    _RuckusZDEventAPSystemWarmStartTrapSwitchCmd_Type()
)
ruckusZDEventAPSystemWarmStartTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventAPSystemWarmStartTrapSwitchCmd.setStatus("current")


class _RuckusZDEventAPSSIDChangedTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventAPSSIDChangedTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventAPSSIDChangedTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventAPSSIDChangedTrapSwitchCmd_Object = MibScalar
ruckusZDEventAPSSIDChangedTrapSwitchCmd = _RuckusZDEventAPSSIDChangedTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 33),
    _RuckusZDEventAPSSIDChangedTrapSwitchCmd_Type()
)
ruckusZDEventAPSSIDChangedTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventAPSSIDChangedTrapSwitchCmd.setStatus("current")


class _RuckusZDEventAPClientExceedValveTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventAPClientExceedValveTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventAPClientExceedValveTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventAPClientExceedValveTrapSwitchCmd_Object = MibScalar
ruckusZDEventAPClientExceedValveTrapSwitchCmd = _RuckusZDEventAPClientExceedValveTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 34),
    _RuckusZDEventAPClientExceedValveTrapSwitchCmd_Type()
)
ruckusZDEventAPClientExceedValveTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventAPClientExceedValveTrapSwitchCmd.setStatus("current")


class _RuckusZDEventAPAvailableStatusTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventAPAvailableStatusTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventAPAvailableStatusTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventAPAvailableStatusTrapSwitchCmd_Object = MibScalar
ruckusZDEventAPAvailableStatusTrapSwitchCmd = _RuckusZDEventAPAvailableStatusTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 35),
    _RuckusZDEventAPAvailableStatusTrapSwitchCmd_Type()
)
ruckusZDEventAPAvailableStatusTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventAPAvailableStatusTrapSwitchCmd.setStatus("current")


class _RuckusZDEventAPWirelessInterfaceFaultTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventAPWirelessInterfaceFaultTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventAPWirelessInterfaceFaultTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventAPWirelessInterfaceFaultTrapSwitchCmd_Object = MibScalar
ruckusZDEventAPWirelessInterfaceFaultTrapSwitchCmd = _RuckusZDEventAPWirelessInterfaceFaultTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 36),
    _RuckusZDEventAPWirelessInterfaceFaultTrapSwitchCmd_Type()
)
ruckusZDEventAPWirelessInterfaceFaultTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventAPWirelessInterfaceFaultTrapSwitchCmd.setStatus("current")


class _RuckusZDEventSystemCpuUtilExceedValveTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventSystemCpuUtilExceedValveTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventSystemCpuUtilExceedValveTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventSystemCpuUtilExceedValveTrapSwitchCmd_Object = MibScalar
ruckusZDEventSystemCpuUtilExceedValveTrapSwitchCmd = _RuckusZDEventSystemCpuUtilExceedValveTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 37),
    _RuckusZDEventSystemCpuUtilExceedValveTrapSwitchCmd_Type()
)
ruckusZDEventSystemCpuUtilExceedValveTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventSystemCpuUtilExceedValveTrapSwitchCmd.setStatus("current")


class _RuckusZDEventSystemMemUtilExceedValveTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventSystemMemUtilExceedValveTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventSystemMemUtilExceedValveTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventSystemMemUtilExceedValveTrapSwitchCmd_Object = MibScalar
ruckusZDEventSystemMemUtilExceedValveTrapSwitchCmd = _RuckusZDEventSystemMemUtilExceedValveTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 38),
    _RuckusZDEventSystemMemUtilExceedValveTrapSwitchCmd_Type()
)
ruckusZDEventSystemMemUtilExceedValveTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventSystemMemUtilExceedValveTrapSwitchCmd.setStatus("current")


class _RuckusZDEventSystemBandwidthUtilExceedValveTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventSystemBandwidthUtilExceedValveTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventSystemBandwidthUtilExceedValveTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventSystemBandwidthUtilExceedValveTrapSwitchCmd_Object = MibScalar
ruckusZDEventSystemBandwidthUtilExceedValveTrapSwitchCmd = _RuckusZDEventSystemBandwidthUtilExceedValveTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 39),
    _RuckusZDEventSystemBandwidthUtilExceedValveTrapSwitchCmd_Type()
)
ruckusZDEventSystemBandwidthUtilExceedValveTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventSystemBandwidthUtilExceedValveTrapSwitchCmd.setStatus("current")


class _RuckusZDEventSystemDropPacketRateExceedValveTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventSystemDropPacketRateExceedValveTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventSystemDropPacketRateExceedValveTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventSystemDropPacketRateExceedValveTrapSwitchCmd_Object = MibScalar
ruckusZDEventSystemDropPacketRateExceedValveTrapSwitchCmd = _RuckusZDEventSystemDropPacketRateExceedValveTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 40),
    _RuckusZDEventSystemDropPacketRateExceedValveTrapSwitchCmd_Type()
)
ruckusZDEventSystemDropPacketRateExceedValveTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventSystemDropPacketRateExceedValveTrapSwitchCmd.setStatus("current")


class _RuckusZDEventAPSyncTimeFailTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventAPSyncTimeFailTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventAPSyncTimeFailTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventAPSyncTimeFailTrapSwitchCmd_Object = MibScalar
ruckusZDEventAPSyncTimeFailTrapSwitchCmd = _RuckusZDEventAPSyncTimeFailTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 41),
    _RuckusZDEventAPSyncTimeFailTrapSwitchCmd_Type()
)
ruckusZDEventAPSyncTimeFailTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventAPSyncTimeFailTrapSwitchCmd.setStatus("current")


class _RuckusZDEventSystemCpuUtilClrWarnTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventSystemCpuUtilClrWarnTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventSystemCpuUtilClrWarnTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventSystemCpuUtilClrWarnTrapSwitchCmd_Object = MibScalar
ruckusZDEventSystemCpuUtilClrWarnTrapSwitchCmd = _RuckusZDEventSystemCpuUtilClrWarnTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 42),
    _RuckusZDEventSystemCpuUtilClrWarnTrapSwitchCmd_Type()
)
ruckusZDEventSystemCpuUtilClrWarnTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventSystemCpuUtilClrWarnTrapSwitchCmd.setStatus("current")


class _RuckusZDEventSystemMemUtilClrwarnTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventSystemMemUtilClrwarnTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventSystemMemUtilClrwarnTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventSystemMemUtilClrwarnTrapSwitchCmd_Object = MibScalar
ruckusZDEventSystemMemUtilClrwarnTrapSwitchCmd = _RuckusZDEventSystemMemUtilClrwarnTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 43),
    _RuckusZDEventSystemMemUtilClrwarnTrapSwitchCmd_Type()
)
ruckusZDEventSystemMemUtilClrwarnTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventSystemMemUtilClrwarnTrapSwitchCmd.setStatus("current")


class _RuckusZDEventClientJoinTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventClientJoinTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventClientJoinTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventClientJoinTrapSwitchCmd_Object = MibScalar
ruckusZDEventClientJoinTrapSwitchCmd = _RuckusZDEventClientJoinTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 60),
    _RuckusZDEventClientJoinTrapSwitchCmd_Type()
)
ruckusZDEventClientJoinTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventClientJoinTrapSwitchCmd.setStatus("current")


class _RuckusZDEventClientJoinFailedTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventClientJoinFailedTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventClientJoinFailedTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventClientJoinFailedTrapSwitchCmd_Object = MibScalar
ruckusZDEventClientJoinFailedTrapSwitchCmd = _RuckusZDEventClientJoinFailedTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 61),
    _RuckusZDEventClientJoinFailedTrapSwitchCmd_Type()
)
ruckusZDEventClientJoinFailedTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventClientJoinFailedTrapSwitchCmd.setStatus("current")


class _RuckusZDEventClientJoinFailedAPBusyTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventClientJoinFailedAPBusyTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventClientJoinFailedAPBusyTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventClientJoinFailedAPBusyTrapSwitchCmd_Object = MibScalar
ruckusZDEventClientJoinFailedAPBusyTrapSwitchCmd = _RuckusZDEventClientJoinFailedAPBusyTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 62),
    _RuckusZDEventClientJoinFailedAPBusyTrapSwitchCmd_Type()
)
ruckusZDEventClientJoinFailedAPBusyTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventClientJoinFailedAPBusyTrapSwitchCmd.setStatus("current")


class _RuckusZDEventClientDisconnectTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventClientDisconnectTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventClientDisconnectTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventClientDisconnectTrapSwitchCmd_Object = MibScalar
ruckusZDEventClientDisconnectTrapSwitchCmd = _RuckusZDEventClientDisconnectTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 63),
    _RuckusZDEventClientDisconnectTrapSwitchCmd_Type()
)
ruckusZDEventClientDisconnectTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventClientDisconnectTrapSwitchCmd.setStatus("current")


class _RuckusZDEventClientRoamOutTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventClientRoamOutTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventClientRoamOutTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventClientRoamOutTrapSwitchCmd_Object = MibScalar
ruckusZDEventClientRoamOutTrapSwitchCmd = _RuckusZDEventClientRoamOutTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 64),
    _RuckusZDEventClientRoamOutTrapSwitchCmd_Type()
)
ruckusZDEventClientRoamOutTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventClientRoamOutTrapSwitchCmd.setStatus("current")


class _RuckusZDEventClientRoamInTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventClientRoamInTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventClientRoamInTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventClientRoamInTrapSwitchCmd_Object = MibScalar
ruckusZDEventClientRoamInTrapSwitchCmd = _RuckusZDEventClientRoamInTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 65),
    _RuckusZDEventClientRoamInTrapSwitchCmd_Type()
)
ruckusZDEventClientRoamInTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventClientRoamInTrapSwitchCmd.setStatus("current")


class _RuckusZDEventClientAuthFailedTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventClientAuthFailedTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventClientAuthFailedTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventClientAuthFailedTrapSwitchCmd_Object = MibScalar
ruckusZDEventClientAuthFailedTrapSwitchCmd = _RuckusZDEventClientAuthFailedTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 66),
    _RuckusZDEventClientAuthFailedTrapSwitchCmd_Type()
)
ruckusZDEventClientAuthFailedTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventClientAuthFailedTrapSwitchCmd.setStatus("current")


class _RuckusZDEventClientAuthorizationFailedTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventClientAuthorizationFailedTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventClientAuthorizationFailedTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventClientAuthorizationFailedTrapSwitchCmd_Object = MibScalar
ruckusZDEventClientAuthorizationFailedTrapSwitchCmd = _RuckusZDEventClientAuthorizationFailedTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 67),
    _RuckusZDEventClientAuthorizationFailedTrapSwitchCmd_Type()
)
ruckusZDEventClientAuthorizationFailedTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventClientAuthorizationFailedTrapSwitchCmd.setStatus("current")


class _RuckusZDEventAPCPUvalveTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventAPCPUvalveTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventAPCPUvalveTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventAPCPUvalveTrapSwitchCmd_Object = MibScalar
ruckusZDEventAPCPUvalveTrapSwitchCmd = _RuckusZDEventAPCPUvalveTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 83),
    _RuckusZDEventAPCPUvalveTrapSwitchCmd_Type()
)
ruckusZDEventAPCPUvalveTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventAPCPUvalveTrapSwitchCmd.setStatus("current")


class _RuckusZDEventAPMEMvalveTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventAPMEMvalveTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventAPMEMvalveTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventAPMEMvalveTrapSwitchCmd_Object = MibScalar
ruckusZDEventAPMEMvalveTrapSwitchCmd = _RuckusZDEventAPMEMvalveTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 84),
    _RuckusZDEventAPMEMvalveTrapSwitchCmd_Type()
)
ruckusZDEventAPMEMvalveTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventAPMEMvalveTrapSwitchCmd.setStatus("current")


class _RuckusZDEventAPCPUvalveClrwarnTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventAPCPUvalveClrwarnTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventAPCPUvalveClrwarnTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventAPCPUvalveClrwarnTrapSwitchCmd_Object = MibScalar
ruckusZDEventAPCPUvalveClrwarnTrapSwitchCmd = _RuckusZDEventAPCPUvalveClrwarnTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 85),
    _RuckusZDEventAPCPUvalveClrwarnTrapSwitchCmd_Type()
)
ruckusZDEventAPCPUvalveClrwarnTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventAPCPUvalveClrwarnTrapSwitchCmd.setStatus("current")


class _RuckusZDEventAPMEMvalveClrwarnTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventAPMEMvalveClrwarnTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventAPMEMvalveClrwarnTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventAPMEMvalveClrwarnTrapSwitchCmd_Object = MibScalar
ruckusZDEventAPMEMvalveClrwarnTrapSwitchCmd = _RuckusZDEventAPMEMvalveClrwarnTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 86),
    _RuckusZDEventAPMEMvalveClrwarnTrapSwitchCmd_Type()
)
ruckusZDEventAPMEMvalveClrwarnTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventAPMEMvalveClrwarnTrapSwitchCmd.setStatus("current")


class _RuckusZDEventAPNumStaExceedValveClrwarnTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventAPNumStaExceedValveClrwarnTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventAPNumStaExceedValveClrwarnTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventAPNumStaExceedValveClrwarnTrapSwitchCmd_Object = MibScalar
ruckusZDEventAPNumStaExceedValveClrwarnTrapSwitchCmd = _RuckusZDEventAPNumStaExceedValveClrwarnTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 87),
    _RuckusZDEventAPNumStaExceedValveClrwarnTrapSwitchCmd_Type()
)
ruckusZDEventAPNumStaExceedValveClrwarnTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventAPNumStaExceedValveClrwarnTrapSwitchCmd.setStatus("current")


class _RuckusZDEventDhcpPoolFullTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventDhcpPoolFullTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventDhcpPoolFullTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventDhcpPoolFullTrapSwitchCmd_Object = MibScalar
ruckusZDEventDhcpPoolFullTrapSwitchCmd = _RuckusZDEventDhcpPoolFullTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 88),
    _RuckusZDEventDhcpPoolFullTrapSwitchCmd_Type()
)
ruckusZDEventDhcpPoolFullTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventDhcpPoolFullTrapSwitchCmd.setStatus("current")


class _RuckusZDEventDhcpPoolAbunTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventDhcpPoolAbunTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventDhcpPoolAbunTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventDhcpPoolAbunTrapSwitchCmd_Object = MibScalar
ruckusZDEventDhcpPoolAbunTrapSwitchCmd = _RuckusZDEventDhcpPoolAbunTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 89),
    _RuckusZDEventDhcpPoolAbunTrapSwitchCmd_Type()
)
ruckusZDEventDhcpPoolAbunTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventDhcpPoolAbunTrapSwitchCmd.setStatus("current")


class _RuckusZDEventSmartRedundancyChangetoActiveTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventSmartRedundancyChangetoActiveTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventSmartRedundancyChangetoActiveTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventSmartRedundancyChangetoActiveTrapSwitchCmd_Object = MibScalar
ruckusZDEventSmartRedundancyChangetoActiveTrapSwitchCmd = _RuckusZDEventSmartRedundancyChangetoActiveTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 100),
    _RuckusZDEventSmartRedundancyChangetoActiveTrapSwitchCmd_Type()
)
ruckusZDEventSmartRedundancyChangetoActiveTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventSmartRedundancyChangetoActiveTrapSwitchCmd.setStatus("current")


class _RuckusZDEventSmartRedundancyActiveConnectedTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventSmartRedundancyActiveConnectedTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventSmartRedundancyActiveConnectedTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventSmartRedundancyActiveConnectedTrapSwitchCmd_Object = MibScalar
ruckusZDEventSmartRedundancyActiveConnectedTrapSwitchCmd = _RuckusZDEventSmartRedundancyActiveConnectedTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 101),
    _RuckusZDEventSmartRedundancyActiveConnectedTrapSwitchCmd_Type()
)
ruckusZDEventSmartRedundancyActiveConnectedTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventSmartRedundancyActiveConnectedTrapSwitchCmd.setStatus("current")


class _RuckusZDEventSmartRedundancyActiveDisconnectedTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventSmartRedundancyActiveDisconnectedTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventSmartRedundancyActiveDisconnectedTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventSmartRedundancyActiveDisconnectedTrapSwitchCmd_Object = MibScalar
ruckusZDEventSmartRedundancyActiveDisconnectedTrapSwitchCmd = _RuckusZDEventSmartRedundancyActiveDisconnectedTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 102),
    _RuckusZDEventSmartRedundancyActiveDisconnectedTrapSwitchCmd_Type()
)
ruckusZDEventSmartRedundancyActiveDisconnectedTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventSmartRedundancyActiveDisconnectedTrapSwitchCmd.setStatus("current")


class _RuckusZDEventSmartRedundancyStandbyConnectedTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventSmartRedundancyStandbyConnectedTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventSmartRedundancyStandbyConnectedTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventSmartRedundancyStandbyConnectedTrapSwitchCmd_Object = MibScalar
ruckusZDEventSmartRedundancyStandbyConnectedTrapSwitchCmd = _RuckusZDEventSmartRedundancyStandbyConnectedTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 103),
    _RuckusZDEventSmartRedundancyStandbyConnectedTrapSwitchCmd_Type()
)
ruckusZDEventSmartRedundancyStandbyConnectedTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventSmartRedundancyStandbyConnectedTrapSwitchCmd.setStatus("current")


class _RuckusZDEventSmartRedundancyStandbyDisconnectedTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventSmartRedundancyStandbyDisconnectedTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventSmartRedundancyStandbyDisconnectedTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventSmartRedundancyStandbyDisconnectedTrapSwitchCmd_Object = MibScalar
ruckusZDEventSmartRedundancyStandbyDisconnectedTrapSwitchCmd = _RuckusZDEventSmartRedundancyStandbyDisconnectedTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 104),
    _RuckusZDEventSmartRedundancyStandbyDisconnectedTrapSwitchCmd_Type()
)
ruckusZDEventSmartRedundancyStandbyDisconnectedTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventSmartRedundancyStandbyDisconnectedTrapSwitchCmd.setStatus("current")


class _RuckusZDEventLBSAdminEnabledTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventLBSAdminEnabledTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventLBSAdminEnabledTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventLBSAdminEnabledTrapSwitchCmd_Object = MibScalar
ruckusZDEventLBSAdminEnabledTrapSwitchCmd = _RuckusZDEventLBSAdminEnabledTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 120),
    _RuckusZDEventLBSAdminEnabledTrapSwitchCmd_Type()
)
ruckusZDEventLBSAdminEnabledTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventLBSAdminEnabledTrapSwitchCmd.setStatus("current")


class _RuckusZDEventLBSAdminDisabledTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventLBSAdminDisabledTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventLBSAdminDisabledTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventLBSAdminDisabledTrapSwitchCmd_Object = MibScalar
ruckusZDEventLBSAdminDisabledTrapSwitchCmd = _RuckusZDEventLBSAdminDisabledTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 121),
    _RuckusZDEventLBSAdminDisabledTrapSwitchCmd_Type()
)
ruckusZDEventLBSAdminDisabledTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventLBSAdminDisabledTrapSwitchCmd.setStatus("current")


class _RuckusZDEventLBSZDLSConnectionUpTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventLBSZDLSConnectionUpTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventLBSZDLSConnectionUpTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventLBSZDLSConnectionUpTrapSwitchCmd_Object = MibScalar
ruckusZDEventLBSZDLSConnectionUpTrapSwitchCmd = _RuckusZDEventLBSZDLSConnectionUpTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 122),
    _RuckusZDEventLBSZDLSConnectionUpTrapSwitchCmd_Type()
)
ruckusZDEventLBSZDLSConnectionUpTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventLBSZDLSConnectionUpTrapSwitchCmd.setStatus("current")


class _RuckusZDEventLBSZDLSConnectionDownTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventLBSZDLSConnectionDownTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventLBSZDLSConnectionDownTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventLBSZDLSConnectionDownTrapSwitchCmd_Object = MibScalar
ruckusZDEventLBSZDLSConnectionDownTrapSwitchCmd = _RuckusZDEventLBSZDLSConnectionDownTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 123),
    _RuckusZDEventLBSZDLSConnectionDownTrapSwitchCmd_Type()
)
ruckusZDEventLBSZDLSConnectionDownTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventLBSZDLSConnectionDownTrapSwitchCmd.setStatus("current")


class _RuckusZDEventLBSReceiveCMDFootfallTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventLBSReceiveCMDFootfallTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventLBSReceiveCMDFootfallTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventLBSReceiveCMDFootfallTrapSwitchCmd_Object = MibScalar
ruckusZDEventLBSReceiveCMDFootfallTrapSwitchCmd = _RuckusZDEventLBSReceiveCMDFootfallTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 124),
    _RuckusZDEventLBSReceiveCMDFootfallTrapSwitchCmd_Type()
)
ruckusZDEventLBSReceiveCMDFootfallTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventLBSReceiveCMDFootfallTrapSwitchCmd.setStatus("current")


class _RuckusZDEventLBSReceiveCMDCalibrationTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventLBSReceiveCMDCalibrationTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusZDEventLBSReceiveCMDCalibrationTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventLBSReceiveCMDCalibrationTrapSwitchCmd_Object = MibScalar
ruckusZDEventLBSReceiveCMDCalibrationTrapSwitchCmd = _RuckusZDEventLBSReceiveCMDCalibrationTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 125),
    _RuckusZDEventLBSReceiveCMDCalibrationTrapSwitchCmd_Type()
)
ruckusZDEventLBSReceiveCMDCalibrationTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventLBSReceiveCMDCalibrationTrapSwitchCmd.setStatus("current")


class _RuckusZDEventALLEventTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusZDEventALLEventTrapSwitchCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("hybrid", 3))
    )


_RuckusZDEventALLEventTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusZDEventALLEventTrapSwitchCmd_Object = MibScalar
ruckusZDEventALLEventTrapSwitchCmd = _RuckusZDEventALLEventTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 3, 200),
    _RuckusZDEventALLEventTrapSwitchCmd_Type()
)
ruckusZDEventALLEventTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEventALLEventTrapSwitchCmd.setStatus("current")

# Managed Objects groups


# Notification objects

ruckusZDEventAPJoinTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 1)
)
ruckusZDEventAPJoinTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventAPMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusZDEventAPJoinTrap.setStatus(
        "current"
    )

ruckusZDEventSSIDSpoofTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 2)
)
ruckusZDEventSSIDSpoofTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSSID"))
)
if mibBuilder.loadTexts:
    ruckusZDEventSSIDSpoofTrap.setStatus(
        "current"
    )

ruckusZDEventMACSpoofTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 3)
)
ruckusZDEventMACSpoofTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSSID"))
)
if mibBuilder.loadTexts:
    ruckusZDEventMACSpoofTrap.setStatus(
        "current"
    )

ruckusZDEventRogueAPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 4)
)
ruckusZDEventRogueAPTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSSID"))
)
if mibBuilder.loadTexts:
    ruckusZDEventRogueAPTrap.setStatus(
        "current"
    )

ruckusZDEventAPLostTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 5)
)
ruckusZDEventAPLostTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventAPMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusZDEventAPLostTrap.setStatus(
        "current"
    )

ruckusZDEventAPLostHeartbeatTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 6)
)
ruckusZDEventAPLostHeartbeatTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventAPMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusZDEventAPLostHeartbeatTrap.setStatus(
        "current"
    )

ruckusZDEventClientAuthFailBlockTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 7)
)
ruckusZDEventClientAuthFailBlockTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventClientMacAddr"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventAPMacAddr"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSSID"))
)
if mibBuilder.loadTexts:
    ruckusZDEventClientAuthFailBlockTrap.setStatus(
        "current"
    )

ruckusZDEventAPResetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 8)
)
ruckusZDEventAPResetTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventAPMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusZDEventAPResetTrap.setStatus(
        "current"
    )

ruckusZDEventIPChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 9)
)
ruckusZDEventIPChangeTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventIPChangeTrap.setStatus(
        "current"
    )

ruckusZDEventSystemColdStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 10)
)
ruckusZDEventSystemColdStartTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventSystemColdStartTrap.setStatus(
        "current"
    )

ruckusZDEventAPChannelChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 11)
)
ruckusZDEventAPChannelChangeTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventAPMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusZDEventAPChannelChangeTrap.setStatus(
        "current"
    )

ruckusZDEventRadiusAuthUnavailableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 12)
)
ruckusZDEventRadiusAuthUnavailableTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventRadiusAuthUnavailableTrap.setStatus(
        "current"
    )

ruckusZDEventRadiusAcctUnavailableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 13)
)
ruckusZDEventRadiusAcctUnavailableTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventRadiusAcctUnavailableTrap.setStatus(
        "current"
    )

ruckusZDEventClientJoinFailAPBusyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 14)
)
ruckusZDEventClientJoinFailAPBusyTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventClientJoinFailAPBusyTrap.setStatus(
        "current"
    )

ruckusZDEventInterferenceADHoc = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 15)
)
ruckusZDEventInterferenceADHoc.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventInterferenceADHoc.setStatus(
        "current"
    )

ruckusZDEventImageUpgradeFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 16)
)
ruckusZDEventImageUpgradeFailTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventImageUpgradeFailTrap.setStatus(
        "current"
    )

ruckusZDEventHeartbeatTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 22)
)
ruckusZDEventHeartbeatTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventHeartbeatTrap.setStatus(
        "current"
    )

ruckusZDEventAttackedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 24)
)
ruckusZDEventAttackedTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventAttackedTrap.setStatus(
        "current"
    )

ruckusZDEventSystemWarmStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 25)
)
ruckusZDEventSystemWarmStartTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventSystemWarmStartTrap.setStatus(
        "current"
    )

ruckusZDEventInterfereAPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 26)
)
ruckusZDEventInterfereAPTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventInterfereAPTrap.setStatus(
        "current"
    )

ruckusZDEventAPSystemColdStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 31)
)
ruckusZDEventAPSystemColdStartTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventAPSystemColdStartTrap.setStatus(
        "current"
    )

ruckusZDEventAPSystemWarmStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 32)
)
ruckusZDEventAPSystemWarmStartTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventAPSystemWarmStartTrap.setStatus(
        "current"
    )

ruckusZDEventAPSSIDChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 33)
)
ruckusZDEventAPSSIDChangedTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventAPSSIDChangedTrap.setStatus(
        "current"
    )

ruckusZDEventAPClientExceedValve = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 34)
)
ruckusZDEventAPClientExceedValve.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventAPMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusZDEventAPClientExceedValve.setStatus(
        "current"
    )

ruckusZDEventAPAvailableStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 35)
)
ruckusZDEventAPAvailableStatusTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventAPAvailableStatusTrap.setStatus(
        "current"
    )

ruckusZDEventAPWirelessInterfaceFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 36)
)
ruckusZDEventAPWirelessInterfaceFaultTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventAPWirelessInterfaceFaultTrap.setStatus(
        "current"
    )

ruckusZDEventSystemCpuUtilExceedValve = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 37)
)
ruckusZDEventSystemCpuUtilExceedValve.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventSystemCpuUtilExceedValve.setStatus(
        "current"
    )

ruckusZDEventSystemMemUtilExceedValve = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 38)
)
ruckusZDEventSystemMemUtilExceedValve.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventSystemMemUtilExceedValve.setStatus(
        "current"
    )

ruckusZDEventSystemBandwidthUtilExceedValve = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 39)
)
ruckusZDEventSystemBandwidthUtilExceedValve.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventSystemBandwidthUtilExceedValve.setStatus(
        "current"
    )

ruckusZDEventSystemDropPacketRateExceedValve = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 40)
)
ruckusZDEventSystemDropPacketRateExceedValve.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventSystemDropPacketRateExceedValve.setStatus(
        "current"
    )

ruckusZDEventAPSyncTimeFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 41)
)
ruckusZDEventAPSyncTimeFail.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventAPSyncTimeFail.setStatus(
        "current"
    )

ruckusZDEventSystemCpuUtilClrWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 42)
)
ruckusZDEventSystemCpuUtilClrWarn.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventSystemCpuUtilClrWarn.setStatus(
        "current"
    )

ruckusZDEventSystemMemUtilClrwarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 43)
)
ruckusZDEventSystemMemUtilClrwarn.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventSystemMemUtilClrwarn.setStatus(
        "current"
    )

ruckusZDEventClientJoin = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 60)
)
ruckusZDEventClientJoin.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventClientMacAddr"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventAPMacAddr"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSSID"))
)
if mibBuilder.loadTexts:
    ruckusZDEventClientJoin.setStatus(
        "current"
    )

ruckusZDEventClientJoinFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 61)
)
ruckusZDEventClientJoinFailed.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventClientMacAddr"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventAPMacAddr"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSSID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventReason"))
)
if mibBuilder.loadTexts:
    ruckusZDEventClientJoinFailed.setStatus(
        "current"
    )

ruckusZDEventClientJoinFailedAPBusy = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 62)
)
ruckusZDEventClientJoinFailedAPBusy.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventClientMacAddr"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventAPMacAddr"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSSID"))
)
if mibBuilder.loadTexts:
    ruckusZDEventClientJoinFailedAPBusy.setStatus(
        "current"
    )

ruckusZDEventClientDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 63)
)
ruckusZDEventClientDisconnect.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventClientMacAddr"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventAPMacAddr"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSSID"))
)
if mibBuilder.loadTexts:
    ruckusZDEventClientDisconnect.setStatus(
        "current"
    )

ruckusZDEventClientRoamOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 64)
)
ruckusZDEventClientRoamOut.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventClientMacAddr"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventAPMacAddr"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSSID"))
)
if mibBuilder.loadTexts:
    ruckusZDEventClientRoamOut.setStatus(
        "current"
    )

ruckusZDEventClientRoamIn = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 65)
)
ruckusZDEventClientRoamIn.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventClientMacAddr"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventAPMacAddr"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSSID"))
)
if mibBuilder.loadTexts:
    ruckusZDEventClientRoamIn.setStatus(
        "current"
    )

ruckusZDEventClientAuthFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 66)
)
ruckusZDEventClientAuthFailed.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventClientMacAddr"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventAPMacAddr"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSSID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventReason"))
)
if mibBuilder.loadTexts:
    ruckusZDEventClientAuthFailed.setStatus(
        "current"
    )

ruckusZDEventClientAuthorizationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 67)
)
ruckusZDEventClientAuthorizationFailed.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventClientMacAddr"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventAPMacAddr"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSSID"))
)
if mibBuilder.loadTexts:
    ruckusZDEventClientAuthorizationFailed.setStatus(
        "current"
    )

ruckusZDEventAPCPUvalve = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 83)
)
ruckusZDEventAPCPUvalve.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventAPMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusZDEventAPCPUvalve.setStatus(
        "current"
    )

ruckusZDEventAPMEMvalve = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 84)
)
ruckusZDEventAPMEMvalve.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventAPMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusZDEventAPMEMvalve.setStatus(
        "current"
    )

ruckusZDEventAPCPUvalveClrwarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 85)
)
ruckusZDEventAPCPUvalveClrwarn.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventAPMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusZDEventAPCPUvalveClrwarn.setStatus(
        "current"
    )

ruckusZDEventAPMEMvalveClrwarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 86)
)
ruckusZDEventAPMEMvalveClrwarn.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventAPMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusZDEventAPMEMvalveClrwarn.setStatus(
        "current"
    )

ruckusZDEventAPNumStaExceedValveClrwarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 87)
)
ruckusZDEventAPNumStaExceedValveClrwarn.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventAPMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusZDEventAPNumStaExceedValveClrwarn.setStatus(
        "current"
    )

ruckusZDEventDhcpPoolFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 88)
)
ruckusZDEventDhcpPoolFull.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventDhcpPoolFull.setStatus(
        "current"
    )

ruckusZDEventDhcpPoolAbun = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 89)
)
ruckusZDEventDhcpPoolAbun.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventDhcpPoolAbun.setStatus(
        "current"
    )

ruckusZDEventSmartRedundancyChangetoActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 100)
)
ruckusZDEventSmartRedundancyChangetoActive.setObjects(
    ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventIpAddr")
)
if mibBuilder.loadTexts:
    ruckusZDEventSmartRedundancyChangetoActive.setStatus(
        "current"
    )

ruckusZDEventSmartRedundancyActiveConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 101)
)
ruckusZDEventSmartRedundancyActiveConnected.setObjects(
    ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventIpAddr")
)
if mibBuilder.loadTexts:
    ruckusZDEventSmartRedundancyActiveConnected.setStatus(
        "current"
    )

ruckusZDEventSmartRedundancyActiveDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 102)
)
ruckusZDEventSmartRedundancyActiveDisconnected.setObjects(
    ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventIpAddr")
)
if mibBuilder.loadTexts:
    ruckusZDEventSmartRedundancyActiveDisconnected.setStatus(
        "current"
    )

ruckusZDEventSmartRedundancyStandbyConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 103)
)
ruckusZDEventSmartRedundancyStandbyConnected.setObjects(
    ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventIpAddr")
)
if mibBuilder.loadTexts:
    ruckusZDEventSmartRedundancyStandbyConnected.setStatus(
        "current"
    )

ruckusZDEventSmartRedundancyStandbyDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 104)
)
ruckusZDEventSmartRedundancyStandbyDisconnected.setObjects(
    ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventIpAddr")
)
if mibBuilder.loadTexts:
    ruckusZDEventSmartRedundancyStandbyDisconnected.setStatus(
        "current"
    )

ruckusZDEventLBSAdminEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 120)
)
ruckusZDEventLBSAdminEnabled.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventLBSAdminEnabled.setStatus(
        "current"
    )

ruckusZDEventLBSAdminDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 121)
)
ruckusZDEventLBSAdminDisabled.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventLBSAdminDisabled.setStatus(
        "current"
    )

ruckusZDEventLBSZDLSConnectionUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 122)
)
ruckusZDEventLBSZDLSConnectionUp.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventLBSZDLSConnectionUp.setStatus(
        "current"
    )

ruckusZDEventLBSZDLSConnectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 123)
)
ruckusZDEventLBSZDLSConnectionDown.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventLBSZDLSConnectionDown.setStatus(
        "current"
    )

ruckusZDEventLBSReceiveCMDFootfall = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 124)
)
ruckusZDEventLBSReceiveCMDFootfall.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventLBSReceiveCMDFootfall.setStatus(
        "current"
    )

ruckusZDEventLBSReceiveCMDCalibration = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 125)
)
ruckusZDEventLBSReceiveCMDCalibration.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventLBSReceiveCMDCalibration.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-ZD-EVENT-MIB",
    **{"ruckusZDEventMIB": ruckusZDEventMIB,
       "ruckusZDEventTraps": ruckusZDEventTraps,
       "ruckusZDEventAPJoinTrap": ruckusZDEventAPJoinTrap,
       "ruckusZDEventSSIDSpoofTrap": ruckusZDEventSSIDSpoofTrap,
       "ruckusZDEventMACSpoofTrap": ruckusZDEventMACSpoofTrap,
       "ruckusZDEventRogueAPTrap": ruckusZDEventRogueAPTrap,
       "ruckusZDEventAPLostTrap": ruckusZDEventAPLostTrap,
       "ruckusZDEventAPLostHeartbeatTrap": ruckusZDEventAPLostHeartbeatTrap,
       "ruckusZDEventClientAuthFailBlockTrap": ruckusZDEventClientAuthFailBlockTrap,
       "ruckusZDEventAPResetTrap": ruckusZDEventAPResetTrap,
       "ruckusZDEventIPChangeTrap": ruckusZDEventIPChangeTrap,
       "ruckusZDEventSystemColdStartTrap": ruckusZDEventSystemColdStartTrap,
       "ruckusZDEventAPChannelChangeTrap": ruckusZDEventAPChannelChangeTrap,
       "ruckusZDEventRadiusAuthUnavailableTrap": ruckusZDEventRadiusAuthUnavailableTrap,
       "ruckusZDEventRadiusAcctUnavailableTrap": ruckusZDEventRadiusAcctUnavailableTrap,
       "ruckusZDEventClientJoinFailAPBusyTrap": ruckusZDEventClientJoinFailAPBusyTrap,
       "ruckusZDEventInterferenceADHoc": ruckusZDEventInterferenceADHoc,
       "ruckusZDEventImageUpgradeFailTrap": ruckusZDEventImageUpgradeFailTrap,
       "ruckusZDEventHeartbeatTrap": ruckusZDEventHeartbeatTrap,
       "ruckusZDEventAttackedTrap": ruckusZDEventAttackedTrap,
       "ruckusZDEventSystemWarmStartTrap": ruckusZDEventSystemWarmStartTrap,
       "ruckusZDEventInterfereAPTrap": ruckusZDEventInterfereAPTrap,
       "ruckusZDEventAPSystemColdStartTrap": ruckusZDEventAPSystemColdStartTrap,
       "ruckusZDEventAPSystemWarmStartTrap": ruckusZDEventAPSystemWarmStartTrap,
       "ruckusZDEventAPSSIDChangedTrap": ruckusZDEventAPSSIDChangedTrap,
       "ruckusZDEventAPClientExceedValve": ruckusZDEventAPClientExceedValve,
       "ruckusZDEventAPAvailableStatusTrap": ruckusZDEventAPAvailableStatusTrap,
       "ruckusZDEventAPWirelessInterfaceFaultTrap": ruckusZDEventAPWirelessInterfaceFaultTrap,
       "ruckusZDEventSystemCpuUtilExceedValve": ruckusZDEventSystemCpuUtilExceedValve,
       "ruckusZDEventSystemMemUtilExceedValve": ruckusZDEventSystemMemUtilExceedValve,
       "ruckusZDEventSystemBandwidthUtilExceedValve": ruckusZDEventSystemBandwidthUtilExceedValve,
       "ruckusZDEventSystemDropPacketRateExceedValve": ruckusZDEventSystemDropPacketRateExceedValve,
       "ruckusZDEventAPSyncTimeFail": ruckusZDEventAPSyncTimeFail,
       "ruckusZDEventSystemCpuUtilClrWarn": ruckusZDEventSystemCpuUtilClrWarn,
       "ruckusZDEventSystemMemUtilClrwarn": ruckusZDEventSystemMemUtilClrwarn,
       "ruckusZDEventClientJoin": ruckusZDEventClientJoin,
       "ruckusZDEventClientJoinFailed": ruckusZDEventClientJoinFailed,
       "ruckusZDEventClientJoinFailedAPBusy": ruckusZDEventClientJoinFailedAPBusy,
       "ruckusZDEventClientDisconnect": ruckusZDEventClientDisconnect,
       "ruckusZDEventClientRoamOut": ruckusZDEventClientRoamOut,
       "ruckusZDEventClientRoamIn": ruckusZDEventClientRoamIn,
       "ruckusZDEventClientAuthFailed": ruckusZDEventClientAuthFailed,
       "ruckusZDEventClientAuthorizationFailed": ruckusZDEventClientAuthorizationFailed,
       "ruckusZDEventAPCPUvalve": ruckusZDEventAPCPUvalve,
       "ruckusZDEventAPMEMvalve": ruckusZDEventAPMEMvalve,
       "ruckusZDEventAPCPUvalveClrwarn": ruckusZDEventAPCPUvalveClrwarn,
       "ruckusZDEventAPMEMvalveClrwarn": ruckusZDEventAPMEMvalveClrwarn,
       "ruckusZDEventAPNumStaExceedValveClrwarn": ruckusZDEventAPNumStaExceedValveClrwarn,
       "ruckusZDEventDhcpPoolFull": ruckusZDEventDhcpPoolFull,
       "ruckusZDEventDhcpPoolAbun": ruckusZDEventDhcpPoolAbun,
       "ruckusZDEventSmartRedundancyChangetoActive": ruckusZDEventSmartRedundancyChangetoActive,
       "ruckusZDEventSmartRedundancyActiveConnected": ruckusZDEventSmartRedundancyActiveConnected,
       "ruckusZDEventSmartRedundancyActiveDisconnected": ruckusZDEventSmartRedundancyActiveDisconnected,
       "ruckusZDEventSmartRedundancyStandbyConnected": ruckusZDEventSmartRedundancyStandbyConnected,
       "ruckusZDEventSmartRedundancyStandbyDisconnected": ruckusZDEventSmartRedundancyStandbyDisconnected,
       "ruckusZDEventLBSAdminEnabled": ruckusZDEventLBSAdminEnabled,
       "ruckusZDEventLBSAdminDisabled": ruckusZDEventLBSAdminDisabled,
       "ruckusZDEventLBSZDLSConnectionUp": ruckusZDEventLBSZDLSConnectionUp,
       "ruckusZDEventLBSZDLSConnectionDown": ruckusZDEventLBSZDLSConnectionDown,
       "ruckusZDEventLBSReceiveCMDFootfall": ruckusZDEventLBSReceiveCMDFootfall,
       "ruckusZDEventLBSReceiveCMDCalibration": ruckusZDEventLBSReceiveCMDCalibration,
       "ruckusZDEventObjects": ruckusZDEventObjects,
       "ruckusZDEventSerial": ruckusZDEventSerial,
       "ruckusZDEventNEID": ruckusZDEventNEID,
       "ruckusZDEventSeverity": ruckusZDEventSeverity,
       "ruckusZDEventType": ruckusZDEventType,
       "ruckusZDEventTime": ruckusZDEventTime,
       "ruckusZDEventStatus": ruckusZDEventStatus,
       "ruckusZDEventTitle": ruckusZDEventTitle,
       "ruckusZDEventContent": ruckusZDEventContent,
       "ruckusZDEventClientMacAddr": ruckusZDEventClientMacAddr,
       "ruckusZDEventAPMacAddr": ruckusZDEventAPMacAddr,
       "ruckusZDEventRogueMacAddr": ruckusZDEventRogueMacAddr,
       "ruckusZDEventSSID": ruckusZDEventSSID,
       "ruckusZDEventChannel": ruckusZDEventChannel,
       "ruckusZDEventReason": ruckusZDEventReason,
       "ruckusZDEventIpAddr": ruckusZDEventIpAddr,
       "ruckusZDEventTrapSwitchCmd": ruckusZDEventTrapSwitchCmd,
       "ruckusZDEventAPJoinTrapSwitchCmd": ruckusZDEventAPJoinTrapSwitchCmd,
       "ruckusZDEventSSIDSpoofTrapSwitchCmd": ruckusZDEventSSIDSpoofTrapSwitchCmd,
       "ruckusZDEventMACSpoofTrapSwitchCmd": ruckusZDEventMACSpoofTrapSwitchCmd,
       "ruckusZDEventRogueAPTrapSwitchCmd": ruckusZDEventRogueAPTrapSwitchCmd,
       "ruckusZDEventAPLostTrapSwitchCmd": ruckusZDEventAPLostTrapSwitchCmd,
       "ruckusZDEventAPLostHeartbeatTrapSwitchCmd": ruckusZDEventAPLostHeartbeatTrapSwitchCmd,
       "ruckusZDEventClientAuthFailBlockTrapSwitchCmd": ruckusZDEventClientAuthFailBlockTrapSwitchCmd,
       "ruckusZDEventAPResetSwitchCmd": ruckusZDEventAPResetSwitchCmd,
       "ruckusZDEventIPChangeSwitchCmd": ruckusZDEventIPChangeSwitchCmd,
       "ruckusZDEventSystemColdStartTrapSwitchCmd": ruckusZDEventSystemColdStartTrapSwitchCmd,
       "ruckusZDEventAPChannelChangeTrapSwitchCmd": ruckusZDEventAPChannelChangeTrapSwitchCmd,
       "ruckusZDEventRadiusAuthUnavailableTrapSwitchCmd": ruckusZDEventRadiusAuthUnavailableTrapSwitchCmd,
       "ruckusZDEventRadiusAcctUnavailableTrapSwitchCmd": ruckusZDEventRadiusAcctUnavailableTrapSwitchCmd,
       "ruckusZDEventClientJoinFailAPBusyTrapSwitchCmd": ruckusZDEventClientJoinFailAPBusyTrapSwitchCmd,
       "ruckusZDEventInterferenceADHocTrapSwitchCmd": ruckusZDEventInterferenceADHocTrapSwitchCmd,
       "ruckusZDEventImageUpgradeFailTrapSwitchCmd": ruckusZDEventImageUpgradeFailTrapSwitchCmd,
       "ruckusZDEventHeartbeatTrapSwitchCmd": ruckusZDEventHeartbeatTrapSwitchCmd,
       "ruckusZDEventAttackedTrapSwitchCmd": ruckusZDEventAttackedTrapSwitchCmd,
       "ruckusZDEventSystemWarmStartTrapSwitchCmd": ruckusZDEventSystemWarmStartTrapSwitchCmd,
       "ruckusZDEventInterfereAPTrapSwitchCmd": ruckusZDEventInterfereAPTrapSwitchCmd,
       "ruckusZDEventAPSystemColdStartTrapSwitchCmd": ruckusZDEventAPSystemColdStartTrapSwitchCmd,
       "ruckusZDEventAPSystemWarmStartTrapSwitchCmd": ruckusZDEventAPSystemWarmStartTrapSwitchCmd,
       "ruckusZDEventAPSSIDChangedTrapSwitchCmd": ruckusZDEventAPSSIDChangedTrapSwitchCmd,
       "ruckusZDEventAPClientExceedValveTrapSwitchCmd": ruckusZDEventAPClientExceedValveTrapSwitchCmd,
       "ruckusZDEventAPAvailableStatusTrapSwitchCmd": ruckusZDEventAPAvailableStatusTrapSwitchCmd,
       "ruckusZDEventAPWirelessInterfaceFaultTrapSwitchCmd": ruckusZDEventAPWirelessInterfaceFaultTrapSwitchCmd,
       "ruckusZDEventSystemCpuUtilExceedValveTrapSwitchCmd": ruckusZDEventSystemCpuUtilExceedValveTrapSwitchCmd,
       "ruckusZDEventSystemMemUtilExceedValveTrapSwitchCmd": ruckusZDEventSystemMemUtilExceedValveTrapSwitchCmd,
       "ruckusZDEventSystemBandwidthUtilExceedValveTrapSwitchCmd": ruckusZDEventSystemBandwidthUtilExceedValveTrapSwitchCmd,
       "ruckusZDEventSystemDropPacketRateExceedValveTrapSwitchCmd": ruckusZDEventSystemDropPacketRateExceedValveTrapSwitchCmd,
       "ruckusZDEventAPSyncTimeFailTrapSwitchCmd": ruckusZDEventAPSyncTimeFailTrapSwitchCmd,
       "ruckusZDEventSystemCpuUtilClrWarnTrapSwitchCmd": ruckusZDEventSystemCpuUtilClrWarnTrapSwitchCmd,
       "ruckusZDEventSystemMemUtilClrwarnTrapSwitchCmd": ruckusZDEventSystemMemUtilClrwarnTrapSwitchCmd,
       "ruckusZDEventClientJoinTrapSwitchCmd": ruckusZDEventClientJoinTrapSwitchCmd,
       "ruckusZDEventClientJoinFailedTrapSwitchCmd": ruckusZDEventClientJoinFailedTrapSwitchCmd,
       "ruckusZDEventClientJoinFailedAPBusyTrapSwitchCmd": ruckusZDEventClientJoinFailedAPBusyTrapSwitchCmd,
       "ruckusZDEventClientDisconnectTrapSwitchCmd": ruckusZDEventClientDisconnectTrapSwitchCmd,
       "ruckusZDEventClientRoamOutTrapSwitchCmd": ruckusZDEventClientRoamOutTrapSwitchCmd,
       "ruckusZDEventClientRoamInTrapSwitchCmd": ruckusZDEventClientRoamInTrapSwitchCmd,
       "ruckusZDEventClientAuthFailedTrapSwitchCmd": ruckusZDEventClientAuthFailedTrapSwitchCmd,
       "ruckusZDEventClientAuthorizationFailedTrapSwitchCmd": ruckusZDEventClientAuthorizationFailedTrapSwitchCmd,
       "ruckusZDEventAPCPUvalveTrapSwitchCmd": ruckusZDEventAPCPUvalveTrapSwitchCmd,
       "ruckusZDEventAPMEMvalveTrapSwitchCmd": ruckusZDEventAPMEMvalveTrapSwitchCmd,
       "ruckusZDEventAPCPUvalveClrwarnTrapSwitchCmd": ruckusZDEventAPCPUvalveClrwarnTrapSwitchCmd,
       "ruckusZDEventAPMEMvalveClrwarnTrapSwitchCmd": ruckusZDEventAPMEMvalveClrwarnTrapSwitchCmd,
       "ruckusZDEventAPNumStaExceedValveClrwarnTrapSwitchCmd": ruckusZDEventAPNumStaExceedValveClrwarnTrapSwitchCmd,
       "ruckusZDEventDhcpPoolFullTrapSwitchCmd": ruckusZDEventDhcpPoolFullTrapSwitchCmd,
       "ruckusZDEventDhcpPoolAbunTrapSwitchCmd": ruckusZDEventDhcpPoolAbunTrapSwitchCmd,
       "ruckusZDEventSmartRedundancyChangetoActiveTrapSwitchCmd": ruckusZDEventSmartRedundancyChangetoActiveTrapSwitchCmd,
       "ruckusZDEventSmartRedundancyActiveConnectedTrapSwitchCmd": ruckusZDEventSmartRedundancyActiveConnectedTrapSwitchCmd,
       "ruckusZDEventSmartRedundancyActiveDisconnectedTrapSwitchCmd": ruckusZDEventSmartRedundancyActiveDisconnectedTrapSwitchCmd,
       "ruckusZDEventSmartRedundancyStandbyConnectedTrapSwitchCmd": ruckusZDEventSmartRedundancyStandbyConnectedTrapSwitchCmd,
       "ruckusZDEventSmartRedundancyStandbyDisconnectedTrapSwitchCmd": ruckusZDEventSmartRedundancyStandbyDisconnectedTrapSwitchCmd,
       "ruckusZDEventLBSAdminEnabledTrapSwitchCmd": ruckusZDEventLBSAdminEnabledTrapSwitchCmd,
       "ruckusZDEventLBSAdminDisabledTrapSwitchCmd": ruckusZDEventLBSAdminDisabledTrapSwitchCmd,
       "ruckusZDEventLBSZDLSConnectionUpTrapSwitchCmd": ruckusZDEventLBSZDLSConnectionUpTrapSwitchCmd,
       "ruckusZDEventLBSZDLSConnectionDownTrapSwitchCmd": ruckusZDEventLBSZDLSConnectionDownTrapSwitchCmd,
       "ruckusZDEventLBSReceiveCMDFootfallTrapSwitchCmd": ruckusZDEventLBSReceiveCMDFootfallTrapSwitchCmd,
       "ruckusZDEventLBSReceiveCMDCalibrationTrapSwitchCmd": ruckusZDEventLBSReceiveCMDCalibrationTrapSwitchCmd,
       "ruckusZDEventALLEventTrapSwitchCmd": ruckusZDEventALLEventTrapSwitchCmd}
)
