# SNMP MIB module (ZTE-AN-MPLS-L2VPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-MPLS-L2VPN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:37 2025
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
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 experimental,
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
    "experimental",
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

(ZxAnIfindex,
 zxAn) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "ZxAnIfindex",
    "zxAn")

(IANAPwPsnTypeTC,
 IANAPwTypeTC) = mibBuilder.importSymbols(
    "ZX-PWE3-MIB",
    "IANAPwPsnTypeTC",
    "IANAPwTypeTC")

(PwIndexType,) = mibBuilder.importSymbols(
    "ZXPW-TC-STD-MIB",
    "PwIndexType")


# MODULE-IDENTITY

zxAnMplsL2vpnMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ZxAnMplsVccvCcType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("pwAch", 0),
          ("mplsRouterAlertLbl", 1),
          ("mplsPwLblTtlEqualsOne", 2),
          ("reserved1", 3),
          ("reserved2", 4),
          ("reserved3", 5),
          ("reserved4", 6),
          ("reserved5", 7))
    )


class ZxAnMplsVccvCvType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("icmpPing", 0),
          ("lspPing", 1),
          ("bfd", 2),
          ("reserved1", 3),
          ("reserved2", 4),
          ("reserved3", 5),
          ("reserved4", 6),
          ("reserved5", 7))
    )


# MIB Managed Objects in the order of their OIDs

_ZxAnL2vpnGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnL2vpnGlobalObjects = _ZxAnL2vpnGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 1)
)
_ZxAnMplsStaticPwTable_Object = MibTable
zxAnMplsStaticPwTable = _ZxAnMplsStaticPwTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 1, 11)
)
if mibBuilder.loadTexts:
    zxAnMplsStaticPwTable.setStatus("current")
_ZxAnMplsStaticPwEntry_Object = MibTableRow
zxAnMplsStaticPwEntry = _ZxAnMplsStaticPwEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 1, 11, 1)
)
zxAnMplsStaticPwEntry.setIndexNames(
    (0, "ZTE-AN-MPLS-L2VPN-MIB", "zxAnMplsStaticPwName"),
)
if mibBuilder.loadTexts:
    zxAnMplsStaticPwEntry.setStatus("current")


class _ZxAnMplsStaticPwName_Type(DisplayString):
    """Custom type zxAnMplsStaticPwName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ZxAnMplsStaticPwName_Type.__name__ = "DisplayString"
_ZxAnMplsStaticPwName_Object = MibTableColumn
zxAnMplsStaticPwName = _ZxAnMplsStaticPwName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 1, 11, 1, 2),
    _ZxAnMplsStaticPwName_Type()
)
zxAnMplsStaticPwName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMplsStaticPwName.setStatus("current")


class _ZxAnMplsOutgoingPwLabel_Type(Unsigned32):
    """Custom type zxAnMplsOutgoingPwLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1044479, 1048575),
    )


_ZxAnMplsOutgoingPwLabel_Type.__name__ = "Unsigned32"
_ZxAnMplsOutgoingPwLabel_Object = MibTableColumn
zxAnMplsOutgoingPwLabel = _ZxAnMplsOutgoingPwLabel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 1, 11, 1, 3),
    _ZxAnMplsOutgoingPwLabel_Type()
)
zxAnMplsOutgoingPwLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMplsOutgoingPwLabel.setStatus("current")


class _ZxAnMplsIncomingPwLabel_Type(Unsigned32):
    """Custom type zxAnMplsIncomingPwLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_ZxAnMplsIncomingPwLabel_Type.__name__ = "Unsigned32"
_ZxAnMplsIncomingPwLabel_Object = MibTableColumn
zxAnMplsIncomingPwLabel = _ZxAnMplsIncomingPwLabel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 1, 11, 1, 4),
    _ZxAnMplsIncomingPwLabel_Type()
)
zxAnMplsIncomingPwLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMplsIncomingPwLabel.setStatus("current")
_ZxAnMplsStaticPwRowStatus_Type = RowStatus
_ZxAnMplsStaticPwRowStatus_Object = MibTableColumn
zxAnMplsStaticPwRowStatus = _ZxAnMplsStaticPwRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 1, 11, 1, 31),
    _ZxAnMplsStaticPwRowStatus_Type()
)
zxAnMplsStaticPwRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMplsStaticPwRowStatus.setStatus("current")
_ZxAnVpwsObjects_ObjectIdentity = ObjectIdentity
zxAnVpwsObjects = _ZxAnVpwsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 2)
)
_ZxAnVpwsTable_Object = MibTable
zxAnVpwsTable = _ZxAnVpwsTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 2, 11)
)
if mibBuilder.loadTexts:
    zxAnVpwsTable.setStatus("current")
_ZxAnVpwsEntry_Object = MibTableRow
zxAnVpwsEntry = _ZxAnVpwsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 2, 11, 1)
)
zxAnVpwsEntry.setIndexNames(
    (0, "ZTE-AN-MPLS-L2VPN-MIB", "zxAnVpwsL3IfIndex"),
)
if mibBuilder.loadTexts:
    zxAnVpwsEntry.setStatus("current")
_ZxAnVpwsL3IfIndex_Type = ZxAnIfindex
_ZxAnVpwsL3IfIndex_Object = MibTableColumn
zxAnVpwsL3IfIndex = _ZxAnVpwsL3IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 2, 11, 1, 1),
    _ZxAnVpwsL3IfIndex_Type()
)
zxAnVpwsL3IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVpwsL3IfIndex.setStatus("current")


class _ZxAnVpwsPeerIpAddrType_Type(InetAddressType):
    """Custom type zxAnVpwsPeerIpAddrType based on InetAddressType"""
    defaultValue = 1


_ZxAnVpwsPeerIpAddrType_Type.__name__ = "InetAddressType"
_ZxAnVpwsPeerIpAddrType_Object = MibTableColumn
zxAnVpwsPeerIpAddrType = _ZxAnVpwsPeerIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 2, 11, 1, 2),
    _ZxAnVpwsPeerIpAddrType_Type()
)
zxAnVpwsPeerIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVpwsPeerIpAddrType.setStatus("current")
_ZxAnVpwsPeerIpAddr_Type = InetAddress
_ZxAnVpwsPeerIpAddr_Object = MibTableColumn
zxAnVpwsPeerIpAddr = _ZxAnVpwsPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 2, 11, 1, 3),
    _ZxAnVpwsPeerIpAddr_Type()
)
zxAnVpwsPeerIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVpwsPeerIpAddr.setStatus("current")


class _ZxAnVpwsVcId_Type(Unsigned32):
    """Custom type zxAnVpwsVcId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ZxAnVpwsVcId_Type.__name__ = "Unsigned32"
