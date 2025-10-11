# SNMP MIB module (DLINKPRIME-SWITCHPORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DLINKPRIME-SWITCHPORT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:48:06 2025
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

(dlinkPrimeCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkPrimeCommon")

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

dlinkPrimeSwitchPortMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 20)
)
if mibBuilder.loadTexts:
    dlinkPrimeSwitchPortMIB.setRevisions(
        ("2014-05-07 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DpSwPortNotifications_ObjectIdentity = ObjectIdentity
dpSwPortNotifications = _DpSwPortNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 20, 0)
)
_DpSwPortObjects_ObjectIdentity = ObjectIdentity
dpSwPortObjects = _DpSwPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 20, 1)
)
_DpSwPortIfTable_Object = MibTable
dpSwPortIfTable = _DpSwPortIfTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 20, 1, 1)
)
if mibBuilder.loadTexts:
    dpSwPortIfTable.setStatus("current")
_DpSwPortIfEntry_Object = MibTableRow
dpSwPortIfEntry = _DpSwPortIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 20, 1, 1, 1)
)
dpSwPortIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dpSwPortIfEntry.setStatus("current")


class _DpSwPortIfMdix_Type(Integer32):
    """Custom type dpSwPortIfMdix based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("normal", 2),
          ("cross", 3))
    )


_DpSwPortIfMdix_Type.__name__ = "Integer32"
_DpSwPortIfMdix_Object = MibTableColumn
dpSwPortIfMdix = _DpSwPortIfMdix_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 20, 1, 1, 1, 1),
    _DpSwPortIfMdix_Type()
)
dpSwPortIfMdix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpSwPortIfMdix.setStatus("current")


class _DpSwPortIfJumboFrameSize_Type(Unsigned32):
    """Custom type dpSwPortIfJumboFrameSize based on Unsigned32"""
    defaultValue = 1518


_DpSwPortIfJumboFrameSize_Type.__name__ = "Unsigned32"
_DpSwPortIfJumboFrameSize_Object = MibTableColumn
dpSwPortIfJumboFrameSize = _DpSwPortIfJumboFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 20, 1, 1, 1, 2),
    _DpSwPortIfJumboFrameSize_Type()
)
dpSwPortIfJumboFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpSwPortIfJumboFrameSize.setStatus("current")


class _DpSwPortIfSpeedAutoDowngrade_Type(TruthValue):
    """Custom type dpSwPortIfSpeedAutoDowngrade based on TruthValue"""
    defaultValue = 2


_DpSwPortIfSpeedAutoDowngrade_Type.__name__ = "TruthValue"
_DpSwPortIfSpeedAutoDowngrade_Object = MibTableColumn
dpSwPortIfSpeedAutoDowngrade = _DpSwPortIfSpeedAutoDowngrade_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 20, 1, 1, 1, 3),
    _DpSwPortIfSpeedAutoDowngrade_Type()
)
dpSwPortIfSpeedAutoDowngrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpSwPortIfSpeedAutoDowngrade.setStatus("current")
_DpSwPortConformance_ObjectIdentity = ObjectIdentity
dpSwPortConformance = _DpSwPortConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 20, 2)
)
_DpSwPortCompliances_ObjectIdentity = ObjectIdentity
dpSwPortCompliances = _DpSwPortCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 20, 2, 1)
)
_DpSwPortGroups_ObjectIdentity = ObjectIdentity
dpSwPortGroups = _DpSwPortGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 20, 2, 2)
)

# Managed Objects groups

dpSwPortBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 20, 2, 2, 1)
)
dpSwPortBasicGroup.setObjects(
      *(("DLINKPRIME-SWITCHPORT-MIB", "dpSwPortIfMdix"),
        ("DLINKPRIME-SWITCHPORT-MIB", "dpSwPortIfJumboFrameSize"),
        ("DLINKPRIME-SWITCHPORT-MIB", "dpSwPortIfSpeedAutoDowngrade"))
)
if mibBuilder.loadTexts:
    dpSwPortBasicGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dpSwPortCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 15, 20, 2, 1, 1)
)
dpSwPortCompliance.setObjects(
    ("DLINKPRIME-SWITCHPORT-MIB", "dpSwPortBasicGroup")
)
if mibBuilder.loadTexts:
    dpSwPortCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKPRIME-SWITCHPORT-MIB",
    **{"dlinkPrimeSwitchPortMIB": dlinkPrimeSwitchPortMIB,
       "dpSwPortNotifications": dpSwPortNotifications,
       "dpSwPortObjects": dpSwPortObjects,
       "dpSwPortIfTable": dpSwPortIfTable,
       "dpSwPortIfEntry": dpSwPortIfEntry,
       "dpSwPortIfMdix": dpSwPortIfMdix,
       "dpSwPortIfJumboFrameSize": dpSwPortIfJumboFrameSize,
       "dpSwPortIfSpeedAutoDowngrade": dpSwPortIfSpeedAutoDowngrade,
       "dpSwPortConformance": dpSwPortConformance,
       "dpSwPortCompliances": dpSwPortCompliances,
       "dpSwPortCompliance": dpSwPortCompliance,
       "dpSwPortGroups": dpSwPortGroups,
       "dpSwPortBasicGroup": dpSwPortBasicGroup}
)
