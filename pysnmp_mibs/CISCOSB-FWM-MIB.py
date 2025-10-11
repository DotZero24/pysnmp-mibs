# SNMP MIB module (CISCOSB-FWM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ciscosb/CISCOSB-FWM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:41:55 2025
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

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

rlFwm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 244)
)
if mibBuilder.loadTexts:
    rlFwm.setRevisions(
        ("2006-02-12 00:00",
         "2003-10-18 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EntityType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-relevant", 0),
          ("cpld", 1),
          ("fpga", 2))
    )



# MIB Managed Objects in the order of their OIDs

_RlFwmTable_Object = MibTable
rlFwmTable = _RlFwmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 244, 1)
)
if mibBuilder.loadTexts:
    rlFwmTable.setStatus("current")
_RlFwmEntry_Object = MibTableRow
rlFwmEntry = _RlFwmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 244, 1, 1)
)
rlFwmEntry.setIndexNames(
    (0, "CISCOSB-FWM-MIB", "rlFwmUnitIndex"),
    (0, "CISCOSB-FWM-MIB", "rlFwmEntity"),
    (0, "CISCOSB-FWM-MIB", "rlFwmIndex"),
)
if mibBuilder.loadTexts:
    rlFwmEntry.setStatus("current")
_RlFwmUnitIndex_Type = Integer32
_RlFwmUnitIndex_Object = MibTableColumn
rlFwmUnitIndex = _RlFwmUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 244, 1, 1, 1),
    _RlFwmUnitIndex_Type()
)
rlFwmUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlFwmUnitIndex.setStatus("current")
_RlFwmEntity_Type = EntityType
_RlFwmEntity_Object = MibTableColumn
rlFwmEntity = _RlFwmEntity_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 244, 1, 1, 2),
    _RlFwmEntity_Type()
)
rlFwmEntity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlFwmEntity.setStatus("current")
_RlFwmIndex_Type = Integer32
_RlFwmIndex_Object = MibTableColumn
rlFwmIndex = _RlFwmIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 244, 1, 1, 3),
    _RlFwmIndex_Type()
)
rlFwmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlFwmIndex.setStatus("current")
_RlFwmVersionActive_Type = DisplayString
_RlFwmVersionActive_Object = MibTableColumn
rlFwmVersionActive = _RlFwmVersionActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 244, 1, 1, 4),
    _RlFwmVersionActive_Type()
)
rlFwmVersionActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFwmVersionActive.setStatus("current")
_RlFwmVersionInactive_Type = DisplayString
_RlFwmVersionInactive_Object = MibTableColumn
rlFwmVersionInactive = _RlFwmVersionInactive_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 244, 1, 1, 5),
    _RlFwmVersionInactive_Type()
)
rlFwmVersionInactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFwmVersionInactive.setStatus("current")
_RlFwmUpdateAvailable_Type = TruthValue
_RlFwmUpdateAvailable_Object = MibTableColumn
rlFwmUpdateAvailable = _RlFwmUpdateAvailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 244, 1, 1, 6),
    _RlFwmUpdateAvailable_Type()
)
rlFwmUpdateAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFwmUpdateAvailable.setStatus("current")
_RlFwmForceAutoUpdate_Type = TruthValue
_RlFwmForceAutoUpdate_Object = MibTableColumn
rlFwmForceAutoUpdate = _RlFwmForceAutoUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 244, 1, 1, 7),
    _RlFwmForceAutoUpdate_Type()
)
rlFwmForceAutoUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFwmForceAutoUpdate.setStatus("current")
_RlFwmVersionUpdate_Type = EntityType
_RlFwmVersionUpdate_Object = MibScalar
rlFwmVersionUpdate = _RlFwmVersionUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 244, 2),
    _RlFwmVersionUpdate_Type()
)
rlFwmVersionUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFwmVersionUpdate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-FWM-MIB",
    **{"EntityType": EntityType,
       "rlFwm": rlFwm,
       "rlFwmTable": rlFwmTable,
       "rlFwmEntry": rlFwmEntry,
       "rlFwmUnitIndex": rlFwmUnitIndex,
       "rlFwmEntity": rlFwmEntity,
       "rlFwmIndex": rlFwmIndex,
       "rlFwmVersionActive": rlFwmVersionActive,
       "rlFwmVersionInactive": rlFwmVersionInactive,
       "rlFwmUpdateAvailable": rlFwmUpdateAvailable,
       "rlFwmForceAutoUpdate": rlFwmForceAutoUpdate,
       "rlFwmVersionUpdate": rlFwmVersionUpdate}
)
