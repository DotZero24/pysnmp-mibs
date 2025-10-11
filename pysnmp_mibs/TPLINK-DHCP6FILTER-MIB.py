# SNMP MIB module (TPLINK-DHCP6FILTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/tplink/TPLINK-DHCP6FILTER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:55:25 2025
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

(InetAddress,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress")

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

tplinkDhcp6FilterMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 67)
)
if mibBuilder.loadTexts:
    tplinkDhcp6FilterMIB.setRevisions(
        ("2012-12-17 10:14",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkDhcp6FilterMIBObjects_ObjectIdentity = ObjectIdentity
tplinkDhcp6FilterMIBObjects = _TplinkDhcp6FilterMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 67, 1)
)
_Dhcp6FilterGlobalConfig_ObjectIdentity = ObjectIdentity
dhcp6FilterGlobalConfig = _Dhcp6FilterGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 67, 1, 1)
)


class _Dhcp6FilterEnable_Type(Integer32):
    """Custom type dhcp6FilterEnable based on Integer32"""
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


_Dhcp6FilterEnable_Type.__name__ = "Integer32"
_Dhcp6FilterEnable_Object = MibScalar
dhcp6FilterEnable = _Dhcp6FilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 67, 1, 1, 1),
    _Dhcp6FilterEnable_Type()
)
dhcp6FilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcp6FilterEnable.setStatus("current")
_Dhcp6FilterPortConfig_ObjectIdentity = ObjectIdentity
dhcp6FilterPortConfig = _Dhcp6FilterPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 67, 1, 2)
)
_Dhcp6FilterPortConfigTable_Object = MibTable
dhcp6FilterPortConfigTable = _Dhcp6FilterPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 67, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dhcp6FilterPortConfigTable.setStatus("current")
_Dhcp6FilterPortConfigEntry_Object = MibTableRow
dhcp6FilterPortConfigEntry = _Dhcp6FilterPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 67, 1, 2, 1, 1)
)
dhcp6FilterPortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dhcp6FilterPortConfigEntry.setStatus("current")


class _Dhcp6FilterPort_Type(OctetString):
    """Custom type dhcp6FilterPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Dhcp6FilterPort_Type.__name__ = "OctetString"
_Dhcp6FilterPort_Object = MibTableColumn
dhcp6FilterPort = _Dhcp6FilterPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 67, 1, 2, 1, 1, 1),
    _Dhcp6FilterPort_Type()
)
dhcp6FilterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcp6FilterPort.setStatus("current")


class _Dhcp6FilterPortConfigState_Type(Integer32):
    """Custom type dhcp6FilterPortConfigState based on Integer32"""
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


_Dhcp6FilterPortConfigState_Type.__name__ = "Integer32"
_Dhcp6FilterPortConfigState_Object = MibTableColumn
dhcp6FilterPortConfigState = _Dhcp6FilterPortConfigState_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 67, 1, 2, 1, 1, 2),
    _Dhcp6FilterPortConfigState_Type()
)
dhcp6FilterPortConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcp6FilterPortConfigState.setStatus("current")


class _Dhcp6FilterPortConfigRateLimit_Type(Integer32):
    """Custom type dhcp6FilterPortConfigRateLimit based on Integer32"""
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


_Dhcp6FilterPortConfigRateLimit_Type.__name__ = "Integer32"
_Dhcp6FilterPortConfigRateLimit_Object = MibTableColumn
dhcp6FilterPortConfigRateLimit = _Dhcp6FilterPortConfigRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 67, 1, 2, 1, 1, 3),
    _Dhcp6FilterPortConfigRateLimit_Type()
)
dhcp6FilterPortConfigRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcp6FilterPortConfigRateLimit.setStatus("current")


class _Dhcp6FilterPortConfigDeclineRateLimit_Type(Integer32):
    """Custom type dhcp6FilterPortConfigDeclineRateLimit based on Integer32"""
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


_Dhcp6FilterPortConfigDeclineRateLimit_Type.__name__ = "Integer32"
_Dhcp6FilterPortConfigDeclineRateLimit_Object = MibTableColumn
dhcp6FilterPortConfigDeclineRateLimit = _Dhcp6FilterPortConfigDeclineRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 67, 1, 2, 1, 1, 4),
    _Dhcp6FilterPortConfigDeclineRateLimit_Type()
)
dhcp6FilterPortConfigDeclineRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcp6FilterPortConfigDeclineRateLimit.setStatus("current")


class _Dhcp6FilterPortConfigPortLag_Type(OctetString):
    """Custom type dhcp6FilterPortConfigPortLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Dhcp6FilterPortConfigPortLag_Type.__name__ = "OctetString"
