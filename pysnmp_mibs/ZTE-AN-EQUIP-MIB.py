# SNMP MIB module (ZTE-AN-EQUIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-EQUIP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:43 2025
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(zxAn,) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "zxAn")


# MODULE-IDENTITY

zxAnEquipMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnEquipObjects_ObjectIdentity = ObjectIdentity
zxAnEquipObjects = _ZxAnEquipObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1)
)
_ZxAnChassisMgmt_ObjectIdentity = ObjectIdentity
zxAnChassisMgmt = _ZxAnChassisMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1)
)
_ZxAnRackTable_Object = MibTable
zxAnRackTable = _ZxAnRackTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    zxAnRackTable.setStatus("current")
_ZxAnRackEntry_Object = MibTableRow
zxAnRackEntry = _ZxAnRackEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 1, 1)
)
zxAnRackEntry.setIndexNames(
    (0, "ZTE-AN-EQUIP-MIB", "zxAnRackNo"),
)
if mibBuilder.loadTexts:
    zxAnRackEntry.setStatus("current")
_ZxAnRackNo_Type = Integer32
_ZxAnRackNo_Object = MibTableColumn
zxAnRackNo = _ZxAnRackNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 1, 1, 1),
    _ZxAnRackNo_Type()
)
zxAnRackNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnRackNo.setStatus("current")
_ZxAnRackActType_Type = Integer32
_ZxAnRackActType_Object = MibTableColumn
zxAnRackActType = _ZxAnRackActType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 1, 1, 2),
    _ZxAnRackActType_Type()
)
zxAnRackActType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnRackActType.setStatus("current")
_ZxAnRackCfgType_Type = Integer32
_ZxAnRackCfgType_Object = MibTableColumn
zxAnRackCfgType = _ZxAnRackCfgType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 1, 1, 3),
    _ZxAnRackCfgType_Type()
)
zxAnRackCfgType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRackCfgType.setStatus("current")


class _ZxAnRackInvSn_Type(DisplayString):
    """Custom type zxAnRackInvSn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnRackInvSn_Type.__name__ = "DisplayString"
_ZxAnRackInvSn_Object = MibTableColumn
zxAnRackInvSn = _ZxAnRackInvSn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 1, 1, 4),
    _ZxAnRackInvSn_Type()
)
zxAnRackInvSn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRackInvSn.setStatus("current")
_ZxAnRackRowStatus_Type = RowStatus
_ZxAnRackRowStatus_Object = MibTableColumn
zxAnRackRowStatus = _ZxAnRackRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 1, 1, 5),
    _ZxAnRackRowStatus_Type()
)
zxAnRackRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRackRowStatus.setStatus("current")
_ZxAnShelfTable_Object = MibTable
zxAnShelfTable = _ZxAnShelfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    zxAnShelfTable.setStatus("current")
_ZxAnShelfEntry_Object = MibTableRow
zxAnShelfEntry = _ZxAnShelfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 2, 1)
)
zxAnShelfEntry.setIndexNames(
    (0, "ZTE-AN-EQUIP-MIB", "zxAnRackNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnShelfNo"),
)
if mibBuilder.loadTexts:
    zxAnShelfEntry.setStatus("current")
_ZxAnShelfNo_Type = Integer32
_ZxAnShelfNo_Object = MibTableColumn
zxAnShelfNo = _ZxAnShelfNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 2, 1, 1),
    _ZxAnShelfNo_Type()
)
zxAnShelfNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnShelfNo.setStatus("current")


class _ZxAnShelfHardVersion_Type(DisplayString):
    """Custom type zxAnShelfHardVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnShelfHardVersion_Type.__name__ = "DisplayString"
_ZxAnShelfHardVersion_Object = MibTableColumn
zxAnShelfHardVersion = _ZxAnShelfHardVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 2, 1, 2),
    _ZxAnShelfHardVersion_Type()
)
zxAnShelfHardVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnShelfHardVersion.setStatus("current")
_ZxAnShelfActType_Type = Integer32
_ZxAnShelfActType_Object = MibTableColumn
zxAnShelfActType = _ZxAnShelfActType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 2, 1, 3),
    _ZxAnShelfActType_Type()
)
zxAnShelfActType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnShelfActType.setStatus("current")
_ZxAnShelfCfgType_Type = Integer32
_ZxAnShelfCfgType_Object = MibTableColumn
zxAnShelfCfgType = _ZxAnShelfCfgType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 2, 1, 4),
    _ZxAnShelfCfgType_Type()
)
zxAnShelfCfgType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnShelfCfgType.setStatus("current")


class _ZxAnShelfInvSn_Type(DisplayString):
    """Custom type zxAnShelfInvSn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnShelfInvSn_Type.__name__ = "DisplayString"
_ZxAnShelfInvSn_Object = MibTableColumn
zxAnShelfInvSn = _ZxAnShelfInvSn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 2, 1, 5),
    _ZxAnShelfInvSn_Type()
)
zxAnShelfInvSn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnShelfInvSn.setStatus("current")


class _ZxAnShelfCleiCode_Type(DisplayString):
    """Custom type zxAnShelfCleiCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnShelfCleiCode_Type.__name__ = "DisplayString"
_ZxAnShelfCleiCode_Object = MibTableColumn
zxAnShelfCleiCode = _ZxAnShelfCleiCode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 2, 1, 6),
    _ZxAnShelfCleiCode_Type()
)
zxAnShelfCleiCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnShelfCleiCode.setStatus("current")
_ZxAnLogicShelfNo_Type = Integer32
_ZxAnLogicShelfNo_Object = MibTableColumn
zxAnLogicShelfNo = _ZxAnLogicShelfNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 2, 1, 7),
    _ZxAnLogicShelfNo_Type()
)
zxAnLogicShelfNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnLogicShelfNo.setStatus("current")


class _ZxAnShelfHardwareType_Type(DisplayString):
    """Custom type zxAnShelfHardwareType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnShelfHardwareType_Type.__name__ = "DisplayString"
_ZxAnShelfHardwareType_Object = MibTableColumn
zxAnShelfHardwareType = _ZxAnShelfHardwareType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 2, 1, 8),
    _ZxAnShelfHardwareType_Type()
)
zxAnShelfHardwareType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnShelfHardwareType.setStatus("current")


class _ZxAnShelfAlias_Type(DisplayString):
    """Custom type zxAnShelfAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnShelfAlias_Type.__name__ = "DisplayString"
_ZxAnShelfAlias_Object = MibTableColumn
zxAnShelfAlias = _ZxAnShelfAlias_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 2, 1, 9),
    _ZxAnShelfAlias_Type()
)
zxAnShelfAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnShelfAlias.setStatus("current")


class _ZxAnShelfAdminStatus_Type(Integer32):
    """Custom type zxAnShelfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reboot", 1)
    )


_ZxAnShelfAdminStatus_Type.__name__ = "Integer32"
_ZxAnShelfAdminStatus_Object = MibTableColumn
zxAnShelfAdminStatus = _ZxAnShelfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 2, 1, 10),
    _ZxAnShelfAdminStatus_Type()
)
zxAnShelfAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnShelfAdminStatus.setStatus("current")
_ZxAnShelfRowStatus_Type = RowStatus
_ZxAnShelfRowStatus_Object = MibTableColumn
zxAnShelfRowStatus = _ZxAnShelfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 2, 1, 15),
    _ZxAnShelfRowStatus_Type()
)
zxAnShelfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnShelfRowStatus.setStatus("current")
_ZxAnCardTable_Object = MibTable
zxAnCardTable = _ZxAnCardTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    zxAnCardTable.setStatus("current")
_ZxAnCardEntry_Object = MibTableRow
zxAnCardEntry = _ZxAnCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 3, 1)
)
zxAnCardEntry.setIndexNames(
    (0, "ZTE-AN-EQUIP-MIB", "zxAnRackNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnShelfNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnSlotNo"),
)
if mibBuilder.loadTexts:
    zxAnCardEntry.setStatus("current")
_ZxAnSlotNo_Type = Integer32
_ZxAnSlotNo_Object = MibTableColumn
zxAnSlotNo = _ZxAnSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 3, 1, 1),
    _ZxAnSlotNo_Type()
)
zxAnSlotNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSlotNo.setStatus("current")
_ZxAnCardConfMainType_Type = Integer32
_ZxAnCardConfMainType_Object = MibTableColumn
zxAnCardConfMainType = _ZxAnCardConfMainType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 3, 1, 2),
    _ZxAnCardConfMainType_Type()
)
zxAnCardConfMainType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCardConfMainType.setStatus("current")
_ZxAnCardActMainType_Type = Integer32
_ZxAnCardActMainType_Object = MibTableColumn
zxAnCardActMainType = _ZxAnCardActMainType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 3, 1, 3),
    _ZxAnCardActMainType_Type()
)
zxAnCardActMainType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardActMainType.setStatus("current")


class _ZxAnCardActType_Type(DisplayString):
    """Custom type zxAnCardActType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnCardActType_Type.__name__ = "DisplayString"
_ZxAnCardActType_Object = MibTableColumn
zxAnCardActType = _ZxAnCardActType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 3, 1, 4),
    _ZxAnCardActType_Type()
)
zxAnCardActType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardActType.setStatus("current")


class _ZxAnCardOperStatus_Type(Integer32):
    """Custom type zxAnCardOperStatus based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("notInService", 2),
          ("hwOnline", 3),
          ("hwOffline", 4),
          ("configuring", 5),
          ("configFailed", 6),
          ("typeMismatch", 7),
          ("deactived", 8),
          ("faulty", 9),
          ("invalid", 10),
          ("noPower", 11))
    )


_ZxAnCardOperStatus_Type.__name__ = "Integer32"
_ZxAnCardOperStatus_Object = MibTableColumn
zxAnCardOperStatus = _ZxAnCardOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 3, 1, 5),
    _ZxAnCardOperStatus_Type()
)
zxAnCardOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardOperStatus.setStatus("current")


class _ZxAnCardAdminStatus_Type(Integer32):
    """Custom type zxAnCardAdminStatus based on Integer32"""
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
        *(("reset", 1),
          ("switch", 2),
          ("stopService", 3),
          ("active", 4),
          ("deactive", 5))
    )


_ZxAnCardAdminStatus_Type.__name__ = "Integer32"
_ZxAnCardAdminStatus_Object = MibTableColumn
zxAnCardAdminStatus = _ZxAnCardAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 3, 1, 6),
    _ZxAnCardAdminStatus_Type()
)
zxAnCardAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCardAdminStatus.setStatus("current")
_ZxAnCardPortNums_Type = Integer32
_ZxAnCardPortNums_Object = MibTableColumn
zxAnCardPortNums = _ZxAnCardPortNums_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 3, 1, 7),
    _ZxAnCardPortNums_Type()
)
zxAnCardPortNums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardPortNums.setStatus("current")
_ZxAnCardActivePortNums_Type = Integer32
_ZxAnCardActivePortNums_Object = MibTableColumn
zxAnCardActivePortNums = _ZxAnCardActivePortNums_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 3, 1, 8),
    _ZxAnCardActivePortNums_Type()
)
zxAnCardActivePortNums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardActivePortNums.setStatus("current")
_ZxAnCardCpuLoad_Type = Integer32
_ZxAnCardCpuLoad_Object = MibTableColumn
zxAnCardCpuLoad = _ZxAnCardCpuLoad_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 3, 1, 9),
    _ZxAnCardCpuLoad_Type()
)
zxAnCardCpuLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardCpuLoad.setStatus("current")
if mibBuilder.loadTexts:
    zxAnCardCpuLoad.setUnits("percent")
_ZxAnCardCpuLoadThreshold_Type = Integer32
_ZxAnCardCpuLoadThreshold_Object = MibTableColumn
zxAnCardCpuLoadThreshold = _ZxAnCardCpuLoadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 3, 1, 10),
    _ZxAnCardCpuLoadThreshold_Type()
)
zxAnCardCpuLoadThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCardCpuLoadThreshold.setStatus("current")
if mibBuilder.loadTexts:
    zxAnCardCpuLoadThreshold.setUnits("percent")
_ZxAnCardMemUsage_Type = Integer32
_ZxAnCardMemUsage_Object = MibTableColumn
zxAnCardMemUsage = _ZxAnCardMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 3, 1, 11),
    _ZxAnCardMemUsage_Type()
)
zxAnCardMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardMemUsage.setStatus("current")
if mibBuilder.loadTexts:
    zxAnCardMemUsage.setUnits("percent")
_ZxAnCardMemUsageThreshold_Type = Integer32
_ZxAnCardMemUsageThreshold_Object = MibTableColumn
zxAnCardMemUsageThreshold = _ZxAnCardMemUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 3, 1, 12),
    _ZxAnCardMemUsageThreshold_Type()
)
zxAnCardMemUsageThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCardMemUsageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    zxAnCardMemUsageThreshold.setUnits("percent")


class _ZxAnCardStandbyStatus_Type(Integer32):
    """Custom type zxAnCardStandbyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              15)
        )
    )
    namedValues = NamedValues(
        *(("main", 1),
          ("standby", 2),
          ("unknown", 15))
    )


_ZxAnCardStandbyStatus_Type.__name__ = "Integer32"
_ZxAnCardStandbyStatus_Object = MibTableColumn
zxAnCardStandbyStatus = _ZxAnCardStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 3, 1, 13),
    _ZxAnCardStandbyStatus_Type()
)
zxAnCardStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardStandbyStatus.setStatus("current")


class _ZxAnCardInvSn_Type(DisplayString):
    """Custom type zxAnCardInvSn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnCardInvSn_Type.__name__ = "DisplayString"
_ZxAnCardInvSn_Object = MibTableColumn
zxAnCardInvSn = _ZxAnCardInvSn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 3, 1, 14),
    _ZxAnCardInvSn_Type()
)
zxAnCardInvSn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCardInvSn.setStatus("current")


class _ZxAnCardCleiCode_Type(DisplayString):
    """Custom type zxAnCardCleiCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnCardCleiCode_Type.__name__ = "DisplayString"
_ZxAnCardCleiCode_Object = MibTableColumn
zxAnCardCleiCode = _ZxAnCardCleiCode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 3, 1, 15),
    _ZxAnCardCleiCode_Type()
)
zxAnCardCleiCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardCleiCode.setStatus("current")


class _ZxAnCardAccessoriesType_Type(DisplayString):
    """Custom type zxAnCardAccessoriesType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnCardAccessoriesType_Type.__name__ = "DisplayString"
_ZxAnCardAccessoriesType_Object = MibTableColumn
zxAnCardAccessoriesType = _ZxAnCardAccessoriesType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 3, 1, 16),
    _ZxAnCardAccessoriesType_Type()
)
zxAnCardAccessoriesType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardAccessoriesType.setStatus("current")


class _ZxAnCardAccessoriesOperstatus_Type(Integer32):
    """Custom type zxAnCardAccessoriesOperstatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("unknow", 4))
    )


_ZxAnCardAccessoriesOperstatus_Type.__name__ = "Integer32"
_ZxAnCardAccessoriesOperstatus_Object = MibTableColumn
zxAnCardAccessoriesOperstatus = _ZxAnCardAccessoriesOperstatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 3, 1, 17),
    _ZxAnCardAccessoriesOperstatus_Type()
)
zxAnCardAccessoriesOperstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardAccessoriesOperstatus.setStatus("current")


class _ZxAnCardLockStatus_Type(Integer32):
    """Custom type zxAnCardLockStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lock", 1),
          ("unlock", 2))
    )


_ZxAnCardLockStatus_Type.__name__ = "Integer32"
_ZxAnCardLockStatus_Object = MibTableColumn
zxAnCardLockStatus = _ZxAnCardLockStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 3, 1, 18),
    _ZxAnCardLockStatus_Type()
)
zxAnCardLockStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCardLockStatus.setStatus("current")
_ZxAnCardMemSize_Type = Integer32
_ZxAnCardMemSize_Object = MibTableColumn
zxAnCardMemSize = _ZxAnCardMemSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 3, 1, 19),
    _ZxAnCardMemSize_Type()
)
zxAnCardMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardMemSize.setStatus("current")
if mibBuilder.loadTexts:
    zxAnCardMemSize.setUnits("MB")


class _ZxAnCardCpldUpdateStatus_Type(Integer32):
    """Custom type zxAnCardCpldUpdateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_ZxAnCardCpldUpdateStatus_Type.__name__ = "Integer32"
_ZxAnCardCpldUpdateStatus_Object = MibTableColumn
zxAnCardCpldUpdateStatus = _ZxAnCardCpldUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 3, 1, 20),
    _ZxAnCardCpldUpdateStatus_Type()
)
zxAnCardCpldUpdateStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCardCpldUpdateStatus.setStatus("current")
_ZxAnCardAvailableStorageSize_Type = Integer32
_ZxAnCardAvailableStorageSize_Object = MibTableColumn
zxAnCardAvailableStorageSize = _ZxAnCardAvailableStorageSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 3, 1, 21),
    _ZxAnCardAvailableStorageSize_Type()
)
zxAnCardAvailableStorageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardAvailableStorageSize.setStatus("current")
if mibBuilder.loadTexts:
    zxAnCardAvailableStorageSize.setUnits("KB")
_ZxAnCardTotalStorageSize_Type = Integer32
_ZxAnCardTotalStorageSize_Object = MibTableColumn
zxAnCardTotalStorageSize = _ZxAnCardTotalStorageSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 3, 1, 22),
    _ZxAnCardTotalStorageSize_Type()
)
zxAnCardTotalStorageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardTotalStorageSize.setStatus("current")
if mibBuilder.loadTexts:
    zxAnCardTotalStorageSize.setUnits("KB")
_ZxAnCardEnergySavingEnable_Type = TruthValue
_ZxAnCardEnergySavingEnable_Object = MibTableColumn
zxAnCardEnergySavingEnable = _ZxAnCardEnergySavingEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 3, 1, 24),
    _ZxAnCardEnergySavingEnable_Type()
)
zxAnCardEnergySavingEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCardEnergySavingEnable.setStatus("current")


class _ZxAnCardAlias_Type(DisplayString):
    """Custom type zxAnCardAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnCardAlias_Type.__name__ = "DisplayString"
_ZxAnCardAlias_Object = MibTableColumn
zxAnCardAlias = _ZxAnCardAlias_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 3, 1, 25),
    _ZxAnCardAlias_Type()
)
zxAnCardAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCardAlias.setStatus("current")
_ZxAnCardLastStartupTime_Type = DateAndTime
_ZxAnCardLastStartupTime_Object = MibTableColumn
zxAnCardLastStartupTime = _ZxAnCardLastStartupTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 3, 1, 26),
    _ZxAnCardLastStartupTime_Type()
)
zxAnCardLastStartupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardLastStartupTime.setStatus("current")
_ZxAnCardRowStatus_Type = RowStatus
_ZxAnCardRowStatus_Object = MibTableColumn
zxAnCardRowStatus = _ZxAnCardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 3, 1, 30),
    _ZxAnCardRowStatus_Type()
)
zxAnCardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCardRowStatus.setStatus("current")
_ZxAnSubcardTable_Object = MibTable
zxAnSubcardTable = _ZxAnSubcardTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    zxAnSubcardTable.setStatus("current")
_ZxAnSubcardEntry_Object = MibTableRow
zxAnSubcardEntry = _ZxAnSubcardEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 4, 1)
)
zxAnSubcardEntry.setIndexNames(
    (0, "ZTE-AN-EQUIP-MIB", "zxAnRackNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnShelfNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnSlotNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnSubcardNo"),
)
if mibBuilder.loadTexts:
    zxAnSubcardEntry.setStatus("current")
_ZxAnSubcardNo_Type = Integer32
_ZxAnSubcardNo_Object = MibTableColumn
zxAnSubcardNo = _ZxAnSubcardNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 4, 1, 1),
    _ZxAnSubcardNo_Type()
)
zxAnSubcardNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSubcardNo.setStatus("current")
_ZxAnSubCardCfgMainType_Type = Integer32
_ZxAnSubCardCfgMainType_Object = MibTableColumn
zxAnSubCardCfgMainType = _ZxAnSubCardCfgMainType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 4, 1, 2),
    _ZxAnSubCardCfgMainType_Type()
)
zxAnSubCardCfgMainType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSubCardCfgMainType.setStatus("current")
_ZxAnSubCardActMainType_Type = Integer32
_ZxAnSubCardActMainType_Object = MibTableColumn
zxAnSubCardActMainType = _ZxAnSubCardActMainType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 4, 1, 3),
    _ZxAnSubCardActMainType_Type()
)
zxAnSubCardActMainType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSubCardActMainType.setStatus("current")


class _ZxAnSubCardActType_Type(DisplayString):
    """Custom type zxAnSubCardActType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnSubCardActType_Type.__name__ = "DisplayString"
_ZxAnSubCardActType_Object = MibTableColumn
zxAnSubCardActType = _ZxAnSubCardActType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 4, 1, 4),
    _ZxAnSubCardActType_Type()
)
zxAnSubCardActType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSubCardActType.setStatus("current")


class _ZxAnSubcardOperStatus_Type(Integer32):
    """Custom type zxAnSubcardOperStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("notInService", 2),
          ("hwOnline", 3),
          ("hwOffline", 4),
          ("configuring", 5),
          ("configFailed", 6),
          ("typeMismatch", 7),
          ("deactived", 8),
          ("faulty", 9),
          ("invalid", 10))
    )


_ZxAnSubcardOperStatus_Type.__name__ = "Integer32"
_ZxAnSubcardOperStatus_Object = MibTableColumn
zxAnSubcardOperStatus = _ZxAnSubcardOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 4, 1, 5),
    _ZxAnSubcardOperStatus_Type()
)
zxAnSubcardOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSubcardOperStatus.setStatus("current")


class _ZxAnSubcardAdminStatus_Type(Integer32):
    """Custom type zxAnSubcardAdminStatus based on Integer32"""
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
        *(("reset", 1),
          ("switch", 2),
          ("stopService", 3),
          ("active", 4),
          ("deactive", 5))
    )


_ZxAnSubcardAdminStatus_Type.__name__ = "Integer32"
_ZxAnSubcardAdminStatus_Object = MibTableColumn
zxAnSubcardAdminStatus = _ZxAnSubcardAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 4, 1, 6),
    _ZxAnSubcardAdminStatus_Type()
)
zxAnSubcardAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSubcardAdminStatus.setStatus("current")
_ZxAnSubcardPortNums_Type = Integer32
_ZxAnSubcardPortNums_Object = MibTableColumn
zxAnSubcardPortNums = _ZxAnSubcardPortNums_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 4, 1, 7),
    _ZxAnSubcardPortNums_Type()
)
zxAnSubcardPortNums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSubcardPortNums.setStatus("current")
_ZxAnSubcardActivePortNums_Type = Integer32
_ZxAnSubcardActivePortNums_Object = MibTableColumn
zxAnSubcardActivePortNums = _ZxAnSubcardActivePortNums_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 4, 1, 8),
    _ZxAnSubcardActivePortNums_Type()
)
zxAnSubcardActivePortNums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSubcardActivePortNums.setStatus("current")
_ZxAnSubcardCpuLoad_Type = Integer32
_ZxAnSubcardCpuLoad_Object = MibTableColumn
zxAnSubcardCpuLoad = _ZxAnSubcardCpuLoad_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 4, 1, 9),
    _ZxAnSubcardCpuLoad_Type()
)
zxAnSubcardCpuLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSubcardCpuLoad.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSubcardCpuLoad.setUnits("percent")
_ZxAnSubcardMemUsage_Type = Integer32
_ZxAnSubcardMemUsage_Object = MibTableColumn
zxAnSubcardMemUsage = _ZxAnSubcardMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 4, 1, 10),
    _ZxAnSubcardMemUsage_Type()
)
zxAnSubcardMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSubcardMemUsage.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSubcardMemUsage.setUnits("percent")


class _ZxAnSubcardInvSn_Type(DisplayString):
    """Custom type zxAnSubcardInvSn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSubcardInvSn_Type.__name__ = "DisplayString"
_ZxAnSubcardInvSn_Object = MibTableColumn
zxAnSubcardInvSn = _ZxAnSubcardInvSn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 4, 1, 11),
    _ZxAnSubcardInvSn_Type()
)
zxAnSubcardInvSn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSubcardInvSn.setStatus("current")


class _ZxAnSubcardCleiCode_Type(DisplayString):
    """Custom type zxAnSubcardCleiCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSubcardCleiCode_Type.__name__ = "DisplayString"
_ZxAnSubcardCleiCode_Object = MibTableColumn
zxAnSubcardCleiCode = _ZxAnSubcardCleiCode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 4, 1, 12),
    _ZxAnSubcardCleiCode_Type()
)
zxAnSubcardCleiCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSubcardCleiCode.setStatus("current")
_ZxAnSubcardMemSize_Type = Integer32
_ZxAnSubcardMemSize_Object = MibTableColumn
zxAnSubcardMemSize = _ZxAnSubcardMemSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 4, 1, 13),
    _ZxAnSubcardMemSize_Type()
)
zxAnSubcardMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSubcardMemSize.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSubcardMemSize.setUnits("MB")


class _ZxAnSubcardCpldUpdateStatus_Type(Integer32):
    """Custom type zxAnSubcardCpldUpdateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_ZxAnSubcardCpldUpdateStatus_Type.__name__ = "Integer32"
_ZxAnSubcardCpldUpdateStatus_Object = MibTableColumn
zxAnSubcardCpldUpdateStatus = _ZxAnSubcardCpldUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 4, 1, 14),
    _ZxAnSubcardCpldUpdateStatus_Type()
)
zxAnSubcardCpldUpdateStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSubcardCpldUpdateStatus.setStatus("current")
_ZxAnSubcardRowStatus_Type = RowStatus
_ZxAnSubcardRowStatus_Object = MibTableColumn
zxAnSubcardRowStatus = _ZxAnSubcardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 4, 1, 20),
    _ZxAnSubcardRowStatus_Type()
)
zxAnSubcardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSubcardRowStatus.setStatus("current")
_ZxAnPhyConfMgmt_ObjectIdentity = ObjectIdentity
zxAnPhyConfMgmt = _ZxAnPhyConfMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 5)
)
_ZxAnStandbyEnableTable_Object = MibTable
zxAnStandbyEnableTable = _ZxAnStandbyEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    zxAnStandbyEnableTable.setStatus("current")
_ZxAnStandbyEnableEntry_Object = MibTableRow
zxAnStandbyEnableEntry = _ZxAnStandbyEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 5, 2, 1)
)
zxAnStandbyEnableEntry.setIndexNames(
    (0, "ZTE-AN-EQUIP-MIB", "zxAnRackNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnShelfNo"),
)
if mibBuilder.loadTexts:
    zxAnStandbyEnableEntry.setStatus("current")


class _ZxStandbyEnable_Type(Integer32):
    """Custom type zxStandbyEnable based on Integer32"""
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


_ZxStandbyEnable_Type.__name__ = "Integer32"
_ZxStandbyEnable_Object = MibTableColumn
zxStandbyEnable = _ZxStandbyEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 5, 2, 1, 1),
    _ZxStandbyEnable_Type()
)
zxStandbyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxStandbyEnable.setStatus("current")


class _ZxAnChassisPnpMode_Type(Integer32):
    """Custom type zxAnChassisPnpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pNPMode", 1),
          ("v3Mode", 2))
    )


_ZxAnChassisPnpMode_Type.__name__ = "Integer32"
_ZxAnChassisPnpMode_Object = MibScalar
zxAnChassisPnpMode = _ZxAnChassisPnpMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 5, 5),
    _ZxAnChassisPnpMode_Type()
)
zxAnChassisPnpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnChassisPnpMode.setStatus("current")
_ZxAnPowerSupplyCardTable_Object = MibTable
zxAnPowerSupplyCardTable = _ZxAnPowerSupplyCardTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 6)
)
if mibBuilder.loadTexts:
    zxAnPowerSupplyCardTable.setStatus("current")
_ZxAnPowerSupplyCardEntry_Object = MibTableRow
zxAnPowerSupplyCardEntry = _ZxAnPowerSupplyCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 6, 1)
)
zxAnPowerSupplyCardEntry.setIndexNames(
    (0, "ZTE-AN-EQUIP-MIB", "zxAnRackNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnShelfNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnSlotNo"),
)
if mibBuilder.loadTexts:
    zxAnPowerSupplyCardEntry.setStatus("current")


class _ZxAnPowerSupplyCardPreviousType_Type(DisplayString):
    """Custom type zxAnPowerSupplyCardPreviousType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnPowerSupplyCardPreviousType_Type.__name__ = "DisplayString"
_ZxAnPowerSupplyCardPreviousType_Object = MibTableColumn
zxAnPowerSupplyCardPreviousType = _ZxAnPowerSupplyCardPreviousType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 6, 1, 1),
    _ZxAnPowerSupplyCardPreviousType_Type()
)
zxAnPowerSupplyCardPreviousType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zxAnPowerSupplyCardPreviousType.setStatus("current")


class _ZxAnPowerSupplyCardCurrentType_Type(DisplayString):
    """Custom type zxAnPowerSupplyCardCurrentType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnPowerSupplyCardCurrentType_Type.__name__ = "DisplayString"
_ZxAnPowerSupplyCardCurrentType_Object = MibTableColumn
zxAnPowerSupplyCardCurrentType = _ZxAnPowerSupplyCardCurrentType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 1, 6, 1, 2),
    _ZxAnPowerSupplyCardCurrentType_Type()
)
zxAnPowerSupplyCardCurrentType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zxAnPowerSupplyCardCurrentType.setStatus("current")
_ZxAnVerMgmt_ObjectIdentity = ObjectIdentity
zxAnVerMgmt = _ZxAnVerMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2)
)
_ZxAnVerFtpMgmt_ObjectIdentity = ObjectIdentity
zxAnVerFtpMgmt = _ZxAnVerFtpMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 1)
)


class _ZxAnFtpVerFileType_Type(Integer32):
    """Custom type zxAnFtpVerFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("areaFile", 1),
          ("updateFile", 2),
          ("mpVersion", 3))
    )


_ZxAnFtpVerFileType_Type.__name__ = "Integer32"
_ZxAnFtpVerFileType_Object = MibScalar
zxAnFtpVerFileType = _ZxAnFtpVerFileType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 1, 1),
    _ZxAnFtpVerFileType_Type()
)
zxAnFtpVerFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFtpVerFileType.setStatus("current")
_ZxAnFtpVerClntOperType_Type = Integer32
_ZxAnFtpVerClntOperType_Object = MibScalar
zxAnFtpVerClntOperType = _ZxAnFtpVerClntOperType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 1, 2),
    _ZxAnFtpVerClntOperType_Type()
)
zxAnFtpVerClntOperType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFtpVerClntOperType.setStatus("current")
_ZxAnFtpVerServerIpAddress_Type = IpAddress
_ZxAnFtpVerServerIpAddress_Object = MibScalar
zxAnFtpVerServerIpAddress = _ZxAnFtpVerServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 1, 3),
    _ZxAnFtpVerServerIpAddress_Type()
)
zxAnFtpVerServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFtpVerServerIpAddress.setStatus("current")


class _ZxAnFtpVerServerUserName_Type(DisplayString):
    """Custom type zxAnFtpVerServerUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnFtpVerServerUserName_Type.__name__ = "DisplayString"
_ZxAnFtpVerServerUserName_Object = MibScalar
zxAnFtpVerServerUserName = _ZxAnFtpVerServerUserName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 1, 4),
    _ZxAnFtpVerServerUserName_Type()
)
zxAnFtpVerServerUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFtpVerServerUserName.setStatus("current")


class _ZxAnFtpVerServerUserPwd_Type(DisplayString):
    """Custom type zxAnFtpVerServerUserPwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnFtpVerServerUserPwd_Type.__name__ = "DisplayString"
_ZxAnFtpVerServerUserPwd_Object = MibScalar
zxAnFtpVerServerUserPwd = _ZxAnFtpVerServerUserPwd_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 1, 5),
    _ZxAnFtpVerServerUserPwd_Type()
)
zxAnFtpVerServerUserPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFtpVerServerUserPwd.setStatus("current")


