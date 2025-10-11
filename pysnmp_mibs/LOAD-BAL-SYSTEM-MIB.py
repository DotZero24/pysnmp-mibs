# SNMP MIB module (LOAD-BAL-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/extreme/LOAD-BAL-SYSTEM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:05:59 2025
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_F5_ObjectIdentity = ObjectIdentity
f5 = _F5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375)
)
_F5systems_ObjectIdentity = ObjectIdentity
f5systems = _F5systems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1)
)
_Loadbal_ObjectIdentity = ObjectIdentity
loadbal = _Loadbal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1)
)
_VirtualAddress_ObjectIdentity = ObjectIdentity
virtualAddress = _VirtualAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2)
)


class _VirtualAddressNumber_Type(Integer32):
    """Custom type virtualAddressNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VirtualAddressNumber_Type.__name__ = "Integer32"
_VirtualAddressNumber_Object = MibScalar
virtualAddressNumber = _VirtualAddressNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 1),
    _VirtualAddressNumber_Type()
)
virtualAddressNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddressNumber.setStatus("mandatory")
_VirtualAddressTable_Object = MibTable
virtualAddressTable = _VirtualAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    virtualAddressTable.setStatus("mandatory")
_VirtualAddressEntry_Object = MibTableRow
virtualAddressEntry = _VirtualAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 2, 1)
)
virtualAddressEntry.setIndexNames(
    (0, "LOAD-BAL-SYSTEM-MIB", "virtualAddressIpAddress"),
)
if mibBuilder.loadTexts:
    virtualAddressEntry.setStatus("mandatory")
_VirtualAddressIpAddress_Type = IpAddress
_VirtualAddressIpAddress_Object = MibTableColumn
virtualAddressIpAddress = _VirtualAddressIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 2, 1, 1),
    _VirtualAddressIpAddress_Type()
)
virtualAddressIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddressIpAddress.setStatus("mandatory")


class _VirtualAddressStatus_Type(Integer32):
    """Custom type virtualAddressStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("maintainance", 2))
    )


_VirtualAddressStatus_Type.__name__ = "Integer32"
_VirtualAddressStatus_Object = MibTableColumn
virtualAddressStatus = _VirtualAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 2, 1, 2),
    _VirtualAddressStatus_Type()
)
virtualAddressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddressStatus.setStatus("mandatory")


class _VirtualAddressConnLimit_Type(Integer32):
    """Custom type virtualAddressConnLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VirtualAddressConnLimit_Type.__name__ = "Integer32"
_VirtualAddressConnLimit_Object = MibTableColumn
virtualAddressConnLimit = _VirtualAddressConnLimit_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 2, 1, 3),
    _VirtualAddressConnLimit_Type()
)
virtualAddressConnLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddressConnLimit.setStatus("mandatory")
_VirtualAddressNetmask_Type = IpAddress
_VirtualAddressNetmask_Object = MibTableColumn
virtualAddressNetmask = _VirtualAddressNetmask_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 2, 1, 4),
    _VirtualAddressNetmask_Type()
)
virtualAddressNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddressNetmask.setStatus("mandatory")
_VirtualAddressBroadcast_Type = IpAddress
_VirtualAddressBroadcast_Object = MibTableColumn
virtualAddressBroadcast = _VirtualAddressBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 2, 1, 5),
    _VirtualAddressBroadcast_Type()
)
virtualAddressBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddressBroadcast.setStatus("mandatory")


class _VirtualAddressInterface_Type(DisplayString):
    """Custom type virtualAddressInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_VirtualAddressInterface_Type.__name__ = "DisplayString"
_VirtualAddressInterface_Object = MibTableColumn
virtualAddressInterface = _VirtualAddressInterface_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 2, 1, 6),
    _VirtualAddressInterface_Type()
)
virtualAddressInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddressInterface.setStatus("mandatory")


class _VirtualAddressFailoverFlags_Type(Integer32):
    """Custom type virtualAddressFailoverFlags based on Integer32"""
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
        *(("mirrorconnections", 1),
          ("mirrorpersistence", 2),
          ("mirrorconnectionspersistence", 3),
          ("nomirroring", 4))
    )


_VirtualAddressFailoverFlags_Type.__name__ = "Integer32"
_VirtualAddressFailoverFlags_Object = MibTableColumn
virtualAddressFailoverFlags = _VirtualAddressFailoverFlags_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 2, 1, 7),
    _VirtualAddressFailoverFlags_Type()
)
virtualAddressFailoverFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddressFailoverFlags.setStatus("mandatory")
_VirtualAddressOctetsIn_Type = Counter32
_VirtualAddressOctetsIn_Object = MibTableColumn
virtualAddressOctetsIn = _VirtualAddressOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 2, 1, 8),
    _VirtualAddressOctetsIn_Type()
)
virtualAddressOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddressOctetsIn.setStatus("mandatory")
_VirtualAddressOctetsOut_Type = Counter32
_VirtualAddressOctetsOut_Object = MibTableColumn
virtualAddressOctetsOut = _VirtualAddressOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 2, 1, 9),
    _VirtualAddressOctetsOut_Type()
)
virtualAddressOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddressOctetsOut.setStatus("mandatory")
_VirtualAddressPacketsIn_Type = Counter32
_VirtualAddressPacketsIn_Object = MibTableColumn
virtualAddressPacketsIn = _VirtualAddressPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 2, 1, 10),
    _VirtualAddressPacketsIn_Type()
)
virtualAddressPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddressPacketsIn.setStatus("mandatory")
_VirtualAddressPacketsOut_Type = Counter32
_VirtualAddressPacketsOut_Object = MibTableColumn
virtualAddressPacketsOut = _VirtualAddressPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 2, 1, 11),
    _VirtualAddressPacketsOut_Type()
)
virtualAddressPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddressPacketsOut.setStatus("mandatory")


class _VirtualAddressCurrentConn_Type(Integer32):
    """Custom type virtualAddressCurrentConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VirtualAddressCurrentConn_Type.__name__ = "Integer32"
_VirtualAddressCurrentConn_Object = MibTableColumn
virtualAddressCurrentConn = _VirtualAddressCurrentConn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 2, 1, 12),
    _VirtualAddressCurrentConn_Type()
)
virtualAddressCurrentConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddressCurrentConn.setStatus("mandatory")


class _VirtualAddressMaxConn_Type(Integer32):
    """Custom type virtualAddressMaxConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VirtualAddressMaxConn_Type.__name__ = "Integer32"
_VirtualAddressMaxConn_Object = MibTableColumn
virtualAddressMaxConn = _VirtualAddressMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 2, 1, 13),
    _VirtualAddressMaxConn_Type()
)
virtualAddressMaxConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddressMaxConn.setStatus("mandatory")
_VirtualAddressTotalConn_Type = Counter32
_VirtualAddressTotalConn_Object = MibTableColumn
virtualAddressTotalConn = _VirtualAddressTotalConn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 2, 1, 14),
    _VirtualAddressTotalConn_Type()
)
virtualAddressTotalConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddressTotalConn.setStatus("mandatory")
_VirtualAddressOctetsInHi32_Type = Counter32
_VirtualAddressOctetsInHi32_Object = MibTableColumn
virtualAddressOctetsInHi32 = _VirtualAddressOctetsInHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 2, 1, 15),
    _VirtualAddressOctetsInHi32_Type()
)
virtualAddressOctetsInHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddressOctetsInHi32.setStatus("mandatory")
_VirtualAddressOctetsOutHi32_Type = Counter32
_VirtualAddressOctetsOutHi32_Object = MibTableColumn
virtualAddressOctetsOutHi32 = _VirtualAddressOctetsOutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 2, 1, 16),
    _VirtualAddressOctetsOutHi32_Type()
)
virtualAddressOctetsOutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddressOctetsOutHi32.setStatus("mandatory")
_VirtualAddressPacketsInHi32_Type = Counter32
_VirtualAddressPacketsInHi32_Object = MibTableColumn
virtualAddressPacketsInHi32 = _VirtualAddressPacketsInHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 2, 1, 17),
    _VirtualAddressPacketsInHi32_Type()
)
virtualAddressPacketsInHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddressPacketsInHi32.setStatus("mandatory")
_VirtualAddressPacketsOutHi32_Type = Counter32
_VirtualAddressPacketsOutHi32_Object = MibTableColumn
virtualAddressPacketsOutHi32 = _VirtualAddressPacketsOutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 2, 1, 18),
    _VirtualAddressPacketsOutHi32_Type()
)
virtualAddressPacketsOutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddressPacketsOutHi32.setStatus("mandatory")
_VirtualAddressUnitId_Type = Integer32
_VirtualAddressUnitId_Object = MibTableColumn
virtualAddressUnitId = _VirtualAddressUnitId_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 2, 1, 19),
    _VirtualAddressUnitId_Type()
)
virtualAddressUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddressUnitId.setStatus("mandatory")
_VirtualServer_ObjectIdentity = ObjectIdentity
virtualServer = _VirtualServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3)
)


class _VirtualServerNumber_Type(Integer32):
    """Custom type virtualServerNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VirtualServerNumber_Type.__name__ = "Integer32"
_VirtualServerNumber_Object = MibScalar
virtualServerNumber = _VirtualServerNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 1),
    _VirtualServerNumber_Type()
)
virtualServerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerNumber.setStatus("mandatory")
_VirtualServerTable_Object = MibTable
virtualServerTable = _VirtualServerTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    virtualServerTable.setStatus("mandatory")
_VirtualServerEntry_Object = MibTableRow
virtualServerEntry = _VirtualServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1)
)
virtualServerEntry.setIndexNames(
    (0, "LOAD-BAL-SYSTEM-MIB", "virtualServerIpAddress"),
    (0, "LOAD-BAL-SYSTEM-MIB", "virtualServerPort"),
)
if mibBuilder.loadTexts:
    virtualServerEntry.setStatus("mandatory")
_VirtualServerIpAddress_Type = IpAddress
_VirtualServerIpAddress_Object = MibTableColumn
virtualServerIpAddress = _VirtualServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 1),
    _VirtualServerIpAddress_Type()
)
virtualServerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerIpAddress.setStatus("mandatory")


class _VirtualServerPort_Type(Integer32):
    """Custom type virtualServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VirtualServerPort_Type.__name__ = "Integer32"
_VirtualServerPort_Object = MibTableColumn
virtualServerPort = _VirtualServerPort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 2),
    _VirtualServerPort_Type()
)
virtualServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerPort.setStatus("mandatory")


class _VirtualServerStatus_Type(Integer32):
    """Custom type virtualServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("maintainance", 2))
    )


_VirtualServerStatus_Type.__name__ = "Integer32"
_VirtualServerStatus_Object = MibTableColumn
virtualServerStatus = _VirtualServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 3),
    _VirtualServerStatus_Type()
)
virtualServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerStatus.setStatus("mandatory")


class _VirtualServerConnLimit_Type(Integer32):
    """Custom type virtualServerConnLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VirtualServerConnLimit_Type.__name__ = "Integer32"
_VirtualServerConnLimit_Object = MibTableColumn
virtualServerConnLimit = _VirtualServerConnLimit_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 4),
    _VirtualServerConnLimit_Type()
)
virtualServerConnLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerConnLimit.setStatus("mandatory")


class _VirtualServerAppProtocol_Type(Integer32):
    """Custom type virtualServerAppProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("ssl", 2),
          ("http-cookie", 3))
    )


_VirtualServerAppProtocol_Type.__name__ = "Integer32"
_VirtualServerAppProtocol_Object = MibTableColumn
virtualServerAppProtocol = _VirtualServerAppProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 5),
    _VirtualServerAppProtocol_Type()
)
virtualServerAppProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerAppProtocol.setStatus("mandatory")


class _VirtualServerAppProtocolTimeout_Type(Integer32):
    """Custom type virtualServerAppProtocolTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VirtualServerAppProtocolTimeout_Type.__name__ = "Integer32"
_VirtualServerAppProtocolTimeout_Object = MibTableColumn
virtualServerAppProtocolTimeout = _VirtualServerAppProtocolTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 6),
    _VirtualServerAppProtocolTimeout_Type()
)
virtualServerAppProtocolTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerAppProtocolTimeout.setStatus("mandatory")


class _VirtualServerAppProtocolReaper_Type(Integer32):
    """Custom type virtualServerAppProtocolReaper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VirtualServerAppProtocolReaper_Type.__name__ = "Integer32"
_VirtualServerAppProtocolReaper_Object = MibTableColumn
virtualServerAppProtocolReaper = _VirtualServerAppProtocolReaper_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 7),
    _VirtualServerAppProtocolReaper_Type()
)
virtualServerAppProtocolReaper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerAppProtocolReaper.setStatus("mandatory")
_VirtualServerPersistTimeout_Type = Integer32
_VirtualServerPersistTimeout_Object = MibTableColumn
virtualServerPersistTimeout = _VirtualServerPersistTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 8),
    _VirtualServerPersistTimeout_Type()
)
virtualServerPersistTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerPersistTimeout.setStatus("mandatory")
_VirtualServerPersistMask_Type = IpAddress
_VirtualServerPersistMask_Object = MibTableColumn
virtualServerPersistMask = _VirtualServerPersistMask_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 9),
    _VirtualServerPersistMask_Type()
)
virtualServerPersistMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerPersistMask.setStatus("mandatory")


class _VirtualServerSticky_Type(Integer32):
    """Custom type virtualServerSticky based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_VirtualServerSticky_Type.__name__ = "Integer32"
_VirtualServerSticky_Object = MibTableColumn
virtualServerSticky = _VirtualServerSticky_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 10),
    _VirtualServerSticky_Type()
)
virtualServerSticky.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerSticky.setStatus("mandatory")
_VirtualServerStickyMask_Type = IpAddress
_VirtualServerStickyMask_Object = MibTableColumn
virtualServerStickyMask = _VirtualServerStickyMask_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 11),
    _VirtualServerStickyMask_Type()
)
virtualServerStickyMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerStickyMask.setStatus("mandatory")


