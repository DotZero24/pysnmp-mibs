# SNMP MIB module (TN-CONN-PROF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TN-CONN-PROF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:59:13 2025
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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")

(TItemDescription,
 TmnxEncapVal) = mibBuilder.importSymbols(
    "TN-TC-MIB",
    "TItemDescription",
    "TmnxEncapVal")

(tnSRMIBModules,
 tnSRObjs) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnSRMIBModules",
    "tnSRObjs")

(tnSysSwitchId,) = mibBuilder.importSymbols(
    "TROPIC-SYSTEM-MIB",
    "tnSysSwitchId")


# MODULE-IDENTITY

tnConnProfMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 5, 1, 3, 75)
)
if mibBuilder.loadTexts:
    tnConnProfMIBModule.setRevisions(
        ("2019-10-18 00:00",
         "2015-04-06 00:00",
         "2011-02-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TnConnProfId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1000),
    )



class TnConnProfVlanRanges(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )



# MIB Managed Objects in the order of their OIDs

_TnConnProfObjs_ObjectIdentity = ObjectIdentity
tnConnProfObjs = _TnConnProfObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 75)
)
_TnConnProfConfigObjs_ObjectIdentity = ObjectIdentity
tnConnProfConfigObjs = _TnConnProfConfigObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 75, 2)
)
_TnConnProfTable_Object = MibTable
tnConnProfTable = _TnConnProfTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 75, 2, 1)
)
if mibBuilder.loadTexts:
    tnConnProfTable.setStatus("current")
_TnConnProfEntry_Object = MibTableRow
tnConnProfEntry = _TnConnProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 75, 2, 1, 1)
)
tnConnProfEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-CONN-PROF-MIB", "tnConnProfId"),
)
if mibBuilder.loadTexts:
    tnConnProfEntry.setStatus("current")
_TnConnProfId_Type = TnConnProfId
_TnConnProfId_Object = MibTableColumn
tnConnProfId = _TnConnProfId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 75, 2, 1, 1, 1),
    _TnConnProfId_Type()
)
tnConnProfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnConnProfId.setStatus("current")
_TnConnProfRowStatus_Type = RowStatus
_TnConnProfRowStatus_Object = MibTableColumn
tnConnProfRowStatus = _TnConnProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 75, 2, 1, 1, 2),
    _TnConnProfRowStatus_Type()
)
tnConnProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnConnProfRowStatus.setStatus("current")
_TnConnProfLastChanged_Type = TimeStamp
_TnConnProfLastChanged_Object = MibTableColumn
tnConnProfLastChanged = _TnConnProfLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 75, 2, 1, 1, 3),
    _TnConnProfLastChanged_Type()
)
tnConnProfLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnConnProfLastChanged.setStatus("current")


class _TnConnProfDescription_Type(TItemDescription):
    """Custom type tnConnProfDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TnConnProfDescription_Type.__name__ = "TItemDescription"
_TnConnProfDescription_Object = MibTableColumn
tnConnProfDescription = _TnConnProfDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 75, 2, 1, 1, 4),
    _TnConnProfDescription_Type()
)
tnConnProfDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnConnProfDescription.setStatus("current")


class _TnConnProfVlanRange_Type(TnConnProfVlanRanges):
    """Custom type tnConnProfVlanRange based on TnConnProfVlanRanges"""
    defaultValue = OctetString("")


_TnConnProfVlanRange_Type.__name__ = "TnConnProfVlanRanges"
_TnConnProfVlanRange_Object = MibTableColumn
tnConnProfVlanRange = _TnConnProfVlanRange_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 75, 2, 1, 1, 5),
    _TnConnProfVlanRange_Type()
)
tnConnProfVlanRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnConnProfVlanRange.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-CONN-PROF-MIB",
    **{"TnConnProfId": TnConnProfId,
       "TnConnProfVlanRanges": TnConnProfVlanRanges,
       "tnConnProfMIBModule": tnConnProfMIBModule,
       "tnConnProfObjs": tnConnProfObjs,
       "tnConnProfConfigObjs": tnConnProfConfigObjs,
       "tnConnProfTable": tnConnProfTable,
       "tnConnProfEntry": tnConnProfEntry,
       "tnConnProfId": tnConnProfId,
       "tnConnProfRowStatus": tnConnProfRowStatus,
       "tnConnProfLastChanged": tnConnProfLastChanged,
       "tnConnProfDescription": tnConnProfDescription,
       "tnConnProfVlanRange": tnConnProfVlanRange}
)
