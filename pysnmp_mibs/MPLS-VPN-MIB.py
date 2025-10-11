# SNMP MIB module (MPLS-VPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/cisco/MPLS-VPN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:38:44 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 experimental,
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
    "experimental",
    "iso")

(DisplayString,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mplsVpnMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 118)
)
if mibBuilder.loadTexts:
    mplsVpnMIB.setRevisions(
        ("2001-10-15 12:00",
         "2001-10-05 12:00",
         "2001-07-17 12:00",
         "2001-07-10 12:00",
         "2001-06-19 12:00",
         "2001-05-30 12:00",
         "2000-09-30 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class MplsVpnId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )



class MplsVpnRouteDistinguisher(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



# MIB Managed Objects in the order of their OIDs

_MplsVpnNotifications_ObjectIdentity = ObjectIdentity
mplsVpnNotifications = _MplsVpnNotifications_ObjectIdentity(
    (1, 3, 6, 1, 3, 118, 0)
)
_MplsVpnObjects_ObjectIdentity = ObjectIdentity
mplsVpnObjects = _MplsVpnObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 118, 1)
)
_MplsVpnScalars_ObjectIdentity = ObjectIdentity
mplsVpnScalars = _MplsVpnScalars_ObjectIdentity(
    (1, 3, 6, 1, 3, 118, 1, 1)
)
_MplsVpnConfiguredVrfs_Type = Unsigned32
_MplsVpnConfiguredVrfs_Object = MibScalar
mplsVpnConfiguredVrfs = _MplsVpnConfiguredVrfs_Object(
    (1, 3, 6, 1, 3, 118, 1, 1, 1),
    _MplsVpnConfiguredVrfs_Type()
)
mplsVpnConfiguredVrfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnConfiguredVrfs.setStatus("current")
_MplsVpnActiveVrfs_Type = Unsigned32
_MplsVpnActiveVrfs_Object = MibScalar
mplsVpnActiveVrfs = _MplsVpnActiveVrfs_Object(
    (1, 3, 6, 1, 3, 118, 1, 1, 2),
    _MplsVpnActiveVrfs_Type()
)
mplsVpnActiveVrfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnActiveVrfs.setStatus("current")
_MplsVpnConnectedInterfaces_Type = Unsigned32
_MplsVpnConnectedInterfaces_Object = MibScalar
mplsVpnConnectedInterfaces = _MplsVpnConnectedInterfaces_Object(
    (1, 3, 6, 1, 3, 118, 1, 1, 3),
    _MplsVpnConnectedInterfaces_Type()
)
mplsVpnConnectedInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnConnectedInterfaces.setStatus("current")


class _MplsVpnNotificationEnable_Type(TruthValue):
    """Custom type mplsVpnNotificationEnable based on TruthValue"""
    defaultValue = 2


_MplsVpnNotificationEnable_Type.__name__ = "TruthValue"
_MplsVpnNotificationEnable_Object = MibScalar
mplsVpnNotificationEnable = _MplsVpnNotificationEnable_Object(
    (1, 3, 6, 1, 3, 118, 1, 1, 4),
    _MplsVpnNotificationEnable_Type()
)
mplsVpnNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsVpnNotificationEnable.setStatus("current")
_MplsVpnVrfConfMaxPossibleRoutes_Type = Unsigned32
_MplsVpnVrfConfMaxPossibleRoutes_Object = MibScalar
mplsVpnVrfConfMaxPossibleRoutes = _MplsVpnVrfConfMaxPossibleRoutes_Object(
    (1, 3, 6, 1, 3, 118, 1, 1, 5),
    _MplsVpnVrfConfMaxPossibleRoutes_Type()
)
mplsVpnVrfConfMaxPossibleRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfConfMaxPossibleRoutes.setStatus("current")
_MplsVpnConf_ObjectIdentity = ObjectIdentity
mplsVpnConf = _MplsVpnConf_ObjectIdentity(
    (1, 3, 6, 1, 3, 118, 1, 2)
)
_MplsVpnInterfaceConfTable_Object = MibTable
mplsVpnInterfaceConfTable = _MplsVpnInterfaceConfTable_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mplsVpnInterfaceConfTable.setStatus("current")
_MplsVpnInterfaceConfEntry_Object = MibTableRow
mplsVpnInterfaceConfEntry = _MplsVpnInterfaceConfEntry_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 1, 1)
)
mplsVpnInterfaceConfEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
    (0, "MPLS-VPN-MIB", "mplsVpnInterfaceConfIndex"),
)
if mibBuilder.loadTexts:
    mplsVpnInterfaceConfEntry.setStatus("current")
_MplsVpnInterfaceConfIndex_Type = InterfaceIndex
_MplsVpnInterfaceConfIndex_Object = MibTableColumn
mplsVpnInterfaceConfIndex = _MplsVpnInterfaceConfIndex_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 1, 1, 1),
    _MplsVpnInterfaceConfIndex_Type()
)
mplsVpnInterfaceConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsVpnInterfaceConfIndex.setStatus("current")


class _MplsVpnInterfaceLabelEdgeType_Type(Integer32):
    """Custom type mplsVpnInterfaceLabelEdgeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("providerEdge", 1),
          ("customerEdge", 2))
    )


_MplsVpnInterfaceLabelEdgeType_Type.__name__ = "Integer32"
_MplsVpnInterfaceLabelEdgeType_Object = MibTableColumn
mplsVpnInterfaceLabelEdgeType = _MplsVpnInterfaceLabelEdgeType_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 1, 1, 2),
    _MplsVpnInterfaceLabelEdgeType_Type()
)
mplsVpnInterfaceLabelEdgeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnInterfaceLabelEdgeType.setStatus("current")


class _MplsVpnInterfaceVpnClassification_Type(Integer32):
    """Custom type mplsVpnInterfaceVpnClassification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("carrierOfCarrier", 1),
          ("enterprise", 2),
          ("interProvider", 3))
    )


_MplsVpnInterfaceVpnClassification_Type.__name__ = "Integer32"
_MplsVpnInterfaceVpnClassification_Object = MibTableColumn
mplsVpnInterfaceVpnClassification = _MplsVpnInterfaceVpnClassification_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 1, 1, 3),
    _MplsVpnInterfaceVpnClassification_Type()
)
mplsVpnInterfaceVpnClassification.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnInterfaceVpnClassification.setStatus("current")


class _MplsVpnInterfaceVpnRouteDistProtocol_Type(Bits):
    """Custom type mplsVpnInterfaceVpnRouteDistProtocol based on Bits"""
    namedValues = NamedValues(
        *(("dummy", 0),
          ("none", 1),
          ("bgp", 2),
          ("ospf", 3),
          ("rip", 4),
          ("isis", 5),
          ("other", 6))
    )

_MplsVpnInterfaceVpnRouteDistProtocol_Type.__name__ = "Bits"
_MplsVpnInterfaceVpnRouteDistProtocol_Object = MibTableColumn
mplsVpnInterfaceVpnRouteDistProtocol = _MplsVpnInterfaceVpnRouteDistProtocol_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 1, 1, 4),
    _MplsVpnInterfaceVpnRouteDistProtocol_Type()
)
mplsVpnInterfaceVpnRouteDistProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnInterfaceVpnRouteDistProtocol.setStatus("current")
_MplsVpnInterfaceConfStorageType_Type = StorageType
_MplsVpnInterfaceConfStorageType_Object = MibTableColumn
mplsVpnInterfaceConfStorageType = _MplsVpnInterfaceConfStorageType_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 1, 1, 5),
    _MplsVpnInterfaceConfStorageType_Type()
)
mplsVpnInterfaceConfStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnInterfaceConfStorageType.setStatus("current")
_MplsVpnInterfaceConfRowStatus_Type = RowStatus
_MplsVpnInterfaceConfRowStatus_Object = MibTableColumn
mplsVpnInterfaceConfRowStatus = _MplsVpnInterfaceConfRowStatus_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 1, 1, 6),
    _MplsVpnInterfaceConfRowStatus_Type()
)
mplsVpnInterfaceConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnInterfaceConfRowStatus.setStatus("current")
_MplsVpnVrfTable_Object = MibTable
mplsVpnVrfTable = _MplsVpnVrfTable_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mplsVpnVrfTable.setStatus("current")
_MplsVpnVrfEntry_Object = MibTableRow
mplsVpnVrfEntry = _MplsVpnVrfEntry_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 2, 1)
)
mplsVpnVrfEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
)
if mibBuilder.loadTexts:
    mplsVpnVrfEntry.setStatus("current")
