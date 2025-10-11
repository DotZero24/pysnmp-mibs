# SNMP MIB module (ARICENT-ECFM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-ECFM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:44:23 2025
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

(Dot1agCfmInterfaceStatus,
 Dot1agCfmPortStatus) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmInterfaceStatus",
    "Dot1agCfmPortStatus")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(LldpChassisId,
 LldpChassisIdSubtype) = mibBuilder.importSymbols(
    "LLDP-MIB",
    "LldpChassisId",
    "LldpChassisIdSubtype")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
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
 RowStatus,
 TAddress,
 TDomain,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TAddress",
    "TDomain",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsecfm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 150)
)
if mibBuilder.loadTexts:
    fsecfm.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FsEcfmOuiType(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3



class FsEcfmSetTraps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("trapUnUsedbit", 0),
          ("trapRDICCM", 1),
          ("trapMACstatus", 2),
          ("trapRemoteCCM", 3),
          ("trapErrorCCM", 4),
          ("trapXconCCM", 5))
    )


# MIB Managed Objects in the order of their OIDs

_FsEcfmSystem_ObjectIdentity = ObjectIdentity
fsEcfmSystem = _FsEcfmSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1)
)


class _FsEcfmSystemControl_Type(Integer32):
    """Custom type fsEcfmSystemControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("shutdown", 2))
    )


_FsEcfmSystemControl_Type.__name__ = "Integer32"
_FsEcfmSystemControl_Object = MibScalar
fsEcfmSystemControl = _FsEcfmSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 1),
    _FsEcfmSystemControl_Type()
)
fsEcfmSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmSystemControl.setStatus("current")


class _FsEcfmModuleStatus_Type(Integer32):
    """Custom type fsEcfmModuleStatus based on Integer32"""
    defaultValue = 2

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


_FsEcfmModuleStatus_Type.__name__ = "Integer32"
_FsEcfmModuleStatus_Object = MibScalar
fsEcfmModuleStatus = _FsEcfmModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 2),
    _FsEcfmModuleStatus_Type()
)
fsEcfmModuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmModuleStatus.setStatus("current")
_FsEcfmOui_Type = FsEcfmOuiType
_FsEcfmOui_Object = MibScalar
fsEcfmOui = _FsEcfmOui_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 3),
    _FsEcfmOui_Type()
)
fsEcfmOui.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmOui.setStatus("current")


class _FsEcfmTraceOption_Type(Integer32):
    """Custom type fsEcfmTraceOption based on Integer32"""
    defaultValue = 262144


_FsEcfmTraceOption_Type.__name__ = "Integer32"
_FsEcfmTraceOption_Object = MibScalar
fsEcfmTraceOption = _FsEcfmTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 4),
    _FsEcfmTraceOption_Type()
)
fsEcfmTraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmTraceOption.setStatus("current")


class _FsEcfmLtrCacheStatus_Type(Integer32):
    """Custom type fsEcfmLtrCacheStatus based on Integer32"""
    defaultValue = 2

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


_FsEcfmLtrCacheStatus_Type.__name__ = "Integer32"
_FsEcfmLtrCacheStatus_Object = MibScalar
fsEcfmLtrCacheStatus = _FsEcfmLtrCacheStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 5),
    _FsEcfmLtrCacheStatus_Type()
)
fsEcfmLtrCacheStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmLtrCacheStatus.setStatus("current")


class _FsEcfmLtrCacheClear_Type(TruthValue):
    """Custom type fsEcfmLtrCacheClear based on TruthValue"""
    defaultValue = 2


_FsEcfmLtrCacheClear_Type.__name__ = "TruthValue"
_FsEcfmLtrCacheClear_Object = MibScalar
fsEcfmLtrCacheClear = _FsEcfmLtrCacheClear_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 6),
    _FsEcfmLtrCacheClear_Type()
)
fsEcfmLtrCacheClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmLtrCacheClear.setStatus("current")


class _FsEcfmLtrCacheHoldTime_Type(Integer32):
    """Custom type fsEcfmLtrCacheHoldTime based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10080),
    )


_FsEcfmLtrCacheHoldTime_Type.__name__ = "Integer32"
_FsEcfmLtrCacheHoldTime_Object = MibScalar
fsEcfmLtrCacheHoldTime = _FsEcfmLtrCacheHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 7),
    _FsEcfmLtrCacheHoldTime_Type()
)
fsEcfmLtrCacheHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmLtrCacheHoldTime.setStatus("current")


class _FsEcfmLtrCacheSize_Type(Integer32):
    """Custom type fsEcfmLtrCacheSize based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_FsEcfmLtrCacheSize_Type.__name__ = "Integer32"
_FsEcfmLtrCacheSize_Object = MibScalar
fsEcfmLtrCacheSize = _FsEcfmLtrCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 8),
    _FsEcfmLtrCacheSize_Type()
)
fsEcfmLtrCacheSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmLtrCacheSize.setStatus("current")
_FsEcfmPortTable_Object = MibTable
fsEcfmPortTable = _FsEcfmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 9)
)
if mibBuilder.loadTexts:
    fsEcfmPortTable.setStatus("current")
_FsEcfmPortEntry_Object = MibTableRow
fsEcfmPortEntry = _FsEcfmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 9, 1)
)
fsEcfmPortEntry.setIndexNames(
    (0, "ARICENT-ECFM-MIB", "fsEcfmPortIndex"),
)
if mibBuilder.loadTexts:
    fsEcfmPortEntry.setStatus("current")


class _FsEcfmPortIndex_Type(Unsigned32):
    """Custom type fsEcfmPortIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsEcfmPortIndex_Type.__name__ = "Unsigned32"
_FsEcfmPortIndex_Object = MibTableColumn
fsEcfmPortIndex = _FsEcfmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 9, 1, 1),
    _FsEcfmPortIndex_Type()
)
fsEcfmPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsEcfmPortIndex.setStatus("current")


class _FsEcfmPortLLCEncapStatus_Type(TruthValue):
    """Custom type fsEcfmPortLLCEncapStatus based on TruthValue"""
    defaultValue = 2


_FsEcfmPortLLCEncapStatus_Type.__name__ = "TruthValue"
_FsEcfmPortLLCEncapStatus_Object = MibTableColumn
fsEcfmPortLLCEncapStatus = _FsEcfmPortLLCEncapStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 9, 1, 2),
    _FsEcfmPortLLCEncapStatus_Type()
)
fsEcfmPortLLCEncapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmPortLLCEncapStatus.setStatus("current")


class _FsEcfmPortModuleStatus_Type(Integer32):
    """Custom type fsEcfmPortModuleStatus based on Integer32"""
    defaultValue = 2

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


