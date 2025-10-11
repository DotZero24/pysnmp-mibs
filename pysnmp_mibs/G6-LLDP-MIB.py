# SNMP MIB module (G6-LLDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/microsens/G6-LLDP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:06 2025
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

(g6,) = mibBuilder.importSymbols(
    "MICROSENS-G6-MIB",
    "g6")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

protocol = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2)
)
if mibBuilder.loadTexts:
    protocol.setRevisions(
        ("2018-02-12 16:19",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Lldp_ObjectIdentity = ObjectIdentity
lldp = _Lldp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43)
)
_ConfigTable_Object = MibTable
configTable = _ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 1)
)
if mibBuilder.loadTexts:
    configTable.setStatus("current")
_ConfigEntry_Object = MibTableRow
configEntry = _ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 1, 1)
)
configEntry.setIndexNames(
    (0, "G6-LLDP-MIB", "configIndex"),
)
if mibBuilder.loadTexts:
    configEntry.setStatus("current")


class _ConfigIndex_Type(Integer32):
    """Custom type configIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_ConfigIndex_Type.__name__ = "Integer32"
_ConfigIndex_Object = MibTableColumn
configIndex = _ConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 1, 1, 1),
    _ConfigIndex_Type()
)
configIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    configIndex.setStatus("current")


class _ConfigEnableLldp_Type(Integer32):
    """Custom type configEnableLldp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ConfigEnableLldp_Type.__name__ = "Integer32"
_ConfigEnableLldp_Object = MibTableColumn
configEnableLldp = _ConfigEnableLldp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 1, 1, 2),
    _ConfigEnableLldp_Type()
)
configEnableLldp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEnableLldp.setStatus("current")


class _ConfigEnableCdp_Type(Integer32):
    """Custom type configEnableCdp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ConfigEnableCdp_Type.__name__ = "Integer32"
_ConfigEnableCdp_Object = MibTableColumn
configEnableCdp = _ConfigEnableCdp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 1, 1, 3),
    _ConfigEnableCdp_Type()
)
configEnableCdp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEnableCdp.setStatus("current")
_ConfigLldpEnabledPorts_Type = Integer32
_ConfigLldpEnabledPorts_Object = MibTableColumn
configLldpEnabledPorts = _ConfigLldpEnabledPorts_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 1, 1, 4),
    _ConfigLldpEnabledPorts_Type()
)
configLldpEnabledPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configLldpEnabledPorts.setStatus("current")


class _ConfigReceiveOnly_Type(Integer32):
    """Custom type configReceiveOnly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ConfigReceiveOnly_Type.__name__ = "Integer32"
_ConfigReceiveOnly_Object = MibTableColumn
configReceiveOnly = _ConfigReceiveOnly_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 1, 1, 5),
    _ConfigReceiveOnly_Type()
)
configReceiveOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configReceiveOnly.setStatus("current")


class _ConfigForwardToLink_Type(Integer32):
    """Custom type configForwardToLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ConfigForwardToLink_Type.__name__ = "Integer32"
_ConfigForwardToLink_Object = MibTableColumn
configForwardToLink = _ConfigForwardToLink_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 1, 1, 6),
    _ConfigForwardToLink_Type()
)
configForwardToLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configForwardToLink.setStatus("current")


class _ConfigAdvertizedMedClass_Type(Integer32):
    """Custom type configAdvertizedMedClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disableMed", 0),
          ("genericEndpoint", 1),
          ("mediaEndpoint", 2),
          ("communicationEndpoint", 3),
          ("networkDevice", 4))
    )


_ConfigAdvertizedMedClass_Type.__name__ = "Integer32"
_ConfigAdvertizedMedClass_Object = MibTableColumn
configAdvertizedMedClass = _ConfigAdvertizedMedClass_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 1, 1, 7),
    _ConfigAdvertizedMedClass_Type()
)
configAdvertizedMedClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configAdvertizedMedClass.setStatus("current")


class _ConfigDisableMedInventory_Type(Integer32):
    """Custom type configDisableMedInventory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ConfigDisableMedInventory_Type.__name__ = "Integer32"
_ConfigDisableMedInventory_Object = MibTableColumn
configDisableMedInventory = _ConfigDisableMedInventory_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 1, 1, 8),
    _ConfigDisableMedInventory_Type()
)
configDisableMedInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configDisableMedInventory.setStatus("current")


class _ConfigDisableVoiceVlanTlv_Type(Integer32):
    """Custom type configDisableVoiceVlanTlv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ConfigDisableVoiceVlanTlv_Type.__name__ = "Integer32"
_ConfigDisableVoiceVlanTlv_Object = MibTableColumn
configDisableVoiceVlanTlv = _ConfigDisableVoiceVlanTlv_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 1, 1, 9),
    _ConfigDisableVoiceVlanTlv_Type()
)
configDisableVoiceVlanTlv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configDisableVoiceVlanTlv.setStatus("current")


class _ConfigCdpVersion_Type(Integer32):
    """Custom type configCdpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1AndV2", 0),
          ("v1", 1),
          ("v2", 2))
    )


_ConfigCdpVersion_Type.__name__ = "Integer32"
_ConfigCdpVersion_Object = MibTableColumn
configCdpVersion = _ConfigCdpVersion_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 1, 1, 10),
    _ConfigCdpVersion_Type()
)
configCdpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCdpVersion.setStatus("current")


class _ConfigVoiceVlanPrio_Type(Integer32):
    """Custom type configVoiceVlanPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ConfigVoiceVlanPrio_Type.__name__ = "Integer32"
_ConfigVoiceVlanPrio_Object = MibTableColumn
configVoiceVlanPrio = _ConfigVoiceVlanPrio_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 1, 1, 11),
    _ConfigVoiceVlanPrio_Type()
)
configVoiceVlanPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configVoiceVlanPrio.setStatus("current")


class _ConfigVoiceVlanSignalPrio_Type(Integer32):
    """Custom type configVoiceVlanSignalPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ConfigVoiceVlanSignalPrio_Type.__name__ = "Integer32"
_ConfigVoiceVlanSignalPrio_Object = MibTableColumn
configVoiceVlanSignalPrio = _ConfigVoiceVlanSignalPrio_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 1, 1, 12),
    _ConfigVoiceVlanSignalPrio_Type()
)
configVoiceVlanSignalPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configVoiceVlanSignalPrio.setStatus("current")


class _ConfigVoiceDscp_Type(Integer32):
    """Custom type configVoiceDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ConfigVoiceDscp_Type.__name__ = "Integer32"
_ConfigVoiceDscp_Object = MibTableColumn
configVoiceDscp = _ConfigVoiceDscp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 1, 1, 13),
    _ConfigVoiceDscp_Type()
)
configVoiceDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configVoiceDscp.setStatus("current")


class _ConfigSignalingDscp_Type(Integer32):
    """Custom type configSignalingDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ConfigSignalingDscp_Type.__name__ = "Integer32"
_ConfigSignalingDscp_Object = MibTableColumn
configSignalingDscp = _ConfigSignalingDscp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 1, 1, 14),
    _ConfigSignalingDscp_Type()
)
configSignalingDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSignalingDscp.setStatus("current")


class _ConfigTimeToLive_Type(Integer32):
    """Custom type configTimeToLive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ConfigTimeToLive_Type.__name__ = "Integer32"
_ConfigTimeToLive_Object = MibTableColumn
configTimeToLive = _ConfigTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 1, 1, 15),
    _ConfigTimeToLive_Type()
)
configTimeToLive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configTimeToLive.setStatus("current")


class _ConfigTxDelay_Type(Integer32):
    """Custom type configTxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ConfigTxDelay_Type.__name__ = "Integer32"
_ConfigTxDelay_Object = MibTableColumn
configTxDelay = _ConfigTxDelay_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 1, 1, 16),
    _ConfigTxDelay_Type()
)
configTxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configTxDelay.setStatus("current")


class _ConfigMsgTxInterval_Type(Integer32):
    """Custom type configMsgTxInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ConfigMsgTxInterval_Type.__name__ = "Integer32"
_ConfigMsgTxInterval_Object = MibTableColumn
configMsgTxInterval = _ConfigMsgTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 1, 1, 17),
    _ConfigMsgTxInterval_Type()
)
configMsgTxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configMsgTxInterval.setStatus("current")


class _ConfigForceLldpTransmission_Type(Integer32):
    """Custom type configForceLldpTransmission based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ConfigForceLldpTransmission_Type.__name__ = "Integer32"
_ConfigForceLldpTransmission_Object = MibTableColumn
configForceLldpTransmission = _ConfigForceLldpTransmission_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 1, 1, 18),
    _ConfigForceLldpTransmission_Type()
)
configForceLldpTransmission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configForceLldpTransmission.setStatus("current")


class _ConfigLldpResponsePreferred_Type(Integer32):
    """Custom type configLldpResponsePreferred based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ConfigLldpResponsePreferred_Type.__name__ = "Integer32"
_ConfigLldpResponsePreferred_Object = MibTableColumn
configLldpResponsePreferred = _ConfigLldpResponsePreferred_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 1, 1, 19),
    _ConfigLldpResponsePreferred_Type()
)
configLldpResponsePreferred.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configLldpResponsePreferred.setStatus("current")
_LocalCoordinatesTable_Object = MibTable
localCoordinatesTable = _LocalCoordinatesTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 2)
)
if mibBuilder.loadTexts:
    localCoordinatesTable.setStatus("current")
_LocalCoordinatesEntry_Object = MibTableRow
localCoordinatesEntry = _LocalCoordinatesEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 2, 1)
)
localCoordinatesEntry.setIndexNames(
    (0, "G6-LLDP-MIB", "localCoordinatesIndex"),
)
if mibBuilder.loadTexts:
    localCoordinatesEntry.setStatus("current")


