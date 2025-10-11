# SNMP MIB module (BRCM-CABLEDATA-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/broadcom/BRCM-CABLEDATA-PRIVATE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:08:52 2025
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

(cableDataPrivate,) = mibBuilder.importSymbols(
    "BRCM-CABLEDATA-SMI",
    "cableDataPrivate")

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

cableDataPrivateMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1)
)
if mibBuilder.loadTexts:
    cableDataPrivateMIB.setRevisions(
        ("2007-02-05 00:00",
         "2002-06-04 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CableDataPrivateMIBObjects_ObjectIdentity = ObjectIdentity
cableDataPrivateMIBObjects = _CableDataPrivateMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1)
)
_CableDataPrivateBase_ObjectIdentity = ObjectIdentity
cableDataPrivateBase = _CableDataPrivateBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 1)
)


class _CdPrivateMibEnable_Type(Integer32):
    """Custom type cdPrivateMibEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("factory", 1),
          ("engineering", 2))
    )


_CdPrivateMibEnable_Type.__name__ = "Integer32"
_CdPrivateMibEnable_Object = MibScalar
cdPrivateMibEnable = _CdPrivateMibEnable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 1, 1),
    _CdPrivateMibEnable_Type()
)
cdPrivateMibEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdPrivateMibEnable.setStatus("current")
_CdPrivateMibEnableKeyTable_Object = MibTable
cdPrivateMibEnableKeyTable = _CdPrivateMibEnableKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cdPrivateMibEnableKeyTable.setStatus("current")
_CdPrivateMibEnableKeyEntry_Object = MibTableRow
cdPrivateMibEnableKeyEntry = _CdPrivateMibEnableKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 1, 2, 1)
)
cdPrivateMibEnableKeyEntry.setIndexNames(
    (0, "BRCM-CABLEDATA-PRIVATE-MIB", "cdPvtMibEnableKeyIndex"),
)
if mibBuilder.loadTexts:
    cdPrivateMibEnableKeyEntry.setStatus("current")


class _CdPvtMibEnableKeyIndex_Type(Integer32):
    """Custom type cdPvtMibEnableKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CdPvtMibEnableKeyIndex_Type.__name__ = "Integer32"
_CdPvtMibEnableKeyIndex_Object = MibTableColumn
cdPvtMibEnableKeyIndex = _CdPvtMibEnableKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 1, 2, 1, 1),
    _CdPvtMibEnableKeyIndex_Type()
)
cdPvtMibEnableKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdPvtMibEnableKeyIndex.setStatus("current")


class _CdPvtMibEnableKeyValue_Type(OctetString):
    """Custom type cdPvtMibEnableKeyValue based on OctetString"""
    defaultValue = OctetString("")


_CdPvtMibEnableKeyValue_Type.__name__ = "OctetString"
_CdPvtMibEnableKeyValue_Object = MibTableColumn
cdPvtMibEnableKeyValue = _CdPvtMibEnableKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 1, 2, 1, 2),
    _CdPvtMibEnableKeyValue_Type()
)
cdPvtMibEnableKeyValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdPvtMibEnableKeyValue.setStatus("current")
_CdPvtMibEnableKeyStatus_Type = RowStatus
_CdPvtMibEnableKeyStatus_Object = MibTableColumn
cdPvtMibEnableKeyStatus = _CdPvtMibEnableKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 1, 2, 1, 3),
    _CdPvtMibEnableKeyStatus_Type()
)
cdPvtMibEnableKeyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdPvtMibEnableKeyStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BRCM-CABLEDATA-PRIVATE-MIB",
    **{"cableDataPrivateMIB": cableDataPrivateMIB,
       "cableDataPrivateMIBObjects": cableDataPrivateMIBObjects,
       "cableDataPrivateBase": cableDataPrivateBase,
       "cdPrivateMibEnable": cdPrivateMibEnable,
       "cdPrivateMibEnableKeyTable": cdPrivateMibEnableKeyTable,
       "cdPrivateMibEnableKeyEntry": cdPrivateMibEnableKeyEntry,
       "cdPvtMibEnableKeyIndex": cdPvtMibEnableKeyIndex,
       "cdPvtMibEnableKeyValue": cdPvtMibEnableKeyValue,
       "cdPvtMibEnableKeyStatus": cdPvtMibEnableKeyStatus}
)