_FsEcfmPortModuleStatus_Type.__name__ = "Integer32"
_FsEcfmPortModuleStatus_Object = MibTableColumn
fsEcfmPortModuleStatus = _FsEcfmPortModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 9, 1, 3),
    _FsEcfmPortModuleStatus_Type()
)
fsEcfmPortModuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmPortModuleStatus.setStatus("current")
_FsEcfmPortTxCfmPduCount_Type = Unsigned32
_FsEcfmPortTxCfmPduCount_Object = MibTableColumn
fsEcfmPortTxCfmPduCount = _FsEcfmPortTxCfmPduCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 9, 1, 4),
    _FsEcfmPortTxCfmPduCount_Type()
)
fsEcfmPortTxCfmPduCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmPortTxCfmPduCount.setStatus("current")
_FsEcfmPortTxCcmCount_Type = Unsigned32
_FsEcfmPortTxCcmCount_Object = MibTableColumn
fsEcfmPortTxCcmCount = _FsEcfmPortTxCcmCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 9, 1, 5),
    _FsEcfmPortTxCcmCount_Type()
)
fsEcfmPortTxCcmCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmPortTxCcmCount.setStatus("current")
_FsEcfmPortTxLbmCount_Type = Unsigned32
_FsEcfmPortTxLbmCount_Object = MibTableColumn
fsEcfmPortTxLbmCount = _FsEcfmPortTxLbmCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 9, 1, 6),
    _FsEcfmPortTxLbmCount_Type()
)
fsEcfmPortTxLbmCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmPortTxLbmCount.setStatus("current")
_FsEcfmPortTxLbrCount_Type = Unsigned32
_FsEcfmPortTxLbrCount_Object = MibTableColumn
fsEcfmPortTxLbrCount = _FsEcfmPortTxLbrCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 9, 1, 7),
    _FsEcfmPortTxLbrCount_Type()
)
fsEcfmPortTxLbrCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmPortTxLbrCount.setStatus("current")
_FsEcfmPortTxLtmCount_Type = Unsigned32
_FsEcfmPortTxLtmCount_Object = MibTableColumn
fsEcfmPortTxLtmCount = _FsEcfmPortTxLtmCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 9, 1, 8),
    _FsEcfmPortTxLtmCount_Type()
)
fsEcfmPortTxLtmCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmPortTxLtmCount.setStatus("current")
_FsEcfmPortTxLtrCount_Type = Unsigned32
_FsEcfmPortTxLtrCount_Object = MibTableColumn
fsEcfmPortTxLtrCount = _FsEcfmPortTxLtrCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 9, 1, 9),
    _FsEcfmPortTxLtrCount_Type()
)
fsEcfmPortTxLtrCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmPortTxLtrCount.setStatus("current")
_FsEcfmPortTxFailedCount_Type = Unsigned32
_FsEcfmPortTxFailedCount_Object = MibTableColumn
fsEcfmPortTxFailedCount = _FsEcfmPortTxFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 9, 1, 10),
    _FsEcfmPortTxFailedCount_Type()
)
fsEcfmPortTxFailedCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmPortTxFailedCount.setStatus("current")
_FsEcfmPortRxCfmPduCount_Type = Unsigned32
_FsEcfmPortRxCfmPduCount_Object = MibTableColumn
fsEcfmPortRxCfmPduCount = _FsEcfmPortRxCfmPduCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 9, 1, 11),
    _FsEcfmPortRxCfmPduCount_Type()
)
fsEcfmPortRxCfmPduCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmPortRxCfmPduCount.setStatus("current")
_FsEcfmPortRxCcmCount_Type = Unsigned32
_FsEcfmPortRxCcmCount_Object = MibTableColumn
fsEcfmPortRxCcmCount = _FsEcfmPortRxCcmCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 9, 1, 12),
    _FsEcfmPortRxCcmCount_Type()
)
fsEcfmPortRxCcmCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmPortRxCcmCount.setStatus("current")
_FsEcfmPortRxLbmCount_Type = Unsigned32
_FsEcfmPortRxLbmCount_Object = MibTableColumn
fsEcfmPortRxLbmCount = _FsEcfmPortRxLbmCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 9, 1, 13),
    _FsEcfmPortRxLbmCount_Type()
)
fsEcfmPortRxLbmCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmPortRxLbmCount.setStatus("current")
_FsEcfmPortRxLbrCount_Type = Unsigned32
_FsEcfmPortRxLbrCount_Object = MibTableColumn
fsEcfmPortRxLbrCount = _FsEcfmPortRxLbrCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 9, 1, 14),
    _FsEcfmPortRxLbrCount_Type()
)
fsEcfmPortRxLbrCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmPortRxLbrCount.setStatus("current")
_FsEcfmPortRxLtmCount_Type = Unsigned32
_FsEcfmPortRxLtmCount_Object = MibTableColumn
fsEcfmPortRxLtmCount = _FsEcfmPortRxLtmCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 9, 1, 15),
    _FsEcfmPortRxLtmCount_Type()
)
fsEcfmPortRxLtmCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmPortRxLtmCount.setStatus("current")
_FsEcfmPortRxLtrCount_Type = Unsigned32
_FsEcfmPortRxLtrCount_Object = MibTableColumn
fsEcfmPortRxLtrCount = _FsEcfmPortRxLtrCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 9, 1, 16),
    _FsEcfmPortRxLtrCount_Type()
)
fsEcfmPortRxLtrCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmPortRxLtrCount.setStatus("current")
_FsEcfmPortRxBadCfmPduCount_Type = Unsigned32
_FsEcfmPortRxBadCfmPduCount_Object = MibTableColumn
fsEcfmPortRxBadCfmPduCount = _FsEcfmPortRxBadCfmPduCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 9, 1, 17),
    _FsEcfmPortRxBadCfmPduCount_Type()
)
fsEcfmPortRxBadCfmPduCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmPortRxBadCfmPduCount.setStatus("current")
_FsEcfmPortFrwdCfmPduCount_Type = Unsigned32
_FsEcfmPortFrwdCfmPduCount_Object = MibTableColumn
fsEcfmPortFrwdCfmPduCount = _FsEcfmPortFrwdCfmPduCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 9, 1, 18),
    _FsEcfmPortFrwdCfmPduCount_Type()
)
fsEcfmPortFrwdCfmPduCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmPortFrwdCfmPduCount.setStatus("current")
_FsEcfmPortDsrdCfmPduCount_Type = Unsigned32
_FsEcfmPortDsrdCfmPduCount_Object = MibTableColumn
fsEcfmPortDsrdCfmPduCount = _FsEcfmPortDsrdCfmPduCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 9, 1, 19),
    _FsEcfmPortDsrdCfmPduCount_Type()
)
fsEcfmPortDsrdCfmPduCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmPortDsrdCfmPduCount.setStatus("current")


class _FsEcfmMipCcmDbStatus_Type(Integer32):
    """Custom type fsEcfmMipCcmDbStatus based on Integer32"""
    defaultValue = 2

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


_FsEcfmMipCcmDbStatus_Type.__name__ = "Integer32"
_FsEcfmMipCcmDbStatus_Object = MibScalar
fsEcfmMipCcmDbStatus = _FsEcfmMipCcmDbStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 10),
    _FsEcfmMipCcmDbStatus_Type()
)
fsEcfmMipCcmDbStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmMipCcmDbStatus.setStatus("current")


class _FsEcfmMipCcmDbClear_Type(TruthValue):
    """Custom type fsEcfmMipCcmDbClear based on TruthValue"""
    defaultValue = 2


_FsEcfmMipCcmDbClear_Type.__name__ = "TruthValue"
_FsEcfmMipCcmDbClear_Object = MibScalar
fsEcfmMipCcmDbClear = _FsEcfmMipCcmDbClear_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 11),
    _FsEcfmMipCcmDbClear_Type()
)
fsEcfmMipCcmDbClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmMipCcmDbClear.setStatus("current")


