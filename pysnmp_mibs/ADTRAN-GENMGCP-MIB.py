# SNMP MIB module (ADTRAN-GENMGCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENMGCP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:33:04 2025
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

(AdGenVoipCodecProfileName,
 AdGenVoipCodecProfileType,
 AdGenVoipMediaProfileName) = mibBuilder.importSymbols(
    "ADTRAN-GENVOIP-MIB",
    "AdGenVoipCodecProfileName",
    "AdGenVoipCodecProfileType",
    "AdGenVoipMediaProfileName")

(adGenMgcp,
 adGenMgcpID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenMgcp",
    "adGenMgcpID")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

adGenMgcpEntity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 54, 1)
)
if mibBuilder.loadTexts:
    adGenMgcpEntity.setRevisions(
        ("2017-02-16 00:00",
         "2014-03-18 00:00",
         "2013-07-18 00:00",
         "2013-05-23 00:00",
         "2013-01-21 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AdGenMgcpProfileName(TextualConvention, OctetString):
    status = "current"
    displayHint = "40a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )



# MIB Managed Objects in the order of their OIDs

_AdGenMgcpProvisioning_ObjectIdentity = ObjectIdentity
adGenMgcpProvisioning = _AdGenMgcpProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1)
)
_AdGenMgcpProfileProv_ObjectIdentity = ObjectIdentity
adGenMgcpProfileProv = _AdGenMgcpProfileProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 1)
)
_AdGenMgcpProfileProvCurrentNumber_Type = Integer32
_AdGenMgcpProfileProvCurrentNumber_Object = MibScalar
adGenMgcpProfileProvCurrentNumber = _AdGenMgcpProfileProvCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 1, 1),
    _AdGenMgcpProfileProvCurrentNumber_Type()
)
adGenMgcpProfileProvCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMgcpProfileProvCurrentNumber.setStatus("current")
_AdGenMgcpProfileProvLastCreateError_Type = DisplayString
_AdGenMgcpProfileProvLastCreateError_Object = MibScalar
adGenMgcpProfileProvLastCreateError = _AdGenMgcpProfileProvLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 1, 2),
    _AdGenMgcpProfileProvLastCreateError_Type()
)
adGenMgcpProfileProvLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMgcpProfileProvLastCreateError.setStatus("current")
_AdGenMgcpProfileProvTable_Object = MibTable
adGenMgcpProfileProvTable = _AdGenMgcpProfileProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 1, 3)
)
if mibBuilder.loadTexts:
    adGenMgcpProfileProvTable.setStatus("current")
_AdGenMgcpProfileProvEntry_Object = MibTableRow
adGenMgcpProfileProvEntry = _AdGenMgcpProfileProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 1, 3, 1)
)
adGenMgcpProfileProvEntry.setIndexNames(
    (1, "ADTRAN-GENMGCP-MIB", "adGenMgcpProfileEntryIndex"),
)
if mibBuilder.loadTexts:
    adGenMgcpProfileProvEntry.setStatus("current")
_AdGenMgcpProfileEntryIndex_Type = AdGenMgcpProfileName
_AdGenMgcpProfileEntryIndex_Object = MibTableColumn
adGenMgcpProfileEntryIndex = _AdGenMgcpProfileEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 1, 3, 1, 1),
    _AdGenMgcpProfileEntryIndex_Type()
)
adGenMgcpProfileEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenMgcpProfileEntryIndex.setStatus("current")
_AdGenMgcpProfileRowStatus_Type = RowStatus
_AdGenMgcpProfileRowStatus_Object = MibTableColumn
adGenMgcpProfileRowStatus = _AdGenMgcpProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 1, 3, 1, 2),
    _AdGenMgcpProfileRowStatus_Type()
)
adGenMgcpProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMgcpProfileRowStatus.setStatus("current")
_AdGenMgcpProfileLastErrorString_Type = DisplayString
_AdGenMgcpProfileLastErrorString_Object = MibTableColumn
adGenMgcpProfileLastErrorString = _AdGenMgcpProfileLastErrorString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 1, 3, 1, 3),
    _AdGenMgcpProfileLastErrorString_Type()
)
adGenMgcpProfileLastErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMgcpProfileLastErrorString.setStatus("current")
_AdGenMgcpProfileCallAgentPrimary_Type = DisplayString
_AdGenMgcpProfileCallAgentPrimary_Object = MibTableColumn
adGenMgcpProfileCallAgentPrimary = _AdGenMgcpProfileCallAgentPrimary_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 1, 3, 1, 4),
    _AdGenMgcpProfileCallAgentPrimary_Type()
)
adGenMgcpProfileCallAgentPrimary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMgcpProfileCallAgentPrimary.setStatus("current")


