# SNMP MIB module (RAISECOM-RTDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-RTDP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:37:01 2025
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

(raisecomCluster,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "raisecomCluster")

(raisecomRndpDiscoveryDeviceId,) = mibBuilder.importSymbols(
    "RAISECOM-RNDP-MIB",
    "raisecomRndpDiscoveryDeviceId")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")

(EnableVar,
 PortList) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar",
    "PortList")


# MODULE-IDENTITY

raisecomTopoDiscovery = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _RaisecomRtdpCollectEnable_Type(EnableVar):
    """Custom type raisecomRtdpCollectEnable based on EnableVar"""
    defaultValue = 2


_RaisecomRtdpCollectEnable_Type.__name__ = "EnableVar"
_RaisecomRtdpCollectEnable_Object = MibScalar
raisecomRtdpCollectEnable = _RaisecomRtdpCollectEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 2, 4),
    _RaisecomRtdpCollectEnable_Type()
)
raisecomRtdpCollectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRtdpCollectEnable.setStatus("mandatory")


class _RaisecomRtdpReportEnable_Type(EnableVar):
    """Custom type raisecomRtdpReportEnable based on EnableVar"""
    defaultValue = 1


_RaisecomRtdpReportEnable_Type.__name__ = "EnableVar"
_RaisecomRtdpReportEnable_Object = MibScalar
raisecomRtdpReportEnable = _RaisecomRtdpReportEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 2, 5),
    _RaisecomRtdpReportEnable_Type()
)
raisecomRtdpReportEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRtdpReportEnable.setStatus("mandatory")


class _RaisecomRtdpMaxHops_Type(Integer32):
    """Custom type raisecomRtdpMaxHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_RaisecomRtdpMaxHops_Type.__name__ = "Integer32"
_RaisecomRtdpMaxHops_Object = MibScalar
raisecomRtdpMaxHops = _RaisecomRtdpMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 2, 6),
    _RaisecomRtdpMaxHops_Type()
)
raisecomRtdpMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRtdpMaxHops.setStatus("mandatory")
_RaisecomRtdpDeviceDiscoveryTable_Object = MibTable
raisecomRtdpDeviceDiscoveryTable = _RaisecomRtdpDeviceDiscoveryTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 2, 7)
)
if mibBuilder.loadTexts:
    raisecomRtdpDeviceDiscoveryTable.setStatus("current")
_RaisecomRtdpDeviceDiscoveryEntry_Object = MibTableRow
raisecomRtdpDeviceDiscoveryEntry = _RaisecomRtdpDeviceDiscoveryEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 2, 7, 1)
)
raisecomRtdpDeviceDiscoveryEntry.setIndexNames(
    (0, "RAISECOM-RNDP-MIB", "raisecomRndpDiscoveryDeviceId"),
)
if mibBuilder.loadTexts:
    raisecomRtdpDeviceDiscoveryEntry.setStatus("current")
_RaisecomRtdpDeviceDiscoveryDeviceId_Type = MacAddress
_RaisecomRtdpDeviceDiscoveryDeviceId_Object = MibTableColumn
raisecomRtdpDeviceDiscoveryDeviceId = _RaisecomRtdpDeviceDiscoveryDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 2, 7, 1, 1),
    _RaisecomRtdpDeviceDiscoveryDeviceId_Type()
)
raisecomRtdpDeviceDiscoveryDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRtdpDeviceDiscoveryDeviceId.setStatus("current")


class _RaisecomRtdpDeviceDiscoveryHops_Type(Integer32):
    """Custom type raisecomRtdpDeviceDiscoveryHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_RaisecomRtdpDeviceDiscoveryHops_Type.__name__ = "Integer32"
_RaisecomRtdpDeviceDiscoveryHops_Object = MibTableColumn
raisecomRtdpDeviceDiscoveryHops = _RaisecomRtdpDeviceDiscoveryHops_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 2, 7, 1, 2),
    _RaisecomRtdpDeviceDiscoveryHops_Type()
)
raisecomRtdpDeviceDiscoveryHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRtdpDeviceDiscoveryHops.setStatus("current")
_RaisecomRtdpDeviceDiscoveryHostName_Type = OctetString
_RaisecomRtdpDeviceDiscoveryHostName_Object = MibTableColumn
raisecomRtdpDeviceDiscoveryHostName = _RaisecomRtdpDeviceDiscoveryHostName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 2, 7, 1, 3),
    _RaisecomRtdpDeviceDiscoveryHostName_Type()
)
raisecomRtdpDeviceDiscoveryHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRtdpDeviceDiscoveryHostName.setStatus("current")
_RaisecomRtdpDeviceDiscoveryPlatformOid_Type = ObjectIdentifier
_RaisecomRtdpDeviceDiscoveryPlatformOid_Object = MibTableColumn
raisecomRtdpDeviceDiscoveryPlatformOid = _RaisecomRtdpDeviceDiscoveryPlatformOid_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 2, 7, 1, 4),
    _RaisecomRtdpDeviceDiscoveryPlatformOid_Type()
)
raisecomRtdpDeviceDiscoveryPlatformOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRtdpDeviceDiscoveryPlatformOid.setStatus("current")
_RaisecomRtdpDeviceDiscoveryVersion_Type = OctetString
_RaisecomRtdpDeviceDiscoveryVersion_Object = MibTableColumn
raisecomRtdpDeviceDiscoveryVersion = _RaisecomRtdpDeviceDiscoveryVersion_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 2, 7, 1, 5),
    _RaisecomRtdpDeviceDiscoveryVersion_Type()
)
raisecomRtdpDeviceDiscoveryVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRtdpDeviceDiscoveryVersion.setStatus("current")


