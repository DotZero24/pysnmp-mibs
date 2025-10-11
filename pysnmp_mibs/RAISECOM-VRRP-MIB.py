# SNMP MIB module (RAISECOM-VRRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-VRRP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:35:36 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(raisecomAgent,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "raisecomAgent")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(vrrpOperVrId,) = mibBuilder.importSymbols(
    "VRRP-MIB",
    "vrrpOperVrId")


# MODULE-IDENTITY

raisecomVrrp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 41)
)
if mibBuilder.loadTexts:
    raisecomVrrp.setRevisions(
        ("2011-07-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RaisecomVrrpNotifications_ObjectIdentity = ObjectIdentity
raisecomVrrpNotifications = _RaisecomVrrpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 41, 0)
)
_RaisecomVrrpObjects_ObjectIdentity = ObjectIdentity
raisecomVrrpObjects = _RaisecomVrrpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 41, 1)
)
_RaisecomVrrpScalarObjects_ObjectIdentity = ObjectIdentity
raisecomVrrpScalarObjects = _RaisecomVrrpScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 41, 1, 1)
)


class _RaisecomVrrpPing_Type(TruthValue):
    """Custom type raisecomVrrpPing based on TruthValue"""
    defaultValue = 1


_RaisecomVrrpPing_Type.__name__ = "TruthValue"
_RaisecomVrrpPing_Object = MibScalar
raisecomVrrpPing = _RaisecomVrrpPing_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 41, 1, 1, 1),
    _RaisecomVrrpPing_Type()
)
raisecomVrrpPing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomVrrpPing.setStatus("current")


class _RaisecomVrrpStatisticsClear_Type(TruthValue):
    """Custom type raisecomVrrpStatisticsClear based on TruthValue"""
    defaultValue = 2


_RaisecomVrrpStatisticsClear_Type.__name__ = "TruthValue"
_RaisecomVrrpStatisticsClear_Object = MibScalar
raisecomVrrpStatisticsClear = _RaisecomVrrpStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 41, 1, 1, 2),
    _RaisecomVrrpStatisticsClear_Type()
)
raisecomVrrpStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomVrrpStatisticsClear.setStatus("current")
_RaisecomVrrpOperTable_Object = MibTable
raisecomVrrpOperTable = _RaisecomVrrpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 41, 1, 2)
)
if mibBuilder.loadTexts:
    raisecomVrrpOperTable.setStatus("current")
_RaisecomVrrpOperEntry_Object = MibTableRow
raisecomVrrpOperEntry = _RaisecomVrrpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 41, 1, 2, 1)
)
raisecomVrrpOperEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VRRP-MIB", "vrrpOperVrId"),
)
if mibBuilder.loadTexts:
    raisecomVrrpOperEntry.setStatus("current")


class _RaisecomVrrpOperDesc_Type(OctetString):
    """Custom type raisecomVrrpOperDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RaisecomVrrpOperDesc_Type.__name__ = "OctetString"
_RaisecomVrrpOperDesc_Object = MibTableColumn
raisecomVrrpOperDesc = _RaisecomVrrpOperDesc_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 41, 1, 2, 1, 1),
    _RaisecomVrrpOperDesc_Type()
)
raisecomVrrpOperDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomVrrpOperDesc.setStatus("current")


class _RaisecomVrrpOperPreemptDelay_Type(Integer32):
    """Custom type raisecomVrrpOperPreemptDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RaisecomVrrpOperPreemptDelay_Type.__name__ = "Integer32"
_RaisecomVrrpOperPreemptDelay_Object = MibTableColumn
raisecomVrrpOperPreemptDelay = _RaisecomVrrpOperPreemptDelay_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 41, 1, 2, 1, 2),
    _RaisecomVrrpOperPreemptDelay_Type()
)
raisecomVrrpOperPreemptDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomVrrpOperPreemptDelay.setStatus("current")
if mibBuilder.loadTexts:
    raisecomVrrpOperPreemptDelay.setUnits("second")
_RaisecomVrrpTrackIfTable_Object = MibTable
raisecomVrrpTrackIfTable = _RaisecomVrrpTrackIfTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 41, 1, 3)
)
if mibBuilder.loadTexts:
    raisecomVrrpTrackIfTable.setStatus("current")
_RaisecomVrrpTrackIfEntry_Object = MibTableRow
raisecomVrrpTrackIfEntry = _RaisecomVrrpTrackIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 41, 1, 3, 1)
)
raisecomVrrpTrackIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VRRP-MIB", "vrrpOperVrId"),
    (0, "RAISECOM-VRRP-MIB", "raisecomVrrpTrackIf"),
)
if mibBuilder.loadTexts:
    raisecomVrrpTrackIfEntry.setStatus("current")
_RaisecomVrrpTrackIf_Type = Integer32
_RaisecomVrrpTrackIf_Object = MibTableColumn
raisecomVrrpTrackIf = _RaisecomVrrpTrackIf_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 41, 1, 3, 1, 1),
    _RaisecomVrrpTrackIf_Type()
)
raisecomVrrpTrackIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomVrrpTrackIf.setStatus("current")
_RaisecomVrrpTrackIfPriChg_Type = Integer32
_RaisecomVrrpTrackIfPriChg_Object = MibTableColumn
raisecomVrrpTrackIfPriChg = _RaisecomVrrpTrackIfPriChg_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 41, 1, 3, 1, 2),
    _RaisecomVrrpTrackIfPriChg_Type()
)
raisecomVrrpTrackIfPriChg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomVrrpTrackIfPriChg.setStatus("current")
_RaisecomVrrpTrackIfRowStatus_Type = RowStatus
_RaisecomVrrpTrackIfRowStatus_Object = MibTableColumn
raisecomVrrpTrackIfRowStatus = _RaisecomVrrpTrackIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 41, 1, 3, 1, 3),
    _RaisecomVrrpTrackIfRowStatus_Type()
)
raisecomVrrpTrackIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomVrrpTrackIfRowStatus.setStatus("current")
_RaisecomVrrpConformance_ObjectIdentity = ObjectIdentity
raisecomVrrpConformance = _RaisecomVrrpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 41, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-VRRP-MIB",
    **{"raisecomVrrp": raisecomVrrp,
       "raisecomVrrpNotifications": raisecomVrrpNotifications,
       "raisecomVrrpObjects": raisecomVrrpObjects,
       "raisecomVrrpScalarObjects": raisecomVrrpScalarObjects,
       "raisecomVrrpPing": raisecomVrrpPing,
       "raisecomVrrpStatisticsClear": raisecomVrrpStatisticsClear,
       "raisecomVrrpOperTable": raisecomVrrpOperTable,
       "raisecomVrrpOperEntry": raisecomVrrpOperEntry,
       "raisecomVrrpOperDesc": raisecomVrrpOperDesc,
       "raisecomVrrpOperPreemptDelay": raisecomVrrpOperPreemptDelay,
       "raisecomVrrpTrackIfTable": raisecomVrrpTrackIfTable,
       "raisecomVrrpTrackIfEntry": raisecomVrrpTrackIfEntry,
       "raisecomVrrpTrackIf": raisecomVrrpTrackIf,
       "raisecomVrrpTrackIfPriChg": raisecomVrrpTrackIfPriChg,
       "raisecomVrrpTrackIfRowStatus": raisecomVrrpTrackIfRowStatus,
       "raisecomVrrpConformance": raisecomVrrpConformance}
)
