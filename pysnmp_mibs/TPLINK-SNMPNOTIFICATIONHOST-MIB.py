# SNMP MIB module (TPLINK-SNMPNOTIFICATIONHOST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/tplink/TPLINK-SNMPNOTIFICATIONHOST-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:55:17 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(tplinkSnmpMIBObjects,) = mibBuilder.importSymbols(
    "TPLINK-SNMP-MIB",
    "tplinkSnmpMIBObjects")

(TPRowStatus,) = mibBuilder.importSymbols(
    "TPLINK-TC-MIB",
    "TPRowStatus")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TpSnmpNotificationHost_ObjectIdentity = ObjectIdentity
tpSnmpNotificationHost = _TpSnmpNotificationHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1)
)
_TpSnmpNotificationHostTable_Object = MibTable
tpSnmpNotificationHostTable = _TpSnmpNotificationHostTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tpSnmpNotificationHostTable.setStatus("current")
_TpSnmpNotificationHostEntry_Object = MibTableRow
tpSnmpNotificationHostEntry = _TpSnmpNotificationHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 1, 1)
)
tpSnmpNotificationHostEntry.setIndexNames(
    (0, "TPLINK-SNMPNOTIFICATIONHOST-MIB", "tpSnmpNotificationHostIndex"),
)
if mibBuilder.loadTexts:
    tpSnmpNotificationHostEntry.setStatus("current")


class _TpSnmpNotificationHostIndex_Type(Integer32):
    """Custom type tpSnmpNotificationHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_TpSnmpNotificationHostIndex_Type.__name__ = "Integer32"
_TpSnmpNotificationHostIndex_Object = MibTableColumn
tpSnmpNotificationHostIndex = _TpSnmpNotificationHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 1, 1, 1),
    _TpSnmpNotificationHostIndex_Type()
)
tpSnmpNotificationHostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpSnmpNotificationHostIndex.setStatus("current")
_TpSnmpNotificationHostIpMode_Type = InetAddressType
_TpSnmpNotificationHostIpMode_Object = MibTableColumn
tpSnmpNotificationHostIpMode = _TpSnmpNotificationHostIpMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 1, 1, 2),
    _TpSnmpNotificationHostIpMode_Type()
)
tpSnmpNotificationHostIpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSnmpNotificationHostIpMode.setStatus("current")
_TpSnmpNotificationHostIpAddr_Type = InetAddress
_TpSnmpNotificationHostIpAddr_Object = MibTableColumn
tpSnmpNotificationHostIpAddr = _TpSnmpNotificationHostIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 1, 1, 3),
    _TpSnmpNotificationHostIpAddr_Type()
)
tpSnmpNotificationHostIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpSnmpNotificationHostIpAddr.setStatus("current")


class _TpSnmpNotificationHostUserName_Type(OctetString):
    """Custom type tpSnmpNotificationHostUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TpSnmpNotificationHostUserName_Type.__name__ = "OctetString"
_TpSnmpNotificationHostUserName_Object = MibTableColumn
tpSnmpNotificationHostUserName = _TpSnmpNotificationHostUserName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 1, 1, 4),
    _TpSnmpNotificationHostUserName_Type()
)
tpSnmpNotificationHostUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpSnmpNotificationHostUserName.setStatus("current")


class _TpSnmpNotificationHostUDPPort_Type(Integer32):
    """Custom type tpSnmpNotificationHostUDPPort based on Integer32"""
    defaultValue = 162


_TpSnmpNotificationHostUDPPort_Type.__name__ = "Integer32"
_TpSnmpNotificationHostUDPPort_Object = MibTableColumn
tpSnmpNotificationHostUDPPort = _TpSnmpNotificationHostUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 1, 1, 5),
    _TpSnmpNotificationHostUDPPort_Type()
)
tpSnmpNotificationHostUDPPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpSnmpNotificationHostUDPPort.setStatus("current")


