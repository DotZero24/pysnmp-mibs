# SNMP MIB module (G6-RADIUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/microsens/G6-RADIUS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:09 2025
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

(g6,) = mibBuilder.importSymbols(
    "MICROSENS-G6-MIB",
    "g6")

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
 enterprises,
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
    "enterprises",
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


# MODULE-IDENTITY

management = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3)
)
if mibBuilder.loadTexts:
    management.setRevisions(
        ("2018-02-12 16:19",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Radius_ObjectIdentity = ObjectIdentity
radius = _Radius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 69)
)
_ServerTable_Object = MibTable
serverTable = _ServerTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 69, 1)
)
if mibBuilder.loadTexts:
    serverTable.setStatus("current")
_ServerEntry_Object = MibTableRow
serverEntry = _ServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 69, 1, 1)
)
serverEntry.setIndexNames(
    (0, "G6-RADIUS-MIB", "serverIndex"),
)
if mibBuilder.loadTexts:
    serverEntry.setStatus("current")


class _ServerIndex_Type(Integer32):
    """Custom type serverIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ServerIndex_Type.__name__ = "Integer32"
_ServerIndex_Object = MibTableColumn
serverIndex = _ServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 69, 1, 1, 1),
    _ServerIndex_Type()
)
serverIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    serverIndex.setStatus("current")
_ServerName_Type = DisplayString
_ServerName_Object = MibTableColumn
serverName = _ServerName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 69, 1, 1, 2),
    _ServerName_Type()
)
serverName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serverName.setStatus("current")


class _ServerServerType_Type(Integer32):
    """Custom type serverServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("radius", 0),
          ("tacacs", 1))
    )


_ServerServerType_Type.__name__ = "Integer32"
_ServerServerType_Object = MibTableColumn
serverServerType = _ServerServerType_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 69, 1, 1, 3),
    _ServerServerType_Type()
)
serverServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serverServerType.setStatus("current")
_ServerHostAddress_Type = DisplayString
_ServerHostAddress_Object = MibTableColumn
serverHostAddress = _ServerHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 69, 1, 1, 4),
    _ServerHostAddress_Type()
)
serverHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serverHostAddress.setStatus("current")


class _ServerUdpPort_Type(Integer32):
    """Custom type serverUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ServerUdpPort_Type.__name__ = "Integer32"
_ServerUdpPort_Object = MibTableColumn
serverUdpPort = _ServerUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 69, 1, 1, 5),
    _ServerUdpPort_Type()
)
serverUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serverUdpPort.setStatus("current")
_ServerSharedSecret_Type = DisplayString
_ServerSharedSecret_Object = MibTableColumn
serverSharedSecret = _ServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 69, 1, 1, 6),
    _ServerSharedSecret_Type()
)
serverSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serverSharedSecret.setStatus("current")
_ServerInterimInterval_Type = Unsigned32
_ServerInterimInterval_Object = MibTableColumn
serverInterimInterval = _ServerInterimInterval_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 69, 1, 1, 7),
    _ServerInterimInterval_Type()
)
serverInterimInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serverInterimInterval.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "G6-RADIUS-MIB",
    **{"management": management,
       "radius": radius,
       "serverTable": serverTable,
       "serverEntry": serverEntry,
       "serverIndex": serverIndex,
       "serverName": serverName,
       "serverServerType": serverServerType,
       "serverHostAddress": serverHostAddress,
       "serverUdpPort": serverUdpPort,
       "serverSharedSecret": serverSharedSecret,
       "serverInterimInterval": serverInterimInterval}
)
