# SNMP MIB module (ELTEX-MES-ISS-ERPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-ISS-ERPS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:48:24 2025
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

(fsErpsContextId,
 fsErpsRingId) = mibBuilder.importSymbols(
    "ARICENT-ERPS-MIB",
    "fsErpsContextId",
    "fsErpsRingId")

(eltMesIss,) = mibBuilder.importSymbols(
    "ELTEX-MES-ISS-MIB",
    "eltMesIss")

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

eltMesIssErpsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 29)
)
if mibBuilder.loadTexts:
    eltMesIssErpsMIB.setRevisions(
        ("2021-12-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesIssErpsObjects_ObjectIdentity = ObjectIdentity
eltMesIssErpsObjects = _EltMesIssErpsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 29, 1)
)
_EltMesIssErpsRingConfig_ObjectIdentity = ObjectIdentity
eltMesIssErpsRingConfig = _EltMesIssErpsRingConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 29, 1, 1)
)
_EltMesIssErpsRingIfmTable_Object = MibTable
eltMesIssErpsRingIfmTable = _EltMesIssErpsRingIfmTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 29, 1, 1, 2)
)
if mibBuilder.loadTexts:
    eltMesIssErpsRingIfmTable.setStatus("current")
_EltMesIssErpsRingIfmEntry_Object = MibTableRow
eltMesIssErpsRingIfmEntry = _EltMesIssErpsRingIfmEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 29, 1, 1, 2, 1)
)
eltMesIssErpsRingIfmEntry.setIndexNames(
    (0, "ARICENT-ERPS-MIB", "fsErpsContextId"),
    (0, "ARICENT-ERPS-MIB", "fsErpsRingId"),
)
if mibBuilder.loadTexts:
    eltMesIssErpsRingIfmEntry.setStatus("current")


class _EltMesIssErpsRingIfmMdLevel_Type(Unsigned32):
    """Custom type eltMesIssErpsRingIfmMdLevel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_EltMesIssErpsRingIfmMdLevel_Type.__name__ = "Unsigned32"
_EltMesIssErpsRingIfmMdLevel_Object = MibTableColumn
eltMesIssErpsRingIfmMdLevel = _EltMesIssErpsRingIfmMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 29, 1, 1, 2, 1, 1),
    _EltMesIssErpsRingIfmMdLevel_Type()
)
eltMesIssErpsRingIfmMdLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssErpsRingIfmMdLevel.setStatus("current")
_EltMesIssErpsRingIfmRowStatus_Type = RowStatus
_EltMesIssErpsRingIfmRowStatus_Object = MibTableColumn
eltMesIssErpsRingIfmRowStatus = _EltMesIssErpsRingIfmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 29, 1, 1, 2, 1, 2),
    _EltMesIssErpsRingIfmRowStatus_Type()
)
eltMesIssErpsRingIfmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssErpsRingIfmRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-ISS-ERPS-MIB",
    **{"eltMesIssErpsMIB": eltMesIssErpsMIB,
       "eltMesIssErpsObjects": eltMesIssErpsObjects,
       "eltMesIssErpsRingConfig": eltMesIssErpsRingConfig,
       "eltMesIssErpsRingIfmTable": eltMesIssErpsRingIfmTable,
       "eltMesIssErpsRingIfmEntry": eltMesIssErpsRingIfmEntry,
       "eltMesIssErpsRingIfmMdLevel": eltMesIssErpsRingIfmMdLevel,
       "eltMesIssErpsRingIfmRowStatus": eltMesIssErpsRingIfmRowStatus}
)