class _VirtualServerFailoverFlags_Type(Integer32):
    """Custom type virtualServerFailoverFlags based on Integer32"""
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
        *(("mirrorconnections", 1),
          ("mirrorpersistence", 2),
          ("mirrorconnectionspersistence", 3),
          ("nomirroring", 4))
    )


_VirtualServerFailoverFlags_Type.__name__ = "Integer32"
_VirtualServerFailoverFlags_Object = MibTableColumn
virtualServerFailoverFlags = _VirtualServerFailoverFlags_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 12),
    _VirtualServerFailoverFlags_Type()
)
virtualServerFailoverFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerFailoverFlags.setStatus("mandatory")
_VirtualServerOctetsIn_Type = Counter32
_VirtualServerOctetsIn_Object = MibTableColumn
virtualServerOctetsIn = _VirtualServerOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 13),
    _VirtualServerOctetsIn_Type()
)
virtualServerOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerOctetsIn.setStatus("mandatory")
_VirtualServerOctetsOut_Type = Counter32
_VirtualServerOctetsOut_Object = MibTableColumn
virtualServerOctetsOut = _VirtualServerOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 14),
    _VirtualServerOctetsOut_Type()
)
virtualServerOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerOctetsOut.setStatus("mandatory")
_VirtualServerPacketsIn_Type = Counter32
_VirtualServerPacketsIn_Object = MibTableColumn
virtualServerPacketsIn = _VirtualServerPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 15),
    _VirtualServerPacketsIn_Type()
)
virtualServerPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerPacketsIn.setStatus("mandatory")
_VirtualServerPacketsOut_Type = Counter32
_VirtualServerPacketsOut_Object = MibTableColumn
virtualServerPacketsOut = _VirtualServerPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 16),
    _VirtualServerPacketsOut_Type()
)
virtualServerPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerPacketsOut.setStatus("mandatory")


class _VirtualServerCurrentConn_Type(Integer32):
    """Custom type virtualServerCurrentConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VirtualServerCurrentConn_Type.__name__ = "Integer32"
_VirtualServerCurrentConn_Object = MibTableColumn
virtualServerCurrentConn = _VirtualServerCurrentConn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 17),
    _VirtualServerCurrentConn_Type()
)
virtualServerCurrentConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerCurrentConn.setStatus("mandatory")


class _VirtualServerMaxConn_Type(Integer32):
    """Custom type virtualServerMaxConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VirtualServerMaxConn_Type.__name__ = "Integer32"
_VirtualServerMaxConn_Object = MibTableColumn
virtualServerMaxConn = _VirtualServerMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 18),
    _VirtualServerMaxConn_Type()
)
virtualServerMaxConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerMaxConn.setStatus("mandatory")
_VirtualServerTotalConn_Type = Counter32
_VirtualServerTotalConn_Object = MibTableColumn
virtualServerTotalConn = _VirtualServerTotalConn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 19),
    _VirtualServerTotalConn_Type()
)
virtualServerTotalConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerTotalConn.setStatus("mandatory")
_VirtualServerSslNew_Type = Counter32
_VirtualServerSslNew_Object = MibTableColumn
virtualServerSslNew = _VirtualServerSslNew_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 20),
    _VirtualServerSslNew_Type()
)
virtualServerSslNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerSslNew.setStatus("mandatory")
_VirtualServerSslHits_Type = Counter32
_VirtualServerSslHits_Object = MibTableColumn
virtualServerSslHits = _VirtualServerSslHits_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 21),
    _VirtualServerSslHits_Type()
)
virtualServerSslHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerSslHits.setStatus("mandatory")
_VirtualServerSslTimeouts_Type = Counter32
_VirtualServerSslTimeouts_Object = MibTableColumn
virtualServerSslTimeouts = _VirtualServerSslTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 22),
    _VirtualServerSslTimeouts_Type()
)
virtualServerSslTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerSslTimeouts.setStatus("mandatory")
_VirtualServerSslMisses_Type = Counter32
_VirtualServerSslMisses_Object = MibTableColumn
virtualServerSslMisses = _VirtualServerSslMisses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 23),
    _VirtualServerSslMisses_Type()
)
virtualServerSslMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerSslMisses.setStatus("mandatory")
_VirtualServerOctetsInHi32_Type = Counter32
_VirtualServerOctetsInHi32_Object = MibTableColumn
virtualServerOctetsInHi32 = _VirtualServerOctetsInHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 24),
    _VirtualServerOctetsInHi32_Type()
)
virtualServerOctetsInHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerOctetsInHi32.setStatus("mandatory")
_VirtualServerOctetsOutHi32_Type = Counter32
_VirtualServerOctetsOutHi32_Object = MibTableColumn
virtualServerOctetsOutHi32 = _VirtualServerOctetsOutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 25),
    _VirtualServerOctetsOutHi32_Type()
)
virtualServerOctetsOutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerOctetsOutHi32.setStatus("mandatory")
_VirtualServerPacketsInHi32_Type = Counter32
_VirtualServerPacketsInHi32_Object = MibTableColumn
virtualServerPacketsInHi32 = _VirtualServerPacketsInHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 26),
    _VirtualServerPacketsInHi32_Type()
)
virtualServerPacketsInHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerPacketsInHi32.setStatus("mandatory")
_VirtualServerPacketsOutHi32_Type = Counter32
_VirtualServerPacketsOutHi32_Object = MibTableColumn
virtualServerPacketsOutHi32 = _VirtualServerPacketsOutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 27),
    _VirtualServerPacketsOutHi32_Type()
)
virtualServerPacketsOutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerPacketsOutHi32.setStatus("mandatory")


class _VirtualServerCookieMethod_Type(Integer32):
    """Custom type virtualServerCookieMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("insert", 1),
          ("rewrite", 2),
          ("passive", 3))
    )


_VirtualServerCookieMethod_Type.__name__ = "Integer32"
_VirtualServerCookieMethod_Object = MibTableColumn
virtualServerCookieMethod = _VirtualServerCookieMethod_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 28),
    _VirtualServerCookieMethod_Type()
)
virtualServerCookieMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerCookieMethod.setStatus("mandatory")


class _VirtualServerRule_Type(DisplayString):
    """Custom type virtualServerRule based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VirtualServerRule_Type.__name__ = "DisplayString"
_VirtualServerRule_Object = MibTableColumn
virtualServerRule = _VirtualServerRule_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 29),
    _VirtualServerRule_Type()
)
virtualServerRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerRule.setStatus("mandatory")


class _VirtualServerPool_Type(DisplayString):
    """Custom type virtualServerPool based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VirtualServerPool_Type.__name__ = "DisplayString"
_VirtualServerPool_Object = MibTableColumn
virtualServerPool = _VirtualServerPool_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 30),
    _VirtualServerPool_Type()
)
virtualServerPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerPool.setStatus("mandatory")
_Snat_ObjectIdentity = ObjectIdentity
snat = _Snat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4)
)
_SnatTransTable_Object = MibTable
snatTransTable = _SnatTransTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    snatTransTable.setStatus("mandatory")
_SnatTransEntry_Object = MibTableRow
snatTransEntry = _SnatTransEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1, 1)
)
snatTransEntry.setIndexNames(
    (0, "LOAD-BAL-SYSTEM-MIB", "snatTransAddr"),
)
if mibBuilder.loadTexts:
    snatTransEntry.setStatus("mandatory")


class _SnatTransEnabled_Type(Integer32):
    """Custom type snatTransEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_SnatTransEnabled_Type.__name__ = "Integer32"
_SnatTransEnabled_Object = MibTableColumn
snatTransEnabled = _SnatTransEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1, 1, 1),
    _SnatTransEnabled_Type()
)
snatTransEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatTransEnabled.setStatus("mandatory")
_SnatTransAddr_Type = IpAddress
_SnatTransAddr_Object = MibTableColumn
snatTransAddr = _SnatTransAddr_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1, 1, 2),
    _SnatTransAddr_Type()
)
snatTransAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatTransAddr.setStatus("mandatory")


class _SnatTransIface_Type(DisplayString):
    """Custom type snatTransIface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SnatTransIface_Type.__name__ = "DisplayString"
_SnatTransIface_Object = MibTableColumn
snatTransIface = _SnatTransIface_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1, 1, 3),
    _SnatTransIface_Type()
)
snatTransIface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatTransIface.setStatus("mandatory")
_SnatTransNetmask_Type = IpAddress
_SnatTransNetmask_Object = MibTableColumn
snatTransNetmask = _SnatTransNetmask_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1, 1, 4),
    _SnatTransNetmask_Type()
)
snatTransNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatTransNetmask.setStatus("mandatory")
_SnatTransBroadcast_Type = IpAddress
_SnatTransBroadcast_Object = MibTableColumn
snatTransBroadcast = _SnatTransBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1, 1, 5),
    _SnatTransBroadcast_Type()
)
snatTransBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatTransBroadcast.setStatus("mandatory")
_SnatTransSecsCollectingStats_Type = Counter32
_SnatTransSecsCollectingStats_Object = MibTableColumn
snatTransSecsCollectingStats = _SnatTransSecsCollectingStats_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1, 1, 6),
    _SnatTransSecsCollectingStats_Type()
)
snatTransSecsCollectingStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatTransSecsCollectingStats.setStatus("mandatory")
_SnatTransBitsIn_Type = Counter32
_SnatTransBitsIn_Object = MibTableColumn
snatTransBitsIn = _SnatTransBitsIn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1, 1, 7),
    _SnatTransBitsIn_Type()
)
snatTransBitsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatTransBitsIn.setStatus("mandatory")
_SnatTransBitsOut_Type = Counter32
_SnatTransBitsOut_Object = MibTableColumn
snatTransBitsOut = _SnatTransBitsOut_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1, 1, 8),
    _SnatTransBitsOut_Type()
)
snatTransBitsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatTransBitsOut.setStatus("mandatory")
_SnatTransPktsIn_Type = Counter32
_SnatTransPktsIn_Object = MibTableColumn
snatTransPktsIn = _SnatTransPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1, 1, 9),
    _SnatTransPktsIn_Type()
)
snatTransPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatTransPktsIn.setStatus("mandatory")
_SnatTransPktsOut_Type = Counter32
_SnatTransPktsOut_Object = MibTableColumn
snatTransPktsOut = _SnatTransPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1, 1, 10),
    _SnatTransPktsOut_Type()
)
snatTransPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatTransPktsOut.setStatus("mandatory")
_SnatTransCurrConns_Type = Integer32
_SnatTransCurrConns_Object = MibTableColumn
snatTransCurrConns = _SnatTransCurrConns_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1, 1, 11),
    _SnatTransCurrConns_Type()
)
snatTransCurrConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatTransCurrConns.setStatus("mandatory")
_SnatTransMaxConns_Type = Integer32
_SnatTransMaxConns_Object = MibTableColumn
snatTransMaxConns = _SnatTransMaxConns_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1, 1, 12),
    _SnatTransMaxConns_Type()
)
snatTransMaxConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatTransMaxConns.setStatus("mandatory")
_SnatTransTotalConns_Type = Counter32
_SnatTransTotalConns_Object = MibTableColumn
snatTransTotalConns = _SnatTransTotalConns_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1, 1, 13),
    _SnatTransTotalConns_Type()
)
snatTransTotalConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatTransTotalConns.setStatus("mandatory")
_SnatTransBitsInHi32_Type = Counter32
_SnatTransBitsInHi32_Object = MibTableColumn
snatTransBitsInHi32 = _SnatTransBitsInHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1, 1, 14),
    _SnatTransBitsInHi32_Type()
)
snatTransBitsInHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatTransBitsInHi32.setStatus("mandatory")
_SnatTransBitsOutHi32_Type = Counter32
_SnatTransBitsOutHi32_Object = MibTableColumn
snatTransBitsOutHi32 = _SnatTransBitsOutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1, 1, 15),
    _SnatTransBitsOutHi32_Type()
)
snatTransBitsOutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatTransBitsOutHi32.setStatus("mandatory")
_SnatTransPktsInHi32_Type = Counter32
_SnatTransPktsInHi32_Object = MibTableColumn
snatTransPktsInHi32 = _SnatTransPktsInHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1, 1, 16),
    _SnatTransPktsInHi32_Type()
)
snatTransPktsInHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatTransPktsInHi32.setStatus("mandatory")
_SnatTransPktsOutHi32_Type = Counter32
_SnatTransPktsOutHi32_Object = MibTableColumn
snatTransPktsOutHi32 = _SnatTransPktsOutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1, 1, 17),
    _SnatTransPktsOutHi32_Type()
)
snatTransPktsOutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatTransPktsOutHi32.setStatus("mandatory")
_SnatTransLastTransPort_Type = Integer32
_SnatTransLastTransPort_Object = MibTableColumn
snatTransLastTransPort = _SnatTransLastTransPort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1, 1, 18),
    _SnatTransLastTransPort_Type()
)
snatTransLastTransPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatTransLastTransPort.setStatus("mandatory")
_SnatTransUnitId_Type = Integer32
_SnatTransUnitId_Object = MibTableColumn
snatTransUnitId = _SnatTransUnitId_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1, 1, 19),
    _SnatTransUnitId_Type()
)
snatTransUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatTransUnitId.setStatus("mandatory")
_SnatOrigTable_Object = MibTable
snatOrigTable = _SnatOrigTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    snatOrigTable.setStatus("mandatory")
_SnatOrigEntry_Object = MibTableRow
snatOrigEntry = _SnatOrigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2, 1)
)
snatOrigEntry.setIndexNames(
    (0, "LOAD-BAL-SYSTEM-MIB", "snatOrigAddr"),
)
if mibBuilder.loadTexts:
    snatOrigEntry.setStatus("mandatory")


class _SnatOrigEnabled_Type(Integer32):
    """Custom type snatOrigEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_SnatOrigEnabled_Type.__name__ = "Integer32"