class _FsEcfmMipCcmDbSize_Type(Integer32):
    """Custom type fsEcfmMipCcmDbSize based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 10000),
    )


_FsEcfmMipCcmDbSize_Type.__name__ = "Integer32"
_FsEcfmMipCcmDbSize_Object = MibScalar
fsEcfmMipCcmDbSize = _FsEcfmMipCcmDbSize_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 12),
    _FsEcfmMipCcmDbSize_Type()
)
fsEcfmMipCcmDbSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmMipCcmDbSize.setStatus("current")


class _FsEcfmMipCcmDbHoldTime_Type(Integer32):
    """Custom type fsEcfmMipCcmDbHoldTime based on Integer32"""
    defaultValue = 24

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(24, 48),
    )


_FsEcfmMipCcmDbHoldTime_Type.__name__ = "Integer32"
_FsEcfmMipCcmDbHoldTime_Object = MibScalar
fsEcfmMipCcmDbHoldTime = _FsEcfmMipCcmDbHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 13),
    _FsEcfmMipCcmDbHoldTime_Type()
)
fsEcfmMipCcmDbHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmMipCcmDbHoldTime.setStatus("current")
_FsEcfmMemoryFailureCount_Type = Unsigned32
_FsEcfmMemoryFailureCount_Object = MibScalar
fsEcfmMemoryFailureCount = _FsEcfmMemoryFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 14),
    _FsEcfmMemoryFailureCount_Type()
)
fsEcfmMemoryFailureCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmMemoryFailureCount.setStatus("current")
_FsEcfmBufferFailureCount_Type = Unsigned32
_FsEcfmBufferFailureCount_Object = MibScalar
fsEcfmBufferFailureCount = _FsEcfmBufferFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 15),
    _FsEcfmBufferFailureCount_Type()
)
fsEcfmBufferFailureCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmBufferFailureCount.setStatus("current")
_FsEcfmUpCount_Type = Unsigned32
_FsEcfmUpCount_Object = MibScalar
fsEcfmUpCount = _FsEcfmUpCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 16),
    _FsEcfmUpCount_Type()
)
fsEcfmUpCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmUpCount.setStatus("current")
_FsEcfmDownCount_Type = Unsigned32
_FsEcfmDownCount_Object = MibScalar
fsEcfmDownCount = _FsEcfmDownCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 17),
    _FsEcfmDownCount_Type()
)
fsEcfmDownCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmDownCount.setStatus("current")
_FsEcfmNoDftCount_Type = Unsigned32
_FsEcfmNoDftCount_Object = MibScalar
fsEcfmNoDftCount = _FsEcfmNoDftCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 18),
    _FsEcfmNoDftCount_Type()
)
fsEcfmNoDftCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmNoDftCount.setStatus("current")
_FsEcfmRdiDftCount_Type = Unsigned32
_FsEcfmRdiDftCount_Object = MibScalar
fsEcfmRdiDftCount = _FsEcfmRdiDftCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 19),
    _FsEcfmRdiDftCount_Type()
)
fsEcfmRdiDftCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmRdiDftCount.setStatus("current")
_FsEcfmMacStatusDftCount_Type = Unsigned32
_FsEcfmMacStatusDftCount_Object = MibScalar
fsEcfmMacStatusDftCount = _FsEcfmMacStatusDftCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 20),
    _FsEcfmMacStatusDftCount_Type()
)
fsEcfmMacStatusDftCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmMacStatusDftCount.setStatus("current")
_FsEcfmRemoteCcmDftCount_Type = Unsigned32
_FsEcfmRemoteCcmDftCount_Object = MibScalar
fsEcfmRemoteCcmDftCount = _FsEcfmRemoteCcmDftCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 21),
    _FsEcfmRemoteCcmDftCount_Type()
)
fsEcfmRemoteCcmDftCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmRemoteCcmDftCount.setStatus("current")
_FsEcfmErrorCcmDftCount_Type = Unsigned32
_FsEcfmErrorCcmDftCount_Object = MibScalar
fsEcfmErrorCcmDftCount = _FsEcfmErrorCcmDftCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 22),
    _FsEcfmErrorCcmDftCount_Type()
)
fsEcfmErrorCcmDftCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmErrorCcmDftCount.setStatus("current")
_FsEcfmXconDftCount_Type = Unsigned32
_FsEcfmXconDftCount_Object = MibScalar
fsEcfmXconDftCount = _FsEcfmXconDftCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 23),
    _FsEcfmXconDftCount_Type()
)
fsEcfmXconDftCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmXconDftCount.setStatus("current")


class _FsEcfmCrosscheckDelay_Type(Integer32):
    """Custom type fsEcfmCrosscheckDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 100),
    )


_FsEcfmCrosscheckDelay_Type.__name__ = "Integer32"
_FsEcfmCrosscheckDelay_Object = MibScalar
fsEcfmCrosscheckDelay = _FsEcfmCrosscheckDelay_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 24),
    _FsEcfmCrosscheckDelay_Type()
)
fsEcfmCrosscheckDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmCrosscheckDelay.setStatus("current")
_FsEcfmMipDynamicEvaluationStatus_Type = TruthValue
_FsEcfmMipDynamicEvaluationStatus_Object = MibScalar
fsEcfmMipDynamicEvaluationStatus = _FsEcfmMipDynamicEvaluationStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 25),
    _FsEcfmMipDynamicEvaluationStatus_Type()
)
fsEcfmMipDynamicEvaluationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmMipDynamicEvaluationStatus.setStatus("current")
_FsEcfmMipTable_Object = MibTable
fsEcfmMipTable = _FsEcfmMipTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 26)
)
if mibBuilder.loadTexts:
    fsEcfmMipTable.setStatus("current")
_FsEcfmMipEntry_Object = MibTableRow
fsEcfmMipEntry = _FsEcfmMipEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 26, 1)
)
fsEcfmMipEntry.setIndexNames(
    (0, "ARICENT-ECFM-MIB", "fsEcfmMipIfIndex"),
    (0, "ARICENT-ECFM-MIB", "fsEcfmMipMdLevel"),
    (0, "ARICENT-ECFM-MIB", "fsEcfmMipVid"),
)
if mibBuilder.loadTexts:
    fsEcfmMipEntry.setStatus("current")
_FsEcfmMipIfIndex_Type = InterfaceIndex
_FsEcfmMipIfIndex_Object = MibTableColumn
fsEcfmMipIfIndex = _FsEcfmMipIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 26, 1, 1),
    _FsEcfmMipIfIndex_Type()
)
fsEcfmMipIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsEcfmMipIfIndex.setStatus("current")