class _RaisecomRtdpDeviceDiscoveryCapabilities_Type(Integer32):
    """Custom type raisecomRtdpDeviceDiscoveryCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("switch", 1),
          ("router", 2),
          ("eoa", 3),
          ("eos", 4),
          ("others", 5))
    )


_RaisecomRtdpDeviceDiscoveryCapabilities_Type.__name__ = "Integer32"
_RaisecomRtdpDeviceDiscoveryCapabilities_Object = MibTableColumn
raisecomRtdpDeviceDiscoveryCapabilities = _RaisecomRtdpDeviceDiscoveryCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 2, 7, 1, 6),
    _RaisecomRtdpDeviceDiscoveryCapabilities_Type()
)
raisecomRtdpDeviceDiscoveryCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRtdpDeviceDiscoveryCapabilities.setStatus("current")


class _RaisecomRtdpDeviceDiscoveryRole_Type(Integer32):
    """Custom type raisecomRtdpDeviceDiscoveryRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("member", 1),
          ("candidate", 2),
          ("commander", 3))
    )


_RaisecomRtdpDeviceDiscoveryRole_Type.__name__ = "Integer32"
_RaisecomRtdpDeviceDiscoveryRole_Object = MibTableColumn
raisecomRtdpDeviceDiscoveryRole = _RaisecomRtdpDeviceDiscoveryRole_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 2, 7, 1, 7),
    _RaisecomRtdpDeviceDiscoveryRole_Type()
)
raisecomRtdpDeviceDiscoveryRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRtdpDeviceDiscoveryRole.setStatus("current")
_RaisecomRtdpDeviceDiscoveryCommanderMac_Type = MacAddress
_RaisecomRtdpDeviceDiscoveryCommanderMac_Object = MibTableColumn
raisecomRtdpDeviceDiscoveryCommanderMac = _RaisecomRtdpDeviceDiscoveryCommanderMac_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 2, 7, 1, 8),
    _RaisecomRtdpDeviceDiscoveryCommanderMac_Type()
)
raisecomRtdpDeviceDiscoveryCommanderMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRtdpDeviceDiscoveryCommanderMac.setStatus("current")
_RaisecomRtdpDeviceDiscoveryAutoActive_Type = EnableVar
_RaisecomRtdpDeviceDiscoveryAutoActive_Object = MibTableColumn
raisecomRtdpDeviceDiscoveryAutoActive = _RaisecomRtdpDeviceDiscoveryAutoActive_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 2, 7, 1, 9),
    _RaisecomRtdpDeviceDiscoveryAutoActive_Type()
)
raisecomRtdpDeviceDiscoveryAutoActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRtdpDeviceDiscoveryAutoActive.setStatus("current")
_RaisecomRtdpDeviceDiscoveryAutoActiveMac_Type = MacAddress
_RaisecomRtdpDeviceDiscoveryAutoActiveMac_Object = MibTableColumn
raisecomRtdpDeviceDiscoveryAutoActiveMac = _RaisecomRtdpDeviceDiscoveryAutoActiveMac_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 2, 7, 1, 10),
    _RaisecomRtdpDeviceDiscoveryAutoActiveMac_Type()
)
raisecomRtdpDeviceDiscoveryAutoActiveMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRtdpDeviceDiscoveryAutoActiveMac.setStatus("current")
_RaisecomRtdpRelationshipTable_Object = MibTable
raisecomRtdpRelationshipTable = _RaisecomRtdpRelationshipTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 2, 8)
)
if mibBuilder.loadTexts:
    raisecomRtdpRelationshipTable.setStatus("current")
_RaisecomRtdpRelationshipEntry_Object = MibTableRow
raisecomRtdpRelationshipEntry = _RaisecomRtdpRelationshipEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 2, 8, 1)
)
raisecomRtdpRelationshipEntry.setIndexNames(
    (0, "RAISECOM-RTDP-MIB", "raisecomRtdpRelationshipDeviceId"),
    (0, "RAISECOM-RTDP-MIB", "raisecomRtdpRelationshipPeerDeviceId"),
)
if mibBuilder.loadTexts:
    raisecomRtdpRelationshipEntry.setStatus("current")
