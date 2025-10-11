# SNMP MIB module (SUPERMICRO-PROVIDERBRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-PROVIDERBRIDGE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:03:18 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(dot1adPepEntry,) = mibBuilder.importSymbols(
    "SUPERMICRO-DOT1AD-MIB",
    "dot1adPepEntry")


# MODULE-IDENTITY

futureProviderBridgeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113)
)
if mibBuilder.loadTexts:
    futureProviderBridgeMIB.setRevisions(
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

_FsPbSystem_ObjectIdentity = ObjectIdentity
fsPbSystem = _FsPbSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 1)
)


class _FsPbMulticastMacLimit_Type(Unsigned32):
    """Custom type fsPbMulticastMacLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsPbMulticastMacLimit_Type.__name__ = "Unsigned32"
_FsPbMulticastMacLimit_Object = MibScalar
fsPbMulticastMacLimit = _FsPbMulticastMacLimit_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 1, 1),
    _FsPbMulticastMacLimit_Type()
)
fsPbMulticastMacLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbMulticastMacLimit.setStatus("current")
_FsPbTunnelStpAddress_Type = MacAddress
_FsPbTunnelStpAddress_Object = MibScalar
fsPbTunnelStpAddress = _FsPbTunnelStpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 1, 2),
    _FsPbTunnelStpAddress_Type()
)
fsPbTunnelStpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbTunnelStpAddress.setStatus("deprecated")
_FsPbTunnelLacpAddress_Type = MacAddress
_FsPbTunnelLacpAddress_Object = MibScalar
fsPbTunnelLacpAddress = _FsPbTunnelLacpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 1, 3),
    _FsPbTunnelLacpAddress_Type()
)
fsPbTunnelLacpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbTunnelLacpAddress.setStatus("deprecated")
_FsPbTunnelDot1xAddress_Type = MacAddress
_FsPbTunnelDot1xAddress_Object = MibScalar
fsPbTunnelDot1xAddress = _FsPbTunnelDot1xAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 1, 4),
    _FsPbTunnelDot1xAddress_Type()
)
fsPbTunnelDot1xAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbTunnelDot1xAddress.setStatus("deprecated")
_FsPbTunnelGvrpAddress_Type = MacAddress
_FsPbTunnelGvrpAddress_Object = MibScalar
fsPbTunnelGvrpAddress = _FsPbTunnelGvrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 1, 5),
    _FsPbTunnelGvrpAddress_Type()
)
fsPbTunnelGvrpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbTunnelGvrpAddress.setStatus("deprecated")
_FsPbTunnelGmrpAddress_Type = MacAddress
_FsPbTunnelGmrpAddress_Object = MibScalar
fsPbTunnelGmrpAddress = _FsPbTunnelGmrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 1, 6),
    _FsPbTunnelGmrpAddress_Type()
)
fsPbTunnelGmrpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbTunnelGmrpAddress.setStatus("deprecated")
_FsPbConfig_ObjectIdentity = ObjectIdentity
fsPbConfig = _FsPbConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2)
)
_FsPbPortInfoTable_Object = MibTable
fsPbPortInfoTable = _FsPbPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 1)
)
if mibBuilder.loadTexts:
    fsPbPortInfoTable.setStatus("current")
_FsPbPortInfoEntry_Object = MibTableRow
fsPbPortInfoEntry = _FsPbPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 1, 1)
)
fsPbPortInfoEntry.setIndexNames(
    (0, "SUPERMICRO-PROVIDERBRIDGE-MIB", "fsPbPort"),
)
if mibBuilder.loadTexts:
    fsPbPortInfoEntry.setStatus("current")


class _FsPbPort_Type(Integer32):
    """Custom type fsPbPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsPbPort_Type.__name__ = "Integer32"
_FsPbPort_Object = MibTableColumn
fsPbPort = _FsPbPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 1, 1, 1),
    _FsPbPort_Type()
)
fsPbPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPbPort.setStatus("current")


class _FsPbPortSVlanClassificationMethod_Type(Integer32):
    """Custom type fsPbPortSVlanClassificationMethod based on Integer32"""
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


_FsPbPortSVlanClassificationMethod_Type.__name__ = "Integer32"
_FsPbPortSVlanClassificationMethod_Object = MibTableColumn
fsPbPortSVlanClassificationMethod = _FsPbPortSVlanClassificationMethod_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 1, 1, 2),
    _FsPbPortSVlanClassificationMethod_Type()
)
fsPbPortSVlanClassificationMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbPortSVlanClassificationMethod.setStatus("current")


class _FsPbPortSVlanIngressEtherType_Type(Integer32):
    """Custom type fsPbPortSVlanIngressEtherType based on Integer32"""
    defaultValue = 34984

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsPbPortSVlanIngressEtherType_Type.__name__ = "Integer32"
_FsPbPortSVlanIngressEtherType_Object = MibTableColumn
fsPbPortSVlanIngressEtherType = _FsPbPortSVlanIngressEtherType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 1, 1, 3),
    _FsPbPortSVlanIngressEtherType_Type()
)
fsPbPortSVlanIngressEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbPortSVlanIngressEtherType.setStatus("current")


class _FsPbPortSVlanEgressEtherType_Type(Integer32):
    """Custom type fsPbPortSVlanEgressEtherType based on Integer32"""
    defaultValue = 34984

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsPbPortSVlanEgressEtherType_Type.__name__ = "Integer32"
_FsPbPortSVlanEgressEtherType_Object = MibTableColumn
fsPbPortSVlanEgressEtherType = _FsPbPortSVlanEgressEtherType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 1, 1, 4),
    _FsPbPortSVlanEgressEtherType_Type()
)
fsPbPortSVlanEgressEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbPortSVlanEgressEtherType.setStatus("current")


class _FsPbPortSVlanEtherTypeSwapStatus_Type(EnabledStatus):
    """Custom type fsPbPortSVlanEtherTypeSwapStatus based on EnabledStatus"""
    defaultValue = 2


_FsPbPortSVlanEtherTypeSwapStatus_Type.__name__ = "EnabledStatus"
_FsPbPortSVlanEtherTypeSwapStatus_Object = MibTableColumn
fsPbPortSVlanEtherTypeSwapStatus = _FsPbPortSVlanEtherTypeSwapStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 1, 1, 5),
    _FsPbPortSVlanEtherTypeSwapStatus_Type()
)
fsPbPortSVlanEtherTypeSwapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbPortSVlanEtherTypeSwapStatus.setStatus("current")
_FsPbPortSVlanTranslationStatus_Type = EnabledStatus
_FsPbPortSVlanTranslationStatus_Object = MibTableColumn
fsPbPortSVlanTranslationStatus = _FsPbPortSVlanTranslationStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 1, 1, 6),
    _FsPbPortSVlanTranslationStatus_Type()
)
fsPbPortSVlanTranslationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbPortSVlanTranslationStatus.setStatus("current")


class _FsPbPortUnicastMacLearning_Type(EnabledStatus):
    """Custom type fsPbPortUnicastMacLearning based on EnabledStatus"""
    defaultValue = 1


