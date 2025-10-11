# SNMP MIB module (PDN-MPE-HEALTH-AND-STATUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/paradyne/PDN-MPE-HEALTH-AND-STATUS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:00:19 2025
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

(mpe_devHealth,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "mpe-devHealth")

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
 NotificationType,
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
    "NotificationType",
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

_MpeDevHealthAndStatusMIBObjects_ObjectIdentity = ObjectIdentity
mpeDevHealthAndStatusMIBObjects = _MpeDevHealthAndStatusMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 7, 1)
)
_MpeDevHealthAndStatusTable_Object = MibTable
mpeDevHealthAndStatusTable = _MpeDevHealthAndStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 7, 1, 1)
)
if mibBuilder.loadTexts:
    mpeDevHealthAndStatusTable.setStatus("mandatory")
_MpeDevHealthAndStatusEntry_Object = MibTableRow
mpeDevHealthAndStatusEntry = _MpeDevHealthAndStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 7, 1, 1, 1)
)
mpeDevHealthAndStatusEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    mpeDevHealthAndStatusEntry.setStatus("mandatory")


class _MpeDevSelfTestResults_Type(DisplayString):
    """Custom type mpeDevSelfTestResults based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MpeDevSelfTestResults_Type.__name__ = "DisplayString"
_MpeDevSelfTestResults_Object = MibTableColumn
mpeDevSelfTestResults = _MpeDevSelfTestResults_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 7, 1, 1, 1, 1),
    _MpeDevSelfTestResults_Type()
)
mpeDevSelfTestResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpeDevSelfTestResults.setStatus("mandatory")
_MpeDevHealthAndStatusMIBTraps_ObjectIdentity = ObjectIdentity
mpeDevHealthAndStatusMIBTraps = _MpeDevHealthAndStatusMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 7, 2)
)

# Managed Objects groups


# Notification objects

mpeSelfTestFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 7, 2, 0, 1)
)
mpeSelfTestFailure.setObjects(
    ("PDN-MPE-HEALTH-AND-STATUS-MIB", "mpeDevSelfTestResults")
)
if mibBuilder.loadTexts:
    mpeSelfTestFailure.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-MPE-HEALTH-AND-STATUS-MIB",
    **{"mpeDevHealthAndStatusMIBObjects": mpeDevHealthAndStatusMIBObjects,
       "mpeDevHealthAndStatusTable": mpeDevHealthAndStatusTable,
       "mpeDevHealthAndStatusEntry": mpeDevHealthAndStatusEntry,
       "mpeDevSelfTestResults": mpeDevSelfTestResults,
       "mpeDevHealthAndStatusMIBTraps": mpeDevHealthAndStatusMIBTraps,
       "mpeSelfTestFailure": mpeSelfTestFailure}
)
