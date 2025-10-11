# SNMP MIB module (RC-QosPolicy-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/huawei/RC-QosPolicy-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:27:34 2025
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

(rc,) = mibBuilder.importSymbols(
    "RC-SMI",
    "rc")

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

rcQoSPolicy = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 65000, 3)
)
if mibBuilder.loadTexts:
    rcQoSPolicy.setRevisions(
        ("2015-03-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcQoSClassMapTable_Object = MibTable
rcQoSClassMapTable = _RcQoSClassMapTable_Object(
    (1, 3, 6, 1, 4, 1, 65000, 3, 1)
)
if mibBuilder.loadTexts:
    rcQoSClassMapTable.setStatus("current")
_RcQoSClassMapEntry_Object = MibTableRow
rcQoSClassMapEntry = _RcQoSClassMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 65000, 3, 1, 1)
)
rcQoSClassMapEntry.setIndexNames(
    (0, "RC-QosPolicy-MIB", "rcQoSClassMapname"),
    (0, "RC-QosPolicy-MIB", "rcQoSClassMapMatchACL"),
)
if mibBuilder.loadTexts:
    rcQoSClassMapEntry.setStatus("current")


class _RcQoSClassMapname_Type(DisplayString):
    """Custom type rcQoSClassMapname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_RcQoSClassMapname_Type.__name__ = "DisplayString"
_RcQoSClassMapname_Object = MibTableColumn
rcQoSClassMapname = _RcQoSClassMapname_Object(
    (1, 3, 6, 1, 4, 1, 65000, 3, 1, 1, 1),
    _RcQoSClassMapname_Type()
)
rcQoSClassMapname.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQoSClassMapname.setStatus("current")


class _RcQoSClassMapMatchACL_Type(DisplayString):
    """Custom type rcQoSClassMapMatchACL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_RcQoSClassMapMatchACL_Type.__name__ = "DisplayString"
_RcQoSClassMapMatchACL_Object = MibTableColumn
rcQoSClassMapMatchACL = _RcQoSClassMapMatchACL_Object(
    (1, 3, 6, 1, 4, 1, 65000, 3, 1, 1, 2),
    _RcQoSClassMapMatchACL_Type()
)
rcQoSClassMapMatchACL.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQoSClassMapMatchACL.setStatus("current")
_RcQoSClassMapRowSta_Type = RowStatus
_RcQoSClassMapRowSta_Object = MibTableColumn
rcQoSClassMapRowSta = _RcQoSClassMapRowSta_Object(
    (1, 3, 6, 1, 4, 1, 65000, 3, 1, 1, 3),
    _RcQoSClassMapRowSta_Type()
)
rcQoSClassMapRowSta.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQoSClassMapRowSta.setStatus("current")
_RcQoSPolicyMapTable_Object = MibTable
rcQoSPolicyMapTable = _RcQoSPolicyMapTable_Object(
    (1, 3, 6, 1, 4, 1, 65000, 3, 2)
)
if mibBuilder.loadTexts:
    rcQoSPolicyMapTable.setStatus("current")
_RcQoSPolicyMapEntry_Object = MibTableRow
rcQoSPolicyMapEntry = _RcQoSPolicyMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 65000, 3, 2, 1)
)
rcQoSPolicyMapEntry.setIndexNames(
    (0, "RC-QosPolicy-MIB", "rcQoSPolicyMapname"),
    (0, "RC-QosPolicy-MIB", "rcQoSPolicyMapClassName"),
)
if mibBuilder.loadTexts:
    rcQoSPolicyMapEntry.setStatus("current")


class _RcQoSPolicyMapname_Type(DisplayString):
    """Custom type rcQoSPolicyMapname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_RcQoSPolicyMapname_Type.__name__ = "DisplayString"
_RcQoSPolicyMapname_Object = MibTableColumn
rcQoSPolicyMapname = _RcQoSPolicyMapname_Object(
    (1, 3, 6, 1, 4, 1, 65000, 3, 2, 1, 1),
    _RcQoSPolicyMapname_Type()
)
rcQoSPolicyMapname.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQoSPolicyMapname.setStatus("current")


class _RcQoSPolicyMapClassName_Type(DisplayString):
    """Custom type rcQoSPolicyMapClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_RcQoSPolicyMapClassName_Type.__name__ = "DisplayString"
_RcQoSPolicyMapClassName_Object = MibTableColumn
rcQoSPolicyMapClassName = _RcQoSPolicyMapClassName_Object(
    (1, 3, 6, 1, 4, 1, 65000, 3, 2, 1, 2),
    _RcQoSPolicyMapClassName_Type()
)
rcQoSPolicyMapClassName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcQoSPolicyMapClassName.setStatus("current")


