# SNMP MIB module (TPLINK-DHCPFILTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/tplink/TPLINK-DHCPFILTER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:55:47 2025
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

(TPRowStatus,) = mibBuilder.importSymbols(
    "TPLINK-TC-MIB",
    "TPRowStatus")


# MODULE-IDENTITY

tplinkDhcpFilterMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 48)
)
if mibBuilder.loadTexts:
    tplinkDhcpFilterMIB.setRevisions(
        ("2012-12-17 10:14",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkDhcpFilterMIBObjects_ObjectIdentity = ObjectIdentity
tplinkDhcpFilterMIBObjects = _TplinkDhcpFilterMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 48, 1)
)
_DhcpFilterGlobalConfig_ObjectIdentity = ObjectIdentity
dhcpFilterGlobalConfig = _DhcpFilterGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 48, 1, 1)
)


class _DhcpFilterEnable_Type(Integer32):
    """Custom type dhcpFilterEnable based on Integer32"""
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


_DhcpFilterEnable_Type.__name__ = "Integer32"
_DhcpFilterEnable_Object = MibScalar
dhcpFilterEnable = _DhcpFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 48, 1, 1, 1),
    _DhcpFilterEnable_Type()
)
dhcpFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpFilterEnable.setStatus("current")
_DhcpFilterPortConfig_ObjectIdentity = ObjectIdentity
dhcpFilterPortConfig = _DhcpFilterPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 48, 1, 2)
)
_DhcpFilterPortConfigTable_Object = MibTable
dhcpFilterPortConfigTable = _DhcpFilterPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 48, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dhcpFilterPortConfigTable.setStatus("current")
_DhcpFilterPortConfigEntry_Object = MibTableRow
dhcpFilterPortConfigEntry = _DhcpFilterPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 48, 1, 2, 1, 1)
)
dhcpFilterPortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dhcpFilterPortConfigEntry.setStatus("current")


class _DhcpFilterPort_Type(OctetString):
    """Custom type dhcpFilterPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DhcpFilterPort_Type.__name__ = "OctetString"
_DhcpFilterPort_Object = MibTableColumn
dhcpFilterPort = _DhcpFilterPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 48, 1, 2, 1, 1, 1),
    _DhcpFilterPort_Type()
)
dhcpFilterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpFilterPort.setStatus("current")


class _DhcpFilterPortConfigState_Type(Integer32):
    """Custom type dhcpFilterPortConfigState based on Integer32"""
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


_DhcpFilterPortConfigState_Type.__name__ = "Integer32"
_DhcpFilterPortConfigState_Object = MibTableColumn
dhcpFilterPortConfigState = _DhcpFilterPortConfigState_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 48, 1, 2, 1, 1, 2),
    _DhcpFilterPortConfigState_Type()
)
dhcpFilterPortConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpFilterPortConfigState.setStatus("current")


class _DhcpFilterPortConfigMacVerify_Type(Integer32):
    """Custom type dhcpFilterPortConfigMacVerify based on Integer32"""
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


_DhcpFilterPortConfigMacVerify_Type.__name__ = "Integer32"
_DhcpFilterPortConfigMacVerify_Object = MibTableColumn
dhcpFilterPortConfigMacVerify = _DhcpFilterPortConfigMacVerify_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 48, 1, 2, 1, 1, 3),
    _DhcpFilterPortConfigMacVerify_Type()
)
dhcpFilterPortConfigMacVerify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpFilterPortConfigMacVerify.setStatus("current")


class _DhcpFilterPortConfigRateLimit_Type(Integer32):
    """Custom type dhcpFilterPortConfigRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              5,
              10,
              15,
              20,
              25,
              30)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("value5pps", 5),
          ("value10pps", 10),
          ("value15pps", 15),
          ("value20pps", 20),
          ("value25pps", 25),
          ("value30pps", 30))
    )


_DhcpFilterPortConfigRateLimit_Type.__name__ = "Integer32"
_DhcpFilterPortConfigRateLimit_Object = MibTableColumn
dhcpFilterPortConfigRateLimit = _DhcpFilterPortConfigRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 48, 1, 2, 1, 1, 4),
    _DhcpFilterPortConfigRateLimit_Type()
)
dhcpFilterPortConfigRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpFilterPortConfigRateLimit.setStatus("current")


class _DhcpFilterPortConfigDeclineRateLimit_Type(Integer32):
    """Custom type dhcpFilterPortConfigDeclineRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              5,
              10,
              15,
              20,
              25,
              30)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("value5pps", 5),
          ("value10pps", 10),
          ("value15pps", 15),
          ("value20pps", 20),
          ("value25pps", 25),
          ("value30pps", 30))
    )


_DhcpFilterPortConfigDeclineRateLimit_Type.__name__ = "Integer32"
_DhcpFilterPortConfigDeclineRateLimit_Object = MibTableColumn
dhcpFilterPortConfigDeclineRateLimit = _DhcpFilterPortConfigDeclineRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 48, 1, 2, 1, 1, 5),
    _DhcpFilterPortConfigDeclineRateLimit_Type()
)
dhcpFilterPortConfigDeclineRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpFilterPortConfigDeclineRateLimit.setStatus("current")


class _DhcpFilterPortConfigPortLag_Type(OctetString):
    """Custom type dhcpFilterPortConfigPortLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_DhcpFilterPortConfigPortLag_Type.__name__ = "OctetString"
