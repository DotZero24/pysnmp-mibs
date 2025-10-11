# SNMP MIB module (RAISECOM-OAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-OAM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:27 2025
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

(dot3OamEventLogLocation,
 dot3OamEventLogOui,
 dot3OamEventLogType,
 dot3OamPeerMacAddress,
 dot3OamPeerVendorInfo,
 dot3OamPeerVendorOui) = mibBuilder.importSymbols(
    "DOT3-OAM-MIB",
    "dot3OamEventLogLocation",
    "dot3OamEventLogOui",
    "dot3OamEventLogType",
    "dot3OamPeerMacAddress",
    "dot3OamPeerVendorInfo",
    "dot3OamPeerVendorOui")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(oam,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "oam")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

raisecomOamMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 17, 1, 2)
)
if mibBuilder.loadTexts:
    raisecomOamMIB.setRevisions(
        ("2006-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RaisecomOamObjects_ObjectIdentity = ObjectIdentity
raisecomOamObjects = _RaisecomOamObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 17, 1, 2, 1)
)
_RaisecomOamTrapTable_Object = MibTable
raisecomOamTrapTable = _RaisecomOamTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 17, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    raisecomOamTrapTable.setStatus("current")
_RaisecomOamTrapEntry_Object = MibTableRow
raisecomOamTrapEntry = _RaisecomOamTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 17, 1, 2, 1, 1, 1)
)
raisecomOamTrapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    raisecomOamTrapEntry.setStatus("current")
_RaisecomOamEventTrapEnable_Type = TruthValue
_RaisecomOamEventTrapEnable_Object = MibTableColumn
raisecomOamEventTrapEnable = _RaisecomOamEventTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 17, 1, 2, 1, 1, 1, 1),
    _RaisecomOamEventTrapEnable_Type()
)
raisecomOamEventTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomOamEventTrapEnable.setStatus("current")
_RaisecomOamPeerEventTrapEnable_Type = TruthValue
_RaisecomOamPeerEventTrapEnable_Object = MibTableColumn
raisecomOamPeerEventTrapEnable = _RaisecomOamPeerEventTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 17, 1, 2, 1, 1, 1, 2),
    _RaisecomOamPeerEventTrapEnable_Type()
)
raisecomOamPeerEventTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomOamPeerEventTrapEnable.setStatus("current")
_RaisecomOamDiscoveryTrapTotal_Type = Unsigned32
_RaisecomOamDiscoveryTrapTotal_Object = MibTableColumn
raisecomOamDiscoveryTrapTotal = _RaisecomOamDiscoveryTrapTotal_Object(
    (1, 3, 6, 1, 4, 1, 8886, 17, 1, 2, 1, 1, 1, 3),
    _RaisecomOamDiscoveryTrapTotal_Type()
)
raisecomOamDiscoveryTrapTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOamDiscoveryTrapTotal.setStatus("current")
_RaisecomOamDiscoveryTrapTimestamp_Type = TimeStamp
_RaisecomOamDiscoveryTrapTimestamp_Object = MibTableColumn
raisecomOamDiscoveryTrapTimestamp = _RaisecomOamDiscoveryTrapTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 17, 1, 2, 1, 1, 1, 4),
    _RaisecomOamDiscoveryTrapTimestamp_Type()
)
raisecomOamDiscoveryTrapTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOamDiscoveryTrapTimestamp.setStatus("current")
_RaisecomOamLostTrapTotal_Type = Unsigned32
_RaisecomOamLostTrapTotal_Object = MibTableColumn
raisecomOamLostTrapTotal = _RaisecomOamLostTrapTotal_Object(
    (1, 3, 6, 1, 4, 1, 8886, 17, 1, 2, 1, 1, 1, 5),
    _RaisecomOamLostTrapTotal_Type()
)
raisecomOamLostTrapTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOamLostTrapTotal.setStatus("current")
_RaisecomOamLostTrapTimestamp_Type = TimeStamp
_RaisecomOamLostTrapTimestamp_Object = MibTableColumn
raisecomOamLostTrapTimestamp = _RaisecomOamLostTrapTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 17, 1, 2, 1, 1, 1, 6),
    _RaisecomOamLostTrapTimestamp_Type()
)
raisecomOamLostTrapTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOamLostTrapTimestamp.setStatus("current")
_RaisecomOamRemoteMgtTable_Object = MibTable
raisecomOamRemoteMgtTable = _RaisecomOamRemoteMgtTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 17, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    raisecomOamRemoteMgtTable.setStatus("current")
_RaisecomOamRemoteMgtEntry_Object = MibTableRow
raisecomOamRemoteMgtEntry = _RaisecomOamRemoteMgtEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 17, 1, 2, 1, 2, 1)
)
raisecomOamRemoteMgtEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    raisecomOamRemoteMgtEntry.setStatus("current")


