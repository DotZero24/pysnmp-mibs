# SNMP MIB module (TPLINK-DHCPL2Relay-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/tplink/TPLINK-DHCPL2Relay-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:55:09 2025
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")


# MODULE-IDENTITY

tplinkDhcpL2RelayMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 66)
)
if mibBuilder.loadTexts:
    tplinkDhcpL2RelayMIB.setRevisions(
        ("2012-12-17 10:14",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkDhcpL2RelayMIBObjects_ObjectIdentity = ObjectIdentity
tplinkDhcpL2RelayMIBObjects = _TplinkDhcpL2RelayMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 66, 1)
)
_DhcpL2RelayGlobalConfig_ObjectIdentity = ObjectIdentity
dhcpL2RelayGlobalConfig = _DhcpL2RelayGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 66, 1, 1)
)


class _DhcpL2RelayEnable_Type(Integer32):
    """Custom type dhcpL2RelayEnable based on Integer32"""
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


_DhcpL2RelayEnable_Type.__name__ = "Integer32"
_DhcpL2RelayEnable_Object = MibScalar
dhcpL2RelayEnable = _DhcpL2RelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 66, 1, 1, 1),
    _DhcpL2RelayEnable_Type()
)
dhcpL2RelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpL2RelayEnable.setStatus("current")
_DhcpL2RelayVlanConfigTable_Object = MibTable
dhcpL2RelayVlanConfigTable = _DhcpL2RelayVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 66, 1, 1, 2)
)
if mibBuilder.loadTexts:
    dhcpL2RelayVlanConfigTable.setStatus("current")
_DhcpL2RelayVlanConfigEntry_Object = MibTableRow
dhcpL2RelayVlanConfigEntry = _DhcpL2RelayVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 66, 1, 1, 2, 1)
)
dhcpL2RelayVlanConfigEntry.setIndexNames(
    (0, "TPLINK-DHCPL2Relay-MIB", "dhcpL2RelayVlanId"),
)
if mibBuilder.loadTexts:
    dhcpL2RelayVlanConfigEntry.setStatus("current")


class _DhcpL2RelayVlanId_Type(Integer32):
    """Custom type dhcpL2RelayVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_DhcpL2RelayVlanId_Type.__name__ = "Integer32"
_DhcpL2RelayVlanId_Object = MibTableColumn
dhcpL2RelayVlanId = _DhcpL2RelayVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 66, 1, 1, 2, 1, 1),
    _DhcpL2RelayVlanId_Type()
)
dhcpL2RelayVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpL2RelayVlanId.setStatus("current")


class _DhcpL2RelayVlanStatus_Type(Integer32):
    """Custom type dhcpL2RelayVlanStatus based on Integer32"""
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


_DhcpL2RelayVlanStatus_Type.__name__ = "Integer32"
_DhcpL2RelayVlanStatus_Object = MibTableColumn
dhcpL2RelayVlanStatus = _DhcpL2RelayVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 66, 1, 1, 2, 1, 2),
    _DhcpL2RelayVlanStatus_Type()
)
dhcpL2RelayVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpL2RelayVlanStatus.setStatus("current")
_DhcpL2RelayOption82Config_ObjectIdentity = ObjectIdentity
dhcpL2RelayOption82Config = _DhcpL2RelayOption82Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 66, 1, 2)
)
_DhcpL2RelayOption82ConfigTable_Object = MibTable
dhcpL2RelayOption82ConfigTable = _DhcpL2RelayOption82ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 66, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dhcpL2RelayOption82ConfigTable.setStatus("current")
_DhcpL2RelayOption82ConfigEntry_Object = MibTableRow
dhcpL2RelayOption82ConfigEntry = _DhcpL2RelayOption82ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 66, 1, 2, 1, 1)
)
dhcpL2RelayOption82ConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dhcpL2RelayOption82ConfigEntry.setStatus("current")


class _DhcpL2RelayOption82ConfigPort_Type(OctetString):
    """Custom type dhcpL2RelayOption82ConfigPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DhcpL2RelayOption82ConfigPort_Type.__name__ = "OctetString"
