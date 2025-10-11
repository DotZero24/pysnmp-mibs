# SNMP MIB module (G6-MAC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/microsens/G6-MAC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:13 2025
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

(g6,) = mibBuilder.importSymbols(
    "MICROSENS-G6-MIB",
    "g6")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

device = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1)
)
if mibBuilder.loadTexts:
    device.setRevisions(
        ("2018-02-12 16:19",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mac_ObjectIdentity = ObjectIdentity
mac = _Mac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 86)
)
_MacFilterPort_Type = DisplayString
_MacFilterPort_Object = MibScalar
macFilterPort = _MacFilterPort_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 86, 1),
    _MacFilterPort_Type()
)
macFilterPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFilterPort.setStatus("current")
_MacFilterUserPorts_Type = DisplayString
_MacFilterUserPorts_Object = MibScalar
macFilterUserPorts = _MacFilterUserPorts_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 86, 2),
    _MacFilterUserPorts_Type()
)
macFilterUserPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFilterUserPorts.setStatus("current")
_MacFilterVlan_Type = DisplayString
_MacFilterVlan_Object = MibScalar
macFilterVlan = _MacFilterVlan_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 86, 3),
    _MacFilterVlan_Type()
)
macFilterVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFilterVlan.setStatus("current")
_MacFilterMac_Type = DisplayString
_MacFilterMac_Object = MibScalar
macFilterMac = _MacFilterMac_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 86, 4),
    _MacFilterMac_Type()
)
macFilterMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFilterMac.setStatus("current")
_MacFilterCustom_Type = DisplayString
_MacFilterCustom_Object = MibScalar
macFilterCustom = _MacFilterCustom_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 86, 5),
    _MacFilterCustom_Type()
)
macFilterCustom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFilterCustom.setStatus("current")
_MacFilterMulticastVlan_Type = DisplayString
_MacFilterMulticastVlan_Object = MibScalar
macFilterMulticastVlan = _MacFilterMulticastVlan_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 86, 6),
    _MacFilterMulticastVlan_Type()
)
macFilterMulticastVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFilterMulticastVlan.setStatus("current")
_MacFilterMulticastPort_Type = DisplayString
_MacFilterMulticastPort_Object = MibScalar
macFilterMulticastPort = _MacFilterMulticastPort_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 86, 7),
    _MacFilterMulticastPort_Type()
)
macFilterMulticastPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFilterMulticastPort.setStatus("current")
_MacClearLearnedMacTable_Type = DisplayString
_MacClearLearnedMacTable_Object = MibScalar
macClearLearnedMacTable = _MacClearLearnedMacTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 86, 8),
    _MacClearLearnedMacTable_Type()
)
macClearLearnedMacTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macClearLearnedMacTable.setStatus("current")
_MacClearMacTableForVlan_Type = DisplayString
_MacClearMacTableForVlan_Object = MibScalar
macClearMacTableForVlan = _MacClearMacTableForVlan_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 86, 9),
    _MacClearMacTableForVlan_Type()
)
macClearMacTableForVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macClearMacTableForVlan.setStatus("current")


class _MacHideMacsOnLinkPorts_Type(Integer32):
    """Custom type macHideMacsOnLinkPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MacHideMacsOnLinkPorts_Type.__name__ = "Integer32"
_MacHideMacsOnLinkPorts_Object = MibScalar
macHideMacsOnLinkPorts = _MacHideMacsOnLinkPorts_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 86, 10),
    _MacHideMacsOnLinkPorts_Type()
)
macHideMacsOnLinkPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macHideMacsOnLinkPorts.setStatus("current")


class _MacGlobalAgingTime_Type(Integer32):
    """Custom type macGlobalAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MacGlobalAgingTime_Type.__name__ = "Integer32"
_MacGlobalAgingTime_Object = MibScalar
macGlobalAgingTime = _MacGlobalAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 86, 11),
    _MacGlobalAgingTime_Type()
)
macGlobalAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macGlobalAgingTime.setStatus("current")


class _MacNumberOfEntries_Type(Integer32):
    """Custom type macNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MacNumberOfEntries_Type.__name__ = "Integer32"
_MacNumberOfEntries_Object = MibScalar
macNumberOfEntries = _MacNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 86, 100),
    _MacNumberOfEntries_Type()
)
macNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macNumberOfEntries.setStatus("current")


class _MacNumberOfIgmpEntries_Type(Integer32):
    """Custom type macNumberOfIgmpEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MacNumberOfIgmpEntries_Type.__name__ = "Integer32"
_MacNumberOfIgmpEntries_Object = MibScalar
macNumberOfIgmpEntries = _MacNumberOfIgmpEntries_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 86, 101),
    _MacNumberOfIgmpEntries_Type()
)
macNumberOfIgmpEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macNumberOfIgmpEntries.setStatus("current")