class _FsEcfmMipMdLevel_Type(Integer32):
    """Custom type fsEcfmMipMdLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsEcfmMipMdLevel_Type.__name__ = "Integer32"
_FsEcfmMipMdLevel_Object = MibTableColumn
fsEcfmMipMdLevel = _FsEcfmMipMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 26, 1, 2),
    _FsEcfmMipMdLevel_Type()
)
fsEcfmMipMdLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsEcfmMipMdLevel.setStatus("current")
_FsEcfmMipVid_Type = VlanId
_FsEcfmMipVid_Object = MibTableColumn
fsEcfmMipVid = _FsEcfmMipVid_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 26, 1, 3),
    _FsEcfmMipVid_Type()
)
fsEcfmMipVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsEcfmMipVid.setStatus("current")
_FsEcfmMipActive_Type = TruthValue
_FsEcfmMipActive_Object = MibTableColumn
fsEcfmMipActive = _FsEcfmMipActive_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 26, 1, 4),
    _FsEcfmMipActive_Type()
)
fsEcfmMipActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsEcfmMipActive.setStatus("current")
_FsEcfmMipRowStatus_Type = RowStatus
_FsEcfmMipRowStatus_Object = MibTableColumn
fsEcfmMipRowStatus = _FsEcfmMipRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 26, 1, 5),
    _FsEcfmMipRowStatus_Type()
)
fsEcfmMipRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsEcfmMipRowStatus.setStatus("current")
_FsEcfmMipCcmDbTable_Object = MibTable
fsEcfmMipCcmDbTable = _FsEcfmMipCcmDbTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 27)
)
if mibBuilder.loadTexts:
    fsEcfmMipCcmDbTable.setStatus("current")
_FsEcfmMipCcmDbEntry_Object = MibTableRow
fsEcfmMipCcmDbEntry = _FsEcfmMipCcmDbEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 27, 1)
)
fsEcfmMipCcmDbEntry.setIndexNames(
    (0, "ARICENT-ECFM-MIB", "fsEcfmMipCcmFid"),
    (0, "ARICENT-ECFM-MIB", "fsEcfmMipCcmSrcAddr"),
)
if mibBuilder.loadTexts:
    fsEcfmMipCcmDbEntry.setStatus("current")


class _FsEcfmMipCcmFid_Type(Unsigned32):
    """Custom type fsEcfmMipCcmFid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FsEcfmMipCcmFid_Type.__name__ = "Unsigned32"
_FsEcfmMipCcmFid_Object = MibTableColumn
fsEcfmMipCcmFid = _FsEcfmMipCcmFid_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 27, 1, 1),
    _FsEcfmMipCcmFid_Type()
)
fsEcfmMipCcmFid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsEcfmMipCcmFid.setStatus("current")
_FsEcfmMipCcmSrcAddr_Type = MacAddress
_FsEcfmMipCcmSrcAddr_Object = MibTableColumn
fsEcfmMipCcmSrcAddr = _FsEcfmMipCcmSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 27, 1, 2),
    _FsEcfmMipCcmSrcAddr_Type()
)
fsEcfmMipCcmSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsEcfmMipCcmSrcAddr.setStatus("current")
_FsEcfmMipCcmIfIndex_Type = InterfaceIndex
_FsEcfmMipCcmIfIndex_Object = MibTableColumn
fsEcfmMipCcmIfIndex = _FsEcfmMipCcmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 27, 1, 3),
    _FsEcfmMipCcmIfIndex_Type()
)
fsEcfmMipCcmIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEcfmMipCcmIfIndex.setStatus("current")


class _FsEcfmGlobalCcmOffload_Type(Integer32):
    """Custom type fsEcfmGlobalCcmOffload based on Integer32"""
    defaultValue = 2

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


_FsEcfmGlobalCcmOffload_Type.__name__ = "Integer32"
_FsEcfmGlobalCcmOffload_Object = MibScalar
fsEcfmGlobalCcmOffload = _FsEcfmGlobalCcmOffload_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 28),
    _FsEcfmGlobalCcmOffload_Type()
)
fsEcfmGlobalCcmOffload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmGlobalCcmOffload.setStatus("current")
_FsEcfmDynMipPreventionTable_Object = MibTable
fsEcfmDynMipPreventionTable = _FsEcfmDynMipPreventionTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 29)
)
if mibBuilder.loadTexts:
    fsEcfmDynMipPreventionTable.setStatus("current")
_FsEcfmDynMipPreventionEntry_Object = MibTableRow
fsEcfmDynMipPreventionEntry = _FsEcfmDynMipPreventionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 29, 1)
)
fsEcfmDynMipPreventionEntry.setIndexNames(
    (0, "ARICENT-ECFM-MIB", "fsEcfmMipIfIndex"),
    (0, "ARICENT-ECFM-MIB", "fsEcfmMipMdLevel"),
    (0, "ARICENT-ECFM-MIB", "fsEcfmMipVid"),
)
if mibBuilder.loadTexts:
    fsEcfmDynMipPreventionEntry.setStatus("current")


class _FsEcfmDynMipPreventionRowStatus_Type(RowStatus):
    """Custom type fsEcfmDynMipPreventionRowStatus based on RowStatus"""
    subtypeSpec = RowStatus.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("createAndGo", 4),
          ("destroy", 6))
    )


_FsEcfmDynMipPreventionRowStatus_Type.__name__ = "RowStatus"
_FsEcfmDynMipPreventionRowStatus_Object = MibTableColumn
fsEcfmDynMipPreventionRowStatus = _FsEcfmDynMipPreventionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 1, 29, 1, 1),
    _FsEcfmDynMipPreventionRowStatus_Type()
)
fsEcfmDynMipPreventionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsEcfmDynMipPreventionRowStatus.setStatus("current")
_FsEcfmExObjects_ObjectIdentity = ObjectIdentity
fsEcfmExObjects = _FsEcfmExObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2)
)
_FsEcfmRemoteMepDbExTable_Object = MibTable
fsEcfmRemoteMepDbExTable = _FsEcfmRemoteMepDbExTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 1)
)
if mibBuilder.loadTexts:
    fsEcfmRemoteMepDbExTable.setStatus("current")
_FsEcfmRemoteMepDbExEntry_Object = MibTableRow
fsEcfmRemoteMepDbExEntry = _FsEcfmRemoteMepDbExEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 1, 1)
)
fsEcfmRemoteMepDbExEntry.setIndexNames(
    (0, "ARICENT-ECFM-MIB", "fsEcfmMdIndex"),
    (0, "ARICENT-ECFM-MIB", "fsEcfmMaIndex"),
    (0, "ARICENT-ECFM-MIB", "fsEcfmMepIdentifier"),
    (0, "ARICENT-ECFM-MIB", "fsEcfmRMepIdentifier"),
)
if mibBuilder.loadTexts:
    fsEcfmRemoteMepDbExEntry.setStatus("current")


class _FsEcfmMdIndex_Type(Unsigned32):
    """Custom type fsEcfmMdIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FsEcfmMdIndex_Type.__name__ = "Unsigned32"
_FsEcfmMdIndex_Object = MibTableColumn
fsEcfmMdIndex = _FsEcfmMdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 1, 1, 1),
    _FsEcfmMdIndex_Type()
)
fsEcfmMdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsEcfmMdIndex.setStatus("current")


class _FsEcfmMaIndex_Type(Unsigned32):
    """Custom type fsEcfmMaIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FsEcfmMaIndex_Type.__name__ = "Unsigned32"
_FsEcfmMaIndex_Object = MibTableColumn
fsEcfmMaIndex = _FsEcfmMaIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 1, 1, 2),
    _FsEcfmMaIndex_Type()
)
fsEcfmMaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsEcfmMaIndex.setStatus("current")


class _FsEcfmMepIdentifier_Type(Unsigned32):
    """Custom type fsEcfmMepIdentifier based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_FsEcfmMepIdentifier_Type.__name__ = "Unsigned32"
_FsEcfmMepIdentifier_Object = MibTableColumn
fsEcfmMepIdentifier = _FsEcfmMepIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 1, 1, 3),
    _FsEcfmMepIdentifier_Type()
)
fsEcfmMepIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsEcfmMepIdentifier.setStatus("current")


class _FsEcfmRMepIdentifier_Type(Unsigned32):
    """Custom type fsEcfmRMepIdentifier based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_FsEcfmRMepIdentifier_Type.__name__ = "Unsigned32"
