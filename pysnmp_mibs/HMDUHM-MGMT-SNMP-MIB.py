# SNMP MIB module (HMDUHM-MGMT-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hirschmann/HMDUHM-MGMT-SNMP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:56:15 2025
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

(hmConfiguration,) = mibBuilder.importSymbols(
    "HMPRIV-MGMT-SNMP-MIB",
    "hmConfiguration")

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
 enterprises,
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

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

_HmDualHoming_ObjectIdentity = ObjectIdentity
hmDualHoming = _HmDualHoming_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 4)
)
_HmDualHomingTable_Object = MibTable
hmDualHomingTable = _HmDualHomingTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 4, 1)
)
if mibBuilder.loadTexts:
    hmDualHomingTable.setStatus("mandatory")
_HmDuHmEntry_Object = MibTableRow
hmDuHmEntry = _HmDuHmEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 4, 1, 1)
)
hmDuHmEntry.setIndexNames(
    (0, "HMDUHM-MGMT-SNMP-MIB", "hmDuHmPrimGroupID"),
    (0, "HMDUHM-MGMT-SNMP-MIB", "hmDuHmPrimIfIndex"),
)
if mibBuilder.loadTexts:
    hmDuHmEntry.setStatus("mandatory")


class _HmDuHmPrimGroupID_Type(Integer32):
    """Custom type hmDuHmPrimGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_HmDuHmPrimGroupID_Type.__name__ = "Integer32"
_HmDuHmPrimGroupID_Object = MibTableColumn
hmDuHmPrimGroupID = _HmDuHmPrimGroupID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 4, 1, 1, 1),
    _HmDuHmPrimGroupID_Type()
)
hmDuHmPrimGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDuHmPrimGroupID.setStatus("mandatory")


class _HmDuHmPrimIfIndex_Type(Integer32):
    """Custom type hmDuHmPrimIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_HmDuHmPrimIfIndex_Type.__name__ = "Integer32"
_HmDuHmPrimIfIndex_Object = MibTableColumn
hmDuHmPrimIfIndex = _HmDuHmPrimIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 4, 1, 1, 2),
    _HmDuHmPrimIfIndex_Type()
)
hmDuHmPrimIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDuHmPrimIfIndex.setStatus("mandatory")


class _HmDuHmPrimIfOpState_Type(Integer32):
    """Custom type hmDuHmPrimIfOpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 1),
          ("active", 2),
          ("active-by-mgmt", 3),
          ("inactive-by-mgmt", 4),
          ("inactive", 5),
          ("absent", 6))
    )


_HmDuHmPrimIfOpState_Type.__name__ = "Integer32"
_HmDuHmPrimIfOpState_Object = MibTableColumn
hmDuHmPrimIfOpState = _HmDuHmPrimIfOpState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 4, 1, 1, 3),
    _HmDuHmPrimIfOpState_Type()
)
hmDuHmPrimIfOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDuHmPrimIfOpState.setStatus("mandatory")
_HmDuHmRedGroupID_Type = Integer32
_HmDuHmRedGroupID_Object = MibTableColumn
hmDuHmRedGroupID = _HmDuHmRedGroupID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 4, 1, 1, 4),
    _HmDuHmRedGroupID_Type()
)
hmDuHmRedGroupID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmDuHmRedGroupID.setStatus("mandatory")
_HmDuHmRedIfIndex_Type = Integer32
_HmDuHmRedIfIndex_Object = MibTableColumn
hmDuHmRedIfIndex = _HmDuHmRedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 4, 1, 1, 5),
    _HmDuHmRedIfIndex_Type()
)
hmDuHmRedIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmDuHmRedIfIndex.setStatus("mandatory")


class _HmDuHmRedIfOpState_Type(Integer32):
    """Custom type hmDuHmRedIfOpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 1),
          ("active", 2),
          ("active-by-mgmt", 3),
          ("inactive-by-mgmt", 4),
          ("inactive", 5),
          ("absent", 6))
    )


_HmDuHmRedIfOpState_Type.__name__ = "Integer32"
_HmDuHmRedIfOpState_Object = MibTableColumn
hmDuHmRedIfOpState = _HmDuHmRedIfOpState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 4, 1, 1, 6),
    _HmDuHmRedIfOpState_Type()
)
hmDuHmRedIfOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDuHmRedIfOpState.setStatus("mandatory")


class _HmDuHmDesiredAction_Type(Integer32):
    """Custom type hmDuHmDesiredAction based on Integer32"""
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
        *(("create", 1),
          ("deactivate", 2),
          ("activate", 3),
          ("delete", 4))
    )


_HmDuHmDesiredAction_Type.__name__ = "Integer32"
_HmDuHmDesiredAction_Object = MibTableColumn
hmDuHmDesiredAction = _HmDuHmDesiredAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 4, 1, 1, 7),
    _HmDuHmDesiredAction_Type()
)
hmDuHmDesiredAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmDuHmDesiredAction.setStatus("mandatory")