class _LocalCoordinatesIndex_Type(Integer32):
    """Custom type localCoordinatesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_LocalCoordinatesIndex_Type.__name__ = "Integer32"
_LocalCoordinatesIndex_Object = MibTableColumn
localCoordinatesIndex = _LocalCoordinatesIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 2, 1, 1),
    _LocalCoordinatesIndex_Type()
)
localCoordinatesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    localCoordinatesIndex.setStatus("current")
_LocalCoordinatesLatitude_Type = DisplayString
_LocalCoordinatesLatitude_Object = MibTableColumn
localCoordinatesLatitude = _LocalCoordinatesLatitude_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 2, 1, 2),
    _LocalCoordinatesLatitude_Type()
)
localCoordinatesLatitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localCoordinatesLatitude.setStatus("current")


class _LocalCoordinatesLatResolution_Type(Integer32):
    """Custom type localCoordinatesLatResolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LocalCoordinatesLatResolution_Type.__name__ = "Integer32"
_LocalCoordinatesLatResolution_Object = MibTableColumn
localCoordinatesLatResolution = _LocalCoordinatesLatResolution_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 2, 1, 3),
    _LocalCoordinatesLatResolution_Type()
)
localCoordinatesLatResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localCoordinatesLatResolution.setStatus("current")
_LocalCoordinatesLongitude_Type = DisplayString
_LocalCoordinatesLongitude_Object = MibTableColumn
localCoordinatesLongitude = _LocalCoordinatesLongitude_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 2, 1, 4),
    _LocalCoordinatesLongitude_Type()
)
localCoordinatesLongitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localCoordinatesLongitude.setStatus("current")


class _LocalCoordinatesLongResolution_Type(Integer32):
    """Custom type localCoordinatesLongResolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LocalCoordinatesLongResolution_Type.__name__ = "Integer32"
_LocalCoordinatesLongResolution_Object = MibTableColumn
localCoordinatesLongResolution = _LocalCoordinatesLongResolution_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 2, 1, 5),
    _LocalCoordinatesLongResolution_Type()
)
localCoordinatesLongResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localCoordinatesLongResolution.setStatus("current")
_LocalCoordinatesAltitude_Type = DisplayString
_LocalCoordinatesAltitude_Object = MibTableColumn
localCoordinatesAltitude = _LocalCoordinatesAltitude_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 2, 1, 6),
    _LocalCoordinatesAltitude_Type()
)
localCoordinatesAltitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localCoordinatesAltitude.setStatus("current")


class _LocalCoordinatesAltResolution_Type(Integer32):
    """Custom type localCoordinatesAltResolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LocalCoordinatesAltResolution_Type.__name__ = "Integer32"
_LocalCoordinatesAltResolution_Object = MibTableColumn
localCoordinatesAltResolution = _LocalCoordinatesAltResolution_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 2, 1, 7),
    _LocalCoordinatesAltResolution_Type()
)
localCoordinatesAltResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localCoordinatesAltResolution.setStatus("current")


class _LocalCoordinatesAltType_Type(Integer32):
    """Custom type localCoordinatesAltType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("meter", 0),
          ("floor", 1))
    )


_LocalCoordinatesAltType_Type.__name__ = "Integer32"
_LocalCoordinatesAltType_Object = MibTableColumn
localCoordinatesAltType = _LocalCoordinatesAltType_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 2, 1, 8),
    _LocalCoordinatesAltType_Type()
)
localCoordinatesAltType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localCoordinatesAltType.setStatus("current")
_LocalCoordinatesDatum_Type = DisplayString
_LocalCoordinatesDatum_Object = MibTableColumn
localCoordinatesDatum = _LocalCoordinatesDatum_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 2, 1, 9),
    _LocalCoordinatesDatum_Type()
)
localCoordinatesDatum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localCoordinatesDatum.setStatus("current")
_LocalCivicLocationTable_Object = MibTable
localCivicLocationTable = _LocalCivicLocationTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 3)
)
if mibBuilder.loadTexts:
    localCivicLocationTable.setStatus("current")
_LocalCivicLocationEntry_Object = MibTableRow
localCivicLocationEntry = _LocalCivicLocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 3, 1)
)
localCivicLocationEntry.setIndexNames(
    (0, "G6-LLDP-MIB", "localCivicLocationIndex"),
)
if mibBuilder.loadTexts:
    localCivicLocationEntry.setStatus("current")


class _LocalCivicLocationIndex_Type(Integer32):
    """Custom type localCivicLocationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_LocalCivicLocationIndex_Type.__name__ = "Integer32"
_LocalCivicLocationIndex_Object = MibTableColumn
localCivicLocationIndex = _LocalCivicLocationIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 3, 1, 1),
    _LocalCivicLocationIndex_Type()
)
localCivicLocationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    localCivicLocationIndex.setStatus("current")
_LocalCivicLocationCountryCode_Type = DisplayString
_LocalCivicLocationCountryCode_Object = MibTableColumn
localCivicLocationCountryCode = _LocalCivicLocationCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 3, 1, 2),
    _LocalCivicLocationCountryCode_Type()
)
localCivicLocationCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localCivicLocationCountryCode.setStatus("current")
_LocalCivicLocationLanguage_Type = DisplayString
_LocalCivicLocationLanguage_Object = MibTableColumn
localCivicLocationLanguage = _LocalCivicLocationLanguage_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 3, 1, 3),
    _LocalCivicLocationLanguage_Type()
)
localCivicLocationLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localCivicLocationLanguage.setStatus("current")
_LocalCivicLocationNationalSubdivision_Type = DisplayString
_LocalCivicLocationNationalSubdivision_Object = MibTableColumn
localCivicLocationNationalSubdivision = _LocalCivicLocationNationalSubdivision_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 3, 1, 4),
    _LocalCivicLocationNationalSubdivision_Type()
)
localCivicLocationNationalSubdivision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localCivicLocationNationalSubdivision.setStatus("current")
_LocalCivicLocationCounty_Type = DisplayString
_LocalCivicLocationCounty_Object = MibTableColumn
localCivicLocationCounty = _LocalCivicLocationCounty_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 3, 1, 5),
    _LocalCivicLocationCounty_Type()
)
localCivicLocationCounty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localCivicLocationCounty.setStatus("current")
_LocalCivicLocationTown_Type = DisplayString
_LocalCivicLocationTown_Object = MibTableColumn
localCivicLocationTown = _LocalCivicLocationTown_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 3, 1, 6),
    _LocalCivicLocationTown_Type()
)
localCivicLocationTown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localCivicLocationTown.setStatus("current")
_LocalCivicLocationDistrict_Type = DisplayString
_LocalCivicLocationDistrict_Object = MibTableColumn
localCivicLocationDistrict = _LocalCivicLocationDistrict_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 3, 1, 7),
    _LocalCivicLocationDistrict_Type()
)
localCivicLocationDistrict.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localCivicLocationDistrict.setStatus("current")
_LocalCivicLocationBlock_Type = DisplayString
_LocalCivicLocationBlock_Object = MibTableColumn
localCivicLocationBlock = _LocalCivicLocationBlock_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 3, 1, 8),
    _LocalCivicLocationBlock_Type()
)
localCivicLocationBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localCivicLocationBlock.setStatus("current")
_LocalCivicLocationStreet_Type = DisplayString
_LocalCivicLocationStreet_Object = MibTableColumn
localCivicLocationStreet = _LocalCivicLocationStreet_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 3, 1, 9),
    _LocalCivicLocationStreet_Type()
)
localCivicLocationStreet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localCivicLocationStreet.setStatus("current")
_LocalCivicLocationLeadingStreetDirection_Type = DisplayString
_LocalCivicLocationLeadingStreetDirection_Object = MibTableColumn
localCivicLocationLeadingStreetDirection = _LocalCivicLocationLeadingStreetDirection_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 3, 1, 10),
    _LocalCivicLocationLeadingStreetDirection_Type()
)
localCivicLocationLeadingStreetDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localCivicLocationLeadingStreetDirection.setStatus("current")
_LocalCivicLocationTrailingStreetSuffix_Type = DisplayString
_LocalCivicLocationTrailingStreetSuffix_Object = MibTableColumn
localCivicLocationTrailingStreetSuffix = _LocalCivicLocationTrailingStreetSuffix_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 3, 1, 11),
    _LocalCivicLocationTrailingStreetSuffix_Type()
)
localCivicLocationTrailingStreetSuffix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localCivicLocationTrailingStreetSuffix.setStatus("current")
_LocalCivicLocationStreetSuffix_Type = DisplayString
_LocalCivicLocationStreetSuffix_Object = MibTableColumn
localCivicLocationStreetSuffix = _LocalCivicLocationStreetSuffix_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 3, 1, 12),
    _LocalCivicLocationStreetSuffix_Type()
)
localCivicLocationStreetSuffix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localCivicLocationStreetSuffix.setStatus("current")
_LocalCivicLocationHouseNumber_Type = DisplayString
_LocalCivicLocationHouseNumber_Object = MibTableColumn
localCivicLocationHouseNumber = _LocalCivicLocationHouseNumber_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 3, 1, 13),
    _LocalCivicLocationHouseNumber_Type()
)
localCivicLocationHouseNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localCivicLocationHouseNumber.setStatus("current")
_LocalCivicLocationHouseNumberSuffix_Type = DisplayString
_LocalCivicLocationHouseNumberSuffix_Object = MibTableColumn
localCivicLocationHouseNumberSuffix = _LocalCivicLocationHouseNumberSuffix_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 3, 1, 14),
    _LocalCivicLocationHouseNumberSuffix_Type()
)
localCivicLocationHouseNumberSuffix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localCivicLocationHouseNumberSuffix.setStatus("current")
_LocalCivicLocationLandmark_Type = DisplayString
_LocalCivicLocationLandmark_Object = MibTableColumn
localCivicLocationLandmark = _LocalCivicLocationLandmark_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 3, 1, 15),
    _LocalCivicLocationLandmark_Type()
)
localCivicLocationLandmark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localCivicLocationLandmark.setStatus("current")
_LocalCivicLocationAdditionalInfo_Type = DisplayString
_LocalCivicLocationAdditionalInfo_Object = MibTableColumn
localCivicLocationAdditionalInfo = _LocalCivicLocationAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 3, 1, 16),
    _LocalCivicLocationAdditionalInfo_Type()
)
localCivicLocationAdditionalInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localCivicLocationAdditionalInfo.setStatus("current")
_LocalCivicLocationName_Type = DisplayString
_LocalCivicLocationName_Object = MibTableColumn
localCivicLocationName = _LocalCivicLocationName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 3, 1, 17),
    _LocalCivicLocationName_Type()
)
localCivicLocationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localCivicLocationName.setStatus("current")
_LocalCivicLocationZipCode_Type = DisplayString
_LocalCivicLocationZipCode_Object = MibTableColumn
localCivicLocationZipCode = _LocalCivicLocationZipCode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 3, 1, 18),
    _LocalCivicLocationZipCode_Type()
)
localCivicLocationZipCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localCivicLocationZipCode.setStatus("current")
_LocalCivicLocationBuilding_Type = DisplayString
_LocalCivicLocationBuilding_Object = MibTableColumn
localCivicLocationBuilding = _LocalCivicLocationBuilding_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 3, 1, 19),
    _LocalCivicLocationBuilding_Type()
)
localCivicLocationBuilding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localCivicLocationBuilding.setStatus("current")
_LocalCivicLocationUnit_Type = DisplayString
_LocalCivicLocationUnit_Object = MibTableColumn
localCivicLocationUnit = _LocalCivicLocationUnit_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 3, 1, 20),
    _LocalCivicLocationUnit_Type()
)
localCivicLocationUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localCivicLocationUnit.setStatus("current")
_LocalCivicLocationFloor_Type = DisplayString
_LocalCivicLocationFloor_Object = MibTableColumn
localCivicLocationFloor = _LocalCivicLocationFloor_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 3, 1, 21),
    _LocalCivicLocationFloor_Type()
)
localCivicLocationFloor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localCivicLocationFloor.setStatus("current")
_LocalCivicLocationRoom_Type = DisplayString
_LocalCivicLocationRoom_Object = MibTableColumn
localCivicLocationRoom = _LocalCivicLocationRoom_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 3, 1, 22),
    _LocalCivicLocationRoom_Type()
)
localCivicLocationRoom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localCivicLocationRoom.setStatus("current")
_LocalCivicLocationPlaceType_Type = DisplayString
_LocalCivicLocationPlaceType_Object = MibTableColumn
localCivicLocationPlaceType = _LocalCivicLocationPlaceType_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 3, 1, 23),
    _LocalCivicLocationPlaceType_Type()
)
localCivicLocationPlaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localCivicLocationPlaceType.setStatus("current")
_LocalCivicLocationScript_Type = DisplayString
_LocalCivicLocationScript_Object = MibTableColumn
localCivicLocationScript = _LocalCivicLocationScript_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 3, 1, 24),
    _LocalCivicLocationScript_Type()
)
localCivicLocationScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localCivicLocationScript.setStatus("current")
_LocalCivicLocationElinNumber_Type = DisplayString
_LocalCivicLocationElinNumber_Object = MibTableColumn
localCivicLocationElinNumber = _LocalCivicLocationElinNumber_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 3, 1, 25),
    _LocalCivicLocationElinNumber_Type()
)
localCivicLocationElinNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localCivicLocationElinNumber.setStatus("current")
_ReceivedOverviewTable_Object = MibTable
receivedOverviewTable = _ReceivedOverviewTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 100)
)
if mibBuilder.loadTexts:
    receivedOverviewTable.setStatus("current")