_ZxAnVpwsVcId_Object = MibTableColumn
zxAnVpwsVcId = _ZxAnVpwsVcId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 2, 11, 1, 4),
    _ZxAnVpwsVcId_Type()
)
zxAnVpwsVcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVpwsVcId.setStatus("current")
_ZxAnVpwsPwType_Type = IANAPwTypeTC
_ZxAnVpwsPwType_Object = MibTableColumn
zxAnVpwsPwType = _ZxAnVpwsPwType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 2, 11, 1, 5),
    _ZxAnVpwsPwType_Type()
)
zxAnVpwsPwType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVpwsPwType.setStatus("current")
_ZxAnVpwsStaticPwName_Type = DisplayString
_ZxAnVpwsStaticPwName_Object = MibTableColumn
zxAnVpwsStaticPwName = _ZxAnVpwsStaticPwName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 2, 11, 1, 6),
    _ZxAnVpwsStaticPwName_Type()
)
zxAnVpwsStaticPwName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVpwsStaticPwName.setStatus("current")


class _ZxAnVpwsStandbyPeerIpAddrType_Type(InetAddressType):
    """Custom type zxAnVpwsStandbyPeerIpAddrType based on InetAddressType"""
    defaultValue = 1


_ZxAnVpwsStandbyPeerIpAddrType_Type.__name__ = "InetAddressType"
_ZxAnVpwsStandbyPeerIpAddrType_Object = MibTableColumn
zxAnVpwsStandbyPeerIpAddrType = _ZxAnVpwsStandbyPeerIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 2, 11, 1, 7),
    _ZxAnVpwsStandbyPeerIpAddrType_Type()
)
zxAnVpwsStandbyPeerIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVpwsStandbyPeerIpAddrType.setStatus("current")
_ZxAnVpwsStandbyPeerIpAddr_Type = InetAddress
_ZxAnVpwsStandbyPeerIpAddr_Object = MibTableColumn
zxAnVpwsStandbyPeerIpAddr = _ZxAnVpwsStandbyPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 2, 11, 1, 8),
    _ZxAnVpwsStandbyPeerIpAddr_Type()
)
zxAnVpwsStandbyPeerIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVpwsStandbyPeerIpAddr.setStatus("current")


class _ZxAnVpwsStandbyVcId_Type(Unsigned32):
    """Custom type zxAnVpwsStandbyVcId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ZxAnVpwsStandbyVcId_Type.__name__ = "Unsigned32"
_ZxAnVpwsStandbyVcId_Object = MibTableColumn
zxAnVpwsStandbyVcId = _ZxAnVpwsStandbyVcId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 2, 11, 1, 9),
    _ZxAnVpwsStandbyVcId_Type()
)
zxAnVpwsStandbyVcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVpwsStandbyVcId.setStatus("current")


class _ZxAnVpwsPwe3CWPreferred_Type(TruthValue):
    """Custom type zxAnVpwsPwe3CWPreferred based on TruthValue"""
    defaultValue = 2


_ZxAnVpwsPwe3CWPreferred_Type.__name__ = "TruthValue"
_ZxAnVpwsPwe3CWPreferred_Object = MibTableColumn
zxAnVpwsPwe3CWPreferred = _ZxAnVpwsPwe3CWPreferred_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 2, 11, 1, 10),
    _ZxAnVpwsPwe3CWPreferred_Type()
)
zxAnVpwsPwe3CWPreferred.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVpwsPwe3CWPreferred.setStatus("current")


class _ZxAnVpwsVccvEnable_Type(Integer32):
    """Custom type zxAnVpwsVccvEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnVpwsVccvEnable_Type.__name__ = "Integer32"
_ZxAnVpwsVccvEnable_Object = MibTableColumn
zxAnVpwsVccvEnable = _ZxAnVpwsVccvEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 2, 11, 1, 11),
    _ZxAnVpwsVccvEnable_Type()
)
zxAnVpwsVccvEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVpwsVccvEnable.setStatus("current")
_ZxAnVpwsCcTypeCapability_Type = ZxAnMplsVccvCcType
_ZxAnVpwsCcTypeCapability_Object = MibTableColumn
zxAnVpwsCcTypeCapability = _ZxAnVpwsCcTypeCapability_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 2, 11, 1, 12),
    _ZxAnVpwsCcTypeCapability_Type()
)
zxAnVpwsCcTypeCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVpwsCcTypeCapability.setStatus("current")
_ZxAnVpwsCvTypeCapability_Type = ZxAnMplsVccvCvType
_ZxAnVpwsCvTypeCapability_Object = MibTableColumn
zxAnVpwsCvTypeCapability = _ZxAnVpwsCvTypeCapability_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 2, 11, 1, 13),
    _ZxAnVpwsCvTypeCapability_Type()
)
zxAnVpwsCvTypeCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVpwsCvTypeCapability.setStatus("current")
_ZxAnVpwsRowStatus_Type = RowStatus
_ZxAnVpwsRowStatus_Object = MibTableColumn
zxAnVpwsRowStatus = _ZxAnVpwsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 2, 11, 1, 31),
    _ZxAnVpwsRowStatus_Type()
)
zxAnVpwsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVpwsRowStatus.setStatus("current")
_ZxAnVplsObjects_ObjectIdentity = ObjectIdentity
zxAnVplsObjects = _ZxAnVplsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3)
)
_ZxAnVplsVfiConfigTable_Object = MibTable
zxAnVplsVfiConfigTable = _ZxAnVplsVfiConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3, 11)
)
if mibBuilder.loadTexts:
    zxAnVplsVfiConfigTable.setStatus("current")
_ZxAnVplsVfiConfigEntry_Object = MibTableRow
zxAnVplsVfiConfigEntry = _ZxAnVplsVfiConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3, 11, 1)
)
zxAnVplsVfiConfigEntry.setIndexNames(
    (0, "ZTE-AN-MPLS-L2VPN-MIB", "zxAnVplsVfiName"),
)
if mibBuilder.loadTexts:
    zxAnVplsVfiConfigEntry.setStatus("current")


class _ZxAnVplsVfiName_Type(DisplayString):
    """Custom type zxAnVplsVfiName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ZxAnVplsVfiName_Type.__name__ = "DisplayString"
_ZxAnVplsVfiName_Object = MibTableColumn
zxAnVplsVfiName = _ZxAnVplsVfiName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3, 11, 1, 1),
    _ZxAnVplsVfiName_Type()
)
zxAnVplsVfiName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVplsVfiName.setStatus("current")


class _ZxAnVplsVfiVcid_Type(Unsigned32):
    """Custom type zxAnVplsVfiVcid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ZxAnVplsVfiVcid_Type.__name__ = "Unsigned32"
