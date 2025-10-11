# SNMP MIB module (HUAWEI-SECURITY-L2TP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/huawei/HUAWEI-SECURITY-L2TP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:22:37 2025
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

hwL2tpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Huawei_ObjectIdentity = ObjectIdentity
huawei = _Huawei_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011)
)
_HuaweiUtility_ObjectIdentity = ObjectIdentity
huaweiUtility = _HuaweiUtility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6)
)
_HwSecurity_ObjectIdentity = ObjectIdentity
hwSecurity = _HwSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122)
)
_HwL2tpMibObjects_ObjectIdentity = ObjectIdentity
hwL2tpMibObjects = _HwL2tpMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1)
)
_HwL2tpEnableFlag_Type = TruthValue
_HwL2tpEnableFlag_Object = MibScalar
hwL2tpEnableFlag = _HwL2tpEnableFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 1),
    _HwL2tpEnableFlag_Type()
)
hwL2tpEnableFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpEnableFlag.setStatus("current")
_HwL2tpGroupConfigTable_Object = MibTable
hwL2tpGroupConfigTable = _HwL2tpGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hwL2tpGroupConfigTable.setStatus("current")
_HwL2tpGroupConfigEntry_Object = MibTableRow
hwL2tpGroupConfigEntry = _HwL2tpGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 2, 1)
)
hwL2tpGroupConfigEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-L2TP-MIB", "hwL2tpGroupindex"),
)
if mibBuilder.loadTexts:
    hwL2tpGroupConfigEntry.setStatus("current")


class _HwL2tpGroupindex_Type(Integer32):
    """Custom type hwL2tpGroupindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_HwL2tpGroupindex_Type.__name__ = "Integer32"
_HwL2tpGroupindex_Object = MibTableColumn
hwL2tpGroupindex = _HwL2tpGroupindex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 2, 1, 1),
    _HwL2tpGroupindex_Type()
)
hwL2tpGroupindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2tpGroupindex.setStatus("current")


class _HwL2tpTunnelNumber_Type(Integer32):
    """Custom type hwL2tpTunnelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_HwL2tpTunnelNumber_Type.__name__ = "Integer32"
_HwL2tpTunnelNumber_Object = MibTableColumn
hwL2tpTunnelNumber = _HwL2tpTunnelNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 2, 1, 2),
    _HwL2tpTunnelNumber_Type()
)
hwL2tpTunnelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpTunnelNumber.setStatus("current")


class _HwL2tpGroupFlag_Type(Integer32):
    """Custom type hwL2tpGroupFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_HwL2tpGroupFlag_Type.__name__ = "Integer32"
_HwL2tpGroupFlag_Object = MibTableColumn
hwL2tpGroupFlag = _HwL2tpGroupFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 2, 1, 3),
    _HwL2tpGroupFlag_Type()
)
hwL2tpGroupFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2tpGroupFlag.setStatus("current")


class _HwL2tpGroupAuthentication_Type(TruthValue):
    """Custom type hwL2tpGroupAuthentication based on TruthValue"""
    defaultValue = 1


_HwL2tpGroupAuthentication_Type.__name__ = "TruthValue"
_HwL2tpGroupAuthentication_Object = MibTableColumn
hwL2tpGroupAuthentication = _HwL2tpGroupAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 2, 1, 4),
    _HwL2tpGroupAuthentication_Type()
)
hwL2tpGroupAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupAuthentication.setStatus("current")


class _HwL2tpGroupPassWord_Type(OctetString):
    """Custom type hwL2tpGroupPassWord based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwL2tpGroupPassWord_Type.__name__ = "OctetString"
_HwL2tpGroupPassWord_Object = MibTableColumn
hwL2tpGroupPassWord = _HwL2tpGroupPassWord_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 2, 1, 5),
    _HwL2tpGroupPassWord_Type()
)
hwL2tpGroupPassWord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupPassWord.setStatus("current")


class _HwL2tpGroupAvpHidden_Type(TruthValue):
    """Custom type hwL2tpGroupAvpHidden based on TruthValue"""
    defaultValue = 2


_HwL2tpGroupAvpHidden_Type.__name__ = "TruthValue"
_HwL2tpGroupAvpHidden_Object = MibTableColumn
hwL2tpGroupAvpHidden = _HwL2tpGroupAvpHidden_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 2, 1, 6),
    _HwL2tpGroupAvpHidden_Type()
)
hwL2tpGroupAvpHidden.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupAvpHidden.setStatus("current")


