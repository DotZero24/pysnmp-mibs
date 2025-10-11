# SNMP MIB module (ZXEPON-SERVICE-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZXEPON-SERVICE-PRIVATE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:46 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(ZxAnIdList,) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "ZxAnIdList")

(zxAnEponMib,) = mibBuilder.importSymbols(
    "ZTE-MASTER-MIB",
    "zxAnEponMib")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PrivateObjects_ObjectIdentity = ObjectIdentity
privateObjects = _PrivateObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7)
)
_SysAttrObjectTable_Object = MibTable
sysAttrObjectTable = _SysAttrObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 1)
)
if mibBuilder.loadTexts:
    sysAttrObjectTable.setStatus("current")
_SysAttrObjectEntry_Object = MibTableRow
sysAttrObjectEntry = _SysAttrObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 1, 1)
)
sysAttrObjectEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    sysAttrObjectEntry.setStatus("current")


class _SysOnuAdminAuthMode_Type(Integer32):
    """Custom type sysOnuAdminAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("mac", 1),
          ("sn", 2),
          ("hybrid", 3),
          ("loid", 4),
          ("snPlusMac", 5))
    )


_SysOnuAdminAuthMode_Type.__name__ = "Integer32"
_SysOnuAdminAuthMode_Object = MibTableColumn
sysOnuAdminAuthMode = _SysOnuAdminAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 1, 1, 1),
    _SysOnuAdminAuthMode_Type()
)
sysOnuAdminAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysOnuAdminAuthMode.setStatus("current")


class _SysAttrAutoAuthEnable_Type(Integer32):
    """Custom type sysAttrAutoAuthEnable based on Integer32"""
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


_SysAttrAutoAuthEnable_Type.__name__ = "Integer32"
_SysAttrAutoAuthEnable_Object = MibTableColumn
sysAttrAutoAuthEnable = _SysAttrAutoAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 1, 1, 2),
    _SysAttrAutoAuthEnable_Type()
)
sysAttrAutoAuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAttrAutoAuthEnable.setStatus("current")


class _MacHwAuthOnuState_Type(Integer32):
    """Custom type macHwAuthOnuState based on Integer32"""
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


_MacHwAuthOnuState_Type.__name__ = "Integer32"
_MacHwAuthOnuState_Object = MibTableColumn
macHwAuthOnuState = _MacHwAuthOnuState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 1, 1, 3),
    _MacHwAuthOnuState_Type()
)
macHwAuthOnuState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macHwAuthOnuState.setStatus("current")


class _ZxAnEponOnuSilenceEnable_Type(TruthValue):
    """Custom type zxAnEponOnuSilenceEnable based on TruthValue"""
    defaultValue = 1


_ZxAnEponOnuSilenceEnable_Type.__name__ = "TruthValue"
_ZxAnEponOnuSilenceEnable_Object = MibTableColumn
zxAnEponOnuSilenceEnable = _ZxAnEponOnuSilenceEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 1, 1, 4),
    _ZxAnEponOnuSilenceEnable_Type()
)
zxAnEponOnuSilenceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuSilenceEnable.setStatus("current")
_OltLinkAdminTestObjectTable_Object = MibTable
oltLinkAdminTestObjectTable = _OltLinkAdminTestObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 2)
)
if mibBuilder.loadTexts:
    oltLinkAdminTestObjectTable.setStatus("current")
_OltLinkAdminTestObjectEntry_Object = MibTableRow
oltLinkAdminTestObjectEntry = _OltLinkAdminTestObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 2, 1)
)
oltLinkAdminTestObjectEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    oltLinkAdminTestObjectEntry.setStatus("current")


class _TestControlMode_Type(Integer32):
    """Custom type testControlMode based on Integer32"""
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


_TestControlMode_Type.__name__ = "Integer32"
_TestControlMode_Object = MibTableColumn
testControlMode = _TestControlMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 2, 1, 1),
    _TestControlMode_Type()
)
testControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    testControlMode.setStatus("current")


class _TestResult_Type(Integer32):
    """Custom type testResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("fail", 2))
    )


_TestResult_Type.__name__ = "Integer32"
_TestResult_Object = MibTableColumn
testResult = _TestResult_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 2, 1, 2),
    _TestResult_Type()
)
testResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testResult.setStatus("current")
_OltLoopbackObjectTable_Object = MibTable
oltLoopbackObjectTable = _OltLoopbackObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 3)
)
if mibBuilder.loadTexts:
    oltLoopbackObjectTable.setStatus("current")
_OltLoopbackObjectEntry_Object = MibTableRow
oltLoopbackObjectEntry = _OltLoopbackObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 3, 1)
)
oltLoopbackObjectEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    oltLoopbackObjectEntry.setStatus("current")


class _LoopbackStation_Type(Integer32):
    """Custom type loopbackStation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pon", 1),
          ("nni", 2))
    )


_LoopbackStation_Type.__name__ = "Integer32"
_LoopbackStation_Object = MibTableColumn
loopbackStation = _LoopbackStation_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 3, 1, 1),
    _LoopbackStation_Type()
)
loopbackStation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopbackStation.setStatus("current")


class _LoopbackDirection_Type(Integer32):
    """Custom type loopbackDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("line", 1),
          ("system", 2))
    )


_LoopbackDirection_Type.__name__ = "Integer32"
_LoopbackDirection_Object = MibTableColumn
loopbackDirection = _LoopbackDirection_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 3, 1, 2),
    _LoopbackDirection_Type()
)
loopbackDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopbackDirection.setStatus("current")


class _LoopbackAdministration_Type(Integer32):
    """Custom type loopbackAdministration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mac", 1),
          ("phy", 2))
    )


_LoopbackAdministration_Type.__name__ = "Integer32"
_LoopbackAdministration_Object = MibTableColumn
loopbackAdministration = _LoopbackAdministration_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 3, 1, 3),
    _LoopbackAdministration_Type()
)
loopbackAdministration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopbackAdministration.setStatus("current")


class _LoopbackState_Type(Integer32):
    """Custom type loopbackState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noloopback", 1),
          ("loopback", 2))
    )


_LoopbackState_Type.__name__ = "Integer32"
_LoopbackState_Object = MibTableColumn
loopbackState = _LoopbackState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 3, 1, 4),
    _LoopbackState_Type()
)
loopbackState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopbackState.setStatus("current")
_OnuAdminObjectTable_Object = MibTable
onuAdminObjectTable = _OnuAdminObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 4)
)
if mibBuilder.loadTexts:
    onuAdminObjectTable.setStatus("current")
_OnuAdminObjectEntry_Object = MibTableRow
onuAdminObjectEntry = _OnuAdminObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 4, 1)
)
onuAdminObjectEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    onuAdminObjectEntry.setStatus("current")
_OnuDescript_Type = DisplayString
_OnuDescript_Object = MibTableColumn
onuDescript = _OnuDescript_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 4, 1, 1),
    _OnuDescript_Type()
)
onuDescript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuDescript.setStatus("current")
_OnuSplitterSn_Type = Integer32
_OnuSplitterSn_Object = MibTableColumn
onuSplitterSn = _OnuSplitterSn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 4, 1, 2),
    _OnuSplitterSn_Type()
)
onuSplitterSn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuSplitterSn.setStatus("current")
_OnuOpticalLineSn_Type = Integer32
_OnuOpticalLineSn_Object = MibTableColumn
onuOpticalLineSn = _OnuOpticalLineSn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 4, 1, 3),
    _OnuOpticalLineSn_Type()
)
onuOpticalLineSn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuOpticalLineSn.setStatus("current")
_OnuUserInfo_Type = DisplayString
_OnuUserInfo_Object = MibTableColumn
onuUserInfo = _OnuUserInfo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 4, 1, 4),
    _OnuUserInfo_Type()
)
onuUserInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuUserInfo.setStatus("current")
_OnuType_Type = DisplayString
_OnuType_Object = MibTableColumn
onuType = _OnuType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 4, 1, 5),
    _OnuType_Type()
)
onuType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuType.setStatus("current")


class _OnuAdminState_Type(Integer32):
    """Custom type onuAdminState based on Integer32"""
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


_OnuAdminState_Type.__name__ = "Integer32"
_OnuAdminState_Object = MibTableColumn
onuAdminState = _OnuAdminState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 4, 1, 6),
    _OnuAdminState_Type()
)
onuAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuAdminState.setStatus("current")
_OnuAuthMACAddress_Type = MacAddress
_OnuAuthMACAddress_Object = MibTableColumn
onuAuthMACAddress = _OnuAuthMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 4, 1, 7),
    _OnuAuthMACAddress_Type()
)
onuAuthMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuAuthMACAddress.setStatus("current")
_OnuRegisterMACAddress_Type = MacAddress
_OnuRegisterMACAddress_Object = MibTableColumn
onuRegisterMACAddress = _OnuRegisterMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 4, 1, 8),
    _OnuRegisterMACAddress_Type()
)
onuRegisterMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuRegisterMACAddress.setStatus("current")
_OnuAuthMACSn_Type = OctetString
_OnuAuthMACSn_Object = MibTableColumn
onuAuthMACSn = _OnuAuthMACSn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 4, 1, 9),
    _OnuAuthMACSn_Type()
)
onuAuthMACSn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuAuthMACSn.setStatus("current")
_OnuRegisterSn_Type = OctetString
_OnuRegisterSn_Object = MibTableColumn
onuRegisterSn = _OnuRegisterSn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 4, 1, 10),
    _OnuRegisterSn_Type()
)
onuRegisterSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuRegisterSn.setStatus("current")


class _OnuCurrentRegState_Type(Integer32):
    """Custom type onuCurrentRegState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unregister", 1),
          ("registering", 2),
          ("registered", 3))
    )


_OnuCurrentRegState_Type.__name__ = "Integer32"
_OnuCurrentRegState_Object = MibTableColumn
onuCurrentRegState = _OnuCurrentRegState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 4, 1, 11),
    _OnuCurrentRegState_Type()
)
onuCurrentRegState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuCurrentRegState.setStatus("current")
_OnuRegisterTime_Type = DisplayString
_OnuRegisterTime_Object = MibTableColumn
onuRegisterTime = _OnuRegisterTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 4, 1, 12),
    _OnuRegisterTime_Type()
)
onuRegisterTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuRegisterTime.setStatus("current")


class _OnuCurrAdminAuthState_Type(Integer32):
    """Custom type onuCurrAdminAuthState based on Integer32"""
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
        *(("init", 1),
          ("authenticating", 2),
          ("pass", 3),
          ("deny", 4))
    )


_OnuCurrAdminAuthState_Type.__name__ = "Integer32"
_OnuCurrAdminAuthState_Object = MibTableColumn
onuCurrAdminAuthState = _OnuCurrAdminAuthState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 4, 1, 13),
    _OnuCurrAdminAuthState_Type()
)
onuCurrAdminAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuCurrAdminAuthState.setStatus("current")
_OnuLatelyPassAdminAuthTime_Type = DisplayString
_OnuLatelyPassAdminAuthTime_Object = MibTableColumn
onuLatelyPassAdminAuthTime = _OnuLatelyPassAdminAuthTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 4, 1, 14),
    _OnuLatelyPassAdminAuthTime_Type()
)
onuLatelyPassAdminAuthTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuLatelyPassAdminAuthTime.setStatus("current")
_OnuCurrDot1xAuthState_Type = Integer32
_OnuCurrDot1xAuthState_Object = MibTableColumn
onuCurrDot1xAuthState = _OnuCurrDot1xAuthState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 4, 1, 15),
    _OnuCurrDot1xAuthState_Type()
)
onuCurrDot1xAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuCurrDot1xAuthState.setStatus("current")
_OnuLatelyPassDot1xAuthTime_Type = DisplayString
_OnuLatelyPassDot1xAuthTime_Object = MibTableColumn
onuLatelyPassDot1xAuthTime = _OnuLatelyPassDot1xAuthTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 4, 1, 16),
    _OnuLatelyPassDot1xAuthTime_Type()
)
onuLatelyPassDot1xAuthTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuLatelyPassDot1xAuthTime.setStatus("current")


class _OnuMgmtOnlineStatus_Type(Integer32):
    """Custom type onuMgmtOnlineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("poweroff", 1),
          ("offline", 2),
          ("online", 3))
    )


_OnuMgmtOnlineStatus_Type.__name__ = "Integer32"
_OnuMgmtOnlineStatus_Object = MibTableColumn
onuMgmtOnlineStatus = _OnuMgmtOnlineStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 4, 1, 17),
    _OnuMgmtOnlineStatus_Type()
)
onuMgmtOnlineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuMgmtOnlineStatus.setStatus("current")


class _OnuActiveStatus_Type(Integer32):
    """Custom type onuActiveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_OnuActiveStatus_Type.__name__ = "Integer32"
_OnuActiveStatus_Object = MibTableColumn
onuActiveStatus = _OnuActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 4, 1, 18),
    _OnuActiveStatus_Type()
)
onuActiveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuActiveStatus.setStatus("current")
_OnuMgmtEntryStatus_Type = RowStatus
_OnuMgmtEntryStatus_Object = MibTableColumn
onuMgmtEntryStatus = _OnuMgmtEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 4, 1, 19),
    _OnuMgmtEntryStatus_Type()
)
onuMgmtEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuMgmtEntryStatus.setStatus("current")


class _OnuMgmtIpCfgMode_Type(Integer32):
    """Custom type onuMgmtIpCfgMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynatmic", 2))
    )