_MplsVpnVrfName_Type = MplsVpnId
_MplsVpnVrfName_Object = MibTableColumn
mplsVpnVrfName = _MplsVpnVrfName_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 2, 1, 1),
    _MplsVpnVrfName_Type()
)
mplsVpnVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsVpnVrfName.setStatus("current")
_MplsVpnVrfDescription_Type = SnmpAdminString
_MplsVpnVrfDescription_Object = MibTableColumn
mplsVpnVrfDescription = _MplsVpnVrfDescription_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 2, 1, 2),
    _MplsVpnVrfDescription_Type()
)
mplsVpnVrfDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfDescription.setStatus("current")
_MplsVpnVrfRouteDistinguisher_Type = MplsVpnRouteDistinguisher
_MplsVpnVrfRouteDistinguisher_Object = MibTableColumn
mplsVpnVrfRouteDistinguisher = _MplsVpnVrfRouteDistinguisher_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 2, 1, 3),
    _MplsVpnVrfRouteDistinguisher_Type()
)
mplsVpnVrfRouteDistinguisher.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteDistinguisher.setStatus("current")
_MplsVpnVrfCreationTime_Type = TimeStamp
_MplsVpnVrfCreationTime_Object = MibTableColumn
mplsVpnVrfCreationTime = _MplsVpnVrfCreationTime_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 2, 1, 4),
    _MplsVpnVrfCreationTime_Type()
)
mplsVpnVrfCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfCreationTime.setStatus("current")


class _MplsVpnVrfOperStatus_Type(Integer32):
    """Custom type mplsVpnVrfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_MplsVpnVrfOperStatus_Type.__name__ = "Integer32"
_MplsVpnVrfOperStatus_Object = MibTableColumn
mplsVpnVrfOperStatus = _MplsVpnVrfOperStatus_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 2, 1, 5),
    _MplsVpnVrfOperStatus_Type()
)
mplsVpnVrfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfOperStatus.setStatus("current")
_MplsVpnVrfActiveInterfaces_Type = Unsigned32
_MplsVpnVrfActiveInterfaces_Object = MibTableColumn
mplsVpnVrfActiveInterfaces = _MplsVpnVrfActiveInterfaces_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 2, 1, 6),
    _MplsVpnVrfActiveInterfaces_Type()
)
mplsVpnVrfActiveInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfActiveInterfaces.setStatus("current")
_MplsVpnVrfAssociatedInterfaces_Type = Unsigned32
_MplsVpnVrfAssociatedInterfaces_Object = MibTableColumn
mplsVpnVrfAssociatedInterfaces = _MplsVpnVrfAssociatedInterfaces_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 2, 1, 7),
    _MplsVpnVrfAssociatedInterfaces_Type()
)
mplsVpnVrfAssociatedInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfAssociatedInterfaces.setStatus("current")
_MplsVpnVrfConfMidRouteThreshold_Type = Unsigned32
_MplsVpnVrfConfMidRouteThreshold_Object = MibTableColumn
mplsVpnVrfConfMidRouteThreshold = _MplsVpnVrfConfMidRouteThreshold_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 2, 1, 8),
    _MplsVpnVrfConfMidRouteThreshold_Type()
)
mplsVpnVrfConfMidRouteThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfConfMidRouteThreshold.setStatus("current")
_MplsVpnVrfConfHighRouteThreshold_Type = Unsigned32
_MplsVpnVrfConfHighRouteThreshold_Object = MibTableColumn
mplsVpnVrfConfHighRouteThreshold = _MplsVpnVrfConfHighRouteThreshold_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 2, 1, 9),
    _MplsVpnVrfConfHighRouteThreshold_Type()
)
mplsVpnVrfConfHighRouteThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfConfHighRouteThreshold.setStatus("current")
_MplsVpnVrfConfMaxRoutes_Type = Unsigned32
_MplsVpnVrfConfMaxRoutes_Object = MibTableColumn
mplsVpnVrfConfMaxRoutes = _MplsVpnVrfConfMaxRoutes_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 2, 1, 10),
    _MplsVpnVrfConfMaxRoutes_Type()
)
mplsVpnVrfConfMaxRoutes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfConfMaxRoutes.setStatus("current")
_MplsVpnVrfConfLastChanged_Type = TimeStamp
_MplsVpnVrfConfLastChanged_Object = MibTableColumn
mplsVpnVrfConfLastChanged = _MplsVpnVrfConfLastChanged_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 2, 1, 11),
    _MplsVpnVrfConfLastChanged_Type()
)
mplsVpnVrfConfLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfConfLastChanged.setStatus("current")
_MplsVpnVrfConfRowStatus_Type = RowStatus
_MplsVpnVrfConfRowStatus_Object = MibTableColumn
mplsVpnVrfConfRowStatus = _MplsVpnVrfConfRowStatus_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 2, 1, 12),
    _MplsVpnVrfConfRowStatus_Type()
)
mplsVpnVrfConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfConfRowStatus.setStatus("current")
_MplsVpnVrfConfStorageType_Type = StorageType
_MplsVpnVrfConfStorageType_Object = MibTableColumn
mplsVpnVrfConfStorageType = _MplsVpnVrfConfStorageType_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 2, 1, 13),
    _MplsVpnVrfConfStorageType_Type()
)
mplsVpnVrfConfStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfConfStorageType.setStatus("current")
_MplsVpnVrfRouteTargetTable_Object = MibTable
mplsVpnVrfRouteTargetTable = _MplsVpnVrfRouteTargetTable_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 3)
)
if mibBuilder.loadTexts:
    mplsVpnVrfRouteTargetTable.setStatus("current")
_MplsVpnVrfRouteTargetEntry_Object = MibTableRow
mplsVpnVrfRouteTargetEntry = _MplsVpnVrfRouteTargetEntry_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 3, 1)
)
mplsVpnVrfRouteTargetEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
    (0, "MPLS-VPN-MIB", "mplsVpnVrfRouteTargetIndex"),
    (0, "MPLS-VPN-MIB", "mplsVpnVrfRouteTargetType"),
)
if mibBuilder.loadTexts:
    mplsVpnVrfRouteTargetEntry.setStatus("current")
_MplsVpnVrfRouteTargetIndex_Type = Unsigned32
_MplsVpnVrfRouteTargetIndex_Object = MibTableColumn
mplsVpnVrfRouteTargetIndex = _MplsVpnVrfRouteTargetIndex_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 3, 1, 2),
    _MplsVpnVrfRouteTargetIndex_Type()
)
mplsVpnVrfRouteTargetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteTargetIndex.setStatus("current")


class _MplsVpnVrfRouteTargetType_Type(Integer32):
    """Custom type mplsVpnVrfRouteTargetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("import", 1),
          ("export", 2),
          ("both", 3))
    )


_MplsVpnVrfRouteTargetType_Type.__name__ = "Integer32"
_MplsVpnVrfRouteTargetType_Object = MibTableColumn
mplsVpnVrfRouteTargetType = _MplsVpnVrfRouteTargetType_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 3, 1, 3),
    _MplsVpnVrfRouteTargetType_Type()
)
mplsVpnVrfRouteTargetType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteTargetType.setStatus("current")
_MplsVpnVrfRouteTarget_Type = MplsVpnRouteDistinguisher
_MplsVpnVrfRouteTarget_Object = MibTableColumn
mplsVpnVrfRouteTarget = _MplsVpnVrfRouteTarget_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 3, 1, 4),
    _MplsVpnVrfRouteTarget_Type()
)
mplsVpnVrfRouteTarget.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteTarget.setStatus("current")
_MplsVpnVrfRouteTargetDescr_Type = DisplayString
_MplsVpnVrfRouteTargetDescr_Object = MibTableColumn
mplsVpnVrfRouteTargetDescr = _MplsVpnVrfRouteTargetDescr_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 3, 1, 5),
    _MplsVpnVrfRouteTargetDescr_Type()
)
mplsVpnVrfRouteTargetDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteTargetDescr.setStatus("current")
_MplsVpnVrfRouteTargetRowStatus_Type = RowStatus
_MplsVpnVrfRouteTargetRowStatus_Object = MibTableColumn
mplsVpnVrfRouteTargetRowStatus = _MplsVpnVrfRouteTargetRowStatus_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 3, 1, 6),
    _MplsVpnVrfRouteTargetRowStatus_Type()
)
mplsVpnVrfRouteTargetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteTargetRowStatus.setStatus("current")
_MplsVpnVrfBgpNbrAddrTable_Object = MibTable
mplsVpnVrfBgpNbrAddrTable = _MplsVpnVrfBgpNbrAddrTable_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 4)
)
if mibBuilder.loadTexts:
    mplsVpnVrfBgpNbrAddrTable.setStatus("current")
