# SNMP MIB module (ADTRAN-GENERIC-PSEUDOWIRE-CEM-COUNTERS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENERIC-PSEUDOWIRE-CEM-COUNTERS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:30:53 2025
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

(adGenPseudowireCEMPerfID,
 adGenPseudowireCEMPerformance) = mibBuilder.importSymbols(
    "ADTRAN-GENERIC-PSEUDOWIRE-CEM-MGMT-MIB",
    "adGenPseudowireCEMPerfID",
    "adGenPseudowireCEMPerformance")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

adGenPseudowireCEMPerfModuleIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 30, 2, 1)
)
if mibBuilder.loadTexts:
    adGenPseudowireCEMPerfModuleIdentity.setRevisions(
        ("2011-04-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenPseudowireCEMPerfProv_ObjectIdentity = ObjectIdentity
adGenPseudowireCEMPerfProv = _AdGenPseudowireCEMPerfProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 1)
)
_AdGenPseudowireCEMPerfProvTable_Object = MibTable
adGenPseudowireCEMPerfProvTable = _AdGenPseudowireCEMPerfProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 1, 1)
)
if mibBuilder.loadTexts:
    adGenPseudowireCEMPerfProvTable.setStatus("current")
_AdGenPseudowireCEMPerfProvTableEntry_Object = MibTableRow
adGenPseudowireCEMPerfProvTableEntry = _AdGenPseudowireCEMPerfProvTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 1, 1, 1)
)
adGenPseudowireCEMPerfProvTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenPseudowireCEMPerfProvTableEntry.setStatus("current")
_AdGenPseudowireCEMPerfErrorStr_Type = DisplayString
_AdGenPseudowireCEMPerfErrorStr_Object = MibTableColumn
adGenPseudowireCEMPerfErrorStr = _AdGenPseudowireCEMPerfErrorStr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 1, 1, 1, 1),
    _AdGenPseudowireCEMPerfErrorStr_Type()
)
adGenPseudowireCEMPerfErrorStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMPerfErrorStr.setStatus("current")


class _AdGenPseudowireCEMPerfClear15MinCounters_Type(Integer32):
    """Custom type adGenPseudowireCEMPerfClear15MinCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenPseudowireCEMPerfClear15MinCounters_Type.__name__ = "Integer32"
_AdGenPseudowireCEMPerfClear15MinCounters_Object = MibTableColumn
adGenPseudowireCEMPerfClear15MinCounters = _AdGenPseudowireCEMPerfClear15MinCounters_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 1, 1, 1, 2),
    _AdGenPseudowireCEMPerfClear15MinCounters_Type()
)
adGenPseudowireCEMPerfClear15MinCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPseudowireCEMPerfClear15MinCounters.setStatus("current")


class _AdGenPseudowireCEMPerfClear24HrCounters_Type(Integer32):
    """Custom type adGenPseudowireCEMPerfClear24HrCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenPseudowireCEMPerfClear24HrCounters_Type.__name__ = "Integer32"
_AdGenPseudowireCEMPerfClear24HrCounters_Object = MibTableColumn
adGenPseudowireCEMPerfClear24HrCounters = _AdGenPseudowireCEMPerfClear24HrCounters_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 1, 1, 1, 3),
    _AdGenPseudowireCEMPerfClear24HrCounters_Type()
)
adGenPseudowireCEMPerfClear24HrCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPseudowireCEMPerfClear24HrCounters.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENERIC-PSEUDOWIRE-CEM-COUNTERS-MIB",
    **{"adGenPseudowireCEMPerfProv": adGenPseudowireCEMPerfProv,
       "adGenPseudowireCEMPerfProvTable": adGenPseudowireCEMPerfProvTable,
       "adGenPseudowireCEMPerfProvTableEntry": adGenPseudowireCEMPerfProvTableEntry,
       "adGenPseudowireCEMPerfErrorStr": adGenPseudowireCEMPerfErrorStr,
       "adGenPseudowireCEMPerfClear15MinCounters": adGenPseudowireCEMPerfClear15MinCounters,
       "adGenPseudowireCEMPerfClear24HrCounters": adGenPseudowireCEMPerfClear24HrCounters,
       "adGenPseudowireCEMPerfModuleIdentity": adGenPseudowireCEMPerfModuleIdentity}
)
