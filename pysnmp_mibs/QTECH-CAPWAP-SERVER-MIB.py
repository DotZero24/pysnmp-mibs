# SNMP MIB module (QTECH-CAPWAP-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-CAPWAP-SERVER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:58:27 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

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

qtechCapwapSvrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 89)
)
if mibBuilder.loadTexts:
    qtechCapwapSvrMIB.setRevisions(
        ("2010-08-24 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechCapwapSvrMIBObjects_ObjectIdentity = ObjectIdentity
qtechCapwapSvrMIBObjects = _QtechCapwapSvrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 89, 1)
)
_QtechCapwapSvrWhiteListURLTable_Object = MibTable
qtechCapwapSvrWhiteListURLTable = _QtechCapwapSvrWhiteListURLTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 89, 1, 1)
)
if mibBuilder.loadTexts:
    qtechCapwapSvrWhiteListURLTable.setStatus("current")
_QtechCapwapSvrWhiteListURLEntry_Object = MibTableRow
qtechCapwapSvrWhiteListURLEntry = _QtechCapwapSvrWhiteListURLEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 89, 1, 1, 1)
)
qtechCapwapSvrWhiteListURLEntry.setIndexNames(
    (0, "QTECH-CAPWAP-SERVER-MIB", "qtechCapwapSvrWhiteListIndex"),
)
if mibBuilder.loadTexts:
    qtechCapwapSvrWhiteListURLEntry.setStatus("current")
_QtechCapwapSvrWhiteListIndex_Type = Unsigned32
_QtechCapwapSvrWhiteListIndex_Object = MibTableColumn
qtechCapwapSvrWhiteListIndex = _QtechCapwapSvrWhiteListIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 89, 1, 1, 1, 1),
    _QtechCapwapSvrWhiteListIndex_Type()
)
qtechCapwapSvrWhiteListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCapwapSvrWhiteListIndex.setStatus("current")


class _QtechCapwapSvrWhiteListURL_Type(DisplayString):
    """Custom type qtechCapwapSvrWhiteListURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QtechCapwapSvrWhiteListURL_Type.__name__ = "DisplayString"
_QtechCapwapSvrWhiteListURL_Object = MibTableColumn
qtechCapwapSvrWhiteListURL = _QtechCapwapSvrWhiteListURL_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 89, 1, 1, 1, 2),
    _QtechCapwapSvrWhiteListURL_Type()
)
qtechCapwapSvrWhiteListURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechCapwapSvrWhiteListURL.setStatus("current")


class _QtechCapwapSvrWhiteListURLParserStatus_Type(DisplayString):
    """Custom type qtechCapwapSvrWhiteListURLParserStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QtechCapwapSvrWhiteListURLParserStatus_Type.__name__ = "DisplayString"
_QtechCapwapSvrWhiteListURLParserStatus_Object = MibTableColumn
qtechCapwapSvrWhiteListURLParserStatus = _QtechCapwapSvrWhiteListURLParserStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 89, 1, 1, 1, 3),
    _QtechCapwapSvrWhiteListURLParserStatus_Type()
)
qtechCapwapSvrWhiteListURLParserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCapwapSvrWhiteListURLParserStatus.setStatus("current")
_QtechCapwapSvrWhiteListURLRowStatus_Type = RowStatus
_QtechCapwapSvrWhiteListURLRowStatus_Object = MibTableColumn
qtechCapwapSvrWhiteListURLRowStatus = _QtechCapwapSvrWhiteListURLRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 89, 1, 1, 1, 4),
    _QtechCapwapSvrWhiteListURLRowStatus_Type()
)
qtechCapwapSvrWhiteListURLRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechCapwapSvrWhiteListURLRowStatus.setStatus("current")
_QtechCapwapSvrWhiteListIPTable_Object = MibTable
qtechCapwapSvrWhiteListIPTable = _QtechCapwapSvrWhiteListIPTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 89, 1, 2)
)
if mibBuilder.loadTexts:
    qtechCapwapSvrWhiteListIPTable.setStatus("current")
_QtechCapwapSvrWhiteListIPEntry_Object = MibTableRow
qtechCapwapSvrWhiteListIPEntry = _QtechCapwapSvrWhiteListIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 89, 1, 2, 1)
)
qtechCapwapSvrWhiteListIPEntry.setIndexNames(
    (0, "QTECH-CAPWAP-SERVER-MIB", "qtechCapwapSvrWhiteListIP"),
)
if mibBuilder.loadTexts:
    qtechCapwapSvrWhiteListIPEntry.setStatus("current")
