# SNMP MIB module (MX-H323-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-H323-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:44 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ipAddressConfig,
 ipAddressStatus,
 mediatrixIpTelephonySignaling) = mibBuilder.importSymbols(
    "MX-SMI",
    "ipAddressConfig",
    "ipAddressStatus",
    "mediatrixIpTelephonySignaling")

(MxIpConfigSource,
 MxIpSelectConfigSource) = mibBuilder.importSymbols(
    "MX-TC",
    "MxIpConfigSource",
    "MxIpSelectConfigSource")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpAddressStatusH323_ObjectIdentity = ObjectIdentity
ipAddressStatusH323 = _IpAddressStatusH323_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 90)
)


class _H323ConfigSource_Type(MxIpConfigSource):
    """Custom type h323ConfigSource based on MxIpConfigSource"""
    defaultValue = 1


_H323ConfigSource_Type.__name__ = "MxIpConfigSource"
_H323ConfigSource_Object = MibScalar
h323ConfigSource = _H323ConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 90, 5),
    _H323ConfigSource_Type()
)
h323ConfigSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323ConfigSource.setStatus("current")
_IpAddressConfigH323_ObjectIdentity = ObjectIdentity
ipAddressConfigH323 = _IpAddressConfigH323_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 90)
)


class _H323SelectConfigSource_Type(MxIpSelectConfigSource):
    """Custom type h323SelectConfigSource based on MxIpSelectConfigSource"""
    defaultValue = 1


_H323SelectConfigSource_Type.__name__ = "MxIpSelectConfigSource"
_H323SelectConfigSource_Object = MibScalar
h323SelectConfigSource = _H323SelectConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 90, 5),
    _H323SelectConfigSource_Type()
)
h323SelectConfigSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323SelectConfigSource.setStatus("current")
_IpAddressConfigH323Static_ObjectIdentity = ObjectIdentity
ipAddressConfigH323Static = _IpAddressConfigH323Static_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 90, 10)
)
_IpAddressConfigH323Dhcp_ObjectIdentity = ObjectIdentity
ipAddressConfigH323Dhcp = _IpAddressConfigH323Dhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 90, 15)
)
_H323_ObjectIdentity = ObjectIdentity
h323 = _H323_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30)
)
if mibBuilder.loadTexts:
    h323.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-H323-MIB",
    **{"ipAddressStatusH323": ipAddressStatusH323,
       "h323ConfigSource": h323ConfigSource,
       "ipAddressConfigH323": ipAddressConfigH323,
       "h323SelectConfigSource": h323SelectConfigSource,
       "ipAddressConfigH323Static": ipAddressConfigH323Static,
       "ipAddressConfigH323Dhcp": ipAddressConfigH323Dhcp,
       "h323": h323}
)