class _AdGenMgcpProfileCallAgentPrimaryUdp_Type(Integer32):
    """Custom type adGenMgcpProfileCallAgentPrimaryUdp based on Integer32"""
    defaultValue = 2727

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdGenMgcpProfileCallAgentPrimaryUdp_Type.__name__ = "Integer32"
_AdGenMgcpProfileCallAgentPrimaryUdp_Object = MibTableColumn
adGenMgcpProfileCallAgentPrimaryUdp = _AdGenMgcpProfileCallAgentPrimaryUdp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 1, 3, 1, 5),
    _AdGenMgcpProfileCallAgentPrimaryUdp_Type()
)
adGenMgcpProfileCallAgentPrimaryUdp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMgcpProfileCallAgentPrimaryUdp.setStatus("current")
_AdGenMgcpProfileCallAgentSecondary_Type = DisplayString
_AdGenMgcpProfileCallAgentSecondary_Object = MibTableColumn
adGenMgcpProfileCallAgentSecondary = _AdGenMgcpProfileCallAgentSecondary_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 1, 3, 1, 6),
    _AdGenMgcpProfileCallAgentSecondary_Type()
)
adGenMgcpProfileCallAgentSecondary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMgcpProfileCallAgentSecondary.setStatus("current")


class _AdGenMgcpProfileCallAgentSecondaryUdp_Type(Integer32):
    """Custom type adGenMgcpProfileCallAgentSecondaryUdp based on Integer32"""
    defaultValue = 2727

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdGenMgcpProfileCallAgentSecondaryUdp_Type.__name__ = "Integer32"
_AdGenMgcpProfileCallAgentSecondaryUdp_Object = MibTableColumn
adGenMgcpProfileCallAgentSecondaryUdp = _AdGenMgcpProfileCallAgentSecondaryUdp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 1, 3, 1, 7),
    _AdGenMgcpProfileCallAgentSecondaryUdp_Type()
)
adGenMgcpProfileCallAgentSecondaryUdp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMgcpProfileCallAgentSecondaryUdp.setStatus("current")


class _AdGenMgcpProfileShutdown_Type(Integer32):
    """Custom type adGenMgcpProfileShutdown based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noShutdown", 1),
          ("shutdown", 2))
    )


_AdGenMgcpProfileShutdown_Type.__name__ = "Integer32"
_AdGenMgcpProfileShutdown_Object = MibTableColumn
adGenMgcpProfileShutdown = _AdGenMgcpProfileShutdown_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 1, 3, 1, 8),
    _AdGenMgcpProfileShutdown_Type()
)
adGenMgcpProfileShutdown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMgcpProfileShutdown.setStatus("current")


class _AdGenMgcpProfileBracketedIp_Type(TruthValue):
    """Custom type adGenMgcpProfileBracketedIp based on TruthValue"""
    defaultValue = 1


_AdGenMgcpProfileBracketedIp_Type.__name__ = "TruthValue"
_AdGenMgcpProfileBracketedIp_Object = MibTableColumn
adGenMgcpProfileBracketedIp = _AdGenMgcpProfileBracketedIp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 1, 3, 1, 9),
    _AdGenMgcpProfileBracketedIp_Type()
)
adGenMgcpProfileBracketedIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMgcpProfileBracketedIp.setStatus("current")


class _AdGenMgcpProfileStandard_Type(Integer32):
    """Custom type adGenMgcpProfileStandard based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rfc3435", 1),
          ("ncs", 2))
    )


_AdGenMgcpProfileStandard_Type.__name__ = "Integer32"
_AdGenMgcpProfileStandard_Object = MibTableColumn
adGenMgcpProfileStandard = _AdGenMgcpProfileStandard_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 1, 3, 1, 10),
    _AdGenMgcpProfileStandard_Type()
)
adGenMgcpProfileStandard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMgcpProfileStandard.setStatus("current")


class _AdGenMgcpProfileMgcpDscp_Type(Integer32):
    """Custom type adGenMgcpProfileMgcpDscp based on Integer32"""
    defaultValue = 46

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AdGenMgcpProfileMgcpDscp_Type.__name__ = "Integer32"
_AdGenMgcpProfileMgcpDscp_Object = MibTableColumn
adGenMgcpProfileMgcpDscp = _AdGenMgcpProfileMgcpDscp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 1, 3, 1, 11),
    _AdGenMgcpProfileMgcpDscp_Type()
)
adGenMgcpProfileMgcpDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMgcpProfileMgcpDscp.setStatus("current")


class _AdGenMgcpProfileRtpDscp_Type(Integer32):
    """Custom type adGenMgcpProfileRtpDscp based on Integer32"""
    defaultValue = 46

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AdGenMgcpProfileRtpDscp_Type.__name__ = "Integer32"
_AdGenMgcpProfileRtpDscp_Object = MibTableColumn
adGenMgcpProfileRtpDscp = _AdGenMgcpProfileRtpDscp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 1, 3, 1, 12),
    _AdGenMgcpProfileRtpDscp_Type()
)
adGenMgcpProfileRtpDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMgcpProfileRtpDscp.setStatus("current")


