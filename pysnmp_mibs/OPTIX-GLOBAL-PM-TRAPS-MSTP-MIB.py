# SNMP MIB module (OPTIX-GLOBAL-PM-TRAPS-MSTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/huawei/OPTIX-GLOBAL-PM-TRAPS-MSTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:22:13 2025
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

(optixGlobalTrap,
 rptEvtDateTime,
 rptEvtObjType,
 rptEvtPara,
 rptEvtParaLen,
 rptEvtPeriod,
 rptEvtValue,
 rptEvtVldty) = mibBuilder.importSymbols(
    "OPTIX-GLOBAL-TRAPS-MIB",
    "optixGlobalTrap",
    "rptEvtDateTime",
    "rptEvtObjType",
    "rptEvtPara",
    "rptEvtParaLen",
    "rptEvtPeriod",
    "rptEvtValue",
    "rptEvtVldty")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OptixTrapsPM_ObjectIdentity = ObjectIdentity
optixTrapsPM = _OptixTrapsPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20)
)

# Managed Objects groups


# Notification objects

pmRisingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 1)
)
pmRisingAlarm.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"),
        ("OPTIX-GLOBAL-PM-TRAPS-MSTP-MIB", "rptEvtDataPmName"),
        ("OPTIX-GLOBAL-PM-TRAPS-MSTP-MIB", "rptEvtMonValue"),
        ("OPTIX-GLOBAL-PM-TRAPS-MSTP-MIB", "rptEvtThValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmRisingAlarm.setStatus(
        "current"
    )

pmFallingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 2)
)
pmFallingAlarm.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"),
        ("OPTIX-GLOBAL-PM-TRAPS-MSTP-MIB", "rptEvtDataPmName"),
        ("OPTIX-GLOBAL-PM-TRAPS-MSTP-MIB", "rptEvtMonValue"),
        ("OPTIX-GLOBAL-PM-TRAPS-MSTP-MIB", "rptEvtThValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmFallingAlarm.setStatus(
        "current"
    )

pmRXPKT64 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 101)
)
pmRXPKT64.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmRXPKT64.setStatus(
        "current"
    )

pmRXPKT65 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 102)
)
pmRXPKT65.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmRXPKT65.setStatus(
        "current"
    )

pmRXPKT128 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 103)
)
pmRXPKT128.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmRXPKT128.setStatus(
        "current"
    )

pmRXPKT256 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 104)
)
pmRXPKT256.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmRXPKT256.setStatus(
        "current"
    )

pmRXPKT512 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 105)
)
pmRXPKT512.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmRXPKT512.setStatus(
        "current"
    )

pmRXPKT1024 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 106)
)
pmRXPKT1024.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmRXPKT1024.setStatus(
        "current"
    )

pmTXPKT64 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 107)
)
pmTXPKT64.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmTXPKT64.setStatus(
        "current"
    )

pmTXPKT65 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 108)
)
pmTXPKT65.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmTXPKT65.setStatus(
        "current"
    )

pmTXPKT128 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 109)
)
pmTXPKT128.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmTXPKT128.setStatus(
        "current"
    )

pmTXPKT256 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 110)
)
pmTXPKT256.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmTXPKT256.setStatus(
        "current"
    )

pmTXPKT512 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 111)
)
pmTXPKT512.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmTXPKT512.setStatus(
        "current"
    )

pmTXPKT1024 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 112)
)
pmTXPKT1024.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmTXPKT1024.setStatus(
        "current"
    )

pmRXUNICAST = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 113)
)
pmRXUNICAST.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmRXUNICAST.setStatus(
        "current"
    )

pmRXMULCAST = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 114)
)
pmRXMULCAST.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmRXMULCAST.setStatus(
        "current"
    )

pmRXBRDCAST = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 115)
)
pmRXBRDCAST.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmRXBRDCAST.setStatus(
        "current"
    )

pmTXUNICAST = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 116)
)
pmTXUNICAST.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmTXUNICAST.setStatus(
        "current"
    )

pmTXMULCAST = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 117)
)
pmTXMULCAST.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmTXMULCAST.setStatus(
        "current"
    )

pmTXBRDCAST = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 118)
)
pmTXBRDCAST.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmTXBRDCAST.setStatus(
        "current"
    )

pmRXPAUSE = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 119)
)
pmRXPAUSE.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmRXPAUSE.setStatus(
        "current"
    )

