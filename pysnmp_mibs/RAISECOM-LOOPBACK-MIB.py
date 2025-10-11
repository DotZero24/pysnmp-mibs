# SNMP MIB module (RAISECOM-LOOPBACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-LOOPBACK-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:35:55 2025
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

(iscomSwitch,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "iscomSwitch")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

rcLoopback = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 73)
)
if mibBuilder.loadTexts:
    rcLoopback.setRevisions(
        ("2012-08-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcLoopbackPortTable_Object = MibTable
rcLoopbackPortTable = _RcLoopbackPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 73, 1)
)
if mibBuilder.loadTexts:
    rcLoopbackPortTable.setStatus("current")
_RcLoopbackPortEntry_Object = MibTableRow
rcLoopbackPortEntry = _RcLoopbackPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 73, 1, 1)
)
rcLoopbackPortEntry.setIndexNames(
    (0, "RAISECOM-LOOPBACK-MIB", "rcLoopbackPortIndex"),
)
if mibBuilder.loadTexts:
    rcLoopbackPortEntry.setStatus("current")
_RcLoopbackPortIndex_Type = Integer32
_RcLoopbackPortIndex_Object = MibTableColumn
rcLoopbackPortIndex = _RcLoopbackPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 73, 1, 1, 1),
    _RcLoopbackPortIndex_Type()
)
rcLoopbackPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcLoopbackPortIndex.setStatus("current")


class _RcLoopbackPortEnable_Type(Integer32):
    """Custom type rcLoopbackPortEnable based on Integer32"""
    defaultValue = 0

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


_RcLoopbackPortEnable_Type.__name__ = "Integer32"
_RcLoopbackPortEnable_Object = MibTableColumn
rcLoopbackPortEnable = _RcLoopbackPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 73, 1, 1, 2),
    _RcLoopbackPortEnable_Type()
)
rcLoopbackPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcLoopbackPortEnable.setStatus("current")


class _RcLoopbackPortMode_Type(Integer32):
    """Custom type rcLoopbackPortMode based on Integer32"""
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
        *(("l1", 1),
          ("l2", 2),
          ("l3", 3))
    )


_RcLoopbackPortMode_Type.__name__ = "Integer32"
_RcLoopbackPortMode_Object = MibTableColumn
rcLoopbackPortMode = _RcLoopbackPortMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 73, 1, 1, 3),
    _RcLoopbackPortMode_Type()
)
rcLoopbackPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcLoopbackPortMode.setStatus("current")
_RcLoopbackPortStatistics_Type = Counter32
_RcLoopbackPortStatistics_Object = MibTableColumn
rcLoopbackPortStatistics = _RcLoopbackPortStatistics_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 73, 1, 1, 4),
    _RcLoopbackPortStatistics_Type()
)
rcLoopbackPortStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcLoopbackPortStatistics.setStatus("current")


class _RcLoopbackPortClearStatistics_Type(Integer32):
    """Custom type rcLoopbackPortClearStatistics based on Integer32"""
    defaultValue = 0

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


_RcLoopbackPortClearStatistics_Type.__name__ = "Integer32"
_RcLoopbackPortClearStatistics_Object = MibTableColumn
rcLoopbackPortClearStatistics = _RcLoopbackPortClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 73, 1, 1, 5),
    _RcLoopbackPortClearStatistics_Type()
)
rcLoopbackPortClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcLoopbackPortClearStatistics.setStatus("current")
_RcLoopbackPortSmac_Type = MacAddress
_RcLoopbackPortSmac_Object = MibTableColumn
rcLoopbackPortSmac = _RcLoopbackPortSmac_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 73, 1, 1, 6),
    _RcLoopbackPortSmac_Type()
)
rcLoopbackPortSmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcLoopbackPortSmac.setStatus("current")
_RcLoopbackPortProtocol_Type = Integer32
_RcLoopbackPortProtocol_Object = MibTableColumn
rcLoopbackPortProtocol = _RcLoopbackPortProtocol_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 73, 1, 1, 7),
    _RcLoopbackPortProtocol_Type()
)
rcLoopbackPortProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcLoopbackPortProtocol.setStatus("current")


class _RcLoopbackPortVlan_Type(Integer32):
    """Custom type rcLoopbackPortVlan based on Integer32"""
    defaultValue = 1


_RcLoopbackPortVlan_Type.__name__ = "Integer32"
_RcLoopbackPortVlan_Object = MibTableColumn
rcLoopbackPortVlan = _RcLoopbackPortVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 73, 1, 1, 8),
    _RcLoopbackPortVlan_Type()
)
rcLoopbackPortVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcLoopbackPortVlan.setStatus("current")
_RcL2LoopbackPortTable_Object = MibTable
rcL2LoopbackPortTable = _RcL2LoopbackPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 73, 2)
)
if mibBuilder.loadTexts:
    rcL2LoopbackPortTable.setStatus("current")