_OnuMgmtIpCfgMode_Type.__name__ = "Integer32"
_OnuMgmtIpCfgMode_Object = MibTableColumn
onuMgmtIpCfgMode = _OnuMgmtIpCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 4, 1, 20),
    _OnuMgmtIpCfgMode_Type()
)
onuMgmtIpCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuMgmtIpCfgMode.setStatus("current")


class _OnuAuthLoid_Type(DisplayString):
    """Custom type onuAuthLoid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_OnuAuthLoid_Type.__name__ = "DisplayString"
_OnuAuthLoid_Object = MibTableColumn
onuAuthLoid = _OnuAuthLoid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 4, 1, 21),
    _OnuAuthLoid_Type()
)
onuAuthLoid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuAuthLoid.setStatus("current")


class _OnuAuthPassword_Type(DisplayString):
    """Custom type onuAuthPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_OnuAuthPassword_Type.__name__ = "DisplayString"
_OnuAuthPassword_Object = MibTableColumn
onuAuthPassword = _OnuAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 4, 1, 22),
    _OnuAuthPassword_Type()
)
onuAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuAuthPassword.setStatus("current")


class _OnuRegisterLoid_Type(DisplayString):
    """Custom type onuRegisterLoid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_OnuRegisterLoid_Type.__name__ = "DisplayString"
_OnuRegisterLoid_Object = MibTableColumn
onuRegisterLoid = _OnuRegisterLoid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 4, 1, 23),
    _OnuRegisterLoid_Type()
)
onuRegisterLoid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuRegisterLoid.setStatus("current")


class _OnuRegisterPassword_Type(DisplayString):
    """Custom type onuRegisterPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_OnuRegisterPassword_Type.__name__ = "DisplayString"
_OnuRegisterPassword_Object = MibTableColumn
onuRegisterPassword = _OnuRegisterPassword_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 4, 1, 24),
    _OnuRegisterPassword_Type()
)
onuRegisterPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuRegisterPassword.setStatus("current")


class _ZxAnEponOnuCreateTime_Type(DisplayString):
    """Custom type zxAnEponOnuCreateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_ZxAnEponOnuCreateTime_Type.__name__ = "DisplayString"
_ZxAnEponOnuCreateTime_Object = MibTableColumn
zxAnEponOnuCreateTime = _ZxAnEponOnuCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 4, 1, 25),
    _ZxAnEponOnuCreateTime_Type()
)
zxAnEponOnuCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuCreateTime.setStatus("current")


class _ZxAnEponOnuLastOfflineTime_Type(DisplayString):
    """Custom type zxAnEponOnuLastOfflineTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_ZxAnEponOnuLastOfflineTime_Type.__name__ = "DisplayString"
_ZxAnEponOnuLastOfflineTime_Object = MibTableColumn
zxAnEponOnuLastOfflineTime = _ZxAnEponOnuLastOfflineTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 4, 1, 26),
    _ZxAnEponOnuLastOfflineTime_Type()
)
zxAnEponOnuLastOfflineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuLastOfflineTime.setStatus("current")
_OltEncryAdminObjectTable_Object = MibTable
oltEncryAdminObjectTable = _OltEncryAdminObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 5)
)
if mibBuilder.loadTexts:
    oltEncryAdminObjectTable.setStatus("current")
_OltEncryAdminObjectEntry_Object = MibTableRow
oltEncryAdminObjectEntry = _OltEncryAdminObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 5, 1)
)
oltEncryAdminObjectEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    oltEncryAdminObjectEntry.setStatus("current")


class _EncryptArithmetic_Type(Integer32):
    """Custom type encryptArithmetic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aes128", 1),
          ("triplechurning", 2))
    )


_EncryptArithmetic_Type.__name__ = "Integer32"
_EncryptArithmetic_Object = MibTableColumn
encryptArithmetic = _EncryptArithmetic_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 5, 1, 1),
    _EncryptArithmetic_Type()
)
encryptArithmetic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    encryptArithmetic.setStatus("current")
_KeyUpdateTime_Type = Integer32
_KeyUpdateTime_Object = MibTableColumn
keyUpdateTime = _KeyUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 5, 1, 2),
    _KeyUpdateTime_Type()
)
keyUpdateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyUpdateTime.setStatus("current")
_KeyUpdateTimeout_Type = Integer32
_KeyUpdateTimeout_Object = MibTableColumn
keyUpdateTimeout = _KeyUpdateTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 5, 1, 3),
    _KeyUpdateTimeout_Type()
)
keyUpdateTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyUpdateTimeout.setStatus("current")
_StartEncryptThreshold_Type = Integer32
_StartEncryptThreshold_Object = MibTableColumn
startEncryptThreshold = _StartEncryptThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 5, 1, 4),
    _StartEncryptThreshold_Type()
)
startEncryptThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    startEncryptThreshold.setStatus("current")
_LineEncryAdminObjectTable_Object = MibTable
lineEncryAdminObjectTable = _LineEncryAdminObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 6)
)
if mibBuilder.loadTexts:
    lineEncryAdminObjectTable.setStatus("current")
_LineEncryAdminObjectEntry_Object = MibTableRow
lineEncryAdminObjectEntry = _LineEncryAdminObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 6, 1)
)
lineEncryAdminObjectEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    lineEncryAdminObjectEntry.setStatus("current")


class _EncryptMode_Type(Integer32):
    """Custom type encryptMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downlink", 1),
          ("both", 2))
    )


_EncryptMode_Type.__name__ = "Integer32"
_EncryptMode_Object = MibTableColumn
encryptMode = _EncryptMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 6, 1, 1),
    _EncryptMode_Type()
)
encryptMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    encryptMode.setStatus("current")
_EncrypeState_Type = TruthValue
_EncrypeState_Object = MibTableColumn
encrypeState = _EncrypeState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 6, 1, 2),
    _EncrypeState_Type()
)
encrypeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    encrypeState.setStatus("current")
_SlaUpAdminObjectTable_Object = MibTable
slaUpAdminObjectTable = _SlaUpAdminObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 7)
)
if mibBuilder.loadTexts:
    slaUpAdminObjectTable.setStatus("current")
_SlaUpAdminObjectEntry_Object = MibTableRow
slaUpAdminObjectEntry = _SlaUpAdminObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 7, 1)
)
slaUpAdminObjectEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    slaUpAdminObjectEntry.setStatus("current")
_UpFixedBw_Type = Integer32
_UpFixedBw_Object = MibTableColumn
upFixedBw = _UpFixedBw_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 7, 1, 1),
    _UpFixedBw_Type()
)
upFixedBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upFixedBw.setStatus("current")
_UpAssuredBw_Type = Integer32
_UpAssuredBw_Object = MibTableColumn
upAssuredBw = _UpAssuredBw_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 7, 1, 2),
    _UpAssuredBw_Type()
)
upAssuredBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upAssuredBw.setStatus("current")
_UpMaximumBw_Type = Integer32
_UpMaximumBw_Object = MibTableColumn
upMaximumBw = _UpMaximumBw_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 7, 1, 3),
    _UpMaximumBw_Type()
)
upMaximumBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upMaximumBw.setStatus("current")
_UpMaxBurstSize_Type = Integer32
_UpMaxBurstSize_Object = MibTableColumn
upMaxBurstSize = _UpMaxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 7, 1, 4),
    _UpMaxBurstSize_Type()
)
upMaxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upMaxBurstSize.setStatus("current")


class _UpPri_Type(Integer32):
    """Custom type upPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_UpPri_Type.__name__ = "Integer32"
_UpPri_Object = MibTableColumn
upPri = _UpPri_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 7, 1, 5),
    _UpPri_Type()
)
upPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upPri.setStatus("current")
_UpMaxTimeDelay_Type = Integer32
_UpMaxTimeDelay_Object = MibTableColumn
upMaxTimeDelay = _UpMaxTimeDelay_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 7, 1, 6),
    _UpMaxTimeDelay_Type()
)
upMaxTimeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upMaxTimeDelay.setStatus("current")
_UpMaxDrift_Type = Integer32
_UpMaxDrift_Object = MibTableColumn
upMaxDrift = _UpMaxDrift_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 7, 1, 7),
    _UpMaxDrift_Type()
)
upMaxDrift.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upMaxDrift.setStatus("current")
_UpFixedPacketSize_Type = Integer32
_UpFixedPacketSize_Object = MibTableColumn
upFixedPacketSize = _UpFixedPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 7, 1, 8),
    _UpFixedPacketSize_Type()
)
upFixedPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upFixedPacketSize.setStatus("current")
_SlaDownAdminObjectTable_Object = MibTable
slaDownAdminObjectTable = _SlaDownAdminObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 8)
)
if mibBuilder.loadTexts:
    slaDownAdminObjectTable.setStatus("current")
_SlaDownAdminObjectEntry_Object = MibTableRow
slaDownAdminObjectEntry = _SlaDownAdminObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 8, 1)
)
slaDownAdminObjectEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    slaDownAdminObjectEntry.setStatus("current")
_DownAssuredBw_Type = Integer32
_DownAssuredBw_Object = MibTableColumn
downAssuredBw = _DownAssuredBw_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 8, 1, 1),
    _DownAssuredBw_Type()
)
downAssuredBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downAssuredBw.setStatus("current")
_DownMaximumBw_Type = Integer32
_DownMaximumBw_Object = MibTableColumn
downMaximumBw = _DownMaximumBw_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 8, 1, 2),
    _DownMaximumBw_Type()
)
downMaximumBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downMaximumBw.setStatus("current")
_DownMaxBurstSize_Type = Integer32
_DownMaxBurstSize_Object = MibTableColumn
downMaxBurstSize = _DownMaxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 8, 1, 3),
    _DownMaxBurstSize_Type()
)
downMaxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downMaxBurstSize.setStatus("current")


class _DownPri_Type(Integer32):
    """Custom type downPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DownPri_Type.__name__ = "Integer32"
_DownPri_Object = MibTableColumn
downPri = _DownPri_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 8, 1, 4),
    _DownPri_Type()
)
downPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downPri.setStatus("current")
_DownMaxTimeDelay_Type = Integer32
_DownMaxTimeDelay_Object = MibTableColumn
downMaxTimeDelay = _DownMaxTimeDelay_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 8, 1, 5),
    _DownMaxTimeDelay_Type()
)
downMaxTimeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downMaxTimeDelay.setStatus("current")
_DownMaxDrift_Type = Integer32
_DownMaxDrift_Object = MibTableColumn
downMaxDrift = _DownMaxDrift_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 8, 1, 6),
    _DownMaxDrift_Type()
)
downMaxDrift.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downMaxDrift.setStatus("current")
_SlaP2pAdminObjectTable_Object = MibTable
slaP2pAdminObjectTable = _SlaP2pAdminObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 9)
)
if mibBuilder.loadTexts:
    slaP2pAdminObjectTable.setStatus("current")
_SlaP2pAdminObjectEntry_Object = MibTableRow
slaP2pAdminObjectEntry = _SlaP2pAdminObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 9, 1)
)
slaP2pAdminObjectEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    slaP2pAdminObjectEntry.setStatus("current")
_P2pAssuredBw_Type = Integer32
_P2pAssuredBw_Object = MibTableColumn
p2pAssuredBw = _P2pAssuredBw_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 9, 1, 1),
    _P2pAssuredBw_Type()
)
p2pAssuredBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p2pAssuredBw.setStatus("current")
_P2pMaximumBw_Type = Integer32
_P2pMaximumBw_Object = MibTableColumn
p2pMaximumBw = _P2pMaximumBw_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 9, 1, 2),
    _P2pMaximumBw_Type()
)
p2pMaximumBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p2pMaximumBw.setStatus("current")
_P2pMaxBurstSize_Type = Integer32
_P2pMaxBurstSize_Object = MibTableColumn
p2pMaxBurstSize = _P2pMaxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 9, 1, 3),
    _P2pMaxBurstSize_Type()
)
p2pMaxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p2pMaxBurstSize.setStatus("current")


class _P2pPri_Type(Integer32):
    """Custom type p2pPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_P2pPri_Type.__name__ = "Integer32"
_P2pPri_Object = MibTableColumn
p2pPri = _P2pPri_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 9, 1, 4),
    _P2pPri_Type()
)
p2pPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p2pPri.setStatus("current")
_P2pMaxTimeDelay_Type = Integer32
_P2pMaxTimeDelay_Object = MibTableColumn
p2pMaxTimeDelay = _P2pMaxTimeDelay_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 9, 1, 5),
    _P2pMaxTimeDelay_Type()
)
p2pMaxTimeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p2pMaxTimeDelay.setStatus("current")
_P2pMaxDrift_Type = Integer32
_P2pMaxDrift_Object = MibTableColumn
p2pMaxDrift = _P2pMaxDrift_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 9, 1, 6),
    _P2pMaxDrift_Type()
)
p2pMaxDrift.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p2pMaxDrift.setStatus("current")
_P2pModeAdminObjectTable_Object = MibTable
p2pModeAdminObjectTable = _P2pModeAdminObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 10)
)
if mibBuilder.loadTexts:
    p2pModeAdminObjectTable.setStatus("current")
_P2pModeAdminObjectEntry_Object = MibTableRow
p2pModeAdminObjectEntry = _P2pModeAdminObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 10, 1)
)
p2pModeAdminObjectEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    p2pModeAdminObjectEntry.setStatus("current")


class _EponP2pMode_Type(Integer32):
    """Custom type eponP2pMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("group", 2))
    )