class _HwL2tpGroupName_Type(OctetString):
    """Custom type hwL2tpGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_HwL2tpGroupName_Type.__name__ = "OctetString"
_HwL2tpGroupName_Object = MibTableColumn
hwL2tpGroupName = _HwL2tpGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 2, 1, 7),
    _HwL2tpGroupName_Type()
)
hwL2tpGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupName.setStatus("current")


class _HwL2tpGroupRemoteName_Type(OctetString):
    """Custom type hwL2tpGroupRemoteName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_HwL2tpGroupRemoteName_Type.__name__ = "OctetString"
_HwL2tpGroupRemoteName_Object = MibTableColumn
hwL2tpGroupRemoteName = _HwL2tpGroupRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 2, 1, 8),
    _HwL2tpGroupRemoteName_Type()
)
hwL2tpGroupRemoteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupRemoteName.setStatus("current")


class _HwL2tpGroupRetransmit_Type(Integer32):
    """Custom type hwL2tpGroupRetransmit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HwL2tpGroupRetransmit_Type.__name__ = "Integer32"
_HwL2tpGroupRetransmit_Object = MibTableColumn
hwL2tpGroupRetransmit = _HwL2tpGroupRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 2, 1, 9),
    _HwL2tpGroupRetransmit_Type()
)
hwL2tpGroupRetransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupRetransmit.setStatus("current")
_HwL2tpGroupTimeout_Type = TimeInterval
_HwL2tpGroupTimeout_Object = MibTableColumn
hwL2tpGroupTimeout = _HwL2tpGroupTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 2, 1, 10),
    _HwL2tpGroupTimeout_Type()
)
hwL2tpGroupTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupTimeout.setStatus("current")
_HwL2tpGroupTimer_Type = TimeInterval
_HwL2tpGroupTimer_Object = MibTableColumn
hwL2tpGroupTimer = _HwL2tpGroupTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 2, 1, 11),
    _HwL2tpGroupTimer_Type()
)
hwL2tpGroupTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupTimer.setStatus("current")
_HwL2tpGroupLnsIP1_Type = IpAddress
_HwL2tpGroupLnsIP1_Object = MibTableColumn
hwL2tpGroupLnsIP1 = _HwL2tpGroupLnsIP1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 2, 1, 12),
    _HwL2tpGroupLnsIP1_Type()
)
hwL2tpGroupLnsIP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupLnsIP1.setStatus("current")
_HwL2tpGroupLnsIP2_Type = IpAddress
_HwL2tpGroupLnsIP2_Object = MibTableColumn
hwL2tpGroupLnsIP2 = _HwL2tpGroupLnsIP2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 2, 1, 13),
    _HwL2tpGroupLnsIP2_Type()
)
hwL2tpGroupLnsIP2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupLnsIP2.setStatus("current")
_HwL2tpGroupLnsIP3_Type = IpAddress
_HwL2tpGroupLnsIP3_Object = MibTableColumn
hwL2tpGroupLnsIP3 = _HwL2tpGroupLnsIP3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 2, 1, 14),
    _HwL2tpGroupLnsIP3_Type()
)
hwL2tpGroupLnsIP3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupLnsIP3.setStatus("current")
_HwL2tpGroupLnsIP4_Type = IpAddress
_HwL2tpGroupLnsIP4_Object = MibTableColumn
hwL2tpGroupLnsIP4 = _HwL2tpGroupLnsIP4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 2, 1, 15),
    _HwL2tpGroupLnsIP4_Type()
)
hwL2tpGroupLnsIP4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupLnsIP4.setStatus("current")
_HwL2tpGroupLnsIP5_Type = IpAddress
_HwL2tpGroupLnsIP5_Object = MibTableColumn
hwL2tpGroupLnsIP5 = _HwL2tpGroupLnsIP5_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 2, 1, 16),
    _HwL2tpGroupLnsIP5_Type()
)
hwL2tpGroupLnsIP5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupLnsIP5.setStatus("current")
_HwL2tpGroupForceChap_Type = TruthValue
_HwL2tpGroupForceChap_Object = MibTableColumn
hwL2tpGroupForceChap = _HwL2tpGroupForceChap_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 2, 1, 17),
    _HwL2tpGroupForceChap_Type()
)
hwL2tpGroupForceChap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupForceChap.setStatus("current")
_HwL2tpGroupForceLcp_Type = TruthValue
_HwL2tpGroupForceLcp_Object = MibTableColumn
hwL2tpGroupForceLcp = _HwL2tpGroupForceLcp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 2, 1, 18),
    _HwL2tpGroupForceLcp_Type()
)
hwL2tpGroupForceLcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupForceLcp.setStatus("current")


class _HwL2tpGroupVt_Type(Integer32):
    """Custom type hwL2tpGroupVt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
        ValueRangeConstraint(65535, 65535),
    )