_MplsVpnVrfBgpNbrAddrEntry_Object = MibTableRow
mplsVpnVrfBgpNbrAddrEntry = _MplsVpnVrfBgpNbrAddrEntry_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 4, 1)
)
mplsVpnVrfBgpNbrAddrEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
    (0, "MPLS-VPN-MIB", "mplsVpnInterfaceConfIndex"),
    (0, "MPLS-VPN-MIB", "mplsVpnVrfBgpNbrIndex"),
)
if mibBuilder.loadTexts:
    mplsVpnVrfBgpNbrAddrEntry.setStatus("current")
_MplsVpnVrfBgpNbrIndex_Type = Unsigned32
_MplsVpnVrfBgpNbrIndex_Object = MibTableColumn
mplsVpnVrfBgpNbrIndex = _MplsVpnVrfBgpNbrIndex_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 4, 1, 1),
    _MplsVpnVrfBgpNbrIndex_Type()
)
mplsVpnVrfBgpNbrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpNbrIndex.setStatus("current")


class _MplsVpnVrfBgpNbrRole_Type(Integer32):
    """Custom type mplsVpnVrfBgpNbrRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ce", 1),
          ("pe", 2))
    )


_MplsVpnVrfBgpNbrRole_Type.__name__ = "Integer32"
_MplsVpnVrfBgpNbrRole_Object = MibTableColumn
mplsVpnVrfBgpNbrRole = _MplsVpnVrfBgpNbrRole_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 4, 1, 2),
    _MplsVpnVrfBgpNbrRole_Type()
)
mplsVpnVrfBgpNbrRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpNbrRole.setStatus("current")
_MplsVpnVrfBgpNbrType_Type = InetAddressType
_MplsVpnVrfBgpNbrType_Object = MibTableColumn
mplsVpnVrfBgpNbrType = _MplsVpnVrfBgpNbrType_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 4, 1, 3),
    _MplsVpnVrfBgpNbrType_Type()
)
mplsVpnVrfBgpNbrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpNbrType.setStatus("current")
_MplsVpnVrfBgpNbrAddr_Type = InetAddress
_MplsVpnVrfBgpNbrAddr_Object = MibTableColumn
mplsVpnVrfBgpNbrAddr = _MplsVpnVrfBgpNbrAddr_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 4, 1, 4),
    _MplsVpnVrfBgpNbrAddr_Type()
)
mplsVpnVrfBgpNbrAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpNbrAddr.setStatus("current")
_MplsVpnVrfBgpNbrRowStatus_Type = RowStatus
_MplsVpnVrfBgpNbrRowStatus_Object = MibTableColumn
mplsVpnVrfBgpNbrRowStatus = _MplsVpnVrfBgpNbrRowStatus_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 4, 1, 5),
    _MplsVpnVrfBgpNbrRowStatus_Type()
)
mplsVpnVrfBgpNbrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpNbrRowStatus.setStatus("current")
_MplsVpnVrfBgpNbrStorageType_Type = StorageType
_MplsVpnVrfBgpNbrStorageType_Object = MibTableColumn
mplsVpnVrfBgpNbrStorageType = _MplsVpnVrfBgpNbrStorageType_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 4, 1, 6),
    _MplsVpnVrfBgpNbrStorageType_Type()
)
mplsVpnVrfBgpNbrStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpNbrStorageType.setStatus("current")
_MplsVpnVrfBgpNbrPrefixTable_Object = MibTable
mplsVpnVrfBgpNbrPrefixTable = _MplsVpnVrfBgpNbrPrefixTable_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 5)
)
if mibBuilder.loadTexts:
    mplsVpnVrfBgpNbrPrefixTable.setStatus("current")
_MplsVpnVrfBgpNbrPrefixEntry_Object = MibTableRow
mplsVpnVrfBgpNbrPrefixEntry = _MplsVpnVrfBgpNbrPrefixEntry_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 5, 1)
)
mplsVpnVrfBgpNbrPrefixEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
    (0, "MPLS-VPN-MIB", "mplsVpnVrfBgpPathAttrIpAddrPrefix"),
    (0, "MPLS-VPN-MIB", "mplsVpnVrfBgpPathAttrIpAddrPrefixLen"),
    (0, "MPLS-VPN-MIB", "mplsVpnVrfBgpPathAttrPeer"),
)
if mibBuilder.loadTexts:
    mplsVpnVrfBgpNbrPrefixEntry.setStatus("current")
_MplsVpnVrfBgpPathAttrPeer_Type = InetAddress
_MplsVpnVrfBgpPathAttrPeer_Object = MibTableColumn
mplsVpnVrfBgpPathAttrPeer = _MplsVpnVrfBgpPathAttrPeer_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 5, 1, 1),
    _MplsVpnVrfBgpPathAttrPeer_Type()
)
mplsVpnVrfBgpPathAttrPeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpPathAttrPeer.setStatus("current")


class _MplsVpnVrfBgpPathAttrIpAddrPrefixLen_Type(Integer32):
    """Custom type mplsVpnVrfBgpPathAttrIpAddrPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_MplsVpnVrfBgpPathAttrIpAddrPrefixLen_Type.__name__ = "Integer32"
_MplsVpnVrfBgpPathAttrIpAddrPrefixLen_Object = MibTableColumn
mplsVpnVrfBgpPathAttrIpAddrPrefixLen = _MplsVpnVrfBgpPathAttrIpAddrPrefixLen_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 5, 1, 2),
    _MplsVpnVrfBgpPathAttrIpAddrPrefixLen_Type()
)
mplsVpnVrfBgpPathAttrIpAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpPathAttrIpAddrPrefixLen.setStatus("current")
_MplsVpnVrfBgpPathAttrIpAddrPrefix_Type = InetAddress
_MplsVpnVrfBgpPathAttrIpAddrPrefix_Object = MibTableColumn
mplsVpnVrfBgpPathAttrIpAddrPrefix = _MplsVpnVrfBgpPathAttrIpAddrPrefix_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 5, 1, 3),
    _MplsVpnVrfBgpPathAttrIpAddrPrefix_Type()
)
mplsVpnVrfBgpPathAttrIpAddrPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpPathAttrIpAddrPrefix.setStatus("current")


class _MplsVpnVrfBgpPathAttrOrigin_Type(Integer32):
    """Custom type mplsVpnVrfBgpPathAttrOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("igp", 1),
          ("egp", 2),
          ("incomplete", 3))
    )


_MplsVpnVrfBgpPathAttrOrigin_Type.__name__ = "Integer32"
_MplsVpnVrfBgpPathAttrOrigin_Object = MibTableColumn
mplsVpnVrfBgpPathAttrOrigin = _MplsVpnVrfBgpPathAttrOrigin_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 5, 1, 4),
    _MplsVpnVrfBgpPathAttrOrigin_Type()
)
mplsVpnVrfBgpPathAttrOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpPathAttrOrigin.setStatus("current")


class _MplsVpnVrfBgpPathAttrASPathSegment_Type(OctetString):
    """Custom type mplsVpnVrfBgpPathAttrASPathSegment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 255),
    )


_MplsVpnVrfBgpPathAttrASPathSegment_Type.__name__ = "OctetString"
_MplsVpnVrfBgpPathAttrASPathSegment_Object = MibTableColumn
mplsVpnVrfBgpPathAttrASPathSegment = _MplsVpnVrfBgpPathAttrASPathSegment_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 5, 1, 5),
    _MplsVpnVrfBgpPathAttrASPathSegment_Type()
)
mplsVpnVrfBgpPathAttrASPathSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpPathAttrASPathSegment.setStatus("current")
_MplsVpnVrfBgpPathAttrNextHop_Type = InetAddress
_MplsVpnVrfBgpPathAttrNextHop_Object = MibTableColumn
mplsVpnVrfBgpPathAttrNextHop = _MplsVpnVrfBgpPathAttrNextHop_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 5, 1, 6),
    _MplsVpnVrfBgpPathAttrNextHop_Type()
)
mplsVpnVrfBgpPathAttrNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpPathAttrNextHop.setStatus("current")


