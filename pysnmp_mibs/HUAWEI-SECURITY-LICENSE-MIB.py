# SNMP MIB module (HUAWEI-SECURITY-LICENSE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/huawei/HUAWEI-SECURITY-LICENSE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:23:27 2025
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
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

hwLicenseMibObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16)
)
if mibBuilder.loadTexts:
    hwLicenseMibObjects.setRevisions(
        ("2016-01-22 09:00",
         "2015-04-15 09:00",
         "2003-03-18 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Huawei_ObjectIdentity = ObjectIdentity
huawei = _Huawei_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011)
)
_HuaweiUtility_ObjectIdentity = ObjectIdentity
huaweiUtility = _HuaweiUtility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6)
)
_HwSecurity_ObjectIdentity = ObjectIdentity
hwSecurity = _HwSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122)
)
_HwLicenseCfgObjects_ObjectIdentity = ObjectIdentity
hwLicenseCfgObjects = _HwLicenseCfgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 1)
)
_HwLicenseMonitorObjects_ObjectIdentity = ObjectIdentity
hwLicenseMonitorObjects = _HwLicenseMonitorObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 2)
)
_HwLicenseTotalVfwNumber_Type = Counter64
_HwLicenseTotalVfwNumber_Object = MibScalar
hwLicenseTotalVfwNumber = _HwLicenseTotalVfwNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 2, 1),
    _HwLicenseTotalVfwNumber_Type()
)
hwLicenseTotalVfwNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLicenseTotalVfwNumber.setStatus("current")
_HwLicenseCurVfwNumber_Type = Counter64
_HwLicenseCurVfwNumber_Object = MibScalar
hwLicenseCurVfwNumber = _HwLicenseCurVfwNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 2, 2),
    _HwLicenseCurVfwNumber_Type()
)
hwLicenseCurVfwNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLicenseCurVfwNumber.setStatus("current")
_HwLicenseTotalIPsecTunnelNumber_Type = Counter64
_HwLicenseTotalIPsecTunnelNumber_Object = MibScalar
hwLicenseTotalIPsecTunnelNumber = _HwLicenseTotalIPsecTunnelNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 2, 3),
    _HwLicenseTotalIPsecTunnelNumber_Type()
)
hwLicenseTotalIPsecTunnelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLicenseTotalIPsecTunnelNumber.setStatus("current")
_HwLicenseCurIPsecTunnelNumber_Type = Counter64
_HwLicenseCurIPsecTunnelNumber_Object = MibScalar
hwLicenseCurIPsecTunnelNumber = _HwLicenseCurIPsecTunnelNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 2, 4),
    _HwLicenseCurIPsecTunnelNumber_Type()
)
hwLicenseCurIPsecTunnelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLicenseCurIPsecTunnelNumber.setStatus("current")
_HwLicenseTotal6RDSessCount_Type = Counter64
_HwLicenseTotal6RDSessCount_Object = MibScalar
hwLicenseTotal6RDSessCount = _HwLicenseTotal6RDSessCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 2, 5),
    _HwLicenseTotal6RDSessCount_Type()
)
hwLicenseTotal6RDSessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLicenseTotal6RDSessCount.setStatus("current")
_HwLicenseCur6RDSessCount_Type = Counter64
_HwLicenseCur6RDSessCount_Object = MibScalar
hwLicenseCur6RDSessCount = _HwLicenseCur6RDSessCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 2, 6),
    _HwLicenseCur6RDSessCount_Type()
)
hwLicenseCur6RDSessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLicenseCur6RDSessCount.setStatus("current")
_HwLicenseTotalNAT64SessCount_Type = Counter64
_HwLicenseTotalNAT64SessCount_Object = MibScalar
hwLicenseTotalNAT64SessCount = _HwLicenseTotalNAT64SessCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 2, 7),
    _HwLicenseTotalNAT64SessCount_Type()
)
hwLicenseTotalNAT64SessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLicenseTotalNAT64SessCount.setStatus("current")
_HwLicenseCurNAT64SessCount_Type = Counter64
_HwLicenseCurNAT64SessCount_Object = MibScalar
hwLicenseCurNAT64SessCount = _HwLicenseCurNAT64SessCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 2, 8),
    _HwLicenseCurNAT64SessCount_Type()
)
hwLicenseCurNAT64SessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLicenseCurNAT64SessCount.setStatus("current")
_HwLicenseTotalDSLiteSessCount_Type = Counter64
_HwLicenseTotalDSLiteSessCount_Object = MibScalar
hwLicenseTotalDSLiteSessCount = _HwLicenseTotalDSLiteSessCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 2, 9),
    _HwLicenseTotalDSLiteSessCount_Type()
)
hwLicenseTotalDSLiteSessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLicenseTotalDSLiteSessCount.setStatus("current")
_HwLicenseCurDSLiteSessCount_Type = Counter64
_HwLicenseCurDSLiteSessCount_Object = MibScalar
hwLicenseCurDSLiteSessCount = _HwLicenseCurDSLiteSessCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 2, 10),
    _HwLicenseCurDSLiteSessCount_Type()
)
hwLicenseCurDSLiteSessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLicenseCurDSLiteSessCount.setStatus("current")
_HwLicenseConformance_ObjectIdentity = ObjectIdentity
hwLicenseConformance = _HwLicenseConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 3)
)
_HwLicenseGroups_ObjectIdentity = ObjectIdentity
hwLicenseGroups = _HwLicenseGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 3, 1)
)
_HwLicenseCompliances_ObjectIdentity = ObjectIdentity
hwLicenseCompliances = _HwLicenseCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 3, 2)
)
_HwLicenseSysObjects_ObjectIdentity = ObjectIdentity
hwLicenseSysObjects = _HwLicenseSysObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 4)
)
_HwLicenseSysCur6RDSessCount_Type = Gauge32
_HwLicenseSysCur6RDSessCount_Object = MibScalar
hwLicenseSysCur6RDSessCount = _HwLicenseSysCur6RDSessCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 4, 1),
    _HwLicenseSysCur6RDSessCount_Type()
)
hwLicenseSysCur6RDSessCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLicenseSysCur6RDSessCount.setStatus("current")
_HwLicenseSysTotal6RDSessCount_Type = Gauge32
_HwLicenseSysTotal6RDSessCount_Object = MibScalar
hwLicenseSysTotal6RDSessCount = _HwLicenseSysTotal6RDSessCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 4, 2),
    _HwLicenseSysTotal6RDSessCount_Type()
)
hwLicenseSysTotal6RDSessCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLicenseSysTotal6RDSessCount.setStatus("current")
_HwLicenseSys6RDSessPercent_Type = Gauge32
_HwLicenseSys6RDSessPercent_Object = MibScalar
hwLicenseSys6RDSessPercent = _HwLicenseSys6RDSessPercent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 4, 3),
    _HwLicenseSys6RDSessPercent_Type()
)
hwLicenseSys6RDSessPercent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLicenseSys6RDSessPercent.setStatus("current")
_HwLicenseSys6RDSessThreshold_Type = Gauge32
_HwLicenseSys6RDSessThreshold_Object = MibScalar
hwLicenseSys6RDSessThreshold = _HwLicenseSys6RDSessThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 4, 4),
    _HwLicenseSys6RDSessThreshold_Type()
)
hwLicenseSys6RDSessThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLicenseSys6RDSessThreshold.setStatus("current")
_HwLicenseSysCurNAT64SessCount_Type = Gauge32
_HwLicenseSysCurNAT64SessCount_Object = MibScalar
hwLicenseSysCurNAT64SessCount = _HwLicenseSysCurNAT64SessCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 4, 5),
    _HwLicenseSysCurNAT64SessCount_Type()
)
hwLicenseSysCurNAT64SessCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLicenseSysCurNAT64SessCount.setStatus("current")
_HwLicenseSysTotalNAT64SessCount_Type = Gauge32
_HwLicenseSysTotalNAT64SessCount_Object = MibScalar
hwLicenseSysTotalNAT64SessCount = _HwLicenseSysTotalNAT64SessCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 4, 6),
    _HwLicenseSysTotalNAT64SessCount_Type()
)
hwLicenseSysTotalNAT64SessCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLicenseSysTotalNAT64SessCount.setStatus("current")
_HwLicenseSysNAT64SessPercent_Type = Gauge32
_HwLicenseSysNAT64SessPercent_Object = MibScalar
hwLicenseSysNAT64SessPercent = _HwLicenseSysNAT64SessPercent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 4, 7),
    _HwLicenseSysNAT64SessPercent_Type()
)
hwLicenseSysNAT64SessPercent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLicenseSysNAT64SessPercent.setStatus("current")
_HwLicenseSysNAT64SessThreshold_Type = Gauge32
_HwLicenseSysNAT64SessThreshold_Object = MibScalar
hwLicenseSysNAT64SessThreshold = _HwLicenseSysNAT64SessThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 4, 8),
    _HwLicenseSysNAT64SessThreshold_Type()
)
hwLicenseSysNAT64SessThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLicenseSysNAT64SessThreshold.setStatus("current")
_HwLicenseSysCurDSLiteSessCount_Type = Gauge32
_HwLicenseSysCurDSLiteSessCount_Object = MibScalar
hwLicenseSysCurDSLiteSessCount = _HwLicenseSysCurDSLiteSessCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 4, 9),
    _HwLicenseSysCurDSLiteSessCount_Type()
)
hwLicenseSysCurDSLiteSessCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLicenseSysCurDSLiteSessCount.setStatus("current")
_HwLicenseSysTotalDSLiteSessCount_Type = Gauge32
_HwLicenseSysTotalDSLiteSessCount_Object = MibScalar
hwLicenseSysTotalDSLiteSessCount = _HwLicenseSysTotalDSLiteSessCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 4, 10),
    _HwLicenseSysTotalDSLiteSessCount_Type()
)
hwLicenseSysTotalDSLiteSessCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLicenseSysTotalDSLiteSessCount.setStatus("current")
_HwLicenseSysDSLiteSessPercent_Type = Gauge32
_HwLicenseSysDSLiteSessPercent_Object = MibScalar
hwLicenseSysDSLiteSessPercent = _HwLicenseSysDSLiteSessPercent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 4, 11),
    _HwLicenseSysDSLiteSessPercent_Type()
)
hwLicenseSysDSLiteSessPercent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLicenseSysDSLiteSessPercent.setStatus("current")
_HwLicenseSysDSLiteSessThreshold_Type = Gauge32
_HwLicenseSysDSLiteSessThreshold_Object = MibScalar
hwLicenseSysDSLiteSessThreshold = _HwLicenseSysDSLiteSessThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 4, 12),
    _HwLicenseSysDSLiteSessThreshold_Type()
)
hwLicenseSysDSLiteSessThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLicenseSysDSLiteSessThreshold.setStatus("current")
_HwLicenseSysUpdateServiceName_Type = OctetString
_HwLicenseSysUpdateServiceName_Object = MibScalar
hwLicenseSysUpdateServiceName = _HwLicenseSysUpdateServiceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 4, 13),
    _HwLicenseSysUpdateServiceName_Type()
)
hwLicenseSysUpdateServiceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLicenseSysUpdateServiceName.setStatus("current")


