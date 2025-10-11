# SNMP MIB module (ZXCESOE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZXCESOE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:33 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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

(zxPwCETH,) = mibBuilder.importSymbols(
    "ZTE-MASTER-MIB",
    "zxPwCETH")

(zxPwIndex,) = mibBuilder.importSymbols(
    "ZXPW-STD-MIB",
    "zxPwIndex")

(PwVlanCfg,) = mibBuilder.importSymbols(
    "ZXPW-TC-STD-MIB",
    "PwVlanCfg")


# MODULE-IDENTITY

zxCesoeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 3, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxCesoeCfgTable_Object = MibTable
zxCesoeCfgTable = _ZxCesoeCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    zxCesoeCfgTable.setStatus("current")
_ZxCesoeCfgEntry_Object = MibTableRow
zxCesoeCfgEntry = _ZxCesoeCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 3, 1, 2, 1, 1)
)
zxCesoeCfgEntry.setIndexNames(
    (0, "ZXPW-STD-MIB", "zxPwIndex"),
)
if mibBuilder.loadTexts:
    zxCesoeCfgEntry.setStatus("current")
_ZxCesoeCfgDstMac_Type = MacAddress
_ZxCesoeCfgDstMac_Object = MibTableColumn
zxCesoeCfgDstMac = _ZxCesoeCfgDstMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 3, 1, 2, 1, 1, 1),
    _ZxCesoeCfgDstMac_Type()
)
zxCesoeCfgDstMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxCesoeCfgDstMac.setStatus("current")
_ZxCesoeCfgCardIfIndex_Type = InterfaceIndexOrZero
_ZxCesoeCfgCardIfIndex_Object = MibTableColumn
zxCesoeCfgCardIfIndex = _ZxCesoeCfgCardIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 3, 1, 2, 1, 1, 2),
    _ZxCesoeCfgCardIfIndex_Type()
)
zxCesoeCfgCardIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxCesoeCfgCardIfIndex.setStatus("current")


class _ZxCesoeCfgVlanId_Type(PwVlanCfg):
    """Custom type zxCesoeCfgVlanId based on PwVlanCfg"""
    defaultValue = 1


_ZxCesoeCfgVlanId_Type.__name__ = "PwVlanCfg"
_ZxCesoeCfgVlanId_Object = MibTableColumn
zxCesoeCfgVlanId = _ZxCesoeCfgVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 3, 1, 2, 1, 1, 3),
    _ZxCesoeCfgVlanId_Type()
)
zxCesoeCfgVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxCesoeCfgVlanId.setStatus("current")
_ZxCesoeCfgPrio_Type = Integer32
_ZxCesoeCfgPrio_Object = MibTableColumn
zxCesoeCfgPrio = _ZxCesoeCfgPrio_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 3, 1, 2, 1, 1, 4),
    _ZxCesoeCfgPrio_Type()
)
zxCesoeCfgPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxCesoeCfgPrio.setStatus("current")
_ZxCesoeCfgRowStatus_Type = RowStatus
_ZxCesoeCfgRowStatus_Object = MibTableColumn
zxCesoeCfgRowStatus = _ZxCesoeCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 3, 1, 2, 1, 1, 5),
    _ZxCesoeCfgRowStatus_Type()
)
zxCesoeCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxCesoeCfgRowStatus.setStatus("current")


class _ZxCesoeCfgCVlanId_Type(PwVlanCfg):
    """Custom type zxCesoeCfgCVlanId based on PwVlanCfg"""
    defaultValue = 1


_ZxCesoeCfgCVlanId_Type.__name__ = "PwVlanCfg"
_ZxCesoeCfgCVlanId_Object = MibTableColumn
zxCesoeCfgCVlanId = _ZxCesoeCfgCVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 3, 1, 2, 1, 1, 6),
    _ZxCesoeCfgCVlanId_Type()
)
zxCesoeCfgCVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxCesoeCfgCVlanId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXCESOE-MIB",
    **{"zxCesoeMIB": zxCesoeMIB,
       "zxCesoeCfgTable": zxCesoeCfgTable,
       "zxCesoeCfgEntry": zxCesoeCfgEntry,
       "zxCesoeCfgDstMac": zxCesoeCfgDstMac,
       "zxCesoeCfgCardIfIndex": zxCesoeCfgCardIfIndex,
       "zxCesoeCfgVlanId": zxCesoeCfgVlanId,
       "zxCesoeCfgPrio": zxCesoeCfgPrio,
       "zxCesoeCfgRowStatus": zxCesoeCfgRowStatus,
       "zxCesoeCfgCVlanId": zxCesoeCfgCVlanId}
)
