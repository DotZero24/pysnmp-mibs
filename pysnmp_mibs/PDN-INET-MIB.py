# SNMP MIB module (PDN-INET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/paradyne/PDN-INET-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:00:31 2025
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

(pdn_common,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-common")

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

pdn_inet = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 26)
)
if mibBuilder.loadTexts:
    pdn_inet.setRevisions(
        ("1902-02-21 00:00",
         "1900-05-10 00:00",
         "1900-04-27 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PdnInetMIBObjects_ObjectIdentity = ObjectIdentity
pdnInetMIBObjects = _PdnInetMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 26, 1)
)


class _PdnInetTelnetServerPort_Type(Integer32):
    """Custom type pdnInetTelnetServerPort based on Integer32"""
    defaultValue = 23

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PdnInetTelnetServerPort_Type.__name__ = "Integer32"
_PdnInetTelnetServerPort_Object = MibScalar
pdnInetTelnetServerPort = _PdnInetTelnetServerPort_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 26, 1, 1),
    _PdnInetTelnetServerPort_Type()
)
pdnInetTelnetServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnInetTelnetServerPort.setStatus("current")


class _PdnInetFtpServerControlPort_Type(Integer32):
    """Custom type pdnInetFtpServerControlPort based on Integer32"""
    defaultValue = 21

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PdnInetFtpServerControlPort_Type.__name__ = "Integer32"
_PdnInetFtpServerControlPort_Object = MibScalar
pdnInetFtpServerControlPort = _PdnInetFtpServerControlPort_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 26, 1, 2),
    _PdnInetFtpServerControlPort_Type()
)
pdnInetFtpServerControlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnInetFtpServerControlPort.setStatus("current")


class _PdnInetFtpServerDataPort_Type(Integer32):
    """Custom type pdnInetFtpServerDataPort based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PdnInetFtpServerDataPort_Type.__name__ = "Integer32"
_PdnInetFtpServerDataPort_Object = MibScalar
pdnInetFtpServerDataPort = _PdnInetFtpServerDataPort_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 26, 1, 3),
    _PdnInetFtpServerDataPort_Type()
)
pdnInetFtpServerDataPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnInetFtpServerDataPort.setStatus("current")
_PdnInetIpAddressTableMaxIpSubnets_Type = Integer32
_PdnInetIpAddressTableMaxIpSubnets_Object = MibScalar
pdnInetIpAddressTableMaxIpSubnets = _PdnInetIpAddressTableMaxIpSubnets_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 26, 1, 4),
    _PdnInetIpAddressTableMaxIpSubnets_Type()
)
pdnInetIpAddressTableMaxIpSubnets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnInetIpAddressTableMaxIpSubnets.setStatus("current")
_PdnInetIpAddressTableCurrentIpSubnets_Type = Integer32
_PdnInetIpAddressTableCurrentIpSubnets_Object = MibScalar
pdnInetIpAddressTableCurrentIpSubnets = _PdnInetIpAddressTableCurrentIpSubnets_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 26, 1, 5),
    _PdnInetIpAddressTableCurrentIpSubnets_Type()
)
pdnInetIpAddressTableCurrentIpSubnets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnInetIpAddressTableCurrentIpSubnets.setStatus("current")
_PdnInetIpAddressTable_Object = MibTable
pdnInetIpAddressTable = _PdnInetIpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 26, 1, 6)
)
if mibBuilder.loadTexts:
    pdnInetIpAddressTable.setStatus("current")
_PdnInetIpAddressTableEntry_Object = MibTableRow
pdnInetIpAddressTableEntry = _PdnInetIpAddressTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 26, 1, 6, 1)
)
pdnInetIpAddressTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "PDN-INET-MIB", "pdnInetIpAddress"),
)
if mibBuilder.loadTexts:
    pdnInetIpAddressTableEntry.setStatus("current")
_PdnInetIpAddress_Type = IpAddress
_PdnInetIpAddress_Object = MibTableColumn
pdnInetIpAddress = _PdnInetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 26, 1, 6, 1, 1),
    _PdnInetIpAddress_Type()
)
pdnInetIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnInetIpAddress.setStatus("current")
_PdnInetIpSubnetMask_Type = IpAddress
_PdnInetIpSubnetMask_Object = MibTableColumn
pdnInetIpSubnetMask = _PdnInetIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 26, 1, 6, 1, 2),
    _PdnInetIpSubnetMask_Type()
)
pdnInetIpSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnInetIpSubnetMask.setStatus("current")


class _PdnInetIpAddressType_Type(Integer32):
    """Custom type pdnInetIpAddressType based on Integer32"""
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
        *(("primary", 1),
          ("secondary", 2),
          ("primaryBootp", 3),
          ("secondaryBootp", 4))
    )


_PdnInetIpAddressType_Type.__name__ = "Integer32"
_PdnInetIpAddressType_Object = MibTableColumn
pdnInetIpAddressType = _PdnInetIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 26, 1, 6, 1, 3),
    _PdnInetIpAddressType_Type()
)
pdnInetIpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnInetIpAddressType.setStatus("current")
_PdnInetIpRowStatus_Type = RowStatus
_PdnInetIpRowStatus_Object = MibTableColumn
pdnInetIpRowStatus = _PdnInetIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 26, 1, 6, 1, 4),
    _PdnInetIpRowStatus_Type()
)
pdnInetIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnInetIpRowStatus.setStatus("current")
_PdnInetIpGateway_Type = IpAddress
_PdnInetIpGateway_Object = MibTableColumn
pdnInetIpGateway = _PdnInetIpGateway_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 26, 1, 6, 1, 5),
    _PdnInetIpGateway_Type()
)
pdnInetIpGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnInetIpGateway.setStatus("current")
_PdnInetMIBTraps_ObjectIdentity = ObjectIdentity
pdnInetMIBTraps = _PdnInetMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 26, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-INET-MIB",
    **{"pdn-inet": pdn_inet,
       "pdnInetMIBObjects": pdnInetMIBObjects,
       "pdnInetTelnetServerPort": pdnInetTelnetServerPort,
       "pdnInetFtpServerControlPort": pdnInetFtpServerControlPort,
       "pdnInetFtpServerDataPort": pdnInetFtpServerDataPort,
       "pdnInetIpAddressTableMaxIpSubnets": pdnInetIpAddressTableMaxIpSubnets,
       "pdnInetIpAddressTableCurrentIpSubnets": pdnInetIpAddressTableCurrentIpSubnets,
       "pdnInetIpAddressTable": pdnInetIpAddressTable,
       "pdnInetIpAddressTableEntry": pdnInetIpAddressTableEntry,
       "pdnInetIpAddress": pdnInetIpAddress,
       "pdnInetIpSubnetMask": pdnInetIpSubnetMask,
       "pdnInetIpAddressType": pdnInetIpAddressType,
       "pdnInetIpRowStatus": pdnInetIpRowStatus,
       "pdnInetIpGateway": pdnInetIpGateway,
       "pdnInetMIBTraps": pdnInetMIBTraps}
)
