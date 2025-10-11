# SNMP MIB module (SL-OSW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/smartoptics/SL-OSW-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:11:21 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(slService,) = mibBuilder.importSymbols(
    "SL-NE-MIB",
    "slService")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

slOSW = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 17)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SlOSWConfig_ObjectIdentity = ObjectIdentity
slOSWConfig = _SlOSWConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 17, 1)
)
_SlOSWPortConfigTable_Object = MibTable
slOSWPortConfigTable = _SlOSWPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 17, 1, 1)
)
if mibBuilder.loadTexts:
    slOSWPortConfigTable.setStatus("current")
_SlOSWPortConfigEntry_Object = MibTableRow
slOSWPortConfigEntry = _SlOSWPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 17, 1, 1, 1)
)
slOSWPortConfigEntry.setIndexNames(
    (0, "SL-OSW-MIB", "slOSWPortConfigLineIndex"),
)
if mibBuilder.loadTexts:
    slOSWPortConfigEntry.setStatus("current")
_SlOSWPortConfigLineIndex_Type = InterfaceIndex
_SlOSWPortConfigLineIndex_Object = MibTableColumn
slOSWPortConfigLineIndex = _SlOSWPortConfigLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 17, 1, 1, 1, 1),
    _SlOSWPortConfigLineIndex_Type()
)
slOSWPortConfigLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOSWPortConfigLineIndex.setStatus("current")
_SlOSWPortConfigInPowerLevel_Type = Integer32
_SlOSWPortConfigInPowerLevel_Object = MibTableColumn
slOSWPortConfigInPowerLevel = _SlOSWPortConfigInPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 17, 1, 1, 1, 2),
    _SlOSWPortConfigInPowerLevel_Type()
)
slOSWPortConfigInPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOSWPortConfigInPowerLevel.setStatus("current")


class _SlOSWPortConfigLosThreshold_Type(Integer32):
    """Custom type slOSWPortConfigLosThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlOSWPortConfigLosThreshold_Type.__name__ = "Integer32"
_SlOSWPortConfigLosThreshold_Object = MibTableColumn
slOSWPortConfigLosThreshold = _SlOSWPortConfigLosThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 17, 1, 1, 1, 3),
    _SlOSWPortConfigLosThreshold_Type()
)
slOSWPortConfigLosThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slOSWPortConfigLosThreshold.setStatus("current")
_SlOSWPm_ObjectIdentity = ObjectIdentity
slOSWPm = _SlOSWPm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 17, 2)
)
_SlOSWTraps_ObjectIdentity = ObjectIdentity
slOSWTraps = _SlOSWTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 17, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SL-OSW-MIB",
    **{"slOSW": slOSW,
       "slOSWConfig": slOSWConfig,
       "slOSWPortConfigTable": slOSWPortConfigTable,
       "slOSWPortConfigEntry": slOSWPortConfigEntry,
       "slOSWPortConfigLineIndex": slOSWPortConfigLineIndex,
       "slOSWPortConfigInPowerLevel": slOSWPortConfigInPowerLevel,
       "slOSWPortConfigLosThreshold": slOSWPortConfigLosThreshold,
       "slOSWPm": slOSWPm,
       "slOSWTraps": slOSWTraps}
)
