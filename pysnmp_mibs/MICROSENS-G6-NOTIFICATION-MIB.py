# SNMP MIB module (MICROSENS-G6-NOTIFICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/microsens/MICROSENS-G6-NOTIFICATION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:14 2025
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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

microsens = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3181)
)
if mibBuilder.loadTexts:
    microsens.setRevisions(
        ("2017-05-03 00:00",
         "2017-02-23 00:00",
         "2015-10-05 00:00",
         "2015-04-24 00:00",
         "2015-02-02 00:00",
         "2014-08-08 00:00",
         "2014-03-17 00:00",
         "2013-11-13 00:00",
         "2012-08-26 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ManagedSwitches_ObjectIdentity = ObjectIdentity
managedSwitches = _ManagedSwitches_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10)
)
_G6_ObjectIdentity = ObjectIdentity
g6 = _G6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6)
)
_G6TrapGroup_ObjectIdentity = ObjectIdentity
g6TrapGroup = _G6TrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1)
)
_G6Trap_ObjectIdentity = ObjectIdentity
g6Trap = _G6Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1)
)
_G6TrapObjects_ObjectIdentity = ObjectIdentity
g6TrapObjects = _G6TrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 2)
)
_G6TrapObjEventName_Type = DisplayString
_G6TrapObjEventName_Object = MibScalar
g6TrapObjEventName = _G6TrapObjEventName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 2, 1),
    _G6TrapObjEventName_Type()
)
g6TrapObjEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g6TrapObjEventName.setStatus("current")


class _G6TrapObjGroupName_Type(Integer32):
    """Custom type g6TrapObjGroupName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
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
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29)
        )
    )
    namedValues = NamedValues(
        *(("internal", 0),
          ("debug", 2),
          ("test", 3),
          ("reset", 4),
          ("firmware", 5),
          ("system", 6),
          ("config", 7),
          ("login", 8),
          ("auth", 9),
          ("power", 10),
          ("temperature", 11),
          ("link", 12),
          ("sfp", 13),
          ("poe", 14),
          ("ring", 15),
          ("ntp", 16),
          ("signals", 17),
          ("script", 18),
          ("filter", 19),
          ("lacp", 20),
          ("app", 21),
          ("cable", 22),
          ("security", 23),
          ("msp1000", 24),
          ("backup", 25),
          ("fan", 26),
          ("messaging", 27),
          ("terminalserver", 28),
          ("smartoffice", 29))
    )


_G6TrapObjGroupName_Type.__name__ = "Integer32"
_G6TrapObjGroupName_Object = MibScalar
g6TrapObjGroupName = _G6TrapObjGroupName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 2, 2),
    _G6TrapObjGroupName_Type()
)
g6TrapObjGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g6TrapObjGroupName.setStatus("current")


class _G6TrapObjRelevance_Type(Integer32):
    """Custom type g6TrapObjRelevance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("positive", 0),
          ("negative", 1),
          ("information", 2))
    )


_G6TrapObjRelevance_Type.__name__ = "Integer32"
_G6TrapObjRelevance_Object = MibScalar
g6TrapObjRelevance = _G6TrapObjRelevance_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 2, 3),
    _G6TrapObjRelevance_Type()
)
g6TrapObjRelevance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g6TrapObjRelevance.setStatus("current")


class _G6TrapObjSeverity_Type(Integer32):
    """Custom type g6TrapObjSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("debug", 1),
          ("info", 2),
          ("notice", 3),
          ("warning", 4),
          ("error", 5),
          ("critical", 6),
          ("alert", 7),
          ("emergency", 8))
    )


_G6TrapObjSeverity_Type.__name__ = "Integer32"
_G6TrapObjSeverity_Object = MibScalar
g6TrapObjSeverity = _G6TrapObjSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 2, 4),
    _G6TrapObjSeverity_Type()
)
g6TrapObjSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g6TrapObjSeverity.setStatus("current")


class _G6TrapObjSource_Type(Integer32):
    """Custom type g6TrapObjSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unit", 0),
          ("port", 1))
    )


