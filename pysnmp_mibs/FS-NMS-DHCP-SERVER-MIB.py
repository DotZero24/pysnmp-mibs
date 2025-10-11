# SNMP MIB module (FS-NMS-DHCP-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-NMS-DHCP-SERVER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:13:16 2025
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

(nmsMgmt,) = mibBuilder.importSymbols(
    "FS-NMS-SMI",
    "nmsMgmt")

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

_Dhcp_ObjectIdentity = ObjectIdentity
dhcp = _Dhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 9, 355)
)


class _DhcpServerStatus_Type(Integer32):
    """Custom type dhcpServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DhcpServerStatus_Type.__name__ = "Integer32"
_DhcpServerStatus_Object = MibScalar
dhcpServerStatus = _DhcpServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 9, 355, 1),
    _DhcpServerStatus_Type()
)
dhcpServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerStatus.setStatus("mandatory")
_NmsDhcpIpAddrPoolTable_Object = MibTable
nmsDhcpIpAddrPoolTable = _NmsDhcpIpAddrPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 9, 355, 2)
)
if mibBuilder.loadTexts:
    nmsDhcpIpAddrPoolTable.setStatus("mandatory")
_NmsDhcpIpAddrPoolEntry_Object = MibTableRow
nmsDhcpIpAddrPoolEntry = _NmsDhcpIpAddrPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 9, 355, 2, 1)
)
nmsDhcpIpAddrPoolEntry.setIndexNames(
    (0, "FS-NMS-DHCP-SERVER-MIB", "nmsDhcpIpAddrPoolIndex"),
)
if mibBuilder.loadTexts:
    nmsDhcpIpAddrPoolEntry.setStatus("mandatory")
_NmsDhcpIpAddrPoolIndex_Type = Integer32
_NmsDhcpIpAddrPoolIndex_Object = MibTableColumn
nmsDhcpIpAddrPoolIndex = _NmsDhcpIpAddrPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 9, 355, 2, 1, 1),
    _NmsDhcpIpAddrPoolIndex_Type()
)
nmsDhcpIpAddrPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsDhcpIpAddrPoolIndex.setStatus("mandatory")
_NmsDhcpIpAddrPoolSubNetwork_Type = IpAddress
_NmsDhcpIpAddrPoolSubNetwork_Object = MibTableColumn
nmsDhcpIpAddrPoolSubNetwork = _NmsDhcpIpAddrPoolSubNetwork_Object(
    (1, 3, 6, 1, 4, 1, 52642, 9, 355, 2, 1, 2),
    _NmsDhcpIpAddrPoolSubNetwork_Type()
)
nmsDhcpIpAddrPoolSubNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsDhcpIpAddrPoolSubNetwork.setStatus("mandatory")
_NmsDhcpIpAddrPoolMask_Type = IpAddress
_NmsDhcpIpAddrPoolMask_Object = MibTableColumn
nmsDhcpIpAddrPoolMask = _NmsDhcpIpAddrPoolMask_Object(
    (1, 3, 6, 1, 4, 1, 52642, 9, 355, 2, 1, 3),
    _NmsDhcpIpAddrPoolMask_Type()
)
nmsDhcpIpAddrPoolMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsDhcpIpAddrPoolMask.setStatus("mandatory")
_NmsDhcpIpAddrPoolStart_Type = IpAddress
_NmsDhcpIpAddrPoolStart_Object = MibTableColumn
nmsDhcpIpAddrPoolStart = _NmsDhcpIpAddrPoolStart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 9, 355, 2, 1, 4),
    _NmsDhcpIpAddrPoolStart_Type()
)
nmsDhcpIpAddrPoolStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsDhcpIpAddrPoolStart.setStatus("mandatory")
_NmsDhcpIpAddrPoolEnd_Type = IpAddress
_NmsDhcpIpAddrPoolEnd_Object = MibTableColumn
nmsDhcpIpAddrPoolEnd = _NmsDhcpIpAddrPoolEnd_Object(
    (1, 3, 6, 1, 4, 1, 52642, 9, 355, 2, 1, 5),
    _NmsDhcpIpAddrPoolEnd_Type()
)
nmsDhcpIpAddrPoolEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsDhcpIpAddrPoolEnd.setStatus("mandatory")
_NmsDhcpIpAddrPoolReserveAddrList_Type = OctetString
_NmsDhcpIpAddrPoolReserveAddrList_Object = MibTableColumn
nmsDhcpIpAddrPoolReserveAddrList = _NmsDhcpIpAddrPoolReserveAddrList_Object(
    (1, 3, 6, 1, 4, 1, 52642, 9, 355, 2, 1, 6),
    _NmsDhcpIpAddrPoolReserveAddrList_Type()
)
nmsDhcpIpAddrPoolReserveAddrList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsDhcpIpAddrPoolReserveAddrList.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-NMS-DHCP-SERVER-MIB",
    **{"dhcp": dhcp,
       "dhcpServerStatus": dhcpServerStatus,
       "nmsDhcpIpAddrPoolTable": nmsDhcpIpAddrPoolTable,
       "nmsDhcpIpAddrPoolEntry": nmsDhcpIpAddrPoolEntry,
       "nmsDhcpIpAddrPoolIndex": nmsDhcpIpAddrPoolIndex,
       "nmsDhcpIpAddrPoolSubNetwork": nmsDhcpIpAddrPoolSubNetwork,
       "nmsDhcpIpAddrPoolMask": nmsDhcpIpAddrPoolMask,
       "nmsDhcpIpAddrPoolStart": nmsDhcpIpAddrPoolStart,
       "nmsDhcpIpAddrPoolEnd": nmsDhcpIpAddrPoolEnd,
       "nmsDhcpIpAddrPoolReserveAddrList": nmsDhcpIpAddrPoolReserveAddrList}
)