_QtechCapwapSvrWhiteListIP_Type = IpAddress
_QtechCapwapSvrWhiteListIP_Object = MibTableColumn
qtechCapwapSvrWhiteListIP = _QtechCapwapSvrWhiteListIP_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 89, 1, 2, 1, 1),
    _QtechCapwapSvrWhiteListIP_Type()
)
qtechCapwapSvrWhiteListIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCapwapSvrWhiteListIP.setStatus("current")
_QtechCapwapSvrWhiteListIPRowStatus_Type = RowStatus
_QtechCapwapSvrWhiteListIPRowStatus_Object = MibTableColumn
qtechCapwapSvrWhiteListIPRowStatus = _QtechCapwapSvrWhiteListIPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 89, 1, 2, 1, 2),
    _QtechCapwapSvrWhiteListIPRowStatus_Type()
)
qtechCapwapSvrWhiteListIPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechCapwapSvrWhiteListIPRowStatus.setStatus("current")
_QtechCapwapSvrBlackListURLTable_Object = MibTable
qtechCapwapSvrBlackListURLTable = _QtechCapwapSvrBlackListURLTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 89, 1, 3)
)
if mibBuilder.loadTexts:
    qtechCapwapSvrBlackListURLTable.setStatus("current")
_QtechCapwapSvrBlackListURLEntry_Object = MibTableRow
qtechCapwapSvrBlackListURLEntry = _QtechCapwapSvrBlackListURLEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 89, 1, 3, 1)
)
qtechCapwapSvrBlackListURLEntry.setIndexNames(
    (0, "QTECH-CAPWAP-SERVER-MIB", "qtechCapwapSvrBlackListIndex"),
)
if mibBuilder.loadTexts:
    qtechCapwapSvrBlackListURLEntry.setStatus("current")
_QtechCapwapSvrBlackListIndex_Type = Unsigned32
_QtechCapwapSvrBlackListIndex_Object = MibTableColumn
qtechCapwapSvrBlackListIndex = _QtechCapwapSvrBlackListIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 89, 1, 3, 1, 1),
    _QtechCapwapSvrBlackListIndex_Type()
)
qtechCapwapSvrBlackListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCapwapSvrBlackListIndex.setStatus("current")


class _QtechCapwapSvrBlackListURL_Type(DisplayString):
    """Custom type qtechCapwapSvrBlackListURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QtechCapwapSvrBlackListURL_Type.__name__ = "DisplayString"
_QtechCapwapSvrBlackListURL_Object = MibTableColumn
qtechCapwapSvrBlackListURL = _QtechCapwapSvrBlackListURL_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 89, 1, 3, 1, 2),
    _QtechCapwapSvrBlackListURL_Type()
)
qtechCapwapSvrBlackListURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechCapwapSvrBlackListURL.setStatus("current")


class _QtechCapwapSvrBlackListURLParserStatus_Type(DisplayString):
    """Custom type qtechCapwapSvrBlackListURLParserStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QtechCapwapSvrBlackListURLParserStatus_Type.__name__ = "DisplayString"
_QtechCapwapSvrBlackListURLParserStatus_Object = MibTableColumn
qtechCapwapSvrBlackListURLParserStatus = _QtechCapwapSvrBlackListURLParserStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 89, 1, 3, 1, 3),
    _QtechCapwapSvrBlackListURLParserStatus_Type()
)
qtechCapwapSvrBlackListURLParserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCapwapSvrBlackListURLParserStatus.setStatus("current")
_QtechCapwapSvrBlackListURLRowStatus_Type = RowStatus
_QtechCapwapSvrBlackListURLRowStatus_Object = MibTableColumn
qtechCapwapSvrBlackListURLRowStatus = _QtechCapwapSvrBlackListURLRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 89, 1, 3, 1, 4),
    _QtechCapwapSvrBlackListURLRowStatus_Type()
)
qtechCapwapSvrBlackListURLRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechCapwapSvrBlackListURLRowStatus.setStatus("current")
_QtechCapwapSvrBlackListIPTable_Object = MibTable
qtechCapwapSvrBlackListIPTable = _QtechCapwapSvrBlackListIPTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 89, 1, 4)
)
if mibBuilder.loadTexts:
    qtechCapwapSvrBlackListIPTable.setStatus("current")