class _AdGenMgcpProfileGatewayUdp_Type(Integer32):
    """Custom type adGenMgcpProfileGatewayUdp based on Integer32"""
    defaultValue = 2427

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdGenMgcpProfileGatewayUdp_Type.__name__ = "Integer32"
_AdGenMgcpProfileGatewayUdp_Object = MibTableColumn
adGenMgcpProfileGatewayUdp = _AdGenMgcpProfileGatewayUdp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 1, 3, 1, 13),
    _AdGenMgcpProfileGatewayUdp_Type()
)
adGenMgcpProfileGatewayUdp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMgcpProfileGatewayUdp.setStatus("current")


class _AdGenMgcpProfileRtpUdpOffset_Type(Integer32):
    """Custom type adGenMgcpProfileRtpUdpOffset based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdGenMgcpProfileRtpUdpOffset_Type.__name__ = "Integer32"
_AdGenMgcpProfileRtpUdpOffset_Object = MibTableColumn
adGenMgcpProfileRtpUdpOffset = _AdGenMgcpProfileRtpUdpOffset_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 1, 3, 1, 14),
    _AdGenMgcpProfileRtpUdpOffset_Type()
)
adGenMgcpProfileRtpUdpOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMgcpProfileRtpUdpOffset.setStatus("current")


class _AdGenMgcpProfilePersistentNotifyHangDown_Type(Integer32):
    """Custom type adGenMgcpProfilePersistentNotifyHangDown based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enbled", 2))
    )


_AdGenMgcpProfilePersistentNotifyHangDown_Type.__name__ = "Integer32"
_AdGenMgcpProfilePersistentNotifyHangDown_Object = MibTableColumn
adGenMgcpProfilePersistentNotifyHangDown = _AdGenMgcpProfilePersistentNotifyHangDown_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 1, 3, 1, 15),
    _AdGenMgcpProfilePersistentNotifyHangDown_Type()
)
adGenMgcpProfilePersistentNotifyHangDown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMgcpProfilePersistentNotifyHangDown.setStatus("current")


class _AdGenMgcpProfilePersistentNotifyHangUp_Type(Integer32):
    """Custom type adGenMgcpProfilePersistentNotifyHangUp based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enbled", 2))
    )


_AdGenMgcpProfilePersistentNotifyHangUp_Type.__name__ = "Integer32"
_AdGenMgcpProfilePersistentNotifyHangUp_Object = MibTableColumn
adGenMgcpProfilePersistentNotifyHangUp = _AdGenMgcpProfilePersistentNotifyHangUp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 1, 3, 1, 16),
    _AdGenMgcpProfilePersistentNotifyHangUp_Type()
)
adGenMgcpProfilePersistentNotifyHangUp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMgcpProfilePersistentNotifyHangUp.setStatus("current")


class _AdGenMgcpProfilePersistentNotifyHookFlash_Type(Integer32):
    """Custom type adGenMgcpProfilePersistentNotifyHookFlash based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enbled", 2))
    )


_AdGenMgcpProfilePersistentNotifyHookFlash_Type.__name__ = "Integer32"
_AdGenMgcpProfilePersistentNotifyHookFlash_Object = MibTableColumn
adGenMgcpProfilePersistentNotifyHookFlash = _AdGenMgcpProfilePersistentNotifyHookFlash_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 1, 3, 1, 17),
    _AdGenMgcpProfilePersistentNotifyHookFlash_Type()
)
adGenMgcpProfilePersistentNotifyHookFlash.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMgcpProfilePersistentNotifyHookFlash.setStatus("current")


class _AdGenMgcpProfileRetransmitDelay_Type(Integer32):
    """Custom type adGenMgcpProfileRetransmitDelay based on Integer32"""
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
        *(("exponentialBackoff", 1),
          ("ms100", 2),
          ("ms250", 3),
          ("ms500", 4),
          ("sec1", 5),
          ("sec2", 6),
          ("sec4", 7))
    )


_AdGenMgcpProfileRetransmitDelay_Type.__name__ = "Integer32"
_AdGenMgcpProfileRetransmitDelay_Object = MibTableColumn
adGenMgcpProfileRetransmitDelay = _AdGenMgcpProfileRetransmitDelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 1, 3, 1, 18),
    _AdGenMgcpProfileRetransmitDelay_Type()
)
adGenMgcpProfileRetransmitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMgcpProfileRetransmitDelay.setStatus("current")


class _AdGenMgcpProfileMax1_Type(Integer32):
    """Custom type adGenMgcpProfileMax1 based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AdGenMgcpProfileMax1_Type.__name__ = "Integer32"
_AdGenMgcpProfileMax1_Object = MibTableColumn
adGenMgcpProfileMax1 = _AdGenMgcpProfileMax1_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 1, 3, 1, 19),
    _AdGenMgcpProfileMax1_Type()
)
adGenMgcpProfileMax1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMgcpProfileMax1.setStatus("current")


class _AdGenMgcpProfileMax2_Type(Integer32):
    """Custom type adGenMgcpProfileMax2 based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AdGenMgcpProfileMax2_Type.__name__ = "Integer32"