_FsPbPortUnicastMacLearning_Type.__name__ = "EnabledStatus"
_FsPbPortUnicastMacLearning_Object = MibTableColumn
fsPbPortUnicastMacLearning = _FsPbPortUnicastMacLearning_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 1, 1, 7),
    _FsPbPortUnicastMacLearning_Type()
)
fsPbPortUnicastMacLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbPortUnicastMacLearning.setStatus("deprecated")


class _FsPbPortUnicastMacLimit_Type(Unsigned32):
    """Custom type fsPbPortUnicastMacLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsPbPortUnicastMacLimit_Type.__name__ = "Unsigned32"
_FsPbPortUnicastMacLimit_Object = MibTableColumn
fsPbPortUnicastMacLimit = _FsPbPortUnicastMacLimit_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 1, 1, 8),
    _FsPbPortUnicastMacLimit_Type()
)
fsPbPortUnicastMacLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbPortUnicastMacLimit.setStatus("current")


class _FsPbPortBundleStatus_Type(EnabledStatus):
    """Custom type fsPbPortBundleStatus based on EnabledStatus"""
    defaultValue = 1


_FsPbPortBundleStatus_Type.__name__ = "EnabledStatus"
_FsPbPortBundleStatus_Object = MibTableColumn
fsPbPortBundleStatus = _FsPbPortBundleStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 1, 1, 9),
    _FsPbPortBundleStatus_Type()
)
fsPbPortBundleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbPortBundleStatus.setStatus("current")


class _FsPbPortMultiplexStatus_Type(EnabledStatus):
    """Custom type fsPbPortMultiplexStatus based on EnabledStatus"""
    defaultValue = 1


_FsPbPortMultiplexStatus_Type.__name__ = "EnabledStatus"
_FsPbPortMultiplexStatus_Object = MibTableColumn
fsPbPortMultiplexStatus = _FsPbPortMultiplexStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 1, 1, 10),
    _FsPbPortMultiplexStatus_Type()
)
fsPbPortMultiplexStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbPortMultiplexStatus.setStatus("current")
_FsPbSrcMacSVlanTable_Object = MibTable
fsPbSrcMacSVlanTable = _FsPbSrcMacSVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 2)
)
if mibBuilder.loadTexts:
    fsPbSrcMacSVlanTable.setStatus("current")
_FsPbSrcMacSVlanEntry_Object = MibTableRow
fsPbSrcMacSVlanEntry = _FsPbSrcMacSVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 2, 1)
)
fsPbSrcMacSVlanEntry.setIndexNames(
    (0, "SUPERMICRO-PROVIDERBRIDGE-MIB", "fsPbPort"),
    (0, "SUPERMICRO-PROVIDERBRIDGE-MIB", "fsPbSrcMacAddress"),
)
if mibBuilder.loadTexts:
    fsPbSrcMacSVlanEntry.setStatus("current")
_FsPbSrcMacAddress_Type = MacAddress
_FsPbSrcMacAddress_Object = MibTableColumn
fsPbSrcMacAddress = _FsPbSrcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 2, 1, 1),
    _FsPbSrcMacAddress_Type()
)
fsPbSrcMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPbSrcMacAddress.setStatus("current")
_FsPbSrcMacSVlan_Type = VlanId
_FsPbSrcMacSVlan_Object = MibTableColumn
fsPbSrcMacSVlan = _FsPbSrcMacSVlan_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 2, 1, 2),
    _FsPbSrcMacSVlan_Type()
)
fsPbSrcMacSVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbSrcMacSVlan.setStatus("current")
_FsPbSrcMacRowStatus_Type = RowStatus
_FsPbSrcMacRowStatus_Object = MibTableColumn
fsPbSrcMacRowStatus = _FsPbSrcMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 2, 1, 3),
    _FsPbSrcMacRowStatus_Type()
)
fsPbSrcMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPbSrcMacRowStatus.setStatus("current")
_FsPbDstMacSVlanTable_Object = MibTable
fsPbDstMacSVlanTable = _FsPbDstMacSVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 3)
)
if mibBuilder.loadTexts:
    fsPbDstMacSVlanTable.setStatus("current")
_FsPbDstMacSVlanEntry_Object = MibTableRow
fsPbDstMacSVlanEntry = _FsPbDstMacSVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 3, 1)
)
fsPbDstMacSVlanEntry.setIndexNames(
    (0, "SUPERMICRO-PROVIDERBRIDGE-MIB", "fsPbPort"),
    (0, "SUPERMICRO-PROVIDERBRIDGE-MIB", "fsPbDstMacAddress"),
)
if mibBuilder.loadTexts:
    fsPbDstMacSVlanEntry.setStatus("current")
_FsPbDstMacAddress_Type = MacAddress
_FsPbDstMacAddress_Object = MibTableColumn
fsPbDstMacAddress = _FsPbDstMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 3, 1, 1),
    _FsPbDstMacAddress_Type()
)
fsPbDstMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPbDstMacAddress.setStatus("current")
_FsPbDstMacSVlan_Type = VlanId
_FsPbDstMacSVlan_Object = MibTableColumn
fsPbDstMacSVlan = _FsPbDstMacSVlan_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 3, 1, 2),
    _FsPbDstMacSVlan_Type()
)
fsPbDstMacSVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbDstMacSVlan.setStatus("current")
_FsPbDstMacRowStatus_Type = RowStatus
_FsPbDstMacRowStatus_Object = MibTableColumn
fsPbDstMacRowStatus = _FsPbDstMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 3, 1, 3),
    _FsPbDstMacRowStatus_Type()
)
fsPbDstMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPbDstMacRowStatus.setStatus("current")
_FsPbCVlanSrcMacSVlanTable_Object = MibTable
fsPbCVlanSrcMacSVlanTable = _FsPbCVlanSrcMacSVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 4)
)
if mibBuilder.loadTexts:
    fsPbCVlanSrcMacSVlanTable.setStatus("current")
_FsPbCVlanSrcMacSVlanEntry_Object = MibTableRow
fsPbCVlanSrcMacSVlanEntry = _FsPbCVlanSrcMacSVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 4, 1)
)
fsPbCVlanSrcMacSVlanEntry.setIndexNames(
    (0, "SUPERMICRO-PROVIDERBRIDGE-MIB", "fsPbPort"),
    (0, "SUPERMICRO-PROVIDERBRIDGE-MIB", "fsPbCVlanSrcMacCVlan"),
    (0, "SUPERMICRO-PROVIDERBRIDGE-MIB", "fsPbCVlanSrcMacAddr"),
)
if mibBuilder.loadTexts:
    fsPbCVlanSrcMacSVlanEntry.setStatus("current")
_FsPbCVlanSrcMacCVlan_Type = VlanId
_FsPbCVlanSrcMacCVlan_Object = MibTableColumn
fsPbCVlanSrcMacCVlan = _FsPbCVlanSrcMacCVlan_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 4, 1, 1),
    _FsPbCVlanSrcMacCVlan_Type()
)
fsPbCVlanSrcMacCVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPbCVlanSrcMacCVlan.setStatus("current")
_FsPbCVlanSrcMacAddr_Type = MacAddress
_FsPbCVlanSrcMacAddr_Object = MibTableColumn
fsPbCVlanSrcMacAddr = _FsPbCVlanSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 4, 1, 2),
    _FsPbCVlanSrcMacAddr_Type()
)
fsPbCVlanSrcMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPbCVlanSrcMacAddr.setStatus("current")
_FsPbCVlanSrcMacSVlan_Type = VlanId
_FsPbCVlanSrcMacSVlan_Object = MibTableColumn
fsPbCVlanSrcMacSVlan = _FsPbCVlanSrcMacSVlan_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 4, 1, 3),
    _FsPbCVlanSrcMacSVlan_Type()
)
fsPbCVlanSrcMacSVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbCVlanSrcMacSVlan.setStatus("current")
_FsPbCVlanSrcMacRowStatus_Type = RowStatus
_FsPbCVlanSrcMacRowStatus_Object = MibTableColumn
fsPbCVlanSrcMacRowStatus = _FsPbCVlanSrcMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 4, 1, 4),
    _FsPbCVlanSrcMacRowStatus_Type()
)
fsPbCVlanSrcMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPbCVlanSrcMacRowStatus.setStatus("current")
_FsPbCVlanDstMacSVlanTable_Object = MibTable
fsPbCVlanDstMacSVlanTable = _FsPbCVlanDstMacSVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 5)
)
if mibBuilder.loadTexts:
    fsPbCVlanDstMacSVlanTable.setStatus("current")
_FsPbCVlanDstMacSVlanEntry_Object = MibTableRow
fsPbCVlanDstMacSVlanEntry = _FsPbCVlanDstMacSVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 5, 1)
)
fsPbCVlanDstMacSVlanEntry.setIndexNames(
    (0, "SUPERMICRO-PROVIDERBRIDGE-MIB", "fsPbPort"),
    (0, "SUPERMICRO-PROVIDERBRIDGE-MIB", "fsPbCVlanDstMacCVlan"),
    (0, "SUPERMICRO-PROVIDERBRIDGE-MIB", "fsPbCVlanDstMacAddr"),
)
if mibBuilder.loadTexts:
    fsPbCVlanDstMacSVlanEntry.setStatus("current")
_FsPbCVlanDstMacCVlan_Type = VlanId
_FsPbCVlanDstMacCVlan_Object = MibTableColumn
fsPbCVlanDstMacCVlan = _FsPbCVlanDstMacCVlan_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 5, 1, 1),
    _FsPbCVlanDstMacCVlan_Type()
)
fsPbCVlanDstMacCVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPbCVlanDstMacCVlan.setStatus("current")
_FsPbCVlanDstMacAddr_Type = MacAddress
_FsPbCVlanDstMacAddr_Object = MibTableColumn
fsPbCVlanDstMacAddr = _FsPbCVlanDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 5, 1, 2),
    _FsPbCVlanDstMacAddr_Type()
)
fsPbCVlanDstMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPbCVlanDstMacAddr.setStatus("current")
_FsPbCVlanDstMacSVlan_Type = VlanId
_FsPbCVlanDstMacSVlan_Object = MibTableColumn
fsPbCVlanDstMacSVlan = _FsPbCVlanDstMacSVlan_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 5, 1, 3),
    _FsPbCVlanDstMacSVlan_Type()
)
fsPbCVlanDstMacSVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbCVlanDstMacSVlan.setStatus("current")
_FsPbCVlanDstMacRowStatus_Type = RowStatus
_FsPbCVlanDstMacRowStatus_Object = MibTableColumn
fsPbCVlanDstMacRowStatus = _FsPbCVlanDstMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 5, 1, 4),
    _FsPbCVlanDstMacRowStatus_Type()
)
fsPbCVlanDstMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPbCVlanDstMacRowStatus.setStatus("current")
_FsPbDscpSVlanTable_Object = MibTable
fsPbDscpSVlanTable = _FsPbDscpSVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 6)
)
if mibBuilder.loadTexts:
    fsPbDscpSVlanTable.setStatus("current")
_FsPbDscpSVlanEntry_Object = MibTableRow
fsPbDscpSVlanEntry = _FsPbDscpSVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 6, 1)
)
fsPbDscpSVlanEntry.setIndexNames(
    (0, "SUPERMICRO-PROVIDERBRIDGE-MIB", "fsPbPort"),
    (0, "SUPERMICRO-PROVIDERBRIDGE-MIB", "fsPbDscp"),
)
if mibBuilder.loadTexts:
    fsPbDscpSVlanEntry.setStatus("current")


class _FsPbDscp_Type(Integer32):
    """Custom type fsPbDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_FsPbDscp_Type.__name__ = "Integer32"