_ZxAnVplsVfiVcid_Object = MibTableColumn
zxAnVplsVfiVcid = _ZxAnVplsVfiVcid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3, 11, 1, 2),
    _ZxAnVplsVfiVcid_Type()
)
zxAnVplsVfiVcid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVplsVfiVcid.setStatus("current")
_ZxAnVplsVfiPwType_Type = IANAPwTypeTC
_ZxAnVplsVfiPwType_Object = MibTableColumn
zxAnVplsVfiPwType = _ZxAnVplsVfiPwType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3, 11, 1, 3),
    _ZxAnVplsVfiPwType_Type()
)
zxAnVplsVfiPwType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVplsVfiPwType.setStatus("current")


class _ZxAnVplsVfiMaxMacLearningNum_Type(Integer32):
    """Custom type zxAnVplsVfiMaxMacLearningNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_ZxAnVplsVfiMaxMacLearningNum_Type.__name__ = "Integer32"
_ZxAnVplsVfiMaxMacLearningNum_Object = MibTableColumn
zxAnVplsVfiMaxMacLearningNum = _ZxAnVplsVfiMaxMacLearningNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3, 11, 1, 4),
    _ZxAnVplsVfiMaxMacLearningNum_Type()
)
zxAnVplsVfiMaxMacLearningNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVplsVfiMaxMacLearningNum.setStatus("current")


class _ZxAnVplsVfiRemoteMacAgingTime_Type(Integer32):
    """Custom type zxAnVplsVfiRemoteMacAgingTime based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(180, 3600),
    )


_ZxAnVplsVfiRemoteMacAgingTime_Type.__name__ = "Integer32"
_ZxAnVplsVfiRemoteMacAgingTime_Object = MibTableColumn
zxAnVplsVfiRemoteMacAgingTime = _ZxAnVplsVfiRemoteMacAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3, 11, 1, 5),
    _ZxAnVplsVfiRemoteMacAgingTime_Type()
)
zxAnVplsVfiRemoteMacAgingTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVplsVfiRemoteMacAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVplsVfiRemoteMacAgingTime.setUnits("second")


class _ZxAnVplsVfiLocalMacAgingTime_Type(Integer32):
    """Custom type zxAnVplsVfiLocalMacAgingTime based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(180, 3600),
    )


_ZxAnVplsVfiLocalMacAgingTime_Type.__name__ = "Integer32"
_ZxAnVplsVfiLocalMacAgingTime_Object = MibTableColumn
zxAnVplsVfiLocalMacAgingTime = _ZxAnVplsVfiLocalMacAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3, 11, 1, 6),
    _ZxAnVplsVfiLocalMacAgingTime_Type()
)
zxAnVplsVfiLocalMacAgingTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVplsVfiLocalMacAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVplsVfiLocalMacAgingTime.setUnits("second")


class _ZxAnVplsVfiBCastRateLimit_Type(Integer32):
    """Custom type zxAnVplsVfiBCastRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 16384000),
    )


_ZxAnVplsVfiBCastRateLimit_Type.__name__ = "Integer32"
_ZxAnVplsVfiBCastRateLimit_Object = MibTableColumn
zxAnVplsVfiBCastRateLimit = _ZxAnVplsVfiBCastRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3, 11, 1, 7),
    _ZxAnVplsVfiBCastRateLimit_Type()
)
zxAnVplsVfiBCastRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVplsVfiBCastRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVplsVfiBCastRateLimit.setUnits("kbps")


class _ZxAnVplsVfiMCastRateLimit_Type(Integer32):
    """Custom type zxAnVplsVfiMCastRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 16384000),
    )


_ZxAnVplsVfiMCastRateLimit_Type.__name__ = "Integer32"
_ZxAnVplsVfiMCastRateLimit_Object = MibTableColumn
zxAnVplsVfiMCastRateLimit = _ZxAnVplsVfiMCastRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3, 11, 1, 8),
    _ZxAnVplsVfiMCastRateLimit_Type()
)
zxAnVplsVfiMCastRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVplsVfiMCastRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVplsVfiMCastRateLimit.setUnits("kbps")


class _ZxAnVplsVfiUnknownUCastRateLimit_Type(Integer32):
    """Custom type zxAnVplsVfiUnknownUCastRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 16384000),
    )


_ZxAnVplsVfiUnknownUCastRateLimit_Type.__name__ = "Integer32"
_ZxAnVplsVfiUnknownUCastRateLimit_Object = MibTableColumn
zxAnVplsVfiUnknownUCastRateLimit = _ZxAnVplsVfiUnknownUCastRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3, 11, 1, 9),
    _ZxAnVplsVfiUnknownUCastRateLimit_Type()
)
zxAnVplsVfiUnknownUCastRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVplsVfiUnknownUCastRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVplsVfiUnknownUCastRateLimit.setUnits("kbps")


class _ZxAnVplsVfiVcidType_Type(Integer32):
    """Custom type zxAnVplsVfiVcidType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_ZxAnVplsVfiVcidType_Type.__name__ = "Integer32"
_ZxAnVplsVfiVcidType_Object = MibTableColumn
zxAnVplsVfiVcidType = _ZxAnVplsVfiVcidType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3, 11, 1, 10),
    _ZxAnVplsVfiVcidType_Type()
)
zxAnVplsVfiVcidType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVplsVfiVcidType.setStatus("current")


class _ZxAnVplsVfiPwe3CWPreferred_Type(TruthValue):
    """Custom type zxAnVplsVfiPwe3CWPreferred based on TruthValue"""
    defaultValue = 2


_ZxAnVplsVfiPwe3CWPreferred_Type.__name__ = "TruthValue"
_ZxAnVplsVfiPwe3CWPreferred_Object = MibTableColumn
zxAnVplsVfiPwe3CWPreferred = _ZxAnVplsVfiPwe3CWPreferred_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3, 11, 1, 11),
    _ZxAnVplsVfiPwe3CWPreferred_Type()
)
zxAnVplsVfiPwe3CWPreferred.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVplsVfiPwe3CWPreferred.setStatus("current")


class _ZxAnVplsVfiVccvEnable_Type(Integer32):
    """Custom type zxAnVplsVfiVccvEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnVplsVfiVccvEnable_Type.__name__ = "Integer32"
