# SNMP MIB module (OA-FRONT-PANEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/OA-FRONT-PANEL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:05:14 2025
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

(nbSwitchG1Il,) = mibBuilder.importSymbols(
    "OS-COMMON-TC-MIB",
    "nbSwitchG1Il")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

oaFrPanel = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 20)
)
if mibBuilder.loadTexts:
    oaFrPanel.setRevisions(
        ("2008-06-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NbDevId_ObjectIdentity = ObjectIdentity
nbDevId = _NbDevId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16)
)
_OaFrPanelGen_ObjectIdentity = ObjectIdentity
oaFrPanelGen = _OaFrPanelGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 20, 1)
)


class _OaFrPanelGenSupport_Type(Integer32):
    """Custom type oaFrPanelGenSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("supported", 2))
    )


_OaFrPanelGenSupport_Type.__name__ = "Integer32"
_OaFrPanelGenSupport_Object = MibScalar
oaFrPanelGenSupport = _OaFrPanelGenSupport_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 20, 1, 1),
    _OaFrPanelGenSupport_Type()
)
oaFrPanelGenSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaFrPanelGenSupport.setStatus("current")
_OaFrPanelSlot_ObjectIdentity = ObjectIdentity
oaFrPanelSlot = _OaFrPanelSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 20, 5)
)
_OaFrPanelSlotTable_Object = MibTable
oaFrPanelSlotTable = _OaFrPanelSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 20, 5, 5)
)
if mibBuilder.loadTexts:
    oaFrPanelSlotTable.setStatus("current")
_OaFrPanelSlotEntry_Object = MibTableRow
oaFrPanelSlotEntry = _OaFrPanelSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 20, 5, 5, 1)
)
oaFrPanelSlotEntry.setIndexNames(
    (0, "OA-FRONT-PANEL-MIB", "oaFrPanelSltShelfId"),
    (0, "OA-FRONT-PANEL-MIB", "oaFrPanelSltSlotId"),
)
if mibBuilder.loadTexts:
    oaFrPanelSlotEntry.setStatus("current")


class _OaFrPanelSltShelfId_Type(Integer32):
    """Custom type oaFrPanelSltShelfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_OaFrPanelSltShelfId_Type.__name__ = "Integer32"
_OaFrPanelSltShelfId_Object = MibTableColumn
oaFrPanelSltShelfId = _OaFrPanelSltShelfId_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 20, 5, 5, 1, 1),
    _OaFrPanelSltShelfId_Type()
)
oaFrPanelSltShelfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaFrPanelSltShelfId.setStatus("current")


class _OaFrPanelSltSlotId_Type(Integer32):
    """Custom type oaFrPanelSltSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_OaFrPanelSltSlotId_Type.__name__ = "Integer32"
_OaFrPanelSltSlotId_Object = MibTableColumn
oaFrPanelSltSlotId = _OaFrPanelSltSlotId_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 20, 5, 5, 1, 2),
    _OaFrPanelSltSlotId_Type()
)
oaFrPanelSltSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaFrPanelSltSlotId.setStatus("current")


class _OaFrPanelSltPortsNumber_Type(Integer32):
    """Custom type oaFrPanelSltPortsNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OaFrPanelSltPortsNumber_Type.__name__ = "Integer32"
_OaFrPanelSltPortsNumber_Object = MibTableColumn
oaFrPanelSltPortsNumber = _OaFrPanelSltPortsNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 20, 5, 5, 1, 3),
    _OaFrPanelSltPortsNumber_Type()
)
oaFrPanelSltPortsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaFrPanelSltPortsNumber.setStatus("current")


class _OaFrPanelSltLedsNumber_Type(Integer32):
    """Custom type oaFrPanelSltLedsNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OaFrPanelSltLedsNumber_Type.__name__ = "Integer32"
_OaFrPanelSltLedsNumber_Object = MibTableColumn
oaFrPanelSltLedsNumber = _OaFrPanelSltLedsNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 20, 5, 5, 1, 4),
    _OaFrPanelSltLedsNumber_Type()
)
oaFrPanelSltLedsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaFrPanelSltLedsNumber.setStatus("current")


class _OaFrPanelSltLedsVersion_Type(Integer32):
    """Custom type oaFrPanelSltLedsVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_OaFrPanelSltLedsVersion_Type.__name__ = "Integer32"
_OaFrPanelSltLedsVersion_Object = MibTableColumn
oaFrPanelSltLedsVersion = _OaFrPanelSltLedsVersion_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 20, 5, 5, 1, 5),
    _OaFrPanelSltLedsVersion_Type()
)
oaFrPanelSltLedsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaFrPanelSltLedsVersion.setStatus("current")


