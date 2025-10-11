# SNMP MIB module (TPLINK-IPMACBINDING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/tplink/TPLINK-IPMACBINDING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:56:37 2025
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

tplinkIpMacBindingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 68)
)
if mibBuilder.loadTexts:
    tplinkIpMacBindingMIB.setRevisions(
        ("2012-12-17 10:14",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkIpMacBindingMIBObjects_ObjectIdentity = ObjectIdentity
tplinkIpMacBindingMIBObjects = _TplinkIpMacBindingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 68, 1)
)
_TpIpMacBindigConfigure_ObjectIdentity = ObjectIdentity
tpIpMacBindigConfigure = _TpIpMacBindigConfigure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 68, 1, 1)
)
_TpIpMacBindingTable_Object = MibTable
tpIpMacBindingTable = _TpIpMacBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 68, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tpIpMacBindingTable.setStatus("current")
_TpIpMacBindingEntry_Object = MibTableRow
tpIpMacBindingEntry = _TpIpMacBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 68, 1, 1, 1, 1)
)
tpIpMacBindingEntry.setIndexNames(
    (0, "TPLINK-IPMACBINDING-MIB", "tpBindingIp"),
)
if mibBuilder.loadTexts:
    tpIpMacBindingEntry.setStatus("current")


class _TpBindingHostName_Type(OctetString):
    """Custom type tpBindingHostName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_TpBindingHostName_Type.__name__ = "OctetString"
_TpBindingHostName_Object = MibTableColumn
tpBindingHostName = _TpBindingHostName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 68, 1, 1, 1, 1, 1),
    _TpBindingHostName_Type()
)
tpBindingHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpBindingHostName.setStatus("current")
_TpBindingIp_Type = IpAddress
_TpBindingIp_Object = MibTableColumn
tpBindingIp = _TpBindingIp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 68, 1, 1, 1, 1, 2),
    _TpBindingIp_Type()
)
tpBindingIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpBindingIp.setStatus("current")


class _TpBindingMac_Type(OctetString):
    """Custom type tpBindingMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_TpBindingMac_Type.__name__ = "OctetString"
_TpBindingMac_Object = MibTableColumn
tpBindingMac = _TpBindingMac_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 68, 1, 1, 1, 1, 3),
    _TpBindingMac_Type()
)
tpBindingMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpBindingMac.setStatus("current")
_TpBindingVlanId_Type = Integer32
_TpBindingVlanId_Object = MibTableColumn
tpBindingVlanId = _TpBindingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 68, 1, 1, 1, 1, 4),
    _TpBindingVlanId_Type()
)
tpBindingVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpBindingVlanId.setStatus("current")


class _TpBindingPort_Type(OctetString):
    """Custom type tpBindingPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_TpBindingPort_Type.__name__ = "OctetString"
_TpBindingPort_Object = MibTableColumn
tpBindingPort = _TpBindingPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 68, 1, 1, 1, 1, 5),
    _TpBindingPort_Type()
)
tpBindingPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpBindingPort.setStatus("current")


class _TpBindingProtectType_Type(Integer32):
    """Custom type tpBindingProtectType based on Integer32"""
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
          ("arp-detection", 1),
          ("ip-source-guard", 2),
          ("both", 3))
    )


_TpBindingProtectType_Type.__name__ = "Integer32"
_TpBindingProtectType_Object = MibTableColumn
tpBindingProtectType = _TpBindingProtectType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 68, 1, 1, 1, 1, 6),
    _TpBindingProtectType_Type()
)
tpBindingProtectType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpBindingProtectType.setStatus("current")


class _TpBindingSource_Type(Integer32):
    """Custom type tpBindingSource based on Integer32"""
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
          ("arp-scanning", 2),
          ("dhcp-snooping", 3))
    )


_TpBindingSource_Type.__name__ = "Integer32"
_TpBindingSource_Object = MibTableColumn
tpBindingSource = _TpBindingSource_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 68, 1, 1, 1, 1, 7),
    _TpBindingSource_Type()
)
tpBindingSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpBindingSource.setStatus("current")
_TpBindingRowStatus_Type = TPRowStatus
_TpBindingRowStatus_Object = MibTableColumn
tpBindingRowStatus = _TpBindingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 68, 1, 1, 1, 1, 8),
    _TpBindingRowStatus_Type()
)
tpBindingRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpBindingRowStatus.setStatus("current")
_TplinkIpMacBindingNotifications_ObjectIdentity = ObjectIdentity
tplinkIpMacBindingNotifications = _TplinkIpMacBindingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 68, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-IPMACBINDING-MIB",
    **{"tplinkIpMacBindingMIB": tplinkIpMacBindingMIB,
       "tplinkIpMacBindingMIBObjects": tplinkIpMacBindingMIBObjects,
       "tpIpMacBindigConfigure": tpIpMacBindigConfigure,
       "tpIpMacBindingTable": tpIpMacBindingTable,
       "tpIpMacBindingEntry": tpIpMacBindingEntry,
       "tpBindingHostName": tpBindingHostName,
       "tpBindingIp": tpBindingIp,
       "tpBindingMac": tpBindingMac,
       "tpBindingVlanId": tpBindingVlanId,
       "tpBindingPort": tpBindingPort,
       "tpBindingProtectType": tpBindingProtectType,
       "tpBindingSource": tpBindingSource,
       "tpBindingRowStatus": tpBindingRowStatus,
       "tplinkIpMacBindingNotifications": tplinkIpMacBindingNotifications}
)