_G6TrapObjSource_Type.__name__ = "Integer32"
_G6TrapObjSource_Object = MibScalar
g6TrapObjSource = _G6TrapObjSource_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 2, 5),
    _G6TrapObjSource_Type()
)
g6TrapObjSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g6TrapObjSource.setStatus("current")
_G6TrapObjSysName_Type = DisplayString
_G6TrapObjSysName_Object = MibScalar
g6TrapObjSysName = _G6TrapObjSysName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 2, 6),
    _G6TrapObjSysName_Type()
)
g6TrapObjSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g6TrapObjSysName.setStatus("current")
_G6TrapObjPortId_Type = Integer32
_G6TrapObjPortId_Object = MibScalar
g6TrapObjPortId = _G6TrapObjPortId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 2, 7),
    _G6TrapObjPortId_Type()
)
g6TrapObjPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g6TrapObjPortId.setStatus("current")
_G6TrapObjPortString_Type = DisplayString
_G6TrapObjPortString_Object = MibScalar
g6TrapObjPortString = _G6TrapObjPortString_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 2, 8),
    _G6TrapObjPortString_Type()
)
g6TrapObjPortString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g6TrapObjPortString.setStatus("current")
_G6TrapObjPortAlias_Type = DisplayString
_G6TrapObjPortAlias_Object = MibScalar
g6TrapObjPortAlias = _G6TrapObjPortAlias_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 2, 9),
    _G6TrapObjPortAlias_Type()
)
g6TrapObjPortAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g6TrapObjPortAlias.setStatus("current")
_G6TrapObjDescription_Type = DisplayString
_G6TrapObjDescription_Object = MibScalar
g6TrapObjDescription = _G6TrapObjDescription_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 2, 10),
    _G6TrapObjDescription_Type()
)
g6TrapObjDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g6TrapObjDescription.setStatus("current")
_G6TrapObjMac_Type = MacAddress
_G6TrapObjMac_Object = MibScalar
g6TrapObjMac = _G6TrapObjMac_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 2, 11),
    _G6TrapObjMac_Type()
)
g6TrapObjMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g6TrapObjMac.setStatus("current")
_G6TrapObjVlanId_Type = Integer32
_G6TrapObjVlanId_Object = MibScalar
g6TrapObjVlanId = _G6TrapObjVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 2, 12),
    _G6TrapObjVlanId_Type()
)
g6TrapObjVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g6TrapObjVlanId.setStatus("current")
_G6TrapObjOfficeGroupName_Type = DisplayString
_G6TrapObjOfficeGroupName_Object = MibScalar
g6TrapObjOfficeGroupName = _G6TrapObjOfficeGroupName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 2, 13),
    _G6TrapObjOfficeGroupName_Type()
)
g6TrapObjOfficeGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g6TrapObjOfficeGroupName.setStatus("current")
_G6TrapObjAvgValue_Type = DisplayString
_G6TrapObjAvgValue_Object = MibScalar
g6TrapObjAvgValue = _G6TrapObjAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 2, 14),
    _G6TrapObjAvgValue_Type()
)
g6TrapObjAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g6TrapObjAvgValue.setStatus("current")
_G6TrapObjTotalValue_Type = DisplayString
_G6TrapObjTotalValue_Object = MibScalar
g6TrapObjTotalValue = _G6TrapObjTotalValue_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 2, 15),
    _G6TrapObjTotalValue_Type()
)
g6TrapObjTotalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g6TrapObjTotalValue.setStatus("current")

# Managed Objects groups


# Notification objects

g6TrapDebug = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 3)
)
g6TrapDebug.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapDebug.setStatus(
        "current"
    )

g6TrapAliveTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 4)
)
g6TrapAliveTest.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapAliveTest.setStatus(
        "current"
    )

g6TrapFirmwareUpdateOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 5)
)
g6TrapFirmwareUpdateOk.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapFirmwareUpdateOk.setStatus(
        "current"
    )

g6TrapFirmwareUpdateFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 6)
)
g6TrapFirmwareUpdateFail.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapFirmwareUpdateFail.setStatus(
        "current"
    )

