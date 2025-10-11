# SNMP MIB module (ARICENT-MIPROVIDERBRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-MIPROVIDERBRIDGE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:42:27 2025
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

(dot1adMIPepEntry,) = mibBuilder.importSymbols(
    "ARICENT-MIDOT1AD-MIB",
    "dot1adMIPepEntry")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(VlanId,
 dot1qVlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId",
    "dot1qVlanIndex")

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

futureMIProviderBridgeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 127)
)
if mibBuilder.loadTexts:
    futureMIProviderBridgeMIB.setRevisions(
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



# MIB Managed Objects in the order of their OIDs

_FsMIPbSystem_ObjectIdentity = ObjectIdentity
fsMIPbSystem = _FsMIPbSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 127, 1)
)
_FsMIPbContextInfoTable_Object = MibTable
fsMIPbContextInfoTable = _FsMIPbContextInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 1, 1)
)
if mibBuilder.loadTexts:
    fsMIPbContextInfoTable.setStatus("current")
_FsMIPbContextInfoEntry_Object = MibTableRow
fsMIPbContextInfoEntry = _FsMIPbContextInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 1, 1, 1)
)
fsMIPbContextInfoEntry.setIndexNames(
    (0, "ARICENT-MIPROVIDERBRIDGE-MIB", "fsMIPbContextId"),
)
if mibBuilder.loadTexts:
    fsMIPbContextInfoEntry.setStatus("current")


class _FsMIPbContextId_Type(Integer32):
    """Custom type fsMIPbContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIPbContextId_Type.__name__ = "Integer32"
_FsMIPbContextId_Object = MibTableColumn
fsMIPbContextId = _FsMIPbContextId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 1, 1, 1, 1),
    _FsMIPbContextId_Type()
)
fsMIPbContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIPbContextId.setStatus("current")


class _FsMIPbMulticastMacLimit_Type(Unsigned32):
    """Custom type fsMIPbMulticastMacLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsMIPbMulticastMacLimit_Type.__name__ = "Unsigned32"
_FsMIPbMulticastMacLimit_Object = MibTableColumn
fsMIPbMulticastMacLimit = _FsMIPbMulticastMacLimit_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 1, 1, 1, 2),
    _FsMIPbMulticastMacLimit_Type()
)
fsMIPbMulticastMacLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPbMulticastMacLimit.setStatus("current")
_FsMIPbTunnelStpAddress_Type = MacAddress
_FsMIPbTunnelStpAddress_Object = MibTableColumn
fsMIPbTunnelStpAddress = _FsMIPbTunnelStpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 1, 1, 1, 3),
    _FsMIPbTunnelStpAddress_Type()
)
fsMIPbTunnelStpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPbTunnelStpAddress.setStatus("deprecated")
_FsMIPbTunnelLacpAddress_Type = MacAddress
_FsMIPbTunnelLacpAddress_Object = MibTableColumn
fsMIPbTunnelLacpAddress = _FsMIPbTunnelLacpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 1, 1, 1, 4),
    _FsMIPbTunnelLacpAddress_Type()
)
fsMIPbTunnelLacpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPbTunnelLacpAddress.setStatus("deprecated")
_FsMIPbTunnelDot1xAddress_Type = MacAddress
_FsMIPbTunnelDot1xAddress_Object = MibTableColumn
fsMIPbTunnelDot1xAddress = _FsMIPbTunnelDot1xAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 1, 1, 1, 5),
    _FsMIPbTunnelDot1xAddress_Type()
)
fsMIPbTunnelDot1xAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPbTunnelDot1xAddress.setStatus("deprecated")
_FsMIPbTunnelGvrpAddress_Type = MacAddress
_FsMIPbTunnelGvrpAddress_Object = MibTableColumn
fsMIPbTunnelGvrpAddress = _FsMIPbTunnelGvrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 1, 1, 1, 6),
    _FsMIPbTunnelGvrpAddress_Type()
)
fsMIPbTunnelGvrpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPbTunnelGvrpAddress.setStatus("deprecated")
_FsMIPbTunnelGmrpAddress_Type = MacAddress
_FsMIPbTunnelGmrpAddress_Object = MibTableColumn
fsMIPbTunnelGmrpAddress = _FsMIPbTunnelGmrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 1, 1, 1, 7),
    _FsMIPbTunnelGmrpAddress_Type()
)
fsMIPbTunnelGmrpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPbTunnelGmrpAddress.setStatus("deprecated")
_FsMIPbConfig_ObjectIdentity = ObjectIdentity
fsMIPbConfig = _FsMIPbConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2)
)
_FsMIPbPortInfoTable_Object = MibTable
fsMIPbPortInfoTable = _FsMIPbPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 1)
)
if mibBuilder.loadTexts:
    fsMIPbPortInfoTable.setStatus("current")
_FsMIPbPortInfoEntry_Object = MibTableRow
fsMIPbPortInfoEntry = _FsMIPbPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 1, 1)
)
fsMIPbPortInfoEntry.setIndexNames(
    (0, "ARICENT-MIPROVIDERBRIDGE-MIB", "fsMIPbPort"),
)
if mibBuilder.loadTexts:
    fsMIPbPortInfoEntry.setStatus("current")


class _FsMIPbPort_Type(Integer32):
    """Custom type fsMIPbPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMIPbPort_Type.__name__ = "Integer32"
_FsMIPbPort_Object = MibTableColumn
fsMIPbPort = _FsMIPbPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 1, 1, 1),
    _FsMIPbPort_Type()
)
fsMIPbPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIPbPort.setStatus("current")


class _FsMIPbPortSVlanClassificationMethod_Type(Integer32):
    """Custom type fsMIPbPortSVlanClassificationMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("sourceMac", 1),
          ("destinationMac", 2),
          ("cvlanSrcMac", 3),
          ("cvlanDstMac", 4),
          ("dscp", 5),
          ("cvlanDscp", 6),
          ("sourceIp", 7),
          ("destinationIp", 8),
          ("srcIpDstIp", 9),
          ("cvlanDstIp", 10),
          ("cvlan", 11),
          ("pvid", 12))
    )


_FsMIPbPortSVlanClassificationMethod_Type.__name__ = "Integer32"
_FsMIPbPortSVlanClassificationMethod_Object = MibTableColumn
fsMIPbPortSVlanClassificationMethod = _FsMIPbPortSVlanClassificationMethod_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 1, 1, 2),
    _FsMIPbPortSVlanClassificationMethod_Type()
)
fsMIPbPortSVlanClassificationMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPbPortSVlanClassificationMethod.setStatus("current")


class _FsMIPbPortSVlanIngressEtherType_Type(Integer32):
    """Custom type fsMIPbPortSVlanIngressEtherType based on Integer32"""
    defaultValue = 34984

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMIPbPortSVlanIngressEtherType_Type.__name__ = "Integer32"
_FsMIPbPortSVlanIngressEtherType_Object = MibTableColumn
fsMIPbPortSVlanIngressEtherType = _FsMIPbPortSVlanIngressEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 1, 1, 3),
    _FsMIPbPortSVlanIngressEtherType_Type()
)
fsMIPbPortSVlanIngressEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPbPortSVlanIngressEtherType.setStatus("deprecated")


class _FsMIPbPortSVlanEgressEtherType_Type(Integer32):
    """Custom type fsMIPbPortSVlanEgressEtherType based on Integer32"""
    defaultValue = 34984

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMIPbPortSVlanEgressEtherType_Type.__name__ = "Integer32"
_FsMIPbPortSVlanEgressEtherType_Object = MibTableColumn
fsMIPbPortSVlanEgressEtherType = _FsMIPbPortSVlanEgressEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 1, 1, 4),
    _FsMIPbPortSVlanEgressEtherType_Type()
)
fsMIPbPortSVlanEgressEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPbPortSVlanEgressEtherType.setStatus("deprecated")


class _FsMIPbPortSVlanEtherTypeSwapStatus_Type(EnabledStatus):
    """Custom type fsMIPbPortSVlanEtherTypeSwapStatus based on EnabledStatus"""
    defaultValue = 2


_FsMIPbPortSVlanEtherTypeSwapStatus_Type.__name__ = "EnabledStatus"
_FsMIPbPortSVlanEtherTypeSwapStatus_Object = MibTableColumn
fsMIPbPortSVlanEtherTypeSwapStatus = _FsMIPbPortSVlanEtherTypeSwapStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 1, 1, 5),
    _FsMIPbPortSVlanEtherTypeSwapStatus_Type()
)
fsMIPbPortSVlanEtherTypeSwapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPbPortSVlanEtherTypeSwapStatus.setStatus("current")
_FsMIPbPortSVlanTranslationStatus_Type = EnabledStatus
_FsMIPbPortSVlanTranslationStatus_Object = MibTableColumn
fsMIPbPortSVlanTranslationStatus = _FsMIPbPortSVlanTranslationStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 1, 1, 6),
    _FsMIPbPortSVlanTranslationStatus_Type()
)
fsMIPbPortSVlanTranslationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPbPortSVlanTranslationStatus.setStatus("current")


