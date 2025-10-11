# SNMP MIB module (RAISECOM-CFM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-CFM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:37:23 2025
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

(Dot1agCfmCcmInterval,
 Dot1agCfmLowestAlarmPri,
 Dot1agCfmMDLevel,
 Dot1agCfmMDLevelOrNone,
 Dot1agCfmMaintAssocName,
 Dot1agCfmMaintAssocNameType,
 Dot1agCfmMepDefects,
 Dot1agCfmMepId,
 dot1agCfmMaCompPrimaryVlanId,
 dot1agCfmMaIndex,
 dot1agCfmMdIndex,
 dot1agCfmMepDbRMepIdentifier,
 dot1agCfmMepIdentifier) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmCcmInterval",
    "Dot1agCfmLowestAlarmPri",
    "Dot1agCfmMDLevel",
    "Dot1agCfmMDLevelOrNone",
    "Dot1agCfmMaintAssocName",
    "Dot1agCfmMaintAssocNameType",
    "Dot1agCfmMepDefects",
    "Dot1agCfmMepId",
    "dot1agCfmMaCompPrimaryVlanId",
    "dot1agCfmMaIndex",
    "dot1agCfmMdIndex",
    "dot1agCfmMepDbRMepIdentifier",
    "dot1agCfmMepIdentifier")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(VlanId,
 VlanIdOrNone) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId",
    "VlanIdOrNone")

(iscomSwitch,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "iscomSwitch")

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

(EnableVar,) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar")


# MODULE-IDENTITY

rcCfm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26)
)
if mibBuilder.loadTexts:
    rcCfm.setRevisions(
        ("2007-11-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcCfmBridge_ObjectIdentity = ObjectIdentity
rcCfmBridge = _RcCfmBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 1)
)


class _RcCfmBridgeAdminCfm_Type(EnableVar):
    """Custom type rcCfmBridgeAdminCfm based on EnableVar"""
    defaultValue = 2


_RcCfmBridgeAdminCfm_Type.__name__ = "EnableVar"
_RcCfmBridgeAdminCfm_Object = MibScalar
rcCfmBridgeAdminCfm = _RcCfmBridgeAdminCfm_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 1, 1),
    _RcCfmBridgeAdminCfm_Type()
)
rcCfmBridgeAdminCfm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmBridgeAdminCfm.setStatus("current")


class _RcCfmBridgeCcmDbArchiveHoldtime_Type(Unsigned32):
    """Custom type rcCfmBridgeCcmDbArchiveHoldtime based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RcCfmBridgeCcmDbArchiveHoldtime_Type.__name__ = "Unsigned32"
_RcCfmBridgeCcmDbArchiveHoldtime_Object = MibScalar
rcCfmBridgeCcmDbArchiveHoldtime = _RcCfmBridgeCcmDbArchiveHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 1, 2),
    _RcCfmBridgeCcmDbArchiveHoldtime_Type()
)
rcCfmBridgeCcmDbArchiveHoldtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmBridgeCcmDbArchiveHoldtime.setStatus("current")


class _RcCfmBridgeTracerouteCacheEnable_Type(TruthValue):
    """Custom type rcCfmBridgeTracerouteCacheEnable based on TruthValue"""
    defaultValue = 2


_RcCfmBridgeTracerouteCacheEnable_Type.__name__ = "TruthValue"
_RcCfmBridgeTracerouteCacheEnable_Object = MibScalar
rcCfmBridgeTracerouteCacheEnable = _RcCfmBridgeTracerouteCacheEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 1, 3),
    _RcCfmBridgeTracerouteCacheEnable_Type()
)
rcCfmBridgeTracerouteCacheEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmBridgeTracerouteCacheEnable.setStatus("current")


class _RcCfmBridgeTracerouteCacheHoldtime_Type(Unsigned32):
    """Custom type rcCfmBridgeTracerouteCacheHoldtime based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RcCfmBridgeTracerouteCacheHoldtime_Type.__name__ = "Unsigned32"
_RcCfmBridgeTracerouteCacheHoldtime_Object = MibScalar
rcCfmBridgeTracerouteCacheHoldtime = _RcCfmBridgeTracerouteCacheHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 1, 4),
    _RcCfmBridgeTracerouteCacheHoldtime_Type()
)
rcCfmBridgeTracerouteCacheHoldtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmBridgeTracerouteCacheHoldtime.setStatus("current")


class _RcCfmBridgeTracerouteCacheSize_Type(Unsigned32):
    """Custom type rcCfmBridgeTracerouteCacheSize based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_RcCfmBridgeTracerouteCacheSize_Type.__name__ = "Unsigned32"
_RcCfmBridgeTracerouteCacheSize_Object = MibScalar
rcCfmBridgeTracerouteCacheSize = _RcCfmBridgeTracerouteCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 1, 5),
    _RcCfmBridgeTracerouteCacheSize_Type()
)
rcCfmBridgeTracerouteCacheSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmBridgeTracerouteCacheSize.setStatus("current")


class _RcCfmBridgeTracerouteCacheClear_Type(TruthValue):
    """Custom type rcCfmBridgeTracerouteCacheClear based on TruthValue"""
    defaultValue = 2


_RcCfmBridgeTracerouteCacheClear_Type.__name__ = "TruthValue"
_RcCfmBridgeTracerouteCacheClear_Object = MibScalar
rcCfmBridgeTracerouteCacheClear = _RcCfmBridgeTracerouteCacheClear_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 1, 6),
    _RcCfmBridgeTracerouteCacheClear_Type()
)
rcCfmBridgeTracerouteCacheClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmBridgeTracerouteCacheClear.setStatus("current")


class _RcCfmBridgeTrapConfig_Type(Dot1agCfmLowestAlarmPri):
    """Custom type rcCfmBridgeTrapConfig based on Dot1agCfmLowestAlarmPri"""
    defaultValue = 6


_RcCfmBridgeTrapConfig_Type.__name__ = "Dot1agCfmLowestAlarmPri"
_RcCfmBridgeTrapConfig_Object = MibScalar
rcCfmBridgeTrapConfig = _RcCfmBridgeTrapConfig_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 1, 7),
    _RcCfmBridgeTrapConfig_Type()
)
rcCfmBridgeTrapConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmBridgeTrapConfig.setStatus("deprecated")


class _RcCfmBridgeRmepAgeTime_Type(Unsigned32):
    """Custom type rcCfmBridgeRmepAgeTime based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RcCfmBridgeRmepAgeTime_Type.__name__ = "Unsigned32"
_RcCfmBridgeRmepAgeTime_Object = MibScalar
rcCfmBridgeRmepAgeTime = _RcCfmBridgeRmepAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 1, 8),
    _RcCfmBridgeRmepAgeTime_Type()
)
rcCfmBridgeRmepAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmBridgeRmepAgeTime.setStatus("current")


class _RcCfmBridgeMode_Type(Integer32):
    """Custom type rcCfmBridgeMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multicast", 1),
          ("unicast", 2))
    )


_RcCfmBridgeMode_Type.__name__ = "Integer32"
_RcCfmBridgeMode_Object = MibScalar
rcCfmBridgeMode = _RcCfmBridgeMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 1, 9),
    _RcCfmBridgeMode_Type()
)
rcCfmBridgeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmBridgeMode.setStatus("current")


class _RcCfmLinkVlanList_Type(OctetString):
    """Custom type rcCfmLinkVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512


_RcCfmLinkVlanList_Type.__name__ = "OctetString"
_RcCfmLinkVlanList_Object = MibScalar
rcCfmLinkVlanList = _RcCfmLinkVlanList_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 1, 10),
    _RcCfmLinkVlanList_Type()
)
rcCfmLinkVlanList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcCfmLinkVlanList.setStatus("current")
_RcCfmIfTable_Object = MibTable
rcCfmIfTable = _RcCfmIfTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 2)
)
if mibBuilder.loadTexts:
    rcCfmIfTable.setStatus("current")
_RcCfmIfEntry_Object = MibTableRow
rcCfmIfEntry = _RcCfmIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 2, 1)
)
rcCfmIfEntry.setIndexNames(
    (0, "RAISECOM-CFM-MIB", "rcCfmIfIndex"),
)
if mibBuilder.loadTexts:
    rcCfmIfEntry.setStatus("current")
_RcCfmIfIndex_Type = InterfaceIndex
_RcCfmIfIndex_Object = MibTableColumn
rcCfmIfIndex = _RcCfmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 2, 1, 1),
    _RcCfmIfIndex_Type()
)
rcCfmIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcCfmIfIndex.setStatus("current")


class _RcCfmIfAdminCfm_Type(EnableVar):
    """Custom type rcCfmIfAdminCfm based on EnableVar"""
    defaultValue = 1


_RcCfmIfAdminCfm_Type.__name__ = "EnableVar"
_RcCfmIfAdminCfm_Object = MibTableColumn
rcCfmIfAdminCfm = _RcCfmIfAdminCfm_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 2, 1, 2),
    _RcCfmIfAdminCfm_Type()
)
rcCfmIfAdminCfm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmIfAdminCfm.setStatus("current")
_RcCfmIfMipLevel_Type = Dot1agCfmMDLevelOrNone
_RcCfmIfMipLevel_Object = MibTableColumn
rcCfmIfMipLevel = _RcCfmIfMipLevel_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 2, 1, 3),
    _RcCfmIfMipLevel_Type()
)
rcCfmIfMipLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmIfMipLevel.setStatus("deprecated")
_RcCfmMdTable_Object = MibTable
rcCfmMdTable = _RcCfmMdTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 3)
)
if mibBuilder.loadTexts:
    rcCfmMdTable.setStatus("current")
_RcCfmMdEntry_Object = MibTableRow
rcCfmMdEntry = _RcCfmMdEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 3, 1)
)
rcCfmMdEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
)
if mibBuilder.loadTexts:
    rcCfmMdEntry.setStatus("current")


class _RcCfmMdCcmRMpClear_Type(TruthValue):
    """Custom type rcCfmMdCcmRMpClear based on TruthValue"""
    defaultValue = 2


_RcCfmMdCcmRMpClear_Type.__name__ = "TruthValue"
_RcCfmMdCcmRMpClear_Object = MibTableColumn
rcCfmMdCcmRMpClear = _RcCfmMdCcmRMpClear_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 3, 1, 1),
    _RcCfmMdCcmRMpClear_Type()
)
rcCfmMdCcmRMpClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmMdCcmRMpClear.setStatus("current")
_RcCfmErrorCcmTable_Object = MibTable
rcCfmErrorCcmTable = _RcCfmErrorCcmTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 4)
)
if mibBuilder.loadTexts:
    rcCfmErrorCcmTable.setStatus("current")
_RcCfmErrorCcmEntry_Object = MibTableRow
rcCfmErrorCcmEntry = _RcCfmErrorCcmEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 4, 1)
)
rcCfmErrorCcmEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "RAISECOM-CFM-MIB", "rcCfmErrorCcmRMepId"),
    (0, "RAISECOM-CFM-MIB", "rcCfmErrorCcmIndex"),
)
if mibBuilder.loadTexts:
    rcCfmErrorCcmEntry.setStatus("current")
_RcCfmErrorCcmRMepId_Type = Dot1agCfmMepId
_RcCfmErrorCcmRMepId_Object = MibTableColumn
rcCfmErrorCcmRMepId = _RcCfmErrorCcmRMepId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 4, 1, 1),
    _RcCfmErrorCcmRMepId_Type()
)
rcCfmErrorCcmRMepId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcCfmErrorCcmRMepId.setStatus("current")


class _RcCfmErrorCcmIndex_Type(Unsigned32):
    """Custom type rcCfmErrorCcmIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RcCfmErrorCcmIndex_Type.__name__ = "Unsigned32"
_RcCfmErrorCcmIndex_Object = MibTableColumn
rcCfmErrorCcmIndex = _RcCfmErrorCcmIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 4, 1, 2),
    _RcCfmErrorCcmIndex_Type()
)
rcCfmErrorCcmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcCfmErrorCcmIndex.setStatus("current")
_RcCfmErrorCcmLevel_Type = Dot1agCfmMDLevel
_RcCfmErrorCcmLevel_Object = MibTableColumn
rcCfmErrorCcmLevel = _RcCfmErrorCcmLevel_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 4, 1, 3),
    _RcCfmErrorCcmLevel_Type()
)
rcCfmErrorCcmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmErrorCcmLevel.setStatus("current")
_RcCfmErrorCcmVlan_Type = VlanIdOrNone
_RcCfmErrorCcmVlan_Object = MibTableColumn
rcCfmErrorCcmVlan = _RcCfmErrorCcmVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 4, 1, 4),
    _RcCfmErrorCcmVlan_Type()
)
rcCfmErrorCcmVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmErrorCcmVlan.setStatus("current")


class _RcCfmErrorCcmRecvMdName_Type(OctetString):
    """Custom type rcCfmErrorCcmRecvMdName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_RcCfmErrorCcmRecvMdName_Type.__name__ = "OctetString"
_RcCfmErrorCcmRecvMdName_Object = MibTableColumn
rcCfmErrorCcmRecvMdName = _RcCfmErrorCcmRecvMdName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 4, 1, 5),
    _RcCfmErrorCcmRecvMdName_Type()
)
rcCfmErrorCcmRecvMdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmErrorCcmRecvMdName.setStatus("current")


class _RcCfmErrorCcmMaid_Type(OctetString):
    """Custom type rcCfmErrorCcmMaid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 44),
    )


_RcCfmErrorCcmMaid_Type.__name__ = "OctetString"
_RcCfmErrorCcmMaid_Object = MibTableColumn
rcCfmErrorCcmMaid = _RcCfmErrorCcmMaid_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 4, 1, 6),
    _RcCfmErrorCcmMaid_Type()
)
rcCfmErrorCcmMaid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmErrorCcmMaid.setStatus("current")
_RcCfmErrorCcmMacAddress_Type = MacAddress
_RcCfmErrorCcmMacAddress_Object = MibTableColumn
rcCfmErrorCcmMacAddress = _RcCfmErrorCcmMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 4, 1, 7),
    _RcCfmErrorCcmMacAddress_Type()
)
rcCfmErrorCcmMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmErrorCcmMacAddress.setStatus("current")
_RcCfmErrorCcmErrorType_Type = Dot1agCfmMepDefects
_RcCfmErrorCcmErrorType_Object = MibTableColumn
rcCfmErrorCcmErrorType = _RcCfmErrorCcmErrorType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 4, 1, 8),
    _RcCfmErrorCcmErrorType_Type()
)
rcCfmErrorCcmErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmErrorCcmErrorType.setStatus("current")


class _RcCfmErrorCcmHoldTime_Type(Unsigned32):
    """Custom type rcCfmErrorCcmHoldTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RcCfmErrorCcmHoldTime_Type.__name__ = "Unsigned32"
_RcCfmErrorCcmHoldTime_Object = MibTableColumn
rcCfmErrorCcmHoldTime = _RcCfmErrorCcmHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 4, 1, 9),
    _RcCfmErrorCcmHoldTime_Type()
)
rcCfmErrorCcmHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmErrorCcmHoldTime.setStatus("current")
_RcCfmErrorCcmClear_Type = TruthValue
_RcCfmErrorCcmClear_Object = MibTableColumn
rcCfmErrorCcmClear = _RcCfmErrorCcmClear_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 4, 1, 10),
    _RcCfmErrorCcmClear_Type()
)
rcCfmErrorCcmClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmErrorCcmClear.setStatus("current")
_RcCfmLtmDbTable_Object = MibTable
rcCfmLtmDbTable = _RcCfmLtmDbTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 5)
)
if mibBuilder.loadTexts:
    rcCfmLtmDbTable.setStatus("current")
_RcCfmLtmDbEntry_Object = MibTableRow
rcCfmLtmDbEntry = _RcCfmLtmDbEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 5, 1)
)
rcCfmLtmDbEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "RAISECOM-CFM-MIB", "rcCfmLtmDbTransactionId"),
)
if mibBuilder.loadTexts:
    rcCfmLtmDbEntry.setStatus("current")


class _RcCfmLtmDbTransactionId_Type(Unsigned32):
    """Custom type rcCfmLtmDbTransactionId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RcCfmLtmDbTransactionId_Type.__name__ = "Unsigned32"
_RcCfmLtmDbTransactionId_Object = MibTableColumn
rcCfmLtmDbTransactionId = _RcCfmLtmDbTransactionId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 5, 1, 1),
    _RcCfmLtmDbTransactionId_Type()
)
rcCfmLtmDbTransactionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcCfmLtmDbTransactionId.setStatus("current")
_RcCfmLtmDbTargetMacAddress_Type = MacAddress
_RcCfmLtmDbTargetMacAddress_Object = MibTableColumn
rcCfmLtmDbTargetMacAddress = _RcCfmLtmDbTargetMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 5, 1, 2),
    _RcCfmLtmDbTargetMacAddress_Type()
)
rcCfmLtmDbTargetMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmLtmDbTargetMacAddress.setStatus("current")
_RcCfmMepDbExTable_Object = MibTable
rcCfmMepDbExTable = _RcCfmMepDbExTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 6)
)
if mibBuilder.loadTexts:
    rcCfmMepDbExTable.setStatus("current")
_RcCfmMepDbExEntry_Object = MibTableRow
rcCfmMepDbExEntry = _RcCfmMepDbExEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 6, 1)
)
rcCfmMepDbExEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepDbRMepIdentifier"),
)
if mibBuilder.loadTexts:
    rcCfmMepDbExEntry.setStatus("current")


class _RcCfmMepDbExEntryHoldTime_Type(Unsigned32):
    """Custom type rcCfmMepDbExEntryHoldTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RcCfmMepDbExEntryHoldTime_Type.__name__ = "Unsigned32"
_RcCfmMepDbExEntryHoldTime_Object = MibTableColumn
rcCfmMepDbExEntryHoldTime = _RcCfmMepDbExEntryHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 6, 1, 1),
    _RcCfmMepDbExEntryHoldTime_Type()
)
rcCfmMepDbExEntryHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmMepDbExEntryHoldTime.setStatus("current")
_RcCfmMaCciEnableTable_Object = MibTable
rcCfmMaCciEnableTable = _RcCfmMaCciEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 7)
)
if mibBuilder.loadTexts:
    rcCfmMaCciEnableTable.setStatus("deprecated")
