# SNMP MIB module (ARICENT-LLDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-LLDP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:44:46 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddressIPv4,
 InetAddressIPv6) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6")

(lldpXdot1RemPortVlanId,
 lldpXdot1RemProtoVlanSupported,
 lldpXdot1RemProtocolId,
 lldpXdot1RemVlanName) = mibBuilder.importSymbols(
    "LLDP-EXT-DOT1-MIB",
    "lldpXdot1RemPortVlanId",
    "lldpXdot1RemProtoVlanSupported",
    "lldpXdot1RemProtocolId",
    "lldpXdot1RemVlanName")

(lldpXdot3RemLinkAggStatus,
 lldpXdot3RemMaxFrameSize,
 lldpXdot3RemPortOperMauType,
 lldpXdot3RemPowerClass) = mibBuilder.importSymbols(
    "LLDP-EXT-DOT3-MIB",
    "lldpXdot3RemLinkAggStatus",
    "lldpXdot3RemMaxFrameSize",
    "lldpXdot3RemPortOperMauType",
    "lldpXdot3RemPowerClass")

(LldpPortNumber,
 lldpLocManAddrEntry,
 lldpLocPortId,
 lldpLocPortNum,
 lldpRemChassisId,
 lldpRemManAddrIfId,
 lldpRemPortId,
 lldpRemSysName,
 lldpStatsRemTablesAgeouts,
 lldpStatsRemTablesDeletes,
 lldpStatsRemTablesDrops,
 lldpStatsRemTablesInserts) = mibBuilder.importSymbols(
    "LLDP-MIB",
    "LldpPortNumber",
    "lldpLocManAddrEntry",
    "lldpLocPortId",
    "lldpLocPortNum",
    "lldpRemChassisId",
    "lldpRemManAddrIfId",
    "lldpRemPortId",
    "lldpRemSysName",
    "lldpStatsRemTablesAgeouts",
    "lldpStatsRemTablesDeletes",
    "lldpStatsRemTablesDrops",
    "lldpStatsRemTablesInserts")

(lldpV2StatsTxPortEntry,) = mibBuilder.importSymbols(
    "LLDP-V2-MIB",
    "lldpV2StatsTxPortEntry")

(LldpV2DestAddressTableIndex,) = mibBuilder.importSymbols(
    "LLDP-V2-TC-MIB",
    "LldpV2DestAddressTableIndex")

(ZeroBasedCounter32,) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "ZeroBasedCounter32")

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

fslldp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 158)
)
if mibBuilder.loadTexts:
    fslldp.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsLldpSystem_ObjectIdentity = ObjectIdentity
fsLldpSystem = _FsLldpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 158, 1)
)


class _FsLldpSystemControl_Type(Integer32):
    """Custom type fsLldpSystemControl based on Integer32"""
    defaultValue = 1

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
          ("shutdownInProgress", 2),
          ("shutdown", 3))
    )


_FsLldpSystemControl_Type.__name__ = "Integer32"
_FsLldpSystemControl_Object = MibScalar
fsLldpSystemControl = _FsLldpSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 2076, 158, 1, 1),
    _FsLldpSystemControl_Type()
)
fsLldpSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLldpSystemControl.setStatus("current")


class _FsLldpModuleStatus_Type(Integer32):
    """Custom type fsLldpModuleStatus based on Integer32"""
    defaultValue = 2

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


_FsLldpModuleStatus_Type.__name__ = "Integer32"
_FsLldpModuleStatus_Object = MibScalar
fsLldpModuleStatus = _FsLldpModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 158, 1, 2),
    _FsLldpModuleStatus_Type()
)
fsLldpModuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLldpModuleStatus.setStatus("current")


class _FsLldpTraceInput_Type(DisplayString):
    """Custom type fsLldpTraceInput based on DisplayString"""
    defaultValue = OctetString("critical")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 288),
    )


_FsLldpTraceInput_Type.__name__ = "DisplayString"
_FsLldpTraceInput_Object = MibScalar
fsLldpTraceInput = _FsLldpTraceInput_Object(
    (1, 3, 6, 1, 4, 1, 2076, 158, 1, 3),
    _FsLldpTraceInput_Type()
)
fsLldpTraceInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLldpTraceInput.setStatus("current")


