# SNMP MIB module (CONVERTOR-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/CONVERTOR-SYSTEM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:37:18 2025
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

(iscomMediaConvertor,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "iscomMediaConvertor")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(EnableVar,
 PortList) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar",
    "PortList")


# MODULE-IDENTITY

rcmcSystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 16, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcmcOamConfig_ObjectIdentity = ObjectIdentity
rcmcOamConfig = _RcmcOamConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 16, 1, 1, 1)
)
_RcmcOamEnable_Type = EnableVar
_RcmcOamEnable_Object = MibScalar
rcmcOamEnable = _RcmcOamEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 16, 1, 1, 1, 1),
    _RcmcOamEnable_Type()
)
rcmcOamEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcmcOamEnable.setStatus("current")


class _RcmcOamWorkMode_Type(Integer32):
    """Custom type rcmcOamWorkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("masterCtrl", 1),
          ("slaveCtrl", 2))
    )


_RcmcOamWorkMode_Type.__name__ = "Integer32"
_RcmcOamWorkMode_Object = MibScalar
rcmcOamWorkMode = _RcmcOamWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 16, 1, 1, 1, 2),
    _RcmcOamWorkMode_Type()
)
rcmcOamWorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcmcOamWorkMode.setStatus("current")
_RcmcOamConfigTrap_ObjectIdentity = ObjectIdentity
rcmcOamConfigTrap = _RcmcOamConfigTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 16, 1, 1, 1, 3)
)
_RcmcPortInfoConfig_ObjectIdentity = ObjectIdentity
rcmcPortInfoConfig = _RcmcPortInfoConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 16, 1, 1, 2)
)
_RcmcPortTable_Object = MibTable
rcmcPortTable = _RcmcPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 16, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    rcmcPortTable.setStatus("current")
_RcmcPortEntry_Object = MibTableRow
rcmcPortEntry = _RcmcPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 16, 1, 1, 2, 1, 1)
)
rcmcPortEntry.setIndexNames(
    (0, "CONVERTOR-SYSTEM-MIB", "rcmcPortIndex"),
)
if mibBuilder.loadTexts:
    rcmcPortEntry.setStatus("current")
_RcmcPortIndex_Type = Integer32
_RcmcPortIndex_Object = MibTableColumn
rcmcPortIndex = _RcmcPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 16, 1, 1, 2, 1, 1, 1),
    _RcmcPortIndex_Type()
)
rcmcPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcmcPortIndex.setStatus("current")


class _RcmcPortOptModuleType_Type(Integer32):
    """Custom type rcmcPortOptModuleType based on Integer32"""
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
        *(("optical-M", 1),
          ("optical-S1", 2),
          ("optical-S2", 3),
          ("optical-S3", 4),
          ("optical-SS13", 5),
          ("optical-SS15", 6),
          ("optical-SS23", 7),
          ("optical-SS25", 8),
          ("optical-SS35", 9),
          ("unknown", 10))
    )


_RcmcPortOptModuleType_Type.__name__ = "Integer32"
_RcmcPortOptModuleType_Object = MibTableColumn
rcmcPortOptModuleType = _RcmcPortOptModuleType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 16, 1, 1, 2, 1, 1, 2),
    _RcmcPortOptModuleType_Type()
)
rcmcPortOptModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcmcPortOptModuleType.setStatus("current")


class _RcmcPortFaultPassEnable_Type(EnableVar):
    """Custom type rcmcPortFaultPassEnable based on EnableVar"""
    defaultValue = 2


_RcmcPortFaultPassEnable_Type.__name__ = "EnableVar"
_RcmcPortFaultPassEnable_Object = MibTableColumn
rcmcPortFaultPassEnable = _RcmcPortFaultPassEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 16, 1, 1, 2, 1, 1, 3),
    _RcmcPortFaultPassEnable_Type()
)
rcmcPortFaultPassEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcmcPortFaultPassEnable.setStatus("current")


class _RcmcPortFaultPassStatus_Type(Integer32):
    """Custom type rcmcPortFaultPassStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("down", 2))
    )


_RcmcPortFaultPassStatus_Type.__name__ = "Integer32"
_RcmcPortFaultPassStatus_Object = MibTableColumn
rcmcPortFaultPassStatus = _RcmcPortFaultPassStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 16, 1, 1, 2, 1, 1, 4),
    _RcmcPortFaultPassStatus_Type()
)
rcmcPortFaultPassStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcmcPortFaultPassStatus.setStatus("current")


class _RcmcPortSD_Type(Integer32):
    """Custom type rcmcPortSD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("sd", 2),
          ("unavailable", 3))
    )


_RcmcPortSD_Type.__name__ = "Integer32"
_RcmcPortSD_Object = MibTableColumn
rcmcPortSD = _RcmcPortSD_Object(
    (1, 3, 6, 1, 4, 1, 8886, 16, 1, 1, 2, 1, 1, 5),
    _RcmcPortSD_Type()
)
rcmcPortSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcmcPortSD.setStatus("current")


class _RcmcPortFaultReturnEnable_Type(Integer32):
    """Custom type rcmcPortFaultReturnEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("unavailable", 3))
    )


_RcmcPortFaultReturnEnable_Type.__name__ = "Integer32"
_RcmcPortFaultReturnEnable_Object = MibTableColumn
rcmcPortFaultReturnEnable = _RcmcPortFaultReturnEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 16, 1, 1, 2, 1, 1, 6),
    _RcmcPortFaultReturnEnable_Type()
)
rcmcPortFaultReturnEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcmcPortFaultReturnEnable.setStatus("current")