_SnatOrigEnabled_Object = MibTableColumn
snatOrigEnabled = _SnatOrigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2, 1, 1),
    _SnatOrigEnabled_Type()
)
snatOrigEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatOrigEnabled.setStatus("mandatory")
_SnatOrigAddr_Type = IpAddress
_SnatOrigAddr_Object = MibTableColumn
snatOrigAddr = _SnatOrigAddr_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2, 1, 2),
    _SnatOrigAddr_Type()
)
snatOrigAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatOrigAddr.setStatus("mandatory")
_SnatOrigConnLimit_Type = Integer32
_SnatOrigConnLimit_Object = MibTableColumn
snatOrigConnLimit = _SnatOrigConnLimit_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2, 1, 3),
    _SnatOrigConnLimit_Type()
)
snatOrigConnLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatOrigConnLimit.setStatus("mandatory")
_SnatOrigTransAddr_Type = IpAddress
_SnatOrigTransAddr_Object = MibTableColumn
snatOrigTransAddr = _SnatOrigTransAddr_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2, 1, 4),
    _SnatOrigTransAddr_Type()
)
snatOrigTransAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatOrigTransAddr.setStatus("mandatory")
_SnatOrigTcpIdleTimeout_Type = Counter32
_SnatOrigTcpIdleTimeout_Object = MibTableColumn
snatOrigTcpIdleTimeout = _SnatOrigTcpIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2, 1, 5),
    _SnatOrigTcpIdleTimeout_Type()
)
snatOrigTcpIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatOrigTcpIdleTimeout.setStatus("mandatory")
_SnatOrigUdpIdleTimeout_Type = Counter32
_SnatOrigUdpIdleTimeout_Object = MibTableColumn
snatOrigUdpIdleTimeout = _SnatOrigUdpIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2, 1, 6),
    _SnatOrigUdpIdleTimeout_Type()
)
snatOrigUdpIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatOrigUdpIdleTimeout.setStatus("mandatory")
_SnatOrigStatsZeroTime_Type = Counter32
_SnatOrigStatsZeroTime_Object = MibTableColumn
snatOrigStatsZeroTime = _SnatOrigStatsZeroTime_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2, 1, 7),
    _SnatOrigStatsZeroTime_Type()
)
snatOrigStatsZeroTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatOrigStatsZeroTime.setStatus("mandatory")
_SnatOrigSecsCollectingStats_Type = Counter32
_SnatOrigSecsCollectingStats_Object = MibTableColumn
snatOrigSecsCollectingStats = _SnatOrigSecsCollectingStats_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2, 1, 8),
    _SnatOrigSecsCollectingStats_Type()
)
snatOrigSecsCollectingStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatOrigSecsCollectingStats.setStatus("mandatory")
_SnatOrigBitsIn_Type = Counter32
_SnatOrigBitsIn_Object = MibTableColumn
snatOrigBitsIn = _SnatOrigBitsIn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2, 1, 9),
    _SnatOrigBitsIn_Type()
)
snatOrigBitsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatOrigBitsIn.setStatus("mandatory")
_SnatOrigBitsOut_Type = Counter32
_SnatOrigBitsOut_Object = MibTableColumn
snatOrigBitsOut = _SnatOrigBitsOut_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2, 1, 10),
    _SnatOrigBitsOut_Type()
)
snatOrigBitsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatOrigBitsOut.setStatus("mandatory")
_SnatOrigPktsIn_Type = Counter32
_SnatOrigPktsIn_Object = MibTableColumn
snatOrigPktsIn = _SnatOrigPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2, 1, 11),
    _SnatOrigPktsIn_Type()
)
snatOrigPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatOrigPktsIn.setStatus("mandatory")
_SnatOrigPktsOut_Type = Counter32
_SnatOrigPktsOut_Object = MibTableColumn
snatOrigPktsOut = _SnatOrigPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2, 1, 12),
    _SnatOrigPktsOut_Type()
)
snatOrigPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatOrigPktsOut.setStatus("mandatory")
_SnatOrigCurrConns_Type = Integer32
_SnatOrigCurrConns_Object = MibTableColumn
snatOrigCurrConns = _SnatOrigCurrConns_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2, 1, 13),
    _SnatOrigCurrConns_Type()
)
snatOrigCurrConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatOrigCurrConns.setStatus("mandatory")
_SnatOrigMaxConns_Type = Integer32
_SnatOrigMaxConns_Object = MibTableColumn
snatOrigMaxConns = _SnatOrigMaxConns_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2, 1, 14),
    _SnatOrigMaxConns_Type()
)
snatOrigMaxConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatOrigMaxConns.setStatus("mandatory")
_SnatOrigTotalConns_Type = Counter32
_SnatOrigTotalConns_Object = MibTableColumn
snatOrigTotalConns = _SnatOrigTotalConns_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2, 1, 15),
    _SnatOrigTotalConns_Type()
)
snatOrigTotalConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatOrigTotalConns.setStatus("mandatory")
_SnatOrigBitsInHi32_Type = Counter32
_SnatOrigBitsInHi32_Object = MibTableColumn
snatOrigBitsInHi32 = _SnatOrigBitsInHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2, 1, 16),
    _SnatOrigBitsInHi32_Type()
)
snatOrigBitsInHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatOrigBitsInHi32.setStatus("mandatory")
_SnatOrigBitsOutHi32_Type = Counter32
_SnatOrigBitsOutHi32_Object = MibTableColumn
snatOrigBitsOutHi32 = _SnatOrigBitsOutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2, 1, 17),
    _SnatOrigBitsOutHi32_Type()
)
snatOrigBitsOutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatOrigBitsOutHi32.setStatus("mandatory")
_SnatOrigPktsInHi32_Type = Counter32
_SnatOrigPktsInHi32_Object = MibTableColumn
snatOrigPktsInHi32 = _SnatOrigPktsInHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2, 1, 18),
    _SnatOrigPktsInHi32_Type()
)
snatOrigPktsInHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatOrigPktsInHi32.setStatus("mandatory")
_SnatOrigPktsOutHi32_Type = Counter32
_SnatOrigPktsOutHi32_Object = MibTableColumn
snatOrigPktsOutHi32 = _SnatOrigPktsOutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2, 1, 19),
    _SnatOrigPktsOutHi32_Type()
)
snatOrigPktsOutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatOrigPktsOutHi32.setStatus("mandatory")
_SnatOrigLastTransPort_Type = Integer32
_SnatOrigLastTransPort_Object = MibTableColumn
snatOrigLastTransPort = _SnatOrigLastTransPort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2, 1, 20),
    _SnatOrigLastTransPort_Type()
)
snatOrigLastTransPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatOrigLastTransPort.setStatus("mandatory")
_Interface_ObjectIdentity = ObjectIdentity
interface = _Interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 5)
)


class _InterfaceNumber_Type(Integer32):
    """Custom type interfaceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_InterfaceNumber_Type.__name__ = "Integer32"
_InterfaceNumber_Object = MibScalar
interfaceNumber = _InterfaceNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 5, 1),
    _InterfaceNumber_Type()
)
interfaceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceNumber.setStatus("mandatory")
_InterfaceTable_Object = MibTable
interfaceTable = _InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    interfaceTable.setStatus("mandatory")
_InterfaceEntry_Object = MibTableRow
interfaceEntry = _InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 5, 2, 1)
)
interfaceEntry.setIndexNames(
    (0, "LOAD-BAL-SYSTEM-MIB", "interfaceName"),
)
if mibBuilder.loadTexts:
    interfaceEntry.setStatus("mandatory")


class _InterfaceName_Type(DisplayString):
    """Custom type interfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_InterfaceName_Type.__name__ = "DisplayString"
_InterfaceName_Object = MibTableColumn
interfaceName = _InterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 5, 2, 1, 1),
    _InterfaceName_Type()
)
interfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceName.setStatus("mandatory")


class _InterfaceIpAddresses_Type(DisplayString):
    """Custom type interfaceIpAddresses based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_InterfaceIpAddresses_Type.__name__ = "DisplayString"
_InterfaceIpAddresses_Object = MibTableColumn
interfaceIpAddresses = _InterfaceIpAddresses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 5, 2, 1, 2),
    _InterfaceIpAddresses_Type()
)
interfaceIpAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceIpAddresses.setStatus("mandatory")


class _InterfaceDestination_Type(Integer32):
    """Custom type interfaceDestination based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_InterfaceDestination_Type.__name__ = "Integer32"
_InterfaceDestination_Object = MibTableColumn
interfaceDestination = _InterfaceDestination_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 5, 2, 1, 3),
    _InterfaceDestination_Type()
)
interfaceDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceDestination.setStatus("mandatory")


class _InterfaceSource_Type(Integer32):
    """Custom type interfaceSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_InterfaceSource_Type.__name__ = "Integer32"
_InterfaceSource_Object = MibTableColumn
interfaceSource = _InterfaceSource_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 5, 2, 1, 4),
    _InterfaceSource_Type()
)
interfaceSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceSource.setStatus("mandatory")
_InterfaceTimeout_Type = Integer32
_InterfaceTimeout_Object = MibTableColumn
interfaceTimeout = _InterfaceTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 5, 2, 1, 5),
    _InterfaceTimeout_Type()
)
interfaceTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTimeout.setStatus("mandatory")


class _InterfaceArmed_Type(Integer32):
    """Custom type interfaceArmed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_InterfaceArmed_Type.__name__ = "Integer32"
_InterfaceArmed_Object = MibTableColumn
interfaceArmed = _InterfaceArmed_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 5, 2, 1, 6),
    _InterfaceArmed_Type()
)
interfaceArmed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceArmed.setStatus("mandatory")


class _InterfaceVLANSEnabled_Type(Integer32):
    """Custom type interfaceVLANSEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_InterfaceVLANSEnabled_Type.__name__ = "Integer32"
_InterfaceVLANSEnabled_Object = MibTableColumn
interfaceVLANSEnabled = _InterfaceVLANSEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 5, 2, 1, 7),
    _InterfaceVLANSEnabled_Type()
)
interfaceVLANSEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceVLANSEnabled.setStatus("mandatory")


class _InterfaceMasqueradeAddress_Type(DisplayString):
    """Custom type interfaceMasqueradeAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_InterfaceMasqueradeAddress_Type.__name__ = "DisplayString"
_InterfaceMasqueradeAddress_Object = MibTableColumn
interfaceMasqueradeAddress = _InterfaceMasqueradeAddress_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 5, 2, 1, 8),
    _InterfaceMasqueradeAddress_Type()
)
interfaceMasqueradeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceMasqueradeAddress.setStatus("mandatory")
_InterfaceLastTimeChanged_Type = Integer32
_InterfaceLastTimeChanged_Object = MibTableColumn
interfaceLastTimeChanged = _InterfaceLastTimeChanged_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 5, 2, 1, 9),
    _InterfaceLastTimeChanged_Type()
)
interfaceLastTimeChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceLastTimeChanged.setStatus("mandatory")
_InterfaceSpeed_Type = Integer32
_InterfaceSpeed_Object = MibTableColumn
interfaceSpeed = _InterfaceSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 5, 2, 1, 10),
    _InterfaceSpeed_Type()
)
interfaceSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceSpeed.setStatus("mandatory")


class _InterfaceFullDuplex_Type(Integer32):
    """Custom type interfaceFullDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_InterfaceFullDuplex_Type.__name__ = "Integer32"
_InterfaceFullDuplex_Object = MibTableColumn
interfaceFullDuplex = _InterfaceFullDuplex_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 5, 2, 1, 11),
    _InterfaceFullDuplex_Type()
)
interfaceFullDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceFullDuplex.setStatus("mandatory")
_Ifaddress_ObjectIdentity = ObjectIdentity
ifaddress = _Ifaddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 6)
)


class _IfaddressNumber_Type(Integer32):
    """Custom type ifaddressNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IfaddressNumber_Type.__name__ = "Integer32"
_IfaddressNumber_Object = MibScalar
ifaddressNumber = _IfaddressNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 6, 1),
    _IfaddressNumber_Type()
)
ifaddressNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaddressNumber.setStatus("mandatory")
_IfaddressTable_Object = MibTable
ifaddressTable = _IfaddressTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 6, 2)
)
if mibBuilder.loadTexts:
    ifaddressTable.setStatus("mandatory")
_IfaddressEntry_Object = MibTableRow
ifaddressEntry = _IfaddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 6, 2, 1)
)
ifaddressEntry.setIndexNames(
    (0, "LOAD-BAL-SYSTEM-MIB", "ifaddressIpAddress"),
)
if mibBuilder.loadTexts:
    ifaddressEntry.setStatus("mandatory")
_IfaddressIpAddress_Type = IpAddress
_IfaddressIpAddress_Object = MibTableColumn
ifaddressIpAddress = _IfaddressIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 6, 2, 1, 1),
    _IfaddressIpAddress_Type()
)
ifaddressIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaddressIpAddress.setStatus("mandatory")


class _IfaddressInterfaceName_Type(DisplayString):
    """Custom type ifaddressInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IfaddressInterfaceName_Type.__name__ = "DisplayString"
_IfaddressInterfaceName_Object = MibTableColumn
ifaddressInterfaceName = _IfaddressInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 6, 2, 1, 2),
    _IfaddressInterfaceName_Type()
)
ifaddressInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaddressInterfaceName.setStatus("mandatory")
_IfaddressNetmask_Type = IpAddress
_IfaddressNetmask_Object = MibTableColumn
ifaddressNetmask = _IfaddressNetmask_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 6, 2, 1, 3),
    _IfaddressNetmask_Type()
)
ifaddressNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaddressNetmask.setStatus("mandatory")
_IfaddressBroadcast_Type = IpAddress
_IfaddressBroadcast_Object = MibTableColumn
ifaddressBroadcast = _IfaddressBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 6, 2, 1, 4),
    _IfaddressBroadcast_Type()
)
ifaddressBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaddressBroadcast.setStatus("mandatory")


class _IfaddressType_Type(Integer32):
    """Custom type ifaddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("iptrue", 1),
          ("ipshared", 2))
    )