g6TrapLicenseViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 7)
)
g6TrapLicenseViolation.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapLicenseViolation.setStatus(
        "current"
    )

g6TrapColdStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 8)
)
g6TrapColdStart.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapColdStart.setStatus(
        "current"
    )

g6TrapWarmStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 9)
)
g6TrapWarmStart.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapWarmStart.setStatus(
        "current"
    )

g6TrapFactoryReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 10)
)
g6TrapFactoryReset.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapFactoryReset.setStatus(
        "current"
    )

g6TrapConfigurationLoaded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 11)
)
g6TrapConfigurationLoaded.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapConfigurationLoaded.setStatus(
        "current"
    )

g6TrapChangeConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 12)
)
g6TrapChangeConfig.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapChangeConfig.setStatus(
        "current"
    )

g6TrapChangeOfflineConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 13)
)
g6TrapChangeOfflineConfig.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapChangeOfflineConfig.setStatus(
        "current"
    )

g6TrapActionResponse = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 14)
)
g6TrapActionResponse.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapActionResponse.setStatus(
        "current"
    )

g6TrapCommitConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 15)
)
g6TrapCommitConfig.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapCommitConfig.setStatus(
        "current"
    )

g6TrapPowerSupplyOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 16)
)
g6TrapPowerSupplyOk.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapPowerSupplyOk.setStatus(
        "current"
    )

g6TrapPowerSupplyFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 17)
)
g6TrapPowerSupplyFail.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapPowerSupplyFail.setStatus(
        "current"
    )

g6TrapLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 18)
)
g6TrapLogin.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapLogin.setStatus(
        "current"
    )

g6TrapLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 19)
)
g6TrapLogout.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapLogout.setStatus(
        "current"
    )

g6TrapLoginAttempt = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 20)
)
g6TrapLoginAttempt.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapLoginAttempt.setStatus(
        "current"
    )

g6TrapLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 21)
)
g6TrapLinkUp.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortId"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortString"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortAlias"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapLinkUp.setStatus(
        "current"
    )

g6TrapLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 22)
)
g6TrapLinkDown.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortId"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortString"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortAlias"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapLinkDown.setStatus(
        "current"
    )

g6TrapRingNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 23)
)
g6TrapRingNormal.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapRingNormal.setStatus(
        "current"
    )

g6TrapRingBackup = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 24)
)
g6TrapRingBackup.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapRingBackup.setStatus(
        "current"
    )

g6TrapRingFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 25)
)
g6TrapRingFailure.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapRingFailure.setStatus(
        "current"
    )

g6TrapCouplingState = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 26)
)
g6TrapCouplingState.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortId"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortString"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortAlias"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapCouplingState.setStatus(
        "current"
    )

g6TrapTemperatureOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 27)
)
g6TrapTemperatureOk.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapTemperatureOk.setStatus(
        "current"
    )

g6TrapTemperatureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 28)
)
g6TrapTemperatureWarning.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapTemperatureWarning.setStatus(
        "current"
    )

g6TrapTemperatureFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 29)
)
g6TrapTemperatureFailure.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapTemperatureFailure.setStatus(
        "current"
    )

g6TrapMacAccepted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 30)
)
g6TrapMacAccepted.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortId"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortString"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortAlias"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjMac"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjVlanId"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapMacAccepted.setStatus(
        "current"
    )

g6TrapMacAuthError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 31)
)
g6TrapMacAuthError.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortId"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortString"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortAlias"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjMac"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjVlanId"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapMacAuthError.setStatus(
        "current"
    )

g6TrapMacBlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 32)
)
g6TrapMacBlocked.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortId"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortString"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortAlias"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjMac"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjVlanId"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapMacBlocked.setStatus(
        "current"
    )

g6TrapMacBlockedVlan = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 33)
)
g6TrapMacBlockedVlan.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortId"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortString"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortAlias"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjMac"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjVlanId"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapMacBlockedVlan.setStatus(
        "current"
    )

