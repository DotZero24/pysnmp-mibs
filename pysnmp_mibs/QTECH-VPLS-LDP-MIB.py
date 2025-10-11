# SNMP MIB module (QTECH-VPLS-LDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-VPLS-LDP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:57:12 2025
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

(IANAPwCapabilities,
 IANAPwPsnTypeTC,
 IANAPwTypeTC) = mibBuilder.importSymbols(
    "IANA-PWE3-MIB",
    "IANAPwCapabilities",
    "IANAPwPsnTypeTC",
    "IANAPwTypeTC")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

(qtechvplsConfigIndex,
 qtechvplsPwBindIndex) = mibBuilder.importSymbols(
    "QTECH-VPLS-GENERIC-MIB",
    "qtechvplsConfigIndex",
    "qtechvplsPwBindIndex")

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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

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

qtechvplsLdpDraft01MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 78)
)
if mibBuilder.loadTexts:
    qtechvplsLdpDraft01MIB.setRevisions(
        ("2010-04-28 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechvplsLdpNotifications_ObjectIdentity = ObjectIdentity
qtechvplsLdpNotifications = _QtechvplsLdpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 78, 0)
)
_QtechvplsLdpObjects_ObjectIdentity = ObjectIdentity
qtechvplsLdpObjects = _QtechvplsLdpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 78, 1)
)
_QtechvplsLdpConfigTable_Object = MibTable
qtechvplsLdpConfigTable = _QtechvplsLdpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 78, 1, 1)
)
if mibBuilder.loadTexts:
    qtechvplsLdpConfigTable.setStatus("current")
_QtechvplsLdpConfigEntry_Object = MibTableRow
qtechvplsLdpConfigEntry = _QtechvplsLdpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 78, 1, 1, 1)
)
qtechvplsLdpConfigEntry.setIndexNames(
    (0, "QTECH-VPLS-GENERIC-MIB", "qtechvplsConfigIndex"),
    (0, "QTECH-VPLS-LDP-MIB", "qtechvplsLdpPwIndex"),
)
if mibBuilder.loadTexts:
    qtechvplsLdpConfigEntry.setStatus("current")
_QtechvplsLdpPwIndex_Type = Unsigned32
_QtechvplsLdpPwIndex_Object = MibTableColumn
qtechvplsLdpPwIndex = _QtechvplsLdpPwIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 78, 1, 1, 1, 1),
    _QtechvplsLdpPwIndex_Type()
)
qtechvplsLdpPwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechvplsLdpPwIndex.setStatus("current")
_QtechvplsLdpPeerAddr_Type = InetAddress
_QtechvplsLdpPeerAddr_Object = MibTableColumn
qtechvplsLdpPeerAddr = _QtechvplsLdpPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 78, 1, 1, 1, 2),
    _QtechvplsLdpPeerAddr_Type()
)
qtechvplsLdpPeerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechvplsLdpPeerAddr.setStatus("current")


class _QtechvplsLdpPwId_Type(Unsigned32):
    """Custom type qtechvplsLdpPwId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_QtechvplsLdpPwId_Type.__name__ = "Unsigned32"
_QtechvplsLdpPwId_Object = MibTableColumn
qtechvplsLdpPwId = _QtechvplsLdpPwId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 78, 1, 1, 1, 3),
    _QtechvplsLdpPwId_Type()
)
qtechvplsLdpPwId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechvplsLdpPwId.setStatus("current")


class _QtechvplsPwType_Type(Integer32):
    """Custom type qtechvplsPwType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mesh", 1),
          ("spoke", 2))
    )


_QtechvplsPwType_Type.__name__ = "Integer32"
_QtechvplsPwType_Object = MibTableColumn
qtechvplsPwType = _QtechvplsPwType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 78, 1, 1, 1, 4),
    _QtechvplsPwType_Type()
)
qtechvplsPwType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechvplsPwType.setStatus("current")
_QtechvplsPwEncapType_Type = IANAPwTypeTC
_QtechvplsPwEncapType_Object = MibTableColumn
qtechvplsPwEncapType = _QtechvplsPwEncapType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 78, 1, 1, 1, 5),
    _QtechvplsPwEncapType_Type()
)
qtechvplsPwEncapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechvplsPwEncapType.setStatus("current")
_QtechvplsLdpNeighborRowStatus_Type = RowStatus
_QtechvplsLdpNeighborRowStatus_Object = MibTableColumn
qtechvplsLdpNeighborRowStatus = _QtechvplsLdpNeighborRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 78, 1, 1, 1, 6),
    _QtechvplsLdpNeighborRowStatus_Type()
)
qtechvplsLdpNeighborRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechvplsLdpNeighborRowStatus.setStatus("current")
_QtechvplsLdpConformance_ObjectIdentity = ObjectIdentity
qtechvplsLdpConformance = _QtechvplsLdpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 78, 2)
)
_QtechvplsLdpCompliances_ObjectIdentity = ObjectIdentity
qtechvplsLdpCompliances = _QtechvplsLdpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 78, 2, 1)
)
_QtechvplsLdpGroups_ObjectIdentity = ObjectIdentity
qtechvplsLdpGroups = _QtechvplsLdpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 78, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechvplsLdpModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 78, 2, 1, 1)
)
qtechvplsLdpModuleFullCompliance.setObjects(
      *(("QTECH-VPLS-LDP-MIB", "qtechvplsLdpGroup"),
        ("QTECH-VPLS-LDP-MIB", "qtechvplsLdpNotificationGroup"))
)
if mibBuilder.loadTexts:
    qtechvplsLdpModuleFullCompliance.setStatus(
        "current"
    )

qtechvplsLdpModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 78, 2, 1, 2)
)
qtechvplsLdpModuleReadOnlyCompliance.setObjects(
      *(("QTECH-VPLS-LDP-MIB", "qtechvplsLdpGroup"),
        ("QTECH-VPLS-LDP-MIB", "qtechvplsLdpNotificationGroup"))
)
if mibBuilder.loadTexts:
    qtechvplsLdpModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-VPLS-LDP-MIB",
    **{"qtechvplsLdpDraft01MIB": qtechvplsLdpDraft01MIB,
       "qtechvplsLdpNotifications": qtechvplsLdpNotifications,
       "qtechvplsLdpObjects": qtechvplsLdpObjects,
       "qtechvplsLdpConfigTable": qtechvplsLdpConfigTable,
       "qtechvplsLdpConfigEntry": qtechvplsLdpConfigEntry,
       "qtechvplsLdpPwIndex": qtechvplsLdpPwIndex,
       "qtechvplsLdpPeerAddr": qtechvplsLdpPeerAddr,
       "qtechvplsLdpPwId": qtechvplsLdpPwId,
       "qtechvplsPwType": qtechvplsPwType,
       "qtechvplsPwEncapType": qtechvplsPwEncapType,
       "qtechvplsLdpNeighborRowStatus": qtechvplsLdpNeighborRowStatus,
       "qtechvplsLdpConformance": qtechvplsLdpConformance,
       "qtechvplsLdpCompliances": qtechvplsLdpCompliances,
       "qtechvplsLdpModuleFullCompliance": qtechvplsLdpModuleFullCompliance,
       "qtechvplsLdpModuleReadOnlyCompliance": qtechvplsLdpModuleReadOnlyCompliance,
       "qtechvplsLdpGroups": qtechvplsLdpGroups}
)