class _TpSnmpNotificationHostSecMode_Type(Integer32):
    """Custom type tpSnmpNotificationHostSecMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2c", 2),
          ("v3", 3))
    )


_TpSnmpNotificationHostSecMode_Type.__name__ = "Integer32"
_TpSnmpNotificationHostSecMode_Object = MibTableColumn
tpSnmpNotificationHostSecMode = _TpSnmpNotificationHostSecMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 1, 1, 6),
    _TpSnmpNotificationHostSecMode_Type()
)
tpSnmpNotificationHostSecMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpSnmpNotificationHostSecMode.setStatus("current")


class _TpSnmpNotificationHostSecLev_Type(Integer32):
    """Custom type tpSnmpNotificationHostSecLev based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAuthNoPriv", 1),
          ("authNoPriv", 2),
          ("authPriv", 3))
    )


_TpSnmpNotificationHostSecLev_Type.__name__ = "Integer32"
_TpSnmpNotificationHostSecLev_Object = MibTableColumn
tpSnmpNotificationHostSecLev = _TpSnmpNotificationHostSecLev_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 1, 1, 7),
    _TpSnmpNotificationHostSecLev_Type()
)
tpSnmpNotificationHostSecLev.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpSnmpNotificationHostSecLev.setStatus("current")


class _TpSnmpNotificationHostNtfyType_Type(Integer32):
    """Custom type tpSnmpNotificationHostNtfyType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trap", 1),
          ("inform", 2))
    )


_TpSnmpNotificationHostNtfyType_Type.__name__ = "Integer32"
_TpSnmpNotificationHostNtfyType_Object = MibTableColumn
tpSnmpNotificationHostNtfyType = _TpSnmpNotificationHostNtfyType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 1, 1, 8),
    _TpSnmpNotificationHostNtfyType_Type()
)
tpSnmpNotificationHostNtfyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpSnmpNotificationHostNtfyType.setStatus("current")
_TpSnmpNotificationHostRetry_Type = Integer32
_TpSnmpNotificationHostRetry_Object = MibTableColumn
tpSnmpNotificationHostRetry = _TpSnmpNotificationHostRetry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 1, 1, 9),
    _TpSnmpNotificationHostRetry_Type()
)
tpSnmpNotificationHostRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpSnmpNotificationHostRetry.setStatus("current")
_TpSnmpNotificationHostTimeout_Type = Integer32
_TpSnmpNotificationHostTimeout_Object = MibTableColumn
tpSnmpNotificationHostTimeout = _TpSnmpNotificationHostTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 1, 1, 10),
    _TpSnmpNotificationHostTimeout_Type()
)
tpSnmpNotificationHostTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpSnmpNotificationHostTimeout.setStatus("current")


class _TpSnmpNotificationHostRowStatus_Type(TPRowStatus):
    """Custom type tpSnmpNotificationHostRowStatus based on TPRowStatus"""
    defaultValue = 4


_TpSnmpNotificationHostRowStatus_Type.__name__ = "TPRowStatus"
_TpSnmpNotificationHostRowStatus_Object = MibTableColumn
tpSnmpNotificationHostRowStatus = _TpSnmpNotificationHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 1, 1, 11),
    _TpSnmpNotificationHostRowStatus_Type()
)
tpSnmpNotificationHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpSnmpNotificationHostRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-SNMPNOTIFICATIONHOST-MIB",
    **{"tpSnmpNotificationHost": tpSnmpNotificationHost,
       "tpSnmpNotificationHostTable": tpSnmpNotificationHostTable,
       "tpSnmpNotificationHostEntry": tpSnmpNotificationHostEntry,
       "tpSnmpNotificationHostIndex": tpSnmpNotificationHostIndex,
       "tpSnmpNotificationHostIpMode": tpSnmpNotificationHostIpMode,
       "tpSnmpNotificationHostIpAddr": tpSnmpNotificationHostIpAddr,
       "tpSnmpNotificationHostUserName": tpSnmpNotificationHostUserName,
       "tpSnmpNotificationHostUDPPort": tpSnmpNotificationHostUDPPort,
       "tpSnmpNotificationHostSecMode": tpSnmpNotificationHostSecMode,
       "tpSnmpNotificationHostSecLev": tpSnmpNotificationHostSecLev,
       "tpSnmpNotificationHostNtfyType": tpSnmpNotificationHostNtfyType,
       "tpSnmpNotificationHostRetry": tpSnmpNotificationHostRetry,
       "tpSnmpNotificationHostTimeout": tpSnmpNotificationHostTimeout,
       "tpSnmpNotificationHostRowStatus": tpSnmpNotificationHostRowStatus}
)
