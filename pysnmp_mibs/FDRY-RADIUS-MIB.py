# SNMP MIB module (FDRY-RADIUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/brocade/FDRY-RADIUS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:02:24 2025
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

(fdryRadius,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-ROOT-MIB",
    "fdryRadius")

(InetAddressType,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fdryRadiusMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    fdryRadiusMIB.setRevisions(
        ("2008-02-25 00:00",
         "2017-08-07 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ServerUsage(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("authenticationOnly", 2),
          ("authorizationOnly", 3),
          ("accountingOnly", 4))
    )



class InetAddress(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x "
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_FdryRadiusServer_ObjectIdentity = ObjectIdentity
fdryRadiusServer = _FdryRadiusServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 8, 1, 1)
)
_FdryRadiusServerTable_Object = MibTable
fdryRadiusServerTable = _FdryRadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 8, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fdryRadiusServerTable.setStatus("current")
_FdryRadiusServerEntry_Object = MibTableRow
fdryRadiusServerEntry = _FdryRadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 8, 1, 1, 1, 1)
)
fdryRadiusServerEntry.setIndexNames(
    (0, "FDRY-RADIUS-MIB", "fdryRadiusServerIndex"),
)
if mibBuilder.loadTexts:
    fdryRadiusServerEntry.setStatus("current")
_FdryRadiusServerIndex_Type = Unsigned32
_FdryRadiusServerIndex_Object = MibTableColumn
fdryRadiusServerIndex = _FdryRadiusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 8, 1, 1, 1, 1, 1),
    _FdryRadiusServerIndex_Type()
)
fdryRadiusServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryRadiusServerIndex.setStatus("current")


class _FdryRadiusServerAddrType_Type(InetAddressType):
    """Custom type fdryRadiusServerAddrType based on InetAddressType"""
    defaultValue = 1


_FdryRadiusServerAddrType_Type.__name__ = "InetAddressType"
_FdryRadiusServerAddrType_Object = MibTableColumn
fdryRadiusServerAddrType = _FdryRadiusServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 8, 1, 1, 1, 1, 2),
    _FdryRadiusServerAddrType_Type()
)
fdryRadiusServerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryRadiusServerAddrType.setStatus("current")
_FdryRadiusServerAddr_Type = InetAddress
_FdryRadiusServerAddr_Object = MibTableColumn
fdryRadiusServerAddr = _FdryRadiusServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 8, 1, 1, 1, 1, 3),
    _FdryRadiusServerAddr_Type()
)
fdryRadiusServerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryRadiusServerAddr.setStatus("current")


class _FdryRadiusServerAuthPort_Type(Unsigned32):
    """Custom type fdryRadiusServerAuthPort based on Unsigned32"""
    defaultValue = 1645


_FdryRadiusServerAuthPort_Type.__name__ = "Unsigned32"
_FdryRadiusServerAuthPort_Object = MibTableColumn
fdryRadiusServerAuthPort = _FdryRadiusServerAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 8, 1, 1, 1, 1, 4),
    _FdryRadiusServerAuthPort_Type()
)
fdryRadiusServerAuthPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryRadiusServerAuthPort.setStatus("current")


class _FdryRadiusServerAcctPort_Type(Unsigned32):
    """Custom type fdryRadiusServerAcctPort based on Unsigned32"""
    defaultValue = 1646


_FdryRadiusServerAcctPort_Type.__name__ = "Unsigned32"
_FdryRadiusServerAcctPort_Object = MibTableColumn
fdryRadiusServerAcctPort = _FdryRadiusServerAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 8, 1, 1, 1, 1, 5),
    _FdryRadiusServerAcctPort_Type()
)
fdryRadiusServerAcctPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryRadiusServerAcctPort.setStatus("current")


class _FdryRadiusServerRowKey_Type(DisplayString):
    """Custom type fdryRadiusServerRowKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FdryRadiusServerRowKey_Type.__name__ = "DisplayString"
_FdryRadiusServerRowKey_Object = MibTableColumn
fdryRadiusServerRowKey = _FdryRadiusServerRowKey_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 8, 1, 1, 1, 1, 6),
    _FdryRadiusServerRowKey_Type()
)
fdryRadiusServerRowKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryRadiusServerRowKey.setStatus("current")


class _FdryRadiusServerUsage_Type(ServerUsage):
    """Custom type fdryRadiusServerUsage based on ServerUsage"""
    defaultValue = 1


_FdryRadiusServerUsage_Type.__name__ = "ServerUsage"
_FdryRadiusServerUsage_Object = MibTableColumn
fdryRadiusServerUsage = _FdryRadiusServerUsage_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 8, 1, 1, 1, 1, 7),
    _FdryRadiusServerUsage_Type()
)
fdryRadiusServerUsage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryRadiusServerUsage.setStatus("current")
_FdryRadiusServerRowStatus_Type = RowStatus
_FdryRadiusServerRowStatus_Object = MibTableColumn
fdryRadiusServerRowStatus = _FdryRadiusServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 8, 1, 1, 1, 1, 8),
    _FdryRadiusServerRowStatus_Type()
)
fdryRadiusServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryRadiusServerRowStatus.setStatus("current")


class _FdryRadiusServerAuthType_Type(OctetString):
    """Custom type fdryRadiusServerAuthType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_FdryRadiusServerAuthType_Type.__name__ = "OctetString"
_FdryRadiusServerAuthType_Object = MibTableColumn
fdryRadiusServerAuthType = _FdryRadiusServerAuthType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 8, 1, 1, 1, 1, 9),
    _FdryRadiusServerAuthType_Type()
)
fdryRadiusServerAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryRadiusServerAuthType.setStatus("current")


class _FdryRadiusServerPriority_Type(Unsigned32):
    """Custom type fdryRadiusServerPriority based on Unsigned32"""
    defaultValue = 0


_FdryRadiusServerPriority_Type.__name__ = "Unsigned32"
_FdryRadiusServerPriority_Object = MibTableColumn
fdryRadiusServerPriority = _FdryRadiusServerPriority_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 8, 1, 1, 1, 1, 10),
    _FdryRadiusServerPriority_Type()
)
fdryRadiusServerPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryRadiusServerPriority.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FDRY-RADIUS-MIB",
    **{"ServerUsage": ServerUsage,
       "InetAddress": InetAddress,
       "fdryRadiusMIB": fdryRadiusMIB,
       "fdryRadiusServer": fdryRadiusServer,
       "fdryRadiusServerTable": fdryRadiusServerTable,
       "fdryRadiusServerEntry": fdryRadiusServerEntry,
       "fdryRadiusServerIndex": fdryRadiusServerIndex,
       "fdryRadiusServerAddrType": fdryRadiusServerAddrType,
       "fdryRadiusServerAddr": fdryRadiusServerAddr,
       "fdryRadiusServerAuthPort": fdryRadiusServerAuthPort,
       "fdryRadiusServerAcctPort": fdryRadiusServerAcctPort,
       "fdryRadiusServerRowKey": fdryRadiusServerRowKey,
       "fdryRadiusServerUsage": fdryRadiusServerUsage,
       "fdryRadiusServerRowStatus": fdryRadiusServerRowStatus,
       "fdryRadiusServerAuthType": fdryRadiusServerAuthType,
       "fdryRadiusServerPriority": fdryRadiusServerPriority}
)