class _FsMIPbPortUnicastMacLearning_Type(EnabledStatus):
    """Custom type fsMIPbPortUnicastMacLearning based on EnabledStatus"""
    defaultValue = 1


_FsMIPbPortUnicastMacLearning_Type.__name__ = "EnabledStatus"
_FsMIPbPortUnicastMacLearning_Object = MibTableColumn
fsMIPbPortUnicastMacLearning = _FsMIPbPortUnicastMacLearning_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 1, 1, 7),
    _FsMIPbPortUnicastMacLearning_Type()
)
fsMIPbPortUnicastMacLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPbPortUnicastMacLearning.setStatus("deprecated")


class _FsMIPbPortUnicastMacLimit_Type(Unsigned32):
    """Custom type fsMIPbPortUnicastMacLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsMIPbPortUnicastMacLimit_Type.__name__ = "Unsigned32"
_FsMIPbPortUnicastMacLimit_Object = MibTableColumn
fsMIPbPortUnicastMacLimit = _FsMIPbPortUnicastMacLimit_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 1, 1, 8),
    _FsMIPbPortUnicastMacLimit_Type()
)
fsMIPbPortUnicastMacLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPbPortUnicastMacLimit.setStatus("current")


class _FsMIPbPortBundleStatus_Type(EnabledStatus):
    """Custom type fsMIPbPortBundleStatus based on EnabledStatus"""
    defaultValue = 1


_FsMIPbPortBundleStatus_Type.__name__ = "EnabledStatus"
_FsMIPbPortBundleStatus_Object = MibTableColumn
fsMIPbPortBundleStatus = _FsMIPbPortBundleStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 1, 1, 9),
    _FsMIPbPortBundleStatus_Type()
)
fsMIPbPortBundleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPbPortBundleStatus.setStatus("current")


class _FsMIPbPortMultiplexStatus_Type(EnabledStatus):
    """Custom type fsMIPbPortMultiplexStatus based on EnabledStatus"""
    defaultValue = 1


_FsMIPbPortMultiplexStatus_Type.__name__ = "EnabledStatus"
_FsMIPbPortMultiplexStatus_Object = MibTableColumn
fsMIPbPortMultiplexStatus = _FsMIPbPortMultiplexStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 1, 1, 10),
    _FsMIPbPortMultiplexStatus_Type()
)
fsMIPbPortMultiplexStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPbPortMultiplexStatus.setStatus("current")
_FsMIPbSrcMacSVlanTable_Object = MibTable
fsMIPbSrcMacSVlanTable = _FsMIPbSrcMacSVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 2)
)
if mibBuilder.loadTexts:
    fsMIPbSrcMacSVlanTable.setStatus("current")
_FsMIPbSrcMacSVlanEntry_Object = MibTableRow
fsMIPbSrcMacSVlanEntry = _FsMIPbSrcMacSVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 2, 1)
)
fsMIPbSrcMacSVlanEntry.setIndexNames(
    (0, "ARICENT-MIPROVIDERBRIDGE-MIB", "fsMIPbPort"),
    (0, "ARICENT-MIPROVIDERBRIDGE-MIB", "fsMIPbSrcMacAddress"),
)
if mibBuilder.loadTexts:
    fsMIPbSrcMacSVlanEntry.setStatus("current")
_FsMIPbSrcMacAddress_Type = MacAddress
_FsMIPbSrcMacAddress_Object = MibTableColumn
fsMIPbSrcMacAddress = _FsMIPbSrcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 2, 1, 1),
    _FsMIPbSrcMacAddress_Type()
)
fsMIPbSrcMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIPbSrcMacAddress.setStatus("current")
_FsMIPbSrcMacSVlan_Type = VlanId
_FsMIPbSrcMacSVlan_Object = MibTableColumn
fsMIPbSrcMacSVlan = _FsMIPbSrcMacSVlan_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 2, 1, 2),
    _FsMIPbSrcMacSVlan_Type()
)
fsMIPbSrcMacSVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPbSrcMacSVlan.setStatus("current")
_FsMIPbSrcMacRowStatus_Type = RowStatus
_FsMIPbSrcMacRowStatus_Object = MibTableColumn
fsMIPbSrcMacRowStatus = _FsMIPbSrcMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 2, 1, 3),
    _FsMIPbSrcMacRowStatus_Type()
)
fsMIPbSrcMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIPbSrcMacRowStatus.setStatus("current")
_FsMIPbDstMacSVlanTable_Object = MibTable
fsMIPbDstMacSVlanTable = _FsMIPbDstMacSVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 3)
)
if mibBuilder.loadTexts:
    fsMIPbDstMacSVlanTable.setStatus("current")
_FsMIPbDstMacSVlanEntry_Object = MibTableRow
fsMIPbDstMacSVlanEntry = _FsMIPbDstMacSVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 3, 1)
)
fsMIPbDstMacSVlanEntry.setIndexNames(
    (0, "ARICENT-MIPROVIDERBRIDGE-MIB", "fsMIPbPort"),
    (0, "ARICENT-MIPROVIDERBRIDGE-MIB", "fsMIPbDstMacAddress"),
)
if mibBuilder.loadTexts:
    fsMIPbDstMacSVlanEntry.setStatus("current")
_FsMIPbDstMacAddress_Type = MacAddress
_FsMIPbDstMacAddress_Object = MibTableColumn
fsMIPbDstMacAddress = _FsMIPbDstMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 3, 1, 1),
    _FsMIPbDstMacAddress_Type()
)
fsMIPbDstMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIPbDstMacAddress.setStatus("current")
_FsMIPbDstMacSVlan_Type = VlanId
_FsMIPbDstMacSVlan_Object = MibTableColumn
fsMIPbDstMacSVlan = _FsMIPbDstMacSVlan_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 3, 1, 2),
    _FsMIPbDstMacSVlan_Type()
)
fsMIPbDstMacSVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPbDstMacSVlan.setStatus("current")
_FsMIPbDstMacRowStatus_Type = RowStatus
_FsMIPbDstMacRowStatus_Object = MibTableColumn
fsMIPbDstMacRowStatus = _FsMIPbDstMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 3, 1, 3),
    _FsMIPbDstMacRowStatus_Type()
)
fsMIPbDstMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIPbDstMacRowStatus.setStatus("current")
_FsMIPbCVlanSrcMacSVlanTable_Object = MibTable
fsMIPbCVlanSrcMacSVlanTable = _FsMIPbCVlanSrcMacSVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 4)
)
if mibBuilder.loadTexts:
    fsMIPbCVlanSrcMacSVlanTable.setStatus("current")
_FsMIPbCVlanSrcMacSVlanEntry_Object = MibTableRow
fsMIPbCVlanSrcMacSVlanEntry = _FsMIPbCVlanSrcMacSVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 4, 1)
)
fsMIPbCVlanSrcMacSVlanEntry.setIndexNames(
    (0, "ARICENT-MIPROVIDERBRIDGE-MIB", "fsMIPbPort"),
    (0, "ARICENT-MIPROVIDERBRIDGE-MIB", "fsMIPbCVlanSrcMacCVlan"),
    (0, "ARICENT-MIPROVIDERBRIDGE-MIB", "fsMIPbCVlanSrcMacAddr"),
)
if mibBuilder.loadTexts:
    fsMIPbCVlanSrcMacSVlanEntry.setStatus("current")
_FsMIPbCVlanSrcMacCVlan_Type = VlanId
_FsMIPbCVlanSrcMacCVlan_Object = MibTableColumn
fsMIPbCVlanSrcMacCVlan = _FsMIPbCVlanSrcMacCVlan_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 4, 1, 1),
    _FsMIPbCVlanSrcMacCVlan_Type()
)
fsMIPbCVlanSrcMacCVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIPbCVlanSrcMacCVlan.setStatus("current")
_FsMIPbCVlanSrcMacAddr_Type = MacAddress
_FsMIPbCVlanSrcMacAddr_Object = MibTableColumn
fsMIPbCVlanSrcMacAddr = _FsMIPbCVlanSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 4, 1, 2),
    _FsMIPbCVlanSrcMacAddr_Type()
)
fsMIPbCVlanSrcMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIPbCVlanSrcMacAddr.setStatus("current")
_FsMIPbCVlanSrcMacSVlan_Type = VlanId
_FsMIPbCVlanSrcMacSVlan_Object = MibTableColumn
fsMIPbCVlanSrcMacSVlan = _FsMIPbCVlanSrcMacSVlan_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 4, 1, 3),
    _FsMIPbCVlanSrcMacSVlan_Type()
)
fsMIPbCVlanSrcMacSVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPbCVlanSrcMacSVlan.setStatus("current")
_FsMIPbCVlanSrcMacRowStatus_Type = RowStatus
_FsMIPbCVlanSrcMacRowStatus_Object = MibTableColumn
fsMIPbCVlanSrcMacRowStatus = _FsMIPbCVlanSrcMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 4, 1, 4),
    _FsMIPbCVlanSrcMacRowStatus_Type()
)
fsMIPbCVlanSrcMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIPbCVlanSrcMacRowStatus.setStatus("current")
_FsMIPbCVlanDstMacSVlanTable_Object = MibTable
fsMIPbCVlanDstMacSVlanTable = _FsMIPbCVlanDstMacSVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 5)
)
if mibBuilder.loadTexts:
    fsMIPbCVlanDstMacSVlanTable.setStatus("current")
_FsMIPbCVlanDstMacSVlanEntry_Object = MibTableRow
fsMIPbCVlanDstMacSVlanEntry = _FsMIPbCVlanDstMacSVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 5, 1)
)
fsMIPbCVlanDstMacSVlanEntry.setIndexNames(
    (0, "ARICENT-MIPROVIDERBRIDGE-MIB", "fsMIPbPort"),
    (0, "ARICENT-MIPROVIDERBRIDGE-MIB", "fsMIPbCVlanDstMacCVlan"),
    (0, "ARICENT-MIPROVIDERBRIDGE-MIB", "fsMIPbCVlanDstMacAddr"),
)
if mibBuilder.loadTexts:
    fsMIPbCVlanDstMacSVlanEntry.setStatus("current")
_FsMIPbCVlanDstMacCVlan_Type = VlanId
_FsMIPbCVlanDstMacCVlan_Object = MibTableColumn
fsMIPbCVlanDstMacCVlan = _FsMIPbCVlanDstMacCVlan_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 5, 1, 1),
    _FsMIPbCVlanDstMacCVlan_Type()
)
fsMIPbCVlanDstMacCVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIPbCVlanDstMacCVlan.setStatus("current")
_FsMIPbCVlanDstMacAddr_Type = MacAddress
_FsMIPbCVlanDstMacAddr_Object = MibTableColumn
fsMIPbCVlanDstMacAddr = _FsMIPbCVlanDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 5, 1, 2),
    _FsMIPbCVlanDstMacAddr_Type()
)
fsMIPbCVlanDstMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIPbCVlanDstMacAddr.setStatus("current")
_FsMIPbCVlanDstMacSVlan_Type = VlanId
_FsMIPbCVlanDstMacSVlan_Object = MibTableColumn
fsMIPbCVlanDstMacSVlan = _FsMIPbCVlanDstMacSVlan_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 5, 1, 3),
    _FsMIPbCVlanDstMacSVlan_Type()
)
fsMIPbCVlanDstMacSVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPbCVlanDstMacSVlan.setStatus("current")
_FsMIPbCVlanDstMacRowStatus_Type = RowStatus
_FsMIPbCVlanDstMacRowStatus_Object = MibTableColumn
fsMIPbCVlanDstMacRowStatus = _FsMIPbCVlanDstMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 5, 1, 4),
    _FsMIPbCVlanDstMacRowStatus_Type()
)
fsMIPbCVlanDstMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIPbCVlanDstMacRowStatus.setStatus("current")
_FsMIPbDscpSVlanTable_Object = MibTable
fsMIPbDscpSVlanTable = _FsMIPbDscpSVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 6)
)
if mibBuilder.loadTexts:
    fsMIPbDscpSVlanTable.setStatus("current")
_FsMIPbDscpSVlanEntry_Object = MibTableRow
fsMIPbDscpSVlanEntry = _FsMIPbDscpSVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 6, 1)
)
fsMIPbDscpSVlanEntry.setIndexNames(
    (0, "ARICENT-MIPROVIDERBRIDGE-MIB", "fsMIPbPort"),
    (0, "ARICENT-MIPROVIDERBRIDGE-MIB", "fsMIPbDscp"),
)
if mibBuilder.loadTexts:
    fsMIPbDscpSVlanEntry.setStatus("current")


class _FsMIPbDscp_Type(Integer32):
    """Custom type fsMIPbDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_FsMIPbDscp_Type.__name__ = "Integer32"
