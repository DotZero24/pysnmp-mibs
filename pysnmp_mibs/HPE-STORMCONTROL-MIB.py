# SNMP MIB module (HPE-STORMCONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/HPE-STORMCONTROL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:34:15 2025
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

(hpVCSE_40Gb_F8_Module,) = mibBuilder.importSymbols(
    "HPSVRMGMT-OID",
    "hpVCSE-40Gb-F8-Module")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 enterprises,
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
    "enterprises",
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

hpeStormControl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 4110)
)
if mibBuilder.loadTexts:
    hpeStormControl.setRevisions(
        ("2015-06-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpeSynergyVCMIBObjects_ObjectIdentity = ObjectIdentity
hpeSynergyVCMIBObjects = _HpeSynergyVCMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1)
)
_HpeStormControlGroup_ObjectIdentity = ObjectIdentity
hpeStormControlGroup = _HpeStormControlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 1)
)


class _HpeStormControlSystemStatus_Type(Integer32):
    """Custom type hpeStormControlSystemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HpeStormControlSystemStatus_Type.__name__ = "Integer32"
_HpeStormControlSystemStatus_Object = MibScalar
hpeStormControlSystemStatus = _HpeStormControlSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 1, 1),
    _HpeStormControlSystemStatus_Type()
)
hpeStormControlSystemStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpeStormControlSystemStatus.setStatus("current")


class _HpeStormControlSystemRateLimitInPps_Type(Integer32):
    """Custom type hpeStormControlSystemRateLimitInPps based on Integer32"""
    defaultValue = 0


_HpeStormControlSystemRateLimitInPps_Type.__name__ = "Integer32"
_HpeStormControlSystemRateLimitInPps_Object = MibScalar
hpeStormControlSystemRateLimitInPps = _HpeStormControlSystemRateLimitInPps_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 1, 2),
    _HpeStormControlSystemRateLimitInPps_Type()
)
hpeStormControlSystemRateLimitInPps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpeStormControlSystemRateLimitInPps.setStatus("current")


class _HpeStormControlSystemPollingInterval_Type(Integer32):
    """Custom type hpeStormControlSystemPollingInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_HpeStormControlSystemPollingInterval_Type.__name__ = "Integer32"
_HpeStormControlSystemPollingInterval_Object = MibScalar
hpeStormControlSystemPollingInterval = _HpeStormControlSystemPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 1, 3),
    _HpeStormControlSystemPollingInterval_Type()
)
hpeStormControlSystemPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpeStormControlSystemPollingInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpeStormControlSystemPollingInterval.setUnits("Seconds")
_HpeStormControlStatsTable_Object = MibTable
hpeStormControlStatsTable = _HpeStormControlStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hpeStormControlStatsTable.setStatus("current")
_HpeStormControlStatsEntry_Object = MibTableRow
hpeStormControlStatsEntry = _HpeStormControlStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 1, 4, 1)
)
hpeStormControlStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpeStormControlStatsEntry.setStatus("current")
_HpeStormControlDLFDropCounters_Type = Counter32
_HpeStormControlDLFDropCounters_Object = MibTableColumn
hpeStormControlDLFDropCounters = _HpeStormControlDLFDropCounters_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 1, 4, 1, 1),
    _HpeStormControlDLFDropCounters_Type()
)
hpeStormControlDLFDropCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpeStormControlDLFDropCounters.setStatus("current")
_HpeStormControlMCASTDropCounters_Type = Counter32
_HpeStormControlMCASTDropCounters_Object = MibTableColumn
hpeStormControlMCASTDropCounters = _HpeStormControlMCASTDropCounters_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 1, 4, 1, 2),
    _HpeStormControlMCASTDropCounters_Type()
)
hpeStormControlMCASTDropCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpeStormControlMCASTDropCounters.setStatus("current")
_HpeStormControlBCASTDropCounters_Type = Counter32
_HpeStormControlBCASTDropCounters_Object = MibTableColumn
hpeStormControlBCASTDropCounters = _HpeStormControlBCASTDropCounters_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 1, 4, 1, 3),
    _HpeStormControlBCASTDropCounters_Type()
)
hpeStormControlBCASTDropCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpeStormControlBCASTDropCounters.setStatus("current")


class _HpeStormControlIfStatus_Type(Integer32):
    """Custom type hpeStormControlIfStatus based on Integer32"""
    defaultValue = 0


_HpeStormControlIfStatus_Type.__name__ = "Integer32"
_HpeStormControlIfStatus_Object = MibTableColumn
hpeStormControlIfStatus = _HpeStormControlIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 1, 4, 1, 4),
    _HpeStormControlIfStatus_Type()
)
hpeStormControlIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpeStormControlIfStatus.setStatus("current")
_HpeStormControlTrap_ObjectIdentity = ObjectIdentity
hpeStormControlTrap = _HpeStormControlTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 4110, 2)
)

# Managed Objects groups


# Notification objects

hpestormControlTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 4110, 2, 1)
)
hpestormControlTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HPE-STORMCONTROL-MIB", "hpeStormControlIfStatus"))
)
if mibBuilder.loadTexts:
    hpestormControlTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPE-STORMCONTROL-MIB",
    **{"hpeSynergyVCMIBObjects": hpeSynergyVCMIBObjects,
       "hpeStormControlGroup": hpeStormControlGroup,
       "hpeStormControlSystemStatus": hpeStormControlSystemStatus,
       "hpeStormControlSystemRateLimitInPps": hpeStormControlSystemRateLimitInPps,
       "hpeStormControlSystemPollingInterval": hpeStormControlSystemPollingInterval,
       "hpeStormControlStatsTable": hpeStormControlStatsTable,
       "hpeStormControlStatsEntry": hpeStormControlStatsEntry,
       "hpeStormControlDLFDropCounters": hpeStormControlDLFDropCounters,
       "hpeStormControlMCASTDropCounters": hpeStormControlMCASTDropCounters,
       "hpeStormControlBCASTDropCounters": hpeStormControlBCASTDropCounters,
       "hpeStormControlIfStatus": hpeStormControlIfStatus,
       "hpeStormControl": hpeStormControl,
       "hpeStormControlTrap": hpeStormControlTrap,
       "hpestormControlTrap": hpestormControlTrap}
)