_EponP2pMode_Type.__name__ = "Integer32"
_EponP2pMode_Object = MibTableColumn
eponP2pMode = _EponP2pMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 10, 1, 1),
    _EponP2pMode_Type()
)
eponP2pMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponP2pMode.setStatus("current")
_P2pGroupAdminObjectTable_Object = MibTable
p2pGroupAdminObjectTable = _P2pGroupAdminObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 12)
)
if mibBuilder.loadTexts:
    p2pGroupAdminObjectTable.setStatus("current")
_P2pGroupAdminObjectEntry_Object = MibTableRow
p2pGroupAdminObjectEntry = _P2pGroupAdminObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 12, 1)
)
p2pGroupAdminObjectEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZXEPON-SERVICE-PRIVATE-MIB", "eponP2pGroupId"),
)
if mibBuilder.loadTexts:
    p2pGroupAdminObjectEntry.setStatus("current")


class _EponP2pGroupId_Type(Integer32):
    """Custom type eponP2pGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2016),
    )


_EponP2pGroupId_Type.__name__ = "Integer32"
_EponP2pGroupId_Object = MibTableColumn
eponP2pGroupId = _EponP2pGroupId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 12, 1, 1),
    _EponP2pGroupId_Type()
)
eponP2pGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponP2pGroupId.setStatus("current")


class _EponP2pGroupName_Type(DisplayString):
    """Custom type eponP2pGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_EponP2pGroupName_Type.__name__ = "DisplayString"
_EponP2pGroupName_Object = MibTableColumn
eponP2pGroupName = _EponP2pGroupName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 12, 1, 2),
    _EponP2pGroupName_Type()
)
eponP2pGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponP2pGroupName.setStatus("current")


class _EponP2pGroupOnus_Type(ZxAnIdList):
    """Custom type eponP2pGroupOnus based on ZxAnIdList"""
    subtypeSpec = ZxAnIdList.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_EponP2pGroupOnus_Type.__name__ = "ZxAnIdList"
_EponP2pGroupOnus_Object = MibTableColumn
eponP2pGroupOnus = _EponP2pGroupOnus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 12, 1, 3),
    _EponP2pGroupOnus_Type()
)
eponP2pGroupOnus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponP2pGroupOnus.setStatus("current")


class _EponP2pGroupAdminStatus_Type(Integer32):
    """Custom type eponP2pGroupAdminStatus based on Integer32"""
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


_EponP2pGroupAdminStatus_Type.__name__ = "Integer32"
_EponP2pGroupAdminStatus_Object = MibTableColumn
eponP2pGroupAdminStatus = _EponP2pGroupAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 12, 1, 4),
    _EponP2pGroupAdminStatus_Type()
)
eponP2pGroupAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponP2pGroupAdminStatus.setStatus("current")


class _EponP2pGroupOpStatus_Type(Integer32):
    """Custom type eponP2pGroupOpStatus based on Integer32"""
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


_EponP2pGroupOpStatus_Type.__name__ = "Integer32"
_EponP2pGroupOpStatus_Object = MibTableColumn
eponP2pGroupOpStatus = _EponP2pGroupOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 12, 1, 5),
    _EponP2pGroupOpStatus_Type()
)
eponP2pGroupOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eponP2pGroupOpStatus.setStatus("current")
_EponP2pGroupRowStatus_Type = RowStatus
_EponP2pGroupRowStatus_Object = MibTableColumn
eponP2pGroupRowStatus = _EponP2pGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 12, 1, 6),
    _EponP2pGroupRowStatus_Type()
)
eponP2pGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponP2pGroupRowStatus.setStatus("current")
_P2pTransmitAdminObjectTable_Object = MibTable
p2pTransmitAdminObjectTable = _P2pTransmitAdminObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 13)
)
if mibBuilder.loadTexts:
    p2pTransmitAdminObjectTable.setStatus("current")
_P2pTransmitAdminObjectEntry_Object = MibTableRow
p2pTransmitAdminObjectEntry = _P2pTransmitAdminObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 13, 1)
)
p2pTransmitAdminObjectEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    p2pTransmitAdminObjectEntry.setStatus("current")
_EponP2pCfgAddressNotFoundEnableFlood_Type = TruthValue
_EponP2pCfgAddressNotFoundEnableFlood_Object = MibTableColumn
eponP2pCfgAddressNotFoundEnableFlood = _EponP2pCfgAddressNotFoundEnableFlood_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 13, 1, 1),
    _EponP2pCfgAddressNotFoundEnableFlood_Type()
)
eponP2pCfgAddressNotFoundEnableFlood.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponP2pCfgAddressNotFoundEnableFlood.setStatus("current")
_EponP2pCfgBroadcastEnableFlood_Type = TruthValue
_EponP2pCfgBroadcastEnableFlood_Object = MibTableColumn
eponP2pCfgBroadcastEnableFlood = _EponP2pCfgBroadcastEnableFlood_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 13, 1, 2),
    _EponP2pCfgBroadcastEnableFlood_Type()
)
eponP2pCfgBroadcastEnableFlood.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponP2pCfgBroadcastEnableFlood.setStatus("current")
_OnuUnPassedAdminAuthInfoTable_Object = MibTable
onuUnPassedAdminAuthInfoTable = _OnuUnPassedAdminAuthInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 14)
)
if mibBuilder.loadTexts:
    onuUnPassedAdminAuthInfoTable.setStatus("current")
_OnuUnPassedAdminAuthInfoEntry_Object = MibTableRow
onuUnPassedAdminAuthInfoEntry = _OnuUnPassedAdminAuthInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 14, 1)
)
onuUnPassedAdminAuthInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZXEPON-SERVICE-PRIVATE-MIB", "onuIndex"),
)
if mibBuilder.loadTexts:
    onuUnPassedAdminAuthInfoEntry.setStatus("current")
_OnuIndex_Type = Integer32
_OnuIndex_Object = MibTableColumn
onuIndex = _OnuIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 14, 1, 1),
    _OnuIndex_Type()
)
onuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    onuIndex.setStatus("current")
_OnuRegisterMacAddress_Type = MacAddress
_OnuRegisterMacAddress_Object = MibTableColumn
onuRegisterMacAddress = _OnuRegisterMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 14, 1, 2),
    _OnuRegisterMacAddress_Type()
)
onuRegisterMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuRegisterMacAddress.setStatus("current")
_OnuReportSn_Type = OctetString
_OnuReportSn_Object = MibTableColumn
onuReportSn = _OnuReportSn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 14, 1, 3),
    _OnuReportSn_Type()
)
onuReportSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuReportSn.setStatus("current")


class _OnuAdminAuthState_Type(Integer32):
    """Custom type onuAdminAuthState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authenticating", 1),
          ("deny", 2))
    )


_OnuAdminAuthState_Type.__name__ = "Integer32"
_OnuAdminAuthState_Object = MibTableColumn
onuAdminAuthState = _OnuAdminAuthState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 14, 1, 4),
    _OnuAdminAuthState_Type()
)
onuAdminAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuAdminAuthState.setStatus("current")


class _OnuDot1xAuthState_Type(Integer32):
    """Custom type onuDot1xAuthState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authenticating", 1),
          ("deny", 2))
    )


_OnuDot1xAuthState_Type.__name__ = "Integer32"
_OnuDot1xAuthState_Object = MibTableColumn
onuDot1xAuthState = _OnuDot1xAuthState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 14, 1, 5),
    _OnuDot1xAuthState_Type()
)
onuDot1xAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuDot1xAuthState.setStatus("current")
_OnuUplineTime_Type = OctetString
_OnuUplineTime_Object = MibTableColumn
onuUplineTime = _OnuUplineTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 14, 1, 6),
    _OnuUplineTime_Type()
)
onuUplineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUplineTime.setStatus("current")
_OnuReportLoid_Type = DisplayString
_OnuReportLoid_Object = MibTableColumn
onuReportLoid = _OnuReportLoid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 14, 1, 7),
    _OnuReportLoid_Type()
)
onuReportLoid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuReportLoid.setStatus("current")
_OnuReportPassword_Type = DisplayString
_OnuReportPassword_Object = MibTableColumn
onuReportPassword = _OnuReportPassword_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 14, 1, 8),
    _OnuReportPassword_Type()
)
onuReportPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuReportPassword.setStatus("current")
_OnuReportType_Type = DisplayString
_OnuReportType_Object = MibTableColumn
onuReportType = _OnuReportType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 14, 1, 9),
    _OnuReportType_Type()
)
onuReportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuReportType.setStatus("current")
_ZxAnEponOnuSwVersion_Type = DisplayString
_ZxAnEponOnuSwVersion_Object = MibTableColumn
zxAnEponOnuSwVersion = _ZxAnEponOnuSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 14, 1, 10),
    _ZxAnEponOnuSwVersion_Type()
)
zxAnEponOnuSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuSwVersion.setStatus("current")
_ZxAnEponOnuHwVersion_Type = DisplayString
_ZxAnEponOnuHwVersion_Object = MibTableColumn
zxAnEponOnuHwVersion = _ZxAnEponOnuHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 14, 1, 11),
    _ZxAnEponOnuHwVersion_Type()
)
zxAnEponOnuHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuHwVersion.setStatus("current")


class _ZxAnEponOnuOamBuildStatus_Type(Integer32):
    """Custom type zxAnEponOnuOamBuildStatus based on Integer32"""
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
        *(("failed", 1),
          ("inProgress", 2),
          ("notSupport", 3),
          ("success", 4))
    )


_ZxAnEponOnuOamBuildStatus_Type.__name__ = "Integer32"
_ZxAnEponOnuOamBuildStatus_Object = MibTableColumn
zxAnEponOnuOamBuildStatus = _ZxAnEponOnuOamBuildStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 14, 1, 12),
    _ZxAnEponOnuOamBuildStatus_Type()
)
zxAnEponOnuOamBuildStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuOamBuildStatus.setStatus("current")
_OnuConfigAdminObjectTable_Object = MibTable
onuConfigAdminObjectTable = _OnuConfigAdminObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 15)
)
if mibBuilder.loadTexts:
    onuConfigAdminObjectTable.setStatus("current")
_OnuConfigAdminObjectEntry_Object = MibTableRow
onuConfigAdminObjectEntry = _OnuConfigAdminObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 15, 1)
)
onuConfigAdminObjectEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    onuConfigAdminObjectEntry.setStatus("current")


class _OnuConfigState_Type(Integer32):
    """Custom type onuConfigState based on Integer32"""
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
        *(("notconfigure", 1),
          ("configuring", 2),
          ("configurationsucceeded", 3),
          ("configurationfailed", 4))
    )


_OnuConfigState_Type.__name__ = "Integer32"
_OnuConfigState_Object = MibTableColumn
onuConfigState = _OnuConfigState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 15, 1, 1),
    _OnuConfigState_Type()
)
onuConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuConfigState.setStatus("current")
_OnuCfgErrObjTables_Type = Integer32
_OnuCfgErrObjTables_Object = MibTableColumn
onuCfgErrObjTables = _OnuCfgErrObjTables_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 15, 1, 2),
    _OnuCfgErrObjTables_Type()
)
onuCfgErrObjTables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuCfgErrObjTables.setStatus("current")
_OltPonAttrObjectTable_Object = MibTable
oltPonAttrObjectTable = _OltPonAttrObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 16)
)
if mibBuilder.loadTexts:
    oltPonAttrObjectTable.setStatus("current")
_OltPonAttrObjectEntry_Object = MibTableRow
oltPonAttrObjectEntry = _OltPonAttrObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 16, 1)
)
oltPonAttrObjectEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    oltPonAttrObjectEntry.setStatus("current")
_OltPonAttrName_Type = DisplayString
_OltPonAttrName_Object = MibTableColumn
oltPonAttrName = _OltPonAttrName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 16, 1, 1),
    _OltPonAttrName_Type()
)
oltPonAttrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oltPonAttrName.setStatus("current")
_OltPonPonAttrDesc_Type = DisplayString
_OltPonPonAttrDesc_Object = MibTableColumn
oltPonPonAttrDesc = _OltPonPonAttrDesc_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 16, 1, 2),
    _OltPonPonAttrDesc_Type()
)
oltPonPonAttrDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oltPonPonAttrDesc.setStatus("current")


class _OltPonAttrReset_Type(Integer32):
    """Custom type oltPonAttrReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("reset", 2))
    )


_OltPonAttrReset_Type.__name__ = "Integer32"
_OltPonAttrReset_Object = MibTableColumn
oltPonAttrReset = _OltPonAttrReset_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 16, 1, 3),
    _OltPonAttrReset_Type()
)
oltPonAttrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oltPonAttrReset.setStatus("current")


class _OltPonAttrResetCounters_Type(Integer32):
    """Custom type oltPonAttrResetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_OltPonAttrResetCounters_Type.__name__ = "Integer32"
_OltPonAttrResetCounters_Object = MibTableColumn
oltPonAttrResetCounters = _OltPonAttrResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 16, 1, 4),
    _OltPonAttrResetCounters_Type()
)
oltPonAttrResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oltPonAttrResetCounters.setStatus("current")


class _OltPonAttrMultiLlidState_Type(Integer32):
    """Custom type oltPonAttrMultiLlidState based on Integer32"""
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