_ReceivedOverviewEntry_Object = MibTableRow
receivedOverviewEntry = _ReceivedOverviewEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 100, 1)
)
receivedOverviewEntry.setIndexNames(
    (0, "G6-LLDP-MIB", "receivedOverviewPortIndex"),
)
if mibBuilder.loadTexts:
    receivedOverviewEntry.setStatus("current")


class _ReceivedOverviewPortIndex_Type(Integer32):
    """Custom type receivedOverviewPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_ReceivedOverviewPortIndex_Type.__name__ = "Integer32"
_ReceivedOverviewPortIndex_Object = MibTableColumn
receivedOverviewPortIndex = _ReceivedOverviewPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 100, 1, 1),
    _ReceivedOverviewPortIndex_Type()
)
receivedOverviewPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    receivedOverviewPortIndex.setStatus("current")
_ReceivedOverviewSysName_Type = DisplayString
_ReceivedOverviewSysName_Object = MibTableColumn
receivedOverviewSysName = _ReceivedOverviewSysName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 100, 1, 2),
    _ReceivedOverviewSysName_Type()
)
receivedOverviewSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedOverviewSysName.setStatus("current")
_ReceivedOverviewSysDesc_Type = DisplayString
_ReceivedOverviewSysDesc_Object = MibTableColumn
receivedOverviewSysDesc = _ReceivedOverviewSysDesc_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 100, 1, 3),
    _ReceivedOverviewSysDesc_Type()
)
receivedOverviewSysDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedOverviewSysDesc.setStatus("current")


class _ReceivedOverviewChassisIdSubtype_Type(Integer32):
    """Custom type receivedOverviewChassisIdSubtype based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("chassisComponent", 1),
          ("interfaceAlias", 2),
          ("portComponent", 3),
          ("macAddress", 4),
          ("networkAddress", 5),
          ("interfaceName", 6),
          ("local", 7))
    )


_ReceivedOverviewChassisIdSubtype_Type.__name__ = "Integer32"
_ReceivedOverviewChassisIdSubtype_Object = MibTableColumn
receivedOverviewChassisIdSubtype = _ReceivedOverviewChassisIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 100, 1, 4),
    _ReceivedOverviewChassisIdSubtype_Type()
)
receivedOverviewChassisIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedOverviewChassisIdSubtype.setStatus("current")
_ReceivedOverviewChassisId_Type = DisplayString
_ReceivedOverviewChassisId_Object = MibTableColumn
receivedOverviewChassisId = _ReceivedOverviewChassisId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 100, 1, 5),
    _ReceivedOverviewChassisId_Type()
)
receivedOverviewChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedOverviewChassisId.setStatus("current")
_ReceivedOverviewMgmtIp_Type = DisplayString
_ReceivedOverviewMgmtIp_Object = MibTableColumn
receivedOverviewMgmtIp = _ReceivedOverviewMgmtIp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 100, 1, 6),
    _ReceivedOverviewMgmtIp_Type()
)
receivedOverviewMgmtIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedOverviewMgmtIp.setStatus("current")
_ReceivedOverviewMgmtOid_Type = DisplayString
_ReceivedOverviewMgmtOid_Object = MibTableColumn
receivedOverviewMgmtOid = _ReceivedOverviewMgmtOid_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 100, 1, 7),
    _ReceivedOverviewMgmtOid_Type()
)
receivedOverviewMgmtOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedOverviewMgmtOid.setStatus("current")


class _ReceivedOverviewCapabilities_Type(Bits):
    """Custom type receivedOverviewCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("other", 0),
          ("repeater", 1),
          ("bridge", 2),
          ("wlan", 3),
          ("router", 4),
          ("telephone", 5),
          ("docsis", 6),
          ("station", 7))
    )

_ReceivedOverviewCapabilities_Type.__name__ = "Bits"
_ReceivedOverviewCapabilities_Object = MibTableColumn
receivedOverviewCapabilities = _ReceivedOverviewCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 100, 1, 8),
    _ReceivedOverviewCapabilities_Type()
)
receivedOverviewCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedOverviewCapabilities.setStatus("current")


class _ReceivedOverviewCapabilitiesEnabled_Type(Bits):
    """Custom type receivedOverviewCapabilitiesEnabled based on Bits"""
    namedValues = NamedValues(
        *(("other", 0),
          ("repeater", 1),
          ("bridge", 2),
          ("wlan", 3),
          ("router", 4),
          ("telephone", 5),
          ("docsis", 6),
          ("station", 7))
    )

_ReceivedOverviewCapabilitiesEnabled_Type.__name__ = "Bits"
_ReceivedOverviewCapabilitiesEnabled_Object = MibTableColumn
receivedOverviewCapabilitiesEnabled = _ReceivedOverviewCapabilitiesEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 100, 1, 9),
    _ReceivedOverviewCapabilitiesEnabled_Type()
)
receivedOverviewCapabilitiesEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedOverviewCapabilitiesEnabled.setStatus("current")


class _ReceivedOverviewMedCapabilities_Type(Bits):
    """Custom type receivedOverviewMedCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("capability", 0),
          ("policy", 1),
          ("location", 2),
          ("mdiPse", 3),
          ("mdiPd", 4),
          ("inventory", 5))
    )

_ReceivedOverviewMedCapabilities_Type.__name__ = "Bits"
_ReceivedOverviewMedCapabilities_Object = MibTableColumn
receivedOverviewMedCapabilities = _ReceivedOverviewMedCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 100, 1, 10),
    _ReceivedOverviewMedCapabilities_Type()
)
receivedOverviewMedCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedOverviewMedCapabilities.setStatus("current")