_IfaddressType_Type.__name__ = "Integer32"
_IfaddressType_Object = MibTableColumn
ifaddressType = _IfaddressType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 6, 2, 1, 5),
    _IfaddressType_Type()
)
ifaddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaddressType.setStatus("mandatory")
_IfaddressUnitId_Type = Integer32
_IfaddressUnitId_Object = MibTableColumn
ifaddressUnitId = _IfaddressUnitId_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 6, 2, 1, 6),
    _IfaddressUnitId_Type()
)
ifaddressUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaddressUnitId.setStatus("mandatory")


class _IfaddressVLANTag_Type(DisplayString):
    """Custom type ifaddressVLANTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_IfaddressVLANTag_Type.__name__ = "DisplayString"
_IfaddressVLANTag_Object = MibTableColumn
ifaddressVLANTag = _IfaddressVLANTag_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 6, 2, 1, 7),
    _IfaddressVLANTag_Type()
)
ifaddressVLANTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaddressVLANTag.setStatus("mandatory")
_Pool_ObjectIdentity = ObjectIdentity
pool = _Pool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7)
)


class _PoolNumber_Type(Integer32):
    """Custom type poolNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PoolNumber_Type.__name__ = "Integer32"
_PoolNumber_Object = MibScalar
poolNumber = _PoolNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 1),
    _PoolNumber_Type()
)
poolNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolNumber.setStatus("mandatory")
_PoolTable_Object = MibTable
poolTable = _PoolTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2)
)
if mibBuilder.loadTexts:
    poolTable.setStatus("mandatory")
_PoolEntry_Object = MibTableRow
poolEntry = _PoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1)
)
poolEntry.setIndexNames(
    (0, "LOAD-BAL-SYSTEM-MIB", "poolName"),
)
if mibBuilder.loadTexts:
    poolEntry.setStatus("mandatory")


class _PoolName_Type(DisplayString):
    """Custom type poolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PoolName_Type.__name__ = "DisplayString"
_PoolName_Object = MibTableColumn
poolName = _PoolName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 1),
    _PoolName_Type()
)
poolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolName.setStatus("mandatory")


class _PoolLBMode_Type(Integer32):
    """Custom type poolLBMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("roundrobin", 1),
          ("ratio", 2),
          ("fastest", 3),
          ("leastConn", 4),
          ("predictive", 5),
          ("observed", 6),
          ("priority", 7),
          ("ratioNodeAddress", 8),
          ("priorityNodeAddress", 9),
          ("leastConnNodeAddress", 10),
          ("globalDefault", 11))
    )


_PoolLBMode_Type.__name__ = "Integer32"
_PoolLBMode_Object = MibTableColumn
poolLBMode = _PoolLBMode_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 2),
    _PoolLBMode_Type()
)
poolLBMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolLBMode.setStatus("mandatory")


class _PoolDependent_Type(Integer32):
    """Custom type poolDependent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_PoolDependent_Type.__name__ = "Integer32"
_PoolDependent_Object = MibTableColumn
poolDependent = _PoolDependent_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 3),
    _PoolDependent_Type()
)
poolDependent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolDependent.setStatus("mandatory")
_PoolMemberQty_Type = Integer32
_PoolMemberQty_Object = MibTableColumn
poolMemberQty = _PoolMemberQty_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 4),
    _PoolMemberQty_Type()
)
poolMemberQty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberQty.setStatus("mandatory")
_PoolBitsin_Type = Counter32
_PoolBitsin_Object = MibTableColumn
poolBitsin = _PoolBitsin_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 5),
    _PoolBitsin_Type()
)
poolBitsin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolBitsin.setStatus("mandatory")
_PoolBitsout_Type = Counter32
_PoolBitsout_Object = MibTableColumn
poolBitsout = _PoolBitsout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 6),
    _PoolBitsout_Type()
)
poolBitsout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolBitsout.setStatus("mandatory")
_PoolBitsinHi32_Type = Counter32
_PoolBitsinHi32_Object = MibTableColumn
poolBitsinHi32 = _PoolBitsinHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 7),
    _PoolBitsinHi32_Type()
)
poolBitsinHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolBitsinHi32.setStatus("mandatory")
_PoolBitsoutHi32_Type = Counter32
_PoolBitsoutHi32_Object = MibTableColumn
poolBitsoutHi32 = _PoolBitsoutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 8),
    _PoolBitsoutHi32_Type()
)
poolBitsoutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolBitsoutHi32.setStatus("mandatory")
_PoolPktsin_Type = Counter32
_PoolPktsin_Object = MibTableColumn
poolPktsin = _PoolPktsin_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 9),
    _PoolPktsin_Type()
)
poolPktsin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolPktsin.setStatus("mandatory")
_PoolPktsout_Type = Counter32
_PoolPktsout_Object = MibTableColumn
poolPktsout = _PoolPktsout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 10),
    _PoolPktsout_Type()
)
poolPktsout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolPktsout.setStatus("mandatory")
_PoolPktsinHi32_Type = Counter32
_PoolPktsinHi32_Object = MibTableColumn
poolPktsinHi32 = _PoolPktsinHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 11),
    _PoolPktsinHi32_Type()
)
poolPktsinHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolPktsinHi32.setStatus("mandatory")
_PoolPktsoutHi32_Type = Counter32
_PoolPktsoutHi32_Object = MibTableColumn
poolPktsoutHi32 = _PoolPktsoutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 12),
    _PoolPktsoutHi32_Type()
)
poolPktsoutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolPktsoutHi32.setStatus("mandatory")


class _PoolMaxConn_Type(Integer32):
    """Custom type poolMaxConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PoolMaxConn_Type.__name__ = "Integer32"
_PoolMaxConn_Object = MibTableColumn
poolMaxConn = _PoolMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 13),
    _PoolMaxConn_Type()
)
poolMaxConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMaxConn.setStatus("mandatory")


class _PoolCurrentConn_Type(Integer32):
    """Custom type poolCurrentConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PoolCurrentConn_Type.__name__ = "Integer32"
_PoolCurrentConn_Object = MibTableColumn
poolCurrentConn = _PoolCurrentConn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 14),
    _PoolCurrentConn_Type()
)
poolCurrentConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolCurrentConn.setStatus("mandatory")
_PoolTotalConn_Type = Counter32
_PoolTotalConn_Object = MibTableColumn
poolTotalConn = _PoolTotalConn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 15),
    _PoolTotalConn_Type()
)
poolTotalConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolTotalConn.setStatus("mandatory")
_PoolMember_ObjectIdentity = ObjectIdentity
poolMember = _PoolMember_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8)
)


class _PoolMemberNumber_Type(Integer32):
    """Custom type poolMemberNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PoolMemberNumber_Type.__name__ = "Integer32"
_PoolMemberNumber_Object = MibScalar
poolMemberNumber = _PoolMemberNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 1),
    _PoolMemberNumber_Type()
)
poolMemberNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberNumber.setStatus("mandatory")
_PoolMemberTable_Object = MibTable
poolMemberTable = _PoolMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2)
)
if mibBuilder.loadTexts:
    poolMemberTable.setStatus("mandatory")
_PoolMemberEntry_Object = MibTableRow
poolMemberEntry = _PoolMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1)
)
poolMemberEntry.setIndexNames(
    (0, "LOAD-BAL-SYSTEM-MIB", "poolMemberPoolName"),
    (0, "LOAD-BAL-SYSTEM-MIB", "poolMemberIpAddress"),
    (0, "LOAD-BAL-SYSTEM-MIB", "poolMemberPort"),
)
if mibBuilder.loadTexts:
    poolMemberEntry.setStatus("mandatory")


class _PoolMemberPoolName_Type(DisplayString):
    """Custom type poolMemberPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PoolMemberPoolName_Type.__name__ = "DisplayString"
_PoolMemberPoolName_Object = MibTableColumn
poolMemberPoolName = _PoolMemberPoolName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1, 1),
    _PoolMemberPoolName_Type()
)
poolMemberPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberPoolName.setStatus("mandatory")
_PoolMemberIpAddress_Type = IpAddress
_PoolMemberIpAddress_Object = MibTableColumn
poolMemberIpAddress = _PoolMemberIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1, 2),
    _PoolMemberIpAddress_Type()
)
poolMemberIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberIpAddress.setStatus("mandatory")


class _PoolMemberPort_Type(Integer32):
    """Custom type poolMemberPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PoolMemberPort_Type.__name__ = "Integer32"
_PoolMemberPort_Object = MibTableColumn
poolMemberPort = _PoolMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1, 3),
    _PoolMemberPort_Type()
)
poolMemberPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberPort.setStatus("mandatory")


class _PoolMemberMaintenance_Type(Integer32):
    """Custom type poolMemberMaintenance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_PoolMemberMaintenance_Type.__name__ = "Integer32"
_PoolMemberMaintenance_Object = MibTableColumn
poolMemberMaintenance = _PoolMemberMaintenance_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1, 4),
    _PoolMemberMaintenance_Type()
)
poolMemberMaintenance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberMaintenance.setStatus("mandatory")
_PoolMemberRatio_Type = Integer32
_PoolMemberRatio_Object = MibTableColumn
poolMemberRatio = _PoolMemberRatio_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1, 5),
    _PoolMemberRatio_Type()
)
poolMemberRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberRatio.setStatus("mandatory")
_PoolMemberPriority_Type = Integer32
_PoolMemberPriority_Object = MibTableColumn
poolMemberPriority = _PoolMemberPriority_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1, 6),
    _PoolMemberPriority_Type()
)
poolMemberPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberPriority.setStatus("mandatory")
_PoolMemberWeight_Type = Integer32
_PoolMemberWeight_Object = MibTableColumn
poolMemberWeight = _PoolMemberWeight_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1, 7),
    _PoolMemberWeight_Type()
)
poolMemberWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberWeight.setStatus("mandatory")
_PoolMemberRipeness_Type = Integer32
_PoolMemberRipeness_Object = MibTableColumn
poolMemberRipeness = _PoolMemberRipeness_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1, 8),
    _PoolMemberRipeness_Type()
)
poolMemberRipeness.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberRipeness.setStatus("mandatory")
_PoolMemberBitsin_Type = Counter32
_PoolMemberBitsin_Object = MibTableColumn
poolMemberBitsin = _PoolMemberBitsin_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1, 9),
    _PoolMemberBitsin_Type()
)
poolMemberBitsin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberBitsin.setStatus("mandatory")
_PoolMemberBitsout_Type = Counter32
_PoolMemberBitsout_Object = MibTableColumn
poolMemberBitsout = _PoolMemberBitsout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1, 10),
    _PoolMemberBitsout_Type()
)
poolMemberBitsout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberBitsout.setStatus("mandatory")
_PoolMemberBitsinHi32_Type = Counter32
_PoolMemberBitsinHi32_Object = MibTableColumn
poolMemberBitsinHi32 = _PoolMemberBitsinHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1, 11),
    _PoolMemberBitsinHi32_Type()
)
poolMemberBitsinHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberBitsinHi32.setStatus("mandatory")
_PoolMemberBitsoutHi32_Type = Counter32
_PoolMemberBitsoutHi32_Object = MibTableColumn
poolMemberBitsoutHi32 = _PoolMemberBitsoutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1, 12),
    _PoolMemberBitsoutHi32_Type()
)
poolMemberBitsoutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberBitsoutHi32.setStatus("mandatory")
_PoolMemberPktsin_Type = Counter32
_PoolMemberPktsin_Object = MibTableColumn
poolMemberPktsin = _PoolMemberPktsin_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1, 13),
    _PoolMemberPktsin_Type()
)
poolMemberPktsin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberPktsin.setStatus("mandatory")
_PoolMemberPktsout_Type = Counter32
_PoolMemberPktsout_Object = MibTableColumn
poolMemberPktsout = _PoolMemberPktsout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1, 14),
    _PoolMemberPktsout_Type()
)
poolMemberPktsout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberPktsout.setStatus("mandatory")
_PoolMemberPktsinHi32_Type = Counter32
_PoolMemberPktsinHi32_Object = MibTableColumn
poolMemberPktsinHi32 = _PoolMemberPktsinHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1, 15),
    _PoolMemberPktsinHi32_Type()
)
poolMemberPktsinHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberPktsinHi32.setStatus("mandatory")
_PoolMemberPktsoutHi32_Type = Counter32
_PoolMemberPktsoutHi32_Object = MibTableColumn
poolMemberPktsoutHi32 = _PoolMemberPktsoutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1, 16),
    _PoolMemberPktsoutHi32_Type()
)
poolMemberPktsoutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberPktsoutHi32.setStatus("mandatory")


class _PoolMemberConnLimit_Type(Integer32):
    """Custom type poolMemberConnLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PoolMemberConnLimit_Type.__name__ = "Integer32"
_PoolMemberConnLimit_Object = MibTableColumn
poolMemberConnLimit = _PoolMemberConnLimit_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1, 17),
    _PoolMemberConnLimit_Type()
)
poolMemberConnLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberConnLimit.setStatus("mandatory")


class _PoolMemberMaxConn_Type(Integer32):
    """Custom type poolMemberMaxConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PoolMemberMaxConn_Type.__name__ = "Integer32"
_PoolMemberMaxConn_Object = MibTableColumn
poolMemberMaxConn = _PoolMemberMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1, 18),
    _PoolMemberMaxConn_Type()
)
poolMemberMaxConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberMaxConn.setStatus("mandatory")


class _PoolMemberCurrentConn_Type(Integer32):
    """Custom type poolMemberCurrentConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PoolMemberCurrentConn_Type.__name__ = "Integer32"
