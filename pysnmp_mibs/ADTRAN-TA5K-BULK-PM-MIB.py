# SNMP MIB module (ADTRAN-TA5K-BULK-PM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-TA5K-BULK-PM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:32:21 2025
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

(adGenPortInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENPORT-MIB",
    "adGenPortInfoIndex")

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adGenTa5kBulkPM,
 adGenTa5kBulkPMID) = mibBuilder.importSymbols(
    "ADTRAN-GENTA5K-MIB",
    "adGenTa5kBulkPM",
    "adGenTa5kBulkPMID")

(adIdentity,
 adIdentityShared,
 adMgmt,
 adProducts) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentity",
    "adIdentityShared",
    "adMgmt",
    "adProducts")

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

adTa5kBulkPMModuleIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 67, 1, 18, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdTa5kBulkPMSlotTable_Object = MibTable
adTa5kBulkPMSlotTable = _AdTa5kBulkPMSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 18, 1)
)
if mibBuilder.loadTexts:
    adTa5kBulkPMSlotTable.setStatus("current")
_AdTa5kBulkPMSlotEntry_Object = MibTableRow
adTa5kBulkPMSlotEntry = _AdTa5kBulkPMSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 18, 1, 1)
)
adTa5kBulkPMSlotEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adTa5kBulkPMSlotEntry.setStatus("current")
_AdTa5kBulkPMSlotInstance_Type = Integer32
_AdTa5kBulkPMSlotInstance_Object = MibTableColumn
adTa5kBulkPMSlotInstance = _AdTa5kBulkPMSlotInstance_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 18, 1, 1, 1),
    _AdTa5kBulkPMSlotInstance_Type()
)
adTa5kBulkPMSlotInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kBulkPMSlotInstance.setStatus("current")
_AdTa5kBulkPM15MinSlotInstance_Type = Integer32
_AdTa5kBulkPM15MinSlotInstance_Object = MibTableColumn
adTa5kBulkPM15MinSlotInstance = _AdTa5kBulkPM15MinSlotInstance_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 18, 1, 1, 2),
    _AdTa5kBulkPM15MinSlotInstance_Type()
)
adTa5kBulkPM15MinSlotInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kBulkPM15MinSlotInstance.setStatus("current")
_AdTa5kBulkPMPortTable_Object = MibTable
adTa5kBulkPMPortTable = _AdTa5kBulkPMPortTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 18, 2)
)
if mibBuilder.loadTexts:
    adTa5kBulkPMPortTable.setStatus("current")
_AdTa5kBulkPMPortEntry_Object = MibTableRow
adTa5kBulkPMPortEntry = _AdTa5kBulkPMPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 18, 2, 1)
)
adTa5kBulkPMPortEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENPORT-MIB", "adGenPortInfoIndex"),
)
if mibBuilder.loadTexts:
    adTa5kBulkPMPortEntry.setStatus("current")
_AdTa5kBulkPMPortInstance_Type = Integer32
_AdTa5kBulkPMPortInstance_Object = MibTableColumn
adTa5kBulkPMPortInstance = _AdTa5kBulkPMPortInstance_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 18, 2, 1, 1),
    _AdTa5kBulkPMPortInstance_Type()
)
adTa5kBulkPMPortInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kBulkPMPortInstance.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-TA5K-BULK-PM-MIB",
    **{"adTa5kBulkPMSlotTable": adTa5kBulkPMSlotTable,
       "adTa5kBulkPMSlotEntry": adTa5kBulkPMSlotEntry,
       "adTa5kBulkPMSlotInstance": adTa5kBulkPMSlotInstance,
       "adTa5kBulkPM15MinSlotInstance": adTa5kBulkPM15MinSlotInstance,
       "adTa5kBulkPMPortTable": adTa5kBulkPMPortTable,
       "adTa5kBulkPMPortEntry": adTa5kBulkPMPortEntry,
       "adTa5kBulkPMPortInstance": adTa5kBulkPMPortInstance,
       "adTa5kBulkPMModuleIdentity": adTa5kBulkPMModuleIdentity}
)
