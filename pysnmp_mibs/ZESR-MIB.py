# SNMP MIB module (ZESR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZESR-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:55 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(zxr10switch,) = mibBuilder.importSymbols(
    "ZXR10-SMI",
    "zxr10switch")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zesr_ObjectIdentity = ObjectIdentity
zesr = _Zesr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12)
)
_ZesrGeneralConfig_ObjectIdentity = ObjectIdentity
zesrGeneralConfig = _ZesrGeneralConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12, 1)
)


class _RestartTime_Type(Integer32):
    """Custom type restartTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 600),
    )


_RestartTime_Type.__name__ = "Integer32"
_RestartTime_Object = MibScalar
restartTime = _RestartTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12, 1, 1),
    _RestartTime_Type()
)
restartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartTime.setStatus("current")


class _ProtocolMac_Type(Integer32):
    """Custom type protocolMac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("special", 1))
    )


_ProtocolMac_Type.__name__ = "Integer32"
_ProtocolMac_Object = MibScalar
protocolMac = _ProtocolMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12, 1, 2),
    _ProtocolMac_Type()
)
protocolMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocolMac.setStatus("current")


class _ClearSwitchTimes_Type(Integer32):
    """Custom type clearSwitchTimes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_ClearSwitchTimes_Type.__name__ = "Integer32"
_ClearSwitchTimes_Object = MibScalar
clearSwitchTimes = _ClearSwitchTimes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12, 1, 3),
    _ClearSwitchTimes_Type()
)
clearSwitchTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearSwitchTimes.setStatus("current")
_ZesrDomainTable_Object = MibTable
zesrDomainTable = _ZesrDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12, 2)
)
if mibBuilder.loadTexts:
    zesrDomainTable.setStatus("current")
_ZesrDomainEntry_Object = MibTableRow
zesrDomainEntry = _ZesrDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12, 2, 1)
)
zesrDomainEntry.setIndexNames(
    (0, "ZESR-MIB", "ctrlVlanID"),
)
if mibBuilder.loadTexts:
    zesrDomainEntry.setStatus("current")


class _CtrlVlanID_Type(Integer32):
    """Custom type ctrlVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_CtrlVlanID_Type.__name__ = "Integer32"
_CtrlVlanID_Object = MibTableColumn
ctrlVlanID = _CtrlVlanID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12, 2, 1, 1),
    _CtrlVlanID_Type()
)
ctrlVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlVlanID.setStatus("current")


class _ProtectInstanceID_Type(Integer32):
    """Custom type protectInstanceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ProtectInstanceID_Type.__name__ = "Integer32"
_ProtectInstanceID_Object = MibTableColumn
protectInstanceID = _ProtectInstanceID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12, 2, 1, 2),
    _ProtectInstanceID_Type()
)
protectInstanceID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    protectInstanceID.setStatus("current")
_ZesrDomainRowStatus_Type = RowStatus
_ZesrDomainRowStatus_Object = MibTableColumn
zesrDomainRowStatus = _ZesrDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12, 2, 1, 3),
    _ZesrDomainRowStatus_Type()
)
zesrDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zesrDomainRowStatus.setStatus("current")


class _ZesrDomainclearSwitchTimes_Type(Integer32):
    """Custom type zesrDomainclearSwitchTimes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_ZesrDomainclearSwitchTimes_Type.__name__ = "Integer32"
_ZesrDomainclearSwitchTimes_Object = MibTableColumn
zesrDomainclearSwitchTimes = _ZesrDomainclearSwitchTimes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12, 2, 1, 4),
    _ZesrDomainclearSwitchTimes_Type()
)
zesrDomainclearSwitchTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zesrDomainclearSwitchTimes.setStatus("current")
_ZesrMajorTable_Object = MibTable
zesrMajorTable = _ZesrMajorTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12, 3)
)
if mibBuilder.loadTexts:
    zesrMajorTable.setStatus("current")
_ZesrMajorEntry_Object = MibTableRow
zesrMajorEntry = _ZesrMajorEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12, 3, 1)
)
zesrMajorEntry.setIndexNames(
    (0, "ZESR-MIB", "ctrlVlanID"),
)
if mibBuilder.loadTexts:
    zesrMajorEntry.setStatus("current")


class _MajorRole_Type(Integer32):
    """Custom type majorRole based on Integer32"""
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
        *(("master", 0),
          ("transit", 1),
          ("zess-master", 2),
          ("zess-transit", 3))
    )


_MajorRole_Type.__name__ = "Integer32"
_MajorRole_Object = MibTableColumn
majorRole = _MajorRole_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12, 3, 1, 1),
    _MajorRole_Type()
)
majorRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    majorRole.setStatus("current")


