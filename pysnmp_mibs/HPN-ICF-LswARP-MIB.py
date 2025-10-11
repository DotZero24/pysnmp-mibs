# SNMP MIB module (HPN-ICF-LswARP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/HPN-ICF-LswARP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:42:37 2025
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

(hpnicflswCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicflswCommon")

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

hpnicfLswArpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 4)
)
if mibBuilder.loadTexts:
    hpnicfLswArpMib.setRevisions(
        ("2001-06-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfLswProxyArpObject_ObjectIdentity = ObjectIdentity
hpnicfLswProxyArpObject = _HpnicfLswProxyArpObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 4, 1)
)
if mibBuilder.loadTexts:
    hpnicfLswProxyArpObject.setStatus("current")
_HpnicfLswProxyArpEnableTable_Object = MibTable
hpnicfLswProxyArpEnableTable = _HpnicfLswProxyArpEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfLswProxyArpEnableTable.setStatus("current")
_HpnicfLswProxyArpEnableEntry_Object = MibTableRow
hpnicfLswProxyArpEnableEntry = _HpnicfLswProxyArpEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 4, 1, 1, 1)
)
hpnicfLswProxyArpEnableEntry.setIndexNames(
    (0, "HPN-ICF-LswARP-MIB", "hpnicfLswIfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfLswProxyArpEnableEntry.setStatus("current")
_HpnicfLswIfIndex_Type = Integer32
_HpnicfLswIfIndex_Object = MibTableColumn
hpnicfLswIfIndex = _HpnicfLswIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 4, 1, 1, 1, 1),
    _HpnicfLswIfIndex_Type()
)
hpnicfLswIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLswIfIndex.setStatus("current")


class _HpnicfLswProxyArpStatus_Type(Integer32):
    """Custom type hpnicfLswProxyArpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_HpnicfLswProxyArpStatus_Type.__name__ = "Integer32"
_HpnicfLswProxyArpStatus_Object = MibTableColumn
hpnicfLswProxyArpStatus = _HpnicfLswProxyArpStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 4, 1, 1, 1, 2),
    _HpnicfLswProxyArpStatus_Type()
)
hpnicfLswProxyArpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLswProxyArpStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-LswARP-MIB",
    **{"hpnicfLswArpMib": hpnicfLswArpMib,
       "hpnicfLswProxyArpObject": hpnicfLswProxyArpObject,
       "hpnicfLswProxyArpEnableTable": hpnicfLswProxyArpEnableTable,
       "hpnicfLswProxyArpEnableEntry": hpnicfLswProxyArpEnableEntry,
       "hpnicfLswIfIndex": hpnicfLswIfIndex,
       "hpnicfLswProxyArpStatus": hpnicfLswProxyArpStatus}
)