class _ZxAnFtpVerServerFilePath_Type(DisplayString):
    """Custom type zxAnFtpVerServerFilePath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnFtpVerServerFilePath_Type.__name__ = "DisplayString"
_ZxAnFtpVerServerFilePath_Object = MibScalar
zxAnFtpVerServerFilePath = _ZxAnFtpVerServerFilePath_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 1, 6),
    _ZxAnFtpVerServerFilePath_Type()
)
zxAnFtpVerServerFilePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFtpVerServerFilePath.setStatus("current")


class _ZxAnFtpVerServerFileName_Type(DisplayString):
    """Custom type zxAnFtpVerServerFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnFtpVerServerFileName_Type.__name__ = "DisplayString"
_ZxAnFtpVerServerFileName_Object = MibScalar
zxAnFtpVerServerFileName = _ZxAnFtpVerServerFileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 1, 7),
    _ZxAnFtpVerServerFileName_Type()
)
zxAnFtpVerServerFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFtpVerServerFileName.setStatus("current")


class _ZxAnFtpVerClntAdminStatus_Type(Integer32):
    """Custom type zxAnFtpVerClntAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("cancleCurrentFtpSession", 1)
    )


_ZxAnFtpVerClntAdminStatus_Type.__name__ = "Integer32"
_ZxAnFtpVerClntAdminStatus_Object = MibScalar
zxAnFtpVerClntAdminStatus = _ZxAnFtpVerClntAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 1, 8),
    _ZxAnFtpVerClntAdminStatus_Type()
)
zxAnFtpVerClntAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFtpVerClntAdminStatus.setStatus("current")


class _ZxAnFtpVerClntOperStatus_Type(Integer32):
    """Custom type zxAnFtpVerClntOperStatus based on Integer32"""
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
        *(("notstarted", 1),
          ("inprogress", 2),
          ("success", 3),
          ("failed", 4),
          ("masterSuccessSlaveFailed", 5))
    )


_ZxAnFtpVerClntOperStatus_Type.__name__ = "Integer32"
_ZxAnFtpVerClntOperStatus_Object = MibScalar
zxAnFtpVerClntOperStatus = _ZxAnFtpVerClntOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 1, 9),
    _ZxAnFtpVerClntOperStatus_Type()
)
zxAnFtpVerClntOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnFtpVerClntOperStatus.setStatus("current")


class _ZxAnFtpVerClntFailedReason_Type(DisplayString):
    """Custom type zxAnFtpVerClntFailedReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnFtpVerClntFailedReason_Type.__name__ = "DisplayString"
_ZxAnFtpVerClntFailedReason_Object = MibScalar
zxAnFtpVerClntFailedReason = _ZxAnFtpVerClntFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 1, 10),
    _ZxAnFtpVerClntFailedReason_Type()
)
zxAnFtpVerClntFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnFtpVerClntFailedReason.setStatus("current")
_ZxAnSwManualUpdateShelf_Type = Integer32
_ZxAnSwManualUpdateShelf_Object = MibScalar
zxAnSwManualUpdateShelf = _ZxAnSwManualUpdateShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 1, 11),
    _ZxAnSwManualUpdateShelf_Type()
)
zxAnSwManualUpdateShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSwManualUpdateShelf.setStatus("current")


class _ZxAnSwManualUpdateSlotList_Type(DisplayString):
    """Custom type zxAnSwManualUpdateSlotList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnSwManualUpdateSlotList_Type.__name__ = "DisplayString"
_ZxAnSwManualUpdateSlotList_Object = MibScalar
zxAnSwManualUpdateSlotList = _ZxAnSwManualUpdateSlotList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 1, 12),
    _ZxAnSwManualUpdateSlotList_Type()
)
zxAnSwManualUpdateSlotList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSwManualUpdateSlotList.setStatus("current")
_ZxAnSwManualUpdateCardType_Type = Integer32
_ZxAnSwManualUpdateCardType_Object = MibScalar
zxAnSwManualUpdateCardType = _ZxAnSwManualUpdateCardType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 1, 13),
    _ZxAnSwManualUpdateCardType_Type()
)
zxAnSwManualUpdateCardType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSwManualUpdateCardType.setStatus("current")


class _ZxAnFtpVerUpdateFileLocation_Type(Integer32):
    """Custom type zxAnFtpVerUpdateFileLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("ftp", 2))
    )


_ZxAnFtpVerUpdateFileLocation_Type.__name__ = "Integer32"
_ZxAnFtpVerUpdateFileLocation_Object = MibScalar
zxAnFtpVerUpdateFileLocation = _ZxAnFtpVerUpdateFileLocation_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 1, 14),
    _ZxAnFtpVerUpdateFileLocation_Type()
)
zxAnFtpVerUpdateFileLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFtpVerUpdateFileLocation.setStatus("current")


class _ZxAnFtpVerClntProgress_Type(Integer32):
    """Custom type zxAnFtpVerClntProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnFtpVerClntProgress_Type.__name__ = "Integer32"
_ZxAnFtpVerClntProgress_Object = MibScalar
zxAnFtpVerClntProgress = _ZxAnFtpVerClntProgress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 1, 15),
    _ZxAnFtpVerClntProgress_Type()
)
zxAnFtpVerClntProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnFtpVerClntProgress.setStatus("current")
if mibBuilder.loadTexts:
    zxAnFtpVerClntProgress.setUnits("%")
_ZxAnFtpVerFileSize_Type = Integer32
_ZxAnFtpVerFileSize_Object = MibScalar
zxAnFtpVerFileSize = _ZxAnFtpVerFileSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 1, 16),
    _ZxAnFtpVerFileSize_Type()
)
zxAnFtpVerFileSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFtpVerFileSize.setStatus("current")


class _ZxAnFtpAdminType_Type(Integer32):
    """Custom type zxAnFtpAdminType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("version", 1),
          ("batch", 2))
    )


_ZxAnFtpAdminType_Type.__name__ = "Integer32"
_ZxAnFtpAdminType_Object = MibScalar
zxAnFtpAdminType = _ZxAnFtpAdminType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 1, 17),
    _ZxAnFtpAdminType_Type()
)
zxAnFtpAdminType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnFtpAdminType.setStatus("current")


class _ZxAnFtpProtocolType_Type(Integer32):
    """Custom type zxAnFtpProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 1),
          ("sftp", 2))
    )


_ZxAnFtpProtocolType_Type.__name__ = "Integer32"
_ZxAnFtpProtocolType_Object = MibScalar
zxAnFtpProtocolType = _ZxAnFtpProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 1, 18),
    _ZxAnFtpProtocolType_Type()
)
zxAnFtpProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFtpProtocolType.setStatus("current")
_ZxAnCardVersionTable_Object = MibTable
zxAnCardVersionTable = _ZxAnCardVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    zxAnCardVersionTable.setStatus("current")
_ZxAnCardVersionEntry_Object = MibTableRow
zxAnCardVersionEntry = _ZxAnCardVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 2, 1)
)
zxAnCardVersionEntry.setIndexNames(
    (0, "ZTE-AN-EQUIP-MIB", "zxAnRackNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnShelfNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnSlotNo"),
)
if mibBuilder.loadTexts:
    zxAnCardVersionEntry.setStatus("current")


class _ZxAnSwCardHardwareVersion_Type(DisplayString):
    """Custom type zxAnSwCardHardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnSwCardHardwareVersion_Type.__name__ = "DisplayString"
_ZxAnSwCardHardwareVersion_Object = MibTableColumn
zxAnSwCardHardwareVersion = _ZxAnSwCardHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 2, 1, 1),
    _ZxAnSwCardHardwareVersion_Type()
)
zxAnSwCardHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardHardwareVersion.setStatus("current")


class _ZxAnSwCardFileName_Type(DisplayString):
    """Custom type zxAnSwCardFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnSwCardFileName_Type.__name__ = "DisplayString"
_ZxAnSwCardFileName_Object = MibTableColumn
zxAnSwCardFileName = _ZxAnSwCardFileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 2, 1, 2),
    _ZxAnSwCardFileName_Type()
)
zxAnSwCardFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardFileName.setStatus("current")


class _ZxAnSwCardFileType_Type(DisplayString):
    """Custom type zxAnSwCardFileType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnSwCardFileType_Type.__name__ = "DisplayString"
_ZxAnSwCardFileType_Object = MibTableColumn
zxAnSwCardFileType = _ZxAnSwCardFileType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 2, 1, 3),
    _ZxAnSwCardFileType_Type()
)
zxAnSwCardFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardFileType.setStatus("current")


class _ZxAnSwCardVersion_Type(DisplayString):
    """Custom type zxAnSwCardVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnSwCardVersion_Type.__name__ = "DisplayString"
_ZxAnSwCardVersion_Object = MibTableColumn
zxAnSwCardVersion = _ZxAnSwCardVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 2, 1, 4),
    _ZxAnSwCardVersion_Type()
)
zxAnSwCardVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardVersion.setStatus("current")
_ZxAnSwCardFileLen_Type = Integer32
_ZxAnSwCardFileLen_Object = MibTableColumn
zxAnSwCardFileLen = _ZxAnSwCardFileLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 2, 1, 5),
    _ZxAnSwCardFileLen_Type()
)
zxAnSwCardFileLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardFileLen.setStatus("current")


class _ZxAnSwCardBuildTime_Type(DisplayString):
    """Custom type zxAnSwCardBuildTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ZxAnSwCardBuildTime_Type.__name__ = "DisplayString"
_ZxAnSwCardBuildTime_Object = MibTableColumn
zxAnSwCardBuildTime = _ZxAnSwCardBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 2, 1, 6),
    _ZxAnSwCardBuildTime_Type()
)
zxAnSwCardBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardBuildTime.setStatus("current")


class _ZxAnSwCardBootwareFileName_Type(DisplayString):
    """Custom type zxAnSwCardBootwareFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnSwCardBootwareFileName_Type.__name__ = "DisplayString"
_ZxAnSwCardBootwareFileName_Object = MibTableColumn
zxAnSwCardBootwareFileName = _ZxAnSwCardBootwareFileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 2, 1, 7),
    _ZxAnSwCardBootwareFileName_Type()
)
zxAnSwCardBootwareFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardBootwareFileName.setStatus("current")


class _ZxAnSwCardBootwareFileType_Type(DisplayString):
    """Custom type zxAnSwCardBootwareFileType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnSwCardBootwareFileType_Type.__name__ = "DisplayString"
_ZxAnSwCardBootwareFileType_Object = MibTableColumn
zxAnSwCardBootwareFileType = _ZxAnSwCardBootwareFileType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 2, 1, 8),
    _ZxAnSwCardBootwareFileType_Type()
)
zxAnSwCardBootwareFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardBootwareFileType.setStatus("current")


class _ZxAnSwCardBootwareVersion_Type(DisplayString):
    """Custom type zxAnSwCardBootwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnSwCardBootwareVersion_Type.__name__ = "DisplayString"
_ZxAnSwCardBootwareVersion_Object = MibTableColumn
zxAnSwCardBootwareVersion = _ZxAnSwCardBootwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 2, 1, 9),
    _ZxAnSwCardBootwareVersion_Type()
)
zxAnSwCardBootwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardBootwareVersion.setStatus("current")
_ZxAnSwCardBootwareFileLen_Type = Integer32
_ZxAnSwCardBootwareFileLen_Object = MibTableColumn
zxAnSwCardBootwareFileLen = _ZxAnSwCardBootwareFileLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 2, 1, 10),
    _ZxAnSwCardBootwareFileLen_Type()
)
zxAnSwCardBootwareFileLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardBootwareFileLen.setStatus("current")


class _ZxAnSwCardBootwareBuildTime_Type(DisplayString):
    """Custom type zxAnSwCardBootwareBuildTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ZxAnSwCardBootwareBuildTime_Type.__name__ = "DisplayString"
_ZxAnSwCardBootwareBuildTime_Object = MibTableColumn
zxAnSwCardBootwareBuildTime = _ZxAnSwCardBootwareBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 2, 1, 11),
    _ZxAnSwCardBootwareBuildTime_Type()
)
zxAnSwCardBootwareBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardBootwareBuildTime.setStatus("current")


class _ZxAnSwCardFirmware1FileName_Type(DisplayString):
    """Custom type zxAnSwCardFirmware1FileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnSwCardFirmware1FileName_Type.__name__ = "DisplayString"
_ZxAnSwCardFirmware1FileName_Object = MibTableColumn
zxAnSwCardFirmware1FileName = _ZxAnSwCardFirmware1FileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 2, 1, 12),
    _ZxAnSwCardFirmware1FileName_Type()
)
zxAnSwCardFirmware1FileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardFirmware1FileName.setStatus("current")


class _ZxAnSwCardFirmware1FileType_Type(DisplayString):
    """Custom type zxAnSwCardFirmware1FileType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnSwCardFirmware1FileType_Type.__name__ = "DisplayString"
_ZxAnSwCardFirmware1FileType_Object = MibTableColumn
zxAnSwCardFirmware1FileType = _ZxAnSwCardFirmware1FileType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 2, 1, 13),
    _ZxAnSwCardFirmware1FileType_Type()
)
zxAnSwCardFirmware1FileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardFirmware1FileType.setStatus("current")


class _ZxAnSwCardFirmware1Version_Type(DisplayString):
    """Custom type zxAnSwCardFirmware1Version based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnSwCardFirmware1Version_Type.__name__ = "DisplayString"
_ZxAnSwCardFirmware1Version_Object = MibTableColumn
zxAnSwCardFirmware1Version = _ZxAnSwCardFirmware1Version_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 2, 1, 14),
    _ZxAnSwCardFirmware1Version_Type()
)
zxAnSwCardFirmware1Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardFirmware1Version.setStatus("current")
_ZxAnSwCardFirmware1FileLen_Type = Integer32
_ZxAnSwCardFirmware1FileLen_Object = MibTableColumn
zxAnSwCardFirmware1FileLen = _ZxAnSwCardFirmware1FileLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 2, 1, 15),
    _ZxAnSwCardFirmware1FileLen_Type()
)
zxAnSwCardFirmware1FileLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardFirmware1FileLen.setStatus("current")


class _ZxAnSwCardFirmware1BuildTime_Type(DisplayString):
    """Custom type zxAnSwCardFirmware1BuildTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ZxAnSwCardFirmware1BuildTime_Type.__name__ = "DisplayString"
_ZxAnSwCardFirmware1BuildTime_Object = MibTableColumn
zxAnSwCardFirmware1BuildTime = _ZxAnSwCardFirmware1BuildTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 2, 1, 16),
    _ZxAnSwCardFirmware1BuildTime_Type()
)
zxAnSwCardFirmware1BuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardFirmware1BuildTime.setStatus("current")


class _ZxAnSwCardFirmware2FileName_Type(DisplayString):
    """Custom type zxAnSwCardFirmware2FileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnSwCardFirmware2FileName_Type.__name__ = "DisplayString"
_ZxAnSwCardFirmware2FileName_Object = MibTableColumn
zxAnSwCardFirmware2FileName = _ZxAnSwCardFirmware2FileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 2, 1, 17),
    _ZxAnSwCardFirmware2FileName_Type()
)
zxAnSwCardFirmware2FileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardFirmware2FileName.setStatus("current")


class _ZxAnSwCardFirmware2FileType_Type(DisplayString):
    """Custom type zxAnSwCardFirmware2FileType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnSwCardFirmware2FileType_Type.__name__ = "DisplayString"
_ZxAnSwCardFirmware2FileType_Object = MibTableColumn
zxAnSwCardFirmware2FileType = _ZxAnSwCardFirmware2FileType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 2, 1, 18),
    _ZxAnSwCardFirmware2FileType_Type()
)
zxAnSwCardFirmware2FileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardFirmware2FileType.setStatus("current")


class _ZxAnSwCardFirmware2Version_Type(DisplayString):
    """Custom type zxAnSwCardFirmware2Version based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnSwCardFirmware2Version_Type.__name__ = "DisplayString"
_ZxAnSwCardFirmware2Version_Object = MibTableColumn
zxAnSwCardFirmware2Version = _ZxAnSwCardFirmware2Version_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 2, 1, 19),
    _ZxAnSwCardFirmware2Version_Type()
)
zxAnSwCardFirmware2Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardFirmware2Version.setStatus("current")
_ZxAnSwCardFirmware2FileLen_Type = Integer32
_ZxAnSwCardFirmware2FileLen_Object = MibTableColumn
zxAnSwCardFirmware2FileLen = _ZxAnSwCardFirmware2FileLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 2, 1, 20),
    _ZxAnSwCardFirmware2FileLen_Type()
)
zxAnSwCardFirmware2FileLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardFirmware2FileLen.setStatus("current")


class _ZxAnSwCardFirmware2BuildTime_Type(DisplayString):
    """Custom type zxAnSwCardFirmware2BuildTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ZxAnSwCardFirmware2BuildTime_Type.__name__ = "DisplayString"
_ZxAnSwCardFirmware2BuildTime_Object = MibTableColumn
zxAnSwCardFirmware2BuildTime = _ZxAnSwCardFirmware2BuildTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 2, 1, 21),
    _ZxAnSwCardFirmware2BuildTime_Type()
)
zxAnSwCardFirmware2BuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardFirmware2BuildTime.setStatus("current")


class _ZxAnSwCardFirmware3FileName_Type(DisplayString):
    """Custom type zxAnSwCardFirmware3FileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnSwCardFirmware3FileName_Type.__name__ = "DisplayString"
_ZxAnSwCardFirmware3FileName_Object = MibTableColumn
zxAnSwCardFirmware3FileName = _ZxAnSwCardFirmware3FileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 2, 1, 22),
    _ZxAnSwCardFirmware3FileName_Type()
)
zxAnSwCardFirmware3FileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardFirmware3FileName.setStatus("current")


class _ZxAnSwCardFirmware3FileType_Type(DisplayString):
    """Custom type zxAnSwCardFirmware3FileType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnSwCardFirmware3FileType_Type.__name__ = "DisplayString"
_ZxAnSwCardFirmware3FileType_Object = MibTableColumn
zxAnSwCardFirmware3FileType = _ZxAnSwCardFirmware3FileType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 2, 1, 23),
    _ZxAnSwCardFirmware3FileType_Type()
)
zxAnSwCardFirmware3FileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardFirmware3FileType.setStatus("current")


class _ZxAnSwCardFirmware3Version_Type(DisplayString):
    """Custom type zxAnSwCardFirmware3Version based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnSwCardFirmware3Version_Type.__name__ = "DisplayString"
_ZxAnSwCardFirmware3Version_Object = MibTableColumn
zxAnSwCardFirmware3Version = _ZxAnSwCardFirmware3Version_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 2, 1, 24),
    _ZxAnSwCardFirmware3Version_Type()
)
zxAnSwCardFirmware3Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardFirmware3Version.setStatus("current")
_ZxAnSwCardFirmware3FileLen_Type = Integer32
_ZxAnSwCardFirmware3FileLen_Object = MibTableColumn
zxAnSwCardFirmware3FileLen = _ZxAnSwCardFirmware3FileLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 2, 1, 25),
    _ZxAnSwCardFirmware3FileLen_Type()
)
zxAnSwCardFirmware3FileLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardFirmware3FileLen.setStatus("current")


class _ZxAnSwCardFirmware3BuildTime_Type(DisplayString):
    """Custom type zxAnSwCardFirmware3BuildTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ZxAnSwCardFirmware3BuildTime_Type.__name__ = "DisplayString"
_ZxAnSwCardFirmware3BuildTime_Object = MibTableColumn
zxAnSwCardFirmware3BuildTime = _ZxAnSwCardFirmware3BuildTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 2, 1, 26),
    _ZxAnSwCardFirmware3BuildTime_Type()
)
zxAnSwCardFirmware3BuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardFirmware3BuildTime.setStatus("current")
_ZxAnSubcardVersionTable_Object = MibTable
zxAnSubcardVersionTable = _ZxAnSubcardVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    zxAnSubcardVersionTable.setStatus("current")
_ZxAnSubcardVersionEntry_Object = MibTableRow
zxAnSubcardVersionEntry = _ZxAnSubcardVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 3, 1)
)
zxAnSubcardVersionEntry.setIndexNames(
    (0, "ZTE-AN-EQUIP-MIB", "zxAnRackNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnShelfNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnSlotNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnSubcardNo"),
)
if mibBuilder.loadTexts:
    zxAnSubcardVersionEntry.setStatus("current")


class _ZxAnSwSubcardHardwareVersion_Type(DisplayString):
    """Custom type zxAnSwSubcardHardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnSwSubcardHardwareVersion_Type.__name__ = "DisplayString"
_ZxAnSwSubcardHardwareVersion_Object = MibTableColumn
zxAnSwSubcardHardwareVersion = _ZxAnSwSubcardHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 3, 1, 1),
    _ZxAnSwSubcardHardwareVersion_Type()
)
zxAnSwSubcardHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwSubcardHardwareVersion.setStatus("current")


class _ZxAnSwSubcardFileName_Type(DisplayString):
    """Custom type zxAnSwSubcardFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnSwSubcardFileName_Type.__name__ = "DisplayString"
_ZxAnSwSubcardFileName_Object = MibTableColumn
zxAnSwSubcardFileName = _ZxAnSwSubcardFileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 3, 1, 2),
    _ZxAnSwSubcardFileName_Type()
)
zxAnSwSubcardFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwSubcardFileName.setStatus("current")


class _ZxAnSwSubcardFileType_Type(DisplayString):
    """Custom type zxAnSwSubcardFileType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnSwSubcardFileType_Type.__name__ = "DisplayString"
_ZxAnSwSubcardFileType_Object = MibTableColumn
zxAnSwSubcardFileType = _ZxAnSwSubcardFileType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 3, 1, 3),
    _ZxAnSwSubcardFileType_Type()
)
zxAnSwSubcardFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwSubcardFileType.setStatus("current")


class _ZxAnSwSubcardVersion_Type(DisplayString):
    """Custom type zxAnSwSubcardVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnSwSubcardVersion_Type.__name__ = "DisplayString"
_ZxAnSwSubcardVersion_Object = MibTableColumn
zxAnSwSubcardVersion = _ZxAnSwSubcardVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 3, 1, 4),
    _ZxAnSwSubcardVersion_Type()
)
zxAnSwSubcardVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwSubcardVersion.setStatus("current")
_ZxAnSwSubcardFileLen_Type = Integer32
_ZxAnSwSubcardFileLen_Object = MibTableColumn
zxAnSwSubcardFileLen = _ZxAnSwSubcardFileLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 3, 1, 5),
    _ZxAnSwSubcardFileLen_Type()
)
zxAnSwSubcardFileLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwSubcardFileLen.setStatus("current")


class _ZxAnSwSubcardBuildTime_Type(DisplayString):
    """Custom type zxAnSwSubcardBuildTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ZxAnSwSubcardBuildTime_Type.__name__ = "DisplayString"
_ZxAnSwSubcardBuildTime_Object = MibTableColumn
zxAnSwSubcardBuildTime = _ZxAnSwSubcardBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 3, 1, 6),
    _ZxAnSwSubcardBuildTime_Type()
)
zxAnSwSubcardBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwSubcardBuildTime.setStatus("current")


class _ZxAnSwSubcardBootwareFileName_Type(DisplayString):
    """Custom type zxAnSwSubcardBootwareFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnSwSubcardBootwareFileName_Type.__name__ = "DisplayString"
_ZxAnSwSubcardBootwareFileName_Object = MibTableColumn
zxAnSwSubcardBootwareFileName = _ZxAnSwSubcardBootwareFileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 3, 1, 7),
    _ZxAnSwSubcardBootwareFileName_Type()
)
zxAnSwSubcardBootwareFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwSubcardBootwareFileName.setStatus("current")


class _ZxAnSwSubcardBootwareFileType_Type(DisplayString):
    """Custom type zxAnSwSubcardBootwareFileType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnSwSubcardBootwareFileType_Type.__name__ = "DisplayString"
_ZxAnSwSubcardBootwareFileType_Object = MibTableColumn
zxAnSwSubcardBootwareFileType = _ZxAnSwSubcardBootwareFileType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 3, 1, 8),
    _ZxAnSwSubcardBootwareFileType_Type()
)
zxAnSwSubcardBootwareFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwSubcardBootwareFileType.setStatus("current")


class _ZxAnSwSubcardBootwareVersion_Type(DisplayString):
    """Custom type zxAnSwSubcardBootwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnSwSubcardBootwareVersion_Type.__name__ = "DisplayString"
_ZxAnSwSubcardBootwareVersion_Object = MibTableColumn
zxAnSwSubcardBootwareVersion = _ZxAnSwSubcardBootwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 3, 1, 9),
    _ZxAnSwSubcardBootwareVersion_Type()
)
zxAnSwSubcardBootwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwSubcardBootwareVersion.setStatus("current")
_ZxAnSwSubcardBootwareFileLen_Type = Integer32
_ZxAnSwSubcardBootwareFileLen_Object = MibTableColumn
zxAnSwSubcardBootwareFileLen = _ZxAnSwSubcardBootwareFileLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 3, 1, 10),
    _ZxAnSwSubcardBootwareFileLen_Type()
)
zxAnSwSubcardBootwareFileLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwSubcardBootwareFileLen.setStatus("current")


class _ZxAnSwSubcardBootwareBuildTime_Type(DisplayString):
    """Custom type zxAnSwSubcardBootwareBuildTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ZxAnSwSubcardBootwareBuildTime_Type.__name__ = "DisplayString"
_ZxAnSwSubcardBootwareBuildTime_Object = MibTableColumn
zxAnSwSubcardBootwareBuildTime = _ZxAnSwSubcardBootwareBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 3, 1, 11),
    _ZxAnSwSubcardBootwareBuildTime_Type()
)
zxAnSwSubcardBootwareBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwSubcardBootwareBuildTime.setStatus("current")


class _ZxAnSwSubcardFirmwareFileName_Type(DisplayString):
    """Custom type zxAnSwSubcardFirmwareFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnSwSubcardFirmwareFileName_Type.__name__ = "DisplayString"
_ZxAnSwSubcardFirmwareFileName_Object = MibTableColumn
zxAnSwSubcardFirmwareFileName = _ZxAnSwSubcardFirmwareFileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 3, 1, 12),
    _ZxAnSwSubcardFirmwareFileName_Type()
)
zxAnSwSubcardFirmwareFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwSubcardFirmwareFileName.setStatus("current")


class _ZxAnSwSubcardFirmwareFileType_Type(DisplayString):
    """Custom type zxAnSwSubcardFirmwareFileType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnSwSubcardFirmwareFileType_Type.__name__ = "DisplayString"
_ZxAnSwSubcardFirmwareFileType_Object = MibTableColumn
zxAnSwSubcardFirmwareFileType = _ZxAnSwSubcardFirmwareFileType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 3, 1, 13),
    _ZxAnSwSubcardFirmwareFileType_Type()
)
zxAnSwSubcardFirmwareFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwSubcardFirmwareFileType.setStatus("current")


class _ZxAnSwSubcardFirmwareVersion_Type(DisplayString):
    """Custom type zxAnSwSubcardFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnSwSubcardFirmwareVersion_Type.__name__ = "DisplayString"
_ZxAnSwSubcardFirmwareVersion_Object = MibTableColumn
zxAnSwSubcardFirmwareVersion = _ZxAnSwSubcardFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 3, 1, 14),
    _ZxAnSwSubcardFirmwareVersion_Type()
)
zxAnSwSubcardFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwSubcardFirmwareVersion.setStatus("current")
_ZxAnSwSubcardFirmwareFileLen_Type = Integer32
_ZxAnSwSubcardFirmwareFileLen_Object = MibTableColumn
zxAnSwSubcardFirmwareFileLen = _ZxAnSwSubcardFirmwareFileLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 3, 1, 15),
    _ZxAnSwSubcardFirmwareFileLen_Type()
)
zxAnSwSubcardFirmwareFileLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwSubcardFirmwareFileLen.setStatus("current")


class _ZxAnSwSubcardFirmwareBuildTime_Type(DisplayString):
    """Custom type zxAnSwSubcardFirmwareBuildTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ZxAnSwSubcardFirmwareBuildTime_Type.__name__ = "DisplayString"
_ZxAnSwSubcardFirmwareBuildTime_Object = MibTableColumn
zxAnSwSubcardFirmwareBuildTime = _ZxAnSwSubcardFirmwareBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 3, 1, 16),
    _ZxAnSwSubcardFirmwareBuildTime_Type()
)
zxAnSwSubcardFirmwareBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwSubcardFirmwareBuildTime.setStatus("current")
_ZxAnVersionSavedTable_Object = MibTable
zxAnVersionSavedTable = _ZxAnVersionSavedTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    zxAnVersionSavedTable.setStatus("current")
_ZxAnVersionSavedEntry_Object = MibTableRow
zxAnVersionSavedEntry = _ZxAnVersionSavedEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 4, 1)
)
zxAnVersionSavedEntry.setIndexNames(
    (0, "ZTE-AN-EQUIP-MIB", "zxAnRackNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnShelfNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnSlotNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnSwImageFileName"),
)
if mibBuilder.loadTexts:
    zxAnVersionSavedEntry.setStatus("current")


class _ZxAnSwImageFileName_Type(DisplayString):
    """Custom type zxAnSwImageFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnSwImageFileName_Type.__name__ = "DisplayString"
_ZxAnSwImageFileName_Object = MibTableColumn
zxAnSwImageFileName = _ZxAnSwImageFileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 4, 1, 1),
    _ZxAnSwImageFileName_Type()
)
zxAnSwImageFileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSwImageFileName.setStatus("current")


class _ZxAnSwImageFileType_Type(DisplayString):
    """Custom type zxAnSwImageFileType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnSwImageFileType_Type.__name__ = "DisplayString"
_ZxAnSwImageFileType_Object = MibTableColumn
zxAnSwImageFileType = _ZxAnSwImageFileType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 4, 1, 2),
    _ZxAnSwImageFileType_Type()
)
zxAnSwImageFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwImageFileType.setStatus("current")


class _ZxAnSwImageVersion_Type(DisplayString):
    """Custom type zxAnSwImageVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnSwImageVersion_Type.__name__ = "DisplayString"
_ZxAnSwImageVersion_Object = MibTableColumn
zxAnSwImageVersion = _ZxAnSwImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 4, 1, 3),
    _ZxAnSwImageVersion_Type()
)
zxAnSwImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwImageVersion.setStatus("current")
_ZxAnSwImageFileLen_Type = Integer32
_ZxAnSwImageFileLen_Object = MibTableColumn
zxAnSwImageFileLen = _ZxAnSwImageFileLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 4, 1, 4),
    _ZxAnSwImageFileLen_Type()
)
zxAnSwImageFileLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwImageFileLen.setStatus("current")


class _ZxAnSwImageBuildTime_Type(DisplayString):
    """Custom type zxAnSwImageBuildTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ZxAnSwImageBuildTime_Type.__name__ = "DisplayString"
_ZxAnSwImageBuildTime_Object = MibTableColumn
zxAnSwImageBuildTime = _ZxAnSwImageBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 4, 1, 5),
    _ZxAnSwImageBuildTime_Type()
)
zxAnSwImageBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwImageBuildTime.setStatus("current")


class _ZxAnSwImageActiveStatus_Type(Integer32):
    """Custom type zxAnSwImageActiveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("verSwap", 1),
          ("inactive", 2),
          ("erase", 3))
    )


_ZxAnSwImageActiveStatus_Type.__name__ = "Integer32"
_ZxAnSwImageActiveStatus_Object = MibTableColumn
zxAnSwImageActiveStatus = _ZxAnSwImageActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 4, 1, 6),
    _ZxAnSwImageActiveStatus_Type()
)
zxAnSwImageActiveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSwImageActiveStatus.setStatus("current")


