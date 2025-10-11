# SNMP MIB module (CISCO-DS1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/cisco/CISCO-DS1-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:40:06 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InterfaceIndex,
 ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifDescr",
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoDs1MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1055)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CoiIntervalType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fifteenMin", 1),
          ("oneDay", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoDs1MIBNotifs_ObjectIdentity = ObjectIdentity
ciscoDs1MIBNotifs = _CiscoDs1MIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1055, 0)
)
_CiscoDs1MIBObjects_ObjectIdentity = ObjectIdentity
ciscoDs1MIBObjects = _CiscoDs1MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1055, 1)
)
_CiscoDS1PMData_ObjectIdentity = ObjectIdentity
ciscoDS1PMData = _CiscoDS1PMData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1055, 1, 1)
)
_CoiDS1PMCurrentTable_Object = MibTable
coiDS1PMCurrentTable = _CoiDS1PMCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1055, 1, 1, 1)
)
if mibBuilder.loadTexts:
    coiDS1PMCurrentTable.setStatus("current")
_CoiDS1PMCurrentEntry_Object = MibTableRow
coiDS1PMCurrentEntry = _CoiDS1PMCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1055, 1, 1, 1, 1)
)
coiDS1PMCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DS1-MIB", "coiDS1CurrentIntervalType"),
)
if mibBuilder.loadTexts:
    coiDS1PMCurrentEntry.setStatus("current")