class _FsLldpTraceOption_Type(Integer32):
    """Custom type fsLldpTraceOption based on Integer32"""
    defaultValue = 8192


_FsLldpTraceOption_Type.__name__ = "Integer32"
_FsLldpTraceOption_Object = MibScalar
fsLldpTraceOption = _FsLldpTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 2076, 158, 1, 4),
    _FsLldpTraceOption_Type()
)
fsLldpTraceOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpTraceOption.setStatus("current")


class _FsLldpTraceLevel_Type(Integer32):
    """Custom type fsLldpTraceLevel based on Integer32"""
    defaultValue = 8192


_FsLldpTraceLevel_Type.__name__ = "Integer32"
_FsLldpTraceLevel_Object = MibScalar
fsLldpTraceLevel = _FsLldpTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 2076, 158, 1, 5),
    _FsLldpTraceLevel_Type()
)
fsLldpTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLldpTraceLevel.setStatus("current")


class _FsLldpTagStatus_Type(Integer32):
    """Custom type fsLldpTagStatus based on Integer32"""
    defaultValue = 2

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


_FsLldpTagStatus_Type.__name__ = "Integer32"
_FsLldpTagStatus_Object = MibScalar
fsLldpTagStatus = _FsLldpTagStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 158, 1, 6),
    _FsLldpTagStatus_Type()
)
fsLldpTagStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLldpTagStatus.setStatus("current")
_FsLldpConfiguredMgmtIpv4Address_Type = InetAddressIPv4
_FsLldpConfiguredMgmtIpv4Address_Object = MibScalar
fsLldpConfiguredMgmtIpv4Address = _FsLldpConfiguredMgmtIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 2076, 158, 1, 7),
    _FsLldpConfiguredMgmtIpv4Address_Type()
)
fsLldpConfiguredMgmtIpv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLldpConfiguredMgmtIpv4Address.setStatus("current")
_FsLldpConfiguredMgmtIpv6Address_Type = InetAddressIPv6
_FsLldpConfiguredMgmtIpv6Address_Object = MibScalar
fsLldpConfiguredMgmtIpv6Address = _FsLldpConfiguredMgmtIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2076, 158, 1, 8),
    _FsLldpConfiguredMgmtIpv6Address_Type()
)
fsLldpConfiguredMgmtIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLldpConfiguredMgmtIpv6Address.setStatus("current")
_FsLldpTLV_ObjectIdentity = ObjectIdentity
fsLldpTLV = _FsLldpTLV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 158, 2)
)


class _FsLldpLocChassisIdSubtype_Type(Integer32):
    """Custom type fsLldpLocChassisIdSubtype based on Integer32"""
    defaultValue = 4

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
        *(("chassiscomp", 1),
          ("ifalias", 2),
          ("portcomp", 3),
          ("macaddr", 4),
          ("nwaddr", 5),
          ("ifname", 6),
          ("local", 7))
    )


_FsLldpLocChassisIdSubtype_Type.__name__ = "Integer32"
_FsLldpLocChassisIdSubtype_Object = MibScalar
fsLldpLocChassisIdSubtype = _FsLldpLocChassisIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 2076, 158, 2, 1),
    _FsLldpLocChassisIdSubtype_Type()
)
fsLldpLocChassisIdSubtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLldpLocChassisIdSubtype.setStatus("current")