class _ZxAnSwImageSyncToSecondary_Type(Integer32):
    """Custom type zxAnSwImageSyncToSecondary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("synVersionToSlave", 1)
    )


_ZxAnSwImageSyncToSecondary_Type.__name__ = "Integer32"
_ZxAnSwImageSyncToSecondary_Object = MibTableColumn
zxAnSwImageSyncToSecondary = _ZxAnSwImageSyncToSecondary_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 4, 1, 7),
    _ZxAnSwImageSyncToSecondary_Type()
)
zxAnSwImageSyncToSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSwImageSyncToSecondary.setStatus("current")


class _ZxAnSwImageSyncToSecondaryStatus_Type(Integer32):
    """Custom type zxAnSwImageSyncToSecondaryStatus based on Integer32"""
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
        *(("idle", 1),
          ("processing", 2),
          ("sendingData", 3),
          ("timeout", 4),
          ("failed", 5),
          ("success", 6),
          ("sameversion", 7))
    )


_ZxAnSwImageSyncToSecondaryStatus_Type.__name__ = "Integer32"
_ZxAnSwImageSyncToSecondaryStatus_Object = MibTableColumn
zxAnSwImageSyncToSecondaryStatus = _ZxAnSwImageSyncToSecondaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 4, 1, 8),
    _ZxAnSwImageSyncToSecondaryStatus_Type()
)
zxAnSwImageSyncToSecondaryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwImageSyncToSecondaryStatus.setStatus("current")


class _ZxAnSavedTableType_Type(Integer32):
    """Custom type zxAnSavedTableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("version", 1),
          ("batch", 2))
    )


_ZxAnSavedTableType_Type.__name__ = "Integer32"
_ZxAnSavedTableType_Object = MibTableColumn
zxAnSavedTableType = _ZxAnSavedTableType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 4, 1, 9),
    _ZxAnSavedTableType_Type()
)
zxAnSavedTableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSavedTableType.setStatus("current")


class _ZxAnSavedFileDesc_Type(DisplayString):
    """Custom type zxAnSavedFileDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ZxAnSavedFileDesc_Type.__name__ = "DisplayString"
_ZxAnSavedFileDesc_Object = MibTableColumn
zxAnSavedFileDesc = _ZxAnSavedFileDesc_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 4, 1, 10),
    _ZxAnSavedFileDesc_Type()
)
zxAnSavedFileDesc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSavedFileDesc.setStatus("current")


class _ZxAnSavedPatchParentVersion_Type(DisplayString):
    """Custom type zxAnSavedPatchParentVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnSavedPatchParentVersion_Type.__name__ = "DisplayString"
_ZxAnSavedPatchParentVersion_Object = MibTableColumn
zxAnSavedPatchParentVersion = _ZxAnSavedPatchParentVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 4, 1, 11),
    _ZxAnSavedPatchParentVersion_Type()
)
zxAnSavedPatchParentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSavedPatchParentVersion.setStatus("current")


class _ZxAnSavedPatchActiveTime_Type(DisplayString):
    """Custom type zxAnSavedPatchActiveTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ZxAnSavedPatchActiveTime_Type.__name__ = "DisplayString"
_ZxAnSavedPatchActiveTime_Object = MibTableColumn
zxAnSavedPatchActiveTime = _ZxAnSavedPatchActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 4, 1, 12),
    _ZxAnSavedPatchActiveTime_Type()
)
zxAnSavedPatchActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSavedPatchActiveTime.setStatus("current")


class _ZxAnSavedPatchActiveStatus_Type(Integer32):
    """Custom type zxAnSavedPatchActiveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("actived", 1),
          ("inactive", 2),
          ("autorun", 3))
    )


_ZxAnSavedPatchActiveStatus_Type.__name__ = "Integer32"
_ZxAnSavedPatchActiveStatus_Object = MibTableColumn
zxAnSavedPatchActiveStatus = _ZxAnSavedPatchActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 4, 1, 13),
    _ZxAnSavedPatchActiveStatus_Type()
)
zxAnSavedPatchActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSavedPatchActiveStatus.setStatus("current")


class _ZxAnSavedPatchAdminStatus_Type(Integer32):
    """Custom type zxAnSavedPatchAdminStatus based on Integer32"""
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
        *(("active", 1),
          ("deactivate", 2),
          ("save", 3),
          ("erase", 4))
    )


_ZxAnSavedPatchAdminStatus_Type.__name__ = "Integer32"
_ZxAnSavedPatchAdminStatus_Object = MibTableColumn
zxAnSavedPatchAdminStatus = _ZxAnSavedPatchAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 4, 1, 14),
    _ZxAnSavedPatchAdminStatus_Type()
)
zxAnSavedPatchAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSavedPatchAdminStatus.setStatus("current")


class _ZxAnSavedAdminFailedReason_Type(DisplayString):
    """Custom type zxAnSavedAdminFailedReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnSavedAdminFailedReason_Type.__name__ = "DisplayString"
_ZxAnSavedAdminFailedReason_Object = MibTableColumn
zxAnSavedAdminFailedReason = _ZxAnSavedAdminFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 4, 1, 15),
    _ZxAnSavedAdminFailedReason_Type()
)
zxAnSavedAdminFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSavedAdminFailedReason.setStatus("current")


class _ZxAnSavedVersionDownloadTime_Type(DisplayString):
    """Custom type zxAnSavedVersionDownloadTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ZxAnSavedVersionDownloadTime_Type.__name__ = "DisplayString"
_ZxAnSavedVersionDownloadTime_Object = MibTableColumn
zxAnSavedVersionDownloadTime = _ZxAnSavedVersionDownloadTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 4, 1, 16),
    _ZxAnSavedVersionDownloadTime_Type()
)
zxAnSavedVersionDownloadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSavedVersionDownloadTime.setStatus("current")
_ZxAnVersionUpdatingStatusTable_Object = MibTable
zxAnVersionUpdatingStatusTable = _ZxAnVersionUpdatingStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 5)
)
if mibBuilder.loadTexts:
    zxAnVersionUpdatingStatusTable.setStatus("current")
_ZxAnVersionUpdatingStatusEntry_Object = MibTableRow
zxAnVersionUpdatingStatusEntry = _ZxAnVersionUpdatingStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 5, 1)
)
zxAnVersionUpdatingStatusEntry.setIndexNames(
    (0, "ZTE-AN-EQUIP-MIB", "zxAnRackNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnShelfNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnSlotNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnSwManualUpdateSoftwareType"),
)
if mibBuilder.loadTexts:
    zxAnVersionUpdatingStatusEntry.setStatus("current")


class _ZxAnSwManualUpdateSoftwareType_Type(DisplayString):
    """Custom type zxAnSwManualUpdateSoftwareType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnSwManualUpdateSoftwareType_Type.__name__ = "DisplayString"
_ZxAnSwManualUpdateSoftwareType_Object = MibTableColumn
zxAnSwManualUpdateSoftwareType = _ZxAnSwManualUpdateSoftwareType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 5, 1, 1),
    _ZxAnSwManualUpdateSoftwareType_Type()
)
zxAnSwManualUpdateSoftwareType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSwManualUpdateSoftwareType.setStatus("current")


class _ZxAnSwManualUpdateStatus_Type(Integer32):
    """Custom type zxAnSwManualUpdateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("negotiating", 1),
          ("downloading", 2),
          ("abort", 3),
          ("success", 4),
          ("ftping", 5),
          ("sameVersion", 6))
    )


_ZxAnSwManualUpdateStatus_Type.__name__ = "Integer32"
_ZxAnSwManualUpdateStatus_Object = MibTableColumn
zxAnSwManualUpdateStatus = _ZxAnSwManualUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 5, 1, 2),
    _ZxAnSwManualUpdateStatus_Type()
)
zxAnSwManualUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwManualUpdateStatus.setStatus("current")


class _ZxAnSwManualFailedReason_Type(Integer32):
    """Custom type zxAnSwManualFailedReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noSupportCardHwVersion", 1),
          ("mismatchCardHwVersion", 2),
          ("mismatchCardConfData", 3),
          ("noSwInNe", 4),
          ("cardUpdateSwFailed", 5),
          ("cardOffline", 6),
          ("noError", 254),
          ("otherErrors", 255))
    )


_ZxAnSwManualFailedReason_Type.__name__ = "Integer32"
_ZxAnSwManualFailedReason_Object = MibTableColumn
zxAnSwManualFailedReason = _ZxAnSwManualFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 5, 1, 3),
    _ZxAnSwManualFailedReason_Type()
)
zxAnSwManualFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwManualFailedReason.setStatus("current")
_ZxAnCpeSoftwareMgmt_ObjectIdentity = ObjectIdentity
zxAnCpeSoftwareMgmt = _ZxAnCpeSoftwareMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6)
)
_ZxAnCpeSwUpdateTaskTable_Object = MibTable
zxAnCpeSwUpdateTaskTable = _ZxAnCpeSwUpdateTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    zxAnCpeSwUpdateTaskTable.setStatus("current")
_ZxAnCpeSwUpdateTaskEntry_Object = MibTableRow
zxAnCpeSwUpdateTaskEntry = _ZxAnCpeSwUpdateTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 1, 1)
)
zxAnCpeSwUpdateTaskEntry.setIndexNames(
    (0, "ZTE-AN-EQUIP-MIB", "zxAnCpeSwUpdateTaskId"),
)
if mibBuilder.loadTexts:
    zxAnCpeSwUpdateTaskEntry.setStatus("current")


class _ZxAnCpeSwUpdateTaskId_Type(DisplayString):
    """Custom type zxAnCpeSwUpdateTaskId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnCpeSwUpdateTaskId_Type.__name__ = "DisplayString"
_ZxAnCpeSwUpdateTaskId_Object = MibTableColumn
zxAnCpeSwUpdateTaskId = _ZxAnCpeSwUpdateTaskId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 1, 1, 1),
    _ZxAnCpeSwUpdateTaskId_Type()
)
zxAnCpeSwUpdateTaskId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnCpeSwUpdateTaskId.setStatus("current")


class _ZxAnCpeSwUpdateTaskCreateTime_Type(DisplayString):
    """Custom type zxAnCpeSwUpdateTaskCreateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ZxAnCpeSwUpdateTaskCreateTime_Type.__name__ = "DisplayString"
_ZxAnCpeSwUpdateTaskCreateTime_Object = MibTableColumn
zxAnCpeSwUpdateTaskCreateTime = _ZxAnCpeSwUpdateTaskCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 1, 1, 2),
    _ZxAnCpeSwUpdateTaskCreateTime_Type()
)
zxAnCpeSwUpdateTaskCreateTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCpeSwUpdateTaskCreateTime.setStatus("current")


class _ZxAnCpeSwUpdateTaskDesc_Type(DisplayString):
    """Custom type zxAnCpeSwUpdateTaskDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnCpeSwUpdateTaskDesc_Type.__name__ = "DisplayString"
_ZxAnCpeSwUpdateTaskDesc_Object = MibTableColumn
zxAnCpeSwUpdateTaskDesc = _ZxAnCpeSwUpdateTaskDesc_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 1, 1, 3),
    _ZxAnCpeSwUpdateTaskDesc_Type()
)
zxAnCpeSwUpdateTaskDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCpeSwUpdateTaskDesc.setStatus("current")


class _ZxAnCpeSwUpdateTaskStatus_Type(Integer32):
    """Custom type zxAnCpeSwUpdateTaskStatus based on Integer32"""
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
        *(("completed", 1),
          ("executing", 2),
          ("aborted", 3),
          ("aborting", 4),
          ("abortFailed", 5),
          ("notStart", 6),
          ("startFailed", 7))
    )


_ZxAnCpeSwUpdateTaskStatus_Type.__name__ = "Integer32"
_ZxAnCpeSwUpdateTaskStatus_Object = MibTableColumn
zxAnCpeSwUpdateTaskStatus = _ZxAnCpeSwUpdateTaskStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 1, 1, 4),
    _ZxAnCpeSwUpdateTaskStatus_Type()
)
zxAnCpeSwUpdateTaskStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCpeSwUpdateTaskStatus.setStatus("current")


class _ZxAnCpeSwUpdateTaskCpeCategory_Type(DisplayString):
    """Custom type zxAnCpeSwUpdateTaskCpeCategory based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnCpeSwUpdateTaskCpeCategory_Type.__name__ = "DisplayString"
_ZxAnCpeSwUpdateTaskCpeCategory_Object = MibTableColumn
zxAnCpeSwUpdateTaskCpeCategory = _ZxAnCpeSwUpdateTaskCpeCategory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 1, 1, 5),
    _ZxAnCpeSwUpdateTaskCpeCategory_Type()
)
zxAnCpeSwUpdateTaskCpeCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCpeSwUpdateTaskCpeCategory.setStatus("current")


class _ZxAnCpeSwUpdateTaskAdminStatus_Type(Integer32):
    """Custom type zxAnCpeSwUpdateTaskAdminStatus based on Integer32"""
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
        *(("downloadAndActive", 1),
          ("downloadOnly", 2),
          ("activeOnly", 3),
          ("deactiveOnly", 4),
          ("abort", 5))
    )


_ZxAnCpeSwUpdateTaskAdminStatus_Type.__name__ = "Integer32"
_ZxAnCpeSwUpdateTaskAdminStatus_Object = MibTableColumn
zxAnCpeSwUpdateTaskAdminStatus = _ZxAnCpeSwUpdateTaskAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 1, 1, 6),
    _ZxAnCpeSwUpdateTaskAdminStatus_Type()
)
zxAnCpeSwUpdateTaskAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCpeSwUpdateTaskAdminStatus.setStatus("current")


class _ZxAnCpeSwUpdateTaskGranularity_Type(Integer32):
    """Custom type zxAnCpeSwUpdateTaskGranularity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ne", 1),
          ("shelf", 2),
          ("card", 3),
          ("olt", 4),
          ("onuOrPort", 5),
          ("slotOfOnu", 6))
    )


_ZxAnCpeSwUpdateTaskGranularity_Type.__name__ = "Integer32"
_ZxAnCpeSwUpdateTaskGranularity_Object = MibTableColumn
zxAnCpeSwUpdateTaskGranularity = _ZxAnCpeSwUpdateTaskGranularity_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 1, 1, 7),
    _ZxAnCpeSwUpdateTaskGranularity_Type()
)
zxAnCpeSwUpdateTaskGranularity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCpeSwUpdateTaskGranularity.setStatus("current")


class _ZxAnCpeSwUpdateTaskObjList_Type(OctetString):
    """Custom type zxAnCpeSwUpdateTaskObjList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1024, 1024),
    )
    fixed_length = 1024


_ZxAnCpeSwUpdateTaskObjList_Type.__name__ = "OctetString"
_ZxAnCpeSwUpdateTaskObjList_Object = MibTableColumn
zxAnCpeSwUpdateTaskObjList = _ZxAnCpeSwUpdateTaskObjList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 1, 1, 8),
    _ZxAnCpeSwUpdateTaskObjList_Type()
)
zxAnCpeSwUpdateTaskObjList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCpeSwUpdateTaskObjList.setStatus("current")


class _ZxAnCpeSwUpdateTaskCpeModel_Type(DisplayString):
    """Custom type zxAnCpeSwUpdateTaskCpeModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnCpeSwUpdateTaskCpeModel_Type.__name__ = "DisplayString"
_ZxAnCpeSwUpdateTaskCpeModel_Object = MibTableColumn
zxAnCpeSwUpdateTaskCpeModel = _ZxAnCpeSwUpdateTaskCpeModel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 1, 1, 9),
    _ZxAnCpeSwUpdateTaskCpeModel_Type()
)
zxAnCpeSwUpdateTaskCpeModel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCpeSwUpdateTaskCpeModel.setStatus("current")
_ZxAnCpeSwUpdateTaskCpeVersions_Type = DisplayString
_ZxAnCpeSwUpdateTaskCpeVersions_Object = MibTableColumn
zxAnCpeSwUpdateTaskCpeVersions = _ZxAnCpeSwUpdateTaskCpeVersions_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 1, 1, 10),
    _ZxAnCpeSwUpdateTaskCpeVersions_Type()
)
zxAnCpeSwUpdateTaskCpeVersions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCpeSwUpdateTaskCpeVersions.setStatus("current")


class _ZxAnCpeSwUpdateTaskVerFileName_Type(DisplayString):
    """Custom type zxAnCpeSwUpdateTaskVerFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnCpeSwUpdateTaskVerFileName_Type.__name__ = "DisplayString"
_ZxAnCpeSwUpdateTaskVerFileName_Object = MibTableColumn
zxAnCpeSwUpdateTaskVerFileName = _ZxAnCpeSwUpdateTaskVerFileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 1, 1, 11),
    _ZxAnCpeSwUpdateTaskVerFileName_Type()
)
zxAnCpeSwUpdateTaskVerFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCpeSwUpdateTaskVerFileName.setStatus("current")


class _ZxAnCpeSwUpdateTaskVerFileLoc_Type(Integer32):
    """Custom type zxAnCpeSwUpdateTaskVerFileLoc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ne", 1),
          ("ftpSvr", 2))
    )


_ZxAnCpeSwUpdateTaskVerFileLoc_Type.__name__ = "Integer32"
_ZxAnCpeSwUpdateTaskVerFileLoc_Object = MibTableColumn
zxAnCpeSwUpdateTaskVerFileLoc = _ZxAnCpeSwUpdateTaskVerFileLoc_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 1, 1, 12),
    _ZxAnCpeSwUpdateTaskVerFileLoc_Type()
)
zxAnCpeSwUpdateTaskVerFileLoc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCpeSwUpdateTaskVerFileLoc.setStatus("current")


class _ZxAnCpeSwUpdateTaskFtpDir_Type(DisplayString):
    """Custom type zxAnCpeSwUpdateTaskFtpDir based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnCpeSwUpdateTaskFtpDir_Type.__name__ = "DisplayString"
_ZxAnCpeSwUpdateTaskFtpDir_Object = MibTableColumn
zxAnCpeSwUpdateTaskFtpDir = _ZxAnCpeSwUpdateTaskFtpDir_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 1, 1, 13),
    _ZxAnCpeSwUpdateTaskFtpDir_Type()
)
zxAnCpeSwUpdateTaskFtpDir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCpeSwUpdateTaskFtpDir.setStatus("current")


class _ZxAnCpeSwUpdateTaskExpiration_Type(DisplayString):
    """Custom type zxAnCpeSwUpdateTaskExpiration based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ZxAnCpeSwUpdateTaskExpiration_Type.__name__ = "DisplayString"
_ZxAnCpeSwUpdateTaskExpiration_Object = MibTableColumn
zxAnCpeSwUpdateTaskExpiration = _ZxAnCpeSwUpdateTaskExpiration_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 1, 1, 14),
    _ZxAnCpeSwUpdateTaskExpiration_Type()
)
zxAnCpeSwUpdateTaskExpiration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCpeSwUpdateTaskExpiration.setStatus("current")
_ZxAnCpeSwUpdateTaskAutoDelete_Type = TruthValue
_ZxAnCpeSwUpdateTaskAutoDelete_Object = MibTableColumn
zxAnCpeSwUpdateTaskAutoDelete = _ZxAnCpeSwUpdateTaskAutoDelete_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 1, 1, 15),
    _ZxAnCpeSwUpdateTaskAutoDelete_Type()
)
zxAnCpeSwUpdateTaskAutoDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCpeSwUpdateTaskAutoDelete.setStatus("current")
_ZxAnCpeSwUpdateTaskAutoUpdate_Type = TruthValue
_ZxAnCpeSwUpdateTaskAutoUpdate_Object = MibTableColumn
zxAnCpeSwUpdateTaskAutoUpdate = _ZxAnCpeSwUpdateTaskAutoUpdate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 1, 1, 16),
    _ZxAnCpeSwUpdateTaskAutoUpdate_Type()
)
zxAnCpeSwUpdateTaskAutoUpdate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCpeSwUpdateTaskAutoUpdate.setStatus("current")
_ZxAnCpeSwUpdateTaskRowStatus_Type = RowStatus
_ZxAnCpeSwUpdateTaskRowStatus_Object = MibTableColumn
zxAnCpeSwUpdateTaskRowStatus = _ZxAnCpeSwUpdateTaskRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 1, 1, 25),
    _ZxAnCpeSwUpdateTaskRowStatus_Type()
)
zxAnCpeSwUpdateTaskRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCpeSwUpdateTaskRowStatus.setStatus("current")
_ZxAnCpeSwUpdateTaskStatTable_Object = MibTable
zxAnCpeSwUpdateTaskStatTable = _ZxAnCpeSwUpdateTaskStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 2)
)
if mibBuilder.loadTexts:
    zxAnCpeSwUpdateTaskStatTable.setStatus("current")
_ZxAnCpeSwUpdateTaskStatEntry_Object = MibTableRow
zxAnCpeSwUpdateTaskStatEntry = _ZxAnCpeSwUpdateTaskStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 2, 1)
)
zxAnCpeSwUpdateTaskStatEntry.setIndexNames(
    (0, "ZTE-AN-EQUIP-MIB", "zxAnCpeSwUpdateTaskId"),
)
if mibBuilder.loadTexts:
    zxAnCpeSwUpdateTaskStatEntry.setStatus("current")
_ZxAnCpeSwUpateTotals_Type = Unsigned32
_ZxAnCpeSwUpateTotals_Object = MibTableColumn
zxAnCpeSwUpateTotals = _ZxAnCpeSwUpateTotals_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 2, 1, 1),
    _ZxAnCpeSwUpateTotals_Type()
)
zxAnCpeSwUpateTotals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCpeSwUpateTotals.setStatus("current")
_ZxAnCpeSwUpdateSucceeds_Type = Unsigned32
_ZxAnCpeSwUpdateSucceeds_Object = MibTableColumn
zxAnCpeSwUpdateSucceeds = _ZxAnCpeSwUpdateSucceeds_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 2, 1, 2),
    _ZxAnCpeSwUpdateSucceeds_Type()
)
zxAnCpeSwUpdateSucceeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCpeSwUpdateSucceeds.setStatus("current")
_ZxAnCpeSwUpdatings_Type = Unsigned32
_ZxAnCpeSwUpdatings_Object = MibTableColumn
zxAnCpeSwUpdatings = _ZxAnCpeSwUpdatings_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 2, 1, 3),
    _ZxAnCpeSwUpdatings_Type()
)
zxAnCpeSwUpdatings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCpeSwUpdatings.setStatus("current")
_ZxAnCpeSwUpdateFails_Type = Unsigned32
_ZxAnCpeSwUpdateFails_Object = MibTableColumn
zxAnCpeSwUpdateFails = _ZxAnCpeSwUpdateFails_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 2, 1, 4),
    _ZxAnCpeSwUpdateFails_Type()
)
zxAnCpeSwUpdateFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCpeSwUpdateFails.setStatus("current")
_ZxAnCpeSwAutoUpdateSucceeds_Type = Unsigned32
_ZxAnCpeSwAutoUpdateSucceeds_Object = MibTableColumn
zxAnCpeSwAutoUpdateSucceeds = _ZxAnCpeSwAutoUpdateSucceeds_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 2, 1, 5),
    _ZxAnCpeSwAutoUpdateSucceeds_Type()
)
zxAnCpeSwAutoUpdateSucceeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCpeSwAutoUpdateSucceeds.setStatus("current")
_ZxAnCpeSwUpdateTaskFailedTable_Object = MibTable
zxAnCpeSwUpdateTaskFailedTable = _ZxAnCpeSwUpdateTaskFailedTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 3)
)
if mibBuilder.loadTexts:
    zxAnCpeSwUpdateTaskFailedTable.setStatus("current")
_ZxAnCpeSwUpdateTaskFailedEntry_Object = MibTableRow
zxAnCpeSwUpdateTaskFailedEntry = _ZxAnCpeSwUpdateTaskFailedEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 3, 1)
)
zxAnCpeSwUpdateTaskFailedEntry.setIndexNames(
    (0, "ZTE-AN-EQUIP-MIB", "zxAnCpeSwUpdateTaskId"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnCpeSwRackNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnCpeSwShelfNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnCpeSwSlotNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnCpeSwPortNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnCpeSwOnuNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnCpeSwCircuitType"),
)
if mibBuilder.loadTexts:
    zxAnCpeSwUpdateTaskFailedEntry.setStatus("current")
_ZxAnCpeSwRackNo_Type = Integer32
_ZxAnCpeSwRackNo_Object = MibTableColumn
zxAnCpeSwRackNo = _ZxAnCpeSwRackNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 3, 1, 1),
    _ZxAnCpeSwRackNo_Type()
)
zxAnCpeSwRackNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnCpeSwRackNo.setStatus("current")
_ZxAnCpeSwShelfNo_Type = Integer32
_ZxAnCpeSwShelfNo_Object = MibTableColumn
zxAnCpeSwShelfNo = _ZxAnCpeSwShelfNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 3, 1, 2),
    _ZxAnCpeSwShelfNo_Type()
)
zxAnCpeSwShelfNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnCpeSwShelfNo.setStatus("current")
_ZxAnCpeSwSlotNo_Type = Integer32
_ZxAnCpeSwSlotNo_Object = MibTableColumn
zxAnCpeSwSlotNo = _ZxAnCpeSwSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 3, 1, 3),
    _ZxAnCpeSwSlotNo_Type()
)
zxAnCpeSwSlotNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnCpeSwSlotNo.setStatus("current")
_ZxAnCpeSwPortNo_Type = Integer32
_ZxAnCpeSwPortNo_Object = MibTableColumn
zxAnCpeSwPortNo = _ZxAnCpeSwPortNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 3, 1, 4),
    _ZxAnCpeSwPortNo_Type()
)
zxAnCpeSwPortNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnCpeSwPortNo.setStatus("current")
_ZxAnCpeSwOnuNo_Type = Integer32
_ZxAnCpeSwOnuNo_Object = MibTableColumn
zxAnCpeSwOnuNo = _ZxAnCpeSwOnuNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 3, 1, 5),
    _ZxAnCpeSwOnuNo_Type()
)
zxAnCpeSwOnuNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnCpeSwOnuNo.setStatus("current")


class _ZxAnCpeSwCircuitType_Type(Integer32):
    """Custom type zxAnCpeSwCircuitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              11)
        )
    )
    namedValues = NamedValues(
        *(("physicalPort", 1),
          ("bridgePort", 2),
          ("onu", 3),
          ("gemportOrLlid", 4),
          ("servicePort", 11))
    )


_ZxAnCpeSwCircuitType_Type.__name__ = "Integer32"
_ZxAnCpeSwCircuitType_Object = MibTableColumn
zxAnCpeSwCircuitType = _ZxAnCpeSwCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 3, 1, 6),
    _ZxAnCpeSwCircuitType_Type()
)
zxAnCpeSwCircuitType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnCpeSwCircuitType.setStatus("current")


class _ZxAnCpeSwUpdateTaskFailCpeName_Type(OctetString):
    """Custom type zxAnCpeSwUpdateTaskFailCpeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_ZxAnCpeSwUpdateTaskFailCpeName_Type.__name__ = "OctetString"
_ZxAnCpeSwUpdateTaskFailCpeName_Object = MibTableColumn
zxAnCpeSwUpdateTaskFailCpeName = _ZxAnCpeSwUpdateTaskFailCpeName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 3, 1, 7),
    _ZxAnCpeSwUpdateTaskFailCpeName_Type()
)
zxAnCpeSwUpdateTaskFailCpeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCpeSwUpdateTaskFailCpeName.setStatus("current")


class _ZxAnCpeSwUpdateTaskFailReason_Type(Integer32):
    """Custom type zxAnCpeSwUpdateTaskFailReason based on Integer32"""
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
        *(("none", 1),
          ("downloadFailed", 2),
          ("commitFailed", 3),
          ("activateFailed", 4),
          ("crcFailed", 5),
          ("validFailed", 6),
          ("userAborted", 7))
    )


_ZxAnCpeSwUpdateTaskFailReason_Type.__name__ = "Integer32"
_ZxAnCpeSwUpdateTaskFailReason_Object = MibTableColumn
zxAnCpeSwUpdateTaskFailReason = _ZxAnCpeSwUpdateTaskFailReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 3, 1, 8),
    _ZxAnCpeSwUpdateTaskFailReason_Type()
)
zxAnCpeSwUpdateTaskFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCpeSwUpdateTaskFailReason.setStatus("current")
_ZxAnCpeSwStatusTable_Object = MibTable
zxAnCpeSwStatusTable = _ZxAnCpeSwStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 4)
)
if mibBuilder.loadTexts:
    zxAnCpeSwStatusTable.setStatus("current")
_ZxAnCpeSwStatusEntry_Object = MibTableRow
zxAnCpeSwStatusEntry = _ZxAnCpeSwStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 4, 1)
)
zxAnCpeSwStatusEntry.setIndexNames(
    (0, "ZTE-AN-EQUIP-MIB", "zxAnCpeSwRackNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnCpeSwShelfNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnCpeSwSlotNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnCpeSwPortNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnCpeSwOnuNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnCpeSwCircuitType"),
)
if mibBuilder.loadTexts:
    zxAnCpeSwStatusEntry.setStatus("current")


class _ZxAnCpeSwCpeName_Type(DisplayString):
    """Custom type zxAnCpeSwCpeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnCpeSwCpeName_Type.__name__ = "DisplayString"
_ZxAnCpeSwCpeName_Object = MibTableColumn
zxAnCpeSwCpeName = _ZxAnCpeSwCpeName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 4, 1, 1),
    _ZxAnCpeSwCpeName_Type()
)
zxAnCpeSwCpeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCpeSwCpeName.setStatus("current")


class _ZxAnCpeSwUpdateStatus_Type(Integer32):
    """Custom type zxAnCpeSwUpdateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("notStart", 1),
          ("failed", 2),
          ("downloading", 3),
          ("commiting", 4),
          ("activating", 5),
          ("completed", 6))
    )


_ZxAnCpeSwUpdateStatus_Type.__name__ = "Integer32"
_ZxAnCpeSwUpdateStatus_Object = MibTableColumn
zxAnCpeSwUpdateStatus = _ZxAnCpeSwUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 4, 1, 2),
    _ZxAnCpeSwUpdateStatus_Type()
)
zxAnCpeSwUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCpeSwUpdateStatus.setStatus("current")


class _ZxAnCpeSwUpdateFailReason_Type(Integer32):
    """Custom type zxAnCpeSwUpdateFailReason based on Integer32"""
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
        *(("none", 1),
          ("downloadFailed", 2),
          ("commitFailed", 3),
          ("activateFailed", 4),
          ("crcFailed", 5),
          ("validFailed", 6),
          ("userAborted", 7))
    )


_ZxAnCpeSwUpdateFailReason_Type.__name__ = "Integer32"
_ZxAnCpeSwUpdateFailReason_Object = MibTableColumn
zxAnCpeSwUpdateFailReason = _ZxAnCpeSwUpdateFailReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 4, 1, 3),
    _ZxAnCpeSwUpdateFailReason_Type()
)
zxAnCpeSwUpdateFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCpeSwUpdateFailReason.setStatus("current")


class _ZxAnCpeSwUpdateProgress_Type(Integer32):
    """Custom type zxAnCpeSwUpdateProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnCpeSwUpdateProgress_Type.__name__ = "Integer32"
_ZxAnCpeSwUpdateProgress_Object = MibTableColumn
zxAnCpeSwUpdateProgress = _ZxAnCpeSwUpdateProgress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 4, 1, 4),
    _ZxAnCpeSwUpdateProgress_Type()
)
zxAnCpeSwUpdateProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCpeSwUpdateProgress.setStatus("current")


class _ZxAnCpeSwCurrVer_Type(DisplayString):
    """Custom type zxAnCpeSwCurrVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnCpeSwCurrVer_Type.__name__ = "DisplayString"
_ZxAnCpeSwCurrVer_Object = MibTableColumn
zxAnCpeSwCurrVer = _ZxAnCpeSwCurrVer_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 4, 1, 5),
    _ZxAnCpeSwCurrVer_Type()
)
zxAnCpeSwCurrVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCpeSwCurrVer.setStatus("current")