_OltPonAttrMultiLlidState_Type.__name__ = "Integer32"
_OltPonAttrMultiLlidState_Object = MibTableColumn
oltPonAttrMultiLlidState = _OltPonAttrMultiLlidState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 16, 1, 5),
    _OltPonAttrMultiLlidState_Type()
)
oltPonAttrMultiLlidState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oltPonAttrMultiLlidState.setStatus("current")


class _ZxAnEponOnuMaxLlidNumber_Type(Integer32):
    """Custom type zxAnEponOnuMaxLlidNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ZxAnEponOnuMaxLlidNumber_Type.__name__ = "Integer32"
_ZxAnEponOnuMaxLlidNumber_Object = MibTableColumn
zxAnEponOnuMaxLlidNumber = _ZxAnEponOnuMaxLlidNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 16, 1, 6),
    _ZxAnEponOnuMaxLlidNumber_Type()
)
zxAnEponOnuMaxLlidNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuMaxLlidNumber.setStatus("current")
_OltPonAuthenticatedOnuIdList_Type = DisplayString
_OltPonAuthenticatedOnuIdList_Object = MibTableColumn
oltPonAuthenticatedOnuIdList = _OltPonAuthenticatedOnuIdList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 16, 1, 7),
    _OltPonAuthenticatedOnuIdList_Type()
)
oltPonAuthenticatedOnuIdList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltPonAuthenticatedOnuIdList.setStatus("current")


class _OltPonDualRate_Type(Integer32):
    """Custom type oltPonDualRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oneG", 1),
          ("tenGSymmetric", 2),
          ("tenGAsymmetric", 3))
    )


_OltPonDualRate_Type.__name__ = "Integer32"
_OltPonDualRate_Object = MibTableColumn
oltPonDualRate = _OltPonDualRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 16, 1, 8),
    _OltPonDualRate_Type()
)
oltPonDualRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oltPonDualRate.setStatus("current")


class _ZxAnEponIsUseOamCtc2Dot1OrMore_Type(Integer32):
    """Custom type zxAnEponIsUseOamCtc2Dot1OrMore based on Integer32"""
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


_ZxAnEponIsUseOamCtc2Dot1OrMore_Type.__name__ = "Integer32"
_ZxAnEponIsUseOamCtc2Dot1OrMore_Object = MibTableColumn
zxAnEponIsUseOamCtc2Dot1OrMore = _ZxAnEponIsUseOamCtc2Dot1OrMore_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 16, 1, 9),
    _ZxAnEponIsUseOamCtc2Dot1OrMore_Type()
)
zxAnEponIsUseOamCtc2Dot1OrMore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponIsUseOamCtc2Dot1OrMore.setStatus("current")
_OnuUpStreamPriorityObjectTable_Object = MibTable
onuUpStreamPriorityObjectTable = _OnuUpStreamPriorityObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 17)
)
if mibBuilder.loadTexts:
    onuUpStreamPriorityObjectTable.setStatus("current")
_OnuUpStreamPriorityObjectEntry_Object = MibTableRow
onuUpStreamPriorityObjectEntry = _OnuUpStreamPriorityObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 17, 1)
)
onuUpStreamPriorityObjectEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    onuUpStreamPriorityObjectEntry.setStatus("current")
_ZxEponOnuUpstreamPriority_Type = Integer32
_ZxEponOnuUpstreamPriority_Object = MibTableColumn
zxEponOnuUpstreamPriority = _ZxEponOnuUpstreamPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 17, 1, 1),
    _ZxEponOnuUpstreamPriority_Type()
)
zxEponOnuUpstreamPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxEponOnuUpstreamPriority.setStatus("current")
_ZxEponOnuUpstreamDefaultVlan_Type = Integer32
_ZxEponOnuUpstreamDefaultVlan_Object = MibTableColumn
zxEponOnuUpstreamDefaultVlan = _ZxEponOnuUpstreamDefaultVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 17, 1, 2),
    _ZxEponOnuUpstreamDefaultVlan_Type()
)
zxEponOnuUpstreamDefaultVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxEponOnuUpstreamDefaultVlan.setStatus("current")


class _ZxEponOnuUpStreamPriorityRegenerate_Type(Integer32):
    """Custom type zxEponOnuUpStreamPriorityRegenerate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_ZxEponOnuUpStreamPriorityRegenerate_Type.__name__ = "Integer32"
_ZxEponOnuUpStreamPriorityRegenerate_Object = MibTableColumn
zxEponOnuUpStreamPriorityRegenerate = _ZxEponOnuUpStreamPriorityRegenerate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 17, 1, 3),
    _ZxEponOnuUpStreamPriorityRegenerate_Type()
)
zxEponOnuUpStreamPriorityRegenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxEponOnuUpStreamPriorityRegenerate.setStatus("current")
_OnuDownStreamPriorityObjectTable_Object = MibTable
onuDownStreamPriorityObjectTable = _OnuDownStreamPriorityObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 18)
)
if mibBuilder.loadTexts:
    onuDownStreamPriorityObjectTable.setStatus("current")
_OnuDownStreamPriorityObjectEntry_Object = MibTableRow
onuDownStreamPriorityObjectEntry = _OnuDownStreamPriorityObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 18, 1)
)
onuDownStreamPriorityObjectEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    onuDownStreamPriorityObjectEntry.setStatus("current")
_ZxEponOnuDownstreamPriority_Type = Integer32
_ZxEponOnuDownstreamPriority_Object = MibTableColumn
zxEponOnuDownstreamPriority = _ZxEponOnuDownstreamPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 18, 1, 1),
    _ZxEponOnuDownstreamPriority_Type()
)
zxEponOnuDownstreamPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxEponOnuDownstreamPriority.setStatus("current")
_ZxEponOnuDownstreamDefaultVlan_Type = Integer32
_ZxEponOnuDownstreamDefaultVlan_Object = MibTableColumn
zxEponOnuDownstreamDefaultVlan = _ZxEponOnuDownstreamDefaultVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 18, 1, 2),
    _ZxEponOnuDownstreamDefaultVlan_Type()
)
zxEponOnuDownstreamDefaultVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxEponOnuDownstreamDefaultVlan.setStatus("current")


class _ZxEponOnuDownStreamPriorityRegenerate_Type(Integer32):
    """Custom type zxEponOnuDownStreamPriorityRegenerate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_ZxEponOnuDownStreamPriorityRegenerate_Type.__name__ = "Integer32"
_ZxEponOnuDownStreamPriorityRegenerate_Object = MibTableColumn
zxEponOnuDownStreamPriorityRegenerate = _ZxEponOnuDownStreamPriorityRegenerate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 18, 1, 3),
    _ZxEponOnuDownStreamPriorityRegenerate_Type()
)
zxEponOnuDownStreamPriorityRegenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxEponOnuDownStreamPriorityRegenerate.setStatus("current")
_ZxEponOnuDbaPriorityObjectTable_Object = MibTable
zxEponOnuDbaPriorityObjectTable = _ZxEponOnuDbaPriorityObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 19)
)
if mibBuilder.loadTexts:
    zxEponOnuDbaPriorityObjectTable.setStatus("current")
_ZxEponOnuDbaPriorityObjectEntry_Object = MibTableRow
zxEponOnuDbaPriorityObjectEntry = _ZxEponOnuDbaPriorityObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 19, 1)
)
zxEponOnuDbaPriorityObjectEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZXEPON-SERVICE-PRIVATE-MIB", "zxDbaPriority"),
)
if mibBuilder.loadTexts:
    zxEponOnuDbaPriorityObjectEntry.setStatus("current")
_ZxDbaPriority_Type = Integer32
_ZxDbaPriority_Object = MibTableColumn
zxDbaPriority = _ZxDbaPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 19, 1, 1),
    _ZxDbaPriority_Type()
)
zxDbaPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxDbaPriority.setStatus("current")
_ZxCyccleTime_Type = Integer32
_ZxCyccleTime_Object = MibTableColumn
zxCyccleTime = _ZxCyccleTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 19, 1, 2),
    _ZxCyccleTime_Type()
)
zxCyccleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxCyccleTime.setStatus("current")
_ZxEponOnuOpticalPowerMeasureObjectTable_Object = MibTable
zxEponOnuOpticalPowerMeasureObjectTable = _ZxEponOnuOpticalPowerMeasureObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 20)
)
if mibBuilder.loadTexts:
    zxEponOnuOpticalPowerMeasureObjectTable.setStatus("current")
_ZxEponOnuOpticalPowerMeasureObjectEntry_Object = MibTableRow
zxEponOnuOpticalPowerMeasureObjectEntry = _ZxEponOnuOpticalPowerMeasureObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 20, 1)
)
zxEponOnuOpticalPowerMeasureObjectEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxEponOnuOpticalPowerMeasureObjectEntry.setStatus("current")


class _ZxEponOnuTxOpticalPower_Type(DisplayString):
    """Custom type zxEponOnuTxOpticalPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxEponOnuTxOpticalPower_Type.__name__ = "DisplayString"
_ZxEponOnuTxOpticalPower_Object = MibTableColumn
zxEponOnuTxOpticalPower = _ZxEponOnuTxOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 20, 1, 1),
    _ZxEponOnuTxOpticalPower_Type()
)
zxEponOnuTxOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxEponOnuTxOpticalPower.setStatus("current")


class _ZxEponOnuRxOpticalPower_Type(DisplayString):
    """Custom type zxEponOnuRxOpticalPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxEponOnuRxOpticalPower_Type.__name__ = "DisplayString"
_ZxEponOnuRxOpticalPower_Object = MibTableColumn
zxEponOnuRxOpticalPower = _ZxEponOnuRxOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 20, 1, 2),
    _ZxEponOnuRxOpticalPower_Type()
)
zxEponOnuRxOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxEponOnuRxOpticalPower.setStatus("current")
_ZxEponOltOpticalPowerMeasureObjectTable_Object = MibTable
zxEponOltOpticalPowerMeasureObjectTable = _ZxEponOltOpticalPowerMeasureObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 21)
)
if mibBuilder.loadTexts:
    zxEponOltOpticalPowerMeasureObjectTable.setStatus("current")
_ZxEponOltOpticalPowerMeasureObjectEntry_Object = MibTableRow
zxEponOltOpticalPowerMeasureObjectEntry = _ZxEponOltOpticalPowerMeasureObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 21, 1)
)
zxEponOltOpticalPowerMeasureObjectEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxEponOltOpticalPowerMeasureObjectEntry.setStatus("current")


class _ZxEponOltTxOpticalPower_Type(DisplayString):
    """Custom type zxEponOltTxOpticalPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxEponOltTxOpticalPower_Type.__name__ = "DisplayString"
_ZxEponOltTxOpticalPower_Object = MibTableColumn
zxEponOltTxOpticalPower = _ZxEponOltTxOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 21, 1, 1),
    _ZxEponOltTxOpticalPower_Type()
)
zxEponOltTxOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxEponOltTxOpticalPower.setStatus("current")


class _ZxEponOltRxOpticalPower_Type(DisplayString):
    """Custom type zxEponOltRxOpticalPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxEponOltRxOpticalPower_Type.__name__ = "DisplayString"
_ZxEponOltRxOpticalPower_Object = MibTableColumn
zxEponOltRxOpticalPower = _ZxEponOltRxOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 21, 1, 2),
    _ZxEponOltRxOpticalPower_Type()
)
zxEponOltRxOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxEponOltRxOpticalPower.setStatus("current")
_ZxEponHighPriorityFrameObjectTable_Object = MibTable
zxEponHighPriorityFrameObjectTable = _ZxEponHighPriorityFrameObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 22)
)
if mibBuilder.loadTexts:
    zxEponHighPriorityFrameObjectTable.setStatus("current")
_ZxEponHighPriorityFrameObjectEntry_Object = MibTableRow
zxEponHighPriorityFrameObjectEntry = _ZxEponHighPriorityFrameObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 22, 1)
)
zxEponHighPriorityFrameObjectEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxEponHighPriorityFrameObjectEntry.setStatus("current")


class _Priority0_Type(Integer32):
    """Custom type priority0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_Priority0_Type.__name__ = "Integer32"
_Priority0_Object = MibTableColumn
priority0 = _Priority0_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 22, 1, 1),
    _Priority0_Type()
)
priority0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priority0.setStatus("current")


class _Priority1_Type(Integer32):
    """Custom type priority1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_Priority1_Type.__name__ = "Integer32"
_Priority1_Object = MibTableColumn
priority1 = _Priority1_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 22, 1, 2),
    _Priority1_Type()
)
priority1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priority1.setStatus("current")


class _Priority2_Type(Integer32):
    """Custom type priority2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_Priority2_Type.__name__ = "Integer32"
_Priority2_Object = MibTableColumn
priority2 = _Priority2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 22, 1, 3),
    _Priority2_Type()
)
priority2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priority2.setStatus("current")


class _Priority3_Type(Integer32):
    """Custom type priority3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_Priority3_Type.__name__ = "Integer32"
_Priority3_Object = MibTableColumn
priority3 = _Priority3_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 22, 1, 4),
    _Priority3_Type()
)
priority3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priority3.setStatus("current")


class _Priority4_Type(Integer32):
    """Custom type priority4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_Priority4_Type.__name__ = "Integer32"
_Priority4_Object = MibTableColumn
priority4 = _Priority4_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 22, 1, 5),
    _Priority4_Type()
)
priority4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priority4.setStatus("current")


class _Priority5_Type(Integer32):
    """Custom type priority5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_Priority5_Type.__name__ = "Integer32"
