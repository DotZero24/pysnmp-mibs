# SNMP MIB module (HP-ICF-IPV6-RA-GUARD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/HP-ICF-IPV6-RA-GUARD-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:38:31 2025
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfIpv6RAGuard = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87)
)
if mibBuilder.loadTexts:
    hpicfIpv6RAGuard.setRevisions(
        ("2011-03-16 05:24",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfIpv6RAGuardObjects_ObjectIdentity = ObjectIdentity
hpicfIpv6RAGuardObjects = _HpicfIpv6RAGuardObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 1)
)
_HpicfIpv6RAGuardConfig_ObjectIdentity = ObjectIdentity
hpicfIpv6RAGuardConfig = _HpicfIpv6RAGuardConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 1, 1)
)
_HpicfRAGuardPortTable_Object = MibTable
hpicfRAGuardPortTable = _HpicfRAGuardPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfRAGuardPortTable.setStatus("current")
_HpicfRAGuardPortEntry_Object = MibTableRow
hpicfRAGuardPortEntry = _HpicfRAGuardPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 1, 1, 1, 1)
)
hpicfRAGuardPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpicfRAGuardPortEntry.setStatus("current")
_HpicfRAGuardPortBlocked_Type = TruthValue
_HpicfRAGuardPortBlocked_Object = MibTableColumn
hpicfRAGuardPortBlocked = _HpicfRAGuardPortBlocked_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 1, 1, 1, 1, 1),
    _HpicfRAGuardPortBlocked_Type()
)
hpicfRAGuardPortBlocked.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRAGuardPortBlocked.setStatus("current")
_HpicfRAGuardPortBlockedRAs_Type = Counter64
_HpicfRAGuardPortBlockedRAs_Object = MibTableColumn
hpicfRAGuardPortBlockedRAs = _HpicfRAGuardPortBlockedRAs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 1, 1, 1, 1, 2),
    _HpicfRAGuardPortBlockedRAs_Type()
)
hpicfRAGuardPortBlockedRAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRAGuardPortBlockedRAs.setStatus("current")
_HpicfRAGuardPortBlockedRedirs_Type = Counter64
_HpicfRAGuardPortBlockedRedirs_Object = MibTableColumn
hpicfRAGuardPortBlockedRedirs = _HpicfRAGuardPortBlockedRedirs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 1, 1, 1, 1, 3),
    _HpicfRAGuardPortBlockedRedirs_Type()
)
hpicfRAGuardPortBlockedRedirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRAGuardPortBlockedRedirs.setStatus("current")
_HpicfRAGuardPortLog_Type = TruthValue
_HpicfRAGuardPortLog_Object = MibTableColumn
hpicfRAGuardPortLog = _HpicfRAGuardPortLog_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 1, 1, 1, 1, 4),
    _HpicfRAGuardPortLog_Type()
)
hpicfRAGuardPortLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRAGuardPortLog.setStatus("current")


class _HpicfRAGuardLastErrorCode_Type(Integer32):
    """Custom type hpicfRAGuardLastErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noError", 1),
          ("insufficientHardwareResources", 2),
          ("genericError", 3))
    )


_HpicfRAGuardLastErrorCode_Type.__name__ = "Integer32"
_HpicfRAGuardLastErrorCode_Object = MibTableColumn
hpicfRAGuardLastErrorCode = _HpicfRAGuardLastErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 1, 1, 1, 1, 5),
    _HpicfRAGuardLastErrorCode_Type()
)
hpicfRAGuardLastErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRAGuardLastErrorCode.setStatus("current")
_HpicfIpv6RAGuardConformance_ObjectIdentity = ObjectIdentity
hpicfIpv6RAGuardConformance = _HpicfIpv6RAGuardConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 2)
)
_HpicfIpv6RAGuardCompliances_ObjectIdentity = ObjectIdentity
hpicfIpv6RAGuardCompliances = _HpicfIpv6RAGuardCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 2, 1)
)
_HpicfIpv6RAGuardGroups_ObjectIdentity = ObjectIdentity
hpicfIpv6RAGuardGroups = _HpicfIpv6RAGuardGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 2, 2)
)

# Managed Objects groups

hpicfIpv6RAGuardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 2, 2, 1)
)
hpicfIpv6RAGuardGroup.setObjects(
      *(("HP-ICF-IPV6-RA-GUARD-MIB", "hpicfRAGuardPortBlocked"),
        ("HP-ICF-IPV6-RA-GUARD-MIB", "hpicfRAGuardPortBlockedRAs"),
        ("HP-ICF-IPV6-RA-GUARD-MIB", "hpicfRAGuardPortBlockedRedirs"),
        ("HP-ICF-IPV6-RA-GUARD-MIB", "hpicfRAGuardPortLog"),
        ("HP-ICF-IPV6-RA-GUARD-MIB", "hpicfRAGuardLastErrorCode"))
)
if mibBuilder.loadTexts:
    hpicfIpv6RAGuardGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfIpv6RAGuardCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 2, 1, 1)
)
hpicfIpv6RAGuardCompliance.setObjects(
    ("HP-ICF-IPV6-RA-GUARD-MIB", "hpicfIpv6RAGuardGroup")
)
if mibBuilder.loadTexts:
    hpicfIpv6RAGuardCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-IPV6-RA-GUARD-MIB",
    **{"hpicfIpv6RAGuard": hpicfIpv6RAGuard,
       "hpicfIpv6RAGuardObjects": hpicfIpv6RAGuardObjects,
       "hpicfIpv6RAGuardConfig": hpicfIpv6RAGuardConfig,
       "hpicfRAGuardPortTable": hpicfRAGuardPortTable,
       "hpicfRAGuardPortEntry": hpicfRAGuardPortEntry,
       "hpicfRAGuardPortBlocked": hpicfRAGuardPortBlocked,
       "hpicfRAGuardPortBlockedRAs": hpicfRAGuardPortBlockedRAs,
       "hpicfRAGuardPortBlockedRedirs": hpicfRAGuardPortBlockedRedirs,
       "hpicfRAGuardPortLog": hpicfRAGuardPortLog,
       "hpicfRAGuardLastErrorCode": hpicfRAGuardLastErrorCode,
       "hpicfIpv6RAGuardConformance": hpicfIpv6RAGuardConformance,
       "hpicfIpv6RAGuardCompliances": hpicfIpv6RAGuardCompliances,
       "hpicfIpv6RAGuardCompliance": hpicfIpv6RAGuardCompliance,
       "hpicfIpv6RAGuardGroups": hpicfIpv6RAGuardGroups,
       "hpicfIpv6RAGuardGroup": hpicfIpv6RAGuardGroup}
)