class _ZxAnCpeSwCurrVerBuildTime_Type(DisplayString):
    """Custom type zxAnCpeSwCurrVerBuildTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ZxAnCpeSwCurrVerBuildTime_Type.__name__ = "DisplayString"
_ZxAnCpeSwCurrVerBuildTime_Object = MibTableColumn
zxAnCpeSwCurrVerBuildTime = _ZxAnCpeSwCurrVerBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 4, 1, 6),
    _ZxAnCpeSwCurrVerBuildTime_Type()
)
zxAnCpeSwCurrVerBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCpeSwCurrVerBuildTime.setStatus("current")


class _ZxAnCpeSwUpdatingVer_Type(DisplayString):
    """Custom type zxAnCpeSwUpdatingVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnCpeSwUpdatingVer_Type.__name__ = "DisplayString"
_ZxAnCpeSwUpdatingVer_Object = MibTableColumn
zxAnCpeSwUpdatingVer = _ZxAnCpeSwUpdatingVer_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 4, 1, 7),
    _ZxAnCpeSwUpdatingVer_Type()
)
zxAnCpeSwUpdatingVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCpeSwUpdatingVer.setStatus("current")


class _ZxAnCpeSwUpdatingVerBuildTime_Type(DisplayString):
    """Custom type zxAnCpeSwUpdatingVerBuildTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ZxAnCpeSwUpdatingVerBuildTime_Type.__name__ = "DisplayString"
_ZxAnCpeSwUpdatingVerBuildTime_Object = MibTableColumn
zxAnCpeSwUpdatingVerBuildTime = _ZxAnCpeSwUpdatingVerBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 4, 1, 8),
    _ZxAnCpeSwUpdatingVerBuildTime_Type()
)
zxAnCpeSwUpdatingVerBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCpeSwUpdatingVerBuildTime.setStatus("current")


class _ZxAnCpeSwVendorId_Type(DisplayString):
    """Custom type zxAnCpeSwVendorId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnCpeSwVendorId_Type.__name__ = "DisplayString"
_ZxAnCpeSwVendorId_Object = MibTableColumn
zxAnCpeSwVendorId = _ZxAnCpeSwVendorId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 4, 1, 9),
    _ZxAnCpeSwVendorId_Type()
)
zxAnCpeSwVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCpeSwVendorId.setStatus("current")


class _ZxAnCpeSwProductId_Type(DisplayString):
    """Custom type zxAnCpeSwProductId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnCpeSwProductId_Type.__name__ = "DisplayString"
_ZxAnCpeSwProductId_Object = MibTableColumn
zxAnCpeSwProductId = _ZxAnCpeSwProductId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 6, 4, 1, 10),
    _ZxAnCpeSwProductId_Type()
)
zxAnCpeSwProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCpeSwProductId.setStatus("current")
_ZxAnVerAutoUpdateMgmt_ObjectIdentity = ObjectIdentity
zxAnVerAutoUpdateMgmt = _ZxAnVerAutoUpdateMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 7)
)


class _ZxAnVerAutoUpdateBootUpdateEn_Type(Integer32):
    """Custom type zxAnVerAutoUpdateBootUpdateEn based on Integer32"""
    defaultValue = 2

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


_ZxAnVerAutoUpdateBootUpdateEn_Type.__name__ = "Integer32"
_ZxAnVerAutoUpdateBootUpdateEn_Object = MibScalar
zxAnVerAutoUpdateBootUpdateEn = _ZxAnVerAutoUpdateBootUpdateEn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 7, 1),
    _ZxAnVerAutoUpdateBootUpdateEn_Type()
)
zxAnVerAutoUpdateBootUpdateEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVerAutoUpdateBootUpdateEn.setStatus("current")


class _ZxAnVerAutoUpdateVerBackupEn_Type(Integer32):
    """Custom type zxAnVerAutoUpdateVerBackupEn based on Integer32"""
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


_ZxAnVerAutoUpdateVerBackupEn_Type.__name__ = "Integer32"
_ZxAnVerAutoUpdateVerBackupEn_Object = MibScalar
zxAnVerAutoUpdateVerBackupEn = _ZxAnVerAutoUpdateVerBackupEn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 7, 2),
    _ZxAnVerAutoUpdateVerBackupEn_Type()
)
zxAnVerAutoUpdateVerBackupEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVerAutoUpdateVerBackupEn.setStatus("current")


class _ZxAnVerAutoUpdateVersionPath_Type(DisplayString):
    """Custom type zxAnVerAutoUpdateVersionPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnVerAutoUpdateVersionPath_Type.__name__ = "DisplayString"
_ZxAnVerAutoUpdateVersionPath_Object = MibScalar
zxAnVerAutoUpdateVersionPath = _ZxAnVerAutoUpdateVersionPath_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 7, 3),
    _ZxAnVerAutoUpdateVersionPath_Type()
)
zxAnVerAutoUpdateVersionPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVerAutoUpdateVersionPath.setStatus("current")


class _ZxAnVerAutoUpdateBackupPath_Type(DisplayString):
    """Custom type zxAnVerAutoUpdateBackupPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnVerAutoUpdateBackupPath_Type.__name__ = "DisplayString"
_ZxAnVerAutoUpdateBackupPath_Object = MibScalar
zxAnVerAutoUpdateBackupPath = _ZxAnVerAutoUpdateBackupPath_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 7, 4),
    _ZxAnVerAutoUpdateBackupPath_Type()
)
zxAnVerAutoUpdateBackupPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVerAutoUpdateBackupPath.setStatus("current")


class _ZxAnVerAutoUpdateLogPath_Type(DisplayString):
    """Custom type zxAnVerAutoUpdateLogPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnVerAutoUpdateLogPath_Type.__name__ = "DisplayString"
_ZxAnVerAutoUpdateLogPath_Object = MibScalar
zxAnVerAutoUpdateLogPath = _ZxAnVerAutoUpdateLogPath_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 7, 5),
    _ZxAnVerAutoUpdateLogPath_Type()
)
zxAnVerAutoUpdateLogPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVerAutoUpdateLogPath.setStatus("current")


class _ZxAnVerAutoUpdateAction_Type(Integer32):
    """Custom type zxAnVerAutoUpdateAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("start", 1)
    )


_ZxAnVerAutoUpdateAction_Type.__name__ = "Integer32"
_ZxAnVerAutoUpdateAction_Object = MibScalar
zxAnVerAutoUpdateAction = _ZxAnVerAutoUpdateAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 7, 6),
    _ZxAnVerAutoUpdateAction_Type()
)
zxAnVerAutoUpdateAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVerAutoUpdateAction.setStatus("current")


class _ZxAnVerAutoUpdateStatus_Type(Integer32):
    """Custom type zxAnVerAutoUpdateStatus based on Integer32"""
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
              12,
              13,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notStarted", 1),
          ("updateStarting", 2),
          ("backingUpFile", 3),
          ("versionAnalyzing", 4),
          ("versionDownloading", 5),
          ("versionDownloadComplete", 6),
          ("masterSlaveSynchronizing", 7),
          ("masterSlaveSyncComplete", 8),
          ("bootUpdating", 9),
          ("bootUpdateComplete", 10),
          ("versionLoading", 11),
          ("updateSuccess", 12),
          ("readyToReboot", 13),
          ("updateFailed", 255))
    )


_ZxAnVerAutoUpdateStatus_Type.__name__ = "Integer32"
_ZxAnVerAutoUpdateStatus_Object = MibScalar
zxAnVerAutoUpdateStatus = _ZxAnVerAutoUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 7, 7),
    _ZxAnVerAutoUpdateStatus_Type()
)
zxAnVerAutoUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVerAutoUpdateStatus.setStatus("current")


class _ZxAnVerAutoUpdateFailedReason_Type(Integer32):
    """Custom type zxAnVerAutoUpdateFailedReason based on Integer32"""
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
              12,
              13,
              255)
        )
    )
    namedValues = NamedValues(
        *(("backupDataFileError", 1),
          ("backupLogFileError", 2),
          ("backupConfigurationFileError", 3),
          ("backupVersionError", 4),
          ("analyzingConfigurationError", 5),
          ("analyzingVersionError", 6),
          ("diskFull", 7),
          ("downloadingVersionError", 8),
          ("masterSlaveSynchronizeError", 9),
          ("updateBootError", 10),
          ("loadingVersionError", 11),
          ("updateConflict", 12),
          ("unavailableServer", 13),
          ("otherError", 255))
    )


_ZxAnVerAutoUpdateFailedReason_Type.__name__ = "Integer32"
_ZxAnVerAutoUpdateFailedReason_Object = MibScalar
zxAnVerAutoUpdateFailedReason = _ZxAnVerAutoUpdateFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 2, 7, 8),
    _ZxAnVerAutoUpdateFailedReason_Type()
)
zxAnVerAutoUpdateFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVerAutoUpdateFailedReason.setStatus("current")
_ZxAnEnvMonitor_ObjectIdentity = ObjectIdentity
zxAnEnvMonitor = _ZxAnEnvMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3)
)


class _ZxAnEnvMgmtCapabilities_Type(Bits):
    """Custom type zxAnEnvMgmtCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("envTemperature", 0),
          ("fanAlarmBeep", 1),
          ("fanAutoSwitchByCardInstall", 2),
          ("fanSpeedCtrlBasedTemperature", 3),
          ("fanFixSpeed", 4),
          ("singleFanShutdown", 5),
          ("mpTemperature", 6),
          ("powerSupply", 7),
          ("cardTemperature", 8),
          ("fanSpeedPercentage", 9),
          ("backplaneInterface", 10),
          ("envMonitorInterfaceTrapEnable", 11),
          ("slaveShelfFanConfig", 12))
    )

_ZxAnEnvMgmtCapabilities_Type.__name__ = "Bits"
_ZxAnEnvMgmtCapabilities_Object = MibScalar
zxAnEnvMgmtCapabilities = _ZxAnEnvMgmtCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 1),
    _ZxAnEnvMgmtCapabilities_Type()
)
zxAnEnvMgmtCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEnvMgmtCapabilities.setStatus("current")
_ZxAnEnvTemperature_Type = Integer32
_ZxAnEnvTemperature_Object = MibScalar
zxAnEnvTemperature = _ZxAnEnvTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 2),
    _ZxAnEnvTemperature_Type()
)
zxAnEnvTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEnvTemperature.setStatus("current")
_ZxAnEnvTemperatureAlarmThreshold_Type = Integer32
_ZxAnEnvTemperatureAlarmThreshold_Object = MibScalar
zxAnEnvTemperatureAlarmThreshold = _ZxAnEnvTemperatureAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 3),
    _ZxAnEnvTemperatureAlarmThreshold_Type()
)
zxAnEnvTemperatureAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvTemperatureAlarmThreshold.setStatus("current")


class _ZxAnEnvMonitorInterfaceUsage_Type(Integer32):
    """Custom type zxAnEnvMonitorInterfaceUsage based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("epm", 1),
          ("fanTray", 2),
          ("noUse", 3),
          ("noSupport", 4),
          ("etmWithTestSubcard", 5),
          ("etmWithoutTestSubcard", 6))
    )


_ZxAnEnvMonitorInterfaceUsage_Type.__name__ = "Integer32"
_ZxAnEnvMonitorInterfaceUsage_Object = MibScalar
zxAnEnvMonitorInterfaceUsage = _ZxAnEnvMonitorInterfaceUsage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 4),
    _ZxAnEnvMonitorInterfaceUsage_Type()
)
zxAnEnvMonitorInterfaceUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvMonitorInterfaceUsage.setStatus("current")
_ZxAnMPTemperature_Type = Integer32
_ZxAnMPTemperature_Object = MibScalar
zxAnMPTemperature = _ZxAnMPTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 5),
    _ZxAnMPTemperature_Type()
)
zxAnMPTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMPTemperature.setStatus("current")
_ZxAnMPTemperatureAlarmThreshold_Type = Integer32
_ZxAnMPTemperatureAlarmThreshold_Object = MibScalar
zxAnMPTemperatureAlarmThreshold = _ZxAnMPTemperatureAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 6),
    _ZxAnMPTemperatureAlarmThreshold_Type()
)
zxAnMPTemperatureAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMPTemperatureAlarmThreshold.setStatus("current")


class _ZxAnEpmConnectPort_Type(Integer32):
    """Custom type zxAnEpmConnectPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("port0", 1),
          ("port1", 2),
          ("notconfigured", 255))
    )


_ZxAnEpmConnectPort_Type.__name__ = "Integer32"
_ZxAnEpmConnectPort_Object = MibScalar
zxAnEpmConnectPort = _ZxAnEpmConnectPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 7),
    _ZxAnEpmConnectPort_Type()
)
zxAnEpmConnectPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEpmConnectPort.setStatus("current")


class _ZxAnEnvBackplaneInterfaceUsage_Type(Integer32):
    """Custom type zxAnEnvBackplaneInterfaceUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("fan", 1),
          ("noUse", 3),
          ("noSupport", 255))
    )


_ZxAnEnvBackplaneInterfaceUsage_Type.__name__ = "Integer32"
_ZxAnEnvBackplaneInterfaceUsage_Object = MibScalar
zxAnEnvBackplaneInterfaceUsage = _ZxAnEnvBackplaneInterfaceUsage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 8),
    _ZxAnEnvBackplaneInterfaceUsage_Type()
)
zxAnEnvBackplaneInterfaceUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvBackplaneInterfaceUsage.setStatus("current")
_ZxAnEnvPowerSupplyMgmt_ObjectIdentity = ObjectIdentity
zxAnEnvPowerSupplyMgmt = _ZxAnEnvPowerSupplyMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 9)
)
_ZxAnPowerSupplyCount_Type = Integer32
_ZxAnPowerSupplyCount_Object = MibScalar
zxAnPowerSupplyCount = _ZxAnPowerSupplyCount_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 9, 1),
    _ZxAnPowerSupplyCount_Type()
)
zxAnPowerSupplyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPowerSupplyCount.setStatus("current")
_ZxAnPowerSupplyTable_Object = MibTable
zxAnPowerSupplyTable = _ZxAnPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 9, 2)
)
if mibBuilder.loadTexts:
    zxAnPowerSupplyTable.setStatus("current")
_ZxAnPowerSupplyEntry_Object = MibTableRow
zxAnPowerSupplyEntry = _ZxAnPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 9, 2, 1)
)
zxAnPowerSupplyEntry.setIndexNames(
    (0, "ZTE-AN-EQUIP-MIB", "zxAnRackNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnShelfNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnSlotNo"),
)
if mibBuilder.loadTexts:
    zxAnPowerSupplyEntry.setStatus("current")


class _ZxAnPowerSupplyInVoltageStatus_Type(Integer32):
    """Custom type zxAnPowerSupplyInVoltageStatus based on Integer32"""
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
        *(("normal", 1),
          ("overVoltage", 2),
          ("underVoltage", 3),
          ("off", 4))
    )


_ZxAnPowerSupplyInVoltageStatus_Type.__name__ = "Integer32"
_ZxAnPowerSupplyInVoltageStatus_Object = MibTableColumn
zxAnPowerSupplyInVoltageStatus = _ZxAnPowerSupplyInVoltageStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 9, 2, 1, 1),
    _ZxAnPowerSupplyInVoltageStatus_Type()
)
zxAnPowerSupplyInVoltageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPowerSupplyInVoltageStatus.setStatus("current")


class _ZxAnPowerSupplyOperState_Type(Integer32):
    """Custom type zxAnPowerSupplyOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("hwOffline", 2),
          ("powerFaulty", 3))
    )


_ZxAnPowerSupplyOperState_Type.__name__ = "Integer32"
_ZxAnPowerSupplyOperState_Object = MibTableColumn
zxAnPowerSupplyOperState = _ZxAnPowerSupplyOperState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 9, 2, 1, 2),
    _ZxAnPowerSupplyOperState_Type()
)
zxAnPowerSupplyOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPowerSupplyOperState.setStatus("current")
_ZxAnPowerSupplyInVoltage_Type = Integer32
_ZxAnPowerSupplyInVoltage_Object = MibTableColumn
zxAnPowerSupplyInVoltage = _ZxAnPowerSupplyInVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 9, 2, 1, 3),
    _ZxAnPowerSupplyInVoltage_Type()
)
zxAnPowerSupplyInVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPowerSupplyInVoltage.setStatus("current")
if mibBuilder.loadTexts:
    zxAnPowerSupplyInVoltage.setUnits("0.001V")


class _ZxAnPowerInVoltageUpperThresh_Type(Integer32):
    """Custom type zxAnPowerInVoltageUpperThresh based on Integer32"""
    defaultValue = 0


_ZxAnPowerInVoltageUpperThresh_Type.__name__ = "Integer32"
_ZxAnPowerInVoltageUpperThresh_Object = MibTableColumn
zxAnPowerInVoltageUpperThresh = _ZxAnPowerInVoltageUpperThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 9, 2, 1, 4),
    _ZxAnPowerInVoltageUpperThresh_Type()
)
zxAnPowerInVoltageUpperThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPowerInVoltageUpperThresh.setStatus("current")
if mibBuilder.loadTexts:
    zxAnPowerInVoltageUpperThresh.setUnits("0.001V")


class _ZxAnPowerInVoltageLowerThresh_Type(Integer32):
    """Custom type zxAnPowerInVoltageLowerThresh based on Integer32"""
    defaultValue = 0


_ZxAnPowerInVoltageLowerThresh_Type.__name__ = "Integer32"
_ZxAnPowerInVoltageLowerThresh_Object = MibTableColumn
zxAnPowerInVoltageLowerThresh = _ZxAnPowerInVoltageLowerThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 9, 2, 1, 5),
    _ZxAnPowerInVoltageLowerThresh_Type()
)
zxAnPowerInVoltageLowerThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPowerInVoltageLowerThresh.setStatus("current")
if mibBuilder.loadTexts:
    zxAnPowerInVoltageLowerThresh.setUnits("0.001V")
_ZxAnPowerSupplyInCurrent_Type = Integer32
_ZxAnPowerSupplyInCurrent_Object = MibTableColumn
zxAnPowerSupplyInCurrent = _ZxAnPowerSupplyInCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 9, 2, 1, 6),
    _ZxAnPowerSupplyInCurrent_Type()
)
zxAnPowerSupplyInCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPowerSupplyInCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnPowerSupplyInCurrent.setUnits("0.001A")


class _ZxAnPowerInCurrentThresh_Type(Integer32):
    """Custom type zxAnPowerInCurrentThresh based on Integer32"""
    defaultValue = 0


_ZxAnPowerInCurrentThresh_Type.__name__ = "Integer32"
_ZxAnPowerInCurrentThresh_Object = MibTableColumn
zxAnPowerInCurrentThresh = _ZxAnPowerInCurrentThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 9, 2, 1, 7),
    _ZxAnPowerInCurrentThresh_Type()
)
zxAnPowerInCurrentThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPowerInCurrentThresh.setStatus("current")
if mibBuilder.loadTexts:
    zxAnPowerInCurrentThresh.setUnits("0.001A")
_ZxAnPowerSupplyInPower_Type = Integer32
_ZxAnPowerSupplyInPower_Object = MibTableColumn
zxAnPowerSupplyInPower = _ZxAnPowerSupplyInPower_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 9, 2, 1, 8),
    _ZxAnPowerSupplyInPower_Type()
)
zxAnPowerSupplyInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPowerSupplyInPower.setStatus("current")
if mibBuilder.loadTexts:
    zxAnPowerSupplyInPower.setUnits("Watts")
_ZxAnEnvFanMgmt_ObjectIdentity = ObjectIdentity
zxAnEnvFanMgmt = _ZxAnEnvFanMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 10)
)


class _ZxAnEnvFanAlarmBeepEnable_Type(Integer32):
    """Custom type zxAnEnvFanAlarmBeepEnable based on Integer32"""
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


_ZxAnEnvFanAlarmBeepEnable_Type.__name__ = "Integer32"
_ZxAnEnvFanAlarmBeepEnable_Object = MibScalar
zxAnEnvFanAlarmBeepEnable = _ZxAnEnvFanAlarmBeepEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 10, 1),
    _ZxAnEnvFanAlarmBeepEnable_Type()
)
zxAnEnvFanAlarmBeepEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvFanAlarmBeepEnable.setStatus("current")


class _ZxAnEnvFanAutoSwitchByCardInst_Type(Integer32):
    """Custom type zxAnEnvFanAutoSwitchByCardInst based on Integer32"""
    defaultValue = 2

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


_ZxAnEnvFanAutoSwitchByCardInst_Type.__name__ = "Integer32"
_ZxAnEnvFanAutoSwitchByCardInst_Object = MibScalar
zxAnEnvFanAutoSwitchByCardInst = _ZxAnEnvFanAutoSwitchByCardInst_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 10, 2),
    _ZxAnEnvFanAutoSwitchByCardInst_Type()
)
zxAnEnvFanAutoSwitchByCardInst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvFanAutoSwitchByCardInst.setStatus("current")
_ZxAnEnvFanTrayHardwareVersion_Type = DisplayString
_ZxAnEnvFanTrayHardwareVersion_Object = MibScalar
zxAnEnvFanTrayHardwareVersion = _ZxAnEnvFanTrayHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 10, 3),
    _ZxAnEnvFanTrayHardwareVersion_Type()
)
zxAnEnvFanTrayHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEnvFanTrayHardwareVersion.setStatus("current")
_ZxAnEnvFanTraySoftwareVersion_Type = DisplayString
_ZxAnEnvFanTraySoftwareVersion_Object = MibScalar
zxAnEnvFanTraySoftwareVersion = _ZxAnEnvFanTraySoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 10, 4),
    _ZxAnEnvFanTraySoftwareVersion_Type()
)
zxAnEnvFanTraySoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEnvFanTraySoftwareVersion.setStatus("current")


class _ZxAnEnvFanInvSn_Type(DisplayString):
    """Custom type zxAnEnvFanInvSn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnEnvFanInvSn_Type.__name__ = "DisplayString"
_ZxAnEnvFanInvSn_Object = MibScalar
zxAnEnvFanInvSn = _ZxAnEnvFanInvSn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 10, 5),
    _ZxAnEnvFanInvSn_Type()
)
zxAnEnvFanInvSn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvFanInvSn.setStatus("current")
_ZxAnEnvFanSpeedCtrlMgmt_ObjectIdentity = ObjectIdentity
zxAnEnvFanSpeedCtrlMgmt = _ZxAnEnvFanSpeedCtrlMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 10, 10)
)


class _ZxAnEnvFanSpeedCtrlMode_Type(Integer32):
    """Custom type zxAnEnvFanSpeedCtrlMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("temperatureBasedAutoCtrl", 1),
          ("fixSpeed", 2))
    )


_ZxAnEnvFanSpeedCtrlMode_Type.__name__ = "Integer32"
_ZxAnEnvFanSpeedCtrlMode_Object = MibScalar
zxAnEnvFanSpeedCtrlMode = _ZxAnEnvFanSpeedCtrlMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 10, 10, 1),
    _ZxAnEnvFanSpeedCtrlMode_Type()
)
zxAnEnvFanSpeedCtrlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvFanSpeedCtrlMode.setStatus("current")
_ZxAnEnvFanLowSpeed_Type = Integer32
_ZxAnEnvFanLowSpeed_Object = MibScalar
zxAnEnvFanLowSpeed = _ZxAnEnvFanLowSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 10, 10, 2),
    _ZxAnEnvFanLowSpeed_Type()
)
zxAnEnvFanLowSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvFanLowSpeed.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEnvFanLowSpeed.setUnits("RPM")
_ZxAnEnvFanStandardSpeed_Type = Integer32
_ZxAnEnvFanStandardSpeed_Object = MibScalar
zxAnEnvFanStandardSpeed = _ZxAnEnvFanStandardSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 10, 10, 3),
    _ZxAnEnvFanStandardSpeed_Type()
)
zxAnEnvFanStandardSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvFanStandardSpeed.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEnvFanStandardSpeed.setUnits("RPM")
_ZxAnEnvFanHighSpeed_Type = Integer32
_ZxAnEnvFanHighSpeed_Object = MibScalar
zxAnEnvFanHighSpeed = _ZxAnEnvFanHighSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 10, 10, 4),
    _ZxAnEnvFanHighSpeed_Type()
)
zxAnEnvFanHighSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvFanHighSpeed.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEnvFanHighSpeed.setUnits("RPM")
_ZxAnEnvFanSuperSpeed_Type = Integer32
_ZxAnEnvFanSuperSpeed_Object = MibScalar
zxAnEnvFanSuperSpeed = _ZxAnEnvFanSuperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 10, 10, 5),
    _ZxAnEnvFanSuperSpeed_Type()
)
zxAnEnvFanSuperSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvFanSuperSpeed.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEnvFanSuperSpeed.setUnits("RPM")
_ZxAnEnvFanLowSpeedShiftTem_Type = Integer32
_ZxAnEnvFanLowSpeedShiftTem_Object = MibScalar
zxAnEnvFanLowSpeedShiftTem = _ZxAnEnvFanLowSpeedShiftTem_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 10, 10, 6),
    _ZxAnEnvFanLowSpeedShiftTem_Type()
)
zxAnEnvFanLowSpeedShiftTem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvFanLowSpeedShiftTem.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEnvFanLowSpeedShiftTem.setUnits("centigrade")
_ZxAnEnvFanStdSpeedShiftTem_Type = Integer32
_ZxAnEnvFanStdSpeedShiftTem_Object = MibScalar
zxAnEnvFanStdSpeedShiftTem = _ZxAnEnvFanStdSpeedShiftTem_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 10, 10, 7),
    _ZxAnEnvFanStdSpeedShiftTem_Type()
)
zxAnEnvFanStdSpeedShiftTem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvFanStdSpeedShiftTem.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEnvFanStdSpeedShiftTem.setUnits("centigrade")
_ZxAnEnvFanHighSpeedShiftTem_Type = Integer32
_ZxAnEnvFanHighSpeedShiftTem_Object = MibScalar
zxAnEnvFanHighSpeedShiftTem = _ZxAnEnvFanHighSpeedShiftTem_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 10, 10, 8),
    _ZxAnEnvFanHighSpeedShiftTem_Type()
)
zxAnEnvFanHighSpeedShiftTem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvFanHighSpeedShiftTem.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEnvFanHighSpeedShiftTem.setUnits("centigrade")
_ZxAnEnvFanSuperSpeedShiftTem_Type = Integer32
_ZxAnEnvFanSuperSpeedShiftTem_Object = MibScalar
zxAnEnvFanSuperSpeedShiftTem = _ZxAnEnvFanSuperSpeedShiftTem_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 10, 10, 9),
    _ZxAnEnvFanSuperSpeedShiftTem_Type()
)
zxAnEnvFanSuperSpeedShiftTem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvFanSuperSpeedShiftTem.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEnvFanSuperSpeedShiftTem.setUnits("centigrade")
_ZxAnEnvFanTable_Object = MibTable
zxAnEnvFanTable = _ZxAnEnvFanTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 10, 10, 10)
)
if mibBuilder.loadTexts:
    zxAnEnvFanTable.setStatus("current")
_ZxAnEnvFanEntry_Object = MibTableRow
zxAnEnvFanEntry = _ZxAnEnvFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 10, 10, 10, 1)
)
zxAnEnvFanEntry.setIndexNames(
    (0, "ZTE-AN-EQUIP-MIB", "zxAnEnvFanIndex"),
)
if mibBuilder.loadTexts:
    zxAnEnvFanEntry.setStatus("current")
_ZxAnEnvFanIndex_Type = Integer32
_ZxAnEnvFanIndex_Object = MibTableColumn
zxAnEnvFanIndex = _ZxAnEnvFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 10, 10, 10, 1, 1),
    _ZxAnEnvFanIndex_Type()
)
zxAnEnvFanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEnvFanIndex.setStatus("current")


class _ZxAnEnvFanConfSpeedLevel_Type(Integer32):
    """Custom type zxAnEnvFanConfSpeedLevel based on Integer32"""
    defaultValue = 2

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
        *(("lowSpeed", 1),
          ("standardSpeed", 2),
          ("highSpeed", 3),
          ("superSpeed", 4))
    )


_ZxAnEnvFanConfSpeedLevel_Type.__name__ = "Integer32"
_ZxAnEnvFanConfSpeedLevel_Object = MibTableColumn
zxAnEnvFanConfSpeedLevel = _ZxAnEnvFanConfSpeedLevel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 10, 10, 10, 1, 2),
    _ZxAnEnvFanConfSpeedLevel_Type()
)
zxAnEnvFanConfSpeedLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEnvFanConfSpeedLevel.setStatus("current")


class _ZxAnEnvFanActualSpeedLevel_Type(Integer32):
    """Custom type zxAnEnvFanActualSpeedLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("lowSpeed", 1),
          ("standardSpeed", 2),
          ("highSpeed", 3),
          ("superSpeed", 4),
          ("other", 10))
    )


_ZxAnEnvFanActualSpeedLevel_Type.__name__ = "Integer32"
_ZxAnEnvFanActualSpeedLevel_Object = MibTableColumn
zxAnEnvFanActualSpeedLevel = _ZxAnEnvFanActualSpeedLevel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 10, 10, 10, 1, 3),
    _ZxAnEnvFanActualSpeedLevel_Type()
)
zxAnEnvFanActualSpeedLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEnvFanActualSpeedLevel.setStatus("current")


class _ZxAnEnvFanAdminStatus_Type(Integer32):
    """Custom type zxAnEnvFanAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_ZxAnEnvFanAdminStatus_Type.__name__ = "Integer32"
_ZxAnEnvFanAdminStatus_Object = MibTableColumn
zxAnEnvFanAdminStatus = _ZxAnEnvFanAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 10, 10, 10, 1, 4),
    _ZxAnEnvFanAdminStatus_Type()
)
zxAnEnvFanAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEnvFanAdminStatus.setStatus("current")


class _ZxAnEnvFanOperStatus_Type(Integer32):
    """Custom type zxAnEnvFanOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("unknown", 3))
    )


_ZxAnEnvFanOperStatus_Type.__name__ = "Integer32"
_ZxAnEnvFanOperStatus_Object = MibTableColumn
zxAnEnvFanOperStatus = _ZxAnEnvFanOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 10, 10, 10, 1, 5),
    _ZxAnEnvFanOperStatus_Type()
)
zxAnEnvFanOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEnvFanOperStatus.setStatus("current")


class _ZxAnEnvFanOnlineStatus_Type(Integer32):
    """Custom type zxAnEnvFanOnlineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("online", 1),
          ("offline", 2),
          ("unknown", 3))
    )


_ZxAnEnvFanOnlineStatus_Type.__name__ = "Integer32"
_ZxAnEnvFanOnlineStatus_Object = MibTableColumn
zxAnEnvFanOnlineStatus = _ZxAnEnvFanOnlineStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 10, 10, 10, 1, 6),
    _ZxAnEnvFanOnlineStatus_Type()
)
zxAnEnvFanOnlineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEnvFanOnlineStatus.setStatus("current")
_ZxAnEnvFanActualSpeed_Type = Integer32
_ZxAnEnvFanActualSpeed_Object = MibTableColumn
zxAnEnvFanActualSpeed = _ZxAnEnvFanActualSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 10, 10, 10, 1, 7),
    _ZxAnEnvFanActualSpeed_Type()
)
zxAnEnvFanActualSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEnvFanActualSpeed.setStatus("current")


class _ZxAnEnvFanLowSpeedPercentage_Type(Integer32):
    """Custom type zxAnEnvFanLowSpeedPercentage based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 97),
    )


_ZxAnEnvFanLowSpeedPercentage_Type.__name__ = "Integer32"
_ZxAnEnvFanLowSpeedPercentage_Object = MibScalar
zxAnEnvFanLowSpeedPercentage = _ZxAnEnvFanLowSpeedPercentage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 10, 10, 11),
    _ZxAnEnvFanLowSpeedPercentage_Type()
)
zxAnEnvFanLowSpeedPercentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvFanLowSpeedPercentage.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEnvFanLowSpeedPercentage.setUnits("percent")


class _ZxAnEnvFanStandardSpeedPercent_Type(Integer32):
    """Custom type zxAnEnvFanStandardSpeedPercent based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 98),
    )