class _FsLldpLocChassisId_Type(OctetString):
    """Custom type fsLldpLocChassisId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_FsLldpLocChassisId_Type.__name__ = "OctetString"
_FsLldpLocChassisId_Object = MibScalar
fsLldpLocChassisId = _FsLldpLocChassisId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 158, 2, 2),
    _FsLldpLocChassisId_Type()
)
fsLldpLocChassisId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLldpLocChassisId.setStatus("current")
_FsLldpLocPortTable_Object = MibTable
fsLldpLocPortTable = _FsLldpLocPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 158, 2, 3)
)
if mibBuilder.loadTexts:
    fsLldpLocPortTable.setStatus("current")
_FsLldpLocPortEntry_Object = MibTableRow
fsLldpLocPortEntry = _FsLldpLocPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 158, 2, 3, 1)
)
fsLldpLocPortEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpLocPortNum"),
)
if mibBuilder.loadTexts:
    fsLldpLocPortEntry.setStatus("current")


class _FsLldpLocPortIdSubtype_Type(Integer32):
    """Custom type fsLldpLocPortIdSubtype based on Integer32"""
    defaultValue = 1

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
        *(("ifalias", 1),
          ("portcomp", 2),
          ("macaddr", 3),
          ("nwaddr", 4),
          ("ifname", 5),
          ("agentcircuitid", 6),
          ("local", 7))
    )


_FsLldpLocPortIdSubtype_Type.__name__ = "Integer32"
_FsLldpLocPortIdSubtype_Object = MibTableColumn
fsLldpLocPortIdSubtype = _FsLldpLocPortIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 2076, 158, 2, 3, 1, 1),
    _FsLldpLocPortIdSubtype_Type()
)
fsLldpLocPortIdSubtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLldpLocPortIdSubtype.setStatus("current")


class _FsLldpLocPortId_Type(OctetString):
    """Custom type fsLldpLocPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_FsLldpLocPortId_Type.__name__ = "OctetString"
_FsLldpLocPortId_Object = MibTableColumn
fsLldpLocPortId = _FsLldpLocPortId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 158, 2, 3, 1, 2),
    _FsLldpLocPortId_Type()
)
fsLldpLocPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLldpLocPortId.setStatus("current")


class _FsLldpPortConfigNotificationType_Type(Integer32):
    """Custom type fsLldpPortConfigNotificationType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("remTabChg", 1),
          ("misCfg", 2),
          ("remTabChgAndMisCfg", 3))
    )


_FsLldpPortConfigNotificationType_Type.__name__ = "Integer32"
_FsLldpPortConfigNotificationType_Object = MibTableColumn
fsLldpPortConfigNotificationType = _FsLldpPortConfigNotificationType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 158, 2, 3, 1, 3),
    _FsLldpPortConfigNotificationType_Type()
)
fsLldpPortConfigNotificationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLldpPortConfigNotificationType.setStatus("current")


class _FsLldpLocPortDstMac_Type(MacAddress):
    """Custom type fsLldpLocPortDstMac based on MacAddress"""
    defaultHexValue = "0180C200000E"


_FsLldpLocPortDstMac_Type.__name__ = "MacAddress"
_FsLldpLocPortDstMac_Object = MibTableColumn
fsLldpLocPortDstMac = _FsLldpLocPortDstMac_Object(
    (1, 3, 6, 1, 4, 1, 2076, 158, 2, 3, 1, 4),
    _FsLldpLocPortDstMac_Type()
)
fsLldpLocPortDstMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLldpLocPortDstMac.setStatus("current")


class _FsLldpMedAdminStatus_Type(Integer32):
    """Custom type fsLldpMedAdminStatus based on Integer32"""
    defaultValue = 2

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


_FsLldpMedAdminStatus_Type.__name__ = "Integer32"
_FsLldpMedAdminStatus_Object = MibTableColumn
fsLldpMedAdminStatus = _FsLldpMedAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 158, 2, 3, 1, 5),
    _FsLldpMedAdminStatus_Type()
)
fsLldpMedAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLldpMedAdminStatus.setStatus("current")
_FsLldpManAddrConfigTable_Object = MibTable
fsLldpManAddrConfigTable = _FsLldpManAddrConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 158, 2, 4)
)
if mibBuilder.loadTexts:
    fsLldpManAddrConfigTable.setStatus("current")
_FsLldpManAddrConfigEntry_Object = MibTableRow
fsLldpManAddrConfigEntry = _FsLldpManAddrConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 158, 2, 4, 1)
)
if mibBuilder.loadTexts:
    fsLldpManAddrConfigEntry.setStatus("current")


class _FsLldpManAddrConfigOperStatus_Type(Integer32):
    """Custom type fsLldpManAddrConfigOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_FsLldpManAddrConfigOperStatus_Type.__name__ = "Integer32"
