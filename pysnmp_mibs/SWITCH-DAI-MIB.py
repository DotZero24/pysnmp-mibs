# SNMP MIB module (SWITCH-DAI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/SWITCH-DAI-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:37:21 2025
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

(rcPortEntry,) = mibBuilder.importSymbols(
    "SWITCH-SYSTEM-MIB",
    "rcPortEntry")

(EnableVar,
 PortList,
 Vlanset) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar",
    "PortList",
    "Vlanset")


# MODULE-IDENTITY

rcDai = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 38)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcDaiConfig_ObjectIdentity = ObjectIdentity
rcDaiConfig = _RcDaiConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 38, 1)
)


class _RcDaiStaticEnable_Type(EnableVar):
    """Custom type rcDaiStaticEnable based on EnableVar"""
    defaultValue = 2


_RcDaiStaticEnable_Type.__name__ = "EnableVar"
_RcDaiStaticEnable_Object = MibScalar
rcDaiStaticEnable = _RcDaiStaticEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 38, 1, 1),
    _RcDaiStaticEnable_Type()
)
rcDaiStaticEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDaiStaticEnable.setStatus("current")


class _RcDaiDhcpSnoopEnable_Type(EnableVar):
    """Custom type rcDaiDhcpSnoopEnable based on EnableVar"""
    defaultValue = 2


_RcDaiDhcpSnoopEnable_Type.__name__ = "EnableVar"
_RcDaiDhcpSnoopEnable_Object = MibScalar
rcDaiDhcpSnoopEnable = _RcDaiDhcpSnoopEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 38, 1, 2),
    _RcDaiDhcpSnoopEnable_Type()
)
rcDaiDhcpSnoopEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDaiDhcpSnoopEnable.setStatus("current")
_RcDaiBindCurrentRules_Type = Integer32
_RcDaiBindCurrentRules_Object = MibScalar
rcDaiBindCurrentRules = _RcDaiBindCurrentRules_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 38, 1, 3),
    _RcDaiBindCurrentRules_Type()
)
rcDaiBindCurrentRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDaiBindCurrentRules.setStatus("current")
_RcDaiBindMaxRules_Type = Integer32
_RcDaiBindMaxRules_Object = MibScalar
rcDaiBindMaxRules = _RcDaiBindMaxRules_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 38, 1, 4),
    _RcDaiBindMaxRules_Type()
)
rcDaiBindMaxRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDaiBindMaxRules.setStatus("current")
_RcDaiPortTrustTable_Object = MibTable
rcDaiPortTrustTable = _RcDaiPortTrustTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 38, 1, 5)
)
if mibBuilder.loadTexts:
    rcDaiPortTrustTable.setStatus("current")
_RcDaiPortTrustEntry_Object = MibTableRow
rcDaiPortTrustEntry = _RcDaiPortTrustEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 38, 1, 5, 1)
)
if mibBuilder.loadTexts:
    rcDaiPortTrustEntry.setStatus("current")


class _RcDaiTrust_Type(Integer32):
    """Custom type rcDaiTrust based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trust", 1),
          ("untrust", 2))
    )


_RcDaiTrust_Type.__name__ = "Integer32"
_RcDaiTrust_Object = MibTableColumn
rcDaiTrust = _RcDaiTrust_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 38, 1, 5, 1, 1),
    _RcDaiTrust_Type()
)
rcDaiTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDaiTrust.setStatus("current")
_RcDaiBindTable_Object = MibTable
rcDaiBindTable = _RcDaiBindTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 38, 1, 6)
)
if mibBuilder.loadTexts:
    rcDaiBindTable.setStatus("current")
_RcDaiBindEntry_Object = MibTableRow
rcDaiBindEntry = _RcDaiBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 38, 1, 6, 1)
)
rcDaiBindEntry.setIndexNames(
    (0, "SWITCH-DAI-MIB", "rcDaiBindIp"),
)
if mibBuilder.loadTexts:
    rcDaiBindEntry.setStatus("current")
_RcDaiBindIp_Type = IpAddress
_RcDaiBindIp_Object = MibTableColumn
rcDaiBindIp = _RcDaiBindIp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 38, 1, 6, 1, 1),
    _RcDaiBindIp_Type()
)
rcDaiBindIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcDaiBindIp.setStatus("current")
_RcDaiBindPortId_Type = Integer32
_RcDaiBindPortId_Object = MibTableColumn
rcDaiBindPortId = _RcDaiBindPortId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 38, 1, 6, 1, 2),
    _RcDaiBindPortId_Type()
)
rcDaiBindPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDaiBindPortId.setStatus("current")
_RcDaiBindMac_Type = MacAddress
_RcDaiBindMac_Object = MibTableColumn
rcDaiBindMac = _RcDaiBindMac_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 38, 1, 6, 1, 3),
    _RcDaiBindMac_Type()
)
rcDaiBindMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDaiBindMac.setStatus("current")


class _RcDaiBindVlan_Type(Integer32):
    """Custom type rcDaiBindVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RcDaiBindVlan_Type.__name__ = "Integer32"