_PoolMemberCurrentConn_Object = MibTableColumn
poolMemberCurrentConn = _PoolMemberCurrentConn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1, 19),
    _PoolMemberCurrentConn_Type()
)
poolMemberCurrentConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberCurrentConn.setStatus("mandatory")
_PoolMemberTotalConn_Type = Counter32
_PoolMemberTotalConn_Object = MibTableColumn
poolMemberTotalConn = _PoolMemberTotalConn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1, 20),
    _PoolMemberTotalConn_Type()
)
poolMemberTotalConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberTotalConn.setStatus("mandatory")
_Uptime_Type = TimeTicks
_Uptime_Object = MibScalar
uptime = _Uptime_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 50),
    _Uptime_Type()
)
uptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uptime.setStatus("mandatory")
_Contot_Type = Counter32
_Contot_Object = MibScalar
contot = _Contot_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 51),
    _Contot_Type()
)
contot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contot.setStatus("mandatory")
_Concur_Type = Integer32
_Concur_Object = MibScalar
concur = _Concur_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 52),
    _Concur_Type()
)
concur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concur.setStatus("mandatory")
_Conmax_Type = Integer32
_Conmax_Object = MibScalar
conmax = _Conmax_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 53),
    _Conmax_Type()
)
conmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    conmax.setStatus("mandatory")
_Pktsin_Type = Counter32
_Pktsin_Object = MibScalar
pktsin = _Pktsin_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 54),
    _Pktsin_Type()
)
pktsin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktsin.setStatus("mandatory")
_Pktsout_Type = Counter32
_Pktsout_Object = MibScalar
pktsout = _Pktsout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 55),
    _Pktsout_Type()
)
pktsout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktsout.setStatus("mandatory")
_Bitsin_Type = Counter32
_Bitsin_Object = MibScalar
bitsin = _Bitsin_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 56),
    _Bitsin_Type()
)
bitsin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitsin.setStatus("mandatory")
_Bitsout_Type = Counter32
_Bitsout_Object = MibScalar
bitsout = _Bitsout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 57),
    _Bitsout_Type()
)
bitsout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitsout.setStatus("mandatory")
_Portdeny_Type = Counter32
_Portdeny_Object = MibScalar
portdeny = _Portdeny_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 58),
    _Portdeny_Type()
)
portdeny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portdeny.setStatus("mandatory")
_Droppedin_Type = Counter32
_Droppedin_Object = MibScalar
droppedin = _Droppedin_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 59),
    _Droppedin_Type()
)
droppedin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    droppedin.setStatus("mandatory")
_Droppedout_Type = Counter32
_Droppedout_Object = MibScalar
droppedout = _Droppedout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 60),
    _Droppedout_Type()
)
droppedout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    droppedout.setStatus("mandatory")


class _Active_Type(Integer32):
    """Custom type active based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standby", 1),
          ("active", 2))
    )


_Active_Type.__name__ = "Integer32"
_Active_Object = MibScalar
active = _Active_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 61),
    _Active_Type()
)
active.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    active.setStatus("mandatory")


class _Mirrorenabled_Type(Integer32):
    """Custom type mirrorenabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_Mirrorenabled_Type.__name__ = "Integer32"
_Mirrorenabled_Object = MibScalar
mirrorenabled = _Mirrorenabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 62),
    _Mirrorenabled_Type()
)
mirrorenabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mirrorenabled.setStatus("mandatory")


class _Resetcounters_Type(Integer32):
    """Custom type resetcounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("unreset", 2))
    )


_Resetcounters_Type.__name__ = "Integer32"
_Resetcounters_Object = MibScalar
resetcounters = _Resetcounters_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 63),
    _Resetcounters_Type()
)
resetcounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetcounters.setStatus("mandatory")
_PktsinHi32_Type = Counter32
_PktsinHi32_Object = MibScalar
pktsinHi32 = _PktsinHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 64),
    _PktsinHi32_Type()
)
pktsinHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktsinHi32.setStatus("mandatory")
_PktsoutHi32_Type = Counter32
_PktsoutHi32_Object = MibScalar
pktsoutHi32 = _PktsoutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 65),
    _PktsoutHi32_Type()
)
pktsoutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktsoutHi32.setStatus("mandatory")
_BitsinHi32_Type = Counter32
_BitsinHi32_Object = MibScalar
bitsinHi32 = _BitsinHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 66),
    _BitsinHi32_Type()
)
bitsinHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitsinHi32.setStatus("mandatory")
_BitsoutHi32_Type = Counter32
_BitsoutHi32_Object = MibScalar
bitsoutHi32 = _BitsoutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 67),
    _BitsoutHi32_Type()
)
bitsoutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitsoutHi32.setStatus("mandatory")
_NodePing_Type = Integer32
_NodePing_Object = MibScalar
nodePing = _NodePing_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 68),
    _NodePing_Type()
)
nodePing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodePing.setStatus("mandatory")
_NodeTimeout_Type = Integer32
_NodeTimeout_Object = MibScalar
nodeTimeout = _NodeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 69),
    _NodeTimeout_Type()
)
nodeTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeTimeout.setStatus("mandatory")


class _LoadbalMode_Type(Integer32):
    """Custom type loadbalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("roundrobin", 1),
          ("ratio", 2),
          ("fastest", 3),
          ("leastConn", 4),
          ("predictive", 5),
          ("observed", 6),
          ("priority", 7),
          ("ratioNodeAddress", 8),
          ("priorityNodeAddress", 9),
          ("leastConnNodeAddress", 10))
    )


_LoadbalMode_Type.__name__ = "Integer32"
_LoadbalMode_Object = MibScalar
loadbalMode = _LoadbalMode_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 70),
    _LoadbalMode_Type()
)
loadbalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadbalMode.setStatus("mandatory")


class _WatchDogArmed_Type(Integer32):
    """Custom type watchDogArmed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("armed", 1),
          ("disarmed", 2))
    )


_WatchDogArmed_Type.__name__ = "Integer32"
_WatchDogArmed_Object = MibScalar
watchDogArmed = _WatchDogArmed_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 71),
    _WatchDogArmed_Type()
)
watchDogArmed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    watchDogArmed.setStatus("mandatory")
_SnatConnLimit_Type = Integer32
_SnatConnLimit_Object = MibScalar
snatConnLimit = _SnatConnLimit_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 72),
    _SnatConnLimit_Type()
)
snatConnLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatConnLimit.setStatus("mandatory")
_SnatTCPIdleTimeout_Type = Integer32
_SnatTCPIdleTimeout_Object = MibScalar
snatTCPIdleTimeout = _SnatTCPIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 73),
    _SnatTCPIdleTimeout_Type()
)
snatTCPIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatTCPIdleTimeout.setStatus("mandatory")
_SnatUDPIdleTimeout_Type = Integer32
_SnatUDPIdleTimeout_Object = MibScalar
snatUDPIdleTimeout = _SnatUDPIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 74),
    _SnatUDPIdleTimeout_Type()
)
snatUDPIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatUDPIdleTimeout.setStatus("mandatory")


class _GatewayFailsafe_Type(Integer32):
    """Custom type gatewayFailsafe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_GatewayFailsafe_Type.__name__ = "Integer32"
_GatewayFailsafe_Object = MibScalar
gatewayFailsafe = _GatewayFailsafe_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 75),
    _GatewayFailsafe_Type()
)
gatewayFailsafe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gatewayFailsafe.setStatus("mandatory")


class _UnitId_Type(DisplayString):
    """Custom type unitId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UnitId_Type.__name__ = "DisplayString"
_UnitId_Object = MibScalar
unitId = _UnitId_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 76),
    _UnitId_Type()
)
unitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitId.setStatus("mandatory")
_MemoryUsed_Type = Integer32
_MemoryUsed_Object = MibScalar
memoryUsed = _MemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 77),
    _MemoryUsed_Type()
)
memoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryUsed.setStatus("mandatory")


class _MemoryTotal_Type(DisplayString):
    """Custom type memoryTotal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MemoryTotal_Type.__name__ = "DisplayString"
_MemoryTotal_Object = MibScalar
memoryTotal = _MemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 78),
    _MemoryTotal_Type()
)
memoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryTotal.setStatus("mandatory")
_Vaddress_ObjectIdentity = ObjectIdentity
vaddress = _Vaddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 100)
)
_VaddressNumber_Type = Integer32
_VaddressNumber_Object = MibScalar
vaddressNumber = _VaddressNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 100, 1),
    _VaddressNumber_Type()
)
vaddressNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaddressNumber.setStatus("mandatory")
_VaddressTable_Object = MibTable
vaddressTable = _VaddressTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 100, 2)
)
if mibBuilder.loadTexts:
    vaddressTable.setStatus("mandatory")
_VaddressEntry_Object = MibTableRow
vaddressEntry = _VaddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 100, 2, 1)
)
vaddressEntry.setIndexNames(
    (0, "LOAD-BAL-SYSTEM-MIB", "vaddressIndex"),
)
if mibBuilder.loadTexts:
    vaddressEntry.setStatus("mandatory")


class _VaddressIndex_Type(Integer32):
    """Custom type vaddressIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VaddressIndex_Type.__name__ = "Integer32"
_VaddressIndex_Object = MibTableColumn
vaddressIndex = _VaddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 100, 2, 1, 1),
    _VaddressIndex_Type()
)
vaddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaddressIndex.setStatus("mandatory")


class _VaddressDescr_Type(DisplayString):
    """Custom type vaddressDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VaddressDescr_Type.__name__ = "DisplayString"
_VaddressDescr_Object = MibTableColumn
vaddressDescr = _VaddressDescr_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 100, 2, 1, 2),
    _VaddressDescr_Type()
)
vaddressDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaddressDescr.setStatus("mandatory")
_VaddressIpAddr_Type = IpAddress
_VaddressIpAddr_Object = MibTableColumn
vaddressIpAddr = _VaddressIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 100, 2, 1, 3),
    _VaddressIpAddr_Type()
)
vaddressIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaddressIpAddr.setStatus("mandatory")
_VaddressPktsin_Type = Counter32
_VaddressPktsin_Object = MibTableColumn
vaddressPktsin = _VaddressPktsin_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 100, 2, 1, 4),
    _VaddressPktsin_Type()
)
vaddressPktsin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaddressPktsin.setStatus("mandatory")
_VaddressPktsout_Type = Counter32
_VaddressPktsout_Object = MibTableColumn
vaddressPktsout = _VaddressPktsout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 100, 2, 1, 5),
    _VaddressPktsout_Type()
)
vaddressPktsout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaddressPktsout.setStatus("mandatory")
_VaddressBitsin_Type = Counter32
_VaddressBitsin_Object = MibTableColumn
vaddressBitsin = _VaddressBitsin_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 100, 2, 1, 6),
    _VaddressBitsin_Type()
)
vaddressBitsin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaddressBitsin.setStatus("mandatory")
_VaddressBitsout_Type = Counter32
_VaddressBitsout_Object = MibTableColumn
vaddressBitsout = _VaddressBitsout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 100, 2, 1, 7),
    _VaddressBitsout_Type()
)
vaddressBitsout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaddressBitsout.setStatus("mandatory")
_VaddressConcur_Type = Integer32
_VaddressConcur_Object = MibTableColumn
vaddressConcur = _VaddressConcur_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 100, 2, 1, 8),
    _VaddressConcur_Type()
)
vaddressConcur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaddressConcur.setStatus("mandatory")
_VaddressConmax_Type = Integer32
_VaddressConmax_Object = MibTableColumn
vaddressConmax = _VaddressConmax_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 100, 2, 1, 9),
    _VaddressConmax_Type()
)
vaddressConmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaddressConmax.setStatus("mandatory")
_VaddressConlimit_Type = Integer32
_VaddressConlimit_Object = MibTableColumn
vaddressConlimit = _VaddressConlimit_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 100, 2, 1, 10),
    _VaddressConlimit_Type()
)
vaddressConlimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaddressConlimit.setStatus("mandatory")
_VaddressContot_Type = Counter32
_VaddressContot_Object = MibTableColumn
vaddressContot = _VaddressContot_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 100, 2, 1, 11),
    _VaddressContot_Type()
)
vaddressContot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaddressContot.setStatus("mandatory")


class _VaddressStatus_Type(Integer32):
    """Custom type vaddressStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("maintainance", 2))
    )


_VaddressStatus_Type.__name__ = "Integer32"
_VaddressStatus_Object = MibTableColumn
vaddressStatus = _VaddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 100, 2, 1, 12),
    _VaddressStatus_Type()
)
vaddressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaddressStatus.setStatus("mandatory")
_VaddressPktsinHi32_Type = Counter32
_VaddressPktsinHi32_Object = MibTableColumn
vaddressPktsinHi32 = _VaddressPktsinHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 100, 2, 1, 13),
    _VaddressPktsinHi32_Type()
)
vaddressPktsinHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaddressPktsinHi32.setStatus("mandatory")
_VaddressPktsoutHi32_Type = Counter32
_VaddressPktsoutHi32_Object = MibTableColumn
vaddressPktsoutHi32 = _VaddressPktsoutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 100, 2, 1, 14),
    _VaddressPktsoutHi32_Type()
)
vaddressPktsoutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaddressPktsoutHi32.setStatus("mandatory")
_VaddressBitsinHi32_Type = Counter32
_VaddressBitsinHi32_Object = MibTableColumn
vaddressBitsinHi32 = _VaddressBitsinHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 100, 2, 1, 15),
    _VaddressBitsinHi32_Type()
)
vaddressBitsinHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaddressBitsinHi32.setStatus("mandatory")
_VaddressBitsoutHi32_Type = Counter32
_VaddressBitsoutHi32_Object = MibTableColumn
vaddressBitsoutHi32 = _VaddressBitsoutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 100, 2, 1, 16),
    _VaddressBitsoutHi32_Type()
)
vaddressBitsoutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaddressBitsoutHi32.setStatus("mandatory")
_Ndaddr_ObjectIdentity = ObjectIdentity
ndaddr = _Ndaddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101)
)
_NdaddrNumber_Type = Integer32
_NdaddrNumber_Object = MibScalar
ndaddrNumber = _NdaddrNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 1),
    _NdaddrNumber_Type()
)
ndaddrNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrNumber.setStatus("mandatory")
_NdaddrTable_Object = MibTable
ndaddrTable = _NdaddrTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2)
)
if mibBuilder.loadTexts:
    ndaddrTable.setStatus("mandatory")
_NdaddrEntry_Object = MibTableRow
ndaddrEntry = _NdaddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1)
)
ndaddrEntry.setIndexNames(
    (0, "LOAD-BAL-SYSTEM-MIB", "ndaddrIndex"),
)
if mibBuilder.loadTexts:
    ndaddrEntry.setStatus("mandatory")


class _NdaddrIndex_Type(Integer32):
    """Custom type ndaddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NdaddrIndex_Type.__name__ = "Integer32"