class _ReceivedOverviewPortIdSubtype_Type(Integer32):
    """Custom type receivedOverviewPortIdSubtype based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("interfaceAlias", 1),
          ("portComponent", 2),
          ("macAddress", 3),
          ("networkAddress", 4),
          ("interfaceName", 5),
          ("agentCircuitId", 6),
          ("local", 7))
    )


_ReceivedOverviewPortIdSubtype_Type.__name__ = "Integer32"
_ReceivedOverviewPortIdSubtype_Object = MibTableColumn
receivedOverviewPortIdSubtype = _ReceivedOverviewPortIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 100, 1, 11),
    _ReceivedOverviewPortIdSubtype_Type()
)
receivedOverviewPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedOverviewPortIdSubtype.setStatus("current")
_ReceivedOverviewPortIdentification_Type = DisplayString
_ReceivedOverviewPortIdentification_Object = MibTableColumn
receivedOverviewPortIdentification = _ReceivedOverviewPortIdentification_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 100, 1, 12),
    _ReceivedOverviewPortIdentification_Type()
)
receivedOverviewPortIdentification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedOverviewPortIdentification.setStatus("current")
_ReceivedOverviewPortDescription_Type = DisplayString
_ReceivedOverviewPortDescription_Object = MibTableColumn
receivedOverviewPortDescription = _ReceivedOverviewPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 100, 1, 13),
    _ReceivedOverviewPortDescription_Type()
)
receivedOverviewPortDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedOverviewPortDescription.setStatus("current")


class _ReceivedOverviewPortVlan_Type(Integer32):
    """Custom type receivedOverviewPortVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ReceivedOverviewPortVlan_Type.__name__ = "Integer32"
_ReceivedOverviewPortVlan_Object = MibTableColumn
receivedOverviewPortVlan = _ReceivedOverviewPortVlan_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 100, 1, 14),
    _ReceivedOverviewPortVlan_Type()
)
receivedOverviewPortVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedOverviewPortVlan.setStatus("current")
_ReceivedCoordinatesTable_Object = MibTable
receivedCoordinatesTable = _ReceivedCoordinatesTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 101)
)
if mibBuilder.loadTexts:
    receivedCoordinatesTable.setStatus("current")
_ReceivedCoordinatesEntry_Object = MibTableRow
receivedCoordinatesEntry = _ReceivedCoordinatesEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 101, 1)
)
receivedCoordinatesEntry.setIndexNames(
    (0, "G6-LLDP-MIB", "receivedCoordinatesPortIndex"),
)
if mibBuilder.loadTexts:
    receivedCoordinatesEntry.setStatus("current")


class _ReceivedCoordinatesPortIndex_Type(Integer32):
    """Custom type receivedCoordinatesPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_ReceivedCoordinatesPortIndex_Type.__name__ = "Integer32"
_ReceivedCoordinatesPortIndex_Object = MibTableColumn
receivedCoordinatesPortIndex = _ReceivedCoordinatesPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 101, 1, 1),
    _ReceivedCoordinatesPortIndex_Type()
)
receivedCoordinatesPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    receivedCoordinatesPortIndex.setStatus("current")
_ReceivedCoordinatesLatitude_Type = DisplayString
_ReceivedCoordinatesLatitude_Object = MibTableColumn
receivedCoordinatesLatitude = _ReceivedCoordinatesLatitude_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 101, 1, 2),
    _ReceivedCoordinatesLatitude_Type()
)
receivedCoordinatesLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedCoordinatesLatitude.setStatus("current")


class _ReceivedCoordinatesLatResolution_Type(Integer32):
    """Custom type receivedCoordinatesLatResolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ReceivedCoordinatesLatResolution_Type.__name__ = "Integer32"
_ReceivedCoordinatesLatResolution_Object = MibTableColumn
receivedCoordinatesLatResolution = _ReceivedCoordinatesLatResolution_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 101, 1, 3),
    _ReceivedCoordinatesLatResolution_Type()
)
receivedCoordinatesLatResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedCoordinatesLatResolution.setStatus("current")
_ReceivedCoordinatesLongitude_Type = DisplayString
_ReceivedCoordinatesLongitude_Object = MibTableColumn
receivedCoordinatesLongitude = _ReceivedCoordinatesLongitude_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 101, 1, 4),
    _ReceivedCoordinatesLongitude_Type()
)
receivedCoordinatesLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedCoordinatesLongitude.setStatus("current")


class _ReceivedCoordinatesLongResolution_Type(Integer32):
    """Custom type receivedCoordinatesLongResolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ReceivedCoordinatesLongResolution_Type.__name__ = "Integer32"
_ReceivedCoordinatesLongResolution_Object = MibTableColumn
receivedCoordinatesLongResolution = _ReceivedCoordinatesLongResolution_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 101, 1, 5),
    _ReceivedCoordinatesLongResolution_Type()
)
receivedCoordinatesLongResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedCoordinatesLongResolution.setStatus("current")
_ReceivedCoordinatesAltitude_Type = DisplayString
_ReceivedCoordinatesAltitude_Object = MibTableColumn
receivedCoordinatesAltitude = _ReceivedCoordinatesAltitude_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 101, 1, 6),
    _ReceivedCoordinatesAltitude_Type()
)
receivedCoordinatesAltitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedCoordinatesAltitude.setStatus("current")


class _ReceivedCoordinatesAltResolution_Type(Integer32):
    """Custom type receivedCoordinatesAltResolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ReceivedCoordinatesAltResolution_Type.__name__ = "Integer32"
_ReceivedCoordinatesAltResolution_Object = MibTableColumn
receivedCoordinatesAltResolution = _ReceivedCoordinatesAltResolution_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 101, 1, 7),
    _ReceivedCoordinatesAltResolution_Type()
)
receivedCoordinatesAltResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedCoordinatesAltResolution.setStatus("current")


class _ReceivedCoordinatesAltUnit_Type(Integer32):
    """Custom type receivedCoordinatesAltUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("meter", 0),
          ("floor", 1))
    )


_ReceivedCoordinatesAltUnit_Type.__name__ = "Integer32"
_ReceivedCoordinatesAltUnit_Object = MibTableColumn
receivedCoordinatesAltUnit = _ReceivedCoordinatesAltUnit_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 101, 1, 8),
    _ReceivedCoordinatesAltUnit_Type()
)
receivedCoordinatesAltUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedCoordinatesAltUnit.setStatus("current")
_ReceivedCoordinatesDatum_Type = DisplayString
_ReceivedCoordinatesDatum_Object = MibTableColumn
receivedCoordinatesDatum = _ReceivedCoordinatesDatum_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 101, 1, 9),
    _ReceivedCoordinatesDatum_Type()
)
receivedCoordinatesDatum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedCoordinatesDatum.setStatus("current")
_ReceivedCivicLocationsTable_Object = MibTable
receivedCivicLocationsTable = _ReceivedCivicLocationsTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 102)
)
if mibBuilder.loadTexts:
    receivedCivicLocationsTable.setStatus("current")
_ReceivedCivicLocationsEntry_Object = MibTableRow
receivedCivicLocationsEntry = _ReceivedCivicLocationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 102, 1)
)
receivedCivicLocationsEntry.setIndexNames(
    (0, "G6-LLDP-MIB", "receivedCivicLocationsPortIndex"),
)
if mibBuilder.loadTexts:
    receivedCivicLocationsEntry.setStatus("current")


class _ReceivedCivicLocationsPortIndex_Type(Integer32):
    """Custom type receivedCivicLocationsPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_ReceivedCivicLocationsPortIndex_Type.__name__ = "Integer32"
