# SNMP MIB module (ELTEX-MES-STORMCTRL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-STORMCTRL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:50:37 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(rlStormCtrlRateLimCfgEntry,) = mibBuilder.importSymbols(
    "RADLAN-STORMCTRL-MIB",
    "rlStormCtrlRateLimCfgEntry")

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

eltMesStormCtrl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 77)
)
if mibBuilder.loadTexts:
    eltMesStormCtrl.setRevisions(
        ("2015-10-29 00:00",
         "2014-12-30 00:00")
    )


# Types definitions



class EltStormCtrlActionType(Integer32):
    """Custom type EltStormCtrlActionType based on Integer32"""
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
        *(("none", 1),
          ("trap", 2),
          ("shutdown", 3),
          ("trapAndShutdown", 4))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesStormCtrlMIBObjects_ObjectIdentity = ObjectIdentity
eltMesStormCtrlMIBObjects = _EltMesStormCtrlMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 77, 1)
)
_EltMesStormCtrlConfig_ObjectIdentity = ObjectIdentity
eltMesStormCtrlConfig = _EltMesStormCtrlConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 77, 1, 1)
)
_EltStormCtrlRateLimCfgTable_Object = MibTable
eltStormCtrlRateLimCfgTable = _EltStormCtrlRateLimCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 77, 1, 1, 3)
)
if mibBuilder.loadTexts:
    eltStormCtrlRateLimCfgTable.setStatus("current")
_EltStormCtrlRateLimCfgEntry_Object = MibTableRow
eltStormCtrlRateLimCfgEntry = _EltStormCtrlRateLimCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 77, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    eltStormCtrlRateLimCfgEntry.setStatus("current")
_EltStormCtrlRateLimCfgPpsAction_Type = EltStormCtrlActionType
_EltStormCtrlRateLimCfgPpsAction_Object = MibTableColumn
eltStormCtrlRateLimCfgPpsAction = _EltStormCtrlRateLimCfgPpsAction_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 77, 1, 1, 3, 1, 1),
    _EltStormCtrlRateLimCfgPpsAction_Type()
)
eltStormCtrlRateLimCfgPpsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltStormCtrlRateLimCfgPpsAction.setStatus("current")


class _EltStormCtrlRateLimCfgRatePps_Type(Unsigned32):
    """Custom type eltStormCtrlRateLimCfgRatePps based on Unsigned32"""
    defaultValue = 0


_EltStormCtrlRateLimCfgRatePps_Type.__name__ = "Unsigned32"
_EltStormCtrlRateLimCfgRatePps_Object = MibTableColumn
eltStormCtrlRateLimCfgRatePps = _EltStormCtrlRateLimCfgRatePps_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 77, 1, 1, 3, 1, 2),
    _EltStormCtrlRateLimCfgRatePps_Type()
)
eltStormCtrlRateLimCfgRatePps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltStormCtrlRateLimCfgRatePps.setStatus("current")


class _EltStormCtrlRateLimCfgBurstSizePackets_Type(Unsigned32):
    """Custom type eltStormCtrlRateLimCfgBurstSizePackets based on Unsigned32"""
    defaultValue = 0


_EltStormCtrlRateLimCfgBurstSizePackets_Type.__name__ = "Unsigned32"
_EltStormCtrlRateLimCfgBurstSizePackets_Object = MibTableColumn
eltStormCtrlRateLimCfgBurstSizePackets = _EltStormCtrlRateLimCfgBurstSizePackets_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 77, 1, 1, 3, 1, 3),
    _EltStormCtrlRateLimCfgBurstSizePackets_Type()
)
eltStormCtrlRateLimCfgBurstSizePackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltStormCtrlRateLimCfgBurstSizePackets.setStatus("current")
rlStormCtrlRateLimCfgEntry.registerAugmentions(
    ("ELTEX-MES-STORMCTRL-MIB",
     "eltStormCtrlRateLimCfgEntry")
)
eltStormCtrlRateLimCfgEntry.setIndexNames(*rlStormCtrlRateLimCfgEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-STORMCTRL-MIB",
    **{"EltStormCtrlActionType": EltStormCtrlActionType,
       "eltMesStormCtrl": eltMesStormCtrl,
       "eltMesStormCtrlMIBObjects": eltMesStormCtrlMIBObjects,
       "eltMesStormCtrlConfig": eltMesStormCtrlConfig,
       "eltStormCtrlRateLimCfgTable": eltStormCtrlRateLimCfgTable,
       "eltStormCtrlRateLimCfgEntry": eltStormCtrlRateLimCfgEntry,
       "eltStormCtrlRateLimCfgPpsAction": eltStormCtrlRateLimCfgPpsAction,
       "eltStormCtrlRateLimCfgRatePps": eltStormCtrlRateLimCfgRatePps,
       "eltStormCtrlRateLimCfgBurstSizePackets": eltStormCtrlRateLimCfgBurstSizePackets}
)
