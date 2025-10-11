# SNMP MIB module (MX-LLDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-LLDP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:07 2025
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

(mediatrixServices,) = mibBuilder.importSymbols(
    "MX-SMI2",
    "mediatrixServices")

(MxActivationState,
 MxAdvancedIpPort,
 MxDigitMap,
 MxEnableState,
 MxIpAddress,
 MxIpHostName,
 MxIpPort,
 MxIpSubnetMask) = mibBuilder.importSymbols(
    "MX-TC",
    "MxActivationState",
    "MxAdvancedIpPort",
    "MxDigitMap",
    "MxEnableState",
    "MxIpAddress",
    "MxIpHostName",
    "MxIpPort",
    "MxIpSubnetMask")

(MxFloat32,
 MxIpAddr,
 MxIpAddrMask,
 MxIpAddrPort,
 MxIpHostNamePort,
 MxUInt64,
 MxUri,
 MxUrl) = mibBuilder.importSymbols(
    "MX-TC2",
    "MxFloat32",
    "MxIpAddr",
    "MxIpAddrMask",
    "MxIpAddrPort",
    "MxIpHostNamePort",
    "MxUInt64",
    "MxUri",
    "MxUrl")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

lldpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4100)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LldpMIBObjects_ObjectIdentity = ObjectIdentity
lldpMIBObjects = _LldpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4100, 1)
)
_StatusGroup_ObjectIdentity = ObjectIdentity
statusGroup = _StatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4100, 1, 100)
)
_RemoteMediaPolicyStateTable_Object = MibTable
remoteMediaPolicyStateTable = _RemoteMediaPolicyStateTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4100, 1, 100, 100)
)
if mibBuilder.loadTexts:
    remoteMediaPolicyStateTable.setStatus("current")
_RemoteMediaPolicyStateEntry_Object = MibTableRow
remoteMediaPolicyStateEntry = _RemoteMediaPolicyStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4100, 1, 100, 100, 1)
)
remoteMediaPolicyStateEntry.setIndexNames(
    (0, "MX-LLDP-MIB", "remoteMediaPolicyStateAppType"),
)
if mibBuilder.loadTexts:
    remoteMediaPolicyStateEntry.setStatus("current")


class _RemoteMediaPolicyStateAppType_Type(Integer32):
    """Custom type remoteMediaPolicyStateAppType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("voice", 1),
          ("voiceSignaling", 2),
          ("guestVoice", 3),
          ("guestVoiceSignaling", 4),
          ("softPhoneVoice", 5),
          ("videoConferencing", 6),
          ("streamingVideo", 7),
          ("videoSignaling", 8))
    )


_RemoteMediaPolicyStateAppType_Type.__name__ = "Integer32"
_RemoteMediaPolicyStateAppType_Object = MibTableColumn
remoteMediaPolicyStateAppType = _RemoteMediaPolicyStateAppType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4100, 1, 100, 100, 1, 100),
    _RemoteMediaPolicyStateAppType_Type()
)
remoteMediaPolicyStateAppType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteMediaPolicyStateAppType.setStatus("current")


class _RemoteMediaPolicyStateVlanId_Type(Unsigned32):
    """Custom type remoteMediaPolicyStateVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_RemoteMediaPolicyStateVlanId_Type.__name__ = "Unsigned32"
_RemoteMediaPolicyStateVlanId_Object = MibTableColumn
remoteMediaPolicyStateVlanId = _RemoteMediaPolicyStateVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4100, 1, 100, 100, 1, 200),
    _RemoteMediaPolicyStateVlanId_Type()
)
remoteMediaPolicyStateVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteMediaPolicyStateVlanId.setStatus("current")


class _RemoteMediaPolicyStatePriority_Type(Unsigned32):
    """Custom type remoteMediaPolicyStatePriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RemoteMediaPolicyStatePriority_Type.__name__ = "Unsigned32"
_RemoteMediaPolicyStatePriority_Object = MibTableColumn
remoteMediaPolicyStatePriority = _RemoteMediaPolicyStatePriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4100, 1, 100, 100, 1, 300),
    _RemoteMediaPolicyStatePriority_Type()
)
remoteMediaPolicyStatePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteMediaPolicyStatePriority.setStatus("current")


class _RemoteMediaPolicyStateDscp_Type(Unsigned32):
    """Custom type remoteMediaPolicyStateDscp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RemoteMediaPolicyStateDscp_Type.__name__ = "Unsigned32"
_RemoteMediaPolicyStateDscp_Object = MibTableColumn
remoteMediaPolicyStateDscp = _RemoteMediaPolicyStateDscp_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4100, 1, 100, 100, 1, 400),
    _RemoteMediaPolicyStateDscp_Type()
)
remoteMediaPolicyStateDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteMediaPolicyStateDscp.setStatus("current")


class _RemoteMediaPolicyStatePolicyFlag_Type(Integer32):
    """Custom type remoteMediaPolicyStatePolicyFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("defined", 100),
          ("unknown", 200))
    )


_RemoteMediaPolicyStatePolicyFlag_Type.__name__ = "Integer32"
_RemoteMediaPolicyStatePolicyFlag_Object = MibTableColumn
remoteMediaPolicyStatePolicyFlag = _RemoteMediaPolicyStatePolicyFlag_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4100, 1, 100, 100, 1, 500),
    _RemoteMediaPolicyStatePolicyFlag_Type()
)
remoteMediaPolicyStatePolicyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteMediaPolicyStatePolicyFlag.setStatus("current")


class _RemoteMediaPolicyStateTaggedFlag_Type(Integer32):
    """Custom type remoteMediaPolicyStateTaggedFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("untagged", 100),
          ("tagged", 200))
    )


