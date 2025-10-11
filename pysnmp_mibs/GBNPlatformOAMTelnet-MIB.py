# SNMP MIB module (GBNPlatformOAMTelnet-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/GBNPlatformOAMTelnet-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:14:56 2025
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

(gbnPlatformOAM,) = mibBuilder.importSymbols(
    "GBNPlatformOAM-MIB",
    "gbnPlatformOAM")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(snmpTraps,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmpTraps")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

gbnPlatformOAMTelnet = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 15)
)
if mibBuilder.loadTexts:
    gbnPlatformOAMTelnet.setRevisions(
        ("1913-04-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _TelnetState_Type(Integer32):
    """Custom type telnetState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TelnetState_Type.__name__ = "Integer32"
_TelnetState_Object = MibScalar
telnetState = _TelnetState_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 15, 1),
    _TelnetState_Type()
)
telnetState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetState.setStatus("current")


class _TelnetUserLimit_Type(Integer32):
    """Custom type telnetUserLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_TelnetUserLimit_Type.__name__ = "Integer32"
_TelnetUserLimit_Object = MibScalar
telnetUserLimit = _TelnetUserLimit_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 15, 2),
    _TelnetUserLimit_Type()
)
telnetUserLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetUserLimit.setStatus("current")
_TelnetLoginUsers_Type = Counter32
_TelnetLoginUsers_Object = MibScalar
telnetLoginUsers = _TelnetLoginUsers_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 15, 3),
    _TelnetLoginUsers_Type()
)
telnetLoginUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telnetLoginUsers.setStatus("current")
_TelnetUserTable_Object = MibTable
telnetUserTable = _TelnetUserTable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 15, 4)
)
if mibBuilder.loadTexts:
    telnetUserTable.setStatus("current")
_TelnetUserEntry_Object = MibTableRow
telnetUserEntry = _TelnetUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 15, 4, 1)
)
telnetUserEntry.setIndexNames(
    (0, "GBNPlatformOAMTelnet-MIB", "telnetUserTerminal"),
)
if mibBuilder.loadTexts:
    telnetUserEntry.setStatus("current")
_TelnetUserTerminal_Type = Counter32
_TelnetUserTerminal_Object = MibTableColumn
telnetUserTerminal = _TelnetUserTerminal_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 15, 4, 1, 1),
    _TelnetUserTerminal_Type()
)
telnetUserTerminal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telnetUserTerminal.setStatus("current")


class _TelnetUserAddrIp_Type(DisplayString):
    """Custom type telnetUserAddrIp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TelnetUserAddrIp_Type.__name__ = "DisplayString"
_TelnetUserAddrIp_Object = MibTableColumn
telnetUserAddrIp = _TelnetUserAddrIp_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 15, 4, 1, 2),
    _TelnetUserAddrIp_Type()
)
telnetUserAddrIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telnetUserAddrIp.setStatus("current")


class _TelnetUserName_Type(DisplayString):
    """Custom type telnetUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TelnetUserName_Type.__name__ = "DisplayString"
_TelnetUserName_Object = MibTableColumn
telnetUserName = _TelnetUserName_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 15, 4, 1, 3),
    _TelnetUserName_Type()
)
telnetUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telnetUserName.setStatus("current")


class _TelnetUserLoginTime_Type(DisplayString):
    """Custom type telnetUserLoginTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_TelnetUserLoginTime_Type.__name__ = "DisplayString"
_TelnetUserLoginTime_Object = MibTableColumn
telnetUserLoginTime = _TelnetUserLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 15, 4, 1, 4),
    _TelnetUserLoginTime_Type()
)
telnetUserLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telnetUserLoginTime.setStatus("current")


class _TelnetUserTransport_Type(DisplayString):
    """Custom type telnetUserTransport based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TelnetUserTransport_Type.__name__ = "DisplayString"
_TelnetUserTransport_Object = MibTableColumn
telnetUserTransport = _TelnetUserTransport_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 15, 4, 1, 5),
    _TelnetUserTransport_Type()
)
telnetUserTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telnetUserTransport.setStatus("current")
_TelnetUserRowStatus_Type = RowStatus
_TelnetUserRowStatus_Object = MibTableColumn
telnetUserRowStatus = _TelnetUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 15, 4, 1, 6),
    _TelnetUserRowStatus_Type()
)
telnetUserRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetUserRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GBNPlatformOAMTelnet-MIB",
    **{"gbnPlatformOAMTelnet": gbnPlatformOAMTelnet,
       "telnetState": telnetState,
       "telnetUserLimit": telnetUserLimit,
       "telnetLoginUsers": telnetLoginUsers,
       "telnetUserTable": telnetUserTable,
       "telnetUserEntry": telnetUserEntry,
       "telnetUserTerminal": telnetUserTerminal,
       "telnetUserAddrIp": telnetUserAddrIp,
       "telnetUserName": telnetUserName,
       "telnetUserLoginTime": telnetUserLoginTime,
       "telnetUserTransport": telnetUserTransport,
       "telnetUserRowStatus": telnetUserRowStatus}
)