class _MajorFirstPort_Type(DisplayString):
    """Custom type majorFirstPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MajorFirstPort_Type.__name__ = "DisplayString"
_MajorFirstPort_Object = MibTableColumn
majorFirstPort = _MajorFirstPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12, 3, 1, 2),
    _MajorFirstPort_Type()
)
majorFirstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    majorFirstPort.setStatus("current")


class _MajorSecondPort_Type(DisplayString):
    """Custom type majorSecondPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MajorSecondPort_Type.__name__ = "DisplayString"
_MajorSecondPort_Object = MibTableColumn
majorSecondPort = _MajorSecondPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12, 3, 1, 3),
    _MajorSecondPort_Type()
)
majorSecondPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    majorSecondPort.setStatus("current")


class _MajorPreforwardTime_Type(Integer32):
    """Custom type majorPreforwardTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_MajorPreforwardTime_Type.__name__ = "Integer32"
_MajorPreforwardTime_Object = MibTableColumn
majorPreforwardTime = _MajorPreforwardTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12, 3, 1, 4),
    _MajorPreforwardTime_Type()
)
majorPreforwardTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    majorPreforwardTime.setStatus("current")


class _MajorPreupTime_Type(Integer32):
    """Custom type majorPreupTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_MajorPreupTime_Type.__name__ = "Integer32"
_MajorPreupTime_Object = MibTableColumn
majorPreupTime = _MajorPreupTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12, 3, 1, 5),
    _MajorPreupTime_Type()
)
majorPreupTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    majorPreupTime.setStatus("current")


class _MajorHelloTime_Type(Integer32):
    """Custom type majorHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_MajorHelloTime_Type.__name__ = "Integer32"
_MajorHelloTime_Object = MibTableColumn
majorHelloTime = _MajorHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12, 3, 1, 6),
    _MajorHelloTime_Type()
)
majorHelloTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    majorHelloTime.setStatus("current")


class _MajorFailTime_Type(Integer32):
    """Custom type majorFailTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 18),
    )


_MajorFailTime_Type.__name__ = "Integer32"
_MajorFailTime_Object = MibTableColumn
majorFailTime = _MajorFailTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12, 3, 1, 7),
    _MajorFailTime_Type()
)
majorFailTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    majorFailTime.setStatus("current")


class _MajorState_Type(Integer32):
    """Custom type majorState based on Integer32"""
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
        *(("init", 0),
          ("up", 1),
          ("down", 2),
          ("preup", 3),
          ("start", 4),
          ("unknown", 5))
    )


_MajorState_Type.__name__ = "Integer32"
_MajorState_Object = MibTableColumn
majorState = _MajorState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12, 3, 1, 8),
    _MajorState_Type()
)
majorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    majorState.setStatus("current")


class _MajorFirstPortState_Type(Integer32):
    """Custom type majorFirstPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("block", 1),
          ("forward", 2))
    )


_MajorFirstPortState_Type.__name__ = "Integer32"
_MajorFirstPortState_Object = MibTableColumn
majorFirstPortState = _MajorFirstPortState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12, 3, 1, 9),
    _MajorFirstPortState_Type()
)
majorFirstPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    majorFirstPortState.setStatus("current")


class _MajorSecondPortState_Type(Integer32):
    """Custom type majorSecondPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("block", 1),
          ("forward", 2))
    )


_MajorSecondPortState_Type.__name__ = "Integer32"
_MajorSecondPortState_Object = MibTableColumn
majorSecondPortState = _MajorSecondPortState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12, 3, 1, 10),
    _MajorSecondPortState_Type()
)
majorSecondPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    majorSecondPortState.setStatus("current")
_MajorSwitchTimes_Type = Integer32
_MajorSwitchTimes_Object = MibTableColumn
majorSwitchTimes = _MajorSwitchTimes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12, 3, 1, 11),
    _MajorSwitchTimes_Type()
)
majorSwitchTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    majorSwitchTimes.setStatus("current")
_ZesrMajorRowStatus_Type = RowStatus
_ZesrMajorRowStatus_Object = MibTableColumn
zesrMajorRowStatus = _ZesrMajorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12, 3, 1, 12),
    _ZesrMajorRowStatus_Type()
)
zesrMajorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zesrMajorRowStatus.setStatus("current")


