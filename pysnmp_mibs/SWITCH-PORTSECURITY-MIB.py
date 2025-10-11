# SNMP MIB module (SWITCH-PORTSECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/SWITCH-PORTSECURITY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:41 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(EnableVar,) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar")


# MODULE-IDENTITY

rcPortsecurity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 49)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcPortSecCfg_ObjectIdentity = ObjectIdentity
rcPortSecCfg = _RcPortSecCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 49, 1)
)


class _RcPortSecMacAgingTime_Type(Integer32):
    """Custom type rcPortSecMacAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_RcPortSecMacAgingTime_Type.__name__ = "Integer32"
_RcPortSecMacAgingTime_Object = MibScalar
rcPortSecMacAgingTime = _RcPortSecMacAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 49, 1, 1),
    _RcPortSecMacAgingTime_Type()
)
rcPortSecMacAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPortSecMacAgingTime.setStatus("current")
_RcPortSecTable_Object = MibTable
rcPortSecTable = _RcPortSecTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 49, 2)
)
if mibBuilder.loadTexts:
    rcPortSecTable.setStatus("current")
_RcPortSecEntry_Object = MibTableRow
rcPortSecEntry = _RcPortSecEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 49, 2, 1)
)
rcPortSecEntry.setIndexNames(
    (0, "SWITCH-PORTSECURITY-MIB", "rcPortSecIndx"),
)
if mibBuilder.loadTexts:
    rcPortSecEntry.setStatus("current")
_RcPortSecIndx_Type = Integer32
_RcPortSecIndx_Object = MibTableColumn
rcPortSecIndx = _RcPortSecIndx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 49, 2, 1, 1),
    _RcPortSecIndx_Type()
)
rcPortSecIndx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcPortSecIndx.setStatus("current")
_RcPortSecEnable_Type = EnableVar
_RcPortSecEnable_Object = MibTableColumn
rcPortSecEnable = _RcPortSecEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 49, 2, 1, 2),
    _RcPortSecEnable_Type()
)
rcPortSecEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPortSecEnable.setStatus("current")


class _RcPortSecMaxAllowedMac_Type(Integer32):
    """Custom type rcPortSecMaxAllowedMac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RcPortSecMaxAllowedMac_Type.__name__ = "Integer32"
_RcPortSecMaxAllowedMac_Object = MibTableColumn
rcPortSecMaxAllowedMac = _RcPortSecMaxAllowedMac_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 49, 2, 1, 3),
    _RcPortSecMaxAllowedMac_Type()
)
rcPortSecMaxAllowedMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPortSecMaxAllowedMac.setStatus("current")


class _RcPortSecMacViolationAction_Type(Integer32):
    """Custom type rcPortSecMacViolationAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_RcPortSecMacViolationAction_Type.__name__ = "Integer32"
_RcPortSecMacViolationAction_Object = MibTableColumn
rcPortSecMacViolationAction = _RcPortSecMacViolationAction_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 49, 2, 1, 4),
    _RcPortSecMacViolationAction_Type()
)
rcPortSecMacViolationAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPortSecMacViolationAction.setStatus("current")


class _RcPortSecShutUp_Type(Integer32):
    """Custom type rcPortSecShutUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RcPortSecShutUp_Type.__name__ = "Integer32"
_RcPortSecShutUp_Object = MibTableColumn
rcPortSecShutUp = _RcPortSecShutUp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 49, 2, 1, 5),
    _RcPortSecShutUp_Type()
)
rcPortSecShutUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPortSecShutUp.setStatus("current")
_RcPortSecMacStickyEnable_Type = EnableVar
_RcPortSecMacStickyEnable_Object = MibTableColumn
rcPortSecMacStickyEnable = _RcPortSecMacStickyEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 49, 2, 1, 6),
    _RcPortSecMacStickyEnable_Type()
)
rcPortSecMacStickyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPortSecMacStickyEnable.setStatus("current")
_RcPortSecTrapEnable_Type = EnableVar
_RcPortSecTrapEnable_Object = MibTableColumn
rcPortSecTrapEnable = _RcPortSecTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 49, 2, 1, 7),
    _RcPortSecTrapEnable_Type()
)
rcPortSecTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPortSecTrapEnable.setStatus("current")