class _MacUsedAgingTime_Type(Integer32):
    """Custom type macUsedAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MacUsedAgingTime_Type.__name__ = "Integer32"
_MacUsedAgingTime_Object = MibScalar
macUsedAgingTime = _MacUsedAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 86, 102),
    _MacUsedAgingTime_Type()
)
macUsedAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macUsedAgingTime.setStatus("current")


class _MacNumberOfHiddenEntires_Type(Integer32):
    """Custom type macNumberOfHiddenEntires based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MacNumberOfHiddenEntires_Type.__name__ = "Integer32"
_MacNumberOfHiddenEntires_Object = MibScalar
macNumberOfHiddenEntires = _MacNumberOfHiddenEntires_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 86, 103),
    _MacNumberOfHiddenEntires_Type()
)
macNumberOfHiddenEntires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macNumberOfHiddenEntires.setStatus("current")
_MacTableTable_Object = MibTable
macTableTable = _MacTableTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 86, 104)
)
if mibBuilder.loadTexts:
    macTableTable.setStatus("current")
_MacTableEntry_Object = MibTableRow
macTableEntry = _MacTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 86, 104, 1)
)
macTableEntry.setIndexNames(
    (0, "G6-MAC-MIB", "macTableIndex"),
)
if mibBuilder.loadTexts:
    macTableEntry.setStatus("current")


class _MacTableIndex_Type(Integer32):
    """Custom type macTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_MacTableIndex_Type.__name__ = "Integer32"
_MacTableIndex_Object = MibTableColumn
macTableIndex = _MacTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 86, 104, 1, 1),
    _MacTableIndex_Type()
)
macTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    macTableIndex.setStatus("current")
_MacTableMac_Type = MacAddress
_MacTableMac_Object = MibTableColumn
macTableMac = _MacTableMac_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 86, 104, 1, 2),
    _MacTableMac_Type()
)
macTableMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macTableMac.setStatus("current")


class _MacTablePort_Type(Integer32):
    """Custom type macTablePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MacTablePort_Type.__name__ = "Integer32"
_MacTablePort_Object = MibTableColumn
macTablePort = _MacTablePort_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 86, 104, 1, 3),
    _MacTablePort_Type()
)
macTablePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macTablePort.setStatus("current")


class _MacTableState_Type(Integer32):
    """Custom type macTableState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unused", 0),
          ("other", 1),
          ("invalid", 2),
          ("learned", 3),
          ("self", 4),
          ("pacc", 5),
          ("multicast", 6))
    )


_MacTableState_Type.__name__ = "Integer32"
_MacTableState_Object = MibTableColumn
macTableState = _MacTableState_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 86, 104, 1, 4),
    _MacTableState_Type()
)
macTableState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macTableState.setStatus("current")


class _MacTableVlan_Type(Integer32):
    """Custom type macTableVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MacTableVlan_Type.__name__ = "Integer32"
_MacTableVlan_Object = MibTableColumn
macTableVlan = _MacTableVlan_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 86, 104, 1, 5),
    _MacTableVlan_Type()
)
macTableVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macTableVlan.setStatus("current")
_CurrentlyAuthorizedMacsTable_Object = MibTable
currentlyAuthorizedMacsTable = _CurrentlyAuthorizedMacsTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 86, 105)
)
if mibBuilder.loadTexts:
    currentlyAuthorizedMacsTable.setStatus("current")
_CurrentlyAuthorizedMacsEntry_Object = MibTableRow
currentlyAuthorizedMacsEntry = _CurrentlyAuthorizedMacsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 86, 105, 1)
)
currentlyAuthorizedMacsEntry.setIndexNames(
    (0, "G6-MAC-MIB", "currentlyAuthorizedMacsIndex"),
)
if mibBuilder.loadTexts:
    currentlyAuthorizedMacsEntry.setStatus("current")


class _CurrentlyAuthorizedMacsIndex_Type(Integer32):
    """Custom type currentlyAuthorizedMacsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CurrentlyAuthorizedMacsIndex_Type.__name__ = "Integer32"
_CurrentlyAuthorizedMacsIndex_Object = MibTableColumn
currentlyAuthorizedMacsIndex = _CurrentlyAuthorizedMacsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 86, 105, 1, 1),
    _CurrentlyAuthorizedMacsIndex_Type()
)
currentlyAuthorizedMacsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    currentlyAuthorizedMacsIndex.setStatus("current")
_CurrentlyAuthorizedMacsMac_Type = MacAddress
_CurrentlyAuthorizedMacsMac_Object = MibTableColumn
currentlyAuthorizedMacsMac = _CurrentlyAuthorizedMacsMac_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 86, 105, 1, 2),
    _CurrentlyAuthorizedMacsMac_Type()
)
currentlyAuthorizedMacsMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentlyAuthorizedMacsMac.setStatus("current")


class _CurrentlyAuthorizedMacsPort_Type(Integer32):
    """Custom type currentlyAuthorizedMacsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CurrentlyAuthorizedMacsPort_Type.__name__ = "Integer32"
