# SNMP MIB module (FS-VPLS-LDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-VPLS-LDP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:14:40 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

(fsvplsConfigIndex,
 fsvplsPwBindIndex) = mibBuilder.importSymbols(
    "FS-VPLS-GENERIC-MIB",
    "fsvplsConfigIndex",
    "fsvplsPwBindIndex")

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

fsvplsLdpDraft01MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 78)
)
if mibBuilder.loadTexts:
    fsvplsLdpDraft01MIB.setRevisions(
        ("2010-04-28 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsvplsLdpNotifications_ObjectIdentity = ObjectIdentity
fsvplsLdpNotifications = _FsvplsLdpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 78, 0)
)
_FsvplsLdpObjects_ObjectIdentity = ObjectIdentity
fsvplsLdpObjects = _FsvplsLdpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 78, 1)
)
_FsvplsLdpConfigTable_Object = MibTable
fsvplsLdpConfigTable = _FsvplsLdpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 78, 1, 1)
)
if mibBuilder.loadTexts:
    fsvplsLdpConfigTable.setStatus("current")
_FsvplsLdpConfigEntry_Object = MibTableRow
fsvplsLdpConfigEntry = _FsvplsLdpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 78, 1, 1, 1)
)
fsvplsLdpConfigEntry.setIndexNames(
    (0, "FS-VPLS-GENERIC-MIB", "fsvplsConfigIndex"),
    (0, "FS-VPLS-LDP-MIB", "fsvplsLdpPwIndex"),
)
if mibBuilder.loadTexts:
    fsvplsLdpConfigEntry.setStatus("current")
_FsvplsLdpPwIndex_Type = Unsigned32
_FsvplsLdpPwIndex_Object = MibTableColumn
fsvplsLdpPwIndex = _FsvplsLdpPwIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 78, 1, 1, 1, 1),
    _FsvplsLdpPwIndex_Type()
)
fsvplsLdpPwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsvplsLdpPwIndex.setStatus("current")
_FsvplsLdpPeerAddr_Type = InetAddress
_FsvplsLdpPeerAddr_Object = MibTableColumn
fsvplsLdpPeerAddr = _FsvplsLdpPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 78, 1, 1, 1, 2),
    _FsvplsLdpPeerAddr_Type()
)
fsvplsLdpPeerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsvplsLdpPeerAddr.setStatus("current")


class _FsvplsLdpPwId_Type(Unsigned32):
    """Custom type fsvplsLdpPwId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsvplsLdpPwId_Type.__name__ = "Unsigned32"
_FsvplsLdpPwId_Object = MibTableColumn
fsvplsLdpPwId = _FsvplsLdpPwId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 78, 1, 1, 1, 3),
    _FsvplsLdpPwId_Type()
)
fsvplsLdpPwId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsvplsLdpPwId.setStatus("current")


class _FsvplsPwType_Type(Integer32):
    """Custom type fsvplsPwType based on Integer32"""
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


_FsvplsPwType_Type.__name__ = "Integer32"
_FsvplsPwType_Object = MibTableColumn
fsvplsPwType = _FsvplsPwType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 78, 1, 1, 1, 4),
    _FsvplsPwType_Type()
)
fsvplsPwType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsvplsPwType.setStatus("current")
_FsvplsPwEncapType_Type = IANAPwTypeTC
_FsvplsPwEncapType_Object = MibTableColumn
fsvplsPwEncapType = _FsvplsPwEncapType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 78, 1, 1, 1, 5),
    _FsvplsPwEncapType_Type()
)
fsvplsPwEncapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsvplsPwEncapType.setStatus("current")
_FsvplsLdpNeighborRowStatus_Type = RowStatus
_FsvplsLdpNeighborRowStatus_Object = MibTableColumn
fsvplsLdpNeighborRowStatus = _FsvplsLdpNeighborRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 78, 1, 1, 1, 6),
    _FsvplsLdpNeighborRowStatus_Type()
)
fsvplsLdpNeighborRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsvplsLdpNeighborRowStatus.setStatus("current")
_FsvplsLdpConformance_ObjectIdentity = ObjectIdentity
fsvplsLdpConformance = _FsvplsLdpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 78, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-VPLS-LDP-MIB",
    **{"fsvplsLdpDraft01MIB": fsvplsLdpDraft01MIB,
       "fsvplsLdpNotifications": fsvplsLdpNotifications,
       "fsvplsLdpObjects": fsvplsLdpObjects,
       "fsvplsLdpConfigTable": fsvplsLdpConfigTable,
       "fsvplsLdpConfigEntry": fsvplsLdpConfigEntry,
       "fsvplsLdpPwIndex": fsvplsLdpPwIndex,
       "fsvplsLdpPeerAddr": fsvplsLdpPeerAddr,
       "fsvplsLdpPwId": fsvplsLdpPwId,
       "fsvplsPwType": fsvplsPwType,
       "fsvplsPwEncapType": fsvplsPwEncapType,
       "fsvplsLdpNeighborRowStatus": fsvplsLdpNeighborRowStatus,
       "fsvplsLdpConformance": fsvplsLdpConformance}
)