pmTXPAUSE = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 120)
)
pmTXPAUSE.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmTXPAUSE.setStatus(
        "current"
    )

pmETHDROP = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 121)
)
pmETHDROP.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmETHDROP.setStatus(
        "current"
    )

pmETHUNDER = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 122)
)
pmETHUNDER.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmETHUNDER.setStatus(
        "current"
    )

pmETHOVER = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 123)
)
pmETHOVER.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmETHOVER.setStatus(
        "current"
    )

pmETHFRG = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 124)
)
pmETHFRG.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmETHFRG.setStatus(
        "current"
    )

pmETHJAB = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 125)
)
pmETHJAB.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmETHJAB.setStatus(
        "current"
    )

pmRXBGOOD = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 126)
)
pmRXBGOOD.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmRXBGOOD.setStatus(
        "current"
    )

pmTXBGOOD = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 127)
)
pmTXBGOOD.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmTXBGOOD.setStatus(
        "current"
    )

pmRXBBAD = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 128)
)
pmRXBBAD.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmRXBBAD.setStatus(
        "current"
    )

pmTXBBAD = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 129)
)
pmTXBBAD.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmTXBBAD.setStatus(
        "current"
    )

pmETHALI = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 131)
)
pmETHALI.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmETHALI.setStatus(
        "current"
    )

pmETHFCS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 132)
)
pmETHFCS.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmETHFCS.setStatus(
        "current"
    )

pmRXPKT1519 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 139)
)
pmRXPKT1519.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmRXPKT1519.setStatus(
        "current"
    )

pmTXPKT1519 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 140)
)
pmTXPKT1519.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmTXPKT1519.setStatus(
        "current"
    )

pmPKT64 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 141)
)
pmPKT64.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmPKT64.setStatus(
        "current"
    )

pmPKT65 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 142)
)
pmPKT65.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmPKT65.setStatus(
        "current"
    )

pmPKT128 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 143)
)
pmPKT128.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmPKT128.setStatus(
        "current"
    )

pmPKT256 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 144)
)
pmPKT256.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmPKT256.setStatus(
        "current"
    )

pmPKT512 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 145)
)
pmPKT512.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmPKT512.setStatus(
        "current"
    )

pmPKT1024 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 146)
)
pmPKT1024.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmPKT1024.setStatus(
        "current"
    )

pmPKT1519 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 147)
)
pmPKT1519.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmPKT1519.setStatus(
        "current"
    )

pmRXGOODFULLFRAMESPEED = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 190)
)
pmRXGOODFULLFRAMESPEED.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmRXGOODFULLFRAMESPEED.setStatus(
        "current"
    )

pmTXGOODFULLFRAMESPEED = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 191)
)
pmTXGOODFULLFRAMESPEED.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmTXGOODFULLFRAMESPEED.setStatus(
        "current"
    )

pmRxfullbgood = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 192)
)
pmRxfullbgood.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"),
        ("OPTIX-GLOBAL-PM-TRAPS-MSTP-MIB", "rptEvtDataPmName"),
        ("OPTIX-GLOBAL-PM-TRAPS-MSTP-MIB", "rptEvtMonValue"),
        ("OPTIX-GLOBAL-PM-TRAPS-MSTP-MIB", "rptEvtThValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmRxfullbgood.setStatus(
        "current"
    )

pmTxfullbgood = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 193)
)
pmTxfullbgood.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"),
        ("OPTIX-GLOBAL-PM-TRAPS-MSTP-MIB", "rptEvtDataPmName"),
        ("OPTIX-GLOBAL-PM-TRAPS-MSTP-MIB", "rptEvtMonValue"),
        ("OPTIX-GLOBAL-PM-TRAPS-MSTP-MIB", "rptEvtThValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmTxfullbgood.setStatus(
        "current"
    )

pmRXCTLPKTS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 194)
)
pmRXCTLPKTS.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmRXCTLPKTS.setStatus(
        "current"
    )

pmTXCTLPKTS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 195)
)
pmTXCTLPKTS.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmTXCTLPKTS.setStatus(
        "current"
    )

pmTXETHDROP = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 196)
)
pmTXETHDROP.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmTXETHDROP.setStatus(
        "current"
    )

pmTXETHOVER = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 197)
)
pmTXETHOVER.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmTXETHOVER.setStatus(
        "current"
    )

pmTXPKTS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 198)
)
pmTXPKTS.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmTXPKTS.setStatus(
        "current"
    )

