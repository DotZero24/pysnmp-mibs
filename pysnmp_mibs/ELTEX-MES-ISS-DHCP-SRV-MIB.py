# SNMP MIB module (ELTEX-MES-ISS-DHCP-SRV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-ISS-DHCP-SRV-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:50:29 2025
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

(dhcpSrvSubnetPoolIndex,) = mibBuilder.importSymbols(
    "ARICENT-DHCP-SERVER-MIB",
    "dhcpSrvSubnetPoolIndex")

(eltMesIss,) = mibBuilder.importSymbols(
    "ELTEX-MES-ISS-MIB",
    "eltMesIss")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

eltMesIssDhcpSrvMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 33)
)
if mibBuilder.loadTexts:
    eltMesIssDhcpSrvMIB.setRevisions(
        ("2023-04-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesIssDhcpSrvObjects_ObjectIdentity = ObjectIdentity
eltMesIssDhcpSrvObjects = _EltMesIssDhcpSrvObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 33, 1)
)
_EltMesIssDhcpSrvGlobals_ObjectIdentity = ObjectIdentity
eltMesIssDhcpSrvGlobals = _EltMesIssDhcpSrvGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 33, 1, 1)
)
_EltMesIssDhcpSrvConfig_ObjectIdentity = ObjectIdentity
eltMesIssDhcpSrvConfig = _EltMesIssDhcpSrvConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 33, 1, 2)
)
_EltMesIssDhcpSrvHostInterfaceOptTable_Object = MibTable
eltMesIssDhcpSrvHostInterfaceOptTable = _EltMesIssDhcpSrvHostInterfaceOptTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 33, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eltMesIssDhcpSrvHostInterfaceOptTable.setStatus("current")
_EltMesIssDhcpSrvHostInterfaceOptEntry_Object = MibTableRow
eltMesIssDhcpSrvHostInterfaceOptEntry = _EltMesIssDhcpSrvHostInterfaceOptEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 33, 1, 2, 1, 1)
)
eltMesIssDhcpSrvHostInterfaceOptEntry.setIndexNames(
    (0, "ELTEX-MES-ISS-DHCP-SRV-MIB", "eltMesIssDhcpSrvHostInterfaceIfIndex"),
    (0, "ARICENT-DHCP-SERVER-MIB", "dhcpSrvSubnetPoolIndex"),
    (0, "ELTEX-MES-ISS-DHCP-SRV-MIB", "eltMesIssDhcpSrvHostInterfaceOptType"),
)
if mibBuilder.loadTexts:
    eltMesIssDhcpSrvHostInterfaceOptEntry.setStatus("current")
_EltMesIssDhcpSrvHostInterfaceIfIndex_Type = InterfaceIndex
_EltMesIssDhcpSrvHostInterfaceIfIndex_Object = MibTableColumn
eltMesIssDhcpSrvHostInterfaceIfIndex = _EltMesIssDhcpSrvHostInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 33, 1, 2, 1, 1, 1),
    _EltMesIssDhcpSrvHostInterfaceIfIndex_Type()
)
eltMesIssDhcpSrvHostInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssDhcpSrvHostInterfaceIfIndex.setStatus("current")