class _RcPortSecMacDel_Type(Integer32):
    """Custom type rcPortSecMacDel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_RcPortSecMacDel_Type.__name__ = "Integer32"
_RcPortSecMacDel_Object = MibTableColumn
rcPortSecMacDel = _RcPortSecMacDel_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 49, 2, 1, 8),
    _RcPortSecMacDel_Type()
)
rcPortSecMacDel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPortSecMacDel.setStatus("current")


class _RcPortSecCurMacNum_Type(Integer32):
    """Custom type rcPortSecCurMacNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RcPortSecCurMacNum_Type.__name__ = "Integer32"
_RcPortSecCurMacNum_Object = MibTableColumn
rcPortSecCurMacNum = _RcPortSecCurMacNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 49, 2, 1, 9),
    _RcPortSecCurMacNum_Type()
)
rcPortSecCurMacNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPortSecCurMacNum.setStatus("current")


class _RcPortSecMaxMacs_Type(Integer32):
    """Custom type rcPortSecMaxMacs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RcPortSecMaxMacs_Type.__name__ = "Integer32"
_RcPortSecMaxMacs_Object = MibTableColumn
rcPortSecMaxMacs = _RcPortSecMaxMacs_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 49, 2, 1, 10),
    _RcPortSecMaxMacs_Type()
)
rcPortSecMaxMacs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPortSecMaxMacs.setStatus("current")


class _RcPortSecMacViolations_Type(Integer32):
    """Custom type rcPortSecMacViolations based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RcPortSecMacViolations_Type.__name__ = "Integer32"
_RcPortSecMacViolations_Object = MibTableColumn
rcPortSecMacViolations = _RcPortSecMacViolations_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 49, 2, 1, 11),
    _RcPortSecMacViolations_Type()
)
rcPortSecMacViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPortSecMacViolations.setStatus("current")


class _RcPortSecViolationStatus_Type(Integer32):
    """Custom type rcPortSecViolationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RcPortSecViolationStatus_Type.__name__ = "Integer32"
_RcPortSecViolationStatus_Object = MibTableColumn
rcPortSecViolationStatus = _RcPortSecViolationStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 49, 2, 1, 12),
    _RcPortSecViolationStatus_Type()
)
rcPortSecViolationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPortSecViolationStatus.setStatus("current")
_RcPortSecLastAccessMacAddress_Type = MacAddress
_RcPortSecLastAccessMacAddress_Object = MibTableColumn
rcPortSecLastAccessMacAddress = _RcPortSecLastAccessMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 49, 2, 1, 13),
    _RcPortSecLastAccessMacAddress_Type()
)
rcPortSecLastAccessMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPortSecLastAccessMacAddress.setStatus("current")


class _RcPortSecLastAccessMacVlan_Type(Integer32):
    """Custom type rcPortSecLastAccessMacVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RcPortSecLastAccessMacVlan_Type.__name__ = "Integer32"
_RcPortSecLastAccessMacVlan_Object = MibTableColumn
rcPortSecLastAccessMacVlan = _RcPortSecLastAccessMacVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 49, 2, 1, 14),
    _RcPortSecLastAccessMacVlan_Type()
)
rcPortSecLastAccessMacVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPortSecLastAccessMacVlan.setStatus("current")
_RcPortSecLastAgingMacAddress_Type = MacAddress
_RcPortSecLastAgingMacAddress_Object = MibTableColumn
rcPortSecLastAgingMacAddress = _RcPortSecLastAgingMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 49, 2, 1, 15),
    _RcPortSecLastAgingMacAddress_Type()
)
rcPortSecLastAgingMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPortSecLastAgingMacAddress.setStatus("current")


class _RcPortSecLastAgingMacVlan_Type(Integer32):
    """Custom type rcPortSecLastAgingMacVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RcPortSecLastAgingMacVlan_Type.__name__ = "Integer32"
_RcPortSecLastAgingMacVlan_Object = MibTableColumn
rcPortSecLastAgingMacVlan = _RcPortSecLastAgingMacVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 49, 2, 1, 16),
    _RcPortSecLastAgingMacVlan_Type()
)
rcPortSecLastAgingMacVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPortSecLastAgingMacVlan.setStatus("current")
_RcPortSecLastDelMacAddress_Type = MacAddress
_RcPortSecLastDelMacAddress_Object = MibTableColumn
rcPortSecLastDelMacAddress = _RcPortSecLastDelMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 49, 2, 1, 17),
    _RcPortSecLastDelMacAddress_Type()
)
rcPortSecLastDelMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPortSecLastDelMacAddress.setStatus("current")


class _RcPortSecLastDelMacVlan_Type(Integer32):
    """Custom type rcPortSecLastDelMacVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RcPortSecLastDelMacVlan_Type.__name__ = "Integer32"