_NdaddrIndex_Object = MibTableColumn
ndaddrIndex = _NdaddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 1),
    _NdaddrIndex_Type()
)
ndaddrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrIndex.setStatus("mandatory")


class _NdaddrDescr_Type(DisplayString):
    """Custom type ndaddrDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NdaddrDescr_Type.__name__ = "DisplayString"
_NdaddrDescr_Object = MibTableColumn
ndaddrDescr = _NdaddrDescr_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 2),
    _NdaddrDescr_Type()
)
ndaddrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrDescr.setStatus("mandatory")
_NdaddrIpAddr_Type = IpAddress
_NdaddrIpAddr_Object = MibTableColumn
ndaddrIpAddr = _NdaddrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 3),
    _NdaddrIpAddr_Type()
)
ndaddrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrIpAddr.setStatus("mandatory")
_NdaddrPktsin_Type = Counter32
_NdaddrPktsin_Object = MibTableColumn
ndaddrPktsin = _NdaddrPktsin_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 4),
    _NdaddrPktsin_Type()
)
ndaddrPktsin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrPktsin.setStatus("mandatory")
_NdaddrPktsout_Type = Counter32
_NdaddrPktsout_Object = MibTableColumn
ndaddrPktsout = _NdaddrPktsout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 5),
    _NdaddrPktsout_Type()
)
ndaddrPktsout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrPktsout.setStatus("mandatory")
_NdaddrBitsin_Type = Counter32
_NdaddrBitsin_Object = MibTableColumn
ndaddrBitsin = _NdaddrBitsin_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 6),
    _NdaddrBitsin_Type()
)
ndaddrBitsin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrBitsin.setStatus("mandatory")
_NdaddrBitsout_Type = Counter32
_NdaddrBitsout_Object = MibTableColumn
ndaddrBitsout = _NdaddrBitsout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 7),
    _NdaddrBitsout_Type()
)
ndaddrBitsout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrBitsout.setStatus("mandatory")
_NdaddrConcur_Type = Integer32
_NdaddrConcur_Object = MibTableColumn
ndaddrConcur = _NdaddrConcur_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 8),
    _NdaddrConcur_Type()
)
ndaddrConcur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrConcur.setStatus("mandatory")
_NdaddrConmax_Type = Integer32
_NdaddrConmax_Object = MibTableColumn
ndaddrConmax = _NdaddrConmax_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 9),
    _NdaddrConmax_Type()
)
ndaddrConmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrConmax.setStatus("mandatory")
_NdaddrConlimit_Type = Integer32
_NdaddrConlimit_Object = MibTableColumn
ndaddrConlimit = _NdaddrConlimit_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 10),
    _NdaddrConlimit_Type()
)
ndaddrConlimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrConlimit.setStatus("mandatory")
_NdaddrContot_Type = Counter32
_NdaddrContot_Object = MibTableColumn
ndaddrContot = _NdaddrContot_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 11),
    _NdaddrContot_Type()
)
ndaddrContot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrContot.setStatus("mandatory")


class _NdaddrStatus_Type(Integer32):
    """Custom type ndaddrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("invalid", 3),
          ("valid", 4),
          ("unchecked", 6),
          ("unknown", 7))
    )


_NdaddrStatus_Type.__name__ = "Integer32"
_NdaddrStatus_Object = MibTableColumn
ndaddrStatus = _NdaddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 12),
    _NdaddrStatus_Type()
)
ndaddrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrStatus.setStatus("mandatory")
_NdaddrPktsinHi32_Type = Counter32
_NdaddrPktsinHi32_Object = MibTableColumn
ndaddrPktsinHi32 = _NdaddrPktsinHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 13),
    _NdaddrPktsinHi32_Type()
)
ndaddrPktsinHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrPktsinHi32.setStatus("mandatory")
_NdaddrPktsoutHi32_Type = Counter32
_NdaddrPktsoutHi32_Object = MibTableColumn
ndaddrPktsoutHi32 = _NdaddrPktsoutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 14),
    _NdaddrPktsoutHi32_Type()
)
ndaddrPktsoutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrPktsoutHi32.setStatus("mandatory")
_NdaddrBitsinHi32_Type = Counter32
_NdaddrBitsinHi32_Object = MibTableColumn
ndaddrBitsinHi32 = _NdaddrBitsinHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 15),
    _NdaddrBitsinHi32_Type()
)
ndaddrBitsinHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrBitsinHi32.setStatus("mandatory")
_NdaddrBitsoutHi32_Type = Counter32
_NdaddrBitsoutHi32_Object = MibTableColumn
ndaddrBitsoutHi32 = _NdaddrBitsoutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 16),
    _NdaddrBitsoutHi32_Type()
)
ndaddrBitsoutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrBitsoutHi32.setStatus("mandatory")


class _NdaddrMaintenance_Type(Integer32):
    """Custom type ndaddrMaintenance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_NdaddrMaintenance_Type.__name__ = "Integer32"
_NdaddrMaintenance_Object = MibTableColumn
ndaddrMaintenance = _NdaddrMaintenance_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 17),
    _NdaddrMaintenance_Type()
)
ndaddrMaintenance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrMaintenance.setStatus("mandatory")
_Nat_ObjectIdentity = ObjectIdentity
nat = _Nat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102)
)
_NatNumber_Type = Integer32
_NatNumber_Object = MibScalar
natNumber = _NatNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102, 1),
    _NatNumber_Type()
)
natNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natNumber.setStatus("mandatory")
_NatTable_Object = MibTable
natTable = _NatTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102, 2)
)
if mibBuilder.loadTexts:
    natTable.setStatus("mandatory")
_NatEntry_Object = MibTableRow
natEntry = _NatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102, 2, 1)
)
natEntry.setIndexNames(
    (0, "LOAD-BAL-SYSTEM-MIB", "natIndex"),
)
if mibBuilder.loadTexts:
    natEntry.setStatus("mandatory")


class _NatIndex_Type(Integer32):
    """Custom type natIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NatIndex_Type.__name__ = "Integer32"
_NatIndex_Object = MibTableColumn
natIndex = _NatIndex_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102, 2, 1, 1),
    _NatIndex_Type()
)
natIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natIndex.setStatus("mandatory")


class _NatDescr_Type(DisplayString):
    """Custom type natDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NatDescr_Type.__name__ = "DisplayString"
_NatDescr_Object = MibTableColumn
natDescr = _NatDescr_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102, 2, 1, 2),
    _NatDescr_Type()
)
natDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natDescr.setStatus("mandatory")
_NatIpAddrFR_Type = IpAddress
_NatIpAddrFR_Object = MibTableColumn
natIpAddrFR = _NatIpAddrFR_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102, 2, 1, 3),
    _NatIpAddrFR_Type()
)
natIpAddrFR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natIpAddrFR.setStatus("mandatory")
_NatIpAddrTO_Type = IpAddress
_NatIpAddrTO_Object = MibTableColumn
natIpAddrTO = _NatIpAddrTO_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102, 2, 1, 4),
    _NatIpAddrTO_Type()
)
natIpAddrTO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natIpAddrTO.setStatus("mandatory")
_NatPktsin_Type = Counter32
_NatPktsin_Object = MibTableColumn
natPktsin = _NatPktsin_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102, 2, 1, 5),
    _NatPktsin_Type()
)
natPktsin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natPktsin.setStatus("mandatory")
_NatPktsout_Type = Counter32
_NatPktsout_Object = MibTableColumn
natPktsout = _NatPktsout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102, 2, 1, 6),
    _NatPktsout_Type()
)
natPktsout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natPktsout.setStatus("mandatory")
_NatBitsin_Type = Counter32
_NatBitsin_Object = MibTableColumn
natBitsin = _NatBitsin_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102, 2, 1, 7),
    _NatBitsin_Type()
)
natBitsin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natBitsin.setStatus("mandatory")
_NatBitsout_Type = Counter32
_NatBitsout_Object = MibTableColumn
natBitsout = _NatBitsout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102, 2, 1, 8),
    _NatBitsout_Type()
)
natBitsout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natBitsout.setStatus("mandatory")
_NatPktsinHi32_Type = Counter32
_NatPktsinHi32_Object = MibTableColumn
natPktsinHi32 = _NatPktsinHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102, 2, 1, 9),
    _NatPktsinHi32_Type()
)
natPktsinHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natPktsinHi32.setStatus("mandatory")
_NatPktsoutHi32_Type = Counter32
_NatPktsoutHi32_Object = MibTableColumn
natPktsoutHi32 = _NatPktsoutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102, 2, 1, 10),
    _NatPktsoutHi32_Type()
)
natPktsoutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natPktsoutHi32.setStatus("mandatory")
_NatBitsinHi32_Type = Counter32
_NatBitsinHi32_Object = MibTableColumn
natBitsinHi32 = _NatBitsinHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102, 2, 1, 11),
    _NatBitsinHi32_Type()
)
natBitsinHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natBitsinHi32.setStatus("mandatory")
_NatBitsoutHi32_Type = Counter32
_NatBitsoutHi32_Object = MibTableColumn
natBitsoutHi32 = _NatBitsoutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102, 2, 1, 12),
    _NatBitsoutHi32_Type()
)
natBitsoutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natBitsoutHi32.setStatus("mandatory")
_NatOutsideNetmask_Type = IpAddress
_NatOutsideNetmask_Object = MibTableColumn
natOutsideNetmask = _NatOutsideNetmask_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102, 2, 1, 13),
    _NatOutsideNetmask_Type()
)
natOutsideNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natOutsideNetmask.setStatus("mandatory")
_NatOutsideBroadcast_Type = IpAddress
_NatOutsideBroadcast_Object = MibTableColumn
natOutsideBroadcast = _NatOutsideBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102, 2, 1, 14),
    _NatOutsideBroadcast_Type()
)
natOutsideBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natOutsideBroadcast.setStatus("mandatory")


class _NatInterface_Type(DisplayString):
    """Custom type natInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NatInterface_Type.__name__ = "DisplayString"
_NatInterface_Object = MibTableColumn
natInterface = _NatInterface_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102, 2, 1, 15),
    _NatInterface_Type()
)
natInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natInterface.setStatus("mandatory")
_NatUnitId_Type = Integer32
_NatUnitId_Object = MibTableColumn
natUnitId = _NatUnitId_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102, 2, 1, 16),
    _NatUnitId_Type()
)
natUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natUnitId.setStatus("mandatory")
_Vport_ObjectIdentity = ObjectIdentity
vport = _Vport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103)
)
_VportNumber_Type = Integer32
_VportNumber_Object = MibScalar
vportNumber = _VportNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 1),
    _VportNumber_Type()
)
vportNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportNumber.setStatus("mandatory")
_VportTable_Object = MibTable
vportTable = _VportTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2)
)
if mibBuilder.loadTexts:
    vportTable.setStatus("mandatory")
_VportEntry_Object = MibTableRow
vportEntry = _VportEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2, 1)
)
vportEntry.setIndexNames(
    (0, "LOAD-BAL-SYSTEM-MIB", "vportIndex"),
)
if mibBuilder.loadTexts:
    vportEntry.setStatus("mandatory")


class _VportIndex_Type(Integer32):
    """Custom type vportIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VportIndex_Type.__name__ = "Integer32"
_VportIndex_Object = MibTableColumn
vportIndex = _VportIndex_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2, 1, 1),
    _VportIndex_Type()
)
vportIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportIndex.setStatus("mandatory")
_VportPort_Type = Integer32
_VportPort_Object = MibTableColumn
vportPort = _VportPort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2, 1, 2),
    _VportPort_Type()
)
vportPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportPort.setStatus("mandatory")


class _VportDescr_Type(DisplayString):
    """Custom type vportDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VportDescr_Type.__name__ = "DisplayString"
