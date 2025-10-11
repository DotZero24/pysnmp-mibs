# SNMP MIB module (MX-IF-ADMIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-IF-ADMIN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:23 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(mediatrixAdmin,) = mibBuilder.importSymbols(
    "MX-SMI",
    "mediatrixAdmin")

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

ifAdminMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 5, 8)
)
if mibBuilder.loadTexts:
    ifAdminMIB.setRevisions(
        ("2004-06-10 00:00",
         "1901-11-28 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IfAdminMIBObjects_ObjectIdentity = ObjectIdentity
ifAdminMIBObjects = _IfAdminMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 5, 8, 1)
)
_IfAdminTable_Object = MibTable
ifAdminTable = _IfAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 5, 8, 1, 10)
)
if mibBuilder.loadTexts:
    ifAdminTable.setStatus("current")
_IfAdminEntry_Object = MibTableRow
ifAdminEntry = _IfAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 5, 8, 1, 10, 1)
)
ifAdminEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ifAdminEntry.setStatus("current")


class _IfAdminSetAdmin_Type(Integer32):
    """Custom type ifAdminSetAdmin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("permanentUnlock", 1),
          ("lock", 2),
          ("forcelock", 3),
          ("permanentForcelock", 4),
          ("unlock", 5))
    )


_IfAdminSetAdmin_Type.__name__ = "Integer32"
_IfAdminSetAdmin_Object = MibTableColumn
ifAdminSetAdmin = _IfAdminSetAdmin_Object(
    (1, 3, 6, 1, 4, 1, 4935, 5, 8, 1, 10, 1, 2),
    _IfAdminSetAdmin_Type()
)
ifAdminSetAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifAdminSetAdmin.setStatus("current")


class _IfAdminAdminState_Type(Integer32):
    """Custom type ifAdminAdminState based on Integer32"""
    defaultValue = 1

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
        *(("unlocked", 1),
          ("shuttingDown", 2),
          ("locked", 3),
          ("permanentlock", 4))
    )


_IfAdminAdminState_Type.__name__ = "Integer32"
_IfAdminAdminState_Object = MibTableColumn
ifAdminAdminState = _IfAdminAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 5, 8, 1, 10, 1, 3),
    _IfAdminAdminState_Type()
)
ifAdminAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAdminAdminState.setStatus("current")


class _IfAdminOpState_Type(Integer32):
    """Custom type ifAdminOpState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_IfAdminOpState_Type.__name__ = "Integer32"
_IfAdminOpState_Object = MibTableColumn
ifAdminOpState = _IfAdminOpState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 5, 8, 1, 10, 1, 4),
    _IfAdminOpState_Type()
)
ifAdminOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAdminOpState.setStatus("current")


class _IfAdminUsageState_Type(Integer32):
    """Custom type ifAdminUsageState based on Integer32"""
    defaultValue = 4

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
        *(("idle", 1),
          ("active", 2),
          ("busy", 3),
          ("idle-unusable", 4))
    )


_IfAdminUsageState_Type.__name__ = "Integer32"
_IfAdminUsageState_Object = MibTableColumn
ifAdminUsageState = _IfAdminUsageState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 5, 8, 1, 10, 1, 5),
    _IfAdminUsageState_Type()
)
ifAdminUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAdminUsageState.setStatus("current")


class _IfAdminParentType_Type(Integer32):
    """Custom type ifAdminParentType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("groupAdmin", 1),
          ("ifAdmin", 2))
    )


_IfAdminParentType_Type.__name__ = "Integer32"
_IfAdminParentType_Object = MibTableColumn
ifAdminParentType = _IfAdminParentType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 5, 8, 1, 10, 1, 14),
    _IfAdminParentType_Type()
)
ifAdminParentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAdminParentType.setStatus("current")
_IfAdminParent_Type = Integer32
_IfAdminParent_Object = MibTableColumn
ifAdminParent = _IfAdminParent_Object(
    (1, 3, 6, 1, 4, 1, 4935, 5, 8, 1, 10, 1, 15),
    _IfAdminParent_Type()
)
ifAdminParent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAdminParent.setStatus("current")


class _IfAdminInitialAdminState_Type(Integer32):
    """Custom type ifAdminInitialAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unlocked", 1),
          ("locked", 2))
    )


_IfAdminInitialAdminState_Type.__name__ = "Integer32"
_IfAdminInitialAdminState_Object = MibTableColumn
ifAdminInitialAdminState = _IfAdminInitialAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 5, 8, 1, 10, 1, 65),
    _IfAdminInitialAdminState_Type()
)
ifAdminInitialAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifAdminInitialAdminState.setStatus("current")
_IfAdminConformance_ObjectIdentity = ObjectIdentity
ifAdminConformance = _IfAdminConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 5, 8, 2)
)
_IfAdminCompliances_ObjectIdentity = ObjectIdentity
ifAdminCompliances = _IfAdminCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 5, 8, 2, 1)
)
_IfAdminGroups_ObjectIdentity = ObjectIdentity
ifAdminGroups = _IfAdminGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 5, 8, 2, 2)
)

# Managed Objects groups

ifAdminAnalogPortGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 5, 8, 2, 2, 1)
)
ifAdminAnalogPortGroupVer1.setObjects(
      *(("MX-IF-ADMIN-MIB", "ifAdminSetAdmin"),
        ("MX-IF-ADMIN-MIB", "ifAdminAdminState"),
        ("MX-IF-ADMIN-MIB", "ifAdminOpState"),
        ("MX-IF-ADMIN-MIB", "ifAdminUsageState"),
        ("MX-IF-ADMIN-MIB", "ifAdminParentType"),
        ("MX-IF-ADMIN-MIB", "ifAdminParent"),
        ("MX-IF-ADMIN-MIB", "ifAdminInitialAdminState"))
)
if mibBuilder.loadTexts:
    ifAdminAnalogPortGroupVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ifAdminAnalogPortComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 5, 8, 2, 1, 1)
)
ifAdminAnalogPortComplVer1.setObjects(
    ("MX-IF-ADMIN-MIB", "ifAdminAnalogPortGroupVer1")
)
if mibBuilder.loadTexts:
    ifAdminAnalogPortComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-IF-ADMIN-MIB",
    **{"ifAdminMIB": ifAdminMIB,
       "ifAdminMIBObjects": ifAdminMIBObjects,
       "ifAdminTable": ifAdminTable,
       "ifAdminEntry": ifAdminEntry,
       "ifAdminSetAdmin": ifAdminSetAdmin,
       "ifAdminAdminState": ifAdminAdminState,
       "ifAdminOpState": ifAdminOpState,
       "ifAdminUsageState": ifAdminUsageState,
       "ifAdminParentType": ifAdminParentType,
       "ifAdminParent": ifAdminParent,
       "ifAdminInitialAdminState": ifAdminInitialAdminState,
       "ifAdminConformance": ifAdminConformance,
       "ifAdminCompliances": ifAdminCompliances,
       "ifAdminAnalogPortComplVer1": ifAdminAnalogPortComplVer1,
       "ifAdminGroups": ifAdminGroups,
       "ifAdminAnalogPortGroupVer1": ifAdminAnalogPortGroupVer1}
)