class _HmDuHmOperState_Type(Integer32):
    """Custom type hmDuHmOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("underCreation", 1),
          ("checking", 2),
          ("active", 3),
          ("inactive", 4),
          ("invalid", 5),
          ("OutOfOrder", 6))
    )


_HmDuHmOperState_Type.__name__ = "Integer32"
_HmDuHmOperState_Object = MibTableColumn
hmDuHmOperState = _HmDuHmOperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 4, 1, 1, 8),
    _HmDuHmOperState_Type()
)
hmDuHmOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDuHmOperState.setStatus("mandatory")
_HmDuHmPortRevivalDelay_Type = Integer32
_HmDuHmPortRevivalDelay_Object = MibTableColumn
hmDuHmPortRevivalDelay = _HmDuHmPortRevivalDelay_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 4, 1, 1, 9),
    _HmDuHmPortRevivalDelay_Type()
)
hmDuHmPortRevivalDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmDuHmPortRevivalDelay.setStatus("mandatory")


class _HmDuHmLinkMode_Type(Integer32):
    """Custom type hmDuHmLinkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("physical", 1),
          ("layer2Frames", 2))
    )


_HmDuHmLinkMode_Type.__name__ = "Integer32"
_HmDuHmLinkMode_Object = MibTableColumn
hmDuHmLinkMode = _HmDuHmLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 4, 1, 1, 10),
    _HmDuHmLinkMode_Type()
)
hmDuHmLinkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmDuHmLinkMode.setStatus("mandatory")


class _HmDuHmRedCheckEnable_Type(Integer32):
    """Custom type hmDuHmRedCheckEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_HmDuHmRedCheckEnable_Type.__name__ = "Integer32"
_HmDuHmRedCheckEnable_Object = MibTableColumn
hmDuHmRedCheckEnable = _HmDuHmRedCheckEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 4, 1, 1, 11),
    _HmDuHmRedCheckEnable_Type()
)
hmDuHmRedCheckEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmDuHmRedCheckEnable.setStatus("mandatory")


class _HmDuHmRedCheckState_Type(Integer32):
    """Custom type hmDuHmRedCheckState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("failed", 2))
    )


_HmDuHmRedCheckState_Type.__name__ = "Integer32"
_HmDuHmRedCheckState_Object = MibTableColumn
hmDuHmRedCheckState = _HmDuHmRedCheckState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 4, 1, 1, 12),
    _HmDuHmRedCheckState_Type()
)
hmDuHmRedCheckState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDuHmRedCheckState.setStatus("mandatory")

# Managed Objects groups


# Notification objects

hmDuHmReconfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 4, 0, 1)
)
hmDuHmReconfig.setObjects(
      *(("HMDUHM-MGMT-SNMP-MIB", "hmDuHmPrimGroupID"),
        ("HMDUHM-MGMT-SNMP-MIB", "hmDuHmPrimIfIndex"),
        ("HMDUHM-MGMT-SNMP-MIB", "hmDuHmPrimIfOpState"),
        ("HMDUHM-MGMT-SNMP-MIB", "hmDuHmRedGroupID"),
        ("HMDUHM-MGMT-SNMP-MIB", "hmDuHmRedIfIndex"),
        ("HMDUHM-MGMT-SNMP-MIB", "hmDuHmRedIfOpState"))
)
if mibBuilder.loadTexts:
    hmDuHmReconfig.setStatus(
        ""
    )

hmDuHmRedundancy = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 4, 0, 2)
)
hmDuHmRedundancy.setObjects(
    ("HMDUHM-MGMT-SNMP-MIB", "hmDuHmRedCheckState")
)
if mibBuilder.loadTexts:
    hmDuHmRedundancy.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HMDUHM-MGMT-SNMP-MIB",
    **{"hmDualHoming": hmDualHoming,
       "hmDuHmReconfig": hmDuHmReconfig,
       "hmDuHmRedundancy": hmDuHmRedundancy,
       "hmDualHomingTable": hmDualHomingTable,
       "hmDuHmEntry": hmDuHmEntry,
       "hmDuHmPrimGroupID": hmDuHmPrimGroupID,
       "hmDuHmPrimIfIndex": hmDuHmPrimIfIndex,
       "hmDuHmPrimIfOpState": hmDuHmPrimIfOpState,
       "hmDuHmRedGroupID": hmDuHmRedGroupID,
       "hmDuHmRedIfIndex": hmDuHmRedIfIndex,
       "hmDuHmRedIfOpState": hmDuHmRedIfOpState,
       "hmDuHmDesiredAction": hmDuHmDesiredAction,
       "hmDuHmOperState": hmDuHmOperState,
       "hmDuHmPortRevivalDelay": hmDuHmPortRevivalDelay,
       "hmDuHmLinkMode": hmDuHmLinkMode,
       "hmDuHmRedCheckEnable": hmDuHmRedCheckEnable,
       "hmDuHmRedCheckState": hmDuHmRedCheckState}
)
