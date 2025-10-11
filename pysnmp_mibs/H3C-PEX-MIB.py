# SNMP MIB module (H3C-PEX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-PEX-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:19:13 2025
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

(entPhysicalDescr,
 entPhysicalIndex) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalDescr",
    "entPhysicalIndex")

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

h3cPex = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 129)
)
if mibBuilder.loadTexts:
    h3cPex.setRevisions(
        ("2015-10-15 11:29",
         "2012-11-12 11:29")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cPexSpecInfo_ObjectIdentity = ObjectIdentity
h3cPexSpecInfo = _H3cPexSpecInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 129, 1)
)
_H3cPexPortMinId_Type = Integer32
_H3cPexPortMinId_Object = MibScalar
h3cPexPortMinId = _H3cPexPortMinId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 129, 1, 1),
    _H3cPexPortMinId_Type()
)
h3cPexPortMinId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPexPortMinId.setStatus("current")
_H3cPexPortMaxId_Type = Integer32
_H3cPexPortMaxId_Object = MibScalar
h3cPexPortMaxId = _H3cPexPortMaxId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 129, 1, 2),
    _H3cPexPortMaxId_Type()
)
h3cPexPortMaxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPexPortMaxId.setStatus("current")
_H3cPexMinAssociateId_Type = Integer32
_H3cPexMinAssociateId_Object = MibScalar
h3cPexMinAssociateId = _H3cPexMinAssociateId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 129, 1, 3),
    _H3cPexMinAssociateId_Type()
)
h3cPexMinAssociateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPexMinAssociateId.setStatus("current")
_H3cPexMaxAssociateId_Type = Integer32
_H3cPexMaxAssociateId_Object = MibScalar
h3cPexMaxAssociateId = _H3cPexMaxAssociateId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 129, 1, 4),
    _H3cPexMaxAssociateId_Type()
)
h3cPexMaxAssociateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPexMaxAssociateId.setStatus("current")
_H3cPexMaxPortPerPexPort_Type = Integer32
_H3cPexMaxPortPerPexPort_Object = MibScalar
h3cPexMaxPortPerPexPort = _H3cPexMaxPortPerPexPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 129, 1, 5),
    _H3cPexMaxPortPerPexPort_Type()
)
h3cPexMaxPortPerPexPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPexMaxPortPerPexPort.setStatus("current")
_H3cPexTable_ObjectIdentity = ObjectIdentity
h3cPexTable = _H3cPexTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 129, 2)
)
_H3cPexPortTable_Object = MibTable
h3cPexPortTable = _H3cPexPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 129, 2, 1)
)
if mibBuilder.loadTexts:
    h3cPexPortTable.setStatus("current")
_H3cPexPortEntry_Object = MibTableRow
h3cPexPortEntry = _H3cPexPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 129, 2, 1, 1)
)
h3cPexPortEntry.setIndexNames(
    (0, "H3C-PEX-MIB", "h3cPexPortId"),
)
if mibBuilder.loadTexts:
    h3cPexPortEntry.setStatus("current")


class _H3cPexPortId_Type(Integer32):
    """Custom type h3cPexPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cPexPortId_Type.__name__ = "Integer32"
_H3cPexPortId_Object = MibTableColumn
h3cPexPortId = _H3cPexPortId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 129, 2, 1, 1, 1),
    _H3cPexPortId_Type()
)
h3cPexPortId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cPexPortId.setStatus("current")


class _H3cPexPortAssociateId_Type(Integer32):
    """Custom type h3cPexPortAssociateId based on Integer32"""
    defaultValue = 65535


_H3cPexPortAssociateId_Type.__name__ = "Integer32"
_H3cPexPortAssociateId_Object = MibTableColumn
h3cPexPortAssociateId = _H3cPexPortAssociateId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 129, 2, 1, 1, 2),
    _H3cPexPortAssociateId_Type()
)
h3cPexPortAssociateId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPexPortAssociateId.setStatus("current")


class _H3cPexPortEntPhysicalIndex_Type(Integer32):
    """Custom type h3cPexPortEntPhysicalIndex based on Integer32"""
    defaultValue = 0


_H3cPexPortEntPhysicalIndex_Type.__name__ = "Integer32"
_H3cPexPortEntPhysicalIndex_Object = MibTableColumn
h3cPexPortEntPhysicalIndex = _H3cPexPortEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 129, 2, 1, 1, 3),
    _H3cPexPortEntPhysicalIndex_Type()
)
h3cPexPortEntPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPexPortEntPhysicalIndex.setStatus("current")


class _H3cPexPortDescr_Type(DisplayString):
    """Custom type h3cPexPortDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_H3cPexPortDescr_Type.__name__ = "DisplayString"
_H3cPexPortDescr_Object = MibTableColumn
h3cPexPortDescr = _H3cPexPortDescr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 129, 2, 1, 1, 4),
    _H3cPexPortDescr_Type()
)
h3cPexPortDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPexPortDescr.setStatus("current")


class _H3cPexPortStatus_Type(Integer32):
    """Custom type h3cPexPortStatus based on Integer32"""
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
        *(("offline", 1),
          ("loading", 2),
          ("online", 3))
    )