g6TrapMacDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 34)
)
g6TrapMacDisconnected.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortId"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortString"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortAlias"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjMac"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjVlanId"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapMacDisconnected.setStatus(
        "current"
    )

g6TrapSfpInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 35)
)
g6TrapSfpInserted.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortId"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortString"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortAlias"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapSfpInserted.setStatus(
        "current"
    )

g6TrapSfpRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 36)
)
g6TrapSfpRemoved.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortId"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortString"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortAlias"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapSfpRemoved.setStatus(
        "current"
    )

g6TrapSfpSignalPresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 37)
)
g6TrapSfpSignalPresent.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortId"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortString"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortAlias"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapSfpSignalPresent.setStatus(
        "current"
    )

g6TrapSfpSignalLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 38)
)
g6TrapSfpSignalLoss.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortId"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortString"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortAlias"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapSfpSignalLoss.setStatus(
        "current"
    )

g6TrapSfpSignalChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 39)
)
g6TrapSfpSignalChange.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortId"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortString"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortAlias"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapSfpSignalChange.setStatus(
        "current"
    )

g6TrapSfpMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 40)
)
g6TrapSfpMismatch.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortId"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortString"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortAlias"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapSfpMismatch.setStatus(
        "current"
    )

g6TrapPoeConnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 41)
)
g6TrapPoeConnect.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortId"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortString"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortAlias"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapPoeConnect.setStatus(
        "current"
    )

g6TrapPoeVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 42)
)
g6TrapPoeVoltage.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortId"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortString"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortAlias"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapPoeVoltage.setStatus(
        "current"
    )

g6TrapPoeError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 43)
)
g6TrapPoeError.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortId"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortString"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortAlias"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapPoeError.setStatus(
        "current"
    )

g6TrapPoeClassmismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 44)
)
g6TrapPoeClassmismatch.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortId"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortString"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortAlias"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapPoeClassmismatch.setStatus(
        "current"
    )

g6TrapPoeDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 45)
)
g6TrapPoeDisconnect.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortId"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortString"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortAlias"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapPoeDisconnect.setStatus(
        "current"
    )

g6TrapNtpFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 46)
)
g6TrapNtpFail.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapNtpFail.setStatus(
        "current"
    )

g6TrapHardwareError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 47)
)
g6TrapHardwareError.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapHardwareError.setStatus(
        "current"
    )

g6TrapSoftwareError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 48)
)
g6TrapSoftwareError.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapSoftwareError.setStatus(
        "current"
    )

g6TrapButtonPressed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 49)
)
g6TrapButtonPressed.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapButtonPressed.setStatus(
        "current"
    )

g6TrapInputSignalNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 67)
)
g6TrapInputSignalNormal.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapInputSignalNormal.setStatus(
        "current"
    )

g6TrapInputSignalActivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 68)
)
g6TrapInputSignalActivated.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapInputSignalActivated.setStatus(
        "current"
    )

g6TrapOutputRelayNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 69)
)
g6TrapOutputRelayNormal.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapOutputRelayNormal.setStatus(
        "current"
    )

g6TrapOutputRelayActivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 70)
)
g6TrapOutputRelayActivated.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapOutputRelayActivated.setStatus(
        "current"
    )

g6TrapPacketIntercepted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 71)
)
g6TrapPacketIntercepted.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortId"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortString"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortAlias"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapPacketIntercepted.setStatus(
        "current"
    )

g6TrapScriptUnitPositive = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 72)
)
g6TrapScriptUnitPositive.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapScriptUnitPositive.setStatus(
        "current"
    )

g6TrapScriptUnitNegative = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 73)
)
g6TrapScriptUnitNegative.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapScriptUnitNegative.setStatus(
        "current"
    )

g6TrapScriptPortPositive = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 74)
)
g6TrapScriptPortPositive.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortId"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortString"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortAlias"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapScriptPortPositive.setStatus(
        "current"
    )

g6TrapScriptPortNegative = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 75)
)
g6TrapScriptPortNegative.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortId"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortString"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortAlias"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapScriptPortNegative.setStatus(
        "current"
    )