_AdGenMgcpProfileMax2_Object = MibTableColumn
adGenMgcpProfileMax2 = _AdGenMgcpProfileMax2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 1, 3, 1, 20),
    _AdGenMgcpProfileMax2_Type()
)
adGenMgcpProfileMax2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMgcpProfileMax2.setStatus("current")


class _AdGenMgcpProfileLocalDomainType_Type(Integer32):
    """Custom type adGenMgcpProfileLocalDomainType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mediaGateway", 1),
          ("userDefined", 2))
    )


_AdGenMgcpProfileLocalDomainType_Type.__name__ = "Integer32"
_AdGenMgcpProfileLocalDomainType_Object = MibTableColumn
adGenMgcpProfileLocalDomainType = _AdGenMgcpProfileLocalDomainType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 1, 3, 1, 21),
    _AdGenMgcpProfileLocalDomainType_Type()
)
adGenMgcpProfileLocalDomainType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMgcpProfileLocalDomainType.setStatus("current")


class _AdGenMgcpProfileLocalDomainAddress_Type(DisplayString):
    """Custom type adGenMgcpProfileLocalDomainAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_AdGenMgcpProfileLocalDomainAddress_Type.__name__ = "DisplayString"
_AdGenMgcpProfileLocalDomainAddress_Object = MibTableColumn
adGenMgcpProfileLocalDomainAddress = _AdGenMgcpProfileLocalDomainAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 1, 3, 1, 22),
    _AdGenMgcpProfileLocalDomainAddress_Type()
)
adGenMgcpProfileLocalDomainAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMgcpProfileLocalDomainAddress.setStatus("current")


class _AdGenMgcpProfileTerminationIdBase_Type(DisplayString):
    """Custom type adGenMgcpProfileTerminationIdBase based on DisplayString"""
    defaultValue = OctetString("aaln/")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_AdGenMgcpProfileTerminationIdBase_Type.__name__ = "DisplayString"
_AdGenMgcpProfileTerminationIdBase_Object = MibTableColumn
adGenMgcpProfileTerminationIdBase = _AdGenMgcpProfileTerminationIdBase_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 1, 3, 1, 23),
    _AdGenMgcpProfileTerminationIdBase_Type()
)
adGenMgcpProfileTerminationIdBase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMgcpProfileTerminationIdBase.setStatus("current")


