# SNMP MIB module (CPQSASSWITCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/CPQSASSWITCH-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:38:20 2025
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

(compaq,
 cpqHoTrapFlags) = mibBuilder.importSymbols(
    "CPQHOST-MIB",
    "compaq",
    "cpqHoTrapFlags")

(cpqDaPhyDrvBoxOnConnector,
 cpqDaPhyDrvCntlrIndex,
 cpqDaPhyDrvFWRev,
 cpqDaPhyDrvIndex,
 cpqDaPhyDrvLocationString,
 cpqDaPhyDrvModel,
 cpqDaPhyDrvSerialNum,
 cpqDaPhyDrvStatus,
 cpqDaPhyDrvType) = mibBuilder.importSymbols(
    "CPQIDA-MIB",
    "cpqDaPhyDrvBoxOnConnector",
    "cpqDaPhyDrvCntlrIndex",
    "cpqDaPhyDrvFWRev",
    "cpqDaPhyDrvIndex",
    "cpqDaPhyDrvLocationString",
    "cpqDaPhyDrvModel",
    "cpqDaPhyDrvSerialNum",
    "cpqDaPhyDrvStatus",
    "cpqDaPhyDrvType")

(cpqSiProductName,
 cpqSiSysProductId,
 cpqSiSysSerialNum) = mibBuilder.importSymbols(
    "CPQSINFO-MIB",
    "cpqSiProductName",
    "cpqSiSysProductId",
    "cpqSiSysSerialNum")

(cpqSsBoxBusIndex,
 cpqSsBoxCntlrHwLocation,
 cpqSsBoxCntlrIndex,
 cpqSsBoxCondition,
 cpqSsBoxLocationString,
 cpqSsBoxModel,
 cpqSsBoxSerialNumber,
 cpqSsBoxVendor) = mibBuilder.importSymbols(
    "CPQSTSYS-MIB",
    "cpqSsBoxBusIndex",
    "cpqSsBoxCntlrHwLocation",
    "cpqSsBoxCntlrIndex",
    "cpqSsBoxCondition",
    "cpqSsBoxLocationString",
    "cpqSsBoxModel",
    "cpqSsBoxSerialNumber",
    "cpqSsBoxVendor")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysLocation,
 sysName) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysLocation",
    "sysName")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CpqSasSwitch_ObjectIdentity = ObjectIdentity
cpqSasSwitch = _CpqSasSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 25)
)
_CpqSasSwitchMibRev_ObjectIdentity = ObjectIdentity
cpqSasSwitchMibRev = _CpqSasSwitchMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 25, 1)
)


class _CpqSasSwitchMibRevMajor_Type(Integer32):
    """Custom type cpqSasSwitchMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqSasSwitchMibRevMajor_Type.__name__ = "Integer32"
_CpqSasSwitchMibRevMajor_Object = MibScalar
cpqSasSwitchMibRevMajor = _CpqSasSwitchMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 232, 25, 1, 1),
    _CpqSasSwitchMibRevMajor_Type()
)
cpqSasSwitchMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSasSwitchMibRevMajor.setStatus("mandatory")


class _CpqSasSwitchMibRevMinor_Type(Integer32):
    """Custom type cpqSasSwitchMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSasSwitchMibRevMinor_Type.__name__ = "Integer32"
_CpqSasSwitchMibRevMinor_Object = MibScalar
cpqSasSwitchMibRevMinor = _CpqSasSwitchMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 232, 25, 1, 2),
    _CpqSasSwitchMibRevMinor_Type()
)
cpqSasSwitchMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSasSwitchMibRevMinor.setStatus("mandatory")


class _CpqSasSwitchMibCondition_Type(Integer32):
    """Custom type cpqSasSwitchMibCondition based on Integer32"""
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
        *(("other", 1),
          ("ok", 2),
          ("degraded", 3),
          ("failed", 4))
    )


_CpqSasSwitchMibCondition_Type.__name__ = "Integer32"
_CpqSasSwitchMibCondition_Object = MibScalar
cpqSasSwitchMibCondition = _CpqSasSwitchMibCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 25, 1, 3),
    _CpqSasSwitchMibCondition_Type()
)
cpqSasSwitchMibCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSasSwitchMibCondition.setStatus("mandatory")
_CpqSasSwitchComponent_ObjectIdentity = ObjectIdentity
cpqSasSwitchComponent = _CpqSasSwitchComponent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 25, 2)
)
_CpqSasSwitchInterface_ObjectIdentity = ObjectIdentity
cpqSasSwitchInterface = _CpqSasSwitchInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 25, 2, 1)
)
_CpqSasSwitchOsCommon_ObjectIdentity = ObjectIdentity
cpqSasSwitchOsCommon = _CpqSasSwitchOsCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 25, 2, 1, 4)
)
_CpqSasSwitchHw_ObjectIdentity = ObjectIdentity
cpqSasSwitchHw = _CpqSasSwitchHw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 25, 2, 2)
)
_CpqSasSwitchHwType_ObjectIdentity = ObjectIdentity
cpqSasSwitchHwType = _CpqSasSwitchHwType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 25, 2, 2, 1)
)