g6TrapScriptExecuted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 76)
)
g6TrapScriptExecuted.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapScriptExecuted.setStatus(
        "current"
    )

g6TrapScriptError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 77)
)
g6TrapScriptError.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapScriptError.setStatus(
        "current"
    )

g6TrapLoopRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 78)
)
g6TrapLoopRemoved.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortId"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortString"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortAlias"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapLoopRemoved.setStatus(
        "current"
    )

g6TrapLoopDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 79)
)
g6TrapLoopDetected.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortId"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortString"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortAlias"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapLoopDetected.setStatus(
        "current"
    )

g6TrapLacpConnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 80)
)
g6TrapLacpConnect.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortId"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortString"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortAlias"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapLacpConnect.setStatus(
        "current"
    )

g6TrapLacpDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 81)
)
g6TrapLacpDisconnect.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortId"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortString"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortAlias"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapLacpDisconnect.setStatus(
        "current"
    )

g6TrapAppInstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 82)
)
g6TrapAppInstalled.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapAppInstalled.setStatus(
        "current"
    )

g6TrapAppInstallationFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 83)
)
g6TrapAppInstallationFail.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapAppInstallationFail.setStatus(
        "current"
    )

g6TrapAppDeinstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 84)
)
g6TrapAppDeinstalled.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapAppDeinstalled.setStatus(
        "current"
    )

g6TrapCableChangeDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 85)
)
g6TrapCableChangeDetected.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortId"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortString"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortAlias"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapCableChangeDetected.setStatus(
        "current"
    )

g6TrapImplausibleConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 86)
)
g6TrapImplausibleConfig.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapImplausibleConfig.setStatus(
        "current"
    )

g6TrapNetworkAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 87)
)
g6TrapNetworkAttack.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortId"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortString"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortAlias"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapNetworkAttack.setStatus(
        "current"
    )

g6TrapModuleInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 88)
)
g6TrapModuleInserted.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapModuleInserted.setStatus(
        "current"
    )

g6TrapModuleRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 89)
)
g6TrapModuleRemoved.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapModuleRemoved.setStatus(
        "current"
    )

g6TrapMsp1000UnitPositive = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 90)
)
g6TrapMsp1000UnitPositive.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapMsp1000UnitPositive.setStatus(
        "current"
    )

g6TrapMsp1000UnitNegative = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 91)
)
g6TrapMsp1000UnitNegative.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapMsp1000UnitNegative.setStatus(
        "current"
    )

g6TrapMsp1000PortPositive = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 92)
)
g6TrapMsp1000PortPositive.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortId"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortString"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortAlias"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapMsp1000PortPositive.setStatus(
        "current"
    )

g6TrapMsp1000PortNegative = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 93)
)
g6TrapMsp1000PortNegative.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortId"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortString"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortAlias"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapMsp1000PortNegative.setStatus(
        "current"
    )

g6TrapBackupTerminated = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 94)
)
g6TrapBackupTerminated.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortId"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortString"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortAlias"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapBackupTerminated.setStatus(
        "current"
    )

g6TrapBackupEngaged = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 95)
)
g6TrapBackupEngaged.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortId"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortString"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortAlias"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapBackupEngaged.setStatus(
        "current"
    )

g6TrapBackupFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 96)
)
g6TrapBackupFailure.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortId"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortString"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortAlias"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapBackupFailure.setStatus(
        "current"
    )

g6TrapFanOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 97)
)
g6TrapFanOk.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapFanOk.setStatus(
        "current"
    )

g6TrapFanDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 98)
)
g6TrapFanDegraded.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapFanDegraded.setStatus(
        "current"
    )

g6TrapFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 99)
)
g6TrapFanFailure.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapFanFailure.setStatus(
        "current"
    )

g6TrapIncomingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 100)
)
g6TrapIncomingAlert.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapIncomingAlert.setStatus(
        "current"
    )

g6TrapCableTerminationEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 101)
)
g6TrapCableTerminationEstablished.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortId"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortString"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortAlias"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapCableTerminationEstablished.setStatus(
        "current"
    )