_FsMIPbDscp_Object = MibTableColumn
fsMIPbDscp = _FsMIPbDscp_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 6, 1, 1),
    _FsMIPbDscp_Type()
)
fsMIPbDscp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIPbDscp.setStatus("current")
_FsMIPbDscpSVlan_Type = VlanId
_FsMIPbDscpSVlan_Object = MibTableColumn
fsMIPbDscpSVlan = _FsMIPbDscpSVlan_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 6, 1, 2),
    _FsMIPbDscpSVlan_Type()
)
fsMIPbDscpSVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPbDscpSVlan.setStatus("current")
_FsMIPbDscpRowStatus_Type = RowStatus
_FsMIPbDscpRowStatus_Object = MibTableColumn
fsMIPbDscpRowStatus = _FsMIPbDscpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 6, 1, 3),
    _FsMIPbDscpRowStatus_Type()
)
fsMIPbDscpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIPbDscpRowStatus.setStatus("current")
_FsMIPbCVlanDscpSVlanTable_Object = MibTable
fsMIPbCVlanDscpSVlanTable = _FsMIPbCVlanDscpSVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 7)
)
if mibBuilder.loadTexts:
    fsMIPbCVlanDscpSVlanTable.setStatus("current")
_FsMIPbCVlanDscpSVlanEntry_Object = MibTableRow
fsMIPbCVlanDscpSVlanEntry = _FsMIPbCVlanDscpSVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 7, 1)
)
fsMIPbCVlanDscpSVlanEntry.setIndexNames(
    (0, "ARICENT-MIPROVIDERBRIDGE-MIB", "fsMIPbPort"),
    (0, "ARICENT-MIPROVIDERBRIDGE-MIB", "fsMIPbCVlanDscpCVlan"),
    (0, "ARICENT-MIPROVIDERBRIDGE-MIB", "fsMIPbCVlanDscp"),
)
if mibBuilder.loadTexts:
    fsMIPbCVlanDscpSVlanEntry.setStatus("current")
_FsMIPbCVlanDscpCVlan_Type = VlanId
_FsMIPbCVlanDscpCVlan_Object = MibTableColumn
fsMIPbCVlanDscpCVlan = _FsMIPbCVlanDscpCVlan_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 7, 1, 1),
    _FsMIPbCVlanDscpCVlan_Type()
)
fsMIPbCVlanDscpCVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIPbCVlanDscpCVlan.setStatus("current")


