# SNMP MIB module (ZTE-AN-PPPOEPLUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-PPPOEPLUS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:30 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(zxAnPortLocatingMib,) = mibBuilder.importSymbols(
    "ZTE-AN-PORT-LOCATING-MIB",
    "zxAnPortLocatingMib")

(ZxAnIfindex,
 zxAn) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "ZxAnIfindex",
    "zxAn")


# MODULE-IDENTITY

zxAnPppoePlusMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 40)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _ZxAnPppoeIAEnable_Type(Integer32):
    """Custom type zxAnPppoeIAEnable based on Integer32"""
    defaultValue = 2

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


_ZxAnPppoeIAEnable_Type.__name__ = "Integer32"
_ZxAnPppoeIAEnable_Object = MibScalar
zxAnPppoeIAEnable = _ZxAnPppoeIAEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 40, 1),
    _ZxAnPppoeIAEnable_Type()
)
zxAnPppoeIAEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPppoeIAEnable.setStatus("current")
_ZxAnPortLocatingPppoePlusTable_Object = MibTable
zxAnPortLocatingPppoePlusTable = _ZxAnPortLocatingPppoePlusTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 40, 10)
)
if mibBuilder.loadTexts:
    zxAnPortLocatingPppoePlusTable.setStatus("current")
_ZxAnPortLocatingPppoePlusEntry_Object = MibTableRow
zxAnPortLocatingPppoePlusEntry = _ZxAnPortLocatingPppoePlusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 40, 10, 1)
)
zxAnPortLocatingPppoePlusEntry.setIndexNames(
    (0, "ZTE-AN-PPPOEPLUS-MIB", "zxAnPortLocatingPppoePlusifIndex"),
)
if mibBuilder.loadTexts:
    zxAnPortLocatingPppoePlusEntry.setStatus("current")
_ZxAnPortLocatingPppoePlusifIndex_Type = ZxAnIfindex
_ZxAnPortLocatingPppoePlusifIndex_Object = MibTableColumn
zxAnPortLocatingPppoePlusifIndex = _ZxAnPortLocatingPppoePlusifIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 40, 10, 1, 1),
    _ZxAnPortLocatingPppoePlusifIndex_Type()
)
zxAnPortLocatingPppoePlusifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnPortLocatingPppoePlusifIndex.setStatus("current")


class _ZxAnPppoeIAIfConfEnable_Type(Integer32):
    """Custom type zxAnPppoeIAIfConfEnable based on Integer32"""
    defaultValue = 2

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


_ZxAnPppoeIAIfConfEnable_Type.__name__ = "Integer32"
_ZxAnPppoeIAIfConfEnable_Object = MibTableColumn
zxAnPppoeIAIfConfEnable = _ZxAnPppoeIAIfConfEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 40, 10, 1, 2),
    _ZxAnPppoeIAIfConfEnable_Type()
)
zxAnPppoeIAIfConfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPppoeIAIfConfEnable.setStatus("current")


class _ZxAnPppoeIAIfConfTrust_Type(Integer32):
    """Custom type zxAnPppoeIAIfConfTrust based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_ZxAnPppoeIAIfConfTrust_Type.__name__ = "Integer32"
_ZxAnPppoeIAIfConfTrust_Object = MibTableColumn
zxAnPppoeIAIfConfTrust = _ZxAnPppoeIAIfConfTrust_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 40, 10, 1, 3),
    _ZxAnPppoeIAIfConfTrust_Type()
)
zxAnPppoeIAIfConfTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPppoeIAIfConfTrust.setStatus("current")


class _ZxAnPppoeIAIfConfPolicy_Type(Integer32):
    """Custom type zxAnPppoeIAIfConfPolicy based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("keep", 1),
          ("replace", 2),
          ("discard", 3),
          ("add", 4))
    )


_ZxAnPppoeIAIfConfPolicy_Type.__name__ = "Integer32"
_ZxAnPppoeIAIfConfPolicy_Object = MibTableColumn
zxAnPppoeIAIfConfPolicy = _ZxAnPppoeIAIfConfPolicy_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 40, 10, 1, 4),
    _ZxAnPppoeIAIfConfPolicy_Type()
)
zxAnPppoeIAIfConfPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPppoeIAIfConfPolicy.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-PPPOEPLUS-MIB",
    **{"zxAnPppoePlusMib": zxAnPppoePlusMib,
       "zxAnPppoeIAEnable": zxAnPppoeIAEnable,
       "zxAnPortLocatingPppoePlusTable": zxAnPortLocatingPppoePlusTable,
       "zxAnPortLocatingPppoePlusEntry": zxAnPortLocatingPppoePlusEntry,
       "zxAnPortLocatingPppoePlusifIndex": zxAnPortLocatingPppoePlusifIndex,
       "zxAnPppoeIAIfConfEnable": zxAnPppoeIAIfConfEnable,
       "zxAnPppoeIAIfConfTrust": zxAnPppoeIAIfConfTrust,
       "zxAnPppoeIAIfConfPolicy": zxAnPppoeIAIfConfPolicy}
)
