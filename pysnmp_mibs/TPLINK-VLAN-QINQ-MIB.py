# SNMP MIB module (TPLINK-VLAN-QINQ-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/tplink/TPLINK-VLAN-QINQ-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:56:32 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")

(TPRowStatus,) = mibBuilder.importSymbols(
    "TPLINK-TC-MIB",
    "TPRowStatus")


# MODULE-IDENTITY

tplinkQinqVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17)
)
if mibBuilder.loadTexts:
    tplinkQinqVlanMIB.setRevisions(
        ("2008-12-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkQinqVlanMIBObjects_ObjectIdentity = ObjectIdentity
tplinkQinqVlanMIBObjects = _TplinkQinqVlanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17, 1)
)


class _VpnConfigVpnMode_Type(Integer32):
    """Custom type vpnConfigVpnMode based on Integer32"""
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


_VpnConfigVpnMode_Type.__name__ = "Integer32"
_VpnConfigVpnMode_Object = MibScalar
vpnConfigVpnMode = _VpnConfigVpnMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17, 1, 1),
    _VpnConfigVpnMode_Type()
)
vpnConfigVpnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpnConfigVpnMode.setStatus("current")
_VpnConfigPort_ObjectIdentity = ObjectIdentity
vpnConfigPort = _VpnConfigPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17, 1, 2)
)
_VpnConfigPortTable_Object = MibTable
vpnConfigPortTable = _VpnConfigPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17, 1, 2, 1)
)
if mibBuilder.loadTexts:
    vpnConfigPortTable.setStatus("current")
_VpnConfigPortEntry_Object = MibTableRow
vpnConfigPortEntry = _VpnConfigPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17, 1, 2, 1, 1)
)
vpnConfigPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vpnConfigPortEntry.setStatus("current")


class _VpnConfigPortNumber_Type(OctetString):
    """Custom type vpnConfigPortNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VpnConfigPortNumber_Type.__name__ = "OctetString"
_VpnConfigPortNumber_Object = MibTableColumn
vpnConfigPortNumber = _VpnConfigPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17, 1, 2, 1, 1, 1),
    _VpnConfigPortNumber_Type()
)
vpnConfigPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnConfigPortNumber.setStatus("current")


class _VpnConfigPortType_Type(Integer32):
    """Custom type vpnConfigPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("nni", 1),
          ("uni", 2))
    )


_VpnConfigPortType_Type.__name__ = "Integer32"
_VpnConfigPortType_Object = MibTableColumn
vpnConfigPortType = _VpnConfigPortType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17, 1, 2, 1, 1, 2),
    _VpnConfigPortType_Type()
)
vpnConfigPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpnConfigPortType.setStatus("current")


class _VpnConfigPortTpid_Type(OctetString):
    """Custom type vpnConfigPortTpid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_VpnConfigPortTpid_Type.__name__ = "OctetString"
_VpnConfigPortTpid_Object = MibTableColumn
vpnConfigPortTpid = _VpnConfigPortTpid_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17, 1, 2, 1, 1, 3),
    _VpnConfigPortTpid_Type()
)
vpnConfigPortTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpnConfigPortTpid.setStatus("current")


class _VpnConfigUseInnerPriority_Type(Integer32):
    """Custom type vpnConfigUseInnerPriority based on Integer32"""
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


_VpnConfigUseInnerPriority_Type.__name__ = "Integer32"
_VpnConfigUseInnerPriority_Object = MibTableColumn
vpnConfigUseInnerPriority = _VpnConfigUseInnerPriority_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17, 1, 2, 1, 1, 4),
    _VpnConfigUseInnerPriority_Type()
)
vpnConfigUseInnerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpnConfigUseInnerPriority.setStatus("current")


class _VpnConfigMissdrop_Type(Integer32):
    """Custom type vpnConfigMissdrop based on Integer32"""
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


_VpnConfigMissdrop_Type.__name__ = "Integer32"
_VpnConfigMissdrop_Object = MibTableColumn
vpnConfigMissdrop = _VpnConfigMissdrop_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17, 1, 2, 1, 1, 5),
    _VpnConfigMissdrop_Type()
)
vpnConfigMissdrop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpnConfigMissdrop.setStatus("current")


class _VpnConfigPortLag_Type(OctetString):
    """Custom type vpnConfigPortLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VpnConfigPortLag_Type.__name__ = "OctetString"
_VpnConfigPortLag_Object = MibTableColumn
vpnConfigPortLag = _VpnConfigPortLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17, 1, 2, 1, 1, 6),
    _VpnConfigPortLag_Type()
)
vpnConfigPortLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnConfigPortLag.setStatus("current")
_VpnConfigVlanMapping_ObjectIdentity = ObjectIdentity
vpnConfigVlanMapping = _VpnConfigVlanMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17, 1, 3)
)


class _VpnConfigVlanMappingMode_Type(Integer32):
    """Custom type vpnConfigVlanMappingMode based on Integer32"""
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