class _RaisecomOamRemoteMgtBranch_Type(Integer32):
    """Custom type raisecomOamRemoteMgtBranch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("object", 3),
          ("package", 4),
          ("attribute", 7))
    )


_RaisecomOamRemoteMgtBranch_Type.__name__ = "Integer32"
_RaisecomOamRemoteMgtBranch_Object = MibTableColumn
raisecomOamRemoteMgtBranch = _RaisecomOamRemoteMgtBranch_Object(
    (1, 3, 6, 1, 4, 1, 8886, 17, 1, 2, 1, 2, 1, 1),
    _RaisecomOamRemoteMgtBranch_Type()
)
raisecomOamRemoteMgtBranch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomOamRemoteMgtBranch.setStatus("current")


class _RaisecomOamRemoteMgtLeaf_Type(Integer32):
    """Custom type raisecomOamRemoteMgtLeaf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RaisecomOamRemoteMgtLeaf_Type.__name__ = "Integer32"
_RaisecomOamRemoteMgtLeaf_Object = MibTableColumn
raisecomOamRemoteMgtLeaf = _RaisecomOamRemoteMgtLeaf_Object(
    (1, 3, 6, 1, 4, 1, 8886, 17, 1, 2, 1, 2, 1, 2),
    _RaisecomOamRemoteMgtLeaf_Type()
)
raisecomOamRemoteMgtLeaf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomOamRemoteMgtLeaf.setStatus("current")


class _RaisecomOamRemoteMgtValue_Type(OctetString):
    """Custom type raisecomOamRemoteMgtValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )


_RaisecomOamRemoteMgtValue_Type.__name__ = "OctetString"
_RaisecomOamRemoteMgtValue_Object = MibTableColumn
raisecomOamRemoteMgtValue = _RaisecomOamRemoteMgtValue_Object(
    (1, 3, 6, 1, 4, 1, 8886, 17, 1, 2, 1, 2, 1, 3),
    _RaisecomOamRemoteMgtValue_Type()
)
raisecomOamRemoteMgtValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomOamRemoteMgtValue.setStatus("current")


class _RaisecomOamRemoteMgtStatus_Type(Integer32):
    """Custom type raisecomOamRemoteMgtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("wait", 1),
          ("get", 2))
    )


_RaisecomOamRemoteMgtStatus_Type.__name__ = "Integer32"
_RaisecomOamRemoteMgtStatus_Object = MibTableColumn
raisecomOamRemoteMgtStatus = _RaisecomOamRemoteMgtStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 17, 1, 2, 1, 2, 1, 4),
    _RaisecomOamRemoteMgtStatus_Type()
)
raisecomOamRemoteMgtStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomOamRemoteMgtStatus.setStatus("current")
_RaisecomOamNotifications_ObjectIdentity = ObjectIdentity
raisecomOamNotifications = _RaisecomOamNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 17, 1, 2, 2)
)
_RaisecomOamScalar_ObjectIdentity = ObjectIdentity
raisecomOamScalar = _RaisecomOamScalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 17, 1, 2, 3)
)


class _RaisecomOamSendPeriod_Type(Integer32):
    """Custom type raisecomOamSendPeriod based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RaisecomOamSendPeriod_Type.__name__ = "Integer32"
_RaisecomOamSendPeriod_Object = MibScalar
raisecomOamSendPeriod = _RaisecomOamSendPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8886, 17, 1, 2, 3, 1),
    _RaisecomOamSendPeriod_Type()
)
raisecomOamSendPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomOamSendPeriod.setStatus("current")


class _RaisecomOamLinkTimeout_Type(Integer32):
    """Custom type raisecomOamLinkTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RaisecomOamLinkTimeout_Type.__name__ = "Integer32"
_RaisecomOamLinkTimeout_Object = MibScalar
raisecomOamLinkTimeout = _RaisecomOamLinkTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8886, 17, 1, 2, 3, 2),
    _RaisecomOamLinkTimeout_Type()
)
raisecomOamLinkTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomOamLinkTimeout.setStatus("current")