class _RcmcPortFaultReturnStatus_Type(Integer32):
    """Custom type rcmcPortFaultReturnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("down", 2),
          ("unavailable", 3))
    )


_RcmcPortFaultReturnStatus_Type.__name__ = "Integer32"
_RcmcPortFaultReturnStatus_Object = MibTableColumn
rcmcPortFaultReturnStatus = _RcmcPortFaultReturnStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 16, 1, 1, 2, 1, 1, 7),
    _RcmcPortFaultReturnStatus_Type()
)
rcmcPortFaultReturnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcmcPortFaultReturnStatus.setStatus("current")


class _RcmcPortFefi_Type(Integer32):
    """Custom type rcmcPortFefi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("fefi", 2),
          ("unavailable", 3))
    )


_RcmcPortFefi_Type.__name__ = "Integer32"
_RcmcPortFefi_Object = MibTableColumn
rcmcPortFefi = _RcmcPortFefi_Object(
    (1, 3, 6, 1, 4, 1, 8886, 16, 1, 1, 2, 1, 1, 8),
    _RcmcPortFefi_Type()
)
rcmcPortFefi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcmcPortFefi.setStatus("current")
_RcmcPortFPToPorts_Type = PortList
_RcmcPortFPToPorts_Object = MibTableColumn
rcmcPortFPToPorts = _RcmcPortFPToPorts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 16, 1, 1, 2, 1, 1, 9),
    _RcmcPortFPToPorts_Type()
)
rcmcPortFPToPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcmcPortFPToPorts.setStatus("current")
_RcmcPortInfoTrap_ObjectIdentity = ObjectIdentity
rcmcPortInfoTrap = _RcmcPortInfoTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 16, 1, 1, 2, 2)
)

# Managed Objects groups


# Notification objects

rcmcOamRemoteLostTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 16, 1, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    rcmcOamRemoteLostTrap.setStatus(
        "current"
    )

rcmcOamRemoteRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 16, 1, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    rcmcOamRemoteRecoverTrap.setStatus(
        "current"
    )

rcmcPortFaultPassTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 16, 1, 1, 2, 2, 1)
)
rcmcPortFaultPassTrap.setObjects(
      *(("CONVERTOR-SYSTEM-MIB", "rcmcPortIndex"),
        ("CONVERTOR-SYSTEM-MIB", "rcmcPortFaultPassStatus"))
)
if mibBuilder.loadTexts:
    rcmcPortFaultPassTrap.setStatus(
        "current"
    )

rcmcPortFaultReturnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 16, 1, 1, 2, 2, 2)
)
rcmcPortFaultReturnTrap.setObjects(
      *(("CONVERTOR-SYSTEM-MIB", "rcmcPortIndex"),
        ("CONVERTOR-SYSTEM-MIB", "rcmcPortFaultReturnStatus"))
)
if mibBuilder.loadTexts:
    rcmcPortFaultReturnTrap.setStatus(
        "current"
    )

rcmcPortFefiTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 16, 1, 1, 2, 2, 3)
)
rcmcPortFefiTrap.setObjects(
      *(("CONVERTOR-SYSTEM-MIB", "rcmcPortIndex"),
        ("CONVERTOR-SYSTEM-MIB", "rcmcPortFefi"))
)
if mibBuilder.loadTexts:
    rcmcPortFefiTrap.setStatus(
        "current"
    )

rcmcPortSDTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 16, 1, 1, 2, 2, 4)
)
rcmcPortSDTrap.setObjects(
      *(("CONVERTOR-SYSTEM-MIB", "rcmcPortIndex"),
        ("CONVERTOR-SYSTEM-MIB", "rcmcPortSD"))
)
if mibBuilder.loadTexts:
    rcmcPortSDTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CONVERTOR-SYSTEM-MIB",
    **{"rcmcSystem": rcmcSystem,
       "rcmcOamConfig": rcmcOamConfig,
       "rcmcOamEnable": rcmcOamEnable,
       "rcmcOamWorkMode": rcmcOamWorkMode,
       "rcmcOamConfigTrap": rcmcOamConfigTrap,
       "rcmcOamRemoteLostTrap": rcmcOamRemoteLostTrap,
       "rcmcOamRemoteRecoverTrap": rcmcOamRemoteRecoverTrap,
       "rcmcPortInfoConfig": rcmcPortInfoConfig,
       "rcmcPortTable": rcmcPortTable,
       "rcmcPortEntry": rcmcPortEntry,
       "rcmcPortIndex": rcmcPortIndex,
       "rcmcPortOptModuleType": rcmcPortOptModuleType,
       "rcmcPortFaultPassEnable": rcmcPortFaultPassEnable,
       "rcmcPortFaultPassStatus": rcmcPortFaultPassStatus,
       "rcmcPortSD": rcmcPortSD,
       "rcmcPortFaultReturnEnable": rcmcPortFaultReturnEnable,
       "rcmcPortFaultReturnStatus": rcmcPortFaultReturnStatus,
       "rcmcPortFefi": rcmcPortFefi,
       "rcmcPortFPToPorts": rcmcPortFPToPorts,
       "rcmcPortInfoTrap": rcmcPortInfoTrap,
       "rcmcPortFaultPassTrap": rcmcPortFaultPassTrap,
       "rcmcPortFaultReturnTrap": rcmcPortFaultReturnTrap,
       "rcmcPortFefiTrap": rcmcPortFefiTrap,
       "rcmcPortSDTrap": rcmcPortSDTrap}
)