_Priority5_Object = MibTableColumn
priority5 = _Priority5_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 22, 1, 6),
    _Priority5_Type()
)
priority5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priority5.setStatus("current")


class _Priority6_Type(Integer32):
    """Custom type priority6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_Priority6_Type.__name__ = "Integer32"
_Priority6_Object = MibTableColumn
priority6 = _Priority6_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 22, 1, 7),
    _Priority6_Type()
)
priority6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priority6.setStatus("current")


class _Priority7_Type(Integer32):
    """Custom type priority7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_Priority7_Type.__name__ = "Integer32"
_Priority7_Object = MibTableColumn
priority7 = _Priority7_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 22, 1, 8),
    _Priority7_Type()
)
priority7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priority7.setStatus("current")
_ZxEponMaxrttObjectTable_Object = MibTable
zxEponMaxrttObjectTable = _ZxEponMaxrttObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 23)
)
if mibBuilder.loadTexts:
    zxEponMaxrttObjectTable.setStatus("current")
_ZxEponMaxrttObjectEntry_Object = MibTableRow
zxEponMaxrttObjectEntry = _ZxEponMaxrttObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 23, 1)
)
zxEponMaxrttObjectEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxEponMaxrttObjectEntry.setStatus("current")
_Maxrtt_Type = Integer32
_Maxrtt_Object = MibTableColumn
maxrtt = _Maxrtt_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 23, 1, 1),
    _Maxrtt_Type()
)
maxrtt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxrtt.setStatus("current")
_ZxEponPriorityQueueMapObjectTable_Object = MibTable
zxEponPriorityQueueMapObjectTable = _ZxEponPriorityQueueMapObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 24)
)
if mibBuilder.loadTexts:
    zxEponPriorityQueueMapObjectTable.setStatus("current")
_ZxEponPriorityQueueMapObjectEntry_Object = MibTableRow
zxEponPriorityQueueMapObjectEntry = _ZxEponPriorityQueueMapObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 24, 1)
)
zxEponPriorityQueueMapObjectEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxEponPriorityQueueMapObjectEntry.setStatus("current")
_Downstreampri0Que_Type = Integer32
_Downstreampri0Que_Object = MibTableColumn
downstreampri0Que = _Downstreampri0Que_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 24, 1, 1),
    _Downstreampri0Que_Type()
)
downstreampri0Que.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downstreampri0Que.setStatus("current")
_Downstreampri1Que_Type = Integer32
_Downstreampri1Que_Object = MibTableColumn
downstreampri1Que = _Downstreampri1Que_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 24, 1, 2),
    _Downstreampri1Que_Type()
)
downstreampri1Que.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downstreampri1Que.setStatus("current")
_Downstreampri2Que_Type = Integer32
_Downstreampri2Que_Object = MibTableColumn
downstreampri2Que = _Downstreampri2Que_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 24, 1, 3),
    _Downstreampri2Que_Type()
)
downstreampri2Que.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downstreampri2Que.setStatus("current")
_Downstreampri3Que_Type = Integer32
_Downstreampri3Que_Object = MibTableColumn
downstreampri3Que = _Downstreampri3Que_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 24, 1, 4),
    _Downstreampri3Que_Type()
)
downstreampri3Que.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downstreampri3Que.setStatus("current")
_Downstreampri4Que_Type = Integer32
_Downstreampri4Que_Object = MibTableColumn
downstreampri4Que = _Downstreampri4Que_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 24, 1, 5),
    _Downstreampri4Que_Type()
)
downstreampri4Que.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downstreampri4Que.setStatus("current")
_Downstreampri5Que_Type = Integer32
_Downstreampri5Que_Object = MibTableColumn
downstreampri5Que = _Downstreampri5Que_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 24, 1, 6),
    _Downstreampri5Que_Type()
)
downstreampri5Que.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downstreampri5Que.setStatus("current")
_Downstreampri6Que_Type = Integer32
_Downstreampri6Que_Object = MibTableColumn
downstreampri6Que = _Downstreampri6Que_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 24, 1, 7),
    _Downstreampri6Que_Type()
)
downstreampri6Que.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downstreampri6Que.setStatus("current")
_Downstreampri7Que_Type = Integer32
_Downstreampri7Que_Object = MibTableColumn
downstreampri7Que = _Downstreampri7Que_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 24, 1, 8),
    _Downstreampri7Que_Type()
)
downstreampri7Que.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downstreampri7Que.setStatus("current")
_Upstreampri0Que_Type = Integer32
_Upstreampri0Que_Object = MibTableColumn
upstreampri0Que = _Upstreampri0Que_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 24, 1, 9),
    _Upstreampri0Que_Type()
)
upstreampri0Que.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upstreampri0Que.setStatus("current")
_Upstreampri1Que_Type = Integer32
_Upstreampri1Que_Object = MibTableColumn
upstreampri1Que = _Upstreampri1Que_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 24, 1, 10),
    _Upstreampri1Que_Type()
)
upstreampri1Que.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upstreampri1Que.setStatus("current")
_Upstreampri2Que_Type = Integer32
_Upstreampri2Que_Object = MibTableColumn
upstreampri2Que = _Upstreampri2Que_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 24, 1, 11),
    _Upstreampri2Que_Type()
)
upstreampri2Que.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upstreampri2Que.setStatus("current")
_Upstreampri3Que_Type = Integer32
_Upstreampri3Que_Object = MibTableColumn
upstreampri3Que = _Upstreampri3Que_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 24, 1, 12),
    _Upstreampri3Que_Type()
)
upstreampri3Que.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upstreampri3Que.setStatus("current")
_Upstreampri4Que_Type = Integer32
_Upstreampri4Que_Object = MibTableColumn
upstreampri4Que = _Upstreampri4Que_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 24, 1, 13),
    _Upstreampri4Que_Type()
)
upstreampri4Que.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upstreampri4Que.setStatus("current")
_Upstreampri5Que_Type = Integer32
_Upstreampri5Que_Object = MibTableColumn
upstreampri5Que = _Upstreampri5Que_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 24, 1, 14),
    _Upstreampri5Que_Type()
)
upstreampri5Que.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upstreampri5Que.setStatus("current")
_Upstreampri6Que_Type = Integer32
_Upstreampri6Que_Object = MibTableColumn
upstreampri6Que = _Upstreampri6Que_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 24, 1, 15),
    _Upstreampri6Que_Type()
)
upstreampri6Que.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upstreampri6Que.setStatus("current")
_Upstreampri7Que_Type = Integer32
_Upstreampri7Que_Object = MibTableColumn
upstreampri7Que = _Upstreampri7Que_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 24, 1, 16),
    _Upstreampri7Que_Type()
)
upstreampri7Que.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upstreampri7Que.setStatus("current")
_ZxEponRxHecObjectTable_Object = MibTable
zxEponRxHecObjectTable = _ZxEponRxHecObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 25)
)
if mibBuilder.loadTexts:
    zxEponRxHecObjectTable.setStatus("current")
_ZxEponRxHecObjectEntry_Object = MibTableRow
zxEponRxHecObjectEntry = _ZxEponRxHecObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 25, 1)
)
zxEponRxHecObjectEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxEponRxHecObjectEntry.setStatus("current")


class _Rxhec_Type(Integer32):
    """Custom type rxhec based on Integer32"""
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
        *(("ahDraft8023", 1),
          ("ahStandard8023", 2),
          ("both", 3),
          ("no", 4))
    )


_Rxhec_Type.__name__ = "Integer32"
_Rxhec_Object = MibTableColumn
rxhec = _Rxhec_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 25, 1, 1),
    _Rxhec_Type()
)
rxhec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rxhec.setStatus("current")
_ZxEponOnuAutoCfgObjectTable_Object = MibTable
zxEponOnuAutoCfgObjectTable = _ZxEponOnuAutoCfgObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 26)
)
if mibBuilder.loadTexts:
    zxEponOnuAutoCfgObjectTable.setStatus("current")
_ZxEponOnuAutoCfgObjectEntry_Object = MibTableRow
zxEponOnuAutoCfgObjectEntry = _ZxEponOnuAutoCfgObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 26, 1)
)
zxEponOnuAutoCfgObjectEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxEponOnuAutoCfgObjectEntry.setStatus("current")


class _OnuBindStatus_Type(Integer32):
    """Custom type onuBindStatus based on Integer32"""
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


_OnuBindStatus_Type.__name__ = "Integer32"
_OnuBindStatus_Object = MibTableColumn
onuBindStatus = _OnuBindStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 26, 1, 1),
    _OnuBindStatus_Type()
)
onuBindStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuBindStatus.setStatus("current")


class _OnuAutoCfgStatus_Type(Integer32):
    """Custom type onuAutoCfgStatus based on Integer32"""
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


_OnuAutoCfgStatus_Type.__name__ = "Integer32"
_OnuAutoCfgStatus_Object = MibTableColumn
onuAutoCfgStatus = _OnuAutoCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 26, 1, 2),
    _OnuAutoCfgStatus_Type()
)
onuAutoCfgStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuAutoCfgStatus.setStatus("current")
_ZxEponIpPoolObjectTable_Object = MibTable
zxEponIpPoolObjectTable = _ZxEponIpPoolObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 27)
)
if mibBuilder.loadTexts:
    zxEponIpPoolObjectTable.setStatus("current")
_ZxEponIpPoolObjectEntry_Object = MibTableRow
zxEponIpPoolObjectEntry = _ZxEponIpPoolObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 27, 1)
)
zxEponIpPoolObjectEntry.setIndexNames(
    (0, "ZXEPON-SERVICE-PRIVATE-MIB", "zxEponIpPoolName"),
)
if mibBuilder.loadTexts:
    zxEponIpPoolObjectEntry.setStatus("current")


