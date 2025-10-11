# SNMP MIB module (INFINERA-ENTITY-FSE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-FSE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:32 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(equipment,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "equipment")

(InfnEqptType,) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "InfnEqptType")

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

fseMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 38)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FseTable_Object = MibTable
fseTable = _FseTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 38, 1)
)
if mibBuilder.loadTexts:
    fseTable.setStatus("current")
_FseEntry_Object = MibTableRow
fseEntry = _FseEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 38, 1, 1)
)
fseEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    fseEntry.setStatus("current")
_FseMoId_Type = DisplayString
_FseMoId_Object = MibTableColumn
fseMoId = _FseMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 38, 1, 1, 1),
    _FseMoId_Type()
)
fseMoId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fseMoId.setStatus("current")
_FseProvEqptType_Type = InfnEqptType
_FseProvEqptType_Object = MibTableColumn
fseProvEqptType = _FseProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 38, 1, 1, 2),
    _FseProvEqptType_Type()
)
fseProvEqptType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fseProvEqptType.setStatus("current")


class _FseOlosSoakTime_Type(Integer32):
    """Custom type fseOlosSoakTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fast", 1),
          ("medium", 2),
          ("long", 3))
    )


_FseOlosSoakTime_Type.__name__ = "Integer32"
_FseOlosSoakTime_Object = MibTableColumn
fseOlosSoakTime = _FseOlosSoakTime_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 38, 1, 1, 3),
    _FseOlosSoakTime_Type()
)
fseOlosSoakTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fseOlosSoakTime.setStatus("current")
_FseIsPathLossCheckInvoked_Type = TruthValue
_FseIsPathLossCheckInvoked_Object = MibTableColumn
fseIsPathLossCheckInvoked = _FseIsPathLossCheckInvoked_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 38, 1, 1, 4),
    _FseIsPathLossCheckInvoked_Type()
)
fseIsPathLossCheckInvoked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fseIsPathLossCheckInvoked.setStatus("current")
_FsePathLossInvokedPortAid_Type = DisplayString
_FsePathLossInvokedPortAid_Object = MibTableColumn
fsePathLossInvokedPortAid = _FsePathLossInvokedPortAid_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 38, 1, 1, 5),
    _FsePathLossInvokedPortAid_Type()
)
fsePathLossInvokedPortAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsePathLossInvokedPortAid.setStatus("current")
_FseConffseance_ObjectIdentity = ObjectIdentity
fseConffseance = _FseConffseance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 38, 3)
)
_FseCompliances_ObjectIdentity = ObjectIdentity
fseCompliances = _FseCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 38, 3, 1)
)
_FseGroups_ObjectIdentity = ObjectIdentity
fseGroups = _FseGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 38, 3, 2)
)

# Managed Objects groups

fseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 38, 3, 2, 1)
)
fseGroup.setObjects(
      *(("INFINERA-ENTITY-FSE-MIB", "fseMoId"),
        ("INFINERA-ENTITY-FSE-MIB", "fseProvEqptType"),
        ("INFINERA-ENTITY-FSE-MIB", "fseOlosSoakTime"),
        ("INFINERA-ENTITY-FSE-MIB", "fseIsPathLossCheckInvoked"),
        ("INFINERA-ENTITY-FSE-MIB", "fsePathLossInvokedPortAid"))
)
if mibBuilder.loadTexts:
    fseGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fseCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 38, 3, 1, 1)
)
fseCompliance.setObjects(
    ("INFINERA-ENTITY-FSE-MIB", "fseGroup")
)
if mibBuilder.loadTexts:
    fseCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-FSE-MIB",
    **{"fseMIB": fseMIB,
       "fseTable": fseTable,
       "fseEntry": fseEntry,
       "fseMoId": fseMoId,
       "fseProvEqptType": fseProvEqptType,
       "fseOlosSoakTime": fseOlosSoakTime,
       "fseIsPathLossCheckInvoked": fseIsPathLossCheckInvoked,
       "fsePathLossInvokedPortAid": fsePathLossInvokedPortAid,
       "fseConffseance": fseConffseance,
       "fseCompliances": fseCompliances,
       "fseCompliance": fseCompliance,
       "fseGroups": fseGroups,
       "fseGroup": fseGroup}
)