_RaisecomRtdpRelationshipDeviceId_Type = MacAddress
_RaisecomRtdpRelationshipDeviceId_Object = MibTableColumn
raisecomRtdpRelationshipDeviceId = _RaisecomRtdpRelationshipDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 2, 8, 1, 1),
    _RaisecomRtdpRelationshipDeviceId_Type()
)
raisecomRtdpRelationshipDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRtdpRelationshipDeviceId.setStatus("current")
_RaisecomRtdpRelationshipPeerDeviceId_Type = MacAddress
_RaisecomRtdpRelationshipPeerDeviceId_Object = MibTableColumn
raisecomRtdpRelationshipPeerDeviceId = _RaisecomRtdpRelationshipPeerDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 2, 8, 1, 2),
    _RaisecomRtdpRelationshipPeerDeviceId_Type()
)
raisecomRtdpRelationshipPeerDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRtdpRelationshipPeerDeviceId.setStatus("current")
_RaisecomRtdpRelationshipNativePort_Type = Integer32
_RaisecomRtdpRelationshipNativePort_Object = MibTableColumn
raisecomRtdpRelationshipNativePort = _RaisecomRtdpRelationshipNativePort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 2, 8, 1, 3),
    _RaisecomRtdpRelationshipNativePort_Type()
)
raisecomRtdpRelationshipNativePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRtdpRelationshipNativePort.setStatus("current")
_RaisecomRtdpRelationshipPeerPort_Type = Integer32
_RaisecomRtdpRelationshipPeerPort_Object = MibTableColumn
raisecomRtdpRelationshipPeerPort = _RaisecomRtdpRelationshipPeerPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 2, 8, 1, 4),
    _RaisecomRtdpRelationshipPeerPort_Type()
)
raisecomRtdpRelationshipPeerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRtdpRelationshipPeerPort.setStatus("current")


class _RaisecomRtdpControlVlan_Type(Integer32):
    """Custom type raisecomRtdpControlVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_RaisecomRtdpControlVlan_Type.__name__ = "Integer32"
_RaisecomRtdpControlVlan_Object = MibScalar
raisecomRtdpControlVlan = _RaisecomRtdpControlVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 2, 10),
    _RaisecomRtdpControlVlan_Type()
)
raisecomRtdpControlVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRtdpControlVlan.setStatus("current")
_RaisecomRtdpControlVlanPorts_Type = PortList
_RaisecomRtdpControlVlanPorts_Object = MibScalar
raisecomRtdpControlVlanPorts = _RaisecomRtdpControlVlanPorts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 2, 11),
    _RaisecomRtdpControlVlanPorts_Type()
)
raisecomRtdpControlVlanPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRtdpControlVlanPorts.setStatus("current")

# Managed Objects groups


# Notification objects

raisecomRtdpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 2, 9)
)
if mibBuilder.loadTexts:
    raisecomRtdpTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-RTDP-MIB",
    **{"raisecomTopoDiscovery": raisecomTopoDiscovery,
       "raisecomRtdpCollectEnable": raisecomRtdpCollectEnable,
       "raisecomRtdpReportEnable": raisecomRtdpReportEnable,
       "raisecomRtdpMaxHops": raisecomRtdpMaxHops,
       "raisecomRtdpDeviceDiscoveryTable": raisecomRtdpDeviceDiscoveryTable,
       "raisecomRtdpDeviceDiscoveryEntry": raisecomRtdpDeviceDiscoveryEntry,
       "raisecomRtdpDeviceDiscoveryDeviceId": raisecomRtdpDeviceDiscoveryDeviceId,
       "raisecomRtdpDeviceDiscoveryHops": raisecomRtdpDeviceDiscoveryHops,
       "raisecomRtdpDeviceDiscoveryHostName": raisecomRtdpDeviceDiscoveryHostName,
       "raisecomRtdpDeviceDiscoveryPlatformOid": raisecomRtdpDeviceDiscoveryPlatformOid,
       "raisecomRtdpDeviceDiscoveryVersion": raisecomRtdpDeviceDiscoveryVersion,
       "raisecomRtdpDeviceDiscoveryCapabilities": raisecomRtdpDeviceDiscoveryCapabilities,
       "raisecomRtdpDeviceDiscoveryRole": raisecomRtdpDeviceDiscoveryRole,
       "raisecomRtdpDeviceDiscoveryCommanderMac": raisecomRtdpDeviceDiscoveryCommanderMac,
       "raisecomRtdpDeviceDiscoveryAutoActive": raisecomRtdpDeviceDiscoveryAutoActive,
       "raisecomRtdpDeviceDiscoveryAutoActiveMac": raisecomRtdpDeviceDiscoveryAutoActiveMac,
       "raisecomRtdpRelationshipTable": raisecomRtdpRelationshipTable,
       "raisecomRtdpRelationshipEntry": raisecomRtdpRelationshipEntry,
       "raisecomRtdpRelationshipDeviceId": raisecomRtdpRelationshipDeviceId,
       "raisecomRtdpRelationshipPeerDeviceId": raisecomRtdpRelationshipPeerDeviceId,
       "raisecomRtdpRelationshipNativePort": raisecomRtdpRelationshipNativePort,
       "raisecomRtdpRelationshipPeerPort": raisecomRtdpRelationshipPeerPort,
       "raisecomRtdpTrap": raisecomRtdpTrap,
       "raisecomRtdpControlVlan": raisecomRtdpControlVlan,
       "raisecomRtdpControlVlanPorts": raisecomRtdpControlVlanPorts}
)
