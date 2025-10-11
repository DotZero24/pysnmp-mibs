# SNMP MIB module (HPN-ICF-LswSMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/HPN-ICF-LswSMON-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:43:10 2025
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

(hpnicfRhw,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfRhw")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfSmonExtend_ObjectIdentity = ObjectIdentity
hpnicfSmonExtend = _HpnicfSmonExtend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 26)
)
_HpnicfsmonExtendObject_ObjectIdentity = ObjectIdentity
hpnicfsmonExtendObject = _HpnicfsmonExtendObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 26, 1)
)
_Hpnicfdot1qVlanStatNumber_Type = Integer32
_Hpnicfdot1qVlanStatNumber_Object = MibScalar
hpnicfdot1qVlanStatNumber = _Hpnicfdot1qVlanStatNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 26, 1, 1),
    _Hpnicfdot1qVlanStatNumber_Type()
)
hpnicfdot1qVlanStatNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1qVlanStatNumber.setStatus("mandatory")
_Hpnicfdot1qVlanStatStatusTable_Object = MibTable
hpnicfdot1qVlanStatStatusTable = _Hpnicfdot1qVlanStatStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 26, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfdot1qVlanStatStatusTable.setStatus("mandatory")
_Hpnicfdot1qVlanStatStatusEntry_Object = MibTableRow
hpnicfdot1qVlanStatStatusEntry = _Hpnicfdot1qVlanStatStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 26, 1, 2, 1)
)
hpnicfdot1qVlanStatStatusEntry.setIndexNames(
    (0, "HPN-ICF-LswSMON-MIB", "hpnicfdot1qVlanStatEnableIndex"),
)
if mibBuilder.loadTexts:
    hpnicfdot1qVlanStatStatusEntry.setStatus("mandatory")
_Hpnicfdot1qVlanStatEnableIndex_Type = Integer32
_Hpnicfdot1qVlanStatEnableIndex_Object = MibTableColumn
hpnicfdot1qVlanStatEnableIndex = _Hpnicfdot1qVlanStatEnableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 26, 1, 2, 1, 1),
    _Hpnicfdot1qVlanStatEnableIndex_Type()
)
hpnicfdot1qVlanStatEnableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1qVlanStatEnableIndex.setStatus("mandatory")


class _Hpnicfdot1qVlanStatEnableStatus_Type(Integer32):
    """Custom type hpnicfdot1qVlanStatEnableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_Hpnicfdot1qVlanStatEnableStatus_Type.__name__ = "Integer32"
_Hpnicfdot1qVlanStatEnableStatus_Object = MibTableColumn
hpnicfdot1qVlanStatEnableStatus = _Hpnicfdot1qVlanStatEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 26, 1, 2, 1, 2),
    _Hpnicfdot1qVlanStatEnableStatus_Type()
)
hpnicfdot1qVlanStatEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1qVlanStatEnableStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-LswSMON-MIB",
    **{"hpnicfSmonExtend": hpnicfSmonExtend,
       "hpnicfsmonExtendObject": hpnicfsmonExtendObject,
       "hpnicfdot1qVlanStatNumber": hpnicfdot1qVlanStatNumber,
       "hpnicfdot1qVlanStatStatusTable": hpnicfdot1qVlanStatStatusTable,
       "hpnicfdot1qVlanStatStatusEntry": hpnicfdot1qVlanStatStatusEntry,
       "hpnicfdot1qVlanStatEnableIndex": hpnicfdot1qVlanStatEnableIndex,
       "hpnicfdot1qVlanStatEnableStatus": hpnicfdot1qVlanStatEnableStatus}
)