_ReceivedCivicLocationsPortIndex_Object = MibTableColumn
receivedCivicLocationsPortIndex = _ReceivedCivicLocationsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 102, 1, 1),
    _ReceivedCivicLocationsPortIndex_Type()
)
receivedCivicLocationsPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    receivedCivicLocationsPortIndex.setStatus("current")
_ReceivedCivicLocationsCountryCode_Type = DisplayString
_ReceivedCivicLocationsCountryCode_Object = MibTableColumn
receivedCivicLocationsCountryCode = _ReceivedCivicLocationsCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 102, 1, 2),
    _ReceivedCivicLocationsCountryCode_Type()
)
receivedCivicLocationsCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedCivicLocationsCountryCode.setStatus("current")
_ReceivedCivicLocationsLanguage_Type = DisplayString
_ReceivedCivicLocationsLanguage_Object = MibTableColumn
receivedCivicLocationsLanguage = _ReceivedCivicLocationsLanguage_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 102, 1, 3),
    _ReceivedCivicLocationsLanguage_Type()
)
receivedCivicLocationsLanguage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedCivicLocationsLanguage.setStatus("current")
_ReceivedCivicLocationsNationalSubdivision_Type = DisplayString
_ReceivedCivicLocationsNationalSubdivision_Object = MibTableColumn
receivedCivicLocationsNationalSubdivision = _ReceivedCivicLocationsNationalSubdivision_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 102, 1, 4),
    _ReceivedCivicLocationsNationalSubdivision_Type()
)
receivedCivicLocationsNationalSubdivision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedCivicLocationsNationalSubdivision.setStatus("current")
_ReceivedCivicLocationsCounty_Type = DisplayString
_ReceivedCivicLocationsCounty_Object = MibTableColumn
receivedCivicLocationsCounty = _ReceivedCivicLocationsCounty_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 102, 1, 5),
    _ReceivedCivicLocationsCounty_Type()
)
receivedCivicLocationsCounty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedCivicLocationsCounty.setStatus("current")
_ReceivedCivicLocationsTown_Type = DisplayString
_ReceivedCivicLocationsTown_Object = MibTableColumn
receivedCivicLocationsTown = _ReceivedCivicLocationsTown_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 102, 1, 6),
    _ReceivedCivicLocationsTown_Type()
)
receivedCivicLocationsTown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedCivicLocationsTown.setStatus("current")
_ReceivedCivicLocationsDistrict_Type = DisplayString
_ReceivedCivicLocationsDistrict_Object = MibTableColumn
receivedCivicLocationsDistrict = _ReceivedCivicLocationsDistrict_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 102, 1, 7),
    _ReceivedCivicLocationsDistrict_Type()
)
receivedCivicLocationsDistrict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedCivicLocationsDistrict.setStatus("current")
_ReceivedCivicLocationsBlock_Type = DisplayString
_ReceivedCivicLocationsBlock_Object = MibTableColumn
receivedCivicLocationsBlock = _ReceivedCivicLocationsBlock_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 102, 1, 8),
    _ReceivedCivicLocationsBlock_Type()
)
receivedCivicLocationsBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedCivicLocationsBlock.setStatus("current")
_ReceivedCivicLocationsStreet_Type = DisplayString
_ReceivedCivicLocationsStreet_Object = MibTableColumn
receivedCivicLocationsStreet = _ReceivedCivicLocationsStreet_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 102, 1, 9),
    _ReceivedCivicLocationsStreet_Type()
)
receivedCivicLocationsStreet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedCivicLocationsStreet.setStatus("current")
_ReceivedCivicLocationsLeadingStreetDirection_Type = DisplayString
_ReceivedCivicLocationsLeadingStreetDirection_Object = MibTableColumn
receivedCivicLocationsLeadingStreetDirection = _ReceivedCivicLocationsLeadingStreetDirection_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 102, 1, 10),
    _ReceivedCivicLocationsLeadingStreetDirection_Type()
)
receivedCivicLocationsLeadingStreetDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedCivicLocationsLeadingStreetDirection.setStatus("current")
_ReceivedCivicLocationsTrailingStreetSuffix_Type = DisplayString
_ReceivedCivicLocationsTrailingStreetSuffix_Object = MibTableColumn
receivedCivicLocationsTrailingStreetSuffix = _ReceivedCivicLocationsTrailingStreetSuffix_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 102, 1, 11),
    _ReceivedCivicLocationsTrailingStreetSuffix_Type()
)
receivedCivicLocationsTrailingStreetSuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedCivicLocationsTrailingStreetSuffix.setStatus("current")
_ReceivedCivicLocationsStreetSuffix_Type = DisplayString
_ReceivedCivicLocationsStreetSuffix_Object = MibTableColumn
receivedCivicLocationsStreetSuffix = _ReceivedCivicLocationsStreetSuffix_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 102, 1, 12),
    _ReceivedCivicLocationsStreetSuffix_Type()
)
receivedCivicLocationsStreetSuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedCivicLocationsStreetSuffix.setStatus("current")
_ReceivedCivicLocationsHouseNumber_Type = DisplayString
_ReceivedCivicLocationsHouseNumber_Object = MibTableColumn
receivedCivicLocationsHouseNumber = _ReceivedCivicLocationsHouseNumber_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 102, 1, 13),
    _ReceivedCivicLocationsHouseNumber_Type()
)
receivedCivicLocationsHouseNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedCivicLocationsHouseNumber.setStatus("current")
_ReceivedCivicLocationsHouseNumberSuffix_Type = DisplayString
_ReceivedCivicLocationsHouseNumberSuffix_Object = MibTableColumn
receivedCivicLocationsHouseNumberSuffix = _ReceivedCivicLocationsHouseNumberSuffix_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 102, 1, 14),
    _ReceivedCivicLocationsHouseNumberSuffix_Type()
)
receivedCivicLocationsHouseNumberSuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedCivicLocationsHouseNumberSuffix.setStatus("current")
_ReceivedCivicLocationsLandmark_Type = DisplayString
_ReceivedCivicLocationsLandmark_Object = MibTableColumn
receivedCivicLocationsLandmark = _ReceivedCivicLocationsLandmark_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 102, 1, 15),
    _ReceivedCivicLocationsLandmark_Type()
)
receivedCivicLocationsLandmark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedCivicLocationsLandmark.setStatus("current")
_ReceivedCivicLocationsAdditionalInfo_Type = DisplayString
_ReceivedCivicLocationsAdditionalInfo_Object = MibTableColumn
receivedCivicLocationsAdditionalInfo = _ReceivedCivicLocationsAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 102, 1, 16),
    _ReceivedCivicLocationsAdditionalInfo_Type()
)
receivedCivicLocationsAdditionalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedCivicLocationsAdditionalInfo.setStatus("current")
_ReceivedCivicLocationsName_Type = DisplayString
_ReceivedCivicLocationsName_Object = MibTableColumn
receivedCivicLocationsName = _ReceivedCivicLocationsName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 102, 1, 17),
    _ReceivedCivicLocationsName_Type()
)
receivedCivicLocationsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedCivicLocationsName.setStatus("current")
_ReceivedCivicLocationsZipCode_Type = DisplayString
_ReceivedCivicLocationsZipCode_Object = MibTableColumn
receivedCivicLocationsZipCode = _ReceivedCivicLocationsZipCode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 102, 1, 18),
    _ReceivedCivicLocationsZipCode_Type()
)
receivedCivicLocationsZipCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedCivicLocationsZipCode.setStatus("current")
_ReceivedCivicLocationsBuilding_Type = DisplayString
_ReceivedCivicLocationsBuilding_Object = MibTableColumn
receivedCivicLocationsBuilding = _ReceivedCivicLocationsBuilding_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 102, 1, 19),
    _ReceivedCivicLocationsBuilding_Type()
)
receivedCivicLocationsBuilding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedCivicLocationsBuilding.setStatus("current")
_ReceivedCivicLocationsUnit_Type = DisplayString
_ReceivedCivicLocationsUnit_Object = MibTableColumn
receivedCivicLocationsUnit = _ReceivedCivicLocationsUnit_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 102, 1, 20),
    _ReceivedCivicLocationsUnit_Type()
)
receivedCivicLocationsUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedCivicLocationsUnit.setStatus("current")
_ReceivedCivicLocationsFloor_Type = DisplayString
_ReceivedCivicLocationsFloor_Object = MibTableColumn
receivedCivicLocationsFloor = _ReceivedCivicLocationsFloor_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 102, 1, 21),
    _ReceivedCivicLocationsFloor_Type()
)
receivedCivicLocationsFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedCivicLocationsFloor.setStatus("current")
_ReceivedCivicLocationsRoom_Type = DisplayString
_ReceivedCivicLocationsRoom_Object = MibTableColumn
receivedCivicLocationsRoom = _ReceivedCivicLocationsRoom_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 102, 1, 22),
    _ReceivedCivicLocationsRoom_Type()
)
receivedCivicLocationsRoom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedCivicLocationsRoom.setStatus("current")
_ReceivedCivicLocationsPlaceType_Type = DisplayString
_ReceivedCivicLocationsPlaceType_Object = MibTableColumn
receivedCivicLocationsPlaceType = _ReceivedCivicLocationsPlaceType_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 102, 1, 23),
    _ReceivedCivicLocationsPlaceType_Type()
)
receivedCivicLocationsPlaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedCivicLocationsPlaceType.setStatus("current")
_ReceivedCivicLocationsScript_Type = DisplayString
_ReceivedCivicLocationsScript_Object = MibTableColumn
receivedCivicLocationsScript = _ReceivedCivicLocationsScript_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 102, 1, 24),
    _ReceivedCivicLocationsScript_Type()
)
receivedCivicLocationsScript.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedCivicLocationsScript.setStatus("current")
_ReceivedCivicLocationsElinNumber_Type = DisplayString
_ReceivedCivicLocationsElinNumber_Object = MibTableColumn
receivedCivicLocationsElinNumber = _ReceivedCivicLocationsElinNumber_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 102, 1, 25),
    _ReceivedCivicLocationsElinNumber_Type()
)
receivedCivicLocationsElinNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedCivicLocationsElinNumber.setStatus("current")
_ReceivedPoliciesTable_Object = MibTable
receivedPoliciesTable = _ReceivedPoliciesTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 103)
)
if mibBuilder.loadTexts:
    receivedPoliciesTable.setStatus("current")
_ReceivedPoliciesEntry_Object = MibTableRow
receivedPoliciesEntry = _ReceivedPoliciesEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 103, 1)
)
receivedPoliciesEntry.setIndexNames(
    (0, "G6-LLDP-MIB", "receivedPoliciesPortIndex"),
)
if mibBuilder.loadTexts:
    receivedPoliciesEntry.setStatus("current")


class _ReceivedPoliciesPortIndex_Type(Integer32):
    """Custom type receivedPoliciesPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_ReceivedPoliciesPortIndex_Type.__name__ = "Integer32"
_ReceivedPoliciesPortIndex_Object = MibTableColumn
receivedPoliciesPortIndex = _ReceivedPoliciesPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 103, 1, 1),
    _ReceivedPoliciesPortIndex_Type()
)
receivedPoliciesPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    receivedPoliciesPortIndex.setStatus("current")


class _ReceivedPoliciesApplicationType_Type(Integer32):
    """Custom type receivedPoliciesApplicationType based on Integer32"""
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
          ("softphoneVoice", 5),
          ("videoConferencing", 6),
          ("streamingVideo", 7),
          ("videoSignaling", 8))
    )


_ReceivedPoliciesApplicationType_Type.__name__ = "Integer32"
_ReceivedPoliciesApplicationType_Object = MibTableColumn
receivedPoliciesApplicationType = _ReceivedPoliciesApplicationType_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 103, 1, 2),
    _ReceivedPoliciesApplicationType_Type()
)
receivedPoliciesApplicationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedPoliciesApplicationType.setStatus("current")


class _ReceivedPoliciesPolicyDefined_Type(Integer32):
    """Custom type receivedPoliciesPolicyDefined based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_ReceivedPoliciesPolicyDefined_Type.__name__ = "Integer32"