_ZxAnEnvFanStandardSpeedPercent_Type.__name__ = "Integer32"
_ZxAnEnvFanStandardSpeedPercent_Object = MibScalar
zxAnEnvFanStandardSpeedPercent = _ZxAnEnvFanStandardSpeedPercent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 10, 10, 12),
    _ZxAnEnvFanStandardSpeedPercent_Type()
)
zxAnEnvFanStandardSpeedPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvFanStandardSpeedPercent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEnvFanStandardSpeedPercent.setUnits("percent")


class _ZxAnEnvFanHighSpeedPercentage_Type(Integer32):
    """Custom type zxAnEnvFanHighSpeedPercentage based on Integer32"""
    defaultValue = 70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 99),
    )


_ZxAnEnvFanHighSpeedPercentage_Type.__name__ = "Integer32"
_ZxAnEnvFanHighSpeedPercentage_Object = MibScalar
zxAnEnvFanHighSpeedPercentage = _ZxAnEnvFanHighSpeedPercentage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 10, 10, 13),
    _ZxAnEnvFanHighSpeedPercentage_Type()
)
zxAnEnvFanHighSpeedPercentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvFanHighSpeedPercentage.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEnvFanHighSpeedPercentage.setUnits("percent")


class _ZxAnEnvFanSuperSpeedPercentage_Type(Integer32):
    """Custom type zxAnEnvFanSuperSpeedPercentage based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 100),
    )


_ZxAnEnvFanSuperSpeedPercentage_Type.__name__ = "Integer32"
_ZxAnEnvFanSuperSpeedPercentage_Object = MibScalar
zxAnEnvFanSuperSpeedPercentage = _ZxAnEnvFanSuperSpeedPercentage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 10, 10, 14),
    _ZxAnEnvFanSuperSpeedPercentage_Type()
)
zxAnEnvFanSuperSpeedPercentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvFanSuperSpeedPercentage.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEnvFanSuperSpeedPercentage.setUnits("percent")
_ZxAnEnvDustCapMgmt_ObjectIdentity = ObjectIdentity
zxAnEnvDustCapMgmt = _ZxAnEnvDustCapMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 11)
)
_ZxAnEnvDustCapOperStatus_Type = RowStatus
_ZxAnEnvDustCapOperStatus_Object = MibScalar
zxAnEnvDustCapOperStatus = _ZxAnEnvDustCapOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 11, 1),
    _ZxAnEnvDustCapOperStatus_Type()
)
zxAnEnvDustCapOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvDustCapOperStatus.setStatus("current")


class _ZxAnEnvMonitorIfTrapEnable_Type(Integer32):
    """Custom type zxAnEnvMonitorIfTrapEnable based on Integer32"""
    defaultValue = 2

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


_ZxAnEnvMonitorIfTrapEnable_Type.__name__ = "Integer32"
_ZxAnEnvMonitorIfTrapEnable_Object = MibScalar
zxAnEnvMonitorIfTrapEnable = _ZxAnEnvMonitorIfTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 12),
    _ZxAnEnvMonitorIfTrapEnable_Type()
)
zxAnEnvMonitorIfTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvMonitorIfTrapEnable.setStatus("current")
_ZxAnEnvCardMgmt_ObjectIdentity = ObjectIdentity
zxAnEnvCardMgmt = _ZxAnEnvCardMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 13)
)
_ZxAnEnvCardTemperatureTable_Object = MibTable
zxAnEnvCardTemperatureTable = _ZxAnEnvCardTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 13, 5)
)
if mibBuilder.loadTexts:
    zxAnEnvCardTemperatureTable.setStatus("current")
_ZxAnEnvCardTemperatureEntry_Object = MibTableRow
zxAnEnvCardTemperatureEntry = _ZxAnEnvCardTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 13, 5, 1)
)
zxAnEnvCardTemperatureEntry.setIndexNames(
    (0, "ZTE-AN-EQUIP-MIB", "zxAnRackNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnShelfNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnSlotNo"),
)
if mibBuilder.loadTexts:
    zxAnEnvCardTemperatureEntry.setStatus("current")
_ZxAnEnvCardTemperature_Type = Integer32
_ZxAnEnvCardTemperature_Object = MibTableColumn
zxAnEnvCardTemperature = _ZxAnEnvCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 13, 5, 1, 1),
    _ZxAnEnvCardTemperature_Type()
)
zxAnEnvCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEnvCardTemperature.setStatus("current")
_ZxAnEnvOverheatProtectionMgmt_ObjectIdentity = ObjectIdentity
zxAnEnvOverheatProtectionMgmt = _ZxAnEnvOverheatProtectionMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 14)
)
_ZxAnEnvOverheatProtectionObjects_ObjectIdentity = ObjectIdentity
zxAnEnvOverheatProtectionObjects = _ZxAnEnvOverheatProtectionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 14, 1)
)


class _ZxAnEnvOverheatProtectionEnable_Type(TruthValue):
    """Custom type zxAnEnvOverheatProtectionEnable based on TruthValue"""
    defaultValue = 2


_ZxAnEnvOverheatProtectionEnable_Type.__name__ = "TruthValue"
_ZxAnEnvOverheatProtectionEnable_Object = MibScalar
zxAnEnvOverheatProtectionEnable = _ZxAnEnvOverheatProtectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 14, 1, 1),
    _ZxAnEnvOverheatProtectionEnable_Type()
)
zxAnEnvOverheatProtectionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvOverheatProtectionEnable.setStatus("current")


class _ZxAnEnvOverheatTmpThreshold_Type(Integer32):
    """Custom type zxAnEnvOverheatTmpThreshold based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_ZxAnEnvOverheatTmpThreshold_Type.__name__ = "Integer32"
_ZxAnEnvOverheatTmpThreshold_Object = MibScalar
zxAnEnvOverheatTmpThreshold = _ZxAnEnvOverheatTmpThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 14, 1, 2),
    _ZxAnEnvOverheatTmpThreshold_Type()
)
zxAnEnvOverheatTmpThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvOverheatTmpThreshold.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEnvOverheatTmpThreshold.setUnits("centigrade")


class _ZxAnEnvOverheatDurThreshold_Type(Integer32):
    """Custom type zxAnEnvOverheatDurThreshold based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ZxAnEnvOverheatDurThreshold_Type.__name__ = "Integer32"
_ZxAnEnvOverheatDurThreshold_Object = MibScalar
zxAnEnvOverheatDurThreshold = _ZxAnEnvOverheatDurThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 14, 1, 3),
    _ZxAnEnvOverheatDurThreshold_Type()
)
zxAnEnvOverheatDurThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvOverheatDurThreshold.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEnvOverheatDurThreshold.setUnits("seconds")


class _ZxAnEnvOverheatAutoRecoveryType_Type(Integer32):
    """Custom type zxAnEnvOverheatAutoRecoveryType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("byTemperature", 1),
          ("byTime", 2))
    )


_ZxAnEnvOverheatAutoRecoveryType_Type.__name__ = "Integer32"
_ZxAnEnvOverheatAutoRecoveryType_Object = MibScalar
zxAnEnvOverheatAutoRecoveryType = _ZxAnEnvOverheatAutoRecoveryType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 14, 1, 25),
    _ZxAnEnvOverheatAutoRecoveryType_Type()
)
zxAnEnvOverheatAutoRecoveryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvOverheatAutoRecoveryType.setStatus("current")


class _ZxAnEnvOverheatAutoRecoveryEn_Type(TruthValue):
    """Custom type zxAnEnvOverheatAutoRecoveryEn based on TruthValue"""
    defaultValue = 2


_ZxAnEnvOverheatAutoRecoveryEn_Type.__name__ = "TruthValue"
_ZxAnEnvOverheatAutoRecoveryEn_Object = MibScalar
zxAnEnvOverheatAutoRecoveryEn = _ZxAnEnvOverheatAutoRecoveryEn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 14, 1, 30),
    _ZxAnEnvOverheatAutoRecoveryEn_Type()
)
zxAnEnvOverheatAutoRecoveryEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvOverheatAutoRecoveryEn.setStatus("current")


class _ZxAnEnvAutoRecoveryTmpThreshold_Type(Integer32):
    """Custom type zxAnEnvAutoRecoveryTmpThreshold based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ZxAnEnvAutoRecoveryTmpThreshold_Type.__name__ = "Integer32"
_ZxAnEnvAutoRecoveryTmpThreshold_Object = MibScalar
zxAnEnvAutoRecoveryTmpThreshold = _ZxAnEnvAutoRecoveryTmpThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 14, 1, 31),
    _ZxAnEnvAutoRecoveryTmpThreshold_Type()
)
zxAnEnvAutoRecoveryTmpThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvAutoRecoveryTmpThreshold.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEnvAutoRecoveryTmpThreshold.setUnits("centigrade")


class _ZxAnEnvOverheatAutoRecoveryTime_Type(Integer32):
    """Custom type zxAnEnvOverheatAutoRecoveryTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_ZxAnEnvOverheatAutoRecoveryTime_Type.__name__ = "Integer32"
_ZxAnEnvOverheatAutoRecoveryTime_Object = MibScalar
zxAnEnvOverheatAutoRecoveryTime = _ZxAnEnvOverheatAutoRecoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 14, 1, 40),
    _ZxAnEnvOverheatAutoRecoveryTime_Type()
)
zxAnEnvOverheatAutoRecoveryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvOverheatAutoRecoveryTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEnvOverheatAutoRecoveryTime.setUnits("minutes")


class _ZxAnEnvOverheatProtectionStatus_Type(Integer32):
    """Custom type zxAnEnvOverheatProtectionStatus based on Integer32"""
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
        *(("normal", 1),
          ("broadbandServiceStopped", 2),
          ("narrowbandServiceStopped", 3),
          ("allServiceStopped", 4))
    )


_ZxAnEnvOverheatProtectionStatus_Type.__name__ = "Integer32"
_ZxAnEnvOverheatProtectionStatus_Object = MibScalar
zxAnEnvOverheatProtectionStatus = _ZxAnEnvOverheatProtectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 14, 1, 50),
    _ZxAnEnvOverheatProtectionStatus_Type()
)
zxAnEnvOverheatProtectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEnvOverheatProtectionStatus.setStatus("current")
_ZxAnEnvBatteryObjects_ObjectIdentity = ObjectIdentity
zxAnEnvBatteryObjects = _ZxAnEnvBatteryObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 15)
)
_ZxAnEnvBatteryGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnEnvBatteryGlobalObjects = _ZxAnEnvBatteryGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 15, 1)
)


class _ZxAnEnvBatteryEnergySavingEnable_Type(Integer32):
    """Custom type zxAnEnvBatteryEnergySavingEnable based on Integer32"""
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


_ZxAnEnvBatteryEnergySavingEnable_Type.__name__ = "Integer32"
_ZxAnEnvBatteryEnergySavingEnable_Object = MibScalar
zxAnEnvBatteryEnergySavingEnable = _ZxAnEnvBatteryEnergySavingEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 15, 1, 1),
    _ZxAnEnvBatteryEnergySavingEnable_Type()
)
zxAnEnvBatteryEnergySavingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvBatteryEnergySavingEnable.setStatus("current")
_ZxAnEnvDeviceObjects_ObjectIdentity = ObjectIdentity
zxAnEnvDeviceObjects = _ZxAnEnvDeviceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 16)
)
_ZxAnEnvDeviceTable_Object = MibTable
zxAnEnvDeviceTable = _ZxAnEnvDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 16, 2)
)
if mibBuilder.loadTexts:
    zxAnEnvDeviceTable.setStatus("current")
_ZxAnEnvDeviceEntry_Object = MibTableRow
zxAnEnvDeviceEntry = _ZxAnEnvDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 16, 2, 1)
)
zxAnEnvDeviceEntry.setIndexNames(
    (0, "ZTE-AN-EQUIP-MIB", "zxAnEnvDeviceId"),
)
if mibBuilder.loadTexts:
    zxAnEnvDeviceEntry.setStatus("current")


class _ZxAnEnvDeviceId_Type(Integer32):
    """Custom type zxAnEnvDeviceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ZxAnEnvDeviceId_Type.__name__ = "Integer32"
_ZxAnEnvDeviceId_Object = MibTableColumn
zxAnEnvDeviceId = _ZxAnEnvDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 16, 2, 1, 1),
    _ZxAnEnvDeviceId_Type()
)
zxAnEnvDeviceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEnvDeviceId.setStatus("current")


class _ZxAnEnvDeviceName_Type(DisplayString):
    """Custom type zxAnEnvDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnEnvDeviceName_Type.__name__ = "DisplayString"
_ZxAnEnvDeviceName_Object = MibTableColumn
zxAnEnvDeviceName = _ZxAnEnvDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 16, 2, 1, 2),
    _ZxAnEnvDeviceName_Type()
)
zxAnEnvDeviceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEnvDeviceName.setStatus("current")
_ZxAnEnvDeviceRowStatus_Type = RowStatus
_ZxAnEnvDeviceRowStatus_Object = MibTableColumn
zxAnEnvDeviceRowStatus = _ZxAnEnvDeviceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 16, 2, 1, 50),
    _ZxAnEnvDeviceRowStatus_Type()
)
zxAnEnvDeviceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEnvDeviceRowStatus.setStatus("current")
_ZxAnEnvDevMonSwitchTable_Object = MibTable
zxAnEnvDevMonSwitchTable = _ZxAnEnvDevMonSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 16, 3)
)
if mibBuilder.loadTexts:
    zxAnEnvDevMonSwitchTable.setStatus("current")
_ZxAnEnvDevMonSwitchEntry_Object = MibTableRow
zxAnEnvDevMonSwitchEntry = _ZxAnEnvDevMonSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 16, 3, 1)
)
zxAnEnvDevMonSwitchEntry.setIndexNames(
    (0, "ZTE-AN-EQUIP-MIB", "zxAnEnvDevMonSwitchId"),
)
if mibBuilder.loadTexts:
    zxAnEnvDevMonSwitchEntry.setStatus("current")


class _ZxAnEnvDevMonSwitchId_Type(Integer32):
    """Custom type zxAnEnvDevMonSwitchId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ZxAnEnvDevMonSwitchId_Type.__name__ = "Integer32"
_ZxAnEnvDevMonSwitchId_Object = MibTableColumn
zxAnEnvDevMonSwitchId = _ZxAnEnvDevMonSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 16, 3, 1, 1),
    _ZxAnEnvDevMonSwitchId_Type()
)
zxAnEnvDevMonSwitchId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEnvDevMonSwitchId.setStatus("current")


class _ZxAnEnvDevMonSwitchDeviceId_Type(Integer32):
    """Custom type zxAnEnvDevMonSwitchDeviceId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnEnvDevMonSwitchDeviceId_Type.__name__ = "Integer32"
_ZxAnEnvDevMonSwitchDeviceId_Object = MibTableColumn
zxAnEnvDevMonSwitchDeviceId = _ZxAnEnvDevMonSwitchDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 16, 3, 1, 2),
    _ZxAnEnvDevMonSwitchDeviceId_Type()
)
zxAnEnvDevMonSwitchDeviceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvDevMonSwitchDeviceId.setStatus("current")


class _ZxAnEnvDevMonSwitchTrapEnable_Type(Integer32):
    """Custom type zxAnEnvDevMonSwitchTrapEnable based on Integer32"""
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


_ZxAnEnvDevMonSwitchTrapEnable_Type.__name__ = "Integer32"
_ZxAnEnvDevMonSwitchTrapEnable_Object = MibTableColumn
zxAnEnvDevMonSwitchTrapEnable = _ZxAnEnvDevMonSwitchTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 16, 3, 1, 3),
    _ZxAnEnvDevMonSwitchTrapEnable_Type()
)
zxAnEnvDevMonSwitchTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvDevMonSwitchTrapEnable.setStatus("current")


class _ZxAnEnvDevMonSwitchNormalStatus_Type(Integer32):
    """Custom type zxAnEnvDevMonSwitchNormalStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lowLevel", 1),
          ("highLevel", 2))
    )


_ZxAnEnvDevMonSwitchNormalStatus_Type.__name__ = "Integer32"
_ZxAnEnvDevMonSwitchNormalStatus_Object = MibTableColumn
zxAnEnvDevMonSwitchNormalStatus = _ZxAnEnvDevMonSwitchNormalStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 16, 3, 1, 4),
    _ZxAnEnvDevMonSwitchNormalStatus_Type()
)
zxAnEnvDevMonSwitchNormalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvDevMonSwitchNormalStatus.setStatus("current")


class _ZxAnEnvDevMonSwitchCurrStatus_Type(Integer32):
    """Custom type zxAnEnvDevMonSwitchCurrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("lowLevel", 1),
          ("highLevel", 2),
          ("unknown", 255))
    )


_ZxAnEnvDevMonSwitchCurrStatus_Type.__name__ = "Integer32"
_ZxAnEnvDevMonSwitchCurrStatus_Object = MibTableColumn
zxAnEnvDevMonSwitchCurrStatus = _ZxAnEnvDevMonSwitchCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 3, 16, 3, 1, 5),
    _ZxAnEnvDevMonSwitchCurrStatus_Type()
)
zxAnEnvDevMonSwitchCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEnvDevMonSwitchCurrStatus.setStatus("current")
_ZxAnPatchMgmt_ObjectIdentity = ObjectIdentity
zxAnPatchMgmt = _ZxAnPatchMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 4)
)
_ZxAnPatchTable_Object = MibTable
zxAnPatchTable = _ZxAnPatchTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    zxAnPatchTable.setStatus("current")
_ZxAnPatchEntry_Object = MibTableRow
zxAnPatchEntry = _ZxAnPatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 4, 1, 1)
)
zxAnPatchEntry.setIndexNames(
    (0, "ZTE-AN-EQUIP-MIB", "zxAnPatchName"),
)
if mibBuilder.loadTexts:
    zxAnPatchEntry.setStatus("current")


class _ZxAnPatchName_Type(OctetString):
    """Custom type zxAnPatchName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnPatchName_Type.__name__ = "OctetString"
_ZxAnPatchName_Object = MibTableColumn
zxAnPatchName = _ZxAnPatchName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 4, 1, 1, 1),
    _ZxAnPatchName_Type()
)
zxAnPatchName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnPatchName.setStatus("current")


class _ZxAnPatchSystemVersion_Type(OctetString):
    """Custom type zxAnPatchSystemVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnPatchSystemVersion_Type.__name__ = "OctetString"
_ZxAnPatchSystemVersion_Object = MibTableColumn
zxAnPatchSystemVersion = _ZxAnPatchSystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 4, 1, 1, 2),
    _ZxAnPatchSystemVersion_Type()
)
zxAnPatchSystemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPatchSystemVersion.setStatus("current")


class _ZxAnPatchVersionNo_Type(OctetString):
    """Custom type zxAnPatchVersionNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnPatchVersionNo_Type.__name__ = "OctetString"
_ZxAnPatchVersionNo_Object = MibTableColumn
zxAnPatchVersionNo = _ZxAnPatchVersionNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 4, 1, 1, 3),
    _ZxAnPatchVersionNo_Type()
)
zxAnPatchVersionNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPatchVersionNo.setStatus("current")
_ZxAnPatchSize_Type = Unsigned32
_ZxAnPatchSize_Object = MibTableColumn
zxAnPatchSize = _ZxAnPatchSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 4, 1, 1, 4),
    _ZxAnPatchSize_Type()
)
zxAnPatchSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPatchSize.setStatus("current")


class _ZxAnPatchStatus_Type(OctetString):
    """Custom type zxAnPatchStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnPatchStatus_Type.__name__ = "OctetString"
_ZxAnPatchStatus_Object = MibTableColumn
zxAnPatchStatus = _ZxAnPatchStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 4, 1, 1, 5),
    _ZxAnPatchStatus_Type()
)
zxAnPatchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPatchStatus.setStatus("current")


class _ZxAnPatchCreateTime_Type(OctetString):
    """Custom type zxAnPatchCreateTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ZxAnPatchCreateTime_Type.__name__ = "OctetString"
_ZxAnPatchCreateTime_Object = MibTableColumn
zxAnPatchCreateTime = _ZxAnPatchCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 4, 1, 1, 6),
    _ZxAnPatchCreateTime_Type()
)
zxAnPatchCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPatchCreateTime.setStatus("current")


class _ZxAnPatchActiveTime_Type(OctetString):
    """Custom type zxAnPatchActiveTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ZxAnPatchActiveTime_Type.__name__ = "OctetString"
_ZxAnPatchActiveTime_Object = MibTableColumn
zxAnPatchActiveTime = _ZxAnPatchActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 4, 1, 1, 7),
    _ZxAnPatchActiveTime_Type()
)
zxAnPatchActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPatchActiveTime.setStatus("current")


class _ZxAnPatchRunningTime_Type(OctetString):
    """Custom type zxAnPatchRunningTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ZxAnPatchRunningTime_Type.__name__ = "OctetString"
_ZxAnPatchRunningTime_Object = MibTableColumn
zxAnPatchRunningTime = _ZxAnPatchRunningTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 4, 1, 1, 8),
    _ZxAnPatchRunningTime_Type()
)
zxAnPatchRunningTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPatchRunningTime.setStatus("current")


class _ZxAnPatchDesc_Type(OctetString):
    """Custom type zxAnPatchDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnPatchDesc_Type.__name__ = "OctetString"
_ZxAnPatchDesc_Object = MibTableColumn
zxAnPatchDesc = _ZxAnPatchDesc_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 4, 1, 1, 9),
    _ZxAnPatchDesc_Type()
)
zxAnPatchDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPatchDesc.setStatus("current")


class _ZxAnPatchAdminStatus_Type(Integer32):
    """Custom type zxAnPatchAdminStatus based on Integer32"""
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
        *(("active", 1),
          ("save", 2),
          ("deactive", 3),
          ("delete", 4))
    )


_ZxAnPatchAdminStatus_Type.__name__ = "Integer32"
_ZxAnPatchAdminStatus_Object = MibTableColumn
zxAnPatchAdminStatus = _ZxAnPatchAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 4, 1, 1, 10),
    _ZxAnPatchAdminStatus_Type()
)
zxAnPatchAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPatchAdminStatus.setStatus("current")
_ZxAnEquipStat_ObjectIdentity = ObjectIdentity
zxAnEquipStat = _ZxAnEquipStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 5)
)
_ZxAnCardStatTable_Object = MibTable
zxAnCardStatTable = _ZxAnCardStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    zxAnCardStatTable.setStatus("current")
_ZxAnCardStatEntry_Object = MibTableRow
zxAnCardStatEntry = _ZxAnCardStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 5, 1, 1)
)
zxAnCardStatEntry.setIndexNames(
    (0, "ZTE-AN-EQUIP-MIB", "zxAnRackNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnShelfNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnSlotNo"),
)
if mibBuilder.loadTexts:
    zxAnCardStatEntry.setStatus("current")
_ZxAnCardInOctets_Type = Counter64
_ZxAnCardInOctets_Object = MibTableColumn
zxAnCardInOctets = _ZxAnCardInOctets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 5, 1, 1, 1),
    _ZxAnCardInOctets_Type()
)
zxAnCardInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardInOctets.setStatus("current")
_ZxAnCardInUcastPkts_Type = Counter64
_ZxAnCardInUcastPkts_Object = MibTableColumn
zxAnCardInUcastPkts = _ZxAnCardInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 5, 1, 1, 2),
    _ZxAnCardInUcastPkts_Type()
)
zxAnCardInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardInUcastPkts.setStatus("current")
_ZxAnCardInMulticastPkts_Type = Counter64
_ZxAnCardInMulticastPkts_Object = MibTableColumn
zxAnCardInMulticastPkts = _ZxAnCardInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 5, 1, 1, 3),
    _ZxAnCardInMulticastPkts_Type()
)
zxAnCardInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardInMulticastPkts.setStatus("current")
_ZxAnCardInBroadcastPkts_Type = Counter64
_ZxAnCardInBroadcastPkts_Object = MibTableColumn
zxAnCardInBroadcastPkts = _ZxAnCardInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 5, 1, 1, 4),
    _ZxAnCardInBroadcastPkts_Type()
)
zxAnCardInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardInBroadcastPkts.setStatus("current")
_ZxAnCardOutOctets_Type = Counter64
_ZxAnCardOutOctets_Object = MibTableColumn
zxAnCardOutOctets = _ZxAnCardOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 5, 1, 1, 5),
    _ZxAnCardOutOctets_Type()
)
zxAnCardOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardOutOctets.setStatus("current")
_ZxAnCardOutUcastPkts_Type = Counter64
_ZxAnCardOutUcastPkts_Object = MibTableColumn
zxAnCardOutUcastPkts = _ZxAnCardOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 5, 1, 1, 6),
    _ZxAnCardOutUcastPkts_Type()
)
zxAnCardOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardOutUcastPkts.setStatus("current")
_ZxAnCardOutMulticastPkts_Type = Counter64
_ZxAnCardOutMulticastPkts_Object = MibTableColumn
zxAnCardOutMulticastPkts = _ZxAnCardOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 5, 1, 1, 7),
    _ZxAnCardOutMulticastPkts_Type()
)
zxAnCardOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardOutMulticastPkts.setStatus("current")
_ZxAnCardOutBroadcastPkts_Type = Counter64
_ZxAnCardOutBroadcastPkts_Object = MibTableColumn
zxAnCardOutBroadcastPkts = _ZxAnCardOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 5, 1, 1, 8),
    _ZxAnCardOutBroadcastPkts_Type()
)
zxAnCardOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardOutBroadcastPkts.setStatus("current")
_ZxAnCardInErrors_Type = Counter64
_ZxAnCardInErrors_Object = MibTableColumn
zxAnCardInErrors = _ZxAnCardInErrors_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 5, 1, 1, 9),
    _ZxAnCardInErrors_Type()
)
zxAnCardInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardInErrors.setStatus("current")
_ZxAnCardOutErrors_Type = Counter64
_ZxAnCardOutErrors_Object = MibTableColumn
zxAnCardOutErrors = _ZxAnCardOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 5, 1, 1, 10),
    _ZxAnCardOutErrors_Type()
)
zxAnCardOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardOutErrors.setStatus("current")
_ZxAnCardInDiscardPkts_Type = Counter64
_ZxAnCardInDiscardPkts_Object = MibTableColumn
zxAnCardInDiscardPkts = _ZxAnCardInDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 5, 1, 1, 11),
    _ZxAnCardInDiscardPkts_Type()
)
zxAnCardInDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardInDiscardPkts.setStatus("current")
_ZxAnCardOutDiscardPkts_Type = Counter64
_ZxAnCardOutDiscardPkts_Object = MibTableColumn
zxAnCardOutDiscardPkts = _ZxAnCardOutDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 5, 1, 1, 12),
    _ZxAnCardOutDiscardPkts_Type()
)
zxAnCardOutDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardOutDiscardPkts.setStatus("current")
_ZxAnCardInDiscardPktRatio_Type = Integer32
_ZxAnCardInDiscardPktRatio_Object = MibTableColumn
zxAnCardInDiscardPktRatio = _ZxAnCardInDiscardPktRatio_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 5, 1, 1, 13),
    _ZxAnCardInDiscardPktRatio_Type()
)
zxAnCardInDiscardPktRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardInDiscardPktRatio.setStatus("current")
if mibBuilder.loadTexts:
    zxAnCardInDiscardPktRatio.setUnits("percent")
_ZxAnCardOutDiscardPktRatio_Type = Integer32
_ZxAnCardOutDiscardPktRatio_Object = MibTableColumn
zxAnCardOutDiscardPktRatio = _ZxAnCardOutDiscardPktRatio_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 5, 1, 1, 14),
    _ZxAnCardOutDiscardPktRatio_Type()
)
zxAnCardOutDiscardPktRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardOutDiscardPktRatio.setStatus("current")
if mibBuilder.loadTexts:
    zxAnCardOutDiscardPktRatio.setUnits("percent")
_ZxAnCardDot3InPauseFrames_Type = Counter64
_ZxAnCardDot3InPauseFrames_Object = MibTableColumn
zxAnCardDot3InPauseFrames = _ZxAnCardDot3InPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 5, 1, 1, 15),
    _ZxAnCardDot3InPauseFrames_Type()
)
zxAnCardDot3InPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardDot3InPauseFrames.setStatus("current")
_ZxAnCardDot3OutPauseFrames_Type = Counter64
_ZxAnCardDot3OutPauseFrames_Object = MibTableColumn
zxAnCardDot3OutPauseFrames = _ZxAnCardDot3OutPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 5, 1, 1, 16),
    _ZxAnCardDot3OutPauseFrames_Type()
)
zxAnCardDot3OutPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardDot3OutPauseFrames.setStatus("current")
_ZxAnEquipSysMgmt_ObjectIdentity = ObjectIdentity
zxAnEquipSysMgmt = _ZxAnEquipSysMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 6)
)


class _ZxAnEquipSysLastSwapRequest_Type(Integer32):
    """Custom type zxAnEquipSysLastSwapRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("forced", 1),
          ("cardOffline", 2),
          ("reset", 3),
          ("cardDown", 99))
    )


_ZxAnEquipSysLastSwapRequest_Type.__name__ = "Integer32"
_ZxAnEquipSysLastSwapRequest_Object = MibScalar
zxAnEquipSysLastSwapRequest = _ZxAnEquipSysLastSwapRequest_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 6, 1),
    _ZxAnEquipSysLastSwapRequest_Type()
)
zxAnEquipSysLastSwapRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEquipSysLastSwapRequest.setStatus("current")


class _ZxAnEquipSysAutoSwapEnable_Type(Integer32):
    """Custom type zxAnEquipSysAutoSwapEnable based on Integer32"""
    defaultValue = 2

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


_ZxAnEquipSysAutoSwapEnable_Type.__name__ = "Integer32"
_ZxAnEquipSysAutoSwapEnable_Object = MibScalar
zxAnEquipSysAutoSwapEnable = _ZxAnEquipSysAutoSwapEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 6, 10),
    _ZxAnEquipSysAutoSwapEnable_Type()
)
zxAnEquipSysAutoSwapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEquipSysAutoSwapEnable.setStatus("current")


class _ZxAnEquipSysAutoSwapStartTime_Type(DisplayString):
    """Custom type zxAnEquipSysAutoSwapStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_ZxAnEquipSysAutoSwapStartTime_Type.__name__ = "DisplayString"
_ZxAnEquipSysAutoSwapStartTime_Object = MibScalar
zxAnEquipSysAutoSwapStartTime = _ZxAnEquipSysAutoSwapStartTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 6, 11),
    _ZxAnEquipSysAutoSwapStartTime_Type()
)
zxAnEquipSysAutoSwapStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEquipSysAutoSwapStartTime.setStatus("current")


class _ZxAnEquipSysAutoSwapInterval_Type(Integer32):
    """Custom type zxAnEquipSysAutoSwapInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 240),
    )


_ZxAnEquipSysAutoSwapInterval_Type.__name__ = "Integer32"
_ZxAnEquipSysAutoSwapInterval_Object = MibScalar
zxAnEquipSysAutoSwapInterval = _ZxAnEquipSysAutoSwapInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 6, 12),
    _ZxAnEquipSysAutoSwapInterval_Type()
)
zxAnEquipSysAutoSwapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEquipSysAutoSwapInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEquipSysAutoSwapInterval.setUnits("days")


class _ZxAnEquipSysAutoSwapRemainDays_Type(Integer32):
    """Custom type zxAnEquipSysAutoSwapRemainDays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 240),
    )