class _RcQoSPolicyMapSetIPDSCP_Type(Unsigned32):
    """Custom type rcQoSPolicyMapSetIPDSCP based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RcQoSPolicyMapSetIPDSCP_Type.__name__ = "Unsigned32"
_RcQoSPolicyMapSetIPDSCP_Object = MibTableColumn
rcQoSPolicyMapSetIPDSCP = _RcQoSPolicyMapSetIPDSCP_Object(
    (1, 3, 6, 1, 4, 1, 65000, 3, 2, 1, 3),
    _RcQoSPolicyMapSetIPDSCP_Type()
)
rcQoSPolicyMapSetIPDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQoSPolicyMapSetIPDSCP.setStatus("current")
_RcQoSPolicyMapRowSta_Type = RowStatus
_RcQoSPolicyMapRowSta_Object = MibTableColumn
rcQoSPolicyMapRowSta = _RcQoSPolicyMapRowSta_Object(
    (1, 3, 6, 1, 4, 1, 65000, 3, 2, 1, 4),
    _RcQoSPolicyMapRowSta_Type()
)
rcQoSPolicyMapRowSta.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcQoSPolicyMapRowSta.setStatus("current")
_RcApplyQoSPolicyMapTable_Object = MibTable
rcApplyQoSPolicyMapTable = _RcApplyQoSPolicyMapTable_Object(
    (1, 3, 6, 1, 4, 1, 65000, 3, 3)
)
if mibBuilder.loadTexts:
    rcApplyQoSPolicyMapTable.setStatus("current")
_RcApplyQoSPolicyMapEntry_Object = MibTableRow
rcApplyQoSPolicyMapEntry = _RcApplyQoSPolicyMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 65000, 3, 3, 1)
)
rcApplyQoSPolicyMapEntry.setIndexNames(
    (0, "RC-QosPolicy-MIB", "rcApplyQoSPolicyInterfacename"),
)
if mibBuilder.loadTexts:
    rcApplyQoSPolicyMapEntry.setStatus("current")


class _RcApplyQoSPolicyInterfacename_Type(DisplayString):
    """Custom type rcApplyQoSPolicyInterfacename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_RcApplyQoSPolicyInterfacename_Type.__name__ = "DisplayString"
_RcApplyQoSPolicyInterfacename_Object = MibTableColumn
rcApplyQoSPolicyInterfacename = _RcApplyQoSPolicyInterfacename_Object(
    (1, 3, 6, 1, 4, 1, 65000, 3, 3, 1, 1),
    _RcApplyQoSPolicyInterfacename_Type()
)
rcApplyQoSPolicyInterfacename.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcApplyQoSPolicyInterfacename.setStatus("current")


class _RcApplyQoSPolicyMapname_Type(DisplayString):
    """Custom type rcApplyQoSPolicyMapname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_RcApplyQoSPolicyMapname_Type.__name__ = "DisplayString"
_RcApplyQoSPolicyMapname_Object = MibTableColumn
rcApplyQoSPolicyMapname = _RcApplyQoSPolicyMapname_Object(
    (1, 3, 6, 1, 4, 1, 65000, 3, 3, 1, 2),
    _RcApplyQoSPolicyMapname_Type()
)
rcApplyQoSPolicyMapname.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcApplyQoSPolicyMapname.setStatus("current")
_RcApplyQoSPolicyMapRowSta_Type = RowStatus
_RcApplyQoSPolicyMapRowSta_Object = MibTableColumn
rcApplyQoSPolicyMapRowSta = _RcApplyQoSPolicyMapRowSta_Object(
    (1, 3, 6, 1, 4, 1, 65000, 3, 3, 1, 3),
    _RcApplyQoSPolicyMapRowSta_Type()
)
rcApplyQoSPolicyMapRowSta.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcApplyQoSPolicyMapRowSta.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RC-QosPolicy-MIB",
    **{"rcQoSPolicy": rcQoSPolicy,
       "rcQoSClassMapTable": rcQoSClassMapTable,
       "rcQoSClassMapEntry": rcQoSClassMapEntry,
       "rcQoSClassMapname": rcQoSClassMapname,
       "rcQoSClassMapMatchACL": rcQoSClassMapMatchACL,
       "rcQoSClassMapRowSta": rcQoSClassMapRowSta,
       "rcQoSPolicyMapTable": rcQoSPolicyMapTable,
       "rcQoSPolicyMapEntry": rcQoSPolicyMapEntry,
       "rcQoSPolicyMapname": rcQoSPolicyMapname,
       "rcQoSPolicyMapClassName": rcQoSPolicyMapClassName,
       "rcQoSPolicyMapSetIPDSCP": rcQoSPolicyMapSetIPDSCP,
       "rcQoSPolicyMapRowSta": rcQoSPolicyMapRowSta,
       "rcApplyQoSPolicyMapTable": rcApplyQoSPolicyMapTable,
       "rcApplyQoSPolicyMapEntry": rcApplyQoSPolicyMapEntry,
       "rcApplyQoSPolicyInterfacename": rcApplyQoSPolicyInterfacename,
       "rcApplyQoSPolicyMapname": rcApplyQoSPolicyMapname,
       "rcApplyQoSPolicyMapRowSta": rcApplyQoSPolicyMapRowSta}
)