_DhcpFilterPortConfigPortLag_Object = MibTableColumn
dhcpFilterPortConfigPortLag = _DhcpFilterPortConfigPortLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 48, 1, 2, 1, 1, 6),
    _DhcpFilterPortConfigPortLag_Type()
)
dhcpFilterPortConfigPortLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpFilterPortConfigPortLag.setStatus("current")
_DhcpFilterServerPermitEntryCofig_ObjectIdentity = ObjectIdentity
dhcpFilterServerPermitEntryCofig = _DhcpFilterServerPermitEntryCofig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 48, 1, 3)
)
_DhcpFilterServerPermitEntryTable_Object = MibTable
dhcpFilterServerPermitEntryTable = _DhcpFilterServerPermitEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 48, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dhcpFilterServerPermitEntryTable.setStatus("current")
_DhcpFilterServerPermitEntry_Object = MibTableRow
dhcpFilterServerPermitEntry = _DhcpFilterServerPermitEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 48, 1, 3, 1, 1)
)
dhcpFilterServerPermitEntry.setIndexNames(
    (0, "TPLINK-DHCPFILTER-MIB", "serverIp"),
    (0, "TPLINK-DHCPFILTER-MIB", "clientMac"),
    (0, "TPLINK-DHCPFILTER-MIB", "interface"),
)
if mibBuilder.loadTexts:
    dhcpFilterServerPermitEntry.setStatus("current")
_ServerIp_Type = IpAddress
_ServerIp_Object = MibTableColumn
serverIp = _ServerIp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 48, 1, 3, 1, 1, 1),
    _ServerIp_Type()
)
serverIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serverIp.setStatus("current")


class _ClientMac_Type(OctetString):
    """Custom type clientMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_ClientMac_Type.__name__ = "OctetString"
_ClientMac_Object = MibTableColumn
clientMac = _ClientMac_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 48, 1, 3, 1, 1, 2),
    _ClientMac_Type()
)
clientMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clientMac.setStatus("current")


class _Interface_Type(OctetString):
    """Custom type interface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Interface_Type.__name__ = "OctetString"
_Interface_Object = MibTableColumn
interface = _Interface_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 48, 1, 3, 1, 1, 3),
    _Interface_Type()
)
interface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    interface.setStatus("current")
_RowStatus_Type = TPRowStatus
_RowStatus_Object = MibTableColumn
rowStatus = _RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 48, 1, 3, 1, 1, 4),
    _RowStatus_Type()
)
rowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rowStatus.setStatus("current")
_TplinkDhcpFilterNotifications_ObjectIdentity = ObjectIdentity
tplinkDhcpFilterNotifications = _TplinkDhcpFilterNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 48, 2)
)

# Managed Objects groups


# Notification objects

dhcpFilterRxIllegalServerPacket = NotificationType(
    (1, 3, 6, 1, 4, 1, 11863, 6, 48, 2, 1)
)
if mibBuilder.loadTexts:
    dhcpFilterRxIllegalServerPacket.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-DHCPFILTER-MIB",
    **{"tplinkDhcpFilterMIB": tplinkDhcpFilterMIB,
       "tplinkDhcpFilterMIBObjects": tplinkDhcpFilterMIBObjects,
       "dhcpFilterGlobalConfig": dhcpFilterGlobalConfig,
       "dhcpFilterEnable": dhcpFilterEnable,
       "dhcpFilterPortConfig": dhcpFilterPortConfig,
       "dhcpFilterPortConfigTable": dhcpFilterPortConfigTable,
       "dhcpFilterPortConfigEntry": dhcpFilterPortConfigEntry,
       "dhcpFilterPort": dhcpFilterPort,
       "dhcpFilterPortConfigState": dhcpFilterPortConfigState,
       "dhcpFilterPortConfigMacVerify": dhcpFilterPortConfigMacVerify,
       "dhcpFilterPortConfigRateLimit": dhcpFilterPortConfigRateLimit,
       "dhcpFilterPortConfigDeclineRateLimit": dhcpFilterPortConfigDeclineRateLimit,
       "dhcpFilterPortConfigPortLag": dhcpFilterPortConfigPortLag,
       "dhcpFilterServerPermitEntryCofig": dhcpFilterServerPermitEntryCofig,
       "dhcpFilterServerPermitEntryTable": dhcpFilterServerPermitEntryTable,
       "dhcpFilterServerPermitEntry": dhcpFilterServerPermitEntry,
       "serverIp": serverIp,
       "clientMac": clientMac,
       "interface": interface,
       "rowStatus": rowStatus,
       "tplinkDhcpFilterNotifications": tplinkDhcpFilterNotifications,
       "dhcpFilterRxIllegalServerPacket": dhcpFilterRxIllegalServerPacket}
)
