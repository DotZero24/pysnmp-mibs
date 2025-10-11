# SNMP MIB module (SUPERMICRO-LDP-TEST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-LDP-TEST-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:04:51 2025
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
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fsLdpTestMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 14)
)
if mibBuilder.loadTexts:
    fsLdpTestMIB.setRevisions(
        ("2012-11-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsLdpTestObjects_ObjectIdentity = ObjectIdentity
fsLdpTestObjects = _FsLdpTestObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 14, 1)
)
_FsLdpTcpConnectionTable_Object = MibTable
fsLdpTcpConnectionTable = _FsLdpTcpConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 14, 1, 1)
)
if mibBuilder.loadTexts:
    fsLdpTcpConnectionTable.setStatus("current")
_FsLdpTcpConnectionEntry_Object = MibTableRow
fsLdpTcpConnectionEntry = _FsLdpTcpConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 14, 1, 1, 1)
)
fsLdpTcpConnectionEntry.setIndexNames(
    (0, "SUPERMICRO-LDP-TEST-MIB", "fsLdpTcpConnectionId"),
)
if mibBuilder.loadTexts:
    fsLdpTcpConnectionEntry.setStatus("current")


class _FsLdpTcpConnectionId_Type(Unsigned32):
    """Custom type fsLdpTcpConnectionId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_FsLdpTcpConnectionId_Type.__name__ = "Unsigned32"
_FsLdpTcpConnectionId_Object = MibTableColumn
fsLdpTcpConnectionId = _FsLdpTcpConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 14, 1, 1, 1, 1),
    _FsLdpTcpConnectionId_Type()
)
fsLdpTcpConnectionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsLdpTcpConnectionId.setStatus("current")
_FsLdpTcpDestIpAddress_Type = IpAddress
_FsLdpTcpDestIpAddress_Object = MibTableColumn
fsLdpTcpDestIpAddress = _FsLdpTcpDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 14, 1, 1, 1, 2),
    _FsLdpTcpDestIpAddress_Type()
)
fsLdpTcpDestIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLdpTcpDestIpAddress.setStatus("current")
_FsLdpTcpSourceIpAddress_Type = IpAddress
_FsLdpTcpSourceIpAddress_Object = MibTableColumn
fsLdpTcpSourceIpAddress = _FsLdpTcpSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 14, 1, 1, 1, 3),
    _FsLdpTcpSourceIpAddress_Type()
)
fsLdpTcpSourceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLdpTcpSourceIpAddress.setStatus("current")


class _FsLdpTcpDestPort_Type(Unsigned32):
    """Custom type fsLdpTcpDestPort based on Unsigned32"""
    defaultValue = 646

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsLdpTcpDestPort_Type.__name__ = "Unsigned32"
_FsLdpTcpDestPort_Object = MibTableColumn
fsLdpTcpDestPort = _FsLdpTcpDestPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 14, 1, 1, 1, 4),
    _FsLdpTcpDestPort_Type()
)
fsLdpTcpDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLdpTcpDestPort.setStatus("current")


class _FsLdpTcpSourcePort_Type(Unsigned32):
    """Custom type fsLdpTcpSourcePort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsLdpTcpSourcePort_Type.__name__ = "Unsigned32"
_FsLdpTcpSourcePort_Object = MibTableColumn
fsLdpTcpSourcePort = _FsLdpTcpSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 14, 1, 1, 1, 5),
    _FsLdpTcpSourcePort_Type()
)
fsLdpTcpSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLdpTcpSourcePort.setStatus("current")


class _FsLdpTcpPacketTxValue_Type(DisplayString):
    """Custom type fsLdpTcpPacketTxValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1500),
    )


_FsLdpTcpPacketTxValue_Type.__name__ = "DisplayString"
_FsLdpTcpPacketTxValue_Object = MibTableColumn
fsLdpTcpPacketTxValue = _FsLdpTcpPacketTxValue_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 14, 1, 1, 1, 6),
    _FsLdpTcpPacketTxValue_Type()
)
fsLdpTcpPacketTxValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLdpTcpPacketTxValue.setStatus("current")
_FsLdpTcpConnectionRowStatus_Type = RowStatus
_FsLdpTcpConnectionRowStatus_Object = MibTableColumn
fsLdpTcpConnectionRowStatus = _FsLdpTcpConnectionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 14, 1, 1, 1, 7),
    _FsLdpTcpConnectionRowStatus_Type()
)
fsLdpTcpConnectionRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLdpTcpConnectionRowStatus.setStatus("current")


class _FsLdpTcpVrfName_Type(DisplayString):
    """Custom type fsLdpTcpVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsLdpTcpVrfName_Type.__name__ = "DisplayString"
_FsLdpTcpVrfName_Object = MibTableColumn
fsLdpTcpVrfName = _FsLdpTcpVrfName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 14, 1, 1, 1, 8),
    _FsLdpTcpVrfName_Type()
)
fsLdpTcpVrfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLdpTcpVrfName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-LDP-TEST-MIB",
    **{"fsLdpTestMIB": fsLdpTestMIB,
       "fsLdpTestObjects": fsLdpTestObjects,
       "fsLdpTcpConnectionTable": fsLdpTcpConnectionTable,
       "fsLdpTcpConnectionEntry": fsLdpTcpConnectionEntry,
       "fsLdpTcpConnectionId": fsLdpTcpConnectionId,
       "fsLdpTcpDestIpAddress": fsLdpTcpDestIpAddress,
       "fsLdpTcpSourceIpAddress": fsLdpTcpSourceIpAddress,
       "fsLdpTcpDestPort": fsLdpTcpDestPort,
       "fsLdpTcpSourcePort": fsLdpTcpSourcePort,
       "fsLdpTcpPacketTxValue": fsLdpTcpPacketTxValue,
       "fsLdpTcpConnectionRowStatus": fsLdpTcpConnectionRowStatus,
       "fsLdpTcpVrfName": fsLdpTcpVrfName}
)
