# SNMP MIB module (SWITCH-SNTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/SWITCH-SNTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:34 2025
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

(iscomSwitch,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "iscomSwitch")

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

(EnableVar,) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar")


# MODULE-IDENTITY

rcSntp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 8)
)
if mibBuilder.loadTexts:
    rcSntp.setRevisions(
        ("1904-12-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcSntpServer_ObjectIdentity = ObjectIdentity
rcSntpServer = _RcSntpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 8, 1)
)


class _RcSntpServerEnable_Type(EnableVar):
    """Custom type rcSntpServerEnable based on EnableVar"""
    defaultValue = 2


_RcSntpServerEnable_Type.__name__ = "EnableVar"
_RcSntpServerEnable_Object = MibScalar
rcSntpServerEnable = _RcSntpServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 8, 1, 1),
    _RcSntpServerEnable_Type()
)
rcSntpServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcSntpServerEnable.setStatus("current")
_RcSntpServerBroadcastAddress_Type = IpAddress
_RcSntpServerBroadcastAddress_Object = MibScalar
rcSntpServerBroadcastAddress = _RcSntpServerBroadcastAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 8, 1, 2),
    _RcSntpServerBroadcastAddress_Type()
)
rcSntpServerBroadcastAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcSntpServerBroadcastAddress.setStatus("current")


class _RcSntpServerSendInterval_Type(Integer32):
    """Custom type rcSntpServerSendInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RcSntpServerSendInterval_Type.__name__ = "Integer32"
_RcSntpServerSendInterval_Object = MibScalar
rcSntpServerSendInterval = _RcSntpServerSendInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 8, 1, 3),
    _RcSntpServerSendInterval_Type()
)
rcSntpServerSendInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcSntpServerSendInterval.setStatus("current")
_RcSntpClient_ObjectIdentity = ObjectIdentity
rcSntpClient = _RcSntpClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 8, 2)
)
_RcSntpClientAddress_Type = IpAddress
_RcSntpClientAddress_Object = MibScalar
rcSntpClientAddress = _RcSntpClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 8, 2, 1),
    _RcSntpClientAddress_Type()
)
rcSntpClientAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcSntpClientAddress.setStatus("current")


class _RcSntpClientGet_Type(Integer32):
    """Custom type rcSntpClientGet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("get", 1)
    )


_RcSntpClientGet_Type.__name__ = "Integer32"
_RcSntpClientGet_Object = MibScalar
rcSntpClientGet = _RcSntpClientGet_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 8, 2, 2),
    _RcSntpClientGet_Type()
)
rcSntpClientGet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcSntpClientGet.setStatus("current")


class _RcSntpClientListenEnable_Type(EnableVar):
    """Custom type rcSntpClientListenEnable based on EnableVar"""
    defaultValue = 2


_RcSntpClientListenEnable_Type.__name__ = "EnableVar"
_RcSntpClientListenEnable_Object = MibScalar
rcSntpClientListenEnable = _RcSntpClientListenEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 8, 2, 3),
    _RcSntpClientListenEnable_Type()
)
rcSntpClientListenEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcSntpClientListenEnable.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWITCH-SNTP-MIB",
    **{"rcSntp": rcSntp,
       "rcSntpServer": rcSntpServer,
       "rcSntpServerEnable": rcSntpServerEnable,
       "rcSntpServerBroadcastAddress": rcSntpServerBroadcastAddress,
       "rcSntpServerSendInterval": rcSntpServerSendInterval,
       "rcSntpClient": rcSntpClient,
       "rcSntpClientAddress": rcSntpClientAddress,
       "rcSntpClientGet": rcSntpClientGet,
       "rcSntpClientListenEnable": rcSntpClientListenEnable}
)