class _AdGenMgcpProfileRFC2833Signaling_Type(Integer32):
    """Custom type adGenMgcpProfileRFC2833Signaling based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enbled", 2))
    )


_AdGenMgcpProfileRFC2833Signaling_Type.__name__ = "Integer32"
_AdGenMgcpProfileRFC2833Signaling_Object = MibTableColumn
adGenMgcpProfileRFC2833Signaling = _AdGenMgcpProfileRFC2833Signaling_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 1, 3, 1, 24),
    _AdGenMgcpProfileRFC2833Signaling_Type()
)
adGenMgcpProfileRFC2833Signaling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMgcpProfileRFC2833Signaling.setStatus("current")
_AdGenMgcpEndpointProv_ObjectIdentity = ObjectIdentity
adGenMgcpEndpointProv = _AdGenMgcpEndpointProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 2)
)
_AdGenMgcpEndpointProvCurrentNumber_Type = Integer32
_AdGenMgcpEndpointProvCurrentNumber_Object = MibScalar
adGenMgcpEndpointProvCurrentNumber = _AdGenMgcpEndpointProvCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 2, 1),
    _AdGenMgcpEndpointProvCurrentNumber_Type()
)
adGenMgcpEndpointProvCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMgcpEndpointProvCurrentNumber.setStatus("current")
_AdGenMgcpEndpointProvLastCreateError_Type = DisplayString
_AdGenMgcpEndpointProvLastCreateError_Object = MibScalar
adGenMgcpEndpointProvLastCreateError = _AdGenMgcpEndpointProvLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 2, 2),
    _AdGenMgcpEndpointProvLastCreateError_Type()
)
adGenMgcpEndpointProvLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMgcpEndpointProvLastCreateError.setStatus("current")
_AdGenMgcpEndpointProvTable_Object = MibTable
adGenMgcpEndpointProvTable = _AdGenMgcpEndpointProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 2, 3)
)
if mibBuilder.loadTexts:
    adGenMgcpEndpointProvTable.setStatus("current")
_AdGenMgcpEndpointProvEntry_Object = MibTableRow
adGenMgcpEndpointProvEntry = _AdGenMgcpEndpointProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 2, 3, 1)
)
adGenMgcpEndpointProvEntry.setIndexNames(
    (0, "ADTRAN-GENMGCP-MIB", "adGenMgcpEndpointEntryIndex"),
)
if mibBuilder.loadTexts:
    adGenMgcpEndpointProvEntry.setStatus("current")
_AdGenMgcpEndpointEntryIndex_Type = InterfaceIndexOrZero
_AdGenMgcpEndpointEntryIndex_Object = MibTableColumn
adGenMgcpEndpointEntryIndex = _AdGenMgcpEndpointEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 2, 3, 1, 1),
    _AdGenMgcpEndpointEntryIndex_Type()
)
adGenMgcpEndpointEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenMgcpEndpointEntryIndex.setStatus("current")
_AdGenMgcpEndpointRowStatus_Type = RowStatus
_AdGenMgcpEndpointRowStatus_Object = MibTableColumn
adGenMgcpEndpointRowStatus = _AdGenMgcpEndpointRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 2, 3, 1, 2),
    _AdGenMgcpEndpointRowStatus_Type()
)
adGenMgcpEndpointRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMgcpEndpointRowStatus.setStatus("current")
_AdGenMgcpEndpointLastErrorString_Type = DisplayString
_AdGenMgcpEndpointLastErrorString_Object = MibTableColumn
adGenMgcpEndpointLastErrorString = _AdGenMgcpEndpointLastErrorString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 2, 3, 1, 3),
    _AdGenMgcpEndpointLastErrorString_Type()
)
adGenMgcpEndpointLastErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMgcpEndpointLastErrorString.setStatus("current")


class _AdGenMgcpEndpointFxsPort_Type(InterfaceIndexOrZero):
    """Custom type adGenMgcpEndpointFxsPort based on InterfaceIndexOrZero"""
    defaultValue = 0


_AdGenMgcpEndpointFxsPort_Type.__name__ = "InterfaceIndexOrZero"
_AdGenMgcpEndpointFxsPort_Object = MibTableColumn
adGenMgcpEndpointFxsPort = _AdGenMgcpEndpointFxsPort_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 2, 3, 1, 4),
    _AdGenMgcpEndpointFxsPort_Type()
)
adGenMgcpEndpointFxsPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMgcpEndpointFxsPort.setStatus("current")
_AdGenMgcpEndpointMgcpProfile_Type = AdGenMgcpProfileName
_AdGenMgcpEndpointMgcpProfile_Object = MibTableColumn
adGenMgcpEndpointMgcpProfile = _AdGenMgcpEndpointMgcpProfile_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 2, 3, 1, 5),
    _AdGenMgcpEndpointMgcpProfile_Type()
)
adGenMgcpEndpointMgcpProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMgcpEndpointMgcpProfile.setStatus("current")


class _AdGenMgcpEndpointBlockCallerId_Type(TruthValue):
    """Custom type adGenMgcpEndpointBlockCallerId based on TruthValue"""
    defaultValue = 1


_AdGenMgcpEndpointBlockCallerId_Type.__name__ = "TruthValue"
_AdGenMgcpEndpointBlockCallerId_Object = MibTableColumn
adGenMgcpEndpointBlockCallerId = _AdGenMgcpEndpointBlockCallerId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 2, 3, 1, 6),
    _AdGenMgcpEndpointBlockCallerId_Type()
)
adGenMgcpEndpointBlockCallerId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMgcpEndpointBlockCallerId.setStatus("current")


class _AdGenMgcpEndpointDescription_Type(DisplayString):
    """Custom type adGenMgcpEndpointDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AdGenMgcpEndpointDescription_Type.__name__ = "DisplayString"
_AdGenMgcpEndpointDescription_Object = MibTableColumn
adGenMgcpEndpointDescription = _AdGenMgcpEndpointDescription_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 2, 3, 1, 7),
    _AdGenMgcpEndpointDescription_Type()
)
adGenMgcpEndpointDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMgcpEndpointDescription.setStatus("current")