class _MplsVpnVrfBgpPathAttrMultiExitDisc_Type(Integer32):
    """Custom type mplsVpnVrfBgpPathAttrMultiExitDisc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_MplsVpnVrfBgpPathAttrMultiExitDisc_Type.__name__ = "Integer32"
_MplsVpnVrfBgpPathAttrMultiExitDisc_Object = MibTableColumn
mplsVpnVrfBgpPathAttrMultiExitDisc = _MplsVpnVrfBgpPathAttrMultiExitDisc_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 5, 1, 7),
    _MplsVpnVrfBgpPathAttrMultiExitDisc_Type()
)
mplsVpnVrfBgpPathAttrMultiExitDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpPathAttrMultiExitDisc.setStatus("current")


class _MplsVpnVrfBgpPathAttrLocalPref_Type(Integer32):
    """Custom type mplsVpnVrfBgpPathAttrLocalPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_MplsVpnVrfBgpPathAttrLocalPref_Type.__name__ = "Integer32"
_MplsVpnVrfBgpPathAttrLocalPref_Object = MibTableColumn
mplsVpnVrfBgpPathAttrLocalPref = _MplsVpnVrfBgpPathAttrLocalPref_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 5, 1, 8),
    _MplsVpnVrfBgpPathAttrLocalPref_Type()
)
mplsVpnVrfBgpPathAttrLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpPathAttrLocalPref.setStatus("current")


class _MplsVpnVrfBgpPathAttrAtomicAggregate_Type(Integer32):
    """Custom type mplsVpnVrfBgpPathAttrAtomicAggregate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lessSpecificRrouteNotSelected", 1),
          ("lessSpecificRouteSelected", 2))
    )


_MplsVpnVrfBgpPathAttrAtomicAggregate_Type.__name__ = "Integer32"
_MplsVpnVrfBgpPathAttrAtomicAggregate_Object = MibTableColumn
mplsVpnVrfBgpPathAttrAtomicAggregate = _MplsVpnVrfBgpPathAttrAtomicAggregate_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 5, 1, 9),
    _MplsVpnVrfBgpPathAttrAtomicAggregate_Type()
)
mplsVpnVrfBgpPathAttrAtomicAggregate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpPathAttrAtomicAggregate.setStatus("current")


class _MplsVpnVrfBgpPathAttrAggregatorAS_Type(Integer32):
    """Custom type mplsVpnVrfBgpPathAttrAggregatorAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MplsVpnVrfBgpPathAttrAggregatorAS_Type.__name__ = "Integer32"
_MplsVpnVrfBgpPathAttrAggregatorAS_Object = MibTableColumn
mplsVpnVrfBgpPathAttrAggregatorAS = _MplsVpnVrfBgpPathAttrAggregatorAS_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 5, 1, 10),
    _MplsVpnVrfBgpPathAttrAggregatorAS_Type()
)
mplsVpnVrfBgpPathAttrAggregatorAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpPathAttrAggregatorAS.setStatus("current")
_MplsVpnVrfBgpPathAttrAggregatorAddr_Type = InetAddress
_MplsVpnVrfBgpPathAttrAggregatorAddr_Object = MibTableColumn
mplsVpnVrfBgpPathAttrAggregatorAddr = _MplsVpnVrfBgpPathAttrAggregatorAddr_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 5, 1, 11),
    _MplsVpnVrfBgpPathAttrAggregatorAddr_Type()
)
mplsVpnVrfBgpPathAttrAggregatorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpPathAttrAggregatorAddr.setStatus("current")


class _MplsVpnVrfBgpPathAttrCalcLocalPref_Type(Integer32):
    """Custom type mplsVpnVrfBgpPathAttrCalcLocalPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_MplsVpnVrfBgpPathAttrCalcLocalPref_Type.__name__ = "Integer32"
_MplsVpnVrfBgpPathAttrCalcLocalPref_Object = MibTableColumn
mplsVpnVrfBgpPathAttrCalcLocalPref = _MplsVpnVrfBgpPathAttrCalcLocalPref_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 5, 1, 12),
    _MplsVpnVrfBgpPathAttrCalcLocalPref_Type()
)
mplsVpnVrfBgpPathAttrCalcLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpPathAttrCalcLocalPref.setStatus("current")


class _MplsVpnVrfBgpPathAttrBest_Type(Integer32):
    """Custom type mplsVpnVrfBgpPathAttrBest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_MplsVpnVrfBgpPathAttrBest_Type.__name__ = "Integer32"
_MplsVpnVrfBgpPathAttrBest_Object = MibTableColumn
mplsVpnVrfBgpPathAttrBest = _MplsVpnVrfBgpPathAttrBest_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 5, 1, 13),
    _MplsVpnVrfBgpPathAttrBest_Type()
)
mplsVpnVrfBgpPathAttrBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpPathAttrBest.setStatus("current")