class _ZxEponIpPoolName_Type(OctetString):
    """Custom type zxEponIpPoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_ZxEponIpPoolName_Type.__name__ = "OctetString"
_ZxEponIpPoolName_Object = MibTableColumn
zxEponIpPoolName = _ZxEponIpPoolName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 27, 1, 1),
    _ZxEponIpPoolName_Type()
)
zxEponIpPoolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxEponIpPoolName.setStatus("current")
_ZxEponIpPoolIpBegin_Type = IpAddress
_ZxEponIpPoolIpBegin_Object = MibTableColumn
zxEponIpPoolIpBegin = _ZxEponIpPoolIpBegin_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 27, 1, 2),
    _ZxEponIpPoolIpBegin_Type()
)
zxEponIpPoolIpBegin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxEponIpPoolIpBegin.setStatus("current")
_ZxEponIpPoolIpEnd_Type = IpAddress
_ZxEponIpPoolIpEnd_Object = MibTableColumn
zxEponIpPoolIpEnd = _ZxEponIpPoolIpEnd_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 27, 1, 3),
    _ZxEponIpPoolIpEnd_Type()
)
zxEponIpPoolIpEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxEponIpPoolIpEnd.setStatus("current")
_ZxEponIpPoolMask_Type = IpAddress
_ZxEponIpPoolMask_Object = MibTableColumn
zxEponIpPoolMask = _ZxEponIpPoolMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 27, 1, 4),
    _ZxEponIpPoolMask_Type()
)
zxEponIpPoolMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxEponIpPoolMask.setStatus("current")
_ZxEponIpPoolpriority_Type = Integer32
_ZxEponIpPoolpriority_Object = MibTableColumn
zxEponIpPoolpriority = _ZxEponIpPoolpriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 27, 1, 5),
    _ZxEponIpPoolpriority_Type()
)
zxEponIpPoolpriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxEponIpPoolpriority.setStatus("current")
_ZxEponIpPoolVlan_Type = Integer32
_ZxEponIpPoolVlan_Object = MibTableColumn
zxEponIpPoolVlan = _ZxEponIpPoolVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 27, 1, 6),
    _ZxEponIpPoolVlan_Type()
)
zxEponIpPoolVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxEponIpPoolVlan.setStatus("current")
_ZxEponIpPoolNetIp_Type = IpAddress
_ZxEponIpPoolNetIp_Object = MibTableColumn
zxEponIpPoolNetIp = _ZxEponIpPoolNetIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 27, 1, 7),
    _ZxEponIpPoolNetIp_Type()
)
zxEponIpPoolNetIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxEponIpPoolNetIp.setStatus("current")
_ZxEponIpPoolNetMask_Type = IpAddress
_ZxEponIpPoolNetMask_Object = MibTableColumn
zxEponIpPoolNetMask = _ZxEponIpPoolNetMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 27, 1, 8),
    _ZxEponIpPoolNetMask_Type()
)
zxEponIpPoolNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxEponIpPoolNetMask.setStatus("current")
_ZxEponIpPoolGateway_Type = IpAddress
_ZxEponIpPoolGateway_Object = MibTableColumn
zxEponIpPoolGateway = _ZxEponIpPoolGateway_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 27, 1, 9),
    _ZxEponIpPoolGateway_Type()
)
zxEponIpPoolGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxEponIpPoolGateway.setStatus("current")
_ZxEponIpPoolRowStatus_Type = RowStatus
_ZxEponIpPoolRowStatus_Object = MibTableColumn
zxEponIpPoolRowStatus = _ZxEponIpPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 27, 1, 10),
    _ZxEponIpPoolRowStatus_Type()
)
zxEponIpPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxEponIpPoolRowStatus.setStatus("current")
_ZxEponRunIpObjectTable_Object = MibTable
zxEponRunIpObjectTable = _ZxEponRunIpObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 28)
)
if mibBuilder.loadTexts:
    zxEponRunIpObjectTable.setStatus("current")
_ZxEponRunIpObjectEntry_Object = MibTableRow
zxEponRunIpObjectEntry = _ZxEponRunIpObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 28, 1)
)
zxEponRunIpObjectEntry.setIndexNames(
    (0, "ZXEPON-SERVICE-PRIVATE-MIB", "zxEponRunIp"),
)
if mibBuilder.loadTexts:
    zxEponRunIpObjectEntry.setStatus("current")
_ZxEponRunIp_Type = Integer32
_ZxEponRunIp_Object = MibTableColumn
zxEponRunIp = _ZxEponRunIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 28, 1, 1),
    _ZxEponRunIp_Type()
)
zxEponRunIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxEponRunIp.setStatus("current")
_ZxEponRunMask_Type = IpAddress
_ZxEponRunMask_Object = MibTableColumn
zxEponRunMask = _ZxEponRunMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 28, 1, 2),
    _ZxEponRunMask_Type()
)
zxEponRunMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxEponRunMask.setStatus("current")
_ZxEponRunOnuIfIndex_Type = Integer32
_ZxEponRunOnuIfIndex_Object = MibTableColumn
zxEponRunOnuIfIndex = _ZxEponRunOnuIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 28, 1, 3),
    _ZxEponRunOnuIfIndex_Type()
)
zxEponRunOnuIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxEponRunOnuIfIndex.setStatus("current")
_ZxEponRunIpPriority_Type = Integer32
_ZxEponRunIpPriority_Object = MibTableColumn
zxEponRunIpPriority = _ZxEponRunIpPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 28, 1, 4),
    _ZxEponRunIpPriority_Type()
)
zxEponRunIpPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxEponRunIpPriority.setStatus("current")
_ZxEponRunIpVlan_Type = Integer32
_ZxEponRunIpVlan_Object = MibTableColumn
zxEponRunIpVlan = _ZxEponRunIpVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 28, 1, 5),
    _ZxEponRunIpVlan_Type()
)
zxEponRunIpVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxEponRunIpVlan.setStatus("current")
_ZxEponRunIpNetIp_Type = IpAddress
_ZxEponRunIpNetIp_Object = MibTableColumn
zxEponRunIpNetIp = _ZxEponRunIpNetIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 28, 1, 6),
    _ZxEponRunIpNetIp_Type()
)
zxEponRunIpNetIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxEponRunIpNetIp.setStatus("current")
_ZxEponRunIpNetMask_Type = IpAddress
_ZxEponRunIpNetMask_Object = MibTableColumn
zxEponRunIpNetMask = _ZxEponRunIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 28, 1, 7),
    _ZxEponRunIpNetMask_Type()
)
zxEponRunIpNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxEponRunIpNetMask.setStatus("current")
_ZxEponRunIpGateway_Type = IpAddress
_ZxEponRunIpGateway_Object = MibTableColumn
zxEponRunIpGateway = _ZxEponRunIpGateway_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 28, 1, 8),
    _ZxEponRunIpGateway_Type()
)
zxEponRunIpGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxEponRunIpGateway.setStatus("current")


class _ZxEponRunIpStatus_Type(Integer32):
    """Custom type zxEponRunIpStatus based on Integer32"""
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


_ZxEponRunIpStatus_Type.__name__ = "Integer32"
_ZxEponRunIpStatus_Object = MibTableColumn
zxEponRunIpStatus = _ZxEponRunIpStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 28, 1, 9),
    _ZxEponRunIpStatus_Type()
)
zxEponRunIpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxEponRunIpStatus.setStatus("current")


class _ZxEponRunIpCfgMode_Type(Integer32):
    """Custom type zxEponRunIpCfgMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_ZxEponRunIpCfgMode_Type.__name__ = "Integer32"
_ZxEponRunIpCfgMode_Object = MibTableColumn
zxEponRunIpCfgMode = _ZxEponRunIpCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 28, 1, 10),
    _ZxEponRunIpCfgMode_Type()
)
zxEponRunIpCfgMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxEponRunIpCfgMode.setStatus("current")
_ZxEponIpPoolConjPonObjectTable_Object = MibTable
zxEponIpPoolConjPonObjectTable = _ZxEponIpPoolConjPonObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 29)
)
if mibBuilder.loadTexts:
    zxEponIpPoolConjPonObjectTable.setStatus("current")
_ZxEponIpPoolConjPonObjectEntry_Object = MibTableRow
zxEponIpPoolConjPonObjectEntry = _ZxEponIpPoolConjPonObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 29, 1)
)
zxEponIpPoolConjPonObjectEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxEponIpPoolConjPonObjectEntry.setStatus("current")


class _ZxEponIpPoolConjPonName_Type(OctetString):
    """Custom type zxEponIpPoolConjPonName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_ZxEponIpPoolConjPonName_Type.__name__ = "OctetString"
_ZxEponIpPoolConjPonName_Object = MibTableColumn
zxEponIpPoolConjPonName = _ZxEponIpPoolConjPonName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 29, 1, 1),
    _ZxEponIpPoolConjPonName_Type()
)
zxEponIpPoolConjPonName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxEponIpPoolConjPonName.setStatus("current")
_ZxEponIpPoolConjRowStatus_Type = RowStatus
_ZxEponIpPoolConjRowStatus_Object = MibTableColumn
zxEponIpPoolConjRowStatus = _ZxEponIpPoolConjRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 29, 1, 2),
    _ZxEponIpPoolConjRowStatus_Type()
)
zxEponIpPoolConjRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxEponIpPoolConjRowStatus.setStatus("current")
_ZxEponBwProfileAdmin_ObjectIdentity = ObjectIdentity
zxEponBwProfileAdmin = _ZxEponBwProfileAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 30)
)
_ZxEponBwProfileTable_Object = MibTable
zxEponBwProfileTable = _ZxEponBwProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 30, 1)
)
if mibBuilder.loadTexts:
    zxEponBwProfileTable.setStatus("current")
_ZxEponBwProfileEntry_Object = MibTableRow
zxEponBwProfileEntry = _ZxEponBwProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 30, 1, 1)
)
zxEponBwProfileEntry.setIndexNames(
    (0, "ZXEPON-SERVICE-PRIVATE-MIB", "profileIndex"),
)
if mibBuilder.loadTexts:
    zxEponBwProfileEntry.setStatus("current")


class _ProfileIndex_Type(Integer32):
    """Custom type profileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_ProfileIndex_Type.__name__ = "Integer32"
_ProfileIndex_Object = MibTableColumn
profileIndex = _ProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 30, 1, 1, 1),
    _ProfileIndex_Type()
)
profileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    profileIndex.setStatus("current")


class _ProfileName_Type(DisplayString):
    """Custom type profileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ProfileName_Type.__name__ = "DisplayString"
_ProfileName_Object = MibTableColumn
profileName = _ProfileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 30, 1, 1, 2),
    _ProfileName_Type()
)
profileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profileName.setStatus("current")


class _UpBwProfileFixedBw_Type(Integer32):
    """Custom type upBwProfileFixedBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_UpBwProfileFixedBw_Type.__name__ = "Integer32"
_UpBwProfileFixedBw_Object = MibTableColumn
upBwProfileFixedBw = _UpBwProfileFixedBw_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 30, 1, 1, 3),
    _UpBwProfileFixedBw_Type()
)
upBwProfileFixedBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upBwProfileFixedBw.setStatus("current")


class _UpBwProfileAssuredBw_Type(Integer32):
    """Custom type upBwProfileAssuredBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 1000000),
    )


_UpBwProfileAssuredBw_Type.__name__ = "Integer32"
_UpBwProfileAssuredBw_Object = MibTableColumn
upBwProfileAssuredBw = _UpBwProfileAssuredBw_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 30, 1, 1, 4),
    _UpBwProfileAssuredBw_Type()
)
upBwProfileAssuredBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upBwProfileAssuredBw.setStatus("current")


class _UpBwProfileMaximumBw_Type(Integer32):
    """Custom type upBwProfileMaximumBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 1000000),
    )


_UpBwProfileMaximumBw_Type.__name__ = "Integer32"
_UpBwProfileMaximumBw_Object = MibTableColumn
upBwProfileMaximumBw = _UpBwProfileMaximumBw_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 30, 1, 1, 5),
    _UpBwProfileMaximumBw_Type()
)
upBwProfileMaximumBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upBwProfileMaximumBw.setStatus("current")


class _UpBwProfileMaxBurstSize_Type(Integer32):
    """Custom type upBwProfileMaxBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_UpBwProfileMaxBurstSize_Type.__name__ = "Integer32"
_UpBwProfileMaxBurstSize_Object = MibTableColumn
upBwProfileMaxBurstSize = _UpBwProfileMaxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 30, 1, 1, 6),
    _UpBwProfileMaxBurstSize_Type()
)
upBwProfileMaxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upBwProfileMaxBurstSize.setStatus("current")


class _UpBwProfilePri_Type(Integer32):
    """Custom type upBwProfilePri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_UpBwProfilePri_Type.__name__ = "Integer32"
_UpBwProfilePri_Object = MibTableColumn
upBwProfilePri = _UpBwProfilePri_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 30, 1, 1, 7),
    _UpBwProfilePri_Type()
)
upBwProfilePri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upBwProfilePri.setStatus("current")


class _UpBwProfileFixedPacketSize_Type(Integer32):
    """Custom type upBwProfileFixedPacketSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1582),
    )


_UpBwProfileFixedPacketSize_Type.__name__ = "Integer32"
_UpBwProfileFixedPacketSize_Object = MibTableColumn
upBwProfileFixedPacketSize = _UpBwProfileFixedPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 30, 1, 1, 8),
    _UpBwProfileFixedPacketSize_Type()
)
upBwProfileFixedPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upBwProfileFixedPacketSize.setStatus("current")


class _DownBwProfileMaximumBw_Type(Integer32):
    """Custom type downBwProfileMaximumBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 999994),
    )


_DownBwProfileMaximumBw_Type.__name__ = "Integer32"
_DownBwProfileMaximumBw_Object = MibTableColumn
downBwProfileMaximumBw = _DownBwProfileMaximumBw_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 30, 1, 1, 9),
    _DownBwProfileMaximumBw_Type()
)
downBwProfileMaximumBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downBwProfileMaximumBw.setStatus("current")


class _DownBwProfileMaxBurstSize_Type(Integer32):
    """Custom type downBwProfileMaxBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_DownBwProfileMaxBurstSize_Type.__name__ = "Integer32"
_DownBwProfileMaxBurstSize_Object = MibTableColumn
downBwProfileMaxBurstSize = _DownBwProfileMaxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 30, 1, 1, 10),
    _DownBwProfileMaxBurstSize_Type()
)
downBwProfileMaxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downBwProfileMaxBurstSize.setStatus("current")
_BwProfileRowStatus_Type = RowStatus
_BwProfileRowStatus_Object = MibTableColumn
bwProfileRowStatus = _BwProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 30, 1, 1, 11),
    _BwProfileRowStatus_Type()
)
bwProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwProfileRowStatus.setStatus("current")
_BwProfileNextIndex_Type = Integer32
_BwProfileNextIndex_Object = MibScalar
bwProfileNextIndex = _BwProfileNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 30, 2),
    _BwProfileNextIndex_Type()
)
bwProfileNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwProfileNextIndex.setStatus("current")
_ZxEponOnuBwCfgTable_Object = MibTable
zxEponOnuBwCfgTable = _ZxEponOnuBwCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 32)
)
if mibBuilder.loadTexts:
    zxEponOnuBwCfgTable.setStatus("current")
_ZxEponOnuBwCfgEntry_Object = MibTableRow
zxEponOnuBwCfgEntry = _ZxEponOnuBwCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 32, 1)
)
zxEponOnuBwCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxEponOnuBwCfgEntry.setStatus("current")


class _OnuCfgBwProfileIndex_Type(Integer32):
    """Custom type onuCfgBwProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_OnuCfgBwProfileIndex_Type.__name__ = "Integer32"
_OnuCfgBwProfileIndex_Object = MibTableColumn
onuCfgBwProfileIndex = _OnuCfgBwProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 32, 1, 1),
    _OnuCfgBwProfileIndex_Type()
)
onuCfgBwProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuCfgBwProfileIndex.setStatus("current")
_ZxEponOnuIpCfgTable_Object = MibTable
zxEponOnuIpCfgTable = _ZxEponOnuIpCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 33)
)
if mibBuilder.loadTexts:
    zxEponOnuIpCfgTable.setStatus("current")
_ZxEponOnuIpCfgEntry_Object = MibTableRow
zxEponOnuIpCfgEntry = _ZxEponOnuIpCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 33, 1)
)
zxEponOnuIpCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxEponOnuIpCfgEntry.setStatus("current")
_ZxEponOnuIpCfgIpAddr_Type = IpAddress
_ZxEponOnuIpCfgIpAddr_Object = MibTableColumn
zxEponOnuIpCfgIpAddr = _ZxEponOnuIpCfgIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 33, 1, 1),
    _ZxEponOnuIpCfgIpAddr_Type()
)
zxEponOnuIpCfgIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxEponOnuIpCfgIpAddr.setStatus("current")