_CoiDS1CurrentIntervalType_Type = CoiIntervalType
_CoiDS1CurrentIntervalType_Object = MibTableColumn
coiDS1CurrentIntervalType = _CoiDS1CurrentIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1055, 1, 1, 1, 1, 1),
    _CoiDS1CurrentIntervalType_Type()
)
coiDS1CurrentIntervalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coiDS1CurrentIntervalType.setStatus("current")
_CoiDS1CurrentLCVs_Type = Counter32
_CoiDS1CurrentLCVs_Object = MibTableColumn
coiDS1CurrentLCVs = _CoiDS1CurrentLCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1055, 1, 1, 1, 1, 2),
    _CoiDS1CurrentLCVs_Type()
)
coiDS1CurrentLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiDS1CurrentLCVs.setStatus("current")
_CoiDS1CurrentPCVs_Type = Counter32
_CoiDS1CurrentPCVs_Object = MibTableColumn
coiDS1CurrentPCVs = _CoiDS1CurrentPCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1055, 1, 1, 1, 1, 3),
    _CoiDS1CurrentPCVs_Type()
)
coiDS1CurrentPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiDS1CurrentPCVs.setStatus("current")
_CoiDS1CurrentSELSs_Type = Counter32
_CoiDS1CurrentSELSs_Object = MibTableColumn
coiDS1CurrentSELSs = _CoiDS1CurrentSELSs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1055, 1, 1, 1, 1, 4),
    _CoiDS1CurrentSELSs_Type()
)
coiDS1CurrentSELSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiDS1CurrentSELSs.setStatus("current")
_CoiDS1CurrentLESs_Type = Counter32
_CoiDS1CurrentLESs_Object = MibTableColumn
coiDS1CurrentLESs = _CoiDS1CurrentLESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1055, 1, 1, 1, 1, 5),
    _CoiDS1CurrentLESs_Type()
)
coiDS1CurrentLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiDS1CurrentLESs.setStatus("current")
_CoiDS1CurrentAISs_Type = Counter32
_CoiDS1CurrentAISs_Object = MibTableColumn
coiDS1CurrentAISs = _CoiDS1CurrentAISs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1055, 1, 1, 1, 1, 6),
    _CoiDS1CurrentAISs_Type()
)
coiDS1CurrentAISs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiDS1CurrentAISs.setStatus("current")
_CoiDS1CurrentFCPs_Type = Counter32
_CoiDS1CurrentFCPs_Object = MibTableColumn
coiDS1CurrentFCPs = _CoiDS1CurrentFCPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1055, 1, 1, 1, 1, 7),
    _CoiDS1CurrentFCPs_Type()
)
coiDS1CurrentFCPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiDS1CurrentFCPs.setStatus("current")
_CoiDS1CurrentESs_Type = Counter32
_CoiDS1CurrentESs_Object = MibTableColumn
coiDS1CurrentESs = _CoiDS1CurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1055, 1, 1, 1, 1, 8),
    _CoiDS1CurrentESs_Type()
)
coiDS1CurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiDS1CurrentESs.setStatus("current")
_CoiDS1CurrentSESs_Type = Counter32
_CoiDS1CurrentSESs_Object = MibTableColumn
coiDS1CurrentSESs = _CoiDS1CurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1055, 1, 1, 1, 1, 9),
    _CoiDS1CurrentSESs_Type()
)
coiDS1CurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiDS1CurrentSESs.setStatus("current")
_CoiDS1CurrentUASs_Type = Counter32
_CoiDS1CurrentUASs_Object = MibTableColumn
coiDS1CurrentUASs = _CoiDS1CurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1055, 1, 1, 1, 1, 10),
    _CoiDS1CurrentUASs_Type()
)
coiDS1CurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiDS1CurrentUASs.setStatus("current")
_CoiDS1CurrentESFEs_Type = Counter32
_CoiDS1CurrentESFEs_Object = MibTableColumn
coiDS1CurrentESFEs = _CoiDS1CurrentESFEs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1055, 1, 1, 1, 1, 11),
    _CoiDS1CurrentESFEs_Type()
)
coiDS1CurrentESFEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiDS1CurrentESFEs.setStatus("current")
_CoiDS1CurrentSESFEs_Type = Counter32
_CoiDS1CurrentSESFEs_Object = MibTableColumn
coiDS1CurrentSESFEs = _CoiDS1CurrentSESFEs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1055, 1, 1, 1, 1, 12),
    _CoiDS1CurrentSESFEs_Type()
)
coiDS1CurrentSESFEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiDS1CurrentSESFEs.setStatus("current")
_CoiDS1CurrentUASFEs_Type = Counter32
_CoiDS1CurrentUASFEs_Object = MibTableColumn
coiDS1CurrentUASFEs = _CoiDS1CurrentUASFEs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1055, 1, 1, 1, 1, 13),
    _CoiDS1CurrentUASFEs_Type()
)
coiDS1CurrentUASFEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiDS1CurrentUASFEs.setStatus("current")
_CoiDS1currentPMValidData_Type = TruthValue
_CoiDS1currentPMValidData_Object = MibTableColumn
coiDS1currentPMValidData = _CoiDS1currentPMValidData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1055, 1, 1, 1, 1, 14),
    _CoiDS1currentPMValidData_Type()
)
coiDS1currentPMValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiDS1currentPMValidData.setStatus("current")
_CoiDS1PMHisTable_Object = MibTable
coiDS1PMHisTable = _CoiDS1PMHisTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1055, 1, 1, 2)
)
if mibBuilder.loadTexts:
    coiDS1PMHisTable.setStatus("current")
_CoiDS1PMHisEntry_Object = MibTableRow
coiDS1PMHisEntry = _CoiDS1PMHisEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1055, 1, 1, 2, 1)
)
coiDS1PMHisEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DS1-MIB", "coiDS1PMHisIntervalType"),
    (0, "CISCO-DS1-MIB", "coiDS1PMHisBucketNumber"),
)
if mibBuilder.loadTexts:
    coiDS1PMHisEntry.setStatus("current")
_CoiDS1PMHisIntervalType_Type = CoiIntervalType
_CoiDS1PMHisIntervalType_Object = MibTableColumn
coiDS1PMHisIntervalType = _CoiDS1PMHisIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1055, 1, 1, 2, 1, 1),
    _CoiDS1PMHisIntervalType_Type()
)
coiDS1PMHisIntervalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coiDS1PMHisIntervalType.setStatus("current")