_ReceivedPoliciesPolicyDefined_Object = MibTableColumn
receivedPoliciesPolicyDefined = _ReceivedPoliciesPolicyDefined_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 103, 1, 3),
    _ReceivedPoliciesPolicyDefined_Type()
)
receivedPoliciesPolicyDefined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedPoliciesPolicyDefined.setStatus("current")


class _ReceivedPoliciesTaggedVlan_Type(Integer32):
    """Custom type receivedPoliciesTaggedVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_ReceivedPoliciesTaggedVlan_Type.__name__ = "Integer32"
_ReceivedPoliciesTaggedVlan_Object = MibTableColumn
receivedPoliciesTaggedVlan = _ReceivedPoliciesTaggedVlan_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 103, 1, 4),
    _ReceivedPoliciesTaggedVlan_Type()
)
receivedPoliciesTaggedVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedPoliciesTaggedVlan.setStatus("current")
_ReceivedPoliciesVlanId_Type = Unsigned32
_ReceivedPoliciesVlanId_Object = MibTableColumn
receivedPoliciesVlanId = _ReceivedPoliciesVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 103, 1, 5),
    _ReceivedPoliciesVlanId_Type()
)
receivedPoliciesVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedPoliciesVlanId.setStatus("current")


class _ReceivedPoliciesLayer2Priority_Type(Integer32):
    """Custom type receivedPoliciesLayer2Priority based on Integer32"""
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
          ("background", 1),
          ("spare", 2),
          ("bestEffort", 3),
          ("excellentEffort", 4),
          ("controlledLoad", 5),
          ("video", 6),
          ("voice", 7),
          ("networkControl", 8))
    )


_ReceivedPoliciesLayer2Priority_Type.__name__ = "Integer32"
_ReceivedPoliciesLayer2Priority_Object = MibTableColumn
receivedPoliciesLayer2Priority = _ReceivedPoliciesLayer2Priority_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 103, 1, 6),
    _ReceivedPoliciesLayer2Priority_Type()
)
receivedPoliciesLayer2Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedPoliciesLayer2Priority.setStatus("current")


class _ReceivedPoliciesDscp_Type(Integer32):
    """Custom type receivedPoliciesDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ReceivedPoliciesDscp_Type.__name__ = "Integer32"
_ReceivedPoliciesDscp_Object = MibTableColumn
receivedPoliciesDscp = _ReceivedPoliciesDscp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 103, 1, 7),
    _ReceivedPoliciesDscp_Type()
)
receivedPoliciesDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedPoliciesDscp.setStatus("current")
_ReceivedInventoryInfosTable_Object = MibTable
receivedInventoryInfosTable = _ReceivedInventoryInfosTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 104)
)
if mibBuilder.loadTexts:
    receivedInventoryInfosTable.setStatus("current")
_ReceivedInventoryInfosEntry_Object = MibTableRow
receivedInventoryInfosEntry = _ReceivedInventoryInfosEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 104, 1)
)
receivedInventoryInfosEntry.setIndexNames(
    (0, "G6-LLDP-MIB", "receivedInventoryInfosPortIndex"),
)
if mibBuilder.loadTexts:
    receivedInventoryInfosEntry.setStatus("current")


class _ReceivedInventoryInfosPortIndex_Type(Integer32):
    """Custom type receivedInventoryInfosPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_ReceivedInventoryInfosPortIndex_Type.__name__ = "Integer32"
_ReceivedInventoryInfosPortIndex_Object = MibTableColumn
receivedInventoryInfosPortIndex = _ReceivedInventoryInfosPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 104, 1, 1),
    _ReceivedInventoryInfosPortIndex_Type()
)
receivedInventoryInfosPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    receivedInventoryInfosPortIndex.setStatus("current")
_ReceivedInventoryInfosHardwareRevision_Type = DisplayString
_ReceivedInventoryInfosHardwareRevision_Object = MibTableColumn
receivedInventoryInfosHardwareRevision = _ReceivedInventoryInfosHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 104, 1, 2),
    _ReceivedInventoryInfosHardwareRevision_Type()
)
receivedInventoryInfosHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedInventoryInfosHardwareRevision.setStatus("current")
_ReceivedInventoryInfosFirmwareRevision_Type = DisplayString
_ReceivedInventoryInfosFirmwareRevision_Object = MibTableColumn
receivedInventoryInfosFirmwareRevision = _ReceivedInventoryInfosFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 104, 1, 3),
    _ReceivedInventoryInfosFirmwareRevision_Type()
)
receivedInventoryInfosFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedInventoryInfosFirmwareRevision.setStatus("current")
_ReceivedInventoryInfosSoftwareRevision_Type = DisplayString
_ReceivedInventoryInfosSoftwareRevision_Object = MibTableColumn
receivedInventoryInfosSoftwareRevision = _ReceivedInventoryInfosSoftwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 104, 1, 4),
    _ReceivedInventoryInfosSoftwareRevision_Type()
)
receivedInventoryInfosSoftwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedInventoryInfosSoftwareRevision.setStatus("current")
_ReceivedInventoryInfosSerialNumber_Type = DisplayString
_ReceivedInventoryInfosSerialNumber_Object = MibTableColumn
receivedInventoryInfosSerialNumber = _ReceivedInventoryInfosSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 104, 1, 5),
    _ReceivedInventoryInfosSerialNumber_Type()
)
receivedInventoryInfosSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedInventoryInfosSerialNumber.setStatus("current")
_ReceivedInventoryInfosManufacturer_Type = DisplayString
_ReceivedInventoryInfosManufacturer_Object = MibTableColumn
receivedInventoryInfosManufacturer = _ReceivedInventoryInfosManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 104, 1, 6),
    _ReceivedInventoryInfosManufacturer_Type()
)
receivedInventoryInfosManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedInventoryInfosManufacturer.setStatus("current")
_ReceivedInventoryInfosModelName_Type = DisplayString
_ReceivedInventoryInfosModelName_Object = MibTableColumn
receivedInventoryInfosModelName = _ReceivedInventoryInfosModelName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 104, 1, 7),
    _ReceivedInventoryInfosModelName_Type()
)
receivedInventoryInfosModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedInventoryInfosModelName.setStatus("current")
_ReceivedInventoryInfosAssetId_Type = DisplayString
_ReceivedInventoryInfosAssetId_Object = MibTableColumn
receivedInventoryInfosAssetId = _ReceivedInventoryInfosAssetId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 104, 1, 8),
    _ReceivedInventoryInfosAssetId_Type()
)
receivedInventoryInfosAssetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedInventoryInfosAssetId.setStatus("current")
_ReceivedPoeInfosTable_Object = MibTable
receivedPoeInfosTable = _ReceivedPoeInfosTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 105)
)
if mibBuilder.loadTexts:
    receivedPoeInfosTable.setStatus("current")
_ReceivedPoeInfosEntry_Object = MibTableRow
receivedPoeInfosEntry = _ReceivedPoeInfosEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 105, 1)
)
receivedPoeInfosEntry.setIndexNames(
    (0, "G6-LLDP-MIB", "receivedPoeInfosPortIndex"),
)
if mibBuilder.loadTexts:
    receivedPoeInfosEntry.setStatus("current")


class _ReceivedPoeInfosPortIndex_Type(Integer32):
    """Custom type receivedPoeInfosPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_ReceivedPoeInfosPortIndex_Type.__name__ = "Integer32"
_ReceivedPoeInfosPortIndex_Object = MibTableColumn
receivedPoeInfosPortIndex = _ReceivedPoeInfosPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 105, 1, 1),
    _ReceivedPoeInfosPortIndex_Type()
)
receivedPoeInfosPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    receivedPoeInfosPortIndex.setStatus("current")


class _ReceivedPoeInfosType_Type(Integer32):
    """Custom type receivedPoeInfosType based on Integer32"""
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
          ("pse", 1),
          ("pd", 2),
          ("noPoe", 3))
    )


_ReceivedPoeInfosType_Type.__name__ = "Integer32"
_ReceivedPoeInfosType_Object = MibTableColumn
receivedPoeInfosType = _ReceivedPoeInfosType_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 105, 1, 2),
    _ReceivedPoeInfosType_Type()
)
receivedPoeInfosType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedPoeInfosType.setStatus("current")


class _ReceivedPoeInfosSource_Type(Integer32):
    """Custom type receivedPoeInfosSource based on Integer32"""
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
          ("pdPsePrimary", 1),
          ("pdLocalBackup", 2),
          ("pdPseLocal", 3))
    )


_ReceivedPoeInfosSource_Type.__name__ = "Integer32"
_ReceivedPoeInfosSource_Object = MibTableColumn
receivedPoeInfosSource = _ReceivedPoeInfosSource_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 105, 1, 3),
    _ReceivedPoeInfosSource_Type()
)
receivedPoeInfosSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedPoeInfosSource.setStatus("current")


class _ReceivedPoeInfosPriority_Type(Integer32):
    """Custom type receivedPoeInfosPriority based on Integer32"""
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
          ("critical", 1),
          ("high", 2),
          ("low", 3))
    )