_RcDaiBindVlan_Object = MibTableColumn
rcDaiBindVlan = _RcDaiBindVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 38, 1, 6, 1, 4),
    _RcDaiBindVlan_Type()
)
rcDaiBindVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDaiBindVlan.setStatus("current")


class _RcDaiBindMode_Type(Integer32):
    """Custom type rcDaiBindMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dhcp-snooping", 2))
    )


_RcDaiBindMode_Type.__name__ = "Integer32"
_RcDaiBindMode_Object = MibTableColumn
rcDaiBindMode = _RcDaiBindMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 38, 1, 6, 1, 5),
    _RcDaiBindMode_Type()
)
rcDaiBindMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDaiBindMode.setStatus("current")


class _RcDaiBindInHw_Type(Integer32):
    """Custom type rcDaiBindInHw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inHw", 1),
          ("notinHw", 2))
    )


_RcDaiBindInHw_Type.__name__ = "Integer32"
_RcDaiBindInHw_Object = MibTableColumn
rcDaiBindInHw = _RcDaiBindInHw_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 38, 1, 6, 1, 6),
    _RcDaiBindInHw_Type()
)
rcDaiBindInHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDaiBindInHw.setStatus("current")
_RcDaiBindRowStatus_Type = RowStatus
_RcDaiBindRowStatus_Object = MibTableColumn
rcDaiBindRowStatus = _RcDaiBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 38, 1, 6, 1, 7),
    _RcDaiBindRowStatus_Type()
)
rcDaiBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDaiBindRowStatus.setStatus("current")
_RcArpRLPortEnableTable_Object = MibTable
rcArpRLPortEnableTable = _RcArpRLPortEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 38, 1, 7)
)
if mibBuilder.loadTexts:
    rcArpRLPortEnableTable.setStatus("current")
_RcArpRLPortEnableEntry_Object = MibTableRow
rcArpRLPortEnableEntry = _RcArpRLPortEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 38, 1, 7, 1)
)
if mibBuilder.loadTexts:
    rcArpRLPortEnableEntry.setStatus("current")


class _RcArpRLEnable_Type(EnableVar):
    """Custom type rcArpRLEnable based on EnableVar"""
    defaultValue = 2


_RcArpRLEnable_Type.__name__ = "EnableVar"
_RcArpRLEnable_Object = MibTableColumn
rcArpRLEnable = _RcArpRLEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 38, 1, 7, 1, 1),
    _RcArpRLEnable_Type()
)
rcArpRLEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcArpRLEnable.setStatus("current")
_RcArpRLPortRateTable_Object = MibTable
rcArpRLPortRateTable = _RcArpRLPortRateTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 38, 1, 8)
)
if mibBuilder.loadTexts:
    rcArpRLPortRateTable.setStatus("current")
_RcArpRLPortRateEntry_Object = MibTableRow
rcArpRLPortRateEntry = _RcArpRLPortRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 38, 1, 8, 1)
)
if mibBuilder.loadTexts:
    rcArpRLPortRateEntry.setStatus("current")


class _RcArpRLRate_Type(Integer32):
    """Custom type rcArpRLRate based on Integer32"""
    defaultValue = 100


_RcArpRLRate_Type.__name__ = "Integer32"
_RcArpRLRate_Object = MibTableColumn
rcArpRLRate = _RcArpRLRate_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 38, 1, 8, 1, 1),
    _RcArpRLRate_Type()
)
rcArpRLRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcArpRLRate.setStatus("current")
_RcArpRLPortStatusTable_Object = MibTable
rcArpRLPortStatusTable = _RcArpRLPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 38, 1, 9)
)
if mibBuilder.loadTexts:
    rcArpRLPortStatusTable.setStatus("current")
_RcArpRLPortStatusEntry_Object = MibTableRow
rcArpRLPortStatusEntry = _RcArpRLPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 38, 1, 9, 1)
)
if mibBuilder.loadTexts:
    rcArpRLPortStatusEntry.setStatus("current")