_RcCfmMaCciEnableEntry_Object = MibTableRow
rcCfmMaCciEnableEntry = _RcCfmMaCciEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 7, 1)
)
rcCfmMaCciEnableEntry.setIndexNames(
    (0, "RAISECOM-CFM-MIB", "rcCfmMaMdLevel"),
    (0, "RAISECOM-CFM-MIB", "rcCfmMaMaVlanId"),
)
if mibBuilder.loadTexts:
    rcCfmMaCciEnableEntry.setStatus("deprecated")
_RcCfmMaMdLevel_Type = Dot1agCfmMDLevel
_RcCfmMaMdLevel_Object = MibTableColumn
rcCfmMaMdLevel = _RcCfmMaMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 7, 1, 1),
    _RcCfmMaMdLevel_Type()
)
rcCfmMaMdLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcCfmMaMdLevel.setStatus("deprecated")
_RcCfmMaMaVlanId_Type = VlanIdOrNone
_RcCfmMaMaVlanId_Object = MibTableColumn
rcCfmMaMaVlanId = _RcCfmMaMaVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 7, 1, 2),
    _RcCfmMaMaVlanId_Type()
)
rcCfmMaMaVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcCfmMaMaVlanId.setStatus("deprecated")
_RcCfmMaCciEnabled_Type = TruthValue
_RcCfmMaCciEnabled_Object = MibTableColumn
rcCfmMaCciEnabled = _RcCfmMaCciEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 7, 1, 3),
    _RcCfmMaCciEnabled_Type()
)
rcCfmMaCciEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmMaCciEnabled.setStatus("deprecated")
_RcCfmMepExTable_Object = MibTable
rcCfmMepExTable = _RcCfmMepExTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 8)
)
if mibBuilder.loadTexts:
    rcCfmMepExTable.setStatus("current")
_RcCfmMepExEntry_Object = MibTableRow
rcCfmMepExEntry = _RcCfmMepExEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 8, 1)
)
rcCfmMepExEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
)
if mibBuilder.loadTexts:
    rcCfmMepExEntry.setStatus("current")


class _RcCfmMepExLbrTimeoutNum_Type(Unsigned32):
    """Custom type rcCfmMepExLbrTimeoutNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RcCfmMepExLbrTimeoutNum_Type.__name__ = "Unsigned32"
_RcCfmMepExLbrTimeoutNum_Object = MibTableColumn
rcCfmMepExLbrTimeoutNum = _RcCfmMepExLbrTimeoutNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 8, 1, 1),
    _RcCfmMepExLbrTimeoutNum_Type()
)
rcCfmMepExLbrTimeoutNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmMepExLbrTimeoutNum.setStatus("current")


class _RcCfmMepExTransmitLbmDataTlvLen_Type(Unsigned32):
    """Custom type rcCfmMepExTransmitLbmDataTlvLen based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1484),
    )


_RcCfmMepExTransmitLbmDataTlvLen_Type.__name__ = "Unsigned32"
_RcCfmMepExTransmitLbmDataTlvLen_Object = MibTableColumn
rcCfmMepExTransmitLbmDataTlvLen = _RcCfmMepExTransmitLbmDataTlvLen_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 8, 1, 2),
    _RcCfmMepExTransmitLbmDataTlvLen_Type()
)
rcCfmMepExTransmitLbmDataTlvLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmMepExTransmitLbmDataTlvLen.setStatus("current")


class _RcCfmMepExLckAdmin_Type(EnableVar):
    """Custom type rcCfmMepExLckAdmin based on EnableVar"""
    defaultValue = 2


_RcCfmMepExLckAdmin_Type.__name__ = "EnableVar"
_RcCfmMepExLckAdmin_Object = MibTableColumn
rcCfmMepExLckAdmin = _RcCfmMepExLckAdmin_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 8, 1, 3),
    _RcCfmMepExLckAdmin_Type()
)
rcCfmMepExLckAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmMepExLckAdmin.setStatus("current")


class _RcCfmMaExAisSuppressStatus_Type(Integer32):
    """Custom type rcCfmMaExAisSuppressStatus based on Integer32"""
    defaultValue = 3


_RcCfmMaExAisSuppressStatus_Type.__name__ = "Integer32"
_RcCfmMaExAisSuppressStatus_Object = MibTableColumn
rcCfmMaExAisSuppressStatus = _RcCfmMaExAisSuppressStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 8, 1, 4),
    _RcCfmMaExAisSuppressStatus_Type()
)
rcCfmMaExAisSuppressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmMaExAisSuppressStatus.setStatus("current")


class _RcCfmMaExAisSuppressAdmin_Type(EnableVar):
    """Custom type rcCfmMaExAisSuppressAdmin based on EnableVar"""
    defaultValue = 1


_RcCfmMaExAisSuppressAdmin_Type.__name__ = "EnableVar"
_RcCfmMaExAisSuppressAdmin_Object = MibTableColumn
rcCfmMaExAisSuppressAdmin = _RcCfmMaExAisSuppressAdmin_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 8, 1, 5),
    _RcCfmMaExAisSuppressAdmin_Type()
)
rcCfmMaExAisSuppressAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmMaExAisSuppressAdmin.setStatus("current")


class _RcCfmMepExPduPriority_Type(Integer32):
    """Custom type rcCfmMepExPduPriority based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcCfmMepExPduPriority_Type.__name__ = "Integer32"
_RcCfmMepExPduPriority_Object = MibTableColumn
rcCfmMepExPduPriority = _RcCfmMepExPduPriority_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 8, 1, 6),
    _RcCfmMepExPduPriority_Type()
)
rcCfmMepExPduPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmMepExPduPriority.setStatus("current")


class _RcCfmMepExPmAdmin_Type(EnableVar):
    """Custom type rcCfmMepExPmAdmin based on EnableVar"""
    defaultValue = 2


_RcCfmMepExPmAdmin_Type.__name__ = "EnableVar"
_RcCfmMepExPmAdmin_Object = MibTableColumn
rcCfmMepExPmAdmin = _RcCfmMepExPmAdmin_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 8, 1, 7),
    _RcCfmMepExPmAdmin_Type()
)
rcCfmMepExPmAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmMepExPmAdmin.setStatus("current")


class _RcCfmMepExRdiAdmin_Type(EnableVar):
    """Custom type rcCfmMepExRdiAdmin based on EnableVar"""
    defaultValue = 2


_RcCfmMepExRdiAdmin_Type.__name__ = "EnableVar"
_RcCfmMepExRdiAdmin_Object = MibTableColumn
rcCfmMepExRdiAdmin = _RcCfmMepExRdiAdmin_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 8, 1, 8),
    _RcCfmMepExRdiAdmin_Type()
)
rcCfmMepExRdiAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmMepExRdiAdmin.setStatus("current")
_RcCfmMaMepListExTable_Object = MibTable
rcCfmMaMepListExTable = _RcCfmMaMepListExTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 9)
)
if mibBuilder.loadTexts:
    rcCfmMaMepListExTable.setStatus("current")
_RcCfmMaMepListExEntry_Object = MibTableRow
rcCfmMaMepListExEntry = _RcCfmMaMepListExEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 9, 1)
)
rcCfmMaMepListExEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
)
if mibBuilder.loadTexts:
    rcCfmMaMepListExEntry.setStatus("current")


class _RcCfmMaMepListType_Type(Integer32):
    """Custom type rcCfmMaMepListType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("static-remote", 2),
          ("dynamic-remote", 3))
    )


_RcCfmMaMepListType_Type.__name__ = "Integer32"
_RcCfmMaMepListType_Object = MibTableColumn
rcCfmMaMepListType = _RcCfmMaMepListType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 9, 1, 1),
    _RcCfmMaMepListType_Type()
)
rcCfmMaMepListType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmMaMepListType.setStatus("deprecated")
_RcCfmMaMepListMacAddress_Type = MacAddress
_RcCfmMaMepListMacAddress_Object = MibTableColumn
rcCfmMaMepListMacAddress = _RcCfmMaMepListMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 9, 1, 2),
    _RcCfmMaMepListMacAddress_Type()
)
rcCfmMaMepListMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmMaMepListMacAddress.setStatus("current")
_RcCfmMaMepListIfIndex_Type = InterfaceIndex
_RcCfmMaMepListIfIndex_Object = MibTableColumn
rcCfmMaMepListIfIndex = _RcCfmMaMepListIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 9, 1, 3),
    _RcCfmMaMepListIfIndex_Type()
)
rcCfmMaMepListIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmMaMepListIfIndex.setStatus("current")
_RcCfmMaNetExTable_Object = MibTable
rcCfmMaNetExTable = _RcCfmMaNetExTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 10)
)
if mibBuilder.loadTexts:
    rcCfmMaNetExTable.setStatus("current")
_RcCfmMaNetExEntry_Object = MibTableRow
rcCfmMaNetExEntry = _RcCfmMaNetExEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 10, 1)
)
rcCfmMaNetExEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
)
if mibBuilder.loadTexts:
    rcCfmMaNetExEntry.setStatus("current")
_RcCfmMaNetRemoteMepLearnEnabled_Type = TruthValue
_RcCfmMaNetRemoteMepLearnEnabled_Object = MibTableColumn
rcCfmMaNetRemoteMepLearnEnabled = _RcCfmMaNetRemoteMepLearnEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 10, 1, 1),
    _RcCfmMaNetRemoteMepLearnEnabled_Type()
)
rcCfmMaNetRemoteMepLearnEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmMaNetRemoteMepLearnEnabled.setStatus("deprecated")


class _RcCfmMaNetCostumerVlan_Type(VlanIdOrNone):
    """Custom type rcCfmMaNetCostumerVlan based on VlanIdOrNone"""
    defaultValue = 0


_RcCfmMaNetCostumerVlan_Type.__name__ = "VlanIdOrNone"
_RcCfmMaNetCostumerVlan_Object = MibTableColumn
rcCfmMaNetCostumerVlan = _RcCfmMaNetCostumerVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 10, 1, 2),
    _RcCfmMaNetCostumerVlan_Type()
)
rcCfmMaNetCostumerVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmMaNetCostumerVlan.setStatus("current")


class _RcCfmMaNetPduPriority_Type(Unsigned32):
    """Custom type rcCfmMaNetPduPriority based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcCfmMaNetPduPriority_Type.__name__ = "Unsigned32"
_RcCfmMaNetPduPriority_Object = MibTableColumn
rcCfmMaNetPduPriority = _RcCfmMaNetPduPriority_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 10, 1, 3),
    _RcCfmMaNetPduPriority_Type()
)
rcCfmMaNetPduPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmMaNetPduPriority.setStatus("current")


class _RcCfmMaNetRemoteMepLearnActive_Type(TruthValue):
    """Custom type rcCfmMaNetRemoteMepLearnActive based on TruthValue"""
    defaultValue = 2


_RcCfmMaNetRemoteMepLearnActive_Type.__name__ = "TruthValue"
_RcCfmMaNetRemoteMepLearnActive_Object = MibTableColumn
rcCfmMaNetRemoteMepLearnActive = _RcCfmMaNetRemoteMepLearnActive_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 10, 1, 4),
    _RcCfmMaNetRemoteMepLearnActive_Type()
)
rcCfmMaNetRemoteMepLearnActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmMaNetRemoteMepLearnActive.setStatus("current")


class _RcCfmMaNetCcCheckEnabled_Type(TruthValue):
    """Custom type rcCfmMaNetCcCheckEnabled based on TruthValue"""
    defaultValue = 2


_RcCfmMaNetCcCheckEnabled_Type.__name__ = "TruthValue"
_RcCfmMaNetCcCheckEnabled_Object = MibTableColumn
rcCfmMaNetCcCheckEnabled = _RcCfmMaNetCcCheckEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 10, 1, 5),
    _RcCfmMaNetCcCheckEnabled_Type()
)
rcCfmMaNetCcCheckEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmMaNetCcCheckEnabled.setStatus("current")
_RcCfmPMTable_Object = MibTable
rcCfmPMTable = _RcCfmPMTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 11)
)
if mibBuilder.loadTexts:
    rcCfmPMTable.setStatus("deprecated")
_RcCfmPMEntry_Object = MibTableRow
rcCfmPMEntry = _RcCfmPMEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 11, 1)
)
rcCfmPMEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepDbRMepIdentifier"),
)
if mibBuilder.loadTexts:
    rcCfmPMEntry.setStatus("deprecated")
_RcCfmPMEnabled_Type = TruthValue
_RcCfmPMEnabled_Object = MibTableColumn
rcCfmPMEnabled = _RcCfmPMEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 11, 1, 1),
    _RcCfmPMEnabled_Type()
)
rcCfmPMEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmPMEnabled.setStatus("deprecated")


class _RcCfmPMDmmTxInterval_Type(Integer32):
    """Custom type rcCfmPMDmmTxInterval based on Integer32"""
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
        *(("intervalInvalid", 0),
          ("interval300Hz", 1),
          ("interval10ms", 2),
          ("interval100ms", 3),
          ("interval1s", 4),
          ("interval10s", 5),
          ("interval1min", 6),
          ("interval10min", 7))
    )


_RcCfmPMDmmTxInterval_Type.__name__ = "Integer32"
_RcCfmPMDmmTxInterval_Object = MibTableColumn
rcCfmPMDmmTxInterval = _RcCfmPMDmmTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 11, 1, 2),
    _RcCfmPMDmmTxInterval_Type()
)
rcCfmPMDmmTxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDmmTxInterval.setStatus("deprecated")


class _RcCfmPMDelayObjective_Type(Unsigned32):
    """Custom type rcCfmPMDelayObjective based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_RcCfmPMDelayObjective_Type.__name__ = "Unsigned32"
_RcCfmPMDelayObjective_Object = MibTableColumn
rcCfmPMDelayObjective = _RcCfmPMDelayObjective_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 11, 1, 3),
    _RcCfmPMDelayObjective_Type()
)
rcCfmPMDelayObjective.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmPMDelayObjective.setStatus("deprecated")


class _RcCfmPMDVObjective_Type(Unsigned32):
    """Custom type rcCfmPMDVObjective based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_RcCfmPMDVObjective_Type.__name__ = "Unsigned32"
_RcCfmPMDVObjective_Object = MibTableColumn
rcCfmPMDVObjective = _RcCfmPMDVObjective_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 11, 1, 4),
    _RcCfmPMDVObjective_Type()
)
rcCfmPMDVObjective.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmPMDVObjective.setStatus("deprecated")


class _RcCfmPMFLRRisingThreshold_Type(Integer32):
    """Custom type rcCfmPMFLRRisingThreshold based on Integer32"""
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
        *(("threshold0", 0),
          ("threshold1PerSouthend", 1),
          ("threshold2PerSouthend", 2),
          ("threshold5PerSouthend", 3),
          ("threshold1PerHundrud", 4),
          ("threshold2PerHundrud", 5),
          ("threshold5PerHundrud", 6),
          ("threshold1", 7))
    )


_RcCfmPMFLRRisingThreshold_Type.__name__ = "Integer32"
_RcCfmPMFLRRisingThreshold_Object = MibTableColumn
rcCfmPMFLRRisingThreshold = _RcCfmPMFLRRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 11, 1, 5),
    _RcCfmPMFLRRisingThreshold_Type()
)
rcCfmPMFLRRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmPMFLRRisingThreshold.setStatus("deprecated")


class _RcCfmPMFLRFallingThreshold_Type(Integer32):
    """Custom type rcCfmPMFLRFallingThreshold based on Integer32"""
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
        *(("threshold0", 0),
          ("threshold1PerSouthend", 1),
          ("threshold2PerSouthend", 2),
          ("threshold5PerSouthend", 3),
          ("threshold1PerHundrud", 4),
          ("threshold2PerHundrud", 5),
          ("threshold5PerHundrud", 6),
          ("threshold1", 7))
    )


_RcCfmPMFLRFallingThreshold_Type.__name__ = "Integer32"
_RcCfmPMFLRFallingThreshold_Object = MibTableColumn
rcCfmPMFLRFallingThreshold = _RcCfmPMFLRFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 11, 1, 6),
    _RcCfmPMFLRFallingThreshold_Type()
)
rcCfmPMFLRFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmPMFLRFallingThreshold.setStatus("deprecated")


class _RcCfmPMDelayRisingThreshold_Type(Integer32):
    """Custom type rcCfmPMDelayRisingThreshold based on Integer32"""
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
        *(("threshold0", 0),
          ("threshold1PerSouthend", 1),
          ("threshold2PerSouthend", 2),
          ("threshold5PerSouthend", 3),
          ("threshold1PerHundrud", 4),
          ("threshold2PerHundrud", 5),
          ("threshold5PerHundrud", 6),
          ("threshold1", 7))
    )


_RcCfmPMDelayRisingThreshold_Type.__name__ = "Integer32"
_RcCfmPMDelayRisingThreshold_Object = MibTableColumn
rcCfmPMDelayRisingThreshold = _RcCfmPMDelayRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 11, 1, 7),
    _RcCfmPMDelayRisingThreshold_Type()
)
rcCfmPMDelayRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmPMDelayRisingThreshold.setStatus("deprecated")


class _RcCfmPMDelayFallingThreshold_Type(Integer32):
    """Custom type rcCfmPMDelayFallingThreshold based on Integer32"""
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
        *(("threshold0", 0),
          ("threshold1PerSouthend", 1),
          ("threshold2PerSouthend", 2),
          ("threshold5PerSouthend", 3),
          ("threshold1PerHundrud", 4),
          ("threshold2PerHundrud", 5),
          ("threshold5PerHundrud", 6),
          ("threshold1", 7))
    )


_RcCfmPMDelayFallingThreshold_Type.__name__ = "Integer32"
_RcCfmPMDelayFallingThreshold_Object = MibTableColumn
rcCfmPMDelayFallingThreshold = _RcCfmPMDelayFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 11, 1, 8),
    _RcCfmPMDelayFallingThreshold_Type()
)
rcCfmPMDelayFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmPMDelayFallingThreshold.setStatus("deprecated")


class _RcCfmPMDVRisingThreshold_Type(Integer32):
    """Custom type rcCfmPMDVRisingThreshold based on Integer32"""
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
        *(("threshold0", 0),
          ("threshold1PerSouthend", 1),
          ("threshold2PerSouthend", 2),
          ("threshold5PerSouthend", 3),
          ("threshold1PerHundrud", 4),
          ("threshold2PerHundrud", 5),
          ("threshold5PerHundrud", 6),
          ("threshold1", 7))
    )


_RcCfmPMDVRisingThreshold_Type.__name__ = "Integer32"
_RcCfmPMDVRisingThreshold_Object = MibTableColumn
rcCfmPMDVRisingThreshold = _RcCfmPMDVRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 11, 1, 9),
    _RcCfmPMDVRisingThreshold_Type()
)
rcCfmPMDVRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmPMDVRisingThreshold.setStatus("deprecated")


class _RcCfmPMDVFallingThreshold_Type(Integer32):
    """Custom type rcCfmPMDVFallingThreshold based on Integer32"""
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
        *(("threshold0", 0),
          ("threshold1PerSouthend", 1),
          ("threshold2PerSouthend", 2),
          ("threshold5PerSouthend", 3),
          ("threshold1PerHundrud", 4),
          ("threshold2PerHundrud", 5),
          ("threshold5PerHundrud", 6),
          ("threshold1", 7))
    )


_RcCfmPMDVFallingThreshold_Type.__name__ = "Integer32"
_RcCfmPMDVFallingThreshold_Object = MibTableColumn
rcCfmPMDVFallingThreshold = _RcCfmPMDVFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 11, 1, 10),
    _RcCfmPMDVFallingThreshold_Type()
)
rcCfmPMDVFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmPMDVFallingThreshold.setStatus("deprecated")


class _RcCfmPMStatiticsClear_Type(Integer32):
    """Custom type rcCfmPMStatiticsClear based on Integer32"""
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
        *(("all", 0),
          ("frame-loss-ratio", 1),
          ("delay", 2),
          ("delay-variation", 3))
    )


_RcCfmPMStatiticsClear_Type.__name__ = "Integer32"
_RcCfmPMStatiticsClear_Object = MibTableColumn
rcCfmPMStatiticsClear = _RcCfmPMStatiticsClear_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 11, 1, 11),
    _RcCfmPMStatiticsClear_Type()
)
rcCfmPMStatiticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmPMStatiticsClear.setStatus("deprecated")
_RcCfmPMTrapSendEnable_Type = TruthValue
_RcCfmPMTrapSendEnable_Object = MibTableColumn
rcCfmPMTrapSendEnable = _RcCfmPMTrapSendEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 11, 1, 12),
    _RcCfmPMTrapSendEnable_Type()
)
rcCfmPMTrapSendEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmPMTrapSendEnable.setStatus("deprecated")


class _RcCfmPMThroughputTimeout_Type(Unsigned32):
    """Custom type rcCfmPMThroughputTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 30),
    )