_HwL2tpGroupVt_Type.__name__ = "Integer32"
_HwL2tpGroupVt_Object = MibTableColumn
hwL2tpGroupVt = _HwL2tpGroupVt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 2, 1, 19),
    _HwL2tpGroupVt_Type()
)
hwL2tpGroupVt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupVt.setStatus("current")
_HwL2tpGroupRowStatus_Type = RowStatus
_HwL2tpGroupRowStatus_Object = MibTableColumn
hwL2tpGroupRowStatus = _HwL2tpGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 2, 1, 20),
    _HwL2tpGroupRowStatus_Type()
)
hwL2tpGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupRowStatus.setStatus("current")
_HwL2tpTunnelTable_Object = MibTable
hwL2tpTunnelTable = _HwL2tpTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 3)
)
if mibBuilder.loadTexts:
    hwL2tpTunnelTable.setStatus("current")
_HwL2tpTunnelEntry_Object = MibTableRow
hwL2tpTunnelEntry = _HwL2tpTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 3, 1)
)
hwL2tpTunnelEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-L2TP-MIB", "hwL2tpTunnelIndex"),
)
if mibBuilder.loadTexts:
    hwL2tpTunnelEntry.setStatus("current")


class _HwL2tpTunnelIndex_Type(Integer32):
    """Custom type hwL2tpTunnelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwL2tpTunnelIndex_Type.__name__ = "Integer32"
_HwL2tpTunnelIndex_Object = MibTableColumn
hwL2tpTunnelIndex = _HwL2tpTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 3, 1, 1),
    _HwL2tpTunnelIndex_Type()
)
hwL2tpTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2tpTunnelIndex.setStatus("current")


class _HwL2tpTunnelLocalID_Type(Integer32):
    """Custom type hwL2tpTunnelLocalID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwL2tpTunnelLocalID_Type.__name__ = "Integer32"
_HwL2tpTunnelLocalID_Object = MibTableColumn
hwL2tpTunnelLocalID = _HwL2tpTunnelLocalID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 3, 1, 2),
    _HwL2tpTunnelLocalID_Type()
)
hwL2tpTunnelLocalID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2tpTunnelLocalID.setStatus("current")


class _HwL2tpTunnelRemoteID_Type(Integer32):
    """Custom type hwL2tpTunnelRemoteID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwL2tpTunnelRemoteID_Type.__name__ = "Integer32"
_HwL2tpTunnelRemoteID_Object = MibTableColumn
hwL2tpTunnelRemoteID = _HwL2tpTunnelRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 3, 1, 3),
    _HwL2tpTunnelRemoteID_Type()
)
hwL2tpTunnelRemoteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2tpTunnelRemoteID.setStatus("current")
_HwL2tpTunnelRemoteName_Type = OctetString
_HwL2tpTunnelRemoteName_Object = MibTableColumn
hwL2tpTunnelRemoteName = _HwL2tpTunnelRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 3, 1, 4),
    _HwL2tpTunnelRemoteName_Type()
)
hwL2tpTunnelRemoteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2tpTunnelRemoteName.setStatus("current")
_HwL2tpTunnelRemoteIP_Type = IpAddress
_HwL2tpTunnelRemoteIP_Object = MibTableColumn
hwL2tpTunnelRemoteIP = _HwL2tpTunnelRemoteIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 3, 1, 5),
    _HwL2tpTunnelRemoteIP_Type()
)
hwL2tpTunnelRemoteIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2tpTunnelRemoteIP.setStatus("current")


class _HwL2tpTunnelRemotePort_Type(Integer32):
    """Custom type hwL2tpTunnelRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwL2tpTunnelRemotePort_Type.__name__ = "Integer32"