_H3cPexPortStatus_Type.__name__ = "Integer32"
_H3cPexPortStatus_Object = MibTableColumn
h3cPexPortStatus = _H3cPexPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 129, 2, 1, 1, 5),
    _H3cPexPortStatus_Type()
)
h3cPexPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPexPortStatus.setStatus("current")
_H3cPexPortRowStatus_Type = RowStatus
_H3cPexPortRowStatus_Object = MibTableColumn
h3cPexPortRowStatus = _H3cPexPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 129, 2, 1, 1, 6),
    _H3cPexPortRowStatus_Type()
)
h3cPexPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPexPortRowStatus.setStatus("current")
_H3cPexPhyPortTable_Object = MibTable
h3cPexPhyPortTable = _H3cPexPhyPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 129, 2, 2)
)
if mibBuilder.loadTexts:
    h3cPexPhyPortTable.setStatus("current")
_H3cPexPhyPortEntry_Object = MibTableRow
h3cPexPhyPortEntry = _H3cPexPhyPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 129, 2, 2, 1)
)
h3cPexPhyPortEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    h3cPexPhyPortEntry.setStatus("current")


class _H3cPexPhyPortStatus_Type(Integer32):
    """Custom type h3cPexPhyPortStatus based on Integer32"""
    defaultValue = 1

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
        *(("unknown", 1),
          ("down", 2),
          ("blocked", 3),
          ("forwarding", 4))
    )


_H3cPexPhyPortStatus_Type.__name__ = "Integer32"
_H3cPexPhyPortStatus_Object = MibTableColumn
h3cPexPhyPortStatus = _H3cPexPhyPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 129, 2, 2, 1, 1),
    _H3cPexPhyPortStatus_Type()
)
h3cPexPhyPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPexPhyPortStatus.setStatus("current")


class _H3cPexPhyPortBelongToPexPort_Type(Integer32):
    """Custom type h3cPexPhyPortBelongToPexPort based on Integer32"""
    defaultValue = 0


_H3cPexPhyPortBelongToPexPort_Type.__name__ = "Integer32"
_H3cPexPhyPortBelongToPexPort_Object = MibTableColumn
h3cPexPhyPortBelongToPexPort = _H3cPexPhyPortBelongToPexPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 129, 2, 2, 1, 2),
    _H3cPexPhyPortBelongToPexPort_Type()
)
h3cPexPhyPortBelongToPexPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPexPhyPortBelongToPexPort.setStatus("current")
_H3cPexPhyPortNeighborEntIndex_Type = Integer32
_H3cPexPhyPortNeighborEntIndex_Object = MibTableColumn
h3cPexPhyPortNeighborEntIndex = _H3cPexPhyPortNeighborEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 129, 2, 2, 1, 3),
    _H3cPexPhyPortNeighborEntIndex_Type()
)
h3cPexPhyPortNeighborEntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPexPhyPortNeighborEntIndex.setStatus("current")
_H3cPexDeviceInfoTable_Object = MibTable
h3cPexDeviceInfoTable = _H3cPexDeviceInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 129, 2, 3)
)
if mibBuilder.loadTexts:
    h3cPexDeviceInfoTable.setStatus("current")
_H3cPexDeviceInfoEntry_Object = MibTableRow
h3cPexDeviceInfoEntry = _H3cPexDeviceInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 129, 2, 3, 1)
)
h3cPexDeviceInfoEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    h3cPexDeviceInfoEntry.setStatus("current")


