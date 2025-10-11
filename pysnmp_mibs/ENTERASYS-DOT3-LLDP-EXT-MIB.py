# SNMP MIB module (ENTERASYS-DOT3-LLDP-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/enterasys/ENTERASYS-DOT3-LLDP-EXT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:47:19 2025
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(lldpV2LocPortIfIndex,) = mibBuilder.importSymbols(
    "LLDP-V2-MIB",
    "lldpV2LocPortIfIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

etsysDot3LldpExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 104)
)
if mibBuilder.loadTexts:
    etsysDot3LldpExtMIB.setRevisions(
        ("2013-08-28 17:51",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysDot3LldpExtObjects_ObjectIdentity = ObjectIdentity
etsysDot3LldpExtObjects = _EtsysDot3LldpExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 104, 1)
)
_EtsysDot3LldpExtEeePort_ObjectIdentity = ObjectIdentity
etsysDot3LldpExtEeePort = _EtsysDot3LldpExtEeePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 104, 1, 2)
)
_EtsysDot3LldpExtEeeConfigTable_Object = MibTable
etsysDot3LldpExtEeeConfigTable = _EtsysDot3LldpExtEeeConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 104, 1, 2, 1)
)
if mibBuilder.loadTexts:
    etsysDot3LldpExtEeeConfigTable.setStatus("current")
_EtsysDot3LldpExtEeeConfigEntry_Object = MibTableRow
etsysDot3LldpExtEeeConfigEntry = _EtsysDot3LldpExtEeeConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 104, 1, 2, 1, 1)
)
etsysDot3LldpExtEeeConfigEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
)
if mibBuilder.loadTexts:
    etsysDot3LldpExtEeeConfigEntry.setStatus("current")


class _EtsysDot3LldpExtEeeAdminStatus_Type(EnabledStatus):
    """Custom type etsysDot3LldpExtEeeAdminStatus based on EnabledStatus"""
    defaultValue = 2


_EtsysDot3LldpExtEeeAdminStatus_Type.__name__ = "EnabledStatus"
_EtsysDot3LldpExtEeeAdminStatus_Object = MibTableColumn
etsysDot3LldpExtEeeAdminStatus = _EtsysDot3LldpExtEeeAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 104, 1, 2, 1, 1, 1),
    _EtsysDot3LldpExtEeeAdminStatus_Type()
)
etsysDot3LldpExtEeeAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDot3LldpExtEeeAdminStatus.setStatus("current")