_QtechCapwapSvrBlackListIPEntry_Object = MibTableRow
qtechCapwapSvrBlackListIPEntry = _QtechCapwapSvrBlackListIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 89, 1, 4, 1)
)
qtechCapwapSvrBlackListIPEntry.setIndexNames(
    (0, "QTECH-CAPWAP-SERVER-MIB", "qtechCapwapSvrBlackListIP"),
)
if mibBuilder.loadTexts:
    qtechCapwapSvrBlackListIPEntry.setStatus("current")
_QtechCapwapSvrBlackListIP_Type = IpAddress
_QtechCapwapSvrBlackListIP_Object = MibTableColumn
qtechCapwapSvrBlackListIP = _QtechCapwapSvrBlackListIP_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 89, 1, 4, 1, 1),
    _QtechCapwapSvrBlackListIP_Type()
)
qtechCapwapSvrBlackListIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCapwapSvrBlackListIP.setStatus("current")
_QtechCapwapSvrBlackListIPRowStatus_Type = RowStatus
_QtechCapwapSvrBlackListIPRowStatus_Object = MibTableColumn
qtechCapwapSvrBlackListIPRowStatus = _QtechCapwapSvrBlackListIPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 89, 1, 4, 1, 2),
    _QtechCapwapSvrBlackListIPRowStatus_Type()
)
qtechCapwapSvrBlackListIPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechCapwapSvrBlackListIPRowStatus.setStatus("current")
_QtechCapwapSvrBlackListPortTable_Object = MibTable
qtechCapwapSvrBlackListPortTable = _QtechCapwapSvrBlackListPortTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 89, 1, 5)
)
if mibBuilder.loadTexts:
    qtechCapwapSvrBlackListPortTable.setStatus("current")
_QtechCapwapSvrBlackListPortEntry_Object = MibTableRow
qtechCapwapSvrBlackListPortEntry = _QtechCapwapSvrBlackListPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 89, 1, 5, 1)
)
qtechCapwapSvrBlackListPortEntry.setIndexNames(
    (0, "QTECH-CAPWAP-SERVER-MIB", "qtechCapwapSvrBlackListPort"),
)
if mibBuilder.loadTexts:
    qtechCapwapSvrBlackListPortEntry.setStatus("current")
_QtechCapwapSvrBlackListPort_Type = Integer32
_QtechCapwapSvrBlackListPort_Object = MibTableColumn
qtechCapwapSvrBlackListPort = _QtechCapwapSvrBlackListPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 89, 1, 5, 1, 1),
    _QtechCapwapSvrBlackListPort_Type()
)
qtechCapwapSvrBlackListPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCapwapSvrBlackListPort.setStatus("current")
_QtechCapwapSvrBlackListPortRowStatus_Type = RowStatus
_QtechCapwapSvrBlackListPortRowStatus_Object = MibTableColumn
qtechCapwapSvrBlackListPortRowStatus = _QtechCapwapSvrBlackListPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 89, 1, 5, 1, 2),
    _QtechCapwapSvrBlackListPortRowStatus_Type()
)
qtechCapwapSvrBlackListPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechCapwapSvrBlackListPortRowStatus.setStatus("current")
_QtechCapwapSvrMIBConformance_ObjectIdentity = ObjectIdentity
qtechCapwapSvrMIBConformance = _QtechCapwapSvrMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 89, 2)
)
_QtechCapwapSvrMIBCompliances_ObjectIdentity = ObjectIdentity
qtechCapwapSvrMIBCompliances = _QtechCapwapSvrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 89, 2, 1)
)
_QtechCapwapSvrMIBGroups_ObjectIdentity = ObjectIdentity
qtechCapwapSvrMIBGroups = _QtechCapwapSvrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 89, 2, 2)
)

# Managed Objects groups

qtechCapwapSvrMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 89, 2, 2, 1)
)
qtechCapwapSvrMIBGroup.setObjects(
      *(("QTECH-CAPWAP-SERVER-MIB", "qtechCapwapSvrWhiteListURL"),
        ("QTECH-CAPWAP-SERVER-MIB", "qtechCapwapSvrWhiteListURLParserStatus"),
        ("QTECH-CAPWAP-SERVER-MIB", "qtechCapwapSvrWhiteListURLRowStatus"),
        ("QTECH-CAPWAP-SERVER-MIB", "qtechCapwapSvrWhiteListIP"),
        ("QTECH-CAPWAP-SERVER-MIB", "qtechCapwapSvrWhiteListIPRowStatus"),
        ("QTECH-CAPWAP-SERVER-MIB", "qtechCapwapSvrBlackListURL"),
        ("QTECH-CAPWAP-SERVER-MIB", "qtechCapwapSvrBlackListURLParserStatus"),
        ("QTECH-CAPWAP-SERVER-MIB", "qtechCapwapSvrBlackListURLRowStatus"),
        ("QTECH-CAPWAP-SERVER-MIB", "qtechCapwapSvrBlackListIP"),
        ("QTECH-CAPWAP-SERVER-MIB", "qtechCapwapSvrBlackListIPRowStatus"),
        ("QTECH-CAPWAP-SERVER-MIB", "qtechCapwapSvrBlackListPort"),
        ("QTECH-CAPWAP-SERVER-MIB", "qtechCapwapSvrBlackListPortRowStatus"))
)
if mibBuilder.loadTexts:
    qtechCapwapSvrMIBGroup.setStatus("deprecated")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechCapwapSvrMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 89, 2, 1, 1)
)
qtechCapwapSvrMIBCompliance.setObjects(
    ("QTECH-CAPWAP-SERVER-MIB", "qtechCapwapSvrMIBGroup")
)
if mibBuilder.loadTexts:
    qtechCapwapSvrMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-CAPWAP-SERVER-MIB",
    **{"qtechCapwapSvrMIB": qtechCapwapSvrMIB,
       "qtechCapwapSvrMIBObjects": qtechCapwapSvrMIBObjects,
       "qtechCapwapSvrWhiteListURLTable": qtechCapwapSvrWhiteListURLTable,
       "qtechCapwapSvrWhiteListURLEntry": qtechCapwapSvrWhiteListURLEntry,
       "qtechCapwapSvrWhiteListIndex": qtechCapwapSvrWhiteListIndex,
       "qtechCapwapSvrWhiteListURL": qtechCapwapSvrWhiteListURL,
       "qtechCapwapSvrWhiteListURLParserStatus": qtechCapwapSvrWhiteListURLParserStatus,
       "qtechCapwapSvrWhiteListURLRowStatus": qtechCapwapSvrWhiteListURLRowStatus,
       "qtechCapwapSvrWhiteListIPTable": qtechCapwapSvrWhiteListIPTable,
       "qtechCapwapSvrWhiteListIPEntry": qtechCapwapSvrWhiteListIPEntry,
       "qtechCapwapSvrWhiteListIP": qtechCapwapSvrWhiteListIP,
       "qtechCapwapSvrWhiteListIPRowStatus": qtechCapwapSvrWhiteListIPRowStatus,
       "qtechCapwapSvrBlackListURLTable": qtechCapwapSvrBlackListURLTable,
       "qtechCapwapSvrBlackListURLEntry": qtechCapwapSvrBlackListURLEntry,
       "qtechCapwapSvrBlackListIndex": qtechCapwapSvrBlackListIndex,
       "qtechCapwapSvrBlackListURL": qtechCapwapSvrBlackListURL,
       "qtechCapwapSvrBlackListURLParserStatus": qtechCapwapSvrBlackListURLParserStatus,
       "qtechCapwapSvrBlackListURLRowStatus": qtechCapwapSvrBlackListURLRowStatus,
       "qtechCapwapSvrBlackListIPTable": qtechCapwapSvrBlackListIPTable,
       "qtechCapwapSvrBlackListIPEntry": qtechCapwapSvrBlackListIPEntry,
       "qtechCapwapSvrBlackListIP": qtechCapwapSvrBlackListIP,
       "qtechCapwapSvrBlackListIPRowStatus": qtechCapwapSvrBlackListIPRowStatus,
       "qtechCapwapSvrBlackListPortTable": qtechCapwapSvrBlackListPortTable,
       "qtechCapwapSvrBlackListPortEntry": qtechCapwapSvrBlackListPortEntry,
       "qtechCapwapSvrBlackListPort": qtechCapwapSvrBlackListPort,
       "qtechCapwapSvrBlackListPortRowStatus": qtechCapwapSvrBlackListPortRowStatus,
       "qtechCapwapSvrMIBConformance": qtechCapwapSvrMIBConformance,
       "qtechCapwapSvrMIBCompliances": qtechCapwapSvrMIBCompliances,
       "qtechCapwapSvrMIBCompliance": qtechCapwapSvrMIBCompliance,
       "qtechCapwapSvrMIBGroups": qtechCapwapSvrMIBGroups,
       "qtechCapwapSvrMIBGroup": qtechCapwapSvrMIBGroup}
)