_ReceivedPoeInfosPriority_Type.__name__ = "Integer32"
_ReceivedPoeInfosPriority_Object = MibTableColumn
receivedPoeInfosPriority = _ReceivedPoeInfosPriority_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 105, 1, 4),
    _ReceivedPoeInfosPriority_Type()
)
receivedPoeInfosPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedPoeInfosPriority.setStatus("current")
_ReceivedPoeInfosValue_Type = Unsigned32
_ReceivedPoeInfosValue_Object = MibTableColumn
receivedPoeInfosValue = _ReceivedPoeInfosValue_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 105, 1, 5),
    _ReceivedPoeInfosValue_Type()
)
receivedPoeInfosValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedPoeInfosValue.setStatus("current")
_ReceivedPoeControlTable_Object = MibTable
receivedPoeControlTable = _ReceivedPoeControlTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 106)
)
if mibBuilder.loadTexts:
    receivedPoeControlTable.setStatus("current")
_ReceivedPoeControlEntry_Object = MibTableRow
receivedPoeControlEntry = _ReceivedPoeControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 106, 1)
)
receivedPoeControlEntry.setIndexNames(
    (0, "G6-LLDP-MIB", "receivedPoeControlPortIndex"),
)
if mibBuilder.loadTexts:
    receivedPoeControlEntry.setStatus("current")


class _ReceivedPoeControlPortIndex_Type(Integer32):
    """Custom type receivedPoeControlPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_ReceivedPoeControlPortIndex_Type.__name__ = "Integer32"
_ReceivedPoeControlPortIndex_Object = MibTableColumn
receivedPoeControlPortIndex = _ReceivedPoeControlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 106, 1, 1),
    _ReceivedPoeControlPortIndex_Type()
)
receivedPoeControlPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    receivedPoeControlPortIndex.setStatus("current")


class _ReceivedPoeControlType_Type(Integer32):
    """Custom type receivedPoeControlType based on Integer32"""
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
          ("pse", 1),
          ("pd", 2),
          ("noPoe", 3))
    )


_ReceivedPoeControlType_Type.__name__ = "Integer32"
_ReceivedPoeControlType_Object = MibTableColumn
receivedPoeControlType = _ReceivedPoeControlType_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 106, 1, 2),
    _ReceivedPoeControlType_Type()
)
receivedPoeControlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedPoeControlType.setStatus("current")


class _ReceivedPoeControlPoePowerSupported_Type(Integer32):
    """Custom type receivedPoeControlPoePowerSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_ReceivedPoeControlPoePowerSupported_Type.__name__ = "Integer32"
_ReceivedPoeControlPoePowerSupported_Object = MibTableColumn
receivedPoeControlPoePowerSupported = _ReceivedPoeControlPoePowerSupported_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 106, 1, 3),
    _ReceivedPoeControlPoePowerSupported_Type()
)
receivedPoeControlPoePowerSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedPoeControlPoePowerSupported.setStatus("current")


class _ReceivedPoeControlPoePowerEnabled_Type(Integer32):
    """Custom type receivedPoeControlPoePowerEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_ReceivedPoeControlPoePowerEnabled_Type.__name__ = "Integer32"
_ReceivedPoeControlPoePowerEnabled_Object = MibTableColumn
receivedPoeControlPoePowerEnabled = _ReceivedPoeControlPoePowerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 106, 1, 4),
    _ReceivedPoeControlPoePowerEnabled_Type()
)
receivedPoeControlPoePowerEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedPoeControlPoePowerEnabled.setStatus("current")


class _ReceivedPoeControlPairControl_Type(Integer32):
    """Custom type receivedPoeControlPairControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_ReceivedPoeControlPairControl_Type.__name__ = "Integer32"
_ReceivedPoeControlPairControl_Object = MibTableColumn
receivedPoeControlPairControl = _ReceivedPoeControlPairControl_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 106, 1, 5),
    _ReceivedPoeControlPairControl_Type()
)
receivedPoeControlPairControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedPoeControlPairControl.setStatus("current")


class _ReceivedPoeControlPowerPairs_Type(Integer32):
    """Custom type receivedPoeControlPowerPairs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("signal", 1),
          ("spare", 2))
    )


_ReceivedPoeControlPowerPairs_Type.__name__ = "Integer32"
_ReceivedPoeControlPowerPairs_Object = MibTableColumn
receivedPoeControlPowerPairs = _ReceivedPoeControlPowerPairs_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 106, 1, 6),
    _ReceivedPoeControlPowerPairs_Type()
)
receivedPoeControlPowerPairs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedPoeControlPowerPairs.setStatus("current")


class _ReceivedPoeControlPowerClass_Type(Integer32):
    """Custom type receivedPoeControlPowerClass based on Integer32"""
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
        *(("noClass", 0),
          ("class0", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("class4", 5))
    )


_ReceivedPoeControlPowerClass_Type.__name__ = "Integer32"
_ReceivedPoeControlPowerClass_Object = MibTableColumn
receivedPoeControlPowerClass = _ReceivedPoeControlPowerClass_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 106, 1, 7),
    _ReceivedPoeControlPowerClass_Type()
)
receivedPoeControlPowerClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedPoeControlPowerClass.setStatus("current")


class _ReceivedPoeControlDeviceType_Type(Integer32):
    """Custom type receivedPoeControlDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ReceivedPoeControlDeviceType_Type.__name__ = "Integer32"
_ReceivedPoeControlDeviceType_Object = MibTableColumn
receivedPoeControlDeviceType = _ReceivedPoeControlDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 106, 1, 8),
    _ReceivedPoeControlDeviceType_Type()
)
receivedPoeControlDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedPoeControlDeviceType.setStatus("current")


class _ReceivedPoeControlSource_Type(Integer32):
    """Custom type receivedPoeControlSource based on Integer32"""
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
          ("pdPsePrimary", 1),
          ("pdLocalBackup", 2),
          ("pdPseLocal", 3))
    )


_ReceivedPoeControlSource_Type.__name__ = "Integer32"
_ReceivedPoeControlSource_Object = MibTableColumn
receivedPoeControlSource = _ReceivedPoeControlSource_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 106, 1, 9),
    _ReceivedPoeControlSource_Type()
)
receivedPoeControlSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedPoeControlSource.setStatus("current")


class _ReceivedPoeControlPriority_Type(Integer32):
    """Custom type receivedPoeControlPriority based on Integer32"""
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
          ("critical", 1),
          ("high", 2),
          ("low", 3))
    )


_ReceivedPoeControlPriority_Type.__name__ = "Integer32"
_ReceivedPoeControlPriority_Object = MibTableColumn
receivedPoeControlPriority = _ReceivedPoeControlPriority_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 106, 1, 10),
    _ReceivedPoeControlPriority_Type()
)
receivedPoeControlPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedPoeControlPriority.setStatus("current")


class _ReceivedPoeControlPdRequestedPower_Type(Integer32):
    """Custom type receivedPoeControlPdRequestedPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ReceivedPoeControlPdRequestedPower_Type.__name__ = "Integer32"
_ReceivedPoeControlPdRequestedPower_Object = MibTableColumn
receivedPoeControlPdRequestedPower = _ReceivedPoeControlPdRequestedPower_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 106, 1, 11),
    _ReceivedPoeControlPdRequestedPower_Type()
)
receivedPoeControlPdRequestedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedPoeControlPdRequestedPower.setStatus("current")


class _ReceivedPoeControlPseAllocatedPower_Type(Integer32):
    """Custom type receivedPoeControlPseAllocatedPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ReceivedPoeControlPseAllocatedPower_Type.__name__ = "Integer32"
