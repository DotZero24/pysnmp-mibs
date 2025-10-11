# SNMP MIB module (FS-MAPINFO-MNG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-MAPINFO-MNG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:14:31 2025
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

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "FS-TC",
    "ConfigStatus",
    "IfIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(radiusAccClientServerPortNumber,
 radiusAccServerAddress) = mibBuilder.importSymbols(
    "RADIUS-ACC-CLIENT-MIB",
    "radiusAccClientServerPortNumber",
    "radiusAccServerAddress")

(radiusAuthClientServerPortNumber,
 radiusAuthServerAddress) = mibBuilder.importSymbols(
    "RADIUS-AUTH-CLIENT-MIB",
    "radiusAuthClientServerPortNumber",
    "radiusAuthServerAddress")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsMapinfoMngMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 150)
)
if mibBuilder.loadTexts:
    fsMapinfoMngMIB.setRevisions(
        ("2016-07-03 20:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsMapinfoMngMIBObjects_ObjectIdentity = ObjectIdentity
fsMapinfoMngMIBObjects = _FsMapinfoMngMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 150, 1)
)
_FsUserObjects_ObjectIdentity = ObjectIdentity
fsUserObjects = _FsUserObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 150, 1, 1)
)
_FsUserTable_Object = MibTable
fsUserTable = _FsUserTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 150, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fsUserTable.setStatus("current")
_FsUserEntry_Object = MibTableRow
fsUserEntry = _FsUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 150, 1, 1, 1, 1)
)
fsUserEntry.setIndexNames(
    (0, "FS-MAPINFO-MNG-MIB", "fsUserMacAddress"),
    (0, "FS-MAPINFO-MNG-MIB", "fsUserVid"),
)
if mibBuilder.loadTexts:
    fsUserEntry.setStatus("current")
_FsUserMacAddress_Type = MacAddress
_FsUserMacAddress_Object = MibTableColumn
fsUserMacAddress = _FsUserMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 150, 1, 1, 1, 1, 1),
    _FsUserMacAddress_Type()
)
fsUserMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsUserMacAddress.setStatus("current")
_FsUserVid_Type = Unsigned32
_FsUserVid_Object = MibTableColumn
fsUserVid = _FsUserVid_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 150, 1, 1, 1, 1, 2),
    _FsUserVid_Type()
)
fsUserVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsUserVid.setStatus("current")
_FsUserDevMacAddress_Type = MacAddress
_FsUserDevMacAddress_Object = MibTableColumn
fsUserDevMacAddress = _FsUserDevMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 150, 1, 1, 1, 1, 3),
    _FsUserDevMacAddress_Type()
)
fsUserDevMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsUserDevMacAddress.setStatus("current")
_FsUserDevSlot_Type = Unsigned32
_FsUserDevSlot_Object = MibTableColumn
fsUserDevSlot = _FsUserDevSlot_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 150, 1, 1, 1, 1, 4),
    _FsUserDevSlot_Type()
)
fsUserDevSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsUserDevSlot.setStatus("current")
_FsUserMapPort_Type = Unsigned32
_FsUserMapPort_Object = MibTableColumn
fsUserMapPort = _FsUserMapPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 150, 1, 1, 1, 1, 5),
    _FsUserMapPort_Type()
)
fsUserMapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsUserMapPort.setStatus("current")
_FsUserRowStatus_Type = ConfigStatus
_FsUserRowStatus_Object = MibTableColumn
fsUserRowStatus = _FsUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 150, 1, 1, 1, 1, 6),
    _FsUserRowStatus_Type()
)
fsUserRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsUserRowStatus.setStatus("current")
_FsFluxObjects_ObjectIdentity = ObjectIdentity
fsFluxObjects = _FsFluxObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 150, 1, 2)
)
_FsFluxTable_Object = MibTable
fsFluxTable = _FsFluxTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 150, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fsFluxTable.setStatus("current")
_FsFluxEntry_Object = MibTableRow
fsFluxEntry = _FsFluxEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 150, 1, 2, 1, 1)
)
fsFluxEntry.setIndexNames(
    (0, "FS-MAPINFO-MNG-MIB", "fsFluxDevMacAddress"),
    (0, "FS-MAPINFO-MNG-MIB", "fsFluxDevSlot"),
    (0, "FS-MAPINFO-MNG-MIB", "fsFluxMapPort"),
)
if mibBuilder.loadTexts:
    fsFluxEntry.setStatus("current")
