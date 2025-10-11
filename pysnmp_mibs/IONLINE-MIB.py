# SNMP MIB module (IONLINE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aruba/IONLINE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:22:30 2025
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
 enterprises,
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "enterprises",
    "iso",
    "snmpModules")

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

elite = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21068)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ionline_ObjectIdentity = ObjectIdentity
ionline = _Ionline_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21068, 1)
)
if mibBuilder.loadTexts:
    ionline.setStatus("current")
_IoPoolStatus_ObjectIdentity = ObjectIdentity
ioPoolStatus = _IoPoolStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21068, 1, 3)
)
_IoPoolUsage_Type = Integer32
_IoPoolUsage_Object = MibScalar
ioPoolUsage = _IoPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 21068, 1, 3, 1),
    _IoPoolUsage_Type()
)
ioPoolUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ioPoolUsage.setStatus("current")
_IoPoolTable_Object = MibTable
ioPoolTable = _IoPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 21068, 2)
)
if mibBuilder.loadTexts:
    ioPoolTable.setStatus("current")
_IoPoolEntry_Object = MibTableRow
ioPoolEntry = _IoPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 21068, 2, 1)
)
ioPoolEntry.setIndexNames(
    (0, "IONLINE-MIB", "sysORIndex"),
)
if mibBuilder.loadTexts:
    ioPoolEntry.setStatus("current")
_IoPoolORId_Type = ObjectIdentifier
_IoPoolORId_Object = MibTableColumn
ioPoolORId = _IoPoolORId_Object(
    (1, 3, 6, 1, 4, 1, 21068, 2, 1, 2),
    _IoPoolORId_Type()
)
ioPoolORId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ioPoolORId.setStatus("current")
_IoPoolORDescr_Type = DisplayString
_IoPoolORDescr_Object = MibTableColumn
ioPoolORDescr = _IoPoolORDescr_Object(
    (1, 3, 6, 1, 4, 1, 21068, 2, 1, 3),
    _IoPoolORDescr_Type()
)
ioPoolORDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioPoolORDescr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IONLINE-MIB",
    **{"elite": elite,
       "ionline": ionline,
       "ioPoolStatus": ioPoolStatus,
       "ioPoolUsage": ioPoolUsage,
       "ioPoolTable": ioPoolTable,
       "ioPoolEntry": ioPoolEntry,
       "ioPoolORId": ioPoolORId,
       "ioPoolORDescr": ioPoolORDescr}
)