class _RcArpRLStatus_Type(Integer32):
    """Custom type rcArpRLStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unoverload", 0),
          ("overload", 1))
    )


_RcArpRLStatus_Type.__name__ = "Integer32"
_RcArpRLStatus_Object = MibTableColumn
rcArpRLStatus = _RcArpRLStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 38, 1, 9, 1, 1),
    _RcArpRLStatus_Type()
)
rcArpRLStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcArpRLStatus.setStatus("current")


class _RcArpRLRecoverEnable_Type(EnableVar):
    """Custom type rcArpRLRecoverEnable based on EnableVar"""
    defaultValue = 2


_RcArpRLRecoverEnable_Type.__name__ = "EnableVar"
_RcArpRLRecoverEnable_Object = MibScalar
rcArpRLRecoverEnable = _RcArpRLRecoverEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 38, 1, 10),
    _RcArpRLRecoverEnable_Type()
)
rcArpRLRecoverEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcArpRLRecoverEnable.setStatus("current")


class _RcArpRLRecoverTime_Type(Integer32):
    """Custom type rcArpRLRecoverTime based on Integer32"""
    defaultValue = 30


_RcArpRLRecoverTime_Type.__name__ = "Integer32"
_RcArpRLRecoverTime_Object = MibScalar
rcArpRLRecoverTime = _RcArpRLRecoverTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 38, 1, 11),
    _RcArpRLRecoverTime_Type()
)
rcArpRLRecoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcArpRLRecoverTime.setStatus("current")


class _RcDaiIsVlanAll_Type(EnableVar):
    """Custom type rcDaiIsVlanAll based on EnableVar"""
    defaultValue = 2


_RcDaiIsVlanAll_Type.__name__ = "EnableVar"
_RcDaiIsVlanAll_Object = MibScalar
rcDaiIsVlanAll = _RcDaiIsVlanAll_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 38, 1, 12),
    _RcDaiIsVlanAll_Type()
)
rcDaiIsVlanAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDaiIsVlanAll.setStatus("current")
_RcDaiProtectVlanList_Type = Vlanset
_RcDaiProtectVlanList_Object = MibScalar
rcDaiProtectVlanList = _RcDaiProtectVlanList_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 38, 1, 13),
    _RcDaiProtectVlanList_Type()
)
rcDaiProtectVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDaiProtectVlanList.setStatus("current")
rcPortEntry.registerAugmentions(
    ("SWITCH-DAI-MIB",
     "rcDaiPortTrustEntry")
)
rcDaiPortTrustEntry.setIndexNames(*rcPortEntry.getIndexNames())
rcPortEntry.registerAugmentions(
    ("SWITCH-DAI-MIB",
     "rcArpRLPortEnableEntry")
)
rcArpRLPortEnableEntry.setIndexNames(*rcPortEntry.getIndexNames())
rcPortEntry.registerAugmentions(
    ("SWITCH-DAI-MIB",
     "rcArpRLPortRateEntry")
)
rcArpRLPortRateEntry.setIndexNames(*rcPortEntry.getIndexNames())
rcPortEntry.registerAugmentions(
    ("SWITCH-DAI-MIB",
     "rcArpRLPortStatusEntry")
)
rcArpRLPortStatusEntry.setIndexNames(*rcPortEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWITCH-DAI-MIB",
    **{"rcDai": rcDai,
       "rcDaiConfig": rcDaiConfig,
       "rcDaiStaticEnable": rcDaiStaticEnable,
       "rcDaiDhcpSnoopEnable": rcDaiDhcpSnoopEnable,
       "rcDaiBindCurrentRules": rcDaiBindCurrentRules,
       "rcDaiBindMaxRules": rcDaiBindMaxRules,
       "rcDaiPortTrustTable": rcDaiPortTrustTable,
       "rcDaiPortTrustEntry": rcDaiPortTrustEntry,
       "rcDaiTrust": rcDaiTrust,
       "rcDaiBindTable": rcDaiBindTable,
       "rcDaiBindEntry": rcDaiBindEntry,
       "rcDaiBindIp": rcDaiBindIp,
       "rcDaiBindPortId": rcDaiBindPortId,
       "rcDaiBindMac": rcDaiBindMac,
       "rcDaiBindVlan": rcDaiBindVlan,
       "rcDaiBindMode": rcDaiBindMode,
       "rcDaiBindInHw": rcDaiBindInHw,
       "rcDaiBindRowStatus": rcDaiBindRowStatus,
       "rcArpRLPortEnableTable": rcArpRLPortEnableTable,
       "rcArpRLPortEnableEntry": rcArpRLPortEnableEntry,
       "rcArpRLEnable": rcArpRLEnable,
       "rcArpRLPortRateTable": rcArpRLPortRateTable,
       "rcArpRLPortRateEntry": rcArpRLPortRateEntry,
       "rcArpRLRate": rcArpRLRate,
       "rcArpRLPortStatusTable": rcArpRLPortStatusTable,
       "rcArpRLPortStatusEntry": rcArpRLPortStatusEntry,
       "rcArpRLStatus": rcArpRLStatus,
       "rcArpRLRecoverEnable": rcArpRLRecoverEnable,
       "rcArpRLRecoverTime": rcArpRLRecoverTime,
       "rcDaiIsVlanAll": rcDaiIsVlanAll,
       "rcDaiProtectVlanList": rcDaiProtectVlanList}
)