pmTXOCTETS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 199)
)
pmTXOCTETS.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmTXOCTETS.setStatus(
        "current"
    )

pmRXOCTETS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 200)
)
pmRXOCTETS.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmRXOCTETS.setStatus(
        "current"
    )

pmRXPKTS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 201)
)
pmRXPKTS.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmRXPKTS.setStatus(
        "current"
    )

pmVCGRXOCTETS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 350)
)
pmVCGRXOCTETS.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmVCGRXOCTETS.setStatus(
        "current"
    )

pmVCGTXOCTETS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 351)
)
pmVCGTXOCTETS.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmVCGTXOCTETS.setStatus(
        "current"
    )

pmVCGRXPACKETS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 352)
)
pmVCGRXPACKETS.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmVCGRXPACKETS.setStatus(
        "current"
    )

pmVCGTXPACKETS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 353)
)
pmVCGTXPACKETS.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmVCGTXPACKETS.setStatus(
        "current"
    )

pmVCGRXGOODPACKETS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 354)
)
pmVCGRXGOODPACKETS.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmVCGRXGOODPACKETS.setStatus(
        "current"
    )

pmVCGTXGOODPACKETS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 355)
)
pmVCGTXGOODPACKETS.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmVCGTXGOODPACKETS.setStatus(
        "current"
    )

pmVCGRXSPEED = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 356)
)
pmVCGRXSPEED.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmVCGRXSPEED.setStatus(
        "current"
    )

pmVCGTXSPEED = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 357)
)
pmVCGTXSPEED.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmVCGTXSPEED.setStatus(
        "current"
    )

pmPORTRXBWUTILIZATION = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 567)
)
pmPORTRXBWUTILIZATION.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmPORTRXBWUTILIZATION.setStatus(
        "current"
    )

pmPORTTXBWUTILIZATION = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 568)
)
pmPORTTXBWUTILIZATION.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmPORTTXBWUTILIZATION.setStatus(
        "current"
    )

pmRXBPS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 679)
)
pmRXBPS.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmRXBPS.setStatus(
        "current"
    )

pmTXBPS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 680)
)
pmTXBPS.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmTXBPS.setStatus(
        "current"
    )

pmRXPPS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 681)
)
pmRXPPS.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmRXPPS.setStatus(
        "current"
    )

pmTXPPS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 682)
)
pmTXPPS.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmTXPPS.setStatus(
        "current"
    )

pmETHRXTHROUGHPUTMAX = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 683)
)
pmETHRXTHROUGHPUTMAX.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmETHRXTHROUGHPUTMAX.setStatus(
        "current"
    )

pmETHRXTHROUGHPUTMIN = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 684)
)
pmETHRXTHROUGHPUTMIN.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmETHRXTHROUGHPUTMIN.setStatus(
        "current"
    )

pmETHRXTHROUGHPUTAVG = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 685)
)
pmETHRXTHROUGHPUTAVG.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmETHRXTHROUGHPUTAVG.setStatus(
        "current"
    )

pmETHTXTHROUGHPUTMAX = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 686)
)
pmETHTXTHROUGHPUTMAX.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmETHTXTHROUGHPUTMAX.setStatus(
        "current"
    )

pmETHTXTHROUGHPUTMIN = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 687)
)
pmETHTXTHROUGHPUTMIN.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmETHTXTHROUGHPUTMIN.setStatus(
        "current"
    )

pmETHTXTHROUGHPUTAVG = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 688)
)
pmETHTXTHROUGHPUTAVG.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmETHTXTHROUGHPUTAVG.setStatus(
        "current"
    )

pmRXDROPRATIO = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 692)
)
pmRXDROPRATIO.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmRXDROPRATIO.setStatus(
        "current"
    )

pmTXDROPRATIO = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 693)
)
pmTXDROPRATIO.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmTXDROPRATIO.setStatus(
        "current"
    )

pmPORTRXBWUTILIZATIONMIN = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 839)
)
pmPORTRXBWUTILIZATIONMIN.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmPORTRXBWUTILIZATIONMIN.setStatus(
        "current"
    )

pmPORTRXBWUTILIZATIONAVG = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 840)
)
pmPORTRXBWUTILIZATIONAVG.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmPORTRXBWUTILIZATIONAVG.setStatus(
        "current"
    )