_FsEcfmRMepIdentifier_Object = MibTableColumn
fsEcfmRMepIdentifier = _FsEcfmRMepIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 1, 1, 4),
    _FsEcfmRMepIdentifier_Type()
)
fsEcfmRMepIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsEcfmRMepIdentifier.setStatus("current")
_FsEcfmRMepCcmSequenceNum_Type = Unsigned32
_FsEcfmRMepCcmSequenceNum_Object = MibTableColumn
fsEcfmRMepCcmSequenceNum = _FsEcfmRMepCcmSequenceNum_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 1, 1, 5),
    _FsEcfmRMepCcmSequenceNum_Type()
)
fsEcfmRMepCcmSequenceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEcfmRMepCcmSequenceNum.setStatus("current")
_FsEcfmRMepPortStatusDefect_Type = TruthValue
_FsEcfmRMepPortStatusDefect_Object = MibTableColumn
fsEcfmRMepPortStatusDefect = _FsEcfmRMepPortStatusDefect_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 1, 1, 6),
    _FsEcfmRMepPortStatusDefect_Type()
)
fsEcfmRMepPortStatusDefect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmRMepPortStatusDefect.setStatus("current")
_FsEcfmRMepInterfaceStatusDefect_Type = TruthValue
_FsEcfmRMepInterfaceStatusDefect_Object = MibTableColumn
fsEcfmRMepInterfaceStatusDefect = _FsEcfmRMepInterfaceStatusDefect_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 1, 1, 7),
    _FsEcfmRMepInterfaceStatusDefect_Type()
)
fsEcfmRMepInterfaceStatusDefect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmRMepInterfaceStatusDefect.setStatus("current")
_FsEcfmRMepCcmDefect_Type = TruthValue
_FsEcfmRMepCcmDefect_Object = MibTableColumn
fsEcfmRMepCcmDefect = _FsEcfmRMepCcmDefect_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 1, 1, 8),
    _FsEcfmRMepCcmDefect_Type()
)
fsEcfmRMepCcmDefect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmRMepCcmDefect.setStatus("current")
_FsEcfmRMepRDIDefect_Type = TruthValue
_FsEcfmRMepRDIDefect_Object = MibTableColumn
fsEcfmRMepRDIDefect = _FsEcfmRMepRDIDefect_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 1, 1, 9),
    _FsEcfmRMepRDIDefect_Type()
)
fsEcfmRMepRDIDefect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmRMepRDIDefect.setStatus("current")
_FsEcfmRMepMacAddress_Type = MacAddress
_FsEcfmRMepMacAddress_Object = MibTableColumn
fsEcfmRMepMacAddress = _FsEcfmRMepMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 1, 1, 10),
    _FsEcfmRMepMacAddress_Type()
)
fsEcfmRMepMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmRMepMacAddress.setStatus("current")
_FsEcfmRMepRdi_Type = TruthValue
_FsEcfmRMepRdi_Object = MibTableColumn
fsEcfmRMepRdi = _FsEcfmRMepRdi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 1, 1, 11),
    _FsEcfmRMepRdi_Type()
)
fsEcfmRMepRdi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmRMepRdi.setStatus("current")


class _FsEcfmRMepPortStatusTlv_Type(Dot1agCfmPortStatus):
    """Custom type fsEcfmRMepPortStatusTlv based on Dot1agCfmPortStatus"""
    defaultValue = 0


_FsEcfmRMepPortStatusTlv_Type.__name__ = "Dot1agCfmPortStatus"
_FsEcfmRMepPortStatusTlv_Object = MibTableColumn
fsEcfmRMepPortStatusTlv = _FsEcfmRMepPortStatusTlv_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 1, 1, 12),
    _FsEcfmRMepPortStatusTlv_Type()
)
fsEcfmRMepPortStatusTlv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmRMepPortStatusTlv.setStatus("current")


class _FsEcfmRMepInterfaceStatusTlv_Type(Dot1agCfmInterfaceStatus):
    """Custom type fsEcfmRMepInterfaceStatusTlv based on Dot1agCfmInterfaceStatus"""
    defaultValue = 0


_FsEcfmRMepInterfaceStatusTlv_Type.__name__ = "Dot1agCfmInterfaceStatus"
_FsEcfmRMepInterfaceStatusTlv_Object = MibTableColumn
fsEcfmRMepInterfaceStatusTlv = _FsEcfmRMepInterfaceStatusTlv_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 1, 1, 13),
    _FsEcfmRMepInterfaceStatusTlv_Type()
)
fsEcfmRMepInterfaceStatusTlv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmRMepInterfaceStatusTlv.setStatus("current")


class _FsEcfmRMepChassisIdSubtype_Type(LldpChassisIdSubtype):
    """Custom type fsEcfmRMepChassisIdSubtype based on LldpChassisIdSubtype"""
    defaultValue = 4


_FsEcfmRMepChassisIdSubtype_Type.__name__ = "LldpChassisIdSubtype"
_FsEcfmRMepChassisIdSubtype_Object = MibTableColumn
fsEcfmRMepChassisIdSubtype = _FsEcfmRMepChassisIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 1, 1, 14),
    _FsEcfmRMepChassisIdSubtype_Type()
)
fsEcfmRMepChassisIdSubtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmRMepChassisIdSubtype.setStatus("current")
_FsEcfmMepDbChassisId_Type = LldpChassisId
_FsEcfmMepDbChassisId_Object = MibTableColumn
fsEcfmMepDbChassisId = _FsEcfmMepDbChassisId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 1, 1, 15),
    _FsEcfmMepDbChassisId_Type()
)
fsEcfmMepDbChassisId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmMepDbChassisId.setStatus("current")
_FsEcfmRMepManAddressDomain_Type = TDomain
_FsEcfmRMepManAddressDomain_Object = MibTableColumn
fsEcfmRMepManAddressDomain = _FsEcfmRMepManAddressDomain_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 1, 1, 16),
    _FsEcfmRMepManAddressDomain_Type()
)
fsEcfmRMepManAddressDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmRMepManAddressDomain.setStatus("current")
_FsEcfmRMepManAddress_Type = TAddress
_FsEcfmRMepManAddress_Object = MibTableColumn
fsEcfmRMepManAddress = _FsEcfmRMepManAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 1, 1, 17),
    _FsEcfmRMepManAddress_Type()
)
fsEcfmRMepManAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmRMepManAddress.setStatus("current")
_FsEcfmLtmTable_Object = MibTable
fsEcfmLtmTable = _FsEcfmLtmTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 2)
)
if mibBuilder.loadTexts:
    fsEcfmLtmTable.setStatus("current")
_FsEcfmLtmEntry_Object = MibTableRow
fsEcfmLtmEntry = _FsEcfmLtmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 2, 1)
)
fsEcfmLtmEntry.setIndexNames(
    (0, "ARICENT-ECFM-MIB", "fsEcfmMdIndex"),
    (0, "ARICENT-ECFM-MIB", "fsEcfmMaIndex"),
    (0, "ARICENT-ECFM-MIB", "fsEcfmMepIdentifier"),
    (0, "ARICENT-ECFM-MIB", "fsEcfmLtmSeqNumber"),
)
if mibBuilder.loadTexts:
    fsEcfmLtmEntry.setStatus("current")


