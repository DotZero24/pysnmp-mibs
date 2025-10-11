# SNMP MIB module (SWITCH-MACCONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/SWITCH-MACCONFIG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:37:28 2025
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

rcMacConfig = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EnableVar(TextualConvention, Integer32):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_RcStaticMacTable_Object = MibTable
rcStaticMacTable = _RcStaticMacTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 3, 1)
)
if mibBuilder.loadTexts:
    rcStaticMacTable.setStatus("current")
_RcStaticMacEntry_Object = MibTableRow
rcStaticMacEntry = _RcStaticMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 3, 1, 1)
)
rcStaticMacEntry.setIndexNames(
    (0, "SWITCH-MACCONFIG-MIB", "rcStaticMacVlan"),
    (0, "SWITCH-MACCONFIG-MIB", "rcStaticMacAddress"),
)
if mibBuilder.loadTexts:
    rcStaticMacEntry.setStatus("current")


class _RcStaticMacVlan_Type(Integer32):
    """Custom type rcStaticMacVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RcStaticMacVlan_Type.__name__ = "Integer32"
_RcStaticMacVlan_Object = MibTableColumn
rcStaticMacVlan = _RcStaticMacVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 3, 1, 1, 1),
    _RcStaticMacVlan_Type()
)
rcStaticMacVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcStaticMacVlan.setStatus("current")
_RcStaticMacAddress_Type = MacAddress
_RcStaticMacAddress_Object = MibTableColumn
rcStaticMacAddress = _RcStaticMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 3, 1, 1, 2),
    _RcStaticMacAddress_Type()
)
rcStaticMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcStaticMacAddress.setStatus("current")
_RcStaticMacPort_Type = Integer32
_RcStaticMacPort_Object = MibTableColumn
rcStaticMacPort = _RcStaticMacPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 3, 1, 1, 3),
    _RcStaticMacPort_Type()
)
rcStaticMacPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcStaticMacPort.setStatus("current")
_RcStaticMacRowStatus_Type = RowStatus
_RcStaticMacRowStatus_Object = MibTableColumn
rcStaticMacRowStatus = _RcStaticMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 3, 1, 1, 4),
    _RcStaticMacRowStatus_Type()
)
rcStaticMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcStaticMacRowStatus.setStatus("current")


class _RcStaticMacPriority_Type(Integer32):
    """Custom type rcStaticMacPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_RcStaticMacPriority_Type.__name__ = "Integer32"
_RcStaticMacPriority_Object = MibTableColumn
rcStaticMacPriority = _RcStaticMacPriority_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 3, 1, 1, 5),
    _RcStaticMacPriority_Type()
)
rcStaticMacPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcStaticMacPriority.setStatus("current")
_RcStaticMacPolicyEnable_Type = EnableVar
_RcStaticMacPolicyEnable_Object = MibTableColumn
rcStaticMacPolicyEnable = _RcStaticMacPolicyEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 3, 1, 1, 6),
    _RcStaticMacPolicyEnable_Type()
)
rcStaticMacPolicyEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcStaticMacPolicyEnable.setStatus("current")
_RcStaticMacNrlEnable_Type = EnableVar
_RcStaticMacNrlEnable_Object = MibTableColumn
rcStaticMacNrlEnable = _RcStaticMacNrlEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 3, 1, 1, 7),
    _RcStaticMacNrlEnable_Type()
)
rcStaticMacNrlEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcStaticMacNrlEnable.setStatus("current")
_RcStaticMacBhEnable_Type = EnableVar
_RcStaticMacBhEnable_Object = MibTableColumn
rcStaticMacBhEnable = _RcStaticMacBhEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 3, 1, 1, 8),
    _RcStaticMacBhEnable_Type()
)
rcStaticMacBhEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcStaticMacBhEnable.setStatus("current")
_RcMacCountGroup_ObjectIdentity = ObjectIdentity
rcMacCountGroup = _RcMacCountGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 3, 2)
)
_RcQueryMacCountPort_Type = Integer32
_RcQueryMacCountPort_Object = MibScalar
rcQueryMacCountPort = _RcQueryMacCountPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 3, 2, 1),
    _RcQueryMacCountPort_Type()
)
rcQueryMacCountPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQueryMacCountPort.setStatus("current")