_RemoteMediaPolicyStateTaggedFlag_Type.__name__ = "Integer32"
_RemoteMediaPolicyStateTaggedFlag_Object = MibTableColumn
remoteMediaPolicyStateTaggedFlag = _RemoteMediaPolicyStateTaggedFlag_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4100, 1, 100, 100, 1, 600),
    _RemoteMediaPolicyStateTaggedFlag_Type()
)
remoteMediaPolicyStateTaggedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteMediaPolicyStateTaggedFlag.setStatus("current")


class _NetworkInterface_Type(OctetString):
    """Custom type networkInterface based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_NetworkInterface_Type.__name__ = "OctetString"
_NetworkInterface_Object = MibScalar
networkInterface = _NetworkInterface_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4100, 1, 200),
    _NetworkInterface_Type()
)
networkInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkInterface.setStatus("current")


class _ChassisId_Type(Integer32):
    """Custom type chassisId based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("macAddress", 100),
          ("networkAddress", 200))
    )


_ChassisId_Type.__name__ = "Integer32"
_ChassisId_Object = MibScalar
chassisId = _ChassisId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4100, 1, 300),
    _ChassisId_Type()
)
chassisId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisId.setStatus("current")


class _OverrideNetworkPolicyEnable_Type(MxEnableState):
    """Custom type overrideNetworkPolicyEnable based on MxEnableState"""
    defaultValue = 0


_OverrideNetworkPolicyEnable_Type.__name__ = "MxEnableState"
_OverrideNetworkPolicyEnable_Object = MibScalar
overrideNetworkPolicyEnable = _OverrideNetworkPolicyEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4100, 1, 400),
    _OverrideNetworkPolicyEnable_Type()
)
overrideNetworkPolicyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overrideNetworkPolicyEnable.setStatus("current")


class _OverrideNetworkPolicyRefresh_Type(Integer32):
    """Custom type overrideNetworkPolicyRefresh based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("disable", 100),
          ("onNetworkPolicyChanges", 200))
    )


_OverrideNetworkPolicyRefresh_Type.__name__ = "Integer32"
_OverrideNetworkPolicyRefresh_Object = MibScalar
overrideNetworkPolicyRefresh = _OverrideNetworkPolicyRefresh_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4100, 1, 410),
    _OverrideNetworkPolicyRefresh_Type()
)
overrideNetworkPolicyRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overrideNetworkPolicyRefresh.setStatus("current")
_NotificationsGroup_ObjectIdentity = ObjectIdentity
notificationsGroup = _NotificationsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4100, 1, 60010)
)


class _MinSeverity_Type(Integer32):
    """Custom type minSeverity based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              100,
              200,
              300,
              400,
              500)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("debug", 100),
          ("info", 200),
          ("warning", 300),
          ("error", 400),
          ("critical", 500))
    )


_MinSeverity_Type.__name__ = "Integer32"
_MinSeverity_Object = MibScalar
minSeverity = _MinSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4100, 1, 60010, 100),
    _MinSeverity_Type()
)
minSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minSeverity.setStatus("current")
_ConfigurationGroup_ObjectIdentity = ObjectIdentity
configurationGroup = _ConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4100, 1, 60020)
)


class _NeedRestartInfo_Type(Integer32):
    """Custom type needRestartInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              100)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 100))
    )


_NeedRestartInfo_Type.__name__ = "Integer32"
_NeedRestartInfo_Object = MibScalar
needRestartInfo = _NeedRestartInfo_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4100, 1, 60020, 100),
    _NeedRestartInfo_Type()
)
needRestartInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    needRestartInfo.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-LLDP-MIB",
    **{"lldpMIB": lldpMIB,
       "lldpMIBObjects": lldpMIBObjects,
       "statusGroup": statusGroup,
       "remoteMediaPolicyStateTable": remoteMediaPolicyStateTable,
       "remoteMediaPolicyStateEntry": remoteMediaPolicyStateEntry,
       "remoteMediaPolicyStateAppType": remoteMediaPolicyStateAppType,
       "remoteMediaPolicyStateVlanId": remoteMediaPolicyStateVlanId,
       "remoteMediaPolicyStatePriority": remoteMediaPolicyStatePriority,
       "remoteMediaPolicyStateDscp": remoteMediaPolicyStateDscp,
       "remoteMediaPolicyStatePolicyFlag": remoteMediaPolicyStatePolicyFlag,
       "remoteMediaPolicyStateTaggedFlag": remoteMediaPolicyStateTaggedFlag,
       "networkInterface": networkInterface,
       "chassisId": chassisId,
       "overrideNetworkPolicyEnable": overrideNetworkPolicyEnable,
       "overrideNetworkPolicyRefresh": overrideNetworkPolicyRefresh,
       "notificationsGroup": notificationsGroup,
       "minSeverity": minSeverity,
       "configurationGroup": configurationGroup,
       "needRestartInfo": needRestartInfo}
)