_FsPbDscp_Object = MibTableColumn
fsPbDscp = _FsPbDscp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 6, 1, 1),
    _FsPbDscp_Type()
)
fsPbDscp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPbDscp.setStatus("current")
_FsPbDscpSVlan_Type = VlanId
_FsPbDscpSVlan_Object = MibTableColumn
fsPbDscpSVlan = _FsPbDscpSVlan_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 6, 1, 2),
    _FsPbDscpSVlan_Type()
)
fsPbDscpSVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbDscpSVlan.setStatus("current")
_FsPbDscpRowStatus_Type = RowStatus
_FsPbDscpRowStatus_Object = MibTableColumn
fsPbDscpRowStatus = _FsPbDscpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 6, 1, 3),
    _FsPbDscpRowStatus_Type()
)
fsPbDscpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPbDscpRowStatus.setStatus("current")
_FsPbCVlanDscpSVlanTable_Object = MibTable
fsPbCVlanDscpSVlanTable = _FsPbCVlanDscpSVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 7)
)
if mibBuilder.loadTexts:
    fsPbCVlanDscpSVlanTable.setStatus("current")
_FsPbCVlanDscpSVlanEntry_Object = MibTableRow
fsPbCVlanDscpSVlanEntry = _FsPbCVlanDscpSVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 7, 1)
)
fsPbCVlanDscpSVlanEntry.setIndexNames(
    (0, "SUPERMICRO-PROVIDERBRIDGE-MIB", "fsPbPort"),
    (0, "SUPERMICRO-PROVIDERBRIDGE-MIB", "fsPbCVlanDscpCVlan"),
    (0, "SUPERMICRO-PROVIDERBRIDGE-MIB", "fsPbCVlanDscp"),
)
if mibBuilder.loadTexts:
    fsPbCVlanDscpSVlanEntry.setStatus("current")
_FsPbCVlanDscpCVlan_Type = VlanId
_FsPbCVlanDscpCVlan_Object = MibTableColumn
fsPbCVlanDscpCVlan = _FsPbCVlanDscpCVlan_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 7, 1, 1),
    _FsPbCVlanDscpCVlan_Type()
)
fsPbCVlanDscpCVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPbCVlanDscpCVlan.setStatus("current")