_FsLldpManAddrConfigOperStatus_Object = MibTableColumn
fsLldpManAddrConfigOperStatus = _FsLldpManAddrConfigOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 158, 2, 4, 1, 1),
    _FsLldpManAddrConfigOperStatus_Type()
)
fsLldpManAddrConfigOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpManAddrConfigOperStatus.setStatus("current")
_FsLldpStatistics_ObjectIdentity = ObjectIdentity
fsLldpStatistics = _FsLldpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 158, 3)
)
_FsLldpMemAllocFailure_Type = Integer32
_FsLldpMemAllocFailure_Object = MibScalar
fsLldpMemAllocFailure = _FsLldpMemAllocFailure_Object(
    (1, 3, 6, 1, 4, 1, 2076, 158, 3, 1),
    _FsLldpMemAllocFailure_Type()
)
fsLldpMemAllocFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpMemAllocFailure.setStatus("current")
_FsLldpInputQOverFlows_Type = Integer32
_FsLldpInputQOverFlows_Object = MibScalar
fsLldpInputQOverFlows = _FsLldpInputQOverFlows_Object(
    (1, 3, 6, 1, 4, 1, 2076, 158, 3, 2),
    _FsLldpInputQOverFlows_Type()
)
fsLldpInputQOverFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpInputQOverFlows.setStatus("current")
_FsLldpStatsRemTablesUpdates_Type = ZeroBasedCounter32
_FsLldpStatsRemTablesUpdates_Object = MibScalar
fsLldpStatsRemTablesUpdates = _FsLldpStatsRemTablesUpdates_Object(
    (1, 3, 6, 1, 4, 1, 2076, 158, 3, 3),
    _FsLldpStatsRemTablesUpdates_Type()
)
fsLldpStatsRemTablesUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpStatsRemTablesUpdates.setStatus("current")
if mibBuilder.loadTexts:
    fsLldpStatsRemTablesUpdates.setUnits("table entries")


class _FsLldpClearStats_Type(TruthValue):
    """Custom type fsLldpClearStats based on TruthValue"""
    defaultValue = 2


_FsLldpClearStats_Type.__name__ = "TruthValue"
_FsLldpClearStats_Object = MibScalar
fsLldpClearStats = _FsLldpClearStats_Object(
    (1, 3, 6, 1, 4, 1, 2076, 158, 3, 4),
    _FsLldpClearStats_Type()
)
fsLldpClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLldpClearStats.setStatus("current")
_FsLldpNotification_ObjectIdentity = ObjectIdentity
fsLldpNotification = _FsLldpNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 158, 4)
)
_FsLldpTraps_ObjectIdentity = ObjectIdentity
fsLldpTraps = _FsLldpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 158, 4, 0)
)
_Fslldpv2Config_ObjectIdentity = ObjectIdentity
fslldpv2Config = _Fslldpv2Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 158, 5)
)