_ZxAnVplsVfiVccvEnable_Object = MibTableColumn
zxAnVplsVfiVccvEnable = _ZxAnVplsVfiVccvEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3, 11, 1, 12),
    _ZxAnVplsVfiVccvEnable_Type()
)
zxAnVplsVfiVccvEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVplsVfiVccvEnable.setStatus("current")
_ZxAnVplsVfiCcTypeCapability_Type = ZxAnMplsVccvCcType
_ZxAnVplsVfiCcTypeCapability_Object = MibTableColumn
zxAnVplsVfiCcTypeCapability = _ZxAnVplsVfiCcTypeCapability_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3, 11, 1, 13),
    _ZxAnVplsVfiCcTypeCapability_Type()
)
zxAnVplsVfiCcTypeCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVplsVfiCcTypeCapability.setStatus("current")
_ZxAnVplsVfiCvTypeCapability_Type = ZxAnMplsVccvCvType
_ZxAnVplsVfiCvTypeCapability_Object = MibTableColumn
zxAnVplsVfiCvTypeCapability = _ZxAnVplsVfiCvTypeCapability_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3, 11, 1, 14),
    _ZxAnVplsVfiCvTypeCapability_Type()
)
zxAnVplsVfiCvTypeCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVplsVfiCvTypeCapability.setStatus("current")
_ZxAnVplsVfiRowStatus_Type = RowStatus
_ZxAnVplsVfiRowStatus_Object = MibTableColumn
zxAnVplsVfiRowStatus = _ZxAnVplsVfiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3, 11, 1, 30),
    _ZxAnVplsVfiRowStatus_Type()
)
zxAnVplsVfiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVplsVfiRowStatus.setStatus("current")
_ZxAnVplsVfiPeerIpAddrTable_Object = MibTable
zxAnVplsVfiPeerIpAddrTable = _ZxAnVplsVfiPeerIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3, 12)
)
if mibBuilder.loadTexts:
    zxAnVplsVfiPeerIpAddrTable.setStatus("current")
_ZxAnVplsVfiPeerIpAddrEntry_Object = MibTableRow
zxAnVplsVfiPeerIpAddrEntry = _ZxAnVplsVfiPeerIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3, 12, 1)
)
zxAnVplsVfiPeerIpAddrEntry.setIndexNames(
    (0, "ZTE-AN-MPLS-L2VPN-MIB", "zxAnVplsVfiName"),
    (0, "ZTE-AN-MPLS-L2VPN-MIB", "zxAnVplsVfiPeerIpAddrType"),
    (0, "ZTE-AN-MPLS-L2VPN-MIB", "zxAnVplsVfiPeerIpAddr"),
)
if mibBuilder.loadTexts:
    zxAnVplsVfiPeerIpAddrEntry.setStatus("current")


class _ZxAnVplsVfiPeerIpAddrType_Type(InetAddressType):
    """Custom type zxAnVplsVfiPeerIpAddrType based on InetAddressType"""
    defaultValue = 1


_ZxAnVplsVfiPeerIpAddrType_Type.__name__ = "InetAddressType"
_ZxAnVplsVfiPeerIpAddrType_Object = MibTableColumn
zxAnVplsVfiPeerIpAddrType = _ZxAnVplsVfiPeerIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3, 12, 1, 1),
    _ZxAnVplsVfiPeerIpAddrType_Type()
)
zxAnVplsVfiPeerIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVplsVfiPeerIpAddrType.setStatus("current")
_ZxAnVplsVfiPeerIpAddr_Type = InetAddress
_ZxAnVplsVfiPeerIpAddr_Object = MibTableColumn
zxAnVplsVfiPeerIpAddr = _ZxAnVplsVfiPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3, 12, 1, 2),
    _ZxAnVplsVfiPeerIpAddr_Type()
)
zxAnVplsVfiPeerIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVplsVfiPeerIpAddr.setStatus("current")


class _ZxAnVplsVfiStandbyPeerIpAddrType_Type(InetAddressType):
    """Custom type zxAnVplsVfiStandbyPeerIpAddrType based on InetAddressType"""
    defaultValue = 1


_ZxAnVplsVfiStandbyPeerIpAddrType_Type.__name__ = "InetAddressType"
_ZxAnVplsVfiStandbyPeerIpAddrType_Object = MibTableColumn
zxAnVplsVfiStandbyPeerIpAddrType = _ZxAnVplsVfiStandbyPeerIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3, 12, 1, 3),
    _ZxAnVplsVfiStandbyPeerIpAddrType_Type()
)
zxAnVplsVfiStandbyPeerIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVplsVfiStandbyPeerIpAddrType.setStatus("current")
_ZxAnVplsVfiStandbyPeerIpAddr_Type = InetAddress
_ZxAnVplsVfiStandbyPeerIpAddr_Object = MibTableColumn
zxAnVplsVfiStandbyPeerIpAddr = _ZxAnVplsVfiStandbyPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3, 12, 1, 4),
    _ZxAnVplsVfiStandbyPeerIpAddr_Type()
)
zxAnVplsVfiStandbyPeerIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVplsVfiStandbyPeerIpAddr.setStatus("current")


class _ZxAnVplsVfiStaticPwName_Type(DisplayString):
    """Custom type zxAnVplsVfiStaticPwName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ZxAnVplsVfiStaticPwName_Type.__name__ = "DisplayString"
_ZxAnVplsVfiStaticPwName_Object = MibTableColumn
zxAnVplsVfiStaticPwName = _ZxAnVplsVfiStaticPwName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3, 12, 1, 5),
    _ZxAnVplsVfiStaticPwName_Type()
)
zxAnVplsVfiStaticPwName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVplsVfiStaticPwName.setStatus("current")


class _ZxAnVplsVfiPwNetType_Type(Integer32):
    """Custom type zxAnVplsVfiPwNetType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("spoke", 1),
          ("hub", 2))
    )


_ZxAnVplsVfiPwNetType_Type.__name__ = "Integer32"
_ZxAnVplsVfiPwNetType_Object = MibTableColumn
zxAnVplsVfiPwNetType = _ZxAnVplsVfiPwNetType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3, 12, 1, 6),
    _ZxAnVplsVfiPwNetType_Type()
)
zxAnVplsVfiPwNetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVplsVfiPwNetType.setStatus("current")
_ZxAnVplsVfiPeerRowStatus_Type = RowStatus
_ZxAnVplsVfiPeerRowStatus_Object = MibTableColumn
zxAnVplsVfiPeerRowStatus = _ZxAnVplsVfiPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3, 12, 1, 20),
    _ZxAnVplsVfiPeerRowStatus_Type()
)
zxAnVplsVfiPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVplsVfiPeerRowStatus.setStatus("current")
_ZxAnL3IfVfiConfigTable_Object = MibTable
zxAnL3IfVfiConfigTable = _ZxAnL3IfVfiConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3, 13)
)
if mibBuilder.loadTexts:
    zxAnL3IfVfiConfigTable.setStatus("current")
_ZxAnL3IfVfiConfigEntry_Object = MibTableRow
zxAnL3IfVfiConfigEntry = _ZxAnL3IfVfiConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3, 13, 1)
)
zxAnL3IfVfiConfigEntry.setIndexNames(
    (0, "ZTE-AN-MPLS-L2VPN-MIB", "zxAnL3IfVfiIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnL3IfVfiConfigEntry.setStatus("current")
_ZxAnL3IfVfiIfIndex_Type = ZxAnIfindex
_ZxAnL3IfVfiIfIndex_Object = MibTableColumn
zxAnL3IfVfiIfIndex = _ZxAnL3IfVfiIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3, 13, 1, 1),
    _ZxAnL3IfVfiIfIndex_Type()
)
zxAnL3IfVfiIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnL3IfVfiIfIndex.setStatus("current")