class _FsPbCVlanDscp_Type(Integer32):
    """Custom type fsPbCVlanDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_FsPbCVlanDscp_Type.__name__ = "Integer32"
_FsPbCVlanDscp_Object = MibTableColumn
fsPbCVlanDscp = _FsPbCVlanDscp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 7, 1, 2),
    _FsPbCVlanDscp_Type()
)
fsPbCVlanDscp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPbCVlanDscp.setStatus("current")
_FsPbCVlanDscpSVlan_Type = VlanId
_FsPbCVlanDscpSVlan_Object = MibTableColumn
fsPbCVlanDscpSVlan = _FsPbCVlanDscpSVlan_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 7, 1, 3),
    _FsPbCVlanDscpSVlan_Type()
)
fsPbCVlanDscpSVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbCVlanDscpSVlan.setStatus("current")
_FsPbCVlanDscpRowStatus_Type = RowStatus
_FsPbCVlanDscpRowStatus_Object = MibTableColumn
fsPbCVlanDscpRowStatus = _FsPbCVlanDscpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 7, 1, 4),
    _FsPbCVlanDscpRowStatus_Type()
)
fsPbCVlanDscpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPbCVlanDscpRowStatus.setStatus("current")
_FsPbSrcIpAddrSVlanTable_Object = MibTable
fsPbSrcIpAddrSVlanTable = _FsPbSrcIpAddrSVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 8)
)
if mibBuilder.loadTexts:
    fsPbSrcIpAddrSVlanTable.setStatus("current")
_FsPbSrcIpAddrSVlanEntry_Object = MibTableRow
fsPbSrcIpAddrSVlanEntry = _FsPbSrcIpAddrSVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 8, 1)
)
fsPbSrcIpAddrSVlanEntry.setIndexNames(
    (0, "SUPERMICRO-PROVIDERBRIDGE-MIB", "fsPbPort"),
    (0, "SUPERMICRO-PROVIDERBRIDGE-MIB", "fsPbSrcIpAddr"),
)
if mibBuilder.loadTexts:
    fsPbSrcIpAddrSVlanEntry.setStatus("current")
_FsPbSrcIpAddr_Type = IpAddress
_FsPbSrcIpAddr_Object = MibTableColumn
fsPbSrcIpAddr = _FsPbSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 8, 1, 1),
    _FsPbSrcIpAddr_Type()
)
fsPbSrcIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPbSrcIpAddr.setStatus("current")
_FsPbSrcIpSVlan_Type = VlanId
_FsPbSrcIpSVlan_Object = MibTableColumn
fsPbSrcIpSVlan = _FsPbSrcIpSVlan_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 8, 1, 2),
    _FsPbSrcIpSVlan_Type()
)
fsPbSrcIpSVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbSrcIpSVlan.setStatus("current")
_FsPbSrcIpRowStatus_Type = RowStatus
_FsPbSrcIpRowStatus_Object = MibTableColumn
fsPbSrcIpRowStatus = _FsPbSrcIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 8, 1, 3),
    _FsPbSrcIpRowStatus_Type()
)
fsPbSrcIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPbSrcIpRowStatus.setStatus("current")
_FsPbDstIpAddrSVlanTable_Object = MibTable
fsPbDstIpAddrSVlanTable = _FsPbDstIpAddrSVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 9)
)
if mibBuilder.loadTexts:
    fsPbDstIpAddrSVlanTable.setStatus("current")
_FsPbDstIpAddrSVlanEntry_Object = MibTableRow
fsPbDstIpAddrSVlanEntry = _FsPbDstIpAddrSVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 9, 1)
)
fsPbDstIpAddrSVlanEntry.setIndexNames(
    (0, "SUPERMICRO-PROVIDERBRIDGE-MIB", "fsPbPort"),
    (0, "SUPERMICRO-PROVIDERBRIDGE-MIB", "fsPbDstIpAddr"),
)
if mibBuilder.loadTexts:
    fsPbDstIpAddrSVlanEntry.setStatus("current")
_FsPbDstIpAddr_Type = IpAddress
_FsPbDstIpAddr_Object = MibTableColumn
fsPbDstIpAddr = _FsPbDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 9, 1, 1),
    _FsPbDstIpAddr_Type()
)
fsPbDstIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPbDstIpAddr.setStatus("current")
_FsPbDstIpSVlan_Type = VlanId
_FsPbDstIpSVlan_Object = MibTableColumn
fsPbDstIpSVlan = _FsPbDstIpSVlan_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 9, 1, 2),
    _FsPbDstIpSVlan_Type()
)
fsPbDstIpSVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbDstIpSVlan.setStatus("current")
_FsPbDstIpRowStatus_Type = RowStatus
_FsPbDstIpRowStatus_Object = MibTableColumn
fsPbDstIpRowStatus = _FsPbDstIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 9, 1, 3),
    _FsPbDstIpRowStatus_Type()
)
fsPbDstIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPbDstIpRowStatus.setStatus("current")
_FsPbSrcDstIpSVlanTable_Object = MibTable
fsPbSrcDstIpSVlanTable = _FsPbSrcDstIpSVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 10)
)
if mibBuilder.loadTexts:
    fsPbSrcDstIpSVlanTable.setStatus("current")
_FsPbSrcDstIpSVlanEntry_Object = MibTableRow
fsPbSrcDstIpSVlanEntry = _FsPbSrcDstIpSVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 10, 1)
)
fsPbSrcDstIpSVlanEntry.setIndexNames(
    (0, "SUPERMICRO-PROVIDERBRIDGE-MIB", "fsPbPort"),
    (0, "SUPERMICRO-PROVIDERBRIDGE-MIB", "fsPbSrcDstSrcIpAddr"),
    (0, "SUPERMICRO-PROVIDERBRIDGE-MIB", "fsPbSrcDstDstIpAddr"),
)
if mibBuilder.loadTexts:
    fsPbSrcDstIpSVlanEntry.setStatus("current")
_FsPbSrcDstSrcIpAddr_Type = IpAddress
_FsPbSrcDstSrcIpAddr_Object = MibTableColumn
fsPbSrcDstSrcIpAddr = _FsPbSrcDstSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 10, 1, 1),
    _FsPbSrcDstSrcIpAddr_Type()
)
fsPbSrcDstSrcIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPbSrcDstSrcIpAddr.setStatus("current")
_FsPbSrcDstDstIpAddr_Type = IpAddress
_FsPbSrcDstDstIpAddr_Object = MibTableColumn
fsPbSrcDstDstIpAddr = _FsPbSrcDstDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 10, 1, 2),
    _FsPbSrcDstDstIpAddr_Type()
)
fsPbSrcDstDstIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPbSrcDstDstIpAddr.setStatus("current")
_FsPbSrcDstIpSVlan_Type = VlanId
_FsPbSrcDstIpSVlan_Object = MibTableColumn
fsPbSrcDstIpSVlan = _FsPbSrcDstIpSVlan_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 10, 1, 3),
    _FsPbSrcDstIpSVlan_Type()
)
fsPbSrcDstIpSVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbSrcDstIpSVlan.setStatus("current")
_FsPbSrcDstIpRowStatus_Type = RowStatus
_FsPbSrcDstIpRowStatus_Object = MibTableColumn
fsPbSrcDstIpRowStatus = _FsPbSrcDstIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 10, 1, 4),
    _FsPbSrcDstIpRowStatus_Type()
)
fsPbSrcDstIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPbSrcDstIpRowStatus.setStatus("current")
_FsPbCVlanDstIpSVlanTable_Object = MibTable
fsPbCVlanDstIpSVlanTable = _FsPbCVlanDstIpSVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 11)
)
if mibBuilder.loadTexts:
    fsPbCVlanDstIpSVlanTable.setStatus("current")
_FsPbCVlanDstIpSVlanEntry_Object = MibTableRow
fsPbCVlanDstIpSVlanEntry = _FsPbCVlanDstIpSVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 11, 1)
)
fsPbCVlanDstIpSVlanEntry.setIndexNames(
    (0, "SUPERMICRO-PROVIDERBRIDGE-MIB", "fsPbPort"),
    (0, "SUPERMICRO-PROVIDERBRIDGE-MIB", "fsPbCVlanDstIpCVlan"),
    (0, "SUPERMICRO-PROVIDERBRIDGE-MIB", "fsPbCVlanDstIp"),
)
if mibBuilder.loadTexts:
    fsPbCVlanDstIpSVlanEntry.setStatus("current")
_FsPbCVlanDstIpCVlan_Type = VlanId
_FsPbCVlanDstIpCVlan_Object = MibTableColumn
fsPbCVlanDstIpCVlan = _FsPbCVlanDstIpCVlan_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 11, 1, 1),
    _FsPbCVlanDstIpCVlan_Type()
)
fsPbCVlanDstIpCVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPbCVlanDstIpCVlan.setStatus("current")
_FsPbCVlanDstIp_Type = IpAddress
_FsPbCVlanDstIp_Object = MibTableColumn
fsPbCVlanDstIp = _FsPbCVlanDstIp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 11, 1, 2),
    _FsPbCVlanDstIp_Type()
)
fsPbCVlanDstIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPbCVlanDstIp.setStatus("current")
_FsPbCVlanDstIpSVlan_Type = VlanId
_FsPbCVlanDstIpSVlan_Object = MibTableColumn
fsPbCVlanDstIpSVlan = _FsPbCVlanDstIpSVlan_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 11, 1, 3),
    _FsPbCVlanDstIpSVlan_Type()
)
fsPbCVlanDstIpSVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbCVlanDstIpSVlan.setStatus("current")
_FsPbCVlanDstIpRowStatus_Type = RowStatus
_FsPbCVlanDstIpRowStatus_Object = MibTableColumn
fsPbCVlanDstIpRowStatus = _FsPbCVlanDstIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 11, 1, 4),
    _FsPbCVlanDstIpRowStatus_Type()
)
fsPbCVlanDstIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPbCVlanDstIpRowStatus.setStatus("current")
_FsPbPortBasedCVlanTable_Object = MibTable
fsPbPortBasedCVlanTable = _FsPbPortBasedCVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 12)
)
if mibBuilder.loadTexts:
    fsPbPortBasedCVlanTable.setStatus("current")
_FsPbPortBasedCVlanEntry_Object = MibTableRow
fsPbPortBasedCVlanEntry = _FsPbPortBasedCVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 12, 1)
)
fsPbPortBasedCVlanEntry.setIndexNames(
    (0, "SUPERMICRO-PROVIDERBRIDGE-MIB", "fsPbPort"),
)
if mibBuilder.loadTexts:
    fsPbPortBasedCVlanEntry.setStatus("current")
_FsPbPortCVlan_Type = VlanId
_FsPbPortCVlan_Object = MibTableColumn
fsPbPortCVlan = _FsPbPortCVlan_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 12, 1, 1),
    _FsPbPortCVlan_Type()
)
fsPbPortCVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbPortCVlan.setStatus("current")


class _FsPbPortCVlanClassifyStatus_Type(EnabledStatus):
    """Custom type fsPbPortCVlanClassifyStatus based on EnabledStatus"""
    defaultValue = 1


_FsPbPortCVlanClassifyStatus_Type.__name__ = "EnabledStatus"
_FsPbPortCVlanClassifyStatus_Object = MibTableColumn
fsPbPortCVlanClassifyStatus = _FsPbPortCVlanClassifyStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 12, 1, 2),
    _FsPbPortCVlanClassifyStatus_Type()
)
fsPbPortCVlanClassifyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbPortCVlanClassifyStatus.setStatus("current")
_FsPbEtherTypeSwapTable_Object = MibTable
fsPbEtherTypeSwapTable = _FsPbEtherTypeSwapTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 13)
)
if mibBuilder.loadTexts:
    fsPbEtherTypeSwapTable.setStatus("current")
_FsPbEtherTypeSwapEntry_Object = MibTableRow
fsPbEtherTypeSwapEntry = _FsPbEtherTypeSwapEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 13, 1)
)
fsPbEtherTypeSwapEntry.setIndexNames(
    (0, "SUPERMICRO-PROVIDERBRIDGE-MIB", "fsPbPort"),
    (0, "SUPERMICRO-PROVIDERBRIDGE-MIB", "fsPbLocalEtherType"),
)
if mibBuilder.loadTexts:
    fsPbEtherTypeSwapEntry.setStatus("current")


class _FsPbLocalEtherType_Type(Integer32):
    """Custom type fsPbLocalEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsPbLocalEtherType_Type.__name__ = "Integer32"