class _CpqSasSwitchHwStatus_Type(Integer32):
    """Custom type cpqSasSwitchHwStatus based on Integer32"""
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
        *(("other", 1),
          ("ok", 2),
          ("degraded", 3),
          ("failed", 4))
    )


_CpqSasSwitchHwStatus_Type.__name__ = "Integer32"
_CpqSasSwitchHwStatus_Object = MibScalar
cpqSasSwitchHwStatus = _CpqSasSwitchHwStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 25, 2, 2, 2),
    _CpqSasSwitchHwStatus_Type()
)
cpqSasSwitchHwStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSasSwitchHwStatus.setStatus("mandatory")


class _CpqSasSwitchHwRedundancyState_Type(Integer32):
    """Custom type cpqSasSwitchHwRedundancyState based on Integer32"""
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
        *(("other", 1),
          ("active", 2),
          ("standby", 3),
          ("notConfigured", 4),
          ("notRedundant", 5),
          ("degraded", 6),
          ("mismatch", 7))
    )


_CpqSasSwitchHwRedundancyState_Type.__name__ = "Integer32"
_CpqSasSwitchHwRedundancyState_Object = MibScalar
cpqSasSwitchHwRedundancyState = _CpqSasSwitchHwRedundancyState_Object(
    (1, 3, 6, 1, 4, 1, 232, 25, 2, 2, 3),
    _CpqSasSwitchHwRedundancyState_Type()
)
cpqSasSwitchHwRedundancyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSasSwitchHwRedundancyState.setStatus("mandatory")

# Managed Objects groups


# Notification objects

cpqSasSwitchTestTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 25, 0, 1)
)
cpqSasSwitchTestTrap.setObjects(
      *(("CPQSINFO-MIB", "cpqSiProductName"),
        ("CPQSINFO-MIB", "cpqSiSysProductId"),
        ("CPQSINFO-MIB", "cpqSiSysSerialNum"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    cpqSasSwitchTestTrap.setStatus(
        ""
    )

cpqSasSwitchHwStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 25, 0, 101)
)
cpqSasSwitchHwStatusChangeTrap.setObjects(
      *(("CPQSINFO-MIB", "cpqSiProductName"),
        ("CPQSINFO-MIB", "cpqSiSysProductId"),
        ("CPQSINFO-MIB", "cpqSiSysSerialNum"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CPQSASSWITCH-MIB", "cpqSasSwitchHwStatus"))
)
if mibBuilder.loadTexts:
    cpqSasSwitchHwStatusChangeTrap.setStatus(
        ""
    )

cpqSasSwitchHwRedundancyStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 25, 0, 201)
)
cpqSasSwitchHwRedundancyStateChangeTrap.setObjects(
      *(("CPQSINFO-MIB", "cpqSiProductName"),
        ("CPQSINFO-MIB", "cpqSiSysProductId"),
        ("CPQSINFO-MIB", "cpqSiSysSerialNum"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CPQSASSWITCH-MIB", "cpqSasSwitchHwRedundancyState"))
)
if mibBuilder.loadTexts:
    cpqSasSwitchHwRedundancyStateChangeTrap.setStatus(
        ""
    )

cpqSasSwitchPhysicalDriveAddedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 25, 0, 301)
)
cpqSasSwitchPhysicalDriveAddedTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CPQIDA-MIB", "cpqDaPhyDrvCntlrIndex"),
        ("CPQIDA-MIB", "cpqDaPhyDrvIndex"),
        ("CPQIDA-MIB", "cpqDaPhyDrvLocationString"),
        ("CPQIDA-MIB", "cpqDaPhyDrvType"),
        ("CPQIDA-MIB", "cpqDaPhyDrvModel"),
        ("CPQIDA-MIB", "cpqDaPhyDrvFWRev"),
        ("CPQIDA-MIB", "cpqDaPhyDrvSerialNum"),
        ("CPQIDA-MIB", "cpqDaPhyDrvBoxOnConnector"))
)
if mibBuilder.loadTexts:
    cpqSasSwitchPhysicalDriveAddedTrap.setStatus(
        ""
    )

cpqSasSwitchPhysicalDriveRemovedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 25, 0, 302)
)
cpqSasSwitchPhysicalDriveRemovedTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CPQIDA-MIB", "cpqDaPhyDrvCntlrIndex"),
        ("CPQIDA-MIB", "cpqDaPhyDrvIndex"),
        ("CPQIDA-MIB", "cpqDaPhyDrvLocationString"),
        ("CPQIDA-MIB", "cpqDaPhyDrvType"),
        ("CPQIDA-MIB", "cpqDaPhyDrvModel"),
        ("CPQIDA-MIB", "cpqDaPhyDrvFWRev"),
        ("CPQIDA-MIB", "cpqDaPhyDrvSerialNum"),
        ("CPQIDA-MIB", "cpqDaPhyDrvBoxOnConnector"))
)
if mibBuilder.loadTexts:
    cpqSasSwitchPhysicalDriveRemovedTrap.setStatus(
        ""
    )

cpqSasSwitchStorageEnclosureAddedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 25, 0, 401)
)
cpqSasSwitchStorageEnclosureAddedTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTSYS-MIB", "cpqSsBoxCntlrHwLocation"),
        ("CPQSTSYS-MIB", "cpqSsBoxCntlrIndex"),
        ("CPQSTSYS-MIB", "cpqSsBoxBusIndex"),
        ("CPQSTSYS-MIB", "cpqSsBoxVendor"),
        ("CPQSTSYS-MIB", "cpqSsBoxModel"),
        ("CPQSTSYS-MIB", "cpqSsBoxSerialNumber"),
        ("CPQSTSYS-MIB", "cpqSsBoxCondition"),
        ("CPQSTSYS-MIB", "cpqSsBoxLocationString"))
)
if mibBuilder.loadTexts:
    cpqSasSwitchStorageEnclosureAddedTrap.setStatus(
        ""
    )

cpqSasSwitchStorageEnclosureRemovedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 25, 0, 402)
)
cpqSasSwitchStorageEnclosureRemovedTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTSYS-MIB", "cpqSsBoxCntlrHwLocation"),
        ("CPQSTSYS-MIB", "cpqSsBoxCntlrIndex"),
        ("CPQSTSYS-MIB", "cpqSsBoxBusIndex"),
        ("CPQSTSYS-MIB", "cpqSsBoxVendor"),
        ("CPQSTSYS-MIB", "cpqSsBoxModel"),
        ("CPQSTSYS-MIB", "cpqSsBoxSerialNumber"),
        ("CPQSTSYS-MIB", "cpqSsBoxCondition"),
        ("CPQSTSYS-MIB", "cpqSsBoxLocationString"))
)
if mibBuilder.loadTexts:
    cpqSasSwitchStorageEnclosureRemovedTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQSASSWITCH-MIB",
    **{"cpqSasSwitch": cpqSasSwitch,
       "cpqSasSwitchTestTrap": cpqSasSwitchTestTrap,
       "cpqSasSwitchHwStatusChangeTrap": cpqSasSwitchHwStatusChangeTrap,
       "cpqSasSwitchHwRedundancyStateChangeTrap": cpqSasSwitchHwRedundancyStateChangeTrap,
       "cpqSasSwitchPhysicalDriveAddedTrap": cpqSasSwitchPhysicalDriveAddedTrap,
       "cpqSasSwitchPhysicalDriveRemovedTrap": cpqSasSwitchPhysicalDriveRemovedTrap,
       "cpqSasSwitchStorageEnclosureAddedTrap": cpqSasSwitchStorageEnclosureAddedTrap,
       "cpqSasSwitchStorageEnclosureRemovedTrap": cpqSasSwitchStorageEnclosureRemovedTrap,
       "cpqSasSwitchMibRev": cpqSasSwitchMibRev,
       "cpqSasSwitchMibRevMajor": cpqSasSwitchMibRevMajor,
       "cpqSasSwitchMibRevMinor": cpqSasSwitchMibRevMinor,
       "cpqSasSwitchMibCondition": cpqSasSwitchMibCondition,
       "cpqSasSwitchComponent": cpqSasSwitchComponent,
       "cpqSasSwitchInterface": cpqSasSwitchInterface,
       "cpqSasSwitchOsCommon": cpqSasSwitchOsCommon,
       "cpqSasSwitchHw": cpqSasSwitchHw,
       "cpqSasSwitchHwType": cpqSasSwitchHwType,
       "cpqSasSwitchHwStatus": cpqSasSwitchHwStatus,
       "cpqSasSwitchHwRedundancyState": cpqSasSwitchHwRedundancyState}
)
