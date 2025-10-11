# SNMP MIB module (OS-MODULE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/OS-MODULE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:03:52 2025
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

(oaOptiSwitch,) = mibBuilder.importSymbols(
    "OS-COMMON-TC-MIB",
    "oaOptiSwitch")

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


# MODULE-IDENTITY

osModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 44)
)
if mibBuilder.loadTexts:
    osModule.setRevisions(
        ("2022-07-13 00:00",
         "2022-06-08 00:00",
         "2022-06-06 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OsModuleGen_ObjectIdentity = ObjectIdentity
osModuleGen = _OsModuleGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 44, 1)
)


class _OsModuleSupport_Type(Integer32):
    """Custom type osModuleSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("supported", 2))
    )


_OsModuleSupport_Type.__name__ = "Integer32"
_OsModuleSupport_Object = MibScalar
osModuleSupport = _OsModuleSupport_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 44, 1, 1),
    _OsModuleSupport_Type()
)
osModuleSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osModuleSupport.setStatus("current")


class _OsModuleType_Type(Integer32):
    """Custom type osModuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("empty", 0),
          ("unknown", 1),
          ("vdsl", 2),
          ("lte", 3),
          ("nfv", 4),
          ("nfvLte", 5),
          ("fiveG", 6))
    )


_OsModuleType_Type.__name__ = "Integer32"
_OsModuleType_Object = MibScalar
osModuleType = _OsModuleType_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 44, 1, 2),
    _OsModuleType_Type()
)
osModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osModuleType.setStatus("current")


class _OsModuleAction_Type(Integer32):
    """Custom type osModuleAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("modemReset", 1))
    )


_OsModuleAction_Type.__name__ = "Integer32"
_OsModuleAction_Object = MibScalar
osModuleAction = _OsModuleAction_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 44, 1, 3),
    _OsModuleAction_Type()
)
osModuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osModuleAction.setStatus("current")


class _OsModuleDescription_Type(DisplayString):
    """Custom type osModuleDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 255),
    )


_OsModuleDescription_Type.__name__ = "DisplayString"
_OsModuleDescription_Object = MibScalar
osModuleDescription = _OsModuleDescription_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 44, 1, 4),
    _OsModuleDescription_Type()
)
osModuleDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osModuleDescription.setStatus("current")
_OsModuleCapabilities_ObjectIdentity = ObjectIdentity
osModuleCapabilities = _OsModuleCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 44, 2)
)
_OsModCapGlobal_ObjectIdentity = ObjectIdentity
osModCapGlobal = _OsModCapGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 44, 2, 1)
)


class _OsModuleGlobalCaps_Type(Bits):
    """Custom type osModuleGlobalCaps based on Bits"""
    namedValues = NamedValues(
        *(("capWireless", 0),
          ("capNfv", 1))
    )

_OsModuleGlobalCaps_Type.__name__ = "Bits"
_OsModuleGlobalCaps_Object = MibScalar
osModuleGlobalCaps = _OsModuleGlobalCaps_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 44, 2, 1, 1),
    _OsModuleGlobalCaps_Type()
)
osModuleGlobalCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osModuleGlobalCaps.setStatus("current")
_OsModCapWirelesslCom_ObjectIdentity = ObjectIdentity
osModCapWirelesslCom = _OsModCapWirelesslCom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 44, 2, 2)
)


class _OsModuleWirelessCaps_Type(Bits):
    """Custom type osModuleWirelessCaps based on Bits"""
    namedValues = NamedValues(
        *(("capLinkProtection", 0),
          ("capMobileAccess", 1),
          ("capFourG", 2),
          ("capFiveG", 3))
    )

_OsModuleWirelessCaps_Type.__name__ = "Bits"
_OsModuleWirelessCaps_Object = MibScalar
osModuleWirelessCaps = _OsModuleWirelessCaps_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 44, 2, 2, 1),
    _OsModuleWirelessCaps_Type()
)
osModuleWirelessCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osModuleWirelessCaps.setStatus("current")