_ZxAnEquipSysAutoSwapRemainDays_Type.__name__ = "Integer32"
_ZxAnEquipSysAutoSwapRemainDays_Object = MibScalar
zxAnEquipSysAutoSwapRemainDays = _ZxAnEquipSysAutoSwapRemainDays_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 6, 13),
    _ZxAnEquipSysAutoSwapRemainDays_Type()
)
zxAnEquipSysAutoSwapRemainDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEquipSysAutoSwapRemainDays.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEquipSysAutoSwapRemainDays.setUnits("days")


class _ZxAnEquipShelfAutoSwapInterval_Type(Integer32):
    """Custom type zxAnEquipShelfAutoSwapInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 1440),
    )


_ZxAnEquipShelfAutoSwapInterval_Type.__name__ = "Integer32"
_ZxAnEquipShelfAutoSwapInterval_Object = MibScalar
zxAnEquipShelfAutoSwapInterval = _ZxAnEquipShelfAutoSwapInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 6, 14),
    _ZxAnEquipShelfAutoSwapInterval_Type()
)
zxAnEquipShelfAutoSwapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEquipShelfAutoSwapInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEquipShelfAutoSwapInterval.setUnits("minutes")
_ZxAnEnvExMonitor_ObjectIdentity = ObjectIdentity
zxAnEnvExMonitor = _ZxAnEnvExMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7)
)
_ZxAnEnvExMgmt_ObjectIdentity = ObjectIdentity
zxAnEnvExMgmt = _ZxAnEnvExMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 1)
)
_ZxAnEnvExMgmtTable_Object = MibTable
zxAnEnvExMgmtTable = _ZxAnEnvExMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 1, 1)
)
if mibBuilder.loadTexts:
    zxAnEnvExMgmtTable.setStatus("current")
_ZxAnEnvExMgmtEntry_Object = MibTableRow
zxAnEnvExMgmtEntry = _ZxAnEnvExMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 1, 1, 1)
)
zxAnEnvExMgmtEntry.setIndexNames(
    (0, "ZTE-AN-EQUIP-MIB", "zxAnRackNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnShelfNo"),
)
if mibBuilder.loadTexts:
    zxAnEnvExMgmtEntry.setStatus("current")
_ZxAnEnvExTemperature_Type = Integer32
_ZxAnEnvExTemperature_Object = MibTableColumn
zxAnEnvExTemperature = _ZxAnEnvExTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 1, 1, 1, 1),
    _ZxAnEnvExTemperature_Type()
)
zxAnEnvExTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEnvExTemperature.setStatus("current")
_ZxAnEnvExTempAlarmThreshold_Type = Integer32
_ZxAnEnvExTempAlarmThreshold_Object = MibTableColumn
zxAnEnvExTempAlarmThreshold = _ZxAnEnvExTempAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 1, 1, 1, 2),
    _ZxAnEnvExTempAlarmThreshold_Type()
)
zxAnEnvExTempAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvExTempAlarmThreshold.setStatus("current")


class _ZxAnEnvExMonitorIfUsage_Type(Integer32):
    """Custom type zxAnEnvExMonitorIfUsage based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("epm", 1),
          ("fanTray", 2),
          ("noUse", 3),
          ("noSupport", 4),
          ("etmWithTestSubcard", 5),
          ("etmWithoutTestSubcard", 6))
    )


_ZxAnEnvExMonitorIfUsage_Type.__name__ = "Integer32"
_ZxAnEnvExMonitorIfUsage_Object = MibTableColumn
zxAnEnvExMonitorIfUsage = _ZxAnEnvExMonitorIfUsage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 1, 1, 1, 3),
    _ZxAnEnvExMonitorIfUsage_Type()
)
zxAnEnvExMonitorIfUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvExMonitorIfUsage.setStatus("current")
_ZxAnEnvExTempCtrlMgmt_ObjectIdentity = ObjectIdentity
zxAnEnvExTempCtrlMgmt = _ZxAnEnvExTempCtrlMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 1, 2)
)
_ZxAnEnvExTempCtrlTable_Object = MibTable
zxAnEnvExTempCtrlTable = _ZxAnEnvExTempCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 1, 2, 2)
)
if mibBuilder.loadTexts:
    zxAnEnvExTempCtrlTable.setStatus("current")
_ZxAnEnvExTempCtrlEntry_Object = MibTableRow
zxAnEnvExTempCtrlEntry = _ZxAnEnvExTempCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 1, 2, 2, 1)
)
zxAnEnvExTempCtrlEntry.setIndexNames(
    (0, "ZTE-AN-EQUIP-MIB", "zxAnRackNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnShelfNo"),
)
if mibBuilder.loadTexts:
    zxAnEnvExTempCtrlEntry.setStatus("current")


class _ZxAnEnvExTempCtrlEnable_Type(Integer32):
    """Custom type zxAnEnvExTempCtrlEnable based on Integer32"""
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


_ZxAnEnvExTempCtrlEnable_Type.__name__ = "Integer32"
_ZxAnEnvExTempCtrlEnable_Object = MibTableColumn
zxAnEnvExTempCtrlEnable = _ZxAnEnvExTempCtrlEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 1, 2, 2, 1, 1),
    _ZxAnEnvExTempCtrlEnable_Type()
)
zxAnEnvExTempCtrlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvExTempCtrlEnable.setStatus("current")


class _ZxAnEnvExTempCtrlLowThresh_Type(Integer32):
    """Custom type zxAnEnvExTempCtrlLowThresh based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 98),
    )


_ZxAnEnvExTempCtrlLowThresh_Type.__name__ = "Integer32"
_ZxAnEnvExTempCtrlLowThresh_Object = MibTableColumn
zxAnEnvExTempCtrlLowThresh = _ZxAnEnvExTempCtrlLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 1, 2, 2, 1, 2),
    _ZxAnEnvExTempCtrlLowThresh_Type()
)
zxAnEnvExTempCtrlLowThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvExTempCtrlLowThresh.setStatus("current")


class _ZxAnEnvExTempCtrlMediumThresh_Type(Integer32):
    """Custom type zxAnEnvExTempCtrlMediumThresh based on Integer32"""
    defaultValue = 45

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_ZxAnEnvExTempCtrlMediumThresh_Type.__name__ = "Integer32"
_ZxAnEnvExTempCtrlMediumThresh_Object = MibTableColumn
zxAnEnvExTempCtrlMediumThresh = _ZxAnEnvExTempCtrlMediumThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 1, 2, 2, 1, 3),
    _ZxAnEnvExTempCtrlMediumThresh_Type()
)
zxAnEnvExTempCtrlMediumThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvExTempCtrlMediumThresh.setStatus("current")


class _ZxAnEnvExTempCtrlHighThresh_Type(Integer32):
    """Custom type zxAnEnvExTempCtrlHighThresh based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 100),
    )


_ZxAnEnvExTempCtrlHighThresh_Type.__name__ = "Integer32"
_ZxAnEnvExTempCtrlHighThresh_Object = MibTableColumn
zxAnEnvExTempCtrlHighThresh = _ZxAnEnvExTempCtrlHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 1, 2, 2, 1, 4),
    _ZxAnEnvExTempCtrlHighThresh_Type()
)
zxAnEnvExTempCtrlHighThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvExTempCtrlHighThresh.setStatus("current")
_ZxAnFanTrayExMgmt_ObjectIdentity = ObjectIdentity
zxAnFanTrayExMgmt = _ZxAnFanTrayExMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 2)
)
_ZxAnFanTrayExMgmtTable_Object = MibTable
zxAnFanTrayExMgmtTable = _ZxAnFanTrayExMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 2, 1)
)
if mibBuilder.loadTexts:
    zxAnFanTrayExMgmtTable.setStatus("current")
_ZxAnFanTrayExMgmtEntry_Object = MibTableRow
zxAnFanTrayExMgmtEntry = _ZxAnFanTrayExMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 2, 1, 1)
)
zxAnFanTrayExMgmtEntry.setIndexNames(
    (0, "ZTE-AN-EQUIP-MIB", "zxAnRackNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnShelfNo"),
)
if mibBuilder.loadTexts:
    zxAnFanTrayExMgmtEntry.setStatus("current")


class _ZxAnFanExAlarmBeepEnable_Type(Integer32):
    """Custom type zxAnFanExAlarmBeepEnable based on Integer32"""
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


_ZxAnFanExAlarmBeepEnable_Type.__name__ = "Integer32"
_ZxAnFanExAlarmBeepEnable_Object = MibTableColumn
zxAnFanExAlarmBeepEnable = _ZxAnFanExAlarmBeepEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 2, 1, 1, 1),
    _ZxAnFanExAlarmBeepEnable_Type()
)
zxAnFanExAlarmBeepEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFanExAlarmBeepEnable.setStatus("current")


class _ZxAnFanExAutoSwitchByCardInstall_Type(Integer32):
    """Custom type zxAnFanExAutoSwitchByCardInstall based on Integer32"""
    defaultValue = 2

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


_ZxAnFanExAutoSwitchByCardInstall_Type.__name__ = "Integer32"
_ZxAnFanExAutoSwitchByCardInstall_Object = MibTableColumn
zxAnFanExAutoSwitchByCardInstall = _ZxAnFanExAutoSwitchByCardInstall_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 2, 1, 1, 2),
    _ZxAnFanExAutoSwitchByCardInstall_Type()
)
zxAnFanExAutoSwitchByCardInstall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFanExAutoSwitchByCardInstall.setStatus("current")
_ZxAnFanExHardwareVersion_Type = DisplayString
_ZxAnFanExHardwareVersion_Object = MibTableColumn
zxAnFanExHardwareVersion = _ZxAnFanExHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 2, 1, 1, 3),
    _ZxAnFanExHardwareVersion_Type()
)
zxAnFanExHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnFanExHardwareVersion.setStatus("current")
_ZxAnFanExSoftwareVersion_Type = DisplayString
_ZxAnFanExSoftwareVersion_Object = MibTableColumn
zxAnFanExSoftwareVersion = _ZxAnFanExSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 2, 1, 1, 4),
    _ZxAnFanExSoftwareVersion_Type()
)
zxAnFanExSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnFanExSoftwareVersion.setStatus("current")


class _ZxAnFanExSpeedCtrlMode_Type(Integer32):
    """Custom type zxAnFanExSpeedCtrlMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("temperatureBasedAutoCtrl", 1),
          ("fixSpeed", 2))
    )


_ZxAnFanExSpeedCtrlMode_Type.__name__ = "Integer32"
_ZxAnFanExSpeedCtrlMode_Object = MibTableColumn
zxAnFanExSpeedCtrlMode = _ZxAnFanExSpeedCtrlMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 2, 1, 1, 5),
    _ZxAnFanExSpeedCtrlMode_Type()
)
zxAnFanExSpeedCtrlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFanExSpeedCtrlMode.setStatus("current")
_ZxAnFanExLowSpeed_Type = Integer32
_ZxAnFanExLowSpeed_Object = MibTableColumn
zxAnFanExLowSpeed = _ZxAnFanExLowSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 2, 1, 1, 6),
    _ZxAnFanExLowSpeed_Type()
)
zxAnFanExLowSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFanExLowSpeed.setStatus("current")
if mibBuilder.loadTexts:
    zxAnFanExLowSpeed.setUnits("RPM")
_ZxAnFanExStandardSpeed_Type = Integer32
_ZxAnFanExStandardSpeed_Object = MibTableColumn
zxAnFanExStandardSpeed = _ZxAnFanExStandardSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 2, 1, 1, 7),
    _ZxAnFanExStandardSpeed_Type()
)
zxAnFanExStandardSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFanExStandardSpeed.setStatus("current")
if mibBuilder.loadTexts:
    zxAnFanExStandardSpeed.setUnits("RPM")
_ZxAnFanExHighSpeed_Type = Integer32
_ZxAnFanExHighSpeed_Object = MibTableColumn
zxAnFanExHighSpeed = _ZxAnFanExHighSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 2, 1, 1, 8),
    _ZxAnFanExHighSpeed_Type()
)
zxAnFanExHighSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFanExHighSpeed.setStatus("current")
if mibBuilder.loadTexts:
    zxAnFanExHighSpeed.setUnits("RPM")
_ZxAnFanExSuperSpeed_Type = Integer32
_ZxAnFanExSuperSpeed_Object = MibTableColumn
zxAnFanExSuperSpeed = _ZxAnFanExSuperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 2, 1, 1, 9),
    _ZxAnFanExSuperSpeed_Type()
)
zxAnFanExSuperSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFanExSuperSpeed.setStatus("current")
if mibBuilder.loadTexts:
    zxAnFanExSuperSpeed.setUnits("RPM")
_ZxAnFanExLowSpeedShiftTemp_Type = Integer32
_ZxAnFanExLowSpeedShiftTemp_Object = MibTableColumn
zxAnFanExLowSpeedShiftTemp = _ZxAnFanExLowSpeedShiftTemp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 2, 1, 1, 10),
    _ZxAnFanExLowSpeedShiftTemp_Type()
)
zxAnFanExLowSpeedShiftTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFanExLowSpeedShiftTemp.setStatus("current")
if mibBuilder.loadTexts:
    zxAnFanExLowSpeedShiftTemp.setUnits("centigrade")
_ZxAnFanExStandardSpeedShiftTemp_Type = Integer32
_ZxAnFanExStandardSpeedShiftTemp_Object = MibTableColumn
zxAnFanExStandardSpeedShiftTemp = _ZxAnFanExStandardSpeedShiftTemp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 2, 1, 1, 11),
    _ZxAnFanExStandardSpeedShiftTemp_Type()
)
zxAnFanExStandardSpeedShiftTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFanExStandardSpeedShiftTemp.setStatus("current")
if mibBuilder.loadTexts:
    zxAnFanExStandardSpeedShiftTemp.setUnits("centigrade")
_ZxAnFanExHighSpeedShiftTemp_Type = Integer32
_ZxAnFanExHighSpeedShiftTemp_Object = MibTableColumn
zxAnFanExHighSpeedShiftTemp = _ZxAnFanExHighSpeedShiftTemp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 2, 1, 1, 12),
    _ZxAnFanExHighSpeedShiftTemp_Type()
)
zxAnFanExHighSpeedShiftTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFanExHighSpeedShiftTemp.setStatus("current")
if mibBuilder.loadTexts:
    zxAnFanExHighSpeedShiftTemp.setUnits("centigrade")
_ZxAnFanExSuperSpeedShiftTemp_Type = Integer32
_ZxAnFanExSuperSpeedShiftTemp_Object = MibTableColumn
zxAnFanExSuperSpeedShiftTemp = _ZxAnFanExSuperSpeedShiftTemp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 2, 1, 1, 13),
    _ZxAnFanExSuperSpeedShiftTemp_Type()
)
zxAnFanExSuperSpeedShiftTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFanExSuperSpeedShiftTemp.setStatus("current")
if mibBuilder.loadTexts:
    zxAnFanExSuperSpeedShiftTemp.setUnits("centigrade")


class _ZxAnFanExLowSpeedPercentage_Type(Integer32):
    """Custom type zxAnFanExLowSpeedPercentage based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 97),
    )


_ZxAnFanExLowSpeedPercentage_Type.__name__ = "Integer32"
_ZxAnFanExLowSpeedPercentage_Object = MibTableColumn
zxAnFanExLowSpeedPercentage = _ZxAnFanExLowSpeedPercentage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 2, 1, 1, 14),
    _ZxAnFanExLowSpeedPercentage_Type()
)
zxAnFanExLowSpeedPercentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFanExLowSpeedPercentage.setStatus("current")
if mibBuilder.loadTexts:
    zxAnFanExLowSpeedPercentage.setUnits("percent")


class _ZxAnFanExStandardSpeedPercentage_Type(Integer32):
    """Custom type zxAnFanExStandardSpeedPercentage based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 98),
    )


_ZxAnFanExStandardSpeedPercentage_Type.__name__ = "Integer32"
_ZxAnFanExStandardSpeedPercentage_Object = MibTableColumn
zxAnFanExStandardSpeedPercentage = _ZxAnFanExStandardSpeedPercentage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 2, 1, 1, 15),
    _ZxAnFanExStandardSpeedPercentage_Type()
)
zxAnFanExStandardSpeedPercentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFanExStandardSpeedPercentage.setStatus("current")
if mibBuilder.loadTexts:
    zxAnFanExStandardSpeedPercentage.setUnits("percent")


class _ZxAnFanExHighSpeedPercentage_Type(Integer32):
    """Custom type zxAnFanExHighSpeedPercentage based on Integer32"""
    defaultValue = 70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 99),
    )


_ZxAnFanExHighSpeedPercentage_Type.__name__ = "Integer32"
_ZxAnFanExHighSpeedPercentage_Object = MibTableColumn
zxAnFanExHighSpeedPercentage = _ZxAnFanExHighSpeedPercentage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 2, 1, 1, 16),
    _ZxAnFanExHighSpeedPercentage_Type()
)
zxAnFanExHighSpeedPercentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFanExHighSpeedPercentage.setStatus("current")
if mibBuilder.loadTexts:
    zxAnFanExHighSpeedPercentage.setUnits("percent")


class _ZxAnFanExSuperSpeedPercentage_Type(Integer32):
    """Custom type zxAnFanExSuperSpeedPercentage based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 100),
    )


_ZxAnFanExSuperSpeedPercentage_Type.__name__ = "Integer32"
_ZxAnFanExSuperSpeedPercentage_Object = MibTableColumn
zxAnFanExSuperSpeedPercentage = _ZxAnFanExSuperSpeedPercentage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 2, 1, 1, 17),
    _ZxAnFanExSuperSpeedPercentage_Type()
)
zxAnFanExSuperSpeedPercentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFanExSuperSpeedPercentage.setStatus("current")
if mibBuilder.loadTexts:
    zxAnFanExSuperSpeedPercentage.setUnits("percent")


class _ZxAnFanExInvSn_Type(DisplayString):
    """Custom type zxAnFanExInvSn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnFanExInvSn_Type.__name__ = "DisplayString"
_ZxAnFanExInvSn_Object = MibTableColumn
zxAnFanExInvSn = _ZxAnFanExInvSn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 2, 1, 1, 18),
    _ZxAnFanExInvSn_Type()
)
zxAnFanExInvSn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFanExInvSn.setStatus("current")
_ZxAnFanExMgmt_ObjectIdentity = ObjectIdentity
zxAnFanExMgmt = _ZxAnFanExMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 3)
)
_ZxAnFanExMgmtTable_Object = MibTable
zxAnFanExMgmtTable = _ZxAnFanExMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 3, 1)
)
if mibBuilder.loadTexts:
    zxAnFanExMgmtTable.setStatus("current")
_ZxAnFanExMgmtEntry_Object = MibTableRow
zxAnFanExMgmtEntry = _ZxAnFanExMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 3, 1, 1)
)
zxAnFanExMgmtEntry.setIndexNames(
    (0, "ZTE-AN-EQUIP-MIB", "zxAnRackNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnShelfNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnFanExIndex"),
)
if mibBuilder.loadTexts:
    zxAnFanExMgmtEntry.setStatus("current")
_ZxAnFanExIndex_Type = Integer32
_ZxAnFanExIndex_Object = MibTableColumn
zxAnFanExIndex = _ZxAnFanExIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 3, 1, 1, 1),
    _ZxAnFanExIndex_Type()
)
zxAnFanExIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnFanExIndex.setStatus("current")


class _ZxAnFanExConfSpeedLevel_Type(Integer32):
    """Custom type zxAnFanExConfSpeedLevel based on Integer32"""
    defaultValue = 2

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
        *(("lowSpeed", 1),
          ("standardSpeed", 2),
          ("highSpeed", 3),
          ("superSpeed", 4))
    )


_ZxAnFanExConfSpeedLevel_Type.__name__ = "Integer32"
_ZxAnFanExConfSpeedLevel_Object = MibTableColumn
zxAnFanExConfSpeedLevel = _ZxAnFanExConfSpeedLevel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 3, 1, 1, 2),
    _ZxAnFanExConfSpeedLevel_Type()
)
zxAnFanExConfSpeedLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnFanExConfSpeedLevel.setStatus("current")


class _ZxAnFanExActualSpeedLevel_Type(Integer32):
    """Custom type zxAnFanExActualSpeedLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("lowSpeed", 1),
          ("standardSpeed", 2),
          ("highSpeed", 3),
          ("superSpeed", 4),
          ("other", 10))
    )


_ZxAnFanExActualSpeedLevel_Type.__name__ = "Integer32"
_ZxAnFanExActualSpeedLevel_Object = MibTableColumn
zxAnFanExActualSpeedLevel = _ZxAnFanExActualSpeedLevel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 3, 1, 1, 3),
    _ZxAnFanExActualSpeedLevel_Type()
)
zxAnFanExActualSpeedLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnFanExActualSpeedLevel.setStatus("current")


class _ZxAnFanExAdminStatus_Type(Integer32):
    """Custom type zxAnFanExAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_ZxAnFanExAdminStatus_Type.__name__ = "Integer32"
_ZxAnFanExAdminStatus_Object = MibTableColumn
zxAnFanExAdminStatus = _ZxAnFanExAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 3, 1, 1, 4),
    _ZxAnFanExAdminStatus_Type()
)
zxAnFanExAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnFanExAdminStatus.setStatus("current")


class _ZxAnFanExOperStatus_Type(Integer32):
    """Custom type zxAnFanExOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("unknown", 3))
    )


_ZxAnFanExOperStatus_Type.__name__ = "Integer32"
_ZxAnFanExOperStatus_Object = MibTableColumn
zxAnFanExOperStatus = _ZxAnFanExOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 3, 1, 1, 5),
    _ZxAnFanExOperStatus_Type()
)
zxAnFanExOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnFanExOperStatus.setStatus("current")


class _ZxAnFanExOnlineStatus_Type(Integer32):
    """Custom type zxAnFanExOnlineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("online", 1),
          ("offline", 2),
          ("unknown", 3))
    )


_ZxAnFanExOnlineStatus_Type.__name__ = "Integer32"
_ZxAnFanExOnlineStatus_Object = MibTableColumn
zxAnFanExOnlineStatus = _ZxAnFanExOnlineStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 3, 1, 1, 6),
    _ZxAnFanExOnlineStatus_Type()
)
zxAnFanExOnlineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnFanExOnlineStatus.setStatus("current")
_ZxAnFanExActualSpeed_Type = Integer32
_ZxAnFanExActualSpeed_Object = MibTableColumn
zxAnFanExActualSpeed = _ZxAnFanExActualSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 7, 3, 1, 1, 7),
    _ZxAnFanExActualSpeed_Type()
)
zxAnFanExActualSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnFanExActualSpeed.setStatus("current")
_ZxAnEquipMonitorObjects_ObjectIdentity = ObjectIdentity
zxAnEquipMonitorObjects = _ZxAnEquipMonitorObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 8)
)
_ZxAnCardWatchdogTable_Object = MibTable
zxAnCardWatchdogTable = _ZxAnCardWatchdogTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 8, 2)
)
if mibBuilder.loadTexts:
    zxAnCardWatchdogTable.setStatus("current")
_ZxAnCardWatchdogEntry_Object = MibTableRow
zxAnCardWatchdogEntry = _ZxAnCardWatchdogEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 8, 2, 1)
)
zxAnCardWatchdogEntry.setIndexNames(
    (0, "ZTE-AN-EQUIP-MIB", "zxAnRackNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnShelfNo"),
    (0, "ZTE-AN-EQUIP-MIB", "zxAnSlotNo"),
)
if mibBuilder.loadTexts:
    zxAnCardWatchdogEntry.setStatus("current")


class _ZxAnCardHardwareWatchdogEnable_Type(Integer32):
    """Custom type zxAnCardHardwareWatchdogEnable based on Integer32"""
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


_ZxAnCardHardwareWatchdogEnable_Type.__name__ = "Integer32"
_ZxAnCardHardwareWatchdogEnable_Object = MibTableColumn
zxAnCardHardwareWatchdogEnable = _ZxAnCardHardwareWatchdogEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 8, 2, 1, 1),
    _ZxAnCardHardwareWatchdogEnable_Type()
)
zxAnCardHardwareWatchdogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnCardHardwareWatchdogEnable.setStatus("current")


class _ZxAnCardTaskSuspendCardResetMode_Type(Integer32):
    """Custom type zxAnCardTaskSuspendCardResetMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notReset", 1),
          ("allTask", 2),
          ("criticalTask", 3))
    )


_ZxAnCardTaskSuspendCardResetMode_Type.__name__ = "Integer32"
_ZxAnCardTaskSuspendCardResetMode_Object = MibTableColumn
zxAnCardTaskSuspendCardResetMode = _ZxAnCardTaskSuspendCardResetMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 8, 2, 1, 2),
    _ZxAnCardTaskSuspendCardResetMode_Type()
)
zxAnCardTaskSuspendCardResetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnCardTaskSuspendCardResetMode.setStatus("current")


class _ZxAnCardSoftwareWatchdogEnable_Type(Integer32):
    """Custom type zxAnCardSoftwareWatchdogEnable based on Integer32"""
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


_ZxAnCardSoftwareWatchdogEnable_Type.__name__ = "Integer32"
_ZxAnCardSoftwareWatchdogEnable_Object = MibTableColumn
zxAnCardSoftwareWatchdogEnable = _ZxAnCardSoftwareWatchdogEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 8, 2, 1, 3),
    _ZxAnCardSoftwareWatchdogEnable_Type()
)
zxAnCardSoftwareWatchdogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnCardSoftwareWatchdogEnable.setStatus("current")


class _ZxAnCardTaskDurationThreshold_Type(Integer32):
    """Custom type zxAnCardTaskDurationThreshold based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_ZxAnCardTaskDurationThreshold_Type.__name__ = "Integer32"
_ZxAnCardTaskDurationThreshold_Object = MibTableColumn
zxAnCardTaskDurationThreshold = _ZxAnCardTaskDurationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 8, 2, 1, 4),
    _ZxAnCardTaskDurationThreshold_Type()
)
zxAnCardTaskDurationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnCardTaskDurationThreshold.setStatus("current")
if mibBuilder.loadTexts:
    zxAnCardTaskDurationThreshold.setUnits("minutes")


class _ZxAnCardTaskCpuUsageThreshold_Type(Integer32):
    """Custom type zxAnCardTaskCpuUsageThreshold based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ZxAnCardTaskCpuUsageThreshold_Type.__name__ = "Integer32"
_ZxAnCardTaskCpuUsageThreshold_Object = MibTableColumn
zxAnCardTaskCpuUsageThreshold = _ZxAnCardTaskCpuUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 1, 8, 2, 1, 5),
    _ZxAnCardTaskCpuUsageThreshold_Type()
)
zxAnCardTaskCpuUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnCardTaskCpuUsageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    zxAnCardTaskCpuUsageThreshold.setUnits("percent")
_ZxAnEquipTrapObjects_ObjectIdentity = ObjectIdentity
zxAnEquipTrapObjects = _ZxAnEquipTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2)
)
_ZxAnEquipSysTrapGroup_ObjectIdentity = ObjectIdentity
zxAnEquipSysTrapGroup = _ZxAnEquipSysTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 1)
)
_ZxAnEquipCardTrapGroup_ObjectIdentity = ObjectIdentity
zxAnEquipCardTrapGroup = _ZxAnEquipCardTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 2)
)
_ZxAnEquipEnvTrapGroup_ObjectIdentity = ObjectIdentity
zxAnEquipEnvTrapGroup = _ZxAnEquipEnvTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3)
)
_ZxAnEquipEnvExTrapGroup_ObjectIdentity = ObjectIdentity
zxAnEquipEnvExTrapGroup = _ZxAnEquipEnvExTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 4)
)
_ZxAnEquipGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnEquipGlobalObjects = _ZxAnEquipGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 3)
)


class _ZxAnEquipCapabilities_Type(Bits):
    """Custom type zxAnEquipCapabilities based on Bits"""
    namedValues = NamedValues(
        ("equipmentAlias", 0)
    )

_ZxAnEquipCapabilities_Type.__name__ = "Bits"
_ZxAnEquipCapabilities_Object = MibScalar
zxAnEquipCapabilities = _ZxAnEquipCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 3, 1),
    _ZxAnEquipCapabilities_Type()
)
zxAnEquipCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEquipCapabilities.setStatus("current")

# Managed Objects groups


# Notification objects

zxAnEquipCtrlCardSwapped = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 1, 2)
)
zxAnEquipCtrlCardSwapped.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnCardOperStatus"),
        ("ZTE-AN-EQUIP-MIB", "zxAnEquipSysLastSwapRequest"))
)
if mibBuilder.loadTexts:
    zxAnEquipCtrlCardSwapped.setStatus(
        "current"
    )

zxAnEquipBackupSynchFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 1, 3)
)
if mibBuilder.loadTexts:
    zxAnEquipBackupSynchFailed.setStatus(
        "current"
    )

zxAnEquipCtrlCardSwapCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 1, 6)
)
if mibBuilder.loadTexts:
    zxAnEquipCtrlCardSwapCleared.setStatus(
        "current"
    )

zxAnEquipCardUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 2, 1)
)
zxAnEquipCardUp.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnCardConfMainType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardActMainType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardActType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardAdminStatus"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardOperStatus"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardInvSn"))
)
if mibBuilder.loadTexts:
    zxAnEquipCardUp.setStatus(
        "current"
    )

zxAnEquipCardDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 2, 2)
)
zxAnEquipCardDown.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnCardConfMainType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardActMainType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardActType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardAdminStatus"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardOperStatus"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardInvSn"))
)
if mibBuilder.loadTexts:
    zxAnEquipCardDown.setStatus(
        "current"
    )

zxAnEquipCardDetectFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 2, 3)
)
zxAnEquipCardDetectFailed.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnCardActMainType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardActType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardStandbyStatus"))
)
if mibBuilder.loadTexts:
    zxAnEquipCardDetectFailed.setStatus(
        "current"
    )

zxAnEquipCardDetectSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 2, 4)
)
zxAnEquipCardDetectSuccess.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnCardActMainType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardActType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardStandbyStatus"))
)
if mibBuilder.loadTexts:
    zxAnEquipCardDetectSuccess.setStatus(
        "current"
    )

zxAnEquipCardCpuLoadAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 2, 6)
)
zxAnEquipCardCpuLoadAlarm.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnCardCpuLoad"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardCpuLoadThreshold"))
)
if mibBuilder.loadTexts:
    zxAnEquipCardCpuLoadAlarm.setStatus(
        "current"
    )

zxAnEquipCardCpuLoadAlarmCleard = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 2, 7)
)
zxAnEquipCardCpuLoadAlarmCleard.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnCardCpuLoad"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardCpuLoadThreshold"))
)
if mibBuilder.loadTexts:
    zxAnEquipCardCpuLoadAlarmCleard.setStatus(
        "current"
    )

zxAnEquipCardMemoryOverLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 2, 8)
)
zxAnEquipCardMemoryOverLoad.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnCardMemUsage"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardMemUsageThreshold"))
)
if mibBuilder.loadTexts:
    zxAnEquipCardMemoryOverLoad.setStatus(
        "current"
    )

zxAnEquipCardMemoryAlarmCleard = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 2, 9)
)
zxAnEquipCardMemoryAlarmCleard.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnCardMemUsage"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardMemUsageThreshold"))
)
if mibBuilder.loadTexts:
    zxAnEquipCardMemoryAlarmCleard.setStatus(
        "current"
    )

zxAnEquipCardUpdateVersionFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 2, 10)
)
zxAnEquipCardUpdateVersionFailed.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnSwManualUpdateStatus"),
        ("ZTE-AN-EQUIP-MIB", "zxAnSwManualFailedReason"))
)
if mibBuilder.loadTexts:
    zxAnEquipCardUpdateVersionFailed.setStatus(
        "current"
    )

zxAnEquipCardUpdateVerSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 2, 11)
)
zxAnEquipCardUpdateVerSuccess.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnSwManualUpdateStatus"),
        ("ZTE-AN-EQUIP-MIB", "zxAnSwManualFailedReason"))
)
if mibBuilder.loadTexts:
    zxAnEquipCardUpdateVerSuccess.setStatus(
        "current"
    )

zxAnEquipCardSvcCommFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 2, 12)
)
zxAnEquipCardSvcCommFailed.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnCardConfMainType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardActMainType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardActType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardOperStatus"))
)
if mibBuilder.loadTexts:
    zxAnEquipCardSvcCommFailed.setStatus(
        "current"
    )

zxAnEquipCardSvcCommSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 2, 13)
)
zxAnEquipCardSvcCommSuccess.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnCardConfMainType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardActMainType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardActType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardOperStatus"))
)
if mibBuilder.loadTexts:
    zxAnEquipCardSvcCommSuccess.setStatus(
        "current"
    )

zxAnEquipCardCpldInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 2, 14)
)
zxAnEquipCardCpldInvalid.setObjects(
    ("ZTE-AN-EQUIP-MIB", "zxAnCardCpldUpdateStatus")
)
if mibBuilder.loadTexts:
    zxAnEquipCardCpldInvalid.setStatus(
        "current"
    )

zxAnEquipCardSwNotRunning = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 2, 15)
)
zxAnEquipCardSwNotRunning.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnCardConfMainType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardActMainType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardActType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardAdminStatus"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardOperStatus"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardInvSn"))
)
if mibBuilder.loadTexts:
    zxAnEquipCardSwNotRunning.setStatus(
        "current"
    )

zxAnEquipCardSwNotRunningRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 2, 16)
)
zxAnEquipCardSwNotRunningRestore.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnCardConfMainType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardActMainType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardActType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardAdminStatus"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardOperStatus"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardInvSn"))
)
if mibBuilder.loadTexts:
    zxAnEquipCardSwNotRunningRestore.setStatus(
        "current"
    )

zxAnEquipCardOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 2, 17)
)
zxAnEquipCardOffline.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnCardConfMainType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardActMainType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardActType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardAdminStatus"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardOperStatus"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardInvSn"))
)
if mibBuilder.loadTexts:
    zxAnEquipCardOffline.setStatus(
        "current"
    )

zxAnEquipCardOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 2, 18)
)
zxAnEquipCardOnline.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnCardConfMainType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardActMainType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardActType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardAdminStatus"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardOperStatus"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardInvSn"))
)
if mibBuilder.loadTexts:
    zxAnEquipCardOnline.setStatus(
        "current"
    )

zxAnEquipCardTypeMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 2, 19)
)
zxAnEquipCardTypeMismatch.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnCardConfMainType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardActMainType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardActType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardAdminStatus"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardOperStatus"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardInvSn"))
)
if mibBuilder.loadTexts:
    zxAnEquipCardTypeMismatch.setStatus(
        "current"
    )

zxAnEquipCardTypeMismatchRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 2, 20)
)
zxAnEquipCardTypeMismatchRestore.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnCardConfMainType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardActMainType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardActType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardAdminStatus"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardOperStatus"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardInvSn"))
)
if mibBuilder.loadTexts:
    zxAnEquipCardTypeMismatchRestore.setStatus(
        "current"
    )

zxAnEquipCardNotConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 2, 21)
)
zxAnEquipCardNotConfigured.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnCardConfMainType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardActMainType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardActType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardAdminStatus"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardOperStatus"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardInvSn"))
)
if mibBuilder.loadTexts:
    zxAnEquipCardNotConfigured.setStatus(
        "current"
    )

zxAnEquipCardConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 2, 22)
)
zxAnEquipCardConfigured.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnCardConfMainType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardActMainType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardActType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardAdminStatus"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardOperStatus"),
        ("ZTE-AN-EQUIP-MIB", "zxAnCardInvSn"))
)
if mibBuilder.loadTexts:
    zxAnEquipCardConfigured.setStatus(
        "current"
    )

zxAnEquipCardNotSupportedAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 2, 23)
)
zxAnEquipCardNotSupportedAlm.setObjects(
    ("ZTE-AN-EQUIP-MIB", "zxAnCardOperStatus")
)
if mibBuilder.loadTexts:
    zxAnEquipCardNotSupportedAlm.setStatus(
        "current"
    )

zxAnEquipCardNotSupportedClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 2, 24)
)
zxAnEquipCardNotSupportedClr.setObjects(
    ("ZTE-AN-EQUIP-MIB", "zxAnCardOperStatus")
)
if mibBuilder.loadTexts:
    zxAnEquipCardNotSupportedClr.setStatus(
        "current"
    )

zxAnEquipSubCardUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 2, 30)
)
zxAnEquipSubCardUp.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnSubCardCfgMainType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnSubCardActMainType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnSubCardActType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnSubCardAdminStatus"),
        ("ZTE-AN-EQUIP-MIB", "zxAnSubCardOperStatus"),
        ("ZTE-AN-EQUIP-MIB", "zxAnSubcardInvSn"))
)
if mibBuilder.loadTexts:
    zxAnEquipSubCardUp.setStatus(
        "current"
    )

zxAnEquipSubCardDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 2, 31)
)
zxAnEquipSubCardDown.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnSubCardCfgMainType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnSubCardActMainType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnSubCardActType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnSubCardAdminStatus"),
        ("ZTE-AN-EQUIP-MIB", "zxAnSubCardOperStatus"),
        ("ZTE-AN-EQUIP-MIB", "zxAnSubcardInvSn"))
)
if mibBuilder.loadTexts:
    zxAnEquipSubCardDown.setStatus(
        "current"
    )

zxAnEquipSubcardCpldInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 2, 32)
)
zxAnEquipSubcardCpldInvalid.setObjects(
    ("ZTE-AN-EQUIP-MIB", "zxAnsubcardCpldUpdateStatus")
)
if mibBuilder.loadTexts:
    zxAnEquipSubcardCpldInvalid.setStatus(
        "current"
    )

zxAnPowerSupplyCardHardwareFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 2, 33)
)
zxAnPowerSupplyCardHardwareFault.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnPowerSupplyCardPreviousType"),
        ("ZTE-AN-EQUIP-MIB", "zxAnPowerSupplyCardCurrentType"))
)
if mibBuilder.loadTexts:
    zxAnPowerSupplyCardHardwareFault.setStatus(
        "current"
    )

zxAnEnvTempExceededTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 1)
)
zxAnEnvTempExceededTrap.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnEnvTemperature"),
        ("ZTE-AN-EQUIP-MIB", "zxAnEnvTemperatureAlarmThreshold"))
)
if mibBuilder.loadTexts:
    zxAnEnvTempExceededTrap.setStatus(
        "current"
    )

zxAnEnvTempNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 2)
)
zxAnEnvTempNormalTrap.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnEnvTemperature"),
        ("ZTE-AN-EQUIP-MIB", "zxAnEnvTemperatureAlarmThreshold"))
)
if mibBuilder.loadTexts:
    zxAnEnvTempNormalTrap.setStatus(
        "current"
    )

zxAnEnvMonitorInterfaceLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 3)
)
if mibBuilder.loadTexts:
    zxAnEnvMonitorInterfaceLinkDown.setStatus(
        "current"
    )

zxAnEnvMonitorInterfaceLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 4)
)
if mibBuilder.loadTexts:
    zxAnEnvMonitorInterfaceLinkUp.setStatus(
        "current"
    )

zxAnEnvFanLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 5)
)
zxAnEnvFanLinkDown.setObjects(
    ("ZTE-AN-EQUIP-MIB", "zxAnEnvFanOnlineStatus")
)
if mibBuilder.loadTexts:
    zxAnEnvFanLinkDown.setStatus(
        "current"
    )

zxAnEnvFanLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 6)
)
zxAnEnvFanLinkUp.setObjects(
    ("ZTE-AN-EQUIP-MIB", "zxAnEnvFanOnlineStatus")
)
if mibBuilder.loadTexts:
    zxAnEnvFanLinkUp.setStatus(
        "current"
    )

zxAnEnvTemperatureSensorFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 7)
)
if mibBuilder.loadTexts:
    zxAnEnvTemperatureSensorFault.setStatus(
        "current"
    )

zxAnEnvFanFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 8)
)
zxAnEnvFanFault.setObjects(
    ("ZTE-AN-EQUIP-MIB", "zxAnEnvFanOperStatus")
)
if mibBuilder.loadTexts:
    zxAnEnvFanFault.setStatus(
        "current"
    )

zxAnEnvFanFaultCleard = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 9)
)
zxAnEnvFanFaultCleard.setObjects(
    ("ZTE-AN-EQUIP-MIB", "zxAnEnvFanOperStatus")
)
if mibBuilder.loadTexts:
    zxAnEnvFanFaultCleard.setStatus(
        "current"
    )

zxAnEnvDustCapDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 10)
)
if mibBuilder.loadTexts:
    zxAnEnvDustCapDown.setStatus(
        "current"
    )

zxAnEnvDustCapUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 11)
)
if mibBuilder.loadTexts:
    zxAnEnvDustCapUp.setStatus(
        "current"
    )

zxAnEnvPowerSupplyDwon = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 12)
)
zxAnEnvPowerSupplyDwon.setObjects(
    ("ZTE-AN-EQUIP-MIB", "zxAnPowerSupplyOperState")
)
if mibBuilder.loadTexts:
    zxAnEnvPowerSupplyDwon.setStatus(
        "current"
    )

zxAnEnvPowerSupplyUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 13)
)
zxAnEnvPowerSupplyUp.setObjects(
    ("ZTE-AN-EQUIP-MIB", "zxAnPowerSupplyOperState")
)
if mibBuilder.loadTexts:
    zxAnEnvPowerSupplyUp.setStatus(
        "current"
    )

zxAnEnvMPTempExceededTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 14)
)
zxAnEnvMPTempExceededTrap.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnMPTemperature"),
        ("ZTE-AN-EQUIP-MIB", "zxAnMPTemperatureAlarmThreshold"))
)
if mibBuilder.loadTexts:
    zxAnEnvMPTempExceededTrap.setStatus(
        "current"
    )

zxAnEnvMPTempNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 15)
)
zxAnEnvMPTempNormalTrap.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnMPTemperature"),
        ("ZTE-AN-EQUIP-MIB", "zxAnMPTemperatureAlarmThreshold"))
)
if mibBuilder.loadTexts:
    zxAnEnvMPTempNormalTrap.setStatus(
        "current"
    )

zxAnEnvFanInterfaceLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 16)
)
if mibBuilder.loadTexts:
    zxAnEnvFanInterfaceLinkDown.setStatus(
        "current"
    )

zxAnEnvFanInterfaceLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 17)
)
if mibBuilder.loadTexts:
    zxAnEnvFanInterfaceLinkUp.setStatus(
        "current"
    )

zxAnEnvPowerOverVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 18)
)
zxAnEnvPowerOverVoltage.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnPowerSupplyInVoltage"),
        ("ZTE-AN-EQUIP-MIB", "zxAnPowerInVoltageUpperThresh"))
)
if mibBuilder.loadTexts:
    zxAnEnvPowerOverVoltage.setStatus(
        "current"
    )

zxAnEnvPowerOverVoltageCleard = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 19)
)
zxAnEnvPowerOverVoltageCleard.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnPowerSupplyInVoltage"),
        ("ZTE-AN-EQUIP-MIB", "zxAnPowerInVoltageUpperThresh"))
)
if mibBuilder.loadTexts:
    zxAnEnvPowerOverVoltageCleard.setStatus(
        "current"
    )

zxAnEnvPowerUnderVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 20)
)
zxAnEnvPowerUnderVoltage.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnPowerSupplyInVoltage"),
        ("ZTE-AN-EQUIP-MIB", "zxAnPowerInVoltageLowerThresh"))
)
if mibBuilder.loadTexts:
    zxAnEnvPowerUnderVoltage.setStatus(
        "current"
    )

zxAnEnvPowerUnderVoltageCleard = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 21)
)
zxAnEnvPowerUnderVoltageCleard.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnPowerSupplyInVoltage"),
        ("ZTE-AN-EQUIP-MIB", "zxAnPowerInVoltageLowerThresh"))
)
if mibBuilder.loadTexts:
    zxAnEnvPowerUnderVoltageCleard.setStatus(
        "current"
    )

zxAnEnvPowerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 22)
)
zxAnEnvPowerOff.setObjects(
    ("ZTE-AN-EQUIP-MIB", "zxAnPowerSupplyInVoltageStatus")
)
if mibBuilder.loadTexts:
    zxAnEnvPowerOff.setStatus(
        "current"
    )

zxAnEnvPowerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 23)
)
zxAnEnvPowerUp.setObjects(
    ("ZTE-AN-EQUIP-MIB", "zxAnPowerSupplyInVoltageStatus")
)
if mibBuilder.loadTexts:
    zxAnEnvPowerUp.setStatus(
        "current"
    )

zxAnEnvCardOverTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 24)
)
zxAnEnvCardOverTemperature.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnEnvCardTemperature"),
        ("ZTE-AN-EQUIP-MIB", "zxAnMPTemperatureAlarmThreshold"))
)
if mibBuilder.loadTexts:
    zxAnEnvCardOverTemperature.setStatus(
        "current"
    )

zxAnEnvCardOverTemperatureCleard = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 25)
)
zxAnEnvCardOverTemperatureCleard.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnEnvCardTemperature"),
        ("ZTE-AN-EQUIP-MIB", "zxAnMPTemperatureAlarmThreshold"))
)
if mibBuilder.loadTexts:
    zxAnEnvCardOverTemperatureCleard.setStatus(
        "current"
    )

zxAnEnvLowerFanBoardLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 26)
)
if mibBuilder.loadTexts:
    zxAnEnvLowerFanBoardLinkDown.setStatus(
        "current"
    )

zxAnEnvLowerFanBoardLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 27)
)
if mibBuilder.loadTexts:
    zxAnEnvLowerFanBoardLinkUp.setStatus(
        "current"
    )

zxAnEnvAcMainsPowerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 28)
)
if mibBuilder.loadTexts:
    zxAnEnvAcMainsPowerOff.setStatus(
        "current"
    )

zxAnEnvAcMainsPowerOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 29)
)
if mibBuilder.loadTexts:
    zxAnEnvAcMainsPowerOn.setStatus(
        "current"
    )

zxAnEnvGponCardsShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 30)
)
zxAnEnvGponCardsShutdown.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnMPTemperature"),
        ("ZTE-AN-EQUIP-MIB", "zxAnMPTemperatureAlarmThreshold"))
)
if mibBuilder.loadTexts:
    zxAnEnvGponCardsShutdown.setStatus(
        "current"
    )

zxAnEnvGponCardsStartup = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 31)
)
zxAnEnvGponCardsStartup.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnMPTemperature"),
        ("ZTE-AN-EQUIP-MIB", "zxAnMPTemperatureAlarmThreshold"))
)
if mibBuilder.loadTexts:
    zxAnEnvGponCardsStartup.setStatus(
        "current"
    )

zxAnEnvCardHighTempShutdownAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 32)
)
zxAnEnvCardHighTempShutdownAlm.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnEnvCardTemperature"),
        ("ZTE-AN-EQUIP-MIB", "zxAnEnvOverheatTmpThreshold"))
)
if mibBuilder.loadTexts:
    zxAnEnvCardHighTempShutdownAlm.setStatus(
        "current"
    )

zxAnEnvCardHighTempShutdownClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 33)
)
zxAnEnvCardHighTempShutdownClr.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnEnvCardTemperature"),
        ("ZTE-AN-EQUIP-MIB", "zxAnEnvOverheatTmpThreshold"))
)
if mibBuilder.loadTexts:
    zxAnEnvCardHighTempShutdownClr.setStatus(
        "current"
    )

zxAnEnvBroadbandOverheatHaltAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 34)
)
zxAnEnvBroadbandOverheatHaltAlm.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnEnvTemperature"),
        ("ZTE-AN-EQUIP-MIB", "zxAnEnvOverheatTmpThreshold"))
)
if mibBuilder.loadTexts:
    zxAnEnvBroadbandOverheatHaltAlm.setStatus(
        "current"
    )

zxAnEnvBroadbandOverheatHaltClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 35)
)
zxAnEnvBroadbandOverheatHaltClr.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnEnvTemperature"),
        ("ZTE-AN-EQUIP-MIB", "zxAnEnvOverheatTmpThreshold"))
)
if mibBuilder.loadTexts:
    zxAnEnvBroadbandOverheatHaltClr.setStatus(
        "current"
    )

zxAnBatteryEnergySavingBbHaltAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 36)
)
if mibBuilder.loadTexts:
    zxAnBatteryEnergySavingBbHaltAlm.setStatus(
        "current"
    )

zxAnBatteryEnergySavingBbHaltClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 37)
)
if mibBuilder.loadTexts:
    zxAnBatteryEnergySavingBbHaltClr.setStatus(
        "current"
    )

zxAnEnvDeviceAbnormalAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 38)
)
zxAnEnvDeviceAbnormalAlm.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnEnvDevMonSwitchDeviceId"),
        ("ZTE-AN-EQUIP-MIB", "zxAnEnvDevMonSwitchNormalStatus"),
        ("ZTE-AN-EQUIP-MIB", "zxAnEnvDevMonSwitchCurrStatus"),
        ("ZTE-AN-EQUIP-MIB", "zxAnEnvDeviceName"))
)
if mibBuilder.loadTexts:
    zxAnEnvDeviceAbnormalAlm.setStatus(
        "current"
    )

zxAnEnvDeviceAbnormalClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 39)
)
zxAnEnvDeviceAbnormalClr.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnEnvDevMonSwitchDeviceId"),
        ("ZTE-AN-EQUIP-MIB", "zxAnEnvDevMonSwitchNormalStatus"),
        ("ZTE-AN-EQUIP-MIB", "zxAnEnvDevMonSwitchCurrStatus"),
        ("ZTE-AN-EQUIP-MIB", "zxAnEnvDeviceName"))
)
if mibBuilder.loadTexts:
    zxAnEnvDeviceAbnormalClr.setStatus(
        "current"
    )

zxAnEnvNoBatteryAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 40)
)
if mibBuilder.loadTexts:
    zxAnEnvNoBatteryAlm.setStatus(
        "current"
    )

zxAnEnvNoBatteryClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 41)
)
if mibBuilder.loadTexts:
    zxAnEnvNoBatteryClr.setStatus(
        "current"
    )

zxAnEnvBatteryUnderVoltageAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 42)
)
if mibBuilder.loadTexts:
    zxAnEnvBatteryUnderVoltageAlm.setStatus(
        "current"
    )

zxAnEnvBatteryUnderVoltageClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 3, 43)
)
if mibBuilder.loadTexts:
    zxAnEnvBatteryUnderVoltageClr.setStatus(
        "current"
    )

zxAnEnvExTempExceededTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 4, 1)
)
zxAnEnvExTempExceededTrap.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnRackNo"),
        ("ZTE-AN-EQUIP-MIB", "zxAnShelfNo"),
        ("ZTE-AN-EQUIP-MIB", "zxAnSlotNo"),
        ("ZTE-AN-EQUIP-MIB", "zxAnEnvExTemperature"),
        ("ZTE-AN-EQUIP-MIB", "zxAnEnvExTempAlarmThreshold"))
)
if mibBuilder.loadTexts:
    zxAnEnvExTempExceededTrap.setStatus(
        "current"
    )

zxAnEnvExTempNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 4, 2)
)
zxAnEnvExTempNormalTrap.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnRackNo"),
        ("ZTE-AN-EQUIP-MIB", "zxAnShelfNo"),
        ("ZTE-AN-EQUIP-MIB", "zxAnSlotNo"),
        ("ZTE-AN-EQUIP-MIB", "zxAnEnvExTemperature"),
        ("ZTE-AN-EQUIP-MIB", "zxAnEnvExTempAlarmThreshold"))
)
if mibBuilder.loadTexts:
    zxAnEnvExTempNormalTrap.setStatus(
        "current"
    )

zxAnEnvExFanInterfaceLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 4, 3)
)
zxAnEnvExFanInterfaceLinkDown.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnRackNo"),
        ("ZTE-AN-EQUIP-MIB", "zxAnShelfNo"),
        ("ZTE-AN-EQUIP-MIB", "zxAnSlotNo"))
)
if mibBuilder.loadTexts:
    zxAnEnvExFanInterfaceLinkDown.setStatus(
        "current"
    )

zxAnEnvExFanInterfaceLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 4, 4)
)
zxAnEnvExFanInterfaceLinkUp.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnRackNo"),
        ("ZTE-AN-EQUIP-MIB", "zxAnShelfNo"),
        ("ZTE-AN-EQUIP-MIB", "zxAnSlotNo"))
)
if mibBuilder.loadTexts:
    zxAnEnvExFanInterfaceLinkUp.setStatus(
        "current"
    )

zxAnEnvExFanFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 4, 5)
)
zxAnEnvExFanFault.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnRackNo"),
        ("ZTE-AN-EQUIP-MIB", "zxAnShelfNo"),
        ("ZTE-AN-EQUIP-MIB", "zxAnSlotNo"),
        ("ZTE-AN-EQUIP-MIB", "zxAnFanExIndex"),
        ("ZTE-AN-EQUIP-MIB", "zxAnFanExOperStatus"))
)
if mibBuilder.loadTexts:
    zxAnEnvExFanFault.setStatus(
        "current"
    )