class _AdGenMgcpEndpointDisplayString_Type(DisplayString):
    """Custom type adGenMgcpEndpointDisplayString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AdGenMgcpEndpointDisplayString_Type.__name__ = "DisplayString"
_AdGenMgcpEndpointDisplayString_Object = MibTableColumn
adGenMgcpEndpointDisplayString = _AdGenMgcpEndpointDisplayString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 2, 3, 1, 8),
    _AdGenMgcpEndpointDisplayString_Type()
)
adGenMgcpEndpointDisplayString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMgcpEndpointDisplayString.setStatus("current")


class _AdGenMgcpEndpointFwdDisconnect_Type(Integer32):
    """Custom type adGenMgcpEndpointFwdDisconnect based on Integer32"""
    defaultValue = 6

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
        *(("delay250", 1),
          ("delay500", 2),
          ("delay750", 3),
          ("delay900", 4),
          ("delay1000", 5),
          ("delay2000", 6))
    )


_AdGenMgcpEndpointFwdDisconnect_Type.__name__ = "Integer32"
_AdGenMgcpEndpointFwdDisconnect_Object = MibTableColumn
adGenMgcpEndpointFwdDisconnect = _AdGenMgcpEndpointFwdDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 2, 3, 1, 9),
    _AdGenMgcpEndpointFwdDisconnect_Type()
)
adGenMgcpEndpointFwdDisconnect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMgcpEndpointFwdDisconnect.setStatus("current")
if mibBuilder.loadTexts:
    adGenMgcpEndpointFwdDisconnect.setUnits("milliseconds")
_AdGenMgcpEndpointMediaProfile_Type = AdGenVoipMediaProfileName
_AdGenMgcpEndpointMediaProfile_Object = MibTableColumn
adGenMgcpEndpointMediaProfile = _AdGenMgcpEndpointMediaProfile_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 2, 3, 1, 10),
    _AdGenMgcpEndpointMediaProfile_Type()
)
adGenMgcpEndpointMediaProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMgcpEndpointMediaProfile.setStatus("current")
_AdGenMgcpEndpointCodecListProfile_Type = AdGenVoipCodecProfileName
_AdGenMgcpEndpointCodecListProfile_Object = MibTableColumn
adGenMgcpEndpointCodecListProfile = _AdGenMgcpEndpointCodecListProfile_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 1, 2, 3, 1, 11),
    _AdGenMgcpEndpointCodecListProfile_Type()
)
adGenMgcpEndpointCodecListProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMgcpEndpointCodecListProfile.setStatus("current")
_AdGenMgcpStatus_ObjectIdentity = ObjectIdentity
adGenMgcpStatus = _AdGenMgcpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 2)
)
_AdGenMgcpEndpointStatus_ObjectIdentity = ObjectIdentity
adGenMgcpEndpointStatus = _AdGenMgcpEndpointStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 2, 1)
)
_AdGenMgcpEndpointStatusTable_Object = MibTable
adGenMgcpEndpointStatusTable = _AdGenMgcpEndpointStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 2, 1, 1)
)
if mibBuilder.loadTexts:
    adGenMgcpEndpointStatusTable.setStatus("current")
_AdGenMgcpEndpointStatusEntry_Object = MibTableRow
adGenMgcpEndpointStatusEntry = _AdGenMgcpEndpointStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 2, 1, 1, 1)
)
adGenMgcpEndpointStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENMGCP-MIB", "adGenMgcpEndpointStatusEntryIndex"),
)
if mibBuilder.loadTexts:
    adGenMgcpEndpointStatusEntry.setStatus("current")
_AdGenMgcpEndpointStatusEntryIndex_Type = InterfaceIndexOrZero
_AdGenMgcpEndpointStatusEntryIndex_Object = MibTableColumn
adGenMgcpEndpointStatusEntryIndex = _AdGenMgcpEndpointStatusEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 2, 1, 1, 1, 1),
    _AdGenMgcpEndpointStatusEntryIndex_Type()
)
adGenMgcpEndpointStatusEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenMgcpEndpointStatusEntryIndex.setStatus("current")
_AdGenMgcpEndpointStatusFXSPort_Type = InterfaceIndexOrZero
_AdGenMgcpEndpointStatusFXSPort_Object = MibTableColumn
adGenMgcpEndpointStatusFXSPort = _AdGenMgcpEndpointStatusFXSPort_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 2, 1, 1, 1, 2),
    _AdGenMgcpEndpointStatusFXSPort_Type()
)
adGenMgcpEndpointStatusFXSPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMgcpEndpointStatusFXSPort.setStatus("current")
_AdGenMgcpEndpointStatusName_Type = DisplayString
_AdGenMgcpEndpointStatusName_Object = MibTableColumn
adGenMgcpEndpointStatusName = _AdGenMgcpEndpointStatusName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 2, 1, 1, 1, 3),
    _AdGenMgcpEndpointStatusName_Type()
)
adGenMgcpEndpointStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMgcpEndpointStatusName.setStatus("current")
_AdGenMgcpEndpointStatusConnectedProfile_Type = DisplayString
_AdGenMgcpEndpointStatusConnectedProfile_Object = MibTableColumn
adGenMgcpEndpointStatusConnectedProfile = _AdGenMgcpEndpointStatusConnectedProfile_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 2, 1, 1, 1, 4),
    _AdGenMgcpEndpointStatusConnectedProfile_Type()
)
adGenMgcpEndpointStatusConnectedProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMgcpEndpointStatusConnectedProfile.setStatus("current")


class _AdGenMgcpEndpointStatusState_Type(Integer32):
    """Custom type adGenMgcpEndpointStatusState based on Integer32"""
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
        *(("connected", 1),
          ("disconnected", 2),
          ("reconnecting", 3),
          ("connectedNoRqnt", 4))
    )


_AdGenMgcpEndpointStatusState_Type.__name__ = "Integer32"
_AdGenMgcpEndpointStatusState_Object = MibTableColumn
adGenMgcpEndpointStatusState = _AdGenMgcpEndpointStatusState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 2, 1, 1, 1, 5),
    _AdGenMgcpEndpointStatusState_Type()
)
adGenMgcpEndpointStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMgcpEndpointStatusState.setStatus("current")
_AdGenMgcpEndpointStatusStateDetail_Type = DisplayString
_AdGenMgcpEndpointStatusStateDetail_Object = MibTableColumn
adGenMgcpEndpointStatusStateDetail = _AdGenMgcpEndpointStatusStateDetail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 2, 1, 1, 1, 6),
    _AdGenMgcpEndpointStatusStateDetail_Type()
)
adGenMgcpEndpointStatusStateDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMgcpEndpointStatusStateDetail.setStatus("current")


class _AdGenMgcpEndpointOperStatus_Type(Integer32):
    """Custom type adGenMgcpEndpointOperStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("unknown", 4))
    )