class _MplsVpnVrfBgpPathAttrUnknown_Type(OctetString):
    """Custom type mplsVpnVrfBgpPathAttrUnknown based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MplsVpnVrfBgpPathAttrUnknown_Type.__name__ = "OctetString"
_MplsVpnVrfBgpPathAttrUnknown_Object = MibTableColumn
mplsVpnVrfBgpPathAttrUnknown = _MplsVpnVrfBgpPathAttrUnknown_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 5, 1, 14),
    _MplsVpnVrfBgpPathAttrUnknown_Type()
)
mplsVpnVrfBgpPathAttrUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpPathAttrUnknown.setStatus("current")
_MplsVpnVrfSecTable_Object = MibTable
mplsVpnVrfSecTable = _MplsVpnVrfSecTable_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 6)
)
if mibBuilder.loadTexts:
    mplsVpnVrfSecTable.setStatus("current")
_MplsVpnVrfSecEntry_Object = MibTableRow
mplsVpnVrfSecEntry = _MplsVpnVrfSecEntry_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    mplsVpnVrfSecEntry.setStatus("current")
_MplsVpnVrfSecIllegalLabelViolations_Type = Counter32
_MplsVpnVrfSecIllegalLabelViolations_Object = MibTableColumn
mplsVpnVrfSecIllegalLabelViolations = _MplsVpnVrfSecIllegalLabelViolations_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 6, 1, 1),
    _MplsVpnVrfSecIllegalLabelViolations_Type()
)
mplsVpnVrfSecIllegalLabelViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfSecIllegalLabelViolations.setStatus("current")
_MplsVpnVrfSecIllegalLabelRcvThresh_Type = Unsigned32
_MplsVpnVrfSecIllegalLabelRcvThresh_Object = MibTableColumn
mplsVpnVrfSecIllegalLabelRcvThresh = _MplsVpnVrfSecIllegalLabelRcvThresh_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 6, 1, 2),
    _MplsVpnVrfSecIllegalLabelRcvThresh_Type()
)
mplsVpnVrfSecIllegalLabelRcvThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfSecIllegalLabelRcvThresh.setStatus("current")
_MplsVpnPerf_ObjectIdentity = ObjectIdentity
mplsVpnPerf = _MplsVpnPerf_ObjectIdentity(
    (1, 3, 6, 1, 3, 118, 1, 3)
)
_MplsVpnVrfPerfTable_Object = MibTable
mplsVpnVrfPerfTable = _MplsVpnVrfPerfTable_Object(
    (1, 3, 6, 1, 3, 118, 1, 3, 1)
)
if mibBuilder.loadTexts:
    mplsVpnVrfPerfTable.setStatus("current")
_MplsVpnVrfPerfEntry_Object = MibTableRow
mplsVpnVrfPerfEntry = _MplsVpnVrfPerfEntry_Object(
    (1, 3, 6, 1, 3, 118, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    mplsVpnVrfPerfEntry.setStatus("current")
_MplsVpnVrfPerfRoutesAdded_Type = Counter32
_MplsVpnVrfPerfRoutesAdded_Object = MibTableColumn
mplsVpnVrfPerfRoutesAdded = _MplsVpnVrfPerfRoutesAdded_Object(
    (1, 3, 6, 1, 3, 118, 1, 3, 1, 1, 1),
    _MplsVpnVrfPerfRoutesAdded_Type()
)
mplsVpnVrfPerfRoutesAdded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfPerfRoutesAdded.setStatus("current")
_MplsVpnVrfPerfRoutesDeleted_Type = Counter32
_MplsVpnVrfPerfRoutesDeleted_Object = MibTableColumn
mplsVpnVrfPerfRoutesDeleted = _MplsVpnVrfPerfRoutesDeleted_Object(
    (1, 3, 6, 1, 3, 118, 1, 3, 1, 1, 2),
    _MplsVpnVrfPerfRoutesDeleted_Type()
)
mplsVpnVrfPerfRoutesDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfPerfRoutesDeleted.setStatus("current")
_MplsVpnVrfPerfCurrNumRoutes_Type = Unsigned32
_MplsVpnVrfPerfCurrNumRoutes_Object = MibTableColumn
mplsVpnVrfPerfCurrNumRoutes = _MplsVpnVrfPerfCurrNumRoutes_Object(
    (1, 3, 6, 1, 3, 118, 1, 3, 1, 1, 3),
    _MplsVpnVrfPerfCurrNumRoutes_Type()
)
mplsVpnVrfPerfCurrNumRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfPerfCurrNumRoutes.setStatus("current")
_MplsVpnRoute_ObjectIdentity = ObjectIdentity
mplsVpnRoute = _MplsVpnRoute_ObjectIdentity(
    (1, 3, 6, 1, 3, 118, 1, 4)
)
_MplsVpnVrfRouteTable_Object = MibTable
mplsVpnVrfRouteTable = _MplsVpnVrfRouteTable_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1)
)
if mibBuilder.loadTexts:
    mplsVpnVrfRouteTable.setStatus("current")
_MplsVpnVrfRouteEntry_Object = MibTableRow
mplsVpnVrfRouteEntry = _MplsVpnVrfRouteEntry_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1, 1)
)
mplsVpnVrfRouteEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
    (0, "MPLS-VPN-MIB", "mplsVpnVrfRouteDest"),
    (0, "MPLS-VPN-MIB", "mplsVpnVrfRouteMask"),
    (0, "MPLS-VPN-MIB", "mplsVpnVrfRouteTos"),
    (0, "MPLS-VPN-MIB", "mplsVpnVrfRouteNextHop"),
)
if mibBuilder.loadTexts:
    mplsVpnVrfRouteEntry.setStatus("current")
_MplsVpnVrfRouteDest_Type = InetAddress
_MplsVpnVrfRouteDest_Object = MibTableColumn
mplsVpnVrfRouteDest = _MplsVpnVrfRouteDest_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1, 1, 1),
    _MplsVpnVrfRouteDest_Type()
)
mplsVpnVrfRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteDest.setStatus("current")
_MplsVpnVrfRouteDestAddrType_Type = InetAddressType
_MplsVpnVrfRouteDestAddrType_Object = MibTableColumn
mplsVpnVrfRouteDestAddrType = _MplsVpnVrfRouteDestAddrType_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1, 1, 2),
    _MplsVpnVrfRouteDestAddrType_Type()
)
mplsVpnVrfRouteDestAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteDestAddrType.setStatus("current")
_MplsVpnVrfRouteMask_Type = InetAddress
_MplsVpnVrfRouteMask_Object = MibTableColumn
mplsVpnVrfRouteMask = _MplsVpnVrfRouteMask_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1, 1, 3),
    _MplsVpnVrfRouteMask_Type()
)
mplsVpnVrfRouteMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteMask.setStatus("current")
_MplsVpnVrfRouteMaskAddrType_Type = InetAddressType
_MplsVpnVrfRouteMaskAddrType_Object = MibTableColumn
mplsVpnVrfRouteMaskAddrType = _MplsVpnVrfRouteMaskAddrType_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1, 1, 4),
    _MplsVpnVrfRouteMaskAddrType_Type()
)
mplsVpnVrfRouteMaskAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteMaskAddrType.setStatus("current")
_MplsVpnVrfRouteTos_Type = Unsigned32
_MplsVpnVrfRouteTos_Object = MibTableColumn
mplsVpnVrfRouteTos = _MplsVpnVrfRouteTos_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1, 1, 5),
    _MplsVpnVrfRouteTos_Type()
)
mplsVpnVrfRouteTos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteTos.setStatus("current")
_MplsVpnVrfRouteNextHop_Type = InetAddress
_MplsVpnVrfRouteNextHop_Object = MibTableColumn
mplsVpnVrfRouteNextHop = _MplsVpnVrfRouteNextHop_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1, 1, 6),
    _MplsVpnVrfRouteNextHop_Type()
)
mplsVpnVrfRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteNextHop.setStatus("current")
_MplsVpnVrfRouteNextHopAddrType_Type = InetAddressType
_MplsVpnVrfRouteNextHopAddrType_Object = MibTableColumn
mplsVpnVrfRouteNextHopAddrType = _MplsVpnVrfRouteNextHopAddrType_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1, 1, 7),
    _MplsVpnVrfRouteNextHopAddrType_Type()
)
mplsVpnVrfRouteNextHopAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteNextHopAddrType.setStatus("current")
_MplsVpnVrfRouteIfIndex_Type = InterfaceIndex
_MplsVpnVrfRouteIfIndex_Object = MibTableColumn
mplsVpnVrfRouteIfIndex = _MplsVpnVrfRouteIfIndex_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1, 1, 8),
    _MplsVpnVrfRouteIfIndex_Type()
)
mplsVpnVrfRouteIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteIfIndex.setStatus("current")


class _MplsVpnVrfRouteType_Type(Integer32):
    """Custom type mplsVpnVrfRouteType based on Integer32"""
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
        *(("other", 1),
          ("reject", 2),
          ("local", 3),
          ("remote", 4))
    )


_MplsVpnVrfRouteType_Type.__name__ = "Integer32"
_MplsVpnVrfRouteType_Object = MibTableColumn
mplsVpnVrfRouteType = _MplsVpnVrfRouteType_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1, 1, 9),
    _MplsVpnVrfRouteType_Type()
)
mplsVpnVrfRouteType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteType.setStatus("current")


class _MplsVpnVrfRouteProto_Type(Integer32):
    """Custom type mplsVpnVrfRouteProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("local", 2),
          ("netmgmt", 3),
          ("icmp", 4),
          ("egp", 5),
          ("ggp", 6),
          ("hello", 7),
          ("rip", 8),
          ("isIs", 9),
          ("esIs", 10),
          ("ciscoIgrp", 11),
          ("bbnSpfIgp", 12),
          ("ospf", 13),
          ("bgp", 14),
          ("idpr", 15),
          ("ciscoEigrp", 16))
    )