class _ZxAnL3IfVfiName_Type(DisplayString):
    """Custom type zxAnL3IfVfiName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ZxAnL3IfVfiName_Type.__name__ = "DisplayString"
_ZxAnL3IfVfiName_Object = MibTableColumn
zxAnL3IfVfiName = _ZxAnL3IfVfiName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3, 13, 1, 2),
    _ZxAnL3IfVfiName_Type()
)
zxAnL3IfVfiName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnL3IfVfiName.setStatus("current")
_ZxAnL3IfVfiRowStatus_Type = RowStatus
_ZxAnL3IfVfiRowStatus_Object = MibTableColumn
zxAnL3IfVfiRowStatus = _ZxAnL3IfVfiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3, 13, 1, 20),
    _ZxAnL3IfVfiRowStatus_Type()
)
zxAnL3IfVfiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnL3IfVfiRowStatus.setStatus("current")
_ZxAnVplsVfiMacTable_Object = MibTable
zxAnVplsVfiMacTable = _ZxAnVplsVfiMacTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3, 14)
)
if mibBuilder.loadTexts:
    zxAnVplsVfiMacTable.setStatus("current")
_ZxAnVplsVfiMacEntry_Object = MibTableRow
zxAnVplsVfiMacEntry = _ZxAnVplsVfiMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3, 14, 1)
)
zxAnVplsVfiMacEntry.setIndexNames(
    (0, "ZTE-AN-MPLS-L2VPN-MIB", "zxAnVplsVfiName"),
    (0, "ZTE-AN-MPLS-L2VPN-MIB", "zxAnVplsVfiMacAddrType"),
    (0, "ZTE-AN-MPLS-L2VPN-MIB", "zxAnVplsVfiMacAddr"),
)
if mibBuilder.loadTexts:
    zxAnVplsVfiMacEntry.setStatus("current")


class _ZxAnVplsVfiMacAddrType_Type(Integer32):
    """Custom type zxAnVplsVfiMacAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_ZxAnVplsVfiMacAddrType_Type.__name__ = "Integer32"
_ZxAnVplsVfiMacAddrType_Object = MibTableColumn
zxAnVplsVfiMacAddrType = _ZxAnVplsVfiMacAddrType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3, 14, 1, 1),
    _ZxAnVplsVfiMacAddrType_Type()
)
zxAnVplsVfiMacAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVplsVfiMacAddrType.setStatus("current")
_ZxAnVplsVfiMacAddr_Type = MacAddress
_ZxAnVplsVfiMacAddr_Object = MibTableColumn
zxAnVplsVfiMacAddr = _ZxAnVplsVfiMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3, 14, 1, 2),
    _ZxAnVplsVfiMacAddr_Type()
)
zxAnVplsVfiMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVplsVfiMacAddr.setStatus("current")


class _ZxAnVplsVfiMacAddrConfLocation_Type(Integer32):
    """Custom type zxAnVplsVfiMacAddrConfLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_ZxAnVplsVfiMacAddrConfLocation_Type.__name__ = "Integer32"
_ZxAnVplsVfiMacAddrConfLocation_Object = MibTableColumn
zxAnVplsVfiMacAddrConfLocation = _ZxAnVplsVfiMacAddrConfLocation_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3, 14, 1, 3),
    _ZxAnVplsVfiMacAddrConfLocation_Type()
)
zxAnVplsVfiMacAddrConfLocation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVplsVfiMacAddrConfLocation.setStatus("current")
_ZxAnVplsVfiMacL3IfVlanIndex_Type = ZxAnIfindex
_ZxAnVplsVfiMacL3IfVlanIndex_Object = MibTableColumn
zxAnVplsVfiMacL3IfVlanIndex = _ZxAnVplsVfiMacL3IfVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3, 14, 1, 4),
    _ZxAnVplsVfiMacL3IfVlanIndex_Type()
)
zxAnVplsVfiMacL3IfVlanIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVplsVfiMacL3IfVlanIndex.setStatus("current")


class _ZxAnVplsVfiMacPeerIpAddrType_Type(InetAddressType):
    """Custom type zxAnVplsVfiMacPeerIpAddrType based on InetAddressType"""
    defaultValue = 1


_ZxAnVplsVfiMacPeerIpAddrType_Type.__name__ = "InetAddressType"
_ZxAnVplsVfiMacPeerIpAddrType_Object = MibTableColumn
zxAnVplsVfiMacPeerIpAddrType = _ZxAnVplsVfiMacPeerIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3, 14, 1, 5),
    _ZxAnVplsVfiMacPeerIpAddrType_Type()
)
zxAnVplsVfiMacPeerIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVplsVfiMacPeerIpAddrType.setStatus("current")
_ZxAnVplsVfiMacPeerIpAddr_Type = InetAddress
_ZxAnVplsVfiMacPeerIpAddr_Object = MibTableColumn
zxAnVplsVfiMacPeerIpAddr = _ZxAnVplsVfiMacPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3, 14, 1, 6),
    _ZxAnVplsVfiMacPeerIpAddr_Type()
)
zxAnVplsVfiMacPeerIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVplsVfiMacPeerIpAddr.setStatus("current")


class _ZxAnVplsVfiMacInnerOutgoingLabel_Type(Integer32):
    """Custom type zxAnVplsVfiMacInnerOutgoingLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_ZxAnVplsVfiMacInnerOutgoingLabel_Type.__name__ = "Integer32"
_ZxAnVplsVfiMacInnerOutgoingLabel_Object = MibTableColumn
zxAnVplsVfiMacInnerOutgoingLabel = _ZxAnVplsVfiMacInnerOutgoingLabel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3, 14, 1, 7),
    _ZxAnVplsVfiMacInnerOutgoingLabel_Type()
)
zxAnVplsVfiMacInnerOutgoingLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVplsVfiMacInnerOutgoingLabel.setStatus("current")


