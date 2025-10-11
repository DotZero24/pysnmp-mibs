# SNMP MIB module (PKTC-MDI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rfc/PKTC-MDI-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:24:47 2025
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

(pktcApplicationMibs,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "pktcApplicationMibs")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

pktcMdiMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 6)
)
if mibBuilder.loadTexts:
    pktcMdiMib.setRevisions(
        ("2009-09-17 00:00",
         "2009-02-26 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PktcMdiType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pots", 1),
          ("dectPP", 2))
    )



# MIB Managed Objects in the order of their OIDs

_PktcMdiNotifications_ObjectIdentity = ObjectIdentity
pktcMdiNotifications = _PktcMdiNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 6, 0)
)
_PktcMdiObjects_ObjectIdentity = ObjectIdentity
pktcMdiObjects = _PktcMdiObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 6, 1)
)
_PktcMdiMdiTable_Object = MibTable
pktcMdiMdiTable = _PktcMdiMdiTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 6, 1, 1)
)
if mibBuilder.loadTexts:
    pktcMdiMdiTable.setStatus("current")
_PktcMdiMdiEntry_Object = MibTableRow
pktcMdiMdiEntry = _PktcMdiMdiEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 6, 1, 1, 1)
)
pktcMdiMdiEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pktcMdiMdiEntry.setStatus("current")
_PktcMdiMdiType_Type = PktcMdiType
_PktcMdiMdiType_Object = MibTableColumn
pktcMdiMdiType = _PktcMdiMdiType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 6, 1, 1, 1, 1),
    _PktcMdiMdiType_Type()
)
pktcMdiMdiType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMdiMdiType.setStatus("current")
_PktcMdiMdiName_Type = SnmpAdminString
_PktcMdiMdiName_Object = MibTableColumn
pktcMdiMdiName = _PktcMdiMdiName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 6, 1, 1, 1, 2),
    _PktcMdiMdiName_Type()
)
pktcMdiMdiName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMdiMdiName.setStatus("current")