_MplsVpnVrfRouteProto_Type.__name__ = "Integer32"
_MplsVpnVrfRouteProto_Object = MibTableColumn
mplsVpnVrfRouteProto = _MplsVpnVrfRouteProto_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1, 1, 10),
    _MplsVpnVrfRouteProto_Type()
)
mplsVpnVrfRouteProto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteProto.setStatus("current")
_MplsVpnVrfRouteAge_Type = Unsigned32
_MplsVpnVrfRouteAge_Object = MibTableColumn
mplsVpnVrfRouteAge = _MplsVpnVrfRouteAge_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1, 1, 11),
    _MplsVpnVrfRouteAge_Type()
)
mplsVpnVrfRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteAge.setStatus("current")
_MplsVpnVrfRouteInfo_Type = ObjectIdentifier
_MplsVpnVrfRouteInfo_Object = MibTableColumn
mplsVpnVrfRouteInfo = _MplsVpnVrfRouteInfo_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1, 1, 12),
    _MplsVpnVrfRouteInfo_Type()
)
mplsVpnVrfRouteInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteInfo.setStatus("current")
_MplsVpnVrfRouteNextHopAS_Type = Unsigned32
_MplsVpnVrfRouteNextHopAS_Object = MibTableColumn
mplsVpnVrfRouteNextHopAS = _MplsVpnVrfRouteNextHopAS_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1, 1, 13),
    _MplsVpnVrfRouteNextHopAS_Type()
)
mplsVpnVrfRouteNextHopAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteNextHopAS.setStatus("current")
_MplsVpnVrfRouteMetric1_Type = Integer32
_MplsVpnVrfRouteMetric1_Object = MibTableColumn
mplsVpnVrfRouteMetric1 = _MplsVpnVrfRouteMetric1_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1, 1, 14),
    _MplsVpnVrfRouteMetric1_Type()
)
mplsVpnVrfRouteMetric1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteMetric1.setStatus("current")
_MplsVpnVrfRouteMetric2_Type = Integer32
_MplsVpnVrfRouteMetric2_Object = MibTableColumn
mplsVpnVrfRouteMetric2 = _MplsVpnVrfRouteMetric2_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1, 1, 15),
    _MplsVpnVrfRouteMetric2_Type()
)
mplsVpnVrfRouteMetric2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteMetric2.setStatus("current")
_MplsVpnVrfRouteMetric3_Type = Integer32
_MplsVpnVrfRouteMetric3_Object = MibTableColumn
mplsVpnVrfRouteMetric3 = _MplsVpnVrfRouteMetric3_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1, 1, 16),
    _MplsVpnVrfRouteMetric3_Type()
)
mplsVpnVrfRouteMetric3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteMetric3.setStatus("current")
_MplsVpnVrfRouteMetric4_Type = Integer32
_MplsVpnVrfRouteMetric4_Object = MibTableColumn
mplsVpnVrfRouteMetric4 = _MplsVpnVrfRouteMetric4_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1, 1, 17),
    _MplsVpnVrfRouteMetric4_Type()
)
mplsVpnVrfRouteMetric4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteMetric4.setStatus("current")
_MplsVpnVrfRouteMetric5_Type = Integer32
_MplsVpnVrfRouteMetric5_Object = MibTableColumn
mplsVpnVrfRouteMetric5 = _MplsVpnVrfRouteMetric5_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1, 1, 18),
    _MplsVpnVrfRouteMetric5_Type()
)
mplsVpnVrfRouteMetric5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteMetric5.setStatus("current")
_MplsVpnVrfRouteRowStatus_Type = RowStatus
_MplsVpnVrfRouteRowStatus_Object = MibTableColumn
mplsVpnVrfRouteRowStatus = _MplsVpnVrfRouteRowStatus_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1, 1, 19),
    _MplsVpnVrfRouteRowStatus_Type()
)
mplsVpnVrfRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteRowStatus.setStatus("current")
_MplsVpnVrfRouteStorageType_Type = StorageType
_MplsVpnVrfRouteStorageType_Object = MibTableColumn
mplsVpnVrfRouteStorageType = _MplsVpnVrfRouteStorageType_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1, 1, 20),
    _MplsVpnVrfRouteStorageType_Type()
)
mplsVpnVrfRouteStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteStorageType.setStatus("current")
_MplsVpnConformance_ObjectIdentity = ObjectIdentity
mplsVpnConformance = _MplsVpnConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 118, 3)
)
_MplsVpnGroups_ObjectIdentity = ObjectIdentity
mplsVpnGroups = _MplsVpnGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 118, 3, 1)
)
_MplsVpnCompliances_ObjectIdentity = ObjectIdentity
mplsVpnCompliances = _MplsVpnCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 118, 3, 2)
)
mplsVpnVrfEntry.registerAugmentions(
    ("MPLS-VPN-MIB",
     "mplsVpnVrfSecEntry")
)
mplsVpnVrfSecEntry.setIndexNames(*mplsVpnVrfEntry.getIndexNames())
mplsVpnVrfEntry.registerAugmentions(
    ("MPLS-VPN-MIB",
     "mplsVpnVrfPerfEntry")
)
mplsVpnVrfPerfEntry.setIndexNames(*mplsVpnVrfEntry.getIndexNames())

# Managed Objects groups

mplsVpnScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 118, 3, 1, 1)
)
mplsVpnScalarGroup.setObjects(
      *(("MPLS-VPN-MIB", "mplsVpnConfiguredVrfs"),
        ("MPLS-VPN-MIB", "mplsVpnActiveVrfs"),
        ("MPLS-VPN-MIB", "mplsVpnConnectedInterfaces"),
        ("MPLS-VPN-MIB", "mplsVpnNotificationEnable"),
        ("MPLS-VPN-MIB", "mplsVpnVrfConfMaxPossibleRoutes"))
)
if mibBuilder.loadTexts:
    mplsVpnScalarGroup.setStatus("current")

mplsVpnVrfGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 118, 3, 1, 2)
)
mplsVpnVrfGroup.setObjects(
      *(("MPLS-VPN-MIB", "mplsVpnVrfDescription"),
        ("MPLS-VPN-MIB", "mplsVpnVrfRouteDistinguisher"),
        ("MPLS-VPN-MIB", "mplsVpnVrfCreationTime"),
        ("MPLS-VPN-MIB", "mplsVpnVrfOperStatus"),
        ("MPLS-VPN-MIB", "mplsVpnVrfActiveInterfaces"),
        ("MPLS-VPN-MIB", "mplsVpnVrfAssociatedInterfaces"),
        ("MPLS-VPN-MIB", "mplsVpnVrfConfMidRouteThreshold"),
        ("MPLS-VPN-MIB", "mplsVpnVrfConfHighRouteThreshold"),
        ("MPLS-VPN-MIB", "mplsVpnVrfConfMaxRoutes"),
        ("MPLS-VPN-MIB", "mplsVpnVrfConfLastChanged"),
        ("MPLS-VPN-MIB", "mplsVpnVrfConfRowStatus"),
        ("MPLS-VPN-MIB", "mplsVpnVrfConfStorageType"))
)
if mibBuilder.loadTexts:
    mplsVpnVrfGroup.setStatus("current")

mplsVpnInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 118, 3, 1, 3)
)
mplsVpnInterfaceGroup.setObjects(
      *(("MPLS-VPN-MIB", "mplsVpnInterfaceLabelEdgeType"),
        ("MPLS-VPN-MIB", "mplsVpnInterfaceVpnClassification"),
        ("MPLS-VPN-MIB", "mplsVpnInterfaceVpnRouteDistProtocol"),
        ("MPLS-VPN-MIB", "mplsVpnInterfaceConfStorageType"),
        ("MPLS-VPN-MIB", "mplsVpnInterfaceConfRowStatus"))
)
if mibBuilder.loadTexts:
    mplsVpnInterfaceGroup.setStatus("current")

mplsVpnPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 118, 3, 1, 4)
)
mplsVpnPerfGroup.setObjects(
      *(("MPLS-VPN-MIB", "mplsVpnVrfPerfRoutesAdded"),
        ("MPLS-VPN-MIB", "mplsVpnVrfPerfRoutesDeleted"),
        ("MPLS-VPN-MIB", "mplsVpnVrfPerfCurrNumRoutes"))
)
if mibBuilder.loadTexts:
    mplsVpnPerfGroup.setStatus("current")

mplsVpnVrfBgpNbrGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 118, 3, 1, 5)
)
mplsVpnVrfBgpNbrGroup.setObjects(
      *(("MPLS-VPN-MIB", "mplsVpnVrfBgpNbrRole"),
        ("MPLS-VPN-MIB", "mplsVpnVrfBgpNbrType"),
        ("MPLS-VPN-MIB", "mplsVpnVrfBgpNbrAddr"),
        ("MPLS-VPN-MIB", "mplsVpnVrfBgpNbrRowStatus"),
        ("MPLS-VPN-MIB", "mplsVpnVrfBgpNbrStorageType"))
)
if mibBuilder.loadTexts:
    mplsVpnVrfBgpNbrGroup.setStatus("current")

mplsVpnVrfBgpPrefixGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 118, 3, 1, 6)
)
mplsVpnVrfBgpPrefixGroup.setObjects(
      *(("MPLS-VPN-MIB", "mplsVpnVrfBgpPathAttrOrigin"),
        ("MPLS-VPN-MIB", "mplsVpnVrfBgpPathAttrASPathSegment"),
        ("MPLS-VPN-MIB", "mplsVpnVrfBgpPathAttrNextHop"),
        ("MPLS-VPN-MIB", "mplsVpnVrfBgpPathAttrMultiExitDisc"),
        ("MPLS-VPN-MIB", "mplsVpnVrfBgpPathAttrLocalPref"),
        ("MPLS-VPN-MIB", "mplsVpnVrfBgpPathAttrAtomicAggregate"),
        ("MPLS-VPN-MIB", "mplsVpnVrfBgpPathAttrAggregatorAS"),
        ("MPLS-VPN-MIB", "mplsVpnVrfBgpPathAttrAggregatorAddr"),
        ("MPLS-VPN-MIB", "mplsVpnVrfBgpPathAttrCalcLocalPref"),
        ("MPLS-VPN-MIB", "mplsVpnVrfBgpPathAttrBest"),
        ("MPLS-VPN-MIB", "mplsVpnVrfBgpPathAttrUnknown"))
)
if mibBuilder.loadTexts:
    mplsVpnVrfBgpPrefixGroup.setStatus("current")

mplsVpnSecGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 118, 3, 1, 7)
)
mplsVpnSecGroup.setObjects(
      *(("MPLS-VPN-MIB", "mplsVpnVrfSecIllegalLabelViolations"),
        ("MPLS-VPN-MIB", "mplsVpnVrfSecIllegalLabelRcvThresh"))
)
if mibBuilder.loadTexts:
    mplsVpnSecGroup.setStatus("current")

mplsVpnVrfRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 118, 3, 1, 8)
)
mplsVpnVrfRouteGroup.setObjects(
      *(("MPLS-VPN-MIB", "mplsVpnVrfRouteDestAddrType"),
        ("MPLS-VPN-MIB", "mplsVpnVrfRouteMaskAddrType"),
        ("MPLS-VPN-MIB", "mplsVpnVrfRouteNextHopAddrType"),
        ("MPLS-VPN-MIB", "mplsVpnVrfRouteIfIndex"),
        ("MPLS-VPN-MIB", "mplsVpnVrfRouteType"),
        ("MPLS-VPN-MIB", "mplsVpnVrfRouteProto"),
        ("MPLS-VPN-MIB", "mplsVpnVrfRouteAge"),
        ("MPLS-VPN-MIB", "mplsVpnVrfRouteInfo"),
        ("MPLS-VPN-MIB", "mplsVpnVrfRouteNextHopAS"),
        ("MPLS-VPN-MIB", "mplsVpnVrfRouteMetric1"),
        ("MPLS-VPN-MIB", "mplsVpnVrfRouteMetric2"),
        ("MPLS-VPN-MIB", "mplsVpnVrfRouteMetric3"),
        ("MPLS-VPN-MIB", "mplsVpnVrfRouteMetric4"),
        ("MPLS-VPN-MIB", "mplsVpnVrfRouteMetric5"),
        ("MPLS-VPN-MIB", "mplsVpnVrfRouteRowStatus"),
        ("MPLS-VPN-MIB", "mplsVpnVrfRouteStorageType"))
)
if mibBuilder.loadTexts:
    mplsVpnVrfRouteGroup.setStatus("current")

mplsVpnVrfRouteTargetGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 118, 3, 1, 9)
)
mplsVpnVrfRouteTargetGroup.setObjects(
      *(("MPLS-VPN-MIB", "mplsVpnVrfRouteTarget"),
        ("MPLS-VPN-MIB", "mplsVpnVrfRouteTargetDescr"),
        ("MPLS-VPN-MIB", "mplsVpnVrfRouteTargetRowStatus"))
)
if mibBuilder.loadTexts:
    mplsVpnVrfRouteTargetGroup.setStatus("current")


# Notification objects

mplsVrfIfUp = NotificationType(
    (1, 3, 6, 1, 3, 118, 0, 1)
)
if mibBuilder.loadTexts:
    mplsVrfIfUp.setStatus(
        "current"
    )

mplsVrfIfDown = NotificationType(
    (1, 3, 6, 1, 3, 118, 0, 2)
)
if mibBuilder.loadTexts:
    mplsVrfIfDown.setStatus(
        "current"
    )

mplsNumVrfRouteMidThreshExceeded = NotificationType(
    (1, 3, 6, 1, 3, 118, 0, 3)
)
if mibBuilder.loadTexts:
    mplsNumVrfRouteMidThreshExceeded.setStatus(
        "current"
    )

mplsNumVrfRouteMaxThreshExceeded = NotificationType(
    (1, 3, 6, 1, 3, 118, 0, 4)
)
if mibBuilder.loadTexts:
    mplsNumVrfRouteMaxThreshExceeded.setStatus(
        "current"
    )

mplsNumVrfSecIllegalLabelThreshExceeded = NotificationType(
    (1, 3, 6, 1, 3, 118, 0, 5)
)
if mibBuilder.loadTexts:
    mplsNumVrfSecIllegalLabelThreshExceeded.setStatus(
        "current"
    )


# Notifications groups

mplsVpnNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 3, 118, 3, 1, 10)
)
mplsVpnNotificationGroup.setObjects(
      *(("MPLS-VPN-MIB", "mplsVrfIfUp"),
        ("MPLS-VPN-MIB", "mplsVrfIfDown"),
        ("MPLS-VPN-MIB", "mplsNumVrfRouteMidThreshExceeded"),
        ("MPLS-VPN-MIB", "mplsNumVrfRouteMaxThreshExceeded"),
        ("MPLS-VPN-MIB", "mplsNumVrfSecIllegalLabelThreshExceeded"))
)
if mibBuilder.loadTexts:
    mplsVpnNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

mplsVpnModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 118, 3, 2, 1)
)
mplsVpnModuleCompliance.setObjects(
      *(("MPLS-VPN-MIB", "mplsVpnScalarGroup"),
        ("MPLS-VPN-MIB", "mplsVpnVrfGroup"),
        ("MPLS-VPN-MIB", "mplsVpnInterfaceGroup"),
        ("MPLS-VPN-MIB", "mplsVpnPerfGroup"),
        ("MPLS-VPN-MIB", "mplsVpnVrfRouteGroup"),
        ("MPLS-VPN-MIB", "mplsVpnVrfBgpNbrGroup"),
        ("MPLS-VPN-MIB", "mplsVpnVrfRouteTargetGroup"))
)
if mibBuilder.loadTexts:
    mplsVpnModuleCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPLS-VPN-MIB",
    **{"MplsVpnId": MplsVpnId,
       "MplsVpnRouteDistinguisher": MplsVpnRouteDistinguisher,
       "mplsVpnMIB": mplsVpnMIB,
       "mplsVpnNotifications": mplsVpnNotifications,
       "mplsVrfIfUp": mplsVrfIfUp,
       "mplsVrfIfDown": mplsVrfIfDown,
       "mplsNumVrfRouteMidThreshExceeded": mplsNumVrfRouteMidThreshExceeded,
       "mplsNumVrfRouteMaxThreshExceeded": mplsNumVrfRouteMaxThreshExceeded,
       "mplsNumVrfSecIllegalLabelThreshExceeded": mplsNumVrfSecIllegalLabelThreshExceeded,
       "mplsVpnObjects": mplsVpnObjects,
       "mplsVpnScalars": mplsVpnScalars,
       "mplsVpnConfiguredVrfs": mplsVpnConfiguredVrfs,
       "mplsVpnActiveVrfs": mplsVpnActiveVrfs,
       "mplsVpnConnectedInterfaces": mplsVpnConnectedInterfaces,
       "mplsVpnNotificationEnable": mplsVpnNotificationEnable,
       "mplsVpnVrfConfMaxPossibleRoutes": mplsVpnVrfConfMaxPossibleRoutes,
       "mplsVpnConf": mplsVpnConf,
       "mplsVpnInterfaceConfTable": mplsVpnInterfaceConfTable,
       "mplsVpnInterfaceConfEntry": mplsVpnInterfaceConfEntry,
       "mplsVpnInterfaceConfIndex": mplsVpnInterfaceConfIndex,
       "mplsVpnInterfaceLabelEdgeType": mplsVpnInterfaceLabelEdgeType,
       "mplsVpnInterfaceVpnClassification": mplsVpnInterfaceVpnClassification,
       "mplsVpnInterfaceVpnRouteDistProtocol": mplsVpnInterfaceVpnRouteDistProtocol,
       "mplsVpnInterfaceConfStorageType": mplsVpnInterfaceConfStorageType,
       "mplsVpnInterfaceConfRowStatus": mplsVpnInterfaceConfRowStatus,
       "mplsVpnVrfTable": mplsVpnVrfTable,
       "mplsVpnVrfEntry": mplsVpnVrfEntry,
       "mplsVpnVrfName": mplsVpnVrfName,
       "mplsVpnVrfDescription": mplsVpnVrfDescription,
       "mplsVpnVrfRouteDistinguisher": mplsVpnVrfRouteDistinguisher,
       "mplsVpnVrfCreationTime": mplsVpnVrfCreationTime,
       "mplsVpnVrfOperStatus": mplsVpnVrfOperStatus,
       "mplsVpnVrfActiveInterfaces": mplsVpnVrfActiveInterfaces,
       "mplsVpnVrfAssociatedInterfaces": mplsVpnVrfAssociatedInterfaces,
       "mplsVpnVrfConfMidRouteThreshold": mplsVpnVrfConfMidRouteThreshold,
       "mplsVpnVrfConfHighRouteThreshold": mplsVpnVrfConfHighRouteThreshold,
       "mplsVpnVrfConfMaxRoutes": mplsVpnVrfConfMaxRoutes,
       "mplsVpnVrfConfLastChanged": mplsVpnVrfConfLastChanged,
       "mplsVpnVrfConfRowStatus": mplsVpnVrfConfRowStatus,
       "mplsVpnVrfConfStorageType": mplsVpnVrfConfStorageType,
       "mplsVpnVrfRouteTargetTable": mplsVpnVrfRouteTargetTable,
       "mplsVpnVrfRouteTargetEntry": mplsVpnVrfRouteTargetEntry,
       "mplsVpnVrfRouteTargetIndex": mplsVpnVrfRouteTargetIndex,
       "mplsVpnVrfRouteTargetType": mplsVpnVrfRouteTargetType,
       "mplsVpnVrfRouteTarget": mplsVpnVrfRouteTarget,
       "mplsVpnVrfRouteTargetDescr": mplsVpnVrfRouteTargetDescr,
       "mplsVpnVrfRouteTargetRowStatus": mplsVpnVrfRouteTargetRowStatus,
       "mplsVpnVrfBgpNbrAddrTable": mplsVpnVrfBgpNbrAddrTable,
       "mplsVpnVrfBgpNbrAddrEntry": mplsVpnVrfBgpNbrAddrEntry,
       "mplsVpnVrfBgpNbrIndex": mplsVpnVrfBgpNbrIndex,
       "mplsVpnVrfBgpNbrRole": mplsVpnVrfBgpNbrRole,
       "mplsVpnVrfBgpNbrType": mplsVpnVrfBgpNbrType,
       "mplsVpnVrfBgpNbrAddr": mplsVpnVrfBgpNbrAddr,
       "mplsVpnVrfBgpNbrRowStatus": mplsVpnVrfBgpNbrRowStatus,
       "mplsVpnVrfBgpNbrStorageType": mplsVpnVrfBgpNbrStorageType,
       "mplsVpnVrfBgpNbrPrefixTable": mplsVpnVrfBgpNbrPrefixTable,
       "mplsVpnVrfBgpNbrPrefixEntry": mplsVpnVrfBgpNbrPrefixEntry,
       "mplsVpnVrfBgpPathAttrPeer": mplsVpnVrfBgpPathAttrPeer,
       "mplsVpnVrfBgpPathAttrIpAddrPrefixLen": mplsVpnVrfBgpPathAttrIpAddrPrefixLen,
       "mplsVpnVrfBgpPathAttrIpAddrPrefix": mplsVpnVrfBgpPathAttrIpAddrPrefix,
       "mplsVpnVrfBgpPathAttrOrigin": mplsVpnVrfBgpPathAttrOrigin,
       "mplsVpnVrfBgpPathAttrASPathSegment": mplsVpnVrfBgpPathAttrASPathSegment,
       "mplsVpnVrfBgpPathAttrNextHop": mplsVpnVrfBgpPathAttrNextHop,
       "mplsVpnVrfBgpPathAttrMultiExitDisc": mplsVpnVrfBgpPathAttrMultiExitDisc,
       "mplsVpnVrfBgpPathAttrLocalPref": mplsVpnVrfBgpPathAttrLocalPref,
       "mplsVpnVrfBgpPathAttrAtomicAggregate": mplsVpnVrfBgpPathAttrAtomicAggregate,
       "mplsVpnVrfBgpPathAttrAggregatorAS": mplsVpnVrfBgpPathAttrAggregatorAS,
       "mplsVpnVrfBgpPathAttrAggregatorAddr": mplsVpnVrfBgpPathAttrAggregatorAddr,
       "mplsVpnVrfBgpPathAttrCalcLocalPref": mplsVpnVrfBgpPathAttrCalcLocalPref,
       "mplsVpnVrfBgpPathAttrBest": mplsVpnVrfBgpPathAttrBest,
       "mplsVpnVrfBgpPathAttrUnknown": mplsVpnVrfBgpPathAttrUnknown,
       "mplsVpnVrfSecTable": mplsVpnVrfSecTable,
       "mplsVpnVrfSecEntry": mplsVpnVrfSecEntry,
       "mplsVpnVrfSecIllegalLabelViolations": mplsVpnVrfSecIllegalLabelViolations,
       "mplsVpnVrfSecIllegalLabelRcvThresh": mplsVpnVrfSecIllegalLabelRcvThresh,
       "mplsVpnPerf": mplsVpnPerf,
       "mplsVpnVrfPerfTable": mplsVpnVrfPerfTable,
       "mplsVpnVrfPerfEntry": mplsVpnVrfPerfEntry,
       "mplsVpnVrfPerfRoutesAdded": mplsVpnVrfPerfRoutesAdded,
       "mplsVpnVrfPerfRoutesDeleted": mplsVpnVrfPerfRoutesDeleted,
       "mplsVpnVrfPerfCurrNumRoutes": mplsVpnVrfPerfCurrNumRoutes,
       "mplsVpnRoute": mplsVpnRoute,
       "mplsVpnVrfRouteTable": mplsVpnVrfRouteTable,
       "mplsVpnVrfRouteEntry": mplsVpnVrfRouteEntry,
       "mplsVpnVrfRouteDest": mplsVpnVrfRouteDest,
       "mplsVpnVrfRouteDestAddrType": mplsVpnVrfRouteDestAddrType,
       "mplsVpnVrfRouteMask": mplsVpnVrfRouteMask,
       "mplsVpnVrfRouteMaskAddrType": mplsVpnVrfRouteMaskAddrType,
       "mplsVpnVrfRouteTos": mplsVpnVrfRouteTos,
       "mplsVpnVrfRouteNextHop": mplsVpnVrfRouteNextHop,
       "mplsVpnVrfRouteNextHopAddrType": mplsVpnVrfRouteNextHopAddrType,
       "mplsVpnVrfRouteIfIndex": mplsVpnVrfRouteIfIndex,
       "mplsVpnVrfRouteType": mplsVpnVrfRouteType,
       "mplsVpnVrfRouteProto": mplsVpnVrfRouteProto,
       "mplsVpnVrfRouteAge": mplsVpnVrfRouteAge,
       "mplsVpnVrfRouteInfo": mplsVpnVrfRouteInfo,
       "mplsVpnVrfRouteNextHopAS": mplsVpnVrfRouteNextHopAS,
       "mplsVpnVrfRouteMetric1": mplsVpnVrfRouteMetric1,
       "mplsVpnVrfRouteMetric2": mplsVpnVrfRouteMetric2,
       "mplsVpnVrfRouteMetric3": mplsVpnVrfRouteMetric3,
       "mplsVpnVrfRouteMetric4": mplsVpnVrfRouteMetric4,
       "mplsVpnVrfRouteMetric5": mplsVpnVrfRouteMetric5,
       "mplsVpnVrfRouteRowStatus": mplsVpnVrfRouteRowStatus,
       "mplsVpnVrfRouteStorageType": mplsVpnVrfRouteStorageType,
       "mplsVpnConformance": mplsVpnConformance,
       "mplsVpnGroups": mplsVpnGroups,
       "mplsVpnScalarGroup": mplsVpnScalarGroup,
       "mplsVpnVrfGroup": mplsVpnVrfGroup,
       "mplsVpnInterfaceGroup": mplsVpnInterfaceGroup,
       "mplsVpnPerfGroup": mplsVpnPerfGroup,
       "mplsVpnVrfBgpNbrGroup": mplsVpnVrfBgpNbrGroup,
       "mplsVpnVrfBgpPrefixGroup": mplsVpnVrfBgpPrefixGroup,
       "mplsVpnSecGroup": mplsVpnSecGroup,
       "mplsVpnVrfRouteGroup": mplsVpnVrfRouteGroup,
       "mplsVpnVrfRouteTargetGroup": mplsVpnVrfRouteTargetGroup,
       "mplsVpnNotificationGroup": mplsVpnNotificationGroup,
       "mplsVpnCompliances": mplsVpnCompliances,
       "mplsVpnModuleCompliance": mplsVpnModuleCompliance}
)