_VpnConfigVlanMappingMode_Type.__name__ = "Integer32"
_VpnConfigVlanMappingMode_Object = MibScalar
vpnConfigVlanMappingMode = _VpnConfigVlanMappingMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17, 1, 3, 1),
    _VpnConfigVlanMappingMode_Type()
)
vpnConfigVlanMappingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpnConfigVlanMappingMode.setStatus("current")
_VpnConfigVlanMappingTable_Object = MibTable
vpnConfigVlanMappingTable = _VpnConfigVlanMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17, 1, 3, 2)
)
if mibBuilder.loadTexts:
    vpnConfigVlanMappingTable.setStatus("current")
_VpnConfigVlanMappingEntry_Object = MibTableRow
vpnConfigVlanMappingEntry = _VpnConfigVlanMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17, 1, 3, 2, 1)
)
vpnConfigVlanMappingEntry.setIndexNames(
    (0, "TPLINK-VLAN-QINQ-MIB", "vpnConfigVlanMappingCVlan"),
    (0, "TPLINK-VLAN-QINQ-MIB", "vpnConfigVlanMappingPort"),
)
if mibBuilder.loadTexts:
    vpnConfigVlanMappingEntry.setStatus("current")
_VpnConfigVlanMappingPort_Type = OctetString
_VpnConfigVlanMappingPort_Object = MibTableColumn
vpnConfigVlanMappingPort = _VpnConfigVlanMappingPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17, 1, 3, 2, 1, 1),
    _VpnConfigVlanMappingPort_Type()
)
vpnConfigVlanMappingPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vpnConfigVlanMappingPort.setStatus("current")


class _VpnConfigVlanMappingCVlan_Type(Integer32):
    """Custom type vpnConfigVlanMappingCVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VpnConfigVlanMappingCVlan_Type.__name__ = "Integer32"
_VpnConfigVlanMappingCVlan_Object = MibTableColumn
vpnConfigVlanMappingCVlan = _VpnConfigVlanMappingCVlan_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17, 1, 3, 2, 1, 2),
    _VpnConfigVlanMappingCVlan_Type()
)
vpnConfigVlanMappingCVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vpnConfigVlanMappingCVlan.setStatus("current")


class _VpnConfigVlanMappingSPVlan_Type(Integer32):
    """Custom type vpnConfigVlanMappingSPVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VpnConfigVlanMappingSPVlan_Type.__name__ = "Integer32"
_VpnConfigVlanMappingSPVlan_Object = MibTableColumn
vpnConfigVlanMappingSPVlan = _VpnConfigVlanMappingSPVlan_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17, 1, 3, 2, 1, 3),
    _VpnConfigVlanMappingSPVlan_Type()
)
vpnConfigVlanMappingSPVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vpnConfigVlanMappingSPVlan.setStatus("current")
_VpnConfigVlanMappingDesc_Type = OctetString
_VpnConfigVlanMappingDesc_Object = MibTableColumn
vpnConfigVlanMappingDesc = _VpnConfigVlanMappingDesc_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17, 1, 3, 2, 1, 4),
    _VpnConfigVlanMappingDesc_Type()
)
vpnConfigVlanMappingDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vpnConfigVlanMappingDesc.setStatus("current")
_VpnConfigVlanMappingStatus_Type = TPRowStatus
_VpnConfigVlanMappingStatus_Object = MibTableColumn
vpnConfigVlanMappingStatus = _VpnConfigVlanMappingStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17, 1, 3, 2, 1, 5),
    _VpnConfigVlanMappingStatus_Type()
)
vpnConfigVlanMappingStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vpnConfigVlanMappingStatus.setStatus("current")
_TplinkQinqVlanMIBNotifications_ObjectIdentity = ObjectIdentity
tplinkQinqVlanMIBNotifications = _TplinkQinqVlanMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-VLAN-QINQ-MIB",
    **{"tplinkQinqVlanMIB": tplinkQinqVlanMIB,
       "tplinkQinqVlanMIBObjects": tplinkQinqVlanMIBObjects,
       "vpnConfigVpnMode": vpnConfigVpnMode,
       "vpnConfigPort": vpnConfigPort,
       "vpnConfigPortTable": vpnConfigPortTable,
       "vpnConfigPortEntry": vpnConfigPortEntry,
       "vpnConfigPortNumber": vpnConfigPortNumber,
       "vpnConfigPortType": vpnConfigPortType,
       "vpnConfigPortTpid": vpnConfigPortTpid,
       "vpnConfigUseInnerPriority": vpnConfigUseInnerPriority,
       "vpnConfigMissdrop": vpnConfigMissdrop,
       "vpnConfigPortLag": vpnConfigPortLag,
       "vpnConfigVlanMapping": vpnConfigVlanMapping,
       "vpnConfigVlanMappingMode": vpnConfigVlanMappingMode,
       "vpnConfigVlanMappingTable": vpnConfigVlanMappingTable,
       "vpnConfigVlanMappingEntry": vpnConfigVlanMappingEntry,
       "vpnConfigVlanMappingPort": vpnConfigVlanMappingPort,
       "vpnConfigVlanMappingCVlan": vpnConfigVlanMappingCVlan,
       "vpnConfigVlanMappingSPVlan": vpnConfigVlanMappingSPVlan,
       "vpnConfigVlanMappingDesc": vpnConfigVlanMappingDesc,
       "vpnConfigVlanMappingStatus": vpnConfigVlanMappingStatus,
       "tplinkQinqVlanMIBNotifications": tplinkQinqVlanMIBNotifications}
)