_DhcpL2RelayOption82ConfigPort_Object = MibTableColumn
dhcpL2RelayOption82ConfigPort = _DhcpL2RelayOption82ConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 66, 1, 2, 1, 1, 1),
    _DhcpL2RelayOption82ConfigPort_Type()
)
dhcpL2RelayOption82ConfigPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpL2RelayOption82ConfigPort.setStatus("current")


class _DhcpL2RelayOption82ConfigSupportStatus_Type(Integer32):
    """Custom type dhcpL2RelayOption82ConfigSupportStatus based on Integer32"""
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


_DhcpL2RelayOption82ConfigSupportStatus_Type.__name__ = "Integer32"
_DhcpL2RelayOption82ConfigSupportStatus_Object = MibTableColumn
dhcpL2RelayOption82ConfigSupportStatus = _DhcpL2RelayOption82ConfigSupportStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 66, 1, 2, 1, 1, 2),
    _DhcpL2RelayOption82ConfigSupportStatus_Type()
)
dhcpL2RelayOption82ConfigSupportStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpL2RelayOption82ConfigSupportStatus.setStatus("current")


class _DhcpL2RelayOption82ConfigOperationStrategy_Type(Integer32):
    """Custom type dhcpL2RelayOption82ConfigOperationStrategy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("keep", 0),
          ("replace", 1),
          ("drop", 2))
    )


_DhcpL2RelayOption82ConfigOperationStrategy_Type.__name__ = "Integer32"
_DhcpL2RelayOption82ConfigOperationStrategy_Object = MibTableColumn
dhcpL2RelayOption82ConfigOperationStrategy = _DhcpL2RelayOption82ConfigOperationStrategy_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 66, 1, 2, 1, 1, 3),
    _DhcpL2RelayOption82ConfigOperationStrategy_Type()
)
dhcpL2RelayOption82ConfigOperationStrategy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpL2RelayOption82ConfigOperationStrategy.setStatus("current")


class _DhcpL2RelayOption82ConfigFormat_Type(Integer32):
    """Custom type dhcpL2RelayOption82ConfigFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("private", 1))
    )


_DhcpL2RelayOption82ConfigFormat_Type.__name__ = "Integer32"
_DhcpL2RelayOption82ConfigFormat_Object = MibTableColumn
dhcpL2RelayOption82ConfigFormat = _DhcpL2RelayOption82ConfigFormat_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 66, 1, 2, 1, 1, 4),
    _DhcpL2RelayOption82ConfigFormat_Type()
)
dhcpL2RelayOption82ConfigFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpL2RelayOption82ConfigFormat.setStatus("current")


class _DhcpL2RelayOption82ConfigCircuitCustomization_Type(Integer32):
    """Custom type dhcpL2RelayOption82ConfigCircuitCustomization based on Integer32"""
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


_DhcpL2RelayOption82ConfigCircuitCustomization_Type.__name__ = "Integer32"
_DhcpL2RelayOption82ConfigCircuitCustomization_Object = MibTableColumn
dhcpL2RelayOption82ConfigCircuitCustomization = _DhcpL2RelayOption82ConfigCircuitCustomization_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 66, 1, 2, 1, 1, 5),
    _DhcpL2RelayOption82ConfigCircuitCustomization_Type()
)
dhcpL2RelayOption82ConfigCircuitCustomization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpL2RelayOption82ConfigCircuitCustomization.setStatus("current")


class _DhcpL2RelayOption82ConfigCircuitID_Type(OctetString):
    """Custom type dhcpL2RelayOption82ConfigCircuitID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DhcpL2RelayOption82ConfigCircuitID_Type.__name__ = "OctetString"
_DhcpL2RelayOption82ConfigCircuitID_Object = MibTableColumn
dhcpL2RelayOption82ConfigCircuitID = _DhcpL2RelayOption82ConfigCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 66, 1, 2, 1, 1, 6),
    _DhcpL2RelayOption82ConfigCircuitID_Type()
)
dhcpL2RelayOption82ConfigCircuitID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpL2RelayOption82ConfigCircuitID.setStatus("current")


class _DhcpL2RelayOption82ConfigRemoteCustomization_Type(Integer32):
    """Custom type dhcpL2RelayOption82ConfigRemoteCustomization based on Integer32"""
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


_DhcpL2RelayOption82ConfigRemoteCustomization_Type.__name__ = "Integer32"
_DhcpL2RelayOption82ConfigRemoteCustomization_Object = MibTableColumn
dhcpL2RelayOption82ConfigRemoteCustomization = _DhcpL2RelayOption82ConfigRemoteCustomization_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 66, 1, 2, 1, 1, 7),
    _DhcpL2RelayOption82ConfigRemoteCustomization_Type()
)
dhcpL2RelayOption82ConfigRemoteCustomization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpL2RelayOption82ConfigRemoteCustomization.setStatus("current")


class _DhcpL2RelayOption82ConfigRemoteID_Type(OctetString):
    """Custom type dhcpL2RelayOption82ConfigRemoteID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DhcpL2RelayOption82ConfigRemoteID_Type.__name__ = "OctetString"