class _EltMesIssDhcpSrvHostInterfaceOptType_Type(Integer32):
    """Custom type eltMesIssDhcpSrvHostInterfaceOptType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EltMesIssDhcpSrvHostInterfaceOptType_Type.__name__ = "Integer32"
_EltMesIssDhcpSrvHostInterfaceOptType_Object = MibTableColumn
eltMesIssDhcpSrvHostInterfaceOptType = _EltMesIssDhcpSrvHostInterfaceOptType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 33, 1, 2, 1, 1, 2),
    _EltMesIssDhcpSrvHostInterfaceOptType_Type()
)
eltMesIssDhcpSrvHostInterfaceOptType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssDhcpSrvHostInterfaceOptType.setStatus("current")
_EltMesIssDhcpSrvHostInterfaceOptLen_Type = Integer32
_EltMesIssDhcpSrvHostInterfaceOptLen_Object = MibTableColumn
eltMesIssDhcpSrvHostInterfaceOptLen = _EltMesIssDhcpSrvHostInterfaceOptLen_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 33, 1, 2, 1, 1, 3),
    _EltMesIssDhcpSrvHostInterfaceOptLen_Type()
)
eltMesIssDhcpSrvHostInterfaceOptLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssDhcpSrvHostInterfaceOptLen.setStatus("current")
_EltMesIssDhcpSrvHostInterfaceOptVal_Type = OctetString
_EltMesIssDhcpSrvHostInterfaceOptVal_Object = MibTableColumn
eltMesIssDhcpSrvHostInterfaceOptVal = _EltMesIssDhcpSrvHostInterfaceOptVal_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 33, 1, 2, 1, 1, 4),
    _EltMesIssDhcpSrvHostInterfaceOptVal_Type()
)
eltMesIssDhcpSrvHostInterfaceOptVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssDhcpSrvHostInterfaceOptVal.setStatus("current")
_EltMesIssDhcpSrvHostInterfaceOptRowStatus_Type = RowStatus
_EltMesIssDhcpSrvHostInterfaceOptRowStatus_Object = MibTableColumn
eltMesIssDhcpSrvHostInterfaceOptRowStatus = _EltMesIssDhcpSrvHostInterfaceOptRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 33, 1, 2, 1, 1, 5),
    _EltMesIssDhcpSrvHostInterfaceOptRowStatus_Type()
)
eltMesIssDhcpSrvHostInterfaceOptRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssDhcpSrvHostInterfaceOptRowStatus.setStatus("current")
_EltMesIssDhcpSrvHostInterfaceConfigTable_Object = MibTable
eltMesIssDhcpSrvHostInterfaceConfigTable = _EltMesIssDhcpSrvHostInterfaceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 33, 1, 2, 2)
)
if mibBuilder.loadTexts:
    eltMesIssDhcpSrvHostInterfaceConfigTable.setStatus("current")
_EltMesIssDhcpSrvHostInterfaceConfigEntry_Object = MibTableRow
eltMesIssDhcpSrvHostInterfaceConfigEntry = _EltMesIssDhcpSrvHostInterfaceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 33, 1, 2, 2, 1)
)
eltMesIssDhcpSrvHostInterfaceConfigEntry.setIndexNames(
    (0, "ELTEX-MES-ISS-DHCP-SRV-MIB", "eltMesIssDhcpSrvHostInterfaceIfIndex"),
    (0, "ARICENT-DHCP-SERVER-MIB", "dhcpSrvSubnetPoolIndex"),
)
if mibBuilder.loadTexts:
    eltMesIssDhcpSrvHostInterfaceConfigEntry.setStatus("current")
_EltMesIssDhcpSrvHostInterfaceIpAddress_Type = IpAddress
_EltMesIssDhcpSrvHostInterfaceIpAddress_Object = MibTableColumn
eltMesIssDhcpSrvHostInterfaceIpAddress = _EltMesIssDhcpSrvHostInterfaceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 33, 1, 2, 2, 1, 1),
    _EltMesIssDhcpSrvHostInterfaceIpAddress_Type()
)
eltMesIssDhcpSrvHostInterfaceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssDhcpSrvHostInterfaceIpAddress.setStatus("current")
_EltMesIssDhcpSrvHostInterfacePoolName_Type = Integer32
_EltMesIssDhcpSrvHostInterfacePoolName_Object = MibTableColumn
eltMesIssDhcpSrvHostInterfacePoolName = _EltMesIssDhcpSrvHostInterfacePoolName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 33, 1, 2, 2, 1, 2),
    _EltMesIssDhcpSrvHostInterfacePoolName_Type()
)
eltMesIssDhcpSrvHostInterfacePoolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssDhcpSrvHostInterfacePoolName.setStatus("current")


class _EltMesIssDhcpSrvHostInterfaceBootFileName_Type(DisplayString):
    """Custom type eltMesIssDhcpSrvHostInterfaceBootFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EltMesIssDhcpSrvHostInterfaceBootFileName_Type.__name__ = "DisplayString"