_AdGenMgcpEndpointOperStatus_Type.__name__ = "Integer32"
_AdGenMgcpEndpointOperStatus_Object = MibTableColumn
adGenMgcpEndpointOperStatus = _AdGenMgcpEndpointOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 2, 1, 1, 1, 7),
    _AdGenMgcpEndpointOperStatus_Type()
)
adGenMgcpEndpointOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMgcpEndpointOperStatus.setStatus("current")
_AdGenMgcpEndpointStatusCodecInUse_Type = AdGenVoipCodecProfileType
_AdGenMgcpEndpointStatusCodecInUse_Object = MibTableColumn
adGenMgcpEndpointStatusCodecInUse = _AdGenMgcpEndpointStatusCodecInUse_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 2, 1, 1, 1, 8),
    _AdGenMgcpEndpointStatusCodecInUse_Type()
)
adGenMgcpEndpointStatusCodecInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMgcpEndpointStatusCodecInUse.setStatus("current")
_AdGenMgcpEndpointLastError_Type = DisplayString
_AdGenMgcpEndpointLastError_Object = MibTableColumn
adGenMgcpEndpointLastError = _AdGenMgcpEndpointLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 2, 1, 1, 1, 9),
    _AdGenMgcpEndpointLastError_Type()
)
adGenMgcpEndpointLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMgcpEndpointLastError.setStatus("current")
_AdGenMgcpActions_ObjectIdentity = ObjectIdentity
adGenMgcpActions = _AdGenMgcpActions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 3)
)
_AdGenMgcpActionsTable_Object = MibTable
adGenMgcpActionsTable = _AdGenMgcpActionsTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 3, 1)
)
if mibBuilder.loadTexts:
    adGenMgcpActionsTable.setStatus("current")
_AdGenMgcpActionsEntry_Object = MibTableRow
adGenMgcpActionsEntry = _AdGenMgcpActionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 3, 1, 1)
)
adGenMgcpActionsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenMgcpActionsEntry.setStatus("current")
_AdGenMgcpActionsLastError_Type = DisplayString
_AdGenMgcpActionsLastError_Object = MibTableColumn
adGenMgcpActionsLastError = _AdGenMgcpActionsLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 3, 1, 1, 1),
    _AdGenMgcpActionsLastError_Type()
)
adGenMgcpActionsLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMgcpActionsLastError.setStatus("current")