_RcCfmPMThroughputTimeout_Type.__name__ = "Unsigned32"
_RcCfmPMThroughputTimeout_Object = MibTableColumn
rcCfmPMThroughputTimeout = _RcCfmPMThroughputTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 11, 1, 13),
    _RcCfmPMThroughputTimeout_Type()
)
rcCfmPMThroughputTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmPMThroughputTimeout.setStatus("deprecated")


class _RcCfmPMThroughputObject_Type(Unsigned32):
    """Custom type rcCfmPMThroughputObject based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(125, 1000000),
    )


_RcCfmPMThroughputObject_Type.__name__ = "Unsigned32"
_RcCfmPMThroughputObject_Object = MibTableColumn
rcCfmPMThroughputObject = _RcCfmPMThroughputObject_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 11, 1, 14),
    _RcCfmPMThroughputObject_Type()
)
rcCfmPMThroughputObject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmPMThroughputObject.setStatus("deprecated")


class _RcCfmPMThroughputPduLength_Type(Integer32):
    """Custom type rcCfmPMThroughputPduLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("length64", 0),
          ("length128", 1),
          ("length256", 2),
          ("length512", 3),
          ("length1024", 4),
          ("length1280", 5),
          ("length1518", 6))
    )


_RcCfmPMThroughputPduLength_Type.__name__ = "Integer32"
_RcCfmPMThroughputPduLength_Object = MibTableColumn
rcCfmPMThroughputPduLength = _RcCfmPMThroughputPduLength_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 11, 1, 15),
    _RcCfmPMThroughputPduLength_Type()
)
rcCfmPMThroughputPduLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmPMThroughputPduLength.setStatus("deprecated")
_RcCfmPMThroughputEnable_Type = TruthValue
_RcCfmPMThroughputEnable_Object = MibTableColumn
rcCfmPMThroughputEnable = _RcCfmPMThroughputEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 11, 1, 16),
    _RcCfmPMThroughputEnable_Type()
)
rcCfmPMThroughputEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmPMThroughputEnable.setStatus("deprecated")
_RcCfmPMRowStatus_Type = RowStatus
_RcCfmPMRowStatus_Object = MibTableColumn
rcCfmPMRowStatus = _RcCfmPMRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 11, 1, 17),
    _RcCfmPMRowStatus_Type()
)
rcCfmPMRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmPMRowStatus.setStatus("deprecated")
_RcCfmPMFLRTotalTable_Object = MibTable
rcCfmPMFLRTotalTable = _RcCfmPMFLRTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 12)
)
if mibBuilder.loadTexts:
    rcCfmPMFLRTotalTable.setStatus("deprecated")
_RcCfmPMFLRTotalEntry_Object = MibTableRow
rcCfmPMFLRTotalEntry = _RcCfmPMFLRTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 12, 1)
)
rcCfmPMFLRTotalEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
)
if mibBuilder.loadTexts:
    rcCfmPMFLRTotalEntry.setStatus("deprecated")
_RcCfmPMFLRTotalElapsedTime_Type = Unsigned32
_RcCfmPMFLRTotalElapsedTime_Object = MibTableColumn
rcCfmPMFLRTotalElapsedTime = _RcCfmPMFLRTotalElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 12, 1, 1),
    _RcCfmPMFLRTotalElapsedTime_Type()
)
rcCfmPMFLRTotalElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMFLRTotalElapsedTime.setStatus("deprecated")
_RcCfmPMFLRTotalFarEndTxCounter_Type = Unsigned32
_RcCfmPMFLRTotalFarEndTxCounter_Object = MibTableColumn
rcCfmPMFLRTotalFarEndTxCounter = _RcCfmPMFLRTotalFarEndTxCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 12, 1, 2),
    _RcCfmPMFLRTotalFarEndTxCounter_Type()
)
rcCfmPMFLRTotalFarEndTxCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMFLRTotalFarEndTxCounter.setStatus("deprecated")
_RcCfmPMFLRTotalFarEndLostCounter_Type = Unsigned32
_RcCfmPMFLRTotalFarEndLostCounter_Object = MibTableColumn
rcCfmPMFLRTotalFarEndLostCounter = _RcCfmPMFLRTotalFarEndLostCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 12, 1, 3),
    _RcCfmPMFLRTotalFarEndLostCounter_Type()
)
rcCfmPMFLRTotalFarEndLostCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMFLRTotalFarEndLostCounter.setStatus("deprecated")


class _RcCfmPMFLRTotalFarEndLossRatio_Type(Unsigned32):
    """Custom type rcCfmPMFLRTotalFarEndLossRatio based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_RcCfmPMFLRTotalFarEndLossRatio_Type.__name__ = "Unsigned32"
_RcCfmPMFLRTotalFarEndLossRatio_Object = MibTableColumn
rcCfmPMFLRTotalFarEndLossRatio = _RcCfmPMFLRTotalFarEndLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 12, 1, 4),
    _RcCfmPMFLRTotalFarEndLossRatio_Type()
)
rcCfmPMFLRTotalFarEndLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMFLRTotalFarEndLossRatio.setStatus("deprecated")
_RcCfmPMFLRTotalFarEndUnaviableSecond_Type = Unsigned32
_RcCfmPMFLRTotalFarEndUnaviableSecond_Object = MibTableColumn
rcCfmPMFLRTotalFarEndUnaviableSecond = _RcCfmPMFLRTotalFarEndUnaviableSecond_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 12, 1, 5),
    _RcCfmPMFLRTotalFarEndUnaviableSecond_Type()
)
rcCfmPMFLRTotalFarEndUnaviableSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMFLRTotalFarEndUnaviableSecond.setStatus("deprecated")
_RcCfmPMFLRTotalNearEndTxCounter_Type = Unsigned32
_RcCfmPMFLRTotalNearEndTxCounter_Object = MibTableColumn
rcCfmPMFLRTotalNearEndTxCounter = _RcCfmPMFLRTotalNearEndTxCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 12, 1, 6),
    _RcCfmPMFLRTotalNearEndTxCounter_Type()
)
rcCfmPMFLRTotalNearEndTxCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMFLRTotalNearEndTxCounter.setStatus("deprecated")
_RcCfmPMFLRTotalNearEndLostCounter_Type = Unsigned32
_RcCfmPMFLRTotalNearEndLostCounter_Object = MibTableColumn
rcCfmPMFLRTotalNearEndLostCounter = _RcCfmPMFLRTotalNearEndLostCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 12, 1, 7),
    _RcCfmPMFLRTotalNearEndLostCounter_Type()
)
rcCfmPMFLRTotalNearEndLostCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMFLRTotalNearEndLostCounter.setStatus("deprecated")


class _RcCfmPMFLRTotalNearEndLossRatio_Type(Unsigned32):
    """Custom type rcCfmPMFLRTotalNearEndLossRatio based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_RcCfmPMFLRTotalNearEndLossRatio_Type.__name__ = "Unsigned32"
_RcCfmPMFLRTotalNearEndLossRatio_Object = MibTableColumn
rcCfmPMFLRTotalNearEndLossRatio = _RcCfmPMFLRTotalNearEndLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 12, 1, 8),
    _RcCfmPMFLRTotalNearEndLossRatio_Type()
)
rcCfmPMFLRTotalNearEndLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMFLRTotalNearEndLossRatio.setStatus("deprecated")
_RcCfmPMFLRTotalNearEndUnaviableSecond_Type = Unsigned32
_RcCfmPMFLRTotalNearEndUnaviableSecond_Object = MibTableColumn
rcCfmPMFLRTotalNearEndUnaviableSecond = _RcCfmPMFLRTotalNearEndUnaviableSecond_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 12, 1, 9),
    _RcCfmPMFLRTotalNearEndUnaviableSecond_Type()
)
rcCfmPMFLRTotalNearEndUnaviableSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMFLRTotalNearEndUnaviableSecond.setStatus("deprecated")
_RcCfmPMFLRCurrentTable_Object = MibTable
rcCfmPMFLRCurrentTable = _RcCfmPMFLRCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 13)
)
if mibBuilder.loadTexts:
    rcCfmPMFLRCurrentTable.setStatus("deprecated")
_RcCfmPMFLRCurrentEntry_Object = MibTableRow
rcCfmPMFLRCurrentEntry = _RcCfmPMFLRCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 13, 1)
)
rcCfmPMFLRCurrentEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "RAISECOM-CFM-MIB", "rcCfmPMFLRCurrentPeriod"),
)
if mibBuilder.loadTexts:
    rcCfmPMFLRCurrentEntry.setStatus("deprecated")


class _RcCfmPMFLRCurrentPeriod_Type(Integer32):
    """Custom type rcCfmPMFLRCurrentPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rcCfmPMFLRCurrentPeriod15Minutes", 1),
          ("rcCfmPMFLRCurrentPeriod24Hours", 2))
    )


_RcCfmPMFLRCurrentPeriod_Type.__name__ = "Integer32"
_RcCfmPMFLRCurrentPeriod_Object = MibTableColumn
rcCfmPMFLRCurrentPeriod = _RcCfmPMFLRCurrentPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 13, 1, 1),
    _RcCfmPMFLRCurrentPeriod_Type()
)
rcCfmPMFLRCurrentPeriod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcCfmPMFLRCurrentPeriod.setStatus("deprecated")
_RcCfmPMFLRCurrentElapsedTime_Type = Unsigned32
_RcCfmPMFLRCurrentElapsedTime_Object = MibTableColumn
rcCfmPMFLRCurrentElapsedTime = _RcCfmPMFLRCurrentElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 13, 1, 2),
    _RcCfmPMFLRCurrentElapsedTime_Type()
)
rcCfmPMFLRCurrentElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMFLRCurrentElapsedTime.setStatus("deprecated")
_RcCfmPMFLRCurrentFarEndTxFrameCounter_Type = Unsigned32
_RcCfmPMFLRCurrentFarEndTxFrameCounter_Object = MibTableColumn
rcCfmPMFLRCurrentFarEndTxFrameCounter = _RcCfmPMFLRCurrentFarEndTxFrameCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 13, 1, 3),
    _RcCfmPMFLRCurrentFarEndTxFrameCounter_Type()
)
rcCfmPMFLRCurrentFarEndTxFrameCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMFLRCurrentFarEndTxFrameCounter.setStatus("deprecated")
_RcCfmPMFLRCurrentFarEndLostFrameCounter_Type = Unsigned32
_RcCfmPMFLRCurrentFarEndLostFrameCounter_Object = MibTableColumn
rcCfmPMFLRCurrentFarEndLostFrameCounter = _RcCfmPMFLRCurrentFarEndLostFrameCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 13, 1, 4),
    _RcCfmPMFLRCurrentFarEndLostFrameCounter_Type()
)
rcCfmPMFLRCurrentFarEndLostFrameCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMFLRCurrentFarEndLostFrameCounter.setStatus("deprecated")


class _RcCfmPMFLRCurrentFarEndLossRatio_Type(Unsigned32):
    """Custom type rcCfmPMFLRCurrentFarEndLossRatio based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_RcCfmPMFLRCurrentFarEndLossRatio_Type.__name__ = "Unsigned32"
_RcCfmPMFLRCurrentFarEndLossRatio_Object = MibTableColumn
rcCfmPMFLRCurrentFarEndLossRatio = _RcCfmPMFLRCurrentFarEndLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 13, 1, 5),
    _RcCfmPMFLRCurrentFarEndLossRatio_Type()
)
rcCfmPMFLRCurrentFarEndLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMFLRCurrentFarEndLossRatio.setStatus("deprecated")
_RcCfmPMFLRCurrentNearEndTxFrameCounter_Type = Unsigned32
_RcCfmPMFLRCurrentNearEndTxFrameCounter_Object = MibTableColumn
rcCfmPMFLRCurrentNearEndTxFrameCounter = _RcCfmPMFLRCurrentNearEndTxFrameCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 13, 1, 6),
    _RcCfmPMFLRCurrentNearEndTxFrameCounter_Type()
)
rcCfmPMFLRCurrentNearEndTxFrameCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMFLRCurrentNearEndTxFrameCounter.setStatus("deprecated")
_RcCfmPMFLRCurrentNearEndLostFrameCounter_Type = Unsigned32
_RcCfmPMFLRCurrentNearEndLostFrameCounter_Object = MibTableColumn
rcCfmPMFLRCurrentNearEndLostFrameCounter = _RcCfmPMFLRCurrentNearEndLostFrameCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 13, 1, 7),
    _RcCfmPMFLRCurrentNearEndLostFrameCounter_Type()
)
rcCfmPMFLRCurrentNearEndLostFrameCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMFLRCurrentNearEndLostFrameCounter.setStatus("deprecated")


class _RcCfmPMFLRCurrentNearEndLossRatio_Type(Unsigned32):
    """Custom type rcCfmPMFLRCurrentNearEndLossRatio based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_RcCfmPMFLRCurrentNearEndLossRatio_Type.__name__ = "Unsigned32"
_RcCfmPMFLRCurrentNearEndLossRatio_Object = MibTableColumn
rcCfmPMFLRCurrentNearEndLossRatio = _RcCfmPMFLRCurrentNearEndLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 13, 1, 8),
    _RcCfmPMFLRCurrentNearEndLossRatio_Type()
)
rcCfmPMFLRCurrentNearEndLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMFLRCurrentNearEndLossRatio.setStatus("deprecated")
_RcCfmPMFLRIntervalTable_Object = MibTable
rcCfmPMFLRIntervalTable = _RcCfmPMFLRIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 14)
)
if mibBuilder.loadTexts:
    rcCfmPMFLRIntervalTable.setStatus("deprecated")
_RcCfmPMFLRIntervalEntry_Object = MibTableRow
rcCfmPMFLRIntervalEntry = _RcCfmPMFLRIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 14, 1)
)
rcCfmPMFLRIntervalEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "RAISECOM-CFM-MIB", "rcCfmPMFLRIntervalPeriod"),
    (0, "RAISECOM-CFM-MIB", "rcCfmPMFLRIntervalIndex"),
)
if mibBuilder.loadTexts:
    rcCfmPMFLRIntervalEntry.setStatus("deprecated")


class _RcCfmPMFLRIntervalPeriod_Type(Integer32):
    """Custom type rcCfmPMFLRIntervalPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rcCfmPMFLRIntervalPeriod15Minutes", 1),
          ("rcCfmPMFLRIntervalPeriod24Hours", 2))
    )


_RcCfmPMFLRIntervalPeriod_Type.__name__ = "Integer32"
_RcCfmPMFLRIntervalPeriod_Object = MibTableColumn
rcCfmPMFLRIntervalPeriod = _RcCfmPMFLRIntervalPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 14, 1, 1),
    _RcCfmPMFLRIntervalPeriod_Type()
)
rcCfmPMFLRIntervalPeriod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcCfmPMFLRIntervalPeriod.setStatus("deprecated")
_RcCfmPMFLRIntervalIndex_Type = Unsigned32
_RcCfmPMFLRIntervalIndex_Object = MibTableColumn
rcCfmPMFLRIntervalIndex = _RcCfmPMFLRIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 14, 1, 2),
    _RcCfmPMFLRIntervalIndex_Type()
)
rcCfmPMFLRIntervalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcCfmPMFLRIntervalIndex.setStatus("deprecated")
_RcCfmPMFLRIntervalPeerMepId_Type = Dot1agCfmMepId
_RcCfmPMFLRIntervalPeerMepId_Object = MibTableColumn
rcCfmPMFLRIntervalPeerMepId = _RcCfmPMFLRIntervalPeerMepId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 14, 1, 3),
    _RcCfmPMFLRIntervalPeerMepId_Type()
)
rcCfmPMFLRIntervalPeerMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMFLRIntervalPeerMepId.setStatus("deprecated")
_RcCfmPMFLRIntervalBeginTime_Type = Unsigned32
_RcCfmPMFLRIntervalBeginTime_Object = MibTableColumn
rcCfmPMFLRIntervalBeginTime = _RcCfmPMFLRIntervalBeginTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 14, 1, 4),
    _RcCfmPMFLRIntervalBeginTime_Type()
)
rcCfmPMFLRIntervalBeginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMFLRIntervalBeginTime.setStatus("deprecated")
_RcCfmPMFLRIntervalFarEndTxFrameCounter_Type = Unsigned32
_RcCfmPMFLRIntervalFarEndTxFrameCounter_Object = MibTableColumn
rcCfmPMFLRIntervalFarEndTxFrameCounter = _RcCfmPMFLRIntervalFarEndTxFrameCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 14, 1, 5),
    _RcCfmPMFLRIntervalFarEndTxFrameCounter_Type()
)
rcCfmPMFLRIntervalFarEndTxFrameCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMFLRIntervalFarEndTxFrameCounter.setStatus("deprecated")
_RcCfmPMFLRIntervalFarEndLostFrameCounter_Type = Unsigned32
_RcCfmPMFLRIntervalFarEndLostFrameCounter_Object = MibTableColumn
rcCfmPMFLRIntervalFarEndLostFrameCounter = _RcCfmPMFLRIntervalFarEndLostFrameCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 14, 1, 6),
    _RcCfmPMFLRIntervalFarEndLostFrameCounter_Type()
)
rcCfmPMFLRIntervalFarEndLostFrameCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMFLRIntervalFarEndLostFrameCounter.setStatus("deprecated")