_EltMesIssDhcpSrvHostInterfaceBootFileName_Object = MibTableColumn
eltMesIssDhcpSrvHostInterfaceBootFileName = _EltMesIssDhcpSrvHostInterfaceBootFileName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 33, 1, 2, 2, 1, 3),
    _EltMesIssDhcpSrvHostInterfaceBootFileName_Type()
)
eltMesIssDhcpSrvHostInterfaceBootFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssDhcpSrvHostInterfaceBootFileName.setStatus("current")
_EltMesIssDhcpSrvHostInterfaceBootServerAddress_Type = IpAddress
_EltMesIssDhcpSrvHostInterfaceBootServerAddress_Object = MibTableColumn
eltMesIssDhcpSrvHostInterfaceBootServerAddress = _EltMesIssDhcpSrvHostInterfaceBootServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 33, 1, 2, 2, 1, 4),
    _EltMesIssDhcpSrvHostInterfaceBootServerAddress_Type()
)
eltMesIssDhcpSrvHostInterfaceBootServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssDhcpSrvHostInterfaceBootServerAddress.setStatus("current")
_EltMesIssDhcpSrvHostInterfaceConfigRowStatus_Type = RowStatus
_EltMesIssDhcpSrvHostInterfaceConfigRowStatus_Object = MibTableColumn
eltMesIssDhcpSrvHostInterfaceConfigRowStatus = _EltMesIssDhcpSrvHostInterfaceConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 33, 1, 2, 2, 1, 5),
    _EltMesIssDhcpSrvHostInterfaceConfigRowStatus_Type()
)
eltMesIssDhcpSrvHostInterfaceConfigRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssDhcpSrvHostInterfaceConfigRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-ISS-DHCP-SRV-MIB",
    **{"eltMesIssDhcpSrvMIB": eltMesIssDhcpSrvMIB,
       "eltMesIssDhcpSrvObjects": eltMesIssDhcpSrvObjects,
       "eltMesIssDhcpSrvGlobals": eltMesIssDhcpSrvGlobals,
       "eltMesIssDhcpSrvConfig": eltMesIssDhcpSrvConfig,
       "eltMesIssDhcpSrvHostInterfaceOptTable": eltMesIssDhcpSrvHostInterfaceOptTable,
       "eltMesIssDhcpSrvHostInterfaceOptEntry": eltMesIssDhcpSrvHostInterfaceOptEntry,
       "eltMesIssDhcpSrvHostInterfaceIfIndex": eltMesIssDhcpSrvHostInterfaceIfIndex,
       "eltMesIssDhcpSrvHostInterfaceOptType": eltMesIssDhcpSrvHostInterfaceOptType,
       "eltMesIssDhcpSrvHostInterfaceOptLen": eltMesIssDhcpSrvHostInterfaceOptLen,
       "eltMesIssDhcpSrvHostInterfaceOptVal": eltMesIssDhcpSrvHostInterfaceOptVal,
       "eltMesIssDhcpSrvHostInterfaceOptRowStatus": eltMesIssDhcpSrvHostInterfaceOptRowStatus,
       "eltMesIssDhcpSrvHostInterfaceConfigTable": eltMesIssDhcpSrvHostInterfaceConfigTable,
       "eltMesIssDhcpSrvHostInterfaceConfigEntry": eltMesIssDhcpSrvHostInterfaceConfigEntry,
       "eltMesIssDhcpSrvHostInterfaceIpAddress": eltMesIssDhcpSrvHostInterfaceIpAddress,
       "eltMesIssDhcpSrvHostInterfacePoolName": eltMesIssDhcpSrvHostInterfacePoolName,
       "eltMesIssDhcpSrvHostInterfaceBootFileName": eltMesIssDhcpSrvHostInterfaceBootFileName,
       "eltMesIssDhcpSrvHostInterfaceBootServerAddress": eltMesIssDhcpSrvHostInterfaceBootServerAddress,
       "eltMesIssDhcpSrvHostInterfaceConfigRowStatus": eltMesIssDhcpSrvHostInterfaceConfigRowStatus}
)
