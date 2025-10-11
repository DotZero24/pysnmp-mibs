# SNMP MIB module (H3C-QINQV2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-QINQV2-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:19:21 2025
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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

h3cQinQv2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 137)
)
if mibBuilder.loadTexts:
    h3cQinQv2.setRevisions(
        ("2013-03-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cQinQv2MibObject_ObjectIdentity = ObjectIdentity
h3cQinQv2MibObject = _H3cQinQv2MibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 137, 1)
)
_H3cQinQv2ScalarObjects_ObjectIdentity = ObjectIdentity
h3cQinQv2ScalarObjects = _H3cQinQv2ScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 137, 1, 1)
)


class _H3cQinQv2ServiceTPID_Type(Integer32):
    """Custom type h3cQinQv2ServiceTPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cQinQv2ServiceTPID_Type.__name__ = "Integer32"
_H3cQinQv2ServiceTPID_Object = MibScalar
h3cQinQv2ServiceTPID = _H3cQinQv2ServiceTPID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 137, 1, 1, 1),
    _H3cQinQv2ServiceTPID_Type()
)
h3cQinQv2ServiceTPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cQinQv2ServiceTPID.setStatus("current")


class _H3cQinQv2CustomerTPID_Type(Integer32):
    """Custom type h3cQinQv2CustomerTPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cQinQv2CustomerTPID_Type.__name__ = "Integer32"
_H3cQinQv2CustomerTPID_Object = MibScalar
h3cQinQv2CustomerTPID = _H3cQinQv2CustomerTPID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 137, 1, 1, 2),
    _H3cQinQv2CustomerTPID_Type()
)
h3cQinQv2CustomerTPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cQinQv2CustomerTPID.setStatus("current")
_H3cQinQv2IfCfgTable_Object = MibTable
h3cQinQv2IfCfgTable = _H3cQinQv2IfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 137, 1, 2)
)
if mibBuilder.loadTexts:
    h3cQinQv2IfCfgTable.setStatus("current")
_H3cQinQv2IfCfgEntry_Object = MibTableRow
h3cQinQv2IfCfgEntry = _H3cQinQv2IfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 137, 1, 2, 1)
)
h3cQinQv2IfCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cQinQv2IfCfgEntry.setStatus("current")


class _H3cQinQv2IfState_Type(TruthValue):
    """Custom type h3cQinQv2IfState based on TruthValue"""
    defaultValue = 2


_H3cQinQv2IfState_Type.__name__ = "TruthValue"
_H3cQinQv2IfState_Object = MibTableColumn
h3cQinQv2IfState = _H3cQinQv2IfState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 137, 1, 2, 1, 1),
    _H3cQinQv2IfState_Type()
)
h3cQinQv2IfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cQinQv2IfState.setStatus("current")


class _H3cQinQv2IfServiceTPID_Type(Integer32):
    """Custom type h3cQinQv2IfServiceTPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cQinQv2IfServiceTPID_Type.__name__ = "Integer32"
_H3cQinQv2IfServiceTPID_Object = MibTableColumn
h3cQinQv2IfServiceTPID = _H3cQinQv2IfServiceTPID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 137, 1, 2, 1, 2),
    _H3cQinQv2IfServiceTPID_Type()
)
h3cQinQv2IfServiceTPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cQinQv2IfServiceTPID.setStatus("current")


class _H3cQinQv2IfCustomerTPID_Type(Integer32):
    """Custom type h3cQinQv2IfCustomerTPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cQinQv2IfCustomerTPID_Type.__name__ = "Integer32"
_H3cQinQv2IfCustomerTPID_Object = MibTableColumn
h3cQinQv2IfCustomerTPID = _H3cQinQv2IfCustomerTPID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 137, 1, 2, 1, 3),
    _H3cQinQv2IfCustomerTPID_Type()
)
h3cQinQv2IfCustomerTPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cQinQv2IfCustomerTPID.setStatus("current")


class _H3cQinQv2IfTransVlanList_Type(OctetString):
    """Custom type h3cQinQv2IfTransVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512


_H3cQinQv2IfTransVlanList_Type.__name__ = "OctetString"
_H3cQinQv2IfTransVlanList_Object = MibTableColumn
h3cQinQv2IfTransVlanList = _H3cQinQv2IfTransVlanList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 137, 1, 2, 1, 4),
    _H3cQinQv2IfTransVlanList_Type()
)
h3cQinQv2IfTransVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cQinQv2IfTransVlanList.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-QINQV2-MIB",
    **{"h3cQinQv2": h3cQinQv2,
       "h3cQinQv2MibObject": h3cQinQv2MibObject,
       "h3cQinQv2ScalarObjects": h3cQinQv2ScalarObjects,
       "h3cQinQv2ServiceTPID": h3cQinQv2ServiceTPID,
       "h3cQinQv2CustomerTPID": h3cQinQv2CustomerTPID,
       "h3cQinQv2IfCfgTable": h3cQinQv2IfCfgTable,
       "h3cQinQv2IfCfgEntry": h3cQinQv2IfCfgEntry,
       "h3cQinQv2IfState": h3cQinQv2IfState,
       "h3cQinQv2IfServiceTPID": h3cQinQv2IfServiceTPID,
       "h3cQinQv2IfCustomerTPID": h3cQinQv2IfCustomerTPID,
       "h3cQinQv2IfTransVlanList": h3cQinQv2IfTransVlanList}
)
