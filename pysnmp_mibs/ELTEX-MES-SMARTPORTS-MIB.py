# SNMP MIB module (ELTEX-MES-SMARTPORTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-SMARTPORTS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:48:38 2025
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

(eltMes,) = mibBuilder.importSymbols(
    "ELTEX-MES",
    "eltMes")

(rlSmartPortsMacroManageEntry,) = mibBuilder.importSymbols(
    "RADLAN-SMARTPORTS-MIB",
    "rlSmartPortsMacroManageEntry")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

eltMesSmartPorts = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 17)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesSmartPortsObjects_ObjectIdentity = ObjectIdentity
eltMesSmartPortsObjects = _EltMesSmartPortsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 17, 1)
)
_EltMesSmartPortsGlobals_ObjectIdentity = ObjectIdentity
eltMesSmartPortsGlobals = _EltMesSmartPortsGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 17, 1, 1)
)
_EltMesSmartPortsConfigs_ObjectIdentity = ObjectIdentity
eltMesSmartPortsConfigs = _EltMesSmartPortsConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 17, 1, 2)
)
_EltSmartPortsMacroManageTable_Object = MibTable
eltSmartPortsMacroManageTable = _EltSmartPortsMacroManageTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 17, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eltSmartPortsMacroManageTable.setStatus("current")
_EltSmartPortsMacroManageEntry_Object = MibTableRow
eltSmartPortsMacroManageEntry = _EltSmartPortsMacroManageEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 17, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    eltSmartPortsMacroManageEntry.setStatus("current")


class _EltSmartPortsMacroTrackObject_Type(Unsigned32):
    """Custom type eltSmartPortsMacroTrackObject based on Unsigned32"""
    defaultValue = 0


_EltSmartPortsMacroTrackObject_Type.__name__ = "Unsigned32"
_EltSmartPortsMacroTrackObject_Object = MibTableColumn
eltSmartPortsMacroTrackObject = _EltSmartPortsMacroTrackObject_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 17, 1, 2, 1, 1, 1),
    _EltSmartPortsMacroTrackObject_Type()
)
eltSmartPortsMacroTrackObject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltSmartPortsMacroTrackObject.setStatus("current")


class _EltSmartPortsMacroTrackActivationState_Type(Integer32):
    """Custom type eltSmartPortsMacroTrackActivationState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("up", 1),
          ("down", 2))
    )


_EltSmartPortsMacroTrackActivationState_Type.__name__ = "Integer32"
_EltSmartPortsMacroTrackActivationState_Object = MibTableColumn
eltSmartPortsMacroTrackActivationState = _EltSmartPortsMacroTrackActivationState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 17, 1, 2, 1, 1, 2),
    _EltSmartPortsMacroTrackActivationState_Type()
)
eltSmartPortsMacroTrackActivationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltSmartPortsMacroTrackActivationState.setStatus("current")
rlSmartPortsMacroManageEntry.registerAugmentions(
    ("ELTEX-MES-SMARTPORTS-MIB",
     "eltSmartPortsMacroManageEntry")
)
eltSmartPortsMacroManageEntry.setIndexNames(*rlSmartPortsMacroManageEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-SMARTPORTS-MIB",
    **{"eltMesSmartPorts": eltMesSmartPorts,
       "eltMesSmartPortsObjects": eltMesSmartPortsObjects,
       "eltMesSmartPortsGlobals": eltMesSmartPortsGlobals,
       "eltMesSmartPortsConfigs": eltMesSmartPortsConfigs,
       "eltSmartPortsMacroManageTable": eltSmartPortsMacroManageTable,
       "eltSmartPortsMacroManageEntry": eltSmartPortsMacroManageEntry,
       "eltSmartPortsMacroTrackObject": eltSmartPortsMacroTrackObject,
       "eltSmartPortsMacroTrackActivationState": eltSmartPortsMacroTrackActivationState}
)
