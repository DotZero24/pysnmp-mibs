# SNMP MIB module (HPN-ICF-PROT-PRIORITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/HPN-ICF-PROT-PRIORITY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:39:28 2025
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

hpnicfProtocolPriority = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 37)
)
if mibBuilder.loadTexts:
    hpnicfProtocolPriority.setRevisions(
        ("2005-01-17 16:33",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfProtocolPriorityObjects_ObjectIdentity = ObjectIdentity
hpnicfProtocolPriorityObjects = _HpnicfProtocolPriorityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 37, 1)
)
_HpnicfPPri_ObjectIdentity = ObjectIdentity
hpnicfPPri = _HpnicfPPri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 37, 1, 1)
)
_HpnicfProtocolPriorityTable_Object = MibTable
hpnicfProtocolPriorityTable = _HpnicfProtocolPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 37, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfProtocolPriorityTable.setStatus("current")
_HpnicfProtocolPriorityEntry_Object = MibTableRow
hpnicfProtocolPriorityEntry = _HpnicfProtocolPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 37, 1, 1, 1, 1)
)
hpnicfProtocolPriorityEntry.setIndexNames(
    (0, "HPN-ICF-PROT-PRIORITY-MIB", "hpnicfPPriProtocolType"),
)
if mibBuilder.loadTexts:
    hpnicfProtocolPriorityEntry.setStatus("current")


class _HpnicfPPriProtocolType_Type(Integer32):
    """Custom type hpnicfPPriProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ospf", 1),
          ("telnet", 2),
          ("snmp", 3),
          ("icmp", 4),
          ("bgp", 5),
          ("ldp", 6))
    )


_HpnicfPPriProtocolType_Type.__name__ = "Integer32"
_HpnicfPPriProtocolType_Object = MibTableColumn
hpnicfPPriProtocolType = _HpnicfPPriProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 37, 1, 1, 1, 1, 1),
    _HpnicfPPriProtocolType_Type()
)
hpnicfPPriProtocolType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPPriProtocolType.setStatus("current")


class _HpnicfPPriPriorityType_Type(Integer32):
    """Custom type hpnicfPPriPriorityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipPrecedence", 1),
          ("dscp", 2))
    )


_HpnicfPPriPriorityType_Type.__name__ = "Integer32"
_HpnicfPPriPriorityType_Object = MibTableColumn
hpnicfPPriPriorityType = _HpnicfPPriPriorityType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 37, 1, 1, 1, 1, 2),
    _HpnicfPPriPriorityType_Type()
)
hpnicfPPriPriorityType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPPriPriorityType.setStatus("current")


class _HpnicfPPriPriorityVlaue_Type(Integer32):
    """Custom type hpnicfPPriPriorityVlaue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HpnicfPPriPriorityVlaue_Type.__name__ = "Integer32"
_HpnicfPPriPriorityVlaue_Object = MibTableColumn
hpnicfPPriPriorityVlaue = _HpnicfPPriPriorityVlaue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 37, 1, 1, 1, 1, 3),
    _HpnicfPPriPriorityVlaue_Type()
)
hpnicfPPriPriorityVlaue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPPriPriorityVlaue.setStatus("current")
_HpnicfPPriRowStatus_Type = RowStatus
_HpnicfPPriRowStatus_Object = MibTableColumn
hpnicfPPriRowStatus = _HpnicfPPriRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 37, 1, 1, 1, 1, 4),
    _HpnicfPPriRowStatus_Type()
)
hpnicfPPriRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPPriRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-PROT-PRIORITY-MIB",
    **{"hpnicfProtocolPriority": hpnicfProtocolPriority,
       "hpnicfProtocolPriorityObjects": hpnicfProtocolPriorityObjects,
       "hpnicfPPri": hpnicfPPri,
       "hpnicfProtocolPriorityTable": hpnicfProtocolPriorityTable,
       "hpnicfProtocolPriorityEntry": hpnicfProtocolPriorityEntry,
       "hpnicfPPriProtocolType": hpnicfPPriProtocolType,
       "hpnicfPPriPriorityType": hpnicfPPriPriorityType,
       "hpnicfPPriPriorityVlaue": hpnicfPPriPriorityVlaue,
       "hpnicfPPriRowStatus": hpnicfPPriRowStatus}
)