_RcPortSecLastDelMacVlan_Object = MibTableColumn
rcPortSecLastDelMacVlan = _RcPortSecLastDelMacVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 49, 2, 1, 18),
    _RcPortSecLastDelMacVlan_Type()
)
rcPortSecLastDelMacVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPortSecLastDelMacVlan.setStatus("current")


class _RcPortSecLastDelMacFlag_Type(Integer32):
    """Custom type rcPortSecLastDelMacFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2),
          ("sticky", 3))
    )


_RcPortSecLastDelMacFlag_Type.__name__ = "Integer32"
_RcPortSecLastDelMacFlag_Object = MibTableColumn
rcPortSecLastDelMacFlag = _RcPortSecLastDelMacFlag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 49, 2, 1, 19),
    _RcPortSecLastDelMacFlag_Type()
)
rcPortSecLastDelMacFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPortSecLastDelMacFlag.setStatus("current")
_RcPortSecMacTable_Object = MibTable
rcPortSecMacTable = _RcPortSecMacTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 49, 3)
)
if mibBuilder.loadTexts:
    rcPortSecMacTable.setStatus("current")
_RcPortSecMacEntry_Object = MibTableRow
rcPortSecMacEntry = _RcPortSecMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 49, 3, 1)
)
rcPortSecMacEntry.setIndexNames(
    (0, "SWITCH-PORTSECURITY-MIB", "rcPortSecVlan"),
    (0, "SWITCH-PORTSECURITY-MIB", "rcPortSecMac"),
)
if mibBuilder.loadTexts:
    rcPortSecMacEntry.setStatus("current")


class _RcPortSecVlan_Type(Integer32):
    """Custom type rcPortSecVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RcPortSecVlan_Type.__name__ = "Integer32"
_RcPortSecVlan_Object = MibTableColumn
rcPortSecVlan = _RcPortSecVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 49, 3, 1, 1),
    _RcPortSecVlan_Type()
)
rcPortSecVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPortSecVlan.setStatus("current")
_RcPortSecMac_Type = MacAddress
_RcPortSecMac_Object = MibTableColumn
rcPortSecMac = _RcPortSecMac_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 49, 3, 1, 2),
    _RcPortSecMac_Type()
)
rcPortSecMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPortSecMac.setStatus("current")
_RcPortSecPort_Type = Integer32
_RcPortSecPort_Object = MibTableColumn
rcPortSecPort = _RcPortSecPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 49, 3, 1, 3),
    _RcPortSecPort_Type()
)
rcPortSecPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcPortSecPort.setStatus("current")


class _RcPortSecFlag_Type(Integer32):
    """Custom type rcPortSecFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2),
          ("sticky", 3))
    )


_RcPortSecFlag_Type.__name__ = "Integer32"
_RcPortSecFlag_Object = MibTableColumn
rcPortSecFlag = _RcPortSecFlag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 49, 3, 1, 4),
    _RcPortSecFlag_Type()
)
rcPortSecFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcPortSecFlag.setStatus("current")


class _RcPortSecAgingTm_Type(Integer32):
    """Custom type rcPortSecAgingTm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_RcPortSecAgingTm_Type.__name__ = "Integer32"
_RcPortSecAgingTm_Object = MibTableColumn
rcPortSecAgingTm = _RcPortSecAgingTm_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 49, 3, 1, 5),
    _RcPortSecAgingTm_Type()
)
rcPortSecAgingTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPortSecAgingTm.setStatus("current")
_RcPortSecRowStatus_Type = RowStatus
_RcPortSecRowStatus_Object = MibTableColumn
rcPortSecRowStatus = _RcPortSecRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 49, 3, 1, 6),
    _RcPortSecRowStatus_Type()
)
rcPortSecRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcPortSecRowStatus.setStatus("current")
_RcPortSecTrapGroup_ObjectIdentity = ObjectIdentity
rcPortSecTrapGroup = _RcPortSecTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 49, 4)
)

# Managed Objects groups


# Notification objects

rcPortSecLearningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 49, 4, 1)
)
rcPortSecLearningTrap.setObjects(
      *(("SWITCH-PORTSECURITY-MIB", "rcPortSecVlan"),
        ("SWITCH-PORTSECURITY-MIB", "rcPortSecMac"),
        ("SWITCH-PORTSECURITY-MIB", "rcPortSecPort"),
        ("SWITCH-PORTSECURITY-MIB", "rcPortSecFlag"))
)
if mibBuilder.loadTexts:
    rcPortSecLearningTrap.setStatus(
        "current"
    )

rcPortSecViolationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 49, 4, 2)
)
rcPortSecViolationTrap.setObjects(
      *(("SWITCH-PORTSECURITY-MIB", "rcPortSecLastAccessMacAddress"),
        ("SWITCH-PORTSECURITY-MIB", "rcPortSecLastAccessMacVlan"))
)
if mibBuilder.loadTexts:
    rcPortSecViolationTrap.setStatus(
        "current"
    )

rcPortSecAgingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 49, 4, 3)
)
rcPortSecAgingTrap.setObjects(
      *(("SWITCH-PORTSECURITY-MIB", "rcPortSecLastAgingMacAddress"),
        ("SWITCH-PORTSECURITY-MIB", "rcPortSecLastAgingMacVlan"))
)
if mibBuilder.loadTexts:
    rcPortSecAgingTrap.setStatus(
        "current"
    )

rcPortSecDelTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 49, 4, 4)
)
rcPortSecDelTrap.setObjects(
      *(("SWITCH-PORTSECURITY-MIB", "rcPortSecLastDelMacAddress"),
        ("SWITCH-PORTSECURITY-MIB", "rcPortSecLastDelMacVlan"),
        ("SWITCH-PORTSECURITY-MIB", "rcPortSecLastDelMacFlag"))
)
if mibBuilder.loadTexts:
    rcPortSecDelTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWITCH-PORTSECURITY-MIB",
    **{"rcPortsecurity": rcPortsecurity,
       "rcPortSecCfg": rcPortSecCfg,
       "rcPortSecMacAgingTime": rcPortSecMacAgingTime,
       "rcPortSecTable": rcPortSecTable,
       "rcPortSecEntry": rcPortSecEntry,
       "rcPortSecIndx": rcPortSecIndx,
       "rcPortSecEnable": rcPortSecEnable,
       "rcPortSecMaxAllowedMac": rcPortSecMaxAllowedMac,
       "rcPortSecMacViolationAction": rcPortSecMacViolationAction,
       "rcPortSecShutUp": rcPortSecShutUp,
       "rcPortSecMacStickyEnable": rcPortSecMacStickyEnable,
       "rcPortSecTrapEnable": rcPortSecTrapEnable,
       "rcPortSecMacDel": rcPortSecMacDel,
       "rcPortSecCurMacNum": rcPortSecCurMacNum,
       "rcPortSecMaxMacs": rcPortSecMaxMacs,
       "rcPortSecMacViolations": rcPortSecMacViolations,
       "rcPortSecViolationStatus": rcPortSecViolationStatus,
       "rcPortSecLastAccessMacAddress": rcPortSecLastAccessMacAddress,
       "rcPortSecLastAccessMacVlan": rcPortSecLastAccessMacVlan,
       "rcPortSecLastAgingMacAddress": rcPortSecLastAgingMacAddress,
       "rcPortSecLastAgingMacVlan": rcPortSecLastAgingMacVlan,
       "rcPortSecLastDelMacAddress": rcPortSecLastDelMacAddress,
       "rcPortSecLastDelMacVlan": rcPortSecLastDelMacVlan,
       "rcPortSecLastDelMacFlag": rcPortSecLastDelMacFlag,
       "rcPortSecMacTable": rcPortSecMacTable,
       "rcPortSecMacEntry": rcPortSecMacEntry,
       "rcPortSecVlan": rcPortSecVlan,
       "rcPortSecMac": rcPortSecMac,
       "rcPortSecPort": rcPortSecPort,
       "rcPortSecFlag": rcPortSecFlag,
       "rcPortSecAgingTm": rcPortSecAgingTm,
       "rcPortSecRowStatus": rcPortSecRowStatus,
       "rcPortSecTrapGroup": rcPortSecTrapGroup,
       "rcPortSecLearningTrap": rcPortSecLearningTrap,
       "rcPortSecViolationTrap": rcPortSecViolationTrap,
       "rcPortSecAgingTrap": rcPortSecAgingTrap,
       "rcPortSecDelTrap": rcPortSecDelTrap}
)