class _HwLicenseSysGracePeriodTime_Type(Integer32):
    """Custom type hwLicenseSysGracePeriodTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_HwLicenseSysGracePeriodTime_Type.__name__ = "Integer32"
_HwLicenseSysGracePeriodTime_Object = MibScalar
hwLicenseSysGracePeriodTime = _HwLicenseSysGracePeriodTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 4, 14),
    _HwLicenseSysGracePeriodTime_Type()
)
hwLicenseSysGracePeriodTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLicenseSysGracePeriodTime.setStatus("current")


class _HwLicenseSysRemainTime_Type(Integer32):
    """Custom type hwLicenseSysRemainTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_HwLicenseSysRemainTime_Type.__name__ = "Integer32"
_HwLicenseSysRemainTime_Object = MibScalar
hwLicenseSysRemainTime = _HwLicenseSysRemainTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 4, 15),
    _HwLicenseSysRemainTime_Type()
)
hwLicenseSysRemainTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLicenseSysRemainTime.setStatus("current")
_HwLicenseTraps_ObjectIdentity = ObjectIdentity
hwLicenseTraps = _HwLicenseTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 5)
)

# Managed Objects groups

hwlicenseMoniGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 3, 1, 1)
)
hwlicenseMoniGroup.setObjects(
      *(("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseTotalVfwNumber"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseCurVfwNumber"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseTotalIPsecTunnelNumber"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseCurIPsecTunnelNumber"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseTotal6RDSessCount"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseCur6RDSessCount"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseTotalNAT64SessCount"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseCurNAT64SessCount"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseTotalDSLiteSessCount"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseCurDSLiteSessCount"))
)
if mibBuilder.loadTexts:
    hwlicenseMoniGroup.setStatus("current")

hwlicenseSysObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 3, 1, 2)
)
hwlicenseSysObjectGroup.setObjects(
      *(("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSysCur6RDSessCount"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSysTotal6RDSessCount"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSys6RDSessPercent"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSys6RDSessThreshold"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSysCurNAT64SessCount"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSysTotalNAT64SessCount"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSysNAT64SessPercent"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSysNAT64SessThreshold"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSysCurDSLiteSessCount"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSysTotalDSLiteSessCount"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSysDSLiteSessPercent"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSysDSLiteSessThreshold"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSysUpdateServiceName"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSysGracePeriodTime"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSysRemainTime"))
)
if mibBuilder.loadTexts:
    hwlicenseSysObjectGroup.setStatus("current")