g6TrapCableTerminationLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 102)
)
g6TrapCableTerminationLost.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortId"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortString"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortAlias"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapCableTerminationLost.setStatus(
        "current"
    )

g6TrapTerminalServerConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 103)
)
g6TrapTerminalServerConnected.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapTerminalServerConnected.setStatus(
        "current"
    )

g6TrapTerminalServerDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 104)
)
g6TrapTerminalServerDisconnected.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapTerminalServerDisconnected.setStatus(
        "current"
    )

g6TrapTerminalServerFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 105)
)
g6TrapTerminalServerFail.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapTerminalServerFail.setStatus(
        "current"
    )

g6TrapSensorGroupChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 108)
)
g6TrapSensorGroupChange.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjOfficeGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjAvgValue"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjTotalValue"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapSensorGroupChange.setStatus(
        "current"
    )

g6TrapActorGroupChangeRequest = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 110)
)
g6TrapActorGroupChangeRequest.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapActorGroupChangeRequest.setStatus(
        "current"
    )

g6TrapRegisterSmartDevice = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 111)
)
g6TrapRegisterSmartDevice.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapRegisterSmartDevice.setStatus(
        "current"
    )

g6TrapUpdateSmartDevice = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 112)
)
g6TrapUpdateSmartDevice.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapUpdateSmartDevice.setStatus(
        "current"
    )

g6TrapRegisterSmartAttribute = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 115)
)
g6TrapRegisterSmartAttribute.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapRegisterSmartAttribute.setStatus(
        "current"
    )

g6TrapUnregisterSmartDevice = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 117)
)
g6TrapUnregisterSmartDevice.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapUnregisterSmartDevice.setStatus(
        "current"
    )

g6TrapUnregisterSmartAttribute = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 118)
)
g6TrapUnregisterSmartAttribute.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapUnregisterSmartAttribute.setStatus(
        "current"
    )

g6TrapSingleActorChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 119)
)
g6TrapSingleActorChange.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapSingleActorChange.setStatus(
        "current"
    )

g6TrapActorGroupChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 120)
)
g6TrapActorGroupChanged.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjOfficeGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjAvgValue"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapActorGroupChanged.setStatus(
        "current"
    )

g6TrapSmartOfficeInitializing = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 121)
)
g6TrapSmartOfficeInitializing.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapSmartOfficeInitializing.setStatus(
        "current"
    )

g6TrapSmartOfficeStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 122)
)
g6TrapSmartOfficeStarted.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapSmartOfficeStarted.setStatus(
        "current"
    )

g6TrapSmartOfficeStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 123)
)
g6TrapSmartOfficeStopped.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapSmartOfficeStopped.setStatus(
        "current"
    )

g6TrapSmartOfficeError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 124)
)
g6TrapSmartOfficeError.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSysName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapSmartOfficeError.setStatus(
        "current"
    )