class _ZesrMajorclearSwitchTimes_Type(Integer32):
    """Custom type zesrMajorclearSwitchTimes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_ZesrMajorclearSwitchTimes_Type.__name__ = "Integer32"
_ZesrMajorclearSwitchTimes_Object = MibTableColumn
zesrMajorclearSwitchTimes = _ZesrMajorclearSwitchTimes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12, 3, 1, 13),
    _ZesrMajorclearSwitchTimes_Type()
)
zesrMajorclearSwitchTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zesrMajorclearSwitchTimes.setStatus("current")
_ZesrLevelTable_Object = MibTable
zesrLevelTable = _ZesrLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12, 4)
)
if mibBuilder.loadTexts:
    zesrLevelTable.setStatus("current")
_ZesrLevelEntry_Object = MibTableRow
zesrLevelEntry = _ZesrLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12, 4, 1)
)
zesrLevelEntry.setIndexNames(
    (0, "ZESR-MIB", "ctrlVlanID"),
    (0, "ZESR-MIB", "levelID"),
    (0, "ZESR-MIB", "levelSegID"),
)
if mibBuilder.loadTexts:
    zesrLevelEntry.setStatus("current")


class _LevelID_Type(Integer32):
    """Custom type levelID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_LevelID_Type.__name__ = "Integer32"
_LevelID_Object = MibTableColumn
levelID = _LevelID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12, 4, 1, 1),
    _LevelID_Type()
)
levelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    levelID.setStatus("current")


class _LevelSegID_Type(Integer32):
    """Custom type levelSegID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_LevelSegID_Type.__name__ = "Integer32"
_LevelSegID_Object = MibTableColumn
levelSegID = _LevelSegID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12, 4, 1, 2),
    _LevelSegID_Type()
)
levelSegID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    levelSegID.setStatus("current")


class _LevelRole_Type(Integer32):
    """Custom type levelRole based on Integer32"""
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
        *(("master", 0),
          ("transit", 1),
          ("edge-assistant", 2),
          ("edge-control", 3))
    )


_LevelRole_Type.__name__ = "Integer32"
_LevelRole_Object = MibTableColumn
levelRole = _LevelRole_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12, 4, 1, 3),
    _LevelRole_Type()
)
levelRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    levelRole.setStatus("current")


class _LevelFirstPort_Type(DisplayString):
    """Custom type levelFirstPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_LevelFirstPort_Type.__name__ = "DisplayString"
_LevelFirstPort_Object = MibTableColumn
levelFirstPort = _LevelFirstPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12, 4, 1, 4),
    _LevelFirstPort_Type()
)
levelFirstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    levelFirstPort.setStatus("current")


class _LevelSecondPort_Type(DisplayString):
    """Custom type levelSecondPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_LevelSecondPort_Type.__name__ = "DisplayString"
_LevelSecondPort_Object = MibTableColumn
levelSecondPort = _LevelSecondPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12, 4, 1, 5),
    _LevelSecondPort_Type()
)
levelSecondPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    levelSecondPort.setStatus("current")


class _LevelPreforwardTime_Type(Integer32):
    """Custom type levelPreforwardTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_LevelPreforwardTime_Type.__name__ = "Integer32"
_LevelPreforwardTime_Object = MibTableColumn
levelPreforwardTime = _LevelPreforwardTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12, 4, 1, 6),
    _LevelPreforwardTime_Type()
)
levelPreforwardTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    levelPreforwardTime.setStatus("current")


class _LevelPreupTime_Type(Integer32):
    """Custom type levelPreupTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_LevelPreupTime_Type.__name__ = "Integer32"
_LevelPreupTime_Object = MibTableColumn
levelPreupTime = _LevelPreupTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12, 4, 1, 7),
    _LevelPreupTime_Type()
)
levelPreupTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    levelPreupTime.setStatus("current")


class _LevelHelloTime_Type(Integer32):
    """Custom type levelHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_LevelHelloTime_Type.__name__ = "Integer32"
_LevelHelloTime_Object = MibTableColumn
levelHelloTime = _LevelHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12, 4, 1, 8),
    _LevelHelloTime_Type()
)
levelHelloTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    levelHelloTime.setStatus("current")


class _LevelFailTime_Type(Integer32):
    """Custom type levelFailTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 18),
    )


_LevelFailTime_Type.__name__ = "Integer32"
_LevelFailTime_Object = MibTableColumn
levelFailTime = _LevelFailTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12, 4, 1, 9),
    _LevelFailTime_Type()
)
levelFailTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    levelFailTime.setStatus("current")


class _LevelState_Type(Integer32):
    """Custom type levelState based on Integer32"""
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
        *(("init", 0),
          ("up", 1),
          ("down", 2),
          ("preup", 3),
          ("start", 4),
          ("unknown", 5))
    )


_LevelState_Type.__name__ = "Integer32"
_LevelState_Object = MibTableColumn
levelState = _LevelState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12, 4, 1, 10),
    _LevelState_Type()
)
levelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    levelState.setStatus("current")


class _LevelFirstPortState_Type(Integer32):
    """Custom type levelFirstPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("block", 1),
          ("forward", 2))
    )