pmPORTRXBWUTILIZATIONMAX = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 841)
)
pmPORTRXBWUTILIZATIONMAX.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmPORTRXBWUTILIZATIONMAX.setStatus(
        "current"
    )

pmPORTTXBWUTILIZATIONMIN = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 842)
)
pmPORTTXBWUTILIZATIONMIN.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmPORTTXBWUTILIZATIONMIN.setStatus(
        "current"
    )

pmPORTTXBWUTILIZATIONAVG = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 843)
)
pmPORTTXBWUTILIZATIONAVG.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmPORTTXBWUTILIZATIONAVG.setStatus(
        "current"
    )

pmPORTTXBWUTILIZATIONMAX = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 844)
)
pmPORTTXBWUTILIZATIONMAX.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmPORTTXBWUTILIZATIONMAX.setStatus(
        "current"
    )

pmPortrxbytesavailability868 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 868)
)
pmPortrxbytesavailability868.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"),
        ("OPTIX-GLOBAL-PM-TRAPS-MSTP-MIB", "rptEvtDataPmName"),
        ("OPTIX-GLOBAL-PM-TRAPS-MSTP-MIB", "rptEvtMonValue"),
        ("OPTIX-GLOBAL-PM-TRAPS-MSTP-MIB", "rptEvtThValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmPortrxbytesavailability868.setStatus(
        "current"
    )

pmPortrxbytesavailability869 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 869)
)
pmPortrxbytesavailability869.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"),
        ("OPTIX-GLOBAL-PM-TRAPS-MSTP-MIB", "rptEvtDataPmName"),
        ("OPTIX-GLOBAL-PM-TRAPS-MSTP-MIB", "rptEvtMonValue"),
        ("OPTIX-GLOBAL-PM-TRAPS-MSTP-MIB", "rptEvtThValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmPortrxbytesavailability869.setStatus(
        "current"
    )

pmRXPBAD = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 944)
)
pmRXPBAD.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmRXPBAD.setStatus(
        "current"
    )

pmTXPBAD = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 945)
)
pmTXPBAD.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmTXPBAD.setStatus(
        "current"
    )

pmRXPGOOD = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 946)
)
pmRXPGOOD.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmRXPGOOD.setStatus(
        "current"
    )

pmTXPGOOD = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 947)
)
pmTXPGOOD.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmTXPGOOD.setStatus(
        "current"
    )

pmRXBRDCASTRATIO = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 957)
)
pmRXBRDCASTRATIO.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmRXBRDCASTRATIO.setStatus(
        "current"
    )