class _Fslldpv2Version_Type(Integer32):
    """Custom type fslldpv2Version based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lldpv1", 1),
          ("lldpv2", 2))
    )


_Fslldpv2Version_Type.__name__ = "Integer32"
_Fslldpv2Version_Object = MibScalar
fslldpv2Version = _Fslldpv2Version_Object(
    (1, 3, 6, 1, 4, 1, 2076, 158, 5, 1),
    _Fslldpv2Version_Type()
)
fslldpv2Version.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fslldpv2Version.setStatus("current")
_Fslldpv2ConfigPortMapTable_Object = MibTable
fslldpv2ConfigPortMapTable = _Fslldpv2ConfigPortMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 158, 5, 2)
)
if mibBuilder.loadTexts:
    fslldpv2ConfigPortMapTable.setStatus("current")
_Fslldpv2ConfigPortMapEntry_Object = MibTableRow
fslldpv2ConfigPortMapEntry = _Fslldpv2ConfigPortMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 158, 5, 2, 1)
)
fslldpv2ConfigPortMapEntry.setIndexNames(
    (0, "ARICENT-LLDP-MIB", "fslldpv2ConfigPortMapIfIndex"),
    (0, "ARICENT-LLDP-MIB", "fslldpv2ConfigPortMapDestMacAddress"),
)
if mibBuilder.loadTexts:
    fslldpv2ConfigPortMapEntry.setStatus("current")
_Fslldpv2ConfigPortMapIfIndex_Type = InterfaceIndex
_Fslldpv2ConfigPortMapIfIndex_Object = MibTableColumn
fslldpv2ConfigPortMapIfIndex = _Fslldpv2ConfigPortMapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 158, 5, 2, 1, 1),
    _Fslldpv2ConfigPortMapIfIndex_Type()
)
fslldpv2ConfigPortMapIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fslldpv2ConfigPortMapIfIndex.setStatus("current")
_Fslldpv2ConfigPortMapDestMacAddress_Type = MacAddress
_Fslldpv2ConfigPortMapDestMacAddress_Object = MibTableColumn
fslldpv2ConfigPortMapDestMacAddress = _Fslldpv2ConfigPortMapDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 158, 5, 2, 1, 2),
    _Fslldpv2ConfigPortMapDestMacAddress_Type()
)
fslldpv2ConfigPortMapDestMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fslldpv2ConfigPortMapDestMacAddress.setStatus("current")
_Fslldpv2ConfigPortMapNum_Type = LldpPortNumber
_Fslldpv2ConfigPortMapNum_Object = MibTableColumn
fslldpv2ConfigPortMapNum = _Fslldpv2ConfigPortMapNum_Object(
    (1, 3, 6, 1, 4, 1, 2076, 158, 5, 2, 1, 3),
    _Fslldpv2ConfigPortMapNum_Type()
)
fslldpv2ConfigPortMapNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fslldpv2ConfigPortMapNum.setStatus("current")
_Fslldpv2ConfigPortRowStatus_Type = RowStatus
_Fslldpv2ConfigPortRowStatus_Object = MibTableColumn
fslldpv2ConfigPortRowStatus = _Fslldpv2ConfigPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 158, 5, 2, 1, 4),
    _Fslldpv2ConfigPortRowStatus_Type()
)
fslldpv2ConfigPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fslldpv2ConfigPortRowStatus.setStatus("current")
_FslldpV2DestAddressTable_Object = MibTable
fslldpV2DestAddressTable = _FslldpV2DestAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 158, 5, 3)
)
if mibBuilder.loadTexts:
    fslldpV2DestAddressTable.setStatus("current")
_FslldpV2DestAddressTableEntry_Object = MibTableRow
fslldpV2DestAddressTableEntry = _FslldpV2DestAddressTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 158, 5, 3, 1)
)
fslldpV2DestAddressTableEntry.setIndexNames(
    (0, "ARICENT-LLDP-MIB", "fslldpV2AddressTableIndex"),
)
if mibBuilder.loadTexts:
    fslldpV2DestAddressTableEntry.setStatus("current")
_FslldpV2AddressTableIndex_Type = LldpV2DestAddressTableIndex
_FslldpV2AddressTableIndex_Object = MibTableColumn
fslldpV2AddressTableIndex = _FslldpV2AddressTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 158, 5, 3, 1, 1),
    _FslldpV2AddressTableIndex_Type()
)
fslldpV2AddressTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fslldpV2AddressTableIndex.setStatus("current")
_FslldpV2DestMacAddress_Type = MacAddress
_FslldpV2DestMacAddress_Object = MibTableColumn
fslldpV2DestMacAddress = _FslldpV2DestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 158, 5, 3, 1, 2),
    _FslldpV2DestMacAddress_Type()
)
fslldpV2DestMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fslldpV2DestMacAddress.setStatus("current")
_Fslldpv2DestRowStatus_Type = RowStatus
_Fslldpv2DestRowStatus_Object = MibTableColumn
fslldpv2DestRowStatus = _Fslldpv2DestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 158, 5, 3, 1, 3),
    _Fslldpv2DestRowStatus_Type()
)
fslldpv2DestRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fslldpv2DestRowStatus.setStatus("current")
_FsLldpStatsTaggedTxPortTable_Object = MibTable
fsLldpStatsTaggedTxPortTable = _FsLldpStatsTaggedTxPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 158, 5, 4)
)
if mibBuilder.loadTexts:
    fsLldpStatsTaggedTxPortTable.setStatus("current")
_FsLldpStatsTaggedTxPortEntry_Object = MibTableRow
fsLldpStatsTaggedTxPortEntry = _FsLldpStatsTaggedTxPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 158, 5, 4, 1)
)
if mibBuilder.loadTexts:
    fsLldpStatsTaggedTxPortEntry.setStatus("current")
_FsLldpStatsTaggedTxPortFramesTotal_Type = Counter32
_FsLldpStatsTaggedTxPortFramesTotal_Object = MibTableColumn
fsLldpStatsTaggedTxPortFramesTotal = _FsLldpStatsTaggedTxPortFramesTotal_Object(
    (1, 3, 6, 1, 4, 1, 2076, 158, 5, 4, 1, 1),
    _FsLldpStatsTaggedTxPortFramesTotal_Type()
)
fsLldpStatsTaggedTxPortFramesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLldpStatsTaggedTxPortFramesTotal.setStatus("current")
if mibBuilder.loadTexts:
    fsLldpStatsTaggedTxPortFramesTotal.setUnits("LLDP frames")
lldpLocManAddrEntry.registerAugmentions(
    ("ARICENT-LLDP-MIB",
     "fsLldpManAddrConfigEntry")
)
fsLldpManAddrConfigEntry.setIndexNames(*lldpLocManAddrEntry.getIndexNames())
lldpV2StatsTxPortEntry.registerAugmentions(
    ("ARICENT-LLDP-MIB",
     "fsLldpStatsTaggedTxPortEntry")
)
fsLldpStatsTaggedTxPortEntry.setIndexNames(*lldpV2StatsTxPortEntry.getIndexNames())

# Managed Objects groups


# Notification objects

fsLldpRemTablesChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 158, 4, 0, 1)
)
fsLldpRemTablesChange.setObjects(
      *(("LLDP-MIB", "lldpStatsRemTablesInserts"),
        ("LLDP-MIB", "lldpStatsRemTablesDeletes"),
        ("LLDP-MIB", "lldpStatsRemTablesDrops"),
        ("LLDP-MIB", "lldpStatsRemTablesAgeouts"),
        ("ARICENT-LLDP-MIB", "fsLldpStatsRemTablesUpdates"))
)
if mibBuilder.loadTexts:
    fsLldpRemTablesChange.setStatus(
        "current"
    )

fsLldpExceedsMaxFrameSize = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 158, 4, 0, 2)
)
fsLldpExceedsMaxFrameSize.setObjects(
    ("LLDP-MIB", "lldpLocPortId")
)
if mibBuilder.loadTexts:
    fsLldpExceedsMaxFrameSize.setStatus(
        "current"
    )

fsLldpDupChassisId = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 158, 4, 0, 3)
)
fsLldpDupChassisId.setObjects(
      *(("LLDP-MIB", "lldpRemChassisId"),
        ("LLDP-MIB", "lldpRemPortId"))
)
if mibBuilder.loadTexts:
    fsLldpDupChassisId.setStatus(
        "current"
    )

fsLldpDupSystemName = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 158, 4, 0, 4)
)
fsLldpDupSystemName.setObjects(
      *(("LLDP-MIB", "lldpRemChassisId"),
        ("LLDP-MIB", "lldpRemPortId"),
        ("LLDP-MIB", "lldpRemSysName"))
)
if mibBuilder.loadTexts:
    fsLldpDupSystemName.setStatus(
        "current"
    )

fsLldpDupManagmentAddress = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 158, 4, 0, 5)
)
fsLldpDupManagmentAddress.setObjects(
      *(("LLDP-MIB", "lldpRemChassisId"),
        ("LLDP-MIB", "lldpRemPortId"),
        ("LLDP-MIB", "lldpRemManAddrIfId"))
)
if mibBuilder.loadTexts:
    fsLldpDupManagmentAddress.setStatus(
        "current"
    )

fsLldpMisConfigPortVlanID = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 158, 4, 0, 6)
)
fsLldpMisConfigPortVlanID.setObjects(
      *(("LLDP-MIB", "lldpRemChassisId"),
        ("LLDP-MIB", "lldpRemPortId"),
        ("LLDP-EXT-DOT1-MIB", "lldpXdot1RemPortVlanId"))
)
if mibBuilder.loadTexts:
    fsLldpMisConfigPortVlanID.setStatus(
        "current"
    )

fsLldpMisConfigPortProtoVlanID = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 158, 4, 0, 7)
)
fsLldpMisConfigPortProtoVlanID.setObjects(
      *(("LLDP-MIB", "lldpRemChassisId"),
        ("LLDP-MIB", "lldpRemPortId"),
        ("LLDP-EXT-DOT1-MIB", "lldpXdot1RemProtoVlanSupported"))
)
if mibBuilder.loadTexts:
    fsLldpMisConfigPortProtoVlanID.setStatus(
        "current"
    )

fsLldpMisConfigVlanName = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 158, 4, 0, 8)
)
fsLldpMisConfigVlanName.setObjects(
      *(("LLDP-MIB", "lldpRemChassisId"),
        ("LLDP-MIB", "lldpRemPortId"),
        ("LLDP-EXT-DOT1-MIB", "lldpXdot1RemVlanName"))
)
if mibBuilder.loadTexts:
    fsLldpMisConfigVlanName.setStatus(
        "current"
    )

fsLldpMisConfigProtocolIdentity = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 158, 4, 0, 9)
)
fsLldpMisConfigProtocolIdentity.setObjects(
      *(("LLDP-MIB", "lldpRemChassisId"),
        ("LLDP-MIB", "lldpRemPortId"),
        ("LLDP-EXT-DOT1-MIB", "lldpXdot1RemProtocolId"))
)
if mibBuilder.loadTexts:
    fsLldpMisConfigProtocolIdentity.setStatus(
        "current"
    )

fsLldpMisConfigLinkAggStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 158, 4, 0, 10)
)
fsLldpMisConfigLinkAggStatus.setObjects(
      *(("LLDP-MIB", "lldpRemChassisId"),
        ("LLDP-MIB", "lldpRemPortId"),
        ("LLDP-EXT-DOT3-MIB", "lldpXdot3RemLinkAggStatus"))
)
if mibBuilder.loadTexts:
    fsLldpMisConfigLinkAggStatus.setStatus(
        "current"
    )

fsLldpMisConfigPowerMDI = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 158, 4, 0, 11)
)
fsLldpMisConfigPowerMDI.setObjects(
      *(("LLDP-MIB", "lldpRemChassisId"),
        ("LLDP-MIB", "lldpRemPortId"),
        ("LLDP-EXT-DOT3-MIB", "lldpXdot3RemPowerClass"))
)
if mibBuilder.loadTexts:
    fsLldpMisConfigPowerMDI.setStatus(
        "current"
    )

fsLldpMisConfigMaxFrameSize = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 158, 4, 0, 12)
)
fsLldpMisConfigMaxFrameSize.setObjects(
      *(("LLDP-MIB", "lldpRemChassisId"),
        ("LLDP-MIB", "lldpRemPortId"),
        ("LLDP-EXT-DOT3-MIB", "lldpXdot3RemMaxFrameSize"))
)
if mibBuilder.loadTexts:
    fsLldpMisConfigMaxFrameSize.setStatus(
        "current"
    )

fsLldpMisConfigOperMauType = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 158, 4, 0, 13)
)
fsLldpMisConfigOperMauType.setObjects(
      *(("LLDP-MIB", "lldpRemChassisId"),
        ("LLDP-MIB", "lldpRemPortId"),
        ("LLDP-EXT-DOT3-MIB", "lldpXdot3RemPortOperMauType"))
)
if mibBuilder.loadTexts:
    fsLldpMisConfigOperMauType.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-LLDP-MIB",
    **{"fslldp": fslldp,
       "fsLldpSystem": fsLldpSystem,
       "fsLldpSystemControl": fsLldpSystemControl,
       "fsLldpModuleStatus": fsLldpModuleStatus,
       "fsLldpTraceInput": fsLldpTraceInput,
       "fsLldpTraceOption": fsLldpTraceOption,
       "fsLldpTraceLevel": fsLldpTraceLevel,
       "fsLldpTagStatus": fsLldpTagStatus,
       "fsLldpConfiguredMgmtIpv4Address": fsLldpConfiguredMgmtIpv4Address,
       "fsLldpConfiguredMgmtIpv6Address": fsLldpConfiguredMgmtIpv6Address,
       "fsLldpTLV": fsLldpTLV,
       "fsLldpLocChassisIdSubtype": fsLldpLocChassisIdSubtype,
       "fsLldpLocChassisId": fsLldpLocChassisId,
       "fsLldpLocPortTable": fsLldpLocPortTable,
       "fsLldpLocPortEntry": fsLldpLocPortEntry,
       "fsLldpLocPortIdSubtype": fsLldpLocPortIdSubtype,
       "fsLldpLocPortId": fsLldpLocPortId,
       "fsLldpPortConfigNotificationType": fsLldpPortConfigNotificationType,
       "fsLldpLocPortDstMac": fsLldpLocPortDstMac,
       "fsLldpMedAdminStatus": fsLldpMedAdminStatus,
       "fsLldpManAddrConfigTable": fsLldpManAddrConfigTable,
       "fsLldpManAddrConfigEntry": fsLldpManAddrConfigEntry,
       "fsLldpManAddrConfigOperStatus": fsLldpManAddrConfigOperStatus,
       "fsLldpStatistics": fsLldpStatistics,
       "fsLldpMemAllocFailure": fsLldpMemAllocFailure,
       "fsLldpInputQOverFlows": fsLldpInputQOverFlows,
       "fsLldpStatsRemTablesUpdates": fsLldpStatsRemTablesUpdates,
       "fsLldpClearStats": fsLldpClearStats,
       "fsLldpNotification": fsLldpNotification,
       "fsLldpTraps": fsLldpTraps,
       "fsLldpRemTablesChange": fsLldpRemTablesChange,
       "fsLldpExceedsMaxFrameSize": fsLldpExceedsMaxFrameSize,
       "fsLldpDupChassisId": fsLldpDupChassisId,
       "fsLldpDupSystemName": fsLldpDupSystemName,
       "fsLldpDupManagmentAddress": fsLldpDupManagmentAddress,
       "fsLldpMisConfigPortVlanID": fsLldpMisConfigPortVlanID,
       "fsLldpMisConfigPortProtoVlanID": fsLldpMisConfigPortProtoVlanID,
       "fsLldpMisConfigVlanName": fsLldpMisConfigVlanName,
       "fsLldpMisConfigProtocolIdentity": fsLldpMisConfigProtocolIdentity,
       "fsLldpMisConfigLinkAggStatus": fsLldpMisConfigLinkAggStatus,
       "fsLldpMisConfigPowerMDI": fsLldpMisConfigPowerMDI,
       "fsLldpMisConfigMaxFrameSize": fsLldpMisConfigMaxFrameSize,
       "fsLldpMisConfigOperMauType": fsLldpMisConfigOperMauType,
       "fslldpv2Config": fslldpv2Config,
       "fslldpv2Version": fslldpv2Version,
       "fslldpv2ConfigPortMapTable": fslldpv2ConfigPortMapTable,
       "fslldpv2ConfigPortMapEntry": fslldpv2ConfigPortMapEntry,
       "fslldpv2ConfigPortMapIfIndex": fslldpv2ConfigPortMapIfIndex,
       "fslldpv2ConfigPortMapDestMacAddress": fslldpv2ConfigPortMapDestMacAddress,
       "fslldpv2ConfigPortMapNum": fslldpv2ConfigPortMapNum,
       "fslldpv2ConfigPortRowStatus": fslldpv2ConfigPortRowStatus,
       "fslldpV2DestAddressTable": fslldpV2DestAddressTable,
       "fslldpV2DestAddressTableEntry": fslldpV2DestAddressTableEntry,
       "fslldpV2AddressTableIndex": fslldpV2AddressTableIndex,
       "fslldpV2DestMacAddress": fslldpV2DestMacAddress,
       "fslldpv2DestRowStatus": fslldpv2DestRowStatus,
       "fsLldpStatsTaggedTxPortTable": fsLldpStatsTaggedTxPortTable,
       "fsLldpStatsTaggedTxPortEntry": fsLldpStatsTaggedTxPortEntry,
       "fsLldpStatsTaggedTxPortFramesTotal": fsLldpStatsTaggedTxPortFramesTotal}
)