_FsFluxDevMacAddress_Type = MacAddress
_FsFluxDevMacAddress_Object = MibTableColumn
fsFluxDevMacAddress = _FsFluxDevMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 150, 1, 2, 1, 1, 1),
    _FsFluxDevMacAddress_Type()
)
fsFluxDevMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFluxDevMacAddress.setStatus("current")
_FsFluxDevSlot_Type = Unsigned32
_FsFluxDevSlot_Object = MibTableColumn
fsFluxDevSlot = _FsFluxDevSlot_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 150, 1, 2, 1, 1, 2),
    _FsFluxDevSlot_Type()
)
fsFluxDevSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFluxDevSlot.setStatus("current")
_FsFluxMapPort_Type = Unsigned32
_FsFluxMapPort_Object = MibTableColumn
fsFluxMapPort = _FsFluxMapPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 150, 1, 2, 1, 1, 3),
    _FsFluxMapPort_Type()
)
fsFluxMapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFluxMapPort.setStatus("current")


class _FsFluxMapPortState_Type(Integer32):
    """Custom type fsFluxMapPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FsFluxMapPortState_Type.__name__ = "Integer32"
_FsFluxMapPortState_Object = MibTableColumn
fsFluxMapPortState = _FsFluxMapPortState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 150, 1, 2, 1, 1, 4),
    _FsFluxMapPortState_Type()
)
fsFluxMapPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFluxMapPortState.setStatus("current")
_FsFluxInputBps_Type = Counter64
_FsFluxInputBps_Object = MibTableColumn
fsFluxInputBps = _FsFluxInputBps_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 150, 1, 2, 1, 1, 5),
    _FsFluxInputBps_Type()
)
fsFluxInputBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFluxInputBps.setStatus("current")
_FsFluxOutputBps_Type = Counter64
_FsFluxOutputBps_Object = MibTableColumn
fsFluxOutputBps = _FsFluxOutputBps_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 150, 1, 2, 1, 1, 6),
    _FsFluxOutputBps_Type()
)
fsFluxOutputBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFluxOutputBps.setStatus("current")
_FsFluxInputPackets_Type = Counter64
_FsFluxInputPackets_Object = MibTableColumn
fsFluxInputPackets = _FsFluxInputPackets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 150, 1, 2, 1, 1, 7),
    _FsFluxInputPackets_Type()
)
fsFluxInputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFluxInputPackets.setStatus("current")
_FsFluxOutputPackets_Type = Counter64
_FsFluxOutputPackets_Object = MibTableColumn
fsFluxOutputPackets = _FsFluxOutputPackets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 150, 1, 2, 1, 1, 8),
    _FsFluxOutputPackets_Type()
)
fsFluxOutputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFluxOutputPackets.setStatus("current")
_FsFluxInputBytes_Type = Counter64
_FsFluxInputBytes_Object = MibTableColumn
fsFluxInputBytes = _FsFluxInputBytes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 150, 1, 2, 1, 1, 9),
    _FsFluxInputBytes_Type()
)
fsFluxInputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFluxInputBytes.setStatus("current")
_FsFluxOutputBytes_Type = Counter64
_FsFluxOutputBytes_Object = MibTableColumn
fsFluxOutputBytes = _FsFluxOutputBytes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 150, 1, 2, 1, 1, 10),
    _FsFluxOutputBytes_Type()
)
fsFluxOutputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFluxOutputBytes.setStatus("current")
_FsFluxRowStatus_Type = ConfigStatus
_FsFluxRowStatus_Object = MibTableColumn
fsFluxRowStatus = _FsFluxRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 150, 1, 2, 1, 1, 11),
    _FsFluxRowStatus_Type()
)
fsFluxRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsFluxRowStatus.setStatus("current")
_FsMapinfoMngMIBConformance_ObjectIdentity = ObjectIdentity
fsMapinfoMngMIBConformance = _FsMapinfoMngMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 150, 2)
)
_FsMapinfoMngMIBCompliances_ObjectIdentity = ObjectIdentity
fsMapinfoMngMIBCompliances = _FsMapinfoMngMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 150, 2, 1)
)
_FsMapinfoMngMIBGroups_ObjectIdentity = ObjectIdentity
fsMapinfoMngMIBGroups = _FsMapinfoMngMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 150, 2, 2)
)

# Managed Objects groups

fsUserMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 150, 2, 2, 1)
)
fsUserMIBGroup.setObjects(
      *(("FS-MAPINFO-MNG-MIB", "fsUserMacAddress"),
        ("FS-MAPINFO-MNG-MIB", "fsUserVid"),
        ("FS-MAPINFO-MNG-MIB", "fsUserDevMacAddress"),
        ("FS-MAPINFO-MNG-MIB", "fsUserDevSlot"),
        ("FS-MAPINFO-MNG-MIB", "fsUserMapPort"),
        ("FS-MAPINFO-MNG-MIB", "fsUserRowStatus"))
)
if mibBuilder.loadTexts:
    fsUserMIBGroup.setStatus("current")

fsFluxMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 150, 2, 2, 2)
)
fsFluxMIBGroup.setObjects(
      *(("FS-MAPINFO-MNG-MIB", "fsFluxDevMacAddress"),
        ("FS-MAPINFO-MNG-MIB", "fsFluxDevSlot"),
        ("FS-MAPINFO-MNG-MIB", "fsFluxMapPort"),
        ("FS-MAPINFO-MNG-MIB", "fsFluxMapPortState"),
        ("FS-MAPINFO-MNG-MIB", "fsFluxInputBps"),
        ("FS-MAPINFO-MNG-MIB", "fsFluxOutputBps"),
        ("FS-MAPINFO-MNG-MIB", "fsFluxInputPackets"),
        ("FS-MAPINFO-MNG-MIB", "fsFluxOutputPackets"),
        ("FS-MAPINFO-MNG-MIB", "fsFluxInputBytes"),
        ("FS-MAPINFO-MNG-MIB", "fsFluxOutputBytes"),
        ("FS-MAPINFO-MNG-MIB", "fsFluxRowStatus"))
)
if mibBuilder.loadTexts:
    fsFluxMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsMapinfoMngMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 150, 2, 1, 1)
)
fsMapinfoMngMIBCompliance.setObjects(
      *(("FS-MAPINFO-MNG-MIB", "fsUserMIBGroup"),
        ("FS-MAPINFO-MNG-MIB", "fsFluxMIBGroup"))
)
if mibBuilder.loadTexts:
    fsMapinfoMngMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-MAPINFO-MNG-MIB",
    **{"fsMapinfoMngMIB": fsMapinfoMngMIB,
       "fsMapinfoMngMIBObjects": fsMapinfoMngMIBObjects,
       "fsUserObjects": fsUserObjects,
       "fsUserTable": fsUserTable,
       "fsUserEntry": fsUserEntry,
       "fsUserMacAddress": fsUserMacAddress,
       "fsUserVid": fsUserVid,
       "fsUserDevMacAddress": fsUserDevMacAddress,
       "fsUserDevSlot": fsUserDevSlot,
       "fsUserMapPort": fsUserMapPort,
       "fsUserRowStatus": fsUserRowStatus,
       "fsFluxObjects": fsFluxObjects,
       "fsFluxTable": fsFluxTable,
       "fsFluxEntry": fsFluxEntry,
       "fsFluxDevMacAddress": fsFluxDevMacAddress,
       "fsFluxDevSlot": fsFluxDevSlot,
       "fsFluxMapPort": fsFluxMapPort,
       "fsFluxMapPortState": fsFluxMapPortState,
       "fsFluxInputBps": fsFluxInputBps,
       "fsFluxOutputBps": fsFluxOutputBps,
       "fsFluxInputPackets": fsFluxInputPackets,
       "fsFluxOutputPackets": fsFluxOutputPackets,
       "fsFluxInputBytes": fsFluxInputBytes,
       "fsFluxOutputBytes": fsFluxOutputBytes,
       "fsFluxRowStatus": fsFluxRowStatus,
       "fsMapinfoMngMIBConformance": fsMapinfoMngMIBConformance,
       "fsMapinfoMngMIBCompliances": fsMapinfoMngMIBCompliances,
       "fsMapinfoMngMIBCompliance": fsMapinfoMngMIBCompliance,
       "fsMapinfoMngMIBGroups": fsMapinfoMngMIBGroups,
       "fsUserMIBGroup": fsUserMIBGroup,
       "fsFluxMIBGroup": fsFluxMIBGroup}
)
