# SNMP MIB module (ARICENT-MIVLAN-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-MIVLAN-EXT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:44:19 2025
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "ARICENTP-BRIDGE-MIB",
    "EnabledStatus")

(VlanId,) = mibBuilder.importSymbols(
    "AricentMIVlan-MIB",
    "VlanId")

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

futureMIVlanExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 138)
)
if mibBuilder.loadTexts:
    futureMIVlanExtMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TunnelStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("peer", 1),
          ("tunnel", 2),
          ("discard", 3))
    )



class L2CPProtocols(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 23),
    )



# MIB Managed Objects in the order of their OIDs

_FsMIVlanSystemConfig_ObjectIdentity = ObjectIdentity
fsMIVlanSystemConfig = _FsMIVlanSystemConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 138, 1)
)
_FsMIVlanBridgeInfoTable_Object = MibTable
fsMIVlanBridgeInfoTable = _FsMIVlanBridgeInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 1, 1)
)
if mibBuilder.loadTexts:
    fsMIVlanBridgeInfoTable.setStatus("current")
_FsMIVlanBridgeInfoEntry_Object = MibTableRow
fsMIVlanBridgeInfoEntry = _FsMIVlanBridgeInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 1, 1, 1)
)
fsMIVlanBridgeInfoEntry.setIndexNames(
    (0, "ARICENT-MIVLAN-EXT-MIB", "fsMIVlanContextId"),
)
if mibBuilder.loadTexts:
    fsMIVlanBridgeInfoEntry.setStatus("current")


class _FsMIVlanContextId_Type(Integer32):
    """Custom type fsMIVlanContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIVlanContextId_Type.__name__ = "Integer32"
_FsMIVlanContextId_Object = MibTableColumn
fsMIVlanContextId = _FsMIVlanContextId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 1, 1, 1, 1),
    _FsMIVlanContextId_Type()
)
fsMIVlanContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIVlanContextId.setStatus("current")


class _FsMIVlanBridgeMode_Type(Integer32):
    """Custom type fsMIVlanBridgeMode based on Integer32"""
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
        *(("customerBridge", 1),
          ("providerBridge", 2),
          ("providerEdgeBridge", 3),
          ("providerCoreBridge", 4),
          ("providerBackoneICompBridge", 5),
          ("providerBackoneBCompBridge", 6),
          ("invalidBridgeMode", 7))
    )


_FsMIVlanBridgeMode_Type.__name__ = "Integer32"
_FsMIVlanBridgeMode_Object = MibTableColumn
fsMIVlanBridgeMode = _FsMIVlanBridgeMode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 1, 1, 1, 2),
    _FsMIVlanBridgeMode_Type()
)
fsMIVlanBridgeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIVlanBridgeMode.setStatus("current")
_FsMIVlanTunnelObjects_ObjectIdentity = ObjectIdentity
fsMIVlanTunnelObjects = _FsMIVlanTunnelObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2)
)
_FsMIVlanTunnelContextInfoTable_Object = MibTable
fsMIVlanTunnelContextInfoTable = _FsMIVlanTunnelContextInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 1)
)
if mibBuilder.loadTexts:
    fsMIVlanTunnelContextInfoTable.setStatus("current")
_FsMIVlanTunnelContextInfoEntry_Object = MibTableRow
fsMIVlanTunnelContextInfoEntry = _FsMIVlanTunnelContextInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 1, 1)
)
fsMIVlanTunnelContextInfoEntry.setIndexNames(
    (0, "ARICENT-MIVLAN-EXT-MIB", "fsMIVlanContextId"),
)
if mibBuilder.loadTexts:
    fsMIVlanTunnelContextInfoEntry.setStatus("current")


class _FsMIVlanTunnelBpduPri_Type(Integer32):
    """Custom type fsMIVlanTunnelBpduPri based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsMIVlanTunnelBpduPri_Type.__name__ = "Integer32"
_FsMIVlanTunnelBpduPri_Object = MibTableColumn
fsMIVlanTunnelBpduPri = _FsMIVlanTunnelBpduPri_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 1, 1, 1),
    _FsMIVlanTunnelBpduPri_Type()
)
fsMIVlanTunnelBpduPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIVlanTunnelBpduPri.setStatus("current")
_FsMIVlanTunnelStpAddress_Type = MacAddress
_FsMIVlanTunnelStpAddress_Object = MibTableColumn
fsMIVlanTunnelStpAddress = _FsMIVlanTunnelStpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 1, 1, 2),
    _FsMIVlanTunnelStpAddress_Type()
)
fsMIVlanTunnelStpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIVlanTunnelStpAddress.setStatus("current")
_FsMIVlanTunnelLacpAddress_Type = MacAddress
_FsMIVlanTunnelLacpAddress_Object = MibTableColumn
fsMIVlanTunnelLacpAddress = _FsMIVlanTunnelLacpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 1, 1, 3),
    _FsMIVlanTunnelLacpAddress_Type()
)
fsMIVlanTunnelLacpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIVlanTunnelLacpAddress.setStatus("current")
_FsMIVlanTunnelDot1xAddress_Type = MacAddress
_FsMIVlanTunnelDot1xAddress_Object = MibTableColumn
fsMIVlanTunnelDot1xAddress = _FsMIVlanTunnelDot1xAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 1, 1, 4),
    _FsMIVlanTunnelDot1xAddress_Type()
)
fsMIVlanTunnelDot1xAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIVlanTunnelDot1xAddress.setStatus("current")
_FsMIVlanTunnelGvrpAddress_Type = MacAddress
_FsMIVlanTunnelGvrpAddress_Object = MibTableColumn
fsMIVlanTunnelGvrpAddress = _FsMIVlanTunnelGvrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 1, 1, 5),
    _FsMIVlanTunnelGvrpAddress_Type()
)
fsMIVlanTunnelGvrpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIVlanTunnelGvrpAddress.setStatus("current")
_FsMIVlanTunnelGmrpAddress_Type = MacAddress
_FsMIVlanTunnelGmrpAddress_Object = MibTableColumn
fsMIVlanTunnelGmrpAddress = _FsMIVlanTunnelGmrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 1, 1, 6),
    _FsMIVlanTunnelGmrpAddress_Type()
)
fsMIVlanTunnelGmrpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIVlanTunnelGmrpAddress.setStatus("current")
_FsMIVlanTunnelMvrpAddress_Type = MacAddress
_FsMIVlanTunnelMvrpAddress_Object = MibTableColumn
fsMIVlanTunnelMvrpAddress = _FsMIVlanTunnelMvrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 1, 1, 7),
    _FsMIVlanTunnelMvrpAddress_Type()
)
fsMIVlanTunnelMvrpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIVlanTunnelMvrpAddress.setStatus("current")
_FsMIVlanTunnelMmrpAddress_Type = MacAddress
_FsMIVlanTunnelMmrpAddress_Object = MibTableColumn
fsMIVlanTunnelMmrpAddress = _FsMIVlanTunnelMmrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 1, 1, 8),
    _FsMIVlanTunnelMmrpAddress_Type()
)
fsMIVlanTunnelMmrpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIVlanTunnelMmrpAddress.setStatus("current")
_FsMIVlanTunnelElmiAddress_Type = MacAddress
_FsMIVlanTunnelElmiAddress_Object = MibTableColumn
fsMIVlanTunnelElmiAddress = _FsMIVlanTunnelElmiAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 1, 1, 9),
    _FsMIVlanTunnelElmiAddress_Type()
)
fsMIVlanTunnelElmiAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIVlanTunnelElmiAddress.setStatus("current")
_FsMIVlanTunnelLldpAddress_Type = MacAddress
_FsMIVlanTunnelLldpAddress_Object = MibTableColumn
fsMIVlanTunnelLldpAddress = _FsMIVlanTunnelLldpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 1, 1, 10),
    _FsMIVlanTunnelLldpAddress_Type()
)
fsMIVlanTunnelLldpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIVlanTunnelLldpAddress.setStatus("current")
_FsMIVlanTunnelEcfmAddress_Type = MacAddress
_FsMIVlanTunnelEcfmAddress_Object = MibTableColumn
fsMIVlanTunnelEcfmAddress = _FsMIVlanTunnelEcfmAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 1, 1, 11),
    _FsMIVlanTunnelEcfmAddress_Type()
)
fsMIVlanTunnelEcfmAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIVlanTunnelEcfmAddress.setStatus("current")
_FsMIVlanTunnelEoamAddress_Type = MacAddress
_FsMIVlanTunnelEoamAddress_Object = MibTableColumn
fsMIVlanTunnelEoamAddress = _FsMIVlanTunnelEoamAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 1, 1, 12),
    _FsMIVlanTunnelEoamAddress_Type()
)
fsMIVlanTunnelEoamAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIVlanTunnelEoamAddress.setStatus("current")
_FsMIVlanTunnelIgmpAddress_Type = MacAddress
_FsMIVlanTunnelIgmpAddress_Object = MibTableColumn
fsMIVlanTunnelIgmpAddress = _FsMIVlanTunnelIgmpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 1, 1, 13),
    _FsMIVlanTunnelIgmpAddress_Type()
)
fsMIVlanTunnelIgmpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIVlanTunnelIgmpAddress.setStatus("current")
_FsMIVlanTunnelTable_Object = MibTable
fsMIVlanTunnelTable = _FsMIVlanTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 2)
)
if mibBuilder.loadTexts:
    fsMIVlanTunnelTable.setStatus("current")