class _ZxAnVplsVfiMacOuterOutgoingLabel_Type(Integer32):
    """Custom type zxAnVplsVfiMacOuterOutgoingLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_ZxAnVplsVfiMacOuterOutgoingLabel_Type.__name__ = "Integer32"
_ZxAnVplsVfiMacOuterOutgoingLabel_Object = MibTableColumn
zxAnVplsVfiMacOuterOutgoingLabel = _ZxAnVplsVfiMacOuterOutgoingLabel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3, 14, 1, 8),
    _ZxAnVplsVfiMacOuterOutgoingLabel_Type()
)
zxAnVplsVfiMacOuterOutgoingLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVplsVfiMacOuterOutgoingLabel.setStatus("current")
_ZxAnVplsVfiMacRowStatus_Type = RowStatus
_ZxAnVplsVfiMacRowStatus_Object = MibTableColumn
zxAnVplsVfiMacRowStatus = _ZxAnVplsVfiMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 3, 14, 1, 30),
    _ZxAnVplsVfiMacRowStatus_Type()
)
zxAnVplsVfiMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVplsVfiMacRowStatus.setStatus("current")
_ZxAnTdmRelayObjects_ObjectIdentity = ObjectIdentity
zxAnTdmRelayObjects = _ZxAnTdmRelayObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 4)
)
_ZxAnTRPwTable_Object = MibTable
zxAnTRPwTable = _ZxAnTRPwTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 4, 11)
)
if mibBuilder.loadTexts:
    zxAnTRPwTable.setStatus("current")
_ZxAnTRPwEntry_Object = MibTableRow
zxAnTRPwEntry = _ZxAnTRPwEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 4, 11, 1)
)
zxAnTRPwEntry.setIndexNames(
    (0, "ZTE-AN-MPLS-L2VPN-MIB", "zxAnTRPwIndex"),
)
if mibBuilder.loadTexts:
    zxAnTRPwEntry.setStatus("current")
_ZxAnTRPwIndex_Type = PwIndexType
_ZxAnTRPwIndex_Object = MibTableColumn
zxAnTRPwIndex = _ZxAnTRPwIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 4, 11, 1, 1),
    _ZxAnTRPwIndex_Type()
)
zxAnTRPwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnTRPwIndex.setStatus("current")
_ZxAnTRPwType_Type = IANAPwTypeTC
_ZxAnTRPwType_Object = MibTableColumn
zxAnTRPwType = _ZxAnTRPwType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 4, 11, 1, 2),
    _ZxAnTRPwType_Type()
)
zxAnTRPwType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnTRPwType.setStatus("current")
_ZxAnTRPwPsnType_Type = IANAPwPsnTypeTC
_ZxAnTRPwPsnType_Object = MibTableColumn
zxAnTRPwPsnType = _ZxAnTRPwPsnType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 4, 11, 1, 3),
    _ZxAnTRPwPsnType_Type()
)
zxAnTRPwPsnType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnTRPwPsnType.setStatus("current")
_ZxAnTRPwPeerIpAddrType_Type = InetAddressType
_ZxAnTRPwPeerIpAddrType_Object = MibTableColumn
zxAnTRPwPeerIpAddrType = _ZxAnTRPwPeerIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 4, 11, 1, 4),
    _ZxAnTRPwPeerIpAddrType_Type()
)
zxAnTRPwPeerIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnTRPwPeerIpAddrType.setStatus("current")
_ZxAnTRPwPeerIpAddr_Type = InetAddress
_ZxAnTRPwPeerIpAddr_Object = MibTableColumn
zxAnTRPwPeerIpAddr = _ZxAnTRPwPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 4, 11, 1, 5),
    _ZxAnTRPwPeerIpAddr_Type()
)
zxAnTRPwPeerIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnTRPwPeerIpAddr.setStatus("current")
_ZxAnTRPwPeerVcId_Type = Unsigned32
_ZxAnTRPwPeerVcId_Object = MibTableColumn
zxAnTRPwPeerVcId = _ZxAnTRPwPeerVcId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 4, 11, 1, 6),
    _ZxAnTRPwPeerVcId_Type()
)
zxAnTRPwPeerVcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnTRPwPeerVcId.setStatus("current")
_ZxAnTRPwStandbyPeerIpAddrType_Type = InetAddressType
_ZxAnTRPwStandbyPeerIpAddrType_Object = MibTableColumn
zxAnTRPwStandbyPeerIpAddrType = _ZxAnTRPwStandbyPeerIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 4, 11, 1, 7),
    _ZxAnTRPwStandbyPeerIpAddrType_Type()
)
zxAnTRPwStandbyPeerIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnTRPwStandbyPeerIpAddrType.setStatus("current")
_ZxAnTRPwStandbyPeerIpAddr_Type = InetAddress
_ZxAnTRPwStandbyPeerIpAddr_Object = MibTableColumn
zxAnTRPwStandbyPeerIpAddr = _ZxAnTRPwStandbyPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 4, 11, 1, 8),
    _ZxAnTRPwStandbyPeerIpAddr_Type()
)
zxAnTRPwStandbyPeerIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnTRPwStandbyPeerIpAddr.setStatus("current")
_ZxAnTRPwStandbyPeerVcId_Type = Unsigned32
_ZxAnTRPwStandbyPeerVcId_Object = MibTableColumn
zxAnTRPwStandbyPeerVcId = _ZxAnTRPwStandbyPeerVcId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 4, 11, 1, 9),
    _ZxAnTRPwStandbyPeerVcId_Type()
)
zxAnTRPwStandbyPeerVcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnTRPwStandbyPeerVcId.setStatus("current")
_ZxAnTRPwOutboundLabel_Type = Unsigned32
_ZxAnTRPwOutboundLabel_Object = MibTableColumn
zxAnTRPwOutboundLabel = _ZxAnTRPwOutboundLabel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 4, 11, 1, 10),
    _ZxAnTRPwOutboundLabel_Type()
)
zxAnTRPwOutboundLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnTRPwOutboundLabel.setStatus("current")
_ZxAnTRPwInboundLabel_Type = Unsigned32
_ZxAnTRPwInboundLabel_Object = MibTableColumn
zxAnTRPwInboundLabel = _ZxAnTRPwInboundLabel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 4, 11, 1, 11),
    _ZxAnTRPwInboundLabel_Type()
)
zxAnTRPwInboundLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnTRPwInboundLabel.setStatus("current")
_ZxAnTRPwOutboundTunnelLabel_Type = Unsigned32
_ZxAnTRPwOutboundTunnelLabel_Object = MibTableColumn
zxAnTRPwOutboundTunnelLabel = _ZxAnTRPwOutboundTunnelLabel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 4, 11, 1, 12),
    _ZxAnTRPwOutboundTunnelLabel_Type()
)
zxAnTRPwOutboundTunnelLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnTRPwOutboundTunnelLabel.setStatus("current")
_ZxAnTRPwInboundTunnelLabel_Type = Unsigned32
_ZxAnTRPwInboundTunnelLabel_Object = MibTableColumn
zxAnTRPwInboundTunnelLabel = _ZxAnTRPwInboundTunnelLabel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 4, 11, 1, 13),
    _ZxAnTRPwInboundTunnelLabel_Type()
)
zxAnTRPwInboundTunnelLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnTRPwInboundTunnelLabel.setStatus("current")
_ZxAnTRPwPayloadSize_Type = Unsigned32
_ZxAnTRPwPayloadSize_Object = MibTableColumn
zxAnTRPwPayloadSize = _ZxAnTRPwPayloadSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 4, 11, 1, 14),
    _ZxAnTRPwPayloadSize_Type()
)
zxAnTRPwPayloadSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnTRPwPayloadSize.setStatus("current")
if mibBuilder.loadTexts:
    zxAnTRPwPayloadSize.setUnits("bytes")
_ZxAnTRPwDstMac_Type = MacAddress
_ZxAnTRPwDstMac_Object = MibTableColumn
zxAnTRPwDstMac = _ZxAnTRPwDstMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 4, 11, 1, 15),
    _ZxAnTRPwDstMac_Type()
)
zxAnTRPwDstMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnTRPwDstMac.setStatus("current")


class _ZxAnTRPwVlanId_Type(Unsigned32):
    """Custom type zxAnTRPwVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxAnTRPwVlanId_Type.__name__ = "Unsigned32"
