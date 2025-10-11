# SNMP MIB module (HPN-ICF-UPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/HPN-ICF-UPS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:33:20 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

hpnicfUps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 82)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfActionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("action", 1),
          ("invalid", 2))
    )



# MIB Managed Objects in the order of their OIDs

_HpnicfUpsMibObjects_ObjectIdentity = ObjectIdentity
hpnicfUpsMibObjects = _HpnicfUpsMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 82, 1)
)
_HpnicfUpsConfigEnable_Type = HpnicfActionType
_HpnicfUpsConfigEnable_Object = MibScalar
hpnicfUpsConfigEnable = _HpnicfUpsConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 82, 1, 1),
    _HpnicfUpsConfigEnable_Type()
)
hpnicfUpsConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfUpsConfigEnable.setStatus("current")
_HpnicfUpsConfigTable_Object = MibTable
hpnicfUpsConfigTable = _HpnicfUpsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 82, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfUpsConfigTable.setStatus("current")
_HpnicfUpsConfigEntry_Object = MibTableRow
hpnicfUpsConfigEntry = _HpnicfUpsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 82, 1, 2, 1)
)
hpnicfUpsConfigEntry.setIndexNames(
    (0, "HPN-ICF-UPS-MIB", "hpnicfUpsIndex"),
)
if mibBuilder.loadTexts:
    hpnicfUpsConfigEntry.setStatus("current")
_HpnicfUpsIndex_Type = Integer32
_HpnicfUpsIndex_Object = MibTableColumn
hpnicfUpsIndex = _HpnicfUpsIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 82, 1, 2, 1, 1),
    _HpnicfUpsIndex_Type()
)
hpnicfUpsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfUpsIndex.setStatus("current")


class _HpnicfUpsType_Type(Integer32):
    """Custom type hpnicfUpsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("emersonUart", 1),
          ("mge", 2),
          ("common", 3),
          ("emersonEth", 4),
          ("liebert", 5))
    )


_HpnicfUpsType_Type.__name__ = "Integer32"
_HpnicfUpsType_Object = MibTableColumn
hpnicfUpsType = _HpnicfUpsType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 82, 1, 2, 1, 2),
    _HpnicfUpsType_Type()
)
hpnicfUpsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfUpsType.setStatus("current")
_HpnicfUpsIpAddress_Type = InetAddress
_HpnicfUpsIpAddress_Object = MibTableColumn
hpnicfUpsIpAddress = _HpnicfUpsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 82, 1, 2, 1, 3),
    _HpnicfUpsIpAddress_Type()
)
hpnicfUpsIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfUpsIpAddress.setStatus("current")
_HpnicfUpsIpAddressType_Type = InetAddressType
_HpnicfUpsIpAddressType_Object = MibTableColumn
hpnicfUpsIpAddressType = _HpnicfUpsIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 82, 1, 2, 1, 4),
    _HpnicfUpsIpAddressType_Type()
)
hpnicfUpsIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfUpsIpAddressType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-UPS-MIB",
    **{"HpnicfActionType": HpnicfActionType,
       "hpnicfUps": hpnicfUps,
       "hpnicfUpsMibObjects": hpnicfUpsMibObjects,
       "hpnicfUpsConfigEnable": hpnicfUpsConfigEnable,
       "hpnicfUpsConfigTable": hpnicfUpsConfigTable,
       "hpnicfUpsConfigEntry": hpnicfUpsConfigEntry,
       "hpnicfUpsIndex": hpnicfUpsIndex,
       "hpnicfUpsType": hpnicfUpsType,
       "hpnicfUpsIpAddress": hpnicfUpsIpAddress,
       "hpnicfUpsIpAddressType": hpnicfUpsIpAddressType}
)