_FsMIVlanTunnelEntry_Object = MibTableRow
fsMIVlanTunnelEntry = _FsMIVlanTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 2, 1)
)
fsMIVlanTunnelEntry.setIndexNames(
    (0, "ARICENT-MIVLAN-EXT-MIB", "fsMIVlanPort"),
)
if mibBuilder.loadTexts:
    fsMIVlanTunnelEntry.setStatus("current")


class _FsMIVlanPort_Type(Integer32):
    """Custom type fsMIVlanPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMIVlanPort_Type.__name__ = "Integer32"
_FsMIVlanPort_Object = MibTableColumn
fsMIVlanPort = _FsMIVlanPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 2, 1, 1),
    _FsMIVlanPort_Type()
)
fsMIVlanPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIVlanPort.setStatus("current")


class _FsMIVlanTunnelStatus_Type(EnabledStatus):
    """Custom type fsMIVlanTunnelStatus based on EnabledStatus"""
    defaultValue = 2


_FsMIVlanTunnelStatus_Type.__name__ = "EnabledStatus"
_FsMIVlanTunnelStatus_Object = MibTableColumn
fsMIVlanTunnelStatus = _FsMIVlanTunnelStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 2, 1, 2),
    _FsMIVlanTunnelStatus_Type()
)
fsMIVlanTunnelStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIVlanTunnelStatus.setStatus("current")
_FsMIVlanTunnelProtocolTable_Object = MibTable
fsMIVlanTunnelProtocolTable = _FsMIVlanTunnelProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 3)
)
if mibBuilder.loadTexts:
    fsMIVlanTunnelProtocolTable.setStatus("current")
_FsMIVlanTunnelProtocolEntry_Object = MibTableRow
fsMIVlanTunnelProtocolEntry = _FsMIVlanTunnelProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 3, 1)
)
fsMIVlanTunnelProtocolEntry.setIndexNames(
    (0, "ARICENT-MIVLAN-EXT-MIB", "fsMIVlanPort"),
)
if mibBuilder.loadTexts:
    fsMIVlanTunnelProtocolEntry.setStatus("current")
_FsMIVlanTunnelProtocolDot1x_Type = TunnelStatus
_FsMIVlanTunnelProtocolDot1x_Object = MibTableColumn
fsMIVlanTunnelProtocolDot1x = _FsMIVlanTunnelProtocolDot1x_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 3, 1, 1),
    _FsMIVlanTunnelProtocolDot1x_Type()
)
fsMIVlanTunnelProtocolDot1x.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIVlanTunnelProtocolDot1x.setStatus("current")
_FsMIVlanTunnelProtocolLacp_Type = TunnelStatus
_FsMIVlanTunnelProtocolLacp_Object = MibTableColumn
fsMIVlanTunnelProtocolLacp = _FsMIVlanTunnelProtocolLacp_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 3, 1, 2),
    _FsMIVlanTunnelProtocolLacp_Type()
)
fsMIVlanTunnelProtocolLacp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIVlanTunnelProtocolLacp.setStatus("current")
_FsMIVlanTunnelProtocolStp_Type = TunnelStatus
_FsMIVlanTunnelProtocolStp_Object = MibTableColumn
fsMIVlanTunnelProtocolStp = _FsMIVlanTunnelProtocolStp_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 3, 1, 3),
    _FsMIVlanTunnelProtocolStp_Type()
)
fsMIVlanTunnelProtocolStp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIVlanTunnelProtocolStp.setStatus("current")
_FsMIVlanTunnelProtocolGvrp_Type = TunnelStatus
_FsMIVlanTunnelProtocolGvrp_Object = MibTableColumn
fsMIVlanTunnelProtocolGvrp = _FsMIVlanTunnelProtocolGvrp_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 3, 1, 4),
    _FsMIVlanTunnelProtocolGvrp_Type()
)
fsMIVlanTunnelProtocolGvrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIVlanTunnelProtocolGvrp.setStatus("current")
_FsMIVlanTunnelProtocolGmrp_Type = TunnelStatus
_FsMIVlanTunnelProtocolGmrp_Object = MibTableColumn
fsMIVlanTunnelProtocolGmrp = _FsMIVlanTunnelProtocolGmrp_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 3, 1, 5),
    _FsMIVlanTunnelProtocolGmrp_Type()
)
fsMIVlanTunnelProtocolGmrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIVlanTunnelProtocolGmrp.setStatus("current")
_FsMIVlanTunnelProtocolIgmp_Type = TunnelStatus
_FsMIVlanTunnelProtocolIgmp_Object = MibTableColumn
fsMIVlanTunnelProtocolIgmp = _FsMIVlanTunnelProtocolIgmp_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 3, 1, 6),
    _FsMIVlanTunnelProtocolIgmp_Type()
)
fsMIVlanTunnelProtocolIgmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIVlanTunnelProtocolIgmp.setStatus("current")
_FsMIVlanTunnelProtocolMvrp_Type = TunnelStatus
_FsMIVlanTunnelProtocolMvrp_Object = MibTableColumn
fsMIVlanTunnelProtocolMvrp = _FsMIVlanTunnelProtocolMvrp_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 3, 1, 7),
    _FsMIVlanTunnelProtocolMvrp_Type()
)
fsMIVlanTunnelProtocolMvrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIVlanTunnelProtocolMvrp.setStatus("current")
_FsMIVlanTunnelProtocolMmrp_Type = TunnelStatus
_FsMIVlanTunnelProtocolMmrp_Object = MibTableColumn
fsMIVlanTunnelProtocolMmrp = _FsMIVlanTunnelProtocolMmrp_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 3, 1, 8),
    _FsMIVlanTunnelProtocolMmrp_Type()
)
fsMIVlanTunnelProtocolMmrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIVlanTunnelProtocolMmrp.setStatus("current")
_FsMIVlanTunnelProtocolElmi_Type = TunnelStatus
_FsMIVlanTunnelProtocolElmi_Object = MibTableColumn
fsMIVlanTunnelProtocolElmi = _FsMIVlanTunnelProtocolElmi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 3, 1, 9),
    _FsMIVlanTunnelProtocolElmi_Type()
)
fsMIVlanTunnelProtocolElmi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIVlanTunnelProtocolElmi.setStatus("current")
_FsMIVlanTunnelProtocolLldp_Type = TunnelStatus
_FsMIVlanTunnelProtocolLldp_Object = MibTableColumn
fsMIVlanTunnelProtocolLldp = _FsMIVlanTunnelProtocolLldp_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 3, 1, 10),
    _FsMIVlanTunnelProtocolLldp_Type()
)
fsMIVlanTunnelProtocolLldp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIVlanTunnelProtocolLldp.setStatus("current")
_FsMIVlanTunnelProtocolEcfm_Type = TunnelStatus
_FsMIVlanTunnelProtocolEcfm_Object = MibTableColumn
fsMIVlanTunnelProtocolEcfm = _FsMIVlanTunnelProtocolEcfm_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 3, 1, 11),
    _FsMIVlanTunnelProtocolEcfm_Type()
)
fsMIVlanTunnelProtocolEcfm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIVlanTunnelProtocolEcfm.setStatus("current")


class _FsMIVlanTunnelOverrideOption_Type(EnabledStatus):
    """Custom type fsMIVlanTunnelOverrideOption based on EnabledStatus"""
    defaultValue = 2


_FsMIVlanTunnelOverrideOption_Type.__name__ = "EnabledStatus"
_FsMIVlanTunnelOverrideOption_Object = MibTableColumn
fsMIVlanTunnelOverrideOption = _FsMIVlanTunnelOverrideOption_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 3, 1, 12),
    _FsMIVlanTunnelOverrideOption_Type()
)
fsMIVlanTunnelOverrideOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIVlanTunnelOverrideOption.setStatus("current")
_FsMIVlanTunnelProtocolEoam_Type = TunnelStatus
_FsMIVlanTunnelProtocolEoam_Object = MibTableColumn
fsMIVlanTunnelProtocolEoam = _FsMIVlanTunnelProtocolEoam_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 3, 1, 13),
    _FsMIVlanTunnelProtocolEoam_Type()
)
fsMIVlanTunnelProtocolEoam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIVlanTunnelProtocolEoam.setStatus("current")
_FsMIVlanTunnelProtocolStatsTable_Object = MibTable
fsMIVlanTunnelProtocolStatsTable = _FsMIVlanTunnelProtocolStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 4)
)
if mibBuilder.loadTexts:
    fsMIVlanTunnelProtocolStatsTable.setStatus("current")
_FsMIVlanTunnelProtocolStatsEntry_Object = MibTableRow
fsMIVlanTunnelProtocolStatsEntry = _FsMIVlanTunnelProtocolStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 4, 1)
)
fsMIVlanTunnelProtocolStatsEntry.setIndexNames(
    (0, "ARICENT-MIVLAN-EXT-MIB", "fsMIVlanPort"),
)
if mibBuilder.loadTexts:
    fsMIVlanTunnelProtocolStatsEntry.setStatus("current")
_FsMIVlanTunnelProtocolDot1xPktsRecvd_Type = Counter32
_FsMIVlanTunnelProtocolDot1xPktsRecvd_Object = MibTableColumn
fsMIVlanTunnelProtocolDot1xPktsRecvd = _FsMIVlanTunnelProtocolDot1xPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 4, 1, 1),
    _FsMIVlanTunnelProtocolDot1xPktsRecvd_Type()
)
fsMIVlanTunnelProtocolDot1xPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanTunnelProtocolDot1xPktsRecvd.setStatus("current")
_FsMIVlanTunnelProtocolDot1xPktsSent_Type = Counter32
_FsMIVlanTunnelProtocolDot1xPktsSent_Object = MibTableColumn
fsMIVlanTunnelProtocolDot1xPktsSent = _FsMIVlanTunnelProtocolDot1xPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 4, 1, 2),
    _FsMIVlanTunnelProtocolDot1xPktsSent_Type()
)
fsMIVlanTunnelProtocolDot1xPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanTunnelProtocolDot1xPktsSent.setStatus("current")
_FsMIVlanTunnelProtocolLacpPktsRecvd_Type = Counter32
_FsMIVlanTunnelProtocolLacpPktsRecvd_Object = MibTableColumn
fsMIVlanTunnelProtocolLacpPktsRecvd = _FsMIVlanTunnelProtocolLacpPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 4, 1, 3),
    _FsMIVlanTunnelProtocolLacpPktsRecvd_Type()
)
fsMIVlanTunnelProtocolLacpPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanTunnelProtocolLacpPktsRecvd.setStatus("current")
_FsMIVlanTunnelProtocolLacpPktsSent_Type = Counter32
_FsMIVlanTunnelProtocolLacpPktsSent_Object = MibTableColumn
fsMIVlanTunnelProtocolLacpPktsSent = _FsMIVlanTunnelProtocolLacpPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 4, 1, 4),
    _FsMIVlanTunnelProtocolLacpPktsSent_Type()
)
fsMIVlanTunnelProtocolLacpPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanTunnelProtocolLacpPktsSent.setStatus("current")
_FsMIVlanTunnelProtocolStpPDUsRecvd_Type = Counter32
_FsMIVlanTunnelProtocolStpPDUsRecvd_Object = MibTableColumn
fsMIVlanTunnelProtocolStpPDUsRecvd = _FsMIVlanTunnelProtocolStpPDUsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 4, 1, 5),
    _FsMIVlanTunnelProtocolStpPDUsRecvd_Type()
)
fsMIVlanTunnelProtocolStpPDUsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanTunnelProtocolStpPDUsRecvd.setStatus("current")
_FsMIVlanTunnelProtocolStpPDUsSent_Type = Counter32
_FsMIVlanTunnelProtocolStpPDUsSent_Object = MibTableColumn
fsMIVlanTunnelProtocolStpPDUsSent = _FsMIVlanTunnelProtocolStpPDUsSent_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 4, 1, 6),
    _FsMIVlanTunnelProtocolStpPDUsSent_Type()
)
fsMIVlanTunnelProtocolStpPDUsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanTunnelProtocolStpPDUsSent.setStatus("current")
_FsMIVlanTunnelProtocolGvrpPDUsRecvd_Type = Counter32
_FsMIVlanTunnelProtocolGvrpPDUsRecvd_Object = MibTableColumn
fsMIVlanTunnelProtocolGvrpPDUsRecvd = _FsMIVlanTunnelProtocolGvrpPDUsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 4, 1, 7),
    _FsMIVlanTunnelProtocolGvrpPDUsRecvd_Type()
)
fsMIVlanTunnelProtocolGvrpPDUsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanTunnelProtocolGvrpPDUsRecvd.setStatus("current")
_FsMIVlanTunnelProtocolGvrpPDUsSent_Type = Counter32
_FsMIVlanTunnelProtocolGvrpPDUsSent_Object = MibTableColumn
fsMIVlanTunnelProtocolGvrpPDUsSent = _FsMIVlanTunnelProtocolGvrpPDUsSent_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 4, 1, 8),
    _FsMIVlanTunnelProtocolGvrpPDUsSent_Type()
)
fsMIVlanTunnelProtocolGvrpPDUsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanTunnelProtocolGvrpPDUsSent.setStatus("current")
_FsMIVlanTunnelProtocolGmrpPktsRecvd_Type = Counter32
_FsMIVlanTunnelProtocolGmrpPktsRecvd_Object = MibTableColumn
fsMIVlanTunnelProtocolGmrpPktsRecvd = _FsMIVlanTunnelProtocolGmrpPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 4, 1, 9),
    _FsMIVlanTunnelProtocolGmrpPktsRecvd_Type()
)
fsMIVlanTunnelProtocolGmrpPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanTunnelProtocolGmrpPktsRecvd.setStatus("current")
_FsMIVlanTunnelProtocolGmrpPktsSent_Type = Counter32
_FsMIVlanTunnelProtocolGmrpPktsSent_Object = MibTableColumn
fsMIVlanTunnelProtocolGmrpPktsSent = _FsMIVlanTunnelProtocolGmrpPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 4, 1, 10),
    _FsMIVlanTunnelProtocolGmrpPktsSent_Type()
)
fsMIVlanTunnelProtocolGmrpPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanTunnelProtocolGmrpPktsSent.setStatus("current")
_FsMIVlanTunnelProtocolIgmpPktsRecvd_Type = Counter32
_FsMIVlanTunnelProtocolIgmpPktsRecvd_Object = MibTableColumn
fsMIVlanTunnelProtocolIgmpPktsRecvd = _FsMIVlanTunnelProtocolIgmpPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 4, 1, 11),
    _FsMIVlanTunnelProtocolIgmpPktsRecvd_Type()
)
fsMIVlanTunnelProtocolIgmpPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanTunnelProtocolIgmpPktsRecvd.setStatus("current")
_FsMIVlanTunnelProtocolIgmpPktsSent_Type = Counter32
_FsMIVlanTunnelProtocolIgmpPktsSent_Object = MibTableColumn
fsMIVlanTunnelProtocolIgmpPktsSent = _FsMIVlanTunnelProtocolIgmpPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 4, 1, 12),
    _FsMIVlanTunnelProtocolIgmpPktsSent_Type()
)
fsMIVlanTunnelProtocolIgmpPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanTunnelProtocolIgmpPktsSent.setStatus("current")
_FsMIVlanTunnelProtocolMvrpPktsRecvd_Type = Counter32
_FsMIVlanTunnelProtocolMvrpPktsRecvd_Object = MibTableColumn
fsMIVlanTunnelProtocolMvrpPktsRecvd = _FsMIVlanTunnelProtocolMvrpPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 4, 1, 13),
    _FsMIVlanTunnelProtocolMvrpPktsRecvd_Type()
)
fsMIVlanTunnelProtocolMvrpPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanTunnelProtocolMvrpPktsRecvd.setStatus("current")
_FsMIVlanTunnelProtocolMvrpPktsSent_Type = Counter32
_FsMIVlanTunnelProtocolMvrpPktsSent_Object = MibTableColumn
fsMIVlanTunnelProtocolMvrpPktsSent = _FsMIVlanTunnelProtocolMvrpPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 4, 1, 14),
    _FsMIVlanTunnelProtocolMvrpPktsSent_Type()
)
fsMIVlanTunnelProtocolMvrpPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanTunnelProtocolMvrpPktsSent.setStatus("current")
_FsMIVlanTunnelProtocolMmrpPktsRecvd_Type = Counter32
_FsMIVlanTunnelProtocolMmrpPktsRecvd_Object = MibTableColumn
fsMIVlanTunnelProtocolMmrpPktsRecvd = _FsMIVlanTunnelProtocolMmrpPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 4, 1, 15),
    _FsMIVlanTunnelProtocolMmrpPktsRecvd_Type()
)
fsMIVlanTunnelProtocolMmrpPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanTunnelProtocolMmrpPktsRecvd.setStatus("current")
_FsMIVlanTunnelProtocolMmrpPktsSent_Type = Counter32
_FsMIVlanTunnelProtocolMmrpPktsSent_Object = MibTableColumn
fsMIVlanTunnelProtocolMmrpPktsSent = _FsMIVlanTunnelProtocolMmrpPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 4, 1, 16),
    _FsMIVlanTunnelProtocolMmrpPktsSent_Type()
)
fsMIVlanTunnelProtocolMmrpPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanTunnelProtocolMmrpPktsSent.setStatus("current")
_FsMIVlanTunnelProtocolElmiPktsRecvd_Type = Counter32
_FsMIVlanTunnelProtocolElmiPktsRecvd_Object = MibTableColumn
fsMIVlanTunnelProtocolElmiPktsRecvd = _FsMIVlanTunnelProtocolElmiPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 4, 1, 17),
    _FsMIVlanTunnelProtocolElmiPktsRecvd_Type()
)
fsMIVlanTunnelProtocolElmiPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanTunnelProtocolElmiPktsRecvd.setStatus("current")
_FsMIVlanTunnelProtocolElmiPktsSent_Type = Counter32
_FsMIVlanTunnelProtocolElmiPktsSent_Object = MibTableColumn
fsMIVlanTunnelProtocolElmiPktsSent = _FsMIVlanTunnelProtocolElmiPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 4, 1, 18),
    _FsMIVlanTunnelProtocolElmiPktsSent_Type()
)
fsMIVlanTunnelProtocolElmiPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanTunnelProtocolElmiPktsSent.setStatus("current")
_FsMIVlanTunnelProtocolLldpPktsRecvd_Type = Counter32
_FsMIVlanTunnelProtocolLldpPktsRecvd_Object = MibTableColumn
fsMIVlanTunnelProtocolLldpPktsRecvd = _FsMIVlanTunnelProtocolLldpPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 4, 1, 19),
    _FsMIVlanTunnelProtocolLldpPktsRecvd_Type()
)
fsMIVlanTunnelProtocolLldpPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanTunnelProtocolLldpPktsRecvd.setStatus("current")
_FsMIVlanTunnelProtocolLldpPktsSent_Type = Counter32
_FsMIVlanTunnelProtocolLldpPktsSent_Object = MibTableColumn
fsMIVlanTunnelProtocolLldpPktsSent = _FsMIVlanTunnelProtocolLldpPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 4, 1, 20),
    _FsMIVlanTunnelProtocolLldpPktsSent_Type()
)
fsMIVlanTunnelProtocolLldpPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanTunnelProtocolLldpPktsSent.setStatus("current")
_FsMIVlanTunnelProtocolEcfmPktsRecvd_Type = Counter32
_FsMIVlanTunnelProtocolEcfmPktsRecvd_Object = MibTableColumn
fsMIVlanTunnelProtocolEcfmPktsRecvd = _FsMIVlanTunnelProtocolEcfmPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 4, 1, 21),
    _FsMIVlanTunnelProtocolEcfmPktsRecvd_Type()
)
fsMIVlanTunnelProtocolEcfmPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanTunnelProtocolEcfmPktsRecvd.setStatus("current")
_FsMIVlanTunnelProtocolEcfmPktsSent_Type = Counter32
_FsMIVlanTunnelProtocolEcfmPktsSent_Object = MibTableColumn
fsMIVlanTunnelProtocolEcfmPktsSent = _FsMIVlanTunnelProtocolEcfmPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 4, 1, 22),
    _FsMIVlanTunnelProtocolEcfmPktsSent_Type()
)
fsMIVlanTunnelProtocolEcfmPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanTunnelProtocolEcfmPktsSent.setStatus("current")
_FsMIVlanTunnelProtocolEoamPktsRecvd_Type = Counter32
_FsMIVlanTunnelProtocolEoamPktsRecvd_Object = MibTableColumn
fsMIVlanTunnelProtocolEoamPktsRecvd = _FsMIVlanTunnelProtocolEoamPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 4, 1, 23),
    _FsMIVlanTunnelProtocolEoamPktsRecvd_Type()
)
fsMIVlanTunnelProtocolEoamPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanTunnelProtocolEoamPktsRecvd.setStatus("current")
_FsMIVlanTunnelProtocolEoamPktsSent_Type = Counter32
_FsMIVlanTunnelProtocolEoamPktsSent_Object = MibTableColumn
fsMIVlanTunnelProtocolEoamPktsSent = _FsMIVlanTunnelProtocolEoamPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 4, 1, 24),
    _FsMIVlanTunnelProtocolEoamPktsSent_Type()
)
fsMIVlanTunnelProtocolEoamPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanTunnelProtocolEoamPktsSent.setStatus("current")
_FsMIServiceVlanTunnelProtocolTable_Object = MibTable
fsMIServiceVlanTunnelProtocolTable = _FsMIServiceVlanTunnelProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 5)
)
if mibBuilder.loadTexts:
    fsMIServiceVlanTunnelProtocolTable.setStatus("current")
_FsMIServiceVlanTunnelProtocolEntry_Object = MibTableRow
fsMIServiceVlanTunnelProtocolEntry = _FsMIServiceVlanTunnelProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 5, 1)
)
fsMIServiceVlanTunnelProtocolEntry.setIndexNames(
    (0, "ARICENT-MIVLAN-EXT-MIB", "fsMIVlanContextId"),
    (0, "ARICENT-MIVLAN-EXT-MIB", "fsMIServiceVlanId"),
    (0, "ARICENT-MIVLAN-EXT-MIB", "fsMIServiceProtocolEnum"),
)
if mibBuilder.loadTexts:
    fsMIServiceVlanTunnelProtocolEntry.setStatus("current")
_FsMIServiceVlanId_Type = VlanId
_FsMIServiceVlanId_Object = MibTableColumn
fsMIServiceVlanId = _FsMIServiceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 5, 1, 1),
    _FsMIServiceVlanId_Type()
)
fsMIServiceVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIServiceVlanId.setStatus("current")
_FsMIServiceProtocolEnum_Type = L2CPProtocols
_FsMIServiceProtocolEnum_Object = MibTableColumn
fsMIServiceProtocolEnum = _FsMIServiceProtocolEnum_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 5, 1, 2),
    _FsMIServiceProtocolEnum_Type()
)
fsMIServiceProtocolEnum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIServiceProtocolEnum.setStatus("current")
_FsMIServiceVlanRsvdMacaddress_Type = MacAddress
_FsMIServiceVlanRsvdMacaddress_Object = MibTableColumn
fsMIServiceVlanRsvdMacaddress = _FsMIServiceVlanRsvdMacaddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 5, 1, 3),
    _FsMIServiceVlanRsvdMacaddress_Type()
)
fsMIServiceVlanRsvdMacaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIServiceVlanRsvdMacaddress.setStatus("current")
_FsMIServiceVlanTunnelMacaddress_Type = MacAddress
_FsMIServiceVlanTunnelMacaddress_Object = MibTableColumn
fsMIServiceVlanTunnelMacaddress = _FsMIServiceVlanTunnelMacaddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 5, 1, 4),
    _FsMIServiceVlanTunnelMacaddress_Type()
)
fsMIServiceVlanTunnelMacaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIServiceVlanTunnelMacaddress.setStatus("current")
_FsMIServiceVlanTunnelProtocolStatus_Type = TunnelStatus
_FsMIServiceVlanTunnelProtocolStatus_Object = MibTableColumn
fsMIServiceVlanTunnelProtocolStatus = _FsMIServiceVlanTunnelProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 5, 1, 5),
    _FsMIServiceVlanTunnelProtocolStatus_Type()
)
fsMIServiceVlanTunnelProtocolStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIServiceVlanTunnelProtocolStatus.setStatus("current")
_FsMIServiceVlanTunnelPktsRecvd_Type = Counter32
_FsMIServiceVlanTunnelPktsRecvd_Object = MibTableColumn
fsMIServiceVlanTunnelPktsRecvd = _FsMIServiceVlanTunnelPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 5, 1, 6),
    _FsMIServiceVlanTunnelPktsRecvd_Type()
)
fsMIServiceVlanTunnelPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIServiceVlanTunnelPktsRecvd.setStatus("current")
_FsMIServiceVlanTunnelPktsSent_Type = Counter32
_FsMIServiceVlanTunnelPktsSent_Object = MibTableColumn
fsMIServiceVlanTunnelPktsSent = _FsMIServiceVlanTunnelPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 5, 1, 7),
    _FsMIServiceVlanTunnelPktsSent_Type()
)
fsMIServiceVlanTunnelPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIServiceVlanTunnelPktsSent.setStatus("current")
_FsMIServiceVlanDiscardPktsRx_Type = Counter32
_FsMIServiceVlanDiscardPktsRx_Object = MibTableColumn
fsMIServiceVlanDiscardPktsRx = _FsMIServiceVlanDiscardPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 5, 1, 8),
    _FsMIServiceVlanDiscardPktsRx_Type()
)
fsMIServiceVlanDiscardPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIServiceVlanDiscardPktsRx.setStatus("current")
_FsMIServiceVlanDiscardPktsTx_Type = Counter32
_FsMIServiceVlanDiscardPktsTx_Object = MibTableColumn
fsMIServiceVlanDiscardPktsTx = _FsMIServiceVlanDiscardPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 2, 5, 1, 9),
    _FsMIServiceVlanDiscardPktsTx_Type()
)
fsMIServiceVlanDiscardPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIServiceVlanDiscardPktsTx.setStatus("current")
_FsMIVlanDiscardObjects_ObjectIdentity = ObjectIdentity
fsMIVlanDiscardObjects = _FsMIVlanDiscardObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 138, 3)
)
_FsMIVlanDiscardStatsTable_Object = MibTable
fsMIVlanDiscardStatsTable = _FsMIVlanDiscardStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 3, 1)
)
if mibBuilder.loadTexts:
    fsMIVlanDiscardStatsTable.setStatus("current")
_FsMIVlanDiscardStatsEntry_Object = MibTableRow
fsMIVlanDiscardStatsEntry = _FsMIVlanDiscardStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 3, 1, 1)
)
fsMIVlanDiscardStatsEntry.setIndexNames(
    (0, "ARICENT-MIVLAN-EXT-MIB", "fsMIVlanPort"),
)
if mibBuilder.loadTexts:
    fsMIVlanDiscardStatsEntry.setStatus("current")
_FsMIVlanDiscardDot1xPktsRx_Type = Counter32
_FsMIVlanDiscardDot1xPktsRx_Object = MibTableColumn
fsMIVlanDiscardDot1xPktsRx = _FsMIVlanDiscardDot1xPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 3, 1, 1, 1),
    _FsMIVlanDiscardDot1xPktsRx_Type()
)
fsMIVlanDiscardDot1xPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanDiscardDot1xPktsRx.setStatus("current")
_FsMIVlanDiscardDot1xPktsTx_Type = Counter32
_FsMIVlanDiscardDot1xPktsTx_Object = MibTableColumn
fsMIVlanDiscardDot1xPktsTx = _FsMIVlanDiscardDot1xPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 3, 1, 1, 2),
    _FsMIVlanDiscardDot1xPktsTx_Type()
)
fsMIVlanDiscardDot1xPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanDiscardDot1xPktsTx.setStatus("current")
_FsMIVlanDiscardLacpPktsRx_Type = Counter32
_FsMIVlanDiscardLacpPktsRx_Object = MibTableColumn
fsMIVlanDiscardLacpPktsRx = _FsMIVlanDiscardLacpPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 3, 1, 1, 3),
    _FsMIVlanDiscardLacpPktsRx_Type()
)
fsMIVlanDiscardLacpPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanDiscardLacpPktsRx.setStatus("current")
_FsMIVlanDiscardLacpPktsTx_Type = Counter32
_FsMIVlanDiscardLacpPktsTx_Object = MibTableColumn
fsMIVlanDiscardLacpPktsTx = _FsMIVlanDiscardLacpPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 3, 1, 1, 4),
    _FsMIVlanDiscardLacpPktsTx_Type()
)
fsMIVlanDiscardLacpPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanDiscardLacpPktsTx.setStatus("current")
_FsMIVlanDiscardStpPDUsRx_Type = Counter32
_FsMIVlanDiscardStpPDUsRx_Object = MibTableColumn
fsMIVlanDiscardStpPDUsRx = _FsMIVlanDiscardStpPDUsRx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 3, 1, 1, 5),
    _FsMIVlanDiscardStpPDUsRx_Type()
)
fsMIVlanDiscardStpPDUsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanDiscardStpPDUsRx.setStatus("current")
_FsMIVlanDiscardStpPDUsTx_Type = Counter32
_FsMIVlanDiscardStpPDUsTx_Object = MibTableColumn
fsMIVlanDiscardStpPDUsTx = _FsMIVlanDiscardStpPDUsTx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 3, 1, 1, 6),
    _FsMIVlanDiscardStpPDUsTx_Type()
)
fsMIVlanDiscardStpPDUsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanDiscardStpPDUsTx.setStatus("current")
_FsMIVlanDiscardGvrpPktsRx_Type = Counter32
_FsMIVlanDiscardGvrpPktsRx_Object = MibTableColumn
fsMIVlanDiscardGvrpPktsRx = _FsMIVlanDiscardGvrpPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 3, 1, 1, 7),
    _FsMIVlanDiscardGvrpPktsRx_Type()
)
fsMIVlanDiscardGvrpPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanDiscardGvrpPktsRx.setStatus("current")
_FsMIVlanDiscardGvrpPktsTx_Type = Counter32
_FsMIVlanDiscardGvrpPktsTx_Object = MibTableColumn
fsMIVlanDiscardGvrpPktsTx = _FsMIVlanDiscardGvrpPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 3, 1, 1, 8),
    _FsMIVlanDiscardGvrpPktsTx_Type()
)
fsMIVlanDiscardGvrpPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanDiscardGvrpPktsTx.setStatus("current")
_FsMIVlanDiscardGmrpPktsRx_Type = Counter32
_FsMIVlanDiscardGmrpPktsRx_Object = MibTableColumn
fsMIVlanDiscardGmrpPktsRx = _FsMIVlanDiscardGmrpPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 3, 1, 1, 9),
    _FsMIVlanDiscardGmrpPktsRx_Type()
)
fsMIVlanDiscardGmrpPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanDiscardGmrpPktsRx.setStatus("current")
_FsMIVlanDiscardGmrpPktsTx_Type = Counter32
_FsMIVlanDiscardGmrpPktsTx_Object = MibTableColumn
fsMIVlanDiscardGmrpPktsTx = _FsMIVlanDiscardGmrpPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 3, 1, 1, 10),
    _FsMIVlanDiscardGmrpPktsTx_Type()
)
fsMIVlanDiscardGmrpPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanDiscardGmrpPktsTx.setStatus("current")
_FsMIVlanDiscardIgmpPktsRx_Type = Counter32
_FsMIVlanDiscardIgmpPktsRx_Object = MibTableColumn
fsMIVlanDiscardIgmpPktsRx = _FsMIVlanDiscardIgmpPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 3, 1, 1, 11),
    _FsMIVlanDiscardIgmpPktsRx_Type()
)
fsMIVlanDiscardIgmpPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanDiscardIgmpPktsRx.setStatus("current")
_FsMIVlanDiscardIgmpPktsTx_Type = Counter32
_FsMIVlanDiscardIgmpPktsTx_Object = MibTableColumn
fsMIVlanDiscardIgmpPktsTx = _FsMIVlanDiscardIgmpPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 3, 1, 1, 12),
    _FsMIVlanDiscardIgmpPktsTx_Type()
)
fsMIVlanDiscardIgmpPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanDiscardIgmpPktsTx.setStatus("current")
_FsMIVlanDiscardMvrpPktsRx_Type = Counter32
_FsMIVlanDiscardMvrpPktsRx_Object = MibTableColumn
fsMIVlanDiscardMvrpPktsRx = _FsMIVlanDiscardMvrpPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 3, 1, 1, 13),
    _FsMIVlanDiscardMvrpPktsRx_Type()
)
fsMIVlanDiscardMvrpPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanDiscardMvrpPktsRx.setStatus("current")
_FsMIVlanDiscardMvrpPktsTx_Type = Counter32
_FsMIVlanDiscardMvrpPktsTx_Object = MibTableColumn
fsMIVlanDiscardMvrpPktsTx = _FsMIVlanDiscardMvrpPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 3, 1, 1, 14),
    _FsMIVlanDiscardMvrpPktsTx_Type()
)
fsMIVlanDiscardMvrpPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanDiscardMvrpPktsTx.setStatus("current")
_FsMIVlanDiscardMmrpPktsRx_Type = Counter32
_FsMIVlanDiscardMmrpPktsRx_Object = MibTableColumn
fsMIVlanDiscardMmrpPktsRx = _FsMIVlanDiscardMmrpPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 3, 1, 1, 15),
    _FsMIVlanDiscardMmrpPktsRx_Type()
)
fsMIVlanDiscardMmrpPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanDiscardMmrpPktsRx.setStatus("current")
_FsMIVlanDiscardMmrpPktsTx_Type = Counter32
_FsMIVlanDiscardMmrpPktsTx_Object = MibTableColumn
fsMIVlanDiscardMmrpPktsTx = _FsMIVlanDiscardMmrpPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 3, 1, 1, 16),
    _FsMIVlanDiscardMmrpPktsTx_Type()
)
fsMIVlanDiscardMmrpPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanDiscardMmrpPktsTx.setStatus("current")
_FsMIVlanDiscardElmiPktsRx_Type = Counter32
_FsMIVlanDiscardElmiPktsRx_Object = MibTableColumn
fsMIVlanDiscardElmiPktsRx = _FsMIVlanDiscardElmiPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 3, 1, 1, 17),
    _FsMIVlanDiscardElmiPktsRx_Type()
)
fsMIVlanDiscardElmiPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanDiscardElmiPktsRx.setStatus("current")
_FsMIVlanDiscardElmiPktsTx_Type = Counter32
_FsMIVlanDiscardElmiPktsTx_Object = MibTableColumn
fsMIVlanDiscardElmiPktsTx = _FsMIVlanDiscardElmiPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 3, 1, 1, 18),
    _FsMIVlanDiscardElmiPktsTx_Type()
)
fsMIVlanDiscardElmiPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanDiscardElmiPktsTx.setStatus("current")
_FsMIVlanDiscardLldpPktsRx_Type = Counter32
_FsMIVlanDiscardLldpPktsRx_Object = MibTableColumn
fsMIVlanDiscardLldpPktsRx = _FsMIVlanDiscardLldpPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 3, 1, 1, 19),
    _FsMIVlanDiscardLldpPktsRx_Type()
)
fsMIVlanDiscardLldpPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanDiscardLldpPktsRx.setStatus("current")
_FsMIVlanDiscardLldpPktsTx_Type = Counter32
_FsMIVlanDiscardLldpPktsTx_Object = MibTableColumn
fsMIVlanDiscardLldpPktsTx = _FsMIVlanDiscardLldpPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 3, 1, 1, 20),
    _FsMIVlanDiscardLldpPktsTx_Type()
)
fsMIVlanDiscardLldpPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanDiscardLldpPktsTx.setStatus("current")
_FsMIVlanDiscardEcfmPktsRx_Type = Counter32
_FsMIVlanDiscardEcfmPktsRx_Object = MibTableColumn
fsMIVlanDiscardEcfmPktsRx = _FsMIVlanDiscardEcfmPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 3, 1, 1, 21),
    _FsMIVlanDiscardEcfmPktsRx_Type()
)
fsMIVlanDiscardEcfmPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanDiscardEcfmPktsRx.setStatus("current")
_FsMIVlanDiscardEcfmPktsTx_Type = Counter32
_FsMIVlanDiscardEcfmPktsTx_Object = MibTableColumn
fsMIVlanDiscardEcfmPktsTx = _FsMIVlanDiscardEcfmPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 3, 1, 1, 22),
    _FsMIVlanDiscardEcfmPktsTx_Type()
)
fsMIVlanDiscardEcfmPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanDiscardEcfmPktsTx.setStatus("current")
_FsMIVlanDiscardEoamPktsRx_Type = Counter32
_FsMIVlanDiscardEoamPktsRx_Object = MibTableColumn
fsMIVlanDiscardEoamPktsRx = _FsMIVlanDiscardEoamPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 3, 1, 1, 23),
    _FsMIVlanDiscardEoamPktsRx_Type()
)
fsMIVlanDiscardEoamPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanDiscardEoamPktsRx.setStatus("current")
_FsMIVlanDiscardEoamPktsTx_Type = Counter32
_FsMIVlanDiscardEoamPktsTx_Object = MibTableColumn
fsMIVlanDiscardEoamPktsTx = _FsMIVlanDiscardEoamPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 138, 3, 1, 1, 24),
    _FsMIVlanDiscardEoamPktsTx_Type()
)
fsMIVlanDiscardEoamPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIVlanDiscardEoamPktsTx.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-MIVLAN-EXT-MIB",
    **{"TunnelStatus": TunnelStatus,
       "L2CPProtocols": L2CPProtocols,
       "futureMIVlanExtMIB": futureMIVlanExtMIB,
       "fsMIVlanSystemConfig": fsMIVlanSystemConfig,
       "fsMIVlanBridgeInfoTable": fsMIVlanBridgeInfoTable,
       "fsMIVlanBridgeInfoEntry": fsMIVlanBridgeInfoEntry,
       "fsMIVlanContextId": fsMIVlanContextId,
       "fsMIVlanBridgeMode": fsMIVlanBridgeMode,
       "fsMIVlanTunnelObjects": fsMIVlanTunnelObjects,
       "fsMIVlanTunnelContextInfoTable": fsMIVlanTunnelContextInfoTable,
       "fsMIVlanTunnelContextInfoEntry": fsMIVlanTunnelContextInfoEntry,
       "fsMIVlanTunnelBpduPri": fsMIVlanTunnelBpduPri,
       "fsMIVlanTunnelStpAddress": fsMIVlanTunnelStpAddress,
       "fsMIVlanTunnelLacpAddress": fsMIVlanTunnelLacpAddress,
       "fsMIVlanTunnelDot1xAddress": fsMIVlanTunnelDot1xAddress,
       "fsMIVlanTunnelGvrpAddress": fsMIVlanTunnelGvrpAddress,
       "fsMIVlanTunnelGmrpAddress": fsMIVlanTunnelGmrpAddress,
       "fsMIVlanTunnelMvrpAddress": fsMIVlanTunnelMvrpAddress,
       "fsMIVlanTunnelMmrpAddress": fsMIVlanTunnelMmrpAddress,
       "fsMIVlanTunnelElmiAddress": fsMIVlanTunnelElmiAddress,
       "fsMIVlanTunnelLldpAddress": fsMIVlanTunnelLldpAddress,
       "fsMIVlanTunnelEcfmAddress": fsMIVlanTunnelEcfmAddress,
       "fsMIVlanTunnelEoamAddress": fsMIVlanTunnelEoamAddress,
       "fsMIVlanTunnelIgmpAddress": fsMIVlanTunnelIgmpAddress,
       "fsMIVlanTunnelTable": fsMIVlanTunnelTable,
       "fsMIVlanTunnelEntry": fsMIVlanTunnelEntry,
       "fsMIVlanPort": fsMIVlanPort,
       "fsMIVlanTunnelStatus": fsMIVlanTunnelStatus,
       "fsMIVlanTunnelProtocolTable": fsMIVlanTunnelProtocolTable,
       "fsMIVlanTunnelProtocolEntry": fsMIVlanTunnelProtocolEntry,
       "fsMIVlanTunnelProtocolDot1x": fsMIVlanTunnelProtocolDot1x,
       "fsMIVlanTunnelProtocolLacp": fsMIVlanTunnelProtocolLacp,
       "fsMIVlanTunnelProtocolStp": fsMIVlanTunnelProtocolStp,
       "fsMIVlanTunnelProtocolGvrp": fsMIVlanTunnelProtocolGvrp,
       "fsMIVlanTunnelProtocolGmrp": fsMIVlanTunnelProtocolGmrp,
       "fsMIVlanTunnelProtocolIgmp": fsMIVlanTunnelProtocolIgmp,
       "fsMIVlanTunnelProtocolMvrp": fsMIVlanTunnelProtocolMvrp,
       "fsMIVlanTunnelProtocolMmrp": fsMIVlanTunnelProtocolMmrp,
       "fsMIVlanTunnelProtocolElmi": fsMIVlanTunnelProtocolElmi,
       "fsMIVlanTunnelProtocolLldp": fsMIVlanTunnelProtocolLldp,
       "fsMIVlanTunnelProtocolEcfm": fsMIVlanTunnelProtocolEcfm,
       "fsMIVlanTunnelOverrideOption": fsMIVlanTunnelOverrideOption,
       "fsMIVlanTunnelProtocolEoam": fsMIVlanTunnelProtocolEoam,
       "fsMIVlanTunnelProtocolStatsTable": fsMIVlanTunnelProtocolStatsTable,
       "fsMIVlanTunnelProtocolStatsEntry": fsMIVlanTunnelProtocolStatsEntry,
       "fsMIVlanTunnelProtocolDot1xPktsRecvd": fsMIVlanTunnelProtocolDot1xPktsRecvd,
       "fsMIVlanTunnelProtocolDot1xPktsSent": fsMIVlanTunnelProtocolDot1xPktsSent,
       "fsMIVlanTunnelProtocolLacpPktsRecvd": fsMIVlanTunnelProtocolLacpPktsRecvd,
       "fsMIVlanTunnelProtocolLacpPktsSent": fsMIVlanTunnelProtocolLacpPktsSent,
       "fsMIVlanTunnelProtocolStpPDUsRecvd": fsMIVlanTunnelProtocolStpPDUsRecvd,
       "fsMIVlanTunnelProtocolStpPDUsSent": fsMIVlanTunnelProtocolStpPDUsSent,
       "fsMIVlanTunnelProtocolGvrpPDUsRecvd": fsMIVlanTunnelProtocolGvrpPDUsRecvd,
       "fsMIVlanTunnelProtocolGvrpPDUsSent": fsMIVlanTunnelProtocolGvrpPDUsSent,
       "fsMIVlanTunnelProtocolGmrpPktsRecvd": fsMIVlanTunnelProtocolGmrpPktsRecvd,
       "fsMIVlanTunnelProtocolGmrpPktsSent": fsMIVlanTunnelProtocolGmrpPktsSent,
       "fsMIVlanTunnelProtocolIgmpPktsRecvd": fsMIVlanTunnelProtocolIgmpPktsRecvd,
       "fsMIVlanTunnelProtocolIgmpPktsSent": fsMIVlanTunnelProtocolIgmpPktsSent,
       "fsMIVlanTunnelProtocolMvrpPktsRecvd": fsMIVlanTunnelProtocolMvrpPktsRecvd,
       "fsMIVlanTunnelProtocolMvrpPktsSent": fsMIVlanTunnelProtocolMvrpPktsSent,
       "fsMIVlanTunnelProtocolMmrpPktsRecvd": fsMIVlanTunnelProtocolMmrpPktsRecvd,
       "fsMIVlanTunnelProtocolMmrpPktsSent": fsMIVlanTunnelProtocolMmrpPktsSent,
       "fsMIVlanTunnelProtocolElmiPktsRecvd": fsMIVlanTunnelProtocolElmiPktsRecvd,
       "fsMIVlanTunnelProtocolElmiPktsSent": fsMIVlanTunnelProtocolElmiPktsSent,
       "fsMIVlanTunnelProtocolLldpPktsRecvd": fsMIVlanTunnelProtocolLldpPktsRecvd,
       "fsMIVlanTunnelProtocolLldpPktsSent": fsMIVlanTunnelProtocolLldpPktsSent,
       "fsMIVlanTunnelProtocolEcfmPktsRecvd": fsMIVlanTunnelProtocolEcfmPktsRecvd,
       "fsMIVlanTunnelProtocolEcfmPktsSent": fsMIVlanTunnelProtocolEcfmPktsSent,
       "fsMIVlanTunnelProtocolEoamPktsRecvd": fsMIVlanTunnelProtocolEoamPktsRecvd,
       "fsMIVlanTunnelProtocolEoamPktsSent": fsMIVlanTunnelProtocolEoamPktsSent,
       "fsMIServiceVlanTunnelProtocolTable": fsMIServiceVlanTunnelProtocolTable,
       "fsMIServiceVlanTunnelProtocolEntry": fsMIServiceVlanTunnelProtocolEntry,
       "fsMIServiceVlanId": fsMIServiceVlanId,
       "fsMIServiceProtocolEnum": fsMIServiceProtocolEnum,
       "fsMIServiceVlanRsvdMacaddress": fsMIServiceVlanRsvdMacaddress,
       "fsMIServiceVlanTunnelMacaddress": fsMIServiceVlanTunnelMacaddress,
       "fsMIServiceVlanTunnelProtocolStatus": fsMIServiceVlanTunnelProtocolStatus,
       "fsMIServiceVlanTunnelPktsRecvd": fsMIServiceVlanTunnelPktsRecvd,
       "fsMIServiceVlanTunnelPktsSent": fsMIServiceVlanTunnelPktsSent,
       "fsMIServiceVlanDiscardPktsRx": fsMIServiceVlanDiscardPktsRx,
       "fsMIServiceVlanDiscardPktsTx": fsMIServiceVlanDiscardPktsTx,
       "fsMIVlanDiscardObjects": fsMIVlanDiscardObjects,
       "fsMIVlanDiscardStatsTable": fsMIVlanDiscardStatsTable,
       "fsMIVlanDiscardStatsEntry": fsMIVlanDiscardStatsEntry,
       "fsMIVlanDiscardDot1xPktsRx": fsMIVlanDiscardDot1xPktsRx,
       "fsMIVlanDiscardDot1xPktsTx": fsMIVlanDiscardDot1xPktsTx,
       "fsMIVlanDiscardLacpPktsRx": fsMIVlanDiscardLacpPktsRx,
       "fsMIVlanDiscardLacpPktsTx": fsMIVlanDiscardLacpPktsTx,
       "fsMIVlanDiscardStpPDUsRx": fsMIVlanDiscardStpPDUsRx,
       "fsMIVlanDiscardStpPDUsTx": fsMIVlanDiscardStpPDUsTx,
       "fsMIVlanDiscardGvrpPktsRx": fsMIVlanDiscardGvrpPktsRx,
       "fsMIVlanDiscardGvrpPktsTx": fsMIVlanDiscardGvrpPktsTx,
       "fsMIVlanDiscardGmrpPktsRx": fsMIVlanDiscardGmrpPktsRx,
       "fsMIVlanDiscardGmrpPktsTx": fsMIVlanDiscardGmrpPktsTx,
       "fsMIVlanDiscardIgmpPktsRx": fsMIVlanDiscardIgmpPktsRx,
       "fsMIVlanDiscardIgmpPktsTx": fsMIVlanDiscardIgmpPktsTx,
       "fsMIVlanDiscardMvrpPktsRx": fsMIVlanDiscardMvrpPktsRx,
       "fsMIVlanDiscardMvrpPktsTx": fsMIVlanDiscardMvrpPktsTx,
       "fsMIVlanDiscardMmrpPktsRx": fsMIVlanDiscardMmrpPktsRx,
       "fsMIVlanDiscardMmrpPktsTx": fsMIVlanDiscardMmrpPktsTx,
       "fsMIVlanDiscardElmiPktsRx": fsMIVlanDiscardElmiPktsRx,
       "fsMIVlanDiscardElmiPktsTx": fsMIVlanDiscardElmiPktsTx,
       "fsMIVlanDiscardLldpPktsRx": fsMIVlanDiscardLldpPktsRx,
       "fsMIVlanDiscardLldpPktsTx": fsMIVlanDiscardLldpPktsTx,
       "fsMIVlanDiscardEcfmPktsRx": fsMIVlanDiscardEcfmPktsRx,
       "fsMIVlanDiscardEcfmPktsTx": fsMIVlanDiscardEcfmPktsTx,
       "fsMIVlanDiscardEoamPktsRx": fsMIVlanDiscardEoamPktsRx,
       "fsMIVlanDiscardEoamPktsTx": fsMIVlanDiscardEoamPktsTx}
)