_ZxAnTRPwVlanId_Object = MibTableColumn
zxAnTRPwVlanId = _ZxAnTRPwVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 4, 11, 1, 16),
    _ZxAnTRPwVlanId_Type()
)
zxAnTRPwVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnTRPwVlanId.setStatus("current")


class _ZxAnTRPwPrio_Type(Integer32):
    """Custom type zxAnTRPwPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnTRPwPrio_Type.__name__ = "Integer32"
_ZxAnTRPwPrio_Object = MibTableColumn
zxAnTRPwPrio = _ZxAnTRPwPrio_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 4, 11, 1, 17),
    _ZxAnTRPwPrio_Type()
)
zxAnTRPwPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnTRPwPrio.setStatus("current")
_ZxAnTRPwRowStatus_Type = RowStatus
_ZxAnTRPwRowStatus_Object = MibTableColumn
zxAnTRPwRowStatus = _ZxAnTRPwRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 4, 11, 1, 30),
    _ZxAnTRPwRowStatus_Type()
)
zxAnTRPwRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnTRPwRowStatus.setStatus("current")
_ZxAnTRTdmSrcMacTable_Object = MibTable
zxAnTRTdmSrcMacTable = _ZxAnTRTdmSrcMacTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 4, 12)
)
if mibBuilder.loadTexts:
    zxAnTRTdmSrcMacTable.setStatus("current")
_ZxAnTRTdmSrcMacEntry_Object = MibTableRow
zxAnTRTdmSrcMacEntry = _ZxAnTRTdmSrcMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 4, 12, 1)
)
zxAnTRTdmSrcMacEntry.setIndexNames(
    (0, "ZTE-AN-MPLS-L2VPN-MIB", "zxAnTRTdmSrcRackNo"),
    (0, "ZTE-AN-MPLS-L2VPN-MIB", "zxAnTRTdmSrcShelfNo"),
    (0, "ZTE-AN-MPLS-L2VPN-MIB", "zxAnTRTdmSrcSlotNo"),
)
if mibBuilder.loadTexts:
    zxAnTRTdmSrcMacEntry.setStatus("current")
_ZxAnTRTdmSrcRackNo_Type = Integer32
_ZxAnTRTdmSrcRackNo_Object = MibTableColumn
zxAnTRTdmSrcRackNo = _ZxAnTRTdmSrcRackNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 4, 12, 1, 1),
    _ZxAnTRTdmSrcRackNo_Type()
)
zxAnTRTdmSrcRackNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnTRTdmSrcRackNo.setStatus("current")
_ZxAnTRTdmSrcShelfNo_Type = Integer32
_ZxAnTRTdmSrcShelfNo_Object = MibTableColumn
zxAnTRTdmSrcShelfNo = _ZxAnTRTdmSrcShelfNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 4, 12, 1, 2),
    _ZxAnTRTdmSrcShelfNo_Type()
)
zxAnTRTdmSrcShelfNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnTRTdmSrcShelfNo.setStatus("current")
_ZxAnTRTdmSrcSlotNo_Type = Integer32
_ZxAnTRTdmSrcSlotNo_Object = MibTableColumn
zxAnTRTdmSrcSlotNo = _ZxAnTRTdmSrcSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 4, 12, 1, 3),
    _ZxAnTRTdmSrcSlotNo_Type()
)
zxAnTRTdmSrcSlotNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnTRTdmSrcSlotNo.setStatus("current")
_ZxAnTRTdmSrcMac_Type = MacAddress
_ZxAnTRTdmSrcMac_Object = MibTableColumn
zxAnTRTdmSrcMac = _ZxAnTRTdmSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 59, 4, 12, 1, 4),
    _ZxAnTRTdmSrcMac_Type()
)
zxAnTRTdmSrcMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnTRTdmSrcMac.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-MPLS-L2VPN-MIB",
    **{"ZxAnMplsVccvCcType": ZxAnMplsVccvCcType,
       "ZxAnMplsVccvCvType": ZxAnMplsVccvCvType,
       "zxAnMplsL2vpnMib": zxAnMplsL2vpnMib,
       "zxAnL2vpnGlobalObjects": zxAnL2vpnGlobalObjects,
       "zxAnMplsStaticPwTable": zxAnMplsStaticPwTable,
       "zxAnMplsStaticPwEntry": zxAnMplsStaticPwEntry,
       "zxAnMplsStaticPwName": zxAnMplsStaticPwName,
       "zxAnMplsOutgoingPwLabel": zxAnMplsOutgoingPwLabel,
       "zxAnMplsIncomingPwLabel": zxAnMplsIncomingPwLabel,
       "zxAnMplsStaticPwRowStatus": zxAnMplsStaticPwRowStatus,
       "zxAnVpwsObjects": zxAnVpwsObjects,
       "zxAnVpwsTable": zxAnVpwsTable,
       "zxAnVpwsEntry": zxAnVpwsEntry,
       "zxAnVpwsL3IfIndex": zxAnVpwsL3IfIndex,
       "zxAnVpwsPeerIpAddrType": zxAnVpwsPeerIpAddrType,
       "zxAnVpwsPeerIpAddr": zxAnVpwsPeerIpAddr,
       "zxAnVpwsVcId": zxAnVpwsVcId,
       "zxAnVpwsPwType": zxAnVpwsPwType,
       "zxAnVpwsStaticPwName": zxAnVpwsStaticPwName,
       "zxAnVpwsStandbyPeerIpAddrType": zxAnVpwsStandbyPeerIpAddrType,
       "zxAnVpwsStandbyPeerIpAddr": zxAnVpwsStandbyPeerIpAddr,
       "zxAnVpwsStandbyVcId": zxAnVpwsStandbyVcId,
       "zxAnVpwsPwe3CWPreferred": zxAnVpwsPwe3CWPreferred,
       "zxAnVpwsVccvEnable": zxAnVpwsVccvEnable,
       "zxAnVpwsCcTypeCapability": zxAnVpwsCcTypeCapability,
       "zxAnVpwsCvTypeCapability": zxAnVpwsCvTypeCapability,
       "zxAnVpwsRowStatus": zxAnVpwsRowStatus,
       "zxAnVplsObjects": zxAnVplsObjects,
       "zxAnVplsVfiConfigTable": zxAnVplsVfiConfigTable,
       "zxAnVplsVfiConfigEntry": zxAnVplsVfiConfigEntry,
       "zxAnVplsVfiName": zxAnVplsVfiName,
       "zxAnVplsVfiVcid": zxAnVplsVfiVcid,
       "zxAnVplsVfiPwType": zxAnVplsVfiPwType,
       "zxAnVplsVfiMaxMacLearningNum": zxAnVplsVfiMaxMacLearningNum,
       "zxAnVplsVfiRemoteMacAgingTime": zxAnVplsVfiRemoteMacAgingTime,
       "zxAnVplsVfiLocalMacAgingTime": zxAnVplsVfiLocalMacAgingTime,
       "zxAnVplsVfiBCastRateLimit": zxAnVplsVfiBCastRateLimit,
       "zxAnVplsVfiMCastRateLimit": zxAnVplsVfiMCastRateLimit,
       "zxAnVplsVfiUnknownUCastRateLimit": zxAnVplsVfiUnknownUCastRateLimit,
       "zxAnVplsVfiVcidType": zxAnVplsVfiVcidType,
       "zxAnVplsVfiPwe3CWPreferred": zxAnVplsVfiPwe3CWPreferred,
       "zxAnVplsVfiVccvEnable": zxAnVplsVfiVccvEnable,
       "zxAnVplsVfiCcTypeCapability": zxAnVplsVfiCcTypeCapability,
       "zxAnVplsVfiCvTypeCapability": zxAnVplsVfiCvTypeCapability,
       "zxAnVplsVfiRowStatus": zxAnVplsVfiRowStatus,
       "zxAnVplsVfiPeerIpAddrTable": zxAnVplsVfiPeerIpAddrTable,
       "zxAnVplsVfiPeerIpAddrEntry": zxAnVplsVfiPeerIpAddrEntry,
       "zxAnVplsVfiPeerIpAddrType": zxAnVplsVfiPeerIpAddrType,
       "zxAnVplsVfiPeerIpAddr": zxAnVplsVfiPeerIpAddr,
       "zxAnVplsVfiStandbyPeerIpAddrType": zxAnVplsVfiStandbyPeerIpAddrType,
       "zxAnVplsVfiStandbyPeerIpAddr": zxAnVplsVfiStandbyPeerIpAddr,
       "zxAnVplsVfiStaticPwName": zxAnVplsVfiStaticPwName,
       "zxAnVplsVfiPwNetType": zxAnVplsVfiPwNetType,
       "zxAnVplsVfiPeerRowStatus": zxAnVplsVfiPeerRowStatus,
       "zxAnL3IfVfiConfigTable": zxAnL3IfVfiConfigTable,
       "zxAnL3IfVfiConfigEntry": zxAnL3IfVfiConfigEntry,
       "zxAnL3IfVfiIfIndex": zxAnL3IfVfiIfIndex,
       "zxAnL3IfVfiName": zxAnL3IfVfiName,
       "zxAnL3IfVfiRowStatus": zxAnL3IfVfiRowStatus,
       "zxAnVplsVfiMacTable": zxAnVplsVfiMacTable,
       "zxAnVplsVfiMacEntry": zxAnVplsVfiMacEntry,
       "zxAnVplsVfiMacAddrType": zxAnVplsVfiMacAddrType,
       "zxAnVplsVfiMacAddr": zxAnVplsVfiMacAddr,
       "zxAnVplsVfiMacAddrConfLocation": zxAnVplsVfiMacAddrConfLocation,
       "zxAnVplsVfiMacL3IfVlanIndex": zxAnVplsVfiMacL3IfVlanIndex,
       "zxAnVplsVfiMacPeerIpAddrType": zxAnVplsVfiMacPeerIpAddrType,
       "zxAnVplsVfiMacPeerIpAddr": zxAnVplsVfiMacPeerIpAddr,
       "zxAnVplsVfiMacInnerOutgoingLabel": zxAnVplsVfiMacInnerOutgoingLabel,
       "zxAnVplsVfiMacOuterOutgoingLabel": zxAnVplsVfiMacOuterOutgoingLabel,
       "zxAnVplsVfiMacRowStatus": zxAnVplsVfiMacRowStatus,
       "zxAnTdmRelayObjects": zxAnTdmRelayObjects,
       "zxAnTRPwTable": zxAnTRPwTable,
       "zxAnTRPwEntry": zxAnTRPwEntry,
       "zxAnTRPwIndex": zxAnTRPwIndex,
       "zxAnTRPwType": zxAnTRPwType,
       "zxAnTRPwPsnType": zxAnTRPwPsnType,
       "zxAnTRPwPeerIpAddrType": zxAnTRPwPeerIpAddrType,
       "zxAnTRPwPeerIpAddr": zxAnTRPwPeerIpAddr,
       "zxAnTRPwPeerVcId": zxAnTRPwPeerVcId,
       "zxAnTRPwStandbyPeerIpAddrType": zxAnTRPwStandbyPeerIpAddrType,
       "zxAnTRPwStandbyPeerIpAddr": zxAnTRPwStandbyPeerIpAddr,
       "zxAnTRPwStandbyPeerVcId": zxAnTRPwStandbyPeerVcId,
       "zxAnTRPwOutboundLabel": zxAnTRPwOutboundLabel,
       "zxAnTRPwInboundLabel": zxAnTRPwInboundLabel,
       "zxAnTRPwOutboundTunnelLabel": zxAnTRPwOutboundTunnelLabel,
       "zxAnTRPwInboundTunnelLabel": zxAnTRPwInboundTunnelLabel,
       "zxAnTRPwPayloadSize": zxAnTRPwPayloadSize,
       "zxAnTRPwDstMac": zxAnTRPwDstMac,
       "zxAnTRPwVlanId": zxAnTRPwVlanId,
       "zxAnTRPwPrio": zxAnTRPwPrio,
       "zxAnTRPwRowStatus": zxAnTRPwRowStatus,
       "zxAnTRTdmSrcMacTable": zxAnTRTdmSrcMacTable,
       "zxAnTRTdmSrcMacEntry": zxAnTRTdmSrcMacEntry,
       "zxAnTRTdmSrcRackNo": zxAnTRTdmSrcRackNo,
       "zxAnTRTdmSrcShelfNo": zxAnTRTdmSrcShelfNo,
       "zxAnTRTdmSrcSlotNo": zxAnTRTdmSrcSlotNo,
       "zxAnTRTdmSrcMac": zxAnTRTdmSrcMac}
)