class _CoiDS1PMHisBucketNumber_Type(Unsigned32):
    """Custom type coiDS1PMHisBucketNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CoiDS1PMHisBucketNumber_Type.__name__ = "Unsigned32"
_CoiDS1PMHisBucketNumber_Object = MibTableColumn
coiDS1PMHisBucketNumber = _CoiDS1PMHisBucketNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1055, 1, 1, 2, 1, 2),
    _CoiDS1PMHisBucketNumber_Type()
)
coiDS1PMHisBucketNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coiDS1PMHisBucketNumber.setStatus("current")
_CoiDS1HisLCVs_Type = Counter32
_CoiDS1HisLCVs_Object = MibTableColumn
coiDS1HisLCVs = _CoiDS1HisLCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1055, 1, 1, 2, 1, 3),
    _CoiDS1HisLCVs_Type()
)
coiDS1HisLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiDS1HisLCVs.setStatus("current")
_CoiDS1HisPCVs_Type = Counter32
_CoiDS1HisPCVs_Object = MibTableColumn
coiDS1HisPCVs = _CoiDS1HisPCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1055, 1, 1, 2, 1, 4),
    _CoiDS1HisPCVs_Type()
)
coiDS1HisPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiDS1HisPCVs.setStatus("current")
_CoiDS1HisSELSs_Type = Counter32
_CoiDS1HisSELSs_Object = MibTableColumn
coiDS1HisSELSs = _CoiDS1HisSELSs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1055, 1, 1, 2, 1, 5),
    _CoiDS1HisSELSs_Type()
)
coiDS1HisSELSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiDS1HisSELSs.setStatus("current")
_CoiDS1HisLESs_Type = Counter32
_CoiDS1HisLESs_Object = MibTableColumn
coiDS1HisLESs = _CoiDS1HisLESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1055, 1, 1, 2, 1, 6),
    _CoiDS1HisLESs_Type()
)
coiDS1HisLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiDS1HisLESs.setStatus("current")
_CoiDS1HisAISs_Type = Counter32
_CoiDS1HisAISs_Object = MibTableColumn
coiDS1HisAISs = _CoiDS1HisAISs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1055, 1, 1, 2, 1, 7),
    _CoiDS1HisAISs_Type()
)
coiDS1HisAISs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiDS1HisAISs.setStatus("current")
_CoiDS1HisFCPs_Type = Counter32
_CoiDS1HisFCPs_Object = MibTableColumn
coiDS1HisFCPs = _CoiDS1HisFCPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1055, 1, 1, 2, 1, 8),
    _CoiDS1HisFCPs_Type()
)
coiDS1HisFCPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiDS1HisFCPs.setStatus("current")
_CoiDS1HisESs_Type = Counter32
_CoiDS1HisESs_Object = MibTableColumn
coiDS1HisESs = _CoiDS1HisESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1055, 1, 1, 2, 1, 9),
    _CoiDS1HisESs_Type()
)
coiDS1HisESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiDS1HisESs.setStatus("current")
_CoiDS1HisSESs_Type = Counter32
_CoiDS1HisSESs_Object = MibTableColumn
coiDS1HisSESs = _CoiDS1HisSESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1055, 1, 1, 2, 1, 10),
    _CoiDS1HisSESs_Type()
)
coiDS1HisSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiDS1HisSESs.setStatus("current")
_CoiDS1HisUASs_Type = Counter32
_CoiDS1HisUASs_Object = MibTableColumn
coiDS1HisUASs = _CoiDS1HisUASs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1055, 1, 1, 2, 1, 11),
    _CoiDS1HisUASs_Type()
)
coiDS1HisUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiDS1HisUASs.setStatus("current")
_CoiDS1HisESFEs_Type = Counter32
_CoiDS1HisESFEs_Object = MibTableColumn
coiDS1HisESFEs = _CoiDS1HisESFEs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1055, 1, 1, 2, 1, 12),
    _CoiDS1HisESFEs_Type()
)
coiDS1HisESFEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiDS1HisESFEs.setStatus("current")
_CoiDS1HisSESFEs_Type = Counter32
_CoiDS1HisSESFEs_Object = MibTableColumn
coiDS1HisSESFEs = _CoiDS1HisSESFEs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1055, 1, 1, 2, 1, 13),
    _CoiDS1HisSESFEs_Type()
)
coiDS1HisSESFEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiDS1HisSESFEs.setStatus("current")
_CoiDS1HisUASFEs_Type = Counter32
_CoiDS1HisUASFEs_Object = MibTableColumn
coiDS1HisUASFEs = _CoiDS1HisUASFEs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1055, 1, 1, 2, 1, 14),
    _CoiDS1HisUASFEs_Type()
)
coiDS1HisUASFEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiDS1HisUASFEs.setStatus("current")
_CoiDS1HisPMValidData_Type = TruthValue
_CoiDS1HisPMValidData_Object = MibTableColumn
coiDS1HisPMValidData = _CoiDS1HisPMValidData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1055, 1, 1, 2, 1, 15),
    _CoiDS1HisPMValidData_Type()
)
coiDS1HisPMValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiDS1HisPMValidData.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DS1-MIB",
    **{"CoiIntervalType": CoiIntervalType,
       "ciscoDs1MIB": ciscoDs1MIB,
       "ciscoDs1MIBNotifs": ciscoDs1MIBNotifs,
       "ciscoDs1MIBObjects": ciscoDs1MIBObjects,
       "ciscoDS1PMData": ciscoDS1PMData,
       "coiDS1PMCurrentTable": coiDS1PMCurrentTable,
       "coiDS1PMCurrentEntry": coiDS1PMCurrentEntry,
       "coiDS1CurrentIntervalType": coiDS1CurrentIntervalType,
       "coiDS1CurrentLCVs": coiDS1CurrentLCVs,
       "coiDS1CurrentPCVs": coiDS1CurrentPCVs,
       "coiDS1CurrentSELSs": coiDS1CurrentSELSs,
       "coiDS1CurrentLESs": coiDS1CurrentLESs,
       "coiDS1CurrentAISs": coiDS1CurrentAISs,
       "coiDS1CurrentFCPs": coiDS1CurrentFCPs,
       "coiDS1CurrentESs": coiDS1CurrentESs,
       "coiDS1CurrentSESs": coiDS1CurrentSESs,
       "coiDS1CurrentUASs": coiDS1CurrentUASs,
       "coiDS1CurrentESFEs": coiDS1CurrentESFEs,
       "coiDS1CurrentSESFEs": coiDS1CurrentSESFEs,
       "coiDS1CurrentUASFEs": coiDS1CurrentUASFEs,
       "coiDS1currentPMValidData": coiDS1currentPMValidData,
       "coiDS1PMHisTable": coiDS1PMHisTable,
       "coiDS1PMHisEntry": coiDS1PMHisEntry,
       "coiDS1PMHisIntervalType": coiDS1PMHisIntervalType,
       "coiDS1PMHisBucketNumber": coiDS1PMHisBucketNumber,
       "coiDS1HisLCVs": coiDS1HisLCVs,
       "coiDS1HisPCVs": coiDS1HisPCVs,
       "coiDS1HisSELSs": coiDS1HisSELSs,
       "coiDS1HisLESs": coiDS1HisLESs,
       "coiDS1HisAISs": coiDS1HisAISs,
       "coiDS1HisFCPs": coiDS1HisFCPs,
       "coiDS1HisESs": coiDS1HisESs,
       "coiDS1HisSESs": coiDS1HisSESs,
       "coiDS1HisUASs": coiDS1HisUASs,
       "coiDS1HisESFEs": coiDS1HisESFEs,
       "coiDS1HisSESFEs": coiDS1HisSESFEs,
       "coiDS1HisUASFEs": coiDS1HisUASFEs,
       "coiDS1HisPMValidData": coiDS1HisPMValidData}
)