_DhcpL2RelayOption82ConfigRemoteID_Object = MibTableColumn
dhcpL2RelayOption82ConfigRemoteID = _DhcpL2RelayOption82ConfigRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 66, 1, 2, 1, 1, 8),
    _DhcpL2RelayOption82ConfigRemoteID_Type()
)
dhcpL2RelayOption82ConfigRemoteID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpL2RelayOption82ConfigRemoteID.setStatus("current")


class _DhcpL2RelayOption82ConfigLag_Type(OctetString):
    """Custom type dhcpL2RelayOption82ConfigLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_DhcpL2RelayOption82ConfigLag_Type.__name__ = "OctetString"
_DhcpL2RelayOption82ConfigLag_Object = MibTableColumn
dhcpL2RelayOption82ConfigLag = _DhcpL2RelayOption82ConfigLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 66, 1, 2, 1, 1, 9),
    _DhcpL2RelayOption82ConfigLag_Type()
)
dhcpL2RelayOption82ConfigLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpL2RelayOption82ConfigLag.setStatus("current")
_TplinkDhcpL2RelayNotifications_ObjectIdentity = ObjectIdentity
tplinkDhcpL2RelayNotifications = _TplinkDhcpL2RelayNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 66, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-DHCPL2Relay-MIB",
    **{"tplinkDhcpL2RelayMIB": tplinkDhcpL2RelayMIB,
       "tplinkDhcpL2RelayMIBObjects": tplinkDhcpL2RelayMIBObjects,
       "dhcpL2RelayGlobalConfig": dhcpL2RelayGlobalConfig,
       "dhcpL2RelayEnable": dhcpL2RelayEnable,
       "dhcpL2RelayVlanConfigTable": dhcpL2RelayVlanConfigTable,
       "dhcpL2RelayVlanConfigEntry": dhcpL2RelayVlanConfigEntry,
       "dhcpL2RelayVlanId": dhcpL2RelayVlanId,
       "dhcpL2RelayVlanStatus": dhcpL2RelayVlanStatus,
       "dhcpL2RelayOption82Config": dhcpL2RelayOption82Config,
       "dhcpL2RelayOption82ConfigTable": dhcpL2RelayOption82ConfigTable,
       "dhcpL2RelayOption82ConfigEntry": dhcpL2RelayOption82ConfigEntry,
       "dhcpL2RelayOption82ConfigPort": dhcpL2RelayOption82ConfigPort,
       "dhcpL2RelayOption82ConfigSupportStatus": dhcpL2RelayOption82ConfigSupportStatus,
       "dhcpL2RelayOption82ConfigOperationStrategy": dhcpL2RelayOption82ConfigOperationStrategy,
       "dhcpL2RelayOption82ConfigFormat": dhcpL2RelayOption82ConfigFormat,
       "dhcpL2RelayOption82ConfigCircuitCustomization": dhcpL2RelayOption82ConfigCircuitCustomization,
       "dhcpL2RelayOption82ConfigCircuitID": dhcpL2RelayOption82ConfigCircuitID,
       "dhcpL2RelayOption82ConfigRemoteCustomization": dhcpL2RelayOption82ConfigRemoteCustomization,
       "dhcpL2RelayOption82ConfigRemoteID": dhcpL2RelayOption82ConfigRemoteID,
       "dhcpL2RelayOption82ConfigLag": dhcpL2RelayOption82ConfigLag,
       "tplinkDhcpL2RelayNotifications": tplinkDhcpL2RelayNotifications}
)