class _FsMIPbCVlanDscp_Type(Integer32):
    """Custom type fsMIPbCVlanDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_FsMIPbCVlanDscp_Type.__name__ = "Integer32"
_FsMIPbCVlanDscp_Object = MibTableColumn
fsMIPbCVlanDscp = _FsMIPbCVlanDscp_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 7, 1, 2),
    _FsMIPbCVlanDscp_Type()
)
fsMIPbCVlanDscp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIPbCVlanDscp.setStatus("current")
_FsMIPbCVlanDscpSVlan_Type = VlanId
_FsMIPbCVlanDscpSVlan_Object = MibTableColumn
fsMIPbCVlanDscpSVlan = _FsMIPbCVlanDscpSVlan_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 7, 1, 3),
    _FsMIPbCVlanDscpSVlan_Type()
)
fsMIPbCVlanDscpSVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPbCVlanDscpSVlan.setStatus("current")
_FsMIPbCVlanDscpRowStatus_Type = RowStatus
_FsMIPbCVlanDscpRowStatus_Object = MibTableColumn
fsMIPbCVlanDscpRowStatus = _FsMIPbCVlanDscpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 7, 1, 4),
    _FsMIPbCVlanDscpRowStatus_Type()
)
fsMIPbCVlanDscpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIPbCVlanDscpRowStatus.setStatus("current")
_FsMIPbSrcIpAddrSVlanTable_Object = MibTable
fsMIPbSrcIpAddrSVlanTable = _FsMIPbSrcIpAddrSVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 8)
)
if mibBuilder.loadTexts:
    fsMIPbSrcIpAddrSVlanTable.setStatus("current")
_FsMIPbSrcIpAddrSVlanEntry_Object = MibTableRow
fsMIPbSrcIpAddrSVlanEntry = _FsMIPbSrcIpAddrSVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 8, 1)
)
fsMIPbSrcIpAddrSVlanEntry.setIndexNames(
    (0, "ARICENT-MIPROVIDERBRIDGE-MIB", "fsMIPbPort"),
    (0, "ARICENT-MIPROVIDERBRIDGE-MIB", "fsMIPbSrcIpAddr"),
)
if mibBuilder.loadTexts:
    fsMIPbSrcIpAddrSVlanEntry.setStatus("current")
_FsMIPbSrcIpAddr_Type = IpAddress
_FsMIPbSrcIpAddr_Object = MibTableColumn
fsMIPbSrcIpAddr = _FsMIPbSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 8, 1, 1),
    _FsMIPbSrcIpAddr_Type()
)
fsMIPbSrcIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIPbSrcIpAddr.setStatus("current")
_FsMIPbSrcIpSVlan_Type = VlanId
_FsMIPbSrcIpSVlan_Object = MibTableColumn
fsMIPbSrcIpSVlan = _FsMIPbSrcIpSVlan_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 8, 1, 2),
    _FsMIPbSrcIpSVlan_Type()
)
fsMIPbSrcIpSVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPbSrcIpSVlan.setStatus("current")
_FsMIPbSrcIpRowStatus_Type = RowStatus
_FsMIPbSrcIpRowStatus_Object = MibTableColumn
fsMIPbSrcIpRowStatus = _FsMIPbSrcIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 8, 1, 3),
    _FsMIPbSrcIpRowStatus_Type()
)
fsMIPbSrcIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIPbSrcIpRowStatus.setStatus("current")
_FsMIPbDstIpAddrSVlanTable_Object = MibTable
fsMIPbDstIpAddrSVlanTable = _FsMIPbDstIpAddrSVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 9)
)
if mibBuilder.loadTexts:
    fsMIPbDstIpAddrSVlanTable.setStatus("current")
_FsMIPbDstIpAddrSVlanEntry_Object = MibTableRow
fsMIPbDstIpAddrSVlanEntry = _FsMIPbDstIpAddrSVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 9, 1)
)
fsMIPbDstIpAddrSVlanEntry.setIndexNames(
    (0, "ARICENT-MIPROVIDERBRIDGE-MIB", "fsMIPbPort"),
    (0, "ARICENT-MIPROVIDERBRIDGE-MIB", "fsMIPbDstIpAddr"),
)
if mibBuilder.loadTexts:
    fsMIPbDstIpAddrSVlanEntry.setStatus("current")
_FsMIPbDstIpAddr_Type = IpAddress
_FsMIPbDstIpAddr_Object = MibTableColumn
fsMIPbDstIpAddr = _FsMIPbDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 9, 1, 1),
    _FsMIPbDstIpAddr_Type()
)
fsMIPbDstIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIPbDstIpAddr.setStatus("current")
_FsMIPbDstIpSVlan_Type = VlanId
_FsMIPbDstIpSVlan_Object = MibTableColumn
fsMIPbDstIpSVlan = _FsMIPbDstIpSVlan_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 9, 1, 2),
    _FsMIPbDstIpSVlan_Type()
)
fsMIPbDstIpSVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPbDstIpSVlan.setStatus("current")
_FsMIPbDstIpRowStatus_Type = RowStatus
_FsMIPbDstIpRowStatus_Object = MibTableColumn
fsMIPbDstIpRowStatus = _FsMIPbDstIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 9, 1, 3),
    _FsMIPbDstIpRowStatus_Type()
)
fsMIPbDstIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIPbDstIpRowStatus.setStatus("current")
_FsMIPbSrcDstIpSVlanTable_Object = MibTable
fsMIPbSrcDstIpSVlanTable = _FsMIPbSrcDstIpSVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 10)
)
if mibBuilder.loadTexts:
    fsMIPbSrcDstIpSVlanTable.setStatus("current")
_FsMIPbSrcDstIpSVlanEntry_Object = MibTableRow
fsMIPbSrcDstIpSVlanEntry = _FsMIPbSrcDstIpSVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 10, 1)
)
fsMIPbSrcDstIpSVlanEntry.setIndexNames(
    (0, "ARICENT-MIPROVIDERBRIDGE-MIB", "fsMIPbPort"),
    (0, "ARICENT-MIPROVIDERBRIDGE-MIB", "fsMIPbSrcDstSrcIpAddr"),
    (0, "ARICENT-MIPROVIDERBRIDGE-MIB", "fsMIPbSrcDstDstIpAddr"),
)
if mibBuilder.loadTexts:
    fsMIPbSrcDstIpSVlanEntry.setStatus("current")
_FsMIPbSrcDstSrcIpAddr_Type = IpAddress
_FsMIPbSrcDstSrcIpAddr_Object = MibTableColumn
fsMIPbSrcDstSrcIpAddr = _FsMIPbSrcDstSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 10, 1, 1),
    _FsMIPbSrcDstSrcIpAddr_Type()
)
fsMIPbSrcDstSrcIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIPbSrcDstSrcIpAddr.setStatus("current")
_FsMIPbSrcDstDstIpAddr_Type = IpAddress
_FsMIPbSrcDstDstIpAddr_Object = MibTableColumn
fsMIPbSrcDstDstIpAddr = _FsMIPbSrcDstDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 10, 1, 2),
    _FsMIPbSrcDstDstIpAddr_Type()
)
fsMIPbSrcDstDstIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIPbSrcDstDstIpAddr.setStatus("current")
_FsMIPbSrcDstIpSVlan_Type = VlanId
_FsMIPbSrcDstIpSVlan_Object = MibTableColumn
fsMIPbSrcDstIpSVlan = _FsMIPbSrcDstIpSVlan_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 10, 1, 3),
    _FsMIPbSrcDstIpSVlan_Type()
)
fsMIPbSrcDstIpSVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPbSrcDstIpSVlan.setStatus("current")
_FsMIPbSrcDstIpRowStatus_Type = RowStatus
_FsMIPbSrcDstIpRowStatus_Object = MibTableColumn
fsMIPbSrcDstIpRowStatus = _FsMIPbSrcDstIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 10, 1, 4),
    _FsMIPbSrcDstIpRowStatus_Type()
)
fsMIPbSrcDstIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIPbSrcDstIpRowStatus.setStatus("current")
_FsMIPbCVlanDstIpSVlanTable_Object = MibTable
fsMIPbCVlanDstIpSVlanTable = _FsMIPbCVlanDstIpSVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 11)
)
if mibBuilder.loadTexts:
    fsMIPbCVlanDstIpSVlanTable.setStatus("current")
_FsMIPbCVlanDstIpSVlanEntry_Object = MibTableRow
fsMIPbCVlanDstIpSVlanEntry = _FsMIPbCVlanDstIpSVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 11, 1)
)
fsMIPbCVlanDstIpSVlanEntry.setIndexNames(
    (0, "ARICENT-MIPROVIDERBRIDGE-MIB", "fsMIPbPort"),
    (0, "ARICENT-MIPROVIDERBRIDGE-MIB", "fsMIPbCVlanDstIpCVlan"),
    (0, "ARICENT-MIPROVIDERBRIDGE-MIB", "fsMIPbCVlanDstIp"),
)
if mibBuilder.loadTexts:
    fsMIPbCVlanDstIpSVlanEntry.setStatus("current")
_FsMIPbCVlanDstIpCVlan_Type = VlanId
_FsMIPbCVlanDstIpCVlan_Object = MibTableColumn
fsMIPbCVlanDstIpCVlan = _FsMIPbCVlanDstIpCVlan_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 11, 1, 1),
    _FsMIPbCVlanDstIpCVlan_Type()
)
fsMIPbCVlanDstIpCVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIPbCVlanDstIpCVlan.setStatus("current")
_FsMIPbCVlanDstIp_Type = IpAddress
_FsMIPbCVlanDstIp_Object = MibTableColumn
fsMIPbCVlanDstIp = _FsMIPbCVlanDstIp_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 11, 1, 2),
    _FsMIPbCVlanDstIp_Type()
)
fsMIPbCVlanDstIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIPbCVlanDstIp.setStatus("current")
_FsMIPbCVlanDstIpSVlan_Type = VlanId
_FsMIPbCVlanDstIpSVlan_Object = MibTableColumn
fsMIPbCVlanDstIpSVlan = _FsMIPbCVlanDstIpSVlan_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 11, 1, 3),
    _FsMIPbCVlanDstIpSVlan_Type()
)
fsMIPbCVlanDstIpSVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPbCVlanDstIpSVlan.setStatus("current")
_FsMIPbCVlanDstIpRowStatus_Type = RowStatus
_FsMIPbCVlanDstIpRowStatus_Object = MibTableColumn
fsMIPbCVlanDstIpRowStatus = _FsMIPbCVlanDstIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 11, 1, 4),
    _FsMIPbCVlanDstIpRowStatus_Type()
)
fsMIPbCVlanDstIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIPbCVlanDstIpRowStatus.setStatus("current")
_FsMIPbPortBasedCVlanTable_Object = MibTable
fsMIPbPortBasedCVlanTable = _FsMIPbPortBasedCVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 12)
)
if mibBuilder.loadTexts:
    fsMIPbPortBasedCVlanTable.setStatus("current")
_FsMIPbPortBasedCVlanEntry_Object = MibTableRow
fsMIPbPortBasedCVlanEntry = _FsMIPbPortBasedCVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 12, 1)
)
fsMIPbPortBasedCVlanEntry.setIndexNames(
    (0, "ARICENT-MIPROVIDERBRIDGE-MIB", "fsMIPbPort"),
)
if mibBuilder.loadTexts:
    fsMIPbPortBasedCVlanEntry.setStatus("current")
_FsMIPbPortCVlan_Type = VlanId
_FsMIPbPortCVlan_Object = MibTableColumn
fsMIPbPortCVlan = _FsMIPbPortCVlan_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 12, 1, 1),
    _FsMIPbPortCVlan_Type()
)
fsMIPbPortCVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPbPortCVlan.setStatus("current")


class _FsMIPbPortCVlanClassifyStatus_Type(EnabledStatus):
    """Custom type fsMIPbPortCVlanClassifyStatus based on EnabledStatus"""
    defaultValue = 1


_FsMIPbPortCVlanClassifyStatus_Type.__name__ = "EnabledStatus"
_FsMIPbPortCVlanClassifyStatus_Object = MibTableColumn
fsMIPbPortCVlanClassifyStatus = _FsMIPbPortCVlanClassifyStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 12, 1, 2),
    _FsMIPbPortCVlanClassifyStatus_Type()
)
fsMIPbPortCVlanClassifyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPbPortCVlanClassifyStatus.setStatus("current")


class _FsMIPbPortEgressUntaggedStatus_Type(Integer32):
    """Custom type fsMIPbPortEgressUntaggedStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_FsMIPbPortEgressUntaggedStatus_Type.__name__ = "Integer32"
