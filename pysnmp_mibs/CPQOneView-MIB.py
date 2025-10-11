# SNMP MIB module (CPQOneView-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/CPQOneView-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:34:23 2025
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

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
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

_CpqOneView_ObjectIdentity = ObjectIdentity
cpqOneView = _CpqOneView_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 179)
)
_CpqOneViewMibRev_ObjectIdentity = ObjectIdentity
cpqOneViewMibRev = _CpqOneViewMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 179, 1)
)


class _CpqOneViewMibRevMajor_Type(Integer32):
    """Custom type cpqOneViewMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqOneViewMibRevMajor_Type.__name__ = "Integer32"
_CpqOneViewMibRevMajor_Object = MibScalar
cpqOneViewMibRevMajor = _CpqOneViewMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 232, 179, 1, 1),
    _CpqOneViewMibRevMajor_Type()
)
cpqOneViewMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOneViewMibRevMajor.setStatus("mandatory")


class _CpqOneViewMibRevMinor_Type(Integer32):
    """Custom type cpqOneViewMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqOneViewMibRevMinor_Type.__name__ = "Integer32"
_CpqOneViewMibRevMinor_Object = MibScalar
cpqOneViewMibRevMinor = _CpqOneViewMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 232, 179, 1, 2),
    _CpqOneViewMibRevMinor_Type()
)
cpqOneViewMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOneViewMibRevMinor.setStatus("mandatory")


class _CpqOneViewMibCondition_Type(Integer32):
    """Custom type cpqOneViewMibCondition based on Integer32"""
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


_CpqOneViewMibCondition_Type.__name__ = "Integer32"
_CpqOneViewMibCondition_Object = MibScalar
cpqOneViewMibCondition = _CpqOneViewMibCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 179, 1, 3),
    _CpqOneViewMibCondition_Type()
)
cpqOneViewMibCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOneViewMibCondition.setStatus("mandatory")
_CpqOneViewComponent_ObjectIdentity = ObjectIdentity
cpqOneViewComponent = _CpqOneViewComponent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 179, 2)
)
_CpqOneViewAlert_ObjectIdentity = ObjectIdentity
cpqOneViewAlert = _CpqOneViewAlert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 179, 2, 1)
)
_CpqOneViewAlertSummary_Type = DisplayString
_CpqOneViewAlertSummary_Object = MibScalar
cpqOneViewAlertSummary = _CpqOneViewAlertSummary_Object(
    (1, 3, 6, 1, 4, 1, 232, 179, 2, 1, 1),
    _CpqOneViewAlertSummary_Type()
)
cpqOneViewAlertSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOneViewAlertSummary.setStatus("optional")
_CpqOneViewAlertResolution_Type = DisplayString
_CpqOneViewAlertResolution_Object = MibScalar
cpqOneViewAlertResolution = _CpqOneViewAlertResolution_Object(
    (1, 3, 6, 1, 4, 1, 232, 179, 2, 1, 2),
    _CpqOneViewAlertResolution_Type()
)
cpqOneViewAlertResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOneViewAlertResolution.setStatus("optional")
_CpqOneViewAlertCategory_Type = DisplayString
_CpqOneViewAlertCategory_Object = MibScalar
cpqOneViewAlertCategory = _CpqOneViewAlertCategory_Object(
    (1, 3, 6, 1, 4, 1, 232, 179, 2, 1, 3),
    _CpqOneViewAlertCategory_Type()
)
cpqOneViewAlertCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOneViewAlertCategory.setStatus("optional")
_CpqOneViewAlertState_Type = DisplayString
_CpqOneViewAlertState_Object = MibScalar
cpqOneViewAlertState = _CpqOneViewAlertState_Object(
    (1, 3, 6, 1, 4, 1, 232, 179, 2, 1, 4),
    _CpqOneViewAlertState_Type()
)
cpqOneViewAlertState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOneViewAlertState.setStatus("optional")
_CpqOneViewAlertIsLifecycle_Type = DisplayString
_CpqOneViewAlertIsLifecycle_Object = MibScalar
cpqOneViewAlertIsLifecycle = _CpqOneViewAlertIsLifecycle_Object(
    (1, 3, 6, 1, 4, 1, 232, 179, 2, 1, 5),
    _CpqOneViewAlertIsLifecycle_Type()
)
cpqOneViewAlertIsLifecycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOneViewAlertIsLifecycle.setStatus("optional")
_CpqOneViewAlertResourceType_Type = DisplayString
_CpqOneViewAlertResourceType_Object = MibScalar
cpqOneViewAlertResourceType = _CpqOneViewAlertResourceType_Object(
    (1, 3, 6, 1, 4, 1, 232, 179, 2, 1, 6),
    _CpqOneViewAlertResourceType_Type()
)
cpqOneViewAlertResourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOneViewAlertResourceType.setStatus("optional")
_CpqOneViewAlertResourceUri_Type = DisplayString
_CpqOneViewAlertResourceUri_Object = MibScalar
cpqOneViewAlertResourceUri = _CpqOneViewAlertResourceUri_Object(
    (1, 3, 6, 1, 4, 1, 232, 179, 2, 1, 7),
    _CpqOneViewAlertResourceUri_Type()
)
cpqOneViewAlertResourceUri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOneViewAlertResourceUri.setStatus("optional")
_CpqOneViewAlertCreatedTime_Type = DisplayString
_CpqOneViewAlertCreatedTime_Object = MibScalar
cpqOneViewAlertCreatedTime = _CpqOneViewAlertCreatedTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 179, 2, 1, 8),
    _CpqOneViewAlertCreatedTime_Type()
)
cpqOneViewAlertCreatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOneViewAlertCreatedTime.setStatus("optional")
_CpqOneViewAlertDeviceHealth_ObjectIdentity = ObjectIdentity
cpqOneViewAlertDeviceHealth = _CpqOneViewAlertDeviceHealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 179, 2, 1, 100)
)
_CpqOneViewAlertSourceIPv4Address_Type = IpAddress
_CpqOneViewAlertSourceIPv4Address_Object = MibScalar
cpqOneViewAlertSourceIPv4Address = _CpqOneViewAlertSourceIPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 232, 179, 2, 1, 100, 1),
    _CpqOneViewAlertSourceIPv4Address_Type()
)
cpqOneViewAlertSourceIPv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOneViewAlertSourceIPv4Address.setStatus("optional")
_CpqOneViewAlertSourceIPv6Address_Type = IpAddress
_CpqOneViewAlertSourceIPv6Address_Object = MibScalar
cpqOneViewAlertSourceIPv6Address = _CpqOneViewAlertSourceIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 232, 179, 2, 1, 100, 2),
    _CpqOneViewAlertSourceIPv6Address_Type()
)
cpqOneViewAlertSourceIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOneViewAlertSourceIPv6Address.setStatus("optional")
_CpqOneViewAlertEnterpriseId_Type = DisplayString
_CpqOneViewAlertEnterpriseId_Object = MibScalar
cpqOneViewAlertEnterpriseId = _CpqOneViewAlertEnterpriseId_Object(
    (1, 3, 6, 1, 4, 1, 232, 179, 2, 1, 100, 3),
    _CpqOneViewAlertEnterpriseId_Type()
)
cpqOneViewAlertEnterpriseId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOneViewAlertEnterpriseId.setStatus("optional")
_CpqOneViewAlertTypeId_Type = Integer32
_CpqOneViewAlertTypeId_Object = MibScalar
cpqOneViewAlertTypeId = _CpqOneViewAlertTypeId_Object(
    (1, 3, 6, 1, 4, 1, 232, 179, 2, 1, 100, 4),
    _CpqOneViewAlertTypeId_Type()
)
cpqOneViewAlertTypeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOneViewAlertTypeId.setStatus("optional")
_CpqOneViewAlertInfo_Type = Integer32
_CpqOneViewAlertInfo_Object = MibScalar
cpqOneViewAlertInfo = _CpqOneViewAlertInfo_Object(
    (1, 3, 6, 1, 4, 1, 232, 179, 2, 1, 100, 5),
    _CpqOneViewAlertInfo_Type()
)
cpqOneViewAlertInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOneViewAlertInfo.setStatus("optional")