# Managed Objects groups


# Notification objects

raisecomOamDiscoveryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 17, 1, 2, 2, 1)
)
raisecomOamDiscoveryTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("DOT3-OAM-MIB", "dot3OamPeerMacAddress"),
        ("DOT3-OAM-MIB", "dot3OamPeerVendorOui"),
        ("DOT3-OAM-MIB", "dot3OamPeerVendorInfo"))
)
if mibBuilder.loadTexts:
    raisecomOamDiscoveryTrap.setStatus(
        "current"
    )

raisecomOamLostTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 17, 1, 2, 2, 2)
)
raisecomOamLostTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    raisecomOamLostTrap.setStatus(
        "current"
    )

raisecomOamNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 17, 1, 2, 2, 3)
)
raisecomOamNormalTrap.setObjects(
      *(("DOT3-OAM-MIB", "dot3OamEventLogOui"),
        ("DOT3-OAM-MIB", "dot3OamEventLogType"),
        ("DOT3-OAM-MIB", "dot3OamEventLogLocation"))
)
if mibBuilder.loadTexts:
    raisecomOamNormalTrap.setStatus(
        "current"
    )

raisecomOamDyingGaspNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 17, 1, 2, 2, 4)
)
raisecomOamDyingGaspNormalTrap.setObjects(
      *(("DOT3-OAM-MIB", "dot3OamEventLogOui"),
        ("DOT3-OAM-MIB", "dot3OamEventLogType"),
        ("DOT3-OAM-MIB", "dot3OamEventLogLocation"))
)
if mibBuilder.loadTexts:
    raisecomOamDyingGaspNormalTrap.setStatus(
        "current"
    )

raisecomOamLinkFaultNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 17, 1, 2, 2, 5)
)
raisecomOamLinkFaultNormalTrap.setObjects(
      *(("DOT3-OAM-MIB", "dot3OamEventLogOui"),
        ("DOT3-OAM-MIB", "dot3OamEventLogType"),
        ("DOT3-OAM-MIB", "dot3OamEventLogLocation"))
)
if mibBuilder.loadTexts:
    raisecomOamLinkFaultNormalTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-OAM-MIB",
    **{"raisecomOamMIB": raisecomOamMIB,
       "raisecomOamObjects": raisecomOamObjects,
       "raisecomOamTrapTable": raisecomOamTrapTable,
       "raisecomOamTrapEntry": raisecomOamTrapEntry,
       "raisecomOamEventTrapEnable": raisecomOamEventTrapEnable,
       "raisecomOamPeerEventTrapEnable": raisecomOamPeerEventTrapEnable,
       "raisecomOamDiscoveryTrapTotal": raisecomOamDiscoveryTrapTotal,
       "raisecomOamDiscoveryTrapTimestamp": raisecomOamDiscoveryTrapTimestamp,
       "raisecomOamLostTrapTotal": raisecomOamLostTrapTotal,
       "raisecomOamLostTrapTimestamp": raisecomOamLostTrapTimestamp,
       "raisecomOamRemoteMgtTable": raisecomOamRemoteMgtTable,
       "raisecomOamRemoteMgtEntry": raisecomOamRemoteMgtEntry,
       "raisecomOamRemoteMgtBranch": raisecomOamRemoteMgtBranch,
       "raisecomOamRemoteMgtLeaf": raisecomOamRemoteMgtLeaf,
       "raisecomOamRemoteMgtValue": raisecomOamRemoteMgtValue,
       "raisecomOamRemoteMgtStatus": raisecomOamRemoteMgtStatus,
       "raisecomOamNotifications": raisecomOamNotifications,
       "raisecomOamDiscoveryTrap": raisecomOamDiscoveryTrap,
       "raisecomOamLostTrap": raisecomOamLostTrap,
       "raisecomOamNormalTrap": raisecomOamNormalTrap,
       "raisecomOamDyingGaspNormalTrap": raisecomOamDyingGaspNormalTrap,
       "raisecomOamLinkFaultNormalTrap": raisecomOamLinkFaultNormalTrap,
       "raisecomOamScalar": raisecomOamScalar,
       "raisecomOamSendPeriod": raisecomOamSendPeriod,
       "raisecomOamLinkTimeout": raisecomOamLinkTimeout}
)