zxAnEnvExFanFaultCleard = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 2, 2, 4, 6)
)
zxAnEnvExFanFaultCleard.setObjects(
      *(("ZTE-AN-EQUIP-MIB", "zxAnRackNo"),
        ("ZTE-AN-EQUIP-MIB", "zxAnShelfNo"),
        ("ZTE-AN-EQUIP-MIB", "zxAnSlotNo"),
        ("ZTE-AN-EQUIP-MIB", "zxAnFanExIndex"),
        ("ZTE-AN-EQUIP-MIB", "zxAnFanExOperStatus"))
)
if mibBuilder.loadTexts:
    zxAnEnvExFanFaultCleard.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-EQUIP-MIB",
    **{"zxAnEquipMib": zxAnEquipMib,
       "zxAnEquipObjects": zxAnEquipObjects,
       "zxAnChassisMgmt": zxAnChassisMgmt,
       "zxAnRackTable": zxAnRackTable,
       "zxAnRackEntry": zxAnRackEntry,
       "zxAnRackNo": zxAnRackNo,
       "zxAnRackActType": zxAnRackActType,
       "zxAnRackCfgType": zxAnRackCfgType,
       "zxAnRackInvSn": zxAnRackInvSn,
       "zxAnRackRowStatus": zxAnRackRowStatus,
       "zxAnShelfTable": zxAnShelfTable,
       "zxAnShelfEntry": zxAnShelfEntry,
       "zxAnShelfNo": zxAnShelfNo,
       "zxAnShelfHardVersion": zxAnShelfHardVersion,
       "zxAnShelfActType": zxAnShelfActType,
       "zxAnShelfCfgType": zxAnShelfCfgType,
       "zxAnShelfInvSn": zxAnShelfInvSn,
       "zxAnShelfCleiCode": zxAnShelfCleiCode,
       "zxAnLogicShelfNo": zxAnLogicShelfNo,
       "zxAnShelfHardwareType": zxAnShelfHardwareType,
       "zxAnShelfAlias": zxAnShelfAlias,
       "zxAnShelfAdminStatus": zxAnShelfAdminStatus,
       "zxAnShelfRowStatus": zxAnShelfRowStatus,
       "zxAnCardTable": zxAnCardTable,
       "zxAnCardEntry": zxAnCardEntry,
       "zxAnSlotNo": zxAnSlotNo,
       "zxAnCardConfMainType": zxAnCardConfMainType,
       "zxAnCardActMainType": zxAnCardActMainType,
       "zxAnCardActType": zxAnCardActType,
       "zxAnCardOperStatus": zxAnCardOperStatus,
       "zxAnCardAdminStatus": zxAnCardAdminStatus,
       "zxAnCardPortNums": zxAnCardPortNums,
       "zxAnCardActivePortNums": zxAnCardActivePortNums,
       "zxAnCardCpuLoad": zxAnCardCpuLoad,
       "zxAnCardCpuLoadThreshold": zxAnCardCpuLoadThreshold,
       "zxAnCardMemUsage": zxAnCardMemUsage,
       "zxAnCardMemUsageThreshold": zxAnCardMemUsageThreshold,
       "zxAnCardStandbyStatus": zxAnCardStandbyStatus,
       "zxAnCardInvSn": zxAnCardInvSn,
       "zxAnCardCleiCode": zxAnCardCleiCode,
       "zxAnCardAccessoriesType": zxAnCardAccessoriesType,
       "zxAnCardAccessoriesOperstatus": zxAnCardAccessoriesOperstatus,
       "zxAnCardLockStatus": zxAnCardLockStatus,
       "zxAnCardMemSize": zxAnCardMemSize,
       "zxAnCardCpldUpdateStatus": zxAnCardCpldUpdateStatus,
       "zxAnCardAvailableStorageSize": zxAnCardAvailableStorageSize,
       "zxAnCardTotalStorageSize": zxAnCardTotalStorageSize,
       "zxAnCardEnergySavingEnable": zxAnCardEnergySavingEnable,
       "zxAnCardAlias": zxAnCardAlias,
       "zxAnCardLastStartupTime": zxAnCardLastStartupTime,
       "zxAnCardRowStatus": zxAnCardRowStatus,
       "zxAnSubcardTable": zxAnSubcardTable,
       "zxAnSubcardEntry": zxAnSubcardEntry,
       "zxAnSubcardNo": zxAnSubcardNo,
       "zxAnSubCardCfgMainType": zxAnSubCardCfgMainType,
       "zxAnSubCardActMainType": zxAnSubCardActMainType,
       "zxAnSubCardActType": zxAnSubCardActType,
       "zxAnSubcardOperStatus": zxAnSubcardOperStatus,
       "zxAnSubcardAdminStatus": zxAnSubcardAdminStatus,
       "zxAnSubcardPortNums": zxAnSubcardPortNums,
       "zxAnSubcardActivePortNums": zxAnSubcardActivePortNums,
       "zxAnSubcardCpuLoad": zxAnSubcardCpuLoad,
       "zxAnSubcardMemUsage": zxAnSubcardMemUsage,
       "zxAnSubcardInvSn": zxAnSubcardInvSn,
       "zxAnSubcardCleiCode": zxAnSubcardCleiCode,
       "zxAnSubcardMemSize": zxAnSubcardMemSize,
       "zxAnSubcardCpldUpdateStatus": zxAnSubcardCpldUpdateStatus,
       "zxAnSubcardRowStatus": zxAnSubcardRowStatus,
       "zxAnPhyConfMgmt": zxAnPhyConfMgmt,
       "zxAnStandbyEnableTable": zxAnStandbyEnableTable,
       "zxAnStandbyEnableEntry": zxAnStandbyEnableEntry,
       "zxStandbyEnable": zxStandbyEnable,
       "zxAnChassisPnpMode": zxAnChassisPnpMode,
       "zxAnPowerSupplyCardTable": zxAnPowerSupplyCardTable,
       "zxAnPowerSupplyCardEntry": zxAnPowerSupplyCardEntry,
       "zxAnPowerSupplyCardPreviousType": zxAnPowerSupplyCardPreviousType,
       "zxAnPowerSupplyCardCurrentType": zxAnPowerSupplyCardCurrentType,
       "zxAnVerMgmt": zxAnVerMgmt,
       "zxAnVerFtpMgmt": zxAnVerFtpMgmt,
       "zxAnFtpVerFileType": zxAnFtpVerFileType,
       "zxAnFtpVerClntOperType": zxAnFtpVerClntOperType,
       "zxAnFtpVerServerIpAddress": zxAnFtpVerServerIpAddress,
       "zxAnFtpVerServerUserName": zxAnFtpVerServerUserName,
       "zxAnFtpVerServerUserPwd": zxAnFtpVerServerUserPwd,
       "zxAnFtpVerServerFilePath": zxAnFtpVerServerFilePath,
       "zxAnFtpVerServerFileName": zxAnFtpVerServerFileName,
       "zxAnFtpVerClntAdminStatus": zxAnFtpVerClntAdminStatus,
       "zxAnFtpVerClntOperStatus": zxAnFtpVerClntOperStatus,
       "zxAnFtpVerClntFailedReason": zxAnFtpVerClntFailedReason,
       "zxAnSwManualUpdateShelf": zxAnSwManualUpdateShelf,
       "zxAnSwManualUpdateSlotList": zxAnSwManualUpdateSlotList,
       "zxAnSwManualUpdateCardType": zxAnSwManualUpdateCardType,
       "zxAnFtpVerUpdateFileLocation": zxAnFtpVerUpdateFileLocation,
       "zxAnFtpVerClntProgress": zxAnFtpVerClntProgress,
       "zxAnFtpVerFileSize": zxAnFtpVerFileSize,
       "zxAnFtpAdminType": zxAnFtpAdminType,
       "zxAnFtpProtocolType": zxAnFtpProtocolType,
       "zxAnCardVersionTable": zxAnCardVersionTable,
       "zxAnCardVersionEntry": zxAnCardVersionEntry,
       "zxAnSwCardHardwareVersion": zxAnSwCardHardwareVersion,
       "zxAnSwCardFileName": zxAnSwCardFileName,
       "zxAnSwCardFileType": zxAnSwCardFileType,
       "zxAnSwCardVersion": zxAnSwCardVersion,
       "zxAnSwCardFileLen": zxAnSwCardFileLen,
       "zxAnSwCardBuildTime": zxAnSwCardBuildTime,
       "zxAnSwCardBootwareFileName": zxAnSwCardBootwareFileName,
       "zxAnSwCardBootwareFileType": zxAnSwCardBootwareFileType,
       "zxAnSwCardBootwareVersion": zxAnSwCardBootwareVersion,
       "zxAnSwCardBootwareFileLen": zxAnSwCardBootwareFileLen,
       "zxAnSwCardBootwareBuildTime": zxAnSwCardBootwareBuildTime,
       "zxAnSwCardFirmware1FileName": zxAnSwCardFirmware1FileName,
       "zxAnSwCardFirmware1FileType": zxAnSwCardFirmware1FileType,
       "zxAnSwCardFirmware1Version": zxAnSwCardFirmware1Version,
       "zxAnSwCardFirmware1FileLen": zxAnSwCardFirmware1FileLen,
       "zxAnSwCardFirmware1BuildTime": zxAnSwCardFirmware1BuildTime,
       "zxAnSwCardFirmware2FileName": zxAnSwCardFirmware2FileName,
       "zxAnSwCardFirmware2FileType": zxAnSwCardFirmware2FileType,
       "zxAnSwCardFirmware2Version": zxAnSwCardFirmware2Version,
       "zxAnSwCardFirmware2FileLen": zxAnSwCardFirmware2FileLen,
       "zxAnSwCardFirmware2BuildTime": zxAnSwCardFirmware2BuildTime,
       "zxAnSwCardFirmware3FileName": zxAnSwCardFirmware3FileName,
       "zxAnSwCardFirmware3FileType": zxAnSwCardFirmware3FileType,
       "zxAnSwCardFirmware3Version": zxAnSwCardFirmware3Version,
       "zxAnSwCardFirmware3FileLen": zxAnSwCardFirmware3FileLen,
       "zxAnSwCardFirmware3BuildTime": zxAnSwCardFirmware3BuildTime,
       "zxAnSubcardVersionTable": zxAnSubcardVersionTable,
       "zxAnSubcardVersionEntry": zxAnSubcardVersionEntry,
       "zxAnSwSubcardHardwareVersion": zxAnSwSubcardHardwareVersion,
       "zxAnSwSubcardFileName": zxAnSwSubcardFileName,
       "zxAnSwSubcardFileType": zxAnSwSubcardFileType,
       "zxAnSwSubcardVersion": zxAnSwSubcardVersion,
       "zxAnSwSubcardFileLen": zxAnSwSubcardFileLen,
       "zxAnSwSubcardBuildTime": zxAnSwSubcardBuildTime,
       "zxAnSwSubcardBootwareFileName": zxAnSwSubcardBootwareFileName,
       "zxAnSwSubcardBootwareFileType": zxAnSwSubcardBootwareFileType,
       "zxAnSwSubcardBootwareVersion": zxAnSwSubcardBootwareVersion,
       "zxAnSwSubcardBootwareFileLen": zxAnSwSubcardBootwareFileLen,
       "zxAnSwSubcardBootwareBuildTime": zxAnSwSubcardBootwareBuildTime,
       "zxAnSwSubcardFirmwareFileName": zxAnSwSubcardFirmwareFileName,
       "zxAnSwSubcardFirmwareFileType": zxAnSwSubcardFirmwareFileType,
       "zxAnSwSubcardFirmwareVersion": zxAnSwSubcardFirmwareVersion,
       "zxAnSwSubcardFirmwareFileLen": zxAnSwSubcardFirmwareFileLen,
       "zxAnSwSubcardFirmwareBuildTime": zxAnSwSubcardFirmwareBuildTime,
       "zxAnVersionSavedTable": zxAnVersionSavedTable,
       "zxAnVersionSavedEntry": zxAnVersionSavedEntry,
       "zxAnSwImageFileName": zxAnSwImageFileName,
       "zxAnSwImageFileType": zxAnSwImageFileType,
       "zxAnSwImageVersion": zxAnSwImageVersion,
       "zxAnSwImageFileLen": zxAnSwImageFileLen,
       "zxAnSwImageBuildTime": zxAnSwImageBuildTime,
       "zxAnSwImageActiveStatus": zxAnSwImageActiveStatus,
       "zxAnSwImageSyncToSecondary": zxAnSwImageSyncToSecondary,
       "zxAnSwImageSyncToSecondaryStatus": zxAnSwImageSyncToSecondaryStatus,
       "zxAnSavedTableType": zxAnSavedTableType,
       "zxAnSavedFileDesc": zxAnSavedFileDesc,
       "zxAnSavedPatchParentVersion": zxAnSavedPatchParentVersion,
       "zxAnSavedPatchActiveTime": zxAnSavedPatchActiveTime,
       "zxAnSavedPatchActiveStatus": zxAnSavedPatchActiveStatus,
       "zxAnSavedPatchAdminStatus": zxAnSavedPatchAdminStatus,
       "zxAnSavedAdminFailedReason": zxAnSavedAdminFailedReason,
       "zxAnSavedVersionDownloadTime": zxAnSavedVersionDownloadTime,
       "zxAnVersionUpdatingStatusTable": zxAnVersionUpdatingStatusTable,
       "zxAnVersionUpdatingStatusEntry": zxAnVersionUpdatingStatusEntry,
       "zxAnSwManualUpdateSoftwareType": zxAnSwManualUpdateSoftwareType,
       "zxAnSwManualUpdateStatus": zxAnSwManualUpdateStatus,
       "zxAnSwManualFailedReason": zxAnSwManualFailedReason,
       "zxAnCpeSoftwareMgmt": zxAnCpeSoftwareMgmt,
       "zxAnCpeSwUpdateTaskTable": zxAnCpeSwUpdateTaskTable,
       "zxAnCpeSwUpdateTaskEntry": zxAnCpeSwUpdateTaskEntry,
       "zxAnCpeSwUpdateTaskId": zxAnCpeSwUpdateTaskId,
       "zxAnCpeSwUpdateTaskCreateTime": zxAnCpeSwUpdateTaskCreateTime,
       "zxAnCpeSwUpdateTaskDesc": zxAnCpeSwUpdateTaskDesc,
       "zxAnCpeSwUpdateTaskStatus": zxAnCpeSwUpdateTaskStatus,
       "zxAnCpeSwUpdateTaskCpeCategory": zxAnCpeSwUpdateTaskCpeCategory,
       "zxAnCpeSwUpdateTaskAdminStatus": zxAnCpeSwUpdateTaskAdminStatus,
       "zxAnCpeSwUpdateTaskGranularity": zxAnCpeSwUpdateTaskGranularity,
       "zxAnCpeSwUpdateTaskObjList": zxAnCpeSwUpdateTaskObjList,
       "zxAnCpeSwUpdateTaskCpeModel": zxAnCpeSwUpdateTaskCpeModel,
       "zxAnCpeSwUpdateTaskCpeVersions": zxAnCpeSwUpdateTaskCpeVersions,
       "zxAnCpeSwUpdateTaskVerFileName": zxAnCpeSwUpdateTaskVerFileName,
       "zxAnCpeSwUpdateTaskVerFileLoc": zxAnCpeSwUpdateTaskVerFileLoc,
       "zxAnCpeSwUpdateTaskFtpDir": zxAnCpeSwUpdateTaskFtpDir,
       "zxAnCpeSwUpdateTaskExpiration": zxAnCpeSwUpdateTaskExpiration,
       "zxAnCpeSwUpdateTaskAutoDelete": zxAnCpeSwUpdateTaskAutoDelete,
       "zxAnCpeSwUpdateTaskAutoUpdate": zxAnCpeSwUpdateTaskAutoUpdate,
       "zxAnCpeSwUpdateTaskRowStatus": zxAnCpeSwUpdateTaskRowStatus,
       "zxAnCpeSwUpdateTaskStatTable": zxAnCpeSwUpdateTaskStatTable,
       "zxAnCpeSwUpdateTaskStatEntry": zxAnCpeSwUpdateTaskStatEntry,
       "zxAnCpeSwUpateTotals": zxAnCpeSwUpateTotals,
       "zxAnCpeSwUpdateSucceeds": zxAnCpeSwUpdateSucceeds,
       "zxAnCpeSwUpdatings": zxAnCpeSwUpdatings,
       "zxAnCpeSwUpdateFails": zxAnCpeSwUpdateFails,
       "zxAnCpeSwAutoUpdateSucceeds": zxAnCpeSwAutoUpdateSucceeds,
       "zxAnCpeSwUpdateTaskFailedTable": zxAnCpeSwUpdateTaskFailedTable,
       "zxAnCpeSwUpdateTaskFailedEntry": zxAnCpeSwUpdateTaskFailedEntry,
       "zxAnCpeSwRackNo": zxAnCpeSwRackNo,
       "zxAnCpeSwShelfNo": zxAnCpeSwShelfNo,
       "zxAnCpeSwSlotNo": zxAnCpeSwSlotNo,
       "zxAnCpeSwPortNo": zxAnCpeSwPortNo,
       "zxAnCpeSwOnuNo": zxAnCpeSwOnuNo,
       "zxAnCpeSwCircuitType": zxAnCpeSwCircuitType,
       "zxAnCpeSwUpdateTaskFailCpeName": zxAnCpeSwUpdateTaskFailCpeName,
       "zxAnCpeSwUpdateTaskFailReason": zxAnCpeSwUpdateTaskFailReason,
       "zxAnCpeSwStatusTable": zxAnCpeSwStatusTable,
       "zxAnCpeSwStatusEntry": zxAnCpeSwStatusEntry,
       "zxAnCpeSwCpeName": zxAnCpeSwCpeName,
       "zxAnCpeSwUpdateStatus": zxAnCpeSwUpdateStatus,
       "zxAnCpeSwUpdateFailReason": zxAnCpeSwUpdateFailReason,
       "zxAnCpeSwUpdateProgress": zxAnCpeSwUpdateProgress,
       "zxAnCpeSwCurrVer": zxAnCpeSwCurrVer,
       "zxAnCpeSwCurrVerBuildTime": zxAnCpeSwCurrVerBuildTime,
       "zxAnCpeSwUpdatingVer": zxAnCpeSwUpdatingVer,
       "zxAnCpeSwUpdatingVerBuildTime": zxAnCpeSwUpdatingVerBuildTime,
       "zxAnCpeSwVendorId": zxAnCpeSwVendorId,
       "zxAnCpeSwProductId": zxAnCpeSwProductId,
       "zxAnVerAutoUpdateMgmt": zxAnVerAutoUpdateMgmt,
       "zxAnVerAutoUpdateBootUpdateEn": zxAnVerAutoUpdateBootUpdateEn,
       "zxAnVerAutoUpdateVerBackupEn": zxAnVerAutoUpdateVerBackupEn,
       "zxAnVerAutoUpdateVersionPath": zxAnVerAutoUpdateVersionPath,
       "zxAnVerAutoUpdateBackupPath": zxAnVerAutoUpdateBackupPath,
       "zxAnVerAutoUpdateLogPath": zxAnVerAutoUpdateLogPath,
       "zxAnVerAutoUpdateAction": zxAnVerAutoUpdateAction,
       "zxAnVerAutoUpdateStatus": zxAnVerAutoUpdateStatus,
       "zxAnVerAutoUpdateFailedReason": zxAnVerAutoUpdateFailedReason,
       "zxAnEnvMonitor": zxAnEnvMonitor,
       "zxAnEnvMgmtCapabilities": zxAnEnvMgmtCapabilities,
       "zxAnEnvTemperature": zxAnEnvTemperature,
       "zxAnEnvTemperatureAlarmThreshold": zxAnEnvTemperatureAlarmThreshold,
       "zxAnEnvMonitorInterfaceUsage": zxAnEnvMonitorInterfaceUsage,
       "zxAnMPTemperature": zxAnMPTemperature,
       "zxAnMPTemperatureAlarmThreshold": zxAnMPTemperatureAlarmThreshold,
       "zxAnEpmConnectPort": zxAnEpmConnectPort,
       "zxAnEnvBackplaneInterfaceUsage": zxAnEnvBackplaneInterfaceUsage,
       "zxAnEnvPowerSupplyMgmt": zxAnEnvPowerSupplyMgmt,
       "zxAnPowerSupplyCount": zxAnPowerSupplyCount,
       "zxAnPowerSupplyTable": zxAnPowerSupplyTable,
       "zxAnPowerSupplyEntry": zxAnPowerSupplyEntry,
       "zxAnPowerSupplyInVoltageStatus": zxAnPowerSupplyInVoltageStatus,
       "zxAnPowerSupplyOperState": zxAnPowerSupplyOperState,
       "zxAnPowerSupplyInVoltage": zxAnPowerSupplyInVoltage,
       "zxAnPowerInVoltageUpperThresh": zxAnPowerInVoltageUpperThresh,
       "zxAnPowerInVoltageLowerThresh": zxAnPowerInVoltageLowerThresh,
       "zxAnPowerSupplyInCurrent": zxAnPowerSupplyInCurrent,
       "zxAnPowerInCurrentThresh": zxAnPowerInCurrentThresh,
       "zxAnPowerSupplyInPower": zxAnPowerSupplyInPower,
       "zxAnEnvFanMgmt": zxAnEnvFanMgmt,
       "zxAnEnvFanAlarmBeepEnable": zxAnEnvFanAlarmBeepEnable,
       "zxAnEnvFanAutoSwitchByCardInst": zxAnEnvFanAutoSwitchByCardInst,
       "zxAnEnvFanTrayHardwareVersion": zxAnEnvFanTrayHardwareVersion,
       "zxAnEnvFanTraySoftwareVersion": zxAnEnvFanTraySoftwareVersion,
       "zxAnEnvFanInvSn": zxAnEnvFanInvSn,
       "zxAnEnvFanSpeedCtrlMgmt": zxAnEnvFanSpeedCtrlMgmt,
       "zxAnEnvFanSpeedCtrlMode": zxAnEnvFanSpeedCtrlMode,
       "zxAnEnvFanLowSpeed": zxAnEnvFanLowSpeed,
       "zxAnEnvFanStandardSpeed": zxAnEnvFanStandardSpeed,
       "zxAnEnvFanHighSpeed": zxAnEnvFanHighSpeed,
       "zxAnEnvFanSuperSpeed": zxAnEnvFanSuperSpeed,
       "zxAnEnvFanLowSpeedShiftTem": zxAnEnvFanLowSpeedShiftTem,
       "zxAnEnvFanStdSpeedShiftTem": zxAnEnvFanStdSpeedShiftTem,
       "zxAnEnvFanHighSpeedShiftTem": zxAnEnvFanHighSpeedShiftTem,
       "zxAnEnvFanSuperSpeedShiftTem": zxAnEnvFanSuperSpeedShiftTem,
       "zxAnEnvFanTable": zxAnEnvFanTable,
       "zxAnEnvFanEntry": zxAnEnvFanEntry,
       "zxAnEnvFanIndex": zxAnEnvFanIndex,
       "zxAnEnvFanConfSpeedLevel": zxAnEnvFanConfSpeedLevel,
       "zxAnEnvFanActualSpeedLevel": zxAnEnvFanActualSpeedLevel,
       "zxAnEnvFanAdminStatus": zxAnEnvFanAdminStatus,
       "zxAnEnvFanOperStatus": zxAnEnvFanOperStatus,
       "zxAnEnvFanOnlineStatus": zxAnEnvFanOnlineStatus,
       "zxAnEnvFanActualSpeed": zxAnEnvFanActualSpeed,
       "zxAnEnvFanLowSpeedPercentage": zxAnEnvFanLowSpeedPercentage,
       "zxAnEnvFanStandardSpeedPercent": zxAnEnvFanStandardSpeedPercent,
       "zxAnEnvFanHighSpeedPercentage": zxAnEnvFanHighSpeedPercentage,
       "zxAnEnvFanSuperSpeedPercentage": zxAnEnvFanSuperSpeedPercentage,
       "zxAnEnvDustCapMgmt": zxAnEnvDustCapMgmt,
       "zxAnEnvDustCapOperStatus": zxAnEnvDustCapOperStatus,
       "zxAnEnvMonitorIfTrapEnable": zxAnEnvMonitorIfTrapEnable,
       "zxAnEnvCardMgmt": zxAnEnvCardMgmt,
       "zxAnEnvCardTemperatureTable": zxAnEnvCardTemperatureTable,
       "zxAnEnvCardTemperatureEntry": zxAnEnvCardTemperatureEntry,
       "zxAnEnvCardTemperature": zxAnEnvCardTemperature,
       "zxAnEnvOverheatProtectionMgmt": zxAnEnvOverheatProtectionMgmt,
       "zxAnEnvOverheatProtectionObjects": zxAnEnvOverheatProtectionObjects,
       "zxAnEnvOverheatProtectionEnable": zxAnEnvOverheatProtectionEnable,
       "zxAnEnvOverheatTmpThreshold": zxAnEnvOverheatTmpThreshold,
       "zxAnEnvOverheatDurThreshold": zxAnEnvOverheatDurThreshold,
       "zxAnEnvOverheatAutoRecoveryType": zxAnEnvOverheatAutoRecoveryType,
       "zxAnEnvOverheatAutoRecoveryEn": zxAnEnvOverheatAutoRecoveryEn,
       "zxAnEnvAutoRecoveryTmpThreshold": zxAnEnvAutoRecoveryTmpThreshold,
       "zxAnEnvOverheatAutoRecoveryTime": zxAnEnvOverheatAutoRecoveryTime,
       "zxAnEnvOverheatProtectionStatus": zxAnEnvOverheatProtectionStatus,
       "zxAnEnvBatteryObjects": zxAnEnvBatteryObjects,
       "zxAnEnvBatteryGlobalObjects": zxAnEnvBatteryGlobalObjects,
       "zxAnEnvBatteryEnergySavingEnable": zxAnEnvBatteryEnergySavingEnable,
       "zxAnEnvDeviceObjects": zxAnEnvDeviceObjects,
       "zxAnEnvDeviceTable": zxAnEnvDeviceTable,
       "zxAnEnvDeviceEntry": zxAnEnvDeviceEntry,
       "zxAnEnvDeviceId": zxAnEnvDeviceId,
       "zxAnEnvDeviceName": zxAnEnvDeviceName,
       "zxAnEnvDeviceRowStatus": zxAnEnvDeviceRowStatus,
       "zxAnEnvDevMonSwitchTable": zxAnEnvDevMonSwitchTable,
       "zxAnEnvDevMonSwitchEntry": zxAnEnvDevMonSwitchEntry,
       "zxAnEnvDevMonSwitchId": zxAnEnvDevMonSwitchId,
       "zxAnEnvDevMonSwitchDeviceId": zxAnEnvDevMonSwitchDeviceId,
       "zxAnEnvDevMonSwitchTrapEnable": zxAnEnvDevMonSwitchTrapEnable,
       "zxAnEnvDevMonSwitchNormalStatus": zxAnEnvDevMonSwitchNormalStatus,
       "zxAnEnvDevMonSwitchCurrStatus": zxAnEnvDevMonSwitchCurrStatus,
       "zxAnPatchMgmt": zxAnPatchMgmt,
       "zxAnPatchTable": zxAnPatchTable,
       "zxAnPatchEntry": zxAnPatchEntry,
       "zxAnPatchName": zxAnPatchName,
       "zxAnPatchSystemVersion": zxAnPatchSystemVersion,
       "zxAnPatchVersionNo": zxAnPatchVersionNo,
       "zxAnPatchSize": zxAnPatchSize,
       "zxAnPatchStatus": zxAnPatchStatus,
       "zxAnPatchCreateTime": zxAnPatchCreateTime,
       "zxAnPatchActiveTime": zxAnPatchActiveTime,
       "zxAnPatchRunningTime": zxAnPatchRunningTime,
       "zxAnPatchDesc": zxAnPatchDesc,
       "zxAnPatchAdminStatus": zxAnPatchAdminStatus,
       "zxAnEquipStat": zxAnEquipStat,
       "zxAnCardStatTable": zxAnCardStatTable,
       "zxAnCardStatEntry": zxAnCardStatEntry,
       "zxAnCardInOctets": zxAnCardInOctets,
       "zxAnCardInUcastPkts": zxAnCardInUcastPkts,
       "zxAnCardInMulticastPkts": zxAnCardInMulticastPkts,
       "zxAnCardInBroadcastPkts": zxAnCardInBroadcastPkts,
       "zxAnCardOutOctets": zxAnCardOutOctets,
       "zxAnCardOutUcastPkts": zxAnCardOutUcastPkts,
       "zxAnCardOutMulticastPkts": zxAnCardOutMulticastPkts,
       "zxAnCardOutBroadcastPkts": zxAnCardOutBroadcastPkts,
       "zxAnCardInErrors": zxAnCardInErrors,
       "zxAnCardOutErrors": zxAnCardOutErrors,
       "zxAnCardInDiscardPkts": zxAnCardInDiscardPkts,
       "zxAnCardOutDiscardPkts": zxAnCardOutDiscardPkts,
       "zxAnCardInDiscardPktRatio": zxAnCardInDiscardPktRatio,
       "zxAnCardOutDiscardPktRatio": zxAnCardOutDiscardPktRatio,
       "zxAnCardDot3InPauseFrames": zxAnCardDot3InPauseFrames,
       "zxAnCardDot3OutPauseFrames": zxAnCardDot3OutPauseFrames,
       "zxAnEquipSysMgmt": zxAnEquipSysMgmt,
       "zxAnEquipSysLastSwapRequest": zxAnEquipSysLastSwapRequest,
       "zxAnEquipSysAutoSwapEnable": zxAnEquipSysAutoSwapEnable,
       "zxAnEquipSysAutoSwapStartTime": zxAnEquipSysAutoSwapStartTime,
       "zxAnEquipSysAutoSwapInterval": zxAnEquipSysAutoSwapInterval,
       "zxAnEquipSysAutoSwapRemainDays": zxAnEquipSysAutoSwapRemainDays,
       "zxAnEquipShelfAutoSwapInterval": zxAnEquipShelfAutoSwapInterval,
       "zxAnEnvExMonitor": zxAnEnvExMonitor,
       "zxAnEnvExMgmt": zxAnEnvExMgmt,
       "zxAnEnvExMgmtTable": zxAnEnvExMgmtTable,
       "zxAnEnvExMgmtEntry": zxAnEnvExMgmtEntry,
       "zxAnEnvExTemperature": zxAnEnvExTemperature,
       "zxAnEnvExTempAlarmThreshold": zxAnEnvExTempAlarmThreshold,
       "zxAnEnvExMonitorIfUsage": zxAnEnvExMonitorIfUsage,
       "zxAnEnvExTempCtrlMgmt": zxAnEnvExTempCtrlMgmt,
       "zxAnEnvExTempCtrlTable": zxAnEnvExTempCtrlTable,
       "zxAnEnvExTempCtrlEntry": zxAnEnvExTempCtrlEntry,
       "zxAnEnvExTempCtrlEnable": zxAnEnvExTempCtrlEnable,
       "zxAnEnvExTempCtrlLowThresh": zxAnEnvExTempCtrlLowThresh,
       "zxAnEnvExTempCtrlMediumThresh": zxAnEnvExTempCtrlMediumThresh,
       "zxAnEnvExTempCtrlHighThresh": zxAnEnvExTempCtrlHighThresh,
       "zxAnFanTrayExMgmt": zxAnFanTrayExMgmt,
       "zxAnFanTrayExMgmtTable": zxAnFanTrayExMgmtTable,
       "zxAnFanTrayExMgmtEntry": zxAnFanTrayExMgmtEntry,
       "zxAnFanExAlarmBeepEnable": zxAnFanExAlarmBeepEnable,
       "zxAnFanExAutoSwitchByCardInstall": zxAnFanExAutoSwitchByCardInstall,
       "zxAnFanExHardwareVersion": zxAnFanExHardwareVersion,
       "zxAnFanExSoftwareVersion": zxAnFanExSoftwareVersion,
       "zxAnFanExSpeedCtrlMode": zxAnFanExSpeedCtrlMode,
       "zxAnFanExLowSpeed": zxAnFanExLowSpeed,
       "zxAnFanExStandardSpeed": zxAnFanExStandardSpeed,
       "zxAnFanExHighSpeed": zxAnFanExHighSpeed,
       "zxAnFanExSuperSpeed": zxAnFanExSuperSpeed,
       "zxAnFanExLowSpeedShiftTemp": zxAnFanExLowSpeedShiftTemp,
       "zxAnFanExStandardSpeedShiftTemp": zxAnFanExStandardSpeedShiftTemp,
       "zxAnFanExHighSpeedShiftTemp": zxAnFanExHighSpeedShiftTemp,
       "zxAnFanExSuperSpeedShiftTemp": zxAnFanExSuperSpeedShiftTemp,
       "zxAnFanExLowSpeedPercentage": zxAnFanExLowSpeedPercentage,
       "zxAnFanExStandardSpeedPercentage": zxAnFanExStandardSpeedPercentage,
       "zxAnFanExHighSpeedPercentage": zxAnFanExHighSpeedPercentage,
       "zxAnFanExSuperSpeedPercentage": zxAnFanExSuperSpeedPercentage,
       "zxAnFanExInvSn": zxAnFanExInvSn,
       "zxAnFanExMgmt": zxAnFanExMgmt,
       "zxAnFanExMgmtTable": zxAnFanExMgmtTable,
       "zxAnFanExMgmtEntry": zxAnFanExMgmtEntry,
       "zxAnFanExIndex": zxAnFanExIndex,
       "zxAnFanExConfSpeedLevel": zxAnFanExConfSpeedLevel,
       "zxAnFanExActualSpeedLevel": zxAnFanExActualSpeedLevel,
       "zxAnFanExAdminStatus": zxAnFanExAdminStatus,
       "zxAnFanExOperStatus": zxAnFanExOperStatus,
       "zxAnFanExOnlineStatus": zxAnFanExOnlineStatus,
       "zxAnFanExActualSpeed": zxAnFanExActualSpeed,
       "zxAnEquipMonitorObjects": zxAnEquipMonitorObjects,
       "zxAnCardWatchdogTable": zxAnCardWatchdogTable,
       "zxAnCardWatchdogEntry": zxAnCardWatchdogEntry,
       "zxAnCardHardwareWatchdogEnable": zxAnCardHardwareWatchdogEnable,
       "zxAnCardTaskSuspendCardResetMode": zxAnCardTaskSuspendCardResetMode,
       "zxAnCardSoftwareWatchdogEnable": zxAnCardSoftwareWatchdogEnable,
       "zxAnCardTaskDurationThreshold": zxAnCardTaskDurationThreshold,
       "zxAnCardTaskCpuUsageThreshold": zxAnCardTaskCpuUsageThreshold,
       "zxAnEquipTrapObjects": zxAnEquipTrapObjects,
       "zxAnEquipSysTrapGroup": zxAnEquipSysTrapGroup,
       "zxAnEquipCtrlCardSwapped": zxAnEquipCtrlCardSwapped,
       "zxAnEquipBackupSynchFailed": zxAnEquipBackupSynchFailed,
       "zxAnEquipCtrlCardSwapCleared": zxAnEquipCtrlCardSwapCleared,
       "zxAnEquipCardTrapGroup": zxAnEquipCardTrapGroup,
       "zxAnEquipCardUp": zxAnEquipCardUp,
       "zxAnEquipCardDown": zxAnEquipCardDown,
       "zxAnEquipCardDetectFailed": zxAnEquipCardDetectFailed,
       "zxAnEquipCardDetectSuccess": zxAnEquipCardDetectSuccess,
       "zxAnEquipCardCpuLoadAlarm": zxAnEquipCardCpuLoadAlarm,
       "zxAnEquipCardCpuLoadAlarmCleard": zxAnEquipCardCpuLoadAlarmCleard,
       "zxAnEquipCardMemoryOverLoad": zxAnEquipCardMemoryOverLoad,
       "zxAnEquipCardMemoryAlarmCleard": zxAnEquipCardMemoryAlarmCleard,
       "zxAnEquipCardUpdateVersionFailed": zxAnEquipCardUpdateVersionFailed,
       "zxAnEquipCardUpdateVerSuccess": zxAnEquipCardUpdateVerSuccess,
       "zxAnEquipCardSvcCommFailed": zxAnEquipCardSvcCommFailed,
       "zxAnEquipCardSvcCommSuccess": zxAnEquipCardSvcCommSuccess,
       "zxAnEquipCardCpldInvalid": zxAnEquipCardCpldInvalid,
       "zxAnEquipCardSwNotRunning": zxAnEquipCardSwNotRunning,
       "zxAnEquipCardSwNotRunningRestore": zxAnEquipCardSwNotRunningRestore,
       "zxAnEquipCardOffline": zxAnEquipCardOffline,
       "zxAnEquipCardOnline": zxAnEquipCardOnline,
       "zxAnEquipCardTypeMismatch": zxAnEquipCardTypeMismatch,
       "zxAnEquipCardTypeMismatchRestore": zxAnEquipCardTypeMismatchRestore,
       "zxAnEquipCardNotConfigured": zxAnEquipCardNotConfigured,
       "zxAnEquipCardConfigured": zxAnEquipCardConfigured,
       "zxAnEquipCardNotSupportedAlm": zxAnEquipCardNotSupportedAlm,
       "zxAnEquipCardNotSupportedClr": zxAnEquipCardNotSupportedClr,
       "zxAnEquipSubCardUp": zxAnEquipSubCardUp,
       "zxAnEquipSubCardDown": zxAnEquipSubCardDown,
       "zxAnEquipSubcardCpldInvalid": zxAnEquipSubcardCpldInvalid,
       "zxAnPowerSupplyCardHardwareFault": zxAnPowerSupplyCardHardwareFault,
       "zxAnEquipEnvTrapGroup": zxAnEquipEnvTrapGroup,
       "zxAnEnvTempExceededTrap": zxAnEnvTempExceededTrap,
       "zxAnEnvTempNormalTrap": zxAnEnvTempNormalTrap,
       "zxAnEnvMonitorInterfaceLinkDown": zxAnEnvMonitorInterfaceLinkDown,
       "zxAnEnvMonitorInterfaceLinkUp": zxAnEnvMonitorInterfaceLinkUp,
       "zxAnEnvFanLinkDown": zxAnEnvFanLinkDown,
       "zxAnEnvFanLinkUp": zxAnEnvFanLinkUp,
       "zxAnEnvTemperatureSensorFault": zxAnEnvTemperatureSensorFault,
       "zxAnEnvFanFault": zxAnEnvFanFault,
       "zxAnEnvFanFaultCleard": zxAnEnvFanFaultCleard,
       "zxAnEnvDustCapDown": zxAnEnvDustCapDown,
       "zxAnEnvDustCapUp": zxAnEnvDustCapUp,
       "zxAnEnvPowerSupplyDwon": zxAnEnvPowerSupplyDwon,
       "zxAnEnvPowerSupplyUp": zxAnEnvPowerSupplyUp,
       "zxAnEnvMPTempExceededTrap": zxAnEnvMPTempExceededTrap,
       "zxAnEnvMPTempNormalTrap": zxAnEnvMPTempNormalTrap,
       "zxAnEnvFanInterfaceLinkDown": zxAnEnvFanInterfaceLinkDown,
       "zxAnEnvFanInterfaceLinkUp": zxAnEnvFanInterfaceLinkUp,
       "zxAnEnvPowerOverVoltage": zxAnEnvPowerOverVoltage,
       "zxAnEnvPowerOverVoltageCleard": zxAnEnvPowerOverVoltageCleard,
       "zxAnEnvPowerUnderVoltage": zxAnEnvPowerUnderVoltage,
       "zxAnEnvPowerUnderVoltageCleard": zxAnEnvPowerUnderVoltageCleard,
       "zxAnEnvPowerOff": zxAnEnvPowerOff,
       "zxAnEnvPowerUp": zxAnEnvPowerUp,
       "zxAnEnvCardOverTemperature": zxAnEnvCardOverTemperature,
       "zxAnEnvCardOverTemperatureCleard": zxAnEnvCardOverTemperatureCleard,
       "zxAnEnvLowerFanBoardLinkDown": zxAnEnvLowerFanBoardLinkDown,
       "zxAnEnvLowerFanBoardLinkUp": zxAnEnvLowerFanBoardLinkUp,
       "zxAnEnvAcMainsPowerOff": zxAnEnvAcMainsPowerOff,
       "zxAnEnvAcMainsPowerOn": zxAnEnvAcMainsPowerOn,
       "zxAnEnvGponCardsShutdown": zxAnEnvGponCardsShutdown,
       "zxAnEnvGponCardsStartup": zxAnEnvGponCardsStartup,
       "zxAnEnvCardHighTempShutdownAlm": zxAnEnvCardHighTempShutdownAlm,
       "zxAnEnvCardHighTempShutdownClr": zxAnEnvCardHighTempShutdownClr,
       "zxAnEnvBroadbandOverheatHaltAlm": zxAnEnvBroadbandOverheatHaltAlm,
       "zxAnEnvBroadbandOverheatHaltClr": zxAnEnvBroadbandOverheatHaltClr,
       "zxAnBatteryEnergySavingBbHaltAlm": zxAnBatteryEnergySavingBbHaltAlm,
       "zxAnBatteryEnergySavingBbHaltClr": zxAnBatteryEnergySavingBbHaltClr,
       "zxAnEnvDeviceAbnormalAlm": zxAnEnvDeviceAbnormalAlm,
       "zxAnEnvDeviceAbnormalClr": zxAnEnvDeviceAbnormalClr,
       "zxAnEnvNoBatteryAlm": zxAnEnvNoBatteryAlm,
       "zxAnEnvNoBatteryClr": zxAnEnvNoBatteryClr,
       "zxAnEnvBatteryUnderVoltageAlm": zxAnEnvBatteryUnderVoltageAlm,
       "zxAnEnvBatteryUnderVoltageClr": zxAnEnvBatteryUnderVoltageClr,
       "zxAnEquipEnvExTrapGroup": zxAnEquipEnvExTrapGroup,
       "zxAnEnvExTempExceededTrap": zxAnEnvExTempExceededTrap,
       "zxAnEnvExTempNormalTrap": zxAnEnvExTempNormalTrap,
       "zxAnEnvExFanInterfaceLinkDown": zxAnEnvExFanInterfaceLinkDown,
       "zxAnEnvExFanInterfaceLinkUp": zxAnEnvExFanInterfaceLinkUp,
       "zxAnEnvExFanFault": zxAnEnvExFanFault,
       "zxAnEnvExFanFaultCleard": zxAnEnvExFanFaultCleard,
       "zxAnEquipGlobalObjects": zxAnEquipGlobalObjects,
       "zxAnEquipCapabilities": zxAnEquipCapabilities}
)