_RcL2LoopbackPortEntry_Object = MibTableRow
rcL2LoopbackPortEntry = _RcL2LoopbackPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 73, 2, 1)
)
rcL2LoopbackPortEntry.setIndexNames(
    (0, "RAISECOM-LOOPBACK-MIB", "rcLoopbackPortIndex"),
    (0, "RAISECOM-LOOPBACK-MIB", "rcL2LoopbackPortNum"),
)
if mibBuilder.loadTexts:
    rcL2LoopbackPortEntry.setStatus("current")
_RcL2LoopbackPortNum_Type = Integer32
_RcL2LoopbackPortNum_Object = MibTableColumn
rcL2LoopbackPortNum = _RcL2LoopbackPortNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 73, 2, 1, 1),
    _RcL2LoopbackPortNum_Type()
)
rcL2LoopbackPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcL2LoopbackPortNum.setStatus("current")
_RcL2LoopbackPortStatistics_Type = Counter32
_RcL2LoopbackPortStatistics_Object = MibTableColumn
rcL2LoopbackPortStatistics = _RcL2LoopbackPortStatistics_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 73, 2, 1, 2),
    _RcL2LoopbackPortStatistics_Type()
)
rcL2LoopbackPortStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcL2LoopbackPortStatistics.setStatus("current")
_RcL2LoopbackPortSmac_Type = MacAddress
_RcL2LoopbackPortSmac_Object = MibTableColumn
rcL2LoopbackPortSmac = _RcL2LoopbackPortSmac_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 73, 2, 1, 3),
    _RcL2LoopbackPortSmac_Type()
)
rcL2LoopbackPortSmac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcL2LoopbackPortSmac.setStatus("current")
_RcL2LoopbackPortProtocol_Type = Integer32
_RcL2LoopbackPortProtocol_Object = MibTableColumn
rcL2LoopbackPortProtocol = _RcL2LoopbackPortProtocol_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 73, 2, 1, 4),
    _RcL2LoopbackPortProtocol_Type()
)
rcL2LoopbackPortProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcL2LoopbackPortProtocol.setStatus("current")


class _RcL2LoopbackPortVlan_Type(Integer32):
    """Custom type rcL2LoopbackPortVlan based on Integer32"""
    defaultValue = 1


_RcL2LoopbackPortVlan_Type.__name__ = "Integer32"
_RcL2LoopbackPortVlan_Object = MibTableColumn
rcL2LoopbackPortVlan = _RcL2LoopbackPortVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 73, 2, 1, 5),
    _RcL2LoopbackPortVlan_Type()
)
rcL2LoopbackPortVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcL2LoopbackPortVlan.setStatus("current")
_RcL2LoopbackPortStatus_Type = RowStatus
_RcL2LoopbackPortStatus_Object = MibTableColumn
rcL2LoopbackPortStatus = _RcL2LoopbackPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 73, 2, 1, 6),
    _RcL2LoopbackPortStatus_Type()
)
rcL2LoopbackPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcL2LoopbackPortStatus.setStatus("current")
_RcL3LoopbackPortTable_Object = MibTable
rcL3LoopbackPortTable = _RcL3LoopbackPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 73, 3)
)
if mibBuilder.loadTexts:
    rcL3LoopbackPortTable.setStatus("current")
_RcL3LoopbackPortEntry_Object = MibTableRow
rcL3LoopbackPortEntry = _RcL3LoopbackPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 73, 3, 1)
)
rcL3LoopbackPortEntry.setIndexNames(
    (0, "RAISECOM-LOOPBACK-MIB", "rcLoopbackPortIndex"),
    (0, "RAISECOM-LOOPBACK-MIB", "rcL3LoopbackPortNum"),
)
if mibBuilder.loadTexts:
    rcL3LoopbackPortEntry.setStatus("current")
_RcL3LoopbackPortNum_Type = Integer32
_RcL3LoopbackPortNum_Object = MibTableColumn
rcL3LoopbackPortNum = _RcL3LoopbackPortNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 73, 3, 1, 1),
    _RcL3LoopbackPortNum_Type()
)
rcL3LoopbackPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcL3LoopbackPortNum.setStatus("current")
_RcL3LoopbackPortDestAddr_Type = IpAddress
_RcL3LoopbackPortDestAddr_Object = MibTableColumn
rcL3LoopbackPortDestAddr = _RcL3LoopbackPortDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 73, 3, 1, 2),
    _RcL3LoopbackPortDestAddr_Type()
)
rcL3LoopbackPortDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcL3LoopbackPortDestAddr.setStatus("current")
_RcL3LoopbackPortMAC_Type = MacAddress
_RcL3LoopbackPortMAC_Object = MibTableColumn
rcL3LoopbackPortMAC = _RcL3LoopbackPortMAC_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 73, 3, 1, 3),
    _RcL3LoopbackPortMAC_Type()
)
rcL3LoopbackPortMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcL3LoopbackPortMAC.setStatus("current")