class _FsEcfmLtmSeqNumber_Type(Unsigned32):
    """Custom type fsEcfmLtmSeqNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsEcfmLtmSeqNumber_Type.__name__ = "Unsigned32"
_FsEcfmLtmSeqNumber_Object = MibTableColumn
fsEcfmLtmSeqNumber = _FsEcfmLtmSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 2, 1, 1),
    _FsEcfmLtmSeqNumber_Type()
)
fsEcfmLtmSeqNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsEcfmLtmSeqNumber.setStatus("current")
_FsEcfmLtmTargetMacAddress_Type = MacAddress
_FsEcfmLtmTargetMacAddress_Object = MibTableColumn
fsEcfmLtmTargetMacAddress = _FsEcfmLtmTargetMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 2, 1, 2),
    _FsEcfmLtmTargetMacAddress_Type()
)
fsEcfmLtmTargetMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEcfmLtmTargetMacAddress.setStatus("current")


class _FsEcfmLtmTtl_Type(Unsigned32):
    """Custom type fsEcfmLtmTtl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsEcfmLtmTtl_Type.__name__ = "Unsigned32"
_FsEcfmLtmTtl_Object = MibTableColumn
fsEcfmLtmTtl = _FsEcfmLtmTtl_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 2, 1, 3),
    _FsEcfmLtmTtl_Type()
)
fsEcfmLtmTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEcfmLtmTtl.setStatus("current")
_FsEcfmMepExTable_Object = MibTable
fsEcfmMepExTable = _FsEcfmMepExTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 3)
)
if mibBuilder.loadTexts:
    fsEcfmMepExTable.setStatus("current")
_FsEcfmMepExEntry_Object = MibTableRow
fsEcfmMepExEntry = _FsEcfmMepExEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 3, 1)
)
fsEcfmMepExEntry.setIndexNames(
    (0, "ARICENT-ECFM-MIB", "fsEcfmMdIndex"),
    (0, "ARICENT-ECFM-MIB", "fsEcfmMaIndex"),
    (0, "ARICENT-ECFM-MIB", "fsEcfmMepIdentifier"),
)
if mibBuilder.loadTexts:
    fsEcfmMepExEntry.setStatus("current")


class _FsEcfmXconnRMepId_Type(Unsigned32):
    """Custom type fsEcfmXconnRMepId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_FsEcfmXconnRMepId_Type.__name__ = "Unsigned32"
_FsEcfmXconnRMepId_Object = MibTableColumn
fsEcfmXconnRMepId = _FsEcfmXconnRMepId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 3, 1, 1),
    _FsEcfmXconnRMepId_Type()
)
fsEcfmXconnRMepId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmXconnRMepId.setStatus("current")


class _FsEcfmErrorRMepId_Type(Unsigned32):
    """Custom type fsEcfmErrorRMepId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_FsEcfmErrorRMepId_Type.__name__ = "Unsigned32"
_FsEcfmErrorRMepId_Object = MibTableColumn
fsEcfmErrorRMepId = _FsEcfmErrorRMepId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 3, 1, 2),
    _FsEcfmErrorRMepId_Type()
)
fsEcfmErrorRMepId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmErrorRMepId.setStatus("current")
_FsEcfmMepDefectRDICcm_Type = TruthValue
_FsEcfmMepDefectRDICcm_Object = MibTableColumn
fsEcfmMepDefectRDICcm = _FsEcfmMepDefectRDICcm_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 3, 1, 3),
    _FsEcfmMepDefectRDICcm_Type()
)
fsEcfmMepDefectRDICcm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmMepDefectRDICcm.setStatus("current")
_FsEcfmMepDefectMacStatus_Type = TruthValue
_FsEcfmMepDefectMacStatus_Object = MibTableColumn
fsEcfmMepDefectMacStatus = _FsEcfmMepDefectMacStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 3, 1, 4),
    _FsEcfmMepDefectMacStatus_Type()
)
fsEcfmMepDefectMacStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmMepDefectMacStatus.setStatus("current")
_FsEcfmMepDefectRemoteCcm_Type = TruthValue
_FsEcfmMepDefectRemoteCcm_Object = MibTableColumn
fsEcfmMepDefectRemoteCcm = _FsEcfmMepDefectRemoteCcm_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 3, 1, 5),
    _FsEcfmMepDefectRemoteCcm_Type()
)
fsEcfmMepDefectRemoteCcm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmMepDefectRemoteCcm.setStatus("current")
_FsEcfmMepDefectErrorCcm_Type = TruthValue
_FsEcfmMepDefectErrorCcm_Object = MibTableColumn
fsEcfmMepDefectErrorCcm = _FsEcfmMepDefectErrorCcm_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 3, 1, 6),
    _FsEcfmMepDefectErrorCcm_Type()
)
fsEcfmMepDefectErrorCcm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmMepDefectErrorCcm.setStatus("current")
_FsEcfmMepDefectXconnCcm_Type = TruthValue
_FsEcfmMepDefectXconnCcm_Object = MibTableColumn
fsEcfmMepDefectXconnCcm = _FsEcfmMepDefectXconnCcm_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 3, 1, 7),
    _FsEcfmMepDefectXconnCcm_Type()
)
fsEcfmMepDefectXconnCcm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmMepDefectXconnCcm.setStatus("current")


class _FsEcfmMepCcmOffload_Type(Integer32):
    """Custom type fsEcfmMepCcmOffload based on Integer32"""
    defaultValue = 2

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


_FsEcfmMepCcmOffload_Type.__name__ = "Integer32"
_FsEcfmMepCcmOffload_Object = MibTableColumn
fsEcfmMepCcmOffload = _FsEcfmMepCcmOffload_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 3, 1, 8),
    _FsEcfmMepCcmOffload_Type()
)
fsEcfmMepCcmOffload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmMepCcmOffload.setStatus("current")
_FsEcfmMepLbrIn_Type = Unsigned32
_FsEcfmMepLbrIn_Object = MibTableColumn
fsEcfmMepLbrIn = _FsEcfmMepLbrIn_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 3, 1, 9),
    _FsEcfmMepLbrIn_Type()
)
fsEcfmMepLbrIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsEcfmMepLbrIn.setStatus("current")
_FsEcfmMepLbrInOutOfOrder_Type = Unsigned32
_FsEcfmMepLbrInOutOfOrder_Object = MibTableColumn
fsEcfmMepLbrInOutOfOrder = _FsEcfmMepLbrInOutOfOrder_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 3, 1, 10),
    _FsEcfmMepLbrInOutOfOrder_Type()
)
fsEcfmMepLbrInOutOfOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsEcfmMepLbrInOutOfOrder.setStatus("current")
_FsEcfmMepLbrBadMsdu_Type = Unsigned32
_FsEcfmMepLbrBadMsdu_Object = MibTableColumn
fsEcfmMepLbrBadMsdu = _FsEcfmMepLbrBadMsdu_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 3, 1, 11),
    _FsEcfmMepLbrBadMsdu_Type()
)
fsEcfmMepLbrBadMsdu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsEcfmMepLbrBadMsdu.setStatus("current")
_FsEcfmMepUnexpLtrIn_Type = Unsigned32
_FsEcfmMepUnexpLtrIn_Object = MibTableColumn
fsEcfmMepUnexpLtrIn = _FsEcfmMepUnexpLtrIn_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 3, 1, 12),
    _FsEcfmMepUnexpLtrIn_Type()
)
fsEcfmMepUnexpLtrIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsEcfmMepUnexpLtrIn.setStatus("current")
_FsEcfmMepLbrOut_Type = Unsigned32
_FsEcfmMepLbrOut_Object = MibTableColumn
fsEcfmMepLbrOut = _FsEcfmMepLbrOut_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 3, 1, 13),
    _FsEcfmMepLbrOut_Type()
)
fsEcfmMepLbrOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsEcfmMepLbrOut.setStatus("current")
_FsEcfmMepCcmSequenceErrors_Type = Unsigned32
_FsEcfmMepCcmSequenceErrors_Object = MibTableColumn
fsEcfmMepCcmSequenceErrors = _FsEcfmMepCcmSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 3, 1, 14),
    _FsEcfmMepCcmSequenceErrors_Type()
)
fsEcfmMepCcmSequenceErrors.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsEcfmMepCcmSequenceErrors.setStatus("current")
_FsEcfmMepCciSentCcms_Type = Unsigned32
_FsEcfmMepCciSentCcms_Object = MibTableColumn
fsEcfmMepCciSentCcms = _FsEcfmMepCciSentCcms_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 3, 1, 15),
    _FsEcfmMepCciSentCcms_Type()
)
fsEcfmMepCciSentCcms.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsEcfmMepCciSentCcms.setStatus("current")
_FsEcfmMdExTable_Object = MibTable
fsEcfmMdExTable = _FsEcfmMdExTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 4)
)
if mibBuilder.loadTexts:
    fsEcfmMdExTable.setStatus("current")