_FsMIPbPortEgressUntaggedStatus_Object = MibTableColumn
fsMIPbPortEgressUntaggedStatus = _FsMIPbPortEgressUntaggedStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 12, 1, 3),
    _FsMIPbPortEgressUntaggedStatus_Type()
)
fsMIPbPortEgressUntaggedStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPbPortEgressUntaggedStatus.setStatus("current")
_FsMIPbEtherTypeSwapTable_Object = MibTable
fsMIPbEtherTypeSwapTable = _FsMIPbEtherTypeSwapTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 13)
)
if mibBuilder.loadTexts:
    fsMIPbEtherTypeSwapTable.setStatus("current")
_FsMIPbEtherTypeSwapEntry_Object = MibTableRow
fsMIPbEtherTypeSwapEntry = _FsMIPbEtherTypeSwapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 13, 1)
)
fsMIPbEtherTypeSwapEntry.setIndexNames(
    (0, "ARICENT-MIPROVIDERBRIDGE-MIB", "fsMIPbPort"),
    (0, "ARICENT-MIPROVIDERBRIDGE-MIB", "fsMIPbLocalEtherType"),
)
if mibBuilder.loadTexts:
    fsMIPbEtherTypeSwapEntry.setStatus("current")


class _FsMIPbLocalEtherType_Type(Integer32):
    """Custom type fsMIPbLocalEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMIPbLocalEtherType_Type.__name__ = "Integer32"
_FsMIPbLocalEtherType_Object = MibTableColumn
fsMIPbLocalEtherType = _FsMIPbLocalEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 13, 1, 1),
    _FsMIPbLocalEtherType_Type()
)
fsMIPbLocalEtherType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIPbLocalEtherType.setStatus("current")


class _FsMIPbRelayEtherType_Type(Integer32):
    """Custom type fsMIPbRelayEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMIPbRelayEtherType_Type.__name__ = "Integer32"
_FsMIPbRelayEtherType_Object = MibTableColumn
fsMIPbRelayEtherType = _FsMIPbRelayEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 13, 1, 2),
    _FsMIPbRelayEtherType_Type()
)
fsMIPbRelayEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPbRelayEtherType.setStatus("current")
_FsMIPbEtherTypeSwapRowStatus_Type = RowStatus
_FsMIPbEtherTypeSwapRowStatus_Object = MibTableColumn
fsMIPbEtherTypeSwapRowStatus = _FsMIPbEtherTypeSwapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 13, 1, 3),
    _FsMIPbEtherTypeSwapRowStatus_Type()
)
fsMIPbEtherTypeSwapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIPbEtherTypeSwapRowStatus.setStatus("current")
_FsMIPbSVlanConfigTable_Object = MibTable
fsMIPbSVlanConfigTable = _FsMIPbSVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 14)
)
if mibBuilder.loadTexts:
    fsMIPbSVlanConfigTable.setStatus("current")
