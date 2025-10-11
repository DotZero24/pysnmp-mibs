# SNMP MIB module (NETGEAR-RADLAN-BOOTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/netgear/NETGEAR-RADLAN-BOOTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:26:14 2025
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(rnd,) = mibBuilder.importSymbols(
    "NETGEAR-RADLAN-MIB",
    "rnd")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rndBootP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 17, 24)
)
if mibBuilder.loadTexts:
    rndBootP.setRevisions(
        ("2007-01-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _RndBootPServerAddress_Type(IpAddress):
    """Custom type rndBootPServerAddress based on IpAddress"""
    defaultHexValue = "00000000"


_RndBootPServerAddress_Type.__name__ = "IpAddress"
_RndBootPServerAddress_Object = MibScalar
rndBootPServerAddress = _RndBootPServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 17, 24, 1),
    _RndBootPServerAddress_Type()
)
rndBootPServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndBootPServerAddress.setStatus("current")
_RndBootPRelaySecThreshold_Type = Integer32
_RndBootPRelaySecThreshold_Object = MibScalar
rndBootPRelaySecThreshold = _RndBootPRelaySecThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4526, 17, 24, 2),
    _RndBootPRelaySecThreshold_Type()
)
rndBootPRelaySecThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndBootPRelaySecThreshold.setStatus("current")
_RndBootPActionTable_Object = MibTable
rndBootPActionTable = _RndBootPActionTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 17, 24, 3)
)
if mibBuilder.loadTexts:
    rndBootPActionTable.setStatus("current")
_RndBootPActionEntry_Object = MibTableRow
rndBootPActionEntry = _RndBootPActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 17, 24, 3, 1)
)
rndBootPActionEntry.setIndexNames(
    (0, "NETGEAR-RADLAN-BOOTP-MIB", "rndBootPActionIfIndex"),
)
if mibBuilder.loadTexts:
    rndBootPActionEntry.setStatus("current")
_RndBootPActionIfIndex_Type = InterfaceIndex
_RndBootPActionIfIndex_Object = MibTableColumn
rndBootPActionIfIndex = _RndBootPActionIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 17, 24, 3, 1, 1),
    _RndBootPActionIfIndex_Type()
)
rndBootPActionIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndBootPActionIfIndex.setStatus("current")
_RndBootPActionStatus_Type = RowStatus
_RndBootPActionStatus_Object = MibTableColumn
rndBootPActionStatus = _RndBootPActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 17, 24, 3, 1, 2),
    _RndBootPActionStatus_Type()
)
rndBootPActionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rndBootPActionStatus.setStatus("current")


class _RndBootPActionHostName_Type(SnmpAdminString):
    """Custom type rndBootPActionHostName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RndBootPActionHostName_Type.__name__ = "SnmpAdminString"
_RndBootPActionHostName_Object = MibTableColumn
rndBootPActionHostName = _RndBootPActionHostName_Object(
    (1, 3, 6, 1, 4, 1, 4526, 17, 24, 3, 1, 3),
    _RndBootPActionHostName_Type()
)
rndBootPActionHostName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rndBootPActionHostName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETGEAR-RADLAN-BOOTP-MIB",
    **{"rndBootP": rndBootP,
       "rndBootPServerAddress": rndBootPServerAddress,
       "rndBootPRelaySecThreshold": rndBootPRelaySecThreshold,
       "rndBootPActionTable": rndBootPActionTable,
       "rndBootPActionEntry": rndBootPActionEntry,
       "rndBootPActionIfIndex": rndBootPActionIfIndex,
       "rndBootPActionStatus": rndBootPActionStatus,
       "rndBootPActionHostName": rndBootPActionHostName}
)
