# SNMP MIB module (ELTEX-MES-AAA-STATISTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-AAA-STATISTICS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:48:20 2025
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

(eltMesAAAStatMIB,) = mibBuilder.importSymbols(
    "ELTEX-MES-MNG-MIB",
    "eltMesAAAStatMIB")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltRadiusServerStatusTable_Object = MibTable
eltRadiusServerStatusTable = _EltRadiusServerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 21)
)
if mibBuilder.loadTexts:
    eltRadiusServerStatusTable.setStatus("current")
_EltRadiusServerStatusEntry_Object = MibTableRow
eltRadiusServerStatusEntry = _EltRadiusServerStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 21, 1)
)
eltRadiusServerStatusEntry.setIndexNames(
    (0, "ELTEX-MES-AAA-STATISTICS-MIB", "eltRadiusServerAddressType"),
    (0, "ELTEX-MES-AAA-STATISTICS-MIB", "eltRadiusServerAddress"),
    (0, "ELTEX-MES-AAA-STATISTICS-MIB", "eltRadiusServerAuthPortNumber"),
    (0, "ELTEX-MES-AAA-STATISTICS-MIB", "eltRadiusServerAcctPortNumber"),
)
if mibBuilder.loadTexts:
    eltRadiusServerStatusEntry.setStatus("current")
_EltRadiusServerAddressType_Type = InetAddressType
_EltRadiusServerAddressType_Object = MibTableColumn
eltRadiusServerAddressType = _EltRadiusServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 21, 1, 1),
    _EltRadiusServerAddressType_Type()
)
eltRadiusServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltRadiusServerAddressType.setStatus("current")
_EltRadiusServerAddress_Type = InetAddress
_EltRadiusServerAddress_Object = MibTableColumn
eltRadiusServerAddress = _EltRadiusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 21, 1, 2),
    _EltRadiusServerAddress_Type()
)
eltRadiusServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltRadiusServerAddress.setStatus("current")


class _EltRadiusServerAuthPortNumber_Type(Integer32):
    """Custom type eltRadiusServerAuthPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EltRadiusServerAuthPortNumber_Type.__name__ = "Integer32"
_EltRadiusServerAuthPortNumber_Object = MibTableColumn
eltRadiusServerAuthPortNumber = _EltRadiusServerAuthPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 21, 1, 3),
    _EltRadiusServerAuthPortNumber_Type()
)
eltRadiusServerAuthPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltRadiusServerAuthPortNumber.setStatus("current")


class _EltRadiusServerAcctPortNumber_Type(Integer32):
    """Custom type eltRadiusServerAcctPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EltRadiusServerAcctPortNumber_Type.__name__ = "Integer32"
_EltRadiusServerAcctPortNumber_Object = MibTableColumn
eltRadiusServerAcctPortNumber = _EltRadiusServerAcctPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 21, 1, 4),
    _EltRadiusServerAcctPortNumber_Type()
)
eltRadiusServerAcctPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltRadiusServerAcctPortNumber.setStatus("current")
_EltRadiusServerAuthClientTimeouts_Type = Unsigned32
_EltRadiusServerAuthClientTimeouts_Object = MibTableColumn
eltRadiusServerAuthClientTimeouts = _EltRadiusServerAuthClientTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 21, 1, 5),
    _EltRadiusServerAuthClientTimeouts_Type()
)
eltRadiusServerAuthClientTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltRadiusServerAuthClientTimeouts.setStatus("current")
_EltRadiusServerDeadStatus_Type = TruthValue
_EltRadiusServerDeadStatus_Object = MibTableColumn
eltRadiusServerDeadStatus = _EltRadiusServerDeadStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 21, 1, 6),
    _EltRadiusServerDeadStatus_Type()
)
eltRadiusServerDeadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltRadiusServerDeadStatus.setStatus("current")
_EltRadiusServerRemainDeadTime_Type = Unsigned32
_EltRadiusServerRemainDeadTime_Object = MibTableColumn
eltRadiusServerRemainDeadTime = _EltRadiusServerRemainDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 21, 1, 7),
    _EltRadiusServerRemainDeadTime_Type()
)
eltRadiusServerRemainDeadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltRadiusServerRemainDeadTime.setStatus("current")


class _EltRadiusServerStatusReset_Type(Integer32):
    """Custom type eltRadiusServerStatusReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_EltRadiusServerStatusReset_Type.__name__ = "Integer32"
_EltRadiusServerStatusReset_Object = MibScalar
eltRadiusServerStatusReset = _EltRadiusServerStatusReset_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 22),
    _EltRadiusServerStatusReset_Type()
)
eltRadiusServerStatusReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltRadiusServerStatusReset.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-AAA-STATISTICS-MIB",
    **{"eltRadiusServerStatusTable": eltRadiusServerStatusTable,
       "eltRadiusServerStatusEntry": eltRadiusServerStatusEntry,
       "eltRadiusServerAddressType": eltRadiusServerAddressType,
       "eltRadiusServerAddress": eltRadiusServerAddress,
       "eltRadiusServerAuthPortNumber": eltRadiusServerAuthPortNumber,
       "eltRadiusServerAcctPortNumber": eltRadiusServerAcctPortNumber,
       "eltRadiusServerAuthClientTimeouts": eltRadiusServerAuthClientTimeouts,
       "eltRadiusServerDeadStatus": eltRadiusServerDeadStatus,
       "eltRadiusServerRemainDeadTime": eltRadiusServerRemainDeadTime,
       "eltRadiusServerStatusReset": eltRadiusServerStatusReset}
)