_FsMIPbSVlanConfigEntry_Object = MibTableRow
fsMIPbSVlanConfigEntry = _FsMIPbSVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 14, 1)
)
fsMIPbSVlanConfigEntry.setIndexNames(
    (0, "ARICENT-MIPROVIDERBRIDGE-MIB", "fsMIPbContextId"),
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    fsMIPbSVlanConfigEntry.setStatus("current")


class _FsMIPbSVlanConfigServiceType_Type(Integer32):
    """Custom type fsMIPbSVlanConfigServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eLine", 1),
          ("eLan", 2))
    )


_FsMIPbSVlanConfigServiceType_Type.__name__ = "Integer32"
_FsMIPbSVlanConfigServiceType_Object = MibTableColumn
fsMIPbSVlanConfigServiceType = _FsMIPbSVlanConfigServiceType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 14, 1, 1),
    _FsMIPbSVlanConfigServiceType_Type()
)
fsMIPbSVlanConfigServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPbSVlanConfigServiceType.setStatus("current")
_FsMIPbTunnelProtocolTable_Object = MibTable
fsMIPbTunnelProtocolTable = _FsMIPbTunnelProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 15)
)
if mibBuilder.loadTexts:
    fsMIPbTunnelProtocolTable.setStatus("deprecated")
_FsMIPbTunnelProtocolEntry_Object = MibTableRow
fsMIPbTunnelProtocolEntry = _FsMIPbTunnelProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 15, 1)
)
fsMIPbTunnelProtocolEntry.setIndexNames(
    (0, "ARICENT-MIPROVIDERBRIDGE-MIB", "fsMIPbPort"),
)
if mibBuilder.loadTexts:
    fsMIPbTunnelProtocolEntry.setStatus("deprecated")
_FsMIPbTunnelProtocolDot1x_Type = TunnelStatus
_FsMIPbTunnelProtocolDot1x_Object = MibTableColumn
fsMIPbTunnelProtocolDot1x = _FsMIPbTunnelProtocolDot1x_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 15, 1, 1),
    _FsMIPbTunnelProtocolDot1x_Type()
)
fsMIPbTunnelProtocolDot1x.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPbTunnelProtocolDot1x.setStatus("deprecated")
_FsMIPbTunnelProtocolLacp_Type = TunnelStatus
_FsMIPbTunnelProtocolLacp_Object = MibTableColumn
fsMIPbTunnelProtocolLacp = _FsMIPbTunnelProtocolLacp_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 15, 1, 2),
    _FsMIPbTunnelProtocolLacp_Type()
)
fsMIPbTunnelProtocolLacp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPbTunnelProtocolLacp.setStatus("deprecated")
_FsMIPbTunnelProtocolStp_Type = TunnelStatus
_FsMIPbTunnelProtocolStp_Object = MibTableColumn
fsMIPbTunnelProtocolStp = _FsMIPbTunnelProtocolStp_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 15, 1, 3),
    _FsMIPbTunnelProtocolStp_Type()
)
fsMIPbTunnelProtocolStp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPbTunnelProtocolStp.setStatus("deprecated")
_FsMIPbTunnelProtocolGvrp_Type = TunnelStatus
_FsMIPbTunnelProtocolGvrp_Object = MibTableColumn
fsMIPbTunnelProtocolGvrp = _FsMIPbTunnelProtocolGvrp_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 15, 1, 4),
    _FsMIPbTunnelProtocolGvrp_Type()
)
fsMIPbTunnelProtocolGvrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPbTunnelProtocolGvrp.setStatus("deprecated")
_FsMIPbTunnelProtocolGmrp_Type = TunnelStatus
_FsMIPbTunnelProtocolGmrp_Object = MibTableColumn
fsMIPbTunnelProtocolGmrp = _FsMIPbTunnelProtocolGmrp_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 15, 1, 5),
    _FsMIPbTunnelProtocolGmrp_Type()
)
fsMIPbTunnelProtocolGmrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPbTunnelProtocolGmrp.setStatus("deprecated")
_FsMIPbTunnelProtocolIgmp_Type = TunnelStatus
_FsMIPbTunnelProtocolIgmp_Object = MibTableColumn
fsMIPbTunnelProtocolIgmp = _FsMIPbTunnelProtocolIgmp_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 15, 1, 6),
    _FsMIPbTunnelProtocolIgmp_Type()
)
fsMIPbTunnelProtocolIgmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPbTunnelProtocolIgmp.setStatus("deprecated")
_FsMIPbTunnelProtocolStatsTable_Object = MibTable
fsMIPbTunnelProtocolStatsTable = _FsMIPbTunnelProtocolStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 16)
)
if mibBuilder.loadTexts:
    fsMIPbTunnelProtocolStatsTable.setStatus("deprecated")
_FsMIPbTunnelProtocolStatsEntry_Object = MibTableRow
fsMIPbTunnelProtocolStatsEntry = _FsMIPbTunnelProtocolStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 16, 1)
)
fsMIPbTunnelProtocolStatsEntry.setIndexNames(
    (0, "ARICENT-MIPROVIDERBRIDGE-MIB", "fsMIPbPort"),
)
if mibBuilder.loadTexts:
    fsMIPbTunnelProtocolStatsEntry.setStatus("deprecated")
_FsMIPbTunnelProtocolDot1xPktsRecvd_Type = Counter32
_FsMIPbTunnelProtocolDot1xPktsRecvd_Object = MibTableColumn
fsMIPbTunnelProtocolDot1xPktsRecvd = _FsMIPbTunnelProtocolDot1xPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 16, 1, 1),
    _FsMIPbTunnelProtocolDot1xPktsRecvd_Type()
)
fsMIPbTunnelProtocolDot1xPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbTunnelProtocolDot1xPktsRecvd.setStatus("deprecated")
_FsMIPbTunnelProtocolDot1xPktsSent_Type = Counter32
_FsMIPbTunnelProtocolDot1xPktsSent_Object = MibTableColumn
fsMIPbTunnelProtocolDot1xPktsSent = _FsMIPbTunnelProtocolDot1xPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 16, 1, 2),
    _FsMIPbTunnelProtocolDot1xPktsSent_Type()
)
fsMIPbTunnelProtocolDot1xPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbTunnelProtocolDot1xPktsSent.setStatus("deprecated")
_FsMIPbTunnelProtocolLacpPktsRecvd_Type = Counter32
_FsMIPbTunnelProtocolLacpPktsRecvd_Object = MibTableColumn
fsMIPbTunnelProtocolLacpPktsRecvd = _FsMIPbTunnelProtocolLacpPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 16, 1, 3),
    _FsMIPbTunnelProtocolLacpPktsRecvd_Type()
)
fsMIPbTunnelProtocolLacpPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbTunnelProtocolLacpPktsRecvd.setStatus("deprecated")
_FsMIPbTunnelProtocolLacpPktsSent_Type = Counter32
_FsMIPbTunnelProtocolLacpPktsSent_Object = MibTableColumn
fsMIPbTunnelProtocolLacpPktsSent = _FsMIPbTunnelProtocolLacpPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 16, 1, 4),
    _FsMIPbTunnelProtocolLacpPktsSent_Type()
)
fsMIPbTunnelProtocolLacpPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbTunnelProtocolLacpPktsSent.setStatus("deprecated")
_FsMIPbTunnelProtocolStpPDUsRecvd_Type = Counter32
_FsMIPbTunnelProtocolStpPDUsRecvd_Object = MibTableColumn
fsMIPbTunnelProtocolStpPDUsRecvd = _FsMIPbTunnelProtocolStpPDUsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 16, 1, 5),
    _FsMIPbTunnelProtocolStpPDUsRecvd_Type()
)
fsMIPbTunnelProtocolStpPDUsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbTunnelProtocolStpPDUsRecvd.setStatus("deprecated")
_FsMIPbTunnelProtocolStpPDUsSent_Type = Counter32
_FsMIPbTunnelProtocolStpPDUsSent_Object = MibTableColumn
fsMIPbTunnelProtocolStpPDUsSent = _FsMIPbTunnelProtocolStpPDUsSent_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 16, 1, 6),
    _FsMIPbTunnelProtocolStpPDUsSent_Type()
)
fsMIPbTunnelProtocolStpPDUsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbTunnelProtocolStpPDUsSent.setStatus("deprecated")
_FsMIPbTunnelProtocolGvrpPDUsRecvd_Type = Counter32
_FsMIPbTunnelProtocolGvrpPDUsRecvd_Object = MibTableColumn
fsMIPbTunnelProtocolGvrpPDUsRecvd = _FsMIPbTunnelProtocolGvrpPDUsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 16, 1, 7),
    _FsMIPbTunnelProtocolGvrpPDUsRecvd_Type()
)
fsMIPbTunnelProtocolGvrpPDUsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbTunnelProtocolGvrpPDUsRecvd.setStatus("deprecated")
_FsMIPbTunnelProtocolGvrpPDUsSent_Type = Counter32
_FsMIPbTunnelProtocolGvrpPDUsSent_Object = MibTableColumn
fsMIPbTunnelProtocolGvrpPDUsSent = _FsMIPbTunnelProtocolGvrpPDUsSent_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 16, 1, 8),
    _FsMIPbTunnelProtocolGvrpPDUsSent_Type()
)
fsMIPbTunnelProtocolGvrpPDUsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbTunnelProtocolGvrpPDUsSent.setStatus("deprecated")
_FsMIPbTunnelProtocolGmrpPktsRecvd_Type = Counter32
_FsMIPbTunnelProtocolGmrpPktsRecvd_Object = MibTableColumn
fsMIPbTunnelProtocolGmrpPktsRecvd = _FsMIPbTunnelProtocolGmrpPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 16, 1, 9),
    _FsMIPbTunnelProtocolGmrpPktsRecvd_Type()
)
fsMIPbTunnelProtocolGmrpPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbTunnelProtocolGmrpPktsRecvd.setStatus("deprecated")
_FsMIPbTunnelProtocolGmrpPktsSent_Type = Counter32
_FsMIPbTunnelProtocolGmrpPktsSent_Object = MibTableColumn
fsMIPbTunnelProtocolGmrpPktsSent = _FsMIPbTunnelProtocolGmrpPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 16, 1, 10),
    _FsMIPbTunnelProtocolGmrpPktsSent_Type()
)
fsMIPbTunnelProtocolGmrpPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbTunnelProtocolGmrpPktsSent.setStatus("deprecated")
_FsMIPbTunnelProtocolIgmpPktsRecvd_Type = Counter32
_FsMIPbTunnelProtocolIgmpPktsRecvd_Object = MibTableColumn
fsMIPbTunnelProtocolIgmpPktsRecvd = _FsMIPbTunnelProtocolIgmpPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 16, 1, 11),
    _FsMIPbTunnelProtocolIgmpPktsRecvd_Type()
)
fsMIPbTunnelProtocolIgmpPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbTunnelProtocolIgmpPktsRecvd.setStatus("deprecated")
_FsMIPbTunnelProtocolIgmpPktsSent_Type = Counter32
_FsMIPbTunnelProtocolIgmpPktsSent_Object = MibTableColumn
fsMIPbTunnelProtocolIgmpPktsSent = _FsMIPbTunnelProtocolIgmpPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 16, 1, 12),
    _FsMIPbTunnelProtocolIgmpPktsSent_Type()
)
fsMIPbTunnelProtocolIgmpPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbTunnelProtocolIgmpPktsSent.setStatus("deprecated")
_FsMIPbPepExtTable_Object = MibTable
fsMIPbPepExtTable = _FsMIPbPepExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 17)
)
if mibBuilder.loadTexts:
    fsMIPbPepExtTable.setStatus("current")
_FsMIPbPepExtEntry_Object = MibTableRow
fsMIPbPepExtEntry = _FsMIPbPepExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 17, 1)
)
if mibBuilder.loadTexts:
    fsMIPbPepExtEntry.setStatus("current")


class _FsMIPbPepExtCosPreservation_Type(EnabledStatus):
    """Custom type fsMIPbPepExtCosPreservation based on EnabledStatus"""
    defaultValue = 2


_FsMIPbPepExtCosPreservation_Type.__name__ = "EnabledStatus"
_FsMIPbPepExtCosPreservation_Object = MibTableColumn
fsMIPbPepExtCosPreservation = _FsMIPbPepExtCosPreservation_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 17, 1, 1),
    _FsMIPbPepExtCosPreservation_Type()
)
fsMIPbPepExtCosPreservation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPbPepExtCosPreservation.setStatus("current")
_FsMIPbPortCVlanCounterTable_Object = MibTable
fsMIPbPortCVlanCounterTable = _FsMIPbPortCVlanCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 18)
)
if mibBuilder.loadTexts:
    fsMIPbPortCVlanCounterTable.setStatus("current")
_FsMIPbPortCVlanCounterEntry_Object = MibTableRow
fsMIPbPortCVlanCounterEntry = _FsMIPbPortCVlanCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 18, 1)
)
fsMIPbPortCVlanCounterEntry.setIndexNames(
    (0, "ARICENT-MIPROVIDERBRIDGE-MIB", "fsMIPbPortCVlanContextId"),
    (0, "ARICENT-MIPROVIDERBRIDGE-MIB", "fsMIPbPortCVlanPort"),
    (0, "ARICENT-MIPROVIDERBRIDGE-MIB", "fsMIPbPortCVlanIndex"),
)
if mibBuilder.loadTexts:
    fsMIPbPortCVlanCounterEntry.setStatus("current")


class _FsMIPbPortCVlanContextId_Type(Integer32):
    """Custom type fsMIPbPortCVlanContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIPbPortCVlanContextId_Type.__name__ = "Integer32"
_FsMIPbPortCVlanContextId_Object = MibTableColumn
fsMIPbPortCVlanContextId = _FsMIPbPortCVlanContextId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 18, 1, 1),
    _FsMIPbPortCVlanContextId_Type()
)
fsMIPbPortCVlanContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIPbPortCVlanContextId.setStatus("current")