_ReceivedPoeControlPseAllocatedPower_Object = MibTableColumn
receivedPoeControlPseAllocatedPower = _ReceivedPoeControlPseAllocatedPower_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 43, 106, 1, 12),
    _ReceivedPoeControlPseAllocatedPower_Type()
)
receivedPoeControlPseAllocatedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedPoeControlPseAllocatedPower.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "G6-LLDP-MIB",
    **{"protocol": protocol,
       "lldp": lldp,
       "configTable": configTable,
       "configEntry": configEntry,
       "configIndex": configIndex,
       "configEnableLldp": configEnableLldp,
       "configEnableCdp": configEnableCdp,
       "configLldpEnabledPorts": configLldpEnabledPorts,
       "configReceiveOnly": configReceiveOnly,
       "configForwardToLink": configForwardToLink,
       "configAdvertizedMedClass": configAdvertizedMedClass,
       "configDisableMedInventory": configDisableMedInventory,
       "configDisableVoiceVlanTlv": configDisableVoiceVlanTlv,
       "configCdpVersion": configCdpVersion,
       "configVoiceVlanPrio": configVoiceVlanPrio,
       "configVoiceVlanSignalPrio": configVoiceVlanSignalPrio,
       "configVoiceDscp": configVoiceDscp,
       "configSignalingDscp": configSignalingDscp,
       "configTimeToLive": configTimeToLive,
       "configTxDelay": configTxDelay,
       "configMsgTxInterval": configMsgTxInterval,
       "configForceLldpTransmission": configForceLldpTransmission,
       "configLldpResponsePreferred": configLldpResponsePreferred,
       "localCoordinatesTable": localCoordinatesTable,
       "localCoordinatesEntry": localCoordinatesEntry,
       "localCoordinatesIndex": localCoordinatesIndex,
       "localCoordinatesLatitude": localCoordinatesLatitude,
       "localCoordinatesLatResolution": localCoordinatesLatResolution,
       "localCoordinatesLongitude": localCoordinatesLongitude,
       "localCoordinatesLongResolution": localCoordinatesLongResolution,
       "localCoordinatesAltitude": localCoordinatesAltitude,
       "localCoordinatesAltResolution": localCoordinatesAltResolution,
       "localCoordinatesAltType": localCoordinatesAltType,
       "localCoordinatesDatum": localCoordinatesDatum,
       "localCivicLocationTable": localCivicLocationTable,
       "localCivicLocationEntry": localCivicLocationEntry,
       "localCivicLocationIndex": localCivicLocationIndex,
       "localCivicLocationCountryCode": localCivicLocationCountryCode,
       "localCivicLocationLanguage": localCivicLocationLanguage,
       "localCivicLocationNationalSubdivision": localCivicLocationNationalSubdivision,
       "localCivicLocationCounty": localCivicLocationCounty,
       "localCivicLocationTown": localCivicLocationTown,
       "localCivicLocationDistrict": localCivicLocationDistrict,
       "localCivicLocationBlock": localCivicLocationBlock,
       "localCivicLocationStreet": localCivicLocationStreet,
       "localCivicLocationLeadingStreetDirection": localCivicLocationLeadingStreetDirection,
       "localCivicLocationTrailingStreetSuffix": localCivicLocationTrailingStreetSuffix,
       "localCivicLocationStreetSuffix": localCivicLocationStreetSuffix,
       "localCivicLocationHouseNumber": localCivicLocationHouseNumber,
       "localCivicLocationHouseNumberSuffix": localCivicLocationHouseNumberSuffix,
       "localCivicLocationLandmark": localCivicLocationLandmark,
       "localCivicLocationAdditionalInfo": localCivicLocationAdditionalInfo,
       "localCivicLocationName": localCivicLocationName,
       "localCivicLocationZipCode": localCivicLocationZipCode,
       "localCivicLocationBuilding": localCivicLocationBuilding,
       "localCivicLocationUnit": localCivicLocationUnit,
       "localCivicLocationFloor": localCivicLocationFloor,
       "localCivicLocationRoom": localCivicLocationRoom,
       "localCivicLocationPlaceType": localCivicLocationPlaceType,
       "localCivicLocationScript": localCivicLocationScript,
       "localCivicLocationElinNumber": localCivicLocationElinNumber,
       "receivedOverviewTable": receivedOverviewTable,
       "receivedOverviewEntry": receivedOverviewEntry,
       "receivedOverviewPortIndex": receivedOverviewPortIndex,
       "receivedOverviewSysName": receivedOverviewSysName,
       "receivedOverviewSysDesc": receivedOverviewSysDesc,
       "receivedOverviewChassisIdSubtype": receivedOverviewChassisIdSubtype,
       "receivedOverviewChassisId": receivedOverviewChassisId,
       "receivedOverviewMgmtIp": receivedOverviewMgmtIp,
       "receivedOverviewMgmtOid": receivedOverviewMgmtOid,
       "receivedOverviewCapabilities": receivedOverviewCapabilities,
       "receivedOverviewCapabilitiesEnabled": receivedOverviewCapabilitiesEnabled,
       "receivedOverviewMedCapabilities": receivedOverviewMedCapabilities,
       "receivedOverviewPortIdSubtype": receivedOverviewPortIdSubtype,
       "receivedOverviewPortIdentification": receivedOverviewPortIdentification,
       "receivedOverviewPortDescription": receivedOverviewPortDescription,
       "receivedOverviewPortVlan": receivedOverviewPortVlan,
       "receivedCoordinatesTable": receivedCoordinatesTable,
       "receivedCoordinatesEntry": receivedCoordinatesEntry,
       "receivedCoordinatesPortIndex": receivedCoordinatesPortIndex,
       "receivedCoordinatesLatitude": receivedCoordinatesLatitude,
       "receivedCoordinatesLatResolution": receivedCoordinatesLatResolution,
       "receivedCoordinatesLongitude": receivedCoordinatesLongitude,
       "receivedCoordinatesLongResolution": receivedCoordinatesLongResolution,
       "receivedCoordinatesAltitude": receivedCoordinatesAltitude,
       "receivedCoordinatesAltResolution": receivedCoordinatesAltResolution,
       "receivedCoordinatesAltUnit": receivedCoordinatesAltUnit,
       "receivedCoordinatesDatum": receivedCoordinatesDatum,
       "receivedCivicLocationsTable": receivedCivicLocationsTable,
       "receivedCivicLocationsEntry": receivedCivicLocationsEntry,
       "receivedCivicLocationsPortIndex": receivedCivicLocationsPortIndex,
       "receivedCivicLocationsCountryCode": receivedCivicLocationsCountryCode,
       "receivedCivicLocationsLanguage": receivedCivicLocationsLanguage,
       "receivedCivicLocationsNationalSubdivision": receivedCivicLocationsNationalSubdivision,
       "receivedCivicLocationsCounty": receivedCivicLocationsCounty,
       "receivedCivicLocationsTown": receivedCivicLocationsTown,
       "receivedCivicLocationsDistrict": receivedCivicLocationsDistrict,
       "receivedCivicLocationsBlock": receivedCivicLocationsBlock,
       "receivedCivicLocationsStreet": receivedCivicLocationsStreet,
       "receivedCivicLocationsLeadingStreetDirection": receivedCivicLocationsLeadingStreetDirection,
       "receivedCivicLocationsTrailingStreetSuffix": receivedCivicLocationsTrailingStreetSuffix,
       "receivedCivicLocationsStreetSuffix": receivedCivicLocationsStreetSuffix,
       "receivedCivicLocationsHouseNumber": receivedCivicLocationsHouseNumber,
       "receivedCivicLocationsHouseNumberSuffix": receivedCivicLocationsHouseNumberSuffix,
       "receivedCivicLocationsLandmark": receivedCivicLocationsLandmark,
       "receivedCivicLocationsAdditionalInfo": receivedCivicLocationsAdditionalInfo,
       "receivedCivicLocationsName": receivedCivicLocationsName,
       "receivedCivicLocationsZipCode": receivedCivicLocationsZipCode,
       "receivedCivicLocationsBuilding": receivedCivicLocationsBuilding,
       "receivedCivicLocationsUnit": receivedCivicLocationsUnit,
       "receivedCivicLocationsFloor": receivedCivicLocationsFloor,
       "receivedCivicLocationsRoom": receivedCivicLocationsRoom,
       "receivedCivicLocationsPlaceType": receivedCivicLocationsPlaceType,
       "receivedCivicLocationsScript": receivedCivicLocationsScript,
       "receivedCivicLocationsElinNumber": receivedCivicLocationsElinNumber,
       "receivedPoliciesTable": receivedPoliciesTable,
       "receivedPoliciesEntry": receivedPoliciesEntry,
       "receivedPoliciesPortIndex": receivedPoliciesPortIndex,
       "receivedPoliciesApplicationType": receivedPoliciesApplicationType,
       "receivedPoliciesPolicyDefined": receivedPoliciesPolicyDefined,
       "receivedPoliciesTaggedVlan": receivedPoliciesTaggedVlan,
       "receivedPoliciesVlanId": receivedPoliciesVlanId,
       "receivedPoliciesLayer2Priority": receivedPoliciesLayer2Priority,
       "receivedPoliciesDscp": receivedPoliciesDscp,
       "receivedInventoryInfosTable": receivedInventoryInfosTable,
       "receivedInventoryInfosEntry": receivedInventoryInfosEntry,
       "receivedInventoryInfosPortIndex": receivedInventoryInfosPortIndex,
       "receivedInventoryInfosHardwareRevision": receivedInventoryInfosHardwareRevision,
       "receivedInventoryInfosFirmwareRevision": receivedInventoryInfosFirmwareRevision,
       "receivedInventoryInfosSoftwareRevision": receivedInventoryInfosSoftwareRevision,
       "receivedInventoryInfosSerialNumber": receivedInventoryInfosSerialNumber,
       "receivedInventoryInfosManufacturer": receivedInventoryInfosManufacturer,
       "receivedInventoryInfosModelName": receivedInventoryInfosModelName,
       "receivedInventoryInfosAssetId": receivedInventoryInfosAssetId,
       "receivedPoeInfosTable": receivedPoeInfosTable,
       "receivedPoeInfosEntry": receivedPoeInfosEntry,
       "receivedPoeInfosPortIndex": receivedPoeInfosPortIndex,
       "receivedPoeInfosType": receivedPoeInfosType,
       "receivedPoeInfosSource": receivedPoeInfosSource,
       "receivedPoeInfosPriority": receivedPoeInfosPriority,
       "receivedPoeInfosValue": receivedPoeInfosValue,
       "receivedPoeControlTable": receivedPoeControlTable,
       "receivedPoeControlEntry": receivedPoeControlEntry,
       "receivedPoeControlPortIndex": receivedPoeControlPortIndex,
       "receivedPoeControlType": receivedPoeControlType,
       "receivedPoeControlPoePowerSupported": receivedPoeControlPoePowerSupported,
       "receivedPoeControlPoePowerEnabled": receivedPoeControlPoePowerEnabled,
       "receivedPoeControlPairControl": receivedPoeControlPairControl,
       "receivedPoeControlPowerPairs": receivedPoeControlPowerPairs,
       "receivedPoeControlPowerClass": receivedPoeControlPowerClass,
       "receivedPoeControlDeviceType": receivedPoeControlDeviceType,
       "receivedPoeControlSource": receivedPoeControlSource,
       "receivedPoeControlPriority": receivedPoeControlPriority,
       "receivedPoeControlPdRequestedPower": receivedPoeControlPdRequestedPower,
       "receivedPoeControlPseAllocatedPower": receivedPoeControlPseAllocatedPower}
)