_HwL2tpTunnelRemotePort_Object = MibTableColumn
hwL2tpTunnelRemotePort = _HwL2tpTunnelRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 3, 1, 6),
    _HwL2tpTunnelRemotePort_Type()
)
hwL2tpTunnelRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2tpTunnelRemotePort.setStatus("current")


class _HwL2tpTunnelSessionNum_Type(Integer32):
    """Custom type hwL2tpTunnelSessionNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwL2tpTunnelSessionNum_Type.__name__ = "Integer32"
_HwL2tpTunnelSessionNum_Object = MibTableColumn
hwL2tpTunnelSessionNum = _HwL2tpTunnelSessionNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 3, 1, 7),
    _HwL2tpTunnelSessionNum_Type()
)
hwL2tpTunnelSessionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2tpTunnelSessionNum.setStatus("current")
_HwL2tpLnsGroupRowStatus_Type = RowStatus
_HwL2tpLnsGroupRowStatus_Object = MibTableColumn
hwL2tpLnsGroupRowStatus = _HwL2tpLnsGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 3, 1, 8),
    _HwL2tpLnsGroupRowStatus_Type()
)
hwL2tpLnsGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpLnsGroupRowStatus.setStatus("current")
_HwL2tpSessionTable_Object = MibTable
hwL2tpSessionTable = _HwL2tpSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 4)
)
if mibBuilder.loadTexts:
    hwL2tpSessionTable.setStatus("current")
_HwL2tpSessionEntry_Object = MibTableRow
hwL2tpSessionEntry = _HwL2tpSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 4, 1)
)
hwL2tpSessionEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-L2TP-MIB", "hwL2tpSessionIndex"),
)
if mibBuilder.loadTexts:
    hwL2tpSessionEntry.setStatus("current")


class _HwL2tpSessionIndex_Type(Integer32):
    """Custom type hwL2tpSessionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwL2tpSessionIndex_Type.__name__ = "Integer32"
_HwL2tpSessionIndex_Object = MibTableColumn
hwL2tpSessionIndex = _HwL2tpSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 4, 1, 1),
    _HwL2tpSessionIndex_Type()
)
hwL2tpSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2tpSessionIndex.setStatus("current")


class _HwL2tpSessionTunnelID_Type(Integer32):
    """Custom type hwL2tpSessionTunnelID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwL2tpSessionTunnelID_Type.__name__ = "Integer32"
_HwL2tpSessionTunnelID_Object = MibTableColumn
hwL2tpSessionTunnelID = _HwL2tpSessionTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 4, 1, 2),
    _HwL2tpSessionTunnelID_Type()
)
hwL2tpSessionTunnelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2tpSessionTunnelID.setStatus("current")


class _HwL2tpSessionLocalSID_Type(Integer32):
    """Custom type hwL2tpSessionLocalSID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwL2tpSessionLocalSID_Type.__name__ = "Integer32"
_HwL2tpSessionLocalSID_Object = MibTableColumn
hwL2tpSessionLocalSID = _HwL2tpSessionLocalSID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 4, 1, 3),
    _HwL2tpSessionLocalSID_Type()
)
hwL2tpSessionLocalSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2tpSessionLocalSID.setStatus("current")