class _FsMIPbPortCVlanPort_Type(Integer32):
    """Custom type fsMIPbPortCVlanPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMIPbPortCVlanPort_Type.__name__ = "Integer32"
_FsMIPbPortCVlanPort_Object = MibTableColumn
fsMIPbPortCVlanPort = _FsMIPbPortCVlanPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 18, 1, 2),
    _FsMIPbPortCVlanPort_Type()
)
fsMIPbPortCVlanPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbPortCVlanPort.setStatus("current")


class _FsMIPbPortCVlanIndex_Type(Unsigned32):
    """Custom type fsMIPbPortCVlanIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_FsMIPbPortCVlanIndex_Type.__name__ = "Unsigned32"
_FsMIPbPortCVlanIndex_Object = MibTableColumn
fsMIPbPortCVlanIndex = _FsMIPbPortCVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 18, 1, 3),
    _FsMIPbPortCVlanIndex_Type()
)
fsMIPbPortCVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbPortCVlanIndex.setStatus("current")
_FsMIPbPortCVlanCounterRxUcast_Type = Counter32
_FsMIPbPortCVlanCounterRxUcast_Object = MibTableColumn
fsMIPbPortCVlanCounterRxUcast = _FsMIPbPortCVlanCounterRxUcast_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 18, 1, 4),
    _FsMIPbPortCVlanCounterRxUcast_Type()
)
fsMIPbPortCVlanCounterRxUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbPortCVlanCounterRxUcast.setStatus("current")
_FsMIPbPortCVlanCounterRxFrames_Type = Counter32
_FsMIPbPortCVlanCounterRxFrames_Object = MibTableColumn
fsMIPbPortCVlanCounterRxFrames = _FsMIPbPortCVlanCounterRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 18, 1, 5),
    _FsMIPbPortCVlanCounterRxFrames_Type()
)
fsMIPbPortCVlanCounterRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbPortCVlanCounterRxFrames.setStatus("current")
_FsMIPbPortCVlanCounterRxBytes_Type = Counter32
_FsMIPbPortCVlanCounterRxBytes_Object = MibTableColumn
fsMIPbPortCVlanCounterRxBytes = _FsMIPbPortCVlanCounterRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 18, 1, 6),
    _FsMIPbPortCVlanCounterRxBytes_Type()
)
fsMIPbPortCVlanCounterRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbPortCVlanCounterRxBytes.setStatus("current")


class _FsMIPbPortCVlanCounterStatus_Type(EnabledStatus):
    """Custom type fsMIPbPortCVlanCounterStatus based on EnabledStatus"""
    defaultValue = 2


_FsMIPbPortCVlanCounterStatus_Type.__name__ = "EnabledStatus"
_FsMIPbPortCVlanCounterStatus_Object = MibTableColumn
fsMIPbPortCVlanCounterStatus = _FsMIPbPortCVlanCounterStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 18, 1, 7),
    _FsMIPbPortCVlanCounterStatus_Type()
)
fsMIPbPortCVlanCounterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPbPortCVlanCounterStatus.setStatus("current")


class _FsMIPbPortCVlanClearCounter_Type(TruthValue):
    """Custom type fsMIPbPortCVlanClearCounter based on TruthValue"""
    defaultValue = 2