class _RcL3LoopbackPortSvlan_Type(Integer32):
    """Custom type rcL3LoopbackPortSvlan based on Integer32"""
    defaultValue = 1


_RcL3LoopbackPortSvlan_Type.__name__ = "Integer32"
_RcL3LoopbackPortSvlan_Object = MibTableColumn
rcL3LoopbackPortSvlan = _RcL3LoopbackPortSvlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 73, 3, 1, 4),
    _RcL3LoopbackPortSvlan_Type()
)
rcL3LoopbackPortSvlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcL3LoopbackPortSvlan.setStatus("current")


class _RcL3LoopbackPortCvlan_Type(Integer32):
    """Custom type rcL3LoopbackPortCvlan based on Integer32"""
    defaultValue = 1


_RcL3LoopbackPortCvlan_Type.__name__ = "Integer32"
_RcL3LoopbackPortCvlan_Object = MibTableColumn
rcL3LoopbackPortCvlan = _RcL3LoopbackPortCvlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 73, 3, 1, 5),
    _RcL3LoopbackPortCvlan_Type()
)
rcL3LoopbackPortCvlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcL3LoopbackPortCvlan.setStatus("current")


class _RcL3LoopbackPortDscp_Type(Integer32):
    """Custom type rcL3LoopbackPortDscp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RcL3LoopbackPortDscp_Type.__name__ = "Integer32"
_RcL3LoopbackPortDscp_Object = MibTableColumn
rcL3LoopbackPortDscp = _RcL3LoopbackPortDscp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 73, 3, 1, 6),
    _RcL3LoopbackPortDscp_Type()
)
rcL3LoopbackPortDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcL3LoopbackPortDscp.setStatus("current")
_RcL3LoopbackPortStatus_Type = RowStatus
_RcL3LoopbackPortStatus_Object = MibTableColumn
rcL3LoopbackPortStatus = _RcL3LoopbackPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 73, 3, 1, 7),
    _RcL3LoopbackPortStatus_Type()
)
rcL3LoopbackPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcL3LoopbackPortStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-LOOPBACK-MIB",
    **{"rcLoopback": rcLoopback,
       "rcLoopbackPortTable": rcLoopbackPortTable,
       "rcLoopbackPortEntry": rcLoopbackPortEntry,
       "rcLoopbackPortIndex": rcLoopbackPortIndex,
       "rcLoopbackPortEnable": rcLoopbackPortEnable,
       "rcLoopbackPortMode": rcLoopbackPortMode,
       "rcLoopbackPortStatistics": rcLoopbackPortStatistics,
       "rcLoopbackPortClearStatistics": rcLoopbackPortClearStatistics,
       "rcLoopbackPortSmac": rcLoopbackPortSmac,
       "rcLoopbackPortProtocol": rcLoopbackPortProtocol,
       "rcLoopbackPortVlan": rcLoopbackPortVlan,
       "rcL2LoopbackPortTable": rcL2LoopbackPortTable,
       "rcL2LoopbackPortEntry": rcL2LoopbackPortEntry,
       "rcL2LoopbackPortNum": rcL2LoopbackPortNum,
       "rcL2LoopbackPortStatistics": rcL2LoopbackPortStatistics,
       "rcL2LoopbackPortSmac": rcL2LoopbackPortSmac,
       "rcL2LoopbackPortProtocol": rcL2LoopbackPortProtocol,
       "rcL2LoopbackPortVlan": rcL2LoopbackPortVlan,
       "rcL2LoopbackPortStatus": rcL2LoopbackPortStatus,
       "rcL3LoopbackPortTable": rcL3LoopbackPortTable,
       "rcL3LoopbackPortEntry": rcL3LoopbackPortEntry,
       "rcL3LoopbackPortNum": rcL3LoopbackPortNum,
       "rcL3LoopbackPortDestAddr": rcL3LoopbackPortDestAddr,
       "rcL3LoopbackPortMAC": rcL3LoopbackPortMAC,
       "rcL3LoopbackPortSvlan": rcL3LoopbackPortSvlan,
       "rcL3LoopbackPortCvlan": rcL3LoopbackPortCvlan,
       "rcL3LoopbackPortDscp": rcL3LoopbackPortDscp,
       "rcL3LoopbackPortStatus": rcL3LoopbackPortStatus}
)