class _ZxEponOnuIpCfgOperator_Type(Integer32):
    """Custom type zxEponOnuIpCfgOperator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("assign", 1),
          ("release", 2))
    )


_ZxEponOnuIpCfgOperator_Type.__name__ = "Integer32"
_ZxEponOnuIpCfgOperator_Object = MibTableColumn
zxEponOnuIpCfgOperator = _ZxEponOnuIpCfgOperator_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 33, 1, 2),
    _ZxEponOnuIpCfgOperator_Type()
)
zxEponOnuIpCfgOperator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxEponOnuIpCfgOperator.setStatus("current")
_ZxEponOnuAutoConfigTable_Object = MibTable
zxEponOnuAutoConfigTable = _ZxEponOnuAutoConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 34)
)
if mibBuilder.loadTexts:
    zxEponOnuAutoConfigTable.setStatus("current")
_ZxEponOnuAutoConfigEntry_Object = MibTableRow
zxEponOnuAutoConfigEntry = _ZxEponOnuAutoConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 34, 1)
)
zxEponOnuAutoConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxEponOnuAutoConfigEntry.setStatus("current")


class _ZxEponOnuAutoConfigStatus_Type(Integer32):
    """Custom type zxEponOnuAutoConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ZxEponOnuAutoConfigStatus_Type.__name__ = "Integer32"
_ZxEponOnuAutoConfigStatus_Object = MibTableColumn
zxEponOnuAutoConfigStatus = _ZxEponOnuAutoConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 34, 1, 1),
    _ZxEponOnuAutoConfigStatus_Type()
)
zxEponOnuAutoConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxEponOnuAutoConfigStatus.setStatus("current")


class _ZxEponOnuVoipAutoConfigStatus_Type(Integer32):
    """Custom type zxEponOnuVoipAutoConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ZxEponOnuVoipAutoConfigStatus_Type.__name__ = "Integer32"
_ZxEponOnuVoipAutoConfigStatus_Object = MibTableColumn
zxEponOnuVoipAutoConfigStatus = _ZxEponOnuVoipAutoConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 34, 1, 2),
    _ZxEponOnuVoipAutoConfigStatus_Type()
)
zxEponOnuVoipAutoConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxEponOnuVoipAutoConfigStatus.setStatus("current")
_ZxEponRunningCtrl_ObjectIdentity = ObjectIdentity
zxEponRunningCtrl = _ZxEponRunningCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 35)
)


class _ZxEponRevision_Type(Bits):
    """Custom type zxEponRevision based on Bits"""
    namedValues = NamedValues(
        ("ctc21", 1)
    )

_ZxEponRevision_Type.__name__ = "Bits"
_ZxEponRevision_Object = MibScalar
zxEponRevision = _ZxEponRevision_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 35, 1),
    _ZxEponRevision_Type()
)
zxEponRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxEponRevision.setStatus("current")
_OnuCustomObjectTable_Object = MibTable
onuCustomObjectTable = _OnuCustomObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 36)
)
if mibBuilder.loadTexts:
    onuCustomObjectTable.setStatus("current")
_OnuCustomObjectEntry_Object = MibTableRow
onuCustomObjectEntry = _OnuCustomObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 36, 1)
)
onuCustomObjectEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    onuCustomObjectEntry.setStatus("current")


class _OnuOnlineForwardAction_Type(Integer32):
    """Custom type onuOnlineForwardAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OnuOnlineForwardAction_Type.__name__ = "Integer32"
_OnuOnlineForwardAction_Object = MibTableColumn
onuOnlineForwardAction = _OnuOnlineForwardAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 36, 1, 1),
    _OnuOnlineForwardAction_Type()
)
onuOnlineForwardAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuOnlineForwardAction.setStatus("current")
_ZxAnEponOnuVportMgmtTable_Object = MibTable
zxAnEponOnuVportMgmtTable = _ZxAnEponOnuVportMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 37)
)
if mibBuilder.loadTexts:
    zxAnEponOnuVportMgmtTable.setStatus("current")
_ZxAnEponOnuVportMgmtTableEntry_Object = MibTableRow
zxAnEponOnuVportMgmtTableEntry = _ZxAnEponOnuVportMgmtTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 37, 1)
)
zxAnEponOnuVportMgmtTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuVportMgmtTableEntry.setStatus("current")
_ZxAnEponOnuVportMacAddress_Type = MacAddress
_ZxAnEponOnuVportMacAddress_Object = MibTableColumn
zxAnEponOnuVportMacAddress = _ZxAnEponOnuVportMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 37, 1, 1),
    _ZxAnEponOnuVportMacAddress_Type()
)
zxAnEponOnuVportMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVportMacAddress.setStatus("current")


class _ZxAnEponOnuVportCurrAuthState_Type(Integer32):
    """Custom type zxAnEponOnuVportCurrAuthState based on Integer32"""
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
        *(("init", 1),
          ("authenticating", 2),
          ("pass", 3),
          ("deny", 4))
    )


_ZxAnEponOnuVportCurrAuthState_Type.__name__ = "Integer32"
_ZxAnEponOnuVportCurrAuthState_Object = MibTableColumn
zxAnEponOnuVportCurrAuthState = _ZxAnEponOnuVportCurrAuthState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 37, 1, 2),
    _ZxAnEponOnuVportCurrAuthState_Type()
)
zxAnEponOnuVportCurrAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuVportCurrAuthState.setStatus("current")
_ZxEponQueueBufferObjectTable_Object = MibTable
zxEponQueueBufferObjectTable = _ZxEponQueueBufferObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 38)
)
if mibBuilder.loadTexts:
    zxEponQueueBufferObjectTable.setStatus("current")
_ZxEponQueueBufferObjectEntry_Object = MibTableRow
zxEponQueueBufferObjectEntry = _ZxEponQueueBufferObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 38, 1)
)
zxEponQueueBufferObjectEntry.setIndexNames(
    (0, "ZXEPON-SERVICE-PRIVATE-MIB", "zxEponQueueRackNo"),
    (0, "ZXEPON-SERVICE-PRIVATE-MIB", "zxEponQueueShelfNo"),
    (0, "ZXEPON-SERVICE-PRIVATE-MIB", "zxEponQueueSlotNo"),
)
if mibBuilder.loadTexts:
    zxEponQueueBufferObjectEntry.setStatus("current")
_ZxEponQueueRackNo_Type = Integer32
_ZxEponQueueRackNo_Object = MibTableColumn
zxEponQueueRackNo = _ZxEponQueueRackNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 38, 1, 1),
    _ZxEponQueueRackNo_Type()
)
zxEponQueueRackNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxEponQueueRackNo.setStatus("current")
_ZxEponQueueShelfNo_Type = Integer32
_ZxEponQueueShelfNo_Object = MibTableColumn
zxEponQueueShelfNo = _ZxEponQueueShelfNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 38, 1, 2),
    _ZxEponQueueShelfNo_Type()
)
zxEponQueueShelfNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxEponQueueShelfNo.setStatus("current")
_ZxEponQueueSlotNo_Type = Integer32
_ZxEponQueueSlotNo_Object = MibTableColumn
zxEponQueueSlotNo = _ZxEponQueueSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 38, 1, 3),
    _ZxEponQueueSlotNo_Type()
)
zxEponQueueSlotNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxEponQueueSlotNo.setStatus("current")