# Notification objects

hwLicense6RDSessOverThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 5, 1)
)
hwLicense6RDSessOverThreshold.setObjects(
      *(("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSysCur6RDSessCount"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSysTotal6RDSessCount"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSys6RDSessPercent"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSys6RDSessThreshold"))
)
if mibBuilder.loadTexts:
    hwLicense6RDSessOverThreshold.setStatus(
        "current"
    )

hwLicense6RDSessBelowThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 5, 2)
)
hwLicense6RDSessBelowThreshold.setObjects(
      *(("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSysCur6RDSessCount"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSysTotal6RDSessCount"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSys6RDSessPercent"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSys6RDSessThreshold"))
)
if mibBuilder.loadTexts:
    hwLicense6RDSessBelowThreshold.setStatus(
        "current"
    )

hwLicenseNAT64SessOverThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 5, 3)
)
hwLicenseNAT64SessOverThreshold.setObjects(
      *(("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSysCurNAT64SessCount"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSysTotalNAT64SessCount"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSysNAT64SessPercent"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSysNAT64SessThreshold"))
)
if mibBuilder.loadTexts:
    hwLicenseNAT64SessOverThreshold.setStatus(
        "current"
    )

hwLicenseNAT64SessBelowThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 5, 4)
)
hwLicenseNAT64SessBelowThreshold.setObjects(
      *(("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSysCurNAT64SessCount"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSysTotalNAT64SessCount"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSysNAT64SessPercent"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSysNAT64SessThreshold"))
)
if mibBuilder.loadTexts:
    hwLicenseNAT64SessBelowThreshold.setStatus(
        "current"
    )

hwLicenseDSLiteSessOverThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 5, 5)
)
hwLicenseDSLiteSessOverThreshold.setObjects(
      *(("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSysCurDSLiteSessCount"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSysTotalDSLiteSessCount"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSysDSLiteSessPercent"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSysDSLiteSessThreshold"))
)
if mibBuilder.loadTexts:
    hwLicenseDSLiteSessOverThreshold.setStatus(
        "current"
    )

hwLicenseDSLiteSessBelowThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 5, 6)
)
hwLicenseDSLiteSessBelowThreshold.setObjects(
      *(("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSysCurDSLiteSessCount"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSysTotalDSLiteSessCount"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSysDSLiteSessPercent"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSysDSLiteSessThreshold"))
)
if mibBuilder.loadTexts:
    hwLicenseDSLiteSessBelowThreshold.setStatus(
        "current"
    )

hwLicenseFileExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 5, 7)
)
hwLicenseFileExpired.setObjects(
    ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSysGracePeriodTime")
)
if mibBuilder.loadTexts:
    hwLicenseFileExpired.setStatus(
        "current"
    )

hwLicenseFileGracePeriodExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 5, 8)
)
if mibBuilder.loadTexts:
    hwLicenseFileGracePeriodExpired.setStatus(
        "current"
    )

hwLicenseFeatureExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 5, 9)
)
hwLicenseFeatureExpired.setObjects(
      *(("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSysUpdateServiceName"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSysGracePeriodTime"))
)
if mibBuilder.loadTexts:
    hwLicenseFeatureExpired.setStatus(
        "current"
    )

hwLicenseFeatureGracePeriodExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 5, 10)
)
hwLicenseFeatureGracePeriodExpired.setObjects(
    ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSysUpdateServiceName")
)
if mibBuilder.loadTexts:
    hwLicenseFeatureGracePeriodExpired.setStatus(
        "current"
    )

hwLicenseFileWillExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 5, 11)
)
hwLicenseFileWillExpired.setObjects(
    ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseSysRemainTime")
)
if mibBuilder.loadTexts:
    hwLicenseFileWillExpired.setStatus(
        "current"
    )


# Notifications groups

hwlicenseTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 3, 1, 3)
)
hwlicenseTrapGroup.setObjects(
      *(("HUAWEI-SECURITY-LICENSE-MIB", "hwLicense6RDSessOverThreshold"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicense6RDSessBelowThreshold"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseNAT64SessOverThreshold"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseNAT64SessBelowThreshold"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseDSLiteSessOverThreshold"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseDSLiteSessBelowThreshold"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseFileExpired"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseFileGracePeriodExpired"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseFeatureExpired"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseFeatureGracePeriodExpired"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwLicenseFileWillExpired"))
)
if mibBuilder.loadTexts:
    hwlicenseTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

licenseModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 16, 3, 2, 1)
)
licenseModuleCompliance.setObjects(
      *(("HUAWEI-SECURITY-LICENSE-MIB", "hwlicenseMoniGroup"),
        ("HUAWEI-SECURITY-LICENSE-MIB", "hwlicenseTrapGroup"))
)
if mibBuilder.loadTexts:
    licenseModuleCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-SECURITY-LICENSE-MIB",
    **{"huawei": huawei,
       "huaweiUtility": huaweiUtility,
       "hwSecurity": hwSecurity,
       "hwLicenseMibObjects": hwLicenseMibObjects,
       "hwLicenseCfgObjects": hwLicenseCfgObjects,
       "hwLicenseMonitorObjects": hwLicenseMonitorObjects,
       "hwLicenseTotalVfwNumber": hwLicenseTotalVfwNumber,
       "hwLicenseCurVfwNumber": hwLicenseCurVfwNumber,
       "hwLicenseTotalIPsecTunnelNumber": hwLicenseTotalIPsecTunnelNumber,
       "hwLicenseCurIPsecTunnelNumber": hwLicenseCurIPsecTunnelNumber,
       "hwLicenseTotal6RDSessCount": hwLicenseTotal6RDSessCount,
       "hwLicenseCur6RDSessCount": hwLicenseCur6RDSessCount,
       "hwLicenseTotalNAT64SessCount": hwLicenseTotalNAT64SessCount,
       "hwLicenseCurNAT64SessCount": hwLicenseCurNAT64SessCount,
       "hwLicenseTotalDSLiteSessCount": hwLicenseTotalDSLiteSessCount,
       "hwLicenseCurDSLiteSessCount": hwLicenseCurDSLiteSessCount,
       "hwLicenseConformance": hwLicenseConformance,
       "hwLicenseGroups": hwLicenseGroups,
       "hwlicenseMoniGroup": hwlicenseMoniGroup,
       "hwlicenseSysObjectGroup": hwlicenseSysObjectGroup,
       "hwlicenseTrapGroup": hwlicenseTrapGroup,
       "hwLicenseCompliances": hwLicenseCompliances,
       "licenseModuleCompliance": licenseModuleCompliance,
       "hwLicenseSysObjects": hwLicenseSysObjects,
       "hwLicenseSysCur6RDSessCount": hwLicenseSysCur6RDSessCount,
       "hwLicenseSysTotal6RDSessCount": hwLicenseSysTotal6RDSessCount,
       "hwLicenseSys6RDSessPercent": hwLicenseSys6RDSessPercent,
       "hwLicenseSys6RDSessThreshold": hwLicenseSys6RDSessThreshold,
       "hwLicenseSysCurNAT64SessCount": hwLicenseSysCurNAT64SessCount,
       "hwLicenseSysTotalNAT64SessCount": hwLicenseSysTotalNAT64SessCount,
       "hwLicenseSysNAT64SessPercent": hwLicenseSysNAT64SessPercent,
       "hwLicenseSysNAT64SessThreshold": hwLicenseSysNAT64SessThreshold,
       "hwLicenseSysCurDSLiteSessCount": hwLicenseSysCurDSLiteSessCount,
       "hwLicenseSysTotalDSLiteSessCount": hwLicenseSysTotalDSLiteSessCount,
       "hwLicenseSysDSLiteSessPercent": hwLicenseSysDSLiteSessPercent,
       "hwLicenseSysDSLiteSessThreshold": hwLicenseSysDSLiteSessThreshold,
       "hwLicenseSysUpdateServiceName": hwLicenseSysUpdateServiceName,
       "hwLicenseSysGracePeriodTime": hwLicenseSysGracePeriodTime,
       "hwLicenseSysRemainTime": hwLicenseSysRemainTime,
       "hwLicenseTraps": hwLicenseTraps,
       "hwLicense6RDSessOverThreshold": hwLicense6RDSessOverThreshold,
       "hwLicense6RDSessBelowThreshold": hwLicense6RDSessBelowThreshold,
       "hwLicenseNAT64SessOverThreshold": hwLicenseNAT64SessOverThreshold,
       "hwLicenseNAT64SessBelowThreshold": hwLicenseNAT64SessBelowThreshold,
       "hwLicenseDSLiteSessOverThreshold": hwLicenseDSLiteSessOverThreshold,
       "hwLicenseDSLiteSessBelowThreshold": hwLicenseDSLiteSessBelowThreshold,
       "hwLicenseFileExpired": hwLicenseFileExpired,
       "hwLicenseFileGracePeriodExpired": hwLicenseFileGracePeriodExpired,
       "hwLicenseFeatureExpired": hwLicenseFeatureExpired,
       "hwLicenseFeatureGracePeriodExpired": hwLicenseFeatureGracePeriodExpired,
       "hwLicenseFileWillExpired": hwLicenseFileWillExpired}
)