_LevelFirstPortState_Type.__name__ = "Integer32"
_LevelFirstPortState_Object = MibTableColumn
levelFirstPortState = _LevelFirstPortState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12, 4, 1, 11),
    _LevelFirstPortState_Type()
)
levelFirstPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    levelFirstPortState.setStatus("current")


class _LevelSecondPortState_Type(Integer32):
    """Custom type levelSecondPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("block", 1),
          ("forward", 2))
    )


_LevelSecondPortState_Type.__name__ = "Integer32"
_LevelSecondPortState_Object = MibTableColumn
levelSecondPortState = _LevelSecondPortState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12, 4, 1, 12),
    _LevelSecondPortState_Type()
)
levelSecondPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    levelSecondPortState.setStatus("current")
_LevelSwitchTimes_Type = Integer32
_LevelSwitchTimes_Object = MibTableColumn
levelSwitchTimes = _LevelSwitchTimes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12, 4, 1, 13),
    _LevelSwitchTimes_Type()
)
levelSwitchTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    levelSwitchTimes.setStatus("current")
_ZesrLevelRowStatus_Type = RowStatus
_ZesrLevelRowStatus_Object = MibTableColumn
zesrLevelRowStatus = _ZesrLevelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12, 4, 1, 14),
    _ZesrLevelRowStatus_Type()
)
zesrLevelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zesrLevelRowStatus.setStatus("current")


class _ZesrLevelclearSwitchTimes_Type(Integer32):
    """Custom type zesrLevelclearSwitchTimes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_ZesrLevelclearSwitchTimes_Type.__name__ = "Integer32"
_ZesrLevelclearSwitchTimes_Object = MibTableColumn
zesrLevelclearSwitchTimes = _ZesrLevelclearSwitchTimes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 12, 4, 1, 15),
    _ZesrLevelclearSwitchTimes_Type()
)
zesrLevelclearSwitchTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zesrLevelclearSwitchTimes.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZESR-MIB",
    **{"zesr": zesr,
       "zesrGeneralConfig": zesrGeneralConfig,
       "restartTime": restartTime,
       "protocolMac": protocolMac,
       "clearSwitchTimes": clearSwitchTimes,
       "zesrDomainTable": zesrDomainTable,
       "zesrDomainEntry": zesrDomainEntry,
       "ctrlVlanID": ctrlVlanID,
       "protectInstanceID": protectInstanceID,
       "zesrDomainRowStatus": zesrDomainRowStatus,
       "zesrDomainclearSwitchTimes": zesrDomainclearSwitchTimes,
       "zesrMajorTable": zesrMajorTable,
       "zesrMajorEntry": zesrMajorEntry,
       "majorRole": majorRole,
       "majorFirstPort": majorFirstPort,
       "majorSecondPort": majorSecondPort,
       "majorPreforwardTime": majorPreforwardTime,
       "majorPreupTime": majorPreupTime,
       "majorHelloTime": majorHelloTime,
       "majorFailTime": majorFailTime,
       "majorState": majorState,
       "majorFirstPortState": majorFirstPortState,
       "majorSecondPortState": majorSecondPortState,
       "majorSwitchTimes": majorSwitchTimes,
       "zesrMajorRowStatus": zesrMajorRowStatus,
       "zesrMajorclearSwitchTimes": zesrMajorclearSwitchTimes,
       "zesrLevelTable": zesrLevelTable,
       "zesrLevelEntry": zesrLevelEntry,
       "levelID": levelID,
       "levelSegID": levelSegID,
       "levelRole": levelRole,
       "levelFirstPort": levelFirstPort,
       "levelSecondPort": levelSecondPort,
       "levelPreforwardTime": levelPreforwardTime,
       "levelPreupTime": levelPreupTime,
       "levelHelloTime": levelHelloTime,
       "levelFailTime": levelFailTime,
       "levelState": levelState,
       "levelFirstPortState": levelFirstPortState,
       "levelSecondPortState": levelSecondPortState,
       "levelSwitchTimes": levelSwitchTimes,
       "zesrLevelRowStatus": zesrLevelRowStatus,
       "zesrLevelclearSwitchTimes": zesrLevelclearSwitchTimes}
)