class _RcCfmPMFLRIntervalFarEndLossRatio_Type(Unsigned32):
    """Custom type rcCfmPMFLRIntervalFarEndLossRatio based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_RcCfmPMFLRIntervalFarEndLossRatio_Type.__name__ = "Unsigned32"
_RcCfmPMFLRIntervalFarEndLossRatio_Object = MibTableColumn
rcCfmPMFLRIntervalFarEndLossRatio = _RcCfmPMFLRIntervalFarEndLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 14, 1, 7),
    _RcCfmPMFLRIntervalFarEndLossRatio_Type()
)
rcCfmPMFLRIntervalFarEndLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMFLRIntervalFarEndLossRatio.setStatus("deprecated")
_RcCfmPMFLRIntervalNearEndTxFrameCounter_Type = Unsigned32
_RcCfmPMFLRIntervalNearEndTxFrameCounter_Object = MibTableColumn
rcCfmPMFLRIntervalNearEndTxFrameCounter = _RcCfmPMFLRIntervalNearEndTxFrameCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 14, 1, 8),
    _RcCfmPMFLRIntervalNearEndTxFrameCounter_Type()
)
rcCfmPMFLRIntervalNearEndTxFrameCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMFLRIntervalNearEndTxFrameCounter.setStatus("deprecated")
_RcCfmPMFLRIntervalNearEndLostFrameCounter_Type = Unsigned32
_RcCfmPMFLRIntervalNearEndLostFrameCounter_Object = MibTableColumn
rcCfmPMFLRIntervalNearEndLostFrameCounter = _RcCfmPMFLRIntervalNearEndLostFrameCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 14, 1, 9),
    _RcCfmPMFLRIntervalNearEndLostFrameCounter_Type()
)
rcCfmPMFLRIntervalNearEndLostFrameCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMFLRIntervalNearEndLostFrameCounter.setStatus("deprecated")


class _RcCfmPMFLRIntervalNearEndLossRatio_Type(Unsigned32):
    """Custom type rcCfmPMFLRIntervalNearEndLossRatio based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_RcCfmPMFLRIntervalNearEndLossRatio_Type.__name__ = "Unsigned32"
_RcCfmPMFLRIntervalNearEndLossRatio_Object = MibTableColumn
rcCfmPMFLRIntervalNearEndLossRatio = _RcCfmPMFLRIntervalNearEndLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 14, 1, 10),
    _RcCfmPMFLRIntervalNearEndLossRatio_Type()
)
rcCfmPMFLRIntervalNearEndLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMFLRIntervalNearEndLossRatio.setStatus("deprecated")
_RcCfmPMDelayCurrentTable_Object = MibTable
rcCfmPMDelayCurrentTable = _RcCfmPMDelayCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 15)
)
if mibBuilder.loadTexts:
    rcCfmPMDelayCurrentTable.setStatus("deprecated")
_RcCfmPMDelayCurrentEntry_Object = MibTableRow
rcCfmPMDelayCurrentEntry = _RcCfmPMDelayCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 15, 1)
)
rcCfmPMDelayCurrentEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "RAISECOM-CFM-MIB", "rcCfmPMDelayCurrentPeriod"),
)
if mibBuilder.loadTexts:
    rcCfmPMDelayCurrentEntry.setStatus("deprecated")


class _RcCfmPMDelayCurrentPeriod_Type(Integer32):
    """Custom type rcCfmPMDelayCurrentPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rcCfmPMDelayCurrentPeriod15Minutes", 1),
          ("rcCfmPMDelayCurrentPeriod24Hours", 2))
    )


_RcCfmPMDelayCurrentPeriod_Type.__name__ = "Integer32"
_RcCfmPMDelayCurrentPeriod_Object = MibTableColumn
rcCfmPMDelayCurrentPeriod = _RcCfmPMDelayCurrentPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 15, 1, 1),
    _RcCfmPMDelayCurrentPeriod_Type()
)
rcCfmPMDelayCurrentPeriod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcCfmPMDelayCurrentPeriod.setStatus("deprecated")
_RcCfmPMDelayCurrentFarEndAboveObjCounter_Type = Unsigned32
_RcCfmPMDelayCurrentFarEndAboveObjCounter_Object = MibTableColumn
rcCfmPMDelayCurrentFarEndAboveObjCounter = _RcCfmPMDelayCurrentFarEndAboveObjCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 15, 1, 2),
    _RcCfmPMDelayCurrentFarEndAboveObjCounter_Type()
)
rcCfmPMDelayCurrentFarEndAboveObjCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDelayCurrentFarEndAboveObjCounter.setStatus("deprecated")
_RcCfmPMDelayCurrentFarEndBelowObjCounter_Type = Unsigned32
_RcCfmPMDelayCurrentFarEndBelowObjCounter_Object = MibTableColumn
rcCfmPMDelayCurrentFarEndBelowObjCounter = _RcCfmPMDelayCurrentFarEndBelowObjCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 15, 1, 3),
    _RcCfmPMDelayCurrentFarEndBelowObjCounter_Type()
)
rcCfmPMDelayCurrentFarEndBelowObjCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDelayCurrentFarEndBelowObjCounter.setStatus("deprecated")
_RcCfmPMDelayCurrentFarEndMaxDelay_Type = Unsigned32
_RcCfmPMDelayCurrentFarEndMaxDelay_Object = MibTableColumn
rcCfmPMDelayCurrentFarEndMaxDelay = _RcCfmPMDelayCurrentFarEndMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 15, 1, 4),
    _RcCfmPMDelayCurrentFarEndMaxDelay_Type()
)
rcCfmPMDelayCurrentFarEndMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDelayCurrentFarEndMaxDelay.setStatus("deprecated")
_RcCfmPMDelayCurrentFarEndAvgDelay_Type = Unsigned32
_RcCfmPMDelayCurrentFarEndAvgDelay_Object = MibTableColumn
rcCfmPMDelayCurrentFarEndAvgDelay = _RcCfmPMDelayCurrentFarEndAvgDelay_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 15, 1, 5),
    _RcCfmPMDelayCurrentFarEndAvgDelay_Type()
)
rcCfmPMDelayCurrentFarEndAvgDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDelayCurrentFarEndAvgDelay.setStatus("deprecated")
_RcCfmPMDelayCurrentFarEndMinDelay_Type = Unsigned32
_RcCfmPMDelayCurrentFarEndMinDelay_Object = MibTableColumn
rcCfmPMDelayCurrentFarEndMinDelay = _RcCfmPMDelayCurrentFarEndMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 15, 1, 6),
    _RcCfmPMDelayCurrentFarEndMinDelay_Type()
)
rcCfmPMDelayCurrentFarEndMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDelayCurrentFarEndMinDelay.setStatus("deprecated")
_RcCfmPMDelayCurrentNearEndAboveObjCounter_Type = Unsigned32
_RcCfmPMDelayCurrentNearEndAboveObjCounter_Object = MibTableColumn
rcCfmPMDelayCurrentNearEndAboveObjCounter = _RcCfmPMDelayCurrentNearEndAboveObjCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 15, 1, 7),
    _RcCfmPMDelayCurrentNearEndAboveObjCounter_Type()
)
rcCfmPMDelayCurrentNearEndAboveObjCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDelayCurrentNearEndAboveObjCounter.setStatus("deprecated")
_RcCfmPMDelayCurrentNearEndBelowObjCounter_Type = Unsigned32
_RcCfmPMDelayCurrentNearEndBelowObjCounter_Object = MibTableColumn
rcCfmPMDelayCurrentNearEndBelowObjCounter = _RcCfmPMDelayCurrentNearEndBelowObjCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 15, 1, 8),
    _RcCfmPMDelayCurrentNearEndBelowObjCounter_Type()
)
rcCfmPMDelayCurrentNearEndBelowObjCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDelayCurrentNearEndBelowObjCounter.setStatus("deprecated")
_RcCfmPMDelayCurrentNearEndMaxDelay_Type = Unsigned32
_RcCfmPMDelayCurrentNearEndMaxDelay_Object = MibTableColumn
rcCfmPMDelayCurrentNearEndMaxDelay = _RcCfmPMDelayCurrentNearEndMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 15, 1, 9),
    _RcCfmPMDelayCurrentNearEndMaxDelay_Type()
)
rcCfmPMDelayCurrentNearEndMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDelayCurrentNearEndMaxDelay.setStatus("deprecated")
_RcCfmPMDelayCurrentNearEndAvgDelay_Type = Unsigned32
_RcCfmPMDelayCurrentNearEndAvgDelay_Object = MibTableColumn
rcCfmPMDelayCurrentNearEndAvgDelay = _RcCfmPMDelayCurrentNearEndAvgDelay_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 15, 1, 10),
    _RcCfmPMDelayCurrentNearEndAvgDelay_Type()
)
rcCfmPMDelayCurrentNearEndAvgDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDelayCurrentNearEndAvgDelay.setStatus("deprecated")
_RcCfmPMDelayCurrentNearEndMinDelay_Type = Unsigned32
_RcCfmPMDelayCurrentNearEndMinDelay_Object = MibTableColumn
rcCfmPMDelayCurrentNearEndMinDelay = _RcCfmPMDelayCurrentNearEndMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 15, 1, 11),
    _RcCfmPMDelayCurrentNearEndMinDelay_Type()
)
rcCfmPMDelayCurrentNearEndMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDelayCurrentNearEndMinDelay.setStatus("deprecated")
_RcCfmPMDelayCurrentRoundTripAboveObjCounter_Type = Unsigned32
_RcCfmPMDelayCurrentRoundTripAboveObjCounter_Object = MibTableColumn
rcCfmPMDelayCurrentRoundTripAboveObjCounter = _RcCfmPMDelayCurrentRoundTripAboveObjCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 15, 1, 12),
    _RcCfmPMDelayCurrentRoundTripAboveObjCounter_Type()
)
rcCfmPMDelayCurrentRoundTripAboveObjCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDelayCurrentRoundTripAboveObjCounter.setStatus("deprecated")
_RcCfmPMDelayCurrentRoundTripBelowObjCounter_Type = Unsigned32
_RcCfmPMDelayCurrentRoundTripBelowObjCounter_Object = MibTableColumn
rcCfmPMDelayCurrentRoundTripBelowObjCounter = _RcCfmPMDelayCurrentRoundTripBelowObjCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 15, 1, 13),
    _RcCfmPMDelayCurrentRoundTripBelowObjCounter_Type()
)
rcCfmPMDelayCurrentRoundTripBelowObjCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDelayCurrentRoundTripBelowObjCounter.setStatus("deprecated")
_RcCfmPMDelayCurrentRoundTripMaxDelay_Type = Unsigned32
_RcCfmPMDelayCurrentRoundTripMaxDelay_Object = MibTableColumn
rcCfmPMDelayCurrentRoundTripMaxDelay = _RcCfmPMDelayCurrentRoundTripMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 15, 1, 14),
    _RcCfmPMDelayCurrentRoundTripMaxDelay_Type()
)
rcCfmPMDelayCurrentRoundTripMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDelayCurrentRoundTripMaxDelay.setStatus("deprecated")
_RcCfmPMDelayCurrentRoundTripAvgDelay_Type = Unsigned32
_RcCfmPMDelayCurrentRoundTripAvgDelay_Object = MibTableColumn
rcCfmPMDelayCurrentRoundTripAvgDelay = _RcCfmPMDelayCurrentRoundTripAvgDelay_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 15, 1, 15),
    _RcCfmPMDelayCurrentRoundTripAvgDelay_Type()
)
rcCfmPMDelayCurrentRoundTripAvgDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDelayCurrentRoundTripAvgDelay.setStatus("deprecated")
_RcCfmPMDelayCurrentRoundTripMinDelay_Type = Unsigned32
_RcCfmPMDelayCurrentRoundTripMinDelay_Object = MibTableColumn
rcCfmPMDelayCurrentRoundTripMinDelay = _RcCfmPMDelayCurrentRoundTripMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 15, 1, 16),
    _RcCfmPMDelayCurrentRoundTripMinDelay_Type()
)
rcCfmPMDelayCurrentRoundTripMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDelayCurrentRoundTripMinDelay.setStatus("deprecated")
_RcCfmPMDelayIntervalTable_Object = MibTable
rcCfmPMDelayIntervalTable = _RcCfmPMDelayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 16)
)
if mibBuilder.loadTexts:
    rcCfmPMDelayIntervalTable.setStatus("deprecated")
_RcCfmPMDelayIntervalEntry_Object = MibTableRow
rcCfmPMDelayIntervalEntry = _RcCfmPMDelayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 16, 1)
)
rcCfmPMDelayIntervalEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "RAISECOM-CFM-MIB", "rcCfmPMDelayIntervalPeriod"),
    (0, "RAISECOM-CFM-MIB", "rcCfmPMDelayIntervalIndex"),
)
if mibBuilder.loadTexts:
    rcCfmPMDelayIntervalEntry.setStatus("deprecated")


class _RcCfmPMDelayIntervalPeriod_Type(Integer32):
    """Custom type rcCfmPMDelayIntervalPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rcCfmPMDelayIntervalPeriod15Minutes", 1),
          ("rcCfmPMDelayIntervalPeriod24Hours", 2))
    )