_FsPbLocalEtherType_Object = MibTableColumn
fsPbLocalEtherType = _FsPbLocalEtherType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 13, 1, 1),
    _FsPbLocalEtherType_Type()
)
fsPbLocalEtherType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPbLocalEtherType.setStatus("current")


class _FsPbRelayEtherType_Type(Integer32):
    """Custom type fsPbRelayEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsPbRelayEtherType_Type.__name__ = "Integer32"
_FsPbRelayEtherType_Object = MibTableColumn
fsPbRelayEtherType = _FsPbRelayEtherType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 13, 1, 2),
    _FsPbRelayEtherType_Type()
)
fsPbRelayEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbRelayEtherType.setStatus("current")
_FsPbEtherTypeSwapRowStatus_Type = RowStatus
_FsPbEtherTypeSwapRowStatus_Object = MibTableColumn
fsPbEtherTypeSwapRowStatus = _FsPbEtherTypeSwapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 13, 1, 3),
    _FsPbEtherTypeSwapRowStatus_Type()
)
fsPbEtherTypeSwapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPbEtherTypeSwapRowStatus.setStatus("current")
_FsPbSVlanConfigTable_Object = MibTable
fsPbSVlanConfigTable = _FsPbSVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 14)
)
if mibBuilder.loadTexts:
    fsPbSVlanConfigTable.setStatus("current")
_FsPbSVlanConfigEntry_Object = MibTableRow
fsPbSVlanConfigEntry = _FsPbSVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 14, 1)
)
fsPbSVlanConfigEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    fsPbSVlanConfigEntry.setStatus("current")


class _FsPbSVlanConfigServiceType_Type(Integer32):
    """Custom type fsPbSVlanConfigServiceType based on Integer32"""
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


_FsPbSVlanConfigServiceType_Type.__name__ = "Integer32"
_FsPbSVlanConfigServiceType_Object = MibTableColumn
fsPbSVlanConfigServiceType = _FsPbSVlanConfigServiceType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 14, 1, 1),
    _FsPbSVlanConfigServiceType_Type()
)
fsPbSVlanConfigServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbSVlanConfigServiceType.setStatus("current")
_FsPbTunnelProtocolTable_Object = MibTable
fsPbTunnelProtocolTable = _FsPbTunnelProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 15)
)
if mibBuilder.loadTexts:
    fsPbTunnelProtocolTable.setStatus("deprecated")
_FsPbTunnelProtocolEntry_Object = MibTableRow
fsPbTunnelProtocolEntry = _FsPbTunnelProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 15, 1)
)
fsPbTunnelProtocolEntry.setIndexNames(
    (0, "SUPERMICRO-PROVIDERBRIDGE-MIB", "fsPbPort"),
)
if mibBuilder.loadTexts:
    fsPbTunnelProtocolEntry.setStatus("deprecated")
_FsPbTunnelProtocolDot1x_Type = TunnelStatus
_FsPbTunnelProtocolDot1x_Object = MibTableColumn
fsPbTunnelProtocolDot1x = _FsPbTunnelProtocolDot1x_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 15, 1, 1),
    _FsPbTunnelProtocolDot1x_Type()
)
fsPbTunnelProtocolDot1x.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbTunnelProtocolDot1x.setStatus("deprecated")
_FsPbTunnelProtocolLacp_Type = TunnelStatus
_FsPbTunnelProtocolLacp_Object = MibTableColumn
fsPbTunnelProtocolLacp = _FsPbTunnelProtocolLacp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 15, 1, 2),
    _FsPbTunnelProtocolLacp_Type()
)
fsPbTunnelProtocolLacp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbTunnelProtocolLacp.setStatus("deprecated")
_FsPbTunnelProtocolStp_Type = TunnelStatus
_FsPbTunnelProtocolStp_Object = MibTableColumn
fsPbTunnelProtocolStp = _FsPbTunnelProtocolStp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 15, 1, 3),
    _FsPbTunnelProtocolStp_Type()
)
fsPbTunnelProtocolStp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbTunnelProtocolStp.setStatus("deprecated")
_FsPbTunnelProtocolGvrp_Type = TunnelStatus
_FsPbTunnelProtocolGvrp_Object = MibTableColumn
fsPbTunnelProtocolGvrp = _FsPbTunnelProtocolGvrp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 15, 1, 4),
    _FsPbTunnelProtocolGvrp_Type()
)
fsPbTunnelProtocolGvrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbTunnelProtocolGvrp.setStatus("deprecated")
_FsPbTunnelProtocolGmrp_Type = TunnelStatus
_FsPbTunnelProtocolGmrp_Object = MibTableColumn
fsPbTunnelProtocolGmrp = _FsPbTunnelProtocolGmrp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 15, 1, 5),
    _FsPbTunnelProtocolGmrp_Type()
)
fsPbTunnelProtocolGmrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbTunnelProtocolGmrp.setStatus("deprecated")
_FsPbTunnelProtocolIgmp_Type = TunnelStatus
_FsPbTunnelProtocolIgmp_Object = MibTableColumn
fsPbTunnelProtocolIgmp = _FsPbTunnelProtocolIgmp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 15, 1, 6),
    _FsPbTunnelProtocolIgmp_Type()
)
fsPbTunnelProtocolIgmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbTunnelProtocolIgmp.setStatus("deprecated")
_FsPbTunnelProtocolStatsTable_Object = MibTable
fsPbTunnelProtocolStatsTable = _FsPbTunnelProtocolStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 16)
)
if mibBuilder.loadTexts:
    fsPbTunnelProtocolStatsTable.setStatus("deprecated")
_FsPbTunnelProtocolStatsEntry_Object = MibTableRow
fsPbTunnelProtocolStatsEntry = _FsPbTunnelProtocolStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 16, 1)
)
fsPbTunnelProtocolStatsEntry.setIndexNames(
    (0, "SUPERMICRO-PROVIDERBRIDGE-MIB", "fsPbPort"),
)
if mibBuilder.loadTexts:
    fsPbTunnelProtocolStatsEntry.setStatus("deprecated")
_FsPbTunnelProtocolDot1xPktsRecvd_Type = Counter32
_FsPbTunnelProtocolDot1xPktsRecvd_Object = MibTableColumn
fsPbTunnelProtocolDot1xPktsRecvd = _FsPbTunnelProtocolDot1xPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 16, 1, 1),
    _FsPbTunnelProtocolDot1xPktsRecvd_Type()
)
fsPbTunnelProtocolDot1xPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbTunnelProtocolDot1xPktsRecvd.setStatus("deprecated")
_FsPbTunnelProtocolDot1xPktsSent_Type = Counter32
_FsPbTunnelProtocolDot1xPktsSent_Object = MibTableColumn
fsPbTunnelProtocolDot1xPktsSent = _FsPbTunnelProtocolDot1xPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 16, 1, 2),
    _FsPbTunnelProtocolDot1xPktsSent_Type()
)
fsPbTunnelProtocolDot1xPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbTunnelProtocolDot1xPktsSent.setStatus("deprecated")
_FsPbTunnelProtocolLacpPktsRecvd_Type = Counter32
_FsPbTunnelProtocolLacpPktsRecvd_Object = MibTableColumn
fsPbTunnelProtocolLacpPktsRecvd = _FsPbTunnelProtocolLacpPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 16, 1, 3),
    _FsPbTunnelProtocolLacpPktsRecvd_Type()
)
fsPbTunnelProtocolLacpPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbTunnelProtocolLacpPktsRecvd.setStatus("deprecated")
_FsPbTunnelProtocolLacpPktsSent_Type = Counter32
_FsPbTunnelProtocolLacpPktsSent_Object = MibTableColumn
fsPbTunnelProtocolLacpPktsSent = _FsPbTunnelProtocolLacpPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 16, 1, 4),
    _FsPbTunnelProtocolLacpPktsSent_Type()
)
fsPbTunnelProtocolLacpPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbTunnelProtocolLacpPktsSent.setStatus("deprecated")
_FsPbTunnelProtocolStpPDUsRecvd_Type = Counter32
_FsPbTunnelProtocolStpPDUsRecvd_Object = MibTableColumn
fsPbTunnelProtocolStpPDUsRecvd = _FsPbTunnelProtocolStpPDUsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 16, 1, 5),
    _FsPbTunnelProtocolStpPDUsRecvd_Type()
)
fsPbTunnelProtocolStpPDUsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbTunnelProtocolStpPDUsRecvd.setStatus("deprecated")
_FsPbTunnelProtocolStpPDUsSent_Type = Counter32
_FsPbTunnelProtocolStpPDUsSent_Object = MibTableColumn
fsPbTunnelProtocolStpPDUsSent = _FsPbTunnelProtocolStpPDUsSent_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 16, 1, 6),
    _FsPbTunnelProtocolStpPDUsSent_Type()
)
fsPbTunnelProtocolStpPDUsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbTunnelProtocolStpPDUsSent.setStatus("deprecated")
_FsPbTunnelProtocolGvrpPDUsRecvd_Type = Counter32
_FsPbTunnelProtocolGvrpPDUsRecvd_Object = MibTableColumn
fsPbTunnelProtocolGvrpPDUsRecvd = _FsPbTunnelProtocolGvrpPDUsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 16, 1, 7),
    _FsPbTunnelProtocolGvrpPDUsRecvd_Type()
)
fsPbTunnelProtocolGvrpPDUsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbTunnelProtocolGvrpPDUsRecvd.setStatus("deprecated")
_FsPbTunnelProtocolGvrpPDUsSent_Type = Counter32
_FsPbTunnelProtocolGvrpPDUsSent_Object = MibTableColumn
fsPbTunnelProtocolGvrpPDUsSent = _FsPbTunnelProtocolGvrpPDUsSent_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 16, 1, 8),
    _FsPbTunnelProtocolGvrpPDUsSent_Type()
)
fsPbTunnelProtocolGvrpPDUsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbTunnelProtocolGvrpPDUsSent.setStatus("deprecated")
_FsPbTunnelProtocolGmrpPktsRecvd_Type = Counter32
_FsPbTunnelProtocolGmrpPktsRecvd_Object = MibTableColumn
fsPbTunnelProtocolGmrpPktsRecvd = _FsPbTunnelProtocolGmrpPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 16, 1, 9),
    _FsPbTunnelProtocolGmrpPktsRecvd_Type()
)
fsPbTunnelProtocolGmrpPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbTunnelProtocolGmrpPktsRecvd.setStatus("deprecated")
_FsPbTunnelProtocolGmrpPktsSent_Type = Counter32
_FsPbTunnelProtocolGmrpPktsSent_Object = MibTableColumn
fsPbTunnelProtocolGmrpPktsSent = _FsPbTunnelProtocolGmrpPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 16, 1, 10),
    _FsPbTunnelProtocolGmrpPktsSent_Type()
)
fsPbTunnelProtocolGmrpPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbTunnelProtocolGmrpPktsSent.setStatus("deprecated")
_FsPbTunnelProtocolIgmpPktsRecvd_Type = Counter32
_FsPbTunnelProtocolIgmpPktsRecvd_Object = MibTableColumn
fsPbTunnelProtocolIgmpPktsRecvd = _FsPbTunnelProtocolIgmpPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 16, 1, 11),
    _FsPbTunnelProtocolIgmpPktsRecvd_Type()
)
fsPbTunnelProtocolIgmpPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbTunnelProtocolIgmpPktsRecvd.setStatus("deprecated")
_FsPbTunnelProtocolIgmpPktsSent_Type = Counter32
_FsPbTunnelProtocolIgmpPktsSent_Object = MibTableColumn
fsPbTunnelProtocolIgmpPktsSent = _FsPbTunnelProtocolIgmpPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 16, 1, 12),
    _FsPbTunnelProtocolIgmpPktsSent_Type()
)
fsPbTunnelProtocolIgmpPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbTunnelProtocolIgmpPktsSent.setStatus("deprecated")
_FsPbPepExtTable_Object = MibTable
fsPbPepExtTable = _FsPbPepExtTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 17)
)
if mibBuilder.loadTexts:
    fsPbPepExtTable.setStatus("current")
_FsPbPepExtEntry_Object = MibTableRow
fsPbPepExtEntry = _FsPbPepExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 17, 1)
)
if mibBuilder.loadTexts:
    fsPbPepExtEntry.setStatus("current")


class _FsPbPepExtCosPreservation_Type(EnabledStatus):
    """Custom type fsPbPepExtCosPreservation based on EnabledStatus"""
    defaultValue = 2


_FsPbPepExtCosPreservation_Type.__name__ = "EnabledStatus"
_FsPbPepExtCosPreservation_Object = MibTableColumn
fsPbPepExtCosPreservation = _FsPbPepExtCosPreservation_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 113, 2, 17, 1, 1),
    _FsPbPepExtCosPreservation_Type()
)
fsPbPepExtCosPreservation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbPepExtCosPreservation.setStatus("current")
dot1adPepEntry.registerAugmentions(
    ("SUPERMICRO-PROVIDERBRIDGE-MIB",
     "fsPbPepExtEntry")
)
fsPbPepExtEntry.setIndexNames(*dot1adPepEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-PROVIDERBRIDGE-MIB",
    **{"TunnelStatus": TunnelStatus,
       "futureProviderBridgeMIB": futureProviderBridgeMIB,
       "fsPbSystem": fsPbSystem,
       "fsPbMulticastMacLimit": fsPbMulticastMacLimit,
       "fsPbTunnelStpAddress": fsPbTunnelStpAddress,
       "fsPbTunnelLacpAddress": fsPbTunnelLacpAddress,
       "fsPbTunnelDot1xAddress": fsPbTunnelDot1xAddress,
       "fsPbTunnelGvrpAddress": fsPbTunnelGvrpAddress,
       "fsPbTunnelGmrpAddress": fsPbTunnelGmrpAddress,
       "fsPbConfig": fsPbConfig,
       "fsPbPortInfoTable": fsPbPortInfoTable,
       "fsPbPortInfoEntry": fsPbPortInfoEntry,
       "fsPbPort": fsPbPort,
       "fsPbPortSVlanClassificationMethod": fsPbPortSVlanClassificationMethod,
       "fsPbPortSVlanIngressEtherType": fsPbPortSVlanIngressEtherType,
       "fsPbPortSVlanEgressEtherType": fsPbPortSVlanEgressEtherType,
       "fsPbPortSVlanEtherTypeSwapStatus": fsPbPortSVlanEtherTypeSwapStatus,
       "fsPbPortSVlanTranslationStatus": fsPbPortSVlanTranslationStatus,
       "fsPbPortUnicastMacLearning": fsPbPortUnicastMacLearning,
       "fsPbPortUnicastMacLimit": fsPbPortUnicastMacLimit,
       "fsPbPortBundleStatus": fsPbPortBundleStatus,
       "fsPbPortMultiplexStatus": fsPbPortMultiplexStatus,
       "fsPbSrcMacSVlanTable": fsPbSrcMacSVlanTable,
       "fsPbSrcMacSVlanEntry": fsPbSrcMacSVlanEntry,
       "fsPbSrcMacAddress": fsPbSrcMacAddress,
       "fsPbSrcMacSVlan": fsPbSrcMacSVlan,
       "fsPbSrcMacRowStatus": fsPbSrcMacRowStatus,
       "fsPbDstMacSVlanTable": fsPbDstMacSVlanTable,
       "fsPbDstMacSVlanEntry": fsPbDstMacSVlanEntry,
       "fsPbDstMacAddress": fsPbDstMacAddress,
       "fsPbDstMacSVlan": fsPbDstMacSVlan,
       "fsPbDstMacRowStatus": fsPbDstMacRowStatus,
       "fsPbCVlanSrcMacSVlanTable": fsPbCVlanSrcMacSVlanTable,
       "fsPbCVlanSrcMacSVlanEntry": fsPbCVlanSrcMacSVlanEntry,
       "fsPbCVlanSrcMacCVlan": fsPbCVlanSrcMacCVlan,
       "fsPbCVlanSrcMacAddr": fsPbCVlanSrcMacAddr,
       "fsPbCVlanSrcMacSVlan": fsPbCVlanSrcMacSVlan,
       "fsPbCVlanSrcMacRowStatus": fsPbCVlanSrcMacRowStatus,
       "fsPbCVlanDstMacSVlanTable": fsPbCVlanDstMacSVlanTable,
       "fsPbCVlanDstMacSVlanEntry": fsPbCVlanDstMacSVlanEntry,
       "fsPbCVlanDstMacCVlan": fsPbCVlanDstMacCVlan,
       "fsPbCVlanDstMacAddr": fsPbCVlanDstMacAddr,
       "fsPbCVlanDstMacSVlan": fsPbCVlanDstMacSVlan,
       "fsPbCVlanDstMacRowStatus": fsPbCVlanDstMacRowStatus,
       "fsPbDscpSVlanTable": fsPbDscpSVlanTable,
       "fsPbDscpSVlanEntry": fsPbDscpSVlanEntry,
       "fsPbDscp": fsPbDscp,
       "fsPbDscpSVlan": fsPbDscpSVlan,
       "fsPbDscpRowStatus": fsPbDscpRowStatus,
       "fsPbCVlanDscpSVlanTable": fsPbCVlanDscpSVlanTable,
       "fsPbCVlanDscpSVlanEntry": fsPbCVlanDscpSVlanEntry,
       "fsPbCVlanDscpCVlan": fsPbCVlanDscpCVlan,
       "fsPbCVlanDscp": fsPbCVlanDscp,
       "fsPbCVlanDscpSVlan": fsPbCVlanDscpSVlan,
       "fsPbCVlanDscpRowStatus": fsPbCVlanDscpRowStatus,
       "fsPbSrcIpAddrSVlanTable": fsPbSrcIpAddrSVlanTable,
       "fsPbSrcIpAddrSVlanEntry": fsPbSrcIpAddrSVlanEntry,
       "fsPbSrcIpAddr": fsPbSrcIpAddr,
       "fsPbSrcIpSVlan": fsPbSrcIpSVlan,
       "fsPbSrcIpRowStatus": fsPbSrcIpRowStatus,
       "fsPbDstIpAddrSVlanTable": fsPbDstIpAddrSVlanTable,
       "fsPbDstIpAddrSVlanEntry": fsPbDstIpAddrSVlanEntry,
       "fsPbDstIpAddr": fsPbDstIpAddr,
       "fsPbDstIpSVlan": fsPbDstIpSVlan,
       "fsPbDstIpRowStatus": fsPbDstIpRowStatus,
       "fsPbSrcDstIpSVlanTable": fsPbSrcDstIpSVlanTable,
       "fsPbSrcDstIpSVlanEntry": fsPbSrcDstIpSVlanEntry,
       "fsPbSrcDstSrcIpAddr": fsPbSrcDstSrcIpAddr,
       "fsPbSrcDstDstIpAddr": fsPbSrcDstDstIpAddr,
       "fsPbSrcDstIpSVlan": fsPbSrcDstIpSVlan,
       "fsPbSrcDstIpRowStatus": fsPbSrcDstIpRowStatus,
       "fsPbCVlanDstIpSVlanTable": fsPbCVlanDstIpSVlanTable,
       "fsPbCVlanDstIpSVlanEntry": fsPbCVlanDstIpSVlanEntry,
       "fsPbCVlanDstIpCVlan": fsPbCVlanDstIpCVlan,
       "fsPbCVlanDstIp": fsPbCVlanDstIp,
       "fsPbCVlanDstIpSVlan": fsPbCVlanDstIpSVlan,
       "fsPbCVlanDstIpRowStatus": fsPbCVlanDstIpRowStatus,
       "fsPbPortBasedCVlanTable": fsPbPortBasedCVlanTable,
       "fsPbPortBasedCVlanEntry": fsPbPortBasedCVlanEntry,
       "fsPbPortCVlan": fsPbPortCVlan,
       "fsPbPortCVlanClassifyStatus": fsPbPortCVlanClassifyStatus,
       "fsPbEtherTypeSwapTable": fsPbEtherTypeSwapTable,
       "fsPbEtherTypeSwapEntry": fsPbEtherTypeSwapEntry,
       "fsPbLocalEtherType": fsPbLocalEtherType,
       "fsPbRelayEtherType": fsPbRelayEtherType,
       "fsPbEtherTypeSwapRowStatus": fsPbEtherTypeSwapRowStatus,
       "fsPbSVlanConfigTable": fsPbSVlanConfigTable,
       "fsPbSVlanConfigEntry": fsPbSVlanConfigEntry,
       "fsPbSVlanConfigServiceType": fsPbSVlanConfigServiceType,
       "fsPbTunnelProtocolTable": fsPbTunnelProtocolTable,
       "fsPbTunnelProtocolEntry": fsPbTunnelProtocolEntry,
       "fsPbTunnelProtocolDot1x": fsPbTunnelProtocolDot1x,
       "fsPbTunnelProtocolLacp": fsPbTunnelProtocolLacp,
       "fsPbTunnelProtocolStp": fsPbTunnelProtocolStp,
       "fsPbTunnelProtocolGvrp": fsPbTunnelProtocolGvrp,
       "fsPbTunnelProtocolGmrp": fsPbTunnelProtocolGmrp,
       "fsPbTunnelProtocolIgmp": fsPbTunnelProtocolIgmp,
       "fsPbTunnelProtocolStatsTable": fsPbTunnelProtocolStatsTable,
       "fsPbTunnelProtocolStatsEntry": fsPbTunnelProtocolStatsEntry,
       "fsPbTunnelProtocolDot1xPktsRecvd": fsPbTunnelProtocolDot1xPktsRecvd,
       "fsPbTunnelProtocolDot1xPktsSent": fsPbTunnelProtocolDot1xPktsSent,
       "fsPbTunnelProtocolLacpPktsRecvd": fsPbTunnelProtocolLacpPktsRecvd,
       "fsPbTunnelProtocolLacpPktsSent": fsPbTunnelProtocolLacpPktsSent,
       "fsPbTunnelProtocolStpPDUsRecvd": fsPbTunnelProtocolStpPDUsRecvd,
       "fsPbTunnelProtocolStpPDUsSent": fsPbTunnelProtocolStpPDUsSent,
       "fsPbTunnelProtocolGvrpPDUsRecvd": fsPbTunnelProtocolGvrpPDUsRecvd,
       "fsPbTunnelProtocolGvrpPDUsSent": fsPbTunnelProtocolGvrpPDUsSent,
       "fsPbTunnelProtocolGmrpPktsRecvd": fsPbTunnelProtocolGmrpPktsRecvd,
       "fsPbTunnelProtocolGmrpPktsSent": fsPbTunnelProtocolGmrpPktsSent,
       "fsPbTunnelProtocolIgmpPktsRecvd": fsPbTunnelProtocolIgmpPktsRecvd,
       "fsPbTunnelProtocolIgmpPktsSent": fsPbTunnelProtocolIgmpPktsSent,
       "fsPbPepExtTable": fsPbPepExtTable,
       "fsPbPepExtEntry": fsPbPepExtEntry,
       "fsPbPepExtCosPreservation": fsPbPepExtCosPreservation}
)