g6TrapOtdrMeasurements = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 1, 125)
)
g6TrapOtdrMeasurements.setObjects(
      *(("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjEventName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjGroupName"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjRelevance"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSeverity"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjSource"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortId"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortString"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjPortAlias"),
        ("MICROSENS-G6-NOTIFICATION-MIB", "g6TrapObjDescription"))
)
if mibBuilder.loadTexts:
    g6TrapOtdrMeasurements.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MICROSENS-G6-NOTIFICATION-MIB",
    **{"microsens": microsens,
       "managedSwitches": managedSwitches,
       "g6": g6,
       "g6TrapGroup": g6TrapGroup,
       "g6Trap": g6Trap,
       "g6TrapDebug": g6TrapDebug,
       "g6TrapAliveTest": g6TrapAliveTest,
       "g6TrapFirmwareUpdateOk": g6TrapFirmwareUpdateOk,
       "g6TrapFirmwareUpdateFail": g6TrapFirmwareUpdateFail,
       "g6TrapLicenseViolation": g6TrapLicenseViolation,
       "g6TrapColdStart": g6TrapColdStart,
       "g6TrapWarmStart": g6TrapWarmStart,
       "g6TrapFactoryReset": g6TrapFactoryReset,
       "g6TrapConfigurationLoaded": g6TrapConfigurationLoaded,
       "g6TrapChangeConfig": g6TrapChangeConfig,
       "g6TrapChangeOfflineConfig": g6TrapChangeOfflineConfig,
       "g6TrapActionResponse": g6TrapActionResponse,
       "g6TrapCommitConfig": g6TrapCommitConfig,
       "g6TrapPowerSupplyOk": g6TrapPowerSupplyOk,
       "g6TrapPowerSupplyFail": g6TrapPowerSupplyFail,
       "g6TrapLogin": g6TrapLogin,
       "g6TrapLogout": g6TrapLogout,
       "g6TrapLoginAttempt": g6TrapLoginAttempt,
       "g6TrapLinkUp": g6TrapLinkUp,
       "g6TrapLinkDown": g6TrapLinkDown,
       "g6TrapRingNormal": g6TrapRingNormal,
       "g6TrapRingBackup": g6TrapRingBackup,
       "g6TrapRingFailure": g6TrapRingFailure,
       "g6TrapCouplingState": g6TrapCouplingState,
       "g6TrapTemperatureOk": g6TrapTemperatureOk,
       "g6TrapTemperatureWarning": g6TrapTemperatureWarning,
       "g6TrapTemperatureFailure": g6TrapTemperatureFailure,
       "g6TrapMacAccepted": g6TrapMacAccepted,
       "g6TrapMacAuthError": g6TrapMacAuthError,
       "g6TrapMacBlocked": g6TrapMacBlocked,
       "g6TrapMacBlockedVlan": g6TrapMacBlockedVlan,
       "g6TrapMacDisconnected": g6TrapMacDisconnected,
       "g6TrapSfpInserted": g6TrapSfpInserted,
       "g6TrapSfpRemoved": g6TrapSfpRemoved,
       "g6TrapSfpSignalPresent": g6TrapSfpSignalPresent,
       "g6TrapSfpSignalLoss": g6TrapSfpSignalLoss,
       "g6TrapSfpSignalChange": g6TrapSfpSignalChange,
       "g6TrapSfpMismatch": g6TrapSfpMismatch,
       "g6TrapPoeConnect": g6TrapPoeConnect,
       "g6TrapPoeVoltage": g6TrapPoeVoltage,
       "g6TrapPoeError": g6TrapPoeError,
       "g6TrapPoeClassmismatch": g6TrapPoeClassmismatch,
       "g6TrapPoeDisconnect": g6TrapPoeDisconnect,
       "g6TrapNtpFail": g6TrapNtpFail,
       "g6TrapHardwareError": g6TrapHardwareError,
       "g6TrapSoftwareError": g6TrapSoftwareError,
       "g6TrapButtonPressed": g6TrapButtonPressed,
       "g6TrapInputSignalNormal": g6TrapInputSignalNormal,
       "g6TrapInputSignalActivated": g6TrapInputSignalActivated,
       "g6TrapOutputRelayNormal": g6TrapOutputRelayNormal,
       "g6TrapOutputRelayActivated": g6TrapOutputRelayActivated,
       "g6TrapPacketIntercepted": g6TrapPacketIntercepted,
       "g6TrapScriptUnitPositive": g6TrapScriptUnitPositive,
       "g6TrapScriptUnitNegative": g6TrapScriptUnitNegative,
       "g6TrapScriptPortPositive": g6TrapScriptPortPositive,
       "g6TrapScriptPortNegative": g6TrapScriptPortNegative,
       "g6TrapScriptExecuted": g6TrapScriptExecuted,
       "g6TrapScriptError": g6TrapScriptError,
       "g6TrapLoopRemoved": g6TrapLoopRemoved,
       "g6TrapLoopDetected": g6TrapLoopDetected,
       "g6TrapLacpConnect": g6TrapLacpConnect,
       "g6TrapLacpDisconnect": g6TrapLacpDisconnect,
       "g6TrapAppInstalled": g6TrapAppInstalled,
       "g6TrapAppInstallationFail": g6TrapAppInstallationFail,
       "g6TrapAppDeinstalled": g6TrapAppDeinstalled,
       "g6TrapCableChangeDetected": g6TrapCableChangeDetected,
       "g6TrapImplausibleConfig": g6TrapImplausibleConfig,
       "g6TrapNetworkAttack": g6TrapNetworkAttack,
       "g6TrapModuleInserted": g6TrapModuleInserted,
       "g6TrapModuleRemoved": g6TrapModuleRemoved,
       "g6TrapMsp1000UnitPositive": g6TrapMsp1000UnitPositive,
       "g6TrapMsp1000UnitNegative": g6TrapMsp1000UnitNegative,
       "g6TrapMsp1000PortPositive": g6TrapMsp1000PortPositive,
       "g6TrapMsp1000PortNegative": g6TrapMsp1000PortNegative,
       "g6TrapBackupTerminated": g6TrapBackupTerminated,
       "g6TrapBackupEngaged": g6TrapBackupEngaged,
       "g6TrapBackupFailure": g6TrapBackupFailure,
       "g6TrapFanOk": g6TrapFanOk,
       "g6TrapFanDegraded": g6TrapFanDegraded,
       "g6TrapFanFailure": g6TrapFanFailure,
       "g6TrapIncomingAlert": g6TrapIncomingAlert,
       "g6TrapCableTerminationEstablished": g6TrapCableTerminationEstablished,
       "g6TrapCableTerminationLost": g6TrapCableTerminationLost,
       "g6TrapTerminalServerConnected": g6TrapTerminalServerConnected,
       "g6TrapTerminalServerDisconnected": g6TrapTerminalServerDisconnected,
       "g6TrapTerminalServerFail": g6TrapTerminalServerFail,
       "g6TrapSensorGroupChange": g6TrapSensorGroupChange,
       "g6TrapActorGroupChangeRequest": g6TrapActorGroupChangeRequest,
       "g6TrapRegisterSmartDevice": g6TrapRegisterSmartDevice,
       "g6TrapUpdateSmartDevice": g6TrapUpdateSmartDevice,
       "g6TrapRegisterSmartAttribute": g6TrapRegisterSmartAttribute,
       "g6TrapUnregisterSmartDevice": g6TrapUnregisterSmartDevice,
       "g6TrapUnregisterSmartAttribute": g6TrapUnregisterSmartAttribute,
       "g6TrapSingleActorChange": g6TrapSingleActorChange,
       "g6TrapActorGroupChanged": g6TrapActorGroupChanged,
       "g6TrapSmartOfficeInitializing": g6TrapSmartOfficeInitializing,
       "g6TrapSmartOfficeStarted": g6TrapSmartOfficeStarted,
       "g6TrapSmartOfficeStopped": g6TrapSmartOfficeStopped,
       "g6TrapSmartOfficeError": g6TrapSmartOfficeError,
       "g6TrapOtdrMeasurements": g6TrapOtdrMeasurements,
       "g6TrapObjects": g6TrapObjects,
       "g6TrapObjEventName": g6TrapObjEventName,
       "g6TrapObjGroupName": g6TrapObjGroupName,
       "g6TrapObjRelevance": g6TrapObjRelevance,
       "g6TrapObjSeverity": g6TrapObjSeverity,
       "g6TrapObjSource": g6TrapObjSource,
       "g6TrapObjSysName": g6TrapObjSysName,
       "g6TrapObjPortId": g6TrapObjPortId,
       "g6TrapObjPortString": g6TrapObjPortString,
       "g6TrapObjPortAlias": g6TrapObjPortAlias,
       "g6TrapObjDescription": g6TrapObjDescription,
       "g6TrapObjMac": g6TrapObjMac,
       "g6TrapObjVlanId": g6TrapObjVlanId,
       "g6TrapObjOfficeGroupName": g6TrapObjOfficeGroupName,
       "g6TrapObjAvgValue": g6TrapObjAvgValue,
       "g6TrapObjTotalValue": g6TrapObjTotalValue}
)