_VportDescr_Object = MibTableColumn
vportDescr = _VportDescr_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2, 1, 3),
    _VportDescr_Type()
)
vportDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportDescr.setStatus("mandatory")
_VportPktsin_Type = Counter32
_VportPktsin_Object = MibTableColumn
vportPktsin = _VportPktsin_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2, 1, 4),
    _VportPktsin_Type()
)
vportPktsin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportPktsin.setStatus("mandatory")
_VportPktsout_Type = Counter32
_VportPktsout_Object = MibTableColumn
vportPktsout = _VportPktsout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2, 1, 5),
    _VportPktsout_Type()
)
vportPktsout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportPktsout.setStatus("mandatory")
_VportBitsin_Type = Counter32
_VportBitsin_Object = MibTableColumn
vportBitsin = _VportBitsin_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2, 1, 6),
    _VportBitsin_Type()
)
vportBitsin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportBitsin.setStatus("mandatory")
_VportBitsout_Type = Counter32
_VportBitsout_Object = MibTableColumn
vportBitsout = _VportBitsout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2, 1, 7),
    _VportBitsout_Type()
)
vportBitsout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportBitsout.setStatus("mandatory")
_VportConcur_Type = Integer32
_VportConcur_Object = MibTableColumn
vportConcur = _VportConcur_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2, 1, 8),
    _VportConcur_Type()
)
vportConcur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportConcur.setStatus("mandatory")
_VportConmax_Type = Integer32
_VportConmax_Object = MibTableColumn
vportConmax = _VportConmax_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2, 1, 9),
    _VportConmax_Type()
)
vportConmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportConmax.setStatus("mandatory")
_VportConlimit_Type = Integer32
_VportConlimit_Object = MibTableColumn
vportConlimit = _VportConlimit_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2, 1, 10),
    _VportConlimit_Type()
)
vportConlimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportConlimit.setStatus("mandatory")
_VportContot_Type = Counter32
_VportContot_Object = MibTableColumn
vportContot = _VportContot_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2, 1, 11),
    _VportContot_Type()
)
vportContot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportContot.setStatus("mandatory")
_VportReaped_Type = Counter32
_VportReaped_Object = MibTableColumn
vportReaped = _VportReaped_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2, 1, 12),
    _VportReaped_Type()
)
vportReaped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportReaped.setStatus("mandatory")
_VportPktsinHi32_Type = Counter32
_VportPktsinHi32_Object = MibTableColumn
vportPktsinHi32 = _VportPktsinHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2, 1, 13),
    _VportPktsinHi32_Type()
)
vportPktsinHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportPktsinHi32.setStatus("mandatory")
_VportPktsoutHi32_Type = Counter32
_VportPktsoutHi32_Object = MibTableColumn
vportPktsoutHi32 = _VportPktsoutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2, 1, 14),
    _VportPktsoutHi32_Type()
)
vportPktsoutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportPktsoutHi32.setStatus("mandatory")
_VportBitsinHi32_Type = Counter32
_VportBitsinHi32_Object = MibTableColumn
vportBitsinHi32 = _VportBitsinHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2, 1, 15),
    _VportBitsinHi32_Type()
)
vportBitsinHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportBitsinHi32.setStatus("mandatory")
_VportBitsoutHi32_Type = Counter32
_VportBitsoutHi32_Object = MibTableColumn
vportBitsoutHi32 = _VportBitsoutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2, 1, 16),
    _VportBitsoutHi32_Type()
)
vportBitsoutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportBitsoutHi32.setStatus("mandatory")


class _VportAllowed_Type(Integer32):
    """Custom type vportAllowed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 2))
    )


_VportAllowed_Type.__name__ = "Integer32"
_VportAllowed_Object = MibTableColumn
vportAllowed = _VportAllowed_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2, 1, 17),
    _VportAllowed_Type()
)
vportAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportAllowed.setStatus("mandatory")
_VportTCPpersistance_Type = Integer32
_VportTCPpersistance_Object = MibTableColumn
vportTCPpersistance = _VportTCPpersistance_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2, 1, 18),
    _VportTCPpersistance_Type()
)
vportTCPpersistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportTCPpersistance.setStatus("mandatory")
_VportUDPpersistance_Type = Integer32
_VportUDPpersistance_Object = MibTableColumn
vportUDPpersistance = _VportUDPpersistance_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2, 1, 19),
    _VportUDPpersistance_Type()
)
vportUDPpersistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportUDPpersistance.setStatus("mandatory")
_Member_ObjectIdentity = ObjectIdentity
member = _Member_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 104)
)
_MemberTable_Object = MibTable
memberTable = _MemberTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 104, 2)
)
if mibBuilder.loadTexts:
    memberTable.setStatus("mandatory")
_MemberEntry_Object = MibTableRow
memberEntry = _MemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 104, 2, 1)
)
memberEntry.setIndexNames(
    (0, "LOAD-BAL-SYSTEM-MIB", "memberVirtualAddress"),
    (0, "LOAD-BAL-SYSTEM-MIB", "memberVirtualAddressPort"),
    (0, "LOAD-BAL-SYSTEM-MIB", "memberOrdinal"),
)
if mibBuilder.loadTexts:
    memberEntry.setStatus("mandatory")
_MemberVirtualAddress_Type = IpAddress
_MemberVirtualAddress_Object = MibTableColumn
memberVirtualAddress = _MemberVirtualAddress_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 104, 2, 1, 1),
    _MemberVirtualAddress_Type()
)
memberVirtualAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberVirtualAddress.setStatus("mandatory")


class _MemberVirtualAddressPort_Type(Integer32):
    """Custom type memberVirtualAddressPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MemberVirtualAddressPort_Type.__name__ = "Integer32"
_MemberVirtualAddressPort_Object = MibTableColumn
memberVirtualAddressPort = _MemberVirtualAddressPort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 104, 2, 1, 2),
    _MemberVirtualAddressPort_Type()
)
memberVirtualAddressPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberVirtualAddressPort.setStatus("mandatory")


class _MemberOrdinal_Type(Integer32):
    """Custom type memberOrdinal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MemberOrdinal_Type.__name__ = "Integer32"
_MemberOrdinal_Object = MibTableColumn
memberOrdinal = _MemberOrdinal_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 104, 2, 1, 3),
    _MemberOrdinal_Type()
)
memberOrdinal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberOrdinal.setStatus("mandatory")
_MemberAddress_Type = IpAddress
_MemberAddress_Object = MibTableColumn
memberAddress = _MemberAddress_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 104, 2, 1, 4),
    _MemberAddress_Type()
)
memberAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberAddress.setStatus("mandatory")
_MemberPort_Type = Integer32
_MemberPort_Object = MibTableColumn
memberPort = _MemberPort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 104, 2, 1, 5),
    _MemberPort_Type()
)
memberPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberPort.setStatus("mandatory")


class _MemberStatus_Type(Integer32):
    """Custom type memberStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("invalid", 3),
          ("maintainance", 4),
          ("unchecked", 5),
          ("unknown", 6))
    )


_MemberStatus_Type.__name__ = "Integer32"
_MemberStatus_Object = MibTableColumn
memberStatus = _MemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 104, 2, 1, 6),
    _MemberStatus_Type()
)
memberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberStatus.setStatus("mandatory")
_MemberPktsin_Type = Counter32
_MemberPktsin_Object = MibTableColumn
memberPktsin = _MemberPktsin_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 104, 2, 1, 7),
    _MemberPktsin_Type()
)
memberPktsin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberPktsin.setStatus("mandatory")
_MemberPktsout_Type = Counter32
_MemberPktsout_Object = MibTableColumn
memberPktsout = _MemberPktsout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 104, 2, 1, 8),
    _MemberPktsout_Type()
)
memberPktsout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberPktsout.setStatus("mandatory")
_MemberBitsin_Type = Counter32
_MemberBitsin_Object = MibTableColumn
memberBitsin = _MemberBitsin_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 104, 2, 1, 9),
    _MemberBitsin_Type()
)
memberBitsin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberBitsin.setStatus("mandatory")
_MemberBitsout_Type = Counter32
_MemberBitsout_Object = MibTableColumn
memberBitsout = _MemberBitsout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 104, 2, 1, 10),
    _MemberBitsout_Type()
)
memberBitsout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberBitsout.setStatus("mandatory")
_MemberConcur_Type = Integer32
_MemberConcur_Object = MibTableColumn
memberConcur = _MemberConcur_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 104, 2, 1, 11),
    _MemberConcur_Type()
)
memberConcur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberConcur.setStatus("mandatory")
_MemberConmax_Type = Integer32
_MemberConmax_Object = MibTableColumn
memberConmax = _MemberConmax_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 104, 2, 1, 12),
    _MemberConmax_Type()
)
memberConmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberConmax.setStatus("mandatory")
_MemberConlimit_Type = Integer32
_MemberConlimit_Object = MibTableColumn
memberConlimit = _MemberConlimit_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 104, 2, 1, 13),
    _MemberConlimit_Type()
)
memberConlimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberConlimit.setStatus("mandatory")
_MemberContot_Type = Counter32
_MemberContot_Object = MibTableColumn
memberContot = _MemberContot_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 104, 2, 1, 14),
    _MemberContot_Type()
)
memberContot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberContot.setStatus("mandatory")
_MemberPktsinHi32_Type = Counter32
_MemberPktsinHi32_Object = MibTableColumn
memberPktsinHi32 = _MemberPktsinHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 104, 2, 1, 15),
    _MemberPktsinHi32_Type()
)
memberPktsinHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberPktsinHi32.setStatus("mandatory")
_MemberPktsoutHi32_Type = Counter32
_MemberPktsoutHi32_Object = MibTableColumn
memberPktsoutHi32 = _MemberPktsoutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 104, 2, 1, 16),
    _MemberPktsoutHi32_Type()
)
memberPktsoutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberPktsoutHi32.setStatus("mandatory")
_MemberBitsinHi32_Type = Counter32
_MemberBitsinHi32_Object = MibTableColumn
memberBitsinHi32 = _MemberBitsinHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 104, 2, 1, 17),
    _MemberBitsinHi32_Type()
)
memberBitsinHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberBitsinHi32.setStatus("mandatory")
_MemberBitsoutHi32_Type = Counter32
_MemberBitsoutHi32_Object = MibTableColumn
memberBitsoutHi32 = _MemberBitsoutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 104, 2, 1, 18),
    _MemberBitsoutHi32_Type()
)
memberBitsoutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberBitsoutHi32.setStatus("mandatory")
_LoadBalTrap_ObjectIdentity = ObjectIdentity
loadBalTrap = _LoadBalTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 110)
)
_LoadBalTraps_ObjectIdentity = ObjectIdentity
loadBalTraps = _LoadBalTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 110, 2)
)

# Managed Objects groups


# Notification objects

loadBalTrapMisc = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 110, 2, 0, 1)
)
if mibBuilder.loadTexts:
    loadBalTrapMisc.setStatus(
        ""
    )

loadBalTrapServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 110, 2, 0, 2)
)
if mibBuilder.loadTexts:
    loadBalTrapServiceDown.setStatus(
        ""
    )

loadBalTrapServiceUP = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 110, 2, 0, 3)
)
if mibBuilder.loadTexts:
    loadBalTrapServiceUP.setStatus(
        ""
    )

loadBalTrapReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 110, 2, 0, 4)
)
if mibBuilder.loadTexts:
    loadBalTrapReset.setStatus(
        ""
    )

loadBalTrapDenial = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 110, 2, 0, 5)
)
if mibBuilder.loadTexts:
    loadBalTrapDenial.setStatus(
        ""
    )

loadBalTrapLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 110, 2, 0, 6)
)
if mibBuilder.loadTexts:
    loadBalTrapLogin.setStatus(
        ""
    )

loadBalTrapRemoveUnit = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 110, 2, 0, 7)
)
if mibBuilder.loadTexts:
    loadBalTrapRemoveUnit.setStatus(
        ""
    )