_RcCfmPMDelayIntervalPeriod_Type.__name__ = "Integer32"
_RcCfmPMDelayIntervalPeriod_Object = MibTableColumn
rcCfmPMDelayIntervalPeriod = _RcCfmPMDelayIntervalPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 16, 1, 1),
    _RcCfmPMDelayIntervalPeriod_Type()
)
rcCfmPMDelayIntervalPeriod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcCfmPMDelayIntervalPeriod.setStatus("deprecated")
_RcCfmPMDelayIntervalIndex_Type = Unsigned32
_RcCfmPMDelayIntervalIndex_Object = MibTableColumn
rcCfmPMDelayIntervalIndex = _RcCfmPMDelayIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 16, 1, 2),
    _RcCfmPMDelayIntervalIndex_Type()
)
rcCfmPMDelayIntervalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcCfmPMDelayIntervalIndex.setStatus("deprecated")
_RcCfmPMDelayIntervalBeginTime_Type = Unsigned32
_RcCfmPMDelayIntervalBeginTime_Object = MibTableColumn
rcCfmPMDelayIntervalBeginTime = _RcCfmPMDelayIntervalBeginTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 16, 1, 3),
    _RcCfmPMDelayIntervalBeginTime_Type()
)
rcCfmPMDelayIntervalBeginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDelayIntervalBeginTime.setStatus("deprecated")
_RcCfmPMDelayIntervalPeerMepId_Type = Dot1agCfmMepId
_RcCfmPMDelayIntervalPeerMepId_Object = MibTableColumn
rcCfmPMDelayIntervalPeerMepId = _RcCfmPMDelayIntervalPeerMepId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 16, 1, 4),
    _RcCfmPMDelayIntervalPeerMepId_Type()
)
rcCfmPMDelayIntervalPeerMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDelayIntervalPeerMepId.setStatus("deprecated")
_RcCfmPMDelayIntervalFarEndAboveObjCounter_Type = Unsigned32
_RcCfmPMDelayIntervalFarEndAboveObjCounter_Object = MibTableColumn
rcCfmPMDelayIntervalFarEndAboveObjCounter = _RcCfmPMDelayIntervalFarEndAboveObjCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 16, 1, 5),
    _RcCfmPMDelayIntervalFarEndAboveObjCounter_Type()
)
rcCfmPMDelayIntervalFarEndAboveObjCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDelayIntervalFarEndAboveObjCounter.setStatus("deprecated")
_RcCfmPMDelayIntervalFarEndBelowObjCounter_Type = Unsigned32
_RcCfmPMDelayIntervalFarEndBelowObjCounter_Object = MibTableColumn
rcCfmPMDelayIntervalFarEndBelowObjCounter = _RcCfmPMDelayIntervalFarEndBelowObjCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 16, 1, 6),
    _RcCfmPMDelayIntervalFarEndBelowObjCounter_Type()
)
rcCfmPMDelayIntervalFarEndBelowObjCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDelayIntervalFarEndBelowObjCounter.setStatus("deprecated")
_RcCfmPMDelayIntervalFarEndMaxDelay_Type = Unsigned32
_RcCfmPMDelayIntervalFarEndMaxDelay_Object = MibTableColumn
rcCfmPMDelayIntervalFarEndMaxDelay = _RcCfmPMDelayIntervalFarEndMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 16, 1, 7),
    _RcCfmPMDelayIntervalFarEndMaxDelay_Type()
)
rcCfmPMDelayIntervalFarEndMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDelayIntervalFarEndMaxDelay.setStatus("deprecated")
_RcCfmPMDelayIntervalFarEndAvgDelay_Type = Unsigned32
_RcCfmPMDelayIntervalFarEndAvgDelay_Object = MibTableColumn
rcCfmPMDelayIntervalFarEndAvgDelay = _RcCfmPMDelayIntervalFarEndAvgDelay_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 16, 1, 8),
    _RcCfmPMDelayIntervalFarEndAvgDelay_Type()
)
rcCfmPMDelayIntervalFarEndAvgDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDelayIntervalFarEndAvgDelay.setStatus("deprecated")
_RcCfmPMDelayIntervalFarEndMinDelay_Type = Unsigned32
_RcCfmPMDelayIntervalFarEndMinDelay_Object = MibTableColumn
rcCfmPMDelayIntervalFarEndMinDelay = _RcCfmPMDelayIntervalFarEndMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 16, 1, 9),
    _RcCfmPMDelayIntervalFarEndMinDelay_Type()
)
rcCfmPMDelayIntervalFarEndMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDelayIntervalFarEndMinDelay.setStatus("deprecated")
_RcCfmPMDelayIntervalNearEndAboveObjCounter_Type = Unsigned32
_RcCfmPMDelayIntervalNearEndAboveObjCounter_Object = MibTableColumn
rcCfmPMDelayIntervalNearEndAboveObjCounter = _RcCfmPMDelayIntervalNearEndAboveObjCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 16, 1, 10),
    _RcCfmPMDelayIntervalNearEndAboveObjCounter_Type()
)
rcCfmPMDelayIntervalNearEndAboveObjCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDelayIntervalNearEndAboveObjCounter.setStatus("deprecated")
_RcCfmPMDelayIntervalNearEndBelowObjCounter_Type = Unsigned32
_RcCfmPMDelayIntervalNearEndBelowObjCounter_Object = MibTableColumn
rcCfmPMDelayIntervalNearEndBelowObjCounter = _RcCfmPMDelayIntervalNearEndBelowObjCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 16, 1, 11),
    _RcCfmPMDelayIntervalNearEndBelowObjCounter_Type()
)
rcCfmPMDelayIntervalNearEndBelowObjCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDelayIntervalNearEndBelowObjCounter.setStatus("deprecated")
_RcCfmPMDelayIntervalNearEndMaxDelay_Type = Unsigned32
_RcCfmPMDelayIntervalNearEndMaxDelay_Object = MibTableColumn
rcCfmPMDelayIntervalNearEndMaxDelay = _RcCfmPMDelayIntervalNearEndMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 16, 1, 12),
    _RcCfmPMDelayIntervalNearEndMaxDelay_Type()
)
rcCfmPMDelayIntervalNearEndMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDelayIntervalNearEndMaxDelay.setStatus("current")
_RcCfmPMDelayIntervalNearEndAvgDelay_Type = Unsigned32
_RcCfmPMDelayIntervalNearEndAvgDelay_Object = MibTableColumn
rcCfmPMDelayIntervalNearEndAvgDelay = _RcCfmPMDelayIntervalNearEndAvgDelay_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 16, 1, 13),
    _RcCfmPMDelayIntervalNearEndAvgDelay_Type()
)
rcCfmPMDelayIntervalNearEndAvgDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDelayIntervalNearEndAvgDelay.setStatus("deprecated")
_RcCfmPMDelayIntervalNearEndMinDelay_Type = Unsigned32
_RcCfmPMDelayIntervalNearEndMinDelay_Object = MibTableColumn
rcCfmPMDelayIntervalNearEndMinDelay = _RcCfmPMDelayIntervalNearEndMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 16, 1, 14),
    _RcCfmPMDelayIntervalNearEndMinDelay_Type()
)
rcCfmPMDelayIntervalNearEndMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDelayIntervalNearEndMinDelay.setStatus("deprecated")
_RcCfmPMDelayIntervalRoundTripAboveObjCounter_Type = Unsigned32
_RcCfmPMDelayIntervalRoundTripAboveObjCounter_Object = MibTableColumn
rcCfmPMDelayIntervalRoundTripAboveObjCounter = _RcCfmPMDelayIntervalRoundTripAboveObjCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 16, 1, 15),
    _RcCfmPMDelayIntervalRoundTripAboveObjCounter_Type()
)
rcCfmPMDelayIntervalRoundTripAboveObjCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDelayIntervalRoundTripAboveObjCounter.setStatus("deprecated")
_RcCfmPMDelayIntervalRoundTripBelowObjCounter_Type = Unsigned32
_RcCfmPMDelayIntervalRoundTripBelowObjCounter_Object = MibTableColumn
rcCfmPMDelayIntervalRoundTripBelowObjCounter = _RcCfmPMDelayIntervalRoundTripBelowObjCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 16, 1, 16),
    _RcCfmPMDelayIntervalRoundTripBelowObjCounter_Type()
)
rcCfmPMDelayIntervalRoundTripBelowObjCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDelayIntervalRoundTripBelowObjCounter.setStatus("deprecated")
_RcCfmPMDelayIntervalRoundTripMaxDelay_Type = Unsigned32
_RcCfmPMDelayIntervalRoundTripMaxDelay_Object = MibTableColumn
rcCfmPMDelayIntervalRoundTripMaxDelay = _RcCfmPMDelayIntervalRoundTripMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 16, 1, 17),
    _RcCfmPMDelayIntervalRoundTripMaxDelay_Type()
)
rcCfmPMDelayIntervalRoundTripMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDelayIntervalRoundTripMaxDelay.setStatus("deprecated")
_RcCfmPMDelayIntervalRoundTripAvgDelay_Type = Unsigned32
_RcCfmPMDelayIntervalRoundTripAvgDelay_Object = MibTableColumn
rcCfmPMDelayIntervalRoundTripAvgDelay = _RcCfmPMDelayIntervalRoundTripAvgDelay_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 16, 1, 18),
    _RcCfmPMDelayIntervalRoundTripAvgDelay_Type()
)
rcCfmPMDelayIntervalRoundTripAvgDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDelayIntervalRoundTripAvgDelay.setStatus("deprecated")
_RcCfmPMDelayIntervalRoundTripMinDelay_Type = Unsigned32
_RcCfmPMDelayIntervalRoundTripMinDelay_Object = MibTableColumn
rcCfmPMDelayIntervalRoundTripMinDelay = _RcCfmPMDelayIntervalRoundTripMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 16, 1, 19),
    _RcCfmPMDelayIntervalRoundTripMinDelay_Type()
)
rcCfmPMDelayIntervalRoundTripMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDelayIntervalRoundTripMinDelay.setStatus("deprecated")
_RcCfmPMDVCurrentTable_Object = MibTable
rcCfmPMDVCurrentTable = _RcCfmPMDVCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 17)
)
if mibBuilder.loadTexts:
    rcCfmPMDVCurrentTable.setStatus("deprecated")
_RcCfmPMDVCurrentEntry_Object = MibTableRow
rcCfmPMDVCurrentEntry = _RcCfmPMDVCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 17, 1)
)
rcCfmPMDVCurrentEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "RAISECOM-CFM-MIB", "rcCfmPMDVCurrentPeriod"),
)
if mibBuilder.loadTexts:
    rcCfmPMDVCurrentEntry.setStatus("deprecated")


class _RcCfmPMDVCurrentPeriod_Type(Integer32):
    """Custom type rcCfmPMDVCurrentPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rcCfmPMDVCurrentPeriod15Minutes", 1),
          ("rcCfmPMDVCurrentPeriod24Hours", 2))
    )


_RcCfmPMDVCurrentPeriod_Type.__name__ = "Integer32"
_RcCfmPMDVCurrentPeriod_Object = MibTableColumn
rcCfmPMDVCurrentPeriod = _RcCfmPMDVCurrentPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 17, 1, 1),
    _RcCfmPMDVCurrentPeriod_Type()
)
rcCfmPMDVCurrentPeriod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcCfmPMDVCurrentPeriod.setStatus("deprecated")
_RcCfmPMDVCurrentFarEndAboveObjCounter_Type = Unsigned32
_RcCfmPMDVCurrentFarEndAboveObjCounter_Object = MibTableColumn
rcCfmPMDVCurrentFarEndAboveObjCounter = _RcCfmPMDVCurrentFarEndAboveObjCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 17, 1, 2),
    _RcCfmPMDVCurrentFarEndAboveObjCounter_Type()
)
rcCfmPMDVCurrentFarEndAboveObjCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDVCurrentFarEndAboveObjCounter.setStatus("deprecated")
_RcCfmPMDVCurrentFarEndBelowObjCounter_Type = Unsigned32
_RcCfmPMDVCurrentFarEndBelowObjCounter_Object = MibTableColumn
rcCfmPMDVCurrentFarEndBelowObjCounter = _RcCfmPMDVCurrentFarEndBelowObjCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 17, 1, 3),
    _RcCfmPMDVCurrentFarEndBelowObjCounter_Type()
)
rcCfmPMDVCurrentFarEndBelowObjCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDVCurrentFarEndBelowObjCounter.setStatus("deprecated")
_RcCfmPMDVCurrentFarEndMaxDv_Type = Unsigned32
_RcCfmPMDVCurrentFarEndMaxDv_Object = MibTableColumn
rcCfmPMDVCurrentFarEndMaxDv = _RcCfmPMDVCurrentFarEndMaxDv_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 17, 1, 4),
    _RcCfmPMDVCurrentFarEndMaxDv_Type()
)
rcCfmPMDVCurrentFarEndMaxDv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDVCurrentFarEndMaxDv.setStatus("deprecated")
_RcCfmPMDVCurrentFarEndAvgDv_Type = Unsigned32
_RcCfmPMDVCurrentFarEndAvgDv_Object = MibTableColumn
rcCfmPMDVCurrentFarEndAvgDv = _RcCfmPMDVCurrentFarEndAvgDv_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 17, 1, 5),
    _RcCfmPMDVCurrentFarEndAvgDv_Type()
)
rcCfmPMDVCurrentFarEndAvgDv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDVCurrentFarEndAvgDv.setStatus("deprecated")
_RcCfmPMDVCurrentNearEndAboveObjCounter_Type = Unsigned32
_RcCfmPMDVCurrentNearEndAboveObjCounter_Object = MibTableColumn
rcCfmPMDVCurrentNearEndAboveObjCounter = _RcCfmPMDVCurrentNearEndAboveObjCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 17, 1, 6),
    _RcCfmPMDVCurrentNearEndAboveObjCounter_Type()
)
rcCfmPMDVCurrentNearEndAboveObjCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDVCurrentNearEndAboveObjCounter.setStatus("deprecated")
_RcCfmPMDVCurrentNearEndBelowObjCounter_Type = Unsigned32
_RcCfmPMDVCurrentNearEndBelowObjCounter_Object = MibTableColumn
rcCfmPMDVCurrentNearEndBelowObjCounter = _RcCfmPMDVCurrentNearEndBelowObjCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 17, 1, 7),
    _RcCfmPMDVCurrentNearEndBelowObjCounter_Type()
)
rcCfmPMDVCurrentNearEndBelowObjCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDVCurrentNearEndBelowObjCounter.setStatus("deprecated")
_RcCfmPMDVCurrentNearEndMaxDv_Type = Unsigned32
_RcCfmPMDVCurrentNearEndMaxDv_Object = MibTableColumn
rcCfmPMDVCurrentNearEndMaxDv = _RcCfmPMDVCurrentNearEndMaxDv_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 17, 1, 8),
    _RcCfmPMDVCurrentNearEndMaxDv_Type()
)
rcCfmPMDVCurrentNearEndMaxDv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDVCurrentNearEndMaxDv.setStatus("deprecated")
_RcCfmPMDVCurrentNearEndAvgDv_Type = Unsigned32
_RcCfmPMDVCurrentNearEndAvgDv_Object = MibTableColumn
rcCfmPMDVCurrentNearEndAvgDv = _RcCfmPMDVCurrentNearEndAvgDv_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 17, 1, 9),
    _RcCfmPMDVCurrentNearEndAvgDv_Type()
)
rcCfmPMDVCurrentNearEndAvgDv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDVCurrentNearEndAvgDv.setStatus("deprecated")
_RcCfmPMDVCurrentRoundTripAboveObjCounter_Type = Unsigned32
_RcCfmPMDVCurrentRoundTripAboveObjCounter_Object = MibTableColumn
rcCfmPMDVCurrentRoundTripAboveObjCounter = _RcCfmPMDVCurrentRoundTripAboveObjCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 17, 1, 10),
    _RcCfmPMDVCurrentRoundTripAboveObjCounter_Type()
)
rcCfmPMDVCurrentRoundTripAboveObjCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDVCurrentRoundTripAboveObjCounter.setStatus("deprecated")
_RcCfmPMDVCurrentRoundTripBelowObjCounter_Type = Unsigned32
_RcCfmPMDVCurrentRoundTripBelowObjCounter_Object = MibTableColumn
rcCfmPMDVCurrentRoundTripBelowObjCounter = _RcCfmPMDVCurrentRoundTripBelowObjCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 17, 1, 11),
    _RcCfmPMDVCurrentRoundTripBelowObjCounter_Type()
)
rcCfmPMDVCurrentRoundTripBelowObjCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDVCurrentRoundTripBelowObjCounter.setStatus("deprecated")
_RcCfmPMDVCurrentRoundTripMaxDv_Type = Unsigned32
_RcCfmPMDVCurrentRoundTripMaxDv_Object = MibTableColumn
rcCfmPMDVCurrentRoundTripMaxDv = _RcCfmPMDVCurrentRoundTripMaxDv_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 17, 1, 12),
    _RcCfmPMDVCurrentRoundTripMaxDv_Type()
)
rcCfmPMDVCurrentRoundTripMaxDv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDVCurrentRoundTripMaxDv.setStatus("deprecated")
_RcCfmPMDVCurrentRoundTripAvgDv_Type = Unsigned32
_RcCfmPMDVCurrentRoundTripAvgDv_Object = MibTableColumn
rcCfmPMDVCurrentRoundTripAvgDv = _RcCfmPMDVCurrentRoundTripAvgDv_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 17, 1, 13),
    _RcCfmPMDVCurrentRoundTripAvgDv_Type()
)
rcCfmPMDVCurrentRoundTripAvgDv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDVCurrentRoundTripAvgDv.setStatus("deprecated")
_RcCfmPMDVIntervalTable_Object = MibTable
rcCfmPMDVIntervalTable = _RcCfmPMDVIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 18)
)
if mibBuilder.loadTexts:
    rcCfmPMDVIntervalTable.setStatus("deprecated")
_RcCfmPMDVIntervalEntry_Object = MibTableRow
rcCfmPMDVIntervalEntry = _RcCfmPMDVIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 18, 1)
)
rcCfmPMDVIntervalEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "RAISECOM-CFM-MIB", "rcCfmPMDVIntervalPeriod"),
    (0, "RAISECOM-CFM-MIB", "rcCfmPMDVIntervalIndex"),
)
if mibBuilder.loadTexts:
    rcCfmPMDVIntervalEntry.setStatus("deprecated")


class _RcCfmPMDVIntervalPeriod_Type(Integer32):
    """Custom type rcCfmPMDVIntervalPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rcCfmPMDVIntervalPeriod15Minutes", 1),
          ("rcCfmPMDVIntervalPeriod24Hours", 2))
    )


_RcCfmPMDVIntervalPeriod_Type.__name__ = "Integer32"
_RcCfmPMDVIntervalPeriod_Object = MibTableColumn
rcCfmPMDVIntervalPeriod = _RcCfmPMDVIntervalPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 18, 1, 1),
    _RcCfmPMDVIntervalPeriod_Type()
)
rcCfmPMDVIntervalPeriod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcCfmPMDVIntervalPeriod.setStatus("deprecated")
_RcCfmPMDVIntervalIndex_Type = Unsigned32
_RcCfmPMDVIntervalIndex_Object = MibTableColumn
rcCfmPMDVIntervalIndex = _RcCfmPMDVIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 18, 1, 2),
    _RcCfmPMDVIntervalIndex_Type()
)
rcCfmPMDVIntervalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcCfmPMDVIntervalIndex.setStatus("deprecated")
_RcCfmPMDVIntervalBeginTime_Type = Unsigned32
_RcCfmPMDVIntervalBeginTime_Object = MibTableColumn
rcCfmPMDVIntervalBeginTime = _RcCfmPMDVIntervalBeginTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 18, 1, 3),
    _RcCfmPMDVIntervalBeginTime_Type()
)
rcCfmPMDVIntervalBeginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDVIntervalBeginTime.setStatus("deprecated")
_RcCfmPMDVIntervalPeerMepId_Type = Dot1agCfmMepId
_RcCfmPMDVIntervalPeerMepId_Object = MibTableColumn
rcCfmPMDVIntervalPeerMepId = _RcCfmPMDVIntervalPeerMepId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 18, 1, 4),
    _RcCfmPMDVIntervalPeerMepId_Type()
)
rcCfmPMDVIntervalPeerMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDVIntervalPeerMepId.setStatus("deprecated")
_RcCfmPMDVIntervalFarEndAboveObjCounter_Type = Unsigned32
_RcCfmPMDVIntervalFarEndAboveObjCounter_Object = MibTableColumn
rcCfmPMDVIntervalFarEndAboveObjCounter = _RcCfmPMDVIntervalFarEndAboveObjCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 18, 1, 5),
    _RcCfmPMDVIntervalFarEndAboveObjCounter_Type()
)
rcCfmPMDVIntervalFarEndAboveObjCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDVIntervalFarEndAboveObjCounter.setStatus("deprecated")
_RcCfmPMDVIntervalFarEndBelowObjCounter_Type = Unsigned32
_RcCfmPMDVIntervalFarEndBelowObjCounter_Object = MibTableColumn
rcCfmPMDVIntervalFarEndBelowObjCounter = _RcCfmPMDVIntervalFarEndBelowObjCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 18, 1, 6),
    _RcCfmPMDVIntervalFarEndBelowObjCounter_Type()
)
rcCfmPMDVIntervalFarEndBelowObjCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDVIntervalFarEndBelowObjCounter.setStatus("deprecated")
_RcCfmPMDVIntervalFarEndMaxDv_Type = Unsigned32
_RcCfmPMDVIntervalFarEndMaxDv_Object = MibTableColumn
rcCfmPMDVIntervalFarEndMaxDv = _RcCfmPMDVIntervalFarEndMaxDv_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 18, 1, 7),
    _RcCfmPMDVIntervalFarEndMaxDv_Type()
)
rcCfmPMDVIntervalFarEndMaxDv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDVIntervalFarEndMaxDv.setStatus("deprecated")
_RcCfmPMDVIntervalFarEndAvgDv_Type = Unsigned32
_RcCfmPMDVIntervalFarEndAvgDv_Object = MibTableColumn
rcCfmPMDVIntervalFarEndAvgDv = _RcCfmPMDVIntervalFarEndAvgDv_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 18, 1, 8),
    _RcCfmPMDVIntervalFarEndAvgDv_Type()
)
rcCfmPMDVIntervalFarEndAvgDv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDVIntervalFarEndAvgDv.setStatus("deprecated")
_RcCfmPMDVIntervalNearEndAboveObjCounter_Type = Unsigned32
_RcCfmPMDVIntervalNearEndAboveObjCounter_Object = MibTableColumn
rcCfmPMDVIntervalNearEndAboveObjCounter = _RcCfmPMDVIntervalNearEndAboveObjCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 18, 1, 9),
    _RcCfmPMDVIntervalNearEndAboveObjCounter_Type()
)
rcCfmPMDVIntervalNearEndAboveObjCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDVIntervalNearEndAboveObjCounter.setStatus("deprecated")
_RcCfmPMDVIntervalNearEndBelowObjCounter_Type = Unsigned32
_RcCfmPMDVIntervalNearEndBelowObjCounter_Object = MibTableColumn
rcCfmPMDVIntervalNearEndBelowObjCounter = _RcCfmPMDVIntervalNearEndBelowObjCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 18, 1, 10),
    _RcCfmPMDVIntervalNearEndBelowObjCounter_Type()
)
rcCfmPMDVIntervalNearEndBelowObjCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDVIntervalNearEndBelowObjCounter.setStatus("deprecated")
_RcCfmPMDVIntervalNearEndMaxDv_Type = Unsigned32
_RcCfmPMDVIntervalNearEndMaxDv_Object = MibTableColumn
rcCfmPMDVIntervalNearEndMaxDv = _RcCfmPMDVIntervalNearEndMaxDv_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 18, 1, 11),
    _RcCfmPMDVIntervalNearEndMaxDv_Type()
)
rcCfmPMDVIntervalNearEndMaxDv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDVIntervalNearEndMaxDv.setStatus("deprecated")
_RcCfmPMDVIntervalNearEndAvgDv_Type = Unsigned32
_RcCfmPMDVIntervalNearEndAvgDv_Object = MibTableColumn
rcCfmPMDVIntervalNearEndAvgDv = _RcCfmPMDVIntervalNearEndAvgDv_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 18, 1, 12),
    _RcCfmPMDVIntervalNearEndAvgDv_Type()
)
rcCfmPMDVIntervalNearEndAvgDv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDVIntervalNearEndAvgDv.setStatus("deprecated")
_RcCfmPMDVIntervalRoundTripAboveObjCounter_Type = Unsigned32
_RcCfmPMDVIntervalRoundTripAboveObjCounter_Object = MibTableColumn
rcCfmPMDVIntervalRoundTripAboveObjCounter = _RcCfmPMDVIntervalRoundTripAboveObjCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 18, 1, 13),
    _RcCfmPMDVIntervalRoundTripAboveObjCounter_Type()
)
rcCfmPMDVIntervalRoundTripAboveObjCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDVIntervalRoundTripAboveObjCounter.setStatus("deprecated")
_RcCfmPMDVIntervalRoundTripBelowObjCounter_Type = Unsigned32
_RcCfmPMDVIntervalRoundTripBelowObjCounter_Object = MibTableColumn
rcCfmPMDVIntervalRoundTripBelowObjCounter = _RcCfmPMDVIntervalRoundTripBelowObjCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 18, 1, 14),
    _RcCfmPMDVIntervalRoundTripBelowObjCounter_Type()
)
rcCfmPMDVIntervalRoundTripBelowObjCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDVIntervalRoundTripBelowObjCounter.setStatus("deprecated")
_RcCfmPMDVIntervalRoundTripMaxDv_Type = Unsigned32
_RcCfmPMDVIntervalRoundTripMaxDv_Object = MibTableColumn
rcCfmPMDVIntervalRoundTripMaxDv = _RcCfmPMDVIntervalRoundTripMaxDv_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 18, 1, 15),
    _RcCfmPMDVIntervalRoundTripMaxDv_Type()
)
rcCfmPMDVIntervalRoundTripMaxDv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDVIntervalRoundTripMaxDv.setStatus("deprecated")
_RcCfmPMDVIntervalRoundTripAvgDv_Type = Unsigned32
_RcCfmPMDVIntervalRoundTripAvgDv_Object = MibTableColumn
rcCfmPMDVIntervalRoundTripAvgDv = _RcCfmPMDVIntervalRoundTripAvgDv_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 18, 1, 16),
    _RcCfmPMDVIntervalRoundTripAvgDv_Type()
)
rcCfmPMDVIntervalRoundTripAvgDv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMDVIntervalRoundTripAvgDv.setStatus("deprecated")
_RcCfmPMThroughputTable_Object = MibTable
rcCfmPMThroughputTable = _RcCfmPMThroughputTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 19)
)
if mibBuilder.loadTexts:
    rcCfmPMThroughputTable.setStatus("deprecated")