class _EtsysDot3LldpExtEeeOperStatus_Type(Integer32):
    """Custom type etsysDot3LldpExtEeeOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("unsupported", 3))
    )


_EtsysDot3LldpExtEeeOperStatus_Type.__name__ = "Integer32"
_EtsysDot3LldpExtEeeOperStatus_Object = MibTableColumn
etsysDot3LldpExtEeeOperStatus = _EtsysDot3LldpExtEeeOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 104, 1, 2, 1, 1, 2),
    _EtsysDot3LldpExtEeeOperStatus_Type()
)
etsysDot3LldpExtEeeOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot3LldpExtEeeOperStatus.setStatus("current")


class _EtsysDot3LldpExtEeeTLVTxEnable_Type(EnabledStatus):
    """Custom type etsysDot3LldpExtEeeTLVTxEnable based on EnabledStatus"""
    defaultValue = 2


_EtsysDot3LldpExtEeeTLVTxEnable_Type.__name__ = "EnabledStatus"
_EtsysDot3LldpExtEeeTLVTxEnable_Object = MibTableColumn
etsysDot3LldpExtEeeTLVTxEnable = _EtsysDot3LldpExtEeeTLVTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 104, 1, 2, 1, 1, 3),
    _EtsysDot3LldpExtEeeTLVTxEnable_Type()
)
etsysDot3LldpExtEeeTLVTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDot3LldpExtEeeTLVTxEnable.setStatus("current")
_EtsysDot3LldpExtEeeLocRxTwSys_Type = Integer32
_EtsysDot3LldpExtEeeLocRxTwSys_Object = MibTableColumn
etsysDot3LldpExtEeeLocRxTwSys = _EtsysDot3LldpExtEeeLocRxTwSys_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 104, 1, 2, 1, 1, 4),
    _EtsysDot3LldpExtEeeLocRxTwSys_Type()
)
etsysDot3LldpExtEeeLocRxTwSys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDot3LldpExtEeeLocRxTwSys.setStatus("current")
_EtsysDot3LldpExtEeeLocFbTwSys_Type = Integer32
_EtsysDot3LldpExtEeeLocFbTwSys_Object = MibTableColumn
etsysDot3LldpExtEeeLocFbTwSys = _EtsysDot3LldpExtEeeLocFbTwSys_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 104, 1, 2, 1, 1, 5),
    _EtsysDot3LldpExtEeeLocFbTwSys_Type()
)
etsysDot3LldpExtEeeLocFbTwSys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDot3LldpExtEeeLocFbTwSys.setStatus("current")
_EtsysDot3LldpExtConformance_ObjectIdentity = ObjectIdentity
etsysDot3LldpExtConformance = _EtsysDot3LldpExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 104, 2)
)
_EtsysDot3LldpExtGroups_ObjectIdentity = ObjectIdentity
etsysDot3LldpExtGroups = _EtsysDot3LldpExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 104, 2, 1)
)
_EtsysDot3LldpExtCompliances_ObjectIdentity = ObjectIdentity
etsysDot3LldpExtCompliances = _EtsysDot3LldpExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 104, 2, 2)
)

# Managed Objects groups

etsysDot3LldpExtEeePortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 104, 2, 1, 1)
)
etsysDot3LldpExtEeePortGroup.setObjects(
      *(("ENTERASYS-DOT3-LLDP-EXT-MIB", "etsysDot3LldpExtEeeAdminStatus"),
        ("ENTERASYS-DOT3-LLDP-EXT-MIB", "etsysDot3LldpExtEeeOperStatus"),
        ("ENTERASYS-DOT3-LLDP-EXT-MIB", "etsysDot3LldpExtEeeTLVTxEnable"),
        ("ENTERASYS-DOT3-LLDP-EXT-MIB", "etsysDot3LldpExtEeeLocRxTwSys"),
        ("ENTERASYS-DOT3-LLDP-EXT-MIB", "etsysDot3LldpExtEeeLocFbTwSys"))
)
if mibBuilder.loadTexts:
    etsysDot3LldpExtEeePortGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysDot3LldpExtEeePortCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 104, 2, 2, 1)
)
etsysDot3LldpExtEeePortCompliance.setObjects(
    ("ENTERASYS-DOT3-LLDP-EXT-MIB", "etsysDot3LldpExtEeePortGroup")
)
if mibBuilder.loadTexts:
    etsysDot3LldpExtEeePortCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-DOT3-LLDP-EXT-MIB",
    **{"etsysDot3LldpExtMIB": etsysDot3LldpExtMIB,
       "etsysDot3LldpExtObjects": etsysDot3LldpExtObjects,
       "etsysDot3LldpExtEeePort": etsysDot3LldpExtEeePort,
       "etsysDot3LldpExtEeeConfigTable": etsysDot3LldpExtEeeConfigTable,
       "etsysDot3LldpExtEeeConfigEntry": etsysDot3LldpExtEeeConfigEntry,
       "etsysDot3LldpExtEeeAdminStatus": etsysDot3LldpExtEeeAdminStatus,
       "etsysDot3LldpExtEeeOperStatus": etsysDot3LldpExtEeeOperStatus,
       "etsysDot3LldpExtEeeTLVTxEnable": etsysDot3LldpExtEeeTLVTxEnable,
       "etsysDot3LldpExtEeeLocRxTwSys": etsysDot3LldpExtEeeLocRxTwSys,
       "etsysDot3LldpExtEeeLocFbTwSys": etsysDot3LldpExtEeeLocFbTwSys,
       "etsysDot3LldpExtConformance": etsysDot3LldpExtConformance,
       "etsysDot3LldpExtGroups": etsysDot3LldpExtGroups,
       "etsysDot3LldpExtEeePortGroup": etsysDot3LldpExtEeePortGroup,
       "etsysDot3LldpExtCompliances": etsysDot3LldpExtCompliances,
       "etsysDot3LldpExtEeePortCompliance": etsysDot3LldpExtEeePortCompliance}
)