# Managed Objects groups


# Notification objects

cpqOneViewCriticalAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 179001)
)
cpqOneViewCriticalAlert.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQOneView-MIB", "cpqOneViewAlertCategory"),
        ("CPQOneView-MIB", "cpqOneViewAlertState"),
        ("CPQOneView-MIB", "cpqOneViewAlertSummary"),
        ("CPQOneView-MIB", "cpqOneViewAlertResolution"),
        ("CPQOneView-MIB", "cpqOneViewAlertIsLifecycle"),
        ("CPQOneView-MIB", "cpqOneViewAlertCreatedTime"),
        ("CPQOneView-MIB", "cpqOneViewAlertResourceType"),
        ("CPQOneView-MIB", "cpqOneViewAlertResourceUri"),
        ("CPQOneView-MIB", "cpqOneViewAlertSourceIPv4Address"),
        ("CPQOneView-MIB", "cpqOneViewAlertSourceIPv6Address"),
        ("CPQOneView-MIB", "cpqOneViewAlertEnterpriseId"),
        ("CPQOneView-MIB", "cpqOneViewAlertTypeId"),
        ("CPQOneView-MIB", "cpqOneViewAlertInfo"))
)
if mibBuilder.loadTexts:
    cpqOneViewCriticalAlert.setStatus(
        ""
    )

cpqOneViewWarningAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 179002)
)
cpqOneViewWarningAlert.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQOneView-MIB", "cpqOneViewAlertCategory"),
        ("CPQOneView-MIB", "cpqOneViewAlertState"),
        ("CPQOneView-MIB", "cpqOneViewAlertSummary"),
        ("CPQOneView-MIB", "cpqOneViewAlertResolution"),
        ("CPQOneView-MIB", "cpqOneViewAlertIsLifecycle"),
        ("CPQOneView-MIB", "cpqOneViewAlertCreatedTime"),
        ("CPQOneView-MIB", "cpqOneViewAlertResourceType"),
        ("CPQOneView-MIB", "cpqOneViewAlertResourceUri"),
        ("CPQOneView-MIB", "cpqOneViewAlertSourceIPv4Address"),
        ("CPQOneView-MIB", "cpqOneViewAlertSourceIPv6Address"),
        ("CPQOneView-MIB", "cpqOneViewAlertEnterpriseId"),
        ("CPQOneView-MIB", "cpqOneViewAlertTypeId"),
        ("CPQOneView-MIB", "cpqOneViewAlertInfo"))
)
if mibBuilder.loadTexts:
    cpqOneViewWarningAlert.setStatus(
        ""
    )

cpqOneViewOkAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 179003)
)
cpqOneViewOkAlert.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQOneView-MIB", "cpqOneViewAlertCategory"),
        ("CPQOneView-MIB", "cpqOneViewAlertState"),
        ("CPQOneView-MIB", "cpqOneViewAlertSummary"),
        ("CPQOneView-MIB", "cpqOneViewAlertResolution"),
        ("CPQOneView-MIB", "cpqOneViewAlertIsLifecycle"),
        ("CPQOneView-MIB", "cpqOneViewAlertCreatedTime"),
        ("CPQOneView-MIB", "cpqOneViewAlertResourceType"),
        ("CPQOneView-MIB", "cpqOneViewAlertResourceUri"),
        ("CPQOneView-MIB", "cpqOneViewAlertSourceIPv4Address"),
        ("CPQOneView-MIB", "cpqOneViewAlertSourceIPv6Address"),
        ("CPQOneView-MIB", "cpqOneViewAlertEnterpriseId"),
        ("CPQOneView-MIB", "cpqOneViewAlertTypeId"),
        ("CPQOneView-MIB", "cpqOneViewAlertInfo"))
)
if mibBuilder.loadTexts:
    cpqOneViewOkAlert.setStatus(
        ""
    )

cpqOneViewUnknownAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 179004)
)
cpqOneViewUnknownAlert.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQOneView-MIB", "cpqOneViewAlertCategory"),
        ("CPQOneView-MIB", "cpqOneViewAlertState"),
        ("CPQOneView-MIB", "cpqOneViewAlertSummary"),
        ("CPQOneView-MIB", "cpqOneViewAlertResolution"),
        ("CPQOneView-MIB", "cpqOneViewAlertIsLifecycle"),
        ("CPQOneView-MIB", "cpqOneViewAlertCreatedTime"),
        ("CPQOneView-MIB", "cpqOneViewAlertResourceType"),
        ("CPQOneView-MIB", "cpqOneViewAlertResourceUri"),
        ("CPQOneView-MIB", "cpqOneViewAlertSourceIPv4Address"),
        ("CPQOneView-MIB", "cpqOneViewAlertSourceIPv6Address"),
        ("CPQOneView-MIB", "cpqOneViewAlertEnterpriseId"),
        ("CPQOneView-MIB", "cpqOneViewAlertTypeId"),
        ("CPQOneView-MIB", "cpqOneViewAlertInfo"))
)
if mibBuilder.loadTexts:
    cpqOneViewUnknownAlert.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQOneView-MIB",
    **{"cpqOneViewCriticalAlert": cpqOneViewCriticalAlert,
       "cpqOneViewWarningAlert": cpqOneViewWarningAlert,
       "cpqOneViewOkAlert": cpqOneViewOkAlert,
       "cpqOneViewUnknownAlert": cpqOneViewUnknownAlert,
       "cpqOneView": cpqOneView,
       "cpqOneViewMibRev": cpqOneViewMibRev,
       "cpqOneViewMibRevMajor": cpqOneViewMibRevMajor,
       "cpqOneViewMibRevMinor": cpqOneViewMibRevMinor,
       "cpqOneViewMibCondition": cpqOneViewMibCondition,
       "cpqOneViewComponent": cpqOneViewComponent,
       "cpqOneViewAlert": cpqOneViewAlert,
       "cpqOneViewAlertSummary": cpqOneViewAlertSummary,
       "cpqOneViewAlertResolution": cpqOneViewAlertResolution,
       "cpqOneViewAlertCategory": cpqOneViewAlertCategory,
       "cpqOneViewAlertState": cpqOneViewAlertState,
       "cpqOneViewAlertIsLifecycle": cpqOneViewAlertIsLifecycle,
       "cpqOneViewAlertResourceType": cpqOneViewAlertResourceType,
       "cpqOneViewAlertResourceUri": cpqOneViewAlertResourceUri,
       "cpqOneViewAlertCreatedTime": cpqOneViewAlertCreatedTime,
       "cpqOneViewAlertDeviceHealth": cpqOneViewAlertDeviceHealth,
       "cpqOneViewAlertSourceIPv4Address": cpqOneViewAlertSourceIPv4Address,
       "cpqOneViewAlertSourceIPv6Address": cpqOneViewAlertSourceIPv6Address,
       "cpqOneViewAlertEnterpriseId": cpqOneViewAlertEnterpriseId,
       "cpqOneViewAlertTypeId": cpqOneViewAlertTypeId,
       "cpqOneViewAlertInfo": cpqOneViewAlertInfo}
)