_Dhcp6FilterPortConfigPortLag_Object = MibTableColumn
dhcp6FilterPortConfigPortLag = _Dhcp6FilterPortConfigPortLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 67, 1, 2, 1, 1, 5),
    _Dhcp6FilterPortConfigPortLag_Type()
)
dhcp6FilterPortConfigPortLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcp6FilterPortConfigPortLag.setStatus("current")
_Dhcp6FilterServerPermitEntryCofig_ObjectIdentity = ObjectIdentity
dhcp6FilterServerPermitEntryCofig = _Dhcp6FilterServerPermitEntryCofig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 67, 1, 3)
)
_Dhcp6FilterServerPermitEntryTable_Object = MibTable
dhcp6FilterServerPermitEntryTable = _Dhcp6FilterServerPermitEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 67, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dhcp6FilterServerPermitEntryTable.setStatus("current")
_Dhcp6FilterServerPermitEntry_Object = MibTableRow
dhcp6FilterServerPermitEntry = _Dhcp6FilterServerPermitEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 67, 1, 3, 1, 1)
)
dhcp6FilterServerPermitEntry.setIndexNames(
    (0, "TPLINK-DHCP6FILTER-MIB", "dhcp6FilterServerIp"),
    (0, "TPLINK-DHCP6FILTER-MIB", "dhcp6FilterInterface"),
)
if mibBuilder.loadTexts:
    dhcp6FilterServerPermitEntry.setStatus("current")
_Dhcp6FilterServerIp_Type = InetAddress
_Dhcp6FilterServerIp_Object = MibTableColumn
dhcp6FilterServerIp = _Dhcp6FilterServerIp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 67, 1, 3, 1, 1, 1),
    _Dhcp6FilterServerIp_Type()
)
dhcp6FilterServerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcp6FilterServerIp.setStatus("current")


class _Dhcp6FilterInterface_Type(OctetString):
    """Custom type dhcp6FilterInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Dhcp6FilterInterface_Type.__name__ = "OctetString"
_Dhcp6FilterInterface_Object = MibTableColumn
dhcp6FilterInterface = _Dhcp6FilterInterface_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 67, 1, 3, 1, 1, 2),
    _Dhcp6FilterInterface_Type()
)
dhcp6FilterInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcp6FilterInterface.setStatus("current")
_Dhcp6FilterRowStatus_Type = TPRowStatus
_Dhcp6FilterRowStatus_Object = MibTableColumn
dhcp6FilterRowStatus = _Dhcp6FilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 67, 1, 3, 1, 1, 3),
    _Dhcp6FilterRowStatus_Type()
)
dhcp6FilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcp6FilterRowStatus.setStatus("current")
_TplinkDhcp6FilterNotifications_ObjectIdentity = ObjectIdentity
tplinkDhcp6FilterNotifications = _TplinkDhcp6FilterNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 67, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-DHCP6FILTER-MIB",
    **{"tplinkDhcp6FilterMIB": tplinkDhcp6FilterMIB,
       "tplinkDhcp6FilterMIBObjects": tplinkDhcp6FilterMIBObjects,
       "dhcp6FilterGlobalConfig": dhcp6FilterGlobalConfig,
       "dhcp6FilterEnable": dhcp6FilterEnable,
       "dhcp6FilterPortConfig": dhcp6FilterPortConfig,
       "dhcp6FilterPortConfigTable": dhcp6FilterPortConfigTable,
       "dhcp6FilterPortConfigEntry": dhcp6FilterPortConfigEntry,
       "dhcp6FilterPort": dhcp6FilterPort,
       "dhcp6FilterPortConfigState": dhcp6FilterPortConfigState,
       "dhcp6FilterPortConfigRateLimit": dhcp6FilterPortConfigRateLimit,
       "dhcp6FilterPortConfigDeclineRateLimit": dhcp6FilterPortConfigDeclineRateLimit,
       "dhcp6FilterPortConfigPortLag": dhcp6FilterPortConfigPortLag,
       "dhcp6FilterServerPermitEntryCofig": dhcp6FilterServerPermitEntryCofig,
       "dhcp6FilterServerPermitEntryTable": dhcp6FilterServerPermitEntryTable,
       "dhcp6FilterServerPermitEntry": dhcp6FilterServerPermitEntry,
       "dhcp6FilterServerIp": dhcp6FilterServerIp,
       "dhcp6FilterInterface": dhcp6FilterInterface,
       "dhcp6FilterRowStatus": dhcp6FilterRowStatus,
       "tplinkDhcp6FilterNotifications": tplinkDhcp6FilterNotifications}
)