_RcCfmPMThroughputEntry_Object = MibTableRow
rcCfmPMThroughputEntry = _RcCfmPMThroughputEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 19, 1)
)
rcCfmPMThroughputEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepDbRMepIdentifier"),
)
if mibBuilder.loadTexts:
    rcCfmPMThroughputEntry.setStatus("deprecated")


class _RcCfmPMThroughputTestResult_Type(Integer32):
    """Custom type rcCfmPMThroughputTestResult based on Integer32"""
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
        *(("successed", 0),
          ("unknownReasonFailed", 1),
          ("localReourceConflict", 2),
          ("remoteResourceConflict", 3),
          ("vsxTimeOut", 4))
    )


_RcCfmPMThroughputTestResult_Type.__name__ = "Integer32"
_RcCfmPMThroughputTestResult_Object = MibTableColumn
rcCfmPMThroughputTestResult = _RcCfmPMThroughputTestResult_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 19, 1, 1),
    _RcCfmPMThroughputTestResult_Type()
)
rcCfmPMThroughputTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMThroughputTestResult.setStatus("deprecated")


class _RcCfmPMThroughputTestState_Type(Integer32):
    """Custom type rcCfmPMThroughputTestState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("farEndStart", 1),
          ("farEndSend", 2),
          ("farEndTest", 3),
          ("nearEndStart", 4),
          ("nearEndTest", 5),
          ("nearEndClose", 6))
    )


_RcCfmPMThroughputTestState_Type.__name__ = "Integer32"
_RcCfmPMThroughputTestState_Object = MibTableColumn
rcCfmPMThroughputTestState = _RcCfmPMThroughputTestState_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 19, 1, 2),
    _RcCfmPMThroughputTestState_Type()
)
rcCfmPMThroughputTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMThroughputTestState.setStatus("deprecated")
_RcCfmPMThroughputFarEndSendbps_Type = Counter64
_RcCfmPMThroughputFarEndSendbps_Object = MibTableColumn
rcCfmPMThroughputFarEndSendbps = _RcCfmPMThroughputFarEndSendbps_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 19, 1, 3),
    _RcCfmPMThroughputFarEndSendbps_Type()
)
rcCfmPMThroughputFarEndSendbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMThroughputFarEndSendbps.setStatus("deprecated")
_RcCfmPMThroughputFarEndRecievebps_Type = Counter64
_RcCfmPMThroughputFarEndRecievebps_Object = MibTableColumn
rcCfmPMThroughputFarEndRecievebps = _RcCfmPMThroughputFarEndRecievebps_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 19, 1, 4),
    _RcCfmPMThroughputFarEndRecievebps_Type()
)
rcCfmPMThroughputFarEndRecievebps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMThroughputFarEndRecievebps.setStatus("deprecated")
_RcCfmPMThroughputFarEndSendpps_Type = Counter64
_RcCfmPMThroughputFarEndSendpps_Object = MibTableColumn
rcCfmPMThroughputFarEndSendpps = _RcCfmPMThroughputFarEndSendpps_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 19, 1, 5),
    _RcCfmPMThroughputFarEndSendpps_Type()
)
rcCfmPMThroughputFarEndSendpps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMThroughputFarEndSendpps.setStatus("deprecated")
_RcCfmPMThroughputFarEndRecievepps_Type = Counter64
_RcCfmPMThroughputFarEndRecievepps_Object = MibTableColumn
rcCfmPMThroughputFarEndRecievepps = _RcCfmPMThroughputFarEndRecievepps_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 19, 1, 6),
    _RcCfmPMThroughputFarEndRecievepps_Type()
)
rcCfmPMThroughputFarEndRecievepps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMThroughputFarEndRecievepps.setStatus("deprecated")
_RcCfmPMThroughputNearEndSendbps_Type = Counter64
_RcCfmPMThroughputNearEndSendbps_Object = MibTableColumn
rcCfmPMThroughputNearEndSendbps = _RcCfmPMThroughputNearEndSendbps_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 19, 1, 7),
    _RcCfmPMThroughputNearEndSendbps_Type()
)
rcCfmPMThroughputNearEndSendbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMThroughputNearEndSendbps.setStatus("deprecated")
_RcCfmPMThroughputNearEndRecievebps_Type = Counter64
_RcCfmPMThroughputNearEndRecievebps_Object = MibTableColumn
rcCfmPMThroughputNearEndRecievebps = _RcCfmPMThroughputNearEndRecievebps_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 19, 1, 8),
    _RcCfmPMThroughputNearEndRecievebps_Type()
)
rcCfmPMThroughputNearEndRecievebps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMThroughputNearEndRecievebps.setStatus("deprecated")
_RcCfmPMThroughputNearEndSendpps_Type = Counter64
_RcCfmPMThroughputNearEndSendpps_Object = MibTableColumn
rcCfmPMThroughputNearEndSendpps = _RcCfmPMThroughputNearEndSendpps_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 19, 1, 9),
    _RcCfmPMThroughputNearEndSendpps_Type()
)
rcCfmPMThroughputNearEndSendpps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMThroughputNearEndSendpps.setStatus("deprecated")
_RcCfmPMThroughputNearEndRecievepps_Type = Counter64
_RcCfmPMThroughputNearEndRecievepps_Object = MibTableColumn
rcCfmPMThroughputNearEndRecievepps = _RcCfmPMThroughputNearEndRecievepps_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 19, 1, 10),
    _RcCfmPMThroughputNearEndRecievepps_Type()
)
rcCfmPMThroughputNearEndRecievepps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmPMThroughputNearEndRecievepps.setStatus("deprecated")
_RcCfmMaExTable_Object = MibTable
rcCfmMaExTable = _RcCfmMaExTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 20)
)
if mibBuilder.loadTexts:
    rcCfmMaExTable.setStatus("current")
_RcCfmMaExEntry_Object = MibTableRow
rcCfmMaExEntry = _RcCfmMaExEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 20, 1)
)
rcCfmMaExEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
)
if mibBuilder.loadTexts:
    rcCfmMaExEntry.setStatus("current")
_RcCfmMaExFormat_Type = Dot1agCfmMaintAssocNameType
_RcCfmMaExFormat_Object = MibTableColumn
rcCfmMaExFormat = _RcCfmMaExFormat_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 20, 1, 1),
    _RcCfmMaExFormat_Type()
)
rcCfmMaExFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcCfmMaExFormat.setStatus("current")
_RcCfmMaExName_Type = Dot1agCfmMaintAssocName
_RcCfmMaExName_Object = MibTableColumn
rcCfmMaExName = _RcCfmMaExName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 20, 1, 2),
    _RcCfmMaExName_Type()
)
rcCfmMaExName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcCfmMaExName.setStatus("current")


class _RcCfmMaExVlanList_Type(OctetString):
    """Custom type rcCfmMaExVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512


_RcCfmMaExVlanList_Type.__name__ = "OctetString"
_RcCfmMaExVlanList_Object = MibTableColumn
rcCfmMaExVlanList = _RcCfmMaExVlanList_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 20, 1, 3),
    _RcCfmMaExVlanList_Type()
)
rcCfmMaExVlanList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcCfmMaExVlanList.setStatus("current")


class _RcCfmMaExCcmInterval_Type(Dot1agCfmCcmInterval):
    """Custom type rcCfmMaExCcmInterval based on Dot1agCfmCcmInterval"""
    defaultValue = 4


_RcCfmMaExCcmInterval_Type.__name__ = "Dot1agCfmCcmInterval"
_RcCfmMaExCcmInterval_Object = MibTableColumn
rcCfmMaExCcmInterval = _RcCfmMaExCcmInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 20, 1, 4),
    _RcCfmMaExCcmInterval_Type()
)
rcCfmMaExCcmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcCfmMaExCcmInterval.setStatus("current")


class _RcCfmMaExCostumerVlan_Type(VlanIdOrNone):
    """Custom type rcCfmMaExCostumerVlan based on VlanIdOrNone"""
    defaultValue = 0


_RcCfmMaExCostumerVlan_Type.__name__ = "VlanIdOrNone"
_RcCfmMaExCostumerVlan_Object = MibTableColumn
rcCfmMaExCostumerVlan = _RcCfmMaExCostumerVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 20, 1, 5),
    _RcCfmMaExCostumerVlan_Type()
)
rcCfmMaExCostumerVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcCfmMaExCostumerVlan.setStatus("current")


class _RcCfmMaExPduPriority_Type(Unsigned32):
    """Custom type rcCfmMaExPduPriority based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcCfmMaExPduPriority_Type.__name__ = "Unsigned32"
_RcCfmMaExPduPriority_Object = MibTableColumn
rcCfmMaExPduPriority = _RcCfmMaExPduPriority_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 20, 1, 6),
    _RcCfmMaExPduPriority_Type()
)
rcCfmMaExPduPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcCfmMaExPduPriority.setStatus("current")
_RcCfmMaExRowStatus_Type = RowStatus
_RcCfmMaExRowStatus_Object = MibTableColumn
rcCfmMaExRowStatus = _RcCfmMaExRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 20, 1, 7),
    _RcCfmMaExRowStatus_Type()
)
rcCfmMaExRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcCfmMaExRowStatus.setStatus("current")
_RcCfmMaExPrimaryVlanId_Type = VlanIdOrNone
_RcCfmMaExPrimaryVlanId_Object = MibTableColumn
rcCfmMaExPrimaryVlanId = _RcCfmMaExPrimaryVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 20, 1, 8),
    _RcCfmMaExPrimaryVlanId_Type()
)
rcCfmMaExPrimaryVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcCfmMaExPrimaryVlanId.setStatus("current")


class _RcCfmMaExMipAutocreateAdmin_Type(EnableVar):
    """Custom type rcCfmMaExMipAutocreateAdmin based on EnableVar"""
    defaultValue = 2


_RcCfmMaExMipAutocreateAdmin_Type.__name__ = "EnableVar"
_RcCfmMaExMipAutocreateAdmin_Object = MibTableColumn
rcCfmMaExMipAutocreateAdmin = _RcCfmMaExMipAutocreateAdmin_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 20, 1, 9),
    _RcCfmMaExMipAutocreateAdmin_Type()
)
rcCfmMaExMipAutocreateAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCfmMaExMipAutocreateAdmin.setStatus("current")
_RcCfmMaExAisTable_Object = MibTable
rcCfmMaExAisTable = _RcCfmMaExAisTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 21)
)
if mibBuilder.loadTexts:
    rcCfmMaExAisTable.setStatus("current")
_RcCfmMaExAisEntry_Object = MibTableRow
rcCfmMaExAisEntry = _RcCfmMaExAisEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 21, 1)
)
rcCfmMaExAisEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
)
if mibBuilder.loadTexts:
    rcCfmMaExAisEntry.setStatus("current")


class _RcCfmMaExAisEnable_Type(EnableVar):
    """Custom type rcCfmMaExAisEnable based on EnableVar"""
    defaultValue = 2


_RcCfmMaExAisEnable_Type.__name__ = "EnableVar"
_RcCfmMaExAisEnable_Object = MibTableColumn
rcCfmMaExAisEnable = _RcCfmMaExAisEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 21, 1, 1),
    _RcCfmMaExAisEnable_Type()
)
rcCfmMaExAisEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcCfmMaExAisEnable.setStatus("current")


class _RcCfmMaExAisLevelAdmin_Type(Dot1agCfmMDLevelOrNone):
    """Custom type rcCfmMaExAisLevelAdmin based on Dot1agCfmMDLevelOrNone"""
    defaultValue = -1


_RcCfmMaExAisLevelAdmin_Type.__name__ = "Dot1agCfmMDLevelOrNone"
_RcCfmMaExAisLevelAdmin_Object = MibTableColumn
rcCfmMaExAisLevelAdmin = _RcCfmMaExAisLevelAdmin_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 21, 1, 2),
    _RcCfmMaExAisLevelAdmin_Type()
)
rcCfmMaExAisLevelAdmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcCfmMaExAisLevelAdmin.setStatus("current")
_RcCfmMaExAisLevelOper_Type = Dot1agCfmMDLevelOrNone
_RcCfmMaExAisLevelOper_Object = MibTableColumn
rcCfmMaExAisLevelOper = _RcCfmMaExAisLevelOper_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 21, 1, 3),
    _RcCfmMaExAisLevelOper_Type()
)
rcCfmMaExAisLevelOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmMaExAisLevelOper.setStatus("current")


class _RcCfmMaExAisPeriod_Type(Integer32):
    """Custom type rcCfmMaExAisPeriod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              60)
        )
    )
    namedValues = NamedValues(
        *(("aisPeriod1s", 1),
          ("aisPeriod60s", 60))
    )


_RcCfmMaExAisPeriod_Type.__name__ = "Integer32"
_RcCfmMaExAisPeriod_Object = MibTableColumn
rcCfmMaExAisPeriod = _RcCfmMaExAisPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 21, 1, 4),
    _RcCfmMaExAisPeriod_Type()
)
rcCfmMaExAisPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcCfmMaExAisPeriod.setStatus("current")