_CurrentlyAuthorizedMacsPort_Object = MibTableColumn
currentlyAuthorizedMacsPort = _CurrentlyAuthorizedMacsPort_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 86, 105, 1, 3),
    _CurrentlyAuthorizedMacsPort_Type()
)
currentlyAuthorizedMacsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentlyAuthorizedMacsPort.setStatus("current")


class _CurrentlyAuthorizedMacsState_Type(Integer32):
    """Custom type currentlyAuthorizedMacsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unused", 0),
          ("other", 1),
          ("invalid", 2),
          ("learned", 3),
          ("self", 4),
          ("pacc", 5),
          ("multicast", 6))
    )


_CurrentlyAuthorizedMacsState_Type.__name__ = "Integer32"
_CurrentlyAuthorizedMacsState_Object = MibTableColumn
currentlyAuthorizedMacsState = _CurrentlyAuthorizedMacsState_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 86, 105, 1, 4),
    _CurrentlyAuthorizedMacsState_Type()
)
currentlyAuthorizedMacsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentlyAuthorizedMacsState.setStatus("current")


class _CurrentlyAuthorizedMacsVlan_Type(Integer32):
    """Custom type currentlyAuthorizedMacsVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CurrentlyAuthorizedMacsVlan_Type.__name__ = "Integer32"
_CurrentlyAuthorizedMacsVlan_Object = MibTableColumn
currentlyAuthorizedMacsVlan = _CurrentlyAuthorizedMacsVlan_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 86, 105, 1, 5),
    _CurrentlyAuthorizedMacsVlan_Type()
)
currentlyAuthorizedMacsVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentlyAuthorizedMacsVlan.setStatus("current")


class _CurrentlyAuthorizedMacsDatabase_Type(Integer32):
    """Custom type currentlyAuthorizedMacsDatabase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CurrentlyAuthorizedMacsDatabase_Type.__name__ = "Integer32"
_CurrentlyAuthorizedMacsDatabase_Object = MibTableColumn
currentlyAuthorizedMacsDatabase = _CurrentlyAuthorizedMacsDatabase_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 86, 105, 1, 6),
    _CurrentlyAuthorizedMacsDatabase_Type()
)
currentlyAuthorizedMacsDatabase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentlyAuthorizedMacsDatabase.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "G6-MAC-MIB",
    **{"device": device,
       "mac": mac,
       "macFilterPort": macFilterPort,
       "macFilterUserPorts": macFilterUserPorts,
       "macFilterVlan": macFilterVlan,
       "macFilterMac": macFilterMac,
       "macFilterCustom": macFilterCustom,
       "macFilterMulticastVlan": macFilterMulticastVlan,
       "macFilterMulticastPort": macFilterMulticastPort,
       "macClearLearnedMacTable": macClearLearnedMacTable,
       "macClearMacTableForVlan": macClearMacTableForVlan,
       "macHideMacsOnLinkPorts": macHideMacsOnLinkPorts,
       "macGlobalAgingTime": macGlobalAgingTime,
       "macNumberOfEntries": macNumberOfEntries,
       "macNumberOfIgmpEntries": macNumberOfIgmpEntries,
       "macUsedAgingTime": macUsedAgingTime,
       "macNumberOfHiddenEntires": macNumberOfHiddenEntires,
       "macTableTable": macTableTable,
       "macTableEntry": macTableEntry,
       "macTableIndex": macTableIndex,
       "macTableMac": macTableMac,
       "macTablePort": macTablePort,
       "macTableState": macTableState,
       "macTableVlan": macTableVlan,
       "currentlyAuthorizedMacsTable": currentlyAuthorizedMacsTable,
       "currentlyAuthorizedMacsEntry": currentlyAuthorizedMacsEntry,
       "currentlyAuthorizedMacsIndex": currentlyAuthorizedMacsIndex,
       "currentlyAuthorizedMacsMac": currentlyAuthorizedMacsMac,
       "currentlyAuthorizedMacsPort": currentlyAuthorizedMacsPort,
       "currentlyAuthorizedMacsState": currentlyAuthorizedMacsState,
       "currentlyAuthorizedMacsVlan": currentlyAuthorizedMacsVlan,
       "currentlyAuthorizedMacsDatabase": currentlyAuthorizedMacsDatabase}
)
