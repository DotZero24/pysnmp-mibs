# SNMP MIB module (DLINKPRIME-CABLE-DIAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DLINKPRIME-CABLE-DIAG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:46:51 2025
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

(dlinkPrimeCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkPrimeCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

dlinkPrimeCableDiagMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 1)
)
if mibBuilder.loadTexts:
    dlinkPrimeCableDiagMIB.setRevisions(
        ("2014-04-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DpCableDiagNotifications_ObjectIdentity = ObjectIdentity
dpCableDiagNotifications = _DpCableDiagNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 1, 0)
)
_DpCableDiagObjects_ObjectIdentity = ObjectIdentity
dpCableDiagObjects = _DpCableDiagObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 1, 1)
)
_DpCableDiagIfTable_Object = MibTable
dpCableDiagIfTable = _DpCableDiagIfTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dpCableDiagIfTable.setStatus("current")
_DpCableDiagIfEntry_Object = MibTableRow
dpCableDiagIfEntry = _DpCableDiagIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 1, 1, 1, 1)
)
dpCableDiagIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dpCableDiagIfEntry.setStatus("current")


class _DpCableDiagIfAction_Type(Integer32):
    """Custom type dpCableDiagIfAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 1),
          ("test", 2),
          ("clear", 3))
    )


_DpCableDiagIfAction_Type.__name__ = "Integer32"
_DpCableDiagIfAction_Object = MibTableColumn
dpCableDiagIfAction = _DpCableDiagIfAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 1, 1, 1, 1, 1),
    _DpCableDiagIfAction_Type()
)
dpCableDiagIfAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpCableDiagIfAction.setStatus("current")
_DpCableDiagResultTable_Object = MibTable
dpCableDiagResultTable = _DpCableDiagResultTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 1, 1, 2)
)
if mibBuilder.loadTexts:
    dpCableDiagResultTable.setStatus("current")
_DpCableDiagResultEntry_Object = MibTableRow
dpCableDiagResultEntry = _DpCableDiagResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 1, 1, 2, 1)
)
dpCableDiagResultEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dpCableDiagResultEntry.setStatus("current")


class _DpCableDiagResultCableStatus_Type(Integer32):
    """Custom type dpCableDiagResultCableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("no_result", 0),
          ("ok", 1),
          ("no_cable", 2),
          ("open", 3),
          ("short", 4),
          ("openshort", 5),
          ("crosstalk", 6))
    )


_DpCableDiagResultCableStatus_Type.__name__ = "Integer32"
_DpCableDiagResultCableStatus_Object = MibTableColumn
dpCableDiagResultCableStatus = _DpCableDiagResultCableStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 1, 1, 2, 1, 1),
    _DpCableDiagResultCableStatus_Type()
)
dpCableDiagResultCableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpCableDiagResultCableStatus.setStatus("current")
_DpCableDiagResultCableLength_Type = Integer32
_DpCableDiagResultCableLength_Object = MibTableColumn
dpCableDiagResultCableLength = _DpCableDiagResultCableLength_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 1, 1, 2, 1, 2),
    _DpCableDiagResultCableLength_Type()
)
dpCableDiagResultCableLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpCableDiagResultCableLength.setStatus("current")
if mibBuilder.loadTexts:
    dpCableDiagResultCableLength.setUnits("meters")


class _DpCableDiagLinkStatus_Type(Integer32):
    """Custom type dpCableDiagLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no_result", 0),
          ("up", 1),
          ("down", 2))
    )


_DpCableDiagLinkStatus_Type.__name__ = "Integer32"
_DpCableDiagLinkStatus_Object = MibTableColumn
dpCableDiagLinkStatus = _DpCableDiagLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 1, 1, 2, 1, 3),
    _DpCableDiagLinkStatus_Type()
)
dpCableDiagLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpCableDiagLinkStatus.setStatus("current")


class _DpCableDiagInterfaceType_Type(Integer32):
    """Custom type dpCableDiagInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no_result", 0),
          ("type_1000BASET", 1),
          ("type_1000BASEX", 2))
    )


_DpCableDiagInterfaceType_Type.__name__ = "Integer32"
_DpCableDiagInterfaceType_Object = MibTableColumn
dpCableDiagInterfaceType = _DpCableDiagInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 1, 1, 2, 1, 4),
    _DpCableDiagInterfaceType_Type()
)
dpCableDiagInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpCableDiagInterfaceType.setStatus("current")
_DpCableDiagConformance_ObjectIdentity = ObjectIdentity
dpCableDiagConformance = _DpCableDiagConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 1, 2)
)
_DpCableDiagCompliances_ObjectIdentity = ObjectIdentity
dpCableDiagCompliances = _DpCableDiagCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 1, 2, 1)
)
_DpCableDiagGroups_ObjectIdentity = ObjectIdentity
dpCableDiagGroups = _DpCableDiagGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 1, 2, 1, 2)
)

# Managed Objects groups

dpCableDiagBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 1, 2, 1, 2, 1)
)
dpCableDiagBasicGroup.setObjects(
      *(("DLINKPRIME-CABLE-DIAG-MIB", "dpCableDiagIfAction"),
        ("DLINKPRIME-CABLE-DIAG-MIB", "dpCableDiagResultCableStatus"),
        ("DLINKPRIME-CABLE-DIAG-MIB", "dpCableDiagResultCableLength"),
        ("DLINKPRIME-CABLE-DIAG-MIB", "dpCableDiagLinkStatus"),
        ("DLINKPRIME-CABLE-DIAG-MIB", "dpCableDiagInterfaceType"))
)
if mibBuilder.loadTexts:
    dpCableDiagBasicGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dpCableDiagCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 15, 1, 2, 1, 1)
)
dpCableDiagCompliance.setObjects(
    ("DLINKPRIME-CABLE-DIAG-MIB", "dpCableDiagBasicGroup")
)
if mibBuilder.loadTexts:
    dpCableDiagCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKPRIME-CABLE-DIAG-MIB",
    **{"dlinkPrimeCableDiagMIB": dlinkPrimeCableDiagMIB,
       "dpCableDiagNotifications": dpCableDiagNotifications,
       "dpCableDiagObjects": dpCableDiagObjects,
       "dpCableDiagIfTable": dpCableDiagIfTable,
       "dpCableDiagIfEntry": dpCableDiagIfEntry,
       "dpCableDiagIfAction": dpCableDiagIfAction,
       "dpCableDiagResultTable": dpCableDiagResultTable,
       "dpCableDiagResultEntry": dpCableDiagResultEntry,
       "dpCableDiagResultCableStatus": dpCableDiagResultCableStatus,
       "dpCableDiagResultCableLength": dpCableDiagResultCableLength,
       "dpCableDiagLinkStatus": dpCableDiagLinkStatus,
       "dpCableDiagInterfaceType": dpCableDiagInterfaceType,
       "dpCableDiagConformance": dpCableDiagConformance,
       "dpCableDiagCompliances": dpCableDiagCompliances,
       "dpCableDiagCompliance": dpCableDiagCompliance,
       "dpCableDiagGroups": dpCableDiagGroups,
       "dpCableDiagBasicGroup": dpCableDiagBasicGroup}
)