class _RcCfmMaExAisStatus_Type(Integer32):
    """Custom type rcCfmMaExAisStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("Active", 1),
          ("noActive", 2))
    )


_RcCfmMaExAisStatus_Type.__name__ = "Integer32"
_RcCfmMaExAisStatus_Object = MibTableColumn
rcCfmMaExAisStatus = _RcCfmMaExAisStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 21, 1, 5),
    _RcCfmMaExAisStatus_Type()
)
rcCfmMaExAisStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmMaExAisStatus.setStatus("current")


class _RcCfmMaExAisAge_Type(Unsigned32):
    """Custom type rcCfmMaExAisAge based on Unsigned32"""
    defaultValue = 0


_RcCfmMaExAisAge_Type.__name__ = "Unsigned32"
_RcCfmMaExAisAge_Object = MibTableColumn
rcCfmMaExAisAge = _RcCfmMaExAisAge_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 21, 1, 6),
    _RcCfmMaExAisAge_Type()
)
rcCfmMaExAisAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmMaExAisAge.setStatus("current")


class _RcCfmMaExAisStatisticsTx_Type(Unsigned32):
    """Custom type rcCfmMaExAisStatisticsTx based on Unsigned32"""
    defaultValue = 0


_RcCfmMaExAisStatisticsTx_Type.__name__ = "Unsigned32"
_RcCfmMaExAisStatisticsTx_Object = MibTableColumn
rcCfmMaExAisStatisticsTx = _RcCfmMaExAisStatisticsTx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 21, 1, 7),
    _RcCfmMaExAisStatisticsTx_Type()
)
rcCfmMaExAisStatisticsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmMaExAisStatisticsTx.setStatus("current")


class _RcCfmMaExAisStatisticsRx_Type(Unsigned32):
    """Custom type rcCfmMaExAisStatisticsRx based on Unsigned32"""
    defaultValue = 0


_RcCfmMaExAisStatisticsRx_Type.__name__ = "Unsigned32"
_RcCfmMaExAisStatisticsRx_Object = MibTableColumn
rcCfmMaExAisStatisticsRx = _RcCfmMaExAisStatisticsRx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 21, 1, 8),
    _RcCfmMaExAisStatisticsRx_Type()
)
rcCfmMaExAisStatisticsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmMaExAisStatisticsRx.setStatus("current")
_RcCfmMaExLckTable_Object = MibTable
rcCfmMaExLckTable = _RcCfmMaExLckTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 22)
)
if mibBuilder.loadTexts:
    rcCfmMaExLckTable.setStatus("current")
_RcCfmMaExLckEntry_Object = MibTableRow
rcCfmMaExLckEntry = _RcCfmMaExLckEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 22, 1)
)
rcCfmMaExLckEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
)
if mibBuilder.loadTexts:
    rcCfmMaExLckEntry.setStatus("current")


class _RcCfmMaExLckLevelAdmin_Type(Dot1agCfmMDLevelOrNone):
    """Custom type rcCfmMaExLckLevelAdmin based on Dot1agCfmMDLevelOrNone"""
    defaultValue = -1


_RcCfmMaExLckLevelAdmin_Type.__name__ = "Dot1agCfmMDLevelOrNone"
_RcCfmMaExLckLevelAdmin_Object = MibTableColumn
rcCfmMaExLckLevelAdmin = _RcCfmMaExLckLevelAdmin_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 22, 1, 1),
    _RcCfmMaExLckLevelAdmin_Type()
)
rcCfmMaExLckLevelAdmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcCfmMaExLckLevelAdmin.setStatus("current")
_RcCfmMaExLckLevelOper_Type = Dot1agCfmMDLevelOrNone
_RcCfmMaExLckLevelOper_Object = MibTableColumn
rcCfmMaExLckLevelOper = _RcCfmMaExLckLevelOper_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 22, 1, 2),
    _RcCfmMaExLckLevelOper_Type()
)
rcCfmMaExLckLevelOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmMaExLckLevelOper.setStatus("current")


class _RcCfmMaExLckPeriod_Type(Integer32):
    """Custom type rcCfmMaExLckPeriod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              60)
        )
    )
    namedValues = NamedValues(
        *(("lckPeriod1s", 1),
          ("lckPeriod60s", 60))
    )


_RcCfmMaExLckPeriod_Type.__name__ = "Integer32"
_RcCfmMaExLckPeriod_Object = MibTableColumn
rcCfmMaExLckPeriod = _RcCfmMaExLckPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 22, 1, 3),
    _RcCfmMaExLckPeriod_Type()
)
rcCfmMaExLckPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcCfmMaExLckPeriod.setStatus("current")


class _RcCfmMaExLckStatus_Type(Integer32):
    """Custom type rcCfmMaExLckStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("Active", 1),
          ("noActive", 2))
    )


_RcCfmMaExLckStatus_Type.__name__ = "Integer32"
_RcCfmMaExLckStatus_Object = MibTableColumn
rcCfmMaExLckStatus = _RcCfmMaExLckStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 22, 1, 4),
    _RcCfmMaExLckStatus_Type()
)
rcCfmMaExLckStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmMaExLckStatus.setStatus("current")


class _RcCfmMaExLckAge_Type(Unsigned32):
    """Custom type rcCfmMaExLckAge based on Unsigned32"""
    defaultValue = 0


_RcCfmMaExLckAge_Type.__name__ = "Unsigned32"
_RcCfmMaExLckAge_Object = MibTableColumn
rcCfmMaExLckAge = _RcCfmMaExLckAge_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 22, 1, 5),
    _RcCfmMaExLckAge_Type()
)
rcCfmMaExLckAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmMaExLckAge.setStatus("current")


class _RcCfmMaExLckStatisticsTx_Type(Unsigned32):
    """Custom type rcCfmMaExLckStatisticsTx based on Unsigned32"""
    defaultValue = 0


_RcCfmMaExLckStatisticsTx_Type.__name__ = "Unsigned32"
_RcCfmMaExLckStatisticsTx_Object = MibTableColumn
rcCfmMaExLckStatisticsTx = _RcCfmMaExLckStatisticsTx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 22, 1, 6),
    _RcCfmMaExLckStatisticsTx_Type()
)
rcCfmMaExLckStatisticsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmMaExLckStatisticsTx.setStatus("current")


class _RcCfmMaExLckStatisticsRx_Type(Unsigned32):
    """Custom type rcCfmMaExLckStatisticsRx based on Unsigned32"""
    defaultValue = 0


_RcCfmMaExLckStatisticsRx_Type.__name__ = "Unsigned32"
_RcCfmMaExLckStatisticsRx_Object = MibTableColumn
rcCfmMaExLckStatisticsRx = _RcCfmMaExLckStatisticsRx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 22, 1, 7),
    _RcCfmMaExLckStatisticsRx_Type()
)
rcCfmMaExLckStatisticsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmMaExLckStatisticsRx.setStatus("current")
_RcCfmNotifications_ObjectIdentity = ObjectIdentity
rcCfmNotifications = _RcCfmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 23)
)
_RcCfmMulticastLbResultTable_Object = MibTable
rcCfmMulticastLbResultTable = _RcCfmMulticastLbResultTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 24)
)
if mibBuilder.loadTexts:
    rcCfmMulticastLbResultTable.setStatus("current")
_RcCfmMulticastLbResultEntry_Object = MibTableRow
rcCfmMulticastLbResultEntry = _RcCfmMulticastLbResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 24, 1)
)
rcCfmMulticastLbResultEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "RAISECOM-CFM-MIB", "rcCfmMcastLbResultIndex"),
)
if mibBuilder.loadTexts:
    rcCfmMulticastLbResultEntry.setStatus("current")


class _RcCfmMcastLbResultIndex_Type(Unsigned32):
    """Custom type rcCfmMcastLbResultIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_RcCfmMcastLbResultIndex_Type.__name__ = "Unsigned32"
_RcCfmMcastLbResultIndex_Object = MibTableColumn
rcCfmMcastLbResultIndex = _RcCfmMcastLbResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 24, 1, 1),
    _RcCfmMcastLbResultIndex_Type()
)
rcCfmMcastLbResultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmMcastLbResultIndex.setStatus("current")


class _RcCfmMcastLbResultRemoteMepId_Type(Unsigned32):
    """Custom type rcCfmMcastLbResultRemoteMepId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_RcCfmMcastLbResultRemoteMepId_Type.__name__ = "Unsigned32"
_RcCfmMcastLbResultRemoteMepId_Object = MibTableColumn
rcCfmMcastLbResultRemoteMepId = _RcCfmMcastLbResultRemoteMepId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 24, 1, 2),
    _RcCfmMcastLbResultRemoteMepId_Type()
)
rcCfmMcastLbResultRemoteMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmMcastLbResultRemoteMepId.setStatus("current")


class _RcCfmMcastLbResultRecvPort_Type(Unsigned32):
    """Custom type rcCfmMcastLbResultRecvPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RcCfmMcastLbResultRecvPort_Type.__name__ = "Unsigned32"
_RcCfmMcastLbResultRecvPort_Object = MibTableColumn
rcCfmMcastLbResultRecvPort = _RcCfmMcastLbResultRecvPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 24, 1, 3),
    _RcCfmMcastLbResultRecvPort_Type()
)
rcCfmMcastLbResultRecvPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmMcastLbResultRecvPort.setStatus("current")
_RcCfmMcastLbResultMacAddress_Type = MacAddress
_RcCfmMcastLbResultMacAddress_Object = MibTableColumn
rcCfmMcastLbResultMacAddress = _RcCfmMcastLbResultMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 24, 1, 4),
    _RcCfmMcastLbResultMacAddress_Type()
)
rcCfmMcastLbResultMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmMcastLbResultMacAddress.setStatus("current")
_RcCfmMcastLbResultRtt_Type = Unsigned32
_RcCfmMcastLbResultRtt_Object = MibTableColumn
rcCfmMcastLbResultRtt = _RcCfmMcastLbResultRtt_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 24, 1, 5),
    _RcCfmMcastLbResultRtt_Type()
)
rcCfmMcastLbResultRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCfmMcastLbResultRtt.setStatus("current")
_RcCfmMipExTable_Object = MibTable
rcCfmMipExTable = _RcCfmMipExTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 25)
)
if mibBuilder.loadTexts:
    rcCfmMipExTable.setStatus("current")
_RcCfmMipExEntry_Object = MibTableRow
rcCfmMipExEntry = _RcCfmMipExEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 25, 1)
)
rcCfmMipExEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaCompPrimaryVlanId"),
    (0, "RAISECOM-CFM-MIB", "rcCfmMipExIfIndex"),
)
if mibBuilder.loadTexts:
    rcCfmMipExEntry.setStatus("current")
_RcCfmMipExIfIndex_Type = Integer32
_RcCfmMipExIfIndex_Object = MibTableColumn
rcCfmMipExIfIndex = _RcCfmMipExIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 25, 1, 1),
    _RcCfmMipExIfIndex_Type()
)
rcCfmMipExIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcCfmMipExIfIndex.setStatus("current")
_RcCfmMipRowStatus_Type = RowStatus
_RcCfmMipRowStatus_Object = MibTableColumn
rcCfmMipRowStatus = _RcCfmMipRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 25, 1, 2),
    _RcCfmMipRowStatus_Type()
)
rcCfmMipRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcCfmMipRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects

rcCfmPmFLRRaisingThreshFaultAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 23, 1)
)
rcCfmPmFLRRaisingThreshFaultAlarm.setObjects(
    ("RAISECOM-CFM-MIB", "rcCfmPMFLRRisingThreshold")
)
if mibBuilder.loadTexts:
    rcCfmPmFLRRaisingThreshFaultAlarm.setStatus(
        "deprecated"
    )

rcCfmPmFLRFallingThreshFaultAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 23, 2)
)
rcCfmPmFLRFallingThreshFaultAlarm.setObjects(
    ("RAISECOM-CFM-MIB", "rcCfmPMFLRFallingThreshold")
)
if mibBuilder.loadTexts:
    rcCfmPmFLRFallingThreshFaultAlarm.setStatus(
        "deprecated"
    )

rcCfmPmDelayRisingThreshFaultAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 23, 3)
)
rcCfmPmDelayRisingThreshFaultAlarm.setObjects(
    ("RAISECOM-CFM-MIB", "rcCfmPMDelayRisingThreshold")
)
if mibBuilder.loadTexts:
    rcCfmPmDelayRisingThreshFaultAlarm.setStatus(
        "deprecated"
    )

rcCfmPmDelayFallingThreshFaultAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 23, 4)
)
rcCfmPmDelayFallingThreshFaultAlarm.setObjects(
    ("RAISECOM-CFM-MIB", "rcCfmPMDelayFallingThreshold")
)
if mibBuilder.loadTexts:
    rcCfmPmDelayFallingThreshFaultAlarm.setStatus(
        "deprecated"
    )

rcCfmPmDVRisingThreshFaultAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 23, 5)
)
rcCfmPmDVRisingThreshFaultAlarm.setObjects(
    ("RAISECOM-CFM-MIB", "rcCfmPMDVRisingThreshold")
)
if mibBuilder.loadTexts:
    rcCfmPmDVRisingThreshFaultAlarm.setStatus(
        "deprecated"
    )

rcCfmPmDVFallingThreshFaultAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 26, 23, 6)
)
rcCfmPmDVFallingThreshFaultAlarm.setObjects(
    ("RAISECOM-CFM-MIB", "rcCfmPMDVFallingThreshold")
)
if mibBuilder.loadTexts:
    rcCfmPmDVFallingThreshFaultAlarm.setStatus(
        "deprecated"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-CFM-MIB",
    **{"rcCfm": rcCfm,
       "rcCfmBridge": rcCfmBridge,
       "rcCfmBridgeAdminCfm": rcCfmBridgeAdminCfm,
       "rcCfmBridgeCcmDbArchiveHoldtime": rcCfmBridgeCcmDbArchiveHoldtime,
       "rcCfmBridgeTracerouteCacheEnable": rcCfmBridgeTracerouteCacheEnable,
       "rcCfmBridgeTracerouteCacheHoldtime": rcCfmBridgeTracerouteCacheHoldtime,
       "rcCfmBridgeTracerouteCacheSize": rcCfmBridgeTracerouteCacheSize,
       "rcCfmBridgeTracerouteCacheClear": rcCfmBridgeTracerouteCacheClear,
       "rcCfmBridgeTrapConfig": rcCfmBridgeTrapConfig,
       "rcCfmBridgeRmepAgeTime": rcCfmBridgeRmepAgeTime,
       "rcCfmBridgeMode": rcCfmBridgeMode,
       "rcCfmLinkVlanList": rcCfmLinkVlanList,
       "rcCfmIfTable": rcCfmIfTable,
       "rcCfmIfEntry": rcCfmIfEntry,
       "rcCfmIfIndex": rcCfmIfIndex,
       "rcCfmIfAdminCfm": rcCfmIfAdminCfm,
       "rcCfmIfMipLevel": rcCfmIfMipLevel,
       "rcCfmMdTable": rcCfmMdTable,
       "rcCfmMdEntry": rcCfmMdEntry,
       "rcCfmMdCcmRMpClear": rcCfmMdCcmRMpClear,
       "rcCfmErrorCcmTable": rcCfmErrorCcmTable,
       "rcCfmErrorCcmEntry": rcCfmErrorCcmEntry,
       "rcCfmErrorCcmRMepId": rcCfmErrorCcmRMepId,
       "rcCfmErrorCcmIndex": rcCfmErrorCcmIndex,
       "rcCfmErrorCcmLevel": rcCfmErrorCcmLevel,
       "rcCfmErrorCcmVlan": rcCfmErrorCcmVlan,
       "rcCfmErrorCcmRecvMdName": rcCfmErrorCcmRecvMdName,
       "rcCfmErrorCcmMaid": rcCfmErrorCcmMaid,
       "rcCfmErrorCcmMacAddress": rcCfmErrorCcmMacAddress,
       "rcCfmErrorCcmErrorType": rcCfmErrorCcmErrorType,
       "rcCfmErrorCcmHoldTime": rcCfmErrorCcmHoldTime,
       "rcCfmErrorCcmClear": rcCfmErrorCcmClear,
       "rcCfmLtmDbTable": rcCfmLtmDbTable,
       "rcCfmLtmDbEntry": rcCfmLtmDbEntry,
       "rcCfmLtmDbTransactionId": rcCfmLtmDbTransactionId,
       "rcCfmLtmDbTargetMacAddress": rcCfmLtmDbTargetMacAddress,
       "rcCfmMepDbExTable": rcCfmMepDbExTable,
       "rcCfmMepDbExEntry": rcCfmMepDbExEntry,
       "rcCfmMepDbExEntryHoldTime": rcCfmMepDbExEntryHoldTime,
       "rcCfmMaCciEnableTable": rcCfmMaCciEnableTable,
       "rcCfmMaCciEnableEntry": rcCfmMaCciEnableEntry,
       "rcCfmMaMdLevel": rcCfmMaMdLevel,
       "rcCfmMaMaVlanId": rcCfmMaMaVlanId,
       "rcCfmMaCciEnabled": rcCfmMaCciEnabled,
       "rcCfmMepExTable": rcCfmMepExTable,
       "rcCfmMepExEntry": rcCfmMepExEntry,
       "rcCfmMepExLbrTimeoutNum": rcCfmMepExLbrTimeoutNum,
       "rcCfmMepExTransmitLbmDataTlvLen": rcCfmMepExTransmitLbmDataTlvLen,
       "rcCfmMepExLckAdmin": rcCfmMepExLckAdmin,
       "rcCfmMaExAisSuppressStatus": rcCfmMaExAisSuppressStatus,
       "rcCfmMaExAisSuppressAdmin": rcCfmMaExAisSuppressAdmin,
       "rcCfmMepExPduPriority": rcCfmMepExPduPriority,
       "rcCfmMepExPmAdmin": rcCfmMepExPmAdmin,
       "rcCfmMepExRdiAdmin": rcCfmMepExRdiAdmin,
       "rcCfmMaMepListExTable": rcCfmMaMepListExTable,
       "rcCfmMaMepListExEntry": rcCfmMaMepListExEntry,
       "rcCfmMaMepListType": rcCfmMaMepListType,
       "rcCfmMaMepListMacAddress": rcCfmMaMepListMacAddress,
       "rcCfmMaMepListIfIndex": rcCfmMaMepListIfIndex,
       "rcCfmMaNetExTable": rcCfmMaNetExTable,
       "rcCfmMaNetExEntry": rcCfmMaNetExEntry,
       "rcCfmMaNetRemoteMepLearnEnabled": rcCfmMaNetRemoteMepLearnEnabled,
       "rcCfmMaNetCostumerVlan": rcCfmMaNetCostumerVlan,
       "rcCfmMaNetPduPriority": rcCfmMaNetPduPriority,
       "rcCfmMaNetRemoteMepLearnActive": rcCfmMaNetRemoteMepLearnActive,
       "rcCfmMaNetCcCheckEnabled": rcCfmMaNetCcCheckEnabled,
       "rcCfmPMTable": rcCfmPMTable,
       "rcCfmPMEntry": rcCfmPMEntry,
       "rcCfmPMEnabled": rcCfmPMEnabled,
       "rcCfmPMDmmTxInterval": rcCfmPMDmmTxInterval,
       "rcCfmPMDelayObjective": rcCfmPMDelayObjective,
       "rcCfmPMDVObjective": rcCfmPMDVObjective,
       "rcCfmPMFLRRisingThreshold": rcCfmPMFLRRisingThreshold,
       "rcCfmPMFLRFallingThreshold": rcCfmPMFLRFallingThreshold,
       "rcCfmPMDelayRisingThreshold": rcCfmPMDelayRisingThreshold,
       "rcCfmPMDelayFallingThreshold": rcCfmPMDelayFallingThreshold,
       "rcCfmPMDVRisingThreshold": rcCfmPMDVRisingThreshold,
       "rcCfmPMDVFallingThreshold": rcCfmPMDVFallingThreshold,
       "rcCfmPMStatiticsClear": rcCfmPMStatiticsClear,
       "rcCfmPMTrapSendEnable": rcCfmPMTrapSendEnable,
       "rcCfmPMThroughputTimeout": rcCfmPMThroughputTimeout,
       "rcCfmPMThroughputObject": rcCfmPMThroughputObject,
       "rcCfmPMThroughputPduLength": rcCfmPMThroughputPduLength,
       "rcCfmPMThroughputEnable": rcCfmPMThroughputEnable,
       "rcCfmPMRowStatus": rcCfmPMRowStatus,
       "rcCfmPMFLRTotalTable": rcCfmPMFLRTotalTable,
       "rcCfmPMFLRTotalEntry": rcCfmPMFLRTotalEntry,
       "rcCfmPMFLRTotalElapsedTime": rcCfmPMFLRTotalElapsedTime,
       "rcCfmPMFLRTotalFarEndTxCounter": rcCfmPMFLRTotalFarEndTxCounter,
       "rcCfmPMFLRTotalFarEndLostCounter": rcCfmPMFLRTotalFarEndLostCounter,
       "rcCfmPMFLRTotalFarEndLossRatio": rcCfmPMFLRTotalFarEndLossRatio,
       "rcCfmPMFLRTotalFarEndUnaviableSecond": rcCfmPMFLRTotalFarEndUnaviableSecond,
       "rcCfmPMFLRTotalNearEndTxCounter": rcCfmPMFLRTotalNearEndTxCounter,
       "rcCfmPMFLRTotalNearEndLostCounter": rcCfmPMFLRTotalNearEndLostCounter,
       "rcCfmPMFLRTotalNearEndLossRatio": rcCfmPMFLRTotalNearEndLossRatio,
       "rcCfmPMFLRTotalNearEndUnaviableSecond": rcCfmPMFLRTotalNearEndUnaviableSecond,
       "rcCfmPMFLRCurrentTable": rcCfmPMFLRCurrentTable,
       "rcCfmPMFLRCurrentEntry": rcCfmPMFLRCurrentEntry,
       "rcCfmPMFLRCurrentPeriod": rcCfmPMFLRCurrentPeriod,
       "rcCfmPMFLRCurrentElapsedTime": rcCfmPMFLRCurrentElapsedTime,
       "rcCfmPMFLRCurrentFarEndTxFrameCounter": rcCfmPMFLRCurrentFarEndTxFrameCounter,
       "rcCfmPMFLRCurrentFarEndLostFrameCounter": rcCfmPMFLRCurrentFarEndLostFrameCounter,
       "rcCfmPMFLRCurrentFarEndLossRatio": rcCfmPMFLRCurrentFarEndLossRatio,
       "rcCfmPMFLRCurrentNearEndTxFrameCounter": rcCfmPMFLRCurrentNearEndTxFrameCounter,
       "rcCfmPMFLRCurrentNearEndLostFrameCounter": rcCfmPMFLRCurrentNearEndLostFrameCounter,
       "rcCfmPMFLRCurrentNearEndLossRatio": rcCfmPMFLRCurrentNearEndLossRatio,
       "rcCfmPMFLRIntervalTable": rcCfmPMFLRIntervalTable,
       "rcCfmPMFLRIntervalEntry": rcCfmPMFLRIntervalEntry,
       "rcCfmPMFLRIntervalPeriod": rcCfmPMFLRIntervalPeriod,
       "rcCfmPMFLRIntervalIndex": rcCfmPMFLRIntervalIndex,
       "rcCfmPMFLRIntervalPeerMepId": rcCfmPMFLRIntervalPeerMepId,
       "rcCfmPMFLRIntervalBeginTime": rcCfmPMFLRIntervalBeginTime,
       "rcCfmPMFLRIntervalFarEndTxFrameCounter": rcCfmPMFLRIntervalFarEndTxFrameCounter,
       "rcCfmPMFLRIntervalFarEndLostFrameCounter": rcCfmPMFLRIntervalFarEndLostFrameCounter,
       "rcCfmPMFLRIntervalFarEndLossRatio": rcCfmPMFLRIntervalFarEndLossRatio,
       "rcCfmPMFLRIntervalNearEndTxFrameCounter": rcCfmPMFLRIntervalNearEndTxFrameCounter,
       "rcCfmPMFLRIntervalNearEndLostFrameCounter": rcCfmPMFLRIntervalNearEndLostFrameCounter,
       "rcCfmPMFLRIntervalNearEndLossRatio": rcCfmPMFLRIntervalNearEndLossRatio,
       "rcCfmPMDelayCurrentTable": rcCfmPMDelayCurrentTable,
       "rcCfmPMDelayCurrentEntry": rcCfmPMDelayCurrentEntry,
       "rcCfmPMDelayCurrentPeriod": rcCfmPMDelayCurrentPeriod,
       "rcCfmPMDelayCurrentFarEndAboveObjCounter": rcCfmPMDelayCurrentFarEndAboveObjCounter,
       "rcCfmPMDelayCurrentFarEndBelowObjCounter": rcCfmPMDelayCurrentFarEndBelowObjCounter,
       "rcCfmPMDelayCurrentFarEndMaxDelay": rcCfmPMDelayCurrentFarEndMaxDelay,
       "rcCfmPMDelayCurrentFarEndAvgDelay": rcCfmPMDelayCurrentFarEndAvgDelay,
       "rcCfmPMDelayCurrentFarEndMinDelay": rcCfmPMDelayCurrentFarEndMinDelay,
       "rcCfmPMDelayCurrentNearEndAboveObjCounter": rcCfmPMDelayCurrentNearEndAboveObjCounter,
       "rcCfmPMDelayCurrentNearEndBelowObjCounter": rcCfmPMDelayCurrentNearEndBelowObjCounter,
       "rcCfmPMDelayCurrentNearEndMaxDelay": rcCfmPMDelayCurrentNearEndMaxDelay,
       "rcCfmPMDelayCurrentNearEndAvgDelay": rcCfmPMDelayCurrentNearEndAvgDelay,
       "rcCfmPMDelayCurrentNearEndMinDelay": rcCfmPMDelayCurrentNearEndMinDelay,
       "rcCfmPMDelayCurrentRoundTripAboveObjCounter": rcCfmPMDelayCurrentRoundTripAboveObjCounter,
       "rcCfmPMDelayCurrentRoundTripBelowObjCounter": rcCfmPMDelayCurrentRoundTripBelowObjCounter,
       "rcCfmPMDelayCurrentRoundTripMaxDelay": rcCfmPMDelayCurrentRoundTripMaxDelay,
       "rcCfmPMDelayCurrentRoundTripAvgDelay": rcCfmPMDelayCurrentRoundTripAvgDelay,
       "rcCfmPMDelayCurrentRoundTripMinDelay": rcCfmPMDelayCurrentRoundTripMinDelay,
       "rcCfmPMDelayIntervalTable": rcCfmPMDelayIntervalTable,
       "rcCfmPMDelayIntervalEntry": rcCfmPMDelayIntervalEntry,
       "rcCfmPMDelayIntervalPeriod": rcCfmPMDelayIntervalPeriod,
       "rcCfmPMDelayIntervalIndex": rcCfmPMDelayIntervalIndex,
       "rcCfmPMDelayIntervalBeginTime": rcCfmPMDelayIntervalBeginTime,
       "rcCfmPMDelayIntervalPeerMepId": rcCfmPMDelayIntervalPeerMepId,
       "rcCfmPMDelayIntervalFarEndAboveObjCounter": rcCfmPMDelayIntervalFarEndAboveObjCounter,
       "rcCfmPMDelayIntervalFarEndBelowObjCounter": rcCfmPMDelayIntervalFarEndBelowObjCounter,
       "rcCfmPMDelayIntervalFarEndMaxDelay": rcCfmPMDelayIntervalFarEndMaxDelay,
       "rcCfmPMDelayIntervalFarEndAvgDelay": rcCfmPMDelayIntervalFarEndAvgDelay,
       "rcCfmPMDelayIntervalFarEndMinDelay": rcCfmPMDelayIntervalFarEndMinDelay,
       "rcCfmPMDelayIntervalNearEndAboveObjCounter": rcCfmPMDelayIntervalNearEndAboveObjCounter,
       "rcCfmPMDelayIntervalNearEndBelowObjCounter": rcCfmPMDelayIntervalNearEndBelowObjCounter,
       "rcCfmPMDelayIntervalNearEndMaxDelay": rcCfmPMDelayIntervalNearEndMaxDelay,
       "rcCfmPMDelayIntervalNearEndAvgDelay": rcCfmPMDelayIntervalNearEndAvgDelay,
       "rcCfmPMDelayIntervalNearEndMinDelay": rcCfmPMDelayIntervalNearEndMinDelay,
       "rcCfmPMDelayIntervalRoundTripAboveObjCounter": rcCfmPMDelayIntervalRoundTripAboveObjCounter,
       "rcCfmPMDelayIntervalRoundTripBelowObjCounter": rcCfmPMDelayIntervalRoundTripBelowObjCounter,
       "rcCfmPMDelayIntervalRoundTripMaxDelay": rcCfmPMDelayIntervalRoundTripMaxDelay,
       "rcCfmPMDelayIntervalRoundTripAvgDelay": rcCfmPMDelayIntervalRoundTripAvgDelay,
       "rcCfmPMDelayIntervalRoundTripMinDelay": rcCfmPMDelayIntervalRoundTripMinDelay,
       "rcCfmPMDVCurrentTable": rcCfmPMDVCurrentTable,
       "rcCfmPMDVCurrentEntry": rcCfmPMDVCurrentEntry,
       "rcCfmPMDVCurrentPeriod": rcCfmPMDVCurrentPeriod,
       "rcCfmPMDVCurrentFarEndAboveObjCounter": rcCfmPMDVCurrentFarEndAboveObjCounter,
       "rcCfmPMDVCurrentFarEndBelowObjCounter": rcCfmPMDVCurrentFarEndBelowObjCounter,
       "rcCfmPMDVCurrentFarEndMaxDv": rcCfmPMDVCurrentFarEndMaxDv,
       "rcCfmPMDVCurrentFarEndAvgDv": rcCfmPMDVCurrentFarEndAvgDv,
       "rcCfmPMDVCurrentNearEndAboveObjCounter": rcCfmPMDVCurrentNearEndAboveObjCounter,
       "rcCfmPMDVCurrentNearEndBelowObjCounter": rcCfmPMDVCurrentNearEndBelowObjCounter,
       "rcCfmPMDVCurrentNearEndMaxDv": rcCfmPMDVCurrentNearEndMaxDv,
       "rcCfmPMDVCurrentNearEndAvgDv": rcCfmPMDVCurrentNearEndAvgDv,
       "rcCfmPMDVCurrentRoundTripAboveObjCounter": rcCfmPMDVCurrentRoundTripAboveObjCounter,
       "rcCfmPMDVCurrentRoundTripBelowObjCounter": rcCfmPMDVCurrentRoundTripBelowObjCounter,
       "rcCfmPMDVCurrentRoundTripMaxDv": rcCfmPMDVCurrentRoundTripMaxDv,
       "rcCfmPMDVCurrentRoundTripAvgDv": rcCfmPMDVCurrentRoundTripAvgDv,
       "rcCfmPMDVIntervalTable": rcCfmPMDVIntervalTable,
       "rcCfmPMDVIntervalEntry": rcCfmPMDVIntervalEntry,
       "rcCfmPMDVIntervalPeriod": rcCfmPMDVIntervalPeriod,
       "rcCfmPMDVIntervalIndex": rcCfmPMDVIntervalIndex,
       "rcCfmPMDVIntervalBeginTime": rcCfmPMDVIntervalBeginTime,
       "rcCfmPMDVIntervalPeerMepId": rcCfmPMDVIntervalPeerMepId,
       "rcCfmPMDVIntervalFarEndAboveObjCounter": rcCfmPMDVIntervalFarEndAboveObjCounter,
       "rcCfmPMDVIntervalFarEndBelowObjCounter": rcCfmPMDVIntervalFarEndBelowObjCounter,
       "rcCfmPMDVIntervalFarEndMaxDv": rcCfmPMDVIntervalFarEndMaxDv,
       "rcCfmPMDVIntervalFarEndAvgDv": rcCfmPMDVIntervalFarEndAvgDv,
       "rcCfmPMDVIntervalNearEndAboveObjCounter": rcCfmPMDVIntervalNearEndAboveObjCounter,
       "rcCfmPMDVIntervalNearEndBelowObjCounter": rcCfmPMDVIntervalNearEndBelowObjCounter,
       "rcCfmPMDVIntervalNearEndMaxDv": rcCfmPMDVIntervalNearEndMaxDv,
       "rcCfmPMDVIntervalNearEndAvgDv": rcCfmPMDVIntervalNearEndAvgDv,
       "rcCfmPMDVIntervalRoundTripAboveObjCounter": rcCfmPMDVIntervalRoundTripAboveObjCounter,
       "rcCfmPMDVIntervalRoundTripBelowObjCounter": rcCfmPMDVIntervalRoundTripBelowObjCounter,
       "rcCfmPMDVIntervalRoundTripMaxDv": rcCfmPMDVIntervalRoundTripMaxDv,
       "rcCfmPMDVIntervalRoundTripAvgDv": rcCfmPMDVIntervalRoundTripAvgDv,
       "rcCfmPMThroughputTable": rcCfmPMThroughputTable,
       "rcCfmPMThroughputEntry": rcCfmPMThroughputEntry,
       "rcCfmPMThroughputTestResult": rcCfmPMThroughputTestResult,
       "rcCfmPMThroughputTestState": rcCfmPMThroughputTestState,
       "rcCfmPMThroughputFarEndSendbps": rcCfmPMThroughputFarEndSendbps,
       "rcCfmPMThroughputFarEndRecievebps": rcCfmPMThroughputFarEndRecievebps,
       "rcCfmPMThroughputFarEndSendpps": rcCfmPMThroughputFarEndSendpps,
       "rcCfmPMThroughputFarEndRecievepps": rcCfmPMThroughputFarEndRecievepps,
       "rcCfmPMThroughputNearEndSendbps": rcCfmPMThroughputNearEndSendbps,
       "rcCfmPMThroughputNearEndRecievebps": rcCfmPMThroughputNearEndRecievebps,
       "rcCfmPMThroughputNearEndSendpps": rcCfmPMThroughputNearEndSendpps,
       "rcCfmPMThroughputNearEndRecievepps": rcCfmPMThroughputNearEndRecievepps,
       "rcCfmMaExTable": rcCfmMaExTable,
       "rcCfmMaExEntry": rcCfmMaExEntry,
       "rcCfmMaExFormat": rcCfmMaExFormat,
       "rcCfmMaExName": rcCfmMaExName,
       "rcCfmMaExVlanList": rcCfmMaExVlanList,
       "rcCfmMaExCcmInterval": rcCfmMaExCcmInterval,
       "rcCfmMaExCostumerVlan": rcCfmMaExCostumerVlan,
       "rcCfmMaExPduPriority": rcCfmMaExPduPriority,
       "rcCfmMaExRowStatus": rcCfmMaExRowStatus,
       "rcCfmMaExPrimaryVlanId": rcCfmMaExPrimaryVlanId,
       "rcCfmMaExMipAutocreateAdmin": rcCfmMaExMipAutocreateAdmin,
       "rcCfmMaExAisTable": rcCfmMaExAisTable,
       "rcCfmMaExAisEntry": rcCfmMaExAisEntry,
       "rcCfmMaExAisEnable": rcCfmMaExAisEnable,
       "rcCfmMaExAisLevelAdmin": rcCfmMaExAisLevelAdmin,
       "rcCfmMaExAisLevelOper": rcCfmMaExAisLevelOper,
       "rcCfmMaExAisPeriod": rcCfmMaExAisPeriod,
       "rcCfmMaExAisStatus": rcCfmMaExAisStatus,
       "rcCfmMaExAisAge": rcCfmMaExAisAge,
       "rcCfmMaExAisStatisticsTx": rcCfmMaExAisStatisticsTx,
       "rcCfmMaExAisStatisticsRx": rcCfmMaExAisStatisticsRx,
       "rcCfmMaExLckTable": rcCfmMaExLckTable,
       "rcCfmMaExLckEntry": rcCfmMaExLckEntry,
       "rcCfmMaExLckLevelAdmin": rcCfmMaExLckLevelAdmin,
       "rcCfmMaExLckLevelOper": rcCfmMaExLckLevelOper,
       "rcCfmMaExLckPeriod": rcCfmMaExLckPeriod,
       "rcCfmMaExLckStatus": rcCfmMaExLckStatus,
       "rcCfmMaExLckAge": rcCfmMaExLckAge,
       "rcCfmMaExLckStatisticsTx": rcCfmMaExLckStatisticsTx,
       "rcCfmMaExLckStatisticsRx": rcCfmMaExLckStatisticsRx,
       "rcCfmNotifications": rcCfmNotifications,
       "rcCfmPmFLRRaisingThreshFaultAlarm": rcCfmPmFLRRaisingThreshFaultAlarm,
       "rcCfmPmFLRFallingThreshFaultAlarm": rcCfmPmFLRFallingThreshFaultAlarm,
       "rcCfmPmDelayRisingThreshFaultAlarm": rcCfmPmDelayRisingThreshFaultAlarm,
       "rcCfmPmDelayFallingThreshFaultAlarm": rcCfmPmDelayFallingThreshFaultAlarm,
       "rcCfmPmDVRisingThreshFaultAlarm": rcCfmPmDVRisingThreshFaultAlarm,
       "rcCfmPmDVFallingThreshFaultAlarm": rcCfmPmDVFallingThreshFaultAlarm,
       "rcCfmMulticastLbResultTable": rcCfmMulticastLbResultTable,
       "rcCfmMulticastLbResultEntry": rcCfmMulticastLbResultEntry,
       "rcCfmMcastLbResultIndex": rcCfmMcastLbResultIndex,
       "rcCfmMcastLbResultRemoteMepId": rcCfmMcastLbResultRemoteMepId,
       "rcCfmMcastLbResultRecvPort": rcCfmMcastLbResultRecvPort,
       "rcCfmMcastLbResultMacAddress": rcCfmMcastLbResultMacAddress,
       "rcCfmMcastLbResultRtt": rcCfmMcastLbResultRtt,
       "rcCfmMipExTable": rcCfmMipExTable,
       "rcCfmMipExEntry": rcCfmMipExEntry,
       "rcCfmMipExIfIndex": rcCfmMipExIfIndex,
       "rcCfmMipRowStatus": rcCfmMipRowStatus}
)