class _OaFrPanelSltLedStatuses_Type(OctetString):
    """Custom type oaFrPanelSltLedStatuses based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OaFrPanelSltLedStatuses_Type.__name__ = "OctetString"
_OaFrPanelSltLedStatuses_Object = MibTableColumn
oaFrPanelSltLedStatuses = _OaFrPanelSltLedStatuses_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 20, 5, 5, 1, 6),
    _OaFrPanelSltLedStatuses_Type()
)
oaFrPanelSltLedStatuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaFrPanelSltLedStatuses.setStatus("current")


class _OaFrPanelSltPrtsConnector_Type(OctetString):
    """Custom type oaFrPanelSltPrtsConnector based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OaFrPanelSltPrtsConnector_Type.__name__ = "OctetString"
_OaFrPanelSltPrtsConnector_Object = MibTableColumn
oaFrPanelSltPrtsConnector = _OaFrPanelSltPrtsConnector_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 20, 5, 5, 1, 7),
    _OaFrPanelSltPrtsConnector_Type()
)
oaFrPanelSltPrtsConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaFrPanelSltPrtsConnector.setStatus("current")


class _OaFrPanelSltPrtsSubConnector_Type(OctetString):
    """Custom type oaFrPanelSltPrtsSubConnector based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OaFrPanelSltPrtsSubConnector_Type.__name__ = "OctetString"
_OaFrPanelSltPrtsSubConnector_Object = MibTableColumn
oaFrPanelSltPrtsSubConnector = _OaFrPanelSltPrtsSubConnector_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 20, 5, 5, 1, 8),
    _OaFrPanelSltPrtsSubConnector_Type()
)
oaFrPanelSltPrtsSubConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaFrPanelSltPrtsSubConnector.setStatus("current")
_OaFrPanelConformance_ObjectIdentity = ObjectIdentity
oaFrPanelConformance = _OaFrPanelConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 20, 101)
)
_OaFrPanelCompliances_ObjectIdentity = ObjectIdentity
oaFrPanelCompliances = _OaFrPanelCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 20, 101, 1)
)
_OaFrPanelGroups_ObjectIdentity = ObjectIdentity
oaFrPanelGroups = _OaFrPanelGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 20, 101, 2)
)

# Managed Objects groups

oaFrPanelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 20, 101, 2, 1)
)
oaFrPanelGroup.setObjects(
      *(("OA-FRONT-PANEL-MIB", "oaFrPanelGenSupport"),
        ("OA-FRONT-PANEL-MIB", "oaFrPanelSltPortsNumber"),
        ("OA-FRONT-PANEL-MIB", "oaFrPanelSltLedsNumber"),
        ("OA-FRONT-PANEL-MIB", "oaFrPanelSltLedsVersion"),
        ("OA-FRONT-PANEL-MIB", "oaFrPanelSltLedStatuses"),
        ("OA-FRONT-PANEL-MIB", "oaFrPanelSltPrtsConnector"),
        ("OA-FRONT-PANEL-MIB", "oaFrPanelSltPrtsSubConnector"))
)
if mibBuilder.loadTexts:
    oaFrPanelGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

oaFrPanelCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 20, 101, 1, 1)
)
oaFrPanelCompliance.setObjects(
    ("OA-FRONT-PANEL-MIB", "oaFrPanelGroup")
)
if mibBuilder.loadTexts:
    oaFrPanelCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OA-FRONT-PANEL-MIB",
    **{"nbDevId": nbDevId,
       "oaFrPanel": oaFrPanel,
       "oaFrPanelGen": oaFrPanelGen,
       "oaFrPanelGenSupport": oaFrPanelGenSupport,
       "oaFrPanelSlot": oaFrPanelSlot,
       "oaFrPanelSlotTable": oaFrPanelSlotTable,
       "oaFrPanelSlotEntry": oaFrPanelSlotEntry,
       "oaFrPanelSltShelfId": oaFrPanelSltShelfId,
       "oaFrPanelSltSlotId": oaFrPanelSltSlotId,
       "oaFrPanelSltPortsNumber": oaFrPanelSltPortsNumber,
       "oaFrPanelSltLedsNumber": oaFrPanelSltLedsNumber,
       "oaFrPanelSltLedsVersion": oaFrPanelSltLedsVersion,
       "oaFrPanelSltLedStatuses": oaFrPanelSltLedStatuses,
       "oaFrPanelSltPrtsConnector": oaFrPanelSltPrtsConnector,
       "oaFrPanelSltPrtsSubConnector": oaFrPanelSltPrtsSubConnector,
       "oaFrPanelConformance": oaFrPanelConformance,
       "oaFrPanelCompliances": oaFrPanelCompliances,
       "oaFrPanelCompliance": oaFrPanelCompliance,
       "oaFrPanelGroups": oaFrPanelGroups,
       "oaFrPanelGroup": oaFrPanelGroup}
)
