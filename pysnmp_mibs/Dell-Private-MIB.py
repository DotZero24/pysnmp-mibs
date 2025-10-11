# SNMP MIB module (Dell-Private-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/dell/Dell-Private-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:09:05 2025
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

(rnd,) = mibBuilder.importSymbols(
    "Dell-MIB",
    "rnd")

(ipAddrEntry,) = mibBuilder.importSymbols(
    "IP-MIB",
    "ipAddrEntry")

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


# MODULE-IDENTITY

rlOperationalMode = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 121)
)
if mibBuilder.loadTexts:
    rlOperationalMode.setRevisions(
        ("2006-11-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _RlOperationalModeState_Type(Integer32):
    """Custom type rlOperationalModeState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("managed", 0),
          ("unmanaged", 1),
          ("secure", 2))
    )


_RlOperationalModeState_Type.__name__ = "Integer32"
_RlOperationalModeState_Object = MibScalar
rlOperationalModeState = _RlOperationalModeState_Object(
    (1, 3, 6, 1, 4, 1, 89, 121, 1),
    _RlOperationalModeState_Type()
)
rlOperationalModeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOperationalModeState.setStatus("current")
_RlGlobalIpAddrTable_Object = MibTable
rlGlobalIpAddrTable = _RlGlobalIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 121, 2)
)
if mibBuilder.loadTexts:
    rlGlobalIpAddrTable.setStatus("current")
_RlGlobalIpAddrEntry_Object = MibTableRow
rlGlobalIpAddrEntry = _RlGlobalIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 121, 2, 1)
)
rlGlobalIpAddrEntry.setIndexNames(
    (0, "Dell-Private-MIB", "rlGlobalIpAdIndex"),
)
if mibBuilder.loadTexts:
    rlGlobalIpAddrEntry.setStatus("current")


class _RlGlobalIpAdIndex_Type(Integer32):
    """Custom type rlGlobalIpAdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_RlGlobalIpAdIndex_Type.__name__ = "Integer32"
_RlGlobalIpAdIndex_Object = MibTableColumn
rlGlobalIpAdIndex = _RlGlobalIpAdIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 121, 2, 1, 1),
    _RlGlobalIpAdIndex_Type()
)
rlGlobalIpAdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlGlobalIpAdIndex.setStatus("current")
_RlGlobalIpAdEntAddr_Type = IpAddress
_RlGlobalIpAdEntAddr_Object = MibTableColumn
rlGlobalIpAdEntAddr = _RlGlobalIpAdEntAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 121, 2, 1, 2),
    _RlGlobalIpAdEntAddr_Type()
)
rlGlobalIpAdEntAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlGlobalIpAdEntAddr.setStatus("current")
_RlGlobalIpAdEntNetMask_Type = IpAddress
_RlGlobalIpAdEntNetMask_Object = MibTableColumn
rlGlobalIpAdEntNetMask = _RlGlobalIpAdEntNetMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 121, 2, 1, 3),
    _RlGlobalIpAdEntNetMask_Type()
)
rlGlobalIpAdEntNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlGlobalIpAdEntNetMask.setStatus("current")
_RlGlobalIpAdDefaultGateway_Type = IpAddress
_RlGlobalIpAdDefaultGateway_Object = MibTableColumn
rlGlobalIpAdDefaultGateway = _RlGlobalIpAdDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 89, 121, 2, 1, 4),
    _RlGlobalIpAdDefaultGateway_Type()
)
rlGlobalIpAdDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlGlobalIpAdDefaultGateway.setStatus("current")


class _RlGlobalIpAdOwner_Type(Integer32):
    """Custom type rlGlobalIpAdOwner based on Integer32"""
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
        *(("static", 1),
          ("dhcp", 2),
          ("default", 3))
    )


_RlGlobalIpAdOwner_Type.__name__ = "Integer32"
_RlGlobalIpAdOwner_Object = MibTableColumn
rlGlobalIpAdOwner = _RlGlobalIpAdOwner_Object(
    (1, 3, 6, 1, 4, 1, 89, 121, 2, 1, 5),
    _RlGlobalIpAdOwner_Type()
)
rlGlobalIpAdOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlGlobalIpAdOwner.setStatus("current")


class _RlDeleteUsersAfterReset_Type(Integer32):
    """Custom type rlDeleteUsersAfterReset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_RlDeleteUsersAfterReset_Type.__name__ = "Integer32"
_RlDeleteUsersAfterReset_Object = MibScalar
rlDeleteUsersAfterReset = _RlDeleteUsersAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 121, 3),
    _RlDeleteUsersAfterReset_Type()
)
rlDeleteUsersAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDeleteUsersAfterReset.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Dell-Private-MIB",
    **{"rlOperationalMode": rlOperationalMode,
       "rlOperationalModeState": rlOperationalModeState,
       "rlGlobalIpAddrTable": rlGlobalIpAddrTable,
       "rlGlobalIpAddrEntry": rlGlobalIpAddrEntry,
       "rlGlobalIpAdIndex": rlGlobalIpAdIndex,
       "rlGlobalIpAdEntAddr": rlGlobalIpAdEntAddr,
       "rlGlobalIpAdEntNetMask": rlGlobalIpAdEntNetMask,
       "rlGlobalIpAdDefaultGateway": rlGlobalIpAdDefaultGateway,
       "rlGlobalIpAdOwner": rlGlobalIpAdOwner,
       "rlDeleteUsersAfterReset": rlDeleteUsersAfterReset}
)