class _PktcMdiMdiActivityStatus_Type(Integer32):
    """Custom type pktcMdiMdiActivityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_PktcMdiMdiActivityStatus_Type.__name__ = "Integer32"
_PktcMdiMdiActivityStatus_Object = MibTableColumn
pktcMdiMdiActivityStatus = _PktcMdiMdiActivityStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 6, 1, 1, 1, 3),
    _PktcMdiMdiActivityStatus_Type()
)
pktcMdiMdiActivityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMdiMdiActivityStatus.setStatus("current")
_PktcMdiNslTable_Object = MibTable
pktcMdiNslTable = _PktcMdiNslTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 6, 1, 2)
)
if mibBuilder.loadTexts:
    pktcMdiNslTable.setStatus("current")
_PktcMdiNslEntry_Object = MibTableRow
pktcMdiNslEntry = _PktcMdiNslEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 6, 1, 2, 1)
)
pktcMdiNslEntry.setIndexNames(
    (0, "PKTC-MDI-MIB", "pktcMdiNslIndex"),
)
if mibBuilder.loadTexts:
    pktcMdiNslEntry.setStatus("current")
_PktcMdiNslIndex_Type = Unsigned32
_PktcMdiNslIndex_Object = MibTableColumn
pktcMdiNslIndex = _PktcMdiNslIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 6, 1, 2, 1, 1),
    _PktcMdiNslIndex_Type()
)
pktcMdiNslIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcMdiNslIndex.setStatus("current")
_PktcMdiNslName_Type = SnmpAdminString
_PktcMdiNslName_Object = MibTableColumn
pktcMdiNslName = _PktcMdiNslName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 6, 1, 2, 1, 2),
    _PktcMdiNslName_Type()
)
pktcMdiNslName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcMdiNslName.setStatus("current")
_PktcMdiNslPortListIn_Type = SnmpAdminString
_PktcMdiNslPortListIn_Object = MibTableColumn
pktcMdiNslPortListIn = _PktcMdiNslPortListIn_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 6, 1, 2, 1, 3),
    _PktcMdiNslPortListIn_Type()
)
pktcMdiNslPortListIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcMdiNslPortListIn.setStatus("current")
_PktcMdiNslPortListOut_Type = SnmpAdminString
_PktcMdiNslPortListOut_Object = MibTableColumn
pktcMdiNslPortListOut = _PktcMdiNslPortListOut_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 6, 1, 2, 1, 4),
    _PktcMdiNslPortListOut_Type()
)
pktcMdiNslPortListOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcMdiNslPortListOut.setStatus("current")
_PktcMdiNslRowStatus_Type = RowStatus
_PktcMdiNslRowStatus_Object = MibTableColumn
pktcMdiNslRowStatus = _PktcMdiNslRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 6, 1, 2, 1, 5),
    _PktcMdiNslRowStatus_Type()
)
pktcMdiNslRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcMdiNslRowStatus.setStatus("current")
_PktcMdiMibConformance_ObjectIdentity = ObjectIdentity
pktcMdiMibConformance = _PktcMdiMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 6, 2)
)
_PktcMdiMibCompliances_ObjectIdentity = ObjectIdentity
pktcMdiMibCompliances = _PktcMdiMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 6, 2, 1)
)
_PktcMdiMibGroups_ObjectIdentity = ObjectIdentity
pktcMdiMibGroups = _PktcMdiMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 6, 2, 2)
)

# Managed Objects groups

pktcMdiGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 6, 2, 2, 1)
)
pktcMdiGroup.setObjects(
      *(("PKTC-MDI-MIB", "pktcMdiMdiType"),
        ("PKTC-MDI-MIB", "pktcMdiMdiName"),
        ("PKTC-MDI-MIB", "pktcMdiMdiActivityStatus"),
        ("PKTC-MDI-MIB", "pktcMdiNslName"),
        ("PKTC-MDI-MIB", "pktcMdiNslPortListIn"),
        ("PKTC-MDI-MIB", "pktcMdiNslPortListOut"),
        ("PKTC-MDI-MIB", "pktcMdiNslRowStatus"))
)
if mibBuilder.loadTexts:
    pktcMdiGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pktcMdiCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 6, 2, 1, 1)
)
pktcMdiCompliance.setObjects(
    ("PKTC-MDI-MIB", "pktcMdiGroup")
)
if mibBuilder.loadTexts:
    pktcMdiCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PKTC-MDI-MIB",
    **{"PktcMdiType": PktcMdiType,
       "pktcMdiMib": pktcMdiMib,
       "pktcMdiNotifications": pktcMdiNotifications,
       "pktcMdiObjects": pktcMdiObjects,
       "pktcMdiMdiTable": pktcMdiMdiTable,
       "pktcMdiMdiEntry": pktcMdiMdiEntry,
       "pktcMdiMdiType": pktcMdiMdiType,
       "pktcMdiMdiName": pktcMdiMdiName,
       "pktcMdiMdiActivityStatus": pktcMdiMdiActivityStatus,
       "pktcMdiNslTable": pktcMdiNslTable,
       "pktcMdiNslEntry": pktcMdiNslEntry,
       "pktcMdiNslIndex": pktcMdiNslIndex,
       "pktcMdiNslName": pktcMdiNslName,
       "pktcMdiNslPortListIn": pktcMdiNslPortListIn,
       "pktcMdiNslPortListOut": pktcMdiNslPortListOut,
       "pktcMdiNslRowStatus": pktcMdiNslRowStatus,
       "pktcMdiMibConformance": pktcMdiMibConformance,
       "pktcMdiMibCompliances": pktcMdiMibCompliances,
       "pktcMdiCompliance": pktcMdiCompliance,
       "pktcMdiMibGroups": pktcMdiMibGroups,
       "pktcMdiGroup": pktcMdiGroup}
)