class _ZxEponQueueBufferSize_Type(Integer32):
    """Custom type zxEponQueueBufferSize based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1020),
    )


_ZxEponQueueBufferSize_Type.__name__ = "Integer32"
_ZxEponQueueBufferSize_Object = MibTableColumn
zxEponQueueBufferSize = _ZxEponQueueBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 7, 38, 1, 4),
    _ZxEponQueueBufferSize_Type()
)
zxEponQueueBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxEponQueueBufferSize.setStatus("current")
if mibBuilder.loadTexts:
    zxEponQueueBufferSize.setUnits("kbytes")
_ZxEponMgmtIndex_ObjectIdentity = ObjectIdentity
zxEponMgmtIndex = _ZxEponMgmtIndex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 8)
)
_ZxEponIfIndexTable_Object = MibTable
zxEponIfIndexTable = _ZxEponIfIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 8, 1)
)
if mibBuilder.loadTexts:
    zxEponIfIndexTable.setStatus("current")
_ZxEponIfIndexEntry_Object = MibTableRow
zxEponIfIndexEntry = _ZxEponIfIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 8, 1, 1)
)
zxEponIfIndexEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxEponIfIndexEntry.setStatus("current")
_ZxEponifIndex_Type = Integer32
_ZxEponifIndex_Object = MibTableColumn
zxEponifIndex = _ZxEponifIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 8, 1, 1, 1),
    _ZxEponifIndex_Type()
)
zxEponifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxEponifIndex.setStatus("current")
_ZxEponEntryStatus_Type = RowStatus
_ZxEponEntryStatus_Object = MibTableColumn
zxEponEntryStatus = _ZxEponEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 8, 1, 1, 2),
    _ZxEponEntryStatus_Type()
)
zxEponEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxEponEntryStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXEPON-SERVICE-PRIVATE-MIB",
    **{"privateObjects": privateObjects,
       "sysAttrObjectTable": sysAttrObjectTable,
       "sysAttrObjectEntry": sysAttrObjectEntry,
       "sysOnuAdminAuthMode": sysOnuAdminAuthMode,
       "sysAttrAutoAuthEnable": sysAttrAutoAuthEnable,
       "macHwAuthOnuState": macHwAuthOnuState,
       "zxAnEponOnuSilenceEnable": zxAnEponOnuSilenceEnable,
       "oltLinkAdminTestObjectTable": oltLinkAdminTestObjectTable,
       "oltLinkAdminTestObjectEntry": oltLinkAdminTestObjectEntry,
       "testControlMode": testControlMode,
       "testResult": testResult,
       "oltLoopbackObjectTable": oltLoopbackObjectTable,
       "oltLoopbackObjectEntry": oltLoopbackObjectEntry,
       "loopbackStation": loopbackStation,
       "loopbackDirection": loopbackDirection,
       "loopbackAdministration": loopbackAdministration,
       "loopbackState": loopbackState,
       "onuAdminObjectTable": onuAdminObjectTable,
       "onuAdminObjectEntry": onuAdminObjectEntry,
       "onuDescript": onuDescript,
       "onuSplitterSn": onuSplitterSn,
       "onuOpticalLineSn": onuOpticalLineSn,
       "onuUserInfo": onuUserInfo,
       "onuType": onuType,
       "onuAdminState": onuAdminState,
       "onuAuthMACAddress": onuAuthMACAddress,
       "onuRegisterMACAddress": onuRegisterMACAddress,
       "onuAuthMACSn": onuAuthMACSn,
       "onuRegisterSn": onuRegisterSn,
       "onuCurrentRegState": onuCurrentRegState,
       "onuRegisterTime": onuRegisterTime,
       "onuCurrAdminAuthState": onuCurrAdminAuthState,
       "onuLatelyPassAdminAuthTime": onuLatelyPassAdminAuthTime,
       "onuCurrDot1xAuthState": onuCurrDot1xAuthState,
       "onuLatelyPassDot1xAuthTime": onuLatelyPassDot1xAuthTime,
       "onuMgmtOnlineStatus": onuMgmtOnlineStatus,
       "onuActiveStatus": onuActiveStatus,
       "onuMgmtEntryStatus": onuMgmtEntryStatus,
       "onuMgmtIpCfgMode": onuMgmtIpCfgMode,
       "onuAuthLoid": onuAuthLoid,
       "onuAuthPassword": onuAuthPassword,
       "onuRegisterLoid": onuRegisterLoid,
       "onuRegisterPassword": onuRegisterPassword,
       "zxAnEponOnuCreateTime": zxAnEponOnuCreateTime,
       "zxAnEponOnuLastOfflineTime": zxAnEponOnuLastOfflineTime,
       "oltEncryAdminObjectTable": oltEncryAdminObjectTable,
       "oltEncryAdminObjectEntry": oltEncryAdminObjectEntry,
       "encryptArithmetic": encryptArithmetic,
       "keyUpdateTime": keyUpdateTime,
       "keyUpdateTimeout": keyUpdateTimeout,
       "startEncryptThreshold": startEncryptThreshold,
       "lineEncryAdminObjectTable": lineEncryAdminObjectTable,
       "lineEncryAdminObjectEntry": lineEncryAdminObjectEntry,
       "encryptMode": encryptMode,
       "encrypeState": encrypeState,
       "slaUpAdminObjectTable": slaUpAdminObjectTable,
       "slaUpAdminObjectEntry": slaUpAdminObjectEntry,
       "upFixedBw": upFixedBw,
       "upAssuredBw": upAssuredBw,
       "upMaximumBw": upMaximumBw,
       "upMaxBurstSize": upMaxBurstSize,
       "upPri": upPri,
       "upMaxTimeDelay": upMaxTimeDelay,
       "upMaxDrift": upMaxDrift,
       "upFixedPacketSize": upFixedPacketSize,
       "slaDownAdminObjectTable": slaDownAdminObjectTable,
       "slaDownAdminObjectEntry": slaDownAdminObjectEntry,
       "downAssuredBw": downAssuredBw,
       "downMaximumBw": downMaximumBw,
       "downMaxBurstSize": downMaxBurstSize,
       "downPri": downPri,
       "downMaxTimeDelay": downMaxTimeDelay,
       "downMaxDrift": downMaxDrift,
       "slaP2pAdminObjectTable": slaP2pAdminObjectTable,
       "slaP2pAdminObjectEntry": slaP2pAdminObjectEntry,
       "p2pAssuredBw": p2pAssuredBw,
       "p2pMaximumBw": p2pMaximumBw,
       "p2pMaxBurstSize": p2pMaxBurstSize,
       "p2pPri": p2pPri,
       "p2pMaxTimeDelay": p2pMaxTimeDelay,
       "p2pMaxDrift": p2pMaxDrift,
       "p2pModeAdminObjectTable": p2pModeAdminObjectTable,
       "p2pModeAdminObjectEntry": p2pModeAdminObjectEntry,
       "eponP2pMode": eponP2pMode,
       "p2pGroupAdminObjectTable": p2pGroupAdminObjectTable,
       "p2pGroupAdminObjectEntry": p2pGroupAdminObjectEntry,
       "eponP2pGroupId": eponP2pGroupId,
       "eponP2pGroupName": eponP2pGroupName,
       "eponP2pGroupOnus": eponP2pGroupOnus,
       "eponP2pGroupAdminStatus": eponP2pGroupAdminStatus,
       "eponP2pGroupOpStatus": eponP2pGroupOpStatus,
       "eponP2pGroupRowStatus": eponP2pGroupRowStatus,
       "p2pTransmitAdminObjectTable": p2pTransmitAdminObjectTable,
       "p2pTransmitAdminObjectEntry": p2pTransmitAdminObjectEntry,
       "eponP2pCfgAddressNotFoundEnableFlood": eponP2pCfgAddressNotFoundEnableFlood,
       "eponP2pCfgBroadcastEnableFlood": eponP2pCfgBroadcastEnableFlood,
       "onuUnPassedAdminAuthInfoTable": onuUnPassedAdminAuthInfoTable,
       "onuUnPassedAdminAuthInfoEntry": onuUnPassedAdminAuthInfoEntry,
       "onuIndex": onuIndex,
       "onuRegisterMacAddress": onuRegisterMacAddress,
       "onuReportSn": onuReportSn,
       "onuAdminAuthState": onuAdminAuthState,
       "onuDot1xAuthState": onuDot1xAuthState,
       "onuUplineTime": onuUplineTime,
       "onuReportLoid": onuReportLoid,
       "onuReportPassword": onuReportPassword,
       "onuReportType": onuReportType,
       "zxAnEponOnuSwVersion": zxAnEponOnuSwVersion,
       "zxAnEponOnuHwVersion": zxAnEponOnuHwVersion,
       "zxAnEponOnuOamBuildStatus": zxAnEponOnuOamBuildStatus,
       "onuConfigAdminObjectTable": onuConfigAdminObjectTable,
       "onuConfigAdminObjectEntry": onuConfigAdminObjectEntry,
       "onuConfigState": onuConfigState,
       "onuCfgErrObjTables": onuCfgErrObjTables,
       "oltPonAttrObjectTable": oltPonAttrObjectTable,
       "oltPonAttrObjectEntry": oltPonAttrObjectEntry,
       "oltPonAttrName": oltPonAttrName,
       "oltPonPonAttrDesc": oltPonPonAttrDesc,
       "oltPonAttrReset": oltPonAttrReset,
       "oltPonAttrResetCounters": oltPonAttrResetCounters,
       "oltPonAttrMultiLlidState": oltPonAttrMultiLlidState,
       "zxAnEponOnuMaxLlidNumber": zxAnEponOnuMaxLlidNumber,
       "oltPonAuthenticatedOnuIdList": oltPonAuthenticatedOnuIdList,
       "oltPonDualRate": oltPonDualRate,
       "zxAnEponIsUseOamCtc2Dot1OrMore": zxAnEponIsUseOamCtc2Dot1OrMore,
       "onuUpStreamPriorityObjectTable": onuUpStreamPriorityObjectTable,
       "onuUpStreamPriorityObjectEntry": onuUpStreamPriorityObjectEntry,
       "zxEponOnuUpstreamPriority": zxEponOnuUpstreamPriority,
       "zxEponOnuUpstreamDefaultVlan": zxEponOnuUpstreamDefaultVlan,
       "zxEponOnuUpStreamPriorityRegenerate": zxEponOnuUpStreamPriorityRegenerate,
       "onuDownStreamPriorityObjectTable": onuDownStreamPriorityObjectTable,
       "onuDownStreamPriorityObjectEntry": onuDownStreamPriorityObjectEntry,
       "zxEponOnuDownstreamPriority": zxEponOnuDownstreamPriority,
       "zxEponOnuDownstreamDefaultVlan": zxEponOnuDownstreamDefaultVlan,
       "zxEponOnuDownStreamPriorityRegenerate": zxEponOnuDownStreamPriorityRegenerate,
       "zxEponOnuDbaPriorityObjectTable": zxEponOnuDbaPriorityObjectTable,
       "zxEponOnuDbaPriorityObjectEntry": zxEponOnuDbaPriorityObjectEntry,
       "zxDbaPriority": zxDbaPriority,
       "zxCyccleTime": zxCyccleTime,
       "zxEponOnuOpticalPowerMeasureObjectTable": zxEponOnuOpticalPowerMeasureObjectTable,
       "zxEponOnuOpticalPowerMeasureObjectEntry": zxEponOnuOpticalPowerMeasureObjectEntry,
       "zxEponOnuTxOpticalPower": zxEponOnuTxOpticalPower,
       "zxEponOnuRxOpticalPower": zxEponOnuRxOpticalPower,
       "zxEponOltOpticalPowerMeasureObjectTable": zxEponOltOpticalPowerMeasureObjectTable,
       "zxEponOltOpticalPowerMeasureObjectEntry": zxEponOltOpticalPowerMeasureObjectEntry,
       "zxEponOltTxOpticalPower": zxEponOltTxOpticalPower,
       "zxEponOltRxOpticalPower": zxEponOltRxOpticalPower,
       "zxEponHighPriorityFrameObjectTable": zxEponHighPriorityFrameObjectTable,
       "zxEponHighPriorityFrameObjectEntry": zxEponHighPriorityFrameObjectEntry,
       "priority0": priority0,
       "priority1": priority1,
       "priority2": priority2,
       "priority3": priority3,
       "priority4": priority4,
       "priority5": priority5,
       "priority6": priority6,
       "priority7": priority7,
       "zxEponMaxrttObjectTable": zxEponMaxrttObjectTable,
       "zxEponMaxrttObjectEntry": zxEponMaxrttObjectEntry,
       "maxrtt": maxrtt,
       "zxEponPriorityQueueMapObjectTable": zxEponPriorityQueueMapObjectTable,
       "zxEponPriorityQueueMapObjectEntry": zxEponPriorityQueueMapObjectEntry,
       "downstreampri0Que": downstreampri0Que,
       "downstreampri1Que": downstreampri1Que,
       "downstreampri2Que": downstreampri2Que,
       "downstreampri3Que": downstreampri3Que,
       "downstreampri4Que": downstreampri4Que,
       "downstreampri5Que": downstreampri5Que,
       "downstreampri6Que": downstreampri6Que,
       "downstreampri7Que": downstreampri7Que,
       "upstreampri0Que": upstreampri0Que,
       "upstreampri1Que": upstreampri1Que,
       "upstreampri2Que": upstreampri2Que,
       "upstreampri3Que": upstreampri3Que,
       "upstreampri4Que": upstreampri4Que,
       "upstreampri5Que": upstreampri5Que,
       "upstreampri6Que": upstreampri6Que,
       "upstreampri7Que": upstreampri7Que,
       "zxEponRxHecObjectTable": zxEponRxHecObjectTable,
       "zxEponRxHecObjectEntry": zxEponRxHecObjectEntry,
       "rxhec": rxhec,
       "zxEponOnuAutoCfgObjectTable": zxEponOnuAutoCfgObjectTable,
       "zxEponOnuAutoCfgObjectEntry": zxEponOnuAutoCfgObjectEntry,
       "onuBindStatus": onuBindStatus,
       "onuAutoCfgStatus": onuAutoCfgStatus,
       "zxEponIpPoolObjectTable": zxEponIpPoolObjectTable,
       "zxEponIpPoolObjectEntry": zxEponIpPoolObjectEntry,
       "zxEponIpPoolName": zxEponIpPoolName,
       "zxEponIpPoolIpBegin": zxEponIpPoolIpBegin,
       "zxEponIpPoolIpEnd": zxEponIpPoolIpEnd,
       "zxEponIpPoolMask": zxEponIpPoolMask,
       "zxEponIpPoolpriority": zxEponIpPoolpriority,
       "zxEponIpPoolVlan": zxEponIpPoolVlan,
       "zxEponIpPoolNetIp": zxEponIpPoolNetIp,
       "zxEponIpPoolNetMask": zxEponIpPoolNetMask,
       "zxEponIpPoolGateway": zxEponIpPoolGateway,
       "zxEponIpPoolRowStatus": zxEponIpPoolRowStatus,
       "zxEponRunIpObjectTable": zxEponRunIpObjectTable,
       "zxEponRunIpObjectEntry": zxEponRunIpObjectEntry,
       "zxEponRunIp": zxEponRunIp,
       "zxEponRunMask": zxEponRunMask,
       "zxEponRunOnuIfIndex": zxEponRunOnuIfIndex,
       "zxEponRunIpPriority": zxEponRunIpPriority,
       "zxEponRunIpVlan": zxEponRunIpVlan,
       "zxEponRunIpNetIp": zxEponRunIpNetIp,
       "zxEponRunIpNetMask": zxEponRunIpNetMask,
       "zxEponRunIpGateway": zxEponRunIpGateway,
       "zxEponRunIpStatus": zxEponRunIpStatus,
       "zxEponRunIpCfgMode": zxEponRunIpCfgMode,
       "zxEponIpPoolConjPonObjectTable": zxEponIpPoolConjPonObjectTable,
       "zxEponIpPoolConjPonObjectEntry": zxEponIpPoolConjPonObjectEntry,
       "zxEponIpPoolConjPonName": zxEponIpPoolConjPonName,
       "zxEponIpPoolConjRowStatus": zxEponIpPoolConjRowStatus,
       "zxEponBwProfileAdmin": zxEponBwProfileAdmin,
       "zxEponBwProfileTable": zxEponBwProfileTable,
       "zxEponBwProfileEntry": zxEponBwProfileEntry,
       "profileIndex": profileIndex,
       "profileName": profileName,
       "upBwProfileFixedBw": upBwProfileFixedBw,
       "upBwProfileAssuredBw": upBwProfileAssuredBw,
       "upBwProfileMaximumBw": upBwProfileMaximumBw,
       "upBwProfileMaxBurstSize": upBwProfileMaxBurstSize,
       "upBwProfilePri": upBwProfilePri,
       "upBwProfileFixedPacketSize": upBwProfileFixedPacketSize,
       "downBwProfileMaximumBw": downBwProfileMaximumBw,
       "downBwProfileMaxBurstSize": downBwProfileMaxBurstSize,
       "bwProfileRowStatus": bwProfileRowStatus,
       "bwProfileNextIndex": bwProfileNextIndex,
       "zxEponOnuBwCfgTable": zxEponOnuBwCfgTable,
       "zxEponOnuBwCfgEntry": zxEponOnuBwCfgEntry,
       "onuCfgBwProfileIndex": onuCfgBwProfileIndex,
       "zxEponOnuIpCfgTable": zxEponOnuIpCfgTable,
       "zxEponOnuIpCfgEntry": zxEponOnuIpCfgEntry,
       "zxEponOnuIpCfgIpAddr": zxEponOnuIpCfgIpAddr,
       "zxEponOnuIpCfgOperator": zxEponOnuIpCfgOperator,
       "zxEponOnuAutoConfigTable": zxEponOnuAutoConfigTable,
       "zxEponOnuAutoConfigEntry": zxEponOnuAutoConfigEntry,
       "zxEponOnuAutoConfigStatus": zxEponOnuAutoConfigStatus,
       "zxEponOnuVoipAutoConfigStatus": zxEponOnuVoipAutoConfigStatus,
       "zxEponRunningCtrl": zxEponRunningCtrl,
       "zxEponRevision": zxEponRevision,
       "onuCustomObjectTable": onuCustomObjectTable,
       "onuCustomObjectEntry": onuCustomObjectEntry,
       "onuOnlineForwardAction": onuOnlineForwardAction,
       "zxAnEponOnuVportMgmtTable": zxAnEponOnuVportMgmtTable,
       "zxAnEponOnuVportMgmtTableEntry": zxAnEponOnuVportMgmtTableEntry,
       "zxAnEponOnuVportMacAddress": zxAnEponOnuVportMacAddress,
       "zxAnEponOnuVportCurrAuthState": zxAnEponOnuVportCurrAuthState,
       "zxEponQueueBufferObjectTable": zxEponQueueBufferObjectTable,
       "zxEponQueueBufferObjectEntry": zxEponQueueBufferObjectEntry,
       "zxEponQueueRackNo": zxEponQueueRackNo,
       "zxEponQueueShelfNo": zxEponQueueShelfNo,
       "zxEponQueueSlotNo": zxEponQueueSlotNo,
       "zxEponQueueBufferSize": zxEponQueueBufferSize,
       "zxEponMgmtIndex": zxEponMgmtIndex,
       "zxEponIfIndexTable": zxEponIfIndexTable,
       "zxEponIfIndexEntry": zxEponIfIndexEntry,
       "zxEponifIndex": zxEponifIndex,
       "zxEponEntryStatus": zxEponEntryStatus}
)
