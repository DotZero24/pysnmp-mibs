# SNMP MIB module (TPLINK-IPV6MACBINDING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/tplink/TPLINK-IPV6MACBINDING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:56:27 2025
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

tplinkIpv6MacBindingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 69)
)
if mibBuilder.loadTexts:
    tplinkIpv6MacBindingMIB.setRevisions(
        ("2012-12-17 10:14",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkIpv6MacBindingMIBObjects_ObjectIdentity = ObjectIdentity
tplinkIpv6MacBindingMIBObjects = _TplinkIpv6MacBindingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 69, 1)
)
_TpIpv6MacBindigConfigure_ObjectIdentity = ObjectIdentity
tpIpv6MacBindigConfigure = _TpIpv6MacBindigConfigure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 69, 1, 1)
)
_TpIpv6MacBindingTable_Object = MibTable
tpIpv6MacBindingTable = _TpIpv6MacBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 69, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tpIpv6MacBindingTable.setStatus("current")
_TpIpv6MacBindingEntry_Object = MibTableRow
tpIpv6MacBindingEntry = _TpIpv6MacBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 69, 1, 1, 1, 1)
)
tpIpv6MacBindingEntry.setIndexNames(
    (0, "TPLINK-IPV6MACBINDING-MIB", "tpIpv6BindingIp"),
)
if mibBuilder.loadTexts:
    tpIpv6MacBindingEntry.setStatus("current")


class _TpIpv6BindingHostName_Type(OctetString):
    """Custom type tpIpv6BindingHostName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_TpIpv6BindingHostName_Type.__name__ = "OctetString"
_TpIpv6BindingHostName_Object = MibTableColumn
tpIpv6BindingHostName = _TpIpv6BindingHostName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 69, 1, 1, 1, 1, 1),
    _TpIpv6BindingHostName_Type()
)
tpIpv6BindingHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpIpv6BindingHostName.setStatus("current")
_TpIpv6BindingIp_Type = InetAddress
_TpIpv6BindingIp_Object = MibTableColumn
tpIpv6BindingIp = _TpIpv6BindingIp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 69, 1, 1, 1, 1, 2),
    _TpIpv6BindingIp_Type()
)
tpIpv6BindingIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIpv6BindingIp.setStatus("current")


class _TpIpv6BindingMac_Type(OctetString):
    """Custom type tpIpv6BindingMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_TpIpv6BindingMac_Type.__name__ = "OctetString"
_TpIpv6BindingMac_Object = MibTableColumn
tpIpv6BindingMac = _TpIpv6BindingMac_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 69, 1, 1, 1, 1, 3),
    _TpIpv6BindingMac_Type()
)
tpIpv6BindingMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIpv6BindingMac.setStatus("current")
_TpIpv6BindingVlanId_Type = Integer32
_TpIpv6BindingVlanId_Object = MibTableColumn
tpIpv6BindingVlanId = _TpIpv6BindingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 69, 1, 1, 1, 1, 4),
    _TpIpv6BindingVlanId_Type()
)
tpIpv6BindingVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIpv6BindingVlanId.setStatus("current")


class _TpIpv6BindingPort_Type(OctetString):
    """Custom type tpIpv6BindingPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_TpIpv6BindingPort_Type.__name__ = "OctetString"
_TpIpv6BindingPort_Object = MibTableColumn
tpIpv6BindingPort = _TpIpv6BindingPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 69, 1, 1, 1, 1, 5),
    _TpIpv6BindingPort_Type()
)
tpIpv6BindingPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIpv6BindingPort.setStatus("current")


class _TpIpv6BindingProtectType_Type(Integer32):
    """Custom type tpIpv6BindingProtectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("nd-detection", 1),
          ("ipv6-source-guard", 2),
          ("both", 3))
    )


_TpIpv6BindingProtectType_Type.__name__ = "Integer32"
_TpIpv6BindingProtectType_Object = MibTableColumn
tpIpv6BindingProtectType = _TpIpv6BindingProtectType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 69, 1, 1, 1, 1, 6),
    _TpIpv6BindingProtectType_Type()
)
tpIpv6BindingProtectType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpIpv6BindingProtectType.setStatus("current")


class _TpIpv6BindingSource_Type(Integer32):
    """Custom type tpIpv6BindingSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("dhcp-snooping", 2),
          ("nd-snooping", 3))
    )


_TpIpv6BindingSource_Type.__name__ = "Integer32"
_TpIpv6BindingSource_Object = MibTableColumn
tpIpv6BindingSource = _TpIpv6BindingSource_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 69, 1, 1, 1, 1, 7),
    _TpIpv6BindingSource_Type()
)
tpIpv6BindingSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIpv6BindingSource.setStatus("current")
_TpIpv6BindingRowStatus_Type = TPRowStatus
_TpIpv6BindingRowStatus_Object = MibTableColumn
tpIpv6BindingRowStatus = _TpIpv6BindingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 69, 1, 1, 1, 1, 8),
    _TpIpv6BindingRowStatus_Type()
)
tpIpv6BindingRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpIpv6BindingRowStatus.setStatus("current")
_TplinkIpv6MacBindingNotifications_ObjectIdentity = ObjectIdentity
tplinkIpv6MacBindingNotifications = _TplinkIpv6MacBindingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 69, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-IPV6MACBINDING-MIB",
    **{"tplinkIpv6MacBindingMIB": tplinkIpv6MacBindingMIB,
       "tplinkIpv6MacBindingMIBObjects": tplinkIpv6MacBindingMIBObjects,
       "tpIpv6MacBindigConfigure": tpIpv6MacBindigConfigure,
       "tpIpv6MacBindingTable": tpIpv6MacBindingTable,
       "tpIpv6MacBindingEntry": tpIpv6MacBindingEntry,
       "tpIpv6BindingHostName": tpIpv6BindingHostName,
       "tpIpv6BindingIp": tpIpv6BindingIp,
       "tpIpv6BindingMac": tpIpv6BindingMac,
       "tpIpv6BindingVlanId": tpIpv6BindingVlanId,
       "tpIpv6BindingPort": tpIpv6BindingPort,
       "tpIpv6BindingProtectType": tpIpv6BindingProtectType,
       "tpIpv6BindingSource": tpIpv6BindingSource,
       "tpIpv6BindingRowStatus": tpIpv6BindingRowStatus,
       "tplinkIpv6MacBindingNotifications": tplinkIpv6MacBindingNotifications}
)