class _HwL2tpSessionRemoteSID_Type(Integer32):
    """Custom type hwL2tpSessionRemoteSID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwL2tpSessionRemoteSID_Type.__name__ = "Integer32"
_HwL2tpSessionRemoteSID_Object = MibTableColumn
hwL2tpSessionRemoteSID = _HwL2tpSessionRemoteSID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 4, 1, 4),
    _HwL2tpSessionRemoteSID_Type()
)
hwL2tpSessionRemoteSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2tpSessionRemoteSID.setStatus("current")
_HwL2tpSessionUserName_Type = OctetString
_HwL2tpSessionUserName_Object = MibTableColumn
hwL2tpSessionUserName = _HwL2tpSessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 4, 1, 5),
    _HwL2tpSessionUserName_Type()
)
hwL2tpSessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2tpSessionUserName.setStatus("current")
_HwL2tpSessionUserOnlineTime_Type = DateAndTime
_HwL2tpSessionUserOnlineTime_Object = MibTableColumn
hwL2tpSessionUserOnlineTime = _HwL2tpSessionUserOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 4, 1, 6),
    _HwL2tpSessionUserOnlineTime_Type()
)
hwL2tpSessionUserOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2tpSessionUserOnlineTime.setStatus("current")


class _HwL2tpSessionState_Type(Integer32):
    """Custom type hwL2tpSessionState based on Integer32"""
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
        *(("sessionIdle", 1),
          ("sessionConnecting", 2),
          ("sessionEstablished", 3),
          ("sessionDisconnecting", 4))
    )


_HwL2tpSessionState_Type.__name__ = "Integer32"
_HwL2tpSessionState_Object = MibTableColumn
hwL2tpSessionState = _HwL2tpSessionState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 4, 1, 7),
    _HwL2tpSessionState_Type()
)
hwL2tpSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2tpSessionState.setStatus("current")


class _HwL2tpSessionCallType_Type(Integer32):
    """Custom type hwL2tpSessionCallType based on Integer32"""
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
        *(("lacIncoming", 1),
          ("lnsIncoming", 2),
          ("lacOutgoing", 3),
          ("lnsOutgoing", 4))
    )


_HwL2tpSessionCallType_Type.__name__ = "Integer32"
_HwL2tpSessionCallType_Object = MibTableColumn
hwL2tpSessionCallType = _HwL2tpSessionCallType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 4, 1, 8),
    _HwL2tpSessionCallType_Type()
)
hwL2tpSessionCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2tpSessionCallType.setStatus("current")
_HwL2tpSessionSerialNumber_Type = Unsigned32
_HwL2tpSessionSerialNumber_Object = MibTableColumn
hwL2tpSessionSerialNumber = _HwL2tpSessionSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 4, 1, 9),
    _HwL2tpSessionSerialNumber_Type()
)
hwL2tpSessionSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2tpSessionSerialNumber.setStatus("current")
_HwL2tpTrapObject_ObjectIdentity = ObjectIdentity
hwL2tpTrapObject = _HwL2tpTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 7)
)


class _HwL2tpTunnelindex_Type(Integer32):
    """Custom type hwL2tpTunnelindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwL2tpTunnelindex_Type.__name__ = "Integer32"
_HwL2tpTunnelindex_Object = MibScalar
hwL2tpTunnelindex = _HwL2tpTunnelindex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 7, 1),
    _HwL2tpTunnelindex_Type()
)
hwL2tpTunnelindex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwL2tpTunnelindex.setStatus("current")