loadBalTrapAddUnit = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 110, 2, 0, 8)
)
if mibBuilder.loadTexts:
    loadBalTrapAddUnit.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LOAD-BAL-SYSTEM-MIB",
    **{"DisplayString": DisplayString,
       "f5": f5,
       "f5systems": f5systems,
       "loadbal": loadbal,
       "virtualAddress": virtualAddress,
       "virtualAddressNumber": virtualAddressNumber,
       "virtualAddressTable": virtualAddressTable,
       "virtualAddressEntry": virtualAddressEntry,
       "virtualAddressIpAddress": virtualAddressIpAddress,
       "virtualAddressStatus": virtualAddressStatus,
       "virtualAddressConnLimit": virtualAddressConnLimit,
       "virtualAddressNetmask": virtualAddressNetmask,
       "virtualAddressBroadcast": virtualAddressBroadcast,
       "virtualAddressInterface": virtualAddressInterface,
       "virtualAddressFailoverFlags": virtualAddressFailoverFlags,
       "virtualAddressOctetsIn": virtualAddressOctetsIn,
       "virtualAddressOctetsOut": virtualAddressOctetsOut,
       "virtualAddressPacketsIn": virtualAddressPacketsIn,
       "virtualAddressPacketsOut": virtualAddressPacketsOut,
       "virtualAddressCurrentConn": virtualAddressCurrentConn,
       "virtualAddressMaxConn": virtualAddressMaxConn,
       "virtualAddressTotalConn": virtualAddressTotalConn,
       "virtualAddressOctetsInHi32": virtualAddressOctetsInHi32,
       "virtualAddressOctetsOutHi32": virtualAddressOctetsOutHi32,
       "virtualAddressPacketsInHi32": virtualAddressPacketsInHi32,
       "virtualAddressPacketsOutHi32": virtualAddressPacketsOutHi32,
       "virtualAddressUnitId": virtualAddressUnitId,
       "virtualServer": virtualServer,
       "virtualServerNumber": virtualServerNumber,
       "virtualServerTable": virtualServerTable,
       "virtualServerEntry": virtualServerEntry,
       "virtualServerIpAddress": virtualServerIpAddress,
       "virtualServerPort": virtualServerPort,
       "virtualServerStatus": virtualServerStatus,
       "virtualServerConnLimit": virtualServerConnLimit,
       "virtualServerAppProtocol": virtualServerAppProtocol,
       "virtualServerAppProtocolTimeout": virtualServerAppProtocolTimeout,
       "virtualServerAppProtocolReaper": virtualServerAppProtocolReaper,
       "virtualServerPersistTimeout": virtualServerPersistTimeout,
       "virtualServerPersistMask": virtualServerPersistMask,
       "virtualServerSticky": virtualServerSticky,
       "virtualServerStickyMask": virtualServerStickyMask,
       "virtualServerFailoverFlags": virtualServerFailoverFlags,
       "virtualServerOctetsIn": virtualServerOctetsIn,
       "virtualServerOctetsOut": virtualServerOctetsOut,
       "virtualServerPacketsIn": virtualServerPacketsIn,
       "virtualServerPacketsOut": virtualServerPacketsOut,
       "virtualServerCurrentConn": virtualServerCurrentConn,
       "virtualServerMaxConn": virtualServerMaxConn,
       "virtualServerTotalConn": virtualServerTotalConn,
       "virtualServerSslNew": virtualServerSslNew,
       "virtualServerSslHits": virtualServerSslHits,
       "virtualServerSslTimeouts": virtualServerSslTimeouts,
       "virtualServerSslMisses": virtualServerSslMisses,
       "virtualServerOctetsInHi32": virtualServerOctetsInHi32,
       "virtualServerOctetsOutHi32": virtualServerOctetsOutHi32,
       "virtualServerPacketsInHi32": virtualServerPacketsInHi32,
       "virtualServerPacketsOutHi32": virtualServerPacketsOutHi32,
       "virtualServerCookieMethod": virtualServerCookieMethod,
       "virtualServerRule": virtualServerRule,
       "virtualServerPool": virtualServerPool,
       "snat": snat,
       "snatTransTable": snatTransTable,
       "snatTransEntry": snatTransEntry,
       "snatTransEnabled": snatTransEnabled,
       "snatTransAddr": snatTransAddr,
       "snatTransIface": snatTransIface,
       "snatTransNetmask": snatTransNetmask,
       "snatTransBroadcast": snatTransBroadcast,
       "snatTransSecsCollectingStats": snatTransSecsCollectingStats,
       "snatTransBitsIn": snatTransBitsIn,
       "snatTransBitsOut": snatTransBitsOut,
       "snatTransPktsIn": snatTransPktsIn,
       "snatTransPktsOut": snatTransPktsOut,
       "snatTransCurrConns": snatTransCurrConns,
       "snatTransMaxConns": snatTransMaxConns,
       "snatTransTotalConns": snatTransTotalConns,
       "snatTransBitsInHi32": snatTransBitsInHi32,
       "snatTransBitsOutHi32": snatTransBitsOutHi32,
       "snatTransPktsInHi32": snatTransPktsInHi32,
       "snatTransPktsOutHi32": snatTransPktsOutHi32,
       "snatTransLastTransPort": snatTransLastTransPort,
       "snatTransUnitId": snatTransUnitId,
       "snatOrigTable": snatOrigTable,
       "snatOrigEntry": snatOrigEntry,
       "snatOrigEnabled": snatOrigEnabled,
       "snatOrigAddr": snatOrigAddr,
       "snatOrigConnLimit": snatOrigConnLimit,
       "snatOrigTransAddr": snatOrigTransAddr,
       "snatOrigTcpIdleTimeout": snatOrigTcpIdleTimeout,
       "snatOrigUdpIdleTimeout": snatOrigUdpIdleTimeout,
       "snatOrigStatsZeroTime": snatOrigStatsZeroTime,
       "snatOrigSecsCollectingStats": snatOrigSecsCollectingStats,
       "snatOrigBitsIn": snatOrigBitsIn,
       "snatOrigBitsOut": snatOrigBitsOut,
       "snatOrigPktsIn": snatOrigPktsIn,
       "snatOrigPktsOut": snatOrigPktsOut,
       "snatOrigCurrConns": snatOrigCurrConns,
       "snatOrigMaxConns": snatOrigMaxConns,
       "snatOrigTotalConns": snatOrigTotalConns,
       "snatOrigBitsInHi32": snatOrigBitsInHi32,
       "snatOrigBitsOutHi32": snatOrigBitsOutHi32,
       "snatOrigPktsInHi32": snatOrigPktsInHi32,
       "snatOrigPktsOutHi32": snatOrigPktsOutHi32,
       "snatOrigLastTransPort": snatOrigLastTransPort,
       "interface": interface,
       "interfaceNumber": interfaceNumber,
       "interfaceTable": interfaceTable,
       "interfaceEntry": interfaceEntry,
       "interfaceName": interfaceName,
       "interfaceIpAddresses": interfaceIpAddresses,
       "interfaceDestination": interfaceDestination,
       "interfaceSource": interfaceSource,
       "interfaceTimeout": interfaceTimeout,
       "interfaceArmed": interfaceArmed,
       "interfaceVLANSEnabled": interfaceVLANSEnabled,
       "interfaceMasqueradeAddress": interfaceMasqueradeAddress,
       "interfaceLastTimeChanged": interfaceLastTimeChanged,
       "interfaceSpeed": interfaceSpeed,
       "interfaceFullDuplex": interfaceFullDuplex,
       "ifaddress": ifaddress,
       "ifaddressNumber": ifaddressNumber,
       "ifaddressTable": ifaddressTable,
       "ifaddressEntry": ifaddressEntry,
       "ifaddressIpAddress": ifaddressIpAddress,
       "ifaddressInterfaceName": ifaddressInterfaceName,
       "ifaddressNetmask": ifaddressNetmask,
       "ifaddressBroadcast": ifaddressBroadcast,
       "ifaddressType": ifaddressType,
       "ifaddressUnitId": ifaddressUnitId,
       "ifaddressVLANTag": ifaddressVLANTag,
       "pool": pool,
       "poolNumber": poolNumber,
       "poolTable": poolTable,
       "poolEntry": poolEntry,
       "poolName": poolName,
       "poolLBMode": poolLBMode,
       "poolDependent": poolDependent,
       "poolMemberQty": poolMemberQty,
       "poolBitsin": poolBitsin,
       "poolBitsout": poolBitsout,
       "poolBitsinHi32": poolBitsinHi32,
       "poolBitsoutHi32": poolBitsoutHi32,
       "poolPktsin": poolPktsin,
       "poolPktsout": poolPktsout,
       "poolPktsinHi32": poolPktsinHi32,
       "poolPktsoutHi32": poolPktsoutHi32,
       "poolMaxConn": poolMaxConn,
       "poolCurrentConn": poolCurrentConn,
       "poolTotalConn": poolTotalConn,
       "poolMember": poolMember,
       "poolMemberNumber": poolMemberNumber,
       "poolMemberTable": poolMemberTable,
       "poolMemberEntry": poolMemberEntry,
       "poolMemberPoolName": poolMemberPoolName,
       "poolMemberIpAddress": poolMemberIpAddress,
       "poolMemberPort": poolMemberPort,
       "poolMemberMaintenance": poolMemberMaintenance,
       "poolMemberRatio": poolMemberRatio,
       "poolMemberPriority": poolMemberPriority,
       "poolMemberWeight": poolMemberWeight,
       "poolMemberRipeness": poolMemberRipeness,
       "poolMemberBitsin": poolMemberBitsin,
       "poolMemberBitsout": poolMemberBitsout,
       "poolMemberBitsinHi32": poolMemberBitsinHi32,
       "poolMemberBitsoutHi32": poolMemberBitsoutHi32,
       "poolMemberPktsin": poolMemberPktsin,
       "poolMemberPktsout": poolMemberPktsout,
       "poolMemberPktsinHi32": poolMemberPktsinHi32,
       "poolMemberPktsoutHi32": poolMemberPktsoutHi32,
       "poolMemberConnLimit": poolMemberConnLimit,
       "poolMemberMaxConn": poolMemberMaxConn,
       "poolMemberCurrentConn": poolMemberCurrentConn,
       "poolMemberTotalConn": poolMemberTotalConn,
       "uptime": uptime,
       "contot": contot,
       "concur": concur,
       "conmax": conmax,
       "pktsin": pktsin,
       "pktsout": pktsout,
       "bitsin": bitsin,
       "bitsout": bitsout,
       "portdeny": portdeny,
       "droppedin": droppedin,
       "droppedout": droppedout,
       "active": active,
       "mirrorenabled": mirrorenabled,
       "resetcounters": resetcounters,
       "pktsinHi32": pktsinHi32,
       "pktsoutHi32": pktsoutHi32,
       "bitsinHi32": bitsinHi32,
       "bitsoutHi32": bitsoutHi32,
       "nodePing": nodePing,
       "nodeTimeout": nodeTimeout,
       "loadbalMode": loadbalMode,
       "watchDogArmed": watchDogArmed,
       "snatConnLimit": snatConnLimit,
       "snatTCPIdleTimeout": snatTCPIdleTimeout,
       "snatUDPIdleTimeout": snatUDPIdleTimeout,
       "gatewayFailsafe": gatewayFailsafe,
       "unitId": unitId,
       "memoryUsed": memoryUsed,
       "memoryTotal": memoryTotal,
       "vaddress": vaddress,
       "vaddressNumber": vaddressNumber,
       "vaddressTable": vaddressTable,
       "vaddressEntry": vaddressEntry,
       "vaddressIndex": vaddressIndex,
       "vaddressDescr": vaddressDescr,
       "vaddressIpAddr": vaddressIpAddr,
       "vaddressPktsin": vaddressPktsin,
       "vaddressPktsout": vaddressPktsout,
       "vaddressBitsin": vaddressBitsin,
       "vaddressBitsout": vaddressBitsout,
       "vaddressConcur": vaddressConcur,
       "vaddressConmax": vaddressConmax,
       "vaddressConlimit": vaddressConlimit,
       "vaddressContot": vaddressContot,
       "vaddressStatus": vaddressStatus,
       "vaddressPktsinHi32": vaddressPktsinHi32,
       "vaddressPktsoutHi32": vaddressPktsoutHi32,
       "vaddressBitsinHi32": vaddressBitsinHi32,
       "vaddressBitsoutHi32": vaddressBitsoutHi32,
       "ndaddr": ndaddr,
       "ndaddrNumber": ndaddrNumber,
       "ndaddrTable": ndaddrTable,
       "ndaddrEntry": ndaddrEntry,
       "ndaddrIndex": ndaddrIndex,
       "ndaddrDescr": ndaddrDescr,
       "ndaddrIpAddr": ndaddrIpAddr,
       "ndaddrPktsin": ndaddrPktsin,
       "ndaddrPktsout": ndaddrPktsout,
       "ndaddrBitsin": ndaddrBitsin,
       "ndaddrBitsout": ndaddrBitsout,
       "ndaddrConcur": ndaddrConcur,
       "ndaddrConmax": ndaddrConmax,
       "ndaddrConlimit": ndaddrConlimit,
       "ndaddrContot": ndaddrContot,
       "ndaddrStatus": ndaddrStatus,
       "ndaddrPktsinHi32": ndaddrPktsinHi32,
       "ndaddrPktsoutHi32": ndaddrPktsoutHi32,
       "ndaddrBitsinHi32": ndaddrBitsinHi32,
       "ndaddrBitsoutHi32": ndaddrBitsoutHi32,
       "ndaddrMaintenance": ndaddrMaintenance,
       "nat": nat,
       "natNumber": natNumber,
       "natTable": natTable,
       "natEntry": natEntry,
       "natIndex": natIndex,
       "natDescr": natDescr,
       "natIpAddrFR": natIpAddrFR,
       "natIpAddrTO": natIpAddrTO,
       "natPktsin": natPktsin,
       "natPktsout": natPktsout,
       "natBitsin": natBitsin,
       "natBitsout": natBitsout,
       "natPktsinHi32": natPktsinHi32,
       "natPktsoutHi32": natPktsoutHi32,
       "natBitsinHi32": natBitsinHi32,
       "natBitsoutHi32": natBitsoutHi32,
       "natOutsideNetmask": natOutsideNetmask,
       "natOutsideBroadcast": natOutsideBroadcast,
       "natInterface": natInterface,
       "natUnitId": natUnitId,
       "vport": vport,
       "vportNumber": vportNumber,
       "vportTable": vportTable,
       "vportEntry": vportEntry,
       "vportIndex": vportIndex,
       "vportPort": vportPort,
       "vportDescr": vportDescr,
       "vportPktsin": vportPktsin,
       "vportPktsout": vportPktsout,
       "vportBitsin": vportBitsin,
       "vportBitsout": vportBitsout,
       "vportConcur": vportConcur,
       "vportConmax": vportConmax,
       "vportConlimit": vportConlimit,
       "vportContot": vportContot,
       "vportReaped": vportReaped,
       "vportPktsinHi32": vportPktsinHi32,
       "vportPktsoutHi32": vportPktsoutHi32,
       "vportBitsinHi32": vportBitsinHi32,
       "vportBitsoutHi32": vportBitsoutHi32,
       "vportAllowed": vportAllowed,
       "vportTCPpersistance": vportTCPpersistance,
       "vportUDPpersistance": vportUDPpersistance,
       "member": member,
       "memberTable": memberTable,
       "memberEntry": memberEntry,
       "memberVirtualAddress": memberVirtualAddress,
       "memberVirtualAddressPort": memberVirtualAddressPort,
       "memberOrdinal": memberOrdinal,
       "memberAddress": memberAddress,
       "memberPort": memberPort,
       "memberStatus": memberStatus,
       "memberPktsin": memberPktsin,
       "memberPktsout": memberPktsout,
       "memberBitsin": memberBitsin,
       "memberBitsout": memberBitsout,
       "memberConcur": memberConcur,
       "memberConmax": memberConmax,
       "memberConlimit": memberConlimit,
       "memberContot": memberContot,
       "memberPktsinHi32": memberPktsinHi32,
       "memberPktsoutHi32": memberPktsoutHi32,
       "memberBitsinHi32": memberBitsinHi32,
       "memberBitsoutHi32": memberBitsoutHi32,
       "loadBalTrap": loadBalTrap,
       "loadBalTraps": loadBalTraps,
       "loadBalTrapMisc": loadBalTrapMisc,
       "loadBalTrapServiceDown": loadBalTrapServiceDown,
       "loadBalTrapServiceUP": loadBalTrapServiceUP,
       "loadBalTrapReset": loadBalTrapReset,
       "loadBalTrapDenial": loadBalTrapDenial,
       "loadBalTrapLogin": loadBalTrapLogin,
       "loadBalTrapRemoveUnit": loadBalTrapRemoveUnit,
       "loadBalTrapAddUnit": loadBalTrapAddUnit}
)
