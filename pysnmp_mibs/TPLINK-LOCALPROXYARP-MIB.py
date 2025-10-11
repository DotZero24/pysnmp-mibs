# SNMP MIB module (TPLINK-LOCALPROXYARP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/tplink/TPLINK-LOCALPROXYARP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:56:05 2025
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


# MODULE-IDENTITY

tplinkLocalProxyArpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 46)
)
if mibBuilder.loadTexts:
    tplinkLocalProxyArpMIB.setRevisions(
        ("2012-12-13 09:30",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkLocalProxyArpMIBObjects_ObjectIdentity = ObjectIdentity
tplinkLocalProxyArpMIBObjects = _TplinkLocalProxyArpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 46, 1)
)
_TpLocalProxyArpConfig_ObjectIdentity = ObjectIdentity
tpLocalProxyArpConfig = _TpLocalProxyArpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 46, 1)
)
_TpLocalProxyArpTable_Object = MibTable
tpLocalProxyArpTable = _TpLocalProxyArpTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 46, 1, 1)
)
if mibBuilder.loadTexts:
    tpLocalProxyArpTable.setStatus("current")
_TpLocalProxyArpEntry_Object = MibTableRow
tpLocalProxyArpEntry = _TpLocalProxyArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 46, 1, 1, 1)
)
tpLocalProxyArpEntry.setIndexNames(
    (0, "TPLINK-LOCALPROXYARP-MIB", "tpLocalProxyArpInterface"),
)
if mibBuilder.loadTexts:
    tpLocalProxyArpEntry.setStatus("current")


class _TpLocalProxyArpInterface_Type(OctetString):
    """Custom type tpLocalProxyArpInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TpLocalProxyArpInterface_Type.__name__ = "OctetString"
_TpLocalProxyArpInterface_Object = MibTableColumn
tpLocalProxyArpInterface = _TpLocalProxyArpInterface_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 46, 1, 1, 1, 1),
    _TpLocalProxyArpInterface_Type()
)
tpLocalProxyArpInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpLocalProxyArpInterface.setStatus("current")
_TpLocalProxyArpIpAddr_Type = IpAddress
_TpLocalProxyArpIpAddr_Object = MibTableColumn
tpLocalProxyArpIpAddr = _TpLocalProxyArpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 46, 1, 1, 1, 2),
    _TpLocalProxyArpIpAddr_Type()
)
tpLocalProxyArpIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpLocalProxyArpIpAddr.setStatus("current")
_TpLocalProxyArpIpMask_Type = IpAddress
_TpLocalProxyArpIpMask_Object = MibTableColumn
tpLocalProxyArpIpMask = _TpLocalProxyArpIpMask_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 46, 1, 1, 1, 3),
    _TpLocalProxyArpIpMask_Type()
)
tpLocalProxyArpIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpLocalProxyArpIpMask.setStatus("current")


class _TpLocalProxyArpEnable_Type(Integer32):
    """Custom type tpLocalProxyArpEnable based on Integer32"""
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


_TpLocalProxyArpEnable_Type.__name__ = "Integer32"
_TpLocalProxyArpEnable_Object = MibTableColumn
tpLocalProxyArpEnable = _TpLocalProxyArpEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 46, 1, 1, 1, 4),
    _TpLocalProxyArpEnable_Type()
)
tpLocalProxyArpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpLocalProxyArpEnable.setStatus("current")
_TplinkLocalProxyArpNotifications_ObjectIdentity = ObjectIdentity
tplinkLocalProxyArpNotifications = _TplinkLocalProxyArpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 46, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-LOCALPROXYARP-MIB",
    **{"tplinkLocalProxyArpMIB": tplinkLocalProxyArpMIB,
       "tplinkLocalProxyArpMIBObjects": tplinkLocalProxyArpMIBObjects,
       "tpLocalProxyArpConfig": tpLocalProxyArpConfig,
       "tpLocalProxyArpTable": tpLocalProxyArpTable,
       "tpLocalProxyArpEntry": tpLocalProxyArpEntry,
       "tpLocalProxyArpInterface": tpLocalProxyArpInterface,
       "tpLocalProxyArpIpAddr": tpLocalProxyArpIpAddr,
       "tpLocalProxyArpIpMask": tpLocalProxyArpIpMask,
       "tpLocalProxyArpEnable": tpLocalProxyArpEnable,
       "tplinkLocalProxyArpNotifications": tplinkLocalProxyArpNotifications}
)