_FsEcfmMdExEntry_Object = MibTableRow
fsEcfmMdExEntry = _FsEcfmMdExEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 4, 1)
)
fsEcfmMdExEntry.setIndexNames(
    (0, "ARICENT-ECFM-MIB", "fsEcfmMdIndex"),
)
if mibBuilder.loadTexts:
    fsEcfmMdExEntry.setStatus("current")


class _FsEcfmMepArchiveHoldTime_Type(Integer32):
    """Custom type fsEcfmMepArchiveHoldTime based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 65535),
    )


_FsEcfmMepArchiveHoldTime_Type.__name__ = "Integer32"
_FsEcfmMepArchiveHoldTime_Object = MibTableColumn
fsEcfmMepArchiveHoldTime = _FsEcfmMepArchiveHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 4, 1, 1),
    _FsEcfmMepArchiveHoldTime_Type()
)
fsEcfmMepArchiveHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmMepArchiveHoldTime.setStatus("current")
_FsEcfmMaExTable_Object = MibTable
fsEcfmMaExTable = _FsEcfmMaExTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 5)
)
if mibBuilder.loadTexts:
    fsEcfmMaExTable.setStatus("current")
_FsEcfmMaExEntry_Object = MibTableRow
fsEcfmMaExEntry = _FsEcfmMaExEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 5, 1)
)
fsEcfmMaExEntry.setIndexNames(
    (0, "ARICENT-ECFM-MIB", "fsEcfmMdIndex"),
    (0, "ARICENT-ECFM-MIB", "fsEcfmMaIndex"),
)
if mibBuilder.loadTexts:
    fsEcfmMaExEntry.setStatus("current")


class _FsEcfmMaCrosscheckStatus_Type(Integer32):
    """Custom type fsEcfmMaCrosscheckStatus based on Integer32"""
    defaultValue = 1

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


_FsEcfmMaCrosscheckStatus_Type.__name__ = "Integer32"
_FsEcfmMaCrosscheckStatus_Object = MibTableColumn
fsEcfmMaCrosscheckStatus = _FsEcfmMaCrosscheckStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 2, 5, 1, 1),
    _FsEcfmMaCrosscheckStatus_Type()
)
fsEcfmMaCrosscheckStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmMaCrosscheckStatus.setStatus("current")
_FsEcfmTrapsControl_ObjectIdentity = ObjectIdentity
fsEcfmTrapsControl = _FsEcfmTrapsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 150, 3)
)
_FsEcfmTrapControl_Type = FsEcfmSetTraps
_FsEcfmTrapControl_Object = MibScalar
fsEcfmTrapControl = _FsEcfmTrapControl_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 3, 1),
    _FsEcfmTrapControl_Type()
)
fsEcfmTrapControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcfmTrapControl.setStatus("current")


class _FsEcfmTrapType_Type(Integer32):
    """Custom type fsEcfmTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("trapRDICCM", 2),
          ("trapMACStatus", 3),
          ("trapRemoteCCM", 4),
          ("trapErroredCCM", 5),
          ("trapXConnCCM", 6))
    )


_FsEcfmTrapType_Type.__name__ = "Integer32"
_FsEcfmTrapType_Object = MibScalar
fsEcfmTrapType = _FsEcfmTrapType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 150, 3, 2),
    _FsEcfmTrapType_Type()
)
fsEcfmTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEcfmTrapType.setStatus("current")
_FsEcfmTraps_ObjectIdentity = ObjectIdentity
fsEcfmTraps = _FsEcfmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 150, 4)
)
_FutureEcfmTraps_ObjectIdentity = ObjectIdentity
futureEcfmTraps = _FutureEcfmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 150, 4, 0)
)

# Managed Objects groups


# Notification objects

fsEcfmMepDefectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 150, 4, 0, 1)
)
fsEcfmMepDefectTrap.setObjects(
    ("ARICENT-ECFM-MIB", "fsEcfmTrapType")
)
if mibBuilder.loadTexts:
    fsEcfmMepDefectTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-ECFM-MIB",
    **{"FsEcfmOuiType": FsEcfmOuiType,
       "FsEcfmSetTraps": FsEcfmSetTraps,
       "fsecfm": fsecfm,
       "fsEcfmSystem": fsEcfmSystem,
       "fsEcfmSystemControl": fsEcfmSystemControl,
       "fsEcfmModuleStatus": fsEcfmModuleStatus,
       "fsEcfmOui": fsEcfmOui,
       "fsEcfmTraceOption": fsEcfmTraceOption,
       "fsEcfmLtrCacheStatus": fsEcfmLtrCacheStatus,
       "fsEcfmLtrCacheClear": fsEcfmLtrCacheClear,
       "fsEcfmLtrCacheHoldTime": fsEcfmLtrCacheHoldTime,
       "fsEcfmLtrCacheSize": fsEcfmLtrCacheSize,
       "fsEcfmPortTable": fsEcfmPortTable,
       "fsEcfmPortEntry": fsEcfmPortEntry,
       "fsEcfmPortIndex": fsEcfmPortIndex,
       "fsEcfmPortLLCEncapStatus": fsEcfmPortLLCEncapStatus,
       "fsEcfmPortModuleStatus": fsEcfmPortModuleStatus,
       "fsEcfmPortTxCfmPduCount": fsEcfmPortTxCfmPduCount,
       "fsEcfmPortTxCcmCount": fsEcfmPortTxCcmCount,
       "fsEcfmPortTxLbmCount": fsEcfmPortTxLbmCount,
       "fsEcfmPortTxLbrCount": fsEcfmPortTxLbrCount,
       "fsEcfmPortTxLtmCount": fsEcfmPortTxLtmCount,
       "fsEcfmPortTxLtrCount": fsEcfmPortTxLtrCount,
       "fsEcfmPortTxFailedCount": fsEcfmPortTxFailedCount,
       "fsEcfmPortRxCfmPduCount": fsEcfmPortRxCfmPduCount,
       "fsEcfmPortRxCcmCount": fsEcfmPortRxCcmCount,
       "fsEcfmPortRxLbmCount": fsEcfmPortRxLbmCount,
       "fsEcfmPortRxLbrCount": fsEcfmPortRxLbrCount,
       "fsEcfmPortRxLtmCount": fsEcfmPortRxLtmCount,
       "fsEcfmPortRxLtrCount": fsEcfmPortRxLtrCount,
       "fsEcfmPortRxBadCfmPduCount": fsEcfmPortRxBadCfmPduCount,
       "fsEcfmPortFrwdCfmPduCount": fsEcfmPortFrwdCfmPduCount,
       "fsEcfmPortDsrdCfmPduCount": fsEcfmPortDsrdCfmPduCount,
       "fsEcfmMipCcmDbStatus": fsEcfmMipCcmDbStatus,
       "fsEcfmMipCcmDbClear": fsEcfmMipCcmDbClear,
       "fsEcfmMipCcmDbSize": fsEcfmMipCcmDbSize,
       "fsEcfmMipCcmDbHoldTime": fsEcfmMipCcmDbHoldTime,
       "fsEcfmMemoryFailureCount": fsEcfmMemoryFailureCount,
       "fsEcfmBufferFailureCount": fsEcfmBufferFailureCount,
       "fsEcfmUpCount": fsEcfmUpCount,
       "fsEcfmDownCount": fsEcfmDownCount,
       "fsEcfmNoDftCount": fsEcfmNoDftCount,
       "fsEcfmRdiDftCount": fsEcfmRdiDftCount,
       "fsEcfmMacStatusDftCount": fsEcfmMacStatusDftCount,
       "fsEcfmRemoteCcmDftCount": fsEcfmRemoteCcmDftCount,
       "fsEcfmErrorCcmDftCount": fsEcfmErrorCcmDftCount,
       "fsEcfmXconDftCount": fsEcfmXconDftCount,
       "fsEcfmCrosscheckDelay": fsEcfmCrosscheckDelay,
       "fsEcfmMipDynamicEvaluationStatus": fsEcfmMipDynamicEvaluationStatus,
       "fsEcfmMipTable": fsEcfmMipTable,
       "fsEcfmMipEntry": fsEcfmMipEntry,
       "fsEcfmMipIfIndex": fsEcfmMipIfIndex,
       "fsEcfmMipMdLevel": fsEcfmMipMdLevel,
       "fsEcfmMipVid": fsEcfmMipVid,
       "fsEcfmMipActive": fsEcfmMipActive,
       "fsEcfmMipRowStatus": fsEcfmMipRowStatus,
       "fsEcfmMipCcmDbTable": fsEcfmMipCcmDbTable,
       "fsEcfmMipCcmDbEntry": fsEcfmMipCcmDbEntry,
       "fsEcfmMipCcmFid": fsEcfmMipCcmFid,
       "fsEcfmMipCcmSrcAddr": fsEcfmMipCcmSrcAddr,
       "fsEcfmMipCcmIfIndex": fsEcfmMipCcmIfIndex,
       "fsEcfmGlobalCcmOffload": fsEcfmGlobalCcmOffload,
       "fsEcfmDynMipPreventionTable": fsEcfmDynMipPreventionTable,
       "fsEcfmDynMipPreventionEntry": fsEcfmDynMipPreventionEntry,
       "fsEcfmDynMipPreventionRowStatus": fsEcfmDynMipPreventionRowStatus,
       "fsEcfmExObjects": fsEcfmExObjects,
       "fsEcfmRemoteMepDbExTable": fsEcfmRemoteMepDbExTable,
       "fsEcfmRemoteMepDbExEntry": fsEcfmRemoteMepDbExEntry,
       "fsEcfmMdIndex": fsEcfmMdIndex,
       "fsEcfmMaIndex": fsEcfmMaIndex,
       "fsEcfmMepIdentifier": fsEcfmMepIdentifier,
       "fsEcfmRMepIdentifier": fsEcfmRMepIdentifier,
       "fsEcfmRMepCcmSequenceNum": fsEcfmRMepCcmSequenceNum,
       "fsEcfmRMepPortStatusDefect": fsEcfmRMepPortStatusDefect,
       "fsEcfmRMepInterfaceStatusDefect": fsEcfmRMepInterfaceStatusDefect,
       "fsEcfmRMepCcmDefect": fsEcfmRMepCcmDefect,
       "fsEcfmRMepRDIDefect": fsEcfmRMepRDIDefect,
       "fsEcfmRMepMacAddress": fsEcfmRMepMacAddress,
       "fsEcfmRMepRdi": fsEcfmRMepRdi,
       "fsEcfmRMepPortStatusTlv": fsEcfmRMepPortStatusTlv,
       "fsEcfmRMepInterfaceStatusTlv": fsEcfmRMepInterfaceStatusTlv,
       "fsEcfmRMepChassisIdSubtype": fsEcfmRMepChassisIdSubtype,
       "fsEcfmMepDbChassisId": fsEcfmMepDbChassisId,
       "fsEcfmRMepManAddressDomain": fsEcfmRMepManAddressDomain,
       "fsEcfmRMepManAddress": fsEcfmRMepManAddress,
       "fsEcfmLtmTable": fsEcfmLtmTable,
       "fsEcfmLtmEntry": fsEcfmLtmEntry,
       "fsEcfmLtmSeqNumber": fsEcfmLtmSeqNumber,
       "fsEcfmLtmTargetMacAddress": fsEcfmLtmTargetMacAddress,
       "fsEcfmLtmTtl": fsEcfmLtmTtl,
       "fsEcfmMepExTable": fsEcfmMepExTable,
       "fsEcfmMepExEntry": fsEcfmMepExEntry,
       "fsEcfmXconnRMepId": fsEcfmXconnRMepId,
       "fsEcfmErrorRMepId": fsEcfmErrorRMepId,
       "fsEcfmMepDefectRDICcm": fsEcfmMepDefectRDICcm,
       "fsEcfmMepDefectMacStatus": fsEcfmMepDefectMacStatus,
       "fsEcfmMepDefectRemoteCcm": fsEcfmMepDefectRemoteCcm,
       "fsEcfmMepDefectErrorCcm": fsEcfmMepDefectErrorCcm,
       "fsEcfmMepDefectXconnCcm": fsEcfmMepDefectXconnCcm,
       "fsEcfmMepCcmOffload": fsEcfmMepCcmOffload,
       "fsEcfmMepLbrIn": fsEcfmMepLbrIn,
       "fsEcfmMepLbrInOutOfOrder": fsEcfmMepLbrInOutOfOrder,
       "fsEcfmMepLbrBadMsdu": fsEcfmMepLbrBadMsdu,
       "fsEcfmMepUnexpLtrIn": fsEcfmMepUnexpLtrIn,
       "fsEcfmMepLbrOut": fsEcfmMepLbrOut,
       "fsEcfmMepCcmSequenceErrors": fsEcfmMepCcmSequenceErrors,
       "fsEcfmMepCciSentCcms": fsEcfmMepCciSentCcms,
       "fsEcfmMdExTable": fsEcfmMdExTable,
       "fsEcfmMdExEntry": fsEcfmMdExEntry,
       "fsEcfmMepArchiveHoldTime": fsEcfmMepArchiveHoldTime,
       "fsEcfmMaExTable": fsEcfmMaExTable,
       "fsEcfmMaExEntry": fsEcfmMaExEntry,
       "fsEcfmMaCrosscheckStatus": fsEcfmMaCrosscheckStatus,
       "fsEcfmTrapsControl": fsEcfmTrapsControl,
       "fsEcfmTrapControl": fsEcfmTrapControl,
       "fsEcfmTrapType": fsEcfmTrapType,
       "fsEcfmTraps": fsEcfmTraps,
       "futureEcfmTraps": futureEcfmTraps,
       "fsEcfmMepDefectTrap": fsEcfmMepDefectTrap}
)