_FsMIPbPortCVlanClearCounter_Type.__name__ = "TruthValue"
_FsMIPbPortCVlanClearCounter_Object = MibTableColumn
fsMIPbPortCVlanClearCounter = _FsMIPbPortCVlanClearCounter_Object(
    (1, 3, 6, 1, 4, 1, 2076, 127, 2, 18, 1, 8),
    _FsMIPbPortCVlanClearCounter_Type()
)
fsMIPbPortCVlanClearCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPbPortCVlanClearCounter.setStatus("current")
dot1adMIPepEntry.registerAugmentions(
    ("ARICENT-MIPROVIDERBRIDGE-MIB",
     "fsMIPbPepExtEntry")
)
fsMIPbPepExtEntry.setIndexNames(*dot1adMIPepEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-MIPROVIDERBRIDGE-MIB",
    **{"TunnelStatus": TunnelStatus,
       "futureMIProviderBridgeMIB": futureMIProviderBridgeMIB,
       "fsMIPbSystem": fsMIPbSystem,
       "fsMIPbContextInfoTable": fsMIPbContextInfoTable,
       "fsMIPbContextInfoEntry": fsMIPbContextInfoEntry,
       "fsMIPbContextId": fsMIPbContextId,
       "fsMIPbMulticastMacLimit": fsMIPbMulticastMacLimit,
       "fsMIPbTunnelStpAddress": fsMIPbTunnelStpAddress,
       "fsMIPbTunnelLacpAddress": fsMIPbTunnelLacpAddress,
       "fsMIPbTunnelDot1xAddress": fsMIPbTunnelDot1xAddress,
       "fsMIPbTunnelGvrpAddress": fsMIPbTunnelGvrpAddress,
       "fsMIPbTunnelGmrpAddress": fsMIPbTunnelGmrpAddress,
       "fsMIPbConfig": fsMIPbConfig,
       "fsMIPbPortInfoTable": fsMIPbPortInfoTable,
       "fsMIPbPortInfoEntry": fsMIPbPortInfoEntry,
       "fsMIPbPort": fsMIPbPort,
       "fsMIPbPortSVlanClassificationMethod": fsMIPbPortSVlanClassificationMethod,
       "fsMIPbPortSVlanIngressEtherType": fsMIPbPortSVlanIngressEtherType,
       "fsMIPbPortSVlanEgressEtherType": fsMIPbPortSVlanEgressEtherType,
       "fsMIPbPortSVlanEtherTypeSwapStatus": fsMIPbPortSVlanEtherTypeSwapStatus,
       "fsMIPbPortSVlanTranslationStatus": fsMIPbPortSVlanTranslationStatus,
       "fsMIPbPortUnicastMacLearning": fsMIPbPortUnicastMacLearning,
       "fsMIPbPortUnicastMacLimit": fsMIPbPortUnicastMacLimit,
       "fsMIPbPortBundleStatus": fsMIPbPortBundleStatus,
       "fsMIPbPortMultiplexStatus": fsMIPbPortMultiplexStatus,
       "fsMIPbSrcMacSVlanTable": fsMIPbSrcMacSVlanTable,
       "fsMIPbSrcMacSVlanEntry": fsMIPbSrcMacSVlanEntry,
       "fsMIPbSrcMacAddress": fsMIPbSrcMacAddress,
       "fsMIPbSrcMacSVlan": fsMIPbSrcMacSVlan,
       "fsMIPbSrcMacRowStatus": fsMIPbSrcMacRowStatus,
       "fsMIPbDstMacSVlanTable": fsMIPbDstMacSVlanTable,
       "fsMIPbDstMacSVlanEntry": fsMIPbDstMacSVlanEntry,
       "fsMIPbDstMacAddress": fsMIPbDstMacAddress,
       "fsMIPbDstMacSVlan": fsMIPbDstMacSVlan,
       "fsMIPbDstMacRowStatus": fsMIPbDstMacRowStatus,
       "fsMIPbCVlanSrcMacSVlanTable": fsMIPbCVlanSrcMacSVlanTable,
       "fsMIPbCVlanSrcMacSVlanEntry": fsMIPbCVlanSrcMacSVlanEntry,
       "fsMIPbCVlanSrcMacCVlan": fsMIPbCVlanSrcMacCVlan,
       "fsMIPbCVlanSrcMacAddr": fsMIPbCVlanSrcMacAddr,
       "fsMIPbCVlanSrcMacSVlan": fsMIPbCVlanSrcMacSVlan,
       "fsMIPbCVlanSrcMacRowStatus": fsMIPbCVlanSrcMacRowStatus,
       "fsMIPbCVlanDstMacSVlanTable": fsMIPbCVlanDstMacSVlanTable,
       "fsMIPbCVlanDstMacSVlanEntry": fsMIPbCVlanDstMacSVlanEntry,
       "fsMIPbCVlanDstMacCVlan": fsMIPbCVlanDstMacCVlan,
       "fsMIPbCVlanDstMacAddr": fsMIPbCVlanDstMacAddr,
       "fsMIPbCVlanDstMacSVlan": fsMIPbCVlanDstMacSVlan,
       "fsMIPbCVlanDstMacRowStatus": fsMIPbCVlanDstMacRowStatus,
       "fsMIPbDscpSVlanTable": fsMIPbDscpSVlanTable,
       "fsMIPbDscpSVlanEntry": fsMIPbDscpSVlanEntry,
       "fsMIPbDscp": fsMIPbDscp,
       "fsMIPbDscpSVlan": fsMIPbDscpSVlan,
       "fsMIPbDscpRowStatus": fsMIPbDscpRowStatus,
       "fsMIPbCVlanDscpSVlanTable": fsMIPbCVlanDscpSVlanTable,
       "fsMIPbCVlanDscpSVlanEntry": fsMIPbCVlanDscpSVlanEntry,
       "fsMIPbCVlanDscpCVlan": fsMIPbCVlanDscpCVlan,
       "fsMIPbCVlanDscp": fsMIPbCVlanDscp,
       "fsMIPbCVlanDscpSVlan": fsMIPbCVlanDscpSVlan,
       "fsMIPbCVlanDscpRowStatus": fsMIPbCVlanDscpRowStatus,
       "fsMIPbSrcIpAddrSVlanTable": fsMIPbSrcIpAddrSVlanTable,
       "fsMIPbSrcIpAddrSVlanEntry": fsMIPbSrcIpAddrSVlanEntry,
       "fsMIPbSrcIpAddr": fsMIPbSrcIpAddr,
       "fsMIPbSrcIpSVlan": fsMIPbSrcIpSVlan,
       "fsMIPbSrcIpRowStatus": fsMIPbSrcIpRowStatus,
       "fsMIPbDstIpAddrSVlanTable": fsMIPbDstIpAddrSVlanTable,
       "fsMIPbDstIpAddrSVlanEntry": fsMIPbDstIpAddrSVlanEntry,
       "fsMIPbDstIpAddr": fsMIPbDstIpAddr,
       "fsMIPbDstIpSVlan": fsMIPbDstIpSVlan,
       "fsMIPbDstIpRowStatus": fsMIPbDstIpRowStatus,
       "fsMIPbSrcDstIpSVlanTable": fsMIPbSrcDstIpSVlanTable,
       "fsMIPbSrcDstIpSVlanEntry": fsMIPbSrcDstIpSVlanEntry,
       "fsMIPbSrcDstSrcIpAddr": fsMIPbSrcDstSrcIpAddr,
       "fsMIPbSrcDstDstIpAddr": fsMIPbSrcDstDstIpAddr,
       "fsMIPbSrcDstIpSVlan": fsMIPbSrcDstIpSVlan,
       "fsMIPbSrcDstIpRowStatus": fsMIPbSrcDstIpRowStatus,
       "fsMIPbCVlanDstIpSVlanTable": fsMIPbCVlanDstIpSVlanTable,
       "fsMIPbCVlanDstIpSVlanEntry": fsMIPbCVlanDstIpSVlanEntry,
       "fsMIPbCVlanDstIpCVlan": fsMIPbCVlanDstIpCVlan,
       "fsMIPbCVlanDstIp": fsMIPbCVlanDstIp,
       "fsMIPbCVlanDstIpSVlan": fsMIPbCVlanDstIpSVlan,
       "fsMIPbCVlanDstIpRowStatus": fsMIPbCVlanDstIpRowStatus,
       "fsMIPbPortBasedCVlanTable": fsMIPbPortBasedCVlanTable,
       "fsMIPbPortBasedCVlanEntry": fsMIPbPortBasedCVlanEntry,
       "fsMIPbPortCVlan": fsMIPbPortCVlan,
       "fsMIPbPortCVlanClassifyStatus": fsMIPbPortCVlanClassifyStatus,
       "fsMIPbPortEgressUntaggedStatus": fsMIPbPortEgressUntaggedStatus,
       "fsMIPbEtherTypeSwapTable": fsMIPbEtherTypeSwapTable,
       "fsMIPbEtherTypeSwapEntry": fsMIPbEtherTypeSwapEntry,
       "fsMIPbLocalEtherType": fsMIPbLocalEtherType,
       "fsMIPbRelayEtherType": fsMIPbRelayEtherType,
       "fsMIPbEtherTypeSwapRowStatus": fsMIPbEtherTypeSwapRowStatus,
       "fsMIPbSVlanConfigTable": fsMIPbSVlanConfigTable,
       "fsMIPbSVlanConfigEntry": fsMIPbSVlanConfigEntry,
       "fsMIPbSVlanConfigServiceType": fsMIPbSVlanConfigServiceType,
       "fsMIPbTunnelProtocolTable": fsMIPbTunnelProtocolTable,
       "fsMIPbTunnelProtocolEntry": fsMIPbTunnelProtocolEntry,
       "fsMIPbTunnelProtocolDot1x": fsMIPbTunnelProtocolDot1x,
       "fsMIPbTunnelProtocolLacp": fsMIPbTunnelProtocolLacp,
       "fsMIPbTunnelProtocolStp": fsMIPbTunnelProtocolStp,
       "fsMIPbTunnelProtocolGvrp": fsMIPbTunnelProtocolGvrp,
       "fsMIPbTunnelProtocolGmrp": fsMIPbTunnelProtocolGmrp,
       "fsMIPbTunnelProtocolIgmp": fsMIPbTunnelProtocolIgmp,
       "fsMIPbTunnelProtocolStatsTable": fsMIPbTunnelProtocolStatsTable,
       "fsMIPbTunnelProtocolStatsEntry": fsMIPbTunnelProtocolStatsEntry,
       "fsMIPbTunnelProtocolDot1xPktsRecvd": fsMIPbTunnelProtocolDot1xPktsRecvd,
       "fsMIPbTunnelProtocolDot1xPktsSent": fsMIPbTunnelProtocolDot1xPktsSent,
       "fsMIPbTunnelProtocolLacpPktsRecvd": fsMIPbTunnelProtocolLacpPktsRecvd,
       "fsMIPbTunnelProtocolLacpPktsSent": fsMIPbTunnelProtocolLacpPktsSent,
       "fsMIPbTunnelProtocolStpPDUsRecvd": fsMIPbTunnelProtocolStpPDUsRecvd,
       "fsMIPbTunnelProtocolStpPDUsSent": fsMIPbTunnelProtocolStpPDUsSent,
       "fsMIPbTunnelProtocolGvrpPDUsRecvd": fsMIPbTunnelProtocolGvrpPDUsRecvd,
       "fsMIPbTunnelProtocolGvrpPDUsSent": fsMIPbTunnelProtocolGvrpPDUsSent,
       "fsMIPbTunnelProtocolGmrpPktsRecvd": fsMIPbTunnelProtocolGmrpPktsRecvd,
       "fsMIPbTunnelProtocolGmrpPktsSent": fsMIPbTunnelProtocolGmrpPktsSent,
       "fsMIPbTunnelProtocolIgmpPktsRecvd": fsMIPbTunnelProtocolIgmpPktsRecvd,
       "fsMIPbTunnelProtocolIgmpPktsSent": fsMIPbTunnelProtocolIgmpPktsSent,
       "fsMIPbPepExtTable": fsMIPbPepExtTable,
       "fsMIPbPepExtEntry": fsMIPbPepExtEntry,
       "fsMIPbPepExtCosPreservation": fsMIPbPepExtCosPreservation,
       "fsMIPbPortCVlanCounterTable": fsMIPbPortCVlanCounterTable,
       "fsMIPbPortCVlanCounterEntry": fsMIPbPortCVlanCounterEntry,
       "fsMIPbPortCVlanContextId": fsMIPbPortCVlanContextId,
       "fsMIPbPortCVlanPort": fsMIPbPortCVlanPort,
       "fsMIPbPortCVlanIndex": fsMIPbPortCVlanIndex,
       "fsMIPbPortCVlanCounterRxUcast": fsMIPbPortCVlanCounterRxUcast,
       "fsMIPbPortCVlanCounterRxFrames": fsMIPbPortCVlanCounterRxFrames,
       "fsMIPbPortCVlanCounterRxBytes": fsMIPbPortCVlanCounterRxBytes,
       "fsMIPbPortCVlanCounterStatus": fsMIPbPortCVlanCounterStatus,
       "fsMIPbPortCVlanClearCounter": fsMIPbPortCVlanClearCounter}
)