pmTXBRDCASTRATIO = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20, 958)
)
pmTXBRDCASTRATIO.setObjects(
      *(("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    pmTXBRDCASTRATIO.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPTIX-GLOBAL-PM-TRAPS-MSTP-MIB",
    **{"optixTrapsPM": optixTrapsPM,
       "pmRisingAlarm": pmRisingAlarm,
       "pmFallingAlarm": pmFallingAlarm,
       "pmRXPKT64": pmRXPKT64,
       "pmRXPKT65": pmRXPKT65,
       "pmRXPKT128": pmRXPKT128,
       "pmRXPKT256": pmRXPKT256,
       "pmRXPKT512": pmRXPKT512,
       "pmRXPKT1024": pmRXPKT1024,
       "pmTXPKT64": pmTXPKT64,
       "pmTXPKT65": pmTXPKT65,
       "pmTXPKT128": pmTXPKT128,
       "pmTXPKT256": pmTXPKT256,
       "pmTXPKT512": pmTXPKT512,
       "pmTXPKT1024": pmTXPKT1024,
       "pmRXUNICAST": pmRXUNICAST,
       "pmRXMULCAST": pmRXMULCAST,
       "pmRXBRDCAST": pmRXBRDCAST,
       "pmTXUNICAST": pmTXUNICAST,
       "pmTXMULCAST": pmTXMULCAST,
       "pmTXBRDCAST": pmTXBRDCAST,
       "pmRXPAUSE": pmRXPAUSE,
       "pmTXPAUSE": pmTXPAUSE,
       "pmETHDROP": pmETHDROP,
       "pmETHUNDER": pmETHUNDER,
       "pmETHOVER": pmETHOVER,
       "pmETHFRG": pmETHFRG,
       "pmETHJAB": pmETHJAB,
       "pmRXBGOOD": pmRXBGOOD,
       "pmTXBGOOD": pmTXBGOOD,
       "pmRXBBAD": pmRXBBAD,
       "pmTXBBAD": pmTXBBAD,
       "pmETHALI": pmETHALI,
       "pmETHFCS": pmETHFCS,
       "pmRXPKT1519": pmRXPKT1519,
       "pmTXPKT1519": pmTXPKT1519,
       "pmPKT64": pmPKT64,
       "pmPKT65": pmPKT65,
       "pmPKT128": pmPKT128,
       "pmPKT256": pmPKT256,
       "pmPKT512": pmPKT512,
       "pmPKT1024": pmPKT1024,
       "pmPKT1519": pmPKT1519,
       "pmRXGOODFULLFRAMESPEED": pmRXGOODFULLFRAMESPEED,
       "pmTXGOODFULLFRAMESPEED": pmTXGOODFULLFRAMESPEED,
       "pmRxfullbgood": pmRxfullbgood,
       "pmTxfullbgood": pmTxfullbgood,
       "pmRXCTLPKTS": pmRXCTLPKTS,
       "pmTXCTLPKTS": pmTXCTLPKTS,
       "pmTXETHDROP": pmTXETHDROP,
       "pmTXETHOVER": pmTXETHOVER,
       "pmTXPKTS": pmTXPKTS,
       "pmTXOCTETS": pmTXOCTETS,
       "pmRXOCTETS": pmRXOCTETS,
       "pmRXPKTS": pmRXPKTS,
       "pmVCGRXOCTETS": pmVCGRXOCTETS,
       "pmVCGTXOCTETS": pmVCGTXOCTETS,
       "pmVCGRXPACKETS": pmVCGRXPACKETS,
       "pmVCGTXPACKETS": pmVCGTXPACKETS,
       "pmVCGRXGOODPACKETS": pmVCGRXGOODPACKETS,
       "pmVCGTXGOODPACKETS": pmVCGTXGOODPACKETS,
       "pmVCGRXSPEED": pmVCGRXSPEED,
       "pmVCGTXSPEED": pmVCGTXSPEED,
       "pmPORTRXBWUTILIZATION": pmPORTRXBWUTILIZATION,
       "pmPORTTXBWUTILIZATION": pmPORTTXBWUTILIZATION,
       "pmRXBPS": pmRXBPS,
       "pmTXBPS": pmTXBPS,
       "pmRXPPS": pmRXPPS,
       "pmTXPPS": pmTXPPS,
       "pmETHRXTHROUGHPUTMAX": pmETHRXTHROUGHPUTMAX,
       "pmETHRXTHROUGHPUTMIN": pmETHRXTHROUGHPUTMIN,
       "pmETHRXTHROUGHPUTAVG": pmETHRXTHROUGHPUTAVG,
       "pmETHTXTHROUGHPUTMAX": pmETHTXTHROUGHPUTMAX,
       "pmETHTXTHROUGHPUTMIN": pmETHTXTHROUGHPUTMIN,
       "pmETHTXTHROUGHPUTAVG": pmETHTXTHROUGHPUTAVG,
       "pmRXDROPRATIO": pmRXDROPRATIO,
       "pmTXDROPRATIO": pmTXDROPRATIO,
       "pmPORTRXBWUTILIZATIONMIN": pmPORTRXBWUTILIZATIONMIN,
       "pmPORTRXBWUTILIZATIONAVG": pmPORTRXBWUTILIZATIONAVG,
       "pmPORTRXBWUTILIZATIONMAX": pmPORTRXBWUTILIZATIONMAX,
       "pmPORTTXBWUTILIZATIONMIN": pmPORTTXBWUTILIZATIONMIN,
       "pmPORTTXBWUTILIZATIONAVG": pmPORTTXBWUTILIZATIONAVG,
       "pmPORTTXBWUTILIZATIONMAX": pmPORTTXBWUTILIZATIONMAX,
       "pmPortrxbytesavailability868": pmPortrxbytesavailability868,
       "pmPortrxbytesavailability869": pmPortrxbytesavailability869,
       "pmRXPBAD": pmRXPBAD,
       "pmTXPBAD": pmTXPBAD,
       "pmRXPGOOD": pmRXPGOOD,
       "pmTXPGOOD": pmTXPGOOD,
       "pmRXBRDCASTRATIO": pmRXBRDCASTRATIO,
       "pmTXBRDCASTRATIO": pmTXBRDCASTRATIO}
)