class _RcQueryMacCountVlan_Type(Integer32):
    """Custom type rcQueryMacCountVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_RcQueryMacCountVlan_Type.__name__ = "Integer32"
_RcQueryMacCountVlan_Object = MibScalar
rcQueryMacCountVlan = _RcQueryMacCountVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 3, 2, 2),
    _RcQueryMacCountVlan_Type()
)
rcQueryMacCountVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQueryMacCountVlan.setStatus("current")
_RcQueryMacCount_Type = Integer32
_RcQueryMacCount_Object = MibScalar
rcQueryMacCount = _RcQueryMacCount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 3, 2, 3),
    _RcQueryMacCount_Type()
)
rcQueryMacCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQueryMacCount.setStatus("current")
_RcQueryMacTable_Type = Integer32
_RcQueryMacTable_Object = MibScalar
rcQueryMacTable = _RcQueryMacTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 3, 2, 4),
    _RcQueryMacTable_Type()
)
rcQueryMacTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcQueryMacTable.setStatus("current")
_RcStaticMacPortTable_Object = MibTable
rcStaticMacPortTable = _RcStaticMacPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 3, 3)
)
if mibBuilder.loadTexts:
    rcStaticMacPortTable.setStatus("current")
_RcStaticMacPortEntry_Object = MibTableRow
rcStaticMacPortEntry = _RcStaticMacPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 3, 3, 1)
)
rcStaticMacPortEntry.setIndexNames(
    (0, "SWITCH-MACCONFIG-MIB", "rcPort"),
)
if mibBuilder.loadTexts:
    rcStaticMacPortEntry.setStatus("current")
_RcPort_Type = Integer32
_RcPort_Object = MibTableColumn
rcPort = _RcPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 3, 3, 1, 1),
    _RcPort_Type()
)
rcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcPort.setStatus("current")


class _RcStaticSmacPolicy_Type(Integer32):
    """Custom type rcStaticSmacPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal-transmit", 0),
          ("drop", 1),
          ("mirror", 2))
    )


_RcStaticSmacPolicy_Type.__name__ = "Integer32"
_RcStaticSmacPolicy_Object = MibTableColumn
rcStaticSmacPolicy = _RcStaticSmacPolicy_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 3, 3, 1, 2),
    _RcStaticSmacPolicy_Type()
)
rcStaticSmacPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcStaticSmacPolicy.setStatus("current")


class _RcStaticDmacPolicy_Type(Integer32):
    """Custom type rcStaticDmacPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal-transmit", 0),
          ("drop", 1),
          ("mirror", 2))
    )


_RcStaticDmacPolicy_Type.__name__ = "Integer32"
_RcStaticDmacPolicy_Object = MibTableColumn
rcStaticDmacPolicy = _RcStaticDmacPolicy_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 3, 3, 1, 3),
    _RcStaticDmacPolicy_Type()
)
rcStaticDmacPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcStaticDmacPolicy.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWITCH-MACCONFIG-MIB",
    **{"EnableVar": EnableVar,
       "rcMacConfig": rcMacConfig,
       "rcStaticMacTable": rcStaticMacTable,
       "rcStaticMacEntry": rcStaticMacEntry,
       "rcStaticMacVlan": rcStaticMacVlan,
       "rcStaticMacAddress": rcStaticMacAddress,
       "rcStaticMacPort": rcStaticMacPort,
       "rcStaticMacRowStatus": rcStaticMacRowStatus,
       "rcStaticMacPriority": rcStaticMacPriority,
       "rcStaticMacPolicyEnable": rcStaticMacPolicyEnable,
       "rcStaticMacNrlEnable": rcStaticMacNrlEnable,
       "rcStaticMacBhEnable": rcStaticMacBhEnable,
       "rcMacCountGroup": rcMacCountGroup,
       "rcQueryMacCountPort": rcQueryMacCountPort,
       "rcQueryMacCountVlan": rcQueryMacCountVlan,
       "rcQueryMacCount": rcQueryMacCount,
       "rcQueryMacTable": rcQueryMacTable,
       "rcStaticMacPortTable": rcStaticMacPortTable,
       "rcStaticMacPortEntry": rcStaticMacPortEntry,
       "rcPort": rcPort,
       "rcStaticSmacPolicy": rcStaticSmacPolicy,
       "rcStaticDmacPolicy": rcStaticDmacPolicy}
)
