# SNMP MIB module (ADTRAN-GEMINAX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GEMINAX-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:31:18 2025
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

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adGenGeminax,
 adGenGeminaxID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-XDSL-MIB",
    "adGenGeminax",
    "adGenGeminaxID")

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

adGenGeminaxMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 73, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenGeminaxMax_ObjectIdentity = ObjectIdentity
adGenGeminaxMax = _AdGenGeminaxMax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 73, 2, 1)
)
_AdGenGeminaxDiagTable_Object = MibTable
adGenGeminaxDiagTable = _AdGenGeminaxDiagTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 73, 2, 1, 1)
)
if mibBuilder.loadTexts:
    adGenGeminaxDiagTable.setStatus("current")
_AdGenGeminaxDiagEntry_Object = MibTableRow
adGenGeminaxDiagEntry = _AdGenGeminaxDiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 73, 2, 1, 1, 1)
)
adGenGeminaxDiagEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenGeminaxDiagEntry.setStatus("current")


class _AdGenGeminaxErrorClassECF_Type(Integer32):
    """Custom type adGenGeminaxErrorClassECF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("logOnly", 2),
          ("softReset", 3),
          ("hardReset", 4))
    )


_AdGenGeminaxErrorClassECF_Type.__name__ = "Integer32"
_AdGenGeminaxErrorClassECF_Object = MibTableColumn
adGenGeminaxErrorClassECF = _AdGenGeminaxErrorClassECF_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 73, 2, 1, 1, 1, 1),
    _AdGenGeminaxErrorClassECF_Type()
)
adGenGeminaxErrorClassECF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGeminaxErrorClassECF.setStatus("current")


class _AdGenGeminaxErrorClassA_Type(Integer32):
    """Custom type adGenGeminaxErrorClassA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("logOnly", 2),
          ("softReset", 3),
          ("hardReset", 4))
    )


_AdGenGeminaxErrorClassA_Type.__name__ = "Integer32"
_AdGenGeminaxErrorClassA_Object = MibTableColumn
adGenGeminaxErrorClassA = _AdGenGeminaxErrorClassA_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 73, 2, 1, 1, 1, 2),
    _AdGenGeminaxErrorClassA_Type()
)
adGenGeminaxErrorClassA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGeminaxErrorClassA.setStatus("current")


class _AdGenGeminaxErrorClassB_Type(Integer32):
    """Custom type adGenGeminaxErrorClassB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("logOnly", 2),
          ("softReset", 3),
          ("hardReset", 4))
    )


_AdGenGeminaxErrorClassB_Type.__name__ = "Integer32"
_AdGenGeminaxErrorClassB_Object = MibTableColumn
adGenGeminaxErrorClassB = _AdGenGeminaxErrorClassB_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 73, 2, 1, 1, 1, 3),
    _AdGenGeminaxErrorClassB_Type()
)
adGenGeminaxErrorClassB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGeminaxErrorClassB.setStatus("current")


class _AdGenGeminaxErrorClassC_Type(Integer32):
    """Custom type adGenGeminaxErrorClassC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("logOnly", 2),
          ("softReset", 3),
          ("hardReset", 4))
    )


_AdGenGeminaxErrorClassC_Type.__name__ = "Integer32"
_AdGenGeminaxErrorClassC_Object = MibTableColumn
adGenGeminaxErrorClassC = _AdGenGeminaxErrorClassC_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 73, 2, 1, 1, 1, 4),
    _AdGenGeminaxErrorClassC_Type()
)
adGenGeminaxErrorClassC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGeminaxErrorClassC.setStatus("current")


class _AdGenGeminaxErrorClassD_Type(Integer32):
    """Custom type adGenGeminaxErrorClassD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("logOnly", 2),
          ("softReset", 3),
          ("hardReset", 4))
    )


_AdGenGeminaxErrorClassD_Type.__name__ = "Integer32"
_AdGenGeminaxErrorClassD_Object = MibTableColumn
adGenGeminaxErrorClassD = _AdGenGeminaxErrorClassD_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 73, 2, 1, 1, 1, 5),
    _AdGenGeminaxErrorClassD_Type()
)
adGenGeminaxErrorClassD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGeminaxErrorClassD.setStatus("current")


class _AdGenGeminaxErrorClassE_Type(Integer32):
    """Custom type adGenGeminaxErrorClassE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("logOnly", 2),
          ("softReset", 3),
          ("hardReset", 4))
    )


_AdGenGeminaxErrorClassE_Type.__name__ = "Integer32"
_AdGenGeminaxErrorClassE_Object = MibTableColumn
adGenGeminaxErrorClassE = _AdGenGeminaxErrorClassE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 73, 2, 1, 1, 1, 6),
    _AdGenGeminaxErrorClassE_Type()
)
adGenGeminaxErrorClassE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGeminaxErrorClassE.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GEMINAX-MIB",
    **{"adGenGeminaxMax": adGenGeminaxMax,
       "adGenGeminaxDiagTable": adGenGeminaxDiagTable,
       "adGenGeminaxDiagEntry": adGenGeminaxDiagEntry,
       "adGenGeminaxErrorClassECF": adGenGeminaxErrorClassECF,
       "adGenGeminaxErrorClassA": adGenGeminaxErrorClassA,
       "adGenGeminaxErrorClassB": adGenGeminaxErrorClassB,
       "adGenGeminaxErrorClassC": adGenGeminaxErrorClassC,
       "adGenGeminaxErrorClassD": adGenGeminaxErrorClassD,
       "adGenGeminaxErrorClassE": adGenGeminaxErrorClassE,
       "adGenGeminaxMIB": adGenGeminaxMIB}
)