class _H3cPexDeviceStatus_Type(Integer32):
    """Custom type h3cPexDeviceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("faulty", 2))
    )


_H3cPexDeviceStatus_Type.__name__ = "Integer32"
_H3cPexDeviceStatus_Object = MibTableColumn
h3cPexDeviceStatus = _H3cPexDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 129, 2, 3, 1, 1),
    _H3cPexDeviceStatus_Type()
)
h3cPexDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPexDeviceStatus.setStatus("current")
_H3cPexDeviceAssociateId_Type = Integer32
_H3cPexDeviceAssociateId_Object = MibTableColumn
h3cPexDeviceAssociateId = _H3cPexDeviceAssociateId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 129, 2, 3, 1, 2),
    _H3cPexDeviceAssociateId_Type()
)
h3cPexDeviceAssociateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPexDeviceAssociateId.setStatus("current")
_H3cPexTopoTable_Object = MibTable
h3cPexTopoTable = _H3cPexTopoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 129, 2, 4)
)
if mibBuilder.loadTexts:
    h3cPexTopoTable.setStatus("current")
_H3cPexTopoEntry_Object = MibTableRow
h3cPexTopoEntry = _H3cPexTopoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 129, 2, 4, 1)
)
h3cPexTopoEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    h3cPexTopoEntry.setStatus("current")
_H3cPexNeighborEntIndex_Type = Integer32
_H3cPexNeighborEntIndex_Object = MibTableColumn
h3cPexNeighborEntIndex = _H3cPexNeighborEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 129, 2, 4, 1, 1),
    _H3cPexNeighborEntIndex_Type()
)
h3cPexNeighborEntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPexNeighborEntIndex.setStatus("current")
_H3cPexTraps_ObjectIdentity = ObjectIdentity
h3cPexTraps = _H3cPexTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 129, 3)
)
_H3cPexTrapPrefix_ObjectIdentity = ObjectIdentity
h3cPexTrapPrefix = _H3cPexTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 129, 3, 0)
)
_H3cPexTrapObjects_ObjectIdentity = ObjectIdentity
h3cPexTrapObjects = _H3cPexTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 129, 4)
)
_H3cPexEntPhysicalIndexBind_Type = Integer32
_H3cPexEntPhysicalIndexBind_Object = MibScalar
h3cPexEntPhysicalIndexBind = _H3cPexEntPhysicalIndexBind_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 129, 4, 1),
    _H3cPexEntPhysicalIndexBind_Type()
)
h3cPexEntPhysicalIndexBind.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cPexEntPhysicalIndexBind.setStatus("current")

# Managed Objects groups


# Notification objects

h3cPexPortOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 129, 3, 0, 1)
)
h3cPexPortOnline.setObjects(
      *(("H3C-PEX-MIB", "h3cPexPortId"),
        ("H3C-PEX-MIB", "h3cPexPortDescr"))
)
if mibBuilder.loadTexts:
    h3cPexPortOnline.setStatus(
        "current"
    )

h3cPexPortOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 129, 3, 0, 2)
)
h3cPexPortOffline.setObjects(
      *(("H3C-PEX-MIB", "h3cPexPortId"),
        ("H3C-PEX-MIB", "h3cPexPortDescr"))
)
if mibBuilder.loadTexts:
    h3cPexPortOffline.setStatus(
        "current"
    )

h3cPexPhyPortForwarding = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 129, 3, 0, 3)
)
h3cPexPhyPortForwarding.setObjects(
      *(("H3C-PEX-MIB", "h3cPexEntPhysicalIndexBind"),
        ("ENTITY-MIB", "entPhysicalDescr"))
)
if mibBuilder.loadTexts:
    h3cPexPhyPortForwarding.setStatus(
        "current"
    )

h3cPexPhyPortBlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 129, 3, 0, 4)
)
h3cPexPhyPortBlocked.setObjects(
      *(("H3C-PEX-MIB", "h3cPexEntPhysicalIndexBind"),
        ("ENTITY-MIB", "entPhysicalDescr"))
)
if mibBuilder.loadTexts:
    h3cPexPhyPortBlocked.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-PEX-MIB",
    **{"h3cPex": h3cPex,
       "h3cPexSpecInfo": h3cPexSpecInfo,
       "h3cPexPortMinId": h3cPexPortMinId,
       "h3cPexPortMaxId": h3cPexPortMaxId,
       "h3cPexMinAssociateId": h3cPexMinAssociateId,
       "h3cPexMaxAssociateId": h3cPexMaxAssociateId,
       "h3cPexMaxPortPerPexPort": h3cPexMaxPortPerPexPort,
       "h3cPexTable": h3cPexTable,
       "h3cPexPortTable": h3cPexPortTable,
       "h3cPexPortEntry": h3cPexPortEntry,
       "h3cPexPortId": h3cPexPortId,
       "h3cPexPortAssociateId": h3cPexPortAssociateId,
       "h3cPexPortEntPhysicalIndex": h3cPexPortEntPhysicalIndex,
       "h3cPexPortDescr": h3cPexPortDescr,
       "h3cPexPortStatus": h3cPexPortStatus,
       "h3cPexPortRowStatus": h3cPexPortRowStatus,
       "h3cPexPhyPortTable": h3cPexPhyPortTable,
       "h3cPexPhyPortEntry": h3cPexPhyPortEntry,
       "h3cPexPhyPortStatus": h3cPexPhyPortStatus,
       "h3cPexPhyPortBelongToPexPort": h3cPexPhyPortBelongToPexPort,
       "h3cPexPhyPortNeighborEntIndex": h3cPexPhyPortNeighborEntIndex,
       "h3cPexDeviceInfoTable": h3cPexDeviceInfoTable,
       "h3cPexDeviceInfoEntry": h3cPexDeviceInfoEntry,
       "h3cPexDeviceStatus": h3cPexDeviceStatus,
       "h3cPexDeviceAssociateId": h3cPexDeviceAssociateId,
       "h3cPexTopoTable": h3cPexTopoTable,
       "h3cPexTopoEntry": h3cPexTopoEntry,
       "h3cPexNeighborEntIndex": h3cPexNeighborEntIndex,
       "h3cPexTraps": h3cPexTraps,
       "h3cPexTrapPrefix": h3cPexTrapPrefix,
       "h3cPexPortOnline": h3cPexPortOnline,
       "h3cPexPortOffline": h3cPexPortOffline,
       "h3cPexPhyPortForwarding": h3cPexPhyPortForwarding,
       "h3cPexPhyPortBlocked": h3cPexPhyPortBlocked,
       "h3cPexTrapObjects": h3cPexTrapObjects,
       "h3cPexEntPhysicalIndexBind": h3cPexEntPhysicalIndexBind}
)