class _HwL2tpSessionindex_Type(Integer32):
    """Custom type hwL2tpSessionindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwL2tpSessionindex_Type.__name__ = "Integer32"
_HwL2tpSessionindex_Object = MibScalar
hwL2tpSessionindex = _HwL2tpSessionindex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 7, 2),
    _HwL2tpSessionindex_Type()
)
hwL2tpSessionindex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwL2tpSessionindex.setStatus("current")
_HwL2tpTunnelRemoteAddr_Type = IpAddress
_HwL2tpTunnelRemoteAddr_Object = MibScalar
hwL2tpTunnelRemoteAddr = _HwL2tpTunnelRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 7, 3),
    _HwL2tpTunnelRemoteAddr_Type()
)
hwL2tpTunnelRemoteAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwL2tpTunnelRemoteAddr.setStatus("current")
_HwL2tpTunnelUserName_Type = OctetString
_HwL2tpTunnelUserName_Object = MibScalar
hwL2tpTunnelUserName = _HwL2tpTunnelUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 7, 4),
    _HwL2tpTunnelUserName_Type()
)
hwL2tpTunnelUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwL2tpTunnelUserName.setStatus("current")
_HwL2tpTunnelStartTime_Type = DateAndTime
_HwL2tpTunnelStartTime_Object = MibScalar
hwL2tpTunnelStartTime = _HwL2tpTunnelStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 7, 5),
    _HwL2tpTunnelStartTime_Type()
)
hwL2tpTunnelStartTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwL2tpTunnelStartTime.setStatus("current")
_HwL2tpTrap_ObjectIdentity = ObjectIdentity
hwL2tpTrap = _HwL2tpTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 8)
)
_HwL2tpNotifications_ObjectIdentity = ObjectIdentity
hwL2tpNotifications = _HwL2tpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 8, 1)
)
_HwL2tpMibConformance_ObjectIdentity = ObjectIdentity
hwL2tpMibConformance = _HwL2tpMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 10)
)
_HwL2tpMibGroups_ObjectIdentity = ObjectIdentity
hwL2tpMibGroups = _HwL2tpMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 10, 2)
)

# Managed Objects groups

hwL2tpGroupConfigTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 10, 2, 2)
)
hwL2tpGroupConfigTableGroup.setObjects(
      *(("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpTunnelNumber"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpGroupFlag"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpGroupAuthentication"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpGroupPassWord"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpGroupAvpHidden"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpGroupName"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpGroupRemoteName"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpGroupRetransmit"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpGroupTimeout"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpGroupTimer"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpGroupLnsIP1"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpGroupLnsIP2"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpGroupLnsIP3"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpGroupLnsIP4"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpGroupLnsIP5"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpGroupForceChap"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpGroupForceLcp"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpGroupVt"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpGroupRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2tpGroupConfigTableGroup.setStatus("current")

hwL2tpTunnelTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 10, 2, 3)
)
hwL2tpTunnelTableGroup.setObjects(
      *(("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpTunnelLocalID"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpTunnelRemoteID"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpTunnelRemoteName"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpTunnelRemoteIP"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpTunnelRemotePort"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpTunnelSessionNum"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpLnsGroupRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2tpTunnelTableGroup.setStatus("current")

hwL2tpSessionTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 10, 2, 4)
)
hwL2tpSessionTableGroup.setObjects(
      *(("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpSessionTunnelID"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpSessionLocalSID"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpSessionRemoteSID"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpSessionUserName"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpSessionUserOnlineTime"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpSessionState"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpSessionCallType"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpSessionSerialNumber"))
)
if mibBuilder.loadTexts:
    hwL2tpSessionTableGroup.setStatus("current")

hwL2tpTrapObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 10, 2, 5)
)
hwL2tpTrapObjectGroup.setObjects(
      *(("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpTunnelindex"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpSessionindex"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpTunnelRemoteAddr"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpTunnelUserName"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpTunnelStartTime"))
)
if mibBuilder.loadTexts:
    hwL2tpTrapObjectGroup.setStatus("current")


# Notification objects

hwL2tpSessionStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 8, 1, 1)
)
hwL2tpSessionStart.setObjects(
      *(("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpTunnelindex"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpSessionindex"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpTunnelRemoteAddr"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpTunnelUserName"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpTunnelStartTime"))
)
if mibBuilder.loadTexts:
    hwL2tpSessionStart.setStatus(
        "current"
    )

hwL2tpSessionStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 8, 1, 2)
)
hwL2tpSessionStop.setObjects(
      *(("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpTunnelindex"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpSessionindex"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpTunnelRemoteAddr"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpTunnelUserName"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpTunnelStartTime"))
)
if mibBuilder.loadTexts:
    hwL2tpSessionStop.setStatus(
        "current"
    )


# Notifications groups

hwL2tpTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 10, 2, 6)
)
hwL2tpTrapGroup.setObjects(
      *(("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpSessionStart"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpSessionStop"))
)
if mibBuilder.loadTexts:
    hwL2tpTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwL2tpMibCompliances = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 2, 1, 10, 1)
)
hwL2tpMibCompliances.setObjects(
      *(("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpGroupConfigTableGroup"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpTunnelTableGroup"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpSessionTableGroup"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpTrapObjectGroup"),
        ("HUAWEI-SECURITY-L2TP-MIB", "hwL2tpTrapGroup"))
)
if mibBuilder.loadTexts:
    hwL2tpMibCompliances.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-SECURITY-L2TP-MIB",
    **{"huawei": huawei,
       "huaweiUtility": huaweiUtility,
       "hwSecurity": hwSecurity,
       "hwL2tpMib": hwL2tpMib,
       "hwL2tpMibObjects": hwL2tpMibObjects,
       "hwL2tpEnableFlag": hwL2tpEnableFlag,
       "hwL2tpGroupConfigTable": hwL2tpGroupConfigTable,
       "hwL2tpGroupConfigEntry": hwL2tpGroupConfigEntry,
       "hwL2tpGroupindex": hwL2tpGroupindex,
       "hwL2tpTunnelNumber": hwL2tpTunnelNumber,
       "hwL2tpGroupFlag": hwL2tpGroupFlag,
       "hwL2tpGroupAuthentication": hwL2tpGroupAuthentication,
       "hwL2tpGroupPassWord": hwL2tpGroupPassWord,
       "hwL2tpGroupAvpHidden": hwL2tpGroupAvpHidden,
       "hwL2tpGroupName": hwL2tpGroupName,
       "hwL2tpGroupRemoteName": hwL2tpGroupRemoteName,
       "hwL2tpGroupRetransmit": hwL2tpGroupRetransmit,
       "hwL2tpGroupTimeout": hwL2tpGroupTimeout,
       "hwL2tpGroupTimer": hwL2tpGroupTimer,
       "hwL2tpGroupLnsIP1": hwL2tpGroupLnsIP1,
       "hwL2tpGroupLnsIP2": hwL2tpGroupLnsIP2,
       "hwL2tpGroupLnsIP3": hwL2tpGroupLnsIP3,
       "hwL2tpGroupLnsIP4": hwL2tpGroupLnsIP4,
       "hwL2tpGroupLnsIP5": hwL2tpGroupLnsIP5,
       "hwL2tpGroupForceChap": hwL2tpGroupForceChap,
       "hwL2tpGroupForceLcp": hwL2tpGroupForceLcp,
       "hwL2tpGroupVt": hwL2tpGroupVt,
       "hwL2tpGroupRowStatus": hwL2tpGroupRowStatus,
       "hwL2tpTunnelTable": hwL2tpTunnelTable,
       "hwL2tpTunnelEntry": hwL2tpTunnelEntry,
       "hwL2tpTunnelIndex": hwL2tpTunnelIndex,
       "hwL2tpTunnelLocalID": hwL2tpTunnelLocalID,
       "hwL2tpTunnelRemoteID": hwL2tpTunnelRemoteID,
       "hwL2tpTunnelRemoteName": hwL2tpTunnelRemoteName,
       "hwL2tpTunnelRemoteIP": hwL2tpTunnelRemoteIP,
       "hwL2tpTunnelRemotePort": hwL2tpTunnelRemotePort,
       "hwL2tpTunnelSessionNum": hwL2tpTunnelSessionNum,
       "hwL2tpLnsGroupRowStatus": hwL2tpLnsGroupRowStatus,
       "hwL2tpSessionTable": hwL2tpSessionTable,
       "hwL2tpSessionEntry": hwL2tpSessionEntry,
       "hwL2tpSessionIndex": hwL2tpSessionIndex,
       "hwL2tpSessionTunnelID": hwL2tpSessionTunnelID,
       "hwL2tpSessionLocalSID": hwL2tpSessionLocalSID,
       "hwL2tpSessionRemoteSID": hwL2tpSessionRemoteSID,
       "hwL2tpSessionUserName": hwL2tpSessionUserName,
       "hwL2tpSessionUserOnlineTime": hwL2tpSessionUserOnlineTime,
       "hwL2tpSessionState": hwL2tpSessionState,
       "hwL2tpSessionCallType": hwL2tpSessionCallType,
       "hwL2tpSessionSerialNumber": hwL2tpSessionSerialNumber,
       "hwL2tpTrapObject": hwL2tpTrapObject,
       "hwL2tpTunnelindex": hwL2tpTunnelindex,
       "hwL2tpSessionindex": hwL2tpSessionindex,
       "hwL2tpTunnelRemoteAddr": hwL2tpTunnelRemoteAddr,
       "hwL2tpTunnelUserName": hwL2tpTunnelUserName,
       "hwL2tpTunnelStartTime": hwL2tpTunnelStartTime,
       "hwL2tpTrap": hwL2tpTrap,
       "hwL2tpNotifications": hwL2tpNotifications,
       "hwL2tpSessionStart": hwL2tpSessionStart,
       "hwL2tpSessionStop": hwL2tpSessionStop,
       "hwL2tpMibConformance": hwL2tpMibConformance,
       "hwL2tpMibCompliances": hwL2tpMibCompliances,
       "hwL2tpMibGroups": hwL2tpMibGroups,
       "hwL2tpGroupConfigTableGroup": hwL2tpGroupConfigTableGroup,
       "hwL2tpTunnelTableGroup": hwL2tpTunnelTableGroup,
       "hwL2tpSessionTableGroup": hwL2tpSessionTableGroup,
       "hwL2tpTrapObjectGroup": hwL2tpTrapObjectGroup,
       "hwL2tpTrapGroup": hwL2tpTrapGroup}
)