class _AdGenMgcpActionsRestart_Type(Integer32):
    """Custom type adGenMgcpActionsRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restart", 1)
    )


_AdGenMgcpActionsRestart_Type.__name__ = "Integer32"
_AdGenMgcpActionsRestart_Object = MibTableColumn
adGenMgcpActionsRestart = _AdGenMgcpActionsRestart_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 54, 3, 1, 1, 2),
    _AdGenMgcpActionsRestart_Type()
)
adGenMgcpActionsRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMgcpActionsRestart.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENMGCP-MIB",
    **{"AdGenMgcpProfileName": AdGenMgcpProfileName,
       "adGenMgcpProvisioning": adGenMgcpProvisioning,
       "adGenMgcpProfileProv": adGenMgcpProfileProv,
       "adGenMgcpProfileProvCurrentNumber": adGenMgcpProfileProvCurrentNumber,
       "adGenMgcpProfileProvLastCreateError": adGenMgcpProfileProvLastCreateError,
       "adGenMgcpProfileProvTable": adGenMgcpProfileProvTable,
       "adGenMgcpProfileProvEntry": adGenMgcpProfileProvEntry,
       "adGenMgcpProfileEntryIndex": adGenMgcpProfileEntryIndex,
       "adGenMgcpProfileRowStatus": adGenMgcpProfileRowStatus,
       "adGenMgcpProfileLastErrorString": adGenMgcpProfileLastErrorString,
       "adGenMgcpProfileCallAgentPrimary": adGenMgcpProfileCallAgentPrimary,
       "adGenMgcpProfileCallAgentPrimaryUdp": adGenMgcpProfileCallAgentPrimaryUdp,
       "adGenMgcpProfileCallAgentSecondary": adGenMgcpProfileCallAgentSecondary,
       "adGenMgcpProfileCallAgentSecondaryUdp": adGenMgcpProfileCallAgentSecondaryUdp,
       "adGenMgcpProfileShutdown": adGenMgcpProfileShutdown,
       "adGenMgcpProfileBracketedIp": adGenMgcpProfileBracketedIp,
       "adGenMgcpProfileStandard": adGenMgcpProfileStandard,
       "adGenMgcpProfileMgcpDscp": adGenMgcpProfileMgcpDscp,
       "adGenMgcpProfileRtpDscp": adGenMgcpProfileRtpDscp,
       "adGenMgcpProfileGatewayUdp": adGenMgcpProfileGatewayUdp,
       "adGenMgcpProfileRtpUdpOffset": adGenMgcpProfileRtpUdpOffset,
       "adGenMgcpProfilePersistentNotifyHangDown": adGenMgcpProfilePersistentNotifyHangDown,
       "adGenMgcpProfilePersistentNotifyHangUp": adGenMgcpProfilePersistentNotifyHangUp,
       "adGenMgcpProfilePersistentNotifyHookFlash": adGenMgcpProfilePersistentNotifyHookFlash,
       "adGenMgcpProfileRetransmitDelay": adGenMgcpProfileRetransmitDelay,
       "adGenMgcpProfileMax1": adGenMgcpProfileMax1,
       "adGenMgcpProfileMax2": adGenMgcpProfileMax2,
       "adGenMgcpProfileLocalDomainType": adGenMgcpProfileLocalDomainType,
       "adGenMgcpProfileLocalDomainAddress": adGenMgcpProfileLocalDomainAddress,
       "adGenMgcpProfileTerminationIdBase": adGenMgcpProfileTerminationIdBase,
       "adGenMgcpProfileRFC2833Signaling": adGenMgcpProfileRFC2833Signaling,
       "adGenMgcpEndpointProv": adGenMgcpEndpointProv,
       "adGenMgcpEndpointProvCurrentNumber": adGenMgcpEndpointProvCurrentNumber,
       "adGenMgcpEndpointProvLastCreateError": adGenMgcpEndpointProvLastCreateError,
       "adGenMgcpEndpointProvTable": adGenMgcpEndpointProvTable,
       "adGenMgcpEndpointProvEntry": adGenMgcpEndpointProvEntry,
       "adGenMgcpEndpointEntryIndex": adGenMgcpEndpointEntryIndex,
       "adGenMgcpEndpointRowStatus": adGenMgcpEndpointRowStatus,
       "adGenMgcpEndpointLastErrorString": adGenMgcpEndpointLastErrorString,
       "adGenMgcpEndpointFxsPort": adGenMgcpEndpointFxsPort,
       "adGenMgcpEndpointMgcpProfile": adGenMgcpEndpointMgcpProfile,
       "adGenMgcpEndpointBlockCallerId": adGenMgcpEndpointBlockCallerId,
       "adGenMgcpEndpointDescription": adGenMgcpEndpointDescription,
       "adGenMgcpEndpointDisplayString": adGenMgcpEndpointDisplayString,
       "adGenMgcpEndpointFwdDisconnect": adGenMgcpEndpointFwdDisconnect,
       "adGenMgcpEndpointMediaProfile": adGenMgcpEndpointMediaProfile,
       "adGenMgcpEndpointCodecListProfile": adGenMgcpEndpointCodecListProfile,
       "adGenMgcpStatus": adGenMgcpStatus,
       "adGenMgcpEndpointStatus": adGenMgcpEndpointStatus,
       "adGenMgcpEndpointStatusTable": adGenMgcpEndpointStatusTable,
       "adGenMgcpEndpointStatusEntry": adGenMgcpEndpointStatusEntry,
       "adGenMgcpEndpointStatusEntryIndex": adGenMgcpEndpointStatusEntryIndex,
       "adGenMgcpEndpointStatusFXSPort": adGenMgcpEndpointStatusFXSPort,
       "adGenMgcpEndpointStatusName": adGenMgcpEndpointStatusName,
       "adGenMgcpEndpointStatusConnectedProfile": adGenMgcpEndpointStatusConnectedProfile,
       "adGenMgcpEndpointStatusState": adGenMgcpEndpointStatusState,
       "adGenMgcpEndpointStatusStateDetail": adGenMgcpEndpointStatusStateDetail,
       "adGenMgcpEndpointOperStatus": adGenMgcpEndpointOperStatus,
       "adGenMgcpEndpointStatusCodecInUse": adGenMgcpEndpointStatusCodecInUse,
       "adGenMgcpEndpointLastError": adGenMgcpEndpointLastError,
       "adGenMgcpActions": adGenMgcpActions,
       "adGenMgcpActionsTable": adGenMgcpActionsTable,
       "adGenMgcpActionsEntry": adGenMgcpActionsEntry,
       "adGenMgcpActionsLastError": adGenMgcpActionsLastError,
       "adGenMgcpActionsRestart": adGenMgcpActionsRestart,
       "adGenMgcpEntity": adGenMgcpEntity}
)