class _OsModCapLinkProtectionRev_Type(DisplayString):
    """Custom type osModCapLinkProtectionRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 63),
    )


_OsModCapLinkProtectionRev_Type.__name__ = "DisplayString"
_OsModCapLinkProtectionRev_Object = MibScalar
osModCapLinkProtectionRev = _OsModCapLinkProtectionRev_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 44, 2, 2, 3),
    _OsModCapLinkProtectionRev_Type()
)
osModCapLinkProtectionRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osModCapLinkProtectionRev.setStatus("current")
_OsModuleMaxApn_Type = Unsigned32
_OsModuleMaxApn_Object = MibScalar
osModuleMaxApn = _OsModuleMaxApn_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 44, 2, 2, 4),
    _OsModuleMaxApn_Type()
)
osModuleMaxApn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osModuleMaxApn.setStatus("current")
_OsModCapNFV_ObjectIdentity = ObjectIdentity
osModCapNFV = _OsModCapNFV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 44, 2, 3)
)


class _OsModuleNfvCaps_Type(Bits):
    """Custom type osModuleNfvCaps based on Bits"""
    namedValues = NamedValues(
        *(("capSingleIP", 0),
          ("capPCIe", 1))
    )

_OsModuleNfvCaps_Type.__name__ = "Bits"
_OsModuleNfvCaps_Object = MibScalar
osModuleNfvCaps = _OsModuleNfvCaps_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 44, 2, 3, 1),
    _OsModuleNfvCaps_Type()
)
osModuleNfvCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osModuleNfvCaps.setStatus("current")
_OsModConformance_ObjectIdentity = ObjectIdentity
osModConformance = _OsModConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 44, 100)
)
_OsModMIBCompliances_ObjectIdentity = ObjectIdentity
osModMIBCompliances = _OsModMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 44, 100, 1)
)
_OsModMIBGroups_ObjectIdentity = ObjectIdentity
osModMIBGroups = _OsModMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 44, 100, 2)
)

# Managed Objects groups

osModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 2, 44, 100, 2, 1)
)
osModuleGroup.setObjects(
    ("OS-MODULE-MIB", "osModuleSupport")
)
if mibBuilder.loadTexts:
    osModuleGroup.setStatus("current")

osModuleOptGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 2, 44, 100, 2, 2)
)
osModuleOptGroup.setObjects(
      *(("OS-MODULE-MIB", "osModuleSupport"),
        ("OS-MODULE-MIB", "osModuleType"),
        ("OS-MODULE-MIB", "osModuleAction"),
        ("OS-MODULE-MIB", "osModuleDescription"),
        ("OS-MODULE-MIB", "osModuleGlobalCaps"),
        ("OS-MODULE-MIB", "osModuleWirelessCaps"),
        ("OS-MODULE-MIB", "osModCapLinkProtectionRev"),
        ("OS-MODULE-MIB", "osModuleMaxApn"),
        ("OS-MODULE-MIB", "osModuleNfvCaps"))
)
if mibBuilder.loadTexts:
    osModuleOptGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

osModuleMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6926, 2, 44, 100, 1, 1)
)
osModuleMIBCompliance.setObjects(
      *(("OS-MODULE-MIB", "osModuleGroup"),
        ("OS-MODULE-MIB", "osModuleOptGroup"))
)
if mibBuilder.loadTexts:
    osModuleMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OS-MODULE-MIB",
    **{"osModule": osModule,
       "osModuleGen": osModuleGen,
       "osModuleSupport": osModuleSupport,
       "osModuleType": osModuleType,
       "osModuleAction": osModuleAction,
       "osModuleDescription": osModuleDescription,
       "osModuleCapabilities": osModuleCapabilities,
       "osModCapGlobal": osModCapGlobal,
       "osModuleGlobalCaps": osModuleGlobalCaps,
       "osModCapWirelesslCom": osModCapWirelesslCom,
       "osModuleWirelessCaps": osModuleWirelessCaps,
       "osModCapLinkProtectionRev": osModCapLinkProtectionRev,
       "osModuleMaxApn": osModuleMaxApn,
       "osModCapNFV": osModCapNFV,
       "osModuleNfvCaps": osModuleNfvCaps,
       "osModConformance": osModConformance,
       "osModMIBCompliances": osModMIBCompliances,
       "osModuleMIBCompliance": osModuleMIBCompliance,
       "osModMIBGroups": osModMIBGroups,
       "osModuleGroup": osModuleGroup,
       "osModuleOptGroup": osModuleOptGroup}
)
