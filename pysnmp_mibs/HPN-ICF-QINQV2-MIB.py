# SNMP MIB module (HPN-ICF-QINQV2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/HPN-ICF-QINQV2-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:38:41 2025
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

hpnicfQinQv2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 137)
)
if mibBuilder.loadTexts:
    hpnicfQinQv2.setRevisions(
        ("2013-03-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfQinQv2MibObject_ObjectIdentity = ObjectIdentity
hpnicfQinQv2MibObject = _HpnicfQinQv2MibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 137, 1)
)
_HpnicfQinQv2ScalarObjects_ObjectIdentity = ObjectIdentity
hpnicfQinQv2ScalarObjects = _HpnicfQinQv2ScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 137, 1, 1)
)


class _HpnicfQinQv2ServiceTPID_Type(Integer32):
    """Custom type hpnicfQinQv2ServiceTPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfQinQv2ServiceTPID_Type.__name__ = "Integer32"
_HpnicfQinQv2ServiceTPID_Object = MibScalar
hpnicfQinQv2ServiceTPID = _HpnicfQinQv2ServiceTPID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 137, 1, 1, 1),
    _HpnicfQinQv2ServiceTPID_Type()
)
hpnicfQinQv2ServiceTPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfQinQv2ServiceTPID.setStatus("current")


class _HpnicfQinQv2CustomerTPID_Type(Integer32):
    """Custom type hpnicfQinQv2CustomerTPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfQinQv2CustomerTPID_Type.__name__ = "Integer32"
_HpnicfQinQv2CustomerTPID_Object = MibScalar
hpnicfQinQv2CustomerTPID = _HpnicfQinQv2CustomerTPID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 137, 1, 1, 2),
    _HpnicfQinQv2CustomerTPID_Type()
)
hpnicfQinQv2CustomerTPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfQinQv2CustomerTPID.setStatus("current")
_HpnicfQinQv2IfCfgTable_Object = MibTable
hpnicfQinQv2IfCfgTable = _HpnicfQinQv2IfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 137, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfQinQv2IfCfgTable.setStatus("current")
_HpnicfQinQv2IfCfgEntry_Object = MibTableRow
hpnicfQinQv2IfCfgEntry = _HpnicfQinQv2IfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 137, 1, 2, 1)
)
hpnicfQinQv2IfCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfQinQv2IfCfgEntry.setStatus("current")


class _HpnicfQinQv2IfState_Type(TruthValue):
    """Custom type hpnicfQinQv2IfState based on TruthValue"""
    defaultValue = 2


_HpnicfQinQv2IfState_Type.__name__ = "TruthValue"
_HpnicfQinQv2IfState_Object = MibTableColumn
hpnicfQinQv2IfState = _HpnicfQinQv2IfState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 137, 1, 2, 1, 1),
    _HpnicfQinQv2IfState_Type()
)
hpnicfQinQv2IfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfQinQv2IfState.setStatus("current")


class _HpnicfQinQv2IfServiceTPID_Type(Integer32):
    """Custom type hpnicfQinQv2IfServiceTPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfQinQv2IfServiceTPID_Type.__name__ = "Integer32"
_HpnicfQinQv2IfServiceTPID_Object = MibTableColumn
hpnicfQinQv2IfServiceTPID = _HpnicfQinQv2IfServiceTPID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 137, 1, 2, 1, 2),
    _HpnicfQinQv2IfServiceTPID_Type()
)
hpnicfQinQv2IfServiceTPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfQinQv2IfServiceTPID.setStatus("current")


class _HpnicfQinQv2IfCustomerTPID_Type(Integer32):
    """Custom type hpnicfQinQv2IfCustomerTPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfQinQv2IfCustomerTPID_Type.__name__ = "Integer32"
_HpnicfQinQv2IfCustomerTPID_Object = MibTableColumn
hpnicfQinQv2IfCustomerTPID = _HpnicfQinQv2IfCustomerTPID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 137, 1, 2, 1, 3),
    _HpnicfQinQv2IfCustomerTPID_Type()
)
hpnicfQinQv2IfCustomerTPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfQinQv2IfCustomerTPID.setStatus("current")


class _HpnicfQinQv2IfTransVlanList_Type(OctetString):
    """Custom type hpnicfQinQv2IfTransVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512


_HpnicfQinQv2IfTransVlanList_Type.__name__ = "OctetString"
_HpnicfQinQv2IfTransVlanList_Object = MibTableColumn
hpnicfQinQv2IfTransVlanList = _HpnicfQinQv2IfTransVlanList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 137, 1, 2, 1, 4),
    _HpnicfQinQv2IfTransVlanList_Type()
)
hpnicfQinQv2IfTransVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfQinQv2IfTransVlanList.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-QINQV2-MIB",
    **{"hpnicfQinQv2": hpnicfQinQv2,
       "hpnicfQinQv2MibObject": hpnicfQinQv2MibObject,
       "hpnicfQinQv2ScalarObjects": hpnicfQinQv2ScalarObjects,
       "hpnicfQinQv2ServiceTPID": hpnicfQinQv2ServiceTPID,
       "hpnicfQinQv2CustomerTPID": hpnicfQinQv2CustomerTPID,
       "hpnicfQinQv2IfCfgTable": hpnicfQinQv2IfCfgTable,
       "hpnicfQinQv2IfCfgEntry": hpnicfQinQv2IfCfgEntry,
       "hpnicfQinQv2IfState": hpnicfQinQv2IfState,
       "hpnicfQinQv2IfServiceTPID": hpnicfQinQv2IfServiceTPID,
       "hpnicfQinQv2IfCustomerTPID": hpnicfQinQv2IfCustomerTPID,
       "hpnicfQinQv2IfTransVlanList": hpnicfQinQv2IfTransVlanList}
)
